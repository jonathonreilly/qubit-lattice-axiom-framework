# REVIEW_SQ_S4: hostile review of lane G session 4 (SQ.md §T4, §15, §16; the [RSQ3-fix] edits; checks q4b, q5)

Reviewer: an independent agent. I wrote none of SQ.md, SQ_LOG.md, RLARGE.md, HW.md or any check. I edited no file except
this one. No git command was run; no commit, PR or push.

Inputs (read-only):
- SQ.md l.1295-1759 (§T4, §15, §16) in full; l.136-350 (§0.3: decay class, MSG-dec, E2, BCH-p, SUP-price, FORCE,
  (REG-min), DESC, PRICE-iii, DESC-ε), l.394-433 (§2: Q_2, Q_str, the 1D Schur tests), l.953-1294 (§T3, §13, §14) in full,
  with every [RSQ3-fix] block.
- SQ_LOG.md l.138-177 (session 4).
- checks/q4_criteria.md, q4_out.txt; checks/q4b_criteria.md, q4b_newton.py, q4b_out.txt, q4b_time.txt;
  checks/q5_criteria.md, q5_lattice_ids.py (T1/T2 in full, l.140-222), q5_out.txt, q5_time.txt.
- REVIEW_SQ_S3.md (all; the binding fix list and the house format), REVIEW_SQ_S2.md l.290-370, l.410-450.
- RLARGE.md l.87-96 (the defect exponent and a_bad), l.260-275, l.340-405, l.485-500, l.605-625, l.640-690, l.780-820.
- REVIEW_RLARGE_V3.md l.40-95, l.150-200, l.255-320, l.360-400.
- HW.md l.160-230 (tower energies, Lemma TE, (CLS-min)_{c,t}, W-bad, W-cb), l.590-600, l.1000-1010, l.1630-1645.
- LINEAR_PACKAGE.md l.65-75, l.115-190.
- BFT_B.md l.236-242, l.2185-2200, l.2677-2720 (NF-uniq, REF/(N1-bd), NF-ex), l.2820-2850, l.2963-3005 (Lemma N1G).

Scratch work (mine; written independently of the session's scripts, pure-python 2x2/exact arithmetic, no BLAS, no lock
needed, nothing left running):
`/private/tmp/claude-502/-Users-jonBridger-Toy-Physics--claude-worktrees-yang-mills-proof-df9972/a931aaa3-5369-4512-9e8d-b8590010706c/scratchpad/rsq4/`
- `su2.py` — R1: is the det-normalised polar factor the SU(2) maximiser of Re tr(W⁻¹M)? (400 instances, perturbed and
  unperturbed, compared against the quaternion-projection maximiser).
- `consts.py` — R2: the numerical thresholds implied by the session's own stated constants (θ_G, LEV-E's condition, τ_R,
  η_♭, t_pr) and the C_err / θ_0 model, validated against the three recorded θ_0 values of §0.3 [RSQ1-fix M-6].
- `prov.py` — R3: the byte arithmetic of the §T4 pre-statement and of the [RSQ3-fix] insertions.

Line numbers are SQ.md's unless another file is named.

---

## Bottom line

- **Provenance is clean but, in this worktree, unverifiable by file times.** Every mtime under the lane dir reads
  2026-10-28 08:03:19 (the worktree checkout), so REVIEW_SQ_S3's mtime evidence no longer exists for anyone re-reading. The
  one number I *can* check matches exactly: §T4 (l.1295-1369) is **7853 bytes = 138407 - 130554**, the figure SQ_LOG claims
  (S4-1). §T4 cites no session-4 result. All sixteen [RSQ3-fix] fixes are present at the cited lines with the original text
  kept (S4-2).
- **Route β is right, and the "integrable, not bounded" step is NOT where it fails.** I looked for the
  averaged→pointwise slippage the brief names and did not find it. The promotion happens *inside* EPS-T, and it is licensed
  by q > d = 4: the source enters in divergence form through ⟨𝒮, D_1*(ψu)⟩ with weight R^{1-4/q}, so an ℓ^q source with
  q > 4 gives a genuine sup bound. I re-did the exponent bookkeeping at q = 8 and it is exactly scale-invariant
  (S4-5). TPL, LEV-E, LOC-T, CARL, GARSIA and the composition to Theorem EPS-0 all re-derive correctly (S4-7 … S4-12).
  CARL is the real content: the ℓ¹ curvature averages below the scale of Q sum geometrically and Cauchy-Schwarz at the
  scale of Q converts them into the *global* ℓ² energy, with no k anywhere.
- **EPS-T has one real hole in its hypotheses, and it is not the Moser iteration.** The proof asserts
  "|u| ≤ ε pointwise … so every plaquette of B_R has η ≤ c_Nε ≤ ¼" (l.1467-1468). That is circular: §15.0's two-sided
  comparison (l.1389-1390) is itself conditional on ||1 - U(p)|| ≤ ¼, and small |𝒫| does **not** imply small ||1 - U||
  (in SU(2), U(p) = -1 gives 𝒫 = 0 and ||1 - U|| = 2). BIA, WB and §15.0's R_1 bound all need η small. The fix is one
  added hypothesis and is harmless in every application in §15 (S4-3).
- **The decision on (CLS-min): PARTIAL.** The *form* is exactly what RLARGE consumes — every m ≥ 1, level-m side ≥ 3,
  every top V, min-form in ||1 - V_P||²_op, with ℰ_P(V) the cone-local free-boundary infimum (HW l.178-183). No
  level-uniformity, norm, boundary or cone-locality mismatch: I checked each clause (S4-14). But RLARGE's *number*,
  a_bad = c_pr·min{ε_1², t_pr²} = c_prε_1², is valid only while ε_1 < t_pr, which REVIEW_RLARGE_V3 l.286 and l.313 already
  record as **C_D ≲ 7·10¹⁵**. Session 4 makes C_D a function of EPS-T's *uncomputed* Moser constant: C_D ≈ (0.5-0.9)·10³·C_T.
  So the condition now reads **C_T ≲ 10¹³**, and nothing in the session bounds C_T. From the written proof I can already
  identify factors 128² ≈ 1.6·10⁴ and e^{8.3} ≈ 4·10³ inside C_T; whether the remainder keeps the product under 10¹³ is
  genuinely open. **EPS-T as stated is therefore not usable by RLARGE** (S4-15).
- **The session also silently moves three recorded numbers and does not say so.** Its own constants force
  θ_0 ≤ 1.46·10⁻¹³ (CARL; LEV-E independently gives 3.0·10⁻¹³), hence τ_R ≤ 2.75·10⁻¹⁵, which becomes the binding entry of
  DESC's τ_♭ in place of SUP-price's θ_0/C' = 1.4·10⁻¹⁰; η_♭ falls from ≈10⁻²⁶ to ≈4·10⁻³⁶ and t_pr from 7.6·10⁻⁹ to
  ≈1.5·10⁻¹³. None of this breaks a_bad (the min is still at ε_1²) but all of it is new, and it is the lead's business
  (S4-13).
- **Both failed checks are honestly reported, and one of them reverses a previous review.**
  - q4b P0: substantive about the *check*, not the mathematics. I reproduced the mechanism independently (R1): the
    det-normalised polar factor of a complex-perturbed M has stationarity residual ~10⁻⁹ while the quaternion-projection
    maximiser is exact to 10⁻¹⁶, and the *value* difference is 4·10⁻¹⁶ (second order) — which is why K3 still passes.
    This **corrects REVIEW_SQ_S3's R1** ("for SU(2), q4's polar factor is exact"), true only on the quaternion line (S4-16).
  - q5 T2: the error is in the **pre-registered criterion**, not only in the script as §15.5 l.1717 says. The criteria file
    defines Q_str := L⁻³Σ_transverseΣ_{i<L} (block-face lines), which is not LINEAR_PACKAGE l.71's
    Q_str := L⁻⁴Σ_{y∈B(X)}Σ_{j<L}. The two have the same total mass L, which is why BFT_B l.2189's coarse-average reading
    cannot tell them apart; only d∘Q_str = Q_2∘d can, and it holds only for the second. TPL is untouched (T1 is exact), but
    the session now has **no pre-registered test** of the identity STOKES-NA actually uses (S4-17).
  - q5's W1-W3 and B1 run on a torus of **side 3**, where every pair of plaquettes is within ℓ^∞ distance 1. WB's locality
    claim (support in N_2(p), coefficient M_3η(p)) and the radius-3 box of its proof cannot be tested there at all (S4-18).
- **(CVX-K) really is not needed**, and LU-ex's proof really does not consume it (S4-19). LU-ex's replacement for the
  continuity method (Wilson flow + GAP + IFT, no Łojasiewicz) is complete in structure (S4-20); its threshold ε_U is not
  explicit and inherits S4-3 through GAP.
- **REVIEW_SQ_S2's "BFT as stated is insufficient" is now moot for SQ, and the session does not record it.** θ_w = 2 and
  θ_r > 2 are proven here, and EPS-T + NREFL + RED-0 do supply the free-boundary cone-box ε-regularity clause that
  REVIEW_SQ_S2 item 4 asked of lane A. §13.8 was not updated (S4-21).

---

## Part 1. Provenance, Step 1

### S4-1 (order of edits): **CONFIRMED as a self-report; the one checkable number matches exactly. NOT-VERIFIED by file times.**
- The claimed order (SQ_LOG l.144-171) is: §T4 at 11:14:39 → Step 1 11:15-11:17 → checks/q4b_criteria.md 11:17:10 →
  q4b_newton.py 11:17:26 → q5_criteria.md 11:25:21 → q5_lattice_ids.py by 11:29:07 → the runs 11:29:41-11:29:50 → §15 and
  §16 11:32-11:40:36. §15's header (l.1370) and §16's (l.1726) assert the same order internally.
