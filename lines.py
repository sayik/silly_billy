import sys
import re

def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = 0
            for line in file:
                if not re.match(r'^\s*(#|$)', line):
                    line_count += 1
        return line_count
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading the file.")

# Check command line arguments
if len(sys.argv) != 2 or not sys.argv[1].endswith(".py"):
    sys.exit("Usage: python appname.py yourprogramname.py")

file_path = sys.argv[1]
lines = count_lines(file_path)
print("Number of lines (excluding comments and empty lines):", lines)
