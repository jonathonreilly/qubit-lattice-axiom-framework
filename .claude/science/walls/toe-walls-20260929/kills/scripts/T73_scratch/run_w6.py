import sys, math, importlib.util
spec = importlib.util.spec_from_file_location('t', 'test_T73.py')
t = importlib.util.module_from_spec(spec); spec.loader.exec_module(t)
L=int(sys.argv[1]); w=float(sys.argv[2])
_, adj = t.grid_adj(L,2)
dist = t.frozen_distribution(adj, w)
N=len(dist); S1,S2,Si=t.renyi(dist)
print(f"L={L} w={w} N={N} S0={math.log(N):.4f} S1={S1:.4f} S2={S2:.4f} Sinf={Si:.4f} S1/S0={S1/math.log(N):.4f} S1/L^2={S1/L**2:.4f}", flush=True)
