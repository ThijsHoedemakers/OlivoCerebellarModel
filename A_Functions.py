from brian2 import *
import datetime, pickle, numpy, random
import scipy.io as sio
from scipy.io import loadmat
class Struct:
    pass
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

def NoiseGenerator(number,noisetype,IC,duration,name,sima):
    N_noise = number
    global simpar
    simpar=sima
    global globname
    globname = name
    namesp=list(name)
    namesp.append('.mat')
    namesp="".join(namesp)
    if noisetype == 'OU':
        print('Noise input is of type OU')
        tau_noise = 50 * ms
        eqs = '''
        dI/dt = (I0 - I)/tau_noise + sigma*xi*tau_noise**-0.5 : amp 
        I0 : amp
        sigma : amp
        weight : 1
        '''
        Noise = NeuronGroup(N_noise, eqs, threshold='True', method='euler', name='Noise', dt=1*ms)

        Noise_statemon = StateMonitor(Noise, variables=['I'], record=True, dt=1*ms)
        Noise.I0 = IC[0] * nA  # rand_params(1.5,nA,N_noise,0.4)
        Noise.I = IC[1] * nA  # rand_params(1.5,nA,N_noise,0.3)
        Noise.sigma = IC[2] * nA  # rand_params(0.5,nA,N_noise,-0.3)
    elif noisetype == 'DS':
        print('Noise input is of type double sine')
        # Noise double sine
        eqs = '''
                dI/dt = (sine_amplitude)*sine_frequency*cos(sine_frequency*t)
                +(sine2_amplitude)*sine2_frequency*cos(sine2_frequency*t) : amp
                sine_amplitude : amp
                sine_frequency: Hz
                sine2_amplitude : amp
                sine2_frequency : Hz
                '''
        Noise = NeuronGroup(N_noise, eqs, threshold='True', method='euler', name='Noise', dt=1*ms)

        Noise_statemon = StateMonitor(Noise, variables=['I'], record=True, dt=1 * ms)

        # initial condition
        Noise.sine_amplitude = IC[0] * nA
        Noise.sine_frequency = IC[1] * Hz * 2 * pi
        # F and A of sine#2
        Noise.sine2_amplitude = IC[2] * nA
        Noise.sine2_frequency = IC[3] * Hz * 2 * pi
    elif noisetype == 'const' :
        print('Noise is of constant input')
        constValue = IC[0] *nA
        dur = int(duration/(0.025*10e-3))
        Noise_statemon = Struct()
        Noise_statemon.t = np.arange(0, dur)
        Noise_statemon.I = np.full((number,dur), constValue)
        duration = 0
    else:
        print('Input type is not correct; chose OU,DS or const')
        
        

    run(duration*ms)


    Noise_created = Struct()

    Noise_created.time = Noise_statemon.t / ms
    Noise_created.I = Noise_statemon.I

    #local = datetime.datetime.now()
    #sio.savemat(namesp, mdict={name: Noise_created})
    print('Data is saved')
    #Noise_mat = Noise_created
    #Noise = Noise_mat[0][0]
    global Noise_t 
    Noise_t= Noise_created.time
    global Noise_I 
    Noise_I = Noise_created.I
    Noise_I = numpy.ascontiguousarray(Noise_I, dtype=np.float64)
    global N_Noise 
    N_Noise = len(Noise_I)

    return Noise_t,Noise_I,N_Noise



