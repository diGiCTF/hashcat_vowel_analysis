import os

# Define the directory containing the word files
directory = "./words"
vowels = set("aeiou")

# Check if the directory exists
if not os.path.exists(directory):
    print(f"Error: The directory '{directory}' was not found.")
else:
    # Process each text file in the directory
    for filename in sorted(os.listdir(directory)):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)

            # Read words from the file
            with open(file_path, "r", encoding="utf-8") as file:
                words = [line.strip().lower() for line in file if line.strip()]

            if not words:
                print(f"Skipping {filename}, no words found.")
                continue

            # Determine the maximum word length in this file
            max_length = max(len(word) for word in words)

            # Initialize vowel count and total words per position
            vowel_counts = [0] * max_length
            total_counts = [0] * max_length

            # Analyze vowel positions
            for word in words:
                for index, char in enumerate(word):
                    total_counts[index] += 1
                    if char in vowels:
                        vowel_counts[index] += 1

            # Compute vowel usage percentages
            percentages = [
                (vowel_counts[i] / total_counts[i]) * 100 if total_counts[i] > 0 else 0
                for i in range(max_length)
            ]

            # Print results in a formatted table
            print(f"\nAnalysis for {filename}:")
            print(" | ".join(f"{i+1:^5}" for i in range(max_length)))
            print("-" * (6 * max_length))
            print(" | ".join(f"{percent:.0f}%".rjust(5) for percent in percentages))
