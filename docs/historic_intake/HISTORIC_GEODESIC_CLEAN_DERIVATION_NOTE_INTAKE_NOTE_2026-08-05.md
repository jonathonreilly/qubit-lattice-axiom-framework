# Historic intake: Geodesic Equation from the Lattice Path-Sum: Clean Derivation

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

A step-by-step chain from the single axiom Cl(3) on Z^3 to the geodesic equation with Christoffel symbols, labelling each step DERIVED, THEOREM or BOUNDED: H = -Delta from the Kogut-Susskind construction, G_0 = H^-1 by definition, the closure condition L^-1 = G_0 forcing the Poisson equation, the discrete Green's function going to M/(4 pi r), then eikonal/stationary-phase steps into Riemannian geometry.

Original verdict: The geodesic equation including Christoffel symbols follows from the lattice path-sum without importing general relativity.
Scope: One step is explicitly BOUNDED (conditional on the continuum limit); the rest are DERIVED or standard-mathematics THEOREM.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The geodesic chain with audited per-step provenance — Christoffels from the path-sum, with the conditional continuum step flagged mid-chain.

## Provenance (pinned)

- Original path: `docs/GEODESIC_CLEAN_DERIVATION_NOTE.md`
- Source commit: `6cb7204d1184a9826e67adb37cef9623f749e040`
- git blob: `0ba0e53e73658e6d2161a42ab84581b366155e79`
- sha256: `e971d12abf132bf073344dd02219f5677eb5cca44bb4c1589461e950951af7b8`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch02/636_GEODESIC_CLEAN_DERIVATION_NOTE.md](../../archive_unlanded/historic_intake_originals/branch02/636_GEODESIC_CLEAN_DERIVATION_NOTE.md)
- Lines: 414; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_geodesic_equation​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- `docs/GEODESIC_EQUATION_NOTE.md` — The measurement predecessor.

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: A continuum-limit-conditional BOUNDED step sits in the middle of a chain whose sibling universality note (idx 632) argues the framework has no continuum limit at all.
- Supersession (as known at extraction): The audited-provenance successor to the earlier results note (idx 637) - same runner, but every step labelled by derivation status.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
