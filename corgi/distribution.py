import numpy as np 

class Distribution:
    def __init__(self,p,dimension=1,spans=[[-1,1]],samplefunction=None,verbose=False):
        self.p = p
        self.dimension = dimension
        self.spans = np.array(spans)

        self.samplefunction = None
        self.xs = list()

        self.verbose = False

    def sample(self):
        if self.samplefunction is not None:
            return self.samplefunction()
        else:
            if self.dimension == 1:
                span = self.spans[0]
                x = np.random.random()*(span[1]-span[0]) + span[0] 
            return x

    def fit(self,checkspan=100,maxiter=10000):
        '''
        Get stable distribution of MCMC in distribution P
        Metropolis-Hastings sampling algorithms
        '''     
        self.xs = list()

        x0 = self.sample()
        self.xs.append(x0)

        t = 0
        flag = False
        while not flag:
            x = self.sample()
            u = np.random.random()

            if u < np.min([self.p(x)/self.p(x0),1]):
                x0 = x
            self.xs.append(x0)

            if len(self.xs) >= 2*checkspan:
                flag = self.check(checkspan)
                del self.xs[:checkspan]

            t += 1
            if t>maxiter:
                break

        return flag

    def check(self,checkspan):
        '''
        Check the stablized status
        '''
        return True

    def evaluate(self,num):
        xs = list()
        x0 = self.xs[-1]
        
        for t in range(num):
            x = self.sample()

            u = np.random.random()
            if u < np.min([self.p(x)/self.p(x0),1]):
                x0 = x
            xs.append(x0)

        return np.array(xs)

