# Tsirelson Bound on Lattice Qubit Pairs

**Date:** 2026-05-20
**Date of scope repair:** 2026-05-30
**Date of tensor-carrier dependency repair:** 2026-06-06
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Status:** source-side proposal — independent audit lane owns the verdict
**Primary runner:** [`scripts/audit_companion_chsh_tsirelson_lattice_qubits_bound_2026_05_20.py`](../scripts/audit_companion_chsh_tsirelson_lattice_qubits_bound_2026_05_20.py)
**Cached runner output:** [`logs/runner-cache/audit_companion_chsh_tsirelson_lattice_qubits_bound_2026_05_20.txt`](../logs/runner-cache/audit_companion_chsh_tsirelson_lattice_qubits_bound_2026_05_20.txt)
**Two-site tensor-carrier bridge:** [`TWO_SITE_QUBIT_TENSOR_CARRIER_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md`](TWO_SITE_QUBIT_TENSOR_CARRIER_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md)
**Companion to:** retained
[`CHSH_STRUCTURAL_BOUND_NARROW_THEOREM_NOTE_2026-05-17.md`](CHSH_STRUCTURAL_BOUND_NARROW_THEOREM_NOTE_2026-05-17.md)
(`retained`, positive_theorem). The existing retained note establishes
the structural CHSH bound; this companion identifies the maximum
violation explicitly as Tsirelson's bound `2√2` on the
qubit-lattice substrate.

## Claim

For any pair of dichotomic single-qubit observables
`A_1, A_2 ∈ M_2(ℂ)_x` and `B_1, B_2 ∈ M_2(ℂ)_y` at distinct
sites `x ≠ y` on `Z^3` (so `[A_i, B_j] = 0` by tensor locality), with
each operator self-adjoint and involutive
`A_i² = B_j² = 𝟙`, the CHSH combination

```text
C := A_1 ⊗ B_1 + A_1 ⊗ B_2 + A_2 ⊗ B_1 − A_2 ⊗ B_2                       (1)
```

acts on `H_x ⊗ H_y = ℂ² ⊗ ℂ²` with operator norm bounded by
**Tsirelson's bound**

```text
‖C‖ ≤ 2√2 ≈ 2.828                                                        (2)
```

with equality achievable on a maximally entangled qubit pair using
the standard Tsirelson configuration. This is the standard two-outcome
CHSH surface: it is strictly looser than the classical Bell bound
`‖C‖ ≤ 2` (Bell 1964) but strictly tighter than the algebraic/no-signaling
bound `‖C‖ ≤ 4` (general-probability-theory).

The framework's finite two-site qubit tensor surface, routed through the
two-site tensor-carrier bridge above, has state-space witnesses that
**saturate Tsirelson's bound** at maximally entangled site pairs. This is a
kinematic operator-algebra statement, not a claim that framework dynamics
prepares those Bell pairs.

## Setup

