import os
import subprocess

def run_python_file(working_dir: str, file_path: str, args: list[str] = None) -> str:
    """
    Runs a Python file using the environment's interpreter with a 30s timeout.
    Captures stdout and stderr for the LLM to inspect.
    """
    abs_working = os.path.abspath(working_dir)
    target_file = os.path.join(abs_working, file_path)
    abs_file = os.path.abspath(target_file)
    
    if not abs_file.startswith(abs_working):
        return f"Error: Access denied. '{file_path}' is outside the project root."
        
    if not os.path.exists(abs_file):
        return f"Error: File '{file_path}' not found."
        
    if not file_path.endswith(".py"):
        return f"Error: '{file_path}' is not a Python file."
        
    cmd = ["python", abs_file]
    if args:
        cmd.extend(args)
        
    try:
        result = subprocess.run(
            cmd,
            cwd=abs_working,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        output = []
        if result.stdout:
            output.append(f"[STDOUT]\n{result.stdout}")
        if result.stderr:
            output.append(f"[STDERR]\n{result.stderr}")
            
        final_str = "\n".join(output)
        return final_str if final_str.strip() else "Execution finished with no output."
    except subprocess.TimeoutExpired:
        return "Error: Execution timed out after 30 seconds."
    except Exception as e:
        return f"Error executing script: {str(e)}"