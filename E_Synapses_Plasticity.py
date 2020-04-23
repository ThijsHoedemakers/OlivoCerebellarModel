from D_NeuronGroups_Plasticity import *
###########################################################################################################################
###########################################################################################################################
##################################################### COUPLED SCENARIO ####################################################
###########################################################################################################################
###########################################################################################################################
#####################################################################
############################ Synapses ###############################
#####################################################################



t_learn = 10
per_above_lt = 1.1
k_freq = 0.3
print('t_learn =',t_learn)



n_Noise = len(Noise)
n_PC = len(PC_Coupled_STDP)
n_IO = len(IO_Coupled_STDP)
print('number of IO',n_IO)
# constants LTP
timebeforespike = 0.000086*second
max_LTP_per = 0.2
u_var = 60*150     # max modulation at 60s assuming 100Hz firing rate of PC
n_var = (1e-15)/3  # normalisation factor 

# constants LTD
dtt=0.33/(40*3*4)
max_LTD = 0.2

### Fixed connectivity

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

    j_DCNIO = [8 , 19 , 10 ,  3 , 12 , 17 ,  11 ,  5 , 13 ,  14 , 11 ,  0 , 13 ,7 , 10 , 12 , 17 ,  9 ,  8 ,  3 ,  4 , 11 ,  7 ,  0 ,  6 ,  9 ,8 , 12 , 19 , 14 ,  4 ,  3 , 16 ,  0 ,  7 ,  1 , 14 ,  5 , 18 ,17 , 19 , 18 ,  1 , 15 ,  2 , 14 ,  8 ,  7 ,  0 ,  3 , 16 , 13 ,11 ,  5 ,  2 , 10 ,  8 ,  0 ,  7 , 18 , 16 , 11 ,  7 ,  0 ,  6 ,5 ,  9 , 18 , 13 ,  4 , 15 ,  0 , 17 ,  6 ,  8 ,  7 , 14 ,  9 ,18 ,  4 , 17 ,  7 , 14 , 13 ,  3 ,  1 ,  2 ,  8 , 16 ,  9 , 10 ,13 ,  1 ,  5 , 11 , 12 ,  4 , 15 ,  8 , 14 ,  7 ,  1 , 19 , 15 ,2 ,  6 , 14 ,  4 , 16 , 12 , 15 ,  2 ,  5 ,  0 , 17 , 14 , 19 ,13 , 16 ,  6 , 10 ,  9 , 18 , 12 ,  1 ,  6 ,  4 ,  2 , 19 ,  5 ,8 , 17 ,  5 , 15 , 14 , 18 , 10 , 16 ,  3 , 12 ,  3 , 10 , 12 ,13 , 15 ,  9 , 19 , 16 ,  1 ,  2 ,  2 , 11 ,  1 , 10 ,  4 , 17 ,16 , 15 ,  6 , 18 ,  6 , 13 ,  1 ,  9 ,  5 ,  3 ,  4 , 17 , 18 ,10 , 18 , 17 ,  9 , 10 , 19 ,  6 , 12 , 11 , 15 , 13 ,  0 ,  2 ,16 ,  1 ,  3 ,  4 , 19 , 15 , 11 ,  5 , 12 ,  9 ,  7 , 11 ,  8 ,0 ,  2 ,  6 ,  3 , 19]

    
    #[11,4,8,9,14,10,1,7,17,6,9,18,1,0,5,3,6,4,13,2,17,15,4,2,10,16,18,13,19,8,10,4,8,6,3,17,2,19,16,11,19,11,15,2,7,8,4,17,10,1,16,12,15,13,3,0,4,11,1,18,11,8,18,17,12,15,2,5,0,6,15,9,6,8,14,4,18,3,19,12,19,4,14,3,1,11,13,8,15,17,14,16,8,9,11,1,17,2,18,19,12,18,19,10,7,2,13,14,4,5,2,8,5,7,0,13,15,18,6,10,16,3,8,15,1,12,4,7,9,2,10,2,8,5,12,19,16,14,15,4,10,17,13,5,0,18,8,15,4,11,5,12,6,4,2,17,19,14,10,3,17,10,1,15,3,4,7,13,5,16,9,3,15,11,12,0,4,5,7,18,18,2,0,3,9,15,13,1,17,8,14,18,17,3,7,8,9,6,5,13]
    
    # PC - DCN
    i_PCDCN = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,9]
    j_PCDCN = [8,17,13,9,11,14,4,16,1,0,17,5,13,2,3,19,4,7,6,8,15,18,2,8,7,11,0,10,16,17,4,16,19,11,18,7,10,8,5,0,0,17,11,13,3,6,1,8,5,10,19,17,12,15,14,4,8,10,18,11,8,6,1,4,16,5,18,3,2,9,3,9,18,11,14,15,4,17,19,10,6,15,10,5,0,11,9,17,12,2,18,0,3,7,2,16,19,10,5,13]
        
    print('nr of noise is 2')
