import sys, pickle, numpy as np
sys.path.insert(0, '.')
import rp_forms as RF
F = pickle.load(open('forms.pkl', 'rb'))
def build_consistent(F, k, m2):
    def Q(q):
        q = np.asarray(q, complex)
        K = F.d(k, -q).T @ F.M(k + 1, q) @ F.d(k, q) if k < 4 else 0
        return K + m2 * F.M(k, q)
    return Q
RF.build = build_consistent
for k in (0, 1):
    R = RF.rp_forms(F, k, 0.5, np.array([0.7, -0.3, 0.2]), 6, 0.0)
    w = np.linalg.eigvalsh(0.5*(R + R.conj().T)); print(f"control, consistent mass, degree {k}: min/max eig {w.min()/w.max():+.2e}")
