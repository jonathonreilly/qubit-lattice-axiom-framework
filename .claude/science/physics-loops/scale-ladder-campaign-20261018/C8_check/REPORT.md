# C8 check report

Provenance: a fresh-context checker of the same model family as the C8 worker, not an independent family. The code path is separate from C8's. It uses the B26 checker's `mymodel.py` (a from-scratch corner-model build, copied unchanged) plus new checker code, and imports nothing from C8, `b26lib`, `B20_check/chklib` or `B18_check/chk_model`. C8's pickles were read only as data, through `safepk.py`. The checker's REPORT.md write was blocked; the supervisor saved this report from the hand-back.

**Verdict.** No C8 claim is refuted in substance. Classes 1–3 hold as stated within their declared scope, and the screen spot check confirms every sampled failure. Corrections are needed in four places:
- the scope of "the only genuinely new letter";
- the Π-taste sentence;
- the label of the 8-fold −k* defect, wrong in about half the cases;
- missing open items.

**Totals: PASS = 49, FAIL = 0.**

| Runner | Result | Covers |
|---|---|---|
| `chk_class1.py` | 20/0 | single-Q, D_Π, doubled-cell orbits and pieces, G0, a·R_L·b |
| `chk_class23.py` | 19/0 | antiunitary; exponentials, E± identities, L1, Π-taste; scoping probes |
| `chk_screen.py` | 9/0 | 38 records plus closest cases |
| `chk_generic_letter.py` | 1/0 | any O-symmetric letter at k* |
| `chk_pitaste.py`, `chk_kminus.py`, `chk_kminus_all.py` | data | Π-taste survival; true minimum speed at −k* |

Checker errors on first runs:
- `chk_class1_firstrun.log`: a wrong kernel-dimension expectation; the extra directions are gauge.
- `chk_screen_firstrun.log`: rounded node momenta and missed small pockets, fixed by polishing and finer grids.
- Two crashed runs were overwritten.

## Class 1: confirmed

- **D_Q structure.** X = D_Q·Y; G_g D_Q G_g⁻¹ = D_{RQ}. Only Q ∈ {0, Π} is O-covariant up to a character, and this holds for **every** Q: the O-fixed points of R³/2πZ³ are exactly 0 and Π. The (π/8)Z³ and (π/12)Z³ grids were also scanned.
- **D_Π.** It commutes with S, A0, H_on, Λ and PC letters, and anticommutes with R_L and Rt. k* + Π ≡ −k*, and W(k+Π) = (−1)^{n_R}W(k) holds on 200 random words.
- **Doubled cell.** 6 orbits of sizes 12/12/12/12/24/24, with stabilisers C2′ ×4 (face diagonals) and free ×2.
  - Pieces at range ≤ 1: 6 per C2′ orbit and 336 per free orbit. Pieces at range 0: 1 per character on C2′ orbits and 8 per character on free orbits.
  - Built with an independent propagation algorithm.
- **G0.** 524,288 letters, exactly 8 translation-invariant (exhaustive).
- **a·R_L·b lemma.**
  - The logic is valid: each column's displacement pair fixes b's target corner, and every (sublattice, corner) is a landing site, so a is fixed too.
  - Exhaustive over 128² perm-part pairs: exactly 4 admissible.
  - With U(1) phases (Smith normal form, mod-4 enumeration), the continuous solutions only change the word by a scalar.
  - Result: exactly z·{R_L, Rt, A0R_L, R_LA0}.
  - Pure-permutation reduction: follows from B26.
- **Not rechecked:** the 20,000-word mixed sample, and the Q-multiplet paragraph.

## Class 2: confirmed

- S, R_L, Rt, A0 and every dressed rotation matrix are real, and PC is conjugation-closed up to a phase.
- (VK)² = V·V* (100 random words), spec U²(−k) = conj spec U²(k), and there is no quasi-energy for odd steps.
- **Precision:** U² is an old-palette word only when V comes from a conjugation-closed palette.

## Class 3: confirmed, with one overstatement

