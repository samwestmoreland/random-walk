import numpy as np
import matplotlib.pyplot as plt

gravity = 1 # a number between 0 and 1
dims = 200
particles = 100000
steps = 1000
draw_every = 300
np.random.seed = 2342354

def force(pos):
    global dims
    distance = pos - dims/2
    if distance > 0:
        return gravity/(distance**2)
    if distance < 0:
        return -gravity/(distance**2)
    return 0

def calculate_new(x):
    global dims
    new_x = 0
    rand3 = np.random.randint(3) - 1
    rand2 = np.random.randint(2) # For boundaries
    if x - 1 < 0:
        new_x = x + rand2
    elif x + 1 >= dims:
        new_x = x - rand2
    else: # We are not on a boundary
        rand = np.random.rand()
        left, right = 0.33, 0.67
        left += left * force(x)
        right += right * force(x)
        if rand < left:
            new_x = x - 1
        elif rand > right:
            new_x = x + 1
        else:
            new_x = x
    return new_x

fg = plt.figure()
ax = fg.gca()

arr = np.zeros((dims,dims))
im = ax.imshow(arr, cmap='Greys')
for i in range(particles):
    x = int(np.random.rand(1)*len(arr))
    y = int(np.random.rand(1)*len(arr[0]))
    if arr[x][y] == 1:
        continue
    arr[x][y] = 1
    for j in range(steps):
        if (x+1 < len(arr) and arr[x+1][y] == 1) \
        or (x-1 >= 0 and arr[x-1][y] == 1) \
        or (y+1 < len(arr[0]) and arr[x][y+1] == 1) \
        or (y-1 >= 0 and arr[x][y-1] == 1) \
        or (x+1 < len(arr) and y+1 < len(arr) and arr[x+1][y+1] == 1) \
        or (x+1 < len(arr) and y-1 >= 0 and arr[x+1][y-1] == 1) \
        or (x-1 >= 0 and y+1 < len(arr) and arr[x-1][y+1] == 1) \
        or (x-1 >= 0 and y-1 >= 0 and arr[x-1][y-1] == 1):
            break

        new_x = calculate_new(x)
        new_y = calculate_new(y)

        arr[x][y] = 0
        x, y = new_x, new_y
        arr[x][y] = 1

        if i%draw_every == 0:
            im.set_data(arr)
            plt.draw(), plt.pause(1e-2)
            im.autoscale()

plt.show()
