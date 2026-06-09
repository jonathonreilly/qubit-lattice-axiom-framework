# R3: the Geometric (Regge / Discrete Einstein–Hilbert) Route Gives the Healthy λ=1 Diffeomorphism-Invariant Graviton — the Missing Two-Derivative Generator

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-08
**Type:** geometric-route confirmation (R3 of the graviton-diffeomorphism exercise chain)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.
**Primary runner:** [`scripts/r3_regge_linearization_lambda1_healthy_graviton_2026_06_08.py`](../scripts/r3_regge_linearization_lambda1_healthy_graviton_2026_06_08.py) (PASS=3).

## The gate

The exercise found the framework's only *derived* native gravity object — the matter effective action
`W=log|det(D+J)|` — has the spin-2 graviton in the exact kernel of its rank-1 longitudinal metric-Hessian
(provably dead for the graviton). The missing object is a **spin-2-coupled two-derivative curvature
generator**. The natural candidate is the framework's **retained geometric action**: the cubic-Coxeter
Regge action `S_R = Σ_hinges A_hinge · δ_hinge` (the discrete Einstein–Hilbert;
[`CUBIC_COXETER_REGGE_DEFICIT_VANISHING`](CUBIC_COXETER_REGGE_DEFICIT_VANISHING_NARROW_THEOREM_NOTE_2026-05-10.md)
proves the flat fact `S_R=0`). R3: does its linearization give the healthy λ=1 structure?

## Result (R3 PASSES — the geometric route is healthy)

The linearized Einstein–Hilbert kinetic operator is the linearized Einstein tensor `G^{lin}` (the
Lichnerowicz / Fierz–Pauli operator) — the λ=1 structure. Verified (exact, momentum space):

- **(R3a) Diffeomorphism-invariant.** Gauge modes `h_{μν} = k_μξ_ν + k_νξ_μ` are **exact zero modes** of
  `G^{lin}` (the linearized Bianchi identity; `max |G^{lin}(gauge)| = 1.8×10⁻¹⁵` over 2000 random `ξ`).
  This is precisely the spin-2 gauge invariance the chain needs.
- **(R3b/R3d) Healthy and nonzero on TT.** For a transverse-traceless `h`, `G^{lin}(h_TT) = ½k² h_TT`
  exactly — a single definite-sign two-derivative kinetic term, **nonzero** on the spin-2 graviton.
  This is the decisive contrast with the matter route: the rank-1 longitudinal `W`-Hessian has TT in its
  **kernel**, while the geometric `G^{lin}` **couples** to TT, healthily.
- **(R3c) Conformal mode distinct (the λ=1 split).** The trace/conformal mode `h ∼ η` is acted on
  differently from TT (the opposite-sign conformal sector, gauge under diffeomorphisms) — the λ=1 split,
  versus the matter-`W` *degenerate* (trace=TT same-sign) metric.

The framework's retained **cubic-Coxeter Regge action is the discrete realization of this EH operator**
(Rocek–Williams / Hamber: linearized Regge on a regular lattice reproduces continuum linearized GR, with
the lattice diffeomorphisms = vertex translations as the kinetic-operator zero modes). **So the geometric
route GIVES the healthy λ=1 diffeomorphism-invariant graviton — it IS the missing spin-2-coupled
two-derivative generator** that the dead matter route could not supply.

## What is and is not claimed

- **Is:** the linearized EH/Lichnerowicz (λ=1) operator is diffeomorphism-invariant (gauge modes are exact
  zero modes), healthy and nonzero on TT (`½k²h_TT`, unlike the matter-`W` kernel), with a distinct
  conformal sector (the λ=1 split); the framework's retained cubic-Coxeter Regge action is its discrete
  generator (Rocek–Williams). So the framework HAS a geometric action that gives the healthy λ=1 graviton.
- **Is not:** does **not** derive the simplicial **edge-length metric DOF** that the Regge action requires —
  the bare Z³ lattice axiom supplies only the site set + adjacency, not edge lengths / a metric. So R3
  confirms the λ=1 structure **given** the geometric action / an emergent metric; the open piece is the
  **emergent metric DOF** (where the edge-length/metric comes from) plus the **continuum limit** (emergent
  Lorentz). Does not explicitly compute the cubic-Coxeter `δ²S_R` (uses the EH operator it realizes +
  the Rocek–Williams correspondence); adds no axiom or fitted value.

## Boundaries (honest)

- **Target operator + correspondence, not an explicit `δ²S_R`.** R3 verifies the λ=1 EH operator's
  properties (the target structure) and identifies the retained Regge action as its discrete generator via
  the standard lattice-gravity correspondence; the explicit cubic-Coxeter second variation is the
  follow-on.
- **The edge-length metric DOF is the open input.** Regge calculus presupposes edge lengths (the metric);
  the framework must *emerge* them. This + the continuum limit are the same bottom as R2's emergent-SO(3)
  residual — the emergent-metric / emergent-Lorentz frontier.

## Load-bearing inputs

- [`CUBIC_COXETER_REGGE_DEFICIT_VANISHING_NARROW_THEOREM_NOTE_2026-05-10.md`](CUBIC_COXETER_REGGE_DEFICIT_VANISHING_NARROW_THEOREM_NOTE_2026-05-10.md)
  — the framework's retained geometric Regge action (flat fact `S_R=0`); R3 linearizes its EH content.
- [`GRAVITY_SIGN_IS_ONE_RESIDUAL_AT_THE_TT_KERNEL_BLOCK_NARROW_THEOREM_NOTE_2026-06-08.md`](GRAVITY_SIGN_IS_ONE_RESIDUAL_AT_THE_TT_KERNEL_BLOCK_NARROW_THEOREM_NOTE_2026-06-08.md)
  — the matter route is dead (TT in the `W`-Hessian kernel); R3 supplies the geometric alternative.

## Forbidden-imports check

No PDG / fitted value. The linearized Einstein tensor `G^{lin}`, its gauge zero modes, and the TT kinetic
coefficient are standard linearized GR, reproduced exactly in the runner. The Regge = discrete-EH
correspondence (Rocek–Williams / Hamber) is named as the literature template connecting the operator to
the framework's retained Regge action; the edge-length metric DOF is flagged as the open input.
