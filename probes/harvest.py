#!/usr/bin/env python3
"""Summarize logs/probes: per task, runs, hits, failures, workers, and the parsed summaries' extremes."""
import json, os, glob, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows = collections.defaultdict(list)
for f in glob.glob(os.path.join(ROOT, "logs", "probes", "*", "*.json")):
    try: rows[json.load(open(f))["task"]].append(json.load(open(f)))
    except Exception: pass
print(f"{'task':70s} runs hits rc!=0 workers")
for task in sorted(rows):
    L = rows[task]; hits = sum(1 for r in L if r.get("hit")); bad = sum(1 for r in L if r.get("returncode"))
    print(f"{task[:70]:70s} {len(L):4d} {hits:4d} {bad:5d} {','.join(sorted(set(r['worker'] for r in L)))[:30]}")
    for r in L:
        if r.get("hit"): print("   HIT:", r["worker"], r["started_utc"], json.dumps(r.get("summary"))[:200])
