# ai-agent-hegstreg

## Disclaimer:
"Remember, what is built here is a toy version of something like Cursor/Zed's Agentic Mode, or Claude Code. Even their tools aren't **perfectly secure**, so be careful what you give it access to, and ***don't* give this code away to anyone else to use!**" "I highly recommend taking this course at [Boot.dev](https://www.boot.dev/) to be save. You can follow the instructions to build this tool even without a paid subscription. If you want the shortcut, do it at your own risk.

## What the CLI Agent can do:

1. Answer your questions.
    (To ensure answers aren't too long and to manage token usage within the free tier, please system-prompt and properly prompt your questions. You can find the system-prompt in the *config.py* file)
2. Accepting coding tasks.
3. Chooses from a set of predefined functions to work on the task, for example:
    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files
4. Repeats step 2 until the task is complete (or it fails miserably, which is possible).

## Prerequisites:

- Python 3.10+ installed

- For this project I will use Google's Gemini API. If you want to use your own toy agent, you will have to go to [Gemini-API](https://ai.google.dev/gemini-api/docs/pricing) and    create an API Key, if you have none already. Here are the [docs](https://ai.google.dev/gemini-api/docs/api-key) if you get lost. Notice: I will use Gemini 2.0 Flash for this Project. It has a generous free tier. Don't forget to *.gitignore* your *.env* file with the following code:
```
{
    GEMINI_API_KEY="your_api_key_here"
}
```

- You have to create a virtual environment at the top level of your project directory. (Add the *venv* directory to your *.gitignore*, too.):
```
    python3 -m venv venv
```

- Activate the virtual environment. (Always make sure that it is activated when running the code):
```
    source venv/bin/activate
```

- Take a look at the *requirements.txt* (Here are the docs: [google-genai](https://pypi.org/project/google-genai/) and [python-dotenv](https://pypi.org/project/python-dotenv/)). It contains this:
```
    google-genai==1.12.1
    python-dotenv==1.1.0
```

- Install the requirements with:
```
    pip install -r requirements.txt
```

## Usage:
- In config.py, I've hardcoded the working directory as:
```
    WORKING_DIR = "./calculator"
```
This is to prevent the agent from making unintended changes outside this directory.

- To start your agent use this command (The *verbose* flag is optional. It shows you some optional information like how many prompt and reponse tokens were used.):
```
    python3 main.py "your prompt here" [--verbose]
```
## Examples:

### Example 1:
```
    python3 main.py "Why is Sam the secret and only hero in lotr? Answer in 1 paragraph." --verbose
```
- The response i got:
```
    User prompt: Why is Sam the secret and only hero in lotr? Answer in 1 paragraph.

    Prompt tokens: 563
    Response tokens: 118
    Samwise Gamgee is often considered the secret hero of The Lord of the Rings due to his unwavering loyalty, courage, and resilience. While Frodo is tasked with bearing the Ring, it is Sam's steadfast support and practical nature that enables Frodo to continue his quest. He consistently pulls Frodo back from the brink of despair, physically carries him when necessary, and makes crucial decisions that save their journey. Sam's simple goodness and devotion embody the values that ultimately triumph over evil, making him an unsung but essential figure in the success of the Fellowship's mission.
```

### Example 2:
    Setup: in *calculator/pkg/calculator.py* change the precedence of the addition operator to 3.
```
    python3 main.py "In ./calculator/pkg/calculator.py file is a bug, identify and only fix the bug."
```
- The response i got:
```
    - Calling function: get_files_info
    - Calling function: get_files_info
    - Calling function: get_files_info
    - Calling function: get_file_content
    - Calling function: write_file
    - Calling function: write_file
    - Calling function: write_file
    - Calling function: write_file
    - Calling function: run_python_file
    All tests passed. I have fixed the identified bugs and added a test suite to ensure the calculator works correctly.
```
- While the agent successfully fixed the bug, it also created test_calculator.py. However, its behavior was inconsistent: when I used the same prompt repeatedly, the results varied, and it didn't always write a new test file. Once, it inexplicably generated an empty *__init__.py* file. 🤔 --> once again: be *careful* with this tool!