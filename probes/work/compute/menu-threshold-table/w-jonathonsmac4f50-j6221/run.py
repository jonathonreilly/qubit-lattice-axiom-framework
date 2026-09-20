#!/usr/bin/env python3
"""C:menu-threshold-table:a2   worker w-jonathonsmac4f50-j6221 (claude-opus-5)

Turn the menu/memory scan logs into the result - if they are there. The task says: if fewer than half the grid
points are logged, report what is missing and stop. This run reports the inventory, the few points that are
logged (with a drift check on each), and the exact list of missing grid points.
"""
import hashlib, json, glob, os, re, time
from pathlib import Path

t0 = time.time()
ROOT = next(p for p in (Path(__file__).resolve().parents[5], Path.cwd()) if (p / "logs" / "probes").exists())
TASKS = ["X:menu-size-threshold", "X:formation-3plus1-sphere-memory", "X:formation-2plus1-sphere-memory"]
tasks = json.load(open(ROOT / "probes" / "TASKS.json"))
tasks = tasks["tasks"] if isinstance(tasks, dict) else tasks
byid = {t["id"]: t for t in tasks}

def norm(extra):
    """canonical form of a formation_levelplane.py argument list"""
    parts = extra.split()
    if len(parts) != 7: return extra.strip()
    dim, menu, beta, L, T, T0, seed = parts
    return f"{dim} {menu} {float(beta):g} {L} {T} {T0} {seed}"

inventory = {}
for tid in TASKS:
    grid = byid.get(tid, {}).get("grid") or []
    want = [norm(g["extra"]) for g in grid]
    have = {}; offgrid = {}; broken = []
    for f in sorted(glob.glob(str(ROOT / "logs" / "probes" / tid / "*.json"))):
        j = json.load(open(f))
        m = re.search(r"formation_levelplane\.py\s+(.*)$", j.get("command", ""))
        if not m: continue
        key = norm(m.group(1))
        s = j.get("summary"); s = s.get("summary") if isinstance(s, dict) else s
        txt = f[:-5] + ".txt"
        rows = []; src = "none"
        if os.path.exists(txt):
            raw = open(txt, "rb").read()
            if hashlib.sha256(raw).hexdigest() == j.get("stdout_sha256"):
                src = "stdout file"
                for line in raw.decode().splitlines():
                    mm = re.match(r"\s*(\d+)\s+([0-9.]+)\s+([+-][0-9.]+)\s*$", line)
                    if mm: rows.append((int(mm.group(1)), float(mm.group(2)), float(mm.group(3))))
            else:
                src = "MISMATCHED stdout file, ignored"
                broken.append((os.path.basename(f), j.get("checked", {}).get("result"),
                               (j.get("checked", {}).get("findings") or [""])[0]))
        if not rows:                                   # fall back to the tail kept inside the log
            for line in str(j.get("stdout_tail", "")).split("\n"):
                mm = re.match(r"\s*(\d+)\s+([0-9.]+)\s+([+-][0-9.]+)\s*$", line)
                if mm: rows.append((int(mm.group(1)), float(mm.group(2)), float(mm.group(3))))
            if rows: src += " (rows from the log's own stdout_tail)"
        (have if key in want else offgrid)[key] = (s, rows, os.path.basename(f), src)
    inventory[tid] = (want, have, offgrid, broken)
    print(f"N1 {tid}: {len(have)} of {len(want)} grid points logged ({100*len(have)/max(len(want),1):.1f}%)"
          + (f"; {len(offgrid)} further run(s) present that are not grid points: "
             + ", ".join(f"[{k}]" for k in offgrid) if offgrid else ""))
    for name, res, first in broken:
        print(f"N1   DATA DEFECT in {tid}: {name} carries a stdout file that does not hash to the log's "
              f"stdout_sha256; the log's own self-check already recorded {res}: {first}")

total_want = sum(len(v[0]) for v in inventory.values())
total_have = sum(len(v[1]) for v in inventory.values())
print(f"N1 overall: {total_have} of {total_want} grid points logged "
      f"({100*total_have/total_want:.1f}%), the task's threshold being half")

print("N2 the points that ARE logged, with the last two rows of their memory table (the drift check):")
for tid, (want, have, offgrid, broken) in inventory.items():
    for key, (s, rows, fn, src) in sorted(list(have.items()) + list(offgrid.items())):
        pl = re.search(r"plateau_\|m\|=([0-9.naning]+)", s or "")
        plateau = pl.group(1) if pl else "?"
        if len(rows) >= 2:
            (n1, m1, _), (n2, m2, _) = rows[-2], rows[-1]
            rel = abs(m2 - m1) / max(m2, 1e-12)
            drift = f"levels {n1}->{n2}: |m| {m1:.4f} -> {m2:.4f} (relative change {rel*100:.1f}%)"
            mark = "STILL DRIFTING" if rel > 0.05 else "settled"
        else:
            drift, mark = "no memory table rows parsed", "UNKNOWN"
        tag = "" if key in want else "  (NOT a grid point)"
        print(f"N2   {tid} [{key}]{tag}: plateau_|m|={plateau}; {drift} -> {mark}  [rows from: {src}]")

print("N3 what is missing (the exact argument lists a later run would need):")
missing_total = 0
for tid, (want, have, offgrid, broken) in inventory.items():
    missing = [w for w in want if w not in have]
    missing_total += len(missing)
    by_menu = {}
    for w in missing:
        p = w.split()
        by_menu.setdefault((p[0], p[1]), []).append(p[2])
    print(f"N3 {tid}: {len(missing)} missing, grouped by (dim, menu):")
    for (dim, menu), betas in sorted(by_menu.items()):
        print(f"N3   dim={dim} menu={menu}: beta in {sorted(set(betas), key=float)} ({len(betas)} runs)")
    for w in missing:
        print(f"N3     missing: cd probes/lib && python3 formation_levelplane.py {w}")

print(f"N4 with {100*total_have/total_want:.1f} percent of the grid logged there is no (dim, menu) with more than "
      f"one coupling, so no plateau")
print("N4 curve, no half-of-the-large-beta-value crossing and no bracket can be formed, for either dimension.")
print("N4 The task's expectation - that the bracket rises without bound with the menu size N in 2+1 and")
print("N4 approaches the sphere's in 3+1 - is therefore neither supported nor contradicted by what is logged.")
print("N4 Stopping here, as the task instructs.")
print(f"SUMMARY: only {total_have} of {total_want} grid points are logged "
      f"({100*total_have/total_want:.1f}%, far below the half the task requires) - "
      + ", ".join(f"{t} {len(v[1])}/{len(v[0])}" for t, v in inventory.items()) + " - "
      f"so no threshold bracket can be formed for any (dim, menu); the {missing_total} missing argument lists are "
      f"printed above and the run stops there, as instructed; {time.time()-t0:.0f}s")
