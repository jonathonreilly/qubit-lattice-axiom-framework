# Flavor Latitude Quantizer And RP Self-Dual Boundary: Repaired Trace/Center Packet

**Original date:** 2026-05-30
**Repair date:** 2026-06-06
**Claim type:** bounded_theorem / demotion boundary
**Status authority:** independent audit lane only. This source note does not
set an audit verdict or effective status.
**Primary runner:** [`scripts/flavor_latitude_quantizer_and_rp_selfdual_2026_05_30.py`](../scripts/flavor_latitude_quantizer_and_rp_selfdual_2026_05_30.py)
**Cached runner output:** [`logs/runner-cache/flavor_latitude_quantizer_and_rp_selfdual_2026_05_30.txt`](../logs/runner-cache/flavor_latitude_quantizer_and_rp_selfdual_2026_05_30.txt)

## Scope

This repair narrows the old latitude-quantizer note to the source facts that are
actually certified by the restricted packet. It does not claim a native
derivation of `r=1/2`, `Q=2/3`, a charged-lepton value, or a framework-selected
mass readout.

The old broad note had two problems that are repaired here:

- The RP "self-dual" route was already refuted as a circular `|b|`-coordinate
  choice, but the source still preserved too much of the self-dual framing.
- The operator-algebra reframe incorrectly classified the equal center state
  and suggested that trace alone uniquely forced a full-algebra weighting.

The repaired packet keeps only a narrow demotion/boundary result.

## Certified Negative Boundary

The runner verifies that the cube-angle and finite-idempotent routes do not
provide a native latitude quantizer:

- `cos^2((1,1,1),(1,1,0)) = 2/3` is real geometry, but it is a value
  coincidence in generation-space geometry, not a canonical map to the
  `(a,|b|)` operator latitude.
- `M_2(C)` idempotent trace/dimension ratios are `{0, 1/2, 1}`; `2/3` is not
  hosted there. The native `2/3` remains the `R[Z3]` doublet/total dimension
  reading, not an `r=1/2` derivation.

N2/N3 historical broad claims are not certified by this repaired packet. In
particular, the old gap-equation and entanglement/Fisher-extremum prose is not
load-bearing here. A future packet may separately prove or refute those claims,
but this source repair does not rely on them.

## RP Self-Dual Route Is Refuted

For `H = aI + b(J-I)` with `a > 0`, the reflection-positivity edges are signed:

```text
singlet-null edge: b = -a/2
doublet-null edge: b = +a
```

The multiplicative inversion on `|b|` swaps the edge magnitudes and fixes
`|b| = a/sqrt(2)`, so it gives `r = |b|^2/a^2 = 1/2` only after discarding
the sign of `b`. On the signed line it is not a native singlet-doublet duality.

The runner also checks that different fixed-point conventions give different
answers:

```text
|b| geometric point:       r = 1/2
|b| arithmetic midpoint:   r = 9/16
signed-affine midpoint:    r = 1/16
```

Therefore the RP self-dual route is a coordinate/functional choice, not a
framework-native derivation of `r=1/2`.

## Corrected Trace/Center Statement

As a real algebra,

```text
A = R[Z3] = R + C
```

is commutative. Hence an equal central-idempotent state is tracial. The repaired
statement is:

- the equal central-idempotent state is tracial;
- the regular/Plancherel state is also tracial;
- trace property alone does not select between these functionals;
- a canonical `r=1/2` result would require an additional framework-native
  selector for the equal-center/block-count functional.

The runner checks both positive tracial functionals on `R + C`:

```text
phi_equal(x,z)   = (x + Re z)/2
phi_regular(x,z) = (x + 2 Re z)/3
```

They are distinct and both satisfy `phi(xy)=phi(yx)` because the algebra is
commutative.

## Metric Boundary

The runner verifies the Hilbert-Schmidt metric identity

```text
Tr(I^T I) = 3,    Tr((J-I)^T(J-I)) = 6,    Tr(I^T(J-I)) = 0.
```

This supports the readout boundary:

```text
block-equal reading:      r = 1/2 -> Q = 2/3
per-real-mode reading:    r = 1   -> Q = 1
```

The metric identity does not choose between those readings. This is consistent
with the audit-clean companion
[`FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02.md`](FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02.md),
which keeps the doublet metric/default result readout-neutral.

## Reproduce

```text
PYTHONPATH=scripts python3 scripts/flavor_latitude_quantizer_and_rp_selfdual_2026_05_30.py
```

Expected current scorecard:

```text
SCORECARD PASS=14 FAIL=0
```

## Boundaries

- This packet is a demotion/source-boundary repair, not a positive
  charged-lepton value derivation.
- It does not derive a native latitude quantizer.
- It does not prove the old N2/N3 gap-equation or entanglement/Fisher claims.
- It does not choose `det_C`/block-count over `det_R`/per-real-mode readout.
- It introduces no new axiom.
