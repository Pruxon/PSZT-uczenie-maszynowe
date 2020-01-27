
import matplotlib.pyplot as plt

#
data=[1,6,4,5,88,-5,-20]
plt.plot(data)
plt.ylabel('MSE')
plt.xlabel('EPOKA')


def print_chart(data,filename):
    plt.plot(data)
    plt.ylabel('MSE')
    plt.xlabel('EPOKA')
    plt.savefig('books_read.png')

def print_chart(data):
    plt.plot(data)
    plt.ylabel('MSE')
    plt.xlabel('EPOKA')
    plt.show()