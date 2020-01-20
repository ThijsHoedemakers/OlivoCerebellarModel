from E_Synapses_Plasticity import *

# rewrite name of voltage and plasticity variables to specificly save it with the right name
#convert str to list 
volt=list(globname)
param = list(globname)
spikes = list(globname)
nois = list(globname)
#add the new words
nois.append('AfterSim.pickle')
volt.append('_VoltageCell.pickle')
param.append('_PlasticityVariables.pickle')
spikes.append('_SpikeTimes.pickle')
nois="".join(nois)
volt="".join(volt)
param="".join(param)
spikes="".join(spikes)

### Plasticity Variables
#PV = Struct()
#PV.a_PC = mon_N_PC_Coupled.a_PC
#PV.a_IO = mon_N_PC_Coupled.a_IO
#PV.delta = mon_N_PC_Coupled.delta_weight
PV={'a_PC':mon_N_PC_Coupled.a_PC, 'a_IO':mon_N_PC_Coupled.a_IO, 'delta':mon_N_PC_Coupled.delta_weight}
#PVdict['a_PC']=mon_N_PC_Coupled.a_PC

with open(param, 'wb') as par:
    pickle.dump(PV, par, pickle.HIGHEST_PROTOCOL)
    print('Plasticity variables are saved')
### Noise input
#Input = Struct()
#Input.I=Noise_extended_statemon.I
#Input.nweight = mon_N_PC_Coupled.new_weight
Input={'I':Noise_extended_statemon.I, 'nweight':mon_N_PC_Coupled.new_weight}
with open(nois, 'wb') as inp:
    pickle.dump(Input, inp, pickle.HIGHEST_PROTOCOL)
    print('Inputs are saved')
### Voltage of Cell
#VoltCell = Struct()
#VoltCell.IOsoma = IO_Statemon_Coupled_STDP.Vs
#VoltCell.IOdend = IO_Statemon_Coupled_STDP.Vd
#VoltCell.PC = PC_Statemon_Coupled_STDP.v
#VoltCell.DCN = DCN_Statemon_Coupled_STDP.v
VoltCell = {'IOsoma':IO_Statemon_Coupled_STDP.Vs, 'IOdend':IO_Statemon_Coupled_STDP.Vd, 
            'PC':PC_Statemon_Coupled_STDP.v, 'DCN':DCN_Statemon_Coupled_STDP.v}
with open(volt, 'wb') as vc:
    pickle.dump(VoltCell, vc, pickle.HIGHEST_PROTOCOL)
    print('Voltage Cells are saved')
### Spike times
#SpikeTimes = Struct()
#SpikeTimes.PC = list(PC_Spikemon_Coupled_STDP.spike_trains().values())
#SpikeTimes.DCN = list(DCN_Spikemon_Coupled_STDP.spike_trains().values())
#SpikeTimes.IO = list(IO_Spikemon_Coupled_STDP.spike_trains().values())

SpikeTimes = {'PC':list(PC_Spikemon_Coupled_STDP.spike_trains().values()),
              'DCN':list(DCN_Spikemon_Coupled_STDP.spike_trains().values()),
              'IO':list(IO_Spikemon_Coupled_STDP.spike_trains().values())}
with open(spikes, 'wb') as st:
    pickle.dump(SpikeTimes, st, pickle.HIGHEST_PROTOCOL)
    print('Spike Times are saved')
#print(SpikeTimes.IO)
#f = open(spikes,"w")
#f.write( str(SpikeTimes) )
#f.close() 
### 
#sio.savemat(nois, mdict={'Input':Input})
#sio.savemat(volt, mdict={'VoltCell':VoltCell})
#sio.savemat(param, mdict={'PV':PV})
#sio.savemat(spikes, mdict={'SpikeTimes':SpikeTimes})