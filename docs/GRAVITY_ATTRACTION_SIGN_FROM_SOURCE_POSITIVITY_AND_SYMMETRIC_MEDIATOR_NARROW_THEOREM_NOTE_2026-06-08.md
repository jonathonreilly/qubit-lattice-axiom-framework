# Newtonian Attraction as the Exchange-Sign Reduction

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-08
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:** [`scripts/gravity_attraction_sign_from_source_positivity_and_symmetric_mediator_2026_06_08.py`](../scripts/gravity_attraction_sign_from_source_positivity_and_symmetric_mediator_2026_06_08.py)
**Runner cache:** [`logs/runner-cache/gravity_attraction_sign_from_source_positivity_and_symmetric_mediator_2026_06_08.txt`](../logs/runner-cache/gravity_attraction_sign_from_source_positivity_and_symmetric_mediator_2026_06_08.txt)

## Statement

This is a bounded exchange-sign reduction for the gravity-sign residual.
On the retained-bounded Poisson surface, the Newtonian attraction sign is not an
additional sign once the source/action exchange model is supplied. For two
like positive macroscopic sources, a non-vector metric mediator, and a healthy
spin-2 kinetic sign, the static exchange potential is attractive. If the
spin-2 kinetic sign is flipped, the same exchange computation is repulsive.

Thus the source/action route reduces the Newtonian attraction sign to the
healthy spin-2 kinetic/source-action orientation. It does not derive that
orientation.

## Exchange-Sign Algebra

Use signature `eta = diag(-1,+1,+1,+1)`. The runner now derives the static
exchange sign from a finite quadratic mediator mode rather than importing it
as a textbook convention. For one bounded static mode with positive kernel
`K > 0`,

```text
E(phi) = (1/2) sigma_kin K phi^2 - (J_A + J_B) phi.
```

Eliminating `phi` gives

```text
phi_* = (J_A + J_B)/(sigma_kin K),
E(phi_*) = -(J_A + J_B)^2/(2 sigma_kin K),
E_AB = - J_A J_B/(sigma_kin K).
```

Since `sigma_kin = +/-1`, the cross-sign is the same as
`-sigma_kin J_A J_B` for `K > 0`. With the numerator contraction `N` and
source product `g_A g_B`, this is the displayed static exchange form

```text
V(r) = - sigma_kin g_A g_B N / (4 pi r),
```

where `sigma_kin=+1` denotes the healthy propagator sign, `g_A g_B > 0` for
like positive sources, and `N` is the relevant numerator contracted with the
static source structure `u^mu=(1,0,0,0)`.

The runner checks:

| derivation item | result |
|---|---|
| finite on-shell mediator cross term | `E_AB = -J_A J_B/(sigma_kin K)` |

| mediator | numerator `N` | healthy same-source sign |
|---|---:|---|
| scalar same-sign source | `+1` | attractive |
| vector like charge | `eta_00 = -1` | repulsive |
| spin-2 metric source | `P_{00,00}=+1/2` | attractive |

with

```text
P_{mu nu,alpha beta}
  = 1/2 (eta_{mu alpha} eta_{nu beta}
       + eta_{mu beta} eta_{nu alpha})
    - 1/2 eta_{mu nu} eta_{alpha beta}.
```

For the spin-2 metric numerator, the potential sign is

```text
sign(V) = - sign(sigma_kin) sign(g_A g_B).
```

Therefore positive sources and a healthy kinetic sign give attraction; a ghost
kinetic sign gives repulsion. The attraction sign and the spin-2 kinetic sign
are the same residual in this exchange model.

## Textbook Reference Boundary

The static tree-level exchange sign agrees with the standard QFT presentation
of one-mediator exchange, but that textbook statement is not load-bearing here.
The runner proves the sign on the framework-local finite quadratic exchange
channel by eliminating the mediator mode. A textbook citation can therefore be
used only as a parallel cross-check of convention and terminology, not as an
imported input.

## Claim Boundary

This is a bounded sign-reduction result. It supplies neither the dynamical
metric construction nor the kinetic coefficient.

It assumes:

