#!/usr/bin/env python3
"""Tube rerun of bond_carry.py on rows through the tube centre; see the amendment in CRITERIA.md."""
import importlib.util
import pathlib

import numpy as np

here = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("bc", here / "bond_carry.py")
bc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bc)
pc = bc.pc


def run(N, r, target, seed=11, rows=12, terms=400):
    U0 = pc.tuned_field("tube", N, target, seed)
    a = pc.a_of(U0)
    U = bc.gauge(U0, seed + 1)
    Vs = pc.chain(U)
    Ed = bc.level_data(Vs)
    rng = np.random.default_rng(seed + 2)
    z = tuple(int(c) for c in rng.integers(0, N, 4))
    J = pc.axis_frame(U, z)
    y0 = tuple((N // 2) // 3 ** r for _ in range(4))
    nc = Vs[r].shape[1]
    S = b1 = b2_max = 0.0
    b2_ok = True
    ctrl = []
    for i in range(rows):
        mu = i % 4
        y = list(y0)
        y[mu] = (y0[mu] - (i // 4) % 2) % nc  # both rows meeting the centre along mu
        base = None
        for _ in range(terms):
            T, x0, ratio, es, e_comp, e_drop, dl = bc.term(Vs, Ed, r, tuple(y), mu, rng)
            b1 = max(b1, ratio)
            b2_max = max(b2_max, e_comp)
            b2_ok = b2_ok and e_comp <= es + 1e-9
            if dl:
                ctrl.append((e_drop, e_comp))
            w = pc.qmul(T, pc.qconj(J[x0]))
            base = w if base is None else base
            S = max(S, bc.dist(w, base))
        pc.guard()
    drop = min(c[0] for c in ctrl)
    comp = max(c[1] for c in ctrl)
    row = dict(N=N, r=r, target=target, S=float(S), S_over_a=float(S / a), b1=float(b1), b2_ok=bool(b2_ok),
               b2_max=float(b2_max), n_carry=len(ctrl), drop_min=float(drop), comp_max=float(comp))
    print(row, flush=True)
    return row


rows = [run(N, r, t) for N, r in ((9, 1), (27, 1), (27, 2)) for t in (0.02, 0.01)]
get = lambda n, r, t: next(x for x in rows if (x["N"], x["r"], x["target"]) == (n, r, t))
fails = []
for x in rows:
    if x["b1"] > 1:
        fails.append(("B1", x))
    if not x["b2_ok"]:
        fails.append(("B2", x))
    if x["drop_min"] < 100 * x["comp_max"]:
        fails.append(("B5 void", x))
s1, s2, s3 = get(9, 1, 0.01)["S_over_a"], get(27, 2, 0.01)["S_over_a"], get(27, 2, 0.02)["S_over_a"]
if s2 > 2 * s1:
    fails.append(("B3", s1, s2))
if abs(s3 - s2) > 0.25 * s2:
    fails.append(("B4", s3, s2))
print("FAILS:", fails if fails else "none")
print("VERDICT:", "FAIL" if fails else "PASS")
