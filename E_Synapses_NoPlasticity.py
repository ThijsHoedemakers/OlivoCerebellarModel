from D_NeuronGroups_NoPlasticity import *
###########################################################################################################################
###########################################################################################################################
##################################################### COUPLED SCENARIO ####################################################
###########################################################################################################################
###########################################################################################################################
#####################################################################
############################ Synapses ###############################
#####################################################################
n_Noise = len(Noise)
n_PC = len(PC_Coupled_noSTDP)
if n_Noise == 5:
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
    
elif n_Noise == 2:
    # Input-dummy
    i_ind = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    j_ind = np.arange(n_Noise*n_PC)

    # dummy-PC
    i_dPC = np.arange(n_Noise*n_PC)
    j_dPC = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # IO - dummy
    i_IOd = [9,10, 18, 17, 0, 6, 5, 12, 16, 11, 9,10, 18, 17, 0, 6, 5, 12, 16, 11]
    j_IOd=np.arange(n_Noise*n_PC)
    
    # IO - PC
    i_IOPC = [9,10, 18, 17, 0, 6, 5, 12, 16, 11]
    j_IOPC = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # DCN - IO
    i_DCNIO = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,9,10,10,10,10,10,10,10,10,10,10,11,11,11,11,11,11,11,11,11,11,12,12,12,12,12,12,12,12,12,12,13,13,13,13,13,13,13,13,13,13,14,14,14,14,14,14,14,14,14,14,15,15,15,15,15,15,15,15,15,15,16,16,16,16,16,16,16,16,16,16,17,17,17,17,17,17,17,17,17,17,18,18,18,18,18,18,18,18,18,18,19,19,19,19,19,19,19,19,19,19]

    j_DCNIO = [11,4,8,9,14,10,1,7,17,6,9,18,1,0,5,3,6,4,13,2,17,15,4,2,10,16,18,13,19,8,10,4,8,6,3,17,2,19,16,11,19,11,15,2,7,8,4,17,10,1,16,12,15,13,3,0,4,11,1,18,11,8,18,17,12,15,2,5,0,6,15,9,6,8,14,4,18,3,19,12,19,4,14,3,1,11,13,8,15,17,14,16,8,9,11,1,17,2,18,19,12,18,19,10,7,2,13,14,4,5,2,8,5,7,0,13,15,18,6,10,16,3,8,15,1,12,4,7,9,2,10,2,8,5,12,19,16,14,15,4,10,17,13,5,0,18,8,15,4,11,5,12,6,4,2,17,19,14,10,3,17,10,1,15,3,4,7,13,5,16,9,3,15,11,12,0,4,5,7,18,18,2,0,3,9,15,13,1,17,8,14,18,17,3,7,8,9,6,5,13]
    
    # PC - DCN
    i_PCDCN = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,9]
    j_PCDCN = [8,17,13,9,11,14,4,16,1,0,17,5,13,2,3,19,4,7,6,8,15,18,2,8,7,11,0,10,16,17,4,16,19,11,18,7,10,8,5,0,0,17,11,13,3,6,1,8,5,10,19,17,12,15,14,4,8,10,18,11,8,6,1,4,16,5,18,3,2,9,3,9,18,11,14,15,4,17,19,10,6,15,10,5,0,11,9,17,12,2,18,0,3,7,2,16,19,10,5,13]
        
    print('nr of noise is 2')
else:
    print('nr of noise it not 2-5')

S_Coupled_noSTDP = Synapses(Noise, PC_Coupled_noSTDP, eqs_syn_Noise_PC_noSTDP,name = 'PC_Noise_Synapse_Coupled_noSTDP',dt=t_Neuron)
S_Coupled_noSTDP.connect()
S_Coupled_noSTDP.noise_weight = 'abs(1-abs(i-j)/N_Cells_PC)'
S_statemon = StateMonitor(S_Coupled_noSTDP, variables=['noise_weight','I_Noise'], record=True,dt=t_Monitor)

Synapse_IO_PC_Coupled_noSTDP = Synapses(IO_Coupled_noSTDP, PC_Coupled_noSTDP, on_pre ='w +=(0.005*nA)', delay=2*ms, name = 'IO_PC_Synapse_Coupled_noSTDP',method = 'euler',dt=t_Neuron)
# Synapse_IO_PC_Coupled_noSTDP.connect('i==j')
IO_index = random.sample(range(N_Cells_IO), 10)
#Synapse_IO_PC_Coupled_noSTDP.connect(i=IO_index, j=range(N_Cells_PC))
Synapse_IO_PC_Coupled_noSTDP.connect(i=i_IOPC, j=j_IOPC)

DCN_PC_Synapse_Coupled_noSTDP = Synapses(PC_Coupled_noSTDP, DCN_Coupled_noSTDP, on_pre='I_PC_post = 1.5*nA', delay=2*ms, name = 'PC_DCN_Synapse_Coupled_noSTDP',dt=t_Neuron) 
# DCN_PC_Synapse_Coupled_noSTDP.connect(j='k for k in range(i,i+N_Cells_PC+1)')
DCN_PC_Synapse_Coupled_a = list(range(N_Cells_DCN))
DCN_PC_Synapse_Coupled_m=[]
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
    for ee in range(10):
        DCN_PC_Synapse_Coupled_targ.append(kk)

