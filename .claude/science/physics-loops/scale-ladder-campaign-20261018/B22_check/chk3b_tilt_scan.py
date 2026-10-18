"""B22 check 3b: Definition A (causal cuts, staircase integer-period lapses) for the MASSIVE walk:
relative deviation of the group-commutator displacement from -w g(k0) as a function of the cut tilt
tau = A kk (periods per cell) and coin angle theta, at fixed lapse amplitude A = 64.
Question: is A's deviation O(1) (B22: "no clean limit") or O(tau) (a higher-gradient correction)?
Uses chk3_cut_1d.Circuit (own implementation, reproduces B22 C5 to 5e-5)."""
import sys, os, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib.util
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chk3_cut_1d.py')).read()
lib = src.split('# ---------------------------------------------------------------- L1')[0]
ns = {}; exec(lib, ns)
Circuit, gfun, stair = ns['Circuit'], ns['gfun'], ns['stair']
t0 = time.time()
A = 64
print("  theta   tau=A*kk    Lc      ratio(k0=+0.1)  ratio(k0=-0.1)  mean|ratio-1|")
res = {}
for th in (0.2, 0.5, 1.0):
    for M_ in (64, 128, 256, 512):
        Lc = M_ * A; Cc = Circuit(Lc, th); kk = 2 * np.pi / Lc; tau = A * kk
        d = min(0.9, 1.5 * tau)
        FN = lambda X: 2 * stair(A * np.cos(kk * X), d); FM = lambda X: 2 * stair(A * np.sin(kk * X), d)
        w = A * A * kk; r = []
        for k0 in (0.1, -0.1):
            psi = Cc.packet(k0, 0.244 * Lc, 20.0); out = Cc.commutator(psi, FN, FM)
            r.append((Cc.xmean(out) - Cc.xmean(psi)) / (-w * gfun(k0, th)))
        res[(th, M_)] = (tau, r)
        print(f"  {th:.1f}    {tau:.4f}   {Lc:6d}     {r[0]:.4f}          {r[1]:.4f}         {np.mean(np.abs(np.array(r) - 1)):.4f}", flush=True)
print("\n  slope of log(mean|ratio-1|) vs log(tau) per theta (1 = deviation proportional to tilt):")
for th in (0.2, 0.5, 1.0):
    tv = np.array([res[(th, m)][0] for m in (64, 128, 256, 512)])
    dv = np.array([np.mean(np.abs(np.array(res[(th, m)][1]) - 1)) for m in (64, 128, 256, 512)])
    print(f"  theta = {th}: slope {np.polyfit(np.log(tv), np.log(dv), 1)[0]:.3f};  deviations {np.round(dv, 4)}")
print(f"({time.time() - t0:.1f} s)  [informational scan; no PASS lines]")
