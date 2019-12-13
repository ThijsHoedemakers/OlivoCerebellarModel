from E_Synapses_Plasticity import *




# print('IO-IO')
# visualise(IO_synapse_Coupled_STDP)
# print('DCN-PC')
# visualise(DCN_PC_Synapse_Coupled_STDP)
# print('IO-DCN')
# visualise(IO_DCN_Synapse_Coupled_STDP)
# print('NOISE-DUMMY')
# visualise(copy_noise_Coupled)
# print('DUMMY-PC')
# visualise(S_N_PC_Coupled)
# print('IO-DUMMY')
# visualise(S_IO_N_Coupled)
# print('IO-PC')
# visualise(Synapse_IO_PC_Coupled_STDP)


if plotting == 'yes':    
    figure(figsize=(15, 4), dpi= 80, facecolor='w', edgecolor='k')
    title('Noise Sources', fontsize=16)
    for ji in range(len(Noise_I)):
        plot(Noise_extended_statemon.t/ms,Noise_extended_statemon.I[ji]/nA, color='C'+str(ji), label=('Noise_I_'+str(ji)))
    xlabel('t (ms)')
    ylabel('I (nA)')
    legend();
    show()  
    
    print('Plasticity')
    figure(figsize=(15, 4), dpi= 80, facecolor='w', edgecolor='k')
    title('I_Noise_PC', fontsize=16)
    for pp in range(0,N_Cells_PC):
        plot(PC_Statemon_Coupled_STDP.t/ms,PC_Statemon_Coupled_STDP.I_Noise[pp]/nA, ('C'+str(pp)), label=('I_Noise_PC'+str(1+pp)))
    xlabel('t (ms)')
    ylabel('I (nA)')
    legend();
    show() 

    print('Plasticity Coupled Scenario')

    figure(figsize=(15, 4), dpi= 80, facecolor='w', edgecolor='k')
    title('Voltage IO Coupled Plasticity', fontsize=16)
    for ii in range(0,N_Cells_IO):
        plot(IO_Statemon_Coupled_STDP.t/msecond, IO_Statemon_Coupled_STDP.Vs[ii]/mvolt, ('C'+str(ii)), lw='1')
    xlabel('Time (ms)')
    ylabel('V (mV)')
    show()
    
    
    for pp in range(0,N_Cells_PC,1):    
        DCN_spikes_Coupled_STDP = DCN_Statemon_Coupled_STDP.v[:]
        Times_DCN_Coupled_STDP = DCN_Spikemon_Coupled_STDP.values('t')[pp]/(dt)
        print("Number of spikes DCN: %s"% np.size(Times_DCN_Coupled_STDP))
    
#     for pp in range(0,N_Cells_PC,1):    
#         DCN_spikes_Coupled_STDP = DCN_Statemon_Coupled_STDP.v[:]
#         Times_DCN_Coupled_STDP = DCN_Spikemon_Coupled_STDP.values('t')[pp]/(0.025*ms)
#         print("Number of spikes DCN: %s"% np.size(Times_DCN_Coupled_STDP))
#         for t in range(0,np.size(Times_DCN_Coupled_STDP),1):
#             i = int(Times_DCN_Coupled_STDP[t])
#             DCN_spikes_Coupled_STDP[pp][i] = 60*mV
#         PC_spikes_Coupled_STDP = PC_Statemon_Coupled_STDP.v[:]
#         Times_PC_Coupled_STDP = PC_Spikemon_Coupled_STDP.values('t')[pp]/(0.025*ms)
#         print("Number of spikes PC: %s"% np.size(Times_PC_Coupled_STDP))
#         for t in range(0,np.size(Times_PC_Coupled_STDP),1):
#             i = int(Times_PC_Coupled_STDP[t])
#             PC_spikes_Coupled_STDP[pp][i] = 50*mV
#         figure(figsize=(15, 4), dpi= 80, facecolor='w', edgecolor='k')
#         title('Voltage Cells '+str(pp+1) + ' Coupled', fontsize=16)
#         plot(PC_Statemon_Coupled_STDP.t/ms, PC_spikes_Coupled_STDP[pp]/mV, ('C'+str(2)), label=('PC'+' '+str(pp+1)))
#         plot(IO_Statemon_Coupled_STDP.t/msecond, IO_Statemon_Coupled_STDP.Vs[pp]/mvolt, ('C'+str(3)), lw='4', label=('Vs'+' '+str(pp+1)))
#         plot(DCN_Statemon_Coupled_STDP.t/ms, DCN_spikes_Coupled_STDP[pp]/mV, ('C'+str(4)), lw='1',label=('DCN'+' '+str(pp+1)))
#         legend(loc='best')
#         xlabel('Time (ms)')
#         ylabel('V (mV)')
#         legend();
#         show()

    
    figure(figsize=(15, 4), dpi= 80, facecolor='w', edgecolor='k')
    title('Voltage Cells DCN Coupled', fontsize=16)
    for pp in range(0,N_Cells_DCN,1):
        plot(DCN_Statemon_Coupled_STDP.t/ms, DCN_Statemon_Coupled_STDP.v[pp]/mV, ('C'+str(pp)), lw='1',label=('DCN'+' '+str(pp+1)))
    legend(loc='best')
    xlabel('Time (ms)')
    ylabel('V (mV)')
    legend();
    show()

