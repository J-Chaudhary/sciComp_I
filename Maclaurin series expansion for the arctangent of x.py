import math

#expansion of arctan (x) is as given in problem 4.4

def arctanx(n): return (((-1)**n) / (2 * n) + 1) * x **((2*n)+1)

x = math.pi/6

#add one term in simplest version of arctan(x) = x
#arctan(x) = x - x**3 / 3
ax = x - ((x **3)/3)
et = ((math.atan(x) - ax) / math.atan(x)) * 100
ea = -((ax - x) / ax) * 100
print ("et : {:.2f}%, ea = {:.2f}%".format(et,ea))

# ading one mor term
#arctan(x) = x - (x**3 / 3) + (x**5 / 5)
ax1 = x - ((x **3)/3) + ((x **5)/5)
et = -((math.atan(x) - ax1) / math.atan(x)) * 100
ea = ((ax1 - ax) / ax1) * 100
print ("et : {:.2f}%, ea = {:.2f}%".format(et,ea))

# ading one mor term
#arctan(x) = x - (x**3 / 3) + (x**5 / 5) - (x**7 / 7)
ax2 = x - ((x **3)/3) + ((x **5)/5) - ((x **7)/7)
et = ((math.atan(x) - ax2) / math.atan(x)) * 100
ea = -((ax2 - ax1) / ax2) * 100
print ("et : {:.2f}%, ea = {:.2f}%".format(et,ea))

print("Hence, it was follen below 0.5%, so no need to add another term")