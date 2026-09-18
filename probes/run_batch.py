#!/usr/bin/env python3
"""Batch mode for tier-0 volume: run one shard of the catalog's mechanical tasks through run_probe.py, one log per task.

    python3 probes/run_batch.py --type R --shard 3/40 --worker <name> --review "<sentence>" [--skip-done 7] [--minutes 30]

Shard k/n runs the tasks whose index (in probes/TASKS.json order, filtered by --type) is congruent to k-1 modulo n.
--skip-done D skips tasks that already have a log by ANY worker with CHECK PASS and no hit younger than D days.
The review sentence is stored on every log of the shard with the automatic suffix "[batch k/n]"; write it about the shard
(machine, python version, what was compared).  Each run's self-check (check_log.py) decides PASS/FAIL as usual.
Prints one tally line at the end: BATCH: ran=<n> pass=<n> fail=<n> hits=<n> skipped=<n>.  Commit logs/probes afterwards."""
import argparse, glob, json, os, subprocess, sys, time
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ap = argparse.ArgumentParser()
ap.add_argument("--type", default="R", help="task id prefix: R, M, L, F, X, S")
ap.add_argument("--shard", default="1/1")
ap.add_argument("--worker", required=True); ap.add_argument("--model", default="")
ap.add_argument("--review", required=True); ap.add_argument("--skip-done", type=float, default=0.0)
ap.add_argument("--minutes", type=float, default=0.0, help="per-task budget passed to run_probe (0 = task default)")
ap.add_argument("--seed", type=int, default=0, help="seed for seeded tasks (F/S/X); 0 = task default")
ap.add_argument("--dry", action="store_true")
a = ap.parse_args()
k, n = (int(x) for x in a.shard.split("/")); assert 1 <= k <= n
tasks = [t for t in json.load(open(os.path.join(ROOT, "probes", "TASKS.json"))) if t["id"].startswith(a.type + ":") and not t.get("direct")]
mine = [t for i, t in enumerate(tasks) if i % n == k - 1]
def recently_done(tid):
    if a.skip_done <= 0: return False
    cutoff = time.time() - a.skip_done * 86400
    for f in glob.glob(os.path.join(ROOT, "logs", "probes", tid, "*.json")):
        if os.path.getmtime(f) < cutoff: continue
        try: L = json.load(open(f))
        except Exception: continue
        if L.get("checked", {}).get("result") == "PASS" and not L.get("hit"): return True
    return False
ran = passed = failed = hits = skipped = 0
for t in mine:
    if recently_done(t["id"]): skipped += 1; continue
    cmd = [sys.executable, os.path.join(ROOT, "probes", "run_probe.py"), t["id"], "--worker", a.worker, "--review", f"{a.review} [batch {k}/{n}]"]
    if a.model: cmd += ["--model", a.model]
    if a.minutes: cmd += ["--minutes", str(a.minutes)]
    if a.seed: cmd += ["--seed", str(a.seed)]
    if a.dry: print(" ".join(cmd)); continue
    r = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True); ran += 1
    out = r.stdout
    ok = "CHECK PASS" in out and r.returncode == 0
    hit = '"hit": true' in out
    passed += ok; failed += (not ok); hits += hit
    line = out.strip().splitlines()[-1] if out.strip() else "(no output)"
    print(f"{t['id']}: {'PASS' if ok else 'FAIL'}{' HIT' if hit else ''}  {line[:100]}", flush=True)
print(f"BATCH: ran={ran} pass={passed} fail={failed} hits={hits} skipped={skipped} shard={k}/{n} type={a.type} tasks={len(mine)}")
