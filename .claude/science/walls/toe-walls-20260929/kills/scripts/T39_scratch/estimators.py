import numpy as np
from scipy.optimize import brentq, fsolve
from common import sets, dial
def masses(a,r,d):
    k=np.arange(3); s=a*(1+2*np.sqrt(r)*np.cos(d+2*np.pi*k/3)); return np.sort(s**2)
def fit_two(m_pair, idx_pair, r=0.5):
    """with r fixed, solve (a,delta) from two of the sorted masses (idx 0=e,1=mu,2=tau)."""
    tgt=np.array(m_pair)
    def f(p):
        a,d=p; mm=masses(a,r,d); return [mm[idx_pair[0]]/tgt[0]-1, mm[idx_pair[1]]/tgt[1]-1]
    sol=fsolve(f,[17.7,0.2222],xtol=1e-14); return sol
for name,ms in sets.items():
    m=[ms['e'][0],ms['mu'][0],ms['tau'][0]]
    print('==',name)
    q,r,d=dial(m); print(' r-free three-mass fit: r=%.7f delta=%.8f (delta-2/9=%.2e)'%(r,d,d-2/9))
    for (i,j) in [(0,1),(0,2),(1,2)]:
        a,dd=fit_two([m[i],m[j]],(i,j))
        print(' r=1/2 fixed, fit to masses',('e','mu','tau')[i],('e','mu','tau')[j],': delta=%.8f  delta-2/9=%.2e  a^2=%.5f'%(dd,dd-2/9,a*a))
    # exact theory (r=1/2,delta=2/9): scale from each mass, relative residuals of the other two
    for i,nm in enumerate(('e','mu','tau')):
        g=lambda aa: masses(aa,0.5,2/9)[i]-m[i]
        aa=brentq(g,10,30); pm=masses(aa,0.5,2/9)
        print(' theory exact, scale from',nm,': rel.dev of (e,mu,tau) =',np.round((pm-np.array(m))/np.array(m),8), ' | tau dev in sigma:', (pm[2]-m[2])/ms['tau'][1])
