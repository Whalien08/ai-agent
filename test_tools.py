from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

print("--- Testing Tool 1: Listing Calculator Root ---")
print(get_files_info(working_dir="calculator"))

print("\n--- Testing Tool 2: Reading main.py ---")
print(get_file_content(working_dir="calculator", file_path="main.py"))