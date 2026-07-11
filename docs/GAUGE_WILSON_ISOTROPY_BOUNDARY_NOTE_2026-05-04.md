# Gauge Wilson Isotropy Boundary Note

**Date:** 2026-05-04
**Closure update:** 2026-05-06
**Derivation hardening:** 2026-07-10
**Type:** no_go
**Claim type:** no_go
**Claim scope:** route-specific exact negative boundary for the accepted
Wilson gauge-action isotropy surface: the two named mechanisms checked here
do not produce a spatial/temporal or orientation-dependent gauge-coupling
split, and therefore do not justify replacing the accepted isotropic Wilson
surface by a new anisotropic Wilson action.
**Status authority:** independent audit lane only. This source note proposes a
route-specific exact negative boundary; audit outcome and effective status are
set only by independent re-audit.
**Primary runner:** `scripts/frontier_gauge_wilson_isotropy_boundary_2026_05_04.py`

## Qubit-Reframe Grounding (refreshed 2026-07-10)

Under the current framework memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md), the
one-qubit operator algebra at each lattice site is equivalently
`Cl(3,0)` with the pseudoscalar `ω = σ_1 σ_2 σ_3` carrying `ω² = −𝟙`
and `ω` central in `Cl(3,0)`. The companion file
`QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md` records the same binding
definition as a non-load-bearing reader pointer (plain-text reference,
not a markdown-link dependency: the ω-centrality calculation in §1
below is the in-line algebraic content, sourced from the
stable `minimal_axioms` Qubit node only). Thus the ω-centrality
calculation in §1 below is a calculation inside the framework's local
algebra, not an extra Clifford-structure premise.

Specifically:
- The three Pauli generators `σ_1, σ_2, σ_3` are the standard
  generators of the one-qubit `Cl(3,0)` local algebra.
- The pseudoscalar `ω = σ_1 σ_2 σ_3` is the `Cl(3,0)` volume element,
  central in the odd-dimensional algebra because moving `ω` past any
  `σ_i` picks up two sign flips (no net sign change).
- The image of `ω` under the `Cl(3,0) ≅ M_2(ℂ)` identification is
  `i · 𝟙_{M_2(ℂ)}`; the complex structure used here is already part
  of the one-qubit operator-algebra identification, not an added
  premise for this no-go.

The no-go below therefore reads as a theorem about the framework's
one-qubit local algebra rather than a result that depends on an
admitted Clifford structure: in `Cl(3,0)`, `ω` is structurally central
(after identification with `i·𝟙`), and a fourth anticommuting Clifford
generator giving `Cl(3,1)` is not supplied by the Qubit axiom. The
four-direction plaquette index set used below comes instead from the named
accepted Wilson `3 spatial + 1 derived-time` source-class dependency; it is
not inferred from `ω` and is not added to the minimal axioms here. The
framework's time-direction lane remains a separate derived structure
(plain-text pointer: `ANOMALY_FORCES_TIME_THEOREM.md`), not a fourth
`Cl(3,0)` generator.

This grounding does not change the no_go's claim_type or claim_scope;
it ties the existing ω-centrality argument to the current one-qubit
operator-algebra wording. The independent audit lane retains status
authority: any effective status after this source edit is pipeline-derived
only after independent re-audit.

## Question

The two named mechanisms ask whether the accepted Wilson gauge action should
be changed or re-described by a derived anisotropy. The repo governance constraint is that
review-loop must not add new axioms, new foundational premises, or new theory
language without explicit user approval.

Within that constraint, what exact boundary can be salvaged from the isotropy
discussion?

## Answer

Two narrow boundary checks close as a route-specific no-go:

1. The `Cl(3)` pseudoscalar squares to `-I` in the Pauli irrep, but it is
   central in odd-dimensional `Cl(3)` and therefore does not anticommute with
   the three spatial generators. It cannot by itself be used as a fourth
   Clifford generator forcing a new `Cl(3,1)` gauge-coupling ratio.
2. The standard staggered-eta product around all six plaquette orientations
   has the same sign. This check does not generate a spatial/temporal
   plaquette-weight split from an isotropic input lattice.

