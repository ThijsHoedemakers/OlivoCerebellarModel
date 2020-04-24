from E_Synapses_NoPlasticity import *

# rewrite name of voltage and plasticity variables to specificly save it with the right name
#convert str to list 
volt=list(globname)
param = list(globname)
spikes = list(globname)
nois = list(globname)
#add the new words
nois.append('AfterSim_NoPlasticity.pickle')
volt.append('_VoltageCell_NoPlasticity.pickle')
param.append('_PlasticityVariables_NoPlasticity.pickle')
spikes.append('_SpikeTimes_NoPlasticity.pickle')
nois="".join(nois)
volt="".join(volt)
param="".join(param)
spikes="".join(spikes)

Input={'I':Noise_statemon.I, 'nweight':S_statemon.noise_weight, 'I_InputPC':PC_Statemon_Coupled_noSTDP.I_Noise}

with open(nois, 'wb') as inp2:
    pickle.dump(Input, inp2, pickle.HIGHEST_PROTOCOL)
    print('Inputs are saved')

### Voltage of Cell
VoltCell = {'IOsoma_coupled':IO_Statemon_Coupled_noSTDP.Vs, 'IOdend_coupled':IO_Statemon_Coupled_noSTDP.Vd, 
            'PC_coupled':PC_Statemon_Coupled_noSTDP.v, 'DCN_coupled':DCN_Statemon_Coupled_noSTDP.v, 'IOsoma_uncoupled':IO_Statemon_Uncoupled_noSTDP.Vs, 'IOdend_uncoupled':IO_Statemon_Uncoupled_noSTDP.Vd, 
            'PC_uncoupled':PC_Statemon_Uncoupled_noSTDP.v, 'DCN_uncoupled':DCN_Statemon_Uncoupled_noSTDP.v}
with open(volt, 'wb') as vc2:
    pickle.dump(VoltCell, vc2, pickle.HIGHEST_PROTOCOL)
    print('Voltage Cells are saved')

SpikeTimes = {'PC_coupled':list(PC_Spikemon_Coupled_noSTDP.spike_trains().values()),
              'DCN_coupled':list(DCN_Spikemon_Coupled_noSTDP.spike_trains().values()),
              'IO_coupled':list(IO_Spikemon_Coupled_noSTDP.spike_trains().values()),
             'PC_uncoupled':list(PC_Spikemon_Uncoupled_noSTDP.spike_trains().values()),
              'DCN_uncoupled':list(DCN_Spikemon_Uncoupled_noSTDP.spike_trains().values()),
              'IO_uncoupled':list(IO_Spikemon_Uncoupled_noSTDP.spike_trains().values())}
with open(spikes, 'wb') as st2:
    pickle.dump(SpikeTimes, st2, pickle.HIGHEST_PROTOCOL)
    print('Spike Times are saved')