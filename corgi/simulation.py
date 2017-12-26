# Simulation Core:
#       Calculation of standard ODE

from scipy.integrate import ode

class simulation:
    def __init__(self,fun,y0,t0=0,jac=None,complex=False,method='fortran'):
        self.fun = fun
        self.jac = jac
        
        self.y0 = y0
        self.t0 = t0
        self.method = method 

        self.system = None

    def set_method(self,method):
        methods = ['fortran','RK23','RK45','Radau','BDF','LSODA']
        if method not in methods:
            return False
        self.method = method
        return True

    def set_fun(self,fun):
        self.fun = fun

    def set_jacobian(self,jac):
        self.jac = jac

    def set_initial_value(self,y0,t0):
        self.y0 = y0
        self.t0 = t0

    def init(self):
        self.system = ode(self.fun,self.jac)
        self.system.set_initial_value(self.y0,self.t0)
        return self.system.successful()

    def cal(self,t,step=False,relax=False):
        return self.system.integrate(t,step,relax)
