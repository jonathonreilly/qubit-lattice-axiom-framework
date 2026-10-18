# representative-free test of a reading: full gauge-projected exchange on lattice-conserved sources -> alpha, beta, 1+gamma
import contextlib, io
with contextlib.redirect_stdout(io.StringIO()):
    from common import *
    from w2 import reading
def exch(k, L, Qi):
    K = L @ Qi @ L.conj().T; Cb = lattice_conserved(k, L); Ts = [T_of_c(c) for c in Cb]
    M = (Cb.conj() @ K @ Cb.T) * (k @ k)
    X = np.array([[np.sum(Ti.conj() * Tj), np.conj(np.trace(Ti)) * np.trace(Tj)] for Ti in Ts for Tj in Ts])
    coef = np.linalg.lstsq(X, M.ravel(), rcond=None)[0]
    return coef.real, np.linalg.norm(X @ coef - M.ravel()) / np.linalg.norm(M.ravel())
ks = {'static axis': np.array([0, 0.01, 0, 0]), 'generic': 0.01 * np.array([0.3, -0.5, 0.6, 0.55]) / np.linalg.norm([0.3, -0.5, 0.6, 0.55])}
Qis = {n: Qinv(k) for n, k in ks.items()}
for om in [(1, 1, 1), (1, 0.25, 1), (1, 4, 1), (1, 0, 1), (1, 1, 0.5), (1, 1, 2), (1, 4, 16), (1, 1, 0)]:
    row = []
    for n, k in ks.items():
        (a, b), res = exch(k, reading(k, om), Qis[n]); row.append(f"{n}: alpha {a:+.4f} beta {b:+.4f} 1+gamma {a/(a+b):.4f} (resid {res:.0e})")
    print(f"omega {str(om):14s}", " | ".join(row))
