import sys, pickle, numpy as np
sys.path.insert(0, '.')
import regge_generic as RG
C = pickle.load(open('d4.pkl', 'rb'))
kd = np.array([0.3, -0.5, 0.6, 0.55]); kd /= np.linalg.norm(kd)
ev = {}
for s in (0.02, 0.01):
    Q = C.Q(s*kd); Q = 0.5*(Q + Q.conj().T)
    w = np.linalg.eigvalsh(Q); idx = np.argsort(np.abs(w)); ev[s] = w[idx]
a, b = ev[0.02], ev[0.01]
print("smallest |eigenvalues| (beyond the 32 gauge), with halving ratio:")
for i in range(32, 48):
    print(f"  #{i}: {a[i]:+.3e} -> {b[i]:+.3e}  ratio {a[i]/b[i]:.2f}")
