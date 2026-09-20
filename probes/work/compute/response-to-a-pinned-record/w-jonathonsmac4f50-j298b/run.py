#!/usr/bin/env python3
"""C:response-to-a-pinned-record:a2   worker w-jonathonsmac4f50-j298b (claude-opus-5)

Response against fluctuation in level time, for the linear gain-one formation model on Z^(d+1), d = 2 and 3:
pin one record at the origin to theta = 1 and propagate the mean, theta(x) = average of the d+1 predecessors.

A1  the response is the multinomial probability n!/(prod a_i!) (d+1)^{-n}; exact propagation check
A2  asymptotics: peak (2 pi n)^{-d/2} (d+1)^{(d+1)/2} on the axis, Gaussian widths across and along it
A3  the equal-level covariance sigma^2/(1-u) is the plane's Green function (log in d = 2, 1/r in d = 3)
A4  how the two differ, and an exact proof that no constant relates them
N1  numerical fits and the ratios
"""
import time
from fractions import Fraction
from itertools import product
from math import comb, factorial, pi, sqrt, log
import numpy as np
import sympy as sp

t0 = time.time()
print("A0 overlap disclosure: I also ran C:two-point-function-response-table:a1, which measured this response in")
print("A0 the sphere law by coupled pairs; here everything is the exact mean propagation and is independent of it.")

# ---------------------------------------------------------------- A1 the multinomial response
def propagate(d, N):
    """exact mean response after n = 0..N levels, dict (a_1..a_d) -> Fraction, starting from a pinned 1"""
    n1 = d + 1
    cur = {tuple([0] * d): Fraction(1)}
    out = [cur]
    for n in range(1, N + 1):
        nxt = {}
        for y, v in cur.items():
            for j in range(-1, d):
                z = list(y)
                if j >= 0: z[j] += 1
                z = tuple(z)
                nxt[z] = nxt.get(z, Fraction(0)) + v / n1
        cur = nxt; out.append(cur)
    return out
for d in (2, 3):
    N = 12
    levels = propagate(d, N)
    ok = True; checked = 0
    for n in range(N + 1):
        for y, v in levels[n].items():
            a0 = n - sum(y)
            if a0 < 0: ok = False; continue
            mult = Fraction(factorial(n), factorial(a0))
            for ai in y: mult /= factorial(ai)
            if v != mult / Fraction(d + 1) ** n: ok = False
            checked += 1
    tot = all(sum(levels[n].values()) == 1 for n in range(N + 1))
    print(f"A1 d={d}: propagating the mean to level {N} reproduces n!/(a_0! prod a_i!) (d+1)^-n at all {checked} "
          f"points exactly: {ok}; every level sums to 1: {tot}")
    print(f"A1 d={d}: the support is the forward cone a_i >= 0 with sum a_i = n, i.e. "
          f"{comb(N + d, d)} points at level {N}; the response is zero everywhere else, at every level")

# ---------------------------------------------------------------- A2 asymptotics
print("A2 the step is uniform on {0, e_1, .., e_d}: mean mu = (1,..,1)/(d+1), second moment I/(d+1),")
print("A2 covariance Sigma = I/(d+1) - J/(d+1)^2, whose eigenvalues are 1/(d+1)^2 along (1,..,1) and 1/(d+1)")
print("A2 with multiplicity d-1, so det Sigma = (d+1)^{-(d+1)}.")
for d in (2, 3):
    n1 = d + 1
    Sig = sp.eye(d) / n1 - sp.ones(d, d) / n1 ** 2
    det = sp.det(Sig)
    peak = sp.sqrt(1 / det) / (2 * sp.pi) ** sp.Rational(d, 2)
    print(f"A2 d={d}: det Sigma = {det} = (d+1)^-(d+1): {sp.simplify(det - sp.Rational(1, n1 ** n1)) == 0}; "
          f"local limit peak at y = n mu is (2 pi n)^(-d/2) (d+1)^((d+1)/2) = {sp.nsimplify(peak)} n^(-{d}/2) "
          f"= {float(peak):.6f} n^(-{d}/2)")
    print(f"A2 d={d}: widths about the axis: sqrt(n/(d+1)) = {float(sp.sqrt(sp.Rational(1,n1))):.4f} sqrt(n) across "
          f"it (multiplicity {d-1}), sqrt(n)/(d+1) = {float(sp.Rational(1,n1)):.4f} sqrt(n) along it")
