# Functions usefull for data analysis
import numpy as np
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