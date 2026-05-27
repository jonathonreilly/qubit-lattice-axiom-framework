# Cubic Bravais Forcing from Cl(3) — Narrow Theorem

**Date:** 2026-05-27
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane.
**Primary runner:** [`scripts/cubic_bravais_forcing_from_cl3_runner.py`](../scripts/cubic_bravais_forcing_from_cl3_runner.py)

## Claim

Let the per-site algebra be `Cl(3,0)` (axiom A1 of the framework, as
restated in
[`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md)). The
algebra carries the canonical 3D-Euclidean signature: it is generated
by three anticommuting self-adjoint generators `γ₁, γ₂, γ₃` with
`γᵢ² = +1` and `γᵢγⱼ + γⱼγᵢ = 0` for `i ≠ j`, on a 3-dim real vector
space `V = span_ℝ(γ₁, γ₂, γ₃) ≅ ℝ³` with the positive-definite
inner product `⟨γᵢ, γⱼ⟩ = ½(γᵢγⱼ + γⱼγᵢ) = δᵢⱼ`. By the universal
property of Clifford algebras, every orthogonal transformation
`R ∈ O(3)` of `V` extends uniquely to an ℝ-algebra automorphism
`φ_R: Cl(3,0) → Cl(3,0)` via `γᵢ ↦ Σⱼ Rᵢⱼ γⱼ`.

Adopt the following two **named premises** (carried explicitly in
`admitted_context_inputs`):

- **(P1) Discrete-translation premise.** The spatial substrate is
  invariant under some discrete rank-3 subgroup `T ⊂ V` of translations
  of the underlying 3D Euclidean space of `Cl(3,0)` (equivalently, the
  site set is a Bravais lattice in `V`).
- **(P2) Generator-axis primitivity premise.** A primitive set of
  generators `{t₁, t₂, t₃}` for `T` is parallel to a permutation of
  the `Cl(3,0)` generator basis `{γ₁, γ₂, γ₃}` (i.e., the lattice's
  primitive translations point along the substrate's algebraic
  generator axes).

**Theorem (Cubic Bravais Forcing).** Given A1 and the premises
(P1), (P2):

1. **(C1) O(3)-orientation.** The substrate point-symmetry group is
   `O_h ⊂ O(3)`, the 48-element cubic point group, and it acts on
   `Cl(3,0)` faithfully by algebra automorphisms via the universal
   property; the pseudoscalar `I = γ₁γ₂γ₃` transforms as the
   sign-of-determinant character `φ_R(I) = det(R)·I`.
2. **(C2) Bravais classification (cubic family).** Among the 14
   three-dimensional Bravais lattice types, exactly three carry full
   `O_h` point symmetry: primitive cubic (cP), body-centred cubic
   (cI), and face-centred cubic (cF). All non-cubic Bravais families
   have strictly smaller point groups.
3. **(C3) Primitive-cubic selection.** Of the three cubic Bravais
   types, only the **primitive cubic** lattice cP has a primitive
   generator triple parallel to the cubic principal-axis basis. The
   bcc and fcc primitive generators point along body-diagonals and
   face-diagonals respectively, not along the principal axes.
4. **(C4) Z³-forcing.** Combining (C1)–(C3): under (P2), the
   substrate is `T = a·Z³` for a single scale parameter `a > 0` (the
   lattice spacing). The "cubic Z³" content of the originally
   declared A2 is a theorem on A1 + (P1) + (P2); the only residual
   axiom-level content of A2 is the scale `a` and the discreteness
   premise (P1).

Identities (C1)–(C4) are finite-group, Clifford-algebra, and
classical-crystallography statements. They do **not** assert that A2
is fully eliminated as an axiomatic commitment; (P1) remains as a
named premise carried by `admitted_context_inputs`. The narrowed
content of the theorem is the sharpening "cubic-Z³ from A1 + discrete
translations + generator-axis primitivity," not "Z³ from A1 alone."

## Proof-walk

| Step | Statement | Load-bearing input |
|---|---|---|
| (B1) | `Cl(3,0)` is the Clifford algebra of `(V, ⟨·,·⟩)` where `V = span_ℝ(γ₁, γ₂, γ₃) ≅ ℝ³` with `⟨γᵢ, γⱼ⟩ = δᵢⱼ`. The (3,0) signature names a positive-definite 3-dim real inner-product space. | Definition of Cl(3,0) |
| (B2) | The universal property of Clifford algebras lifts every orthogonal `R ∈ O(3)` of `V` to a unique ℝ-algebra automorphism `φ_R: Cl(3,0) → Cl(3,0)` extending `γᵢ ↦ Σⱼ Rᵢⱼ γⱼ`. The map `R ↦ φ_R` is a faithful group homomorphism `O(3) ↪ Aut_ℝ(Cl(3,0))`. | Universal property of Clifford algebras |
| (B3) | (P1) commits the substrate translation group to a discrete rank-3 Abelian subgroup `T ⊂ V`. By the structure theorem for free Abelian groups, `T = ℤ·v₁ ⊕ ℤ·v₂ ⊕ ℤ·v₃` for some ℝ-linearly independent primitive generators `v₁, v₂, v₃ ∈ V`. | Free-Abelian structure theorem |
| (B4) | The point-symmetry group `P(T) := {R ∈ O(V) : R·T = T}` is a finite subgroup of `O(3)` (since it permutes a discrete cocompact set). The classical 3D crystallographic classification (Bieberbach / Schönflies / International Tables for Crystallography) enumerates the 32 crystallographic point groups; among these `O_h` is the unique maximal one consistent with full cubic symmetry. | Classical 3D crystallographic classification |
| (B5) | The 14 Bravais lattice types are the orbits of the action of `GL(3,ℤ)` on the space of rank-3 lattices. Exactly three Bravais types carry full `O_h` point symmetry: cP (primitive cubic, generators along principal axes), cI (body-centred cubic, primitive generators along body-diagonals from corner to body-centre), cF (face-centred cubic, primitive generators along face-diagonals). All other 11 Bravais types have point groups strictly smaller than `O_h`. | Classical 3D Bravais classification |
| (B6) | (P2) commits the primitive generator triple `{v₁, v₂, v₃}` to be parallel to a permutation of `{γ₁, γ₂, γ₃}`. After ordering by the chosen permutation and absorbing signs (which leave `T` invariant), `vᵢ = aᵢ · γᵢ` for some `aᵢ > 0`. | (P2) |
| (B7) | The point-symmetry constraint `O_h ⊂ P(T)` requires `T` to be invariant under permutations of the `γᵢ`-axes and under sign-flips. Invariance under axis permutation forces `a₁ = a₂ = a₃ =: a`. | `O_h`-symmetry of the generator triple |
| (B8) | (B6) + (B7) ⇒ `T = a · (ℤ·γ₁ ⊕ ℤ·γ₂ ⊕ ℤ·γ₃) = a · Z³`, the primitive cubic lattice with spacing `a`. By (B5) this is exactly the cP Bravais type. | Algebra |

## Why (P2) is the honest narrowing line

(P2) is **necessary**: without it, the three cubic Bravais types (cP,
cI, cF) all satisfy `O_h ⊂ P(T)`, and `O_h`-symmetry alone does not
distinguish them. Concretely:

- **cP:** primitive generators `a · γᵢ`. Point group `O_h`. Primitive
  vectors parallel to `Cl(3,0)` generator axes. **This is Z³.**
- **cI:** primitive generators `(a/2)(±γ₁ ± γ₂ ± γ₃)` with appropriate
  parity; equivalently, `T = aZ³ ∪ (aZ³ + (a/2)(γ₁+γ₂+γ₃))`. Point
  group `O_h`. Primitive vectors along body-diagonals, not principal
  axes.
- **cF:** primitive generators `(a/2)(γᵢ + γⱼ)` for distinct `i, j`.
  Point group `O_h`. Primitive vectors along face-diagonals, not
  principal axes.

(P2) selects cP from {cP, cI, cF}. It is a frame-compatibility
premise: the substrate's algebraic generator basis `{γᵢ}` is
identified with the spatial principal axes of the lattice. This is
the same identification that PR-1974 / `CL3_OH_CUBIC_LIFT_FAITHFUL`
makes implicitly when it labels `γᵢ` as the i-th spatial axis. The
honest narrowing line is that this identification is a named premise,
not a theorem.

## What this collapses, and what remains

**Collapsed from A2 into A1 + (P1) + (P2):**

- The choice of cubic spatial geometry (`O_h` point symmetry) — fully
  derivable from A1 and the universal property; (P2) only fixes the
  frame, not the cubic-vs-other-system question.
- The choice of primitive cubic vs body-/face-centred cubic — fixed
  by (P2) (generator-axis primitivity).

**Residual axiom-level content of A2:**

- (P1) The discreteness of translations. Cl(3,0) is the Clifford
  algebra of the continuous Euclidean ℝ³; discreteness is not algebraic
  data of A1.
- A single scale parameter `a > 0` (lattice spacing). The "M_Pl-pin"
  derivation chain (`PLANCK_TARGET3_NOTE.md` and downstream) is the
  separate lane that ties `a` to a physical scale.

**Honest final minimum:**

| Surface | Pre-this-note | Post-this-note (under audit-clean) |
|---|---|---|
| Framework axioms | `{A1, A2}` | `{A1}` |
| Named premises in `admitted_context_inputs` | none beyond gates | `(P1)` discrete translations, `(P2)` generator-axis primitivity |
| Physical scale admission | M_Pl | M_Pl |

`(P2)` is a frame-identification convention rather than a substantive
ontological commitment; once one declares that the Cl(3,0) generators
`γᵢ` are the spatial axes (which is the standard meaning of the
positive-definite signature in (3,0)), (P2) is automatic. The
genuinely irreducible non-A1 content is (P1) — the discrete-translation
premise.

## Exact arithmetic check (illustrative)

Take `a = 1` (units of lattice spacing) and the canonical realization
`γᵢ = σᵢ` (Pauli matrices). Then under (P1) + (P2):

- Primitive generators: `v₁ = γ₁ = σ₁`, `v₂ = γ₂ = σ₂`, `v₃ = γ₃ = σ₃`
  in the algebraic basis. Spatially: `v₁ = (1,0,0)`, `v₂ = (0,1,0)`,
  `v₃ = (0,0,1)`.
- `T = ℤ · v₁ ⊕ ℤ · v₂ ⊕ ℤ · v₃ = Z³`.
- Point symmetry of `T`: 48 signed permutation matrices = `O_h`. ✓
- Pseudoscalar `I = γ₁γ₂γ₃` transforms as `φ_R(I) = det(R)·I`
  under `O_h` action (verified element-wise; same as the sibling
  CL3_OH lift). ✓

For comparison, bcc with the same axes-and-scale parameter `a`:

- Primitive bcc generators: `b₁ = (a/2)(γ₁+γ₂-γ₃)`, etc.
- These are **not** parallel to any single `γᵢ`, so (P2) is violated.
- The bcc lattice has `O_h` point symmetry but is excluded by (P2).

The runner verifies these checks symbolically with `sympy` and exact
integer/rational arithmetic.

## Dependencies

- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md)
  for the current A1 / A2 axiom framing being sharpened by this note.
- [`AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md)
  for the retained per-site `Cl(3)` primitive that supplies the
  underlying algebra and its 3D-Euclidean signature.
- [`CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md`](CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md)
  for the retained `Cl(3,0) ⊗ ℂ ≅ M₂(ℂ) ⊕ M₂(ℂ)` structural identity
  used in the Pauli realization of the runner.
- [`CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md`](CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md)
  for the retained_bounded Pauli-irrep uniqueness used to fix the
  concrete `γᵢ = σᵢ` realization.

The Clifford-algebra automorphism lift `O(3) ↪ Aut_ℝ(Cl(3,0))` used
in (B1)–(B2) is the universal property of Clifford algebras (standard
algebra). The 14 Bravais types and 32 crystallographic point groups
used in (B4)–(B5) are classical 3D crystallography. The structure
theorem for free Abelian groups used in (B3) is standard algebra. No
new admission is introduced. PR-1974
(`CL3_OH_CUBIC_LIFT_FAITHFUL_NARROW_THEOREM_NOTE_2026-05-26`) is a
sibling note that establishes the same `O(3) ↪ Aut_ℝ(Cl(3,0))` lift
with explicit pseudoscalar-character verification; if/when that note
retains, the proof of (B2) can be cited directly to it rather than
re-derived from the universal property.

## Historical provenance (cited prior art, NOT load-bearing imports)

The Bravais-lattice classification and crystallographic point groups
are classical content:

- **Hamermesh, M.** (1962). *Group Theory and Its Application to
  Physical Problems*. Addison-Wesley. Chapters on crystallographic
  groups and lattice symmetries.
- **Tinkham, M.** (1964). *Group Theory and Quantum Mechanics*.
  McGraw-Hill. Ch. 4 on crystallographic point groups.
- **Cornwell, J. F.** (1997). *Group Theory in Physics: An
  Introduction*. Academic Press. Ch. 7 on the cubic point group
  `O_h` and the Bravais lattice classification.
- **International Tables for Crystallography, Vol. A** (2016). Wiley.
  Definitive enumeration of the 14 Bravais lattices and 32
  crystallographic point groups in 3D.
- **Lounesto, P.** (2001). *Clifford Algebras and Spinors*, 2nd ed.,
  Cambridge University Press. Ch. 16 on the lift `O(n) → Pin(n)
  ⊂ Cl(n)` via the universal property.

**These references are cited as historical prior art / provenance
only.** This note imports no theorem, normalization, or numerical
value from the cited works. The derivation in (B1)–(B8) proceeds
entirely on the framework's retained `Cl(3)` primitive, the named
premises (P1) and (P2), and standard finite-group / linear-algebra /
free-Abelian-structure facts. The Bravais classification is used as
classical reference content (enumeration of the 14 types), not as an
imported load-bearing theorem.

## Boundaries

This bridge does **not** close:

- (P1) the discrete-translation premise (the substrate is invariant
  under a discrete rank-3 translation subgroup of ℝ³). This remains
  a named premise carried in `admitted_context_inputs`. Closing (P1)
  would require a separate UV-regulator / cutoff-from-Planck-scale
  derivation; the present note does not attempt this.
- The pinning of the lattice spacing `a` to a physical scale; that is
  the separate Planck-scale chain.
- Lorentzian or relativistic spatial geometry; (3,0) signature is
  Euclidean, and the temporal / kinematic lift is a separate concern
  (`DT1_TIME_DIMENSION_PROOF_WALK_LATTICE_INDEPENDENCE_BOUNDED_NOTE_2026-05-08.md`
  and adjacent notes).
- Removal of (P2) as a frame-identification premise; while (P2) is
  conventionally automatic once one identifies the algebraic generators
  with spatial axes, the present note carries it as a named premise
  for honesty.

What this **does** close: that the "cubic" content of A2 is a corollary
of A1 + (P1) + (P2). The remaining axiomatic content of A2 reduces to
(P1) (discrete translations) plus a single scale parameter. The
framework's axiom surface contracts from `{A1, A2}` to
`{A1, (P1)}` modulo the physical-scale admission.

## Audit-lane status field hints

For the audit-lane row generated from this note:

- `claim_type`: `bounded_theorem`
- `claim_scope`: cubic-Bravais forcing of the spatial substrate, given
  retained A1, the discrete-translation premise (P1), and the
  generator-axis primitivity premise (P2); does not close (P1).
- `admitted_context_inputs`: `(P1)` discrete-translation premise,
  `(P2)` generator-axis primitivity premise.
- `chain_closes`: contingent on retention of the cited
  `Cl(3)`-uniqueness, `Cl(3)`-complexification-split, and Pauli-irrep
  uniqueness authorities, all of which are retained or
  retained_bounded.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/cubic_bravais_forcing_from_cl3_runner.py
```

Expected:

```text
TOTAL: PASS=22 FAIL=0
VERDICT: Cubic Bravais forcing holds; (P1)+(P2) reduce A2 to a discrete-translation
premise; Z³ is forced from A1 + (P1) + (P2).
```
