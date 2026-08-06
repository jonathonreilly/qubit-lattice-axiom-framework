# Historic intake: CKM Higgs Z_3 Charge: Obstruction to L-Independence

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_no_go
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Proves the Higgs Z_3 charge delta = 1 is not L-independent: the 1D transition element <z+delta|eps|z> factorizes as a geometric sum with phase phi_delta = pi(3 - 2 delta)/3, and phi_1 and phi_2 have equal magnitude pi/3, so |T(delta=1)| = |T(delta=2)| exactly for every even L.

Original verdict: Sharp obstruction: the charge-1 selection cannot be made universal on this route, and the CKM lane stays bounded.
Scope: Staggered mass operator eps(x) on a d-dimensional cubic lattice with Z_3 taste projectors; threefold analytic obstruction.
Escape conditions (negative claims): The equality is a consequence of complex-conjugate phase symmetry for this operator — a Higgs candidate whose transition phases are not conjugate-symmetric escapes it.

## Why pulled (supervisor decision, on the record)

Sharp obstruction: the Higgs Z_3 charge-1 selection cannot be universal (phase equality forced by conjugate symmetry) — the route-killing exact negative, escape named.

## Provenance (pinned)

- Original path: `docs/CKM_HIGGS_Z3_UNIVERSAL_NOTE.md`
- Source commit: `6a4c225af365390328bc4441ea1e829206be5054`
- git blob: `09c945c13c1506a594eec57b86ffd5fd0553731b`
- sha256: `fd01fb0001a24366add1e43a1a25d8e3d0054420f44babe37fc72eaa1c7249d8`
- Lines: 123; runners named: frontier_ckm_interpretation_derivation.py, scripts/frontier_ckm_higgs_z3_universal.py

## Attached evidence (registered with, not as, this claim)

- `docs/CKM_HIGGS_FROM_ANOMALY_NOTE.md` — Anomaly route places no constraint (trivial cancellation); scoped to discrete conditions.
- `docs/CKM_HIGGS_FROM_GAUGE_NOTE.md` — Staggered condensate is exactly charge-0; the operator-level kill.

## Flags carried

none recorded

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
