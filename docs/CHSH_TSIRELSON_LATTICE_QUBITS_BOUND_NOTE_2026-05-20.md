# Tsirelson Bound on Lattice Qubit Pairs

**Date:** 2026-05-20
**Type:** bounded_theorem candidate
**Status:** source-side proposal — independent audit lane owns the verdict
**Companion to:** retained
[`CHSH_STRUCTURAL_BOUND_NARROW_THEOREM_NOTE_2026-05-17.md`](CHSH_STRUCTURAL_BOUND_NARROW_THEOREM_NOTE_2026-05-17.md)
(`retained`, positive_theorem). The existing retained note establishes
the structural CHSH bound; this companion identifies the maximum
violation explicitly as Tsirelson's bound `2√2` on the
qubit-lattice substrate.

## Claim

For any pair of single-qubit operators
`A_1, A_2 ∈ M_2(ℂ)_x` and `B_1, B_2 ∈ M_2(ℂ)_y` at distinct
sites `x ≠ y` on `Z^3` (so `[A_i, B_j] = 0` by microcausality), with
each operator self-adjoint and bounded in operator norm
`‖A_i‖, ‖B_j‖ ≤ 1`, the CHSH combination

```text
C := A_1 ⊗ B_1 + A_1 ⊗ B_2 + A_2 ⊗ B_1 − A_2 ⊗ B_2                       (1)
```

acts on `H_x ⊗ H_y = ℂ² ⊗ ℂ²` with operator norm bounded by
**Tsirelson's bound**

```text
‖C‖ ≤ 2√2 ≈ 2.828                                                        (2)
```

with equality achievable on a maximally entangled qubit pair using
the standard Tsirelson configuration. This is strictly tighter than
the classical Bell bound `‖C‖ ≤ 2` (Bell 1964) but strictly looser
than the algebraic bound `‖C‖ ≤ 4` (general-probability-theory).

