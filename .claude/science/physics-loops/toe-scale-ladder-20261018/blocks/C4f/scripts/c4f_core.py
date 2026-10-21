"""C4f construction (sparse implementation, Z^3 or torus via `wrap`).

U = L2 o L1.
  L1 (squares): exactly C4e's square layer. Unit (sq, a, k): S = k + {0, e_b, e_c, e_b+e_c},
      D = {k, k+e_b+e_c}, D' = {k+e_b, k+e_c}; no control (Gamma = empty set, F = S).
  L2 (controlled tetra-axes), ONE family with two kinds of units, cube K(k) = k + {0,1}^3:
      B(k) = sites of K(k) with parity != par(k);  A(k) = K(k) \\ B(k).
      (B, j, k): S = B(k), D = B(k) n {x_j=k_j}, D' = B(k) n {x_j=k_j+1}, Gamma = A(k), control EMPTY
      (A, j, k): S = A(k), D = A(k) n {x_j=k_j}, D' = A(k) n {x_j=k_j+1}, Gamma = B(k), control FULL
      read set F = S u Gamma = K(k).
  candidate(u,c): c n S_u in {D_u, D'_u} and (control EMPTY: c n Gamma = 0 / FULL: Gamma subset c)
  N1(u) = {w != u in the same layer : F_w n S_u != 0  or  F_u n S_w != 0}
  N2(u) = U_{w in N1(u)} N1(w)  minus N1(u) minus {u}
  active(u,c): (a) candidate; (b) for both states of u (rest fixed) no unit of N1(u) is a candidate;
               (c) no unit of N2(u) is a candidate.
  L(c) = c with every active unit crossed.

For squares F = S, so N1/N2 reduce to C4e's site-sharing definition.
A configuration is a frozenset of occupied sites (wrapped); `wrap` = identity (Z^3) or mod L (torus).
"""
import itertools

CUBE = list(itertools.product((0, 1), repeat=3))
E = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
def par(z): return (z[0] + z[1] + z[2]) & 1
def add(a, b): return (a[0] + b[0], a[1] + b[1], a[2] + b[2])
def sub(a, b): return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def unit_geom(u):
    """unwrapped (D, D', Gamma, control) of unit u = (kind, axis, corner)."""
    kind, a, k = u
    if kind == 'sq':
        b, c = [i for i in range(3) if i != a]
        D = (k, add(add(k, E[b]), E[c]))
        Dp = (add(k, E[b]), add(k, E[c]))
        return D, Dp, (), None
    odd = [add(k, d) for d in CUBE if sum(d) & 1]
    even = [add(k, d) for d in CUBE if not sum(d) & 1]
    S, G, ctl = (odd, even, 'empty') if kind == 'B' else (even, odd, 'full')
    D = tuple(z for z in S if z[a] == k[a])
    Dp = tuple(z for z in S if z[a] == k[a] + 1)
    return D, Dp, tuple(G), ctl


def _units_S_at(kinds, x):
    out = []
    for kind in kinds:
        if kind == 'sq':
            for a in range(3):
                b, c = [i for i in range(3) if i != a]
                for db in (0, 1):
                    for dc in (0, 1):
                        d = [0, 0, 0]; d[b] = db; d[c] = dc
                        out.append(('sq', a, sub(x, tuple(d))))
        else:
            want = 1 if kind == 'B' else 0
            for d in CUBE:
                if (sum(d) & 1) == want:
                    for a in range(3): out.append((kind, a, sub(x, d)))
    return out


def _units_F_at(kinds, x):
    out = []
    for kind in kinds:
        if kind == 'sq':
            out += _units_S_at(('sq',), x)
        else:
            for d in CUBE:
                for a in range(3): out.append((kind, a, sub(x, d)))
    return out


