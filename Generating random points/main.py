
import random
import math


inside = 0 
outside = 0
nPoints = 100000


for i in range(nPoints):
    randX = random.random()
    randY = random.random()

    d = math.sqrt((randX - 0.5)**2 + (randY - 0.5)**2)
    color = 'red'
    if(d<=0.5):
        inside +=1

print("Pi has a value of approximately:", 4*inside/nPoints)