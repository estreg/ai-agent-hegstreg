# ai-agent-hegstreg

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

For this project I will use Google's Gemini API. If you want to use your own little Toy Agent, you will have to go to [Gemini-API]("https://ai.google.dev/gemini-api/docs/pricing") and create an API Key, if you have none already. Here are the [docs](https://ai.google.dev/gemini-api/docs/api-key) if you get lost. Notice: I will use Gemini 2.0 Flash for this Project. It has a generous free tier.
Don't forget to *.gitignore* your *.env* file with the following code:

```
{
    GEMINI_API_KEY="your_api_key_here"
}
```

## usage
... under construction ...
<!-- verbose flag -->

## Disclaimer
Remember, what is built here is a toy version of something like Cursor/Zed's Agentic Mode, or Claude Code. Even their tools aren't perfectly secure, so be careful what you give it access to, and don't give this code away to anyone else to use!