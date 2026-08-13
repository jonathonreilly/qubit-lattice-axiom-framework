# Cl(3) Volume Elements +ω and −ω Are Not Axiom-Selected

**Date:** 2026-08-13
**Type:** bounded_theorem
**Claim scope:** on the real Clifford algebra `Cl(3,0)`, the two opposite
volume elements `ω := e1 e2 e3` and `ω' := e3 e2 e1` satisfy `ω' = −ω`,
are both odd and central, and are square-equal (`ω² = (−ω)² = −I`). Proper
cubic rotations preserve both signs. No axiom-selected structure on the
current Lattice/Qubit wording distinguishes `+ω` from `−ω`. The extra
object for an orientation is a displayed choice `s ∈ {+1, −1}` with
oriented volume `s ω`. This note does not add a chirality axiom and does
not reopen the parent odd-`d_t` restriction.
**Status authority:** independent audit lane only. This source note does
not set or predict an audit outcome.
**Primary runner:**
[`scripts/cl3_volume_elements_plus_minus_not_axiom_selected_2026_08_13.py`](../scripts/cl3_volume_elements_plus_minus_not_axiom_selected_2026_08_13.py)

This block is the orientation `Z2` on `Cl(3,0)`. It is independent of the
May 10 chirality-existence statement (a square-normalized anticommuting
element exists iff total dimension `n` is even) and of any in-flight
carrier work. The only parent algebra reused here is the May 10 odd-`n`
centrality rule, applied at `n = 3`.

## Parents

- [`CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md`](CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md)
  — volume-element (anti)commutation rule `(V)` and the odd-`n` centrality
  of `ω`.
- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) — Lattice
  proper cubic rotations; Qubit `Cl(3,0)`-compatible real-algebra
  presentation.

## Algebra

Let `Cl(3,0)` be the real Clifford algebra on generators `e1, e2, e3`
satisfying

```text
{ ei, ej }  =  2 δ_{ij} I.
```

Define the volume element and the opposite-order volume element by

```text
ω   :=  e1 e2 e3,
ω'  :=  e3 e2 e1.
```

All identities below are exact integer Clifford arithmetic: abstract
anticommutators on the eight-dimensional integer span, with a 2×2 Pauli
model exhibited as a faithful check.

## Theorem 1

`ω' = −ω`.

**Proof.** Three adjacent transpositions, each from `{ei, ej} = 0` for
`i ≠ j`:

```text
ω'  =  e3 e2 e1
    =  − e2 e3 e1          (swap e3 past e2)
    =    e2 e1 e3          (swap e3 past e1)
    =  − e1 e2 e3          =  −ω.
```

The same identity is the explicit product `e3 e2 e1` in the integer
basis.

Both products are grade-odd (three generators). The parent May 10 rule
`(V)` says `ω γ_μ = (−1)^{n−1} γ_μ ω`. At `n = 3` (odd),
`(−1)^{n−1} = +1`, so `ω` is central: it commutes with every generator.
Then `ω' = −ω` is the other central orientation. Direct check for `e1`:

```text
ω e1  =  e1 e2 e3 e1  =  e1 e2 (− e1 e3)  =  − e1 (e2 e1) e3
      =  − e1 (− e1 e2) e3  =  (e1 e1) e2 e3  =  e2 e3,
e1 ω  =  e1 e1 e2 e3  =  e2 e3.
```

The `e2` and `e3` calculations are cyclic. Centrality of `−ω` is
immediate.

## Theorem 2

On this real `Cl(3,0)` convention, `ω² = −I`. Consequently
`(−ω)² = ω² = −I`. The two orientations are square-equal. Neither is
distinguished by the value of the square.

**Proof.** Move generators through by the same anticommutators:

