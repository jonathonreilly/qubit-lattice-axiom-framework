#!/usr/bin/env python3
"""J:attack-f:PR9373 -- NORMALIZATION: is the printed 'Pauli vector' n of the handover note the Pauli vector of the effective two-level Hamiltonian, and is item 5 ('D's weighted-degree-4 part equals c |d|^2') true for it?

Note (open PR 9373, item 4): the effective Hamiltonian to weighted order two has Pauli vector d = n u + quadratic(v, t) with n = (4 pi, -+8 pi q, 4 pi q (4 q^2 - 1)/(4 q^2 + 1)) at f+-;
item 5: the weighted-degree-4 part of D = det H equals c |d|^2, identically in q, with c = 256 q^2 (8q^2+1)/(4q^2+1)^2; item 6: the two components of the quadratic part transverse to n have the printed A, B and
the printed resultant -2^29 q^10 (6q^2+1)(12q^2+1)^2/(8q^2+1)^4.

The u^2 term of D is fixed by the Hessian of item 3: D = 2 pi^2 h(q) u^2 + (terms of weight >= 5), so an orthonormal-basis Pauli vector has c |n|^2 = 2 pi^2 h(q). This script checks, with its own construction
(own site/flavour network, exact symbolic algebra in q, 40-digit effective Hamiltonian in an orthonormal kernel basis, and a basis-free eigenvalue slope along (1, -1, 0)):
  (1) exactly, in q: c(q) |n_printed(q)|^2 - 2 pi^2 h(q) is a rational function that is positive for every q > 0 (it never vanishes);
  (2) the orthonormal-basis |n|^2 = 2 pi^2 h / c at six q; the ratio |n_printed|^2/|n|^2 at the same q; and the basis-free slope of the middle eigenvalues along (1, -1, 0), which fixes |n| without any kernel basis;
  (3) the weighted-degree-4 coefficient of u^2 from the determinant, against c |n|^2 and c |n_printed|^2;
  (4) the PR's runner (fetched at the PR head, read as text): its own identity carries a metric factor (n1 n2)^-1 on the first two components that the note's item 5 does not state;
  (5) the printed resultant against the resultant of the transverse forms of the true Pauli vector: their ratio varies with q (the magnitude depends on the frame) while the sign does not (exact rational check that the
      resultant of two binary quadratics scales by the square of the determinant of any real change of the pair).
Prints SUMMARY:; HIT: if the printed n or item 5 as written fails.
"""
import sys, time, itertools, subprocess, os, re
import numpy as np
import sympy as sp
import mpmath as mp
from fractions import Fraction as Fr
from pathlib import Path

PASS = FAIL = 0; HITS = []
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1; HITS.append(name)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}", flush=True)
T0 = time.time()

# ---------------------------------------------------------------- own network construction (site, flavour and Bloch-cell rules)
def is_site(p):
    i, j, z = p; m = z % 4
    if m == 0: return j % 2 == 0
    if m == 1: return i % 2 == 1
    if m == 2: return j % 2 == 1
    return i % 2 == 0
def nbrs(p):
    out = []
    for a in range(3):
        for s in (-1, 1):
            q = list(p); q[a] += s; q = tuple(q)
            if is_site(q): out.append(q)
    return out
def flavour(p, q):
    d = tuple(q[a] - p[a] for a in range(3))
    if d[2] != 0: return "z"
    lo = p if sum(d) > 0 else q; m = p[2] % 4
    idx = lo[0] + m // 2 if m in (0, 2) else lo[1] + (m - 1) // 2
    return "x" if idx % 2 == 0 else "y"
REPS = [(0, 0, 0), (1, 0, 0), (1, 0, 1), (1, 1, 1)]
def reduce(p):
    n3 = p[2] // 2; x, y, z = p[0] - n3, p[1] - n3, p[2] - 2 * n3
    n1, n2 = x // 2, y // 2; rep = (x - 2 * n1, y - 2 * n2, z)
    return REPS.index(rep), (n1, n2, n3)
def terms_of(Jx, Jy, Jz, kappa):
    J = {"x": Jx, "y": Jy, "z": Jz}; out = []
    for p in REPS:
        a, _ = reduce(p)
        if sum(p) % 2 == 0:
            for q in nbrs(p):
                b, n = reduce(q); out.append((a, b, n, 2 * J[flavour(p, q)]))
        nb = {flavour(p, q): q for q in nbrs(p)}
        for (l, m) in (("x", "y"), ("y", "z"), ("z", "x")):
            r1, n1 = reduce(nb[l]); r2, n2 = reduce(nb[m])
            out.append((r1, r2, tuple(int(x) for x in np.subtract(n2, n1)), 2 * kappa))
    return out
