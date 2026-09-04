"""C1 -- flat Kuhn stencil, lumped mass, volume; and the offset inventory at eps != 0."""
import numpy as np
from collections import defaultdict
from kx_base import build, CH_P, N_MODE

L, n = 16, N_MODE
kk = 2 * np.pi * n / L

print("=== C1  flat Kuhn stencil / mass / volume  (L=%d) ===" % L)
r = build(L, 0.0, CH_P["CONFORMAL"], kk)
st = r['stencil']
axis = {}
diag_max = 0.0
diag_worst = None
self_c = []
for (x0, d0, d1, d2, d3), v in st.items():
    d = (d0, d1, d2, d3)
    nz = sum(1 for q in d if q != 0)
    if nz == 0:
        self_c.append(v)
    elif nz == 1:
        axis.setdefault(d, []).append(v)
    else:
        if abs(v) > diag_max:
            diag_max, diag_worst = abs(v), (x0, d)
print("  self coupling  K[x,x]      : min %.15f  max %.15f  (want 8)"
      % (min(self_c), max(self_c)))
av = np.array([v for vs in axis.values() for v in vs])
print("  axis couplings (8 dirs)    : min %.15f  max %.15f  (want -1)"
      % (av.min(), av.max()))
print("  n distinct axis offsets    : %d  (want 8)" % len(axis))
print("  max |non-axis coupling|    : %.3e   at %s   (want < 1e-12)"
      % (diag_max, diag_worst))
print("  lumped mass                : min %.15f  max %.15f  (want 1)"
      % (r['mass'].min(), r['mass'].max()))
print("  volume / L^4               : %.15f  (want 1)" % (r['vol'] / L ** 4))
print("  max |mass-1|               : %.3e" % np.max(np.abs(r['mass'] - 1.0)))
print("  max |K[x,x]-8|             : %.3e" % max(abs(v - 8) for v in self_c))
print("  max |axis+1|               : %.3e" % np.max(np.abs(av + 1)))

print("\n=== C1b  offset inventory at eps != 0 (does the stencil stay axis-only?) ===")
for name, P in CH_P.items():
    for eps in (0.05, 0.10):
        r = build(L, eps, P, kk)
        byoff = defaultdict(float)
        for (x0, d0, d1, d2, d3), v in r['stencil'].items():
            byoff[(d0, d1, d2, d3)] = max(byoff[(d0, d1, d2, d3)], abs(v))
        naxis = sum(1 for d in byoff if sum(1 for q in d if q != 0) == 1)
        nother = {d: v for d, v in byoff.items()
                  if sum(1 for q in d if q != 0) > 1 and v > 1e-14}
        mx = max(nother.values()) if nother else 0.0
        print(f"  {name:13s} eps={eps:.2f}: axis offsets {naxis:2d}, "
              f"non-axis offsets with |K|>1e-14: {len(nother):3d}, max |K| {mx:.3e}")
        print(f"                 mass  min {r['mass'].min():.8f} max {r['mass'].max():.8f}"
              f"   vol/L^4 {r['vol']/L**4:.10f}")
