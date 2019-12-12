from E_Synapses_Plasticity import *

# rewrite name of voltage and plasticity variables to specificly save it with the right name
#convert str to list 
volt=list(globname)
param = list(globname)
spikes = list(globname)
nois = list(globname)
#add the new words
nois.append('.mat')
volt.append('_VoltageCell.mat')
param.append('_PlasticityVariables.mat')
spikes.append('_SpikeTimes.mat')
nois="".join(nois)
volt="".join(volt)
param="".join(param)
spikes="".join(spikes)

### Plasticity Variables
PV = Struct()
PV.a_PC = mon_N_PC_Coupled.a_PC
PV.a_IO = mon_N_PC_Coupled.a_IO
PV.delta = mon_N_PC_Coupled.delta_weight

### Noise input
Noise = Struct()
Noise.I=Noise_extended_statemon.I

### Voltage of Cell
VoltCell = Struct()
VoltCell.IOsoma = IO_Statemon_Coupled_STDP.Vs
VoltCell.IOdend = IO_Statemon_Coupled_STDP.Vd
VoltCell.PC = PC_Statemon_Coupled_STDP.v
VoltCell.DCN = DCN_Statemon_Coupled_STDP.v

### Spike times
SpikeTimes = Struct()
SpikeTimes.PC = list(PC_Spikemon_Coupled_STDP.spike_trains().values())
SpikeTimes.DCN = list(DCN_Spikemon_Coupled_STDP.spike_trains().values())
SpikeTimes.IO = list(IO_Spikemon_Coupled_STDP.spike_trains().values())
#print(SpikeTimes.IO)
#f = open(spikes,"w")
#f.write( str(SpikeTimes) )
#f.close() 
### 
sio.savemat(nois, mdict={'Noise':Noise})
sio.savemat(volt, mdict={'VoltCell':VoltCell})
sio.savemat(param, mdict={'PV':PV})
sio.savemat(spikes, mdict={'SpikeTimes':SpikeTimes})