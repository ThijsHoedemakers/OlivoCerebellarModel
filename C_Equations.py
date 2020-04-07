from B_StartUp import *
#####################################################################
############################ Input Noise ############################
#####################################################################
N_Noise = len(Noise_I)
I_recorded = TimedArray(Noise_I.T, t_Neuron)
eqs_noise = '''
I = I_recorded(t,i)*amp : amp
'''
Noise = NeuronGroup(N_Noise, eqs_noise, threshold = 'True', method='euler',name = 'Noise',dt=t_Neuron)
Noise_statemon = StateMonitor(Noise, variables=['I'], record=True, dt=t_Monitor)

period = exp_runtime
eqs_noise_extended = '''
I = I_recorded(t % period,i)*amp : amp
'''
Noise_extended = NeuronGroup(N_Noise, eqs_noise_extended, threshold = 'True', method='euler',name = 'Noise_extended',dt=t_Neuron)
Noise_extended_statemon = StateMonitor(Noise_extended, variables=['I'], record=True, dt=t_Monitor)
#####################################################################
########################### Purkinje Cells ##########################
#####################################################################
PC_Equations = """
    dv/dt = (gL*(EL - v) + gL*DeltaT*exp((v - VT)/DeltaT) + I_Noise + I_intrinsic  -w)/C : volt
    dw/dt = (a*(v - EL) - w)/(tauw) : amp
    
    
    I_intrinsic : amp
    I_Noise  : amp  
  
    C : farad
    gL : siemens 
    EL : volt
    VT : volt
    DeltaT : volt
    Vcut : volt
    tauw : second
    a : siemens
    b : ampere
    Vr : volt
"""
#####################################################################
################### Deep Cerebellar Nuclei Cells ####################
#####################################################################
DCN_Equations = """
dv/dt = (gL*(EL - v) + gL*DeltaT*exp((v - VT)/DeltaT) + I_intrinsic - I_PC - w)/C : volt
dw/dt = (a*(v - EL) - w)/tauw : amp

dI_PC/dt = (I_PC_max - I_PC)/tauI : amp

I_intrinsic : amp

C : farad
gL : siemens 
EL : volt
taum : second
VT : volt
DeltaT : volt
Vcut : volt
tauw : second
a : siemens
b : ampere
Vr : volt
tauI : second
I_PC_max : amp
"""
#####################################################################
###################### Inferior Olivary Cells #######################
#####################################################################
eqs_IO_V = '''
dVs/dt = (-(I_ds + I_ls + I_Na + I_Ca_l + I_K_dr + I_h + I_as) + Iapp_s + I_IO_DCN)/Cm : volt
dVd/dt = (-(I_sd + I_ld + I_Ca_h + I_K_Ca + I_c + I_extra) + Iapp_d)/Cm : volt
dVa/dt = (-(I_K_a + I_sa + I_la + I_Na_a))/Cm : volt
dI_IO_DCN/dt = (0*uA*cm**-2 - I_IO_DCN)/(30*ms) : amp*meter**-2
I_c : metre**-2*amp
Iapp_s : metre**-2*amp
Iapp_d : metre**-2*amp
'''
eqs_IO_Ca = '''
dCa/dt = (-3*I_Ca_h*((uamp / cm**2)**-1)*mM - 0.075*Ca)/ms : mM
'''
eqs_IO_Isom = '''
I_as    = (g_int/(1-p2))*(Vs-Va)     : metre**-2*amp
I_ls    = g_ls*(Vs-V_l)              : metre**-2*amp
I_ds    = (g_int/p)*(Vs-Vd)          : metre**-2*amp
I_Na    = g_Na*m_inf**3*h*(Vs-V_Na)  : metre**-2*amp
I_Ca_l  = g_Ca_l*k*k*k*l*(Vs-V_Ca)   : metre**-2*amp
I_K_dr  = g_Kdr*n*n*n*n*(Vs-V_K)     : metre**-2*amp
I_h     = g_h*q*(Vs-V_h)             : metre**-2*amp
I_K_s   = g_K_s*(x_s**4)*(Vs-V_K)    : metre**-2*amp
'''
eqs_IO_Iden = '''
I_extra = a_value                    : metre**-2*amp
I_sd    = (g_int/(1-p))*(Vd-Vs)      : metre**-2*amp
I_ld    = g_ld*(Vd-V_l)              : metre**-2*amp
I_Ca_h  = g_Ca_h*r*r*(Vd-V_Ca)       : metre**-2*amp
I_K_Ca  = g_K_Ca*s*(Vd-V_K)          : metre**-2*amp
'''
eqs_IO_Iax = '''
I_K_a  = g_K_a *x_a**4*(Va-V_K)      : metre**-2*amp
I_sa   = (g_int/p2)*(Va-Vs)          : metre**-2*amp
I_la   = g_la*(Va-V_l)               : metre**-2*amp
I_Na_a = g_Na_a*m_a**3*h_a*(Va-V_Na) : metre**-2*amp
'''
eqs_IO_activation = '''
dh/dt = (h_inf - h)/tau_h : 1
dk/dt = (k_inf - k)/tau_k : 1
dl/dt = (l_inf - l)/tau_l : 1
dn/dt = (n_inf - n)/tau_n : 1
dq/dt = (q_inf - q)/tau_q : 1
dr/dt = (r_inf - r)/tau_r : 1
ds/dt = (s_inf - s)/tau_s : 1
m_a = m_inf_a : 1
dh_a/dt = (h_inf_a - h_a)/tau_h_a : 1
dx_a/dt = (x_inf_a - x_a)/tau_x_a : 1
dx_s/dt = (x_inf_s - x_s)/tau_x_s : 1
'''
eqs_IO_inf = '''
m_inf   = alpha_m /(alpha_m+beta_m)        : 1
h_inf   = alpha_h/(alpha_h+beta_h)         : 1
k_inf   = 1/(1+e**(-(Vs/mvolt+61)/4.2))    : 1
l_inf   = 1/(1+e**((Vs/mvolt+85.5)/8.5))   : 1
n_inf   = alpha_n/(alpha_n+beta_n)         : 1
q_inf   = 1/(1+e**((Vs/mvolt+75)/(5.5)))   : 1
r_inf   = alpha_r/(alpha_r + beta_r)       : 1
s_inf   = alpha_s/(alpha_s+beta_s)         : 1
m_inf_a = 1/(1+(e**((-30-Va/mvolt)/ 5.5))) : 1
h_inf_a = 1/(1+(e**((-60-Va/mvolt)/-5.8))) : 1
x_inf_a = alpha_x_a/(alpha_x_a+beta_x_a)   : 1
x_inf_s = alpha_x_s/(alpha_x_s + beta_x_s) : 1
'''
eqs_IO_tau = '''
tau_h   = 170*msecond/(alpha_h+beta_h)                                          : second
tau_k   = 5*msecond                                                             : second
tau_l   = 1*msecond*(35+(20*e**((Vs/mvolt+160)/30/(1+e**((Vs/mvolt+84)/7.3))))) : second
tau_n   = 5*msecond/(alpha_n+beta_n)                                            : second
tau_q   = 1*msecond/(e**((-0.086*Vs/mvolt-14.6))+e**((0.07*Vs/mvolt-1.87)))     : second
tau_r   = 5*msecond/(alpha_r + beta_r)                                          : second
tau_s   = 1*msecond/(alpha_s + beta_s)                                          : second
tau_h_a = 1.5*msecond*e**((-40-Va/mvolt)/33)                                    : second
tau_x_a = 1*msecond/(alpha_x_a + beta_x_a)                                      : second
tau_x_s = 1*msecond/(alpha_x_s + beta_x_s)                                      : second
'''
eqs_IO_alpha = '''
alpha_m   = (0.1*(Vs/mvolt + 41))/(1-e**(-(Vs/mvolt+41)/10)) : 1
alpha_h   = 5.0*e**(-(Vs/mvolt+60)/15) : 1
alpha_n   = (Vs/mvolt + 41)/(1-e**(-(Vs/mvolt+41)/10)) : 1
alpha_r   = 1.7/(1+e**(-(Vd/mvolt - 5)/13.9)) : 1
alpha_s   = ((0.00002*Ca/mM)*int((0.00002*Ca/mM)<0.01) + 0.01*int((0.00002*Ca/mM)>=0.01)) : 1
alpha_x_a = 0.13*(Va/mvolt + 25)/(1-e**(-(Va/mvolt+25)/10)) : 1
alpha_x_s = 0.13*(Vs/mvolt + 25)/(1-e**(-(Vs/mvolt+25)/10)) : 1
'''

