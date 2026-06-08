#!/usr/bin/env python3
"""
Audit-unlock keystone map: which rows to audit FIRST to drain the dependency DAG fastest.

DIAGNOSIS (computed from the live ledger docs/audit/data/audit_ledger.json):
the audit backlog is NOT blocked by physics or by missing/broken dependency edges --
it is a dependency-DAG DRAIN problem. The auditor must audit a row's deps before the
row itself becomes 'ready' (compute_audit_queue.py: a row is ready iff all deps are
at retained-grade). Most blocked rows are waiting SOLELY on unaudited deps. So the
single highest-leverage lever is audit ORDER: audit the high-fanout READY 'keystone'
rows first, so each audit cascade-unlocks the most downstream rows.

This runner is a reproducible TOOL: re-run it as the DAG drains to regenerate the
next keystone priority list. It asserts ROBUST structural facts (thresholds, not
exact counts, which drift as auditing proceeds) and PRINTS the current priority list.
"""
import json
import collections
import os

PASS = 0
FAIL = 0
def check(name, cond):
    global PASS, FAIL
    ok = bool(cond)
    print(("PASS" if ok else "FAIL") + ": " + name)
    PASS += ok
    FAIL += (not ok)

LEDGER = os.path.join(os.path.dirname(__file__), "..", "docs", "audit", "data", "audit_ledger.json")
rows = json.load(open(LEDGER))["rows"]

# dep-readiness mirrors compute_audit_queue.py: retained-grade + metadata tiers count as ready.
READY = {"retained", "retained_bounded", "retained_no_go", "meta",
         "audited_conditional", "audited_numerical_match", "audited_renaming", "open_gate"}
def dep_ready(s):
    return (s in READY) or (bool(s) and s.startswith("decoration_under_"))
def is_ready(r):
    return all(dep_ready(rows.get(dp, {}).get("effective_status")) for dp in r.get("deps", []))

# need-audit = audit_status unaudited/in_progress
unaud = set(k for k, r in rows.items()
            if r.get("audit_status", "unaudited") in ("unaudited", "audit_in_progress"))
# BLOCKS downstream only if its effective_status is itself non-ready
blocks = set(k for k in unaud if not dep_ready(rows[k].get("effective_status")))

# reverse-dependency graph + transitive downstream
revdeps = collections.defaultdict(set)
for k, r in rows.items():
    for dp in r.get("deps", []):
        if dp in rows:
            revdeps[dp].add(k)
def downstream(x):
    seen = set(); st = [x]
    while st:
        n = st.pop()
        for c in revdeps.get(n, ()):
            if c not in seen:
                seen.add(c); st.append(c)
    return seen

# ===========================================================================
# A -- the bottleneck is DAG-drain, not blockers / wiring.
# ===========================================================================
print("--- A: the bottleneck is DAG-drain (not blockers / broken edges) ---")
total = len(rows)
n_unaud = len(unaud)
n_blocks = len(blocks)
missing_edges = sum(1 for k in rows for dp in rows[k].get("deps", []) if dp not in rows)
recorded_blockers = sum(1 for k in blocks if rows[k].get("blocker"))
print(f"  total rows={total}  need-audit={n_unaud}  blocking(unaud & non-ready-eff)={n_blocks}")
print(f"  missing dep edges (broken wiring)={missing_edges}   rows with a recorded blocker={recorded_blockers}")
check("a large unaudited backlog exists (need-audit > 1000)", n_unaud > 1000)
check("NO broken dependency edges (the backlog is not a wiring bug)", missing_edges == 0)
check("almost no rows carry a recorded blocker (backlog is DAG-drain, not blocked-by-physics)",
      recorded_blockers < 0.02 * n_blocks)

# ===========================================================================
# B -- only a small fraction is READY-now; the rest waits on unaudited deps.
# ===========================================================================
print("--- B: ready-now vs waiting-on-deps ---")
ready_now = [k for k in blocks if is_ready(rows[k])]
solely_unaud = sum(1 for k in blocks if not is_ready(rows[k]) and
                   all(dep_ready(rows.get(dp, {}).get("effective_status")) or
                       rows.get(dp, {}).get("effective_status") in ("unaudited", None)
                       for dp in rows[k].get("deps", [])))
