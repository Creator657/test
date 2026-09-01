#!/usr/bin/env python3
"""
Script to recombine split resource files (resources.assets.resS.001-011)
into a single resources.assets.resS file.

This script concatenates binary files in order and creates the final combined file.
"""

import os
import sys

def combine_resources(output_file='resources.assets.resS', num_parts=11):
    """
    Combine split resource files into a single file.
    
    Args:
        output_file: Name of the output file (default: resources.assets.resS)
        num_parts: Number of parts to combine (default: 11)
    """
    input_files = [f'resources.assets.resS.{str(i).zfill(3)}' for i in range(1, num_parts + 1)]
    
    print(f"Starting to combine {num_parts} resource files...")
    print(f"Output file: {output_file}\n")
    
    # Verify all input files exist
    missing_files = []
    for input_file in input_files:
        if not os.path.exists(input_file):
            missing_files.append(input_file)
    
    if missing_files:
        print("ERROR: The following files are missing:")
        for file in missing_files:
            print(f"  - {file}")
        sys.exit(1)
    
    # Combine files
    try:
        with open(output_file, 'wb') as outfile:
            total_size = 0
            for i, input_file in enumerate(input_files, 1):
                file_size = os.path.getsize(input_file)
                print(f"[{i}/{num_parts}] Reading {input_file} ({file_size:,} bytes)...", end='', flush=True)
                
                with open(input_file, 'rb') as infile:
                    outfile.write(infile.read())
                
                total_size += file_size
                print(" ✓")
        
        print(f"\n✓ Successfully combined all files!")
        print(f"Total size: {total_size:,} bytes ({total_size / (1024**2):.2f} MB)")
        print(f"Output file: {output_file}")
        
    except IOError as e:
        print(f"\nERROR: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nCombination cancelled by user.")
        if os.path.exists(output_file):
            os.remove(output_file)
            print(f"Cleaned up incomplete {output_file}")
        sys.exit(1)

if __name__ == '__main__':
    combine_resources()
