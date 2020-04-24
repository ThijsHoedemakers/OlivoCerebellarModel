from C_Equations import *
###########################################################################################################################
###########################################################################################################################
##################################################### COUPLED SCENARIO ####################################################
###########################################################################################################################
###########################################################################################################################
#####################################################################
########################### PURKINJE CELLS ##########################
#####################################################################
PC_Coupled_noSTDP = NeuronGroup(N_Cells_PC, model=PC_Equations, threshold='v>Vcut', reset="v=Vr; w+=b", method='euler', name = 'PC_Coupled_noSTDP',dt=t_Neuron)
for jj in range(0,N_Cells_PC,1):
    PC_Coupled_noSTDP.C[jj] = PC_C[jj]
    PC_Coupled_noSTDP.gL[jj] = PC_gL[jj]
    PC_Coupled_noSTDP.EL[jj] = PC_EL[jj]
    PC_Coupled_noSTDP.VT[jj] = PC_VT[jj]
    PC_Coupled_noSTDP.DeltaT[jj] = PC_DeltaT[jj]
    PC_Coupled_noSTDP.Vcut[jj] = PC_Coupled_noSTDP.VT[jj] + 5*PC_Coupled_noSTDP.DeltaT[jj]
    PC_Coupled_noSTDP.tauw[jj] = PC_tauw[jj]
    PC_Coupled_noSTDP.a[jj] = PC_a[jj]
    PC_Coupled_noSTDP.b[jj] = PC_b[jj]
    PC_Coupled_noSTDP.Vr[jj] = PC_Vr[jj]
    # why is this one in the noSTDP but not in STDP?
    #PC_Coupled_noSTDP.I_Noise[jj] = 0.9*nA
    PC_Coupled_noSTDP.v[jj] = PC_v[jj]
    PC_Coupled_noSTDP.I_intrinsic[jj] = PC_I_intrinsic[jj]
PC_Statemon_Coupled_noSTDP = StateMonitor(PC_Coupled_noSTDP, ['v', 'w', 'I_Noise','I_intrinsic','tauw'], record=True,dt=t_Monitor)
PC_Spikemon_Coupled_noSTDP = SpikeMonitor(PC_Coupled_noSTDP)
PC_rate_Coupled_noSTDP = PopulationRateMonitor(PC_Coupled_noSTDP)
#####################################################################
###################### INFERIOR OLIVARY CELLS #######################
#####################################################################
IO_Coupled_noSTDP = NeuronGroup(N_Cells_IO, model = eqs_IO, threshold='Vs>20*mV' , method = 'euler',name = 'SchweighoferOlive_Coupled_noSTDP',dt=t_Neuron)
for ii in range(0, N_Cells_IO, 1):
    IO_Coupled_noSTDP.V_Na[ii] = IO_V_Na[ii]
    IO_Coupled_noSTDP.V_K[ii] = IO_V_K[ii]
    IO_Coupled_noSTDP.V_Ca[ii] = IO_V_Ca[ii]
    IO_Coupled_noSTDP.V_l[ii] = IO_V_l[ii]
    IO_Coupled_noSTDP.V_h[ii] = IO_V_h[ii]
    IO_Coupled_noSTDP.Cm[ii] = IO_Cm [ii]
    IO_Coupled_noSTDP.g_Na[ii] = IO_g_Na[ii]
    IO_Coupled_noSTDP.g_Kdr[ii] = IO_g_Kdr[ii]
    IO_Coupled_noSTDP.g_K_s[ii] = IO_g_K_s[ii]
    IO_Coupled_noSTDP.g_h[ii] = IO_g_h[ii]
    IO_Coupled_noSTDP.g_Ca_h[ii] = IO_g_Ca_h[ii]
    IO_Coupled_noSTDP.g_K_Ca[ii] = IO_g_K_Ca[ii]
    IO_Coupled_noSTDP.g_Na_a[ii] = IO_g_Na_a[ii]
    IO_Coupled_noSTDP.g_K_a[ii] = IO_g_K_a[ii]
    IO_Coupled_noSTDP.g_ls[ii] = IO_g_ls[ii]
    IO_Coupled_noSTDP.g_ld[ii] = IO_g_ld[ii]
    IO_Coupled_noSTDP.g_la[ii] = IO_g_la[ii]
    IO_Coupled_noSTDP.g_int[ii] = IO_g_int[ii]
    IO_Coupled_noSTDP.p[ii] = IO_p[ii]
    IO_Coupled_noSTDP.p2[ii] = IO_p2[ii]
    IO_Coupled_noSTDP.g_Ca_l[ii] =  IO_g_Ca_l[ii]
