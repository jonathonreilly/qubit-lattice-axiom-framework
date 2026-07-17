# Structural CHSH Bound — Narrow Theorem (Classical 2, Tsirelson 2√2)

**Date:** 2026-05-17
**Type:** positive_theorem
**Class:** `positive_theorem` (Class A — pure algebra over retained primitives)
**Lane:** bell / foundational QM
**Block:** physics-loop / block09 / 2026-05-17 / bell-inequality-derivation
**Source note:** `docs/CHSH_STRUCTURAL_BOUND_NARROW_THEOREM_NOTE_2026-05-17.md`
**Runner:** `scripts/audit_companion_chsh_structural_bound_narrow_exact_2026_05_17.py`
**Cache:** `logs/runner-cache/chsh_structural_bound_narrow_2026_05_17.txt`

## Scope

This note derives the **structural** CHSH bounds purely from algebraic
primitives. It is a narrow algebra theorem, not a framework-Hamiltonian
saturation theorem.

Specifically it proves two separate algebraic facts:

1. **Classical CHSH bound.** For any local hidden-variable model
   assigning four `{±1}`-valued observables `(A_0, A_1, B_0, B_1)` to a
   shared classical state `λ ∈ Λ` (with arbitrary distribution `p(λ)`),
   the CHSH combinant
   `S = ⟨A_0 B_0⟩ + ⟨A_0 B_1⟩ + ⟨A_1 B_0⟩ − ⟨A_1 B_1⟩`
   satisfies `|S| ≤ 2`. (Bell/CHSH, 1969 form.)

2. **Tsirelson (quantum) bound.** For any tensor-product Hilbert space
   `H_A ⊗ H_B`, any self-adjoint involutions `A_i = A_i^* ` with
   `A_i^2 = I` on `H_A` and `B_j = B_j^*` with `B_j^2 = I` on `H_B`,
   any pure state `|ψ⟩ ∈ H_A ⊗ H_B`, and the lifted observables
   `Ã_i = A_i ⊗ I`, `B̃_j = I ⊗ B_j` (so `[Ã_i, B̃_j] = 0` automatically),
   the CHSH operator
   `S_op = Ã_0 B̃_0 + Ã_0 B̃_1 + Ã_1 B̃_0 − Ã_1 B̃_1`
   satisfies `‖S_op‖ ≤ 2√2`, hence `|⟨ψ| S_op |ψ⟩| ≤ 2√2`.

Both bounds are *upper bounds on the maximum |S|*. The classical bound
is the inequality that local realism enforces; the Tsirelson bound is
the inequality that any tensor-product Hilbert quantum model enforces.

## Why this is a G→C **partial** reduction

The current `bell_inequality_derived_note` (`audited_numerical_match`,
class G) shows that a specific framework Hamiltonian on small two-species
staggered-fermion lattices reaches `|S| ≈ 2.823` (close to `2√2`) at
selected couplings, with `G = 0` giving exactly `|S| = 2`. The audit
flags two distinct sub-questions:

| Sub-question | Status before this note | Status after this note |
|---|---|---|
| (a) Is the **structural inequality** `|S_quantum| ≤ 2√2` derivable? | Tacit / unverified | **Derived from retained primitives (class A)** |
| (b) Is `G=0 ⇒ |S|=2` derivable as a no-entanglement consequence? | Tacit / unverified | **Derived: separable state on tensor bipartition saturates classical bound only** |
| (c) Does the framework Hamiltonian saturate `2√2` for derived (not tuned) couplings? | Open — remains G-class | Still open — out of scope of this narrow theorem |
| (d) Does the framework give a physical normalization of G? | Open | Still open — out of scope |

This note closes (a) and (b) cleanly. It does **not** close (c) or (d);
those remain as the residual G-class content of
`bell_inequality_derived_note` and are explicitly out of scope here.

## Retained primitives consumed

The proof uses only the following retained inputs:

