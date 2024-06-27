import os

def rename_files_in_directory(directory_path):
    # Ensure the directory exists
    if not os.path.isdir(directory_path):
        print(f"The directory '{directory_path}' does not exist.")
        return

    # List all files in the directory
    files = os.listdir(directory_path)
    
    # Filter out directories
    files = [f for f in files if os.path.isfile(os.path.join(directory_path, f))]
    
    # Sort files to ensure consistent order
    files.sort()
    
    # Rename each file
    for i, filename in enumerate(files, start=1):
        # Get the file extension
        file_extension = os.path.splitext(filename)[1]
        
        # New file name with the same extension
        new_filename = f"{i}{file_extension}"
        
        # Full paths
        old_file = os.path.join(directory_path, filename)
        new_file = os.path.join(directory_path, new_filename)
        
        # Rename the file
        os.rename(old_file, new_file)
        print(f"Renamed '{old_file}' to '{new_file}'")
