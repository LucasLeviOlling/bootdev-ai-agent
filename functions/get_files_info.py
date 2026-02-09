import os

def main():
    pass

    
def get_files_info(working_directory, directory="../calculator"):
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

    if not os.path.isdir(target_dir):
        print(f'Error: "{directory}" is not a directory')
        return

    if valid_target_dir:
        if directory == ".":
            print("Result for current directory:")
        else:
            print(f"Result for '{directory}' directory:")
        for fd in os.listdir(target_dir):
            target_file = os.path.join(target_dir, fd)
            print(f" - {fd}: file_size={os.path.getsize(target_file)} bytes, is_dir={os.path.isdir(target_file)}")

    else:
        print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    

if __name__ == "__main__":
    main()