IO_Statemon_Coupled_noSTDP = StateMonitor(IO_Coupled_noSTDP, variables = ['Vs','Vd', 'I_IO_DCN','I_c'], record = True, dt=t_Monitor)
IO_Spikemon_Coupled_noSTDP = SpikeMonitor(IO_Coupled_noSTDP)
IO_rate_Coupled_noSTDP = PopulationRateMonitor(IO_Coupled_noSTDP)
#####################################################################
################### DEEP CEREBELLAR NUCLEI CELLS ####################
#####################################################################
DCN_Coupled_noSTDP = NeuronGroup(N_Cells_DCN, model=DCN_Equations, threshold='v>Vcut', reset="v=Vr; w+=b", method='euler', name = 'DCN_Coupled_noSTDP',dt=t_Neuron)
for dd in range(0,N_Cells_DCN,1):    
    DCN_Coupled_noSTDP.C[dd] = DCN_C[dd]
    DCN_Coupled_noSTDP.gL[dd] = DCN_gL[dd]
    DCN_Coupled_noSTDP.EL[dd] = DCN_EL[dd]
    DCN_Coupled_noSTDP.VT[dd] = DCN_VT[dd]
    DCN_Coupled_noSTDP.DeltaT[dd] = DCN_DeltaT[dd]
    DCN_Coupled_noSTDP.Vcut[dd] = DCN_Coupled_noSTDP.VT[dd] + 5*DCN_Coupled_noSTDP.DeltaT[dd]
    DCN_Coupled_noSTDP.tauw[dd] = DCN_tauw[dd]
    DCN_Coupled_noSTDP.a[dd] = DCN_a[dd]
    DCN_Coupled_noSTDP.b[dd] = DCN_b[dd]
    DCN_Coupled_noSTDP.Vr[dd] = DCN_Vr[dd]
    DCN_Coupled_noSTDP.tauI[dd] = DCN_tauI[dd]
    DCN_Coupled_noSTDP.I_PC_max[dd] = DCN_I_PC_max[dd]
    DCN_Coupled_noSTDP.v[dd] = DCN_v[dd]
    DCN_Coupled_noSTDP.I_intrinsic[dd] = DCN_I_intrinsic[dd]
######### Monitors ###############
DCN_Statemon_Coupled_noSTDP = StateMonitor(DCN_Coupled_noSTDP, ['v', 'I_PC','w'], record=True,dt=t_Monitor)
DCN_Spikemon_Coupled_noSTDP = SpikeMonitor(DCN_Coupled_noSTDP)
DCN_rate_Coupled_noSTDP = PopulationRateMonitor(DCN_Coupled_noSTDP)
###########################################################################################################################
###########################################################################################################################
################################################### UNCOUPLED SCENARIO ####################################################
###########################################################################################################################
###########################################################################################################################
#####################################################################
########################### PURKINJE CELLS ##########################
#####################################################################
PC_Uncoupled_noSTDP = NeuronGroup(N_Cells_PC, model=PC_Equations, threshold='v>Vcut', reset="v=Vr; w+=b", method='euler', name = 'PC_Uncoupled_noSTDP',dt=t_Neuron)
for jj in range(0,N_Cells_PC,1):
    PC_Uncoupled_noSTDP.C[jj] = PC_C[jj]
    PC_Uncoupled_noSTDP.gL[jj] = PC_gL[jj]
    PC_Uncoupled_noSTDP.EL[jj] = PC_EL[jj]
    PC_Uncoupled_noSTDP.VT[jj] = PC_VT[jj]
    PC_Uncoupled_noSTDP.DeltaT[jj] = PC_DeltaT[jj]
    PC_Uncoupled_noSTDP.Vcut[jj] = PC_Uncoupled_noSTDP.VT[jj] + 5*PC_Uncoupled_noSTDP.DeltaT[jj]
    PC_Uncoupled_noSTDP.tauw[jj] = PC_tauw[jj]
    PC_Uncoupled_noSTDP.a[jj] = PC_a[jj]
    PC_Uncoupled_noSTDP.b[jj] = PC_b[jj]
    PC_Uncoupled_noSTDP.Vr[jj] = PC_Vr[jj]
    #PC_Uncoupled_noSTDP.I_Noise[jj] = 0.9*nA
    PC_Uncoupled_noSTDP.v[jj] = PC_v[jj]