The framework's qubit-lattice substrate (A1+A2 of
[`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md))
**saturates Tsirelson's bound** at maximally entangled site pairs —
the lattice is genuinely quantum-mechanical (not a hidden-variable
theory), and not super-quantum (not a Popescu-Rohrlich-box theory).

## Setup

By A1, the per-site operator algebra is `M_2(ℂ)`. By A2, sites are
indexed by `Z^3` and compose by tensor product. For a pair of
distinct sites `x ≠ y`, the joint Hilbert space is
`H_{xy} = ℂ²_x ⊗ ℂ²_y` (4-dimensional) and the joint operator
algebra is `A_{xy} = M_2(ℂ)_x ⊗ M_2(ℂ)_y = M_4(ℂ)`.

By microcausality
([`LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md`](LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md),
retained), operators at distinct sites commute:
`[A_i ⊗ 𝟙, 𝟙 ⊗ B_j] = 0`.

A CHSH operator (1) is a linear combination of four tensor products
of self-adjoint single-qubit operators on each site.

## Step 1 — Tsirelson's algebraic argument

Define
`C^2 = C · C` where `C` is from (1). Direct expansion using
`A_i ⊗ B_j` notation:

```text
C^2 = (A_1 ⊗ B_1 + A_1 ⊗ B_2 + A_2 ⊗ B_1 − A_2 ⊗ B_2)²                  (3)
```

Expanding and using `[A_i ⊗ 𝟙, 𝟙 ⊗ B_j] = 0` (microcausality
splits site factors into commuting factors):

```text
C^2 = (A_1² + A_2²) ⊗ (B_1² + B_2²) + [A_1, A_2] ⊗ [B_1, B_2]            (4)
```

(Tsirelson's 1980 expansion.) For self-adjoint `A_i, B_j` with
`‖A_i‖, ‖B_j‖ ≤ 1`, we have `A_i² ≤ 𝟙` and `B_j² ≤ 𝟙`. Therefore

```text
‖A_1² + A_2²‖ ≤ 2,   ‖B_1² + B_2²‖ ≤ 2                                  (5)
```

For the commutator terms `[A_1, A_2]` and `[B_1, B_2]` (self-adjoint
single-qubit operators with norm ≤ 1), Tsirelson's bound on
single-qubit commutators is:

```text
‖[A_1, A_2]‖ ≤ 2,   ‖[B_1, B_2]‖ ≤ 2                                    (6)
```

(Pauli-algebra fact: for `A_1 = σ_1`, `A_2 = σ_2`, the commutator
`[σ_1, σ_2] = 2iσ_3` has norm 2.)

Combining (4), (5), (6):

```text
‖C^2‖ ≤ 2 · 2 + 2 · 2 = 8                                                (7)
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
the joint two-qubit Hilbert space `ℂ² ⊗ ℂ²` (A1+A2 supplies the
state space; no gate is required).

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
and saturates it (Step 2). It is **genuinely quantum** (achieves
violations beyond the Bell bound) and **not super-quantum** (does
not achieve the PR-box bound).

## Step 4 — Lattice extension and multi-site Tsirelson chains

For pairs of distant sites `x, y ∈ Z^3`, the Tsirelson bound `2√2`
holds **uniformly** — the algebraic argument (Step 1) is per-pair
and does not depend on the spatial distance. So the framework's
qubit lattice admits Tsirelson-saturating Bell pairs at any
spacelike-separated pair of sites.

For multi-site chains and CHSH-like inequalities with more parties,
analogous bounds exist (Wehner et al.; Brunner et al.). Those are
out of scope of this note; the result here is the **pair-wise
Tsirelson bound**.

## What this closes

- The pair-wise Tsirelson identification on the framework's qubit
  lattice — making explicit that the framework's quantum content is
  exactly that of standard quantum mechanics on qubits (saturates
  Tsirelson, does not exceed it).

## What this does not close

- **Multi-party Bell extensions** (3-site, 4-site, etc.) — beyond
  scope.
- **Sharper bounds under additional constraints** (e.g., dimension
  witnesses, communication complexity) — beyond scope.
- **Experimental Bell test reproductions** on the framework's
  predictions — out of theory-side scope.

## Admitted inputs

1. **Microcausality on the qubit lattice** — retained via
   `LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10`.
2. **Tsirelson 1980 algebraic argument** — standard quantum-information
   result; the framework cites the standard derivation.
3. **Standard operator-norm bounds on Pauli commutators** — textbook
   matrix algebra.

## Risk classification

This is a `bounded_theorem` candidate. The argument is textbook
quantum-information theory (Tsirelson 1980; Nielsen-Chuang Ch.2;
Watrous Ch.11). The narrow contribution is the explicit
identification that the framework's qubit-lattice substrate
saturates Tsirelson's bound, situating the framework
unambiguously between classical Bell and super-quantum PR.

## Citation-graph note

**Upstream framework dependencies** (load-bearing; markdown links):

- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) — supplies A1+A2 (qubit-form local algebra + Z^3 substrate)
- [`CHSH_STRUCTURAL_BOUND_NARROW_THEOREM_NOTE_2026-05-17.md`](CHSH_STRUCTURAL_BOUND_NARROW_THEOREM_NOTE_2026-05-17.md) — retained companion supplying the structural CHSH bound this note tightens to Tsirelson
- [`LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md`](LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md) — supplies microcausality for the commuting-site-factors step

**Upstream standard-math imports** (named non-derivation):

- Tsirelson 1980 *Lett. Math. Phys.* 4, 93 — original Tsirelson bound proof
- Bell 1964 *Physics* 1, 195 — classical Bell bound (comparison only)
- Popescu-Rohrlich 1994 *Found. Phys.* 24, 379 — super-quantum PR-box bound (comparison only)

**Plain-text pointer references** (NOT load-bearing deps):

- Standard QI textbook treatments (Nielsen-Chuang Ch.2; Watrous Ch.11; Wilde Ch.13)

## What this file is not

- Not a derivation of Tsirelson's theorem from A1+A2 (the theorem itself is standard QI; the framework cites it)
- Not a multi-party Bell extension
- Not an experimental claim
- Not a numerical-prediction change
- Not a unilateral retagging
