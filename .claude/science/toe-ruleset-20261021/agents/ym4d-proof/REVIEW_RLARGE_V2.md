# REVIEW_RLARGE_V2: first hostile review of RLARGE.md v2, with a check of PROOF session 23's two hand numbers

Reviewer: an independent agent that wrote none of RLARGE.md, RLARGE_INTEGRATION_LOG.md, PROOF.md or any lane file. This file is
the only file written in the working tree. No commits, PRs or pushes. Date: 2026-10-28, ≈09:10-09:40 UTC.

**Inputs (read-only).**
- RLARGE.md v2 §0-§8 (l.1-595) in full; Appendix A headings only. RLARGE_INTEGRATION_LOG.md (all).
- Lane logs: HIST_LOG, HW_LOG, PLD_LOG, SQ_LOG, BFT_A_LOG (all); FLOW_LOG sessions 8-10.
- Reviews: REVIEW_HW_S1 (bottom line, Priority 4, l.225-256, l.426-440), REVIEW_HW_S2 (bottom line, tally, binding fixes),
  REVIEW_S22 (overclaims, fixes, FOR OTHER FILES, l.436-500), REVIEW_SF_S7 (E-2, E-3, B-5, l.37, 153-163, 215-221, 290-330).
- Lane files by anchor: HW.md §5.3, §18-§19 (l.265-280, 380-391, 924-1040); FLOW.md l.200-218, l.1296-1330, l.3814;
  PROOF.md header l.1-30, [S20]-[S23] blocks (l.5440-5680, 5735-5741, 5812-5830, 5951-6012, 6085-6110, 6295-6410, 6489-6713).
- The FLOW, HIST/SQ and SF/PLD/BFT statuses were first collected by three read-only search agents (provenance: Explore agents of
  this session, same model; not independent evidence). Every status used for a verdict below was re-read by me at the quoted
  line: FLOW l.204-205, 1296-1330, 3814; REVIEW_FLOW_S3 l.34, 203; REVIEW_HIST_S4 l.447-450; REVIEW_SQ_S2 l.393-396;
  REVIEW_SF_S7 l.290-300; SF.md l.2228-2237; REVIEW_BFT_B_S5 l.480-500; REVIEW_SF_S5 l.343; HIST l.1392-1394.
- Not read: EXISTENCE.md (so K8, K9 are not re-checked), BFT_A/BFT_B bodies, REVIEW_PLD_* beyond what PROOF [S23] and the
  agents quote (PLD.md and REVIEW_PLD_S3 predate v2 and were integrated by it).

**Numerics.** One script, scratchpad `rlv2/s23_numbers.py` (mpmath interval arithmetic, 60 digits, outward rounding on the
quoted decimal inputs), three runs under the numeric lock (each one mkdir, one rmdir; nice 10; thread variables 1; load
1.7-2.5; < 1 s each; no process left). Output `rlv2/s23_out.txt`.

Status words as in PROOF.md. "l.N" without a file name means a line of RLARGE.md.

---

## Bottom line

- **RLARGE v2 is stale on most of its open rows.** Every lane it integrated has moved since 01:18 UTC. Part 1 lists 31
  stale or wrong statements. The largest:
  - K1, K4 and K5 are resolved.
  - (AE) is now CONDITIONAL ⇐ (MS-Sob), and (MSG) is CONFIRMED-WITH-FIX. HW, however, consumes (CLS-min) ⇐ (REG-min) instead.
  - (I_k^E)'' exists, with new defects.
  - (H-w) has a CONDITIONAL proof route (HW^cap + REL-seq). Its wall (SDP)^A is re-owned to node A.
  - (BG-unif) and (BG)_k are re-pointed to BFT clauses. BFT-3 is PROVEN at k = 1.
  - (U-IR) has dissolved into a new FLOW list.
  - The N5 threshold numbers and the ε_1 range are out of date by many orders.
- **The three-way pricing of §3 is NOT sound as written. The defect is architectural, not a status lag.**
  - Branch (iii) is stated as a fixed-V integrand bound whose removed-cone normalisation is "absorbed by the history
    bookkeeping (e^{B_0} per boundary cube)" (l.358-359).
  - Proposition FV (HW; CONFIRMED as CONDITIONAL ⇐ (CLS-min) by REVIEW_HW_S1 l.235-251) shows that at a fixed bad coarse field
    that normalisation is ≥ e^{θa_bad u_k}. It cancels the price exactly.
  - §4.3 step 6 ("priced … before U_k is integrated") therefore cannot be a fixed-V bound either.
  - What survives:
    - branch (i) for the plain chain;
    - branch (ii) as PLD-desc's implication on good V;
    - branch (iii) read FORWARD, which is Theorem HW: one energy threshold per defect plus one joint Chernoff moment under a
      single relaxed law. This replaces the §3.4 case split, the greedy factors, RS-joint and, for bad cubes, E10.
- **The inductive step §4.3 is sound in its shape, but its hypothesis list is incomplete.** Missing items:
  - (SDP)^A, (SF-cap)^A, (LI^F), (NA-∅) and (KS-N);
  - the collar-bad extension (TC);
  - the S4-5 conflict between (RLF-5) and (I_k^E)'' (b'');
  - the requirement g² ≪ ε_1²·10⁻¹³;
  - the stage-0 (CH-c)/DX-rel routing.
  - (RLF-3) is also written with the wrong exponent and the wrong reference. HW delivers a = min{θa_bad, a_A} ≪ a_♯, relative
    to Z(∅), and Z(∅) reaches Z_K^{sf} only through (NA-∅).
  - Verdict on §4.3: **ARGUED stands, with the list replaced by Part 3's.**
- **Job 2, both hand numbers: the arithmetic is right, but both are stated slightly too loosely.**
  - **κ window.** The exact windows are 1.93965·10⁻² (session-23 class) and 2.58576·10⁻² (old class).
    - PROOF's "< 1.94·10⁻²" and "< 2.586·10⁻²" both round UP past the exact value: e_κ = 1.000075 and 1.000052 > 1 at those
      endpoints.
    - The second is the binding fix KW-1 of REVIEW_SF_S7, which said "< 2.585·10⁻²", applied unfaithfully.
  - **coth⁴(m_1/2).** It is 5.8544·10²⁰ (session-23 m_1 = 1.28576·10⁻⁵); the old value is 2.9399·10⁴². Both confirmed.
    - But the C_θ term it sits in, 288A_incoth⁴(m_1/2)ℓ_θ, carries a second coth⁴ inside A_in and a factor ℓ_θ ∝ 1/m_1.
    - It is ≥ 7.8·10⁵⁶·C_Δ on the session-23 class (≥ 5.5·10¹¹⁶·C_Δ on the old class), not "≈ 10⁴²".
    - The conclusion "CURV1 not yet usable" is reinforced, not changed.
