# FCON: FC-mean-match and FC-test for the actual stage contour (pass 1, long draft)

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), 2026-11-05, pass 1 (long draft) of critical-path item 7 of `library/assembly-status.md`, in the draft → distil → referee → freeze process. Not distilled, not refereed, not checked by another model. Research text, not an audit; it grants no status. All arguments are by hand. No step is discharged by a computation.

**Credit.** SA is the four-dimensional outline `ym4.tex` (revision 31a47c543775), CA-I its complete account I, Y3 the three-dimensional manuscript. Their stage operation, soft block gauge, relative gauge form, running-radius table and older-test implications are by **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text**. The averaging, background, gauge-fixing and stage methods originate with **Tadeusz Bałaban**; the flat-propagator exposition used by P82 is **Jonathan Dimock**'s. Library texts by Claude and Codex keep their own stated premises.

**Read for this draft** (bounded ranges; "L" is a line of the named file in this clone): `assembly-status.md` (whole); `st1-r4.md` L1–191, L650–697, L771–1128, L1129–1468, L1528–1591, L1687–1710; `f-meas.md` L1–60, L590–649; `geoh.md` L207–257 and anchors L248–253, L352–386; `descent.md` (whole, 319 lines); `dom-draft.md` L1–117, L246–342 and anchors; `dr.md` L170–182, L592–628; `in1.md` L221–236, L664–676; `gates/st1-r4-gate.md` anchors L32, L40, L61, L65, L69. SA (`scratchpad/sa/ym4.tex`): L7165–7195 (soft gauge factor), L17360–17400 (Lemma 2.2), L17510–17570 (the operation **T** and its stored stage), L17612–17630 (graded stage thresholds). CA-I (`ca_I.tex`): L74300–74324 (stage collar and rim). I did not read p82.md, pr-lay.md, hm.md, fp1.md or cp12.md beyond the anchors that other frozen texts quote; where I use them I cite the quoting line.

**Words.** *Proved* means proved here by a written argument from named frozen imports (each frozen text is itself an implication from its own imports). *Reduced* means proved here to follow from a named statement owned by another critical-path item. *Outstanding* means not proved here. *Moved variable* means a coordinate of the free removed rows \(F\) of the stage, or a function of them through F2's chart (the pivots); it never means a rim coordinate \(\mathfrak a\), a retained row, or the new datum \(W\).

**Name clash.** The frozen FC texts write \(\kappa_j\) for the coefficient of the action \(\mathcal S\) in the stage exponent (st1-r4 L1221, L1431). This is not IN1's consumer rate \(\kappa\) (in1 row 4). Below, \(\kappa_j\) always means the former; IN1's rate is written \(\kappa\) with no index.

## 0. Results

| Clause | Result here | Status |
|---|---|---|
| FC-mean-match (a) "its Gaussian" | Theorem 3.4(a): the stage precision is the Hessian of \(\kappa_j\mathcal S+\Gamma\) at the CV critical reference; the absolute (SA 7181) and relative (Y3) gauge readings give the same Hessian there, real or complex (Lemma 3.1); Remark 3.4′ gives the identification argument, one reading of which is flagged for the referee | **proved** (identification reading flagged) |
| FC-mean-match (b) "linear/seam terms" | Lemma 3.2: the linear term of \(\kappa_j\mathcal S+\Gamma\) at \(\beta=0\) is exactly zero at every datum in use, with no coverage premise on the gauge pairs; every other linear term is assigned to the remainder and written explicitly (Definition 3.3) | **proved** |
| FC-mean-match (c) "slot coupling" | Theorem 3.4(c): \(S\), the centre \(m\) and the reference do not depend on the rim coordinates \(\mathfrak a\); the rim/collar coupling is the explicit term (3.6) of the remainder | **proved** |
| FC-mean-match (d) "switch/external-pair dependence" | Theorem 3.4(d) and Proposition 3.5: \(S,m\) depend on switches and on the external pair only through the stage datum, holomorphically; the local split centred at \(Z=0\) (the localized reference \(V^\sharp\)) differs from (FCr) by an explicit term bounded by \(s_1N\mu_\sharp(2b+\tfrac12\mu_\sharp)\), \(\mu_\sharp\le g^{-1}\sqrt{M_*C_F}e^{-aR_\sharp/2}\) | **proved** (Proposition 3.5 uses frozen F6 and FC7, hence LOC) |
| FC-mean-match, the consequence for F5 | Corollary 3.6: \(m_r=0\), \(\vartheta_m=0\), \(\varepsilon_m=1/16\) | **proved** |
| FC-mean-match, "otherwise its additional conditional force must be bounded" | Proposition 3.7: the stationary point of the quadratic model of the full exponent lies within \(2\sqrt{3N}\mathcal M/(c_Sb)\) of \(m\), given NL1/LF1's positive precision \(c_S\) and a remainder majorant \(\mathcal M\) on the tube | **reduced** to the NL1/LF1 inputs that st1-r4 L1450 already names; not needed for (FCr) |
| FC-test, gauge exponent (\(\operatorname{Re}\operatorname{tr}\)) | Lemma 4.1 | **proved** |
| FC-test, gauge indicators \(\mathbf 1\{|V(y,x)-\mathbf 1|<\varepsilon\}\) (gate L65, st1-r4 L1212) | Lemma 4.2: redundant on the whole passing domain \(D_b\), by CV, after a \(\gamma\)-ceiling | **proved** |
| FC-test, factors not reading moved rows; tests of level \(\ge j+1\); rim tests | Lemma 4.3: independent of the moved coordinates | **proved** |
| FC-test, carried activities, forms, normalizers, strip factors, earlier stages | Lemma 4.4: holomorphic in the moved coordinates | **reduced** to CI, DR and Theorem 14 (75), as already declared; earlier stages by induction |
| FC-test, older datum-loop tests (58) on loops that read a moved row | §4.6: three attacks | **Outstanding: Lemma OT** (first remaining statement) |
| Constants | §6: every FCON constant is fixed at IN1 row 2–3 (ST1 row 2), before \(\kappa\), independent of \(M,\bar\kappa\); all \(M\)-, \(\bar\kappa\)- and amplitude-dependence sits in the final \(\gamma\)-ceiling (IN1 row 9, ST1 row 10) | **proved** |

