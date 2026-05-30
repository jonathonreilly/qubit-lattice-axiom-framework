# Field Equation Derivation — Variational Argument

**Status:** support - structural or confirmatory support note
**Date:** 2026-04-11
**Primary runner:** scripts/frontier_field_equation_uniqueness.py
**Type:** bounded_theorem
**Status authority:** independent audit lane only.

## 2026-05-28 Audit Repair (load-bearing core split from unsupplied bridge)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The variation of the chosen action algebraically gives the screened Poisson equation, but the packet does not close the missing bridge that this chosen action is uniquely forced by the framework rather than assumed. The included runner also"*

with repair: *"missing_bridge_theorem: provide a restricted-class uniqueness theorem deriving the local quadratic field action, including why the mass term and source coupling are selected rather than assumed."*.

Supplying the named retained authority/bridge is substantive new work, out of
scope for this repair. This revision takes the **split path**:

- **Load-bearing (in scope):** Within the restricted class of local, quadratic, positive-definite graph field actions, the Euler-Lagrange variation of the stated action algebraically and uniquely yields the screened Poisson equation `(L + mu^2 I) Phi = G rho`; this derivation is exact and constitutes the runner-verified content.
- **NON-load-bearing (split off / admitted):** The selection of the local quadratic action form itself — specifically why the mass term and source coupling are chosen and not derived from the framework axioms — is an assumed premise rather than a retained, derived result; this uniqueness-forcing bridge remains an admitted, non-load-bearing input until a retained restricted-class uniqueness theorem for the action is supplied.

No new axiom, import, or retained bridge is introduced. The runner-verified
core is the load-bearing content; the named bridge stays an admitted,
non-load-bearing input until a retained authority for it lands.

**Audit-dispatch parent candidate:** If a future independent audit
evaluates whether this variational wrapper is a non-chain-closing
alias/decorative handle, the candidate parent is
[`SELF_CONSISTENCY_FORCES_POISSON_NOTE.md`](SELF_CONSISTENCY_FORCES_POISSON_NOTE.md).
This is source-side routing context only; it does not assert an
`audit_status` or `effective_status`.

## The Problem

The screened Poisson equation (L + μ²)Φ = G·ρ was chosen by convention.
Four alternatives (bare Laplacian, biharmonic, heat kernel) all pass the
same consistency tests. Is the field equation a free parameter?

## The Variational Argument

The total action for the coupled matter-field system on a graph is:

    S = S_matter[ψ] + S_field[Φ] + S_coupling[ψ, Φ]

where the matter action is fixed by the staggered Dirac structure and
the coupling is fixed by the parity prescription (m + Φ)·ε(x).

The simplest local quadratic field action on a graph is:

    S_field = (1/2) Σ_edges w_ij (Φ_i − Φ_j)² + (μ²/2) Σ_nodes Φ_i² − G Σ_nodes ρ_i Φ_i

The first term is the graph gradient energy (penalizes spatial variation).
The second is the mass term (penalizes large field values).
The third is the source coupling.

Extremizing δS_field/δΦ_i = 0 gives:

    Σ_j w_ij (Φ_i − Φ_j) + μ² Φ_i = G ρ_i

which in matrix form is exactly:

    (L + μ²I) Φ = G ρ

The screened Poisson equation is the Euler-Lagrange equation of the
simplest local quadratic graph field action.

## What This Means

The field equation is NOT purely "chosen by convention." It is justified by
the requirement that the field-matter system is at a stationary point
of the combined action, under the constraint that the field action is:

1. **Local** — involves only nearest-neighbor differences (the graph gradient)
2. **Quadratic** — leading-order field theory (no self-interaction)
3. **Positive-definite** — the field has a unique minimum (stability)

Any other choice (biharmonic, heat kernel, etc.) corresponds to a
DIFFERENT field action with higher-order terms or non-local structure.
Within this restricted class, the screened Poisson equation is the unique
lowest-order local field equation on the graph.

## What Remains Free

- **G** (coupling constant) — analogous to Newton's G_N
- **μ** (screening mass) — analogous to the Compton wavelength of the
  graviton; sets the range of the gravitational interaction
- **The graph itself** — which bipartite graph is not predicted

These are free parameters, like coupling constants in any field theory.
Having free coupling constants is standard physics, not a weakness.

## Connection to Einstein's Equation

The graph Laplacian L is the discrete analog of the spatial Laplacian ∇².
In the weak-field (linearized) limit, Einstein's equation reduces to:

    ∇²Φ = 4πG ρ

which on the graph becomes L Φ = G ρ. The screened version (L + μ²)Φ = G ρ
corresponds to massive gravity (Yukawa-type potential with range 1/μ).

So the field equation on the graph is best read as a lowest-order discrete
analog of the linearized Einstein / Yukawa equation, not as a full derivation
of Einstein's equation from the axioms.
