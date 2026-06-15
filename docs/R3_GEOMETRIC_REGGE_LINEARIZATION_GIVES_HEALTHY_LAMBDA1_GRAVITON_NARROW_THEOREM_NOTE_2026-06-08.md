# R3 Target Operator: Linearized Einstein Tensor Lambda-One Algebra

**Date:** 2026-06-08
**Type:** bounded target-operator algebra certificate
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:** [`scripts/r3_regge_linearization_lambda1_healthy_graviton_2026_06_08.py`](../scripts/r3_regge_linearization_lambda1_healthy_graviton_2026_06_08.py)
**Runner cache:** [`logs/runner-cache/r3_regge_linearization_lambda1_healthy_graviton_2026_06_08.txt`](../logs/runner-cache/r3_regge_linearization_lambda1_healthy_graviton_2026_06_08.txt)

## Statement

This note verifies the algebra of the **target continuum operator** that a
geometric Regge/EH route would need to reproduce after the relevant geometric
premises are supplied.

For the linearized Einstein tensor `G_lin` in momentum space:

- pure gauge modes `h_{mu nu} = k_mu xi_nu + k_nu xi_mu` are zero modes;
- a transverse-traceless sample has nonzero two-derivative response
  `G_lin(h_TT) = (1/2) k^2 h_TT` under the sign convention used by the runner;
- the trace/conformal direction is acted on differently from the TT sample.

This is a target-operator certificate only. It does not compute the second
variation of the cubic-Coxeter Regge action, does not derive edge-length metric
degrees of freedom, and does not prove that the framework has a physical
lambda-one graviton.

## Runner-Verified Result

The runner uses the linearized Einstein tensor with signature `(-,+,+,+)` and
a simple spacelike momentum frame. It checks:

- **R3a:** gauge modes are annihilated numerically below tolerance;
- **R3b:** a supplied TT sample is an eigenmode with coefficient `(1/2) k^2`;
- **R3c:** the conformal sample is not acted on like the TT sample;
- **R3d:** the source note contains the explicit guardrails that Regge
  second-variation and metric emergence are not supplied.

`TOTAL: PASS=4 FAIL=0`.

## What This Establishes

The linearized EH/Lichnerowicz target has the expected lambda-one algebra:
gauge zero modes, a nonzero TT kinetic response, and a distinct trace sector.
This is the algebraic target a discrete Regge calculation would need to match.

## What This Does Not Establish

This note does **not** establish:

- the cubic-Coxeter Regge action's explicit `delta^2 S_R`;
- a retained bridge from the framework's flat Regge-deficit note to this
  momentum-space operator;
- the edge-length metric degrees of freedom required by Regge calculus;
- the continuum limit, Lorentz limit, or physical graviton dispersion;
- a Newton-sign result, source/action normalization, or observed coupling;
- that the bare `Z^3` lattice, Record axiom, scale-reference primitive, or
  kinetic-isotropy primitive supplies a dynamical metric.

## Relation to R3

The submitted PR claimed that the geometric route gives the healthy
lambda-one diffeomorphism-invariant graviton. That is not landed. What lands
here is the narrower target-operator algebra certificate: if a later theory
supplies the Regge second variation, the edge-length metric, and the continuum
bridge, this row identifies the lambda-one operator properties that bridge
must reproduce.
