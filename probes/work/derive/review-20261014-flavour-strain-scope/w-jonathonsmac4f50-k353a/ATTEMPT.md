# Attempt: exact scope of the flavour-strain implication (X2-L8)

Task `J:derive:review-20261014-flavour-strain-scope:a1`. Worker: Claude Sonnet 5.5, same family as the source author (Opus 5.5). Unrefereed. Nothing here is accepted science.

## Plain-language summary

The source (X2 combination report) says: if the three generations are the three special-momentum corners of the walker, then any vacuum symmetry that allows quark-type mixing leaves room for a direction-dependent ("strain") term at first order. I rebuilt the classification with a different method and the numbers agree (1120 residual groups, 283 allow mixing). What the claim does and does not say is narrower than the report's wording:

1. It is a statement about what symmetry *allows*. It does not say the coefficient is nonzero, and it gives no size. Symmetry never forces a coefficient; the coefficient comes from dynamics that the axioms do not supply.
2. The strain that the flavour matrices can feed is only the "stretch along the cube axes" kind (two components). The "shear/body-diagonal" kind (three components) cannot be fed by the generation matrices at all, because the half-turns about the three axes act as the identity on the generation triplet, so they leave any generation-built quantity unchanged but flip the sign of shear components.
3. "Nontrivial mixing" in the source means "not a permutation". That includes mixing of only two generations. Mixing with all nine entries nonzero (what a real CKM needs) happens only when the residual symmetry acts as the identity on the generation triplet, so the symmetry then constrains nothing about flavour.
4. The strain-free escape needs a three-fold symmetry, and a three-fold symmetry forces trivial mixing. That direction is exact.

## What was read (stated as required)

- Read in full: `docs/MINIMAL_AXIOMS_2026-06-29.md` (233 lines) and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (130 lines), at main `a77a3449c9`.
- Relevant content: Lattice (cubic adjacency, proper cubic rotations, translations; `MINIMAL_AXIOMS_2026-06-29.md:37-41`), Qubit `M_2(C)` (`:43-53`), Admissibility supplies a distribution from nearest-neighbour conditions and "is not a dynamics axiom" (`:114-123`), Record: only records are readable (`:82-83`). The three registered primitives (scale reference, kinetic isotropy, realized state) each declare zero dimensionless content: no mixing angle, mass ratio, selector or coefficient (`PRIMITIVE_REGISTRY_CHECK.md:44, 89-90, 122-123`).
- Source objects: all four sha256 verified (see `RECOVERY_STATUS.json`). Read in full: `COMBO_REPORT.md`, `PREREG.md`, `x2_cert.py` lines 1-40 and 140-293, the run-1 `.out`. I re-ran `x2_cert.py` (unmodified copy): 1120 subgroups, violation list empty (`src_rerun.out:54`), strain-free count 61. The corrected `x2_cert.out` named in the report is not among the hashed objects, so its text is unverified; my rerun stands in for it.
- NOT read (not reachable on main or on the frozen source branch): TW-2 (`C5_TW2_report.md`), cited by the source for the "first-order strain" hazard. Its definition of the strain coupling is taken from the source's wording only.

## Setting and premises

- ASSUMED (lane-supplied, not axiom): the supplied continuous-time walker `H = sum_a sigma_a sin p_a` and its hw1 corners `(pi,0,0),(0,pi,0),(0,0,pi)` as the three generations (`COMBO_REPORT.md:32, 47`). Walker, Spin(10) matter and fermion statistics are supplied content (`COMBO_REPORT.md:212-214`).
- ASSUMED (reading of "residual symmetry"): a vacuum is described, on the generation index, by two Hermitian left-handed matrices A (up) and B (down), e.g. M M^dagger. They are invariant under the vacuum's stabiliser H, a subgroup of the symmetry group G below. A and B are the objects whose eigenbases give "mixing". Using one H for both sectors loses nothing: if the sectors have different residual groups, the vacuum's residual group is their intersection and both matrices are invariant under it.
- ASSUMED: strain is a traceless symmetric 3x3 tensor; rotations act on it, translations do not (`x2_cert.py:243-247`).
- Symmetry group G (derived, not assumed): lattice translations modulo 2 (only parity matters on the corner modes) extended by the 24 proper cubic rotations; order 192.

