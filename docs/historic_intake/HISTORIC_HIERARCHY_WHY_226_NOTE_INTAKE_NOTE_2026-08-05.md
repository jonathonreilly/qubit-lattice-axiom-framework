# Historic intake: Why Did v = 226 GeV Shake Out? A Thorough Investigation

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

The 226 GeV result is a coincidence from two large errors that nearly cancel: y_t = 0.9369 (the SM pole-scale value) was quietly substituted for the framework's derived y_t = 0.439, and Sigma_1 was inflated to 6.0; with the derived y_t and N_eff = 10.64 the chain gives v = 45 GeV (or 3.6 TeV at N_eff = 12). Exact integrals give I_stag(4) = 0.619734 = 4 I_Wilson(4), so Sigma_1 is 2.479 under d*I_stag or 6.117 under pi^2*I_stag.

Original verdict: The number is a coincidence but the mechanism is real — CW dimensional transmutation with the framework's structural y_t genuinely produces v in the O(0.1-10 TeV) range; the precise value cannot be extracted without resolving the matching scheme.
Scope: Full re-derivation of the original 226 GeV chain plus identification of which lattice-integral combination 'Sigma_1' denotes.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

WHY-226 coincidence anatomy: two large errors nearly cancel, smuggled y_t identified — pairs with 696 as the era's numeric-integrity record.

## Provenance (pinned)

- Original path: `docs/HIERARCHY_WHY_226_NOTE.md`
- Source commit: `3524a8b5c9e89bb310fbd48b590258242b374f70`
- git blob: `f756c33c24da97d54aa2566ef96df83b9752e1e5`
- sha256: `ce62ce56c2350ae983a4d677d2df73893d197011e4ad573dfef021f1d4b4d9e3`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch03/708_HIERARCHY_WHY_226_NOTE.md](../../archive_unlanded/historic_intake_originals/branch03/708_HIERARCHY_WHY_226_NOTE.md)
- Lines: 784; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_sigma1_exact(.py)`

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

Documents a smuggled observed input (y_t = 0.9369) in a published derivation chain; the two corrective notes disagree on the correct Sigma_1 identification.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_analysis
intake_directive: owner_2026-08-05
```

Independent audit still required.
