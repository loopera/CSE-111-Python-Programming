import math

#Function of Main body
def main():
    
    name = "#1 Picnic"	
    radius = 6.83	
    height = 10.16	
    cost = 0.28
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = volume/surface_area
    print(f"Name: {name} Volume: {volume:.2f} Surface Area: {surface_area:.2f} Storage Efficiency: {storage_efficiency:.2f}")
    
    name = "#1 Tall"
    radius = 7.78	
    height = 11.91	
    cost = 0.43
    storage_efficiency = compute_storage_efficiency(radius, height)
    print(f"Name: {name} Vol: {volume:.2f} Surface Area: {surface_area:.2f} Storage Efficiency: {storage_efficiency:.2f}")
   
    name = "#2"	
    radius = 8.73	
    height = 11.59	
    cost = 0.45
    storage_efficiency = compute_storage_efficiency(radius, height)
    print(f"Name: {name}  Storage Efficiency: {storage_efficiency:.2f}")



    #2.5	10.32	11.91	$0.61
    #3 Cylinder	10.79	17.78	$0.86
    #5	13.02	14.29	$0.83
    #6Z	5.40	8.89	$0.22
    #8Z short	6.83	7.62	$0.26
    #10	15.72	17.78	$1.53
    #211	6.83	12.38	$0.34
    #300	7.62	11.27	$0.38
    #303	8.10	11.11	$0.42

    



def compute_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume


def compute_surface_area(radius, height):
    surface_area = 2*math.pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(radius, height):
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = volume/surface_area
    return storage_efficiency

main()


