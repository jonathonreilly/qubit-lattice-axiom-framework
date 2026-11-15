Reviewer model: claude-opus-5-5

# GSHARP55 — (G♯_0-field): pin, need, attack (Opus 5.5 worker)

UTC start: 2026-10-28 23:45 UTC (from `date -u`, 23:45:07)

## PRE-STATED (written before any derivation; statements only)

Targets.
- T1 (pin). State (G♯_0-field) exactly as the sources give it (RTARGET.md §33, located by string; NBG_B.md's
  pinned form), with every quantifier (k, T, X_0 uniformity; which norm; which configuration; which sources).
- T2 (re-derive, do not inherit). The earlier decomposition in NBG_B / NBG_ADJ:
  "(G♯_0-field) = [multi-level per-level-slice gap] + [(G♯_0-fine)], with (G♯_0-fine) OPEN because the
  K ≠ 0 alias symbol is not analytic in a strip". Verdict per piece: CONFIRMED / NOT-VERIFIED / REFUTED.
- T3 (need). Do the consumers of BFT-5 clause (b) read the FIELD components B_i in the X_c norm, or only
  gauge-invariant quantities (curvatures dB_i) plus a gauge-fixing estimate already banked? If the field half
  is needed, the weakest consumed form.
- T4 (attack). Prove the needed form, or reduce it to named inputs, or locate the exact step where a K ≠ 0
  alias obstruction (if real) bites.
- T5 (Codex). Agree/disagree, explicitly, with each Codex verdict used (CODEX_REVIEW_GAPZ, CODEX_REVIEW_NBG2,
  and any other I lean on), reading the files as they are on disk now.

What would count as a refutation.
- Of the decomposition (T2): the field bound does not reduce to the two named pieces (a missing third term, or a
  piece that is not implied by / does not imply what is claimed); or the "alias symbol" is in fact analytic in a
  strip (an explicit continuation exhibited); or the non-analyticity, though true, is not what blocks the bound
  (the bound holds or fails for a different reason).
- Of "the field half is needed" (T3): every consumer of clause (b) can be fed by gauge-invariant quantities plus a
  banked gauge-fixing estimate, with file:line evidence for each consumer. Of "the field half is NOT needed": one
  consumer that reads ‖B_i‖_{∞,m} (or ‖B_i‖ in an equivalent weighted sup norm) in an essential way.
- Of any bound I claim (T4): an explicit configuration (finite torus or Z^4, exact arithmetic) violating it
  uniformly in the stated quantifiers, or a step whose constant depends on k, T or X_0.
- Of my own verdicts generally: a wrong CONFIRMED is worse than an honest NOT-VERIFIED; every numeric gate gets
  checks/gs55_*_criteria.md before its script, exact rational arithmetic only.

Numeric checks: none run (stated after the work, not pre-registered as a target). Every claim below is either exact
linear algebra written out in full, or a composition of already-reviewed analytic theorems whose load-bearing steps I
re-derive in the text. No new number changes a decision, so no `checks/gs55_*` file was created.

---

## 0. Bottom line (each item has its own section below)

1. **Pin (§2).** RTARGET §33 states (G♯_0-field) only in words (l.605): "the configuration version in ||·||_{X_c}". NBG_B §3
   writes it out faithfully, but the source statement has four defects. (i) The slice "h^{(i)} = 0 with Feynman terms"
   (l.599-600) is never defined as an operator. (ii) The constant list "(L, κ_±, m, α)" (l.601) omits θ, and every proven
   route needs 0 < α < θ. (iii) The inequality is never displayed. (iv) Its two named consumers inherit the per-level slice by
   citation, not because they need it.
2. **The field half is not an independent obstruction (§5).** On the lane's single slice S_E (lead decision D1), the field
   components of every trivial-chain response are bounded by that response's gauge-invariant data alone. This is BFT_B
   Theorem EP-rec + Theorem EP-opt + Corollary EP-lin, CONFIRMED in REVIEW_BFT_B_S5 B.5-B.7. I re-derived the load-bearing
   steps (§5.1). Consequences:
   - (a) **RTARGET's (G♯_0-field) holds on S_E at m = 0 for 0 < α < θ < 1, in RTARGET's own source norm: PROVEN as an
     implication** (Theorem GF-E′, §5.2). Every input has been CONFIRMED by a lane review: LIN0 (= W0 + GU + BL-4/5),
     RHT/RH-inv, EP-rec, EP-opt, Prop SM. Lane B already wrote this down in its session 6: "Corollary EP-lin gives
     (W-lin-Π) for S_E from (H-inv) alone" (BFT_B l.2509-2510). The ledger's "not attempted" / "paper-scale" status is stale.
   - (b) **BFT-5 clause (b)'s field half (R1), at Z = 1 and m = 0, on the composite-co-closed class: PROVEN as an
     implication** (Theorem GF-E, §5.2): ||x_E||_{𝔐^∇} ≤ C·N(S). Inputs: CC-INV (S26-banked; Codex CONFIRMED in
     CODEX_REVIEW_TOPCC), RHT-cc (CONFIRMED twice) and EP-rec/EP-opt.
     - COFUN_CC §6.2 says "(R1) … needs (G♯_0-field) … CC-INV gives nothing here … the wrong direction". **REFUTED**: EP-rec
       is the right direction.
     - Codex TOPCC grades "Field components — NOT-VERIFIED". That is right about CC-INV alone, and wrong as a status of (R1).
   - (c) **At m > 0 the field half adds nothing (§5.3).** EP-rec's reach is finite and absolute (audited here), so the
     weighted field half reduces to the weighted gauge-invariant half plus N_res,m (RHT_m-cc CONFIRMED). What is left is
     exactly (R3). For RTARGET's divergence-form class it is exactly the weighted Theorem GU: its sup part needs lane A's
     DX_m and DB_m (OPEN), and its Hölder part is not written.
   - (d) **At Z ≠ 1 the field half is the Z-covariant reconstruction (EP-rec)_Z**, the linear part of lane B's (N1). It
     belongs inside (R2). Outline ARGUED (§5.4).
   - Net, against the lead's three open items: **(R1) is absorbed.** It is CLOSED at Z = 1, m = 0; it equals (R3) at m > 0;
     and it sits inside (R2) at Z ≠ 1.
3. **The decomposition (§3).** The claim was "(G♯_0-field) = [multi-level per-level-slice gap] + [(G♯_0-fine)], with
   (G♯_0-fine) OPEN because the K ≠ 0 alias symbol is not analytic in a strip". **REFUTED in every part.**
   - The "=" is at most an order of work, and neither piece is necessary for the form that is consumed.
   - Under PROOF's own gloss ("PG at every level with the effective energies E_i, via E-low"), the "gap" is LINEAR_PACKAGE
     Prop 6.4 / Lemma N5-coer, which is PROVEN.
   - (G♯_0-fine) at m = 0 is LIN0 = W0 + GU, which is CONFIRMED.
   - The K ≠ 0 alias factors ARE analytic in a strip. PROOF's own N2-exp proof shows it (l.3030, l.3058), and §3.4
     re-derives a strip of width > 1, uniformly in n.
   - The obstruction PROOF actually recorded (l.3369-3372) is different: per-offset alias sums at short distance are not
     summable uniformly in n. That is the sup-norm Calderón–Zygmund effect G0-F2, which the Hölder norm and lane A's
     real-space route remove. **The alias "obstruction" bites nowhere on the live route.**
4. **Clause (b) as written is false for field components (§4.2).** BFT_B §32.1 (b) says "these bounds are independent of
   the gauge fixing". I give an explicit family of admissible gauge fixings whose responses have unbounded field norm and
   identical invariant outputs. Fix: state (b) in the orbit norm ||[x]||_𝔐 := inf_{g∈𝒢_0}||x + g||_𝔐, which is
   gauge-free by construction and equivalent to the S_E norm up to the constant C_Π (Theorem EP-bd).
5. **The per-level slice (§5.5).** It is an admissible gauge fixing (Lemma PL-adm, PROVEN-HERE), but no live route consumes
   it. The transfer S_E → per-level slice in X_c is ARGUED, and it needs only the per-level gauge-fixing inverses, not a
   "physical gap". I also argue that 𝔐^∇ is not expected to be uniform in that slice (block-centre spikes), which is one
   more reason the per-level form is the wrong target.

---

## 1. Read record, and symbols pinned (systemic defect 1)

**Read (located by string; ranges as read):**
- REVIEW_BRIEF_55.
- PROOF.md: header and [S26-BANKED]; l.118-170; l.3380-3420; l.3580-3740; l.3020-3062; l.3360-3376; l.5084-5115;
  l.5380-5460; l.6790-6960.
- RTARGET.md l.560-680 and l.1020-1130.
- COFUN_CC.md l.1-145, §5 head, §6 (l.405-500).
- NBG_B.md l.1-430, 498-605; NBG_ADJ.md l.140-200, 280-400.
- CODEX_REVIEW_GAPZ.md and CODEX_REVIEW_NBG2.md, all.
- CODEX_REVIEW_TOPCC.md: disposition, §5 (assembly), "Exactly what may be banked". It appeared at 00:01Z while I worked,
  and its last lines look complete.
- CODEX_REVIEW_HINT.md: its 9 lines are a PRE-STATED block only. Unfinished, and not used.
- LINEAR_PACKAGE.md l.1-500.
- BFT_A.md l.18-47, 230-275, 437-575, 1101-1166, 1688-1760, 2510-2545, 2600-2627, 2826-2845, 3125-3150.
- BFT_B.md l.1586-1640, 2016-2090, 2126-2262, 2492-2530, 2612-2626, 3580-3612, 3820-3860.
- REVIEW_BFT_B_S5 l.150-245; REVIEW55_BFTB l.222-240, 352-370; REVIEW55_LEAD l.115-135; REVIEW_BFT_A_S7 (verdict lines).
- FLATZ.md (an abandoned draft; nothing in it is a result).
- SF.md l.676-730, 880-900; PLAN_S26.md, all.

