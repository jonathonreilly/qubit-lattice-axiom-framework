"""R18-10 canonical-sector SAMPLER (not the registered local dynamics): proposals are either one local pattern flip
or a pair of pattern flips at two independent uniformly random positions; accept only if the combined per-type count
change is zero (total gamma-dipole conserved, N_ab fixed) and then Metropolis on the combined dE. Symmetric involutive
proposals + symmetric filter => detailed balance for exp(-bU sum gamma^2) restricted to the N-sector class reached.
Its communicating class contains the local chain's class (single balanced flips are included)."""
import numpy as np, numba as nb
from mc import *
@nb.njit(cache=True)
def flip(n, g, L, S, GE, GN, a, bx, by, bz, dN):
    """apply XOR flip of pattern a at (bx,by,bz) to n and g in place; add signed per-type changes to dN; return dE"""
    dE = 0.0
    for b in range(S.shape[1]):
        if S[a, b, 0] < 0: break
        sx = (bx + S[a, b, 0]) % L; sy = (by + S[a, b, 1]) % L; sz = (bz + S[a, b, 2]) % L; t = S[a, b, 3]
        dl = 1 - 2*n[t, sx, sy, sz]; dN[t] += dl; n[t, sx, sy, sz] ^= 1
        for q in range(GN[t]):
            ex = (sx + GE[t, q, 0]) % L; ey = (sy + GE[t, q, 1]) % L; ez = (sz + GE[t, q, 2]) % L; j = GE[t, q, 3]
            g0 = g[j, ex, ey, ez]; g1 = g0 + GE[t, q, 4]*dl
            dE += (g1*g1 - g0*g0)/4.0; g[j, ex, ey, ez] = g1
    return dE
@nb.njit(cache=True)
def sweeps_pair(n, g, L, bU, S, GE, GN, nsweep, seed, extra):
    np.random.seed(seed)
    V = L*L*L; npat = S.shape[0]; acc = 0; tot = 0; dN = np.zeros(6, dtype=np.int64); dummy = np.zeros(6, dtype=np.int64)
    for m in range(npat*V*nsweep + extra):
        for t in range(6): dN[t] = 0
        a1 = np.random.randint(npat); x1 = np.random.randint(L); y1 = np.random.randint(L); z1 = np.random.randint(L)
        pair = np.random.random() < 0.5
        dE = flip(n, g, L, S, GE, GN, a1, x1, y1, z1, dN)
        if pair:
            a2 = np.random.randint(npat); x2 = np.random.randint(L); y2 = np.random.randint(L); z2 = np.random.randint(L)
            dE += flip(n, g, L, S, GE, GN, a2, x2, y2, z2, dN)
        ok = True
        for t in range(6):
            if dN[t] != 0: ok = False
        tot += 1
        if ok and (dE <= 0 or np.random.random() < np.exp(-bU*dE)):
            acc += 1
        else:
            if pair: flip(n, g, L, S, GE, GN, a2, x2, y2, z2, dummy)
            flip(n, g, L, S, GE, GN, a1, x1, y1, z1, dummy)
    return acc/max(tot, 1)
@nb.njit(cache=True)
def sweeps_bias(n, g, Nc, L, bU, lam, half, S, GE, GN, nsweep, seed, extra):
    """GC chain (R18-1 moves) with weight exp(-bU sum gamma^2 - lam sum_ab (N_ab - half)^2). The bias depends on N only,
    so conditioning its samples on N = half (all six) gives EXACTLY the canonical restricted Boltzmann measure on the
    N-sector of the trivial coset (exact canonical sampler; mixing as the GC chain)."""
    np.random.seed(seed)
    V = L*L*L; npat = S.shape[0]; acc = 0; tot = 0; dN = np.zeros(6, dtype=np.int64); dummy = np.zeros(6, dtype=np.int64)
    for m in range(npat*V*nsweep + extra):
        for t in range(6): dN[t] = 0
        a1 = np.random.randint(npat); x1 = np.random.randint(L); y1 = np.random.randint(L); z1 = np.random.randint(L)
        dE = flip(n, g, L, S, GE, GN, a1, x1, y1, z1, dN)
        db = 0.0
        for t in range(6):
            db += (Nc[t] + dN[t] - half)**2 - (Nc[t] - half)**2
        w = bU*dE + lam*db; tot += 1
        if w <= 0 or np.random.random() < np.exp(-w):
            acc += 1
            for t in range(6): Nc[t] += dN[t]
        else:
            flip(n, g, L, S, GE, GN, a1, x1, y1, z1, dummy)
    return acc/max(tot, 1)
@nb.njit(cache=True)
def drive_planar(n, g, L, bU, S, GE, GN, nsweep, seed, extra):
    """preparation only: GC moves accepted only if the objective sum_a sum_planes |N_aa(plane) - L^2/2| + sum_faces |N_ab - L^3/2|
    does not increase (then Metropolis at bU). Returns the final objective."""
    np.random.seed(seed); V = L*L*L; npat = S.shape[0]; dN = np.zeros(6, dtype=np.int64); dum = np.zeros(6, dtype=np.int64)
    P = np.zeros((3, L), dtype=np.int64); Nf = np.zeros(3, dtype=np.int64)
    for a in range(3):
        for x in range(L):
            for y in range(L):
                for z in range(L):
                    c = (x, y, z)[a]; P[a, c] += n[a, x, y, z]
        Nf[a] = n[3 + a].sum()
    h2 = L*L//2; h3 = V//2
    def_obj = 0
    for a in range(3):
        def_obj += abs(Nf[a] - h3)
        for c in range(L): def_obj += abs(P[a, c] - h2)
    obj = def_obj
    P2 = P.copy()
    for m in range(npat*V*nsweep + extra):
        a1 = np.random.randint(npat); x1 = np.random.randint(L); y1 = np.random.randint(L); z1 = np.random.randint(L)
        # planar changes of diagonal slots
        for a in range(3):
            for c in range(L): P2[a, c] = P[a, c]
        for b in range(S.shape[1]):
            if S[a1, b, 0] < 0: break
            t = S[a1, b, 3]
            if t < 3:
                sx = (x1 + S[a1, b, 0]) % L; sy = (y1 + S[a1, b, 1]) % L; sz = (z1 + S[a1, b, 2]) % L
                c = sx if t == 0 else (sy if t == 1 else sz)
                P2[t, c] += 1 - 2*n[t, sx, sy, sz]
        for t in range(6): dN[t] = 0
        dE = flip(n, g, L, S, GE, GN, a1, x1, y1, z1, dN)
        new = 0
        for a in range(3):
            new += abs(Nf[a] + dN[3 + a] - h3)
            for c in range(L): new += abs(P2[a, c] - h2)
        if new <= obj and (dE <= 0 or np.random.random() < np.exp(-bU*dE)):
            obj = new
            for a in range(3):
                Nf[a] += dN[3 + a]
                for c in range(L): P[a, c] = P2[a, c]
        else:
            flip(n, g, L, S, GE, GN, a1, x1, y1, z1, dum)
        if obj == 0: break
    return obj
