"""t9: degeneracy pattern of the eight bands at generic K."""
import numpy as np
from vcyc import layers_U, plain6, strang9
pi = np.pi
rng = np.random.default_rng(9)
def blk(a, phi): return [(a, 0, phi / 2), (a, 1, phi), (a, 0, phi / 2)]
def pal18(phi): return blk(0, phi) + blk(1, phi) + blk(2, phi) + blk(2, phi) + blk(1, phi) + blk(0, phi)
Ks = rng.uniform(-pi, pi, (2000, 3))
for name, lay, sg in [("plain-6", plain6(0.6), False), ("signed-6", plain6(0.6), True),
                      ("signed strang-9", strang9(0.6), True), ("signed palindrome-18", pal18(0.3), True),
                      ("plain palindrome-18", pal18(0.3), False)]:
    ph = np.sort(np.angle(np.linalg.eigvals(layers_U(Ks, lay, sg))), axis=1)
    d = np.diff(ph, axis=1)
    # count degenerate neighbours per K (gap < 1e-9)
    ndeg = (d < 1e-9).sum(1)
    vals, cnts = np.unique(ndeg, return_counts=True)
    print(f"{name}: #(adjacent degenerate pairs) per generic K -> {dict(zip(vals.tolist(), cnts.tolist()))}; "
          f"min adjacent gap over 2000 K = {d.min():.1e}")
