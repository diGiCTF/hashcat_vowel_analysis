import os

# Define the file path
file_path = "words_alpha.txt"

# Check if the file exists
if not os.path.exists(file_path):
    print(f"Error: The file '{file_path}' was not found in the current directory.")
else:
    word_length_dict = {}

    # Read words from the file
    with open(file_path, "r", encoding="utf-8") as file:
        words = [line.strip() for line in file]

    # Find the shortest and longest word lengths
    word_lengths = [len(word) for word in words]
    min_length = min(word_lengths)
    max_length = max(word_lengths)

    # Organize words by length
    for word in words:
        length = len(word)
        if length not in word_length_dict:
            word_length_dict[length] = []
        word_length_dict[length].append(word)

    # Create new text files based on word length
    for length, words in word_length_dict.items():
        output_file = f"words_{length}letters.txt"
        with open(output_file, "w", encoding="utf-8") as file:
            file.write("\n".join(words))

    # Print the results
    print(f"Processing completed. Shortest word length: {min_length}, Longest word length: {max_length}")
