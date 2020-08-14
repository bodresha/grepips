import requests
import oyaml as yaml
import sys
import os

INPUT_FILE_NAME = sys.argv[1] #'config.yaml'
URL=sys.argv[2] #"https://raw.githubusercontent.com/BBerastegui/fresh-dns-servers/master/resolvers.txt"

print('downloading data...')
r = requests.get(URL)

print('processing data...')
response_text = r.text
new_ips = []
for txt in response_text.splitlines():
    new_ips.append(txt)

print('read yaml file...')
yaml_dict = {}

with open(INPUT_FILE_NAME) as file:
    documents = yaml.full_load(file)
    documents['resolvers'] = new_ips
    
print('write yaml file with processed data...')
with open(INPUT_FILE_NAME, 'w') as file:
    d = yaml.dump(documents, file, indent=4)

old_string = '- '
new_string = '    - '

# Safely read the input filename using 'with'
with open(INPUT_FILE_NAME) as f:
    s = f.read()

# Safely write the changed content, if found in the file
with open(INPUT_FILE_NAME, 'w') as f:
    s = s.replace(old_string, new_string)
    s += '.'
    f.write(s)


with open(INPUT_FILE_NAME, "r+", encoding = "utf-8") as file:

    # Move the pointer (similar to a cursor in a text editor) to the end of the file
    file.seek(0, os.SEEK_END)

    # This code means the following code skips the very last character in the file -
    # i.e. in the case the last line is null we delete the last line
    # and the penultimate one
    pos = file.tell() - 1

    # Read each character in the file one at a time from the penultimate
    # character going backwards, searching for a newline character
    # If we find a new line, exit the search
    while pos > 0 and file.read(1) != "\n":
        pos -= 1
        file.seek(pos, os.SEEK_SET)

    # So long as we're not at the start of the file, delete all the characters ahead
    # of this position
    if pos > 0:
        file.seek(pos, os.SEEK_SET)
        file.truncate()



        
print('completed...')
