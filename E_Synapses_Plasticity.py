from D_NeuronGroups_Plasticity import *
###########################################################################################################################
###########################################################################################################################
##################################################### COUPLED SCENARIO ####################################################
###########################################################################################################################
###########################################################################################################################
#####################################################################
############################ Synapses ###############################
#####################################################################
tau_PC = 20*ms
tau_IO = 60*ms
wmax = 0.3
A_PC = 1/float(exp_runtime/msecond)
A_IO = -1/float(exp_runtime/msecond)#Apre*taupre/taupost*1.05
n_Noise = len(Noise)
n_PC = len(PC_Coupled_STDP)
### Fixed connectivity

# input-dummy 
i_ind = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
j_ind = np.arange(n_Noise*n_PC)

# dummy-PC
i_dPC = np.arange(n_Noise*n_PC)
j_dPC = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# IO - dummy 
i_IOd = [9, 10, 18, 17, 0, 6, 5, 12, 16, 11, 9, 10, 18, 17, 0, 6, 5, 12, 16, 11, 9, 10, 18, 17, 0, 6, 5, 12, 16, 11, 9, 10, 18, 17, 0, 6, 5, 12, 16, 11, 9, 10, 18, 17, 0, 6, 5, 12, 16, 11]
j_IOd=np.arange(n_Noise*n_PC)

# IO - PC
i_IOPC = [9,10, 18, 17, 0, 6, 5, 12, 16, 11]
j_IOPC = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# DCN - IO
i_DCNIO = [0, 0 ,0, 0 ,0,0 ,0, 0,0,0,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,9 ,10 ,10 ,10 ,10 ,10 ,10 ,10 ,10 ,10 ,10 ,11 ,11 ,11 ,11 ,11 ,11 ,11 ,11 ,11 ,11 ,12 ,12 ,12 ,12 ,12 ,12 ,12 ,12 ,12 ,12 ,13 ,13 ,13 ,13 ,13 ,13 ,13 ,13 ,13 ,13 ,14 ,14 ,14 ,14,14 ,14 ,14 ,14 ,14 ,14 ,15 ,15 ,15 ,15 ,15 ,15 ,15 ,15 ,15 ,15 ,16 ,16 ,16 ,16 ,16 ,16 ,16 ,16 ,16 ,16 ,17 ,17 ,17 ,17 ,17 ,17 ,17 ,17 ,17 ,17 ,18 ,18 ,18 ,18 ,18 ,18 ,18 ,18 ,18 ,18 ,19 ,19,19 ,19 ,19 ,19 ,19 ,19 ,19 ,19]
j_DCNIO = [5 ,7, 10, 15 ,4 ,6 ,9 ,3 ,1, 11 ,8 ,4 ,11, 17, 14 ,9 ,3 ,2 ,0, 15 ,0 ,3 ,7 ,2 ,9 ,10, 19, 17 ,4 ,14 ,2 ,8, 16 ,3 ,5, 19, 12 ,0, 18, 17, 12 ,9 ,6, 10, 13 ,3 ,4 ,2, 15, 18 ,2, 14, 19, 18, 16, 17 ,5 ,8 ,4 ,9, 14 ,6 ,8, 16, 12, 19 ,4 ,5 ,0 ,3, 16 ,9,13 ,1, 17 ,0 ,8, 14 ,7, 10, 10 ,6, 13 ,1 ,4, 18 ,8, 12, 17 ,0 ,7, 11 ,3 ,1 ,9, 10,6, 17, 13, 18 ,8, 16 ,7 ,1 ,6, 12, 10, 19, 15 ,4, 12 ,2 ,4 ,1, 19, 13, 17, 16 ,8 ,9, 12 ,4 ,3 ,1 ,0 ,8 ,2, 11, 14, 13, 10, 17, 12, 13, 16, 11 ,4 ,2 ,8 ,5, 15, 17, 13, 19, 14 ,1 ,4, 16 ,6 ,3 ,5, 16 ,0, 19 ,2 ,9, 18 ,6 ,4 ,1, 10 ,8, 15 ,3 ,0 ,1 ,4, 13, 19 ,7 ,3 ,9, 14, 18, 16, 17 ,5, 19, 11, 10, 11 ,6, 15, 10 ,5, 12, 17 ,4 ,8, 16, 14 ,8,
 10, 15, 4, 11 ,2 ,7 ,5, 18]

