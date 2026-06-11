"""Filling confound (lens 1's decisive check) + monotonicity-reversal robustness.
Build env4 ONCE (one dense U_step), reuse for all seeds/fillings. Memory-safe."""
import importlib.util, numpy as np
src = open("/tmp/scale-wt/scripts/frontier_record_conditional_law_period_scaling_2026_06_11.py").read()
cut = src.index('print("=" * 78)')
ns = {}
exec(src[:cut], ns)
build, scan, prefix, null_p95 = ns["build"], ns["scan"], ns["prefix"], ns["null_p95"]

env4 = build(4)
print("env4 built ONCE: NM=%d DIM=%d" % (env4["NM"], env4["DIM"]))

def report(tag, seed, K):
    most, rows, sv = scan(env4, seed, 9, K)
    n, g1, Th, w = most
    p2,p3,p4 = prefix(Th,w,2), prefix(Th,w,3), prefix(Th,w,4)
    nl = null_p95(Th,w,3)
    mono = p2 < p3 < p4
    print(f"  {tag}: K={K} depth {n} global {g1:.3f} | profile {p2:.3f}/{p3:.3f}/{p4:.3f} | null p95 {nl:.3f} | gap {p3-nl:+.3f} | clears_null={p3>nl} monotone={mono}")
    return p3>nl, mono, p3-nl

print("\n=== FILLING CONFOUND: note uses K=7 (7/12). Test K=6 (half-filling 6/12) ===")
print("--- note's K=7 (reproduce) ---")
report("seed 1 ", 1, 7)
report("seed 99", 99, 7)
print("--- K=6 half-filling ---")
report("seed 1 ", 1, 6)
report("seed 99", 99, 6)
report("seed 2026", 2026, 6)

print("\n=== MONOTONICITY-REVERSAL ROBUSTNESS: fresh seeds at K=7 (the load-bearing positive fact) ===")
res = []
for s in (1, 4242, 99, 2026, 314, 7, 555):
    cn, mono, gap = report(f"seed {s}", s, 7)
    res.append((s, cn, mono, gap))
print("\n  monotone count:", sum(1 for _,_,m,_ in res if m), "/", len(res))
print("  clears-null count:", sum(1 for _,c,_,_ in res if c), "/", len(res))
print("  gaps:", [f"{g:+.3f}" for _,_,_,g in res])