These checks support the exact negative boundary statement:

> on the accepted Wilson nearest-neighbor plaquette surface, the two named
> mechanisms checked here do not derive orientation-dependent plaquette
> coefficients. They provide no basis for replacing the accepted isotropic
> surface by an anisotropic Wilson action.

## Closed Derivation

### 0. Premise and target closure

The load-bearing premise set is explicit:

1. the Qubit axiom supplies the one-site algebra `M_2(C) ≅ Cl(3,0)`;
2. the accepted Wilson source-class theorem cited below supplies the six
   orientations
   `O = {xy, xz, xt, yz, yt, zt}` and one common input coefficient `w`;
3. the standard staggered phases in §2 are a stated definition on that
   accepted four-direction index set.

No observed anisotropy, fitted coupling ratio, metric identification, or new
time-direction axiom is used. The constant-lift obstruction cited below is
non-load-bearing context and is not needed for either algebraic calculation.

Write the Wilson plaquette coefficients as

```text
c = (c_xy, c_xz, c_xt, c_yz, c_yt, c_zt) in R^6.
```

The accepted isotropic surface is the one-dimensional subspace

```text
I_iso = {w 1_6 : w in R}.
```

Equivalently, with `c_bar = (1/6) sum_(mu<nu) c_mu_nu`, its anisotropic
component is

```text
Pi_aniso(c) = c - c_bar 1_6.
```

A new anisotropic Wilson action requires `Pi_aniso(c_new) != 0`; a
spatial/temporal split in particular requires unequal averages over
`{xy,xz,yz}` and `{xt,yt,zt}`. The accepted input has `c = w 1_6` and
`Pi_aniso(c) = 0`. The question is exactly whether either named
mechanism supplies a nonzero anisotropic orientation datum. In the eta route,
the object tested below is only the six-entry sign signature `E`; no
fermion-determinant, hopping-expansion, or source/action map from `E` to a
physical coefficient update is assumed.

### 1. The `Cl(3)` pseudoscalar is not a fourth generator

Let `G_1, G_2, G_3` satisfy the `Cl(3)` relations

```text
{G_i, G_j} = 2 delta_ij I.
```

Set

```text
omega = G_1 G_2 G_3.
```

For any fixed `i`, moving `G_i` through the other two generators gives two
minus signs and therefore no net sign change. Using `G_i^2 = I`,

```text
omega G_i = G_i omega.
```

So `[omega, G_i] = 0` for all three spatial generators. In the Pauli irrep,
`omega = i I` and `omega^2 = -I`, matching the runner's pseudoscalar-square
check. But a fourth Clifford generator `T` capable of supplying an independent
time-like Clifford direction would need

```text
{T, G_i} = 0
```

for the three spatial generators. Since `omega` commutes with every `G_i`,

```text
{omega, G_i} = 2 omega G_i != 0.
```

Thus the `Cl(3)` pseudoscalar is a central complex-structure element on this
surface, not a standalone fourth anticommuting generator. It cannot force a
new temporal Clifford direction. In this route, `ω` was the proposed supplier
of the fourth direction whose distinction was supposed to induce a temporal
coefficient. Since it fails the defining anticommutation relations, the route
produces no admissible fourth-generator coefficient map at all and hence no
`Pi_aniso(c_new)`.

### 2. Staggered eta plaquette products are orientation-blind

Use the standard staggered phases on four directions:

```text
eta_0(x) = 1,
eta_mu(x) = (-1)^(x_0 + ... + x_{mu-1}) for mu > 0.
```

For `mu < nu`, the plaquette sign product is

```text
E_mu_nu(x)
  = eta_mu(x) eta_nu(x + e_mu) eta_mu(x + e_nu) eta_nu(x).
```

The factor `eta_mu` is independent of `x_nu`, so
`eta_mu(x + e_nu) = eta_mu(x)`. The factor `eta_nu` does depend on `x_mu`, so
`eta_nu(x + e_mu) = -eta_nu(x)`. Therefore

```text
E_mu_nu(x) = - eta_mu(x)^2 eta_nu(x)^2 = -1
```

