# Import the libraries
import random
import math

# Take the number of steps from the user
N = int(input("Enter the total number of steps: "))

# Define a function for calculating rms distance
def rms(x0, y0, x1, y1):
    rms = math.sqrt((x1-x0)**2 +(y1-y0)**2)
    return rms

# Define the directions 
east, south = 1, 2
west, north = 3, 4

# Define the origin
xi, yi = 0, 0

# Walker Code
x = xi
y = yi
x_steps = []
y_steps = []
for j in range(0, N):
    R = random.randint(1,4)
    if R == east:
            x += -1
    elif R == south:
            y += -1   
    elif R == west:
            x += 1
    elif R == north:
            y += 1
    x_steps.append(x)
    y_steps.append(y)

# Proof for the relation between distance traveled and growing number of N's
rmsvalue = []
sqrtofN = []
for n in range(0, N):
  xf = x_steps[n]
  yf = y_steps[n]
  rmsval = rms(xi,yi,xf,yf)
  rmsvalue.append(rmsval)

for i in range(1, N+1):
  sqrtN = math.sqrt(i)
  sqrtofN.append(sqrtN)

# Printing all the outputs
for j in range(0, N):
    print("------------------------------------------------")
    print("Final Point :  ", (x_steps[j], y_steps[j]))
    print("The Number of Steps : ", j+1)
    print("RMS Distance : ", rmsvalue[j])
    print("Sqrt of N : ", sqrtofN[j])

