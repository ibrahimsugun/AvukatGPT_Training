import os
from pathlib import Path

def delete_uploaded_files():
    base_dir = Path(r"c:\Users\IT\Desktop\datas\blog_contents\converted_markdown")
    list_file = base_dir / "yuklenenler.txt"
    
    if not list_file.exists():
        print(f"Error: {list_file} not found.")
        return

    # Read the list of files to delete
    with open(list_file, 'r', encoding='utf-8') as f:
        files_to_delete = [line.strip() for line in f if line.strip()]

    # Get all actual files in the directory
    actual_files = {f.name: f for f in base_dir.iterdir() if f.is_file()}
    
    deleted_count = 0
    not_found_count = 0
    ambiguous_count = 0

    print(f"Found {len(actual_files)} files in directory.")
    print(f"Processing {len(files_to_delete)} items from list...")

    for filename in files_to_delete:
        target_file = None
        
        # 1. Try exact match
        if filename in actual_files:
            target_file = actual_files[filename]
        
        # 2. Try truncated match
        elif "..." in filename:
            parts = filename.split("...")
            if len(parts) == 2:
                prefix = parts[0]
                suffix = parts[1]
                matches = [f for name, f in actual_files.items() if name.startswith(prefix) and name.endswith(suffix)]
                
                if len(matches) == 1:
                    target_file = matches[0]
                elif len(matches) > 1:
                    print(f"Ambiguous match for '{filename}': {[m.name for m in matches]}")
                    ambiguous_count += 1
                    continue
        
        if target_file:
            try:
                # Check if it still exists (might have been deleted if duplicates in list)
                if target_file.exists():
                    target_file.unlink()
                    deleted_count += 1
                    # print(f"Deleted: {target_file.name}")
            except Exception as e:
                print(f"Error deleting {target_file.name}: {e}")
        else:
            # print(f"Not found: {filename}")
            not_found_count += 1

    print("-" * 30)
    print(f"Total processed: {len(files_to_delete)}")
    print(f"Deleted: {deleted_count}")
    print(f"Not found: {not_found_count}")
    print(f"Ambiguous: {ambiguous_count}")
    
    remaining_files = len(list(base_dir.iterdir()))
    print(f"Remaining files in directory: {remaining_files}")

if __name__ == "__main__":
    delete_uploaded_files()
