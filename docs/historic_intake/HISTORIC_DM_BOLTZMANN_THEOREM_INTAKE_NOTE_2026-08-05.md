# Historic intake: Boltzmann Equation as a Lattice Theorem

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

Proves the lattice master equation for taste occupation numbers reduces to the Boltzmann equation dn/dt + 3Hn = -<sigma v>(n^2 - n_eq^2) in the thermodynamic limit, via exact transition rates, a Stosszahlansatz derived from the spectral gap, Riemann-sum and Weyl's-law convergence with UV finiteness from the compact Brillouin zone, and an expansion term from graph growth.

Original verdict: The Boltzmann equation is a lattice theorem rather than an import, making R a corollary given the Casimir ratio, alpha_s at g_bare = 1, and the Sommerfeld factor.
Scope: Thermodynamic limit L -> infinity at fixed lattice spacing; closes the objection that freeze-out was imported cosmology.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The Boltzmann equation as a lattice THEOREM (exact transition rates, Stosszahlansatz discharged) closing a standing import objection — with the alpha_s/g_bare caveat carried.

## Provenance (pinned)

- Original path: `docs/DM_BOLTZMANN_THEOREM.md`
- Source commit: `8e20182cc534935063b9a384e11da7b0f6772d37`
- git blob: `c80a5dd85671602d64c66da5042127c08084fffd`
- sha256: `70330dbc1b9ba39db6af5f359c4dd4c601c4107dc5bab4bfaa83ed5bc33846cd`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch01/338_DM_BOLTZMANN_THEOREM.md](../../archive_unlanded/historic_intake_originals/branch01/338_DM_BOLTZMANN_THEOREM.md)
- Lines: 275; runners named: historic runner (unpinned, not in this packet): `frontier_dm_direct_boltzmann​.py`; historic runner (unpinned, not in this packet): `frontier_dm_friedmann_from_newton​.py`; historic runner (unpinned, not in this packet): `frontier_dm_stosszahlansatz_theorem​.py`; historic runner (unpinned, not in this packet): `scripts/frontier_dm_boltzmann_theorem​.py`; historic runner (unpinned, not in this packet): `scripts/frontier_dm_friedmann_from_newton​.py`; historic runner (unpinned, not in this packet): `scripts/frontier_dm_stosszahlansatz_theorem​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: The corollary still routes through alpha_s at g_bare = 1, which other notes flag as an assumed input (Axiom A5).
- Supersession (as known at extraction): Closes a standing Codex objection that Boltzmann/Friedmann freeze-out was imported standard cosmology.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
