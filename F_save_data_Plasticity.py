from E_Synapses_Plasticity import *

# rewrite name of voltage and plasticity variables to specificly save it with the right name
#convert str to list 
volt=list(globname)
param = list(globname)
spikes = list(globname)
nois = list(globname)
#add the new words
nois.append('AfterSim_Plasticity.pickle')
volt.append('_VoltageCell_Plasticity.pickle')
param.append('_PlasticityVariables.pickle')
spikes.append('_SpikeTimes_Plasticity.pickle')
nois="".join(nois)
volt="".join(volt)
param="".join(param)
spikes="".join(spikes)

### Plasticity Variables

PV={'a_PC':mon_N_PC_Coupled.a_PC, 'a_IO':mon_N_PC_Coupled.a_IO, 'delta':mon_N_PC_Coupled.delta_weight}

with open(param, 'wb') as par:
    pickle.dump(PV, par, pickle.HIGHEST_PROTOCOL)
    print('Plasticity variables are saved')

### Noise input

Input={'I':Noise_extended_statemon.I, 'nweight':mon_N_PC_Coupled.new_weight}
with open(nois, 'wb') as inp:
    pickle.dump(Input, inp, pickle.HIGHEST_PROTOCOL)
    print('Inputs are saved')

### Voltage of Cell

VoltCell = {'IOsoma':IO_Statemon_Coupled_STDP.Vs, 'IOdend':IO_Statemon_Coupled_STDP.Vd, 
            'PC':PC_Statemon_Coupled_STDP.v, 'DCN':DCN_Statemon_Coupled_STDP.v}
with open(volt, 'wb') as vc:
    pickle.dump(VoltCell, vc, pickle.HIGHEST_PROTOCOL)
    print('Voltage Cells are saved')

    ### Spike times

SpikeTimes = {'PC':list(PC_Spikemon_Coupled_STDP.spike_trains().values()),
              'DCN':list(DCN_Spikemon_Coupled_STDP.spike_trains().values()),
              'IO':list(IO_Spikemon_Coupled_STDP.spike_trains().values())}
with open(spikes, 'wb') as st:
    pickle.dump(SpikeTimes, st, pickle.HIGHEST_PROTOCOL)
    print('Spike Times are saved')
