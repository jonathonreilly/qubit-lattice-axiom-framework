# Reflection-Positive Gravity Sign Gate

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-08
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:** [`scripts/gravity_sign_from_reflection_positivity_unitarity_dewitt_lambda_2026_06_08.py`](../scripts/gravity_sign_from_reflection_positivity_unitarity_dewitt_lambda_2026_06_08.py)
**Runner cache:** [`logs/runner-cache/gravity_sign_from_reflection_positivity_unitarity_dewitt_lambda_2026_06_08.txt`](../logs/runner-cache/gravity_sign_from_reflection_positivity_unitarity_dewitt_lambda_2026_06_08.txt)

## Statement

Reflection positivity constrains physical states after OS reconstruction: the
physical Hilbert inner product is positive semidefinite after null states are
quotiented. A negative-norm ghost cannot be a physical state in that Hilbert
space.

Therefore, if all of the following are supplied:

1. an emergent spin-2 TT graviton sector is identified as a physical RP
   excitation;
2. the conformal/trace wrong-sign sector is removed as gauge by an actual
   diffeomorphism or equivalent gauge structure; and
3. the source/action exchange orientation tying Newtonian attraction to healthy
   TT kinetic sign is supplied,

then the physical spin-2 branch must be the healthy branch. This is a
conditional gate, not a derivation of `G>0` from reflection positivity alone.

## DeWitt Lambda Check

For symmetric spatial two-tensors in `d=3`, use

```text
G_lambda(h,h) = h_ij h^ij - lambda (tr h)^2.
```

The TT sector is traceless, so its eigenvalue is positive and independent of
`lambda`. The trace weight is proportional to `1 - lambda d`.

- At the GR control value `lambda=1`, TT and trace have opposite signs. The
  trace/conformal sign is acceptable only if the conformal mode is gauge, not a
  physical ghost.
- At the no-conformal-term control `lambda=0`, trace and TT have the same sign.
  This is not the GR `lambda=1` split.
- At `lambda=1/d`, the trace direction is degenerate. This is also not the GR
  `lambda=1` split.

The existing universal-GR blocker remains load-bearing: the framework has not
yet derived the needed lambda-one/diffeomorphism gauge structure.

## Relation to the Gravity-Sign Chain

- [`GRAVITY_ATTRACTION_SIGN_FROM_SOURCE_POSITIVITY_AND_SYMMETRIC_MEDIATOR_NARROW_THEOREM_NOTE_2026-06-08.md`](GRAVITY_ATTRACTION_SIGN_FROM_SOURCE_POSITIVITY_AND_SYMMETRIC_MEDIATOR_NARROW_THEOREM_NOTE_2026-06-08.md)
  gives the bounded source/action exchange-sign reduction.
- [`GRAVITY_SIGN_IS_ONE_RESIDUAL_AT_THE_TT_KERNEL_BLOCK_NARROW_THEOREM_NOTE_2026-06-08.md`](GRAVITY_SIGN_IS_ONE_RESIDUAL_AT_THE_TT_KERNEL_BLOCK_NARROW_THEOREM_NOTE_2026-06-08.md)
  locates the scalar-`W` TT-kernel boundary and leaves geometric/full
  stress-response/RP-unitarity routes open.
- [`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md)
  supplies the reflection-positive Hilbert-space input.
- [`UNIVERSAL_GR_SUPERMETRIC_NORMAL_FORM_NOTE.md`](UNIVERSAL_GR_SUPERMETRIC_NORMAL_FORM_NOTE.md)
  records the current supermetric blocker.

This note only packages the RP/unitarity side of the route map. It does not
turn the open diffeomorphism/gauge structure into an established theorem.

## No-Go Discipline Boundary

**Status:** PASS for the local negative statement only: RP alone does not close
the gravity sign. No global no-go is shipped.

- **N1 - Alternative routes.** Five routes remain distinguished: scalar-`W`
  Hessian, static source/action exchange, full stress response, geometric
  Regge/EH action, and RP/unitarity with diffeomorphism gauge. This note only
  conditions the last route.
- **N2 - Wall independence.** Physical RP embedding of TT modes, conformal
  gauge removal, and source/action orientation are independent requirements.
  None is collapsed into RP alone.
- **N3 - Hidden-wall scan.** "Physical RP mode," "diffeomorphism," and
  "source/action orientation" are explicit open inputs, not baseline axioms or
  primitives.
- **N4 - Residual matching.** The matched residual is the healthy spin-2
  kinetic branch. The note does not claim to derive the geometric coefficient.
- **N5 - Rhetoric audit.** "Forbids a ghost" means forbids physical
  negative-norm states in the reconstructed physical Hilbert space. It does not
  forbid an unphysical gauge conformal direction.
- **N6 - Partial-closure path scan.** A retained diffeomorphism/gauge theorem
  or retained geometric action calculation could retire this gate without a new
  axiom.
- **N7 - Steelman.** A hostile reviewer can say the hard part is precisely
  showing that the emergent graviton is a physical RP TT mode and that the
  conformal sector is gauge. The note accepts that as the open work.
- **N8 - Cross-cycle echo.** This preserves the current universal-GR
  supermetric blocker and does not convert a conditional route into closure.

## What Is Not Claimed

- no unconditional derivation of `G>0`;
- no derivation of emergent diffeomorphism invariance;
- no derivation of a lambda-one DeWitt supermetric from the framework;
- no derivation of the source/action orientation;
- no new primitive, axiom, Tier-A admission, registered scale, or fitted value;
- no claim that Record, the scale-reference primitive, or the
  kinetic-isotropy primitive supplies gravitational dynamics.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/gravity_sign_from_reflection_positivity_unitarity_dewitt_lambda_2026_06_08.py
```
