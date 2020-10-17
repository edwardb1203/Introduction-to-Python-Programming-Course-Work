import sys

from typing import List, Dict

# args: List[str] = sys.argv
# print(len(args))
# print(args[1])
# print(args[2])

def main() -> None:
    """Entrypoint of program run as module."""
    args: Dict[str, str] = read_args()
    results: List[str] = search_file(args["file_path"], args["keyword"])
    shows_results(results)
    print(len(results))
    ...


def read_args() -> Dict[str, str]:
    """Check for valid CLI arguments and return them in a dictionary."""
    if len(sys.argv) != 3:
        print("Usage: python -m lessons.ls29_cli_args [file] [keyword]")
        exit()
    return {
        "file_path": sys.argv[1],
        "keyword": sys.argv[2]

    }

def search_file(file_path: str, keyword: str) -> List[str]:
    """Opens and reads file_path, returns a List of lines w/ keyword."""
    matches: List[str] = []
    file_handle = open(file_path, "r",  encoding="utf8")
    for line in file_handle:
        if keyword in line:
            matches.append(line)
    file_handle.close()
    return matches


def show_results(matches: List[str]) -> None:
    """Print out matching lines and total number of matches."""
    for line in matches:
        print(line.strip())

    print("Total matches: " + str(len(matches)))







# Run our program as a module with two command-line arguments:
# 1. Name of the file to search 
# 2. Search term we're looking for
# Print out all lines containing the search term and total
# number of matches.

if __name__ == "__main__":
    main()
