import numpy as np
src = open("/tmp/scale-wt/scripts/frontier_record_conditional_law_period_scaling_2026_06_11.py").read()
head = src.split("# ===========================================================================\nprint")[0]
ns = {}; exec(head, ns)
build, scan, prefix, null_p95 = ns["build"], ns["scan"], ns["prefix"], ns["null_p95"]
env3 = build(3)

# Enumerate ALL rows (depth n>=6, same window as draft's `most` selection n>=5 -> rows keyed n+1>=7;
# but draft's `most` only requires n>=5 i.e. row index>=6). We scan every row index 6..11.
print("L=3 ALL EVENTS (each row = one event; gap = prefix-3 minus its OWN permutation-null p95)")
print("seed  depth  global  p2     p3     p4     null   gap     cleared  monotone(p2<p3<p4)")
seeds = [1, 4242, 99, 7, 11, 123, 2024, 555]
allrows = []
for seed in seeds:
    most, rows, sv = scan(env3, seed, 11, 5)
    for n in sorted(rows):          # n is the row key (n+1 in scan), i.e. actual depth
        if n < 6:  # match draft 'most' window n>=5 (row key = n+1 >=6); use depth>=6
            continue
        g, Th, w = rows[n]
        p2, p3, p4 = prefix(Th,w,2), prefix(Th,w,3), prefix(Th,w,4)
        nl = null_p95(Th, w, 3)
        gap = p3 - nl
        cleared = p3 > nl
        mono = (p2 < p3 < p4)
        allrows.append((seed,n,g,p2,p3,p4,nl,gap,cleared,mono))
        print("%4d  %5d  %.3f  %.3f  %.3f  %.3f  %.3f  %+.3f   %s    %s"%(
            seed,n,g,p2,p3,p4,nl,gap, ("YES" if cleared else "no "),("YES" if mono else "no ")))

cleared_gaps = [r[7] for r in allrows if r[8]]
print()
print("L=3 cleared-event gaps:", sorted(round(x,3) for x in cleared_gaps))
print("L=3 cleared count: %d / %d rows;  gap min %.3f  median %.3f  max %.3f"%(
    len(cleared_gaps), len(allrows), min(cleared_gaps), float(np.median(cleared_gaps)), max(cleared_gaps)))
# how many L=3 cleared events are >= the draft's L=4 gaps (0.193,0.217,0.076)?
for thr in (0.076, 0.193, 0.217):
    print("  L=3 cleared events with gap >= %.3f : %d"%(thr, sum(g>=thr for g in cleared_gaps)))
# stall audit: among cleared L=3 events, how many STALL (p2~p3) vs monotone?
stalls = [r for r in allrows if r[8] and abs(r[3]-r[4])<0.02]
monos  = [r for r in allrows if r[8] and r[9]]
print("L=3 cleared events that STALL (|p2-p3|<0.02): %d ; that are MONOTONE p2<p3<p4: %d"%(len(stalls),len(monos)))
