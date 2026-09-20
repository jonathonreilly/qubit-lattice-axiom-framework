#!/usr/bin/env python3
"""source-potential-tables, independent run 1 of 2 (worker w-jonathonsmac4f50-jc2a8, claude-opus-5).

Reads the grid of X:source-potential from probes/TASKS.json and the logs under logs/probes/X:source-potential/*.txt, matches each
log to a grid point by its header, and applies the task's rule: if fewer than half the points are logged, list what is missing and
stop.  What is logged is tabulated anyway: the ratio measured/linear by r along e_1, r times the measured displacement against the
continuum value h/(4 pi beta), and the forward/backward diagonal asymmetry for the backward lattice."""
import glob
import json
import math
import os
import re
import sys

HERE = os.getcwd()
HEAD = re.compile(r"dim=(\S+) beta=([\d.]+) L=(\d+) T=(\d+) T0=(\d+) h=([\d.]+) seed=(\d+); n=(\d+)")
ROW = re.compile(r"^\s+(\d+)\s+([+-][\d.]+)\s+([+-][\d.]+)\s+([\d.]+)(?:\s+([+-][\d.]+))?\s*$", re.M)
DIAG = re.compile(r"^\s+(\d+)\s+([+-][\d.]+)\s+([+-][\d.]+)\s+([+-][\d.]+)\s+([+-][\d.]+)\s*$", re.M)


def parse(path):
    txt = open(path).read()
    h = HEAD.search(txt)
    if not h:
        return None
    dimtok, beta, L, T, T0, hh, seed, n = h.groups()
    blocks = txt.split("along the body diagonal")
    axis = [(int(a), float(b), float(c), float(d)) for a, b, c, d, _ in ROW.findall(blocks[0])]
    diag = [(int(a), float(b), float(c), float(d), float(e)) for a, b, c, d, e in DIAG.findall(blocks[1])] if len(blocks) > 1 else []
    return dict(key=(dimtok, float(beta), int(L), int(T), int(T0), float(hh), int(seed)), n=int(n), axis=axis, diag=diag, path=path)


def key_of_extra(extra):
    dimtok, beta, L, T, T0, hh, seed = extra.split()
    return (dimtok, float(beta), int(L), int(T), int(T0), float(hh), int(seed))


def main():
    tasks = json.load(open(os.path.join(HERE, "probes/TASKS.json")))
    tasks = tasks if isinstance(tasks, list) else tasks.get("tasks", tasks)
    grid = [key_of_extra(g["extra"]) for g in next(t for t in tasks if t.get("id") == "X:source-potential")["grid"]]
    logs = [d for d in (parse(p) for p in sorted(glob.glob(os.path.join(HERE, "logs/probes/X:source-potential/*.txt")))) if d]
    have = {d["key"]: d for d in logs}
    logged = [k for k in grid if k in have]
    missing = [k for k in grid if k not in have]
    extra = [d for d in logs if d["key"] not in set(grid)]
    print(f"X:source-potential: {len(logged)} of {len(grid)} grid points logged; {len(extra)} further logs outside the grid")
    for d in logged and [have[k] for k in logged] or []:
        k = d["key"]
        ratios = ", ".join(f"r={r}: {q:.3f}" for r, m, l, q in d["axis"])
        rm = ", ".join(f"r={r}: {r * m:+.6f}" for r, m, l, q in d["axis"])
        cont = float(k[5]) / (4 * math.pi * k[1])
        print(f"  logged: dim={k[0]} beta={k[1]:g} L={k[2]} T={k[3]} h={k[5]:g} seed={k[6]} (n={d['n']}): measured/linear {ratios}")
        print(f"          r * measured {rm}; the continuum value h/(4 pi beta) = {cont:.6f}")
        if d["diag"] and not k[0].endswith("s"):
            asym = ", ".join(f"r={r}: {(p - m):+.6f}" for r, p, m, lp, lm in d["diag"])
            print(f"          backward lattice, forward minus backward along the body diagonal: {asym}")
    for d in extra:
        k = d["key"]
        ratios = ", ".join(f"r={r}: {q:.3f}" for r, m, l, q in d["axis"][:4])
        print(f"  outside the grid: dim={k[0]} beta={k[1]:g} L={k[2]} T={k[3]} h={k[5]:g} seed={k[6]}: measured/linear {ratios}")
    enough = 2 * len(logged) >= len(grid)
    if not enough:
        for k in missing:
            print(f"  missing: X:source-potential extra='{k[0]} {k[1]:g} {k[2]} {k[3]} {k[4]} {k[5]:g} {k[6]}'")
        print(f"SUMMARY: not computed: only {len(logged)} of {len(grid)} grid points of X:source-potential are logged (the {len(extra)} other logs "
              f"are off-grid short runs); the {len(missing)} missing points are listed above; no ratio, plateau, linearity or asymmetry table is fitted")
        return 0
    print("SUMMARY: enough points logged; the tables are not implemented in this run")
    return 0


if __name__ == "__main__":
    sys.exit(main())