- **Spot-check of the S23 consolidation: 11 edits sampled; 10 faithful, 1 unfaithful (KW-1).**

---

## Part 1. Stale or wrong statuses in RLARGE v2 (job 1 (a))

"Now" is the current status per the latest review that judges the item (lane file only where no review exists; marked
"unreviewed").

### 1A. FLOW-side items (lane C)
| # | RLARGE v2 place and claim | now | source |
|---|---|---|---|
| F1 | §4.2 row 1, §7: (F_R) ⇐ F-flow ⇐ (UNIV-1L) ⇐ UNIV ⇐ **(U-IR), (U-loc)** | UNIV ⇐ (L-loc2) [ARGUED], (VFINE) [s], (VC-V) [s], (DEF) [s-P]. Last reviewed list: (V-IR) in form (Q1)(d), (UIR)/(V-IR-S), the vector off-shell defect, (L-loc2). | FLOW l.3814 (session 10, unreviewed); REVIEW_FLOW_S9 l.379-384 |
| F2 | row 1: **(U-loc) PROVEN-HERE [S3, unreviewed]** | Lemma U-loc′ **CONFIRMED (counted)**; Corollary U-red holds without (U-loc). (L-loc)/(L-loc2) are a new, different hypothesis, not a rename. | REVIEW_FLOW_S3 l.203 |
| F3 | row 1: **(U-IR) OPEN [s-P]** (vertices, slice, longitudinal) | Dissolved: (U-IR)(a3) RETIRED (FLOW l.2793); (a2), (a4′), (b) "not additional hypotheses" (REVIEW_FLOW_S7 l.347-349); the scalar-proxy (UIR) PROVEN (Theorem UIR-S, session 10, unreviewed); (IRR*) RETIRED | FLOW l.3347, 3843-3846 |
| F4 | §8 K1: "FLOW (SF-g)'s sign should be re-checked by its owner" | **Resolved:** FLOW agrees β[𝒮^{LF}_k] = −δβ_k, i.e. u → u − δβ (FLOW l.204-205); "K1 is right" (REVIEW_FLOW_S3 l.34). No bound changes. | FLOW l.200-218 |
| F5 | §0 bullet, §4.4, §8 K4: g_k ≤ g_{k+1} "not implied"; "HIST owner should confirm" | **Supplied by Lemma F-mono** (CONFIRMED-WITH-FIX S3-2, not counted separately): e^{−a/g_k²} ≤ e^{aR}e^{−a/g_{k+1}²}; 1/g_{k+1}² ≤ 1/g_k² + R (⋆); g_{k+1}^{−p} ≤ g_k^{−p}(1 + Rg_k²)^{p/2}. All five HIST uses H1-H5 covered. **New:** H3 (Λ^J_1 → (1 + R)Λ^J_1) was not in the K4 list. **Still owed by HIST:** restate CL^J's Setting (HIST l.190, 349, 767 still say g_k ≤ g_{k+1}). Exact monotonicity rests on UNIV-rate, a GAP. | FLOW l.1296-1330 |
| F6 | §7: "+ (SF-g), (SF-cont), (SF-∞) (⊂ node A)"; (SF-bg) not named | (SF-bg) is no longer used by UNIV (Lemma TOW, CONFIRMED); where node A uses it, it is BFT-2, 3 at the trivial field | FLOW l.1690; REVIEW_FLOW_S4 l.51; PROOF l.6646 |
| F7 | §0 "β_1 := β_0^std"; F-flow's β_± = β_0^std ± … | FLOW writes β_0′. The same quantity; cosmetic. | FLOW l.420-421 |

