#!/usr/bin/env python3
"""Compact-cluster joint LP on the 6^3 torus: three- and four-record configurations with a record at the origin and the
others in the box [0,2]^3. These rows involve no wrap-around (check.py re-derives them on the 9^3 torus), so they are rows
of the problem on Z^3; a Farkas certificate for this subset of rows rules out any local rule on Z^3.
Adds cert_Z3_{mode}_{name} to data.json (or reports feasibility)."""
import json
import os
import sys
import time
from itertools import combinations, product

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from clocklib import Torus, is_move  # noqa: E402
from make_data import WF, to_matrix, sparse_certificate, fmt  # noqa: E402
from scipy.optimize import linprog  # noqa: E402

t0 = time.time()
path = os.path.join(HERE, "data.json")
OUT = json.load(open(path))
T = Torus(6)
BOX = [T.IDX[(a, b, c)] for a in range(3) for b in range(3) for c in range(3) if (a, b, c) != (0, 0, 0)]


def compact_configs(nrec):
    for rest in combinations(sorted(BOX), nrec - 1):
        pos = (0,) + rest
        for con in product(range(6), repeat=nrec):
            occ = [-1] * T.N
            for p_, c_ in zip(pos, con):
                occ[p_] = c_
            yield pos, con, occ


for mode in sys.argv[1:] or ("base", "rot"):
    for name in WF:
        keys, rows = {}, {}
        for nrec in (3, 4):
            for pos, con, occ in compact_configs(nrec):
                r = T.row(pos, occ, WF[name], mode, 1.0)
                for k in r:
                    if k not in keys:
                        keys[k] = len(keys)
                key = tuple(sorted((keys[k], v) for k, v in r.items()))
                if key and key not in rows:
                    rows[key] = (pos, con)
        A, rk = to_matrix(keys, rows)
        inv = {v: k for k, v in keys.items()}
        lb = np.array([1.0 if is_move(inv[i]) else 0.0 for i in range(len(keys))])
        res = linprog(np.ones(len(keys)), A_eq=A, b_eq=np.zeros(A.shape[0]), bounds=[(l, None) for l in lb], method="highs")
        print(f"Z3 compact {mode} {name}: {len(keys)} classes, {len(rk)} distinct equations, LP status {res.status} "
              f"({time.time() - t0:.0f} s)", flush=True)
        if res.status == 2:
            y = sparse_certificate(A, -(A @ lb))
            reps = [rows[k] for k in rk]
            OUT[f"cert_Z3_{mode}_{name}"] = {f"{r[0]}|{r[1]}": fmt(v) for r, v in zip(reps, y) if v != 0}
            print(f"   certificate support {len(OUT[f'cert_Z3_{mode}_{name}'])}", flush=True)
json.dump(OUT, open(path, "w"), indent=0)
print("updated data.json")
