"""A52 shared helpers: record-conditioned (tournament) decorations for light's charge hops.

Legs i in DIRS = [+x,-x,+y,-y,+z,-z] (A48).  A tournament T (6x6, 0/1) at a corner:
T[i][j] = 1  <=>  the hop along leg i carries the field factor (Z = sigma^axis) on leg j's link.
Fermionic at the corner iff T[i][j] + T[j][i] = 1 for all i != j (every pair of hops anticommutes).
Record content f (a direction, e.g. a body diagonal) transforms as f -> R_g f under turn g.
Covariant family: T_{g f}[P_g i][P_g j] = T_f[i][j].
"""
import sys, itertools
import numpy as np
sys.path.insert(0, '/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A48')
from a48lib import (ROT, RIDX, MUL, ID, INV, DIRS, NAMES, AXIS, SIGN, PERM, su2_of_rot, raise_out,
                    I2, SX, SY, SZ, PAUL, closure, C4, C2, C3d, rot_about, key, gf2_consistent, gf2_solve)

U = [su2_of_rot(R) for R in ROT]
BD = [tuple(s) for s in itertools.product([1, -1], repeat=3)]        # 8 body diagonals (unnormalised)
AXD = [tuple(d) for d in DIRS]                                        # 6 axis directions
F0 = (1, 1, 1)

def act_vec(g, f):
    return tuple(int(v) for v in ROT[g] @ np.array(f))

def stabilizer(f):
    return [g for g in range(24) if act_vec(g, f) == tuple(f)]

def is_tournament(T):
    return all(T[i][j] + T[j][i] == 1 for i in range(6) for j in range(6) if i != j)

def transport_T(g, T):
    """image tournament under turn g: T'[P_g i][P_g j] = T[i][j]."""
    P = PERM[g]
    Tn = [[0] * 6 for _ in range(6)]
    for i in range(6):
        for j in range(6):
            if i != j:
                Tn[P[i]][P[j]] = T[i][j]
    return Tn

def family(T0, f0=F0):
    """transport T0 (for record f0) to every f in the O-orbit of f0.
    Returns (dict f -> T_f, number of conflicts).  Conflicts = 0 iff T0 is Stab(f0)-invariant."""
    fam = {}; conflicts = 0
    for g in range(24):
        f = act_vec(g, f0)
        Tn = transport_T(g, T0)
        if f in fam:
            if fam[f] != Tn:
                conflicts += 1
        else:
            fam[f] = Tn
    return fam, conflicts

# ---- the C3(111)-invariant tournaments: 5 pair-orbits, each oriented one of two ways (2^5 = 32) ----
C3GROUP = stabilizer(F0)
def c3_pair_orbits():
    seen = set(); orbs = []
    for i in range(6):
        for j in range(i + 1, 6):
            if (i, j) in seen:
                continue
            orb = []
            for g in C3GROUP:
                a, b = PERM[g][i], PERM[g][j]
                orb.append((a, b))
                seen.add((min(a, b), max(a, b)))
            orbs.append(orb)
    return orbs
C3_ORBITS = c3_pair_orbits()

def c3_tournament(bits):
    """bits: 5 bits, one per pair orbit; bit 0 -> for each ordered rep (a,b): T[a][b] = 1 (hop a carries Z on b)."""
    T = [[0] * 6 for _ in range(6)]
    for orb, bit in zip(C3_ORBITS, bits):
        for (a, b) in orb:
            if bit == 0:
                T[a][b] = 1
            else:
                T[b][a] = 1
    return T

ALL_C3_T = [c3_tournament(b) for b in itertools.product([0, 1], repeat=5)]

