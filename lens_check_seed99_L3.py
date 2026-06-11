"""Recompute #3554's OTHER null-cleared L=3 event (seed 99) using the DRAFT RUNNER's
own functions. L=3 build is NM=9, DIM=512 -- trivial memory. No new dense machinery."""
import importlib.util, numpy as np
spec = importlib.util.spec_from_file_location(
    "runner", "/tmp/scale-wt/scripts/frontier_record_conditional_law_period_scaling_2026_06_11.py")
# We must avoid executing the module-level driver (which builds L=4). Read source,
# strip everything from the Part-1 print onward, exec the function defs only.
src = open("/tmp/scale-wt/scripts/frontier_record_conditional_law_period_scaling_2026_06_11.py").read()
cut = src.index('print("=" * 78)')
ns = {}
exec(src[:cut], ns)
build, scan, prefix, null_p95 = ns["build"], ns["scan"], ns["prefix"], ns["null_p95"]

env3 = ns["build"](3)
print("L=3 env built: NM=%d DIM=%d" % (env3["NM"], env3["DIM"]))

# Part-1 baseline event the runner uses: seed 4242, the runner reads rows3[9] (depth 9 fixed)
most_4242, rows_4242, sv_4242 = scan(env3, 4242, 11, 5)
g9, Th9, w9 = rows_4242[9]
print("\n--- seed 4242 (runner's Part-1 event, depth 9 FIXED) ---")
p2,p3,p4 = prefix(Th9,w9,2), prefix(Th9,w9,3), prefix(Th9,w9,4)
n3 = null_p95(Th9,w9,3)
print(f"  profile {p2:.4f}/{p3:.4f}/{p4:.4f}  null p95 {n3:.4f}  gap {p3-n3:+.4f}  |p2-p3|={abs(p2-p3):.4f}")

# Now: seed 4242's MOST-SPREAD row (the runner's selector for L=4, applied to L=3)
n_ms, g_ms, Th_ms, w_ms = most_4242
p2,p3,p4 = prefix(Th_ms,w_ms,2), prefix(Th_ms,w_ms,3), prefix(Th_ms,w_ms,4)
n_ms3 = null_p95(Th_ms,w_ms,3)
print(f"\n--- seed 4242 MOST-SPREAD row (runner's L=4 selector, applied to L=3): depth {n_ms} ---")
print(f"  global {g_ms:.4f}  profile {p2:.4f}/{p3:.4f}/{p4:.4f}  null p95 {n_ms3:.4f}  gap {p3-n_ms3:+.4f}  |p2-p3|={abs(p2-p3):.4f}")

# seed 99 at L=3 -- #3554's OTHER null-cleared event. Use the runner's OWN most-spread selector.
most_99, rows_99, sv_99 = scan(env3, 99, 11, 5)
n99, g99, Th99, w99 = most_99
p2,p3,p4 = prefix(Th99,w99,2), prefix(Th99,w99,3), prefix(Th99,w99,4)
n99_3 = null_p95(Th99,w99,3)
print(f"\n--- seed 99 MOST-SPREAD row (runner's selector) at L=3: depth {n99} ---")
print(f"  global {g99:.4f}  profile {p2:.4f}/{p3:.4f}/{p4:.4f}  null p95 {n99_3:.4f}  gap {p3-n99_3:+.4f}  |p2-p3|={abs(p2-p3):.4f}")
print(f"  monotone p2<p3<p4 ? {p2<p3<p4}")

# Summary: the L=3 baseline SET vs L=4 SET
print("\n=== BASELINE-FAIRNESS SUMMARY ===")
print(f"L=3 set (runner most-spread rule, two #3554 null-cleared seeds):")
print(f"   seed 4242 depth {n_ms}: gap {prefix(Th_ms,w_ms,3)-n_ms3:+.4f}")
print(f"   seed 99   depth {n99}: gap {prefix(Th99,w99,3)-n99_3:+.4f}")
