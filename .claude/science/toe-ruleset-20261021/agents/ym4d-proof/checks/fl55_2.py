#!/usr/bin/env python3
"""fl55_2 -- value-function (envelope) jets, exact.  Criteria: checks/fl55_2_criteria.md (written first).
Plain python + sympy exact rationals; no numpy, no floats in verdicts."""
import itertools, random
import sympy as sp

rng = random.Random(5502)
def rr():
    return sp.Rational(rng.randint(-5, 5), rng.randint(1, 4))

u1, u2, v1, v2, s = sp.symbols('u1 u2 v1 v2 s')
U = [u1, u2]; Vv = [v1, v2]; allv = U + Vv
A = sp.Matrix([[3, 1], [1, 2]])
B = sp.Matrix(2, 2, lambda i, j: rr())
C = sp.Matrix(2, 2, lambda i, j: rr()); C = (C + C.T) / 2
Um = sp.Matrix(U); Vm = sp.Matrix(Vv)
f = (sp.Rational(1, 2) * (Um.T * A * Um)[0] + (Um.T * B * Vm)[0] + sp.Rational(1, 2) * (Vm.T * C * Vm)[0])
for deg in (3, 4):
    for combo in itertools.combinations_with_replacement(allv, deg):
        f += rr() * sp.Mul(*combo)
f = sp.expand(f)

def truncate(expr, vars_, maxdeg):
    p = sp.Poly(sp.expand(expr), *vars_)
    return sum(c * sp.Mul(*[v ** e for v, e in zip(vars_, mon)]) for mon, c in p.terms() if sum(mon) <= maxdeg)

# U*(V) as a polynomial of degree 3 in V: fixed-point iteration U <- -A^{-1}(grad_U f - A U)
Ainv = A.inv()
grad = [sp.diff(f, ui) for ui in U]
Ustar = [sp.Integer(0), sp.Integer(0)]
for it in range(6):
    sub = {u1: Ustar[0], u2: Ustar[1]}
    g = sp.Matrix([sp.expand(gi.subs(sub, simultaneous=True)) for gi in grad])
    Ucur = sp.Matrix(Ustar)
    new = Ucur - Ainv * g
    Ustar = [truncate(new[0], Vv, 3), truncate(new[1], Vv, 3)]
sub = {u1: Ustar[0], u2: Ustar[1]}
res = [truncate(gi.subs(sub, simultaneous=True), Vv, 3) for gi in grad]
E0 = all(sp.expand(r) == 0 for r in res)
print(f"E0 critical family (grad_U f has no terms of degree <= 3): {'PASS' if E0 else 'FAIL'}  residuals={res}")

W = truncate(f.subs(sub, simultaneous=True), Vv, 4)

# derivatives of f at 0 as multilinear forms via directional derivatives along a line
def D_k_f(k, vec):
    # D^k f(0)[vec^k] = d^k/ds^k f(s*vec)|_{s=0}
    expr = f.subs({x: s * vx for x, vx in zip(allv, vec)}, simultaneous=True)
    return sp.diff(expr, s, k).subs(s, 0)
def D_k_W(k, v):
    expr = W.subs({v1: s * v[0], v2: s * v[1]}, simultaneous=True)
    return sp.diff(expr, s, k).subs(s, 0)

# U*'(0) v : linear part of Ustar
def Ulin(v):
    return [sp.expand(truncate(Ui, Vv, 1)).subs({v1: v[0], v2: v[1]}) for Ui in Ustar]

def c_vec(zeta):
    # c_i = d/dU_i of D^3 f(0)[zeta, zeta, .]  =  third mixed derivative contracted
    out = []
    for i in range(2):
        # D^3 f(0)[zeta, zeta, e_i] = (1/2) d^2/ds^2 d/dt f(s*zeta + t*e_i) at 0
        t = sp.symbols('t')
        ei = [0, 0, 0, 0]; ei[i] = 1
        expr = f.subs({x: s * zx + t * ex for x, zx, ex in zip(allv, zeta, ei)}, simultaneous=True)
        val = sp.diff(expr, s, 2, t, 1).subs({s: 0, t: 0})
        out.append(val)
    return sp.Matrix(out)

tests = [(1, 0), (0, 1), (1, 1), (2, -3), (-1, 4)]
E3ok = True; E4ok = True; E3c_fires = False; E4c_fires = False
for v in tests:
    ul = Ulin(v)
    zeta = [ul[0], ul[1], v[0], v[1]]
    d3W = D_k_W(3, v); d3f = D_k_f(3, zeta)
    d4W = D_k_W(4, v); d4f = D_k_f(4, zeta)
    cv = c_vec(zeta)
    exch = (cv.T * Ainv * cv)[0]
    e3 = sp.simplify(d3W - d3f) == 0
    e4 = sp.simplify(d4W - (d4f - 3 * exch)) == 0
    E3ok &= e3; E4ok &= e4
    d3f_naive = D_k_f(3, [0, 0, v[0], v[1]])
    if sp.simplify(d3W - d3f_naive) != 0: E3c_fires = True
    if sp.simplify(d4W - d4f) != 0: E4c_fires = True
    print(f"v={v}: D3W={d3W}  D3f[zeta^3]={d3f}  | D4W={d4W}  D4f[zeta^4]-3c^TA^-1c={sp.simplify(d4f - 3*exch)}  (exchange={exch})")
print(f"E3 single pullback: {'PASS' if E3ok else 'FAIL'}")
print(f"E4 quartic with exchange: {'PASS' if E4ok else 'FAIL'}")
print(f"E3-c (zeta -> (0,v)) differs: {'control fires' if E3c_fires else 'CONTROL DOES NOT FIRE'}")
print(f"E4-c (exchange dropped) differs: {'control fires' if E4c_fires else 'CONTROL DOES NOT FIRE'}")
overall = E0 and E3ok and E4ok and E3c_fires and E4c_fires
print("=== fl55_2 SUMMARY ===")
print("OVERALL:", "PASS" if overall else ("INVALID (a control did not fire)" if (E0 and E3ok and E4ok) else "FAIL"))