1. the retained-bounded Poisson surface
   [`SELF_CONSISTENCY_FORCES_POISSON_NOTE.md`](SELF_CONSISTENCY_FORCES_POISSON_NOTE.md);
2. the static source/action exchange normalization displayed above;
3. positive macroscopic Newtonian sources, `g_A g_B > 0`;
4. a rank-2 symmetric metric mediator rather than a vector mediator; and
5. a healthy spin-2 kinetic sign.

Reflection positivity
[`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md)
supports positive total energy after OS reconstruction. It is not used here as
a pointwise local energy-condition theorem, and it does not by itself provide
the source/action normalization or the spin-2 kinetic sign.

## Relation to the Sign No-Go

[`GRAVITY_SIGN_NOT_FORCED_BY_ARROW_STABILITY_OR_SPECTRAL_ROUTES_NO_GO_SHARPENING_NOTE_2026-06-08.md`](GRAVITY_SIGN_NOT_FORCED_BY_ARROW_STABILITY_OR_SPECTRAL_ROUTES_NO_GO_SHARPENING_NOTE_2026-06-08.md)
left explicit source/action orientation as the live route after spectral,
energy-stability, and arrow routes failed to force attraction. This note walks
that route under its explicit exchange premises.

The result is not an unconditional closure of `G>0`. It says that once the
source/action exchange orientation and healthy spin-2 kinetic sign are supplied,
Newtonian attraction is no longer a second independent sign problem. The open
frontier is the healthy kinetic/source-action orientation itself.

## No-Go Discipline Gate

**Status:** PASS for the local negative phrase only: "not a second independent
sign problem after the exchange premises are supplied." No global no-go is
shipped.

- **N1 - Alternative routes.** Five routes are separated: spectral magnitude,
  energy-stability, arrow/entropy, local selector routes, and explicit
  source/action exchange orientation. This note treats only the last route and
  only under the stated exchange premises.
- **N2 - Wall independence.** Positive macroscopic source sign, source/action
  normalization, metric-mediator class, and healthy spin-2 kinetic sign are
  distinct inputs. Collapsing the Newtonian attraction sign to the kinetic
  sign does not collapse those inputs into one derived theorem.
- **N3 - Hidden-wall scan.** The exchange-sign algebra is now derived by the
  finite on-shell quadratic-mode calculation. "Positive source," "metric
  mediator," and "healthy kinetic" remain explicit premises here, not silent
  consequences of the baseline axioms.
- **N4 - Residual matching.** The prior residual is the Newtonian attraction
  sign on the Poisson surface. This note matches only the source/action
  exchange version of that residual and maps it to the healthy spin-2 kinetic
  sign.
- **N5 - Rhetoric audit.** "Attraction is forced" means forced inside the
  displayed exchange model. The note does not say that all gravity-sign routes
  are closed or that the framework has derived `G>0`.
- **N6 - Partial-closure path scan.** A later retained derivation of the
  metric source/action normalization, the kinetic coefficient, or a Regge/EH
  action would retire the remaining residual without adding a new axiom.
- **N7 - Steelman.** A hostile reviewer can object that the source/action
  normalization and kinetic sign are exactly the hard physics. The note accepts
  that objection and leaves those items open.
- **N8 - Cross-cycle echo.** This aligns with the current gravity-sign no-go
  discipline: route-specific failures must not become global impossibility
  claims, and partial sign reductions must preserve their open inputs.

## What Is Not Claimed

- no derivation of the healthy spin-2 kinetic sign;
- no derivation of the framework source/action normalization;
- no derivation of a local pointwise energy condition from reflection
  positivity;
- no observed value or registered scale such as `G_Newton`;
- no assertion that Record, the scale-reference primitive, or the
  kinetic-isotropy primitive supplies a gravitational action.

## Support Inventory

- **Derived finite exchange sign:** the tree-level exchange sign follows by
  completing the square / on-shell elimination for the bounded quadratic
  mediator mode; standard QFT is parallel reference only.
- **Framework support:** the retained-bounded Poisson surface and
  reflection-positivity total-energy support.
- **Open input:** the healthy spin-2 kinetic/source-action orientation.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/gravity_attraction_sign_from_source_positivity_and_symmetric_mediator_2026_06_08.py
```
