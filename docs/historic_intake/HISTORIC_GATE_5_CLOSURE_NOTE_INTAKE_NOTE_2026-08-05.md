# Historic intake: Gate 5: Dark Matter Freeze-Out

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_bounded
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Splits the R = 5.48 chain into three input classes: particle content (derived from the same orbit algebra as generations, with the hw=0 light singlet as the DM candidate), cross-section and coupling (derived from alpha_s and SU(3) group theory plus the lattice Sommerfeld factor, 20/20 PASS), and the thermal freeze-out mechanism (Boltzmann, Friedmann, g_* = 106.75, x_F ~ 25) which is argued to be universal cosmology common to every DM model.

Original verdict: The ratio is a structural consistency result, not a pure first-principles derivation, because the thermal cosmological mechanism is imported as universal physics.
Scope: The framework derives the inputs to the thermal history, not the history itself.


## Why pulled (supervisor decision, on the record)

Gate-5 honest verdict: the DM ratio is structural consistency, not first-principles — the thermal-cosmology imports named.

## Provenance (pinned)

- Original path: `docs/GATE_5_CLOSURE_NOTE.md`
- Source commit: `87eb5109dc2bc0ce8350c02f02d63cea5c3dd327`
- git blob: `8f4c8b7786ab6cf7c6ee839189f23c3d4fd78ea3`
- sha256: `b67a620449446c9598191591c0c89de0b71d79b3055bd11e219890b4c3d7034b`
- Lines: 94; runners named: scripts/frontier_dm_ratio_sommerfeld.py, scripts/frontier_freezeout_from_lattice.py

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

Defends imported machinery by analogy to other DM models rather than deriving it; the honest boundary is drawn to place Boltzmann and Friedmann outside the claim.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
