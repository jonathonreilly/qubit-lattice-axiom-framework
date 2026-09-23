#!/usr/bin/env python3
"""What the probes have found.  Run in an up-to-date ai/probes checkout.

    python3 probes/harvest.py            totals, hits by triage verdict (untriaged first), stale runners
    python3 probes/harvest.py --by-pr    one line per open PR: re-execution, falsifier, attack, provenance, confirmations
A hit is evidence only after a reader's triage (`check_log.py <log> --reviewer <name> --review "..." --verdict science`) and,
for judgment and search hits, an independent confirmation (the J-confirm units)."""
import argparse, collections, glob, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ap = argparse.ArgumentParser(); ap.add_argument("--by-pr", action="store_true"); a = ap.parse_args()
logs = []
for f in glob.glob(os.path.join(ROOT, "logs", "probes", "*", "*.json")):
    try: L = json.load(open(f)); L["_path"] = os.path.relpath(f, ROOT); logs.append(L)
    except Exception: pass
by_task = collections.defaultdict(list)
for L in logs: by_task[L.get("task", "?")].append(L)
def verdict(L): return L.get("triage", {}).get("verdict", "")
def passed(L): return (L.get("checked", {}).get("result") == "PASS" if "checked" in L else L.get("returncode") == 0) and (not L.get("hit") or verdict(L) == "false-positive")
if a.by_pr:
    prs = sorted({m.group(1) for t in by_task for m in [re.search(r"(?:^P:|:PR)(\d+)$", t)] if m}, key=int)
    print(f"{'PR':>6}  {'re-exec':<10} {'falsifier':<10} {'attack':<10} {'provenance':<11} confirmations")
    def cell(tid):
        ls = by_task.get(tid, [])
        if not ls: return "-"
        real = [l for l in ls if l.get("hit") and verdict(l) != "false-positive"]
        return ("HIT" + ("*" if any(verdict(l) == "science" for l in real) else "?")) if real else ("ok" if any(passed(l) for l in ls) else "fail")
    for n in prs:
        conf = [t for t in by_task if t.startswith("J:confirm:") and t.endswith("PR" + n)]
        cs = ", ".join(("confirmed" if any(l.get("hit") for l in by_task[t]) else "not reproduced") + " (" + t.split(":")[2].split("-")[1] + ")" for t in conf)
        print(f"{n:>6}  {cell('P:' + n):<10} {cell('J:falsifier:PR' + n):<10} {cell('J:attack:PR' + n):<10} {cell('J:provenance:PR' + n):<11} {cs}")
    print("\nHIT? = a hit nobody has triaged; HIT* = triaged as science; ok = ran and passed; fail = ran, self-check or run failed; - = not run yet"); sys.exit(0)
kinds = collections.Counter(L.get("task", "?").split(":")[0] for L in logs)
print("runs by kind:", dict(kinds), " workers:", len({L.get("worker") for L in logs}))
hits = [L for L in logs if L.get("hit")]
for title, sel in (("HITS NOT TRIAGED (read these first)", lambda L: not verdict(L)), ("HITS triaged as SCIENCE", lambda L: verdict(L) == "science"),
                   ("hits triaged as false positives of a pattern (supervisor: fix the pattern)", lambda L: verdict(L) == "false-positive"), ("hits triaged as machine problems", lambda L: verdict(L) == "machine"), ("stale runners (input file gone; automatic triage)", lambda L: verdict(L) == "stale")):
    sel_hits = [L for L in hits if sel(L)]
    print(f"\n== {title}: {len(sel_hits)}")
    for L in sorted(sel_hits, key=lambda L: L.get("task", "")):
        print(f"  {L.get('task')}  [{L.get('worker')}, {L.get('model') or '?'}]  {L['_path']}\n      {(L.get('review') or '')[:300]}")
comp = sorted(((t, L) for t, ls in by_task.items() if t.startswith(("C:", "J:derive:")) for L in ls), key=lambda p: (p[0], str(p[1].get("utc") or p[1].get("_path") or "")))
print(f"\n== derivations and computations logged: {len(comp)}")
for t, L in comp: print(f"  {t}  [{L.get('worker')}, {L.get('model') or '?'}] {'HIT ' if L.get('hit') else ''}{str(L.get('summary', {}).get('summary', ''))[:260]}")
stale = []
for t, ls in by_task.items():
    if t.startswith("R:") and not any(passed(l) for l in ls):
        bad = [l for l in ls if l.get("returncode") not in (0, None) or l.get("checked", {}).get("result") == "FAIL"]
        if bad: stale.append((t, len({l.get("worker") for l in bad}), (bad[-1].get("stdout_tail") or "").strip().splitlines()[-1][:110] if (bad[-1].get("stdout_tail") or "").strip() else ""))
print(f"\n== runners that fail on current main (no passing log; candidates for repository hygiene): {len(stale)}")
for t, n, last in sorted(stale): print(f"  {t}  ({n} worker{'s' if n != 1 else ''})  {last}")
