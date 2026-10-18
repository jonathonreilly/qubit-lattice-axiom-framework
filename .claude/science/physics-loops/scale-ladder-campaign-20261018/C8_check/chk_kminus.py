"""C8 check (d) supplement: true minimum cone speed at -k* of E+.S.L033 (E=-pi/4): flat direction or anisotropic?"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chk_screen.py')).read()
exec(src[:src.index("SAMPLE = []")])
from scipy.optimize import minimize
w = build(('E+', 'S', 'o'), ('L033',)); E = -np.pi / 4
W0 = W(w, -kst); e, V = np.linalg.eig(W0); sel = np.abs(wrap(np.angle(e) - E)) < 1e-6; Q, _ = np.linalg.qr(V[:, sel])
hj = []
for j in range(3):
    dk = np.zeros(3); dk[j] = 1e-6; G = (W(w, -kst + dk) - W(w, -kst - dk)) / 2e-6
    x = -1j * np.exp(-1j * E) * Q.conj().T @ G @ Q; hj.append((x + x.conj().T) / 2)
def smin(p):
    d = np.array([np.sin(p[0]) * np.cos(p[1]), np.sin(p[0]) * np.sin(p[1]), np.cos(p[0])])
    return np.abs(np.linalg.eigvalsh(sum(d[j] * hj[j] for j in range(3)))).min()
best = min((minimize(smin, s, method='Nelder-Mead', options={'xatol': 1e-12, 'fatol': 1e-14}) for s in np.random.default_rng(3).uniform(0, np.pi, (40, 2))), key=lambda r: r.fun)
d = best.x; print("multiplicity", int(sel.sum()), "min over directions of the smallest |speed|:", best.fun, "at theta,phi =", d)
print("eigen-speeds along that direction:", np.round(np.linalg.eigvalsh(sum(np.array([np.sin(d[0])*np.cos(d[1]), np.sin(d[0])*np.sin(d[1]), np.cos(d[0])])[j] * hj[j] for j in range(3))), 6))
print("along (1,1,1)/sqrt3 type axes:", [np.round(np.sort(np.abs(np.linalg.eigvalsh(sum(np.array(s)[j] / np.sqrt(3) * hj[j] for j in range(3))))), 4) for s in [(1,1,1),(1,-1,1),(-1,1,1),(1,1,-1)]])
