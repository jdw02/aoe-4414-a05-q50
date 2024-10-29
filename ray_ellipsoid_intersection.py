# ray_ellipsoid_intersection.py

# Usage: ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z
#  Python script to find the intersection point (if it exists)...
#  between a ray and the Earth reference ellipsoid.

# Parameters:
#  #  d_l_x: x-coorditate of origin-referenced ray unit vector
#  d_l_y: y-coorditate of origin-referenced ray unit vector
#  d_l_z: z-coorditate of origin-referenced ray unit vector
#  c_l_x: x-coorditate of the ray origin offset
#  c_l_y: y-coorditate of the ray origin offset
#  c_l_z: z-coorditate of the ray origin offset

# Output:
# print(l_d[0]) # x-component of intersection point
# print(l_d[1]) # y-component of intersection point
# print(l_d[2]) # z-component of intersection point

# Written by Jayden Warren

# import Python modules
import sys # argv
import math

# Constants
w = 7.292115*10**-5
R_E_KM = 6378.1363
E_E    = 0.081819221456

# initialize script arguments
d_l_x = float('nan') # x-coorditate of origin-referenced ray unit vector
d_l_y = float('nan') # y-coorditate of origin-referenced ray unit vector
d_l_z = float('nan') # z-coorditate of origin-referenced ray unit vector
c_l_x = float('nan') # x-coorditate of the ray origin offset
c_l_y = float('nan') #y-coorditate of the ray origin offset
c_l_z = float('nan') #z-coorditate of the ray origin offset


# parse script arguments
if len(sys.argv)==7:
    d_l_x = float(sys.argv[1]) # x-coorditate of origin-referenced ray unit vector
    d_l_y = float(sys.argv[2]) # y-coorditate of origin-referenced ray unit vector
    d_l_z = float(sys.argv[3]) # z-coorditate of origin-referenced ray unit vector
    c_l_x = float(sys.argv[4]) # x-coorditate of the ray origin offset
    c_l_y = float(sys.argv[5]) #y-coorditate of the ray origin offset
    c_l_z = float(sys.argv[6]) #z-coorditate of the ray origin offset
else:
    print(\
     'Usage: '\
     'ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z'\
    )
    exit()

# write script below this line
a = d_l_x*d_l_x + d_l_y*d_l_y + (d_l_z*d_l_z)/(1-E_E*E_E)
b = 2*(d_l_x*c_l_x+d_l_y*c_l_y+(d_l_z*c_l_z)/(1-E_E**2))
c = c_l_x**2+c_l_y**2+(c_l_z**2)/(1-E_E**2)-R_E_KM**2
discr = b*b-4.0*a*c

if discr >= 0:
    d = (-b - math.sqrt(discr))/(2*a)
    if d < 0:
        d = (-b + math.sqrt(discr))/(2*a)
    if d > 0:
        l_d = [d*d_l_x+c_l_x, d*d_l_y+c_l_y, d*d_l_z+c_l_z]

print(l_d[0]) # x-component of intersection point
print(l_d[1]) # y-component of intersection point
print(l_d[2]) # z-component of intersection point
