"""R2-6 (b)(c)(d)(e): Snyder momentum composition on dS_4 = SO(4,1)/SO(3,1).

Momentum space: X in R^{1,4}, G = diag(-1,1,1,1,1), X.X = 1/a^2, origin O = e4/a.
Plane waves e^{i k.xhat} = exp(W(k)), W(k) = a (kappa e4^T G - e4 kappa^T G),
kappa = (k^0,k^1,k^2,k^3,0): these are the transvections (coset exponentials).
Composition (Weyl/exponential section, Girelli-Livine / Battisti-Meljanac form):
    g(k) g(q) = g(k (+) q) h,   h in SO(3,1)  (fixes O).
Momentum labels k are normal (geodesic) coordinates; any Lorentz-covariant
relabelling p = f(k^2) k (e.g. Snyder's projective chart) leaves every ratio
p_i/p_0 (velocity) and every invariant unchanged.

Checks:
 C1  g(k)O equals the closed-form geodesic point; h fixes O; Lorentz covariance
     L(k(+)q) = Lk (+) Lq.
 C2  non-commutativity and non-associativity at O(a^2 k^3); BCH prediction
     k(+)q = k + q - (1/6)[X,[X,Y]] - (1/3)[Y,[X,Y]] (projected), residual O(a^4).
 C3  collinear momenta add exactly (normal coordinates).
 C4  "body as one Snyder particle" (mapping A): response to a soft spatial kick
     q on a body at rest of mass M: left P(+)q gives v = a q / sinh(aM),
     right q(+)P gives v = a q coth(aM).
 C5  N-constituent body at rest with internal (Fermi) momenta: spurious total
     spatial momentum and ordering ambiguity vs N (sequential and tree bracketings).
 C6  Lemma W test: equal-mass 2->2 on the (+)-conservation surface; the linear
     law k1+k2 = k3+k4 fails at O(a^2 k^3); k1(+)k2 is not parallel to k1+k2.
 C7  free-particle worldline velocity in the Snyder realisation (sympy).
"""
import numpy as np
from scipy.linalg import expm
import sympy as sp

rng = np.random.default_rng(20261012)
G5 = np.diag([-1.0, 1, 1, 1, 1])
eta4 = np.diag([-1.0, 1, 1, 1])
e4 = np.array([0, 0, 0, 0, 1.0])


def dot4(u, v):
    return u @ eta4 @ v


def W(k, a):
    kap = np.concatenate([k, [0.0]])
    return a * (np.outer(kap, e4) @ G5 - np.outer(e4, kap) @ G5)


def g(k, a):
    return expm(W(k, a))


def point(k, a):
    """closed form geodesic point from O with normal coords k."""
    k2 = dot4(k, k)
    kap = np.concatenate([k, [0.0]])
    O = e4 / a
    if k2 < 0:
        mu = np.sqrt(-k2)
        return np.cosh(a * mu) * O + np.sinh(a * mu) / (a * mu) * kap
    elif k2 > 0:
        lam = np.sqrt(k2)
        return np.cos(a * lam) * O + np.sin(a * lam) / (a * lam) * kap
    return O + kap


def log_pt(X, a):
    """normal coordinates of a dS point X reachable from O."""
    v = X[:4]
    vv = dot4(v, v)
    if vv < 0:
        s = a * np.sqrt(-vv)
        if X[4] <= 0:
            raise ValueError("timelike point not reachable by a geodesic from O")
        return v * np.arcsinh(s) / s
    elif vv > 0:
        s = a * np.sqrt(vv)
        th = np.arctan2(s, a * X[4])
        return v * th / s
    return v.copy()


def oplus(k, q, a):
    return log_pt(g(k, a) @ g(q, a) @ (e4 / a), a)


def lorentz(rap, axis, rot):
    """a Lorentz transform in SO(3,1) embedded in 5D (fixes e4)."""
    M = np.zeros((5, 5))
    M[0, axis] = M[axis, 0] = 1.0
    B = expm(rap * M)
    R = np.eye(5)
    c, s = np.cos(rot), np.sin(rot)
    R[1:3, 1:3] = [[c, -s], [s, c]]
    return B @ R


def onshell(m, kv):
    return np.array([np.sqrt(m * m + kv @ kv), *kv])


