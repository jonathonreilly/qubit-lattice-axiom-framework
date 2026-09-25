#!/usr/bin/env python3
"""Exact checks for J:derive:nondegenerate-stationary-points-of-the-pair-bands-at-one-wave-vector:a1
(worker w-macbookpro9927a-j546d).  An algebraic certificate of block 143's (A') / T6: a Groebner
basis equal to [1] shows that the polynomial system "stationary point of some band pair, off the
cones, with zero Hessian determinant" has no solution at all, even over C.

Variables: C_a = cos 2k1_a, S_a = sin 2k1_a on the unit circle, so every function is a polynomial and
no chart point is missed; e1 = s1 eps(k1), e2 = s2 eps(k2) signed (one system covers all four band
pairs); z e1 e2 = 1 removes the cones.  All arithmetic is exact (sympy over Q).
"""
import time

import sympy as sp

T0 = time.time()
RES = []


def check(tag, ok, msg):
    RES.append((tag, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {tag}: {msg}")


def system(tK, with_hessian=True):
    d = len(tK)
    Cs = sp.symbols(f'C1:{d + 1}')
    Ss = sp.symbols(f'S1:{d + 1}')
    e1, e2, z = sp.symbols('e1 e2 z')
    CK = [(1 - t ** 2) / (1 + t ** 2) for t in tK]          # cos 2K0_a
    SK = [2 * t / (1 + t ** 2) for t in tK]                 # sin 2K0_a
    C2k = [CK[a] * Cs[a] + SK[a] * Ss[a] for a in range(d)]  # cos 2k2_a, k2 = K0 - k1
    S2k = [SK[a] * Cs[a] - CK[a] * Ss[a] for a in range(d)]  # sin 2k2_a
    f1 = sum((1 - Cs[a]) / 2 for a in range(d))             # eps(k1)^2 = sum sin^2 k1_a
    f2 = sum((1 - C2k[a]) / 2 for a in range(d))
    # E(q) = e1 + e2, k1 = K0/2 + q, k2 = K0/2 - q:  dE/dq_a = S_a/(2 e1) - S2k_a/(2 e2)
    stat = [sp.expand(Ss[a] * e2 - S2k[a] * e1) for a in range(d)]

    def hess(Cv, Sv, e):
        # s * d2 eps/dk dk = f_ab/(2e) - f_a f_b/(4e^3), f_a = sin 2k_a, f_ab = 2 cos 2k_a delta_ab, e = s eps
        return sp.Matrix(d, d, lambda a, b: (2 * Cv[a] if a == b else 0) / (2 * e) - Sv[a] * Sv[b] / (4 * e ** 3))

    Hq = hess(Cs, Ss, e1) + hess(C2k, S2k, e2)             # d2E/dq dq (the two sign flips from k2 cancel)
    eqs = [Cs[a] ** 2 + Ss[a] ** 2 - 1 for a in range(d)] + [sp.expand(e1 ** 2 - f1), sp.expand(e2 ** 2 - f2)]
    eqs += stat + [sp.expand(z * e1 * e2 - 1)]
    if with_hessian:
        eqs.append(sp.expand(sp.numer(sp.together(Hq.det()))))
    gens = [z, e1, e2, *Cs, *Ss]
    return eqs, gens, (Cs, Ss, e1, e2, C2k, S2k, f1, f2, stat, Hq)


# ------------------------------------------------------------ V1: the formulas against direct differentiation
k = sp.symbols('k1:3', real=True)
tK2 = [sp.Rational(5, 6), sp.Rational(18, 5)]
K0 = [sp.atan(t) for t in tK2]
ok1 = True
eqs2, gens2, parts = system(tK2)
Cs, Ss, e1, e2, C2k, S2k, f1, f2, stat, Hq = parts
q = sp.symbols('q1:3', real=True)
for s1 in (1, -1):
    for s2 in (1, -1):
        k1 = [K0[a] / 2 + q[a] for a in range(2)]
        k2 = [K0[a] / 2 - q[a] for a in range(2)]
        E = s1 * sp.sqrt(sum(sp.sin(x) ** 2 for x in k1)) + s2 * sp.sqrt(sum(sp.sin(x) ** 2 for x in k2))
        pt = {q[0]: sp.Rational(1, 3), q[1]: -sp.Rational(2, 7)}
        grad = [sp.diff(E, q[a]).subs(pt) for a in range(2)]
        hes = sp.Matrix(2, 2, lambda a, b: sp.diff(E, q[a], q[b]).subs(pt))
        rep = {Cs[a]: sp.cos(2 * k1[a].subs(pt)) for a in range(2)}
        rep.update({Ss[a]: sp.sin(2 * k1[a].subs(pt)) for a in range(2)})
        rep[e1] = s1 * sp.sqrt(sum(sp.sin(x.subs(pt)) ** 2 for x in k1))
        rep[e2] = s2 * sp.sqrt(sum(sp.sin(x.subs(pt)) ** 2 for x in k2))
        g_form = [(Ss[a] / (2 * e1) - S2k[a] / (2 * e2)).subs(rep) for a in range(2)]
        h_form = Hq.subs(rep)
        ok1 = ok1 and all(abs(sp.N(grad[a] - g_form[a], 40)) < sp.Float('1e-30') for a in range(2))
        ok1 = ok1 and all(abs(sp.N(hes[a, b] - h_form[a, b], 40)) < sp.Float('1e-30') for a in range(2) for b in range(2))
check("V1", ok1, "the polynomial gradient and Hessian in (C, S, e) agree with direct differentiation of "
      "E(q) = s1 eps(K0/2 + q) + s2 eps(K0/2 - q) for all four band pairs at a test point (40-digit agreement, "
      "a labelled numeric control of the algebra)")

# ------------------------------------------------------------ G2: the plane
t2 = time.time()
G2 = sp.groebner(eqs2, *gens2, order='grevlex')
ok2 = list(G2.exprs) == [1]
eqs2n, gens2n, _ = system(tK2, with_hessian=False)
G2n = sp.groebner(eqs2n, *gens2n, order='grevlex')
ok2n = list(G2n.exprs) != [1]
check("G2", ok2 and ok2n, f"Z^2, tan K0 = (5/6, 18/5): Groebner basis of {{circles, e1^2 = eps(k1)^2, e2^2 = eps(k2)^2, "
      f"stationary, z e1 e2 = 1, det Hess = 0}} is [1] ({time.time() - t2:.1f} s): no degenerate stationary point of "
      f"any band pair off the cones, even over C; control: without det Hess the basis is not [1] (stationary "
      f"points exist)")

# ------------------------------------------------------------ G3: space
tK3 = [sp.Rational(5, 6), sp.Rational(18, 5), sp.Rational(1, 2)]
t3 = time.time()
eqs3, gens3, _ = system(tK3)
G3 = sp.groebner(eqs3, *gens3, order='grevlex')
ok3 = list(G3.exprs) == [1]
check("G3", ok3, f"Z^3, tan K0 = (5/6, 18/5, 1/2): the same system (det Hess numerator of degree 10) has Groebner "
      f"basis [1] ({time.time() - t3:.0f} s): every stationary point of every band pair off the cones is "
      f"nondegenerate")

# ------------------------------------------------------------ C0: a control where degeneracy is present
eqs0, gens0, _ = system([sp.Integer(0), sp.Integer(0)])
G0 = sp.groebner(eqs0, *gens0, order='grevlex')
ok0 = list(G0.exprs) != [1]
check("C0", ok0, "control at K0 = 0 (flat band E_{+-} = 0, so every point is a degenerate stationary point): the "
      "same system is not [1], so the certificate can fail")

# ------------------------------------------------------------ K1: cones


def tilt2(tau):
    return sum((x / (1 + x ** 2)) ** 2 for x in tau) / sum(x ** 2 / (1 + x ** 2) for x in tau)


ok4 = (tilt2(tK2) == sp.Rational(139761000, 606502321) and tilt2(tK3) == sp.Rational(2653455542, 8714332815)
       and tilt2(tK2) < 1 and tilt2(tK3) < 1)
check("K1", ok4, f"cones: at a cone of record 1 (eps(k1) = 0) the other record's energy has |grad|^2 = "
      f"{tilt2(tK2)} (plane), {tilt2(tK3)} (space) < 1 (and by symmetry at record 2's cones), so near a cone "
      f"E = tau + s1|y| + t.y + O(|y|^2) with |t| < 1: a strict conical minimum (s1 = +1) or maximum, not a smooth "
      f"stationary point, with closed tilted-cone level sets")

npass = sum(ok for _, ok in RES)
print(f"TOTAL: PASS={npass} FAIL={len(RES) - npass}  ({time.time() - T0:.0f} s)")
if npass == len(RES):
    print("SUMMARY: PROVED block 143's (A') at tan K0 = (5/6, 18/5) on Z^2 and (5/6, 18/5, 1/2) on Z^3 by an algebraic "
          "certificate independent of T6's resultants and interval boxes: in circle variables (cos 2k1, sin 2k1) with "
          "signed energies e1, e2 (all four band pairs at once) and z e1 e2 = 1 off the cones, the system 'stationary "
          "and det Hess = 0' has Groebner basis [1], so no degenerate stationary point exists even over C; a K0 = 0 "
          "control is not [1]; cones are strict conical extrema (tilt^2 < 1).")
    print("HIT: T6 of block 143 confirmed by a different method: at tan K0 = (5/6, 18/5) (Z^2) and (5/6, 18/5, 1/2) "
          "(Z^3) the ideal generated by C_a^2 + S_a^2 - 1, e1^2 - eps(k1)^2, e2^2 - eps(k2)^2, S_a e2 - S2k_a e1, "
          "z e1 e2 - 1 and the numerator of det Hess E has Groebner basis [1] (exact, sympy, 1 s and ~45 s): every "
          "stationary point of every band pair off the cones is nondegenerate, with no chart gaps and no interval "
          "arithmetic; cone tilts 139761000/606502321 and 2653455542/8714332815 < 1.")
else:
    print("SUMMARY: ROUTE FAILS AT a failed check above")