**Collisions that bear on this target (each checked by file:line):**
- **"𝔐-pair"** names three different norm pairs:
  - (P1) RTARGET §33's (Y, Y_α; X_c, X_c + [f_0]_{α,m}) (RTARGET l.592, l.599-600);
  - (P2) REVIEW_S22's 𝔐, which is described but not defined (REVIEW_S22 l.392-399);
  - (P3) lane A's (𝔐^∇, 𝒴^∇) (BFT_A l.36-41).

  BFT_B §32.1 (b) (l.3831) says "SF/RTARGET §33's 𝔐-pair", and COFUN_CC §6.2 glosses that as "(field components, Hölder
  curvature)". Everything below is proved in 𝔐^∇, which dominates X_c: ||x||_{X_c} + [f_0]_α ≤ 3||x||_{𝔐^∇}, because
  |(dx_j)^c| ≤ 2|∇^cx^c_j| componentwise and [f_0]_α ≤ 2[∇^cx^c_0]_α.
- **One object under four names.** "The trivial-chain composite-slice inverse in the 𝔐-pair" appears as:
  - (W-lin-Π) for S_E (BFT_B §12.1, l.1612);
  - (G♯_0-field^∇) (BFT_A l.266, l.559);
  - NBG_ADJ's "fourth object" (A6; PROOF l.166);
  - COFUN_CC's (R1) at Z = 1.

  RTARGET's (G♯_0-field) is the same estimate on a different slice and in the weaker X_c norm.
- **C_E** names three constants: EP-int's absolute constant (BFT_B §16.2); Lemma LE's √192 + 10⁴C_K (BFT_A §28.3); and
  LINEAR_PACKAGE Thm 2.6's 1.2·10⁸. I write **C_int** for EP-int's.
- **Λ** names four objects: the S_E gauge function Λ(x) (BFT_B §15.0); the gauge-parameter space Λ_0; the residual group
  Λ_res; and lane A's root-to-root line sums Λ_i / Λ_root (BFT_A §13.11). I write **Λ_E(x)** for the first and **H_root**
  for the last.
- **m** is both the weight rate and, inside BFT_B §19.3 and §31.2, a depth index "m = k − 1 − i". I write the depth as
  **q := k − 1 − i**.
- **θ** here is always the class exponent: RTARGET l.587-588's θ, which is BFT_A §7.2's θ and COFUN's θ_c. It is never
  REVIEW_S22's θ_w.

**Fixed notation (the lane's, located):**
- 𝒢_0 = {Dλ : λ a level-0 function vanishing at the level-k roots}, with Dλ := (d ev^{(j)}λ)_{j<k} (BFT_B l.1589).
- 𝓑 = H is the chain Hessian at the trivial chain, with Ker H = 𝒢_0 on {x_k = 0} (BFT_B §16.5 kernel step; Lemma FG (i)).
- ||x||_inv := max_j[||f_j||_∞ + [f_j]_α + L^{k−1−j}||r^c_j||_∞] (BFT_A l.462).
- N_res(x) := Σ_{0≤i≤k−2}||r_i||_{C^{1,α}} (BFT_B §15.0).
- N(S) := ||G^c_0||_∞ + [G^c_0]_α + ||j^c_0||_∞ + ||j||_Pc + ||G||_Y + ||s||_R (COFUN_CC §1).
- (cc) means composite co-closedness, Ξ^TS = 0 (BFT_B §27.1).
- Both ||x||_inv and N_res are 𝒢_0-invariant: residuals by root covariance, curvatures because d∘d = 0.

---

## 2. T1 — (G♯_0-field), pinned from the source

**Source (RTARGET §33, header at l.572; the lead's "l.586-605" is the body).**
- Setting SC with level-wise sources j_l = d^*G_l, each "a co-closed, zero-mean level-l 1-form" (l.575-579).
- Level weights ω_0 = 1, ω_l ≥ 1, "intended choice ω_l = L^{θ(k−l)} (θ ∈ (0, 1])" (l.587-588).
- ||G||_Y := max_lω_l||G_l||_{∞,m} and ||G||_{Y,α} := ||G||_Y + [G_0]_{α,m} (l.592).
- Data norm ||B_k||_{D,m} (l.593-594).
- "configuration (for B-NA-red): ||B||_{X_c} := max_i(||B_i||_{∞,m} + ||dB_i||_{∞,m}) for a stated gauge-fixed
  representative (the abelian per-level slice h^{(i)} = 0 with Feynman terms); its Hölder version adds [f_0]_{α,m}"
  (l.599-600).
- "With constants depending only on (L, κ_±, m, α), uniformly in k ≥ 1, T and X_0, for m < m_*′ (some stated loss)"
  (l.601).
- "(G♯_0-field) the configuration version in ||·||_{X_c} (needed by B-NA-red; pre-stated, attempted only if the first two
  are done)" (l.605).

Outcome recorded: "(G♯_0-field) not attempted" (RTARGET l.654; PROOF l.3654).

**NBG_B §3's assembled form (NBG_B l.122-132): CONFIRMED as a reading.** It displays
||B||_{X_c} ≤ C(||G||_{Y,α} + ||B_k||_{D,m}), for the critical configuration in the per-level slice, with C = C(L, κ_±, m, α)
uniform in k, T, X_0. That is what RTARGET's words mean by analogy with (G♯_0-fine) (l.604). I read "the Hölder version"
as adding [f_0]_{α,m} on the left.

**Four defects of the source statement.** None is a defect of NBG_B's transcription.
- **(P-1) The slice is not defined.** RTARGET and PROOF (B-NA-red [R1314-fix] (2), l.3404) describe it in words only.
  §5.5 supplies the operator Γ_PL and proves it admissible.
- **(P-2) The constant list is incomplete.**
  - Every proven route has θ-dependent constants.
    - GU's level sum is Σ_t(t + 1)²L^{−(θ−α)t} (BFT_A l.2530).
    - RHT's sums are 1/(L^{θ−α} − 1).
  - Every proven route needs **0 < α < θ**: GU and LIN0 (BFT_A l.2530, l.2541), CC-INV (COFUN_CC l.415), RHT-cc
    (BFT_B l.3604).
  - In lane A's pair, α > θ is proven FALSE for residual-type sources (BL-5 (c), BFT_A l.534-538).
  - For RTARGET's divergence-form class and RTARGET's X_c (whose Hölder term is f_0's only), failure at α ≥ θ is
    **NOT-VERIFIED** here.
  - So the quantifier list "(L, κ_±, m, α)" with θ free matches no proven route. It must read
    C = C(L, κ_±, m, α, θ) with 0 < α < θ.
- **(P-3) No inequality is displayed** (only "the configuration version").
- **(P-4) Neither consumer needs the per-level slice.** B-NA-red's reduction is proven for "a linear chain gauge slice 𝒮
  with a Feynman term … on its residual group" (PROOF l.3385-3388); the slice is a parameter of NA-IFT. SF (a5-G♯) names
  the per-level slice (SF l.680-681), but SF's own [RSF2-fix GP-1] says the natural slice is the trivial slice at x^r
  (SF l.890-893).

---

## 3. T2 — the decomposition, re-derived rather than inherited

PROOF.md was being edited while I worked: its strings moved by +4 lines between 23:50Z and 00:20Z. PROOF line numbers
below are as of **00:20Z** and are given with their locating strings.

### 3.1 The claim and its sources
- **NBG_ADJ §2.4 (l.164-177):** "(G♯_0-field) = [multi-level per-level-slice gap] + [(G♯_0-fine), a Campanato/Hölder
  bound]", and "(G♯_0-fine) is OPEN for a reason that has nothing to do with any gap: PROOF l.3612, *the source-to-f_0
  symbol with K ≠ 0 aliases has not been shown analytic in a strip*". In its graph (NBG_ADJ l.350-357) both nodes are OPEN.
  The claim was copied into PROOF [S25-fix 5] (PROOF l.≈156-165) and SESSION25_RESULTS l.616, l.626.
- **Where NBG_ADJ took it from (PROOF, current lines):**
  - "(G♯_0-fine) is also needed for (G♯_0-field) and for (R♯)" (l.3657);
  - "(G♯_0-field): not attempted. It needs, in addition, the abelian multi-level (per-level slice) physical gap, which is
    not PG^{(k)} … see Proposition NA-lev (c) for the one-level version" (l.3658-3659);
  - the S15 order of work, "(G♯_0-field): the abelian multi-level per-level-slice gap (PG at every level with the
    effective energies E_i, via E-low), then the Hölder field bound" (l.5113-5114).
- **The root:** B-NA-red's failure mode BNA-F3 (session 14, PROOF l.3428-3433). There the per-level slice is *asserted*
  to be "a smooth complete gauge … its (G♯) contains a multi-level physical gap of PG/PG^{(k)} type". The smoothness of
  that slice was never proven. Lane B later built a gauge that is *provably* smooth and complete, S_E: Theorem EP-bd shows
  Π_E is bounded on 𝔐^∇ (BFT_B §16.4), and §16.4 contrasts it with the axial gauge's L^{k(1−α)} loss.

### 3.2 The "=": REFUTED as an identity; NOT-VERIFIED as a sufficiency; the gap piece is not necessary
- None of the sources displays an implication. l.5113 is an order of work and l.3658 is a "needs". So the "=" is at most a
  proposed route. I agree with CODEX_REVIEW_NBG2 F13, row 1 ("An order of work is not the sufficiency theorem":
  NOT-VERIFIED), and with F10 (a decomposition of a goal is a list of obligations).
- **Necessity is decided by construction.** Theorem GF-E′ (§5.2) proves the S_E form of (G♯_0-field) at m = 0 from
  ||x||_inv + N_res + EP-rec + EP-opt. EP-rec is a reconstruction — no inverse and no coercivity — so **no slice gap of any
  kind enters**. The curvature input ||x||_inv does contain (G♯_0-fine)'s content (LIN0 ⊇ W0 + GU). The decomposition
  that is correct on the slice actually consumed is therefore

  > (G♯_0-field)_{S_E} ⟸ (H-inv) [= (G♯_0-soft) + (G♯_0-fine) + the curvature tower] + (Res-Hölder) [N_res] + EP-rec + EP-opt,

  and at m = 0 every input of it has been CONFIRMED by a lane review (§5.2).
- The per-level-slice form is a different statement because the slice differs. It is related to the S_E form by a gauge
  transfer, not by a gap (§5.5).

