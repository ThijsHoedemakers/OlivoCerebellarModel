from C_Equations import *
###########################################################################################################################
###########################################################################################################################
##################################################### COUPLED SCENARIO ####################################################
###########################################################################################################################
###########################################################################################################################
#####################################################################
########################### PURKINJE CELLS ##########################
#####################################################################
PC_Coupled_STDP = NeuronGroup(N_Cells_PC, model=PC_Equations, threshold='v>Vcut', reset="v=Vr; w+=b", method='euler', name = 'PC_Coupled_STDP',dt=t_Neuron)
for jj in range(0,N_Cells_PC,1):
    PC_Coupled_STDP.C[jj] = PC_C[jj]
    PC_Coupled_STDP.gL[jj] = PC_gL[jj]
    PC_Coupled_STDP.EL[jj] = PC_EL[jj]
    PC_Coupled_STDP.VT[jj] = PC_VT[jj]
    PC_Coupled_STDP.DeltaT[jj] = PC_DeltaT[jj]
    PC_Coupled_STDP.Vcut[jj] = PC_Coupled_STDP.VT[jj] + 5*PC_Coupled_STDP.DeltaT[jj]
    PC_Coupled_STDP.tauw[jj] = PC_tauw[jj]
    PC_Coupled_STDP.a[jj] = PC_a[jj]
    PC_Coupled_STDP.b[jj] = PC_b[jj]
    PC_Coupled_STDP.Vr[jj] = PC_Vr[jj]
    PC_Coupled_STDP.v[jj] = PC_v[jj]
    PC_Coupled_STDP.I_intrinsic[jj] = PC_I_intrinsic[jj]
    #PC_I_intrinsic[jj]
#print('intrinsic current coupled =',PC_Coupled_STDP.I_intrinsic)
PC_Statemon_Coupled_STDP = StateMonitor(PC_Coupled_STDP, ['v', 'w', 'I_Noise','I_intrinsic','tauw'], record=True,dt=t_Monitor)
PC_Spikemon_Coupled_STDP = SpikeMonitor(PC_Coupled_STDP)
PC_rate_Coupled_STDP = PopulationRateMonitor(PC_Coupled_STDP)
#####################################################################
###################### INFERIOR OLIVARY CELLS #######################
#####################################################################
IO_Coupled_STDP = NeuronGroup(N_Cells_IO, model = eqs_IO, threshold='Vs>20*mV' , method = 'euler',name = 'SchweighoferOlive_Coupled_STDP',dt=t_Neuron)
for ii in range(0, N_Cells_IO, 1):
    IO_Coupled_STDP.V_Na[ii] = IO_V_Na[ii]
    IO_Coupled_STDP.V_K[ii] = IO_V_K[ii]
    IO_Coupled_STDP.V_Ca[ii] = IO_V_Ca[ii]
    IO_Coupled_STDP.V_l[ii] = IO_V_l[ii]
    IO_Coupled_STDP.V_h[ii] = IO_V_h[ii]
    IO_Coupled_STDP.Cm[ii] = IO_Cm[ii]
    IO_Coupled_STDP.g_Na[ii] = IO_g_Na[ii]
    IO_Coupled_STDP.g_Kdr[ii] = IO_g_Kdr[ii]
    IO_Coupled_STDP.g_K_s[ii] = IO_g_K_s[ii]
    IO_Coupled_STDP.g_h[ii] = IO_g_h[ii]
    IO_Coupled_STDP.g_Ca_h[ii] = IO_g_Ca_h[ii]
    IO_Coupled_STDP.g_K_Ca[ii] = IO_g_K_Ca[ii]
    IO_Coupled_STDP.g_Na_a[ii] = IO_g_Na_a[ii]
    IO_Coupled_STDP.g_K_a[ii] = IO_g_K_a[ii]
    IO_Coupled_STDP.g_ls[ii] = IO_g_ls[ii]
    IO_Coupled_STDP.g_ld[ii] = IO_g_ld[ii]
    IO_Coupled_STDP.g_la[ii] = IO_g_la[ii]
    IO_Coupled_STDP.g_int[ii] = IO_g_int[ii]
    IO_Coupled_STDP.p[ii] = IO_p[ii]
    IO_Coupled_STDP.p2[ii] = IO_p2[ii]
    IO_Coupled_STDP.g_Ca_l[ii] =  IO_g_Ca_l[ii]

