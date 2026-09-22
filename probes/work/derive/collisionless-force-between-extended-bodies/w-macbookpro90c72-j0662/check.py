#!/usr/bin/env python3
"""J:derive:collisionless-force-between-extended-bodies:a3 -- checks and the extended-body prediction.

The unit's single-site law (independent records, gamma = 0, small density): the force on a transparent site at x
from a capturing site at 0 is -(rho/(4 pi sqrt3)) sum over the octants sigma that reach x of
sigma * E[Phi(W)]/((n+1)(n+2)), Phi(w) = w (w.w)^(-5/2), W ~ Dirichlet(|x|+1), n = |x|_1.  Units: rho/(4 pi sqrt3) = 1.
EXACT: the quadrature against exact Dirichlet moments (Fractions); the 1/n remainder of the law by the delta method
(sympy).  FLOATING POINT (labelled): the quadrature of Phi itself and the random-body averages.
"""
import sys
from fractions import Fraction as F
from itertools import product, permutations
import numpy as np
import sympy as sy
from scipy.special import roots_jacobi

OUT = []
FAIL = []


def rec(msg):
    OUT.append(msg)


def need(cond, msg):
    if not cond:
        FAIL.append(msg)


def beta_rule(a, b, m):
    """E over Beta(a, b) on [0, 1] by Gauss-Jacobi (exact for polynomials of degree < 2m)"""
    x, w = roots_jacobi(m, b - 1, a - 1)
    return (x + 1) / 2, w / w.sum()


def dirichlet_nodes(al, m=40):
    t, wt = beta_rule(al[0], al[1] + al[2], m)                # W1 ~ Beta(a1, a2+a3), (W2, W3)/(1-W1) ~ Beta(a2, a3)
    s, ws = beta_rule(al[1], al[2], m)
    T, S = np.meshgrid(t, s, indexing="ij")
    return (T, (1 - T) * S, (1 - T) * (1 - S)), np.outer(wt, ws)


# ---------------------------------- S1 the quadrature against exact Dirichlet moments
def exact_moment(al, e):
    num, den, A = 1, 1, sum(al)
    for a, k in zip(al, e):
        for j in range(k):
            num *= a + j
    for j in range(sum(e)):
        den *= A + j
    return F(num, den)


worst = 0.0
for al in ((1, 1, 1), (3, 1, 2), (11, 21, 21), (29, 2, 2), (17, 13, 5)):
    Wn, Wg = dirichlet_nodes(al)
    for e in ((1, 0, 0), (2, 1, 0), (3, 3, 2), (0, 5, 1), (4, 4, 4), (9, 0, 7)):
        q = (Wg * Wn[0] ** e[0] * Wn[1] ** e[1] * Wn[2] ** e[2]).sum()
        ex = exact_moment(al, e)
        worst = max(worst, abs(q - float(ex)) / float(ex))
need(worst < 1e-12, "S1 quadrature")
rec("ok S1 the simplex quadrature (Gauss-Jacobi, 40x40 nodes) reproduces exact Dirichlet moments "
    "prod (a_i)_(e_i)/(A)_(E) to %.1e relative, on five parameter sets and six monomials each" % worst)

_EC = {}


def E_phi(ax):
    key = tuple(int(t) for t in ax)
    if key not in _EC:
        Wn, Wg = dirichlet_nodes([k + 1 for k in key])
        f = (Wn[0] ** 2 + Wn[1] ** 2 + Wn[2] ** 2) ** -2.5
        _EC[key] = np.array([(Wg * Wn[i] * f).sum() for i in range(3)])
    return _EC[key]


SIGNS = [np.array(s) for s in product((-1, 1), repeat=3)]


def force(x):
    x = np.asarray(x)
    n = int(np.abs(x).sum())
    ep = E_phi(np.abs(x))
    tot = np.zeros(3)
    for sg in SIGNS:
        if np.all(sg * x >= 0):
            tot += sg * ep
    return -tot / ((n + 1) * (n + 2))


def lead(x):
    x = np.asarray(x, float)
    n, r = np.abs(x).sum(), np.linalg.norm(x)
    return -(2 ** int(np.sum(x == 0))) * x * n ** 2 / r ** 5


