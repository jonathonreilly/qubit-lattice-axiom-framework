"""T2 -- validate the improvement against the EXACT flat-torus heat trace
K_exact(s) = (4 pi s)^-2 Vol sum_{w in Z^4} exp(-|w|_g^2 L^2 / (4 s)).
The flat torus has no higher heat coefficients, so every deviation is lattice error.
Also: uniform (constant) diagonal metrics, where c = tr g/96 must beat c = 1/24."""
import math, itertools
import numpy as np
from kuhn import (build, _bands, bloch_eigs, all_momenta,
                  flat_lattice_trace, flat_exact_trace)

SV = [1, 2, 3, 4, 6, 8, 10, 16, 25, 40, 64]

print("=== T2a  unit flat torus: lattice trace vs winding sum ===")
for L in (32, 64):
    ex = flat_exact_trace(L, SV)
    pl = flat_lattice_trace(L, SV, improve=False)
    im = flat_lattice_trace(L, SV, improve=True)
    print(f"  L = {L}")
    print("      s     plain rel.err   improved rel.err")
    for s, a, b, c in zip(SV, ex, pl, im):
        print(f"   {s:6.1f}    {b/a-1:+11.3e}     {c/a-1:+11.3e}")

print()
print("=== T2b  CONSTANT diagonal metrics (exactly flat, tr g != 4): c=1/24 vs c=tr g/96 ===")
print("    metric                tr g      s      err(c=1/24)   err(c=trg/96)")
for f in ([1.4, 1.4, 1.4, 1.4], [0.6, 0.6, 0.6, 0.6], [1.5, 0.8, 1.2, 0.9]):
    f = np.array(f)
    L = 32
    ex = flat_exact_trace(L, SV, f=f)
    d1 = 2.0 * (1.0 - np.cos(2 * np.pi * np.arange(L) / L))
    D = sum(d1.reshape([-1 if i == m else 1 for i in range(4)]) / f[m] for m in range(4))
    for cname, cval in (("1/24", 1.0 / 24.0), ("trg/96", float(f.sum()) / 96.0)):
        pass
    for j, s in enumerate(SV):
        e24 = float(np.exp(-s * (D + D * D / 24.0)).sum()) / ex[j] - 1
        etr = float(np.exp(-s * (D + D * D * float(f.sum()) / 96.0)).sum()) / ex[j] - 1
        if s in (4, 8, 16, 25):
            print(f"    {str(list(f)):22s} {f.sum():5.2f} {s:6.1f}   {e24:+11.3e}    {etr:+11.3e}")

print()
print("=== T2c  pipeline check: constant conformal metric through build()+bloch ===")
# g = (1+e) delta everywhere: exactly flat, Vol = (1+e)^2 L^4, S_Regge = 0.
for L in (8, 16):
    for e in (0.0, 0.10):
        r = build(L, e, (1, 1, 1, 1), 0.0)             # kk = 0 -> constant metric
        bands = _bands(L, r['stencil'])
        ev, herm = bloch_eigs(L, bands, r['mass'], all_momenta(L), C=r['C'], improve=True)
        ev = np.sort(ev.ravel())
        f = np.full(4, 1.0 + e)
        ref = flat_lattice_trace(L, SV, improve=True, f=f)
        ex = flat_exact_trace(L, SV, f=f)
        tr = np.array([float(np.exp(-s * ev).sum()) for s in SV])
        print(f"  L={L} eps={e:.2f}: Vol={r['vol']:.6f} (exact {(1+e)**2*L**4:.6f})  "
              f"S_Regge={r['S']:.2e}  C={r['C'][0]:.4f} (tr g/4 = {1+e:.4f})")
        print(f"        max rel |pipeline - uniform-symbol| over s: "
              f"{np.max(np.abs(tr/ref-1)):.2e}    rel err vs exact torus at s=8/16/25: "
              f"{tr[SV.index(8)]/ex[SV.index(8)]-1:+.2e} "
              f"{tr[SV.index(16)]/ex[SV.index(16)]-1:+.2e} "
              f"{tr[SV.index(25)]/ex[SV.index(25)]-1:+.2e}")
