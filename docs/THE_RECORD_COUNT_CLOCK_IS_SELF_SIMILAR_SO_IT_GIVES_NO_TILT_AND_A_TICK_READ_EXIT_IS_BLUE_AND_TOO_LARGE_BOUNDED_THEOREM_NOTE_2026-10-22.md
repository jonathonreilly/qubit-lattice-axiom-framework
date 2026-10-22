---
claim_id: the_record_count_clock_is_self_similar_so_it_gives_no_tilt_and_a_tick_read_exit_is_blue_and_too_large_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the actuality law's records (one permanent record per matter site per half-tick, a new site's first record at the half-tick after it appears, records never conditioning the odds, a past record read only through a pointer) and the update law's split (eight children per block, children's edges along parent edges at the parent's value minus s, tied lapse): (A) exact counting: a block has unrecorded sites only on its 7/8 new sites, and only for the one half-tick after its split, so the unrecorded share per generation is (7/8)/T_gen, the same at every level; the share of a region's records laid in the latest generation is 8^l / sum_j 8^j, which tends to 7/8 with per-split ratio 1 + O(8^-l), a start transient and not a constant factor; the tied lapse gives 1/(2 k l_c H) ticks per generation, equal at every level of a de Sitter cascade; records never condition the odds, so no vacuum-energy share belongs to unrecorded modes; a pointer's occupation odds never change, so a pointer holds no tick count. (B) With a supplied exit that reads ticks, an exact tight-binding edge register with the fewest-change (quantile) transport gives a Born split-time spread delta N = ln2 sigma_T/T_gen per level that does not depend on H; its minimum over Gaussian packets is 0.023 to 0.22 e-folds for s = 23 to 113 and register speed x = v/2J = 0.5 to 0.9999, at least 600 times the 3.8e-5 that A_s needs; in de Sitter the levels repeat, so lam = 1; when H falls the register slows and spreads more, so n_s - 1 = p eps with p = +1.0 to +5.4 (blue). (C) The record clock adds no tensor channel; r is set by a supplied plateau H. Supplied model, finite diagnostic: the octree with S, T_gen and a Born spread; an 8-mode ring; a random controlled unitary; a one-dimensional tight-binding register with J = 1, Gaussian packets and quantile transport; eps; the plateau H. Measured numbers enter only the estimates."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/the_record_count_clock_is_self_similar_so_it_gives_no_tilt_and_a_tick_read_exit_is_blue_and_too_large_2026_10_22.py
---

# The record-count clock is self-similar, so it gives no tilt, and a tick-read exit is blue and too large

