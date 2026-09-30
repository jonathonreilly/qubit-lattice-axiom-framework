import numpy as np
import test1_classes as T
DC=T.DC
print('\n--- nearest candidate per class (height <= %d) and the height needed to reach the tight window by 1/H^2 scaling ---'%T.H)
for cl in sorted(set(c[0] for c in T.C)):
    cs=[c for c in T.C if c[0]==cl]
    best=min(cs,key=lambda c:abs(c[3]-DC))
    off=abs(best[3]-DC)
    need=T.H*np.sqrt(max(off,1e-12)/1e-6)  # candidates ~ H^2 dense => spacing ~ 1/H^2
    print('%-24s nearest %-22s height %-3d offset %.2e  -> height needed for +-1e-6 window ~ %.0f'%(cl,best[2],best[1],off,need))
