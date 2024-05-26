import re
import os

def preprocess(source_code):
    comment_pattern = re.compile(r'#.*')
    preprocessed_code = re.sub(comment_pattern, '', source_code)
    preprocessed_code = '\n'.join(line for line in preprocessed_code.split('\n') if line.strip() != '')
    return preprocessed_code

def read_file(file_path):
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist. Please create the file and try again.")
        return None
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

input_file = 'code.txt'
output_file = 'preprocessed_code.txt'

source_code = read_file(input_file)

if source_code is not None:
    preprocessed_code = preprocess(source_code)
    write_file(output_file, preprocessed_code)
    print("Preprocessing is complete. The code without comments is written to 'preprocessed_code.txt'.")