# Flavor — audit-ready verification of the det multiplicative-character selection (log-det factor 2): det is the unique composition-character (clean abelianization math) and additive-of-multiplicative fixes W = c·log|det|; the residual is the fermionic origin of Z=det, not the det-selection math

**Date:** 2026-06-04
**Claim type:** an audit-ready verification companion — supplies the verified computational backbone for the det multiplicative-character form-selection step (factor 2 of the log-det generator), with the honest two-premise bound. Not a value derivation; does not retag any row.
**Status authority:** independent audit lane only. This note sets no audit status and assigns no grade. It does not edit, re-cite, or promote any existing row — in particular it leaves `OBSERVABLE_PRINCIPLE_DET_UNIQUE_MULTIPLICATIVE_CHARACTER_FORM_SELECTION` (the claim it backs) untouched.
**Runner:** `scripts/flavor_det_character_selection_audit_ready_2026_06_04.py` (SCORECARD 7/7).
**Depends:** `minimal_axioms` (the Record axiom) for the additive-over-patches step.

## Purpose
The log-det generator `W = log|det(D+J)|` is the dominant blocker (59 rows) of the post-Record
observable-principle surface. Its three-factor provenance
(`FLAVOR_LOGDET_GENERATOR_THREE_FACTOR_PROVENANCE`) is: **(1)** additivity [Record axiom — closed],
**(2)** det multiplicative-character [this note], **(3)** source/action coupling [admission]. This note
makes **factor 2** an audit-ready, verified object and states its honest bound precisely.

## What is verified (runner 7/7)
- **STEP (i) — composition-axis selection (clean math).** On the composition axis
  `χ(A·S)=χ(A)χ(S)`, the determinant is multiplicative (`det(A·S)=det(A)det(S)`), while **`tr`,
  power-traces `tr(M^s)`, and elementary symmetric `e_k` (k<n) all FAIL** — they are excluded. The full
  algebraic multiplicative-composition character family is `det^k` (verified). This is the GL(n)
  abelianization content of step (i) of the existing note, now computationally confirmed.
- **STEP (ii) — additive-of-multiplicative → log (Record axis).** The partition amplitude `Z=det`
  multiplies over independent patches (`|det(A⊕B)|=|det A||det B|`); an observable `W` **additive** over
  those patches (the **Record axiom**) is uniquely `W = c·log|det|` (Cauchy) — `|det|^p` *multiplies* and
  only `log|det|` *adds* (verified). The character power `k` is absorbed into the scale `c`.

## The honest bound — Pattern L
**Additivity alone does NOT select det.** Verified explicitly: `tr` *is* additive over direct sums
(`tr(A⊕B)=tr(A)+tr(B)`), so the Record axiom's additivity axis **cannot exclude `tr`** — this is the
documented Pattern-L point. The exclusion of `tr` (hence the selection of `det`) requires the **separate
composition-multiplicativity premise (M)**, `χ(A·S)=χ(A)χ(S)`. Premise (M) is supplied by the
**Berezin/Grassmann partition amplitude** `Z = det(D+J)` multiplying over independent source patches — a
**fermionic-frame** property, not an additivity property.

So factor 2 decomposes honestly into:
- **clean math** (audit-ready here): GL(n) abelianization (det = unique composition-character up to
  power) + the Cauchy additive-of-multiplicative → log step; and
- **a residual premise** (M): the multiplicativity of `Z=det` over patches, which is the fermionic /
  Berezin origin of `Z=det` — i.e. it **overlaps the source-coupling factor 3**, not the Record axiom.

## Net effect on the chain
After this note, the log-det generator's factor-2 *mathematics* (det-selection + log form) is verified
and audit-ready; the only open content of factor 2 collapses onto premise (M) = the fermionic/Berezin
origin of `Z=det`. Combined with the provenance note, the 59-row log-det blocker now reduces to a
**single remaining open premise** — *why `Z=det(D+J)` is the partition amplitude (the fermionic/Berezin
frame)* — rather than two fuzzy factors. That single premise is the genuine next target (it is the
source/action–coupling / Grassmann-realization admission already tracked downstream); the additivity
(Record) and the det-selection/log math are now both supplied.

## Scope discipline
New files only. Does not edit or re-cite the existing det-character note, the 91 observable-principle
dependents, `observable_principle_from_axiom_note`, the axiom-premise allowlist, or any audit data file.
The dependency classification is owned by `RECORD_P1_DEPENDENCY_AUDIT_NOTE`; all status is the
independent audit lane's.

## Provenance (verified 2026-06-04)
- det multiplicative under composition; `tr`/power-trace/`e_2` excluded; `det^k` family; Pattern-L (`tr`
  additive over direct sums); `Z=det` multiplies over patches with only `log|det|` additive: verified
  directly (runner 7/7).
- This note sets no audit status; it supplies the verified backbone for factor 2 and names the precise
  residual premise (M).
