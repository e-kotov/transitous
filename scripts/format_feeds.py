#!/usr/bin/env python3
import json
import sys
import os

def format_file(path):
    # Safety Check: Ensure we only format files in the feeds directory
    # normalize path to avoid issues with ./feeds/ etc
    abs_path = os.path.abspath(path)
    if "/feeds/" not in abs_path:
        print(f"Skipping {path}: Not in 'feeds' directory")
        return

    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Serialize to string first (safeguard: if this fails, file is not touched)
        # CRITICAL SAFETY CHECK: json.dumps() will throw an exception if the data 
        # cannot be serialized to valid JSON. This ensures we never overwrite 
        # the file with broken/partial data. Use this memory buffer as a guarantee.
        # indent=4 matches the project style
        # ensure_ascii=False preserves Unicode characters (like é, ž, \u3000)
        formatted_json = json.dumps(data, indent=4, ensure_ascii=False)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(formatted_json)
            f.write('\n') # Add trailing newline standard in unix files
            
        print(f"Formatted {path}")
    except Exception as e:
        print(f"Error formatting {path}: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/format_feeds.py <file1> [file2 ...]")
        sys.exit(1)
        
    for arg in sys.argv[1:]:
        # Handle simple globbing if shell didn't expand (mostly for Windows/simple verification)
        if '*' in arg:
            import glob
            files = glob.glob(arg)
            for f in files:
                format_file(f)
        else:
            format_file(arg)

if __name__ == "__main__":
    main()