| Primitive | Status | Used for |
|---|---|---|
| `i3_zero_exact_theorem_note` (Born quadratic surface `P=|A|^2`) | retained (class A) | `⟨O⟩ = ⟨ψ|O|ψ⟩` expectation |
| Tensor product `H_A ⊗ H_B` for two distinguishable subsystems | retained (SINGLE_AXIOM_HILBERT_NOTE) | automatic `[Ã_i, B̃_j] = 0` |
| Cl(3) per-site Hilbert dimension two | retained_bounded (`cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02`) | minimal nontrivial `H_A`, `H_B` realisation; eigenvalues ±1 of Pauli involutions |
| Anticommuting `{Z, X} = 0` involutions in Cl(3) taste algebra | retained (`fermion_parity_pauli_tensor_involution_narrow_theorem_note_2026-05-10`, `koide_anticommuting_operator_derivation_theorem_note_2026-05-10`) | exhibits saturating witness on `C^2 ⊗ C^2` |

No new axioms, no fitted parameters, no observational comparator, no
literature import.

## Proof

### Part 1 — Classical CHSH bound `|S| ≤ 2`

Let `λ ~ p(λ)` be a classical hidden variable on a measurable space `Λ`.
Each measurement setting deterministically returns `A_i(λ), B_j(λ) ∈ {-1, +1}`.

Define `S(λ) = A_0(λ) B_0(λ) + A_0(λ) B_1(λ) + A_1(λ) B_0(λ) − A_1(λ) B_1(λ)`.

Factor:
```
S(λ) = A_0(λ) [B_0(λ) + B_1(λ)] + A_1(λ) [B_0(λ) − B_1(λ)]
```

Since `B_0(λ), B_1(λ) ∈ {-1, +1}`, exactly one of `B_0(λ) + B_1(λ)` and
`B_0(λ) − B_1(λ)` equals zero, and the other equals `±2`. Combined with
`A_i(λ) ∈ {-1, +1}`, this gives `S(λ) ∈ {-2, +2}` pointwise, hence
`|S(λ)| ≤ 2` for every `λ`.

By linearity of expectation: `S = ⟨S(λ)⟩_λ`, so
```
|S| ≤ ⟨|S(λ)|⟩_λ ≤ 2.
```

This is pure case analysis on `{-1, +1}^4`. **QED Part 1.**

(The case enumeration is 16 sign assignments to `(A_0, A_1, B_0, B_1)`;
each one gives `S ∈ {-2, 0, +2}`, so the maximum modulus is exactly 2.
This is exhaustively checked in the runner.)

### Part 2 — Tsirelson bound `‖S_op‖ ≤ 2√2`

We follow Landau (1987) and Tsirelson (1980). Let `Ã_i = A_i ⊗ I` and
`B̃_j = I ⊗ B_j` with `A_i^2 = I` on `H_A` and `B_j^2 = I` on `H_B`
(self-adjoint involutions). Then `Ã_i^2 = I` on `H_A ⊗ H_B`, similarly
`B̃_j^2 = I`, and `[Ã_i, B̃_j] = 0` for all `i, j` because they act on
disjoint tensor factors.

Define `S_op = Ã_0 B̃_0 + Ã_0 B̃_1 + Ã_1 B̃_0 − Ã_1 B̃_1`. Compute
`S_op^2` carefully using the commutation `[Ã_i, B̃_j] = 0`:

```
S_op = Ã_0 (B̃_0 + B̃_1) + Ã_1 (B̃_0 − B̃_1)
```

Squaring:
```
S_op^2 = Ã_0^2 (B̃_0 + B̃_1)^2 + Ã_1^2 (B̃_0 − B̃_1)^2
       + Ã_0 Ã_1 (B̃_0 + B̃_1)(B̃_0 − B̃_1)
       + Ã_1 Ã_0 (B̃_0 − B̃_1)(B̃_0 + B̃_1).
```

Using `Ã_i^2 = I` and expanding the B-products:
```
(B̃_0 + B̃_1)^2 = B̃_0^2 + B̃_0 B̃_1 + B̃_1 B̃_0 + B̃_1^2 = 2I + {B̃_0, B̃_1}
(B̃_0 − B̃_1)^2 = B̃_0^2 − B̃_0 B̃_1 − B̃_1 B̃_0 + B̃_1^2 = 2I − {B̃_0, B̃_1}
```

