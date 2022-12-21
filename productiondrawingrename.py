import os
import glob
import re


# Specify the directory containing the files
directory = 'enter folder path here'

# This next section will get rid of all extra, unneeded characters and replace them with spaces
files = os.listdir(directory)

for file in files:
 
  filename, file_extension = os.path.splitext(file)
  
  # Replace underscores, periods, and dashes with spaces
  new_filename = filename.replace('_', ' ').replace('.', ' ').replace('-', ' ')
  
  # Construct the new file name with the original extension
  new_file = new_filename + file_extension
  
  os.replace(os.path.join(directory, file), os.path.join(directory, new_file))

# This section will make all version of the word "Rev", the same capitalization
for filename in os.listdir(directory):
    # Check if the string 'REV' is present in the file name
    if 'REV' in filename:
        # Replace 'REV' with 'Rev'
        new_filename = filename.replace('REV', 'Rev')

        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

# This section will look for any time the string 'Rev' has two spaces after, and make the second space a dash
for filename in os.listdir(directory):
  if 'Rev  ' in filename:
    parts = filename.split('Rev  ')
    # Create a new filename by joining the parts with a space and a dash
    new_filename = parts[0] + 'Rev - ' + parts[1]

    os.replace(os.path.join(directory, filename), os.path.join(directory, new_filename))

# This section will get rid of any extra spaces in the file names
for file in glob.glob(f'{directory}/*'):
    # Get the current file name and split it into a list of words
    current_name = os.path.basename(file)
    words = current_name.split()
    # Join the words together with a single space as a separator
    new_name = ' '.join(words)
    # Use the re module to replace multiple spaces with a single space
    new_name = re.sub(' +', ' ', new_name)
    # Check if the new name is different from the current name
    if new_name != current_name:

        os.rename(file, f'{directory}/{new_name}')

# This section will look for two number with a space between them after the 'Rev' string, there is supposed to be a period in between these numbers, 
# but it had to be deleted when taking out all of the extra characters
for filename in os.listdir(directory):
    # Check if the 14th character is a space
    if filename[13] == ' ':
        # Check if the 13th and 15th characters are digits
        if filename[12].isdigit() and filename[14].isdigit():
            # Split the filename into two parts around the 14th character
            part1 = filename[:13]
            part2 = filename[14:]
            # Construct the new filename with a period instead of a space
            new_filename = part1 + '.' + part2
            # Rename the file
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

# In this section, the program will delete all dashed that are not directly followed by a 'VCN' string. Earlier in the program there was a function that added a dash everytime there was too spaces after the 'Rev' string.
# This created unneccasary dashes in filenames that acutally had revisions, so this cleans up that error.
files = os.listdir(directory)

for file in files:
  # Check if the file name contains a dash followed by a space and any letter that is not v
  if '- ' and not '- V' in file:
    # Split the file name and extension into separate variables
    name, extension = os.path.splitext(file)
    # Replace the dash with an empty string
    new_name = name.replace('- ', '')
    # Create the new file name with the modified name and the original extension
    new_file = new_name + extension
    
    os.replace(os.path.join(directory, file), os.path.join(directory, new_file))

# This section makes sure there is still a dash after 'Rev' strings that aren't followed by a 'VCN'. 
# There was originally a problem that if the 'Rev' string was at the end of the filename, it wasn't followed by two spaces, therefore the previous code didn't apply.
folder_path = 'enter folder path here'
os.chdir(folder_path)

for file in os.listdir():
 
  name, extension = os.path.splitext(file)
  # Check if the file name has 12 characters
  if len(name) == 12:
    # Add a dash as the 13th character
    new_name = name[:12] + '-' + extension

    os.rename(file, new_name)
  # Check if the file name has at least 13 characters
  elif len(name) >= 13:
    # Check if the 13th character of the name is a space
    if name[12] == ' ':
      # Replace the 13th character with a dash
      new_name = name[:12] + '-' + extension
      # Rename the file
      os.rename(file, new_name)

print("Finished manipulating file names")
