import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def seed_point(v):
    x = y = 0
    if np.random.randint(2) == 0:
        x, y = np.random.randint(2) * (len(v)-1), int(np.random.rand() * len(v))
    else:
        y, x = np.random.randint(2) * (len(v)-1), int(np.random.rand() * len(v))

    v[x][y] = 1
    return x, y

def walk_point(x, y, v):
    stepcount = 0
    while stepcount < 50000:
        new_x = new_y = 0

        if x-1 < 0:
            new_x = x + np.random.randint(2)
        elif x+1 >= len(v):
            new_x = x + np.random.randint(2) - 1
        else:
            new_x = x + np.random.randint(3) - 1

        if y-1 < 0:
            new_y = y + np.random.randint(2)
        elif y+1 >= len(v):
            new_y = y + np.random.randint(2) - 1
        else:
            new_y = y + np.random.randint(3) - 1

        v[x][y] = 0
        x, y = new_x, new_y
        v[x][y] = 1

        if (x+1 < len(v) and v[x+1][y] == 1) or (x-1 >= 0 and v[x-1][y] == 1) or (y+1 < len(v[0]) and v[x][y+1] == 1) or (y-1 >= 0 and v[x][y-1] == 1):
            break;

        stepcount += 1

def main():
    v = np.zeros((1000,1000))
    v[int(len(v)/2)][int(len(v)/2)] = 1

    for i in range(4000):
        x, y = seed_point(v)
        walk_point(x, y, v)

    plt.imshow(v)
    plt.show()

if __name__ == '__main__':
    main()
