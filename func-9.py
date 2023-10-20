import math

def calculate_sphere(radius):
    volume = (4/3) * math.pi * radius**3
    return volume


radius = float(input("Enter the radius: "))
sphere_volume = calculate_sphere(radius)
print(sphere_volume)
