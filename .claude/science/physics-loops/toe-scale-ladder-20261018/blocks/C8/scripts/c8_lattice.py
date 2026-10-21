#!/usr/bin/env python3
"""C8 production runner: lattice Sakharov coefficients. Results are checkpointed to
logs/c8_results.json (one entry per configuration; reruns skip finished entries).
Usage: c8_lattice.py A   (b*, b_iso, massless, couplings M1-M4, lapse L1/L2)
       c8_lattice.py B   (massive b*, b_iso)
       c8_lattice.py C   (b_gold at theta > 0)
"""
from __future__ import annotations

import json
import os
import sys
import time
import functools

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import c8_core as cc

print = functools.partial(print, flush=True)
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs', 'c8_results.json')
res = json.load(open(OUT)) if os.path.exists(OUT) else {}
CHANS = [('z', 'A'), ('z', 'B'), ('f', 'A'), ('f', 'B'), ('d', 'A'), ('d', 'B'), ('g', 'A'), ('g', 'B')]
XPTS = [(np.pi, 0, 0), (0, np.pi, 0), (0, 0, np.pi)]


def run(walk, theta, chi, coupling, ch, N, kap=1.0, nr=96, nmu=32, nph=64, gold_balls=False):
    key = f"{walk}|th={theta}|chi={chi:.4f}|{coupling}|{ch[0]}{ch[1]}|N={N}|kap={kap}|in={nr},{nmu},{nph}|X={int(gold_balls)}"
    if key in res:
        return res[key]
    W = cc.Walk(walk, theta=theta, chi=chi)
    qh, eps = cc.tt_eps(*ch)
    t0 = time.time()
    centers = [np.zeros(3)] + ([np.array(x) for x in XPTS] if gold_balls else [])
    I0, I2, rerr = cc.bz_integral(W, coupling, eps, qh, N, kap=kap, nr=nr, nmu=nmu, nph=nph, centers=centers)
    c2 = -0.25*I2                      # q^2 coefficient of e2(q) = E2/(Vol lambda^2), lattice units
    cG = 2*c2/W.s                      # a^2/(16 pi G) per walk, c = 1 units (tau = s a)
    res[key] = dict(walk=walk, theta=theta, chi=chi, coupling=coupling, chan=ch[0] + ch[1], N=N, kap=kap,
                    inner=[nr, nmu, nph], X=gold_balls, I0=I0, I2=I2, c2=c2, cG=cG, s=W.s, rich=rerr,
                    sec=time.time() - t0)
    json.dump(res, open(OUT, 'w'), indent=0)
    print(f"{key}: cG = {cG:.12e}  e2(0) = {-I0:.10e}  ({time.time()-t0:.1f}s)")
    return res[key]


job = sys.argv[1] if len(sys.argv) > 1 else 'A'
if job == 'A':
    for walk in ('bstar', 'iso'):
        for ch in CHANS:
            for N in (96, 128):
                run(walk, 0.0, np.pi/2, 'M1', ch, N)
        for ch in (('z', 'A'), ('z', 'B'), ('d', 'A')):
            run(walk, 0.0, np.pi/2, 'M1', ch, 128, kap=1.4)
            run(walk, 0.0, np.pi/2, 'M1', ch, 96, nr=128, nmu=40, nph=80)
        for cp in ('M2', 'M3', 'M4'):
            for ch in CHANS[:6]:
                for N in (96, 128):
                    run(walk, 0.0, np.pi/2, cp, ch, N)
        for cp in ('L1', 'L2'):
            for ch in (('z', 'A'), ('d', 'A')):
                run(walk, 0.0, np.pi/2, cp, ch, 96)
elif job == 'B':
    for walk in ('bstar', 'iso'):
        for chi in (0.0, np.pi/2):
            for th in (0.2, 0.1, 0.05):
                for ch in (('z', 'A'), ('z', 'B'), ('d', 'A')):
                    run(walk, th, chi, 'M1', ch, 96)
elif job == 'C':
    for th in (0.4, 0.2, 0.1, 0.05):
        for ch in CHANS[:6]:
            for N in (96, 128):
                run('gold', th, np.pi/2, 'M1', ch, N, gold_balls=True)
    for th in (0.1, 0.05):
        for ch in (('z', 'A'), ('z', 'B'), ('d', 'A')):
            run('gold', th, np.pi/2, 'M1', ch, 128, kap=1.4, gold_balls=True)
            run('gold', th, np.pi/2, 'M1', ch, 96, nr=128, nmu=40, nph=80, gold_balls=True)
elif job == 'D':                                    # review fix: theta -> 0 at b_gold
    for th in (0.0125, 0.0):
        for ch in CHANS[:6]:
            for N in (96, 128):
                run('gold', th, np.pi/2, 'M1', ch, N, gold_balls=True)
print('done', job)
