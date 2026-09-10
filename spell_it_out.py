word = input("Enter a word: ")

print("\nLetters:")
for letter in word:
    print(letter)

print("\nNumbered letters:")
counter = 1

for letter in word:
    print(f"{counter}. {letter}")
    counter += 1

print(f"\nThe word has {len(word)} letters.")
Example run

If the user enters PYTHON, the result will be:

Enter a word: PYTHON

Letters:
P
Y
T
H
O
N

Numbered letters:
1. P
2. Y
3. T
4. H
5. O
6. N

The word has 6 letters.
This program uses:

The first for loop to print each letter.
The second for loop plus counter to number each letter.
len(word) to count the total letters.
