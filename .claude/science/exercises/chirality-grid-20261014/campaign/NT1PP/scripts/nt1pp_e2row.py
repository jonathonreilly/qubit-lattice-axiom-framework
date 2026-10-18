"""NT-1'' E2-edge (PREREG F1, descriptive): E2 statistic with y at the bottom time edge: x-link (0, t=-T+1), t-link (0, t=-T+1).
usage: python3 nt1pp_e2row.py Lx T W0 trow (y = x-link (0,trow), t-link (0,trow))"""
import sys, time
import numpy as np
from nt1pp_common import *
Lx, T, W0, tr = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]); t00 = time.time()
S = Strip(Lx, T); A = uniformW(S, W0); ys = [S.key[('x', 0, tr)], S.key[('t', 0, tr)]]
chunk = 1 if S.N >= 192 else 2; out = {}
for model in ('11112', 'L1'):
    MS = Measure(S, model, Ns=8); resp, g, ok = fd_response(MS, A, ys, chunk=chunk)
    tq_m, tq_s = tail_stat(S, resp['kQ'], ys); tk_m, _ = tail_stat(S, resp['kbb'], ys); out[model] = (tq_m, tk_m)
    print(f"Lx={Lx:2d} Lt={2*T} W0={W0} {model:5s} row {tr} y: gmin {g:.3f} idx {ok} | tau_kQ(s*) {tq_m:.3e} tau_kQ(Lx/2) {tq_s:.2e} tau_kbb(s*) {tk_m:.3e} [{time.time()-t00:.0f}s]", flush=True)
np.save(f"e2row{tr}_Lx{Lx}_Lt{2*T}_W{W0}.npy", np.array([out['11112'], out['L1']]))
