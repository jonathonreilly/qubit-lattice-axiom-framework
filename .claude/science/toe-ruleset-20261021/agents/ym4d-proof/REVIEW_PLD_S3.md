# REVIEW_PLD_S3: hostile review of lane E session 3 (PLD.md §15 and the [RPLD-fix] edits)

Reviewer: an independent agent that wrote none of PLD.md. I edited no other file. No commits, PRs or pushes.

Inputs (line numbers are PLD.md's at mtime 2026-10-28 00:33:09 UTC, 1278 lines):
- REVIEW_PLD_S1_S2.md in full (format; binding fixes B1-B9).
- PLD.md by offset:
  - every [RPLD-fix] site (l.21-25, 196-259, 261-309, 383-430, 449-496, 505-515, 532-590, 626-632, 660-672, 757-777, 870-890);
  - §15 in full (l.892-1278).
- PLD_LOG.md in full, including the appended session-3 process-gap note.
- checks/p3_criteria.md, p3_pld.py, p3_out.txt, p3_time.txt (re-run in Part 4).
- RLARGE.md:
  - §0 (l.40-56);
  - §1A (l.95-162);
  - §5 Proposition CL (l.254-314);
  - §6 Lemma RS (l.316-361);
  - §8.1-§8.5 (l.584-721).
- HIST.md (read-only):
  - §6 including Proposition CF and its reading (l.346-413);
  - §7.3 Lemma RS-joint and (PLD-q) (l.504-524);
  - §14 (I_k^E) (l.832-937);
  - §15.1-15.2 (cones, Lemma E-loc; l.938-960);
  - grep for CLS-sf / CLS-red.
- PROOF.md: Theorem N5-sf0 statement and constants (l.5319-5366).
- EXISTENCE.md l.1655-1670 (Lemma KN, RX34-fix 9, Corollary KN-step).

Scratch work (lock wrapper, re-run outputs, my independent arithmetic) is in
`/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/rerun3/`.

---

## Bottom line

1. **The fixes are applied correctly and honestly.**
   - Every PLD-owned binding fix B1-B4, and the PLD-owned parts of B6-B9, is in place and tagged.
   - The process-gap note is accurate against the file times.
   - Two residues remain:
     - the stale "unreviewed"/tally lines in §13 and §14.9;
     - one inherited misidentification, η_1 = c_1ε_1. It is in F-9 (l.772) and throughout §15. The previous review made
       the same slip.
2. **The two counted items are mathematically right.**
   - Lemma HS-net + Proposition PLD-SG: CONFIRMED (one scope fix).
   - Proposition PLD-desc + Proposition INH: CONFIRMED-WITH-FIX.
   - I re-derived the constants C_net = 5^{N²-1}e^{m²/σ²} and a(τ) = 49τ²/(256σ²).
3. **The architecture reading (§15.3 "Reading", §15.6 E4-E5) is WRONG as an architecture.** Three findings:
   - (a) **PLD-desc gives nothing for RLF-step step 6.** It is restricted to V ∈ 𝒱^{sf}(A). Step 6 prices exactly the
     event that V is bad next to A. So RS's plaquette branch has no price under E5.
   - (b) **The look-ahead cascade does not terminate.** Its last term is a bad coarse cube, which is step 6 again. The
     zero-mismatch, zero-fluctuation configuration of Proposition CF has no in-step price at any level. E5 itself uses
     this fact to reject alternative (A), but misses that it also defeats E5.
   - (c) **m_τ = 3 uses η_1 = c_1ε_1, which is not RLARGE's η_1.** With RLARGE's (R3) η_1 = min{ε_1/(2L²),
     ε_1²/(512NA_d)}, m_τ depends on ε_1. With RLARGE's η_1 it is 5-10 levels at ε_1 = 2, and 54-101 levels at R1819-fix 8's ε_1 ≈ 2·10⁻³² (C_I = 1-2; Part 4).
4. **Finding 1 ("the ℓ¹ term is load-bearing") is mis-aimed.**
   - The consumer (Lemma HS-net) uses only t = θτ/(σ²g²) ≳ η/g². There the ℓ¹ term contributes e^{O(1/g)}, which is
     negligible.
   - What is load-bearing is the large-t non-Gaussian (background-field) mechanism of G-IR (2)(b).
   - The Gaussian computation (1) is right.
5. **Recommendation for RLARGE v2: neither option the brief names.**
   - Not in-step PLD with look-ahead: findings (a) and (b).
   - Not PLD carried across levels as its own inductive hypothesis: it contains all coarser scales (G-IR, INH) and is
     downstream of A5.
   - Instead: **a three-branch in-step price for every defect.**
     - Kernel mismatch: Lemma KN / RS (R4). Proven.
     - Fluctuation about the background: (SG^{fl})_k + PLD-desc. In-step.
     - The coherent background: priced by **the chain energy as an integrand bound** ((I_k^E) main term + a local
       classical stability inequality, HIST's CLS-sf in cone form; Lemma E-loc is its proven linear version). It goes
       into ℒ_𝔥 directly, not through a probability.
   - Proposition CF's reading (HIST l.403-412) says the third branch is the only kind of bound that sees CF's cost. It is
     ARGUED here, and its wall is CLS-sf (reduced in HIST §15 by CLS-red), not (PLD).

---

# PART 1: the [RPLD-fix] edits (priority 1)

## P-1 provenance (l.21-25): CONFIRMED
- The correction states REVIEW_X3_X4's verdicts as REVIEW_PLD_S1_S2 quoted them, and says REVIEW_X3_X4 was not re-read.
  That is accurate.
- Residue (cosmetic). §13 l.582-583 still lists the imported inputs as "unreviewed there". The header note covers it, but
  the line should carry "[see P-1]".

## F-1, PLD-fin constant (l.198-202): CONFIRMED
- 1/g_0² ≤ 1/g_k² + β_+k log L is (F)'s upper half (RLARGE l.53, j = 0). It gives g_0^{-2} ≤ (1 + β_+k log L)g_k^{-2} for
  g_k ≤ 1.
- The maximum of x^{p/2}e^{-(a-a')x} is (p/(2e(a - a')))^{p/2} at x = p/(2(a - a')). p3 C3 confirms it to 6e-16, and I
  re-derived it.
- The absorption is per plaquette, so it survives the |A|-th power. Correct.

## F-2 (l.209): CONFIRMED
- A lower bound on the m-th term needs 1/g_{k-1-m}² ≤ 1/g_k² + β_+(m + 1)log L. That is (F)'s upper half. Correct.

## F-3 (l.223-224): CONFIRMED
The sentence is narrowed exactly as asked.

## F-4 and Lemma TL (l.252-259, 951-964): CONFIRMED-WITH-FIX (minor)
- **Re-derivation.**
  - Σθ_j = 2πm, |m| ≤ N/2, since every θ_j ∈ (-π, π].
  - Shifting the m largest (or the |m| smallest) angles by ∓2π gives trace 0 and ||X||_op < 3π.
  - Γ(U) is compact and nonempty with a closed graph. A compact-valued upper hemicontinuous correspondence into a metric
    space is weakly measurable, and KRN gives a Borel selector.
  - On O_N, |θ_j| < 2π/N, so |Σθ_j| < 2π and m = 0. The principal log is then continuous (|θ_j| < π for N ≥ 2),
    Ad-covariant and odd.
  - (iii): ||1 - U||²_HS = Σ|1 - e^{iθ'_j}|² ≤ Σθ'_j² in the common eigenbasis.
  - All correct.
- My independent re-check uses a Schur-form construction and scipy expm, not p3's routine (Part 4).
- **Fix (TL-1), internal inconsistency.**
  - l.258-259 says ε_1 < 2sin(π/N) is "implied by" R1819-fix 8 (ε_1 ≤ ε_*).
  - §15.6 E8 (l.1222-1223) proposes adding it as a new condition.
  - Both are defensible: ε_* ≈ 2·10⁻³²/C_Δ is below 2sin(π/N) for every N < 10³¹. But the file should say one thing.
    Proposed wording: "implied once ε_1 ≤ ε_* < 2sin(π/N); E8 records it explicitly because ε_* is an existence constant
    (PROOF l.5320-5321)".
- Lemma TL is correctly not counted.

## F-5 (l.284-285, 342): CONFIRMED

## B2 (l.298-304, 555): CONFIRMED
The narrowed text is the review's wording, and Lemma HS-net now writes the net route out.

## F-6 SHADOW direction (l.390-394): CONFIRMED
- The comparison now goes through (F)'s upper half, and the condition (2n_c + 1)⁴a > 3κε_♮ is right. p3 C6 checks it at
  n_c = 10¹³ and a = 10⁻⁴⁰.
- **Remark (no fix needed).** Under R1819-fix 8 both a_♯ ∝ ε_1² and ε_♮ ≤ ε_loc/3 ∝ ε_1 shrink, so C6's sample point is not
  the operative regime. The condition holds anyway for structural reasons:
  - n_c = n_♯ = ⌊4/(a_♯β_-)⌋ gives n_c·a ≳ 4/β_-;
  - so (2n_c + 1)⁴a ≥ 16n_c³·(4/β_-), which diverges as ε_1 → 0, while 3κε_♮ → 0.
  Adding this sentence would make F-6 independent of the crude constants.

## F-7 bridge (l.395-399): CONFIRMED

## B4 (l.416-425, 492-494, 568-570): CONFIRMED
- The overclaim is withdrawn.
- The σ-restricted gas and the collar-bad activity family 𝓗^{cb} are stated as the review asked.
- **Note (new, see Part 3 item 3).** The 𝓗^{cb} bound is quoted "given (PLD)_k (ii) on the per-history law (§15.3, with its
  status there)". After §15.3 that status is "not an in-step output". In addition, coherent cut-good backgrounds make σ_Q = 0
  on whole regions at zero kernel and fluctuation cost (INH with ε_loc in place of η_1). So the collar-bad family has the
  same pricing gap as step 6, and the same remedy (Part 3).

## F-8 (l.449-457): CONFIRMED
Locality is now a hypothesis, the GT-lat' (ii) clause is quoted (RLARGE l.233-234), and the typo is fixed.

## W1R item (l.494-496): CONFIRMED

## B3 process-gap correction (PLD_LOG session-3 bullet; PLD.md l.626-632): CONFIRMED (honest)
- The quoted mtimes match `ls -lT` now:
  - p2_criteria 19:38:33 EDT = 23:38:33 UTC;
  - p2_pld.py 23:39:31;
  - p2_out 23:40:24;
  - p2_time 23:40:53.
- The PLD.md/PLD_LOG times 23:44:49 / 23:43:54 cannot be re-checked now (both files were rewritten), but they agree with
  REVIEW_PLD_S1_S2's "mtime 23:44 UTC".
- No history was rewritten, and the session-2 lines are left as written.
- The cross-lane EXISTENCE inconsistency is correctly routed to its owner.
- **Session 3's own record is consistent:**
  - p3_criteria 00:25:33 < script 00:26:46 < output 00:32:08 < p3_time 00:32:36 < PLD.md 00:33:09 UTC;
  - the log says §15.6 was appended at 00:27:34, while waiting for the lock.
- **Informational:** p3_time.txt says "Released by trap". The p3 criteria do not forbid a trap, so this is not a defect of
  the session.

## F-9 LD-arith (l.766-777): CONFIRMED-WITH-FIX (new fix F-9')
- **Recomputed** (Part 4, by an independent scan; log n_U/log L = 6.89279):
  - N ≥ 37 at t = 2;
  - N ≥ 593 (α = 1/(2(N - 1))) and 594 (α = 1/(2N)) at t = ½;
  - N ≥ 507954 / 507955 at t = 2/117.
  - These match p3 C1-C2.
- **Fix (F-9'), identification.** l.772 reads "at t = η_1 = c_1ε_1".
  - RLARGE's η_1 is (R3)'s min{ε_1/(2L²), ε_1²/(512NA_d)} (RLARGE l.328, l.361).
  - c_1ε_1 is the improved threshold of EXISTENCE's KN-step re-centred dichotomy (RX34-fix 9, EXISTENCE l.1663-1665).
    RLARGE has not adopted it.
  - REVIEW_PLD_S1_S2 F-9 made the same identification, so this corrects the previous review too.
  - At RLARGE's η_1 the active branch (ε_1²/(512NA_d), for every ε_1 ≤ 2 and N ≥ 2) gives αη_1²β_1 ≤ 3.5·10⁻⁸ (N = 2, ε_1 = 2; smaller for larger N or smaller ε_1), far below 6.893 for all N.
    So **"for no N" is literally true at RLARGE's η_1**, and the "not uniformly in N" wording is needed only at c_1ε_1 and
    at ε_1/4.
- **Proposed text.** "at t = η_1: with RLARGE (R3)'s η_1 for no N; with KN-step's c_1ε_1 (if adopted) only for
  N ≥ 507954".
- The route-(a) conclusion for SU(2), SU(3) is unchanged.

## B6 quantifier (l.243-245, 666-672, 875-876, E1): CONFIRMED-WITH-FIX
- The direction is right: the sequence must run at least as fast as the chain, so the condition is on the lower rate.
- **Fix (E1-a).** E1 proposes editing "§1 l.67". RLARGE §1 is pre-stated text "kept verbatim" (RLARGE l.59-62). The
  amendment belongs in §1A's change log and in Theorem RLF (l.124-125), not in §1.
- **Precision (E1-b, recommended).** "β_- ≥ β_1 - o(1)" has no meaning for a constant bracket. Write instead:
  1/g_j² - 1/g_k² ≥ β_1(k - j)log L - C(1 + log(1 + k - j)) for all j ≤ k.
  - This is the two-loop-tolerant form, and it is what GR's summable relative error needs.
  - Alternatively, keep only "the chain's own sequence (A5)".

## Overclaims withdrawn (priority 1): CONFIRMED
All three are withdrawn in place:
- the RLARGE §8.2 "correction" (l.298, l.555);
- "R1 (i) needs no (H-ch)" (l.416, l.492, l.568);
- "for no N" (l.766-773), with the identification fix F-9' above.

## Stale lines (cosmetic, fix S-1)
- §13 l.589: "+7 PROVEN-HERE (unreviewed)".
- §14.9 l.886-889: "+5 PROVEN-HERE (unreviewed)", and LC "with Propositions LD-arith and GR (one item: the loss-term
  arithmetic)".
- Both contradict the reviewed status and the F-9 counting fix (l.777). Append "[reviewed: REVIEW_PLD_S1_S2]" and "counted
  item: Lemma LC".

---

# PART 2: Lemma HS-net and Proposition PLD-SG (priority 2)

## (SG^{ph}), (SG^{net}), (SG^{fl}) definitions (l.968-990): CONFIRMED-WITH-FIX
- (M3) and (M3^+) are correctly separated. Events in U have the same law under both, because ∫K_k dV = 1 and the
  level-(k+1) indicators are not yet inserted (RLARGE §8.2 R-9 ordering).
- **Fix (SG-1), boundary scope.**
  - 𝒫°(𝔥) and 𝒬°(𝔥) exclude plaquettes and cubes near ∂Λ(𝔥), and l.976-977 sends them to "(HIST)'s boundary terms
    (e^{B_0} per boundary cube)".
  - e^{B_0} is a cost, not a suppression. An RS-generated bad level-(k+1) cube next to the history boundary still needs
    its e^{-a/g²}.
  - Since ω (the exterior) is fixed in μ_{𝔥,ω}, nothing prevents stating (SG^{net}) for every plaquette with at least one
    link in Λ(𝔥) (the others are constants). Either extend the sets, or name the boundary-adjacent defects as a separate
    priced family.
- **Fix (SG-2), what "cut-good" covers.**
  - The (TH) row (l.1022) says cut-good U and 𝒱^{sf} lie in N5's class 𝔑(α_*).
  - But G_k constrains only cube-interior plaquettes (RLARGE l.51). The inter-cube plaquettes of U are unconstrained and
    are rough with density ~e^{-c/g²} (Proposition ROUGH's mechanism).
  - E8's clause "the cut controls every plaquette used as an N5 background" must therefore be implemented as an event in
    U inside (SG^{fl})'s domain (like 𝒱^{sf}), with the residual rough inter-cube plaquettes priced separately.
  - It must **not** be implemented as a change of χ_Q: Proposition CL (a)-(b) use that χ_Q reads only interior
    plaquettes (RLARGE l.278-284).

## Lemma HS-net (l.1027-1040): CONFIRMED
- **Net.**
  - Disjoint δ/2-balls inside the (1 + δ/2)-ball give |𝒩| ≤ (1 + 2/δ)^D.
  - Maximality gives |u - v| < δ.
  - ⟨u, v⟩ = 1 - |u - v|²/2 ≥ θ.
- **Union and Markov.** At t = θτ/(σ²g²), the exponent is |A|(½θ²τ²/(σ²g²) + mθτ/(σ²g) - θ²τ²/(σ²g²)). That is the first
  form.
- **Second form.** ab ≤ a²/4 + b² with a = θτ/(σg), b = m/σ.
- At δ = ½: θ = 7/8, θ²/4 = 49/256, 5^D. **C_net = 5^{N²-1}e^{m²/σ²} and a(τ) = 49τ²/(256σ²) are confirmed.**
- t ≤ t_1 holds since θ < 1 and τ ≤ ε_1.
- Remark (cosmetic). The hypothesis is used at the single t = θτ/(σ²g²) only. Stating it as "for all t ∈ [0, t_1]" is
  harmless, but it is the source of Finding 1's mis-aim (Part 3).

## Proposition PLD-SG (l.1042-1064): CONFIRMED (fix SG-1 applies)
- (i) follows from Lemma TL (iii) and HS-net. No disjointness and no RP are used. Correct.
- (ii) Every step of PLD-red (ii) transfers:
  - the greedy 𝒜' with |𝒜'| ≥ |𝒜|/7⁴;
  - U° := U;
  - RS (R1);
  - Lemma KN at t = ε_loc/4, with independence of V's links given U under μ^+ (product kernel);
  - the subset expansion with n_R^{|S|} choice functions.
  - The last factor uses (i) on the distinct plaquettes {p_Q}, which lie in 𝒫°(𝔥) because N_1(Q) ⊂ Λ(𝔥).
  - η_♭ ≤ ε_1 is needed for (i). It holds, since η_♭ ≈ 0.064ε_loc ≤ ε_1.
  - Base ≤ 1 gives the |𝒜|/7⁴ power.
  - Correct.
- (iii) is §9.5 with η_♭'. Correct.
- The weights, (PLD-q) at η_q (stronger than HIST l.505-507, since no disjointness is needed), and "no RP" are all as
  claimed.
- The label "(PLD)_k (i) at τ = η_1" is right for any η_1 ≤ ε_1, so F-9' does not affect it.
- **Counted item 1 (HS-net + PLD-SG): CONFIRMED.** It is a correct, constant-explicit implication. Its value is
  conditional on a hypothesis that §15.2 itself says is not an in-step output. Record it as an implication, not as
  progress on (PLD).

---

# PART 3: the finding against the planned architecture (priorities 3-4)

## Finding 1 / Remark G-IR (l.992-1004): (1) CONFIRMED; (2) ARGUED, accepted; the headline "ℓ¹ term load-bearing" is MIS-AIMED (fix G-1)
- **(1) is exact.**
  - For a centred Gaussian, log E e^{t⟨e,X⟩} = ½t²v|A|.
  - The (SG^{net}) inequality at all t ≤ t_1 is equivalent to the inequality at t_1, since the slack 2mg/t decreases in t.
  - So v ≤ σ²g² + 2mσ²g³/ε_1. p3 B5 checks this algebra.
- **(2) is a plausible one-loop reading.** In the free theory the per-plaquette aligned variance of a side-ℓ family is a
  constant times g(ℓ)², because the aligned sum is ℓ⁴ × the box-averaged F, whose variance is g(ℓ)²/ℓ⁴. The constant is
  absorbable in σ_*; the running is not.
- **Fix (G-1).** HS-net and PLD-SG consume (SG^{net}) only at t = θτ/(σ²g²) ≥ θη/(σ²g²), where τ ≥ η is the smallest
  threshold used.
  - At such t the ℓ¹ slack is 2mg/t ≤ 2mσ²g³/(θη): a relative correction O(g/η) to σ²g², i.e. nothing.
  - In the bound it contributes e^{mθτ/(σ²g)} = e^{O(1/g)}, subleading to e^{-τ²/g²}.
  - Conversely, the ℓ¹ term rescues small t ≲ 2mg_k/(g(ℓ)² - σ²g²) ~ g_k only, which no consumer uses.
- So the correct statements are:
  - (SG^{net}) restricted to t ∈ [θη/(σ²g²), t_1] suffices for every consumer, and there m_* = 0 is not excluded by G-IR;
  - what G-IR (1)-(2) exclude, for aligned families at large scale, is **every Gaussian-domination proof at large t**.
    For (SG^{net}) to hold there, the non-Gaussian background-field mechanism (2)(b) must be the thing that holds.
- Replace "the ℓ¹ term is load-bearing" (l.992, l.1255-1257) by: "Gaussian domination with the true two-point function
  fails for aligned families; the large-t regime that the consumers use needs the background-field (non-Gaussian)
  mechanism; the ℓ¹ term is inessential there."
- SG-F3 is then met for a different reason: a quantifier change, namely t restricted to the consumed range.

## Finding 2 (l.1006-1014): the meta-claim is ARGUED (accepted); the counted part is INH
- "μ_{𝔥,ω} contains all coarser scales inside Λ(𝔥)" is right: it is the level-k marginal with fixed exterior, and no
  coarser variable has been integrated.
- "(SG^{net}) is not an in-step output" is a correct statement about the method. It is not a theorem: no pair of chains
  agreeing on step-k data but differing on (SG^{net}) is exhibited. Label it ARGUED. l.1006 says "SG-F1 MET", which is
  acceptable as a valid-failure outcome of the pre-stated kind, provided the ARGUED status is attached.
- "(SG^{fl})_k is in-step" is right as a reading: conditioning on V pins the block averages, so the law of U given V is
  the gapped fluctuation law of N5.

## Proposition INH (l.1066-1080): CONFIRMED-WITH-FIX (fix INH-1)
- **Re-derivation from Proposition CF** (HIST l.383-402, read):
  - the top level is k + 1, with θ := 2arcsin(ε/2) ≤ 2arcsin(0.2585) = 0.5229 < π/6;
  - ||1 - V_P|| = 2sin(θ/2) = ε;
  - the level-k (1,2)-plaquette is e^{iθL^{-2}σ_3}, so ||1 - U_p|| = 2sin(θ/(2L²)) ≥ (θ/L²)(1 - θ²/(24L⁴));
  - θ ≥ ε, and θ²/(24L⁴) ≤ 0.2734/1944 = 1.41·10⁻⁴;
  - so the plaquette is ≥ 1.001c_1ε_1(1 - 1.5·10⁻⁴) > c_1ε_1;
  - CF (1) gives zero mismatch, and CF (2) gives the finer levels.
  - Correct. p3 C4 checks the inequality on grids. The 1.001 margin is the stated one.
- **Fix (INH-1), the threshold.** "RLARGE's η_1 = c_1ε_1" (l.1010, 1071, 1077, 1096, 1204, 1259) is wrong (F-9'). The
  proposition is a statement about configurations and holds for any threshold η < ε_1/L². RLARGE's (R3) η_1 ≤ ε_1/(2L²)
  makes the admissible ε-range [1.001L²η_1, ε_1) larger, so **INH holds a fortiori with RLARGE's η_1.** State INH for a
  general threshold η ≤ ε_1/(1.001L²).
- **Structural strengthening (recommended).** INH does not depend on the constants:
  - RS (R3) must catch CF's bad V (curvature ε_1, zero mismatch), whose level-k plaquettes are ≈ ε_1/L². So **every
    RS-compatible threshold satisfies η_RS ≤ ε_1/L²(1 + o(1)).**
  - INH realises every η < ε_1/L² with cut-good V.
  - Hence no choice of thresholds puts η_RS in PLD-desc's in-step range τ ≥ 2τ_bg. The range can be refined to
    (1 + δ)τ_bg, but τ_bg ≥ ε_1/L²(1 - o(1)) under the CF identification.
  - This answers the brief's question 3. **Choosing η_1 relative to τ_bg cannot restore in-step derivation.**
  - Nor can decoupling the cut used in 𝒱^{sf} from RS's ε_1. With a smaller cut ε_1'' the in-step range can be made to
    contain η_RS, but the remainder becomes the level-(k+1) event "some V_P ∈ [ε_1'', ε_1) near A". Pricing it is
    (PLD)_{k+1} at threshold ε_1'', whose own remainder is a coarser event, and so on: the cascade below.

## Proposition PLD-desc (l.1082-1091): CONFIRMED-WITH-FIX (fix PD-1, trivial)
- **Proof.** B_V is V-measurable, so conditionally on V the family (Y_p)_{p∈A∖B_V} is fixed. (SG^{fl}) for the subset
  needs V ∈ 𝒱^{sf}(A∖B_V), which is implied by V ∈ 𝒱^{sf}(A). Lemma TL (iii) and HS-net at τ/2 then give the bound.
  Correct.
- **Fix (PD-1).** B_V is defined with "≥ τ/2" and τ_bg as a sup. At τ = 2τ_bg with the sup attained, B_V ≠ ∅. Write
  τ > 2τ_bg, or define B_V with ">".
- **Counted item 2 (PLD-desc + INH): CONFIRMED-WITH-FIX (INH-1, PD-1).** Both statements are correct; the fixes are
  wording.

## The "Reading" of PLD-desc and the look-ahead claim (l.1092-1102): WRONG as an architecture (three independent defects)
1. **(Arch-1) Step 6 is outside PLD-desc's domain.**
   - RLARGE step 6 (l.673-676) prices a bad level-(k+1) plaquette P (||1 - V_P|| ≥ ε_1). By RS (R3) it reduces to a
     level-k plaquette ≥ η_1 in U_4(P).
   - PLD-desc bounds μ^+(…, V ∈ 𝒱^{sf}(A)), and 𝒱^{sf}(A) requires every level-(k+1) plaquette within R_bg of A to be
     < ε_1. P is within distance 1 of A.
   - So on step 6's event V ∉ 𝒱^{sf}(A), and **PLD-desc gives no bound at all**: there is neither an in-step part nor an
     "inherited part".
   - E5's replacement of step 6, "PLD-desc at τ = η_1 (in-step part) + inherited part as in step 4" (l.1210-1211), is
     therefore void. RS's plaquette branch is unpriced.
2. **(Arch-2) The cascade does not terminate.**
   - The inherited remainder at each level is a coarser large-ish field. After m_τ levels it is a cut-bad coarse cube
     (V ∉ 𝒱^{sf}), whose only price in RLARGE is step 6 at that level. That is RS → (PLD)(i) at η_1 → Arch-1 again.
   - CF's configuration is the obstruction. It has zero mismatch at every level (CF (1)) and zero fluctuation about its
     own background (under §15.3's ARGUED identification 𝔟(V) = CF preimage; even without that identification, Arch-1
     already leaves it unpriced).
   - Every in-step price in E4-E5 (KN, (SG^{fl})) therefore vanishes on it at every level. Its only cost is the chain
     energy, ≈ θ²/(2g_0²) per site (CF (3)).
   - E5 (l.1213-1215) rejects alternative (A) because of exactly this configuration ("a bad level-(k+1) plaquette with no
     fluctuation and no mismatch at any level"). The same configuration defeats E5's own look-ahead.
   - "Evaluating them after m_τ more steps changes no other step" (l.1211-1212) is therefore false: no later step prices
     them either.
3. **(Arch-3) m_τ = 3 uses the wrong η_1.**
   - With RLARGE's η_1 = ε_1²/(512NA_d) (the active branch), the least m with (L²/(2C_I))^mη_1 ≥ 2C_Iε_1/L² is
     5/7/10 (C_I = 1/1.5/2; N = 2, ε_1 = 2), 6/8/12 at ε_1 = 0.517, 10/14/19 at ε_1 = 10⁻³ and 54/74/101 at ε_1 = 2·10⁻³² (N = 3 within ±1).
   - It grows like log(1/ε_1), so it is 54-101 levels under R1819-fix 8's ε_1 ≈ 2·10⁻³².
   - With KN-step's c_1ε_1 (not in RLARGE, and not among E1-E8) it is 3/4/5 for C_I = 1/1.5/2, as p3 C5 says.
   - Either way the depth is g-independent, but "m_τ = 3" is not RLARGE's number.

**Physics check (why the obstruction is architectural, not a falsity of (PLD)).**
- The coherent event at threshold η involves scales k … k + m(η), with L^{2m}η ≈ ε_1.
- The running over m levels changes 1/g² by O(m), i.e. a factor e^{O(mη²)} per plaquette. That is a constant, absorbable
  in C.
- So (PLD)_k at η_1 is very plausibly TRUE with uniform constants. What fails is only that no in-step probability
  argument proves it.
- The quantity that does carry the cost locally is the chain energy, which aggregates the L^{4(k-j)} finer terms. HIST's
  CF reading (l.408-412) states exactly this: aggregating bounds see CF's cost; sup-threshold and fluctuation bounds do
  not.

## §15.4 levels 0 and 1 (l.1104-1145): CONFIRMED as a reduction (priority 5)
- **Level 0.**
  - The Gaussian-part arithmetic is right: ||C|| ≤ 1/λ_min, ||D_𝔟||² ≤ 16(1 + O(α_*)), so
    σ_fl² = 128coth⁴(m/2)(1 + O(α_*))/(γ'(1 - ε_R)).
  - **Fix (L0-1).** PROOF l.5322-5325 instructs that "everywhere a 'gap' of N5-sf0 is quoted, these are the numbers":
    - λ_min ≈ 7·10⁻⁸² (product-rule m), or
    - ≥ γ'(1 - ε_R)/9 ≈ 6.6·10⁻¹⁰ by Proposition RW-ℓ² [S20].
    So quote σ_fl² ≤ 144(1 + O(α_*))/(γ'(1 - ε_R)) via RW-ℓ², not "γ' ~ 10⁻⁸" with the coth⁴ form unevaluated. Only
    finiteness is used, so nothing else changes.
  - **The named missing steps are the right ones.**
    - (G0-1) covariance → exponential moment by Bakry-Émery → LSI → Herbst. The Bakry-Émery step needs a convex chart
      domain: Lemma AX boxes. Conditioning on the cut costs 1/μ(cut | box). This is legitimate for exponential moments,
      since E[e^f 1_cut] ≤ E e^f, though not for LSI itself. The chart-Hessian estimate (a) and the FP/Jacobian
      estimate (b) are correctly ARGUED.
    - (G0-2) (SF)_0.
    - (G0-3) threshold compatibility: needs fix SG-2 (inter-cube plaquettes).
    - (G0-4) the mean, O(g²): correctly ARGUED.
  - "SG-F2 MET" is accurate.
- **Level 1.**
  - The reduction to (NA-H_loc)_1 (with locality) + (I_1^E) + (G1-1)-(G1-4) is consistent with PROOF's Proposition
    N5-sf_i (implication from (NA-H_loc)_i) and HIST §14.1.
  - The dependency on session 20 is correctly flagged.

## §15.5 (INF)_k and Lemma AZ (l.1147-1183): Lemma AZ CONFIRMED (uncounted, correctly); (INF) merge CONFIRMED-WITH-FIX (tally)
- **AZ re-derivation.**
  - 𝔉_{i+1} = σ(𝔉_i, φ_i) (φ_i determines U_{i+1} given 𝔉_i), so the M_j := E[Φ | 𝔉_j] form a Doob martingale, and
    Σ_{i<k}D_i = Φ - E[Φ | 𝔉_0] because Φ is 𝔉_k-measurable.
  - Herbst under LSI(c_Kg_i²/κ) with Lip ≤ C_Iρ^n gives b_i².
  - The tower property from the top gives Σb_i² ≤ c_KC_I²g_k²/(κ(1 - ρ²)), using g_i ≤ g_k ((F)).
  - With r = τ/2 this gives a_N = κ(1 - ρ²)/(8c_KC_I²). Correct.
- **Caveat (already ARGUED in the file, sharpened here).** (NH-i') is an LSI on SU(N) for e^{-(κ/g²)φ}, which is not
  log-concave globally. A uniform LSI constant ∝ g²/κ for a single nondegenerate well needs a single-well argument
  (Holley-Stroock alone loses e^{O(κ/g²)}). It is OPEN for N ≥ 3, as stated.
- AZ is a statement about the plain chain P_K, which is where (NH) lives (§14.3). Correct.
- **Fix (INF-1), tally.**
  - (INF) is strictly stronger than each of (NH-iii) and (NA-R2): (INF) ⇒ (NH) is PROVEN (AZ + (NH-i')), and
    (INF) ⇒ (NA-R2) is ARGUED. Neither converse holds.
  - Merging is consolidation by a common sufficient condition, not an equivalence.
  - So the ledger should record "(NH-iii), (NA-R2) ⇐ (INF)" and keep **0 net change**. The "−1 otherwise" of l.1275-1276
    should be struck.

---

# PART 4: check p3 (re-run under the numeric lock) and reviewer arithmetic (priority 7)

Run discipline, from my run record:
- The lock was acquired by the mandated `until mkdir … numeric; do sleep 20; done` loop and released by one `rmdir`. No
  trap was used.
- Wait from 00:46:34 UTC (held by another agent); acquired 00:50:34; load 2.79; 37% memory free; p3 00:50:34-00:50:35 (1.19 s, 90 MB, exit 0); reviewer arithmetic 0.62 s, 61 MB, exit 0; released 00:50:36 UTC (another agent re-took it afterwards).
- nice 10; OPENBLAS/OMP/MKL/VECLIB threads 1; PYTHONDONTWRITEBYTECODE=1; python3 without -I; no `timeout`.
- Outputs went to the scratchpad; the stored outputs were not touched.

| Check | Criteria before script (mtime UTC) | Re-run vs stored output | Verdict |
|---|---|---|---|
| p3 A (TL) | 00:25:33 < 00:26:46 | byte-identical (whole file, SUMMARY included) | PASS as reported |
| p3 B (HS-net, HS, net, negative control, G-IR algebra) | same | byte-identical | PASS as reported; B3 is in-tolerance (0.87439 vs 0.875) and disclosed |
| p3 C (arithmetic) | same | byte-identical | PASS as reported; C2's t = 2/117 and C5 encode η_1 = c_1ε_1 (F-9', Arch-3) |

**Discrimination.**
- A6 is a genuine negative control: the principal log is not traceless at central elements.
- B4 shows that the exact probabilities are not trivially small.
- B1-B2 hold with ratios 103 and 21.9. They are not tight, as is usual for net bounds.
- B3 certifies covering only of the sample points. The proof uses the maximal-net covering, not this set, as the file
  says.
- B5's Monte Carlo is a sanity check of the Gaussian MGF identity only.
- Nothing tests SU(N) measures, (SG), N5, CF on the lattice, or (INF). The file says so.

**Reviewer arithmetic** (my script `s3_review_arith.py`; it uses no code from p3):
- log n_U/log L = 6.892789 (L = 3). Smallest N: 37 (t = 2); 593 / 594 (t = ½; α = 1/(2(N - 1)) / 1/(2N)); 507954 / 507955
  (t = 2/117). All agree with p3 C1-C2.
- RLARGE (R3)'s η_1 (active branch ε_1²/(512NA_d) for every ε_1 ≤ 2): αη_1²β_1 = 3.5·10⁻⁸ (N = 2, ε_1 = 2), 1.6·10⁻¹⁰ (ε_1 =
  0.517), decreasing in N; no N satisfies the summability condition (scan to 10⁹). c_1ε_1/η_1 = 39-229 for ε_1 ∈ [0.517, 2],
  ~10⁵ at ε_1 = 10⁻³: the two thresholds are not interchangeable.
- m_τ with (R3)'s η_1 (least m with (L²/(2C_I))^mη_1 ≥ 2C_Iε_1/L², L = 3), C_I = 1/1.5/2: N = 2: 5/7/10 (ε_1 = 2), 6/8/12
  (0.517), 10/14/19 (10⁻³), 54/74/101 (2·10⁻³²); N = 3 within ±1. With c_1ε_1: 3/4/5 (p3 C5).
- INH with (R3)'s η_1: at ε = 0.999ε_1 the coherent level-k curvature is 2.02× ε_1/(2L²) (ε_1 = 0.517 and 10⁻³), so the
  INH range is non-empty for every RS-compatible threshold.
- Lemma TL by an independent construction (complex Schur form, scipy expm; N = 2, 3, 5; 1500 Haar samples + all central
  elements each): ||e^X - U|| ≤ 8.5·10⁻¹⁵, |tr X| ≤ 1.0·10⁻¹⁴, ||1 - U||_HS ≤ |X|_HS in every sample, ||X||_op ≤ 1.6π (< 3π).
- G-IR (1) illustration: equicorrelated Gaussian with correlation 0.1 has per-plaquette aligned variance 1.9 / 10.9 at
  |A| = 10 / 100: the aligned variance, not the per-plaquette one, is what (SG^{net}) must bound.

---

# PART 5: the proposed RLARGE v2 edits E1-E8 (priority 6): coherence, sufficiency, ranking

Ranked by necessity (1 = most necessary):

| Rank | Edit | Necessary? | Correct as drafted? | Verdict |
|---|---|---|---|---|
| 1 | **E2** (drop (H-ch) from collar-badness; σ_Q) | Yes: SHADOW is PROVEN; without it (RLF-3) is false | Yes | ADOPT |
| 2 | **E3** (σ-restricted gas; collar-bad family in (SC)/(W1-ret')(a); extract after the sea average) | Yes: B4 gap | Yes, but the 𝓗^{cb} price inherits Arch-1/2 (Part 1, B4 note) | ADOPT, with its price routed as in the recommendation below |
| 3 | **E1** ((F) quantifier) | Yes: the RLF statement is false otherwise (one-loop basis ARGUED) | Direction right; must not edit pre-stated §1 (E1-a); make "o(1)" precise (E1-b) | ADOPT-WITH-FIX |
| 4 | **E4** ((PLD)_k is not a hypothesis; (SG^{fl}) + PLD-desc + look-ahead) | Some replacement of (PLD)_k is necessary: Part 5 of REVIEW_PLD_S1_S2 and §15.2 both show it cannot stay an independent hypothesis | **No**: the look-ahead clause fails (Arch-1, Arch-2); m_τ is mis-stated (Arch-3) | REWRITE (text below) |
| 5 | **E5** (RLF-step hypothesis list, steps 4 and 6) | Necessary with E4 | **No**: the step-6 replacement is void (Arch-1); "changes no other step" is false (Arch-2) | REWRITE (text below) |
| 6 | **E8** (ε_1 < 2sin(π/N); the cut controls the N5 backgrounds) | Yes for (SG^{fl}) to be applicable | First clause redundant but harmless (TL-1); second clause must be an event in (SG^{fl})'s domain, **not** a change of χ_Q (SG-2) | ADOPT-WITH-FIX |
| 7 | **E7** (hypercubic tori where W1R-sym gives one shift; no even-torus need for the per-history route) | Only where W1R-sym / GT-lat' (ii) is used | Yes | ADOPT |
| 8 | **E6** (weights) | Bookkeeping | Must follow the rewritten E4/E5: add (CLS-sf) [P], and drop "look-ahead bookkeeping [s]" | ADOPT after the rewrite |

Missing from E1-E8, and needed:
- **E9 (threshold).** Either adopt KN-step's re-centred dichotomy in RLARGE §6 (η_1 := c_1ε_1, citing EXISTENCE RX34-fix 9),
  or replace every "η_1 = c_1ε_1" in PLD §15 by (R3)'s η_1. Today PLD and RLARGE use different η_1.
- **E10 (boundary-adjacent defects).** Name the pricing of RS-generated defects next to ∂Λ(𝔥) (SG-1). e^{B_0} is not a
  price.

**Proposed replacement for E4/E5 (for the integrator; ARGUED by this reviewer, not proven).**

> (PLD)_k is not a hypothesis. Every level-(k+1) defect created at stage k (RS's dichotomy, collar-badness σ_Q = 0) is
> priced in-step by one of three branches.
>
> - **(i) Mismatch:** Lemma KN / RS (R4), unconditional.
> - **(ii) Fluctuation about the background:** (SG^{fl})_k [a clause of (SF)_k's output] and Proposition PLD-desc, on the
>   event V ∈ 𝒱^{sf}.
> - **(iii) Coherent background:** an integrand bound. Under (I_k^E), the stage-k joint main term
>   u_k[Σ_x𝓔_{k,x}(U) + κΦ_k(U, V)] restricted to the cone of a level-(k+1) plaquette P is ≥ u_kc_sf·min{||1 - V_P||², ε_1²}
>   (CLS-sf, cone form; HIST §15, Lemma E-loc the linear case). So a defect cube carries a factor ≤ e^{-u_kc_sfε_1²/C}
>   (resp. ε_loc²) times the integrand with that cube's cone energy removed. That factor enters ℒ_𝔥 directly
>   (Dimock II form), and the removed-cone integrand is the history in which the cube is large-field.
>
> No probability under the per-history law is needed, and no later step is consulted. Hypotheses consumed: (I_k^E) on the
> stage-k small-field domain (the CF preimage is level-k small-field), CLS-sf, (SG^{fl})_k, (BG)_k.

Why this is coherent:
- Branch (iii) sees CF (CF (3); HIST l.408-412).
- It is in-step, because U on the cone is level-k small-field: the CF preimage has curvature ≈ ε_1/L² < ε_1.
- It is the form RLARGE's Proposition CL (c) already uses at the bare level, where Wilson positivity is the energy bound.

What it costs:
- CLS-sf becomes a main-path wall [P]. HIST already names it and reduces it (CLS-red).
- Branch (iii)'s localisation needs 𝓔_{k,x} to be defined near the defect, which HIST does on the small-field domain via
  (SF-bg).
- The removed-cone normalisation must be absorbed by the (HIST) bookkeeping (e^{B_0} per boundary cube), as for any new
  large-field region.

Branches (ii) and (iii) together replace (PLD)_k (i)-(ii), and branch (iii) replaces the look-ahead.

---

# Verdict counts and tally

| Item | Verdict |
|---|---|
| T6: in-place fixes P-1, F-1..F-8, B2, B3, B4, W1R, cosmetic | CONFIRMED (TL-1, S-1 cosmetic) |
| F-9 | CONFIRMED-WITH-FIX (F-9': η_1 identification; also corrects REVIEW_PLD_S1_S2) |
| B6 / E1 text | CONFIRMED-WITH-FIX (E1-a, E1-b) |
| Lemma TL (uncounted) | CONFIRMED (TL-1) |
| (SG^{ph}/net/fl) definitions | CONFIRMED-WITH-FIX (SG-1 boundary scope, SG-2 inter-cube plaquettes) |
| **Counted 1: Lemma HS-net + Proposition PLD-SG** | **CONFIRMED** |
| **Counted 2: Proposition PLD-desc + Proposition INH** | **CONFIRMED-WITH-FIX** (INH-1 threshold, PD-1 strictness) |
| Remark G-IR (uncounted) | (1) CONFIRMED; (2) ARGUED, accepted; headline MIS-AIMED (G-1) |
| Finding 2 "not in-step" | ARGUED (accepted as a method statement; label it) |
| PLD-desc "Reading" / look-ahead / m_τ = 3 | **WRONG as an architecture** (Arch-1, Arch-2, Arch-3; uncounted) |
| §15.4 levels 0-1 | CONFIRMED as a reduction (L0-1 gap numbers) |
| (INF)_k statement; Lemma AZ (uncounted) | CONFIRMED; tally fix INF-1 |
| E1-E8 | E2, E3, E7 adopt; E1, E8 adopt-with-fix; E4, E5 rewrite; E6 after the rewrite; add E9, E10 |
| p3 | PASS as reported (re-run byte-identical) |

**0 GAP and 0 WRONG among the counted items.** The WRONG verdict is on the uncounted architecture reading, which E4-E5
promote into proposed RLARGE text. It is binding there.

**Corrected tally (lane E, session 3):**
- **+2 PROVEN-HERE**, now reviewed: HS-net + PLD-SG; PLD-desc + INH.
- 0 OPEN items closed.
- (INF) recorded as a sufficient condition for (NH-iii) and (NA-R2): **net 0**, not −1.
- No new top-level OPEN item. The architecture change moves the weight from (PLD) [s given SF] to CLS-sf [P], already
  named in HIST, so the main-path OPEN count is unchanged but the weight of RLF-step's large-field pricing rises from s to
  P.

# Binding fixes

1. **B-S3-1 (PLD §15.3 Reading, §15.6 E4-E5, §15.8).** Withdraw the claims:
   - "(PLD)_k at RLARGE's thresholds is an output of steps k, …, k + m_τ";
   - "priced m_τ steps later … changes no other step".
   State Arch-1 (step 6 lies outside PLD-desc's domain) and Arch-2 (CF is unpriced by every in-step branch at every level).
   Replace E4/E5 by the three-branch text of Part 5 (marked ARGUED), or by an explicit OPEN item "pricing of zero-mismatch
   coherent defects".
2. **B-S3-2 (η_1).** Fix F-9' at l.772 and INH-1 at l.1010, 1071, 1077, 1096, 1204, 1259. Recompute m_τ with (R3)'s η_1, or
   adopt KN-step's dichotomy in RLARGE (new E9). Record that REVIEW_PLD_S1_S2 F-9 shared the misidentification.
3. **B-S3-3 (G-IR headline).** Fix G-1. Restrict (SG^{net})'s t-range to the consumed range [θη/(σ²g²), t_1]. Replace "the
   ℓ¹ term is load-bearing" by "Gaussian domination fails at large t for aligned families; the background-field mechanism is
   load-bearing".
4. **B-S3-4 (scope).** SG-1: extend (SG)'s plaquette sets to those with a link in Λ(𝔥), or name the boundary-adjacent
   family (new E10). SG-2: E8's second clause is an event in U inside (SG^{fl})'s domain, not a change of χ_Q.
5. **B-S3-5 (E1).** E1-a: do not edit RLARGE §1 (pre-stated); amend §1A. E1-b: replace "o(1)" by a two-loop-tolerant
   inequality, or by "the chain's own sequence (A5)".
6. **B-S3-6 (bookkeeping).**
   - INF-1: (INF) is a sufficient condition; net 0.
   - L0-1: quote N5-sf0's gap per PROOF l.5322-5325 (RW-ℓ²).
   - PD-1: strict inequality.
   - TL-1: one statement about ε_1 < 2sin(π/N).
   - S-1: the stale "unreviewed"/tally lines in §13, §14.9.
   - F-6: add the structural sentence n_c·a ≳ 4/β_-.
7. **B-S3-7 (B4 note).** The collar-bad family 𝓗^{cb} of §9.1 (β) needs the same three-branch pricing. Coherent cut-good
   backgrounds make σ_Q = 0 on whole regions with zero mismatch and zero fluctuation.

# Recommendation for the RLARGE v2 architecture (the brief's question)

**Neither "in-step (PLD) with look-ahead" nor "(PLD) as a separate inductive hypothesis carried across levels".**
- The first is incoherent. PLD-desc does not reach step 6 (Arch-1), and its cascade ends at a bad coarse cube that is
  priced by nothing in-step at any level (Arch-2, Proposition CF).
- The second assumes the conclusion. The per-history (SG^{net})/(PLD) contains every coarser scale in Λ(𝔥) (G-IR, INH), and
  in torus-wide form it is downstream of A5 (REVIEW_PLD_S1_S2 Part 5).

**Recommended: a three-branch in-step defect price.** For every defect: kernel mismatch (KN/RS, proven); fluctuation
((SG^{fl})_k + PLD-desc, in-step); coherent background (the chain-energy integrand bound from (I_k^E) + CLS-sf in cone form,
into ℒ_𝔥, Dimock form).
- Under this, (PLD)_k disappears as a hypothesis and no look-ahead is needed.
- The new wall is CLS-sf [P]: HIST names it, Lemma E-loc proves its linear case, and CLS-red reduces it.
- **Next session-scale target:** CLS-sf in cone form for the soft chain at small field, i.e. the non-linear Lemma E-loc. It
  decides whether branch (iii) closes.
- The (BG)_k C_I computation that §15.8 recommends is no longer decisive, because no look-ahead depth is needed.
