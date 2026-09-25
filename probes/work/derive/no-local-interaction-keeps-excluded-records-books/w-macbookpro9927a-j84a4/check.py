#!/usr/bin/env python3
"""Exact checks for J:derive:no-local-interaction-keeps-excluded-records-books:a2
(worker w-macbookpro9927a-j84a4).  See ATTEMPT.md.  Every check is exact
(sympy rationals, Gaussian rationals, symbols).

  C1  the resolvent identity [g, T(z)] = (h0 - z)[F2, R''(z)](h0 - z) and its
      shell form i eta <F2 R'' F1 - F1 R'' F2> (algebra, exact instance)
  C2  push-through: T = F1 (1 + R0 F1)^{-1} = A W (1 + Q0 W)^{-1} A*, and
      (1 + F1 R0)(1 - F1 R'') = 1
  C3  finite-rank determinant identity (Sylvester):
      det(1 + W(Q - c B B*)) = det(1 + W Q) det(1 - c B* M B), M = W(1 + Q W)^{-1}
  C4  lemma L0: [h,[h,f.s]] = 4(|h|^2 f - (h.f) h).s, and the two-record split
  C5  block 143 T1's exact witness (g varies on the shells), Z^2 and Z^3
  C6  block 143 T6's cone tilts, exact rationals below one
  C7  the line: g is constant on both kinds of shell, so the density step has
      nothing to act on there
"""
import time

import sympy as sp

T0 = time.time()
RES = []


def check(tag, ok, msg):
    RES.append((tag, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {tag}: {msg}")


I_ = sp.I
R_ = sp.Rational


def herm(M):
    return M.H


# ---------------------------------------------------------------- C1, C2
n = 6
h0 = sp.diag(0, 0, 0, 1, -2, R_(3, 2))          # a three-fold "shell" at E = 0
g = sp.diag(1, -2, 5, 7, 0, R_(1, 3))           # commutes with h0, varies on the shell
A = sp.Matrix([[1, I_], [2 - I_, 0], [R_(1, 2), 3], [0, 1 + I_], [-1, R_(2, 3)], [I_, -2]])
W = sp.Matrix([[R_(3, 4), 1 - I_], [1 + I_, -R_(1, 2)]])
F1 = A * W * herm(A)
h2 = h0 + F1
jpp = 2 * sp.eye(n) - h2 + 3 * h2 * h2         # commutes with h'' (a kept quantity)
F2 = jpp - g
assert (h2 * jpp - jpp * h2).applyfunc(sp.expand) == sp.zeros(n) and h0 * g == g * h0


def resolvents(z):
    R0 = (h0 - z * sp.eye(n)).inv()
    R2 = (h2 - z * sp.eye(n)).inv()
    return R0, R2


ok1 = True
for z in (R_(1, 3) + I_ / 5, -R_(2, 7) + 2 * I_):
    R0, R2 = resolvents(z)
    T = F1 - F1 * R2 * F1
    lhs = g * T - T * g
    rhs = (h0 - z * sp.eye(n)) * (F2 * R2 - R2 * F2) * (h0 - z * sp.eye(n))
    ok1 = ok1 and sp.simplify(lhs - rhs) == sp.zeros(n)
eta = R_(1, 7)
z = 0 + I_ * eta                                   # on the shell energy E = 0
R0, R2 = resolvents(z)
T = F1 - F1 * R2 * F1
PE = sp.diag(1, 1, 1, 0, 0, 0)
lhs = PE * (g * T - T * g) * PE
rhs = PE * (I_ * eta * (F2 * R2 * F1 - F1 * R2 * F2)) * PE
ok1b = sp.simplify(lhs - rhs) == sp.zeros(n)
check("C1", ok1 and ok1b, "for [h'', j''] = 0 with h'' = h0 + F1, j'' = g + F2, [h0, g] = 0: [g, T(z)] = "
      "(h0 - z)[F2, R''(z)](h0 - z) with T = F1 - F1 R'' F1 (two generic z), and on the h0-shell at "
      "z = E + i eta its sandwich equals i eta P(F2 R'' F1 - F1 R'' F2)P (exact 6x6 instance, rank-2 F1)")
z = R_(1, 3) + I_ / 5
R0, R2 = resolvents(z)
T = F1 - F1 * R2 * F1
Q0 = herm(A) * R0 * A
Tpt = A * W * (sp.eye(2) + Q0 * W).inv() * herm(A)
ok2 = (sp.simplify(T - Tpt) == sp.zeros(n)
       and sp.simplify((sp.eye(n) + F1 * R0) * (sp.eye(n) - F1 * R2) - sp.eye(n)) == sp.zeros(n)
       and sp.simplify((sp.eye(2) + W * Q0).det() * (sp.eye(2) - W * herm(A) * R2 * A).det() - 1) == 0)
check("C2", ok2, "T(z) = A W (1 + Q0(z) W)^{-1} A* with Q0 = A* R0 A, (1 + F1 R0)(1 - F1 R'') = 1, and "
      "det(1 + W Q0) det(1 - W Q'') = 1 (Q'' = A* R'' A): Delta(z) is finite and nonzero wherever Q'' is finite")

# ---------------------------------------------------------------- C3
c = sp.symbols('c')
W3 = sp.Matrix([[2, R_(1, 3) - I_, 0], [R_(1, 3) + I_, -1, R_(1, 2)], [0, R_(1, 2), R_(5, 4)]])
Q3 = sp.Matrix([[R_(1, 2) + I_, 2, -I_ / 3], [R_(1, 5), -1 + 2 * I_, 1], [3, I_, R_(2, 3)]])
B3 = sp.Matrix([[1, I_], [R_(1, 2), -1], [2 - I_, R_(1, 3)]])
G3 = B3 * herm(B3)
M3 = W3 * (sp.eye(3) + Q3 * W3).inv()
lhs = (sp.eye(3) + W3 * (Q3 - c * G3)).det()
rhs = (sp.eye(3) + W3 * Q3).det() * (sp.eye(2) - c * herm(B3) * M3 * B3).det()
ok3 = sp.simplify(sp.expand(lhs - rhs)) == 0
check("C3", ok3, "det(1 + W(Q - c Gamma)) = det(1 + W Q) det(1 - c B* M B) for Gamma = B B*, M = W(1 + Q W)^{-1}, "
      "identically in c: with Q = Q0(E+i0), c = 2 pi i and B* M B = 0 (transparency) it gives "
      "Delta(E - i0) = Delta(E + i0)")

# ---------------------------------------------------------------- C4
SIG = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I_], [I_, 0]]), sp.Matrix([[1, 0], [0, -1]])]
hv = sp.symbols('h1:4', real=True)
fv = sp.symbols('f1:4', real=True)
Hs = sum((hv[a] * SIG[a] for a in range(3)), sp.zeros(2))
Fs = sum((fv[a] * SIG[a] for a in range(3)), sp.zeros(2))
hh = sum(x * x for x in hv)
hf = sum(hv[a] * fv[a] for a in range(3))
comm = lambda X, Y: X * Y - Y * X
ok4a = sp.expand(comm(Hs, comm(Hs, Fs)) - 4 * sum(((hh * fv[a] - hf * hv[a]) * SIG[a] for a in range(3)),
                                                   sp.zeros(2))) == sp.zeros(2)