def M_sym(z1, z2, z3, Jx, Jy, Jz, kappa):
    M = sp.zeros(4, 4)
    for (a, b, n, amp) in terms_of(Jx, Jy, Jz, kappa):
        e = z1 ** n[0] * z2 ** n[1] * z3 ** n[2]
        M[a, b] += amp * e; M[b, a] -= amp / e
    return M

# ---------------------------------------------------------------- (1) exact algebra in q
q = sp.symbols('q', positive=True); z1, z2, z3, lam = sp.symbols('z1 z2 z3 lam')
NQ = 1 + 4 * q ** 2; Jq = 8 * q ** 2 / NQ
Msym = M_sym(z1, z2, z3, 1, 1, Jq, q)
Dsym = sp.factor(sp.together(Msym.det()))
def z0sym(sg): return (2 * q + sg * sp.I) ** 2 / NQ
c_formula = 256 * q ** 2 * (8 * q ** 2 + 1) / NQ ** 2
h_formula = 512 * q ** 2 * (8 * q ** 2 + 1) * (128 * q ** 6 + 16 * q ** 4 + 16 * q ** 2 + 1) / NQ ** 4
# validation of my reconstruction of the network against the note's own J = 1 numbers
M12 = M_sym(z1, z2, z3, 1, 1, 1, sp.Rational(1, 2)); sub12 = {z1: sp.I, z2: -sp.I, z3: -1}
check("network reconstruction: at J = 1, kappa = 1/2 and f+ = (1/4, 3/4, 1/2) the characteristic polynomial is lambda^2 (lambda^2 - 48)", sp.expand((sp.I * M12.subs(sub12) - lam * sp.eye(4)).det()) == lam ** 4 - 48 * lam ** 2)
ok_cp = ok_grad = ok_hess = True
for sg in (1, -1):
    sub = {z1: z0sym(sg), z2: sp.conjugate(z0sym(sg)), z3: -1}
    H0 = sp.I * Msym.subs(sub)
    cp = sp.expand((H0 - lam * sp.eye(4)).det())
    ok_cp &= sp.simplify(cp - lam ** 2 * (lam ** 2 - c_formula)) == 0
    zs = [z1, z2, z3]
    ok_grad &= sp.simplify(Dsym.subs(sub)) == 0 and all(sp.simplify((2 * sp.pi * sp.I * zs[j] * sp.diff(Dsym, zs[j])).subs(sub)) == 0 for j in range(3))
    Hess = sp.zeros(3, 3)
    for j in range(3):
        dj = 2 * sp.pi * sp.I * zs[j] * sp.diff(Dsym, zs[j])
        for k in range(3): Hess[j, k] = sp.simplify((2 * sp.pi * sp.I * zs[k] * sp.diff(dj, zs[k])).subs(sub))
    ok_hess &= (Hess - 4 * sp.pi ** 2 * h_formula * sp.Matrix([[1, -1, 0], [-1, 1, 0], [0, 0, 0]])).applyfunc(sp.simplify) == sp.zeros(3, 3)
check("for every q > 0 (symbolic in q): det(H - lambda) = lambda^2 (lambda^2 - c) with c = 256 q^2 (8q^2+1)/(4q^2+1)^2 at both f+ and f-", ok_cp, f"{time.time()-T0:.0f}s")
check("for every q > 0: D = det H and its gradient vanish at f+ and f-", ok_grad)
check("for every q > 0: the Hessian of D at f+ and f- equals 4 pi^2 h(q) (1,-1,0)(1,-1,0)^T with h(q) = 512 q^2 (8q^2+1)(128q^6+16q^4+16q^2+1)/(4q^2+1)^4 (h(1/2) = 192)", ok_hess and h_formula.subs(q, sp.Rational(1, 2)) == 192, f"{time.time()-T0:.0f}s")

# ---------------------------------------------------------------- (2) effective Hamiltonian, weighted degree four, resultant (mpmath, 40 digits)
mp.mp.dps = 40
def setup(qv, sg):
    qq = mp.mpf(qv); NQn = 1 + 4 * qq ** 2; J = 8 * qq ** 2 / NQn
    T = terms_of(1, 1, J, qq)
    z0 = (2 * qq + sg * 1j * mp.mpf(1)) ** 2 / NQn
    x = mp.arg(z0) / (2 * mp.pi)
    f0 = [x, 1 - x, mp.mpf(1) / 2]
    return qq, J, T, f0
