**Provenance:** the worker's final message, saved verbatim by the supervisor.

I read this as **LOCK-MIXED**. The repo's main ordering rule for records, the record gas, gives a period-2 chessboard in one corner of its parameter range and a liquid or a uniform state everywhere else. These results are from one agent of the same family, not refereed, finished 22:00Z.

## Plain words

The record gas is the only landed rule family that actually orders matter at densities 1/8–1/2 on Z³. It is the static law with vacancies: blocks 39, 40, 81, 117, and the follow-up notes on uniqueness and the neutral scale. Its one free number is the bond scale g, the weight of a bond between two records relative to a bond with an empty end.

- **g below 1 (records repel):** records form the chessboard, which is period 2. They do so only when they are dense enough and the repulsion is strong enough.
- **g of 1 or more (neutral or attracting):** records stay a liquid or gather into uniform clumps, which is period 1. They never form a chessboard.
- **Odd and other even periods:** never seen, at any point.
- **Density 1/8:** liquid at every g up to 2. At g = 4 and 8 the records clump instead, still with no crystal.
- **Main's own preferred value:** the neutral scale g = 1 (block 40's proposal) sits on the safe side, and so does the whole range where the law with vacancies is reflection positive (g ≥ 1). The chessboard needs a repulsion that block 40's T4 says the rule itself does not supply.

## The boundary

The chessboard forms only when g is below a threshold g_N that depends on density (checked by Monte Carlo):

| density ρ | g_N(ρ) (Binder crossing, L = 12/16/24) |
|---|---|
| 1/2 | 0.41–0.42. The sc Ising comparator e^{−4K_c} = 0.412 agrees. |
| 3/8 | 0.36–0.37 |
| 1/4 | 0.16–0.18 |
| 0.21 ± 0.005 | g_N → 0: the hard-core limit |
| 1/8 | no chessboard at any g |

## Results by family

**Static law with vacancies / record gas.**
- **Proved on main:**
  - Chessboard for g ≤ 9/62500 at half filling, grand canonical (block 117 note, lines 151–156 and 162).
  - A unique state for 25/49 < g < 49/25 with no contents, at every activity. That means translation-invariant, so no lock at any density (uniqueness note, `...WHERE_MOVING_RECORDS_CANNOT_CLUMP...49_OVER_25...md`:30–32).
  - Reflection positivity iff g ≥ 1 (block 39 note:27).
  - At the neutral scale, no order at low density, and uniform alignment at high density with large β (2026-09-26 note:25–30).
- **Checked (Monte Carlo, my runs):**
  - **No contents:**
    - Period 2 at (π,π,π) whenever g < g_N(ρ). Binder U is 0.66–0.667 and S(Q)/V is flat from L = 16 to 24.
    - Liquid elsewhere for g ≤ 2: S/V falls like 1/V, a ratio of about 0.30 against 0.296 expected.
    - Clumped at g = 4 and 8 for ρ ≥ 1/4, and at g = 8 for ρ = 1/8. At ρ = 1/8, g = 4 sits near the clumping edge.
  - **Contents (3,1,2):** chessboard at g = 10⁻⁵ (ρ = 1/4, 1/2) and g = 0.25 (ρ = 1/2). Liquid at g = 1. Clumped at g = 4.
  - **Contents (12,1,2):** the same at small g. At g = 1 and 4 the records form clusters with aligned contents (uniform alignment up to 0.91). The staggered content order is zero at every point.
- Of 354 runs, every peak that grows with L sits at (π,π,π) or at the smallest k. The five exceptions are random starts that froze into domains; they are resolved under Deviations.

**Quantum walkers with one record per site (blocks 121, 125, 130, 137, 141–143).**
- On a ring the records are proved to be one twisted spinless band, i.e. a free sea, liquid, no lock (block 130 note:40, 84–90).
- On Z³ the many-record ground state is not on main and was not computed. Small exact diagonalisation cannot tell a lock from a liquid. This family is **OPEN** in 3D.

**Signed hopping plus density repulsion (`RECORD_CONSERVING_INTERACTION_KEEPS_THE_STAGGERED_SECTOR...2026-09-03.md`:121–125).** This covers finite cubes at half filling only. The weight on the two chessboard (Néel) patterns rises with repulsion. That leans toward period 2 at half filling, but main makes no infinite-volume or other-density statement, and I ran nothing on it.

**Block 133.** This is a statement about one walker's rest state under a supplied mass term, not a rule that orders many records, so it is outside this classification.

## A point GEN-2 should check

The chessboard keeps only the translations that land on same-colour sites. Those reach only (π,π,π) among the corners (checked). So the chessboard folds that one corner onto Γ and pairs up the other six. It does **not** fold all 8 corners onto Γ.

GEN-2's c6 tested simple-cubic crystals of period c (`GEN2/scripts/gen2_symm.py`:47–51). Whether the chessboard actually removes X2′'s index protection depends on X2′'s index at (π,π,π). I did not compute that; it belongs to GEN-2.

## Scope

- **Rules:** the record gas exactly as landed. Weight is the product over recorded bonds of g·M(s,s′), with M = 6ω/(p+q+4r) and contents summed uniformly. No contents, (3,1,2) and (12,1,2).
- **Ensemble:** fixed record number (block 39 T1: motion keeps N).
- **Method:** Metropolis with nonlocal record–vacancy swaps plus content redraws. It samples the static law; it is not the motion rule's dynamics.
- **Sizes:** periodic L³ with L = 8, 12, 16, 24. L = 12 and 24 allow periods 2, 3, 4 and 6.
- **Sweeps:** 2,000 to settle and 4,000 measured, sampling every 5 sweeps. The follow-ups used 20,000 to settle.
- **Errors:** statistical only, from 10 block means. Finite-size effects are judged only from the L trends. The boundary values are brackets, not fitted critical points.
- **Validation (checked):** exact enumeration on the 4³ torus with N = 4 matches the MC at g = 0, 0.3 and 3. The contents check P(bond) gives 0.0502 against 0.05 exact.
- **Comparator:** Yamagata 1995 gives the hard-core critical activity on sc as z_c = 1.0588 ([arXiv cond-mat/9409093](https://arxiv.org/pdf/cond-mat/9409093)). My density estimate of 0.21 is my own measurement; that paper does not give one.

## Deviations (logged as dated follow-ups in PREREG.md)

1. **Frozen random starts at near-hard-core half filling.** At ρ = 1/2 with g ≤ 0.1, random starts froze into two chessboard domains: L = 24 at g = 0.02 and 0.1, and L = 16 at g = 10⁻⁵ with contents. Chessboard starts with 20,000 settling sweeps give S(Q)/V = 0.250 and 0.249, and at g = 0.1 the random start reaches 0.249 too. Block 117 proves order at g ≤ 9/62500 anyway.
2. **Classifier fix.** The first script labelled clumping at the smallest k as "other". It is now classed as clumped (period 1), as the PREREG intended.
3. **Boundary scans added.** I added boundary scans F2–F4 after the first grid read out.

## Files

All in `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/campaign/LOCK1/`:
- `PREREG.md`
- `scripts/lock_mc.py`, `scripts/validate.py`, `scripts/validate2.py`, `scripts/classify.py`, `scripts/archive.py`
- `scripts/lock1_archive.npz`: 354 run summaries and 280 S(k) arrays
- `runs/*.out`, `runs/*.jsonl`

Peak memory was 147 MB, one process at a time. None of my processes are still running, and QMC-1b was not touched.