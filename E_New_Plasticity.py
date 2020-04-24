from E_Synapses_Plasticity import *
import elephant.statistics as stat
from scipy.signal import find_peaks

### NETWORK OPERATION 
# The network operation is included to determine firing frequency dependent variables
# Long term frequency
# Short term frequency
# FIT OF %-max based on parameter
# divided into two parts to make a better fit
dm_part1 = np.array([.20,.28,.26,.38,.14])
dm_part2 = np.array([.14,.08,.29,.20])

freq_part1 = np.array([0.5,0.71,0.83,1,1.3])
freq_part2 = np.array([1.3,2,4,5])

fit_p1 = np.polyfit(freq_part1,dm_part1,3)
fit_p2 = np.polyfit(freq_part2, dm_part2,3)

@network_operation(dt=t_Monitor)
def f(t):
    
    # The time parameters (moving average)
    PC_long_t = t_learn # how much time the average of IO frequency is taken
    PC_short_t = 0.15
    
    IO_long_t =  20 # how much time the average of IO frequency is taken
    IO_short_t = 0.8
    
    t_start = 1*second
    
    ############
    ### LTD ####
    ############
    
    
    ## COUPLED 
    # Get the Voltage of IO to get the spikes
    voltage_IO_coupled = IO_Statemon_Coupled_STDP.Vs
    connection_vector = [9,10,18,17,0,6,5,12,16,11]
    # takes too long to look for spikes every millisecond, perhaps make new network operation with a larger dt, but that has the possibility that it misses the spike..
    #IO_spike_list_coupled = np.empty((n_IO,1+len(IO_Statemon_Coupled_STDP.Vs[0])))
    for k in range(0,n_PC):
        #start_t = IO_spike_list_coupled[0][-1]   
        if t >= 0.1*second:
            spikeio_c, _ = find_peaks(voltage_IO_coupled[connection_vector[k]], height=0.0, distance = 10) 
            spikeio_c = spikeio_c/1000
            IO_spike_list_coupled = np.empty((1,len(spikeio_c)))
            if len(spikeio_c) >= 1:
                IO_spike_list_coupled=spikeio_c
            #print('io spikes before 1 s',IO_spike_list_coupled)
                
          
        if t >= t_start:
            
            IO_short_term_variable_coupled =IO_spike_list_coupled[IO_spike_list_coupled>(t/second-IO_short_t)]
            IO_long_term_variable_coupled = IO_spike_list_coupled
            #nrSpikesIO = len(IO_spike_list_coupled[k])/((t-0.1*second)/second)
        


            # calculate the mean frequency short term
            conn_N_PC_Coupled.freq_st_IO_coupled[k] = conn_N_PC_Coupled.freq_st_IO_coupled[k+10] = np.mean(1/stat.isi(IO_short_term_variable_coupled))
                        
            frequencies_IO_coupled = 1/stat.isi(IO_long_term_variable_coupled)
            
            std_freq_IO_coupled = np.std(frequencies_IO_coupled)
            mean_freq_IO_coupled = np.mean(frequencies_IO_coupled)

            
            if mean_freq_IO_coupled >= 1.3:
                conn_N_PC_Coupled.max_LTD_IO_coupled[k]=conn_N_PC_Coupled.max_LTD_IO_coupled[k+10] = np.polyval(fit_p2,mean_freq_IO_coupled)
                #print('max % change',conn_N_PC_Coupled.max_LTD_IO_coupled[k])
            else:
                conn_N_PC_Coupled.max_LTD_IO_coupled[k]=conn_N_PC_Coupled.max_LTD_IO_coupled[k+10] = np.polyval(fit_p1,mean_freq_IO_coupled)
                #print('max % change',conn_N_PC_Coupled.max_LTD_IO_coupled[k])

            conn_N_PC_Coupled.mean_freq_IO_coupled[k] = conn_N_PC_Coupled.mean_freq_IO_coupled[k+10] = mean_freq_IO_coupled
            #print('mean freq io',mean_freq_IO_coupled)
            conn_N_PC_Coupled.std_f_IO_coupled[k]= conn_N_PC_Coupled.std_f_IO_coupled[k+10] = std_freq_IO_coupled
            
    ## UNCOUPLED
    
    # Get the Voltage of IO to get the spikes
    voltage_IO_uncoupled = IO_Statemon_Uncoupled_STDP.Vs
    connection_vector = [9,10,18,17,0,6,5,12,16,11]
    # takes too long to look for spikes every millisecond, perhaps make new network operation with a larger dt, but that has the possibility that it misses the spike..
    #IO_spike_list_coupled = np.empty((n_IO,1+len(IO_Statemon_Coupled_STDP.Vs[0])))
    for k in range(0,n_PC):
        #start_t = IO_spike_list_coupled[0][-1]   
        if t >= 0.1*second:
            spikeio_uc, _ = find_peaks(voltage_IO_uncoupled[connection_vector[k]], height=0.0, distance = 10) 
            spikeio_uc = spikeio_uc/1000
            IO_spike_list_uncoupled = np.empty((1,len(spikeio_uc)))
            if len(spikeio_uc) >= 1:
                IO_spike_list_uncoupled=spikeio_uc
            #print('io spikes before 1 s',IO_spike_list_coupled)
                
          
        if t >= t_start:
            
            IO_short_term_variable_uncoupled =IO_spike_list_uncoupled[IO_spike_list_uncoupled>(t/second-IO_short_t)]
            IO_long_term_variable_uncoupled = IO_spike_list_uncoupled
            #nrSpikesIO = len(IO_spike_list_coupled[k])/((t-0.1*second)/second)
        


            # calculate the mean frequency short term
            conn_N_PC_Uncoupled.freq_st_IO_uncoupled[k] = conn_N_PC_Uncoupled.freq_st_IO_uncoupled[k+10] = np.mean(1/stat.isi(IO_short_term_variable_uncoupled))
                        
            frequencies_IO_uncoupled = 1/stat.isi(IO_long_term_variable_uncoupled)
            
            mean_freq_IO_uncoupled = np.mean(frequencies_IO_uncoupled)
            std_freq_IO_uncoupled = np.std(frequencies_IO_uncoupled)
            
            if mean_freq_IO_uncoupled >= 1.3:
                conn_N_PC_Uncoupled.max_LTD_IO_uncoupled[k]=conn_N_PC_Uncoupled.max_LTD_IO_uncoupled[k+10] = np.polyval(fit_p2,mean_freq_IO_uncoupled)
                #print('max % change',conn_N_PC_Coupled.max_LTD_IO_coupled[k])
            else:
                conn_N_PC_Uncoupled.max_LTD_IO_uncoupled[k]=conn_N_PC_Uncoupled.max_LTD_IO_uncoupled[k+10] = np.polyval(fit_p1,mean_freq_IO_uncoupled)
                #print('max % change',conn_N_PC_Coupled.max_LTD_IO_coupled[k])

            conn_N_PC_Uncoupled.mean_freq_IO_uncoupled[k] = conn_N_PC_Uncoupled.mean_freq_IO_uncoupled[k+10] = mean_freq_IO_uncoupled
            #print('mean freq io',mean_freq_IO_coupled)
            conn_N_PC_Uncoupled.std_f_IO_uncoupled[k]= conn_N_PC_Uncoupled.std_f_IO_uncoupled[k+10] = std_freq_IO_uncoupled
    
    
    
    
    ############
    ### LTP ###
    ############
    
    ## COUPLED 
    
    # Get the spikes from the spike monitor
    PC_spike_list_coupled = list(PC_Spikemon_Coupled_STDP.spike_trains().values())
    #print('pc spike list',PC_spike_list_coupled)

    #PC_spike_list_coupled = PC_spike_list_coupled/second
    #print('pc spike list',PC_spike_list_coupled)
    # loop over all dummy variables corresponding to the different weights
    for k in range(0,n_PC):
        #start_t = PC_spike_list_coupled[0][-1]/second    
        if t >= t_start :
            # Get the firing frequency for the short- and long term, 15ms and 1s accordingly
            PC_long_term_variable_coupled = (PC_spike_list_coupled[k][PC_spike_list_coupled[k]>(0.5*second)])/second

            PC_short = (PC_long_term_variable_coupled[PC_long_term_variable_coupled>(t/second-PC_short_t)])
            
            PC_long = (PC_long_term_variable_coupled[PC_long_term_variable_coupled>(t/second-PC_long_t)])
            #PC_short = (PC_spike_list_coupled[k][PC_spike_list_coupled[k]>(t-PC_short_t*second)])/second
            #PC_long_term_variable_coupled = (PC_spike_list_coupled[k][PC_spike_list_coupled[k]>(0.5*second)])/second
            #PC_spike_list_coupled[k][-15:]/second 
            PC_long_term_variable_coupled = len(PC_long)/(min(t/second,PC_long_t))
            
            PC_short_term_variable_coupled = len(PC_short)/(PC_short_t)
            #PC_long_term_variable_coupled = (len(PC_long_term_variable_coupled)/(t/second-0.5))
            #(PC_spike_list_coupled[k][PC_spike_list_coupled[k]>(t-PC_long_t*second)])/second
            #PC_spike_list_coupled[k][-1000:]/second 
        #if t == 4.9*second:
            #print('spike list',PC_spike_list_coupled)
            #print('time',t)
            
            #nrSpikesPC = len(PC_long_term_variable_coupled[k])/(t/second-0.99)
      
        # In the beginning of the simulation the neuron has only spiked once and from there the frequency can not be determined. 
        # therefore this if-statement is added
            
            # In the beginning of the simulation there is a transient. 
            # Therefore the plasticity mechanisms only start after a given time
           # if len(short_term_variable_coupled)>1:
                # calculate the mean frequency short term
            conn_N_PC_Coupled.f_st_PC_coupled[k]=conn_N_PC_Coupled.f_st_PC_coupled[k+10] = PC_short_term_variable_coupled
            #conn_N_PC_Coupled.f_st_PC[k]=conn_N_PC_Coupled.f_st_PC[k+10] = len(PC_short_term_variable_coupled)/PC_short_t
                # calculate the mean frequency long term
            conn_N_PC_Coupled.f_lt_PC_coupled[k]=conn_N_PC_Coupled.f_lt_PC_coupled[k+10] = PC_long_term_variable_coupled
            #np.mean(1/stat.isi(PC_long_term_variable_coupled))
            #np.mean(1/stat.isi(PC_long_term_variable_coupled)) 
            
    # UNCOUPLED
    
    # Get the spikes from the spike monitor
    PC_spike_list_uncoupled = list(PC_Spikemon_Uncoupled_STDP.spike_trains().values())
    #print('pc spike list',PC_spike_list_coupled)

    #PC_spike_list_coupled = PC_spike_list_coupled/second
    #print('pc spike list',PC_spike_list_coupled)
    # loop over all dummy variables corresponding to the different weights
    for k in range(0,n_PC):
        #start_t = PC_spike_list_coupled[0][-1]/second    
        if t >= t_start :
            # Get the firing frequency for the short- and long term, 15ms and 1s accordingly
            PC_long_term_variable_uncoupled = (PC_spike_list_uncoupled[k][PC_spike_list_uncoupled[k]>(0.5*second)])/second
            
            PC = (PC_long_term_variable_uncoupled[PC_long_term_variable_uncoupled>(t/second-PC_short_t)])
            
            PC_long =  (PC_long_term_variable_uncoupled[PC_long_term_variable_uncoupled>(t/second-PC_long_t)])
            #PC_long_term_variable_uncoupled = (PC_spike_list_uncoupled[k][PC_spike_list_uncoupled[k]>(0.5*second)])/second
            #PC_spike_list_coupled[k][-15:]/second 
            
            PC_short_term_variable_uncoupled = len(PC)/(PC_short_t)
            
            PC_long_term_variable_uncoupled = len(PC_long)/(min(t/second,PC_long_t))
            #nrPCspikes_uncoupled = len(PC_long_term_variable_uncoupled)/(t/second-0.5)
            
            
            #(PC_spike_list_uncoupled[k][PC_spike_list_uncoupled[k]>(t-PC_long_t*second)])/second
            #PC_spike_list_coupled[k][-1000:]/second 
  
        # In the beginning of the simulation the neuron has only spiked once and from there the frequency can not be determined. 
        # therefore this if-statement is added
            
            # In the beginning of the simulation there is a transient. 
            # Therefore the plasticity mechanisms only start after a given time
           # if len(short_term_variable_coupled)>1:
                # calculate the mean frequency short term
            conn_N_PC_Uncoupled.f_st_PC_uncoupled[k]=conn_N_PC_Uncoupled.f_st_PC_uncoupled[k+10] = PC_short_term_variable_uncoupled 
            
            #conn_N_PC_Coupled.f_st_PC[k]=conn_N_PC_Coupled.f_st_PC[k+10] = len(PC_short_term_variable_coupled)/PC_short_t
                # calculate the mean frequency long term
            conn_N_PC_Uncoupled.f_lt_PC_uncoupled[k]=conn_N_PC_Uncoupled.f_lt_PC_uncoupled[k+10] = PC_long_term_variable_uncoupled
            
            
            #np.mean(1/stat.isi(PC_long_term_variable_uncoupled))
            #np.mean(1/stat.isi(PC_long_term_variable_coupled)) 
    
# Create the network
net = Network(f)
