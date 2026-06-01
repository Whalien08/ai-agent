import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

def main():
    # 1. Load the .env file explicitly
    load_dotenv()

    # 2. Verify the key is actually loaded in Python
    if not os.environ.get("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY is still missing from environment variables!")
        sys.exit(1)
    else:
        print("API Key successfully loaded.")

    # 3. Initialize the Gemini Client
    client = genai.Client()

    # 4. Check for command-line arguments
    if len(sys.argv) < 2:
        print("I need a prompt")
        sys.exit(1)

    # FIX 1: Define verbose_flag with a default value so it always exists
    verbose_flag = False
    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        verbose_flag = True
    
    prompt = sys.argv[1]

    # 5. Generate content
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
    )
    print("\nAI Response:", response.text)
    
    # FIX 2: Safe Pythonic check to ensure response and metadata are valid
    if not response or not response.usage_metadata:
        print("Error: Response is malformed or missing metadata.")
        return
    
    # This will now run perfectly whether you use --verbose or not!
    if verbose_flag:
        print("\n[Token Metrics]")
        print(f"  User Prompt:     {prompt}")
        print(f"  Prompt Tokens:   {response.usage_metadata.prompt_token_count}")
        print(f"  Response Tokens: {response.usage_metadata.candidates_token_count}")
        print(f"  Total Tokens:    {response.usage_metadata.total_token_count}\n")

if __name__ == "__main__":
    main()