def Hnum(T, f):
    M = mp.zeros(4, 4)
    for (a, b, n, amp) in T:
        ph = mp.expjpi(2 * sum(n[j] * f[j] for j in range(3)))
        M[a, b] += amp * ph; M[b, a] -= amp * mp.conj(ph)
    return 1j * M
def derivs(T, f0):
    H0 = Hnum(T, f0); Hj = [mp.zeros(4, 4) for _ in range(3)]; Hjk = {}
    for j in range(3):
        for k in range(j, 3): Hjk[(j, k)] = mp.zeros(4, 4)
    for (a, b, n, amp) in T:
        ph = mp.expjpi(2 * sum(n[j] * f0[j] for j in range(3)))
        for j in range(3):
            Hj[j][a, b] += 1j * amp * ph * (2j * mp.pi * n[j]); Hj[j][b, a] += 1j * amp * mp.conj(ph) * (2j * mp.pi * n[j])   # d/d delta of -amp*conj(ph) is -amp*(-2 pi i n) conj(ph)
            for k in range(j, 3):
                Hjk[(j, k)][a, b] += 1j * amp * ph * (2j * mp.pi) ** 2 * n[j] * n[k]
                Hjk[(j, k)][b, a] -= 1j * amp * mp.conj(ph) * (-2j * mp.pi) ** 2 * n[j] * n[k]
    return H0, Hj, Hjk
def analyse(qv, sg):
    qq, J, T, f0 = setup(qv, sg)
    H0, Hj, Hjk = derivs(T, f0)
    c = 256 * qq ** 2 * (8 * qq ** 2 + 1) / (4 * qq ** 2 + 1) ** 2
    E, Ev = mp.eigh(H0)
    ker = [i for i in range(4) if abs(E[i]) < mp.mpf(10) ** -25]
    assert len(ker) == 2 and abs(sorted([E[i] for i in range(4)])[3] ** 2 - c) < mp.mpf(10) ** -30
    K = mp.matrix(4, 2)
    for a_, i in enumerate(ker):
        for r in range(4): K[r, a_] = Ev[r, i]
    Qm = mp.eye(4) - K * K.H
    def pieces(u, v, t):
        d = [(v + u) / 2, (v - u) / 2, t]
        V1 = sum((Hj[j] * d[j] for j in range(3)), mp.zeros(4, 4)) if False else None
    def heff(u, v, t):
        dv = [v / 2, v / 2, t]; du = [u / 2, -u / 2, 0]
        V1 = sum((Hj[j] * dv[j] for j in range(3)), mp.zeros(4, 4))
        W2 = sum((Hj[j] * du[j] for j in range(3)), mp.zeros(4, 4))
        for (j, k), X in Hjk.items(): W2 += X * dv[j] * dv[k] * (mp.mpf(1) / 2 if j == k else 1)
        first = K.H * V1 * K
        second = K.H * W2 * K - K.H * V1 * Qm * (H0 / c) * Qm * V1 * K
        return first, second
    def pauli(h): return mp.re((h[0, 0] + h[1, 1]) / 2), mp.matrix([mp.re(h[0, 1]), -mp.im(h[0, 1]), mp.re((h[0, 0] - h[1, 1]) / 2)])
    first_max = max(abs(x) for M_ in (heff(0, 1, 0)[0], heff(0, 0, 1)[0], heff(0, 1, 1)[0]) for x in M_)
    n = pauli(heff(1, 0, 0)[1])[1]; idu = abs(pauli(heff(1, 0, 0)[1])[0])
    Q2 = {}
    for name, (a_, b_) in (("v", (1, 0)), ("t", (0, 1)), ("vt", (1, 1))):
        Q2[name] = pauli(heff(0, a_, b_)[1])
    idq = max(abs(Q2[k][0]) for k in Q2)
    qv_ = Q2["v"][1]; qt_ = Q2["t"][1]; qvt_ = Q2["vt"][1] - qv_ - qt_
    def dvec(u, v, t): return n * u + qv_ * v ** 2 + qt_ * t ** 2 + qvt_ * v * t
    return dict(qq=qq, c=c, J=J, T=T, f0=f0, n=n, first=first_max, idu=idu, idq=idq, dvec=dvec, qforms=(qv_, qt_, qvt_))
