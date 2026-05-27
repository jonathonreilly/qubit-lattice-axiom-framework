# alpha_s Derived Narrow Theorem (Retained Algebra Relay)

**Date:** 2026-05-10 (scope repaired 2026-05-27)
**Type:** positive_theorem
**Claim scope:** an exact algebraic relay from the already audited-clean
retained tadpole-improvement algebra packet to the two identities formerly
carried here as a conditional CMT import.

The only load-bearing cited dependency is the retained theorem
[`ALPHA_S_TADPOLE_IMPROVEMENT_VERTEX_POWER_NARROW_THEOREM_NOTE_2026-05-10.md`](ALPHA_S_TADPOLE_IMPROVEMENT_VERTEX_POWER_NARROW_THEOREM_NOTE_2026-05-10.md).
That retained packet proves, over abstract positive reals
`(alpha_bare, u_0)`, the definitions

```text
alpha_LM    := alpha_bare / u_0,                                      (D1)
alpha_s(v)  := alpha_bare / u_0^2,                                    (D2)
```

and their exact algebraic consequences. This repaired note does not ask the
auditor to import CMT or `n_link` physics from the older EW-color-projection
surface. It records only the downstream identities that follow after the
retained algebra packet has supplied `(D1)` and `(D2)`.

**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:** [`scripts/frontier_alpha_s_derived_narrow_retained_algebra_repair.py`](./../scripts/frontier_alpha_s_derived_narrow_retained_algebra_repair.py)

## Statement

Let `alpha_bare` and `u_0` be abstract positive real symbols. Define
`alpha_LM` and `alpha_s(v)` exactly as in the retained tadpole-improvement
vertex-power theorem:

```text
alpha_LM    := alpha_bare / u_0,
alpha_s(v)  := alpha_bare / u_0^2.
```

Then the following identities hold exactly in
`Q(alpha_bare, u_0, 1/u_0)`:

```text
alpha_LM^2              = alpha_bare * alpha_s(v),                    (P1)
alpha_s(v) / alpha_LM   = 1 / u_0,                                    (P2)
alpha_s(v)^2 / alpha_LM^4 = 1 / alpha_bare^2,                         (C1)
alpha_LM / alpha_bare   = 1 / u_0,                                    (C2)
alpha_s(v) / alpha_bare = 1 / u_0^2,                                  (C3)
alpha_LM^2 / alpha_s(v) = alpha_bare.                                 (C4)
```

## Proof

Pure substitution from `(D1)` and `(D2)`.

For `(P1)`:

```text
alpha_LM^2 = (alpha_bare / u_0)^2
           = alpha_bare^2 / u_0^2
           = alpha_bare * (alpha_bare / u_0^2)
           = alpha_bare * alpha_s(v).
```

For `(P2)`:

```text
alpha_s(v) / alpha_LM = (alpha_bare / u_0^2) / (alpha_bare / u_0)
                      = 1 / u_0.
```

The corollaries `(C1)`-`(C4)` are the same substitution and rearrangement
steps.

## Repair Relative To The Prior Conditional Verdict

The prior audit verdict correctly rejected this row because it cited
`YT_EW_COLOR_PROJECTION_THEOREM.md` as a retained source for CMT tadpole-power
coupling inputs, while the current audited scope of that EW row is a
`kappa_EW` family/no-go boundary and does not supply those inputs.

This repair removes that import. The row no longer claims that the EW
color-projection surface supplies CMT identities, `n_link = (1, 2)`, or
physics readouts. The retained dependency now supplies only the exact
abstract algebraic definitions `(D1)` and `(D2)`, and this note proves only
the identities listed above.

## What This Claims

- Exact algebraic identities `(P1)`, `(P2)`, and `(C1)`-`(C4)` over abstract
  positive real symbols.
- A narrow relay from the retained tadpole-improvement algebra packet into the
  historical `alpha_s_derived_narrow` row.

## What This Does Not Claim

- No derivation of a CMT change-of-variables identity.
- No derivation of an `n_link = 1` or `n_link = 2` operator count.
- No value of `u_0`, `<P>`, `alpha_bare`, `alpha_s(v)`, or `alpha_s(M_Z)`.
- No Wilson plaquette analytic insertion, Wilson-loop static-potential
  measurement, low-energy running bridge, or Standard-Model strong-coupling
  identification.
- No use of PDG observations, comparison data, fitted selectors, or admitted
  unit conventions.

## Relation To The Parent alpha_s Row

The broad `ALPHA_S_DERIVED_NOTE.md` still bundles this algebraic identity with
additional bounded or open surfaces: the plaquette/u0 lane, bare-normalization
choices, the downstream running bridge to `M_Z`, and numerical readouts. This
repaired narrow note does not promote that parent row. It only makes the
historical narrow algebra row auditable against a retained algebraic
dependency instead of a mis-scoped CMT import.

## Cited Dependencies

- [`ALPHA_S_TADPOLE_IMPROVEMENT_VERTEX_POWER_NARROW_THEOREM_NOTE_2026-05-10.md`](ALPHA_S_TADPOLE_IMPROVEMENT_VERTEX_POWER_NARROW_THEOREM_NOTE_2026-05-10.md)
  - audited-clean retained algebra over abstract positive reals, including the
    definitions `(D1)` and `(D2)` and the geometric-mean / constant-ratio
    consequences.

## Validation

Primary runner
[`scripts/frontier_alpha_s_derived_narrow_retained_algebra_repair.py`](./../scripts/frontier_alpha_s_derived_narrow_retained_algebra_repair.py)
performs exact symbolic checks that:

1. the repaired note and retained dependency are present;
2. the retained dependency contains the two source definitions;
3. `(P1)`, `(P2)`, and `(C1)`-`(C4)` reduce to zero residuals under sympy;
4. the repaired note no longer contains a markdown dependency on the prior
   EW-color-projection row;
5. no numerical plaquette, running, or Standard-Model input is consumed.
