import argparse
from pathlib import Path


def parse_command_line_arguments():
    parser = argparse.ArgumentParser(
        prog='duplicate_file_finder.py',
        usage='Find duplicate files/directories and display them.',
        add_help=True
    )

    args = parser.parse_args()


def find_duplicate_name_paths():
    duplicate_name_paths = set()
    all_paths = list(Path('.').glob('**/*'))

    for path in all_paths:
        for target_path in all_paths:
            if path != target_path and path.name == target_path.name:
                duplicate_name_paths.add(path)
                duplicate_name_paths.add(target_path)
    
    return duplicate_name_paths


def main():
    parse_command_line_arguments()
    duplicate_name_paths = find_duplicate_name_paths()
    for path in duplicate_name_paths:
        print(path)


if __name__ == '__main__':
    main()