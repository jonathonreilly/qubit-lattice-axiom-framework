# KCPT symplectic-leg χ_sgn-covariance: the Unit-10 form ω = −J_full is sign-covariant under H = ⟨G_amb, S_eps⟩, sorting the six-constituent CP-completion into two symplectic classes and canonically pairing the chiral backbone 12⁺ ↔ 12⁻

**Type:** bounded_theorem
**Date:** 2026-07-20
**Lane:** KCPT (periodic L = 4, N = 64 staggered qubit lattice on the 4³ torus)

## Claim boundary

This note records a symplectic-form covariance and a bilinear-pairing census for a set of already-derived objects on one finite periodic lattice (L = 4, N = 64): the symplectic leg ω = −J_full of the Unit-10 Kähler triple, the lattice-parity involution S_eps, the extended group H = ⟨G_amb, S_eps⟩ (order 1536, with G_amb of order 768 sitting as an index-2 subgroup and the coset S_eps·G_amb its 768 nontrivial elements), the order-2 quotient character χ_sgn of H/G_amb ≅ ℤ/2, and the six Unit-14 constituents C⁶⁴ = 8 ⊕ 8 ⊕ 12 ⊕ 12 ⊕ 12⁺ ⊕ 12⁻. It inherits the Unit-10 counting metric g = I and that parent's chosen J_full sign-family representative; it does not derive or select either choice. It fixes no new free parameter, selects no bulk sign-family member, chooses no dynamics, and is r-neutral and orientation-neutral. "CP" and "chiral" are used throughout as geometric labels for the lattice-parity involution S_eps and the two split halves of the real-12; nothing here is a statement about Standard-Model CP or Standard-Model chirality. Every load-bearing quantity is checked, with explicit wrong-sign or wrong-value rejectors, by the companion runner `scripts/kcpt_symplectic_leg_chisgn_covariance_omega_pairing_2026_07_20.py`.

## T1 — χ_sgn-covariance of ω under H

ω := −J_full is the symplectic leg of the Unit-10 Kähler triple. Over H it satisfies

`hᵀ ω h = χ_sgn(h) · ω`   for every h ∈ H,

i.e. ω is preserved on G_amb (Uᵀ ω U = +ω, the Unit-10 fact) and sign-reversed on the coset (cᵀ ω c = −ω). The generator identity is Sᵀ_eps ω S_eps = −ω, which follows from Unit 9's S_eps J_full S_eps = −J_full together with ω = −J_full and S_eps diagonal (S_eps = Sᵀ_eps): Sᵀ_eps ω S_eps = −(S_eps J_full S_eps) = −(−J_full) = J_full = −ω.

The companion runner obtains bit-for-bit zero deviation in its rebuilt double-precision matrices on all 768 G_amb elements (+ω) and all 768 coset elements (−ω), and for S_eps itself. It also gates the group and coset cardinalities, disjointness, and normalization needed for H = G_amb ⊔ S_eps·G_amb; each covariance check carries a live wrong-sign rejector — a deviation of the wrong sign is 2·max|ω| = 0.748, which exceeds max|ω| = 0.3739.

Physics reading: the symplectic form is not H-invariant but H-sign-covariant — the coset (the "CP" lattice reflection) reverses the symplectic two-form while the metric g = I is untouched. In real dimension 64, this antisymplectic action does not reverse the induced real orientation, because (−ω)³² = ω³².

## T2 — the ω-pairing census of the six constituents

Take Hermitian-orthonormal bases Z_i of the complexified Unit-14 constituents and form the complex-bilinear extension of the real symplectic pairing, Ω_ij = Z_iᵀ ω Z_j (transpose, no conjugation). The pattern is:

