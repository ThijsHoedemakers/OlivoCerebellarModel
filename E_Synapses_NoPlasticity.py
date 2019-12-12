from D_NeuronGroups_NoPlasticity import *
###########################################################################################################################
###########################################################################################################################
##################################################### COUPLED SCENARIO ####################################################
###########################################################################################################################
###########################################################################################################################
#####################################################################
############################ Synapses ###############################
#####################################################################
S_Coupled_noSTDP = Synapses(Noise, PC_Coupled_noSTDP, eqs_syn_Noise_PC_noSTDP,name = 'PC_Noise_Synapse_Coupled_noSTDP',dt=dt)
S_Coupled_noSTDP.connect()
S_Coupled_noSTDP.noise_weight = 'abs(1-abs(i-j)/N_Cells_PC)'
S_statemon = StateMonitor(S_Coupled_noSTDP, variables=['noise_weight','I_Noise'], record=True,dt=dt)

Synapse_IO_PC_Coupled_noSTDP = Synapses(IO_Coupled_noSTDP, PC_Coupled_noSTDP, on_pre ='w +=(0.005*nA)', delay=2*ms, name = 'IO_PC_Synapse_Coupled_noSTDP',method = 'euler',dt=dt)
# Synapse_IO_PC_Coupled_noSTDP.connect('i==j')
IO_index = random.sample(range(N_Cells_IO), 10)
Synapse_IO_PC_Coupled_noSTDP.connect(i=IO_index, j=range(N_Cells_PC))

DCN_PC_Synapse_Coupled_noSTDP = Synapses(PC_Coupled_noSTDP, DCN_Coupled_noSTDP, on_pre='I_PC_post = 1.5*nA', delay=2*ms, name = 'PC_DCN_Synapse_Coupled_noSTDP',dt=dt) 
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

DCN_PC_Synapse_Coupled_noSTDP.connect(i=DCN_PC_Synapse_Coupled_targ,j=DCN_PC_Synapse_Coupled_mm)


IO_DCN_Synapse_Coupled_noSTDP = Synapses(DCN_Coupled_noSTDP, IO_Coupled_noSTDP, on_pre = 'I_IO_DCN_post += -(1/(N_Cells_IO*(N_Cells_DCN/2)))*uA*cm**-2', delay=3*ms, name = 'IO_DCN_Synapse_Coupled_noSTDP', method = 'euler',dt=dt)
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
IO_DCN_Synapse_Coupled_noSTDP.connect(i=IO_DCN_Synapse_Coupled_targ,j=IO_DCN_Synapse_Coupled_mm)


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
S_Uncoupled_noSTDP = Synapses(Noise, PC_Uncoupled_noSTDP, eqs_syn_Noise_PC_noSTDP,name = 'PC_Noise_Synapse_Uncoupled_noSTDP',dt=dt)
S_Uncoupled_noSTDP.connect()
S_Uncoupled_noSTDP.noise_weight = 'abs(1-abs(i-j)/N_Cells_PC)'
S_statemon = StateMonitor(S_Uncoupled_noSTDP, variables=['noise_weight','I_Noise'], record=True,dt=dt)

Synapse_IO_PC_Uncoupled_noSTDP = Synapses(IO_Uncoupled_noSTDP, PC_Uncoupled_noSTDP, on_pre ='w +=(0.005*nA)', delay=2*ms, name = 'IO_PC_Synapse_Uncoupled_noSTDP',method = 'euler',dt=dt)
# Synapse_IO_PC_Uncoupled_noSTDP.connect('i==j')
Synapse_IO_PC_Uncoupled_noSTDP.connect(i=IO_index, j=range(N_Cells_PC))

DCN_PC_Synapse_Uncoupled_noSTDP = Synapses(PC_Uncoupled_noSTDP, DCN_Uncoupled_noSTDP, on_pre='I_PC_post = 1.5*nA', delay=2*ms, name = 'PC_DCN_Synapse_Uncoupled_noSTDP',dt=dt) 
# DCN_PC_Synapse_Uncoupled_noSTDP.connect(j='k for k in range(i,i+N_Cells_PC+1)')
DCN_PC_Synapse_Uncoupled_noSTDP.connect(i=DCN_PC_Synapse_Coupled_targ,j=DCN_PC_Synapse_Coupled_mm)

IO_DCN_Synapse_Uncoupled_noSTDP = Synapses(DCN_Uncoupled_noSTDP, IO_Uncoupled_noSTDP, on_pre = 'I_IO_DCN_post += -(1/(N_Cells_IO*(N_Cells_DCN/2)))*uA*cm**-2', delay=3*ms, name = 'IO_DCN_Synapse_Uncoupled_noSTDP', method = 'euler',dt=dt)
# IO_DCN_Synapse_Uncoupled_noSTDP.connect(j='k for k in range(i,i+int(N_Cells_IO/2))', skip_if_invalid=True)
# IO_DCN_Synapse_Uncoupled_noSTDP.connect(j='k for k in range(i-int(N_Cells_IO/2)) if i>int(N_Cells_IO/2)')
IO_DCN_Synapse_Uncoupled_noSTDP.connect(i=IO_DCN_Synapse_Coupled_targ,j=IO_DCN_Synapse_Coupled_mm)


eqs_IO_syn_Uncoupled_noSTDP = ''' I_c_pre = (0*mS/cm**2)*(0.6*e**(-((Vd_pre/mvolt-Vd_post/mvolt)/50)**2) + 0.4)*(Vd_pre-Vd_post) : metre**-2*amp (summed)'''
IO_synapse_Uncoupled_noSTDP = Synapses(IO_Uncoupled_noSTDP, IO_Uncoupled_noSTDP, eqs_IO_syn_Uncoupled_noSTDP, name = 'IO_Synapse_Uncoupled_noSTDP')
IO_synapse_Uncoupled_noSTDP.connect()