IO_Statemon_Coupled_STDP = StateMonitor(IO_Coupled_STDP, variables = ['Vs','Vd','I_IO_DCN', 'I_c'], record = True, dt=t_Monitor)
IO_Spikemon_Coupled_STDP = SpikeMonitor(IO_Coupled_STDP)
IO_rate_Coupled_STDP = PopulationRateMonitor(IO_Coupled_STDP)
#####################################################################
################### DEEP CEREBELLAR NUCLEI CELLS ####################
#####################################################################
DCN_Coupled_STDP = NeuronGroup(N_Cells_DCN, model=DCN_Equations, threshold='v>Vcut', reset="v=Vr; w+=b", method='euler', name = 'DCN_Coupled_STDP',dt=t_Neuron)
for dd in range(0,N_Cells_DCN,1):    
    DCN_Coupled_STDP.C[dd] = DCN_C[dd]
    DCN_Coupled_STDP.gL[dd] = DCN_gL[dd]
    DCN_Coupled_STDP.EL[dd] = DCN_EL[dd]
    DCN_Coupled_STDP.VT[dd] = DCN_VT[dd]
    DCN_Coupled_STDP.DeltaT[dd] = DCN_DeltaT[dd]
    DCN_Coupled_STDP.Vcut[dd] = DCN_Coupled_STDP.VT[dd] + 5*DCN_Coupled_STDP.DeltaT[dd]
    DCN_Coupled_STDP.tauw[dd] = DCN_tauw[dd]
    DCN_Coupled_STDP.a[dd] = DCN_a[dd]
    DCN_Coupled_STDP.b[dd] = DCN_b[dd]
    DCN_Coupled_STDP.Vr[dd] = DCN_Vr[dd]
    DCN_Coupled_STDP.tauI[dd] = DCN_tauI[dd]
    DCN_Coupled_STDP.I_PC_max[dd] = DCN_I_PC_max[dd]
    DCN_Coupled_STDP.v = DCN_v[dd]
    DCN_Coupled_STDP.I_intrinsic[dd] = DCN_I_intrinsic[dd]
######### Monitors ###############
DCN_Statemon_Coupled_STDP = StateMonitor(DCN_Coupled_STDP, ['v', 'I_PC','w'], record=True,dt=t_Monitor)
DCN_Spikemon_Coupled_STDP = SpikeMonitor(DCN_Coupled_STDP)
DCN_rate_Coupled_STDP = PopulationRateMonitor(DCN_Coupled_STDP)
###########################################################################################################################
###########################################################################################################################
################################################### UNCOUPLED SCENARIO ####################################################
###########################################################################################################################
###########################################################################################################################
#####################################################################
########################### PURKINJE CELLS ##########################
#####################################################################
PC_Uncoupled_STDP = NeuronGroup(N_Cells_PC, model=PC_Equations, threshold='v>Vcut', reset="v=Vr; w+=b", method='euler', name = 'PC_Uncoupled_STDP',dt=t_Neuron)
for jj in range(0,N_Cells_PC,1):
    PC_Uncoupled_STDP.C[jj] = PC_C[jj]
    PC_Uncoupled_STDP.gL[jj] = PC_gL[jj]
    PC_Uncoupled_STDP.EL[jj] = PC_EL[jj]
    PC_Uncoupled_STDP.VT[jj] = PC_VT[jj]
    PC_Uncoupled_STDP.DeltaT[jj] = PC_DeltaT[jj]
    PC_Uncoupled_STDP.Vcut[jj] = PC_Uncoupled_STDP.VT[jj]+ 5*PC_Uncoupled_STDP.DeltaT[jj]
    PC_Uncoupled_STDP.tauw[jj] = PC_tauw[jj]
    PC_Uncoupled_STDP.a[jj] = PC_a[jj]
    PC_Uncoupled_STDP.b[jj] = PC_b[jj]
    PC_Uncoupled_STDP.Vr[jj] = PC_Vr[jj]
    PC_Uncoupled_STDP.v[jj] = PC_v[jj]
    PC_Uncoupled_STDP.I_intrinsic[jj] = PC_I_intrinsic[jj]
    #PC_I_intrinsic[jj]
