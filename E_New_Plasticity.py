from E_Synapses_Plasticity import *
import elephant.statistics as stat
from scipy.signal import find_peaks

### NETWORK OPERATION 
# The network operation is included to determine firing frequency dependent variables
# Long term frequency
# Short term frequency
@network_operation
def f(t):
    
    # The time parameters (moving average)
    PC_long_t = 0.3 # how much time the average of IO frequency is taken
    PC_short_t = 90e-3
    
    IO_long_t =  5 # how much time the average of IO frequency is taken
    IO_short_t = 0.8
    
    ############
    ### LTD ####
    ############
    
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
                
          
        if t >= 0.5*second:
    # loop over the IO cell 
            #print('io spikes',IO_spike_list_coupled)
            #print('t before spike',t-800*ms)
            IO_short_term_variable_coupled =IO_spike_list_coupled[IO_spike_list_coupled>(t/second-IO_short_t)]
            IO_long_term_variable_coupled = IO_spike_list_coupled[IO_spike_list_coupled>(t/second-IO_long_t)]
        
            #if len(IO_long_term_variable_coupled) >=2:          
                # In the beginning of the simulation there is a transient. 
                # Therefore the plasticity mechanisms only start after a given time

            # calculate the mean frequency short term
            conn_N_PC_Coupled.f_st_IO[k]=conn_N_PC_Coupled.f_st_IO[k+10] = np.mean(1/stat.isi(IO_short_term_variable_coupled)) 
            # calculate the mean frequency long term
            conn_N_PC_Coupled.f_lt_IO[k] = conn_N_PC_Coupled.f_lt_IO[k+10] = np.mean(1/stat.isi(IO_long_term_variable_coupled))  

    ############
    ### LTP ###
    ############
    # Get the spikes from the spike monitor
    PC_spike_list_coupled = list(PC_Spikemon_Coupled_STDP.spike_trains().values())
    #print('pc spike list',PC_spike_list_coupled)

    #PC_spike_list_coupled = PC_spike_list_coupled/second
    #print('pc spike list',PC_spike_list_coupled)
    # loop over all dummy variables corresponding to the different weights
    for k in range(0,n_PC):
        #start_t = PC_spike_list_coupled[0][-1]/second    
        if t >= 0.5*second :
            # Get the firing frequency for the short- and long term, 15ms and 1s accordingly
            short_term_variable_coupled = (PC_spike_list_coupled[k][PC_spike_list_coupled[k]>(t-PC_short_t*second)])/second
            #PC_spike_list_coupled[k][-15:]/second 
            long_term_variable_coupled = (PC_spike_list_coupled[k][PC_spike_list_coupled[k]>(t-PC_long_t*second)])/second
            #PC_spike_list_coupled[k][-1000:]/second 
        #if len(long_term_variable_coupled) >=2:
        #short_term_variable_uncoupled = spike_list_uncoupled[k][-15:]/second 
        #long_term_variable_uncoupled = spike_list_uncoupled[k][-1000:]/second 
        
        # In the beginning of the simulation the neuron has only spiked once and from there the frequency can not be determined. 
        # therefore this if-statement is added
            #if 
            
            # In the beginning of the simulation there is a transient. 
            # Therefore the plasticity mechanisms only start after a given time
            
                # calculate the mean frequency short term
            conn_N_PC_Coupled.f_st_PC[k]=conn_N_PC_Coupled.f_st_PC[k+10] = np.mean(1/stat.isi(short_term_variable_coupled)) 
                # calculate the mean frequency long term
            conn_N_PC_Coupled.f_lt_PC[k]=conn_N_PC_Coupled.f_lt_PC[k+10] = np.mean(1/stat.isi(long_term_variable_coupled))  

# Create the network
net = Network(f)
