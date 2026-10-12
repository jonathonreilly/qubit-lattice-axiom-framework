"""C2 controls: (1) stacked interacting XXZ chains on Z^2 (x-bonds only, Delta=0.5): J^x conserved exactly (integrable,
Zotos-Naef-Prelovsek), J^y = 0 identically -- validates the algebra on an interacting integrable case and is the
non-covariant 'PASS-shaped' degenerate example; (2) same chains plus a weak vertical XXZ coupling g: [H,J] != 0;
(3) stacked chains with next-nearest-neighbour term (non-integrable 1D control)."""
import numpy as np
from pauli_ti import energy_current, comm_density, norm2, patch_basis, improvement_search
import c2_models as M
from c2_models import dens, SQ, X, Y, Z
def xxz_stack(Delta=0.5, g=0.0, nnn=0.0):
    t = []
    for p, c in [(X, 1.0), (Y, 1.0), (Z, Delta)]:
        t.append((c, [((0,0,0),p), ((1,0,0),p)]))
        if g: t.append((g*c, [((0,0,0),p), ((0,1,0),p)]))
        if nnn: t.append((nnn*c, [((0,0,0),p), ((2,0,0),p)]))
    return SQ, dens(t)
for name, (lat, H) in [("stacked XXZ chains D=0.5", xxz_stack()), ("stacked XXZ + vertical g=0.2", xxz_stack(g=0.2)),
                       ("stacked XXZ + NNN 0.3 (1D nonintegrable)", xxz_stack(nnn=0.3))]:
    for comp in (0, 1):
        J = energy_current(H, lat, comp=comp)
        if norm2(J) < 1e-20:
            print(f"{name:42s} J^{'xy'[comp]} = 0 identically"); continue
        C = comm_density(H, J)
        print(f"{name:42s} J^{'xy'[comp]}: |J|={np.sqrt(norm2(J)):.4f}  ||[H,J]||/(||H||||J||) = {np.sqrt(norm2(C)/(norm2(H)*norm2(J))):.3e}")
