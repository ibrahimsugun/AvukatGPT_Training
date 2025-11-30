import os
import re
from pathlib import Path

class BaseParser:
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.content = self.read_file()
        self.lines = self.content.splitlines()

    def read_file(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except UnicodeDecodeError:
            # Fallback for other encodings if utf-8 fails
            with open(self.file_path, 'r', encoding='latin-1') as f:
                return f.read()

    def clean_line(self, line):
        return line.strip()

    def is_header(self, line):
        # Basic heuristic: Short, starts with capital, no ending punctuation (except ?), or all caps
        line = line.strip()
        if not line:
            return False
        if len(line) > 100:
            return False
        if line.endswith('?') or line.endswith(':'):
            return True
        if line.isupper():
            return True
        # Title Case check (mostly)
        words = line.split()
        if len(words) > 0 and all(w[0].isupper() for w in words if w.isalpha()):
            return True
        return False

class MevzuatParser(BaseParser):
    def parse(self):
        md_lines = []
        
        # Title is usually the first line
        if self.lines:
            md_lines.append(f"# {self.lines[0].strip()}")
            md_lines.append("")

        current_section = None
        
        for i, line in enumerate(self.lines[1:], start=1):
            line = line.strip()
            if not line:
                continue

            # Detect specific Mevzuat sections
            if "Gerekçesi" in line and len(line) < 50:
                md_lines.append(f"## {line}")
                current_section = "gerekce"
            elif "Emsal Yargıtay Kararları" in line:
                md_lines.append(f"## {line}")
                current_section = "kararlar"
            elif line.startswith("YARGITAY") and "DAİRESİ" in line:
                md_lines.append(f"### {line}")
            elif line.startswith("Esas No:") or line.startswith("Karar No:") or line.startswith("Tarih:"):
                md_lines.append(f"- **{line}**")
            elif re.match(r'^\d+\.$', line) or re.match(r'^[a-z]\)$', line):
                 # Numbered lists often found in law text
                md_lines.append(f"{line}") 
            else:
                # Regular text
                md_lines.append(line)
            
            md_lines.append("") # Add spacing

        return "\n".join(md_lines)

class GeneralParser(BaseParser):
    def parse(self):
        md_lines = []
        
        # Title
        if self.lines:
            md_lines.append(f"# {self.lines[0].strip()}")
            md_lines.append("")

        for i, line in enumerate(self.lines[1:], start=1):
            line = line.strip()
            if not line:
                continue

            # Headers
            if self.is_header(line):
                # Determine level? For now, just use H2 for all subheaders
                md_lines.append(f"## {line}")
            # Lists
            elif line.startswith(('-', '*', '•')):
                md_lines.append(f"- {line.lstrip('-*• ')}")
            elif re.match(r'^\d+\.', line):
                md_lines.append(line)
            # Bold text (lines ending with :)
            elif line.endswith(':'):
                md_lines.append(f"**{line}**")
            else:
                md_lines.append(line)
            
            md_lines.append("")

        return "\n".join(md_lines)

def convert_files(source_dir, target_dir):
    source_path = Path(source_dir)
    target_path = Path(target_dir)
    
    if not target_path.exists():
        target_path.mkdir(parents=True)

    for root, dirs, files in os.walk(source_path):
        # Avoid recursing into the output directory
        if target_path in Path(root).parents or Path(root) == target_path:
            continue

        for file in files:
            if not file.endswith('.txt'):
                continue
            
            # Skip the script itself if it has .txt extension (unlikely but good practice)
            if file == 'convert_blog_content.py':
                continue
                
            file_path = Path(root) / file
            
            # Determine Parser
            if 'mevzuat' in file.lower() or 'mevzuat' in root.lower():
                parser = MevzuatParser(file_path)
            else:
                parser = GeneralParser(file_path)
            
            markdown_content = parser.parse()
            
            # Determine output path
            rel_path = file_path.relative_to(source_path)
            output_file_path = target_path / rel_path.with_suffix('.md')
            
            # Ensure subdirs exist
            output_file_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_file_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            
            print(f"Converted: {file} -> {output_file_path}")

if __name__ == "__main__":
    # Configuration
    # Use current directory as source
    SOURCE_DIR = os.path.dirname(os.path.abspath(__file__))
    TARGET_DIR = os.path.join(SOURCE_DIR, "converted_markdown")
    
    print(f"Starting conversion from {SOURCE_DIR} to {TARGET_DIR}...")
    convert_files(SOURCE_DIR, TARGET_DIR)
    print("Conversion complete.")
