import numpy as np
from matplotlib import pyplot as plt
import statistics
import math


def sigm(x):
    return 1/(1+np.exp(-x))

def normalized_sigmoid_fkt(a, b, x):
    s= 1/(1+np.exp(b*(x-a)))  
    return 1*(s-min(s))/(max(s)-min(s)) # normalize function to 0-1def 
 
def draw_function_on_2x2_grid(x):     
     fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)   
     plt.subplots_adjust(wspace=.5)    
     plt.subplots_adjust(hspace=.5)    
     ax1.plot(x, normalized_sigmoid_fkt( .5, 18, x))    
     ax1.set_title('1')    
     ax2.plot(x, normalized_sigmoid_fkt(0.518, 10.549, x))    
     ax2.set_title('2')    
     ax3.plot(x, normalized_sigmoid_fkt( .7, 11, x))    
     ax3.set_title('3')    
     ax4.plot(x, normalized_sigmoid_fkt( .2, 14, x))    
     ax4.set_title('4')   
     plt.suptitle('Different normalized (sigmoid) function',size=10 )    
     return fig
 
x = np.linspace(0,1,100) 
Travel_function = draw_function_on_2x2_grid(x)
print('Per x=0.458 si ha=', sigm(0.458))

#Funzione sigmoide da libreria