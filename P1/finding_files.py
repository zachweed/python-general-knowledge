import os

def find_files(suffix, path):
    matching_file_list = []
    try:
        ff_list = os.listdir(path)
        if len(ff_list) == 1 and ff_list[0].endswith(suffix):
            return ff_list[0]
        else:
            for item in ff_list:
                full_path = os.path.join(path, item)
                if os.path.isdir(full_path):
                    files = find_files(suffix, full_path)
                    if len(files) > 0:
                        for file in files:
                            if file.endswith(suffix):
                                matching_file_list.append(file)
                elif os.path.isfile(full_path):
                    if full_path.endswith(suffix):
                        matching_file_list.append(full_path)

    except(PermissionError, FileNotFoundError):
        return None
    return matching_file_list
