"""Common objects: cubic rotations, corner permutations, signed actions.
Convention: corner index idx(v) = 4 v0 + 2 v1 + v2.
D(R)[idx(Rv), idx(v)] = s_R[idx(v)]   (sign attached to SOURCE corner).
Global action: (T_R psi)(R(x-c)+c) = s_R(v(x)) psi(x).
"""
import itertools, numpy as np

corners = [np.array(v) for v in itertools.product([0, 1], repeat=3)]
def idx(v): return int(4*v[0] + 2*v[1] + v[2])
c = np.array([0.5, 0.5, 0.5])

def rotations():
    Rs = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product([1, -1], repeat=3):
            R = np.zeros((3, 3), int)
            for i in range(3):
                R[i, perm[i]] = sg[i]
            if round(np.linalg.det(R)) == 1:
                Rs.append(R)
    return Rs
ROTS = rotations()
def rkey(R): return tuple(R.flatten())
RIDX = {rkey(R): i for i, R in enumerate(ROTS)}

def corner_image(R, v):
    w = R @ (v - c) + c
    return np.rint(w).astype(int)

def Pmat(R):
    P = np.zeros((8, 8))
    for v in corners:
        P[idx(corner_image(R, v)), idx(v)] = 1
    return P

def Dmat(R, s):
    P = Pmat(R)
    return P @ np.diag(s)   # column v gets sign s[v]

# generators
A_q = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])   # quarter turn about z
B_t = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])   # threefold about (1,1,1)

def rot_order(R):
    M = np.eye(3, dtype=int)
    for k in range(1, 7):
        M = M @ R
        if (M == np.eye(3)).all():
            return k

def gen_group(gens, maxsize=200):
    """generate matrix group from gens (8x8 signed perms, integer)"""
    key = lambda M: M.astype(np.int8).tobytes()
    I = np.eye(gens[0].shape[0], dtype=int)
    G = {key(I): I}
    frontier = [I]
    while frontier:
        nf = []
        for g in frontier:
            for h in gens:
                p = (g @ h).astype(int)
                k = key(p)
                if k not in G:
                    G[k] = p
                    nf.append(p)
                    if len(G) > maxsize:
                        return None
        frontier = nf
    return list(G.values())

def perm_part(M):
    return (np.abs(M) > 0.5).astype(int)
