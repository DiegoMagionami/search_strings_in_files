```markdown
# File Search Script

This Python script searches for a list of strings in all files under a specified directory.

## Usage

```bash
python script.py -e <file_extension> -d <directory> -f <strings_file>
```

### Options

- `-e, --extension`: Specify the file extension to search for.
- `-d, --directory`: Specify the directory where the script will search for files.
- `-f, --strings-file`: Specify the file containing a comma-separated list of strings to search for in the files.

## Example

```bash
python script.py -e txt -d /path/to/directory -f strings.txt
```

This example searches for occurrences of the strings listed in the `strings.txt` file within all text files (`.txt`) under the specified directory.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:

```bash
git clone https://github.com/DiegoMagionami/search_strings_in_files.git
```

2. Navigate to the script's directory:

```bash
cd file-search-script
```

3. Run the script with the appropriate options.

## License

This script is provided under the [MIT License](LICENSE).
