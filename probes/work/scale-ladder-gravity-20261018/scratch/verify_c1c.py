import sys, pickle, math, numpy as np, scipy.linalg as sl
sys.path.insert(0, '.')
import regge_generic as RG, whitney as WF
from d4f import golden
C = pickle.load(open('canon_1.pkl', 'rb')); F = WF.Forms(C)
for name, n in {'axis': (1,0,0), 'face': (1,1,0), 'body': (1,1,1), 'gen': (3,1,2)}.items():
    n = np.array(n, float); n /= np.linalg.norm(n); out = []
    for j in range(5):
        r = []
        for km in (0.05, 0.025):
            K, M = F.hodge(j, np.array([*(km*n), 1j*km])); w = np.sort(np.abs(sl.eigvals(K, M))); r.append(w[:math.comb(4, j)]/km**4)
        out.append(f"deg{j}: alpha_eff~{np.round(r[1], 3).tolist()}")
    print(name, "|lambda(omega=k)|/k^4 at |k|=0.025 (= |alpha| per component):", "; ".join(out))
ng = 4*len(C.types)
def svn(k):
    s_ = np.sort(np.linalg.svd(C.Q(k), compute_uv=False)); return s_/s_[-1]
for name, n in {'axis': (1,0,0), 'face': (1,1,0), 'body': (1,1,1), 'gen': (3,1,2)}.items():
    n = np.array(n, float); n /= np.linalg.norm(n); km = 0.05; ks = km*n; res = []
    for j in (0, 1):
        oms = km*np.linspace(0.996, 1.004, 161); f = [svn(np.array([*ks, 1j*o]))[ng+j] for o in oms]
        for i in range(1, 160):
            if f[i] < f[i-1] and f[i] < f[i+1] and f[i] < 1e-6:
                w = golden(lambda o: svn(np.array([*ks, 1j*o]))[ng+j], oms[i-1], oms[i+1]); res.append(round((w*w/km**2-1)/km**2, 4))
    print(f"graviton {name}: on-shell alphas {sorted(set(res))}")
