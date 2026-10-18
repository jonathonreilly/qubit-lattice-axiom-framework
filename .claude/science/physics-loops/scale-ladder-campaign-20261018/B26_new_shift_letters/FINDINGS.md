# B26 findings: no new symmetric shift letter in the declared class; the enlarged-palette screen finds no passing step

Provenance: a worker of the same model family. Checked by a fresh-context same-family agent (`../B26_check/REPORT.md`, PASS=47 FAIL=0, new model build): no claim refuted; corrections applied below. Saved by the supervisor from the hand-back (the worker's file write was blocked). Imports, read-only: `B7_check/chk_core.py` (classification) and `B20_check/chklib.py` on `B18_check/chk_model.py` (structure, tastes, screen).

| Runner | Result |
|---|---|
| `classify_letters.py` | 13/0 |
| `letter_structure.py` | 16/0 |
| `tastes_new.py` | 3/0 |
| `b26_screen.py` (5 runs) | 4/0 each |
| `summarise.py` | 1/0 |

Total PASS=53, FAIL=0. Three earlier failing runs (`*_firstrun.log`, `tastes_new_secondrun_singularV.log`) were the worker's own errors: a buggy diagonal-gauge factorisation test; a wrong expectation that S has no e = (1,1,1) taste (in fact S(k + π(1,1,1)) = S(k), consistent with B18); counting singular intertwiners (the error B25 once made).

## 1. Classification (exact: short proof plus enumeration in two builds)

**Declared class.** Translation-invariant phased permutations X of the 12 corner modes, entries in {±1, ±i}, with G_g X G_g⁻¹ = χ(g) X for the gauge-dressed rotations; χ is a 1-d character of O (trivial or A2). The dressed lifts compose up to a global sign (the defect is a u-preserving gauge transformation, hence constant), so Ad(G) is a true representation and χ ∈ {A1, A2}. The entry restriction is unnecessary: the argument holds for any monomial letter (check).

**Theorem.** For any displacement range the class is exactly
- symmetric letters z·S^a, and
- A2 "half-letters" z·A_a = z·A0·S^a, with A0 the on-site antipodal map {c}@v → {−c}@v.

**Proof sketch.** O acts transitively on corner × site; the stabiliser of {d,e}@0 is {1, C2′ about d+e}. So the image of one corner is C2′-fixed: c or −c at displacement a(d+e). Equivariance fixes the rest. The stabiliser sign gives χ through two model facts (check, all 12 corners, gauge-invariant): λ_{C2′}·f_c is even, so S^t is A1 for every t; τ_{C2′}(c) + τ_{C2′}(−c) is odd, with A2(C2′) = −1, so A0·S^t is A2. The check's independent enumeration to range ≤ 4 finds exactly S^t and A0·S^t, |t| ≤ R.

**Enumeration** (range ≤ 2; 3,000 twisted and untwisted group averages): exactly 10 letters, S^a and A_a for a = −2…2.

**Spectra and velocity.**
- S^a: k-dependent for a ≠ 0; A_a: constant spectrum ±i (6 each), A_a² = −1.
- At ±k*, S is the scalar 1 on D₊ and D₋ with compressed derivative of Frobenius norm 2/3 (spectral norm √2/3) per axis; A_a swaps D₊ ↔ D₋, so it is no velocity source; R_L and Rt are scalars with zero compressed derivative.

**No new symmetric letter is generated.** Checked in both builds: A0 S A0⁻¹ = S⁻¹, A0² = −1 (real normalisation), A0 R_L A0⁻¹ = −S R_L S⁻¹, A0 H_on A0⁻¹ = H_on, A0 Λ A0⁻¹ = −Λ; also (check) A0 Rt A0⁻¹ = +R_L and S⁻¹ Rt S = −R_L; A0 maps the Clifford and π/6 palettes and the 6-dimensional on-site algebra onto themselves (up to scalars in {±1, ±i}). So A letters enter symmetric words in pairs, A_a X A_b Y = −S^{−a} X̃ S^{b} Y (X̃ the A0-dual), and **every even-A word is z × an old-palette word**, with z ∈ {±1, ±i} for normalised palette fills (±1 if arbitrary symmetric on-site letters are allowed) (often longer or reordered, outside the B20/B23 skeletons).

- **L1 unchanged:** speed |n_S^eff|·√2/3 (sign flip between A-pairs); 474 random doublets, worst deviation 6e−13.
- **A0-duality** (S ↔ S⁻¹, R ↔ Rt, Λ → −Λ, D₊ ↔ D₋) is exact for the conjugated word; as a relabelling of palette fills it is isospectral up to a global phase.

## 2. Tastes

- Letter level (constant invertible V): A_a has tastes for every e and ω = ±1; jointly with S only e = (1,1,1) (k* → −k*, B18's S-theorem re-derived); with H_on only e = (1,1,1); with R_L every e.
- Word level: even-A words are themselves O-symmetric translation-invariant steps, so B24's lattice theorem and B25's index lemma (k-independent intertwiners) apply to them directly, with the same limits. (Check: with independent ω per letter there are extra joint tastes, (1,−1) for (S, A_1) at e = (1,1,1) and (−1,1) for (R_L, A_1); the conclusion is unchanged. The `tastes_new.py` line "any word containing S inherits the S-theorem" overstates and is not cited.) Census of 222 sampled new words: bcc(2π) 220, sc(π/2) 1, bcc(π) 1 — all B24 lattices.
- **The new letters do not evade B18, B24 or B25.** k-dependent tastes stay open.

## 3. Screen (numerical, negative search; not a no-go)

- Family: words in {S^{±1}, S^{±2}, R_L, Rt} with one or two on-site Clifford slots, length ≤ 5, reduced modulo cyclic S cancellation and A0-duality, keeping classes not among B20/B23 skeletons and with n_S ≠ 0: 74 one-slot, 40 two-slot classes (upper bounds; some are isospectral). The family contains the reductions of even-A words whose merged S powers stay in {±1, ±2} and whose slots stay separated; it does **not** cover every even-A word of length ≤ 5 (check: A_2·S·o₁·A_0·o₂ = −S⁻³·õ₁·o₂ and A_1·S²·o₁·A_1·o₂ = −S⁻³·õ₁·S·o₂; adjacent slots such as L·H are not in PHL).
- Fills: one-slot × PC (80) for all 74; one-slot × PHL (1,104) for the 22 classes of length ≤ 4; 300 sampled PHL fills per length-5 one-slot class; two-slot × PC² (6,400) for the 3 four-letter classes; 300 sampled fills for each of the other 37. About 73k words.
- Criterion (B20/B23): exact 2-fold D± or 4-fold D₊⊕D₋ level at k*; r(k) sign test on 8³ then 16³; survivors: nodes on (π/4)Z³ plus 40 Nelder–Mead starts, classified by DPT.
- **Results:** 88,998 (word, level) pairs (76,121 D±; 12,877 D₊⊕D₋); 86,599 fail the sign test; 2,399 survivors; **0 pass**. r(k) real to 4e−14. Every survivor's own k* node is an isotropic cone at |n_S|√2/3 (classifier sanity). G3/2-containing levels counted, not screened.
- Survivor search caveat: most survivors were rejected at their first defective (π/4)Z³ node; only 27 searched in full (all defective). Defect counts are lower bounds.
- Obstruction pattern: anisotropic cube-point doublets (1,713 survivors); anisotropic nodes at Γ, X_π, M_π, R_π (~1,281 each); flat or anisotropic nodes at D4 points; generic tilted or anisotropic nodes. Same pattern as B20/B23.
- Best candidates (full census of 8; none close): S·o·Rt·o with (L130, L332) — only (π/4)Z³ defect is the 8-fold anisotropic −k* level, but 61 defective nodes in full; S·Rt·o with (H20·L002) — three 4-fold uniaxial cube doublers, 36 generic anisotropic nodes.

## Status

- **Exact:** the classification theorem; the even-A reduction to old-palette words; L1 unchanged.
- **Numerical:** the screen (negative).
- **Open:** S^{±3}/S^{±4} skeletons and adjacent-slot cases that even-A words generate at length ≤ 5; O_h letters with inversion characters or letters covariant under subgroups only; non-monomial unitary letters of range ≥ 1 combining S, A and link hops; letters outside the declared class (non-permutation; covariant up to translation characters, i.e. momentum-shifting or doubled cell; antiunitary); words longer than 5 and unsampled length-5 fills; π/6 fills on these skeletons; G3/2 levels.

**Bottom line:** the S^a are the only symmetric monomial letters, and the A0·S^a (constant spectrum) are the only A2 ones. Enlarging the palette this way adds no velocity source and no new taste. A closure route has to leave this letter class.