### 3.3 "The multi-level per-level-slice physical gap": two readings, and on neither is it an open obstruction
- **Reading A — PROOF's own gloss** (l.5113-5114: "PG at every level with the effective energies E_i, via E-low").
  - This is LINEAR_PACKAGE Prop 6.4 (NA-lev (c), LINEAR_PACKAGE l.352-354): E_i(A) + (κ_i/2)||QA||² ≥
    min(c_E, κ_i/2)·c_1||A||²_B on the one-level Phys, uniformly in i, k, T. PROVEN, and in the reviewed frozen package.
  - In Feynman form it is Lemma N5-coer, O_i ≥ γ_i on H_0 uniformly in i, k, T (PROOF l.5392). It was CONFIRMED with
    Theorem N5-triv by REVIEW_S18_S19 (PROOF l.4802).
  - **On reading A the "gap" is PROVEN, so NBG_ADJ's node "[OPEN; NOT PG^{(k)}]" is REFUTED.**
- **Reading B — one joint lower bound for the whole k-level chain Hessian on the per-level slice.**
  - No inequality, norm or level normalisation is stated for it anywhere. I searched for "multi-level" in PROOF, RTARGET
    and LINEAR_PACKAGE: PROOF l.406 and l.3432 name it, and l.3658 and l.5113 use it, but none displays it.
  - With no statement to check, it is **NOT-VERIFIED** (undefined), not OPEN.
  - Two remarks on reading B:
    - An ℓ² gap would not by itself give sup/Hölder field bounds uniformly in n, since one coarse cell holds n⁴ fine links.
    - Composing per-level inverses is the route that REVIEW_S22's anti-circularity clause excludes from the BFT proof
      (REVIEW_S22 l.422-423: "may not use the per-level covariances C^{(j)} as Newton inverses").

### 3.4 "(G♯_0-fine) is OPEN because the K ≠ 0 alias symbol is not analytic in a strip": REFUTED, for three independent reasons
**(i) The status is stale.**
- In RTARGET's own source norm (weighted sup at levels ≥ 1, Hölder at level 0), at m = 0 with 0 < α < θ, (G♯_0-fine) is
  **Corollary LIN0** (BFT_A §28.8, l.2533-2545). Its parts:
  - Theorem W0 for level-0 sources, including (LED-src), which Lemma LE closes.
  - Theorem GU for levels ≥ 1. GU uses only weighted sups of G_l there ("no Hölder norm of G_l used", BFT_A l.2241,
    l.2514). CODEX_REVIEW_TOPCC independently makes the same observation (its Ñ_Σ remark).
  - BL-4/BL-5 for data.
- All CONFIRMED in REVIEW_BFT_A_S6 (W0 l.23, GU l.24, LIN0 l.25-26).
- Weighted and at level 0: Theorem W0_m for 0 ≤ m ≤ m_Y, CONFIRMED (REVIEW_BFT_A_S7 l.48, l.314).

**(ii) The source is misquoted, and the alias factors are in fact analytic in a strip.**
- PROOF l.3656 says the symbol "has not been shown analytic in a strip". That is a statement about what is known.
  NBG_ADJ and [S25-fix 5] turned it into "not analytic".
- PROOF's own Theorem N2-exp proof (P4) shows that the K ≠ 0 alias denominators do not vanish on the strip:
  - "For K ≠ 0 some |θ_α| ∈ [π, πn], so φ^{(K)}(x) ≥ 4n²sin²(π/2n) ≥ 9 (n ≥ 3)" (l.3034);
  - "Re sin²(a + ib) ≥ sin²a − sinh²b gives |φ^{(K)}(z)| ≥ φ^{(K)}(x) − 4η²cosh²η" (l.3062).
- **Re-derivation (PROVEN-HERE; elementary; it widens (P4)'s strip and nothing below uses the widening).**
  - Notation of LINEAR_PACKAGE §1.5: φ_α(z) = 2n²(1 − cos(z_α/n)) = 4n²sin²(z_α/(2n)), and
    φ^{(K)}(z) := Σ_αφ_α(z_α + 2πK_α). Take K ∈ {0, …, n − 1}⁴ ∖ {0}, z = x + iy with x ∈ (−π, π]⁴, and n ≥ 3.
  - **Real part.** Some α has K_α ∈ {1, …, n − 1}. Then θ_α := x_α + 2πK_α ∈ [π, 2πn − π], so
    sin²(θ_α/(2n)) ≥ sin²(π/(2n)). Hence φ^{(K)}(x) ≥ 4n²sin²(π/(2n)). This is increasing in n and equals 9 at n = 3.
  - **Imaginary part.** Re sin²(a + ib) = sin²a·cosh²b − cos²a·sinh²b ≥ sin²a − sinh²b. Also
    4n²sinh²(y/(2n)) ≤ y²cosh²(y/(2n)), since sinh t ≤ t·cosh t.
  - So if |y_α| ≤ η for every α: **Re φ^{(K)}(z) ≥ 9 − 4η²cosh²(η/6)**. At η = 1.4 the subtracted term is
    7.84·cosh²(0.2334) ≤ 7.84·1.0554 < 8.28 < 9.
  - Conclusion. Every K ≠ 0 alias factor 1/φ^{(K)} is analytic on {|Im p_α| ≤ 1.4}, with bound
    1/(9 − 4η²cosh²(η/6)), uniformly in n ≥ 3 and K. That strip is 36 times wider than m_*′ = 0.0384.
  - The K = 0 alias's 1/φ is cancelled exactly by the screening identity β − κ|W|² = φR (SRC-id, LINEAR_PACKAGE Lemma 6.5;
    EXP-id). So for each fixed n, **each entry** of the source-to-f_0 Bloch symbol — a finite sum over aliases — is analytic
    on |Im p| < m_*′.

**(iii) The obstruction PROOF actually recorded is a failure of summation, not of analyticity.**
- SRC-id's own scope note (PROOF l.3373-3376): "the K ≠ 0 aliases of dΔ^{-1}j are the short-distance Biot-Savart kernel
  (|x|^{-3}), whose per-offset alias sums are not absolutely summable uniformly in n, so the fine-level bound needs a
  real-space localisation (a finite-range split of Δ^{-1}), not done here."
- That is exactly failure mode G0-F2 (RTARGET l.611-612): no sup-norm-only bound for f_0. It is the Π_ex |x|^{-4} kernel
  and COMP-F1's log n, measured in check ba1 A1 (BFT_A l.279-281). It is the reason the norm is Hölder.
- The real-space localisation PROOF asked for is LES-div + Lemma LE inside Theorem W0 (BFT_A §28.3-28.5), CONFIRMED.

**So where would the alias obstruction bite?** Only on the symbol route for fine sources, in sup norm, within one coarse
unit. There it is an obstruction to *that route*, not to the theorem: the log n is real in sup norm, and the Hölder norm
removes it. No live consumer goes through the source symbol, since W0, GU, COF and CC-INV are real-space or duality
arguments.

**Verdict on the lead's question: the K ≠ 0 alias obstruction is not real as stated. Its true content (G0-F2) is resolved,
and it bites nowhere on the live route.**

---

## 4. T3 — who consumes clause (b), and what they actually need

### 4.1 The consumers (located)

**1. The composite contraction for BFT-0/1/2** (Theorem BA via (H-lin^∇); BFT_A §3.9 l.205-230, §3.11 l.258-272;
REVIEW_S22 l.422-423).
- What it reads: the trivial-chain inverse applied to the remainder rows, in 𝔐^∇. The rows are (cc) at critical points
  (Lemma CD, as corrected in [S26-BANKED]).
- Field components needed: **yes.** The rows (BCH₂, BA-6) are functions of the potentials, and (CL-2) needs ∇-control of
  the potentials at every level (BA-6; BFT_A l.271-272).
- Slice: **S_E** (lead decision D1, BFT_B l.2856; CONFIRMED by REVIEW_BFT_A_S8, PROOF "D1 (one slice, S_E)").

**2. B-NA-red** (the IFT for the SU(N) background; PROOF l.≈3386-3420).
- What it reads: (G♯), i.e. ||𝓛^{-1}||_{Y→X} and ||𝓛^{-1}N||_{D→X}, plus their weighted forms.
- Field components needed: **yes.** The BCH remainder has size |x||dx| in own units (BNA-F2).
- Slice: any linear slice with (FP♯′) — "Let 𝒮 be a linear chain gauge slice …" (l.3389-3390). [R1314-fix] (2) fixed the
  per-level slice by choice (l.≈3404), justified only by BNA-F3's unproven smoothness claim (§3.1).

**3. SF (a5-G♯) → HIST Theorem A5** (SF l.680-686; REVIEW_S22 l.427).
- What it reads: (G♯) at real critical chains, in the §33 pair.
- Field components needed: **yes.**
- Slice: the statement says "per-level covariant slice through ψ^r". But SF's own [RSF2-fix GP-1] (l.890-893) says the
  natural slice is "the TRIVIAL slice at x^r" and that changing slice needs a lemma. The slice is a choice.

**4. G-pert / (G♯-patch^Ω) / HESS-rel** — the background transfer (R2); SF l.697-705; BFT_B §32.2; CODEX_REVIEW_NBG2 F8.
- What it reads: the trivial-chain inverse applied to the range of a perturbation, which is a general (non-cc) source.
- Field components needed: **yes, but they reduce.** On S_E the response to a general source y is the (cc) response to
  Π_E^Ty (§4.3). Its field half is therefore again a gauge-invariant question — clause (c)'s (NC-Γ)/(GT-sup) — and not a
  field question.

So **every consumer needs field components**, because every nonlinear remainder is a function of the potentials. Each needs
them **in one fixed slice in which its nonlinear problem is posed**. None needs a particular slice, and the slice the lane
has decided on is S_E.

### 4.2 Clause (b) as written is false for field components; the correct gauge-free form

BFT_B §32.1 (b) (l.3831): "the response x = H_E^{-1}S obeys the (G♯) bounds in SF/RTARGET §33's 𝔐-pair,
||x||_𝔐 ≤ C_5||S||_{𝔐*}, … and by Lemma FG (iii) these bounds are **independent of the gauge fixing**, so (b) is a
statement about the orbit, not about S_E."

**Proposition GF-DEP (PROVEN-HERE; exact linear algebra).** For field components that sentence is false. Even for one
fixed (cc) source there is no C with ||x_Γ||_{X_c} ≤ C for every admissible gauge fixing Γ.

