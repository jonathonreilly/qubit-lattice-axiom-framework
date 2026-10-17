"""Folded spectrum with finite O-invariant staggered A1 terms: degeneracies at k* and at generic k;
and which candidate symmetries (I, I.T_x as Bloch maps) the staggered terms respect."""
import numpy as np
from core import *
from bases import get
rng = np.random.default_rng(2)
fm = fixed_momenta(); KS = np.array(fm[0]) * np.pi / 4
def rnd(bs):
    c = rng.normal(size=len(bs)); m = addm(*bs, coeffs=list(c)); nrm = max(np.abs(M).max() for M in m.values()); return {k: v / nrm for k, v in m.items()}
Hb = addm(hop(-1.0, 0.2), rnd(get('X_r1')), coeffs=[1, 0.05])
eI, sI = PSGI
for nm in ('Q_onsite_re_A1', 'Q_onsite_im_A1', 'Q_r1_re_A1', 'Q_r1_im_A1'):
    S = rnd(get(nm)); SI_ = act(INV, eI, sI, S)
    ip = max(np.abs(S.get(k, 0) - SI_.get(k, 0)).max() for k in set(S) | set(SI_))
    im = max(np.abs(S.get(k, 0) + SI_.get(k, 0)).max() for k in set(S) | set(SI_))
    k = rng.uniform(-np.pi, np.pi, 3)
    eg = np.linalg.eigvalsh(fold(Hb, {a: 0.3 * b for a, b in S.items()}, k))
    e0 = np.linalg.eigvalsh(fold(Hb, {a: 0.3 * b for a, b in S.items()}, KS))
    print(f"{nm}: |S - I S| = {ip:.2f}, |S + I S| = {im:.2f}; min level spacing at generic k {np.diff(eg).min():.2e}; at k*: levels {np.round(e0[:8],4)}")