else:
    print('nr of noise it not 2-5')
# This represents the noise-PC synapses:


conn_N_PC_Coupled = NeuronGroup(n_Noise*n_PC, eqs_syn_Noise_PC_STDP_coupled, method='euler',name = 'dummy_Coupled',dt=t_Neuron)
mon_N_PC_Coupled = StateMonitor(conn_N_PC_Coupled , ['noise_source','PC_target','weight','I','new_weight', 'delta_weight', 'weight_PC','weight_IO','f_lt_PC_coupled','f_st_PC_coupled','max_LTD_IO_coupled','freq_dep_PC', 'freq_dep_IO', 'input_dep','w_PC_coupled','w_IO_coupled','evalCont','tau'], record=True, dt=t_Monitor)
#,'freq_st_IO_coupled','max_LTD_IO_coupled','mean_freq_IO_coupled', 'std_f_IO_coupled','f_st_PC_coupled','f_lt_PC_coupled'
# Set up the labels
ofs_c = np.zeros(n_Noise*n_PC)
ampl_c = np.zeros(n_Noise*n_PC)
freq_c = np.zeros(n_Noise*n_PC)
for kk in range(0,n_Noise):
    #print(k*10, k*10+9)
    ofs_c[kk*10:kk*10+10]=np.ones(n_PC)*input_params[kk]
    ampl_c[kk*10:kk*10+10]=np.ones(n_PC)*input_params[n_Noise+kk]
    freq_c[kk*10:kk*10+10]=np.ones(n_PC)*input_params[n_Noise*2+kk]
print('offset',ofs_c, 'ampl',ampl_c,'freq',freq_c)
conn_N_PC_Coupled.offset = ofs_c
conn_N_PC_Coupled.amplitude = ampl_c
#print(conn_N_PC_Uncoupled.amplitude)
#np.array(input_params[n_Noise:(n_Noise+n_Noise)])*nA
#conn_N_PC_Coupled.weight_PC = np.zeros(n_Noise*n_PC)
conn_N_PC_Coupled.frequency = freq_c
conn_N_PC_Coupled.noise_source = 'i // n_PC'  # i.e., 0, 0, 1, 1, 2, 2, ...
conn_N_PC_Coupled.PC_target = 'i % n_Noise' # i.e., 0, 1, 2, 3, 4, 0, 1, ...
conn_N_PC_Coupled.conn_target = 'i % n_PC' # i.e., 0, 1, 0, 1, 0, 1, 0, 1, 0, 1
conn_N_PC_Coupled.indx = 'conn_target+(10*rand())'
# Set the static weight in some way (can refer to noise_source and PC_target)
#original
conn_N_PC_Coupled.weight = '1-(abs(((conn_target-noise_source)/N_Cells_PC)))'
print(conn_N_PC_Coupled.weight)
#print('weights before', conn_N_PC_Coupled.weight)
# reshape the values to a matrix of size [#input #PC]
norm_coupled=conn_N_PC_Coupled.weight[:].reshape(n_Noise,n_PC)
#print('reshaped weigth',norm_coupled)
# calculate the sum of the column
column_sum= norm_coupled.sum(axis=0)
#print('column sum =', column_sum)
# normalize by the weight of the columns
reshaped_weight = norm_coupled/ column_sum[np.newaxis,:]
# reshape it to the form of 'conn_N_PC_Coupled.weight'
reshaped_weight = reshaped_weight.reshape(n_Noise*n_PC)

#print('final static weights STDP',reshaped_weight)
conn_N_PC_Coupled.weight = 0.5*np.ones((n_Noise*n_PC))

#all_weights.reshape(n_PC,n_Noise)
#print(all_weights)
# "Synapses" to copy over the noise current

