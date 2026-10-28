# REVIEW_S16_S17: hostile review of sessions 16 and 17 (linear package write-up; 4D large-field R-operation)

Reviewer: an independent agent that wrote none of the proof. I edited no other file. No commits, PRs or pushes.

Inputs:
- REVIEW_S15_CONVERGENCE.md (format; its 6 binding fixes).
- `diff PROOF_session15_snapshot.md PROOF_session17_snapshot.md` (261 lines). PROOF.md is byte-identical to the session-17
  snapshot (`cmp` empty). The session-16 and session-17 snapshots differ only by the [S17] pointer appended at the end
  (PROOF l.4947-4965).
- PROOF.md read by offset: the headers l.1-61; N2-exp l.2735-2772; Corollary N2-exp-b l.2773-2798; N2-exp' l.3113-3160;
  the (G♯_0-fine) block l.3290-3320; NA-lev / E-low l.3326-3381; the [S16] block l.3408-3479; Theorem CE l.1744-1915;
  CE-geo' l.2141-2172; the tally l.4456-4500; the [S17] pointer. For LINEAR_PACKAGE I checked every "l.N" pointer
  against PROOF_session16_snapshot.md (as the package says).
- LINEAR_PACKAGE.md (all 431 lines). RLARGE.md (all 529 lines). LOG.md sessions 16-17 (l.745-808).
- checks/c31_* and c32_* (criteria, scripts, records, stored outputs); c21-c30 stored outputs for the package's §8 inventory.

Scratch work (re-runs) is in the scratchpad directory `rev1617/`.

---

## Bottom line

- **All 6 R15 fixes are applied correctly.** No residue of the narrowed NA-lev headline is left unannotated.
- **Lemma F-df_0: CONFIRMED.** I re-derived steps (0)-(4) independently. The gauge-invariance continuation, the
  divided-difference bound, the telescoping, the antisymmetry bookkeeping and the constant 2M/(m_*' - m') are all
  right. The condition m_*' ≤ 0.1 that the last inequality needs holds by the definition of η'_*.
- **LINEAR_PACKAGE.md: NOT READY for outside readers.**
  - The mathematics in it is transcribed faithfully. Two statements drop a hypothesis or conflate a constant, and 13
    sentences would mislead an expert.
  - It has no bibliography. It uses about 30 internal labels without defining them, and it carries internal governance
    text.
- **RLARGE.**
  - RLF is a reasonable target statement, but it is not yet faithful in three places: (RLF-3), the reference
    normalisation of (RLF-1), and the complex-field requirement.
  - GT-lat' and RS: CONFIRMED.
  - CL: CONFIRMED-WITH-FIX.
  - The TS item (counted together with R1): **GAP**. R1 (iii)'s B_4 step is false as written: Ŷ = Y + {0,1}⁴ is not
    B_4-covariant at a fixed base point. TS's hypothesis region is also too small for R1's hypotheses. Both are repairable
    in one session.
  - The inductive step is conditional on more than the five named hypotheses. I found four unnamed gaps. (P1), (P4) and
    (P5) are not "proven outright".
  - The n_* table is labelled [inference], but the conclusion drawn from it is not.
- **c31 and c32 re-run identically** (all six parts; only the timing differs).
- **Corrected tally: 67 / 2 / 7 / 24 + 1**, against the claimed 68. Lemma F-df_0 (+1) is confirmed. The TS/R1 item
  (-1) is held at GAP until fixes R-3 to R-5 are written.

---

# PART 1: session 16

## [R15-fix] audit (REVIEW_S15_CONVERGENCE binding fixes 1-6)

| # | Fix | Where now | Verdict |
|---|---|---|---|
| 1 | G♯_0-soft: two sentences labelled ARGUED | PROOF l.3260-3264 | Applied. The theorem itself is unconditional in ω, and this is said. |
| 2 | NA-lev headline narrowed; Def indexing; explicit smallness | header l.56-61; L2 l.720-724; L5 l.3189-3191, 3338-3349, 3375-3381; tally l.4488-4489; LOG l.730 and RTARGET §37 annotated, not edited | Applied. `grep` finds no unannotated "artefact of the direct step" or "no longer an n-uniformity problem" in PROOF, RTARGET or LINEAR_PACKAGE. The RTARGET §34 title is a pre-stated question, which is fine. The 8-pairs multiplicity for link indexing is right: 4 directions × 2 endpoint blocks. |
| 3 | (G♯_0-fine): k ≥ 3; the k = 1, 2 cases; (G♯_0-fine-up) displayed | l.3303-3313 | Applied. I re-derived the finite-scale bound: Osc_2(Q_ρ)² ≤ ρ^{-4}Osc_2(Q_1)² by sub-box averaging, so ρ^{-α}Osc_2 ≤ n^{2+α}Osc_2(Q_1) ≤ 9³Osc_2(Q_1). Correct. (G♯_0-fine-up) is now a precise statement. |
| 4 | RTARGET §37 annotation | RTARGET l.661 | Applied, as an annotation. |
| 5 | c31 E: E-low instance | c31 E | Applied. It is the exact per-mode minimum λ_2(A)/ψ (ν is the null vector of A, so the ν^⊥ minimum is λ_2). Re-run: identical. |
| 6 | LOG l.666, l.700 annotated | LOG l.666, l.701 | Applied. |

The governance correction (header l.27-29; LOG l.756-762) cites a session brief I cannot see. I take no position on it.
The cost point it keeps is the substantive one.

## Lemma F-df_0 (PROOF l.3414-3469): CONFIRMED

- **(0) Gauge invariance on the strip.**
  - f_0 depends on B_k only through dB_k (N2-a). So 𝔅(p)·ν(p)t̂ = 0 for every t̂ at every grid point p ≠ 0. At p = 0 it
    holds trivially.
  - The grids (2π/T)Z⁴ over all T ≥ 1 are dense. N2-exp' (i) gives analyticity of 𝔅 on the open strip, so the identity
    continues to it.
  - Two remarks on the end point:
    - The parenthetical justification of f̂_0(0) = 0 in step (3) is redundant. Factorisation (2) gives 𝔅(0) = 0
      directly.
    - The constant-B_k (harmonic) mode is also covered by N2-a.
