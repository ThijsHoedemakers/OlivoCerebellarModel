from E_Synapses_NoPlasticity import *

if plotting == 'yes':    
    figure(figsize=(15, 4), dpi= 80, facecolor='w', edgecolor='k')
    title('Noise Sources', fontsize=16)
    for ji in range(len(Noise_I)):
        plot(Noise_statemon.t/ms,Noise_statemon.I[ji]/nA, color='C'+str(ji), label=('Noise_I_'+str(ji)))
    legend(loc='best')
    xlabel('t (ms)')
    ylabel('I (nA)')
    legend();
    show()  

    figure(figsize=(15, 4), dpi= 80, facecolor='w', edgecolor='k')
    title('I_Noise_PC', fontsize=16)
    for pp in range(0,N_Cells_PC):
        plot(PC_Statemon_Coupled_noSTDP.t/ms,PC_Statemon_Coupled_noSTDP.I_Noise[pp]/nA, ('C'+str(pp)), label=('I_Noise_PC'+str(1+pp)))
    legend(loc='best')
    xlabel('t (ms)')
    ylabel('I (nA)')
    legend();
    show() 
    
    print('Coupled Scenario')

    figure(figsize=(15, 4), dpi= 80, facecolor='w', edgecolor='k')
    title('Voltage IO Coupled No Plasticity', fontsize=16)
    for ii in range(0,N_Cells_IO):
        plot(IO_Statemon_Coupled_noSTDP.t/msecond, IO_Statemon_Coupled_noSTDP.Vs[ii]/mvolt, ('C'+str(ii)), lw='1')
    xlabel('Time (ms)')
    ylabel('V (mV)')
    show()
    
    
    for pp in range(0,N_Cells_PC,1):    
        DCN_spikes_Coupled_noSTDP = DCN_Statemon_Coupled_noSTDP.v[:]
        Times_DCN_Coupled_noSTDP = DCN_Spikemon_Coupled_noSTDP.values('t')[pp]/(0.025*ms)
        print("Number of spikes DCN: %s"% np.size(Times_DCN_Coupled_noSTDP))

#     for pp in range(0,N_Cells_PC,1):    
#         DCN_spikes_Coupled_noSTDP = DCN_Statemon_Coupled_noSTDP.v[:]
#         Times_DCN_Coupled_noSTDP = DCN_Spikemon_Coupled_noSTDP.values('t')[pp]/(0.025*ms)
#         print("Number of spikes DCN: %s"% np.size(Times_DCN_Coupled_noSTDP))
#         for t in range(0,np.size(Times_DCN_Coupled_noSTDP),1):
#             i = int(Times_DCN_Coupled_noSTDP[t])
#             DCN_spikes_Coupled_noSTDP[pp][i] = 60*mV
#         PC_spikes_Coupled_noSTDP = PC_Statemon_Coupled_noSTDP.v[:]
#         Times_PC_Coupled_noSTDP = PC_Spikemon_Coupled_noSTDP.values('t')[pp]/(0.025*ms)
#         print("Number of spikes PC: %s"% np.size(Times_PC_Coupled_noSTDP))
#         for t in range(0,np.size(Times_PC_Coupled_noSTDP),1):
#             i = int(Times_PC_Coupled_noSTDP[t])
#             PC_spikes_Coupled_noSTDP[pp][i] = 50*mV
#         figure(figsize=(15, 4), dpi= 80, facecolor='w', edgecolor='k')
#         title('Voltage Cells '+str(pp+1) + ' Coupled', fontsize=16)
#         plot(PC_Statemon_Coupled_noSTDP.t/ms, PC_spikes_Coupled_noSTDP[pp]/mV, ('C'+str(2)), label=('PC'+' '+str(pp+1)))
#         plot(IO_Statemon_Coupled_noSTDP.t/msecond, IO_Statemon_Coupled_noSTDP.Vs[pp]/mvolt, ('C'+str(3)), lw='4', label=('Vs'+' '+str(pp+1)))
#         plot(DCN_Statemon_Coupled_noSTDP.t/ms, DCN_spikes_Coupled_noSTDP[pp]/mV, ('C'+str(4)), lw='1',label=('DCN'+' '+str(pp+1)))
#         legend(loc='best')
#         xlabel('Time (ms)')
#         ylabel('V (mV)')
#         legend();
#         show()
        
        
    figure(figsize=(15, 4), dpi= 80, facecolor='w', edgecolor='k')
    title('Voltage DCN Cells Coupled', fontsize=16)
    for pp in range(0,N_Cells_DCN,1):    
        plot(DCN_Statemon_Coupled_noSTDP.t/ms, DCN_Statemon_Coupled_noSTDP.v[pp]/mV, ('C'+str(pp)), lw='1',label=('DCN'+' '+str(pp+1)))
    legend(loc='best')
    xlabel('Time (ms)')
    ylabel('V (mV)')
    legend();
    show()
        
        
