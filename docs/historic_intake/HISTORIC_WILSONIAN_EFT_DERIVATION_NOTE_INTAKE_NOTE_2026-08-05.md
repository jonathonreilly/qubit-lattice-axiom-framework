# Historic intake: Wilsonian EFT Derivation: Closing the y_t Irreducible Residual

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

Argues the continuum-bridge assessment conflated two statements: the a -> 0 limit does not exist under A5, but a low-energy EFT for E << 1/a does, obtained by the exact Feshbach-Loewdin projection H_eff(E) = P_< H P_< + P_< H P_> (E - P_> H P_>)^{-1} P_> H P_<, verified numerically on toy lattices L = 16 to 128 to ~1e-15. Symmetry is preserved ([H,G] = 0 and [P_<,G] = 0 imply [H_eff, G_eff] = 0), and at E = M_Z lattice artifacts are suppressed by (E a)^2 = 5.6e-35.

Original verdict: Status CLOSED — the irreducible residual is claimed resolved by Feshbach projection, which is a mathematical identity rather than an imported physical assumption.
Scope: Feshbach projection as a QM identity plus operator classification under the derived gauge symmetry and emergent Lorentz invariance.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The EFT-vs-continuum-limit distinction: no a -> 0 limit under A5 but a low-energy EFT exists — pulled WITH its self-declared CLOSED flag for audit.

## Provenance (pinned)

- Original path: `docs/WILSONIAN_EFT_DERIVATION_NOTE.md`
- Source commit: `8b47a77b3a546b7a2041dd131d025eedbc599897`
- git blob: `d7615ae57dd6fe69627168f949e07dffa64606a3`
- sha256: `68ca65455f8f1bb6c739e82b7e6fb0f7de5ceeff7a6ca749fc3edbc784740be2`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch07/2118_WILSONIAN_EFT_DERIVATION_NOTE.md](../../archive_unlanded/historic_intake_originals/branch07/2118_WILSONIAN_EFT_DERIVATION_NOTE.md)
- Lines: 213; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_wilsonian_eft​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: Self-declares 'CLOSED' on a lane the rest of the corpus keeps open, and the Lorentz-emergence step is asserted from the free dispersion expansion rather than computed at loop level.
- Supersession (as known at extraction): Directly overturns YT_CONTINUUM_BRIDGE_ASSESSMENT's conclusion that the y_t blocker 'cannot be closed by further algebra' (idx 2167).

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_bounded_result
intake_directive: owner_2026-08-05
```

Independent audit still required.
