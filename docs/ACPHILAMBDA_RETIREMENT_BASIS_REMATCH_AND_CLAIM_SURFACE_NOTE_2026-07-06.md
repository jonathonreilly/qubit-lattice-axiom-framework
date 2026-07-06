# AC_phi_lambda Retirement-Basis Re-Match and Claim-Surface Check

**Date:** 2026-07-06
**Type:** meta
**Claim type:** meta
**Status authority:** independent audit lane only. This note is a
post-landing verification artifact: it re-matches the landed owner-governance
retirement accounting against the audited realized-state decomposition basis
and sweeps the retired gate row's dependent claim surface. It sets no audit
verdict, changes no registry entry, and does not broaden the adoption beyond
its recorded boundary.
**Primary runner:**
[`scripts/acphilambda_retirement_basis_rematch_claim_surface_2026_07_06.py`](../scripts/acphilambda_retirement_basis_rematch_claim_surface_2026_07_06.py)
**Cache:**
[`logs/runner-cache/acphilambda_retirement_basis_rematch_claim_surface_2026_07_06.txt`](../logs/runner-cache/acphilambda_retirement_basis_rematch_claim_surface_2026_07_06.txt)

## Purpose

The theta retirement carried a re-match artifact checking the retirement
basis against the refined minimum statement before the registry action was
treated as settled. This note is the `AC_phi_lambda` analogue, run after the
2026-07-05 landing of the owner-governed retirement
([TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md](TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md)):
does the landed two-atom adoption accounting match, atom for atom and
boundary for boundary, what the audited decomposition basis actually
established — and does the direct-dependent lexical guard flag any
note-level bare-value reading?

## Re-match 1 — adopted atoms vs audited decomposition survivors

The audited realized-state decomposition split the original `AC_phi_lambda`
admission into three sub-admissions. The re-match, per atom:

