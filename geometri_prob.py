# author : Jignesh Chaudhary Student Id: 197320
# solution of problem 2.27 (page 54)
#============================================================================================
# V = 1/3 * pi * h * (r1**2 + r2**2 + r1 * r2) # to find volume of frustum part(top) of water tank
# V = pi * (r**2) * h1 # to find volume of cylinder part of water tank
#============================================================================================
import math

def vol_cyl(h,r1):# to calculate volume of cylinder part of tank
    vocl = math.pi * (r1**2) * h
    return vocl
#end function

def vol_fru(r1,r2,h): #function to calculate volume of frustum
    r2h = float(r1 + (r2 - r1) / H2 * (h - H1))
    V = (1 / 3) * math.pi * (h - H1) * (r1 ** 2 + r2h ** 2 + r1 * r2h)
    return V
# end function

def vol_tank(h,H1,H2,r1,r2): # function to calculate volume of tank
    v = 0
    if h <= 0: # returns a value of zero for negative h’s
        v = 0.00
    elif h <= H1:# return a value of h's up to h = H1
        v = vol_cyl(h,r1)
    elif h > H1 and h <= H1+H2: # return a value of h's up to h = H1+H2
        v = vol_cyl(H1, r1) + vol_fru(r1, r2, h)
    elif h > H1+H2: # return a value of the maximum filled volume for h’s greater than the tank’s maximum depth
        h = H1 + H2
        v = vol_cyl(H1, r1) + vol_fru(r1, r2, h)
    return float(v)
#end Function

r1 = 4
H1 = 10
H2 = 5
r2 = 6.5

for h in range (-1, 16+1):
    Vol = vol_tank(h, H1, H2, r1, r2)
    print ("Height : {:2.0f} Volume: {:.2f}".format (h, Vol))
