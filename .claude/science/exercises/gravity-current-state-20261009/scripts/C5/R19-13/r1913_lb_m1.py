# scalar lower bound (any slab operation) at R = 8..12 for m = 1 and m = 0 (lattice correlators), and at R=10 for heavier m
import numpy as np
from r1913_lib import chain_corr
def LB_chain(M, R):
    Gx, Gp, e0 = chain_corr(float(M), 2*R+2); d = 2*R+1
    a = Gx[0]-Gx[d]; b = Gx[0]-Gx[d+1]
    if b - a < 1e-13: return 0.0
    u = np.log(b/a)/(b-a); Dl = np.exp(-u*a)-np.exp(-u*b); return M*Dl*Dl/4
NQ = 300; t = (np.arange(NQ)+0.5)/NQ; p = 3.0; qv = np.pi*t**p; wv = p*t**(p-1)/NQ
QY, QZ = np.meshgrid(qv, qv, indexing='ij'); WW = np.outer(wv, wv); S = 4*np.sin(QY/2)**2 + 4*np.sin(QZ/2)**2
for m in (1.0, 0.0, 2.0, 3.0):
    for R in ((8, 9, 10, 11, 12) if m < 2 else (4, 6, 8, 10)):
        Mtab = np.logspace(np.log10(max(m, 1e-6)), np.log10(np.sqrt(m*m+8)), 160)
        lt = np.array([LB_chain(Mi, R) for Mi in Mtab])
        v = np.interp(np.log(np.sqrt(m*m+S)), np.log(Mtab), lt, left=0.0, right=0.0)
        print('m=%g R=%d LB=%.4e  (persistent thr 3.78e-124; registered thr/R = %.2e)' % (m, R, (WW*v).sum(), 3.209e-63/R), flush=True)
