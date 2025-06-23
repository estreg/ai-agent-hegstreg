from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Shows the content of a file in the specified directory, constrained to the working directory, and with MaxChars = 10.000.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The directory path where the file is located."
            ),
        },
        required=["file_path"] # A file_path is required to read content.
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file (.py) located in the specified directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The full path to the Python file to be executed. This path must be within the allowed working directory."
            ),
        },
        required=["file_path"] # Added 'required' field since a file path is necessary.
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes specified content to a file at the given path. If the file exists, its content will be overwritten.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The full path to the file where the content will be written. This path must be within the allowed working directory."
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The string content to write to the file.",
            ),
        },
        required=["file_path", "content"] # Both file_path and content are required.
    ),
)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,        
    ]
)
