import matplotlib.pyplot as plt

# Read points from the file
with open("points.txt", "r") as file:
    points = [line.strip().split() for line in file]

# Convert points to float
x_coords = [float(p[0]) for p in points]
y_coords = [float(p[1]) for p in points]

# Plot the points
plt.scatter(x_coords, y_coords, s=1)  # Small dots for each point

# Plot the line
plt.plot([3, 6], [1, 4], 'r--', label='Line joining (3,1) and (6,4)')  # Line in red dashed

plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Points on the Line Segment')
plt.legend()
plt.savefig('../figs/fig.png')
plt.grid(True)

plt.show()

