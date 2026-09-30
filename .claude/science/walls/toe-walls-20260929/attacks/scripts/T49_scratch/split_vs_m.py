import sys, numpy as np
sys.argv = ['x', '8']
exec(open('massive_bdg.py').read().split('m = 0.3')[0])
val = all_invariants((1,1,1))[0]
Delta = np.zeros((N, N))
for (i, j), x in val.items(): Delta[i, j] = x; Delta[j, i] = -x
lam = 0.01
for m in [0.0, 0.05, 0.1, 0.3, 0.6]:
    hm = h + m * np.diag(eps)
    H = np.block([[hm, lam * Delta], [-lam * Delta, -hm]])
    E = np.linalg.eigvalsh(H)
    pos = np.sort(E[E > 1e-9])[:8]
    print(f"m={m:4.2f} lam={lam}: lowest positive BdG levels {np.round(pos,4)}   (m +- 8 lam = {m-8*lam:.3f}, {m+8*lam:.3f})")
