# KCPT CP-completion under the extended group H = ⟨G_amb, S_eps⟩: the unique real 12 splits into CP-even 12⁺ and CP-odd 12⁻, and the 20 complex modes CP-double with their anti-holomorphic conjugates

**Type:** bounded_theorem
**Date:** 2026-07-20
**Lane:** KCPT (L = 4, N = 64 staggered qubit lattice over the 4³ cube)

## Claim boundary

This note records a complex-representation-theory computation about three specific derived operators — the staggered antisymmetric adjacency D2, the ambient-invariant total complex structure J_full, and the chiral-parity involution S_eps — on one finite lattice (L = 4, N = 64) together with the two derived finite groups G_amb (order 768) and its extension H = ⟨G_amb, S_eps⟩ (order 1536). It fixes no free parameter, selects no bulk sign-family member, and chooses no dynamics. "CP" is used throughout as a geometric label for the lattice parity involution S_eps, exactly as in the Unit-9/11 sibling notes; nothing here is a statement about Standard-Model CP or SM multiplets. Every load-bearing quantity is checked, with explicit wrong-value rejectors, by the companion runner `scripts/kcpt_cp_completion_under_extended_group_2026_07_20.py`.

## T1 — CP-completion decomposition

Adjoining the chiral-parity involution S_eps (Unit 9) to the ambient group G_amb yields the order-1536 group H = ⟨G_amb, S_eps⟩, in which G_amb sits as an index-2 subgroup; the nontrivial coset is S_eps·G_amb (768 elements, disjoint from G_amb). Unit 12 established that the holomorphic 32-plane W (the +i eigenspace of J_full) is a multiplicity-free complex G_amb-representation, `4 + 4 + 6 + 6 + 12 = 32`; Unit 13 identified the rank-12 constituent as the unique self-conjugate (real-type) piece, the two 4's and two 6's being complex-type.

For the extended action of H on the complexified full carrier V_R ⊗ C ≅ C^64 = W ⊕ H_− — with H_− the −i eigenspace of J_full, the anti-holomorphic 32-plane — the decomposition is

`C^64 = 8 + 8 + 12 + 12 + 12⁺ + 12⁻`  (six multiplicity-free constituents).

The four complex-type G_amb constituents (the two 4's and the two 6's) CP-double with their S_eps-images in H_−: each complex holomorphic constituent joins its anti-holomorphic conjugate into a single irreducible H-representation — the two rank-4's become two irreducible 8's and the two rank-6's become two irreducible 12's. The unique real 12 is the one constituent that does not fuse. Its 24-dimensional H-module — the real 12 in W together with its S_eps-image in H_− — is H-reducible and splits into a CP-even 12⁺ and a CP-odd 12⁻, inequivalent, each meeting W and H_− evenly. The superscripts label the two extensions that differ by the quotient sign character; they do not mean that S_eps acts pointwise as +I or −I on the whole 12-dimensional constituent. "Splits" versus "fuses" is here always a statement about the 24- / 8- / 12-dimensional H-module, never about a subspace of W alone: S_eps carries W ↔ H_− and fixes no nonzero subspace of W.

## T2 — the exact-integer discriminator

The commutant dimensions are exact integers read directly off the signed-permutation traces χ(h) = tr(h) ∈ Z:

- c_G = dim_C End_{G_amb}(C^64) = (Σ_{g∈G_amb} tr(g)²) / |G_amb| = 9216 / 768 = 12,
- c_H = dim_C End_H(C^64) = (Σ_{h∈H} tr(h)²) / |H| = 9216 / 1536 = 6.

The value c_H = 6 (six constituents) rather than 5 (a single unsplit 24) is precisely the statement that the real 12 splits. Every element of the coset S_eps·G_amb is traceless in the 64-rep — Σ_coset tr² = 0 and max|tr| = 0 — because S_eps anticommutes both with the adjacency, S_eps·D2·S_eps = −D2, and with the complex structure, `S_eps J_full S_eps = -J_full` (Unit 9): the coset elements interchange W and H_− and therefore carry zero diagonal. Within the index-2 extension already established independently by the order and disjoint-coset gate, this is the exact-integer signature of the W ↔ H_− action; tracelessness alone is not being used to prove index two.

## T3 — the 12⁺/12⁻ split, three complementary checks

The 24-dimensional H-module built from the real 12 in W together with its S_eps-image in H_− splits as 12⁺ ⊕ 12⁻. This is checked three complementary ways, each testing a distinct consequence and able to fail on its own:

