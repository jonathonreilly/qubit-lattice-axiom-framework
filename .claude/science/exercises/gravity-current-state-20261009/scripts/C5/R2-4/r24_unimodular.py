"""R2-4 check G2: does a local hard constraint tr h = 0 (linearised unimodular gravity, gauge group
reduced to transverse diffeos s.xi = 0) remove the negative direction of the Euclidean weight?
Same lattice symbol as r24_graviton_quotient.py. Quotient = (traceless h) / (transverse gauge range).
Also: lapse-like constraint check -- is the residual spin-0 direction positive, zero or negative?"""
import numpy as np
exec(open('r24_graviton_quotient.py').read().split("worst_gi, neg_quot")[0])  # reuse helpers
rng = np.random.default_rng(11)
res = []
for trial in range(300):
    k = rng.uniform(-np.pi, np.pi, 4); s = 2*np.sin(k/2); s2 = s @ s
    if s2 < 1e-6: continue
    K = Kform(s)
    trv = mat_to_vec(np.eye(4)); trv /= np.linalg.norm(trv)
    # traceless subspace basis
    Q, _ = np.linalg.qr(np.column_stack([trv, np.eye(10)]), mode='complete'); T = Q[:, 1:]   # 10x9 orthonormal, ⟂ trace
    # transverse gauge range: xi with s.xi = 0
    Qx, _ = np.linalg.qr(np.column_stack([s/np.sqrt(s2), np.eye(4)]), mode='complete'); Xi = Qx[:, 1:4]
    GT = np.array([mat_to_vec(np.outer(s, x) + np.outer(x, s)) for x in Xi.T]).T  # 10x3
    assert np.max(np.abs(trv @ GT)) < 1e-12
    GTt = T.T @ GT                                    # in traceless coords (9x3)
    Qg, _ = np.linalg.qr(GTt, mode='complete'); Gp = Qg[:, 3:]   # 9x6 quotient basis
    KT = T.T @ K @ T
    ev = np.linalg.eigvalsh(Gp.T @ KT @ Gp) / s2
    res.append(ev)
    if trial == 0:
        print("traceless + transverse-gauge quotient eigenvalues / s^2:", np.round(ev, 6))
        print("max |K_T G_T| =", np.max(np.abs(KT @ GTt)))
res = np.array(res)
print("over", len(res), "momenta: min eigenvalue / s^2 =", res.min().round(6),
      "; #negative per momentum (max) =", int((res < -1e-10).sum(1).max()),
      "; #zero per momentum (max) =", int((np.abs(res) < 1e-10).sum(1).max()))
