""" Compute and print the storage efficiency for each of the
    following 12 steel can sizes:
        Name	Radius (cm)	Height(cm)	Cost per Can (U.S. dollars)
        #1 Picnic	6.83	10.16	$0.28
        #1 Tall	    7.78	11.91	$0.43
        #2	        8.73	11.59	$0.45
        #2.5	    10.32	11.91	$0.61
        #3 Cylinder	10.79	17.78	$0.86
        #5	        13.02	14.29	$0.83
        #6Z	        5.40	8.89	$0.22
        #8Z short	6.83	7.62	$0.26
        #10	        15.72	17.78	$1.53
        #211	    6.83	12.38	$0.34
        #300	    7.62	11.27	$0.38
        #303	    8.10	11.11	$0.42
        
    Visually examine the output and answer the question "Which can 
    size has the hightest storage efficiency?"
"""

import math

def main():
    can_names = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", 
                "#6Z", "#8Z Short", "#10", "#211", "#300", "#303"]
    radius_list = ["6.83", "7.78", "8.73", "10.32", "10.79", "13.02", "5.40",
            "6.83", "15.72", "6.83", "7.62", "8.10"]
    height_list = ["10.16", "11.91", "11.59", "11.91", "17.78", "14.29", "8.89",
            "7.62", "17.78", "12.38", "11.27", "11.11"]
    cost_us_dollars_list = ["0.28", "0.43", "0.45", "0.61", "0.86", "0.83",
                   "0.22", "0.26", "1.53", "0.34", "0.38", "0.42"]
    
    # Enumerate through the list and compute for each can
    for i, can_name in enumerate(can_names):
        radius = float(radius_list[i])
        height = float(height_list[i])
        cost = float(cost_us_dollars_list[i])
        i += 1

    # Compute the volume
        volume = compute_volume(radius, height)
    
    # Compute surface area
        surface_area = compute_surface_area(radius, height)
    
    # Compute storage efficiency
        # For core requirement
        # storage_efficiency = volume / surface_area
        
        # For stretch challenges
        storage_efficiency = compute_storage_efficiency(volume, surface_area)
        
        cost_efficiency = compute_cost_efficiency(volume, cost)                                                
                                                        
        print(f"{can_name:<14} Storage Efficiency: {storage_efficiency:.2f} - Cost Efficiency: {cost_efficiency:.0f}")
        
def compute_volume(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume

def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(volume, surface_area):
    storage_efficiency = volume / surface_area
    return storage_efficiency

def compute_cost_efficiency(volume, cost):
    cost_efficiency = volume / cost 
    return cost_efficiency

main()