Reviewer model: claude-opus-5-5

# REVIEW55_ARS — Opus 5.5 re-review of batch C6: the a_RS / KN-step complex (sessions 24-25)

## PRE-STATED (written 2026-10-28T22:12:57Z UTC, after reading only the shared brief and the lead's scope
message; before reading any batch file, any source range, or the Codex KN review)

Batch files: ARS_FIX.md, REVIEW_ARS_EPS_S1.md, KN_ADOPT.md, ARS_BIND.md. Source: RLARGE.md (by range).
Cross-family input: CODEX_REVIEW_KN.md (read as it is on disk; re-read before finishing). Check ids: r55a_*.
No git. The only file I write besides checks/r55a_* (criteria + scripts + outputs, criteria first) is this one.

Targets, in order, each with what would count as a refutation (statements only; nothing derived yet):

T1. "a_RS binds nothing on the live v3 route" (ARS_BIND) vs "a_RS binds today by 15.6 decades; a linear
    threshold gains 82.141 decades" (ARS_FIX) vs "real gain +2.303 over Lemma RS-lin" (REVIEW_ARS_EPS_S1).
    Method: grep the WHOLE lane (not just RLARGE) for a_RS, a_♯, n_♯, e^{a_RS} and every spelling variant;
    for each hit decide (i) frozen appendix / historical vs live, (ii) whether it feeds an inequality that is
    a hypothesis or conclusion of the live RLF-step v3 statement. REFUTES ARS_BIND if any live hypothesis or
    live chain step consumes a_RS (or its input) in a way that sets a binding margin. REFUTES ARS_FIX's
    "binds by 15.6 decades" if every consumer is outside the live route. The "+63.619 decades" for
    a = θ·a_bad = 1.040e-86 is REFUTED if my exact recomputation (rational interval logs) of the stated
    margin differs beyond rounding, or if the symbols a, θ, a_bad or the ceiling are not the objects the
    live statement uses (symbol-collision check by file:line).
T2. ARS_BIND's eight failed construction routes (K1-K8), especially K7 and K8: does each failure argument
    actually fail for the stated reason? REFUTES a "route fails" verdict if I can exhibit the construction
    working, or show the stated obstruction is not one; REFUTES a "route works" verdict symmetrically.
T3. H1 / KN-step': (a) the S4' averaging weights are the uniform (d!L^d)^{-1} = 1/1944 at PROOF.md string
    "M̄_c(U) := (d!L^d)^{-1}" (REFUTED if the definition there is not uniform, or d!L^d != 1944 at the lane's
    d, L); (b) RLARGE's (R1) second clause already consumes the convexity KN-step' needs (REFUTED if (R1)'s
    second clause is a different inequality, is not convexity-based, or is stated for a different object).
T4. Degeneracy count of distinct transporters: KN_ADOPT says 633 with weights {1/1944, 1/486, 1/162, 1/81};
    Codex says 633 = (y, axial-path) label count and the freely reduced paths number 475 with weights incl.
    1/324, 5/486, 2/81, 1/27. I will ENUMERATE it myself from the definition in PROOF.md (exact rational
    weights). Either claim is REFUTED by my enumeration if the count or the weight multiset differs; if the
    definition admits two readings, I report both counts and say which reading the proof text uses.
T5. KN_ADOPT §8.1 "ε_1 > 814.587 for the other branch" vs Codex "branch boundary is κ = 128/13689,
    independent of ε_1 and N". Re-derive the branch condition from the patch's own inequality. REFUTED side
    = whichever my derivation contradicts; a stale-minimum verdict requires naming the constant it was
    evaluated at.
T6. Reversals against banked items (each must be re-derived, not accepted):
    (a) RLARGE l.65 "η_1 ≤ η_q" claimed false with values 512/13 and 768/13;
    (b) HIST l.186 route comparison (201.029x vs 1551x);
    (c) RLARGE l.618 (FALSE per ARS_FIX, TRUE per ARS_BIND);
    (d) PROOF.md [S24-flag 6].
    A reversal is REFUTED (i.e. the banked item stands) if the banked statement, read with the symbols it
    actually used at its own file:line, is true; it is CONFIRMED if I re-derive the counterexample.
T7. REVIEW_ARS_EPS_S1's "its targets never cite RLARGE §3.5 — zero grep hits" vs ARS_BIND's "false: ARS_FIX
    cites §3.5 at l.294 and l.788". Settled by grep of ARS_FIX for every spelling of the section reference.
T8. Every other PROVEN / PROVEN-HERE claim and every decision-changing number in the four files: re-derive
    the load-bearing step, or mark spot-checked / NOT-VERIFIED explicitly.

Verdict scale per the brief: CONFIRMED (re-derived load-bearing step) / NOT-VERIFIED (say what is missing) /
REFUTED (give the correct statement and its derivation). "The file says PROVEN" is not evidence.

---

## 0. What I read, what I ran, and citation drift

