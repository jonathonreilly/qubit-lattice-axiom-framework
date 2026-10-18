"""QMC-1 cost model (suggested): projections of this engine's cost from measured pilot timings.

Model: seconds per sweep T = a * N_d^3 * L_tau (local rank-D updates + stabilisation are O(N_d^3) per slice), with
N_d = 32 * (number of sites) (Spin(10) d-frame), calibrated on the measured 2+1D L = 6 sweep time (this machine,
numpy + Accelerate, 2 BLAS threads).  Memory: complex128 N_d x N_d matrices; left UDV stack (L_tau/n_s + 1) x 2
matrices + ~10 work matrices.  Sweeps per W point: 1000 (pilot runs used 45-60; autocorrelation of S10 measured
~0.5-1.2 sweeps, but run lengths at larger L are unknown).
Optional factor 1/8: the singlet-only Fierz vertex in 2D with f2 or f == 1 gives det = |det_sector|^2 (check_sector.py),
halving N_d per determinant.
"""
import numpy as np

T6, Nd6, Lt6 = 29.7, 32 * 36, 40        # measured 2+1D L = 6, beta = 4, dtau = 0.1 (runs/L6_f2_W2.log)
a = T6 / (Nd6 ** 3 * Lt6)
print(f"calibration a = {a:.3e} s per (N_d^3 L_tau); check 2D L = 4: predicted {a * 512**3 * 40:.1f} s, measured ~3.6 s "
      f"(python overhead dominates at small N_d)")
print("| geometry | L | sites | N_d | beta | L_tau (dtau 0.1) | s/sweep (2 threads) | core-h / 1000 sweeps | "
      "with |det_sector|^2 (2D only) | memory (n_s = 4) |")
print("|---|---|---|---|---|---|---|---|---|---|")
for geo, L, dim in [("2+1D", 8, 2), ("2+1D", 10, 2), ("2+1D", 12, 2), ("3+1D", 4, 3), ("3+1D", 6, 3), ("3+1D", 8, 3)]:
    sites = L ** dim; Nd = 32 * sites
    for beta in (4.0, float(L)):
        Lt = int(round(beta / 0.1))
        T = a * Nd ** 3 * Lt
        ch = T * 2 * 1000 / 3600
        mem = (Lt / 4 + 1 + 0.5 * 10) * 2 * Nd ** 2 * 16 / 2 ** 30
        fac = f"{ch / 8:,.0f}" if dim == 2 else "n/a"
        print(f"| {geo} | {L} | {sites} | {Nd} | {beta:g} | {Lt} | {T:,.0f} | {ch:,.0f} | {fac} | {mem:,.1f} GB |")
