# The Centered U(1) Fluctuation Law: Not Distribution-Stationary, Non-Gaussian in the Spread Regime — and the Spread Decomposes into Record-Sector Mixture plus Within-Sector Spread

**Date:** 2026-06-11
**Type:** bounded theorem (answer-mode; source proposal for PR #3532's named next object)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_centered_u1_fluctuation_record_mixture_structure_2026_06_11.py`
**Cache:** `logs/runner-cache/frontier_centered_u1_fluctuation_record_mixture_structure_2026_06_11.txt`
**Status:** source proposal; the audit lane grades. A mandatory 4-lens adversarial panel
returned `land_with_edits`; **all edits applied** (the decisive one re-anchors E3 on the
permutation-null-cleared events). Runner `PASS=8 FAIL=0` — exact,
deterministic, no MC (Born-weighted outcome tree to depth 11; **six seeds including the
adversarial set, per the standing policy**; #3507's guards inherited).

## The question #3532 posed, and the answer

#3532 split the det/U(1) increment into the deterministic record-free dynamical phase
plus a record-induced fluctuation and posed the U(1)-CLT question on the **centered
fluctuation**. This note answers it at this size and horizon — negatively for the
unconditional law, with a constructive structure as the remainder.

## The findings (exact — runner `PASS=8 FAIL=0`)

**(E1) Not distribution-stationary — the honest negative.** The centered law's per-depth
characteristic-function drift is far below the raw law's at the tame seed
(median ratio `≈ 0.2`) but rises toward `~0.5+` at adversarial seeds, with individual
rows where the centered drift *exceeds* the raw: **distribution-stationarity of the
centered law fails as a seed-robust claim.** Centering removes the *mean* wandering
(#3532's seed-robust ratio result); it does not deliver a stationary law.

**(E2) Non-Gaussian in the spread regime — where the test has teeth.** At identified
spread rows (`|ch₁| < 0.8`), the composed centered phase violates the wrapped-Gaussian
relation **in the atomic direction**: `|ch₂|` *exceeds* the Gaussian prediction by `>0.2`
(sharpest row: `0.925` vs `0.147`) across multiple seeds — the **bimodal/few-atom
signature**, not diffusion. With the #3532-D4 control armed (high-concentration matches
are variance-automatic and prove nothing), the conclusion is clean: **no U(1)-CLT emerges
unconditionally at this object, size, and horizon.**

**(E3) The record-mixture structure — panel-re-anchored on null-cleared events.** A
**label-permutation control** is armed in-runner (random relabel into same-cardinality
families). The draft's depth-3 "exact mixture at machine precision" headline was a
**two-atom tautology** — family size 2, cardinality-forced, the permutation null also
reaches ~1, true value `1 − 2.2×10⁻⁵` (worst family `1 − 5.1×10⁻⁵`), collapsing with
family growth (`0.99998` d3 → `0.984` d4 → `0.868` d5 → `0.557` d9) — **demoted and
disclosed** (it is also E2's sharpest bimodal row: the *same* event, double-duty
disclosed). The **load-bearing structure** is at events with large families, where the
record prefix **clears the permutation null decisively**:

```
LOAD-BEARING event    (seed 4242, depth 9; 128 branches/family at prefix-3):
                      record 0.557  vs  null median 0.463 / p95 0.469 / max 0.481
SECOND event          (seed 99, depth 7):  0.057 → 0.347 → 0.502 (prefixes 2, 3)
                      vs null p95 0.315
(near-exact small-family events also occur — seed 7 depth 4: 0.081 → 0.9999 at
 prefix-3 — same cardinality caveat as d3, disclosed)
```

The record **registers partial phase-family structure** (exhibited structure, not an
axiom claim), with a **within-sector remainder** conditioning does not remove — the
two-component anatomy. **Consequence, and the next object defined sharply:** the
unconditional composed-phase law is a record-mixture and is *not* the CLT-walker object;
the well-posed conditional object is the **fixed-prefix-`k` law as the horizon grows**
(full conditioning is vacuous — singleton families). First datum, honest: the fixed-`k`
profile does **not** concentrate at this instance (`d9`: prefix-2 = prefix-3 = `0.557`,
prefix-4 `0.598`) — **the re-posing is open, with a first negative data point.**

**(E4) Correlations, disclosed.** Consecutive centered increments: medians mostly small
(`< 0.15`) with adversarial spikes (up to `~0.55`) — the independence premise is also
not seed-robust as-is.

## Where this leaves the program

- **Residual 1 of #3507 now has a three-layer anatomy:** the matrix-level wandering is
  bi-frame (#3522); the invariant marginal's wandering is the deterministic dynamical
  phase (#3532); and the centered fluctuation around that phase is a **record-sector
  mixture plus within-sector spread** (here). Each layer was found by quotienting out
  the previous one; the remaining question — the record-conditional law's behavior — is
  the sharpest form yet.
- **No CLT premise is delivered**; #3507's residuals stand. The `U(1)` factor of `U_eff`
  is not identified with a physical gauge field (identification gate, as throughout).
- Finite horizon; six seeds (adversarial included); one `(ε,τ)` instance; all numbers
  seed/instance-labeled. Conditionality inherited (#3507/#3522/#3532): the Born
  derived-chain cap — the assembly note
  `born_rule_from_gleason_busch_derivation_note_2026-05-20` is **unaudited** on the live
  ledger (self-verified at landing; status volatility documented in #3532) — named
  instruments with supplied `ε`; supplied `C³` carrier; named hopping; guarded full-rank
  domain. Discrete-time throughout (retained R1 boundaries untouched). No new axiom,
  primitive, measure, or weight; `r` untouched. The audit lane grades.

## Cross-references

- The posed question and the baseline decomposition: PR #3532 — science landed on
  origin/main via cherry-pick; PR closed-not-merged. The split and its scope: PR #3522 —
  same status.
  The four residuals: PR #3507 — same status. The det/center thread: PR #3491 — same
  status.
- Standard math (method only): circular statistics; mixture decompositions; conditioning
  on filtrations (record prefixes); quantum-trajectory trees.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [born_rule_from_gleason_busch_derivation_note_2026-05-20](BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md)
