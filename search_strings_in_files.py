import os
import argparse

def search_strings_in_files(file_extension, directory, strings_file):
    # Validate arguments
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return

    # Read the list of strings from the file
    with open(strings_file, 'r') as file:
        search_strings = file.read().strip().split(',')

    # Iterate through files in the directory
    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith(file_extension):
                file_path = os.path.join(root, file_name)

                # Open the file and search for strings
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                    content = file.read()
                    for search_string in search_strings:
                        if search_string in content:
                            print(f"Found '{search_string}' in {file_path}")

def main():
    parser = argparse.ArgumentParser(description="Search for strings in files under a specified directory.")
    parser.add_argument("-e", "--extension", required=True, help="File extension to search")
    parser.add_argument("-d", "--directory", required=True, help="Directory to search")
    parser.add_argument("-f", "--strings-file", required=True, help="File containing comma-separated list of strings to search for")

    args = parser.parse_args()
    file_extension = args.extension
    directory = args.directory
    strings_file = args.strings_file

    search_strings_in_files(file_extension, directory, strings_file)

if __name__ == "__main__":
    main()