##### CHANGE NOISE_EXTENDED TO SIMPLY NOISE
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
                            on_post='''
                           input_dep = ((I_pre/1e-9)/amp)/(clip((I_pre/1e-9)/amp,(amplitude_pre+offset_pre),10)) 
                           freq_dep_PC_pre = (1/(1+exp(-k_freq*(f_st_PC_coupled_pre-per_above_lt*f_lt_PC_coupled_pre))))
                           
                           max_LTP = y_pre*((max_LTD_IO_coupled_pre*new_weight_pre)/(f_lt_PC_coupled_pre*t_learn+(y_pre-1)))
                           weight_PC_pre += max_LTP*w_PC_coupled_pre*input_dep*freq_dep_PC_pre
                          ''' ,
                          method='euler',name = 'dummy_PC_Coupled',dt=t_Neuron)
#
#max_LTP*input_dep*freq_dep                        
# max_LTP = y_pre*((max_LTD_IO_coupled_pre*weight_pre)/(f_lt_PC_pre*60+(y_pre-1)))
#Q: how much ltp? Same as depression?

#(clip(f_st_PC_pre-f_lt_PC_pre,0,20)*I_pre*weight_pre/amp)*1e8
# clip((f_st_PC_pre*(f_st_PC_pre-f_lt_PC_pre)*(I_pre/amp)*weight_pre)/(f_lt_PC_pre+1),0,0.2)

#((-(1e-9)*amplitude_pre*cos(2*pi*frequency_pre*t/second)/(2*pi*frequency_pre)+ amplitude_pre*1e-9*cos(2*pi*frequency_pre*(t-timebeforespike)/second)/(2*pi*frequency_pre)+offset_pre*1e-9*(timebeforespike/second))*(max_LTP*weight_pre/u_var))/n_var'


 #((-(1e-9)*amplitude_pre/(2*pi*frequency_pre)*cos(2*pi*frequency_pre*t/second)+1e-#9*amplitude_pre/(2*pi*frequency_pre)*cos(2*pi*frequency_pre*(t-timebeforespike)/second))+offset_pre*timebeforespike*1e-#9/second)*new_weight_pre/normfactor', 
# "connect if PC target label matches target index":
S_N_PC_Coupled.connect(i=i_dPC,j =j_dPC)

# LTD from IO cells:
S_IO_N_Coupled = Synapses(IO_Coupled_STDP, conn_N_PC_Coupled, 
                           on_pre='''
                           
                        input_dep_post = ((I_post/1e-9)/amp)/(clip((I_post/1e-9)/amp,(amplitude_post+offset_post),10)) 
                        
                        freq_dep_IO_post = (1/(1+exp(-k_freq*(f_st_PC_coupled_post-per_above_lt*f_lt_PC_coupled_post))))
                        max_LTD = y_post*((max_LTD_IO_coupled_post*new_weight_post)/(t_learn*1e2*mean_freq_IO_coupled_post+(y_post-1)))
                                                
                        weight_IO_post += -max_LTD*w_IO_coupled_post*input_dep*freq_dep_IO_post
                        '''
                          ,method='euler',name = 'dummy_IO_Coupled',dt=t_Neuron)  # where f is some function
#

#freq_dep_post = int(y_post*(f_lt_PC_coupled_post/((y_post-1)+f_st_PC_coupled_post)))

#y_post*distribution_eval/(distribution_mean+y_post-1)
# WHY 1E2 TOO SMALL?
#max_LTD = y_post*((max_LTD_IO_coupled_post*weight_post)/(60e2*mean_freq_IO_coupled_post+(y_post-1)))

# input_dep = ((I_post/1e-9)/amp)/(amplitude_post+offset_post)
#                           distribution_eval = y_post*exp(-(freq_st_IO_coupled_post-mean_freq_IO_coupled_post)**2/(2*(y_post-#1)+std_f_IO_coupled_post**2))/((y_post-1)+std_f_IO_coupled_post*sqrt(2*pi))
#                           distribution_mean = y_post*exp(-(mean_freq_IO_coupled_post-mean_freq_IO_coupled_post)**2/(2*(y_post-#1)*std_f_IO_coupled_post**2))/((y_post-1)+std_f_IO_coupled_post*sqrt(2*pi))
#                           freq_dep = y_post*distribution_eval/(distribution_mean+y-1)
#                           max_LTD = (y_post*25*max_LTD_IO_coupled_post*weight_post)/(60e2*mean_freq_IO_coupled_post+(y_post-1))
#                           a_IO_post += - input_dep*freq_dep*max_LTD 
#-clip((f_st_IO_post*(f_st_IO_post-f_lt_IO_post)*(I_post/amp)*weight_post)/(f_lt_IO_post+1),0,0.2)

