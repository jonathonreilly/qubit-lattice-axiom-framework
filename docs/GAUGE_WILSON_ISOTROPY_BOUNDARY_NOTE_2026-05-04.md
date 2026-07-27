# Gauge Wilson Isotropy Boundary Note

**Date:** 2026-05-04
**Closure update:** 2026-05-06
**Derivation hardening:** 2026-07-10
**No-go discipline packet:** 2026-07-26
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

The plain-text relation pointer
`GAUGE_VACUUM_PLAQUETTE_CONSTANT_LIFT_OBSTRUCTION_NOTE.md` also remains in
force on its own narrower scope: an exact reduction
`P(beta) = P_1plaq(Gamma beta)` with constant `Gamma` must have `Gamma = 1`
at strong-coupling onset. That result is non-load-bearing here and does not
establish a general staggered-fermion source/action map.

## No-Go Discipline Gate

This gate stress-tests only the route-specific boundary theorem above:

> on the accepted isotropic nearest-neighbor Wilson surface, neither the
> `Cl(3)` pseudoscalar proposed as a fourth generator nor the displayed
> standard staggered-eta plaquette-sign mechanism supplies a nonzero
> anisotropic orientation datum.

It does not test, and does not assert, a global no-go for anisotropic gauge
actions, effective-action corrections, or spacetime emergence.

### N1 — Alternative-route enumeration

The route families are distinguished by their primary object, invariant, or
terminal obligation rather than by notation.

| Attack on the narrow claim | Marker | Resolution |
|---|---|---|
| Use `omega^2 = -I` alone as a time-like signature | `ATTEMPTED` | Section 1 and the primary runner check the actual terminal obligation for a fourth generator, `{omega,G_i}=0`; it fails for all three `G_i` because `omega` is central. |
| Escape through a representation in which `omega` is not central | `ATTEMPTED` | The two-sign-flip proof in §1 is an identity in abstract `Cl(3,0)`, independent of representation; the Pauli runner separately checks the framework's `M_2(C)` presentation. |
| Use integer sites outside the binary runner cube to change the eta product | `ATTEMPTED` | Section 2 proves the result for arbitrary integer `x`; the eta functions depend only on coordinate parity, so the runner's parity cube is exhaustive rather than sampled. |
| Use another one of the six Wilson plaquette orientations to obtain a different eta sign | `ATTEMPTED` | Section 2 reduces every `mu < nu` product to `-1`, and the runner checks all six orientations supplied by the accepted Wilson source-class theorem. |
| Challenge the premise that the accepted Wilson input has one common coefficient | `RULED OUT BY PRIOR` | [`GAUGE_SCALAR_TEMPORAL_COMPLETION_THEOREM_NOTE.md`](GAUGE_SCALAR_TEMPORAL_COMPLETION_THEOREM_NOTE.md) states the accepted source grammar as the one-dimensional common-coefficient class. Starting from six independent coefficients studies propagation of pre-existing anisotropy, not derivation by either mechanism tested here. |
| Convert the uniform eta signs into anisotropic physical coefficients through an additional determinant, hopping, or source/action kernel | `ATTEMPTED` | Such a kernel is a third mechanism and an additional premise. The current framework axioms do not supply a source/action map, this theorem applies only to the displayed sign datum `E`, and the possible effective-action route remains explicitly open. |

The first five attacks close on the stated premise surface. The sixth is the
strongest scope escape: it does not refute the two-route theorem because it
changes the mechanism and premise set, but it remains a live route against any
broader no-go.

### N2 — Wall-independence audit

The theorem has two route walls. The accepted Wilson grammar is an input
boundary, not a third wall, and the constant-lift obstruction is
non-load-bearing context.

| Wall pair | Closing the first closes the second? | Closing the second closes the first? | Independent? |
|---|---:|---:|---:|
| Pseudoscalar centrality / eta orientation-blindness | no | no | yes |

The collapsed wall set therefore still contains exactly these two independent
route failures.

### N3 — Hidden-wall scan

The phrases that could conceal premises resolve as follows:

