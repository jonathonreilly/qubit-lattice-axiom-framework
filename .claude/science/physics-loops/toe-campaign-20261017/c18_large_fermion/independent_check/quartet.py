"""Outside the claimed sign sector: t1 = +1 with triangle 0 (equivalently t1 = -1, triangle pi).
The band minimum is 4-fold; identify its 2O irrep at k* via the Bloch sewing matrices."""
import numpy as np, io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import irrep as IR          # my own 2O helpers (prints suppressed)
from model import *
u = solve_gauge(dict(square=1, triangle=0, plaquette=1, tube=1))
PS = [(R, *psg(u, R)) for R in ROTS]
chiG = np.array([8 * q[0]**3 - 4 * q[0] for q in IR.Q])
IR.IRR['G3/2'] = chiG
KP = np.array([1, -1, 1]) * np.pi / 2
for t1, t2, lam in ((1.0, 0.1, -0.5), (1.0, 0.3, 0.5), (-1.0, 0.1, -0.5)):
    best = None
    for k in (KP, -KP):
        ev, V = np.linalg.eigh(bloch(u, k, t1, t2, lam))
        if best is None or ev[0] < best[0][0]: best = (ev, V, k)
    ev, V, k = best; m = int(np.sum(ev - ev[0] < 1e-8)); P = V[:, :m]
    D = [(1j ** w1(R)) * (P.conj().T @ Wmat(R, eta) @ P) for R, eta, s in PS]
    # check D is a (projective) rep on this subspace: W maps the k-eigenspace into itself
    inv = max(np.linalg.norm(Wmat(R, eta) @ P - P @ (P.conj().T @ Wmat(R, eta) @ P)) for R, eta, s in PS)
    print(f"t1={t1:+} tri=0 t2={t2} lam={lam}: min at {np.round(k/(np.pi/2)).astype(int)}, deg {m}, invariance {inv:.0e}, lifts ->",
          [(sg, {a: b for a, b in IR.label(ch).items() if abs(b) > 1e-6}) for sg, ch in IR.lifts(D)])
