# Flavor Supplied Heat-Kernel Arrow r=1/2 Stability Boundary (Bounded Route-Pruning Theorem)

**Date:** 2026-06-04
**Claim type:** bounded_theorem
**Claim scope:** conditional algebraic route-pruning for the two one-dimensional
flow maps

```text
sharpen(r) = 2 r^2,
thermalize(r) = sqrt(r/2),
```

and the explicitly supplied heat-kernel/blocking path

```text
r(t) = tanh(t)^4.
```

On that supplied path, `r=1/2` is a transit value and not an attractor.
The theorem does not derive `r(t)=tanh(t)^4` from the framework baseline,
from the single-clock theorem, or from a retained generation-sector beta
theorem. It therefore does not prove that the framework-native dynamics
anti-favors `Q=2/3`; it only prunes the route that assumes the supplied
heat-kernel path is the relevant arrow and then expects that arrow to
attract `r` to `1/2`.

**Status authority:** independent audit lane only. This source note does
not set or predict an audit verdict; effective status is pipeline-derived
after independent audit.
**Runner:** [`scripts/native_arrow_resolution.py`](../scripts/native_arrow_resolution.py)
**Cache:** [`logs/runner-cache/native_arrow_resolution.txt`](../logs/runner-cache/native_arrow_resolution.txt)

## Motivation

Two existing flavor-flow notes pull against each other:

- `FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02` studies a
  sharpening map and reads `r=1/2` as an unstable separatrix.
- `FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02` studies a
  thermalizing map and reads `r=1/2` as a stable attractor.

The runner verifies that these are inverse branches of the same
one-dimensional map family. Thus the stability contradiction is not an
algebraic contradiction: it is an arrow-selection question.

The live audit history for `FLAVOR_NATIVE_BETA_NO_HALF_ATTRACTOR_NOTE_2026-05-30`
already identified the key wall: the `tanh(t)^4` path is supplied, not
derived as an exhaustive native beta law. This note adopts that boundary
instead of restating the broader no-go.

## Statement

Let `r = |b|^2/a^2` on the positive real C3-circulant Koide line, so that
[`KOIDE_LIGHTCONE_PRIMITIVE_THEOREM_NOTE_2026-05-10.md`](KOIDE_LIGHTCONE_PRIMITIVE_THEOREM_NOTE_2026-05-10.md)
supplies the algebraic identification `Q=2/3` iff `r=1/2`.

1. `sharpen(r)=2r^2` and `thermalize(r)=sqrt(r/2)` are exact inverse
   branches on `r>0`.
2. Both maps have fixed points `{0, 1/2}`. At `r=1/2`,
   `sharpen'(1/2)=2` and `thermalize'(1/2)=1/2`, so the same point is
   repelling for the sharpening branch and attracting for the
   thermalizing branch.
3. For the supplied heat-kernel/blocking path `r(t)=tanh(t)^4`,
   `dr/dt = 4 tanh(t)^3 sech(t)^2 > 0` for finite `t>0`, with
   endpoint limits `r(0)=0` and `lim_{t->infty} r(t)=1`.
4. Therefore `r=1/2` is a transit value of the supplied heat-kernel path,
   not a fixed point or attractor of that path.

This is a conditional route-pruning theorem: under the supplied
heat-kernel path, the path does not dynamically select `Q=2/3`.

## Proof Sketch

The inverse-map identities are direct:

```text
thermalize(sharpen(r)) = sqrt((2 r^2)/2) = r,
sharpen(thermalize(r)) = 2 (sqrt(r/2))^2 = r.
```

Solving `2r^2=r` and `sqrt(r/2)=r` gives the same fixed set `{0, 1/2}`.
The derivatives at `1/2` are respectively `2` and `1/2`, so stability
flips with arrow reversal.

For the supplied path,

```text
d/dt tanh(t)^4 = 4 tanh(t)^3 sech(t)^2.
```

For finite `t>0`, both factors are positive. The unique time where
`tanh(t)^4 = 1/2` has positive derivative, so `r=1/2` is crossed rather
than selected.

The paired runner verifies these identities exactly with `sympy`, checks
the sampled monotonicity of the supplied path, and records a non-load-bearing
block-dimension consistency check.

## Import Discipline

The following are not delivered by this note:

- a derivation that the generation-sector framework-native beta function is
  `r(t)=tanh(t)^4`;
- an exhaustion theorem excluding other C3-symmetric beta functions with a
  generic fixed point at `r=1/2`;
- a proof that the physical charged-lepton flow follows the sharpening branch;
- a proof that `Q=2/3` is wrong or unreachable;
- a retirement of the `AC_phi_lambda` / det_C / block-counting input.

The open bridge is explicit: to promote this route beyond bounded support,
the repo needs a retained derivation of the generation-sector native beta
law, or a retained theorem showing that the physical coarse-graining is the
supplied heat-kernel path rather than the thermalizing/block-counting path.

No measured values, fitted selectors, new axioms, or new framework primitives
are consumed.

## Bounded-Wall / No-Go Discipline Gate (N1-N8)

Gate result: PASS for the narrowed bounded theorem. The broader source-branch
claim that "the retained native dynamics anti-favors `Q=2/3`" does not pass
and is not landed here.

- **N1 alternative routes.** The exact inverse-map route is closed by algebra;
  the supplied heat-kernel path route is closed only under its stated path
  assumption; deriving that path from the single-clock theorem remains open;
  a block-counting thermalizer can still select `r=1/2` if its physical
  premise is supplied; and a T-odd/chiral installer could still provide the
  missing coarse-graining. These are distinct routes.
- **N2 wall independence.** The collapsed wall is the native-beta/coarse-
  graining bridge. The inverse-map algebra and the derivative of a supplied
  path do not close that bridge.
- **N3 hidden walls.** Phrases such as "native", "heat-kernel", and
  "blocking" are treated as labels for the supplied path unless backed by a
  linked retained theorem. No baseline axiom or approved primitive supplies
  this generation-sector beta law.
- **N4 residual matching.** The residual matches the prior audit warning for
  `FLAVOR_NATIVE_BETA_NO_HALF_ATTRACTOR_NOTE_2026-05-30`: hard-coding
  `tanh(t)^4` is not a derivation of a native beta law. This note narrows to
  the algebraic transit check that warning allowed.
- **N5 rhetoric audit.** The note does not say `Q=2/3` is false, impossible,
  or globally ruled out. It only says the supplied heat-kernel path does not
  attract `r` to `1/2`.
- **N6 partial-closure path.** A future retained native-beta derivation or
  retained T-odd/chiral/block-counting installer could change the route
  status without adding a new axiom or primitive.
- **N7 steelman.** A hostile reviewer can accept every runner line while
  rejecting the broader no-go: a different retained physical arrow, or a
  retained proof that the charged-lepton sector uses block-counting
  coarse-graining, could still make `r=1/2` dynamically selected.
- **N8 cross-cycle echo.** This is the same wall already surfaced by the
  prior native-beta audit. The repair mechanism is scope narrowing, not
  calling the wall an axiom fact.

## Boundary

This note is safe as bounded algebraic route-pruning. It is not a retained
native-arrow theorem, not a no-go against Koide, and not a claim that the
framework baseline by itself selects or rejects `Q=2/3`.
