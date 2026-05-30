# Cl(3) Faithful Lift of the Cubic Point Group O_h — Narrow Theorem

**Date:** 2026-05-26
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane.
**Primary runner:** [`scripts/cl3_oh_cubic_lift_faithful_runner.py`](../scripts/cl3_oh_cubic_lift_faithful_runner.py)

## Audit context

This note is an algebraic input for a proposed strong-CP / θ retirement
stack. The structural mechanism under review is: the cubic point group
`O_h` of the `Z^3` spatial substrate acts on the `Cl(3)`
pseudoscalar `I = γ₁γ₂γ₃` as the sign-of-determinant character. If
later notes independently establish the relevant O_h-invariant action
class and show that a candidate action slot transforms only by this
character, that slot is forced to vanish.

That mechanism is contingent on a decision-grade lemma: **does O_h lift
faithfully to Cl(3) as algebra automorphisms, and does the lift act on
the pseudoscalar as the determinant character?**

This narrow theorem closes that decision-grade lemma.

## Claim

Let `Cl(3) = Cl(3,0; ℝ)` be the real Clifford algebra of dimension 8
with generators `γ₁, γ₂, γ₃` satisfying `γᵢ² = +1` and
`γᵢγⱼ + γⱼγᵢ = 0` for `i ≠ j`. Let `O_h ⊂ O(3)` be the full cubic
point group, realized as the 48 signed permutation matrices on the
standard basis of `ℝ³`.

**Theorem (Cl(3) faithful lift of O_h).**

1. **(T1) Faithful lift.** For every `R ∈ O_h`, the linear map on
   generators
   ```text
   γᵢ ↦ Σⱼ Rᵢⱼ γⱼ                                                (V)
   ```
   extends uniquely to an ℝ-algebra automorphism `φ_R : Cl(3) → Cl(3)`.
2. **(T2) Pseudoscalar character.** Under this lift,
   ```text
   φ_R(I) = det(R) · I,        where I = γ₁γ₂γ₃.                  (P)
   ```
3. **(T3) Z₂ grading.** The O_h-action splits the pseudoscalar
   subspace `ℝ·I ⊂ Cl(3)` into the **sgn(det)** representation: the
   24 proper rotations (`O ⊂ O_h`, `det = +1`) fix `I`; the 24
   improper rotations (`O_h ∖ O`, `det = -1`) flip `I → −I`.
4. **(T4) Pseudoscalar-odd coefficient slots are O_h-odd.** The
   O_h-average of the pure pseudoscalar line `ℝ·I` is zero. Therefore,
   once a later action-class note independently proves O_h-invariance
   and identifies a candidate slot as transforming only by the
   determinant character, the coefficient of that slot must vanish.

Identities (T1)–(T4) are pure finite-group / Clifford-algebra
statements internal to the framework's one-qubit operator algebra on
the `Z^3` spatial substrate. They do **not** assert strong-CP closure
or action-class O_h-invariance; they supply the structural ingredient
that subsequent bridge notes would have to compose
with a separately reviewed and audited action-class result.

## Proof-walk

| Step | Statement | Load-bearing input |
|---|---|---|
| (B1) | The Clifford relations `γᵢγⱼ + γⱼγᵢ = 2 δᵢⱼ` are preserved by `(V)` for any orthogonal `R`: `(Σₖ Rᵢₖγₖ)(Σₗ Rⱼₗγₗ) + (Σₗ Rⱼₗγₗ)(Σₖ Rᵢₖγₖ) = Σₖₗ RᵢₖRⱼₗ (γₖγₗ + γₗγₖ) = 2 Σₖ RᵢₖRⱼₖ = 2 δᵢⱼ` (last equality is `RR^T = I` for orthogonal `R`). | Orthogonality of `R ∈ O_h ⊂ O(3)` |
| (B2) | By the universal property of Clifford algebras, the linear map `(V)` extends uniquely to a ℝ-algebra homomorphism `Cl(3) → Cl(3)`. Injectivity follows from invertibility of `R`; surjectivity from finite dimension. Hence `φ_R` is an algebra automorphism. | Universal property of `Cl(3)` |
| (B3) | For pseudoscalar `I = γ₁γ₂γ₃`, expand: `φ_R(I) = φ_R(γ₁)φ_R(γ₂)φ_R(γ₃) = Σₐ,ᵦ,c R₁ₐR₂ᵦR₃c γₐγᵦγc`. For non-coincident `(a,b,c)`, `γₐγᵦγc = ε(abc) I` (signed by permutation parity); for coincident indices, the product reduces to lower grade. | Clifford multiplication rules |
| (B4) | Coincident-index contributions cancel pairwise (e.g., `γ₁γ₂γ₁ = -γ₂` and `γ₂γ₁γ₁ = +γ₂` cancel after summing with antisymmetric coefficient pairings under orthogonality). | Antisymmetry + orthogonality computation |
| (B5) | The surviving sum is `(Σ ε(abc) R₁ₐ R₂ᵦ R₃c) · I = det(R) · I` by the Leibniz formula. | Leibniz formula for `det` |
| (B6) | Combining (B1)–(B5): `(V)` extends to an algebra automorphism `φ_R` of `Cl(3)` for every orthogonal `R`, and `φ_R(I) = det(R) · I`. | Algebra |
| (B7) | For O_h ⊂ O(3): 24 proper rotations have `det = +1` (so `I` is fixed); 24 improper have `det = -1` (so `I → −I`). This is the Z₂ sgn-rep on `ℝ·I`. | Standard O_h structure |
| (B8) | The pure pseudoscalar line transforms by the sign character. Therefore an O_h-invariant expression cannot have a nonzero coefficient in a slot already proved to transform only by that character. This is a representation-theoretic consequence, not a proof that every CP-odd lattice discretization belongs to such a slot. | Group representation theory |