Claim type: bounded_theorem.
Primary runner: `scripts/the_record_count_clock_is_self_similar_so_it_gives_no_tilt_and_a_tick_read_exit_is_blue_and_too_large_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. The split-time cascade note shows that the update law's split cascade alone is exactly flat (n_s = 1) and seedless at linear order. It also shows that split-time spread is a pure time relabelling (zeta = 0) unless some rule component reads ticks rather than local edge length. The actuality law (CL-2) lays one permanent record per matter site per half-tick, so records count ticks. This note asks whether a record-count clock that the laws already imply makes split-time spread physical and tilted. The measured tilt needs lam = 2^(n_s - 1) = 0.976 (Planck) to 0.982 (ACT with DESI) per split, r < 0.036 and A_s = 2.1e-9. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

A. Record arithmetic through splits.

1. Exact. Every matter site gets one record per half-tick. At a split the eight children hold 8S sites; 7S of them are new, and each new site gets its first record at the next half-tick. So a block is unrecorded only on 7/8 of its sites, for one half-tick, and the unrecorded share per generation is (7/8)/T_gen. It is the same at every level. A seeded octree (S = 8 sites per block, T_gen = 40 half-ticks, Born spread sd 4, six generations, 262144 blocks) gives the per-generation ratios 0.997, 1.003, 0.995 and 1.002. The unrecorded fraction does not fall by any factor per split.
2. Exact. In a comoving region the share of all records laid in the latest generation is f_l = 8^l / sum_{j<=l} 8^j, which tends to 7/8. The per-split ratio f_l/f_(l-1) is 0.889, 0.9863, 0.9983, 0.9998: 1 + O(8^-l). Its log2 passes the measured -0.035 between levels 1 and 2 and is -0.020 at level 2, but it falls by 8 per level. The running is +0.22 per ln k between levels 1 and 2 and +0.025 between levels 2 and 3, against the measured -0.0045 +- 0.0067. The tilt is gone by level 4 (-0.0003), while the CMB spans about ten octaves. This is a start transient pinned to the first split, not a constant lam.
3. Exact. Records never condition the odds (CL-2: the joint update is their only change). The vacuum energy is a function of the odds, so recorded and unrecorded modes carry it in the same way: on an 8-mode ring E0 = -4.8284 before and after a record. No "unrecorded share" of vacuum energy exists to fall by lam. A collapse reading, which the law excludes, would remove all of it in one half-tick (factor 0, as heat), not 0.98.
4. Exact. The tied lapse makes the proper time per tick proportional to the cube's proper length. A generation runs from l_c to 2 l_c, so it takes 1/(2 k l_c H) ticks, the same at every level of a de Sitter cascade. The records per block per generation are a fixed number: the record clock is self-similar.
5. Exact. A pointer is a mode the update acts on as a control only, so its occupation odds never change (spread 3e-15 over 50 half-ticks of a random controlled unitary). A pointer holds no tick count. The registers that are read and advance monotonically are the edge registers, which are the local length. A clock built from what the laws read is therefore a length clock, and the split-time cascade note's D1 gives zeta = 0.

B. A supplied exit that reads ticks.

1. Diagnostic. Suppose an exit law read the record count (ticks since birth) instead of length. Then the Born spread of an edge register's actual value becomes a split-time spread: delta N = ln2 sigma_T/T_gen per level. Converting the length spread to e-folds through the mean rate cancels H. The model is an exact tight-binding register (J = 1, packet speed x = v/2J) with the fewest-change transport on a line (the quantile coupling: the actual value is the u-quantile of the odds, and u is the Born variable). Minimised over Gaussian packet widths, the per-level spread is:

   | s | x | min delta N |
   |---|---|---|
   | 23 | 0.5 | 0.217 |
   | 23 | 0.99 | 0.077 |
   | 64 | 0.5 | 0.119 |
   | 64 | 0.99 | 0.040 |
   | 113 | 0.5 | 0.090 |
   | 113 | 0.99 | 0.029 |
   | 113 | 0.9999 | 0.023 |

   A_s needs 3.8e-5, so the spread is at least about 600 times too large in rms (A_s of at least 8e-4).
2. Diagnostic. When H falls, as the null energy condition requires, the register must move slower each split (x falls by eps ln2), and a slower packet spreads more over the generation. So lam = (dN_(l+1)/dN_l)^2 > 1, giving n_s - 1 = p eps with p = +1.42 (s = 64, x = 0.5), +5.43 (s = 64, x = 0.9) and +1.01 (s = 23, x = 0.5). The tilt is blue, the wrong sign.
3. In de Sitter every level repeats the same register problem: children start at the parent's value minus s, with the same x and the same ticks per generation (A4). A tick-read exit therefore gives lam = 1 exactly, so n_s = 1.

C. Tensors. The record clock adds no tensor channel; the trigger reads tensors at second order only (split-time cascade note A3). P_t = 2(H/M_p)^2/pi^2 needs a supplied plateau H, and the record-clock A_s does not depend on H, so the model leaves r free. r < 0.036 needs H/M_p < 1.9e-5. The laws' only de Sitter phase is today's, which gives r of about 0.

## Derivation

A1 and A2 are counting with the CL-2 record clause and the eight-child split. A2 is the geometric sum 8^l / ((8^(l+1) - 1)/7). A3 holds because CL-2 records leave the odds unchanged, and the energy is tr(h C) with C fixed by the odds. For A4, proper time per tick is sin(eps0)/sqrt 3 times the proper cube length, which is l_c e^(H t) between splits. Integrating dt/(k l_c e^(H t)) over one doubling gives 1/(2 k l_c H). A5: the control's diagonal block commutes with a controlled unitary.

For B1, write T_gen = s/v ticks for one generation. The quantile first-passage time T(u) through s steps has spread sigma_T, and one generation is ln2 e-folds, so delta N = ln2 sigma_T/T_gen. Both are in ticks, so H cancels. The spread has a minimum over packet widths because a narrow packet disperses (the dispersion is v'(k0) = 2J sqrt(1 - x^2), and the third-order term remains near x = 1). On a discrete register this minimum is several steps, not a fraction of a step. For B2, the minimum spread grows as x falls (v' grows and T_gen grows), and NEC makes x non-increasing, so lam >= 1.

## Checks

The runner prints 10 checks: A1 exact counting with a seeded finite octree; A2 exact (fractions); A3 exact (an 8-mode ring); A4 exact (sympy); A5 exact (a random controlled unitary); B1 and B2 finite diagnostics; B3 exact under self-similarity; C1 estimate arithmetic; E1 estimate arithmetic.

## Estimates against measurement

- Index. Every record-clock channel gives lam = 1 at a constant expansion rate, so n_s = 1, 8.4 sigma from Planck. The record-share start transient gives a red tilt at levels 1 and 2 but runs by 8 per level: its running is 4.4 sigma (levels 2 to 3) to 33 sigma (levels 1 to 2) from the measured value, and it would put the CMB within two levels of the first split. A tick-read exit is blue whenever H falls.
- Amplitude. A tick-read exit gives A_s >= 8e-4 against 2.1e-9. The laws' own channel (a length clock) gives zero at linear order.
- Tensors. r = 2(H/M_p)^2/(pi^2 A_s) with a supplied H; with the record-clock A_s, r <= 1e-7 at r-allowed H.
- Numerology. Of five simple forms built from 8, 7, ln 2 and s, three land in [0.976, 0.982]: 1 - 1/s for s in [42, 55], and 1 - ln2/s and 2^(-1/s) for s in [29, 38]. Each needs s picked from its supplied range 23-113, and none follows from a law, since nothing in the rules makes a record share or a register number change from one split to the next.

## Boundary

Supplied: the octree, with S = 8 sites per block, T_gen = 40 half-ticks and a Born spread of sd 4 (A1); the 8-mode ring (A3); a random controlled unitary (A5); the one-dimensional tight-binding register with J = 1, Gaussian packets and quantile transport as the fewest-change transport on a line (B); eps = 0.02 (B2); a plateau H (C).

Forced, given those: the 7/8 one-half-tick unrecorded share; the 8^-l transient; equal ticks per generation in de Sitter; records carry no vacuum-energy share; pointers carry no count; delta N = ln2 sigma_T/T_gen independent of H; lam = 1 in de Sitter; the blue sign under NEC in the scanned register model.

Not computed: the three-dimensional register with all 18 edges and the coupled trigger; quantum edge dynamics beyond free tight-binding (CL-3 response); non-Gaussian or squeezed packets (a squeezed register still disperses, but this is not scanned); any exit law, since none is law text.

Not claimed: that records cannot tilt the spectrum under some other reading. The tested candidate clause was "the plateau ends in a block when its sites' record count since birth reaches a fixed number". It is not adopted: it is a new reading clause (CL-2 lets no law read a record count), it gives n_s = 1 in de Sitter and a blue tilt when H falls, and it overshoots A_s by 4e5 in power.

## Dependencies

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [candidate_laws](CANDIDATE_LAWS.md)
- Used: the split-time cascade note (n_s - 1 = log2 lam, zeta = 0 for length-read rules, trigger reads tensors at second order); the record and clock split-trigger note (#9949: a record-count trigger is a fixed schedule); split-creation B5 (the split time is Born-spread on the edges); the cosmology cascade (3.81e-5 per-level spread).
- Narrowed: the owner instinct that ticks and records are the clock. Records do count ticks, but no law reads the count, and reading it gives no red tilt.

## How to run

python3 scripts/the_record_count_clock_is_self_similar_so_it_gives_no_tilt_and_a_tick_read_exit_is_blue_and_too_large_2026_10_22.py

AUDIT_TIMEOUT_SEC = 120; about 3 s, peak about 200 MB; ends with TOTAL: PASS=10 FAIL=0.
