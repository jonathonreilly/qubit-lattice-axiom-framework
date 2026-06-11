# The U(1)/Det Sector of the Bi-Orbit-Quotient Step Law: the Quotient's Invariant Marginal Is Non-Stationary, and It Decomposes into the Deterministic Dynamical Phase plus Quasi-Centered Record Noise

**Date:** 2026-06-10
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope note:** retire-mode; the owner-directed strike on PR #3522's named open object.
**Script:** `scripts/frontier_u1_det_sector_bi_orbit_quotient_step_law_2026_06_10.py`
**Cache:** `logs/runner-cache/frontier_u1_det_sector_bi_orbit_quotient_step_law_2026_06_10.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=21 FAIL=0` — exact,
deterministic, no MC (Born-weighted outcome tree to depth 11; **six seeds, including the
owner-found adversarial ones** — the draft's three-seed `< 0.25` median gate was
seed-tuned (seed 4242 gives 0.353; seeds 99/7 carry near-π stray maxima ~2.9/~2.0), and
the gates now assert only seed-robust content; #3507's guards inherited).

## The object, identified exactly

The bi-invariant split note
([`UNRAVELED_STEP_LAW_BI_INVARIANT_QUASI_STATIONARITY_SPLIT_BOUNDED_THEOREM_NOTE_2026-06-10.md`](UNRAVELED_STEP_LAW_BI_INVARIANT_QUASI_STATIONARITY_SPLIT_BOUNDED_THEOREM_NOTE_2026-06-10.md))
named the **bi-orbit-quotient step law** as its open object. **(D1)** For
*unitary* increments the quotient under `SU(3)×SU(3)` is **exactly the determinant
phase**: `det(V·dU·W†) = det dU` (invariance), and any unitary with the same det is
reachable by `(V,W)` (constructive exhibit in-runner) — the non-det content of a single
increment is entirely bi-gauge. The det increment is also **exactly gauge-invariant**
(`det(g_x dU g_y†) = det dU`) — it is the U(1)/center thread #3491 left named-and-open,
now probed as the quotient law's invariant marginal.

## The findings (exact — runner `PASS=21 FAIL=0`)

**(D2) The raw law is non-stationary — the honest refutation.** The Born-weighted mean
phase increment `E[arg]` **wanders O(1)** across the horizon at all six seeds. So the
bi-orbit-quotient **law** is *not* quasi-stationary, even though the moment *spectra*
freeze (#3522): **the Block-26 panel-forced scope — "spectra of the mean, not the law" —
was load-bearing**, and the bi-frame localization does not extend to all bi-invariant
content. The natural extrapolation of the split is refuted.

**(D3) The baseline decomposition — the constructive result, in its seed-robust form.**
Centered on the **computable record-free dynamical phase**, the claim that survives seed
choice is the **raw/centered median-drift ratio: > 2× at all six seeds** (observed
3.2×–18.1× — scoped to these six seeds: an independent 86-seed stress found ~1/86 below
2×, so the ratio claim is *typical*, not universal) — the wandering is
**baseline-carried**. The absolute medians are
**seed-dependent**: cross-seed spread `[0.048, 0.353]` (the draft's `< 0.25` was a
seed-tuned numeral — **owner-caught**; the gate is now the disclosed spread with margin),
and the stray maxima reach `~2.9` — near-π rows sitting at **small-singular-value
polar-readout rows near the rank-guard edge** (`ε` is constant, so these are geometry-
driven phase flips, not measurement-strength effects) — disclosed, not hidden. **The det sector's non-stationarity is deterministic-phase-driven, not
noise-driven; the residual noise magnitude is seed-dependent.**

**(D4) The k² relation has no teeth at high concentration — methodological control.**
The wrapped-Gaussian moment relation `|ch_k| = |ch_1|^{k²}` is **variance-automatic** for
*any* concentrated circular law — exhibited with a manifestly non-Gaussian two-atom toy
matching it to ~1% — so the scratch's striking high-concentration matches do **not**
establish U(1)-CLT structure. Genuine teeth exist only at spread (the same toy violates
the relation grossly there, as do the tree's spread-regime rows). **No U(1)-CLT is
claimed**; the question is now correctly posed on the **centered fluctuation** — the
named next object.

## What this sharpens, and what it does not deliver

- **Residual 1 (#3507), sharpened twice:** its reach *includes* bi-invariant content (D2 —
  not just bi-frame junk), and it *decomposes* (D3 — deterministic baseline + small
  quasi-centered noise). The follow-on question is no longer "is the law stationary?"
  but "is the **centered record-noise law** stationary/central?" — strictly sharper.
- **No CLT premise is delivered**; #3507's four residuals stand. The U(1) factor of
  `U_eff` is **not** identified with a physical gauge field (identification gate, as
  throughout).
- Finite horizon; six seeds (adversarial ones included); one `(ε,τ)` instance; all
  numbers seed/instance-labeled.
  Conditionality inherited from
  [`UNRAVELED_RECORD_TRAJECTORIES_SUPPLY_NONDEGENERATE_STEP_DISTRIBUTION_BOUNDED_THEOREM_NOTE_2026-06-10.md`](UNRAVELED_RECORD_TRAJECTORIES_SUPPLY_NONDEGENERATE_STEP_DISTRIBUTION_BOUNDED_THEOREM_NOTE_2026-06-10.md)
  and
  [`UNRAVELED_STEP_LAW_BI_INVARIANT_QUASI_STATIONARITY_SPLIT_BOUNDED_THEOREM_NOTE_2026-06-10.md`](UNRAVELED_STEP_LAW_BI_INVARIANT_QUASI_STATIONARITY_SPLIT_BOUNDED_THEOREM_NOTE_2026-06-10.md):
  the Born derived-chain cap (the assembly note
  [`BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md`](BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md)
  is **unaudited** on
  the live ledger — self-verified at landing; two prior panels reported conflicting
  statuses, demonstrating the volatility); named instruments with supplied `ε`;
  supplied `C³` carrier; named hopping; guarded full-rank domain. Discrete-time
  throughout (retained R1 boundaries untouched). No new axiom, primitive, measure, or
  weight; `r` untouched. The audit lane grades.

## No-Go Discipline Gate (for the negative legs)

Negative legs shipped here: the raw determinant law is not quasi-stationary
on the tested finite-horizon, six-seed object; high-concentration `k^2`
matches do not establish a U(1)-CLT premise.

- **N1 alternative routes:** (1) read only moment spectra — fails to control
  the law by D2; (2) center by the record-free deterministic phase — sharpens
  the residual but does not rescue raw stationarity by D3; (3) change seeds —
  six seeds, including adversarial seeds, all pass D2, but universality beyond
  them is not claimed; (4) use the `k^2` relation as CLT evidence — blocked by
  the two-atom control in D4; (5) identify the U(1) factor with a physical
  gauge field — explicitly out of scope; (6) change horizon, `ε`, `τ`, carrier,
  or hopping — named open, not closed here.
- **N2 wall independence:** quotient identification (D1), raw-law drift (D2),
  baseline centering (D3), and CLT-control (D4) are separate checks; closing
  one does not imply the others.
- **N3 hidden-wall scan:** Born weights, supplied instruments, supplied
  `C³` carrier, hopping, rank guard, horizon, and seeds are declared inputs.
  No physical gauge-field identification or new measure is used.
- **N4 residual matching:** the residual matched is the split note's named
  bi-orbit-quotient step law object and the nondegenerate-step-distribution
  note's residual 1. This note refines those residuals; it does not close the
  centered fluctuation law.
- **N5 rhetoric audit:** "not quasi-stationary" means the raw finite-horizon
  determinant law at the six tested seeds. It is not a universal all-seed,
  all-parameter, all-horizon no-go.
- **N6 partial-closure scan:** centering by the deterministic phase is the
  partial closure; it produces the named next object, the centered
  fluctuation law.
- **N7 steelman:** a deeper or different-parameter tree might yield a
  stationary centered noise law or a CLT after the deterministic phase is
  removed. That is not refuted here; it is the next target.
- **N8 cross-cycle echo:** this mirrors #3522's split between mean spectra and
  laws: spectra can freeze while the underlying law drifts. The new result
  preserves that scope distinction rather than promoting a broader no-go.

## Dependencies

- [`UNRAVELED_STEP_LAW_BI_INVARIANT_QUASI_STATIONARITY_SPLIT_BOUNDED_THEOREM_NOTE_2026-06-10.md`](UNRAVELED_STEP_LAW_BI_INVARIANT_QUASI_STATIONARITY_SPLIT_BOUNDED_THEOREM_NOTE_2026-06-10.md)
  — names the bi-orbit-quotient step law object and the spectra-versus-law
  split refined here.
- [`UNRAVELED_RECORD_TRAJECTORIES_SUPPLY_NONDEGENERATE_STEP_DISTRIBUTION_BOUNDED_THEOREM_NOTE_2026-06-10.md`](UNRAVELED_RECORD_TRAJECTORIES_SUPPLY_NONDEGENERATE_STEP_DISTRIBUTION_BOUNDED_THEOREM_NOTE_2026-06-10.md)
  — supplies the Born-weighted unraveled step distribution surface and its
  residual 1.
- [`INDUCED_HOLONOMY_MATTER_STATE_FUNCTIONAL_DERIVED_CURVATURE_TRAJECTORY_BOUNDED_THEOREM_NOTE_2026-06-10.md`](INDUCED_HOLONOMY_MATTER_STATE_FUNCTIONAL_DERIVED_CURVATURE_TRAJECTORY_BOUNDED_THEOREM_NOTE_2026-06-10.md)
  — supplies the det/center induced-link thread this note probes at the
  quotient-law marginal.
- [`BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md`](BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md)
  — the unaudited Born assembly cap inherited from the parent route; this
  note does not promote it.

## Cross-references

- The named open object this strikes: the split note linked above. The four
  residuals: the nondegenerate-step-distribution note linked above. The
  det/center thread: the induced-holonomy note linked above.
- Standard math (method only): bi-orbits of unitary groups; determinant as the U(3)
  abelianization; circular statistics and characteristic functions; wrapped Gaussians;
  quantum-trajectory trees.
