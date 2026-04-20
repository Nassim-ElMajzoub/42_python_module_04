#!/usr/bin/env python3


import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            file = open(sys.argv[1], 'r')
            original_content = file.read()
            print("---")
            print(original_content)
            print("---")
            file.close()
            print(f"File '{sys.argv[1]}' closed.")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
            original_content = str()

        if original_content:
            print("\nTransform data:")

            new_content = str()
            for line in original_content.splitlines():
                new_content = new_content + line + '#\n'
            print("---\n")
            print(new_content)
            print("---")

            name = input("Enter new file name (or empty): ")
            if not name:
                print("Not saving data.")
            else:
                try:
                    file = open(name, 'w')
                    print(f"Saving data to '{name}'")
                    file.write(new_content)
                    file.close()
                    print(f"Data saved in file '{name}'")
                except OSError as e:
                    print(f"Error writing to file: {e}")
