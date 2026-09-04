import numpy as np, math
def report(L=32, svals=(1,2,2.7,4,6,10,16,25,40)):
    n = np.arange(L); kk = 2*np.pi*n/L
    d1 = 2*(1-np.cos(kk))                       # per-direction lattice symbol
    D = d1[:,None,None,None]+d1[None,:,None,None]+d1[None,None,:,None]+d1[None,None,None,:]
    th = lambda s: np.sum(np.exp(-s*(2*np.pi*np.arange(-60,61)/L)**2))
    print(" s      plain rel.err    improved rel.err   winding frac")
    for s in svals:
        exact = th(s)**4
        pl = np.exp(-s*D).sum()
        im = np.exp(-s*(D+D*D/24.0)).sum()
        wind = 8*math.exp(-L*L/(4*s))
        print("%6.2f   %+12.3e   %+12.3e   %8.1e" % (s, pl/exact-1, im/exact-1, wind*(4*np.pi*s)**2/L**4))
if __name__=="__main__":
    for L in (32,64): print("L =",L); report(L); print()
