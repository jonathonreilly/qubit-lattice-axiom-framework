---
claim_id: the_3450_far_wall_term_keeps_a_unique_gapped_wall_mode_chain_state_to_l_18_but_its_gap_falls_from_six_to_eight_modes_per_flavour_bounded_theorem_note_2026-10-24
claim_type: bounded_theorem
claim_scope: "Finite diagnostics on exactly the far-wall-smg wall-mode chain (far-wall modes |k| < pi/2, antiperiodic, the two forced 6-fermion bond terms l1 = (1,-2,1,2), l2 = (2,1,-2,1), one coupling g, sectors (Q_A, Q_B, P)) at L = 8, 10, 12, 14, 16, 18, i.e. n = 4, 4, 6, 6, 8, 8 modes per flavour; L = 16, 18 sectors have 2.1-2.3e6 states and were computed by sparse Lanczos on a separate machine (results committed as data). At g = 200 the ground state is unique, neutral and at P = 0 for every L = 12..18; the neutral gap is 4.03, 3.36, 1.60, 1.44 and the single-particle gap 4.84, 4.31, 1.54, 1.42 (free 2 sin(pi/L), sin(pi/L)). Within fixed n the gap tracks 1/L (gap*L = 48.4, 47.0 at n = 6; 25.6, 26.0 at n = 8); at equal window fraction n/L it falls by 0.40 (12 -> 16) and 0.43 (14 -> 18); at g = 1000 by 0.32 (12 -> 16). A fit gap = D_inf + c/L gives D_inf = -4.4 with residual 0.42, so the data do not support a finite large-L gap of that form; this is a trend over two mode numbers, not a limit. g = 5 is free-like (gap = 2 sin(pi/L) to 0.1%); g = 40 sits in the small-gap crossing region (0.06-0.11). Pre-set classification: INCONCLUSIVE (persistence ratio 0.36 < 0.5; closing criterion not met). Not covered: n = 10 (L = 20, 3.5e8 states per sector), the slab with the bulk, a mode-number-breaking far-wall term, 3+1D."
upstream_dependencies:
  - the_fewest_change_symmetric_far_wall_term_is_forced_and_gaps_the_3450_mirror_in_a_wall_mode_chain_while_the_flux_pump_separates_anomalous_content_bounded_theorem_note_2026-10-23
  - the_forced_far_wall_term_has_a_unique_gapped_three_site_cell_state_but_a_strong_coupling_cell_only_moves_the_mirror_and_the_one_orbital_sixteen_site_has_only_two_spin10_singlets_bounded_theorem_note_2026-10-23
runner: scripts/the_3450_far_wall_term_keeps_a_unique_gapped_wall_mode_chain_state_to_l_18_but_its_gap_falls_from_six_to_eight_modes_per_flavour_2026_10_24.py
---

# The 3450 far-wall term keeps a unique gapped wall-mode-chain state to L = 18, but its gap falls from six to eight modes per flavour

Claim type: bounded_theorem (exact statements [T]; finite diagnostics [F]; recorded larger-L results [R] read
from mini_results.json). Runner: runner.py, TOTAL: PASS=12 FAIL=0, 4.2 s, 204 MB peak, 5.3 k characters, seeded,
AUDIT_TIMEOUT_SEC = 120; run under a unique filename. Axioms unchanged. No rule adopted.

## Question

far-wall-smg showed that the forced far-wall term gaps the 3450 mirror in a wall-mode chain at L = 12 (unique
symmetric ground state, neutral gap 4.03) but left persistence with L open: L = 8 is mode-capped and L = 16 was beyond
the laptop. Does the gap stay open as L grows?

## Method

- Model: identical to far-wall-smg section C (same dispersion, far-layer amplitude, bond-average and point-split forms,
  antiperiodic momenta, sectors). The engine (mini_chain.py) is a memory-lean rewrite. It differs in three ways:
  - one sector basis is built per momentum;
  - the interaction is stored once as a real CSR matrix and applied as O + O^T;
  - the operator products are applied as a tree, flavour 0 last (the same order as the original).