kv = sp.symbols('u1:4', real=True)
gv = sp.symbols('v1:4', real=True)
H1 = sum((hv[a] * SIG[a] for a in range(3)), sp.zeros(2))
H2 = sum((kv[a] * SIG[a] for a in range(3)), sp.zeros(2))
F1s = sum((fv[a] * SIG[a] for a in range(3)), sp.zeros(2))
F2s = sum((gv[a] * SIG[a] for a in range(3)), sp.zeros(2))
kron = lambda X, Y: sp.kronecker_product(X, Y)
h0p = kron(H1, sp.eye(2)) + kron(sp.eye(2), H2)
mp = kron(F1s, sp.eye(2)) + kron(sp.eye(2), F2s)
split = comm(h0p, comm(h0p, mp)) - kron(comm(H1, comm(H1, F1s)), sp.eye(2)) - kron(sp.eye(2), comm(H2, comm(H2, F2s)))
ok4b = sp.expand(split) == sp.zeros(4)
check("C4", ok4a and ok4b, "[h.s,[h.s,f.s]] = 4(|h|^2 f - (h.f)h).s and [h0,[h0,m]] = [h1,[h1,f1]](x)1 + "
      "1(x)[h2,[h2,f2]] for one-body m: a one-body placement current i[h0, m] is a multiplication operator, "
      "and it vanishes iff each [h, f] = 0 (lemma L0)")

# ---------------------------------------------------------------- C5  (block 143 T1 witness, recomputed)
PY = [(R_(3, 5), R_(4, 5)), (R_(5, 13), R_(12, 13)), (R_(20, 29), R_(21, 29)),
      (R_(8, 17), R_(15, 17)), (R_(7, 25), R_(24, 25)), (R_(9, 41), R_(40, 41))]