| Phrase class | Classification | Resolution |
|---|---|---|
| `current framework memo` / `framework's local algebra` | cited premise authority | The Qubit node in [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies `M_2(C)`, equivalently the `Cl(3,0)` presentation. |
| `accepted Wilson` | cited retained authority | The common-coefficient six-orientation grammar is supplied by the Wilson source-class theorem linked above. |
| `standard staggered phases` | explicit definition | The full formula is stated in §2; no physical eta-to-action identification is hidden in the word `standard`. |
| future approved or repo-conventional primitive | non-load-bearing scope context | No such primitive is used in the proof; the sentence preserves possible future routes. |

No occurrence of `we assume`, `by construction`, `bridge context`, `naturally`,
`obviously`, or `standard QFT` supplies an unlisted wall. In particular, the
proof never assumes that eta signs act on physical Wilson coefficients.

### N4 — Residual matching

| Cited surface | Residual it addresses | Role here | Match? |
|---|---|---|---:|
| [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | the one-site `M_2(C) ~= Cl(3,0)` presentation | premise for the pseudoscalar calculation | yes |
| [`GAUGE_SCALAR_TEMPORAL_COMPLETION_THEOREM_NOTE.md`](GAUGE_SCALAR_TEMPORAL_COMPLETION_THEOREM_NOTE.md) | the common-coefficient six-orientation Wilson grammar | definition of the accepted input surface | yes |
| `GAUGE_VACUUM_PLAQUETTE_CONSTANT_LIFT_OBSTRUCTION_NOTE.md` | a nonunit constant observable reduction `P(beta)=P_1plaq(Gamma beta)` | plain-text relation context only, not a dependency | no; dropped from witness support |
| `GAUGE_WILSON_ISOTROPY_BOUNDARY_HYGIENE_COMPANION_NOTE_2026-06-04.md` | invariance of these two calculations under a Record-axiom memo change | meta hygiene only; plain-text pointer, not a dependency | no independent proof weight claimed |

The negative boundary therefore rests on the in-line algebra and the primary
runner, with matching premise support. It does not borrow a differently scoped
no-go as a witness.

### N5 — Rhetoric audit by resolution

| Resolution | Tested? | Exact boundary |
|---|---:|---|
| one-site algebra, proposed element `omega` | yes | `omega` is not the proposed fourth anticommuting generator |
| integer site / parity class | yes | `E_mu_nu(x)=-1` for every `x` under the displayed eta definition |
| each of the six unoriented plaquette classes | yes | the six-entry sign signature is `-1_6` |
| one accepted six-coefficient Wilson block | yes | `Pi_aniso(E)=0` and the spatial/temporal contrast vanishes |
| momentum mode, determinant/hopping order, multiplaquette effective action, radiative correction, or arbitrary dynamics | no | no negative claim is made at these resolutions |
| every possible spacetime-emergence or anisotropy mechanism | no | explicitly left open |

Accordingly, phrases such as "does not derive" and "provides no basis" refer
only to the two named mechanisms at the tested resolutions, never to arbitrary
operators or lattice-wide dynamics.

### N6 — Partial-closure path scan

The registered `kinetic_isotropy_primitive` (plain-text source pointer:
`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`) supplies only structural OS0
kinetic-form isotropy `c_t=c_s`. It is an approved
primitive, not a wall or bounded import, but it supplies no Wilson
gauge-action coefficient map and is not load-bearing here. The accepted Wilson
grammar already supplies the input surface. A separate retained source/action,
effective-action, or anisotropy theorem could still produce a different action
surface; this note leaves that route open and does not misclassify it as
requiring a new axiom. No convention or metadata reframe can change the
algebraic identities `[omega,G_i]=0` or `E=-1_6` into a nonzero anisotropic
signature.

### N7 — Steelman

A hostile reviewer should object that a uniform bare eta sign does not imply
an isotropic renormalized gauge action: integrating out staggered matter could
produce an orientation-dependent determinant or hopping correction once a
derived temporal structure is present, and an enlarged operator module could
supply a time-like generator other than `omega`. The nearby, currently
unaudited source `SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md`
(plain-text prior-art pointer, not a dependency) gives the concrete witness
family `c_t p_t^2 + c_s |p_spatial|^2` with independent temporal and spatial
kinetic coefficients under spatial cubic symmetry alone. That witness defeats
a global anisotropy no-go, but not the theorem stated here: an extra
effective-action kernel, enlarged module, or different temporal supplier is
not either of the two tested mechanisms and is expressly left open.

### N8 — Cross-cycle echo

The spatial-cubic time-anisotropy gate is the closest structural echo. Its
kinetic-form escape was later supplied by the approved kinetic-isotropy
primitive, but that governance mechanism cannot be reused as a derivation of
orientation-dependent Wilson coefficients: the primitive supplies equality
`c_t=c_s`, not a gauge source/action map. The Record-axiom hygiene companion is
the closest same-claim echo; it confirms only that these two calculations are
unchanged by the Record premise update. Neither echo retires a mechanism that
could make `omega` anticommuting or make the displayed eta signature
orientation-dependent. The broader effective-action route identified in N7
therefore remains open rather than being hidden by this no-go.

**N1-N8 status:** `PASS` for the route-specific two-mechanism negative
boundary. A global anisotropic-action or spacetime-emergence no-go remains
forbidden.

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