- **Every mtime and ctime under the lane dir is 2026-10-28 08:03:19** (the worktree checkout). I checked SQ.md, SQ_LOG.md,
  all of checks/q4*, checks/q5*. REVIEW_SQ_S3 Priority 1 could still read the EDT stamps; a reviewer today cannot. This is
  not the session's fault, but it means the criteria-before-script and §T4-before-Step-1 rules are now backed only by
  SQ_LOG's own text. Flag for the lead: if provenance is to remain auditable, the stat lines have to be *quoted* in
  SQ_LOG (they are, for §T4, q4b_criteria and q5_criteria: "stat 07:14:39/07:17:10/07:25:21 EDT") and nothing more can be
  recovered.
- **The byte arithmetic is exact** (R3). SQ_LOG l.145 claims SQ.md went 130554 → 138407 bytes at the §T4 append, i.e.
  §T4 = 7853 bytes. The §T4 block as it now stands, l.1295-1369 (the session header through the blank line before §15), is
  **7853 bytes**. Lines 1-1294 are now 139433 bytes, so the [RSQ3-fix] insertions total 139433 - 130554 = **8879 bytes**;
  my crude paragraph delimiter put 18 tagged blocks at ≤10329 bytes, over-counting because two blocks (l.1028-1041,
  l.1166-1175) run into pre-existing text. Consistent.
- **§T4 cites no session-4 result.** I read l.1297-1368 line by line. Every forward reference is either a plan
  ("[planned: PROVEN-HERE]"), a constant *name* to be defined (C_B, C_K, C_S, C_GS, C_0, C_β, θ_E, θ_G, τ-small), or a
  prior-session / REVIEW_SQ_S3 item. The pre-statement is unusually tight: Proposition EPS-0b-avg's final form (l.1611)
  reproduces §T4 l.1354 verbatim including the factor 2, and LOC-T's exponential form (l.1570) matches §T4 l.1348. That is
  good evidence of order, not of ignorance — and the session correctly discloses that unrecorded exploratory reasoning
  preceded it (l.1297), so its only claim is file order. Accepted.
- **Disclosed drift from §T4 to §15:** the six "[post-proof correction]"s at l.1372-1377. Of these, (6) (EPS-T needs
  scale-invariant source smallness) and (3) (no Łojasiewicz) are real changes to a pre-stated statement and are flagged
  where they occur (l.1461-1463, l.1673-1674). Honest.