def D_eps_coeff4(qv, sg, u, v, t):
    qq, J, T, f0 = setup(qv, sg)
    def Deps(eps):
        d = [(eps * v + eps ** 2 * u) / 2, (eps * v - eps ** 2 * u) / 2, eps * t]
        return mp.det(Hnum(T, [f0[j] + d[j] for j in range(3)]))
    return mp.taylor(Deps, 0, 4)
def resultant(qforms):
    qv_, qt_, qvt_ = qforms
    return qv_, qt_, qvt_

# ================================================================ the normalization attack
def n_printed(qq, sg):
    return [4 * mp.pi, -sg * 8 * mp.pi * qq, 4 * mp.pi * qq * (4 * qq ** 2 - 1) / (4 * qq ** 2 + 1)]
qsym = sp.symbols('q', positive=True)
c_q = 256 * qsym ** 2 * (8 * qsym ** 2 + 1) / (4 * qsym ** 2 + 1) ** 2
h_q = 512 * qsym ** 2 * (8 * qsym ** 2 + 1) * (128 * qsym ** 6 + 16 * qsym ** 4 + 16 * qsym ** 2 + 1) / (4 * qsym ** 2 + 1) ** 4
npr2 = sp.expand((4 * sp.pi) ** 2 + (8 * sp.pi * qsym) ** 2) + (4 * sp.pi * qsym * (4 * qsym ** 2 - 1) / (4 * qsym ** 2 + 1)) ** 2
gap = sp.factor(sp.together(c_q * npr2 - 2 * sp.pi ** 2 * h_q))
num, den = sp.fraction(sp.together(gap))
pnum = sp.Poly(sp.expand(num / sp.pi ** 2), qsym)
check("exact in q: c(q) |n_printed|^2 - 2 pi^2 h(q) = " + str(gap) + " -- a rational function whose numerator has only positive coefficients, so it is positive for every q > 0: the printed n cannot be the Pauli vector of item 5's identity at any coupling",
      all(cf >= 0 for cf in pnum.all_coeffs()) and pnum.LC() > 0 and sp.simplify(den) != 0, f"numerator/pi^2 = {pnum.as_expr()}")
ratio_sym = sp.simplify(c_q * npr2 / (2 * sp.pi ** 2 * h_q))
check("exact: the ratio c |n_printed|^2 / (2 pi^2 h) = |n_printed|^2 / |n|^2 = " + str(sp.factor(ratio_sym)) + ", equal to 4 only at q = 1/2 and tending to 5/2 as q -> infinity",
      ratio_sym.subs(qsym, sp.Rational(1, 2)) == 4 and abs(float(sp.limit(ratio_sym, qsym, sp.oo)) - 2.5) < 1e-12)
mp.mp.dps = 40
rows = []; ok_norm = True; ok_ratio = True; ok_slope = True
def mid_slope(qv, sg, s):
    q_, J_, T_, f0_ = setup(qv, sg)
    ev = mp.eigh(Hnum(T_, [f0_[0] + s / 2, f0_[1] - s / 2, f0_[2]]), eigvals_only=True)
    return (ev[2] - ev[1]) / 2 / s                      # half-gap of the middle bands over s = u
for qs_ in ["0.2", "0.3333333333333333", "0.5", "1", "2", "5"]:
    for sg in (1, -1):
        r = analyse(qs_, sg); qq = r["qq"]; nt = r["n"]; n2 = sum(x ** 2 for x in nt)
        h = 512 * qq ** 2 * (8 * qq ** 2 + 1) * (128 * qq ** 6 + 16 * qq ** 4 + 16 * qq ** 2 + 1) / (4 * qq ** 2 + 1) ** 4
        npn = n_printed(qq, sg); np2 = sum(x ** 2 for x in npn)
        ok_norm &= abs(n2 - 2 * mp.pi ** 2 * h / r["c"]) < mp.mpf(10) ** -28
        rq_ = 4 * (80 * qq ** 6 + 40 * qq ** 4 + 13 * qq ** 2 + 1) / (128 * qq ** 6 + 16 * qq ** 4 + 16 * qq ** 2 + 1)
        ok_ratio &= abs(np2 / n2 - rq_) < mp.mpf(10) ** -25
        s1, s2 = mid_slope(qs_, sg, mp.mpf(10) ** -12), mid_slope(qs_, sg, mp.mpf(2) * mp.mpf(10) ** -12)
        slope = 2 * s1 - s2                              # Richardson
        ok_slope &= abs(slope - mp.sqrt(n2)) < mp.mpf(10) ** -9 * mp.sqrt(n2) and abs(slope - mp.sqrt(np2)) > 0.1 * mp.sqrt(n2)
        if sg == 1: rows.append((qs_, float(np2 / n2), float(mp.sqrt(n2)), float(mp.sqrt(np2)), float(slope)))
