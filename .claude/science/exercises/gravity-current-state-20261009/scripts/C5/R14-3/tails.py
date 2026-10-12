"""Quasi-locality of the witnesses: 1D axis hopping kernel |eps_r| (Fourier coefficients of eps at m = 0.3, other
momenta 0), r = 32..512, against R14-1's G(1.4) and S(1.4)."""
import numpy as np, sys
sys.path.insert(0, '.')
from prof import *
exec(open('wit_b.py').read().split('for law in [W14, W08]:')[0].split('T0 = time.time()')[1])
n = 1 << 16; k = 2*np.pi*np.arange(n)/n
for law in [G_law(1.4), S_law(1.4), Law([1.0, 0.0], [1.4], [0.344371], 'G_w*(1.4) w=0.3444'), Law([1.0, 0.0, 1.0, 0.0], [1.4, 2.85, np.pi-0.05], [0.05, 0.05, 0.05], 'E2'), W08]:
    g, f, fp = law.gff(k); e = np.sqrt(0.09 + g); c = np.abs(np.fft.fft(e))/n
    print('%-28s |eps_r| r=32 %.1e  r=64 %.1e  r=128 %.1e  r=256 %.1e  r=512 %.1e' % (law.name[:28], c[32], c[64], c[128], c[256], c[512]))