### S4-2 (Step 1: the [RSQ3-fix] edits): **CONFIRMED. All sixteen applied, original text kept.**
I located each one: S3-1 (l.912-916), S3-2 (l.1137-1141), S3-3 (l.1164-1165 and l.1287-1290), S3-4 (l.1193-1199),
S3-5 (l.1207-1212), S3-6 (l.1166-1175, l.1217-1219, l.1253-1256), S3-7 + M3-8 (l.1236-1242), S3-8 (l.1275-1279),
M3-1 (l.1019-1022), M3-2 (l.827), M3-3 (l.1028-1030), M3-4 (l.1057-1059), M3-5 (l.1075-1077), M3-6 (l.1115-1117),
M3-7 (l.1134-1136). Each says what REVIEW_SQ_S3 asked, including the two that were only recommended (S3-2) or purely
cosmetic (M3-2's "(paired energy-residual sources; S2-3)"). The tally correction S3-3 is carried through to §16's
"14 (11 + 3)" (l.1746).
- One defect: **l.1277 points q4b at "§15.6", which does not exist** — q4b is recorded in §15.5 (l.1700-1710). Minor
  (M4-1).

---

## Part 2. Theorem EPS-T (l.1458-1509) and its lemmas

### S4-3 (the missing smallness hypothesis): **CONFIRMED-WITH-FIX. This is the one real hole in §15.1.**
EPS-T is stated "for every SU(N) configuration on a 4D lattice torus (or on Z⁴) and every embedded cube B_R … with
||𝒫||_{ℓ²(B_R)} ≤ ε_* and R^{3-4/q}||𝒮||_{ℓ^q(B_R)} ≤ ε_*" (l.1460-1463). The proof's second sentence is
> "|u| ≤ ε pointwise on B_R (SOB (c)), so every plaquette of B_R has η ≤ c_Nε ≤ ¼ and the lemmas apply" (l.1467-1468).

The step η ≤ c_Nε is not available. §15.0 l.1389-1390 states the comparison as
"**For ||1 - U(p)|| ≤ ¼**: c_N⁻¹|log U(p)| ≤ |𝒫(p)| ≤ |log U(p)|" — the smallness of η is the *hypothesis* of the
comparison, not its conclusion. And the implication really does fail: 𝒫 is the traceless part of (U - U*)/2, which
vanishes on every Hermitian unitary. In SU(2) that is exactly U = ±1, so U(p) = -1 gives |𝒫(p)| = 0 with
||1 - U(p)|| = 2; in SU(N) the whole set of involutions (e.g. diag(-1, -1, 1) in SU(3)) is invisible to 𝒫. A
configuration can therefore have ||𝒫||_{ℓ²(B_R)} = 0 and plaquettes at distance 2 from 1 (take one link equal to the
central element -1 ∈ SU(2): six plaquettes flip to -1, 𝒫 ≡ 0).

Three of EPS-T's four lemmas need η small:
- **BIA** (l.1419-1420) has it as an explicit hypothesis: "If ||1 - U(f)|| ≤ ¼ for the six faces of a 3-cell c".
- **WB**'s proof (l.1437-1441) needs the axial-gauge ladder bound ||U(b) - 1|| ≤ 12·M_3η(p) and the expansion
  Ad_γ = 1 + O(M_3η) to be a *small* perturbation of the abelian operator; at η ≍ 1 the bound is vacuous.
- §15.0's **R_1 bound** (l.1396) and step (1)'s |R_1|, |B| ≤ C(M_1u)² (l.1469-1470) are obtained from
  "η ≤ c_N|u|" — the same unavailable step.

I could not turn this into a counterexample to the *statement*: the conclusion also speaks about 𝒫, sup ≤ ℓ² is free, and
the source hypothesis R^{3-4/q}||𝒮||_{ℓ^q} ≤ ε_* already forces ε ≲ ε_*R^{-3+4/q} on a spike. So I do not call EPS-T
WRONG. But its proof does not cover the stated hypothesis class, and the gap is in the *hypotheses*, which is exactly
where a theorem that other lanes will cite must be right.
- **Fix S4-3 (binding).** Add to EPS-T: "and sup_{p ⊂ B_R}||1 - U(p)|| ≤ ¼" (equivalently: all plaquettes of B_R in
  Lüscher's admissible sector), delete the "so every plaquette … η ≤ c_Nε" sentence, and derive η ≤ c_N|u| from the new
  hypothesis instead. Harmless downstream: Corollary EPS-0a and Theorem EPS-0 have ||1 - U_0(p)|| ≤ √(2NE) ≤
  1.6√(Nκ_+)θ ≤ 2.6·10⁻¹³ (M2-1; θ ≤ θ_0 by S4-13), NREFL's crossing plaquettes are exactly 1 and its images carry the
  same η (l.1404-1407), and GAP has ||1 - U(p)|| ≤ √(2N)ε_G from Σ_ps ≤ ε_G² (l.1661). State that in one line at each
  use so the hypothesis is visibly discharged.

### S4-4 (the status word on EPS-T): **NARROWED.** PROVEN in structure; the label overstates what is written.
The session is candid — "the Moser iteration is written at the level of its inequalities" (l.1459), "constants
uncomputed" — but then tags the item **PROVEN-HERE** and counts it (l.1742). Under the lane's own rule ("PROVEN = a
complete proof is written out in the file, from stated hypotheses") several steps are asserted rather than carried out:
- step (2)'s cutoff split, where the Young absorption is run against ψ̄ ≥ ½ζ_min²w_max^{β-1} (l.1486). The inequality
  ψ̄ ≥ ½ζ_min²w_max^{β-1} is correct (either ζ_min²w_max^{β-1} or something larger appears in ψ̄), but it is vacuous at a
  site where ζ vanishes, and the repair — the standard "ζ_max² ≤ 2ζ_min² + C/r²" trick quoted at l.1486 — is stated, not
  executed;
- step (3)'s transfer of neighbour maxima onto a single site ("w(p)^αw(p')^γ ≤ w(p)^{α+γ} + w(p')^{α+γ} and
  ζ(p)² ≤ 2ζ(p')² + 2(6/r)²", l.1483-1484), which is where the "≤ 200 terms" of WB and the N_3 maxima are absorbed;
- step (6)'s "(★) with Hölder, interpolation and SOB gives … the standard Moser step" (l.1497-1502).
I re-derived every one of these at the level of inequalities and found **no error**: the discrete convexity identity at
l.1472 is exact (I verified
⟨b - a, ψ_bb - ψ_aa⟩ = ψ̄|b - a|² + ½(ψ_b - ψ_a)(|b|² - |a|²) algebraically); the sign of
½ζ_b²(w_b^{β-1} - w_a^{β-1})(|b|² - |a|²) is correct because w is monotone in |u|; Stage 1's critical absorption
(||V_c||_{ℓ²} ≤ C(ε + ε²), Hölder against ||ζ̃W̃||²_{ℓ⁴}, SOB (a)) is Uhlenbeck's absorption and is right; Stage 2's two
potentials really are supercritical with scale-invariant norms (R||V_c||_{ℓ⁴} ≤ Cε_* and R^{2-8/q}||V_s||_{ℓ^{q/2}} = C,
l.1496-1497); the iteration product Π_i(C16^iβ_i⁴)^{1/p_i} converges because 1/p_i = 2^{-i-1} and β_i⁴ ≍ 16^i.
- **Fix S4-4 (binding, status only).** Relabel: "PROVEN-HERE modulo standard Moser bookkeeping (the cutoff/Young and
  neighbour-maximum steps are written as inequalities, not expanded); constants uncomputed." Keep it counted. A reader
  in RLARGE or BFT must not read "PROVEN" here as "the constants exist on paper".

### S4-5 ("integrable, not bounded"): **CONFIRMED. There is no averaged→pointwise slippage. Name the arrow: it is inside EPS-T, and it is justified.**
The brief asks me to check every arrow of EPS-0b-avg ⇒ (EPS-0) ⇒ (REG-min) ⇒ (CLS-min) for the classic failure. I did,
and the architecture is deliberately built to avoid it:
1. **EPS-0b-avg ⇒ Corollary EPS-0a's hypothesis** (l.1611 → l.1512): this arrow stays averaged. The output is an ℓ^q
   norm, and EPS-0a's hypothesis is an ℓ^q norm. Nothing is promoted.
2. **Inside EPS-T**: the promotion happens here, at step (3)'s pairing ⟨𝒮 - R_1, D_1*(ψu)⟩ (l.1471). Because 𝒮 enters in
   **divergence form**, an ℓ^q source with q > d = 4 is subcritical for the Moser iteration: V_s = C|𝒮|²_loc/k² sits in
   ℓ^{q/2} with q/2 > 2 = d/2, and its scale-invariant norm R^{2-8/q}||V_s||_{ℓ^{q/2}} is exactly constant (l.1492-1493).
   This is the continuum fact that L^q data with q > d gives a Hölder (hence bounded) solution, transcribed to the
   lattice. The session states the mechanism correctly at l.1508-1509 and l.1616-1617. **Justified.**
3. **The exponent bookkeeping is exact, not approximate.** At q = 8 (l.1621): with
   (Σ_{box_0}|𝒮|⁸)^{1/8} ≤ (32n⁴)^{1/8}C_0θn⁻³ (l.1611), the hypothesis side is
   n^{3-4/q}·(32n⁴)^{1/q}·C_0θn⁻³ = 32^{1/q}C_0θ — the n's cancel identically — and the conclusion side is
   n^{1-4/q}·(32n⁴)^{1/q}·C_0θn⁻³ = 32^{1/q}C_0θn⁻². Both match l.1625-1626. I also checked the factor-of-16 bookkeeping
   through NREFL (||𝒫||_{ℓ²(𝕋_R)} = 4||𝒫||_{box_0}, ||𝒮^R||_{ℓ^q} = 16^{1/q}||𝒮||_{ℓ^q}, R = n/2) and C_T' = 2^{2+4/q}·4C_T
   covers both terms.
4. **(EPS-0) ⇒ (REG-min) ⇒ (CLS-min)** are pointwise→pointwise (STOKES-it, RES-dec, FORCE, DESC), already CONFIRMED by
   REVIEW_SQ_S3 and re-checked in S4-14.
The only cost of the averaged route is that §15.3's conclusion is a bound on max_{level-0 p}||1 - U_0(p)|| obtained from
a *global* ℓ^q bound over box_0, which is where the big constants land (S4-13). That is a price, not a gap.

### S4-6 (R_0 = 64 is wrong; use 128): **CONFIRMED-WITH-FIX (arithmetic).**
l.1466 declares the statement trivial for R < R_0 := 64 and runs the iteration for R ≥ R_0. But l.1499-1503 set
i_* := ⌊log₂R⌋ - 6 and require r_i - r_{i+1} = R2^{-i-4} ≥ 4, i.e. 2^{i+6} ≤ R. At R ∈ [64, 128) this gives i_* = 0: the
iteration performs **no step**, p_{i_*} = p_0 = 2, and R^{4/p_{i_*}} = R², so the "gain" is only the trivial bound. The
claim is still true there (sup ≤ ε ≤ R_0²R⁻²ε), but with R_0 = 128, not 64.
- **Fix:** set R_0 := 128, and note explicitly that C_T ≥ 128² = 16384 from this branch alone.
- Related, and worth stating because it is the only explicit constant in §15.1: l.1504's "R^{4/p_{i_*}} ≤ R^{256/R} ≤
  e^{100}" is valid but 36 orders crude. The true supremum over R ≥ 128 is attained at R = 128 and equals 128² ≈ 1.6·10⁴,
  decaying to 1 for large R. Replace e^{100} by 1.6·10⁴ — it matters for S4-15.

### S4-7 (NREFL, BIA, WB, SOB as lemmas): **CONFIRMED, with S4-3's hypothesis and S4-18's caveat on WB's numerics.**
- **NREFL** (l.1401-1415) is correct and is the session's cleanest piece. (a): a crossing link in direction ν sits in a
  plaquette whose two t-links are mirror images and carry the same matrix, so the holonomy is W·1·W⁻¹·1 = 1 — right. (c):
  because every non-box plaquette containing a box link is a crossing plaquette and is flat, 𝒫 = 0 there and it
  contributes nothing to the torus gradient at a box link, so the torus gradient equals the **free-boundary** box
  gradient. This is precisely the nonlinear REFL that REVIEW_SQ_S2 (NA-1) left ARGUED and REVIEW_SQ_S3 l.261 flagged as
  still ARGUED: **it is now proven**, and q5 R1 is a real exact-identity check of all four clauses.
- **BIA** (l.1419-1428): the spanning-tree gauge is legitimate (|D_2𝒫| is gauge invariant; 7 tree edges of the 3-cube,
  5 non-tree edges each of which is a lasso around one or two faces), D_2𝒫(c) = Σ_fε_f𝒫(f) exactly in that gauge because
  the three transports at the base vertex are tree edges, and Σ_fε_f log U(f) = O(ε²) by abelian dd = 0 on the first-order
  parts. 𝒫(f) = log U(f) + O(|log U(f)|³) covers the rest. Correct.
- **WB** (l.1431-1441): (i) the Hodge identity dd* + d*d = Σ_λ∂_λ*∂_λ on 2-forms of a product cubical complex is standard
  and is exactly checked in q5 W1; (ii) gauge covariance of K is right; (iii) the axial-gauge/Ad_γ = 1 + O(M_3η)
  expansion is right in structure, with crude counts (≤ 200 terms, ladders of ≤ 12 plaquettes) that the session itself
  calls crude. The conclusion "on the lattice 'zeroth order' and 'first order with a small coefficient' coincide"
  (l.1442-1443) is the correct reading of REVIEW_SQ_S3's S3-4. **S4-F1 does not occur — CONFIRMED.**
- **SOB** (l.1445-1456): the discrete Gagliardo-Nirenberg/Loomis-Whitney route gives C_S = 3, and the even reflection to
  3Q with the path-graph Poincaré gap gives C_SP = 27C_S = 81 under S_max ≤ 2S_min. Correct; the torus 𝕋_R of sides
  (4n, 4n, 2n, 2n) meets S_max ≤ 2S_min with equality, so GS's use at l.1650 is legal.

---

## Part 3. Route β (§15.2) and Theorem EPS-0 (§15.3)

### S4-8 (TPL and the norm facts (N1), (N2)): **CONFIRMED by independent re-derivation. S4-F2 does not occur.**
With T_n(u) := #{(a, b) ∈ [0, n)² : a + b = u} (§2 l.404), the three claims at l.1531 follow:
max_uT_{L^m} = L^m, Σ_uT_{L^m}(u) = L^{2m}, and Σ_XT_n(s - nX) = n for every s (two non-zero terms at residue r,
summing to (n - r) + r). With the prefactor L^{-m}: in-plane max 1, row sum L^m, column sum 1; transverse max L^{-m},
row sum 1, column sum L^{-m}. The product over two in-plane and two transverse directions gives **entries ≤ L^{-2m},
row sums L^{2m}, column sums ≤ L^{-2m}** — exactly l.1531. (N1) is the Schur test √(row·col) = 1, written out correctly
at l.1548; (N2) is ||Tv||_∞ ≤ L^{-2m}||v||_{ℓ¹} combined with ||Tv||_{ℓ¹} ≤ L^{-2m}||v||_{ℓ¹}, giving
||Tv||_{ℓ²} ≤ L^{-2m}||v||_{ℓ¹}. All correct. q5 T1 checks the composition and the column sums in exact integer
arithmetic for m = 1, 2, 3 — a genuine check, and the one that matters, since TPL is what route β uses (S4-17).

### S4-9 (STOKES-avg): **CONFIRMED.** The collection
4C_e(m² + 1.011mx) ≤ 6.1C_e(m² + x²) (4·1.5055 = 6.02 ≤ 6.1) and
C_p((p_L + 1)m + 2.03x)² ≤ 2C_p((p_L + 1)² + 4.2)(m² + x²) reproduce C_S' at l.1541-1542 exactly, and
m² ≤ (1.011A_ax)²Σ_{p⊂R_q}F_{j-1}(p)² (max² ≤ sum) gives C_S''. The x² term is folded into 4.1x(q) under the stated
condition C_S'x(q) ≤ 0.05 (4.044 + 0.05 ≤ 4.1) — correctly carried into LEV-E's hypothesis "C_S'X_1 ≤ 0.05" (l.1553).
C_S' = 3.78·10⁴ and C_S'' = 5.56·10⁶ at N = 2, L = 3 (R2).

### S4-10 (LEV-E): **CONFIRMED. S4-F3 does not occur, and the reason given is the right one.**
I re-derived the three estimates. (a) ||E_i^x||_{ℓ²} ≤ 4.1X_i(24L^{4(k-i)})^{1/2} = 20.1C_rθ(L²q)^{k-i}, summing to
≤ C_Xθ with C_X = 21C_r/(1 - qL²) = 239.4 (R2; 4.1√24 = 20.1 ≤ 21 ✓, qL² = 2/3 ✓). (b) and (c) are right:
Σ_qΣ_{p⊂R_q}F² ≤ c_R𝓔 and ||v||_{ℓ²} ≤ (max v)^{1/2}(Σ v)^{1/2} give ||E_j^F||_{ℓ²} ≤ C_S''c_R^{1/2}𝓔_{j-1}. The
induction closes: Σ_{i<j}L^{-2(j-i)} ≤ L^{-2}/(1 - L^{-2}) = 1/8, so 𝓔_j^{1/2} ≤ e + 4e²C_S''c_R(9/8) ≤ e + 5C_S''c_Re²
≤ 2e under 5C_S''c_Re ≤ 1. **The explanation at l.1561-1563 is exactly right and is the structural point:** the main term
is the *direct* transport T^{(j←0)}F_0, an ℓ²-contraction by (N1), not a transport of F_{j-1}; errors made at level i
reach level j through ℓ¹ → ℓ² with gain L^{-2(j-i)}; the error made at level j is quadratic. So the recursion is
𝓔_j^{1/2} ≤ e + O(e²), not multiplicative.

### S4-11 (LOC-T): **CONFIRMED. S4-F4 does not occur, and the locality count is exact at L ≥ 3.**
(i) is a correct re-reading of §13.3: the straight weights sum to ≤ L⁻³ over the level-(l+2) links having b' in a contour;
the funnel part is ≤ 8·max(x + σ + σ') over the ≤ 8 links at the root c_Y of b''s own block (CC-NA at Y is exact — that
is what makes the funnel cancellation *local*); the remainder is 17.7√NA_d·(local f_{l+1}). Every maximum in §13.3's
per-level factor is over objects attached to b''s own block or its neighbours, so the factor is local. (ii) is exact:
the level-(l+1) link reached at step l is within Σ_{i≤l}2L^{i+1} ≤ 3L^{l+1} of b, the objects in a(b_l) within a further
2L^{l+2}, and 3L^{l+1} + 2L^{l+2} ≤ L^{l+3} ⟺ L² - 2L - 3 ≥ 0 ⟺ **L ≥ 3**, which is the lane's standing hypothesis. The
k factors and C_0 = 1.67Nκ_+κ̂^{1/2} check out (max|j_{k-1}| ≤ κ_+·1.01·1.65√κ̂θ from RES-dec steps (1)-(2), times N
for 𝒮 = -N·(kernel gradient)).

### S4-12 (CARL): **CONFIRMED. This is the mechanism, and it is depth-uniform for the stated reason.**
All three sums re-derive.
- The max→ℓ¹ conversion at l.1589 is right: A_l is constant on level-(l + 3) blocks, so
  avg_{x∈Q}max_{q⊂𝔑_{l+3}(x)}F_j ≤ |Q|⁻¹·L^{4(l+3)}·5⁴·Σ_{q⊂Q⁺}F_j, the 5⁴ because a given q lies in 𝔑(B) for at most
  5⁴ level-(l+3) blocks B.
- The F_0 term: the weight is 5⁴L^{4(l+3)-4M}·L^{-2j} with j = l + 1, i.e. 5⁴L⁸L^{-4M}L^{2j}; Σ_{j≤M-2}L^{2j} ≤
  (9/8)L^{2M-4}; and Cauchy-Schwarz over the ≤ 6·7⁴L^{4M} plaquettes of Q⁺⁺ converts L^{-2M}||F_0||_{ℓ¹(Q⁺⁺)} into
  (6·7⁴)^{1/2}||F_0||_{ℓ²}. **Every power of L^M cancels.** l.1594-1595's sentence ("the ℓ¹ averages of the curvature at
  the scales below Q sum geometrically to the ℓ² norm at the scale of Q") is the correct statement of why the Carleson
  constant is depth-uniform, and it is the only place in the session where the *energy* does the work.
- The X term is geometric in (qL²)^{M-2-i} with qL² = 2/3 < 1, and the e² term is geometric in L^{4j-4M}. Both fine.
- The level-M blocks tile box_0 exactly for M ≤ k (2n/L^M and n/L^M are integers), so |Q| = L^{4M}; M = k + 1 is handled
  separately at l.1598. No boundary problem.
- C_1 = (9/8)·5⁴·49√6·L⁴ = **6.84·10⁶** and C_qL³ = **1.796·10⁴** (R2).

### S4-13 (GARSIA and EPS-0b-avg): **CONFIRMED**, including the filtration orientation, which is the easy place to go wrong.
GARSIA (l.1600-1606) is Garsia's lemma and is correctly reproduced. The filtration is *decreasing* in the index
(F_{k+1} ⊂ … ⊂ F_0), a_m is F_m-measurable (constant on level-m blocks), and S_M = Σ_{m≤M}a_m is the sum over the
scales *finer* than M. So E[S_M | F_M] ≤ β is "the expected future increment given the past ≤ β", which is the correct
Garsia hypothesis, and it is exactly CARL's statement (avg over a level-M block). The tower step
E[a_mS_m^{p-1}|F_M] = E[a_mE[S_m^{p-1}|F_m]|F_M] uses F_M ⊂ F_m and a_m F_m-measurable — correct. The induction gives
E[S^p|F] ≤ p!β^p and the exponential series gives (1 - λβ)⁻¹. a_m := C_qL³A_{m-3} is indeed F_m-measurable because
𝔑_{l+3}(b) depends only on Q_{l+3}(b) (l.1566-1568). EPS-0b-avg's final step (4 links per site, 4n⁴ sites, λ = q = 8,
qβ ≤ ½ so (1 - qβ)⁻¹ ≤ 2) is right. q5 G1 is a reasonable numerical sanity check of the inequality on three process
types.
**Theorem EPS-0** (l.1620-1627) then composes correctly, and l.1628-1630's "no bootstrap is used" is **true**: the two
hypotheses are τ-smallness at levels ≥ 1 and θ ≤ θ_0, and no decay, uniqueness or continuity enters. That is the
session's genuine advance, and it is the thing REVIEW_SQ_S2 S2-6 and REVIEW_SQ_S3 S3-5 said was missing.

### S4-14 (**the numbers the session does not state**): **CONFIRMED by me, NOT-VERIFIED by the session. Binding.**
§15.2 and §15.3 define θ_G, θ_ε, θ_0, τ_R, A_0, C_D only symbolically. Every constant needed to evaluate θ_G is stated
in the file, so I evaluated it (R2, at the file's own reference point N = 2, L = 3, κ_± = κ̂ = 1):
- ||F_0||_{ℓ²} ≤ 2.47√(Nκ_+)θ = 3.493θ (l.1526); C_X = 239.4, so **e = 242.9θ** (l.1552).
- CARL: β ≥ C_qL³·C_1·||F_0||_{ℓ²} = 1.796·10⁴ · 6.84·10⁶ · 3.493 · θ = **4.29·10¹¹·θ**.
  EPS-0b-avg requires qβ ≤ ½ with q = 8 (l.1609), i.e. β ≤ 1/16, i.e. **θ_G ≤ 1.46·10⁻¹³**.
- LEV-E independently requires 5C_S''c_Re ≤ 1 (l.1553), i.e. θ ≤ **3.04·10⁻¹³**.
- Hence **θ_0 = min{θ_G, θ_ε} ≤ 1.46·10⁻¹³** and, by the (REG-min) corollary's τ_R := min{τ_0, τ_*, τ_S, θ_S/C', θ_0/C'}
  (l.1633), **τ_R ≤ 2.75·10⁻¹⁵**.
Consequences the session does not record:
1. **τ_R becomes the binding entry of DESC's τ_♭** (§0.3 l.294-295, l.318-319), displacing SUP-price's
   θ_0/C' = 7.6·10⁻⁹/53 = 1.43·10⁻¹⁰ which §0.3 [RSQ1-fix M-6] l.218-219 records as "DESC's binding entry". That
   statement is now stale.
2. **η_♭ = c_♭τ_♭²/C'² falls from ≈10⁻²⁶ to ≈4.2·10⁻³⁶** (l.349's "η_♭ ≈ 10⁻²⁶ (C_D = 2)"), shrinking DESC-ε's domain of
   validity by ten orders. Nothing I read needs E above 10⁻³⁶, but every consumer of DESC-ε's size clause (§0.5) should
   be re-checked against the new number.
3. **t_pr = C'τ_♭ falls from 7.6·10⁻⁹ to ≈1.5·10⁻¹³**, which is the quantity RLARGE's a_bad depends on (S4-15).
4. **θ_0 collides with §0.3's θ_0.** §0.3 l.188 defines θ_0 := 1/(2C_err); §15.3 l.1622 redefines θ_0 := min{θ_G, θ_ε}.
   Both appear as "θ_0/C'" inside τ-formulas (l.1633 and l.294/l.318), and *both constraints apply*. Rename one
   (e.g. θ_ε-0 or θ_0^{SQ4}) — this is load-bearing, not cosmetic.
5. Minor: §15.3's θ_0 does not include the condition that makes the level-0 half of τ_0-smallness automatic,
   1.6√(Nκ_+)θ_0 < τ_0 (M3-6, l.1116). It holds numerically (3.3·10⁻¹³ ≪ τ_* = 5.6·10⁻⁵) but should be listed.
- **Fix S4-14 (binding).** Add a short "numerical thresholds" paragraph to §15.3 stating θ_G, θ_0, τ_R, τ_♭, η_♭ and t_pr
  at the reference point, and a sentence saying which entry of τ_♭ now binds. The lane's own standing instruction is that
  the constants are the enemy (lead decision D3); delivering (REG-min) without its threshold is delivering half the
  result.

---

## Part 4. Is (CLS-min) delivered to RLARGE, and in what form?

### S4-15 (the form, clause by clause): **CONFIRMED. No mismatch.**
The consumer's statement is HW.md l.178-180:
> **(CLS-min)_{c,t}**: for every m ≥ 1, every level-m plaquette P (level-m side ≥ 3) and every top V, the cone-local
> free-boundary minimum ℰ_P(V) = 𝓔^{𝒞(P)}(V) satisfies ℰ_P(V) ≥ c·min{||1 - V_P||², t²},

consumed only through Lemma TE (ii), with c_pr = c_♭/C'², t_pr = C'τ_♭, and used by W-bad (HW l.199-207), W-cb
(l.214-222), SAT and FV. I checked each clause against what route β actually produces:

| clause RLARGE/HW consumes | what SQ's chain delivers | match |
|---|---|---|
| **every m ≥ 1, depth-uniform c, t** | EPS-0 for every k with A_0, θ_0, τ_0 depth-uniform (l.1623-1624); the depth-uniformity comes from E_𝒞 ≤ κ_+π²θ²/8 being k-independent, so the ℓ² hypothesis of EPS-0a is k-free | ✓ |
| **level-m side ≥ 3** | SUP-price and DESC both carry it (l.187, l.320); EPS-T is stated for every R ≥ 1 with the small-R branch absorbed into C_T | ✓ |
| **every top V** (no amplitude threshold) | DESC (a) covers ||1 - V_P|| ≥ C'τ and DESC (b) covers < C'τ; REVIEW_RLARGE_V3 l.79 reads this correctly | ✓ |
| **min-form in ||1 - V_P||²_op** | DESC (b) gives c_♭min{θ/C', τ}² = (c_♭/C'²)min{θ², (C'τ)²} with θ = ||1 - V_P||_op | ✓ |
| **ℰ_P(V) = the cone-local *infimum*, free boundary, top four links fixed** | E_𝒞 as in §13.0 l.1005-1006 with free boundary and V fixed; NREFL reflects the **level-0** box across its own faces, which is exactly the free-boundary convention, and all level-0 links of box_0 are free variables | ✓ — and this is the clause REVIEW_SQ_S2 (NA-1) left ARGUED |
| **a cone-local, not global, statement** | box_0 has sides (2, 2, 1, 1)n; EPS-T is applied on cubes of radius n/2 embedded in the reflection torus (4, 4, 2, 2)n, and the ℓ^q source norm is taken over box_0 only | ✓ |
| **c_pr's value** | c_pr = c_♭/C'² = (1/640)/2809 = 5.56·10⁻⁷, built from SUP-price's C_1 = 160 and FORCE's C' = 53, **both independent of session 4** | ✓ unchanged |

So: route β's chain EPS-0 ⇒ (REG-min) [RED-0, l.1153-1159, CONFIRMED by REVIEW_SQ_S3] ⇒ DESC (b) [§0.3 l.298] ⇒
(CLS-min) produces (CLS-min) **in the form HW consumes**, with no level-uniformity, norm, boundary or cone-locality
mismatch. The FORCE step at l.1633-1634 is also correct: "τ-small" includes the top residuals on P's four links
(§13.0 l.1015-1016), so FORCE at j = k genuinely forces θ < C'τ_R ≤ θ_0 and the hypothesis θ ≤ θ_0 is not an extra
assumption on the data.

### S4-16 (the *number*): **NARROWED to a single explicit inequality, and it is NOT established. This is the finding the lead needs.**
RLARGE's whole defect price is a := min{θa_bad, a_A} with **a_bad := c_pr·min{ε_1², t_pr²}** (RLARGE l.88-89), and
RLARGE l.90 records "At ε_1 ≲ 6.7·10⁻⁴⁰, ε_1 < t_pr on both routes, so a_bad = c_prε_1² ≈ 2.5·10⁻⁸⁵". REVIEW_RLARGE_V3
already pinned the condition for that:
> l.286: "ε_1 < t_pr (REG-min) | t_pr = C′τ_♭ ≤ θ_0 ≈ 7.6·10⁻⁹ (C_D = 2), so ε_1 < t_pr **iff C_D ≲ 7·10¹⁵**" and
> l.313: "Caveats: (i) it needs C_D ≲ 7·10¹⁵".

I reproduced that condition exactly. Modelling §0.3's C_err (l.189) at N = 2, L = 3, κ_- = 1 with K = 78.3C_D,
K_top = 81.3C_D gives **C_err = 1.655·10⁷·C_D²**, hence θ_0^{SUP} = 1/(2C_err) = 1/(3.31·10⁷C_D²); this reproduces all
three recorded values (C_D = 0.45 → 1.49·10⁻⁷; C_D = 2 → 7.5·10⁻⁹; C_D = 2.25 → 5.97·10⁻⁹, against l.217-218's
1.5·10⁻⁷ / 7.6·10⁻⁹ / 6.0·10⁻⁹). Since t_pr = C'τ_♭ ≤ θ_0^{SUP}, the condition ε_1 < t_pr is
**C_D ≤ 1/(3.31·10⁷·6.7·10⁻⁴⁰) = 6.7·10¹⁵**, i.e. REVIEW_RLARGE_V3's number.

**What session 4 changes is that C_D is no longer an O(1) parameter.** l.1633-1634 sets C_D := max{G, C_r} with
G = 2(1.011A_0 + B_0) and l.1624 sets A_0 := c_NC_T'(2.47N√κ_+ + 32^{1/8}C_0), C_T' := 2^{2+4/q}·4·C_T (l.1513). At the
reference point: 2.47N√κ_+ + 32^{1/8}C_0 = 4.94 + 1.542·3.34 = 10.09, C_T' = 22.63C_T, B_0 = 4.1C_r/(1 - qL²) = 46.8, and
c_N ∈ [1, 2]. So

  **A_0 ≈ (2.3-4.6)·10²·C_T,  G ≈ (0.5-0.9)·10³·C_T,  C_D ≈ (0.5-0.9)·10³·C_T,**

and the consumable-form condition becomes

  **C_T ≲ 10¹³.**

The previously recorded C_D values (0.45, 2, 2.25) were parameters of an *open hypothesis*; now C_D is an output of
EPS-T, and **EPS-T's constants are uncomputed** (l.1459). From the written proof I can already identify two factors
inside C_T: the finite-iteration/trivial branch contributes ≥ 128² ≈ 1.6·10⁴ (S4-6), and the Moser product
Π_i(C16^iβ_i⁴)^{1/p_i} contributes C·e^{ln16·Σ(2i+1)2^{-i-1}} ≈ C·4·10³ with C the Stage-1 absorption and
neighbour-maximum constant (built from C_S = 3, C_SP = 81, the ≤200-term local sums of WB, the C_δ's and the Hölder /
interpolation constants of l.1491-1497). A product of 10⁹ is optimistic; 10¹⁵ is entirely possible. **The threshold sits
inside the plausible range**, so this cannot be waved away as "constants are crude but harmless".
- The parallel condition through θ_ε is safe: θ_ε ≈ ε_*/84 (l.1622), so t_pr > ε_1 needs ε_* ≳ 5.6·10⁻³⁸, and ε_* is an
  absorption threshold ≍ 1/C''' with C''' plausibly 10⁴-10⁸, i.e. safe by ~30 orders. **Only the C_T half is live.**
- If the condition fails, a_bad collapses from c_prε_1² ≈ 2.5·10⁻⁸⁵ to c_prt_pr², and with it a, n_H ≳ 2·10⁸⁷, the ≈184
  wrap levels (RLARGE l.613) and the coupling ceilings of RLARGE l.618-620. That is the whole quantitative spine of the
  large-field lane.
- **Fix S4-16 (binding).** Either (i) carry the constants through EPS-T to an explicit C_T (even a decade-level bound
  suffices), or (ii) state in §15.3 and in §16 that the delivery of (CLS-min) *in RLARGE's consumable form* is
  **CONDITIONAL on C_D ≤ 6.7·10¹⁵, i.e. on C_T ≲ 10¹³**, name it as a new OPEN item, and say that SQ does not supply it.
  Option (ii) is cheap and must happen now; option (i) is the real work and belongs in the next session.
- Note for the lead: this is the answer to "do SQ's consumers need EPS-T's constants explicitly?" — **yes, and to one
  decade.** It is also the exact shape of lead decision D3 ("the constants are the enemy") appearing inside a lane that
  otherwise reports a clean win.

---

## Part 5. The two failed checks

### S4-17 (q4b P0): **CONFIRMED as reported. Substantive about the check, not the mathematics — and it corrects REVIEW_SQ_S3.**
checks/q4b_out.txt: K1-K6 all PASS (K3 at 2.072·10⁻¹⁰ against 1e-8, reproducing REVIEW_SQ_S3's S3-8), P0 FAIL at
4.306·10⁻¹⁰ against 1e-13, OVERALL FAIL. §15.5 l.1701-1710 reports it as a FAIL and labels the diagnostic post hoc.
Honest.
- **Mechanism, verified independently (R1).** q4b_newton.py l.68-70 returns the det-normalised polar factor for N = 2
  without any Newton step, because q4b_criteria.md says "SU(2): unchanged (exact polar factor)". My own pure-python test
  over 400 instances: the det-normalised polar factor of a complex-perturbed M has **max stationarity residual
  3.7·10⁻⁹**, while the quaternion-projection maximiser (SU(2) = unit quaternions, so W_0 = P_H(M)/|P_H(M)|) is exact to
  **1.2·10⁻¹⁶**. The *value* gap Re tr(W_q†M) - Re tr(W_polar†M) is **4.4·10⁻¹⁶** — second order, which is exactly why
  K3 still passes at 2·10⁻¹⁰ and why the error never showed up before. The session's diagnosis (l.1703-1708) is right in
  every particular.
- **This reverses REVIEW_SQ_S3 R1** (l.398, l.407: "for SU(2), q4's polar factor is exact (9·10⁻¹⁷)"). That holds only at
  the unperturbed M, where M is a real combination of SU(2) elements and so lies in the quaternion span by construction;
  it is false at M + hδ with complex δ, which is precisely what K2 and K3 evaluate. Session 4 caught a reviewer error. It
  should say so explicitly rather than only "REVIEW_SQ_S3's … holds at the unperturbed M only".
- **What the FAIL falsifies:** only that q4b met its own stated precondition. Lemma K is not implicated (K1-K6 pass; my
  own value-gap measurement shows the maximiser error cannot move φ at first order). The criterion was mis-designed: P0
  ranges over *all* W_0 evaluations while the script deliberately leaves the SU(2) branch unimproved. The session's
  proposed repair ("project M onto the real-quaternion span first", l.1709) is the right one.

### S4-18 (q5 T2): **CONFIRMED as a FAIL; the session's attribution understates it. The error is in the pre-registered criterion, and the referral to lane B is under-specified.**
- q5_out.txt: T2 max |dQ_str a - Q_2 da| = **8.018·10⁻¹** against 1e-12.
- §15.5 l.1717 calls it "the script's Q_str". It is not only the script's: **checks/q5_criteria.md** (written before the
  script, 11:25:21) itself states "Q_str := L⁻³Σ_{transverse offsets}Σ_{i<L} (straight lines from the block face)". So a
  **pre-registered criterion asserted a false identity**. Under the lane's rules that is the more serious reading, and
  §15.5 should say it.
- **What the two operators actually are.** I read q5_lattice_ids.py l.191-203: `Qstr(Y, d)` sums `a[x, d]` over all L³
  transverse offsets and all L longitudinal positions inside the block, divided by L³ — i.e. **the uniform average of the
  L⁴ block links in direction d, normalised by L⁻³**. LINEAR_PACKAGE l.71 defines
  **(Q_strA)(X, μ) := L⁻⁴Σ_{y∈B(X)}Σ_{j<L}A_μ(y + je_μ)** — each link weighted by the tent T_L over 2L - 1 longitudinal
  values, normalised by L⁻⁴, with mass leaking one block beyond the face. Both have **total mass L**, which is why
  BFT_B l.2189's own consequence "(Q_strv)^c = L^{k-b}·s·avg(v)" and LINEAR_PACKAGE l.170's "||Q_str^T||_{∞→∞} = L⁻³"
  hold for *either*. The only property that separates them is d∘Q_str = Q_2∘d, and it holds only for the second:
  d(L⁻⁴Σ_{y∈B(X)}∮ along the four averaged lines) = L⁻⁴Σ_y∮_{∂sq_y}a = L⁻⁴Σ_yΣ_{p∈sq_y}da(p) = Q_2 da, exactly §2's
  Q_2 (l.402-403). I re-derived this analytically; T2b's 2.8·10⁻¹⁶ is what it must be.
- **So: cosmetic for SQ, potentially substantive for BFT_B.** TPL uses §2's Q_2 and nothing else (l.1528-1532), and T1
  checks it exactly, so route β is untouched. STOKES-NA (§13.4 l.1127) cites "dQ_root = dQ_str = Q_2d, §2, §11.3 (d)" and
  is therefore also fine on the LINEAR_PACKAGE reading. But **BFT_B l.2189's displayed formula reads as the uniform-block
  operator**, and the session's referral — "whether BFT_B's Q_str means the face-start lines is BFT_B's to state (flagged
  for lane B; not edited)" (l.1721-1722) — gives lane B no line number and no statement of what breaks.
  - **Fix S4-18 (binding).** In §15.5, (a) say the error is in the criterion, not only the script; (b) cite
    **BFT_B l.2189** and **LINEAR_PACKAGE l.71** side by side; (c) state the discriminating fact (equal mass L, equal
    ||Q_str^T||_{∞→∞} = L⁻³, equal coarse average on constants; **different d-intertwining**), so lane B can check in one
    read whether anything of theirs rests on d∘Q_str = Q_2∘d; (d) record that the session now has **no pre-registered
    test** of that identity, only the post-hoc T2b and this reviewer's derivation.

### S4-19 (what q5's PASSes do and do not establish): **NARROWED. W1, W2, R1, T1, G1 are real; W3 and B1 are much weaker than they look.**
q5_criteria.md fixes "torus side 3 for the operator checks (dimension 1458 for 2-forms)". On a side-3 torus the maximum
ℓ^∞ distance between two sites is 1, so **N_1(p) = N_2(p) = N_3(p) = the whole torus**.
- WB's two substantive claims are (α) the identity K = 0 at U ≡ 1 and gauge covariance, and (β) locality:
  K(u)(p) = Σ_{p'∈N_2(p)}k(p, p')u(p') with ||k(p, p')|| ≤ C_K·M_3η(p), proved in a box of ℓ^∞ **radius 3** (side 7,
  l.1437). **(α) is genuinely checked** — W1 gives max|K| = 0 exactly at U = 1 and W2 gives 3.6·10⁻¹⁵ on a Haar-random
  pure gauge, which together test the Hodge identity and gauge covariance and are strong. **(β) is not checked at all**:
  the support claim is vacuous at side 3, M_3η degenerates to the global max, and the radius-3 box of the proof does not
  embed in the torus used. W3's R_K = ||K||_op/η_P ∈ [3.48, 3.88] is a global scaling ratio, not an entrywise test.
- The same applies to B1: R_B is measured on 3-cells of a side-3 torus; the lasso/spanning-tree geometry of BIA's proof
  is local and would be better tested on a larger torus with a localised perturbation.
- **Fix (recommended, not binding).** A future check should run W3/B1 on a torus of side ≥ 9 with a single localised
  perturbation and verify (i) k(p, p') = 0 for |p - p'| > 2 and (ii) ||k(p, p')|| ≤ C_K·M_3η(p) entrywise. Until then
  WB's locality half is **NOT-VERIFIED numerically** (the hand proof stands; I checked it in S4-7).
- Record keeping is otherwise good: the lock discipline (three holds, one mkdir and one rmdir each, nice 10, threads 1,
  no process left running, l.1723-1724), the resource figures (3.0 s / 57 MB and 5.6 s / 211 MB), and the two disclosed
  pre-run script edits (SQ_LOG l.154-155) are all in order. One note: both scripts run `python3` **without `-I`** and
  import numpy/scipy from the checks directory; that is the lane's established practice and the directory holds no
  shadowing module, so no finding.

---

## Part 6. Route α, (CVX-K), and the BFT requirement

### S4-20 ((CVX-K) "not needed"): **CONFIRMED. Verified by tracing every citation, including inside LU-ex's proof.**
- Route β (§15.1-§15.3) cites GS, LU-ap, GAP or LU-ex **nowhere**. Theorem EPS-0's proof (l.1625-1627) consumes only
  Corollary EPS-0a and Proposition EPS-0b-avg. So (EPS-0), (REG-min) and (CLS-min) do not touch route α.
- **LU-ex's own proof** (l.1675-1685) consumes: the Wilson gradient flow on the compact manifold SU(N)^{links}, GAP,
  LU-ap, GS (through LU-ap), the implicit function theorem, and the Hessian expansion of BFT_B 19.9 for the *gauge*
  functional Φ_t(g) = Σ_b|log U_t^g(b)|². (CVX-K) is a statement about the second variation of the **kernel terms** of
  the multi-level energy (l.1695-1697) and appears in none of these. Confirmed.
- The route-(α) verdict is correctly labelled: (i) level-0 slice convexity **[ARGUED]**, (ii) the corner computation
  **[ARGUED]**, (iii) (CVX-K) **OPEN** (l.1690-1698). No over-claim.

### S4-21 (LU-ex and the replacement for the continuity method): **CONFIRMED-WITH-FIX.**
Uhlenbeck's smallness-plus-continuity argument is genuinely replaced, and the replacement is complete in structure:
- **The dilation path becomes the Wilson flow.** ∫_0^∞|∇E_W|²dt ≤ E_W(U_0) gives t_n → ∞ with |∇E_W(U_{t_n})| → 0;
  compactness gives a subsequential limit that is critical with E_W ≤ ε_U²; **GAP** makes it flat, hence a pure gauge
  (box_0 is a product of intervals, so flat ⟹ pure gauge). This is why **post-proof correction (3) is right: no
  Łojasiewicz input is needed** — only one t_* at which U_{t_*} is near a pure gauge. ✓
- **The open/closed argument on [0, t_*]** is correct: 𝒯 is closed by compactness and continuity; open because LU-ap
  gives the *strict* bound ||w||_{ℓ⁴} ≤ C_Uε_U < η_1 at every t_0 ∈ 𝒯, and the IFT then continues the gauge. The IFT's
  nondegeneracy is supplied by the Hessian lower bound H(ξ) = H(ξ - ξ̄) ≥ ||dξ||² on {ξ(c) = 0}; the reduction
  H(ξ) = H(ξ - ξ̄) is legitimate because Φ(hg) = Φ(g) for constant h, so the constants lie in the Hessian's radical. ✓
- **GS** (l.1646-1651) and **LU-ap** (l.1653-1657) both check: Σ|∇w^R|² = ||dw^R||² + ||d*w^R||² = ||dw^R||² = 16||dw||²,
  SOB (b) on the torus per mean-zero component, and ||w||_{ℓ⁴(box)} = ||w^R||_{ℓ⁴}/2 give C_GS = 2C_SP = 162; LU-ap's
  bootstrap closes because C_3√24||w||²_{ℓ⁴} ≤ ½||w||_{ℓ⁴} under ||w||_{ℓ⁴} ≤ η_U.
- **GAP** (l.1659-1667) checks: 𝒮 = 0, EPS-T with zero source gives sup|𝒫| ≤ Cn⁻²√E; the complete axial gauge gives
  |a| ≤ C√E/n; Σ|𝒫|² = ⟨d*𝒫, a⟩ + ⟨𝒫, B'⟩ with |d*𝒫| = |d*𝒫 - (D_1^tr)*𝒫| ≤ CE/n³ and ≤ 16n⁴ links / 24n⁴ plaquettes
  gives Σ|𝒫|² ≤ C'''E^{3/2}; against Σ|𝒫|² ≥ (N/2)E this forces E = 0 or √E ≥ N/(2C'''). Correct.
- **Fixes.** (a) GAP uses EPS-T, so LU-ex inherits S4-3; add the one line discharging it (η ≤ √(2N)ε_G). (b) **The
  threshold ε_U is not explicit**: ε_U ≤ min{ε_G, ε_*} and ε_G < N/(2C''') with C''' containing EPS-T's constants, so
  "where SQ's consumers sit" cannot be checked. The available energy is E ≤ κ_+π²θ²/8 ≲ 2·10⁻²⁶ at θ ≤ θ_0, which makes
  compatibility overwhelmingly likely but unproven; say so instead of leaving the question unasked. (c) GS depends on
  **BFT_B Lemma REF (§19.11, PROVEN there given (N1-G)) and Lemma N1G (§22.2, IMPORTED-AND-REVERIFIED from
  REVIEW_BFT_B_S6 D.4)**. §16 lists them (l.1751) — good — but §15.4 should name their status inline, since LU-ex is the
  only counted item in the session that leans on another lane.
- "Why this is the lattice Uhlenbeck theorem" (l.1686-1688) is a fair claim: it is the critical-norm (ℓ⁴ ≍ L⁴ in d = 4)
  Coulomb gauge under small ℓ² curvature, uniform in box size, with no sup-decay hypothesis — which is exactly what
  REVIEW_SQ_S3 S3-7 / recommendation (3) asked for and what NF-ex could not supply.

### S4-22 (REVIEW_SQ_S2's "BFT as stated is insufficient"): **NARROWED — the requirement is now moot for SQ, and the session fails to record it. Binding.**
REVIEW_SQ_S2 l.305-306 and l.347-356 put two requirements on lane A: **item 3**, θ_w > 1 as a *stated value* rather than
BFT's existential "θ_w ∈ (0, 2]"; and **item 4**, "a uniqueness or ε-regularity clause in a ball large enough to contain
every cone minimiser whose sizes are all < τ_R at every level", with **item 1** asking for the free-boundary cone-box
form.
- Session 4 **supplies all three for SQ's own purposes**: θ_w = 2 for curvature and θ_r > 2 for residuals are now proven
  (l.1634-1635, l.1639-1640); and EPS-T + NREFL + RED-0 are precisely an ε-regularity clause on the free-boundary
  level-0 cone box, valid for every τ_R-small minimiser (not just BFT's critical point), which is item 4 in
  ε-regularity rather than uniqueness form. EPS-T **does** supply the missing cone-box clause.
- But **§13.8 (l.1244-1256) was not touched in session 4.** It still asks lane A for items (1), (3), (4). §16's
  "Consumers" bullet (l.1737-1738) does not mention it. SQ_LOG l.176-177 names it only as a *recommendation* for a
  future session ("§13.8 item (4) is then supplied by SQ itself"). So the file, read today, still records a demand on
  lane A that SQ has met itself — exactly the kind of stale cross-lane requirement REVIEW_SQ_S2 was written to remove.
- **Fix S4-22 (binding).** Append to §13.8: items (1), (3) and (4) are **withdrawn as SQ requirements** — SQ proves
  θ_w = 2 and θ_r > 2 (§13.3, §13.4, §15.3) and supplies the free-boundary cone-box ε-regularity clause itself
  (§15.1, §15.3) — while item (5) (identification of E_𝒞 with 𝔉_k restricted to the cone) stands, and BFT's Hölder part
  and minimiser uniqueness are still **not** supplied by SQ (l.1640 says so; keep it). Note that lane A's *other*
  consumers may still need items (1)/(3)/(4) and that this is a withdrawal on SQ's behalf only.
- Consequence for the cross-lane map: RLARGE l.490 row 9 and HW l.1005 row A5 both carry "SQ requires of BFT: θ_w > 1 as
  a stated value, and a cone-box uniqueness/ε-regularity clause". Those rows become stale once this review and session 4
  are accepted. Flagged for the lead (RLARGE and HW are not mine to edit).

---

## Part 7. Minor (M4-n)

- **M4-1.** l.1277 ([RSQ3-fix S3-8]) points q4b at "§15.6"; q4b is in **§15.5** (l.1700).
- **M4-2.** l.1504's "R^{4/p_{i_*}} ≤ R^{256/R} ≤ e^{100}" — valid, but the sup over the relevant range is 128² ≈ 1.6·10⁴
  (S4-6). Since this is the only numerical factor the session gives inside C_T, replace it.
- **M4-3.** l.1466's R_0 := 64 should be 128 (S4-6).
- **M4-4.** l.1622's θ_0 collides with §0.3 l.188's θ_0 := 1/(2C_err), and both occur as "θ_0/C'" in τ-formulas
  (l.1633, l.294, l.318). Rename one (S4-14 item 4).
- **M4-5.** l.1622's θ_0 should also carry 1.6√(Nκ_+)θ_0 < τ_0, which is what makes the level-0 half of τ_0-smallness
  automatic (M3-6, l.1116). It holds numerically; list it.
- **M4-6.** l.1611 writes (32n⁴)^{1/q} from "4 links per site and 4n⁴ sites"; box_0 has 4n⁴ sites, so 16n⁴ links and the
  factor 2 of the average gives 32n⁴. Correct, but the count silently includes links whose head leaves box_0. Say
  "conservatively".
- **M4-7.** l.1512's hypothesis is "n^{3-4/q}(Σ|𝒮|^q)^{1/q} ≤ ε_*/16"; l.1515 then applies EPS-T "with R = n/2", and the
  16^{1/q} ≤ 16 slack is what absorbs the halving. Correct, but state the inequality chain (one line) — it is the only
  place where the free factor could silently vanish.
- **M4-8.** §16 l.1748-1749 says "If review finds a gap in EPS-T or CARL, (REG-min) ⟺ (EPS-0) returns to OPEN and the
  tally to 14 / 3 / 2". Good foresight; note that S4-3 is a hypothesis gap in EPS-T that does **not** trigger this,
  because it is discharged at every use.

---

## Corrected tally

| Item | SQ's status | Reviewer |
|---|---|---|
| Step 1 ([RSQ3-fix] ×16) | DONE | **CONFIRMED** (all sixteen at the cited lines, original text kept); M4-1 |
| §T4 provenance | first edit, 7853 bytes | **CONFIRMED as self-report** — byte arithmetic exact; file times destroyed by the worktree checkout (S4-1) |
| Lemma NREFL | PROVEN-HERE | **CONFIRMED** — and it closes REVIEW_SQ_S2 (NA-1) / REVIEW_SQ_S3 l.261's ARGUED nonlinear REFL |
| Lemma BIA | PROVEN-HERE | **CONFIRMED** |
| Lemma WB | PROVEN-HERE | **CONFIRMED** (hand proof); locality half **NOT-VERIFIED numerically** (S4-19). S4-F1 does not occur |
| Lemma SOB | PROVEN-HERE | **CONFIRMED** (C_S = 3, C_SP = 81) |
| **Theorem EPS-T** (counted) | PROVEN-HERE, constants uncomputed | **CONFIRMED-WITH-FIX**: missing hypothesis sup||1 - U(p)|| ≤ ¼ (**S4-3**, binding); status word should be "modulo standard Moser bookkeeping" (S4-4); R_0 = 128 not 64 (S4-6). No error found in the iteration |
| Corollary EPS-0a | PROVEN as an implication | **CONFIRMED** (exponent bookkeeping re-checked; M4-7) |
| Lemma TPL, (N1), (N2) | PROVEN-HERE, uncounted | **CONFIRMED** (re-derived). S4-F2 does not occur |
| Lemma STOKES-avg | PROVEN-HERE, uncounted | **CONFIRMED** (C_S' reproduced) |
| Lemma LEV-E | PROVEN-HERE | **CONFIRMED**. S4-F3 does not occur; the stated reason is the right one |
| Lemma LOC-T | PROVEN-HERE | **CONFIRMED**; the locality count is exact at L ≥ 3. S4-F4 does not occur |
| Lemma CARL | PROVEN-HERE | **CONFIRMED**; this is the mechanism (C_1 = 6.84·10⁶) |
| Lemma GARSIA | PROVEN-HERE | **CONFIRMED** (classical; filtration orientation correct) |
| **Prop. EPS-0b-avg** (counted) | PROVEN as an implication | **CONFIRMED** |
| **Theorem EPS-0** | PROVEN as an implication, uncounted | **CONFIRMED**; "no bootstrap" is TRUE. The thresholds it implies are **not stated** (**S4-14**, binding) |
| (REG-min), PRICE-iii, DESC-ε, (CLS-min), (MIN-reg)_cone sup part | PROVEN as implications | **CONFIRMED in form** (S4-15); **the number is CONDITIONAL on C_D ≤ 6.7·10¹⁵, i.e. C_T ≲ 10¹³** (**S4-16**, binding) |
| Lemma GS, Theorem LU-ap | PROVEN-HERE | **CONFIRMED** |
| Lemma GAP | PROVEN as an implication | **CONFIRMED-WITH-FIX** (inherits S4-3) |
| **Theorem LU-ex** (counted) | PROVEN as an implication | **CONFIRMED-WITH-FIX**: the continuity method is genuinely replaced and the Łojasiewicz withdrawal is right; ε_U not explicit; depends on BFT_B REF + N1G (S4-21) |
| Route (α) level-0 convexity, corner | ARGUED | **CONFIRMED as ARGUED** (correctly labelled) |
| (CVX-K) | OPEN, not needed | **CONFIRMED** — not consumed anywhere, including inside LU-ex (S4-20) |
| q4b | FAIL (P0), disclosed | **FAIL stands; honestly reported.** Mechanism independently reproduced; **corrects REVIEW_SQ_S3 R1** (S4-17) |
| q5 | FAIL (T2), disclosed; T2b post hoc | **FAIL stands.** Error is in the **criterion**, not only the script; falsifies d∘Q_str^{uniform} = Q_2∘d; TPL untouched; referral to lane B under-specified (S4-18) |
| §13.8 BFT clause request | unchanged | **NARROWED**: items (1), (3), (4) are moot for SQ and must be withdrawn (**S4-22**, binding) |

**Counted items: I accept the session's 3** (EPS-T with NREFL/BIA/WB/SOB; EPS-0b-avg with LEV-E/LOC-T/CARL/GARSIA;
LU-ex with GS/LU-ap/GAP), two of them CONFIRMED-WITH-FIX. **File tally 14 / 1 / 2**, not 14 / 1 / 1: the OPEN column is
non-abelian (SQ) [off-path] and **(CONST-T): an explicit bound on EPS-T's C_T, equivalently C_D ≤ 6.7·10¹⁵** [**on** the
critical path]. (CVX-K) is correctly excluded as off the file's chain. If a later review finds a gap in EPS-T's
iteration or in CARL, the tally returns to 14 / 3 / 3 by the session's own rule (M4-8).

---

## (a) Binding fixes (next lane-G session)

1. **S4-3** (l.1460-1468). Add "and sup_{p ⊂ B_R}||1 - U(p)|| ≤ ¼" to Theorem EPS-T; delete the circular sentence
   "so every plaquette of B_R has η ≤ c_Nε ≤ ¼"; discharge the new hypothesis in one line at each of the three uses
   (Corollary EPS-0a: √(2NE) ≤ 1.6√(Nκ_+)θ; NREFL's images and crossing plaquettes; GAP: √(2N)ε_G).
2. **S4-16** (§15.3, §16). State that the delivery of (CLS-min) *in RLARGE's consumable form* is CONDITIONAL on
   **C_D ≤ 6.7·10¹⁵**, i.e. on **C_T ≲ 10¹³** (REVIEW_RLARGE_V3 l.286, l.313; C_D ≈ (0.5-0.9)·10³·C_T from l.1624,
   l.1633). Name it as an OPEN item (CONST-T) and say SQ does not supply it. Then, as the next session's main target,
   carry the constants through EPS-T to a decade-level bound on C_T.
3. **S4-14** (§15.3). State the numerical thresholds the session's own constants imply: θ_G ≤ 1.46·10⁻¹³ (CARL, q = 8),
   LEV-E's 3.04·10⁻¹³, θ_0 ≤ 1.46·10⁻¹³, τ_R ≤ 2.75·10⁻¹⁵, τ_♭ ≤ 2.75·10⁻¹⁵ (now the binding entry, displacing §0.3
   l.218's θ_0/C' = 1.43·10⁻¹⁰), η_♭ ≈ 4.2·10⁻³⁶ (was ≈10⁻²⁶), t_pr ≈ 1.5·10⁻¹³ (was 7.6·10⁻⁹). Note that a_bad is
   unaffected because the min in c_pr·min{ε_1², t_pr²} is still at ε_1².
4. **S4-22** (§13.8). Withdraw items (1), (3), (4) as SQ requirements on lane A (SQ now proves θ_w = 2, θ_r > 2, and
   supplies the free-boundary cone-box ε-regularity clause); keep item (5); keep the statement that BFT's Hölder part and
   uniqueness are not supplied. Flag for the lead that RLARGE l.490 row 9 and HW l.1005 row A5 go stale.
5. **S4-18** (§15.5). Rewrite the T2 paragraph: the error is in **checks/q5_criteria.md**, not only in the script; cite
   **BFT_B l.2189** against **LINEAR_PACKAGE l.71**; state the discriminating property (equal mass L, equal
   ||Q_str^T||_{∞→∞}, equal action on constants, **different d-intertwining**); record that no pre-registered test of
   d∘Q_str = Q_2∘d now exists (T2b is post hoc).
6. **S4-17** (§15.5). Say plainly that the post-hoc diagnostic **corrects REVIEW_SQ_S3 R1**: the SU(2) polar factor is
   the maximiser only on the real-quaternion line, so REVIEW_SQ_S3's "exact (9·10⁻¹⁷)" does not apply at the perturbed M
   that K2/K3 evaluate (reviewer-reproduced: residual 3.7·10⁻⁹ vs 1.2·10⁻¹⁶; value gap 4.4·10⁻¹⁶).
7. **S4-4** (l.1458-1459, l.1742). Relabel EPS-T "PROVEN-HERE modulo standard Moser bookkeeping; constants uncomputed",
   so that a downstream lane cannot read "PROVEN" as "the constants exist on paper".
8. **S4-6 / M4-2 / M4-3** (l.1466, l.1504). R_0 := 128; replace e^{100} by 128² ≈ 1.6·10⁴; record C_T ≥ 16384 from this
   branch.
9. **Minor:** M4-1 (§15.6 → §15.5), M4-4 (the θ_0 name collision — load-bearing), M4-5, M4-6, M4-7, M4-8.
10. **Recommended, not binding:** rerun W3 and B1 on a torus of side ≥ 9 with a localised perturbation, to test WB's
    support claim (k(p, p') = 0 for |p - p'| > 2) and the entrywise bound ||k(p, p')|| ≤ C_K·M_3η(p) (S4-19).

## (b) Independent tally

**14 PROVEN-HERE counted / 1 CONDITIONAL / 2 OPEN** (non-abelian (SQ) [off-path]; **(CONST-T)** an explicit bound on
C_T / C_D [on the critical path]), against the session's claimed 14 / 1 / 1. Session 4 contributes **3** counted items,
all three of which I confirm as mathematics — two with binding fixes (EPS-T: S4-3, S4-4, S4-6; LU-ex: S4-3 via GAP, plus
an unquantified ε_U). Nothing in §15 is WRONG. Three claims are NARROWED (S4-4, S4-19, S4-22), one is
CONFIRMED-WITH-FIX in its hypotheses (S4-3), and one previously recorded reviewer claim is **reversed in the session's
favour** (S4-17: REVIEW_SQ_S3 R1). Five pre-stated failure modes are correctly adjudicated: S4-F1, S4-F2, S4-F3 and
S4-F4 do not occur (each independently re-derived here); S4-F5's corner half does not occur [ARGUED] and its kernel half
is (CVX-K), OPEN and genuinely off the path.

## (c) Is (CLS-min) delivered to RLARGE, and in what form? **PARTIAL.**

**Yes in form, no in number.**
- **In form: delivered.** Clause by clause against HW l.178-180 and RLARGE l.88-90 — every m ≥ 1, level-m side ≥ 3,
  **every** top V, the min-form in ||1 - V_P||²_op, ℰ_P(V) read as the cone-local **free-boundary infimum** with the top
  four links fixed, depth-uniform constants, cone-local rather than global. I found **no** level-uniformity mismatch, no
  norm mismatch, no free-vs-fixed-boundary mismatch and no cone-local-vs-global mismatch. The chain is
  EPS-T + EPS-0b-avg ⇒ EPS-0 ⇒ (REG-min) [RED-0] ⇒ DESC (b) ⇒ (CLS-min)_{c_pr, t_pr}, with
  c_pr = c_♭/C'² = 5.56·10⁻⁷ unchanged by this session. The averaged source does **not** damage the delivery: the
  promotion to a pointwise bound happens inside EPS-T and is licensed by q > d = 4 (S4-5). This is a real result and the
  first time the lane has (CLS-min) off a hypothesis rather than on one.
- **In number: not yet delivered.** RLARGE consumes a_bad = c_pr·min{ε_1², t_pr²} and uses the branch c_prε_1², valid
  only while ε_1 < t_pr, i.e. (REVIEW_RLARGE_V3 l.286, l.313, reproduced here) **C_D ≤ 6.7·10¹⁵**. Session 4 turns C_D
  from an O(1) parameter of an open hypothesis into **C_D ≈ (0.5-0.9)·10³·C_T**, where C_T is EPS-T's uncomputed Moser
  constant. The condition therefore reads **C_T ≲ 10¹³**, and the session establishes no bound on C_T at all; my own
  reading of the written proof puts it somewhere in 10⁹-10¹⁵, straddling the threshold. Until C_T is bounded, RLARGE's
  a_bad ≈ 2.5·10⁻⁸⁵, a ≲ 1.0·10⁻⁸⁶, n_H ≳ 2·10⁸⁷ and the ≈184 wrap levels are **not** supported by this route.
- **Everything else is clean and should be propagated now:** the (CLS-min) ⇐ (REG-min) arrow stops being conditional on
  an open hypothesis and becomes conditional on a *constant*, which is a strictly better place to be; the cone-box
  free-boundary clause and θ_w > 1 stop being demands on BFT; and the thresholds of S4-14 should be entered in §0.3 and
  flagged to RLARGE and HW.

## (d) The biggest live wall

**(CONST-T): EPS-T's Moser constant.** Not the mathematics of route β — I attacked every arrow of
EPS-0b-avg ⇒ (EPS-0) ⇒ (REG-min) ⇒ (CLS-min) and they hold. The wall is that this lane's single new output is a
*quantitative* lower bound consumed by a lane whose entire price table (a_bad, a, n_H, the wrap count, the coupling
ceilings) is sensitive to it through one inequality, **C_D ≤ 6.7·10¹⁵ ⟺ C_T ≲ 10¹³**, and the proof that produces C_D is
written "at the level of its inequalities" with constants nobody has multiplied out. This is lead decision D3 reappearing
one lane over: a structurally correct theorem whose constants are four orders of freedom away from the thing the
downstream lane needs. The next session's highest-value work is not more theorem-building — it is to carry
C_S = 3, C_SP = 81, C_B, C_K, C_δ, the ≤200-term local sums and the Moser product through §15.1 to a decade-level value
for C_T and ε_*, and then re-enter θ_0, τ_R, τ_♭, η_♭ and t_pr in §0.3.

Second, well behind it: EPS-T's hypothesis gap (S4-3) — one line to fix, but it is the kind of thing a referee finds
first, and until it is fixed the theorem as stated is not what the proof proves.

## FOR OTHER FILES (not edited)

- **RLARGE.md** l.490 row 9 and l.87-96: "SQ requires of BFT: θ_w > 1 as a stated value, and a cone-box
  uniqueness/ε-regularity clause" goes stale on S4-22; and the a_bad entry should record the condition as
  **C_T ≲ 10¹³** (not only C_D ≲ 7·10¹⁵) now that C_D is an output of EPS-T. Also worth an open-item id alongside U7.
- **HW.md** l.1005 row A5 and l.180-183: same staleness; and t_pr's quoted value ("τ_♭ ≤ θ_0/C' with SQ's
  θ_0 ≈ 10⁻⁸/C_D²") should be updated to the S4-14 numbers once §15.3 states them.
- **BFT_B.md** l.2189: the displayed Q_str = s⁻³Σ_transverseΣ_{i<s}v reads as the uniform-block average, which does
  **not** satisfy d∘Q_str = Q_2∘d (q5 T2, 0.80; LINEAR_PACKAGE l.71 is the operator that does). Lane B should state which
  it means and check whether anything in §19/§22 rests on the d-intertwining.
