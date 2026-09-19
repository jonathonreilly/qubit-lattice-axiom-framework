#!/usr/bin/env python3
"""lro-finite-size-analysis, independent run 1 of 2 (worker w-jonathonsmac4f50-j796b, claude-opus-5).

Reads the grids of X:formation-3plus1-finite-size and X:formation-3plus1-long from probes/TASKS.json and the logs under
logs/probes/<task>/*.txt; matches each log to a grid point by its header line; if fewer than half of the points are logged,
lists the missing ones and stops (the task's rule).  Supplementary (not used for any fit): the other X:formation-3plus1-*
logs at beta = 2, 3 with four predecessors, with their plateau |m| and the last three memory-table rows."""
import glob
import json
import os
import re
import sys

HERE = os.getcwd()
HEAD = re.compile(r"dim=(\d+) \(event lattice Z\^\d\) menu=(\S+) beta=([\d.]+) L=(\d+) T=(\d+) T0=(\d+) seed=(\d+); predecessors n=(\d+)")


def parse(path):
    txt = open(path).read()
    h = HEAD.search(txt)
    if not h:
        return None
    dim, menu, beta, L, T, T0, seed, n = h.groups()
    plat = re.search(r"plateau_\|m\|=([\d.]+)", txt)
    rows = re.findall(r"^\s+(\d+)\s+([\d.]+)\s+([+-][\d.]+)\s*$", txt, re.M)
    return dict(dim=int(dim), menu=menu, beta=float(beta), L=int(L), T=int(T), T0=int(T0), seed=int(seed), n=int(n),
                plateau=float(plat.group(1)) if plat else None, rows=[(int(a), float(b), float(c)) for a, b, c in rows], path=path)


def key_of_extra(extra):
    dimtok, menu, beta, L, T, T0, seed = extra.split()
    return (dimtok, menu, float(beta), int(L), int(T), int(T0), int(seed))


def key_of_log(d):
    dimtok = str(d["dim"]) + ("s" if d["n"] == 2 * d["dim"] + 1 else "")
    return (dimtok, d["menu"], d["beta"], d["L"], d["T"], d["T0"], d["seed"])


def main():
    tasks = json.load(open(os.path.join(HERE, "probes/TASKS.json")))
    tasks = tasks if isinstance(tasks, list) else tasks.get("tasks", tasks)
    byid = {t["id"]: t for t in tasks if isinstance(t, dict) and "id" in t}
    total_logged = total_points = 0
    missing_all = []
    for tid in ("X:formation-3plus1-finite-size", "X:formation-3plus1-long"):
        grid = [key_of_extra(g["extra"]) for g in byid[tid]["grid"]]
        logs = [d for d in (parse(p) for p in sorted(glob.glob(os.path.join(HERE, "logs/probes", tid, "*.txt")))) if d]
        have = {key_of_log(d): d for d in logs}
        logged = [k for k in grid if k in have]
        missing = [k for k in grid if k not in have]
        total_logged += len(logged)
        total_points += len(grid)
        missing_all += [(tid, k) for k in missing]
        print(f"{tid}: {len(logged)} of {len(grid)} grid points logged")
        for k in logged:
            d = have[k]
            last3 = ", ".join(f"level {a}: |m| {b:.4f}" for a, b, c in d["rows"][-3:])
            print(f"  logged: beta={k[2]:g} L={k[3]} T={k[4]} T0={k[5]} seed={k[6]}: plateau |m| = {d['plateau']}; last rows {last3}")
    print(f"logged {total_logged} of {total_points} points (half would be {total_points / 2:g})")
    enough = 2 * total_logged >= total_points
    if not enough:
        for tid, k in missing_all:
            print(f"  missing: {tid} extra='{k[0]} {k[1]} {k[2]:g} {k[3]} {k[4]} {k[5]} {k[6]}'")
    # supplementary inventory: other 3+1 scans at beta = 2, 3, four predecessors
    sup = []
    for p in sorted(glob.glob(os.path.join(HERE, "logs/probes/X:formation-3plus1-*/*.txt"))):
        tid = p.split("/logs/probes/")[1].split("/")[0]
        if tid in ("X:formation-3plus1-finite-size", "X:formation-3plus1-long"):
            continue
        d = parse(p)
        if d and d["menu"] == "sphere" and d["n"] == 4 and d["beta"] in (2.0, 3.0):
            sup.append((tid, d))
    for tid, d in sup:
        last3 = ", ".join(f"{b:.4f}" for a, b, c in d["rows"][-3:])
        print(f"supplementary (not fitted): {tid} beta={d['beta']:g} L={d['L']} T={d['T']} seed={d['seed']}: plateau |m| = {d['plateau']}, last three |m| {last3}")
    if not enough:
        print(f"SUMMARY: not computed: only {total_logged} of {total_points} grid points are logged (finite-size and long grids); "
              f"the {len(missing_all)} missing points are listed above; no fit of m_inf is attempted")
        return 0
    print("SUMMARY: enough points logged; the fit is not implemented in this run")
    return 0


if __name__ == "__main__":
    sys.exit(main())
