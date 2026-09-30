import numpy as np
def eps(p,q=1.,r=2.):
    d1=1-p**3/(p**3+q**3+4*r**3); d2=1-p*p*q/(p*q*(p+q)+4*r**3); d3=1-p*p/(p*p+q*q+r*(p+q)+2*r*r)
    return d1,max(d2,d3)
def feas(p):
    e1,e2=eps(p)
    best=1e9
    for sg in np.linspace(0.005,0.5,4000):
        c=6*e1/sg; mu=sg*(2+e2/sg)**3
        if mu>=1: continue
        Z=np.linspace(1,0.9999/c,20000)
        g=1+mu*Z/(1-c*Z)**3-Z
        best=min(best,g.min())
    return best
for p in (83.0,83.5,83.6,83.62,83.7,84,90):
    print(p,feas(p))
# independent eta' mean-field check of onset: linear growth rate 3*e2
for p in (11,16,19,19.5):
    print(p,eps(p))
