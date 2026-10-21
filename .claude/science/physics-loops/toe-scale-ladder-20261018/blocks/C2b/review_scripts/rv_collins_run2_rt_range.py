#!/usr/bin/env python3
"""Reviewer run 2 (rv_collins.log kept: RT failed there because m a >= 0.00625 is still pre-asymptotic for
the dimension-5 mismatch, same as the author's run 2). Same reviewer integrator (rv_collins.Z); RT extended
to m a = 1.95e-4; limits also estimated by a least-squares fit A(m) = A_inf + c1 m + c2 m ln m (different
from a geometric-tail estimate)."""
import sys, time
import numpy as np
from rv_collins import Z
P = F = 0
def chk(n, ok):
    global P, F
    P += bool(ok); F += (not ok); print(('PASS ' if ok else 'FAIL ') + n, flush=True)
t0 = time.time()
res = {}
def run(kind, par, MS):
    out = []
    for m in MS:
        a = {}
        for q in (6, 8):
            a[q] = Z(kind, par, m, q, 2.0, 0) - Z(kind, par, m, q, 2.0, 1)
        print(f'{kind} par={par} m={m:.7f}: Z0-Zs q6 {a[6]:+.8e} q8 {a[8]:+.8e} [{time.time()-t0:4.0f}s]', flush=True)
        out.append((m, a[8], abs(a[6] - a[8])))
    return np.array(out)
def fit(arr, mmax):
    sel = arr[arr[:, 0] <= mmax]; m = sel[:, 0]
    X = np.column_stack([np.ones_like(m), m, m*np.log(m)])
    c, *_ = np.linalg.lstsq(X, sel[:, 1], rcond=None)
    return c[0], np.max(np.abs(X @ c - sel[:, 1]))
MS_RT = [0.025*2**-j for j in range(8)]          # 0.025 ... 1.95e-4
rt = run('RT', 0.5, MS_RT)
chk(f'RT: mesh change q6 vs q8 below {rt[:,2].max():.1e} < 1e-6', rt[:, 2].max() < 1e-6)
st = np.abs(np.diff(rt[:, 1])); r = st[-1]/st[-2]
print('RT steps', np.array2string(st, formatter={'float_kind': lambda x: f'{x:.2e}'}), f' last ratio {r:.3f}')
tail = st[-1]*r/(1 - r)
lim_g = rt[-1, 1] - tail
lim_f, resid = fit(rt, 0.0032)
CRg, CRf = 8*np.pi**2*(-lim_g), 8*np.pi**2*(-lim_f)
print(f'RT limit: geometric {lim_g:+.5e} (C = {CRg:.3f}); fit A_inf + c1 m + c2 m ln m on m <= 0.0032: {lim_f:+.5e} (C = {CRf:.3f}, max resid {resid:.1e})')
chk(f'RT: converging (last step ratio {r:.2f} < 0.8) to a nonzero limit (|A_min| = {abs(rt[-1,1]):.3e} > 20 x tail {tail:.1e})', r < 0.8 and abs(rt[-1, 1]) > 20*abs(tail))
chk(f'RT: C ~ 0.93 reproduced within 10% (geometric {CRg:.3f}, fit {CRf:.3f})', abs(CRg - 0.93) < 0.093 and abs(CRf - 0.93) < 0.093)
MS_T = [0.025*2**-j for j in range(6)]
t3 = run('T3', 0.5, MS_T)
lim_t, resid_t = fit(t3, 0.0125)
CT = 8*np.pi**2*(-lim_t)/0.5
print(f'T3 eps=0.5 fit limit {lim_t:+.5e} (C per unit eps = {CT:.3f}, max resid {resid_t:.1e})')
chk(f'T3: fit-based C per unit eps {CT:.3f} ~ 0.36 within 10%', abs(CT - 0.36) < 0.036)
chk('T3: |A| at m = 7.8e-4 exceeds |A| at m = 0.025 (grows toward the continuum, no power suppression)', abs(t3[-1, 1]) > abs(t3[0, 1]))
print(f'elapsed {time.time()-t0:.0f}s')
print(f'TOTAL: PASS={P} FAIL={F}')
sys.exit(1 if F else 0)