| decomposition atom | audited value face (retained-grade) | audited survivor | adopted premise (registry id) | match |
|---|---|---|---|---|
| (i) occupancy | `r = B^2/a^2` is a defined functional of the registered signed-root masses; the chain-of-custody capstone carries the structure/value split ([CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md), [ACPHILAMBDA_OCCUPANCY_SELECTION_REALIZED_STATE_REDUCTION_NOTE_2026-06-11.md](ACPHILAMBDA_OCCUPANCY_SELECTION_REALIZED_STATE_REDUCTION_NOTE_2026-06-11.md)) | the measure-side realization binary (which statistical grain the realized state reads out through) | `ac_orbit_occupancy_statistical_grain_premise` — Candidate 1 adopts exactly "the matter-action occupancy grain needed to discharge the surviving AC(i) measure-side realization binary" | YES |
| (ii) R-eta | `Phi = (1/3) arccos(cos 3 delta)` is a single-valued functional of the unordered registered signed-root multiset ([ACPHILAMBDA_R_ETA_VALUE_FACE_REGISTERED_ANGLE_FUNCTIONAL_EXACTNESS_RELOCATION_NOTE_2026-07-05.md](ACPHILAMBDA_R_ETA_VALUE_FACE_REGISTERED_ANGLE_FUNCTIONAL_EXACTNESS_RELOCATION_NOTE_2026-07-05.md)); the forced form layer and the single surviving identification atom are separated in [ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING_BOUNDED_THEOREM_NOTE_2026-06-11.md](ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING_BOUNDED_THEOREM_NOTE_2026-06-11.md); the consuming chain declares the premise rather than deriving it ([KOIDE_DELTA_ETA_DENSITY_READOUT_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-09.md](KOIDE_DELTA_ETA_DENSITY_READOUT_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-09.md)) | the h-class/h-unit readout license (density read identity in h-units, no intervening factor) | `ac_reta_hclass_hunit_readout_premise` — Candidate 2 adopts exactly the "fixed-locus density class h, identity-read in h-units" license | YES |
| (iii) species | within-triplet naming is vacuous; the 1-of-6 assignment is registration surviving records; the carrier-locus chirality gate is already tracked at [KOIDE_GENERATION_ID_CL3_GRADE1_BRIDGE_NARROW_THEOREM_NOTE_2026-06-02.md](KOIDE_GENERATION_ID_CL3_GRADE1_BRIDGE_NARROW_THEOREM_NOTE_2026-06-02.md); the readout context `{P_k}` is supplied per the K/CPT bridge ([ACPHILAMBDA_SPECIES_BRIDGE_REALIZED_STATE_DECOMPOSITION_NOTE_2026-06-11.md](ACPHILAMBDA_SPECIES_BRIDGE_REALIZED_STATE_DECOMPOSITION_NOTE_2026-06-11.md)) | none requiring adoption — "No admitted content beyond named, already-tracked items survives in sub-admission (iii)" | (correctly not adopted; the registry's minimum is two atoms) | YES |

The landed registry's two-atom minimum is exactly the audited basis's
surviving-atom set. No atom is adopted that the basis shows dischargeable,
and no audited survivor is missing from the adoption.

## Re-match 2 — adopted boundary vs audited claim surface

The recorded boundary — the adoption "supplies no value of `r`, `delta`,
charged-lepton mass, mixing angle, probability rule, above-C3
taste/Dirac/chirality content, CKM/PMNS alignment, or sector-weight law" —
matches the audited surface:

- the value faces are registered, not derived (the counterfactual test of
  the realized-state primitive is applied inside the basis notes);
- the exactness residuals stay open frontiers, not adopted content: the
  registered-angle note labels `Phi_PDG - 2/9` a **comparator** (7.4e-6,
  never thresholded), and the occupancy-side exactness residual is likewise
  named, not consumed;
- the carrier-locus chirality gate remains an open tracked row, outside the
  adoption;
- the direct-dependent sweep below flags no note that both mentions the two
  values and lacks a named-input marker. This is only a note-level lexical
  guard.

## Re-match 3 — cross-admission consistency (theta)

- Theta is retired **by retained derivation**; its two Block49 candidates
  were approval context only, and the landing correctly did not resurrect
  theta as an owner-governed premise (registry: theta appears in
  `retired_derivation_targets` and NOT in the owner-governed canonical ids).
- The K/CPT orbit machinery consumed by the AC basis (the supplied-context
  bridge pattern) is the same pattern the theta mass-side discharge row uses;
  neither retirement consumes the other's residual atoms. The runner checks
  the registry-level separation.

## Claim-surface lexical check (the retired gate row's dependents)

The retired gate row has ~54 direct citation-graph dependents. The runner
sweeps every dependent note that exists on disk and enforces, mechanically:
any dependent whose text mentions the values (`r = 1/2` / `2/9`) must also
carry admission/conditionality vocabulary (the admission id, "admitted",
"modulo", "conditional", "premise", "adopted", or "registered") somewhere in
the note. This is a note-level lexical guard, not a per-sentence semantic
classification; it is the same class of check the two-gate bounded verifier
applies, extended across the dependent set. Zero flagged notes means zero
direct dependents tripped this lexical screen; it is not a per-sentence
semantic proof.

## Result

**Re-match result: supported.** The landed owner-governance retirement's accounting
(two adopted atoms; species leg not adopted; recorded no-value boundary;
theta untouched at its retained-derivation standing) matches the audited
realized-state decomposition basis atom-for-atom, and the direct-dependent
claim-surface sweep found zero bare-value lexical flags. The named open
frontiers survive the retirement unconsumed: the two exactness residuals and
the carrier-locus chirality gate.

## Firewalls

- No audit verdict is set or implied for any row; the audit lane remains the
  single status authority.
- No registry file is edited; this note only reads the landed state.
- The adoption is cited only at its registry id and exact boundary text; no
  broadening by title or summary.
- No value of `r`, `delta`, or any charged-lepton observable is derived,
  asserted, or thresholded here.

## Verification

Run:

```bash
python3 scripts/acphilambda_retirement_basis_rematch_claim_surface_2026_07_06.py
```

Expected close: `FAIL=0`.
