"""Brute-force (no pruning) cross-check of the C2z backtracking on random slices: fix site0 and the +-x pair, enumerate 64^3 rest."""
import sys, pickle, time, random, numpy as np
sys.path.insert(0, '/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C4')
from sitecore import *
W = '/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C4/'
t0 = time.time()
for mode in ('soldered', 'unsoldered'):
    SP, ROT, SG = tables(mode == 'soldered')
    found = set(pickle.load(open(W + 'fixed_%s_C2z_C2xy_C4z_C3.pkl' % mode, 'rb'))['C2z'])
    g = [r for r, R in enumerate(O) if (R == np.diag([-1, -1, 1])).all()][0]
    i0, ipx, imx, ipy, imy, ipz, imz = [PIDX[p] for p in [(0,0,0),(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]
    rng = random.Random(7)
    slices = [(0, 0), (1, 8)] + [(rng.randrange(64), rng.randrange(64)) for _ in range(6)]
    for c0, cx in slices:
        y, z1, z2 = np.meshgrid(np.arange(64), np.arange(64), np.arange(64), indexing='ij')
        S = np.zeros((64**3, 7), int)
        S[:, i0] = c0; S[:, ipx] = cx; S[:, imx] = ROT[g, cx]
        S[:, ipy] = y.ravel(); S[:, imy] = ROT[g][y.ravel()]; S[:, ipz] = z1.ravel(); S[:, imz] = z2.ravel()
        ok = np.ones(len(S), bool)
        for r in range(24):
            RS = np.zeros_like(S)
            for i in range(7): RS[:, SP[r, i]] = ROT[r][S[:, i]]
            for t, pr in OVL.items():
                p = np.zeros(len(S), np.uint8)
                for i, j in pr: p ^= COMM[S[:, i], RS[:, j]]
                ok &= (p == 0)
        bf = set(map(tuple, S[ok]))
        # require also fixedness (site0 / z sites fixed by g)
        bf = {s for s in bf if all(ROT[g, s[i]] == s[i] for i in (i0, ipz, imz))}
        sub = {s for s in found if s[i0] == c0 and s[ipx] == cx}
        print(mode, 'slice', (c0, cx), 'bruteforce', len(bf), 'backtracking', len(sub), bf == sub)
print('%.1fs' % (time.time() - t0))
