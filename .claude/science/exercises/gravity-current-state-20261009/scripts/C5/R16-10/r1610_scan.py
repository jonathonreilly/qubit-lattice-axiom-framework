"""R16-10 scan: F_s(0+) = K_s + lattice part at m -> 0, lam = 0 (IR-excised split), over matter x photon laws.
Also prints the tadpole/seagull part (lattice) and the photon's axis v_max = max d'(q) and d(pi)."""
import numpy as np, sys, time
from r1610_eval import *
from r1610_laws import *
t0 = time.time()
N = int(sys.argv[1]) if len(sys.argv) > 1 else 64
def vmax_ph(d):
    q = np.linspace(0, np.pi, 20001); dd = np.gradient(d(q), q); return dd.max(), dd.min(), float(d(np.array(np.pi)))
photons = [('naive',), ('R85', 1.0, 2.0, 1.0), ('Gph', 0.6), ('Gph', 1.0), ('Gph', 1.4), ('Gph', 2.0), ('Gph', 2.6), ('Gph', 3.0),
           ('R85', 1.0, 2.0, 2.0), ('R85', 1.0, 2.0, 4.0), ('R85', 1.0, 2.0, 16.0)]
mats = [('D1', 1.4, 1/np.sqrt(3)), ('D1', 1.0, 1/np.sqrt(3)), ('lit', 2.0, 3.0), ('G', 1.4), ('G', 2.6), ('G', 0.6)]
for mat in mats:
    for ph in photons:
        d = photon(*ph)
        if ph[0] == 'naive':
            continue
        cbox = ph[1]
        bbox = mat[1]
        box = min(cbox, bbox)
        r1 = min(0.75*box, 0.9); r0 = 0.35*r1
        if mat[0] == 'G':
            spin = 0; matter = scalar_G(mat[1]); m = 0.0
        elif mat[0] == 'D1':
            spin = 0.5; matter = dirac_D1(mat[1], mat[2]); m = 1e-6
        else:
            spin = 0.5; matter = dirac_lit(mat[1], mat[2]); m = 1e-6
        lp, tp = lattice_part(spin, N, m, 0.0, matter, d, r0, r1, h=0.02)
        vmx, vmn, dpi = vmax_ph(d)
        print('%-22s ph=%-22s N=%d | F(0+) = K %+.4f + lattice %+9.4f = %+9.4f | [tad/seagull %+8.4f] | photon max d\' %.3f min d\' %+.3f d(pi) %.3f'
              % (str(mat), str(ph), N, K[spin], lp, K[spin] + lp, tp, vmx, vmn, dpi), flush=True)
print('elapsed %.1fs' % (time.time() - t0))
