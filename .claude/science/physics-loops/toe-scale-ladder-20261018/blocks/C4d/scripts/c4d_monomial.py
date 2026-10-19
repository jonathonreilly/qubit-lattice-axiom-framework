"""Monomial (deterministic, phases irrelevant) pair maps W on near pairs, built equivariantly from
orbit representatives, and the exact 3-magnon spectator consistency test.
Used by c4d_02 (range 1, exhaustive) and c4d_03 (range 2, glider)."""
import itertools
import numpy as np
from c4d_common import (T, O, cheb, add, sub, rot, ball, canon_rho, near_rhos, pair, box, dist_set)


def lexmin(S):
    return min(S)


def normalise(S):
    m = lexmin(S)
    return frozenset(sub(s, m) for s in S)


def orbit_reps(G, r):
    """orbits of canonical relative vectors under G (acting up to sign)."""
    rhos = near_rhos(r)
    seen, reps = set(), []
    for rho in rhos:
        if rho in seen:
            continue
        orb = {canon_rho(rot(R, rho)) for R in G}
        seen |= orb
        reps.append((rho, sorted(orb)))
    return reps


def stabiliser(G, rho):
    """space-group elements (R,t), R in G, fixing the pair {0,rho} as a set."""
    out = []
    for R in G:
        Rr = rot(R, rho)
        if Rr == rho:
            out.append((R, (0, 0, 0)))
        elif Rr == tuple(-x for x in rho):
            out.append((R, rho))
    return out


def act(g, S):
    R, t = g
    return frozenset(add(rot(R, s), t) for s in S)


def allowed_images(G, rho, r):
    p = pair((0, 0, 0), rho)
    B = box(p, r)
    st = stabiliser(G, rho)
    out = []
    for a, b in itertools.combinations(B, 2):
        s = pair(a, b)
        if cheb(a, b) > r:
            continue
        if all(act(g, s) == s for g in st):
            out.append(s)
    return out


class MonomialW:
    """W defined on reps, extended by G-equivariance and translations."""

    def __init__(self, G, r, rep_images):
        self.G, self.r = G, r
        self.img = {}
        # for every canonical rho find (R, sign) mapping a rep onto it
        self.rep_of = {}
        for rho0, orb in orbit_reps(G, r):
            for R in G:
                v = rot(R, rho0)
                c = canon_rho(v)
                if c not in self.rep_of:
                    self.rep_of[c] = (rho0, R)
        self.rep_images = rep_images

    def __call__(self, p):
        x, y = sorted(p)
        rho = sub(y, x)
        c = canon_rho(rho)
        rho0, R = self.rep_of[c]
        v = rot(R, rho0)
        # R maps {0, rho0} -> {0, v}; v = rho or -rho
        if v == rho:
            t = x
        else:
            t = y
        return act((R, t), self.rep_images[rho0])

    def check_equivariance(self):
        """W(g p) = g W(p) for g in G and translations, on all canonical near pairs."""
        for rho in near_rhos(self.r):
            p = pair((0, 0, 0), rho)
            Wp = self(p)
            for R in self.G:
                for t in [(0, 0, 0), (1, -2, 3)]:
                    g = (R, t)
                    if self(act(g, p)) != act(g, Wp):
                        return False
        return True


def bijective_on_near(W, r):
    """injective on near pairs (=> bijective by TI + finiteness on a torus)."""
    imgs = {}
    for x in ball(r + 1):
        for rho in near_rhos(r):
            p = pair(x, add(x, rho))
            q = W(p)
            if cheb(*tuple(q)) > r:
                return False
            if lexmin(q) != (0, 0, 0):
                continue
            if q in imgs and imgs[q] != p:
                return False
            imgs[q] = p
    return True


def inverse(W, r):
    inv = {}
    for x in ball(r + 1):
        for rho in near_rhos(r):
            p = pair(x, add(x, rho))
            q = W(p)
            m = lexmin(q)
            inv[normalise(q)] = frozenset(sub(s, m) for s in p)
    def Winv(q):
        m = lexmin(q)
        base = inv[normalise(q)]
        return frozenset(add(s, m) for s in base)
    return Winv


def spectator_relations(W, Winv, r):
    """All exact 3-magnon relations X -> Y forced by the spectator lemma (forward for U, backward for
    U^-1), up to translation (pair anchored at the origin)."""
    rel = []
    wr = 3 * r + 2
    for rho in near_rhos(r):
        p = pair((0, 0, 0), rho)
        for w in ball(wr, (0, 0, 0)):
            if w in p or dist_set(w, p) <= r:
                continue
            q = W(p)
            if w in q:
                continue  # cannot happen: W(p) lies in box(p) and w is far
            rel.append((p | {w}, q | {w}, 'F'))
            # backward: Y = p u {w} has spectator w for U^-1  ->  U^-1 Y = Winv(p) u {w}
            pi = Winv(p)
            rel.append((pi | {w}, p | {w}, 'B'))
    return rel


def consistency(rel):
    """the relations must form a partial bijection (U is a bijection on 3-magnon configs for a
    monomial W; for general W this is the isometry statement)."""
    byY, byX = {}, {}
    bad = []
    for X, Y, kind in rel:
        mY = lexmin(Y)
        kY = (frozenset(sub(s, mY) for s in Y))
        vX = frozenset(sub(s, mY) for s in X)
        if kY in byY and byY[kY][0] != vX:
            bad.append(('Y-collision', byY[kY], (vX, kind)))
        else:
            byY.setdefault(kY, (vX, kind))
        mX = lexmin(X)
        kX = frozenset(sub(s, mX) for s in X)
        vY = frozenset(sub(s, mX) for s in Y)
        if kX in byX and byX[kX][0] != vY:
            bad.append(('X-collision', byX[kX], (vY, kind)))
        else:
            byX.setdefault(kX, (vY, kind))
    return bad


def com2(S):
    """2 x centre of mass (integer)."""
    a = np.sum(np.array(list(S)), axis=0)
    return tuple(int(v) for v in a)


def cycle_displacements(W, r):
    """type permutation cycles of W and their net COM displacement (flat band iff all zero)."""
    out = []
    seen = set()
    for rho in near_rhos(r):
        if rho in seen:
            continue
        p = pair((0, 0, 0), rho)
        start = com2(p)
        cur = p
        length = 0
        while True:
            cur = W(cur)
            length += 1
            x, y = sorted(cur)
            c = canon_rho(sub(y, x))
            if c == rho:
                break
            seen.add(c)
        seen.add(rho)
        # cur is a translate of p
        disp = tuple((a - b) // 2 for a, b in zip(com2(cur), start))
        out.append((rho, length, disp))
    return out
