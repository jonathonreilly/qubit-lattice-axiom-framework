# Historic intake: Weinberg Angle Derivation Attempt from Cl(3) Structure

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

The Cl(3) commutant fixes the hypercharge generator uniquely (traceless, eigenvalues +1/3 on six quark states and -1 on two lepton states) but not its coupling normalization: the C^8 trace-norm ratio Tr[S^2]/Tr[(Y/2)^2] = 3, not the GUT value 5/3, and the three candidate conventions give sin^2_UV = 1/2 (k=1), 3/8 (k=5/3) and 1/4 (k=3), running to 0.262, 0.176 and 0.106 at M_Z against a measured 0.231. Runner 13 PASS / 0 FAIL.

Original verdict: sin^2(theta_W) = 3/8 is NOT derived from Cl(3) — in a product group the relative U(1) normalization is not fixed by the algebra, and the note lists explicitly forbidden paper wordings including 'the Weinberg angle is a prediction of the framework'.
Scope: Cl(3)-on-Z^3 commutant algebra plus SM-only beta functions; the normalization obstruction is the central finding.
Escape conditions (negative claims): Three named future attacks: a lattice-theoretic normalization from staggered vertex-function ratios, anomaly matching (noted to constrain charges not couplings), or lattice perturbation theory generating a nontrivial k radiatively — none demonstrated and all bounded at best.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The Weinberg-angle terminal: sin^2 = 3/8 NOT derived from Cl(3) (relative normalization free in a product group) — retracts framework-level claim language; three future attacks named.

## Provenance (pinned)

- Original path: `docs/WEINBERG_ANGLE_DERIVED_NOTE.md`
- Source commit: `fb55ab178b77043b8eaf8e7d5725dfe1b8fff281`
- git blob: `2a9eba22a83a0b5ec9f4a1728b1545e34afd19e6`
- sha256: `99aa9122ffcdb91b2d6f537b9491951843fdac67a773da7d3980560d35a5e85a`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch07/2113_WEINBERG_ANGLE_DERIVED_NOTE.md](../../archive_unlanded/historic_intake_originals/branch07/2113_WEINBERG_ANGLE_DERIVED_NOTE.md)
- Lines: 185; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_weinberg_angle_derived​.py`; historic runner (unpinned, not in this packet): `scripts/frontier_gauge_unification​.py`; historic runner (unpinned, not in this packet): `scripts/frontier_weinberg_angle_correction​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- `docs/WEINBERG_ANGLE_CORRECTION_NOTE.md` — SM-only running correction (0.176 not 0.263).

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: Retracts framework-level claim language used elsewhere in the repo ('sin^2 theta_W = 3/8 is derived from Cl(3)' is listed as what the paper should NOT say).
- Supersession (as known at extraction): TERMINAL for the April Weinberg-angle pair: makes explicit the GUT-normalization assumption that frontier_gauge_unification​.py and the correction note (idx 2112) had used silently.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_no_go
intake_directive: owner_2026-08-05
```

Independent audit still required.
