# Historic intake: DM Source-Surface Z_3-Doublet-Phase Chart-Change Scout Note

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

The prompt's z = q_+ + i delta is a chart artifice (q_+ is a Z_3 singlet, delta a real slice of the doublet), so Im(z^3) is not a retained invariant; the correct doublet-phase coordinate A(H) = Tr(H T_{d,w}) = 3 delta + i sqrt(3) m gives the real Z_3-invariant delta-ODD polynomial 2 Re(A^3) = 54 delta(delta^2 - m^2).

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Genuine counterexample refining a retained theorem's scope: Im(z^3) is a chart artifice but the correct doublet-phase coordinate exposes the delta-evenness claim as Hermitian-insertion-scoped — audit-relevant scope repair.

## Provenance (pinned)

- Original path: `docs/DM_NEUTRINO_SOURCE_SURFACE_Z3_DOUBLET_PHASE_CHART_SCOUT_NOTE_2026-04-18.md`
- Source commit: `5329f8dbf8643636c3de4ddce4214bd5a4d26794`
- git blob: `de0ba82010d24fca61b94a3dc3ac6d0b0f46d234`
- sha256: `e4991d7d9c84e6c3282bbaf6ec0f758b8305560757b60249a5050c09df259924`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch02/384_DM_NEUTRINO_SOURCE_SURFACE_Z3_DOUBLET_PHASE_CHART_SCOUT_NOTE_2026-04-18.md](../../archive_unlanded/historic_intake_originals/branch02/384_DM_NEUTRINO_SOURCE_SURFACE_Z3_DOUBLET_PHASE_CHART_SCOUT_NOTE_2026-04-18.md)
- Lines: 342; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_dm_neutrino_source_surface_z3_doublet_phase_chart_scout​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): PARTIAL - the Case 3 impossibility theorem's delta-evenness claim holds only for Hermitian-operator insertions, so its scope needs refinement rather than retraction.
- Extraction scope (triage compression; may reflect later context): Drops assumption A1.2 (that the affine (m,delta,q_+) chart is the right parametrization); the delta-odd invariant is built from non-Hermitian operator insertions.
- Extraction escape conditions (negative claims; triage compression): The parent impossibility theorem survives only if the retained observable class is restricted to Hermitian-operator insertions; admitting the broader operator class (non-Hermitian C_3-eigenvector insertions T_{d,w}) produces an explicit real Z_3-invariant delta-odd polynomial and breaks delta-evenness.
- Extraction red flags: Finds a genuine counterexample to the parent theorem's delta-evenness claim under a broader operator class; also notes a cited prerequisite note does not exist on the atlas.
- Supersession (as known at extraction): Proposes a candidate refinement to the SCOPE of DM_NEUTRINO_SOURCE_SURFACE_MICROSCOPIC_POLYNOMIAL_IMPOSSIBILITY_THEOREM_NOTE_2026-04-17.md and includes a 'Revised impossibility theorem status' section.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_partial
intake_directive: owner_2026-08-05
```

Independent audit still required.
