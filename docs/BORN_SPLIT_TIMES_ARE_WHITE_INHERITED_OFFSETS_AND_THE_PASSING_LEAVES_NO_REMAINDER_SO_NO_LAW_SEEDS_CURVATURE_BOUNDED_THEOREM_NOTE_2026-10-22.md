---
claim_id: born_split_times_are_white_inherited_offsets_and_the_passing_leaves_no_remainder_so_no_law_seeds_curvature_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the update law's split and passing (eight children; edges along parent edges take the parent's value minus s, other registers start as in the children's vacuum; the nearest unitary carrying the update's vacuum onto the children's vacuum and each excitation onto the children's lowest excitation of the same charges, flux and momentum; the trigger on the cube's 18-edge mean at 4s with each unsplit +x, +y, +z face neighbour's shared-face edges full) and the actuality law (fewest-change transport, records never conditioning the odds): (A) the clause's remainder is zero for every mode, edge registers included, so A_s = 0 and P_t = 0 at linear order; the raw passing before the clause is no small squeezing: in a 1D free-fermion toy it leaves 0.62 excitations per parent site, fidelity e^(-1.27 per site), and a white density structure factor (1/16 at Q -> 0); a mode carried by its configuration gets |beta|^2 = 9/16. (B) The quantile transport keeps each register's Born quantile, and value-minus-s keeps it through the passing, so split-time offsets are inherited, never redrawn (1/4 of a child's trigger edges inherited: 6 on even, 3 on odd children); the block-mean offset is stationary at sigma_r/sqrt18 over 40 generations, the field is white (coarse variance ~8^-j), and as a curvature seed it gives Delta^2 ~ (k l)^3, about 1e-99 at the pivot. The coupled trigger DAMPS the spread (x0.43 on a 32^3 lattice with shared edges; always waiting for the face would amplify x2.4). Split phases spread by 0.35 e-folds would need Gaussian register odds of sd >= 4.9 s steps, more than half the (4+Delta)s window; the pair vacuum, the one-step floor and the own-hop window vacuum give 0.0002-0.065 e-folds, leaving the ln2 sawtooth (modulation 0.94-0.96). (C) Record picks seed nothing through odds; read through actual occupations they carry the vacuum's own density correlator, S(Q) -> Q^2 on a gapped staggered sea, so n_s - 1 = +4. (D) A mode-resolving passing threshold keeps the sawtooth (0.34-0.77) and its power depends on the chosen threshold; even with a supplied 0.35 dephasing and the inflation-rule's order carriage, A_s needs the FITTED rung, n_s = 0.957 (-5.6 sigma ACT+DESI) and r = 0. Supplied: Delta = 1, s = 23 and 135, the three register-odds readings, Gaussian offsets, the 1D raw-passing toy, a 10^3 staggered sea with mass 0.5, the inflation-rule's N* = 46.8 and H l_c = 2.3e-13, its mode model and dephasing requirement."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/born_split_times_are_white_inherited_offsets_and_the_passing_leaves_no_remainder_so_no_law_seeds_curvature_2026_10_22.py
---

# Born split times are white inherited offsets and the passing leaves no remainder, so no law seeds curvature

Claim type: bounded_theorem. The candidate-law register has zero premise weight, and the axioms are unchanged.

## Where this starts

The inflation-rule note found a new wall, D1: the passing carries vacuum to vacuum, so it seeds no perturbation and A_s = 0. Synchronised splits under order carriage (IN-1) give an excluded ln2 sawtooth, and removing it needs split phases dephased by about 0.35 e-folds or more. The laws were estimated to give 0.07-0.10, but only through a supplied Poisson register model. The spectral-tilt note showed that a self-similar split-time cascade gives n_s = 1, and the record-clock-tilt note showed that a record clock gives no tilt. This note tests three candidate seeds that the laws might already contain:
- (a) the passing's quantum remainder;
- (b) Born randomness of split times, computed from the registers' own odds;
- (c) Born picks of new sites' first records.

The goal is near-scale-invariant curvature with A_s ~ 2.1e-9 and n_s ~ 0.965-0.974, from a rule in site, possibility, record and update terms only.

## A. The passing's remainder (candidate a)

**A1 [T].**
- A mode carried by its configuration through a split (M -> 8M, w -> w/2, so M w x4) gets |beta|^2 = ((2 - 1/2)/2)^2 = 9/16.
- The clause as written takes the unitary nearest the raw passing that carries the vacuum onto the children's vacuum and each excitation onto the children's lowest excitation with the same charges, flux and momentum. That unitary has remainder 0 for every mode by construction, edge registers included.

**A2 [D]. 1D free-fermion toy of the raw passing.** Each corner mode is shared evenly over two children, and the other modes start as in the children's vacuum (reduced state). For N_p = 16 to 128:
- fidelity with the children's vacuum is e^(-1.27 N_p);
- there are 0.618 excitations per parent site;
- the density structure factor tends to 1/16 as Q -> 0 (white), where the children's vacuum has S ~ Q/2pi.

So the nearest-unitary step is load-bearing, not a small correction. The register's own junction note already says a local passing that falls short lowers transmission rather than heating.

**A3 [T+E].** Candidate (a) therefore gives one of two things:
- nothing, with the clause as written: A_s = 0 and P_t = 0 at linear order;
- without the clause, white UV heating of O(1) quanta per site per split: Delta^2 ~ (k l)^3, n_s - 1 = +3, and (k l)^3 is about 1e-99 at the pivot (k l ~ H l_c e^-N*).

It never gives a small, scale-invariant squeezing.

## B. Born split times from the registers' own odds (candidate b)

**B1 [T]. Offsets are inherited.**
- On a register line, the fewest-change transport keeps the actual value at a fixed Born quantile u. On a translating packet the offset from the mean is constant (0.023 steps of binning drift over 37 steps).
- The passing's "value minus s" shifts the odds rigidly, so it keeps every quantile.
- So a split-time offset is inherited, never redrawn. Spectral-tilt's Poisson model redrew every step; the laws' transport does not.

**B2 [T]. Three readings of a register's odds.** The per-register spread is sigma_r = ln2 sigma_n / s e-folds.

| Reading | sigma_n | s = 23 | s = 135 |
|---|---|---|---|
| R0, one-step floor | 1/sqrt12 | 0.0087 | 0.0015 |
| R1, pair vacuum (each partner pair bonding, n binomial) | sqrt((4+Delta)s)/2 | 0.162 | 0.067 |
| R2, own-hop vacuum on the window | 0.1808 (4+Delta)s | 0.637 | 0.628 |

**B3 [T]. Inheritance geometry.** Of a child cube's 18 trigger edges (12 axis edges and the 6 even-corner face diagonals), the ones along parent edges number 6 on even children and 3 on odd ones, a mean of 4.5 (1/4). The rest start fresh.

**B4 [D]. No accumulation.**
- Over 40 generations of one lineage, the block-mean offset stays at sigma_r/sqrt18 (0.237 at generation 1, 0.231 at generation 40). The parent-child correlation is 1/4.
- A redraw-per-generation model random-walks (x6.3 over the same 40 generations).

**B5 [D]. The coupled trigger damps the spread.** The test lattice is 32^3 blocks with shared edges. A block splits when its own 18-edge mean reaches 4s and, for each UNSPLIT +x, +y, +z neighbour, the five shared-face edges are all full (the least fixed point of T = max(own, max_n min(T_n, F_n))).
- Coupled spread: 0.102 sigma_r, against 0.236 for the own mean alone (x0.43; mean delay 0.93 sigma_r). A neighbour that has already split lifts its condition, so late faces are skipped.
- A variant that always waits for the face would amplify the spread (x2.42).
- Coarse-grained over 2^j blocks, the variance falls as 8^-j: the field is white.

**B6 [D+E]. Dephasing is not supplied.**
- IN-3 needs split phases spread by about 0.35 e-folds or more (inflation-rule D3). The coupled spread is linear in sigma_r, so this needs Gaussian register odds with sd >= 4.94 s steps. That is more than half the 5s window (at Delta = 1), which no odds on the window reach.
- The readings give sigma_split = 0.0002-0.065 e-folds.
- With the inflation-rule's mode model, the ln2-periodic modulation is 0.94 (R2) and 0.96 (R1), with mean power 2.6 and 6.8 times Bunch-Davies. The sawtooth stays.

**B7 [T+E]. The offsets can dephase, but they never seed.** As a curvature seed the white offset field gives Delta^2 ~ (k l)^3, n_s - 1 = +3, negligible at the pivot. The Poisson cascade's n_s = 1 assumed redraws that the quantile transport does not make.

## C. Born picks of new sites' first records (candidate c)

**C1 [T+D].**
- Records never condition the odds, so a response that reads odds sees no record seed (exact).
- If a source read the recorded occupations instead, the Born picks would carry the vacuum's own density correlator. On a gapped staggered sea (10^3, mass 0.5), S(Q) -> Q^2 (local power 1.75 at the two smallest Q). So Delta^2 ~ Q^5 and n_s - 1 = +4.
- A gapless 1D sea gives S ~ Q.

## D. Seed rules against the gate

**D1 [D]. SE-2 (mode-resolving passing).** Proposed text: "the passing carries a mode vacuum to vacuum when the children's tick turns it by more than th per generation, and by its configuration otherwise." With synchronised splits, the power is 0.87, 0.96 and 1.84 times Bunch-Davies at th = 1, pi and 2pi, with ln2 modulation 0.34, 0.59 and 0.77. The power depends on the chosen threshold, and the sawtooth stays. SE-2 still needs dephasing, so it adds a clause and solves nothing.

**D2 [E]. Even with dephasing supplied.** Grant a supplied dephasing of 0.35 or more (IN-3), together with IN-1 order carriage. The seed is then Bunch-Davies times 1.2-1.3 (inflation-rule D3), and:
- A_s = R V/(24 pi^2 eps M_P^4), with the rung FITTED;
- n_s = 1 - 2/N* = 0.9573 (-1.8 sigma Planck, -5.6 sigma ACT+DESI); a constant dephasing adds no tilt;
- edge registers pass vacuum to vacuum, so r = 0.

## Rule text tested

> SE-1 (Born dephasing; a reading of CL-2 and the split, with no new text). "A block's split time is read from the actual values of its edge registers, each a Born quantile of its odds; the passing keeps the quantile of every edge along a parent edge, and fresh registers take fresh quantiles."

> SE-2 (mode-resolving passing; new CL-level text). "The passing carries a mode vacuum to vacuum when the children's tick turns it by more than th per generation, and carries its configuration and momentum otherwise."

## Anti-smuggling gate (owner 2026-10-22)

- SE-1:
  1. No number is chosen.
  2. No observed structure is named.
  3. It makes predictions it was not built for: offsets are white (n_s - 1 = +3 as a seed); the coupled trigger damps them; the ln2 modulation is 0.94-0.96. Those modulations are excluded by the Planck feature search (a few-percent bound, approximate).
  4. It bends no axiom.

  Result: FAILS on measurement.
- SE-2:
  1. The threshold th is chosen, and the amplitude depends on it.
  2. No observed structure is named.
  3. Its prediction, the sawtooth, is excluded.
  4. It is CL-level and bends no axiom.

  Result: FAILS.

No candidate seeds A_s ~ 2e-9 with n_s 0.965-0.974. The goal is not met, and nothing is adopted.

## What the measurement now demands (not claimed derived)

- A horizon-correlated seed. Every Born or record source the laws contain is local and kept (white). Only the modes themselves carry correlations at the horizon scale, and the vacuum clause removes their squeezing.
- A route that remains open (UNTESTED): smooth expansion inside a block. If the edge stretching between splits were not a pure dilation in cell units (the tied lapse makes it one), then a mode carried by its configuration would be pumped continuously, and no dephasing would be needed. That requires a rule under which the tick is not static in cell units between splits. This bends the dilation-gauge result of inflation-rule A2.
- A_s still needs the plateau height in Planck units from a rule for the fold rung, and n_s >= 0.965 needs N* > 57 or a non-exponential plateau.

## Smuggling review

Supplied:
- Delta = 1 (the AX-4 value, FITTED there);
- s = 23 and 135;
- the three register-odds readings and Gaussian offsets;
- the 1D raw-passing toy and its reduced-state reading of "start half filled as in the children's vacuum";
- the 10^3 staggered sea with mass 0.5;
- from the inflation-rule note: N* = 46.8, H l_c = 2.3e-13, the mode model (summed cell count) and the 0.35 dephasing requirement (approximate).

Forced, given those:
- the zero remainder of the clause and 9/16 for configuration carriage;
- the O(1) raw remainder;
- quantile inheritance and 1/4 inheritance;
- stationarity and whiteness;
- damping by the coupled trigger;
- the impossibility of 0.35 dephasing on the window for Gaussian odds;
- the record correlator ~Q^2.

Not computed:
- the edge register's odds under the CL-3 response during stretching (the true sigma_n);
- held edges and positive-volume restrictions in the coupled trigger;
- the correlated pair of child edges along one parent edge, in the lattice test;
- non-Gaussian odds;
- the 3D raw passing;
- the second-order tensor readout.

## Dependencies

- Used:
  - inflation-rule (#10000): D1-D3, the mode model, N*, IN-1;
  - spectral-tilt: cascade theorem, Poisson model, trigger edges;
  - record-clock-tilt: records never condition the odds; quantile register transport;
  - the register's split, passing and junction text (CANDIDATE_LAWS_v3).
- Narrowed:
  - spectral-tilt B (its Poisson redraws are not the laws' transport; the laws make split-time offsets white);
  - inflation-rule D4 (the laws' dephasing is 0.0002-0.065, not 0.07-0.10, and the coupled trigger damps it).

## How to run

python3 scripts/born_split_times_are_white_inherited_offsets_and_the_passing_leaves_no_remainder_so_no_law_seeds_curvature_2026_10_22.py

AUDIT_TIMEOUT_SEC = 120. It takes about 3 s, peaks at about 175 MB, prints 5693 characters and ends with TOTAL: PASS=14 FAIL=0. It was checked through scripts/runner_cache.execute_runner from a temporary origin/main worktree (status ok, exit 0).
