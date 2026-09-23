#!/usr/bin/env python3
"""Adds the three-record rule on the 5^3 torus (c = 1 and c0 = 1/2) to data.json (LP proposal; check.py verifies exactly)."""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from clocklib import Torus, is_move, kstr  # noqa: E402
from make_data import WF, distinct_rows, to_matrix, exact_vertex, fmt  # noqa: E402

t0 = time.time()
path = os.path.join(HERE, "data.json")
OUT = json.load(open(path))
T5 = Torus(5)
for name in WF:
    keys, rows = distinct_rows(T5, (3,), 'base', name)
    A, rk = to_matrix(keys, rows)
    inv = {v: k for k, v in keys.items()}
    lb = [1 if is_move(inv[i]) else 0 for i in range(len(keys))]
    rates = exact_vertex(A, rk, keys, lb)
    OUT[f"rule_L5_{name}"] = {kstr(inv[i]): fmt(rates[i]) for i in range(len(keys))}
    print(f"rule L=5 {name}: {len(keys)} classes, {len(rk)} distinct equations ({time.time() - t0:.0f} s)", flush=True)
json.dump(OUT, open(path, "w"), indent=0)
print("updated data.json")
