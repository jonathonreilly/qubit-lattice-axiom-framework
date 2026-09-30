import numpy as np
from scipy.optimize import least_squares
from common import sets
def masses(a,r,d):
    k=np.arange(3); s=a*(1+2*np.sqrt(r)*np.cos(d+2*np.pi*k/3)); return np.sort(s**2)
for name,ms in sets.items():
    m=np.array([ms[k][0] for k in ('e','mu','tau')]); sg=np.array([ms[k][1] for k in ('e','mu','tau')])
    print('==',name,' rel. errors',sg/m)
    def chi(res): return float(np.sum(res**2))
    # hypotheses
    def run(label,free,fixed):
        # free: list of names among a,r,d ; fixed dict
        names=free
        def f(p):
            kw=dict(fixed); 
            for n,v in zip(names,p): kw[n]=v
            return (masses(kw['a'],kw['r'],kw['d'])-m)/sg
        p0={'a':17.7,'r':0.5,'d':2/9}
        best=None
        for da in (0,):
            sol=least_squares(f,[p0[n] for n in names],xtol=1e-15,ftol=1e-15,gtol=1e-15,x_scale=[1e-3 if n!='a' else 1e-2 for n in names] if False else 'jac')
            best=sol
        dof=3-len(names)
        print(f'{label:45s} chi2={chi(best.fun):14.4f} dof={dof}  fit={dict(zip(names,np.round(best.x,9)))}')
    run('exact r=1/2, d=2/9 (a free)',['a'],{'r':0.5,'d':2/9})
    run('r=1/2 exact, d free',['a','d'],{'r':0.5})
    run('d=2/9 exact, r free',['a','r'],{'d':2/9})
    run('all free (0 dof)',['a','r','d'],{})