Sum: `(B̃_0+B̃_1)^2 + (B̃_0−B̃_1)^2 = 4I`. So
```
Ã_0^2 (B̃_0 + B̃_1)^2 + Ã_1^2 (B̃_0 − B̃_1)^2 = 4I.
```

For the cross terms:
```
(B̃_0 + B̃_1)(B̃_0 − B̃_1) = B̃_0^2 − B̃_0 B̃_1 + B̃_1 B̃_0 − B̃_1^2 = −[B̃_0, B̃_1]
(B̃_0 − B̃_1)(B̃_0 + B̃_1) = B̃_0^2 + B̃_0 B̃_1 − B̃_1 B̃_0 − B̃_1^2 = +[B̃_0, B̃_1]
```

So the cross terms become
```
Ã_0 Ã_1 (B̃_0 + B̃_1)(B̃_0 − B̃_1) + Ã_1 Ã_0 (B̃_0 − B̃_1)(B̃_0 + B̃_1)
  = −Ã_0 Ã_1 [B̃_0, B̃_1] + Ã_1 Ã_0 [B̃_0, B̃_1]
  = −[Ã_0, Ã_1] [B̃_0, B̃_1]
```
(using `[B̃_0, B̃_1]` is the same operator both times, and grouping).

Putting it together:
```
S_op^2 = 4·I − [Ã_0, Ã_1] [B̃_0, B̃_1].
```

This is the **Landau identity**. It is exact, with no inequality so far.

Now estimate the operator norm of each commutator factor. For any two
self-adjoint involutions `X, Y` with `X^2 = Y^2 = I` and `‖X‖ = ‖Y‖ = 1`:
```
‖[X, Y]‖ = ‖XY − YX‖ ≤ ‖XY‖ + ‖YX‖ ≤ 2 ‖X‖ ‖Y‖ = 2.
```

Apply to `Ã_0, Ã_1` (acting nontrivially on the `H_A` factor only,
so `‖Ã_i‖ = ‖A_i‖ = 1`) and to `B̃_0, B̃_1` (similarly `‖B̃_j‖ = 1`):
```
‖[Ã_0, Ã_1]‖ ≤ 2,    ‖[B̃_0, B̃_1]‖ ≤ 2.
```

Therefore:
```
‖S_op^2‖ ≤ ‖4I‖ + ‖[Ã_0, Ã_1] [B̃_0, B̃_1]‖
        ≤ 4 + 2·2 = 8.
```

Since `S_op` is self-adjoint, `‖S_op^2‖ = ‖S_op‖^2`. So
```
‖S_op‖ ≤ √8 = 2√2.
```

Born expectation: `⟨ψ| S_op |ψ⟩` is real (self-adjoint operator) and
satisfies `|⟨ψ| S_op |ψ⟩| ≤ ‖S_op‖ ≤ 2√2` by the operator-norm bound on
expectations of self-adjoint operators against unit vectors. **QED Part 2.**

### Part 3 — Saturating witness exists in Cl(3) ⊗ Cl(3)

To verify the bound `2√2` is the tight upper bound (not a loose one),
exhibit a state and observables that saturate it. Take `H_A = H_B = C^2`
(Cl(3) per-site Hilbert dim two, retained). Take
```
A_0 = σ_z,    A_1 = σ_x,
B_0 = (σ_z + σ_x)/√2,    B_1 = (σ_z − σ_x)/√2.
```
All four are self-adjoint involutions with eigenvalues ±1 (standard
Pauli algebra). Take `|ψ⟩` = Bell state `(|00⟩ + |11⟩)/√2`.

Direct computation (verified in the runner):
```
⟨ψ| A_0 ⊗ B_0 |ψ⟩ = +1/√2
⟨ψ| A_0 ⊗ B_1 |ψ⟩ = +1/√2
⟨ψ| A_1 ⊗ B_0 |ψ⟩ = +1/√2
⟨ψ| A_1 ⊗ B_1 |ψ⟩ = −1/√2

S = 4·(1/√2) = 2√2.
```

So Tsirelson's bound `2√2` is **saturated** by an explicit witness using
only Cl(3) per-site Hilbert dim two (retained) and tensor product
bipartition (retained). The framework's Cl(3) primitive supplies the
required `(C^2, σ_z, σ_x)` directly.

