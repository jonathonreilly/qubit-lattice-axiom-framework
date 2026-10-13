"""R18-10 engine: R18-1's Metropolis (mc.py, rechecked) plus a dipole-conserving kinetic filter.
mode 0 (conserve): accept only if the signed per-type count change dN_ab = 0 for all 6 types (== dD(gamma) = 0, s1);
mode 1 (drive, preparation only): accept only if sum_ab |N_ab - half| does not increase; then Metropolis.
Proposals are symmetric involutive XOR flips; the filter is symmetric (dN -> -dN on the reverse move), so detailed
balance holds for exp(-bU sum gamma^2) restricted to the communicating class (A2)."""
import numpy as np, numba as nb
from mc import *
@nb.njit(cache=True)
def sweeps_c(n, g, Nc, L, bU, S, GE, GN, nsweep, seed, extra, mode, half, flipped):
    np.random.seed(seed)
    V = L*L*L; npat = S.shape[0]; acc = 0; tot = 0; filt = 0
    eidx = np.zeros((64, 4), dtype=np.int64); edel = np.zeros(64, dtype=np.int64); dN = np.zeros(6, dtype=np.int64)
    for m in range(npat*V*nsweep + extra):
        a = np.random.randint(npat); bx = np.random.randint(L); by = np.random.randint(L); bz = np.random.randint(L)
        ne = 0
        for t in range(6): dN[t] = 0
        for b in range(S.shape[1]):
            if S[a, b, 0] < 0: break
            sx = (bx + S[a, b, 0]) % L; sy = (by + S[a, b, 1]) % L; sz = (bz + S[a, b, 2]) % L; t = S[a, b, 3]
            dl = 1 - 2*n[t, sx, sy, sz]; dN[t] += dl
            for q in range(GN[t]):
                ex = (sx + GE[t, q, 0]) % L; ey = (sy + GE[t, q, 1]) % L; ez = (sz + GE[t, q, 2]) % L; j = GE[t, q, 3]
                found = -1
                for r in range(ne):
                    if eidx[r, 0] == ex and eidx[r, 1] == ey and eidx[r, 2] == ez and eidx[r, 3] == j:
                        found = r; break
                if found < 0:
                    eidx[ne, 0] = ex; eidx[ne, 1] = ey; eidx[ne, 2] = ez; eidx[ne, 3] = j; edel[ne] = 0; found = ne; ne += 1
                edel[found] += GE[t, q, 4]*dl
        tot += 1
        ok = True
        if mode == 0:
            for t in range(6):
                if dN[t] != 0: ok = False
        else:
            s0 = 0; s1 = 0
            for t in range(6):
                s0 += abs(Nc[t] - half); s1 += abs(Nc[t] + dN[t] - half)
            if s1 > s0: ok = False
        if not ok:
            continue
        filt += 1
        dE = 0.0
        for r in range(ne):
            g0 = g[eidx[r, 3], eidx[r, 0], eidx[r, 1], eidx[r, 2]]; g1 = g0 + edel[r]
            dE += (g1*g1 - g0*g0)/4.0
        if dE <= 0 or np.random.random() < np.exp(-bU*dE):
            acc += 1
            for b in range(S.shape[1]):
                if S[a, b, 0] < 0: break
                sx = (bx + S[a, b, 0]) % L; sy = (by + S[a, b, 1]) % L; sz = (bz + S[a, b, 2]) % L; t = S[a, b, 3]
                n[t, sx, sy, sz] ^= 1; flipped[t, sx, sy, sz] = 1
            for t in range(6): Nc[t] += dN[t]
            for r in range(ne):
                g[eidx[r, 3], eidx[r, 0], eidx[r, 1], eidx[r, 2]] += edel[r]
    return acc/max(tot, 1), filt/max(tot, 1)
def counts(n):
    return n.reshape(6, -1).sum(1).astype(np.int64)
