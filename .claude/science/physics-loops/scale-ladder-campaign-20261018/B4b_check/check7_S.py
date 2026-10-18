import numpy as np, indep_bubble as ib
fS = lambda x: np.sin(x / 2)
N, m = 6, 0.7; K = np.array([0.0, 2*np.pi/N, 0, 0])
base = ib.grid
def shifted(N, shift=0.0):   # same nodes mod 2pi, window [0,2pi) instead of [-pi,pi)
    P = base(N, shift); return np.where(P < 0, P + 2*np.pi, P)
for lab, f in (("S sin(Pbar/2)", fS), ("D sin(Pbar)", np.sin)):
    ib.grid = base; A = ib.bubble(K, N, m, f=f) - ib.bubble(0*K, N, m, f=f)
    ib.grid = shifted; B = ib.bubble(K, N, m, f=f) - ib.bubble(0*K, N, m, f=f)
    print(lab, "window change rel = %.3e" % (np.abs(A - B).max() / np.abs(A).max()))
ib.grid = base
