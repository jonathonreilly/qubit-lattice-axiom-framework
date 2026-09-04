# KCPT H-level Frobenius-Schur reality census: the six CP-completed constituents {8, 8, 12, 12, 12⁺, 12⁻} are all real/orthogonal type, and the CP-completion realifies the holomorphic census

**Type:** bounded_theorem
**Date:** 2026-07-20
**Lane:** KCPT (L = 4, N = 64 staggered qubit lattice over the 4³ cube)

## Claim boundary

This note records a complex-representation-theory computation about three specific derived operators — the staggered antisymmetric adjacency D2, the ambient-invariant total complex structure J_full, and the chiral-parity involution S_eps — on one finite lattice (L = 4, N = 64), together with the two derived finite groups G_amb (order 768) and its extension H = ⟨G_amb, S_eps⟩ (order 1536). It fixes no free parameter, selects no bulk sign-family member, and chooses no dynamics. "CP" is used throughout as a geometric label for the lattice parity involution S_eps, exactly as in the Unit-9/11/13/14 sibling notes; nothing here is a statement about Standard-Model CP or SM multiplets. Every load-bearing quantity is computed from real group sums and real bilinear-form singular values — never from the ranks or the expected value — and is checked, with explicit wrong-value rejectors, by the companion runner `scripts/kcpt_extended_group_reality_census_2026_07_20.py`.

## T1 — the H-level reality census

Unit 14 decomposed the complexified full carrier V_R ⊗ C ≅ C^64 into six multiplicity-free constituents under the order-1536 extended group H = ⟨G_amb, S_eps⟩:

`C^64 = 8 + 8 + 12 + 12 + 12⁺ + 12⁻`  (four CP-doubled complex blocks and the two halves of the split real 12).

The Frobenius-Schur reality census of these six constituents is

`FS_H = (+1, +1, +1, +1, +1, +1)`  — every constituent is real / orthogonal type.

Each indicator is computed two independent ways (below), and both give +1: none of the six is complex-type (indicator 0) and none is symplectic/quaternionic (indicator −1). The six real dimensions are (8, 8, 12, 12, 12, 12).

## T2 — the realification map

Over G_amb alone, the five holomorphic constituents of the 32-plane W (the +i eigenspace of J_full, ranks 4, 4, 6, 6, 12) carry the reality census `(0, 0, 0, 0, +1)` (Unit 13): the two 4's and two 6's are complex-type, and only the rank-12 is real-type. Adjoining S_eps and passing to H realifies the whole census,

`(0, 0, 0, 0, +1)` over ranks (4, 4, 6, 6, 12)  →  `(+1, +1, +1, +1, +1, +1)` over (8, 8, 12, 12, 12, 12).

The four complex-type G_amb constituents each fuse with their anti-holomorphic S_eps-image into a single self-dual real induced H-representation: a complex-type constituent V and its conjugate together carry an H-invariant symmetric form that neither carries alone, so each induced 8 or 12 is orthogonal-type (+1). The unique real-type 12 does not fuse; it splits into 12⁺ ⊕ 12⁻, and each half remains real-type (+1). Thus the four complex-type W-blocks flip 0 → +1 under CP-completion while the real 12 stays +1 in both split halves, and the census sum moves from 1 to 6.

The mechanism is isotropy cured by CP-completion, stated here as the reason rather than an assumption. Because J_full is real antisymmetric (Jᵀ = −J), both eigenspaces W (+i) and H_− (−i) are totally isotropic for the symmetric form B(u, v) = uᵀv: for Ju = iu and Jv = iv one has uᵀv = (Ju)ᵀ(Jv) = (iu)ᵀ(iv) = −uᵀv, forcing uᵀv = 0. The symmetric form therefore vanishes identically on any holomorphic-only block, so no G_amb-constituent inside W can be certified real by B on its own. B becomes nondegenerate only on a CP-completed block, which meets both W and H_− and is paired across the two by S_eps; that cross-pairing supplies the H-level real structure. For the four formerly complex-type blocks, the +1 type is produced by the S_eps CP-doubling; for the already-real rank-12 block, CP-completion instead resolves its two +1 H-extensions.

## T3 — alignment with the metric leg of the Kähler triple

