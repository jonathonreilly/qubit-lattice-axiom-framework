# Gravity Sign Residual at the Scalar-W TT Kernel

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-08
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:** [`scripts/gravity_sign_is_one_residual_at_the_tt_kernel_block_2026_06_08.py`](../scripts/gravity_sign_is_one_residual_at_the_tt_kernel_block_2026_06_08.py)
**Runner cache:** [`logs/runner-cache/gravity_sign_is_one_residual_at_the_tt_kernel_block_2026_06_08.txt`](../logs/runner-cache/gravity_sign_is_one_residual_at_the_tt_kernel_block_2026_06_08.txt)

## Statement

This is a bounded residual-location result, not a closure of the gravity sign.

Given the static source/action exchange normalization used in
[`GRAVITY_ATTRACTION_SIGN_FROM_SOURCE_POSITIVITY_AND_SYMMETRIC_MEDIATOR_NARROW_THEOREM_NOTE_2026-06-08.md`](GRAVITY_ATTRACTION_SIGN_FROM_SOURCE_POSITIVITY_AND_SYMMETRIC_MEDIATOR_NARROW_THEOREM_NOTE_2026-06-08.md),
the Newtonian attraction sign and the healthy spin-2 kinetic sign track the
same overall sign `kappa=8 pi G`.

Separately, the scalar observable generator route
`W=log|det(D+J)|` sees the spatial metric only through the longitudinal scalar

```text
s(q) = g_ij qhat_i qhat_j.
```

Its metric Hessian is therefore rank-one longitudinal:

```text
H = W''(s) (qhat qhat) tensor (qhat qhat).
```

Every transverse-traceless spin-2 perturbation `h_TT` satisfies
`qhat_i h_TT^{ij}=0`, hence

```text
qhat_i qhat_j h_TT^{ij} = 0,
<h_TT | H | h_TT> = 0.
```

The scalar-`W` route cannot determine the spin-2 kinetic coefficient sign. The
remaining sign residual belongs to a geometric action, full-vielbein/stress
response, or other non-scalar-`W` route. This note does not derive that sign.

## Runner-Checked Content

- **K1 - exchange-sign identity under supplied premises.** With the displayed
  source/action convention, `1/(2 kappa)` is a healthy TT kinetic coefficient
  iff `kappa>0`, and the one-graviton exchange potential
  `-kappa P_{00,00} source^2` is attractive iff `kappa>0`.
- **K2 - scalar-W TT kernel.** For random nonzero lattice momenta, explicit
  transverse-traceless samples satisfy `qhat qhat : h_TT = 0` to numerical
  precision, so the rank-one scalar-`W` Hessian annihilates the TT block.
- **K3 - route guardrails.** The source note explicitly keeps the result to
  the scalar-`W` route and excludes any derivation of a framework gravitational
  action, a spin-2 kinetic sign, or an approved new primitive.

## Relation to Existing Gravity-Sign Notes

- [`GRAVITY_SIGN_NOT_FORCED_BY_ARROW_STABILITY_OR_SPECTRAL_ROUTES_NO_GO_SHARPENING_NOTE_2026-06-08.md`](GRAVITY_SIGN_NOT_FORCED_BY_ARROW_STABILITY_OR_SPECTRAL_ROUTES_NO_GO_SHARPENING_NOTE_2026-06-08.md)
  locates the sign as unresolved after spectral, stability, and arrow routes.
- [`GRAVITY_ATTRACTION_SIGN_FROM_SOURCE_POSITIVITY_AND_SYMMETRIC_MEDIATOR_NARROW_THEOREM_NOTE_2026-06-08.md`](GRAVITY_ATTRACTION_SIGN_FROM_SOURCE_POSITIVITY_AND_SYMMETRIC_MEDIATOR_NARROW_THEOREM_NOTE_2026-06-08.md)
  shows, under explicit exchange premises, that Newtonian attraction reduces to
  the healthy spin-2 kinetic/source-action orientation.
- [`UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md)
  supplies the scalar-`W` TT-kernel authority sharpened here.

This note combines those facts only at the bounded route-map level: it says
which scalar-`W` route cannot carry the sign and which sign identity the
source/action exchange route uses. It does not claim the full gravity-sign
problem is solved.

## No-Go Discipline Gate

**Status:** PASS for the local negative statement only: the scalar-`W`
metric-Hessian route cannot source the TT spin-2 kinetic coefficient. No global
no-go is shipped.

- **N1 - Alternative routes.** Five routes are separated: static
  source/action exchange identity, scalar-`W` metric Hessian, full-vielbein or
  stress-tensor response, geometric Regge/EH action, and reflection-positivity
  or unitarity constraints. This note closes only the scalar-`W` Hessian route.
- **N2 - Wall independence.** The scalar-`W` TT kernel does not imply failure
  of full-vielbein, geometric, or RP/unitarity routes. Those are separate
  routes, not hidden copies of the same wall.
- **N3 - Hidden-wall scan.** The source/action convention, positive-source
  regime, scalar-`W` ansatz, and healthy kinetic sign are explicit premises or
  open inputs. None is silently granted by Lattice, Quantum, Record, the
  scale-reference primitive, or the kinetic-isotropy primitive.
- **N4 - Residual matching.** The residual matched here is the TT spin-2
  kinetic sign on the gravity-sign surface. The scalar-`W` kernel only shows
  that this residual is not fixed by that scalar Hessian.
- **N5 - Rhetoric audit.** "Cannot source" means cannot source through the
  rank-one scalar-`W` metric-Hessian route. It does not mean matter, stress
  response, or all induced-gravity routes are impossible.
- **N6 - Partial-closure path scan.** A later retained Regge/EH calculation,
  full-vielbein stress response, or RP/unitarity theorem could still determine
  the sign without adding a new axiom.
- **N7 - Steelman.** The strongest objection is that the physical spin-2
  coefficient should be read from a geometric or full stress-response action,
  not from the scalar `s(q)` Hessian. This note accepts that objection and
  leaves those routes open.
- **N8 - Cross-cycle echo.** Prior gravity-sign notes warn against turning a
  route-specific missing bridge into a global no-go. This note preserves that
  boundary.

## What Is Not Claimed

- no derivation of `G>0`;
- no derivation of the spin-2 kinetic coefficient;
- no derivation of a framework gravitational action;
- no claim that all matter response routes fail;
- no new primitive, axiom, Tier-A admission, registered scale, or fitted value;
- no use of Record, the scale-reference primitive, or the kinetic-isotropy
  primitive as a gravitational-action source.

## Import and Support Inventory

- **Standard exchange-sign convention:** bounded input shared with the
  source/action exchange note.
- **Finite tensor algebra:** the scalar-`W` TT-kernel computation checked by
  the runner.
- **Open input:** the actual geometric or full stress-response origin and sign
  of the spin-2 kinetic term.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/gravity_sign_is_one_residual_at_the_tt_kernel_block_2026_06_08.py
```
