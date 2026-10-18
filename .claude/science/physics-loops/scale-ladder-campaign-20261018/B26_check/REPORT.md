# B26 check report

Provenance: a fresh-context checker of the same model family as the B26 worker, not an independent model family. The code path is new: `mymodel.py` rebuilds the corner model from its definition and imports no repository or campaign code. It has its own GF(2) flux and lift solver, builds S and A0 by orbit propagation from their covariance, and reads B26 pickles only as data, through a whitelisting unpickler (`safepk.py`). The checker's REPORT.md write was blocked; the supervisor saved this report from the hand-back.

**Verdict:** no B26 claim is refuted. Claims 1–3 hold in substance, and the screen spot check confirms every sampled failure. The corrections concern proof completeness, sign and phase bookkeeping, a norm convention, and one false coverage statement in the screen description.

**Totals:** PASS=47, FAIL=0 on the final runs.

| Runner | Result | Covers |
|---|---|---|
| `chk_classify.py` | 13/0 | classification proof, enumeration |
| `chk_identities.py` | 15/0 | identities, even-A reduction, D± swap, L1 |
| `chk_screen.py` | 7/0 | screen spot check |
| `chk_tastes.py` + `chk_tastes2.py` | 6/0 + 2/0 | letter-level tastes |
| `chk_scope.py` | 4/0 | scoping |

Run notes:
- `chk_tastes.py` hit the 30-minute background limit while the C8 screen was using all cores (`chk_tastes_part1_timeout.log`); `chk_tastes2.py` ran the remaining checks. Its "TOTAL PASS=0" line is a counter-scoping bug; both check lines read PASS.
- Two first runs failed because of checker errors:
  - `chk_identities` had a dictionary-key collision in the π/6 test; that log was overwritten.
  - `chk_scope` wrongly expected a commutative on-site algebra (`chk_scope_firstrun.log`).

## Classification

- **Stabiliser.** The stabiliser of {d,e}@0 in O is exactly {1, C2′ about d+e} for all 12 corners. Gauge dressing adds only signs.
- **Projective signs.** The dressed lifts compose up to a global sign. The defect is a u-preserving gauge transformation, hence constant; all 24² pairs were checked. So Ad(G) is a true representation and χ ∈ {A1, A2}.
- **Uniqueness.** By Frobenius reciprocity, each C2′-fixed support carries exactly one of A1 or A2. The projector ranks are (1,0) for c → c and (0,1) for c → −c.
- **"For any displacement range": justified exactly.** The restriction to {±1, ±i} is unnecessary: the argument holds for any monomial letter (argued, not tested separately).
- **Gap.** The step that assigns the character needs two model facts, both true for all 12 corners and both gauge-invariant:
  - λ_{C2′}·f_c is even, so S^t is A1 for every t;
  - τ_{C2′}(c) + τ_{C2′}(−c) is odd, with A2(C2′) = −1, so A0·S^t is A2.
- **Enumeration** (scan over displacement and target corner for the image of {x,y}@0):

  | Range | Candidates | Letters |
  |---|---|---|
  | ≤ 1 | 324 | 6 |
  | ≤ 2 | 1,500 | 10 |
  | ≤ 3 | 4,116 | 14 |
  | ≤ 4 | 8,748 | 18 |

  These are always exactly S^t and A0·S^t for |t| ≤ R.

## Identities and the even-A reduction

- **All five listed identities hold exactly** (residual ≤ 3e−16):
  - A0² = −1 (real normalisation; (iA0)² = +1);
  - A0 S A0⁻¹ = S⁻¹;
  - A0 R_L A0⁻¹ = −S R_L S⁻¹ (the alternatives fail with residual 1.41);
  - A0 H_on A0⁻¹ = H_on;
  - A0 Λ A0⁻¹ = −Λ.
- **Rt identities** (not listed in B26):
  - A0 Rt A0⁻¹ = +R_L;
  - S⁻¹ Rt S = −R_L;
  - Rt² = 1, Rt is Hermitian, and Rt ≠ ±R_L.
