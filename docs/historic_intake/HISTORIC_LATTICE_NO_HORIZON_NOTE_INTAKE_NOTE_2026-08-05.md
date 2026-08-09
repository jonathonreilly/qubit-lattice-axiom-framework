# Historic intake: Lattice No-Horizon Argument: g_tt > 0 from Bounded Green's Function

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

The Z^3 lattice Green's function is finite at the origin, G_L(0) = 0.2527 (Watson integral, BZ-converged 0.24995 -> 0.25245 over 50-500 points), so phi(0) = 0.2527 M is bounded for any finite M where the continuum diverges. Since g_tt = -(1-2phi)^2 is a perfect square it vanishes only at phi = 1/2 exactly, which for generic M is met at no lattice site (critical M_crit = 1/(2 G_L(0)) = 1.981 touches it only at the source site).

Original verdict: g_tt > 0 at all lattice sites generically, so no event horizon forms — an upgrade of the claim from CONJECTURE (which used Schwarzschild at r ~ R_S) to CONDITIONAL (on the conformal metric form).
Scope: Depends only on the lattice Poisson equation, Watson finiteness, and the conformal metric form g_tt = (1-2phi)^2 — notably NOT on Schwarzschild holding anywhere; but it does depend on the conformal metric being correct in strong field.
Escape conditions (negative claims): The result is a lattice artifact that survives only if the physical lattice spacing is nonzero (a = l_Planck); as a -> 0 the regularization disappears. Whether the conformal metric is the correct strong-field metric remains open.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

No-horizon theorem: G_L(0) finite bounds phi so g_tt > 0 generically — the frozen-star lane's exact basis, lattice-artifact escape stated.

## Provenance (pinned)

- Original path: `docs/LATTICE_NO_HORIZON_NOTE.md`
- Source commit: `d170649668480527c7724550c2380ed8d4ef28bb`
- git blob: `7ad915e72b74f027900cd7114af419c6f568ef8e`
- sha256: `a56acd31b747c0da05d04d5793d0845c64b6359d11db2c57fed72535c4e28b71`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch04/1099_LATTICE_NO_HORIZON_NOTE.md](../../archive_unlanded/historic_intake_originals/branch04/1099_LATTICE_NO_HORIZON_NOTE.md)
- Lines: 223; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_lattice_no_horizon​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: none recorded
- Supersession (as known at extraction): Explicitly supersedes/complements the previous conjecture in STRONG_FIELD_HONEST_ASSESSMENT.md, replacing a Schwarzschild-dependent argument with a lattice-only one (comparison table included).

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
