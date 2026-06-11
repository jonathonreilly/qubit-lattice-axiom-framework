# The U(1)/Det Sector of the Bi-Orbit-Quotient Step Law: the Quotient's Invariant Marginal Is Non-Stationary, and It Decomposes into the Deterministic Dynamical Phase plus Quasi-Centered Record Noise

**Date:** 2026-06-10
**Type:** bounded theorem (retire-mode; the owner-directed strike on PR #3522's named open object)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_u1_det_sector_bi_orbit_quotient_step_law_2026_06_10.py`
**Cache:** `logs/runner-cache/frontier_u1_det_sector_bi_orbit_quotient_step_law_2026_06_10.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=20 FAIL=0` — exact,
deterministic, no MC (Born-weighted outcome tree to depth 11; **six seeds, including the
owner-found adversarial ones** — the draft's three-seed `< 0.25` median gate was
seed-tuned (seed 4242 gives 0.353; seeds 99/7 carry near-π stray maxima ~2.9/~2.0), and
the gates now assert only seed-robust content; #3507's guards inherited).

## The object, identified exactly

PR #3522 named the **bi-orbit-quotient step law** as its open object. **(D1)** For
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
  Conditionality inherited from #3507/#3522: the Born derived-chain cap (the assembly
  note `born_rule_from_gleason_busch_derivation_note_2026-05-20` is **unaudited** on
  the live ledger — self-verified at landing; two prior panels reported conflicting
  statuses, demonstrating the volatility); named instruments with supplied `ε`;
  supplied `C³` carrier; named hopping; guarded full-rank domain. Discrete-time
  throughout (retained R1 boundaries untouched). No new axiom, primitive, measure, or
  weight; `r` untouched. The audit lane grades.

## Cross-references

- The named open object this strikes: PR #3522 (science landed on origin/main via
  cherry-pick if closed; check `gh pr view 3522`). The split it refines: #3522. The four
  residuals: PR #3507 — science landed on origin/main via cherry-pick; PR
  closed-not-merged. The det/center thread: PR #3491 — same status.
- Standard math (method only): bi-orbits of unitary groups; determinant as the U(3)
  abelianization; circular statistics and characteristic functions; wrapped Gaussians;
  quantum-trajectory trees.
