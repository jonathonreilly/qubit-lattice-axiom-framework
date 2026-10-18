"""C8 check (d) supplement: for every C8 survivor whose -k* level is recorded 8-fold 'aniso', compute the true minimum
linear-order speed over all directions (C8 and the B26-check classifier sample 43/60 directions only)."""
import os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chk_screen.py')).read()
exec(src[:src.index("SAMPLE = []")])
from scipy.optimize import minimize
def hmat(w, k0, E):
    W0 = W(w, k0); e, V = np.linalg.eig(W0); sel = np.abs(wrap(np.angle(e) - E)) < 1e-6; Q, _ = np.linalg.qr(V[:, sel]); hj = []
    for j in range(3):
        dk = np.zeros(3); dk[j] = 1e-6; G = (W(w, k0 + dk) - W(w, k0 - dk)) / 2e-6
        x = -1j * np.exp(-1j * E) * Q.conj().T @ G @ Q; hj.append((x + x.conj().T) / 2)
    return int(sel.sum()), hj
def true_smin(hj, rg):
    def f(p):
        d = np.array([np.sin(p[0]) * np.cos(p[1]), np.sin(p[0]) * np.sin(p[1]), np.cos(p[0])])
        return np.abs(np.linalg.eigvalsh(sum(d[j] * hj[j] for j in range(3)))).min()
    return min(minimize(f, s, method='Nelder-Mead', options={'xatol': 1e-12, 'fatol': 1e-14}).fun for s in rg.uniform(0, np.pi, (12, 2)))
rg = np.random.default_rng(5); cnt = collections.Counter(); n = 0
for pk in PK:
    for r in load(os.path.join(D, pk))['recs']:
        if r['fermi']: continue
        for x in r['nodes']:
            if np.allclose(np.array(x[0], float), -kst / np.pi, atol=1e-4) and x[2] == 8 and x[3] == 'aniso':
                w = build(r['sk'], r['names']); m, hj = hmat(w, -kst, r['E']); s = true_smin(hj, rg)
                cnt[('flat direction' if s < 1e-8 else 'anisotropic, no flat direction', m)] += 1; n += 1
print(f"survivors with an 8-fold 'aniso' -k* level: {n}; true classification: {dict(cnt)}")
