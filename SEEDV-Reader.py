"""
Create by AdrianRA
"""
import numpy as np
import pickle
import pandas as pd
import os

# Path to the input folder
input_folder = r'FilePath\EEG_DE_features'
output_folder = r'FilePath\EEG_DE_features\output'

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Loop to process 16 files
for i in range(1, 17):
    file_name = f'{i}_123.npz'
    file_path = os.path.join(input_folder, file_name)
    
    data_npz = np.load(file_path)
    
    # Get data and label
    data = pickle.loads(data_npz['data'])
    label = pickle.loads(data_npz['label'])
    
    # Indices of the arrays to concatenate
    indices_happy = [0, 5, 10, 19, 20, 26, 34, 35, 41]
    indices_neutral = [2, 7, 12, 17, 22, 25, 32, 37, 40]
    indices_sad = [3, 8, 13, 15, 23, 28, 30, 38, 43]
    indices_disgust = [4, 9, 14, 18, 21, 29, 33, 36, 44]
    
    # Create new arrays by concatenating the specific ones
    happy_array = np.concatenate([data[j] for j in indices_happy])
    neutral_array = np.concatenate([data[j] for j in indices_neutral])
    sad_array = np.concatenate([data[j] for j in indices_sad])
    disgust_array = np.concatenate([data[j] for j in indices_disgust])
    
    # Add an extra column to each array with the specific values
    happy_array = np.column_stack((happy_array, np.zeros(happy_array.shape[0])))
    neutral_array = np.column_stack((neutral_array, np.full(neutral_array.shape[0], 3)))
    sad_array = np.column_stack((sad_array, np.full(sad_array.shape[0], 2)))
    disgust_array = np.column_stack((disgust_array, np.ones(disgust_array.shape[0])))
    
    # Concatenate all arrays into one
    ClassificationData = np.vstack((happy_array, neutral_array, sad_array, disgust_array))
    
    # Convert the array to a pandas DataFrame
    column_names = [f"Feature_{k}" for k in range(ClassificationData.shape[1] - 1)] + ["Class"]
    df = pd.DataFrame(ClassificationData, columns=column_names)
    
    # Save the DataFrame to a CSV file
    output_csv = os.path.join(output_folder, f'ClassificationData_{i}.csv')
    df.to_csv(output_csv, index=False)
    
    print(f'File saved: {output_csv}')

# Combine all CSV files into one
combined_csv_path = os.path.join(output_folder, 'ClassificationData_Combined.csv')

# Read all generated CSV files
csv_files = [os.path.join(output_folder, f'ClassificationData_{i}.csv') for i in range(1, 17)]
df_list = [pd.read_csv(file) for file in csv_files]

# Concatenate all DataFrames, ignoring redundant headers
combined_df = pd.concat(df_list, ignore_index=True)

# Save the combined DataFrame to a CSV file
combined_df.to_csv(combined_csv_path, index=False)

print(f'Combined file saved: {combined_csv_path}')