# PC - DCN
i_PCDCN = [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,3 ,3 ,3 ,3 ,3 ,3 ,3
 ,3 ,3 ,3 ,4 ,4 ,4 ,4 ,4 ,4 ,4 ,4 ,4 ,4 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,7 ,7 ,7 ,7
 ,7 ,7 ,7 ,7 ,7 ,7 ,8 ,8 ,8 ,8 ,8 ,8 ,8 ,8 ,8 ,8 ,9 ,9 ,9 ,9 ,9 ,9 ,9 ,9 ,9 ,9]
j_PCDCN = [15, 10, 18 ,3 ,8 ,7 ,1 ,4, 16 ,2 ,4, 14, 12, 10 ,2, 13 ,3 ,0, 15, 16 ,5 ,9 ,0, 13,14, 11, 15, 17, 16, 10, 16 ,1, 13, 17 ,9 ,3 ,5, 10, 12, 18 ,4, 12, 18 ,2 ,5, 13, 15 ,7 ,1 ,6 ,8, 16, 17 ,1, 13, 12, 15 ,7 ,4 ,2, 17 ,0, 14 ,7 ,3, 19 ,4 ,9 ,5 ,2, 18 ,4 ,0, 11, 15 ,3 ,9 ,1 ,8 ,2 ,19 ,1 ,11, 10 ,6 ,0 ,9, 17, 12 ,3 ,7, 11, 17 ,1 ,2, 14,5 ,4, 12 ,0]
# This represents the noise-PC synapses:

conn_N_PC_Coupled = NeuronGroup(n_Noise*n_PC, eqs_syn_Noise_PC_STDP, method='euler',name = 'dummy_Coupled',dt=t_Neuron)
mon_N_PC_Coupled = StateMonitor(conn_N_PC_Coupled , ['a_PC','a_IO','noise_source','PC_target','weight','I','delta_weight','new_weight'], record=True, dt=t_Monitor)
# Set up the labels
conn_N_PC_Coupled.noise_source = 'i // n_PC'  # i.e., 0, 0, 1, 1, 2, 2, ...
conn_N_PC_Coupled.PC_target = 'i % n_Noise' # i.e., 0, 1, 2, 3, 4, 0, 1, ...
conn_N_PC_Coupled.conn_target = 'i % n_PC' # i.e., 0, 1, 0, 1, 0, 1, 0, 1, 0, 1
conn_N_PC_Coupled.indx = 'conn_target+(10*rand())'
# Set the static weight in some way (can refer to noise_source and PC_target)
#original
conn_N_PC_Coupled.weight = '1-(abs(((conn_target-noise_source)/N_Cells_PC)))'
print('weights before', conn_N_PC_Coupled.weight)
# reshape the values to a matrix of size [#input #PC]
norm_coupled=conn_N_PC_Coupled.weight[:].reshape(n_Noise,n_PC)
print('reshaped weigth',norm_coupled)
# calculate the sum of the column
column_sum= norm_coupled.sum(axis=0)
print('column sum =', column_sum)
# normalize by the weight of the columns
reshaped_weight = norm_coupled/ column_sum[np.newaxis,:]
# reshape it to the form of 'conn_N_PC_Coupled.weight'
reshaped_weight = reshaped_weight.reshape(n_Noise*n_PC)

conn_N_PC_Coupled.weight=reshaped_weight
#all_weights.reshape(n_PC,n_Noise)
#print(all_weights)
# "Synapses" to copy over the noise current
copy_noise_Coupled = Synapses(Noise_extended, conn_N_PC_Coupled, 'I_post = I_pre : amp (summed)')
# "connect if noise source label matches source index":
copy_noise_Coupled.connect(i=i_ind, j=j_ind)

## uncomment to see connectivity Noise-Dummyneuron
#visualise(copy_noise_Coupled)
print('new weights', conn_N_PC_Coupled.weight)

# Synapses to Purkinje cells
# original
#S_N_PC_Coupled = Synapses(conn_N_PC_Coupled, PC_Coupled_STDP,'''    
#                                    I_Noise_post = (1.0/n_Noise)*(new_weight_pre)*I_pre : amp (summed)''',
#                            on_post='a_PC_pre += A_PC', method='euler',name = 'dummy_PC_Coupled',dt=t_Neuron)

# removed (1.0/n_Noise) since it is already normalized in the previous step
S_N_PC_Coupled = Synapses(conn_N_PC_Coupled, PC_Coupled_STDP,'''    
                                    I_Noise_post = (new_weight_pre)*I_pre : amp (summed)''',
                            on_post='a_PC_pre += A_PC', method='euler',name = 'dummy_PC_Coupled',dt=t_Neuron)
# "connect if PC target label matches target index":
S_N_PC_Coupled.connect(i=i_dPC,j =j_dPC)

