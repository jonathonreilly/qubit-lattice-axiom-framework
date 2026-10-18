# probe: quasi-energy-pi behaviour at +-k* for the Wilson-type (B4) and tuned on-site (B5b) pairings
import sys
sys.argv = ['x', '8']
exec(open('c1_bdg_step.py').read().split("# ---------------- B1 ----------------")[0])
TAB = {nm: level(k, np.pi / 2) for nm, k in NODES.items()}
def singlet(Qm, Dm): return (Qm.conj().T @ Dm @ Qm.conj())[0, 1]
F = np.array([[singlet(TAB[nm], X) for X in VA2] for nm in ('k*', '-k*')])
_, s, Vh = np.linalg.svd(F); nullv = Vh[np.sum(s > 1e-9):]
c = nullv.T @ (rng.normal(size=len(nullv)) + 1j * rng.normal(size=len(nullv)))
At = sum(ci * X for ci, X in zip(c, VA2)); At /= np.linalg.norm(At)
for lab, Df in (("Wilson w(k)A", lambda k: wfun(k) * A2m), ("tuned on-site", lambda k: At)):
    print(lab, {nm: round(gappi(NODES[nm], Df, Q_R, 0.5), 5) for nm in NODES})
