# ai-agent-hegstreg

## Disclaimer
"Remember, what is built here is a toy version of something like Cursor/Zed's Agentic Mode, or Claude Code. Even their tools aren't **perfectly secure**, so be careful what you give it access to, and ***don't* give this code away to anyone else to use!**" "I highly recommend taking this course at [Boot.dev](https://www.boot.dev/) to be save. You can follow the instructions to build this tool even without a paid subscription. If you want the shortcut, do it at your own risk.

## what the cli tool can do:

1. accepting coding tasks
2. chooses from a set of predefined functions to work on the task, for example:
    - scan the files in a directory
    - read a file's contents
    - overwrite a file's contents
    - execute the python interpreter on a file
3. repeats step 2 until the task is complete (or it fails miserably, which is possible)

## prerequisites
- Python 3.10+ installed

For this project I will use Google's Gemini API. If you want to use your own little Toy Agent, you will have to go to [Gemini-API](https://ai.google.dev/gemini-api/docs/pricing) and create an API Key, if you have none already. Here are the [docs](https://ai.google.dev/gemini-api/docs/api-key) if you get lost. Notice: I will use Gemini 2.0 Flash for this Project. It has a generous free tier.
Don't forget to *.gitignore* your *.env* file with the following code:

```
{
    GEMINI_API_KEY="your_api_key_here"
}
```

- You have to create a virtual environment at the top level of your (this) project directory. (Add the *venv* directory to your *.gitignore*, too.):

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



## usage
... under construction ...
- file_content
- file_info
- run_python
- write_file
<!-- verbose flag // token input/output count
        Usage: python main.py "your prompt here" [--verbose]'
        Example: python main.py "Why is Sam the secret and only hero in lotr?"
-->
