"""
Task 1: Copy and Sort Files by Extension
"""

import os
import shutil
import sys

def copy_files(src_dir, dest_dir):
    """
    Recursively copies files from src_dir to dest_dir, 
    sorting them into subdirectories based on their extensions.
    """
    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        if os.path.isdir(src_path):
            new_dest_dir = os.path.join(dest_dir, item)
            os.makedirs(new_dest_dir, exist_ok=True)
            copy_files(src_path, new_dest_dir)
        else:
            try:
                file_ext = os.path.splitext(item)[1][1:].lower()
                ext_dir = os.path.join(dest_dir, file_ext)
                os.makedirs(ext_dir, exist_ok=True)
                shutil.copy2(src_path, os.path.join(ext_dir, item))
            except OSError as e:
                print(f"Oopsie: {e}")
                sys.exit(1)

def main():
    """
    Main function to parse arguments and start the file copying and sorting process.
    """
    if len(sys.argv) < 2:
        print("Usage: python script.py <source_dir> [destination_dir]")
        sys.exit(1)

    src_dir = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"

    os.makedirs(dest_dir, exist_ok=True)
    copy_files(src_dir, dest_dir)

    print(f"Files have been copied and sorted into {dest_dir}.")

if __name__ == "__main__":
    main()
