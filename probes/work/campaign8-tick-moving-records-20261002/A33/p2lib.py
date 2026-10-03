"""A33 shared library.

REUSED (cited): A20's grp.py (the 24 proper cubic rotations, soldered label_map) and
A20's pauli.py (exact Pauli strings with phases). Everything else here is new.

Conventions (as A20):
 - a rotation R is a 3x3 signed permutation matrix with det +1. About a centre c it moves
   y -> R(y - c) + c and turns sigma^a -> eps[a] sigma^{pi[a]} (soldered: sigma.n -> sigma.(R n)).
 - label codes: 0 = identity, 1 = sigma^x, 2 = sigma^y, 3 = sigma^z.
 - mod-2 bits (bx, bz): sigma^x = (1,0), sigma^y = (1,1), sigma^z = (0,1).
 - a "pattern" is a canonical Hermitian Pauli string {site tuple: label code}; its exact
   rotation is (prod of eps) * (rotated pattern).
"""
import sys
import itertools
import numpy as np

A20DIR = ("/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-"
          "focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A20")


def _load_a20():
    """A20's grp.py shadows the stdlib module `grp`; load both A20 files by path under
    private names, giving pauli.py the A20 grp while it imports."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("a20_grp", A20DIR + "/grp.py")
    g = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(g)
    saved = sys.modules.get("grp")
    sys.modules["grp"] = g
    try:
        spec2 = importlib.util.spec_from_file_location("a20_pauli", A20DIR + "/pauli.py")
        pm = importlib.util.module_from_spec(spec2)
        spec2.loader.exec_module(pm)
    finally:
        if saved is not None:
            sys.modules["grp"] = saved
        else:
            del sys.modules["grp"]
    return g, pm


_g, _pm = _load_a20()
rotations, label_map = _g.rotations, _g.label_map   # A20, reused
P = _pm.P                                           # A20, reused

ROT = rotations()
LM = [label_map(R) for R in ROT]
LBITS = {0: (0, 0), 1: (1, 0), 2: (1, 1), 3: (0, 1)}
BITS2L = {v: k for k, v in LBITS.items()}
LNAME = "IXYZ"


def popc(v):
    return bin(v).count("1")


# ---------------------------------------------------------------- group action
def rot_label(ri, l):
    """soldered image of label l under ROT[ri] -> (sign, label)."""
    if l == 0:
        return 1, 0
    pi, eps = LM[ri]
    return eps[l - 1], pi[l - 1] + 1


def act2(ri, y2, c2):
    """doubled coordinates: 2y -> R(2y - 2c) + 2c."""
    R = ROT[ri]
    d = np.array(y2) - np.array(c2)
    return tuple(int(t) for t in (R @ d + np.array(c2)))


def act(ri, y, c2=(0, 0, 0)):
    y2 = tuple(2 * t for t in y)
    z2 = act2(ri, y2, c2)
    assert all(t % 2 == 0 for t in z2)
    return tuple(t // 2 for t in z2)


def rot_pattern(ri, pat, c2=(0, 0, 0)):
    """exact soldered rotation about centre c = c2/2 of a canonical string -> (sign, pattern)."""
    sg, out = 1, {}
    for y, l in pat.items():
        s, l2 = rot_label(ri, l)
        sg *= s
        out[act(ri, y, c2)] = l2
    return sg, out


def ladd(a, b):
    x = (LBITS[a][0] ^ LBITS[b][0], LBITS[a][1] ^ LBITS[b][1])
    return BITS2L[x]


def padd(p, q):
    """mod-2 sum of patterns."""
    out = dict(p)
    for y, l in q.items():
        out[y] = ladd(out.get(y, 0), l)
        if out[y] == 0:
            del out[y]
    return out


def lcomm(a, b):
    """1 if single-site labels anticommute."""
    if a == 0 or b == 0 or a == b:
        return 0
    return 1


def pcomm(p, q):
    """1 if patterns anticommute."""
    t = 0
    for y, l in p.items():
        if y in q:
            t ^= lcomm(l, q[y])
    return t


def translate(p, t):
    return {tuple(a + b for a, b in zip(y, t)): l for y, l in p.items()}


def pat_str(p):
    return " ".join(f"{LNAME[l]}{y}" for y, l in sorted(p.items()))


# ---------------------------------------------------------------- groups
def group(kind, axis=2):
    if kind == "O":
        return list(range(24))
    if kind == "D4":      # rotations keeping the axis line (either direction)
        return [i for i, R in enumerate(ROT) if abs(R[axis, axis]) == 1]
    if kind == "C4":      # rotations fixing e_axis
        return [i for i, R in enumerate(ROT) if R[axis, axis] == 1]
    if kind == "C3":      # about (1,1,1)
        c3 = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
        out = []
        M = np.eye(3, dtype=int)
        for _ in range(3):
            out.append(next(i for i, R in enumerate(ROT) if np.array_equal(R, M)))
            M = c3 @ M
        return out
    if kind == "T":       # tetrahedral: even permutations with even number of sign flips
        out = []
        for i, R in enumerate(ROT):
            perm = [int(np.nonzero(R[:, a])[0][0]) for a in range(3)]
            ev = sum(1 for a in range(3) for b in range(a + 1, 3) if perm[a] > perm[b]) % 2 == 0
            if ev:
                out.append(i)
        return out
    raise ValueError(kind)


def axis_rotation(a):
    """a rotation index R with R e_z = e_a."""
    ez = np.array([0, 0, 1])
    for i, R in enumerate(ROT):
        if np.array_equal(R @ ez, np.eye(3, dtype=int)[a]):
            return i
    raise ValueError


# ---------------------------------------------------------------- invariant shapes
def invariant_basis(ball, grp, c2=(0, 0, 0)):
    """mod-2 basis of patterns on `ball` (list of site tuples, closed under grp about c2/2)
    that are invariant (mod 2) under the soldered action of grp. Orbit by orbit:
    the label at an orbit representative must be fixed (mod 2) by its stabiliser."""
    ballset = set(ball)
    seen, basis, orbits = set(), [], []
    for y in sorted(ball):
        if y in seen:
            continue
        orb = {}
        for ri in grp:
            z = act(ri, y, c2)
            assert z in ballset, (y, z)
            orb.setdefault(z, []).append(ri)
        seen |= set(orb)
        stab = orb[y]
        inv = [l for l in range(4) if all(rot_label(ri, l)[1] == l for ri in stab)]
        if len(inv) == 4:
            labs = [1, 3]
        elif len(inv) == 2:
            labs = [inv[1]]
        else:
            labs = []
        orbits.append((y, len(orb), len(stab), inv))
        for l0 in labs:
            pat = {}
            for ri in grp:
                z = act(ri, y, c2)
                l = rot_label(ri, l0)[1]
                if z in pat:
                    assert pat[z] == l
                pat[z] = l
            basis.append(pat)
    return basis, orbits


def combo(basis, bits):
    p = {}
    for b, on in zip(basis, bits):
        if on:
            p = padd(p, b)
    return p


def exact_invariant(pat, grp, c2=(0, 0, 0)):
    """True iff every soldered rotation in grp maps the canonical string to itself with sign +1."""
    for ri in grp:
        s, q = rot_pattern(ri, pat, c2)
        if q != pat or s != 1:
            return False
    return True


def ball_sites(r2max, c2=(0, 0, 0)):
    """sites y with |y - c|^2 <= r2max (r2max in units of the fine lattice; c = c2/2)."""
    rng = range(-4, 6)
    out = []
    for y in itertools.product(rng, repeat=3):
        d2 = sum((2 * a - b) ** 2 for a, b in zip(y, c2))  # = 4|y-c|^2
        if d2 <= 4 * r2max:
            out.append(y)
    return out


# ---------------------------------------------------------------- torus utilities
class Torus:
    def __init__(self, L):
        self.L = L
        self.N = L ** 3
        self.sites = list(itertools.product(range(L), repeat=3))

    def idx(self, y):
        L = self.L
        return (y[0] % L) + L * (y[1] % L) + L * L * (y[2] % L)

    def wrap(self, y):
        L = self.L
        return tuple(a % L for a in y)

    def bits(self, pat):
        """pattern -> (xbits, zbits) python ints; asserts no self-overlap after wrapping."""
        xb = zb = 0
        seen = {}
        for y, l in pat.items():
            i = self.idx(y)
            if i in seen:
                raise ValueError("pattern overlaps itself on this torus")
            seen[i] = l
            bx, bz = LBITS[l]
            if bx:
                xb |= 1 << i
            if bz:
                zb |= 1 << i
        return xb, zb

    def wrapped(self, pat):
        return {self.wrap(y): l for y, l in pat.items()}


def symp(a, b):
    return popc((a[0] & b[1]) ^ (a[1] & b[0])) & 1


class Elim:
    """incremental F2 row reduction on python-int bit vectors (leading-bit pivots),
    optionally tracking the combination (another python int) that produced each row."""

    def __init__(self):
        self.rows = {}

    def reduce(self, v, c=0):
        while v:
            h = v.bit_length() - 1
            r = self.rows.get(h)
            if r is None:
                return v, c
            v ^= r[0]
            c ^= r[1]
        return 0, c

    def add(self, v, c=0):
        v, c = self.reduce(v, c)
        if v:
            self.rows[v.bit_length() - 1] = (v, c)
            return True
        return False

    def __len__(self):
        return len(self.rows)


def syndrome_table(T, gens):
    """gens: list of (xb, zb) one per generator (index = position in list).
    Returns, for every site, the syndrome bit-vectors of X_y and Z_y."""
    N = T.N
    sx = [0] * N
    sz = [0] * N
    for gi, (xb, zb) in enumerate(gens):
        # X_y anticommutes with generators having a Z-part at y; Z_y with an X-part at y
        v = zb
        while v:
            h = v & -v
            sx[h.bit_length() - 1] |= 1 << gi
            v ^= h
        v = xb
        while v:
            h = v & -v
            sz[h.bit_length() - 1] |= 1 << gi
            v ^= h
    return sx, sz


def pauli_exact(pat_wrapped, sign=1):
    """A20 P object for sign * canonical string (sites already wrapped)."""
    out = P(0 if sign == 1 else 2, {})
    for y in sorted(pat_wrapped):
        l = pat_wrapped[y]
        out = out * P.single(y, l - 1)
    return out