eqs_IO_beta = '''
beta_m = 9.0*e**(-(Vs/mvolt+60)/20)                        : 1
beta_h = (Vs/mvolt+50)/(1-e**(-(Vs/mvolt+50)/10))          : 1
beta_n = 12.5*e**(-(Vs/mvolt+51)/80)                       : 1
beta_r = 0.02*(Vd/mvolt + 8.5)/(e**((Vd/mvolt + 8.5)/5)-1) : 1
beta_s = 0.015                                             : 1
beta_x_a  = 1.69*e**(-0.0125*(Va/mvolt + 35))              : 1
beta_x_s  = 1.69*e**(-0.0125*(Vs/mvolt+ 35))               : 1
'''

eqs_vector = '''
V_Na : volt
V_K  : volt
V_Ca : volt
V_l  : volt
V_h  : volt
Cm : farad*meter**-2
g_Na   : siemens/meter**2
g_Kdr  : siemens/meter**2
g_Ca_l : siemens/meter**2
g_h    : siemens/meter**2
g_Ca_h : siemens/meter**2
g_K_Ca : siemens/meter**2
g_ls : siemens/meter**2
g_ld : siemens/meter**2
g_int  : siemens/meter**2
g_Na_a   : siemens/meter**2
g_K_a   : siemens/meter**2
g_la   : siemens/meter**2
g_K_s   : siemens/meter**2
p : 1
p2 : 1
a_value : metre**-2*amp
'''

