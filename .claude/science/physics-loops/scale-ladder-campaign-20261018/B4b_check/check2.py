import time, numpy as np
from indep_bubble import *
m = 0.7; N = 12
n = np.array([1.0, 0.37, 0.61, -0.23]); n /= np.linalg.norm(n)
P0 = bubble(np.zeros(4), N, m)
print("|khat.Pi(0)| trivially 0; Pi(0) max", np.abs(P0).max())
rows = []
for kap in (0.4, 0.2, 0.1, 0.05):
    K = kap * n; Pk = bubble(K, N, m)
    e = tt_pol(K)
    S = abs(np.einsum('ab,abcd,cd->', e, Pk - P0, e))
    r0 = np.abs(ward(Pk, K)).max(); r1 = np.abs(ward(Pk - P0, K)).max()
    rows.append((kap, r0, r1, S, Pk))
    print("kappa %.3f  |k.Pi|=%.3e  |k.(Pi-Pi0)|=%.3e  TT signal=%.3e  ratio r1/(|khat|*maxsym)=%.3f" %
          (kap, r0, r1, S, r1 / (np.linalg.norm(khat(K)) * np.abs(Pk - P0).max())), flush=True)
ks = np.array([r[0] for r in rows])
for j, lab in ((1, 'unsubtracted'), (2, 'Pi(0)-subtracted')):
    print(lab, "power (last 3):", np.polyfit(np.log(ks[1:]), np.log([r[j] for r in rows][1:]), 1)[0])
# leading symbol via Richardson along n
M_a = (rows[2][4] - P0) / 0.1**2; M_b = (rows[3][4] - P0) / 0.05**2
M2 = (4 * M_b - M_a) / 3
wr = np.abs(np.einsum('m,mnrs->nrs', n, M2)).max() / np.abs(M2).max()
print("symbol-level Ward ratio max|n.M2|/max|M2| along n = %.4f" % wr)
np.save('M2_n.npy', M2)
