#!/usr/bin/env python3
"""T73 extras: (1) 1D bulk density under RSA vs flat (Edwards) measure, KL per site;
(2) 2D L=6 uniform RSA entropy (extra volume-class point)."""
import math, sys, time, importlib.util
spec = importlib.util.spec_from_file_location('t', 'test_T73.py')
t = importlib.util.module_from_spec(spec); spec.loader.exec_module(t)

which = sys.argv[1] if len(sys.argv) > 1 else "1d"
if which == "1d":
    for L in (14, 18, 22, 26):
        _, adj = t.grid_adj(L, 1)
        dist = t.frozen_distribution(adj, 1.0)
        N = len(dist); mid = L // 2
        rsa = sum(p for s, p in dist.items() if s >> mid & 1)
        flat = sum(1 for s in dist if s >> mid & 1) / N
        S1 = t.renyi(dist)[0]
        print(f"L={L} N={N} centre-site occupation: RSA {rsa:.4f}  flat(Edwards) {flat:.4f}  ratio {rsa/flat:.4f}   KL(RSA||flat)={math.log(N)-S1:.4f} = {(math.log(N)-S1)/L:.4f} per site", flush=True)
    lam = 1.3247179572447460
    print("infinite chain: flat (Parry) density =", 1/(2*lam**-2 + 3*lam**-3), " RSA jamming density (1-e^-2)/2 =", (1-math.exp(-2))/2)
else:
    L = 6
    _, adj = t.grid_adj(L, 2)
    t0 = time.time()
    dist = t.frozen_distribution(adj, 1.0)
    N = len(dist); S1, S2, Si = t.renyi(dist)
    print(f"2D L=6 w=1: N={N} S0={math.log(N):.4f} S1={S1:.4f} S2={S2:.4f} Sinf={Si:.4f} S1/L^2={S1/36:.4f} S1/S0={S1/math.log(N):.4f} time={time.time()-t0:.0f}s", flush=True)