eqs_IO = eqs_IO_beta
eqs_IO += eqs_IO_alpha
eqs_IO += eqs_IO_tau
eqs_IO += eqs_IO_inf
eqs_IO += eqs_IO_activation
eqs_IO += eqs_IO_Iax
eqs_IO += eqs_IO_Iden
eqs_IO += eqs_IO_Isom
eqs_IO += eqs_IO_Ca
eqs_IO += eqs_IO_V
eqs_IO += eqs_vector



## Deleted (1.0/N_Noise) since it is already normalized in the weights

eqs_syn_Noise_PC_noSTDP = '''
    noise_weight : 1
    I_Noise_post = (noise_weight)*(I_pre) : amp (summed)
'''
# ADD new_weight = weight+delta_weight
eqs_syn_Noise_PC_STDP = '''
                        I : amp  # copy of the noise current
                        weight : 1  (constant)
                        new_weight = weight + delta_weight : 1 
                    
                        delta_weight = weight_PC + weight_IO : 1

                        w_PC_coupled = (1-1/(1+exp(-200*(weight_PC-max_LTD_IO_coupled*weight/1.2)))) : 1                   
                        w_IO_coupled = (1/(1+exp(-200*(weight_IO+max_LTD_IO_coupled*weight/1.2)))) : 1
                        w_PC_uncoupled =(1-1/(1+exp(-200*(weight_PC-max_LTD_IO_uncoupled*weight/1.2)))) : 1                    
                        w_IO_uncoupled =(1/(1+exp(-200*(weight_IO+max_LTD_IO_uncoupled*weight/1.2)))) : 1
                        
                        weight_PC : 1
                        weight_IO : 1
                       
                        y = clip(int(t/second-0.9),0,1) : 1

                        f_st_PC_coupled : 1 # frequency short term
                        f_lt_PC_coupled : 1 # frequency long term
                        
                        f_lt_PC_uncoupled : 1
                        f_st_PC_uncoupled : 1
                        
                        freq_st_IO_coupled : 1
                        freq_st_IO_uncoupled : 1

                        std_f_IO_coupled : 1 # frequency short term
                        mean_freq_IO_coupled : 1 # frequency long term
                        max_LTD_IO_coupled : 1
                        
                        std_f_IO_uncoupled : 1 # frequency short term
                        mean_freq_IO_uncoupled : 1 # frequency long term
                        max_LTD_IO_uncoupled : 1
                        
                        
                        input_dep : 1
                        freq_dep : 1
                        offset : 1 # offset of the input
                        amplitude : 1 # amplitude of the input
                        frequency : 1  # frequency of the input

                        noise_source : integer (constant)
                        PC_target : integer (constant)
                        conn_target : integer (constant)
                        indx : integer (constant)

'''
# w_PC = (1-1/(1+exp(-200*(delta_weight-max_LTD_IO_uncoupled*weight/1.2)))) : 1

                        #w_IO = (1/(1+exp(-200*(delta_weight+max_LTD_IO_uncoupled*weight/1.2)))) :1
                        
#max_LTD_IO_uncoupled*weight*(ceil(delta_weight)*(1-1/(1+exp(-100*(delta_weight-max_LTD_IO_uncoupled*weight/2))))+floor(delta_weight)*(-1)*(1/(1+exp(-100*(delta_weight+max_LTD_IO_uncoupled*weight/2))))) : 1

# dweight_IO/dt = (a_IO/second) : 1
                        
#dweight_PC/dt = ((f_st_PC*(f_st_PC-f_lt_PC)*I*weight)/(f_lt_PC+1))/(amp*second) : 1
#dweight_IO/dt = ((f_st_IO*(f_st_IO-f_lt_IO)*I*weight)/(f_lt_IO+1))/(amp*second) : 1

eqs_IO_syn_Coupled = ''' I_c_pre = (0.00125*mS/cm**2)*(0.6*e**(-((Vd_pre/mvolt-Vd_post/mvolt)/50)**2) + 0.4)*(Vd_pre-Vd_post) : metre**-2*amp (summed)'''
