import os, subprocess

def run_python_file(working_directory, file_path, args=None):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(target_file):
        return f'Error: File "{file_path}" not found.'
    if not target_file.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        commands = ["python3", target_file]
        if args:
            commands.extend(args)
        result = subprocess.run(
            commands,
            cwd=working_directory,  # Set working directory.
            capture_output=True,    # Capture both stdout and stderr.
            text=True,              # Return output as strings, not bytes.
            timeout=30              # Set timeout to 30 Seconds.
        )
        
        # Output formating
        output_parts = []
        if result.stdout:
            output_parts.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output_parts.append(f"STDERR:\n{result.stderr}")
            
        # Checking if process failed
        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")
        
        # Case: No output at all
        if not output_parts:
            return "No output produced."
        
        return "\n".join(output_parts)
        
    except Exception as e:
        return f"Error: executing Python file: {e}"