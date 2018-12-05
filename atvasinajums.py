#print(vars())
import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
#print(vars())

from numpy import sin,linspace
#print(vars())

def f(x):
    return sin(x)

x = linspace(0,4,11)
#print(vars())

y = f(x)

legend = []
#print(legend)

from matplotlib import pyplot as plt
#print(plt.plot._doc_)
plt.axis([0,4,-1,1])
plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Funkcijas $sin(x)$ un tas atvasinajumi")
plt.plot(x,y,"k")
legend.append("$sin(x)$ - default - viss ir savienots ar taisnam linijam")
#print(legend)
plt.plot(x,y,"ro")
legend.append("$sin(x)$ - tikai dazhi punkti")
print(legend)

N = len(x)
deltax = x[1] - x[0]
derivative = []

for i in range(N):
    temp = (f(x[i]+deltax)-f(x[i])) / deltax
    derivative.append(temp)
    
plt.plot(x,derivative,"y")
legend.append("$sin(x)$ atvasinajums - viss ir savienots ar taisnam limijam")
plt.plot(x,derivative, "go")
legend.append("$sin(x)$ atvasinajums - dazhi punkti")

derivative_through_array = []
for i in range(N-1):
    temp = (y[i+1] - y[i]) / (x[i+1])
    derivative_through_array.append(temp)

plt.plot(x[0:N-1], derivative_through_array,"m")
legend.append("$sin(x)$ atvasinajums, izmantojot masiva vertibas - viss ir savienots ar taisnam linijam")
plt.plot(x[0:N-1], derivative_through_array, "bo")
legend.append("$sin(x)$ atvasinajums, izmantojot masiva vertibas - dazhi punkti")              



plt.plot(0.680,0.620, 'ch',markersize = 15)
#plt.legend(legend, loc = "lower left")
plt.legend(legend, loc = 3)
plt.show()

