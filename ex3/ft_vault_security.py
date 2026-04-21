#!/usr/bin/env python3


def secure_archive(file_name: str,
                   action: str = 'r',
                   content: str | None = None) -> tuple[bool, str]:

    if action not in ['r', 'w']:
        return (
            False,
            "Error: invalid action! Enter 'r' for read or 'w' for write!"
        )

    if action == 'w' and content is None:
        return (
            False,
            "Can't write to file. No content is provided to write."
        )

    try:
        with open(file_name, action) as file:
            if action == 'r':
                return (True, file.read())
            else:
                file.write(content)
                return (True, 'Content successfully written to file')
    except (FileNotFoundError, PermissionError) as e:
        return (False, str(e))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive('/not/existing/file'))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive('inaccessible_file', 'r'))

    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive('ancient_fragment.txt'))

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive('new_fargments.txt', 'w', 'new archive'))
