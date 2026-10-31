# REVIEW_S15_CONVERGENCE: hostile review of session 15, and a convergence audit of sessions 5-15

Reviewer: an independent agent that wrote none of the proof. I edited no other file.

Inputs:
- REVIEW_S13_S14.md (format; its 13 binding fixes).
- `diff PROOF_session14_snapshot.md PROOF_session15_snapshot.md` (465 lines). PROOF.md is byte-identical to the session-15
  snapshot (`cmp` empty). I read PROOF.md by offset: the header l.1-38; EXP-real/EXP-strip/N2-exp l.2640-2712;
  EXP-strip'/N2-exp' l.3077-3114; the (NA) gap l.2942-2958; the [S15] block l.3152-3344; the (DF) sub-DAG l.2031-2099;
  §0 l.379-408; L6 l.3346-3367; the tallies l.4321-4540.
- RTARGET.md §32-37; LOG.md sessions 5-15; REVIEW_S5_S6 to REVIEW_S13_S14 (their verdict and tally lines).
- checks/c30_criteria.md, c30_sources.py, c30_time.txt, the stored c30A-D outputs and time files.

Scratch work is in the scratchpad `rev15/`:
- `my_strip.py` and `my_strip2.py`: my own mpmath (30-digit) implementation of the η_* and η'_* conditions, written from
  the PROOF text (l.2656-2702 and l.3078-3114), not from c30;
- `elow.py`: a chain-level sanity check of Lemma E-low;
- the c30 re-run outputs.

---

# JOB 1: hostile review of session 15

## Bottom line

- **All 13 R1314 fixes are applied correctly.** Two trivial residues are left in the LOG (l.666 "0.0118", l.700 "0.0385").
  Those lines are historical and no fix named them.
- **The strip constants are right.**
  - My own re-implementation reproduces c30 A's ratios to every printed digit at five pairs.
  - The superseded pairs fail, as the previous review said.
- **No counted session-15 item is WRONG or a GAP.**
  - Lemma LES-div is CONFIRMED.
  - Theorem G♯_0-soft (with SRC-all, REC, KF) is CONFIRMED-WITH-FIX: two sentences are argued, not proven, and must be
    labelled.
  - Proposition NA-lev (with E-low) is CONFIRMED-WITH-FIX: its headline overclaims. The k-uniformity has not gone away; it
    has moved into (NA-H).
- **c30 re-runs identically** in all four parts.
- **Corrected tally: 63 / 2 / 7 / 24 + 1, as claimed.**
  - The count is accurate under the ledger's convention.
  - But that convention hides the growth of open leaves under the active nodes. Job 2 measures that growth.

## [R1314-fix] audit (REVIEW_S13_S14 binding fixes 1-13)

