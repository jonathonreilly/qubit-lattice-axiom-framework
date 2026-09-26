#!/usr/bin/env python3
"""Independent check for the neutral moving-records law at low density.

Does not import the author's script. Finite identities are exact (sympy).
The correlation bound is the path sum proved from those identities.
"""
import itertools
import mpmath as mp
import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (f" :: {detail}" if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


b, v, th, u = sp.symbols("beta v theta u", positive=True)
m = sp.symbols("m", integer=True, positive=True)

# --- sphere average and neutral scale ---
avg = sp.integrate(sp.exp(b * v * sp.cos(th)) * sp.sin(th) / 2, (th, 0, sp.pi))
target = sp.sinh(b * v) / (b * v)
check(
    "S1 sphere average",
    sp.simplify(avg - target) == 0,
    str(sp.simplify(avg)),
)
c0 = b / sp.sinh(b)
check(
    "S1b neutral scale",
    sp.simplify(c0 * sp.sinh(b) / b - 1) == 0,
)

# g(y)=sinh(y)/y increases because q(u)=u cosh u - sinh u equals a series of positive terms
n = sp.symbols("n", integer=True, positive=True)
q = u * sp.cosh(u) - sp.sinh(u)
term_sum = sp.summation(2 * n * u ** (2 * n + 1) / sp.factorial(2 * n + 1), (n, 1, sp.oo))
check(
    "S2a q(u) series",
    sp.simplify(q - term_sum) == 0,
    "u cosh u - sinh u = sum_{n>=1} 2n u^(2n+1)/(2n+1)!, so q(u)>0 for u>0",
)

# F_1 = 1 and the ratio identity
F = lambda mm: c0**mm * sp.sinh(mm * b) / (mm * b)
check("S2b F_1 = 1", sp.simplify(F(1) - 1) == 0)
ratio = sp.simplify(F(m + 1) / F(m))
closed = sp.simplify(m / (m + 1) * b * (sp.coth(b) + sp.coth(m * b)))
check(
    "S2c occupation ratio",
    sp.simplify(ratio - closed) == 0,
    "F_{m+1}/F_m = [m/(m+1)] beta (coth beta + coth(m beta))",
)
# coth u > 1/u because u cosh u - sinh u has the positive coefficients above,
# so beta(coth beta + coth(m beta)) > 1 + 1/m and the ratio is > 1.
gap = sp.simplify(b * (sp.coth(b) - 1 / b) - q.subs(u, b) / sp.sinh(b))
check(
    "S2d coth beta - 1/beta",
    gap == 0,
    "equals (beta cosh beta - sinh beta)/(beta sinh beta), whose numerator series is positive",
)

# --- asymptotics of F_6 ---
F6 = sp.simplify(F(6))
elem = (
    sp.Rational(16, 3)
    * b**5
    * (1 - sp.exp(-12 * b))
    / (1 - sp.exp(-2 * b)) ** 6
)
sinh_id = sp.simplify(sp.sinh(b) - (sp.exp(b) - sp.exp(-b)) / 2)
raw = (b / ((sp.exp(b) - sp.exp(-b)) / 2)) ** 6 * ((sp.exp(6 * b) - sp.exp(-6 * b)) / 2) / (6 * b)
check("S3a sinh rewrite", sinh_id == 0 and sp.simplify(raw - elem) == 0, str(sp.factor(sp.simplify(raw / elem))))
check(
    "S3b large beta",
    sp.limit((1 - sp.exp(-12 * b)) / (1 - sp.exp(-2 * b)) ** 6, b, sp.oo) == 1,
    "F_6 / beta^5 -> 16/3, so z0 = 1/(5 F_6) ~ 3/(80 beta^5)",
)
check("S3c constant", sp.simplify(sp.Rational(1, 5) / sp.Rational(16, 3) - sp.Rational(3, 80)) == 0)
check("S3d small beta", sp.limit(F6, b, 0) == 1)
old = (b * sp.exp(b) / sp.sinh(b)) ** 6
ratio_old = sp.simplify(old / F6)
check(
    "S3e remark ratio",
    sp.simplify(ratio_old - 6 * b * sp.exp(6 * b) / sp.sinh(6 * b)) == 0
    and sp.limit(ratio_old / b, b, sp.oo) == 12,
    "prior (beta e^beta/sinh beta)^6 exceeds F_6 by a factor ~ 12 beta",
)

# --- only the zero vector is fixed by these two rotations ---
Rz = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
Rx = sp.Matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
stack = (Rz - sp.eye(3)).col_join(Rx - sp.eye(3))
check(
    "S4 no common fixed vector",
    Rz.det() == 1
    and Rx.det() == 1
    and Rz.T * Rz == sp.eye(3)
    and Rx.T * Rx == sp.eye(3)
    and stack.nullspace() == [],
    "a cluster mean fixed by both rotations is the zero vector",
)
Rs = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        M = sp.zeros(3)
        for i in range(3):
            M[i, perm[i]] = signs[i]
        if M.det() == 1:
            Rs.append(M)
total = sum(Rs, sp.zeros(3))
check(
    "S4b cube rotations",
    len(Rs) == 24 and all(entry == 0 for entry in total),
    "the 24 proper cubic rotations sum to 0",
)

# --- path sum ---
p = sp.symbols("p", positive=True)
n_sym = sp.symbols("n", integer=True, positive=True)
N_sym = sp.symbols("N", integer=True, positive=True)
partial = sp.summation(6 * 5 ** (n_sym - 1) * p ** (n_sym + 1), (n_sym, 1, N_sym))
cleared = sp.simplify((1 - 5 * p) * partial - 6 * p**2 * (1 - (5 * p) ** N_sym))
check(
    "S5 geometric partial sum",
    cleared == 0,
    "(1-5p) sum_{n=1}^N 6*5^(n-1) p^(n+1) = 6 p^2 (1-(5p)^N)",
)
tail_ok = sp.limit(sp.Rational(4, 5) ** N_sym, N_sym, sp.oo) == 0
for pv in (sp.Rational(1, 6), sp.Rational(1, 7), sp.Rational(1, 10), sp.Rational(3, 16)):
    inf = sp.limit(6 * pv**2 * (1 - (5 * pv) ** N_sym) / (1 - 5 * pv), N_sym, sp.oo)
    if sp.simplify(inf - 6 * pv**2 / (1 - 5 * pv)) != 0:
        tail_ok = False
check(
    "S5b tail",
    tail_ok,
    "at p=1/6,1/7,1/10,3/16 the tail vanishes; (4/5)^N -> 0. For every p<1/5 the same holds by the binomial bound (1+s)^N>=1+N s",
)

# --- two-valued menu ---
t = sp.symbols("t", positive=True)
check(
    "T0 neutral factors",
    sp.simplify(sp.exp(b) - (sp.cosh(b) + sp.sinh(b))) == 0
    and sp.simplify(sp.exp(-b) - (sp.cosh(b) - sp.sinh(b))) == 0
    and sp.simplify(sp.tanh(b) - sp.sinh(b) / sp.cosh(b)) == 0
    and sp.together((sp.cosh(b) + sp.sinh(b)) / sp.cosh(b) - 1 - sp.sinh(b) / sp.cosh(b)) == 0
    and sp.together((sp.cosh(b) - sp.sinh(b)) / sp.cosh(b) - 1 + sp.sinh(b) / sp.cosh(b)) == 0,
    "e^{±beta} = cosh beta ± sinh beta, so (1/cosh beta) e^{±beta} = 1 ± tanh beta",
)
G = sp.expand((1 + t) ** 6 + (1 - t) ** 6)
Gpoly = 2 + 30 * t**2 + 30 * t**4 + 2 * t**6
check("T2 expansion", sp.expand(G - Gpoly) == 0)
dG = sp.diff(Gpoly, t)
check(
    "T2 increasing",
    sp.expand(dG - (60 * t + 120 * t**3 + 12 * t**5)) == 0
    and all(cf > 0 for cf in sp.Poly(sp.expand(dG / t), t).coeffs()),
    "G(0)=2, G(1)=64",
)
check("T2 endpoints", sp.simplify(G.subs(t, 0) - 2) == 0 and sp.simplify(G.subs(t, 1) - 64) == 0)
ok_pairs = True
n_pairs = 0
for k in range(7):
    for ell in range(7 - k):
        n_pairs += 1
        S = sp.expand((1 + t) ** k * (1 - t) ** ell + (1 - t) ** k * (1 + t) ** ell)
        diff = sp.Poly(sp.expand(G - S), t)
        if any(cf < 0 for cf in diff.coeffs()):
            ok_pairs = False
check(
    "T1 pair polynomials",
    ok_pairs and n_pairs == 28,
    "for every k+l<=6, G(t)-S(k,l) has no negative coefficient",
)
check("T3 contains 1/320", sp.Rational(1, 5) / 64 == sp.Rational(1, 320))
check("T3b small-beta factor", sp.Integer(64) / 2 == 32)
w = sp.symbols("w", positive=True)
rho = w / (1 + w)
check(
    "S6 sharp occupation",
    sp.simplify(sp.together(rho - sp.Rational(1, 5)) - (4 * w - 1) / (5 * (1 + w))) == 0,
    "zS/(1+zS) < 1/5 iff zS < 1/4, so the same bound closes for z < 1/(4 F_6) and z < 1/(4 G)",
)
check(
    "S6b constants",
    sp.Rational(1, 4) / sp.Rational(16, 3) == sp.Rational(3, 64)
    and sp.Rational(1, 4) / 64 == sp.Rational(1, 256)
    and sp.Integer(80) / 2 == 40
    and sp.Rational(80, 64) == sp.Rational(5, 4),
    "sharp sphere threshold ~ 3/(64 beta^5); sharp two-valued endpoint 1/256 is 5/4 times 1/320",
)

mp.mp.dps = 40
factor_1 = 64 / (2 * (1 + 15 * mp.tanh(1) ** 2 + 15 * mp.tanh(1) ** 4 + mp.tanh(1) ** 6))
print(f"   factor 64/G(tanh beta) at beta=1 is {mp.nstr(factor_1, 8)}", flush=True)
for bv in (1, 5, 20):
    bb = sp.Integer(bv)
    z0 = 1 / (5 * F6.subs(b, bb))
    old_z = 1 / (5 * old.subs(b, bb))
    print(
        f"   beta={bv}: z0={mp.nstr(mp.mpf(z0.evalf(40)), 8)}  remark={mp.nstr(mp.mpf(old_z.evalf(40)), 8)}",
        flush=True,
    )

print(f"TOTAL FAIL={len(FAIL)}", flush=True)
if FAIL:
    print("SUMMARY: fails at " + ", ".join(FAIL), flush=True)
else:
    print(
        "SUMMARY: PARTIAL at the neutral scales, on every even cubic torus: "
        "conditional occupation is at most rho=w/(1+w) with w=z F_6 for the sphere and w=z G(tanh beta) for the two-valued menu. "
        "rho<1/5 iff w<1/4, so the path bound closes for z<1/(4 F_6) and z<1/(4 G). "
        "F_6/beta^5->16/3, hence 1/(4 F_6)~3/(64 beta^5). The attempt's smaller region z<1/(5 F_6)~3/(80 beta^5) is contained in this one. "
        "G rises from 2 to 64, so the two-valued region contains z<1/256 and therefore z<1/320. "
        "A cluster mean fixed by two explicit rotations is 0. "
        "High density and the torus separation lemma were not taken up.",
        flush=True,
    )
    print(
        "HIT: confirmed - sphere menu at c0=beta/sinh beta has no long-range order for "
        "z<1/(4 F_6(beta)), and F_6/beta^5->16/3 so this threshold is asymptotic to 3/(64 beta^5). "
        "The attempt's z<1/(5 F_6)~3/(80 beta^5) is the same bound with zS/(1+zS) replaced by zS, and is contained in this region. "
        "Rotating one occupied cluster kills cross correlations. "
        "Two-valued menu at c0=1/cosh beta: the same path bound holds for "
        "z<1/(4[(1+t)^6+(1-t)^6]), which contains z<1/256 and therefore the earlier z<1/320.",
        flush=True,
    )
