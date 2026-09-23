#!/usr/bin/env python3
"""Proposes the rules and certificates that check.py verifies exactly (LP in floating point via HiGHS; every number is then
turned into a rational and re-checked by check.py in Fraction arithmetic). Writes data.json next to this file.
usage: make_data.py [L5]    (L5 adds the three-record rule on the 5^3 torus, slow)"""
import json
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np
import scipy.sparse as sps
import sympy as sp
from scipy.optimize import linprog
from sympy.polys.matrices import DomainMatrix

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from clocklib import Torus, is_move, kstr  # noqa: E402

WF = {"c1": (3.0, 1.0, 2.0), "c0": (1.5, 0.5, 1.0)}           # exact in binary floating point (products stay exact)
OUT = {}


def distinct_rows(T, sectors, mode, name, rowfun=None):
    """float rows (exact for these weights), deduplicated; one representative configuration per row"""
    keys, rows = {}, {}
    for nrec in sectors:
        for pos, con, occ in T.configs(nrec):
            if rowfun is None:
                r = T.row(pos, occ, WF[name], mode, 1.0)
                cand = [r]
            else:
                cand = rowfun(T, pos, occ, WF[name])
            for k_rec, r in enumerate(cand):
                for k in r:
                    if k not in keys:
                        keys[k] = len(keys)
                key = tuple(sorted((keys[k], v) for k, v in r.items()))
                if key and key not in rows:
                    rows[key] = (pos, con) if rowfun is None else (pos, con, k_rec)
    return keys, rows


def to_matrix(keys, rows):
    rk = list(rows)
    ri, ci, dd = [], [], []
    for i, key in enumerate(rk):
        for v, c in key:
            ri.append(i)
            ci.append(v)
            dd.append(c)
    return sps.csr_matrix((dd, (ri, ci)), shape=(len(rk), len(keys))), rk


def exact_vertex(A, rk, keys, lb):
    nv = len(keys)
    res = linprog(np.ones(nv), A_eq=A, b_eq=np.zeros(A.shape[0]), bounds=[(l, None) for l in lb], method="highs")
    assert res.status == 0, res.message
    x = res.x
    fixed = {i for i in range(nv) if abs(x[i] - lb[i]) < 1e-9}
    free = [i for i in range(nv) if i not in fixed]
    fpos = {v: j for j, v in enumerate(free)}
    M = []
    for key in rk:
        row = [sp.QQ(0)] * (len(free) + 1)
        const = Fr(0)
        for v, c in key:
            c = Fr(c)
            if v in fpos:
                row[fpos[v]] += sp.QQ(c.numerator, c.denominator)
            else:
                const += c * lb[v]
        row[-1] = sp.QQ((-const).numerator, (-const).denominator)
        M.append(row)
    R, piv = DomainMatrix(M, (len(M), len(free) + 1), sp.QQ).rref()
    Rm = R.to_Matrix()
    sol = {}
    for rr, p in enumerate(piv):
        assert p < len(free), "inconsistent"
        sol[free[p]] = Fr(int(Rm[rr, len(free)].p), int(Rm[rr, len(free)].q))
    rates = [Fr(lb[i]) if i in fixed else sol.get(i) for i in range(nv)]
    assert all(r is not None for r in rates), "degenerate vertex"
    return rates


def sparse_certificate(M, b):
    """y with M^T y >= 0 and b.y = -1 (so b.y < 0), minimising |y|_1; M rows x vars"""
    m = M.shape[0]
    Mt = M.T.tocsr()
    A_ub = sps.hstack([-Mt, Mt]).tocsr()                     # -(M^T)(y+ - y-) <= 0
    A_eq = sps.csr_matrix(np.concatenate([b, -b])[None, :])  # b.(y+ - y-) = -1
    res = linprog(np.ones(2 * m), A_ub=A_ub, b_ub=np.zeros(Mt.shape[0]), A_eq=A_eq, b_eq=[-1.0],
                  bounds=[(0, None)] * (2 * m), method="highs")
    assert res.status == 0, res.message
    y = res.x[:m] - res.x[m:]
    return [Fr(v).limit_denominator(10 ** 6) for v in y]


def fmt(f):
    return f"{f.numerator}/{f.denominator}"