**First remaining Outstanding statement: Lemma OT (older-test margin), §4.6.** For every passing stage of level \(j\) in an admitted history, every real datum \(W\) in use, and every older test of the stored integrand of the form \(\mathbf 1\{|\partial D(\tau)-I|<t_\tau\}\) on a datum loop \(\tau\) whose stencil contains a moved row, the CV reference \(V=M_-(U_+)\) satisfies
\[
 |\partial V(\tau)-I|\le t_\tau-4C_{\rm ch}L^4\cdot\tfrac98\,\delta'_j 
\]
(for a plaquette; \(\tfrac98n_\tau C_{\rm ch}L^4\delta'_j\) for a loop with \(n_\tau\) moved bonds). Attack 1 (fine-from-coarse regularity of the critical background) fails because no frozen text gives an \(L\)-uniform fine-from-coarse constant, and because inherited exponents are only bounded above. Attack 2 (SA's graded stage thresholds, SA 17612–17624) proves FC-test if the stage adds a reference-curvature test, but ST1's frozen stage test contains none; adding one is a design change whose new failing outcome must be paid by LF1, and no text supplies that. Attack 3 (split the indicator and continue from the open set where it is redundant) fails because the consumers need the actual stage value at every real datum in use, which is Lemma OT again. Details in §4.6.

**Statements used wrongly or imprecisely by frozen or drafted texts** (§7): (i) st1-r4 FC5 (L1221) states its conclusion under the premise "If these varying pairs are in those blocks"; that premise is a theorem (Lemma 2.2), so FC5 holds unconditionally at a CV critical reference. (ii) FC5 (L1218) writes the gauge exponent with \(\operatorname{tr}\), SA 7181 writes \(\operatorname{Re}\operatorname{tr}\); they agree on real data, and only the former continues holomorphically (Lemma 4.1); not an error, but the continuation must use FC5's form. (iii) `assembly-status.md` L130 and L148 list the edge "FCON → CI (stage contours)". No NL1/LF1 text consumes a stage contour explicitly (grep count of "contour" is 0 in `nl1-L.md`, `ci-form.md`, `td.md`, `drlocp.md`, `cls.md`, `in1.md`, `ag1.md`, `tp1.md`, `dr.md`, `cp12.md`, `pr-lay.md`). The only consumers are ST1 Theorem 14 hypothesis 5 and Corollary 14′ (gate L40 says the same), and through them dom-draft Theorem 8. The edge is right as a dependency, but the consumer is ST1, not a CI text. (iv) Theorem FC's phrase "the Hessian \(S\) … has zero linear term" (L1431–1432) is loose wording for Lemma 3.2. (v) The task brief names dom-draft's first Outstanding "Lemma LOC-flat" and its class "K-flat"; in this clone dom-draft's first Outstanding is **Lemma LOC♮** (L329) and its class is \(\mathcal K^\natural\). I read the clone.

Line count is given at the end of the reply, not here.

## 1. The two statements, exactly as the frozen consumers read them

### 1.1 FC-mean-match

Every occurrence in a frozen text, quoted:

* `st1-r4.md` L156 (§2, "Activity and contour supply"): "Its full conditional contour requires Outstanding FC-mean-match and FC-test. Theorem FC proves the geometric and analytic implication with those premises explicit."
* L903 (F-contour paragraph): "The full stored contour still requires **FC-mean-match** and **FC-test**. In particular a geometric centre is not automatically the mean of the stored quadratic form, and retained older Borel tests must be independent of the moved variables or proved redundant."
* L1254–1259: "**Outstanding FC6-history and FC-mean-match.** FC6 is not, as stated in pass 1, a proved counterexample for the actual conditional mean of an admitted stored history. A stationary point and the mean obtained by completing a specified quadratic form are different objects. After a nonlinear change to test coordinates a Gaussian need not remain Gaussian. One can choose a new Gaussian centred at (FC6b), putting the exact difference into its remainder; that choice does not identify the old Gaussian or prove a bound on the new remainder."
* L1269–1276: "For a stored quadratic form with exterior coordinate \(a\), \(\tfrac12 B^{\mathsf T}SB+B^{\mathsf T}Ra+\ell^{\mathsf T}B\) has centre \(-S^{-1}(Ra+\ell)\). (FC6c) Nothing in a representative choice sets \(R\) or \(\ell\) to zero. Stored forms may instead be assigned to the remainder, as in `shift-map.md` §14; this is exact bookkeeping, with a separate analytic bound to prove."
* L1445–1451 (Theorem FC, "Outstanding F-contour"): "Full closure for the actual stored stage still requires **FC-mean-match** (its Gaussian, linear/seam terms, slot coupling and switch/external-pair dependence) and **FC-test** (every remaining moved-variable factor satisfies the analytic premise). CV alone proves neither. If a matched Gaussian has exactly the split (FCr), then its chosen mean has \(m_r=0\), the threshold term vanishing (written \(\vartheta_m=0\), not RUN's \(\theta_m\)), and \(\varepsilon_m=1/16\) for the radius \(b_j\) of F5 (the value is valid for FC7's \(b\) as well); otherwise its additional conditional force must be bounded. The positive reference precision, its complex perturbation bound, and the full remainder bound remain the NL1/LF1 inputs."
* L1545 (Theorem 14, hypothesis 5): "To claim its actual complex conditional contour, require **FC-mean-match** and **FC-test**, as well as the uniform analytic majorants in FC2. These remain **Outstanding**."
* L1587 (Corollary 14′): "For assertions on its conditional contours, assume ST-test\(^{\rm hol}\), FC-mean-match and FC-test, with FC2's uniform analytic majorant. Theorem FC then supplies the exact-test containment and deformation."
* L1657 and L1665 (revision checks, Result): "**FM-match, FC-mean-match and FC-test remain Outstanding**"; "its actual conditional contour remains **Outstanding FC-mean-match/FC-test**."
* L1696 (status line): "Outstanding, all named: CI (NL1/LF1), FM-match, FC-mean-match, FC-test, FC6-history (unused)."
* `geoh.md` L253 (Lemma 10, frozen): "For its conditional contours retain ST-test\(^{\rm hol}\), FC-mean-match, FC-test and FC2's uniform analytic majorant."
* `gates/st1-r4-gate.md` L40: "**FC-mean-match** and **FC-test** enter only there [Theorem 14 hypothesis 5 and Corollary 14′] and in Theorem FC's statement of its premise."
* `f-meas.md` L388, L579–581, L632 (distilled, folded into st1-r4): the same sentences as st1-r4 L1254, L1445–1447, L1657.

**What F5 consumes.** Lemma F5 (L900–901): "Put \(b_j=9\delta'_j/(8g_j)\). Every contour point with \(|\Re B(b)|+|\Im B(b)|<b_j\) on every free row lies in \(\mathcal T_j\). So does a contour with \(|\Re B(b)|<b_j\) and \(|\Im B(b)|\le\epsilon_m b_j\), \(\epsilon_m<1\). … If \(m_r\) is real and \(|m-m_r|\le\epsilon_m b_j\), a translated contour has this imaginary bound whenever its real part stays in that region." So the consumer needs a *matched Gaussian centre* \(m\) and a real point \(m_r\) within \(\epsilon_mb_j\) of it.

**My reading (to be checked by the referee).** FC-mean-match is the identification of the Gaussian that the stage contour is centred on. It has four named parts, read from L1446:

* (MM-a) *its Gaussian*: which quadratic form in the moved coordinates is the stage's Gaussian;
* (MM-b) *linear/seam terms*: that form has no linear term at the reference, so the centre is not shifted as in (FC6c) by \(\ell\);
* (MM-c) *slot coupling*: it has no cross term \(B^{\mathsf T}Ra\) with the rim (exterior) coordinates, so the centre is not \(-S^{-1}Ra\);
* (MM-d) *switch/external-pair dependence*: its precision and centre depend on the decoupling switches and on the pair outside the stage only in a stated, holomorphic way.

The conclusion the consumer reads is L1449: with exactly the split (FCr), \(m_r=0\), \(\vartheta_m=0\), \(\varepsilon_m=1/16\). The alternative "otherwise its additional conditional force must be bounded" is the branch in which the chosen Gaussian is not (FCr).

L1450 excludes three items from FC-mean-match: "The positive reference precision, its complex perturbation bound, and the full remainder bound remain the NL1/LF1 inputs." I keep them excluded.

### 1.2 FC-test

* `st1-r4.md` L903 (quoted above): "retained older Borel tests must be independent of the moved variables or proved redundant."
* L1212 (FC5): "(FC-test includes the indicator in the moved variables that SA 7181's soft gauge factor contains.)"
* L1315–1327 (FC2, the premise FC-test must supply): "For fixed Borel parameters, if the full integrand remaining after the new test is removed is jointly holomorphic in \(Z,W\) on a neighbourhood of the integration contours, and the outer integral has a locally uniform integrable majorant, this formula is holomorphic in \(W\). It is the unique continuation on a connected chart containing an open real slice. … A bounded integrand alone is insufficient on an unbounded rim domain."
* L1329–1339: "**Outstanding FC-test.** The cited ST1 inputs do not supply FC2's premise for every stored stage. They retain older indicators exactly. F4 and CI give holomorphic coordinate maps and activities, not holomorphy of an older indicator depending on \(Z\). Such an indicator may be retained as a Borel parameter only if it is independent of moved coordinates, or proved redundant there. The outline's older-test implication at 17369–17396 and 17624 is the relevant additional statement; F7 explicitly does not prove it for the designed ST-test. This is a real obstruction to the proposed inference, not a boundary regularity convention. In one coordinate, \(\int_{-b}^{b}\mathbf1_{\{|z+x|<b\}}\,dz=2b-|x|\) for \(|x|<b\). The coordinate map is entire and the new domain fixed, but the result has no holomorphic extension at zero."
* L1447: "**FC-test** (every remaining moved-variable factor satisfies the analytic premise)."
* `gates/st1-r4-gate.md` L65: "SA's block-axial factor (7181) also carries the indicator \(\mathbf 1\{|V(y,x)-\mathbf 1|<\varepsilon_k\}\). It is a Borel factor in moved variables. FC-test's general wording covers it".
* L1545, L1587, geoh L253: as in §1.1.

**My reading.** FC-test is: every factor of the stored integrand \(\Theta\) that depends on the moved coordinates at fixed Borel parameters is either (i) a holomorphic function of \((Z,W)\) on a neighbourhood of the contours, or (ii) constant in \(Z\) on the real passing domain \(D_b\) for every real \(W\) in use ("independent of moved coordinates, or proved redundant there"). FC2's majorant is a separate item in L1545 and L1587 ("as well as the uniform analytic majorants in FC2"); I do not include it in FC-test, and I note its reduction in Remark 4.7.

### 1.3 Every place a stage contour is consumed

A stage contour is consumed where a statement integrates the moved coordinates over a complex contour, or asserts holomorphy in \(W\) of the stage integral off the real slice. From the grep above and the gate:

1. `st1-r4.md` Lemma F5 (L900–901): contour containment in the tube \(\mathcal T_j\), conditional on a matched centre.
2. Theorem FC (L1424–1451): FC1, FC2, FC7, FC8, FC9 and (FCr), with the two premises.
3. L1453: "using another stored presentation requires F-measure and, when a complex contour is consumed, F-contour."
4. Theorem 14 hypothesis 5 (L1545): "To claim its actual complex conditional contour".
5. Corollary 14′ (L1587) and its proof (L1589: "for an asserted integration contour use the additional containment/deformation supply").
6. `geoh.md` Lemma 10 (L253), which re-states Corollary 14′ with SLOT-ST.
7. `dom-draft.md` Theorem 8 item 5 (L265: "contours (F5, FC): item 7") and the hypothesis of Theorem 8 (L260: "where a contour is asserted, FC-mean-match and FC-test (item 7)"); consumer note L59 for ST-test\(^{\rm hol}\) (unrefereed).
8. `td2.md` L38 (distilled): admission through st1-r3 Theorem 14 and Corollary 14′ "with their actual-domain and F-measure/F-contour qualifications where applicable".

No other frozen or distilled text in this clone consumes a stage contour (grep count of "FC-mean-match\|FC-test\|F-contour" is zero outside `FINISH.md`, `gates/st1-gate.md`, `gates/st1-r4-gate.md`, `f-meas-draft.md`, `f-meas.md`, `st1-r3.md`, `st1-r4.md`, `td2.md`, `geoh.md`, `dom-draft.md`, `assembly-status.md`).

## 2. The actual stage

### 2.1 The actual construction

As fixed by the task and by dom-draft L75: SA's step with
(A1) the Y3 relative soft-gauge form of frozen `descent.md` (Lemma 2, Theorem 5) for the gauge part of every Gaussian precision;
(A2) ST1's chart-free intrinsic domains with the radius table (Tq0) (`st1-r4.md` L82–89) and unit lifts \(\lambda_\tau\equiv1\), \(\Lambda_Q=1\);
(A3) Amendment CV's averaged-contour representative (`st1-r4.md` L41, L1140–1144);
(A4) SLOT-ST for every stored Haar/delta stage (Amendment GS, `st1-r4.md` L1705; `geoh.md` L248). No CA-I presentation is identified, so neither SLOT-CA nor FM-match is used (they are only for "a separately fixed CA-I presentation", L1587).

Under (A4) the stage is an intrinsic object: its integrand is the one Theorem FM specifies, and the split of its exponent is a declaration of this construction. Theorem FM explicitly allows any declared split: L1072, "For any declared split \(\mathcal A=\mathcal W+\mathcal K\), and symmetric forms \(S_a,S_B\)", with the exact identity (FMg). This is the freedom §3 uses. It is not a relabelling of a separately frozen presentation, which L1591 forbids ("No NL1/LF1 estimate follows from relabelling a remainder"): no estimate is inferred from the split.

### 2.2 Stage data and notation

Fix one passing stage of level \(j\) in an admitted finite history, enlarging member \(j+1\). Use `geoh.md` Definition 5 (L209–217): \(S=\Omega^{\rm old}_{j+1}\), \(Y\) the new part, \(E\) the removed rows, \(C_+\) the added rows, \(F=E\setminus p(C_+)\) the free removed rows, \(N=|F|\); Lemma 9 there gives \(E=\Gamma^{\rm rm}\), \(C_+=\Gamma^{\rm ad}\). Write \(W=D_+\) for the new datum, \(U_+\) for its CV canonical real regular critical background, \(V=M_-(U_+)\), and \(V^\sharp=M_-(U_+^\sharp)\) for the localized reference of ST-test (L152). Put \(g=g_j\), \(\delta'=\delta'_j\), \(b=\delta'/g\), and, as in (FC0) (L1293–1298),
\[
 \eta_e=i^{-1}\operatorname{Log}(V_e(V_e^\sharp)^{-1}),\quad
 Z_e=g^{-1}i^{-1}\operatorname{Log}(D_e(V_e^\sharp)^{-1}),\quad
 u_e(Z)=i^{-1}\operatorname{Log}(e^{igZ_e}e^{-i\eta_e}),\quad m_e=\eta_e/g ,
\]
and \(\beta=u/g\), the free coordinate relative to \(V\). The moved field is \(D(Z)=e^{ia_V(u(Z))}V\) on \(E\), with F2's chart \(a_V(u)=\Psi_V(\mathsf C_Vu)\), and \(V\) on retained rows. FC1 (L1303–1313) gives the passing domain \(D_b=\{|Z_e|<b\}\).

**Two identities used repeatedly.**
(2.1) On a free row \(e\in F\): \(e^{iu_e}V_e=e^{igZ_e}e^{-i\eta_e}V_e=e^{igZ_e}V^\sharp_e\), since \(e^{i\eta_e}=V_e(V^\sharp_e)^{-1}\). So \(D_e=e^{igZ_e}V^\sharp_e\) on free rows.
(2.2) On real data with \(Z\in D_b\) and \(h=\|\eta\|\le\delta'/8\) (F6): the group angle of \(D_eV_e^{-1}\) on a free row is \(|u_e|<\delta'+\delta'/8=\tfrac98\delta'\) (the real group triangle inequality, as in FC1's proof), and on every removed row \(\|a_V(u)\|\le C_{\rm ch}L^4\|u\|<\tfrac98C_{\rm ch}L^4\delta'\) (F2).

### 2.3 Which factors read moved rows

**Definition 2.1.** A *factor* of the stage is one factor in the product that defines the stored integrand \(\Theta(\mathfrak a,D)=\Xi(\mathfrak a,D)e^{\mathcal A(\mathfrak a,D)}\) of Theorem FM (L1045–1047: "It includes every earlier normalizer, Gaussian weight, gauge factor, strip Jacobian and test"). A factor is *moved* if, at fixed rim coordinates \(\mathfrak a\), fixed retained rows and fixed \(W\), its value changes with \(D|_E\).

**Lemma 2.2 (moved reads of gauge contours).** Let \(y\) be a level-\((j+1)\) block centre and \(x\in B(y)\setminus\{y\}\). The contour mean \(D(y,x)\) of a level-\(j\) field \(D\) reads only bonds with both endpoints in \(B(y)\). Consequently: (i) if \(B(y)\) is a new-member block (st1-r4 L1131–1132), \(D(y,x)\) reads only free removed rows, and \(D(y,x)\) is a function of \(Z|_{\operatorname{Bd}^\circ(B(y))}\) and \(V^\sharp\) alone; (ii) if \(B(y)\) is not a new-member block, \(D(y,x)\) reads no removed row and is not moved.

*Proof.* The contour family from \(y\) to \(x\) consists of "the at most \(4!\) shortest paths completing each coordinate displacement before the next" (p82 L45, quoted; st1-r4 L36 defines \(\mathcal M\) with the same family). Along such a path each coordinate moves monotonically from that of \(y\) to that of \(x\). Hence every site on the path has each coordinate between those of \(y\) and \(x\). A block is a centred aligned cube (st1-r4 L9), so coordinatewise convex; both endpoints lie in \(B(y)\), hence every site and every bond of the path lies in \(B(y)\). The mean (st1-r4 L36: "\(\operatorname{av}(V_i)\) solves \(\sum_i\log(V_iV^{-1})=0\)") is a function of the path products only.

(i) Let \(B(y)\subset\Omega^+_{j+1}\setminus\Omega^-_{j+1}\). By st1-r4 L1134–1137, "Its internal level-\(j\) bonds were old determining rows and are removed by this stage … Pivots cross block faces, so internal bonds are free." So every bond read is in \(F\), and by (2.1) its value is \(e^{igZ_e}V^\sharp_e\).

(ii) If \(B(y)\subset\Omega^-_{j+1}\), its internal level-\(j\) bonds have both endpoints in \(\Omega^-_{j+1}\), so they were not determining at level \(j\) in either system (st1-r4 L26: a determining row has "no endpoint in \(\Omega_{q+1}\)"); they are not removed rows. If \(B(y)\cap\Omega^+_{j+1}=\varnothing\), its internal bonds have no endpoint in \(\Omega^\pm_{j+1}\) and keep their status: retained rows or non-rows. Members are unions of aligned blocks (st1-r4 L22, GEO), so no other case occurs. In neither case is a removed row read. ∎

**Remark.** Lemma 2.2 discharges the premise "If these varying pairs are in those blocks" of FC5 (st1-r4 L1221): every pair whose factor varies with the moved coordinates lies in a new-member block.

**Lemma 2.3 (tests of level at least \(j+1\)).** A factor that reads \(D\) only through its averages onto level-\((j+1)\) rows of the new system, through retained rows, or through rows of levels other than \(j\), is not moved.

*Proof.* On the stage fibre \(F(D)=W\) (st1-r4 (67), F4 (70): \(F(D_{\rm old})=D_+\)): every added row's average equals \(W\), retained rows are copied. Rows of other levels are different coordinates; the stage varies "Only the removed rows" (L793). By `geoh.md` Lemma 9's proof (L225), "Rows at other levels do not change." An old level-\((j+1)\) row with an endpoint in \(Y\) has its other endpoint in \(S\) (since \(Y\cap\Omega_{j+1}^{\rm old}=\varnothing\) and it is an old row); in the new system both endpoints lie in \(\Omega^{\rm new}_{j+1}\) and none in \(\Omega_{j+2}\subset S\), so it is still a row and is retained. ∎

### 2.4 The factor classes

By Definition 2.1 and the description in Theorem FM (L1045–1047), SA's stored stage (SA 17531: \(\mathbf T^{(j)}=\int dV_j|_{\Omega_{j+1}^c}\delta(\mathcal M(V_j)V_{j+1}^{-1})\,\mathfrak G_j\,\chi\chi^c\,z^{(j)}\int dA'\,\chi\chi^c\,e^{-\frac12\langle A',[\Delta^{(j)}-\Delta^{(j)}C^{(j)}\Delta^{(j)}]A'\rangle}\)), and SA's carriage rule (SA 17558: "in an integral operation that a term carries, the tests, the gauge factors and the delta functions depend on no background, whereas the forms \(\Delta^{\rm loc}_{\mathfrak k}\) and the factors \(z^{(j)}\) do"), the factors of \(\Theta\) fall into these classes:

