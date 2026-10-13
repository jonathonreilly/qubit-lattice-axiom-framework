"""Named laws for R16-3 (all |sigma'| <= 1 by construction: sigma' is a pointwise convex blend of adjacent values in {1,-1,0})."""
import numpy as np, sys; sys.path.insert(0, '.')
from zz import ZLaw
def r143_make(b, c, name):
    # re-implementation of R14-3's node law (wit_b.py make): transition j starts at a_j, width w_j
    K = len(c); a = np.linspace(b, np.pi, K+2)[:-1]; w = a[1]-a[0]
    vals = [1.0] + list(c) + [0.0]; widths = [w]*(K+1); widths[-1] = np.pi - a[-1]
    return ZLaw(vals, [aj + wj/2 for aj, wj in zip(a, widths)], widths, name)
W08 = lambda: r143_make(0.8, [-1, 1, 1, -1, -1, 1, 1, -1], 'W08')
W14 = lambda: r143_make(1.4, [-1, 1, -1, -1, -1, 1, 1, -1], 'W14')
def G(b):   # R14-1's G(b): sigma' = 1 - sstep((k-b)/(pi-b))
    return ZLaw([1.0, 0.0], [b + (np.pi-b)/2], [np.pi-b], 'G(%.2f)' % b)
def Z1(wt=0.06):
    # witness: sigma' = 1 on [0,1.0], then -1,+1,-1,+1,-1 on 0.4-long segments, then 0 on [3.0,pi]; C^inf steps of width wt at breakpoints
    return ZLaw([1, -1, 1, -1, 1, -1, 0], [1.0, 1.4, 1.8, 2.2, 2.6, 3.0], wt, 'Z1(wt=%.3f)' % wt)
def Zgen(vals, bks, wt, name='Z'):
    return ZLaw(vals, bks, wt, name)