# ---- coarse torus geometry ----
class Torus:
    def __init__(self, L):
        self.L = tuple(L) if hasattr(L, '__len__') else (L, L, L)
        self.P = tuple(2 * l for l in self.L)
        self.corners = [tuple(2 * np.array(c)) for c in itertools.product(*[range(l) for l in self.L])]
        self.corners = [tuple(int(v) for v in c) for c in self.corners]
        self.cidx = {c: k for k, c in enumerate(self.corners)}
        links = []
        for c in self.corners:
            for a in range(3):
                e = [0, 0, 0]; e[a] = 1
                links.append(self.wrap(np.array(c) + np.array(e)))
        self.links = links
        self.lidx = {l: k for k, l in enumerate(links)}
        self.n = len(links)
        # plaquettes: (corner, a, b) a<b ; loop v -> v+2ea -> v+2ea+2eb -> v+2eb -> v
        self.plaqs = []
        for c in self.corners:
            for a, b in [(0, 1), (0, 2), (1, 2)]:
                self.plaqs.append((c, a, b))
        self._ltab = {}
        for c in self.corners:
            for i in range(6):
                self._ltab[(c, i)] = self.lidx[self.wrap(np.array(c) + np.array(DIRS[i]))]
        self._ends = [self._ends_calc(l) for l in range(self.n)]
        self._perm = {}
    def wrap(self, x):
        return tuple(int(v) % p for v, p in zip(x, self.P))
    def link(self, v, i):
        return self._ltab[(v, i)]
    def link_perm(self, g, centre=(0, 0, 0)):
        k = (g, tuple(centre))
        if k not in self._perm:
            self._perm[k] = [self.lidx[self.turn(g, self.links[q], centre)] for q in range(self.n)]
        return self._perm[k]
    def nbr(self, v, i):
        return self.wrap(np.array(v) + 2 * np.array(DIRS[i]))
    def ends(self, l):
        return self._ends[l]
    def _ends_calc(self, l):
        """(v, i, w, i') with link l = v + DIRS[i] = w + DIRS[i'] (i = + direction from v)."""
        x = np.array(self.links[l]); a = [k for k in range(3) if x[k] % 2 == 1][0]
        e = np.zeros(3, int); e[a] = 1
        v = self.wrap(x - e); w = self.wrap(x + e)
        return v, 2 * a, w, 2 * a + 1
    def plaq_loop(self, p):
        """list of (link, from_corner, leg_from, to_corner, leg_to) around the loop."""
        c, a, b = p
        ea = 2 * a; eb = 2 * b               # + legs
        v0 = c; v1 = self.nbr(v0, ea); v2 = self.nbr(v1, eb); v3 = self.nbr(v0, eb)
        return [(self.link(v0, ea), v0, ea, v1, ea + 1), (self.link(v1, eb), v1, eb, v2, eb + 1),
                (self.link(v2, ea + 1), v2, ea + 1, v3, ea), (self.link(v3, eb + 1), v3, eb + 1, v0, eb)]
    def turn(self, g, x, centre=(0, 0, 0)):
        c = np.array(centre)
        return self.wrap(c + ROT[g] @ (np.array(x) - c))

# ---- symbolic Pauli strings: P = i^p * prod X^x Z^z (bits in python ints) ----
def pmul(A, B):
    x1, z1, p1 = A; x2, z2, p2 = B
    return (x1 ^ x2, z1 ^ z2, (p1 + p2 + 2 * bin(z1 & x2).count('1')) % 4)
def anticomm(A, B):
    return (bin(A[0] & B[1]).count('1') + bin(A[1] & B[0]).count('1')) % 2

def hop_string(tor, l, recs, Tof, include_far=True):
    """Z2-version hop on link l: X_l * Z-decorations at both ends, from the records (dict corner -> f)
    and the tournament map Tof (f -> T)."""
    v, i, w, ip = tor.ends(l)
    z = 0
    Tv = Tof[recs[v]]
    for j in range(6):
        if j != i and Tv[i][j]:
            z ^= 1 << tor.link(v, j)
    if include_far:
        Tw = Tof[recs[w]]
        for j in range(6):
            if j != ip and Tw[ip][j]:
                z ^= 1 << tor.link(w, j)
    return (1 << l, z, 0)

def gauss_string(tor, v):
    z = 0
    for j in range(6):
        z ^= 1 << tor.link(v, j)
    return (0, z, 0)

def turn_string(tor, g, A, centre=(0, 0, 0)):
    """image of a Pauli string under the soldered turn, ignoring signs/phases: link qubits keep field
    type (Z->Z) and X->X up to sign (a turn maps a link's sigma^a to +-sigma^a' at the image link and
    the transverse pair to the image transverse pair).  For X we only track 'transverse' type."""
    x, z, p = A
    xn = 0; zn = 0
    perm = tor.link_perm(g, centre)
    for q in range(tor.n):
        im = perm[q]
        if (x >> q) & 1:
            xn |= 1 << im
        if (z >> q) & 1:
            zn |= 1 << im
    return (xn, zn, 0)