### 1B. HIST / SQ items (branch (iii), (I_k^E))
| # | RLARGE v2 place and claim | now | source |
|---|---|---|---|
| H1 | §3.3, §4.1, row 4: (I_k^E) HYPOTHESIS with GAPs S2-1..S2-3; "(I_k^E)′ announced for §20.3 (not present)" | **(I_k^E)″** is written (HIST l.1720; HYPOTHESIS). S2-1 and S2-3 are repaired; S2-2 is repaired once S3-7's notation fix is applied. New defects: S3-6, S4-1, S4-2, **S4-5** | REVIEW_HIST_S4 l.453; REVIEW_HIST_S3 l.46, 420 |
| H2 | (not in v2) | Theorem A5 (the analytic main term) is **ARGUED**, not CONDITIONAL. (a5-G) is false in ℓ^∞→ℓ^∞ (S4-1); base-set gap (S4-2). After restatement it would be CONDITIONAL ⇐ (a5-G♯) + **(R♯)** [OPEN, PROOF/N2-owned] + (a5-U) + (a3-q) [OPEN, HIST] + (MS-Sob). HIST l.1683 still says CONDITIONAL (stale in the lane file) | REVIEW_HIST_S4 l.220, 252, 449 |
| H3 | §3.3, row 9: **(AE) OPEN [P]** | **CONDITIONAL ⇐ (MS-Sob)** (Theorem AE-red CONFIRMED). Wall: (MS-Sob) ⇐[ARGUED] MSG-loc-dev + MS-HLS + (SQ-dev) | REVIEW_HIST_S4 l.50, 379-380 |
| H4 | §3.3, §7: **(MSG) "under attack"; P?** | Theorem MSG **CONFIRMED-WITH-FIX**, depth-uniform, C_M = 66.1. MSG-loc as stated is a GAP; MSG-loc′ PROVEN | REVIEW_HIST_S3 l.22, 29, 192 |
| H5 | §3.3: CLS-sf cone form "Target S5, not yet written" | **Corollary CLS-cone** written: CONDITIONAL ⇐ (AE), CONFIRMED with scope fix S3-5 ((c1) 1/24, (c2) 1/576, (c3) disjoint footprints, else k-fold). C_cone ≈ 1.1·10¹⁵, η_AE ≈ 1.8·10⁻¹⁵ (N = 2). **Requirement for RLARGE: g² ≪ ε_1²·10⁻¹³** wherever the price must beat per-defect entropy | REVIEW_HIST_S3 l.282, 307-309; REVIEW_HIST_S4 l.112; HIST l.1392-1394 |
| H6 | §3.3: CLS-red constant "max{C_loc, 2/η_E}" | C_cone = max{C′_AE/(2N), 2/η_E} (N-4) | REVIEW_HIST_S4 l.77 |
| H7 | §3.3, rows 9-10: the branch-(iii) wall is CLS-sf via (AE)/(MSG) | **On the route HW actually uses: (CLS-min) ⇐ (REG-min)** (SQ: PRICE-iii, DESC-ε CONFIRMED as CONDITIONAL ⇐ (REG-min)). (REG-min) OPEN, its wall = (MIN-reg)_cone. "(REG-min) ⇐ (BFT-cone) + (MIN-reg)_cone" is "close to circular". The (AE) route survives as a parallel route. Whether the merger lowers the wall count is UNDECIDED | REVIEW_SQ_S1 l.155, 346; REVIEW_SQ_S2 l.50, 339, 395, 439-442; REVIEW_HW_S2 bottom line |
| H8 | §3.4: a_coh "not yet a number" | a_bad = c_prmin{ε_1², t_pr²}; ≈ (1.1-2.3)·10⁻¹⁶ε_1² via (AE), ≈ 5.6·10⁻²³/C_D⁴ via (REG-min). SQ and REVIEW_SQ_S1 l.410 ask RLARGE to record a_coh as the **binding** entry of a_♯ (g² ≪ 10⁻²³ sup route, ≪ 10⁻³¹ energy route) | REVIEW_HW_S2 (W-2 check); SQ l.224-225 |
| H9 | §1.2 (RLF-5): "unchanged"; §8 K7 "not reconciled" | **S4-5 (binding integration item):** (RLF-5)'s width O(g/√κ) and (I_k^E)″ (b″) "cannot hold for the same polymers" — a conflict of targets. Primary option: holomorphy on 𝔇_{2ε_1,α_E} after re-centring at the holomorphic critical branch; fallback: two polymer classes (a node-A norm decision) | REVIEW_HIST_S4 l.306, 316-321 |
| H10 | §8 K2 (σ^J_Q not stated), K3, K6 | Unchanged: no σ^J_Q anywhere. K3 is moot for HW's (ref-a) route (no extraction; REVIEW_HW_S1 bottom line) but not for the R-operation. K6 gains τ_c (Part 1C, S4) | — |

### 1C. HW items ((H-w), K5)
| # | RLARGE v2 place and claim | now | source |
|---|---|---|---|
| W1 | row 10, §5.2, §7: **(H-w) OPEN [P]** | **(H-w′) CONDITIONAL ⇐ (F_R) [g_K² ≤ 1/(2R)] + (CLS-min) + (LI^F) + (M-f^A)_θ.** Route: Theorem HW^cap + H4-red′ (CONFIRMED-WITH-FIX, counted) + Lemma REL-seq on ℛ_𝔥^↑ (CONFIRMED-WITH-FIX, counted). Conditions: max{6θ, 24θ}(1 + 2Rg_K²) < 1, a = θa_bad. Scope: SU(2) (SU(N ≥ 3) needs (KS-N)), bad-only defects. HW counted 6 | HW l.966-972, 985-990; REVIEW_HW_S2 tally |
| W2 | (not in v2) | **(SDP)^A** [OPEN, P; node A]: a per-level in-step returned-defect probability bound under every μ ∈ ℛ_𝔥^↑ ∪ {μ_{R(𝔥)}}, from (I_{k−1}^E)′(d) + (CLS-min) + (W1-ret′^J)_{k−1}(c) + (SC) + I-tay^J + R1^J. It is never derived from level k − 1 (LOOP-const = LF-count at n = 1). Also **(SF-cap)^A** [OPEN, node A], rate 24θ(1 + 2Rg_K²) < 1. (M-f^A) ⇐ both | HW §18.1; REVIEW_HW_S2 SDP-1 |
| W3 | (not in v2) | **(NA-∅)** (NA-1 form, with 𝒱_K^{LF}) [OPEN, node A] converts HIST-sum's Z(∅)-relative output into (RLF-4)'s comparison. As written it was WRONG (NA-1) | HW §13.3, §19 A3 |
| W4 | §8 K5 "not written … ARGUED" | **Resolved** (REVIEW_HW_S1): the three prices did not combine because their moments were taken under three different laws. Under one relaxed law they combine by one pointwise Chernoff inequality (Lemma CH), with no greedy or independence factor. Not consumed by HW: RS-joint, (PLD-q), (SG^fl), PLD-desc, (BG)_k, the §3.4 case split, E10 | HW §5.3 (l.380-391) |
| W5 | §3.3 last bullet: removed-cone normalisation "absorbed by … e^{B_0} per boundary cube" | **FALSE at a fixed bad coarse field** (Proposition FV): it is ≥ e^{θa_bad u_k} and cancels the price. Fix R-1 (for the RLARGE owner) | REVIEW_HW_S1 l.235-251 |
| W6 | §4.3 step 6; §2.1 RS ordering "priced before U_k is integrated" | Cannot be a fixed-V integrand bound; the RS ordering has no pricing role (R-1) | REVIEW_HW_S1 l.243-251 |
| W7 | row 12: H-4 [ARGUED, s] | On the HW route it is replaced by **(LI)/(LI^F)** [OPEN, HW], with H4-red CONFIRMED as CONDITIONAL ⇐ (LI). (LI) is "a precise form of H-4 in the indicator representation", a different object (H-8) | REVIEW_HW_S1 l.229-233 |
| W8 | §1.2 (RLF-3) exponent a_♯, reference Z_K^{sf} | HW delivers a = min{θa_bad, a_A} ≪ a_♯, relative to Z(∅) (ref-a), in Lemma HS′'s per-component shadow form; n_H is computed from this a (n_H ≈ 10²², HW §18.2) | HW §19 notes |
| W9 | §2.2/§2.3 (D-b) collar-bad covered by the same price | Collar-bad and non-quiet cubes are covered only by Theorem HW's W-cb extension (condition (TC), θ < 1/(96·82), (M-i) unreduced), **not by HW^cap** | HW §19 Scope; REVIEW_HW_S1 W-3 |

