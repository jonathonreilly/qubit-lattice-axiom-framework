# Historical Tier-A Admission Registry Index

**Original date:** 2026-05-23

**Current posture:** historical provenance only as of 2026-07-11

**Claim type:** meta

**Premise weight:** none
**Primary runner:** [`scripts/admitted_input_registry_tier_a_boundary_check.py`](../scripts/admitted_input_registry_tier_a_boundary_check.py)

## Current foundation rule

The supplied premise surface contains exactly:

1. framework axioms; and
2. explicitly approved primitives.

Both are registered in
[`docs/audit/data/axiom_premise_nodes.json`](audit/data/axiom_premise_nodes.json).
No admission, convention, governance decision, or derivation target satisfies
a physics dependency.

The machine file
[`docs/audit/data/tier_a_admissions.json`](audit/data/tier_a_admissions.json)
is retained solely to preserve historical statements, no-go portfolios, and
disposition provenance. Its live fields are permanently empty:

```text
genuine_admitted_input_count = 0
canonical_ids = []
derivation_targets = {}
```

## Historical targets

- **theta:** historical naturalness admission. Its gauge-side disposition is
  retained-derived; its mass-side K-real reading is conditional on the open AC
  occupancy-grain obligation.
- **AC_phi_lambda:** historical discrete-flavor admission. A 2026-07-05
  governance decision attempted to retire its remaining atoms without making
  them axioms or primitives. That premise channel was withdrawn on 2026-07-11.

The two unresolved AC atoms are now exact, non-premise open work:

- [AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md](AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md)
- [AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md](AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md)

They are indexed in
[`docs/audit/data/derivation_obligations.json`](audit/data/derivation_obligations.json)
and never make a dependent audit-ready or retained-grade.

## Approved primitives are unaffected

The scale reference `a^-1`, kinetic isotropy `c_t=c_s`, and realized-state
interface remain explicitly approved primitives. They are foundational,
chain-satisfy without bounding, and are guarded with the axiom memo by
`check_axiom_premise_clean.py`. The Record content remains part of the current
four-axiom memo.

## Convention metadata

The historical JSON continues to list `Y0` and `g0` for survey completeness as
vacuous rescaling conventions. They are not supplied inputs, do not satisfy a
dependency, and do not carry broader parent-note physics.

## Propagation rule

`docs/audit/scripts/premise_nodes.py` recognizes only ids from
`axiom_premise_nodes.json`. Every other dependency must already be
retained-grade or metadata context. An open obligation therefore leaves a clean
consumer at `retained_pending_chain`; a note that explicitly assumes the
obligation can be audited only at its honest conditional scope.

All graph and publication effects are regenerated mechanically. This index
sets no audit verdict and authorizes no hand promotion.
