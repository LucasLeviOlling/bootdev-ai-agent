import os

def main():
    pass

    
def get_files_info(working_directory, directory="../calculator"):
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
     



    if valid_target_dir:
        print(working_dir_abs, target_dir, valid_target_dir)
    else:
        print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    

if __name__ == "__main__":
    main()
