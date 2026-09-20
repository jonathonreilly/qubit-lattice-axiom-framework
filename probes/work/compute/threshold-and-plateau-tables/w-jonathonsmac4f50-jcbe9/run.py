#!/usr/bin/env python3
"""C:threshold-and-plateau-tables:a2   worker w-jonathonsmac4f50-jcbe9 (claude-opus-5)

Turn the 3+1 scan logs into tables - if they are there. The task asks for plateau curves, memory brackets, a
dichotomy table by dimension and the kernel normalisation against beta, and says: if fewer than half the points
are logged, list what is missing and stop. Fewer than half are logged, so this is that report.
"""
import hashlib, json, glob, os, re, time
from pathlib import Path

t0 = time.time()
ROOT = next(p for p in (Path(__file__).resolve().parents[5], Path.cwd()) if (p / "logs" / "probes").exists())
TASKS = ["X:formation-3plus1-threshold-fine", "X:lightcone-threshold-fine", "X:formation-3plus1-seeds",
         "X:formation-by-dimension", "X:lightcone-by-dimension"]
tasks = json.load(open(ROOT / "probes" / "TASKS.json"))
tasks = tasks["tasks"] if isinstance(tasks, dict) else tasks
byid = {t["id"]: t for t in tasks}

def norm(extra):
    parts = extra.split()
    if len(parts) != 7: return extra.strip()
    dim, menu, beta, L, T, T0, seed = parts
    return f"{dim} {menu} {float(beta):g} {L} {T} {T0} {seed}"

inv = {}
for tid in TASKS:
    grid = byid.get(tid, {}).get("grid") or []
    want = [norm(g["extra"]) for g in grid]
    have, offgrid, broken = {}, {}, []
    for f in sorted(glob.glob(str(ROOT / "logs" / "probes" / tid / "*.json"))):
        j = json.load(open(f))
        m = re.search(r"formation_levelplane\.py\s+(.*)$", j.get("command", ""))
        if not m: continue
        key = norm(m.group(1))
        s = j.get("summary"); s = s.get("summary") if isinstance(s, dict) else s
        txt = f[:-5] + ".txt"; rows = []; src = "none"
        if os.path.exists(txt):
            raw = open(txt, "rb").read()
            if hashlib.sha256(raw).hexdigest() == j.get("stdout_sha256"):
                src = "stdout file"
                for line in raw.decode().splitlines():
                    mm = re.match(r"\s*(\d+)\s+([0-9.]+)\s+([+-][0-9.]+)\s*$", line)
                    if mm: rows.append((int(mm.group(1)), float(mm.group(2))))
            else:
                src = "MISMATCHED stdout file, ignored"
                broken.append((os.path.basename(f), j.get("checked", {}).get("result")))
        if not rows:
            for line in str(j.get("stdout_tail", "")).split("\n"):
                mm = re.match(r"\s*(\d+)\s+([0-9.]+)\s+([+-][0-9.]+)\s*$", line)
                if mm: rows.append((int(mm.group(1)), float(mm.group(2))))
            if rows: src += " (rows from the log's stdout_tail)"
        (have if key in want else offgrid)[key] = (s, rows, os.path.basename(f), src)
    inv[tid] = (want, have, offgrid, broken)
    extra = (f"; {len(offgrid)} run(s) present that are not grid points: " + ", ".join(f"[{k}]" for k in offgrid)) if offgrid else ""
    print(f"N1 {tid}: {len(have)} of {len(want)} grid points logged "
          f"({100*len(have)/max(len(want),1):.1f}%){extra}")
    for name, res in broken:
        print(f"N1   DATA DEFECT: {name} carries a stdout file that does not hash to its stdout_sha256 "
              f"(its own self-check recorded {res})")
tw = sum(len(v[0]) for v in inv.values()); th = sum(len(v[1]) for v in inv.values())
print(f"N1 overall: {th} of {tw} grid points logged ({100*th/tw:.1f}%), the task's threshold being half")

print("N2 everything that IS logged, with the plateau, the kernel normalisation and a drift check over the last")
print("N2 three rows of the memory table (the task's own criterion):")
for tid, (want, have, offgrid, broken) in inv.items():
    for key, (s, rows, fn, src) in sorted(list(have.items()) + list(offgrid.items())):
        pl = re.search(r"plateau_\|m\|=([0-9.]+|nan)", s or ""); lk = re.search(r"lowk_ratio=([0-9.\-]+|nan)", s or "")
        if len(rows) >= 3:
            (n1, m1), (n2, m2), (n3, m3) = rows[-3], rows[-2], rows[-1]
            span = max(m1, m2, m3) - min(m1, m2, m3)
            rel = span / max(m3, 1e-12)
            drift = (f"last three rows {n1}:{m1:.4f} {n2}:{m2:.4f} {n3}:{m3:.4f}, spread {rel*100:.1f}% -> "
                     + ("STILL DRIFTING" if rel > 0.05 else "settled"))
        else:
            drift = "fewer than three memory-table rows available"
        tag = "" if key in want else "  (NOT a grid point)"
        print(f"N2   {tid} [{key}]{tag}: plateau={pl.group(1) if pl else '?'}, "
              f"lowk_ratio={lk.group(1) if lk else '?'}; {drift}  [{src}]")

print("N3 what is missing, per scan, with the exact argument lists:")
missing_total = 0
for tid, (want, have, offgrid, broken) in inv.items():
    missing = [w for w in want if w not in have]; missing_total += len(missing)
    groups = {}
    for w in missing:
        p = w.split(); groups.setdefault((p[0], p[1], p[3]), []).append(p[2])
    print(f"N3 {tid}: {len(missing)} missing")
    for (dim, menu, L), betas in sorted(groups.items()):
        print(f"N3   dim={dim} menu={menu} L={L}: beta in {sorted(set(betas), key=float)} ({len(betas)} runs)")
    for w in missing:
        print(f"N3     missing: cd probes/lib && python3 formation_levelplane.py {w}")

print("N4 consequences for the four tables the task asks for:")
print("N4   (1) plateau against beta: no lattice has more than one coupling logged, so there is no curve and no")
print("N4       seed scatter (the only two logged runs are a pair at the same beta with different neighbourhoods).")
print("N4   (2) the memory bracket needs a largest beta with plateau < 0.1 and a smallest with plateau > 0.5 that")
print("N4       is not drifting: no lattice has both, so no bracket can be given.")
print("N4   (3) the dichotomy by dimension: the only two logged runs are both at dimension 3, beta = 2, L = 48")
print("N4       (one backward, one light-cone); dimensions 1, 2 and 4 have no logged run in these five scans, so")
print("N4       every entry of the table would read 'undecided' - a table of undecideds, not a result.")
print("N4   (4) lowk_ratio against beta: two points, one per lattice, at the same beta; no curve.")
print("N4 Stopping here, as the task instructs.")
print(f"SUMMARY: only {th} of {tw} grid points are logged ({100*th/tw:.1f}%, far below the half the task requires) - "
      + ", ".join(f"{t.split(':')[1]} {len(v[1])}/{len(v[0])}" for t, v in inv.items()) +
      f" - so none of the four tables (plateau against beta, the memory bracket, the dimension dichotomy, "
      f"lowk_ratio against beta) can be formed; the {missing_total} missing argument lists are printed above and "
      f"the run stops there, as instructed; {time.time()-t0:.0f}s")
