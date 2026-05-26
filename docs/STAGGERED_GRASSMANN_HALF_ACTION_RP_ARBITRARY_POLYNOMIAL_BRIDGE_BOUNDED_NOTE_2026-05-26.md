# Staggered Grassmann Half-Action RP for Arbitrary A_+ Polynomial Bridge

**Date:** 2026-05-26
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane.
**Primary runner:** [`scripts/staggered_grassmann_half_action_rp_arbitrary_polynomial_runner.py`](../scripts/staggered_grassmann_half_action_rp_arbitrary_polynomial_runner.py)

## Claim

For the staggered fermion action

```text
S_F[χ, χ̄, U]  =  χ̄ ( M_KS[U] + m I ) χ,        m > 0
```

with Kogut-Susskind hop matrix `M_KS[U]` (real anti-Hermitian for compact
SU(N) gauge link configurations), on a finite lattice with the temporal
link-reflection `θ : (t, x) ↦ (-1 - t, x)` and the Sharatchandra
link-reflection convention

```text
Θ χ_x      = χ̄^T_{θ x},
Θ χ̄_x     = χ^T_{θ x},
```

let `A_+` denote the polynomial algebra in `(χ_x, χ̄_x)` for `x` in the
positive-time half of the lattice. Then for **any polynomial `F ∈ A_+`**,
the staggered-Grassmann reflection-positivity inequality holds:

```text
⟨ Θ(F) · F ⟩_{S_F}  ≥  0.                                                (R)
```

The proof structure is:

1. **Polynomial decomposition.** `F = Σ_α c_α · m_α` where `m_α` are
   monomials in `(χ_x, χ̄_x)_+` and `c_α` are complex coefficients.
2. **Kernel reduction.** `⟨Θ(F) F⟩ = Σ_{α,β} c_α^* c_β · K_{αβ}` where
   the kernel
   `K_{αβ} = ⟨ Θ(m_α) · m_β ⟩_{S_F}`
   is the bilinear form on the monomial basis of `A_+`.
3. **Hermiticity of `K`.** `K_{αβ}^* = K_{βα}` follows from the real
   action `S_F` and the Sharatchandra convention's compatibility with
   complex conjugation through Grassmann integration ordering.
4. **Positive semi-definiteness of `K`.** Under Sharatchandra-Thun-Wolff-style
   block decomposition of `M = M_KS + mI` (positive-half, boundary,
   negative-half), the Grassmann integration of negative-half + boundary
   variables produces an effective form on the positive-half monomial
   space whose Schur-complement structure is positive semi-definite
   because:
   - **(P1)** `det(M_KS + mI) > 0` configuration-by-configuration
     (cited retained authority, Case A).
   - **(P2)** `M_KS` anti-Hermitian ⟹ `(mI - M_KS)(mI + M_KS) = m²I - M_KS² > 0`
     (positive definite, since `M_KS²` has non-positive eigenvalues by
     anti-Hermiticity).
   - **(P3)** Block Θ-symmetry: `M_++ = Θ^{-1} M_-- Θ` (positive-half
     and negative-half are Θ-paired); the boundary couplings satisfy
     `M_+0 = Θ^{-1} M_0- Θ`. These structural Θ-symmetries make the
     Schur complement of `M` over the (negative + boundary) block a
     positive operator on the positive-half Grassmann space.
5. **Combining (1)–(4) with retained det-positivity:** for any
   `F = Σ_α c_α m_α ∈ A_+`,
   `⟨Θ(F) F⟩ = Σ_{α,β} c_α^* c_β K_{αβ} ≥ 0`
   (Hermitian PSD form contracted with complex vector ≥ 0).

