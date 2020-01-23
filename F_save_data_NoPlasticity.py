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

#PV={'a_PC':mon_N_PC_Coupled.a_PC, 'a_IO':mon_N_PC_Coupled.a_IO, 'delta':mon_N_PC_Coupled.delta_weight}

#with open(param, 'wb') as par:
#    pickle.dump(PV, par, pickle.HIGHEST_PROTOCOL)
#    print('Plasticity variables are saved')

Input={'I':S_statemon.I_Noise, 'nweight':S_statemon.noise_weight}

with open(nois, 'wb') as inp2:
    pickle.dump(Input, inp2, pickle.HIGHEST_PROTOCOL)
    print('Inputs are saved')

### Voltage of Cell
VoltCell = {'IOsoma':IO_Statemon_Coupled_noSTDP.Vs, 'IOdend':IO_Statemon_Coupled_noSTDP.Vd, 
            'PC':PC_Statemon_Coupled_noSTDP.v, 'DCN':DCN_Spikemon_Coupled_noSTDP.v}
with open(volt, 'wb') as vc2:
    pickle.dump(VoltCell, vc2, pickle.HIGHEST_PROTOCOL)
    print('Voltage Cells are saved')

SpikeTimes = {'PC':list(PC_Spikemon_Coupled_noSTDP.spike_trains().values()),
              'DCN':list(DCN_Spikemon_Coupled_noSTDP.spike_trains().values()),
              'IO':list(IO_Spikemon_Coupled_noSTDP.spike_trains().values())}
with open(spikes, 'wb') as st2:
    pickle.dump(SpikeTimes, st2, pickle.HIGHEST_PROTOCOL)
    print('Spike Times are saved')