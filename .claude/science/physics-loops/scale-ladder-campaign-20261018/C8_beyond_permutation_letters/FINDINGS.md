# C8 findings: letters outside B26's class add no velocity source and no new taste; the E-letter screen passes nothing

Provenance: a worker of the same model family. Checked by a fresh-context same-family agent on an independent model build (`../C8_check/REPORT.md`, PASS=49 FAIL=0): no claim refuted in substance; corrections applied below. The model chain `b26lib` → `B20_check/chklib` → `B18_check/chk_model` was imported read-only, so this is not an independent build. Saved by the supervisor from the hand-back (the worker's file write was blocked).

| Runner | Result |
|---|---|
| `c8_qletters.py` (class 1: single-Q letters, doubled-cell orbits, letter enumeration, conjugates) | 14/0 |
| `c8_mixed.py` (class 1: a·R_L·b lemma, random mixed words) | 5/0 |
| `c8_class3.py` (classes 2 and 3: exact checks, taste census) | 14/0 |
| `c8_screen.py` (5 runs) | 4/0 each |
| `c8_summarise.py` | 1/0 |
| `c8_best_census.py` | 1/0 |

Total PASS=55, FAIL=0.

Earlier failing runs were the worker's own bugs: a determinant threshold, a block-ordering comparison and a mis-written identity. Their logs were overwritten. The first five screen runs wrote their pickles into `B26_new_shift_letters/` because b26lib's `HERE` shadowed the worker's. The worker moved them to this directory unchanged; no B26 file was overwritten.

**Short answer.** None of the three classes helps:
- momentum-shifting letters reduce to old words in every subclass settled exactly;
- antiunitary steps are meaningful only through U², which is an old word;
- among the π/4 exponentials examined (of A0, A_a, S^a, on-site involutions, R_L, Rt, D_Π), exp(±iπ/4·R_L) is the only new letter. It adds no velocity source and no taste outside the B24 lattices (it breaks the exact relation W(k+Π) = ±W(k)), and its screen passes 0 of 69,660 levels. exp(iθR_L) for θ ∈ (π/6)Z is a further parameter-free O-symmetric letter (check), not screened; conjugates gE₊g⁻¹ by old words are already generated.

## 1. Classification

### Class 1: momentum-shifting letters

- **Single-Q letters (exact).**
  - T_v X T_v⁻¹ = e^{iQ·v}X gives X = D_Q·Y, with D_Q = (−1)^{q·x} and Y translation-invariant.
  - Rotations send D_Q to D_{RQ} (24 rotations × 8 Q). So X can be covariant up to a character only if Q ∈ {0, Π}, with Π = π(1,1,1); the other Q's in π{0,1}³ form two 3-element orbits. (Check: this holds for every Q, since the O-fixed points of R³/2πZ³ are exactly 0 and Π.)
  - The Q = Π letters are z·D_Π·S^a and z·D_Π·A0·S^a.
  - D_Π commutes with S, A0 and on-site letters, and anticommutes with R_L and Rt. A translation-invariant word therefore has an even number of D_Π factors and is ± an old word.
  - k* + Π ≡ −k*. The D_Π relation is the known Π-taste W(k+Π) = (−1)^{n_R}W(k) of every old word (B18; B20's 2πZ³ + Π).
- **Q-multiplets.** A member with Q in a 3-orbit is only D4-covariant: there are infinitely many at every range, and an O-symmetric step needs the whole multiplet, i.e. a doubled-cell letter.
- **Doubled-cell letters (exact plus exhaustive; covers Q ∈ π{0,1}³ and monomial letters only).** These are phased permutations commuting with 2Z³ translations, O-covariant up to a 1-d character.
  - There are 6 orbits per doubled cell:
    - four with stabiliser C2′, 12 modes each: sublattice 000, sublattice 111, 100-type perpendicular corners, 110-type perpendicular corners;
    - two free orbits, 24 modes each: the 100-type and 110-type corners parallel to the D4 axis.
  - C2′ orbits go to the same or the antipodal corner, and the stabiliser sign fixes the character. Free orbits go to any free-orbit mode, at any displacement, with either character.
  - Range ≤ 1: 6 pieces per C2′ orbit and 336 per free orbit, with 0 mismatches.
  - Range 0: a group G0 of 524,288 letters (2 characters × 64 free-orbit choices × 4⁶ phases).
- **What they generate.**
  - *Pure-permutation words (exact, any range, any cell):* a translation-invariant O-covariant product is z·S^a or z·A0·S^a. Only 8 of the G0 letters are translation-invariant (z·1, z·A0).
  - *One link letter between two G0 letters (exact lemma):* R_L's two hops run along the two directions of its corner, so translation invariance of a·R_L·b forces both permutation parts to be sublattice-independent, i.e. 1 or A0. With all ℤ₄ phases solved (check: U(1) phases add only an overall scalar) there are 16 such words, all z·{R_L, Rt, A0·R_L, R_L·A0}. Every translation-invariant conjugate P·R_L·P⁻¹ is ±R_L or ±Rt.
  - *Longer mixed words (sampled):* of 20,000 random words M·g·M·g·M, 3 are translation-invariant with non-invariant G0 letters, and all 3 are old type, with k* speed |n_S|·√2/3.

### Class 2: antiunitary letters (brief)

- An antiunitary U has no quasi-energy, since eigenvalue phases can be rotated by rephasing; only U² is a sensible step.
- The rotations, S, R_L and A0 are real, and the Clifford palette is closed under conjugation up to a phase. So (V·K)² = V·V* is an old-palette word, provided V is a word of a conjugation-closed palette.
- The class adds only the pairing constraint spec U²(−k) = conj spec U²(k) (checked).

### Class 3: non-permutation letters

- (1+iX)/√2 is unitary only when X² = +1. For X² = −1 the unitary is exp(π/4·X) = (1+X)/√2.
- **A0 and the A_a do not qualify.** They are A2-odd: a rotation sends exp(θA0) to exp(χθA0), so exp(π/4·A0) is only T-covariant (the 12 even rotations).
- S^a with a ≠ 0 is not an involution.
- On-site involutions 1−2P built from H_on or Λ eigenprojectors are already in PC up to a phase. Others stay in the 6-dimensional on-site algebra, which L1 already covers.
- **New letter:** E± = exp(±iπ/4·R_L) = (1 ± iR_L)/√2. It is O-symmetric and translation-invariant, with 3 nonzeros per column, so it is not a phased permutation. It satisfies E₊E₋ = 1, E₊² = i·R_L and E₊·R_L = i·E₋.
- exp(±iπ/4·Rt) = S·E∓·S⁻¹ is nothing new.
- exp(iπ/4·D_Π) gives nothing (by hand): words are (old word) × F^m, which is translation-invariant only when F^m = ±1.

## 2. Velocity and tastes

- **Velocity (exact).** At ±k*, E±, the class-1 conjugates and the a·R_L·b words are scalars on D₊ and D₋ with zero compressed derivative. So L1 holds unchanged; on 508 D± levels from 300 random E-words the worst deviation is 7e−14.
- **Tastes.**
  - *Class 1.* D_Π is the known Π-taste. Doubled-cell symmetries of translation-invariant words give k-independent intertwiners V_Q·W(k) = ω·W(k+Q)·V_Q, which B24 and B25 cover. Displaced doubled-cell letters give k-dependent intertwiners, B25's open class.
  - *Class 3.* E obeys R_L's rules, E(k+t) = D_t·E(k)·D_t⁻¹ and E(k)ᵀ = E(−k), but E(k+Π) = E∓(k). **So E letters break the exact Π relation W(k+Π) = ±W(k)**, and −k* is no longer guaranteed to be a copy of k*. (Check: slot-free E-words keep a spectral Π-taste, 167/167, because every letter is real; words with a generic symmetric on-site slot lose it, 133/133. The census below has 37 of 120 words on Π-containing lattices.) Taste census of 120 random E-words:

    | Lattice | Words |
    |---|---|
    | sc(2π) | 83 |
    | bcc(2π) | 17 |
    | sc(π/4) | 8 |
    | bcc(π) | 7 |
    | sc(π/2) | 3 |
    | bcc(π/2) | 1 |
    | sc(π) | 1 |

    All are B24 lattices, so B24's scale-free theorem and B25's index lemma apply unchanged.

## 3. Screen (numerical negative search, not a no-go)

- **Family:** words in S^{±1}, S^{±2}, R_L, Rt and E± with at least one E and n_S ≠ 0, length ≤ 5, with one or two on-site Clifford slots. Reduced modulo cyclic rotation and complex conjugation (E₊ ↔ E₋), this leaves 348 one-slot and 84 two-slot classes.
- **Fills** (60,832 words in total):
  - one-slot classes of length ≤ 4 × all 80 PC letters (4,800);
  - length-5 one-slot classes × 40 sampled PC fills (11,520);
  - length-3 one-slot classes × the full PHL palette (8,832);
  - length-4 two-slot classes × PC² (25,600);
  - length-5 two-slot classes × 120 sampled fills (10,080).
- **Criterion:** as in B20/B23/B26.
- **Results:**

  | Quantity | Count |
  |---|---|
  | (word, level) pairs screened | 69,660 (D₊ 30,273; D₋ 30,251; D₊⊕D₋ 9,136) |
  | Fail the sign test | 69,021 |
  | Survivors | 639 (278 rejected early at a defective (π/4)Z³ node) |
  | **Pass** | **0** |

- **Sanity:** every survivor's k* node is an isotropic cone at |n_S|·√2/3.
- **Obstructions:** mostly tilted or anisotropic generic-k nodes; also anisotropic cube-point levels (474), X_π and M_π nodes (282 each) and (π/4)-type points.
- **−k* among survivors:** 8-fold defective in 180 (check: 89 have an exact linear-order flat direction and 91 are genuinely anisotropic; the worker's 43-direction s_min is an upper bound), isotropic in 79, not at E in 371.
- **Closest cases:** E₊·S·L033, E₊·Rt·S·L011, E₊·S·R·L011 and E₊·S·Rt·L011. Each has a single (π/4)Z³ defect, the 8-fold −k* level (flat for E₊·S·L033, per the check), but a full census finds 40–41 defective nodes, mostly tilted generic ones; these counts are lower bounds (the check finds 59 for E₊·S·L033).

## Status

- **Exact:**
  - the single-Q classification, the D_Π reduction and its identification with the Π-taste;
  - the doubled-cell orbits, stabilisers and letter pieces;
  - the pure-permutation reduction and the a·R_L·b lemma;
  - the class-2 reduction;
  - the exclusion of exp(π/4·A0);
  - E± as the only new letter among the π/4 exponentials examined;
  - L1 for E letters, conjugates and a·R_L·b;
  - the broken Π-taste.
- **By hand:** the F = exp(iπ/4·D_Π) reduction, and the reduction of doubled-cell symmetries to k-independent tastes.
- **Numerical:** the mixed-word sample, the taste census and the screen (negative).

## Remark (numerical, from the check; a sketched symmetry argument, not a proof)

Every O-symmetric translation-invariant letter tested (12 random group-averaged range-2 exp(iH)) is scalar on D± at k*, with compressed derivative c·(S's), c real. So no new symmetric letter can make the k* doublet anisotropic or tilted; it can only rescale the speed. The obstruction lies at the other nodes and in the tastes.

## Open

- exp(iθR_L) at other rational angles (θ ∈ (π/6)Z), not screened.
- Momentum-shift multiplets with Q outside π{0,1}³ (larger cells); non-monomial doubled-cell letters.
- Non-conjugate O-symmetric Hermitian involutions beyond those probed (search not exhaustive).
- Antiunitary steps with V outside a conjugation-closed palette; O_h letters with inversion characters.

- Mixed words with displaced (range ≥ 1) doubled-cell letters, the only class-1 route to k-dependent intertwiners.
- Longer range-0 mixed words with two or more link letters (sampled only).
- T-only steps with exp(π/4·A0), where D₊ and D₋ can mix (outside the declared class).
- E-words longer than 5, the unsampled fills, π/6 fills, and G3/2 levels.
- Exponentials of on-site involutions in the M₂ block.
