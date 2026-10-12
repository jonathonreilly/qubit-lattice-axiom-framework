"""F2 part 2b: why the finite-|q| least-squares residual of the full system drops below the
1-jet residual: the best fit at small |q| ~ s uses coefficients that grow like 1/s (second-jet
terms of A and X promoted to O(s)); an exact solution must have s-independent coefficients.
Also: Tikhonov-bounded fits (||u|| <= const) recover the 1-jet floor."""
import numpy as np
import f2_full_system as F   # reuses builders (runs nothing heavy at import: guarded below)

def fit(G, b, lam=0.0):
    if lam == 0.0:
        u, *_ = np.linalg.lstsq(G, b, rcond=None)
    else:   # ridge: min ||Gu-b||^2 + lam^2 ||u||^2
        n = G.shape[1]
        Ga = np.vstack([G, lam * np.eye(n)]); ba = np.concatenate([b, np.zeros(n)])
        u, *_ = np.linalg.lstsq(Ga, ba, rcond=None)
    return np.linalg.norm(G @ u - b) / np.linalg.norm(b), np.linalg.norm(u)

print("== coefficient growth of the best small-|q| fit (K2 lattice, m2=1, rA=1, rX=1) ==")
for s_ in (0.3, 0.1, 0.03, 0.01):
    G, b = F.build_lattice(1.0, 1, 1, 400, small=s_)
    r0, n0 = fit(G, b)
    out = [f"s={s_:5.2f}: unconstrained rel.res={r0:.3f} ||u||={n0:9.2e}"]
    for lam in (1e-2, 1e-1):
        r1, n1 = fit(G, b, lam * s_)     # penalty relative to |b| ~ s
        out.append(f"ridge(lam={lam:g}) rel.res={r1:.3f} ||u||={n1:7.2f}")
    print("  " + " | ".join(out), flush=True)
print("1-jet floor (f2_jet_system.out, m2=1): 0.455")
