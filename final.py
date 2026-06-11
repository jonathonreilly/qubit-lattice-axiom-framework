import numpy as np
# L=3 most-spread gaps (draft's own rule), 10 seeds, from apples.py run:
L3 = {1:0.031,4242:0.088,99:0.190,7:0.331,11:0.097,123:0.110,2024:0.260,555:0.047,314:0.251,2718:0.041}
# L=4 draft-reported (seed 99 + 4242 reproduced exactly by me; seed1 draft value):
L4 = {1:0.193,4242:0.217,99:0.076}
l3=np.array(list(L3.values())); l4=np.array(list(L4.values()))
print("=== HONEST CROSS-L (draft's OWN most-spread selection rule) ===")
print("L=3 most-spread gaps (10 seeds):", sorted(round(x,3) for x in l3))
print("  L=3: min %.3f  median %.3f  max %.3f"%(l3.min(),np.median(l3),l3.max()))
print("L=4 most-spread gaps (3 seeds):", sorted(round(x,3) for x in l4))
print("  L=4: min %.3f  median %.3f  max %.3f"%(l4.min(),np.median(l4),l4.max()))
print()
print("RANGE OVERLAP: L=3 [%.3f, %.3f]  vs  L=4 [%.3f, %.3f]"%(l3.min(),l3.max(),l4.min(),l4.max()))
print("  L=4 range is a SUBSET of L=3 range:", (l4.min()>=l3.min() and l4.max()<=l3.max()))
print("  L=3 max %.3f EXCEEDS L=4 max %.3f by %.3f"%(l3.max(),l4.max(),l3.max()-l4.max()))
print()
print("SAME-SEED comparison (the only matched test) for seeds present at both L:")
for s in (1,4242,99):
    print("  seed %4d:  L=3 gap %+.3f   L=4 gap %+.3f   ratio %.2f   %s"%(
        s,L3[s],L4[s],L4[s]/L3[s], "L4>L3" if L4[s]>L3[s] else "L4<L3 (gap SHRINKS)"))
print()
print("Draft's headline 'doubling': uses ONLY seed-4242 L=3 (+0.088, the 4th-SMALLEST of 10)")
print("  vs 3-seed L=4 median (+0.193). Apples-to-apples L=3 median = %.3f (NOT half of %.3f)."%(np.median(l3),np.median(l4)))