A Frobenius-Schur indicator +1 means the constituent carries a nonzero H-invariant SYMMETRIC (g-like, metric) bilinear form; an indicator −1 would mean it carries an antisymmetric (ω-like, symplectic) one instead. The ambient Kähler triple (Unit 10) pairs the symmetric metric g with the antisymmetric symplectic form ω through J_full. All six indicators being +1 says every constituent of the CP-completed carrier is aligned with the SYMMETRIC, metric leg of that triple — the invariant form each constituent carries is g-like, none ω-like/symplectic. The CP-completion thus renders the entire 64-dimensional carrier orthogonal-type with respect to the metric leg g of the Kähler triple assembled in `KCPT_KAHLER_TRIPLE_AMBIENT_INVARIANT_METRIC_SYMPLECTIC_BOUNDED_THEOREM_NOTE_2026-07-19.md`.

## Methods

The census is computed two independent ways, and both give +1 on all six constituents.

Method A — group-sum Frobenius-Schur. For each constituent projector P_i, FS_i = (1/|H|) Σ_{h∈H} χ_i(h²) = tr(P_i · T) with T = (1/|H|) Σ_{h∈H} h@h. The identity tr(P_i R(h²)) = χ_i(h²) holds because each P_i commutes with the H-action; this commutation is verified first as a precondition rejector — if any commutator ‖[P_i, R(h)]‖ were nonzero the group-sum would be void. The sum T is accumulated from the actual group elements (real signed-permutation matrices), never from the ranks or the target +1.

Method B — invariant symmetric bilinear form. Every h ∈ H is a real orthogonal signed permutation, so the symmetric form B(u, v) = uᵀv (no complex conjugation) is H-invariant. Restricting B to a Hermitian-orthonormal basis Z_i of constituent i (64 × r, the top-r eigenvectors of (P_i + P_iᴴ)/2) gives the complex symmetric matrix G_i = Z_iᵀ Z_i; its minimum singular value is positive exactly when B is nondegenerate on the constituent, i.e. when the constituent is real/orthogonal type. All six give minimum singular value ≈ 1.

The built-in discriminator. Because W and H_− are each totally B-isotropic, B vanishes on any holomorphic-only block: the minimum singular value of G restricted to PW[k] alone is ≈ 0 (a live rejector gate), while on the CP-completed block PW[k] + PHm[k] it is ≈ 1. The contrast — degenerate on the un-completed W-only block, nondegenerate only after the S_eps CP-doubling — is gated directly, so a +1 that was merely assumed rather than caused by the CP-completion would fail the runner.

## Honest boundary

In this census every h ∈ H acts in the full 64-representation as a signed permutation, so its full character tr(h) is an integer (and the coset elements S_eps·G_amb are traceless); each constituent character χ_i(h) = tr(P_i h) is real, and every Frobenius-Schur indicator is the integer +1. Real does not mean rational: the two 12± constituent characters are the Unit-14 half-characters built with the √m bulk-shell normalizers of J_full, and they can take the real irrational values ±2√2. Those individual values are not gate targets here. This census decides reality entirely by gate structure — group-sum indicators and symmetric-form nondegeneracy — never by matching an individual irrational character value.

This is a complex-representation fact about specific derived operators (J_full, D2, S_eps) on one finite lattice and its two derived groups — not a claim about Standard-Model CP or SM multiplets; "CP" here is a geometric label for the lattice parity involution S_eps, the same geometric-label reading as the Unit-9/11/13/14 sibling notes. All parents (Units 8, 9, 10, 12, 13, 14) are currently unaudited; this note inherits that and makes no retained-grade or publication-usable claim. It fixes no free parameter, selects no bulk sign-family member, and chooses no dynamics; it is r-neutral, orientation-neutral, and takes no external numerical or literature input.

## Two paths this opens

- Whether the six real symmetric forms can each be pinned to a canonical g-like normalization against the single ambient metric — the next question this hands forward is what fixes the relative scale of the six invariant forms relative to the metric leg of the Kähler triple.
- How the realified census interacts with the 12⁺/12⁻ chiral split — the route this hands forward is reading the two real half-forms of the split 12 against the four CP-doubled real forms, toward whether the reality pattern constrains a chiral half-sector assignment.

## Runner evidence

Companion runner: `scripts/kcpt_extended_group_reality_census_2026_07_20.py`. Each gate below contributes one PASS; the anti-fabrication rejectors (a √m→1 non-complex-structure proxy, the wrong split ranks, a non-commuting projector, the W-only isotropic form, and the wrong constituent count) are wired to FAIL if the object were wrong.

