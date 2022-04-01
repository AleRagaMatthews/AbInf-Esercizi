import numpy as np
from matplotlib import pyplot as plt
import statistics
import math

data=np.loadtxt('ex2.txt')

year, t, tmin, tmax, p = data.T


y=[]
tmin=[]
tmax=[]

for i in range(len(data)):
    for j in range(5):
        if j==0:
            y.append(data[i][j])
        if j==2:
            tmin.append(data[i][j])
        if j==3:
            tmax.append(data[i][j])
            
            
mediatmin=statistics.mean(tmin)
mediatmax=statistics.mean(tmax)

sommatmin=0
sommatmax=0

for i in range(len(data)):
    sommatmin+=(tmin[i]-mediatmin)**2
    sommatmax+=(tmax[i]-mediatmax)**2
    
    
std_calc_tmin=math.sqrt(sommatmin/(len(data)-1))
std_calc_tmax=math.sqrt(sommatmax/(len(data)-1))

std_tmin=statistics.pstdev(tmin)
std_tmax=statistics.pstdev(tmax)

print('Calcolata std Tmin', std_calc_tmin)
print('Calcolata std Tmax',std_calc_tmax)
print('Con funzioni std Tmin',std_tmin)
print('Con funzioni std Tmax',std_tmax)

import numpy as np
from matplotlib import pyplot as plt
import statistics
import math

data=np.loadtxt('ex2.txt')

year, t, tmin, tmax, p = data.T

plt.plot(year, tmin, year, tmax) 
plt.legend(('Tmin', 'Tmax'), loc=(1.05, 0.5))
plt.show()

y=[]
tmin=[]
tmax=[]

for i in range(len(data)):
    for j in range(5):
        if j==0:
            y.append(data[i][j])
        if j==2:
            tmin.append(data[i][j])
        if j==3:
            tmax.append(data[i][j])
            
            
mediatmin=statistics.mean(tmin)
mediatmax=statistics.mean(tmax)

sommatmin=0
sommatmax=0

for i in range(len(data)):
    sommatmin+=(tmin[i]-mediatmin)**2
    sommatmax+=(tmax[i]-mediatmax)**2
    
    
std_calc_tmin=math.sqrt(sommatmin/(len(data)-1))
std_calc_tmax=math.sqrt(sommatmax/(len(data)-1))

std_tmin=statistics.pstdev(tmin)
std_tmax=statistics.pstdev(tmax)

print('Calcolata std Tmin', std_calc_tmin)
print('Calcolata std Tmax',std_calc_tmax)
print('Con funzioni std Tmin',std_tmin)
print('Con funzioni std Tmax',std_tmax)

plt.plot(year, tmin, year, tmax) 
plt.legend(('Tmin', 'Tmax'), loc=(1.05, 0.5))
plt.show()


