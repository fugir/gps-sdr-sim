#!/usr/bin/env python3
import csv

def main():
    circle_file = "circle.csv"
    random_file = "random_coordinates_three.csv"
    output_file = "combined.csv"
    
    # Read all rows from circle.csv
    with open(circle_file, "r", newline="") as cf:
        circle_reader = csv.reader(cf)
        circle_rows = list(circle_reader)
    
    # Read all rows from random_coordinates_three.csv
    with open(random_file, "r", newline="") as rf:
        random_reader = csv.reader(rf)
        random_rows = list(random_reader)
    
    # Determine the total number of rows to process.
    # We'll take the minimum length if they differ.
    total_rows = min(len(circle_rows), len(random_rows))
    
    combined_rows = []
    chunk_size = 10
    # Process rows in blocks of 10 until we reach total_rows.
    for i in range(0, total_rows, chunk_size):
        # Take a block of 10 rows from circle
        circle_block = circle_rows[i:i+chunk_size]
        # Take a block of 10 rows from random file
        random_block = random_rows[i:i+chunk_size]
        
        # Append the entire block from circle then the block from random
        combined_rows.extend(circle_block)
        combined_rows.extend(random_block)
    
    # Write the combined rows to the output file
    with open(output_file, "w", newline="") as outf:
        writer = csv.writer(outf)
        writer.writerows(combined_rows)
    
    print(f"Combined file '{output_file}' created with {len(combined_rows)} lines.")

if __name__ == "__main__":
    main()