# ---------------------------------- S2 the law's 1/n remainder, exactly (delta method)
y = sy.symbols("y1:4", positive=True)
wv = sy.Matrix(y)
rr = sy.sqrt(sum(t ** 2 for t in y))
Phi = wv / rr ** 5


def c_coef(yv):
    """lim n (|F| - |lead|)/|lead| along the direction yv (|yv|_1 = 1):
    mean shift (1 - 3y)/n, covariance (diag y - y y^T)/n, prefactor 1 - 3/n"""
    sub = dict(zip(y, yv))
    P0 = Phi.subs(sub)
    grad = Phi.jacobian(wv)
    shift = (grad * sy.Matrix([1 - 3 * t for t in y])).subs(sub)
    Sig = (sy.diag(*y) - wv * wv.T)
    second = sy.Matrix([sum(Sig[i, j] * sy.diff(Phi[k], y[i], y[j]) for i in range(3) for j in range(3))
                        for k in range(3)]).subs(sub).subs(sub) / 2
    Pn = P0 / sy.sqrt((P0.T * P0)[0])
    return sy.nsimplify(sy.simplify(-3 + ((Pn.T * (shift + second))[0]) / sy.sqrt((P0.T * P0)[0])))


c111 = c_coef([sy.Rational(1, 3)] * 3)
c122 = c_coef([sy.Rational(1, 5), sy.Rational(2, 5), sy.Rational(2, 5)])
c2811 = sy.simplify(c_coef([sy.Rational(28, 30), sy.Rational(1, 30), sy.Rational(1, 30)]))
ok = c111 == -8 and c122 == sy.Rational(-481, 81) and c2811 == sy.Rational(167603, 34322)
num_ok = True                                                 # floating point: the quadrature approaches them
for base, cv in (((1, 1, 1), c111), ((1, 2, 2), c122), ((28, 1, 1), c2811)):
    devs = []
    for k in ((16, 32) if base != (28, 1, 1) else (8, 16)):
        x = np.array(base) * k
        f_, l_ = force(x), lead(x)
        devs.append((np.linalg.norm(f_) - np.linalg.norm(l_)) / np.linalg.norm(l_) * np.abs(x).sum())
    num_ok &= abs(devs[-1] - float(cv)) < abs(devs[0] - float(cv)) + 1e-9 and abs(devs[-1] - float(cv)) < 1.0
need(ok and num_ok, "S2 remainder")
rec("ok S2 the law's relative remainder is c/|x|_1 + O(|x|_1^-2) with c exact by the delta method: c = %s towards "
    "(1,1,1), %s towards (1,2,2), %s = %.4f towards (28,1,1) (the quadrature approaches each: floating point); the "
    "unit's ESTABLISHED values -24, -16, +5.6 are not the stated law's" % (c111, c122, c2811, float(c2811)))

# ---------------------------------- S3 the law's symmetry and multiplicities (floating point, to rounding)
cube = []
for perm in permutations(range(3)):
    for sg in product((-1, 1), repeat=3):
        Mg = np.zeros((3, 3))
        for i in range(3):
            Mg[i, perm[i]] = sg[i]
        cube.append(Mg)
rng = np.random.default_rng(7)
sym_err = 0.0
for _ in range(40):
    x = rng.integers(-9, 10, 3)
    if not x.any():
        continue
    for Mg in cube:
        gx = (Mg @ x).astype(int)
        sym_err = max(sym_err, np.abs(force(gx) - Mg @ force(x)).max())
m_ok = (np.allclose(force((5, 0, 0))[1:], 0) and np.allclose(force((5, 3, 0))[2], 0))
need(sym_err < 1e-12 and m_ok, "S3 symmetry")
rec("ok S3 (floating point) the law is covariant under all 48 cube symmetries to %.0e; on a coordinate plane the "
    "force stays in the plane and on an axis along it (two and four octants reach the site)" % sym_err)

