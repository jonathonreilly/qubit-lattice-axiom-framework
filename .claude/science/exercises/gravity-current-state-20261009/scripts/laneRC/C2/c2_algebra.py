"""C2 step 1: exact operator algebra (infinite lattice) for [H, J_E] and the improvement search.
For each model: J = J_E^x density; report ||J||, ||[H,J]|| / (||H|| ||J||) (HS norms per cell), and
min over B in span(patch strings) of ||[H, J + i[H,B]]|| / ||[H,J]||.
"""
import sys, time
import numpy as np
from pauli_ti import energy_current, comm_density, norm2, patch_basis, improvement_search
import c2_models as M

models = [
    ("toric code (commuting projectors)", M.toric(), 2, [[(0,0),(1,0)], [(0,0),(0,1)]]),
    ("Xu-Moore plaquette Ising h=0 (commuting)", M.plaquette_ising(h=0.0), 1, [[(0,0),(1,0),(0,1),(1,1)]]),
    ("XX chains decoupled (1D free control)", M.xx_chains(), 1, [[(0,0),(1,0),(0,1),(1,1)], [(0,0),(1,0),(2,0)], [(0,0),(0,1),(0,2)]]),
    ("Kitaev honeycomb Jz=0 (decoupled chains)", M.kitaev(1.0, 1.0, 0.0), 2, [[(0,0),(1,-1)], [(0,0),(0,-1)], [(0,0),(1,0)]]),
    ("Kitaev honeycomb isotropic", M.kitaev(), 2, [[(0,0),(1,-1)], [(0,0),(0,-1)], [(0,0),(1,0)]]),
    ("Kitaev + field h=0.1 [111]", M.kitaev(hfield=0.1), 2, [[(0,0),(1,-1)], [(0,0),(0,-1)], [(0,0),(1,0)]]),
    ("toric code + hz=0.3 (mobile e)", M.toric(hz=0.3), 2, [[(0,0),(1,0)], [(0,0),(0,1)]]),
    ("2D TFIM h=3", M.tfim(3.0), 1, [[(0,0),(1,0),(0,1),(1,1)], [(0,0),(1,0),(2,0)], [(0,0),(0,1),(0,2)]]),
    ("2D XX (hard-core bosons)", M.xx2d(), 1, [[(0,0),(1,0),(0,1),(1,1)], [(0,0),(1,0),(2,0)], [(0,0),(0,1),(0,2)]]),
    ("2D compass", M.compass(), 1, [[(0,0),(1,0),(0,1),(1,1)], [(0,0),(1,0),(2,0)], [(0,0),(0,1),(0,2)]]),
    ("Xu-Moore plaquette Ising h=1", M.plaquette_ising(h=1.0), 1, [[(0,0),(1,0),(0,1),(1,1)], [(0,0),(1,0),(2,0)], [(0,0),(0,1),(0,2)]]),
]
only = sys.argv[1:]
for name, (lat, H), nsub, patches in models:
    if only and not any(o in name for o in only): continue
    t0 = time.time()
    J = energy_current(H, lat, comp=0)
    nJ = np.sqrt(norm2(J)); nH = np.sqrt(norm2(H))
    if nJ < 1e-12:
        print(f"{name:45s} J_E^x density = 0 identically (||J||={nJ:.1e})", flush=True); continue
    C = comm_density(H, J)
    rho = np.sqrt(norm2(C))/(nH*nJ)
    basis = set()
    for p in patches:
        basis |= set(patch_basis(p, nsub))
    basis = sorted(basis)
    nC, res, rank, nb = improvement_search(H, J, basis)
    print(f"{name:45s} |J|={nJ:.4f} terms(J)={len(J):4d}  ||[H,J]||/(||H||||J||)={rho:.4e}  "
          f"improvement: basis={nb} rank={rank} min||[H,J+i[H,B]]||/||[H,J]||={res/max(nC,1e-300):.4f}  ({time.time()-t0:.1f}s)", flush=True)
