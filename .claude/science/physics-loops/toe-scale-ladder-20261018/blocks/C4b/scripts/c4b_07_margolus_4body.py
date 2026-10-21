"""C4b-07: probability-weighted motion of the 4-magnon clusters flagged by c4b_06 (block-c Margolus;
out of the Z^3-TI premise).  Exact evolution with amplitude pruning |amp| < EPS; the discarded
norm is reported (so the pruning error is explicit).  Diagnostic: <dCOM^2>(n) and the weight
P_far(n) of configurations whose COM moved by more than 2 lattice units.
Prediction declared before the run: if 4-clusters are mobile, P_far(n) grows with n and
<dCOM^2> grows faster than any bounded function; if confined, both saturate.
"""
import io
import contextlib
import numpy as np
import c4b_common

buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    import c4b_04_margolus_magnons as M
c4b_common.PASS = 0
c4b_common.FAIL = 0
from c4b_common import check, total

EPS = 1e-6
inits = [[(1, 1, 0), (1, 0, 2), (0, 2, 2), (0, 1, 1)],
         [(3, 1, 2), (2, 3, 3), (3, 2, 1), (1, 2, 3)]]
for init in inits:
    st = {tuple(sorted(init)): 1.0 + 0j}
    c0 = np.mean(np.array(init, float), axis=0)
    lost = 0.0
    hist = []
    for n in range(1, 7):
        for par in (0, 1):
            st = M.layer(st, 'c', par)
            small = {k: v for k, v in st.items() if abs(v) < EPS}
            lost += sum(abs(v) ** 2 for v in small.values())
            st = {k: v for k, v in st.items() if abs(v) >= EPS}
        msd = 0.0
        pfar = 0.0
        for conf, a in st.items():
            d2 = float(((np.mean(np.array(conf, float), axis=0) - c0) ** 2).sum())
            msd += abs(a) ** 2 * d2
            if d2 > 4.0:
                pfar += abs(a) ** 2
        norm = sum(abs(a) ** 2 for a in st.values())
        hist.append((n, msd, pfar))
        print(f"init={init} n={n} |supp|={len(st)} norm={norm:.6f} discarded={lost:.2e} "
              f"<dCOM^2>={msd:.4f} P(|dCOM|>2)={pfar:.4f}", flush=True)
        if len(st) > 1500000:
            print("  [stopped: support cap 1.5e6 -- operational]")
            break
    grows = hist[-1][2] > hist[0][2] + 0.01 and hist[-1][1] > hist[0][1]
    print(f"  -> P_far: {[round(h[2], 4) for h in hist]}; <dCOM^2>: {[round(h[1], 3) for h in hist]}")
    check(f"4-cluster {init}: weight transported beyond |dCOM|>2 grows with n (mobile cluster), "
          f"pruning loss {lost:.1e}", grows and lost < 1e-3)
total()