class Layer:
    def __init__(self, kinds, wrap=None):
        self.kinds = tuple(kinds)
        self.wrap = wrap or (lambda z: z)
        self._n1 = {}; self._n2 = {}

    # unwrapped neighbourhood offsets, computed from the definition by brute force on Z^3
    def _N1_raw(self, u):
        key = (u[0], u[1])
        if key not in self._n1:
            u0 = (u[0], u[1], (0, 0, 0))
            D, Dp, G, _ = unit_geom(u0)
            S = set(D) | set(Dp); F = S | set(G)
            cand = set()
            for x in S: cand.update(_units_F_at(self.kinds, x))     # F_w n S_u != 0
            for x in F: cand.update(_units_S_at(self.kinds, x))     # F_u n S_w != 0
            res = set()
            for w in cand:                                            # re-verify by direct test
                Dw, Dpw, Gw, _ = unit_geom(w)
                Sw = set(Dw) | set(Dpw); Fw = Sw | set(Gw)
                if w != u0 and (Fw & S or F & Sw): res.add(w)
            self._n1[key] = res
        k = u[2]
        return {(w[0], w[1], add(w[2], k)) for w in self._n1[key]}

    def _N2_raw(self, u):
        key = (u[0], u[1])
        if key not in self._n2:
            u0 = (u[0], u[1], (0, 0, 0))
            n1 = self._N1_raw(u0); s = set()
            for w in n1: s |= self._N1_raw(w)
            s -= n1; s.discard(u0)
            self._n2[key] = s
        k = u[2]
        return {(w[0], w[1], add(w[2], k)) for w in self._n2[key]}

    def W(self, u):
        return (u[0], u[1], self.wrap(u[2]))

    def N1(self, u): return {self.W(w) for w in self._N1_raw(u)}
    def N2(self, u): return {self.W(w) for w in self._N2_raw(u)}

    def geom(self, u):
        D, Dp, G, ctl = unit_geom(u); w = self.wrap
        return frozenset(map(w, D)), frozenset(map(w, Dp)), frozenset(map(w, G)), ctl

    def is_cand(self, u, occ):
        D, Dp, G, ctl = self.geom(u)
        inside = (D | Dp) & occ
        if inside != D and inside != Dp: return False
        if ctl == 'empty': return not (G & occ)
        if ctl == 'full': return G <= occ
        return True

    def candidates(self, occ):
        cand = set(); seen = set()
        for z in occ:
            for u in _units_S_at(self.kinds, z):
                u = self.W(u)
                if u in seen: continue
                seen.add(u)
                if self.is_cand(u, occ): cand.add(u)
        return cand

    def active(self, occ):
        occ = frozenset(occ)
        cand = self.candidates(occ)
        act = set()
        for u in cand:
            if self.N2(u) & cand: continue                                   # (c)
            n1 = self.N1(u)
            if n1 & cand: continue                                           # (b), current state
            D, Dp, G, ctl = self.geom(u)
            cur = D if D <= occ else Dp
            other = (occ - cur) | (Dp if cur is D else D)
            if any(self.is_cand(v, other) for v in n1): continue             # (b), other state
            act.add(u)
        return act

    def apply(self, occ, return_active=False):
        occ = frozenset(occ)
        act = self.active(occ)
        out = set(occ)
        for u in act:
            D, Dp, G, ctl = self.geom(u)
            cur = D if D <= occ else Dp
            out -= cur; out |= (Dp if cur is D else D)
        out = frozenset(out)
        return (out, act) if return_active else out


class Dyn:
    """U = L2 o L1.  variant='C4f' (controlled B/A family) or 'C4e' (plain B tetra-axes, no control)."""
    def __init__(self, wrap=None, variant='C4f'):
        self.L1 = Layer(('sq',), wrap)
        if variant == 'C4f':
            self.L2 = Layer(('B', 'A'), wrap)
        else:
            self.L2 = _C4eTetra(wrap)
    def __call__(self, occ): return self.L2.apply(self.L1.apply(occ))
    def inv(self, occ): return self.L1.apply(self.L2.apply(occ))


class _C4eTetra(Layer):
    """C4e's L2 (B tetra-axes, no control) for comparison."""
    def __init__(self, wrap=None):
        super().__init__(('B',), wrap)
    def geom(self, u):
        D, Dp, G, ctl = super().geom(u)
        return D, Dp, frozenset(), None
    def _N1_raw(self, u):
        key = (u[0], u[1])
        if key not in self._n1:
            u0 = (u[0], u[1], (0, 0, 0))
            D, Dp, _, _ = unit_geom(u0); S = set(D) | set(Dp)
            res = set()
            for x in S: res.update(_units_S_at(('B',), x))
            res.discard(u0); self._n1[key] = res
        k = u[2]
        return {(w[0], w[1], add(w[2], k)) for w in self._n1[key]}


# ---------------------------------------------------------------- group O and the axis action
def build_O():
    import numpy as np
    O = []
    for p in itertools.permutations(range(3)):
        for s in itertools.product((1, -1), repeat=3):
            M = np.zeros((3, 3), int)
            for i in range(3): M[p[i], i] = s[i]
            if round(np.linalg.det(M)) == 1: O.append(M)
    return O

def perm_sign(M):
    import numpy as np
    return int(round(np.linalg.det(np.abs(M))))

def rot(M, z):
    return tuple(int(sum(M[i][j] * z[j] for j in range(3))) for i in range(3))
