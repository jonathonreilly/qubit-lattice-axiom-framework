"""Independent geometry for the corner graph of Z^3 (written from the note's description only).

Corner (v; {d, d'}) with d perpendicular to d', placed at v + (d + d')/4.
On-site edges: cuboctahedron edges (share one direction, other two perpendicular).
Links: (v; {d, d'}) -- (v + d; {-d, d'}).
"""
import itertools
import numpy as np

DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
DIDX = {d: i for i, d in enumerate(DIRS)}


def neg(d):
    return tuple(-a for a in d)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def perp(a, b):
    return sum(x * y for x, y in zip(a, b)) == 0


# 12 corner types: unordered perpendicular pairs
CTYPES = []
for i in range(6):
    for j in range(i + 1, 6):
        if perp(DIRS[i], DIRS[j]):
            CTYPES.append(frozenset([DIRS[i], DIRS[j]]))
assert len(CTYPES) == 12
CTIDX = {c: i for i, c in enumerate(CTYPES)}


def rotations():
    """24 proper rotations as integer 3x3 matrices."""
    out = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            M = np.zeros((3, 3), dtype=int)
            for r in range(3):
                M[r, perm[r]] = signs[r]
            if round(np.linalg.det(M)) == 1:
                out.append(M)
    assert len(out) == 24
    # put identity first
    out.sort(key=lambda M: (not np.array_equal(M, np.eye(3, dtype=int)),))
    return out


def rot_vec(M, v):
    return tuple(int(x) for x in M @ np.array(v))


def classify(M):
    """Return 'E','C4','C2axis','C3','C2edge'."""
    tr = int(np.trace(M))
    if tr == 3:
        return 'E'
    if tr == 1:
        return 'C4'
    if tr == 0:
        return 'C3'
    # tr == -1: C2; axis C2 iff diagonal
    if np.count_nonzero(M - np.diag(np.diag(M))) == 0:
        return 'C2axis'
    return 'C2edge'


def w1(M):
    """Sign of the permutation of the six directions (0 even, 1 odd)."""
    img = [DIDX[rot_vec(M, d)] for d in DIRS]
    seen = [False] * 6
    par = 0
    for i in range(6):
        if not seen[i]:
            j = i
            ln = 0
            while not seen[j]:
                seen[j] = True
                j = img[j]
                ln += 1
            par ^= (ln - 1) & 1
    return par


class Lattice:
    def __init__(self, L):
        self.L = L
        self.sites = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
        self.sidx = {s: i for i, s in enumerate(self.sites)}
        self.ncorner = 12 * len(self.sites)

    def wrap(self, v):
        return tuple(a % self.L for a in v)

    def corner(self, v, ct):
        return self.sidx[self.wrap(v)] * 12 + CTIDX[frozenset(ct)]

    def corner_info(self, c):
        return self.sites[c // 12], CTYPES[c % 12]

    def corner_pos4(self, v, ct):
        """4 * position (integer), unwrapped."""
        d, e = tuple(ct)
        return tuple(4 * a + b + c for a, b, c in zip(v, d, e))

    def neighbours(self, v, ct):
        """Return list of (v', ct', kind) for the 6 neighbours of (v; ct) in unwrapped coords."""
        d, e = tuple(ct)
        out = []
        # on-site: share one direction a, other f perpendicular to both of ct
        for a, b in ((d, e), (e, d)):
            for f in DIRS:
                if perp(f, a) and perp(f, b):
                    out.append((v, frozenset([a, f]), 'onsite'))
        # links
        for a, b in ((d, e), (e, d)):
            out.append((add(v, a), frozenset([neg(a), b]), 'link'))
        assert len(out) == 6
        return out
