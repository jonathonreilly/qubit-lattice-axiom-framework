#!/usr/bin/env python3
"""B11 exact number-field data for the step factors (sympy).

K = Q(sqrt2, sqrt3, i); Q(zeta8) = Q(sqrt2, i) is the fixed field of sigma: sqrt3 -> -sqrt3.
Obstruction used: if a physical unitary with entries in Z[1/sqrt2, i] (any exact Clifford+T circuit, ancillas
in |0> returned to |0>, no measurement) acts on the corner code as Gamma(W) up to phase, then every product
W_ia conj(W_jb) lies in Q(zeta8) (coefficients of Gamma Q(c+_a c_b) Gamma^dag in the linearly independent
logical bilinears, extracted with traces against the code projector, whose entries lie in Q(i)).
"""
import sys, os, itertools
import numpy as np, sympy as sp
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import io, contextlib
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    import circuit as CC
PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''), flush=True)
s2, s3, I = sp.sqrt(2), sp.sqrt(3), sp.I
def exact_int(M):
    return sp.Matrix(M.shape[0], M.shape[1], lambda i, j: sp.Integer(int(round(M[i, j].real))) + I * sp.Integer(int(round(M[i, j].imag))))
Hon = exact_int(CC.Hon); Lam = exact_int(CC.Lam)
assert np.allclose(np.array(Hon.evalf(), dtype=complex), CC.Hon) and np.allclose(np.array(Lam.evalf(), dtype=complex), CC.Lam)
def proj(M, lam, others):
    P = sp.eye(12)
    for mu in others: P = P * (M - mu * sp.eye(12)) / (lam - mu)
    return P.applyfunc(sp.expand)
eH = [-1 - s3, -1 + s3, 2]; eL = [-2 * s2, -s2, s2, 2 * s2]
PH = [proj(Hon, l, [m for m in eH if m != l]) for l in eH]
PL = [proj(Lam, l, [m for m in eL if m != l]) for l in eL]
UH = (PH[0] - PH[1] - I * PH[2]).applyfunc(sp.expand); UL = (PL[0] + I * PL[1] + I * PL[2] + PL[3]).applyfunc(sp.expand)
num = lambda M: np.array(M.evalf(30), dtype=complex)
check("exact eigenprojector formulas reproduce the numerical U_H and U_L of the runner construction",
      np.allclose(num(UH), CC.UH) and np.allclose(num(UL), CC.UL))
sigma = lambda x: x.xreplace({s3: -s3})
def in_qz8(x): return abs(complex(sp.N(x - sigma(x), 40))) < 1e-30
print("distinct U_H entries:", sorted({str(sp.nsimplify(x)) for x in UH}, key=len)[:8])
print("distinct U_L entries:", sorted({str(sp.nsimplify(x)) for x in UL}, key=len)[:10])
uh_bad = [x for x in UH if not in_qz8(x)]; ul_bad = [x for x in UL if not in_qz8(x)]
check("U_L has all entries in Q(zeta8) (= Q(sqrt2, i)); U_H has entries outside it (sqrt3)", not ul_bad and len(uh_bad) > 0,
      f"{len(uh_bad)} U_H entries contain sqrt3")
# U_L: entries lie in Q(i); ring-level test. Recorded: an earlier version of this check asserted U_L entries lie in
# Z[1/sqrt2, i]; that FAILED (entries 1/3 + 2i/3, (1 - i)/6). The corrected statement is tested here.
def dyadic_gauss(z):
    z = sp.nsimplify(sp.expand(z)); re, im = sp.Rational(sp.re(z)), sp.Rational(sp.im(z))
    return all((r.q & (r.q - 1)) == 0 for r in (re, im))
badUL = None
for a, b in itertools.permutations(range(12), 2):
    for i, j in itertools.permutations(range(12), 2):
        z = sp.expand(UL[i, a] * sp.conjugate(UL[j, b]))
        if z != 0 and not dyadic_gauss(z): badUL = (i, j, a, b, sp.nsimplify(z)); break
    if badUL: break
check("U_L entries lie in Q(i) but not in Z[1/sqrt2, i] (denominator 3): some product U_ia conj(U_jb), i != j, a != b, is not "
      "dyadic, so U_L has no exact measurement-free Clifford+T implementation either", badUL is not None and
      all(sp.nsimplify(x).is_real is not None and not sp.nsimplify(x).has(s2) for x in UL), f"e.g. {badUL[-1] if badUL else None}")
# W columns for inputs at site 0
nV = CC.nV; VID = CC.VID; CORN = CC.CORN
V = (UH * UL).applyfunc(sp.expand)
loc0 = CC.loc0
def ex(x):
    if abs(x) < 1e-12: return sp.Integer(0)
    if np.isclose(abs(x), 1): return sp.Integer(int(np.sign(x)))
    assert np.isclose(abs(x), 1 / np.sqrt(2)); return int(np.sign(x)) / s2
cols = {}
for a in range(2):
    vin = {loc0[m]: V[m, a] for m in range(12) if V[m, a] != 0}
    w1 = {}
    for j, val in vin.items():
        for i in np.nonzero(np.abs(CC.RLr[:, j]) > 1e-12)[0]:
            w1[i] = w1.get(i, 0) + ex(CC.RLr[i, j]) * val
    w2 = {}
    for j, val in w1.items():
        for i in np.nonzero(np.abs(CC.Sr[:, j]) > 1e-12)[0]:
            w2[i] = w2.get(i, 0) + ex(CC.Sr[i, j]) * val
    cols[a] = {i: sp.expand(v) for i, v in w2.items()}
    ok = all(abs(complex(sp.N(v)) - CC.Wref[i, loc0[a]]) < 1e-12 for i, v in cols[a].items()) and \
         np.isclose(sum(abs(CC.Wref[:, loc0[a]]) ** 2), 1)
    assert ok
found = None
for i, x in cols[0].items():
    for j, y in cols[1].items():
        z = sp.expand(x * sp.conjugate(y))
        if not in_qz8(z): found = (i, j, z); break
    if found: break
check("exact W columns (inputs at site 0) agree with the numerical W; some product W_ia conj(W_jb) (a != b) lies outside Q(zeta8): "
      "no exact measurement-free Clifford+T circuit on the corner code implements the step", found is not None,
      f"e.g. W_ia conj(W_jb) = {sp.nsimplify(found[2]) if found else None}")
print(f"\nexact_field TOTAL: PASS={PASS} FAIL={FAIL}")
