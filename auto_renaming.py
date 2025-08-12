import os

def rename_files(folder_path, base_name="file"):
    files = os.listdir(folder_path)
    count = 1
    
    for file_name in files:
        old_path = os.path.join(folder_path, file_name)
        
        # Skip directories and the running script
        if os.path.isdir(old_path) or file_name == os.path.basename(__file__):
            continue
        
        # Get original file extension
        ext = os.path.splitext(file_name)[1]
        
        new_name = f"{base_name}_{count}{ext}"
        new_path = os.path.join(folder_path, new_name)
        
        # Avoid overwriting
        if os.path.exists(new_path):
            print(f" Skipping {file_name} → {new_name} (already exists)")
            continue
        
        os.rename(old_path, new_path)
        print(f"Renamed: {file_name} → {new_name}")
        count += 1

# Example usage
folder = r"C:\Users\vy849\OneDrive\Desktop\task4"  # Update with your exact folder path
rename_files(folder, base_name="file")
