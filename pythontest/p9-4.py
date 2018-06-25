import matplotlib.pyplot as plt
steps = [6543, 7000, 8900, 10789, 3467, 11045, 5095]
labels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
num_bars = len(steps)
positions = range(1, num_bars+1)
plt.bar(positions, steps, align='center')
plt.xticks(positions, labels)
plt.xlabel('Steps')
plt.ylabel('Day')
plt.title('Number of steps walked')
plt.grid()
plt.show()
>>>>>>> 3e856e3f8057d40dc84ff639e05a83d6844e5abd
