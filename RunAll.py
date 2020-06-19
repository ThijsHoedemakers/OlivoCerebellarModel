import sys
from A_Functions import *
import h5py

freq = int(sys.argv[1])
print(freq)
simulation = int(sys.argv[2])

data = h5py.File("Data_Collection.hdf5",'a')

simtype = ['initial', 'plasticity','adapted']
namenoise = str(freq)+'Hz_'+simtype[simulation]
print(namenoise)
## input of NoiseGenerator for double sine is :
# (amount of noise sources, 'DS', [offset sine1,offset sine2,amplitude sine1 (nA), frequency sine1(Hz),,
#amplitude sine2, frequency sine2], duration in ms, name of the file)

## input of NoiseGenerator for OU is :
# (amount of noise sources, 'OU', [initial I, initial I0, sigma], duration in ms, name of the file)

## input of NoiseGenerator Constant value :
# (amount, 'const',[constant value in nA], duration in ms, name of the file)

Noise_t,Noise_I,N_Noise=NoiseGenerator(2,'DS',[0.2,0.2    # offset in nA
                                               ,0.2,0.2 # amplitude in nA
                                               ,freq,freq   # frequency in Hz
                                              ],5000,15000,20000,
                                       namenoise,'no',simtype[simulation],freq)

#Noise_t,Noise_I,N_Noise=NoiseGenerator(5,'DS',[1 ,0.5, 0, -0.5, -1,     #offsets in nA
#                                              1, 0.5, 0, 0.5, 1, #amplitude in nA
#                                              20, 2, 2, 20, 2]         # frequency in Hz
#                                              ,2500,namenoise,simparameter)

#Noise_const15 = NoiseGenerator(2,'const',[1.5],10,'Noise_const15')


######################## Saving SimParams
#with open(name, 'wb') as sims:
#    pickle.dump(SimParams,sims, pickle.HIGHEST_PROTOCOL)
#sio.savemat('SimParams.mat', mdict={'SimParams': SimParams})

if namenoise.find('initial') != -1:
    print('intial run - no Plasticity')
    from E_Synapses_NoPlasticity import *
elif namenoise.find('adapt') != -1:
    print('adapted network - no Plasticity')
    from E_Synapses_NoPlasticity import *
elif namenoise.find('plasticity') != -1:
    print('adaptation - Plasticity')
    from E_New_Plasticity import *
    
else:
    print('relook at name of namenoise')
    
run(exp_runtime,report='text')


if namenoise.find('initial') != -1:
    from F_save_data_NoPlasticity import *
elif namenoise.find('adapt') != -1:
    from F_save_data_NoPlasticity import *
elif namenoise.find('plasticity') != -1:
    from F_save_data_Plasticity import *
else:
    print('something is wrong but it should have appeared earlier, weird af')

    
