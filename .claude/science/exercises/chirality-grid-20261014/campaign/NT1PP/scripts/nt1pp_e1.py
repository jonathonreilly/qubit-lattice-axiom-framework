"""NT-1'' E1 (PREREG section 5): the fixed minimal (b') test on NT-1' ensemble configurations (W-centred), Lt = 8.
tau_c = max over y in {x(0,0), x(0,1), t(0,0)} and mixed pairs at s* = Lx/2 - 0.5 (|dt_mid| <= 0.5) of |d kQ_m / d A_y|.
usage: python3 nt1pp_e1.py Lx [nconf]"""
import sys, time
import numpy as np
from nt1pp_common import *

Lx = int(sys.argv[1]); nconf = int(sys.argv[2]) if len(sys.argv) > 2 else 6; T = 4
S = Strip(Lx, T); rng = np.random.default_rng(4600 + Lx); t00 = time.time()
ys = [S.key[('x', 0, 0)], S.key[('x', 0, 1)], S.key[('t', 0, 0)]]
M2 = Measure(S, '11112', Ns=8); M1 = Measure(S, 'L1', Ns=8)
print(f"# NT-1'' E1 Lx={Lx} Lt={2*T} N={S.N} seed {4600+Lx} nconf {nconf}; ys = {ys}", flush=True)
rows = []; rej = 0; draws = 0
while len(rows) < nconf and draws < nconf + 40:
    draws += 1
    A = gen_config(S, rng, center=True)
    try:
        b = M2.ray(A, 8)
    except AssertionError:
        rej += 1; print(f"  draw {draws}: rejected (index change on the ray, G6)", flush=True); continue
    if not (b['gmin'] >= 0.1 and b['idx_ok']):
        rej += 1; print(f"  draw {draws}: rejected (gmin {b['gmin']:.3f}, idx_ok {b['idx_ok']})", flush=True); continue
    try:
        r2, g2, ok2 = fd_response(M2, A, ys)
        r1, g1, ok1 = fd_response(M1, A, ys)
    except AssertionError:
        rej += 1; print(f"  draw {draws}: rejected (index change on an FD ray, G6)", flush=True); continue
    if not (g2 >= 0.1 and ok2 and g1 >= 0.1 and ok1):
        rej += 1; print(f"  draw {draws}: rejected on FD rays", flush=True); continue
    tq, tqs = tail_stat(S, r2['kQ'], ys); tk, _ = tail_stat(S, r2['kbb'], ys); t1, _ = tail_stat(S, r1['kQ'], ys)
    F, W = S.FW(A)
    rows.append((tq, tqs, tk, t1))
    print(f"  conf {len(rows)-1} (draw {draws}): gmin {min(b['gmin'], g2):.3f} Wbot {W[0,0]:+.2f} Wtop {W[0,-1]:+.2f} | 11112 tau_kQ(s*) {tq:.3e} "
          f"tau_kQ(Lx/2) {tqs:.2e} tau_kbb(s*) {tk:.3e} | L1 tau_kQ(s*) {t1:.3e} [{time.time()-t00:.0f}s]", flush=True)
R = np.array(rows); n = len(R)
if n:
    m = R.mean(0); se = R.std(0, ddof=1) / np.sqrt(n) if n > 1 else np.full(4, np.nan)
    print(f"SUMMARY Lx={Lx}: n={n} rejected={rej} | 11112 tau mean {m[0]:.4e} SE {se[0]:.2e} max {R[:,0].max():.3e} | "
          f"L1 plateau mean {m[3]:.4e} SE {se[3]:.2e}; Lx*plateau {Lx*m[3]:.4f}; ratio L1/11112 {m[3]/m[0]:.1f}")
np.save(f"e1_Lx{Lx}.npy", R)
