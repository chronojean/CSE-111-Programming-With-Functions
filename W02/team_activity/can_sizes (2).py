# DataFrames
import math

def compute_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume
 
def compute_surface_area(radius, height):
    base_area = math.pi * radius**2
    lateral_area = 2 * math.pi * radius * height
    surface_area = 2 * base_area + lateral_area
    return surface_area

def main():
    can_name = ["#1picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder,", "#5","#6Z", "#8Z short", "#10", "#211", "#300", "#303" ]
    can_sizes = [
        (6.83, 10.16),
        (7.78, 11.91),
        (8.73, 11.59),
        (10.32,	11.91),
        (10.79, 17.78),
        (13.02,	14.29),
        (5.40,	8.89),
        (6.83,	7.62),
        (15.72,	17.78),
        (6.83,	12.38),
        (7.62, 11.27),
        (8.10,	11.11)
        
    



        # Add the remaining can sizes here
    ]

    for i, (radius, height) in enumerate(can_sizes,start=1):
        volume = compute_volume(radius, height)
        surface_area = compute_surface_area(radius, height)
        storage_efficiency = volume / surface_area

        print(f"{can_name[i-1]}:")
        print("Volume:", volume)
        print("Surface Area:", surface_area)
        print("Storage Efficiency:", storage_efficiency)
        print()

if __name__ == "__main__":
    main()
