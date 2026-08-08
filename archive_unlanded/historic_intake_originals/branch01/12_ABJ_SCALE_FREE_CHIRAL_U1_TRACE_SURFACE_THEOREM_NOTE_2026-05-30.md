# ABJ Scale-Free Chiral U(1) Trace Surface Theorem

**Date:** 2026-05-30
**Claim type:** positive_theorem
**Status authority:** independent audit lane only. This source note proposes
a narrow positive theorem; it does not set or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_abj_scale_free_chiral_u1_trace_surface.py`](../scripts/frontier_abj_scale_free_chiral_u1_trace_surface.py)
**Generated output:**
[`outputs/abj_scale_free_chiral_u1_trace_surface_2026-05-30.json`](../outputs/abj_scale_free_chiral_u1_trace_surface_2026-05-30.json)

## Purpose

The 3+1 anomaly route does not need the bounded physical-hypercharge
normalization bridge.  For the ABJ obstruction it is enough that the chiral
U(1) generator carried by the retained graph-first selected-axis surface has a
nonzero cubic trace.  That statement is scale-free.

This note proves exactly that replacement:

```text
retained graph-first selected-axis 6+2 surface
+ canonical traceless primitive U(1) generator Y0 = P_+ - 3 P_-
=> Tr[Y0] = 0 and Tr[Y0^3] = -48 != 0.
```

No `alpha = 1/3`, No GMN, No electron-charge, and No physical-SM hypercharge
identification is used.  The optional rescale `Y0/3` reproduces the familiar
`(+1/3, -1)` eigenvalues, but that rescale is not load-bearing for the ABJ
obstruction.

## Theorem

On the retained graph-first selected-axis cube surface, let `tau` be the
residual swap of the two axes complementary to the selected axis.  Define

```text
P_+ = (I + tau) / 2,
P_- = (I - tau) / 2,
Y0 = P_+ - 3 P_-.
```

Then, for every selected axis:

```text
rank(P_+) = 6,
rank(P_-) = 2,
Tr[Y0] = 6*1 + 2*(-3) = 0,
Tr[Y0^3] = 6*1^3 + 2*(-3)^3 = -48 != 0.
```

For every nonzero scale `lambda`,

```text
Tr[(lambda Y0)^3] = -48 lambda^3 != 0.
```

Thus the ABJ-relevant cubic trace is nonzero independently of the convention
used to name or normalize physical hypercharge.

## Proof

The retained graph-first selector theorem supplies a selected axis of the
taste cube.  The retained graph-first `SU(3)` integration theorem supplies the
residual complementary-axis swap `tau` and the `6+2` decomposition of the
selected-axis weak-doublet surface.  Because `tau^2 = I`, the operators
`P_+` and `P_-` above are complementary Hermitian projectors.

The graph-first theorem verifies the multiplicities:

```text
Tr(P_+) = rank(P_+) = 6,
Tr(P_-) = rank(P_-) = 2.
```

The primitive traceless abelian generator in this two-projector commutant is
`Y0 = P_+ - 3 P_-`.  Its eigenvalues are exactly `+1` on the six-dimensional
`P_+` block and `-3` on the two-dimensional `P_-` block.  Therefore

```text
Tr[Y0]   = 6 - 6 = 0,
Tr[Y0^3] = 6 - 54 = -48.
```

Scaling a generator by a nonzero `lambda` scales the cubic trace by
`lambda^3`, so the anomaly/non-anomaly dichotomy is unchanged by the choice of
normalization.  The exact-symbolic runner constructs `tau`, `P_+`, `P_-`, and
`Y0` for all three selected axes and verifies the identities above.

## Relation to the ABJ Action Theorem

The action-surface ABJ theorem only requires a nonzero chiral U(1)^3 trace.  It
does not require the physical names "quark", "lepton", or "hypercharge", and it
does not require the absolute Standard Model normalization `alpha = 1/3`.

This note therefore replaces the bounded normalization/readout dependency in
the 3+1 route with a retained-surface algebraic trace fact.  The physical
hypercharge chain remains useful for Standard Model identification, but it is
not load-bearing for the 3+1 anomaly obstruction.

## Dependencies

- [`GRAPH_FIRST_SELECTOR_DERIVATION_NOTE.md`](GRAPH_FIRST_SELECTOR_DERIVATION_NOTE.md)
  — retained selected-axis surface.
- [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)
  — retained selected-axis commutant theorem, residual swap, and `6+2`
  decomposition.

Ordinary finite-dimensional linear algebra over the explicit `8 x 8`
projector matrices is the only mathematical infrastructure used internally.

## Claim Boundary

This note closes only the scale-free cubic trace needed by ABJ:

```text
Tr[(lambda Y0)^3] != 0 for lambda != 0.
```

It does **not** claim:

- physical-SM hypercharge identification;
- the `alpha = 1/3` normalization bridge;
- GMN or electric-charge quantization;
- quark/lepton naming;
- right-handed anomaly cancellation;
- the full matter spectrum;
- any observed or Monte Carlo input.

## Audit Handoff

```yaml
proposed_claim_type: positive_theorem
actual_current_surface_status: scale-free positive theorem candidate
trace_class: direct_blocker_closure
target_claim_id: anomaly_forces_time_theorem
target_blocker_text: "The 3+1 ABJ route previously mentioned bounded physical hypercharge/readout rows where only a nonzero cubic U(1) trace was needed."
reachability_to_target: closes
bounded_alpha_or_hypercharge_row_load_bearing: false
alpha_equals_one_third_load_bearing: false
physical_sm_hypercharge_load_bearing: false
abj_relevant_trace_nonzero: true
audit_required_before_effective_status_change: true
```
