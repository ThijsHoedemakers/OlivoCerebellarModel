from E_Synapses_Plasticity import *

### NETWORK OPERATION 
# The network operation is included to determine firing frequency dependent variables
# Long term frequency
# Short term frequency
@network_operation
def f(t):
    # Get the spikes from the spike monitor
    spike_list_coupled = list(PC_Spikemon_Coupled_STDP.spike_trains().values())
    #spike_list_uncoupled = list(PC_Spikemon_Unoupled_STDP.spike_trains().values())
    #print('spike times',spike_list_coupled)
    # loop over all dummy variables corresponding to the different weights
    for k in range(0,n_PC):
        
        # Get the firing frequency for the short- and long term, 15ms and 1s accordingly
        short_term_variable_coupled = spike_list_coupled[k][-15:]/second 
        long_term_variable_coupled = spike_list_coupled[k][-1000:]/second 
        
        #short_term_variable_uncoupled = spike_list_uncoupled[k][-15:]/second 
        #long_term_variable_uncoupled = spike_list_uncoupled[k][-1000:]/second 
        
        # In the beginning of the simulation the neuron has only spiked once and from there the frequency can not be determined. 
        # therefore this if-statement is added
        if len(short_term_variable_coupled) >=2:
            
            # In the beginning of the simulation there is a transient. 
            # Therefore the plasticity mechanisms only start after a given time
            start_t = spike_list_coupled[0][-1]/second    
            if start_t >= 1:
                S_N_PC_Coupled.f_st[k],S_N_PC_Coupled.f_st[k+10] = np.mean(1/stat.isi(short_term_variable)) # calculate the mean frequency short term
                S_N_PC_Coupled.f_lt[k],S_N_PC_Coupled.f_lt[k+10] = np.mean(1/stat.isi(long_term_variable))  # calculate the mean frequency long term

# Create the network
net = Network(f)
