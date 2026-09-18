#!/usr/bin/env python3
"""Generate probes/TASKS.json: every runner in scripts/ with a pinned cache becomes a re-execution task (type R), every runner with
--list-mutations becomes a mutation-census task (type M), every *refuter*.py control in a science pack becomes a re-run task (type F);
the hand-written tasks in probes/tasks/*.json (searches, scans, falsifier work) are appended.  Run from the repository root."""
import json, os, re, glob, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tasks = []
cache = set(os.path.splitext(f)[0] for f in os.listdir(os.path.join(ROOT, "logs", "runner-cache")) if f.endswith(".txt")) if os.path.isdir(os.path.join(ROOT, "logs", "runner-cache")) else set()
runners = sorted(glob.glob(os.path.join(ROOT, "scripts", "*_20[0-9][0-9]_[0-9][0-9]_[0-9][0-9].py")))
for r in runners:
    name = os.path.splitext(os.path.basename(r))[0]
    src = open(r, encoding="utf-8", errors="ignore").read()
    total = re.search(r"Expected final line: `TOTAL: PASS=(\d+) FAIL=0`", src) or re.search(r"TOTAL: PASS=(\d+) FAIL=0", src)
    fam = name.split("_")[0]
    tasks.append({"id": f"R:{name}", "type": "runner-reexecution", "lane": fam, "tier": 0,
                  "command": f"python3 scripts/{name}.py", "cwd": ".", "timeout_s": 1200,
                  "expect_pattern": r"TOTAL: PASS=\d+ FAIL=0", "parse": {"total": r"TOTAL: PASS=\d+ FAIL=\d+"},
                  "hit_pattern": r"TOTAL: PASS=\d+ FAIL=[1-9]", "cached": name in cache,
                  "what": "re-execute the runner; a hit is any FAIL (compare with logs/runner-cache/<name>.txt)"})
    if "--list-mutations" in src:
        tasks.append({"id": f"M:{name}", "type": "mutation-census", "lane": fam, "tier": 0,
                      "command": f"for m in $(python3 scripts/{name}.py --list-mutations | awk '{{print $1}}'); do echo \"== $m\"; python3 scripts/{name}.py --mutation $m | grep 'mutation_family\\|TOTAL'; done",
                      "cwd": ".", "timeout_s": 3600, "parse": {"expected": r"mutation_family_expected: (\S+)", "observed": r"mutation_family_observed: (\S+)"},
                      "hit_pattern": r"mutation_family_observed: -", "what": "run every declared mutation; a hit is a mutation that fails no family or fails outside its family (compare expected/observed)"})
for spec in sorted(glob.glob(os.path.join(ROOT, ".claude", "science", "**", "specs", "*refuter*.py"), recursive=True)):
    rel = os.path.relpath(spec, ROOT); name = os.path.splitext(os.path.basename(spec))[0]
    tasks.append({"id": f"F:{name}", "type": "refuter-rerun", "lane": rel.split("/")[3] if rel.count("/") >= 3 else "pack", "tier": 1,
                  "command": f"cd scripts && python3 ../{rel} . {{EXTRA}}", "cwd": ".", "timeout_s": 3600,
                  "hit_pattern": r"INCONSISTENC|refuted|FAIL", "parse": {"verdict": r"== verdict: (.*)"},
                  "what": "re-run the refuting control (its own seeds; pass --extra for other arguments); a hit is an inconsistency it reports"})
for f in sorted(glob.glob(os.path.join(ROOT, "probes", "tasks", "*.json"))):
    tasks.extend(json.load(open(f)))
json.dump(tasks, open(os.path.join(ROOT, "probes", "TASKS.json"), "w"), indent=1)
by = {}
for t in tasks: by[t["type"]] = by.get(t["type"], 0) + 1
print("tasks:", len(tasks), by)
