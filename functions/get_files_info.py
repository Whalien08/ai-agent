import os

def get_files_info(working_dir: str, directory: str = ".") -> str:
    """
    Returns a string listing all files/directories, their sizes, 
    and whether they are folders. Strictly restricted to the working directory.
    """
    # 1. Resolve absolute paths for security guardrails
    abs_working = os.path.abspath(working_dir)
    
    # Target directory is relative to the working directory
    target_path = os.path.join(abs_working, directory)
    abs_target = os.path.abspath(target_path)
    
    # Safety Check: Block the LLM if it tries to escape using '../'
    if not abs_target.startswith(abs_working):
        return f"Error: Access denied. Directory '{directory}' is outside the project root."
        
    if not os.path.exists(abs_target):
        return f"Error: Directory '{directory}' does not exist."
        
    if not os.path.isdir(abs_target):
        return f"Error: '{directory}' is a file, not a directory."
        
    # 2. Crawl the directory
    try:
        items = os.listdir(abs_target)
        output = []
        for item in items:
            full_path = os.path.join(abs_target, item)
            is_folder = os.path.isdir(full_path)
            size = os.path.getsize(full_path)
            output.append(f"- Name: {item} | Size: {size} bytes | Directory: {is_folder}")
            
        return "\n".join(output) if output else "Directory is empty."
    except Exception as e:
        return f"Error listing directory: {str(e)}"