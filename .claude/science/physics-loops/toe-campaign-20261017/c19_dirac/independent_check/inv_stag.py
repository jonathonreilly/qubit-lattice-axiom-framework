"""Why O-invariant staggered A1 terms keep 4-fold levels at the folded k*: inversion parity of the bases."""
import numpy as np
from core import *
from bases import get
eI, sI = PSGI
def same(a, b, sgn):
    keys = set(a) | set(b)
    return all(np.allclose(a.get(k, 0), sgn * b.get(k, 0)) for k in keys)
for nm in ('Q_onsite_re_A1', 'Q_onsite_im_A1', 'Q_r1_re_A1', 'Q_r1_im_A1', 'Q_onsite_im_A2', 'Q_onsite_re_A2', 'X_r1', 'P0_onsite_im_O'):
    bs = get(nm); ev = od = 0
    for m in bs:
        Im = act(INV, eI, sI, m)
        ev += same(Im, m, 1); od += same(Im, m, -1)
    print(f"{nm:16s} dim {len(bs):3d}: inversion-even elements {ev}, inversion-odd {od}")