| # | Fix | Where now | Verdict |
|---|---|---|---|
| 1 | Residues: "levels n ≥ 1"; S12 "non-analytic part" annotated | l.676-677; l.120-122 | Applied |
| 2 | N2-exp valid pairs; f_0 condition in the definition of η_* and in the script | l.2701-2712; header l.7-9; c30 A | Applied. I recomputed it (below). The κ̂ = 16 value 0.0083 → 0.0082 is an extra correction the session found itself (bisection 0.00826, which I confirm) |
| 3 | Periodicity: periodic-meromorphic + Riemann extension | l.2720-2726 | Applied; the argument is correct (2π-translates of S_η(Q) cover the strip; a locally bounded meromorphic function is holomorphic) |
| 4 | N2-exp' valid pairs | l.3115-3120; header l.68-69; RTARGET annotation after §36 | Applied. I recomputed it (below) |
| 5 | "true rate" → "located rate"; fit ranges | l.92, 681, 2777-2779; LOG l.667 | Applied; no "true rate" is left outside the fix notes |
| 6 | "What N6 consumes" ARGUED; F-df_0 OPEN | l.2747-2758; tally | Applied |
| 7 | NA-alg (b): ‖ρ‖_op < 2π/N | l.2842-2845, 2868 | Applied. It gives \|Σθ_j\| < 2π with Σθ_j ∈ 2πZ, so tr ρ = 0. Correct |
| 8 | NA-FP at the Hessian level; composite covariance; onto-ness | header l.59-61; l.2887-2890; l.2925-2941 | Applied. The covariance derivation (left-trivialised derivative, nested centres) is right. The onto-ness through the factorisation M^{(k)} = ∏M_{V^{(m)}} is right: y = c_Y + e_1 is reached by a single link under every S4' ordering, and it is no level-1 centre. CONFIRMED |
| 9 | SRC-id f_0 half written out; c30 B | l.2985-2996 | Applied. I re-derived both lines: δ/β = (1 - φR/β)/a turns the second curl term into -(S/Ψ)φν_ρν_σ(R_ρ/β_ρ - R_σ/β_σ). Correct |
| 10 | (FP♯') combined map + NA-crit'; norms | l.3026-3038 | Applied. The NA-crit' Lagrange proof is right: it needs Dh(x) onto (regular slice) and S invariant on all of 𝒳, both stated |
| 11 | BNA-F2 "argued" | header l.48-49; LOG l.693 | Applied |
| 12 | RTARGET §32: annotation, not edit | RTARGET l.639-649 | Applied (l.562 and l.567 are unedited) |
| 13 | c29 tolerance record | checks/c29_time.txt tail | Applied |

## Independent recomputation of the strip constants (my code, from the PROOF text)

| Pair (κ, κ̂, η, r_0) | Result | Binding ratios |
|---|---|---|
| N2-exp (1, 1, 0.0111, 0.57) | all hold | br_V 1.0341, e_Ψ/(Ψ_U/2) 0.9581, f_0 0.1261 |
| N2-exp (4, 16, 0.0082, 0.60) | all hold | br_V 1.0244, e_Ψ 0.9908; bisection η = 0.008256 |
| N2-exp (0.25, 1, 0.0077, 0.37) | all hold | br_V 1.0517, f_0 0.1350 |
| N2-exp (4, 16, 0.0083, 0.60) (old) | **fails** | e_Ψ 1.0072 |
| N2-exp (1, 1, 0.0111, 0.55) (old) | **fails** | br_V 0.9979 |
| N2-exp' (1, 1, 0.0384, 0.70) | all hold | br'_V/req 1.0120, Ψ_L 0.1115 |
| N2-exp' (4, 1, 0.0306, 0.90) | all hold | 1.0275 |
| N2-exp' (1, 16, 0.0226, 0.47) | all hold | 1.0304 |
| N2-exp' (1, 1, 0.0385, 0.70), (4, 1, 0.0307, 0.90) (old) | **fail** | 0.9891, 0.9931 |

Every ratio agrees with c30 A's print to all digits. **CONFIRMED.** The margins are thin (bisection margins +0.00004 to
+0.00073). That is expected for constants defined by inequalities at a chosen r_0; it is not a defect.

## Session-15 PROVEN-HERE items

### Lemma SRC-all: CONFIRMED
- **Euler-Lagrange equations.** I re-derived them: d*dB_0 + Q_0^Ts_0 = j_0, and s_{i-1} = Q_i^Ts_i - j_i, with s_i = κ_ir_i.
- **Unrolling.**
  - (i) follows by unrolling, with transposed composites from level l to level i + 1.
  - (ii) follows by inserting (i) at i = 0.
- **(iii), the telescoping.** B_k = Q^{(0→k)}B_0 - Σκ_i^{-1}Q^{(i+1→k)}s_i, so B_k + Ps ≡ g_eff mod Closed.
  - The signs of both source terms of g_eff are right.
  - The zero-mean step is right.
- c30 C1/C2 re-run: ≤ 1.6e-10.

