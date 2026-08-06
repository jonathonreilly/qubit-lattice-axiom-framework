# Historic intake: SU(3) Bridge Derivation Candidate: rho = (c/c_00)^12 -> P = 0.5888

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_bounded
Stratum: branch_only_never_mainlined
Era: may_june_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Identifies the K-plaquette tube formula at k=12, rho_(p,q)(6) = (c_(p,q)(6)/c_(0,0)(6))^12, giving P = 0.5887944343 against the MC target 0.5934, a 0.78% gap (15x epsilon_witness) versus 543x for the prior d^(-16) ansatz; the residual matches the 1-loop scale 1/(2N^2 beta) = 0.93%.

Original verdict: bounded_theorem, strong derivation candidate but UNAUDITED; explicitly does not claim 0.5888 is the MC value.
Scope: L_s = 2 APBC cube with 12 plaquettes at beta = 6, Wilson character coefficients via Bessel determinant with mode_max = 200.


## Why pulled (supervisor decision, on the record)

The K-plaquette tube candidate: rho = (c_pq/c_00)^12 gives P = 0.58879 vs 0.5934 — a real bounded derivation candidate WITH its picture-choice flag; feeds the beta6 lane.

## Provenance (pinned)

- Original path: `docs/SU3_BRIDGE_DERIVATION_CANDIDATE_2026-05-04.md`
- Source commit: `094e400916bcd39845c7346dcf12df04b15d5aa5`
- git blob: `d868ab4b287513e12c6d4d5808c8331639b70f2c`
- sha256: `6fc9ef5654b1dfd47f4d1aa298163b4c0cff04a54fd1cd3fa131456d3fdcfbf1`
- Lines: 253; runners named: scripts/frontier_su3_bridge_rho_modification_scoping_2026_05_04.py, scripts/frontier_su3_bridge_mixed_ansatz_2026_05_04.py

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

Chooses among physical pictures (independent product vs Haar pairing) partly because it matches MC better; status is unaudited.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