* **(H) analytic factors:** the carried activities and regular-action terms (\(E,R,B\)), the kept forms \(\Delta^{\rm loc}_{\mathfrak k}\) and normalizers \(z^{(j)}\) as pair functions, the strip Jacobians (F1), the Haar and chart factors (FM3), and the outputs of earlier stages of the same operation;
* **(G) the soft gauge factor** \(\mathfrak G_j\) (SA 7181): for each carried pair, \(z_{\mathfrak G}^{-1}\mathbf 1\{|V(y,x)-\mathbf 1|<\varepsilon_j\}e^{-x_j(1-\frac12\operatorname{Re}\operatorname{tr}V(y,x))}\);
* **(T) tests:** (T1) tests of rim fluctuation fields and of coordinates other than level-\(j\) rows; (T2) tests of level \(\ge j+1\) data; (T3) older datum-loop curvature tests (58) on level-\(j\) loops; (T4) the passing tests of earlier stages; (T5) the strip cutoffs \(\vartheta_{\rm co}\);
* **(Fl) failure factors** \(1-\chi\) of stopped stages.

The Wilson weight is in \(e^{\mathcal A}\), not in the operation (SA 17534: "This operation contains no Wilson weight. That weight belongs to \(\exp A_{k,\mathcal S}\)").

**Completeness of the list.** This list is my reading of Theorem FM's "every earlier normalizer, Gaussian weight, gauge factor, strip Jacobian and test" together with SA 17531–17560. The referee should check whether the actual construction carries any other factor in moved variables. If one exists, it falls under FC-test's general wording and must be added to §4.

## 3. FC-mean-match

### 3.1 The reference and the two gauge readings