### Part 4 — `G = 0` ⇒ `|S| = 2` (separable state corollary)

A product state `|ψ⟩ = |α⟩_A ⊗ |β⟩_B` admits the local decomposition
`p(λ) = δ(α) δ(β)`, `A_i(λ) = ⟨α| A_i |α⟩ · sign(...)`, ... formally
because for product states `⟨A_i ⊗ B_j⟩ = ⟨A_i⟩_α · ⟨B_j⟩_β` factors.

Substituting in `S`:
```
S = ⟨A_0⟩_α ⟨B_0⟩_β + ⟨A_0⟩_α ⟨B_1⟩_β + ⟨A_1⟩_α ⟨B_0⟩_β − ⟨A_1⟩_α ⟨B_1⟩_β
  = ⟨A_0⟩_α (⟨B_0⟩_β + ⟨B_1⟩_β) + ⟨A_1⟩_α (⟨B_0⟩_β − ⟨B_1⟩_β).
```

With `|⟨A_i⟩_α|, |⟨B_j⟩_β| ≤ 1`:
```
|S| ≤ |⟨B_0⟩_β + ⟨B_1⟩_β| + |⟨B_0⟩_β − ⟨B_1⟩_β|
    ≤ max over b_0, b_1 ∈ [-1,1] of |b_0 + b_1| + |b_0 − b_1|
    = 2.
```

The last equality is `max(|b_0+b_1| + |b_0−b_1|)` on `[-1,1]^2`, attained
at `(±1, ±1)` corners (e.g. `b_0 = 1, b_1 = -1` gives `0 + 2 = 2`; with
the same `A` factors saturating ±1 we recover `|S| ≤ 2`).

In particular, this matches the framework's `G = 0` runner result
`|S| = 2.000` exactly. Product (separable) initial state plus `G = 0`
means the Hamiltonian preserves separability (no entangling interaction),
so the runtime state stays product, so `|S| ≤ 2` follows from Part 4.

**QED Part 4.** This closes audit sub-question (b).

## What the runner verifies

The audit-companion runner
`scripts/audit_companion_chsh_structural_bound_narrow_exact_2026_05_17.py`
performs the following exact-precision checks:

1. **Part 1 exhaustive enumeration.** Enumerate all 16 sign-assignments
   `(A_0, A_1, B_0, B_1) ∈ {-1, +1}^4`. Compute `S` for each; verify
   `S ∈ {-2, 0, +2}` for all; verify `max |S| = 2`.

2. **Part 2 Landau identity (symbolic + numerical).** With `A_i, B_j`
   set to specific Pauli matrices, compute
   `S_op^2 − 4I + [A_0,A_1] ⊗ [B_0,B_1]` (using `Ã_i ⊗ I` and `I ⊗ B̃_j`
   structure). Verify equals zero matrix.

3. **Part 2 norm chain.** Compute `‖S_op‖` numerically for the Bell
   witness setup; verify `≤ 2√2` and equal to `2√2` for the saturating
   choice.

4. **Part 2 commutator norm.** Verify `‖[σ_z, σ_x]‖ = 2`, demonstrating
   the inequality `‖[X,Y]‖ ≤ 2` is tight for Pauli pairs.

5. **Part 3 saturating witness.** Construct Bell state `(|00⟩+|11⟩)/√2`
   and the four observables above; compute all four expectations
   `⟨A_i ⊗ B_j⟩` symbolically (sympy `Rational`/`sqrt`) and verify each
   equals `±1/√2`; sum to verify `S = 2√2` exactly.

6. **Part 4 product-state saturation.** Enumerate product-state
   expectations over a grid of `(⟨A_i⟩, ⟨B_j⟩) ∈ {-1, -1/2, 0, 1/2, 1}`
   and verify `|S| ≤ 2` for every grid point.

7. **Cross-check vs. retained.** Verify `{σ_z, σ_x} = 0` matches the
   anticommuting-operator retained input. Verify `σ_z^2 = σ_x^2 = I`
   (involution property).

8. **Boundary guard.** Print explicit list of things this theorem does
   NOT claim (framework Hamiltonian saturation, derived G normalization,
   continuum limit) to prevent downstream misuse.

