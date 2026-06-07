import os

def get_file_content(working_dir: str, file_path: str) -> str:
    """
    Reads the full content of a file within the working directory.
    Truncates content to prevent overloading the LLM's token boundaries.
    """
    abs_working = os.path.abspath(working_dir)
    target_file = os.path.join(abs_working, file_path)
    abs_file = os.path.abspath(target_file)
    
    # Safety Check: Prevent directory traversal hacking
    if not abs_file.startswith(abs_working):
        return f"Error: Access denied. '{file_path}' is outside the project root."
        
    if not os.path.exists(abs_file):
        return f"Error: File '{file_path}' not found."
        
    if os.path.isdir(abs_file):
        return f"Error: '{file_path}' is a directory, cannot read content."
        
    # Read text with a 10,000 character circuit breaker
    try:
        with open(abs_file, "r", encoding="utf-8") as f:
            content = f.read(10000)
            if len(content) >= 10000:
                content += "\n\n... [File truncated at 10,000 characters to optimize token metrics] ..."
            return content
    except Exception as e:
        return f"Error reading file: {str(e)}"