import numpy as np, sys
sys.path.insert(0, '.')
from rge import *
print("TEST A: SM-extrapolated couplings at M_Pl (SM content only, no tastes)")
for loops in (1, 2):
    y = up_from_mz(MPL, loops)
    o = observables(y)
    inv = {k: 4*PI/o[k] for k in ('g32', 'g22', 'gp2')}
    g2s = np.array([o['g32'], o['g22'], o['gp2']])
    spread = (g2s.max()-g2s.min())/g2s.mean()
    print(f"loops={loops}: g3^2={o['g32']:.4f} (1/a3={inv['g32']:.2f})  g2^2={o['g22']:.4f} (1/a2={inv['g22']:.2f})  gY^2={o['gp2']:.4f} (1/aY={inv['gp2']:.2f})"
          f"  sin^2(M_Pl)={o['s2']:.4f}  1/aem(M_Pl)={o['aem_inv']:.2f}  spread={spread:.3f}  yt(MPl)={y[3]:.3f}")
    print("   nearest 1/n: g3^2->1/%.2f  g2^2->1/%.2f  gY^2->1/%.2f" % (1/o['g32'], 1/o['g22'], 1/o['gp2']))
# observed at v
for loops in (1, 2):
    o = observables(up_from_mz(V, loops))
    print(f"observed-run couplings at v: loops={loops}: g3={np.sqrt(o['g32']):.4f} g2={np.sqrt(o['g22']):.4f} g'={np.sqrt(o['gp2']):.4f}  a_s(v)={o['g32']/(4*PI):.4f}")
# what the lane's numbers are
print("lane values at lattice scale: g3^2=1, g2^2=1/4, gY^2=1/5; ratio to SM-extrapolated (2-loop): ")
o = observables(up_from_mz(MPL, 2))
print("   g3^2: %.2fx   g2^2: %.3fx   gY^2: %.3fx" % (1/o['g32'], 0.25/o['g22'], 0.2/o['gp2']))
print("beta_lat = 2Nc/g^2 needed for SU(3) if g3^2=%.3f: %.1f" % (o['g32'], 6/o['g32']))
