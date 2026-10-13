# R18-10 method, fixed before any run (2026-10-13 ~03:06Z)

Item: TESTS:6871-6897 (R18-10), readings FIXED at :6891-6894. Setting as R18-1 (N0914 slots, mod-2 law,
labels n in {0,1}, gamma = Gn/2, weight exp(-bU sum_edges gamma^2), shift action P112), plus: the move set conserves
the gamma-dipole D_ab = sum_x x_a gamma_b(x) in addition to Gn mod 2.

## Analytic step (before numerics)
A1. Moment lemma on the stencil (N0914:95-97; rR17-1 s3; vR17-1:10): for finitely supported integer delta,
    D(G delta) = -M0(delta). Compute the exact tensor map slot type -> D for this stencil, and hence what
    "the move conserves D(gamma)" means for an XOR flip (signed change s = n' - n on the flipped slots).
    Expected: D-conservation <=> each slot-type total N_ab = sum_x n_ab(x) is conserved. Check by exact integer
    arithmetic on unwrapped (Z^3) supports for every pattern copy and random signings.
A2. Stationary measure of a symmetric-proposal Metropolis chain with a symmetric kinetic filter (accept only
    D-conserving flips) = weight restricted to the communicating class (standard; state proof).
    Consequence to test: the static ensemble is R18-1's grand-canonical one conditioned on the sector
    {coset, N_ab fixed}; by ensemble equivalence (Lebowitz-Percus; comparator, RECALLED) S(k != 0) should
    differ from R18-1's only by O(1/V) IF the filtered chain is ergodic in the sector. If it fragments, the
    sampled Krylov sector is reported and the reading is OPEN.

## Move set (probe a)
Proposals: R18-1's patterns (cube; mu8 in 3 orientations), every translate, XOR flip; ACCEPT only if the signed
per-type count change dN_ab = 0 for all six types (== dD(gamma) = 0 for non-wrapping supports, by A1), then
Metropolis on exp(-bU sum gamma^2). Optional second family (declared now, used only if the first freezes or
fragments): XOR of a pattern and its unit translate (pattern "hop").
Sector: trivial coset (as R18-1) intersected with N_ab = V/2 for all six types (the F_all- and shift-action-
covariant half-filling sector; n = 0 is a frozen singleton sector, N = 0). Starting states: a grand-canonical
(R18-1 chain) equilibrium state driven to N_ab = V/2 exactly by accepting only moves that do not increase
sum_ab |N_ab - V/2| (a preparation step only; then the conserving chain runs).
Checks: detailed balance (proved, A2) and exact enumeration at L = 2 (coset dim 10; connected components of the
filtered move graph vs the N-sectors; MC vs exact restricted Boltzmann). Ergodicity at L >= 6 cannot be
enumerated; evidence used: (i) hot (bU = 0 GC) vs cold (GC at bU+1) starts agree; (ii) every slot flips;
(iii) energy and S agree with the grand-canonical chain run by the same code. Failure of (i)-(iii) => OPEN.

## Observables (probe b), as R18-1 (fixed)
E/edge (charged-edge fraction), rho(q) = S_xz,xz(k||z)/S_xz,xz(k||y) averaged over cubic copies,
xi^2(q) = (1/rho - 1)/q^2 at the two smallest axis q, S_gamma/q^2 and S_gamma/q^4 at q_min (axis), S_T(q1).
bU in {0.5, 1, 2, 3} at L = 6, 8, 10 (12 at bU = 2 if time); bU = 4 at L = 6, 8 if time. Grand-canonical
reference runs (same code, no filter) at bU = 2 (L = 6, 8, 10) to recheck R18-1 and compare directly.
Readings (TESTS:6891-6894): PINCH-PRESENT needs xi^2 growing ~ L^2 at some finite bU (xi/L constant) and
S_gamma/q^2 -> 0; SCREENED needs xi finite and L-independent at every finite bU tested; non-ergodic => OPEN.
(c) helicity check of the readout only if a pinch appears. (d) prices.
Each run < 10 min, OMP_NUM_THREADS=2, at most 4 concurrent single-thread runs. No extrapolation beyond largest L.
