import os
from pathlib import Path

def analyze_embedding_status():
    base_dir = Path(r"c:\Users\IT\Desktop\datas\blog_contents\converted_markdown")
    status_file = base_dir / "durum.txt"
    
    if not status_file.exists():
        print(f"Error: {status_file} not found.")
        return

    # Read the list of uploaded files from durum.txt
    with open(status_file, 'r', encoding='utf-8') as f:
        # Skip the first line if it says "Yüklenenler:"
        lines = [line.strip() for line in f if line.strip()]
    
    if lines and lines[0].startswith("Yüklenenler"):
        uploaded_entries = lines[1:]
    else:
        uploaded_entries = lines

    # Get all actual files in the directory (excluding durum.txt and other non-md files if any)
    all_files = {f.name: f for f in base_dir.iterdir() if f.is_file() and f.suffix == '.md'}
    
    uploaded_files = []
    failed_files = []
    
    # Logic to match entries to actual files
    matched_filenames = set()
    
    print(f"Processing {len(uploaded_entries)} entries from durum.txt...")
    
    for entry in uploaded_entries:
        target_file = None
        
        # 1. Try exact match
        if entry in all_files:
            target_file = all_files[entry]
        
        # 2. Try truncated match
        elif "..." in entry:
            parts = entry.split("...")
            if len(parts) == 2:
                prefix = parts[0]
                suffix = parts[1]
                matches = [name for name in all_files.keys() if name.startswith(prefix) and name.endswith(suffix)]
                
                if len(matches) == 1:
                    target_file = all_files[matches[0]]
                elif len(matches) > 1:
                    # Ambiguous, but we assume one of them is the one. 
                    # For accounting purposes, taking the first one is a reasonable approximation 
                    # if we mark it as matched.
                    target_file = all_files[matches[0]] 
        
        if target_file:
            uploaded_files.append(target_file)
            matched_filenames.add(target_file.name)
        else:
            # Entry in text file but not found on disk? 
            # Could be deleted or renamed. We'll ignore for token count but note it.
            pass

    # Identify failed files (those on disk but not in the uploaded list)
    for filename, file_path in all_files.items():
        if filename not in matched_filenames:
            failed_files.append(file_path)

    # Function to estimate tokens
    def estimate_tokens(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # Estimate: 1 token ~= 4 chars. 
                # For Turkish, it might be slightly more chars per token due to suffixes, 
                # but 4 is a standard conservative estimate for pricing/limits.
                return len(content), len(content) / 4
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return 0, 0

    # Calculate stats
    uploaded_chars = 0
    uploaded_tokens = 0
    for f in uploaded_files:
        c, t = estimate_tokens(f)
        uploaded_chars += c
        uploaded_tokens += t

    failed_chars = 0
    failed_tokens = 0
    for f in failed_files:
        c, t = estimate_tokens(f)
        failed_chars += c
        failed_tokens += t

    print("-" * 30)
    print(f"Total MD files on disk: {len(all_files)}")
    print(f"Files identified as Uploaded: {len(uploaded_files)}")
    print(f"Files identified as Failed (Not Uploaded): {len(failed_files)}")
    print("-" * 30)
    print("UPLOADED FILES STATS:")
    print(f"Total Characters: {uploaded_chars:,.0f}")
    print(f"Estimated Tokens: {uploaded_tokens:,.0f}")
    print("-" * 30)
    print("FAILED FILES STATS (Need to be embedded):")
    print(f"Total Characters: {failed_chars:,.0f}")
    print(f"Estimated Tokens: {failed_tokens:,.0f}")
    print("-" * 30)
    print("FAILED FILES STATS (Need to be embedded):")
    print(f"Total Characters: {failed_chars:,.0f}")
    print(f"Estimated Tokens: {failed_tokens:,.0f}")
    if failed_files:
        print("List of Failed Files:")
        for f in failed_files:
            print(f" - {f.name}")
    print("-" * 30)

if __name__ == "__main__":
    analyze_embedding_status()