- The four induced constituents {8_a, 8_b, 12_a, 12_b} each self-pair nondegenerately: their ω self-blocks have ranks 8, 8, 12, 12 respectively.
- 12⁺ and 12⁻ are each ω-isotropic: ω vanishes identically within 12⁺ and within 12⁻.
- The cross pairing 12⁺ ↔ 12⁻ is nondegenerate, rank 12.
- Every other constituent pair has vanishing ω-block.
- Accounting: total ω-rank = 40 (four self-blocks: 8+8+12+12) + 24 (2×12 for the one 12⁺ ↔ 12⁻ cross) = 64. The assembled Gram G = Z_cᵀ ω Z_c over all of C⁶⁴ is antisymmetric (‖G + Gᵀ‖ ≈ 0) and nondegenerate (rank 64), consistent with ω being a symplectic form on the full 64-space.

Selection rule (the representation-theoretic explanation, consistent with T1 and this pattern, not an independent claim). For irreducible constituents and a form obeying `hᵀ ω h = χ_sgn(h) ω`, a nonzero block requires V_j ≅ V_i* ⊗ χ_sgn. In the multiplicity-free Unit-14 decomposition, nondegeneracy of ω then pairs every constituent with its unique χ_sgn-twisted dual. The four induced constituents are χ_sgn-invariant and self-partner; the split halves obey 12⁻ ≅ 12⁺ ⊗ χ_sgn, so the 12⁺ self-block is zero and ω pairs 12⁺ nondegenerately with 12⁻. Physics reading: ω sorts the six-constituent CP-completion into two symplectic classes and canonically pairs the chiral backbone 12⁺ ↔ 12⁻.

## T3 — symmetric-vs-antisymmetric contrast on 12⁺

On the single Unit-14 constituent 12⁺, the invariant SYMMETRIC form has all 12 singular values equal to 1 within 1e-12, so 12⁺ is nondegenerate under the symmetric form, while the ANTISYMMETRIC ω self-block on the same 12⁺ vanishes (‖·‖ ≈ 1.0e-14). The symmetric value agrees with the separately computed Unit-15 census, but the gate here checks the structural target 1 directly rather than comparing two copies of the same local computation. The isotropy in T2 is therefore a genuine consequence of ω's antisymmetry twisted by χ_sgn (12⁺ ⊗ χ_sgn = 12⁻ ≠ 12⁺), not a subspace degeneracy: a computation that used the wrong (symmetric) form would find nondegeneracy everywhere and fail this contrast.

## Honest boundary

Only integer ranks and tolerance-separated zero / covariance quantities are gated, each with a wrong-sign or wrong-value rejector; the selection rule is the standard Schur fact for a G-invariant-up-to-character form, specialized to H with χ_sgn. ω = −J_full is real, orthogonal, antisymmetric (max entry 0.3739…) and nondegenerate on the full 64-space.

The direct parents (Units 10 and 14) are currently unaudited; this note inherits their unresolved KCPT dependency chain and makes no retained-grade or publication-usable claim. The periodic boundary, g = I counting metric, and chosen J_full sign-family representative are inherited finite-surface inputs, not outputs of this note. It fixes no new free parameter, selects no bulk sign-family member, chooses no dynamics; it is r-neutral, orientation-neutral, and takes no external numerical or literature input.

## Two paths this opens

- The canonical 12⁺ ↔ 12⁻ symplectic pairing gives the split real backbone a distinguished nondegenerate structure — the next question this hands forward is what lattice object (dynamical or metric) this symplectic pairing of the two chiral halves controls.
- Each of the four induced constituents carries its own nondegenerate ω-block — a route toward reading the symplectic geometry of the CP-doubled complex modes against the symplectically-paired real backbone.

## Runner evidence

Companion runner `scripts/kcpt_symplectic_leg_chisgn_covariance_omega_pairing_2026_07_20.py` reports `TOTAL: PASS=16 FAIL=0`. Each row below is one gate; the covariance and pairing rows each carry a live wrong-sign or wrong-value rejector wired to FAIL if the object were wrong.

