"""R17-9: 3-knob (b_g, b_f, b_s) re-solve of the VM root at photon grid N = 128, starting from the N = 96 root."""
import numpy as np, time
import smsolve_lib as L
from scipy.optimize import fsolve
L.vert = 'VM'; t0 = time.time()
z = np.load('verified_VM.npy'); kn = [0, 2, 4]
def g(y):
    zz = z.copy(); zz[kn] = y; return L.tot(zz, N=128)[:3]*1e2
y = fsolve(g, z[kn], xtol=1e-10, epsfcn=1e-10); zz = z.copy(); zz[kn] = y
print('N=96 root :', z); print('N=128 root:', zz, ' knob shift', zz[kn] - z[kn])
print('totals N=128:', L.tot(zz, N=128), '(%.0fs)' % (time.time()-t0))
np.save('verified_VM_N128.npy', zz)
