import numpy
from scipy import stats
import matplotlib.pyplot

speed=[99,96,65,25,98,97,102,110,103,85,70,85]

x=numpy.mean(speed)
print(x)
x=numpy.median(speed)
print(x)
x=stats.mode(speed)
print(x)
x=numpy.std(speed)
print(x)
x=numpy.var(speed)
print(x)
x=numpy.percentile(speed,70)
print(x)

x=numpy.random.uniform(0.0, 5.0, 100000)
plt.hist(x, 100)
plt.show()

x=[5,7,8,7,2,17,2,9,4,11,12,9,6]
y=[99,86,87,88,111,86,103,87,94,78,77,85,86]

matplotlib.pyplot.scatter(x, y)
matplotlib.pyplot.show()