#DCN_PC_Synapse_Coupled_noSTDP.connect(i=DCN_PC_Synapse_Coupled_targ,j=DCN_PC_Synapse_Coupled_mm)
DCN_PC_Synapse_Coupled_noSTDP.connect(i=i_PCDCN,j=j_PCDCN)


IO_DCN_Synapse_Coupled_noSTDP = Synapses(DCN_Coupled_noSTDP, IO_Coupled_noSTDP, on_pre = 'I_IO_DCN_post += -0.05*uA*cm**-2', delay=3*ms, name = 'IO_DCN_Synapse_Coupled_noSTDP', method = 'euler',dt=t_Neuron)
# orgininal effect : (1/(N_Cells_IO*(N_Cells_DCN/2)))

# IO_DCN_Synapse_Coupled_noSTDP.connect(j='k for k in range(i,i+int(N_Cells_IO/2))', skip_if_invalid=True)
# IO_DCN_Synapse_Coupled_noSTDP.connect(j='k for k in range(i-int(N_Cells_IO/2)) if i>int(N_Cells_IO/2)')
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
#IO_DCN_Synapse_Coupled_noSTDP.connect(i=IO_DCN_Synapse_Coupled_targ,j=IO_DCN_Synapse_Coupled_mm)
IO_DCN_Synapse_Coupled_noSTDP.connect(i=i_DCNIO,j=j_DCNIO)


IO_synapse_Coupled_noSTDP = Synapses(IO_Coupled_noSTDP, IO_Coupled_noSTDP, eqs_IO_syn_Coupled, name = 'IO_Synapse_Coupled_noSTDP')
IO_synapse_Coupled_noSTDP.connect()
###########################################################################################################################
###########################################################################################################################
################################################### UNCOUPLED SCENARIO ####################################################
###########################################################################################################################
###########################################################################################################################
#####################################################################
############################ Synapses ###############################
#####################################################################
S_Uncoupled_noSTDP = Synapses(Noise, PC_Uncoupled_noSTDP, eqs_syn_Noise_PC_noSTDP,name = 'PC_Noise_Synapse_Uncoupled_noSTDP',dt=t_Neuron)
S_Uncoupled_noSTDP.connect()
S_Uncoupled_noSTDP.noise_weight = 'abs(1-abs(i-j)/N_Cells_PC)'
S_statemon = StateMonitor(S_Uncoupled_noSTDP, variables=['noise_weight','I_Noise'], record=True,dt=t_Monitor)

Synapse_IO_PC_Uncoupled_noSTDP = Synapses(IO_Uncoupled_noSTDP, PC_Uncoupled_noSTDP, on_pre ='w +=(0.005*nA)', delay=2*ms, name = 'IO_PC_Synapse_Uncoupled_noSTDP',method = 'euler',dt=t_Neuron)
# Synapse_IO_PC_Uncoupled_noSTDP.connect('i==j')
#Synapse_IO_PC_Uncoupled_noSTDP.connect(i=IO_index, j=range(N_Cells_PC))
Synapse_IO_PC_Uncoupled_noSTDP.connect(i=i_IOPC, j=j_IOPC)

DCN_PC_Synapse_Uncoupled_noSTDP = Synapses(PC_Uncoupled_noSTDP, DCN_Uncoupled_noSTDP, on_pre='I_PC_post = 1.5*nA', delay=2*ms, name = 'PC_DCN_Synapse_Uncoupled_noSTDP',dt=t_Neuron) 
# DCN_PC_Synapse_Uncoupled_noSTDP.connect(j='k for k in range(i,i+N_Cells_PC+1)')
DCN_PC_Synapse_Uncoupled_noSTDP.connect(i=DCN_PC_Synapse_Coupled_targ,j=DCN_PC_Synapse_Coupled_mm)

IO_DCN_Synapse_Uncoupled_noSTDP = Synapses(DCN_Uncoupled_noSTDP, IO_Uncoupled_noSTDP, on_pre = 'I_IO_DCN_post += -0.05*uA*cm**-2', delay=3*ms, name = 'IO_DCN_Synapse_Uncoupled_noSTDP', method = 'euler',dt=t_Neuron)
# IO_DCN_Synapse_Uncoupled_noSTDP.connect(j='k for k in range(i,i+int(N_Cells_IO/2))', skip_if_invalid=True)
# IO_DCN_Synapse_Uncoupled_noSTDP.connect(j='k for k in range(i-int(N_Cells_IO/2)) if i>int(N_Cells_IO/2)')

#IO_DCN_Synapse_Uncoupled_noSTDP.connect(i=IO_DCN_Synapse_Coupled_targ,j=IO_DCN_Synapse_Coupled_mm)
IO_DCN_Synapse_Uncoupled_noSTDP.connect(i=i_DCNIO,j=j_DCNIO)


eqs_IO_syn_Uncoupled_noSTDP = ''' I_c_pre = (0*mS/cm**2)*(0.6*e**(-((Vd_pre/mvolt-Vd_post/mvolt)/50)**2) + 0.4)*(Vd_pre-Vd_post) : metre**-2*amp (summed)'''
IO_synapse_Uncoupled_noSTDP = Synapses(IO_Uncoupled_noSTDP, IO_Uncoupled_noSTDP, eqs_IO_syn_Uncoupled_noSTDP, name = 'IO_Synapse_Uncoupled_noSTDP')
IO_synapse_Uncoupled_noSTDP.connect()