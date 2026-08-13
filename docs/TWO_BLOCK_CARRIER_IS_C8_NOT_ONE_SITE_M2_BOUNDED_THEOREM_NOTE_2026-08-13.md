---
claim_id: two_block_carrier_is_c8_not_one_site_m2_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "The May 2 two-block ranks (6,2) reconstruct an 8x8 self-adjoint operator Y_0 = Pi_+ - 3 Pi_- on C^8 with spectrum {+1 x6, -3 x2}. That eigenvalue multiset has length 8, so the smallest Hilbert-space dimension that can carry it is 8. No spectrum-preserving *-embedding of (C^8, Y_0) into the one-site pair (C^2, M_2(C)) exists, because 8 > 2. The current Qubit sentence presents the one-site possibility domain as M_2(C); the current Lattice sentence presents sites of Z^3 with no site privileged. Neither sentence names a C^8 taste cube, a 3-factor tensor, or ranks (6,2). The 8-dimensional carrier is therefore a displayed missing input relative to one-site Qubit. This note does not identify Y_0 with U(1)_Y, does not select (6,2) over (4,4), does not derive alpha = 1/3, and does not claim that no later 8-carrier compiler exists."
upstream_dependencies:
  - minimal_axioms
  - lh_doublet_traceless_abelian_eigenvalue_ratio_narrow_theorem_note_2026-05-02
runner: scripts/two_block_carrier_is_c8_not_one_site_m2_2026_08_13.py
---

