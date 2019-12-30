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


# This represents the noise-PC synapses:
n_Noise = len(Noise)
n_PC = len(PC_Coupled_STDP)
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
copy_noise_Coupled.connect('noise_source_post == i')

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
S_N_PC_Coupled.connect('conn_target_pre == j')

# LTD from IO cells:
S_IO_N_Coupled = Synapses(IO_Coupled_STDP, conn_N_PC_Coupled, on_pre='a_IO_post += A_IO*abs((new_weight_post*I_post))/nA', method='euler',name = 'dummy_IO_Coupled',dt=t_Neuron)  # where f is some function
# weight of all noise-Purkinje synapses:
IO_index = random.sample(range(N_Cells_IO), 10)
S_IO_N_Coupled.connect(i=IO_index*n_Noise, j=range(len(conn_N_PC_Coupled)))

Synapse_IO_PC_Coupled_STDP = Synapses(IO_Coupled_STDP, PC_Coupled_STDP, on_pre ='w_post +=(0.005*nA)', delay=2*ms, name = 'IO_PC_Synapse_Coupled_STDP',method = 'euler',dt=t_Neuron)
Synapse_IO_PC_Coupled_STDP.connect(i=IO_index, j=range(n_PC))

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

DCN_PC_Synapse_Coupled_STDP.connect(i=DCN_PC_Synapse_Coupled_targ,j=DCN_PC_Synapse_Coupled_mm)

IO_DCN_Synapse_Coupled_STDP = Synapses(DCN_Coupled_STDP, IO_Coupled_STDP, on_pre = 'I_IO_DCN_post += -(1/(N_Cells_IO*(N_Cells_DCN/2)))*uA*cm**-2', delay=3*ms, name = 'IO_DCN_Synapse_Coupled_STDP', method = 'euler',dt=t_Neuron)
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
IO_DCN_Synapse_Coupled_STDP.connect(i=IO_DCN_Synapse_Coupled_targ,j=IO_DCN_Synapse_Coupled_mm)


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
copy_noise_Uncoupled.connect('noise_source_post == i')

# Synapses to Purkinje cells
#S_N_PC_Uncoupled = Synapses(conn_N_PC_Uncoupled, PC_Uncoupled_STDP,'''    
#                                    I_Noise_post = (1.0/n_Noise)*(new_weight_pre)*I_pre : amp (summed)''',
#                            on_post='a_PC_pre += A_PC', method='euler',name = 'dummy_PC_Uncoupled',dt=dt)

S_N_PC_Uncoupled = Synapses(conn_N_PC_Uncoupled, PC_Uncoupled_STDP,'''    
                                    I_Noise_post = (new_weight_pre)*I_pre : amp (summed)''',
                            on_post='a_PC_pre += A_PC', method='euler',name = 'dummy_PC_Uncoupled',dt=dt)
# "connect if PC target label matches target index":
S_N_PC_Uncoupled.connect('conn_target_pre == j')

# LTD from IO cells:
S_IO_N_Uncoupled = Synapses(IO_Uncoupled_STDP, conn_N_PC_Uncoupled, on_pre='a_IO_post += A_IO*abs((new_weight_post*I_post))/nA', method='euler',name = 'dummy_IO_Uncoupled',dt=dt)  # where f is some function
# weight of all noise-Purkinje synapses:
# IO_index = random.sample(range(20), 10)
S_IO_N_Uncoupled.connect(i=IO_index*n_Noise, j=range(len(conn_N_PC_Uncoupled)))

Synapse_IO_PC_Uncoupled_STDP = Synapses(IO_Uncoupled_STDP, PC_Uncoupled_STDP, on_pre ='w_post +=(0.005*nA)', delay=2*ms, name = 'IO_PC_Synapse_Uncoupled_STDP',method = 'euler',dt=t_Neuron)
Synapse_IO_PC_Uncoupled_STDP.connect(i=IO_index, j=range(n_PC))

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
DCN_PC_Synapse_Uncoupled_STDP.connect(i=DCN_PC_Synapse_Coupled_targ,j=DCN_PC_Synapse_Coupled_mm)

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
IO_DCN_Synapse_Uncoupled_STDP.connect(i=IO_DCN_Synapse_Coupled_targ,j=IO_DCN_Synapse_Coupled_mm)


eqs_IO_syn_Uncoupled_STDP = ''' I_c_pre = (0*mS/cm**2)*(0.6*e**(-((Vd_pre/mvolt-Vd_post/mvolt)/50)**2) + 0.4)*(Vd_pre-Vd_post) : metre**-2*amp (summed)'''
IO_synapse_Uncoupled_STDP = Synapses(IO_Uncoupled_STDP, IO_Uncoupled_STDP, eqs_IO_syn_Uncoupled_STDP, name = 'IO_Synapse_Uncoupled_STDP')
IO_synapse_Uncoupled_STDP.connect()