- **(1) E and T.**
  - On |Re w| ≥ π/2 we have Re e^{iw} ≤ 0, so |ν| ≥ 1. On |Re w| ≤ π/2:
    - Re∫_0^1e^{itw}dt ≥ e^{-m'}·2/π;
    - Cauchy on discs of radius below m_*' - m' gives |g'| ≤ M/(m_*' - m').
  - The bound max(2, (π/2)e^{m'}/(m_*' - m'))·M is right.
  - The final ≤ 2M/(m_*' - m') needs m_*' ≤ 0.1. This holds because η'_* is defined as the largest η ≤ 0.1
    (l.3148).
- **(2) Telescoping.** I re-derived it.
  - E_{<α+1} = E_αE_{<α} (the evaluations commute), and (1 - E_α)g = ν_αT_αg.
  - Apply E_{<v} and E_{<v+1} to Σν_μ𝔅^μ = 0. The μ < v terms vanish because ν_μ(0) = 0; at v the second also loses its
    μ = v term. Subtracting gives ν_vE_{<v}𝔅^v = -ν_vΣ_{μ>v}ν_μh_{vμ}, and division off {ν_v = 0} gives the rest.
    Correct.
- **(3) Antisymmetry.** Σ_{α<β}h_{αβ}(ν_αb̂_β - ν_βb̂_α) = Σ_vb̂_vΣ_μν_μh_{μv}. Correct.
- **(4) Kernel bound.** Paley-Wiener and Poisson summation, as in N2-exp. Correct.
- **c31 F, re-run.**
  - Identical output. The script does test the identity non-trivially. It uses the actual c26 f_0 symbol at all grid
    points with every p_α ≠ 0, and h is built from B-values at grid points with some p_γ = 0. Those are genuine values,
    not limits.
  - The strip bound is not tested. This is disclosed.
- **Fix F-1 (wording, optional).** The name "F-df_0" is historical. Read literally it is empty: f_0 = n²dB_0, so df_0 = 0
  by Bianchi. In LINEAR_PACKAGE, call the lemma by what it proves: "Lemma 4.4 (exponential F-representative of
  f_0)". Keep the old label only in parentheses.

## Lemma E-low and c31 E: CONFIRMED (re-run)

- c_E = 2/(π²·49.80) = 0.0040691, with R̄ = 1.2361. Correct.
- E1 minima: 7.61, 7.31, 7.28 and 9.05 × c_E. E2 chain ratios: ≥ 7.3 c_E. Symbol and chain agree to ≤ 6.5e-15.
- E3 gives η̄ = 1.9038e-7. All identical to the stored output.

## LINEAR_PACKAGE.md: line-by-line against PROOF_session16_snapshot.md

### Statement-match audit
I checked every "l.N" pointer (§1-§7). Where a statement is faithful I say nothing. Mismatches:

| Package | PROOF | Issue | Fix |
|---|---|---|---|
| §4 Thm 4.2/4.2', l.171-178 | l.2735-2742; l.3148-3150 | "m_* (resp. m_*')", but (i) and (ii) are written with m_*' only. As written, the reader is told that N2-exp gives the strip m_*'. | Write (i)-(ii) with "m_♮ ∈ {m_*, m_*'} respectively", or state the two theorems separately. |
| §3 Prop 3.3, l.142-145 | l.1990-1996 | Drops "(b1) needs M_2 ≤ ε_*, i.e. small F_0 and R_top". BG-b is a smallness condition, so without this the proposition reads as unconditional. | Add "provided M_2 ≤ ε_* (small coarse curvature and top residual)". |
| §1.3 l.55 / §2.7 l.116 | l.1924 vs l.2654 | κ̂ has two definitions: max_iκ_{k-1}/κ_i in Setting SC, κ_+/κ_- in §4 and EXP-real. Lemma 2.7 uses R̄ "of EXP-real", so κ̂ = κ_+/κ_- there. E-low holds with either, because the first is ≤ the second and R_μ ≤ 1 + (max_iκ_{k-1}/κ_i)/(L² - 1). | Say which κ̂ each constant uses, and that either is valid in E-low. |
| §2 Lemma 2.2, l.89 | l.3849-3856 | "In d = 4 the coarse action never exceeds the fine action, at any depth" leaves out "linearised abelian". An outside reader will take it as the Wilson action. | "(linearised abelian action; compact U(1) within the principal branch)". |
| §6.2 l.271 | l.2604 | "O_FP ≥ min(c_PG, 4) on the slice"; PROOF says "on H_0". | Use PROOF's wording, with H_0 defined. |
| §4.4 (ii), l.209 | l.3447 | The "≤ 2M/(m_*' - m')" uses m_*' ≤ 0.1, which is not said. | Add "(m_*' ≤ 0.1 by definition)". |

Every other statement matches PROOF: hypotheses, constants, "linearised"/"abelian"/"n ≥ 1" scope, and the
small-curvature scope where it is stated. This covers Thm 2.1, Lemmas 2.3-2.7, 3.1-3.2'', 3.4-3.7, Thm 3.8, 4.1,
Cor 4.3, Lemma 4.4, Thm 5.1 (S11 constants κ_0 = 16 log 12800, K_0 = e^{κ_0}/6400, C_K = 32eK_0), 6.1-6.8 and 7.1.

### Check inventory (§8): CONFIRMED-WITH-FIX
- I compared the stored outputs with the table.
  - c23 Q3 FAIL, c26 Q7 FAIL, c27 E3 FAIL and c28 B FAIL are reported as pre-registered.
  - c28 C3 and C4 FAIL are reported as pre-registered, but grouped under one reason.
  - c21 13/13 PASS and c24 V1, Q1 PASS are reported correctly.
- **Fix P-1.** c28 C3 is the T-stability of R (≤ 1.10 failed). Only C4 is the pre-asymptotic fit window. Give each its
  own reason.

### Sentences that would mislead an outside expert (each needs a fix before publication)
1. **l.42-44** "Balaban's averaged link CMP 109 (0.4), with the two contour families paired by order, equals S4' exactly
   … So the averaging is not the soft-specific part of this package; the constraint is."
   - Balaban's (0.4) averages the two families *independently* (PROOF l.567-570). With the pairing it is S4'. Without
     it, the two differ at second order (c17 B, ratio 3.96).
   - The pairing is load-bearing for RS's ribbon constant (c32 A6: 15 against 9).
   - Rewrite as: "S4' is Balaban's (0.4) with the two families paired by order; they agree at linear order, which is
     all this package uses, and differ beyond it." Make the same correction at l.365-367.
2. **l.89** (above): "never exceeds the fine action" without "linearised abelian".
3. **l.171-178** (above): the m_*/m_*' conflation.
4. **l.233** "Theorem CE = Dimock I Thm 27 in corrected form", and **l.244** "Four textual discrepancies of the source
   were repaired".
   - An expert will read this as errors in Dimock's paper.
   - What PROOF actually records: the quantifier order of c_0 (which Dimock's own proof remarks on, p.40), four textual
     discrepancies (1, 3, 4, 5) and one difference in polymer class (l.1909-1915).
   - List them in the package and classify each (typographical or substantive). Say "re-proved in d = 4 with explicit
     constants; the κ-dependence of c_0 that Dimock's proof notes (p.40) is put into the statement".
5. **l.249-251 (credit).** The credit is substantively accurate. PROOF l.1863-1869 and the remark "So c0 does depend on κ"
   match. But the paper is cited only as "Dimock I". Give the full reference: J. Dimock, "The renormalization group
   according to Balaban, I. Small fields", Rev. Math. Phys. 25 (2013), arXiv:1108.1335 (as in PROOF L6). Balaban's papers
   need full references too (CMP 95, 96, 98, 99, 102, 109, 116, 119, 122). **The package has no bibliography.**
6. **l.192** "The located rate scales like √κ, the mass of the soft constraint". "Mass of the soft constraint" is an
   interpretation, and the √κ scaling is numerical. Label both.
7. **l.195-196** "so the proven rate alone requires blocks of side M ≳ 457/m_*'".
   - That the linear kernel rate is the rate N6 needs is ARGUED in PROOF ("a necessary input, not N6 itself"; "What N6
     consumes" is ARGUED).
   - Say "if N6's activities inherit the linear rate (argued, not proven)".
8. **l.262-267** "the slice alone is not admissible, and the earlier 'double fixing' … is not an identity". This is
   internal history and means nothing to an outside reader. Delete it, or state the admissibility condition itself.
9. **l.363-364** "Not the OpenAI / Balaban result. The announced 2026-10-26 proof is unverified …"
   - This puts Balaban's published UV-stability series side by side with an unverified announcement.
   - Rewrite as: "This is neither a re-verification of Balaban's UV-stability theorem (CMP 1984-89), nor an assessment of
     any recent claim."
   - Do not name an unverified third-party announcement in a mathematical write-up.
10. **l.414-416** "In Balaban units this package is roughly the U = 1 part of CMP 95/96". CMP 95/96 have not been read:
    NOTES has only formula (1.66) of CMP 95, cited through CMP 109. Label it "[inference, from citations; CMP 95/96 not
    read]".
11. **l.7-10** "Every item below has been through at least one independent hostile review … The one exception is Lemma
    F-df_0". Update this after the present review: F-df_0 is CONFIRMED. The rest is accurate (A1/A2 were reviewed in
    REVIEW_S5_S6, which the list includes).
12. **§10, l.381-389** "at most one more session under the owner's wind-down decision".
    - It is stale: session 17 spent that session on RLARGE, so (LED-src) and the multi-level gap were not attempted.
    - §10's tree also predates RLARGE's reduction of B-W2.
    - Either freeze the package "as of session 16" with a dated note, or update §10.
13. **§11 (l.420-431).** This is internal governance: "owner", "lead", a quoted private message, the memory file and the
    correction of a review's reading. It does not belong in a public mathematical document. Move it to an internal
    appendix or delete it.

### Undefined internal coinages (define in §1, or replace with a description)
- **Labels used without definition:** N2, N4, N5, N6, N7-N12, BG-reg, BG-b (only "the soft analogue of Balaban's (1.2)"),
  B-NA, B-NA-red, NA-H, (G♯_0-field), (G♯_0-fine), (G♯_0-fine-up), (R♯_ω), (FP♯'), G♯_0-plain, LED-src, FP_U(V),
  L4a-flow, L1d-soft, DF1-3', W1-loc, W2, D4-obs, L6, L7-L10, F2-F4, C1-C4, E7.0', R4D-iso, D4-norm, LF-count, decision 4,
  "comparison branch", "(H1)/(H2)" (defined in §3.3 but used earlier), Phys, H_0, "template contours", "located rate"
  (defined, good).
- **§10.** The DAG is unreadable to an outsider. Replace it with a short prose list of the paper-scale tasks, each in
  standard terms: background-field existence and regularity for SU(N); propagator bounds at a general background;
  localisation and polymer bounds; coupling flow; large-field renormalisation; assembly.

### "What this is NOT" (§9): incomplete
Add:
- **(a)** Not the compact or non-linear abelian theory. Everything is the non-compact linearisation.
- **(b)** Not a statement about the functional integral. §2-§6 are deterministic, variational statements about the
  chain's minimiser and responses; §7 is the only probabilistic statement, and it is for the free field.
- **(c)** Not the continuum limit, the OS axioms or a mass gap.
- **(d)** Not the large-field work of RLARGE.md, which is a separate, conditional reduction.

### Public-readiness verdict: NOT READY
The mathematics is faithfully transcribed, but the document is not yet self-contained. Required before publication:
- statement fixes P-2 to P-6 (the table above and items 1-3);
- a bibliography;
- definitions or removal of the coinages;
- the governance and OpenAI text removed;
- the Dimock "discrepancies" made explicit;
- the F-df_0 review status and name updated;
- §9 completed;
- §10 frozen or updated;
- the line pointers made to resolve for an outside reader. They point to an internal snapshot, so either publish that
  snapshot with the package, or inline the short proofs that are now pointers (Thm 2.1, 2.6, 3.8, 5.1, 6.2, 6.3).

This is one focused editing session. No new mathematics is needed.

---

# PART 2: session 17 (RLARGE.md)

## RLF as a target (RLARGE l.42-69): CONFIRMED-WITH-FIX (statement)
RLF is a reasonable reconstruction of what a large-field R-operation must deliver: vacuum c-number, returned clusters,
unreturned regions, output, and the composition rules. Three places are not faithful:
- **(RLF-3), l.59-61: clusters whose collar is not small-field.**
  - These include clusters with |Y| ≤ n_*, and the bound Σ ≤ exp(C|T|e^{-(n_*+1)a/g_K²}) is claimed for them too.
  - It fails for them. A collar-bad cluster with few cubes has weight (Ce^{-a/g_k²})^{small}. Summed over levels with
    L^{4(K-k)} placements, that diverges, exactly as LF-count says. This is unchanged when the "bad collar" costs
    e^{-a_♭/g²}, because a_♭ (scale ε_loc² ≈ 10⁻⁵) is tiny.
  - **Fix R-1.** Either every cluster of total bad-or-collar-bad cube number ≤ n_♭ := ⌊4/(min(a, a_♭)β_-)⌋ is returned
    (a two-threshold R-operation), or (RLF-3) is restricted to clusters with n > n_♭. The second makes n_* huge.
- **(RLF-1)/(P3): the reference normalisation.**
  - "Cancels … in Z_K/Z_K^ref with matching constants" makes L6's uniformity depend on a Z_ref that is never defined.
    L6 l.3482 is itself a paraphrase.
  - **Fix R-2.** Define Z_K^ref, for example as exp(𝒱_K)·(the reference small-field partition function). Then state
    plainly that (RLF-4) gives L6-soft *for that normalisation*.
- **Missing requirement: complex fields.**
  - The small-field package works with complex data: N10, Remark CE-cx and the complex tilts of (DF3').
  - RLF should require (RLF-2)'s returned activities, and the large-field factors, to be analytic and bounded for the
    coarse field in a complex neighbourhood, not only C³ in V.
  - Add this, or record it as a further requirement on (W1-ret).
- **Composition with Theorem CE (l.67-69, §8.4 (P5)).** CE needs a *product* probability measure (PROOF l.1757). The
  level-K integrand (I_K) is Wilson + polymers at small g_K, which is not a small-activity expansion relative to Haar
  measure. See (P5) below.

## Lemma GT-lat' (l.125-156): CONFIRMED
- **(i).** I checked each of the following:
  - the tree-gauge reading S_c = hol(π_xcπ_{x'}^{-1}), and the lasso bound ||log S_c|| ≤ Cε_2;
  - the BCH estimate |Y_c(D) - Y_c(D^Φ)| ≤ C(ε_V + ε_3 + ε_2²);
  - DF̃(0) = 0, because su(N) has no Ad-trivial summand;
  - the remainder 𝔯 = ε_2(ε_3 + ε_V) + (ε_3 + ε_V)² + ε_2³. Its terms come from |∇F| = O(K_F|Z|) times |Z - Z^Φ|, plus
    the cubic Taylor term.
  - Ad-invariant forms on su(N) ⊗ R⁶ are ⟨,⟩_HS ⊗ t, by absolute irreducibility.
- **(ii).** If the family is permuted, T commutes with Λ²(R), and Λ²R⁴ is absolutely irreducible under B_4. c32 D re-run:
  the full average is scalar, and the rotation-only average is non-scalar in 20/20.

## Proposition CL (l.158-209): CONFIRMED-WITH-FIX
- **(a) Fubini.**
  - χ_Q for Q ∉ B involves only int(Q) links, which are disjoint from int(B).
  - Den_B > 0, since setting the interior links to 1 gives χ = 1.
  - ⟨r_B⟩_cut = Z_∅^{-1}∫Π_{Q∉B}χ w_rest r_B Den_B = Z_B/Z_∅.
  - Correct. This is exact and pointwise in the sample.
- **(b) Factorisation.**
  - The sites of blocks at block distance ≥ 2 are at sup-distance ≥ L + 1 ≥ 4. A plaquette meeting both interiors would
    need distance ≤ 3, so none exists.
  - A coarse link in C(Y) ∩ C(Y') would have its two endpoint blocks touching, so none exists.
  - Correct for the bare form.
- **(c) Size bound.**
  - I recomputed the numerator e^{-|Y|ε_1²/(2Ng²)}(ec_N^{-1}(κ/g²)^{N²-1})^{8|Y|} and the denominator caps (ε° + 4rg <
    ε_1, so χ = 1).
  - b_1 = n_P + 12κ(1 + A_d)² and b_0 = 16n_P + 12κp_L², from the factor ½ × 3 × 8 coarse links per cube.
  - p_r = (N² - 1)(n_ℓ + 16), and C_r as stated.
  - c32 C's b_1 = 2496 and ε_loc = 3.5384e-3 agree.
- **(d) Fix CL-1.**
  - Λ_1 = 6 + κ(2 + C_𝒩) is asserted, not derived. A fine link lies in the contours of up to 8 coarse links of C(Y), and
    log 𝒩 enters once per coarse link.
  - Either derive the per-link multiplicity of the contour means, or replace Λ_1 by 6 + 8κ(1 + C_𝒩).
  - Only constants change.
- **(e).** Correct.

## Lemma RS (l.211-256): CONFIRMED
- **(R1) Ribbon bound.**
  - The lasso inequality ||ab - 1|| ≤ ||a - 1|| + ||b - 1|| holds.
  - The far-end path is the translate of the near-end path because S4' pairs the orders.
  - A μ-step gives a degenerate rectangle. Both paths are then the same straight μ-line, so R_t = 1 exactly.
  - There are Σ_{α≠μ}|y_α - c_α| ≤ (d - 1)(L - 1)/2 off-axis steps, each worth L plaquettes. So A_d(L) = (d - 1)L(L - 1)/2.
- **(R2), (R3).** Correct.
- **(R4) Kernel branch.**
  - |N^{-1}tr(V^{-1}(M̄ - S))| ≤ ||M̄ - S||.
  - min_V of the kernel exponent ≤ its value at V = S, which is ≤ δ_c.
  - The bracket is ≥ ε_1²/(128N) - 2A_dη_1 ≥ ε_1²/(256N).
  - Correct.
- **"Kernel-mismatch case hypothesis-free": CONFIRMED.**
  - The joint law is the forward Markov chain e^{-S_0}Π K_i(U_{i+1}, U_i), and each K_i is normalised in U_{i+1}. So
    conditional on U_0, …, U_k, the law of U_{k+1} is exactly K_k(·, U_k), whatever happens downstream.
- **c32 A re-run: identical.**
  - The ribbon constant 9 and the square constant 9 are attained (8.99997).
  - With unpaired orders the ribbon ratio reaches 14.99986, so the pairing is load-bearing.
- **Caveat for the induction (not a defect of RS).** RS's event involves U_k. So the level-(k+1) large-field indicators
  must be inserted *before* U_k is integrated. RLF-step step 6 ("at the next step") has the order wrong. Fold this into
  (HIST) (fix R-9).

## Theorem R1 + Theorem TS (counted as one item; l.258-374): GAP
- **R1 (i): CONFIRMED-WITH-FIX.**
  - Hard core equals disjointness: Ŷ ∩ Ŷ' ≠ ∅ ⇔ x - x' ∈ {-1, 0, 1}⁴. The component bijection holds.
  - The other ingredients are right: |Ŷ| ≤ 16|Y|; d(Ŷ) ≤ 2(|Ŷ| - 1); #{Y : Ŷ = X} ≤ 2^{|X|}; the grading
    r' = e^{a''|Y|/g²}r; |z'_X| ≤ θ^{|X|} ≤ C_Kc_0e^{-κ_1d(X)}.
  - This is exactly the hypothesis of CE steps 3-4. Step 1 of CE (S11) outputs |K| ≤ C_KH_0e^{-κ_1d}, κ_1 = κ - κ_0 - 2
    (PROOF l.2163-2167).
  - The grading is legitimate because r_Y ≥ 0, so |z'_X| = Σ|r'_Y|.
  - The output |𝓗^{(N)}_X| ≤ e^{-a''N/g²}2κ_0Bc_0e^{-κ_0d(X)} is right.
  - **Fix R-3a.** The proof of (i) applies (c) to clusters of every size. (c) needs ε_♭(D; Y) ≤ ε_loc for *clusters*, and
    the per-cube hypothesis (H-loc) does not imply that: a plaquette straddling two cubes of Y couples their completions.
    (H-ch) on every box does imply it, since it gives ε_♭ ≤ ε_2 + 2ε_V ≤ 3ε_♮ ≤ ε_loc with D's own links, as (ii)'s proof
    itself observes. Cite (H-ch) in (i), or state (H-loc) for clusters.
- **R1 (ii): CONFIRMED.**
  - 𝓗^{(N)}_X is a finite polynomial, because N ≥ n, the number of factors.
  - K_F ~ g^{-6}e^{-a''N/g²}: the relative bounds of (d) cube to (Λ_1/g²)³.
- **R1 (iii): GAP (false step).** l.306-307 says "the family {𝓗^{(N)}_X : X ∋ x, N ≤ n_*} is permuted by B_4 about x".
  It is not.
  - Ŷ = Y + {0,1}⁴, and R{0,1}⁴ = {0,1}⁴ + t_R. So R maps the fattened union X(Y) to X(RY) + t_R, and the base-point
    condition x ∈ X is not preserved.
  - Explicit case: Y = {x - e_1} has x ∈ Ŷ. Its reflection through x, Y' = {x + e_1}, has x ∉ Ŷ'.
  - So Σ_{X∋x}Q_{X,x}/|X| need not be B_4-invariant. GT-lat' (ii) does not apply, and anisotropic marginal terms
    (t_{ab} ≠ cδ_{ab}) are not excluded. RLF-F2 is then not shown AVOIDED.
  - **Fix R-3b.** Localise at the level of cluster tuples:
    - write log Ξ = Σ over tuples (Y_1, …, Y_n) of ρ^T(touching graph)Πr_{Y_i}. The touching graph is B_4-invariant;
    - assign each tuple, with weight 1/|∪Y_i|, to base points x ∈ ∪Y_i (unfattened);
    - this family is B_4-covariant about x, and absolute convergence is inherited from (i)'s majorant;
    - then GT-lat' (ii) applies, and δβ_j is as stated with |X| replaced by |∪Y_i|.
- **R1 (iii): torus wrap. Fix R-4.**
  - Polymers with |X| ≤ 16n_* wrap around a torus of side ≤ 16n_* cubes. RLF admits every torus with side ≥ 3 blocks at
    level K, so at the last levels c̄_0 and δβ_j would depend on T.
  - Either require side ≥ 2R_*/L + 1 at every level, or define c̄_0 and δβ_j in infinite volume and move the wrap-around
    differences into a bounded boundary term. Those terms are O(e^{-a''/g²}) per cube and are not of irrelevant order.
- **TS (l.323-357): GAP (hypothesis region).**
  - (b1)-(b2) are imposed only on "every level-i cube Q meeting Δ".
  - But (TS-a) invokes R1, whose (H-ch) is on boxes of radius R_* = (16n_* + 2)L about every block centre. That is
    ~16n_* + 2 cubes beyond Δ: for n = 0, about 6000 cubes around a single cube. And R1's gas identity is a statement about
    the whole-level gas.
  - The scope line l.374, "(H-loc) holds everywhere near Δ", concedes part of this, but not the R_*-boxes.
  - **Fix R-5.**
    - State (b1)-(b2) on Δ_* := the (R_* + L)-neighbourhood of Δ at each inner level, with R1's hypotheses global.
    - State (TS-a) and (TS-b) for the terms with base point in Δ.
    - The extra volume factor ((2R_*/L + 1)⁴) goes into C_TS.
  - Small point: (TS-b) uses w_i ≤ w_{k-1}, which needs g² < a''/3, since g^{-6}e^{-a''/g²} increases only for
    g² < a''/3. Say so.
- **The "irrelevant order" reading: overclaim (R1 "Reading" l.316-321; §7.4 l.359-362, 371; PROOF pointer l.4959; LOG
  l.793-794).**
  - 𝔯 contains ε_2ε_V and ε_V².
  - For the soft kernel, ε_V = max||log(V_cS_c^{-1})|| is an O(g/√κ) fluctuation in every sea sample. So for a sea sample
    𝔯 = O(g²), the same order as the extracted quadratic part. Per level and per cube, ℛ ~ g^{-4}e^{-a''/g²}, and summed
    over levels with L^{4(K-j)} cubes that diverges, as LF-count says.
  - TS-b avoids this only because (b1) assumes ε_2 + ε_V ≤ M_2L^{-2n}. That is a smooth-background (minimiser) property.
    A level-i sea sample violates it once L^{-2n}M_2 < g.
  - So W2-F1 is "CIRCUMVENTED" only for frozen data obeying BG-b. Identifying "BG-b at level k - 1 (= node N2/BG-reg)"
    (l.362) conflates the background minimiser with the frozen sample.
  - **Fix R-6.** Replace "remainder of irrelevant order" by "remainder of order 𝔯(D). This is irrelevant for
    BG-b-regular frozen data. For sea samples it is O(g²), and its c-number and marginal parts must be re-extracted after
    the sea average ((W1-ret), restated as in R-8)". Make the same change in the PROOF pointer and in the LOG.
  - Note also: TS is not used by RLF-step at all (§8.3 uses R1 pointwise). Say that TS is the frozen-background shadow.

## The inductive step (§8; l.376-466): CONDITIONAL, but not only on the named hypotheses
- **The named hypotheses** are precise enough to state: (F), (SF)_k ⊃ (H-pos)_k, (PLD)_k, (W1-ret)_k, (HIST)_k.
- **Unnamed gaps**, each of which must be named or fixed before "a proof modulo the named hypotheses" (l.416-417) is
  true:
  - **G1 (step 1, l.418-419).**
    - CL (b)'s factorisation needs every factor of the integrand to involve the interior links of only one component.
      At effective levels, (I_k) contains the polymers E_k(X) of arbitrary extent. They couple distinct *-components, so
      r_B ≠ Πr_{Y_i}.
    - (H-pos) controls sizes and C³ bounds, not locality.
    - **Fix R-7a.** Mayer-expand e^{ΣE_k} = Π(1 + (e^{E_k} - 1)) jointly with the bad clusters. The gas becomes one of
      connected unions with e^{-κd} tails, to which CE still applies. Alternatively, name this as part of (SF)/(H-pos).
  - **G2 ((I_k) itself, l.379-386).**
    - (I_k) asserts the Wilson + polymer form of e^{-S_k} on Λ(𝔥) for *every* U_k, including cubes where U_k is level-k
      bad (CL needs the action there).
    - A small-field package produces effective actions on small-field domains only.
    - So (H-pos) "for U_k in bad cubes" is the large-field control of the effective action. That is paper-scale content,
      not the "[s]" of §11 item 6 (l.515).
    - **Fix R-7b.** Re-weight (H-pos) as [P]. Alternatively, run CL at level k with the joint (U_{k-1}, U_k) integrand,
      RS-style, so that only small-field effective actions are used.
  - **G3 (step 4 and (P1), l.425-427, 435-438).**
    - Step 4 claims weight (C_ℓe^{-a''/g_k²})^{|cubes|} for the r^ℓ-part. But (W1-ret) as stated supplies only
      min(a'', a_♭).
    - The collar-bad clusters with few cubes are unreturned (step 4), and (P1) sums only n > n_*. So they are not covered,
      which is the same divergence as in R-1.
    - **Fix R-8.**
      - Use min(a'', a_♭, a_η) consistently, and define n_* from it.
      - Return the collar-bad clusters with ≤ n_* cubes (the two-threshold R-operation).
      - Restate (W1-ret) so that it also delivers the sea-averaged c-number and marginal part of the returned activities.
        Today it subtracts only 𝓗(z^s)(1). Applied to (W1-ret)'s C³ covariant activities in V, GT-lat' would do the
        extraction; step 3 already assumes it.
  - **G4 ((P5), l.450-456).**
    - The activity arithmetic is right: κ = a''/(8g_K²), g_K² < a''/3654, and c_0(κ) ≥ c(κ_0)e^{-2κ}.
    - But CE needs a product measure, and the level-K integrand is not one.
    - **Fix R-9.** Add "(SF)_K: the last small-field step outputs the level-K integrand as a product measure times
      small-activity polymers, or a cluster expansion relative to a correlated Gaussian (which needs N5)" to the hypotheses
      of (RLF-4). Also add RS's ordering (above) to (HIST).
- **(P1)-(P5): "proven outright" is too strong.**
  - **(P1): CONFIRMED-WITH-FIX as arithmetic.**
    - Lemma LF-n is right.
    - The count is cited as 80^{2(n-1)} ((g3)) but the sum uses (80e)^n. Both are valid lattice-animal bounds, but use
      one.
    - The coverage gap is G3.
    - The RS-generated threshold 4/(a_RSβ_-) is ≈ 6·10¹⁰ (a_η ~ η_1², c32 C). Say how RS-generated clusters below it are
      returned.
  - **(P2): CONFIRMED.** Σ_k|δβ_k| is geometric with no volume factor, and |δβ_k| ≤ g_k⁶.
  - **(P3): CONFIRMED-WITH-FIX.** It needs R-2's Z_ref.
  - **(P4): not arithmetic. ARGUED.** It is a structural claim about the nesting, and it rests on (HIST)'s e^{B_0} boundary
    bound.
  - **(P5): CONFIRMED as arithmetic, GAP as composition** (G4).
  - Re-label §8.4 "PROVEN-HERE as arithmetic" as: (P1), (P2), (P3) and (P5) arithmetic PROVEN; (P4) ARGUED.
- **§8.5 l.465-466.** "Of which two are multi-defect forms of statements already proven for one defect": for (W1-ret), the
  one-defect (cl) is ARGUED [S9], as l.407 says. Write "one proven ((LD)), one argued ((cl))".
- **The n_* table (c32 C) is labelled [inference] (RLARGE l.479; LOG l.799; c32 criteria): CONFIRMED.**
  - But the conclusion "for every admissible ε_1 (≤ 2) the R-operation is needed (n_* ≥ 15)" (l.480) is also an inference.
    It rests on the one-loop rate and on a'' = 0.9ε_1²/(4N). That is the *frozen lower bound* on the per-cube cost, not
    the true cost.
  - **Fix R-10.** Label the sentence [inference]. Say that n_* is a property of the bound, and that after R-8 the
    relevant exponent is min(a'', a_♭), which makes n_* far larger.

## Checks (re-run)
Setup: laptop, nice 10, OPENBLAS/OMP/MKL/vecLib threads 1, PYTHONDONTWRITEBYTECODE = 1, sequential, no `timeout`, without
-I (as disclosed), load 4.1-6.1 (< 8), 39-40% free.

| Part | Result | Time | Peak RSS | vs stored |
|---|---|---|---|---|
| c31 F | PASS (F0 ≤ 3.7e-16, F1 ≤ 5.0e-16) | 0.63 s | 71 MB | identical |
| c31 E | PASS (E1, V, E2a, E2b, E3) | 7.8 s | 494 MB | identical except timing |
| c32 D | PASS | 0.11 s | 35 MB | identical |
| c32 C | C1 PASS (informational table) | 0.05 s | 29 MB | identical |
| c32 B | PASS | 1.4 s | 40 MB | identical |
| c32 A | PASS (A1-A6) | 3.8 s | 40 MB | identical |

Procedure:
- The file mtimes agree with the claimed order.
  - c31: criteria 16:26:54, script 16:27:35, outputs 16:28.
  - c32: criteria 17:15:47, script 17:16:55, outputs 17:17. RLARGE.md was last written at 17:18:19, after the outputs:
    this was §9 and later.
  - The order *inside* RLARGE (§0-§2 before §3) cannot be verified from mtimes.
- No tolerance was added, and no criterion was edited.
- Scope limits are disclosed: F does not test the strip, A is SU(2) on one plaquette, and B3 is d = 1.
- Two observations:
  - c32 tests none of CL (c), R1 (iii) or TS. In particular, no check would have caught the B_4 base-point error. Add
    a d = 2 instance in a future c33: compute Σ_{X∋x}Q_{X,x} for a toy gas with the fattened localisation, and show that
    it is non-invariant.
  - c32 B3 (d = 1) tests extensivity, which is generic, not the d = 4 grading.

## Overclaims in the headers and tallies
1. **PROOF l.1.** The title still says "sessions 1-16".
2. **PROOF §3 tally (l.4456) and the header tally line (l.28) say 64.** The 68 appears only in the end pointer (l.4964).
   Put the [S17] tally in §3, and list the four RLARGE items there.
3. **PROOF l.4958-4960** "the remainders are of irrelevant order and sum over inner levels uniformly under BG-b at the
   last small-field level, whatever the level-k field": R-6.
4. **LOG l.793-794** "(iv) inner remainders sum against BG-b at the LAST small-field level, never the large one (W2-F1
   circumvented)": R-6. Add "for frozen BG-b data".
5. **RLARGE l.371** "RLF-F2 AVOIDED (R1 (iii))": not shown until R-3b. Also "RLF-F3 AVOIDED": frozen BG-b data only.
6. **RLARGE l.416-417** "a proof modulo the named hypotheses, with every new estimate it uses proven": G1-G4.
7. **RLARGE l.459-461** "all level summations (P1)-(P5)" listed as "Closed": (P4) is argued, and (P1)/(P5) have coverage
   gaps.
8. **RLARGE §11 item 6**: (H-pos) weighted [s]. It should be [P] (G2).
9. **Governance (not a ruling).**
   - The [S16] order (PROOF l.4704-4714) and the owner decision relayed in LOG l.747-749 were: "no new frontier work", the
     review, (LED-src) and the gap, freeze, then the cost audit, then pause.
   - Session 17 instead opened node B-W2.
   - The LOG's session-17 "Inputs" (l.780-784) records no direction for this. If it was directed, record the source.
   - LINEAR_PACKAGE was not frozen, and the [S16] order's items 1-3 are undone (item 1 is this review).

## Verdict counts and tally

**Counted items.**
- **S16, 1 item.** Lemma F-df_0: CONFIRMED.
- **S17, 4 items.**
  - Lemma GT-lat': CONFIRMED.
  - Lemma RS: CONFIRMED.
  - Proposition CL: CONFIRMED-WITH-FIX (CL-1, constants only).
  - Theorem TS + Theorem R1: **GAP.** R1 (iii)'s B_4 step is false as written (R-3b). TS's hypothesis region does not
    support R1 (R-5). There are also two CONFIRMED-WITH-FIX items inside (R-3a, R-4).
- **0 WRONG.**

**Uncounted items.**
- RLF: a precise target; CONFIRMED-WITH-FIX (R-1, R-2, complex fields).
- RLF-step: CONDITIONAL, with the unnamed gaps G1-G4.
- (P1), (P2), (P3), (P5): arithmetic CONFIRMED (P1 and P5 have coverage gaps). (P4): ARGUED.
- LF-n: CONFIRMED.
- The c31 and c32 instances: CONFIRMED (re-run identical).

**Corrected tally: 67 PROVEN-HERE / 2 IMPORTED-AND-REVERIFIED / 7 IMPORTED-NOT-YET-REVERIFIED / 24 OPEN (main path)
+ 1 comparison branch.**
- The claim was 68. F-df_0 confirmed brings it to 64 after S16.
- After S17 it is 64 + 3: GT-lat', CL and RS. The TS/R1 item is held at GAP.
- It is restored, giving 68, once R-3a, R-3b, R-4 and R-5 are written. That is about one session. R1 alone would then be
  CONFIRMED-WITH-FIX.

## Required fixes (binding for the next session)
1. **R-3b:** re-localise R1 (iii) on unfattened tuple supports, so that the B_4 family is genuinely permuted. Add a toy
   check (c33).
2. **R-3a / R-4 / R-5:** cite (H-ch) for the cluster size bounds; handle torus wrap; state TS's hypotheses on the
   R_*-neighbourhood Δ_*, and note g² < a''/3.
3. **R-6:** "remainder of irrelevant order" → "of order 𝔯; irrelevant only for BG-b frozen data". Change RLARGE l.316-321,
   359-362 and 371, PROOF l.4958-4960, and LOG l.793-794. State that TS is not used by RLF-step.
4. **R-1, R-8:** the two-threshold R-operation for collar-bad clusters; a single exponent min(a'', a_♭, a_η) in step 4,
   (P1) and n_*; (W1-ret) restated so that it delivers the sea-averaged c-number and marginal extraction.
5. **R-7a, R-7b:** name the Mayer expansion of the non-local E_k in step 1; re-weight (H-pos) to [P], or restructure CL
   on the joint two-level integrand.
6. **R-2, R-9:** define Z_ref; add the product-measure or last-step hypothesis to (RLF-4)/(P5); fold RS's ordering into
   (HIST).
7. **(P4) → ARGUED.** Fix the (P1) count factor. Fix §8.5's "already proven" wording. Add the complex-field requirement
   to RLF.
8. **R-10:** label the "R-operation is needed" sentence [inference].
9. **CL-1:** derive Λ_1 or use 6 + 8κ(1 + C_𝒩).
10. **PROOF:** update the title, the header and the §3 tally (67 after this review), with the RLARGE items listed.
11. **LINEAR_PACKAGE:**
    - statement fixes P-2 to P-6;
    - the 13 sentences above;
    - a bibliography;
    - coinages defined or removed;
    - §9 completed;
    - §10 and §11 frozen or removed;
    - the F-df_0 review status and name;
    - P-1 (the c28 C3/C4 reasons);
    - then freeze.
12. Record in LOG what directed session 17 to B-W2.

---

## Strategic verdict: next target among (SF), (PLD), (W1-ret), (HIST), (F), N5

- **First, inside any next session: the binding RLARGE fixes (items 1-7), at one session.**
  - Their purpose is not polish. G2 and G3 show that the R-operation as written needs a two-threshold structure, and an
    effective action controlled at bad cubes.
  - Those are the parts of the large-field problem that CMP 122 is about. The reduction is less complete than §8.5 says.
- **(HIST): do not attack.** It is [P], and it is literally CMP 122 II's subject (localisation and exponentiation). The
  papers are unread, and the owner's plan pauses until they are available.
- **(F): do not attack now.** It is [P]. It needs (SF) to define the effective coupling, and it is the most standard
  (perturbative) item, so it is the best candidate for re-verification from CMP 109/119 rather than re-derivation.
- **(PLD): blocked.** It is "[s given SF]". Its multi-point form needs (DF3') with ℓ¹ control (N9), which needs N5.
- **(W1-ret): blocked.** It needs (DF4) and the corridor localisation. After R-8 it carries the sea-averaged
  re-extraction, which is genuinely new. It is premature before N5.
- **(SF) as a whole:** [P×3-4]. Too large as a single target.
- **N5: recommended**, if the lane continues past the planned soft-vs-hard cost audit.
  - N5 is the common upstream input of (SF), (PLD) (via N9/(DF3')) and (W1-ret) (via (DF4)). It has been untouched
    since session 10.
  - Its trivial-background abelian case is the natural continuation of the frozen linear package. It needs the
    exponential decay of the gauge-fixed soft fluctuation covariance (O_FP's inverse) at U = 1, by the same
    strip/EXP-id methods. The pieces are already there: PG, PG^{(k)}, FP-ab and NA-lev (c) give the gap, and LED-symb
    gives the symbols.
  - That makes it session-scale, with a clear success criterion: an exponential ℓ¹ bound on the covariance with explicit
    constants, uniform in k and T.
  - The general small-field background then becomes a perturbation of it. That part is paper-scale (CMP 95/96/99) and is
    best done after those papers are read.
- **Order:**
  - the RLARGE fixes plus the LINEAR_PACKAGE freeze (one session);
  - the soft-vs-hard cost audit (one session, already planned);
  - then, if the owner lifts the pause, N5 at the trivial background (one or two sessions);
  - everything else waits for CMP 116/119/122.
