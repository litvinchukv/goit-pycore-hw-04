import sys
from pathlib import Path
from colorama import init, Fore, Style

def list_directory(path, level=0):
    try:
        entries = sorted(Path(path).iterdir(), key=lambda e: (e.is_file(), e.name))
        for entry in entries:
            indent = ' ' * (level * 4)
            if entry.is_dir():
                print(f"{indent}{Fore.BLUE}{entry.name}{Style.RESET_ALL}/")
                list_directory(entry, level + 1)
            else:
                print(f"{indent}{Fore.GREEN}{entry.name}{Style.RESET_ALL}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    init(autoreset=True)

    if len(sys.argv) != 2:
        print("Usage: python task_3.py <path_to_directory>")
        sys.exit(1)

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(f"Error: The directory '{directory_path}' does not exist.")
        sys.exit(1)

    if not directory_path.is_dir():
        print(f"Error: The path '{directory_path}' is not a directory.")
        sys.exit(1)

    print(f"{Fore.BLUE}{directory_path.name}{Style.RESET_ALL}/")
    list_directory(directory_path, 1)

if __name__ == "__main__":
    main()
