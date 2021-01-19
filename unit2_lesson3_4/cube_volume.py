"""
Mykyta S.
cube_volume.py
Finds the volume of a cube
"""

def cube_volume(side_length : float):
    return side_length ** 3

volume = cube_volume(float(input("Enter side length: ")))

print("The volume is", volume)
