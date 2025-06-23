import os, sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from config import system_prompt
from call_functions import available_functions

def main():
    load_dotenv()
    
    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    
    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "Why is Sam the secret and only hero in lotr?"')
        sys.exit(1)
    
    user_prompt = " ".join(args)
    
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    if verbose:
        print(f"User prompt: {user_prompt}\n")
    
    messages = [
        types.Content(
            role="user",
            parts=[types.Part(text=user_prompt)]),
    ]
    
    generate_content(client, messages, verbose)


    
def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages,
        config=types.GenerateContentConfig(
             tools=[available_functions], system_instruction=system_prompt),
    )
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    if response.function_calls:
        for function_call in response.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print("Response:")
        print(response.text)
    


if __name__ == "__main__":
    main()