- **Palettes.** A0 maps the Clifford (80) and π/6 (1,872) palettes onto themselves up to scalars in {±1, ±i}. The 6-dimensional symmetric on-site algebra is M1⊕M1⊕M2(C) and is non-commutative; D₊ and D₋ are its multiplicity-1 blocks.
- **Reduction.** 300 random words with 2 or 4 A letters each equal an old-palette word (max deviation 6e−16). A_a X A_b = −S^{−a} X̃ S^b holds for a, b ∈ −2..2, and n_eff = Σ(−1)^{#A0 to the left}·p. The prefactor is z ∈ {±1, ±i} for normalised palette fills, and ±1 only if arbitrary symmetric on-site letters are allowed.

## D± swap and L1

- **D± swap confirmed:** A_a maps D₊ ↔ D₋ at both ±k*.
- **Letter values:** S is scalar 1 on D±. R_L is (−1, +1) on (D₊, D₋) at +k* and (+1, −1) at −k*; Rt has these values with D₊ and D₋ swapped. Both have zero compressed derivative, and on-site symmetric letters are scalars on D₊ and on D₋.
- **Norm:** the compressed derivative of S has spectral norm √2/3 per axis and Frobenius norm 2/3. B26's "2/3" is the Frobenius norm.
- **L1 confirmed** with the sign-flipped n_eff: 400 random words, 710 exact doublets, all untilted isotropic cones at |n_eff|·√2/3 (max deviation 5e−10). In 333 of them |n_eff| ≠ |n_raw|.

## Screen spot check

The seeded sample has 40 records from all 5 pickles.
- The k* level kind is reproduced in 40/40.
- **Fermi-surface failures: 30/30 confirmed** with a determinant-based r(k) computed independently. 26 were found on the checker's 10³ grid; 4 needed the 16³ grid.
- **Survivor failures: 10/10 confirmed** (multiplicity and defect type). The s_min values are upper bounds in both codes; the verdicts agree.
- **S·o·Rt·o (L130, L332), E = 0: confirmed failing.**
  - +k* is a 4-fold isotropic cone at √2/3.
  - −k* is 8-fold and anisotropic, with s_min = 0.235702 and s_max = 0.707107.
  - The checker found 40 further defective nodes.
- **S·Rt·o (H20·L002): confirmed** — three anisotropic 4-fold cube doublets (0.2467, 0.6236).

## Tastes (letter level)

Each letter was allowed its own ω.
- A_0, A_1 and A_2: tastes for every e at ω = ±1.
- S: only e = (1,1,1), mapping k* → −k*.
- Jointly with A_1:
  - with S: only e = (1,1,1), plus an extra (ω_S, ω_A) = (1, −1);
  - with H_on: only e = (1,1,1);
  - with R_L: every e, including (−1, 1).
- Rt: every e.
- None of the extras changes B26's conclusion.
- Even-A words are themselves symmetric steps, so B24 and B25 apply to them directly by their own hypotheses.
- The log line "any word containing S letter-wise inherits the S-theorem" overstates and should not be cited: joint letter tastes are sufficient for a word taste, not necessary.

## Scoping

- The class is natural as the monomial analogue of S, but narrow: it excludes R_L itself (a two-term sum) and every on-site letter except the identity.
- **"S is the only k-dependent letter" is inaccurate.** A0·S(k)^a is k-dependent as a Bloch matrix; only its spectrum is constant.
- **"Covers every even-A word of that length" is false.** Two exact counterexamples reduce to an S power of magnitude 3:
  - A_2·S·o₁·A_0·o₂ = −S⁻³·õ₁·o₂;
  - A_1·S²·o₁·A_1·o₂ = −S⁻³·õ₁·S·o₂.

  Also, A_0 letters can make on-site slots adjacent, and products such as L·H are not in PHL.
- **"Isospectral involution"** is exact for the conjugated word, and holds up to a global phase for palette relabelling.
- **Open items to add:**
  - O_h letters with inversion characters, or letters covariant under subgroups only;
  - non-monomial unitary letters of range ≥ 1 that combine S, A and link hops;
  - S^{±3} and S^{±4} skeletons and adjacent-slot cases at length ≤ 5.

## Corrections (applied by the supervisor to `../B26_new_shift_letters/FINDINGS.md`)

1. Sign facts in the proof.
2. Projective-sign wording.
3. A0² real normalisation.
4. Rt identities.
5. Reduction prefactor z.
6. Norm convention.
7. Screen family coverage.
8. Bottom line.
9. Tastes apply directly.
10. Open items.
