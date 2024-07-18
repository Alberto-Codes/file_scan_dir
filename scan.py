import os
import time

def get_file_metadata(root_dir):
    start_time = time.time()
    file_metadata = []
    
    for root, dirs, files in os.walk(root_dir):
        for name in files:
            filepath = os.path.join(root, name)
            try:
                file_info = os.stat(filepath)
                file_metadata.append((filepath, file_info.st_size, file_info.st_mtime))
            except Exception as e:
                print(f"Error retrieving metadata for {filepath}: {e}")
    
    print(f"Time taken using os.walk: {time.time() - start_time} seconds")
    return file_metadata

def get_file_metadata_scandir(root_dir):
    start_time = time.time()
    file_metadata = []

    def scan_dir(path):
        with os.scandir(path) as it:
            for entry in it:
                if entry.is_file():
                    try:
                        file_info = entry.stat()
                        file_metadata.append((entry.path, file_info.st_size, file_info.st_mtime))
                    except Exception as e:
                        print(f"Error retrieving metadata for {entry.path}: {e}")
                elif entry.is_dir():
                    scan_dir(entry.path)
    
    scan_dir(root_dir)
    print(f"Time taken using os.scandir: {time.time() - start_time} seconds")
    return file_metadata

root_dir = '/path/to/your/directory'
metadata_walk = get_file_metadata(root_dir)
metadata_scandir = get_file_metadata_scandir(root_dir)
