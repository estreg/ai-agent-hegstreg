import os, sys
from dotenv import load_dotenv
from google import genai

def main():
    load_dotenv()
    
    args = sys.argv[1:]
    
    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "Why is Sam the secret and only hero in lotr?"')
        sys.exit(1)
    user_prompt = " ".join(args)
    
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=user_prompt,
    )
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