## Numbered steps

1. CHECKED (check.py R1-R4). The action of G on the three corner plane waves `(-1)^{x_i}` is derived from the lattice itself: translations act by diagonal signs, rotations by pure permutations (no sign, because `pi` and `-pi` are the same momentum). Exactly 8 symmetries act as a scalar +-1: the half-turns about the three axes and the identity, each with or without the all-three flip. Call this group K0.
2. CHECKED (E1-E5, disjoint method). All subgroups of G are enumerated as pairs (image in S4, translation kernel K) plus a 1-cocycle; the count is sum over (Q_H, K) of |Z^1| = 1120, matching the source's 1120 (obtained there by generator-pair closure). Cross-check: closure of every cyclic and 2-generated subgroup is in the list.
3. CHECKED (C1-C3). For each H, the dimension of the commutant of the 3-dim generation action, computed two ways (character norm, and fixed Hermitian matrices of the 9-dim action), agree for all 1120. Types: a (three distinct 1-dim characters) 485; b (repeated pair plus one) 267; c (scalar) 16; d (2-dim irrep plus 1) 291; e (3-dim irrep) 61. The source's counts by (order-3 rotation, distinct masses, nontrivial mixing) are reproduced: 231, 445, 283, 121, 40.
4. PROVED + CHECKED (A3, A4). If H contains a symmetry whose rotation part has order 3, its generation matrix has characteristic polynomial x^3-1 or x^3+1 (three distinct eigenvalues, 64 such symmetries, all checked). Its commutant is therefore diagonal, so any two H-invariant Hermitian matrices commute: no mixing. This is the exact content of the source's "a 3-cycle makes the commutant commutative".
5. PROVED + CHECKED (A1, A5). Without an order-3 rotation the rotation part is a 2-group, hence lies in a Sylow D4 of S4, which fixes a nonzero traceless strain (e.g. 2z^2-x^2-y^2): invariant strain >= 1 (the source's argument; checked for all such H). Combined with step 4: nontrivial mixing implies invariant strain >= 1 (A2). Added exactness: invariant strain is zero for exactly the 61 subgroups whose rotation part is the tetrahedral or octahedral group (A1). Order-3 rotation does not by itself kill strain: rotation part C3 or D3 keeps a body-diagonal strain (100 subgroups, A6). The source table leaves that cell blank (`COMBO_REPORT.md:128-134`).
6. PROVED (new scoping; checks R4, W2, I8, V1). Let F be any G-equivariant map from the vev data (A,B) to strain, of any degree or form. Every k in K0 fixes (A,B) (K0 acts as +-1 on the generations, so conjugation is trivial), so F(A,B) = F(kA,kB) = k.F(A,B). Hence F(A,B) lies in the K0-invariant strain, which is the diagonal traceless part (2 dim); the off-diagonal part (3 dim: xy, xz, yz) is excluded. The generation matrices alone can feed only the cube-axis-stretch (E-type) quadrupole, never the shear (T2-type) one. Checked: the 5-dim strain splits into invariant diagonal and off-diagonal parts; K0-invariants are exactly the diagonal part; dim Hom_G(Sym^d, off-diagonal strain) = 0 for d = 1, 2, 3; dim Hom into diagonal strain = 2, 17, 98.
   Scope: this is about data carried by A and B. Other order parameters of the vacuum (a Higgs profile with spin or momentum structure) can carry half-turn charge and feed shear strain; this attempt does not exclude them.
7. CHECKED (I1-I8). The exact stabiliser of a generic pair (A,B) in the fixed space of H is the pointwise fixer of that fixed space ("isotropy group"). It contains H and K0. Of the 1120 subgroups only 29 are isotropy groups. Among isotropy groups: all have zero invariant off-diagonal strain; those with an order-3 rotation (rotation part / V4 containing a 3-cycle) are strain-free with trivial mixing; nontrivial mixing occurs only with rotation part / V4 of order 1 or 2; exactly one isotropy group (K0 itself) has type c.
8. PROVED + CHECKED (B1-B3, I8). Realistic mixing, meaning all nine |V_ij| nonzero for non-degenerate spectra, forces ρ(H) scalar. Proof: with a non-degenerate spectrum all irreps of ρ(H) are 1-dim (a 2-dim irrep forces a degenerate pair), so A and B are block-diagonal in the isotypic decomposition and every eigenvector lies in one isotypic block; V is then block-diagonal across blocks, so nine nonzero entries needs one block of dimension 3, i.e. ρ(H) = +-1. By step 1, that is exactly H inside K0 (16 subgroups; D0 strain invariants = 2 for all of them). Consequence: a residual symmetry compatible with a CKM-like pattern puts no constraint on the generation index. The "mass degeneracies, representation assignments, residual groups excluded" reading is the table in step 12.
   Weaker mixing: type b gives mixing inside a 2+1 split (V_13 = V_23 = V_31 = V_32 = 0 exactly); that is "nontrivial" in the source's sense (`x2_cert.py:263`) but is not a realistic CKM (V_ub, V_cb, V_td, V_ts nonzero). Of the 283 groups in the source's headline, 267 are of this two-generation kind.
9. PROVED (short). For a finite group, the values at a point w of all polynomial covariants (equivariant maps to strain) fill the whole invariant space S^{Stab(w)}: define the equivariant function on the finite orbit by g.w -> g.s for any s in S^{Stab(w)}, extend it to a polynomial map, average over G. So symmetry never forbids a channel that S^{Stab(w)} allows, and every vacuum with nontrivial mixing has some nonzero covariant (by step 5). CHECKED on two vacua (V5, X3): rank of covariant values equals dim S^Stab by degree 3. Also CHECKED (V3, V4): the degree-1 covariant "traceless part of the corner-diagonal of A (and of B)" is equivariant and spans the whole invariant space of every isotropy group that has one, so the allowed channel is populated at linear order in the matrices generically.
10. CHECKED (X0-X3). Allowed is not forced, in two senses. (i) Kinematic: the exact rational full-mixing vacuum A = [[0,1,i],[1,0,1],[-i,1,0]], B = [[0,i,1],[-i,0,1],[1,1,0]] (zero diagonals, non-commuting, three distinct eigenvalues each, all |V_ij| >= 0.244 in float) has stabiliser K0, a 2-dim allowed strain channel, yet every degree-1 covariant vanishes; the first nonzero covariant is degree 2 (rank 2 at degrees 2 and 3). Its spectra are equal and not realistic masses, so this is a counterexample to "linear strain is automatic", not a flavour fit. (ii) Dynamical (PROVED, trivial): an energy function E(A,B,eps) with no eps-linear term is invariant under G, has the same vacua, and gives zero first-order strain response. The coefficient of each independent covariant is a free input of the supplied dynamics; the axioms supply no dynamics (`MINIMAL_AXIOMS_2026-06-29.md:114-123`).
11. CHECKED (T1, T2). Translation structure: exact single translations (isotropy group containing all of N) force diagonal A and B, so no mixing at all, and with a 3-cycle also a triple degeneracy. Every mixing-capable isotropy group (10 of 29) has pure-translation part K of order 2 ({0,111}) or 4 ({s : s_i = s_j} for the mixed pair); none preserves all unit translations. So any mixing needs a momentum-carrying condensate that breaks the single translations the light-mode protection relies on (`COMBO_REPORT.md:84-88`). Whether the supplied dynamics produces such a vacuum is not shown.
12. Exclusion table, CHECKED (isotropy groups of the generation data, 29 groups; rot/V4 is the rotation part modulo the half-turns):

| rot/V4 | type | groups | invariant diagonal strain | forced degeneracy / mixing |
|---|---|---|---|---|
| 1 | a | 1 | 2 | none / none (all translations kept) |
| 1 | b | 3 | 2 | none / two-generation only |
| 1 | c | 1 | 2 | none / full |
| 2 | a | 6 | 1 | none / none |
| 2 | b | 6 | 1 | none / two-generation only |
| 2 | d | 3 | 1 | one degenerate pair / none |
| 3 | a | 4 | 0 | none / none (strain-free, "T-circulant" kind) |
| 6 | d | 4 | 0 | one degenerate pair / none |
| 6 | e | 1 | 0 | all three equal / none |

   Excluded: nontrivial mixing together with strain-freeness; any 3-cycle together with mixing; full mixing together with any non-scalar generation action; three distinct masses together with a 2-dim or 3-dim irrep (types d, e); mixing together with exact single translations. Not excluded: any of the above once other order parameters or soft breaking are allowed (suggested, not checked).

## What is new relative to the sources

NEW (scoped, unrefereed): steps 6 and 7 (strain from the generation matrices is diagonal-only; isotropy closure; 29 of 1120), step 8 (realistic mixing means a generation-trivial residual symmetry; 267 of the 283 are two-generation only), step 9-10 (allowed versus populated versus forced, with an explicit exact vacuum and the finite-group lemma), step 11 (mixing needs a vacuum that breaks single translations), and the exact "strain-free iff rotation part is T or O" statement (step 5, 61 groups) with the C3/D3 gap in the source table.
NOT new: the 1120 count, the 283 count, the D4 argument, the circulant example, the "mixing implies invariant strain" implication (all in `COMBO_REPORT.md:126-136`, reproduced here by a different method). Open PR #9922 (candidate-laws, zoom-3 families) states a similar "translation invariance gives family-diagonal mixing" conclusion on a different carrier (cube tick); step 11 overlaps in spirit only. Overlap with #9998 and #10001 (family mass rules) not examined.

## Where the source wording outruns the result

- `COMBO_REPORT.md:49, 203, 218`: "unavoidable", "forces an axis". Proved: allowed. The same report says the size is not computed (`:49, :136`).
- `COMBO_REPORT.md:132`: "Nontrivial CKM" counts any non-permutation V (`x2_cert.py:263`), not a realistic CKM.
- `COMBO_REPORT.md:128-134`: the strain cell for "contains a C3" is blank; 100 of those groups do carry strain.
- The table ranges over all 1120 subgroups; only 29 are exact stabilisers of generation data.
- `x2_cert_run1_strainnorm_bug.out` shows "strain 0" for groups that have strain; known bug (`COMBO_REPORT.md:270`), not evidence.

## First unresolved step

Step 10(ii), the coefficient. Obligations, in order:
1. (coefficient) From a supplied, G-invariant vacuum functional E(A,B,eps), compute the eps-linear response, i.e. the coefficients of the covariants q_E(A) = diag(A) - tr(A)/3, the same for B, and their higher-degree companions, for a vacuum in a mixing isotropy group. No axiom or registered primitive supplies E.
2. (vacuum) Show the supplied dynamics yields a condensate with translation kernel K as in step 11, or state that mixing requires a different carrier.
3. (readout) A strain response is readable only through records (`MINIMAL_AXIOMS_2026-06-29.md:82-83`): define a record-determined observable, e.g. direction dependence of the hw1 light-cone speeds, and relate it to the diagonal quadrupole.
4. (scope) Soft breaking: a nearly-symmetric vacuum (small perturbation of a strain-free T-type group) gives mixing at the cost of a small strain, not zero; the exact theorem does not cover it (suggested).

## Labels summary

PROVED: steps 4, 5 (D4 part), 6, 8 (block argument), 9, 10(ii). CHECKED: steps 1-3, 5 (A1, A6), 7, 8 (B1-B3), 10(i), 11, 12; all exact except X1 (float eigenvalues). ASSUMED: setting and residual-symmetry reading above. READING: the physical interpretation of E-type strain as a readable anisotropy; the soft-breaking remark.
