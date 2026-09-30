# exploratory (before PREREG for the main test): does the lane's kernel reproduce its own R? and what if the Sommerfeld argument is 2*pi*alpha/v_rel?
import numpy as np
from scipy.integrate import quad
def S(zeta, k):   # k=1: lane's pi*zeta/(1-exp(-pi zeta)); k=2: 2 pi zeta/(1-exp(-2 pi zeta))
    z=k*np.pi*zeta
    return 1.0 if abs(z)<1e-12 else z/(-np.expm1(-z))
def avg(alpha, x, k):
    a=x/4
    num=quad(lambda v: S(alpha/v,k)*v*v*np.exp(-a*v*v),0,np.inf,limit=400)[0]
    den=quad(lambda v: v*v*np.exp(-a*v*v),0,np.inf)[0]
    return num/den
def R(alpha,k,x=25):
    s1=avg(4/3*alpha,x,k); s8=avg(-alpha/6,x,k)
    return 31/9*(8*s1+s8)/9
for al in [0.03,0.048,0.05,0.0907,0.09226]:
    print(al, R(al,1), R(al,2))
