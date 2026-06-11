#!/usr/bin/env python3
"""LENS 2 baseline-fairness check (L=3 ONLY -- memory-contract safe; 9 modes, 512-dim).

Reuses the DRAFT RUNNER's OWN functions (build, scan, prefix, null_p95) by exec'ing only
its function definitions (everything before the 'Part 1' driver is stripped, so NO L=4
build is triggered on import). We then evaluate L=3 for BOTH #3554 null-cleared seeds.

Decisive questions:
  (a) Does seed 99 / depth 7 / L=3 reproduce gap ~ +0.187 (record 0.502 vs null 0.315)?
  (b) Did the seed-99 fixed-k profile STALL, or was it monotone (0.347 -> 0.502)?
  (c) Set comparison: L=3 baseline = {seed 4242/d9 gap, seed 99/d7 gap}.
      Does the L=4 gap set {+0.193, +0.217, +0.076} still "roughly double" the L=3 SET?
"""
import numpy as np

src_path = "/tmp/scale-wt/scripts/frontier_record_conditional_law_period_scaling_2026_06_11.py"
with open(src_path) as f:
    src = f.read()

# Strip the driver: keep only up to the first 'Part 1' banner line.
cut = src.index('print("=" * 78)\nprint("Part 1')
defs_only = src[:cut]
ns = {}
exec(compile(defs_only, src_path, "exec"), ns)

build, scan, prefix, null_p95 = ns["build"], ns["scan"], ns["prefix"], ns["null_p95"]

print("=" * 78)
print("L=3 baseline-fairness: BOTH #3554 null-cleared events, runner machinery")
print("=" * 78)
env3 = build(3)
print(f"L=3: NM={env3['NM']} DIM={env3['DIM']}  (memory-safe)")

# ---- Event A: seed 4242, the note's chosen load-bearing event (depth 9) ----
most_4242, rows_4242, sv_4242 = scan(env3, 4242, 11, 5)
g_4242, Th_4242, w_4242 = rows_4242[9]
p2a, p3a, p4a = (prefix(Th_4242, w_4242, 2), prefix(Th_4242, w_4242, 3),
                 prefix(Th_4242, w_4242, 4))
na = null_p95(Th_4242, w_4242, 3)
gap_a = p3a - na
print(f"\n[A] seed 4242 depth 9 (note's baseline):")
print(f"    global {g_4242:.3f} | profile {p2a:.3f}/{p3a:.3f}/{p4a:.3f} | "
      f"null p95 {na:.3f} | gap {gap_a:+.3f}")
print(f"    stall? |p2-p3|={abs(p2a-p3a):.3f}  (note claims STALL, threshold <0.02): "
      f"{'STALL' if abs(p2a-p3a) < 0.02 else 'MONOTONE/NON-STALL'}")
print(f"    p2<p3<p4 monotone? {p2a < p3a < p4a}")

# ---- Event B: seed 99, depth 7 -- #3554's OTHER null-cleared event ----
# scan's `most` row may differ; we want depth 7 explicitly from rows.
most_99, rows_99, sv_99 = scan(env3, 99, 11, 5)
print(f"\n[B] seed 99 -- ALL depths, to locate the depth-7 event and the `most` row:")
print(f"    `most` row chosen by runner = depth {most_99[0]} (global {most_99[1]:.3f})")
for depth in sorted(rows_99):
    g, Th, w = rows_99[depth]
    p2, p3, p4 = prefix(Th, w, 2), prefix(Th, w, 3), prefix(Th, w, 4)
    nl = null_p95(Th, w, 3)
    flag = "  <-- depth 7 (#3554 event)" if depth == 7 else ""
    flag += "  <-- runner `most`" if depth == most_99[0] else ""
    stall = "STALL" if abs(p2 - p3) < 0.02 else "mono?" if p2 < p3 < p4 else "non-mono"
    print(f"    d{depth}: global {g:.3f} | prof {p2:.3f}/{p3:.3f}/{p4:.3f} | "
          f"null {nl:.3f} | gap {p3-nl:+.3f} | {stall}{flag}")

# Pull the depth-7 event explicitly for the set comparison.
g7, Th7, w7 = rows_99[7]
p2b, p3b, p4b = prefix(Th7, w7, 2), prefix(Th7, w7, 3), prefix(Th7, w7, 4)
nb = null_p95(Th7, w7, 3)
gap_b = p3b - nb
print(f"\n[B] seed 99 depth 7 (the decisive event):")
print(f"    global {g7:.3f} | profile {p2b:.3f}/{p3b:.3f}/{p4b:.3f} | "
      f"null p95 {nb:.3f} | gap {gap_b:+.3f}")
print(f"    stall? |p2-p3|={abs(p2b-p3b):.3f}: "
      f"{'STALL' if abs(p2b-p3b) < 0.02 else 'NON-STALL (profile moves)'}")
print(f"    p2<p3<p4 monotone? {p2b < p3b < p4b}")

# ---- The decisive set comparison ----
l3_set = sorted([gap_a, gap_b])
l4_set = sorted([0.193, 0.217, 0.076])
print("\n" + "=" * 78)
print("DECISIVE SET COMPARISON")
print("=" * 78)
print(f"L=3 gap SET (both #3554 null-cleared events): {[f'{g:+.3f}' for g in l3_set]}")
print(f"L=4 gap SET (note F2):                        {[f'{g:+.3f}' for g in l4_set]}")
print(f"L=3 range: [{l3_set[0]:+.3f}, {l3_set[-1]:+.3f}]   "
      f"L=4 range: [{l4_set[0]:+.3f}, {l4_set[-1]:+.3f}]")
print(f"Ranges OVERLAP? {l3_set[0] <= l4_set[-1] and l4_set[0] <= l3_set[-1]}")
print(f"L=3 median {np.median(l3_set):+.3f}  vs  L=4 median {np.median(l4_set):+.3f}  "
      f"(ratio {np.median(l4_set)/np.median(l3_set):.2f}x)")
print(f"Is the WORST L=4 gap (+{l4_set[0]:.3f}) below the BEST L=3 gap "
      f"(+{l3_set[-1]:.3f})? {l4_set[0] < l3_set[-1]}")
