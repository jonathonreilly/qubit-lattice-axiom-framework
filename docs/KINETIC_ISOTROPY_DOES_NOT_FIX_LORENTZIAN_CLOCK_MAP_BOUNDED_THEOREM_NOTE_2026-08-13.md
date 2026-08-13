---
claim_id: kinetic_isotropy_does_not_fix_lorentzian_clock_map_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "The approved kinetic-isotropy primitive supplies the Euclidean OS0 equality c_t = c_s, equivalently the TT form (k4^2+k^2)/4. Continuing that same polynomial by the linear Record/Wick clock map k4=i a ω produces the family Q_a = (-a^2 ω^2 + k^2)/4. The Euclidean polynomial does not depend on a. The three values a=1/2,1,2 give three distinct Lorentzian ω^2 coefficients 1/16, 1/4, 1. No sentence of the primitive or of the four-axiom memo names the continuation parameter a. This note performs no axiom edit and does not install a clock map."
upstream_dependencies:
  - minimal_axioms
  - kinetic_isotropy_primitive
runner: scripts/kinetic_isotropy_does_not_fix_lorentzian_clock_map_2026_08_13.py
---

# Kinetic Isotropy Does Not Fix The Lorentzian Clock Map

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact algebra of the Euclidean OS0 TT form versus the linear
Record/Wick continuation parameter `a` in `k4 = i a ω`.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/kinetic_isotropy_does_not_fix_lorentzian_clock_map_2026_08_13.py`](../scripts/kinetic_isotropy_does_not_fix_lorentzian_clock_map_2026_08_13.py)

## Result Up Front

The approved kinetic-isotropy primitive
[`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
supplies one Euclidean kinetic-form equality,

```text
c_t = c_s,
```

equivalently the Osterwalder-Schrader OS0 normalization of the Euclidean
regulator block `Z^3 x Z_tau`. In momentum space that is the declared
Euclidean TT form

```text
Q_E(k4, k) = (k4^2 + k^2)/4,
```

where `k^2 = kx^2 + ky^2 + kz^2`. The coefficient of `k4^2` equals the
coefficient of each spatial `k_i^2`, both `1/4`. That is the primitive's
content.

A linear Record/Wick clock map is a different object: the continuation

```text
k4 = i a ω,    a ≠ 0,
```

from Euclidean temporal momentum to a Lorentzian frequency. Substituting
into the same `Q_E` produces the family

```text
Q_a(ω, k) = ((i a ω)^2 + k^2)/4 = (-a^2 ω^2 + k^2)/4.
```

The Euclidean polynomial never sees `a`. The Lorentzian kinetic
coefficient of `ω^2` is `a^2/4`. The three values `a = 1/2`, `a = 1`,
`a = 2` therefore return `1/16`, `1/4`, `1`. Those three rationals are
distinct, so the Euclidean OS0 form does not select a clock map.

The four-axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
likewise does not name `a`. Lattice is cubic `Z^3`. Record supplies
content-determined additive readout. Admissibility does not define a time
metric. The primitive's uses of the letter `a` are the spatial adjacency
`a_x = a_y = a_z` and the sibling scale anchor `a^{-1} = M_Pl`, not a
Wick parameter.

If a continuation rule is separately declared, then `κ(a) = a^2/4` is
determined. That rule is a second object. It is not `c_t = c_s`, is not
installed here, and is not claimed to be physical.

## Machine Status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The Euclidean TT polynomial is independent of a, the three displayed continuations give three distinct Lorentzian ω^2 coefficients, and neither source sentence names the clock map. A declared continuation would fix κ(a) but is not the primitive."
trace_class: negative_route_pruning
target_claim_id: kinetic_isotropy_does_not_fix_lorentzian_clock_map
target_blocker_text: "decide whether Euclidean OS0 kinetic isotropy selects the Record/Wick clock map a"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for the displayed Q_a family and the three-value rejector; a physical clock map remains open"
hypothetical_axiom_status: no edit
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `k^2 := kx^2 + ky^2 + kz^2` for spatial Euclidean momentum. The
**Euclidean TT form** is the quadratic polynomial

```text
Q_E(k4, kx, ky, kz) = (k4^2 + k^2)/4.
```

Its temporal and spatial coefficients are

```text
[k4^2] Q_E = 1/4,    [kx^2] Q_E = [ky^2] Q_E = [kz^2] Q_E = 1/4.
```

