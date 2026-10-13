# R19-7 method, fixed before any spectral run (2026-10-13 ~04:25Z)

Registration: TESTS:7425-7448 (R19-7). FIXED readings TESTS:7444-7447 used verbatim.

## Setting (literal, as R18-1/R19-1)
- N0914 slots (6 per site), integer stencil from R18-1 common.py (rechecked: G_matrix, pattern_vectors identical
  to R19-1's archived copy), labels n in {0,1}, mod-2 law, gamma = Gn/2, E = sum gamma^2.
- Moves: XOR of cube + three mu8 orientations, every pattern at every base site (with multiplicity, wraps
  reduced mod L, exactly as R19-1 s1_ed_L2.py). Sector: trivial coset = span of the moves.
- H(v, bU) = sum_m [ -t X^{p_m} + v * exp(-bU*Delta_m(C)/2) ],  t = 1, Delta_m(C) = E(C xor p_m) - E(C).
  v = t is R19-1's RK Hamiltonian (Lemma 1 there). Identity moves (p_m = 0 at small L) contribute only the
  constant (v - t) and are dropped (as R19-1 does at v = t). Off-diagonal -t <= 0: stoquastic for every real v.
- Signs of law data (rule TESTS:7125): t > 0, v real (v < 0 included as a tested regime and labelled), no signed
  classical weights.

## Sign-free method: exact diagonalisation (no QMC unless time remains)
- Clusters: the L = 2 cube (1024 states; full diagonalisation) and anisotropic Lx x Ly x Lz tori with
  Lx = Ly = 2 and Lz chosen as the largest values whose coset dimension d <= 23 (selection by d only, made before
  any spectral run). Basis: states = F2 coefficient vectors c in {0,1}^d over a row-reduced basis of the move span;
  every move is an XOR mask on c, so H acts matrix-free (psi[c xor mask]).
- Ground state: Lanczos (scipy eigsh, which='SA') on the stoquastic H; uniqueness checked by the second
  eigenvalue (Perron-Frobenius predicts a unique positive ground state in the connected coset).
- Dynamical structure factor S_X(k, w) for X in {TT1, TT2 (T2 along axes), V1, V2, S}, R19-1's polarisations and
  normalisation (cvec: eps_jj diagonal, 2 eps_ij face; channel_pols), observable O_k = V^-1/2 sum_s c_s e^{-ik.pos}(n_s - 1/2).
  At L = 2: exact spectral decomposition. At larger d: Lanczos continued fraction from O_k psi0 (connected part),
  M = 200 steps, poles and weights from the tridiagonal (Gauss quadrature; exact for the low moments).
- Max-ent-free diagnostics per (k, channel), all from the same spectral data:
  (i)   first-moment / SMA  w_SMA = f/S, f = <O|(H-E0)|O>, S = <O|O> (connected);
  (ii)  lowest pole carrying >= 10% of S ("main pole"), and the lowest pole with any weight >= 1e-6 S;
  (iii) imaginary-time decay rate = -d ln C(k,tau)/dtau evaluated at tau = 2/w_SMA and tau = 20/w_SMA
        (C computed exactly from the poles).
- k-points: axis k = (0,0,2 pi m/Lz), m = 1..Lz/2 on 2x2xLz; at L = 2 the axis (0,0,pi), face (pi,pi,0), body (pi,pi,pi)
  (R18-10 off-axis rule; on 2x2xLz also (pi,pi,k_z)-type off-axis points are reported where available).
- Grid: v/t in {-1, 0, 0.25, 0.5, 0.75, 0.9, 1, 1.1, 1.25, 1.5, 2, 4}; bU in {0.5, 1, 2, 3}; bU = 0 is
  v-independent (diagonal = v * #moves, a constant), solved exactly by R19-1 Lemma 2.
- Checks before use: v = t reproduces R19-1 s1 (gap 0.840445 at bU=1, 0.087565 at bU=2 at L = 2; TT2 main pole
  8.2159 at k=(0,0,pi), bU = 1); H psi0 = 0 at v = t; Lanczos vs full ED agree at L = 2.

## Pre-stated linearity criterion (for LINEAR-T2-EVIDENCE)
- A T2 (TT2 along axes; TT1/TT2 off-axis) main pole w(k) at >= 3 nonzero k-points along one direction with
  w(k)/|k| constant within 15% and w at the smallest k below 0.5 x w at the largest; V and S main poles at
  every k above the T2 pole at the smallest k by a factor >= 2 (gapped V/S); the same pattern on two cluster sizes.
- With 2 x 2 x Lz, Lz <= 6, at most 3 nonzero axis k exist (Lz = 6). If no cluster with 3 nonzero k fits, linearity
  cannot be certified and LINEAR-T2-EVIDENCE is unreachable by construction (stated, not hidden).
- NO-LINEAR is checked only in the operational sense "the T2 main pole is k-flat (gapped) or rises faster than
  linear" at every tested v/t, on two sizes. A tiny finite-size gap that is k-flat counts as gapped only if it does
  not shrink with cluster size beyond 30%; otherwise OPEN.

## Analytic probes (to be done alongside)
- v = 0: H = -t sum X^p, exactly the bU = 0 RK point up to a constant (gapped flat bands; R19-1 Lemma 2).
- bU = 0: v-independent.
- Large bU, v > 0: the diagonal term is exponentially large on charged states with a charge-lowering move;
  effective dynamics on the gamma = 0 manifold (integer law: R16-7/R16-11 class, R18-1 frozen moves).
- Perron-Frobenius uniqueness; stability of the v = 0 gap (comparator only).

## Rules
- OMP_NUM_THREADS=2; each run < 10 min; no repo edits; no downloads.
