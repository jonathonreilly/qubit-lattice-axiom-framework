# Kinetic Isotropy B4/S4 Transitivity Route No-Go

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-06-20
**Claim type:** no_go
**Type:** no_go
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.

**Primary runner:**
[`scripts/kinetic_isotropy_b4_transitivity_route_no_go_2026_06_20.py`](../scripts/kinetic_isotropy_b4_transitivity_route_no_go_2026_06_20.py)
**Cached runner output:**
[`logs/runner-cache/kinetic_isotropy_b4_transitivity_route_no_go_2026_06_20.txt`](../logs/runner-cache/kinetic_isotropy_b4_transitivity_route_no_go_2026_06_20.txt)

## Claim

The approved
[`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
declares the structural OS0 kinetic-form isotropy `c_t = c_s`. This note does
not amend, narrow, retire, or re-approve that primitive.

It closes only a route class: deriving `c_t = c_s` by treating the four
Euclidean axes as already `B4`/`S4`-equivalent is circular. Spatial cubic
symmetry supplies an `O_h`-invariant kinetic form with two independent
coefficients, and the missing time-space exchange is a metric symmetry exactly
when `c_t = c_s`. A positive-transfer free-scalar witness also shows that
reflection positivity and square geometry do not, by themselves, select
`c_t = c_s`.

## Certified Facts

Let the diagonal quadratic kinetic form be
`Q(p) = sum_mu c_mu p_mu^2`, with metric
`G = diag(c_t, c_s, c_s, c_s)` on axes `(t, x, y, z)`.

**C1. Invariant-dimension wall.** On diagonal quadratic forms, and on the full
10-dimensional space of symmetric `4x4` matrices, the spatial cubic group `O_h`
(signed permutations of the three spatial axes, time fixed; `|O_h| = 48`)
leaves a two-dimensional invariant space. The independent coefficients are
`c_t` and `c_s`. The full hypercubic group `B4` (signed permutations of all four
axes; `|B4| = 384`) collapses the invariant space to one dimension, `c_t =
c_s`.

**C2. Circularity certificate.** The missing generator is the time-space swap
`W`, for example `t <-> x`. A purely spatial swap is a symmetry of `G` for all
`(c_t, c_s)`, but

```text
W^T G W - G = diag(c_s - c_t, c_t - c_s, 0, 0),
```

which vanishes exactly when `c_t = c_s`. Therefore a derivation that assumes
the time-space swap is already a metric symmetry assumes the target equality.
Axis-label transitivity is not a derivation of metric equality.

**C3. Reflection-positivity witness.** On a geometrically square lattice
(`a = 1` on all four axes), the runner gives an anisotropic free Euclidean
scalar witness with `c_t != c_s` whose transfer eigenvalues lie in `(0, 1)` on
the tested finite mode grid and whose OS reflection Gram matrices are positive
semidefinite up to numerical tolerance. This witness refutes the route
"reflection positivity plus square geometry selects `c_t = c_s`"; it does not
derive a replacement normalization.

## Boundary

- This is a route no-go, not a derivation of `c_t = c_s`.
- It does not update the registered kinetic-isotropy primitive, the primitive
  registry, or Tier-A admissions.
- The approved primitive is unchanged and not retired here.
- It does not import the past hypothesis, a time-direction admission, a
  clock-rate normalization, a Wick-rotation rule, a probability rule, a
  dynamics, a source/action, a scale, or an empirical comparator.
- It does not say no future metric-layer theorem can derive `c_t = c_s`; it
  says the `B4`/`S4` transitivity route and the tested reflection-positivity
  route do not derive it without already supplying the missing metric equality.

## No-Go Discipline Gate

Gate result: PASS for this narrow route no-go.

- N1 alternative routes checked: spatial `O_h` invariance, full `B4`
  transitivity, axis-label `S4` relabeling, square lattice geometry,
  reflection positivity/positive transfer, and scale/reference normalization.
  The first leaves two coefficients, the next two assume the time-space metric
  swap, the geometry and positivity witness allow anisotropic examples, and the
  approved scale primitive supplies no dimensionless kinetic ratio.
- N2 wall-independence: no inflated independent wall set is claimed. The closed
  target is one route class plus the positive-transfer witness route; a future
  metric-layer theorem remains open.
- N3 hidden-wall scan: "B4", "S4", "square geometry", "reflection positivity",
  "normalization", and "primitive" are explicit boundaries. No hidden
  dynamics, clock-rate rule, or past-hypothesis input is used.
- N4 residual matching: the residual matches the kinetic-isotropy primitive
  note's stated gap, namely that spatial cubic symmetry, reflection positivity,
  scale, records' causal order, and single-clock structure do not fix the
  dimensionless kinetic-form ratio.
- N5 rhetoric audit: the no-go is not "kinetic isotropy is impossible" and not
  "all derivations fail". It is only the B4/S4 transitivity route and the
  positive-transfer selection route.
- N6 partial-closure scan: the primitive registry was checked. The approved
  primitive remains an accepted premise and is not treated as a bounded import;
  this note does not propose a new primitive or claim to retire the existing
  primitive.
- N7 steelman: a future non-circular metric-layer theorem could identify a
  canonical emergent tick normalization and derive `c_t = c_s` without assuming
  the time-space metric swap. This note leaves that route open.
- N8 cross-cycle echo: nearby kinetic-isotropy, spatial-anisotropy, and
  primitive-registry notes already separate accepted primitives from bounded
  imports and separate route closures from retained derivations. This note
  preserves that boundary.

## Inputs

- [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  declares the approved primitive whose attempted transitivity derivation is
  being fenced off.
- [`SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md`](SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md)
  records the earlier `O_h` versus `B4` gate.
- [`SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md`](SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md)
  supplies the retained single-clock generator scope; it does not fix the
  kinetic-form ratio.
- [`ALLORDERS_B4_MARGINAL_PROTECTION_SYMMETRY_THEOREM_NOTE_2026-06-14.md`](ALLORDERS_B4_MARGINAL_PROTECTION_SYMMETRY_THEOREM_NOTE_2026-06-14.md)
  consumes a `B4`-symmetric kinetic surface; it does not derive that surface.

## Reproduce

```bash
python3 scripts/kinetic_isotropy_b4_transitivity_route_no_go_2026_06_20.py
# expect: TOTAL: PASS=18 FAIL=0
```
