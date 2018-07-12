import argparse
from pathlib import Path


def parse_command_line_args():
    parser = argparse.ArgumentParser(
        prog='duplicate_file_finder.py',
        description=
"""
description:
Find duplicate files/directories within a specified directory and its subdirectories.
"""
,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        'search_dir',
        help='Path of the directory to search. Subdirectories are searched as well.'
    )

    return parser.parse_args()


def find_duplicate_name_paths(command_line_args):
    duplicate_name_paths = set()
    all_paths = list(Path(command_line_args.search_dir).glob('**/*'))

    for path in all_paths:
        for target_path in all_paths:
            if path != target_path and path.name == target_path.name:
                duplicate_name_paths.add(path)
                duplicate_name_paths.add(target_path)
    
    return duplicate_name_paths


def main():
    command_line_args = parse_command_line_args()
    duplicate_name_paths = find_duplicate_name_paths(command_line_args)
    for path in duplicate_name_paths:
        print(path)


if __name__ == '__main__':
    main()