print("   (ok_norm, ok_ratio) =", ok_norm, ok_ratio)
check("40 digits, six q, both f+ and f-: the orthonormal-basis Pauli vector has |n|^2 = 2 pi^2 h / c, and |n_printed|^2 / |n|^2 equals the exact ratio above (3.80 at q = 0.2, 4 at q = 1/2, 3.33 at q = 1, 2.73 at q = 2)", ok_norm and ok_ratio,
      "; ".join(f"q = {r[0]}: ratio {r[1]:.4f}" for r in rows))
check("basis-free slope: half the gap of the middle bands along f = f+- + s (1, -1, 0)/2 is |n| s exactly (Richardson at s = 1e-12), and it differs from sqrt(|n_printed|^2) at every tested q", ok_slope,
      "; ".join(f"q = {r[0]}: slope {r[4]:.9f} = |n| {r[2]:.9f} vs printed |n| {r[3]:.9f}" for r in rows))
# weighted-degree-4 coefficient of u^2
ok_d4 = True; d4rows = []
for qs_ in ["0.2", "0.5", "1", "2"]:
    r = analyse(qs_, 1); qq = r["qq"]
    co = D_eps_coeff4(qs_, 1, mp.mpf(1), mp.mpf(0), mp.mpf(0))
    lhs = mp.re(co[4]); nt = r["n"]; npn = n_printed(qq, 1)
    ok_d4 &= abs(lhs - r["c"] * sum(x ** 2 for x in nt)) < mp.mpf(10) ** -25 * lhs and abs(lhs - r["c"] * sum(x ** 2 for x in npn)) > 0.1 * lhs
    d4rows.append((qs_, float(lhs), float(r["c"] * sum(x ** 2 for x in nt)), float(r["c"] * sum(x ** 2 for x in npn))))
check("the eps^4 coefficient of det H(f+ + (eps^2 u/2, -eps^2 u/2, 0)) at u = 1 equals c |n|^2 (orthonormal basis) and differs from c |n_printed|^2 by more than 10% of itself at every tested q", ok_d4,
      "; ".join(f"q = {r[0]}: {r[1]:.6f} = {r[2]:.6f}, with printed n {r[3]:.6f}" for r in d4rows))
# the runner's own identity
ROOT = Path(__file__).resolve().parents[3]
def git(*a): return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True)
git("fetch", "origin", "pull/9373/head", "--quiet"); HEAD = git("rev-parse", "FETCH_HEAD").stdout.strip()
files = git("diff", "--name-only", f"origin/main...{HEAD}").stdout.split()
runner = git("show", f"{HEAD}:" + [f for f in files if f.startswith("scripts/") and f.endswith(".py")][0]).stdout
note = git("show", f"{HEAD}:" + [f for f in files if f.startswith("docs/") and f.endswith(".md") and "audit" not in f][0]).stdout
ident_line = [ln for ln in runner.split("\n") if ln.strip().startswith("ident =")]
kernel_lines = [ln.strip() for ln in runner.split("\n") if "w1 = k0" in ln or "n1, n2 = dot" in ln]
check("the PR runner's identity line is " + (ident_line[0].strip() if ident_line else "?") + " -- it divides d1^2 + d2^2 by n1 n2 = |w1|^2 |w2|^2 of an orthogonal but unnormalised kernel basis, whereas the note's item 5 states c |d|^2 for the printed d",
      len(ident_line) == 1 and "(n1 * n2)" in ident_line[0] and "c |d|^2" in note and "n1" not in note, "kernel basis lines: " + " | ".join(kernel_lines))