*Proof.*
- **Gauge fixings.** A gauge fixing is a linear Γ such that ΓD is a bijection of Λ_0 (BFT_B l.3781, "the defining property
  of a gauge fixing"). For (cc) S, the Γ-response x_Γ = 𝓛_Γ^{-1}S is the unique critical point with Γx_Γ = 0 (Lemma FG
  (iii); BFT_B l.3741).
- **The family.** Write Γ_E := Λ_E(·) for the S_E functional. By EP-alg (e) (BFT_B l.2152-2153), Λ_E(Dμ) = −μ for every
  μ ∈ Λ_0.
  - Fix a level-0 plaquette p_0. Put ℓ(x) := (dx_0)(p_0). This is gauge-invariant: ℓ∘D = 0, because d∘d = 0.
  - Fix μ_0 ∈ Λ_0 with Dμ_0 ≠ 0.
  - For t ∈ ℝ put Γ_tx := Λ_E(x) + tℓ(x)μ_0.
  - Then Γ_tD = Γ_ED = −Id, so every Γ_t is admissible.
- **Its responses.** Let x_E ∈ S_E be the response to a (cc) source S, and put x_t := x_E + tℓ(x_E)Dμ_0.
  - x_t is a critical point, since Dμ_0 ∈ Ker H.
  - Γ_tx_t = Λ_E(x_t) + tℓ(x_t)μ_0. Here Λ_E(x_t) = 0 − tℓ(x_E)μ_0, and ℓ(x_t) = ℓ(x_E). So Γ_tx_t = 0, and x_t is the
    Γ_t-response.
- **Blow-up.** Choose S with f_0(p_0) ≠ 0: any source with f_0 ≢ 0 works, with p_0 a plaquette where f_0 is nonzero. Then
  ℓ(x_E) = f_0(p_0)/n² ≠ 0, and
  ||x_t||_{X_c} ≥ |t|·|ℓ(x_E)|·||Dμ_0||_{X_c} − ||x_E||_{X_c} → ∞ as |t| → ∞.
- Meanwhile S, ||x_t||_inv = ||x_E||_inv and N_res(x_t) = N_res(x_E) do not change. ∎

**What is gauge-fixing independent:** ||x||_inv and N_res, by Lemma FG (iii) and 𝒢_0-invariance.

**The correct gauge-free statement of (b)** uses the orbit norm
  ||[x]||_𝔐 := inf_{g∈𝒢_0}||x + g||_𝔐.
It is equivalent to the S_E statement up to C_Π:
  ||[x]||_𝔐 ≤ ||Π_Ex||_𝔐 ≤ C_Π||[x]||_𝔐.
- The first inequality holds because Π_Ex is in the orbit.
- For the second: Π_E is constant on orbits (Π_E(x + Dμ) = Π_Ex, EP-alg (a), (d)). Apply EP-bd (||Π_Ev||_X ≤ C_Π||v||_X
  for every v, BFT_B l.2062) to a near-minimising representative.

So "a statement about the orbit" is achievable, but only with the orbit norm or with the slice named.

### 4.3 The weakest form that is needed

**(F_min).** Let 𝒮 be the consumer's source class (the (cc) rows at a critical point; lane A's 𝒴^∇ classes; data). (F_min)
asks for **one** complete linear slice S, admissible for the nonlinear problem ((FP♯′) near 0), with ||x_S||_{𝔐^∇} ≤ C||S||
for every S ∈ 𝒮.

Take S = S_E:
- At the trivial chain, (FP♯′) is exact: Λ_E∘D = −Id on Λ_0 (EP-alg (e)).
- The nonlinear and background forms belong to lane B's (N1) (BFT_B §40-41, l.4500-4504: "(N1-a) is PROVEN and (N1-d) is
  CONDITIONAL on (N1-nd) alone"). Those are session-24-era statements, PROVISIONAL, and I have not re-checked them; they lie
  outside Z = 1.
- On S_E, for every source y (cc or not), the slice problem 𝓑(u, w) = ⟨y, w⟩ for all w ∈ S_E is the full problem with source
  Π_E^Ty. Indeed w − Π_Ew ∈ 𝒢_0 ⊂ Ker 𝓑, so 𝓑(u, w) = ⟨y, Π_Ew⟩ for all w ∈ X. And Π_E^Ty annihilates 𝒢_0, so it is (cc).
- By EP-opt + EP-rec (§5.1), (F_min) on S_E is therefore equivalent to the gauge-invariant bound ||x||_inv + N_res(x) ≤ C||y||
  for the responses to the projected sources.

**The weakest needed form has no field-specific content: it is (H-inv) + (Res-Hölder) on the consumer's (projected) class.**

---

## 5. T4 — the attack: the field half reduces to gauge-invariant quantities

### 5.1 Proposition FH: on S_E, the field half is a function of gauge-invariant data

**Statement.** At the trivial chain, let x be any configuration with data x_k. This covers every critical point of E_src for
any source class, and every S_E-response to any source. Let Π_E be the S_E projection (T ≥ 5; Π^{(T)} of Prop SM for T ≤ 4).
Then
  **||Π_Ex||_{𝔐^∇} ≤ C_rec(||x||_inv + ||x_k||_D + N_res(x)),**
with C_rec = C_rec(α, d, L) uniform in k and T. Moreover, for every source y that annihilates 𝒢_0 and every x with 𝓛x = y,
**𝓛_{S_E}^{-1}π_{S_E}y = Π_Ex.**

These are BFT_B's Theorem EP-rec (l.2068, proof §16.6) and Theorem EP-opt (l.2065, proof §16.5), CONFIRMED in REVIEW_BFT_B_S5
B.5-B.6. **Provenance.** They are lane-B session-5 work (≈08:25Z on 2026-10-28), before the session-24/25 provenance window,
and they have had a lane review but no cross-family check. I re-derived the load-bearing steps.

**(a) Identification (EP-opt).**
- **Ker 𝓑 = 𝒢_0 on {x_k = 0}.**
  - 𝓑(x, x) = ||dx_0||² + Σ_lκ_l||r_l(x)||² = 0 forces dx_0 = 0. So x_0 = dλ + h, with h a constant (harmonic) 1-form.
  - It also forces r_l = 0, so x_l = Q^{(0→l)}x_0.
  - Then 0 = x_k = Q^{(0→k)}x_0 = d ev^{(k)}λ + L^kh. Taking means gives h = 0, and then ev^{(k)}λ is constant.
  - So x = Dλ′ with λ′ := λ − const ∈ Λ_0.
  - This agrees with BFT_B l.2204-2207 and with CODEX_REVIEW_GAPZ F1's independent zero-mode argument.
- **Existence and uniqueness.** For y ⊥ 𝒢_0 = Ker 𝓑, solutions exist (𝓑 is symmetric) and are unique modulo 𝒢_0. Π_Ex is a
  solution and lies in S_E. It is the only one there, because S_E ∩ 𝒢_0 = {0}: Λ_E(Dμ) = −μ (EP-alg (e)). ∎

**(b) Level 0 (EP-rec).**
- **Formula.** Put a_X := x_0 + dλ^E_X on Ñ_X. For b = (z, z + e_μ):
  (Π_Ex)_0(b) = Σ_Xχ_X(z + e_μ)a_X(b) + Σ_X(λ^E_X(z) − λ^E_*(z))dχ_X(b).
  Re-derived from the product rule d(χλ)(b) = χ(z + e_μ)dλ(b) + λ(z)dχ(b) and Σ_Xχ_X ≡ 1, then subtracting
  λ^E_*(z)·Σ_Xdχ_X(b) = 0.
- **a_X** (EP-int (b), BFT_B l.2163-2165; proof §16.2 Step 5).
  - Inside Ñ_X, a_X satisfies d*a = 0 and da = dx_0. With the flat Weitzenböck identity this gives, componentwise,
    −Δa_μ = Σ_ν∂^-_ν(dx_0)_{νμ}: an equation in divergence form.
  - LES-div (LINEAR_PACKAGE Lemma 3.2″) plus Caccioppoli then bound the C^{1,α}(N′_X) norm of a_X by C_int times
    (the L² average of a_X + sup|f_0| + [f_0]_α).
  - The L² term is controlled by the projection property ||a_X||_{ℓ²(Ñ)} ≤ ||x_0 + dμ||_{ℓ²(Ñ)}, which holds for every μ.
  - Re-derived: the projection property is the first variation of the box minimisation, and the interior equation is
    d*a = 0 at interior sites.
- **Choice of μ.** Take μ := the tent-axial gauge function, so that x_0 + dμ = (P_tentx)_0. Its sup is gauge-invariant data by
  Lemma LR-pot (BFT_A §13.12): sup|(P_tentx)^c_0| ≤ 155||f_0||_∞ + 8||x_k||_D + 40Σ_i||r^c_i||_∞. I re-read the proof: strip
  fluxes of at most 3n plaquettes, closed axial loops of length at most 12n, and root-to-root line sums.
- **λ^E_X − λ^E_*.**
  - Its coarse gradient is (a_X − a_*)^c.
  - Its value at c_* is Σ_π(a_X − x_0) along at most 4 root-to-root segments.
  - The x_0 line sums H_root on those segments are bounded by Lemma Λ (BFT_A §13.11): |H_root| ≤ ||x_k||_D +
    5Σ_i||r^c_i||_∞ + 10||f_0||_∞. Re-derived: the one-step ribbon fluxes are at most 2L(L − 1)L^{2i}s_0, and they
    telescope.
- **Tents.** Multiply by the C^{2,1} tents (σ_5, σ′_5 and σ″_5 all vanish at 1); at most 16 terms. This gives
  ||(Π_Ex)_0||_{C^{1,α}} ≤ C(||f_0||_∞ + [f_0]_α + ||x_k||_D + Σ_i||r^c_i||_∞), and Σ_i||r^c_i||_∞ ≤ (L/(L − 1))||x||_inv
  because ||x||_inv ≥ L^{k−1−i}||r^c_i||_∞.

**(c) Levels j ≥ 1.**
- r_i(Π_Ex) = r_i(x), by root covariance (Q∘d = d∘ev) and because ev^{(k)}Λ_E = 0.
- The relation x_{i+1} = Q_ix_i − r_i telescopes: (Π_Ex)_j = Q^{(0→j)}(Π_Ex)_0 − Σ_{i<j}Q^{(i+1→j)}r_i(x).
- Lemma Q-hold (BFT_B §16.3) bounds Q^{(a→b)} on C^{1,α}. Its straight part is an average of translates of v^c, so it
  preserves sup, gradient and Hölder. Its gauge part −d∘h^{(a→b)} costs 2ρ_b||∇^cv^c|| and 2ρ_b^α[∇^cv^c]^∞_α. C_Q does
  not depend on b − a.
