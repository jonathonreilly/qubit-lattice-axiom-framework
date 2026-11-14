# REVIEW_S3: independent hostile review of PROOF_session3_snapshot.md

Reviewer: independent agent (did not write the proof). Inputs: the session-3 snapshot (byte-identical to PROOF.md when
read), the session-2 snapshot, REVIEW_S2.md, LOG.md, checks c8-c12 (all re-run). PROOF.md and the snapshots were not edited.

**Bottom line.** All 24 PROVEN-HERE items survive as stated inequalities/identities. One *consequence* is wrong: the E7.0
falsification uses the wrong threshold. With the correct one (3τ_N/4) it holds only for N = 2, 3, 4, and the SU(2)
ratio is ≈ 6, not 14. The E8 falsification (domain D) holds for N = 2, 3 only; the "all N" statement is about a
different event (threshold τ_N/2), not E8. Both retirements are correctly labelled "conditional on L4a" in the tally.
No PROVEN-HERE argument uses an IMPORTED-NOT-YET-REVERIFIED lemma. Every [R2-fix] is applied.

## [R2-fix] audit

All applied: L1e scope and the L1d withdrawal; S5 aligned with L7.0; L8b off-D citation; L8c Π_s block; Dimock
entry; R3.1 promoted; Migdal/Kadanoff [m]; MK bump vacuous. Only "keep first runs" is partial: the first c9 run was
overwritten again (disclosed in LOG).

## (1) New PROVEN-HERE items

**S4' re-checks + axis permutations: CORRECT.** The reference S_{c_X} is order-free. A permutation π sends order-σ
paths to order-(π∘σ) paths and straight legs to straight legs. The uniform average over all d! orders is π-invariant,
and so is the cubic block grid through the origin. Hence V[πU] = πV[U]. Coordinate reflections preserve each order, so
L9a' carries over. L1e needs only the link count (d+2)L and the ribbon, both order-independent. With L8b this gives
the hyperoctahedral group. c8(d) is exact (1e-15), and the S4 control fails at 0.1.
- Fix (consistency): the document now has two off-D extensions. L8b/L8c use "failed link := 1"; S5'/E7.0' use S4''.
  Say which map defines O. If S4'' is used at every level, L8b/L8c need the branch set to be null under the *pushforward*
  laws of V^(j), not just under Haar. That is unproven.

**"Root-path extra terms are a coarse gauge transformation" (L3g(a)-slice identity): CORRECT, linearised/abelian only.**
Re-derived: ∫_{T^σ_y}A = ∫_{P^σ(c_X→y)}A + ∫_{S_y}A − ∫_{P^σ(c_Y→y+Le_μ)}A. The reference cancels at linear order.
y ↦ y + Le_μ is a bijection B(X) → B(Y), so the third term averages to h(Y). Hence Q_root = Q_str − dh. The slice
h(A+dλ) = h + Q_0λ − λ(c) is onto, as claimed (the image is s_X(1−n^-d)). Fixes:
- "Coarse gauge transformation" should read "coarse exact 1-form dh(A)". It depends on A, and there is no nonlinear
  SU(N) analogue: the nonabelian straight average is not even covariant.
- The slice gap uses Δ = d*d + dd* *on top of* δ(h). That is a double gauge fixing whose legitimacy is exactly (FP).
  "The revised L3g(a) target is met in the abelian linearised case" must read "conditional on (FP)".

**L3g(a)-glob: CORRECT.** Re-derived: flat Weitzenböck; tent ω_X with ∫ω = ε^{d+1}n^{d−1}n² = 1, sup ω = 1; slab gap
(4/ε²)sin²(π/4n) ≥ 1; ||f||²_S ≤ 4|ω(f)|² + 5||∂f||²_S; double covering (also at T = 2, where the Neumann form drops
the wrap bond). So ||A||² ≤ 5⟨A,ΔA⟩ + 2||QA||².

The constant is not tested: c9(B) always finds λ_min = a (constants), so it cannot probe the 1/5. Scope (abelian,
flat, one level) is correctly stated.

**E8.1 (chessboard): CORRECT.** Re-derived:
- Cauchy-Schwarz with |H_+| + |H_−| = 2|H| gives ρ(H) ≤ √(ρ(H_+)ρ(H_−)); run doubling (≥ 2min(ℓ, m) > ℓ) ends at ∅ or Λ.
- (ii) ≤ 4 cells per plaquette; 1 − N^-1 Re tr U ≥ ||1−U||²/(2N); denominator 6|Λ| plaquettes ≤ 8δ², 4|Λ| links.
- (iii) h_2 = (θ − sinθcosθ)/π ≥ 8θ³/(3π³).