#     for pp in range(0,N_Cells_IO,1):   
#         figure(figsize=(15, 4), dpi= 80, facecolor='w', edgecolor='k')
#         title('Voltage IO Cells '+str(pp+1) + ' Coupled', fontsize=16)
#         plot(IO_Statemon_Coupled_noSTDP.t/msecond, IO_Statemon_Coupled_noSTDP.Vs[pp]/mvolt, ('C'+str(3)), lw='4', label=('Vs'+' '+str(pp+1)))
#         legend(loc='best')
#         xlabel('Time (ms)')
#         ylabel('V (mV)')
#         legend();
#         show()

    figure(figsize=(15, 4), dpi= 80, facecolor='w', edgecolor='k')
    title('Voltage IO Coupled', fontsize=16)
    for ii in range(0,N_Cells_IO):
        plot(IO_Statemon_Coupled_noSTDP.t/msecond, IO_Statemon_Coupled_noSTDP.Vs[ii]/mvolt, ('C'+str(ii)), lw='1')
    xlabel('Time (ms)')
    ylabel('V (mV)')
    show()
    
    
    
    print('Uncoupled Scenario')

    figure(figsize=(15, 4), dpi= 80, facecolor='w', edgecolor='k')
    title('Voltage IO Uncoupled No Plasticity', fontsize=16)
    for ii in range(0,N_Cells_IO):
        plot(IO_Statemon_Uncoupled_noSTDP.t/msecond, IO_Statemon_Uncoupled_noSTDP.Vs[ii]/mvolt, ('C'+str(ii)), lw='1')
    xlabel('Time (ms)')
    ylabel('V (mV)')
    show()
    
    for pp in range(0,N_Cells_PC,1):    
        DCN_spikes_Uncoupled_noSTDP = DCN_Statemon_Uncoupled_noSTDP.v[:]
        Times_DCN_Uncoupled_noSTDP = DCN_Spikemon_Uncoupled_noSTDP.values('t')[pp]/(0.025*ms)
        print("Number of spikes DCN: %s"% np.size(Times_DCN_Uncoupled_noSTDP))
        
#     for pp in range(0,N_Cells_PC,1):    
#         DCN_spikes_Uncoupled_noSTDP = DCN_Statemon_Uncoupled_noSTDP.v[:]
#         Times_DCN_Uncoupled_noSTDP = DCN_Spikemon_Uncoupled_noSTDP.values('t')[pp]/(0.025*ms)
#         print("Number of spikes DCN: %s"% np.size(Times_DCN_Uncoupled_noSTDP))
#         for t in range(0,np.size(Times_DCN_Uncoupled_noSTDP),1):
#             i = int(Times_DCN_Uncoupled_noSTDP[t])
#             DCN_spikes_Uncoupled_noSTDP[pp][i] = 60*mV
#         PC_spikes_Uncoupled_noSTDP = PC_Statemon_Uncoupled_noSTDP.v[:]
#         Times_PC_Uncoupled_noSTDP = PC_Spikemon_Uncoupled_noSTDP.values('t')[pp]/(0.025*ms)
#         print("Number of spikes PC: %s"% np.size(Times_PC_Uncoupled_noSTDP))
#         for t in range(0,np.size(Times_PC_Uncoupled_noSTDP),1):
#             i = int(Times_PC_Uncoupled_noSTDP[t])
#             PC_spikes_Uncoupled_noSTDP[pp][i] = 50*mV
#         figure(figsize=(15, 4), dpi= 80, facecolor='w', edgecolor='k')
#         title('Voltage Cells '+str(pp+1) + ' Uncoupled', fontsize=16)
#         plot(PC_Statemon_Uncoupled_noSTDP.t/ms, PC_spikes_Uncoupled_noSTDP[pp]/mV, ('C'+str(2)), label=('PC'+' '+str(pp+1)))
#         plot(IO_Statemon_Uncoupled_noSTDP.t/msecond, IO_Statemon_Uncoupled_noSTDP.Vs[pp]/mvolt, ('C'+str(3)), lw='4', label=('Vs'+' '+str(pp+1)))
#         plot(DCN_Statemon_Uncoupled_noSTDP.t/ms, DCN_spikes_Uncoupled_noSTDP[pp]/mV, ('C'+str(4)), lw='1',label=('DCN'+' '+str(pp+1)))
#         legend(loc='best')
#         xlabel('Time (ms)')
#         ylabel('V (mV)')
#         legend();
#         show()
        
        
    
    figure(figsize=(15, 4), dpi= 80, facecolor='w', edgecolor='k')
    title('Voltage DCN Cells Uncoupled', fontsize=16)
    for pp in range(0,N_Cells_DCN,1): 
        plot(DCN_Statemon_Uncoupled_noSTDP.t/ms, DCN_Statemon_Uncoupled_noSTDP.v[pp]/mV, ('C'+str(pp)), lw='1',label=('DCN'+' '+str(pp+1)))
    legend(loc='best')
    xlabel('Time (ms)')
    ylabel('V (mV)')
    legend();
    show()
        
        
#     for pp in range(0,N_Cells_IO,1):   
#         figure(figsize=(15, 4), dpi= 80, facecolor='w', edgecolor='k')
#         title('Voltage IO Cells '+str(pp+1) + ' Uncoupled', fontsize=16)
#         plot(IO_Statemon_Uncoupled_noSTDP.t/msecond, IO_Statemon_Uncoupled_noSTDP.Vs[pp]/mvolt, ('C'+str(3)), lw='4', label=('Vs'+' '+str(pp+1)))
#         legend(loc='best')
#         xlabel('Time (ms)')
#         ylabel('V (mV)')
#         legend();
#         show()

    figure(figsize=(15, 4), dpi= 80, facecolor='w', edgecolor='k')
    title('Voltage IO Uncoupled', fontsize=16)
    for ii in range(0,N_Cells_IO):
        plot(IO_Statemon_Uncoupled_noSTDP.t/msecond, IO_Statemon_Uncoupled_noSTDP.Vs[ii]/mvolt, ('C'+str(ii)), lw='1')
#     legend(loc='best')
    xlabel('Time (ms)')
    ylabel('V (mV)')
#     legend();
    show()