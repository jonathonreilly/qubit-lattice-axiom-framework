# LOCK-1 pre-registration (written 21:43Z 2026-10-17, before any run)

Agent: Claude Opus 5.5 (xhigh), same family as the supervisor; not independent.
Deadline: 00:30Z 2026-10-18. Cap 0.4 GB via scripts/capped.sh, one process at a time.

## Fixed readings (TESTS.md, LOCK-1 entry; copied, not changed)
- LOCK-EVEN: every landed rule family gives an even-period lock across its stated parameter range, wherever it orders.
- LOCK-SAFE: some landed family, in its stated range, gives a liquid or odd-period state at matter-relevant density.
- LOCK-MIXED: both occur, with the boundary stated.
- OPEN: otherwise.
Classes: period-2 locked / odd-period locked / other even period / liquid-floating.
Scope to state: rules, parameters, finite size, method.

## Prior art read (origin/main, step 0)
- Static law with vacancies = record gas: block 39 (PR 8530, ...RECORDS_THAT_MOVE_PAIR_WEIGHT_TRANSIT...2026-09-20.md: T1 motion equilibrium = static law at fixed N; T5 RP iff c >= c0), block 40 (...BINDING_SCALE_PINNED_AT_THE_NEUTRAL_VALUE...: proposal g = c/c0 = 1; T4 off-neutral = content-less gas with bond activity c/c0), block 81 (...RECORD_GAS_NEVER_MAKES_THE_CHESSBOARD...: weight z^N 6^N g^B Q; finite only), block 117 (...RECORD_GAS_DOES_MAKE_THE_CHESSBOARD...: chessboard for g <= 9/62500 at zeta = g^-3, grand canonical; open: canonical ensemble, window 0.3-0.5), uniqueness note (...WHERE_MOVING_RECORDS_CANNOT_CLUMP...49_OVER_25...: unique state for 25/49 < g < 49/25, content-less, every z), neutral-scale order note 2026-09-26 (two-valued menu: no LRO for z < 1/320; aligned order at large beta and high density), block 126 (vacancies, infrared bound above neutral).
- Quantum exclusion walkers: blocks 121, 125, 130 (ring = one twisted band), 137, 141-143; 3D many-record ground state not on main.
- Signed hopping + density repulsion (RECORD_CONSERVING_INTERACTION_KEEPS_THE_STAGGERED_SECTOR...2026-09-03): finite cubes, half filling only.
- Block 133: one massive body at rest on one sublattice (single-walker statement, not a many-record ordering rule).

## Families and parameter ranges to classify
F1 static law with vacancies (record gas). Weight per arrangement on the torus: prod over recorded bonds of g*M(s,s'), M = 6 omega/(p+q+4r), contents summed uniformly (block 117's Q), canonical at fixed N (block 39 T1: motion conserves N and contents; equilibrium = static law).
  - g ranges on main: 9/62500 and below (block 117), 1/4, 1, 4 (block 81 fixtures), 1/2, 1, neutral (block 39 map), 25/49 < g < 49/25 (uniqueness), g >= 1 (RP), g = 1 (block 40 proposal).
  - triples: content-less (p=q=r); (3,1,2); (12,1,2).
F2 quantum exclusion walkers; F3 signed hopping + repulsion; F4 block 133: classified from main's own statements only (no new runs planned; reasons in report).

## Method (F1 only)
- Metropolis Monte Carlo of the static law, canonical N = round(rho V), periodic L^3 tori, L in {8, 12, 16, 24} (12, 24 admit periods 2, 3, 4, 6). Moves: nonlocal record-vacancy exchange (carries content) and content re-draw (heat bath). This samples the static law; it is not the motion clause's dynamics.
- Densities rho in {1/8, 1/4, 3/8, 1/2}.
- C1 content-less: g in {0, 0.02, 0.1, 0.2, 0.3, 0.35, 0.4, 0.45, 0.5, 1, 2, 4, 8}.
- C2 contents (3,1,2), (12,1,2): g in {1e-5, 0.25, 1, 4}, rho in {1/8, 1/4, 1/2}, L in {12, 16}.
- C3 hard-core edge: g = 0, rho in {0.16, 0.18, 0.20, 0.21, 0.22, 0.24}, L in {12, 16, 24}.
- Observables: staggered m_s = (N_A - N_B)/V, its Binder U = 1 - <m^4>/(3<m^2>^2); full S(k) = <|n(k)|^2>/V over the L^3 grid, its maximum over k != 0 and location; S(k_min)/V at k_min = 2 pi/L (clumping); content vectors: uniform |sum s|^2/N^2 and staggered.
- Classification per (g, rho):
  - period-2 locked: Bragg peak at a corner k* in {0,pi}^3 \ {0} with S(k*)/V not decreasing with L (L=16 -> 24 ratio > 0.7) and U(24) > 0.5;
  - odd period / other even period: same test at a non-corner k* != 0 with components in 2pi/c;
  - clumped (phase separated, uniform dense phase, period 1): S(k_min)/V not decreasing with L and no Bragg peak elsewhere;
  - liquid: max_k S(k)/V decreasing like 1/V (ratio L=16 -> 24 < 0.5) and U(24) < 0.3;
  - otherwise "near boundary".
- Error: standard error from 10 block means per run; hysteresis check at L=16 from random and chessboard starts.
- Equilibration: 2000 sweeps discarded (sweep = V attempted exchanges + V content updates), 4000 measured, measurements every 5 sweeps; L=24 near boundaries may be under-equilibrated; reported as such.
- Comparators (not results): sc Ising K_c = 0.2216544 (cited in block 39) gives g_N(1/2) = e^{-4 K_c} ~ 0.412 for the half-filling chessboard and e^{4 K_c} ~ 2.43 for clumping; hard-core nearest-neighbour exclusion on sc orders above a density near 0.2 (literature value to be checked).

## Reading rule
Apply the fixed readings to F1 over main's stated g ranges and densities 1/8-1/2, plus main's own statements for F2-F4. If F1 shows both a period-2 lock and a liquid at matter density in main's stated ranges, the reading is LOCK-MIXED with the boundary g_N(rho) stated; the RP / neutral sub-range is reported separately.

## Follow-up (21:54Z, after C1 read out; PREREG text above unchanged)
- C1 at L=24, rho=1/2, g=0.02 and 0.1 from random starts gave SQ/V = 0.11 and 0.013 against 0.25 at L=16 (frozen two-chessboard domains; under-equilibrated). Added F1: same points, 20000 equilibration sweeps, chessboard and random starts.
- Added boundary scans F2-F4 (rho = 1/4, 3/8, 1/2; g brackets from C1; L = 12, 16, 24; Binder crossing) to state the boundary g_N(rho).
- Classification fix: a peak at the smallest k (one component 2pi/L) growing with L is classed "clumped (period 1)", as PREREG's clumping class intends; C1's g=8, rho=1/8 row was mislabelled "other" by the first script.
- 21:56Z: C2 at rho=1/2, g=1e-5, L=16 random start shows the same frozen domains; added F5 (contents (3,1,2), (12,1,2), board and random starts, 20000 equilibration sweeps).