**Lemma 3.1 (the CV reference is axial on every moved pair, real and complex).** At every datum \(W\) in use (real, or complex in ST-test\(^{\rm hol}\)'s chart), for every new-member block \(B(y)\) and every \(x\in B(y)\setminus\{y\}\), \(V(y,x)=I\). Consequently, for every such pair the absolute function \(D\mapsto1-\tfrac12\operatorname{tr}W^V_{y,x}(D)\), \(W^V_{y,x}(D)=(e^{iD}V)(y,x)\), and the relative function \(D\mapsto1-\tfrac12\operatorname{tr}\widehat W^V_{y,x}(D)\), \(\widehat W^V_{y,x}(D)=W^V_{y,x}(D)W^V_{y,x}(0)^{-1}\), are the same function of \(D\); in particular their Hessians at \(D=0\), the pair's terms of \(\mathsf G^{\rm abs}_V\) and \(\mathsf G^{\rm Y}_V\) in `descent.md` (3), coincide.

*Proof.* Each noncentre site \(x\) of a new-member block is "an old node but no new node" with "new parent \(y\)" (st1-r4 L1135–1137). Amendment CV (L1140–1141) sets \((\mathcal M^nU)(z,x)=I\) at every nonnode with parent \(z\), for the canonical background of the system in question; here the system is the new (+) one and \(n=j\). On removed rows \(V=M_-(U_+)\) is the level-\(j\) average \(\mathcal M^jU_+\) (st1-r4 (4)), and by Lemma 2.2(i) the contour \(V(y,x)\) reads only removed rows. So \(V(y,x)=(\mathcal M^jU_+)(y,x)=I\) at real data. (FC5, L1223, records the same: "Under CV, \(V_{\rm ax}=V\).") On the complex chart, \(W\mapsto V(y,x)\) is holomorphic (A1/F0/REG's local analytic continuation of the background and the analytic branch of the mean, st1-r4 L128, L36–41) and equals \(I\) on an open real set; the chart is connected (ST-test\(^{\rm hol}\), L154: a ball), so \(V(y,x)\equiv I\) there by the identity theorem. With \(W^V_{y,x}(0)=V(y,x)=I\), \(\widehat W=W\); this is the case "If \(W(0)=I\), the absolute and relative functions themselves coincide" of `descent.md` Lemma 2 (proof, L142), which also states (L131) that \(\mathsf G^{\rm Y}_V\) "equals \(\mathsf G^{\rm abs}_V\) at every block-axial \(V\), real or complex". ∎

So on the actual construction (A1) and SA's literal stored factor (SA 7181, absolute) give the same stage Gaussian. This is the only point where (A1) enters FCON. Off the reference (at \(D\ne V\)) the stored factor is SA's absolute function; FCON never needs it to equal the relative one there, since everything beyond second order is kept exactly in the remainder (Definition 3.3).

### 3.2 The linear term

Write \(D_\beta=e^{ia_V(g\beta)}V\) on \(E\) (and \(V\) on retained rows), \(\mathcal S(D)=S_{\Omega_0}(\Phi_-(D))\) as in FC3 (L1195), and, for any set \(\mathcal P\) of carried pairs,
\[
 \Gamma_{\mathcal P}(D)=x_j\sum_{(y,x)\in\mathcal P}\bigl[1-\tfrac12\operatorname{tr}D(y,x)\bigr]\qquad\text{(FC5, L1218).}
\]

**Lemma 3.2 (zero linear term).** At every datum in use, real or complex, and for every set \(\mathcal P\) of carried pairs,
\[
 \frac{d}{dt}\Big|_{t=0}\bigl[\kappa_j\mathcal S(D_{t\beta})+\Gamma_{\mathcal P}(D_{t\beta})\bigr]=0\qquad\text{for every }\beta.          \tag{3.1}
\]
No coverage hypothesis on \(\mathcal P\) is used.

*Proof.* *Action.* FC3 (L1196–1199): "The derivative of \(B\mapsto\mathcal S(e^{ia_V(gB)}V)\) vanishes at zero. Indeed its curve lies in the fixed \(M_+\)-fibre, by \(M_+=F_{\rm av}\circ M_-\). At zero, uniqueness identifies its background with \(U_+\) modulo a residual \(M_-\)-gauge. Criticality and gauge invariance annihilate that derivative. The identity theorem gives the complex version." I use it as stated.

*Gauge.* Split \(\mathcal P=\mathcal P_{\rm mv}\cup\mathcal P_0\), where \(\mathcal P_{\rm mv}\) are the pairs in new-member blocks. By Lemma 2.2(ii) the terms of \(\mathcal P_0\) do not depend on \(\beta\). For \((y,x)\in\mathcal P_{\rm mv}\) put \(w(t)=D_{t\beta}(y,x)\). By Lemma 3.1, \(w(0)=I\). The map \(t\mapsto w(t)\) is holomorphic near \(0\) with values in \(SL(2,\mathbb C)\): it is the continuation of the real mean, which lies in \(SU(2)\) (descent L121: "The real mean lies in \(SU(2)\)"), so \(\det w(t)\) is holomorphic and equals \(1\) for real data, hence identically. Write \(w(t)=\exp(iH(t))\) on the branch near \(I\) with \(H(0)=0\); \(\det w=1\) gives \(\operatorname{tr}H(t)=0\). Then
\[
 \frac d{dt}\Big|_0\bigl[1-\tfrac12\operatorname{tr}w(t)\bigr]=-\tfrac12\operatorname{tr}\bigl(i\dot H(0)\bigr)=0 .
\]
This is the computation in `descent.md` Lemma 2's proof (L137–142), at a complex \(V\) with \(w(0)=I\). Summing over pairs proves (3.1). ∎

**Consequence for FC5's premise.** FC5 (L1221) asserts \(d(\kappa_j\mathcal S+\Gamma)=0\) at \(V_{\rm ax}\) "If these varying pairs are in those blocks". Lemma 2.2 proves that every varying pair is in a new-member block, and Lemma 3.2 proves the conclusion directly, for complex data too and for any carried subset. The premise is therefore not an open input.

### 3.3 The declared split

**Definition 3.3 (the stage split of the actual construction).** Let \(\Theta=\Xi e^{\mathcal A}\) be the stored integrand of Theorem FM (L1045–1047). Declare
\[
 \mathcal W(\mathfrak a,D):=-\kappa_j\mathcal S(D)-\Gamma_{\mathcal P}(D),\qquad \mathcal K:=\mathcal A-\mathcal W,               \tag{3.2}
\]
with \(\mathcal P\) the carried pairs of the stored soft gauge factor (its exponent written with \(\operatorname{tr}\), Lemma 4.1). \(\mathcal W\) does not depend on \(\mathfrak a\). Declare the symmetric forms
\[
 S_B:=S:=-\operatorname{Hess}_{\beta=0}\,\mathcal W(D_\beta),\qquad S_a:=\Delta^{\rm loc}(V),                     \tag{3.3}
\]
where \(\Delta^{\rm loc}(\cdot)\) is the stored rim form (SA 17555–17558: the kept form \(\sum_{\mathfrak k}\langle A',\Delta^{\rm loc}_{\mathfrak k}A'\rangle\), "given as functions of a pair \((\mathbf U,\mathbf J)\) near \(\mathfrak k\)"), evaluated at the pair of the reference, i.e. at \(\beta=0\). The Gaussian factor of the stage, in test coordinates, is
\[
 e^{-\frac12(Z-m)^{\mathsf T}S(Z-m)},                                                                              \tag{3.4}
\]
and the remainder is
\[
 \mathcal R(\mathfrak a,Z)=R_{\rm rec}(Z)+T_3(Z)+P_{\rm slot}(\mathfrak a,Z)+K'(\mathfrak a,Z)+J'(Z),                  \tag{3.5}
\]
with \(R_{\rm rec}\) as in (FCr) (L1435–1436),
\[
 \begin{aligned}
 T_3(Z)&=\mathcal W(D(Z))-\mathcal W(V)+\tfrac12\beta(Z)^{\mathsf T}S\beta(Z),\\
 P_{\rm slot}(\mathfrak a,Z)&=-\tfrac12\bigl\langle\mathfrak a,[\Delta^{\rm loc}(D(Z))-\Delta^{\rm loc}(V)]\mathfrak a\bigr\rangle,          \\
 K'(\mathfrak a,Z)&=\mathcal K(\mathfrak a,D(Z))-\mathcal K(\mathfrak a,V)-P_{\rm slot}(\mathfrak a,Z),\\
 J'(Z)&=\sum_{e\in F}\log s(g^2Q(Z_e))+\log\bigl[\Pi_V(u(Z))/z_V\bigr],
 \end{aligned}                                                                                                      \tag{3.6}
\]
where \(\beta(Z)=u(Z)/g\), \(s,Q\) are as in FM1 and \(\Pi_V,z_V\) as in FM3–FM5, the logarithms taken by continuation from \(Z=m\) (where \(u=0\)) as in (FMd) (L1067–1070).

**Lemma 3.3′ (the split is exact).** At real data, for nonnegative Borel or absolutely integrable integrands, the passing stage integral (FC2) equals
\[
 (\sigma_Hg^3)^Nz_V\,e^{\mathcal W(V)}\int d\mathfrak a\,e^{\mathcal K(\mathfrak a,V)}\int_{D_b}dZ\,\Xi(\mathfrak a,D(Z))\,
 e^{-\frac12(Z-m)^{\mathsf T}S(Z-m)+\mathcal R(\mathfrak a,Z)} ,                                                   \tag{3.7}
\]
and \(\mathcal K(\mathfrak a,V)=-\tfrac12\langle\mathfrak a,S_a\mathfrak a\rangle+\mathcal K^\circ(\mathfrak a)\), where \(\mathcal K^\circ\) collects the \(\mathfrak a\)-dependence of the other stored terms at the reference. No factor has been removed.

*Proof.* FC2 (L1317–1319) is \((\sigma_Hg^3)^N\int d\mathfrak a\int_{D_b}dZ\prod_{e\in F}s(g^2Q(Z_e))\Pi_V(u(Z))\Theta(\mathfrak a,e^{ia_V(u(Z))}V)\), with the new test already giving the domain \(D_b\) (FC1). Write \(\prod_es(g^2Q(Z_e))\Pi_V(u(Z))=z_Ve^{J'(Z)}\) (the branch of the logarithm is the one continued from \(Z=m\), where \(u=0\), \(\Pi_V(0)=z_V\) by FM5's definition with \(\det D\Psi_V(0)=1\) and \(a_V(0)=0\); the products are near one by (FMd)'s bounds, L1067–1070). Write \(\mathcal A=\mathcal W+\mathcal K\) and add and subtract: \(\mathcal W(D(Z))=\mathcal W(V)-\tfrac12\beta^{\mathsf T}S\beta+T_3\), \(-\tfrac12\beta^{\mathsf T}S\beta=-\tfrac12(Z-m)^{\mathsf T}S(Z-m)+R_{\rm rec}\) (this is (FCr)), \(\mathcal K(\mathfrak a,D(Z))=\mathcal K(\mathfrak a,V)+P_{\rm slot}+K'\). Every step is an identity of finite sums; Tonelli (or Fubini under absolute integrability) handles the rim integral, as in Theorem FM's proof (L1089–1092). The decomposition of \(\mathcal K(\mathfrak a,V)\) is the definition of \(\mathcal K^\circ\). ∎

This is Theorem FM's (FMg) for the declared split (3.2)–(3.3), written in test coordinates; FM's own statement allows it (L1072).

### 3.4 FC-mean-match for the actual stage

**Theorem 3.4 (FC-mean-match).** Assume the actual construction (A1)–(A4), ST1's declared inputs used by FC0–FC9 (GEO, CH/F2, A1/F0/REG, OPS/SLICE/UNQ, DR/(15), AV/CURV, PROF/RCG4, RUN/RUN-low, ST-test, ST-test\(^{\rm hol}\) and one LOC clause, L924), and the \(\gamma\)-ceilings of Theorem FC. Then the matched Gaussian of the stage is (3.4) and:

(a) *(its Gaussian)* \(S\) is the Hessian at the CV critical reference of \(\kappa_j\mathcal S+\Gamma_{\mathcal P}\) in the free coordinate \(\beta\); it is holomorphic in \(W\) on the chart and real symmetric on real data; it is the same for the absolute (SA 7181) and relative (Y3) gauge readings.

(b) *(linear/seam terms)* The Gaussian (3.4) has no linear term relative to its centre \(m\), and \(T_3\) vanishes to third order at \(Z=m\). Every other linear term of the stored exponent at the reference, including every seam term, is a term of \(P_{\rm slot}+K'+J'\) in (3.5) and is kept exactly.

(c) *(slot coupling)* \(S\), \(m\) and \(V\) do not depend on the rim coordinates \(\mathfrak a\). The whole rim/collar coupling is \(P_{\rm slot}+K'\); \(P_{\rm slot}\) vanishes at \(Z=m\) for every \(\mathfrak a\) and is a quadratic form in \(\mathfrak a\).

(d) *(switch/external-pair dependence)* \(S\) and \(m\) are holomorphic functions of the stage datum on the chart. Along any family of stage data holomorphic in decoupling switches, \(S\) and \(m\) are holomorphic in the switches. Their dependence on the pair outside the quarter-cell enlargement \(X^\sharp\) is only through \(V\); for the centre, Proposition 3.5 bounds it.

(e) The split is exact (Lemma 3.3′). Hence "a matched Gaussian has exactly the split (FCr)" (L1448) holds for the actual stage.

*Proof.* (a) Definition (3.3), with Lemma 3.1 for the two readings. Holomorphy: \(\beta\mapsto\mathcal W(D_\beta)\) is holomorphic jointly in \(\beta\) and \(W\) (F2's chart is jointly holomorphic in \(u,V\), L850; \(\mathcal S\) is the action of the continued background, A1/F0/REG; the contour means are holomorphic on AV's branch); Hessians of jointly holomorphic functions are holomorphic in the parameter. Reality and symmetry at real data: \(\mathcal W\) is real there (\(\operatorname{tr}\) of \(SU(2)\) elements is real) and twice differentiable.

(b) Relative to the centre \(m\), (3.4) is a pure quadratic form. For \(T_3\): the function \(\beta\mapsto\mathcal W(D_\beta)-\mathcal W(V)\) is holomorphic near \(0\), vanishes at \(0\), has zero first derivative by Lemma 3.2, and has second derivative \(-S\) by (3.3); so \(T_3=\mathcal W(D_\beta)-\mathcal W(V)+\tfrac12\beta^{\mathsf T}S\beta\) has a zero of order at least three at \(\beta=0\), that is at \(Z=m\) (since \(u(m)=0\), FC0, L1300). The remaining terms of (3.5) are by definition all the other terms of the stored exponent; a seam term (a term present only next to a region boundary, the \(t\)-terms of SA 17534, or the difference between the regional action and the action of the stored term at incomplete stars) is a part of \(\mathcal K\), hence of \(P_{\rm slot}+K'\). No linear term has been deleted; all are in \(\mathcal R\).

(c) \(V\) is determined by \(W\) (st1-r4 L1194; F4, L879); \(m=\eta/g\) by \(V,V^\sharp\), and \(V^\sharp\) by the localized rule applied to \(W|_{X^\sharp}\) (ST-test, L152); \(S\) by \(V\) and \(\mathcal W\), and \(\mathcal W\) does not read \(\mathfrak a\) (3.2). \(P_{\rm slot}\) is visibly quadratic in \(\mathfrak a\) and vanishes when \(D(Z)=V\), i.e. at \(Z=m\).

(d) Holomorphy in the datum is (a) and FC0 (\(\eta\) is a logarithm of a holomorphic product, on the branch fixed by \(h\le\delta'/8\)). Composition with a family holomorphic in switches preserves holomorphy. \(S\) and \(m\) read the external pair only through \(V=M_-(U_+)\), since \(V^\sharp\) reads only \(W|_{X^\sharp}\) by ST-test's locality clause.

(e) Lemma 3.3′. ∎

**Remark 3.4′ (why (3.4) is the matched Gaussian, not a relabelling).** L1258–1259 warns that choosing a Gaussian and "putting the exact difference into its remainder … does not identify the old Gaussian". Under (A4) there is no old collar Gaussian to identify. (1) SA's stored stage operation carries no Wilson weight: SA 17534, "This operation contains no Wilson weight. That weight belongs to \(\exp A_{k,\mathcal S}\)". Its only stored quadratic form is the rim form \(\langle A',[\Delta^{(j)}-\Delta^{(j)}C^{(j)}\Delta^{(j)}]A'\rangle\) (SA 17531), a form in the rim coordinates \(\mathfrak a\) alone. (2) No CA-I presentation is identified (SLOT-CA and FM-match unused), so no separately frozen collar form \((A_j,B_j)\) exists in this construction. (3) The consumer's Gaussian is named by L1450: "The positive reference precision, its complex perturbation bound, and the full remainder bound remain the NL1/LF1 inputs." The reference precision is the Hessian of the reference exponent at the critical reference, which is \(S\) of (3.3). (4) Every other quadratic or linear term in \(\beta\) (the \(\mathfrak a\)-dependent second derivatives of the rim form, the regular-action terms, the Jacobians) is in \(\mathcal R\); L1275–1276 permits exactly this: "Stored forms may instead be assigned to the remainder, as in `shift-map.md` §14; this is exact bookkeeping, with a separate analytic bound to prove." The separate bound is the NL1/LF1 remainder bound, which Theorem 3.4 does not claim. The referee should check (3): if NL1/LF1's Gaussian estimate at a stage is designed around a different precision (for instance one including the \(\mathfrak a\)-averaged second derivative of the rim form), then the matched Gaussian is that one, its centre is shifted by the corresponding linear term, and Proposition 3.7 is the branch that applies.

**Corollary 3.6 (what F5 receives).** Under Theorem 3.4 the chosen mean is \(m\), and one may take \(m_r=0\), \(\vartheta_m=0\) and \(\epsilon_m=1/16\) in Lemma F5.

*Proof.* FC7 (L1345): \(|m_e|\le b/16\). Since \(b=\delta'/g<9\delta'/(8g)=b_j\), \(|m-0|\le b/16<b_j/16=\epsilon_mb_j\) with \(\epsilon_m=1/16\). The real point \(m_r=0\) is the centre of the real test ball, so no threshold shift is needed (\(\vartheta_m=0\)). This is st1-r4 L1449, with the gate's notation fix (gate finding 3, L61). For the contour itself, FC9 with \(\nu=\Im m\), \(|\nu_e|\le b/16\), passes through the centre's imaginary part on the inner ball \(|\beta_e|\le r_-b\) (L1404–1406). ∎

**Status of §3.1–3.4: proved**, from the frozen imports named, with no new input. What is *not* proved here, and is not part of FC-mean-match by L1450: positivity of \(\operatorname{Re}S\) (the "positive reference precision"), the bound on \(S\)'s complex perturbation, and the bound on \(\mathcal R\) (the "full remainder bound"); these "remain the NL1/LF1 inputs".

### 3.5 External-pair dependence of the centre: the local split

The centre \(m\) reads the external pair through \(V\). A consumer that prefers a Gaussian centred at the local reference can use the following exact alternative.

**Proposition 3.5 (local recentring).** Assume Theorem FC's hypothesis that \(S\) has row-sum bound \(s_1\) (L1439) on the chart. With centre \(0\) instead of \(m\),
\[
 -\tfrac12(Z-m)^{\mathsf T}S(Z-m)=-\tfrac12Z^{\mathsf T}SZ+R_{\rm loc}(Z),\qquad R_{\rm loc}(Z)=m^{\mathsf T}SZ-\tfrac12m^{\mathsf T}Sm,          \tag{3.8}
\]
and on \(T^\sharp_{2b}\)
\[
 |R_{\rm loc}(Z)|\le s_1N\mu_\sharp\,(2b+\tfrac12\mu_\sharp),\qquad
 \mu_\sharp:=\max_e|m_e|\le g^{-1}\sqrt{M_*C_F}\,e^{-aR_\sharp/2}.                          \tag{3.9}
\]
Moreover \(\mu_\sharp/b\to0\) uniformly over the stage window as \(\gamma\to0\).

*Proof.* (3.8) is the expansion of the quadratic form, using \(S=S^{\mathsf T}\). For (3.9): \(|m^{\mathsf T}SZ|\le\sum_e|m_e|\sum_{e'}|S_{ee'}||Z_{e'}|\le N\mu_\sharp s_1\max|Z_{e'}|\), and \(|Z_{e'}|\le|\Re Z_{e'}|+|\Im Z_{e'}|<2b\) on \(T^\sharp_{2b}\); similarly \(|m^{\mathsf T}Sm|\le Ns_1\mu_\sharp^2\). The bound on \(\mu_\sharp\) is FC7's proof (L1350–1370): on the chart \(\|\eta\|\le\sqrt{M_*C_F}e^{-aR_\sharp/2}\), and \(m=\eta/g\). The last assertion is FC7's final paragraph (L1373–1378): \(e^{-c\ell_t^r}/(A_1\theta_j^{-1/2}\ell_j^{p_1})\to0\) uniformly, with \(b=A_1\ell_j^{p_1}\) since \(\delta'_j=A_1g_j\ell_j^{p_1}\) (Tq0). ∎

So the local split has centre exactly \(0\) (real, so \(m_r=0\), no contour shift at all), at the price of the explicit additional term \(R_{\rm loc}\), whose size is \(Ns_1\) times a quantity that tends to zero faster than any power of \(\ell_j\) relative to \(b\). Both splits are exact; which one the consumer integrates is the consumer's choice. (FCr) is the one st1-r4 L1448 names. **Status: proved** (given \(s_1\), which is Theorem FC's own hypothesis; it belongs to the NL1/LF1 "complex perturbation bound").

### 3.6 The other branch: an additional conditional force

L1449 says "otherwise its additional conditional force must be bounded". Under Theorem 3.4 this branch is not needed. For completeness, here is what bounds the force when the consumer wants the exact saddle of the full exponent instead of \(m\).

**Proposition 3.7 (force bound from a remainder majorant).** Fix \(\mathfrak a\) and the Borel parameters. Suppose \(\mathcal R(\mathfrak a,\cdot)\) is holomorphic on \(T^\sharp_{2b}\) with \(|\mathcal R|\le\mathcal M\) there, and \(\operatorname{Re}S\ge c_S>0\) as a form on \(\mathbb C^{3N}\) (both NL1/LF1 inputs, L1450). Let \(f=\nabla_Z\mathcal R(\mathfrak a,m)\) be the additional conditional force. Then every component satisfies \(|f_{e,a}|\le2\mathcal M/b\), and the quadratic model
\(-\tfrac12(Z-m)^{\mathsf T}S(Z-m)+\mathcal R(\mathfrak a,m)+f^{\mathsf T}(Z-m)\)
has its stationary point at \(m+S^{-1}f\), with
\[
 \|S^{-1}f\|_\infty\le\|S^{-1}f\|_2\le\frac{2\sqrt{3N}\,\mathcal M}{c_S\,b}.                    \tag{3.10}
\]

*Proof.* For one real colour component \(Z_{e,a}\), complexified, the disc \(\{Z_{e,a}=m_{e,a}+w:|w|\le b/2\}\) with the other coordinates at \(m\) lies in \(T^\sharp_{2b}\): \(|\Re Z_e|+|\Im Z_e|\le2|m_e|+2|w|\le b/8+b<2b\) (FC7 gives \(|m_e|\le b/16\)). Cauchy's estimate on this disc gives \(|f_{e,a}|\le\mathcal M/(b/2)\). The stationary point of the model solves \(S(Z-m)=f\). Since \(\operatorname{Re}\langle v,Sv\rangle\ge c_S\|v\|_2^2\) (Hermitian pairing), \(\|S v\|_2\ge c_S\|v\|_2\), so \(\|S^{-1}f\|_2\le\|f\|_2/c_S\le\sqrt{3N}\,(2\mathcal M/b)/c_S\). ∎

Thus if the consumer's remainder majorant satisfies \(\mathcal M\le c_Sb^2/(32\sqrt{3N})\), the model saddle lies within \(b/16\) of \(m\) and Corollary 3.6 holds with \(\epsilon_m=1/8\) for the saddle-centred contour. **Status: reduced** to the NL1/LF1 inputs \(c_S\) and \(\mathcal M\) (L1450). The bound (3.10) carries the factor \(\sqrt N\) because it uses only \(\ell^2\) coercivity; a sup-norm inverse bound for \(S\) would remove it. Neither bound is needed for FC-mean-match in the form (FCr).

**Remark 3.8 (size of the slot force; not used).** The slot term's force at \(Z=m\) is \(\partial_ZP_{\rm slot}(\mathfrak a,m)=-\tfrac12\langle\mathfrak a,\partial_Z\Delta^{\rm loc}(D(Z))|_{Z=m}\,\mathfrak a\rangle\). Since \(D(Z)\) depends on \(Z\) through \(e^{igZ}\) (identity (2.1)), each \(Z\)-derivative carries a factor \(g\). On the support of the kept rim tests SA 17558 gives \(|A'(b)|\le Cp_0(g_j)\), and SA 17560 says that a piece of a kept form has oscillation in the pair "bounded by \(Cp_0(g_j)^2e^{-\kappa d^\natural_{j+1}(R)}\)" and that its difference at the two backgrounds of a stage localizes into pieces of modulus "at most \(C(\log x_i)^{-(q-3\mathfrak p_0-Cr)}e^{-c\,d^\natural_k(Y)}\)". These are SA's sketched remainder estimates, i.e. part of the NL1/LF1 remainder bound. I record them only to say that the slot coupling is a small remainder in SA's own accounting, not a shift of order \(b\) of the centre; nothing in §3 depends on this remark.

## 4. FC-test

Throughout, "real data in use" is the open set of real stage data \(W\) on which every new-structure test holds strictly; FC2's formula is used there and continued (FC2, L1324: "It is the unique continuation on a connected chart containing an open real slice"). A moved factor is *redundant* if it equals \(1\) at every \((Z,W)\) with \(Z\in D_b\) and \(W\) real in use. If a factor is redundant, replacing it by \(1\) does not change the real integrand in FC2, so it does not change the real formula or its unique continuation. This is the meaning of "proved redundant there" in L1332.

### 4.1 The gauge exponent

**Lemma 4.1.** On real data the stored gauge exponent \(e^{-x_j(1-\frac12\operatorname{Re}\operatorname{tr}V(y,x))}\) of SA 7181 equals \(e^{-x_j(1-\frac12\operatorname{tr}V(y,x))}\), and the latter is holomorphic in \(Z\) and \(W\) on the tube where the contour mean is on AV's branch.

*Proof.* For \(V(y,x)\in SU(2)\), \(\operatorname{tr}V(y,x)\in\mathbb R\). The mean is holomorphic on its branch (Lemma 3.1's proof), and \(\operatorname{tr}\) is linear. The normalizer \(z_{\mathfrak G}^{-1}\) is a constant. ∎

FC5 (L1218) already writes \(\operatorname{tr}\); the continuation must use that form, not \(\operatorname{Re}\operatorname{tr}\), which is not holomorphic. **Status: proved.**

### 4.2 The gauge indicators

**Lemma 4.2 (gauge indicators are redundant under CV).** Let \(C^\natural_{\rm av}\) be a Lipschitz constant of the contour mean on AV's branch ball, in the sense that for two families \((P_i),(P'_i)\) of at most \(4!\) path products on that ball, \(d(\operatorname{av}(P),\operatorname{av}(P'))\le C^\natural_{\rm av}\max_id(P_i,P'_i)\), with \(d(g,g')=|\operatorname{Log}(gg'^{-1})|\). Put
\[
 C_{\rm gi}=\tfrac94(L-1)\,C^\natural_{\rm av}.                                                  \tag{4.1}
\]
Impose the \(\gamma\)-ceiling
\[
 2C_{\rm gi}\,\delta'_j<\varepsilon_j,\quad\text{equivalently}\quad 2C_{\rm gi}\frac{A_1}{A_0}\,\ell_j^{-(p_0-p_1)}<1,     \tag{4.2}
\]
uniformly on the stage window, together with the ceiling that keeps \(\tfrac94(L-1)\delta'_j\) inside AV's branch ball. Then for every real \(W\) in use, every \(Z\in D_b\) and every carried pair \((y,x)\) whose factor is moved, \(|D(Z)(y,x)-\mathbf 1|<\varepsilon_j/2\). Hence every moved gauge indicator \(\mathbf 1\{|D(y,x)-\mathbf 1|<\varepsilon_{j'}\}\) with \(\varepsilon_{j'}\ge\varepsilon_j/2\) (in particular \(j'\in\{j-1,j,j+1\}\), by (T2) for \(\varepsilon\), L673) is redundant.

*Proof.* By Lemma 2.2, a moved pair lies in a new-member block \(B(y)\) and its contour reads only free removed rows of \(B(y)\). By Lemma 3.1, \(V(y,x)=I\). Fix a path \(\pi\) of the contour family; it has at most \(2(L-1)\) bonds (L1169: "Each path has at most \(2(L-1)\) bonds"). On each of its bonds \(D_e=e^{iu_e}V_e\) with \(|u_e|<\tfrac98\delta'\) by (2.2). Write the path product as \(P_\pi(D)=\prod_k e^{iu_{e_k}}V_{e_k}\). Moving each factor \(e^{iu_{e_k}}\) to the left through the unitary partial product gives \(P_\pi(D)P_\pi(V)^{-1}=\prod_k\operatorname{Ad}(Q_k)e^{iu_{e_k}}\) with unitary \(Q_k\). The group angle is bi-invariant and satisfies the triangle inequality on \(SU(2)\), so
\[
 d(P_\pi(D),P_\pi(V))\le\sum_k|u_{e_k}|<2(L-1)\cdot\tfrac98\delta'=\tfrac94(L-1)\delta'.
\]
The ceiling keeps both families on AV's branch ball, and the Lipschitz bound gives \(d(D(y,x),V(y,x))\le C^\natural_{\rm av}\tfrac94(L-1)\delta'=C_{\rm gi}\delta'\). Since \(V(y,x)=I\) and \(|e^{iA}-I|\le|A|\) for Hermitian \(A\) in the operator norm, \(|D(y,x)-\mathbf 1|\le C_{\rm gi}\delta'_j<\varepsilon_j/2\) by (4.2). The second form of (4.2) is (Tq0): \(\delta'_j/\varepsilon_j=(A_1/A_0)\ell_j^{p_1-p_0}\), and \(p_0-p_1>r>1\) (L89) makes it tend to zero, so (4.2) is a ceiling on \(\gamma\). ∎

**Where the constant comes from.** ST1 row 2 lists "CV's fixed mean and conjugator constants" (L163); Lemma CV item 4 (L1169–1170) uses "a fixed Lipschitz constant \(C_{\rm av}(L)\)" for the same mean on "a smaller common ball". I take \(C^\natural_{\rm av}\) to be that constant, or the larger of the two if the referee finds they differ; in either case it depends on \(L\) and AV only.

**Why CV matters here.** Under the comb representative of st1-r3, the reference's mean \(V(y,x)\) need not be \(I\): FC6 (L1237–1241) computes \(V_{\rm ax}(e)=e^{iF_p/2}\) against the comb value \(e^{iF_p}\) on a central plaquette. With a mean contour of size up to \(|F_p|/2\) at the reference, the indicator \(\mathbf 1\{|D(y,x)-\mathbf 1|<\varepsilon\}\) has no margin. Under CV the margin is the whole \(\varepsilon_j\). **Status of Lemma 4.2: proved.**

### 4.3 Factors that do not read moved rows

**Lemma 4.3.** The following factors are not moved (Definition 2.1): (T1) tests of rim fluctuation fields and of all coordinates other than level-\(j\) rows; (T2) tests of level-\((j+1)\) and coarser data; the gauge factors of pairs outside new-member blocks; (T5) the strip cutoffs \(\vartheta_{\rm co}\) and the strip variables; (Fl) the failure factors of stopped stages.

*Proof.* (T1): SA 17558: "in an integral operation that a term carries, the tests, the gauge factors and the delta functions depend on no background". A test of a rim coordinate is therefore a function of that coordinate alone, a Borel parameter of FC2 (FC2: "For fixed Borel parameters"). (T2): Lemma 2.3. Pairs outside new-member blocks: Lemma 2.2(ii).

(T5): SA 17526: the strip substitution is "made bond by bond, with new variable \(W'=e^{i\mathcal A'(b)}\)", and the cutoff \(\vartheta_{\rm co}\) "is a smooth cut-off in \(|\log W'|\)". The strip lies in \(S_{j+1}\subset\Omega_{j+1}\setminus\Lambda_{j+1}\) (SA 17518), where the stored field is \(A'=\mathcal A^{\rm s}_j|_{\Omega_{j+1}\setminus\Lambda_{j+1}}\) (SA 17528); these are the rim coordinates of the later stage (CA-I 74317–74320: the rim \(Z_{j+1}\cap\Omega_{j+1}\cap Z\) "carry the integration variables \(A_j\)"). So the cutoff depends only on a rim coordinate. st1-r4 L828: "Its real stored variable belongs to the near/Borel tier." The strip Jacobian and the reconstructed bond depend on the discrepancy \(H\), treated in Lemma 4.4.

(Fl): a stopped stage of operation level \(s\) keeps the failure factor \(1-\chi_\sharp\) of its own free rows, at its own stage level \(j_0\). Within operation \(s\), later stages are at higher levels (each stage enlarges the next member, SA 17612: "Put \(j=k_\flat+n\)"), so they do not move level-\(j_0\) rows. In a later operation \(t\) whose class component contains the stopped drop-out's mark, GEO-mark (st1-r4 L146) gives \(s<t-N_t\); the stages of operation \(t\) are at levels \(k_\flat+n\ge t-N_t\) (my reading of SA 17612 and RUN-low's \(k_\sharp=t-N^0_t\), L147, to be checked), so again above \(j_0<s\). If the later class component does not contain the mark, its stages do not touch the mark's rows. ∎

**Status: proved**, with one reading flagged for the referee: the range of stage levels of an operation used in (Fl).

### 4.4 Holomorphic factors

**Lemma 4.4.** Each factor of class (H) is holomorphic in \(Z\) on the tube \(\mathcal T_j\) and in \(W\) on the chart, at fixed Borel parameters, as follows.

1. *Haar and chart factors* \(\prod_es(g^2Q(Z_e))\), \(\Pi_V(u(Z))\): **proved** (FM5, L1029: "Continuation of its coefficient identity is holomorphic on a common complex chart"; \(s\) is entire, FM1).
2. *Strip Jacobians and the reconstructed strip bond*: for fixed strip variable \(W'\), F1's Jacobian \(1-\vartheta'(|A'|/\delta)\langle A',H\rangle/(\delta|A'|)\) is affine in \(H\), and \(f_H(A')=i^{-1}\operatorname{Log}(e^{iA'}e^{-i\theta(W')H})\) is holomorphic in \(H\) on the logarithm's branch (L819–820). The discrepancy \(H=H^{(j)}\) is the logarithm of a ratio of averaged backgrounds (SA 17518–17524), holomorphic on A1's continuation chart. **Proved**, given A1/F0/REG.
3. *Carried activities and regular-action terms.* At the stage, Theorem 14 (L1549–1556) rewrites each such term as \(\Phi_Y(s,z)=f(\rho^{\rm res}_X(P\dotplus(zh_Y(s;P,\xi))^\delta);\mathfrak q_X)\) and states that it "is defined and holomorphic in \(z\) …, in the switches …, and in all declared complex variables at fixed real factor"; at \(s=\mathbf1,z=1\) it "is exactly the old activity at the actual reconstructed background" (L1557). The moved coordinates enter through the completed source \(\xi=B'=b_V(a_V(u(Z)))\) (L793). The chain \(Z\mapsto u(Z)\) (a logarithm on its branch), \(u\mapsto a_V(u)\) (F2, jointly holomorphic, L850), \(a\mapsto b_V(a)\) (F4, holomorphic on the whole tube, L898), \(\xi\mapsto h_Y\) (DR, "jointly holomorphic" on the source ball \(\|S\|_{\rm src}<s_D\), dr Theorem 4, L180), \(h\mapsto P\dotplus zh\) (Lemma 4, L1577) and \(f\) (CI) is a composition of holomorphic maps. It is holomorphic in \(Z\) on \(\mathcal T_j\) provided the source stays in DR's ball, \(\|b_V(a_V(u))\|<C'_A\delta'_j\cdot\) (70) \(<s_D\), a \(\gamma\)-ceiling reading \(\bar\kappa\) through \(s_D=\epsilon_De^{-64\bar\kappa}\), and provided the substituted point is in the target domain (Theorem 14 hypotheses 2–3). **Reduced** to CI (item 8), DR (item 4) and complex input membership (item 5, through dom-draft Theorem 8), exactly as Theorem 14 already declares them.
4. *Kept rim forms \(\Delta^{\rm loc}_{\mathfrak k}\) and normalizers \(z^{(j)}\).* SA 17558: "These forms and factors are given as functions of a pair \((\mathbf U,\mathbf J)\) near \(\mathfrak k\), and they are constructed once and for all." Their holomorphy in the pair is part of the actual Gaussian family (HM, item 6) and of CI's analytic interface. **Reduced** to items 6 and 8.
5. *Outputs of earlier stages of the same operation.* An earlier stage's output is a function of its own datum, which contains the rows moved now. By induction on the stage index within the operation, FC2 at the earlier stage, with FCON there, makes that output holomorphic in its datum. Its own passing indicator is inside its own integral. **Proved by induction**, given FCON at earlier stages (the induction starts at the first stage, whose datum is main-step data).

∎

### 4.5 FC-test, reduced

**Theorem 4.6 (FC-test for the actual stage, reduced).** Assume the actual construction (A1)–(A4), Theorem 3.4's imports, the ceilings (4.2) and Lemma 4.4.3's source ceiling, the items reduced in Lemma 4.4 (CI, DR, complex input membership, HM's rim forms), and **Lemma OT** below. Then every moved factor of \(\Theta\) is holomorphic in \((Z,W)\) on a neighbourhood of the contours, or redundant. Hence FC2's analytic premise holds for the actual stage, and with FC2's majorant (Remark 4.7) the stage integral is holomorphic in \(W\) and Theorem FC's deformation (FC9) applies.

*Proof.* By §2.4 every factor is in one of the classes (H), (G), (T1)–(T5), (Fl). (G): exponent by Lemma 4.1, indicator by Lemma 4.2 for moved pairs and Lemma 2.2(ii) for the others. (T1), (T2), (T5), (Fl): Lemma 4.3. (T4), earlier stages' tests: inside their own integrals (Lemma 4.4.5). (H): Lemma 4.4. (T3): Lemma OT. Redundant factors are replaced by \(1\) on the real slice; the remaining integrand is holomorphic; FC2 applies. ∎

**Remark 4.7 (FC2's majorant; not part of FC-test).** L1545 and L1587 list "the uniform analytic majorants in FC2" separately. In (3.7) the rim integrand is bounded by \(e^{-\frac12\operatorname{Re}\langle\mathfrak a,S_a\mathfrak a\rangle+\operatorname{Re}\mathcal K^\circ(\mathfrak a)+\sup_Z\operatorname{Re}\mathcal R}\) times the moduli of the analytic factors. It is locally uniformly integrable if \(\operatorname{Re}S_a\ge c_a>0\) uniformly on the chart and \(\operatorname{Re}(\mathcal K^\circ+\sup_Z\mathcal R)\le\tfrac14c_a|\mathfrak a|^2+C\). These are the NL1/LF1 positivity and remainder inputs of L1450. **Reduced**, not proved.

### 4.6 The first remaining Outstanding statement: Lemma OT

Class (T3) consists of the older datum-loop tests (58) of the stored integrand on level-\(j\) loops whose stencil contains a moved row. They exist: SA 17396 lists, among the tests that must equal one on the support of a stage, "the plaquette tests of its two levels"; st1-r4 L152 retains them ("Older tests and stored densities are retained exactly"); (58) (L665–667) gives their form \(|\partial V(\tau)-I|\le C_{\rm te}L_\flat^{2\mathcal E(\tau)}\varepsilon_{m(\tau)}\). On \(D_b\) the moved field changes each bond of a level-\(j\) loop by a group angle at most \(\|a_V(u)\|<\tfrac98C_{\rm ch}L^4\delta'_j\) (identity (2.2)), so the loop holonomy by at most four times that. Therefore the following is exactly what redundancy needs.

**Lemma OT (Outstanding).** For every passing stage of level \(j\) in an admitted finite history, every real datum \(W\) in use, and every older test \(\mathbf 1\{|\partial D(\tau)-I|<t_\tau\}\) of the stored integrand on a level-\(j\) datum loop \(\tau\) whose stencil contains a moved row, the CV reference \(V=M_-(U_+)\) satisfies
\[
 |\partial V(\tau)-I|\le t_\tau-\tfrac92C_{\rm ch}L^4\,\delta'_j .                                \tag{OT}
\]
Here \(t_\tau=C_{\rm te}L_\flat^{2\mathcal E_{\rm old}(\tau)}\varepsilon_{m_{\rm old}(\tau)}\) is the old structure's threshold for \(\tau\), with its own exponent and layer.

For a loop with \(n_\tau\) moved bonds replace \(\tfrac92=4\cdot\tfrac98\) by \(\tfrac98n_\tau\); \(n_\tau\) is bounded by the fixed length of (58)'s test loops (four for a plaquette of rows of one level). Below I write the plaquette case.

*Proof that (OT) implies redundancy.* For \(Z\in D_b\) and real \(W\), each of the four bonds of \(\tau\) satisfies \(d(D_e,V_e)\le\|a_V(u)\|<\tfrac98C_{\rm ch}L^4\delta'_j\) (F2, (2.2)); retained bonds are unchanged. By bi-invariance and the triangle inequality, \(d(\partial D(\tau),\partial V(\tau))<\tfrac92C_{\rm ch}L^4\delta'_j\); with \(|e^{iA}-I|\le|A|\) and the triangle inequality in the operator norm, \(|\partial D(\tau)-I|<|\partial V(\tau)-I|+\tfrac92C_{\rm ch}L^4\delta'_j\le t_\tau\). ∎

The margin in (OT) is tiny relative to the threshold: \(\tfrac92C_{\rm ch}L^4\delta'_j/t_\tau\le\tfrac{3C_{\rm ch}}{4C_{\rm sm}}(A_1/A_0)\ell_j^{-(p_0-p_1)}\to0\), using \(C_{\rm te}=6C_{\rm sm}L^4\) and \(\mathcal E\ge0\). So (OT) asks only that the reference lie strictly inside each older test by a vanishing fraction. It does not follow from the old datum passing the old test: the old datum is within \(\tfrac92C_{\rm ch}L^4\delta'_j\) of \(V\) on \(\tau\), which gives only \(|\partial V(\tau)-I|<t_\tau+\tfrac92C_{\rm ch}L^4\delta'_j\), the wrong side.

#### Attack 1: fine-from-coarse regularity of the critical background

*Idea.* \(V\) is the level-\(j\) datum of the smooth critical background \(U_+\) of the new system, whose datum \(W\) obeys the formation input (58) at level \(j+1\). A level-\(j\) loop of a smooth field has about \(L^{-2}\) times the curvature of a level-\((j+1)\) loop, and the old threshold at level \(j\) is comparable to the new one at level \(j+1\). So \(V\) should be far inside the old test.

*The argument as far as it goes.* (i) PROF (L136): "A real critical background has normalized curvature and current bounded by \(C_P\max_\tau e^{-\delta_Pd(x,\tau)}|\partial V(\tau)-I|\)", the maximum over the datum loops of its own system. For \(U_+\) on \(Y\) (layer \(j+1\) of the new system) this is \(\xi_{j+1}^2\eta^{-2}|\partial U_+(p)-I|\le C_P\max_{\tau'}e^{-\delta_Pd(x,\tau')}|\partial W(\tau')-I|\) for bare plaquettes \(p\) at \(x\). (ii) AV/CURV's real recursion \(v_{n+1}\le L^2v_n+C(L^2v_n)^2\) (L127), iterated from the bare level to level \(j\) under the small-curvature ceiling, gives \(|\partial V(\tau)-I|\le(1+o(1))(\xi_j/\eta)^2\max_p|\partial U_+(p)-I|\) for a level-\(j\) loop \(\tau\) in \(Y\), the product \(\prod_n(1+CL^2v_n)\) being \(1+o(1)\) as \(\gamma\to0\). (iii) Combining, \(|\partial V(\tau)-I|\le(1+o(1))L^{-2}C_P\max_{\tau'}e^{-\delta_Pd}|\partial W(\tau')-I|\). (iv) By (58) for the new structure, \(|\partial W(\tau')-I|\le C_{\rm te}L_\flat^{2\mathcal E_{\rm new}(\tau')}\varepsilon_{m(\tau')}\). If the exponents satisfy \(\mathcal E_{\rm new}(\tau')\le\mathcal E_{\rm new}(x)+1+d(x,\tau')/\rho_0\), then, exactly as in Lemma 10's proof (L675–678, with \(\varepsilon_v/\varepsilon_m\le2e^{\delta D/4}\), \(\delta\le\delta_P\), \(\delta\rho_0\ge64\log L\)), the maximum is at most \(2L_\flat^2C_{\rm te}L_\flat^{2\mathcal E_{\rm new}(x)}\varepsilon_{j+1}\). (v) At a newly raised point \(\mathcal E_{\rm new}=e_j+1\) (L660), and \(\varepsilon_{j+1}\le2\varepsilon_j\). So
\[
 |\partial V(\tau)-I|\le(1+o(1))\,\frac{4C_PL_\flat^4}{L^2}\;t_\tau .
\]
(OT) then holds after a \(\gamma\)-ceiling if \(4C_PL_\flat^4/L^2\le1/2\), e.g. with \(L_\flat=2\) if \(L^2\ge128C_P\).

*Exact failure.* Two inputs are missing. (F1a) **\(L\)-uniformity of \(C_P\).** ST1 fixes \(C_P\) at row 2, after \(L\) (L163: "AV/CURV, PROF, RCG4, derivative, DR base constants/rates" follow \(L\) in row 1). No frozen text read here states how \(C_P\) depends on \(L\); if \(C_P\ge cL^2\), the inequality \(L^2\ge128C_P\) can fail for every \(L\). A floor \(L^2\ge128C_P(L)\) is a floor in IN1 row 2 only if \(C_P(L)=o(L^2)\). (F1b) **Exponent regularity.** Step (iv) needs the exponents to grow at most linearly in distance with slope \(1/\rho_0\). For the new exponents \(e_j\) of Lemma 10 this holds, since \(e_j\) depends on the layer index, which changes by at most \(1+D/\rho_0\) (Lemma 2, quoted at L675). For *inherited* exponents Lemma 10's proof says "the bound on inherited exponents is still an input" (L671), and (56) gives only the upper bound \(L_\flat^{2\mathcal E}\le C_R^2\ell^{2r_R}\). Using (56) instead loses the factor \(C_R^2\ell^{2r_R}\), which tends to infinity; then step (v) fails. (F1c) Step (v) also assumes \(\mathcal E_{\rm old}(\tau)\ge\mathcal E_{\rm new}(x)-1\), which is Lemma 10's raising rule (L660) read at the point; for loops whose old exponent was inherited this is again the missing input of (F1b). Step (ii) uses AV/CURV's recursion in its stated, upward direction (bare curvature bounds the curvature of each successive average); the referee should check that its \(v_n\) is the plaquette curvature of the \(n\)-th average on this regional geometry, including next to seams, where AV/CURV gives \(C_{\rm sm}L^2\varepsilon\) instead of \(2\varepsilon\) (L127).

#### Attack 2: SA's graded stage thresholds

*Idea.* SA proves the older-test implication with graded thresholds. SA 17612–17624: "As in Lemma 2.2, the tests made at a stage have to imply the earlier ones", with the comparison
"\(|\partial U^{(n)}_{k,X}-\mathbf{1}|\le|\partial U^{(n+1)}_{k,X}-\mathbf{1}|(1+c\beta_{\mathrm{s}}2^{-(j-i)})+c\beta_{\mathrm{s}}2^{-(j-i)}\varepsilon_i\eta_i^2\)" and a stage-\(n\) requirement \(|\partial U^{(n)}_{k,X}-\mathbf 1|<(1-\beta_{\rm s}(1-2^{-(j-i+1)}))\varepsilon_i\eta_i^2\). The error term is "\(C\delta'_je^{-\delta_0\operatorname{dist}}\eta_i^2\)": the difference of two backgrounds with the same constraints is a decaying response. In ST1's terms: the old and new backgrounds differ by DR's response to the stage source of size \(C'_A\delta'_j\) ((16), (70)), so their curvatures differ by \(CE_{\bar\kappa}C_A\delta'_je^{-\mu d}\). If the stage carried a test of the reference's own level-\(j\) loops at the graded threshold \((1-\tfrac12\beta_s)t_\tau\), (OT) would hold on its support (see (F2b) for the size of the margin).

*Exact failure.* (F2a) ST1's stage test does not contain such a test. ST-test (L152) "tests every free removed row against \(V^\sharp\) at \(\delta'_j\)", and nothing else; "The chosen test is a design input; its compatibility with the rest of the history construction is not inferred merely by reducing a threshold." Adding a test \(\chi_{\rm ref}(W)\) on \(V\) is a test in \(W\) alone, so it does not disturb Theorem FC; but it creates a new failing outcome, \((1-\chi_{\rm ref})\chi_{\rm free}\), at which the older test may vanish. The failing operation "keeps its original integrand with \(1-\chi_\sharp\)" (L1055), so this outcome needs its own small factor and its own place in the history rules (GEO-mark, the M1 ledger, LF1's rarity). No frozen text supplies the failure gain for such a test. (F2b) The size of the graded margin is not an obstruction for the loops that matter. For a (T3) loop the shell is the stage's own level, \(i=j\), so SA's margin is \(\beta_s(1-2^{-1})t_\tau=\tfrac12\beta_st_\tau\), and \(\tfrac12\beta_st_\tau>\tfrac92C_{\rm ch}L^4\delta'_j\) after a \(\gamma\)-ceiling, since \(\delta'_j/\varepsilon_j\to0\). So with the added test, (OT) holds on its support and FC-test follows. **Attack 2 therefore proves FC-test under a design change**, and the exact failure is (F2a): the new failing outcome needs a failure gain and history rules that no frozen text supplies. This is a reduction to LF1 and to a change of frozen ST1's ST-test, not a proof of Lemma OT as stated.

#### Attack 3: split the indicator and continue on an open set

*Idea.* Write \(\chi_{\rm old}(D(Z))=1-(1-\chi_{\rm old}(D(Z)))\). The first term gives a holomorphic integrand. The second is supported on the real set \(B=\{W\text{ real in use}:\exists Z\in D_b,\ \chi_{\rm old}(D(Z,W))=0\}\). On the open set \(O=(\text{real data in use})\setminus\overline B\) the formula equals the holomorphic one, so FC2 continues it to a complex neighbourhood of \(O\).

*Exact failure.* FC2 continues a formula from an open real set, and the continuation equals the actual stage integral only where the replaced integrand equals the actual one. The consumers need the actual stage value at **every** real datum in use: Theorem 14's second bullet identifies (75) at \(s=\mathbf1,z=1\) "exactly" with "the old activity at the actual reconstructed background" (L1557), and CI's real tie (L120) is a statement at every real splitting. At a point of \(B\) that is in use, the actual integrand contains a non-redundant indicator, so the actual stage value is not the value of the continued formula there; by FC-test's own example (L1337–1338) it need not be the restriction of any holomorphic function. Hence Attack 3 gives the needed conclusion exactly when \(B\) contains no real datum in use, which is Lemma OT. It reduces to Lemma OT and does not prove it.

**Neither proved nor refuted.** A counterexample to (OT) would be an admitted history with nonzero weight, a passing stage, and a level-\(j\) loop \(\tau\) containing a moved row with \(t_\tau-\tfrac92C_{\rm ch}L^4\delta'_j<|\partial V(\tau)-I|<t_\tau+\tfrac92C_{\rm ch}L^4\delta'_j\) (the upper bound is forced by the old datum passing its test). The same three checks as for FC6-history (L1278–1286) apply: an algebraic witness for a smooth background is not a history, and the history rules are supplied inputs that could exclude it. I did not construct one.

**Status: Outstanding.** Lemma OT is the first statement in FCON's proof order that is neither proved here nor reduced to another critical-path item. Owner: ST1 (stage test design), with LF1 if Attack 2's design change is adopted, or PROF's supplier (PR1/BG1) if Attack 1's \(L\)-uniform constant is supplied.

## 5. The contour for the actual stage

**Theorem 5.1 (FCON, conditional).** Assume:
1. the actual construction (A1)–(A4);
2. ST1's declared inputs used by FC0–FC9 (L924), with one LOC clause (owned by DOM, item 5; in this clone dom-draft's Lemma LOC♮) and ST-test\(^{\rm hol}\);
3. Theorem FC's ceilings, (4.2), the AV-branch ceiling of Lemma 4.2 and the DR source ceiling of Lemma 4.4.3, all in the final \(\gamma\)-ceiling;
4. the reduced items: CI (item 8), DR (item 4), complex input membership (item 5), HM's rim forms (item 6), FC2's majorant (Remark 4.7, NL1/LF1);
5. Lemma OT.

Then, at every passing stage of every admitted finite history: the stage integral at real data is (3.7) exactly; it continues holomorphically to the ST-test\(^{\rm hol}\) chart; its matched Gaussian is (3.4) with centre \(m\), \(|m_e|\le b/16\); and for every \(\nu\) with \(|\nu_e|\le b/16\), in particular \(\nu=\Im m\), FC9's deformation holds with the image in \(T^\sharp_b\subset\mathcal T_j\) (FC8, F5). In F5's notation \(m_r=0\), \(\vartheta_m=0\), \(\epsilon_m=1/16\). This supplies the clauses "FC-mean-match and FC-test" in Theorem 14 hypothesis 5, Corollary 14′ and geoh Lemma 10, for the actual construction.

*Proof.* FC-mean-match: Theorem 3.4 and Corollary 3.6. FC-test: Theorem 4.6, which uses Lemma OT and the reduced items. With FC-test, FC2's premise holds; with the majorant, FC2 gives holomorphy in \(W\) and uniqueness of the continuation. FC1 gives the domain, FC7 the centre bound, FC8 the tube containment, FC9 the deformation for the now holomorphic integrand. Corollary 3.6 gives F5's parameters. ∎

What Theorem 5.1 does not do: it proves no Gaussian bound, no remainder bound and no positivity of \(\operatorname{Re}S\) or \(\operatorname{Re}S_a\) (L1450–1451: "No Gaussian estimate is proved by this contour identity"). It does not identify a CA-I presentation (FM-match, SLOT-CA). It does not supply LOC.

## 6. Order of the constants

IN1's rule (in1 rows 1–10 with Amendment 1): structural constants are fixed before \(\kappa\) (row 4) and are independent of \(M\) (row 5) and \(\bar\kappa\) (row 5); amplitudes \(A_1,A_0,C_0,C_1\) follow \(M\) (row 6); every smallness requirement is a ceiling on \(\gamma\) through \(X_0\) (row 9). ST1's own table (L160–171) is compatible with it (its rows 1–6 precede \(\kappa\), row 7 is \(\kappa,\bar\kappa\), row 8 \(M\), row 9 amplitudes, row 10 the \(\gamma\)-ceiling). Every constant FCON introduces or reads:

| Constant | Definition | Fixed at (IN1 row / ST1 row) | Reads | Before \(\kappa\), free of \(M,\bar\kappa\)? |
|---|---|---|---|---|
| \(1/16,1/4,3/4,7/16,13/16,9/8,9/4,2\) | contour and test fractions (FC1, FC7–FC9, Lemma 4.2, Prop. 3.7) | absolute, before row 1 | nothing | yes |
| \(C_{\rm ch},r_u,r_{\rm sol}\) | F2 chart | IN1 row 2 ("flat and averaging constants") / ST1 row 2 (CH) | \(L\) | yes |
| \(C^\natural_{\rm av}\) | Lipschitz constant of the mean on AV's branch (Lemma 4.2) | IN1 row 2 / ST1 row 2 ("CV's fixed mean and conjugator constants", L163) | \(L\), AV | yes |
| \(C_{\rm gi}=\tfrac94(L-1)C^\natural_{\rm av}\) | (4.1) | same | \(L\), AV | yes |
| \(\tfrac92C_{\rm ch}L^4\) | OT margin coefficient | same | \(L\), CH | yes |
| \(r_{\rm hol},M_*\) | ST-test\(^{\rm hol}\) | IN1 row 3 / ST1 row 2 (L154: "precede \(\kappa\)") | \(L\), charts | yes |
| \(C_F,a\) | F6/LOC decay (Prop. 3.5) | IN1 row 3 / ST1 row 2 (LOC constants) | \(\theta_4\), \(L\), carriers | yes; \(M\) enters only through the lower bound \(R_\sharp\ge MR_t/4\) (f-meas L597) |
| \(s_1\) | row-sum bound of \(S\) (Theorem FC's hypothesis, Prop. 3.5) | required before \(\kappa\) with IN1's precision constants (st1-r4 L185: "The uniform IN1 precision constants \((a,H,\mu_0)\) still have to be supplied before \(\kappa\)") | NL1/LF1 | **required**, not supplied here |
| \(c_S,\mathcal M\) | Prop. 3.7 only | NL1/LF1 | — | not used by (FCr) |
| (4.2) | \(2C_{\rm gi}(A_1/A_0)\ell_j^{-(p_0-p_1)}<1\) | IN1 row 9 / ST1 row 10 | \(C_{\rm gi}\), \(A_1/A_0\) (row 6), \(p_0-p_1\) (row 1) | it is a \(\gamma\)-ceiling, chosen last |
| AV branch ceiling | \(\tfrac94(L-1)\delta'_j<\rho_{\rm AV}\) | IN1 row 9 / ST1 row 10 | \(A_1\), \(L\) | \(\gamma\)-ceiling |
| DR source ceiling | \(C'_A\delta'_j<s_D=\epsilon_De^{-64\bar\kappa}\) (dr (9)) | IN1 row 9 / ST1 row 10 | \(\bar\kappa\), \(A_1\) | \(\gamma\)-ceiling; reads \(\bar\kappa\), allowed for a ceiling |
| Prop. 3.5 smallness | \(\mu_\sharp/b\to0\) | IN1 row 9 / ST1 row 10 | \(M\) (only as \(R_\sharp\ge MR_t/4\)), \(A_1\) | \(\gamma\)-ceiling |
| OT margin ceiling | \(\tfrac92C_{\rm ch}L^4\delta'_j\le\) margin, once Lemma OT supplies a margin of size \(c\,t_\tau\) | IN1 row 9 / ST1 row 10 | \(A_1/A_0\) | \(\gamma\)-ceiling (conditional on Lemma OT) |
| Attack 1's floor (not adopted) | \(L^2\ge128C_P(L)\) with \(L_\flat=2\) | would be IN1 row 2 | \(C_P(L)\) | only if \(C_P(L)=o(L^2)\); otherwise a cycle |
| Attack 2's \(\beta_s\) (not adopted) | graded margin \(\tfrac12\beta_s\) | ST1 row 1 | — | yes |

No constant fixed before \(\kappa\) reads \(b_f,C_0,C_1,A_0,A_1,M\) or \(\bar\kappa\). Amendment 1's floors \(L>L_0^\natural\), \(\kappa\ge\kappa_0^\natural(L)\) are not read by FCON and only raise floors, so they change nothing here. **Status: proved** (as a check of the order; the required \(s_1\) is named, not supplied).

## 7. Statements used wrongly or imprecisely

1. **st1-r4 FC5's premise (L1221).** "If these varying pairs are in those blocks, \(d(\kappa_j\mathcal S+\Gamma)=0\) at \(V_{\rm ax}\)." The premise is a theorem (Lemma 2.2), and the conclusion holds at complex data and for any carried subset (Lemma 3.2). FC5's text is not wrong; its conditional form understates what is proved. L1227–1228's caution ("Gauge-factor coverage of a particular stored stage, and its resulting precision, must be checked") remains right for the *precision* (positivity needs coverage, FC4), not for the centre.
2. **SA 7181 versus FC5 (L1218).** SA writes \(\operatorname{Re}\operatorname{tr}\), FC5 writes \(\operatorname{tr}\). They agree on real data; only FC5's form is holomorphic (Lemma 4.1). A continuation that kept \(\operatorname{Re}\) would be wrong.
3. **Theorem FC, L1431–1432:** "the Hessian \(S\) of \(\kappa_j\mathcal S+\Gamma\) in the free coordinate \(\beta=u/g\) has zero linear term". A Hessian has no linear term; the intended statement is that \(\kappa_j\mathcal S+\Gamma\) has zero linear term at \(\beta=0\) (Lemma 3.2). Wording only.
4. **assembly-status L130 and L148, "FCON → CI (stage contours)".** No CI-owning text consumes a stage contour (grep count of "contour" is zero in `nl1-L.md`, `ci-form.md`, `td.md`, `drlocp.md`, `cls.md`, `in1.md`, `ag1.md`, `tp1.md`, `dr.md`, `cp12.md`, `pr-lay.md`). The consumers are ST1 Theorem 14 hypothesis 5, Corollary 14′ and Theorem FC (gate L40), and through them geoh Lemma 10 and dom-draft Theorem 8. The dependency is right; the named consumer should be ST1.
5. **The task brief's "Lemma LOC-flat", "class K-flat".** Not in this clone; dom-draft's first Outstanding is Lemma LOC♮ (L329), its class \(\mathcal K^\natural\). If the lead's copy is newer, the referee should check that FCON's uses of LOC (only through F6 and FC7, Proposition 3.5) are unchanged.
6. **Not wrong, checked:** L1449's "\(\varepsilon_m=1/16\) for the radius \(b_j\) of F5 (the value is valid for FC7's \(b\) as well)" is right (Corollary 3.6). Gate L65's reading that FC-test's general wording covers SA 7181's indicator is right, and Lemma 4.2 discharges that indicator. L1329's "F4 and CI give holomorphic coordinate maps and activities, not holomorphy of an older indicator depending on \(Z\)" is right; the holomorphy of carried activities in the moved coordinates comes from Theorem 14's (75) through the source (Lemma 4.4.3), as L1556 states.

## 8. Status of each step

| Step | Status | Rests on |
|---|---|---|
| §1 statements and consumer list | read; quoted with lines | the texts quoted |
| Lemma 2.2 (moved gauge reads) | proved | p82 L45, st1-r4 L9, L22, L26, L36, L1131–1137 |
| Lemma 2.3 (level \(\ge j+1\)) | proved | st1-r4 (67), L793; geoh Lemma 9 |
| Lemma 3.1 (CV axial, two readings agree) | proved | CV L1140; descent Lemma 2; A1/F0/REG continuation |
| Lemma 3.2 (zero linear term) | proved | FC3; descent Lemma 2's computation |
| Definition 3.3, Lemma 3.3′ (exact split) | proved | Theorem FM (L1072), FM5, (FCr) |
| Theorem 3.4 (FC-mean-match) | **proved** | the above |
| Corollary 3.6 (F5 parameters) | proved | FC7, F5 |
| Proposition 3.5 (local recentring) | proved | FC7's proof, F6; \(s_1\) as in Theorem FC |
| Proposition 3.7 (force bound) | reduced | NL1/LF1's \(c_S,\mathcal M\) |
| Lemma 4.1 (\(\operatorname{tr}\)) | proved | SU(2) |
| Lemma 4.2 (gauge indicators) | **proved** | Lemma 2.2, Lemma 3.1, F2, (Tq0), AV Lipschitz constant |
| Lemma 4.3 (independent factors) | proved (one reading flagged: stage-level range, (Fl)) | SA 17558, 17518–17528; CA-I 74317–74320; GEO-mark |
| Lemma 4.4 (holomorphic factors) | items 1, 2, 5 proved; items 3, 4 reduced | FM5; F1; Theorem 14; DR; CI; HM |
| Theorem 4.6 (FC-test) | reduced to Lemma OT and items 4, 5, 6, 8 | §4 |
| Remark 4.7 (FC2 majorant) | reduced | NL1/LF1 |
| **Lemma OT** | **Outstanding** (three attacks, §4.6) | — |
| Theorem 5.1 | conditional on Lemma OT and the reduced items | §§3–4 |
| §6 constants | proved (order check) | IN1 rows 1–10, ST1 L160–171 |

## Result

**Proved here**, for the actual construction (Y3 relative form, ST1's intrinsic (Tq0) domains with unit lifts, CV, SLOT-ST): **FC-mean-match** in the form st1-r4 L1448 names, "a matched Gaussian has exactly the split (FCr)" (Theorem 3.4): the stage Gaussian is the Hessian at the CV critical reference of \(\kappa_j\mathcal S+\Gamma\), the same for the absolute and relative gauge readings (Lemma 3.1); its linear term vanishes exactly, at real and complex data, with no gauge-coverage premise (Lemma 3.2); it has no slot coupling and its external-pair dependence is through \(V\) only, with an explicit local alternative (Proposition 3.5); F5 receives \(m_r=0\), \(\vartheta_m=0\), \(\varepsilon_m=1/16\) (Corollary 3.6). In **FC-test**: the gauge exponent (Lemma 4.1), the gauge indicators of SA 7181 (Lemma 4.2, redundant because CV makes the reference's contour mean exactly \(I\)), all factors that do not read moved rows (Lemma 4.3), and the Haar, chart, strip and earlier-stage factors (Lemma 4.4.1, 4.4.2, 4.4.5).

**Reduced to other items:** carried activities and kept rim forms (to CI, DR, complex input membership and HM, exactly as Theorem 14 already declares them); FC2's majorant and Proposition 3.7's force bound (to the NL1/LF1 inputs of L1450).

**First remaining Outstanding statement: Lemma OT** (§4.6): at every passing stage and every real datum in use, the CV reference lies strictly inside every older datum-loop test (58) on a level-\(j\) loop that reads a moved row, by the margin \(\tfrac92C_{\rm ch}L^4\delta'_j\). Attack 1 (fine-from-coarse regularity through PROF and AV/CURV) reduces it to an \(L\)-uniform PROF constant, \(C_P(L)\le L^2/(8L_\flat^4)\), and to linear growth of inherited exponents; neither is in a frozen text. Attack 2 (SA's graded thresholds) proves FC-test if the stage adds a reference-curvature test at \((1-\tfrac12\beta_s)t_\tau\), but that is a change of frozen ST-test whose new failing outcome needs an LF1 failure gain that no text supplies. Attack 3 (indicator splitting) reduces back to Lemma OT, because continuation from the set where the indicator is redundant reproduces the actual stage value only there, and the consumers need it at every real datum in use.

**Definitions supplied:** moved factor (Definition 2.1); the factor classes (§2.4); the declared stage split (Definition 3.3); redundancy on the real slice in use (§4, opening); the OT margin.

No frozen text, gate, ledger or status file was changed. This is pass 1, not distilled, not refereed, and grants no status.