if __name__ == "__main__":
    t0 = time.time()
    T3, T4 = Torus(3), Torus(4)
    # ---------------- three-record rules on the 3^3 and 4^3 tori
    for L, T in ((3, T3), (4, T4)):
        for name in WF:
            keys, rows = distinct_rows(T, (3,), 'base', name)
            A, rk = to_matrix(keys, rows)
            inv = {v: k for k, v in keys.items()}
            lb = [1 if is_move(inv[i]) else 0 for i in range(len(keys))]
            rates = exact_vertex(A, rk, keys, lb)
            OUT[f"rule_L{L}_{name}"] = {kstr(inv[i]): fmt(rates[i]) for i in range(len(keys))}
            print(f"rule L={L} {name}: {len(keys)} classes, {len(rk)} distinct equations ({time.time() - t0:.0f} s)", flush=True)
    # ---------------- restricted families on 3^3: moves at the local clock / at 1, exchanges free
    for fam in ("localclock", "unitmoves"):
        for name in WF:
            keys, rows = distinct_rows(T3, (3,), 'base', name)
            inv = {v: k for k, v in keys.items()}
            w = WF[name]

            def mv_rate(k):
                if fam == "unitmoves":
                    return 1.0
                own = 1.0
                for pos_ in (1, 2, 3, 4, 5, 6):     # L = 3 keys: 0 x, 1 target, 2 behind, 3..6 transverse neighbours of x
                    c = k[pos_]
                    if c >= 0:
                        own *= w[0] if c == 0 else (w[1] if c == 1 else w[2])
                return 1.0 / own
            ex = [i for i in range(len(keys)) if not is_move(inv[i])]
            col = {v: j for j, v in enumerate(ex)}
            reps, Mrows, bvec = [], [], []
            seen = {}
            for key, rep in rows.items():
                coef, bb = {}, 0.0
                for v, c in key:
                    if is_move(inv[v]):
                        bb -= c * mv_rate(inv[v])
                    else:
                        coef[col[v]] = coef.get(col[v], 0.0) + c
                kk = (tuple(sorted(coef.items())), bb)
                if kk in seen or (not coef and bb == 0):
                    continue
                seen[kk] = 1
                reps.append(rep)
                Mrows.append(coef)
                bvec.append(bb)
            M = sps.lil_matrix((len(Mrows), len(ex)))
            for i, cf in enumerate(Mrows):
                for j, c in cf.items():
                    M[i, j] = c
            y = sparse_certificate(M.tocsr(), np.array(bvec))
            OUT[f"cert_{fam}_{name}"] = {f"{r[0]}|{r[1]}": fmt(v) for r, v in zip(reps, y) if v != 0}
            print(f"certificate {fam} {name}: support {len(OUT[f'cert_{fam}_{name}'])} ({time.time() - t0:.0f} s)", flush=True)
    # ---------------- record-wise balance on 3^3
    def recordwise(T, pos, occ, w):
        pi = T.weight(occ, w, 1.0)
        out = []
        for x in pos:
            s = occ[x]
            behind = T.NB[x][s ^ 1]
            occ2 = list(occ)
            if occ[behind] >= 0:
                occ2[behind], occ2[x] = occ[x], occ[behind]
            else:
                occ2[behind] = s
                occ2[x] = -1
            r = {}
            k1, k2 = T.env(occ, x), T.env(occ2, behind)
            r[k1] = r.get(k1, 0.0) + pi
            r[k2] = r.get(k2, 0.0) - T.weight(occ2, w, 1.0)
            out.append({k: v for k, v in r.items() if v != 0})
        return out
    for name in WF:
        keys, rows = distinct_rows(T3, (3,), 'base', name, rowfun=recordwise)
        A, rk = to_matrix(keys, rows)
        inv = {v: k for k, v in keys.items()}
        lb = np.array([1.0 if is_move(inv[i]) else 0.0 for i in range(len(keys))])
        y = sparse_certificate(A, -(A @ lb))                  # A s = -A l, s >= 0 infeasible: A^T y >= 0, (-A l).y < 0
        reps = [rows[k] for k in rk]
        OUT[f"cert_recordwise_{name}"] = {f"{r[0]}|{r[1]}|{r[2]}": fmt(v) for r, v in zip(reps, y) if v != 0}
        print(f"certificate recordwise {name}: support {len(OUT[f'cert_recordwise_{name}'])} ({time.time() - t0:.0f} s)", flush=True)
    # ---------------- joint three- and four-record sectors on 3^3, base and enlarged (head-on re-draw) families
    for mode in ("base", "rot"):
        for name in WF:
            keys, rows = distinct_rows(T3, (3, 4), mode, name)
            A, rk = to_matrix(keys, rows)
            inv = {v: k for k, v in keys.items()}
            lb = np.array([1.0 if is_move(inv[i]) else 0.0 for i in range(len(keys))])
            y = sparse_certificate(A, -(A @ lb))
            reps = [rows[k] for k in rk]
            OUT[f"cert_joint_{mode}_{name}"] = {f"{r[0]}|{r[1]}": fmt(v) for r, v in zip(reps, y) if v != 0}
            print(f"certificate joint {mode} {name}: {len(keys)} classes, {len(rk)} distinct equations, support "
                  f"{len(OUT[f'cert_joint_{mode}_{name}'])} ({time.time() - t0:.0f} s)", flush=True)
    if "L5" in sys.argv:
        T5 = Torus(5)
        for name in WF:
            keys, rows = distinct_rows(T5, (3,), 'base', name)
            A, rk = to_matrix(keys, rows)
            inv = {v: k for k, v in keys.items()}
            lb = [1 if is_move(inv[i]) else 0 for i in range(len(keys))]
            rates = exact_vertex(A, rk, keys, lb)
            OUT[f"rule_L5_{name}"] = {kstr(inv[i]): fmt(rates[i]) for i in range(len(keys))}
            print(f"rule L=5 {name}: {len(keys)} classes, {len(rk)} distinct equations ({time.time() - t0:.0f} s)", flush=True)
    json.dump(OUT, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json"), "w"), indent=0)
    print("wrote data.json", {k: len(v) for k, v in OUT.items()})
