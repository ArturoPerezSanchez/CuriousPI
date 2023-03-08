
# Generating Random Points
'''
	The main idea is to generate random points inside a 1x1 square with an inscribed circle.

	-> We know that the area of the square is side*side and since the side coincides with the diameter of the circle (2 times the radius), the area of the square is (2*r)^2 = 4r^2

	-> We also know that the area of the circle is π*r^2

	-> The relation between the two areas would be (π*r^2)/(4r^2), which simplified is π/4

	If we generate random points within the square, the ratio of points within the inscribed circle to the total of points should get closer and closer to the ratio between the two areas as we generate more points.
	Therefore, we have that for large values of total_points: π/4 ≈ points_inside_circle/total_points
	From which we can solve for pi: π ≈ 4*(points_inside_circle/total_points)
'''

import random # Used to generate random points
import math   # Used to perform basic gemotry calculations


inside = 0 		 # Number of points inside the circle
nPoints = 100000 # Total number of points

# Generate nPoints
for i in range(nPoints):
    randX = random.random() # X axis of the new Point
    randY = random.random() # Y axis of the new Point

    # in order to now if the new point is inside the circle, we calculate the distance of the point
    # to the center of the circle (0.5, 0.5) using the Pythagorean theorem and if the distance is lower
    # than the radious of the circle (0,5), the point is inside, otherwise its outside.
    distance = math.sqrt((randX - 0.5)**2 + (randY - 0.5)**2)
    
    if(distance <= 0.5):
        inside +=1

# After generating all the points we only have to use the formula described above to get our aproximation of PI
print("Pi has a value of approximately:", 4*inside/nPoints)