# Historic intake: Hierarchy Ratio: Gravity/EM Coupling Constraints

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

Registered as a bounded registration of a historical negative claim; no live no-go is asserted by this wrapper — no-go discipline applies at audit adjudication.

## The claim (as stated by the original, supervisor-compressed)

The path-sum framework does not constrain the gravity/EM hierarchy: the mixed residual R_GE = 0 to machine precision (< 1e-14) for all 20 tested (G,q) pairs, gravity convergence is independent of q, and all tested ratios from 0.004 to 1000 work equally well.

Original verdict: Null result — the two sectors are strictly independent and the hierarchy problem is really a mass-spectrum problem (why m_proton << m_Planck), not a coupling-ratio problem.
Scope: 16^3 cubic lattice, k = 4.0, Dirichlet BC; four tests (G sweep via self-consistent Poisson, q sweep via ray deflection, natural-scale ratio, combined grid).
Escape conditions (negative claims): The negative rests on the sectors' structural independence (gravity enters as a self-consistently sourced scalar in S = L(1-f), EM as a phase q*V with no back-reaction) and on G having units [length^2] while q is dimensionless; the escape named is a mechanism relating the mass spectrum to lattice structure, which is absent from the current formulation.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Clean null: gravity/EM sectors strictly independent (mixed residual < 1e-14 across 20 pairs) — the hierarchy problem is a mass-spectrum problem, not a coupling problem.

## Provenance (pinned)

- Original path: `docs/HIERARCHY_RATIO_NOTE.md`
- Source commit: `fafde285641ea02cec7b7c6e10011378f8712675`
- git blob: `af3cc8abf89ca1d032cbec43e3470d3c8070f97e`
- sha256: `c9e2347502d2ee7a49fad098687dbf546aace7c3fe16e8f940989ac4a258e6d7`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch03/703_HIERARCHY_RATIO_NOTE.md](../../archive_unlanded/historic_intake_originals/branch03/703_HIERARCHY_RATIO_NOTE.md)
- Lines: 62; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_hierarchy_ratio​.py`; historic runner (unpinned, not in this packet): `scripts/frontier_self_consistent_field_equation​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: none recorded
- Supersession (as known at extraction): none recorded

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_no_go
intake_directive: owner_2026-08-05
```

Independent audit still required.