- A2 [T]: the interaction is real in the mode basis. Each factor carries the phase e^{i pi q/2L} times +-i per
  pair, and momentum conservation makes the product real; numerically the ratio |Im|/|c| is at most 3e-16.
- Validation:
  - A3: the runner rebuilds L = 12 live and reproduces 4.031 / 4.838.
  - B0: the mini engine agrees with the live runner to 1e-6.
  - The mini engine also reproduces every far-wall-smg L = 8 value, and the scratch L = 14 values 3.36 / 4.31 and
    16.8 / 23.2.
- Modes per flavour: n = 4 (L = 8, 10), 6 (12, 14), 8 (16, 18), 10 (20). So L = 12 -> 16 and 14 -> 18 compare equal
  window fractions n/L.
- Symmetry reductions, both checked and not assumed:
  - E(P) = E(-P) in the neutral sector. It is exact over all P at L = 12 and 14. At L = 16, E(P=30) = E(P=2) to 2e-13.
  - E(-3,-2,P) = E(3,2,P), checked at L = 8, 12 and 14.
  So at L = 16 and 18 the runs cover neutral P = 0..L and every Q = (3,2) sector.
- Compute: Mac mini (M4). Sector dimensions are 2.27e6 (L = 16) and 2.13e6 (L = 18), with 6.3e8 matrix entries.
  Peak RSS was 6.1 GB and the peak footprint 8.5 GB. Each sector took 3-7 min.

## Results

| L | n | g = 5 gap | g = 40 gap / sp | g = 200 gap / sp | g = 1000 gap / sp | gap*L (200) |
|---|---|---|---|---|---|---|
| 8 | 4 | - | 0.085 / 0.94 | 0.183 / 1.53 | - | 1.5 |
| 10 | 4 | 0.618 | 0.089 / 0.64 | 0.093 / 1.61 | 0.267 / 7.86 | 0.9 |
| 12 | 6 | 0.517 | 0.079 / 0.66 | 4.031 / 4.84 | 20.26 / 26.37 | 48.4 |
| 14 | 6 | 0.445 | 0.063 / 0.59 | 3.360 / 4.31 | 16.79 / 23.18 | 47.0 |
| 16 | 8 | 0.390 | 0.113 / 0.60 | 1.597 / 1.54 | 6.45 / NA | 25.6 |
| 18 | 8 | - | - | 1.444 / 1.42 | - | 26.0 |

Here "gap" is the neutral gap over all momentum sectors and "sp" is (E(3,2) + E(-3,-2))/2 - E0.

- R1 [R] Uniqueness at g = 200. For L = 12, 14, 16 and 18 the ground state is unique, neutral and at P = 0, and both
  gaps stay > 1, well above the free values (<= 0.52 and <= 0.26). No symmetry breaking or degeneracy is seen.
- R2 [R] The lowest neutral excitation for L >= 14 sits at P = 4 (k = 4 pi/L), not at P = 2: E(P=2) = 2.02 against
  E(P=4) = 1.60 and 1.44. The branch is non-monotone, so the softening is at finite momentum.
- R3 [R] Size dependence, at fixed n and at fixed window fraction:
  - At fixed n the gap tracks 1/L to 4%. This is how the mode-basis couplings change with L at fixed modes.
  - At equal window fraction the gap falls by 0.40 and 0.43 (g = 200) and by 0.32 (g = 1000).
- R4 [R] Coupling dependence:
  - L = 12 is linear in g between 200 and 1000 (gap/g = 0.0202). At L = 16, gap/g still decreases (0.0080 -> 0.0065).
    So larger n needs larger g to reach the strong-coupling regime, and even there the gap per unit coupling is smaller.
  - g = 5 is free-like at every L (gap / 2 sin(pi/L) = 0.999); this is the gapless reading.
  - g = 40 stays in the small-gap crossing region at all L.
- R5 [R] n = 4 (L = 8, 10) is mode-capped: a quasi-doublet at g = 200 with gap < 0.2. This reproduces far-wall-smg C4.