L9a is IMPORTED-AND-REVERIFIED, which is permitted. The site-reflection sketch in L9a is thin but correct: no plaquette
crosses a site plane, and in-plane plaquettes split symmetrically. Missing attribution: this is the
Fröhlich-Israel-Lieb-Simon chessboard estimate (CMP 62 (1978) 1 [m]); cite it.

**E8.2 (volume-uniform first-step bound): CORRECT, correctly scoped.**
- The ribbon gives ||Z−1|| ≤ A_L max_p ||1−U_p||, with A_L = (d−1)L(L−1)/2 = 9. ν = μ rectangles backtrack exactly to 1.
- Union over ≤ 2L^4 cells, then E8.1(i). Disjoint regions give distinct cells, hence the Peierls power r.
- c = 1/(4A_L²) = 1/324 checks.
- It is a bound in the *bare* coupling, first step only.

**E8.3 inequality: CORRECT.**
- Second-order lemma: zero first variation, ||e^X−1−X|| ≤ ||X||²/2, |tr(MW)| ≤ N||M||·||W||, w = 2(d−1).
- Conditional lemma, both cases: in case 2, |ζ_j| < 2arcsin((t+δ)/2) < w_0. So a has the sign of ζ_1, and the second
  phase stays ≤ w_0 provided ζ_1 has the largest modulus. Say so, and take sign(0) = +1. Every U ∈ A' has
  ||e^{X'}−1|| ≤ t+3δ, and the N ≥ 3 tracelessness hypothesis is needed and stated.
- Proposition:
  - ⌊s/2⌋s³ ≥ s⁴/3 (s ≥ 3). b lies in B(X+e_1) or on the crossing bond, is off S_c, and the B(X+e_1) axial path
    approaches from c_{Y,1} ≥ y_{0,1}+L, so b occurs once. Successive conditioning is valid (bound uniform in the rest).
- t = 1 arithmetic verified: 1.222, 2.750, 4.889 (SU(2-4)). Dense failures at a fixed threshold are expected
  (Balaban's thresholds scale with p(g)g): a finding about this document's S4 domain, not about Balaban.

**E8.3 consequences: WRONG as written (fix required).**
- ζ = 0 only when some ||Z−1|| ≥ 3τ_N/4. So E[w̃] ≤ E[ζ] ≤ μ(no failure at threshold **3τ_N/4**). The snapshot's
  "threshold τ_N/2" bound goes the wrong way: {all < τ/2} ⊂ {all < 3τ/4}.
- Recomputed 3x²·4Nb_0 (δ → 0) at t = 3τ_N/4, against 4:

| N | 2 | 3 | 4 | 5 | 6 | 7 | 10 | ∞ |
|---|---|---|---|---|---|---|---|---|
| 3x²·4Nb_0 | 0.659 | 1.482 | 2.635 | 4.117 | 5.929 | 6.000 | 6.097 | 6.19 |

- So E7.0 fails in the AF window for **N = 2, 3, 4 only**; N ≥ 5 is undecided. For SU(2), λ_c/λ_AF ≈ 6.1, not 14.
- E8 with domain D: false for N = 2, 3. N = 4 is undecided; t = 1 is inadmissible in the lemma for N ≥ 6; D_N for
  N ≥ 7 is not covered.
- The "all N, τ_N/2" result falsifies only "all steps within τ_N/2", a stronger event than E8 and not what E7.0 needs.
- Correct L6loc, the L7.0 [S3] bullet, S5, the tally and c10(F) (which prints only t = 1 and τ_N/2).

**False, or false conditional on L4a?** The inequality is unconditional. The answer depends on what E8's "g" means:
- If g is a fixed bare coupling, E8 is unconditionally false (β fixed ≤ λK eventually, so sup_K μ = 1).
- If g is the running coupling along the tuned sequence, the failure needs the tuned β_K ≤ λ_cK, which is the
  imported L4a rate.

The tally's "retired as false, conditional on L4a" is right. Headings saying "FALSE along AF-rate sequences" are fine
only if "AF-rate" means the explicit rate. Also: E7.0 as stated (sup over all β) is not falsified; only its AF-window
restriction is. The text says so; keep it.

**S5' per-K: CORRECT.**
On the flat set every Z^σ = 1 at every level, so w ∘ S4'' is continuous near it and vanishes there; dominated
convergence, Laplace and IVT hold. Near-trivial content, as stated.

## (2) E7.0' and c12
- The reduction is correct but only *sufficient*: liminf w_0(K) > 0 implies a uniform w*, since sup_β E[w] could
  exceed w_0. Say "sufficient".
- **Unflagged hostile point.** Nothing shows that S5'-tuned β_K follow the AF rate. E8.3 says first-step outputs are
  garbage on a dense set at AF couplings, and S4'' then averages garbage logs. S5' may force β_K ≫ AF by the same
  mechanism as S5. "Repair" is premature; state it as open.
- c12 numbers reproduced exactly: 0.9956 ± 0.0166, 0.9932 ± 0.0081, 0.9804 ± 0.0126, 1.0348 ± 0.0188.
  - The 77.5% is consistent with exact Haar: Z is Haar unless y differs from c_X only in coordinate μ (Z = 1, 3 of 81
    sites), and P_Haar(||U−1|| ≥ 1) = 0.8045. So 78/81 × 0.8045 = 0.7747.
  - The K = 2 S4'' value rests on 2 configurations; its error bar is not credible (correlated plaquettes).
  - Two K values say nothing about the liminf (stated).

## (3) c11 spatial MK interface
- Reproduced: T3 interface 0.6666 (86 classes) vs exterior 0.0704 (only 4 classes); T3b 0.667, 0.604, 0.617, 0.603 vs
  predicted 0.738 → 0.963. The FAIL is honestly kept, and the pre-registered criterion is unchanged.
- "Falsified" is correct for the specific quantitative hypothesis.
- **Limitation not stated.** Box corners are 1/16-dyadic, so at depth ≥ 4 every node is pure. Interface nodes exist
  only at depths ≤ 3. The toy never iterates an interface contraction, so it cannot say whether a 2/3 factor compounds.
  "Vanishing fraction" here is "finitely many levels".
- **Untested alternative:** in d = 4 MK the marginal t is *averaged* over children (t_parent ≈ Σ_slots(Σ t⁻¹)⁻¹),
  not contracted. An interface Δ with a marginal component RC does not fix would give a ratio ≈ share of Δ-carrying
  children, flat in a*; 0.6666 ≈ 2/3 hints at counting. Test: project Δ on the t-direction.

## (4) Citations
No new external citations in S3. Add FILS (chessboard) [m]. Existing entries are unchanged from R2 (not re-verified
here). There are no suspicious or fabricated references.

## (5) Checks re-run
Laptop; OMP/OpenBLAS/MKL/vecLib threads = 1; nice 10; load 1.6-2.4.

| Check | Result | Time | Peak RSS | Output |
|---|---|---|---|---|
| c8 | 12/12 PASS | 1.8 s | 42 MB | identical to stored |
| c9 | 8/8 PASS | 2.9 s | 153 MB | identical |
| c10 | 5/5 PASS | 24.0 s | 189 MB | identical |
| c11 | 3 PASS / 1 FAIL (T3, as stored) | 1.1 s | 71 MB | identical |
| c12 | 1/1 PASS | 45.8 s | 80 MB | identical |

Caveats: c10(A) is non-geometric (stated); c10(D) lb/p ≤ 1.2e-4 (valid, very loose); c8(f) tests 3 links.

## Required fixes
1. E8.3 consequences: use the 3τ_N/4 threshold. E7.0 fails in the AF window for N ≤ 4 only, with SU(2) ratio ≈ 6.
   E8(D) fails for N = 2, 3 only. Drop "all N" for E8. Fix the tally and c10(F).
2. State E8's falsity by reading: unconditional for fixed bare g; conditional on L4a for the tuned sequence.
3. L3g(a)-slice: "coarse exact form", not "gauge transformation"; the target is met only conditional on (FP).
4. One off-D extension, or prove the branch set is null under the level-j laws for S4''.
5. S5': E7.0' is sufficient, not equivalent; the AF compatibility of S5' tuning is OPEN.
6. Conditional lemma: ζ_1 is the largest-modulus phase; sign(0) = +1.
7. c11: add the depth ≤ 3 interface limitation.
8. Cite FILS; keep first runs.

**Count:** 24/24 PROVEN-HERE survive (fixes 3, 4, 6 are wording/scope). The real new content is L3g(a)-glob, E8.1-E8.3.
S5' per-K and the slice gap are thin corollaries. The retired-as-false list shrinks to E8(D) for SU(2)/SU(3) and
E7.0-in-AF-window for SU(2)-SU(4), both conditional on L4a.
