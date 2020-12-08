import math

def f(x): return math.cos(x)
es = 0.5 * 10**(-2) * 100
x = math.pi / 3

# evaluate series zero order
tv = math.cos(x)

# calculate true error for zero order
et = -((es - tv) / es) * 100

print ("0 : {} , te = {}%".format(tv, et))
x = (math.pi / 3) ** 2
e1 = tv - x / 2

et = ((es - e1)/es) * 100

ae = -((e1 - 1)/e1) * 100

print ("1 : {} , te = {}%, ae = {}% ".format(e1, et, ae))

# evaluate series for second order
x = (math.pi / 3) ** 4
e2 = e1 + x / math.factorial(4)

et = -((es - e2) / es ) * 100

ae = ((e2 - e1) / e2 ) * 100

print ("2 : {} , te = {}%, ae = {}% ".format(e2, et, ae))

# evaluate series for third order

x = (math.pi / 3) ** 6
e3 = e2 - x / math.factorial(6)

et = ((es - e3) / es ) * 100

ae = -((e3 - e2) / e3 ) * 100

print ("3 : {} , te = {}%, ae = {}% ".format(e2, et, ae))
print("approximate error is below 0.5%")
