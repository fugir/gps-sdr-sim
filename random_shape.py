#!/usr/bin/env python3
import numpy as np

def main():
    num_lines = 3000      # Total number of samples
    dt = 0.1              # Time step in seconds (10 Hz)
    times = np.arange(0, num_lines * dt, dt)
    
    # Define ranges for random coordinates (in meters)
    # Adjust these ranges to suit your simulation requirements.
    x_min, x_max = -3813480, -3813580  # ~20 meter range around the sample X
    y_min, y_max = 3554265, 3554365     # ~15 meter range around the sample Y
    z_min, z_max = 3662780, 3662880     # ~30 meter range around the sample Z
    
    # Generate random coordinates within these ranges
    x_vals = np.random.uniform(x_min, x_max, num_lines)
    y_vals = np.random.uniform(y_min, y_max, num_lines)
    z_vals = np.random.uniform(z_min, z_max, num_lines)
    
    # Write the data to a CSV file
    with open("random_coordinates_three.csv", "w") as f:
        for t, x, y, z in zip(times, x_vals, y_vals, z_vals):
            # Format: time,x,y,z
            f.write(f"{t:.1f},{x:.3f},{y:.3f},{z:.3f}\n")
    
    print("Generated random_coordinates_three.csv with 3000 lines.")

if __name__ == "__main__":
    main()
