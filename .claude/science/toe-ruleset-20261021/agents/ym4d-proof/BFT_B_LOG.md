# BFT_B_LOG (BFT lane B: BFT-3 locality, BFT-4 branch-action class)

## Session 1, 2026-10-28 UTC
- 04:3x-04:52 Read (read-only): REVIEW_S22 (all); PROOF [S18]-[S22] (l.5145-6368); LINEAR_PACKAGE §1.3-1.4, 3.8, 4, 6.2;
  SF §6.1, §7.1; FLOW §4 (SF-bg); RLARGE §3.2 ((BG)_k); HIST §14.2 (Lemma HF); c37/c38 scripts (structure only).
- 04:52:52 timestamp; ≈04:53 BFT_B.md §0-§1 (pre-stated lemmas) written in one write.
- 04:54:32 checks/bb1_criteria.md (mtime). Then checks/bb1_decay.py (imports c37_kcurv unchanged).
- 04:55:13-04:56:36 bb1 A, B under the numeric lock (one acquisition; load1 3.00, free 40%; peaks 582/562 MB).
  A1 PASS, **A2 FAIL** (Z_col 156.687 vs c37's 156.079), A3 PASS, B informational.
- 05:02:12-05:02:43 post-hoc diagnostic checks/bb1_diag.py (added after reading A2; not a criterion; second lock
  acquisition; 616 MB): c37 D2's Z_col is a float32 accumulation artefact (value 156.6868). A2's verdict stays FAIL.
- 05:05 BFT_B.md §2 (proofs) appended in one write; 05:07 §1/§2 header timestamps corrected (the §1 header had a guessed
  "04:53-05:10"); 05:07-05:08 §3 (check record), §4 (outcome), FOR OTHER FILES.
- 05:09 **Self-correction:** the first versions of "Lemma BB-mix ⇒ bound" and "Proposition BB-mix-gap" counted polymers as
  unconstrained subsets of a ball and claimed that max-type decay plus Cauchy always diverges; false (polymers are
  *-connected, lattice animals grow only exponentially). Rewritten: what BFT-4 needs is per-cube smallness K < e^{-m_0}/(80e)
  beyond compact clusters; the mass-interpolation Cauchy route loses the condition number S/γ. Marked [post-proof
  correction] in place.
- No process left running; lock directory removed by each runner (rmdir once per acquisition). No commits, PRs, pushes,
  CL or axiom edits; only BFT_B.md, BFT_B_LOG.md, checks/bb1* written.

### Results by name
- PROVEN-HERE: BB-geo, BB-C, BB-IFT, BB-MCT (solid norms), BB-NL, **Theorem BB-3_1 (BFT-3 at k = 1, all orders, every
  curvature-small real/complex background)**, BB-E1, back-substitution identity Ξ_{j←k} = ζ_j⋯ζ_{k-1} + telescoping,
  **Construction BB-loc (a)-(d) at k = 1 (exact gauge-invariant polymer decomposition)**, BB-mix-gap, BB-env.
- PROVEN as an implication: BB-3_k (⇐ BFT-0/2 + (H-𝔊_w)), BB-mix ⇒ bound, BB-4-ind, **Corollary BB-4c (BFT-4 ⇒ C_♭, (H-G),
  (I_i) level-uniform, no θ-cascade; NAH-unif′ ⇐ (H-K) + BFT-2 + BFT-4; BFT-3 E-part all n)**.
- ARGUED: (LEG_w) for tower potentials. OPEN: (H-𝔊_w) for k ≥ 2, (H-op), (BB-mix), (O1)-(O4) of BB-4-ind.
- Failure modes: B3-F1, B3-F2, B3-F3 OCCUR (absolute/solid-norm estimates); B4-F1: BB-4-ind's contraction fails in the
  polydisc-sup norm at quadratic order [power count; inference].

## Session 2, 2026-10-28 UTC
- 05:2x-05:42 Read (read-only): REVIEW_BFT_B_S1 (all, binding), BFT_B.md (all), BFT_B_LOG, REVIEW_BFT_A_S1 (all), BFT_A §1, §2,
  §3.9-3.11, FLOW §3-§5.4 (F-tree, F-ren, L4a-Π use), REVIEW_S22 Part 5 (BFT statement), PROOF L4a-Π (l.1181-1225), Theorem RW
  (l.5346-5385), N5-sf0 (l.5415-5476), N5-an♭ + BR1 (l.5648-5705); checks/bb1_decay.py, c37_kcurv.py l.1-135.
- 05:42:06 `TZ=UTC stat`: BFT_B.md born 05:10:26 mod 05:10:26 size 53232 (session-1 state). Step 1 (the 11 binding fixes,
  tagged [RBB1-fix]) starts now; edits are in place, so the session-1 text they replace is recoverable only from
  REVIEW_BFT_B_S1's quotations.
- 05:42-05:45:38 Step 1: all 11 binding fixes applied in place, tagged [RBB1-fix …] (41 tags): B1-1 (μ_1 ≈ 2.4·10⁻¹¹,
  Lμ_1 ≈ 7.2·10⁻¹¹), B1-2/3/4 + BB-geo star line + scope (tori only), B-NL-1, B3k-1/2/3 (+ telescoping marked per-level
  alternative), B4-1/B4-2 ((H-𝔊_w) = lane A's (H-lin^∇)_m + (H-rem^∇)_m; (LEG_w) = lane A's data-map row), B3F1-1, B3F2-1 (NOT
  ESTABLISHED; "⊂ BFT-4" removed everywhere), B-loc-1/2 (E_∅ = L^{2k}S_W; general-k clause withdrawn), B-mix-1/2/3 (§1.4
  marked superseded; K ≈ Ce^{-μM_c/2^d}; BB-mix-gap (2) ARGUED route NO-GO), B4i-1/2/3, B4c-1/2, B-bb1-1/2 (ℓ¹ rate 0.5-1),
  BB-E1 Balaban convention. One self-correction during step 1: the B-mix-3 tag first said "a family with a large radius is
  constructed in §5"; §5 did not exist yet, so it was reworded (same minute) to "is the subject of session 2's §5".
- 05:45:38 `TZ=UTC stat` BFT_B.md: born 05:45:09 (the Edit tool rewrites the file, so APFS birth time moves) mod 05:45:38
  size 69328.
- 05:49:21 §5 "PRE-STATED (session 2)" appended in one write (statements only: BB-W, BB-sm, Theorem BB-4♮, check bb2's
  criterion summary, BB-mix-wall, Construction BB-bond, Theorem BB-mix′_1, BB-mix-k). `TZ=UTC stat` BFT_B.md: mod 05:49:21
  size 76562. No proof, criteria file or script of session 2 exists before this time.
- 05:50:12 checks/bb2_criteria.md (born = mod 05:50:12); then checks/bb2_symbol.py (imports bb1_decay.build and c37 helpers
  unchanged). 05:50:5x runner scratchpad bb/run_bb2.sh started in the background; the numeric lock directory was already
  held (another session), so it waits in the `until mkdir` loop.
- 05:51:32-05:51:34 bb2 under the numeric lock (one acquisition; load1 5.68, memory free 50%; 2.1 s wall, peak 560 MB;
  rmdir once; no process left; no __pycache__ in checks/). **bb2 PASS** (B2-1 gauge defect 1.1e-16; B2-2 max|β(0.025) - 1| =
  5.55e-4, ratios 3.993; B2-3 ρ ratios 1.0069, 1.0017, ρ ≈ 0.888). Informational κ = 0.25, 4: same pattern (ratios 3.97, 4.00).
- 05:56:20 §6 (proofs: BB-W, BB-sm, BB-4♮, BB-mix-wall, BB-bond + BB-mix′_1, BB-mix-k) appended in one write, after §5
  (05:49:21) and after bb2 (05:51:34). Two post-proof corrections of pre-stated details, marked in place: BB-W's symbol range
  m' < m/(n - 1) (pre-stated m' < m); BB-mix′_1's thresholds use 𝔠_s := max(s̄𝔠_♮p_Π, 𝔠_∞) (pre-stated s̄𝔠_♮p_Π) so that the
  s-family's ball contains BR1's. 05:57 one in-place edit of §6.4 (BB-mix-wall: product-form count (n - 3^d)M_c vs the tree-type
  Steiner count (n/2^d - 1)M_c, which is what gives K ≈ Ce^{-μM_c/2^d}). 05:57:34 §7 (bb2 record, session-2 outcome table, FOR
  OTHER FILES) appended. Title line changed to "sessions 1-2". Final `TZ=UTC stat` BFT_B.md below.
- No commits, PRs, pushes, CL or axiom edits; only BFT_B.md, BFT_B_LOG.md, checks/bb2_criteria.md, checks/bb2_symbol.py,
  checks/bb2.out, checks/bb2.out.time written (runner in the scratchpad). Lock acquired once, released by one rmdir; no
  process left.

### Results by name (session 2; all unreviewed)
- Step 1: the 11 binding fixes of REVIEW_BFT_B_S1 applied ([RBB1-fix]).
- PROVEN-HERE: Lemma BB-W (dimension lemma), Lemma BB-sm (ℓ^{-2} irrelevance on smooth fields), **Theorem BB-mix′_1
  ((BB-mix) at k = 1 for the bond-weighted cluster representation: K = 2^{41}/(s̄ - 1) from ε ≤ ε_mix(s̄); BFT-4's polymer
  bound at k = 1)**.