# LTD from IO cells:
S_IO_N_Coupled = Synapses(IO_Coupled_STDP, conn_N_PC_Coupled, on_pre='a_IO_post += A_IO*abs((new_weight_post*I_post))/nA', method='euler',name = 'dummy_IO_Coupled',dt=t_Neuron)  # where f is some function
# weight of all noise-Purkinje synapses:
IO_index = random.sample(range(N_Cells_IO), 10)
S_IO_N_Coupled.connect(i=i_IOd, j=j_IOd)

Synapse_IO_PC_Coupled_STDP = Synapses(IO_Coupled_STDP, PC_Coupled_STDP, on_pre ='w_post +=(0.005*nA)', delay=2*ms, name = 'IO_PC_Synapse_Coupled_STDP',method = 'euler',dt=t_Neuron)
Synapse_IO_PC_Coupled_STDP.connect(i=i_IOPC, j=j_IOPC)

DCN_PC_Synapse_Coupled_STDP = Synapses(PC_Coupled_STDP, DCN_Coupled_STDP, on_pre='I_PC_post = 1.5*nA', delay=2*ms, name = 'PC_DCN_Synapse_Coupled_STDP',dt=t_Neuron) 
DCN_PC_Synapse_Coupled_a = list(range(N_Cells_DCN))
DCN_PC_Synapse_Coupled_m=[]
# 1 PC synapse onto 10 random DCN - DCN receives max 10 inputs
for ii in range(0,N_Cells_PC):
    DCN_PC_Synapse_Coupled_m.append(random.sample(DCN_PC_Synapse_Coupled_a, 10))
    for jj in range(0,N_Cells_PC):
        if DCN_PC_Synapse_Coupled_m.count(jj) == 10:
            if jj not in a:
                continue
            DCN_PC_Synapse_Coupled_a.remove(jj)
DCN_PC_Synapse_Coupled_mm = []
for kk in range(len(DCN_PC_Synapse_Coupled_m)):
    DCN_PC_Synapse_Coupled_mm = DCN_PC_Synapse_Coupled_mm+DCN_PC_Synapse_Coupled_m[kk]
i = range(N_Cells_PC)
DCN_PC_Synapse_Coupled_targ = []
for kk in range(N_Cells_PC):
    
    # why range(10) -> 10 specifically?
    
    for ee in range(10): 
        DCN_PC_Synapse_Coupled_targ.append(kk)

DCN_PC_Synapse_Coupled_STDP.connect(i=i_PCDCN,j=j_PCDCN)

IO_DCN_Synapse_Coupled_STDP = Synapses(DCN_Coupled_STDP, IO_Coupled_STDP, on_pre = 'I_IO_DCN_post += -0.05*uA*cm**-2', delay=3*ms, name = 'IO_DCN_Synapse_Coupled_STDP', method = 'euler',dt=t_Neuron)
# before : currently -0.005 uA*cm**-2 =(1/(N_Cells_IO*(N_Cells_DCN/2)))
# tried efforts: -0.5   : Result: no IO spike : Conclusion too large
# IO_DCN_Synapse_Coupled_STDP.connect(j='k for k in range(i,i+int(N_Cells_IO/2))', skip_if_invalid=True)
# IO_DCN_Synapse_Coupled_STDP.connect(j='k for k in range(i-int(N_Cells_IO/2)) if i>int(N_Cells_IO/2)')
IO_DCN_Synapse_Coupled_a = list(range(N_Cells_DCN))
IO_DCN_Synapse_Coupled_m=[]
for ii in range(0,N_Cells_DCN):
    if size(IO_DCN_Synapse_Coupled_a) == 10:
        break
    IO_DCN_Synapse_Coupled_m.append(random.sample(IO_DCN_Synapse_Coupled_a, 10))
    for jj in range(0,N_Cells_DCN):
        if IO_DCN_Synapse_Coupled_m.count(jj) == 10:
            if jj not in IO_DCN_Synapse_Coupled_a:
                continue
            IO_DCN_Synapse_Coupled_a.remove(jj)
IO_DCN_Synapse_Coupled_mm = []
for kk in range(len(IO_DCN_Synapse_Coupled_m)):
    IO_DCN_Synapse_Coupled_mm = IO_DCN_Synapse_Coupled_mm+IO_DCN_Synapse_Coupled_m[kk]
IO_DCN_Synapse_Coupled_i = range(N_Cells_DCN)
IO_DCN_Synapse_Coupled_targ = []
for kk in range(N_Cells_DCN):
    for ee in range(10):
        IO_DCN_Synapse_Coupled_targ.append(kk)
IO_DCN_Synapse_Coupled_STDP.connect(i=i_DCNIO,j=j_DCNIO)


