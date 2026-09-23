"""Exact Gaussian-rational vectors on a torus: psi[x, c] with c the coin index; real and imaginary parts as Fraction object arrays."""
from fractions import Fraction as Fr
import numpy as np


class V:
    def __init__(self, re, im=None):
        self.re = re
        self.im = im if im is not None else np.full(re.shape, Fr(0), dtype=object)

    def __add__(self, o): return V(self.re + o.re, self.im + o.im)
    def __sub__(self, o): return V(self.re - o.re, self.im - o.im)
    def __neg__(self): return V(-self.re, -self.im)
    def scale(self, c):             # c complex rational given as (a, b)
        a, b = c
        return V(self.re * a - self.im * b, self.re * b + self.im * a)
    def times_i(self): return V(-self.im, self.re.copy())
    def mulfield(self, f):          # f real Fraction array over sites (shape L,L,L)
        return V(self.re * f[..., None], self.im * f[..., None])
    def roll(self, m):              # (T^m psi)(x) = psi(x + m)
        sh = tuple(-x for x in m)
        return V(np.roll(self.re, sh, axis=(0, 1, 2)), np.roll(self.im, sh, axis=(0, 1, 2)))
    def sigma(self, a):
        r, i = self.re, self.im
        if a == 0:   # sigma_x swaps
            return V(r[..., ::-1].copy(), i[..., ::-1].copy())
        if a == 1:   # sigma_y (u, d) -> (-i d, i u)
            nr = np.empty_like(r); ni = np.empty_like(i)
            nr[..., 0], ni[..., 0] = i[..., 1], -r[..., 1]
            nr[..., 1], ni[..., 1] = -i[..., 0], r[..., 0]
            return V(nr, ni)
        sg = np.array([Fr(1), Fr(-1)], dtype=object)
        return V(r * sg, i * sg)
    def zero_like(self): return V(np.full(self.re.shape, Fr(0), dtype=object))


def inner(u, v):
    """<u|v> as a pair (re, im)"""
    re = np.sum(u.re * v.re + u.im * v.im)
    im = np.sum(u.re * v.im - u.im * v.re)
    return (re, im)


def sitedens(u, v):
    """Re u(x)^dagger v(x) per site"""
    return np.sum(u.re * v.re + u.im * v.im, axis=-1)