## Exact arithmetic check (illustrative)

For `R = ` inversion `= diag(-1, -1, -1)`:
- `φ_R(γᵢ) = -γᵢ`
- `φ_R(I) = (-γ₁)(-γ₂)(-γ₃) = -γ₁γ₂γ₃ = -I = det(R) · I` ✓

For `R = ` 90° rotation about z-axis `= [[0,-1,0],[1,0,0],[0,0,1]]`:
- `φ_R(γ₁) = γ₂`, `φ_R(γ₂) = -γ₁`, `φ_R(γ₃) = γ₃`
- `φ_R(I) = γ₂(-γ₁)γ₃ = -γ₂γ₁γ₃ = γ₁γ₂γ₃ = +I = det(R) · I` ✓

For `R = ` reflection across `xy`-plane `= diag(1, 1, -1)`:
- `φ_R(γ₁) = γ₁`, `φ_R(γ₂) = γ₂`, `φ_R(γ₃) = -γ₃`
- `φ_R(I) = γ₁γ₂(-γ₃) = -I = det(R) · I` ✓

The runner verifies all 48 elements of O_h.

## Implication for strong-CP / θ retirement (preview)

The proposed downstream target theorem reads, in slogan form:

> *Cl(3)/Z^3-Cubic Pinning of θ: O_h-invariance of the framework's
> action class + the pseudoscalar sgn-character (T2)-(T4) of this note
> + the `Z^3` spatial-substrate O_h symmetry forces every CP-odd action slot —
> single-plaquette, clover, multi-plaquette, or extended-trace — to
> vanish identically as an O_h-invariant action class member.*

This preview is not a theorem of this note. This note supplies **only
T1-T4**, the substrate-algebraic determinant-character input. The
remaining work must:

- Show that the Wilson + staggered + scalar-mass action
  class IS O_h-invariant (action-class side, not substrate-algebraic
  side).
- Compose with the Aharony-Razamat-Tachikawa 2026-03
  discrete-θ-projection framework (arXiv:2603.05195) on the natural
  Z₃ body-diagonal subgroup of O_h, gauging the (−1)-form θ-shift
  symmetry.
- Address the clover-`F̃F` counter-attack: show that the O_h-action on
  the pseudoscalar also kills extended-trace CP-odd discretizations,
  not just the single-plaquette one.
- Bridge to continuum θ_QCD; this note does not attempt that bridge.

This narrow theorem closes the **first** of these — the decision-grade
substrate-algebraic input for that proposed stack.

## Dependencies

- [`AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md)
  — supplies the retained Cl(3) per-site algebra primitive on which the
  cubic action operates.
- [`CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md`](CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md)
  — supplies retained `Cl(3) ≅ M₂(ℂ)` structural identification used
  for the concrete Pauli realization in the runner.

These are the only load-bearing dependencies. The cubic group `O_h` and
its 48-element structure are standard finite-group content; the
universal property of Clifford algebras is standard algebra; no new
admission introduced.

## Historical provenance (cited prior art, not load-bearing imports)

The Clifford-algebra action of the orthogonal group is classical:

- **Lounesto, P.** (2001). *Clifford Algebras and Spinors*, 2nd ed.,
  Cambridge University Press. Ch. 16 covers the natural lifting of
  `O(n)` to `Pin(n) ⊂ Cl(n)`.
- **Doran, C.; Lasenby, A.** (2003). *Geometric Algebra for
  Physicists*. Cambridge University Press. Chapters on Cl(3) and
  the cubic point group.
- **Cornwell, J. F.** (1997). *Group Theory in Physics: An
  Introduction*. Academic Press. Ch. 7 on the cubic point group
  O_h and its representations.

**These references are cited as historical prior art / provenance
only.** This bridge does not import any theorem, normalization, or
numerical value from the cited works. The derivation in (B1)-(B8)
proceeds entirely on the framework's retained Cl(3) primitive and
finite-group structure of O_h. Specialization to Cl(3) on the framework's
`Z^3` spatial substrate is the framework's own derivation; the cited literature
provides general-Pin-group context.

## Boundaries

This bridge does **not** close:

- The strong-CP problem (additional bridge steps still required);
- Lattice action-class O_h-invariance (Step 2 target);
- Multi-plaquette or clover CP-odd term exclusion (Step 4 target);
- Lattice-to-continuum θ bridge (Step 5 target);
- Any retired status of θ from the Tier-A admission registry.

What this **does** close: the substrate-algebraic lemma that O_h acts
on Cl(3) as algebra automorphisms with pseudoscalar transforming as
det character. This is the decision-grade input that gates Track A
continuation.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/cl3_oh_cubic_lift_faithful_runner.py
```

Expected:

```text
TOTAL: PASS=18 FAIL=0
VERDICT: Cl(3) faithful lift of O_h holds; pseudoscalar transforms as
det character; all 48 elements verified.
```
