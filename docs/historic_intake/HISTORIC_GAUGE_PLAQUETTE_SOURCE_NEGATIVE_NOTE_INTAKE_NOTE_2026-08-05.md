# Historic intake: Gauge Plaquette Source Theorem and Constant-Lift No-Go

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

Both the full 3+1 plaquette and the one-plaquette block have strong-coupling slope exactly 1/18 at beta = 0, so any exact identity P_full(beta) = P_1plaq(c beta) on an interval forces c = 1 - ruling out the proposed lift constant c = (3/2)(2/sqrt3)^(1/4) = 1.554921974442116.

Original verdict: The proposed constant-lift closure is exactly ruled out; what survives is the source identity, the exact Toeplitz/Bessel one-plaquette block, and the strong-coupling slope.
Scope: Exact on a finite 3+1 Wilson lattice; the one-plaquette block is cross-checked against an independent Weyl-angle integral to machine precision (P_1plaq(6) = 0.422531739649983).
Escape conditions (negative claims): The negative kills only CONSTANT lifts: it forces c = 1 for any identity valid on an interval, leaving non-constant (beta-dependent) lifts and other closure forms untouched.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Exact no-go: strong-coupling slope 1/18 on both objects forces c = 1 — every constant-lift closure (including the landed-adjacent 575) is ruled out.

## Provenance (pinned)

- Original path: `docs/GAUGE_PLAQUETTE_SOURCE_NO_GO_NOTE.md`
- Source commit: `60a264ba93427b648c4c01edb5b2437542b78eb5`
- git blob: `7c919d734b04fd836be4b57255d2eb12179c47e0`
- sha256: `58efe8f729692c38acf7d5a2a6d398f1517471ae1b64720ecbbd6a2cfefc105b`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch02/564_GAUGE_PLAQUETTE_SOURCE_NO_GO_NOTE.md](../../archive_unlanded/historic_intake_originals/branch02/564_GAUGE_PLAQUETTE_SOURCE_NO_GO_NOTE.md)
- Lines: 226; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_gauge_plaquette_source_no_go​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- `docs/GAUGE_VACUUM_PLAQUETTE_CLOSURE_NOTE.md` — The constant-lift closure claim; exactly refuted by 564.

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
