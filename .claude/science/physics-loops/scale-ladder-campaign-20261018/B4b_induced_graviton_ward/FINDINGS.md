# B4b findings: Ward identity of the 2026-06-08 staggered Kahler-Dirac induced-graviton kernel

Provenance: same-model-family worker (Claude Opus), not independent. Scripts in this directory; logs
`b4b_ward_symbol.log` (PASS=20 FAIL=3; the FAILs are listed below) and `b4b_variantS_and_mass.log` (PASS=12 FAIL=0).

## Kernel (reconstructed from runners, vectorised re-implementation in `stag_kernel.py`)
Pi_{mn,rs}(K) = N^-4 sum_P tr[G(P) V_mn(Pbar) G(P+K) V_rs(Pbar)], with the 16x16 block staggered D, G = D^dag/Delta,
V_mn = 1/2[Vel_m f_n + Vel_n f_m], Vel = dD/dP, Pbar = P+K/2. The runners use the bubble only, minus Pi(0) (no seagull).
Two vertex variants are in the repo: f = sin(Pbar) (dispersion/telescope runners: "D") and f = sin(Pbar/2)
(isotropy/TT-positive runners: "S"). The runner-cache constants were reproduced: C_time(N=6) = 0.08961606, Zener A = 0.9746.

## Results (D vertex, m=0.7, symbol from Richardson finite differences, N=14 quadrature)
- Symbol is even in K, B4-invariant (projection residual 1e-7). B4 allows 9 two-derivative quadratic invariants (4 Lorentz + 5 extra).
- **Exactly one B4-invariant symbol is gauge invariant: linearised EH.**
- **Ward identity BROKEN at leading order.** max|k_m M2_{mn,rs}| / max|M2| = 0.23. Lattice residual
  |2sin(K/2).(Pi(K)-Pi(0))| scales as K^3.00, so the K^2 symbol itself violates the identity. Without the Pi(0) subtraction it scales as K^1.
  The 10x10 symbol has no 4-dim null space at any sampled k, so there is no gauge redundancy in any linear field basis. Mass-robust: ratio 0.228 at m=0.5 and 0.215 at m=1.
- Decomposition: 92% of the symbol (Frobenius) is not EH; 5.4% is non-Lorentz B4-extra.
- Gauge modes k(x)xi get stiffness: 0.46 x TT for transverse xi and -0.12 x TT for longitudinal xi (wrong sign). The full 10x10 Lorentzian pencil along [100] gives
  c^2 = -8.40, -0.12, 0.46 (x2), 1 (x4), 2.17 (x2). These are extra propagating and unstable modes.
- 4D-TT spectrum is not degenerate: E/T2 = 1.042 along axes (1.058 at m=0.5, 1.026 at m=1.0).
- TT speeds: along [100], c^2 = 1, 1. B4 t<->x exchange forces this. The dispersion runner's yz/t-x "0.043 k0^2" excess is O(k^4): the symbol-level excess is -1e-7.
  Within the TT-restricted pencil, [110] gives c^2 = 1.0304 and 1.0358 (birefringence 5.4e-3) and [111] gives 1.0457 (x2).
  In the full pencil the [110] E-type polarisation mixes with non-TT modes, giving 1.000 and 1.074.
  These numbers belong to a non-gauge-invariant kernel, so they are not physical graviton speeds.
- Pi(0) = 0.101 dd + (-0.336)(dd+dd) + (-0.147) d_mnrs. It is not of cosmological sqrt(g) form, and it has a non-Lorentz piece.
  Read as a TT mass, m^2 = -13 to -16 (block units). The runners discard it by subtraction, and it is scheme-dependent until a seagull is derived.
- The S vertex is not a periodic lattice kernel: shifting the Brillouin-zone window changes Pi by O(1) (relative 2.1 to 2.6; the D control changes by 1e-15).
  Its finite-grid Ward residual is 0.30 to 0.41 of the TT signal.

## FAIL lines
- S2: the N=14 vs N=12 convergence threshold of 1e-5 was set before the run; the measured difference is 1.7e-4. All reported effects are at least 25x larger.
- W1 and T3 are hypothesis tests that were falsified: the Ward identity is exact, and the raw kernel has no birefringence.

## Verdict
The 06-08 bubble kernels are not linearised-diffeomorphism-covariant at leading order, so they are not induced graviton kernels as defined.
Their "TT isotropy" is (a) forced by symmetry on the axes they sampled and (b) not meaningful off-axis without gauge invariance.
Conditional positive (proved here only numerically, B4 basis rank): any completion that restores the Ward identity at the K^2 symbol, using a seagull or counterterm, lands on the unique B4 gauge invariant, linearised EH.
That gives TT degeneracy, common speed, and eps3-type birefringence = 0 at leading order. This agrees with B4.
The restoring counterterm is not derived. It must cancel an O(1) non-invariant part of the power-divergent K^2 coefficient, so the induced 1/G is not fixed by the bubble.
