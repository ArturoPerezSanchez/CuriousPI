
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

visualize = True # Switch to activate the visualization of the results
points = []		 # Array to store the generated points in order to visualize them later

# Generate nPoints
for i in range(nPoints):
	randX = random.random() # X axis of the new Point
	randY = random.random() # Y axis of the new Point

	# in order to now if the new point is inside the circle, we calculate the distance of the point
	# to the center of the circle (0.5, 0.5) using the Pythagorean theorem and if the distance is lower
	# than the radious of the circle (0,5), the point is inside, otherwise its outside.
	distance = math.sqrt((randX - 0.5)**2 + (randY - 0.5)**2)
	
	color = 'red' # If the point is outside the circle we paint it red
	if(distance <= 0.5):
		color = 'blue' # Otherwise if the point is inside the circle we paint it blue
		inside +=1

	points.append((randX, randY, color)) # Add the point and its color to the points array to visualize them later

# After generating all the points we only have to use the formula described above to get our aproximation of PI
print("Pi has a value of approximately:", 4*inside/nPoints)


if (visualize):
	# Import matplotlib library for visualization
	import matplotlib.pyplot as plt
    
	# Create a figure with two axes, one for the plot and one for the mathematical formulas
	fig = plt.figure(figsize=(12,6))

	# Background Color
	fig.set_facecolor('lightblue')

	# Create the axes
	ax1 = fig.add_axes([0.1, 0.1, 0.4, 0.8])
	ax2 = fig.add_axes([0.5, 0.1, 0.4, 0.8])

	# Limit the number of plotted points to 500 to avoid performance issues
	points = points[:500]

	# Plot the square 
	square = plt.Rectangle((0, 0), 1, 1, fill=True, facecolor=(0.6, 0.2, 0.3, 0.75), zorder=1)
	ax1.add_patch(square)

	# Plot the inscribed circle
	circle = plt.Circle((0.5, 0.5), 0.5, fill=True, facecolor=(0, 0.6, 1, 0.8), zorder=2)
	ax1.add_patch(circle)

	# Plot the points
	for x, y, color in points:
	    ax1.scatter(x, y, color=color, zorder=3)

	# Limit the visualization view to the size of the square
	ax1.set_xlim(0, 1)
	ax1.set_ylim(0, 1)


	# Add the mathematical formulas in the second axis
	ax2.text(0.6, 0.5, "Area of circle = " + r"$\pi r^2$" + "\n\nArea of square = " +  r"$4 r^2$" + f"\n\nTotal number of points = {nPoints} \n\nPoints inside the circle= {inside}", fontsize=16, ha='center', va='center')
	ax2.text(0.62, 0.1, f"Approximate value of pi: {4*inside/nPoints}", fontsize=20, ha='center', va='bottom', weight='bold')


	# Remove the axis
	ax2.axis('off')

	# Show the visualization
	plt.show()

