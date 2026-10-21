"""Independent reviewer implementation (written from scratch; does not import author code).

Representation: Pauli strings as dicts {site(tuple): label in 'XYZ'} with explicit sign;
F2 layer as Python-int bitsets over (site,label-bit) coordinates.
"""
import itertools
import numpy as np

# ---- proper cubic group O: signed permutation matrices with det +1
O = []
for p in itertools.permutations(range(3)):
    for s in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), dtype=int)
        for i in range(3):
            M[p[i], i] = s[i]
        if round(np.linalg.det(M)) == 1:
            O.append(M)
assert len(O) == 24

def parity(R):  # sign of the underlying axis permutation
    return int(round(np.linalg.det(np.abs(R))))

HF = np.array([[-1, 0, 0], [0, 0, 1], [0, 1, 0]])  # half turn about (0,1,1)

def Qmat(R, action):
    s = parity(R)
    if action == 'trivial':
        return np.eye(3, dtype=int)
    if action == 'sign':
        return np.diag([1, s, s])
    if action == 'signf':
        return np.eye(3, dtype=int) if s == 1 else HF.copy()
    if action == 'axis':
        return s * np.abs(R)
    if action == 'full':
        return R.copy()
    raise ValueError(action)

ACTIONS = ['trivial', 'sign', 'signf', 'axis', 'full']
LAB = 'XYZ'

def check_hom(action):
    for A in O:
        for B in O:
            if not np.array_equal(Qmat(A @ B, action), Qmat(A, action) @ Qmat(B, action)):
                return False
    return all(round(np.linalg.det(Qmat(R, action))) == 1 for R in O)

# ---- single-site Pauli algebra with phases: sigma_a sigma_b = delta + i eps sigma_c
def mul1(a, b):
    """returns (phase as power of i, label or 'I')"""
    if a == 'I':
        return 0, b
    if b == 'I':
        return 0, a
    if a == b:
        return 0, 'I'
    order = {'X': 0, 'Y': 1, 'Z': 2}
    c = 'XYZ'[3 - order[a] - order[b]]
    # cyclic -> +i, anticyclic -> -i
    if (order[b] - order[a]) % 3 == 1:
        return 1, c
    return 3, c

def mul(P, Q):
    """P,Q = (sign int(+-1 or power-of-i int), dict). Represent phase as power of i (0..3)."""
    ph = (P[0] + Q[0]) % 4
    out = dict(P[1])
    for r, b in Q[1].items():
        a = out.get(r, 'I')
        k, c = mul1(a, b)
        ph = (ph + k) % 4
        if c == 'I':
            out.pop(r, None)
        else:
            out[r] = c
    return ph, out

def beta(R, action, P):
    """Apply soldering action beta_R to phased Pauli string P=(phase, dict)."""
    Qm = Qmat(R, action)
    ph, d = P
    out = {}
    for r, a in d.items():
        col = Qm[:, LAB.index(a)]
        b = int(np.nonzero(col)[0][0])
        if col[b] < 0:
            ph = (ph + 2) % 4
        out[tuple(int(x) for x in R @ np.array(r))] = LAB[b]
    return ph, out

def canon(P):
    return (P[0] % 4, tuple(sorted(P[1].items())))

def translate(P, t):
    return P[0], {tuple(r[i] + t[i] for i in range(3)): a for r, a in P[1].items()}

def anticomm(P, Q):
    n = 0
    for r, a in P[1].items():
        b = Q[1].get(r)
        if b is not None and b != a:
            n += 1
    return n % 2
