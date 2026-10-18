import sys, pickle, numpy as np
sys.path.insert(0, '.')
from rp_forms import rp_forms
F = pickle.load(open('forms.pkl', 'rb'))
for k in (0, 1):
    for t0 in (0.0, 0.5):
        res = []
        for ks in [np.array([0.0, 0.0, 0.0]), np.array([0.7, -0.3, 0.2]), np.array([1.9, 0.4, -1.1])]:
            R = rp_forms(F, k, 0.5, ks, 6, t0)
            herm = np.abs(R - R.conj().T).max()/np.abs(R).max()
            w = np.linalg.eigvalsh(0.5*(R + R.conj().T)); res.append((w.min()/w.max(), herm, R.shape[0]))
        print(f"degree {k} plane t0={t0}: min/max eig {min(r[0] for r in res):+.2e}; Hermiticity dev {max(r[1] for r in res):.0e}; size {res[0][2]}")
