---
claim_id: energy_dictionary_mobius_interpolation_uniqueness_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "Among nonconstant Möbius maps sending the three named endpoints w=1→r=0, w=1/2→r=1/2, and w=1/3→r=1, the interpolant is uniquely r=(1-w)/(2w) up to overall nonzero scale of (α,β,γ,δ); the inverse is w=1/(1+2r) and the independent generation-3 identity Q=1/3+(2/3)r composes to Q=1/(3w), equaling 1/3, 2/3, 1 at those points; Residual Atom 2 remains declared modeling and r=1/2 is only the quotient-counting image."
upstream_dependencies:
  - minimal_axioms
  - koide_formation_gate_relocation_tied_measure_per_cell_weight_compatibility_bounded_theorem_note_2026-07-12
runner: scripts/energy_dictionary_mobius_interpolation_uniqueness_2026_08_13.py
---

# Energy Dictionary Möbius Interpolation Uniqueness

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact Möbius interpolation of three named formation-weight
endpoints; Residual Atom 2 remains a declared modeling element.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/energy_dictionary_mobius_interpolation_uniqueness_2026_08_13.py`](../scripts/energy_dictionary_mobius_interpolation_uniqueness_2026_08_13.py)

## Result Up Front

The July 12 formation-gate relocation note
[`KOIDE_FORMATION_GATE_RELOCATION_TIED_MEASURE_PER_CELL_WEIGHT_COMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-12.md`](KOIDE_FORMATION_GATE_RELOCATION_TIED_MEASURE_PER_CELL_WEIGHT_COMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-12.md)
declares, rather than derives, an energy-to-formation-state bridge. Residual
Atom 2 of that source states that the identification

`E_s = w E_tot`, `E_d = (1-w) E_tot`

against the first-order channel split `E_s = 3 a^2`, `E_d = 6 |b|^2` is
**this note's own declared modeling element**. That source states that the
identification is not supplied by the Record axiom. Conditional on that
declaration, T2 of the same source solves

`r = |b|^2/a^2 = (1-w)/(2w)`, `w = 1/(1+2r)`

for `0 < w < 1`. Residual Atom 1 records the energy image
`r = (1-w)/(2w)` for positive weights, with special points

- quotient counting: `w = 1/2` gives `r = 1/2`,
- carrier-trace restriction: `w = 1/3` gives `r = 1`,

and domain `0 <= w <= 1`. The remaining domain endpoint is the pure-singlet
state `w = 1`, whose energy image under the same formula is the limit
`r = 0`. Independently, on the generation 3-space,

`Q = 1/3 + (2/3) r`.

This note does not re-derive the formation-state construction. It does not
install Residual Atom 2. It does not force `r = 1/2` for every sector.

The exact advance is interpolation uniqueness. Among nonconstant Möbius maps

`r = (α w + β)/(γ w + δ)`, `αδ - βγ ≠ 0`,

that send the three named endpoints

`w = 1 → r = 0`, `w = 1/2 → r = 1/2`, `w = 1/3 → r = 1`,

the map is uniquely `r = (1-w)/(2w)` up to overall nonzero scale of
`(α, β, γ, δ)`. Two of those endpoints leave a one-parameter family. The
concrete rejector `r_alt = (1-w)/w` already fails `w = 1/2 → 1/2` because it
gives `1`. Record additivity and the `C_3` singlet/doublet split supply the
dial `r = |b|^2/a^2`; they do not supply the share identification
`E_s = w E_tot`. The interpolant maps every `w` in `(0, 1]` onto `r ≥ 0`, and
`r = 1/2` is the image of the quotient-counting endpoint only.

## Machine Status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Three named endpoints fix a unique nonconstant Möbius map, equal to r=(1-w)/(2w) up to scale. Two-point interpolation is not unique. Residual Atom 2 remains declared. Universal r=1/2 is the image of w=1/2 only."
trace_class: upstream_support
target_claim_id: energy_dictionary_r_from_w
target_blocker_text: "derive or uniquely characterize the formation-energy bridge r=(1-w)/(2w)"
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Möbius interpolation of the three named endpoints is unique; Residual Atom 2 remains declared. Do not force r=1/2. Do not adopt axiom text."
conditional_surface_status: "exact for three-point Möbius uniqueness, the two-point family, the inverse and Q composition, and the scoped negatives; Residual Atom 2 is not derived"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

A **Möbius map** is a fractional linear map

```text
r(w) = (α w + β)/(γ w + δ),
```

not identically constant, equivalently `αδ - βγ ≠ 0`. Overall nonzero
rescaling of `(α, β, γ, δ)` defines the same map.

The **three named endpoints** are the July 12 energy-image points

```text
w = 1     (pure singlet; domain endpoint)           →  r = 0,
w = 1/2   (quotient counting)                       →  r = 1/2,
w = 1/3   (carrier-trace restriction)                →  r = 1.
```

The **identity-gate dictionary formula** is the July 12 energy image

```text
r_of_w(w) = (1 - w)/(2 w),     w > 0.
```

Its algebraic inverse on `r ≥ 0` is

```text
w_of_r(r) = 1/(1 + 2 r).
```

The **generation-3 identity**, independent of Residual Atom 2, is

```text
Q_of_r(r) = 1/3 + (2/3) r.
```

The **two-point rejector** that must appear is

```text
r_alt(w) = (1 - w)/w.
```

A **two-point interpolant** of `w = 1 → 0` and `w = 1/3 → 1` that is not the
three-point map is the affine Möbius map

```text
r_2pt(w) = (3/2)(1 - w).
```

The current Record axiom in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies a
single additive scalar on finite pairwise-disjoint record collections:

> For any finite collection of pairwise-disjoint records, scalar readout
> `I` is additive, with `I(empty)=0`.

That scalar is not an energy-share identification.

## Exact Target And Obligation Graph

**Exact target.** Decide whether a nonconstant Möbius map through the three
named endpoints is unique, whether that unique value equals the July 12
energy image, and whether that uniqueness derives Residual Atom 2 or forces
`r = 1/2` on every sector.

| Obligation | Role | Disposition |
|---|---|---|
| quote Residual Atom 2 as a declared modeling element | premise | quoted; not raised in grade |
| quote `r = (1-w)/(2w)` and the three endpoints | premise | July 12 energy image and domain |
| unique Möbius interpolant | Theorem 1 | three homogeneous conditions, one scale |
| inverse and `Q` composition | Theorem 2 | exact solve and substitution |
| two-point family is not unique | Theorem 3 | free parameter; `r_alt` and `r_2pt` |
| dictionary is extra | Theorem 4 | Record and `C_3` do not supply `E_s = w E_tot` |
| no universal `r = 1/2` | Theorem 5 | `r = 1/2` only at `w = 1/2` |
| derive Residual Atom 2 from Record | non-claim | not attempted |
| force `r = 1/2` in every sector | non-claim | falsified at `w = 1/3` |
| edit an axiom | non-claim | no edit |

## Theorem 1 — Unique Möbius Interpolant

Let `r = (α w + β)/(γ w + δ)` be nonconstant. The three named endpoints
impose three homogeneous linear conditions.

1. `w = 1 → r = 0` forces the numerator to vanish and the denominator not
   to vanish: `α + β = 0` and `γ + δ ≠ 0`. Hence `β = -α`.
2. `w = 1/2 → r = 1/2` becomes
   `(α/2 - α)/(γ/2 + δ) = 1/2`, so `-α/2 = (1/2)(γ/2 + δ)`, hence
   `-α = γ/2 + δ`, and `δ = -α - γ/2`.
3. `w = 1/3 → r = 1` becomes
   `(α/3 - α)/(γ/3 + δ) = 1`, so `-2α/3 = γ/3 + δ`.

Substitute the expression for `δ` from (2) into (3):

```text
-2α/3 = γ/3 + (-α - γ/2) = γ/3 - α - γ/2.
```

Then `α/3 = -γ/6`, so `γ = -2α`. Back-substitution gives
`δ = -α - (-2α)/2 = 0`. The four-tuple is therefore

```text
(α, β, γ, δ) = (α, -α, -2α, 0)
```

for a single free scale `α`. Nonconstancy is `αδ - βγ = -2 α^2 ≠ 0`, hence
`α ≠ 0`. The zero tuple is excluded. Every admissible representative gives
the same function:

```text
r(w) = (α w - α)/(-2 α w) = (w - 1)/(-2 w) = (1 - w)/(2 w).
```

The three denominators on the solution are `γ + δ = -2α`,
`γ/2 + δ = -α`, and `γ/3 + δ = -2α/3`, all nonzero. Equivalently, the
`3 × 4` interpolation matrix

```text
[ 1  1   0   0 ]
[ 2  4  -1  -2 ]
[ 1  3  -1  -3 ]
```

has a one-dimensional nullspace spanned by `(1, -1, -2, 0)`. That is the
same scale class.

Thus, among nonconstant Möbius maps sending the three named endpoints, the
value is uniquely `r = (1-w)/(2w)`. This is uniqueness of an interpolant,
not a derivation that those endpoints must be interpolated, and not a
derivation of Residual Atom 2.

## Theorem 2 — Inverse And `Q` Composition

Solve `r = (1-w)/(2w)` for `w`, with `r ≥ 0` and `w > 0`:

```text
2 r w = 1 - w,     w (1 + 2 r) = 1,     w = 1/(1 + 2 r).
```

The inverse recovers the three named endpoints:

```text
w(0) = 1,     w(1/2) = 1/2,     w(1) = 1/3.
```

The generation-3 identity `Q = 1/3 + (2/3) r` does not use Residual Atom 2.
Substituting the interpolant gives

```text
Q = 1/3 + (2/3) · (1 - w)/(2 w) = 1/3 + (1 - w)/(3 w) = 1/(3 w).
```

The three named endpoints then read

```text
w = 1   →  r = 0    →  Q = 1/3,
w = 1/2 →  r = 1/2  →  Q = 2/3,
w = 1/3 →  r = 1    →  Q = 1.
```

A wrong closed form `(2 - w)/(3 w)` agrees at `w = 1` but returns `1` at
`w = 1/2`, not `2/3`. The composition is `1/(3 w)`, not that form.

## Theorem 3 — Two-Point Families Are Not Unique

Drop the quotient-counting condition `w = 1/2 → r = 1/2`. The remaining
conditions `β = -α` and `-2α/3 = γ/3 + δ` leave a free ratio `t = γ/α`
(`α ≠ 0`):

```text
β = -α,     γ = t α,     δ = -α (2 + t)/3,
r_t(w) = (w - 1)/(t w - (2 + t)/3).
```

The three-point solution is the single value `t = -2`, which forces `δ = 0`
and recovers `r = (1-w)/(2w)`. Any other `t` is a different Möbius map
through `w = 1 → 0` and `w = 1/3 → 1`.

The affine slice `t = 0` is the explicit witness

```text
r_2pt(w) = (3/2)(1 - w).
```

It sends `w = 1 → 0` and `w = 1/3 → 1`, but

`r_2pt(1/2) = 3/4 ≠ 1/2`.

The concrete rejector that must appear is not even a two-point interpolant
of the carrier-trace endpoint:

```text
r_alt(w) = (1 - w)/w
```

sends `w = 1 → 0`, `w = 1/3 → 2`, and `w = 1/2 → 1`. It fails
`w = 1/2 → 1/2` because it gives `1`. Replacing the identity gate
`r_of_w(w) = (1-w)/(2w)` by `r_alt` therefore fails the quotient-counting
endpoint. Replacing it by the linear map `1 - w` fails the carrier-trace
endpoint: `1 - 1/3 = 2/3 ≠ 1`.

Two endpoints do not select the energy-image formula among Möbius maps.

## Theorem 4 — Dictionary Is Extra (Scoped)

The current Record axiom supplies only additivity of a scalar readout `I`
on finite pairwise-disjoint record collections, with `I(empty)=0`. The
`C_3` singlet/doublet split supplies the registered dial

`r = |b|^2/a^2`

together with the channel decomposition `E_s = 3 a^2`, `E_d = 6 |b|^2`.
Neither object names the share rule `E_s = w E_tot`, `E_d = (1-w) E_tot`.

July 12 Residual Atom 2 already labels that identification as a **declared
modeling element**, not supplied by the Record axiom, by either cited
source note, or by the R-D surface. This note does not adopt it. An auditor
who rejects Residual Atom 2 keeps the two-cell menu and the two named
canonical constructions, and loses the bijection `r = (1-w)/(2w)` of that
source's T2.

Theorem 1 is conditional on interpolating the three named endpoints. It is
not a derivation that those endpoints must be interpolated, and it is not a
derivation of the share identification from Record additivity.

## Theorem 5 — No Universal `r = 1/2`

For every `w` in `(0, 1]` the interpolant is defined and nonnegative:

```text
r_of_w(w) = (1 - w)/(2 w) ≥ 0,
```

with equality only at the pure-singlet endpoint `w = 1`. There is a pole at
`w = 0`. The difference from the quotient-counting value is the exact
identity

```text
r_of_w(w) - 1/2 = (1 - 2 w)/(2 w),
```

which vanishes if and only if `w = 1/2`. In particular the carrier-trace
endpoint gives `r_of_w(1/3) = 1 ≠ 1/2`. The predicate “the dictionary
forces `r = 1/2` for every sector” therefore fails.

`r = 1/2` is the image of the quotient-counting endpoint only. Universal
forcing of `r = 1/2` is out of scope and is physically falsified for other
sectors. This note does not force it.

## Boundary And Non-Claims

The note does not:

- edit an axiom, or argue that an axiom update is necessary;
- adopt Residual Atom 2, or raise its declared-modeling grade;
- derive `E_s = w E_tot` from Record additivity or from the `C_3` split;
- force `r = 1/2` for every sector, or prefer `w = 1/2`;
- claim that the three endpoints must be interpolated;
- classify non-Möbius interpolants;
- re-derive the formation-state construction, the tied measure, or the
  lawful-weight selection of
  [`KOIDE_FORMATION_WEIGHT_CONDITIONAL_SELECTION_UNIQUE_REGISTRATION_COMPATIBLE_LAWFUL_WEIGHT_BOUNDED_THEOREM_NOTE_2026-07-12.md`](KOIDE_FORMATION_WEIGHT_CONDITIONAL_SELECTION_UNIQUE_REGISTRATION_COMPATIBLE_LAWFUL_WEIGHT_BOUNDED_THEOREM_NOTE_2026-07-12.md).

The scope is the exact interpolant of three named points among Möbius maps,
together with the two scoped negatives of Theorems 4 and 5.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| July 12 Residual Atom 2, declared modeling element | premise | quoted; not adopted |
| July 12 energy image `r = (1-w)/(2w)` and T2 solve | common object | restated; uniqueness is new |
| three named endpoints, including domain endpoint `w = 1` | interpolation data | quoted from July 12 |
| Record additivity and `I(empty)=0` | Theorem 4 premise | quoted; no edit |
| `Q = 1/3 + (2/3) r` | independent generation-3 identity | composed, not rederived |
| unique Möbius interpolant and two-point family | declared algebra | computed here |

The exact advance is a three-point Möbius uniqueness theorem with two
scoped negatives. Independent audit remains required before any effective
status may change.

## Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | Residual Atom 2 of the July 12 relocation note states that the identification `E_s = w E_tot`, `E_d = (1-w) E_tot` is "this note's own declared modeling element". This note uniquely characterizes the energy-image formula as a Möbius interpolant of the three named endpoints and leaves that declaration in place. |
| V2 | New content? | Searched `origin/main` at `c45dd5ab30` for Möbius uniqueness of the energy dictionary, three-point interpolation of `r = (1-w)/(2w)`, and the pair `(1-w)/w` as a rejector of `w = 1/2 → 1/2`. July 12 has the symbolic solve given the share split, and later notes consume that solve. No landed three-point Möbius uniqueness for these formation endpoints appears on that commit. |
| V3 | Independently checkable? | Textbook Möbius interpolation (three distinct points determine a unique nonconstant Möbius map) does not mention Koide `r` or the three formation endpoints `w = 1, 1/2, 1/3`. The runner solves the homogeneous system and evaluates identity gates in exact rational arithmetic. |
| V4 | More than a restatement? | Yes. The unique interpolant, its inverse, the composition `Q = 1/(3w)`, the two-point family, and the rejector `r_alt = (1-w)/w` are exact Fraction identities. |
| V5 | One-step relabel? | No. The July 12 T2 solve assumes the share split and produces `r = (1-w)/(2w)`. That is not uniqueness among Möbius interpolants of the three named endpoints. |

## No-Go Discipline Gate (Theorems 4–5)

The negative claims are restricted to these two: Record additivity and the
`C_3` split do not supply `E_s = w E_tot`, and the interpolant does not
force `r = 1/2` on every sector. The gate does not ship a global
non-existence theorem for energy dictionaries.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| Möbius 3-point | impose `w=1→0`, `w=1/2→1/2`, `w=1/3→1` on `(α,β,γ,δ)` | Theorem 1: unique scale class `(α,-α,-2α,0)` | **ATTEMPTED** |
| Möbius 2-point | drop `w=1/2→1/2`; free `t=γ/α` | Theorem 3: `r_2pt=(3/2)(1-w)` hits the two points and misses `1/2` | **ATTEMPTED** |
| force `r=1/2` | require `r_of_w(w)=1/2` for every `w` in `(0,1]` | Theorem 5: fails at `w=1/3`, where `r=1` | **ATTEMPTED** |
| Record-supplies-split | read `E_s=w E_tot` off additivity of `I` | Theorem 4: `I` is a scalar sum, not a share rule | **ATTEMPTED** |
| axiom edit | treat an axiom sentence as forcing the dictionary | forbidden by the no-edit surface; see N6 | **RULED OUT** |
| `r_alt=(1-w)/w` as the dictionary | replace the identity gate | fails `w=1/2→1/2` because it gives `1` | **ATTEMPTED** |
| linear `1-w` as the dictionary | replace the identity gate | fails `w=1/3→1` because it gives `2/3` | **ATTEMPTED** |

### N2 — wall independence

Theorem 4 closes only the claim that Record additivity or the `C_3` split
already is the share identification. Theorem 5 closes only universal
`r = 1/2`. Theorem 1 does not close either wall: uniqueness of an
interpolant is conditional on the three endpoints and does not derive
Residual Atom 2. The walls remain independent.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| Möbius class `r=(αw+β)/(γw+δ)`, `αδ-βγ≠0` | explicit interpolation class |
| three named endpoints | July 12 energy-image special points plus domain endpoint `w=1` |
| Residual Atom 2 share rule | declared modeling; not derived |
| `Q=1/3+(2/3)r` | independent generation-3 identity |
| Record additivity | quoted; no edit |
| formation dynamics supplying shares | open; not assumed |
| observations or empirical frequencies | none |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | Record additivity sentence and `I(empty)=0` | quoted as Theorem 4 premises only; no edit |
| July 12 relocation note, Residual Atom 2 | identification `E_s=w E_tot`, `E_d=(1-w) E_tot` as a declared modeling element, and energy image `r = (1-w)/(2w)` | quoted; three-point Möbius uniqueness is new |
| July 12 relocation note, T2 | symbolic solve of the declared split | the solve is not the uniqueness theorem |

No citation is used as authority for the nullspace computation or the
two-point rejectors; those are proved here and checked by the runner.

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | the three endpoints and the coefficient 4-tuple `(α,β,γ,δ)` | no classification of every energy map |
| per site | one two-cell formation menu `{s,d}` | no composite carrier theorem |
| per mode | the channel split and the dial `r=\|b\|^2/a^2` | no spectral-mode exhaustion |
| per block | Möbius 3-point uniqueness, 2-point family, and Theorems 4–5 | no formation dynamics |
| lattice-wide | checked and not executed | no lattice-wide dictionary or universal `r=1/2` |

The uniqueness is coefficient-level Möbius interpolation. It is not
lattice-wide.

### N6 — live partial-closure paths

1. A later derivation of Residual Atom 2 from formation dynamics or from
   some other independently justified bridge.
2. A reason the three named endpoints must be interpolated, which this note
   does not supply.
3. A non-Möbius interpolant, if an independent reason restricts the map
   class differently.
4. Sector-by-sector selection of a single `w`, which may land at `w=1/2`
   without forcing `r=1/2` universally.

No axiom sentence is required by the interpolation uniqueness. Those paths
remain live. Universal `r=1/2` is not among them.

### N7 — hostile steelman

> Three points always determine a unique Möbius map, and July 12 already
> solved `r = (1-w)/(2w)`, so nothing new is proved.

**Answer.** Textbook three-point uniqueness does not mention Koide `r` or
the three formation endpoints, and does not identify the interpolant with
the declared energy image. The July 12 solve assumes the share split. That
assumption is Residual Atom 2, a declared modeling element. Uniqueness
among interpolants of the endpoints is a different statement, and it still
does not derive the split.

### N8 — cross-cycle echo

July 12 T2 is a symbolic solve given `E_s = w E_tot`. Downstream notes
consume `r = (1-w)/(2w)` at declared-modeling grade. The present residual
is interpolation uniqueness conditional on the three named endpoints.
Residual Atom 2 remains declared. Universal `r=1/2` remains the image of
one endpoint only.

**Gate disposition.** PASS for the scoped interpolation uniqueness and for
Theorems 4–5. FAIL / DO NOT SHIP for “Residual Atom 2 is derived” or for
“the dictionary forces `r=1/2` in every sector”.

## Primary Runner

[`scripts/energy_dictionary_mobius_interpolation_uniqueness_2026_08_13.py`](../scripts/energy_dictionary_mobius_interpolation_uniqueness_2026_08_13.py)
solves the homogeneous Möbius system, inverts `r_of_w`, composes `Q`, and
evaluates the two-point family in exact rational arithmetic. Identity gates
call `r_of_w(w) = (1-w)/(2w)`. Replacing that gate by `(1-w)/w` fails
`w=1/2 → 1/2`. Replacing it by `1-w` fails `w=1/3 → 1`. The predicate that
the dictionary forces `r=1/2` for every sector fails at `w=1/3`.
