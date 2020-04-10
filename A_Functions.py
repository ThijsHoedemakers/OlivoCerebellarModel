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
    
    
def NoiseGenerator(number,noisetype,IC,durationInput,durationTotal,name):
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
        #Input.sine_amplitude = np.array([IC[5], IC[6], IC[7], IC[8],IC[9]])*nA
        Input.sine_frequency = np.array(IC[number*2:])*2*pi*Hz
        #eqs = '''
                
#                I = sine_amplitude*sin(sine_frequency*2*pi*t):amp
#                sine_frequency = (exp(log(fmin)+(log(fmax)-log(fmin))*(0.5-#0.5*cos(2*pi*t/T))))*Hz : Hz
#                sine_amplitude : amp
#                T : second
#                fmin: 1
#                fmax: 1
#                '''
        #Input = NeuronGroup(N_noise, eqs, threshold='True', method='euler', name='Noise', dt=t_Neuron)
        #Input.sine_amplitude = np.array(IC[number:(number+number)])*nA
        #print(Input.sine_amplitude)
        #Input.sine_amplitude = np.array([IC[5], IC[6], IC[7], IC[8],IC[9]])*nA
        #Input.T = 1*second
        #Input.fmin = np.array(IC[-2])#*2*pi*Hz
        #Input.fmax = np.array(IC[-1])#*2*pi*Hz
        #print(Input.fmin, Input.fmax)
        #Input.sine_frequency = np.array([IC[10], IC[11],IC[12],IC[13],IC[14]])*2*pi* Hz

        Input_statemon = StateMonitor(Input, variables=['I'], record=True, dt=t_Neuron)

        # initial condition
        #Noise.sine_amplitude = IC[0] * nA
        #Noise.sine_frequency = IC[1] * 2 * pi * Hz
        # F and A of sine#2
        #Noise.sine2_amplitude = IC[2] * nA
        #Noise.sine2_frequency = IC[3] * 2 * pi * Hz
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


    #Input_created = Struct()
    #Input_created.time = Input_statemon.t / ms
    #Input_created.I = Input_statemon.I
    
    #print('input before offset',Input_created.I)
    #print(Input_created.I[0])
    Is = np.zeros((number,int(durationTotal/(t_Neuron*1000))))
    Inp = Input_statemon.I
    #plt.figure()
    #plt.plot(Input_statemon.t,Is[0])
    for ii in range(0,number):
        Inp[ii] = Inp[ii]+np.ones(len(Inp[ii]))*IC[ii]*nA
        print(len(Inp[ii]))
        Is[ii] =np.append(np.asarray(Inp[ii]),np.zeros(int((durationTotal-durationInput)/(t_Neuron*1000))))
        print(Is[ii])
        
    #Is[1] = Is[1]+np.ones(len(Is[1]))*IC[1]*nA
    #Is[2] = Input_created.I[2]+np.ones(len(Input_created.I[2]))*IC[2]*nA
    #Input_statemon.I[3] = Input_created.I[3]+np.ones(len(Input_created.I[3]))*IC[3]*nA   
    #Input_statemon.I[4] = Input_created.I[4]+np.ones(len(Input_created.I[4]))*IC[4]*nA
    #print(Is)
    #plt.figure()
    #plt.plot(Input_statemon.t,Input_statemon.sine_frequency[0])
    #plt.show()
    simT =int(durationTotal/1000)
    step = int(simT/((t_Neuron/ms)/1000))
    t = np.linspace(0,simT,step)
    t = np.round(t,6)
    Input_created = {'I':Is,'time':t}
    #print(Input_created)
    #local = datetime.datetime.now()
    #sio.savemat(namesp, mdict={'Input_created': Input_created})
    with open(namesp, 'wb') as nn:
        pickle.dump(Input_created, nn, pickle.HIGHEST_PROTOCOL)
        print('Data is saved')
    #Noise_mat = Noise_created
    #Noise = Noise_mat[0][0]
    global Noise_t 
    Noise_t= Input_created['time']
    global Noise_I 
    Noise_I = Input_created['I']
    Noise_I = numpy.ascontiguousarray(Noise_I, dtype=np.float64)
    global N_Noise 
    N_Noise = number

    return Noise_t,Noise_I,N_Noise



