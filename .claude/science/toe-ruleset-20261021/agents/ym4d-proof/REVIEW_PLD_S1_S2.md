# REVIEW_PLD_S1_S2: hostile review of lane E sessions 1-2 (PLD.md: multi-defect Peierls large deviations, returned clusters)

Reviewer: an independent agent that wrote none of PLD.md. I edited no other file. No commits, PRs or pushes.

Inputs:
- PLD.md: all 801 lines, read by offset. Line numbers below are PLD.md's as of mtime 2026-10-27 23:44 UTC.
- PLD_LOG.md (23 lines).
- checks/p1_*, p2_*: criteria, scripts, stored outputs, time records. Both scripts were re-run (Part 4).
- RLARGE.md:
  - §0-§1A (l.40-150);
  - §5 Proposition CL (l.243-304);
  - §7.2 Setting, (H-ch), Lemma 7.2-0 and R1 (i)-(iii) (l.370-409);
  - §8.1-§8.5, the inductive step (l.564-696).
- EXISTENCE.md:
  - §13.1-§13.2 (Setting S, (L), (C), X-RP^S with RX34-fix 1; l.1379-1455);
  - §13.4 (Lemma CBE, Theorem CB, (RLF-3^dis); l.1491-1546);
  - §13.6 (Lemma KN, KN-step, CB-sg, (PLD^mod_dis), (W-lc); l.1604-1693);
  - l.818-830 (W-AF);
  - §15.2 (NA-R2) by grep only.
- REVIEW_X3_X4.md: verdict table and the X-RP^S / KN items.
- REVIEW_S16_S17.md (R-3a, R-6) and REVIEW_S18_S19.md (format; G5) by offset.

Scratch work (re-run outputs, lock wrapper) is in
`/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/rerun/`.

---

## Bottom line

- **The mathematics of both sessions is essentially right.**
  - I re-derived every counted proof and found no WRONG counted item.
  - Seven items need fixes. They concern precision, a reversed inequality direction, an su(N)-valued logarithm, and the
    measure quantifier.
  - The non-counted reading claims have three overstatements:
    - the "correction" of RLARGE §8.2's sketch;
    - "for no N" in LD-arith;
    - "R1 (i) then needs no (H-ch)".
