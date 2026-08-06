# Historic intake: Neutrino Solar Gap: Candidate Closure via eps/B = alpha_LM^2

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_conjecture
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Replacing the retained eps/B = alpha_LM/2 with a candidate alpha_LM^2 changes the predicted solar splitting from 4.19e-4 eV^2 (5.6x too big) to 7.56e-5 eV^2, matching the observed 7.41e-5 to 2%, while preserving the atmospheric splitting at 2.22e-3 (8% low) and normal ordering (m_1 = 4.4 < m_2 = 47.5 < m_3 = 48.3 meV).

Original verdict: Would CLOSE the retained solar-gap open lane (9/9 PASS) — the first concrete quantitative match within 2% after ~9 commits / 4 months — but the outstanding structural step is a retained derivation that does not exist on main.
Scope: Conditional on deriving eps/B = alpha_LM^2 from retained structure via a proposed three-level staircase (k_C = 9) with second-order residual-sharing.
Escape conditions (negative claims): The required extension is well-scoped and not a new axiom: extend the adjacent-placement theorem to a three-level staircase and prove second-order residual-sharing gives alpha_LM^2.

## Why pulled (supervisor decision, on the record)

The solar-gap alpha_LM^2 proposal: first quantitative match on the retained open lane (9/9) — WITH the substituted-coefficient/look-elsewhere flag; displaces a retained coefficient, so audit must see it.

## Provenance (pinned)

- Original path: `docs/NEUTRINO_SOLAR_GAP_ALPHA_LM_SQUARED_CANDIDATE_NOTE_2026-04-22.md`
- Source commit: `7dc554495c13551d89f358f1042ce6e2d043c906`
- git blob: `9ad622b9432f7c33069bd94d4979d73067c1cb28`
- sha256: `16accb73db5a2a72bfed72d005cefd54ca8d9041cad7dcf6faca5f40b3caa41d`
- Lines: 142; runners named: scripts/frontier_neutrino_solar_gap_alpha_lm_squared_candidate.py

## Attached evidence (registered with, not as, this claim)

- `docs/NEUTRINO_THREE_LEVEL_STAIRCASE_PROPOSAL_NOTE_2026-04-22.md` — Three-level staircase structural companion.

## Flags carried

A numerical match found by substituting a different coefficient into a retained theorem, with the supporting mechanism explicitly not yet derived.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