#print('intrinsic current uncoupled =',PC_Uncoupled_STDP.I_intrinsic)
PC_Statemon_Uncoupled_STDP = StateMonitor(PC_Uncoupled_STDP, ['v', 'w', 'I_Noise','I_intrinsic','tauw'], record=True,dt=t_Monitor)
PC_Spikemon_Uncoupled_STDP = SpikeMonitor(PC_Uncoupled_STDP)
PC_rate_Uncoupled_STDP = PopulationRateMonitor(PC_Uncoupled_STDP)
#####################################################################
###################### INFERIOR OLIVARY CELLS #######################
#####################################################################
IO_Uncoupled_STDP = NeuronGroup(N_Cells_IO, model = eqs_IO, threshold='Vs>20*mV' , method = 'euler',name = 'SchweighoferOlive_Uncoupled_STDP',dt=t_Neuron)
for ii in range(0, N_Cells_IO, 1):
    IO_Uncoupled_STDP.V_Na[ii] = IO_V_Na[ii]
    IO_Uncoupled_STDP.V_K[ii] = IO_V_K[ii]
    IO_Uncoupled_STDP.V_Ca[ii] = IO_V_Ca[ii]
    IO_Uncoupled_STDP.V_l[ii] = IO_V_l[ii]
    IO_Uncoupled_STDP.V_h[ii] = IO_V_h[ii]
    IO_Uncoupled_STDP.Cm[ii] = IO_Cm[ii]
    IO_Uncoupled_STDP.g_Na[ii] = IO_g_Na[ii]
    IO_Uncoupled_STDP.g_Kdr[ii] = IO_g_Kdr[ii]
    IO_Uncoupled_STDP.g_K_s[ii] = IO_g_K_s[ii]
    IO_Uncoupled_STDP.g_h[ii] = IO_g_h[ii]
    IO_Uncoupled_STDP.g_Ca_h[ii] = IO_g_Ca_h[ii]
    IO_Uncoupled_STDP.g_K_Ca[ii] = IO_g_K_Ca[ii]
    IO_Uncoupled_STDP.g_Na_a[ii] = IO_g_Na_a[ii]
    IO_Uncoupled_STDP.g_K_a[ii] = IO_g_K_a[ii]
    IO_Uncoupled_STDP.g_ls[ii] = IO_g_ls[ii]
    IO_Uncoupled_STDP.g_ld[ii] = IO_g_ld[ii]
    IO_Uncoupled_STDP.g_la[ii] = IO_g_la[ii]
    IO_Uncoupled_STDP.g_int[ii] = IO_g_int[ii]
    IO_Uncoupled_STDP.p[ii] = IO_p[ii]
    IO_Uncoupled_STDP.p2[ii] = IO_p2[ii]
    IO_Uncoupled_STDP.g_Ca_l[ii] =  IO_g_Ca_l[ii]
    
IO_Statemon_Uncoupled_STDP = StateMonitor(IO_Uncoupled_STDP, variables = ['Vs','Vd', 'I_IO_DCN','I_c'], record = True, dt=t_Monitor)
IO_Spikemon_Uncoupled_STDP = SpikeMonitor(IO_Uncoupled_STDP)
IO_rate_Uncoupled_STDP = PopulationRateMonitor(IO_Uncoupled_STDP)
#####################################################################
################### DEEP CEREBELLAR NUCLEI CELLS ####################
#####################################################################
DCN_Uncoupled_STDP = NeuronGroup(N_Cells_DCN, model=DCN_Equations, threshold='v>Vcut', reset="v=Vr; w+=b", method='euler', name = 'DCN_Uncoupled_STDP',dt=t_Neuron)
for dd in range(0,N_Cells_DCN,1):    
    DCN_Uncoupled_STDP.C[dd] = DCN_C[dd]
    DCN_Uncoupled_STDP.gL[dd] = DCN_gL[dd]
    DCN_Uncoupled_STDP.EL[dd] = DCN_EL[dd]
    DCN_Uncoupled_STDP.VT[dd] = DCN_VT[dd]
    DCN_Uncoupled_STDP.DeltaT[dd] = DCN_DeltaT[dd]
    DCN_Uncoupled_STDP.Vcut[dd] = DCN_Uncoupled_STDP.VT[dd] + 5*DCN_Uncoupled_STDP.DeltaT[dd]
    DCN_Uncoupled_STDP.tauw[dd] = DCN_tauw[dd]
    DCN_Uncoupled_STDP.a[dd] = DCN_a[dd]
    DCN_Uncoupled_STDP.b[dd] = DCN_b[dd]
    DCN_Uncoupled_STDP.Vr[dd] = DCN_Vr[dd]
    DCN_Uncoupled_STDP.tauI[dd] = DCN_tauI[dd]
    DCN_Uncoupled_STDP.I_PC_max[dd] = DCN_I_PC_max[dd]
    DCN_Uncoupled_STDP.v[dd] = DCN_v[dd]
    DCN_Uncoupled_STDP.I_intrinsic[dd] = DCN_I_intrinsic[dd]
######### Monitors ###############
DCN_Statemon_Uncoupled_STDP = StateMonitor(DCN_Uncoupled_STDP, ['v', 'I_PC','w'], record=True,dt=t_Monitor)
DCN_Spikemon_Uncoupled_STDP = SpikeMonitor(DCN_Uncoupled_STDP)
DCN_rate_Uncoupled_STDP = PopulationRateMonitor(DCN_Uncoupled_STDP)

