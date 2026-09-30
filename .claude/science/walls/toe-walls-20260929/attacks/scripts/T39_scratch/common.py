import numpy as np
sets = {
 'note-era PDG2020': dict(e=(0.5109989461,3.1e-9), mu=(105.6583745,2.4e-6), tau=(1776.86,0.12)),
 'PDG2024':          dict(e=(0.51099895000,1.5e-10), mu=(105.6583755,2.3e-6), tau=(1776.93,0.09)),
}
def Q(m):
    m=np.array(m,float); return m.sum()/np.sqrt(m).sum()**2
def dial(m):
    """return Q, r, delta in [0,pi/3] for a mass triple (Brannen form with modulus 2 sqrt(r))."""
    s=np.sqrt(np.sort(np.array(m,float))); a=s.sum()/3
    q=np.sum(np.array(m,float))/s.sum()**2
    r=(3*q-1)/2
    x=(s/a-1)/(2*np.sqrt(r))          # = cos(delta + 2 pi k/3)
    d=np.arccos(np.clip(x.max(),-1,1)) # heaviest (k=0-like) -> cos(delta)
    return q,r,d
def fold(theta):
    """fold an angle into the fundamental domain [0,pi/3] of the Brannen phase."""
    t=np.mod(theta,2*np.pi/3)
    return np.minimum(t,2*np.pi/3-t)
def mc(name,n=20000,seed=1):
    ms=sets[name]; rng=np.random.default_rng(seed)
    out=[]
    for _ in range(n):
        mm=[rng.normal(*ms[k]) for k in ('e','mu','tau')]
        out.append(dial(mm))
    return np.array(out)
if __name__=='__main__':
    for name,ms in sets.items():
        m=[ms['e'][0],ms['mu'][0],ms['tau'][0]]
        q,r,d=dial(m); arr=mc(name)
        print(name,'Q-2/3=%.3e r=%.7f delta=%.7f delta-2/9=%.3e'%(q-2/3,r,d,d-2/9),
              '| MC std: Q %.2e r %.2e delta %.2e | corr(r,delta)=%.3f'%(arr[:,0].std(),arr[:,1].std(),arr[:,2].std(),np.corrcoef(arr[:,1],arr[:,2])[0,1]))