# ---------------------------------- S4 two random bodies (floating point)
ball = np.array([p for p in product(range(-6, 7), repeat=3) if p[0] ** 2 + p[1] ** 2 + p[2] ** 2 <= 36])
DIRS = {"(1,0,0)": np.array([16, 0, 0]), "(1,1,0)": np.array([11, 11, 0]), "(1,1,1)": np.array([9, 9, 9])}
NB, SAMPLES = 20, 200
res = {}
for nm, d in DIRS.items():
    r = np.linalg.norm(d)
    dh = d / r
    vals, lvals = [], []
    for _ in range(SAMPLES):
        b1 = ball[rng.choice(len(ball), NB, replace=False)]
        b2 = ball[rng.choice(len(ball), NB, replace=False)] + d
        Ftot = np.zeros(3)
        Ltot = np.zeros(3)
        for p1 in b1:
            for p2 in b2:
                Ftot += force(p2 - p1)
                Ltot += lead(p2 - p1)
        vals.append(-Ftot @ dh * r ** 2 / NB ** 2)
        lvals.append(-Ltot @ dh * r ** 2 / NB ** 2)
    vals = np.array(vals)
    point = (2 ** int(np.sum(d == 0))) * (np.abs(d).sum() / r) ** 2
    res[nm] = (vals.mean(), vals.std() / np.sqrt(SAMPLES), np.mean(lvals), point)
# the mean over random positions exactly: the sum is over pairs, so E[force] = N1 N2 <F(p2 - p1 + d)> over the pair
# offsets of two uniform balls, whose counts are the ball's integer autocorrelation
from scipy.signal import correlate
ind = np.zeros((13, 13, 13), dtype=np.int64)
for p in ball:
    ind[tuple(p + 6)] = 1
auto = correlate(ind, ind, mode="full", method="direct")      # offsets -12..12, exact integer counts
need(int(auto.sum()) == len(ball) ** 2, "S4 autocorrelation")
for nm, d in DIRS.items():
    r = np.linalg.norm(d)
    dh = d / r
    tot = 0.0
    for off in zip(*np.nonzero(auto)):
        delta = np.array(off) - 12
        tot += auto[off] * (-force(delta + d) @ dh)
    res[nm] = res[nm] + (tot * r ** 2 / len(ball) ** 2,)
ok = all(v[0] > 0 and abs(v[0] - v[4]) < 4 * v[1] for v in res.values())
need(ok, "S4 attraction and the exact mean")
rec("ok S4 (floating point; %d random pairs of %d-site bodies in balls of radius 6, centres at (16,0,0), (11,11,0), "
    "(9,9,9)) the attraction along the separation, times r^2/(N1 N2), in units rho/(4 pi sqrt3): " % (SAMPLES, NB)
    + "; ".join("%s mean over positions %.4f (sampled %.3f +- %.3f; leading law %.3f; point pair %.0f)"
                % (k, v[4], v[0], v[1], v[2], v[3]) for k, v in res.items())
    + "; ratios to (1,0,0): %.4f and %.4f; the collisional law gives 9/4 in every direction"
    % (res["(1,1,0)"][4] / res["(1,0,0)"][4], res["(1,1,1)"][4] / res["(1,0,0)"][4]))

print("\n".join(OUT))
print("SUMMARY: " + ("ROUTE FAILS AT " + FAIL[0] if FAIL else
      "PARTIAL the stated single-site law, summed over all site pairs of two 20-site bodies at random positions in "
      "balls of radius 6 (separation about 16), predicts mean attraction factors %.3f, %.3f, %.3f along (1,0,0), "
      "(1,1,0), (1,1,1) (floating point; configuration spread %.2f), against 9/4 for the collisional law: nearly "
      "isotropic; the law's exact 1/n remainder coefficients are -8 (diagonal), "
      "-481/81 towards (1,2,2) and 167603/34322 towards (28,1,1), not the -24, -16, +5.6 the unit quotes."
      % (res["(1,0,0)"][4], res["(1,1,0)"][4], res["(1,1,1)"][4], max(v[1] for v in res.values()) * np.sqrt(SAMPLES))))
if not FAIL:
    print("HIT: the unit's single-site law (sum over reaching octants of E[Phi(W)]/((n+1)(n+2)), W ~ Dirichlet(|x|+1)) "
          "has relative remainder c/|x|_1 + O(|x|_1^-2) with c = -3 + [shift + covariance terms] exactly by the "
          "delta method: c = -8 on the body diagonal, -481/81 towards (1,2,2) and 167603/34322 towards (28,1,1), "
          "not the -24, -16 and +5.6 the unit quotes as established.")
sys.exit(1 if FAIL else 0)
