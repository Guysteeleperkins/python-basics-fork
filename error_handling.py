from pathlib import Path

cwd = Path.cwd()

demo_file_path = cwd / 'demo_files' / 'my_data.txt'

# file = open(demo_file_path)

# print(demo_file_path)

try:
    file = open(demo_file_path)
except TypeError as te:
    print(f'TypeError: {te}')
except FileNotFoundError as fnf:
    print(f'FileNotFoundError: {fnf}')
except Exception as e:
    print(f'Exception: {e}')
finally:
    if file:
        file.close()
    print("Continuing with the rest of the program")
