"""R19-26: r1926_fourier.py's convention-free periodic-gauge test on lines that pass through the soft/corner region
(k2 soft or in the annulus, small q_y, q_z, so k1 = k2 + q sweeps through |k1| ~ 0) and along q_y / q_z.  NP = 8192."""
import numpy as np, lib1926 as R
import r1926_fourier as F0           # reuses G(); importing it runs its own report (kept in its .out), so silence it
L = R.L
NP = 8192
qs = -np.pi + 2*np.pi*(np.arange(NP) + 1)/NP
bands = [(64, 128), (256, 512), (1024, 2048), (2048, 4096)]
lines = [('k2 soft, q_yz small (k1 passes k = 0)', np.array([0.004, -0.003, 0.002]), (0, 0.003, -0.002)),
         ('k2 in annulus, line along q_y', np.array([0.03, 0.12, -0.05]), (1, 0.02, 0.01)),
         ('k2 hard, line along q_z', np.array([1.3, -2.2, 0.9]), (2, 1.1, -2.7))]
for tag in ('R19-16 ', 'REPLACED'):
    (R.unpatch if tag.startswith('R19') else R.patch)()
    for name, k2, (ax, o1, o2) in lines:
        vals = []
        for t in qs:
            q = np.empty(3); q[ax] = t; others = [i for i in range(3) if i != ax]; q[others[0]] = o1; q[others[1]] = o2
            vals.append(F0.G(q, k2, False))
        c = np.fft.fft(np.array(vals), axis=0)/NP; amp = np.abs(c).reshape(NP, -1).max(axis=1)
        print('[%s] %-40s: ' % (tag, name) + '; '.join('max|c_n| n in [%d,%d]: %.2e' % (a, b, max(amp[a:b + 1].max(), amp[NP - b:NP - a + 1].max())) for a, b in bands), flush=True)