## What this note explicitly does NOT claim

- Does NOT claim the framework Hamiltonian saturates Tsirelson's bound
  at *derived* (not tuned) couplings. The G-class status of the
  numerical-saturation question of `bell_inequality_derived_note`
  remains.
- Does NOT claim to derive a physical normalization of the gravitational
  coupling `G` or its continuum scaling.
- Does NOT close the audit on `bell_inequality_derived_note` from G to
  C. The retained `bell_inequality_derived_note` would still need (c)
  and (d) above to flip to retained.
- Does NOT derive the Born rule `P = |A|^2` itself; that is imported as
  the retained `i3_zero_exact_theorem_note` surface.
- Does NOT prove non-locality (Bell-test loophole questions are
  experimental, not algebraic).

## Honest boundaries

- The classical bound (Part 1) is pure combinatorics on `{-1,+1}^4`,
  16-case verifiable, requires zero physics. Including it here is for
  framework completeness — local-realist models cannot exceed 2.
- The Tsirelson bound (Part 2) requires only: self-adjoint involutions
  with `‖X‖=1`, tensor-product bipartition giving `[Ã_i, B̃_j]=0`,
  and Born expectation `⟨O⟩=⟨ψ|O|ψ⟩`. All three are retained primitives.
- The saturating witness (Part 3) requires only `H = C^2` (Cl(3)
  per-site dim two, retained) and Pauli involutions `σ_z, σ_x` with
  `{σ_z,σ_x}=0` (retained). No framework Hamiltonian, no coupling
  parameter, no continuum prescription.
- The proof has no free parameters, no fitted constants, no observational
  inputs, no literature numerical imports.

## Derivation chain

```
A1 (graph axiom)        \
A2 (Cl(3))               -- retained: cl3_per_site_hilbert_dim_two
                         -- retained: fermion_parity_pauli_tensor_involution
                              (σ_z, σ_x with σ_z^2 = σ_x^2 = I, {σ_z,σ_x}=0)
                              |
                              v
                         Bell witness state |ψ⟩ = (|00⟩+|11⟩)/√2
                              + Pauli involutions A_i, B_j
                              |
                              v
                         Landau identity: S_op^2 = 4I − [A_0,A_1][B_0,B_1]
                              + commutator-norm bound ‖[X,Y]‖ ≤ 2
                              |
                              v
                         Tsirelson |S| ≤ 2√2 (Part 2)
                              + saturating witness gives S = 2√2 (Part 3)

Independent classical line:
{-1,+1}^4 local realism + linearity-of-expectation
                              |
                              v
                         Classical |S| ≤ 2 (Part 1)
                              + product-state saturation gives |S|=2 (Part 4)
```

## Manuscript-safe wording

> The framework derives a structural CHSH bound theorem at class-A
> algebra precision: any local hidden-variable model satisfies
> |S| ≤ 2, and any tensor-product Hilbert quantum model with
> self-adjoint involution observables satisfies |S| ≤ 2√2 (Tsirelson's
> bound) via Landau's exact operator identity. The bound 2√2 is
> saturated by a Bell witness state in Cl(3) per-site Hilbert dim two
> with anticommuting Pauli involutions, both of which are retained
> primitives.
>
> Whether the framework's specific Hamiltonian dynamically saturates
> 2√2 at derived (non-tuned) couplings remains a separate open
> question; the retained `bell_inequality_derived_note` provides
> numerical evidence at selected couplings on small lattices, but
> physical normalization of G and continuum scaling are not yet
> derived.

## Audit lane positioning

- **Suggested status:** `audited_clean` → `retained`.
- **Class:** A (pure algebra over retained primitives).
- **Criticality:** medium (foundational, supports any QM/Bell discussion).
- **Independence:** runner is exact-symbolic (sympy `Rational` and
  `sqrt`) plus exact numpy verification with float ≤ 1e-12 tolerance.

## Why this is a clean source-only deliverable

Per the review-loop-source-only policy: this is exactly **one source
theorem note** + **one paired runner** + **one cache**. No output
packets, no lane promotions, no synthesis. The note has no hidden
dependencies on framework Hamiltonian details; all inputs are named
retained primitives. The runner is self-contained.
