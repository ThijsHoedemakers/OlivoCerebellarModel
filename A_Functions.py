from brian2 import *
import datetime, pickle, numpy, random
import scipy.io as sio
from scipy.io import loadmat

def visualise(S):
    Ns = len(S.source)
    Nt = len(S.target)
    figure(figsize=(10, 4), dpi= 80, facecolor='w', edgecolor='k')
    subplot(121)
    plot(zeros(Ns), arange(Ns), 'ok', ms=10)
    plot(ones(Nt), arange(Nt), 'ok', ms=10)
    for i, j in zip(S.i, S.j):
        plot([0, 1], [i, j], '-k')
    xticks([0, 1], ['Source', 'Target'])
    ylabel('Neuron index')
    xlim(-0.1, 1.1)
    ylim(-1, max(Ns, Nt))
    subplot(122)
    plot(S.i, S.j, 'ok')
    xlim(-1, Ns)
    ylim(-1, Nt)
    xlabel('Source neuron index')
    ylabel('Target neuron index')
    
def rand_params(Parameter,Unit,N_Cells,Step):
    Nn = [int(N_Cells/2), N_Cells-int(N_Cells/2)] 
    shuffle(Nn)
    Base = int(1/Step)
    Start = int(Base*Parameter)
    Begin = Start - Nn[0]
    End = Start + Nn[1]
    Param_vector = [x / float(Base) for x in range(Begin, End, 1)]*Unit
    shuffle(Param_vector)
    return Param_vector 
    
    
def NoiseGenerator(number,noisetype,IC,durSilence,durationInput,durationTotal,name):
    N_noise = number
    # create global variables, so they can be used in the other scripts as well
    global t_Neuron 
    t_Neuron=0.025*ms
    global t_Monitor 
    t_Monitor=1*ms
    
    global input_params
    input_params=IC
    
    global globname
    globname = name
    namesp=list(name)
    namesp.append('BeforeSim.pickle')
    namesp="".join(namesp)
    
    ### Different types of inputs
    
    # OhlenbeckUhler? 
    if noisetype == 'OU':
        print('Noise input is of type OU')
        tau_noise = 50 * ms
        eqs = '''
        dI/dt = (I0 - I)/tau_noise + sigma*xi*tau_noise**-0.5 : amp 
        I0 : amp
        sigma : amp
        weight : 1
        '''
        Noise = NeuronGroup(N_noise, eqs, threshold='True', method='euler', name='Noise', dt=t_Neuron)

        Noise_statemon = StateMonitor(Noise, variables=['I'], record=True, dt=t_Neuron)
        Noise.I0 = IC[0] * nA  # rand_params(1.5,nA,N_noise,0.4)
        Noise.I = IC[1] * nA  # rand_params(1.5,nA,N_noise,0.3)
        Noise.sigma = IC[2] * nA  # rand_params(0.5,nA,N_noise,-0.3)
        
        # Double sine
    elif noisetype == 'DS':
        print('Noise input is of type double sine')
        # Noise double sine
        eqs = '''
                I = sine_amplitude*sin(sine_frequency*t): amp
                sine_amplitude : amp
                sine_frequency: Hz
                '''
        Input = NeuronGroup(N_noise, eqs, threshold='True', method='euler', name='Noise', dt=t_Neuron)
        Input.sine_amplitude = np.array(IC[number:(number+number)])*nA
        Input.sine_frequency = np.array(IC[number*2:])*2*pi*Hz


        Input_statemon = StateMonitor(Input, variables=['I'], record=True, dt=t_Neuron)

    elif noisetype == 'const' :
        print('Noise is of constant input')
        constValue = IC[0] *nA
        dur = int(duration/(0.025))
        Noise_statemon = Struct()
        Noise_statemon.t = np.arange(0, dur)
        Noise_statemon.I = np.full((number,dur), constValue)
        duration = 0
    else:
        print('Input type is not correct; chose OU,DS or const')

    run(durationInput*ms)
    
    Is  = np.zeros((number,int((durationTotal)/(t_Neuron*1000))))
    Inp = Input_statemon.I

    for ii in range(0,number):
        Inp[ii] = Inp[ii]+np.ones(len(Inp[ii]))*IC[ii]*nA
        I2 = np.append(np.zeros(int(durSilence/(t_Neuron*1000))),Inp[ii])
        Is[ii] = np.append(I2,np.zeros(int((durationTotal-durationInput-durSilence)/(t_Neuron*1000))))

    simT =int(durationTotal/1000)
    step = int(simT/((t_Neuron/ms)/1000))
    t = np.linspace(0,simT,step)
    t = np.round(t,6)
    Input_created = {'I':Is,'time':t}
   
    with open(namesp, 'wb') as nn:
        pickle.dump(Input_created, nn, pickle.HIGHEST_PROTOCOL)
        print('Data is saved')

    global Noise_t 
    Noise_t= Input_created['time']
    global Noise_I 
    Noise_I = Input_created['I']
    Noise_I = numpy.ascontiguousarray(Noise_I, dtype=np.float64)
    global N_Noise 
    N_Noise = number

    return Noise_t,Noise_I,N_Noise