1. **H-commutant dimension 2.** The H-restricted commutant of the 24-block has dimension 2 — two inequivalent H-irreducibles — whereas each of the four complex-pair blocks has H-commutant dimension 1. Splitting the 24-block by a generic self-adjoint element of its H-commutant yields two sub-idempotents of equal rank, sorted [12, 12]. Each 12-half meets W and H_− evenly: tr(Π_{12⁺}·Π_W) = tr(Π_{12⁺}·Π_{H_−}) = 6, and likewise for 12⁻. This is forced — 12⁺ is H-invariant, hence S_eps-invariant, while S_eps swaps Π_W ↔ Π_{H_−}, so the two overlaps are S_eps-conjugate and sum to dim 12. Neither overlap is 0 or 12: the split is CP-diagonal, not a relabelling of W versus H_−.

2. **G_amb-commutant dimension 4 = M_2.** The same 24-block, restricted to G_amb alone, has commutant dimension 4 = M_2: under G_amb the 24 is two copies of one irreducible — the self-conjugate real 12, whose anti-holomorphic image is G_amb-isomorphic to itself. G_amb-commutant 4 (M_2, same content) versus H-commutant 2 (split by the coset): the split is created by the coset, not by G_amb.

3. **Opposite coset character = χ_sgn.** Exhaustively over all elements, the two half-characters agree on G_amb and are opposite on S_eps·G_amb; a nonzero coset value confirms that the two characters are distinct. The two halves therefore differ exactly by the nontrivial sign character χ_sgn of H/G_amb ≅ Z/2, so 12⁻ = 12⁺ ⊗ χ_sgn. This character check uses the halves constructed by the commutant split, so it characterizes and cross-checks that split rather than constituting a disjoint construction of the halves.

Multiplicity-freeness follows as a corollary of the two gated integers rather than a separate probe: count = 6 constituents together with c_H = 6 forces Σ_i m_i² = 6 over six terms, hence every multiplicity m_i = 1 — the two 8's are inequivalent and the four 12's pairwise inequivalent (a repeated irreducible would push c_H ≥ 8).

## Honest boundary

In the full 64-representation every h ∈ H is a signed permutation, so its character tr(h) ∈ Z is an integer (and coset elements are traceless, tr = 0). Irrationality appears only on the 24-block-restricted half-characters χ_{12±}, which are built with the √m bulk-shell normalizers of J_full; exhaustive evaluation gives real values in Q(√2), with the only noninteger pair ±2√2, and no imaginary character component above floating tolerance. Only the summed exact-integer class invariants (c_G = 12, c_H = 6, coset trace-sum = 0) and the integer decomposition dimensions are fixed as numeric gate targets. G15 gates equality on all of G_amb, opposition on all of the coset, a nonzero witness, and reality; it does not gate any half-character to the numeric value ±2√2.

This is a complex-representation fact about specific derived operators (J_full, D2, S_eps) on one finite lattice and one derived group — not a claim about Standard-Model CP or SM multiplets; "CP" here is a geometric label for the lattice parity involution S_eps, the same geometric-label reading as the Unit-9/11 sibling notes. All parents (Units 8, 9, 10, 12, 13) are currently unaudited; this note inherits that and makes no retained-grade or publication-usable claim. It fixes no free parameter, selects no bulk sign-family member, and chooses no dynamics; it is r-neutral, orientation-neutral, and takes no external numerical or literature input.

## Two paths this opens

- Whether the CP-even 12⁺ and CP-odd 12⁻ carry distinguished internal structure as candidate chiral half-sectors — the next question this hands forward is what geometric data on the lattice separates the two halves beyond the bare coset sign.
- How the two CP-doubled 8's and two 12's organize relative to the split real backbone under the full extended group — a route toward reading the CP-doubling pattern of the complex modes against the one self-conjugate constituent that splits.

## Runner evidence

Companion runner: `scripts/kcpt_cp_completion_under_extended_group_2026_07_20.py`. Each gate below contributes one PASS; the anti-fabrication rejectors (a √m→1 non-complex-structure proxy, wrong commutant values, a vacuous or all-traceless-G_amb coset, a W/H_− relabelling of the split) are wired to FAIL if the object were wrong.

