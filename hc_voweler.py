import itertools

# Vowel frequency rankings for word lengths 6-15 (sorted from highest to lowest frequency)
VOWEL_PRIORITIES = {
    6: [2, 5, 4, 3, 6, 1],
    7: [2, 5, 6, 3, 4, 7, 1],
    8: [2, 6, 5, 4, 7, 3, 8, 1],
    9: [2, 7, 5, 6, 4, 8, 3, 9, 1],
    10: [2, 8, 5, 6, 9, 4, 7, 3, 10, 1],
    11: [2, 9, 7, 10, 5, 6, 8, 4, 3, 11, 1],
    12: [10, 2, 9, 8, 5, 6, 4, 7, 11, 3, 12, 1],
    13: [11, 2, 9, 8, 7, 10, 5, 6, 12, 4, 3, 13, 1],
    14: [12, 2, 10, 5, 8, 7, 6, 11, 9, 13, 4, 3, 14, 1],
    15: [13, 2, 10, 7, 5, 8, 9, 6, 11, 14, 4, 12, 3, 15, 1]
}

def has_too_many_consecutive_vowels(mask):
    """ Check if the mask has more than 3 consecutive vowels. """
    return "?1?1?1?1" in mask

def main():
    # Get user input
    try:
        length = int(input("What's the password length? "))
        vowels_count = int(input("How many vowel positions? "))
    except ValueError:
        print("Please enter valid integers.")
        return

    if length not in VOWEL_PRIORITIES:
        print("This script only supports password lengths between 6 and 15.")
        return

    if vowels_count < 0 or vowels_count > length:
        print("Vowel count must be between 0 and the total password length.")
        return

    casing = input("What casing for characters? (lower/upper/both): ").strip().lower()
    if casing not in ['lower', 'upper', 'both']:
        print("Invalid casing option. Please enter lower, upper, or both.")
        return

    # Assign charset files based on casing
    vowel_file = f"vowels_{casing}.hcchr"
    non_vowel_file = f"novowels_{casing}.hcchr"

    # Define charset references
    prefix = f"#HL# -w4 -O -a3 -1 {vowel_file} -2 {non_vowel_file} "

    # Get prioritized vowel positions for the given length
    vowel_priority_order = VOWEL_PRIORITIES[length]

    # Generate all unique combinations of `vowels_count` positions from the priority list
    valid_combinations = list(itertools.combinations(vowel_priority_order, vowels_count))

    output_lines = []
    
    for comb in valid_combinations:
        selected_vowel_positions = set(comb)

        # Build the mask pattern
        mask_parts = []
        for pos in range(1, length + 1):  # Positions are 1-based in the provided ranking
            if pos in selected_vowel_positions:
                mask_parts.append("?1")  # Vowel
            else:
                mask_parts.append("?2")  # Non-vowel

        mask_pattern = "".join(mask_parts)

        # Skip masks with too many consecutive vowels
        if has_too_many_consecutive_vowels(mask_pattern):
            continue

        # Store final formatted output
        output_lines.append(prefix + mask_pattern)

    # Write to output file
    with open("hc_voweler.txt", "w") as f:
        for line in output_lines:
            f.write(line + "\n")

    print(f"{len(output_lines)} mask commands written to hc_voweler.txt.")

if __name__ == "__main__":
    main()
