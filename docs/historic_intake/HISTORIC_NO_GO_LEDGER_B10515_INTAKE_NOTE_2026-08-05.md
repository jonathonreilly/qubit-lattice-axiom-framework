# Historic intake: No-Go Ledger (hadron sqrt-sigma B2)

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_no_go
Stratum: pack_science_family
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Four results proven in-loop, most sharply: the PDG backsolve factor cannot be used because solving 440/484 approximately 0.909 takes the target comparator as the SOURCE of the screening factor; the rough x0.96 B2 promotion fails for lack of a branch-local N_f = 2+1 dynamical ensemble, a full-QCD observable definition, and an uncertainty budget; a pure quenched volume-scaling route can help B5 but cannot close B2, which is specifically about dynamical sea-quark effects; and the literal asymptotic full-QCD string tension is the wrong B2 object because full-QCD strings break, so B2 must target a pre-breaking effective tension, force scale, or static-energy fit window.

Original verdict: Every shortcut to a retained sqrt(sigma) is closed, one of them for explicit circularity.
Scope: The B2 bridge; inherits three prior firewalls including the confinement-to-mass shortcut and the Banks-Casher Sigma route.
Escape conditions (negative claims): A branch-local N_f = 2+1 dynamical ensemble with a defined full-QCD observable and uncertainty budget, targeting a pre-breaking window.

## Why pulled (supervisor decision, on the record)

Verification-integrity catch plus route closure: the PDG backsolve factor 440/484 ~ 0.909 is EXPLICITLY CIRCULAR (it takes the target comparator as its own source), and every shortcut to a retained sqrt(sigma) is closed; the honest escape (branch-local N_f = 2+1 dynamical ensemble) is named.

## Provenance (pinned)

- Original path: `.claude/science/physics-loops/hadron-sqrt-sigma-b2-20260430/NO_GO_LEDGER.md`
- Source commit: `b0067afbf66a4ced91b5fadd07dd54368539dc75`
- git blob: `3aec55968310e6e20d63ac76416599775031c5dc`
- sha256: `1cfe05e6c4524ee5a15ed582819c5358d349c99a72904f6cbbaafcf405b1797c`
- Lines: 27; runners named: none

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

Explicit circularity caught: a screening factor was being backsolved from the PDG target it was meant to predict (440/484 = 0.909).

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
