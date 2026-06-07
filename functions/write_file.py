import os

def write_file(working_dir: str, file_path: str, content: str) -> str:
    """
    Overwrites or creates a file with the provided text string content.
    Strictly restricted to the working directory.
    """
    abs_working = os.path.abspath(working_dir)
    target_file = os.path.join(abs_working, file_path)
    abs_file = os.path.abspath(target_file)
    
    if not abs_file.startswith(abs_working):
        return f"Error: Access denied. '{file_path}' is outside the project root."
        
    try:
        # Create parent directories if they don't exist
        os.makedirs(os.path.dirname(abs_file), exist_ok=True)
        
        with open(abs_file, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Success: Successfully wrote {len(content)} characters to '{file_path}'."
    except Exception as e:
        return f"Error writing to file: {str(e)}"