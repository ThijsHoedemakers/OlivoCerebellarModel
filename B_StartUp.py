from A_Functions import *

nameopen = globname+'SimParam.pickle'
with open(nameopen, 'rb') as sims:
    Sims = pickle.load(sims)
#SimParams_mat = loadmat(simpar)['SimParams']
print('loading went fine')

saving =  Sims['saving']
plotting = Sims['plotting']
dt = Sims['dt']*second
exp_runtime = Sims['exp_runtime']*second
IO_response = Sims['IO_response']

N_Cells_PC = Sims['N_Cells_PC']
N_Cells_DCN = Sims['N_Cells_DCN']
N_Cells_IO = Sims['N_Cells_IO']
#SimParams = SimParams_mat[0][0]
#saving = SimParams[0][0]
#plotting = SimParams[1][0]
#dt = SimParams[2][0][0]*second
#exp_runtime = SimParams[3][0][0]*second
#IO_response = SimParams[4][0]

#N_Cells_PC = SimParams[5][0][0]
#N_Cells_DCN = SimParams[6][0][0]
#N_Cells_IO = SimParams[7][0][0]
#####################################################################
########################### PURKINJE CELLS ##########################
#####################################################################
PC_C = 75*pF #rand_params(75,pF,N_Cells_PC,(1.0/N_Cells_PC))  #75*pF  #40 * pF  # 0.77*uF*cm**-2* #1090*pF
PC_gL = 30*nS #rand_params(30,nS,N_Cells_PC,(1.0/N_Cells_PC))  #30 * nS
PC_EL = -70.6 *mV #rand_params(-70.6,mV,N_Cells_PC,(0.5/N_Cells_PC))  #-70.6 * mV
PC_VT = -50.4*mV #rand_params(-50.4,mV,N_Cells_PC,(0.5/N_Cells_PC))  #-50.4 * mV
PC_DeltaT = 2*mV #rand_params(2,mV,N_Cells_PC,(0.5/N_Cells_PC))  #2 * mV
PC_tauw = 144*ms #rand_params(144,ms,N_Cells_PC,(2.0/N_Cells_PC))  #144*ms
PC_a = 4*nS#rand_params(4,nS,N_Cells_PC,(0.5/N_Cells_PC))  #4*nS #2*PC_SingleNeuron.C[jj]/(144*ms) # 
PC_b = 0.0805*nA #rand_params(0.0805,nA,N_Cells_PC,(0.001/N_Cells_PC))  #0.0805*nA  #0*nA #
PC_Vr = -70.6*mV #rand_params(-70.6,mV,N_Cells_PC,(0.5/N_Cells_PC))  #-70.6*mV
PC_v = -70.6*mV #rand_params(-70.6,mV,N_Cells_PC,(0.5/N_Cells_PC))  #[-70.6*mV]*N_Cells_PC
PC_I_intrinsic = 2*nA #rand_params(2,nA,N_Cells_PC,(0.2/N_Cells_PC))  #[2*nA]*N_Cells_PC
#print('intrinsic currents PC',PC_I_intrinsic)
#####################################################################
################### DEEP CEREBELLAR NUCLEI CELLS ####################
#####################################################################
DCN_C = 281*pF #rand_params(281,pF,N_Cells_DCN,(1.0/N_Cells_DCN))  #281*pF  #40 * pF  # 0.77*uF*cm**-2* #1090*pF
DCN_gL = 30*nS #rand_params(30,nS,N_Cells_DCN,(1.0/N_Cells_DCN))  #30 * nS
DCN_EL = -70.6*mV #rand_params(-70.6,mV,N_Cells_DCN,(0.5/N_Cells_DCN))  #-70.6 * mV
DCN_VT = -50.4mV#rand_params(-50.4,mV,N_Cells_DCN,(0.5/N_Cells_DCN))  #-50.4 * mV
DCN_DeltaT = 2*mV# rand_params(2,mV,N_Cells_DCN,(0.5/N_Cells_DCN))  #2 * mV
DCN_tauw = 30*ms#rand_params(30,ms,N_Cells_DCN,(1.0/N_Cells_DCN))  #30*ms
DCN_a = 4*nS#rand_params(4,nS,N_Cells_DCN,(0.5/N_Cells_DCN))  #4*nS #2*DCN_SingleNeuron.C[jj]/(144*ms) # 
DCN_b = 0.0805*nA#rand_params(0.0805,nA,N_Cells_DCN,(0.001/N_Cells_DCN))  #0.0805*nA  #0*nA #
DCN_Vr = -65*mV#rand_params(-65,mV,N_Cells_DCN,(0.5/N_Cells_DCN))  #-65*mV
DCN_tauI= 30*ms#rand_params(30,ms,N_Cells_DCN,(1.0/N_Cells_DCN))  #30*ms
DCN_I_PC_max= 0*nA #rand_params(0.1,nA,N_Cells_DCN,(0.009/N_Cells_DCN))  #0*nA
DCN_v = -70.6*mV#rand_params(-70.6,mV,N_Cells_DCN,(0.5/N_Cells_DCN))  #[-70.6*mV]*N_Cells_DCN
DCN_I_intrinsic = 2.2*nA  #rand_params(2.5,nA,N_Cells_DCN,(0.001/N_Cells_DCN))  #[3*nA]*N_Cells_DCN
#####################################################################
###################### INFERIOR OLIVARY CELLS #######################
#####################################################################
IO_V_Na = 55*mV#rand_params(55,mvolt ,N_Cells_IO,(1.0/N_Cells_IO))  #55*mvolt
IO_V_K = -75*mV#rand_params(-75,mvolt ,N_Cells_IO,(1.0/N_Cells_IO))  #-75*mvolt
IO_V_Ca = 120*mV#rand_params(120,mvolt ,N_Cells_IO,(1.0/N_Cells_IO))  #120*mvolt
IO_V_l = 10*mV#rand_params(10,mvolt ,N_Cells_IO,(1.0/N_Cells_IO))  #10*mvolt 
IO_V_h = -43*mV#rand_params(-43,mvolt ,N_Cells_IO,(1.0/N_Cells_IO))  #-43*mvolt 
IO_Cm = 1*uF*cm**-2#rand_params(1,uF*cm**-2 ,N_Cells_IO,(0.1/N_Cells_IO))  #1*uF*cm**-2 
IO_g_Na = 150*mS/cm**2#rand_params(150,mS/cm**2,N_Cells_IO,(1.0/N_Cells_IO))  #150*mS/cm**2
IO_g_Kdr = 9.0*mS/cm**2#rand_params(9.0,mS/cm**2,N_Cells_IO,(0.1/N_Cells_IO))  #9.0*mS/cm**2
IO_g_K_s = 5.0*mS/cm**2#rand_params(5.0,mS/cm**2,N_Cells_IO,(0.1/N_Cells_IO))  #5.0*mS/cm**2
IO_g_h = 0.12*mS/cm**2#rand_params(0.12,mS/cm**2,N_Cells_IO,(0.01/N_Cells_IO))  #0.12*mS/cm**2
IO_g_Ca_h = 4.5*mS/cm**2#rand_params(4.5,mS/cm**2,N_Cells_IO,(0.1/N_Cells_IO))  #4.5*mS/cm**2
IO_g_K_Ca = 35*mS/cm**2 #rand_params(35,mS/cm**2,N_Cells_IO,(0.5/N_Cells_IO))  #35*mS/cm**2
IO_g_Na_a = 240*mS/cm**2#rand_params(240,mS/cm**2,N_Cells_IO,(1.0/N_Cells_IO))  #240*mS/cm**2
IO_g_K_a = 20*mS/cm**2#rand_params(20,mS/cm**2,N_Cells_IO,(0.5/N_Cells_IO))  #20*mS/cm**2
IO_g_ls = 0.016*mS/cm**2#rand_params(0.016,mS/cm**2,N_Cells_IO,(0.001/N_Cells_IO))  #0.016*mS/cm**2
IO_g_ld = 0.016*mS/cm**2#rand_params(0.016,mS/cm**2,N_Cells_IO,(0.001/N_Cells_IO))  #0.016*mS/cm**2
IO_g_la = 0.016*mS/cm**2#rand_params(0.016,mS/cm**2,N_Cells_IO,(0.001/N_Cells_IO))  #0.016*mS/cm**2
IO_g_int =0.13*mS/cm**2# rand_params(0.13,mS/cm**2,N_Cells_IO,(0.001/N_Cells_IO))  #0.13*mS/cm**2
IO_p =0.25# rand_params(0.25,1,N_Cells_IO,(0.01/N_Cells_IO))  #0.25
IO_p2 =0.15# rand_params(0.15,1,N_Cells_IO,(0.01/N_Cells_IO))   #0.15
# if IO_response=='oscillatory':    
#     IO_g_Ca_l =  rand_params(0.5,mS/cm**2,N_Cells_IO,(0.05/N_Cells_IO))  #[.5*mS/cm**2]*N_Cells_IO
# elif IO_response=='non':    
#     IO_g_Ca_l =  rand_params(0.1,mS/cm**2,N_Cells_IO,(0.05/N_Cells_IO))  #[.1*mS/cm**2]*N_Cells_IO
# elif IO_response=='spiking':    
#     IO_g_Ca_l =  rand_params(1.1,mS/cm**2,N_Cells_IO,(0.2/N_Cells_IO))  #[1.1*mS/cm**2]*N_Cells_IO
# elif IO_response=='both':    
#     IO_g_Ca_l =  rand_params(0.75,mS/cm**2,N_Cells_IO,(0.01/N_Cells_IO))  #[.75*mS/cm**2]*N_Cells_IO
if IO_response=='oscillatory':    
    IO_g_Ca_l =  [.5*mS/cm**2]
elif IO_response=='non':    
    IO_g_Ca_l =  [.1*mS/cm**2]
elif IO_response=='spiking':    
    IO_g_Ca_l =  [1.1*mS/cm**2]
elif IO_response=='both':    
    IO_g_Ca_l =  [.75*mS/cm**2]
    
        