### 1D. Node A / PROOF / SF / BFT items
| # | RLARGE v2 place and claim | now | source |
|---|---|---|---|
| A1 | §0 [v2-C]: N5 threshold "≈ 2·10⁻³²/C_Δ" at level 0; "shrinking by ≈ 10⁻⁴⁰ per level" | Level 0: **ε_* = 2.476·10⁻¹³/C_Δ** on the session-23 class (N5-w0: 1.7·10⁻²⁴/C_Δ). The 0 → 1 factor is 1/(1 + 36p_L𝔠_∞^♯) ≈ 8·10⁻⁶. Level-i ≥ 1 constants are not covered by CI-bg. The level-uniform form is GAP along the per-level route (CURV-F2′, CURV-F2″) | PROOF l.12-16, 5504-5512, 5953, 6008, 6386-6392 |
| A2 | row 3a: (BG-unif) "named, not precisely stated" | Precisely stated ([R20-fix 12]) and **re-pointed:** (i) ⊂ BFT-0 + BFT-1 (θ_w = 0), (ii) ⊂ BFT-2, (iii) ⊂ BFT-3, (iv) ⇐ BFT-4 | PROOF l.5990, 6631-6633 |
| A3 | row 8, §3.2: (BG)_k [OPEN, s, PLD §15.2] | **= BFT-3** (R_bg, load-bearing under v2); C_I = BFT-1 one-step (not load-bearing). **BFT-3: k = 1 PROVEN** (Theorem BB-3_1); k ≥ 2 ⇐ weighted (H-inv+)_m | REVIEW_S22 l.429; REVIEW_BFT_B_S5 l.484; BFT_B l.648 |
| A4 | §3.2: N5-sf_i ⇐ (NA-H_loc)_i, OPEN i ≥ 2 | PROOF needs BFT-0, 1 (θ_w = 0), 2, 4 for level-uniformity. NAH-unif′ GAP as written; COMP GAP ((CL-4)) | PROOF l.6700-6712 |
| A5 | §0 thresholds ε_1, ε_loc; Appendix A c32/c33 at ε_1 = 0.5 | The current ε_1 ceiling is ≲ 6.7·10⁻⁴⁰ (TB-1, rerun class). c32/c33's ε_1 = 0.5 is "outside the admissible range" (needs a reading note). SF asks to add τ_c and (TH-ch′) to [v2-C] | REVIEW_SF_S7 l.297; REVIEW_SF_S5 l.359; SF l.2232-2233 |
| A6 | §3.4 stage-0 routing; §2.3 (D-d) E10 | At stage 0 the plaquette leg above τ_c for (D-b)/(D-c) is **DX-rel** (in-step, PROVEN inequality), not branches (ii)/(iii). **(CH-c)** is CONDITIONAL ⇐ DX-rel + (DX-loc) [OPEN] + E10 [OPEN] + CH-3 scope. E10 is now on lane F's path | SF l.2177, 2235-2236; REVIEW_SF_S5 l.398 |
| A7 | row 11 (SF-last): HYPOTHESIS, s | Conflict to record: ≈ 60 final levels are affected by the torus clause (wrapped clusters break "shapes up to translation"), not O(1) | REVIEW_SF_S5 l.343 |
| A8 | row 7 (SG^fl)_k | Stage 0: (SG^fl)_0 has a non-circular O-chain (O0-O5), CONDITIONAL. Circularity note: it must consume only CE-Q (band), not CE-Q^∞ | SF l.2226; REVIEW_SF_S3 l.223 |
| A9 | §7 "(SF^J) = node A1-A4: N2, N4, N5, N6" | SF splits it: A1.0 PROVEN; A1.k OPEN; A3's CE and RW proven but their composition at k ≥ 1 not written; A4 all HYPOTHESIS/OPEN. New open names: (DX-loc-3/4), (GF-B^𝔥), (GF-dec)_k, (C_♭-eval), the C_Δ evaluation. "No RLARGE §4.2 row discharged" | SF l.49-52; REVIEW_SF_S7 l.292, 341-347 |
| A10 | §6 PROVEN list | Missing: HW's 6 counted items, MSG, AE-red, TERM-an, NORM-an, U-loc′, F-mono, SQ's TOP/REFL/SHIFT/REG-lin, BFT-3 and BFT-4 at k = 1 | as above |

**Count:** F1-F7, H1-H10, W1-W9, A1-A10 = 36 rows. Of these, 31 are stale or wrong statuses; F7, H10 and A10 are cosmetic or
"unchanged", and W2, W3 are new items v2 could not have had.

---

## Part 2. Soundness (job 1 (b))

### 2.1 Three-way pricing (§3, §3.4), as amended by the lanes: **NOT SOUND AS WRITTEN; repairable by re-basing on HW**

1. **Branch (i)** (l.296-308). PROVEN for the plain chain stands (RS, RS-lin, KN, and for SU(2) the exact moments of
   KS-chain). The in-history form is not "≤ e^{Σ|ρ|} × kernel" (H-4) on the route that works. It is H4-red ⇐ (LI) (HW).
   "Unconditional" (§6 l.503) must read "plain chain; in-history ⇐ (LI) [SU(2); (KS-N) for N ≥ 3]".
2. **Branch (ii)** (l.310-331). The implication PLD-desc ⇐ (SG^fl) is correct. It is valid only on good V (𝒱^sf), with a
   forward law μ^+ (FV does not refute it, REVIEW_HW_S1). However, no route to (H-w) now consumes it: HW does not, and stage 0
   uses DX-rel for (D-b)/(D-c) above τ_c (A6). The (SG^fl) row survives only as a node-A clause.
3. **Branch (iii)** (l.333-361): **WRONG as a fixed-V statement.**
   - The text says "a defect cube carries a factor ≤ e^{−u_kc_sfε_1²/C} times the integrand with that cube's cone energy
     removed". It adds that the removed-cone normalisation is absorbed at e^{B_0} per cube.
   - Proposition FV: for every V with ζ_Q(V) = 1 and every U, κΦ_{int Q} + F^col_Q ≥ a_bad. The normalisation of the
     removed-cone integrand at that fixed V is therefore ≥ e^{θa_bad u_k}, and it cancels the factor exactly (Lemma EQ).
   - The bad-V suppression lives in V's own law. It can only be collected forward, as a moment under the level-k marginal
     (KS-chain factorisation).
   - REVIEW_PLD_S3's proposed branch (iii) is itself only ARGUED. FV is a CONDITIONAL theorem (⇐ (CLS-min)), so the error is
     documented, not suspected.