| Gate | Checks | What it discriminates |
|------|--------|-----------------------|
| `G-CONSTRUCT-J2` | J_full² = −I₆₄ (inherited) | rejects a non-complex-structure J. |
| `G-DECOMP-COMPLETE` | the six constituent projectors are Hermitian idempotents, mutually orthogonal, H-invariant, and sum to I₆₄ | rejects an incomplete, overlapping, or non-constituent decomposition. |
| `G-DECOMP-RANKS` | constituent ranks are exactly [8, 8, 12, 12, 12, 12] | rejects a mis-dimensioned split. |
| `G-OMEGA-DEF` | ω = −J_full is real antisymmetric, rank 64 | rejects a symmetric or degenerate form. |
| `G-OMEGA-INV` | \|G_amb\| = 768 and gᵀ ω g = +ω on every element (dev 0.00e+00) | rejects an incomplete reconstructed group; wrong-sign rejector 0.748 > max\|ω\| 0.3739. |
| `G-OMEGA-COSET` | the 768-element coset is unique, disjoint, and normalized, and cᵀ ω c = −ω on every coset element (dev 0.00e+00) | rejects an invalid index-2 extension; wrong-sign rejector 0.748 > max\|ω\| 0.3739. |
| `G-OMEGA-SEPS` | Sᵀ_eps ω S_eps = −ω (dev 0.00e+00) | wrong-sign rejector 0.748 > max\|ω\| 0.3739. |
| `G-PAIR-INDUCED` | the four induced self-blocks are nondegenerate, ranks [8, 8, 12, 12] | rejects a collapsed induced block. |
| `G-PAIR-ISOTROPIC` | ω vanishes within 12⁺ and within 12⁻ (‖·‖ ≈ 1.0e-14) | rejects a non-isotropic split half. |
| `G-PAIR-CROSS` | the 12⁺ ↔ 12⁻ cross-block has rank 12 | rejects a degenerate chiral pairing. |
| `G-PAIR-OFFDIAG` | every other constituent pair has vanishing ω-block (‖·‖ ≈ 3.7e-13) | rejects a spurious cross pairing. |
| `G-PAIR-RANK` | assembled Gram G = Z_cᵀ ω Z_c is antisymmetric, rank 64; accounting 40 + 2×12 = 64 | rejects a rank-deficient assembly. |
| `G-CONTRAST-SYMVSANTI` | on 12⁺: all symmetric-form singular values equal 1 within 1e-12, while the ω self-block is isotropic (‖·‖ ≈ 1.0e-14) | rejects a rounded/idealized anchor or a computation using the wrong bilinear form. |
| `G-PIN-U14` | the Unit-14 six-constituent decomposition string is present in the Unit-14 note | pins the parent claim to its source text. |
| `G-PIN-U10` | the Unit-10 symplectic-leg identities ("J_full^T g = -J_full" and "U^T omega U = omega") are present in the Unit-10 note | pins the parent claim to its source text. |
| `G-PIN-SELF` | this note carries exactly two dependency links (Unit-14 and Unit-10) and none to Units 9/13/15 | pins the declared dependency edges. |

## Dependencies

- [Unit 14 CP-completion under the extended group](KCPT_CP_COMPLETION_UNDER_EXTENDED_GROUP_BOUNDED_THEOREM_NOTE_2026-07-20.md) — supplies the six-constituent H-decomposition C⁶⁴ = 8 ⊕ 8 ⊕ 12 ⊕ 12 ⊕ 12⁺ ⊕ 12⁻ and the χ_sgn relation 12⁻ ≅ 12⁺ ⊗ χ_sgn between the split halves.
- [Unit 10 ambient-invariant Kähler triple](KCPT_KAHLER_TRIPLE_AMBIENT_INVARIANT_METRIC_SYMPLECTIC_BOUNDED_THEOREM_NOTE_2026-07-19.md) — supplies the symplectic leg ω = −J_full of the Kähler triple (J_full^T g = −J_full) and its G_amb-invariance U^T ω U = ω.

Units 8, 9, 11, 12 and 13 enter only transitively (through Units 14 and 10); Unit 15 is a sibling census (also a child of Unit 14) whose symmetric-form result is a non-load-bearing consistency comparison in T3. All are referenced here by name only, never as dependency links.
