import sys, pickle, numpy as np, scipy.linalg as sl
sys.path.insert(0, '.')
import regge_generic as RG, whitney as WF
F = pickle.load(open('forms.pkl', 'rb'))
kd = np.array([0.3, -0.5, 0.6, 0.55]); kd /= np.linalg.norm(kd)
for k in range(5):
    lam = {}
    for s in (0.02, 0.01):
        K, M = F.hodge(k, s*kd)
        w = np.sort(np.real(sl.eigvals(K, M))); lam[s] = w
    a, b = lam[0.02], lam[0.01]
    nsoft = int(sum((abs(b[i]) < 1e-2) for i in range(len(b))))
    ratio = a[:nsoft+2]/np.where(abs(b[:nsoft+2]) > 1e-300, b[:nsoft+2], 1)
    print(f"degree {k}: {F.n[k]} classes; soft eigenvalues (|lambda|<1e-2 at |k|=0.01): {nsoft}; lambda/k^2 = {np.round(b[:nsoft]/1e-4, 4)}; halving ratios {np.round(ratio[:nsoft], 3)}; next {b[nsoft]:.3f}")
