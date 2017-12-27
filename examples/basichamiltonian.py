import sys
sys.path.append('..')

import numpy as np 
from corgi.simulation import fastsimulation
import matplotlib.pyplot as plt

if __name__=='__main__':
    print('Example: wave function oscillation with constant energy')
    def energy(psi,t):
        e = 1.0
        psir,psii = psi
        dpsidt = [e*psii, -e*psir]
        return dpsidt

    psi0 = [1.0,0.0]
    ts = np.linspace(0,10,101)
    sim = fastsimulation(fun=energy,y0=psi0)
    sol = sim.evaluate(ts)

    plt.figure()
    plt.plot(ts, sol[:, 0], 'b', label='$\psi_r(t)$')
    plt.plot(ts, sol[:, 1], 'g', label='$\psi_i(t)$')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.title('Constant energy')
    plt.show(False)
    
    print('Example: wave function oscillation with time-dependent energy')
    def efun(t):
        return 1.0 + 0.5*np.cos(np.pi*t)

    def energy(psi,t):
        e = efun(t)
        psir,psii = psi
        dpsidt = [e*psii, -e*psir]
        return dpsidt

    psi0 = [1.0,0.0]
    ts = np.linspace(0,10,101)
    sim = fastsimulation(fun=energy,y0=psi0)
    sol = sim.evaluate(ts)

    plt.figure()
    plt.plot(ts, sol[:, 0], 'b', label='$\psi_r(t)$')
    plt.plot(ts, sol[:, 1], 'g', label='$\psi_i(t)$')
    plt.plot(ts, efun(ts), 'r', label='energy')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.title('Time-depdent energy')
    plt.show()

    