# The Two-Block Carrier Is C^8, Not One-Site M_2(C)

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact finite-dimensional comparison of the reconstructed two-block
operator `Y_0` on `C^8` with the one-site Qubit algebra `M_2(C)`.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_block_carrier_is_c8_not_one_site_m2_2026_08_13.py`](../scripts/two_block_carrier_is_c8_not_one_site_m2_2026_08_13.py)

## Result Up Front

The one-site Qubit domain is the pair `(C^2, M_2(C))`. Any self-adjoint
element of that algebra has at most two eigenvalues, counting multiplicity.

The May 2 two-block ranks `(6,2)` live on an eight-dimensional space. This
note reconstructs, and does not import Standard Model names for, the
complementary projectors

```text
Pi_+ = diag(I_6, 0_2),
Pi_- = diag(0_6, I_2),
```

and the ratio representative

```text
Y_0 := Pi_+ − 3 Pi_-.
```

The spectrum of `Y_0` is `{+1 × 6, −3 × 2}`. The trace is `6 − 6 = 0`. The
ratio `β = −3α` is used only as the cited May 2 identity
`6α + 2β = 0`. The scale choice here is the representative `α = 1`, not a
derivation of `α = 1/3`.

Five bounded statements follow.

1. `Y_0` is self-adjoint on `C^8` and has eight eigenvalues with
   multiplicity. The smallest Hilbert-space dimension that can carry that
   multiset is 8.
2. No `*`-embedding of `(C^8, Y_0)` into `(C^2, M_2(C))` can preserve the
   spectrum, because `8 > 2`. Therefore `Y_0` is not an element of the
   one-site algebra.
3. The current Qubit sentence and the current Lattice sentence do not name a
   `C^8` taste cube, a 3-factor tensor, or ranks `(6,2)`.
4. Any operator with spectrum `{1^6, (−3)^2}` requires an 8-dimensional
   carrier. That carrier is extra relative to one-site Qubit. The carrier is
   displayed; this note does not adopt a taste-cube axiom.
5. This note does not identify `Y_0` with `U(1)_Y`, does not select the
   `(6,2)` split over `(4,4)`, and does not claim that no later 8-carrier
   compiler exists.

The predicates "`Y_0` acts on `C^2`" and "one-site `M_2` contains `Y_0`"
are therefore false.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The dimension comparison is exact integer-linear algebra on a reconstructed 8x8 operator and the one-site M_2(C) presentation. The (6,2) ranks and the ratio beta = -3 alpha are cited May 2 inputs, not axiom consequences. No physical identification, split selection, or later compiler existence claim is made."
trace_class: missing_input_display
artifact_role: theorem
hypothetical_axiom_status: "display only; no canonical axiom edit and no taste-cube adoption"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

One-site Qubit data, quoted from the current axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

The underlying one-site Hilbert space is therefore `H_2 = C^2`, and the
one-site operator algebra is `End(H_2) = M_2(C)`. Write `site_dim()` for
that Hilbert-space dimension. The unique positive integer `n` with
`n^2 = dim_C M_2(C) = 4` is `n = 2`, so `site_dim() = 2`.

Lattice data, quoted from the same memo:

> Physical sites are the points of the cubic lattice `Z^3`, with
> nearest-neighbor adjacency, standard translations, and proper cubic
> rotations about each site.
>
> No site is privileged.

May 2 two-block ranks, cited from
[`LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md`](LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md)
and not re-derived here: a traceless two-block operator with multiplicities
`6` and `2` satisfies

```text
6 · α + 2 · β = 0
⇒ β = −3 α.
```

This note uses that identity only as a cited May 2 fact. It reconstructs one
ratio representative on `H_8 = C^8` by the block projectors above. It does
not import Standard Model names for the two blocks.

Let `I_k` and `0_k` be the `k × k` identity and zero matrices over the
rationals. Define

```text
Pi_+ := diag(I_6, 0_2) ∈ M_8(Q),
Pi_- := diag(0_6, I_2) ∈ M_8(Q),
Y_0  := Pi_+ − 3 Pi_-.
```

These are explicit `8 × 8` matrices. All arithmetic below is exact over
`Q` (equivalently Python `Fraction`).

Write `spectrum_multiset(T)` for the eigenvalue multiset of a self-adjoint
operator `T`, counted with algebraic multiplicity and ordered
non-increasingly.

## Theorem 1 — Eight eigenvalues on C^8

`Y_0` is self-adjoint on `C^8`. Its spectrum is `{+1 × 6, −3 × 2}`. The
smallest Hilbert-space dimension that can carry that multiset is 8.

**Proof.** Each of `Pi_+` and `Pi_-` is real symmetric, hence self-adjoint,
and `Y_0` is an integer-linear combination of them, hence self-adjoint.
Direct matrix multiplication gives

```text
Pi_+^2 = Pi_+,   Pi_-^2 = Pi_-,   Pi_+ Pi_- = 0 = Pi_- Pi_+,
Pi_+ + Pi_- = I_8.
```

In the same block basis, `Y_0` is diagonal with six entries `+1` and two
entries `−3`. Therefore

```text
spectrum_multiset(Y_0) = (1, 1, 1, 1, 1, 1, −3, −3).
```

The length of that multiset is 8. For any self-adjoint operator the length
of the eigenvalue multiset equals the dimension of the Hilbert space on
which it acts. A space that carries eight eigenvalues, counted with
multiplicity, therefore has dimension at least 8. The constructed space has
dimension 8, so 8 is the smallest such dimension.

The trace is the sum of the multiset:

```text
Tr(Y_0) = 6 · 1 + 2 · (−3) = 0,
```

which is the same identity as `6α + 2β = 0` at the cited May 2
representative `α = 1`, `β = −3`.

## Theorem 2 — No spectrum-preserving embedding into one-site M_2(C)

There is no `*`-embedding of the pair `(C^8, Y_0)` into the one-site pair
`(C^2, M_2(C))` that preserves `spectrum_multiset(Y_0)`. In particular
`Y_0` is not an element of the one-site algebra.

**Proof.** A self-adjoint element of `M_2(C)` acts on a Hilbert space of
dimension `site_dim() = 2`, so it has at most two eigenvalues counting
multiplicity. A spectrum-preserving `*`-embedding would send `Y_0` to such
an element, forcing

```text
len(spectrum_multiset(Y_0)) ≤ site_dim().
```

The left side is 8 and the right side is 2. The inequality `8 ≤ 2` is
false. Equivalently, there is no injective linear map `C^8 → C^2`.

Therefore the predicate "`Y_0` acts on `C^2`" fails, and the predicate
"one-site `M_2` contains `Y_0`" fails.

## Theorem 3 — Current axiom sentences do not name the carrier

Quote Qubit: the full one-site possibility domain has algebraic
presentation `M_2(C)`. Quote Lattice: sites of `Z^3`, no site privileged.

Neither sentence names a `C^8` taste cube, a 3-factor tensor, or ranks
`(6,2)`.

**Proof.** The quoted sentences are the current axiom-memo wording. Direct
inspection of that wording shows that the phrases "`C^8` taste cube",
"3-factor tensor", and "ranks `(6,2)`" do not occur there. The one-site
algebra named by Qubit is `M_2(C)`, whose carrier dimension is
`site_dim() = 2`. Lattice names the site set `Z^3` and states that no site
is privileged; it does not add an internal eight-dimensional fiber.

## Theorem 4 — Missing input, displayed not adopted

Any operator with spectrum `{1^6, (−3)^2}` requires an 8-dimensional
carrier. That carrier is extra relative to one-site Qubit. This note
displays the carrier. It does not adopt a taste-cube axiom.

**Proof.** Theorem 1 supplies the dimension count. Theorem 2 supplies the
comparison with one-site `M_2(C)`. Theorem 3 supplies that the current
axiom sentences do not already name the eight-dimensional object. The
conjunction is a missing-input statement: the reconstructed operator is
not an output of the one-site Qubit presentation. Displaying
`(C^8, Y_0)` records the extra carrier. Recording a missing input is not
an axiom edit and is not an adoption of a taste-cube axiom.

## Theorem 5 — Explicit non-claims

This note does not identify `Y_0` with `U(1)_Y`. It does not select the
`(6,2)` split over `(4,4)`. It does not claim that no later 8-carrier
compiler exists. It does not derive `α = 1/3`. It does not force `r = 1/2`.

The `(6,2)` ranks enter only as the cited May 2 two-block data. A different
two-block split of an eight-dimensional space, such as `(4,4)`, would give
a different traceless ratio and is not compared or eliminated here. The
representative `Y_0 = Pi_+ − 3 Pi_-` fixes the May 2 ratio at scale
`α = 1`; that is a reconstruction choice, not a derivation of the
normalization `α = 1/3`. A later construction that compiles an
eight-dimensional carrier from already retained data would be a different
claim and is not ruled out by `8 > 2`.

## What This Note Does Not Close

- Identification of `Y_0` with Standard Model hypercharge `U(1)_Y`.
- Selection of ranks `(6,2)` over `(4,4)` or any other split of 8.
- A derivation of the normalization `α = 1/3`.
- Any claim about `r = 1/2`.
- Existence or non-existence of a later 8-carrier compiler.
- Adoption of a `C^8` taste cube, a 3-factor tensor, or any new axiom.
- Anomaly cancellation, charge formulae, or any Standard Model renaming.

## Dependencies

Load-bearing one-hop sources:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  the current Qubit presentation `M_2(C)` and the current Lattice wording
  that sites are the points of `Z^3` with no site privileged.
- [`LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md`](LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md)
  supplies the two-block ranks `(6,2)` and the cited identity
  `6α + 2β = 0 ⇒ β = −3α`. That parent already places Standard Model
  hypercharge identification, the normalization `α = 1/3`, and the charge
  formula outside its load-bearing chain.

No other scientific source is load-bearing. Unmerged pull requests are not
cited.

## No-Go Discipline Gate

The negative fragment is only the spectrum-preserving embedding obstruction
of Theorem 2 and the two failed predicates of the identity gates.

| Item | Statement |
|---|---|
| Exact negative | no spectrum-preserving `*`-embedding of `(C^8, Y_0)` into `(C^2, M_2(C))`; `Y_0` is not an element of one-site `M_2(C)` |
| Mechanism | eigenvalue-multiset length 8 exceeds `site_dim() = 2` |
| Live remainder | a later 8-carrier compiler, a different split of 8, and any physical identification of `Y_0` remain open |
| Not claimed | axiom necessity, taste-cube adoption, uniqueness of ranks `(6,2)`, non-existence of every 8-dimensional construction |

The obstruction is a finite dimension count on named matrices. It is not a
global no-go against every future eight-dimensional object.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/two_block_carrier_is_c8_not_one_site_m2_2026_08_13.py
```

The runner reconstructs `Pi_+`, `Pi_-`, and `Y_0` over `Fraction`, computes
`spectrum_multiset(Y_0)` from the matrix, computes `site_dim()` from
`dim M_2(C) = 4`, and evaluates the two identity predicates by calling
those two functions. Both predicates must fail. The runner binds
`AUDIT_INPUT_PATHS` to this note, the May 2 parent, and the axiom memo.
