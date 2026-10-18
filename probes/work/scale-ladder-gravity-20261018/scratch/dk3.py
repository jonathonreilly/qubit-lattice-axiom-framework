import sys, pickle, numpy as np, scipy.linalg as sl
sys.path.insert(0, '.')
import regge_generic as RG, whitney as WF
from d4f import golden
F = pickle.load(open('forms.pkl', 'rb'))
def lam(k, p):
    K, M = F.hodge(k, p); w = sl.eigvals(K, M); return np.sort(np.abs(w))
for name, n in {'axis': (1,0,0), 'face': (1,1,0), 'body': (1,1,1), 'gen': (3,1,2)}.items():
    n = np.array(n, float); n /= np.linalg.norm(n); km = 0.05; ks = km*n
    row = []
    for k in range(5):
        oms = km*np.linspace(0.998, 1.002, 81); f = [lam(k, np.array([*ks, 1j*o]))[0] for o in oms]
        roots = []
        for j in range(3):   # track up to 3 lowest |lambda| minima for splitting
            g = [lam(k, np.array([*ks, 1j*o]))[j] for o in oms]
            for i in range(1, 80):
                if g[i] < g[i-1] and g[i] < g[i+1] and g[i] < 1e-6:
                    w = golden(lambda o: lam(k, np.array([*ks, 1j*o]))[j], oms[i-1], oms[i+1]); roots.append(round((w*w/km**2-1)/km**2, 4))
        row.append(sorted(set(roots)))
    print(f"{name}: alpha per degree 0..4: {row}")
