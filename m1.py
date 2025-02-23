'''from datasets import load_dataset

# Load the dataset
dataset = load_dataset("shb777/wiki-en-in-neerja-speech")

# Print dataset information (optional, but good to check)
print(dataset)

# Save the entire dataset to disk
dataset.save_to_disk("neerja_speech_dataset")  # Choose your desired directory name

print("Dataset downloaded and saved to 'neerja_speech_dataset' directory.")'''

from datasets import load_from_disk

loaded_dataset = load_from_disk("neerja_speech_dataset") # Use the directory name you used when saving
print(loaded_dataset)
print(loaded_dataset['train'][1]) # Assuming there's a 'train' split, check the first example