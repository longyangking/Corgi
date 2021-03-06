import sys
sys.path.append('..')

import numpy as np 
from corgi.distribution import Distribution
import matplotlib.pyplot as plt

if __name__=='__main__':
    def p(x):
        return np.exp(-((x-0.5)**2/0.5**2)) + np.exp(-(x+0.5)**2/0.5**2)

    dis = Distribution(p,spans=[[-2,2]])
    print('Fit status : ',dis.fit(checkspan=1000000))

    num,bins = 3000,21
    data = dis.evaluate(num)

    n,bins,patches = plt.hist(data,bins=bins)

    xs = np.linspace(-2,2,100)
    ps = p(xs)

    c0 = np.max(n)/np.max(ps)
    plt.plot(xs,ps*c0,label='probability')
    plt.xlabel('x')
    plt.ylabel('account')
    plt.legend(loc='best',fontsize=12)
    plt.show()