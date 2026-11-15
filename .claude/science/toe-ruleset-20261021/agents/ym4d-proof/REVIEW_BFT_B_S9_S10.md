# REVIEW_BFT_B_S9_S10: hostile review of BFT lane B sessions 9 and 10 (BFT_B.md §27-§37.4; checks bb9, bb9b, bb10, bb10c)

Reviewer: an independent agent. I wrote none of BFT_B.md, BFT_A.md, SF.md or any check. This file is the only repository
file I edited. No git command was run; no commit, PR or push. No numeric lock was taken (my own arithmetic is exact
`fractions.Fraction` in plain python, which DRIVE_BRIEF rule 6 exempts).

**Scope.** §27-§37.4 only. A session 11 was being appended to BFT_B.md while I read; everything after l.4307 (§37.4's
last line) is outside this review. BFT_B.md was 576227 B / 4385 lines when I finished, and the text I reviewed is
unchanged by that growth (appends only).

**Inputs** (`TZ=UTC stat`, read 2026-10-28 ≈13:30-14:10 UTC):
- BFT_B.md: birth 12:03:19 (worktree creation), mod 13:58:33, 576227 B. Reviewed range l.3570-4307.
- BFT_B_LOG.md: mod 13:58:46. Reviewed sessions 9 (l.422-495) and 10 (l.497-566).
- BFT_A.md: mod 12:03:19, 351969 B — **unchanged since the worktree snapshot**, so lane A session 8 is the version both
  sessions cite.
- REVIEW_BFT_B_S8.md: birth/mod 11:28 range, 38842 B (binding on session 8). REVIEW_BFT_A_S8.md: birth 12:45:36 — i.e. it
  landed after session 9 ended (12:42:41) and before session 10's first edit (13:07:28), which is consistent with §36.5 (v)'s
  "the review could not see §31".
- checks: bb9_criteria.md birth **12:31:25**, mod 12:34:06; bb9_rtcc.py birth 12:35:37; bb9.out 12:35:52; bb9b_rtcc.py
  12:36:21; bb9b.out 12:36:27; bb10_criteria.md birth **and** mod 13:12:15; bb10_cof.py 13:14:02; bb10.out 13:14:14;
  bb10c_criteria.md 13:24:27; bb10c_cof3.py 13:25:13; bb10c.out 13:25:14.
- SESSION24_RESULTS.md (mod 14:07:44) and HANDOFF.md (mod 13:31:34) — read only to see what has already been banked
  downstream.

**What I read.** BFT_B §27-§37.4 in full; §19.2-19.6, §24.1, §25.1 (a)-(f) in full; BFT_A §26.0-26.2 (l.2228-2265),
§28.5 (l.2465-2494) line by line, §28.11-28.12, Lemma RC and its *Reading* (l.3540-3553), the binding erratum
[RBA2-fix] B3/B4 (l.802-834); REVIEW_BFT_A_S5 l.28-32, l.370-375; REVIEW_BFT_A_S6 l.22-26, l.179-200; REVIEW_BFT_A_S7
l.318-322; REVIEW_BFT_A_S8 S8-4 (l.147-157), S8-12/S8-13 (l.351-374), "The biggest live wall" (l.550-590);
REVIEW_BFT_B_S8 "Required fixes" (l.454-502); SF.md Lemma G-pert (l.695-700) and [RSF2-fix GP-1/GP-2] (l.888-897).
Line by line: bb9_criteria.md, bb10_criteria.md, bb10c_criteria.md, and the scripts bb9_rtcc.py / bb9b_rtcc.py (full
diff), bb10_cof.py (helpers + A3-A8 + B0-B1), bb10c_cof3.py (header + shared core diff against bb9b).

**What I recomputed myself** (scratchpad `rev/indep.py`, exact `Fraction`, no BLAS, no lock):
1. The funnel kernel of BL-2 (b) rebuilt from the definition in d = 2, L = 3: **max|c(X, b)| = 1/3**, ℓ¹ row sum
   **4/3 ≤ d(L−1)/2 = 2**, every funnel link interior to its block, the row sum equal to the mean axial path length (so
   there is no cancellation to hide behind). This reproduces bb9b A4/A7 and bb10 A6 from scratch.
2. **K_f = 8.73768983885771…** at d = 4, L = 3, α = ¼, and the index swap of §29.3 re-derived by hand
   (L^{−(1−α)(k−l'−u)}L^{−3u} = L^{−(1−α)(k−l')}L^{−(2+α)u}).
3. **bb10c C4's bounds re-derived exactly** from the printed π_l, by the criteria formulas, for two instances:
   π = (448, 27, 9) → B^ψ = (1792, 2116/3, 2440/9), B^ξ_0 = 648, B^ξ_1 = 108; π = (229, 27, 9) → B^ψ = (916, 1240/3,
   1564/9). Both agree with `bb10c.out` to the last digit.
4. **bb10 A8's bounds re-derived exactly**: 2d·π_0(j_0) = 332 and 2d·L^{d−1}·π_1(j_1) = 108 at π_0 = 83, π_1 = 9.
5. The byte accounting (below), and the θ-optimisation of §35.6's constant (Part J).

I did **not** re-run bb9b, bb10 or bb10c (eight agents share one slot and the verdicts I needed are re-derivable in closed
form, as above). I did not re-open Theorem YH, Theorem W0's own inputs, LES-div, Theorem GU or Corollary LIN0.

---

## Bottom line

- **Provenance: CONSISTENT, with one claim the filesystem does not support.** §1-§26 are byte-for-byte untouched
  (l.1-3569 = **409782 B exactly**, the session-8 final size), and the two in-place §28 header corrections are confirmed
  to the byte (5259 + 119 + 80 = 5458). bb9's criteria genuinely precede its script (birth 12:31:25 < 12:35:37), and its
  amendment is a genuine append (birth ≠ mod). **bb10_criteria.md has birth = mod = 13:12:15**, which does not support
  "born 13:09:13, with one amendment appended at 13:12:09" (§37.1, l.4217); criteria-before-script still holds, but the
  pre-amendment text is not recoverable (S10-P2).
- **Lemma RT-cc: CONFIRMED. I rebuilt it and could not break it.** ev^{(0→l+1)T} is injective on the **whole** space of
  level-(l+1) functions (distinct roots, distinct level-0 sites), not on a subspace; and the cascade's consistency
  condition is **equivalent** to composite co-closedness, not merely implied by it, because the total-zero half of
  D(S) ⟂ Λ_0 is automatic (Σ_z ev^{(0→l)T}d*j_l = Σ_X d*j_l(X) = 0 on the level-l torus). The one-way-implication failure
  the task expected does not occur. The keystone holds.
- **Lemma FT, Theorem RHT-cc, Theorem RHT_m-cc: CONFIRMED** (kernel, index swap and K_f all independently re-derived;
  c_w = 14 is conservative — 12 suffices — which is harmless, S9-8).
- **Corollary RHT-V: CONFIRMED-WITH-FIX.** "For every gauge fixing" is exactly right and I re-derived it. But the
  parenthetical "(using ||r^c_{k−1}||_∞ ≤ ||x||_inv ≤ G_Rη² …)" (l.3739) is a **hypothesis**, not bookkeeping: it is
  (H-inv) for the same non-co-closed rows. (Res-Hölder) is an increment statement; stated as an absolute η² bound it is
  conditional.
- **>>> THE HEADLINE FINDING: Corollary COF-crit (§35.6) is WRONG, and Theorem NCE (i) is not k-uniform.** Theorem COF is
  correct for the (Pl-c) class, but §35.6 substitutes the **per-level** row bound π_l(V_l) ≤ 2C_NCC_bchκ_+L²η²
  ("uniform in l", l.3729, l.3735; BFT_B l.2629) for the **class norm** ‖V‖_Pc = max_l L^{θ(k−l)}π_l(V_l) ≍
  L^{θ(k−1)}η². Those differ by L^{θ(k−1)}. Taking the sharper route instead (Σ_l π_l(ĵ_l) directly, §35.4 step 3) gives a
  factor (k−1); optimising θ ≈ 1/((k−1)ln L) gives ≈ 25(k−1). This is exactly BFT_A's own binding erratum
  [RBA2-fix] B3 (l.819-824): "the level-0 images add up to Σ_l‖j^c_l‖ ≤ (k−1)η²: **the entire level-count loss sits in the
  level-0 image**", and Theorem COF's binding term is that level-0 image. It is also exactly the factor k that
  REVIEW_BFT_A_S8 S8-13 confirms stands ("the level sum stops being geometric, and the factor k returns") — and which
  **§36.5 (iv) itself says is untouched** (l.4209). §36.5 (i) and §36.5 (iv) cannot both be right.
- **Lemma W0-use, Lemma SPLIT, Lemma DF-cc, Proposition COF-size, Proposition COF-res, Remark MASSLESS,
  Proposition GT-split, Proposition GT-loc, Proposition GT-ell: CONFIRMED** (each re-derived; W0-use checked against
  BFT_A l.2465-2494 line by line). Session 10's structural work is good; its arithmetic step into the rows is where it
  fails.
- **Session 10 is RIGHT against session 9 on (CO-fun), on both counts** (Part O). (CC-0) is the right hypothesis, not a
  convenient one — it is exactly ψ_{k−1} = 0, i.e. "the top residual is co-closed", which is precisely what Theorem W0's
  own step 3 uses (BFT_A l.2473). **There is no circularity in Theorem COF**: it is a statement about sources, is
  non-vacuous without any critical point existing, and does not assume BFT-0.
- **But Theorem NCE (i)'s "at every critical point of 𝔉_k" is weaker than it reads in a second way**: it is an
  a-posteriori regularity statement about a fixed point, and the contraction that is supposed to construct that fixed
  point needs the estimate at non-critical iterates, which is the OPEN half. Lane A's (NC-Γ) was explicitly a
  ball statement ("for all configurations of the ball", §31 l.3777). The narrowing is real and the sessions mostly say so.
- **§36.2's headline — "(GT-sup) is not a spike-support question" — is NOT established** (S10-14). The inequality is
  correct, but it reduces (GT-sup) to (Y-sup^loc), a sufficient condition that is likely **false** exactly where the
  session says the hard case is: (Y-sup^loc) in coarse units demands max_own|Y^p_{*,0}| ≲ 1/n near p, while the only
  profile consistent with 𝒩(Y^p) ≍ n (a |z|^{−3} dipole, Σ_{r≤n}r³r^{−3} = n) has it O(1). The route is lossy by a factor
  n, as bb8t T1's own ‖kernel‖₁ ≈ 10.6n against the measured σ ≈ 0.003 shows.
- **§36.5 (v) and §37's FOR OTHER FILES 1 ("REVIEW_BFT_A_S8's closing request is already answered") are WRONG.** That
  review asked for a *bound* — "**That bound** is the single highest-value missing object in lane A" (l.574-575).
  Proposition NCR is an exact *identity* whose two factors are both OPEN. An identity is not a bound.
- **The two FAILED checks were handled correctly.** bb9's diagnosis is real (I verified the diff and re-derived the
  correct gradient from the criteria file's own energy, so the fix is forced by the pre-registration, not fitted to the
  outcome); bb9b changes exactly one expression plus header/label lines. bb10c's C4(b) FAIL touches no lemma, and C4(a)
  really is the inequality Proposition COF-size uses. **But** the control that failed is the one §34.5 **pre-stated**
  at 13:07:28 ("the regrouping is load-bearing"), first weakened to vacuity by the criteria amendment and then refuted at
  k = 3: **no check supports the size claim.** §37.4 (2) says this; §37.2's table does not (S10-22).
