# Hierarchy D4 Density-Scale Readout Bridge Bounded Theorem Note

**Date:** 2026-06-16
**Claim type:** bounded_theorem
**Status:** bounded support theorem source proposal; independent audit lane
ratifies effective status.
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:** `scripts/frontier_hierarchy_d4_density_scale_readout_bridge_2026_06_16.py`

## 2026-06-18 endpoint-algebra hardening

This repair removes the bridge runner's dependence on the audit-ledger status
of `HIERARCHY_EFFECTIVE_POTENTIAL_ENDPOINT_NOTE.md`. The endpoint note remains
useful context, but the load-bearing endpoint ratios used here are now
recomputed inside this packet from the APBC small-m coefficient formula

```text
A(L_t) = (1 / (2 L_t u_0^2)) * Sum_omega 1 / (3 + sin^2 omega).
```

The verifier checks directly that

```text
A_2 = 1/(8 u_0^2),      A_4 = 1/(7 u_0^2),
A_inf = 1/(4 sqrt(3) u_0^2),
```

and hence `A_2/A_4 = 7/8` and `A_inf/A_2 = 2/sqrt(3)`. These are source-side
algebraic checks in this bridge packet, not an audit-status import from the
endpoint row. The upstream Matsubara free-energy formula and the physical
electroweak order-parameter/VEV identification remain separately scoped; no
new axiom, Tier-A admission, observed target, fitted coefficient, or audit
verdict is introduced.

## Claim

This note supplies the narrow source-side bridge requested by the current
hierarchy-dimensional-compression audit blocker:

> derive the D=4 determinant/effective-potential-density readout bridge fixing
> exponent, inverse/direct placement, sign, and normalization before promoting
> beyond conditional arithmetic support.

The exact theorem here is the fixed positive D=4 density-coefficient readout:

```text
rho_* = A(L) v(L)^4,   rho_* > 0,   A(L) > 0.
```

For any reference endpoint `L_ref`,

```text
v(L) / v(L_ref) = (A_ref / A(L))^(1/4),
where A_ref := A(L_ref).
```

This fixes the four pieces named by the audit blocker:

- **exponent:** the fourth root comes from the retained dimensional algebra
  theorem for a dimension-four positive density;
- **placement:** the coefficient is in the denominator of the scale readout,
  so the ratio is `A_ref / A(L)`, not `A(L) / A_ref`;
- **sign:** if `A(L) > A_ref`, then `v(L) < v(L_ref)`, so the correction is a
  downward compression;
- **normalization:** the reference endpoint is exactly normalized, because
  `v(L_ref) / v(L_ref) = 1`.

This bridge does not identify the electroweak VEV with that fixed-density
readout. It supplies the algebraic insertion map once a downstream physical
order-parameter theorem names the fixed density `rho_*` and identifies the
relevant `A(L)` surface. No observed target value, fitted coefficient, new
axiom, or textbook import is load-bearing here.

## Proof

Assume two positive endpoints satisfy the same fixed D=4 density readout:

```text
rho_* = A_ref v_ref^4 = A(L) v(L)^4.
```

Since all quantities are positive,

```text
v(L)^4 / v_ref^4 = A_ref / A(L).
```

Taking the unique positive fourth root gives

```text
v(L) / v_ref = (A_ref / A(L))^(1/4).
```

The baseline normalization follows by setting `A(L) = A_ref`, giving ratio
`1`. If `A(L) > A_ref`, then `A_ref / A(L) < 1`, hence the positive fourth
root is also below `1`: the scale is compressed downward. If `A(L) < A_ref`,
the same formula gives an upward rescaling. This is exact algebra on positive
reals plus the retained `D = 4` fourth-root dimensional theorem.

## Endpoint Applications

The endpoint coefficient ratios are recomputed in this packet from the APBC
small-m coefficient formula. Existing endpoint notes are cited in parallel for
context; their live audit status is not load-bearing on this bridge verifier.

### L_t = 4 Matsubara Endpoint

The effective-potential endpoint note gives

```text
A_2 = 1 / (8 u_0^2),
A_4 = 1 / (7 u_0^2).
```

Therefore

```text
A_2 / A_4 = 7/8
```