- So ||(Π_Ex)_j||_{C^{1,α}} ≤ C_Q||(Π_Ex)_0||_{C^{1,α}} + C_QN_res(x).
- The residual terms of 𝔐^∇ are already terms of ||x||_inv. ∎

**Not re-derived here.** LES-div's Campanato iteration and the Caccioppoli constant (LINEAR_PACKAGE Lemma 3.2″, reviewed).
The values 155 / 8 / 40 in LR-pot and C_Λ = 10. Only the structure and finiteness of these constants are used; any finite
values would do.

### 5.2 Theorems GF-E and GF-E′

> **Theorem GF-E (BFT-5 clause (b), field half; trivial background; m = 0; composite-co-closed class). PROVEN as an
> implication; unreviewed.**
>
> Fix d = 4, L ≥ 3 odd, κ_±, and 0 < α < θ < 1. Let k ≥ 1 and T ≥ 1, and let S be any Setting LIN^cc source with B_k = 0 in
> the (P0) + (Pl-c) + (G) + (R) classes. Let x_E := 𝓛_{S_E}^{-1}π_{S_E}S be its S_E-response — equivalently its
> Γ_E-response, or its unique critical point in S_E (S_E^{(T)} when T ≤ 4). Then
>   **||x_E||_{𝔐^∇} ≤ C_GF·N(S),  C_GF := C_rec[(1 + 5κ_+/(κ_−(L^{1−α} − 1)))C_inv + C_N],**
> uniformly in k and T. Hence also ||[x]||_{𝔐^∇} ≤ C_GF·N(S) in the orbit norm, and in RTARGET's norm
> ||x_E||_{X_c} + [f_0]_α ≤ 3C_GF·N(S).

**Inputs.**
- **Theorem CC-INV**, ||x||_inv ≤ C_inv·N(S) (COFUN_CC §6.1). S26-banked; CONFIRMED in CODEX_REVIEW_TOPCC, "Exactly what
  may be banked", item 3. Its own inputs include Lemma TOP-cc, Theorem COF's lane-A inputs and LINEAR_PACKAGE Thm 4.2(ii).
- **Theorem RHT-cc** (BFT_B §29.3). CONFIRMED in REVIEW_BFT_B_S9_S10 S9-7 and in REVIEW55_BFTB l.92.
- **Proposition FH** (§5.1).
- **Proposition SM** (CONFIRMED, REVIEW_BFT_A_S7 l.51).

*Proof.*
1. S is (cc), so critical points exist and are unique modulo 𝒢_0 (Lemma FG (i)). By FH (a), x_E = Π_Ex for any critical
   point x.
2. By FH with x_k = 0: ||x_E||_{𝔐^∇} ≤ C_rec(||x||_inv + N_res(x)). Both terms are 𝒢_0-invariant, so they can be computed on
   any representative.
3. CC-INV bounds ||x||_inv.
4. RHT-cc's display (BFT_B l.3604-3605) bounds N_res(x) by the source norms plus κ_+||r^c_{k−1}||_∞. Bound it term by term
   using ||r^c_{k−1}||_∞ ≤ ||x||_inv, ||s^c_{k−1}||_∞ ≤ L^{−θ}||s||_R, π_l(j_l) ≤ L^{−θ(k−l)}||j||_Pc for l ≥ 1,
   π_0(j_0) = ||j^c_0||_∞, and ||G^c_l||_∞ ≤ L^{−θ(k−l)}||G||_Y:

   N_res ≤ (5/κ_−)[(κ_+||x||_inv + L^{−θ}||s||_R)/(L^{1−α} − 1) + L^{−θ}||s||_R/(L^{θ−α} − 1)
            + (1 − L^{−(1−α)})^{−1}((1 + K_f)||j||_Pc/(L^{1−α+θ} − 1) + 6||G||_Y/(L^{θ−α} − 1) + K_fL^{−(1−α)k}||j^c_0||_∞)].

   Every geometric series converges because 0 < α < θ < 1. For example, the G-term is
   6Σ_lL^{α(k−l)}||G^c_l|| ≤ 6Σ_{u≥1}L^{−(θ−α)u}||G||_Y. So N_res ≤ (5κ_+/(κ_−(L^{1−α} − 1)))||x||_inv + C_N·N(S), with
   C_N read off the display.
5. Combine 2-4. ∎

CODEX_REVIEW_TOPCC independently notes that "RHT-cc can also consume TOP-cc … the old occurrence of the unknown top
residual is removed there as well".

