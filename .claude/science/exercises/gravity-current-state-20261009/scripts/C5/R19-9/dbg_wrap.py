import numpy as np, lib199 as L
rng = np.random.default_rng(3)
for l in range(3):
    k1 = rng.uniform(-np.pi, np.pi, 3); k1[l] = np.pi - 1e-7; k2 = rng.uniform(-np.pi, np.pi, 3)
    k1b = k1.copy(); k1b[l] = -np.pi + 1e-7
    T = np.ones(6); T[l] = -1; T[3:] = -1; T[3+l] = 1
    Sa = L.spatial_VW(k1, k2); Sb = L.spatial_VW(k1b, k2)
    print('l', l, 'spatial VW jump', np.abs(Sa - np.einsum('a,ijab->ijab', T, Sb)).max())
    ha = L.hmat(L.sig(k1)); hb = L.hmat(L.sig(k1b)); print('  h covariance', np.abs(ha - np.diag(T) @ hb @ np.diag(T)).max())
    print('  c(k1_l)', L.cfun(k1)[l], 'sig', L.sig(k1)[l], L.sig(k1b)[l])
    for i in range(3):
        for j in range(3):
            dE = np.abs(Sa[i,j,:3,:3] - np.einsum('a,ab->ab', T[:3], Sb[i,j,:3,:3])).max(); dB = np.abs(Sa[i,j,3:,3:] - np.einsum('a,ab->ab', T[3:], Sb[i,j,3:,3:])).max()
            if max(dE, dB) > 1e-6: print('   comp', i, j, 'dE %.2e dB %.2e' % (dE, dB)); print(Sa[i,j,3:,3:]); print(Sb[i,j,3:,3:])