### Lemma REC: CONFIRMED
- Take the symmetric form ℰ with its top components.
- At criticality, ℰ(B, δ) = Σ⟨j_l, δ_l⟩ - κ_{k-1}⟨r_{k-1}, δ_k⟩ (r_{k-1} = Q B_{k-1} - B_k, so the sign is right), and
  ℰ(B', δ) = 0 for δ_k = 0. Symmetry gives the identity.
- Gauge invariance of d_lB'_l makes the choice of critical B' immaterial.
- c30 C3 re-run: ≤ 4.3e-9.

### Lemma KF: CONFIRMED
- **Pointwise bounds.** The kernel of a transposed non-negative averaging is bounded pointwise by (row sum) × max over
  the support. Q_str^T has row sums L^{-3} (J-str (c)), and its support shifts by ≤ 4.5. So
  |K_{r_i}| ≤ κ̂L^{-3(k-1-i)}Me^{4.5m'}e^{-m'd}.
- **The ϱ_i bookkeeping.** The factor L^{2(k-1-i)} turns this into L^{-(k-1-i)}. The sum Σ_{i<l}L^{-(k-1-i)} ≤
  (3/2)L^{-(k-l)} ≤ 3/2.
- **The exponent.** The total is e^{1.5m'}·e^{6m'}·(1 + 6κ̂) ≤ e^{8m'}(1 + 6κ̂). Correct.

### Theorem G♯_0-soft: CONFIRMED-WITH-FIX
- **Data part.** The torus periodisation, plus w(X) ≤ w(Y)e^{md}, gives 4MS(μ). Correct.
- **Source part.** By REC, r = κ^{-1}Σ_lΣ_PL^{-2(k-l)}K_{f_l}G_l, with G_l = L^{-2(k-l)}G^c_l.
  - The plaquette count per coarse cell is 6L^{4(k-l)}, so the L-powers cancel exactly: one O(1) per level.
  - Σ_l ≤ Ω·max_lω_l‖G_l‖.
  - Uniform in k, T and X_0. The (G0-F1) marginal count is real and is handled honestly by Ω < ∞.
- **(b).** Q^Td^* = d^*W^T with ‖W^T‖_{∞→∞} = L^{-2} per step, and |d^*H| ≤ 6max|H|.
  - The level powers: L^{2(k-1-i)}·L^{-2(l-1-i)}·L^{-2(k-l)} = 1. Correct.
  - c30 D (d = 4, k = 2, level-1 source): 4.64 against the proven 6. Consistent.
  - (The d = 2 rows of D, 5.72 at k = 3, are outside the theorem, since the L-power cancellation is d = 4 specific.)
- **Fix 1 (label).** "the bound is attained in order of magnitude by sources coherent at the coarse scale" (l.3223) is
  asserted, not shown. Label it argued, or exhibit the source.
- **Fix 2 (label).** "which is what the soft remainders at levels l ≥ 1 provide (BNA-F2 …)" is argued (it rests on BNA-F2,
  which is argued). The theorem itself is unconditional in ω, so only the sentence needs the label.
- **Scope (correct, but it must stay visible).** This is the easiest third of (G♯)_0: the gauge-invariant soft outputs at
  the trivial abelian background. B-NA-red consumes (G♯_0-field), which was not attempted.

### Lemma LES-div: CONFIRMED
- **Energy step.** Test with w. Summation by parts moves ∂^- onto w, and Dirichlet Poincaré gives
  ‖∇w‖_2 ≤ ‖g - ḡ‖_2 + Cr‖h‖_2, so ‖∇w‖² ≤ C(r^{4+2α}[g]² + r^6H_0²).
- **Harmonic decay.** The decay exponent d + 2 = 6 is the right one.
- **Iteration.** The iteration lemma with a = 6 > b = 4 + 2α gives the stated inequality. I checked both of its
  conversions: ρ^{-4}ρ^{4+2α}[g]² = (ρ/R)^{2α}R^{2α}[g]², and ρ^{2α}R^{2-2α}H_0² = (ρ/R)^{2α}R²H_0².
- **Constants.** They are absolute and not computed, as in LES. This is standard. Its use in the (G♯_0-fine) reduction at
  R = n needs n ≥ 16, i.e. k ≥ 3 at L = 3. The finitely many small k are trivially finite-dimensional, but the text should
  say so.

### Proposition NA-lev with Lemma E-low: CONFIRMED-WITH-FIX (scope of the headline)
- **(a) defect bound.**
  - The inequality is correct. I verified p_L = 5L - 4 against c26's `template`: at most 4·(L-1)/2 axial links out, L
    along μ, and at most 4·(L-1)/2 back, so 11 at L = 3.
  - The multiplicity is crude: per coarse link, a fine link lies in N(X, μ) for at most 8 pairs (X, μ), since templates
    stay in blocks X and X + μ. So the stated 81 holds under either indexing, by site or by link.
  - **Fix (wording).** State whether Def is indexed by coarse sites or by coarse links. The text says "coarse sites", but the
    soft term lives on coarse links.
- **E-low: CONFIRMED.**
  - The dual formula and the Lagrange identity give min_t|b̂ - νt|² = |F̂|²/ψ.
  - P̂^{-1} = φ/β; β ≤ κ + 4π²R̄ (φ ≤ |x|² ≤ 4π² on Q); φ/ψ ≥ 4/π².
  - R̄ = 1 + 1/8 + 1/9 = 1.2361 gives **c_E = 0.004069**, as stated.
  - My chain-level check (`elow.py`, c26 chains, d = 4: (T, k) = (3, 1), (2, 2), random and Fourier data): min E_k/‖dB_k‖² =
    0.058 and 0.047, both ≥ c_E. The bound is valid and about 11× loose.
- **(c): CONFIRMED** given PG at n = L.
- **The headline overclaims.** "NA-F2 is an artefact of the direct n = L^k step" and "it is no longer an n-uniformity
  problem" (header l.29-33; l.3292, l.3317) go too far.
  - It is correct that N4's per-step fluctuation operator is the one-level operator, with contours of ≤ 5L - 4 links, and
    that its top-level defect has no n-loss.
  - But E_i^{NA} is the Schur complement over all i finer levels of the SU(N) chain. Its Hessian contains a soft defect of
    the same type at every finer level.
  - So the multi-level uniformity has not disappeared. It is now (NA-H), which is B-NA, the hardest open item on the N2
    side.
  - **Fix:** "the top-level per-step defect has no n-loss; the multi-level uniformity is carried by (NA-H) ⊂ B-NA".
- **Record the explicit smallness.** With δ_H = 0 and κ ≡ 1, the stated condition (κ_i/2)L²·81p_L(e^{2η̄} - 1)² ≤
  ½min(c_E, κ_i/4)c_1 needs **η̄ ≲ 1.9·10⁻⁷**. By the argued Stokes bound, that is a background plaquette angle ≲ 1.6·10⁻⁸
  in level-i units.
  - It is uniform, so it is not a defect.
  - But it shows that the PG constant c_1 = 1/(3.5·10⁶) sets the small-field threshold. Write the number down.

## Uncounted items

- **(G♯_0-fine) reduction: CONFIRMED-WITH-FIX.**
  - The n-cancellations are right (n^{2+α}·n^{1-α}·L^{-3k} = 1).
  - The roughness of the transported coarse sources is correctly identified.
  - Two fixes:
    - the k ≥ 3 caveat above;
    - (G♯_0-fine-up) is named, but not stated precisely ("the curvature response at level l_min").
- **RTARGET §37 "the acceptable partial outcome is met": CONFIRMED-WITH-FIX.**
  - It is met for level-0 sources.
  - For sources at levels ≥ 1 the remaining input is named but not precisely stated, which §33's partial outcome requires.
  - Annotate as before. Do not edit the line.
- **(R♯_ω): CONFIRMED as a precise statement; its proof is argued (honestly labelled).**
  - The quadratic bound in weighted sup norms is well-posed, since w ≥ 1.
  - It depends on Lemma G♯_0-plain (OPEN), so it is not independent of the linear side.
- **Lemma NA-crit' and the composite steps:** CONFIRMED (table above).

## c30 (re-run)

Setup: laptop, nice 10, OPENBLAS/OMP/MKL/vecLib threads = 1, PYTHONDONTWRITEBYTECODE = 1, sequential runs, no `timeout`,
load 2.3-3.1, 41% free.

| Part | Result | Time | Peak RSS | vs stored |
|---|---|---|---|---|
| A | PASS (11 pairs) | 0.5 s | 65 MB | identical except timing |
| B | PASS (B1-B3 ≤ 5.2e-13) | 0.7 s | 97 MB | identical except timing |
| C | PASS (V1, C1-C4; C3 4.3e-9) | 7.0 s | 508 MB | identical except timing |
| D | informational | 2.5 s | 442 MB | identical except timing |

Procedure:
- The criteria were written before the script, and the one pre-script C4 correction is disclosed.
- No tolerance was added. This is the first check file to follow REVIEW_S13_S14 fix 13 cleanly.
- The run without -I is disclosed (as for c29).
- C4 is vacuous at k = 1 (disclosed).
- **c30 does not test Lemma E-low**, which is a new counted constant. Add an E-low instance to c31; mine is in `rev15/`.

## Verdict counts and tally

- **Counted [S15] PROVEN-HERE items: 3.**
  - CONFIRMED: Lemma LES-div.
  - CONFIRMED-WITH-FIX: Theorem G♯_0-soft (two "argued" labels); Proposition NA-lev (headline scope, Def indexing,
    explicit smallness).
  - Sub-lemmas counted with them: SRC-all, REC, KF and E-low are CONFIRMED.
  - **0 GAP, 0 WRONG.**
- **Uncounted.** NA-crit' and the composite NA-FP steps: CONFIRMED. The (G♯_0-fine) reduction, RTARGET §37, and the "no
  longer an n-uniformity problem" sentence: CONFIRMED-WITH-FIX (wording). (R♯_ω): a precise statement, argued.
- **Corrected tally: 63 PROVEN-HERE / 2 IMPORTED-AND-REVERIFIED / 7 IMPORTED-NOT-YET-REVERIFIED / 24 OPEN (main path)
  + 1 comparison branch. Unchanged from the claim.**

## Required fixes (binding for session 16)

1. G♯_0-soft: label as argued the "attained by coherent sources" sentence and the "supplied by the soft remainders"
   sentence.
2. NA-lev: replace the headline (header l.29-33, l.3292, l.3317, LOG l.729, RTARGET §37) with: "the top-level per-step
   defect has no n-loss; the multi-level uniformity is carried by (NA-H) ⊂ B-NA". State the indexing of Def. Record
   η̄ ≲ 1.9·10⁻⁷ (κ ≡ 1, δ_H = 0) as the explicit smallness.
3. The (G♯_0-fine) reduction: note n ≥ 16 (k ≥ 3 at L = 3) for LES-div at R = n, and state (G♯_0-fine-up) as a displayed
   inequality.
4. RTARGET §37: annotate "met for level-0 sources; (G♯_0-fine-up) named, not yet stated".
5. c31: add a Lemma E-low instance.
6. Optional: annotate LOG l.666 and l.700 with the corrected values.

---

# JOB 2: convergence audit, sessions 5-15

## (a) Per-session ledger

How to read the table:
- "Top-level" means the 24-item OPEN tally.
- "Leaves" means the named open sub-obligations under the active nodes N2/N4/N5/N6 of the (DF) sub-DAG, counted from the
  tally's "narrowed content" lines.
- Classes: **R** = a genuine refinement (smaller, precisely stated); **L** = lateral (a new obligation beside the old one,
  or created by a convention or review); **D** = a duplicate or relabelling of an existing obligation.

| S | PROVEN | OPEN (top) | Closed | Opened (class) | Leaves on N2/N4/N5/N6 |
|---|---|---|---|---|---|
| 5 | 30→34 | 21→22 | — | A1-NA (R); E8** relabelled as an import target (D) | — |
| 6 | 34→39 | 22→21 | A1-NA (as A1-NA(1)) | LF-count shows a large-field R-operation is mandatory in d = 4: a major genuine finding, recorded inside L5, uncounted (R) | — |
| 7 | 39→40 | 21→23 | — | L1e-(0.4) from review (L); R4D-iso (R); walls W1-W3 named inside L5 (R) | — |
| 8 | 40→43 | 23 | R4D-iso | W1-loc (R) | — |
| 9 | 43→46 | 23→24→23 | L1e-(0.4) and W3 moved to the comparison branch by decision 4 | BG-reg from review (R: a missing hypothesis). **Decision 4 turns the six hard imports into re-derivation obligations, uncounted (L)** | — |
| 10 | 46→49 | 23 | Thm 27 import → Theorem CE | (DF) sub-DAG: 11 open nodes, uncounted (R) | 10 |
| 11 | 49→53 | 23→24 | FP identity (abelian) | D4-obs from review (L; created by decision 4); (LED), physical gap (R) | 8 |
| 12 | 53→55 | 24 | (LED) (linear), physical gap | N10 complex-data decay (R); (IT') (L: composite root map) | 7 |
| 13 | 55→57 | 24 | decay (N2-exp), (IT') | none substantive | **6** |
| 14 | 57→60 | 24 | NA identity (Hessian level) | (G♯), (R♯), (FP♯) (R); (NA) gap (R); FP_U(V) background dependence (L); curvature localisation (L) | 10 |
| 15 | 60→63 | 24 | G♯_0-soft; NA-F2 at the top level | LED-src (R); G♯_0-field (R, pre-stated); R♯_ω (R); per-block perturbation (R); G♯_0-fine-up (L: soft multi-level sources); G♯_0-plain (L: needed only for R♯'s plain current); F-df_0 (L, review); NA-H (D: a sub-statement of B-NA) | **14** |

What the table shows:

1. **The flat OPEN count is an artefact of the counting convention, not evidence of circling.**
   - About 17 of the 24 top-level items have not been touched since session 4: E7.0'(-TV, -AF), L7b, L7c, L8d, L9b-d,
     L10, F2-F4, C1-C4 and L3g-ob. They lie on the T_OS / QCD path, not the UV-stability path.
   - The three active nodes (BG-reg, the L3g(a)-slice completion, W1-loc) can only close when a whole SU(N) package
     closes.
   - So the top-level count could not have moved, whatever the sessions did.
2. **The honest measure is the leaf count. It is U-shaped: 10 → 8 → 7 → 6 → 10 → 14.**
   - In the linear abelian regime (S11-S13) the lane converged. Leaves fell, and every closed item stayed closed. Four
     reviews in a row found 0 WRONG and 0 GAP among the counted items.
   - On entering SU(N) (S14-S15) the front fans out: (G♯) alone became 5 leaves, of which 1 is closed.
3. **Reviews add about one lateral obligation per review:** L1e-(0.4), BG-reg, D4-obs, F-df_0. Each one was correct to add.
4. **N5 and N6 have not been worked on since session 10.** The only change is N6's block-size number, M ≳ 1.2·10⁴.
   W2 (nested multi-scale large fields) has never been attacked. LF-count (S6) shows the large-field R-operation cannot be
   avoided in d = 4.

## (b) The current critical path to UV stability of 4D SU(N) on the soft RG

Target: L6-soft, exp(-E_-|T|) ≤ Z_K/Z_ref ≤ exp(E_+|T|) uniformly in K, for the decision-4 kernel. Under decision 4, every
hard-constraint import becomes a node to derive. **P** marks a paper-scale node: about one Balaban-sized CMP paper, the
size given in brackets. **s** marks a session-scale node: one to three sessions.

```
L6-soft (UV stability) ⇐ A (small-field package, every scale) + B (large-field R-operation) + C (assembly)
A. small field
 ├─ A1  N2 = BG-reg, the SU(N) soft background field: existence, uniqueness, regularity, decay, analyticity
 │      [P: CMP 102 + parts of CMP 99]
 │      ⇐ B-NA-red (PROVEN as an implication)
 │        ├─ (G♯_0-field)        s-s: ⇐ G♯_0-soft ✓, (G♯_0-fine) ⇐ LED-src (s), G♯_0-fine-up (s), multi-level
 │        │                       per-level-slice gap (s)
 │        ├─ (R♯_ω)              s: ⇐ G♯_0-plain (s); marginal 4D Wilson remainder
 │        └─ (FP♯')              s
 │      + N10 non-linear analytic dependence on complex data   [s to P]
 │      + F-df_0 / curvature localisation                       [s]
 ├─ A2  N4 (NA) gap   ⇐ NA-H (⊂ A1) + per-block perturbation (s); FP_U(V) locality/analyticity [s to P]
 ├─ A3  N5 soft covariance at general backgrounds: ℓ², ℓ¹, random-walk expansion with complex s-weakening
 │      [P: CMP 95/96/99 propagators]   (untouched since S10)
 ├─ A4  N6 polymer bound / localisation for the soft kernel, rate κ > 457 in M-units with M ≳ 1.2·10⁴
 │      [P: CMP 116]   (untouched)
 ├─ A5  L4a-flow: coupling flow over all scales, β-function control   [P: CMP 109 Thm 2 (deferred) / CMP 119]
 └─ A6  N7-N9 (DF1-3'), L1d-soft                         [s each, after A1-A4]
B. large field (L5-soft)
 ├─ R4D-iso / D4-norm (PROVEN: isolated cube)
 ├─ W1-loc ⇐ N11, N12 ⇐ A                                 [s each, given A]
 └─ W2 nested multi-scale large fields; renormalising large-field regions (LF-count forces it)
        [P×2: CMP 122 I + II]   (never attacked)
C. assembly: per-step bounds → bulk bound; E8** as a corollary   [P: CMP 119]
(off the UV-stability path: D4-obs; all of L7-L10, F2-F4, C1-C4, E7.0')
```

**Size of the critical path.**
- **Paper-scale nodes: 6-7.**
  - A1, the SU(N) background-field theorem. Its session-scale leaves add up to a paper.
  - A3, the propagators and the random walk.
  - A4, the cluster expansion and localisation.
  - A5, the flow.
  - B-W2, the R-operation, which is 2 papers.
  - C, the assembly. It may share a paper with A5.
- **Session-scale nodes: about 15-18.** LED-src, G♯_0-fine-up, the multi-level gap, G♯_0-field, G♯_0-plain, R♯_ω, FP♯',
  NA-H's per-block part, F-df_0, FP_U(V), N7, N8, N9, N11, N12, L1d-soft, and possibly N10.

**What 11 sessions bought, in Balaban units.**
- The linearised abelian trivial-background content of the soft chain: N2-lin, N2-exp, PG, PG^{(k)}, FP-ab, G♯_0-soft.
  This is a correct, clean analogue of the U = 1 parts of CMP 95/96.
- A d = 4 re-proof of Dimock's abstract polymer theorem (Theorem CE).
- The isolated-cube R-step (R4D-iso / D4-norm).
- Roughly one paper-equivalent in all, and the easiest one: linear, translation-invariant and symbol-level. **None of the six
  remaining paper-scale nodes has been entered, except A1 through reductions.**

## (c) Verdict

**Converging slowly but honestly on the linear sub-problem. Fanning out on the non-linear front. Not measurably converging
on the main theorem.**
- **Honest.** No counted item has been WRONG since session 9. The fixes are applied faithfully. Pre-registration is
  disciplined, the checks re-run bit-for-bit, and the failures are recorded.
- **Slow.** At about one easy paper-equivalent per 11 sessions, the six harder paper-scale nodes extrapolate to well over
  60 sessions. Two facts make that an underestimate:
  - the non-linear and large-field nodes do not decompose into 2-4 independent session lemmas the way the linear symbols
    did. They are coupled inductive estimates with shared constants;
  - the leaf count has risen in each of the two sessions since the lane entered SU(N).
- **Not circling.** Circling would mean re-proving or re-opening closed items, and that has not happened. The lane is
  walking down a tree whose remaining branches are each paper-sized.

**Decision 4: locally helpful, globally multiplying.**
- **Helps.**
  - W3 (hard-constraint fibre smoothness) and L1e-(0.4) leave the main path.
  - R4D-iso holds for the exact normalised soft step (D4-norm).
  - The linear soft chain has a clean analytic structure: P̂ = β/φ screening, with a decay rate set by the soft
    constraint's mass √κ.
- **Multiplies.**
  - **The decisive cost.** All six hard imports (L1d, L2, L3g, L4a, L5, L6) change from "re-verify Balaban" to "re-derive
    a Balaban analogue". This forfeits the import option for exactly the papers not yet read (CMP 116, 119, 122 I-II),
    which are the hardest.
  - Soft-specific obligations that Balaban's constrained minimiser does not have: residual currents at every level (SRC-all,
    the Ω marginal count, G♯_0-fine-up, G♯_0-plain) and D4-obs.
  - The S4' funnel items (J-str, IT, PG-line) are not soft-specific: B-avg shows Balaban's (0.4) with diagonal pairing is
    S4'.
- **Governance point for the lead (not a ruling).**
  - The lead's memory file `project_openai_ym_writeup_watch_2026_10_26.md` records the owner's order as "Balaban Z^4
    standard first, then D4".
  - Decision 4 put a non-standard kernel first.
  - Nothing found here says the soft kernel is wrong. It is simply not the cheapest road to the stated target.

## (d) Recommendation: RE-PLAN

**The plan.**
1. **Gate (owner action, now).** Obtain CMP 102, 116, 119 and 122 I-II.
   - The standing request goes back to session 5.
   - Project Euclid is bot-blocked, and the lane rightly did not bypass it.
   - Every remaining paper-scale node is the content of these papers, on either branch.
2. **Finish the linear package (≤ 2 sessions), then stop adding to it.**
   - Prove LED-src and the multi-level per-level-slice gap, giving (G♯_0-fine) for level-0 sources and (G♯_0-field).
   - Write them up as one self-contained proposition: k-uniform exponential locality plus the Schauder bounds of the
     linearised soft RG at the trivial background.
   - Defer G♯_0-fine-up and G♯_0-plain.
3. **Decision-4 cost audit and transfer attempt (1 session).**
   - For each of L1d, L2, L3g, L4a, L5, L6, list where Balaban's proof uses δ(Q U V^{-1}) and what changes under the soft
     kernel.
   - Attempt a **soft-to-hard transfer lemma**: write the normalised soft kernel as the hard constraint composed with an
     ultralocal gauge-covariant smearing of V, i.e. one extra ultralocal fluctuation field per level, which Dimock-type
     machinery absorbs.
   - Outcomes:
     - (a) the transfer holds: keep soft and import the hard-branch results after re-verification;
     - (b) it fails: move the main path back to Balaban's (0.4) with diagonal pairing (= S4', B-avg), and keep the soft
       lemmas as tools;
     - (c) keep soft and re-derive, only if the audit finds a soft-specific simplification in L5 / CMP 122.
4. **When the papers arrive: run a re-verification lane, risk first.**
   - First, scope CMP 122 I-II (W2, the R-operation), since LF-count makes it unavoidable and it is the least-exposited
     part of Balaban.
   - Then CMP 116 → 119 at one paper per 1-2 reading sessions, re-verifying on our structures, with the owner's
     independence requirement met by line-by-line re-derivation of each used step, not by building a different RG.
5. **Process.**
   - Replace the 24-item OPEN tally as the progress metric with this critical-path DAG, carrying P/s weights and leaf counts.
   - Keep the hostile reviews, but scope them to load-bearing items (a 13-fix list costs about a third of each session).

**Expected value of each option (my judgement, not a computation).**
- **Continue as is** (top 3 targets: LED-src, G♯_0-field, NA-H).
  - Likely closes (G♯)_0 in 2-4 sessions (≈ 60%). That is real but local.
  - P(UV stability on the soft RG within about 30 more sessions) ≲ 5%.
  - Leaf fan-out is likely to continue, since NA-H is B-NA itself.
- **Re-plan (recommended).**
  - Costs 1-3 sessions of redirection, and banks the linear package as a deliverable.
  - If step 3 gives (a) or (b), the hardest remaining nodes change from derivation (unbounded risk) to verification
    (bounded, about 1-2 sessions per paper).
  - P(a re-verified UV-stability ledger within about 30 sessions | papers arrive) ≈ 15-25%. Most of the risk is in
    CMP 122.
- **Pause pending the papers.**
  - Zero cost, but zero progress, and it forfeits the 2-session finish of the linear package.
  - It is dominated by the re-plan, which contains the pause (steps 1 and 4) and does the cheap high-value items while it
    waits.
