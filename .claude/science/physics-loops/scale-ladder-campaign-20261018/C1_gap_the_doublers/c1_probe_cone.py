# probe: BdG cone at k* for the tuned on-site A2 pairing (B5b) -- isotropic? speed?
import sys
sys.argv = ['x', '8']
exec(open('c1_bdg_step.py').read().split("# ---------------- B1 ----------------")[0])
TAB = {nm: level(k, np.pi / 2) for nm, k in NODES.items()}
def singlet(Qm, Dm): return (Qm.conj().T @ Dm @ Qm.conj())[0, 1]
F = np.array([[singlet(TAB[nm], X) for X in VA2] for nm in ('k*', '-k*')])
_, s, Vh = np.linalg.svd(F); nullv = Vh[np.sum(s > 1e-9):]
for trial in range(3):
    c = nullv.T @ (rng.normal(size=len(nullv)) + 1j * rng.normal(size=len(nullv)))
    At = sum(ci * X for ci, X in zip(c, VA2)); At /= np.linalg.norm(At)
    for t in (0.1, 0.5):
        sp = []
        for _ in range(40):
            d = rng.normal(size=3); d /= np.linalg.norm(d); q = 1e-5
            ev = np.sort(np.abs(bdg_quasienergies(kst + q * d, lambda k: At, t)))[:4] / q; sp.append(ev)
        sp = np.array(sp); print(f"trial {trial} tau={t}: k* BdG cone speeds over 40 directions: min {sp.min():.6f} max {sp.max():.6f}  (v*={np.sqrt(2)/3:.6f})")