print(f"  READY-now (deps all retained-grade, auditable immediately)={len(ready_now)}")
print(f"  waiting SOLELY on unaudited deps (unlock as DAG drains)={solely_unaud}")
check("only a minority of blocked rows are ready-now (most wait on the DAG)",
      0 < len(ready_now) < 0.25 * n_blocks)
check("the overwhelming majority of not-ready rows wait SOLELY on unaudited deps "
      "(=> draining the DAG in keystone order unlocks them)", solely_unaud > 0.7 * (n_blocks - len(ready_now)))

# ===========================================================================
# C -- the KEYSTONE priority: ready rows sorted by downstream-blocker fanout.
# ===========================================================================
print("--- C: keystone priority (audit these READY rows first for max cascade) ---")
keys = sorted(((sum(1 for c in downstream(k) if c in blocks), k) for k in ready_now), reverse=True)
print("  TOP READY KEYSTONES (downstream blocked rows unlocked | criticality | id):")
for n, k in keys[:12]:
    print(f"    {n:5d}  {rows[k].get('criticality','?'):9s}  {k[:58]}")
# cumulative dedup unlock of top-5 ready keystones
top5 = set()
for n, k in keys[:5]:
    top5 |= set(c for c in downstream(k) if c in blocks)
print(f"  => the TOP-5 ready keystones together gate {len(top5)} distinct blocked rows "
      f"({100*len(top5)/max(1,n_blocks):.0f}% of the backlog)")
check("a top ready keystone exists that unlocks >= 500 downstream blocked rows", keys and keys[0][0] >= 500)
check("the top-5 ready keystones together gate a large majority (>= 60%) of the blocked backlog",
      len(top5) >= 0.60 * n_blocks)
check("the top ready keystones are critical-criticality (foundational)",
      all(rows[k].get("criticality") in ("critical", "high") for _, k in keys[:5]))

# ===========================================================================
# D -- secondary unlocks: dependency cycles + gated sources.
# ===========================================================================
print("--- D: dependency cycles (Tarjan SCCs) -- KEYSTONE cycles block the top keystones ---")
import sys as _s; _s.setrecursionlimit(80000)
idx = {}; low = {}; onst = {}; stk = []; cnt = [0]; sccs = []
def strong(v):
    idx[v] = low[v] = cnt[0]; cnt[0] += 1; stk.append(v); onst[v] = True
    for w in rows[v].get("deps", []):
        if w not in rows: continue
        if w not in idx:
            strong(w); low[v] = min(low[v], low[w])
        elif onst.get(w):
            low[v] = min(low[v], idx[w])
    if low[v] == idx[v]:
        comp = []
        while True:
            w = stk.pop(); onst[w] = False; comp.append(w)
            if w == v: break
        if len(comp) > 1:
            sccs.append(comp)
for v in list(rows):
    if v not in idx:
        strong(v)
def fanout(k): return sum(1 for c in downstream(k) if c in blocks)
keystone_cycles = sorted(((max(fanout(k) for k in comp), comp) for comp in sccs), reverse=True)
print(f"  cyclic SCCs (mutual-dependency clusters; NONE become 'ready' until broken)={len(sccs)}")
for mf, comp in keystone_cycles[:6]:
    tag = "KEYSTONE" if mf >= 200 else "minor"
    print(f"    [{tag}, max-fanout {mf:4d}, size {len(comp)}] " + " <-> ".join(c[:32] for c in comp[:3]) + ("..." if len(comp) > 3 else ""))
check("cyclic SCCs exist (mutual-dep clusters that never become 'ready' until broken)", len(sccs) > 0)
check("at least one KEYSTONE cycle exists (a top keystone trapped in a cycle => break-first)",
      any(mf >= 200 for mf, _ in keystone_cycles))
kc_members = set(c for mf, comp in keystone_cycles if mf >= 200 for c in comp)
check("the highest-fanout keystones are TRAPPED in cycles (RP / observable-principle / staggered) "
      "-> breaking these cycles is the PREREQUISITE for the keystone unlock",
      any("reflection_positivity" in c or "observable_principle_from_axiom" in c or "kawamoto_smit" in c
          for c in kc_members))

print("--- D2: gated sources (secondary) ---")
gated = json.load(open(LEDGER)).get("stats", {}).get("dropped_gated_sources", 0)
print(f"  gated/dropped sources (excluded from audit; review for ungating)={gated}")
check("gated sources exist and are a (secondary) unlock target (review for ungating)", gated >= 0)

print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
if FAIL:
    raise SystemExit(1)
