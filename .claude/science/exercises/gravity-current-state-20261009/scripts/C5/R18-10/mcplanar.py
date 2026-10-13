"""R18-10 planar (subsystem) variant, a deliberate stress test of the axis-only pinch diagnostic.
Filter: accept a flip only if, for every slot type, the signed label change vanishes in every plane perpendicular to each
of the type's indices (diag aa: a-planes; face ab: a- and b-planes). This implies dN = 0 (dipole conserved).
In the sector where all those planar counts are uniform, n_row(k || e_a)(k != 0) = 0 exactly for every row slot of a,
so by Identity V S_gamma(k || axis) = 0 exactly: an axis-line zero forced by the prepared sector, not by the weight."""
import numpy as np, numba as nb
from mc import *
from mcpair import flip
PLANES = np.array([[0, -1], [1, -1], [2, -1], [0, 1], [1, 2], [0, 2]], dtype=np.int64)   # axes whose planes are conserved, per type
@nb.njit(cache=True)
def planar_ok(n, L, S, a1, x1, y1, z1, dP):
    for t in range(6):
        for ax in range(3):
            for c in range(L): dP[t, ax, c] = 0
    for b in range(S.shape[1]):
        if S[a1, b, 0] < 0: break
        sx = (x1 + S[a1, b, 0]) % L; sy = (y1 + S[a1, b, 1]) % L; sz = (z1 + S[a1, b, 2]) % L; t = S[a1, b, 3]
        dl = 1 - 2*n[t, sx, sy, sz]
        dP[t, 0, sx] += dl; dP[t, 1, sy] += dl; dP[t, 2, sz] += dl
    PL = ((0, -1), (1, -1), (2, -1), (0, 1), (1, 2), (0, 2))
    for t in range(6):
        for k in range(2):
            ax = PL[t][k]
            if ax < 0: continue
            for c in range(L):
                if dP[t, ax, c] != 0: return False
    return True
@nb.njit(cache=True)
def sweeps_planar(n, g, L, bU, S, GE, GN, nsweep, seed, extra):
    np.random.seed(seed); V = L*L*L; npat = S.shape[0]; acc = 0; tot = 0; filt = 0
    dP = np.zeros((6, 3, L), dtype=np.int64); dN = np.zeros(6, dtype=np.int64); dum = np.zeros(6, dtype=np.int64)
    for m in range(npat*V*nsweep + extra):
        a1 = np.random.randint(npat); x1 = np.random.randint(L); y1 = np.random.randint(L); z1 = np.random.randint(L)
        tot += 1
        if not planar_ok(n, L, S, a1, x1, y1, z1, dP): continue
        filt += 1
        for t in range(6): dN[t] = 0
        dE = flip(n, g, L, S, GE, GN, a1, x1, y1, z1, dN)
        if dE <= 0 or np.random.random() < np.exp(-bU*dE):
            acc += 1
        else:
            flip(n, g, L, S, GE, GN, a1, x1, y1, z1, dum)
    return acc/max(tot, 1), filt/max(tot, 1)
@nb.njit(cache=True)
def drive_all_planar(n, g, L, bU, S, GE, GN, nsweep, seed, extra):
    """preparation only: GC moves accepted only if sum over types and conserved planes |count - half-plane| does not increase."""
    np.random.seed(seed); V = L*L*L; npat = S.shape[0]; h2 = L*L//2
    PL = ((0, -1), (1, -1), (2, -1), (0, 1), (1, 2), (0, 2))
    P = np.zeros((6, 3, L), dtype=np.int64)
    for t in range(6):
        for x in range(L):
            for y in range(L):
                for z in range(L):
                    v = n[t, x, y, z]; P[t, 0, x] += v; P[t, 1, y] += v; P[t, 2, z] += v
    def_obj = 0
    for t in range(6):
        for k in range(2):
            ax = PL[t][k]
            if ax < 0: continue
            for c in range(L): def_obj += abs(P[t, ax, c] - h2)
    obj = def_obj; dP = np.zeros((6, 3, L), dtype=np.int64); dN = np.zeros(6, dtype=np.int64); dum = np.zeros(6, dtype=np.int64)
    for m in range(npat*V*nsweep + extra):
        a1 = np.random.randint(npat); x1 = np.random.randint(L); y1 = np.random.randint(L); z1 = np.random.randint(L)
        for t in range(6):
            for ax in range(3):
                for c in range(L): dP[t, ax, c] = 0
        for b in range(S.shape[1]):
            if S[a1, b, 0] < 0: break
            sx = (x1 + S[a1, b, 0]) % L; sy = (y1 + S[a1, b, 1]) % L; sz = (z1 + S[a1, b, 2]) % L; t = S[a1, b, 3]
            dl = 1 - 2*n[t, sx, sy, sz]; dP[t, 0, sx] += dl; dP[t, 1, sy] += dl; dP[t, 2, sz] += dl
        new = 0
        for t in range(6):
            for k in range(2):
                ax = PL[t][k]
                if ax < 0: continue
                for c in range(L): new += abs(P[t, ax, c] + dP[t, ax, c] - h2)
        if new > obj: continue
        for t in range(6): dN[t] = 0
        dE = flip(n, g, L, S, GE, GN, a1, x1, y1, z1, dN)
        if dE <= 0 or np.random.random() < np.exp(-bU*dE):
            obj = new
            for t in range(6):
                for ax in range(3):
                    for c in range(L): P[t, ax, c] += dP[t, ax, c]
        else:
            flip(n, g, L, S, GE, GN, a1, x1, y1, z1, dum)
        if obj == 0: break
    return obj