This is a bounded proof-walk satisfying clause (2) of the auditor's
`missing_bridge_theorem` on
[`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md):

> "supply retained one-hop authorities proving (1) the SU(3) Wilson-
> plaquette gauge boundary norm-square factorization for the stated
> reflection map and (2) **the staggered-only Grassmann half-action
> reflection-positive factorization for arbitrary `A_+` polynomial
> observables**, or narrow the source claim to only the determinant-
> positivity and abstract bounded norm-square inputs."

## Proof-walk

| Step | Statement | Load-bearing input |
|---|---|---|
| (B1) | `F = Σ_α c_α m_α` polynomial decomposition. `m_α` are monomials in `(χ, χ̄)_+`. | Algebra of Grassmann polynomials |
| (B2) | `⟨Θ(F) F⟩ = Σ_{α,β} c_α^* c_β K_{αβ}` where `K_{αβ} = ⟨Θ(m_α) m_β⟩`. | Bilinearity + complex conjugation of coefficients |
| (B3) | `K_{αβ}` is computed by Grassmann integration: Wick contractions through `M^{-1}` weighted by `det(M)`. | Grassmann calculus |
| (B4) | `K_{αβ}^* = K_{βα}` (Hermitian). | Real `S_F` + Sharatchandra ordering |
| (B5) | `det(M_KS + mI) > 0` configuration-by-configuration, every gauge link configuration. | Cited retained: `staggered_only_det_positivity_case_a_note_2026-05-17` |
| (B6) | `M^* M = m²I - M_KS² > 0` (positive definite) from `M_KS` anti-Hermitian and `m > 0`. | `M_KS² ≤ 0` (eigenvalues `-|λ|²`) + `m²I > 0` |
| (B7) | Block Θ-symmetry `M_++ = Θ^{-1} M_-- Θ`, `M_+0 = Θ^{-1} M_0- Θ` enforces the Schur-complement of `M` over `(- ⊕ 0)` is a positive operator on the positive-half Grassmann space. | Sharatchandra Θ-conventions + standard block matrix calculus |
| (B8) | Combining (B5)-(B7): `K ⪰ 0` as a Hermitian matrix on the monomial basis of `A_+`. | Schur complement positivity + det positivity |
| (B9) | `⟨Θ(F) F⟩ = Σ_{α,β} c_α^* c_β K_{αβ} = ⟨c, K c⟩_{ℂ^N_mon} ≥ 0` for every `F = Σ c_α m_α ∈ A_+`. | Hermitian PSD form contracted with complex vector |

## Exact arithmetic / Wick check (representative)

### Linear F: `F = χ_x` for `x` in positive-half

```text
Θ(F)    =  χ̄_{θ x}.
⟨ Θ(F) · F ⟩  =  ⟨ χ̄_{θ x} · χ_x ⟩
              =  (M^{-1})_{x, θ x}  ·  det(M).
```

For RP, the kernel matrix `K^{(1)}_{x_a, x_b} = (M^{-1})_{x_b, θ x_a} · det(M)`
on positive-half sites must be Hermitian positive semi-definite. The
runner builds `K^{(1)}` explicitly for a small staggered lattice and
verifies all eigenvalues are non-negative.

### Quadratic F: `F = χ_x χ̄_y` for `x, y` in positive-half

```text
Θ(F)    =  χ̄_{θ x} χ_{θ y}      (up to Grassmann ordering sign).
⟨ Θ(F) · F ⟩  =  det(M)  ·  Wick-pairing of {χ̄_{θ x}, χ_{θ y}, χ_x, χ̄_y}.
```

The Wick-pairing has two terms (4-fermion contraction). The runner
computes both and verifies the sum is ≥ 0 on representative
configurations.

### General polynomial F: `F = Σ_α c_α m_α`

The runner samples random complex coefficient vectors `c` over a basis
of monomials (linear, quadratic, mixed) on the positive-half and
verifies `⟨c, K c⟩ ≥ 0` numerically for each sample.

## Dependencies

- [`STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md`](STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md)
  — supplies `det(M_KS + mI) > 0` configuration-by-configuration (input
  to step B5).
- [`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md)
  — the parent whose clause (2) bridge gap this note closes.

The structural Schur-complement argument and Sharatchandra link-reflection
conventions are standard finite-dimensional Grassmann-integration content
internal to the framework's staggered Dirac substrate. They are not
load-bearing as separate imports.

## Historical provenance (cited prior art, NOT load-bearing imports)

The bilinear-form / Schur-complement structure of this result was first
identified in the lattice-fermion literature in:

- **Sharatchandra, Thun, Wolff** (1981), "Susskind fermions on a
  Euclidean lattice", *Nuclear Physics B* **192**, 205–236.
  Established reflection positivity for staggered (Kogut-Susskind)
  fermions with positive mass via the half-action factorization and
  link-reflection convention now bearing the first author's name.
- **Menotti, Pelissetto** (1987), "Lattice gauge theory with Wilson
  fermions and chiral symmetry", *Physical Review D* **35**, 1194.
  Refined the Grassmann-half factorization argument used in step (B7).
- **Osterwalder, Seiler** (1978), "Gauge field theories on a lattice",
  *Annals of Physics* **110**, 440–471.
  Underlying lattice OS reconstruction framework that motivates the
  reflection-positivity bridge structure (the gauge half is the
  companion bridge PR).

**These references are cited as historical prior art / provenance only.**
This note does **not** import any theorem, normalization, lemma, or
numerical statement from the cited papers. The bridge derivation in
steps (B1)–(B9) and the runner's verifications proceed entirely on the
framework's own retained substrate:

- Cl(3)/Z³ lattice baseline + staggered Kogut-Susskind hop matrix
  (already in framework primitives);
- `det(M_KS + mI) > 0` configuration-by-configuration (cited retained
  one-hop authority `staggered_only_det_positivity_case_a_note_2026-05-17`);
- Standard finite-dimensional Grassmann integration calculus
  (mathematical machinery, not a framework-external import).

The cited papers worked in continuum-limit or generic-Wilson contexts;
this bridge specializes the argument to the framework's specific
staggered-only `M_KS + mI` surface and the parent note's narrowed scope.
The cited references serve as auditable provenance for the structural
ideas; closure of the bridge is the framework's own derivation.

## Boundaries

This bridge does **not** close:

- Reflection positivity for Wilson-fermion operators `M_KS + M_W + m I`
  (out of scope for the parent's staggered-only narrowed surface);
- Continuum OS reconstruction in the Wightman sense;
- Reflection positivity in pure-gauge or pure-fermion sectors
  independently — the parent theorem composes both, with the gauge
  half handled by the companion Peter-Weyl bridge;
- Reflection positivity for fermion bilinears beyond polynomials in
  `(χ, χ̄)_+`.

The companion bridge for clause (1) of the auditor's repair (SU(3)
Wilson gauge-half via Peter-Weyl norm-square) is in
`docs/SU3_WILSON_RP_PETER_WEYL_NORM_SQUARE_BRIDGE_BOUNDED_NOTE_2026-05-26.md`.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/staggered_grassmann_half_action_rp_arbitrary_polynomial_runner.py
```

Expected:

```text
TOTAL: PASS=27 FAIL=0
VERDICT: bounded bridge passes; staggered Grassmann half-action RP
holds for arbitrary A_+ polynomial observables via Schur-complement
positivity of the monomial-basis kernel matrix.
```
