import sys, numpy as np
exec(open('verify_and_bdg.py').read().split('print("\\n== step 3')[0].replace('print(','(lambda *a,**k: None)('))
def spec(lam):
    H = np.block([[h, lam * Delta], [-lam * Delta, -h]])
    E = np.linalg.eigvalsh(H)
    return np.sort(np.abs(E))
for lam in [0.0, 0.05, 0.1, 0.2, 0.4, 0.8]:
    a = spec(lam)
    nz = int(np.sum(a < 1e-8))
    nxt = a[a >= 1e-8][:6]
    print(f"L={L} lam={lam:4.2f}: zero modes (of {len(a)}) = {nz}; first nonzero |E| = {np.round(nxt,4)}")