# weight of all noise-Purkinje synapses:
#-(1e-9*dtt*abs((I_post*weight_post)/nA)*(weight_post*max_LTD))/((offset_post+amplitude_post)*weight_post*1e-9)
IO_index = random.sample(range(N_Cells_IO), 10)
S_IO_N_Coupled.connect(i=i_IOd, j=j_IOd)
#S_IO_N_Coupled.connect(i=IO_index*n_Noise, j=range(len(conn_N_PC_Coupled)))

Synapse_IO_PC_Coupled_STDP = Synapses(IO_Coupled_STDP, PC_Coupled_STDP, on_pre ='w_post +=(0.005*nA)', delay=2*ms, name = 'IO_PC_Synapse_Coupled_STDP',method = 'euler',dt=t_Neuron)
Synapse_IO_PC_Coupled_STDP.connect(i=i_IOPC, j=j_IOPC)
#Synapse_IO_PC_Coupled_STDP.connect(i=IO_index, j=range(n_PC))
    
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

#DCN_PC_Synapse_Coupled_STDP.connect(i=DCN_PC_Synapse_Coupled_targ,j=DCN_PC_Synapse_Coupled_mm)
DCN_PC_Synapse_Coupled_STDP.connect(i=i_PCDCN,j=j_PCDCN)

IO_DCN_Synapse_Coupled_STDP = Synapses(DCN_Coupled_STDP, IO_Coupled_STDP, on_pre = 'I_IO_DCN_post += -0.08*uA*cm**-2', delay=3*ms, name = 'IO_DCN_Synapse_Coupled_STDP', method = 'euler',dt=t_Neuron)
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
#IO_DCN_Synapse_Coupled_STDP.connect(i=IO_DCN_Synapse_Coupled_targ,j=IO_DCN_Synapse_Coupled_mm)

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
conn_N_PC_Uncoupled = NeuronGroup(n_Noise*n_PC, eqs_syn_Noise_PC_STDP_uncoupled, method='euler',name = 'dummy_Uncoupled',dt=t_Neuron)
mon_N_PC_Uncoupled = StateMonitor(conn_N_PC_Uncoupled , ['weight','I','new_weight','delta_weight','weight_PC','weight_IO','f_lt_PC_uncoupled','f_st_PC_uncoupled','max_LTD_IO_uncoupled','w_PC_uncoupled','w_IO_uncoupled','freq_dep_PC', 'freq_dep_IO','evalCont','tau'], record=True, dt=t_Monitor)
#'max_LTD_IO_uncoupled','mean_freq_IO_uncoupled','distribution_mean','distribution_eval', 'freq_st_IO_uncoupled','std_f_IO_uncoupled','f_lt_PC_uncoupled','f_st_PC_uncoupled'
# Set up the labels
ofs = np.zeros(n_Noise*n_PC)
ampl = np.zeros(n_Noise*n_PC)
freq = np.zeros(n_Noise*n_PC)

for kk in range(0,n_Noise):
    #print(k*10, k*10+9)
    ofs[kk*10:kk*10+10]=np.ones(n_PC)*input_params[kk]
    ampl[kk*10:kk*10+10]=np.ones(n_PC)*input_params[n_Noise+kk]
    freq[kk*10:kk*10+10]=np.ones(n_PC)*input_params[n_Noise*2+kk]
print('offset',ofs, 'ampl',ampl,'freq',freq)

conn_N_PC_Uncoupled.offset = ofs
conn_N_PC_Uncoupled.amplitude = ampl
#print(conn_N_PC_Uncoupled.amplitude)
#np.array(input_params[n_Noise:(n_Noise+n_Noise)])*nA
conn_N_PC_Uncoupled.frequency = freq
conn_N_PC_Uncoupled.noise_source = 'i // n_PC'  # i.e., 0, 0, 1, 1, 2, 2, ...
conn_N_PC_Uncoupled.PC_target = 'i % n_Noise' # i.e., 0, 1, 2, 3, 4, 0, 1, ...
conn_N_PC_Uncoupled.conn_target = 'i % n_PC' # i.e., 0, 1, 0, 1, 0, 1, 0, 1, 0, 1
conn_N_PC_Uncoupled.indx = 'conn_target+(10*rand())'
# Set the static weight in some way (can refer to noise_source and PC_target)
#conn_N_PC_Uncoupled.weight = 'abs(1-(abs(((conn_target-noise_source)/N_Cells_PC))))'

