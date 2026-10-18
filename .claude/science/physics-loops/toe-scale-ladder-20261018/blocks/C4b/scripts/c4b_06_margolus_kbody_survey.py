"""C4b-06: survey of k = 3, 4 magnon clusters in the block-c Margolus QCA (block = identity on
<= 1 magnon per block; out of the Z^3-TI premise).  Exact infinite-lattice dict evolution
(reuses the evolution code of c4b_04 by import; the block unitaries are re-built there).

Question: do multi-magnon clusters move when one- and two-magnon states are frozen?
Diagnostic: max COM displacement reached by any configuration in the support after n two-steps,
and whether the support size has stopped growing (closed reachable set) -- a closed reachable
set is an exact certificate of confinement for that initial condition.
Sample: random initial clusters inside {0..3}^3 (seeded), 8 two-steps.
"""
import io
import contextlib
import math
import numpy as np
import c4b_common

buf = io.StringIO()
with contextlib.redirect_stdout(buf):       # silence c4b_04's own checks on import
    import c4b_04_margolus_magnons as M
c4b_common.PASS = 0
c4b_common.FAIL = 0
from c4b_common import check, total

rng = np.random.default_rng(7)
pts = [(x, y, z) for x in range(4) for y in range(4) for z in range(4)]


def reachable_closed(kind, init, steps, cap=200000):
    st = {tuple(sorted(init)): 1.0 + 0j}
    seen = set(st)
    c0 = np.mean(np.array(init, float), axis=0)
    reach = 0.0
    closed_at = None
    for n in range(1, steps + 1):
        st = M.layer(M.layer(st, kind, 0), kind, 1)
        new = set(st) - seen
        seen |= set(st)
        for conf in st:
            com = np.mean(np.array(conf, float), axis=0)
            reach = max(reach, float(np.sqrt(((com - c0) ** 2).sum())))
        if len(seen) > cap:
            return reach, None, len(seen), n
        if not new and closed_at is None:
            closed_at = n
    return reach, closed_at, len(seen), steps


for k, nsamp, steps in [(3, 120, 8), (4, 40, 8)]:
    reaches, unclosed, capped = [], 0, 0
    for s in range(nsamp):
        init = [pts[i] for i in rng.choice(len(pts), size=k, replace=False)]
        reach, closed_at, nseen, nrun = reachable_closed('c', init, steps)
        reaches.append(reach)
        if closed_at is None:
            unclosed += 1
            print(f"  k={k} init={init}: reachable set not closed within {nrun} two-steps; "
                  f"|seen|={nseen}, COM reach {reach:.3f}")
    print(f"k={k}: {nsamp} random clusters in {{0..3}}^3, {steps} two-steps: max COM reach "
          f"{max(reaches):.3f}, mean {np.mean(reaches):.3f}; not closed: {unclosed}")
    check(f"k={k}: every sampled cluster has a closed (finite, exactly invariant) reachable set "
          f"within {steps} two-steps (confinement certificate per sample)", unclosed == 0)
total()
