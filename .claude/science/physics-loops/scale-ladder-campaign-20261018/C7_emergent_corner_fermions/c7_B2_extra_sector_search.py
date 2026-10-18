#!/usr/bin/env python3
"""C7 part B2: a wider period-2 search at Majorana half filling (complements B3).

Greedy single-edge-flip descent over all period-2 Z2 sectors (2^3 supercell, 288 edges, 4^3 K-grid),
started (a) from the runner-up uniform patterns and (b) from fresh random gauge fields, plus a short
zero-temperature-with-kicks schedule (random 12-edge kick, re-descend, keep if lower) from the best
state.  Question: does any start reach a period-2 sector below 1c+11?  A search, not a certificate.
"""
import os, sys, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from c7_common import Lattice, per_site, majorana_amp, uniform_targets, flux_summary

PASS = FAIL = 0
T0 = time.time()


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''), flush=True)


rng = np.random.default_rng(2026)
L2 = Lattice(2)
Z = np.zeros(L2.nE, np.uint8)
base = majorana_amp(L2, Z, 1, 1)
gauge = lambda P: L2.solve_u(base, uniform_targets(L2, *P, 'maj'), rng=rng)


def energy(u, t2, nk=4):
    return per_site(L2.spectrum(majorana_amp(L2, u, 1.0, t2), nk), 6)


def greedy(u, t2, max_sweeps=6):
    u = u.copy(); e = energy(u, t2); sweeps = 0; improved = True
    while improved and sweeps < max_sweeps:
        improved = False; sweeps += 1
        for k in rng.permutation(L2.nE):
            u[k] ^= 1
            e2 = energy(u, t2)
            if e2 < e - 1e-10:
                e = e2; improved = True
            else:
                u[k] ^= 1
    return u, e


all_ok = True
for t2 in (0.2, 1.0):
    ref = energy(gauge((1, 'c+', 1, 1)), t2)
    print(f"\nt2 = {t2}: 1c+11 E = {ref:.5f} (4^3 grid)", flush=True)
    starts = [('uniform 1s+11', gauge((1, 's+', 1, 1))), ('uniform 0c+11', gauge((0, 'c+', 1, 1))),
              ('uniform 1c+01', gauge((1, 'c+', 0, 1)))]
    starts += [(f'random {i}', rng.integers(0, 2, L2.nE).astype(np.uint8)) for i in range(2)]
    best = (np.inf, None)
    for name, u0 in starts:
        e0 = energy(u0, t2)
        ur, er = greedy(u0, t2)
        print(f"  {name:14s}: E {e0:.5f} -> {er:.5f}  ({'above' if er > ref + 1e-6 else 'NOT ABOVE'} 1c+11 by {er-ref:+.5f}); "
              f"fluxes {flux_summary(L2, majorana_amp(L2, ur, 1, t2))}; t = {time.time()-T0:.0f}s", flush=True)
        all_ok &= er > ref - 1e-6
        if er < best[0]:
            best = (er, ur)
    # kicks from the best non-1c+11 state
    e, u = best
    for it in range(3):
        uk = u.copy(); idx = rng.choice(L2.nE, 12, replace=False); uk[idx] ^= 1
        uk, ek = greedy(uk, t2, max_sweeps=3)
        if ek < e:
            e, u = ek, uk
        print(f"  kick {it}: {ek:.5f} (best {e:.5f}); t = {time.time()-T0:.0f}s", flush=True)
    all_ok &= e > ref - 1e-6
check("no start (3 uniform runners-up, 4 random, 6 kicks) reaches a period-2 sector below 1c+11 at t2 = 0.2, 1",
      all_ok)
print(f"\nelapsed {time.time()-T0:.1f}s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