#     for pp in range(0,N_Cells_IO,1):
#         figure(figsize=(15, 4), dpi= 80, facecolor='w', edgecolor='k')
#         title('Voltage Cells IO '+str(pp+1) + ' Coupled', fontsize=16)
#         plot(IO_Statemon_Coupled_STDP.t/msecond, IO_Statemon_Coupled_STDP.Vs[pp]/mvolt, ('C'+str(3)), lw='4', label=('Vs'+' '+str(pp+1)))
#         legend(loc='best')
#         xlabel('Time (ms)')
#         ylabel('V (mV)')
#         legend();
#         show()

    figure(figsize=(15, 4), dpi= 80, facecolor='w', edgecolor='k')
    title('Voltage IO Coupled', fontsize=16)
    for ii in range(0,N_Cells_IO):
        plot(IO_Statemon_Coupled_STDP.t/msecond, IO_Statemon_Coupled_STDP.Vs[ii]/mvolt, ('C'+str(ii)), lw='1')
    xlabel('Time (ms)')
    ylabel('V (mV)')
    show()

    figure(figsize=(15, 4), dpi= 80, facecolor='w', edgecolor='k')
    title('a_PC', fontsize=16)
    for pp in range(0,n_Noise*n_PC,1):
        plot(mon_N_PC_Coupled.t/msecond, mon_N_PC_Coupled.a_PC[pp], ('C'+str(pp)), lw='2')
    xlabel('Time (ms)')
    ylabel('V (mV)')
    # legend();
    show()

    figure(figsize=(15, 4), dpi= 80, facecolor='w', edgecolor='k')
    title('a_IO', fontsize=16)
    for pp in range(0,n_Noise*n_PC,1):
        plot(mon_N_PC_Coupled.t/msecond, mon_N_PC_Coupled.a_IO[pp], ('C'+str(pp)), lw='2')
    xlabel('Time (ms)')
    ylabel('V (mV)')
    # legend();
    show()

    figure(figsize=(15, 4), dpi= 80, facecolor='w', edgecolor='k')
    title('delta_weight', fontsize=16)
    for pp in range(0,n_Noise*n_PC,1):
        plot(mon_N_PC_Coupled.t/msecond, mon_N_PC_Coupled.delta_weight[pp], ('C'+str(pp)), lw='2')
    xlabel('Time (ms)')
    ylabel('V (mV)')
    # legend();
    show()


    print('Plasticity Uncoupled Scenario')


    figure(figsize=(15, 4), dpi= 80, facecolor='w', edgecolor='k')
    title('Voltage IO Uncoupled Plasticity', fontsize=16)
    for ii in range(0,N_Cells_IO):
        plot(IO_Statemon_Uncoupled_STDP.t/msecond, IO_Statemon_Uncoupled_STDP.Vs[ii]/mvolt, ('C'+str(ii)), lw='1')
    xlabel('Time (ms)')
    ylabel('V (mV)')
    show()

    for pp in range(0,N_Cells_PC,1):    
        DCN_spikes_Uncoupled_STDP = DCN_Statemon_Uncoupled_STDP.v[:]
        Times_DCN_Uncoupled_STDP = DCN_Spikemon_Uncoupled_STDP.values('t')[pp]/(dt)
        print("Number of spikes DCN: %s"% np.size(Times_DCN_Uncoupled_STDP))
        