```text
ω²  =  e1 e2 e3 e1 e2 e3
    =  e1 e2 (− e1 e3) e2 e3
    =  − e1 (e2 e1) e3 e2 e3
    =  − e1 (− e1 e2) e3 e2 e3
    =  e1 e1 e2 e3 e2 e3
    =  e2 (e3 e2) e3
    =  e2 (− e2 e3) e3
    =  − (e2 e2) (e3 e3)
    =  − I.
```

Then `(−ω)² = ω² = −I`.

**Pauli model.** The standard 2×2 Pauli matrices `e_i = σ_i` realize the
same relations over `Z[i]`:

```text
σ1 σ2 σ3  =  i I,     (σ1 σ2 σ3)²  =  i² I  =  −I,
(− σ1 σ2 σ3)²  =  (−i I)²  =  i² I  =  −I.
```

The model confirms the abstract square. It does not add a sign
selection: both `+i I` and `−i I` square to `−I`.

## Theorem 3

Qubit states: “A `Cl(3,0)`-compatible real-algebra presentation may be
used equivalently and adds no further primitive structure.” Lattice
supplies proper cubic rotations (orientation-preserving) about each
site. A proper rotation `R` (det `=+1`) acts on the volume by

```text
R(ω)   =  R(e1) R(e2) R(e3)  =  (det R) ω  =  +ω,
R(−ω)  =  − R(ω)             =  −ω.
```

Proper cubic rotations therefore preserve `ω` and also preserve `−ω`.
Covariance under the supplied Lattice symmetry does not pick the sign.
(An improper map with det `= −1` exchanges the two signs; the axiom
wording names only proper cubic rotations.)

## Theorem 4 (missing-input)

The extra object for an orientation is a choice `s ∈ {+1, −1}` with
oriented volume `s ω`. This note displays that pair. It does not add a
chirality axiom.

The May 10 parent already forces odd `d_t` for a spacetime volume that
admits a square-normalized anticommuting chirality element. This note
does not reopen `d_t`. The present `Z2` is the residual sign of the
spatial `Cl(3,0)` volume after that parent dichotomy is granted.

## Theorem 5

Do not identify `s` with the sign of weak hypercharge, with a gravity
orientation, or with a fifth framework axiom. Those identifications are
outside the algebra checked here. The displayed pair `{+ω, −ω}` is only
the orientation `Z2` of `Cl(3,0)`.

## What this claims

- Identity: `ω' = −ω` by three transpositions.
- Both volume elements are odd and central at `n = 3`.
- Square identity: `ω² = (−ω)² = −I` on real `Cl(3,0)`; the Pauli model
  exhibits the same square.
- Proper cubic rotations preserve both signs, so Lattice covariance does
  not select `s`.
- Qubit adds no further primitive that would select `s`.
- The missing input is the displayed choice `s ∈ {+1, −1}`.

## What this does not claim

- Does not add, propose, or adopt a chirality axiom or any fifth axiom.
- Does not identify `s` with weak hypercharge sign or gravity
  orientation.
- Does not reopen `d_t`, does not claim `d_t = 1`, and does not reuse
  the May 10 chirality-existence theorem beyond odd-`n` centrality.
- Does not select a preferred faithful irrep (`χ = +i` versus `χ = −i`)
  and does not identify the spatial volume sign with staggered
  `ε(x)`, generation handedness, or a spacetime `γ5`.
- Does not edit the axiom memo.

## Forbidden imports check

- No PDG values, fitted selectors, or unit conventions.
- No unmerged-PR citations.
- No observational inputs.

## Validation

Primary runner:
[`scripts/cl3_volume_elements_plus_minus_not_axiom_selected_2026_08_13.py`](../scripts/cl3_volume_elements_plus_minus_not_axiom_selected_2026_08_13.py)

The runner uses exact integer Clifford arithmetic (abstract
anticommutators on `Z^8`, plus a 2×2 Pauli model over Gaussian
integers). Identity gates call `volume()` and `volume_opp()`. A
predicate `ω' ≠ −ω` fails. A predicate `ω² ≠ (−ω)²` fails. Declared
inputs are this note, the May 10 parent, and the axiom memo.
