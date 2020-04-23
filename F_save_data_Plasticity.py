from E_New_Plasticity import *

# rewrite name of voltage and plasticity variables to specificly save it with the right name
#convert str to list 
volt=list(globname)
param = list(globname)
spikes = list(globname)
nois = list(globname)
poprate = list(globname)
#add the new words
nois.append('AfterSim_Plasticity.pickle')
volt.append('_VoltageCell_Plasticity.pickle')
param.append('_PlasticityVariables.pickle')
spikes.append('_SpikeTimes_Plasticity.pickle')
poprate.append('_Population_rate.pickle')
nois="".join(nois)
volt="".join(volt)
param="".join(param)
spikes="".join(spikes)
poprate="".join(poprate)

### Plasticity Variables

PV={'weight_PC_coupled':mon_N_PC_Coupled.weight_PC,'weight_IO_coupled':mon_N_PC_Coupled.weight_IO,'delta_weight_coupled':mon_N_PC_Coupled.delta_weight, 'new_weight_coupled':mon_N_PC_Coupled.new_weight,'weight_PC_uncoupled': mon_N_PC_Uncoupled.weight_PC, 'weight_IO_uncoupled':mon_N_PC_Uncoupled.weight_IO, 'delta_weight_uncoupled':mon_N_PC_Uncoupled.delta_weight, 'new_weight_uncoupled':mon_N_PC_Uncoupled.new_weight,
'PC_long_term_freq_coupled':mon_N_PC_Coupled.f_lt_PC_coupled,'PC_short_term_freq_coupled':mon_N_PC_Coupled.f_st_PC_coupled,'PC_long_term_freq_uncoupled':mon_N_PC_Uncoupled.f_lt_PC_uncoupled,'PC_short_term_freq_uncoupled':mon_N_PC_Uncoupled.f_lt_PC_uncoupled, 'tau_coupled':mon_N_PC_Uncoupled.tau,'tau_uncoupled':mon_N_PC_Coupled.tau}

with open(param, 'wb') as par:
    pickle.dump(PV, par, pickle.HIGHEST_PROTOCOL)
    print('Plasticity variables are saved')

### Noise input

Input={'I':Noise_extended_statemon.I, 'nweight':mon_N_PC_Coupled.new_weight, 'I_InputPC':PC_Statemon_Coupled_STDP.I_Noise}
with open(nois, 'wb') as inp:
    pickle.dump(Input, inp, pickle.HIGHEST_PROTOCOL)
    print('Inputs are saved')

### Voltage of Cell

VoltCell = {'IOsoma_coupled':IO_Statemon_Coupled_STDP.Vs, 'IOdend':IO_Statemon_Coupled_STDP.Vd, 
            'IOsoma_uncoupled':IO_Statemon_Uncoupled_STDP.Vs,'PC_coupled':PC_Statemon_Coupled_STDP.v, 'DCN_coupled':DCN_Statemon_Coupled_STDP.v,'PC_uncoupled':PC_Statemon_Uncoupled_STDP.v, 'DCN_uncoupled':DCN_Statemon_Uncoupled_STDP.v}
with open(volt, 'wb') as vc:
    pickle.dump(VoltCell, vc, pickle.HIGHEST_PROTOCOL)
    print('Voltage Cells are saved')

    ### Spike times

SpikeTimes = {'PC_coupled':list(PC_Spikemon_Coupled_STDP.spike_trains().values()),
              'DCN_coupled':list(DCN_Spikemon_Coupled_STDP.spike_trains().values()),
              'PC_uncoupled':list(PC_Spikemon_Uncoupled_STDP.spike_trains().values()),
              'DCN_uncoupled':list(DCN_Spikemon_Uncoupled_STDP.spike_trains().values()),
              'IO_coupled':list(IO_Spikemon_Coupled_STDP.spike_trains().values()),
             'IO_uncoupled':list(IO_Spikemon_Uncoupled_STDP.spike_trains().values())}
with open(spikes, 'wb') as st:
    pickle.dump(SpikeTimes, st, pickle.HIGHEST_PROTOCOL)
    print('Spike Times are saved')
Population = {'PC_uncoupled':PC_rate_Uncoupled_STDP.smooth_rate(window='gaussian', width=1*ms)/Hz, 'DCN_uncoupled':DCN_rate_Uncoupled_STDP.smooth_rate(window='gaussian',width=1*ms)/Hz, 'IO_uncoupled':IO_rate_Uncoupled_STDP.smooth_rate(window='gaussian',width=1*ms)/Hz,'PC_coupled':PC_rate_Coupled_STDP.smooth_rate(window='gaussian',width=1*ms)/Hz, 'DCN_coupled': DCN_rate_Coupled_STDP.smooth_rate(window='gaussian',width=1*ms)/Hz,'IO_coupled':IO_rate_Coupled_STDP.smooth_rate(window='gaussian',width=1*ms)/Hz,'t':PC_rate_Uncoupled_STDP.t/ms}

with open(poprate, 'wb') as ka:
    pickle.dump(Population, ka, pickle.HIGHEST_PROTOCOL)
    print('population rates saved')