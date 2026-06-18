# Gate B GB-S3 Lattice Forward-Stencil Bridge

```yaml
actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This splits and partially closes the Gate B GB-S3 connectivity ingredient by deriving the label/offset-preserving forward stencil as a finite-range Z^3 relation. It does not derive Gate B dynamics closure or the physical gravity/readout bridge."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

**Date:** 2026-06-18
**Type:** bounded-support bridge
**Runner:** [`scripts/gate_b_gb_s3_lattice_forward_stencil_bridge_2026_06_18.py`](../scripts/gate_b_gb_s3_lattice_forward_stencil_bridge_2026_06_18.py)

## Claim

Split the Gate B generated-connectivity ingredient `GB-S3` into:

- `GB-S3a`: the label/offset-preserving forward stencil used by the
  positive Gate B generated-geometry rows.
- `GB-S3b`: the remaining physical/growth-rule question of why this
  stencil, layer axis, embedding update, and readout package are selected
  as Gate B dynamics.

`GB-S3a` is a native finite-range relation on the Lattice axiom surface.
Given the `Z^3` site set with standard translation action and finite-range
locality, and given a supplied forward layer axis from the Gate B
propagation packet, define

```text
(x,y,z) -> (x+1, y+dy, z+dz),   dy,dz in {-1,0,1}.
```

Every edge in this relation is a finite-range `Z^3` dependency with
Manhattan range at most `3`, and the interior offset set is translation
covariant in the two transverse directions. This retires the narrow
reading of `GB-S3` as an arbitrary row-local generated-connectivity rule
for the label/offset-preserving stencil.

## Proof Sketch

The Lattice axiom supplies `Z^3`, its standard translation action, and
finite graph-distance locality. Once the Gate B packet supplies a forward
layer direction, the displayed relation is the finite offset cylinder

```text
Delta = {(1,dy,dz) : dy,dz in {-1,0,1}}.
```

For every `delta in Delta`, the graph-distance on cubic `Z^3` is

```text
|1| + |dy| + |dz| <= 3.
```

Thus the rule is finite-range local. Translation by any transverse
interior vector preserves the same offset set, so the relation is not a
coordinate-fitted KNN rule and not a row-local graph import.

The generated coordinates used by the Gate B runners may drift or restore
as an embedding, but this bridge concerns the label-inherited adjacency.
Coordinate recomputation rules such as KNN are separate control rules and
can disagree with the label stencil under drift.

## Boundaries

- `GB-S3b remains open`: this bridge does not derive why the full Gate B
  dynamics should select this stencil as physical generated geometry.
- This does not derive Gate B dynamics closure.
- This does not derive `GB-S1b`, the Gate B scalar normalization,
  finite-core regulator, or source strength.
- This does not derive `GB-S2`, the propagation/readout semantics,
  detector-window rule, `TOWARD` sign, or `F~M` readout.
- This does not introduce a new axiom, Tier-A admission, observed
  comparator, or audit-status change.

## Verification

Run:

```text
python3 scripts/gate_b_gb_s3_lattice_forward_stencil_bridge_2026_06_18.py
```

Expected summary:

```text
TOTAL: PASS=9 FAIL=0
```
