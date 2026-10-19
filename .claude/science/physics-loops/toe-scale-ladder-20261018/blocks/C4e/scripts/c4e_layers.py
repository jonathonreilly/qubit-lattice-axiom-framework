"""C4e construction: U = L2 o L1, each L_i a translation-invariant involution built from two-state
"units".  A unit u has a site set S_u and two disjoint states D_u, D'_u with D_u u D'_u = S_u;
crossing u swaps them (a permutation of S_u, hence number conserving).

  L1 units: unit squares (normal axis a, lower corner k): S = k + {0,e_b,e_c,e_b+e_c},
            D = {k, k+e_b+e_c}, D' = {k+e_b, k+e_c}      (the two face diagonals)
  L2 units: (unit cube with lower corner k, axis j): S = B(k) = the 4 cube sites whose parity
            differs from parity(k) (the "B-tetrahedron"), D = B(k) n {x_j = k_j}, D' = B(k) n {x_j = k_j+1}
            (two opposite, parallel edges of the B-tetrahedron, lying on the faces normal to e_j)

  candidate(u, c): c n S_u in {D_u, D'_u}
  N1(u) = units != u sharing a site with u;  N2(u) = units sharing a site with some unit of N1(u)
  active(u, c): (a) candidate;
                (b) for BOTH states of u (rest of c fixed) no unit of N1(u) is a candidate;
                (c) no unit of N2(u) \\ (N1(u) u {u}) is a candidate.
  L(c) = c with every active unit crossed.
A configuration is a set of occupied sites; `wrap` maps a site to its canonical representative
(identity on Z^3, or reduction mod L on a torus).
"""
import itertools

CUBE = list(itertools.product((0, 1), repeat=3))
def par(z): return (z[0] + z[1] + z[2]) & 1
def _add(a, b): return (a[0] + b[0], a[1] + b[1], a[2] + b[2])
def _sub(a, b): return (a[0] - b[0], a[1] - b[1], a[2] - b[2])
E = ((1, 0, 0), (0, 1, 0), (0, 0, 1))

class Layer:
    def __init__(self, kind, wrap=None):
        assert kind in ('square', 'tetra')
        self.kind = kind
        self.wrap = wrap or (lambda z: z)

    # ---- unit geometry; a unit is (axis, corner) with corner already wrapped
    def states(self, u):
        a, k = u; w = self.wrap
        if self.kind == 'square':
            b, c = [i for i in range(3) if i != a]
            D = (w(k), w(_add(_add(k, E[b]), E[c])))
            Dp = (w(_add(k, E[b])), w(_add(k, E[c])))
        else:
            B = [_add(k, d) for d in CUBE if (sum(d) & 1) == 1]   # parity differs from corner
            D = tuple(w(z) for z in B if z[a] == k[a])
            Dp = tuple(w(z) for z in B if z[a] == k[a] + 1)
        return frozenset(D), frozenset(Dp)

    def sites(self, u):
        D, Dp = self.states(u); return D | Dp

    def units_at(self, x):
        """all units containing site x"""
        w = self.wrap; out = []
        if self.kind == 'square':
            for a in range(3):
                b, c = [i for i in range(3) if i != a]
                for db in (0, 1):
                    for dc in (0, 1):
                        d = [0, 0, 0]; d[b] = db; d[c] = dc
                        out.append((a, w(_sub(x, tuple(d)))))
        else:
            for d in CUBE:
                if (sum(d) & 1) == 1:          # x - d has parity != parity(x)  => x in B(corner)
                    k = w(_sub(x, d))
                    for a in range(3): out.append((a, k))
        return out

    def N1(self, u):
        s = set()
        for x in self.sites(u): s.update(self.units_at(x))
        s.discard(u); return s

    def N2(self, u):
        n1 = self.N1(u); s = set()
        for v in n1:
            for x in self.sites(v): s.update(self.units_at(x))
        s -= n1; s.discard(u); return s

    # ---- dynamics
    def is_cand(self, u, occ):
        D, Dp = self.states(u); S = D | Dp
        inside = frozenset(z for z in S if z in occ)
        return inside == D or inside == Dp

    def candidates(self, occ):
        cand = set()
        for z in occ:
            for u in self.units_at(z):
                if u not in cand and self.is_cand(u, occ): cand.add(u)
        return cand

    def active(self, occ):
        occ = frozenset(occ)
        cand = self.candidates(occ)
        act = set()
        for u in cand:
            if any(v in cand for v in self.N2(u)): continue          # (c)
            D, Dp = self.states(u); base = occ - (D | Dp); ok = True
            for st in (D, Dp):                                        # (b)
                occ2 = base | st
                if any(self.is_cand(v, occ2) for v in self.N1(u)): ok = False; break
            if ok: act.add(u)
        return act

    def apply(self, occ, return_active=False):
        occ = frozenset(occ)
        act = self.active(occ)
        out = set(occ)
        for u in act:
            D, Dp = self.states(u)
            cur = D if D <= occ else Dp
            new = Dp if cur is D else D
            out -= cur; out |= new
        out = frozenset(out)
        return (out, act) if return_active else out

class U:
    def __init__(self, wrap=None):
        self.L1 = Layer('square', wrap); self.L2 = Layer('tetra', wrap)
    def __call__(self, occ): return self.L2.apply(self.L1.apply(occ))
    def inv(self, occ): return self.L1.apply(self.L2.apply(occ))
