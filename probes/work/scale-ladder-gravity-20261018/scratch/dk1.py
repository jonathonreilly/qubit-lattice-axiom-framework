import sys, pickle, time, numpy as np
sys.path.insert(0, '.')
import regge_generic as RG, whitney as WF
C = pickle.load(open('d4.pkl', 'rb'))
t0 = time.time(); F = WF.Forms(C); print("class counts per degree:", F.n, "Euler char per cell:", sum((-1)**k*F.n[k] for k in range(5)), f"{time.time()-t0:.1f}s")
q = np.array([0.31, -0.22, 0.17, 0.4])
print("d^2 = 0:", max(np.abs(F.d(k+1, q) @ F.d(k, q)).max() for k in range(3)))
# mass matrices: Hermitian PD and exact on constant forms? check M_0 total = volume: sum of M0 entries at q=0 = 1 (int 1*1)
print("sum M0(0) =", F.M(0, np.zeros(4)).sum().real, "(cell volume 1)")
for k in range(5):
    Mk = F.M(k, q); w = np.linalg.eigvalsh(0.5*(Mk + Mk.conj().T)); print(f"M_{k}: {F.n[k]}x{F.n[k]}, Hermitian dev {np.abs(Mk - Mk.conj().T).max():.0e}, min eig {w.min():.3e}")
pickle.dump(F, open('forms.pkl', 'wb'))