> **Theorem GF-E′ (RTARGET §33's (G♯_0-field) on the slice S_E, m = 0). PROVEN as an implication; unreviewed.**
>
> Same (d, L, κ_±), with 0 < α < θ < 1 and ω_l = L^{θ(k−l)}. For every k and T, every collection of co-closed, zero-mean,
> divergence-form sources G_l (0 ≤ l ≤ k − 1) and every datum B_k, the S_E critical configuration B obeys
>   **||B||_{X_c} + [f_0]_α ≤ 3||B||_{𝔐^∇} ≤ C′(||G||_{Y,α} + ||B_k||_D),**
> where ||G||_{Y,α} is RTARGET's own source norm: sup at levels ≥ 1, Hölder at level 0.

**Inputs.**
- **Corollary LIN0** (BFT_A §28.8). At levels ≥ 1 it enters through GU, which uses sup norms only (BFT_A l.2241, l.2514).
- **Theorem RHT, Corollary RH-inv and Corollary RH-D** (BFT_B §18.1, §19.3). CONFIRMED / CONFIRMED-WITH-FIX for level-wise
  co-closed classes (REVIEW_BFT_B_S6 l.42-43). RTARGET's sources are level-wise co-closed.
- **Proposition FH** with x_k = B_k.

*Proof.* Apply FH with ||x_k||_D = ||B_k||_D. RH-inv gives N_res ≤ C_1||x||_inv + C_2||y||, where y is the sources plus the
datum. LIN0 bounds ||x||_inv. ∎

*Scope.* The slice is S_E, not RTARGET's per-level slice (§5.5). m = 0 (see §5.3 for m > 0). The window α < θ is required
(P-2).

This is exactly the content the ledger has carried as "(G♯_0-field): not attempted" since session 15. It has been an
implication of reviewed items since BFT_B session 6 ("Corollary EP-lin gives (W-lin-Π) for S_E from (H-inv) alone",
BFT_B l.2509) together with lane A's LIN0 (lane A session 6). NBG_B §9 S9 and S11 (i) half-recorded it (§6 below).

### 5.3 m > 0: the field half adds nothing, and the residue is named

**EP-rec's weighted reach — ARGUED in REVIEW_BFT_B_S5 under RS5-4 (a) — is finite and absolute: CONFIRMED.** Every quantity
used for the field at an output link b lies within a k- and T-independent coarse distance R_* of b:
- Π_E at b reads Λ_E at the two end roots. That reads λ^E_X for |z − c_X|_∞ < 1, and each λ^E_X reads x_0 on Ñ_X (coarse
  half-width 2). EP-alg (g) gives radius 4.
- EP-int (b) bounds a_X on N′_X (half-width 3/2) by quantities on Ñ_X. It is local by construction: an interior estimate on a
  fixed coarse box.
- LR-pot's bound at a point w ∈ Ñ_X uses:
  - strips between axial paths and closed loops, all within ∞-distance 1 of c_X;
  - root-to-root segments joining adjacent corners;
  - Lemma Λ's loops for a coarse link (X′, ν), which lie in B(X′) ∪ B(X′ + e_ν) (BFT_A l.1118-1119, "All loops lie in
    B(X) ∪ B(X + e_μ)").

  I checked the nesting: each level-l S4′ contour of a level-(l+1) link stays in that link's two level-(l+1) blocks, so
  every composite contour of a level-k link stays in the fine sites of its two level-k blocks.
- Q^{(a→b)} at a level-b link reads within its two level-b blocks, at distance ≤ 8ρ_b ≤ 8 (BFT_A l.1102-1103). Hölder
  differences add one more coarse unit.
- Adding the radii: **R_* ≤ 4 + 3 + 5 + 8 + 1 = 21**.

So ||Π_Ex||_{𝔐^∇,m} ≤ e^{R_*m}·C_rec·(||x||_{inv,m} + ||x_k||_{D,m} + N_res,m(x)), with local sups and box-weighted
Campanato, because e^{md(b,X_0)} ≤ e^{mR_*}e^{md(w,X_0)} whenever d(w, b) ≤ R_*. The lane's c_r = 24 is consistent with
this. I did not re-count that exact value, and it does not matter.

**Consequence, for 0 ≤ m ≤ m_Y.** On S_E, the weighted field half follows from the weighted gauge-invariant half plus
N_res,m. N_res,m is supplied by RH_m (CONFIRMED with c_w = 12; REVIEW_BFT_B_S6 l.42) and by RHT_m-cc (CONFIRMED with
c_w = 14). Hence:
- **For (cc), i.e. clause (b):** the weighted field half follows from **(R3)** — weighted CC-INV / COF — and from nothing
  else.
- **For RTARGET's class:** it follows from the weighted LIN0. Its parts:
  - W0_m for level-0 sources (CONFIRMED);
  - Theorem W / Prop W for data and residual-type sources (CONFIRMED);
  - **GU_m**. Its sup part is Corollary Y_m, which needs **DX_m and DB_m** (BFT_A §26.3, §28.13: "OPEN, not written").
    Its Hölder part is not written. BFT_A §28.13 notes that the global-Coulomb route fails for the weighted Hölder norm and
    asks for a box-local gauge, which is what W0-loc / LES-dd did at level 0.
- So BFT5-red's input (1), "with the weighted constants", has as its exact residue **lane A's DX_m and DB_m plus the
  weighted Hölder half of GU**. None of it is field-specific.

### 5.4 Z ≠ 1: the field half lives in (R2) as (EP-rec)_Z

At a background Z = Z(V_k), the field half is the Z-covariant form of Proposition FH. I write it **(EP-rec)_Z**. It is not a
new object: it is the linear part of the slice clause of lane B's (N1) (BFT_B l.2255: "the Z-covariant (background) version
is (N1)").

**Statement.** Let λ^{E,Z}_X be the covariant box-Coulomb gauge function: minimise Σ_{b⊂Ñ_X}|x_0 + d_Zλ|² subject to
λ(c_X) = 0. Put Λ^Z_E := Σ_Xχ_Xλ^{E,Z}_X and S_E^Z := {Λ^Z_E(x) = 0}. With the covariant quantities 𝔐^∇_Z, ||·||^Z_inv and
N^Z_res of BFT_B §12.0, (EP-rec)_Z says
  ||Π^Z_Ex||_{𝔐^∇_Z} ≤ C(||x||^Z_inv + N^Z_res(x) + ||x_k||_D),
uniformly over the background class.

**Its four ingredients.** Each is a perturbation of the flat one on a box of fixed coarse size, in a frame where Z is
C^{1,α}-small (Corollary CL-iv: sup_j||log Z^off_j||_{C^{1,α}} ≤ C_1ε):
- (i) **EP-int at Z.** Interior Schauder for d_Z^*a = 0, d_Za = F. The covariant Weitzenböck identity adds zero-order
  [F_Z, a]-type terms and first-order Ad-transport terms, each of relative size C_1ε in the frame.
- (ii) **LR-pot at Z.** Covariant axial transports; Stokes picks up background-curvature terms.
- (iii) **Lemma Λ at Z.** Covariant root-to-root transports. The telescoping uses root covariance of Q^Z, which fails by a
  defect ≲ Cρ²_{l+1}f_k on straight-row towers (REVIEW55_BFTB item 11). That defect is summable in l.
- (iv) **Q-hold at Z.**

**Why no global patching is needed.** (EP-rec)_Z is local with finite reach, and every quantity in it is frame-covariant. So,
unlike (G♯-patch), it can be proved one frame at a time.

**Status: ARGUED — an outline only, not attempted. It belongs to (R2), next to (CC-dec_Z).** It does **not** need (GAP-Z):
like EP-rec it is a reconstruction, not an inverse estimate.

### 5.5 The per-level slice: admissible, not consumed

> **Lemma PL-adm (the per-level slice is an admissible gauge fixing). PROVEN-HERE.**
>
> At the trivial chain put Γ_PLx := (h_i(x_i), P^{(i)}_res d*_ix_i)_{0≤i≤k−1}. Here h_i is the one-step slice functional
> (Q_i = Q_{str,i} − d∘h_i), and P^{(i)}_res is the orthogonal projector onto
> Λ^{(i)}_res := {μ on level-i sites : μ(c_X) = 0 and Σ_{B(X)}μ = 0 for every level-(i+1) site X}. Then Γ_PLD is a
> bijection from Λ_0 onto ⊕_i(ℝ^{N_{i+1}} ⊕ Λ^{(i)}_res), where N_i is the number of level-i sites. Hence, by Lemma FG (iii),
> for every (cc) source the per-level-slice response is the critical point with Γ_PLx = 0. Explicitly,
> x_PL = x_E + Dν_PL with ν_PL = −(Γ_PLD)^{-1}Γ_PLx_E.

*Proof.*
- **Injectivity, top-down.** Let λ ∈ Λ_0 with Γ_PLDλ = 0, and put λ_i := ev^{(i)}λ. Because h is an average of path
  integrals from c_X, h_i(dν)(X) = avg_{y∈B(X)}ν(y) − ν(c_X).
  - Level k − 1: λ_{k−1}(c_X) = ev^{(k)}λ(X) = 0, and the h-condition gives avg_{B(X)}λ_{k−1} = 0. So
    λ_{k−1} ∈ Λ^{(k−1)}_res.
  - Then 0 = ⟨λ_{k−1}, P_resd*dλ_{k−1}⟩ = ||dλ_{k−1}||², so λ_{k−1} is constant, and it vanishes at the roots, so
    λ_{k−1} = 0.
  - Level k − 2: now λ_{k−2}(c_Y) = λ_{k−1}(Y) = 0 for every Y, and the same argument applies. Induct down to
    λ_0 = λ = 0.
- **Dimensions.** dim Λ_0 = N_0 − N_k. dim Λ^{(i)}_res = N_i − 2N_{i+1}: two independent conditions per block, since each
  block has L⁴ ≥ 81 sites. The target therefore has dimension Σ_{i<k}(N_{i+1} + N_i − 2N_{i+1}) = N_0 − N_k. ∎

**The transfer S_E → per-level slice: ARGUED, and not needed.**
- ν_PL is computed top-down, one level at a time. At level i it is fixed by the block means (the h-condition) and by
  T_i^{-1}, where T_i := P_resΔ_0|_{Λ_res} ≥ ν_N = 2(1 − cos(π/L)) (Lemma N5-coer step (1); PROOF l.5394).
- T_i^{-1} is exponentially local in level-i units (Combes–Thomas, as in Lemma CT / Theorem N5-triv).
- For an S_E field with 𝔐^∇ control, the per-level defects are of higher order: the h-defect of an affine field is zero by
  centring, and the Feynman defect is the oscillation of the divergence within a block. I estimate the level-i correction at
  O(ρ_i^{1+α}) in coarse sup units, times ||x_E||_{𝔐^∇}, which is summable over levels.
- **The hole:** how a level-i correction propagates to finer levels through the triangular system is not written.
- The input this transfer needs is the per-level gauge-fixing inverse (block Neumann gap ν_N), **not** a multi-level
  physical gap. No live consumer needs the transfer.

### 5.6 Where the suggested tools enter
- **LINEAR_PACKAGE Thm 4.2 / 4.2′ (response kernels).** They enter only inside the gauge-invariant half: in Prop W / BL-4 for
  the data map, and through Green reciprocity in W0 / GU / COF. They are never used as an inverse (I agree with
  CODEX_REVIEW_GAPZ F2). The field half (FH) uses no inverse at all.
- **Random-walk and multiscale expansions (Theorem RW, N5-triv).** Not needed for the field half at Z = 1. They would serve
  global patching of (EP-rec)_Z, but FH's locality makes such patching unnecessary.
- **Combes–Thomas weighted inverses (CODEX_REVIEW_GAPZ F5).** They enter only the per-level transfer (T_i^{-1}, §5.5), and
  possibly the weighted gauge-invariant half (R3). Not the field half.
- **Balaban CMP 95/96.** These treat trivial-background propagators for the hard constraint, in axial- and Landau-type
  gauges. They bear on (R3), since his random-walk bounds are weighted by construction. CMP 99/102 (background-field
  regularity in a fixed gauge) are the hard-scheme analogue of (EP-rec)_Z, so they bear on (R2). None of them is needed for
  (R1) at Z = 1, and I did not wait for them.

---

## 6. Findings, claim by claim

Scope: the earlier statements about (G♯_0-field) that the lead asked me to re-derive rather than inherit, plus the lane
statements that §5 overturns.

- **F1.** NBG_B §3 (l.120-132), "(G♯_0-field) pinned". **CONFIRMED** as a reading of RTARGET §33. The source statement has
  four defects of its own (§2, P-1 to P-4).
- **F2.** NBG_B §3 (l.134-147), "Status: OPEN, and specifically 'not attempted'". The quotation is accurate (PROOF l.3658;
  RTARGET l.654). As the status of the mathematics: **REFUTED**.
  - On S_E the statement is PROVEN as an implication at m = 0 (Theorem GF-E′).
  - It has been so since BFT_B session 6 together with lane A session 6.
  - The per-level-slice version is the only one never attempted, and nothing consumes it.
- **F3.** NBG_B §3 (l.149-155), "None of it is the configuration statement, and none of it is on the per-level slice".
  - The first half is **REFUTED**: EP-lin, RH-inv and EP-rec are the configuration statement on S_E.
  - The second half is true but immaterial.
- **F4.** NBG_B §6.2 table (l.242-249), row "extra input: the abelian multi-level per-level-slice physical gap". **REFUTED**
  as a requirement (§3.2-3.3).
- **F5.** NBG_B §6.5 (l.291-292): "the gauge-variant half, and the multi-level slice gap; the first six are PROVEN at Z = 1
  and the last two are not". **REFUTED.**
  - The gauge-variant half on S_E follows from FH + LIN0 + RH-inv.
  - NBG_B contradicts itself: its own §9 S6, S9 and S11 (i) say the opposite.
  - The gap is PROVEN under reading A and undefined under reading B (§3.3).
- **F6.** NBG_B §9.2 S9 (l.533-535), "(W-lin-Π) ⟺ (H-inv+) now resolves at m = 0" for level-wise co-closed classes.
  **CONFIRMED**, re-derived through FH. It respects REVIEW_BFT_B_S9_S10's S9-13 class caveat.
- **F7.** NBG_B §9.2 S11 (i) (l.545-548): "on S_E the live name is (G♯_0-field^∇) … both of its halves are in hand at the
  trivial background for data and residual-type sources". **CONFIRMED, but too narrow.** By FH both halves are in hand for
  every level-wise co-closed class (GF-E′) and for (cc) (GF-E).
- **F8.** NBG_ADJ §2.4 (l.164-177) and PROOF [S25-fix 5] (l.≈156-165): "(G♯_0-field) = [per-level-slice gap] +
  [(G♯_0-fine)]". **REFUTED** as an identity.
  - As a sufficiency it is NOT-VERIFIED (I agree with Codex NBG2 F13).
  - Neither piece is necessary on S_E: the gap is replaced by a reconstruction (§3.2).
- **F9.** NBG_ADJ graph (l.350-357), node "multi-level per-level-slice physical gap [OPEN; NOT PG^{(k)}]". **REFUTED**
  under PROOF's own gloss, where it is LINEAR_PACKAGE Prop 6.4 / N5-coer, both PROVEN. Under the joint reading B it is
  undefined (§3.3).
- **F10.** NBG_ADJ: "(G♯_0-fine) is OPEN for a reason that has nothing to do with any gap: … the K ≠ 0 alias symbol has
  not been shown analytic in a strip" (§2.4; graph node l.355-356). **REFUTED** (§3.4):
  - the status is stale (LIN0; W0_m);
  - the source is misquoted;
  - the alias factors are analytic (PROOF's own (P4), and my re-derivation);
  - the obstruction PROOF actually recorded is G0-F2, and it is resolved.
- **F11.** PROOF [S25-fix 5] (l.≈170-171), "That fourth object's status is recorded NOWHERE", and NBG_ADJ A6
  (l.298-302). **REFUTED.** The object is (W-lin-Π) for S_E:
  - defined at BFT_B §12.1 (l.1612);
  - proved through EP-opt and EP-lin (BFT_B l.2065-2074, §16.5-16.7) and RH-inv (l.2507-2510);
  - graded CONFIRMED / CONFIRMED-WITH-FIX in REVIEW_BFT_B_S5 B.5-B.7 and REVIEW_BFT_B_S6 l.43;
  - recorded by NBG_B itself (§9 S9).

  FLATZ.md had pre-registered exactly this outcome ("FZ-F5 (recorded after all)") before it was abandoned.
- **F12.** PROOF [S25-fix 5]: "Independent paper-scale obstructions: TWO, (GAP-Z) and (G♯_0-field)". REVIEW55_LEAD H14c has
  already reverted the count. On (G♯_0-field) specifically: **REFUTED.**
  - It is not an independent obstruction (FH).
  - At Z = 1, m = 0 it is an implication of reviewed items.
  - LINEAR_PACKAGE §10 itself rates its configuration-norm item session-scale "(s)" (l.470-471).
- **F13.** COFUN_CC §6.2 (R1) (l.437-438): "Needs (G♯_0-field) (BFT5-red input (1), OPEN; BFT_A BL-7 (e)). CC-INV gives
  nothing here: ||x||_inv ≤ 2||x||_{𝔐^∇} is the wrong direction." **REFUTED.**
  - On S_E, EP-rec supplies the reverse direction, given N_res, and RHT-cc controls N_res.
  - BL-7 (e) (BFT_A l.559; lane A session 2) is superseded by BFT_B §16 (lane B session 5) and Prop SM (c) (lane A
    session 7).
  - The correct statement is Theorem GF-E.
- **F14.** COFUN_CC "Verdict T2" (l.484-487): "(BFT-5_E) clause (b): still OPEN, with (R1) (G♯_0-field), (R2) …, (R3) …".
  **REFUTED as to (R1) at Z = 1, m = 0.** (R2) and (R3) stand. (R1)'s m > 0 part merges into (R3), and its Z ≠ 1 part into
  (R2).
- **F15.** BFT_B §32.1 (b) (l.3831): "these bounds are independent of the gauge fixing, so (b) is a statement about the
  orbit". **REFUTED** for field components (Proposition GF-DEP). Fix: use the orbit norm (§4.2).
- **F16.** BFT_B §32.2 input (1) (l.3840): "(G♯_0-field) — (G♯) for the chain Hessian at the trivial chain in the §33 pair,
  with the weighted constants. Status quoted: OPEN … (it also needs the abelian multi-level physical gap)". **REFUTED as a
  status.**
  - It is stale against BFT_B's own §16 and §18.1, and against BFT_A §33.13.
  - At m = 0 it is PROVEN as an implication (GF-E′, on S_E).
  - At m > 0 it is DX_m + DB_m + the weighted Hölder half of GU (§5.3).
- **F17.** PROOF BNA-F3 (l.3428-3433, session 14): "A smooth complete gauge is the covariant multi-level slice …; its (G♯)
  contains a multi-level physical gap". **NOT-VERIFIED.**
  - The smoothness of the per-level slice was asserted and never proven.
  - "Contains a gap" describes an ℓ²-coercivity route, not a necessity.
  - S_E is the smooth complete gauge that is actually proven (EP-bd).
- **F18.** RTARGET §33 (l.601): constants "depending only on (L, κ_±, m, α)", with θ free. **NOT-VERIFIED** (§2 P-2). This
  matches no proven route; whether a θ-free constant or α ≥ θ is possible is not decided.
- **F19.** BFT_B Theorems EP-opt and EP-rec (§16.5-16.6). **CONFIRMED**; load-bearing steps re-derived in §5.1.
- **F20.** EP-rec's weighted reach (REVIEW_BFT_B_S5 RS5-4 (a), ARGUED). **CONFIRMED** finite and absolute, with
  R_* ≤ 21 (§5.3). The specific value c_r = 24 is NOT-VERIFIED and immaterial.
- **F21.** RHT-cc's absolute form in N(S), consuming TOP-cc (COFUN_CC l.404; Codex TOPCC). **CONFIRMED**; I re-derived the
  geometric sums (§5.2 step 4).

---

## 7. Codex verdicts used — agree or disagree, explicitly

Every file listed was read as it is on disk now. CODEX_REVIEW_TOPCC appeared at 00:01Z while I worked; its last lines are
complete. CODEX_REVIEW_HINT is a PRE-STATED block only and looks unfinished; I did not use it.

**CODEX_REVIEW_GAPZ**
- **F1** (Z = 1 is admissible; no new exact flat zero mode): **AGREE.** FH (a)'s kernel step re-derives it independently.
- **F2** (M bounds response kernels, not an inverse; scalar witness): **AGREE.** Nothing here uses M as an inverse. The field
  half is a reconstruction, and the gauge-invariant half is an inverse estimate restricted to invariant outputs for all
  sources in the class — which is not M.
- **F3** (status labels cannot decide identity): **AGREE.** (G♯_0-field) is a live example: it was labelled "not attempted"
  while already an implication of reviewed items.
- **F5** (Combes–Thomas; the "norm row" is not fatal): **AGREE.** It is irrelevant to the field half.
- **F10** (phrase collisions): **AGREE.** I add the "𝔐-pair" collision and the four names of the composite-slice inverse.
- **Table, "GZ ⇒ Gf NOT-VERIFIED"**: **AGREE.** GF-E′ shows that the S_E form of Gf needs no GZ at all.

**CODEX_REVIEW_NBG2**
- **F10** (a decomposition is a list of obligations; "no decay claimed" ≠ "decay cannot follow"): **AGREE.**
- **F13 row 1** (per-level gap + G♯_0-fine → G♯_0-field: NOT-VERIFIED): **AGREE** on sufficiency. I add that neither piece
  is necessary on S_E, and that the gap is PROVEN under PROOF's gloss.
- **F14** (every historical PROOF citation NOT-VERIFIED): I have now checked them. The strings exist; the drift is in §8.

**CODEX_REVIEW_TOPCC**
- **TOP-cc, CC-FUN(c), CC-INV CONFIRMED** at Z = 1, m = 0: **AGREE.** I used them as banked inputs and re-derived only the
  RHT-cc summability.
- **"6.2 … CONFIRMED as a scope separation" and "1. Field components — NOT-VERIFIED … cannot be reversed to obtain
  (G♯_0-field)": PARTLY DISAGREE.**
  - I agree that CC-INV alone does not give the field half, and that ||x||_inv ≤ 2||x||_𝔐 does not reverse in general.
  - I disagree that the field half is therefore an additional obligation. On S_E it does reverse, with the gauge-invariant
    extra term N_res (EP-rec), and Codex's own remark that "RHT-cc can also consume TOP-cc" controls N_res. So (R1) at
    Z = 1, m = 0 is PROVEN as an implication (GF-E).
  - I agree that "uniformity over gauges for invariant outputs says nothing comparable about the fields". Proposition
    GF-DEP makes that exact.
- **"𝒬_{H,m} ARGUED" is stale; QH_m and W0_m supersede it**: **AGREE.** I found independently that W0_m is CONFIRMED
  (REVIEW_BFT_A_S7 l.48, l.314), and §5.3 uses it.
- **Ñ_Σ remark** (GU uses only sups at positive levels): **AGREE** (BFT_A l.2241, l.2514). It is what lets GF-E′ use
  RTARGET's own Y_α norm.

---

## 8. Citation drift found, and corrections to this file

**Drift in other files**
- PROOF.md moved +4 lines between 23:50Z and 00:20Z (live edits elsewhere).
  - "(G♯_0-field): not attempted" is now at l.3658. It is cited as l.3588 (NBG_B §3, §6.1; SESSION25_RESULTS l.78) and as
    l.3614 (NBG_ADJ; [S25-fix 5]).
  - "(G♯_0-fine) is also needed" is at l.3657 (cited as l.3613).
  - "has not been shown analytic in a strip" is at l.3656 (cited as l.3612).
- [S25-fix 5] (PROOF l.≈164-165) quotes PROOF as "K≠0 alias symbol not analytic in a strip". The source says "has not been
  shown analytic in a strip": a misquotation (§3.4 (ii)).
- RTARGET §33 begins at l.572. The lead's "l.586-605" is the section body; the (G♯_0-field) line at l.605 is correct.
- BFT_B §32.2 input (1) cites "PROOF l.3473, l.6698". The matching strings are now at l.≈3405 ("(G♯) at U = 1 is
  (G♯_0-field) of §33") and in the PROOF clause-table row for BFT-5 (l.≈6882).

**Corrections to THIS file** (append-only; nothing above is edited)
- §2 (P-2): "BFT_A l.2530" (GU's level sum) → **l.2531**; "l.2541" (LIN0) → **l.2542**; "BL-5 (c), BFT_A l.534-538" →
  **l.524-528**.
- §2 (P-4): "PROOF l.3385-3388" → **l.3389-3390**, the sentence "Let 𝒮 be a linear chain gauge slice with a Feynman term …".
- §0 item 5: the sentence "I also argue that 𝔐^∇ is not expected to be uniform in that slice (block-centre spikes) …" is
  **WITHDRAWN.** When I re-checked it (§5.5), the per-level conditions turned out to be second-order on smooth fields (a
  Coulomb-like cancellation), so the spike estimate behind that sentence was wrong. I make no claim about 𝔐^∇ in the
  per-level slice: **NOT-VERIFIED.**

---

## 9. Summary table

### 9.1 Claims reviewed

| id | claim (file, locating string) | verdict | correction / reason |
|---|---|---|---|
| F1 | NBG_B §3, "(G♯_0-field) … pinned" | **CONFIRMED** (as a reading) | the source statement has four defects (§2, P-1 to P-4) |
| F2 | NBG_B §3, "Status: OPEN, and specifically 'not attempted'" | **REFUTED** (as a status; the quotation is accurate) | PROVEN as an implication on S_E at m = 0 (GF-E′) |
| F3 | NBG_B §3, "none of it is the configuration statement" | **REFUTED** | EP-lin / RH-inv / EP-rec are the configuration statement on S_E |
| F4 | NBG_B §6.2 row "extra input: … per-level-slice physical gap" | **REFUTED** | not required (§3.2-3.3) |
| F5 | NBG_B §6.5, "the gauge-variant half … [not] PROVEN at Z = 1" | **REFUTED** | FH + LIN0 + RH-inv; contradicts NBG_B's own §9 |
| F6 | NBG_B §9 S9, "(W-lin-Π) ⟺ (H-inv+) now resolves at m = 0" | **CONFIRMED** | re-derived through FH |
| F7 | NBG_B §9 S11 (i), "both halves in hand … for data and residual-type sources" | **CONFIRMED** (too narrow) | true for all level-wise classes and for (cc) |
| F8 | NBG_ADJ §2.4 / [S25-fix 5], "(G♯_0-field) = [gap] + [(G♯_0-fine)]" | **REFUTED** | an order of work; neither piece is necessary on S_E |
| F9 | NBG_ADJ graph, "multi-level per-level-slice gap [OPEN]" | **REFUTED** | under PROOF's gloss it is Prop 6.4 / N5-coer (PROVEN); under reading B it is undefined |
| F10 | NBG_ADJ, "(G♯_0-fine) OPEN … K ≠ 0 alias symbol not analytic in a strip" | **REFUTED** | stale (LIN0, W0_m); misquoted; the factors are analytic (P4 and §3.4); the real issue G0-F2 is resolved |
| F11 | [S25-fix 5] / NBG_ADJ A6, "fourth object … recorded NOWHERE" | **REFUTED** | it is (W-lin-Π) for S_E: BFT_B §12.1, §15.1, §16.5-16.7, §18.1; CONFIRMED in lane reviews |
| F12 | [S25-fix 5], "(G♯_0-field)" a paper-scale obstruction | **REFUTED** | not independent (FH); an implication at Z = 1, m = 0 |
| F13 | COFUN_CC §6.2 (R1), "CC-INV gives nothing here … wrong direction" | **REFUTED** | EP-rec reverses the inequality on S_E; Theorem GF-E |
| F14 | COFUN_CC "Verdict T2": (R1) still OPEN | **REFUTED** (as to (R1) at Z = 1, m = 0) | (R1) is absorbed: closed / into (R3) / into (R2) |
| F15 | BFT_B §32.1 (b), "independent of the gauge fixing" | **REFUTED** (for field components) | Prop GF-DEP; state (b) in the orbit norm |
| F16 | BFT_B §32.2 input (1), status OPEN | **REFUTED** (stale) | m = 0: GF-E′; m > 0: DX_m, DB_m + weighted GU Hölder |
| F17 | PROOF BNA-F3, "a smooth complete gauge is the covariant multi-level slice … contains a … gap" | **NOT-VERIFIED** | smoothness never proven; "contains a gap" is a route, not a necessity |
| F18 | RTARGET §33 l.601, constants (L, κ_±, m, α) with θ free | **NOT-VERIFIED** | must read C(L, κ_±, m, α, θ) with α < θ for every proven route |
| F19 | BFT_B Theorems EP-opt, EP-rec | **CONFIRMED** | re-derived (§5.1) |
| F20 | EP-rec weighted reach (RS5-4 (a), ARGUED) | **CONFIRMED** (finite, R_* ≤ 21) | the value c_r = 24 is NOT-VERIFIED and immaterial |
| F21 | RHT-cc absolute in N(S) via TOP-cc | **CONFIRMED** | geometric sums re-derived |

### 9.2 Results of this file (status words; none has had a Codex check yet)

| id | statement | status |
|---|---|---|
| N1 | Proposition FH (= EP-opt + EP-rec, applied to every S_E-response) | CONFIRMED (re-derived) |
| N2 | **Theorem GF-E**: clause (b)'s field half, Z = 1, m = 0, (cc): ||x_E||_{𝔐^∇} ≤ C_GF·N(S) | **PROVEN as an implication** |
| N3 | **Theorem GF-E′**: RTARGET's (G♯_0-field) on S_E, m = 0, 0 < α < θ < 1 | **PROVEN as an implication** |
| N4 | Proposition GF-DEP: field responses are unbounded across admissible gauge fixings | PROVEN-HERE |
| N5 | orbit norm ≍ S_E norm: ||[x]|| ≤ ||Π_Ex|| ≤ C_Π||[x]|| | PROVEN-HERE (from EP-bd) |
| N6 | Lemma PL-adm: the per-level slice is an admissible gauge fixing | PROVEN-HERE |
| N7 | the K ≠ 0 alias factors are analytic on |Im p_α| ≤ 1.4, uniformly in n ≥ 3 | PROVEN-HERE (elementary; sharpens PROOF's (P4)) |
| N8 | m > 0: weighted field half ⟸ weighted gauge-invariant half + N_res,m | PROVEN as an implication (given F20) |
| N9 | (EP-rec)_Z at Z ≠ 1, perturbative and frame-local | ARGUED (outline) |
| N10 | transfer S_E → per-level slice in X_c | ARGUED (hole named in §5.5) |

### 9.3 Counts (claims reviewed, §9.1)

- **CONFIRMED 6:** F1, F6, F7, F19, F20, F21.
- **NOT-VERIFIED 2:** F17, F18.
- **REFUTED 13:** F2, F3, F4, F5, F8, F9, F10, F11, F12, F13, F14, F15, F16.

---

## 10. For the lead — what changes

**1. BFT-5 clause (b), open list.**
- (R1), the field components, is **CLOSED at Z = 1, m = 0** as an implication (Theorem GF-E). Its inputs are:
  - CC-INV (S26-banked, Codex-confirmed);
  - RHT-cc (confirmed twice, once by Opus 5.5);
  - EP-rec / EP-opt (lane review only — **these should go to the Codex checker together with GF-E**, especially EP-int (b),
    LR-pot, Lemma Λ and Q-hold).
- At m > 0, (R1) **is (R3)**: §5.3 adds nothing beyond the weighted gauge-invariant half.
- At Z ≠ 1, (R1) **is (EP-rec)_Z, inside (R2)**.
- The clause-(b) open list therefore becomes:
  - (R2) — background transfer, (CC-dec_Z), (EP-rec)_Z;
  - (R3) — weighted COF;
  - (R4) — the level count.

**2. Statement of clause (b).** BFT_B §32.1 (b)'s "independent of the gauge fixing" is false for field components. Restate
(b) in the orbit norm ||[x]||_𝔐 = inf_{g∈𝒢_0}||x + g||_𝔐, or name S_E. The two are equivalent up to C_Π.

**3. BFT5-red input (1)** (BFT_B §32.2). Replace "(G♯_0-field) [OPEN; needs the multi-level physical gap]" by
"(W-lin-Π)_m for S_E ⟸ (H-inv)_m + (Res-Hölder)_m (EP-lin, RH-inv)". Its status:
- m = 0: PROVEN as an implication (GF-E′, with the S9-13 class caveat handled by GF-E for (cc));
- m > 0: residue = lane A's **DX_m and DB_m**, plus the weighted Hölder half of GU.

**4. Lines in PROOF.md that should change** (the lead edits; I do not):
- [S25-fix 5]'s graph "(G♯_0-field) ⟸ [multi-level per-level-slice gap] + [(G♯_0-fine)]" and its "K≠0 alias … not
  analytic" (PROOF l.≈156-165): strike.
- "That fourth object's status is recorded NOWHERE" (l.≈170): strike. It is (W-lin-Π) for S_E, BFT_B §15.1 / §16.
- "(G♯_0-field): not attempted" (l.3658): annotate as superseded on S_E (BFT_B §16.5-16.7, §18.1 RH-inv; BFT_A §33.13).
- BNA-F3's smoothness claim for the per-level slice (l.3428-3433): flag as unproven. S_E is the proven smooth complete gauge.
- RTARGET §33 l.601: C = C(L, κ_±, m, α, θ) with 0 < α < θ.

**5. HANDOFF / critical path.**
- (G♯_0-field) should **leave** the list of paper-scale walls.
- At the trivial background, BFT-5's remaining analytic items are (R3) (weighted COF ⟸ DX_m, DB_m, …) and (R4).
- At the nontrivial background they are (R2) (with (EP-rec)_Z, perturbative given CL-iv) together with (GAP-Z) / (N-bg) as
  before.
- None of this needs CMP 95/96 at Z = 1.

**6. Tally.** No PROOF item moves on my say-so. If the 105-item ledger counts B-NA's (G♯) at U = 1 or (G♯_0-field) as an
OPEN item, its m = 0 part is now an implication of reviewed items, pending Codex. Whether that moves a count is the lead's
call after that check.

**7. Owners' statement edits** (not mine to make). SF (a5-G♯) / (G♯-patch) and B-NA-red's [R1314-fix] (2) name "the
per-level covariant slice". Nothing consumes that choice. Re-pointing them to S_E removes the only remaining reason the
per-level slice appears in the ledger. LINEAR_PACKAGE §10's "(s)" item "a uniform per-level gauge-fixed gap … and with it a
configuration-norm bound" is resolved on S_E at m = 0; that is v2 change-log material.

UTC end: 2026-10-29 (see the `date -u` stamp below).
UTC end stamp: 2026-10-29T00:26:55Z

---

## 11. Line corrections found on the final read (append-only; content unchanged)

Checked at 00:27Z. PROOF.md is still being edited elsewhere.
- §0 item 3 gives PROOF "l.3030, l.3058" and "l.3369-3372". Those are the 23:50Z positions; as of 00:27Z they are
  **l.3034, l.3062, l.3373-3376**. §3.4 already uses the current numbers.
- §2 ("Outcome recorded … PROOF l.3654") and §2 (P-1) ("l.3404") → **l.3658** and **l.3408**.
- §0 item 2(b) and §5.2 describe CC-INV as "S26-banked". When first written that was true only of its (CO-fun) part. At
  00:15Z the lead banked CC-INV itself in PROOF's header ("[2026-10-29T00:15Z] Gauge-invariant half of BFT-5 clause (b) …
  Theorem CC-INV", PROOF l.12), on CODEX_REVIEW_TOPCC item 3. The description is accurate now.
- New header entry seen at the same read: "Lemma TR (level-count factor) — CONFIRMED at the quadratic level" (PROOF l.13).
  This bears on (R4) and does not change anything above.
