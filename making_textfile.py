import os

# Define the textfiles path folder containing the all the text files
textfiles_path = "textfiles"

# Define the FaltFile path to the Flat file
FlatFile_path = "FlatFile.txt"

# Read the criteria from the opening the Faltfile path and use the fuction of the splitlines() is a method of the string object that splits the string into a list of strings, where each string represents a line in the original string. This method removes the newline character at the end of each line.
with open(FlatFile_path, "r") as Flat_file:
    criteria = Flat_file.read().splitlines()

# Define a dictionary to store the scores for each text file.
scores = {}

# Loop through the text files in the folder and use the os library os.listdir fuction and read the text.
for filename in os.listdir(textfiles_path):
    if filename.endswith(".txt"):
        filepath = os.path.join(textfiles_path, filename)
        with open(filepath, "r") as text_file:
            text = text_file.read()

        # Calculate the score for the file criteria.
        score = 0
        for c in criteria:
            if c in text:
                score += 1
        scores[filename] = score

# Sort the text files by score in descending order
sorted_files = sorted(scores, key=scores.get, reverse=True)

# Print the file names in order of priority
print("File names in order of priority:")
for i, filename in enumerate(sorted_files):
    print(f"{i+1}. {filename}")

# Select the first three files and print their justification
# Finally, I would select the top three text files and print out the justification  for why they were selected. The justification would depend on the specific requirements of the task, but might include information such as the specific criteria that each file scored well on, and how those criteria were weighted. For example, the justification might look something like this:
selected_files = sorted_files[:3]
print("\nSelected files and their justifications:")

# for this justify the top three file ranking on the custmors choice of the 55 inch tv.
for filename in selected_files:
    print(f"\nFilename: {filename}")
    justification = "My customer needs a 55-inch Size of tv, second one is LED, \n COLUR IN BLACK, and the Resolution should be 4K and 3840 x 2160 Pixels, Refresh Rate 60Hz"

    for c in criteria:
        if c in open(os.path.join(textfiles_path, filename)).read():
            justification += f"\n- Contains '{c}'"
    print(f"Justification of Television Key spaces: {justification}")

