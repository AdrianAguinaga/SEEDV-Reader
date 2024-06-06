# SEEDV-Reader
This script processes SEEDV data stored in multiple .npz files, concatenates specific subsets, labels them, and saves the results in CSV format(this file only uses 4 of the 5 emotions contained in SEEDV, in order to match the experiment. 

Steps:
Import Necessary Libraries:

numpy: For numerical operations.
pickle: For loading serialized data.
pandas: For handling data in DataFrame format.
os: For file and directory operations.
Define Paths:

input_folder: The directory containing the input .npz files.
output_folder: The directory where the output CSV files will be saved. The script ensures this directory exists.
Process Each File:

Loop through 16 files (1_123.npz to 16_123.npz).
For each file:
Load the data and labels using numpy and pickle.
Extract specific subsets of the data based on predefined indices for different emotional states (happy, neutral, sad, disgust).
Concatenate the subsets for each emotional state.
Add an extra column to each subset with a specific value to label the emotional state (0 for happy, 3 for neutral, 2 for sad, and 1 for disgust).
Combine all labeled subsets into a single array.
Convert the array to a pandas DataFrame with appropriate column names.
Save the DataFrame to a CSV file.
Combine All CSV Files:

Read all the generated CSV files.
Concatenate them into a single DataFrame, ignoring redundant headers.
Save the combined DataFrame to a final CSV file.
