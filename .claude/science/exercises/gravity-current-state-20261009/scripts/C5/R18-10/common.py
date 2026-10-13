"""R18-1 common: N0914 stencil (re-derived from N0914:95-97 and checked against R17-1 s1 G_entries), patterns."""
import numpy as np, itertools
TYPES = [(0,0),(1,1),(2,2),(0,1),(1,2),(0,2)]   # xx yy zz xy yz xz
TIDX = {t: n for n, t in enumerate(TYPES)}
E3 = np.eye(3, dtype=int)
def G_entries(x, t):
    """(G p)_j(x) = p_jj(x+e_j) - p_jj(x) + sum_{i!=j}[p_ij(x) - p_ij(x-e_i)]  (N0914:95-97).
    Returns list of ((edge base x, j), coeff) for slot (x,t)."""
    i, j = TYPES[t]; x = np.array(x); out = []
    if i == j: out += [((tuple(x - E3[j]), j), 1), ((tuple(x), j), -1)]
    else: out += [((tuple(x), j), 1), ((tuple(x + E3[i]), j), -1), ((tuple(x), i), 1), ((tuple(x + E3[j]), i), -1)]
    return out
def pos(x, t):
    i, j = TYPES[t]; p = np.array(x, float)
    if i != j: p = p + 0.5*(E3[i] + E3[j])
    return p
def rot_mats():
    Rs = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product([1,-1], repeat=3):
            R = np.zeros((3,3), int)
            for a in range(3): R[a, perm[a]] = sg[a]
            if round(np.linalg.det(R)) == 1: Rs.append(R)
    return Rs
def rotate(supp, R):
    out = []
    for (x, t), v in supp:
        i, j = TYPES[t]; p = R @ pos(x, t)
        ii = int(np.argmax(np.abs(R[:, i]))); jj = int(np.argmax(np.abs(R[:, j])))
        tt = TIDX[tuple(sorted((ii, jj)))]
        base = p - (0.5*(E3[ii] + E3[jj]) if ii != jj else 0)
        out.append(((tuple(int(round(b)) for b in base), tt), v))
    return out
def canon(supp):
    xs = np.array([x for (x, t), v in supp]); mn = xs.min(0)
    return tuple(sorted(((tuple(np.array(x) - mn), t) for (x, t), v in supp)))
# cube: six face slots of the lattice cube with corner 0 (R17-1 s1 'weight=6' pattern, translated)
CUBE = [((0,0,0),3,1), ((0,0,1),3,1), ((0,0,0),4,1), ((1,0,0),4,1), ((0,0,0),5,1), ((0,1,0),5,1)]
MU8 = [((0,1,1),5,1),((0,1,2),2,1),((0,1,2),5,1),((1,1,1),0,1),((1,1,1),5,1),((1,1,2),5,1),((1,1,3),0,1),((2,1,2),2,1)]
def orbit(pat):
    pat = [((x, t), v) for x, t, v in pat]; orb = {}
    for R in rot_mats():
        r = rotate(pat, R); orb.setdefault(canon(r), r)
    out = []
    for c in orb:   # canonical (min corner at 0)
        out.append([(x, t) for x, t in c])
    return out
PATTERNS = orbit(CUBE) + orbit(MU8)
def G_matrix(L):
    """integer G as dense (3V x 6V) array; slot index t*V + site, edge index j*V + site; site = (x*L+y)*L+z"""
    V = L**3; G = np.zeros((3*V, 6*V), dtype=np.int64)
    for x in itertools.product(range(L), repeat=3):
        s0 = (x[0]*L + x[1])*L + x[2]
        for t in range(6):
            for (e, j), c in G_entries(x, t):
                e = tuple(np.mod(e, L)); ei = j*V + (e[0]*L + e[1])*L + e[2]
                G[ei, t*V + s0] += c
    return G
def pattern_vectors(L):
    V = L**3; vecs = []
    for p in PATTERNS:
        for x in itertools.product(range(L), repeat=3):
            v = np.zeros(6*V, dtype=np.int64)
            for (d, t) in p:
                y = np.mod(np.array(x) + np.array(d), L); s = (y[0]*L + y[1])*L + y[2]
                v[t*V + s] ^= 1
            vecs.append(v)
    return np.array(vecs)
def f2_rank(M):
    M = (np.array(M) % 2).astype(np.uint8).copy(); r = 0; rows, cols = M.shape
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i, c]: piv = i; break
        if piv is None: continue
        M[[r, piv]] = M[[piv, r]]
        nz = np.nonzero(M[:, c])[0]; nz = nz[nz != r]
        M[nz] ^= M[r]
        r += 1
        if r == rows: break
    return r
def f2_basis(M):
    """row-reduced basis rows of the F2 row space"""
    M = (np.array(M) % 2).astype(np.uint8).copy(); r = 0; rows, cols = M.shape
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i, c]: piv = i; break
        if piv is None: continue
        M[[r, piv]] = M[[piv, r]]
        nz = np.nonzero(M[:, c])[0]; nz = nz[nz != r]
        M[nz] ^= M[r]
        r += 1
        if r == rows: break
    return M[:r]