IO_synapse_Coupled_STDP = Synapses(IO_Coupled_STDP, IO_Coupled_STDP, eqs_IO_syn_Coupled, name = 'IO_Synapse_Coupled_STDP')
IO_synapse_Coupled_STDP.connect()
###########################################################################################################################
###########################################################################################################################
################################################### UNCOUPLED SCENARIO ####################################################
###########################################################################################################################
###########################################################################################################################
#####################################################################
############################ Synapses ###############################
#####################################################################
# This represents the noise-PC synapses:
n_Noise = len(Noise)
n_PC = len(PC_Uncoupled_STDP)
conn_N_PC_Uncoupled = NeuronGroup(n_Noise*n_PC, eqs_syn_Noise_PC_STDP, method='euler',name = 'dummy_Uncoupled',dt=t_Neuron)
mon_N_PC_Uncoupled = StateMonitor(conn_N_PC_Uncoupled , ['a_PC','a_IO','noise_source','PC_target','weight','I','delta_weight','new_weight'], record=True)
# Set up the labels
conn_N_PC_Uncoupled.noise_source = 'i // n_PC'  # i.e., 0, 0, 1, 1, 2, 2, ...
conn_N_PC_Uncoupled.PC_target = 'i % n_Noise' # i.e., 0, 1, 2, 3, 4, 0, 1, ...
conn_N_PC_Uncoupled.conn_target = 'i % n_PC' # i.e., 0, 1, 0, 1, 0, 1, 0, 1, 0, 1
conn_N_PC_Uncoupled.indx = 'conn_target+(10*rand())'
# Set the static weight in some way (can refer to noise_source and PC_target)
conn_N_PC_Uncoupled.weight = 'abs(1-(abs(((conn_target-noise_source)/N_Cells_PC))))'

norm_uncoupled=conn_N_PC_Uncoupled.weight[:].reshape(n_Noise,n_PC)
# calculate the sum of the column
column_sumun= norm_uncoupled.sum(axis=0)
# normalize by the weight of the columns
reshaped_weightun = norm_uncoupled/ column_sumun[np.newaxis,:]
# reshape it to the form of 'conn_N_PC_Coupled.weight'
reshaped_weightun = reshaped_weightun.reshape(n_Noise*n_PC)

conn_N_PC_Uncoupled.weight=reshaped_weightun
# "Synapses" to copy over the noise current
copy_noise_Uncoupled = Synapses(Noise_extended, conn_N_PC_Uncoupled, 'I_post = I_pre : amp (summed)')
# "connect if noise source label matches source index":
copy_noise_Uncoupled.connect(i=i_ind, j=j_ind)

# Synapses to Purkinje cells
#S_N_PC_Uncoupled = Synapses(conn_N_PC_Uncoupled, PC_Uncoupled_STDP,'''    
#                                    I_Noise_post = (1.0/n_Noise)*(new_weight_pre)*I_pre : amp (summed)''',
#                            on_post='a_PC_pre += A_PC', method='euler',name = 'dummy_PC_Uncoupled',dt=dt)

S_N_PC_Uncoupled = Synapses(conn_N_PC_Uncoupled, PC_Uncoupled_STDP,'''    
                                    I_Noise_post = (new_weight_pre)*I_pre : amp (summed)''',
                            on_post='a_PC_pre += A_PC', method='euler',name = 'dummy_PC_Uncoupled',dt=dt)
# "connect if PC target label matches target index":
S_N_PC_Uncoupled.connect(i=i_dPC,j =j_dPC)

# LTD from IO cells:
S_IO_N_Uncoupled = Synapses(IO_Uncoupled_STDP, conn_N_PC_Uncoupled, on_pre='a_IO_post += A_IO*abs((new_weight_post*I_post))/nA', method='euler',name = 'dummy_IO_Uncoupled',dt=dt)  # where f is some function
# weight of all noise-Purkinje synapses:
# IO_index = random.sample(range(20), 10)
S_IO_N_Uncoupled.connect(i=i_IOd, j=j_IOd)

Synapse_IO_PC_Uncoupled_STDP = Synapses(IO_Uncoupled_STDP, PC_Uncoupled_STDP, on_pre ='w_post +=(0.005*nA)', delay=2*ms, name = 'IO_PC_Synapse_Uncoupled_STDP',method = 'euler',dt=t_Neuron)
Synapse_IO_PC_Uncoupled_STDP.connect(i=i_IOPC, j=j_IOPC)

