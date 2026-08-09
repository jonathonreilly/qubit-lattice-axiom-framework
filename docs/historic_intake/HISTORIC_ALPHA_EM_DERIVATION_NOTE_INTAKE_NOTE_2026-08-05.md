# Historic intake: α_EM from Cl(3)/Z³ Axioms: Resolution of the 27% Gap

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

Closes the earlier 27% gap in g_1(v) by adding the taste threshold staircase and the color projection: g_1(v) = 0.46438 vs 0.46400 (+0.08%), g_2(v) = 0.64803 vs 0.64630 (+0.27%), sin^2 theta_W(M_Z) = 0.23064 vs 0.23122 (-0.25%), 1/alpha_EM(M_Z) = 127.682 vs 127.951 (-0.21%), claimed with zero SM imports.

Original verdict: DERIVED at 0.21% accuracy; unblocks the alpha_EM half of the hydrogen/helium blocker while the electron mass stays open.
Scope: Claims derivation from Cl(3)/Z^3 axioms with zero SM imports; the 0.21% residual is attributed to 2-loop systematics.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The era's alpha_EM/electroweak closure claim at 0.21% (g_1, g_2, sin^2 theta_W) WITH its next-day audit attached — flagship-era numeric surface for the audit lane to price.

## Provenance (pinned)

- Original path: `docs/ALPHA_EM_DERIVATION_NOTE.md`
- Source commit: `a6fdce65069126907d9e2f1ab8bf55569b5487de`
- git blob: `6d82fd00e6502eb25522b3d691964b83ad32f64d`
- sha256: `75f9496d34f6fbb07d07fa7d1cc5f273559536b174029bffd23d408132b0556a`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch01/45_ALPHA_EM_DERIVATION_NOTE.md](../../archive_unlanded/historic_intake_originals/branch01/45_ALPHA_EM_DERIVATION_NOTE.md)
- Lines: 198; runners named: historic runner (unpinned, not in this packet): `alpha_em_twoloop_rge​.py`; historic runner (unpinned, not in this packet): `scripts/alpha_em_from_axioms​.py`; historic runner (unpinned, not in this packet): `scripts/alpha_em_twoloop_rge​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- `docs/ALPHA_EM_AUDIT_NOTE.md` — The step-by-step audit that downgrades three steps of 45 — rides the pull as adverse evidence.

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: Audited the next day (ALPHA_EM_AUDIT_NOTE) which downgrades three of its steps to vulnerable and flags a circularity risk.
- Supersession (as known at extraction): Explicitly supersedes EW_COUPLING_DERIVATION_NOTE.md (2026-04-14, marked SUPERSEDED), whose perturbative 1-loop treatment gave the +27% gap.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_derived
intake_directive: owner_2026-08-05
```

Independent audit still required.
