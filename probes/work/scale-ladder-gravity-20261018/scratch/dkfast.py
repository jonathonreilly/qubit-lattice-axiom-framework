import sys, pickle, numpy as np, scipy.linalg as sl
sys.path.insert(0, '.')
F = pickle.load(open('forms.pkl', 'rb')); from math import comb
for name, n in {'axis': (1,0,0), 'gen': (3,1,2)}.items():
    n = np.array(n, float); n /= np.linalg.norm(n)
    for k in range(5):
        r = []
        for km in (0.05, 0.025):
            K, M = F.hodge(k, np.array([*(km*n), 1j*km])); w = np.sort(np.abs(sl.eigvals(K, M)))
            r.append((w[comb(4, k)-1]/km**2, w[comb(4, k)]/km**2))
        print(f"{name} degree {k}: largest of the C(4,k)={comb(4,k)} on-shell |lambda|/k^2: {r[0][0]:.2e} -> {r[1][0]:.2e} (ratio {r[0][0]/r[1][0]:.1f}); next {r[1][1]:.1e}")
