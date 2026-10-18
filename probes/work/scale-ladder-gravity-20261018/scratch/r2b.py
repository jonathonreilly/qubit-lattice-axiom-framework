import sys, pickle, numpy as np
sys.path.insert(0, '.')
import regge_generic as RG
from r2 import R2
OFF, S = RG.kuhn(); K = RG.Complex(OFF, S); D = pickle.load(open('d4.pkl', 'rb'))
def scan(C, ng, lam, ks, axis):
    """rank-drop roots of Q' at spatial ks: imaginary k_t = i w (real energies, w in (0,3)) or real k_t (tachyonic, in (0,3))."""
    vals = np.linspace(0.005, 3.0, 600); out = []
    def s_at(v):
        kt = 1j*v if axis == 'E' else v
        Q = C.Q(np.array([*ks, kt])) + lam*R2(C, np.array([*ks, kt])); s = np.sort(np.linalg.svd(Q, compute_uv=False)); return s[ng]/s[-1]
    f = np.array([s_at(v) for v in vals])
    for i in range(1, len(vals)-1):
        if f[i] < f[i-1] and f[i] < f[i+1] and f[i] < 1e-4: out.append(round(vals[i], 3))
    return out
ks = np.array([0.05, 0.0, 0.0])
for name, C, ng in (('Kuhn', K, 4), ('D4', D, 32)):
    for lam in (0.1, -0.1):
        print(f"{name} lambda={lam:+.1f}: real-energy roots w = {scan(C, ng, lam, ks, 'E')};  tachyonic (real k_t) roots = {scan(C, ng, lam, ks, 'T')}")
