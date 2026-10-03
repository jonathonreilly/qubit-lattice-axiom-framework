"""Exact Pauli-string algebra with phases.

P = i^k * prod_s X_s^{bx_s} Z_s^{bz_s}   (X written before Z at each site)
sigma^y = i X Z.
"""
import numpy as np
from grp import label_map


class P:
    __slots__ = ("k", "s")

    def __init__(self, k=0, s=None):
        self.k = k % 4
        self.s = {} if s is None else {v: b for v, b in s.items() if b != (0, 0)}

    @staticmethod
    def single(site, a, sign=1):
        """sign * sigma^a at site (a in 0,1,2)."""
        k = 0 if sign == 1 else 2
        if a == 0:
            return P(k, {site: (1, 0)})
        if a == 2:
            return P(k, {site: (0, 1)})
        return P(k + 1, {site: (1, 1)})

    def __mul__(self, o):
        k = self.k + o.k
        s = dict(self.s)
        for v, (c, d) in o.s.items():
            a, b = s.get(v, (0, 0))
            # (X^a Z^b)(X^c Z^d) = (-1)^{b c} X^{a+c} Z^{b+d}
            if b and c:
                k += 2
            s[v] = ((a + c) % 2, (b + d) % 2)
        return P(k, s)

    def key(self):
        return (self.k, tuple(sorted(self.s.items())))

    def __eq__(self, o):
        return self.key() == o.key()

    def __hash__(self):
        return hash(self.key())

    def commutes(self, o):
        t = 0
        for v, (a, b) in self.s.items():
            if v in o.s:
                c, d = o.s[v]
                t += a * d + b * c
        return t % 2 == 0

    def is_hermitian(self):
        ny = sum(1 for b in self.s.values() if b == (1, 1))
        # i^k X..Z.. with ny sites XZ: hermitian iff k - ny even  (XZ)^dag = ZX = -XZ
        return (self.k - ny) % 2 == 0

    def translate(self, t):
        return P(self.k, {tuple(int(c) for c in np.add(v, t)): b for v, b in self.s.items()})

    def __repr__(self):
        ny = sum(1 for b in self.s.values() if b == (1, 1))
        ph = ["+", "+i", "-", "-i"][(self.k - ny) % 4]   # phase relative to sigma's (XZ = -i Y)
        items = sorted(self.s.items())
        return ph + " ".join(f"{'IXZY'[b[0] + 2 * b[1]]}{tuple(int(c) for c in v)}" for v, b in items)


def rotate(p, R):
    """Exact soldered rotation of a Pauli string: sites v->Rv, sigma^a -> eps sigma^{pi a}.
    Implemented by decomposing each site factor into sigma's."""
    pi, eps = label_map(R)
    out = P(p.k, {})
    for v, (bx, bz) in sorted(p.s.items()):
        w = tuple(int(c) for c in R @ np.array(v))
        # X^bx Z^bz expressed via sigma's: X=s^x, Z=s^z, XZ = -i s^y
        if (bx, bz) == (1, 0):
            fac = P.single(w, pi[0], eps[0])
        elif (bx, bz) == (0, 1):
            fac = P.single(w, pi[2], eps[2])
        else:  # XZ = -i sigma^y
            fac = P(3, {}) * P.single(w, pi[1], eps[1])
        out = out * fac
    return out