### TODO RESHAPE WEIGHT UNCOMMENT!! ####

#norm_uncoupled=conn_N_PC_Uncoupled.weight[:].reshape(n_Noise,n_PC)
# calculate the sum of the column
#column_sumun= norm_uncoupled.sum(axis=0)
# normalize by the weight of the columns
#reshaped_weightun = norm_uncoupled/ column_sumun[np.newaxis,:]
# reshape it to the form of 'conn_N_PC_Coupled.weight'
#reshaped_weightun = reshaped_weightun.reshape(n_Noise*n_PC)

conn_N_PC_Uncoupled.weight=0.5*np.ones((n_Noise*n_PC))

#print('final static weights uncoupled STDP',reshaped_weightun)
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
                            on_post='''  
                            input_dep = ((I_pre/1e-9)/amp)/(clip((I_pre/1e-9)/amp,(amplitude_pre+offset_pre),10)) 
                            freq_dep_PC_pre = (1/(1+exp(-k_freq*(f_st_PC_uncoupled_pre-per_above_lt*f_lt_PC_uncoupled_pre))))

                            max_LTP = y_pre*((max_LTD_IO_uncoupled_pre*new_weight_pre)/(f_lt_PC_uncoupled_pre*t_learn+(y_pre-1)))

                            weight_PC_pre += max_LTP*w_PC_uncoupled_pre*input_dep*freq_dep_PC_pre  
                            '''
                            , method='euler',name = 'dummy_PC_Uncoupled',dt=t_Neuron)
 #                         

#print(S_N_PC_Uncoupled)
#print(S_N_PC_Uncoupled.on_post)
# "connect if PC target label matches target index":
S_N_PC_Uncoupled.connect(i=i_dPC,j =j_dPC)

# LTD from IO cells:
#(1e-9*dtt*abs((I_post*weight_post)/nA)*(weight_post*max_LTD))/((offset_post+amplitude_post)*weight_post*1e-9)
S_IO_N_Uncoupled = Synapses(IO_Uncoupled_STDP, conn_N_PC_Uncoupled, on_pre='''
                        input_dep = ((I_post/1e-9)/amp)/(clip((I_post/1e-9)/amp,(amplitude_post+offset_post),10)) 

                        freq_dep_IO_post = (1/(1+exp(-k_freq*(f_st_PC_uncoupled_post-per_above_lt*f_lt_PC_uncoupled_post))))
                                             
                        max_LTD = y_post*((max_LTD_IO_uncoupled_post*new_weight_post)/(t_learn*1e2*mean_freq_IO_uncoupled_post+(y_post-1)))
                        weight_IO_post += -max_LTD*w_IO_uncoupled_post*input_dep*freq_dep_IO_post
                          ''', 
                            method='euler',name = 'dummy_IO_Uncoupled',dt=t_Neuron)  # where f is some function

#

  #                        -max_LTD*input_dep*freq_dep

#y_post*distribution_eval/(distribution_mean+y_post-1)
# weight of all noise-Purkinje synapses:
# IO_index = random.sample(range(20), 10)
#S_IO_N_Uncoupled.connect(i=IO_index*n_Noise, j=range(len(conn_N_PC_Coupled)))
S_IO_N_Uncoupled.connect(i=i_IOd, j=j_IOd)

Synapse_IO_PC_Uncoupled_STDP = Synapses(IO_Uncoupled_STDP, PC_Uncoupled_STDP, on_pre ='w_post +=(0.005*nA)', delay=2*ms, name = 'IO_PC_Synapse_Uncoupled_STDP',method = 'euler',dt=t_Neuron)
#Synapse_IO_PC_Uncoupled_STDP.connect(i=IO_index, j=range(n_PC))
Synapse_IO_PC_Uncoupled_STDP.connect(i=i_IOPC, j=j_IOPC)