4. **§3.4 case split and joint pricing** (l.364-378). These are superseded, not repaired:
   - The greedy factors (7⁴, 81, 5⁴) and the probability-versus-integrand mix (K5) are replaced by Lemma CH: one pointwise
     Chernoff inequality under the single relaxed law μ_{R(𝔥)}, with one energy threshold per defect (W-bad ⇐ (CLS-min)).
   - The a_♯ formula should be replaced by a = min{θa_bad, a_A} with max{6θ, 24θ}(1 + 2Rg_K²) < 1.
   - The binding entry is a_coh = a_bad (H8). It forces g² ≪ ε_1²·10⁻¹³ (energy route), or the corresponding (REG-min) number.
5. **Coverage gap.** HW^cap covers bad cubes only. The collar-bad and non-quiet family (D-b) and (D-c) is covered only by W-cb
   with (TC) and an unreduced (M-i), at θ < 1/(96·82). E10 is not needed for bad cubes on the HW route (bad windows lie in their
   own column). It is still needed for collar-bad cubes and on lane F's stage-0 route ((CH-c) ⇐ E10).
6. **What to write in v3 (Fix V-1).**
   - Replace §3 by "defect price = Theorem HW^cap (bad) + W-cb (collar-bad, with (TC)), forward, under ℛ_𝔥^↑".
   - Keep branch (i) and branch (ii) as the moment inputs (M-i) and (M-f) they now are.
   - Delete the e^{B_0} absorption claim and §4.3 step 6's pricing reading (R-1).

### 2.2 Inductive step (§4.3) as amended: **ARGUED stands; the hypothesis list is incomplete, (RLF-3) is mis-stated, and three interface questions are open**

1. **Steps 1-3 and 5** (exact rewriting, σ-gas, sea average and re-extraction, small-field step). These are not affected by
   FV. HW's analysis actually re-confirms that node A must use the R-operation's non-saturating split ((W1-ret′^J) (a)-(b) +
   I-tay^J + (SF-irr)), because (SDP)^A has to be derived through it (HW §18.1). So I-σ, I-σ^J (K2 still unstated), I-tay^J and
   (SC) stay on the critical path, now as inputs to (SDP)^A.
2. **Step 4 and step 6** (unreturned prices; new large fields). These are wrong as fixed-V statements (2.1 item 3). Replace
   them by the forward joint moment.
3. **Step 7 / (RLF-3).** The per-history bound must be restated:
   - exponent a = min{θa_bad, a_A}, not a_♯;
   - reference Z(∅) under (ref-a), connected to Z_K^{sf} by (NA-∅) in the NA-1 form including 𝒱_K^{LF};
   - Lemma HS′'s shadow form;
   - C_ℓ = (1 − λ_*)^{−3n_int/2}C_fc.
   HIST-sum consumes this form unchanged. n_H then becomes ≈ 10²², so W = 2n_♯ + 5 and the number of wrap levels
   (≈ log_L W ≈ 46, or ≈ 60 per REVIEW_SF_S5) make the (SF-last)/torus clause a many-level item (A7), not O(1).
4. **Non-circularity, three checks the integrator must add.**
   - (a) **(SDP)^A at level k is built from the stage-(k − 1) representation.** Node A must not consume (H-w′) or HIST-sum at
     levels ≥ k (HW §19 note). The laws ℛ_𝔥^↑ carry the history indicators of coarser levels, so their U_{≤k} marginal is tilted
     by the future probability. That tilt is (LI)'s content, and it must enter (SDP)^A only through (LI^F) [inference].
   - (b) **FI-1** (§4.4) says the stage-k constants depend on g_k and g_{k±1}. By F-mono, the g_{k+1}-dependence (HIST H1-H4)
     uses (F_R) at (k, k + 1), i.e. a datum one level beyond [0, k], and g_{k+1} is itself an output of stage k (through
     δβ_k). The fixed point is consistent only if the kernel coupling sequence is fixed first (A5's fixed-point reading, l.89),
     or if CL^J's Setting is stated with an a-priori bracket for g_{k+1} [inference; not checked against F-ind's proof]. §4.4's
     "met by the structure" should name this.
   - (c) **S4-5.** (RLF-5)'s width and (I_k^E)″ (b″) cannot both hold for the same polymers. Until node A chooses one, steps 3
     and 5 cannot both use their stated complex domains.
5. **K-list after the lanes.**
   - K1 resolved. K4 resolved modulo HIST's restatement and H3. K5 resolved for bad cubes. K7 is now S4-5 (binding).
   - K2 open. K3 open for the R-operation, moot for HW. K6 extended by τ_c and (TH-ch′/″).
   - K8 and K9 not re-checked (EXISTENCE not read). K10 superseded: v2's own row weights are stale (P/s on (H-w), (BG)_k,
     (MSG)).

### 2.3 Other checks of v2's own text
- §0 η_1 ≤ η_q (l.66-67): for ε_1 ≤ 2, ε_1²/(512NA_d) ≤ ε_1/(256NA_d). CORRECT.
- §0 "g_j² ≤ g_K²/(1 − Rg_K²)" (l.94): from u_j − u_K ≥ −R. CORRECT. It agrees with F-mono (ii).
- §1.2 (RLF-δ)_k (l.173-175): the bound uses g_k ≤ γ_0 only. CORRECT as a statement. But γ_0 must satisfy
  Cg^{−p}e^{−a/g²} ≤ g⁶ with a the binding exponent. At a_coh ≈ 10⁻¹⁶ε_1² and ε_1 ≲ 10⁻³⁹ this is g² ≲ 10⁻⁹⁵, astronomically
  small but g-independent [arithmetic].
- §5.2 K-uniform constants: unchanged by the lanes, apart from W8.

---

## Part 3. The rebuilt critical-path DAG of OPEN items to UV stability (job 1 (c))