| Gate | What it discriminates | Pass |
|------|-----------------------|------|
| G-CONSTRUCT-GROUP | reconstructed \|G_amb\| = 768 and \|H\| = 1536; G_amb ⊂ H and the disjoint 768-element S_eps·G_amb coset completes H; rejectors \|H\| ≠ 768, 3072 | 1 |
| G-CONSTRUCT-J2 | J_full² = −I_64 and antisymmetric from the independent shell/kernel rebuild — no sign proxy | 1 |
| G-CONSTRUCT-PROXY | anti-proxy rejector — the √m→1 rational stand-in fails J² = −I (residual ≈ 0.6) and differs from J_full | 1 |
| G-CONSTRUCT-SEPS | S_eps J_full S_eps = −J_full (float tolerance, rejector ≠ +J_full) and exact-integer S_eps D2 S_eps = −D2 | 1 |
| G-DECOMP-IDEM | all six P6 idempotent (‖P²−P‖ < 1e-8) | 1 |
| G-DECOMP-COMPLETE | the six P6 tile the identity (‖Σ P6 − I_64‖ < 1e-8) | 1 |
| G-DECOMP-RANKS | integer ranks sorted [8,8,12,12,12,12] summing to 64; rejectors ≠ [8,8,12,12,24], ≠ [4,4,6,6,12,32] | 1 |
| G-FSGROUP-COMM | precondition — every P_i commutes with every H generator (else the group-sum FS is void) | 1 |
| G-FSGROUP-FS | Method A group-sum FS_i = tr(P_i·T), T = mean_H h@h: all six real parts +1, imaginary parts 0 | 1 |
| G-FSFORM-CP | Method B symmetric-form minimum singular value > 1e-6 (≈ 1.0) on all six CP-completed blocks | 1 |
| G-FSFORM-WONLY | built-in W-only rejector — form min-sv < 1e-6 on the holomorphic-only complex-type blocks (W isotropic) while CP-completed > 1e-6 | 1 |
| G-AGREE | Methods A and B agree on all six (+1); none complex-type (all \|FS\| = 1), none symplectic (no −1) | 1 |
| G-REALCHAR | χ_i(h) = tr(P_i h) real over all 1536 h ∈ H (max_h \|Im χ_i\| < 1e-9): self-dual/real directly | 1 |
| G-REALIFY-BEFORE | before-census over G_amb on the five holomorphic PW: FS_G sorted [0,0,0,0,1], sum 1 (reproduces Unit 13) | 1 |
| G-REALIFY-AFTER | after-census over H: sum(FS_H) = 6; the four complex W-blocks flip 0 → +1, the real 12 stays +1 in both halves | 1 |
| G-COUNT | c_H = (Σ_{h∈H} tr(h)²)/1536 = 6 from real integer traces; rejectors ≠ 5, ≠ 7 | 1 |
| G-PIN-U14 | Unit-14 note contains `C^64 = 8 + 8 + 12 + 12 + 12⁺ + 12⁻` | 1 |
| G-PIN-U13 | Unit-13 note contains `FS = (0, 0, 0, 0, +1)` | 1 |
| G-PIN-SELF | this note carries exactly two KCPT dependency links (Units 14, 13); Units 9/10 backticked only | 1 |

## Dependencies

- [Unit 14 CP-completion under the extended group note](KCPT_CP_COMPLETION_UNDER_EXTENDED_GROUP_BOUNDED_THEOREM_NOTE_2026-07-20.md) — the six-constituent decomposition `C^64 = 8 + 8 + 12 + 12 + 12⁺ + 12⁻` being censused, and the extended group H = ⟨G_amb, S_eps⟩ with c_H = 6.
- [Unit 13 holomorphic reality / CP census note](KCPT_HOLOMORPHIC_REALITY_CP_CENSUS_FROBENIUS_SCHUR_BOUNDED_THEOREM_NOTE_2026-07-20.md) — the before-census `(0, 0, 0, 0, +1)` over the five holomorphic W-constituents that this unit realifies.

Unit 10 and Unit 9 enter only as backticked named context, never as dependency links: the Kähler triple `KCPT_KAHLER_TRIPLE_AMBIENT_INVARIANT_METRIC_SYMPLECTIC_BOUNDED_THEOREM_NOTE_2026-07-19.md` (Unit 10), whose metric leg g the six +1 indicators align with, and the chiral-parity involution S_eps of `KCPT_CHIRAL_PARITY_COMMON_SIGN_ORBIT_BOUNDED_THEOREM_NOTE_2026-07-19.md` (Unit 9), the CP-doubling engine of the realification.