**Read in full:** ARS_FIX.md (901 l.), REVIEW_ARS_EPS_S1.md (631), KN_ADOPT.md (760), ARS_BIND.md (541),
CODEX_REVIEW_KN.md (312; mtime 22:09:30Z, 36 466 bytes, unchanged when re-checked at 22:34Z; it ends with a complete
summary table and a closing sentence — **it looks finished**, not truncated).
**Read by range / string:** RLARGE.md l.1-125, 185-232, 380-450, 500-660, 755-845, 960-1032, 1175-1252 (this exceeds the
lead's suggested ranges because §1.2 (RLF-0)/(RLF-δ) and §3.3-§3.4 turned out to be load-bearing); PROOF.md by string
("S4 Averaging (L1)", "S4' [S3] Order-averaged", "Decision 4: the RG kernel", "[S24-flag 6]", the S24 consolidation
paragraph); HIST.md l.136-192, 738-748 and grep hits; EXISTENCE.md l.1756-1790 and grep hits; EPS1_SWEEP.md l.425-500;
REVIEW_PLD_S3.md l.460-464; REVIEW_SF_S7.md grep hits for DX′; FLOW.md l.210-222, 456-482; SESSION25_RESULTS.md l.38-46;
HANDOFF.md grep; PLD.md, SQ.md, SYMBOLS.md grep hits; the check files ar1_margins.py (l.240-272), ar1c (l.70-80),
kn1_h1.py, kn1_sides_out.txt, ab1_margins.py (DX′ line).

**My checks (criteria file written before each script; exact integers/Fractions only, no floats):**
- `checks/r55a_1_criteria.md` 22:26:38Z → `r55a_1_enum.py` → `r55a_1_out.txt` (22:27:18Z; err file empty except timing).
- `checks/r55a_2_criteria.md` 22:28:38Z → `r55a_2_arith.py` → `r55a_2_out.txt` (22:29:39Z). Every log10 is a rigorous
  rational enclosure (atanh series + explicit remainder; ln10 = 3ln2 + ln(5/4)); √N by isqrt enclosure. Every
  pre-registered verdict is reported below. One cosmetic defect in r55a_2_out.txt: the G5 rows print ε = 10⁻³ as "+0.00"
  (2-digit display); the values on those rows are correct (η ratio 39.3846; η_RS/η_q = 0.000500 = ε/2). Output kept unaltered.

**Citation drift found (locate by string):** KN_ADOPT's PROOF.md l.1754-1755 (decision 4) is now **l.1806-1807**; its
l.711-715 (S4′) is now **l.763-767**; its l.702 (blocks/centres) is now **l.753-754**; its "PROOF.md l.84" ([S25-fix 1])
is now **l.94**. ARS_BIND's "PROOF.md l.6921" is now **l.6950**; its "RLARGE l.829" (cutoff note) is **l.828**.
PROOF.md [S25-fix 1] cites "KN_ADOPT §5" for the 201× rebuild; the rebuild is **KN_ADOPT §3.2** (§5 is the (PLD)_k item).
RLARGE.md is unmodified since 08:03 local, so every RLARGE line cited by the four batch files still matches.

---

## 1. Findings

### r55a-F01 — Does a_RS bind anything on the live v3 route? ARS_BIND's (V-NO): **CONFIRMED** (with one refinement, F03)

My own trace, not ARS_BIND's census:
- **Literal a_RS in RLARGE.md:** exactly l.830, 1020, 1023, 1024, 1247 (grep). All ≥ l.824, the start of
  "# Appendix A. Frozen and one-step content of v1 (§3-§9A), verbatim". l.830 sits in the "v3 reading notes" block
  (l.826-839), which is live v3 text; the other four are frozen v1 text.
- **Lane-wide literal a_RS:** RLARGE, FLOW (l.909/925/975: a consumer TABLE quoting RLARGE v1 §6/§7.1, not a use), PROOF
  ([S24-flag 6]/[S25-fix] and l.6950), SF l.2204 (a sensitivity cell), and session-24/25 work files and reviews (ARS_FIX,
  EPS1_SWEEP, EPS1_EXEC, KN_ADOPT, QFIX, ARS_BIND, SYMBOLS, RTARGET, logs, Codex reviews), plus three RLARGE snapshots.
  **Zero** in HIST, HW, PLD, SQ, BFT_A, BFT_B, NORMS, LINEAR_PACKAGE, EXISTENCE (grep, spellings a_RS, a_{RS}, aRS,
  e^{a_RS, a_{\rm RS}, a^{RS}).
- **The channel ARS_BIND's census does not trace: a_♯** (whose frozen definition l.1024 is min{a″, a_♭, a_RS/c_RS}). a_♯
  occurs in HW (5 lines), HIST (10), FLOW (7), PLD (1), SQ (1), EXISTENCE (≥10). I classified each: HW l.1010-1011 says
  outright HW delivers a = min{θa_bad, a_A}, not a_♯; HW l.458/688 and HIST l.46/564-595/643/699/734 are v1/v2-era
  threshold arithmetic or quotations of v1's (RLF-4), re-pointed by RLARGE v3 (l.171 "(RLF-3′): exponent a … (not a_♯)",
  l.590 "a is HW's a …, not v2's a_♯", l.602 "(P5) … with a in place of a_♯"); FLOW l.219 and HIST l.864/1754 and HW l.930
  are bounds on **returned**-cluster quantities (δβ_k, C³ data), whose v3 exponent is **a_ret** (RLARGE l.192-196, F03);
  PLD l.42 and SQ l.225 are label imports; EXISTENCE l.1882-1886, 3072-3083, 3362-3403 use a_♯ as an opaque exponent
  (RLARGE l.767: "The exponent EXISTENCE should read is a (not a_♯)"). **None reads the value a_RS/c_RS.**
- **Live replacements, verified in situ:** RLARGE l.87-89 (a := min{θa_bad, a_A}); l.94 ("v2's a_♯ formula (§3.4) is
  superseded for unreturned defects (§3.5)"); l.434-439 (§3.5: case split, greedy factors, RS-joint's c_RS = 81, the a_♯
  formula "are **not consumed**"); l.513-517 ("Not hypotheses of RLF-step v3": "(PLD)_k (i)-(ii), (PLD-q)_k", "RS-joint and the
  greedy joint pricing (§3.5)", "Theorem TS / TS_K", "CLS-cone and CLS-red"); l.545 (live constants "(C_ℓ, B_0, E_0, a, n_♯)");
  l.586-590 (n_H from a); l.828 (cutoff n_♯ ≥ max{n^J_*, n_H}); l.832 (a_♯, c_RS = 5⁴, n_♯ := ⌊4/(a_♯β_-)⌋ superseded); l.835
  (§7.3 TS "not used by RLF-step v3").
- **Lemma RS itself in the live body:** only l.64 (η_1's definition), l.421 (kept statement), l.434 (superseded case
  split), l.626 (status list), and "RS ordering" (l.263: "ordering kept; pricing role removed"). **No step of RLF-step v3
  (l.521-545) invokes (R3)-(R5).** η_1 has no live consumer (grep: l.64-65, l.261, l.761 only); η_q has three (l.82-83 (TC),
  l.297 non-quiet definition, l.443 a_cb) — ARS_BIND §7's flag is right.

**Verdict:** no statement the live v3 route asserts or requires changes if a_RS is replaced by another positive real.
(V-NO) CONFIRMED. ARS_BIND's own status word for it ("ARGUED … an exhaustive-search negative") is the right one; my trace
adds the a_♯ channel and finds nothing in it.

### r55a-F02 — ARS_FIX §2.2-§2.3 / §6.1 (V2): "a_RS's ceiling BINDS TODAY; RLARGE l.618 is FALSE" — arithmetic **CONFIRMED**, claim **REFUTED**

r55a_2 G2: a_RS^quad = 5.931360·10⁻¹⁶⁶ at ε_1 = 6.7·10⁻⁴⁰, N = 2, κ = 1; log10((a_RS/10²)/DX′) = **−15.617074** at
DX′ = 2.456·10⁻¹⁵² (REVIEW_SF_S7 l.203) and **−15.624786** at the rounded 2.5·10⁻¹⁵² (RLARGE l.618); with the c_RS = 625
divisor −18.412954. All of ARS_FIX's printed figures reproduce. But the quantity is consumed by nothing (F01): "binds" is
a statement about a superseded object. ARS_FIX's own pre-registered (G6) failure mode named exactly this; §2.3 quoted
l.832 *including* "(a = min{θa_bad, a_A})" and did not follow it. **Correct statement:** "a_RS/10², if anything consumed it,
would sit 15.62 decades below DX′; nothing on the live route consumes it."

### r55a-F03 — RLARGE l.618 "RLF's own ceilings do not bind": ARS_BIND's "TRUE AS WRITTEN" — **CONFIRMED for two of the three items l.615 names; NOT-VERIFIED for (RLF-δ)**; ARS_BIND (K7b) "all three carry exponent a" — **REFUTED**

l.615 names "HIST-sum's, REL-seq's and (RLF-δ)'s smallness conditions". HIST-sum and REL-seq carry **a** (l.588-591). But
**(RLF-δ) does not**: RLARGE §1.2 l.192 (|c̄_0^{sea}| + |δβ_k| ≤ Cg_k^{-p}e^{-a_ret/g_k²}), l.195-196 ("**a_ret** denotes the
exponent of the returned-cluster bounds …; **no source states its value** (v2's a_♯ list … was a formula for the joint price
of defects; unresolved item U1)"), l.198-201 ("The γ_0 needed for Cg^{-p}e^{-a_ret/g²} ≤ g⁶ is g-independent but
astronomically small"), K12 at l.780-781. So l.615's "all have the form e^{-a/g²}" is an internal inconsistency of RLARGE v3,
and l.618 is **unevaluable** for (RLF-δ) until U1 fixes a_ret. This does **not** revive a_RS: l.195-196 and l.781 say
explicitly that v2's a_♯ formula is not the returned-cluster exponent. It does mean "l.618 TRUE as written" ([S25-fix 4])
overstates by one item. Neither ARS_FIX nor ARS_BIND nor Codex noticed it.

### r55a-F04 — "the live exponent a = θa_bad = 1.040·10⁻⁸⁶ clears DX′ by +63.619 decades" — **CONFIRMED with three qualifications**; ARS_BIND's error attribution — **REFUTED**

r55a_2 G3: c_pr = 1/(640·53²) = 1/1 797 760 (RLARGE l.90-91); a_bad = 2.496996·10⁻⁸⁵; a = a_bad/24 = 1.0404151·10⁻⁸⁶
(reproduces A7 to 1·10⁻⁷ relative). Margin **+63.619267** at DX′ = 2.5·10⁻¹⁵², **+63.626978** at DX′ = 2.456·10⁻¹⁵².
Qualifications: (i) θ < 1/24 is **strict** (CAP-1, l.88), so +63.62 is a supremum, not attained; (ii) a = θa_bad presumes
a_A ≥ θa_bad, which is **U1** (open; l.89 "If a_A < θa_bad, θ is lowered"); (iii) it is the (REG-min) route; via (AE)
a_bad ≈ 10⁻⁹⁴ (l.93) and the margin is ≈ +54. With θ = 1/96 ([HW-2]) the margin is +63.025; with the collar's θ = 1/(96·82)
+61.111 (reported, not pre-registered). **No qualification changes the sign.**
**ARS_BIND §6's attribution** "(A8) differs … because the review carried −15.617 where the exact figure is −15.6248" is
wrong: the two figures differ by exactly log10(2.5/2.456) = 0.0077116 (G3 ATTRIBUTION → **DIFFERENT-DX-INPUT**).
`ab1_margins.py` l.26 uses DX′ = 2.5·10⁻¹⁵² (RLARGE l.618's rounding); ARS_FIX/REVIEW use REVIEW_SF_S7 l.203's 2.456·10⁻¹⁵².
Both are exact at their own input. Immaterial to every verdict; recorded so the "+63.619" is quoted with its DX′.

### r55a-F05 — ARS_BIND §5's eight failed construction routes — **CONFIRMED for K1-K6 and K8; K7 CONFIRMED in conclusion, half (b) REFUTED as worded**; one route missing (K9)

- **K1 (cutoff n_♯):** l.828 (n_♯ ≥ max{n^J_*, n_H}, n_H from a), l.439/l.1024 (R1/R1^J hold for every n_c ≥ n_*). CONFIRMED.
- **K2 ((R4) → (M-i)):** l.386-390: (M-i) ⇐ H4-red′ ⇐ (LI^F) via Lemma KS (c); C_ℓ = (1−λ_*)^{-3n_int/2}C_fc (l.414). No (R4). CONFIRMED.
- **K3 (collar):** l.443 a_cb = min{c_pr·min{ε_loc²/4, t_pr²}, κε_loc²/(64N), c_pr·min{η_q², t_pr²}} — η_q, not η_1/a_RS. CONFIRMED.
- **K4 (TS):** l.835, l.517, and frozen l.1204 ("Proposition RLF-step (§8.3) does not use TS"). CONFIRMED.
- **K5 (EXISTENCE):** opaque exponent; RLARGE l.767 re-points it to a; zero a_RS in EXISTENCE. CONFIRMED; residual stale
  label (U11), as ARS_BIND says.
- **K6 (l.830's e^{a_RS R}):** the factor repairs frozen l.1003-1007's "(1/g_i² ≥ 1/g_{i+1}² under (F))" and frozen l.1023's
  conversion; the live route prices "at its own level's coupling u_j, so the defect price itself carries no e^{aR}"
  (l.114-116) and uses e^{aR} at **a** (l.586-589). CONFIRMED: not a consumer.
- **K7 (ARS_FIX's construction):** (a) Lemma RS's clauses (R1)-(R5) (l.972-981) contain no a_RS — CONFIRMED by reading.
  (b) "l.615-617 … three named items, all of which carry exponent **a**" — **REFUTED for (RLF-δ)** (exponent a_ret, F03).
  The kill still holds, because a_ret ≠ a_RS by l.195-196.
- **K8 ((PLD)_k (i) off-route):** l.513 lists "(PLD)_k (i)-(ii), (PLD-q)_k" among "Not hypotheses of RLF-step v3"; l.1020 says
  "a_η from (PLD)_k (i)". So at effective levels a_RS has no live supplier. CONFIRMED (the cleanest kill, as ARS_BIND says).
- **Missing route K9 (mine): the returned-cluster exponent a_ret.** (RLF-0)/(RLF-2)/(RLF-δ) need a_ret, value unstated (U1,
  K12), and l.420-422 keeps "Lemma RS (R3)-(R4) … for the representation route". If node A's eventual (W1-ret′^J) bound were
  built on RS's dichotomy at effective levels with a (PLD)-type plaquette price, an a_RS-type quartic could re-enter there.
  **Today it does not** (no source states a_ret; v3 decouples it from the a_♯ formula), so (V-NO) stands; this is the one
  door through which it could come back, and it is the same item l.615 mislabels (F03).

### r55a-F06 — H1 (KN_ADOPT §1.2): the S4′ weights are uniform (d!L^d)^{-1} = 1/1944 — **CONFIRMED**; "(R1)'s second clause already consumes the convexity" — **CONFIRMED**; "‖M̄_c‖ ≤ 1 holds *iff* the weights are a probability vector" and "if H1 failed, RLARGE (R1) would be false" — **REFUTED**

PROOF.md "Decision 4: the RG kernel" (now l.1806): *"M̄_c(U) := (d!L^d)^{-1}Σ_σΣ_{y∈B(X)}T^σ_y(U) be the mean of the S4'
contour transporters (S4' pairing: the same order σ at both ends). ‖M̄_c‖_op ≤ 1."* The index set is S_d × B(X) (PROOF
"S4' [S3]": "For each of the d! coordinate orders σ"; "S4 Averaging (L1)": blocks of side L with centres c_X), so |I| = 24·81
= 1944 and every weight is 1/1944 > 0, summing to 1. RLARGE l.992 ("So δ_c ≤ A_d(L)η, and M̄_c is a mean of the T^σ_y") is
the justification of (R1)'s "hence ‖M̄_c − S_c‖ ≤ A_d(L)η" (l.973), and that step is ‖Σw(T−S)‖ ≤ Σw‖T−S‖ ≤ max‖T−S‖ — it
uses w ≥ 0, Σw = 1. So the adoption imports no hypothesis RLARGE's own argument does not already use. **ARS_FIX §6.2's
"CONDITIONAL on one word" was over-cautious** (it looked only in RLARGE, where the weights are indeed not written).
But KN_ADOPT §1.4's "**iff**" and "If H1 failed, RLARGE (R1) would be false as written today" are wrong: a proof that uses
a hypothesis does not make the conclusion false without it. Codex F5's counterexample checks out by hand:
z = (99+20i)/101 (|z| = 1), T_± = diag(z, z̄)^{±1}, weights (1, 1, −1) on (T_+, T_−, I) give M = (97/101)I, ‖M‖ < 1 and
‖M − I‖ = 4/101 ≤ max‖T_i − I‖ = 2/√101, while M is outside the convex hull (diagonal real parts there are ≥ 99/101).
KN_ADOPT §8.4 item 1's "If decision 4's kernel is ever restated with a reweighted … or field-dependent average, three
statements break at once" is likewise too strong: any pointwise nonnegative normalised weights preserve both norm bounds
and the KN algebra (Codex F5, agreed).

### r55a-F07 — H1-F2 ruled out; W′_c = the S4′ coarse link U′(c) on D′ (KN_ADOPT §1.3, §1.5) — **CONFIRMED** (where Codex could only say NOT-VERIFIED)

Codex F5 left the source identity NOT-VERIFIED because it did not open PROOF.md. I did: the RG kernel (decision 4) averages
exactly the paired contours T^σ_y = P^σ(c_X → y)·S_y·P^σ(c_Y → y + Le_μ)^† of PROOF "S4' [S3]"; RLARGE §6's δ_c is the max over
"the S4' contours of c" (l.970) and its (R4) consumes M̄ through D4-norm (2) (l.996), the kernel of decision 4 (PROOF l.1808-
1809: k_c := exp(−(κ/g²)[1 − N^{-1}Re tr(V_c^{-1}M̄_c(U))])/𝒩(M̄_c(U))). And PROOF "S4' [S3]" defines
U′(X, X+e_μ) = S_{c_X} exp((1/d!)Σ_σ L^{-d}Σ_y log(S_{c_X}^{-1}T^σ_y)) on D′ — character for character W′ = S e^{X̄} with the
uniform weights. One object throughout. (The inherited-symmetry remarks are true on D′ but not needed by KN′; Codex F10's
advice to drop them from a local append is sensible.)

### r55a-F08 — The degeneracy count (KN_ADOPT §1.6, kn1-1): **633 is CONFIRMED as the (y, axial-path) label count; "633 distinct transporters" with weights {1/1944, 1/486, 1/162, 1/81} is REFUTED — there are 475**, weights {1/1944, 1/486, 1/324, 1/162, 5/486, 2/81, 1/27}

r55a_1 (criteria first): E1 1944 index pairs; E2 633 labels, histogram {1:384, 4:192, 12:48, 24:9} (**LABELS-633-CONFIRMED**);
E3 **475** freely reduced full transport words, histogram {1:288, 4:96, 6:48, 12:12, 20:24, 48:6, 72:1}
(**REDUCED-475-CONFIRMED**); E5 the closed form Σ_{k=0}^{3}C(3,k)2^k k!(1+2k) = 475 (**AGREES**); E6 both partitions
nonnegative and summing to 1 exactly (**CONVEX-PRESERVED**). The decisive leg is **E7**: on two generic gauge fields with every
link an exact rational unit quaternion (SU(2)), the 1944 holonomies take **exactly 475 distinct values** on each field, and
every reduced class is constant — so 475 is the number of distinct transporter *values*, independent of my reduction code
(**PASS**). Controls: C1 switching off free reduction gives 633 (FIRES — the gap is reduction alone); C2 an unpaired far end
gives 631 values (FIRES); C3 the identity field gives 1 value (FIRES). The mechanism: a μ-step of the axial path placed
after every transverse step cancels against the straight leg (e.g. all 72 indices with y − c_X ∈ {−e_μ, 0, +e_μ} give S_c,
weight 1/27, absent from KN_ADOPT's list). KN_ADOPT's `kn1_h1.py` keyed on (y, order of moving coordinates) and labelled the
result "distinct transporters"; the normalisation gate could not catch that (it passes for any partition). **Harmless for
H1** — merging equal terms preserves a probability vector — but the stated refinement is wrong. Codex F1: **agree**.

### r55a-F09 — Lemma KN′ and Corollary KN-step′ (ARS_FIX §3.2, KN_ADOPT patch (R3′)/(R4′)): **CONFIRMED** (re-derived)

Re-derived step by step: R := W′^{-1}M̄ − 1 = Σw(e^{−X̄}−1)(e^{X_i}−1) + (e^{−X̄}−1+X̄) + Σw(e^{X_i}−1−X_i) is exact given
ΣwX_i = X̄ (H1); ‖X̄‖ ≤ δ (H1); ‖R‖ ≤ (e^δ−1)² + δ²e^δ ≤ δ²(e^{2δ}+e^δ) ≤ 3δ² at δ ≤ ¼ (e^{1/2}+e^{1/4} = 2.9327 < 3);
Re tr(1−Z^{-1}) = ½‖1−Z‖²_HS exactly for unitary Z; |Re tr((1−Z^{-1})R)| ≤ x√N‖R‖_op; ½x² − 3√Nδ²x ≥ ¼x² ⟺ x ≥ 12√Nδ²;
W′ ∈ SU(N) needs X̄ traceless (H3: N·(π/3)A_dη < 2π ⟺ ε_1 < 78/N at η < c_1ε_1); normaliser via D4-norm (2) needs only
‖M̄‖ ≤ 1. Dichotomy: ‖1−W′_P‖ ≤ L²η + 4(e^δ−1), δ ≤ (π/3)A_dη (chord bound valid for ‖·‖ ≤ 1, i.e. A_dc_1ε_1 ≤ 1), and
4((e^{1/4}−1)/(1/4))(π/3) = 4.758892 ≤ 5.5; (L²+5.5A_d)c_1 = ½ by definition of c_1; t/8 ≥ 12√Nδ² ⟸
t ≤ 1/(8·12·(π/3)²√N A_d²c_1²), coefficient 105.2758 ≤ 106; exponent κ(t/8)²/(4Ng²) = κt²/(256Ng²). All of it holds.
H7 (independence) is not needed — a union bound over the four links suffices (EXISTENCE's own KN-step proof says "and a
union bound"); REVIEW_ARS_EPS_S1 RA-8: agree. The identity (L²+5.5A_d)c_1 = ½ is definitional and cannot serve as
evidence (RA-4: agree; `ar1_margins.py` l.243-245 is that tautology). Codex F7: **agree**.

### r55a-F10 — ARS_FIX §3.1-§3.2 "the quadratic η_1 is forced … centring at W′ instead of S … **That is the whole 82 decades**" — **REFUTED**: about 81 of the 82 decades need no re-centring

Codex F4's alternative, re-derived by me: keep the centre S, write M̄ = S(I+E) with ‖E‖_op = ‖M̄−S‖ ≤ A_dη ((R1) second
clause), Z := S^{-1}V, x := ‖I−Z‖_HS. Then exactly Re tr((S^{-1}−V^{-1})M̄) = Re tr((I−Z^{-1})(I+E)) = ½x² + Re tr((I−Z^{-1})E)
≥ ½x² − x√N A_dη. With S as the candidate in D4-norm (2) (Re tr V_0^{-1}M̄ ≥ Re tr S^{-1}M̄), k_c(V) ≤
e c_N^{-1}(κ/g²)^{N²−1}exp(−(κ/(Ng²))[½x² − √N A_dηx]) ≤ (same)·e^{−κx²/(4Ng²)} as soon as √N A_dη ≤ x/4, and on
{‖V_c−S_c‖_op ≥ ε_1/8} (x ≥ ε_1/8) that holds for η ≤ ε_1/(32√N A_d). With (R2) the dichotomy holds at
**η_F4 := min{ε_1/(2L²), ε_1/(32√N A_d)} = ε_1/(288√N)** (d=4, L=3), with the **same** kernel exponent κε_1²/(256N).
RLARGE's (R4) loses 2δ_c only because it bounds N^{-1}Re tr(V^{-1}(M̄−S)) by ‖M̄−S‖ separately instead of pairing it with
(I − Z^{-1}). r55a_2 G7: η_KN/η_F4 = 288√N/117 ∈ [3.481141] (N=2), [4.263510] (N=3); so of the 82.1406 decades
(N = 2, ε_1 = 6.7·10⁻⁴⁰) **81.0571 come from the sharpened estimate alone and 1.0834 from re-centring** (N = 3: 81.2332 and
1.2595). η_F4 also beats RS-lin's η_q by 8√N (11.31 at N = 2) with a 4× better kernel exponent. **Codex F4: agree**
(Codex proved it with the weaker η_q; the sharp threshold is mine). This does not touch KN′'s correctness; it removes the
claim that KN is *the* mechanism of the gain.

### r55a-F11 — The gains 82.141 (today) / 91.848 (proposed ε_1), and the N = 3 values 82.4927 / 92.2000 — arithmetic **CONFIRMED**; as a programme gain **REFUTED**

r55a_2 G1: 2log10(4608N/(117ε_1)) = [82.140564] (6.7·10⁻⁴⁰, N=2), [82.492746] (N=3), [91.847849] (9.38495112638·10⁻⁴⁵,
N=2), [92.200032] (N=3); the direct min-formula ratio equals the closed form exactly. ARS_FIX's "82.141 at today's ε_1,
not 92" correction and KN_ADOPT's N-labelling are right. But both are gains of a frozen formula over a frozen formula, at
κ = 1, with a_η at its bare value: no live quantity moves (F01). Codex F8: agree on the numbers and on the scope.

### r55a-F12 — HIST l.186's route comparison: **201.029× CONFIRMED in HIST's own currency; ARS_FIX's 1551× REFUTED as a route comparison**; REVIEW_ARS_EPS_S1's "+2.303 decades over the lane's own best proven route" — number **CONFIRMED**, status **REFUTED**

HIST l.185-186: "The binding exponent of the joint route is the plaquette branch a_η/81 ∝ η_q² (h4); most of h4's 80-fold
reduction of n_♯ comes from c_RS = 81 against 5⁴ = 625, and the rest from η_q² against η_1²." Independent check of the
currency: at h4's ε_1 = 0.5, N = 2, η_q/η_1 = 8.7·10⁻⁵/2.7·10⁻⁵ ≈ 3.2 (HIST l.180-181), and (625/81)·3.2² = 7.716·10.24 ≈ 79 —
the "80-fold". So HIST's comparison is the **product** of both factors, and under the adoption the RS/joint ratio of binding
exponents is (81/625)(η_KN/η_q)² = **21233664/105625 = 201.0288** (N=2), 452.3147 (N=3); log10 2.303258 / 2.655441
(r55a_2 G4, all reproduce). 1551.148 = (512/13)² is the η-factor alone. KN_ADOPT §3.2, REVIEW_ARS_EPS_S1 RA-16, PROOF
[S25-fix 1] and Codex F8 are right; ARS_FIX l.537 and §8.4 item 1 are wrong.
**But both sides of that comparison are non-live pricing formulas**: a_RS/625 (frozen §7.1 greedy, ARGUED, superseded) and
a_η(η_q)/81 (RS-joint, "CONDITIONAL ⇐ (PLD-q)_k", l.437, l.651, and on l.513's not-a-hypothesis list). So RA-17's "the lane's
own best proven route" is wrong as a status: the **lemma** RS-lin is proven (F26) but the **joint pricing route** is
conditional and unconsumed. Codex F3/F4 said the status was "not established by the text"; having read HIST, I can say it
is not true. The live comparator is a (F04): a = 1.040·10⁻⁸⁶ beats the joint per-cube 6.524987·10⁻⁸⁹ by 2.20263 decades
(r55a_2 G8; ARS_BIND's POST-HOC figure reproduces).

### r55a-F13 — RLARGE l.65 "For ε_1 ≤ 2, η_1 ≤ η_q unless δ_0/A_d binds": the banked item is **TRUE as written**; "l.65 is FALSE" (present tense) — **REFUTED**; the conditional reversal under the adoption — **CONFIRMED**, but "by 512/13 (768/13) at every ε_1" — **REFUTED as universal**

r55a_2 G5(b): at every tested ε_1 ∈ (0, 2], N = 2, 3, either η_RS ≤ η_q or the δ_0/9 entry of η_q is active; without the
"unless" clause a violation appears (η_RS/η_q = 1.25 at ε_1 = 1, 5.0 at ε_1 = 2; control FIRES) — so the clause is
load-bearing and the sentence is exactly right (**L65-TRUE-AS-WRITTEN**; REVIEW_RLARGE_V2 §2.3's "CORRECT" stands). At live
ε_1, η_RS/η_q = ε_1/2 = 3.35·10⁻⁴⁰. SESSION25_RESULTS.md l.41's "**RLARGE l.65's η_1 ≤ η_q is FALSE**" is therefore wrong
(also flagged by CODEX_REVIEW_DECADES, which I agree with on this point). What is true: **if** η_1 were redefined as
η_KN = ε_1/117, the sentence would have to be rewritten, because η_KN/η_q = max{256N/13, 640Nε_1/13} > 1 for every ε_1
(G5(a): REVERSAL-HOLDS), equal to 512/13 = 39.3846 (N=2) and 768/13 = 59.0769 (N=3) **only for ε_1 ≤ 0.4** (δ_0 = 1/(640N)
inactive) and larger above (40.37 at 0.41, 196.92 at 2; **REFUTED-AS-UNIVERSAL** for KN_ADOPT §3.1's "at every ε_1" and
"exactly ε_1-free"). On the δ_0 remark (ARS_FIX §5.1, KN_ADOPT §3.1): the substance — the computed ratio is a lower bound —
is right; Codex F8's "opposite direction" objection is to the literal wording "omitting … can only lower η_q", which is
indeed backwards as worded. Codex F8: agree on substance, and agree the reversal is a definition change, not a falsified
theorem ("Adoption invalidates continued use of that old statement; it does not falsify the old theorem").

### r55a-F14 — KN_ADOPT §8.1 "(it would take ε_1 > 814.587 for the other branch, N = 2)" — **REFUTED (stale minimum)**; the branch boundary is κ = 128/13689, independent of ε_1 and N — **CONFIRMED**; ARS_FIX §2.1's "active iff ε_1 < 814.587" — **REFUTED as an iff, even before the adoption**

After the adoption a_η = ε_1²/(27378N) and the kernel entry is κε_1²/(256N): both ∝ ε_1²/N, so the plaquette branch is
active iff κ ≥ 256/27378 = **128/13689 = 0.00935057** (r55a_2 G6(a): BOUNDARY-KAPPA-ONLY at every tested ε_1 from 10⁻⁴⁰ to
1000, N = 2, 3; at κ = 1 no change between 814 and 815 → **STALE**). 814.587 = √663552 is the crossover of the *quadratic*
formula. It was never real even before: the quadratic entry of η_RS is active only for ε_1 ≤ 4608N/18 = 512 (N=2), and
above that a_η = ε_1²/(648N) < ε_1²/(256N) at κ = 1, so the plaquette entry is active at **every** ε_1 > 0 (G6(b):
ALWAYS-PLAQUETTE; control at κ = 1/100 changes branch, FIRES). Pre-adoption the κ-boundary for "plaquette everywhere" is
κ ≥ 32/81. Immaterial at live ε_1; material for the patch text, which states the wrong reason. Below κ*, RA-14's
"gain = 84.170 + log10 κ" (ε_1 = 6.7·10⁻⁴⁰, N = 2) checks by hand (log10(165888N²κ/ε_1²)). κ is symbolic in RLARGE (l.1020);
PROOF uses example values 1 and 1/4 (SYMBOLS §6.5), both above κ*. Codex F2: **agree**; RA-14: agree.

### r55a-F15 — KN_ADOPT §8.1 side conditions: S1-S3 **CONFIRMED as sufficient**; "(S1) is exactly the statement" — **REFUTED (wording)**; "all four hold … by ~40 decades; verified in kn1_sides_out.txt" — **REFUTED as an evidence claim**

kn1_sides_out.txt contains (S1) and (S2) only — no S3 line and no S4 line, no R, no g_K (read in full). S3 (ε_1 < 78/N) is
trivially true at live ε_1 but not "verified" there; S4 (g_K² ≤ 1/(2R)) is a flow hypothesis with no numerical check
anywhere in the batch. 169/(106√N) = 1.127368 / 0.920492 and 351/(36π) = 3.103521 reproduce; the sharp S1 coefficient is
32π²/3 = 105.2758 < 106, so S1 is sufficient, not exact. Codex F6: **agree**.

### r55a-F16 — KN_ADOPT §4 "a consumer of a_RS that the banked sweep missed" (l.830's e^{a_RS R}, side condition S4, −15.918 / +66.222) — occurrence **CONFIRMED**, consumer status **REFUTED (superseded target)**; flow wording **REFUTED as worded** (Codex F6)

The occurrence is real and has the opposite sign, and sweeping a_RS rather than η_1 was the right method. But its target
(frozen l.1003-1007 and l.1023) is not on the live route (F05 K6), so the 0.30103-decade correction and S4 price nothing live.
Separately, Codex F6 is right that g_K² ≤ 1/(2R) does not give Rg_j² ≤ ½ at intermediate levels — its counterexample
(R = 10, u_1 = 20, u_0 = 21/2, β_±log L = ½: u_0 − u_1 = −19/2 is (F_R)'s lower endpoint, g_1² = 1/(2R), but u_0 − R < u_0/2)
checks by hand against RLARGE l.98-100 — and the correct sufficient form is the final-coupling one (u_i ≥ u_K − R ≥ u_K/2,
so g_K² ≤ a/(2B)), which gives the same 0.30103 decades. Moot either way.

### r55a-F17 — REVIEW_ARS_EPS_S1 §1 item 1: "Neither file cites §3.5, l.435, l.438 or l.835 anywhere (grep: zero hits in both)" — **REFUTED**; ARS_BIND's correction — **CONFIRMED**

grep: "§3.5" occurs in ARS_FIX at **l.294** and **l.788** (both inside its quotation of RLARGE l.832, l.294 including
"(a = min{θa_bad, a_A})"); "l.435", "l.438", "l.835", "not consumed" occur 0 times in ARS_FIX and EPS1_SWEEP; EPS1_SWEEP has
0 "§3.5". The review's own §5.1 concedes the pointer ("which ARS_FIX cites only through that pointer and never reads"), so
§1 contradicts §5.1. The substantive point (ARS_FIX never read §3.5's body) stands. ARS_BIND's "TRUNCATED" finding on the
"No counted item depends on a_♯ or n_♯" quote is also right for §1 and the RA-15 table row (l.438-439 continue "stands for the
frozen lemmas (R1/R1^J hold for every cutoff n_c ≥ n_*, n^J_*)"); §5.1 of the review quotes it in full.

### r55a-F18 — REVIEW_ARS_EPS_S1 §5.1 "The one place η_1²/(2N) becomes a cost, (TS-c) at l.1183-1186" — **REFUTED**; ARS_BIND's counter-example — **CONFIRMED**

HIST l.1377-1379 (Corollary CLS-cone (b)): "E_𝒞(p) ≥ η_1²/(2N·C_cone) … at i = 0, E_𝒞(p) ≥ s(U_0(p)) ≥ η_1²/(2N) directly".
CLS-cone is on l.517's off-route list, so it is not a live consumer either.

### r55a-F19 — PROOF.md [S24-flag 6] (string "[S24-flag 6] a_RS BINDS TODAY") and its [S25-fix 4] reversal

- **[S24-flag 6]'s two headline claims** ("a_RS BINDS TODAY", "RLARGE l.618 is FALSE") — **REFUTED** (F01-F03). Its numbers
  (−15.62/−18.41, 82.141, 105.276, 4.75889) — **CONFIRMED** as arithmetic. "(L² + 5.5A_d)c_1 = ½ exactly, which is what makes
  its dichotomy exhaustive" — the identity is definitional (F09). "H1 is not [available]" — superseded (F06). Its "second
  defect in RLARGE §5.4 (l.612 reports 184 levels from n_H while l.1024 says the induction uses n_♯)" — **REFUTED**: l.1024 is
  frozen v1 text whose n_♯ := ⌊4/(a_♯β_-)⌋ is superseded by l.832, and v3's cutoff is n_♯ ≥ max{n^J_*, n_H} (l.828), so l.612's
  n_H-based count is the consistent one (ARS_FIX §4.2 had flagged this row as conditional on the same reading). "l.65 …
  reverses" — conditional only (F13). The retained closing sentence "**Either way l.618 needs editing**" rests on the refuted
  premise; a scope clarification of l.615-618 is still advisable, but for the (RLF-δ)/a_ret reason of F03, not for a_RS.
- **[S25-fix 4]** ("a_RS binds NOTHING on the live RLF-step v3 route, and RLARGE l.618 is TRUE as written") — **CONFIRMED with
  corrections**: (i) "TRUE as written" holds for HIST-sum and REL-seq, NOT-VERIFIED for (RLF-δ) (F03); (ii) "+63.619 decades"
  is at DX′ = 2.5·10⁻¹⁵² and the supremum θ → 1/24, given U1's a_A ≥ θa_bad — +63.627 at DX′ = 2.456·10⁻¹⁵² (F04); (iii) "all
  inside Appendix A (frozen v1 …)" — l.830 is in the live v3 reading-note block at the head of Appendix A (ARS_BIND §4 says
  so itself); (iv) "zero times in HIST, HW, PLD, SQ …" is true of the literal symbol; the a_♯ channel exists and is
  harmless (F01).
- **Unflagged residue in PROOF.md:** the S24 consolidation paragraph (now **l.6945-6951**, string "a_RS is found to bind
  TODAY") still says "**RLARGE l.618 [is] REFUTED or struck**" and "**a_RS is found to bind TODAY**, with a repair worth 82 decades
  blocked only by a prior either/or", with **no [S25-fix 4] pointer** (the (GAP-Z) clause in the same paragraph did get its
  [S25-fix 2] pointer). ARS_BIND asked for it (under its old line number l.6921). **This is a PROOF.md edit the lead owes.**

### r55a-F20 — ARS_FIX §1 "η_1 is THREE symbols" — **CONFIRMED (spot)**; §1.1 "E9 was an either/or and RLARGE took the other horn at l.830" — **CONFIRMED**, with a provenance nuance

η_1 counts: HW, NORMS, BFT_A, BFT_B, FLOW, LINEAR_PACKAGE 0; PLD 16; SF 2; SQ 5 with SQ l.1679 "η_1 := η_U/2" (a local
bound variable). PLD writes "RLARGE's η_1 = c_1ε_1" at l.1077, 1096, 1204, 1259 (and l.1010, 1071 at c_1ε_1) while RLARGE's η_1
is the quadratic min — a real collision. REVIEW_PLD_S3 l.462: "**Either** adopt KN-step's re-centred dichotomy … **or** replace
every 'η_1 = c_1ε_1' in PLD §15 by (R3)'s η_1." RLARGE l.830: "η_1 is v2/v3's η_1 (E9)". Nuance: l.64 carries the tag
[v2-E9], so the choice was made in **v2** and re-affirmed in v3 (KN_ADOPT §1.7 item 3 noticed this). The choice only
resolves the collision once PLD's text is fixed; it has not been.

### r55a-F21 — ARS_FIX (V1): a_RS ∝ ε_1⁴ under the current η_1, "EXP-4 at every live ε_1" — **CONFIRMED**
At live ε_1 the quadratic entry of η_RS is active (ε_1 ≤ 512) and a_η ∝ ε_1⁴ ≪ κε_1²/(256N); r55a_2 G1's direct ratios
confirm. (The "iff ε_1 < 814.587" part: F14.)

### r55a-F22 — ARS_FIX §2.2 "Correction 1": the honest margin is −15.62 to −18.41 because of c_RS = 625 — arithmetic **CONFIRMED**, relevance **none**
−18.412954 (G2). The c_RS = 625 of l.1021 is itself "ARGUED, not written" and superseded (l.832). Also note c_RS is two
objects (625 at l.1021; 81 at l.435/HIST l.186) — ARS_BIND §8: agree.

### r55a-F23 — REVIEW_ARS_EPS_S1 RA-11 "(C2) is not the binding condition" — **CONFIRMED and strengthened**
EPS1_SWEEP l.481-484 (read in situ): "(C2) Adopt KN-step's linear η_1 first, or scope RLARGE l.618 … **This is the binding
condition; everything else is bookkeeping.**" With F01, (C2)'s object has no live consumer, so it is not merely non-binding
but about nothing (ARS_BIND §9(a)). RA-11's reasons (i) and (iii) I checked against l.481-496 and agree; (ii) and (iv) concern
EPS1_SWEEP's other conditions, which are outside my batch — spot-checked only.

### r55a-F24 — REVIEW_ARS_EPS_S1 RA-12 "(C7) is written with the wrong operator" — **CONFIRMED**
EPS1_SWEEP l.441-444/l.494: "CONDITIONAL on c_+·C_Ω ≲ 1.5·10⁴⁶". Since DX′ ∝ 1/C_Ω (REVIEW_SF_S7 l.203) and g²_CRC =
1.85835·10⁻⁹⁶/c_+ (EPS1_SWEEP l.448), the g²_CRC-over-DX′ margin is log10(1.85835·10⁻⁹⁶C_Ω/(2.456·10⁻¹⁵²c_+)): exhausted when
**c_+/C_Ω** reaches 7.57·10⁵⁵ (today; the file's 7.87·10⁵⁵ uses its own rounding), and the a/10²-over-DX′ margin is exhausted
when **1/C_Ω** reaches 10^{63.6}. The product form is wrong; a large C_Ω protects these margins.

### r55a-F25 — REVIEW_ARS_EPS_S1 RA-10 (five unfalsifiable gates) — **CONFIRMED for the three I opened**; RA-13 (C_Ω* = 4.14·10¹⁵) — arithmetic **CONFIRMED**, relevance none
`ar1_margins.py` l.243-245 tests (L²+5.5A_d)c_1 == ½ with c_1 built from the same 5.5 (cannot fail); l.269-271 prints the
literal "SAME-CONSTANT" (no comparison); `ar1c_knrebuild_posthoc.py` l.76-78 hard-codes "(REPRODUCES)". G9: C_Ω* =
4.14070·10¹⁵ (DX′ = 2.456·10⁻¹⁵²) and 4.21488·10¹⁵ (2.5·10⁻¹⁵²) — both batch figures reproduce; the threshold reverses a
"breach" that prices nothing live.

### r55a-F26 — Lemma RS-lin (HIST l.168-179, with PM l.136-149 and KQ l.155-166) is PROVEN and live — **CONFIRMED** (ARS_BIND (M7)(i)-(ii)); Codex F4's "NOT-VERIFIED for HIST's full RS-lin" is settled in the positive
I re-derived PM step (3) (Y = P(R), ‖P(Z)‖ ≤ 2‖Z‖, ‖R‖ ≤ ½e^{1/8}‖Y‖² + δ, hence ‖Y‖ ≤ 2.34δ under δ ≤ δ_0 = min{1/(640N), 2/N³},
with the trace-zero argument needing δ < 4/N³), KQ (lower) (φ = s(U) + N^{-1}Re tr((1−U)(A−1)) ≥ x²/(2N) − x‖M−W_0‖), and
RS-lin (b): x ≥ ε_1/8 − 3ε_1/(256N) ≥ ε_1/16 and ‖M̄−W_0‖ ≤ ε_1/(64N) ≤ x/(4N) give φ ≥ x²/(4N) ≥ ε_1²/(1024N). Live: CL^J
uses RS-lin (a)-(c) (HIST l.233-242) and CL^J (a)-(b) is step 1 of RLF-step v3 (RLARGE l.521-522); η_q feeds (TC), the
non-quiet definition and a_cb (l.82-83, l.297, l.443). The *joint pricing route* built on it is CONDITIONAL and off-route (F12).

### r55a-F27 — "a_RS's STATUS is unchanged — CONDITIONAL on (PLD)_k (i)" (ARS_FIX §3.4, KN_ADOPT §5, PROOF [S25-fix 1] tail) — arithmetic **CONFIRMED (spot)**, framing **moot**
KN_ADOPT's ×26.0 (= 2·117/9) and ×2.002 (= 2·1.001) shortfalls check. But (PLD)_k (i) is on RLARGE l.513's not-a-hypothesis
list, so on the live route a_RS is not "conditional on" anything — it is not defined there (F05 K8; ARS_BIND §8 says the same).

### r55a-F28 — Spot-checks only (no verdict beyond "spot-checked, consistent")
ARS_FIX m_τ: 66 (C_I = 1, quadratic, 6.7·10⁻⁴⁰) and 3 (linear) re-derived by hand; PLD LD-arith least N = 37 at t = 2 re-derived
(N²/(N−1) > 37.105); PLD's a(η) = 49η²/(256σ_*²) is ×49.6 below η²/(2N) at σ_*² = 38; RS-compatibility ×12.99 = 117/9.009;
REVIEW_ARS_EPS_S1 RA-3 (two of the four "live" ε_1 come from the l.611 row) — a defensible reading, not decision-changing;
RA-18's 71391.9 — not re-derived. KN_ADOPT §1.7 item 2 (EXISTENCE l.1756-1757 already states "(probability weights)") —
CONFIRMED by reading.

### r55a-F29 — KN_ADOPT §6/§8.1 "**The adoption LANDS**" / "literal and append-ready" — **REFUTED**: do not land the patch into RLARGE as written

Reasons, each established above: (1) η_1 and a_RS have **no live consumer** (F01), so the replacement changes nothing the
live route asserts; (2) RLARGE v3 **already keeps** "Lemma KN with KN-step" as a statement "for the representation route and
for collar links" (l.420-422), so nothing needs importing; (3) the target is **frozen verbatim** Appendix A (l.824 "verbatim
from RLARGE_v1_snapshot.md"; l.826 "the text below is not edited; read it with these notes") — v3's mechanism for such a
change is a reading note, and "§6" is ambiguous (live §6 is the status list at l.623; Codex F10 noted this too); (4) the
patch text carries errors: the stale 814.587 crossover (F14), "all four side conditions verified" (F15), "(S1) exactly" (F15),
the bare value of a_η presented as *the* a_η (RLARGE l.1020-1021 make the effective a_η an output of (PLD)_k (i), itself
off-route; Codex F7), and a consequential edit (item 4, "l.618 must be edited regardless") built on the refuted a_RS premise;
(5) its headline value (82 decades) is a frozen-formula gain, ≈81 decades of which need no re-centring (F10).
What *would* be worth recording (owner's call, not mine): a one-line v3 reading note at l.830 that η_1 = η_RS has no live
consumer and that a linear threshold is available (KN-step′ at c_1ε_1, or the sharpened (R4) at ε_1/(32√N A_d)); a rename
(η_RS / η_KN, c_KN) to end the PLD collision (F20); and the l.615 scope fix for (RLF-δ) (F03). Codex F10's "NO": **agree**.

### r55a-F30 — Other KN_ADOPT claims
- §2.1 "the gain is convention-free" (the /10², c_RS and DX′ cancel in the difference; the gain is N-dependent) — **CONFIRMED** (G1).
- §1.5 item 3 / §8.4 item 2 (polar(M̄_c) vs ‖W′^{-1}M̄ − 1‖ ≤ 3δ²) — flagged by KN_ADOPT as not reconciled; **NOT-VERIFIED** (I did
  not attempt it; it is outside the a_RS question).
- §9 errata (the ×13.0 → ×6.5 / ×12.99 correction; l.702 vs l.703) — consistent with my arithmetic (117/18 = 6.5; 117/9.009 = 12.99).

### Errata to this file (append-only; nothing above is edited)
- **r55a-F24**: the clause "(today; the file's 7.87·10⁵⁵ uses its own rounding)" is an **unverified guess** and is withdrawn. What
  I verified: with g²_CRC = 1.85835·10⁻⁹⁶/c_+ and DX′ = 2.456·10⁻¹⁵²/C_Ω the exhaustion value is c_+/C_Ω = 7.57·10⁵⁵
  (10^55.879, matching REVIEW_ARS_EPS_S1's +55.879); EPS1_SWEEP's 7.87·10⁵⁵ (10^55.896) differs by 0.017 decades for a reason I
  did not trace. The operator correction (quotient, not product) does not depend on it.

---

## 2. Summary table — every claim in the batch, with its verdict

| # | claim | where (file, locating string) | verdict | finding |
|---|---|---|---|---|
| 1 | a_RS binds nothing on the live v3 route (V-NO) | ARS_BIND §9 "(V-NO)" | **CONFIRMED** | F01 |
| 2 | a_RS: 5 RLARGE hits, all ≥ l.824; 0 in HIST/HW/PLD/SQ/BFT/NORMS/LP | ARS_BIND §2.1-2.2 | **CONFIRMED** (literal symbol; a_♯ channel traced, harmless) | F01 |
| 3 | a_RS's ceiling binds today (−15.617 / −18.413) | ARS_FIX §2.2 "BINDS TODAY" | **REFUTED** (arithmetic right, nothing consumes it) | F02 |
| 4 | RLARGE l.618 is FALSE | ARS_FIX §2.2, §8.1 item 1; PROOF [S24-flag 6] | **REFUTED** | F02, F19 |
| 5 | l.618 TRUE as written — for HIST-sum, REL-seq | ARS_BIND §9(b); PROOF [S25-fix 4] | **CONFIRMED** (given U1's a_A ≥ θa_bad) | F03, F04 |
| 6 | l.618 TRUE as written — for (RLF-δ) | same | **NOT-VERIFIED** (exponent a_ret, value unstated, U1/K12) | F03 |
| 7 | (K7b) all three l.615 items carry exponent a | ARS_BIND §5 (K7) | **REFUTED** ((RLF-δ) carries a_ret, RLARGE l.192-201) | F03, F05 |
| 8 | live a = θa_bad = 1.040e-86 clears DX′ by +63.619 | ARS_BIND A7; PROOF [S25-fix 4] | **CONFIRMED** at DX′ = 2.5e-152, θ → 1/24, U1; +63.627 at 2.456e-152 | F04 |
| 9 | "the review carried −15.617 where the exact figure is −15.6248" | ARS_BIND §6 | **REFUTED** (different DX′ input, exactly log10(2.5/2.456)) | F04 |
| 10 | routes K1-K6, K8 fail to build a consumer | ARS_BIND §5 | **CONFIRMED** | F05 |
| 11 | K7(a): Lemma RS's clauses contain no a_RS | ARS_BIND §5 | **CONFIRMED** | F05 |
| 12 | H1: S4′ weights uniform (d!L^d)^{-1} = 1/1944 | KN_ADOPT §1.2; PROOF "Decision 4" (l.1806) | **CONFIRMED** | F06 |
| 13 | (R1)'s second clause already consumes the convexity | KN_ADOPT §1.4 | **CONFIRMED** | F06 |
| 14 | "‖M̄‖ ≤ 1 iff probability vector"; "(R1) would be false"; "three statements break" | KN_ADOPT §1.4, §8.4 item 1 | **REFUTED** (Codex F5 counterexample checked) | F06 |
| 15 | H1-F2 ruled out; W′_c = U′(c) on D′ | KN_ADOPT §1.3, §1.5 | **CONFIRMED** (PROOF read) | F07 |
| 16 | 633 (y, axial-path) labels, histogram {1:384,4:192,12:48,24:9} | KN_ADOPT §1.6; Codex F1 | **CONFIRMED** | F08 |
| 17 | 633 distinct transporters, weights {1/1944,1/486,1/162,1/81} | KN_ADOPT §1.6, §6, §7 | **REFUTED** → **475**, weights {1/1944,1/486,1/324,1/162,5/486,2/81,1/27} | F08 |
| 18 | Lemma KN′ + Corollary KN-step′ PROVEN (rebuild) | ARS_FIX §3.2; KN_ADOPT (R3′)/(R4′) | **CONFIRMED** | F09 |
| 19 | 105.276 / 4.75889 / H5 1.12737, 0.920492 / S2 3.103521 | ARS_FIX §3.2-3.3; KN_ADOPT §8.1 | **CONFIRMED** | F09, F15 |
| 20 | (L²+5.5A_d)c_1 = ½ "verified" as evidence | ARS_FIX §6.2, §8.3; PROOF [S24-flag 6] | **REFUTED as evidence** (definitional) | F09 |
| 21 | quadratic η_1 is forced; re-centring is "the whole 82 decades" | ARS_FIX §3.1-3.2 | **REFUTED** (81.06 of 82.14 dec. need no re-centring; re-centring 1.08 at N=2) | F10 |
| 22 | gains 82.1406 / 91.8478 (N=2), 82.4927 / 92.2000 (N=3) | ARS_FIX §4.1; KN_ADOPT §2.2 | **CONFIRMED** (arithmetic) | F11 |
| 23 | the adoption is worth ~82 decades to the programme | ARS_FIX §7.7, §8.1; PROOF [S24-flag 6]; S24 consolidation | **REFUTED** (no live consumer) | F11 |
| 24 | route reversal 1551× | ARS_FIX §5.1, §8.4 item 1 | **REFUTED** → 201.029× (N=2), 452.315× (N=3) | F12 |
| 25 | route reversal 201.029× / 452.315× | KN_ADOPT §3.2; REVIEW RA-16; PROOF [S25-fix 1] | **CONFIRMED** (both sides non-live) | F12 |
| 26 | "+2.303 decades over the lane's own best proven route" | REVIEW_ARS_EPS_S1 RA-17 | **REFUTED as status** (number right; joint route CONDITIONAL ⇐ (PLD-q)_k, off-route) | F12 |
| 27 | "RLARGE l.65's η_1 ≤ η_q is FALSE" (present tense) | SESSION25_RESULTS l.41, relaying KN_ADOPT §3.1 | **REFUTED** (true as written; G5(b)) | F13 |
| 28 | under the adoption η_KN > η_q at every ε_1 | ARS_FIX §5.1; KN_ADOPT §3.1 | **CONFIRMED** | F13 |
| 29 | … by exactly 512/13 (768/13), "ε_1-free", "at every ε_1" | KN_ADOPT §3.1, §8.1 item 3 | **REFUTED as universal** (exact only for ε_1 ≤ 0.4; max{256N/13, 640Nε_1/13}) | F13 |
| 30 | "it would take ε_1 > 814.587 for the other branch" | KN_ADOPT §8.1 patch | **REFUTED** (stale; boundary κ = 128/13689) | F14 |
| 31 | a_η active "iff ε_1 < 814.587" | ARS_FIX §2.1 | **REFUTED as iff** (immaterial at live ε_1) | F14 |
| 32 | branch boundary κ = 128/13689, independent of ε_1, N; gain 84.170 + log10κ below it | Codex F2; REVIEW RA-14 | **CONFIRMED** | F14 |
| 33 | S1-S3 sufficient side conditions | KN_ADOPT §8.1 | **CONFIRMED** | F15 |
| 34 | "all four … verified in kn1_sides_out.txt"; "(S1) is exactly" | KN_ADOPT §8.1 | **REFUTED** | F15 |
| 35 | l.830's e^{a_RS R} is a consumer of a_RS (S4; −15.918 / +66.222) | KN_ADOPT §4, §8.1 item 5 | **REFUTED as a consumer** (superseded target) | F16 |
| 36 | "Neither file cites §3.5 … zero hits" | REVIEW_ARS_EPS_S1 §1 item 1 | **REFUTED** (ARS_FIX l.294, l.788) | F17 |
| 37 | the §3.5 "No counted item" quote is truncated in the review | ARS_BIND §3 | **CONFIRMED** (§1 and RA-15 row) | F17 |
| 38 | "the one place η_1²/(2N) becomes a cost, (TS-c)" | REVIEW_ARS_EPS_S1 §5.1 | **REFUTED** (HIST l.1379) | F18 |
| 39 | "second defect in RLARGE §5.4" (n_♯ level count 355.6 vs 184) | ARS_FIX §4.2, §8.1 item 8; PROOF [S24-flag 6] | **REFUTED** (l.1024 superseded; v3 n_♯ ≥ n_H) | F19 |
| 40 | [S25-fix 4] as written | PROOF.md "[S25-fix 4] REFUTED IN FULL" | **CONFIRMED with corrections** ((RLF-δ); DX′; θ; U1; l.830 is live) | F19 |
| 41 | η_1 is three symbols; PLD/RLARGE collision | ARS_FIX §1 | **CONFIRMED** | F20 |
| 42 | E9 was either/or; RLARGE took the other horn (l.830) | ARS_FIX §1.1 | **CONFIRMED** (decided in v2, tag [v2-E9]) | F20 |
| 43 | a_RS ∝ ε_1⁴ (EXP-4) at live ε_1 | ARS_FIX §2.1 | **CONFIRMED** | F21 |
| 44 | c_RS = 625 makes the margin −15.62 to −18.41 | ARS_FIX §2.2 Correction 1 | **CONFIRMED** (arithmetic; irrelevant) | F22 |
| 45 | (C2) is not the binding condition | REVIEW RA-11 | **CONFIRMED** (and vacuous) | F23 |
| 46 | (C7)'s operator is c_+/C_Ω (and 1/C_Ω), not c_+·C_Ω | REVIEW RA-12 | **CONFIRMED** | F24 |
| 47 | unfalsifiable gates in ar1 / ar1c | REVIEW RA-10 | **CONFIRMED** (3 of 5 opened) | F25 |
| 48 | C_Ω* = 4.14e15 reverses the a_RS "breach" | REVIEW RA-13 | **CONFIRMED** (arithmetic; moot) | F25 |
| 49 | Lemma RS-lin PROVEN and live | ARS_BIND §7 (M7) | **CONFIRMED** (re-derived) | F26 |
| 50 | live a is 2.203 dec. better than the joint per-cube 6.525e-89 | ARS_BIND §7; PROOF [S25-fix 4] | **CONFIRMED** (arithmetic; comparator non-live) | F12 |
| 51 | a_RS CONDITIONAL on (PLD)_k (i) before and after; ×26.0 shortfall | ARS_FIX §3.4; KN_ADOPT §5 | **CONFIRMED** (arithmetic; framing moot — input off-route) | F27 |
| 52 | REVIEW's reproductions RA-1, 2, 4, 5, 6, 7, 8, 9 | REVIEW_ARS_EPS_S1 §2-§3 | **CONFIRMED** | F09, F11, F12 |
| 53 | "The adoption LANDS"; patch "literal and append-ready" | KN_ADOPT §6, §8.1 | **REFUTED** — do not land as written | F29 |
| 54 | the gain is convention-free and N-dependent | KN_ADOPT §2.1 | **CONFIRMED** | F30 |
| 55 | polar(M̄_c) vs 3δ² reconciliation | KN_ADOPT §1.5 item 3, §8.4 item 2 | **NOT-VERIFIED** (not attempted; outside the question) | F30 |
| 56 | EXISTENCE l.1756 already states "(probability weights)" | KN_ADOPT §1.7 item 2 | **CONFIRMED** | F28 |
| — | m_τ, LD-arith N = 37, a(η) ×49.6, ×12.99, RA-3, RA-18 | ARS_FIX §4-§5; REVIEW §2.3, §5.4 | **spot-checked only** (consistent where checked; not counted) | F28 |

**Counts (rows 1-56): CONFIRMED 33 · NOT-VERIFIED 2 · REFUTED 21.**

---

## 3. To the lead

**Counts:** CONFIRMED 33 · NOT-VERIFIED 2 · REFUTED 21 (56 claims; plus six spot-checks not counted). CODEX_REVIEW_KN.md
re-checked at 22:39Z: unchanged since 22:09:30Z, complete.

**Every REFUTED item, with its correction**
1. "a_RS binds today" (ARS_FIX) → the arithmetic −15.617 is right; nothing on the live route consumes a_RS.
2. "RLARGE l.618 is FALSE" (ARS_FIX, [S24-flag 6]) → true for HIST-sum and REL-seq at a; unevaluable for (RLF-δ) (a_ret).
3. ARS_BIND (K7b) "all three l.615 items carry a" → (RLF-δ) carries a_ret (RLARGE l.192-201); l.615 itself is mislabelled.
4. ARS_BIND "the review carried −15.617, exact is −15.6248" → both exact; they used DX′ = 2.456·10⁻¹⁵² vs 2.5·10⁻¹⁵².
5. KN_ADOPT "‖M̄‖ ≤ 1 iff probability weights" / "(R1) would be false" / "three statements break" → sufficiency only.
6. KN_ADOPT "633 distinct transporters" → 475; weights {1/1944, 1/486, 1/324, 1/162, 5/486, 2/81, 1/27}.
7. (L²+5.5A_d)c_1 = ½ as evidence → definitional; the evidential constants are 105.2758 and 4.758892.
8. ARS_FIX "re-centring is the whole 82 decades" → 81.06 of 82.14 decades (N=2) come from a sharpened (R4) without
   re-centring (η_F4 = ε_1/(32√N A_d)); re-centring adds 1.083 (N=2) / 1.260 (N=3).
9. "the adoption is worth ~82 decades" → 82.14 is a frozen-formula gain at κ = 1; zero live effect.
10. ARS_FIX "1551×" → 201.029× (N=2), 452.315× (N=3), in HIST's own currency.
11. RA-17 "+2.303 over the lane's own best proven route" → number right; the joint route is CONDITIONAL ⇐ (PLD-q)_k and off-route.
12. "RLARGE l.65 is FALSE" (SESSION25_RESULTS l.41) → TRUE as written; only a redefinition of η_1 would make it inapplicable.
13. "by exactly 512/13 at every ε_1" → η_KN/η_q = max{256N/13, 640Nε_1/13}; exact for ε_1 ≤ 0.4.
14. Patch "ε_1 > 814.587 for the other branch" → the branch is decided by κ ≥ 128/13689 alone.
15. ARS_FIX "a_η active iff ε_1 < 814.587" → active at every ε_1 > 0 when κ ≥ 32/81 (the crossover lies outside the
    quadratic entry's own domain ε_1 ≤ 256N).
16. "All four side conditions verified in kn1_sides_out.txt"; "(S1) exactly" → only S1, S2 are there; S1 is sufficient, not exact.
17. KN_ADOPT §4 "a consumer of a_RS the sweep missed" → real occurrence, superseded target (l.1023).
18. REVIEW "zero grep hits for §3.5" → ARS_FIX l.294, l.788.
19. REVIEW "the one place η_1²/(2N) becomes a cost" → also HIST l.1379 (CLS-cone, off-route).
20. "Second defect in RLARGE §5.4" → l.1024's n_♯ is superseded (l.832); v3's cutoff is n_♯ ≥ max{n^J_*, n_H}.
21. "The adoption LANDS / append-ready" → do not land as written (F29).

**Findings that change what PROOF.md / HANDOFF should say**
- **No tally change.** Lemma KN / KN-step are already counted in the existence lane (RLARGE l.633) and kept in RLARGE (l.420-422);
  nothing in this batch adds or removes a counted item.
- **PROOF.md S24 consolidation (now l.6945-6951, string "a_RS is found to bind TODAY")** still asserts "RLARGE l.618 … REFUTED or
  struck" and "a_RS is found to bind TODAY, with a repair worth 82 decades" with no [S25-fix 4] pointer. It needs one.
- **[S25-fix 4]** needs four qualifications: l.618's truth for (RLF-δ) is open (a_ret, U1); "+63.619" is at DX′ = 2.5·10⁻¹⁵² and
  θ → 1/24 given U1 (+63.627 at 2.456·10⁻¹⁵²); l.830 is live reading-note text; the a_♯ channel exists and is harmless.
  The retained S24 sentence "Either way l.618 needs editing" rests on the refuted premise. The "second defect in RLARGE §5.4"
  should be struck. [S25-fix 1] should cite KN_ADOPT §3.2, not §5.
- **SESSION25_RESULTS** l.13 ("The keystone lands") and l.41 ("RLARGE l.65's η_1 ≤ η_q is FALSE") are wrong as written.
- **RLARGE (owner's item, new):** l.615 says (RLF-δ)'s smallness condition has the form e^{-a/g²}; §1.2 (l.192-201) says its
  exponent is a_ret, value unstated (U1/K12). That is the one live smallness condition whose ceiling nobody can evaluate today,
  and the only door through which an a_RS-type quartic could come back (if node A built a_ret on Lemma RS's dichotomy).
- **HANDOFF:** no critical-path change. Its "There is no constants crisis" is consistent with this review. Any next-step that
  says "land KN_ADOPT §8.1" should be withdrawn. QFIX.md's objective function is a_RS's margin (QFIX l.123, l.258-264,
  l.374); with a_RS unconsumed that objective prices nothing live — for QFIX's reviewer.

**Codex verdicts used (CODEX_REVIEW_KN.md), agree / disagree**
F1 (633 labels / 475 reduced paths): **agree** — reproduced, and E7 shows 475 distinct holonomy values on generic fields.
F2 (814.587 stale; κ = 128/13689): **agree**. F3 (live ceiling uses a, not a_RS; "best proven route" not established):
**agree**, and I go further on both halves — the joint route is CONDITIONAL and off-route, and (RLF-δ) uses a_ret, which Codex
also did not notice. F4 (linear threshold without re-centring): **agree**; I re-derived it with the sharp threshold
ε_1/(32√N A_d) and price re-centring's share at 1.08 decades; its NOT-VERIFIED on HIST's RS-lin I settle as CONFIRMED (read
and re-derived). F5 (local chain CONFIRMED; source identity NOT-VERIFIED; "iff" REFUTED): **agree on the refutation**, and the
source identity is **CONFIRMED** here (PROOF.md decision 4 and S4′ read by string). F6 (S1-S3 sufficient; S4 unverified;
factor-two wording): **agree** (counterexample checked by hand). F7 (KN′ correct; bare vs effective a_η): **agree**.
F8 (ratios exact only on the inactive-cap branch; 201.029; gains): **agree**. F9 (gate audit): **agree**. F10 (do not append
as written): **agree**. Also CODEX_REVIEW_DECADES's "SESSION25_RESULTS l.41's present-tense 'RLARGE l.65 is FALSE' is REFUTED
as written": **agree** (I read only that passage of that file).

---

## 4. What the lane should now believe about a_RS, η_1 and the KN-step adoption

**a_RS** (RLARGE l.1020) is a frozen v1 quantity with no consumer on the live RLF-step v3 route. Its only input at effective
levels, (PLD)_k (i), is on RLARGE's own "Not hypotheses of RLF-step v3" list. Every figure computed against it — the
"−15.62-decade breach", the "82-decade repair", the "2.3-decade net gain over RS-lin", the l.830 "0.301-decade" factor — is
correct arithmetic about a quantity nothing reads. The live unreturned-defect exponent is a = min{θa_bad, a_A}. It clears
DX′ by about 63.6 decades (+63.627 at DX′ = 2.456·10⁻¹⁵², +63.619 at the rounded 2.5·10⁻¹⁵², θ → 1/24), given U1's
a_A ≥ θa_bad. So RLARGE l.618 is true for HIST-sum and REL-seq. It is not yet evaluable for (RLF-δ), whose exponent is the
unstated a_ret, and that, not a_RS, is what l.615-618 should be scoped around. **η_1** is three symbols. RLARGE's own
η_1 = η_RS (the quadratic min of l.64) has no consumer in RLARGE's live body. The live threshold of this type is RS-lin's η_q
(collar (TC), the non-quiet definition, a_cb, CL^J), which is linear and proven. RLARGE l.65 ("η_1 ≤ η_q unless δ_0/A_d
binds") is true as written. It would only need rewriting if η_1 were redefined. **KN′ and KN-step′** are correct
mathematics. H1 holds by PROOF.md's definition of the decision-4 kernel (uniform weights 1/1944), and RLARGE's (R1) already
relies on it. But the adoption buys nothing on the live route. RLARGE v3 already keeps "Lemma KN with KN-step" as a
statement. Most of its advertised gain (≈81 of 82 decades) is available from a three-line sharpening of RLARGE's own (R4)
without re-centring. The patch text carries a stale crossover, an unsupported "all four verified" claim, a wrong transporter
count and an edit request built on the refuted a_RS premise. **The KN-step patch should not be landed into RLARGE as
written, and on present evidence it need not be landed at all.** At most, RLARGE's owner could add a one-line v3 reading note
at l.830: η_RS has no live consumer, and a linear threshold is available if anything ever needs one. The owner could also
rename η_RS/η_KN (and c_KN) to end the PLD collision, and scope l.615 for (RLF-δ)/a_ret. The next real work on this front
is U1: fixing a_ret and a_A. Nothing in this batch moves the main-path tally.
