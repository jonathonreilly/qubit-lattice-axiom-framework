"""A54 helpers: GF(2) systems for a local diagonal sign chi relating A52's dressed ring to the bare ring.

Z2 form: hop t_l = X_l Z^{d_l}; dressed ring S_p = prod of the four hops = s_p X^{dp} Z^{d dp}.
Pauli strings are (x, z, p) with python-int bitmasks over links (A52 convention, phase i^p).
"""
import sys, itertools
import numpy as np
SP = '/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad'
sys.path.insert(0, SP + '/c8/A52')
from a52lib import (Torus, hop_string, gauss_string, family, ALL_C3_T, BD, F0, DIRS, SIGN, AXIS,
                    pmul, anticomm)

def popc(x):
    return bin(x).count('1')

class GF2:
    """incremental GF(2) elimination; a row is an int, bit 0 = right-hand side, bits >= 1 = unknowns.
    Highest-bit pivoting (unknown indices should be assigned in spatial order to limit fill-in)."""
    def __init__(self):
        self.piv = {}; self.incons = 0; self.neq = 0
    def add(self, row):
        self.neq += 1
        while row > 1:
            b = row.bit_length() - 1
            p = self.piv.get(b)
            if p is None:
                self.piv[b] = row
                return
            row ^= p
        if row == 1:
            self.incons += 1
    def rank(self):
        return len(self.piv)
    def solve(self, nvar):
        """one solution (free unknowns = 0) as an int bitmask over unknown indices 1..nvar; None if inconsistent."""
        if self.incons:
            return None
        sol = 0
        for b in sorted(self.piv):              # ascending: lower pivots first
            row = self.piv[b]
            rhs = row & 1
            rest = (row >> 1) & ~(1 << (b - 1))
            val = rhs ^ (popc(rest & sol) & 1)
            if val:
                sol |= 1 << (b - 1)
        return sol

def setup(Ls, tidx=0, recs_kind='uniform', seed=0):
    tor = Torus(Ls)
    Tof, conf = family(ALL_C3_T[tidx]); assert conf == 0
    rng = np.random.default_rng(seed)
    if recs_kind == 'uniform':
        recs = {v: F0 for v in tor.corners}
    else:
        recs = {v: BD[rng.integers(8)] for v in tor.corners}
    hops = [hop_string(tor, l, recs, Tof) for l in range(tor.n)]
    dcol = [h[1] for h in hops]                      # Z-set of hop l (bitmask over links)
    loops = [tor.plaq_loop(p) for p in tor.plaqs]
    dp = []
    for lp in loops:
        m = 0
        for (l, v, i, w, ip) in lp:
            m |= 1 << l
        dp.append(m)
    Ddp = []
    for lp in loops:
        z = 0
        for (l, v, i, w, ip) in lp:
            z ^= dcol[l]
        Ddp.append(z)
    return tor, recs, hops, dcol, loops, dp, Ddp

def link_d2(tor, l, m):
    a = tor.links[l]; b = tor.links[m]; s = 0
    for k in range(3):
        t = abs(a[k] - b[k]) % tor.P[k]; t = min(t, tor.P[k] - t); s += t * t
    return s

def pt_d2(tor, a, b):
    s = 0
    for k in range(3):
        t = abs(a[k] - b[k]) % tor.P[k]; t = min(t, tor.P[k] - t); s += t * t
    return s

def plaqs_of_links(tor, dp):
    out = [[] for _ in range(tor.n)]
    for p, m in enumerate(dp):
        x = m
        while x:
            l = (x & -x).bit_length() - 1; x &= x - 1
            out[l].append(p)
    return out

def bits_of(x):
    out = []
    while x:
        l = (x & -x).bit_length() - 1; x &= x - 1
        out.append(l)
    return out

def stabilizer_signs_ok(tor, hops, loops):
    """exact dressed-loop Pauli strings S_p (phase tracked)."""
    S = []
    for lp in loops:
        P = (0, 0, 0)
        for (l, v, i, w, ip) in lp:        # t1 acts first -> rightmost
            P = pmul(hops[l], P)
        S.append(P)
    return S
