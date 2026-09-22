"""Exact Gaussian-rational lattice machinery (copied from a-bond-placed-stress-for-the-walk/w-jonathonsmac4f50-j1518/check.py)."""
import itertools
import random
from fractions import Fraction as F


class G:
    """Gaussian rational re + i im, exact."""
    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re = F(re); self.im = F(im)

    def __add__(self, o):
        o = gg(o); return G(self.re + o.re, self.im + o.im)
    __radd__ = __add__

    def __sub__(self, o):
        o = gg(o); return G(self.re - o.re, self.im - o.im)

    def __rsub__(self, o):
        return gg(o) - self

    def __mul__(self, o):
        o = gg(o); return G(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)
    __rmul__ = __mul__

    def __neg__(self):
        return G(-self.re, -self.im)

    def conj(self):
        return G(self.re, -self.im)

    def __eq__(self, o):
        o = gg(o); return self.re == o.re and self.im == o.im

    def __hash__(self):
        return hash((self.re, self.im))

    def __repr__(self):
        return f"({self.re}{'+' if self.im >= 0 else '-'}{abs(self.im)}i)"


def gg(x):
    return x if isinstance(x, G) else G(x, 0)


I = G(0, 1)
MINUS_I_HALF = G(0, F(-1, 2))                                        # 1/(2i)


def sig(a, u):
    u0, u1 = u
    if a == 0: return (u1, u0)
    if a == 1: return (-I * u1, I * u0)
    return (u0, -u1)


def inner(u, v):
    return u[0].conj() * v[0] + u[1].conj() * v[1]


class Torus:
    def __init__(self, dims):
        self.dims = dims
        self.sites = list(itertools.product(*[range(d) for d in dims]))
        self.index = {x: n for n, x in enumerate(self.sites)}
        self.N = len(self.sites)

    def nb(self, n, a, k):
        x = list(self.sites[n]); x[a] = (x[a] + k) % self.dims[a]
        return self.index[tuple(x)]

    def shift(self, f, a, k=1):
        return [f[self.nb(n, a, k)] for n in range(self.N)]

    def S(self, f, j):
        fp, fm = self.shift(f, j, 1), self.shift(f, j, -1)
        return [((fp[n][0] - fm[n][0]) * MINUS_I_HALF, (fp[n][1] - fm[n][1]) * MINUS_I_HALF) for n in range(self.N)]

    def H(self, f):
        out = [(G(), G()) for _ in range(self.N)]
        for a in range(3):
            Sa = self.S(f, a)
            out = [(o[0] + s[0], o[1] + s[1]) for o, s in zip(out, (sig(a, v) for v in Sa))]
        return out

    def J(self, psi, a, j, phi=None):
        """bond current of pi_j on the bond x -> x + e_a (exact, a Fraction per site)."""
        if phi is None: phi = self.S(psi, j)
        psa, pha = self.shift(psi, a), self.shift(phi, a)
        return [F(1, 2) * (inner(psa[n], sig(a, phi[n])) + inner(pha[n], sig(a, psi[n]))).re for n in range(self.N)]

    def back(self, f, a):
        fm = self.shift(f, a, -1)
        return [f[n] - fm[n] for n in range(self.N)]

    def fwd(self, f, a):
        fp = self.shift(f, a, 1)
        return [fp[n] - f[n] for n in range(self.N)]


def rand_state(T, rng, amp=3):
    return [(G(rng.randint(-amp, amp), rng.randint(-amp, amp)), G(rng.randint(-amp, amp), rng.randint(-amp, amp))) for _ in range(T.N)]


