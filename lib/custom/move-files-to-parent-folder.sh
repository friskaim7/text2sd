#!/bin/bash

find "./code2diagram" -type f > filelist.txt

# Read each line from the filelist.txt file
while IFS= read -r line; do
    # Get the filename without the path
    filename=$(basename "$line")
    
    # Get the parent folder of the file
    parent_folder=$(dirname "$(dirname "$line")")
    
    # Move the file to its parent folder
    mv "$line" "$parent_folder"
    echo "$filename has been moved to $parent_folder"
done < filelist.txt
