import numpy as np
src = open("/tmp/scale-wt/scripts/frontier_record_conditional_law_period_scaling_2026_06_11.py").read()
head = src.split("# ===========================================================================\nprint")[0]
ns = {}; exec(head, ns)
build, scan, prefix, null_p95 = ns["build"], ns["scan"], ns["prefix"], ns["null_p95"]

# APPLES-TO-APPLES: apply the DRAFT's OWN selection rule (the 'most' = min-global row, n>=6)
# at L=3 for the SAME seed family used at L=4 {1,4242,99}, and also a broader family.
print("=== L=3 with the DRAFT'S OWN 'most-spread' selection rule (min-global row, depth>=6) ===")
print("seed  depth(most)  global  p2     p3     p4     null   gap     monotone")
env3 = build(3)
def most_row(env, seed, scan_depth, K):
    most, rows, sv = scan(env, seed, scan_depth, K)
    n, g1, Th, w = most
    p2,p3,p4 = prefix(Th,w,2),prefix(Th,w,3),prefix(Th,w,4)
    nl = null_p95(Th,w,3)
    return n,g1,p2,p3,p4,nl,p3-nl,(p2<p3<p4)
L3_same = []
for seed in (1,4242,99):
    n,g1,p2,p3,p4,nl,gap,mono = most_row(env3,seed,11,5)
    L3_same.append(gap)
    print("%4d  %5d        %.3f  %.3f  %.3f  %.3f  %.3f  %+.3f   %s"%(seed,n,g1,p2,p3,p4,nl,gap,mono))
print("L=3 (same 3 seeds, draft's rule) gaps:", [round(g,3) for g in L3_same], " median", round(float(np.median(L3_same)),3))
print()
# broader L=3 seed family, draft's rule
print("=== L=3 draft-rule, broader seed family ===")
L3_broad=[]
mono_fail=[]
for seed in (1,4242,99,7,11,123,2024,555,314,2718):
    n,g1,p2,p3,p4,nl,gap,mono = most_row(env3,seed,11,5)
    L3_broad.append(gap)
    if not mono: mono_fail.append((seed,n,round(p2,3),round(p3,3),round(p4,3)))
    print("%4d  d%-2d  global %.3f  p2/p3/p4 %.3f/%.3f/%.3f  null %.3f  gap %+.3f  mono=%s"%(seed,n,g1,p2,p3,p4,nl,gap,mono))
print("L=3 (10 seeds, draft's rule) gaps:", sorted(round(g,3) for g in L3_broad))
print("  median %.3f  min %.3f  max %.3f"%(float(np.median(L3_broad)),min(L3_broad),max(L3_broad)))
print("  MOST-SPREAD rows that STALL (not monotone p2<p3<p4):", mono_fail if mono_fail else "NONE -- all monotone")