DCN_PC_Synapse_Uncoupled_STDP = Synapses(PC_Uncoupled_STDP, DCN_Uncoupled_STDP, on_pre='I_PC_post = 1.5*nA', delay=2*ms, name = 'PC_DCN_Synapse_Uncoupled_STDP',dt=t_Neuron) 
# DCN_PC_Synapse_Uncoupled_a = list(range(N_Cells_DCN))
# DCN_PC_Synapse_Uncoupled_m=[]
# for ii in range(0,N_Cells_PC):
#     DCN_PC_Synapse_Uncoupled_m.append(random.sample(DCN_PC_Synapse_Uncoupled_a, 10))
#     for jj in range(0,N_Cells_PC):
#         if DCN_PC_Synapse_Uncoupled_m.count(jj) == 10:
#             if jj not in a:
#                 continue
#             DCN_PC_Synapse_Uncoupled_a.remove(jj)
# DCN_PC_Synapse_Uncoupled_mm = []
# for kk in range(len(DCN_PC_Synapse_Uncoupled_m)):
#     DCN_PC_Synapse_Uncoupled_mm = DCN_PC_Synapse_Uncoupled_mm+DCN_PC_Synapse_Uncoupled_m[kk]
# i = range(N_Cells_PC)
# DCN_PC_Synapse_Uncoupled_targ = []
# for kk in range(N_Cells_PC):
#     for ee in range(10):
#         DCN_PC_Synapse_Uncoupled_targ.append(kk)

# DCN_PC_Synapse_Uncoupled_STDP.connect(i=DCN_PC_Synapse_Uncoupled_targ,j=DCN_PC_Synapse_Uncoupled_mm)
DCN_PC_Synapse_Uncoupled_STDP.connect(i=i_PCDCN,j=j_PCDCN)

IO_DCN_Synapse_Uncoupled_STDP = Synapses(DCN_Uncoupled_STDP, IO_Uncoupled_STDP, on_pre = 'I_IO_DCN_post += -(1/(N_Cells_IO*(N_Cells_DCN/2)))*uA*cm**-2', delay=3*ms, name = 'IO_DCN_Synapse_Uncoupled_STDP', method = 'euler',dt=t_Neuron)
# IO_DCN_Synapse_Uncoupled_STDP.connect(j='k for k in range(i,i+int(N_Cells_IO/2))', skip_if_invalid=True)
# IO_DCN_Synapse_Uncoupled_STDP.connect(j='k for k in range(i-int(N_Cells_IO/2)) if i>int(N_Cells_IO/2)')
# IO_DCN_Synapse_Uncoupled_a = list(range(N_Cells_DCN))
# IO_DCN_Synapse_Uncoupled_m=[]
# for ii in range(0,N_Cells_DCN):
#     if size(IO_DCN_Synapse_Uncoupled_a) == 10:
#         break
#     IO_DCN_Synapse_Uncoupled_m.append(random.sample(IO_DCN_Synapse_Uncoupled_a, 10))
#     for jj in range(0,N_Cells_DCN):
#         if IO_DCN_Synapse_Uncoupled_m.count(jj) == 10:
#             if jj not in IO_DCN_Synapse_Uncoupled_a:
#                 continue
#             IO_DCN_Synapse_Uncoupled_a.remove(jj)
# IO_DCN_Synapse_Uncoupled_mm = []
# for kk in range(len(IO_DCN_Synapse_Uncoupled_m)):
#     IO_DCN_Synapse_Uncoupled_mm = IO_DCN_Synapse_Uncoupled_mm+IO_DCN_Synapse_Uncoupled_m[kk]
# IO_DCN_Synapse_Uncoupled_i = range(N_Cells_DCN)
# IO_DCN_Synapse_Uncoupled_targ = []
# for kk in range(N_Cells_DCN):
#     for ee in range(10):
#         IO_DCN_Synapse_Uncoupled_targ.append(kk)
# IO_DCN_Synapse_Uncoupled_STDP.connect(i=IO_DCN_Synapse_Uncoupled_targ,j=IO_DCN_Synapse_Uncoupled_mm)
IO_DCN_Synapse_Uncoupled_STDP.connect(i=i_DCNIO,j=j_DCNIO)


eqs_IO_syn_Uncoupled_STDP = ''' I_c_pre = (0*mS/cm**2)*(0.6*e**(-((Vd_pre/mvolt-Vd_post/mvolt)/50)**2) + 0.4)*(Vd_pre-Vd_post) : metre**-2*amp (summed)'''
IO_synapse_Uncoupled_STDP = Synapses(IO_Uncoupled_STDP, IO_Uncoupled_STDP, eqs_IO_syn_Uncoupled_STDP, name = 'IO_Synapse_Uncoupled_STDP')
IO_synapse_Uncoupled_STDP.connect()