# resultant: printed vs true transverse forms
def frame_res(qs_, sg):
    r = analyse(qs_, sg); qq = r["qq"]; n = r["n"]; n2 = sum(x ** 2 for x in n); nn = n / mp.sqrt(n2)
    e1 = mp.matrix([nn[1], -nn[0], 0]); e1 = e1 / mp.sqrt(sum(x ** 2 for x in e1)); e2 = mp.matrix([nn[1] * e1[2] - nn[2] * e1[1], nn[2] * e1[0] - nn[0] * e1[2], nn[0] * e1[1] - nn[1] * e1[0]])
    qv_, qt_, qvt_ = r["qforms"]
    A = [sum(e1[k] * w[k] for k in range(3)) for w in (qv_, qvt_, qt_)]; B = [sum(e2[k] * w[k] for k in range(3)) for w in (qv_, qvt_, qt_)]
    a0, a1, a2 = A; b0, b1, b2 = B
    res = (a0 * b2 - a2 * b0) ** 2 - (a0 * b1 - a1 * b0) * (a1 * b2 - a2 * b1)
    noteR = -mp.mpf(2) ** 29 * qq ** 10 * (6 * qq ** 2 + 1) * (12 * qq ** 2 + 1) ** 2 / (8 * qq ** 2 + 1) ** 4
    return res, noteR
rr = [(qs_, frame_res(qs_, 1)) for qs_ in ["0.2", "0.5", "1", "2"]]
ratios = [float(a / b) for _, (a, b) in rr]
check("the resultant of the transverse forms of the orthonormal-basis Pauli vector is negative at every tested q (the sign statement of item 6 holds), while its ratio to the printed resultant is not a constant (the printed magnitude is frame-dependent)",
      all(a < 0 for _, (a, b) in rr) and max(ratios) / min(ratios) > 10, "; ".join(f"q = {q_}: true {float(a):.6g}, printed {float(b):.6g}, ratio {float(a / b):.4g}" for q_, (a, b) in rr))
rng_ = np.random.default_rng(11); ok_inv = True
def resq(a, b):
    a0, a1, a2 = a; b0, b1, b2 = b
    return (a0 * b2 - a2 * b0) ** 2 - (a0 * b1 - a1 * b0) * (a1 * b2 - a2 * b1)
for _ in range(400):
    a = [Fr(int(x)) for x in rng_.integers(-9, 10, 3)]; b = [Fr(int(x)) for x in rng_.integers(-9, 10, 3)]
    al, be, ga, de = [Fr(int(x)) for x in rng_.integers(-9, 10, 4)]
    a2_ = [al * a[i] + be * b[i] for i in range(3)]; b2_ = [ga * a[i] + de * b[i] for i in range(3)]
    ok_inv &= resq(a2_, b2_) == (al * de - be * ga) ** 2 * resq(a, b)
check("exact rational check on 400 random binary quadratics: Res(alpha A + beta B, gamma A + delta B) = (alpha delta - beta gamma)^2 Res(A, B), so the sign of the resultant is frame-independent (item 6's conclusion survives the normalization problem)", ok_inv)
print(f"   total {time.time() - T0:.0f}s")
# the checks above each PASS when the evidence was obtained; the defect is demonstrated when all of the evidence checks passed
EVIDENCE = ["exact in q", "exact: the ratio", "40 digits, six q", "basis-free slope", "the eps^4 coefficient", "the PR runner's identity line"]
defect = FAIL == 0 and PASS >= 10
if defect:
    print("SUMMARY: normalization defect: the printed Pauli vector n of item 4 is not the Pauli vector of any orthonormal kernel basis: c |n_printed|^2 - 2 pi^2 h = 3072 pi^2 q^2 (8q^2+1)/(4q^2+1) > 0 for every q > 0 (|n_printed|^2/|n|^2 = 3.80, 4.00, 3.33, 2.73 at q = 0.2, 1/2, 1, 2, where 2 pi^2 h/c is the value fixed by the Hessian of item 3 and confirmed by the basis-free slope of the middle bands), so item 5 as written (c |d|^2 with the printed d) is false in its u^2 term; the runner verifies a different identity with a metric factor (n1 n2)^-1; the printed A, B and the magnitude of the resultant depend on the frame, while the sign of the resultant (item 6's charge-two conclusion) is frame-independent and stands")
    print("HIT: item 4's printed n is not the Pauli vector of the effective Hamiltonian, and item 5's identity c |d|^2 as stated fails for it (exactly: c |n_printed|^2 - 2 pi^2 h(q) = 3072 pi^2 q^2 (8q^2 + 1)/(4 q^2 + 1)); the runner checks the identity with an unnormalised-kernel-basis metric factor (n1 n2)^-1 that the note omits; item 6's sign conclusion is unaffected")
else:
    print("SUMMARY: no normalization defect demonstrated: " + "; ".join(HITS))
sys.exit(0)
