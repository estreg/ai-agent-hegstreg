import os

def get_files_info(working_directory, directory=None):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = abs_working_dir
    
    if directory:
        target_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    try:
        files_info = []
        for filename in os.listdir(target_dir):
            filepath = os.path.join(target_dir, filename)
            file_size = 0
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            files_info.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"
    
    # what i have build with the AI Boots...
    #if directory is None:
    #    directory = "."

    #if not os.path.isabs(directory):
    #    full_directory_path = os.path.join(working_directory, directory)
    #else:
    #    full_directory_path = directory

    #working_abs_path = os.path.abspath(working_directory)
    #directory_abs_path = os.path.abspath(full_directory_path)
    
    #if not (directory_abs_path == working_abs_path or directory_abs_path.startswith(working_abs_path + os.sep)):
    #   return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    #if not os.path.isdir(directory_abs_path):
    #    return f'Error: "{directory}" is not a directory'
    
    #try:
    #    file_info_list = []
    #    for filename in os.listdir(directory_abs_path):
    #       full_path = os.path.join(directory_abs_path, filename)
    #        file_size = os.path.getsize(full_path)
    #        is_dir = os.path.isdir(full_path)
    #        file_info_list.append(f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}")
    #    
    #    return "\n".join(file_info_list)
    
    #except Exception as e:
    #    return f"Error: {str(e)}"