## Extrapolation

The fits run over L = 12..18 at g = 200: four sizes, but only two mode numbers.
- gap = D_inf + c/L gives D_inf = -4.4 and c = 103, with a maximum residual of 0.42. A negative D_inf is unphysical.
  The form fails, so these sizes give no positive estimate of a large-L gap.
- A power law gap ~ L^-p gives p = 2.8, faster than the 1/L of a gapless linear branch.
- Grouped by n, gap*L is about 48 at n = 6 and about 26 at n = 8. If the n-step repeated, the gap at fixed g would close.
  With two mode numbers this is a TREND, not a limit, and n = 10 (3.5e8 states per sector) is out of reach here.

## Pre-set criteria (criteria_pre_run.txt, fixed before any L > 12 run)

- PASS needed gap(18)/gap(12) >= 0.5 with a unique ground state and gaps > 1. Measured: 0.358, so NOT met.
- FAIL needed one of the following, and none occurred:
  - a gap < 0.3 at L = 16 or 18;
  - a degenerate ground state;
  - gap*L constant to 15% over 12..18 (the spread is 0.62).
- Classification: INCONCLUSIVE.
- Disclosure: the criteria did not anticipate a decline faster than 1/L that still stays above 0.3. That is what was
  found. It is reported as a falling trend, not reclassified.

## Answer

To L = 18 the forced term's strong-coupling state stays unique, neutral, P = 0 and gapped, with both gaps > 1. But the
gap does not look L-independent. It drops by about 0.4 at each equal-window comparison from n = 6 to n = 8, faster than
1/L, and the extrapolation does not support a finite large-L gap. Persistence is therefore NOT established. The trend
points toward closing at fixed g, though it is not decisive with two mode numbers.

One consistent reading is that the bond terms frustrate one another. smg-strong-coupling found that overlapping bond terms do not
commute and that the uniform open chain is frustrated. That fits a gap that weakens as more modes share each bond and
softens at finite momentum (R2). This reading is a hypothesis, not computed.

## Caveats carried forward

- Validity. Every strong-coupling gap (1.4 to 20) exceeds the bulk gap of 1; the closest is 1.44 at L = 18. In that
  regime the chain is a cutoff wall theory, not the slab.
- smg-strong-coupling: a frozen far layer only moves the mirror inward. A gapped far-layer product is not a gapped
  mirror in the slab.
- The real far-wall term must break mode number (the charge-4 Omega route). This chain is the mode-conserving proxy.
- The chain is a non-local momentum-window regulator. It also gaps 3451 (far-wall-smg E2), so it cannot see the anomaly.
  The flux pump does that.
- Literature (supplied, not computed): Zeng-Zhu-Wang-You 2022 (arXiv:2202.12355) find BKT-type gapping of 3-4-5-0 on a
  Chern-strip boundary. Zakharov et al. 2026 need a Luttinger helper interaction. A BKT-type gap is exponentially small
  near the transition, which fits strong finite-size drift. This is supplied, not tested here.

## Smuggling review

Supplied:
- the wall-mode projection (bulk dropped);
- the bond forms;
- g and L;
- the 3450 charges, inherited from far-wall-smg.

Forced (inherited):
- the two terms;
- the single coupling.

Nothing is fitted to measurement and no rule is proposed, so the anti-smuggling gate does not apply. The far-wall
clause proposed in far-wall-smg stays UNTESTED. This result weakens its support at the chain level.

## Not computed

- L = 20 (n = 10);
- L = 18 at g other than 200;
- L = 16 charged sectors at g = 5 and 1000;
- L = 16, g = 5 at P = 16. Lanczos stalled on near-degenerate free levels; the gap comes from the other sectors.

Files: criteria_pre_run.txt, runner.py, out.txt, mini_results.json (summary), mini_raw_jsonl.tgz (per-sector records),
mini_chain.py, analyze.py, queue2.sh, queue3.sh, swap.sh (the mini engine and job scripts).
