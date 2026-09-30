"""T70 test 3: entropy per plaquette of the same lattice scalar across a plane (normal z), by
(i) corner-transfer-matrix formula per transverse mode (checked against finite-chain correlation-matrix entropy),
(ii) comparison with the induced G: Jacobson/Susskind-Uglum relation would be  1/(4 c_ent) = G_ind.
Model: H = sum 1/2 pi^2 + 1/2 (grad phi)^2 + 1/2 m^2 phi^2 on Z^3, flat metric; z-chain per transverse momentum has
mu^2 = m^2 + (2-2cos qx) + (2-2cos qy)."""
import numpy as np, math, sys
from scipy.special import ellipk

def S_ctm(mu2):
    alpha = 1 + mu2/2.0
    k = alpha - math.sqrt(alpha*alpha - 1.0)      # nome parameter xi (checked against the finite chain)
    kp = math.sqrt(1-k*k)
    eps = math.pi*ellipk(kp*kp)/ellipk(k*k)
    j = np.arange(0, 4000)
    e = np.minimum((2*j+1)*eps, 700.0)
    return float(np.sum(e/np.expm1(e) - np.log1p(-np.exp(-e))))

def S_chain(mu2, L=400):
    V = np.diag(np.full(L, 2+mu2)) - np.diag(np.ones(L-1), 1) - np.diag(np.ones(L-1), -1)
    w, U = np.linalg.eigh(V)
    Vh = (U*np.sqrt(w))@U.T; Vmh = (U/np.sqrt(w))@U.T
    X = 0.5*Vmh; P = 0.5*Vh
    A = slice(0, L//2)
    nu2 = np.linalg.eigvals(X[A, A]@P[A, A]).real
    nu = np.sqrt(np.clip(nu2, 0.25+1e-15, None))
    return float(np.sum((nu+0.5)*np.log(nu+0.5) - (nu-0.5)*np.log(nu-0.5)))

if __name__ == "__main__":
    out = []
    P = lambda *a: (print(*a), out.append(" ".join(str(x) for x in a)))
    P("check CTM formula against finite-chain correlation-matrix entropy (single cut):")
    for mu2 in (0.05, 0.25, 1.0, 4.0):
        P(f"  mu^2={mu2}: CTM={S_ctm(mu2):.6f}  chain(L=400)={S_chain(mu2):.6f}")
    Nt = 400
    q = 2*np.pi*(np.arange(Nt)+0.5)/Nt
    ax = 2-2*np.cos(q)
    for m in (0.0, 0.25, 0.5, 1.0):
        s = 0.0
        # use symmetry: sum over grid
        MU2 = (m*m + ax[:, None] + ax[None, :]).ravel()
        vals = np.array([S_ctm(x) for x in np.unique(np.round(MU2, 12))])
        # map back
        uniq, inv = np.unique(np.round(MU2, 12), return_inverse=True)
        c = float(np.mean(vals[inv]))
        P(f"m={m}: c_ent (entropy per plaquette, plane cut normal to z) = {c:.5f}   G_ent = 1/(4 c) = {1/(4*c):.3f}")
    open("test3_output.txt", "w").write("\n".join(out) + "\n")