for every site `x` and every one of the six orientations
`xy`, `xz`, `xt`, `yz`, `yt`, and `zt`.

An anisotropic Wilson action would need an orientation-dependent coefficient
pattern. The eta-product mechanism supplies the same factor `-1` on every
orientation. Its complete orientation signature is therefore

```text
E = (E_xy, E_xz, E_xt, E_yz, E_yt, E_zt) = -1_6,
Pi_aniso(E) = 0.
```

In particular,

```text
(E_xy + E_xz + E_yz)/3 = (E_xt + E_yt + E_zt)/3 = -1.
```

Thus the eta sign data itself lies in the isotropic pattern subspace and
contains no spatial/temporal contrast. This is not a claim that the physical
Wilson coefficients transform as `c -> diag(E)c`: deriving an additive or
multiplicative action correction from staggered fermions would require a
separate retained source/action bridge. The narrower conclusion is that the
standard eta plaquette-sign mechanism alone supplies no orientation-dependent
datum from which to derive a spatial/temporal plaquette-weight split.

### Boundary theorem

Combining the two checks:

1. the accepted Wilson input lies in `I_iso`;
2. the `Cl(3)` route fails to supply its proposed fourth generator and hence
   supplies no coefficient update;
3. the staggered eta route supplies the signature `E = -1_6`, whose
   anisotropic projection vanishes.

Therefore these two named routes do not derive a new anisotropic Wilson
gauge action: neither supplies the orientation-dependent structure needed for
a coefficient vector with nonzero anisotropic projection. This conclusion is
an exact negative boundary for these two mechanisms, not a derivation of
isotropy from the minimal axioms and not a staggered-fermion source/action
bridge. The live action surface remains the accepted isotropic Wilson surface
unless a separate, independently audited theorem derives a different
orientation-dependent coefficient pattern.

## Relation To Existing Authority

[`GAUGE_SCALAR_TEMPORAL_COMPLETION_THEOREM_NOTE.md`](GAUGE_SCALAR_TEMPORAL_COMPLETION_THEOREM_NOTE.md)
states the accepted Wilson nearest-neighbor plaquette grammar with one common
coefficient across the six plaquette orientations. This note does not promote
that statement or re-axiomatize it. It records that the two named candidate
mechanisms do not force a different action surface.

[`GAUGE_VACUUM_PLAQUETTE_CONSTANT_LIFT_OBSTRUCTION_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_CONSTANT_LIFT_OBSTRUCTION_NOTE.md)
also remains in force on its own narrower scope: an exact reduction
`P(beta) = P_1plaq(Gamma beta)` with constant `Gamma` must have `Gamma = 1`
at strong-coupling onset. That result is non-load-bearing here and does not
establish a general staggered-fermion source/action map.

## Runner Result

Command:

```bash
python3 scripts/frontier_gauge_wilson_isotropy_boundary_2026_05_04.py
```

Expected summary:

```text
SUMMARY: PASS=19 FAIL=0
```

The runner verifies:

- the Pauli-irrep `Cl(3)` anticommutation relations;
- the `Cl(3)` pseudoscalar has square `-I`;
- the pseudoscalar commutes with each `Cl(3)` generator and so is not a
  standalone fourth anticommuting generator;
- all staggered eta-products around `xy`, `xz`, `xt`, `yz`, `yt`, and `zt`
  plaquettes equal `-1` on the exhaustive parity cube;
- the six-entry eta orientation signature has zero anisotropic projection and
  zero spatial/temporal contrast.

## What This Does Not Close

This exact negative boundary does not prove a global no-go for every possible
spacetime-emergence route. A future independently audited theorem could still
derive a metric ratio or a specific anisotropic Wilson action from an
explicitly approved and repo-conventional primitive.

Until such a theorem is reviewed and audited, the live boundary is:

- no repo-wide anisotropy axiom has been added;
- no new gauge-action language has been introduced;
- isotropic Wilson remains the scoped accepted surface already present in the
  plaquette stack;
- the analytic plaquette value at `beta = 6` remains open.
