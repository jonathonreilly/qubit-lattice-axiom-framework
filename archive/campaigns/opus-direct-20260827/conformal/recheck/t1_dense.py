"""T1 -- validate the Bloch reduction against a direct dense L^4 x L^4 assembly,
and check the flat stencil / lumped mass / zero deficit."""
import math, itertools
import numpy as np
from kuhn import build, bloch_eigs, _bands, dense_eigs, all_momenta, W

print("=== T1a  flat configuration: stencil, mass, deficits ===")
for L in (6, 8):
    r = build(L, 0.0, (0, 0, 0, 0), 2 * math.pi / L)
    st = r['stencil']
    ons = set(); nn = set(); other = {}
    for (x0, d0, d1, d2, d3), v in st.items():
        d = (d0, d1, d2, d3)
        if d == (0, 0, 0, 0):
            ons.add(round(v, 12))
        elif sum(abs(x) for x in d) == 1:
            nn.add(round(v, 12))
        elif abs(v) > 1e-12:
            other[(x0, d)] = v
    mx = max((abs(v) for k, v in st.items() if sum(abs(x) for x in k[1:]) > 1), default=0.0)
    print(f"  L={L}: on-site {sorted(ons)}  NN {sorted(nn)}  "
          f"non-NN couplings with |v|>1e-12: {len(other)}  max|non-NN| = {mx:.2e}")
    print(f"        lumped mass min/max = {r['mass'].min():.15f} / {r['mass'].max():.15f}"
          f"   Vol = {r['vol']:.10f} (L^4 = {L**4})   S_Regge = {r['S']:.3e}")

print()
print("=== T1b  Bloch vs dense assembly (all L^4 sites, no translation assumption) ===")
print("     L  eps   P               improved   max|dlambda|    spectrum range      herm")
for L in (4, 6):
    for eps, P in ((0.0, (0, 0, 0, 0)), (0.13, (0, 1, -1, 0)), (0.13, (1, 1, 1, 1)),
                   (0.13, (1.5, 0.8, -1.2, 0.9))):
        kk = 2 * math.pi / L
        r = build(L, eps, P, kk)
        bands = _bands(L, r['stencil'])
        qs = all_momenta(L)
        for improve, Cuse in ((False, None), (True, r['C'])):
            eb, herm = bloch_eigs(L, bands, r['mass'], qs, C=Cuse, improve=improve)
            eb = np.sort(eb.ravel())
            ed, M = dense_eigs(L, eps, P, kk, C=(r['C'] if improve else None), improve=improve)
            merr = float(np.max(np.abs(M.reshape(L, L ** 3)[:, 0] - r['mass'])))
            print(f"   {L:3d} {eps:5.2f} {str(P):16s} {str(improve):5s}    "
                  f"{np.max(np.abs(ed - eb)):.3e}   {ed.min():9.5f}..{ed.max():8.4f}   "
                  f"{herm:.1e}  mass {merr:.1e}")