- PROVEN as an implication: **Theorem BB-4♮** (E_k^br = c_kS_W + R_k, c_k = 1, β[R_k] = 0, sup_k𝒩(R_k) < ∞, R_k irrelevant)
  ⇐ (H-lin^∇)_m + (H-rem^∇)_m + (FP♯') + (SF-∞)_B + BA-9; composite route, no per-level step.
- ARGUED (walls named): BB-mix-wall ((BB-prod)_1 for BB-loc's Möbius activities), BB-mix-k ((H-RW^∇)_k + 𝔐^∇-compatible
  cube weights).
- Check bb2: PASS (c_1 = 1, H_1 - H_W = O(p⁴) at k = 1).

## Session 3, 2026-10-28 UTC
- 06:1x-06:29 Read (read-only): REVIEW_BFT_B_S2 (all, binding), BFT_B.md §0-§1, §2.2 (l.195-240), §5-§7 (all), BFT_B_LOG;
  PROOF block-kernel conventions + CT♯ + Theorem RW (all parts) + RW-triv + N5-sf0 (l.5246-5481), U0, FPq, N5-an♭, BR1
  (l.5598-5709); BFT_A §1 (l.18-97), §3.9-3.10 (l.205-257), §6 [RBA1-fix] GAP 1/2 + corrected pair (l.380-436), §7
  (l.437-575); LINEAR_PACKAGE §4 (Thm 4.2/4.2', Cor 4.3, Lemma 4.4); REVIEW_S22 Part 5 (BFT statement); SF l.178-186,
  l.843-852 ((L-loc)_k). BFT_A.md mtime at read: 05:54:34 UTC (lane A is working; its (H-lin^∇) is used only as a named
  hypothesis).
- 06:30:06 `TZ=UTC stat` BFT_B.md: born = mod 05:58:03, size 104744 (session-2 state). Step 1 starts.
- 06:30-06:33:18 Step 1: binding fixes of REVIEW_BFT_B_S2 applied in place, tagged [RBB2-fix …] (17 tags): R-1 (l.77/79
  pointer to B1-2; provenance note for the 05:57 §6.4 edit appended to §6.4), B4N-1 (ρ := r_ℂε_0/2 with the BCH reason),
  B4N-r1, B4N-2 (§6.3 "right form" withdrawn; the §FOR OTHER FILES (session 2) line is corrected in §11 below, not in
  place), B4N-r2, BMW-1, C2-1 (BB-geo (c) for link sums; N_0(|P|) ≤ (8/γ')coth⁴; 𝔠_♮ := (32/3)coth⁴(m/2)/γ'), C2-2
  (pointer to Lemma N5-an♭-dens, c_ρ := 2S_ρ/r_♭), C2-3 (complex domains), C2-4 (C_R explicit up to c_ρ; "for each m_0").
  **One deviation from the reviewer's literal C2-3, with reason:** BB-mix′_1's complex radius is set to ε_mix(s̄)/16 (not
  ε_br(R)/16), and BB-3_1's to ε_B/16 (not ε_br/16), because the contraction thresholds of those theorems are ε_mix and
  ε_B, so the complex curvature of the lift must be below them (the reviewer's own parenthesis "complex curvature ≤
  ε_mix"); the radii are smaller than the reviewer's and still ε-independent. This uses a complex form of U0 (iv),
  pre-stated as Lemma U0-ℂ in §9.
- 06:33:18 `TZ=UTC stat` BFT_B.md: born = mod 06:33:18, size 111780.
- 06:37:48 §9 "PRE-STATED (session 3)" appended in one write (statements only: Setting W; named hypotheses (W-lin),
  (W-comm), (W-loc), (f), (E3^∇), (I-id); (H-RW^∇)_k with clauses (a)-(f); Lemmas W-ls, W-cut, W-mult, W-pair,
  N5-an♭-dens, U0-ℂ; Theorem RW^∇_k; Construction BB-bond_k; Theorem BB-mix_k; Corollaries BFT4-poly_k, BB-Lloc_k; remark
  (SF-∞)_B; failure modes RW∇-F1..F4; check bb3 summary). `TZ=UTC stat` BFT_B.md: born 06:33:18 mod 06:37:48 size
  128892. No session-3 proof, criteria file or script exists before this time.
- 06:39:49 checks/bb3_criteria.md (born = mod). 06:41:47 checks/bb3_walk.py (final bytes; one pre-run edit of the seed
  line, cosmetic). Runner scratchpad bb3/run_bb3.sh. 06:42:01-06:42:03 bb3 under the numeric lock (one acquisition; lock
  free on arrival; load1 2.38; memory free 41%; 2.38 s wall; peak footprint 793 MB; rmdir once; no process left; no
  __pycache__ in checks/). **bb3 ALL PASS** (B3-1 7.8e-16; B3-2 4.8e-15 with ||R||_∞ = 0.0524; B3-3 1.3e-15; B3-4 class-A
  change 0.0 / 0.0, control 1.48; B3-5 2.4e-15; B3-6 printed rel 0.0; B3-7 0.0 / 0.0, control 3.8e-2). Informational:
  ||R||_∞ at μ² = 1: 0.148, 0.041, 0.012 (R = 4, 6, 8); μ² = 2: 0.052, 0.0098, 0.0020.
- 06:47:02 one further in-place Step-1 edit after §9 (logged here): the session-2 FOR OTHER FILES line "the right form of
  BFT-4 is" tagged [RBB2-fix B4N-2] (withdrawn). No other text above §9 was edited after 06:37:48.
- 06:49:17 §10 (proofs) appended in one write, after §9 (06:37:48) and after bb3 (06:42:03); 06:49:42 two in-place
  clean-ups inside §10 (a garbled Schwarz sentence in §10.5 rewritten; the walk-sum bound in §10.7 Step 4 restated as
  ||PR^ny|| ≤ 4^dG_Pε_W^n||y||). Post-proof corrections of pre-stated details, marked in §10 and collected in §10.9 (§9 not
  edited): χ scale ¼ and η scale ½ (constants C_M^Y(¼), C_M^X(½)); C_M^X(ℓ) = 1 + (2d + 31)/ℓ + d/ℓ² (pre-stated
  1 + (12d + 3)/ℓ + 2/ℓ²); T_W = 3R + 14 (pre-stated 3R + 12); N5-an♭-dens radius r_ρ ≤ r_♭ and c_ρ = 4S_ρ/r_ρ (the C2-2 tag's
  2S_ρ/r_♭ was too optimistic; two ε-independent thresholds added to BB-mix′_1); the weighted remark needs a localised
  (W-comm) and gains e^{-m(R/2-7)}; **𝔈_Q corrected** to Σ_{D∈𝒟_Q}[D(u) - D(0) - ½⟨∇D(u), u⟩] (the pre-stated form missed
  ½⟨𝔑(0; B), A⟩), with Lemma W-grad0 added during the proof (not pre-stated) and (f)'s locality extended to the data.
- 06:50:41 §11 (bb3 record, outcome table, FOR OTHER FILES incl. the proposed BR1 (v) restatement for PROOF's owner)
  appended; title "sessions 1-2" → "sessions 1-3" (same byte length). Final `TZ=UTC stat` BFT_B.md: born = mod 06:50:41,
  size 164390.
- No commits, PRs, pushes, CL or axiom edits; only BFT_B.md, BFT_B_LOG.md, checks/bb3_criteria.md, checks/bb3_walk.py,
  checks/bb3.out, checks/bb3.out.time written (runner in the scratchpad). Lock acquired once, released by one rmdir; no
  process left.

### Results by name (session 3; all unreviewed)
- Step 1: REVIEW_BFT_B_S2's binding fixes applied ([RBB2-fix]; 22 occurrences of the tag in BFT_B.md, counting cross-references), with the C2-3 radius deviation explained above.
- PROVEN-HERE: Lemma N5-an♭-dens (routine; radius r_ρ ≤ r_♭), Lemma U0-ℂ, Lemmas W-ls, W-cut, W-mult, W-pair, Lemma W-grad0
  (added; given Setting LIN's Q).
- Stated precisely: (H-RW^∇)_k (§9.2, clauses (a)-(f)).
- PROVEN as an implication: **Theorem RW^∇_k** ((H-RW^∇)_k (a)-(e) ⇐ (W-lin) + (W-comm) + (W-loc); per-step factor
  ε_W = O(C_cG/R), k-uniform; weighted remark), **Theorem BB-mix_k** (exact polymer decomposition at every k on 𝒞_glob,
  per-cube smallness K = 2^{41}/(s̄ - 1), ||R||_𝒜 ≤ 2e^{m_0}C_R k-uniformly ⇐ (H-RW^∇)_k + (f) + (E3^∇) + (I-id)), Corollary
  BFT4-poly_k (BFT-4's polymer bound at every k on 𝒞_glob, minus local gauge invariance of the pieces), Corollary BB-Lloc_k
  (classical part of SF's (L-loc)_k).
- ARGUED: remark (SF-∞)_B; failure mode RW∇-F1. OPEN: (BB-gi)_k; everything outside 𝒞_glob; lane A's inputs.
- Check bb3: PASS (B3-1..B3-7; model algebra only).

## Session 4, 2026-10-28 UTC
- 07:10-07:29 Read (read-only): REVIEW_BFT_B_S3 (all, binding), BFT_B.md §9-§11 (l.1025-1497) and the heading index,
  BFT_B_LOG, HIST §20.0-§20.2 (Theorem MSG, Corollary MSG-loc' and the superseded MSG-loc, l.1182-1305), BFT_A §3.9-§3.11
  (l.205-273) and §12 (l.869-949: S_tent, LR-pot, LR-grad), REVIEW_BFT_A_S3 Part 6 (LRL statement, l.225-284; lane A is
  proving LRL now, not duplicated here). At 07:10:39 `TZ=UTC stat` BFT_B.md: born = mod 06:50:41, size 164390 (session-3
  state); BFT_A.md mod 06:42:14.
- 07:29:39 stat BFT_B.md unchanged (164390). 07:30:46 **§12 "PRE-STATED (session 4)" appended in one write — the first edit
  of the session** (statements only: Settings Π and GI, covariant norms, box frames; (W-Π), (W-lin-Π), Lemma W-gauge0,
  Theorem RW^∇_k-Π, Corollary BB-mix_k-Π, mixed-operator remark; (BB-gi)_k definition, (CovLift), background hypotheses,
  Lemmas GI-frame, GI-norm, GI-pert, Construction BB-bond_k^cov, Theorem GI-cov, Theorem BB-gi_k, Proposition GI-off,
  Corollary BFT4-poly^gi_k, Proposition CovLift-status; failure modes GI-F1..F3, RWΠ-F1, RW∇-F5; check bb4 summary).
  `TZ=UTC stat` BFT_B.md: born 06:50:41 mod 07:30:46 size 177344. No session-4 proof, criteria file or script exists before
  this time; no [RBB3-fix] edit precedes it.
- 07:31-07:33:17 Step 1: binding and cosmetic fixes of REVIEW_BFT_B_S3 applied in place, tagged [RBB3-fix …] (30 tag
  occurrences): RS3-1 (l.940 pointer to §10.5's c_ρ = 4S_ρ/r_ρ), RS3-2 (S ≤ 0.17), RS3-3 (ε ≤ 0.02 in "Use"), RW3-1 (W-ls
  restated: lane A's norms are sums of sups; ||·||' ≤ ||·|| ≤ t||·||', t_X = 4, t_Y = 6; the factor t inserted into N_P, ε_W,
  R_W, 𝔠_W, σ and the BB-mix_k (i) bound; tags in §9.3, §10.1, §10.7 Step 3, §11 table), RW3-2 (Step 1: the x'' argument),
  RW3-3 (R ≥ 13 for T = 4R, or T ≥ 3R + 14; product partitions with sides in [M_c, 2M_c) and [R, 2R), local tori 4R + 14),
  RW3-4 (Feynman form recorded; pointer to Theorem RW^∇_k-Π of §12.1; mixed form OPEN), RW3-5 (§11's "now a theorem" struck
  and replaced: implication only; GAP 1 / BL-6 (b), LR-grad, slice listed), BB-mix_k at m = 0 (smallness from cube size,
  κ_L ~ log M_c/M_c; the weighted form needed for a rate), BP3-1 (Corollary BFT4-poly_k narrowed in §9.5, §10.8, the §11
  table row and the BFT-4 FOR OTHER FILES line), BL3-1 (K^{(|X|-1)/2} kept: §9.5, §10.8, table row, SF line), item 9
  ((BB-gi)_k restated with a pointer to §12.2), RS3-4 (cutoffs ℓ ≥ ¼), RS3-5 (§10.9 wording), RS3-6 (translations by M_c),
  RS3-7 (sinh continuation). §12 (written 07:30:46, before these edits) cites "[RBB3-fix RW3-3]" for the product partitions:
  a forward reference to this step's fix, not to a result. `TZ=UTC stat` BFT_B.md: born = mod 07:33:17, size 188151.
- 07:36:13 checks/bb4_criteria.md (born = mod; no session-4 constant in it beyond the pre-registered model parameters and
  thresholds). 07:39:19 checks/bb4_models.py born; 07:40:55 one pre-run edit (fixed-point tolerance 1e-15 → 1e-14; an
  unused helper removed); a py_compile syntax check created checks/__pycache__, removed at once. Runner scratchpad
  bb4/run_bb4.sh.
- 07:41:10-07:41:22 bb4 under the numeric lock (one acquisition; free on arrival; load1 3.67; memory free 38%; nice 10;
  thread variables 1; PYTHONDONTWRITEBYTECODE=1; /usr/bin/time -l; python3 without -I; no `timeout`; no trap; `rmdir`
  once). 11.5 s wall, peak footprint 780 MB. **Verdict NOT ALL PASS (12/14):** A-1, A-2, B-1..B-5, C-1..C-4, C-6 PASS;
  **C-5 FAIL** (small-plateau control: identity residual 1.1e-15, predicted ≥ 1e-6) and **B-6 FAIL** (frame-free control:
  non-invariance 2.1e-10 / 2.2e-12, predicted ≥ 1e-6 / 1e-8). Both are failed PREDICTIONS of control rows; not repaired.
- 07:44:49 checks/bb4_diag.py (POST-HOC diagnostic, written after reading bb4.out; not a criterion; imports bb4_models
  unchanged). 07:45:28-07:46:08 under the numeric lock (second acquisition; load1 4.66; memory free 42%; 40.7 s; 146 MB;
  `rmdir` once). D1: measured radius of the model Π = 1.5 (bb4 assumed r_Π = 3); slice identity residual 6.9e-4 at
  plateau 0.5, ≤ 1e-15 at plateaus 1.0-2.0 — the control of C-5 was mis-designed (its plateau already covered Π's reach).
  D2: frame-free non-invariance of ΔE(s) = 2.1e-10, 1.9e-5, 1.3e-2 at μ² = 1, 0.25, 0.05; frame version ≤ 2.1e-14 at all
  three — B-6's threshold mis-estimated the size, which is set by the decay from the transplant cut to the box.
- No process left; lock directory gone after each run; no __pycache__ in checks/.
- 07:49:24 §13 (proofs) and §14 (bb4 record, outcome table, FOR OTHER FILES) appended in one write, after §12 (07:30:46),
  Step 1 (07:33:17) and bb4 + diagnostic (07:41:10-07:46:08); title "sessions 1-3" → "sessions 1-4" (same length).
  07:49:46 two in-place clean-ups inside §13 (the header's collected list of post-proof corrections, replacing a dangling
  "§13.9" pointer; one sentence of 13.4 rewritten); 07:49:58 one word in 13.7 changed. §12 not edited after 07:30:46.
  Post-proof corrections of pre-stated details (marked in §13): Lemma GI-pert needs the added input (Mult-Y) (transposed
  multipliers produce plain rows, GAP-1 family), so Theorem BB-gi_k's new inputs are (CovLift) AND (Mult-Y), not one;
  BB-gi_k's bound uses (CovLift) (iv) + a local pairing bound (ARGUED for non-residual components) instead of W-grad0;
  GI-frame proven for unitary V only. Final `TZ=UTC stat` BFT_B.md: born = mod 07:49:58, size 217135.
- No commits, PRs, pushes, CL or axiom edits; only BFT_B.md, BFT_B_LOG.md, checks/bb4_criteria.md, checks/bb4_models.py,
  checks/bb4.out, checks/bb4.out.time, checks/bb4_diag.py, checks/bb4diag.out, checks/bb4diag.out.time written (runners in
  the scratchpad). Lock acquired twice (run, post-hoc diagnostic), each released by one rmdir; no process left.

### Results by name (session 4; all unreviewed)
- Step 1: REVIEW_BFT_B_S3's binding and cosmetic fixes applied ([RBB3-fix]).
- PROVEN-HERE: Lemma W-gauge0; Lemma GI-frame (unitary); Lemma GI-norm (a), (b) except the residual term.
- PROVEN as an implication: **Theorem RW^∇_k-Π** (hard-slice RW^∇_k, ⇐ (W-Π), (W-lin-Π), (W-comm), (W-loc) (i), (ii), (iv)),
  Corollary BB-mix_k-Π, Lemma GI-pert (with (Mult-Y)), **Theorem GI-cov** (covariant construction ⇒ locally gauge-invariant
  polymers), **Theorem BB-gi_k** ((BB-gi)_k on 𝒞_glob and its gauge saturation ⇐ (CovLift) + (Mult-Y) + BB-mix_k's
  hypotheses, pure Feynman form), Corollary BFT4-poly^gi_k.
- ARGUED: Proposition GI-off; Proposition CovLift-status; RWΠ-F1 (S_tent's piecewise-linear tents fail (W-Π); C^{1,1}
  tents proposed). OPEN: (CovLift); (Mult-Y) (GAP-1 family); the mixed slice+Feynman form.
- Check bb4: 12/14 — A-1, A-2 (m = 0 regime; RW∇-F5 confirmed in a model), B-1..B-5, C-1..C-4, C-6 PASS; C-5 and B-6 FAILED
  as predictions (diagnostics D1, D2: mis-set control thresholds/plateau), not repaired.

## Session 5, 2026-10-28 UTC
- 08:1x-08:24 Read (read-only): REVIEW_BFT_B_S4 (all, binding), BFT_B.md §9.0-§9.4 (l.1031-1140), §10.1-§10.3, §10.7 Step 1
  and the RBB3 tags (l.1216-1350), the m = 0 mechanism note (l.1536-1549), §12-§14 and FOR OTHER FILES (l.1582-1957);
  BFT_B_LOG; BFT_A §1.3-1.4 (l.30-45), §7.1-7.3 (l.444-572), §12-§13 (l.869-1163: S_tent, LR-pot, LR-grad), §16 (l.1226-1313),
  the [RBA3-fix] B5'/B6' text (l.1340-1360: LRL (b)); REVIEW_BFT_A_S4 Part 6 (LRL (b) needs) and its fix list; LINEAR_PACKAGE
  Lemmas 3.2/3.2'/3.2'' (l.170-180); PROOF Lemma LES-div (l.3394-3407) and Lemma U0 (l.5608-5616); REVIEW_BFT_B_S3 l.405-420.
  At 08:24:08 `TZ=UTC stat`: BFT_B.md born = mod 07:49:58, size 217135 (session-4 state); BFT_A.md mod 07:41:05 (lane A
  active; used read-only). Load 3.2, memory free 38%.
- 08:25:04 **§15 "PRE-STATED (session 5)" appended in one write — the first edit of the session** (statements only:
  Setting EΠ, norms, N_res, G_opt, Q_ax, Construction CP, corner lift/Φ-chain; Lemmas EP-alg, EP-int, Q-hold; Theorems EP-bd,
  EP-opt, EP-rec; Corollaries EP-lin, EP-LRL(b); Theorem RW^∇_k-Π(E); Proposition RATE-m; Lemmas CL-uniq, CL-blk; Propositions
  CL-lin, CL-Φ, CovLift-route; failure modes EP-F1..F4, CL-F1..F3; bb5 summary). `TZ=UTC stat` BFT_B.md: born 07:49:58
  mod 08:25:04 size 228448. No session-5 proof, criteria file, script or [RBB4-fix] edit exists before this time.
- **Note for lane A (BFT_A):** lane B owns the slice construction from this session (owner instruction). Lane A's LRL (b)
  "tent-patched local slice" P_♯ should consume S_E / Π_E of BFT_B §15-§16 (box-Coulomb gauge on half-width-2 boxes glued
  with quintic tents) rather than build a separate one; lane A keeps (CO-0)/(CO-up) and the residual-Hölder input.
- 08:25:3x-08:26:44 Step 1: binding and cosmetic fixes of REVIEW_BFT_B_S4 applied in place, tagged [RBB4-fix …] (24 tag
  occurrences in Step 1; 26 in the file counting one forward reference in §15's Theorem RW^∇_k-Π(E) statement and one in §16.9):
  RS4-1 (T^Π_W, T^cov_W at l.1616/1652/1813-area, ℓ_Ω in 13.3, Step 3 of 13.2, §14 table row), RS4-2 (Corollary BB-mix_k-Π in
  §12.1 and 13.2), RS4-3 (13.5: residual part ARGUED; Feynman difference moved under (Mult-Y), two tags), RS4-4 (13.2 remark,
  §12.3 RWΠ-F1, §14 table row, FOR OTHER FILES (2), 13.8's slice sentence), RS4-5 (13.4 |a| ≤ ⅓), RS4-6 ((W-Π) in §12.1), RS4-7
  (13.7 input list with (Pair-loc) and (I-id)_Z, §14 table row, SF line: unweighted/weighted rate), item 8 (13.10: seventh
  candidate (R1)-(R3) and MSG own units). `TZ=UTC stat` BFT_B.md after Step 1: mod 08:26:44 size 233686.
- 08:27:06 checks/bb5_criteria.md (born = mod; thresholds are predictions, no session-5 constant). 08:28:06 checks/bb5_lift.py
  born; 08:28:21 one pre-run edit (the block-constant scalar extension's index offset corrected; a no-op conditional and an
  unused line removed; no criterion touched). Runner scratchpad bb5/run_bb5.sh. Before the run: load1 3.54, memory free 41%.
- 08:28:31-08:28:34 bb5 under the numeric lock (one acquisition; free on arrival; load1 3.31; memory free 40%; nice 10; thread
  variables 1; PYTHONDONTWRITEBYTECODE=1; /usr/bin/time -l; python3 without -I; no `timeout`; no trap; `rmdir` once). 2.85 s wall,
  peak RSS 521 MB. **Verdict ALL PASS (5/5)**: B5-1 identities (≤ 8.5e-13); B5-2 Q1 gradient ×27 from depth 2 to 5; B5-3 cubic
  spline flat (ratios 1.000/1.017/1.018); B5-4 DD6, DD8 pass (DD4 fails the condition); B5-5 Φ(dμ) = dC_0μ to 9.7e-17 and ×729.
  Informational guess "Φ-chain curvature Hölder proxy ratio ≤ 1.5" FAILED (1.73; recorded, not repaired). No process left; lock
  directory gone; no __pycache__ in checks/.
- 08:35:44 §16 (proofs) appended in one write, after §15 (08:25:04), Step 1 (08:26:44) and bb5 (08:28:34); 08:36:05 one in-place
  clarification inside 16.6 (the tent-support case of the Hölder comparison). 08:36:40 §17 (bb5 record, outcome table, FOR
  OTHER FILES) appended; 08:36:46 title "sessions 1-4" → "sessions 1-5" (same length). §15 not edited after 08:25:04.
  Post-proof corrections of pre-stated details (marked in §16): EP-int proved on the larger N'_X; EP-lin converse constant
  (C_Q + 1); CL-blk fails at levels with L^{2(k-j)} > C_sm (k-uniform failure), not at every depth ≥ 1; CL-lin residual with lane
  A's Q ≤ 2||f_j|| (not 2L²) and finite range only for finite masks; CL-uniq's consequence for GI-F2 (new). Final `TZ=UTC stat`
  BFT_B.md: born 08:36:05 mod 08:36:46 size 268561.
- No commits, PRs, pushes, CL or axiom edits; only BFT_B.md, BFT_B_LOG.md, checks/bb5_criteria.md, checks/bb5_lift.py,
  checks/bb5.out, checks/bb5.out.time written (runner in the scratchpad). Lock acquired once, released by one rmdir; no process
  left.

### Results by name (session 5; all unreviewed)
- Step 1: REVIEW_BFT_B_S4's binding and cosmetic fixes applied ([RBB4-fix]).
- PROVEN-HERE: Lemma EP-alg; Lemma EP-int (given LES-div); Lemma Q-hold; **Theorem EP-bd ((W-Π) for the elliptic slice S_E)**;
  **Theorem EP-opt ((W-lin-Π) for S_E ⟺ (H-lin^∇) in the best gauge)**; **Theorem EP-rec (||Π_Ex||_𝔐 ≤ C(||x||_inv + ||x_k||_D +
  N_res(x)))**; Lemma CL-uniq (cocycle automatic; GI-F2 cannot occur); Lemma CL-blk (block-constant extensions excluded);
  Proposition CL-lin (given the mask regularity φ ∈ C^{2,α}).
- PROVEN as an implication: Corollary EP-lin ((W-lin-Π) ⇐ gauge-invariant (H-inv+)); Corollary EP-LRL(b) (LRL (b) ⇐
  (Res-Hölder)_m); **Theorem RW^∇_k-Π(E)**; Proposition RATE-m (κ_L ≥ m/8 from the top-residual coarse mass); Proposition CL-Φ.
- ARGUED: Proposition CovLift-route. OPEN: (CovLift) (nonabelian exact covariance with smooth extension); (Res-Hölder);
  (H-inv+) beyond data + residual sources; mask regularity of DD6/DD8 as a proof.
- Check bb5: ALL PASS (5/5); informational Φ-curvature guess FAILED.

## Session 6, 2026-10-28 UTC
- 09:0x-09:19 Read (read-only): REVIEW_BFT_B_S5 (all, binding), BFT_B.md §15-§17 (l.2001-2417), BFT_B_LOG session 5, BFT_A §1
  (l.18-47), §7.1-§7.3 (l.437-574), §8.1-§8.5 (l.588-661), §12.0 (l.879-897), §13.9-§13.13 (l.1076-1165), [RBA3-fix] B5'-B7'
  (l.1316-1372), §21 (l.1676-1760), LINEAR_PACKAGE §2.5-§3.8 (l.120-200), BFT_B §9.0-§9.1 (l.1031-1084). At 09:19:04 `TZ=UTC
  stat`: BFT_B.md born 08:36:05 mod 08:36:46 size 268561 (session-5 state); BFT_A.md mod 08:52:26 (lane A active; read-only);
  `ls checks | grep -c ^bb6` = 0. Load 1.66, memory free 41%.
- **Ownership:** lane B owns (Res-Hölder) from this session (owner instruction); lane A will not work on it.
- 09:20:07 **§18 "PRE-STATED (session 6)" appended in one write — the first edit of the session** (statements only: Setting RH,
  ρ_l, N_res variants, N_res,m defined (RS5-3 (b)), box functional, 𝒲_δ, (N1-G) import named, Karcher facts cited,
  Constructions KΠ and GC; Lemmas RT, TC; Theorem RH; Corollaries RH-inv, RH-D; Theorem RH_m; Corollary LRL(b)-E; Lemmas
  NF-crit, NF-uniq, NF-cov, REF; Theorem NF-ex; Proposition KΠ; Lemma GC-lin; Proposition AX-cov; Theorem CovLift-KΠ;
  failure modes RH-F1..F3, NF-F1..F3, CL-F4; checks bb6, bb6m, bb6n). `TZ=UTC stat` BFT_B.md: born 08:36:05 mod 09:20:07
  size 281066. No session-6 proof, criteria file, script or [RBB5-fix] edit exists before this time.
- 09:20:4x-09:22:01 Step 1: binding and cosmetic fixes of REVIEW_BFT_B_S5 applied in place, tagged [RBB5-fix …] (20 tag strings):
  RS5-1 (GI-F2 at §12.3, §13.6 Step 2, two §14 rows), RS5-2 (16.5 ⟨πy, w⟩), RS5-3 (EP-LRL(b): T ≥ 5, N_res,m defined, at §15.1,
  16.8 and the §17 row), RS5-4 ((a) 16.6 weighted constant ARGUED with lane-A line pointers, (b) in EP-LRL(b), (c) EP-bd and
  EP-rec scope = linear slice at the trivial chain), RS5-5 (CL-lin table row: "(i), (ii), (iii), (iv) first clause, (v)";
  C_g clause θ = 0 only), RS5-6 (16.10: 2^{44}; ε_mix,k is k-uniform, written ε_mix), RS5-7 (CL-blk: fails once L^{k-j} > C_sm),
  RS5-8 (CL-uniq conditions), RS5-9 (disclosure tag at the session-4 item-8 text), RS5-10 (16.13 status, CL-lin row, (CovLift)
  row, failure-mode row: mask regularity PROVEN (REVIEW_BFT_B_S5 Part D), DD8 adopted, DD6 marginal on the bb5 proxy).
  `TZ=UTC stat` BFT_B.md after Step 1: born 09:21:46 (atomic rewrites by the editor) mod 09:22:01 size 285413.
- **[RBB5-fix RS5-9] Disclosure (appended note).** In session 5 the item-8 tag (BFT_B l.1920-1925, written at Step 1, 08:26)
  says CL-blk was "tested and corrected in §16"; that was written before bb5 ran and before §16 existed (a forward reference).
  CL-blk itself was pre-stated in §15 at 08:25:04. Likewise in this session two RS5-10 tags name checks/bb6m before it
  exists; they say "planned at the time of this tag".
- **[RBB5-fix RS5-10] Correction of the session-5 results list:** "mask regularity of DD6/DD8 as a proof: OPEN" reads "PROVEN by
  an exact finite computation (REVIEW_BFT_B_S5 Part D); DD8 adopted".
- 09:23:17 checks/bb6_criteria.md, bb6m_criteria.md, bb6n_criteria.md (born = mod; thresholds are machine/solver precision, lane
  A's BL-2 constants, or REVIEW_BFT_B_S5 Part D's values; no session-6 constant). 09:25:02 bb6 control A5 replaced, before
  bb6_transport.py existed (the original non-co-closed-j_1 control has no critical point). Scripts: bb6m_mask.py 09:25:33;
  bb6_transport.py 09:26:41 (one pre-run edit: CG cap 6000); bb6n_nf.py 09:27:26, one pre-run edit 09:27:59 (principal SU(2) log
  without sign flip; unpinned descent normalised at c_X). No criterion touched by the script edits.
- 09:28:23-09:29:14 bb6m, bb6n, bb6 under the numeric lock (one acquisition; free on arrival; load1 2.86; memory free 38%; nice 10;
  thread variables 1; PYTHONDONTWRITEBYTECODE=1; /usr/bin/time -l; python3 without -I; no `timeout`; no trap; `rmdir` once). Wall
  0.38 s / 45.1 s / 5.8 s; peak RSS 95 / 35 / 559 MB. **All three ALL PASS.** bb6m reproduces REVIEW_BFT_B_S5 Part D exactly (DD8
  β_10 = 0.4732, DD6 0.2677, DD4 ρ_n = 1.222). bb6n: normal-form uniqueness 3.2e-11, covariance 1.4e-11, KΠ idempotence 3.0e-12,
  root-value covariance 5.6e-12; exp-gluing control fails as predicted (0.336). bb6: transport identities ≤ 1.8e-11; L^{-2m} bound
  attained; inverse estimate saturated (guess RH-F3 holds). No process left; no __pycache__. (A lock directory seen at 09:32 was
  created 09:32:18 by another worker.)
- 09:34:46 §19 (proofs) and §20 (record, table, FOR OTHER FILES) appended in one write, after §18 (09:20:07), Step 1 (09:22:01) and
  the runs (09:29:14); 09:35:12 one in-place correction inside 19.4 (the BCH₂-row size: a direct count replaced an imprecise SPD
  citation). §18 not edited after 09:20:07. Post-proof corrections (marked in §19): c_w = 12 (10 data); NF-ex needs small coarse
  curvature along the path; CovLift-KΠ (i)-(iii) need (N2-0); KΠ's covariance identity is automatic, its content is the root-value
  formula, idempotence and smooth extension; CL-F4 does not occur on 𝒞_glob; AX-cov linearisation proven (pre-stated ARGUED).
  Final `TZ=UTC stat` BFT_B.md: born 09:21:46 mod 09:35:12 size 313159.
- No commits, PRs, pushes, CL or axiom edits; only BFT_B.md, BFT_B_LOG.md and checks/bb6* written (runner in the scratchpad).

### Results by name (session 6; all unreviewed)
- Step 1: REVIEW_BFT_B_S5's binding and cosmetic fixes applied ([RBB5-fix]); item-8 forward reference disclosed.
- PROVEN-HERE: Lemma RT (exact residual transport); Lemma TC; **Theorem RH ((Res-Hölder), m = 0, all source classes)**; **Theorem
  RH_m (weighted; (Res-Hölder)_m for the data map)**; Lemma NF-crit; **Lemma NF-uniq (nonabelian normal-form uniqueness)**;
  Lemma NF-cov; Lemma GC-lin; Proposition AX-cov.
- PROVEN as an implication: **Corollary RH-inv ((H-inv+) ⟺ (H-inv) for α < θ; (W-lin-Π) for S_E ⇐ (H-inv))**; Corollary RH-D;
  **Corollary LRL(b)-E (lane A's LRL (b) for T ≥ 5)**; Theorem CovLift-KΠ (i)-(iii) (given (N1-G), (N2-0)).
- PROVEN given the named import (N1-G): Lemma REF / (N1-bd); Theorem NF-ex; Proposition KΠ (+ Karcher facts, cited).
- OPEN: (CovLift) (iv), (v): (N1-int), (N2-bd) = (R3), (N2-0) nonlinear, C_g clause at θ > 0; (N1-G) on the framework; LRL (b) at
  T = 3, 4; (H-inv) for the remaining source classes (lane A).
- Checks: bb6m, bb6n, bb6 ALL PASS.

## Session 7, 2026-10-28 UTC
- 09:56-10:20 Read (read-only): REVIEW_BFT_B_S6 (all, binding), BFT_B §18-§20 (l.2446-2816), BFT_B_LOG session 6, BFT_B §12.2
  (l.1630-1680), 13.7-13.8 (l.1869-1905), 16.12-16.13 CL-lin (l.2092-2104, 2328-2352), HIST §20.2 Theorem MSG (l.1213-1300) and the
  S4' reflection text (l.385-402, l.1036-1044), checks/bb5_lift.py (l.1-100), bb6n_nf.py (all), bb6_criteria.md (head). At 09:56:32
  `TZ=UTC stat`: BFT_B.md mod 09:35:12 size 313159 (session-6 state); BFT_B_LOG.md mod 09:35:32 size 32864; BFT_A.md mod 09:40:30
  (lane A active; read-only). `ls checks | grep -c ^bb7` = 0. Load 2.99, memory free 44% at 10:20.
- **Lead decision recorded:** both BFT lanes use the elliptic slice S_E as the single gauge fixing.
- 10:21:15 **§21 "PRE-STATED (session 7)" appended in one write — the first edit of the session** (statements only: definitions
  f_j, a_{j+1}, D_ax, 𝒦(ε), Λ_2, (N2-0)_j with quantifiers, (C_g-θ), m_w, Construction KΠ-off, clustered; Remark PL; Lemma N1G;
  Lemmas S2K, N2-step; Theorem N2 (+ N2-lip); Corollary N2-cons; Lemma Γ0; Propositions Cg-lin, Cg-NL; the C_g design decision;
  Lemma CUT; Theorem KΠ-off; Proposition TOP; Remark HOL; failure modes N2-F1, Cg-F1, KO-F1..F3; checks bb7g, bb7n, bb7c, bb7k).
  `TZ=UTC stat` BFT_B.md: born 09:21:46 mod 10:21:15 size 324833 (growth 11674 bytes = §21 exactly). No session-7 proof, criteria
  file, script or [RBB6-fix] edit exists before this time.
- 10:22-10:23:36 Step 1: binding and cosmetic fixes of REVIEW_BFT_B_S6 applied in place, tagged [RBB6-fix …] (25 tag strings in
  BFT_B.md): RS6-1 (§18.1 RH-inv tag with the co-closed scope and V_l OPEN; 19.4 BCH₂-row sentence; table row; FOR OTHER FILES);
  RS6-2 (commutator rows named, 19.4); RS6-3 (19.7 and table row: periodic lift, Remark PL, proof in §22); RS6-4 ((a) 19.16 (i) and
  table row: small gauges only; (b) 19.13 and the failure-mode row: CL-F4 OCCURS off 𝒞_glob; (c) 13.7: extension to the gauge
  saturation by invariance; (d) 13.8 and the §14 GI-off row: (KΠ-off) named); RS6-5 (19.16: (N2-0) restated per level, §21.0);
  RS6-6 (§18.0 (N1-G) tag, 19.11, table rows, §20 paragraph, FOR OTHER FILES); RS6-8 (Theorem RH → RHT, RH_m → RHT_m; 19.6 depth
  m → t; 19.9 C_1 → C_ℓ; Φ_0 for the S_0 kernel; 19.4 C_B' → C_bch); RS6-9 (19.4 in-place correction marked; l.2421 clause struck;
  19.12 "… more precisely" annotated in §19, §18 not edited; 19.13/table: 𝒟(ε) carries both NF-ex hypotheses; checks/bb6_criteria.md
  A5 edit time written as 09:25:02). Tags in pre-stated §18 are additive (original words kept). `TZ=UTC stat` BFT_B.md after Step 1:
  mod 10:23:36 size 331455.
- 10:28:08 checks/bb7g_criteria.md, bb7c_criteria.md, bb7n_criteria.md, bb7k_criteria.md (born = mod; thresholds: float/descent
  precision, the reviewer's closed forms (bb7g), or the pre-stated scalings of §21; no constant derived in session 7). Scripts after
  them: bb7g_n1g.py 10:28:43, bb7c_resid.py 10:29:15, bb7n_chain.py 10:31:10 (one pre-run edit: a dead stub removed), bb7k_off.py
  10:32:39 (born time reset by one pre-run sed edit: an `if False` expression in glue_site replaced by its value w0; no criterion
  touched). Runner scratchpad bb7/run_bb7.sh (lock `until mkdir …/locks/numeric`, load1 < 8 wait, nice 10, thread variables 1,
  PYTHONDONTWRITEBYTECODE=1, /usr/bin/time -l, python3 without -I, no `timeout`, no trap, one `rmdir`). At 10:32 the lock was held
  by another worker (load 2.76, memory free 35%); the runner waits.
- 10:34:18-10:35:23 bb7g, bb7c, bb7n, bb7k under the numeric lock (one acquisition; load1 3.03; memory free 36% → 34%). Wall 0.29 /
  0.40 / 0.82 / 63.4 s; peak RSS 289 / 263 / 178 / 35 MB. **bb7g, bb7c, bb7n ALL PASS; bb7k NOT ALL PASS: K1-K8 PASS, control K10
  FAILED** (Karcher gluing of Haar-spread corner data (spreads ≤ 2.76 < π) converged start-independently; the predicted failure
  needs near-antipodal data, not measured). bb7n disclosure: f_k = 0.26 / 0.52, not the 0.10 / 0.20 named in its criteria (the
  rescaling used the unscaled field's plaquettes); its thresholds are relative to f_k. No process left; no __pycache__.
- 10:38:24 §22 (proofs) appended in one write, after §21 (10:21:15), Step 1 (10:23:36) and the runs (10:35:23); 10:39:24 §23 (check
  record, table, FOR OTHER FILES) appended. §21 not edited after 10:21:15. Post-proof corrections (marked in §22): Remark PL constant
  e^{16m+4m'}; (N2-lip) without the factor k - j; new Lemma CL-clu (the chain of a field small in one level-k gauge is not small in one
  level-0 gauge, so 19.13's domain clause did not literally cover U = chain(V); CL-clu repairs it); Cg-NL's BCH remainder ARGUED;
  bb7k K10 failed. Final `TZ=UTC stat` BFT_B.md: born 09:21:46 mod 10:39:24 size 365788.
- No commits, PRs, pushes, CL or axiom edits; only BFT_B.md, BFT_B_LOG.md and checks/bb7* (plus the RS6-9 one-line time fix in
  checks/bb6_criteria.md) written; runner in the scratchpad.

### Results by name (session 7; all unreviewed)
- Step 1: REVIEW_BFT_B_S6's binding and cosmetic fixes applied ([RBB6-fix], RS6-1..RS6-9).
- PROVEN-HERE: Remark PL (LRL (b) for all T ≥ 3); Lemma S2K; Lemma N2-step; **Theorem N2 ((N2-0) per level with quantifiers,
  k-uniform, curvature-only)**; Lemma Γ0 (given the cited S4' property L1); **Proposition Cg-lin ((C_g-θ) for 0 ≤ θ ≤ 1, linear)**;
  Lemma CUT; Lemma CL-clu; **Theorem KΠ-off (a)-(c)** ((d) as in KΠ); Proposition TOP (a)-(c).
- IMPORTED-AND-REVERIFIED: Lemma N1G ((N1-G), C_G = ¼; REVIEW_BFT_B_S6 D.4).
- PROVEN as an implication: Corollary N2-cons; Proposition Cg-NL first-order term; (CovLift) (i)-(iii) for Z^off on 𝒦(ε) for every
  gauge; Proposition TOP (d) given Lüscher's charge theorem (cited).
- ARGUED: Cg-NL's BCH remainder; Remark HOL. OPEN: (N1-int), (N2-bd) (the (iv) walls, unchanged from 𝒞_glob); V_l's (Res-Hölder);
  the non-residual components of g_Z at θ > 0.
- Checks: bb7g, bb7c, bb7n ALL PASS; bb7k NOT ALL PASS (control K10 failed).

## Session 8, 2026-10-28 UTC
- 10:58-11:10 Read (read-only): REVIEW_BFT_B_S7 (all, binding), REVIEW_BFT_A_S7 (Parts 1-4, l.1-285), BFT_A §31.0-31.1 (l.2745-2813),
  33.1 (l.2936-2952), 33.7 (l.3027-3047), BFT_B §12.2 (l.1630-1669), §15-§16.7 (l.2012-2261), §18 (l.2453-2580), 19.7-19.16 and §20
  (l.2660-2853), §21-§23 (l.2854-3252), BFT_B_LOG session 7, checks/bb6n_nf.py (l.1-120). At 11:10:36 `TZ=UTC stat`: BFT_B.md mod
  10:39:24 size 365788 (session-7 state); BFT_B_LOG.md mod 10:39:42 size 38915; BFT_A.md mod 10:26:38 size 305985, BFT_A_LOG.md mod
  10:26:52 (lane A session 8 has not written its Γ_E^T request; (GE-T) stated in REVIEW_BFT_A_S7 Part 4's form). `ls checks | grep -c
  ^bb8` = 0. Load 3.80, memory free 35% at 11:10.
- 11:12:37 **§24 "PRE-STATED (session 8)" appended in one write — the first edit of the session** (statements only: definitions
  M_n, image fields, level-l sources, frames, δF_j, row defect; Lemma GE-T (a)-(f); Remark GE-T'; Theorem N2-loc; Theorem N1-loc;
  Corollary CL-iv; failure modes GE-F1..F3, N2L-F1, N1L-F1, N1L-F2; checks bb8t, bb8n, bb8w). `TZ=UTC stat` BFT_B.md: mod 11:12:37
  size 375969 (growth 10181 bytes = §24 exactly). No session-8 proof, criteria file, script or [RBB7-fix] edit exists before this time.
- 11:13-11:15:04 Step 1: REVIEW_BFT_B_S7's fixes applied in place, tagged [RBB7-fix …] (25 tag strings in BFT_B.md), all before §24
  except none (§24 untouched): RS7-1 (six Step-1 tags l.1901, 1975, 2475, 2666, 2711, 2774: "planned at the time of this tag, Step 1
  10:23; proof written 10:38"); RS7-2 (22 preamble correction (1) withdrawn, 22.1 two places, table row; e^{20m} stands; q-fold lift
  for T = 1, 2 recorded ARGUED-routine; also noted in the 19.7 tag); RS7-3 (22.2 step (2): Metzler/maximum-principle replacement
  written out; §18.0 tag and §21.1 N1G statement annotated "(proof replaced: REVIEW_BFT_B_S7 B.2)" — additive tags in pre-stated
  text, original words kept); RS7-4 (22.11: log := inverse of exp on the injectivity ball, or r_2 < π); RS7-5 (19.16, 22.12, §23:
  local forms, pointing to §24.2); RS7-6 ((a) T ≥ 5 for Z^off in 22.12 and §12.2; (b) hypercubic symmetrisation note in 22.12);
  RS7-7 (CL-clu: explicit C_clε ≤ r_1/2 ≤ convexity radius, Ω ⊇ corner boxes); RS7-8 (§12.2 cocycle convention; 22.7 cites BFT_A
  l.1112; §23 FOR OTHER FILES (3) question withdrawn; §23 bb7c C3 tightness, bb7n reviewer amplitude run, bb7k K10 mis-design notes).
  11:15:11 one dated note appended to checks/bb7k_criteria.md (K10 mis-designed; E.2 is the real control); criteria text unchanged.
  `TZ=UTC stat` BFT_B.md after Step 1: mod 11:15:04 size 382187.
- 11:17:28 checks/bb8t_criteria.md, bb8n_criteria.md, bb8w_criteria.md (born = mod; thresholds: float precision, the proven bounds of
  §24 (2M_n, M_n/4 + 32|⟨ψ⟩|, 240(n/s)³, C_∞ ≤ 2), and trend clauses fixed before any run). Scripts after them: bb8t_get.py born
  11:18:52 (one pre-run edit 11:19:08: malformed mask-index line fixed, unused variable removed), bb8n_lip.py, bb8w_nf.py (11:19-11:20).
  Runner scratchpad bb8/run_bb8.sh as in session 7 (lock, load1 < 8, nice 10, threads 1, no `timeout`, no trap, one `rmdir`).
- 11:21:05-11:21:12 bb8t, bb8n, bb8w under the numeric lock (one acquisition; load1 2.42; memory free 32% → 32%). Wall 5.5 / 1.7 /
  0.1 s; peak 650 / 176 / 66 MB. **bb8t ALL PASS; bb8w ALL PASS; bb8n NOT ALL PASS (L-c FAIL)**: the defect ratios printed 0.0000 and the
  [0.5, 2] scaling clause compared round-off.
- 11:25:00 checks/bb8n_defect_criteria.md (prediction d_j = 0 exactly, written before the script) and bb8n_defect.py (informational
  probe; bb8n.out kept as the record); 11:25:12-11:25:13 run under the lock (bb8/run_bb8b.sh; load1 2.89; memory 37% → 33%): D-a PASS,
  max own|d_j| ≤ 8.9e-17. No process left; no __pycache__.
- 11:27:31 §25 (proofs) appended in one write, after §24 (11:12:37), Step 1 (11:15:04) and the runs (11:25:13); 11:27:56 one in-place
  correction inside §25.4 (the last-scale constant 256η → 512η, with its derivation); 11:28:30 §26 (check record, table, FOR OTHER FILES)
  appended, 11:28:44 one garbled bound in §26 FOR OTHER FILES cleaned. §24 not edited after 11:12:37. Post-proof corrections (marked in
  §25): exact Q_X sum 2d(n/s)^{d-1} (bound 8L^{3(k-l)}); (c), (e) of GE-T in d = 4; **N2-loc (c) with C_d = 0 (row defect ≡ 0)**; measured
  C_∞ = 1/8. Final `TZ=UTC stat` BFT_B.md: mod 11:28:44 size 409782.
- No commits, PRs, pushes, CL or axiom edits; only BFT_B.md, BFT_B_LOG.md and checks/bb8* (plus one dated note appended to
  checks/bb7k_criteria.md for RS7-8) written; runners in the scratchpad.

### Results by name (session 8; all unreviewed)
- Step 1: REVIEW_BFT_B_S7's fixes applied ([RBB7-fix], RS7-1..RS7-8).
- PROVEN-HERE: **Lemma GE-T** (for lane A: Γ_E^T ℓ¹ ≤ 4(4n + 1), locality 3, exact divergence identity, root charges ≤ 8L^{3(k-l)}||j||_∞,
  ℓ^∞ bound, dual sup-data bound for Λ); **Theorem N2-loc** (local (N2-bd): covariant Lipschitz curvature, exact root rows);
  **Theorem N1-loc** given LES-div (local (N1-int)).
- PROVEN as an implication: **Corollary CL-iv** ((CovLift) (iv) first clause for Z^off in frames; residual term at Cg-NL's status).
- ARGUED: GE-T's sharper bulk sup (given BA-7); Remark GE-T' (log n loss of the operator route). OPEN: S_E vs 𝒩-optimal in ℓ¹;
  non-residual g_Z components at θ > 0; (v); (Mult-Y) / GAP 1 (not attempted).
- Checks: bb8t, bb8w ALL PASS; bb8n NOT ALL PASS (L-c; defect identically 0); bb8n_defect PASS.

## Session 9, 2026-10-28 UTC
- 12:20-12:26 Read (read-only): DRIVE_BRIEF.md (scratchpad), HANDOFF.md, **REVIEW_BFT_B_S8.md in full (binding)**, REVIEW_BFT_B_S5
  l.430-519, REVIEW_BFT_B_S6 Part B (l.91-215) and its fix list, BFT_B §18.1 (l.2480-2515) and §19.1-19.6 (l.2576-2650), §25.1
  l.3405-3420 and §25.5-§26 (l.3480-3569), BFT_A §26.0-26.2 (l.2199-2270), §28.7-28.10 (l.2510-2560), §31.1 (l.2777-2812), BL-2 and
  its proof (l.488-500, 598-620), PROOF.md l.6590-6713 (cross-lane map and the BFT clause table), REVIEW_BFT_A_S4 l.25-40,
  REVIEW_BFT_A_S6 l.23-26, 151, 181, 198, 219-224, REVIEW_BFT_A_S7 l.48, 289-320, SF l.695-723, 881-895.
  At 12:22:43 `TZ=UTC stat` (this worktree was created at 12:03:19, so every file's birth time reads 12:03:19 and birth times carry no
  information here; sizes and mod times do): BFT_B.md 409782 B, BFT_B_LOG.md 44498 B, BFT_A.md 351969 B, REVIEW_BFT_B_S8.md 38842 B.
  `ls checks | grep -c ^bb9` = 0. Load averages 1.92 2.00 2.08.
- 12:27:05 **§27 "PRE-STATED (session 9)" appended in one write — the FIRST edit of session 9** (statements only: scope and targets;
  definitions Setting LIN^cc, D(S), Ψ_l/ψ_l, h_l^T, ĵ_l, π_l, J_0, λ^Γ_*; Lemma RT-cc; Lemma FT; Theorem RHT-cc; Corollary RHT-V;
  Theorem RHT_m-cc; failure modes RHcc-F1..F4; Proposition CO-use; Proposition NCR; (NC-Γ)_cc; Proposition INV-cc; the named open
  items (CO-fun) and (GT-sup); (BFT-5_E); Proposition BFT5-red; Lemma Rω-frame; the [RBB8-fix] erratum list; check bb9).
  `TZ=UTC stat` BFT_B.md: mod 12:27:05, size 424557 — **growth 14775 bytes = §27 exactly**. No session-9 erratum entry, proof,
  criteria file or script exists before this time.
- 12:28:06 **§28 "[RBB8-fix] Errata entries for session 8"** appended (RS8-1..RS8-9, every fix required by REVIEW_BFT_B_S8,
  each naming the line it corrects; §24-§26 untouched, append-only ownership). `stat` size 429816 — growth 5259 B. One
  in-place correction of my own §28 header at 12:28:19 (the draft said "appended 12:31", the actual append was 12:28:06;
  size 429935) and a second wording correction of the same header at 12:42:41 (size 482875). Both are corrections to
  session-9 text only; no line of §1-§26 was touched at any point — verified at 12:42 by `sed -n '1,3569p' | wc -c` =
  **409782 B**, byte-for-byte the session-8 final size.
- 12:30:43 **§29 "Proofs, Step 2"** appended (Lemma RT-cc PROVEN-HERE; Lemma FT PROVEN-HERE; Theorem RHT-cc PROVEN-HERE;
  Corollary RHT-V PROVEN as an implication; Theorem RHT_m-cc PROVEN-HERE, c_w = 14). Growth 14241 B. Written **before** the
  criteria file and before any script.
- 12:31:25 `checks/bb9_criteria.md` (A1-A6, B0-B7 with pre-registered PASS/FAIL verdicts; no constant derived in this
  session); 12:34:06 one **amendment appended to the criteria** adding test A7 (funnel non-vacuity) — appended **before any
  script existed**, and so disclosed in the criteria file itself. 12:35:37 `checks/bb9_rtcc.py`.
- 12:35:52 **bb9 run: NOT ALL PASS — B3 and B4 FAILED.** 6.13 s, 27.5 MB. No numeric lock taken: exact `fractions.Fraction`
  / int arithmetic in plain python, no numpy, no BLAS (DRIVE_BRIEF rule 6). Environment: nice 10, OMP/OPENBLAS/MKL/VECLIB
  threads = 1, PYTHONDONTWRITEBYTECODE=1, `python3 -I`, `/usr/bin/time -l`, no `timeout`, no trap. **Cause, found after the
  run: a script bug** — the level-1 gradient applied Q_1^T twice, so Part B solved the wrong energy (B0 passed because the
  same buggy operator built and checked the system). `checks/bb9.out` and `checks/bb9_rtcc.py` are **kept unaltered as the
  record of the FAIL.**
- 12:36:21 `checks/bb9b_rtcc.py` = bb9_rtcc.py with that **one expression** corrected and nothing else changed (the fix is
  stated in its header); **the criteria file was not retuned and no test was added after seeing an outcome.**
  12:36:27 **bb9b run: ALL PASS** (A1-A7, B0-B7). 6.14 s, 28.2 MB. No process left; no `checks/__pycache__` (no `-B` needed:
  `-I` plus PYTHONDONTWRITEBYTECODE).
- 12:38:58 **§30 (Proposition CO-use) and §31 (the (NC-Γ) restatement)** appended in one write. Growth 15193 B.
- 12:40:10 **§32 (BFT-5: (BFT-5_E), Proposition BFT5-red with the (G♯-patch^Ω) narrowing, Lemma Rω-frame ARGUED)** appended.
  Growth 7539 B.
- 12:41:45 **§33 (check record including the disclosed bb9 FAIL, outcome table, what BFT-0/1/2 now rests on) and
  "FOR OTHER FILES (session 9)"** appended. Growth 15410 B. One in-place correction inside §31.2 at 12:42:21 (an
  over-precise "·L^{-m}" on the s-slot replaced by the term-by-term decay L^{-θ(m+1)} / L^{-m}; size 482795).
- Final `TZ=UTC stat` BFT_B.md: mod 12:42:41, size 482875. Files written this session: BFT_B.md (appends plus three
  in-place corrections of session-9 text only), BFT_B_LOG.md, `checks/bb9_criteria.md`, `checks/bb9_rtcc.py`,
  `checks/bb9.out`, `checks/bb9.time`, `checks/bb9b_rtcc.py`, `checks/bb9b.out`, `checks/bb9b.time`. **No git command was
  run; no commit, PR or push; no axiom, CL or other lane file touched.** Requests for other owners are in §33's
  "FOR OTHER FILES (session 9; not edited)".

### Results by name (session 9; all unreviewed)
- Errata: REVIEW_BFT_B_S8's RS8-1..RS8-9 entered as [RBB8-fix] erratum entries in §28, including the three the task named
  (RS8-2 rewording, RS8-3 the GE-T → **Lemma ΓT-op** rename, RS8-8 withdrawal of "S_E vs 𝒩-optimal in ℓ¹") and RS8-9.
- **PROVEN-HERE:** **Lemma RT-cc** (d*ρ_l is the level-(l+1)-root restriction of Σ_{l'≤l}d*j_{l'}; the recursion with
  ĵ_l = j_l + h_l^Tψ_l; d*J_0 = 0, f_0 = n²dΔ_0^{-1}J_0); **Lemma FT** (||h_l^T||_{ℓ^∞→ℓ^∞} ≤ 1, block-interior support,
  π_l(h_l^Tψ_l) ≤ 2dΣ_{l'≤l}L^{-3(l-l')}π_{l'}(j_{l'}), e^{2m} weighted); **Theorem RHT-cc** (K_f = 8.737 at d = 4, L = 3,
  α = ¼); **Theorem RHT_m-cc** (c_w = 14); **Proposition NCR**; Proposition CO-use (bookkeeping).
- **PROVEN as an implication:** **Corollary RHT-V** — **(Res-Hölder) = EP-F4 closed at m = 0 for the non-co-closed BCH₂
  remainder V_l**, at critical points and for every gauge fixing, given lane A's Lemma CD (i), Proposition NC, Corollary NC;
  **Proposition INV-cc** (reduction); **Proposition BFT5-red** (with the new (G♯-patch^Ω) narrowing).
- **CONDITIONAL:** **(NC-Γ)_cc** — residual half PROVEN unconditionally, curvature half CONDITIONAL on the newly named
  **(CO-fun)**.
- **ARGUED:** **Lemma Rω-frame** (the frame rewriting of (R♯_ω) is not a new wall; the commutator-to-divergence-form step
  has no explicit constants).
- **Stated, OPEN, with precise statements:** **(CO-fun)**, **(GT-sup)**, **(BFT-5_E)** (owner lane B, status OPEN with its
  inputs named; clause (c) PROVEN by Proposition NCR).
- **Status corrections carried to other files (not edited):** (CO-0) = Theorem W0 and (CO-up) = Theorem GU are PROVEN in
  lane A and CONFIRMED by REVIEW_BFT_A_S6 — REVIEW_BFT_A_S4's ARGUED (CO-up) and REVIEW_BFT_B_S5's "(CO-0), (CO-up) OPEN"
  are stale; **(SB) is no longer an input to (H-inv+)** (Theorem CO-B removes it, REVIEW_BFT_A_S5 l.373). Hence **(H-inv+)
  at m = 0 and the trivial background, for level-wise co-closed classes, is PROVEN as an implication with every input
  CONFIRMED by a lane review.**
- **Not attempted:** Step 5's (Mult-Y) / GAP 1 and the nonabelian (CovLift) items (targets 1-4 consumed the session).
- **Failure modes:** RHcc-F1, RHcc-F2, RHcc-F4 do not occur (proven); **RHcc-F3 OCCURS** as pre-stated and expected (the
  (P0) slot now enters N_res, with the exponentially small weight L^{-(1-α)k}).
- **Checks: bb9 NOT ALL PASS (B3, B4 FAIL, script bug, record kept); bb9b ALL PASS** on the same unaltered criteria.

## Session 10 (2026-10-28 UTC) — lane B, the two items session 9 isolated: (CO-fun) and (GT-sup)

### Provenance
- Task: close (CO-fun) and (GT-sup), the two named open items of §31.2 and §31.3, so that (NC-Γ) for Γ_E is complete.
  Scope given: trivial background, m = 0, one slice S_E (DRIVE_BRIEF D1). Owned files: a new "# Session 10" appended to
  the END of BFT_B.md, this log entry, and new `checks/bb10_*` files. **Append-only: no line of §1-§33 or of any earlier
  log entry is altered.**
- Reading before the first edit (exploratory, not recorded in the file): BFT_B §27-§33 in full (session 9, unreviewed),
  §16.1-16.2, §24.1, §25.1 (c)-(e), §26 FOR OTHER FILES; REVIEW_BFT_B_S8; REVIEW_BFT_A_S8 (landed during this session's
  reading) Parts 4-6, "Verdict on the stand-in transport", "The biggest live wall in lane A"; BFT_A §26.0-26.2,
  §28.4-28.9, §38.1-38.6, §38.8, Lemma CD (l.2789); HANDOFF.md; `checks/bb9b_rtcc.py`.
- **First edit: §34, the PRE-STATED section, statements only.** `TZ=UTC date` immediately before the append: 13:07:28.
  `TZ=UTC stat` immediately after: **mod 13:07:28, size 496400** (BFT_B.md was 482875 at the end of session 9, so §34 plus
  its "# Session 10" heading is **13525 bytes**). §34 cites nothing produced in this session; its only claim is file order.
  It names the two targets, the definitions (Λ_0, D^root/D^⊥, (CC-0), C(j), ξ_i, (Y-sup^loc), (NEUT-box)), the planned
  statements with planned labels, six failure modes (S10-F1..S10-F6) and the plan of check bb10.
- Appends after §34, in order, each after the one before: **§35** (the (CO-fun) proofs; mod 13:19:26, size 520502),
  **§36** (the (GT-sup) proofs and Theorem NCE; mod 13:21:20, size 535218), **§37.1-§37.3** (check record, outcome table,
  what (NC-Γ) rests on; mod 13:23:08, size 551268), **§37.4** (the correction to §37.1's limitation 2 and the bb10c
  record, including a disclosed FAIL; mod 13:26:10, size 555646).
- **Checks.** `checks/bb10_criteria.md` born 13:09:13 with an amendment at 13:12:09, **both before**
  `checks/bb10_cof3`… precisely: before `checks/bb10_cof.py` (born 13:14:02). bb10 ran 13:14-13:15: **ALL PASS**
  (A1-A8, B0, B1), 5.95 s, 27.8 MB. Then `checks/bb10c_criteria.md` born 13:24:27, **before**
  `checks/bb10c_cof3.py` (born 13:25:13); bb10c ran 13:25: **NOT ALL PASS — C4 (b) FAILED**, 0.39 s, 22.4 MB;
  output and script kept unaltered, **no rerun**. No numeric lock was taken for either (exact `fractions.Fraction`,
  no numpy, no BLAS, single thread, `python3 -I`, nice 10); DRIVE_BRIEF rule 6 exempts them. Both scripts copy bb9b's
  operator construction (bb9b itself untouched); bb10c's only change to that copy is K = 3.
- Files written this session: BFT_B.md (appends only — **no line of §1-§33 altered**), BFT_B_LOG.md,
  `checks/bb10_criteria.md`, `checks/bb10_cof.py`, `checks/bb10.out`, `checks/bb10.time`,
  `checks/bb10c_criteria.md`, `checks/bb10c_cof3.py`, `checks/bb10c.out`, `checks/bb10c.time`.
  **No git command was run; no commit, PR or push; no axiom and no other lane file touched.** Requests for other owners
  are in §37's "FOR OTHER FILES (session 10; not edited)".

### Results by name (session 10; all unreviewed)
- **PROVEN-HERE:** **Lemma W0-use** (co-closedness enters BFT_A §28.5 twice: step 2's representative freedom, which is a
  condition on the **total** object paired with Y^p_0, and step 3's straightening, which **is** the funnel and is priced by
  Lemma FT; steps 1, 4, 5 use sups and divergence form only); **Lemma SPLIT** (every slot of a Setting LIN^cc source is
  composite-co-closed, so slot-by-slot superposition **is** available); **Lemma DF-cc** (ξ_i = R_{i+1}(D(S)) − ψ_i; under
  (CC-0), C(j) = Σ_l(Q_str^{(0→l)})^Tĵ_l, and the same at every intermediate level); **Proposition COF-size**
  (π_0(C(j)) ≤ C_C(||j^c_0||_∞ + ||j||_{Pc}), k-, T-uniform); **Proposition COF-res** (the residue is the level-k root
  charges against the response's funnel Φ_k(Y^p_0) = Proposition TE's tent coefficient); **Remark MASSLESS** (the free
  dΔ_0^{-1} route loses a factor T); **Proposition GT-split** (the level-k root charges never enter the gauge-fixing
  remainder; Λ(x)(c_Y) = 0); **Proposition GT-loc** (sup|λ^{Γ_E}_*| ≤ 20·local coarse field sup, absolute constant).
- **PROVEN as an implication:** **Theorem COF = (CO-fun) under (CC-0)** (inputs quoted and CONFIRMED in lane A: Theorem YH,
  W0 steps 3-4 with LES-div/Lemma LE/BL-C, Theorem GU, Corollary LIN0, Theorem PW-cc's residual estimates; plus session 9's
  Lemma RT-cc and Lemma FT); **Corollary COF-crit** (so **the curvature half of (NC-Γ)_cc is closed at critical points of
  𝔉_k**); **Proposition GT-ell** (the ℓ^∞ × ℓ¹ route and its exact price); **Theorem NCE (i)**: **(NC-Γ) for Γ_E holds at
  every critical point of 𝔉_k, m = 0, trivial background, every gauge fixing, k- and T-uniformly.**
- **ARGUED:** **Proposition GT-attr** — lane A's own arithmetic puts the L^{2k−3}η² of Lemma RC's *Reading* in |D(R)(Z)|·n²
  and not in σ, so **(GT-sup) is expected TRUE**, not false ([S10-fix 2]).
- **CONDITIONAL:** **(GT-sup)** on the new named item **(Y-sup^loc)** (a local sup bound on a named representative's
  level-0 field), with the absolute constant 20; alternatively on **(NEUT-box)** via Proposition GT-ell.
- **Refuted / corrected:** **(CO-fun) as stated in §31.2 is FALSE without (CC-0)** (S10-F4 OCCURS; erratum [S10-fix 1]),
  and its stated **reason** for being open ("Theorem W0 cannot take the funnel pieces one at a time") is **superseded** —
  the funnel is not a source, it never enters the dual pairing, and the regrouping of Lemma DF-cc makes the one object that
  is paired co-closed. §31.3's expectation that (GT-sup) is false is corrected ([S10-fix 2]). §37.1's own limitation 2 is
  corrected in §37.4 (the two groupings are the same **vector**; they differ in the available **bound**).
- **Still OPEN, now named and sharp:** **(TENT-Q)** = **(NEUT-box)** — off the critical set the whole of (NC-Γ) for Γ_E
  reduces to **one scalar per level-k box**, the compensation charge ⟨χ^5_XD(S)⟩, which appears both as the (P0) size of
  the slice correction Γ_E^TD(S) and as the root charge of Proposition COF-res; **(Y-sup^loc)**.
- **Failure modes:** **S10-F1 OCCURS** (expected, harmless: W0 step 3's straightening is the funnel);
  **S10-F2 does not occur**; **S10-F3 does not occur**; **S10-F4 OCCURS** (expected); **S10-F5 OCCURS** (expected: the
  massless route loses T); **S10-F6 OCCURS** (expected: the remainder is dominated by the coarse cell of p).
- **Not attempted:** (Y-sup^loc); (NEUT-box) and its relation to lane A's Proposition OB; m > 0; θ > 0; the nontrivial
  background; the factor k; (PW-ii).
- **Checks: bb10 ALL PASS; bb10c NOT ALL PASS (C4 (b) FAILED, disclosed, diagnosed, record kept, no rerun).** The FAIL is
  of a **demonstration** (that the two available bounds separate on the test data), not of a lemma: the constructed family
  inflates π_0(j_0) because `solve_div` builds an antiderivative, so B^ψ_0 exceeded B^ξ_0 on every instance. C4 (a) — the
  inequality Proposition COF-size actually uses — passed everywhere.

---

# Session 11 (2026-10-28 UTC) — the nontrivial background: the input audit, (N1), conjugation transport, g_Z at θ > 0

## Step 1 (process): PRE-STATED first
- **§38 (PRE-STATED, session 11) is the FIRST edit of session 11.** Appended at the end of BFT_B.md; stat time
  **13:58:33 UTC**; **20,581 bytes** appended (BFT_B.md 555,646 → 576,227 bytes). Statements only. Nothing in §38 cites a
  result of this session; its only claim is file order. §27-§37 (sessions 9 and 10) are **not edited** — they are under
  review and they are the record; everything this session has to correct in them is entered as a dated erratum naming the
  line it corrects.
- Reading that preceded the append (not recorded, so §38 claims nothing but file order): BFT_B §27-§37 in full, §12.0-§12.3,
  §15.0-§15.4, §16.1-§16.9, §21.0-§21.3, §22.8-§22.10, §25.5; REVIEW_BFT_B_S5 Parts C, D, E and the overclaim list;
  REVIEW_S22 l.389-432 (the BFT statement, the norm 𝔐 and the anti-circularity constraint); REVIEW_BFT_A_S8;
  BFT_A §12.2-§12.3, §21.2, §23.7-§23.12, §26.1-§26.2, §28.4-§28.9, §38; LINEAR_PACKAGE §3, §4, §6, §9, §10;
  PROOF.md l.6525-6560 and l.6731; HANDOFF; SESSION24_RESULTS.
- Targets, pre-stated in §38.0: (1) the audit of the six lane-A inputs into Tier A/B/C; (2) (N1) stated clause by clause
  and its minimal consumption by BFT-0/1/2; (3) transport by conjugation, priced in 𝔐; (4) (CovLift) (iv)'s non-residual
  g_Z at θ > 0. Six failure modes S11-F1..S11-F6 pre-stated in §38.5; check bb11 planned in §38.6 with the explicit
  warning that the model must be **nonabelian** (bb9b's and bb10's abelian model is vacuous for every §38.3 statement).

## Step 2 (process): criteria before scripts; the model had to change
- `checks/bb11_criteria.md` born **13:59:43 UTC** (8,867 bytes), with one amendment appended at **14:02:18 UTC**, **both
  before any bb11 script existed** (`checks/bb11_bgd.py` born 14:04:15). The amendment has six items and is disclosed in
  full in the criteria file: A1's exact form (transport prefactor, far corner), A3's norm changed to the exactly-computable
  Frobenius form (which **strengthens** the constant from 2 to 1), A4b's sign, the box reduced from `Ñ_X` to own
  half-width 2 (`Ñ_X` is 4107 rational unknowns in this model), B1's tents and B2's **pointwise** intertwining forms, and
  C2's construction. **No bb11 criterion was retuned after any outcome.**
- **No constant derived in session 11 appears in either criteria file.** The only constants are the model parameters
  (`d = 2`, `L = 3`, `k = 2`), the rational rotation entries `3/5, 4/5`, and the elementary `||M v|| ≤ ||M||_F ||v||`.
- **bb11 is the first lane-B check that is NOT abelian.** For an abelian group `Ad ≡ 1` and every statement of §38.3 is
  vacuous, so bb9b's and bb10's model could not be reused. bb11 uses **SU(2) in the adjoint** with every `Ad_{Z(b)}` a
  product of rational 3-4-5 rotations, so all arithmetic stays exact in `ℚ`. `checks/bb9b_rtcc.py` and
  `checks/bb10_cof.py` are **not edited**; `checks/bb11b_quant.py` reads `checks/bb11_bgd.py` and cuts it at its TESTS
  banner without modifying it.
- No numeric lock taken (DRIVE_BRIEF rule 6: exact rational arithmetic in plain python, no numpy/BLAS). Load 1.69 at
  launch. **bb11: 13.24 s, 20.9 MB. bb11b: 4.22 s, 17.9 MB.**

## Step 3: results (§39-§43 appended; file 576,227 → 660,202 bytes; §27-§37 byte-identical and untouched)

- **§39 Proposition AUDIT (PROVEN-HERE) and Proposition SIX-RED (PROVEN-HERE as a reduction).** The six lane-A inputs
  decompose into **Tier A** (operator identities, background-free), **Tier B** (four exactness steps: `d*d* = 0`; root
  covariance; "a constant 2-form is co-closed", which sits inside Theorem YH — **S11-F1 OCCURS**; "a closed 1-form is a
  gradient" / "`d` of a constant is 0") and **Tier C** (four shared analytic kernels: `M`/`M_f` of LINEAR_PACKAGE Theorem
  4.2′; `C_α` of LES/LES-div; `C_K`; Lemma LE). **Corollary LIN0 and Theorem CO-upR carry NO kernel of their own**;
  W0, GU, CO-0R, CO-B rest on the same list, and only W0 needs `𝒩*`. **So the nontrivial background is four shared
  kernels and four exactness defects, not six background hypotheses.** [S11-fix 1] corrects §33.3/§37.3's reading.
- **§40 (N1).** Stated clause by clause (a)-(e). **This session REFUTED its own pre-stated Theorem N1-alg** (bb11 **A5
  FAIL**): §16.1 (a)'s gauge shift uses "`d` of a constant is 0", and `d_Z`(const) `= (Ad_Z − 1)c ≠ 0`. The exact
  replacement is (40.1) (bb11b A5g, exact). **(N1-a) is PROVEN-HERE in the narrowed form (a′)-(g′)** — the gauge shift on
  the **pinned** class, which is exactly what §16.1 (d), (e) use (bb11 B1 PASS at a curved nonabelian background) — with
  uniqueness by **Lemma CL-uniq** (CONFIRMED) and **stronger** at `Z ≠ 1` than at `Z = 1` (bb11 A6). **S11-F4 OCCURS**:
  covariance becomes equivariance in `(Z, x)`, which is what Theorem GI-cov consumes. **`Λ_0` cannot be read modulo
  constants at `Z ≠ 1`** (bb11b A6q) — a simplification that costs nothing, since GT-split already takes that
  representative. **(N1-d) PROVEN as an implication of the new named item (N1-nd)** = Lemma FG (i) at `Z` = the
  linearisation of BFT-0's own uniqueness clause. **Proposition N1-CONS (PROVEN-HERE as bookkeeping):** BFT-0/1/2
  consumes **(N1-a) + (N1-d)** for (CL-0)/(FP♯′) — both algebraic — plus (N1-c) for §16.9, and (N1-b)/(N1-e) only as the
  𝔐-bridge.
- **§41 conjugation transport.** **Lemma CONJ (PROVEN-HERE):** at a **flat** background `Ad_G` intertwines everything
  exactly, pointwise — so the deviation from the trivial problem is governed by the background **curvature**, not by
  `||log Z||`, and `f_j ≤ C_N f_k` holds on all of `𝒦(ε)` gauge-invariantly with no global gauge (**SF's BNA-F4 is about
  `log Z`, not `F_Z`**). **Theorem BGD:** (a) PROVEN-HERE, `(d_Z d_Z λ)(p) = (U_1 − U_2)λ(far corner)` with
  `||U_1 − U_2||_F = ||Ad_{W_p} − 1||_F` and own size `≤ c_N C_N L^{−2(k−j)} f_k`; (b) PROVEN-HERE as an identity —
  **root covariance is EXACT iff the background is a straight-row tower, which §25.5 proves for `Z^off`** — and
  CONDITIONAL on `(C_g-θ)` for the size off the tower; (c) PROVEN-HERE, **both defects are level-diagonal-relative, so
  they cost a FACTOR `(1 + C f_k)` with no weight penalty, no factor `k` and no restriction on `θ_w ∈ (0, 2]`**
  (**S11-F2 does NOT occur**). **Lemma FR-price (PROVEN as an implication of Corollary CL-iv):** in the **box normal
  form** frame the local kernels (C-II), (C-III), (C-IV) and (N1-b), (N1-c) transport at `(1 − 8c_N C_1 f_k)^{−1}`,
  k-, T-uniformly; **the complete axial frame cannot be used** (BNA-F4 on one box). **S11-F3 does not occur for T ≥ 17.**
  **Proposition NL-GLOB:** Theorem 4.2′ is a **momentum-space** argument, so **(C-I) is the only kernel that does not
  transport**; it splits into **(GAP-Z)** and exponential locality (Combes-Thomas, scalar weight, ARGUED).
  **Theorem TRANSP (PROVEN as an implication): `(H-inv+)_Z` follows from `(GAP-Z)` + `(N1-nd)` alone, at the price
  `(1 + C f_k)`.** Anti-circularity checked explicitly: (GAP-Z) is the composite `ℓ²`/symbol input, the same shape as
  Theorem 4.2′ ⟹ W0/GU ⟹ LIN0 at `Z = 1`; no per-level `C^{(j)}` is used as a Newton inverse.
- **§42 (CovLift) (iv)'s non-residual `g_Z` at θ > 0. Lemma GZ-SLOT (PROVEN-HERE):** the non-residual components are
  exactly the **(G) slot with 2-form `F_j(Z)`** plus a plain slot of order `f²`. **Proposition GZ-FALSE (PROVEN-HERE):
  the clause is FALSE at every θ > 0 for EVERY lift** — it demands coarse-curvature decay at rate θ while BFT-1's
  **maximal** `θ_w^c = 2` gives `f_l ≤ C f_k` with no decay. **Not a nonlinearity, not a parametrisation artefact — a
  currency mismatch**, and `θ > 0` is doing real work because Theorem GU needs `θ > α > 0` in the same slot.
  **Theorem Cg-nr:** the (G)-slot representative is free modulo `Ker d_Z^*` and its consumers take it as input, so the
  clause reads with `𝔤_l = inf{||(F_l − 𝒫)^c||_∞ : d_Z^* 𝒫 = 0}`; `(N2-lip)` gives the right size, weighted
  `≤ C(L, θ) f_k` for every `0 ≤ θ < 1`. **S11-F5 OCCURS**: the block-wise `Z`-parallel comparison 2-form is co-closed
  only inside the blocks, so the residue is a **per-block neutrality condition** (Lemma BOG's no-wrap clause) — the new
  named item **(CURV-dec)**. A reduction of an OPEN item to a sharper OPEN item.
- **S11-F6 OCCURS and is answered (ARGUED):** W0 step 4 / CO-0R / CO-B apply LES "on the periodic lift", which has no
  frame; **Theorem W0-loc is W0 step 4 in box form**, exactly the box Lemma FR-price prices, so the lift is a device and
  not a requirement — but the box forms of CO-0R's and CO-B's applications are written nowhere.
- **New named items:** **(N1-nd)**, **(GAP-Z)**, **(CURV-dec)**, all OPEN, all stated. **(GAP-Z) is NOT a new item:**
  it is BFT-5's input (1), (G♯_0-field), moved off the trivial chain, and LINEAR_PACKAGE §10's paper-scale "propagator
  bounds at a general background [cf. CMP 95, 96, 99]". **The nontrivial background and BFT-5 are ONE obstruction.**
- **Errata entered against this session's own reading (sessions 9 and 10 stand as the record):** **[S11-fix 1]** to
  §33.3 item 1 / §37.3 item 4. Two of this session's own §38 displays were corrected before any script existed, in the
  criteria amendment: `d_Z d_Z`'s far-corner form and the **pointwise** (not `G(c_X)`) intertwining of Lemma CONJ.
- **Checks: bb11 NOT ALL PASS (A5 FAIL — a correct FAIL of a wrong pre-stated statement; output and script kept
  unaltered, NO rerun of bb11); bb11b ALL PASS** under new criteria with four new pre-registered tests. Six scope
  limitations recorded in §43.1, of which the material one is **limitation 2**: the reduced `5 × 5` box tests the algebra
  but **nothing** about Lemma FR-price, whose whole content is that the box has fixed **coarse** size.
- **Not attempted:** lane A's `DX_m`, `DB_m` at `m > 0`; `(GAP-Z)`; `(N1-nd)`; `(CURV-dec)`; the three-neutrality
  identification; `(TENT-Q)`/`(NEUT-box)`/`(Y-sup^loc)` (session 10's residue).

## Step 4 (process): one self-clarification appended, nothing edited
- **§43.4** appended (14:17:44 UTC) clarifying §41.2 (c)'s "level-diagonal-relative": the claim is about the **defect
  operators** (cost = a factor, no weight), while the **one level-crossing composition** in which a defect appears —
  Lemma SPLIT's `Σ_l ev^{(0→l)T} d_Z* d_Z* G_l` — is priced separately in §41.3 and lands on **(TENT-Q)**. §41.2 and
  §41.3 stand unaltered as the record, in the same way session 10's §37.4 corrected §37.1 without editing it.
- **Ownership respected throughout:** the only files written this session are `BFT_B.md` (appended: §38-§43),
  `BFT_B_LOG.md` (appended), and `checks/bb11_criteria.md`, `checks/bb11_bgd.py`, `checks/bb11.out`, `checks/bb11.time`,
  `checks/bb11b_criteria.md`, `checks/bb11b_quant.py`, `checks/bb11b.out`, `checks/bb11b.time`. **§27-§37 verified
  byte-identical** (the first 4307 lines of BFT_B.md are 555,646 bytes, the pre-session size). No git command was run.
  Every request on another lane is in the "FOR OTHER FILES (session 11; not edited)" section.