- **Proposition SHADOW is a real finding: CONFIRMED-WITH-FIX.**
  - With RLARGE §1A's clause "(H-ch) fails on Q's box", one moderately rough plaquette makes ≥ (2n_♯ + 1)⁴ cubes
    defective. Its cost is e^{-O(ε_♮)/g²}.
  - That is incompatible with (RLF-3) and (W1-ret') (c).
  - This goes beyond REVIEW_S18_S19's G5. G5 proposed a box-local (H-ch); SHADOW shows that a box-local (H-ch) as a
    *defect* criterion is already fatal, because of the box radius R_*.
  - The proposed local collar clause σ_Q is consistent, but it does not by itself restore R1 (i) for collar-bad
    configurations. See fix B4.
- **PLD-AF is the most consequential result: CONFIRMED.** Uniform (PLD-dis) implies an AF upper bound for soft block
  plaquettes, measured against the coupling sequence. The (W-F3) consequence is correctly labelled ARGUED, since it uses
  one-loop perturbation theory. It reaches further than the file says:
  - RLF itself is quantified "for every coupling sequence obeying (F)" (RLARGE l.116-117);
  - so is EXISTENCE's (RLF-3^dis) (l.1536-1538);
  - both are inconsistent with one-loop running for sequences with β_+ < β_1, for the same reason.
- **Circularity verdict (Part 5).**
  - As a torus-wide statement about the soft chain, uniform (PLD-dis)_k is not an independent node. It is the
    non-perturbative core of the UV-stability problem in probabilistic form: the running of the block coupling to depth k.
  - It does not imply UV stability (no effective action, no Z bounds), so it is not *equivalent* to the main theorem. But
    every known route to it goes through that theorem.
  - Inside RLARGE's induction it is legitimate only as an **output of (I_k) + (SF)_k**, not as a separately proven input.
  - The chessboard/SPLIT machinery cannot produce that output, because the per-history measure is not reflection
    symmetric. Lemma HS can, because it is measure-agnostic.
- **Checks p1, p2.**
  - Criteria predate scripts (mtimes); both re-ran byte-identically under the numeric lock.
  - **Process GAP:** PLD_LOG's session-2 time line is not credible.
    - The derivations are logged as written "23:42-00:10 UTC". But PLD.md's mtime is 23:44 UTC, and this review began at
      23:46 UTC.
    - p2_criteria.md (mtime 23:38 UTC) already encodes session-2 results (w_P = L^{-4}m(z_μ)m(z_ν), Σw² = 361/729, PLD-AF
      (ii)'s closed form). That contradicts the header at PLD.md l.560, "written after … checks/p2_criteria.md".
    - The checks test only identities and arithmetic, so no conclusion changes. The disclosure must be corrected.

---

# PART 1: session 1

## §2, measures (M1)-(M4) and (PLD-F1) (l.77-96): CONFIRMED

- The four measures are correctly separated.
- RLARGE §8.2 does state (PLD) for the per-history law (M3) (RLARGE l.599). RLF-step steps 4 and 6 consume it there.
- Chessboard needs a reflection-invariant torus-wide functional. Neither a history 𝔥 nor a fixed V is reflection
  symmetric, and P(E | 𝔥) ≤ P(E)/P(𝔥) loses a factor exponential in |𝔥|.
- The identity P_cut,k = ω_G/P_K(G_k) with 1/P_K(G_k) = ⟨Ξ⟩_cut is exact, given CL (a), which needs (H-pos) at effective
  levels. The file says so.
- **Provenance fix (P-1).** l.19-20 and l.99-100 call X-RP^S, Lemma CBE, Lemma KN and KN-step "not yet independently
  reviewed", citing REVIEW_X1_X2. REVIEW_X3_X4 (18:43 UTC) reviewed all of them:
  - X-RP^S CONFIRMED-WITH-FIX (RX34-fix 1, the continuum-support class);
  - KN CONFIRMED-WITH-FIX;
  - CBE, CB and KN-step CONFIRMED.
  Cite REVIEW_X3_X4, and state that CB-m's 𝔅_t lies in the corrected class (next item).

## Lemma CB-m with Corollaries CB-m.1, CB-m.2 (l.98-145): CONFIRMED

**Is the needed RP available for the soft chain over the planes used? Yes, for every grid actually used.**
- **(G-a), level j.** The planes between 2-boxes of level-j sites lie midway between adjacent level-j sites. They are
  planes of P_{K-j} and fine-link mid-planes (L odd).
  - 𝔅_t uses levels ≤ j only, i.e. resolutions ≥ K - j. Reflections in P_{K-j} preserve the class hierarchy at those
    resolutions (EXISTENCE l.1518-1520), so no class change occurs.
  - The ancestors of a level-i link (i ≤ j) with endpoint sites in t have continuum supports nested in t.
  - This is exactly RX34-fix 1's corrected class. The session-4 counterexample needs a variable *coarser* than the
    plane's resolution, and CB-m excludes those by its Remark (l.122-123).
- **(G-b).** Planes lie between level-k cubes (P_{K-k-1}), and the variables are of levels ≤ k + 1, as before.
- **ω_G.** The step 1_{G_k} = θ(χ_+)χ_+ is right: every cube lies on one side, θ maps interior plaquettes to interior
  plaquettes, and ||1 - W|| is inversion- and conjugation-invariant. So ω_G(θ(F)^*F) = E[θ(Fχ_+)^*(Fχ_+)] ≥ 0. CBE is
  homogeneous of degree 1 in ω.
- **Upstream remark (not PLD's error).** X-RP^S's class reads "closed union … in the OPEN half-space" (EXISTENCE
  l.1410-1411). Taken literally, this excludes every variable whose sites are adjacent to the plane, because their closed
  cells touch it. That includes Theorem CB's own interior plaquettes. The proof only needs all descendant sites strictly
  on one side. Owner: EXISTENCE.
- **CB-m.1.**
  - The parity identity 2c - a - 1 ≡ a (mod 2) for 2c odd is right for every box side b, so all 𝒢'-copies sit in boxes of
    the same 2-grid o'.
  - The proof does not need the 𝒢'-copies to be 2-grid copies of q; it uses Θ_j as a max over the 24 patterns. Correct.
  - "n_j/b even" is not used.
- **CB-m.2.** The 16-class Hölder argument is right; at most one plaquette per 2-box follows from the disjoint
  1-neighbourhoods.

## Proposition PLD-0 (l.147-162): CONFIRMED

- (B): s = ||1 - U||²_HS/(2N) ≥ ||1 - U||²_op/(2N), so Z[E] ≤ e^{-n_Bτ²/(2Ng²)}.
- Caps ||U_b - 1|| ≤ g give ||1 - U_p|| ≤ 4g, s ≤ op²/2 ≤ 8g², hence S/g² ≤ 8 per plaquette.
- Per 2-box: 16 sites, 64 links, 96 plaquettes. This gives exactly C_0 = e^{768}c_N^{-64} and p_0 = 64(N² - 1). Needs
  g_0 ≤ 1 (Haar ball δ ≤ 1); stated.
- The prefactor is in g_0, i.e. the bare coupling.
- The exponent τ²/(2Ng_0²) is a lower bound only. (B) is **not** attained in SU(N) at finite N. For SU(2), s = op²/2, twice
  (B). In general the minimal s at given op norm is ≈ τ²/(2(N - 1)). This matters in LD-arith (S2 item 5).

## Proposition PLD-step and Corollary PLD-fin (l.166-194): CONFIRMED-WITH-FIX

- KN-step conditional form: the window t ≤ t_N = 1.5/√N is inside both conditions.
  - 117²/(106·81) = 1.594;
  - 351/(36π) = 3.10.
- c_1 = 1/117.
- n_U = 24L⁴ bounds the plaquettes of the 2L × 2L × L × L region.
- Conditional independence given U_{k-1}, the subset expansion, and CB-m on the same grid at level k - 1 (planes between
  level-k sites ∈ P_{K-k}) are correct.
- CB-m.1 applies, since the side is 2L ≥ 2 level-(k-1) sites.
- The iterate and the bound a_k = c_1^{2k}min{κ/(256Nc_1²), 1/(2N)} are right; κ/(256c_1²) ≥ ½ iff κ ≥ 0.0094.
- **Fix (F-1).** The (PLD-i)_k constant C = ((k + 1)n_U^kB_0)^{1/16} contains g_0^{-p_0/16} and (κ/g_0²)^{(N²-1)/16}. T1
  (l.43-45) asks for a constant C, so the polynomial loss must be stated or absorbed. Under (F) at fixed k,
  g_0^{-p} ≤ C(k)g_k^{-p}, and g^{-p}e^{-a/g²} ≤ C'e^{-a'/g²} for a' < a. Say this.
- **Fix (F-2), §5.3 (l.197-199).** To show that the m-th term does *not* decay, one needs a lower bound on the term, i.e.
  (F)'s upper half (β_+), as LD-arith (i) correctly uses. l.198-199 writes β_-.

## §5.3 route obstructions and "𝒩 costs no volume factor" (l.196-222): CONFIRMED (route obstructions, uncounted)

- **(F3) identity.** Multiplying by e^{(κ/g²)(1 - σ)} is exact.
  - 𝒩̃ ≤ 1 because σ(M) ≥ N^{-1}Re tr(V^{-1}M) by definition.
  - 𝒩̃ ≥ e^{-1}c_N(g²/κ)^{N²-1} from a Haar ball of radius g²/κ around the maximiser, using ||M̄|| ≤ 1.
  - So the shrinkage 1 - σ(M̄) cancels, and a modified M̄ moves 1/𝒩̃ by at most a polynomial factor per affected link.
- **Precision (F-3).** This is a statement about 𝒩 only. In a Peierls map the kernel *numerator* still changes by
  e^{O(κ/g²)·mismatch} per link. The text says "no 1/g² per link" (l.212); add "from 𝒩".
- The fine-entropy obstruction (l.204-211) is a correct route obstruction. Correctly not called a no-go.

## Lemma HS and Proposition PLD-red, with §9.5 (l.233-278, 443-453): CONFIRMED-WITH-FIX

- **Lemma HS: arithmetic re-derived.**
  - e^{λ|F|²} = E_ξe^{√(2λ)⟨ξ,F⟩}.
  - At λ = 1/(4σ_*²g²) the exponent is |ξ|²/4 + c|ξ|_1 with c = m_*/(√2σ_*).
  - The one-coordinate integral is ≤ 2√2e^{c²} (p1 D: 0.5 at c = 0, sharp as c grows).
- **Fix (F-4), su(N) logarithm.** F_p is defined (l.236) as a log "with eigenvalues in (-π, π]". For SU(N) that log is in
  u(N), not su(N): at -1 ∈ SU(2) and at central elements of SU(N) its trace is 2πi·m ≠ 0. The pairing with
  s_p ∈ su(N) then sees only the traceless part, and Lemma HS bounds only that part. Then "||1 - U|| ≤ |F|" fails, e.g.
  at U = ω·1 the traceless part is 0.
  - **Fix.** Take F_p to be any measurable su(N)-valued X with e^X = U_p. One exists: choose angles with sum 0. Then
    ||1 - U||_op ≤ ||1 - U||_HS ≤ |X|_HS still holds, since |1 - e^{iθ}| ≤ |θ| for real θ.
  - On G_k, for cube-interior p, the principal log is already traceless, so ω_G statements are unaffected. (SG)^full on
    P_K is affected.
- **Fix (F-5).** "(SG)_k ⇒ (PLD-dis)_k" (l.259, l.311, l.473) needs (SG)_k for the ω_G half **and** (SG)_k^full for the
  P_K 2-grid half. State both.
- **PLD-red (ii) (l.253-271).**
  - Greedy factor 7⁴; |C(Q)| = 8; n_R = 6(3L)⁴.
  - The threshold algebra: η_♭ = 3ε_loc/47.2; (π/3)A_dη_♭ = 0.6ε_loc ≤ ¼; 1.14δ ≤ 1.2A_dη.
  - KN's condition ε_loc/4 ≥ 12√Nδ²: uses ε_loc ≤ 1/(36√N), from n_P = 6·4L³(L - 1) = 1296.
  - Chosen plaquettes in N_1(Q)'s at cube distance ≥ 4 have disjoint 1-neighbourhoods.
  - All of the above is correct.
- **§9.5.** η_♭' = ε_loc/43.2 ≤ η_♭; (π/3)A_dη_♭' = 0.218ε_loc; 1.2A_dη_♭' = ε_loc/4; 12√N(0.218ε_loc)² = 0.57√Nε_loc² ≤ ε_loc/4.
  Correct.
- **Measure.** Every PLD-red statement is torus-wide, on P_K or ω_G. By (PLD-F1) none of them is the per-history (M3)
  form that RLF-step consumes. The file says so (l.451-453, §12 item 2). Keep that sentence next to every use.
- **Remark (1) (l.272-274), "correction to RLARGE §8.2's sketch": OVERSTATED (narrow it).**
  - RLARGE l.603-604 says the multi-point form "needs (DF3') for general linear functionals with ℓ¹ control … and a union
    bound over disjoint supports".
  - Read with its first half, this is the joint-exponential-moment route: (DF3') for Σ_p⟨s_p, F_p⟩ plus a union bound
    over a net of directions s, at a cost of C^{|A|}. It does give a product bound.
  - That is the same route as (SG) + Lemma HS, with a net in place of Gaussian averaging.
  - **Keep:** "a family of one-point bounds (LD) does not imply it".
  - **Replace:** "cannot give the product bound" by "the phrase 'union bound over disjoint supports' is ambiguous; the
    product bound comes from the joint exponential moment, not from the union bound".

## Proposition PLD-lin (l.280-312): CONFIRMED (model statement)

- (1) Q_root = Q_str - d∘h, so d∘Q_root^m = d∘Q_str^m. p1 B: 5e-15.
- (2) Schur: row sums L, column sums L^{-3}, so ||Q_str||² ≤ L^{-2}, attained on constants (p1 A). ||d||² ≤ 16 (p1: 16
  attained at T = 2).
- (3) The Wilson part has norm ≤ 1 on im d, by Lemma 2.2 (A1).
- (4)-(5) Independent sum; det(1 - 2λΣ_A)^{-1/2} ≤ 2^{|A|/2} at λ = 1/(4σ²).
- 16/(1 - 1/9) = 18.
- With γ_0² = Ng_0² and s_i² = Ng_i²/κ (HS-orthonormal components of the RLARGE normalisation), the exponent is
  τ²/(4N(1 + 18/κ)g_k²), uniform in k, the volume and the cutoff. **Confirmed.**
- p1 C shows the noise covariance saturating geometrically: 16, 16.724, 16.792.
- Reading (a), "EXISTENCE §13.6's log divergence is an artefact of tracking curvature alone", is right for the model.
- Reading (c) is correctly hedged: it is the target, not SU(N).

## Proposition SHADOW (l.350-377): CONFIRMED-WITH-FIX

- **Re-derivation.**
  - T: U_k(b) ↦ U_k(b)R is Haar-preserving.
  - For level-k events only the marginal (U_0..U_k) matters, and U_k(b) (k ≥ 1) enters only k_b(·, M̄_b(U_{k-1})). 𝒩(M̄_b)
    is unchanged.
  - The exponent shift is ≤ (κ/g_{k-1}²)·3ε_♮, by |N^{-1}tr(AB)| ≤ ||A||_op||B||_op.
  - On F^c ∩ G_k: p becomes > 2ε_♮, and every plaquette through b stays ≤ 4ε_♮ < ε_1, so T(F^c ∩ G_k) ⊂ F ∩ G_k.
  - Hence P_cut(F) ≥ ¼e^{-3κε_♮/g_{k-1}²}.
- (H-ch) (RLARGE l.374) is ε_2 + ε_V ≤ ε_♮ on B̂_*(x). ε_2 dominates max||log U_p||_op (Lemma 7.2-0's proof), so F makes
  (H-ch) fail on every box within R_* of p.
- Cubes within cube distance n_c of Q_0 qualify, since nL + L + 2 ≤ (n_c + 2)L for L ≥ 3. That gives ≥ (2n_c + 1)⁴
  collar-bad, *-connected cubes. **Correct.**
- **Fix (F-6), direction of the coupling comparison (l.356).**
  - "… once g_k is small (g_{k-1} ≤ g_k)" has the inequality the wrong way. g_{k-1} ≤ g_k makes e^{-3κε_♮/g_{k-1}²} *smaller*
    than e^{-3κε_♮/g_k²}, i.e. it weakens the lower bound.
  - The comparison needs (F)'s upper half: 1/g_{k-1}² ≤ 1/g_k² + β_+ log L.
  - The contradiction then reads (2n_c + 1)⁴a > 3κε_♮, plus constants. This holds with enormous room, since n_c ~ 10¹³ and
    ε_♮ ≤ ε_loc/3 < 0.007.
- **Fix (F-7), the bridge.** State explicitly why the RLF-3 / (W1-ret') (c) weights dominate the cut-law probability. In
  the (I_k) representation, the probability of a history containing 𝒟 is (Σ of its weights)/Z with nonnegative weights.
  This is the reading used by (P1) and by EXISTENCE's (RLF-3^dis). One sentence; it is what "that dominates its cut-law
  probability" (l.355) assumes.
- **Relation to REVIEW_S18_S19 G5.**
  - G5 proposed "R1 with local (H-ch) on the boxes B̂_*(x) of the supports used".
  - SHADOW shows that this box-local (H-ch) must **not** be used as a defect criterion. The box radius R_* ~ n_♯L makes one
    rough plaquette cost ~(2n_♯)⁴ defects.
  - So G5 is to be closed by PLD's local clause σ_Q, not by a box-local (H-ch).
- **The fix (l.369-377).**
  - (i) is consistent in the ⟨Ξ⟩_cut representation, where the sample is all-cut. Its own interior links are a legitimate
    completion U°, so σ_Q ≡ 1 on Y gives ε_♭(U; Y) ≤ ε_loc. Correct.
  - (ii) (extraction after the sea average) is the right repair of REVIEW_S16_S17 R-6.
  - **But "R1 (i) then needs no (H-ch)" is overstated: GAP (B4).**
    - R1 (i)'s convergent gas and the pointwise 𝒢_x of §9.0 need CL (c) for every cluster in the gas.
    - Under the fix, CL (c) holds only for clusters with σ ≡ 1 on Y.
    - Collar-bad configurations with n ≤ n_♯ (which are returned) have no CL (c) bound. So the pointwise expansion of §9.0
      does not cover them.
    - **Fix.** Define 𝒢_x from the σ-restricted gas (R1 (i) with σ in place of (H-ch): Lemma 7.2-0 verbatim). Put the
      collar-bad returned configurations into (SC)_k explicitly, as an additional activity family with its own bound.
- The "primary-defect circularity" remark (l.375-377) is ARGUED and uncounted. Fine.

## Lemmas W1R-sym + W1R-tay (l.379-421): CONFIRMED-WITH-FIX

- **W1R-sym.**
  - Change of variables U = R·U' in numerator and denominator of ⟨·⟩_{R·V}, with S_k, 1_{G_k} and K_k covariant.
  - The sum over S ∋ x is permuted because R fixes c_x.
  - Gauge: extend g from the roots. **Correct.**
  - The anisotropic-torus caveat (l.391-393 and §12 item 4) is right. Λ²R⁴ splits into electric and magnetic triplets
    under the time-preserving subgroup, so there are two shifts. Binding for RLARGE/EXISTENCE.
- **W1R-tay.**
  - A direct application of GT-lat' (RLARGE §4, confirmed by REVIEW_S16_S17) with C = ∅, plus the R4D-iso quadratic
    identification. Correct, given its hypotheses.
  - **Fix (F-8).**
    - Locality in a box B̂ is a *hypothesis* ("suppose", l.396). ⟨·⟩_V is a torus-wide measure, so A_x(V) is not local in
      general. Locality is supplied only by (SC1) in Proposition W1R. Say so at the lemma's head.
    - Cite the GT-lat' (ii) clause used for the site-centred B_4 at level k + 1 (orbit-average form).
    - Typo: "(δβ^{(x)}/1)" (l.399).
- **"Honest order" paragraph (l.413-421) and the naming of (SF-irr): CONFIRMED.** This is the correct, unflattering
  reading of R-6.
- **Proposition W1R is CONDITIONAL and correctly not counted.** (SC)_k is close in strength to (W1-ret') (a)-(b)
  themselves. What is proven is the bookkeeping: symmetry survival and extraction at V = 1. Say this in §11.

---

# PART 2: session 2

## Proposition PLD-AF (l.566-594): CONFIRMED (the (W-F3) reading is ARGUED, correctly labelled)

- (i): CB-m with one non-trivial f; Θ(1) = 1 for P_K.
- (ii): E X² = ∫2tP(X ≥ t); split at τ_0² = (g²/a)log₊B; s ≤ op²/2. All correct. p2 E: closed form ≥ numerical in all 18
  cases.
- (W-F1) is a genuine necessary condition: uniform (PLD-dis) ⇒ E s(U_k(P)) ≤ Cg_k²log(1/g_k).
- **β_1 normalisation independently re-checked.**
  - RLARGE's (1/g²)Σ(1 - N^{-1}Re tr U) is the standard β = 2N/g_std² with g² = g_std²/(2N).
  - 1/g_std² runs at 2b_0 per log, so 1/g² runs at 4Nb_0 = 11N²/(12π²). That is 0.3715 for SU(2) and 0.8359 for SU(3).
  - Correct.
  - p1 F used b_0 = 11N/(48π²) as "β" (cosmetic inconsistency, informational only).
- **Extension the file misses (binding, B6).** The same argument applies to RLF itself. RLF's "for every coupling sequence
  … obeying (F)" (RLARGE l.116-117) and EXISTENCE's (RLF-3^dis) "independent … of the coupling sequence (within (F))"
  (l.1536-1538) are both false, given one-loop, for sequences with β_+ < β_1:
  - the level-k field is then at strong coupling;
  - bad cubes have probability O(1), not e^{-a/g_k²}.
  - The quantifier must be "the chain's own effective sequence (node A5), or (F) with β_- ≥ β_1 - o(1)". This holds for
    every consumer of (F), not only for (PLD-dis).
  - Note that the kernel couplings enter the chain's own running through the noise O(g_i²/κ). "The chain's own sequence"
    is therefore a fixed-point condition: node A5's content.

## Lemma CONE and Theorem SPLIT (l.596-626): CONFIRMED

- **CONE.**
  - The kernels of cone(u) links depend only on cone(u) links or on U_0|_{R_u}, by (L) and nesting.
  - Integrating out the non-cone links top-down is legitimate: no remaining factor depends on them.
  - The covariance p_{θu}(θU_0) = p_u(U_0) holds for planes between level-k sites, since the class hierarchy at levels
    ≤ k is preserved.
- **SPLIT.**
  - (ii) Π_up_u ≥ e^{-λ|𝒢|}Π1_{D_u}.
  - (i) p_u ≤ e^{-λ} + 1_{D_u}, then the subset expansion and the Wilson chessboard on the fine boxes R_u. Their
    boundaries are fine-link mid-planes, 2L^{M+K-k} (even) per direction, and X-LRP applies.
  - The converse constant 1 + C_Wg^{-p_W} is right.
- **Reading.**
  - This is an exact reformulation. Its value: the soft-chain RP (X-RP^S) is never needed, only Wilson RP plus
    conditional independence.
  - It does not make (PLD-dis) easier: the events D_u carry the whole kernel chain inside their definition.
  - Remark (2): with an aligned super-block grid no cube is dropped. Fine.

## Proposition NH-WH (l.628-658): CONFIRMED

- (a): p_u ≤ ε + 1{φ_u ≥ τ/2}, then CBE.
- (b): φ_u ≤ τ/4 + 2P(X_u ≥ τ/4 | U_0), so {φ_u ≥ τ/2} ⊂ {p_u(τ/4) ≥ τ/8}.
  - Cosmetic: D_u is defined with a strict ">". Use log(16/τ), or define D_u with ≥.
  - SPLIT (ii); the τ < g case is trivial since RHS ≥ 1. The constants are right.
- "Given (NH), (PLD-dis) ⟺ (WH)" is a correct two-sided statement. (b) needs no (NH).
- **Linear model.**
  - (NH): Jensen gives φ_u ≥ |G|, so X_u - φ_u ≤ |η|, and a_N = κ/(288N) from σ_η² ≤ 18Ng_k²/κ.
  - (WH) holds with the enlarged C_W.
  - Correct.
- (NH-i)-(NH-iii) are ARGUED. The identification (NH-iii) ≈ (NA-R2) is plausible and correctly uncounted.

## Proposition ROUGH (l.660-675): CONFIRMED

- 6 plaquettes, each shifted by ≤ 2ε/g_0², give P ≥ ½e^{-12ε/g_0²}.
- 6L^{4k} plaquettes per block.
- (F) upper half gives L^{(4-12εβ_+)k}.
- Thresholds 1/(3β_1): 0.897 (SU(2)), 0.399 (SU(3)).
- Correct, and expected: this is why multiscale large-field regions are needed at every scale (Balaban). It is a valid
  obstruction to a conditioning route for (NH), nothing more.

## Lemma LC with Propositions LD-arith and GR (l.678-736): CONFIRMED-WITH-FIX

- **LC.**
  - Stokes on the L × L squares.
  - m(t) = min(t + 1, 2L - 1 - t) ≤ L automatically.
  - Σm = L², Σm² = L(2L² + 1)/3, so ||w||² = (2L² + 1)²/(9L⁴) = 361/729. p2 A: 1.3e-15.
  - The min-cost identity τ²/||Πw||² is right.
  - The reading "the c_1² loss is the max-norm transfer, not the measure" is correct.
  - p2 B's finite-torus values grow with T (0.1435 → 0.1812), so the "7.0τ², 5.5τ²" costs are torus artefacts. Only the
    bound 2.02τ² is a statement.
- **GR.** Π(1 + cg_j²) ≤ exp(cΣg_j²) with the integral bound; v_k ≤ Ag_k²(g_k²/g_0²)^{θ-1}. Correct (p2 C).
- **LD-arith fixes (F-9).**
  - **"α ≤ 1/(2N) (inequality (B) is attained)" (l.686): wrong justification.** (B) is not attained in SU(N) (det = 1
    forces ≥ 2 eigenvalues to move). The sharp bare exponent is ≈ 1/(2(N - 1)), and 1/N for SU(2).
    - With α = 1/(2(N - 1)), the c = 1 recursion is summable at t = 2 iff 0.1857N²/(N - 1) > 6.893, i.e. N ≥ 37, not 38.
    - Immaterial physically; correct the sentence.
  - **"at the thresholds actually used … for no N" (l.688-689): WRONG as written.** At t = ε_1/4 ≤ ½,
    αt²β_1 ≤ 11N/(96π²) = 0.0116N. That exceeds 6.893 for N ≳ 594, and at t = η_1 = c_1ε_1 for N ≳ 5·10⁵.
    - **Fix:** "for no N ≤ 593 (resp. ~5·10⁵)", or "not uniformly in N".
    - The route-(a) conclusion for SU(2), SU(3) stands.
  - **Precedent (counting).** RLARGE §8.4 does not count its arithmetic items (P1)-(P5). LD-arith and GR are of that type.
    Recommendation: the counted item is **Lemma LC**; LD-arith and GR are recorded as arithmetic (CONFIRMED,
    uncounted). This does not change the count, which was one item.

## §14.6 (route (c), location of the wall; l.738-752): ARGUED, accepted; see Part 5

---

# PART 3: overclaims and process

1. RLARGE §8.2 "correction" (l.272-274): overstated; narrow it (above).
2. "R1 (i) then needs no (H-ch)" (l.372, l.434): overstated; GAP B4.
3. LD-arith "for no N" (l.688-689): wrong as literal.
4. PLD_LOG l.22-23 and PLD.md l.560: the session-2 ordering claim is not supported.
   - The criteria already encode derived results.
   - "00:10 UTC" lies after the file's mtime (23:44 UTC) and after the start of this review.
   - Replace with the true order: derivation sketch → criteria → script → write-up. Give real timestamps.
   - Session 1 is consistent: T3 (l.71-72) pre-registers criteria *after* T1's derivations, and the mtimes agree
     (criteria 23:17:22 < script 23:18:28 < run 23:18:35 UTC).
5. Cross-lane timestamp inconsistency (not PLD's to fix). EXISTENCE §15.0 (l.1983) says that at 23:21 UTC PLD.md had
   "targets only, no derivations yet". But p1 ran at 23:18 UTC on §7's content. One of the two logs is wrong; it is
   probably EXISTENCE's read time.
6. Inputs called "unreviewed" that were reviewed (P-1).

# PART 4: checks (re-run)

Run discipline:
- Numeric lock acquired by the mandated `until mkdir … numeric` loop and released by trap. Another agent took it
  afterwards at 23:56:25 UTC.
- Run started 23:55:44 UTC; load 3.01; 41% memory free.
- nice 10; OPENBLAS/OMP/MKL/VECLIB threads 1; no `timeout`.
- Outputs to scratchpad `rerun/`; the stored outputs were not touched.

| Check | Criteria before script (mtime) | Re-run vs stored output (SUMMARY line excluded) | Resources | Verdict |
|---|---|---|---|---|
| p1 (G, A-E; F informational) | 23:17:22 < 23:18:28 UTC | byte-identical; all PASS | 2.71 s, 96 MiB | PASS as reported |
| p2 (A-E) | 23:38:33 < 23:39:31 UTC | byte-identical; all PASS | 0.56 s, 76 MiB | PASS as reported; D's informational slip correctly disclosed |

- Discrimination.
  - p1 A, B, C and p2 A test the exact linear identities, and they discriminate: they would fail on a wrong operator.
  - p1 D and E, and p2 C, D and E, are arithmetic.
  - No check touches SU(N), CB-m, CONE, SPLIT, ROUGH or SHADOW. Both files say so.
- p2 D's PASS condition (n_* = 382, 255) checks consistency with RLARGE's own number, not the normalisation. The
  normalisation is confirmed independently above.

# PART 5: strategic verdict — is the lane now circular with the full RG?

**Bluntly: as a torus-wide statement, uniform (PLD-dis) is a restatement of the core of the main problem, not an
independent node.**

1. **What PLD-AF + NH-WH prove.**
   - Uniform (PLD-dis)_k ⇒ (WH)_k ⇒ E s(U_k(P)) ≤ Cg_k²log(1/g_k) for every k.
   - (WH)_k is a Gaussian large-deviation bound, uniform in depth, for noise-smoothed block plaquettes of the *Wilson
     measure* at scale L^k, at the coupling g_k.
   - With one-loop (ARGUED), it is consistent only if g_k tracks the true running to within a summable relative error
     (GR).
   - So it contains the non-perturbative AF upper bound with the correct running: the content of node A5 (W-AF1/W-AF2 in
     EXISTENCE's language), which is the UV-stability theorem's main output.
2. **Not equivalent, but downstream.**
   - (WH) for all k does not give effective actions, polymer representations or the Z-bounds of RLF-4/L6. So it is
     strictly weaker than UV stability.
   - But no route to it is known except through the multiscale small-field/large-field control: Balaban's machinery, here
     (SF) + RLF.
   - Route (c) relocates it to node A (l.739-744).
   - Routes (a) and (b) fail with explicit losses (LD-arith, ROUGH, GR).
   - So (PLD-dis), as a torus-wide input, is a *consequence* of the theorem RLF-step is meant to prove.
3. **Implication for RLARGE's inductive step (§8.3).**
   - RLF-step lists (PLD)_k as an independent hypothesis next to (SF)_k. As a separately proven statement (torus-wide,
     uniform), that is circular in effect: proving it requires the induction's conclusion at levels < k.
   - It is legitimate only as an **inductive output**: (I_k) + (SF)_k ⇒ (PLD)_k on Λ(𝔥), for the per-history measure (M3).
   - That route cannot use CB-m/SPLIT ((PLD-F1)). It can use **Lemma HS**, which is measure-agnostic: (SG)_k on Λ(𝔥) is
     an exponential-moment bound for linear functionals of curvature. It is exactly what (SF)'s Gaussian domination
     ((DF3') for general linear functionals with ℓ¹ control) should deliver, which is RLARGE's own sketch.
4. **Architecture recommendation.**
   - (a) **Retire (PLD)_k as a separate hypothesis of RLF-step.**
     - Add to (I_k) (or to (SF)_k's output) the clause "(SG)_k holds for the per-history all-cut measure on Λ(𝔥), with
       σ_*, m_* uniform".
     - Derive (PLD)_k (i)-(ii) in-step from it by Lemma HS + the KN/RS steps of PLD-red (ii). These steps do not need RP
       once CB-m.2 is replaced by Lemma HS.
   - (b) **Keep the torus-wide chessboard results (CB-m, PLD-0, PLD-fin, SPLIT, NH-WH) for the existence lane only.**
     There, CB-sg's (PLD^mod_dis) is torus-wide on ω_G. Record that (PLD^mod_dis) uniform is downstream of A5 (PLD-AF),
     not an independent wall.
   - (c) **Requantify (F)** everywhere (B6).
   - (d) **Adopt SHADOW's fix** (σ_Q; extraction after the sea average) **with B4.**
   - (e) **Do not open a lane on (WH) or (NH-iii) as stand-alone targets.** (WH) is A5 in disguise; (NH-iii) is (NA-R2)
     and should be tracked as one item, per §14.9 item 2.
   - (f) **The next useful PLD-type target** is the inductive implication "(SF)_k (DF3' general linear functionals,
     ℓ¹ control) ⇒ (SG)_k on Λ(𝔥)". It is session-scale given (SF), and it is the only form RLF-step can consume.

# Verdict counts and tally

| Item (counted by the author) | Verdict |
|---|---|
| S1: Lemma CB-m (+ CB-m.1, CB-m.2) | CONFIRMED (P-1 provenance) |
| S1: Proposition PLD-0 | CONFIRMED |
| S1: Proposition PLD-step + Corollary PLD-fin | CONFIRMED-WITH-FIX (F-1, F-2) |
| S1: Lemma HS + Proposition PLD-red (+ §9.5) | CONFIRMED-WITH-FIX (F-4 su(N) log, F-5) |
| S1: Proposition PLD-lin (model) | CONFIRMED |
| S1: Proposition SHADOW | CONFIRMED-WITH-FIX (F-6 direction, F-7 bridge) |
| S1: Lemmas W1R-sym + W1R-tay | CONFIRMED-WITH-FIX (F-8) |
| S2: Proposition PLD-AF | CONFIRMED |
| S2: Lemma CONE + Theorem SPLIT | CONFIRMED |
| S2: Proposition NH-WH (+ linear instance) | CONFIRMED |
| S2: Proposition ROUGH | CONFIRMED |
| S2: Lemma LC (+ LD-arith, GR as uncounted arithmetic) | CONFIRMED-WITH-FIX (F-9) |

Uncounted items:
- Proposition W1R: CONDITIONAL, correctly so.
- §5.3 obstructions: CONFIRMED (F-3).
- §6 Remark (1): OVERSTATED.
- §8 two halves, §9.4 (RLF-5) width, §14.6: ARGUED, accepted.
- The fix-9.1 claim "R1 (i) needs no (H-ch)": GAP B4.
- LD-arith "for no N": WRONG (literal).

**0 GAP and 0 WRONG among counted items.**

**Corrected tally (lane E):**
- +12 PROVEN-HERE, now reviewed: 7 from S1 and 5 from S2, as proposed.
- LD-arith and GR are reclassified as arithmetic inside the LC item, so the count is unchanged.
- 0 OPEN items closed. No new top-level OPEN item.
- (PLD-dis)/(WH) are to be recorded as **downstream of A5, not a new wall**, and (NH-iii) is to be merged with (NA-R2).

# Binding fixes (for the next lane-E session and the file owners)

1. **B1 (PLD.md):** F-1, F-2, F-4, F-5, F-6, F-7, F-8, F-9 as stated above; P-1 provenance.
2. **B2 (PLD.md l.272-274):** narrow the "correction" to RLARGE §8.2 (joint exponential moment + net is a valid route).
3. **B3 (PLD_LOG, PLD.md l.560):** correct the session-2 ordering and timestamps. Do not edit p2_criteria.md; append a
   dated note in PLD_LOG.
4. **B4 (PLD.md §9.1, §9.4; RLARGE owner):** R1 (i) and §9.0's 𝒢_x under the fix: σ-restricted gas (Lemma 7.2-0 with σ
   in place of (H-ch)). Collar-bad returned configurations become an explicit part of (SC)_k. This closes REVIEW_S18_S19
   G5 instead of the box-local (H-ch) it proposed.
5. **B5 (RLARGE §1A item 2):** drop "(H-ch) fails on Q's box" from collar-badness (SHADOW); use σ_Q.
6. **B6 (RLARGE §0/§1A, EXISTENCE §13.1 and (RLF-3^dis), PLD §6):** replace "every coupling sequence obeying (F)" by "the
   chain's own effective sequence (A5), or (F) with β_- ≥ β_1 - o(1)", with the one-loop basis marked ARGUED.
7. **B7 (RLARGE §8.2-8.3):** move (PLD)_k from RLF-step's hypothesis list into (I_k)/(SF)_k's outputs via (SG)_k on Λ(𝔥)
   and Lemma HS (Part 5, 4a).
8. **B8 (EXISTENCE, owner):** X-RP^S class: "closed … open half-space" should read "all descendant sites strictly on the
   positive side". Record (PLD^mod_dis) uniform as downstream of A5 (PLD-AF).
9. **B9 (tori):** adopt PLD §12 item 4. Use hypercubic tori in RLARGE, or allow two (electric/magnetic) coupling shifts.
