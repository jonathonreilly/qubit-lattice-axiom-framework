"""Order-of-magnitude DQMC cost/memory for the 2+1D tests (suggested; not a benchmark).
Model scale anchored on He-You-Xu arXiv:2603.18278: 8 modes per honeycomb cell, L<=20,
projector length 2*Theta = L+30, dtau = 0.1. Cost ~ Ltau * Nfields * N^2 flops per sweep
(local HS updates), Nfields ~ N. Effective single-core throughput assumed 16 GFLOP/s."""
GF = 16e9
def est(L, modes_per_cell=8, layers=1, sweeps=2000, couplings=15, nstab=10):
    N = modes_per_cell * L * L * layers
    Ltau = int((L + 30) / 0.1)
    flops_sweep = Ltau * N * N**2
    ch_point = flops_sweep * sweeps / GF / 3600
    mem_GB = (Ltau / nstab) * N * N * 16 / 1e9   # stored complex matrices for stabilisation
    return N, Ltau, ch_point, ch_point * couplings, mem_GB
for label, kw in [("far surface only, L=12", dict(L=12)),
                  ("far surface only, L=20", dict(L=20)),
                  ("slab, 6 layers, L=12", dict(L=12, layers=6)),
                  ("slab, 6 layers, L=20", dict(L=20, layers=6))]:
    N, Lt, cp, cs, m = est(**kw)
    print(f"{label:24s} N={N:6d} Ltau={Lt:4d}  core-h/point={cp:9.3g}  core-h/scan(15)={cs:9.3g}  mem~{m:7.3g} GB")
print("cloud CPU at $0.01-0.05 per core-hour (spot/on-demand range, assumption)")
