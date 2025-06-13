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

## Disclaimer
Remember, what is built here is a toy version of something like Cursor/Zed's Agentic Mode, or Claude Code. Even their tools aren't perfectly secure, so be careful what you give it access to, and don't give this code away to anyone else to use!