The OS0 sentence `c_t = c_s` is exactly that equality of coefficients.
The overall `1/4` is the declared TT normalization; the primitive fixes
the ratio, and the displayed polynomial is the isotropic representative
with that normalization.

A **linear Record/Wick clock map** is a nonzero scalar `a` together with
the substitution `k4 = i a ω`. The **continued family** is

```text
Q_a(ω, k) := Q_E(i a ω, k) = (-a^2 ω^2 + k^2)/4.
```

The **Lorentzian kinetic coefficient** is the coefficient of `-ω^2`,

```text
κ(a) := [-ω^2] Q_a = a^2/4.
```

Equivalently, `Q_a = -κ(a) ω^2 + (1/4) k^2`. The three rejector values
are the nonzero rationals `a ∈ {1/2, 1, 2}`.

The inverse substitution `ω = -i k4 / a`, available whenever `a ≠ 0`,
returns the same Euclidean polynomial:

```text
Q_a(-i k4 / a, k) = (k4^2 + k^2)/4 = Q_E.
```

That recovery identity is independent of the particular nonzero `a`.

| `a` | `κ(a) = a^2/4` | `Q_a` | recovered `Q_E` |
|---|---|---|---|
| `1/2` | `1/16` | `-ω^2/16 + k^2/4` | `(k4^2 + k^2)/4` |
| `1` | `1/4` | `-ω^2/4 + k^2/4` | `(k4^2 + k^2)/4` |
| `2` | `1` | `-ω^2 + k^2/4` | `(k4^2 + k^2)/4` |

The spatial coefficient remains `1/4` on every row. Only the Lorentzian
`ω^2` coefficient moves.

The primitive's wording "one tick is one edge in form, not only in
spacing" is the same Euclidean OS0 statement: the kinetic *form* is
isotropic. It is not a declaration that the continuation parameter
equals `1`, and it is not a selection among the three rows.

## Exact Target And Obligation Graph

**Exact target.** Decide whether the Euclidean OS0 TT form, as supplied
by the kinetic-isotropy primitive, selects the linear Record/Wick clock
map `a` among the displayed family.

| Obligation | Role | Disposition |
|---|---|---|
| pin `c_t = c_s` and the OS0 Euclidean wording | premise | quoted from the primitive |
| pin that the primitive does not add or amend an axiom | premise | quoted from the primitive |
| pin that Admissibility does not define a time metric | premise | quoted from the axiom memo |
| show `Q_E` has no `a` and is OS0 | Theorem 1 | coefficient comparison |
| show `a = 1/2, 1, 2` give `1/16, 1/4, 1` | Theorem 2 | substitution `k4 = i a ω` |
| show no source sentence names the clock map `a` | Theorem 3 | sentence pin |
| install a physical clock map or standard Wick `a = 1` | autonomous closure | open |
| claim Lorentzian physics is impossible | non-claim | not attempted |

## Theorem 1 — The Euclidean OS0 Form Is Independent Of `a`

The polynomial `Q_E = (k4^2 + k^2)/4` is written in the Euclidean
momenta `(k4, kx, ky, kz)` alone. The symbol `a` does not appear. The
four quadratic coefficients are

```text
[k4^2] Q_E = 1/4 = [kx^2] Q_E,
```

which is `c_t = c_s` at the declared TT normalization. That is the OS0
statement.

For each nonzero `a`, the Euclidean member of the family is the same
polynomial: one obtains `Q_a` by substituting `k4 = i a ω`, and the
inverse substitution displayed above returns `Q_E` with no residual `a`.
Evaluating `Q_E` at any Euclidean point, for example
`(k4, k^2) = (2, 9)`, returns the single rational `13/4`, independent of
which continuation will later be used.

Therefore every member of `{Q_{1/2}, Q_1, Q_2}` shares one Euclidean
OS0 form. The primitive, which speaks only about that Euclidean form,
cannot distinguish the three members.

## Theorem 2 — Three Values Of `a` Give Three Distinct Lorentzian Coefficients

Substitute `k4 = i a ω` into `Q_E`:

```text
(i a ω)^2 / 4 + k^2/4 = (i^2 a^2 ω^2)/4 + k^2/4
                      = (-a^2 ω^2)/4 + k^2/4.
```

The coefficient of `-ω^2` is `κ(a) = a^2/4`. The three rejector values
are then ordinary rational arithmetic:

```text
κ(1/2) = (1/4)/4 = 1/16,
κ(1)   = 1/4,
κ(2)   = 4/4     = 1.
```

