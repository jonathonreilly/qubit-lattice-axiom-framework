"""R18-13: q = 0 TT pair weights of the UD Dirac field (dface conventions): P_e = <t0_e / E>, t0 = (Nc/2)(|G|^2 - (c.G)^2/E^2)
(the pair weight 2t at q = 0 over Ea + Eb = 2E). By Lemma O, UD own-direction smearings (u_d, u_o) would move the Dirac rows by
d face2 = (wo/2) P_T2g, d face1 = (wd/8)(4 P_Eg') + (wo/4) P_T2g with P_Eg' the Eg weight in the e:e-matched normalization (see report)."""
import os, sys, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'arch18'))
import dfam
from content3 import D1q
from dface import POL
bf, r, m = 0.9091029701, 0.5556036793, 0.01
law = D1q(bf, r); k, wq = dfam.gl_nodes(law.breaks(), 4, 10)
S, Sp, Spp, W, Wp, Wpp = law.tables(k); Nc = 4
res = {p: 0.0 for p in ('T2g', 'Eg', 'face1', 'face2')}
Sy, Spy, Wy, Wpy = (A[:, None] + 0*k[None, :] for A in (S, Sp, W, Wp)); Sz, Spz, Wz, Wpz = (A[None, :] + 0*k[:, None] for A in (S, Sp, W, Wp))
wyz = wq[:, None]*wq[None, :]
for ix in range(len(k)):
    M = m + W[ix] + Wy + Wz; c = [S[ix] + 0*M, Sy, Sz, M]; E2 = sum(x*x for x in c); E = np.sqrt(E2)
    s_ = [S[ix] + 0*M, Sy, Sz]; sp_ = [Sp[ix] + 0*M, Spy, Spz]; wp_ = [Wp[ix] + 0*M, Wpy, Wpz]
    p = [s_[d]*sp_[d] + M*wp_[d] for d in range(3)]
    for pol in res:
        e = POL[pol]; G = [0*M]*4
        for i in range(3):
            for j in range(3):
                if e[i, j] == 0: continue
                G[i] = G[i] + e[i, j]*0.5*p[j]*sp_[i]; G[3] = G[3] + e[i, j]*0.5*p[j]*wp_[i]
                G[j] = G[j] + e[i, j]*0.5*p[i]*sp_[j]; G[3] = G[3] + e[i, j]*0.5*p[i]*wp_[j]
        G2 = sum(a*a for a in G); g = sum(a*b for a, b in zip(c, G)); t0 = (Nc/2)*(G2 - g*g/E2)
        res[pol] += wq[ix]*float(np.sum(wyz*t0/E))
print('UD Dirac D1(%.6f, %.6f) m=%g per field, q=0 pair weights <t0/E>: ' % (bf, r, m) + ' '.join('%s %+.8e' % kv for kv in res.items()))
print('Schur: face1-(3Eg+T2g)/4 %+.2e  face2-T2g %+.2e' % (res['face1'] - (3*res['Eg'] + res['T2g'])/4, res['face2'] - res['T2g']))
