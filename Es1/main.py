import seaborn as sns 
import matplotlib.pyplot as plt

def crea_istogramma_grafico():
    
    hist = sns.load_dataset("attention")
    sns.catplot(x="score", kind="count", data=hist);
    plt.show()
    
def crea_istogramma(a):
    
    for i in range(len(a)):
        print('\n')
        for j in range(a[i]):
            print('*', end=" ")
    print('\n')

          
           
a=[3,7,9,5]
 
crea_istogramma(a)
crea_istogramma_grafico()


