import sys, pickle, math, time, numpy as np, scipy.linalg as sl
sys.path.insert(0, '.')
import regge_generic as RG, whitney as WF
names = sys.argv[1:]
for nm in names:
    t0 = time.time(); C = pickle.load(open(f'canon_{nm}.pkl', 'rb')); F = WF.Forms(C)
    worst = {}
    for dname, n in {'axis': (1,0,0), 'gen': (3,1,2)}.items():
        n = np.array(n, float); n /= np.linalg.norm(n); km = 0.025
        for j in range(5):
            K, M = F.hodge(j, np.array([*(km*n), 1j*km])); w = np.sort(np.abs(sl.eigvals(K, M)))
            worst[(dname, j)] = w[math.comb(4, j)-1]/km**4
    mx = max(worst.values())
    print(f"canon {nm}: forms {F.n}; max over degrees/dirs of |lambda(omega=k)|/k^4 = {mx:.3e}  ({'no O(k^4) term' if mx < 1e-4 else 'O(k^4) splitting'})  [{time.time()-t0:.0f}s]", flush=True)
