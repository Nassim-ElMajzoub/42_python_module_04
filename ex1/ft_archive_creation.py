#!/usr/bin/env python3


def ft_archive_creation() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print("Initializing new storage unit: new_discovery.txt")

    entries = [
        "[ENTRY 001] New quantum algorithm discovered\n",
        "[ENTRY 002] Efficiency increased by 347%\n",
        "[ENTRY 003] Archived by Data Archivist trainee"
    ]

    try:
        file = open('new_discovery.txt', 'w')
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        try:
            for entry in entries:
                file.write(entry)
        except ValueError as e:
            print(f"{e}")
        finally:
            file.close()
        try:
            file = open('new_discovery.txt', 'r')
            print(file.read())
            print("\nData inscription complete. Storage unit sealed.")
            print("Archive 'new_discovery.txt' "
                  "ready for long-term preservation.")
        except OSError as e:
            print(f"Can't read file: {e}")
        finally:
            file.close()
    except OSError as e:
        print(f"Can't write to file: {e}")


if __name__ == "__main__":
    ft_archive_creation()
