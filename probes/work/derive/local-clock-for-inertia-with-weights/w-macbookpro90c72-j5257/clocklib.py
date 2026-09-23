"""Shared machinery for check.py and make_data.py (J:derive:local-clock-for-inertia-with-weights:a1).

Block 50's objects (PR 'ail50', supervisor_control_block50_refuter.py): six-axis contents 0..5 = +x,-x,+y,-y,+z,-z on the L^3
torus; pi(C) = product over adjacent occupied pairs of c omega(a, b), omega = p, q, r for equal, opposite, orthogonal;
inertial streaming: the record at x with content s targets x + e_s, enters it if empty, exchanges contents if it is occupied.
A LOCAL rate is a function of the contents and occupancies of the sites within distance one of x or its target, taken up to
the eight lattice symmetries that fix the event (x, e_s) - its canonical ENVIRONMENT. Optional extra event ('rot'): a
head-on pair (target holds -s) re-draws on its momentum class to (a, -a) along a transverse axis a (four outcomes).
Balance at C: sum of pi(C) r(event) over the events of C = sum of pi(C'') r(event) over the events that lead into C."""
import itertools
from itertools import combinations, product
from fractions import Fraction as Fr

E = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
GROUP = [(perm, sg) for perm in itertools.permutations(range(3)) for sg in product((1, -1), repeat=3)]
BASE = [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (2, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1),
        (1, 1, 0), (1, -1, 0), (1, 0, 1), (1, 0, -1)]          # in the frame where the event is along +x: index 1 = target


def gvec(g, v):
    perm, sg = g
    w = [0, 0, 0]
    for i in range(3):
        w[perm[i]] = sg[i] * v[i]
    return tuple(w)


CON_OF = {E[c]: c for c in range(6)}


class Torus:
    def __init__(self, L):
        self.L = L
        self.SITES = list(product(range(L), repeat=3))
        self.IDX = {x: i for i, x in enumerate(self.SITES)}
        self.N = L ** 3
        self.NB = [[self.add(x, d) for d in E] for x in self.SITES]
        self.FR = {}
        for x in range(self.N):
            for s in range(6):
                lst = []
                for g in GROUP:
                    if gvec(g, E[s]) != (1, 0, 0):
                        continue
                    perm, sg = g
                    sites, seen = [], set()
                    for d in BASE:
                        r = [sg[i] * d[perm[i]] for i in range(3)]
                        site = self.add(self.SITES[x], r)
                        if site in seen:
                            continue                     # L = 3: 2 e_s is -e_s
                        seen.add(site)
                        sites.append(site)
                    lst.append((sites, [CON_OF[gvec(g, E[c])] for c in range(6)]))
                self.FR[(x, s)] = lst

    def add(self, x, d):
        return self.IDX[tuple((x[i] + d[i]) % self.L for i in range(3))]

    def env(self, occ, x):
        best = None
        for sites, gc in self.FR[(x, occ[x])]:
            key = tuple(gc[occ[t]] if occ[t] >= 0 else -1 for t in sites)
            if best is None or key < best:
                best = key
        return best

    def rot(self, occ, x, a):
        best = None
        for sites, gc in self.FR[(x, occ[x])]:
            key = (tuple(gc[occ[t]] if occ[t] >= 0 else -1 for t in sites), gc[a])
            if best is None or key < best:
                best = key
        return ('rot',) + best

    def weight(self, occ, w, one=1):
        """pi(C): product over adjacent occupied pairs (scans only occupied sites); w entries Fractions or floats"""
        val = one
        occd = [a for a in range(self.N) if occ[a] >= 0]
        for a in occd:
            for b in self.NB[a]:
                if b > a and occ[b] >= 0:
                    c1, c2 = occ[a], occ[b]
                    val *= w[0] if c1 == c2 else (w[1] if c1 == (c2 ^ 1) else w[2])
        return val

    def own(self, occ, x, w):
        val = Fr(1)
        for b in self.NB[x]:
            if occ[b] >= 0:
                c1, c2 = occ[x], occ[b]
                val *= w[0] if c1 == c2 else (w[1] if c1 == (c2 ^ 1) else w[2])
        return val

    def configs(self, nrec):
        for rest in combinations(range(1, self.N), nrec - 1):
            pos = (0,) + rest
            for con in product(range(6), repeat=nrec):
                occ = [-1] * self.N
                for p_, c_ in zip(pos, con):
                    occ[p_] = c_
                yield pos, con, occ

    def terms(self, pos, occ, mode='base'):
        """(key, sign, config) : sign +1 an event out of C (config None), -1 an event into C from config"""
        out = []
        for x in pos:
            s = occ[x]
            t = self.NB[x][s]
            out.append((self.env(occ, x), +1, None))
            if mode == 'rot' and occ[t] == (s ^ 1):
                for a in range(6):
                    if a // 2 != s // 2:
                        out.append((self.rot(occ, x, a), +1, None))
            behind = self.NB[x][s ^ 1]
            occ2 = list(occ)
            if occ[behind] >= 0:
                occ2[behind], occ2[x] = occ[x], occ[behind]
            else:
                occ2[behind] = s
                occ2[x] = -1
            out.append((self.env(occ2, behind), -1, occ2))
        if mode == 'rot':
            for x in pos:
                for di in (0, 2, 4):
                    y = self.NB[x][di]
                    c = occ[x]
                    if occ[y] >= 0 and occ[y] == (c ^ 1) and c // 2 != di // 2:
                        occ3 = list(occ)
                        occ3[x] = di
                        occ3[y] = di ^ 1
                        for actor, a_out in ((x, c), (y, occ[y])):
                            out.append((self.rot(occ3, actor, a_out), -1, occ3))
        return out

    def row(self, pos, occ, w, mode='base', one=1):
        pi = self.weight(occ, w, one)
        acc = {}
        for key, sg, o2 in self.terms(pos, occ, mode):
            acc[key] = acc.get(key, 0) + (pi if sg > 0 else -self.weight(o2, w, one))
        return {k: v for k, v in acc.items() if v != 0}


def is_move(key):
    return key[0] != 'rot' and key[1] == -1


def kstr(key):
    return repr(key)
