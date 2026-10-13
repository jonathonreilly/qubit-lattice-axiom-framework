"""R19-32 s6 (pre-registered 07:52Z): probe (d) static pull at finite d. Proved (report): fields decouple in Feynman gauge and
W H_T W^dag = H_L (W = diag(i^n) per T slot) maps a source J f_T to -iJ f_L, so the second-order ground-energy shift of a
static source t (component vector) is  dE = -chi_d * sum_A eta_A (R^T t)_A^2 J^2 = -chi_d (t.G.t) J^2, chi_d > 0.
Check numerically on one scalar field (L-site AP ring, truncated d, nu = 1): chi_d(x0,x0) from second-order PT and from
finite differences of the lowest eigenvalue for the eta=+1 field and the (non-Hermitian) eta=-1 field; CCR value G(0) =
(1/L) sum_k 1/(2 w_k) * 2/w_k ... = (1/L) sum_k 1/w_k^2 (static lattice Green function, field normalised as in mb)."""
import numpy as np, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from mb import *
import scipy.sparse.linalg as sla
for L in [3, 4]:
    ks = [(2*np.pi*j + np.pi)/L for j in range(L)]; Gccr = np.mean([1/(2*np.sin(k/2))**2 for k in ks])
    for d in [3, 4, 5, 6, 7, 8]:
        if d**L > 5000: continue
        out = []
        for etaA in [1, -1]:
            fld = [0] if etaA > 0 else [2]           # TT+ (eta +1) or v0x (eta -1): a single field on the ring
            S = Sector('TT', L, d, 1.0, -1, fields=fld)
            H = S.H.toarray(); f0 = S.f[S.slot(0, 0)].toarray()
            Es = []
            for J in [0, 1e-3, -1e-3]:
                ev = np.linalg.eigvals(H + J*f0); Es.append(ev[np.argmin(ev.real)].real)
            chi = -(Es[1] + Es[2] - 2*Es[0])/(2*1e-6)       # dE = -chi J^2
            out.append(chi)
        print(f"L={L} AP d={d}: chi_d(eta=+1) = {out[0]:.6f}, chi_d(eta=-1) = {out[1]:.6f} (expect -chi_+); CCR static G(0)/2 = {Gccr/2:.6f}")