and the fixed-density bridge gives

```text
v_4 / v_2 = (A_2 / A_4)^(1/4) = (7/8)^(1/4) < 1.
```

The sign and placement are therefore forced within this readout: the
`L_t = 4` endpoint has the larger coefficient, so the scale correction is the
inverse fourth-root compression relative to `L_t = 2`.

### Temporal-Average Scalar Endpoint

The scalar `3+1` temporal ratio theorem gives the exact ratio

```text
A_inf / A_2 = 2 / sqrt(3).
```

The same fixed-density bridge gives

```text
v_inf / v_2 = (A_2 / A_inf)^(1/4)
            = (sqrt(3) / 2)^(1/4)
            = (A_inf / A_2)^(-1/4) < 1.
```

This is the exact algebraic version of the `R^(-1/4)` placement used by
`HIERARCHY_DIMENSIONAL_COMPRESSION_NOTE.md` when `R` is a positive endpoint
coefficient ratio.

## Dependencies

Graph-visible dependencies:

- [`HIERARCHY_DIMENSIONAL_FOURTH_ROOT_COMPRESSION_NARROW_THEOREM_NOTE_2026-05-10.md`](HIERARCHY_DIMENSIONAL_FOURTH_ROOT_COMPRESSION_NARROW_THEOREM_NOTE_2026-05-10.md)
  -- retained dimensional algebra for the `D = 4` fourth-root exponent.

Downstream target:

- `docs/HIERARCHY_DIMENSIONAL_COMPRESSION_NOTE.md`
  -- current audited-conditional consumer, named as plain context rather than
  a graph-visible dependency. This bridge supplies the
  coefficient-to-scale insertion algebra for re-audit, but it does not itself
  promote that parent row.

Parallel context pointers, not load-bearing status dependencies:

- `HIERARCHY_MATSUBARA_FREE_ENERGY_DENSITY_NARROW_THEOREM_NOTE_2026-05-16.md`
  -- derivation of the APBC free-energy density formula used as upstream
  formula context.
- `HIERARCHY_EFFECTIVE_POTENTIAL_ENDPOINT_NOTE.md`
  -- prior endpoint-algebra packet for `A_2`, `A_4`, and `A_inf`.
- `SCALAR_3PLUS1_TEMPORAL_RATIO_NOTE.md`
  -- independent retained scalar endpoint ratio `A_inf / A_2 = 2/sqrt(3)`.

## Boundary

This bridge closes the fixed-density coefficient-to-scale algebra. It does not
close the broader hierarchy formula.

Still open for a full physical VEV theorem:

1. identify the electroweak order parameter as the framework's fixed
   positive D=4 density readout;
2. prove which endpoint coefficient surface supplies the physical `A(L)`;
3. tie the absolute `L_t = 2` normalization to the broader hierarchy chain;
4. settle any radiative or continuum corrections outside the finite endpoint
   algebra.

Until those are supplied and independently audited, downstream rows should cite
this note only as bounded support for the exponent, inverse/direct placement,
sign, and reference normalization of the D=4 density-scale map.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_hierarchy_d4_density_scale_readout_bridge_2026_06_16.py
```

Expected final line:

```text
TOTAL: PASS=17 FAIL=0
```

## Audit Handoff

```yaml
claim_id: hierarchy_d4_density_scale_readout_bridge_bounded_theorem_note_2026-06-16
note_path: docs/HIERARCHY_D4_DENSITY_SCALE_READOUT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md
runner_path: scripts/frontier_hierarchy_d4_density_scale_readout_bridge_2026_06_16.py
proposed_claim_type: bounded_theorem
proposed_load_bearing_step_class: A
status_authority: independent audit lane only
audit_required_before_effective_status_change: true

graph_visible_one_hop_deps:
  - hierarchy_dimensional_fourth_root_compression_narrow_theorem_note_2026-05-10

target_consumer:
  - hierarchy_dimensional_compression_note

forbidden_imports_used: false
observed_target_used_in_pass_conditions: false
proposal_allowed: false
proposal_allowed_reason: "The bridge fixes the D=4 coefficient-to-scale map, but a later physical order-parameter theorem must still identify the electroweak VEV with the fixed-density readout."
```
