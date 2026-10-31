# lg55_1 — criteria (written BEFORE the script; LARGE55.md §2.1, Theorem DENSE (iv))

Author: claude-opus-5-5 (LARGE55 worker). Written 2026-10-29 (UTC, before lg55_1_dense.py exists).

## What is computed (exact rational arithmetic only; Python fractions; no floats in any verdict)
For N in {2, 3, 4, 5, 6, 8, 10} and eps = k/1000, k = 1..682:
- A_N(eps) := (24/N)(1 + eps^2)^2 + 6 eps.
- Feasibility of the DENSE construction: eps + eps^3 <= 1 (checked exactly for every grid point used).
- beta_up(N) := 11 N^2 / (12 * (333/106)^2)  (an UPPER bound on beta_0^std = 11N^2/(12 pi^2), since pi > 333/106).
- beta_lo(N) := 11 N^2 / (12 * (355/113)^2) (a LOWER bound, since pi < 355/113).
- Robustness factor: also with beta_up * 11/10 (a stand-in for beta_+ = beta_0 + C_rho gamma^2/log L up to 10%).
- Condition C(eps, beta): eps^2 * A_N(eps) * beta < 4   (exact rational comparison).
- eps_lo(N, beta) := largest grid eps such that C holds at EVERY grid point <= eps (monotone prefix).
- eps_hi(N) := smallest grid eps at which C FAILS with beta_lo (so the true threshold for beta_0^std lies in
  [eps_lo(N, beta_up), eps_hi(N)] up to one grid step).
- Monotonicity: eps^2 A_N(eps) strictly increasing on the grid (checked exactly).

## Pre-registered PASS/FAIL (predictions from the hand estimate in LARGE55 §2.1, written before running)
- P1: eps_lo(2, beta_up) in [0.600, 0.640].   PASS iff inside.
- P2: eps_lo(3, beta_up) in [0.500, 0.560].   PASS iff inside.
- P3: monotonicity holds for every N.          PASS iff it holds.
- P4: eps_lo(N, beta_up) is non-increasing in N over the list.  PASS iff it holds.
- Control C1 (must FAIL the condition; shows the gate can fail): C(0.682, beta_lo(2)) is FALSE.  PASS iff C is false there.
- Control C2 (must hold): C(1/1000, beta_up(10)) is TRUE.  PASS iff true.
If P1 or P2 fails, LARGE55 §2.1's quoted numbers are wrong and are corrected by an appended erratum (the theorem itself is
unaffected: it is stated for every eps with eps^2 A_N(eps) beta_* < 4).

## Report-only lines (not verdicts)
- eps_lo(N, 1.1*beta_up) for every N.
- Whether the lane's eps_1 = 67/10^41 satisfies C for every N in the list (trivially expected; reported, not a gate).

## Limits
Wall-clock < 60 s, memory < 100 MB. Exit code 0 and empty stderr required for any PASS to count.
