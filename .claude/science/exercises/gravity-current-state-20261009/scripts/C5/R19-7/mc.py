"""R18-1 MC engine: Metropolis over XOR flips of the 4 local patterns (cube + 3 mu8), weight exp(-bU sum gamma^2)."""
import numpy as np, itertools, numba as nb
from common import *
def move_tables(L):
    """per pattern type: XOR-deduped slot list (dx,dy,dz,t) mod L, and for each slot its G entries (ex,ey,ez,j,c)"""
    tabs = []
    for p in PATTERNS:
        cnt = {}
        for d, t in p:
            key = (tuple(int(v) % L for v in d), t); cnt[key] = cnt.get(key, 0) ^ 1
        tabs.append([k for k, v in cnt.items() if v])
    maxs = max(len(t) for t in tabs)
    S = -np.ones((len(tabs), maxs, 4), dtype=np.int64)
    for a, tab in enumerate(tabs):
        for b, (d, t) in enumerate(tab): S[a, b] = (d[0], d[1], d[2], t)
    GE = np.zeros((6, 4, 5), dtype=np.int64); GN = np.zeros(6, dtype=np.int64)
    for t in range(6):
        ent = G_entries((0,0,0), t); GN[t] = len(ent)
        for b, ((e, j), c) in enumerate(ent): GE[t, b] = (e[0], e[1], e[2], j, c)
    return S, GE, GN
@nb.njit(cache=True)
def charges(n, L):
    g = np.zeros((3, L, L, L), dtype=np.int64)
    for x in range(L):
        for y in range(L):
            for z in range(L):
                for t in range(6):
                    v = n[t, x, y, z]
                    if v == 0: continue
                    if t < 3:
                        j = t; xm = [x, y, z]; xm[j] = (xm[j] - 1) % L
                        g[j, xm[0], xm[1], xm[2]] += 1; g[j, x, y, z] -= 1
                    else:
                        if t == 3: i, j = 0, 1
                        elif t == 4: i, j = 1, 2
                        else: i, j = 0, 2
                        g[j, x, y, z] += 1
                        xp = [x, y, z]; xp[i] = (xp[i] + 1) % L; g[j, xp[0], xp[1], xp[2]] -= 1
                        g[i, x, y, z] += 1
                        xq = [x, y, z]; xq[j] = (xq[j] + 1) % L; g[i, xq[0], xq[1], xq[2]] -= 1
    return g
@nb.njit(cache=True)
def sweeps(n, g, L, bU, S, GE, GN, nsweep, seed, extra=0):
    np.random.seed(seed)
    V = L*L*L; npat = S.shape[0]; acc = 0; tot = 0
    eidx = np.zeros((64, 4), dtype=np.int64); edel = np.zeros(64, dtype=np.int64)
    for m in range(npat*V*nsweep + extra):
        if True:
            a = np.random.randint(npat); bx = np.random.randint(L); by = np.random.randint(L); bz = np.random.randint(L)
            ne = 0
            for b in range(S.shape[1]):
                if S[a, b, 0] < 0: break
                sx = (bx + S[a, b, 0]) % L; sy = (by + S[a, b, 1]) % L; sz = (bz + S[a, b, 2]) % L; t = S[a, b, 3]
                dl = 1 - 2*n[t, sx, sy, sz]
                for q in range(GN[t]):
                    ex = (sx + GE[t, q, 0]) % L; ey = (sy + GE[t, q, 1]) % L; ez = (sz + GE[t, q, 2]) % L; j = GE[t, q, 3]
                    found = -1
                    for r in range(ne):
                        if eidx[r, 0] == ex and eidx[r, 1] == ey and eidx[r, 2] == ez and eidx[r, 3] == j:
                            found = r; break
                    if found < 0:
                        eidx[ne, 0] = ex; eidx[ne, 1] = ey; eidx[ne, 2] = ez; eidx[ne, 3] = j; edel[ne] = 0; found = ne; ne += 1
                    edel[found] += GE[t, q, 4]*dl
            dE = 0.0
            for r in range(ne):
                g0 = g[eidx[r, 3], eidx[r, 0], eidx[r, 1], eidx[r, 2]]; g1 = g0 + edel[r]
                dE += (g1*g1 - g0*g0)/4.0
            tot += 1
            if dE <= 0 or np.random.random() < np.exp(-bU*dE):
                acc += 1
                for b in range(S.shape[1]):
                    if S[a, b, 0] < 0: break
                    sx = (bx + S[a, b, 0]) % L; sy = (by + S[a, b, 1]) % L; sz = (bz + S[a, b, 2]) % L; t = S[a, b, 3]
                    n[t, sx, sy, sz] ^= 1
                for r in range(ne):
                    g[eidx[r, 3], eidx[r, 0], eidx[r, 1], eidx[r, 2]] += edel[r]
    return acc/max(tot, 1)
OFFS = np.array([pos((0,0,0), t) for t in range(6)])   # slot offsets within the unit cell
def kgrid_dirs(L):
    """lattice k along axis/face/body directions, with all cubic-equivalent copies (indices m)"""
    out = {}
    ax = [(1,0,0),(0,1,0),(0,0,1)]
    fa = [(1,1,0),(1,-1,0),(0,1,1),(0,1,-1),(1,0,1),(1,0,-1)]
    bo = [(1,1,1),(1,1,-1),(1,-1,1),(-1,1,1)]
    for name, dirs, mmax in [("axis", ax, L//2), ("face", fa, L//2), ("body", bo, L//2)]:
        out[name] = [(m, [np.array(d)*m for d in dirs]) for m in range(1, mmax+1)]
    return out
def channel_pols(khat):
    """unit traceless polarizations: TT1, TT2, V1, V2, S; plus trace T. eps as 3x3."""
    k = khat/np.linalg.norm(khat)
    a = np.array([1.0, 0, 0]) if abs(k[0]) < 0.9 else np.array([0, 1.0, 0])
    u = np.cross(k, a); u /= np.linalg.norm(u); w = np.cross(k, u)
    sym = lambda p, q: (np.outer(p, q) + np.outer(q, p))/2
    TT1 = (np.outer(u, u) - np.outer(w, w))/np.sqrt(2); TT2 = sym(u, w)*np.sqrt(2)
    V1 = sym(k, u)*np.sqrt(2); V2 = sym(k, w)*np.sqrt(2)
    S = (3*np.outer(k, k) - np.eye(3))/np.sqrt(6); T = np.eye(3)/np.sqrt(3)
    return dict(TT=[TT1, TT2], V=[V1, V2], S=[S], T=[T])
def cvec(eps):
    """weights c_s on the 6 slot types: eps_jj on diagonal, 2 eps_ij on face (R17-1 probe)"""
    return np.array([eps[0,0], eps[1,1], eps[2,2], 2*eps[0,1], 2*eps[1,2], 2*eps[0,2]])
