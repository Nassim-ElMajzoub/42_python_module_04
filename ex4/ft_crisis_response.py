#!/usr/bin/env python3


import sys


def ft_crisis_response(filename: str) -> None:

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
            print(f"SUCCESS: Archive recovered - ``{content}''")
            print("STATUS: Normal operations resumed\n")

    except FileNotFoundError:
        print(
            f"CRISIS ALERT: Attempting access to '{filename}'...",
            file=sys.stderr
        )
        print("RESPONSE: Archive not found in storage matrix", file=sys.stderr)
        print("STATUS: Crisis handled, system stable\n", file=sys.stderr)

    except PermissionError:
        print(
            f"CRISIS ALERT: Attempting access to '{filename}'...",
            file=sys.stderr
        )
        print("RESPONSE: Security protocols deny access", file=sys.stderr)
        print("STATUS: Crisis handled, security maintained\n", file=sys.stderr)

    except OSError as e:
        print(e, file=sys.stderr)


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    ft_crisis_response('lost_archive.txt')
    ft_crisis_response('classified_vault.txt')
    ft_crisis_response('standard_archive.txt')

    print("All crisis scenarios handled successfully. Archives secure.")
