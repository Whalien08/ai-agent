import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
import time

# Import the structural operations
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def main():
    load_dotenv()
    
    if not os.environ.get("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY is missing from environment variables!")
        sys.exit(1)
        
    if len(sys.argv) < 2:
        print("Usage: python main.py \"<instruction>\" [--verbose]")
        sys.exit(1)
        
    user_prompt = sys.argv[1]
    # This checks if '--verbose' is anywhere in the command arguments
    verbose_flag = "--verbose" in sys.argv
        
    client = genai.Client()
    working_dir = "calculator"
    
    # Define our manual mappings to execute functions during tool calls
    tool_map = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "write_file": write_file,
        "run_python_file": run_python_file
    }

    # Register tool structural declarations to map cleanly into Gemini's configuration
    tools = [
        types.FunctionDeclaration(
            name="get_files_info",
            description="Lists files and directories inside the target directory.",
            parameters=types.Schema(
                type="OBJECT",
                properties={
                    "directory": types.Schema(type="STRING", description="Relative path within project. Defaults to '.'")
                }
            )
        ),
        types.FunctionDeclaration(
            name="get_file_content",
            description="Reads the text content of a specified file.",
            parameters=types.Schema(
                type="OBJECT",
                properties={
                    "file_path": types.Schema(type="STRING", description="Relative file path to read.")
                },
                required=["file_path"]
            )
        ),
        types.FunctionDeclaration(
            name="write_file",
            description="Writes or overwrites content into a file.",
            parameters=types.Schema(
                type="OBJECT",
                properties={
                    "file_path": types.Schema(type="STRING", description="Relative file path to write."),
                    "content": types.Schema(type="STRING", description="Full text to write into the file.")
                },
                required=["file_path", "content"]
            )
        ),
        types.FunctionDeclaration(
            name="run_python_file",
            description="Runs a Python script file and monitors stdout/stderr outputs.",
            parameters=types.Schema(
                type="OBJECT",
                properties={
                    "file_path": types.Schema(type="STRING", description="Relative path of the Python file."),
                    "args": types.Schema(
                        type="ARRAY", 
                        items=types.Schema(type="STRING"), 
                        description="Optional argument list strings."
                    )
                },
                required=["file_path"]
            )
        )
    ]

    system_prompt = (
        "You are an autonomous AI coding agent capable of diagnosing, modifying, and proving "
        "fixes on a local codebase. You must explore the codebase structural path, locate issues, "
        "verify changes by running tests, and provide a short overview text when completed."
    )

    # Initialize conversation history with structural tracking
    messages = [types.Content(role="user", parts=[types.Part.from_text(text=user_prompt)])]
    
    config = types.GenerateContentConfig(
        system_instruction=system_prompt,
        tools=[types.Tool(function_declarations=tools)],
    )
    
    print("Agent engine initialized. Executing task loop...")
    
    max_iterations = 15
    for iteration in range(max_iterations):
        time.sleep(5)
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=messages,
            config=config
        )
        
        if verbose_flag and response.usage_metadata:
            print(f"\n[Iteration {iteration+1} Metrics] Total Tokens Used: {response.usage_metadata.total_token_count}")

        # Extract model choice or text response
        function_calls = response.function_calls
        
        # If the model didn't ask for a tool, it has provided its final text explanation!
        if not function_calls:
            print(f"\n[Agent Final Response]:\n{response.text}")
            break
            
        # If it generated function actions, append the model's message choice to context history
        for candidate in response.candidates:
            if candidate.content:
                messages.append(candidate.content)
                
        # Execute the required functions sequentially
        for call in function_calls:
            func_name = call.name
            func_args = dict(call.args)
            
            print(f" -> AI requesting tool execution: {func_name}({func_args})")
            
            # Dynamically grab function reference and inject standard workspace context safely
            if func_name in tool_map:
                target_func = tool_map[func_name]
                execution_result = target_func(working_dir=working_dir, **func_args)
                
                # Format execution logs cleanly back into Gemini tracking history formats
                messages.append(
                    types.Content(
                        role="tool",
                        parts=[
                            types.Part.from_function_response(
                                name=func_name,
                                response={"result": execution_result}
                            )
                        ]
                    )
                )
            else:
                print(f"Error: Tool name '{func_name}' matched no registered implementations.")

if __name__ == "__main__":
    main()
#---

### Step 4: Let's Break the Calculator and Watch the Agent Fix It!

#To see your agent work its magic, let's break the calculator exactly like Lane does in the video:

#1. Open your **`calculator/pkg/calculator.py`** file.
#2. Find the `get_precedence` function around line 7, and temporarily break the precedence rules by raising addition/subtraction to `3`:
#   ```python
#   def get_precedence(op: str) -> int:
#       if op in ("+", "-"):
#           return 3  # <--- Change this from 1 to 3 to break math rule checking!
#       if op in ("*", "/"):
#           return 2
#       return 0