# Historic intake: Born Rule Derived from Lattice Propagator Structure

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

Proves the algebraic identity |A+B+C|^2 - |A+B|^2 - |A+C|^2 - |B+C|^2 + |A|^2 + |B|^2 + |C|^2 = 0, i.e. the Sorkin third-order interference parameter I_3 vanishes identically given amplitude linearity and P = |A|^2, following from finite tensor-product Hilbert space alone with no lattice-specific input.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Exact I3=0 identity from amplitude linearity WITH the era-audited title overclaim on the record ('Born rule derived' while assuming Born) — prior art for the live Born lane.

## Provenance (pinned)

- Original path: `docs/BORN_RULE_DERIVED_NOTE.md`
- Source commit: `f0f65457a234d889d21c0258e0d19faef707cb63`
- git blob: `d99588bce01359fb2ca6914bc8d40f5fe6dffc9b`
- sha256: `886f47537ee820611fd93cdd0527d1aad1225d7dcf6b74bd286f4aad6d710a03`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch01/115_BORN_RULE_DERIVED_NOTE.md](../../archive_unlanded/historic_intake_originals/branch01/115_BORN_RULE_DERIVED_NOTE.md)
- Lines: 127; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_born_rule_derived​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): Exact theorem for I_3 = 0 — but the title's 'Born rule derived' overstates it, since the Born rule is an assumption of the proof.
- Extraction scope (triage compression; may reflect later context): Assumes the Born rule P_S = |A_S|^2 and linearity of amplitudes; no lattice detail enters.
- Extraction red flags: Title claims the Born rule is derived while the proof assumes it; flagged as OVERCLAIMED by the April adversarial audit.
- Supersession (as known at extraction): Independently audited in ADVERSARIAL_AUDIT_2026-04-13, which rules the note and its runner OVERCLAIMED.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