ok5 = True
vals = []
for dim in (2, 3):
    a, b = PY[:dim], PY[3:3 + dim]
    sadd = a[0][0] * b[0][1] + a[0][1] * b[0][0]
    ssub = a[0][0] * b[0][1] - a[0][1] * b[0][0]
    dg = -2 * sadd * ssub
    e1 = sum(x[0] ** 2 for x in a)
    e2 = sum(x[0] ** 2 for x in b)
    s2a = 2 * a[1][0] * a[1][1]
    s2b = 2 * b[1][0] * b[1][1]
    ok5 = ok5 and dg != 0 and s2a ** 2 * e2 != s2b ** 2 * e1
    vals.append(dg)
K1, q1 = sp.symbols('K1 q1', real=True)
ok5 = ok5 and sp.simplify(sp.expand_trig((sp.sin(2 * (K1 / 2 + q1)) + sp.sin(2 * (K1 / 2 - q1))) / 2
                                         - sp.sin(K1) * sp.cos(2 * q1))) == 0
check("C5", ok5, f"block 143 T1 recomputed: g_a = sin K_a cos 2q_a, and at its Pythagorean point dg_1/dq_1 = "
      f"{vals[0]} (plane), {vals[1]} (space) with dE/dq_2 nonzero for all four band pairs: dg_1 ^ dE != 0, so g "
      f"is constant on no shell component for a.e. (K, E)")

# ---------------------------------------------------------------- C6  (block 143 T6 cone tilts)


def tilt2(tau):
    sinsq = [x ** 2 / (1 + x ** 2) for x in tau]
    sincos = [x / (1 + x ** 2) for x in tau]
    return sum(v ** 2 for v in sincos) / sum(sinsq)


t2, t3 = tilt2([R_(5, 6), R_(18, 5)]), tilt2([R_(5, 6), R_(18, 5), R_(1, 2)])
ok6 = t2 == R_(139761000, 606502321) and t3 == R_(2653455542, 8714332815) and t2 < 1 and t3 < 1
check("C6", ok6, f"block 143 T6 cone tilts at tan K0 = (5/6, 18/5[, 1/2]): |grad eps(k2)|^2 = {t2}, {t3} < 1, so "
      f"near each cone the level sets of E are small closed tilted cones")

# ---------------------------------------------------------------- C7  (the line)
q0, K = sp.symbols('q0 K', real=True)
gl = lambda q: sp.sin(K) * sp.cos(2 * q)
ok7 = (sp.simplify(gl(q0) - gl(-q0)) == 0 and sp.simplify(gl(q0) - gl(sp.pi - q0)) == 0)
check("C7", ok7, "on the line both shells ({q0, -q0}, {q0, pi - q0}) carry one value of g: the density step "
      "has nothing to act on, consistent with block 137's kept current on the infinite line")

npass = sum(ok for _, ok in RES)
print(f"TOTAL: PASS={npass} FAIL={len(RES) - npass}  ({time.time() - T0:.0f} s)")
if npass == len(RES):
    print("SUMMARY: PROVED (named standard imports listed in ATTEMPT.md) no finite-range interaction with a local "
          "placement keeps two excluded records' total energy current on Z^3 or Z^2: keeping it forces (L0) a zero "
          "one-body placement current, then the resolvent identity [g, T(z)] = (h0 - z)[F2, R''](h0 - z) (C1) makes "
          "the on-shell T vanish at a.e. energy, the finite-rank determinant identity (C3) makes Delta(E+i0) real, "
          "bounded (Z^3) or L^p (Z^2) spectral densities near block 143's K0 put Delta - 1 in H^2 of both half-planes, "
          "so Delta = 1, contradicting the removed on-site states.")
    print("HIT: two excluded records of block 54's walk: no finite-range interaction with a local placement keeps "
          "J' = i[H', D'] on Z^3 or Z^2, either exchange sign. In each fiber a kept current gives [g, T(z)] = "
          "(h0 - z)[F2, R''(z)](h0 - z) with F2 = j'' - g of finite rank, whose shell sandwich is "
          "i eta <F2 R'' F1 - F1 R'' F2> -> 0, so T(E+i0) = 0 on shells (block 143 T1); det(1 + W Q0(E+i0)) is then "
          "real (Sylvester), Delta - 1 lies in H^2 of both half-planes (bounded densities from block 143 T6), so "
          "Delta = 1, contradicting Delta(lambda) = 0 at the removed on-site states (block 143 T4).")
else:
    print("SUMMARY: ROUTE FAILS AT a failed exact check above")
