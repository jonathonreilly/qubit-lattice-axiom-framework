# Historic intake: Weinberg Angle Derivation Attempt from Cl(3) Structure

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

The Cl(3) commutant fixes the hypercharge generator uniquely (traceless, eigenvalues +1/3 on six quark states and -1 on two lepton states) but not its coupling normalization: the C^8 trace-norm ratio Tr[S^2]/Tr[(Y/2)^2] = 3, not the GUT value 5/3, and the three candidate conventions give sin^2_UV = 1/2 (k=1), 3/8 (k=5/3) and 1/4 (k=3), running to 0.262, 0.176 and 0.106 at M_Z against a measured 0.231. Runner 13 PASS / 0 FAIL.

Original verdict: sin^2(theta_W) = 3/8 is NOT derived from Cl(3) — in a product group the relative U(1) normalization is not fixed by the algebra, and the note lists explicitly forbidden paper wordings including 'the Weinberg angle is a prediction of the framework'.
Scope: Cl(3)-on-Z^3 commutant algebra plus SM-only beta functions; the normalization obstruction is the central finding.
Escape conditions (negative claims): Three named future attacks: a lattice-theoretic normalization from staggered vertex-function ratios, anomaly matching (noted to constrain charges not couplings), or lattice perturbation theory generating a nontrivial k radiatively — none demonstrated and all bounded at best.

## Why pulled (supervisor decision, on the record)

The Weinberg-angle terminal: sin^2 = 3/8 NOT derived from Cl(3) (relative normalization free in a product group) — retracts framework-level claim language; three future attacks named.

## Provenance (pinned)

- Original path: `docs/WEINBERG_ANGLE_DERIVED_NOTE.md`
- Source commit: `fb55ab178b77043b8eaf8e7d5725dfe1b8fff281`
- git blob: `2a9eba22a83a0b5ec9f4a1728b1545e34afd19e6`
- sha256: `99aa9122ffcdb91b2d6f537b9491951843fdac67a773da7d3980560d35a5e85a`
- Lines: 185; runners named: scripts/frontier_weinberg_angle_derived.py, scripts/frontier_gauge_unification.py, scripts/frontier_weinberg_angle_correction.py

## Attached evidence (registered with, not as, this claim)

- `docs/WEINBERG_ANGLE_CORRECTION_NOTE.md` — SM-only running correction (0.176 not 0.263).

## Flags carried

Retracts framework-level claim language used elsewhere in the repo ('sin^2 theta_W = 3/8 is derived from Cl(3)' is listed as what the paper should NOT say).

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
