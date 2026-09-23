#!/usr/bin/env python3
"""Turns the LP-proposed joint certificates in data.json into exact ones: on the support rows (recomputed exactly), impose
the constraints the solver left active, (A^T y)_j = 0, and y.(A l) = 1; solve in rationals; keep y only if every
(A^T y)_j >= 0 exactly. usage: exactify.py key [key ...]   (keys of data.json: cert_joint_base_c1, ...)"""
import ast
import json
import os
import sys
from fractions import Fraction as Fr

import sympy as sp
from sympy.polys.matrices import DomainMatrix

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from clocklib import Torus, is_move  # noqa: E402

W = {"c1": (Fr(3), Fr(1), Fr(2)), "c0": (Fr(3, 2), Fr(1, 2), Fr(1))}
path = os.path.join(HERE, "data.json")
D = json.load(open(path))
TORI = {}


def rq(s):
    a, b = s.split("/")
    return Fr(int(a), int(b))


for key in sys.argv[1:]:
    parts = key.split("_")                      # cert_joint_{mode}_{name} or cert_Z3_{mode}_{name}
    mode, name = parts[2], parts[3]
    L = 6 if parts[1] == "Z3" else 3
    T = TORI.setdefault(L, Torus(L))
    w = W[name]
    sup = list(D[key].items())
    rows = []
    for kc, yy in sup:
        pos, con = ast.literal_eval(kc.split("|")[0]), ast.literal_eval(kc.split("|")[1])
        occ = [-1] * T.N
        for p_, c_ in zip(pos, con):
            occ[p_] = c_
        rows.append(T.row(pos, occ, w, mode, Fr(1)))
    yf = [float(rq(yy)) for _, yy in sup]
    keys = sorted({k for r in rows for k in r}, key=repr)
    ATy = {k: sum(r.get(k, 0) * yv for r, yv in zip(rows, yf)) for k in keys}
    active = [k for k in keys if abs(float(ATy[k])) < 1e-7]
    n = len(rows)
    M = [[sp.QQ(r.get(k, Fr(0)).numerator, r.get(k, Fr(0)).denominator) for r in rows] + [sp.QQ(0)] for k in active]
    al = [sum(c for k, c in r.items() if is_move(k)) for r in rows]
    M.append([sp.QQ(a.numerator, a.denominator) for a in al] + [sp.QQ(1)])
    R, piv = DomainMatrix(M, (len(M), n + 1), sp.QQ).rref()
    Rm = R.to_Matrix()
    free = [j for j in range(n) if j not in piv]
    # particular solution: free variables at their rationalised float values
    y = [None] * n
    for j in free:
        y[j] = Fr(yf[j]).limit_denominator(10 ** 6)
    for rr, p in enumerate(piv):
        if p == n:
            raise SystemExit(f"{key}: inconsistent")
        val = Fr(int(Rm[rr, n].p), int(Rm[rr, n].q))
        for j in free:
            val -= Fr(int(Rm[rr, j].p), int(Rm[rr, j].q)) * y[j]
        y[p] = val
    ATy_ex = {k: sum(r.get(k, 0) * yv for r, yv in zip(rows, y)) for k in keys}
    yl = sum(a * yv for a, yv in zip(al, y))
    good = all(v >= 0 for v in ATy_ex.values()) and yl > 0
    print(key, "support", n, "active", len(active), "free", len(free), "exact:", good, "y.(A l) =", yl)
    if good:
        D[key] = {kc: f"{v.numerator}/{v.denominator}" for (kc, _), v in zip(sup, y) if v != 0}
json.dump(D, open(path, "w"), indent=0)