| Gate | What it discriminates | Pass |
|------|-----------------------|------|
| G1 | \|G_amb\| = 768; G_amb commutes with D2 (exact) and J_full ([FLOAT]) — complex-linear action; TR-shift witness non-vacuous | 1 |
| G2 | J_full² = −I, antisymmetric; anti-proxy rejector — the √m→1 rational stand-in fails J² = −I and differs from J_full | 1 |
| G3 | +i and −i eigenspaces of J_full each dim 32 (W holo, H_− anti-holo) | 1 |
| G4 | S_eps·D2·S_eps = −D2 (exact integer): S_eps anticommutes with the adjacency | 1 |
| G5 | S_eps·J_full·S_eps = −J_full ([FLOAT]); rejector ≠ +J_full — S_eps carries W → H_− | 1 |
| G6 | \|H\| = 1536 = 2·768; G_amb ⊆ H; coset ⊆ H and disjoint (index 2); rejectors ≠ 768, ≠ 3072 | 1 |
| G7 | c_G = 12 from real integer traces (Σ tr² = 9216); rejectors ≠ 10, 11, 13 | 1 |
| G8 | c_H = 6 from real integer traces (Σ tr² = 9216); rejectors ≠ 5, 7 — c_H = 6 ⟺ real 12 splits | 1 |
| G9 | coset traceless (Σ tr² = 0, max\|tr\| = 0); non-vacuous and G_amb not all-traceless (max\|tr\| = 64) | 1 |
| G10 | idempotent tiling: Σ PW_k = Π_W, Σ PHm_k = Π_{H_−}, each PHm_k supported in H_− ([FLOAT]) | 1 |
| G11 | per-block H-commutant dims [1,1,1,1,2]; the dim-2 block is exactly the rank-12; Σ = 6 = c_H | 1 |
| G12 | full H-decomposition dims sorted [8,8,12,12,12,12]; mult-free corollary; rejectors ≠ [8,8,12,12,24], [4,4,6,6,12,32] | 1 |
| G13 | proof 1 — 24-block H-commutant 2, sub-idempotents [12,12], each half evenly 6+6 in W and H_− (CP-diagonal) | 1 |
| G14 | proof 2 — 24-block G_amb-commutant 4 = M_2 (same content); rejectors ≠ 2, ≠ 1 | 1 |
| G15 | character cross-check — half-characters equal on all 768 G_amb elements, opposite on all 768 coset elements, real, and nonzero for a witness; value ±2√2 not gated | 1 |
| G-MEM | greedy generating sets close to exactly 768 / 1536; loose length bounds; commutants use generators only | 1 |
| G-PIN-U9 | Unit-9 note contains `S_eps J_full S_eps = -J_full` | 1 |
| G-PIN-U12 | Unit-12 note contains `4 + 4 + 6 + 6 + 12 = 32` | 1 |
| G-PIN-U13 | Unit-13 note contains `FS = (0, 0, 0, 0, +1)` | 1 |
| G-PIN-SELF | this note carries exactly three KCPT dependency links (Units 12, 13, 9); Units 8/10/11 backticked only | 1 |

## Dependencies

- [Unit 12 holomorphic G_amb-representation note](KCPT_HOLOMORPHIC_GAMB_REPRESENTATION_BOUNDED_THEOREM_NOTE_2026-07-20.md) — the five constituents `4 + 4 + 6 + 6 + 12 = 32` that CP-complete, and c_G = 12.
- [Unit 13 holomorphic reality / CP census note](KCPT_HOLOMORPHIC_REALITY_CP_CENSUS_FROBENIUS_SCHUR_BOUNDED_THEOREM_NOTE_2026-07-20.md) — the rank-12 is the unique self-conjugate constituent, so it is the one constituent that can split under CP.
- [Unit 9 chiral-parity common-sign-orbit note](KCPT_CHIRAL_PARITY_COMMON_SIGN_ORBIT_BOUNDED_THEOREM_NOTE_2026-07-19.md) — S_eps and the exact sign reversals S_eps·D2·S_eps = −D2 and `S_eps J_full S_eps = -J_full`: the index-2 CP-extension engine and why the coset is traceless.

Units 8, 10, and 11 enter only transitively via Units 12/13/9 and are referenced by name only, never as dependency links: the total complex structure J_full assembled in `KCPT_TOTAL_COMPLEX_STRUCTURE_AMBIENT_INVARIANT_KERNEL_BULK_ASSEMBLY_BOUNDED_THEOREM_NOTE_2026-07-19.md`, the Kähler triple of `KCPT_KAHLER_TRIPLE_AMBIENT_INVARIANT_METRIC_SYMPLECTIC_BOUNDED_THEOREM_NOTE_2026-07-19.md`, and the real-Lagrangian polarization of `KCPT_CHIRAL_PARITY_LAGRANGIAN_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-19.md`.