- **Discriminating power (Part P, added at the lead's request).** Of bb9b's 15 verdicts, **5 had unforced outcomes and 4
  are tautological or forced**: **A3 is the literal transpose of the script's own definition `Q = Qstr − dfun∘h`** and so
  cannot falsify Lemma RT-cc (b); **B0 has near-zero power** (every operator built from r_l is annihilated by Ξ — proved
  empirically by bb9, where B0 PASSED on the buggy energy); B4's "ψ_1 = 0" is forced by the one-site level-2 torus. Of
  bb10's 11 verdicts, **3 had unforced outcomes**, and **A4 — the criteria file's "central test", whose FAIL was to
  "refute Lemma DF-cc (ii) and therefore the session-10 proof of Theorem COF" — cannot fail if A3 passes**. bb10c's
  C4/C5 are the only gates in session 10 with both power and a non-vacuous hypothesis, and C4 (b) failed. **The funnel's
  role inside the ρ-recursion is exercised numerically nowhere in either session**, and no check in either session can
  reach my Part J refutation (the rows are absent from the model, and a factor k−1 is 1 or 2 at k = 2, 3).
- **On the nonabelian lens: I do not hold session 11's vacuity finding against bb9b/bb10.** Sessions 9-10 are at the
  trivial background, where Setting LIN's chain maps *are* the abelian ones, so the model is scope-matched — unlike
  session 11's §41 statements, which are about nonabelian structure. But **(CC-0) at critical points rests entirely on
  Lemma CD (i), a nonabelian identity quoted from lane A that no lane-B check touches**, and all of §36 is outside the
  model by the session's own limitation 6.
- **The nine [RBB8-fix] errata: all nine entered, with the content asked for. The GE-T → ΓT-op rename is COMPLETE**: every
  surviving "GE-T" in §28-§37 is either inside RS8-3/RS8-8 (quoting the old name in order to retire it) or refers
  explicitly to lane A's refuted (GE-T). No occurrence now misreads.
- **Downstream exposure.** SESSION24_RESULTS.md l.870-872 and HANDOFF.md l.84-85 have **already banked** the k,T-uniform
  form of Theorem NCE (i) and "off the critical set the entire remaining obstruction is the compensation charge". Both
  need the Part J correction before any further session builds on them.

---

# PART A: provenance

## S9-P1 Append-only and byte accounting: **CONFIRMED (exact)**
- `sed -n '1,3569p' BFT_B.md | wc -c` = **409782**, byte-for-byte the session-8 final size the log claims (l.429, l.442).
  §1-§26 are untouched.
- §27 block (l.3570-3640) = 14776 B against the claimed 14775 (l.435): a one-newline append-boundary difference.
- §28 block (l.3641-3654) = **5458 B = 5259 + 119 + 80**, matching the claimed append (5259, l.438) plus both disclosed
  in-place header corrections (429816→429935 = +119 at 12:28:19; and the second wording correction, +80). I did not expect
  to be able to confirm two in-place edits to the byte from the final file; I can, and they are as described.
- l.1-3945 = 482876 against the claimed session-9 final 482875 (l.465): the same one newline.
- Session 10's chain 482875 + 13525 = 496400 (l.509-510) → 520502 → 535218 → 551268 → **555646**, and 555646 is what the
  file contained at the end of session 10. Internally consistent and consistent with the filesystem.

## S9-P2 Criteria before script: **CONFIRMED to the second**
bb9_criteria.md birth **12:31:25** (exactly the claimed time, l.446), bb9_rtcc.py birth 12:35:37 (exactly l.448),
bb9.out 12:35:52. The A7 amendment is a genuine **append**: birth 12:31:25 ≠ mod 12:34:06. Birth times are usable here for
files created after 12:03:19, contrary to the log's note at l.428-429 (which is correct only for pre-existing files).

## S9-P3 bb9_criteria.md's no-session-constant disclaimer: **WRONG as written; CONFIRMED-WITH-FIX in substance**
The file says (bb9_criteria.md l.4-5) "No threshold below uses any constant derived in session 9". The thresholds of A4 (b)
("max over entries of |c(X, b)| ≤ 1") and A7 ("the reported ratio is ≤ 1 … the pre-stated bound ‖h_l^T‖_{ℓ^∞→ℓ^∞} ≤ 1 of
§27.2 Lemma FT (i)") **are** the constant of Lemma FT (i), and the file itself records that it was written "after §27
(PRE-STATED) **and §29**" — §29, which contains the proof of Lemma FT, was appended at 12:30:43, 42 s before the criteria
file. DRIVE_BRIEF rule 2's letter is breached.
*Why it does not matter substantively:* the same constant stands in §27.2 (l.3603) at 12:27:05, the first edit of the
session, before any derivation; and the pre-registration that counts (criteria before script) holds. **Fix:** the
disclaimer must read "every threshold is from §27.2, this session's PRE-STATED section; the proofs of §29 preceded this
file". This is the same class of breach the task warns about in three sister lanes, and lane B's is the mild form.

## S9-P4 The pre-registration value of §27 (and §34) is file order only: **NARROWED**
§27.2 pre-states **K_f = 2d/(1 − L^{−(2+α)}) = 8.74** and **c_w := 14** (l.3606, l.3608). Those are the output constants of
§29.3 and §29.5. §27's header concedes that unrecorded exploratory reasoning preceded the append and that "the only claim
§27 makes is file order", and the failure modes are explicitly marked "(considered before this append; no pre-registration
weight beyond the labels)". That is honest, and it is exactly the situation lane A's binding [RBA2-fix] P1 ruled on
(BFT_A l.802-807: "§7 carries the final constants of finished proofs … So §7 states results already derived").
**Apply the same standard:** no ledger may treat §27.2's or §34.2-34.3's constants and labels as pre-registered. §34 is in
the same position (it pre-states (CC-0), (NEUT-box), (Y-sup^loc) and six failure modes, five of which then "OCCUR as
expected").

## S10-P1 §34 as first edit: **CONFIRMED** (13:07:28, +13525 B; chain to 555646 verified in S9-P1).

## S10-P2 bb10_criteria.md's two-stage write: **NOT-VERIFIED**
§37.1 (l.4217) and the log (l.517-518) say the file was "born **13:09:13** UTC, with one amendment appended at
**13:12:09**". The filesystem says **birth = mod = 13:12:15**. bb9_criteria.md proves the tooling preserves birth time on
an append, so the most likely history is a *full rewrite* at 13:12:15, not an append — in which case the word "appended"
is wrong and **the pre-amendment text is not recoverable**, so the original pre-registration cannot be audited. What is
verified: the criteria file exists at 13:12:15 and bb10_cof.py at 13:14:02, so criteria-before-script holds with 1 m 47 s
to spare, and §34.5 (13:07:28, inside BFT_B.md) independently pre-states the plan. **Fix:** record the rewrite, or state
that the 13:09:13 figure is a self-report.
*This is not cosmetic*, because the amendment changed a FAIL condition (A6/A7's exponent) and added A8.

## S10-P3 bb10c is not labelled post-hoc: **CONFIRMED-WITH-FIX**
bb10c was designed after seeing bb10's A8 ratio = 1 (bb10c_criteria.md l.3-11 says so plainly). DRIVE_BRIEF rule 3: "Any
probe run after seeing the result is labelled post-hoc." Nowhere in §37.4, §37.2 or the log does the word appear — while
the same lane correctly applied the label to bb8n_defect three hours earlier ([RBB8-fix RS8-7] (ii), l.3651). The
disclosure is complete in substance; the label is missing. **Fix:** label bb10c post-hoc (it retains full weight as a
*refutation* attempt — a post-hoc check that FAILS against the session's own narrative is the strongest kind).

## S10-P4 Session-10 constructs used as criteria thresholds: **NARROWED**
bb10_criteria.md's A8 threshold `2d·L^{(d−1)}·π_1(j_1)` and bb10c_criteria.md's B^ψ/B^ξ are session-10 objects (B^ψ/B^ξ are
first written down in §37.4, l.4289-4290, *after* bb10c ran). Rule 2's letter again. Both were written before their
scripts and the FAIL was reported, so the purpose of the rule is served. Recorded, not held against the result.

---

# PART B: Lemma RT-cc (§29.1) — rebuilt from scratch

I derived (a)-(d) independently from root covariance, d*d* = 0 and the Euler-Lagrange equations, without reading the proof
first, then compared.

## S9-1 (a), the cascade and the forcing of d*ρ_l: **CONFIRMED**
- Apply d* to (E_0): d*d*dx_0 = 0, d*d*G_0 = 0, d*Q_0^Tρ_0 = ev^{(0→1)T}d*ρ_0 (the transpose of Q_ld = d ev, with
  d^T = d* in the §23.1 convention), so **ev^{(0→1)T}ψ_0 = d*j_0** ✓ (★0).
- Apply d* to (E_l): ψ_{l−1} = ev^{(l→l+1)T}ψ_l − d*j_l ✓ (★l). Applying ev^{(0→l)T} and using
  ev^{(0→l)T}∘ev^{(l→l+1)T} = ev^{(0→l+1)T} gives Ψ'_l = Ψ'_{l−1} + ev^{(0→l)T}d*j_l, and with Ψ'_0 = d*j_0 induction gives
  **ev^{(0→l+1)T}ψ_l = Ψ_l** ✓ (†). The induction is as written.
- **Injectivity, the point the task flags.** ev^{(0→l+1)T} places a level-(l+1) function on the level-0 sites of the
  level-(l+1) roots, which are **distinct**; so it is injective on the **entire** space of level-(l+1) functions, not on a
  subspace. The nesting that this needs (the level-0 site of a level-(l+1) root is the same whether it is read through
  level l or directly) is a property of the root convention, and the model's own root map
  z = L^l X + Σ_{t<l}L^t·(L−1)/2 (bb10_cof.py l.265-274) satisfies it exactly: level 1 → 3X+1, level 2 → 9X+4 = 3(3X+1)+1.
  Verified. **No restriction to a subspace anywhere.**
- **Equivalence, the second point the task flags.** The consistency condition the cascade imposes is "Ψ_l is supported on
  the level-(l+1) roots for every l". At l = k−1, Ψ_{k−1} = D(S), so the condition is "D(S) is supported on the level-k
  roots"; for l < k−1 it follows, since Ψ_l = D(S) − Σ_{l'>l}ev^{(0→l')T}d*j_{l'} and every subtracted term already sits on
  level-l' ⊆ level-(l+1) roots. Conversely, composite co-closedness is D(S) ⟂ Λ_0, i.e. *(i)* D(S) = 0 off the level-k
  roots and *(ii)* Σ_{roots}D(S) = 0. **(ii) is automatic**: Σ_z(ev^{(0→l)T}d*j_l)(z) = Σ_X(d*j_l)(X) = 0 on the level-l
  torus, for every l. So D(S) ⟂ Λ_0 ⟺ D(S) root-supported ⟺ the cascade is consistent: the **equivalence** holds, and the
  one-way-implication failure the task expected is not there. (§36.1 l.4147 uses the same Σ_zD(S) = 0 fact; it is correct.)
- §29.1's observation that the support claim follows **from the source alone**, with no reference to x, is right and is
  stronger than the statement of (a) — see S9-4.

## S9-2 (b), (c), (d): **CONFIRMED**
- (b): transposing Q_l = Q_{str,l} − d∘h_l gives Q_l^T = Q_{str,l}^T − h_l^Td*, so (E_l) becomes
  ρ_{l−1} = Q_{str,l}^Tρ_l − d*G_l − ĵ_l with ĵ_l = j_l + h_l^Tψ_l ✓. The level bookkeeping is right (h_l^T: level-(l+1)
  functions → level-l 1-forms).
- (c): the downward iteration and the composite identities Q_{str,0}^T(Q_str^{(1→l)})^T = (Q_str^{(0→l)})^T check ✓, and
  RHcc-F4's non-occurrence is exactly the observation that the substitution is made before iterating ✓.
- (d): d*J_0 = d*j_0 − ev^{(0→1)T}ψ_0 = 0 by (★0) ✓. The Hodge step: with x_0 = dφ + d*ω + c,
  J_0 = d*d d*ω = (d*d + dd*)(d*ω) = Δ_0(d*ω) since d*d* = 0 ✓; zero componentwise mean from
  ⟨d*dx_0, ce_μ⟩ = ⟨dx_0, d(ce_μ)⟩ = 0 ✓; so f_0 = n²dΔ_0^{−1}J_0 ✓. bb9b B5 confirms both halves exactly.

## S9-3 The *Reading* at l.3692 ("forced by root covariance and the injectivity of ev^T"): **CONFIRMED**
This is the load-bearing sentence of session 9 and it is accurate. I could not find a weaker reading of it.

## S9-4 A strengthening the file does not claim (reviewer, in the sessions' favour)
ψ_l is determined by the **source** alone — ev^{(0→l+1)T}ψ_l = Ψ_l, with Ψ_l built from d*j_{l'} only — and therefore
ψ_l exists and is computable with no reference to a critical point. This matters later: it is what makes Lemma DF-cc
legitimate (DF-cc uses ψ_i for a *source*, not for a solution), and bb10_cof.py's `psis` (l.339-348) computes ψ from the
source, so bb10's A3/A4/A5 are solve-independent. §29.1 states the fact (l.3674) but neither §35.3 nor §37 points out that
it is what removes the apparent circularity in DF-cc's use of ψ. Record it.

---

# PART C: Lemma FT (§29.2), Theorem RHT-cc (§29.3), Theorem RHT_m-cc (§29.5)

## S9-5 Lemma FT (i): **CONFIRMED (independently recomputed)**
Rebuilt from BL-2 (b)'s definition in d = 2, L = 3 (my `rev/indep.py`):
- every axial path from c_X to y ∈ B(X) stays inside B(X) (both endpoints in a product of intervals, path monotone in each
  coordinate), so c(X, b) = 0 unless both ends of b lie in B(X), and blocks are disjoint ⇒ **one block per link** ✓;
- **max|c(X, b)| = 1/3** (the direction-0 links adjacent to the centre at row c_1 carry 3/L^d = 1/3) — exactly bb9b A4's
  printed value, and ≤ 1 as Lemma FT (i) claims. The general bound |c| ≤ L^{−d}·L^d = 1 is immediate, and all paths through
  a given link cross it in the same direction (the link is on one side of c_X in that coordinate), so there is no sign
  cancellation inflating the count;
- **Σ_b|c(X, b)| = 4/3**, equal to the mean axial path length 4/3, against the stated bound d(L−1)/2 = 2 ✓.
So ‖h_l^T‖_{ℓ^∞→ℓ^∞} ≤ 1 and ‖h_l^T‖_{ℓ¹→ℓ¹} ≤ d(L−1) hold, with the centre-convention sharpening as noted at l.3700.
This is REVIEW item (2) of §33's request list, and it survives.

## S9-6 Lemma FT (ii)-(iv): **CONFIRMED**
(ii) sup|ψ_l| ≤ Σ_{l'≤l}sup|d*j_{l'}| ≤ 2dΣ_{l'≤l}sup_own|j_{l'}|, and multiplying by L^{3(k−l)} gives
π_l(h_l^Tψ_l) ≤ 2dΣ_{l'≤l}L^{−3(l−l')}π_{l'}(j_{l'}) ✓ — a geometric convolution over levels **at or below** l, with no
power of L^{k−l}, so RHcc-F2 indeed does not occur. The "raw lattice values" claim (ev^T carries no rescaling) is tested
exactly by bb9b B2. (iii) is the same algebra in the class ✓. (iv): the funnel reads ψ within one coarse unit and d* within
one more, so e^{2m} ✓.

## S9-7 Theorem RHT-cc and K_f: **CONFIRMED**
The index swap (l.3719-3721) is correct: with l = l' + u,
L^{−(1−α)(k−l)}L^{−3(l−l')} = L^{−(1−α)(k−l')}L^{−(2+α)u}, so Σ_{u≥0} = (1 − L^{−(2+α)})^{−1} and
K_f = 2d/(1 − L^{−(2+α)}). I get **8.7376898…**, i.e. the quoted 8.737 ✓. Truncating the inner sum at l = k−1 and bounding
by the full geometric series is legitimate ✓. The left-hand sum correctly starts at l = 1 (h_0^Tψ_0 never enters r_i, only
J_0) while the right-hand sum starts at l' = 0 — which is RHcc-F3, and the file reports it as OCCURRING with the
exponentially small weight L^{−(1−α)k} ✓.

## S9-8 Theorem RHT_m-cc, c_w = 14: **CONFIRMED-WITH-FIX (conservative, so the bound stands)**
§19.6's constants are e^{10m} for the top and plain terms, e^{12m} for the G-terms (BFT_B l.2646-2655, with the
post-proof correction c_w = 12). The funnel is a **plain** level-l source and ψ_l depends on no G-slot (d*d*G = 0), so its
extra e^{2m} lands on the plain slot: 10 + 2 = 12, and the G-slot stays at 12. So **c_w = 12 suffices**; §29.5 adds the
funnel's e^{2m} to the G-slot's 12 instead and gets 14. Over-stating a crude exponential constant upward weakens the
statement, so nothing is wrong — but the arithmetic as written attributes the cost to the wrong slot. Marked "[crude]" ✓.

---

# PART D: Corollary RHT-V (§29.4) — the three uniformities and the universal quantifier

## S9-9 V is composite-co-closed at critical points: **CONFIRMED**
Each d*W_l is level-wise co-closed, hence D(d*W) = 0 (d*d* = 0; equivalently dd = 0 on the gauge direction); so
Ξ^TV = Ξ^T𝔑^0 = 0 at a critical point by Lemma CD (i) ✓. Lemma SPLIT (§35.2) makes the same point more cleanly in session
10. Nothing hidden.

## S9-10 "for every gauge fixing Γ": **CONFIRMED — this one is solid**
r_l(x + Ξλ) = Q_l(x_l + d ev^{(0→l)}λ) − (x_{l+1} + d ev^{(0→l+1)}λ) and Q_ld ev^{(0→l)} = d ev^{(l→l+1)}ev^{(0→l)} =
d ev^{(0→l+1)} by root covariance and the composition of evaluations, so the two added terms cancel **exactly**: every r_l,
hence N_res, is exactly composite-gauge invariant ✓. Then Lemma FG (iii) makes x_Γ = 𝓛_Γ^{−1}S a critical point of E_src
for every Γ, so Theorem RHT-cc applies to it with the same constant ✓. The universal quantifier over gauge fixings is
earned, and it costs nothing: it is Lemma FG (iii) plus one exact identity. I tried to break it through the Γ-dependence of
the *representative* and could not: N_res is built from r_l only.

## S9-11 C_V's ingredients and the three uniformities: **CONFIRMED-WITH-FIX**
Three separate points.
1. **The hidden hypothesis (binding).** The displayed bound (l.3738-3739) carries κ̂‖r^c_{k−1}‖_∞ on the right, and the
   parenthetical disposes of it with "using ‖r^c_{k−1}‖_∞ ≤ ‖x‖_inv ≤ G_Rη² or Corollary LIN0's bound for the top term".
   Corollary LIN0 covers (R), (G), (P0) and **level-wise co-closed** plain currents (BFT_A l.2242-2245) — the V_l are
   precisely not that, so the only available route is ‖x‖_inv ≤ G_Rη², i.e. **(H-inv) for the same non-co-closed rows**,
   whose curvature half is the open item. This is inherent to what (Res-Hölder) *is* (Corollary RH-inv, §19.4: it converts
   (H-inv) into (H-inv+)), so it is not an error — but then the headline must be the increment, not "N_res ≤ C_Vη²". The
   §33.2 table row and the FOR OTHER FILES entry to lane A do not say it.
2. **C_NC's provenance.** §29.4 re-derives C_NC := 8dN_Rq_R(q_R+1)^d. I checked the arithmetic — N_R·4q_R·2d(q_R+1)^d —
   and it is right, and it differs from lane A's own C_NC(q_R, N_R) := 48N_R(2q+1)⁴q⁵(1+8q) (BFT_A l.2570), which is fine
   (re-derivation is the house rule). But it is stated in terms of sup_own|R^B_l|, whereas lane A's own precision note says
   "Proposition NC's size bound is in terms of σ := max_c sup|R_c| (the bound available for the rows), **not** sup|R|"
   (BFT_A l.2394). Cite σ.
3. **"Crude" does not hide a divergence.** q_R, N_R are the BCH₂ piece side and overlap, O(1) in own units and
   independent of k, l and T; BFT_A l.3385-3386 records Proposition NC and Corollary NC for every T ≥ 1 with C_NC itself.
   I looked for a k- or T-dependence in C_V's list (L, d, κ_±, α, θ, q_R, N_R, C_bch) and found none. The k-uniformity of
   the **residual** half is real, and it comes from the transport weight Σ_lL^{−(1−α)(k−l)} ≤ (1−L^{−(1−α)})^{−1} beating
   the level count — I checked that the uniform-in-l row size is enough for this. **Three uniformities: earned, for the
   residual half.**

---

# PART E: Proposition CO-use (§30) and the (H-inv+) claim

## S9-12 Proposition CO-use: **CONFIRMED as bookkeeping**
I spot-checked every load-bearing quotation at the cited line: Theorem YH and Theorem W0 CONFIRMED and Theorem GU
CONFIRMED (REVIEW_BFT_A_S6 l.23-24, l.181); Corollary LIN0 "CONFIRMED in its stated scope" (l.24, l.198); Proposition NC
CONFIRMED and Corollary NC CONFIRMED-WITH-FIX (l.26); CO-0R/CO-upR/CO-B CONFIRMED (REVIEW_BFT_A_S5 l.30) and **"CO-B
removes 13.7's (SB) gap outright"** (l.373, verbatim); DX_m/DB_m and the weighted sups of GU, CO-0R, CO-B still OPEN
(REVIEW_BFT_A_S7 l.320). The ruling that REVIEW_BFT_A_S4's "(CO-up) ARGUED, fix T6" and REVIEW_BFT_B_S5's "(CO-0),
(CO-up) OPEN" are **stale** is correct: both predate Theorems W0/GU. Nothing is re-judged, as promised. The "What is NOT
claimed" paragraph (l.3773) is the right paragraph to have written.

## S9-13 "(H-inv+) at m = 0 … PROVEN as an implication": **CONFIRMED-WITH-FIX (class caveat)**
The implication chain is sound (W0 + GU + CO-0R/CO-upR/G♯R + LIN0 + Corollary RH-inv + Theorem RHT). Two qualifications
the entry omits:
- It is for **level-wise co-closed** Setting-LIN classes, and BFT_A's own binding erratum says of that class: "BL-7 is a
  correct linear statement for a source class **the remainders do not occupy**" ([RBA2-fix] B3, l.820-821). §33.3's "at
  m = 0 and the trivial background that whole bundle is closed" (l.3922) must carry that sentence. (§33.3's list of what
  remains does include "the off-critical-set curvature half", so session 9 is not hiding it; but the headline reads wider
  than the class.)
- Corollary LIN0 is PROVEN in lane A "given the reviewed package and **§23 (unreviewed)**" (BFT_A l.2683). "Every one of
  its inputs is CONFIRMED by a lane review" is therefore one step strong.

---

# PART F: Proposition NCR (§31.1), (NC-Γ)_cc (§31.2), the remainder (§31.3)

## S9-14 Proposition NCR: **CONFIRMED**
f_0^Γ(S)(p) = ⟨S, Y^p_Γ⟩ (Lemma FG (ii)) and Y^p_Γ = Y^p_* + Ξλ with λ unique in Λ_0/const because ΓΞ is a bijection of
Λ_0/const onto Ran Γ; then ⟨S, Ξλ⟩ = ⟨Ξ^TS, λ⟩ = ⟨D(S), λ⟩ ✓. One line, and it is right. It is a genuinely useful
identity: it quarantines the whole slice dependence in a bilinear term with one source factor and one slice factor.

## S9-15 The missing n² (binding, and **not** harmless where §35.1 says it is)
§35.1's convention note (l.4011) spots that §27.4/§31.1's displays of NCR omit the n² of BFT_A §26.0's coarse convention,
and judges that "the omission changes nothing in either statement (every term of NCR carries the same factor)". That is
true of NCR itself. It is **false of §31.3 (R2)**, which is an inequality, not an identity: with n² restored,
|remainder| ≤ **n²**‖D(S)‖_1·sup|λ|, and n² = L^{2k}. So the advertised implication
"**(NC-Γ)_cc + (GT-sup) ⟹ (NC-Γ) for Γ_E**" (l.3816, l.3821, and §27.4's "Expected relation", l.3621) requires a **third**
input that neither antecedent supplies: a k-uniform bound on n²‖D^⊥(S)‖_1. And by §36.3's own attribution that is exactly
the factor where the k-growth lives. Session 9 saw the issue informally ("multiplied by the (possibly k-growing)
λ … what route (i) needs is only that the product stays bounded", l.3818) and then stated the implication without it;
session 10 does not add it to the named open set, and the PROOF.md export (l.4283) repeats the two-factor framing.
**Fix:** enter the n² as an erratum to §27.4, §31.1 and §31.3 (and ask lane A about BFT_A §26.2's display of Lemma FG (ii)),
and state the third input.

## S9-16 §31.1 *Reading* 2's identification of λ's "level-k-root part": **WRONG**
l.3787 says "its root values are lane A's σ … and **its level-k-root part is TE's tent data**". Session 10's own §36.1
proves that **λ^{Γ_E}_*(p) vanishes at every level-k root** (l.4147), and I verified the proof: χ^5_X(c_X) = σ_5(0)^d = 1
and Σ_Xχ^5_X = 1 with χ^5 ≥ 0 force χ^5_{X'}(c_X) = 0 for X' ≠ X, so Λ(x)(c_Y) = λ^E_Y(x)(c_Y) = 0 by the pin. So λ has
no level-k-root part at all. §35.7 then shows the tent data is Φ_k(Y^p_{*,0})(c_X), the **response's funnel**, paired with
D^root — a different object in a different pairing. The §31.1 sentence is superseded and **no erratum covers it**:
[S10-fix 1] is about §31.2's quantifier and [S10-fix 2] about §31.3's expectation.
Also in the same sentence: lane A's σ is defined as the transport from **S_E to the hard slice S^♯**
(f^♯_0 − f^E_0 = n²⟨D(S), σ(Π_EY^p)⟩, BFT_A l.3546-3547), not from a representative to S_E. Identifying it with
λ^{Γ_E}_{C0#}(p) needs C0# to be the S^♯ representative and fixes a sign; that identification is asserted in both
sessions and verified in neither. It is load-bearing for §36.3 (see S10-15).

## S9-17 §31.2 (a), the residual half: **CONFIRMED (k-, T-, level-uniform)**
I checked the step the display glosses. Collecting L^m·L^{−2m}·Σ_{l>i}π_l(ĵ_l) = L^{−m}Σ_{l>i}π_l(ĵ_l) with m = k−1−i and
m summands: even with **no** per-level decay, max_m mL^{−m} = 1/L, so the collected form's
"(1 + K_f)max_lπ_l(j_l)(1 − L^{−1})^{−1}" is a valid (indeed generous) bound. So the residual half of (NC-Γ)_cc is
k-uniform for the rows, which is what matters downstream. **This is the half that survives Part J**, and the contrast with
the curvature half is instructive: the residual slot has an L^{−m} transport factor; the level-0 image has none.

---

# PART G: BFT-5 (§32)

## S9-18 (BFT-5_E) clause (c) "PROVEN (Proposition NCR)": **WRONG at the stated scope**
§32.1 states (BFT-5_E) at the background **Z(V_k)** for V_k ∈ 𝒦(ε_5), and clause (c) asserts that the slice-dependent
remainder "is given **exactly** by Proposition NCR" (l.3832); §32.2 and §33.2 then record clause (c) as **PROVEN**
(l.3839, l.3851, l.3913). Proposition NCR is proven at the **trivial** background: its proof is Lemma FG (ii) plus
"ΓΞ is a bijection", and Lemma FG is BFT_A §26.2's lemma about the Setting-LIN Hessian H with Ker H = Ran Ξ. At Z(V_k) the
corresponding statement (Ker H_E = Ran Ξ, and H_EΞ = 0) is part of clause (a)'s invertibility and of the
background-covariant slice (N1), which §33.3 item 1 lists as the **first** remaining obstruction. **So clause (c) is
CONDITIONAL on the background-covariant analogue of Lemma FG (i)-(ii), not PROVEN.** §36.5 (iv) says "every lane-A input
used is at the trivial background" — that sentence contradicts §32's clause-(c) status, not §36.
Also minor: clause (b) includes "BFT-3's weighted locality at rate ≥ m_Y" while clause (d) says the weighted form "is not
claimed at the same status". Pick one.

## S9-19 Proposition BFT5-red's (G♯-patch^Ω) narrowing: **NARROWED (ARGUED, not "PROVEN as bookkeeping")**
§32.2's new content is "Corollary CL-iv supplies [G-pert's smallness] on every frame, k- and T-uniformly … **No step of
the gluing has to produce the smallness: CL-iv has produced it**" (l.3845-3847). Against SF.md:
1. G-pert's hypothesis is **t := ‖x^r‖_X + ‖B^r‖_D ≤ min{ρ_0, 1/(4GC_R), 1/(4G_wC_{R,w})}** (SF l.699-700). CL-iv
   bounds sup_j‖log Z^off_j‖_{C^{1,α}} ≤ C_1ε — at most the *chain* half, in a norm not shown to dominate ‖·‖_{X_c}.
   **Nothing in §32.2 supplies ‖B^r‖_D in the frame gauge**, and [RSF2-fix GP-2] says precisely that this clause means
   "the data are small in ONE global gauge: exactly B-NA-red's class" and that G-pert "reaches no background that
   B-NA-red does not already handle" (SF l.895-896). §32.2 quotes that scope note in item 3 and then claims past it.
2. [RSF2-fix GP-1] (SF l.890-894): G-pert bounds the Hessian **in the trivial slice at x^r**, not in a covariant slice,
   and bridging the two needs "a slice-change lemma … **not proven**". (G♯-patch^Ω) asks to "glue the frame-local inverses
   supplied by Lemma G-pert … into a global inverse in the §33 pair" — the objects being glued are inverses of a different
   gauge-fixed operator from the H_E that (BFT-5_E) is about. The slice change is an unnamed step inside the narrowing.
So the narrowing is real as a *relocation* of the difficulty (and it is the right relocation), but "PROVEN as bookkeeping"
over-states it: the reduction (BFT-5_E) (a),(b) ⇐ (1)+(2)+(3)+(4) is incomplete at step 3.

## S9-20 Lemma Rω-frame: **CONFIRMED as ARGUED**
The status is honest and correctly refuses CONDITIONAL ("a CONDITIONAL would require the constants of (i) to be written",
l.3862). The content claimed — that the frame rewriting is not a *new* wall — is the right modest claim. No new objection.

---

# PART H: checks bb9 and bb9b

## S9-21 The bb9 B3/B4 FAIL and its diagnosis: **CONFIRMED (the diagnosis is real)**
`diff bb9_rtcc.py bb9b_rtcc.py` is: a 7-line header, 5 print-label strings, and **one expression**, l.339→346:
`g1 = [-KAP[0]*a + KAP[1]*b for a,b in zip(r0, mapply(mt(Q1), mapply(mt(Q1), r1, n1L), n1L))]`
→ `… zip(r0, mapply(mt(Q1), r1, n1L))`. Exactly as claimed, and nothing else.
The diagnosis is correct and independently checkable: the criteria file pre-registers the energy
E_src = ½|dx_0|² + Σ(κ_l/2)|r_l|² − … (bb9_criteria.md l.16-17), whose x_1-gradient is unambiguously
**−κ_0r_0 + κ_1Q_1^Tr_1**. So the fix is **forced by the pre-registration**, not fitted to the outcome — which is the
question that matters, and the answer is clean. (The buggy form is also silently ill-typed: at T = 1, `mt(Q1)` expects a
level-2 vector of length 2 and is handed the 18-vector Q_1^Tr_1, so the sparse `mapply` reads only its first two entries.)
bb9.out's own printout corroborates the story: B0 PASSES on the buggy operator (it is built from the same `Hop`), B3 fails,
and B4 reports "ψ_1 = 0; identity without the funnel holds = **False**" — the exact inconsistency the wrong energy
produces.

## S9-22 bb9b tests the same thing bb9 was meant to test: **CONFIRMED**
Same criteria file, unretuned (birth 12:31:25, mod 12:34:06, both before bb9_rtcc.py at 12:35:37, and untouched since);
no test added after an outcome; the script differs by the one expression above. The failure mode the task warns about — a
re-run that quietly tests something easier — **did not happen**.

## S9-23 But two tests are weaker than the record reads: **NARROWED**
- **B0 cannot detect an assembly bug**, since it verifies Hx = S with the same `Hop` that built the system. The only guard
  was B3, a test of the lemma. §33.1 says this ("B0 passed on the wrong functional", l.3872) — good — but the lesson for
  the next check is that the Hessian needs an independent construction (e.g. a finite-difference or second-derivative
  cross-check of E_src), not that B0 is a criticality test.
- At T = 1 the level-2 lattice has one site, so **ψ_1 ≡ 0 identically**, hence Q_1^Tρ_1 = Q_{str,1}^Tρ_1 and
  **B3 does not test the straightening at all** — it tests the level-1 Euler-Lagrange equation. bb9_criteria.md l.58-59's
  "it does not make B3 vacuous (B3 still tests the straightening Q_1^T → Q_{str,1}^T at the critical point)" is **void**.
  §33.1's scope limitation (4) (l.3894) is honest about the substance, and A3 + A7 at T = 2 do carry the operator identity
  with a nonzero funnel, so the coverage is adequate overall. The criteria file's sentence should be withdrawn.

---

# PART I: session 10's structural work (§35.1-§35.4)

## S10-1 Lemma W0-use: **CONFIRMED (checked against BFT_A l.2465-2494, line by line)**
- Step 1 (l.2467): Lemma DUAL + symmetry, **no co-closedness** ✓.
- Step 2 (l.2469): "for every λ" is the use, and it is what licenses 𝒩(Y^p) ≤ C_YNn in place of ‖Y^p_0‖_1 ✓. Use (A) ✓,
  and the characterisation "it is a condition on the **total** object paired with Y^p_0, not on a sum of co-closed pieces"
  is correct and is the whole idea of §35.
- Step 3 (l.2472-2478): co-closedness enters through **r_{k−1}**, used to straighten Q^T → Q_str^T ✓. And — a point
  §35.1 asserts and I verified — in W0's own setting that *is* a use of d*j_0 = 0: by Lemma RT-cc (a),
  ψ_{k−1} = R_k(Ψ_{k−1}) = R_k(d*j_0) = 0 when d*j_0 = 0. So the "exactly two uses" headline survives, and
  **(CC-0) ⟺ ψ_{k−1} = 0 ⟺ r_{k−1} co-closed** is the exact generalisation of W0's hypothesis. That is a real insight and
  it is the best argument in either session that (CC-0) is the right hypothesis rather than a convenient one.
- Step 4 (l.2479-2490): the plain slot enters only through sup|h| in LES-div's n^{1−α}sup|h| ✓, so any sup-bounded
  enlargement is admissible ✓. Step 5 (l.2491): no co-closedness ✓.
Review request (2) of §37 is answered affirmatively: LES-div and Lemma LE ask nothing of the plain slot but its sup.

## S10-2 Lemma SPLIT: **CONFIRMED**, including review request (3)
D(S^G) = 0 by d*d*G = 0 (equivalently dd = 0 on Ξλ); D(S^s) = 0 because r_i(Ξλ) = 0 exactly (S9-10) so the residual slot's
linear functional annihilates every gauge direction; D(S^j) = D(S) by linearity ✓. And the specific worry §37 asks about —
does Corollary LIN0 cover an s-only source with no plain currents? — **yes**: j = 0 is level-wise co-closed, so LIN0's
hypothesis is satisfied vacuously, not violated (BFT_A l.2242-2245). The correction of §31.2's "Corollary LIN0's
superposition does not apply" is right: the pieces being superposed are source slots, each composite-co-closed.

## S10-3 Lemma DF-cc (i)-(iii): **CONFIRMED** (this is §37's review request (1))
- (i) d*(Q^{(0→l)})^T = ev^{(0→l)T}d* iterated, so d*C(j) = Σ_lev^{(0→l)T}d*j_l = D(S) ✓, and C(j) co-closed ⟺ (CC-0) ✓.
- (ii) The double-sum exchange is correct (the pair set {(i, l) : i < l} read either way), the injectivity step is the one
  I verified in S9-1, and the i = k−1 bookkeeping — which looked wrong at first reading — is right: the term
  h_{k−1}^Tψ_{k−1} added to make the ĵ-sum uniform over l is cancelled exactly by the i = k−1 defect term
  −(Q_str^{(0→k−1)})^Th_{k−1}^TR_k(D), because ψ_{k−1} = R_k(D(S)) by (†) at l = k−1. Under (CC-0) both vanish ✓.
- (iii) same algebra with the shifted base level ✓, and it is what Theorem COF (c)'s residual term uses.
bb10 A2/A3/A4 and bb10c C2/C3 test this exactly, and C5 shows the hypothesis is load-bearing at k = 3.

## S10-4 "ξ_i = −ψ_i exactly, at every k and every i" under (CC-0): **CONFIRMED — and session 10's self-correction is right**
§37.4 (l.4288-4291) withdraws §37.1's limitation 2 ("the size gain is a k ≥ 3 phenomenon") and says the two groupings are
the **same vector** at every k, differing only in the available bound. That is correct: ev^{(0→i+1)T}(ξ_i + ψ_i) = D(S) = 0
plus injectivity gives ξ_i = −ψ_i identically. So "the regrouping" is the substitution of the ψ-expression for the
ξ-expression of one vector, and the content of §35.3-§35.4 is entirely that the ψ-expression admits the k-uniform bound
B^ψ. The session identified and corrected its own over-reading within three minutes of writing it, before building a check
on it. That is the best process behaviour in either session, and the bb10c criteria file records the reasoning before the
check ran.

## S10-5 Proposition COF-size: **CONFIRMED as an inequality in the (Pl-c) class**
Step 1's coarse-unit contraction is right: |Q_str^Tv| ≤ L·L^{−d}sup|v| = L^{−(d−1)}sup|v| per step (BL-2 (c), and
REVIEW_BFT_A_S8 S8-4 l.151 confirms the d = 4 form), so π_0((Q_str^{(0→l)})^Tv) ≤ π_l(v) — the push-down is a contraction
in coarse units with **factor exactly 1 per level, no gain**. Step 2 is Lemma FT (iii) ✓. Step 3's C_C is loosely grouped
but valid: the derivation gives (1+2d(1−L^{−3})^{−1})[(1−L^{−θ})^{−1}‖j‖_Pc + (1−L^{−3})^{−1}‖j^c_0‖_∞] and the stated
C_C = (1+2d(1−L^{−3})^{−1})(1+(1−L^{−θ})^{−1}) dominates it, since (1−L^{−3})^{−1} = 27/26 ≤ 1 + (1−L^{−θ})^{−1}; the
quoted 9.31 = 1 + 8·27/26 ✓. **k- and T-uniform in the class, as claimed.**

---

# PART J: Theorem COF and Corollary COF-crit — the level-count loss

## S10-6 **Corollary COF-crit (§35.6) is WRONG as stated.** Theorem COF is CONFIRMED; its application to the rows is not.

Theorem COF (§35.5, l.4076-4077) is correct and I could not break it. Its right-hand side contains **‖j‖_Pc**, and its
class hypothesis is π_l(j_l) ≤ L^{−θ(k−l)}‖j‖_Pc, i.e. ‖j‖_Pc = max_lω_lπ_l(j_l) with ω_l = L^{θ(k−l)} (BFT_A l.470;
BFT_B l.2629).

Corollary COF-crit substitutes "Corollary NC's slot sizes (ω_l‖W^c_l‖_∞ ≤ CL^{−(1−θ)(k−l)}η², **π_l(V_l) ≤
2C_NCC_bchκ_+L²η²**, §29.4)" (l.4109-4110) and concludes ‖f_0‖_∞ + [f_0]^∞_α ≤ C_funC'η² "k-, T- and Γ-uniformly".
The W-sizes are quoted **with** their ω_l weight, so ‖W‖_Y ≤ Cη² ✓. The V-sizes are quoted **without** one, and §29.4
(l.3729 item (3), l.3735) and BFT_B §19.4 (l.2629) both say explicitly that they are **"uniform in l"** — no level decay.
Converting to the norm Theorem COF actually uses:

  **‖V‖_Pc = max_{1≤l≤k−1}L^{θ(k−l)}π_l(V_l) ≍ L^{θ(k−1)}·2C_NCC_bchκ_+L²η².**

So the conclusion that follows from the quoted inputs is ‖f_0‖_∞ + [f_0]_α ≲ C_fun·L^{θ(k−1)}η², **not** k-uniform.
Taking instead the sharper route inside the proof (Proposition COF-size step 3, π_0(C(j)) ≤ Σ_lπ_l(ĵ_l), bypassing the
class norm) gives ≈ 9.31·(k−1)·2C_NCC_bchκ_+L²η² — linear in k. And optimising θ: minimising
C_C·L^{θ(k−1)} ≈ 9.31·L^{θ(k−1)}/(θ ln L) over θ gives θ* = 1/((k−1)ln L) and value **9.31·e·(k−1) ≈ 25(k−1)**. There is
no choice of θ in (α, 1) that removes the factor.

**Three independent corroborations that this is the real thing and not a bookkeeping quibble.**
1. BFT_A's own binding erratum **[RBA2-fix] B3** (l.819-824): "The F3 remainder rows … are O(η²) per level in plain
   coarse units **with no level decay**, so ‖rows‖_{Pc} ≍ L^{θ(k−1)}η² (upper bound), and **(Pl-c) does not contain
   them** … while the level-0 images add up to Σ_l‖j^c_l‖ ≤ (k−1)η²: **the entire level-count loss sits in the level-0
   image**." Theorem COF's binding term is, by its own admission (l.4096), "the co-closed level-0 pairing" — i.e. that
   level-0 image.
2. **REVIEW_BFT_A_S8 S8-13** (l.366-369), CONFIRMED there: "without (PW-ii) the interpolation term loses the s-gain, the
   level sum stops being geometric, and **the factor k returns**." The mechanism named is the mechanism here.
3. **§36.5 (iv) itself** (l.4209): "The factor k in (NC-Γ) and (PW-ii) are untouched (REVIEW_BFT_A_S8 S8-12, S8-13
   stand)." §36.5 (i) claims constants independent of k for the same object. The two paragraphs are two pages apart and
   contradict each other.

What the fix needs: a **level-decay** input for the non-co-closed plain rows — lane A's **(SPD)/(W2)** ("the Ran Q^T
component of a remainder row at level l, carried up to level m, has plain coarse size ≲ L^{−(m−l)}η²", BFT_A l.830-831,
**OPEN**) or (G♯-rough) for the rough part of the split. Nothing in session 9 or 10 supplies it, and the funnel only adds
to each π_l(ĵ_l).

**Honest status for Corollary COF-crit:** PROVEN as an implication with a constant that grows like k (≈ 25(k−1) at the
optimal θ), and **CONDITIONAL on (SPD)** for the k-uniform form. Theorem COF, Lemma DF-cc, Lemma SPLIT, Lemma W0-use and
Proposition COF-size are all untouched by this: the error is one substitution.

## S10-7 Theorem NCE (i): **NARROWED**
"(NC-Γ) for Γ_E holds at every critical point of 𝔉_k, at m = 0, at the trivial background, for every gauge fixing,
**with constants independent of k and T**" (l.4199) is not established. The residual half is k-uniform (S9-17, S9-11) and
the Γ-uniformity is exact (S9-10); the **curvature half carries the factor k** by S10-6. The correct headline is: at
critical points, the residual half of (NC-Γ) for Γ_E is PROVEN k-, T-, Γ-uniformly, and the curvature half is PROVEN with
a constant O(k), k-uniform only given (SPD).

## S10-8 Content of "at every critical point of 𝔉_k", and the circularity question: **no circularity, but weaker than it reads**
The task asks whether Theorem NCE assumes what BFT-0 is supposed to establish. It does not:
- **Theorem COF is a statement about sources**, quantified over Setting LIN^cc sources satisfying (CC-0). It is
  non-vacuous without any critical point of 𝔉_k existing: every level-wise co-closed source, every pure-G source and
  every pure-s source satisfies (CC-0) (Lemma SPLIT). Its proof never assumes existence or uniqueness in the ball.
- Likewise **Theorem RHT-cc** is quantified over critical points of **E_src** — the *linear* energy — which exist for
  every composite-co-closed source by Lemma FG (i). That is not a hypothesis about 𝔉_k at all. (Session 9 is careful
  about this distinction; the PROOF.md export at l.3939 is not — see the binding fixes.)
- What **is** weaker than it reads: "for every x with ∇(𝔉_k∘exp)(x) = 0 and ‖x‖_𝔐 ≤ η, [bounds]" is an **a-posteriori
  regularity statement** about a fixed point. A Newton/contraction argument that constructs the fixed point needs the
  linear estimate at **non-critical iterates**, and lane A's (NC-Γ) was explicitly a ball statement ("for all
  configurations of the ball", l.3777). So Theorem NCE (i) cannot by itself feed BFT-0's construction; it can serve a
  bootstrap/regularity role once a fixed point is known to exist. The sessions mostly say this (§29.4's caveat (1),
  §31.2's "this is the statement the contraction needs **at its fixed point**", §37.3 items 1-2), and §36.5 (ii) prices
  the off-critical case. One sentence over-reaches: §36.5 (i)'s "it is the scope lead decision D1 asked for" — D1 asked
  for "composite-co-closed sources **plus a remainder bound**", and no remainder bound exists (S10-18).

---

# PART K: Proposition COF-res, (CO-fun)'s falsity, Remark MASSLESS

## S10-9 Proposition COF-res, the identity: **CONFIRMED**
⟨Σ_i(Q_str^{(0→i)})^Th_i^TR_{i+1}(D), Y^p_0⟩ = Σ_i⟨R_{i+1}(D), h_iQ_str^{(0→i)}Y^p_0⟩, and since R_{i+1}(D) sits on the
level-k roots **as level-(i+1) sites**, pairing reads ev^{(i+1→k)} of the level-(i+1) function (this is §37's review
request (5), and it is right — the support claim is exactly the nesting of S9-1). Then
Σ_{i<k}ev^{(i+1→k)}h_iQ_str^{(0→i)} = h^{(0→k)} = Φ_k by Proposition RF ✓. So the residue is
n²Σ_XD(S)(c_X)Φ_k(Y^p_{*,0})(c_X) ✓ = Proposition TE's tent coefficient.

## S10-10 "with every other term bounded as in Theorem COF": **NOT-VERIFIED**
COF-res's framing (l.4114) and §36.5 (ii)'s "Theorem COF applies to S^E_0(S) **except** for Proposition COF-res's
residue" (l.4203) both need the main object Σ_l(Q_str^{(0→l)})^Tĵ_l to admit Theorem COF's step (c) when D(S) ≠ 0. Step (c)
is licensed by co-closedness of the paired object, and here d*(main) = D(S) − d*(defect) is **not computed anywhere**;
d*(Q_str^{(0→i)})^T is not ev^{(0→i)T}d* (that identity holds for the full Q^T, not the straight one — the two differ by
d*h^Td*). Equivalently, ⟨C(j), Y^p_0⟩ is representative-dependent when D ≠ 0, with defect ⟨D(S), λ_opt⟩ against the
𝒩-optimal λ_opt, which is **not** in Λ_0 and so is not killed by GT-split. So the clean statement is either (a) prove
d*(main) = 0 when D^root ≠ 0, or (b) re-run step (c) with the representative-dependence term explicit. Until then
COF-res is PROVEN as an **identity for the defect term**, and the claim that it is the *only* uncovered term is ARGUED.

## S10-11 "(CO-fun) as stated in §31.2 is FALSE without (CC-0)": **CONFIRMED**
The residue is a **point** pairing at the level-k roots, and the (P0)+(Pl-c)+(G)+(R) classes bound no norm of D^root(S)
beyond what follows from the currents' sups; with q of own size L^{−3}π_{k−1}(j_{k−1}) and Φ_k level- and k-independent in
own units (S8-5's convergent Φ_l, exact ratio 17/243), the term reaches ≍ L^{2k−3}π_{k−1}(j_{k−1}) ✓. S10-F4 genuinely
occurs. This is a correct self-refutation of session 9's statement, and [S10-fix 1] is the right erratum.

## S10-12 Remark MASSLESS / S10-F5: **CONFIRMED**
The free-kernel route f_0(p) = n²⟨J_0, Δ_0^{−1}d*δ_p⟩ loses a factor T. The shell count is right for d = 4
(|∇G| ≍ r^{−(d−1)}, Σ_{r≤N}r^{d−1}r^{−(d−1)} = N, so ‖∇G‖_1 ≍ side ≍ Tn) and then n²·n^{−3}π_0(J_0)·Tn = T·π_0(J_0) ✓.
The contrast with 𝒩(Y^p) ≤ C_YNn — which is T-uniform because Y^p decays exponentially on the coarse scale — is the right
diagnosis, and it is the reason (CC-0) rather than a sup bound is the hypothesis. Honest and useful.

---

# PART L: the (GT-sup) collapse (§36)

## S10-13 Proposition GT-split: **CONFIRMED**
Two independent routes, both checked: (a) λ ∈ Λ_0/const with Λ_0 = functions constant on the level-k roots, and
Σ_zD(S)(z) = 0 for every chain source (verified in S9-1), so the constant may be chosen to make λ vanish on the roots;
(b) for Γ_E it is pointwise, since χ^5_X(c_X) = 1 and Σ_Xχ^5_X = 1 with χ^5 ≥ 0 force Λ(x)(c_Y) = λ^E_Y(x)(c_Y) = 0 by
§16.1 (c)'s pin. ✓ The complementarity table (l.4151-4154) is a genuine structural finding: D^root and D^⊥ partition the
composite divergence between the two targets and neither drives both. I tried to find a source whose D^root feeds the
gauge-fixing remainder and could not — the pin forbids it.

## S10-14 Proposition GT-loc: **the inequality is CONFIRMED; the headline conclusion is NOT-VERIFIED**
*The inequality.* Lemma ΓT-op (d) (§25.1 (d), l.3390-3391) is a pure duality bound on **any** level-0 1-form:
|λ^E_X(x)(z)| = |⟨(λ^E_X)^Tδ_z, x_0⟩| ≤ ‖(λ^E_X)^Tδ_z‖_1·max|x_0| ≤ M_n‖δ_z − δ_{c_X}‖_1·max_{Ñ_X}|x_0| = 2M_nmax_{Ñ_X}|x_0|,
with the localisation to Ñ_X legitimate because (λ^E_X)^Tψ lives on the links of Ñ_X (ΓT-op (b)). **Y^p_{*,0} is in that
hypothesis class** — the class is "level-0 1-form", with no co-closedness or decay requirement — so the task's suspicion
(that ΓT-op (d) might not apply to Λ(Y^p_{*,0})) does not materialise. χ^5 ≥ 0 with Σχ^5 = 1 makes Λ(x)(z) a convex
combination over the ≤ 2^d boxes with |z − c_X|_∞ < 1 ✓, and 2M_n/n = 4(4n+1)/n = 16 + 4/n ≤ 20 for every n ≥ 1
(at k = 2, n = 9, it is 16.44). **Constant 20: verified, and absolute.** So "(GT-sup) ⟸ (Y-sup^loc) with constant 20" is
CONFIRMED.
*The headline.* "**(GT-sup) is not a question about where the spikes of λ^{Γ_E}_* sit**" (l.4168) does not follow, because
the sufficient condition it reduces to is probably **false** precisely in the regime the session identifies as the hard
one.
- (Y-sup^loc) is a bound on max_X‖(Y^p_*)^c_0‖_{∞,Ñ_X} in **coarse** units (§34.1 l.3966, §36.2 l.4162-4163), i.e. on
  n·max_own|Y^p_{*,0}|. So it demands max_own|Y^p_{*,0}| ≲ C/n on the boxes meeting supp D^⊥(S).
- The only profile consistent with Theorem YH's 𝒩(Y^p) ≤ C_YNn is a lattice-dipole field: in d = 4,
  |Y^p_0| ≍ |z|^{−3} gives Σ_{r≤n}r³·r^{−3} = n ✓, with an **O(1)** peak at the nearest links to p. Then the coarse sup
  near p is ≍ n, not ≍ 1.
- §36.2's own S10-F6 paragraph says the hard case is the core: "the response field is largest in the coarse cell
  containing p … if supp D^⊥(S) meets the coarse cell of p — which it does for a generic non-critical configuration …
  then the core value is what enters" (l.4170). So the reduction is to a statement that is most doubtful exactly where it
  is needed.
- The looseness is measurable in the lane's own data: bb8t T1 gives ‖(λ^E_X)^Tδ_z‖_1 ≈ 10.6n (§25.1 (c)), while lane A
  measures the actual λ at the roots next to p as σ ≈ 0.003 — i.e. the true value arises from **cancellation** in the
  dipole kernel A^X_w, which the ℓ¹ × sup step throws away. GT-loc is off by about a factor n relative to the measured
  object.
**So:** §36.2 establishes "there is a sufficient condition for (GT-sup) that is not about spike support". It does not
establish that (GT-sup) is not a spike question: it replaces a question that lane A's measurements say is favourable by a
condition the free-field count says is false. That is a legitimate and useful route to have priced, but the headline, the
§37.2 table row and the lane-A note 4 ("A new named item that is yours, and **it is small**: (Y-sup^loc)") read as
settling more than they do. (Y-sup^loc) is not small; on the free-field count it is false.

## S10-15 Proposition GT-attr: **the arithmetic is CONFIRMED; the conclusion is NOT-VERIFIED as stated**
The attribution arithmetic is right and I re-did it: n²·L^{−3(k−l)}η²·σ = L^{3l−k}·σ·η², reaching L^{2k−3}η² at l = k−1
(BFT_A l.3550-3551), so **every power of L in Lemma RC's *Reading* comes from n² = L^{2k} and from the own-unit size of a
point charge at a level-l root; σ contributes the k-independent 0.003.** Conclusion: the k-growth in that display sits in
the **charge** factor ✓.
Two problems with the step from there to "(GT-sup) is expected TRUE".
1. **Three distinct objects are conflated.** Lane A's σ is the **S_E → S^♯** transport of Lemma RC
   (f^♯_0 − f^E_0 = n²⟨D(S), σ(Π_EY^p)⟩, BFT_A l.3546); Φ_k is the **response's funnel**, which §35.7 pairs with D^root;
   λ^{Γ_E}_*(p) is the **representative → S_E** transport. §36.1 proves λ vanishes at the level-k roots while
   Φ_k(Y^p_0)(c_X) does not, so these cannot all be the same thing. The "independent support" paragraph (l.4177) argues
   λ's k-independence from S8-5's convergence of Φ_l. The status ARGUED is right; its two named reasons (σ quoted, not
   re-derived; (Y-sup^loc) unproven) should be joined by a third: **the identification of λ^{Γ_E}_{C0#} with lane A's σ is
   itself unverified** (S9-16).
2. **[S10-fix 2] over-corrects.** Session 9's "expected FALSE" was poorly argued (it attributed the growth to λ) and the
   correction of that attribution is right. But the replacement, "**(GT-sup) is expected TRUE**, conditionally on
   (Y-sup^loc)", rests on a conditional whose antecedent is probably false (S10-14) plus a two-point measurement at
   k = 2, 3 of a different object. The defensible erratum is: *the k-growth of Lemma RC's Reading is in the charge factor
   (PROVEN arithmetic); the k-uniformity of sup|λ^{Γ_E}_*| is established by neither route and remains open.*
3. Independently of 1-2: even a k-uniform sup|λ| does not give the implication of §31.3 (R2), because of the n² of S9-15.

## S10-16 Proposition GT-ell: **CONFIRMED as an implication**
The identity ⟨D^⊥, Λ(Y^p_0)⟩ = ⟨Γ_E^TD^⊥, Y^p_0⟩ is right (Λ = Γ_E as an operator, §25.1 (a)); Hölder ✓; ΓT-op (e) ✓;
the n-bookkeeping ✓ (n²·𝒩 ≤ C_YNn³; (M_n/4)n³ = (4n+1)n³/2 ≤ 2.5n⁴). The **derived** (NEUT-box),
max_X|⟨χ^5_XD^⊥⟩| ≤ Cn‖D^⊥‖_∞, is the correct comparison of the two terms, and the session is right that §34.1's
pre-stated form had the n-power on the wrong side, and right to leave the pre-stated line as the record. The "without
cancellation |Q_X| ≍ n^d‖D^⊥‖_∞ so the second term exceeds the first by n^{d−1}" count is right.
Two notes. (i) **The exported name is ambiguous**: §37's FOR OTHER FILES sends "(NEUT-box)" to PROOF.md, and §34.1 and
§36.4 define it **differently** (by a factor n⁴). The export must carry §36.4's definition explicitly. (ii) §36.4 keeps
C_∞ ≤ 1.71 although this session's own [RBB8-fix RS8-5] records C_∞ = (1 − M^{−4})/8 = 0.125 (bb8t T2's measured
max|∇G_M| = 0.1250): the second term is quoted 13.7× loose. Cosmetic, but it is an erratum the same session entered.

---

# PART M: Theorem NCE and the answer sent to lane A

## S10-17 §36.5 (ii)'s "one scalar per level-k box": **CONFIRMED for the corrected source; NARROWED as a reduction**
The identity D(S^E_0(S)) = I_χ^TD(S) is right (Lemma DF (iii) / §25.1 (f): d*Γ_E^TD = −D + Σ_XQ_Xδ_{c_X} with
Q_X = ⟨χ^5_XD⟩), and it was already verified numerically in session 8 (bb8t T6, 1.5e-15). For **S^E_0(S)** the root
charges of COF-res and the compensation charges of GT-ell/(NEUT-box) are literally the same scalars ⟨χ^5_XD(S)⟩, so "two
faces of the same quantity" is CONFIRMED **for the corrected source** (it is not a general statement about a source's own
D^root, which is a value at a root rather than a box average). The reduction as a whole is NARROWED by S10-10: that
everything *other* than those scalars is covered by Theorem COF is not established when D ≠ 0.

## S10-18 §36.5 (v) and FOR OTHER FILES 1: **WRONG**
REVIEW_BFT_A_S8 l.571-575 asks: lead decision D1's route "is the only route that sidesteps the dichotomy … **the
remainder bound it needs is written nowhere**, and Lemma RC's *Reading* says the remainder can reach L^{2k−3}η². **That
bound** is the single highest-value missing object in lane A." §36.5 (v) replies "**It is written:** Proposition NCR …
is that bound, in exact product form", and §37's lane-A note 1 says the request "is already answered".
Proposition NCR is an **identity**. Its two factors are n²‖D^⊥(S)‖_1 (unbounded as far as anything proven goes; by
§36.3's own attribution this is the k-growing one) and sup|λ^{Γ_E}_*| (CONDITIONAL on (Y-sup^loc), itself doubtful). The
bound asked for does not exist yet. What §31/§35/§36 genuinely supply is the exact **form** of the remainder and a
reduction of its size to two named open items — which is real progress and should be reported as such. **Fix the two
sentences before lane A reads them**, since a lane owner told "your highest-value missing object is already supplied" will
not look for it.

## S10-19 §36.5 (iv): **CONFIRMED, and it is the most valuable paragraph in the two sessions**
"Nothing above is at θ > 0, at m > 0 or at a nontrivial background; every lane-A input used is at the trivial background.
The factor k in (NC-Γ) and (PW-ii) are untouched … (GE-T) remains refuted … so the two refutations are the same fact seen
twice." Every clause of that is right, and the last one — that (CO-fun)'s residue and the (GE-T) refutation are one
functional — is a real unification (it is why §37's lane-A note 3 "please do not price them as two items" is correct
advice). The paragraph also contains the admission that refutes §36.5 (i), which is why S10-6 is a correction and not a
reversal of the session's own understanding.
One terminology collision to fix: "nothing here is claimed at θ > 0" (§34.0 l.3952) sits beside Theorem COF's hypothesis
"0 < α < θ < 1" (l.4076). Two different θ's, or one θ used two ways; as written the scope line contradicts the theorem.

---

# PART N: checks bb10 and bb10c

## S10-20 bb10: **CONFIRMED ALL PASS, and each test computes what its table row says it computes** (whether it could have *failed* is Part P)
I read the helpers and A2-A8, B0-B1. `mkC` uses the **full** Q^{(0→1)T} ✓; `DofS` is D(S) as defined ✓; `rootrestrict`
uses the nested centre map z = L^lX + Σ_{t<l}L^t·1 ✓ and returns `ok = False` when the function is not root-supported, so
A3/A5 and C5 are genuine constraints ✓; `psis` builds ψ from the **source** ✓ (so A3/A4/A5 are solve-independent — see
S9-4). A8's two bounds re-derived exactly (332, 108 against values 24-30) ✓. The disclosures are accurate and unflattering
where they should be: A1 "trivial at k = 2", A7 "second half vacuous", limitation 2 "bb10 verifies the regrouping identity
and does not — cannot — exhibit its size gain", limitation 6 "bb10 tests nothing in §36".

## S10-21 bb10c: **CONFIRMED, including the handling of the C4(b) FAIL**
- Script provenance verified: `diff` of bb9b l.9-250 against bb10c l.1-250 differs only in the header block and
  `K = 3`; the whole operator core (Lev, sparse helpers, build, solve_div, rnd) is byte-identical. "Exactly one change"
  is exactly true.
- C4's numbers re-derived exactly from the printed π_l for two of six instances: B^ψ = (1792, 2116/3, 2440/9) and
  (916, 1240/3, 1564/9), B^ξ_0 = 648, B^ξ_1 = 108. All match.
- **C4(a) really is the inequality Proposition COF-size uses.** V_i := π_0((Q_str^{(0→i)})^Th_i^Tψ_i) ≤ B^ψ_i is the
  composition of the two facts the proof uses (the coarse-unit contraction π_0((Q_str^{(0→i)})^Tv) ≤ π_i(v) and
  Lemma FT (ii)'s bound on π_i(h_i^Tψ_i)). It passed in all 18 instances (V = 0-108 against B^ψ = 184-2116/3). The task's
  suspicion — that C4(a) might be a different, easier inequality — does not hold.
- C4(b) compares two **upper bounds** on one vector and so can refute no lemma. The diagnosis is right: `solve_div`
  builds an antiderivative, so π_0(j_0) = 229-448 against π_1 = 27, π_2 = 9, and B^ψ_0 = 4π_0(j_0) exceeds
  B^ξ_0 = 4(3·27 + 9·9) = 648 on all six instances. I verified both arithmetics. Keeping the FAIL, not re-running, and
  refusing to design a balanced family after seeing the result ("designing one after seeing this result would be a
  post-hoc probe; it is **not** run here", l.4307) is exactly right.

## S10-22 What the bb10c FAIL does cost: **CONFIRMED-WITH-FIX**
The control that failed is the one **§34.5 pre-stated at 13:07:28, inside BFT_B.md**: "(C1) a collection whose regrouping
is done with the **naive** per-level funnel (no regrouping) fails the size claim, i.e. the regrouping is load-bearing"
(l.4000). Its criteria-file form (A7) was declared half-vacuous by the 13:12 amendment, and its direct form at k = 3
(C4 (b)) FAILED. So: **no check supports the size claim of Proposition COF-size; it rests on Lemma FT (ii) and the
push-down contraction alone** — both of which I verified analytically (S9-5, S9-6, S10-5), so the claim stands on proof.
§37.4 (2) states this plainly (l.4307) and the log repeats it; **§37.2's outcome table does not**, and its rows
"bb10 ALL PASS" and "A7 … PASS" read against it. Add the sentence to the table.
(A5/C5 are a *different* control: they show (CC-0) is load-bearing for the **identity**, not for the size.)

---

# PART P: discriminating power — which verdicts could have FAILED?

Added at the lead's request after BFT_B session 11 (outside my scope) recorded that lane B's abelian model is vacuous for
its own §41 nonabelian statements. The lens: **for each claimed PASS, does the abelian, d = 2, k = 2 (or k = 3) model have
the power to have failed it?** I answered this from the code (bb9b l.97-172 for the operator construction, which bb10 and
bb10c copy verbatim), not from the tables.

## S10-23 The construction, and what it makes unfalsifiable
`build(T)` (bb9b l.97-172) codes `dfun`, `dstar`, `dform`, `ev`, `Qstr` and `h` each from its own formula, and then
**defines** `Q = Qstr − dfun∘h` (l.171). Two consequences:
- `dstar` is coded independently (l.110-117) but is numerically equal to `mt(dfun)`: for site z it sums
  v(z−e_μ, μ) − v(z, μ) over μ, which is exactly dfun's transpose. So any test of the form "d*(X^T) = (dX)^T" is the
  transpose of another test plus the single fact dstar = dfun^T.
- Because `Q` is **defined** as Qstr − d∘h, every identity that is the transpose or rearrangement of that definition holds
  by construction. BL-2 (b) is therefore **assumed** in the model, not tested.

## S10-24 bb9b, test by test: **5 of 15 verdicts were not forced; 4 are tautological or near-tautological**

| id | could it have failed? | why |
|---|---|---|
| A1 Q_ld = d ev | **YES — real power** | Q_str's telescoping over block translates (Σ_{j<L}dλ = λ(y+Le_μ)−λ(y) ⇒ d of the block average) and h's axial telescoping (h(dλ)(X) = Avg_Xλ − λ(c_X)) are coded independently and must cancel. A wrong offset in Q_str's y-range or a wrong axial path fails it. This is the one operator gate with content. |
| A2 d*Q_l^T = ev^Td* | low | A1 transposed; its only independent content is "the independently coded dstar equals dfun^T". |
| A3 Q_l^T = Q_str^T − h^Td* | **NO — TAUTOLOGY** | it is the literal transpose of l.171's definition of `Q`: mt(Qstr − dfun·h) = Qstr^T − h^T·dfun^T, compared against Qstr^T − h^T·dstar. It reduces to dstar = dfun^T and **cannot falsify Lemma RT-cc (b)**, which *is* that transpose. |
| A4 FT (i) | **YES — real power** | support, one-block-per-link and |c| ≤ 1 are properties of the axial-path code; I rebuilt them from the definition and they are non-trivial (a wrapping path or a block-crossing link fails it). |
| A5 cascade support | no, **by design** | Ψ_0 root-supported *follows* from composite co-closedness (that is the proof, S9-1), and the sources are constructed composite-co-closed. Power only against an ev^T/d* indexing error. |
| A6 control | **YES — real power**, and it is what makes A5 non-vacuous | it exhibits a source violating the support claim; had every source satisfied it, A5 would have been empty. The A5/A6 pair is correctly designed. |
| A7 funnel non-vacuity | **YES — real power** | h^T could have been vacuous and the ratio could have exceeded 1. The criteria amendment (bb9_criteria.md l.78-80) adds A7 for exactly this reason — the session applied the lead's lens to itself, before the script existed. Credit. |
| B0 criticality | **NO — near-zero power** | every operator assembled from r_l and dx_0 is annihilated by Ξ (root covariance, S9-10), so HΞ = 0 holds for a wide class of *wrong* Hessians, and Ax = S with Ξ^TS = 0 then forces Ξ^Tx = 0 and Hx = S. **Demonstrated empirically: B0 PASSED in bb9 on the buggy energy.** |
| B1 non-vacuity | **YES** | the constructed source could have come out level-wise co-closed. |
| B2 RT-cc (a) at the solution | **YES — over the level-0 equation** | ψ_0 = d*ρ_0 is solution-derived, the root restriction of d*j_0 is source-derived, and the 180×180 solve links them. It passed in **both** runs because the bug was in g1, not g0 — which is itself evidence that B2's power is confined to (E_0). |
| B3 RT-cc (b),(c) | **YES — over the level-1 equation; NO over the funnel** | it is the gate that caught the bug, so its power is demonstrated. But ψ_1 ≡ 0 at T = 1 (the level-2 torus has one site, so d* of any 1-form is identically 0), hence Q_1^Tρ_1 = Q_{str,1}^Tρ_1 and B3 reduces to the level-1 Euler-Lagrange equation. The straightening is not exercised. |
| B4 control branch | **NO — zero independent power** | "ψ_1 = 0" is forced by the one-site level-2 torus, not measured; with ψ_1 = 0 the funnel-free identity *is* B3. |
| B5 RT-cc (d) | low | "d*dx_0 = J_0" is the solve's own g0 row given B0; "d*J_0 = 0" follows from A2 + B2. |
| B6 FT (i) at the solution | low | A4 applied to one ψ; it does add a non-vacuity instance (2 against 6). |
| B7 control | **YES** | it could have shown the solve always returns a critical point. |

**So the funnel's role inside the ρ-recursion — Lemma RT-cc (b)-(c)'s one substantive content — is exercised numerically
nowhere in bb9 or bb9b.** §33.1's scope limitation (4) says Part B does not exercise it and that "A3 + A7 at T = 2 carry
that part" (l.3894); **A3 cannot carry it**, being the transpose of the model's definition of Q, so only A7's non-vacuity
of h^T survives, and A7 says nothing about the recursion. This is the sharper form of S9-23 and it strengthens, rather
than weakens, the answer on the re-run: bb9b does test the same thing bb9 was meant to test (same criteria, one
expression, S9-21/S9-22) — but **what both were meant to test in Part B is the Euler-Lagrange system and the level-0
assembly, not the funnel**, and the record reads wider than that.

## S10-25 bb10 and bb10c, test by test: **only A5, A7(a), A8 and C4/C5 had unforced outcomes**

| id | could it have failed? | why |
|---|---|---|
| bb10 A1 | **NO — tautology** | at l = 1 the telescoping collapses by cancellation for *any* operators: ⟨j,Y_1⟩ = ⟨j,Q_0Y_0⟩ − ⟨j,Q_0Y_0−Y_1⟩. **The session says so in its own table** ("trivial at k = 2 — an exactness check of the operators, not of content", l.4225). Credit for the disclosure. |
| bb10 A2 | low | ≡ bb9b A2, i.e. A1 transposed. |
| bb10 A3 ξ_0 = R_1(D) − ψ_0 | low-moderate | it reduces to R_1∘ev^{(0→1)T} = id plus linearity, which `rootrestrict` (l.262-275) satisfies by construction; its real content is the **nesting of the root hierarchy** (z = L^lX + Σ_{t<l}L^t·1), which a wrong offset would break. |
| bb10 A4 "the central test" | **NO — forced by A3** | expanding, A4 ⟺ h_0^T(ψ_0 + ξ_0) = 0 ⟺ h_0^TR_1(D(S)) = 0, which under (CC-0) is h_0^T(0) = 0. So A4 = A3 + the transposed definition of Q + D(S) = 0. The criteria call it "the central test" whose FAIL "refutes Lemma DF-cc (ii) and therefore the session-10 proof of Theorem COF" (bb10_criteria.md l.37-42); **in this model it cannot fail if A3 passes.** |
| bb10 A5 control | **YES — real power** | the defect could have vanished for every constructed source, which would have made A4's hypothesis vacuous; it did not. Together with C5 this is the best-designed gate in session 10. |
| bb10 A6 | low | the push-down bound is forced by the kernel being L terms of weight L^{−d}; |h_0^Tψ_0| ≤ |ψ_0| is A4-of-bb9b; |ψ_0| ≤ |d*j_0| is forced because ψ_0 is a *restriction* of d*j_0. |
| bb10 A7(a) naive funnel exceeds the threshold | **YES** | a genuine measurement that could have gone either way. |
| bb10 A7(b) regrouped does not | **NO — vacuous** (disclosed in the amendment and in the table) | ψ_1 = 0 under (CC-0) at k = 2. |
| bb10 A8 | moderate, but loose | the two LHS are **the same vector** (ψ_0 = −ξ_0, S10-4), so it is one measurement against two bounds, with a ×10 margin (24-30 against 332 and 108): it would not catch a factor-2 error in 2d. |
| bb10 B0 | **NO — near-zero** | as bb9b B0. |
| bb10 B1 | **YES — over the level-1 equation** | J_0 = C(j) − (Q_str^{(0→k)})^Tρ_{k−1} uses (E_1) at the solution (I checked: it needs ρ_0 = Q_1^Tρ_1 − j_1 **and** d*(Q_{str,1}^Tρ_1) = ev^Tψ_1 = 0), so a wrong Hessian fails it. Zero power over the funnel, again because ψ_1 ≡ 0. |
| bb10c C1 (k = 3) | moderate | three-level nesting and the composition ev^{(0→i+1)T}ev^{(i+1→l)T} = ev^{(0→l)T}; a root-convention or composition error fails it. No power against the lemma. |
| bb10c C2 (k = 3) | moderate | C1 plus the **composite factorisation** (Q^{(0→l)})^T = (Q_str^{(0→l)})^T − Σ_{i<l}(Q_str^{(0→i)})^Th_i^Tev^{(i+1→l)T}d*, i.e. the double-sum exchange of Lemma DF-cc (ii) at two inner terms. This is the one place in either session where that exchange is exercised at all, and a wrong order of composition would fail it. It is still an algebraic consequence of the definition, so it cannot falsify the lemma. |
| bb10c C3 | low | A2-type algebra plus (CC-0). |
| bb10c C4 (a) | **YES** | a genuine inequality (V = 0-108 against B^ψ = 184-2116/3), though loose. |
| bb10c C4 (b) | **YES — and it DID fail** | the only gate in session 10 whose outcome was neither forced nor favourable. |
| bb10c C5 control | **YES** | it could have shown the (CC-0)/root-support hypothesis vacuous at k = 3; it did not. |

## S10-26 What no check in either session can reach — including my own Part J refutation
1. **The sources.** Both checks set s = G = 0 and use random or constructed small-integer currents, so **nothing about the
   actual BCH₂ remainder rows is tested**: not their sizes, not q_R/N_R, and — decisively — **not their level decay**.
   My Part J refutation of Corollary COF-crit turns on exactly that (per-level π_l(V_l) vs the class norm
   ‖V‖_Pc ≍ L^{θ(k−1)}π_l), and it is invisible in this model twice over: the rows are absent, and at k = 2 or 3 a factor
   (k−1) is 1 or 2. **bb10's "ALL PASS" gives no support whatever to §35.6**, and §37.2's table should not be read as if
   it did.
2. **Lemma CD (i)**, the sole supplier of (CC-0) at critical points, is a **nonabelian** identity
   (Ξ^T𝔑^0 = −K'^T_x∇(𝔉_k∘exp)) quoted from lane A. No lane-B check touches it. So the hypothesis that carries
   Corollary COF-crit, Corollary COF-crit's η² sizes and Theorem NCE (i) rests entirely on a quoted nonabelian lemma,
   while every check in sessions 9-10 is abelian.
3. **All of §36.** The box-Neumann objects (λ^E_X, Λ, Γ_E^T) are not in the model at all — §37.1 limitation 6 says so
   (l.4242). So Proposition GT-loc's constant 20, GT-ell's n-powers and (NEUT-box) are unchecked here; they rest on §25.1
   and on session 8's bb8t.
4. **d*d* = 0** (used at l.3667, l.3686 and in Lemma SPLIT l.4035) is not among the tested identities in either check.
   Cheap to add.

## S10-27 Verdict on the nonabelian lens for sessions 9-10, as against session 11
**The abelian model is scope-matched here, unlike session 11's case, and I will not hold the nonabelian vacuity against
bb9b/bb10.** Sessions 9-10 are explicitly at m = 0 and the **trivial background**, where Setting LIN's chain maps are the
linear ones (Ad_Z = 1), so Lemma RT-cc, Lemma FT, Lemma SPLIT, Lemma DF-cc, Proposition COF-size and Proposition NCR are
genuinely abelian-visible statements and the model is the right one for them. Session 11's situation is different in kind:
its statements are *about* nonabelian structure.
What the lens does establish is narrower and still worth entering: **the two checks verify the implementation of the
operator algebra and the nesting of the root convention, not the content of the lemmas** — which is consistent with the
lemmas being transposed and rearranged forms of the definitions (that is why my own rebuild went through without
resistance, S9-1 to S9-3 and S10-3). The honest one-line summary for the ledger is: *of 15 bb9b verdicts, 5 had unforced
outcomes and 4 are tautological or forced; of 11 bb10 verdicts, 3 had unforced outcomes; bb10c's C4/C5 are the only gates
in session 10 with both power and a non-vacuous hypothesis, and C4 (b) failed.*

---

# PART O: adjudication — session 10 against session 9 on (CO-fun)

**Session 10 is right, on both of its claims, and (CC-0) is the right hypothesis rather than a convenient one.**

1. **"The funnel is not a source"** (l.4006): CONFIRMED. The funnel is produced by the ρ-recursion, so it never appears in
   the dual pairing f_0(p) = n²⟨S, Y^p⟩; what is superposed is the **source**, slot by slot, and each slot is
   composite-co-closed (Lemma SPLIT, S10-2). §31.2's stated reason for (CO-fun) being open — "the funnel pieces … cannot
   be fed into Theorem W0's hypothesis one at a time, and Corollary LIN0's superposition does not apply to them"
   (l.3802) — is therefore **superseded**, exactly as [S10-fix 1] says. Session 9's diagnosis was wrong.
2. **"(CO-fun) as stated in §31.2 is FALSE"** (l.4009, l.4122): CONFIRMED (S10-11). The classes bound no norm of
   D^root(S), and COF-res's point pairing reaches L^{2k−3}π_{k−1}(j_{k−1}).
3. **Is (CC-0) the right hypothesis?** Yes, and session 10 under-sells the reason. (CC-0) ⟺ ψ_{k−1} = 0 ⟺ **the top
   residual r_{k−1} is co-closed**, which is precisely the property Theorem W0's own step 3 uses (BFT_A l.2473: "with
   r_{k−1} co-closed as in §18.4 Step 1"). So (CC-0) is not an extra assumption bolted on to make a proof work: it is the
   exact generalisation to multi-level sources of the hypothesis W0 already has. Lemma CD (i) supplying it at critical
   points is then a fact about the nonlinear problem, not a choice.
4. **Circularity?** No (S10-8). Theorem COF quantifies over sources and is non-vacuous without any critical point
   existing; it does not assume existence or uniqueness in the ball. The *specialisation* to critical points is a
   narrowing of scope, not a circular argument — and the narrowing is stated in both sessions.
5. **Where session 10 over-reaches is not (CC-0) at all.** It is the one arithmetic substitution of S10-6: feeding
   per-level row sizes into a bound whose k-uniformity needs the (Pl-c) class norm. Remove that step and everything else in
   §35-§36 stands.

One further asymmetry worth recording: session 10 refuted its predecessor **and itself** (§37.4 withdrew §37.1's
limitation 2 within three minutes, before building a check on it) and then ran a post-hoc check that **failed against its
own narrative** and kept it. That is the behaviour this process is supposed to produce.

---

# Binding fixes

Binding unless marked cosmetic. Numbering [RBB9/10-fix].

**Lane B — session 10's arithmetic (highest priority; downstream files already carry the error)**
1. **RS10-1 (binding).** §35.6 Corollary COF-crit: the substitution of π_l(V_l) ≤ 2C_NCC_bchκ_+L²η² ("uniform in l") for
   ‖V‖_Pc is invalid; ‖V‖_Pc ≍ L^{θ(k−1)}η². Re-state as: *at a critical point of 𝔉_k,
   ‖f_0‖_∞ + [f_0]^∞_α ≤ C''·k·η² with C'' k-, T-free (≈ 25(k−1) at θ* = 1/((k−1)ln L)); the k-uniform form is
   **CONDITIONAL on a level-decay input for the non-co-closed plain rows** — lane A's (SPD)/(W2) (BFT_A l.830-831,
   OPEN).* Cite [RBA2-fix] B3 (BFT_A l.819-824) as the standing statement of the same fact.
2. **RS10-2 (binding).** §36.5 (i) Theorem NCE (i): split the claim. Residual half (Corollary RHT-V + §31.2 (a)):
   PROVEN, k-, T-, Γ-uniform. Curvature half (Corollary COF-crit): PROVEN with a constant O(k); k-uniform only given
   (SPD). Delete "with constants independent of k and T" from the combined statement, and reconcile with §36.5 (iv).
3. **RS10-3 (binding).** §36.5 (v) and §37 FOR OTHER FILES → BFT_A item 1: withdraw "It is written" / "is already
   answered". Proposition NCR is the exact **form** of the remainder; the **bound** REVIEW_BFT_A_S8 l.574-575 asks for does
   not exist, since both of NCR's factors are open.
4. **RS10-4 (binding).** §31.3 (R2) / §27.4's "expected relation": restore the n² and state the **third** input the
   implication needs — a k-uniform bound on n²‖D^⊥(S)‖_1 — and add it to the named open set and to the PROOF.md export.
   §35.1's "the omission changes nothing in either statement" holds for NCR and not for (R2).
5. **RS10-5 (binding).** §34.1/§36.4: the exported name **(NEUT-box)** has two inequivalent definitions in this session
   (they differ by n⁴). Every export must carry §36.4's derived form.
6. **RS10-6 (binding).** §35.7/§36.5 (ii): state that "every other term bounded as in Theorem COF" is not established for
   D ≠ 0, because d*(Σ_l(Q_str^{(0→l)})^Tĵ_l) is not computed and step (c)'s representative freedom is unlicensed for it.
   Either prove it or re-run step (c) with the ⟨D^root, λ_opt⟩ term explicit.
7. **RS10-7 (binding).** §36.2/§37.2/§37's lane-A note 4: (Y-sup^loc) demands max_own|Y^p_{*,0}| ≲ C/n near p, which the
   |z|^{−3} profile behind 𝒩(Y^p) ≍ n contradicts. Remove "it is small"; record that GT-loc is lossy by ≍ n against the
   lane's own measurements (bb8t T1's 10.6n vs σ ≈ 0.003), so the route prices (GT-sup) rather than settling it.
8. **RS10-8 (binding).** [S10-fix 2]: keep the attribution correction (it is right), drop "expected TRUE". Read:
   *the k-growth of Lemma RC's Reading sits in n²|D(R)(Z)| (arithmetic PROVEN); the k-uniformity of sup|λ^{Γ_E}_*| is
   established by neither route.* Add as a third named reason that the identification of λ^{Γ_E}_{C0#} with lane A's σ —
   which is the S_E → S^♯ transport (BFT_A l.3546) — is unverified.
9. **RS10-9 (binding).** §31.1 *Reading* 2's "its level-k-root part is TE's tent data" is refuted by this session's own
   §36.1 (λ vanishes at the level-k roots) and superseded by §35.7. Enter the erratum; neither [S10-fix 1] nor
   [S10-fix 2] covers it.
10. **RS10-10 (cosmetic).** §34.0's "nothing here is claimed at θ > 0" contradicts Theorem COF's "0 < α < θ < 1".
    Disambiguate the two θ's.
11. **RS10-11 (cosmetic).** §36.4 should use RS8-5's own C_∞ = (1 − M^{−4})/8 = 0.125, not 1.71 (13.7× loose).

**Lane B — session 9**
12. **RS9-1 (binding).** §32.1 (c)/§32.2/§33.2: clause (c) of (BFT-5_E) is at the background Z(V_k), while
    Proposition NCR is a trivial-background Setting-LIN statement (Lemma FG (ii), Ker H = Ran Ξ). Clause (c) is
    **CONDITIONAL** on the background-covariant analogue, not PROVEN.
13. **RS9-2 (binding).** §29.4 / §33.2 / FOR OTHER FILES: state Corollary RHT-V as the **increment** — N_res ≤ C_1‖x‖_inv
    + C_2η² — or keep the η² form and name the hypothesis ‖r^c_{k−1}‖_∞ ≤ ‖x‖_inv ≤ G_Rη², which is (H-inv) for the same
    non-co-closed rows and is not supplied by Corollary LIN0 (whose plain slot is level-wise co-closed).
14. **RS9-3 (binding).** §32.2's (G♯-patch^Ω): record that CL-iv supplies at most the chain half of G-pert's
    t = ‖x^r‖_X + ‖B^r‖_D, in a norm not shown to dominate ‖·‖_{X_c}; that ‖B^r‖_D in the frame gauge is unsupplied
    ([RSF2-fix GP-2]); and that the gluing needs the slice-change step SF calls "not proven" ([RSF2-fix GP-1]). Status of
    the narrowing: **ARGUED**.
15. **RS9-4 (cosmetic).** §29.4: cite σ := max_c sup|R_c| rather than sup|R^B_l| in C_NC's bound (BFT_A l.2394).
16. **RS9-5 (cosmetic).** §29.5: the funnel's e^{2m} belongs to the plain slot (10 + 2), so c_w = 12 suffices; 14 is a
    valid over-estimate.
17. **RS9-6 (cosmetic).** §33.3 / FOR OTHER FILES → PROOF.md: the "(Res-Hölder)" line must distinguish
    **Theorem RHT-cc** (every composite-co-closed source, every critical point of **E_src** — unconditional, no
    𝔉_k-criticality) from **Corollary RHT-V** (the BCH₂ remainder, at critical points of **𝔉_k** only). As written
    (l.3939) the ledger entry reads as the second with the scope of the first.
18. **RS9-7 (cosmetic).** bb9_criteria.md l.4-5's "No threshold below uses any constant derived in session 9" is false as
    written (§29 preceded the file by 42 s); re-word to "every threshold is from §27.2, written before any derivation".
    bb9_criteria.md l.58-59's "B3 still tests the straightening" is void at T = 1 (ψ_1 ≡ 0): withdraw it.
19. **RS9-8 (cosmetic).** No ledger may treat §27.2's K_f = 8.74 or c_w = 14, or §34's labels, as pre-registered; both
    sections concede that their only claim is file order. This is [RBA2-fix] P1's standard, applied to lane B.

**Process**
20. **RS10-P1 (binding).** Label **bb10c post-hoc** (designed after bb10's A8 ratio was seen), per DRIVE_BRIEF rule 3 and
    this lane's own precedent [RBB8-fix RS8-7] (ii). It loses no weight: a post-hoc check that fails against its author's
    narrative is the strongest kind.
21. **RS10-P2 (binding).** §37.1: bb10_criteria.md has birth = mod = 13:12:15, so "born 13:09:13, with one amendment
    appended at 13:12:09" is not supported and the pre-amendment text is unrecoverable. Record the rewrite.
22. **RS10-P3 (binding).** §37.2's outcome table must carry §37.4's conclusion: **no check supports the size claim of
    Proposition COF-size**; the pre-stated control of §34.5 ("the regrouping is load-bearing") was weakened to vacuity
    (A7) and then failed at k = 3 (C4 (b)).
23. **RS10-P4 (binding; Part P).** §33.1's and §37.1's check tables must record which verdicts had the power to fail.
    In particular: **bb9b A3 is the transpose of the script's own definition of Q** and cannot carry Lemma RT-cc (b)
    (so §33.1's "A3 + A7 at T = 2 carry that part", l.3894, is wrong — only A7 survives, and A7 is about h^T's
    non-vacuity, not the recursion); **bb9b/bb10 B0 has near-zero power** (demonstrated by bb9, where it passed on the
    buggy energy), so it must not be cited as a criticality test; **bb10 A4 cannot fail if A3 passes**, so the criteria
    file's "a FAIL refutes Lemma DF-cc (ii)" overstates it; bb10 A1 and A7 (b) and bb9b B4 are already disclosed as
    trivial or vacuous, which is the right practice and should be extended to the three above.
24. **RS10-P5 (binding; Part P).** §37.2 must state that **bb10 bears on nothing in §35.6**: the model contains no rows
    (s = G = 0) and no level count worth measuring at k = 2-3, so "ALL PASS" is not evidence for Corollary COF-crit.
    Also record that **(CC-0) at critical points rests on Lemma CD (i), a nonabelian identity no lane-B check touches**.
25. **RS10-P6 (cosmetic; Part P).** Add d(dλ) = 0 / d*d* = 0 to the next check's operator identities: it is used at
    l.3667, l.3686 and l.4035 and is tested nowhere.

**Downstream (for the lead, not edited)**
26. **RS10-D1 (binding).** SESSION24_RESULTS.md l.870-872 ("**k,T-uniformly**" at critical points) and HANDOFF.md
    l.84-85 ("Off the critical set, the **entire** remaining obstruction … is the compensation charge") both pre-date
    RS10-1/RS10-2 and must be corrected before any further session builds on them. The level-count factor k is
    **upstream** of (TENT-Q), (NEUT-box) and (Y-sup^loc): supplying all three still leaves ≈ 25(k−1) in the curvature
    half at critical points.

**Lane A (for its owner; not edited)**
- **P9/10-a.** Lane B's §29 closes (Res-Hölder) for your non-co-closed V_l **as the (H-inv+) increment**, at critical
  points of 𝔉_k, for every gauge fixing. The mechanism is real and I rebuilt it: d*ρ_l is the level-(l+1)-root
  restriction of Σ_{l'≤l}d*j_{l'}, forced by root covariance and the injectivity of ev^T, and determined by the **source
  alone**. [RBA5-fix] U7's co-closedness restriction can be lifted for the residual-gradient outputs — not for the
  curvature outputs.
- **P9/10-b.** Your (SPD)/(W2) (l.830-831) has become the **gating item** for the curvature half at critical points, by
  the mechanism of your own [RBA2-fix] B3. It is now worth more than (TENT-Q), (NEUT-box) or (Y-sup^loc).
- **P9/10-c.** (CO-fun)'s residue and your tent coefficient really are one functional (Proposition COF-res); lane B's
  advice not to price them twice is right.
- **P9/10-d.** Your "single highest-value missing object" (REVIEW_BFT_A_S8 l.574) is **not** supplied. Its exact form is
  (Proposition NCR), and the two factors are named and open.

---

# Tally (lane B session 9; nothing counted in PROOF)

| verdict | items |
|---|---|
| CONFIRMED | provenance and append-only (byte-exact, including both in-place §28 corrections); criteria-before-script (birth times); all nine [RBB8-fix] errata, with the content REVIEW_BFT_B_S8 asked for; the GE-T → ΓT-op rename (complete, no misreading survives); **Lemma RT-cc (a)-(d)** (rebuilt; ev^T injective on the whole space; cascade consistency ⟺ composite co-closedness, both directions); **Lemma FT (i)-(iv)** (kernel independently recomputed: max|c| = 1/3, ℓ¹ row sum 4/3); **Theorem RHT-cc** (index swap, K_f = 8.7377); **Theorem RHT_m-cc** (c_w = 14 conservative); V composite-co-closed at critical points; **Corollary RHT-V's "for every gauge fixing"** (exact gauge invariance of r_l + Lemma FG (iii)); C_V free of hidden k/T/level dependence; **Proposition CO-use** (every quoted status checked at its line); **Proposition NCR**; **§31.2 (a)**, the residual half, k-, T-, level-uniform; **Lemma Rω-frame as ARGUED**; the bb9 bug diagnosis and that bb9b tests the same thing |
| CONFIRMED-WITH-FIX | Corollary RHT-V's η² headline (hidden (H-inv) hypothesis; σ vs sup|R| in C_NC); "(H-inv+) PROVEN as an implication" (class the remainders do not occupy; LIN0 rests on lane A's unreviewed §23); the n² omission (harmless in NCR, **not** in §31.3 (R2)); bb9_criteria.md's no-session-constant disclaimer |
| NARROWED | §27's pre-registration value (file order only; K_f and c_w already derived — [RBA2-fix] P1's standard); Proposition BFT5-red's (G♯-patch^Ω) narrowing (chain half only, no ‖B^r‖_D, slice change unproven) → ARGUED; bb9b's B0 (near-zero power — it passed on the buggy energy) and B3 (tests the EL equation, not the straightening, since ψ_1 ≡ 0 at T = 1); **bb9b A3 (tautology: the transpose of the script's definition of Q), B4 (forced), B5/B6 (dependent) — so the funnel inside the ρ-recursion is tested nowhere** (Part P) |
| WRONG | §31.1 *Reading* 2's "λ's level-k-root part is TE's tent data" (refuted by the same lane's §36.1); (BFT-5_E) clause (c) recorded as PROVEN at the background Z(V_k) |
| NOT-VERIFIED | the identification of λ^{Γ_E}_{C0#}(p) with lane A's σ (which is the S_E → S^♯ transport) |

# Tally (lane B session 10; nothing counted in PROOF)

| verdict | items |
|---|---|
| CONFIRMED | **Lemma W0-use** (checked against BFT_A l.2465-2494 line by line; and use (B) *is* a use of d*j_0 = 0, via ψ_{k−1} = R_k(d*j_0)); **Lemma SPLIT** (including LIN0's hypothesis being vacuous at j = 0); **Lemma DF-cc (i)-(iii)** (double-sum exchange, injectivity, and the i = k−1 add-and-subtract); ξ_i = −ψ_i at every k (and the §37.4 self-correction); **Proposition COF-size** as an inequality in the (Pl-c) class; **Theorem COF** as stated; **(CO-fun) as stated in §31.2 is FALSE without (CC-0)** (S10-F4 genuinely occurs); **Proposition COF-res's identity**; **Remark MASSLESS / S10-F5** (the factor T); **Proposition GT-split** (the pin is pointwise: χ^5_X(c_X) = 1); **Proposition GT-loc as an inequality** (ΓT-op (d) applies to any level-0 1-form, so Y^p_{*,0} is in its class; constant 20 verified); **Proposition GT-ell** and its derived (NEUT-box); **§36.5 (iv)**; (TENT-Q) = (NEUT-box) for the corrected source S^E_0; bb10 ALL PASS and that its tests test what the table says; bb10c's script provenance (K = 3 only), C4 (a) being the inequality COF-size uses, and the handling of the C4 (b) FAIL |
| CONFIRMED-WITH-FIX | **Proposition GT-attr's arithmetic** (n²L^{−3(k−l)}σ = L^{3l−k}σ: the k-growth is in the charge factor) — but not its conclusion; the (NEUT-box) name collision; bb10c's missing post-hoc label; §37.2's table against §37.4's "no check supports the size claim" |
| NARROWED | **Theorem NCE (i)** (residual half k-uniform; curvature half O(k)); §36.5 (ii)'s reduction (inherits S10-10); "at every critical point" as an a-posteriori statement where the contraction needs the ball |
| WRONG | **Corollary COF-crit** (k-uniformity does not follow from the quoted inputs; ≈ 25(k−1) at best); §36.5 (v) / FOR OTHER FILES 1 ("already answered") |
| NOT-VERIFIED | §36.2's headline "(GT-sup) is not a spike-support question" (the sufficient condition (Y-sup^loc) is probably false at the core); [S10-fix 2]'s "expected TRUE"; §35.7/§36.5 (ii)'s "every other term bounded as in Theorem COF" for D ≠ 0; §37.1's claimed two-stage criteria write |
| ZERO / FORCED DISCRIMINATING POWER (Part P) | **bb10 A4** ("the central test" — forced by A3 plus the transposed definition of Q), **A1** (tautology, disclosed), **A7 (b)** (vacuous, disclosed), **A6** and **B0** (forced), **A2** (≡ bb9b A2); unforced outcomes: only **A5**, **A7 (a)**, **A8** (loose), **B1** (over the Hessian), and bb10c's **C4**, **C5**. No check reaches §35.6 (no rows in the model; k−1 ∈ {1, 2}) |

---

# (c) Is (Res-Hölder) closed at m = 0?

**Partly, and the two halves must be stated separately.**

1. **Theorem RHT-cc: YES, closed at m = 0** (and at m > 0 with c_w ≤ 14), for **every** Setting LIN^cc source and every
   critical point of **E_src**. This is a linear statement with no reference to 𝔉_k, and critical points of E_src exist
   for every composite-co-closed source by Lemma FG (i), so it is non-vacuous and usable. I rebuilt its two inputs
   (Lemma RT-cc, Lemma FT) and its arithmetic (K_f). **This is the genuine result of session 9.** It closes the
   level-wise-co-closedness restriction that [RBB6-fix RS6-1] left in place.
2. **Corollary RHT-V (the non-co-closed BCH₂ remainder V_l): closed as the (H-inv+) increment, at critical points of
   𝔉_k, for every gauge fixing — NOT closed as the absolute bound N_res ≤ C_Vη².** The η² form needs
   ‖r^c_{k−1}‖_∞ ≤ ‖x‖_inv ≤ G_Rη² for the same non-co-closed rows, i.e. (H-inv) for them, whose curvature half is
   exactly the item Part J refutes at k-uniform level. So EP-F4 at m = 0 is closed in the form (Res-Hölder) actually has
   in this program (an increment over the invariant norm, Corollary RH-inv), and the η² headline is conditional.
3. Everything above is at **m = 0 and the trivial background**; the weighted form adds the m > 0 caveats lane B already
   records (Theorem RHT_m-cc plus lane A's DX_m, DB_m, OPEN).

# (c′) Does Theorem NCE have content?

**Yes, but less than the statement reads, and its headline uniformity is wrong.**
- It has content in the logical sense: no circularity. Theorem COF is quantified over **sources** and is non-vacuous
  without any critical point of 𝔉_k; (CC-0) is a hypothesis on the source, not a smuggled existence assumption; nothing
  in the proof uses existence or uniqueness in the ball, so BFT-0 is not assumed.
- It has content in the mathematical sense: the residual half is genuinely k-, T-, Γ-uniform at critical points, and the
  Γ-uniformity is exact rather than estimated.
- It does **not** have the content claimed: the curvature half carries the factor k (S10-6), so "with constants
  independent of k and T" fails; and the statement is an a-posteriori regularity statement about a fixed point, whereas
  the contraction that constructs the fixed point needs the ball version, which §36.5 (ii) correctly leaves open.
- Its instance set is conditional on a critical point existing — which is BFT-0's job — so the theorem is best read as
  *"if the contraction has a fixed point in the ball, its gauge-invariant residual data obey k-uniform bounds, and its
  curvature data obey bounds with a factor k"*. That is worth having. It is not "(NC-Γ) for Γ_E is complete at the fixed
  point".

# (d) Adjudication of session 10 against session 9 on (CO-fun)

**Session 10 wins, cleanly, on both of its claims** — see Part O. §31.2's diagnosis ("the funnel pieces are co-closed only
collectively, so they cannot be fed into Theorem W0 one at a time") is wrong twice over: the funnel is not a source and
never enters the dual pairing, and the source slots that **are** superposed are each composite-co-closed. And (CO-fun) as
§31.2 states it is false, by a point pairing at the level-k roots that the source classes do not bound.
**(CC-0) is the right hypothesis, not a convenient one**: it is equivalent to ψ_{k−1} = 0, i.e. to the top residual being
co-closed, which is exactly the hypothesis Theorem W0's own step 3 uses, and Lemma CD (i) supplies it at critical points
as an identity of level-0 functions. There is no circularity.
**But session 10's win does not extend to Corollary COF-crit.** The over-reach there has nothing to do with (CC-0): it is
one invalid substitution of a per-level bound for a class norm, and it reinstates the factor k that the same session's
§36.5 (iv) says still stands. Session 10 should be credited with the structural result (Theorem COF) and corrected on its
specialisation.

# (e) The biggest live wall

**The level-count loss in the level-0 image of the non-co-closed plain remainder rows — the factor k.**

It is upstream of everything these two sessions named. Grant (TENT-Q), (NEUT-box) and (Y-sup^loc) in full, and the
curvature half of (NC-Γ)_cc **at a critical point, at m = 0, at the trivial background** still carries ≈ 25(k−1)η²,
because π_0(C(j)) ≤ Σ_{l<k}π_l(ĵ_l) has no decay factor and the rows have no level decay. Three independent records say
the same thing in three vocabularies: BFT_A [RBA2-fix] B3 ("the entire level-count loss sits in the level-0 image"),
REVIEW_BFT_A_S8 S8-13 ("the level sum stops being geometric, and the factor k returns"), and BFT_B §36.5 (iv) ("the
factor k … untouched"). The named object that would close it is lane A's **(SPD)/(W2)**, level decay of the Ran Q^T
component of a remainder row (BFT_A l.830-831, OPEN) — or a rough/smooth split of the non-co-closed rows through
(G♯-rough). That is now the highest-value missing object in either BFT lane, and it is cheaper to state than (PW-ii).

Second, and separable: **(Y-sup^loc) is probably false**, so the §36.2 route to (GT-sup) is likely a dead end at the core
of the response, and the live question there is the one §36.4 isolates — box-local neutrality of D^⊥(S), i.e. whether
lane A's Proposition OB is literally (NEUT-box). Lane B's own offer of "one session's worth of work" on that
(§37 FOR OTHER FILES, BFT_A item 6) is the right next move, and it should be taken **after** RS10-1 is entered, because a
negative answer there plus the factor k would together force lead decision D1's alternative (arranging the contraction to
meet only composite-co-closed sources) rather than merely recommending it.
