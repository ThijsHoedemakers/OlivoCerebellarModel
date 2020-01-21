# Functions usefull for data analysis
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def Slicing(data, t_start=None, t_end=None):
    
    output={}
    for label in data.keys():
        nrCell = len(data[label])
        output[label] = [data[label][k][t_start:t_end] for k in range(0,nrCell)]
    
    return output
    
def SlicingSpikes(data, t_start=float("-inf"), t_end=float("inf")):
    
    output={}
    for label in data.keys():
        collection = data[label]
        output[label] = []
        for arr in collection:
            x = np.array(arr)
            output_arr = x[(x>t_start) & (x<t_end)]
            output[label].append(output_arr)
    
    return output

def Connectivity(cell1,cell2,name_cell1,name_cell2):   
    cell1nr =  max(cell1)
    cell2nr = max(cell2)
    len_cell = len(cell1)
    data = np.zeros((cell1nr+1, cell2nr+1)) 

    for p in range(0,len_cell) :  
        data[cell1[p],cell2[p]] = 1
  
    xspace = cell2nr/3
    yspace = cell1nr/2
    fig, ax = plt.subplots(1, 1,figsize=(xspace,yspace))
    ax.set_xticks(np.arange(cell1nr))
    ax.set_xticks(np.arange(cell2nr))
    title = 'Vertical Index = ',name_cell1,'Horizontal Index = ',name_cell2
    ax.set_title(title)
    ax.set_xlabel(name_cell1)
    ax.set_ylabel(name_cell2)
    sns.heatmap(data,cmap='Greys',linewidths=.5,linecolor='white',cbar=False,square=True)
    
    plt.show()
def FreqSpectrum(x):
    spec = np.absolute(np.fft.fft(x))
    leng = int(len(x)/2)
    spec = spec[:leng]  # take positive frequency components
    spec /= len(x)  # normalize
    spec *= 2.0  # to get amplitudes of sine components, need to multiply by 2
    spec[0] /= 2.0  # except for the dc component
    return spec
    