PC_Uncoupled_noSTDP.I_intrinsic = PC_I_intrinsic
PC_Statemon_Uncoupled_noSTDP = StateMonitor(PC_Uncoupled_noSTDP, ['v', 'w', 'I_Noise','I_intrinsic','tauw'], record=True,dt=t_Monitor)
PC_Spikemon_Uncoupled_noSTDP = SpikeMonitor(PC_Uncoupled_noSTDP)
PC_rate_Uncoupled_noSTDP = PopulationRateMonitor(PC_Uncoupled_noSTDP)
#####################################################################
###################### INFERIOR OLIVARY CELLS #######################
#####################################################################
IO_Uncoupled_noSTDP = NeuronGroup(N_Cells_IO, model = eqs_IO, threshold='Vs>20*mV' , method = 'euler',name = 'SchweighoferOlive_Uncoupled_noSTDP',dt=t_Neuron)
for ii in range(0, N_Cells_IO, 1):
    IO_Uncoupled_noSTDP.V_Na[ii] = IO_V_Na[ii]
    IO_Uncoupled_noSTDP.V_K[ii] = IO_V_K[ii]
    IO_Uncoupled_noSTDP.V_Ca[ii] = IO_V_Ca[ii]
    IO_Uncoupled_noSTDP.V_l[ii] = IO_V_l[ii]
    IO_Uncoupled_noSTDP.V_h[ii] = IO_V_h[ii]
    IO_Uncoupled_noSTDP.Cm[ii] = IO_Cm[ii]
    IO_Uncoupled_noSTDP.g_Na[ii] = IO_g_Na[ii]
    IO_Uncoupled_noSTDP.g_Kdr[ii] = IO_g_Kdr[ii]
    IO_Uncoupled_noSTDP.g_K_s[ii] = IO_g_K_s[ii]
    IO_Uncoupled_noSTDP.g_h[ii] = IO_g_h[ii]
    IO_Uncoupled_noSTDP.g_Ca_h[ii] = IO_g_Ca_h[ii]
    IO_Uncoupled_noSTDP.g_K_Ca[ii] = IO_g_K_Ca[ii]
    IO_Uncoupled_noSTDP.g_Na_a[ii] = IO_g_Na_a[ii]
    IO_Uncoupled_noSTDP.g_K_a[ii] = IO_g_K_a[ii]
    IO_Uncoupled_noSTDP.g_ls[ii] = IO_g_ls[ii]
    IO_Uncoupled_noSTDP.g_ld[ii] = IO_g_ld[ii]
    IO_Uncoupled_noSTDP.g_la[ii] = IO_g_la[ii]
    IO_Uncoupled_noSTDP.g_int[ii] = IO_g_int[ii]
    IO_Uncoupled_noSTDP.p[ii] = IO_p[ii]
    IO_Uncoupled_noSTDP.p2[ii] = IO_p2[ii]
    IO_Uncoupled_noSTDP.g_Ca_l[ii] =  IO_g_Ca_l[ii]
IO_Statemon_Uncoupled_noSTDP = StateMonitor(IO_Uncoupled_noSTDP, variables = ['Vs','Vd', 'I_IO_DCN','I_c'], record = True, dt=t_Monitor)
IO_Spikemon_Uncoupled_noSTDP = SpikeMonitor(IO_Uncoupled_noSTDP)
IO_rate_Uncoupled_noSTDP = PopulationRateMonitor(IO_Uncoupled_noSTDP)
#####################################################################
################### DEEP CEREBELLAR NUCLEI CELLS ####################
#####################################################################
DCN_Uncoupled_noSTDP = NeuronGroup(N_Cells_DCN, model=DCN_Equations, threshold='v>Vcut', reset="v=Vr; w+=b", method='euler', name = 'DCN_Uncoupled_noSTDP',dt=t_Neuron)
for dd in range(0,N_Cells_DCN,1):    
    DCN_Uncoupled_noSTDP.C[dd] = DCN_C[dd]
    DCN_Uncoupled_noSTDP.gL[dd] = DCN_gL[dd]
    DCN_Uncoupled_noSTDP.EL[dd] = DCN_EL[dd]
    DCN_Uncoupled_noSTDP.VT[dd] = DCN_VT[dd]
    DCN_Uncoupled_noSTDP.DeltaT[dd] = DCN_DeltaT[dd]
    DCN_Uncoupled_noSTDP.Vcut[dd] = DCN_Uncoupled_noSTDP.VT[dd] + 5*DCN_Uncoupled_noSTDP.DeltaT[dd]
    DCN_Uncoupled_noSTDP.tauw[dd] = DCN_tauw[dd]
    DCN_Uncoupled_noSTDP.a[dd] = DCN_a[dd]
    DCN_Uncoupled_noSTDP.b[dd] = DCN_b[dd]
    DCN_Uncoupled_noSTDP.Vr[dd] = DCN_Vr[dd]
    DCN_Uncoupled_noSTDP.tauI[dd] = DCN_tauI[dd]
    DCN_Uncoupled_noSTDP.I_PC_max[dd] = DCN_I_PC_max[dd]
    DCN_Uncoupled_noSTDP.v[dd] = DCN_v[dd]
    DCN_Uncoupled_noSTDP.I_intrinsic[dd] = DCN_I_intrinsic[dd]
######### Monitors ###############
DCN_Statemon_Uncoupled_noSTDP = StateMonitor(DCN_Uncoupled_noSTDP, ['v', 'I_PC','w'], record=True,dt=t_Monitor)
DCN_Spikemon_Uncoupled_noSTDP = SpikeMonitor(DCN_Uncoupled_noSTDP)
DCN_rate_Uncoupled_noSTDP = PopulationRateMonitor(DCN_Uncoupled_noSTDP)