# numerical check of the peak constant with exact multinomials
for d in (2, 3):
    n1 = d + 1
    print(f"A2 d={d} exact multinomial at y = n mu against the constant:", end=" ")
    for n in (60, 120, 240, 480):
        if n % n1: continue
        a = [n // n1] * d; a0 = n - sum(a)
        num = Fraction(factorial(n), factorial(a0))
        for ai in a: num /= factorial(ai)
        val = float(num) / n1 ** n
        pred = (2 * pi * n) ** (-d / 2) * n1 ** ((d + 1) / 2)
        print(f"n={n}: {val:.6e} vs {pred:.6e} (ratio {val/pred:.4f})", end="  ")
    print()

# ---------------------------------------------------------------- A3 the equal-level covariance
kk3 = sp.symbols("k1 k2 k3", real=True)
for d in (2, 3):
    ks = kk3[:d]; n1 = d + 1
    phi = (1 + sum(sp.exp(-sp.I * k) for k in ks)) / n1
    u = sp.expand(phi * sp.conjugate(phi))
    M = sp.eye(d) / n1 - sp.ones(d, d) / n1 ** 2
    kv = sp.Matrix(list(ks))
    quad = sp.series((1 - u).subs({ks[i]: sp.Symbol('t') * ks[i] for i in range(d)}), sp.Symbol('t'), 0, 3).removeO().coeff(sp.Symbol('t'), 2)
    print(f"A3 d={d}: 1 - u(k) = k^T M k + O(k^4) with M = Sigma (the same matrix):",
          sp.simplify(sp.expand_complex(sp.expand(quad - (kv.T * M * kv)[0, 0]))) == 0)
    if d == 3:
        c = 1 / (4 * sp.pi * sp.sqrt(sp.det(M)))
        print(f"A3 d=3: C(x) = sigma^2/(4 pi sqrt(det M) sqrt(x^T M^-1 x)) with det M = {sp.det(M)}, "
              f"so C(x) -> {sp.nsimplify(c)} sigma^2/sqrt(x^T M^-1 x) = {float(c):.6f} sigma^2/sqrt(x^T M^-1 x)")
    else:
        c = 1 / (2 * sp.pi * sp.sqrt(sp.det(M)))
        print(f"A3 d=2: C(x) = -(sigma^2/(2 pi sqrt(det M))) log sqrt(x^T M^-1 x) + const, det M = {sp.det(M)}, "
              f"coefficient {sp.nsimplify(c)} = {float(c):.6f} sigma^2 (a logarithm: no finite C(infinity))")

# ---------------------------------------------------------------- A4 how they differ, exactly
print("A4 support: the response is zero unless every a_i >= 0 (the forward cone); the covariance is supported on")
print("A4 the whole plane and satisfies C(x) = C(-x), because its symbol |phi|^2 is even. One is one-sided in")
print("A4 level time, the other is inversion symmetric: they differ before any constant is chosen.")
print("A4 decay: the response at level n decays like n^(-d/2) with a Gaussian profile of width sqrt(n) about the")
print("A4 drifting centre n mu; the equal-level covariance decays like log(1/r) (d = 2) or 1/r (d = 3) in space.")
print("A4 no constant: summed over levels the response has symbol 1/(1 - phi) and the covariance sigma^2/(1-|phi|^2),")
print("A4 so response = lambda covariance would force (1 - |phi(k)|^2)/(1 - phi(k)) = lambda sigma^2 at every k.")
for d in (2, 3):
    ks = kk3[:d]; n1 = d + 1
    phi = (1 + sum(sp.exp(-sp.I * k) for k in ks)) / n1
    ratio = (1 - phi * sp.conjugate(phi)) / (1 - phi)
    pts = {}
    for name, val in ((f"k=(pi,{'pi,' * (d-1)})".replace(",)", ")"), [sp.pi] * d),
                      ("k=(pi,0,..)", [sp.pi] + [sp.Integer(0)] * (d - 1)),
                      ("k=(pi/2,0,..)", [sp.pi / 2] + [sp.Integer(0)] * (d - 1))):
        v = sp.simplify(ratio.subs({ks[i]: val[i] for i in range(d)}))
        pts[name] = sp.nsimplify(sp.expand_complex(v))
    vals = list(pts.values())
    print(f"A4 d={d}: that ratio takes the values " +
          ", ".join(f"{n} -> {v}" for n, v in pts.items()) +
          f"; all equal: {len(set(sp.simplify(x - vals[0]) == 0 for x in vals)) == 1 and sp.simplify(vals[1]-vals[0]) == 0}"
          f" -> no single lambda can work (the fluctuation-response relation fails)")

# ---------------------------------------------------------------- N1 numerics
print("N1 least squares over the forward cone: the best lambda in R = lambda C, and the spread of R/C")
for d, L in ((2, 256), (3, 64)):
    n1 = d + 1
    g = np.meshgrid(*([2 * np.pi * np.arange(L) / L] * d), indexing="ij")
    phi = (1 + sum(np.exp(-1j * x) for x in g)) / n1
    m = np.ones((L,) * d, bool); m[(0,) * d] = False
    Rk = np.zeros_like(phi); Ck = np.zeros_like(phi)
    Rk[m] = 1.0 / (1 - phi[m]); Ck[m] = 1.0 / (1 - np.abs(phi[m]) ** 2)
    R = np.fft.ifftn(Rk).real; C = np.fft.ifftn(Ck).real
    pts = [p for p in product(range(1, 9), repeat=d)] + [tuple([r] + [0] * (d - 1)) for r in range(1, 9)]
    Rv = np.array([R[p] for p in pts]); Cv = np.array([C[p] for p in pts])
    lam = float(Rv @ Cv / (Cv @ Cv))
    resid = float(np.linalg.norm(Rv - lam * Cv) / np.linalg.norm(Rv))
    rat = Rv / Cv
    print(f"N1 d={d} (L={L}, {len(pts)} points inside the cone): best lambda = {lam:.4f}, relative residual "
          f"{resid*100:.1f}%, R/C ranges {rat.min():.4f} to {rat.max():.4f} (a factor {rat.max()/rat.min():.1f})")
    mir = [tuple((-np.array(p)) % L) for p in pts]
    Cm = np.array([C[q] for q in mir])
    print(f"N1 d={d}: the covariance at the mirrored points is {np.abs(Cm).min():.4f} to {np.abs(Cm).max():.4f} and "
          f"C(x) - C(-x) is at most {np.abs(Cv - Cm).max():.2e} (inversion symmetric to machine precision), while "
          f"the response at a fixed level n < L is exactly zero there - see the next line. Summed over all levels "
          f"on a torus the cone wraps after L levels, so only the fixed-level statement is one-sided.")
    # the response at a fixed level against the covariance, same points
    lev = 8
    Rn = np.zeros((L,) * d)
    for a in product(range(lev + 1), repeat=d):
        if sum(a) <= lev:
            a0 = lev - sum(a); v = Fraction(factorial(lev), factorial(a0))
            for ai in a: v /= factorial(ai)
            Rn[a] = float(v) / n1 ** lev
    Rnv = np.array([Rn[p] for p in pts]); Rnm = np.array([Rn[q] for q in mir])
    lam2 = float(Rnv @ Cv / (Cv @ Cv))
    print(f"N1 d={d}: at the single level n={lev}, best lambda = {lam2:.4f} with relative residual "
          f"{float(np.linalg.norm(Rnv - lam2*Cv)/np.linalg.norm(Rnv))*100:.1f}%, and the response at the mirrored "
          f"points is exactly {np.abs(Rnm).max():.1e} against a covariance of {np.abs(Cm).min():.4f} or more")
print(f"SUMMARY: the pinned-record response is exactly the multinomial n!/(a_0! prod a_i!) (d+1)^-n on the forward "
      f"cone (checked exactly to level 12 for d = 2, 3), peaking as (2 pi n)^(-d/2) (d+1)^((d+1)/2) = "
      f"0.826993 n^-1 (d=2) and 1.015918 n^(-3/2) (d=3) with widths sqrt(n/(d+1)) across the axis; the equal-level "
      f"covariance is the plane's Green function (log in d=2, 1/r in d=3), inversion symmetric and supported "
      f"everywhere, and (1-|phi|^2)/(1-phi) is not constant, so no lambda gives response = lambda x covariance: "
      f"the equilibrium fluctuation-response relation fails, as expected; {time.time()-t0:.0f}s")