By the current Quantum axiom in
[`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md), the
per-site operator algebra is `M_2(ℂ)`. By the two-site tensor-carrier
bridge
[`TWO_SITE_QUBIT_TENSOR_CARRIER_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md`](TWO_SITE_QUBIT_TENSOR_CARRIER_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md),
the retained finite-block tensor surface specializes at distinct sites
`x ≠ y` to the joint Hilbert space
`H_{xy} = ℂ²_x ⊗ ℂ²_y` (4-dimensional) and joint operator algebra
`A_{xy} = M_2(ℂ)_x ⊗ M_2(ℂ)_y = M_4(ℂ)`.

This routing is not a derivation from operational locality alone. The
retained no-go
[`TENSOR_COMPOSITION_REQUIRES_LOCAL_TOMOGRAPHY_BEYOND_LOCALITY_NARROW_NO_GO_NOTE_2026-06-03.md`](TENSOR_COMPOSITION_REQUIRES_LOCAL_TOMOGRAPHY_BEYOND_LOCALITY_NARROW_NO_GO_NOTE_2026-06-03.md)
keeps that boundary explicit: locality alone does not force the ordinary
generated tensor product.

By tensor locality
([`LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md`](LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md),
retained), operators at distinct sites commute:
`[A_i ⊗ 𝟙, 𝟙 ⊗ B_j] = 0`.

A CHSH operator (1) is a linear combination of four tensor products
of dichotomic self-adjoint single-qubit observables on each site.

## Step 1 — Tsirelson's algebraic argument

Define `C^2 = C · C` where `C` is from (1), and write
`X = B_1 + B_2`, `Y = B_1 - B_2`, so `C = A_1 ⊗ X + A_2 ⊗ Y`.
The two site factors commute by tensor locality, but `A_1` need not commute
with `A_2` and `B_1` need not commute with `B_2`. Direct expansion gives

```text
C^2 = A_1^2 ⊗ X^2 + A_2^2 ⊗ Y^2
      + A_1 A_2 ⊗ X Y + A_2 A_1 ⊗ Y X.                                  (3)
```

For dichotomic observables, `A_i^2 = B_j^2 = 𝟙`, hence

```text
X^2 + Y^2 = (B_1 + B_2)^2 + (B_1 - B_2)^2 = 4𝟙,
X Y = -[B_1, B_2],       Y X = [B_1, B_2].
```

Substitution yields the Landau/Tsirelson square identity for this
plus/plus/plus/minus CHSH convention:

```text
C^2 = 4𝟙 − [A_1, A_2] ⊗ [B_1, B_2].                                      (4)
```

For self-adjoint involutions, `‖A_i‖ = ‖B_j‖ = 1`, so the elementary
submultiplicative norm bound gives

```text
‖[A_1, A_2]‖ ≤ ‖A_1 A_2‖ + ‖A_2 A_1‖ ≤ 2,
‖[B_1, B_2]‖ ≤ ‖B_1 B_2‖ + ‖B_2 B_1‖ ≤ 2.                                (5)
```

Since `C` is self-adjoint, `‖C‖^2 = ‖C^2‖`. Combining (4) and (5),

```text
‖C‖^2 = ‖C^2‖ ≤ 4 + ‖[A_1, A_2]‖ ‖[B_1, B_2]‖ ≤ 8.                       (6)
```

Therefore `‖C‖ ≤ √8 = 2√2`. ✓

## Step 2 — Saturation at maximally entangled qubit pairs

The bound `‖C‖ = 2√2` is achievable with the standard configuration:

- `A_1 = σ_z`, `A_2 = σ_x` at site `x`
- `B_1 = (σ_z + σ_x)/√2`, `B_2 = (σ_z − σ_x)/√2` at site `y`
- Joint state `|Φ⁺⟩ = (|00⟩ + |11⟩)/√2`, the Bell state on the
  two-qubit pair

Direct computation gives `⟨Φ⁺| C |Φ⁺⟩ = 2√2`, saturating
Tsirelson's bound. The Bell state `|Φ⁺⟩` is a valid pure state on
the joint two-qubit Hilbert space `ℂ² ⊗ ℂ²`; this is a state-space
witness only, not a claim about dynamical preparation.

## Step 3 — Comparison to the classical Bell bound and PR-box bound

For comparison:

- **Classical Bell bound** (Bell 1964): under any local hidden-variable
  theory, `‖C‖_classical ≤ 2`. Saturated by deterministic strategies
  on classical bits.
- **Tsirelson bound** (Tsirelson 1980, this note): on the qubit
  lattice, `‖C‖_quantum ≤ 2√2`. Saturated by Bell states (Step 2).
- **Popescu-Rohrlich-box bound** (Popescu-Rohrlich 1994): under any
  no-signaling correlation, `‖C‖_PR ≤ 4`. Saturated by PR boxes,
  which are not realizable by quantum mechanics.

The framework's qubit lattice respects the Tsirelson bound (Step 1)
and contains state-space witnesses that saturate it (Step 2). It has
the standard qubit-quantum CHSH surface and does not contain
super-quantum PR-box correlations.

## Step 4 — Lattice extension and multi-site Tsirelson chains

For pairs of distinct sites `x, y ∈ Z^3`, the Tsirelson bound `2√2`
holds **uniformly** — the algebraic argument (Step 1) is per-pair
and does not depend on the spatial distance. So the framework's
qubit lattice admits Tsirelson-saturating state-space witnesses at any
distinct pair of sites.

For multi-site chains and CHSH-like inequalities with more parties,
analogous bounds exist (Wehner et al.; Brunner et al.). Those are
out of scope of this note; the result here is the **pair-wise
Tsirelson bound**.

## What this closes

- The pair-wise Tsirelson identification on the framework's qubit
  lattice for dichotomic two-outcome qubit observables. It makes
  explicit that this CHSH surface is standard qubit quantum mechanics:
  it has Tsirelson-saturating state-space witnesses and does not
  exceed the Tsirelson bound.

## What this does not close

- **Multi-party Bell extensions** (3-site, 4-site, etc.) — beyond
  scope.
- **Sharper bounds under additional constraints** (e.g., dimension
  witnesses, communication complexity) — beyond scope.
- **Experimental Bell test reproductions** on the framework's
  predictions — out of theory-side scope.

## Admitted inputs

1. **Two-site qubit tensor carrier and Bell vector state space** — routed
   through
   [`TWO_SITE_QUBIT_TENSOR_CARRIER_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md`](TWO_SITE_QUBIT_TENSOR_CARRIER_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md).
2. **Tensor locality on the qubit lattice** — retained via
   `LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10`.
3. **Landau/Tsirelson square identity and commutator norm bound** — derived
   above as finite-dimensional operator algebra on the framework two-site
   tensor surface; Tsirelson 1980 and standard QI texts are cited in parallel,
   not imported as load-bearing authority.
4. **Pauli/Bell saturation witness** — verified directly by the companion
   runner on `M_2(C) ⊗ M_2(C)`.

## Risk classification

This is a `bounded_theorem` candidate. The proof is finite-dimensional
operator algebra over the retained two-site tensor surface, with the
Landau/Tsirelson identity derived explicitly above and checked by the
companion runner. Tsirelson 1980 and standard quantum-information texts are
parallel citations. The narrow contribution is the explicit identification
that the framework's qubit-lattice substrate has Tsirelson-saturating
state-space witnesses while obeying the Tsirelson upper bound, situating this
CHSH surface between classical Bell and super-quantum PR.

## Citation-graph note

**Upstream framework dependencies** (load-bearing; markdown links):

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) — supplies the current Lattice and Quantum axiom wording
- [`TWO_SITE_QUBIT_TENSOR_CARRIER_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md`](TWO_SITE_QUBIT_TENSOR_CARRIER_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md) — supplies the distinct-site `C²_x ⊗ C²_y` carrier, generated `M_4(C)` algebra, and Bell-vector state-space witness surface
- [`CHSH_STRUCTURAL_BOUND_NARROW_THEOREM_NOTE_2026-05-17.md`](CHSH_STRUCTURAL_BOUND_NARROW_THEOREM_NOTE_2026-05-17.md) — retained companion supplying the structural CHSH bound this note tightens to Tsirelson
- [`LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md`](LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md) — supplies tensor locality for the commuting-site-factors step
- [`TENSOR_COMPOSITION_REQUIRES_LOCAL_TOMOGRAPHY_BEYOND_LOCALITY_NARROW_NO_GO_NOTE_2026-06-03.md`](TENSOR_COMPOSITION_REQUIRES_LOCAL_TOMOGRAPHY_BEYOND_LOCALITY_NARROW_NO_GO_NOTE_2026-06-03.md) — negative boundary showing that locality alone is not the tensor-composition proof route

**Upstream standard-math imports** (named non-derivation):

- Tsirelson 1980 *Lett. Math. Phys.* 4, 93 — original Tsirelson bound proof
  (parallel citation; the identity is derived in this note)
- Bell 1964 *Physics* 1, 195 — classical Bell bound (comparison only)
- Popescu-Rohrlich 1994 *Found. Phys.* 24, 379 — super-quantum PR-box bound (comparison only)

**Plain-text pointer references** (NOT load-bearing deps):

- Standard QI textbook treatments (Nielsen-Chuang Ch.2; Watrous Ch.11; Wilde Ch.13)

## What this file is not

- Not a new axiom or imported theorem gate; the pair-wise Tsirelson bound is
  derived here as finite-dimensional two-site operator algebra, with standard
  literature cited in parallel
- Not a multi-party Bell extension
- Not an experimental claim
- Not a numerical-prediction change
- Not a unilateral retagging
