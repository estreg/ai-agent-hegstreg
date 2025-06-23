import os, sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from config import system_prompt
from call_functions import available_functions, call_function

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
    
    for i in range(20):
        response = generate_content(client, messages, verbose)
        for candidate in response.candidates:
            messages.append(candidate.content)

        function_responses = []
        if response.function_calls:
            for function_call in response.function_calls:
                function_call_result = call_function(function_call, verbose)
                if (
                    not function_call_result.parts
                    or not function_call_result.parts[0].function_response
                ):
                    raise Exception("empty function call result")
                if verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
                function_responses.append(function_call_result.parts[0])
                messages.append(function_call_result)
        else:
            print(response.text)
            break

 
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

    return response

if __name__ == "__main__":
    main()
