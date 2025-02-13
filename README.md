# HC Voweler - Optimized Hashcat Brute Force Masks

## Overview
This project contains three Python scripts designed to generate optimized brute-force masks for **Hashcat** based on real-world vowel frequency analysis in words of different lengths. The goal is to improve efficiency by prioritizing vowel positions in generated masks, reducing the number of total brute-force attempts.

## Files & Their Purpose

### `hc_voweler.py`
**Purpose:**  
Generates Hashcat mask files (`hc_voweler.txt`) by strategically placing vowels in high-frequency positions within words of a given length.

**How it Works:**
- Asks the user for:
  - Password length (6-15 characters)
  - Number of vowels to include
  - Character casing (lowercase, uppercase, or both)
- Uses pre-analyzed **vowel frequency rankings** to place vowels in positions where they are most commonly found in real words.
- Outputs multiple masks that follow the priority order, ensuring vowels are spread out optimally.
- Masks with **more than 3 consecutive vowels** are **excluded** to avoid unnecessary computations.
- Outputs the masks in a format optimized for Hashcat.

**Example Usage:**
```sh
$ python hc_voweler.py
What's the password length? 6
How many vowel positions? 2
What casing for characters? lower
#HL# -w4 -O -a3 -1 vowels_lower.hcchr -2 novowels_lower.hcchr ?2?1?2?2?1?2
#HL# -w4 -O -a3 -1 vowels_lower.hcchr -2 novowels_lower.hcchr ?2?1?2?1?2?2
...


words.py → Splits words into individual files by length.
vowelanalysis.py → Analyzes which positions vowels are most common.
hc_voweler.py → Uses the analysis to optimize brute-force masks for Hashcat.

$ python vowelanalysis.py
Analysis for words_6letters.txt:
  1   |   2   |   3   |   4   |   5   |   6
------------------------------------
 18% |  65% |  31% |  40% |  53% |  26%


$ python words.py
Processing completed. Shortest word length: 2, Longest word length: 15
words_6letters.txt
words_7letters.txt
words_8letters.txt
...