DCN_PC_Synapse_Uncoupled_STDP = Synapses(PC_Uncoupled_STDP, DCN_Uncoupled_STDP, on_pre='I_PC_post = 1.5*nA', delay=2*ms, name = 'PC_DCN_Synapse_Uncoupled_STDP',dt=t_Neuron) 
DCN_PC_Synapse_Uncoupled_a = list(range(N_Cells_DCN))
DCN_PC_Synapse_Uncoupled_m=[]
for ii in range(0,N_Cells_PC):
    DCN_PC_Synapse_Uncoupled_m.append(random.sample(DCN_PC_Synapse_Uncoupled_a, 10))
    for jj in range(0,N_Cells_PC):
        if DCN_PC_Synapse_Uncoupled_m.count(jj) == 10:
            if jj not in a:
                continue
            DCN_PC_Synapse_Uncoupled_a.remove(jj)
DCN_PC_Synapse_Uncoupled_mm = []
for kk in range(len(DCN_PC_Synapse_Uncoupled_m)):
    DCN_PC_Synapse_Uncoupled_mm = DCN_PC_Synapse_Uncoupled_mm+DCN_PC_Synapse_Uncoupled_m[kk]
i = range(N_Cells_PC)
DCN_PC_Synapse_Uncoupled_targ = []
for kk in range(N_Cells_PC):
    for ee in range(10):
        DCN_PC_Synapse_Uncoupled_targ.append(kk)

#DCN_PC_Synapse_Uncoupled_STDP.connect(i=DCN_PC_Synapse_Uncoupled_targ,j=DCN_PC_Synapse_Uncoupled_mm)
DCN_PC_Synapse_Uncoupled_STDP.connect(i=i_PCDCN,j=j_PCDCN)

IO_DCN_Synapse_Uncoupled_STDP = Synapses(DCN_Uncoupled_STDP, IO_Uncoupled_STDP, on_pre = 'I_IO_DCN_post += -0.08*uA*cm**-2', delay=3*ms, name = 'IO_DCN_Synapse_Uncoupled_STDP', method = 'euler',dt=t_Neuron)
#IO_DCN_Synapse_Uncoupled_STDP.connect(j='k for k in range(i,i+int(N_Cells_IO/2))', skip_if_invalid=True)
#IO_DCN_Synapse_Uncoupled_STDP.connect(j='k for k in range(i-int(N_Cells_IO/2)) if i>int(N_Cells_IO/2)')
#IO_DCN_Synapse_Uncoupled_a = list(range(N_Cells_DCN))
#IO_DCN_Synapse_Uncoupled_m=[]
#for ii in range(0,N_Cells_DCN):
#    if size(IO_DCN_Synapse_Uncoupled_a) == 10:
#        break
#    IO_DCN_Synapse_Uncoupled_m.append(random.sample(IO_DCN_Synapse_Uncoupled_a, 10))
#    for jj in range(0,N_Cells_DCN):
#        if IO_DCN_Synapse_Uncoupled_m.count(jj) == 10:
#            if jj not in IO_DCN_Synapse_Uncoupled_a:
#                continue
#            IO_DCN_Synapse_Uncoupled_a.remove(jj)
#IO_DCN_Synapse_Uncoupled_mm = []
#for kk in range(len(IO_DCN_Synapse_Uncoupled_m)):
#    IO_DCN_Synapse_Uncoupled_mm = IO_DCN_Synapse_Uncoupled_mm+IO_DCN_Synapse_Uncoupled_m[kk]
#IO_DCN_Synapse_Uncoupled_i = range(N_Cells_DCN)
#IO_DCN_Synapse_Uncoupled_targ = []
#for kk in range(N_Cells_DCN):
#    for ee in range(10):
#        IO_DCN_Synapse_Uncoupled_targ.append(kk)
#IO_DCN_Synapse_Uncoupled_STDP.connect(i=IO_DCN_Synapse_Uncoupled_targ,j=IO_DCN_Synapse_Uncoupled_mm)
IO_DCN_Synapse_Uncoupled_STDP.connect(i=i_DCNIO,j=j_DCNIO)


eqs_IO_syn_Uncoupled_STDP = ''' I_c_pre = (0*mS/cm**2)*(0.6*e**(-((Vd_pre/mvolt-Vd_post/mvolt)/50)**2) + 0.4)*(Vd_pre-Vd_post) : metre**-2*amp (summed)'''
IO_synapse_Uncoupled_STDP = Synapses(IO_Uncoupled_STDP, IO_Uncoupled_STDP, eqs_IO_syn_Uncoupled_STDP, name = 'IO_Synapse_Uncoupled_STDP')
IO_synapse_Uncoupled_STDP.connect()

