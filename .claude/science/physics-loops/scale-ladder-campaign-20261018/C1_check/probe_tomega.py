"""Probe: the T-omega pairing channel at +-k*: level shift, Bogoliubov surface, scaling with tau."""
import sys
from cklib import *
from scipy.optimize import minimize_scalar
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 5)
T = [g for g in PROPER if cls(OH[g]) in ('E', 'C2', 'C3')]
D2 = [g for g in PROPER if cls(OH[g]) in ('E', 'C2')]
c3 = [g for g in T if cls(OH[g]) == 'C3'][0]; w = np.exp(2j * np.pi / 3)
coset = {}
P = np.eye(3, dtype=int)
for m in range(3):
    for h in D2: coset[find_el(np.linalg.matrix_power(OH[c3], m) @ OH[h])] = m
chi = {g: w ** coset[g] for g in T}
assert all(abs(chi[find_el(OH[a] @ OH[b])] - chi[a] * chi[b]) < 1e-12 for a in T for b in T)
V = onsite_channel(chi, idx=T)
A = sum((rng.normal() + 1j * rng.normal()) * X for X in V); A /= np.linalg.norm(A)
assert all(np.allclose(UF[g] @ A @ UF[g].T, chi[g] * A) for g in T)
Don = lambda ks: np.broadcast_to(A, (len(np.atleast_2d(ks)), 12, 12)).copy()
DQ = {n: node_doublet(n) for n in NODES}
print("dim channel", len(V), " |m| at k*, -k*:", abs(singlet(DQ[(0,0,0)], 2*A)), abs(singlet(DQ[(1,1,1)], 2*A)))
for n in ((0,0,0),(1,1,1)):
    K = NODES[n]
    # couplings of node doublet to other levels
    for E, Qm in levels(K):
        if abs(wrap(E-np.pi/2)) < 1e-6: continue
        print(f"  {NAME[n]} node<->level E={E:+.3f} dim{Qm.shape[1]}: |block| = {np.abs(DQ[n].conj().T @ (2*A) @ Qm.conj()).max():.3e}")
    for tau in (0.05, 0.1, 0.2, 0.4):
        ev = np.sort(bdg_eps(K, Don, tau, QR)[0]); low = ev[np.argsort(np.abs(ev))[:4]]
        # per-direction zero search
        dirs = rng.normal(size=(40, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
        mins = []; rads = []
        for d in dirs:
            f = lambda r: gap0(K + r * d, Don, tau, QR)[0]
            rs = np.linspace(0, 0.4, 81); vals = gap0(K + rs[:, None] * d, Don, tau, QR); j = np.argmin(vals)
            res = minimize_scalar(f, bounds=(max(0, rs[j] - 0.01), rs[j] + 0.01), method='bounded', options=dict(xatol=1e-9))
            mins.append(res.fun); rads.append(res.x)
        mins = np.array(mins); rads = np.array(rads)
        print(f"  {NAME[n]} tau={tau}: 4 lowest |eps| at K = {np.round(np.abs(low), 6)}; per-direction min |eps|: "
              f"median {np.median(mins):.1e}, max {mins.max():.1e}; zero radius range [{rads[mins<1e-6].min() if (mins<1e-6).any() else np.nan:.4f}, "
              f"{rads[mins<1e-6].max() if (mins<1e-6).any() else np.nan:.4f}]; fraction of directions with a zero: {(mins<1e-6).mean():.2f}")
