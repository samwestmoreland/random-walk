import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

np.random.seed(3)

def generate_path():
    pass

def gen_rand_line(length):
    line_data = np.empty((2,length))
    line_data[:, 0] = np.random.rand(2)
    print(line_data)
    for index in range(1, length):
        step = (np.random.rand(2) - 0.5)*1
        line_data[:, index] = line_data[:, index-1] + step
        print(line_data)
    return line_data



def main():
    line = gen_rand_line(5)
    print(line)
#    fig = plt.figure()
#    ax = fig.add_subplot()
#    data = [(0,0)]
#    lines = [ax.plot(dat[0, 0:1], dat[1, 0:1])[0] for dat in data]
#    line_ani = animation.FuncAnimation(fig, append_to_path, 100, fargs=(data, lines), interval=50)
#    plt.show()

if __name__ == '__main__':
    main()
