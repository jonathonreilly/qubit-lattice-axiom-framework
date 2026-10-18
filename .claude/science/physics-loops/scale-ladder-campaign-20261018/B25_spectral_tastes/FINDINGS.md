# B25 findings: steps exploiting a spectral taste lattice larger than the unitary one

Provenance: a worker of the same model family; not yet checked. Saved by the supervisor from the hand-back. The model is B24's library copied unmodified, plus new code in `b25lib.py`.

**Runners: PASS=42, FAIL=1.**
- The FAIL is genuine: one word, effectively S⁶·P, has non-dyadic spectral tastes off the (π/8)Z³ grid. All of them are unitary, so no conclusion changes.
- The worker's earlier errors were fixed and their logs kept. These were: the R_L transpose rule, the screen's early-reject order, a Fourier-check memory failure, singular intertwiners counted as intertwiners (`v1_singularV_runs/`), and a probe speed.

**Result.** No palette word realises any of the 29 good (Λ_u, Λ_sp) pairs, and the screen of the closest family finds 0 clean steps.

## 1. Tastes of transpose and antiunitary type

- **Letter rules (exact).**
  - S^n(k)^T = S^n(k).
  - R_L(k)^T = R_L(−k) = σSR_LS⁻¹σ.
  - PH^T = PH, PLm_i^T = PLm_{3−i}, and L_abc^T = i^c L_{(b−c)(a−c)(−c)} (all 64 letters checked).
  - PL(φ)^T = Y PL(φ) Y.

  So W(k)^T is a palette word.
- **Gauge table (exact).**
  - Generic letters have scalar gauges only, and they satisfy O^T = ±O.
  - Non-scalar gauges appear only for the plane letters and L202.
  - The shift Δ(m) is a scalar iff m ∈ bcc(2π), plane-constant iff m ∈ πZ³, and Y × plane-constant iff m ∈ (π/2)(1,1,1) + πZ³ (all 4,096 points checked).
- **Index lemma (exact; the lattice part is exhaustive).**
  - Tastes with a k-independent intertwiner of kind U, T, I or K form a group.
  - [Λ_ind : Λ_u] ≤ 4 (≤ 2 with U and T only), and O acts trivially on the quotient.
  - So the only admissible pairs are (Λ, Λ), (sc(a), bcc(a)) and (fcc(b), sc(b)).
  - All 74 nested pairs from 2πZ³ to (π/8)Z³ were enumerated: exactly 8 are admissible, and all 8 are bad.
  - **A good pair needs spectral tastes with no k-independent intertwiner.**
- **Census (numerical): 2,008 words.**
  - Index 1 in 1,932 words, 2 in 75, 4 in 1.
  - All index-2 cases are (sc(a), bcc(a)): 47 with a transpose intertwiner and 28 k-dependent. The k-dependent ones are all ALIGN2 words, whose mechanism is made explicit.
  - The index-4 word is decoupled into coordinate planes, with flat bands, so it is irrelevant.
  - **Good pairs: 0.** fcc never occurs.
  - *By hand, not a full proof:* letter-by-letter diagonal gauges can add only the Y-coset.
- **Fourier check.** Λ_sp is 2π times the dual of the span of the Fourier frequencies of tr W^p. It agrees with the detector on 60 of 60 grid words.
- **Pinning audit.**
  - At C2-pair points modulo both lattices: 225 of 225 classes are pinned.
  - Modulo Λ_sp only: transpose extensions give 0 of 282 pinned; k-dependent extensions give 48 of 168.

## 2. Screen of the ALIGN2 family (k-dependent tastes)

- **Family:** 2,340 words, giving 1,140 k* levels. 852 fail the sign test, leaving 288 survivors. **Clean: 0.**
- **Seeding:** nodes are first classified on (π/16)Z³, because the witness points for bcc(π/4) lie there.
- **Obstructions:**
  - 64 words: pinned 4-fold anisotropic nodes;
  - 136 words: 4-fold anisotropic nodes at C3-axis-type points;
  - 60 words: generic anisotropic doublets;
  - 28 words: Fermi crossings the grid missed.
  - No defect at any T-fixed point.
- **Closest case:** S⁴·P1·S⁴·L130·S⁴·P11·S⁴·L130 at E = 0. All its T-fixed classes are isotropic at 16√2/3, but it has 4 classes of anisotropic 4-fold nodes and at least 40 generic defects.

## Status

- **Exact:** the letter rules, the gauge and Δ classification, and the index lemma.
- **By hand:** the Y-coset limit.
- **Numerical:** the census, pinning audit, screen and Fourier check.
- **A theorem for k-independent intertwiners only;** for k-dependent tastes it is an argument plus a census.
- **Open:**
  - Fourier-cancellation tastes that no gauge realises;
  - non-dyadic k-dependent tastes;
  - tastes with nontrivial linear part;
  - higher-multiplicity levels.