Class tags: **[BFT]** a clause of BFT (REVIEW_S22 Part 5 / PROOF [S23]); **[A]** node-A small-field item (SF, PLD, PROOF
N2-N6, HIST's (I^E)); **[FLOW]**; **[HW]**; **[R]** RLARGE-owned; **[other]**. Weights P/s from the owners where given.
Only OPEN, ARGUED or GAP nodes are listed; proven nodes appear only as conditional edges (C).

```
L6-soft (UV stability)  ⇐ (RLF-1) + (RLF-3') + (RLF-4) + node-A bulk bound + assembly C [other, P: CMP 119]
│
├─ (RLF-3') per-history bound, exponent a = min{θa_bad, a_A}   ⇐ HIST-sum (C) ⇐ (H-w')
│   (H-w') (C: HW^cap + REL-seq + H4-red')  ⇐
│     ├─ (F_R), g_K² ≤ 1/(2R)                                   → FLOW branch below
│     ├─ (CLS-min)  ⇐ (REG-min) [A/SQ, OPEN, P]  ⇐ (MIN-reg)_cone [A/SQ, OPEN; "close to circular" with (BFT-cone)]
│     │      parallel: ⇐ CLS-cone (C) ⇐ (AE) (C) ⇐ (MS-Sob) [HIST/SQ, OPEN] ⇐[ARGUED] MSG-loc-dev + MS-HLS + (SQ-dev) [OPEN]
│     ├─ (LI^F) capped future-tilt bound [HW, OPEN]
│     ├─ (M-f^A)_θ ⇐ (SF-cap)^A [A, OPEN] + (SDP)^A [A, OPEN, P]
│     │      (SDP)^A ⇐ (I_{k-1}^E)'(d) + (CLS-min) + (W1-ret'^J)(c) + (SC)_k [A/PLD, s-P] + I-tay^J [R/HIST, s]
│     │                + R1^J gas on σ-good part: I-σ [R, s], I-σ^J + σ^J_Q statement (K2) [R/HIST, s]
│     ├─ (KS-N) for SU(N ≥ 3) [HW, HYPOTHESIS, s]
│     ├─ collar-bad family: W-cb with (TC) [HW, OPEN] (not covered by HW^cap)
│     └─ (NA-∅), NA-1 form with 𝒱_K^{LF} [A, OPEN]          (connects Z(∅) to Z_K^{sf})
│
├─ (RLF-2) returned contributions / (RLF-0) counterterms
│     ├─ (W1-ret'^J)_k (a)-(b) ⇐ (SC)_k [A/PLD] + (SF-irr)_{k+1} [A, the A4 wall] + I-tay^J [R/HIST]
│     ├─ (H-Mayer^J)_k [HIST, ARGUED, s]
│     └─ RLF-step v2 assembly [R, ARGUED]: rewrite §3 (V-1), §4.3 steps 4/6 (R-1), FI-1 g_{k+1} bracket [R]
│
├─ (I_k^E)'' [A/HIST, HYPOTHESIS, P]
│     ├─ Theorem A5 [ARGUED] ⇐ (a5-G♯) + (R♯) [A/PROOF-N2, OPEN] + (a5-U) [HIST, OPEN] + (a3-q) [HIST, OPEN] + (MS-Sob)
│     ├─ (a4) [HIST, ARGUED]; statement fixes S4-1, S4-2 [HIST, s]; CL^J Setting restatement for K4 (H1-H5) [HIST, s]
│     └─ S4-5: (RLF-5) width vs (b'') — node-A norm decision [A / lead, binding]
│
├─ (SF^J)_k = node A1-A4 [A, P×3-4]
│     ├─ A1.k, A1.loc; A3 composition at k ≥ 1; (GF-dec)_k; (GF-B^𝔥); (DX-loc-3), (DX-loc-4) [SF, OPEN]
│     ├─ stage 0: (CH-c) (C) ⇐ DX-rel ✓ + (DX-loc) + E10 [R/SF, OPEN] + CH-3 scope;  (SG^fl)_0 (C) on the O-chain
│     ├─ (SG^fl)_k, k ≥ 1 [A/PLD, HYPOTHESIS]; (SF-last) incl. ≈ 60 wrap levels [A/R, HYPOTHESIS]
│     ├─ (C_♭-eval), C_Δ evaluation (binding iff C_Δ ≳ 1.2·10²¹) [A/PROOF, OPEN, s]
│     └─ N5 level-uniformity ⇐ BFT-0, BFT-1 (θ_w = 0), BFT-2, BFT-4; (MIN_1); small tori; FP_U background dependence [A/PROOF]
│
├─ BFT [BFT, OPEN, P]
│     ├─ BFT-0/1/2 ⇐ (H-lin^∇) [⇐ (H-inv+): (CO-0) = (G♯_0-lev0), (CO-up), (G♯-rough) curvature half, (SB)] + (Res-Hölder)
│     │            + LRL (b) + (H-rem^∇) third order [ARGUED] + (FP♯') + background slice (N1); PROOF's (CL-4) (identification)
│     ├─ BFT-3 (= RLARGE (BG)_k, R_bg; = FLOW (SF-bg) at trivial field): k = 1 ✓; k ≥ 2 ⇐ weighted (H-inv+)_m
│     ├─ BFT-4 (= (CL-cl), (H-C⁺), level-uniform (H-G)): k = 1 ✓; k ≥ 2 ⇐ (W-comm) [GAP 1] + (CovLift) + (Mult-Y) + (Pair-loc), (I-id)_Z, (E3^∇) [ARGUED]
│     └─ BFT-5 [no status anywhere] ⇐ (G♯_0-field) + (R♯_ω) + (G♯-patch); SQ needs θ_w > 1 stated + cone-box uniqueness clause
│
└─ (F_R) along the chain's own sequence [FLOW, node A5, P]  ⇐ F-flow (C) ⇐ (UNIV-1L) ⇐ Theorem UNIV ⇐
      (L-loc2) [ARGUED] + (VFINE) [s] + (VC-V) [s] + (DEF) [s-P, the crux] (session 10, unreviewed);
      reviewed list: (V-IR) form (Q1)(d), vector off-shell defect;  k-uniform vector step gap [s];
      + (SF-g), (SF-cont), (SF-∞) [layer-1, ⊂ node A]; (SF-bg) = BFT-2, 3 at trivial field;
      + (RLF-δ)_k per level, FI-1 [R]
```

**Open items on the critical path, grouped by owner file.**
- **RLARGE.md [R]:**
  - V-1 (re-base §3 on HW), R-1 (§3.3 and §4.3 step 6), the restated (RLF-3′);
  - I-σ; I-σ^J with σ^J_Q (K2); I-tay^J (shared with HIST);
  - E10 (shared with SF);
  - FI-1 with the g_{k+1} bracket; (RLF-δ)_k;
  - the (SF-last) wrap-level clause;
  - recording a_coh as binding and g² ≪ ε_1²·10⁻¹³;
  - adding τ_c and (TH-ch′) to [v2-C].
- **HW.md [HW]:** (LI^F); (KS-N); W-cb's (TC) for collar-bad cubes.
- **Node A [A].** SF.md: A1.k/A1.loc, the A3 composition, (GF-dec)_k, (GF-B^𝔥), (DX-loc-3/4), (CH-c)'s inputs.
  - PLD.md: (SC)_k, (SF-irr)_{k+1}, (SG^fl)_k.
  - HIST.md: (I_k^E)″ with (a5-U), (a3-q), (a4), S4-1/S4-2, the CL^J restatement, (H-Mayer^J).
  - SQ.md: (REG-min) ⇐ (MIN-reg)_cone (or, in parallel, HIST/SQ (MS-Sob)/(SQ-dev)).
  - PROOF.md: (R♯), (a5-G♯) (with lane F), (CL-4), (MIN_1), small tori, (C_♭-eval), the C_Δ evaluation, FP_U's background
    dependence.
  - Node-A interface items: (SDP)^A, (SF-cap)^A, (NA-∅), the S4-5 decision.
- **BFT_A.md / BFT_B.md [BFT]:**
  - BFT-0/1/2: (H-inv+) [(CO-0), (CO-up), (SB)], (Res-Hölder), LRL (b), (FP♯′), (N1);
  - BFT-3 at k ≥ 2: weighted (H-inv+)_m;
  - BFT-4 at k ≥ 2: (W-comm) GAP 1, (CovLift), (Mult-Y), (Pair-loc);
  - BFT-5 (unowned; no status anywhere).
- **FLOW.md [FLOW]:** (L-loc2), (VFINE), (VC-V), (DEF) (crux); (V-IR) (Q1)(d); the k-uniform vector step gap.
- **Other:** the assembly C [P].

**Shared objects (one proof, several consumers):**
- (H-inv+) feeds BFT-0/1/2, BFT-3 and BFT-4.
- (CLS-min) feeds HW and (SDP)^A.
- BFT-3 serves as RLARGE's R_bg and as FLOW's (SF-bg).
- I-tay^J feeds (W1-ret′^J) and (SDP)^A.
- E10 feeds RLARGE (collar-bad family) and SF (CH-c).

---

## Part 4. Job 2: PROOF session 23's two hand numbers, and the consolidation spot-check

### 4.1 The κ window (PROOF l.5669-5672, l.6599)
Formula: e_κ := e_0 + δk_0 + |κ_0 − 1|qk_0, 𝔠 finite iff e_κ < 1, so W = (1 − e_0 − δk_0)/(qk_0), with q = 161215/985608,
k_0 = 132.842054, e_0 = 0.4381436. δ = C_Δα_* is recomputed from its definition: m_4 solves (449171/10935)m(1 + 40m) = γ_0/4,
and C_Δα_* = γ_0/(4e^{20m_4}). Interval results (60 digits; the inputs are PROOF's decimals):

| class | γ_0 used | m_4 | δ = C_Δα_* | 𝔠_∞^♯ | exact W | e_κ at PROOF's endpoint |
|---|---|---|---|---|---|---|
| session 23 (λ_min CI-0) | 4.229507·10⁻³ | 2.571523·10⁻⁵ | 1.056833·10⁻³ (δk_0 = 0.140392) | 315.1926 | **1.93965·10⁻²** | 1.000075 at 1.94·10⁻² |
| old ([S19]-[S20]) | 1.587·10⁻⁸ | 9.65882·10⁻¹¹ | 3.96750·10⁻⁹ | 236.4344 | **2.58576·10⁻²** | 1.000052 at 2.586·10⁻² |

- The lead's "≈ 1.94·10⁻²" is CORRECT as an approximation (rounded δ = 1.0568·10⁻³ gives 1.939674·10⁻²). As a strict bound,
  "|κ_0 − 1| < 1.94·10⁻²" is slightly too large. Write **< 1.939·10⁻²**.
- The old-class "< 2.586·10⁻²" (l.5669, l.6599) is WRONG in the fourth digit, the same error class as KW-1 itself. REVIEW_SF_S7
  fix KW-1 (l.163, l.299) prescribes **"< 2.585·10⁻²"** (e_κ = 0.99983 there). B-5's "exact window 2.5858·10⁻²" is correct
  (2.58576). PROOF quoted the rounded-up value instead of the fix.
- 𝔠_∞^♯ = 315.19 and 236.43 are reproduced (REVIEW_SF_S7 has 236.434155 from unrounded inputs).
- Caveat: the window holds δ at its κ_0 = 1 value. Off κ_0 = 1, CI-0's certified λ_min (hence m_4 and α_*) is not re-certified.
  The window formula follows REVIEW_SF_S7 C-3's substitution and inherits that scope.

### 4.2 coth⁴(m_1/2) in CURV1's C_θ (PROOF l.6094-6105)
| m_1 = m_4/2 | coth⁴(m_1/2) |
|---|---|
| 1.2857613·10⁻⁵ (m_4 recomputed from γ_0 = 4.229507·10⁻³) | **5.85435·10²⁰** |
| 1.28575·10⁻⁵ (PROOF's quoted m_4 = 2.5715·10⁻⁵) | 5.85455·10²⁰ |
| 4.83·10⁻¹¹ (N5-w0's m_4 = 9.66·10⁻¹¹) | **2.93989·10⁴²** |

- Both factors CONFIRMED: the lead's 5.9·10²⁰ (two figures) and the old 2.9·10⁴².
- **The term is much larger than the factor.** C_θ's term is 288·A_in·coth⁴(m_1/2)·ℓ_θ.
  - Lemma LOC (l.5822) defines A_in = 16coth⁴(a/2)e^{m_1r_1}C_Δ/(γ′γ_0), with a = m − m_1 = m_1. So the term carries coth⁸.
  - ℓ_θ ≥ 2D_g/L + 3, where D_g ≥ (2/m_1)ln(832c_Kcoth⁴(m_1/4)/θ) and c_K ≥ 2/γ′, θ ≤ 1, t_Z ≥ 0.
  - Rigorous lower bounds: on the session-23 class (γ′ = 3.17267·10⁻³), A_in ≥ 6.98·10²⁶C_Δ, D_g ≥ 9.92·10⁶, ℓ_θ ≥ 6.61·10⁶, and
    **288A_incoth⁴(m_1/2)ℓ_θ ≥ 7.8·10⁵⁶·C_Δ**.
  - On the old class: A_in ≥ 1.87·10⁵⁹C_Δ, ℓ_θ ≥ 3.48·10¹², **term ≥ 5.5·10¹¹⁶·C_Δ**.
  - REVIEW_SF_S7 E-3 ("the coth⁴(m_1/2) term (≈ 10⁴²)") and PROOF l.6104-6105 ("≈ 10⁴² and more"; "5.9·10²⁰, still dominant")
    name the factor, not the term.
  - The conclusion "CURV1 is NOT yet usable; (c_K, m_1) must be replaced by CI-bg's (730.4, 0.02), and LOC's A_in, A_out are not
    covered" is reinforced. With m_1 = 0.02, coth⁴(0.01) ≈ 10⁸, and the coth⁸ term would be ≈ 10¹⁶·C_Δ·ℓ_θ/(γ′γ_0) [hand
    arithmetic, not run]; it needs LOC re-derived with CI-bg's rate.
- **Fix N-1 (for the ledger owner):** replace "coth⁴(m_1/2) ≈ 5.9·10²⁰, still dominant" by "288A_incoth⁴(m_1/2)ℓ_θ ≥ 7.8·10⁵⁶C_Δ
  (A_in ∝ coth⁴(m_1/2) as well; ℓ_θ ≥ 6.6·10⁶)". Optionally correct the old-class "≈ 10⁴²" to "≥ 5.5·10¹¹⁶C_Δ".

### 4.3 Spot-check of the S23 consolidation (11 edits sampled against REVIEW_S22 l.436-500 and REVIEW_SF_S7 E-2/E-3)
| # | fix | PROOF place | verdict |
|---|---|---|---|
| 1 | S22-1 c38: R_3(ℤ⁴) ∈ [1.40, ≲ 60]; N3^abs 73.2/90.8/111.1/131.9; torus N3 a lower bound | l.50, 6433-6437 | FAITHFUL |
| 2 | S22-3(a) Ad(h) − 1 term 648ℓ_{θ′}p_L𝔠_∞ε² in C_G | l.6303-6304 (9α·2p_Lr with α = 3ℓε, r = 12𝔠ε = 648ℓp_L𝔠ε²: arithmetic checked) | FAITHFUL |
| 3 | S22-3(b) near/far split, far part 30κ_0p_L𝔠_∞ε into D_g, box-nesting condition | l.6345-6351 | FAITHFUL |
| 4 | S22-4 r^{(i+1)} := 2𝔠_∞^{(i+1)}κ_i(N_0(\|𝒦_ρ^{(i)}\|) + 1)ε; (iv)-route ≥ 10³ per level | l.6370-6373 (≥ 1.1·10³) | FAITHFUL |
| 5 | S22-5 CURV-F2″ θ-cascade, ε_unif = O(1/k), NAH-unif′ GAP, "derived at each fixed level" | l.6386-6407, header l.8-10 | FAITHFUL |
| 6 | S22-6 (CL-0) additions (𝔊_k into S_k, 𝔊_kHess = 1 on S_k) and (CL-4) | l.6502-6513 | FAITHFUL |
| 7 | S22-8 (CL-cl) as BFT-4, "⇒ (BG-unif) (iv)" not "⊂" | l.6548-6550 (the original "⊂" at l.6542 is kept with the correction appended) | FAITHFUL |
| 8 | SF7 E-3 edit 1 + KW-1 window "< 2.585·10⁻²" | l.5669, 6599: "< 2.586·10⁻²" | **UNFAITHFUL (minor)**: rounds past the exact 2.58576·10⁻² (4.1) |
| 9 | SF7 edit 2 (ε_br, 1.25·10⁵ / 9.4·10⁴; level ≥ 1 not covered) | l.5953, 6008 (×8·10⁻⁶ is the 0 → 1 step) | FAITHFUL (1 + 396·315.19 = 1.248·10⁵; 1 + 396·236.43 = 9.36·10⁴) |
| 10 | SF7 edit 5 arithmetic + "REJECT usability" + (c_K, m_1) from CI-bg + LOC not covered | l.6100-6107 | FAITHFUL arithmetic (3.81·10⁹, 1.101·10⁻⁶, 9.0·10⁹, 8.26·10⁻⁷, 6.83·10⁹, 1.21·10¹⁰ re-derived); the "≈ 10⁴²" magnitude is the reviewer's own understatement (4.2) |
| 11 | SF7 edits 3, 6 (gap 3.1727·10⁻³ on the session-23 class; C_Δ named as binding, 8.4·10⁹ old / 1.2·10²¹ new) | l.5449-5451, 5735-5739 | FAITHFUL (matches REVIEW_SF_S7 l.54, 215, 221) |

**Verdict:** the consolidation is faithful except one fourth-digit window value. Not applied by design and correctly recorded
as SF-internal: TB-1, PV-1, the §20.1 leftover (l.6600).

---

## Required fixes

**For the RLARGE owner (v3):**
1. Update every row of Part 1 (31 statuses).
2. **V-1 / R-1.** Rewrite §3 and §4.3 steps 4 and 6 around HW's forward joint moments. Delete the e^{B_0} absorption claim.
3. Restate (RLF-3) with a = min{θa_bad, a_A}, the reference Z(∅) plus (NA-∅) in the NA-1 form, and HS′'s shadow form.
   Recompute n_H, W and the wrap-level count.
4. Add to §4.2: (SDP)^A, (SF-cap)^A, (NA-∅), (LI^F), (KS-N), W-cb/(TC), S4-5, (CH-c), the CL^J restatement, and the FI-1
   g_{k+1} bracket.
5. Record a_coh as binding, g² ≪ ε_1²·10⁻¹³, the ε_1 ceiling ≲ 6.7·10⁻⁴⁰, and τ_c/(TH-ch′) in [v2-C]. Add a reading note to
   Appendix A's c32/c33 (ε_1 = 0.5).
6. Mark K1, K4 (modulo HIST), K5 (bad cubes) resolved. K7 → S4-5.
7. Replace §7 by Part 3's DAG.

**For the PROOF owner:**
- KW-1 window "< 2.585·10⁻²" (old class) and "< 1.939·10⁻²" (session-23 class).
- Fix N-1 (the coth⁸ term).

**For HIST:** the CL^J Setting restatement (F-mono H1-H5, including H3), and HIST l.1683's stale A5 status.
