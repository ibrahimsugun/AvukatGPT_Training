import os
from pathlib import Path
import statistics

def estimate_tokens(text):
    # Rough estimate: 1 token ~= 4 characters or 0.75 words
    # For Turkish, words might be longer, so char count is safer.
    # OpenAI suggests ~4 chars per token for English. Turkish is agglutinative, so words are longer but carry more info.
    # Let's use a conservative 4 chars per token estimate for sizing.
    return len(text) / 4

def analyze_markdown_sections(directory):
    section_lengths = []
    
    files = list(Path(directory).rglob("*.md"))
    print(f"Analyzing {len(files)} markdown files...")

    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Simple split by headers
        # This mimics a basic Markdown splitter
        lines = content.splitlines()
        current_section = []
        
        for line in lines:
            if line.startswith('#'):
                if current_section:
                    text = "\n".join(current_section).strip()
                    if text:
                        section_lengths.append(estimate_tokens(text))
                    current_section = []
                # Include the header in the next section context
                current_section.append(line)
            else:
                current_section.append(line)
        
        # Add last section
        if current_section:
            text = "\n".join(current_section).strip()
            if text:
                section_lengths.append(estimate_tokens(text))

    if not section_lengths:
        print("No sections found.")
        return

    print(f"\n--- Analysis Results ({len(section_lengths)} sections) ---")
    print(f"Min Tokens: {min(section_lengths):.1f}")
    print(f"Max Tokens: {max(section_lengths):.1f}")
    print(f"Avg Tokens: {statistics.mean(section_lengths):.1f}")
    print(f"Median Tokens: {statistics.median(section_lengths):.1f}")
    
    # Percentiles
    sorted_lengths = sorted(section_lengths)
    p90 = sorted_lengths[int(len(sorted_lengths) * 0.9)]
    p95 = sorted_lengths[int(len(sorted_lengths) * 0.95)]
    
    print(f"90th Percentile: {p90:.1f}")
    print(f"95th Percentile: {p95:.1f}")

if __name__ == "__main__":
    TARGET_DIR = r"c:\Users\IT\Desktop\datas\blog_contents\converted_markdown"
    analyze_markdown_sections(TARGET_DIR)