These three rationals are pairwise distinct. The spatial coefficient
stays `1/4` in every case, so the mismatch is isolated to the Lorentzian
clock direction.

A function of the Euclidean polynomial alone is constant on the family.
No such function can equal the triple `(1/16, 1/4, 1)`. Euclidean OS0
kinetic isotropy therefore does not fix the Lorentzian clock map.

Two nearby substitutions fail in instructive ways and are not used as
the claim. Dropping `a` and writing the textbook rule `k4 = i ω` returns
`κ = 1/4` for every formal label `a`. Inserting `a` already on the
Euclidean side, as `(a^2 k4^2 + k^2)/4`, makes the Euclidean form
itself `a`-dependent and abandons the primitive. Replacing the TT
normalization `1/4` by `1/2` would move the triple to `(1/8, 1/2, 2)`.
The displayed family is the continuation of the declared TT form, not
those replacements.

## Theorem 3 — No Source Sentence Names `a`; No Axiom Edit

The primitive's load-bearing sentence is the Euclidean equality
`c_t = c_s`, identified with OS0 hypercubic symmetry of `Z^3 x Z_tau`.
It states that it supplies only that kinetic-form ratio, that it does
not add or amend an axiom, and that it does not re-axiomatize time. Its
only quantity-level uses of the letter `a` are the Lattice spatial
adjacency `a_x = a_y = a_z` and the sibling scale-reference identity
`a^{-1} = M_Pl`. It does not write `k4 = i a ω`, does not name a
Record/Wick clock map, and does not select among `{1/2, 1, 2}`.

The axiom memo names four premises: Lattice, Qubit, Admissibility, and
Record. Lattice is the cubic lattice `Z^3`. Record locks content and
supplies additive scalar readout `I` with `I(empty)=0`. Admissibility
determines a nearest-neighbor distribution and, in the memo's own
dynamics paragraph, does not define a time metric. No axiom sentence
introduces a continuation parameter `a` or a Lorentzian `ω^2`
coefficient.

This note performs no axiom edit and does not argue that an axiom
update is required. The missing object, if a later construction wants a
definite `κ`, is a separately declared clock map. Declaring such a map
is a live formal escape. It is not the kinetic-isotropy primitive, and
it is not claimed here to be physical.

## Boundary And Non-Claims

The note does not:

- edit an axiom, or argue that an axiom update is necessary;
- install `a = 1` or any other continuation as a physical law;
- deny that a later bridge may supply a clock map;
- claim that Lorentzian reconstruction, boost generators, or OS
  reconstruction are impossible;
- vary `c_t / c_s` or reopen the Euclidean isotropy primitive;
- identify `κ(a)` with a mass ratio, coupling, or empirical fit;
- exhaust nonlinear clock maps.

The scope is the exact gap: the primitive supplies `c_t = c_s` in
Euclidean form, not the Record/Wick parameter `a`.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| primitive sentence `c_t = c_s` and OS0 wording | premise | quoted; no edit |
| primitive non-amendment of the four axioms | premise | quoted; no edit |
| axiom memo: `Z^3` Lattice; Admissibility does not define a time metric | premise | quoted; no edit |
| Euclidean TT form `(k4^2+k^2)/4` and family `Q_a` | declared algebra | computed here |
| physical Record/Wick clock map | escape route | live, not derived |

The exact advance is a finite continuation-versus-isotropy theorem.
Independent audit remains required before any effective status may
change.

## Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | Whether Euclidean kinetic isotropy already selects a Lorentzian clock map. It does not, on the displayed linear family. |
| V2 | New content? | Yes: the family `Q_a`, the three-value coefficient table, and the source-sentence pin that `a` is un-named. |
| V3 | Independently checkable? | Yes. The runner substitutes `k4 = i a ω` in exact arithmetic and re-reads the two source notes. |
| V4 | More than a restatement? | Yes. Quoting `c_t = c_s` does not by itself produce the triple `1/16, 1/4, 1`. |
| V5 | One-step relabel? | No. The Euclidean polynomial and the Lorentzian coefficients are different functions on the same family. |

## Primary Runner

[`scripts/kinetic_isotropy_does_not_fix_lorentzian_clock_map_2026_08_13.py`](../scripts/kinetic_isotropy_does_not_fix_lorentzian_clock_map_2026_08_13.py)
recomputes the Euclidean TT polynomial, the continuation `k4 = i a ω`,
the three Lorentzian coefficients, and the source-sentence pins in
exact arithmetic.
