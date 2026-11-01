#!/usr/bin/env python3
"""R1 of CRITERIA.md: the frozen-action copy of paid-inputs-frozen-energy.md on the comb block map."""
import math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "gate_ex"))
from ex_core import Block, guard, ident, plaquettes, qexp, qlog, wilson
import torch

def put(U, x, mu, angle):
    n = U.shape[0]
    idx = tuple(int(v) % n for v in x)
    U[idx + (mu,)] = qexp(torch.tensor([0.0, 0.0, angle]))

def field(n, centres, a, offsets=(1, -1), signs=(1, -1)):
    U = ident((n,) * 4 + (4,))
    for z in centres:
        for o, s in zip(offsets, signs):
            put(U, (z[0], z[1] + o, z[2], z[3]), 0, s * a)
    return U

def parent_max(U, L, order):
    n = U.shape[0]
    V = Block(n, L, 4, order=order)(U)
    return float(qlog(V).norm(dim=-1).max())

ORDERS = [[0, 1, 2, 3], [3, 2, 1, 0], [1, 0, 3, 2], [1, 2, 3, 0]]
ok = True
for L in (5, 7):
    n = 2 * L
    for a in (0.01, 0.1, 0.19):
        U = field(n, [(0, 0, 0, 0)], a)
        worst = max(parent_max(U, L, o) for o in ORDERS)
        angs = torch.cat([qlog(p).norm(dim=-1).reshape(-1) for _, p in plaquettes(U)])
        cnt = int(((angs - a).abs() < 1e-12).sum())
        rest = float(angs[(angs - a).abs() >= 1e-12].max())
        act = float(wilson(U)) / 2
        a_ok = worst < 1e-12 and cnt == 12 and rest < 1e-12 and abs(act - 12 * (1 - math.cos(a))) < 1e-12
        ok &= a_ok
        print(f"R1a,b L {L} a {a}: parent {worst:.2e} count {cnt} rest {rest:.1e} action {act:.10f} exact {12*(1-math.cos(a)):.10f} {'PASS' if a_ok else 'FAIL'}", flush=True)
        guard()
    a = 0.1
    for name, cs in (("adjacent dir 2", [(0, 0, 0, 0), (0, L, 0, 0)]), ("adjacent dir 1", [(0, 0, 0, 0), (L, 0, 0, 0)])):
        worst = max(parent_max(field(n, cs, a), L, o) for o in ORDERS)
        c_ok = worst < 1e-12
        ok &= c_ok
        print(f"R1c L {L} {name}: parent {worst:.2e} {'PASS' if c_ok else 'FAIL'}", flush=True)
    one = max(parent_max(field(n, [(0, 0, 0, 0)], a, offsets=(1,), signs=(1,)), L, o) for o in ORDERS)
    same = max(parent_max(field(n, [(0, 0, 0, 0)], a, signs=(1, 1)), L, o) for o in ORDERS)
    off = max(parent_max(field(n, [(0, 0, 0, 0)], a, offsets=(1, -2)), L, o) for o in ORDERS)
    c_ok = one > a / 20 and same > a / 20 and off > 1e-3
    ok &= c_ok
    print(f"R1d L {L} controls: one link {one:.4e}, equal signs {same:.4e}, off centre {off:.4e} {'PASS' if c_ok else 'FAIL'}", flush=True)
print("R1", "PASS" if ok else "FAIL")