- **Exponentials of A0.** exp(π/4·A0) is covariant up to a phase for exactly the 12 χ = +1 rotations, so it is only T-covariant.
- **E± letters.**
  - E± is unitary, with E₊E₋ = 1, E₊² = iR_L and E₊R_L = iE₋.
  - Rt = −S R_L S⁻¹, so exp(±iπ/4·Rt) = S E∓ S⁻¹.
  - E₊ is O-symmetric (24/24) and not monomial (|entries| ∈ {1/√2, 1/2}).
  - E± are scalars on D± at ±k* with zero compressed derivative.
- **L1.** 250 random words give 220 doublets, all untilted isotropic cones at |n_S|·√2/3 (worst deviation 1.3e−9).
- **Momentum relations.** E(k+Π) = E∓(k), and E(k)ᵀ = E(−k).
- **Overstated:** "−k* is no longer a copy of k*". W(k+Π) = ±W(k) is lost, but a spectral Π-taste often survives (`chk_pitaste.log`, 300 E-words):
  - slot-free words keep it (167/167), since every letter is real;
  - words with a generic symmetric on-site slot lose it (133/133).

  C8's own census has 37 of 120 words on Π-containing lattices.

## Screen spot check: confirmed

- **Totals.** The pickles match FINDINGS: 69,660 levels, 69,021 sign-test failures, 639 survivors, 0 records without a defect.
- **Sample.** 38 seeded records:
  - k* level kind reproduced 38/38;
  - sign-test failures confirmed 28/28 by a determinant-based r(k) and bisection to an actual eigenvalue (26 on an 11³ grid, 2 needing 16³);
  - survivor failures confirmed 10/10.
- **E₊·S·L033 at E = −π/4 fails.**
  - +k* is a 4-fold isotropic cone at √2/3, and −k* is 8-fold and defective.
  - The checker's census finds 60 nodes, 59 defective (57 tilted, 1 anisotropic, plus the 8-fold one). C8's 41 is a lower bound.
  - E₊·Rt·S·L011 behaves the same way.
- **Correction (−k* label).** E₊·S·L033's −k* level has an exact linear-order flat direction (minimum speed 1.7e−14), so it is "flat" in the B20 sense. Of the 180 survivors C8 labels 8-fold "aniso" at −k*, 89 are flat and 91 anisotropic. C8 sampled 43 directions, so its s_min is an upper bound. The verdict is unchanged.

## Scoping

- **"E± is the only genuinely new parameter-free letter"** holds only within the π/4 exponentials examined (A0, A_a, S^a, on-site involutions, R_L, Rt, D_Π).
  - exp(iθR_L) for θ ∈ (π/6)Z is O-symmetric and parameter-free on the same footing as the π/6 on-site fills. It is not z·E₊ⁿ, it flips under Π, and it adds no velocity source.
  - S²R_LS⁻² and every gXg⁻¹ (g an old word) are conjugates, so gE₊g⁻¹ is already generated.
  - (R_L + Rt)/√2 is not an involution. No involution of the form R_L·P + (1−P) exists (Schur). H_link = √2·R_L. H_on + H_link needs a parameter.
  - No further non-conjugate parameter-free involution was found; the search was not exhaustive.
- **Wider observation (numerical; a sketched symmetry argument, not a proof).** Every O-symmetric translation-invariant letter tested (exp(iH) with H a random group-averaged range-2 Hermitian letter, 12 samples) is scalar on D± at k*, with compressed derivative c·(S's), c real. So no new symmetric letter can make the k* doublet anisotropic or tilted; it can only rescale the speed. The obstruction lies at the other nodes and in the tastes.
- **Open items to add:**
  - exp(iθR_L) at other rational angles;
  - multiplets with Q outside π{0,1}³ (larger cells);
  - non-monomial doubled-cell letters;
  - non-conjugate symmetric involutions beyond those probed;
  - antiunitary steps with V outside the palette;
  - O_h letters with inversion characters.

## Corrections (applied by the supervisor to `../C8_beyond_permutation_letters/FINDINGS.md`)

1. Scope of "only new letter", noting exp(iπ/6·R_L) and that conjugates are generated.
2. Π-taste wording.
3. Class 1 scope (all Q; multiplet analysis only for π{0,1}³, monomial letters and ℤ₄ phases; U(1) a·R_L·b).
4. Class 2 proviso.
5. −k* flat/aniso split and the census lower bound.
6. Open items.
7. The numerical remark on symmetric letters at k*.
