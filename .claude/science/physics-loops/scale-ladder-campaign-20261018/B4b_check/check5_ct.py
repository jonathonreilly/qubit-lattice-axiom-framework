import numpy as np
from indep_bubble import *
T = np.load('Tmeas_m0.7_N12.npy')
d = np.eye(4)
def symm(T):
    T = (T + T.transpose(1,0,2,3,4,5)) / 2; T = (T + T.transpose(0,1,3,2,4,5)) / 2
    T = (T + T.transpose(0,1,2,3,5,4)) / 2; return (T + T.transpose(2,3,0,1,4,5)) / 2
EH = symm(0.5*np.einsum('ac,bd,ef->abcdef', d,d,d) - np.einsum('ae,cf,bd->abcdef', d,d,d)
          + 0.5*(np.einsum('ab,ce,df->abcdef', d,d,d) + np.einsum('cd,ae,bf->abcdef', d,d,d))
          - 0.5*np.einsum('ab,cd,ef->abcdef', d,d,d))
a = np.vdot(EH.ravel(), T.ravel()) / np.vdot(EH.ravel(), EH.ravel())
CT = a*EH - T      # local nearest-neighbour two-graviton contact: S(K) = CT[khat,khat]
m, N = 0.7, 12
n = np.array([0.3, 0.8, -0.4, 0.33]); n /= np.linalg.norm(n)   # direction NOT used in the fit
P0 = bubble(np.zeros(4), N, m); ks = [0.4, 0.2, 0.1]; res = []
for kap in ks:
    K = kap*n; kh = khat(K)
    Pk = bubble(K, N, m) - P0; S = np.einsum('abcdef,e,f->abcd', CT, kh, kh)
    r1 = np.abs(ward(Pk, K)).max(); r2 = np.abs(ward(Pk + S, K)).max(); res.append((r1, r2))
    print("kappa %.2f  |k.(Pi-Pi0)|=%.3e   |k.(Pi-Pi0+S_K2)|=%.3e" % (kap, r1, r2))
print("powers:", [np.polyfit(np.log(ks), np.log([r[j] for r in res]), 1)[0] for j in (0, 1)])