#     for pp in range(0,N_Cells_PC,1):    
#         DCN_spikes_Uncoupled_STDP = DCN_Statemon_Uncoupled_STDP.v[:]
#         Times_DCN_Uncoupled_STDP = DCN_Spikemon_Uncoupled_STDP.values('t')[pp]/(0.025*ms)
#         print("Number of spikes DCN: %s"% np.size(Times_DCN_Uncoupled_STDP))
#         for t in range(0,np.size(Times_DCN_Uncoupled_STDP),1):
#             i = int(Times_DCN_Uncoupled_STDP[t])
#             DCN_spikes_Uncoupled_STDP[pp][i] = 60*mV
#         PC_spikes_Uncoupled_STDP = PC_Statemon_Uncoupled_STDP.v[:]
#         Times_PC_Uncoupled_STDP = PC_Spikemon_Uncoupled_STDP.values('t')[pp]/(0.025*ms)
#         print("Number of spikes PC: %s"% np.size(Times_PC_Uncoupled_STDP))
#         for t in range(0,np.size(Times_PC_Uncoupled_STDP),1):
#             i = int(Times_PC_Uncoupled_STDP[t])
#             PC_spikes_Uncoupled_STDP[pp][i] = 50*mV
#         figure(figsize=(15, 4), dpi= 80, facecolor='w', edgecolor='k')
#         title('Voltage Cells '+str(pp+1) + ' Uncoupled', fontsize=16)
#         plot(PC_Statemon_Uncoupled_STDP.t/ms, PC_spikes_Uncoupled_STDP[pp]/mV, ('C'+str(2)), label=('PC'+' '+str(pp+1)))
#         plot(IO_Statemon_Uncoupled_STDP.t/msecond, IO_Statemon_Uncoupled_STDP.Vs[pp]/mvolt, ('C'+str(3)), lw='4', label=('Vs'+' '+str(pp+1)))
#         plot(DCN_Statemon_Uncoupled_STDP.t/ms, DCN_spikes_Uncoupled_STDP[pp]/mV, ('C'+str(4)), lw='1',label=('DCN'+' '+str(pp+1)))
#         legend(loc='best')
#         xlabel('Time (ms)')
#         ylabel('V (mV)')
#         legend();
#         show()

    figure(figsize=(15, 4), dpi= 80, facecolor='w', edgecolor='k')
    title('Voltage Cells DCN Uncoupled', fontsize=16)
    for pp in range(0,N_Cells_DCN,1):    
        plot(DCN_Statemon_Uncoupled_STDP.t/ms, DCN_Statemon_Uncoupled_STDP.v[pp]/mV, ('C'+str(pp)), lw='1',label=('DCN'+' '+str(pp+1)))
    legend(loc='best')
    xlabel('Time (ms)')
    ylabel('V (mV)')
    legend();
    show()

#     for pp in range(0,N_Cells_IO,1):    
#         figure(figsize=(15, 4), dpi= 80, facecolor='w', edgecolor='k')
#         title('Voltage Cells IO'+str(pp+1) + ' Uncoupled', fontsize=16)
#         plot(IO_Statemon_Uncoupled_STDP.t/msecond, IO_Statemon_Uncoupled_STDP.Vs[pp]/mvolt, ('C'+str(3)), lw='4', label=('Vs'+' '+str(pp+1)))
#         legend(loc='best')
#         xlabel('Time (ms)')
#         ylabel('V (mV)')
#         legend();
#         show()

    figure(figsize=(15, 4), dpi= 80, facecolor='w', edgecolor='k')
    title('Voltage IO Uncoupled', fontsize=16)
    for ii in range(0,N_Cells_IO):
        plot(IO_Statemon_Uncoupled_STDP.t/msecond, IO_Statemon_Uncoupled_STDP.Vs[ii]/mvolt, ('C'+str(ii)), lw='1')
    xlabel('Time (ms)')
    ylabel('V (mV)')
    show()
    
    
    figure(figsize=(15, 4), dpi= 80, facecolor='w', edgecolor='k')
    title('a_PC', fontsize=16)
    for pp in range(0,n_Noise*n_PC,1):
        plot(mon_N_PC_Uncoupled.t/msecond, mon_N_PC_Uncoupled.a_PC[pp], ('C'+str(pp)), lw='2')
    xlabel('Time (ms)')
    ylabel('V (mV)')
    # legend();
    show()
    
    
    figure(figsize=(15, 4), dpi= 80, facecolor='w', edgecolor='k')
    title('a_IO', fontsize=16)
    for pp in range(0,n_Noise*n_PC,1):
        plot(mon_N_PC_Uncoupled.t/msecond, mon_N_PC_Uncoupled.a_IO[pp], ('C'+str(pp)), lw='2')
    xlabel('Time (ms)')
    ylabel('V (mV)')
    # legend();
    show()

    figure(figsize=(15, 4), dpi= 80, facecolor='w', edgecolor='k')
    title('delta_weight', fontsize=16)
    for pp in range(0,n_Noise*n_PC,1):
        plot(mon_N_PC_Uncoupled.t/msecond, mon_N_PC_Uncoupled.delta_weight[pp], ('C'+str(pp)), lw='2')
    xlabel('Time (ms)')
    ylabel('V (mV)')
    # legend();
    show()



