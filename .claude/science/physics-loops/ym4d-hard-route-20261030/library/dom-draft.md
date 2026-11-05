# DOM: complex-domain admission for the actual roster (critical path item 5, owner ST1 with NL1) — pass 1 draft

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), 2026-11-05, pass 1 (long draft) of the draft → distil → referee → freeze process. Research text, not an audit; it grants no status. Not checked by another model. All arguments are by hand; no step is discharged by a computation.

Credit: **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text**, for the outline (SA = `ym4.tex`, revision 31a47c543775), the complete account and Y3, including the running-radius table, the stage tests, the inner substitution and the regular-pair class. Tadeusz Bałaban supplies the background-field, averaging, gauge and stage methods that these texts and the library rebuild; Jonathan Dimock supplies the flat-propagator exposition used by P82. Library imports by Claude and Codex keep their own dependencies.

**Read for this draft** (bounded ranges; a line "L" is a line of the named file in this clone): `assembly-status.md` (whole); `cp12.md` L1–35, L463–686 (§§6–8, Result, change log); `cp12-draft.md` L586–645 (§11–12); `pr-lay.md` (whole, 395 lines); `st1-r4.md` L1–345, L345–369, L496–922, L1455–1698; `descent.md` L9–126, L196–318; `hm.md` L1–182, L262–327; `in1.md` L30–60, L184–200, L221–236, L666–676; `nl1-L.md` L565–636; `ci-form.md` L28–40; `geoh-draft.md` L9–23, L83–92, L289–322, L477–482; `dr-draft.md` L11–28, L534–552; `layered-a3.md` L1–50; `ym4-assembly.md` L187; `FINISH.md` row 272. SA (`scratchpad/sa/ym4.tex`): L6017–6040 (frame and running radii, (R19)) and L9763–9775 (inner substitution). The SA index README and `obligations.md` were not needed beyond the anchors already quoted by the frozen texts.

**Words.** *Proved* means proved here by a written argument from the named frozen imports (each frozen text is itself an implication from its own imports). *Reduced* means proved here to follow from a named statement owned by another critical-path item. *Outstanding* means not proved. *Roster* means the list of records (simple, tower, core, witness) that the actual construction forms at each structure of a history.

## 0. Results

| # | DOM clause (exact text in §1) | Result here | Status |
|---|---|---|---|
| D1 | PR-lay's D, (19), on every complex input pair where (7) is used | Theorem 3, for the roster R♮ of §2 (current-scale records at every structure; this is FINISH row 272's design clause (I-G) with unit lifts) | **proved** (from frozen ST1, pr-lay) |
| D2a | "every ST1 chain domain inside R4" (descent L285; assembly item 5) | Proposition 4: **false as literally stated** for supports that reach layers \(m\le k-n_0\) (explicit point) | **counterexample** to the literal clause |
| D2b | the corrected clause: every chain-domain point lies in the class on which hm Theorem 7 / descent Theorem 5 are actually proved | Theorem 5 (inclusion in \(\mathcal K^\natural\)) and Theorem 6 (those proofs read only \(\mathcal K^\natural\)) | **proved** (Theorem 6 is a line-by-line reading of hm's and descent's proofs; the referee must check it) |
| D3 | ST1 Theorem 14 hyp. 2, "complex input membership" | Theorem 8: every complex point at which a frozen consumer evaluates an activity lies in the stated chain domain, given the other items; Proposition 7 (polydisc room) | **reduced** to DR (item 4), the main-step source supply and FCON (item 7); the DOM part is proved |
| D4 | cp12 L626, the complex inner-substitution evaluations (DOM-in) | Corollary 9: on ST1's route the H-ct ball \(\mathfrak B_k(2r_k^{\rm ct})\) is admitted with half gap if \(c_{\rm ct}\le c_{\rm main}/E_{\bar\kappa}\); the tower clause is ST1 Lemma 8 | **reduced** to DR (item 4) and PR-H's C3 identification (item 2) |
| D5 | RUN-low | Theorem 1, from SA (R19) | **proved** |
| D6 | LOC | Three attacks, §7. Attack 1: LOC-form is impossible for every local rule (Proposition 10). Attack 3 proves LOC-decay from a path statement | **Outstanding: Lemma LOC♮** (first remaining statement in proof order) |
| D7 | ST-test | Theorem 11: the pivot clause follows from the free-row test, the retained curvature tests and LOC | **proved given LOC♮** |
| D8 | ST-test\(^{\rm hol}\) | Proposition 12: follows from a holomorphic rule | **proved given LOC♮** (the rule is LOC♮'s) |
| D9 | BOX (bg, id, resp) | Proposition 13: BOX-bg's straddling loops follow from BOX-id and BOX-resp; these are DR's output instance | **reduced** to DR (item 4) and the output test definition |
| D10 | IN1 "full admission" (L195) and H-E's "independent verification at every later read" | Proposition 14: the chain domain under R♮ is a valid specification of IN1's \(\mathcal D_j(X)\), hereditary, with retention at half radius | **proved** for the domain part; formation stays H-SF |
| — | PR1(5b) = layered-a3 (1) | §9: no frozen text on the path reads it; frozen ST1 Lemmas 5, 8, 11 and Theorem 14 replace each of its clauses | **does not belong to DOM**; leaves the critical path |

**First remaining Outstanding statement:** Lemma LOC♮ (§7.4). It is the only DOM clause not proved or reduced to another critical-path item. Its three attacks and their exact failure points are in §7.

**A statement used wrongly.** The obligation "every ST1 chain domain inside R4" (assembly-status L127, L186; descent L285 states it only as not done) is false for the unweighted R4 of hm L33 and descent (2) on supports that reach shallow layers (Proposition 4). Hm's and descent's theorems are not wrong: their proofs use less than R4 (Theorem 6). A consumer must cite them through \(\mathcal K^\natural\), not through R4.

## 1. The DOM clauses, exactly as the frozen consumers use them

Each entry gives the text, its line, and the consumer that reads it.

**D1 = PR-lay's D** (`pr-lay.md` L242–252, frozen). "Every complex input pair on which the consumer uses (7), with its fixed real \(U\), satisfies on **every required bond and derivative stencil of \(\Omega_0\)**
\(l|A'|,\ l^2|\nabla^UA'|\le(1+\beta_s)\lambda_\sigma C_1\theta_\nu^{-1/2}(\log\theta_\nu)^q\), \(l^3|\mathbf J|\le(1+\beta_s)\lambda_\sigma C_0\theta_\nu^{-1/2}(\log\theta_\nu)^q\), \(\lambda_\sigma\le C_\lambda'(\log\theta_\nu)^{2r_R}\). (19) Here \(l\) is the **current** longer-sequence scale, and \(\nu\) is the radius index actually assigned to that read. … The initial structure must satisfy the same envelope, or a separately specified envelope tending to zero." The Outstanding mark (L254) adds: "One must show that the actual roster supplies a current-scale bound at every read, including boundaries, outputs, drop-outs and the next fibre's longer sequence. … Replacing the domain by its intersection with (19) changes the consumer hypothesis; it requires checking coverage of its actual substitutions and integrals."
*Consumers.* pr-lay Theorem 8 (L317) through Lemma 7 (L312: "Under D, \(r(P)\le D_cF_{q+2r_R}(\gamma)\)"); it supplies "the precision hypotheses of frozen IN1 Lemma 2" (L328), hence the precision part of nl1-L's CI-Gauss (nl1-L L578–581). ci-form's H-D (L36) assumes it: "For the precision, assume PR-lay's R, W, G, B, Q and D … D is its current-layer envelope (19), on every required bond and stencil, with the actual initial/boundary/top radius assignments."

**D2 = "every ST1 chain domain inside R4".** Descent L285 (frozen): "Nor does this note put every ST1 chain domain inside this R4 domain." Hm L37 (frozen): "R4, and the additional R5–R6 conditions defining SA's hereditary core, do not imply Rep." Hm L371: "its whole declared local domain must be admitted to the representative class or supplied with a compatible descent theorem." R4 is hm L33: "The class \(\mathcal K(Y;a_0,a_1,j_0)\) imposes SA R4 on \(Y\): both plaquette defects \(<a_0\epsilon_{\rm lat}^2\), \(|A'|,|\nabla^UA'|<a_1\), \(|\mathbf J|<j_0\), and on every contained box of side at most \(C_{\rm box}LM\) a real gauge with \(|A|,|\nabla A|<C_{\rm pot}Ma_0\)", and descent (2) (L22–28) without Rep. These are **unweighted** bounds in level-\(k\) units (bare mesh \(\epsilon_{\rm lat}=L^{-k}\), hm L11).
*Consumers.* Descent Theorem 5 (L196: "On every \(P\in\mathrm{R4}(Z;a_0,a_1,j_0)\), with no Rep condition") and hm Theorems 7–8 (L278, L327), hence IN1's H-M as nl1-L Theorem 7 item 3 (CI-Gauss) reads it, and Corollary 13.1's UM budget.

**D3 = ST1 Theorem 14, hypothesis 2** (`st1-r4.md` L1542, frozen). "The input point belongs to \(\mathcal D_{a|+}\) and all required R1 working cores. … B4 gives membership at actual real backgrounds; complex input membership remains this hypothesis." Lemma B4 (L1531): "Admission of real backgrounds also does not assert that an arbitrary complex point lies in the chain domain." Corollary 14′ (L1587) applies "for complex inputs assumed to lie in the admitted domain."
*Consumers.* ST1 Theorem 14 and Corollary 14′ themselves; nl1-L CI-maps (L573–577: "Theorem 4's hypotheses other than the old activity bounds hold uniformly on every fibre of the entire new chain domain. The substitution maps take values in earlier activities' domains."); ci-form H-D (L36: "hold on these entire fibres").

**D4 = the complex inner-substitution evaluations** (`cp12.md` L626, frozen). "One must still identify every actual complex step evaluation, including its independently supplied current, with the proposed inner Landau map on every old window and every decoupling; establish hereditary core and gauge membership with quantitative room; and supply the localized derivative bounds on that room. … SA 9767–9772's inner-substitution statement assumes the higher-level simple conditions **and** the tower clause on a larger region at larger radii; citing it does not prove these hypotheses for the actual maps." SA L9767 (read here): "Suppose that \((U,A')\) satisfies, on some region containing \(\square_0\) and at radii larger than \(\alpha_{i,k}\) by a fixed factor, both the simple conditions of level \(k+1\) and, at that same level, the tower clause of \(\square_0\). … Then, on the domains well inside \(\square_0\), the inner substitution in Landau form takes values in the cores of every level \(1\le j\le k\), with the running radii \(\alpha_{i,j}\)."
*Consumers.* cp12 Theorem 10 (H-ct, C1 on \(\mathfrak B_k(2r_k^{\rm ct})\), L476–479) and its radius remark (L565: "the application must place its evaluation centres and fluctuation shifts in this smaller domain"); a2-full Theorem V; the ordinary-window estimate (cp12 §5, D7).

**D5 = RUN-low** (`st1-r4.md` L147). "The cell factors satisfy \(R_i\ge c_N(\log\theta_i)^r\), with fixed \(c_N>0\), \(r>1\), and \(L^{N_t^0-1}=R_{k_\sharp+1}\), \(k_\sharp=t-N_t^0\), \(N_t^0\ge2\). This is a lower bound, additional to RUN's upper bound. It is consistent with the rounded logarithmic cell sizes of SA 6026–6035."
*Consumers.* Lemma B1 (L726: "The identity \(L^{N_t^0-1}=R_{k_\sharp+1}\) and RUN-low imply …"), Lemma F6 (L914: "\(R_\sharp\ge MR_t/4\ge c_N\ell_t^r/4\)"), FC7 (L1343). Geoh-draft Theorem B (v) also uses \(L^{N^0-1}=R_{k_0+1}\).

**D6 = LOC** (`st1-r4.md` L155). "Either (decay) the common-gauge raw discrepancy on removed rows is at most \(C_{\rm loc}e^{-c_{\rm loc}R_\sharp}\), where \(R_\sharp\ge MR_t/4\); or (form) the two references belong to one admitted raw-datum chart, and are connected there by \(D_s=e^{isB_\Delta}D_+\), \(\|B_\Delta\|\le r_B\), with \(B_\Delta\) supported outside distance \(R_\sharp\) of the full stage carriers. The derivative theorem must hold along this entire segment in consistent gauges. Equality of nearby data and real regularity alone do not supply this common chart."
*Consumers.* Lemma F6 (L905–916), hence F4's \(h_j\le\delta'_j/8\) and \(h_j<r_{\rm sol}/4\) (L885–886), hence Lemma 12's stage identification, (70), the stage budget (73), and Theorem 14 at every stage.

**D7 = ST-test** (`st1-r4.md` L152). "The stage's passing factor tests every free removed row against \(V^\sharp=M_-(U_+^\sharp)\) at \(\delta'_j\). Every removed row, pivots included, lies within \(r_{\rm sol}/4\) of that reference, where \(r_{\rm sol}\) is the converse neighborhood in Lemma F2. The reference is formed from data in \(X^\sharp\), the quarter-cell enlargement of the component, with a specified local boundary rule. Older tests and stored densities are retained exactly. The chosen test is a design input; its compatibility with the rest of the history construction is not inferred merely by reducing a threshold."
*Consumers.* F4's proof (L896: "full logarithms below \(r_{\rm sol}/4+h_j<r_{\rm sol}/2\). F2's converse applies"), F7 (L918), FC1 (L1308–1312, L1426).

**D8 = ST-test\(^{\rm hol}\)** (`st1-r4.md` L154). "The localized-datum rule is holomorphic, real on real data, and uses CV for both references. There is a fixed raw-datum ball of radius \(r_{\rm hol}>0\), inside both admitted continuation charts, on which the relative row logarithm is holomorphic and bounded by \(M_*\). Real LOC holds on its real slice, in the same gauge. Data in use have coordinates \(X+iY\), \(\|X\|<r_{\rm hol}/4\), \(\|Y\|\le C_Qr_1(i)\). The fixed ball and bound precede \(\kappa\)."
*Consumers.* FC7 (L1343–1353) and Theorem FC (L1426), used only where a stage contour is consumed (FCON, item 7).

**D9 = BOX** (`st1-r4.md` L149–151): (bg) "The output background is the canonical real regular critical background of \(D_{\rm out}\). Loops in \(\mathcal B_t\) have curvature at most \(C_{\rm bx}C(M)\varepsilon_t\); all other loops satisfy the inherited (58), converted to their output levels." (id) "At real parameters the preceding background is \((e^{i\eta H}U_{\rm out})^g\), with \(g\) real, the correct independent/plain-current identity, and surviving stored transports as in Lemma 12." (resp) "On the full switch polydisc the box response has the DR properties and \(n_b(H,K)\le C(M)E_{\bar\kappa}\delta'_te^{-\mu d_+(b,S_{\rm bx})}\)."
*Consumers.* Lemmas B1–B3 (L722–728, L1505–1525), Theorem 14 hyp. 1 and 3 at outputs.

**D10 = IN1's domain and "full admission"** (`in1.md` L44, frozen): "Each connected union \(X\) of level-\(j\) \(M\)-cubes has a specified hereditary complex core \(\mathcal D_j(X)\), as in SA 5663–5755 (R4–R6). Its data include local gauges and potential/current bounds on every required subdomain, existence of the required averaging towers, and their uniform bounds." L195: "It does not construct the gauges, potential bounds or towers in R4–R6. Even at a real pair with zero fluctuation these other domain conditions remain. H-E requires their independent verification at every later read."
*Consumers.* IN1's norm (4) (L44–48) and every IN1 theorem that bounds \(\|E\|_{j,\kappa}\).

**PR1(5b)** = `layered-a3.md` (1) (L39–45): on the full earlier-parameter and switch domains, along the stage path, "\(\operatorname{dist}_\infty(D_e(t),\mathcal T_e^c)\ge\eta_*>0\), \(\|\partial_tF_a\|\le Cr_a^{\rm lift}\sum_{l\in E_n}u_l\sqrt{1+|m-l|}\,e^{-D|m-l|}\)". Its stated consumer is `stage-resp.md` (layered-a3 L9: "This is input (B) of `stage-resp.md`"). §9 settles it.

**One name, several statements.** "R4" means three different things in the library: SA's single-level simple conditions (SA 5665–5694); the unweighted level-\(k\) class of hm L33 and descent (2) on a multi-layer support; and ST1's scalar comparison core (11), which is imposed only at a core address \(X\subset\Omega_i\) in level-\(i\) units. Only the third is part of the ST1 chain domain. D2's failure (Proposition 4) is the gap between the second and the third.

## 2. The actual history and the roster R♮

### 2.1 The actual step

The actual step is SA's step with the four analytic changes fixed by the frozen texts and repeated in geoh-draft §2.1: the Y3 relative soft-gauge form of frozen `descent.md` (Theorem 5); ST1's chart-free intrinsic domains with the radius table (Tq0) and unit record lifts \(\lambda_\tau\equiv1\), \(\Lambda_Q=1\) (`st1-r4.md` L82–89); Amendment CV's averaged-contour representative (`st1-r4.md` L41). By geoh-draft Lemma 2.0 (unrefereed; its proof only notes that none of the four changes enters the region rules), the geometric record of a history is a function of its test outcomes; I use that lemma only to say that the regions, cells, layers and fates below are those of SA's rules.

A **history** is a finite ordered list of structures \(\sigma_0<\sigma_1<\cdots\): the initial structure, main-step inputs, stage structures, outputs and drop-out stops. A structure \(\sigma\) has a depth \(k(\sigma)\), a determining sequence \(\Omega_0^\sigma\supset\cdots\supset\Omega^\sigma_{k(\sigma)}\) as in `st1-r4.md` (3), with layer index \(m_\sigma(x)=\max\{q:x\in\Omega_q^\sigma\}\) and scale \(\xi_{m_\sigma(x)}\), and, where a fibre integral is taken, the longer sequence \(\mathbf S_\sigma=(\Omega_0^\sigma,\ldots,\Omega^\sigma_{k+1})\) of `pr-lay.md` §1 with its next region \(\Omega_{k+1}^\sigma\). Write \(-\to+\) for consecutive structures, as in ST1 (13): "+" is the later structure (the input of the next substitution), "−" the earlier (its target).

**Geometry used.** GEO of ST1 (L126), including memberwise monotonicity \(m_-(x)\le m_+(x)\) along compared transitions, and pr-lay's G (L217): stage, prepared and retained drop-out sequences have gaps at least \(LM\xi_j\), label gaps at least \(cM\xi_j\), and torus room. In particular, at a fibre with next region \(\Omega_{k+1}\),
\[
 \operatorname{dist}_\infty(\Omega_{k+1},\Omega_k^c)\ge LM\quad\text{(level-\(k\) units)}. \tag{G\(_k\)}
\]
G is SA Proposition 2.3 (SA 17398–17407 as checked in pr-lay L343: "Confirms the stated one-later-\(M\)-cube gaps") and is the subject of item 3 (GEOH); it is an import here.

### 2.2 The roster

ST1 fixes the *form* of each record (`st1-r4.md` L80, L104, L112–118, R1) but not *which* records are born at each structure. PR-lay L254 asks for exactly this: "One must show that the actual roster supplies a current-scale bound at every read". FINISH row 272 records that the pr-lay draft proposed it as a design clause (I-G): "SA (R4) on every bond of Omega_0 at its current layer with lifted radii (SA L6141-6152), shown formed, met at the real reference and kept with half room; to be adopted by NL1 and ST1", and pr-lay L354 refused to adopt it without "an explicit consumer change with its consequences checked". I adopt it here, with ST1's unit lifts, and check the consequences in Lemma 2.

**Definition R♮ (the actual roster).** At every structure \(\sigma\) of a history the construction forms, in addition to ST1's tower and stored-slot records:

* **(R♮-s) current-scale simple records.** For every bare bond \(b\) of \(\Omega_0^\sigma\) whose stencil is contained, read at its base site \(x\) with index \(m=m_\sigma(x)\) and base radii \(r_\iota(m)L^{-am}\) (level-0 units, `st1-r4.md` L112), the records
 \[
 \xi_m^2\eta^{-2}|\partial U(p)-I|,\ \xi_m^2\eta^{-2}|\partial\mathbf U(p)-I|<c^*_\sigma(x|m)\,r_0(m),\quad
 \xi_m|A'(b)|,\ \xi_m^2|\nabla^U_\nu A'(b)|<c^*_\sigma(x|m)\,r_1(m),\quad
 \xi_m^3|\mathbf J(b)|<c^*_\sigma(x|m)\,r_0(m),
 \]
 for every plaquette \(p\) based at \(x\) and every direction \(\nu\). (In level-0 units \(\xi_m=L^m\), \(\eta=1\); the display is the same inequality written unit-free.) At the initial structure the index is the initial convention's index \(\nu_0(x)\) with \(\theta_{\nu_0}\ge\gamma^{-2}\); at an unfinished top it is SA's index \(t-1\) (SA 6145–6148 as quoted at pr-lay L256). In all cases the assigned index \(\nu\) is recorded.
* **(R♮-c) level-\(k\) core records.** At a structure of depth \(k\), the R1 core (Definition R1, L91–102) at every core address \(X\subset\Omega_k^\sigma\) that is a connected union of level-\(k\) \(M\)-cubes, with its prescribed core cubes taken to be **every** cube of side at most \(C_{\rm box}LM\) contained in \(\Omega_k^\sigma\), each with its supplied enlarged carrier in layers at least \(k-1\) (L118).
* **(R♮-w) natural witnesses.** For every \(j\) and every cube of side at most \(c_gM_1\xi_j\) in \(\Omega_0^\sigma\cap(\mathcal L_j\cup\mathcal L_{j+1})\) (pr-lay L42), a real gauge witness record with bound \(\xi_j|A|,\xi_j^2|\nabla A|<a_\flat\), where the absolute ceiling satisfies \(a_\flat\le h/4\), \(h=\min(a_R,a_W,1/2)\) of pr-lay (11).

Records are never deleted (ST1 L104, L1673: "Made the ledger a permanent union"). The chain domain \(\mathcal D_{a|\sigma}\) is ST1's: it imposes every record born between \(a\) and \(\sigma\), each at its current radius \(c_\sigma(r)R_r\).

**Lemma 2 (R♮ is admissible for frozen ST1).** Under ST1's declared inputs (Theorem 14 hyp. 1) the following hold for the roster R♮.
1. *Formation.* Every R♮ record forms at the plain real triple of its birth structure with base multiplier \(c_{\min}/4\).
2. *Compatibility.* For every transition \(-\to+\), every target record occurs in the input with the room (13).
3. *Substitution and drift.* Lemma 11 (65) and its drift clause, Lemma 9′, Lemma B4 and Theorem 14 hold verbatim for the enlarged record list.
4. *Consumers.* CI (L1533) for R♮ is implied by CI for any sub-roster on the same structures: a smaller domain weakens every "on the whole chain domain" clause.

*Proof.* 1. The R♮-s records are simple records in the sense of L112, at the birth index. Lemma 10 (L669) states that "all simple, tower, R1-core and witness records form at the plain real triple with base multiplier \(c_{\min}/4\)" under GEO, AV/CURV, PROF/RCG4 and (T1)–(T3); its proof (L689–693) bounds simple curvature and current at a core address by \(\epsilon_{\rm f}r_0(i)\) and notes "the potential is zero", and (59) with (T1) gives the same bound \(\epsilon_{\rm f}r_0(m)\) at every bond of layer \(m\), since (59) holds pointwise at every complete element and incomplete-star plain currents are zero (L693). The plain triple has \(A'=0\), so the potential and derivative records hold with value zero. The R♮-c records are R1 cores, covered by the same lemma; the witness bound for core cubes is (60) with \(s\le C_{\rm box}LM\), and L704 says these quotients "are bounded independently of \(M\), since \(s\le CLM\) and every \(g_Q\) contains \(M\)". The R♮-w records are natural witnesses; L704: "For natural cubes \(s\le12M_1\), use the cube itself as its containing cube and a separate absolute ceiling"; (60) gives \(|A|,|\nabla A|<8L^3B_*(s+2)\epsilon_{\rm f}r_0(i)\), which is below any fixed \(a_\flat\) after a ceiling on \(\gamma\), because \(r_0(i)\le C_0F_q(\gamma)\) by `pr-lay.md` Lemma 7 (22). (If the pr-lay cube constant \(c_g\) exceeds 12, apply (60) with \(s\le c_gM_1\); the bound is still a fixed multiple of \(\epsilon_{\rm f}r_0(i)\).)

2. A target record of \(-\to+\) is born at some structure \(\le-\); it is also born before \(+\), so it is imposed by \(\mathcal D_{a|+}\) (records are never deleted). Its coefficient drops by at least \(d_*(m_r)\) by Lemma 1′/M2 (L213), which is stated for every \(x\) and every \(0\le m\le t\), hence for every R♮ record's \((x,m)\). Records born at \(+\) are not targets of \(-\to+\).

3. Lemma 11's proof treats records one at a time: "Freezing records makes the target functions, units, lifts and base radii identical to functions already imposed at the input. By GEO-monotonicity, a frozen index \(m^\circ\) is at most \(m_+\)" (L749), then (66) and (45) bound "every simple-read increment" (L753); towers and R1 elements are treated likewise (L755–769); witnesses are unchanged by substitution and transported under drift (L774). None of these steps uses the number of records or which structure formed them. Lemma 9′ is per element. Theorem 14's proof (L1577) cites "Lemma 11 puts it inside the target domain with room; Lemmas 5 and 8 supply the continuation domain". B4 (L1529) is "Lemma 11 now telescopes each frozen read". So all four statements hold for R♮.

4. Immediate. ∎

The roster changes no constant of ST1's table (L160–171): the R♮ records use ST1's own radii and coefficients. The only new constant is \(a_\flat\le h/4\), an absolute ceiling of ST1 row 4, after \(h\) (pr-lay §2 step 2, IN1 row 3) and before \(\kappa\).

## 3. RUN-low (D5)

**Theorem 1 (RUN-low for the actual frame).** Let the frame be SA's (R19) (SA L6017–6026): \(\theta_0,\ldots,\theta_k\ge\gamma^{-2}\), \(0<\gamma<e^{-1/2}\); for \(i\le j\), \(\underline\lambda(j-i)-c_5\le\theta_i-\theta_j\le\bar B(j-i)\); \(\check R_j=R(\min_{i\le j}\theta_i)\), where "\(R(y)\) is the smallest power of \(L\) not below \((\log y)^r\)"; and \(\check R_j\le L\check R_{j+1}\). Let the actual cell factors be \(R_i=\check R_i\) (SA 6026–6035; ST1 L147). Then:
1. If \(\gamma^{-2}\ge\max(4,2c_5)\), then \(R_i\ge2^{-r}(\log\theta_i)^r\) for every \(i\). So RUN-low's first clause holds with \(c_N=2^{-r}\).
2. Put \(\rho_j=\log_LR_j\in\mathbb Z\). At every operation level \(t\ge1+\rho_1\) there is a least integer \(N=N_t^0\) with \(L^{N-1}=R_{t-N+1}\); it satisfies \(2\le N_t^0\le t\), so \(k_\sharp=t-N_t^0\ge0\).

*Proof.* 1. Take \(u\le i\). The left inequality of (R19) with \((u,i)\) gives \(\theta_u-\theta_i\ge\underline\lambda(i-u)-c_5\ge-c_5\) (SA's \(\underline\lambda\) is a positive rate). Hence \(\min_{u\le i}\theta_u\ge\theta_i-c_5\ge\theta_i/2\) when \(\theta_i\ge2c_5\). For \(\theta_i\ge4\), \(\log(\theta_i/2)\ge\frac12\log\theta_i\). Since \(R\) is nondecreasing and \(R(y)\ge(\log y)^r\),
\(R_i\ge(\log\min_{u\le i}\theta_u)^r\ge(\tfrac12\log\theta_i)^r\).

2. Because \(\gamma<e^{-1/2}\), every \(\theta\ge\gamma^{-2}>e\), so \((\log\min_{u\le j}\theta_u)^r>1\) and \(R_j\ge L\), that is \(\rho_j\ge1\). The map \(j\mapsto\min_{i\le j}\theta_i\) is nonincreasing and \(R\) is nondecreasing, so \(\rho_j\) is nonincreasing in \(j\). The last clause of (R19) gives \(\rho_j-\rho_{j+1}\le1\). For \(1\le N\le t\) put \(g(N)=N-1-\rho_{t-N+1}\). Then \(g(1)=-\rho_t\le-1\), and
\[
 g(N+1)-g(N)=1-(\rho_{t-N}-\rho_{t-N+1})\in\{0,1\}.
\]
At \(N=t\), \(g(t)=t-1-\rho_1\ge0\) by hypothesis. A function on integers that starts below zero, ends at or above zero and increases by steps 0 or 1 takes the value 0; let \(N_t^0\) be the least zero. Then \(N_t^0\ge2\) since \(g(1)<0\), \(N_t^0\le t\), and \(g(N_t^0)=0\) is \(L^{N_t^0-1}=L^{\rho_{t-N_t^0+1}}=R_{k_\sharp+1}\). ∎

This is the definition used by CA-I 53765–53769 as geoh-draft §7.1 quotes it ("the least such positive integer"); Theorem 1 shows it is well defined and has the two properties ST1 reads.

**Remark (early levels).** For \(t\le\rho_1\) the identity has no solution with \(k_\sharp\ge0\). Such an operation, if it occurs, belongs to ST1's initial/unfinished convention ("Initial/unfinished entries have their separately supplied comparisons", L1542). A stage window \(j_{t,n}=t-N_t+n\ge0\) needs \(t\ge N_t=R_t\ge L^{\rho_t}\). Under (R19), \(\log\theta_1\le\log\theta_t+\log(1+\bar Bt)\) and \(\log\theta_t\le2R_t^{1/r}\le2t^{1/r}\) (part 1), so \(\rho_1<1+r\log_L(K_1t^{1/r})\) with \(K_1=2+r+\log(1+\bar B)\). Then \(t\ge1+\rho_1\) holds for every \(t\ge L\) once \(L\ge2(2+r\log_LK_1)\). If \(\bar B\le C_*\log L\) with \(C_*\) absolute (the one-loop form of the frame increments), this is a floor on \(L\) depending on \(r,C_*\) only, at IN1 row 2. ST1 L170 lets "any numerical RUN frame-increment bound" be chosen at row 9; that is compatible with this floor only if the increment bound has the stated \(C_*\log L\) form. I do not prove that form here; it is SA's frame hypothesis. **Status of the remark: conditional on \(\bar B\le C_*\log L\).** Theorem 1 itself needs no such bound.

## 4. PR-lay's D (D1)

**Which sequence is "current".** PR-lay §4 opens (L215): "The following inputs concern the **same current longer sequence and real representative** used in (7)." Its B (L219) says: "At every such structure \(U\) is the supplied regular critical background, in the step's real axial representative." At a fibre \(-\to+\) the real factor of the input triple is the new background \(U_+\) (ST1 Lemma 12, L786; F4, L879), so the current longer sequence is the input structure's sequence \(\mathbf S_+\), with its next region; a stage is "cut at its own depth" (pr-lay L326). I use this identification below; it is a reading of pr-lay L215–219 and L326, and the referee should check it.

**Theorem 3 (D for the actual roster).** Assume R♮ and ST1's declared inputs. Let \(\sigma\) be any structure (initial, main-step input, stage, output or drop-out stop) and \(P=(U,A',\mathbf J)\in\mathcal D_{a|\sigma}\). Let \(b\) be any bare bond of \(\Omega^\sigma_0\) whose stencil is contained, with base site \(x\), \(m=m_\sigma(x)\), and let \(l\) be any reading scale at \(b\) or at a derivative stencil based at \(b\) that does not exceed \(L\xi_m\). Then, with \(\nu\) the index recorded by R♮-s,
\[
 l|A'(b)|<L(1+\beta_s)r_1(\nu),\quad
 l^2|\nabla^U_\nu A'(b)|<L^2(1+\beta_s)r_1(\nu),\quad
 l^3|\mathbf J(b)|<L^3(1+\beta_s)r_0(\nu).                              \tag{3.1}
\]
In particular PR-lay's largest-incident-scale readings on \(\mathbf S_\sigma\) and on each of its depth cuts satisfy (19) with \(\lambda_\sigma=L^3\), and (19)'s last clause holds with
\[
 C'_\lambda:=\max\{2^{2r_R}C_\lambda,\,L^3\}.                         \tag{3.2}
\]
Consequently, under pr-lay's R, W, G, B and Q, Theorem 8 of `pr-lay.md` applies at every complex input pair in \(\mathcal D_{a|\sigma}\), at every point \(P\dotplus(zh_Y)^\delta\) produced by ST1 Theorem 14, and at every line point \(P_z=(U,zA',z\mathbf J)\) with \(|z|\le R_{\rm line}\), for any fixed \(R_{\rm line}\ge1\) chosen before \(\gamma\). Its complex-size bound improves to
\[
 r(P_z)\le R_{\rm line}L^3(1+\beta_s)C_1F_q(\gamma).                  \tag{3.3}
\]

*Proof.* \(P\in\mathcal D_{a|\sigma}\) imposes the R♮-s records born at \(\sigma\), at current radius \(c_\sigma(r)R_r\). At its own birth structure the coefficient is \(c^*_\sigma(x|\nu)\), and Lemma 1′/M2 gives \(c^*_\sigma\le1+\beta_s\) (L213). So \(\xi_\nu|A'(b)|<(1+\beta_s)r_1(\nu)\), and likewise for the derivative and the current; for ordinary reads \(\nu=m\).

Scale comparison. A bond and each derivative stencil based at \(b\) have diameter at most \(2\eta\). Two points in one stencil cannot lie in layers differing by two, since that would cross a complete layer of width greater than \(\rho_0\xi\ge4L^2\eta\) (ST1 (3) and row 3). So every corner scale of the stencil is at most \(L\xi_m\); this is the argument of pr-lay (5) (L56). Multiplying the record bounds by \(l/\xi_m\le L\), \((l/\xi_m)^2\le L^2\), \((l/\xi_m)^3\le L^3\) gives (3.1).

Matching (19). Put \(\lambda_\sigma=L^3\). Since \(\theta_\nu\ge\gamma^{-2}>e\), \((\log\theta_\nu)^{2r_R}\ge1\), so \(\lambda_\sigma\le C'_\lambda(\log\theta_\nu)^{2r_R}\) with (3.2). With \(r_\iota(\nu)=C_\iota\theta_\nu^{-1/2}(\log\theta_\nu)^q\), (3.1) is (19) at index \(\nu\). The "required bonds and derivative stencils of \(\Omega_0\)" are all bonds with contained stencils, which R♮-s covers, including boundary bonds; "boundaries, outputs, drop-outs" are structures \(\sigma\) of the list; "the next fibre's longer sequence" is \(\mathbf S_+\) by the identification above; a depth cut only lowers the reading scale. The initial structure satisfies the same envelope with its recorded index \(\nu_0\), and unfinished tops with SA's index; pr-lay requires only that the index be "the radius index actually assigned to that read" (L252).

Points produced by Theorem 14 lie in \(\mathcal D_{a|-}\) by (65) (L742–745), so the first part applies at \(\sigma=-\). Line points need not lie in any chain domain: Theorem 3 of `pr-lay.md` needs only \(r(P_z)<r_*\) and the real bound of \(U\); \(r(P_z)=|z|r(P)\), and (3.1) with `pr-lay.md` Lemma 7 (22) gives (3.3), since \(\sup_{\theta\ge\gamma^{-2}}\theta^{-1/2}(\log\theta)^q\le F_q(\gamma)\). Then (23) of pr-lay holds after a ceiling on \(\gamma\) that reads \(R_{\rm line},L,\beta_s,C_1\): \(R_{\rm line}L^3(1+\beta_s)C_1F_q(\gamma)<r_*\). ∎

**What Theorem 3 does not do.** It does not prove pr-lay's G (item 3), B (ST1 Lemma 10 and B4, under their inputs), R and W (operator imports) or IN1's H-M (item 6). It does not replace a domain by its intersection with (19): (19) is a *consequence* of membership in the unchanged ST1 chain domain with the roster R♮, so pr-lay L254's warning ("Replacing the domain by its intersection with (19) changes the consumer hypothesis") does not apply. The coverage of "actual substitutions and integrals" that L254 also asks for is Theorem 8 below.

## 5. "Every ST1 chain domain inside R4" (D2)

### 5.1 The literal clause is false

**Proposition 4 (a chain-domain point outside R4).** Fix radii \((a_0,a_1,j_0)\) satisfying hm (24) (so \(a_1<r_{\rm loc}/(2L^3)\)). Put
\[
 s_0:=\frac{c_{\min}\min_{\ell\le k}r_0(\ell)}{16K_aK^\sharp},\qquad
 n_0:=\Big\lceil\log_L\frac{2a_1}{s_0}\Big\rceil+1,                         \tag{5.1}
\]
with \(K_a\ge1\) of ST1 Lemma 8 and \(K^\sharp=\max(1,e^{4\delta_T}K_T)\) of ST1 row 4. Let a structure \(+\) of depth \(k\) have a layer \(m\le k-n_0\) containing a bare bond \(b\) (direction \(e_1\)) whose \(\ell^\infty\) distance from every other layer exceeds \(3\xi_m\), and let the region \(Z\) of hm Theorem 7 (or descent Theorem 5) contain the \(2\xi_m\)-neighbourhood of \(b\). Let \(\varphi\) be the lattice function \(\varphi(y)=(1-\operatorname{dist}_\infty(y,b_-)/\xi_m)_+\). Then for \(s_0/2<s<s_0\) the triple
\[
 P_s=(I,\ A'_s,\ 0),\qquad (A'_s)_\mu(y)=\delta_{\mu1}\,s\,\xi_m^{-1}\varphi(y)\,\sigma_3,
\]
lies in \(\mathcal D_{a|+}\) but not in \(\mathrm{R4}(Z;a_0,a_1,j_0)\).

*Proof.* *Not in R4.* In level-\(k\) units \(\xi_m=L^{m-k}\), so \(|A'_s(b)|=sL^{k-m}\ge(s_0/2)L^{n_0}>a_1\).

*In \(\mathcal D_{a|+}\).* The chain domain is defined by its records (L104). At \(P_0=(I,0,0)\) every record function vanishes: the flat field has zero curvature and current, its towers are flat (Lemma 8: at real \(w\) the towers "equal the canonical real backgrounds of their actual averaged data", here \(I\)), and every witness is the trivial gauge. Every current radius is at least \(c_{\min}\) times its base radius (L213), and every base radius in normalized form is at least \(r_0(\ell)\) for some \(\ell\le k\) (simple and core potential records use \(r_1\ge r_0\), since \(C_1\ge C_0\)). It suffices that each record function stays below \(c_{\min}\min_\ell r_0(\ell)/2\) at \(P_s\).

The field is abelian and \(U=I\), so \(\nabla^U=\nabla\) and every plaquette holonomy is exactly \(\exp(i\eta^2\operatorname{curl}A'_s)\). The support of \(\varphi\) lies in layer \(m\), where the scale is \(\xi_m\). With \(|\varphi(y+\eta e)-\varphi(y)|\le\eta/\xi_m\):
\[
 \xi_m|A'_s|\le s,\qquad
 \xi_m^2|\nabla A'_s|\le\xi_m^2\cdot\eta^{-1}\cdot s\xi_m^{-1}\cdot\eta/\xi_m=s,\qquad
 \xi_m^2\eta^{-2}|\partial\mathbf U-I|\le\xi_m^2\cdot2\sup|\nabla A'_s|\le2s .
\]
*Simple records* (R♮-s and older ones at the same bonds) therefore read at most \(2s\); older records have index \(m^\circ\le m\) and radii no smaller (ST1 (66)). *Core records* at an address \(X\subset\Omega_i\) read in level-\(i\) units with \(i\le m\) (the support meets \(\Omega_i\) only if \(i\le m\)); there \(\xi_m=L^{m-i}\ge1\), so \(|A'_s|\le s\), \(|\nabla A'_s|\le s\), and \(|\partial\mathbf U-I|\le2s\eta_i^2\), each at most \(2s\) times the core's normalization in (11). *Tower records* (ordinary and in R1 cores): Lemma 8 (49) with \(E_U^{\delta_T}=0\) and \(E_w^{\delta_T}\le\sup_bn(w;b)\le s\) gives \(|G|\le K_as\), and moving sites to tops costs \(e^{4\delta_T}\le K^\sharp\) (L560); Lemma 8 applies because \(\sup n(w)\le s<a_T\). Lemma 8 also supplies the open continuation domains. *Witness records* involve only \(U\). Every record function is therefore at most \(2K_aK^\sharp s<c_{\min}\min_\ell r_0(\ell)/8\). ∎

**Reading.** hm L33 and descent (2) impose SA's single-level R4 inequalities, in level-\(k\) units, on a multi-layer support. ST1 imposes level-\(i\) R4 only at core addresses inside \(\Omega_i\), and own-scale bounds elsewhere (L112). On layers \(m\ge k-1\) the two agree up to fixed powers of \(L\); on layers \(m\le k-n_0\) the R4 bound is stronger by \(L^{k-m}\). The hypothesis of Proposition 4 holds in any history in which a shallow layer survives inside the support of a long walk label (hm L59: hulls lie near trees of length \(t_\omega\), which are unrestricted). So the obligation "every ST1 chain domain inside R4" cannot be met; what can be met, and what hm's proofs use, is §5.2.

### 5.2 The class the proofs use

Fix a structure \(+\) of depth \(k\) with longer sequence \(\mathbf S\), a region \(Z\) (union of coarse cubes of side \(LM\)) and the integrand's fine support \(Z_0\) with collar \(H=Z_0^\sharp\subset Z\) (hm L17, L325). Let \(h=\min(a_R,a_W,a_h,1/2)\) (pr-lay (11) and hm (7)), and let \(b_{\rm gap}\) be hm Lemma 4's buffer (L131).

**Definition (\(\mathcal K^\natural\)).** \(\mathcal K^\natural(Z;Z_0;\varrho,a_0)\) is the set of triples \(P=(U,A',\mathbf J)\) such that
* **(K1)** \(r_Z(P)<\varrho\), with hm (3)'s largest-incident-scale convention;
* **(K2)** \(P\in\mathcal R_{\rm loc}(Z;\alpha_0,\alpha_1,\alpha_J)\) with \(\alpha_0=\alpha_1=\alpha_J=h/4\) (hm L27);
* **(K3)** \(U\) has local real bound \(<h/2\) on \(Z\) (pr-lay L38–44, read on \(Z\));
* **(K4)** every box \(B\) of side at most \(C_{\rm box}LM\) with \(B\subset N_{b_{\rm gap}+2L}(Z_0)\) admits a real gauge \(U^g=e^{i\epsilon_{\rm lat}A}\) with \(|A|,|\nabla A|<C_{\rm pot}Ma_0\), unweighted, in level-\(k\) units.

By hm Lemma 2's first part (L97: "Since \(l\le L\), scaling R4's inequalities and gauge bounds proves (6)"), \(\mathcal K(Z;a_0,a_1,j_0)\subset\mathcal K^\natural(Z;Z_0;L^3(a_1+j_0),a_0)\) whenever (24) holds. The converse fails by Proposition 4.

**Theorem 5 (the chain domain lies in \(\mathcal K^\natural\)).** Assume R♮, ST1's declared inputs, (G\(_k\)), and \(M\ge M_{\rm dom}:=3+e_c\), where \(e_c\) is the fixed carrier enlargement of L118 (implied by ST1 row 8, \(M\ge L^4M'_1\), whenever \(e_c\le L^4M'_1-3\)). Put
\[
 \varrho_\gamma:=L^3(1+\beta_s)C_1F_q(\gamma),\qquad a_0^\gamma:=C_0F_q(\gamma).          \tag{5.2}
\]
Then for every \(Z\supset H\) and every \(P\in\mathcal D_{a|+}\), both \(P\) and \(P^{u_Z(U)}\) (descent Lemma 1's canonical gauge) lie in \(\mathcal K^\natural(Z;Z_0;\varrho_\gamma,a_0^\gamma)\), once \(\gamma\) is below a ceiling \(\gamma_{\rm dom}\) fixed by
\[
 \varrho_\gamma<\min\{h/4,\ r_{\rm loc}/2,\ 1/(2H_0)\},\quad
 L^2(1+\beta_s)C_0F_q(\gamma)<h/4,\quad
 L^2(1+C_{\rm pot}M)a_0^\gamma<h/16.                               \tag{5.3}
\]

*Proof.* (K1) is Theorem 3, (3.1), at \(\sigma=+\): every read in \(Z\) has \(l\le L\xi_m\) and \(r_\iota(\nu)\le C_\iota F_q(\gamma)\le C_1F_q(\gamma)\).
(K2) Curvature: the R♮-s curvature records give \(\xi_m^2\eta^{-2}|\partial U(p)-I|,\ \xi_m^2\eta^{-2}|\partial\mathbf U(p)-I|<(1+\beta_s)r_0(m)\) for \(p\) based at \(x\); hm's normalization uses the largest corner scale \(l_p\le L\xi_m\), so the normalized curvature is \(<L^2(1+\beta_s)C_0F_q(\gamma)<h/4\) by (5.3). Natural gauge cubes: the R♮-w records give \(\xi_j|A|,\xi_j^2|\nabla A|<a_\flat\le h/4\) on exactly hm's family ("every contained natural gauge cube of side at most \(c_gM_1\xi_j\) in the two-layer zone", L27). The \(\alpha_1,\alpha_J\) parts follow from (K1) since \(\varrho_\gamma<h/4\).
(K3) is (K2)'s real part: pr-lay's real bound is the curvature bound and the same cube family, both \(<h/2\).
(K4) Let \(B\subset N_{b_{\rm gap}+2L}(Z_0)\). Since the free coordinates touch \(\Omega_{k+1}\) and \(Z_0\) is a union of fine \(M\)-cubes containing their bases and the bases of every coordinate read by the integrand (hm L17, L325), \(Z_0\subset N_{M+1}(\Omega_{k+1})\). Hence \(B\) and its enlarged carrier lie in \(N_{M+1+b_{\rm gap}+2L+e_c}(\Omega_{k+1})\). By hm (23), \(b_{\rm gap}\le M\). The level-\(k\) \(M\)-cubes meeting \(B\) or its carrier reach at most \(M\) further, so everything lies in \(N_{3M+2L+1+e_c}(\Omega_{k+1})\). With \(L\ge27\) and \(M\ge3+e_c\), \((L-3)M\ge(L-3)(3+e_c)\ge3L-9+e_c>2L+1+e_c\), so \(3M+2L+1+e_c<LM\).
By (G\(_k\)), \(B\), its carrier and every level-\(k\) \(M\)-cube meeting them lie in \(\Omega_k\), in layers \(k\) and \(k+1\). So \(B\) is a prescribed core cube of R♮-c at a core address \(X\subset\Omega_k\) (the connected union of the level-\(k\) \(M\)-cubes meeting \(B\) and its carrier), and the core witness (L101: "For every prescribed core cube \(Q\), require a real gauge with \(|A|,|\nabla A|<C_{\rm pot}Mr_0(i)\) on the supplied enlarged carrier") gives (K4) with \(a_0=r_0(k)\le a_0^\gamma\). These witness bounds have no coefficient (L102) and are retained unchanged (L104).
Gauge. Every condition (K1)–(K4) is invariant under real site gauges: the norms by conjugation, the witnesses by \(h\mapsto hg^{-1}\). This is the argument of descent Lemma 1 (L109–114: "every bounded quantity in (2), the local regular class and \(r_Y\) is preserved"), which applies word for word to (K1)–(K4). So \(P^{u_Z(U)}\) lies in the same class. ∎

**Theorem 6 (hm and descent on \(\mathcal K^\natural\)).** In hm Theorems 7–8 and Corollary 13.1, replace "\(P\in\mathcal K(Z;a_0,a_1,j_0)\)" by "\(P\in\mathcal K^\natural(Z;Z_0;\varrho,a_0)\cap\mathrm{Rep}(Z)\)", replace \(L^3(a_1+j_0)\) in (24) by \(\varrho\), and replace \(L^3(a_0+a_1+j_0)\) in (26) and (33) by \(\varrho\). In descent Theorem 5 make the same replacement, without Rep, and in (7)–(8) and (15). Then all conclusions of those theorems hold with the same early constants.

*Proof.* This is a reading of the proofs; each use of the class is listed with its line.
1. Hm Lemma 1 (L53): the labels are "defined directly at \(P\in\mathcal R_{\rm loc}(Y;\alpha)\), \(\alpha<a_h\)" on hulls in \(Y=Z\). (K2) with \(h/4<a_h\).
2. Hm Lemma 2 (L85–102). Its first sentence, (6), converts \(\mathcal K\) into \(\mathcal R_{\rm loc}\) and bounds \(r_Y\); it is replaced by (K1)–(K2). Its second part assumes "\(U\) has local real bound \(<h/2\)" and \(r=r_Y(P)<r_{\rm loc}\) (L95): (K3) and (K1) with \(\varrho\le r_{\rm loc}/2\). Its proof (L97–102) uses only these.
3. Hm Lemma 3 (L106) needs a real gauge \(|A|,|\nabla A|\le\alpha\le1/16\) on a box \(B^+\) and Rep on its blocks. Lemma 4 applies it to boxes obtained from cubes \(Q_c\) meeting \(S\), "round its \(b_{\rm tail}+r_{\rm av}+2L\) neighbourhood outward to next-level blocks" (L150); these lie in \(N_{b_{\rm gap}+2L}(S)\) by the definition of \(b_{\rm gap}\) (L131). Theorem 7 applies Lemma 4 "on the collar" (L291) with \(S=Z_0\) (the compression \(\chi\) is onto coordinates based in \(Z_0\), L17). So (K4) and Rep suffice, with \(\alpha<C_{\rm pot}Ma_0<h/(16L^2)\) by the last condition of (5.3).
4. Hm Lemma 4 (L125–152) otherwise uses (4), R on the extension, and "Lemma 2 loses at most \(H_1r\le c_L/8\)" (L152): items 1–3. "For a whole-torus support use R directly" (L152): (K3) globally.
5. Hm Theorem 5 is stated on \(\mathcal W(Y)\), "real \(U\) obeying Rep and the local gauge/curvature bounds used in Lemma 4, and complex data with \(r_Y(P)<r_{\rm loc}\)" (L156): (K1), (K3), (K4), Rep.
6. Hm Lemma 6 (L249) is tag counting; it reads no field.
7. Hm Theorem 7's proof (L291–314) uses Lemma 4 on the collar, (4), Theorem 5, Lemma 6, and "Put \(r=r_Z(P)\). Lemma 2 and (27) give …"; the last line, "Use (6); adding the harmless \(a_0\) term yields (26)", is the only place where R4's radii enter, and it only bounds \(r\) by \(L^3(a_1+j_0)\). With (K1) one has \(r<\varrho\) directly.
8. Hm Theorem 8 (L327) assumes Theorem 7 and FG/UM; Corollary 13.1's (33) is "a later radius/tube ceiling compatible with (24)" (L449), so its replacement is \(H_0\varrho+C_\tau|\tau-1|\le\varepsilon_*/2\).
9. Descent Theorem 5's proof (L228–249) uses descent Lemma 1 (gauge to the representative, which preserves (K1)–(K4) by the last paragraph of the proof of Theorem 5 above), descent Lemma 4 (L184–194: "hm's representative-domain construction and estimates hold under R, W and AV"; its proof says "Its Lemma 2 uses only R4 and Cauchy bounds", which by item 2 means (K1)–(K3)), and hm's FG. The bound (15) is hm (26) for the replacement family.
Nothing else in these proofs reads the field. ∎

**Status.** Theorem 5 is proved from frozen ST1 and R♮. Theorem 6 is a proof by reading of frozen proofs; the readings are quoted, and **a referee must check items 1–9 against hm L53–327 and descent L184–249**. Together they give the corrected D2: at every chain-domain point of every structure where a Gaussian is formed, and for every support \(Z\), hm Theorems 7–8 and descent Theorem 5 apply, with
\[
 \varepsilon^\natural=H_0\{e^{32\bar\kappa-dM}+\varrho_\gamma\}+C_\tau|\tau-1|.            \tag{5.4}
\]
G-ID, F, FG/UM and the identification of the actual Gaussian (item 6, HM) are not touched.

## 6. Complex input membership (D3) and the inner-substitution evaluations (D4)

### 6.1 Polydisc room at admitted real points

**Proposition 7 (polydisc room).** Assume R♮ and ST1's declared inputs. Let \(P_0=(U,0,J_+(U))\) be the plain real triple of a real background admitted at structure \(\sigma\), in the sense of Lemma B4 (every record of \(\mathcal D_{a|\sigma}\) holds at \(P_0\) with at least half its declared radius). Put \(w^\natural(m)=c_{\min}r_0(m)/4\) and define \(\|h\|_{w^\natural}\) by (63) with \(w^\natural\) in place of \(w\). Then
\[
 \{P_0\dotplus h:\ \|h\|_{w^\natural}<r_*\}\subset\mathcal D_{a|\sigma},             \tag{6.1}
\]
and the map \(h\mapsto P_0\dotplus h\) is holomorphic there. In particular \(\mathcal D_{a|\sigma}\) contains the product polydisc of complex \((A',\mathbf J-J_+)\) with \(\xi_m|A'|,\xi_m^2|\nabla^UA'|,\xi_m^3|\mathbf J-J_+|<r_*c_{\min}r_0(m)/4\) at every bond of layer \(m\).

*Proof.* Lemma 11's proof (L749–769) bounds the increment of each record function under a shift \(h\) by a fixed multiple of \(\|h\|_ww(m^\circ)\), using only two properties of \(w\): \(L^{-a(m_+-m^\circ)}w(m_+)\le w(m^\circ)\) (66), and \(w(m')\le4^{|m'-m|}w(m)\) (used at L758). Both hold for \(w^\natural\): by (T2), \(r_0(m+1)\le2r_0(m)\), so \(L^{-a\nu}r_0(m+\nu)\le(2/L)^\nu r_0(m)\le r_0(m)\) and \(r_0(m')\le2^{|m'-m|}r_0(m)\). With \(\|h\|_{w^\natural}<r_*\), Lemma 11's choice of \(r_*\) makes each simple and tower increment at most \(\tfrac1{16}\cdot2w^\natural(m^\circ)=c_{\min}r_0(m^\circ)/32\). The room at \(P_0\) is at least half the current radius, hence at least \(c_{\min}r_0(m^\circ)/2\) in the same normalization (current coefficients are \(\ge c_{\min}\), L213; base radii are \(\ge r_0\)). For R1 elements apply Lemma 9′ with \(\tau_0=1/2\): the input radii at \(P_0\) are at most half the current radii. As in L769, each shift quantity on an incident bond is at most \(4L^3\|h\|_{w^\natural}w^\natural(i)\le L^3r_*c_{\min}r_0(i)\). By row 6 and (64), \(r_*\le[8K_{\rm core}]^{-1}=c_{\min}/(64L^3C_{\rm os}K^\flat(1+c_\natural))\) with \(C_{\rm os}=18\), so this is at most \(c_{\min}^2r_0(i)/(1152K^\flat(1+c_\natural))\), below (55)'s \(s(b)=b_0(b)/(36K^\flat(1+c_\natural))\) because \(b_0(b)\ge c_{\min}r_0(i)\). The current condition of (55) holds at the midpoint radius as in L769. Witnesses are unchanged by substitution (L745). Holomorphy is Lemma 9′'s last sentence and (10). (The room at \(P_0\) here replaces the gap (13) of a transition; the increment estimates are the same.) ∎

### 6.2 Every frozen consumer's evaluation point

**Theorem 8 (complex input membership, reduced).** Assume R♮, ST1's declared inputs, and the following items owned elsewhere: DR with (16) on the full switch polydisc (item 4); the main-step source supply (ST1 Corollary 14′'s "main-step coordinate/source supply"); Lemma LOC♮ (§7) at stages; DR's output instance at outputs (Proposition 13); and, where a contour is asserted, FC-mean-match and FC-test (item 7). Then every complex point at which a frozen consumer evaluates an activity or a precision lies in the domain on which that consumer requires it:
1. *Activities on the new domain* (CI, L1533; nl1-L CI-maps): the points are those of \(\mathcal D_{a|+}\), by the statement of CI. Under R♮-c every R1 working core born up to \(+\) is a record of \(\mathcal D_{a|+}\), so membership in \(\mathcal D_{a|+}\) includes Theorem 14's "all required R1 working cores".
2. *Substituted points* \(P\dotplus(zh_Y(s;P,\xi))^\delta\), \(|z|<\rho_X\), \(|s_\Delta|<e^{\bar\kappa}\): they lie in \(\mathcal D_{a|-}\) with half of every gap, by Theorem 14's first bullet (L1556), whose hypothesis 3 is supplied by the listed items: (70) at stages (F4, which needs LOC through F6 and ST-test, §7–8), the main-step bound, or BOX-resp at outputs.
3. *Cauchy polydiscs at admitted real points* (IN1's readout \(b[\widehat E]\), L49–60; cp12 (26)): Proposition 7.
4. *Precision evaluations* (pr-lay Theorem 8; hm Theorems 7–8; descent Theorem 5): Theorem 3 and Theorems 5–6, at the points of items 1–2 and on their line discs.
5. *Stage fluctuation tubes* \(\mathcal T_j\) (F4): F4 itself, given \(h_j\le\delta'_j/8\), \(h_j<r_{\rm sol}/4\) (LOC) and ST-test; contours (F5, FC): item 7.
6. *Initial points*: CI-base (nl1-L Theorem 7 item 1).

*Proof.* Items 1, 3, 4 are Lemma 2, Proposition 7, Theorems 3, 5, 6. Item 2 is Theorem 14 (L1556: "Every target read retains half its gap and every datum remains in its open continuation tube"), with Lemma 2 for the roster. Item 5 is F4 (L879–898). ∎

So the DOM content of D3 is proved, and what remains of ST1's "complex input membership" is exactly DR (item 4), the main-step source supply, LOC♮ (this item) and FCON (item 7).

### 6.3 The inner substitution on ST1's route (D4)

On ST1's route the old terms are not evaluated through SA 9767's inner substitution. They are evaluated at the pinned substituted input (75), and their domains are the frozen records of ST1. The tower clause of SA 9767 is ST1 Lemma 8 (cp12 Lemma 11 already reads the enlarged potential ball from Lemma 8's (51)–(52)); "hereditary core and gauge membership with quantitative room" is Lemma 11 (65) with half gaps and Lemma 9′; "the localized derivative bounds on that room" are (15) on the fixed raw-datum ball (P82M, cp12 Theorem 3, conditional) and DR (16). What D4 adds is the size of the fluctuation ball.

**Corollary 9 (the H-ct ball is admitted).** At a main step of level \(k\), let the fluctuation \(B\) range over cp12's doubled ball \(\mathfrak B_k(2r_k^{\rm ct})=\{\sup|g_kB|<2c_{\rm ct}\alpha_{0,k}\}\) (cp12 D8, L465–470), feeding DR as a main-step source of size \(\delta_{\rm src}=2c_{\rm ct}\alpha_{0,k}=2c_{\rm ct}r_0(k)\). There is a structural constant \(K_{\rm main}\), fixed before \(\kappa\) and independent of \(M,\bar\kappa,C_0,A_1\), such that if
\[
 c_{\rm ct}\le\frac1{4E_{\bar\kappa}K_{\rm main}}                            \tag{6.2}
\]
and \(\gamma\) is below a ceiling, then for every \(P\in\mathcal D_{a|+}\), every such \(B\), every \(|s_\Delta|<e^{\bar\kappa}\) and \(|z|<\rho_X\) with \(\rho_X>1\), the substituted point lies in \(\mathcal D_{a|-}\) with half of every gap.

*Proof.* Repeat Lemma 13's main-step computation (L1488–1503) with \(\delta_{\rm src}=2c_{\rm ct}r_0(k)\) in place of \(\delta_{t-1}\). By (71), \(a_X=D_{\rm src}\max\{C_{\rm lev}Q_X/r_*,\ K_{\rm pin}E_X/\epsilon_{\rm lev}\}\) with \(D_{\rm src}=C_DE_{\bar\kappa}C_A\delta_{\rm src}\). The main-step bound on \(Q_X\) is \(Q_X\le C/(a\,r_0(k))\) with \(a\) "a fixed multiple of \((1-\theta_s)\beta_s\)" (L1503). Hence
\[
 a_X\le c_{\rm ct}E_{\bar\kappa}K_{\rm main}+2c_{\rm ct}r_0(k)C_DE_{\bar\kappa}C_AK_{\rm pin}/\epsilon_{\rm lev},
 \qquad K_{\rm main}:=\frac{2C_DC_AC_{\rm lev}C}{a\,r_*}.
\]
\(K_{\rm main}\) reads only structural constants (rows ≤ 6 of ST1's table). Under (6.2) the first term is at most \(1/4\); the second tends to zero with \(\gamma\) since \(r_0(k)\le C_0F_q(\gamma)\). So \(a_X<1/2\) and \(\rho_X>1\). DR's source-domain threshold \(\epsilon_De^{-c_D\bar\kappa}\) (L143) is met after the same ceiling. Theorem 14's first bullet gives the conclusion. ∎

**Consequences for cp12.** (i) Corollary 9 is the "typical datum inclusion" of cp12 (27) on ST1's route: (71)–(73) replace (27), and the real background needs no budget because it is admitted by B4. (ii) (6.2) is a new upper bound on \(c_{\rm ct}\) that reads \(\bar\kappa\) through \(E_{\bar\kappa}\). It is compatible with cp12's order ("window constants, core ratios and \(c_{\rm ct}\) at row 6", L544), which comes after \(\bar\kappa\) (row 5). cp12 (26) then has \((g_k/r_k^{\rm ct})^2=(c_{\rm ct}C_0)^{-2}(\log\theta_k)^{-2q}\), whose larger constant is absorbed by \(q>r\) as cp12 L545–550 already states. (iii) What Corollary 9 does not do: it does not identify cp12's pointed functions \(\Psi_z(B;s)\) with the old activities evaluated at (75) on every old window and decoupling; that identification and C2–C3 are PR-H's actual-step obligations (item 2), and DR on the full polydisc is item 4. **Status: reduced** to items 2 and 4.

## 7. LOC (D6): the first remaining Outstanding statement

### 7.1 What is needed

F6 (L905) needs \(h_j\le\delta'_j/8\) and \(h_j<r_{\rm sol}/4\), where (L885)
\(h_j=\max_{b\in\mathfrak E}|i^{-1}\operatorname{Log}(V^\sharp(b)V(b)^{-1})|\), \(V=M_-(U_+)\) is the true reference and \(V^\sharp=M_-(U_+^\sharp)\) the localized one. Its proof turns LOC into this bound by \(R_\sharp\ge MR_t/4\ge c_N\ell_t^r/4\) (RUN-low, now Theorem 1) and \(r>1\). The localized reference is a design input: ST-test (L152) says "The reference is formed from data in \(X^\sharp\), the quarter-cell enlargement of the component, with a specified local boundary rule", and ST-test\(^{\rm hol}\) (L154) says "The localized-datum rule is holomorphic". F7 (L918) needs the rule to use "only its declared data". So LOC is a statement about a rule \(\mathsf R\): \(D^\sharp=\mathsf R(D_+|_{X^\sharp})\), \(U_+^\sharp\) its canonical background.

**Remark 7.0 (what LOC must deliver, at least).** F4 uses \(h_j\) twice: to place the passing support in the tube around \(V\), with F2's converse (L896); and to bound the source relative to \(V\), which feeds DR and the budget (73). The first use disappears if F2–F3 are centred at \(V^\sharp\) on the component's own equations: if the rule satisfies (L2) below, then \(V^\sharp\) agrees with \(D_{\rm old}\) on every retained row in \(X^\sharp\) and \(F(V^\sharp)=D_+\) on the component's added rows (both because retained rows are copied by \(F\), L781, and \(M_\pm(U^\sharp_+)=D^\sharp=D_+\) there), and F2's equations read only double blocks inside \(X^\sharp\). The second use remains: the source \(\operatorname{Log}(D_{\rm old}V^{-1})\) on removed rows is at most \(|u^\sharp|+h_j\). So the minimum LOC must deliver is \(h_j\le C_h\delta'_j\) with a structural \(C_h\) (absorbed into \(C_A\) of (71)). This is a proposal to recentre F4, which would change frozen ST1's F4; I record it and do not use it below.

### 7.2 Attack 1: LOC-form with a local rule

**Proposition 10 (LOC-form fails for every local rule).** Let \(\mathsf R\) be any rule for which \(D^\sharp\) depends only on \(D_+|_{X^\sharp}\). Then there are admitted real data for which LOC-form (L155) fails.

*Proof.* LOC-form requires \(D^\sharp=e^{iB_\Delta}D_+\) rowwise with \(\|B_\Delta\|_\infty\le r_B\), and ST1 takes \(r_B\) small (\(\delta_B\le r_B/40\), row 4; Lemma 5 uses \(\delta_B\le1/40\)). On a large torus let \(D_+\equiv I\) on every determining row (the datum of the flat background). Pick a row \(c_1\) at distance at least \(2w\) from \(X^\sharp\), and put \(D'_+(c)=e^{i\beta\chi(c)\sigma_3}\) with \(\beta=3r_B\), where \(\chi\in[0,1]\) is \(1\) at \(c_1\), \(0\) on \(X^\sharp\), and changes by at most \(1/w\) between rows sharing a datum loop. The perturbation is abelian, so every datum loop of \(D'_+\) has holonomy \(e^{i\beta(\text{signed sum of }\chi)\sigma_3}\) with angle at most \(4\beta/w\); for \(w\) large this is below every test ceiling (58) and the regularity ceiling of A1/F0/REG, so \(D'_+\) is admitted, as is \(D_+\). Both agree on \(X^\sharp\), so the rule gives the same \(D^\sharp\). The group-angle distance \(d(g,g')=|\operatorname{Log}(gg'^{-1})|\) is a bi-invariant metric near \(I\). If LOC-form held for both, then at \(c_1\)
\(3r_B=d(D_+(c_1),D'_+(c_1))\le d(D_+(c_1),D^\sharp(c_1))+d(D^\sharp(c_1),D'_+(c_1))\le2r_B\), a contradiction. ∎

**Why Attack 1 fails.** Admitted data outside \(X^\sharp\) are not determined, even approximately in the raw rowwise norm, by data inside \(X^\sharp\). LOC-form asks for exactly that. ST1's own remark (L916) already rejects inferring the common chart "from real regularity of two data"; Proposition 10 shows no local rule can supply it. So LOC must be LOC-decay.

### 7.3 Attack 2: a regional reference with a boundary current

*Idea.* Let \(U^\sharp_+\) be the canonical background of the **restricted** system on \(X^\sharp\) (action \(S_{X^\sharp}\), data \(D_+|_{X^\sharp}\), zero boundary current). This is local. Compare it with \(U_+\): by the structure of ST1 Lemma 6 (L366–369, an independent boundary current \(\mathbf J=J+\delta\) with \(\delta=0\) on bonds touching \(\Omega_1\)), \(U_+|_{X^\sharp}\) is critical for \(S_{X^\sharp}\) with the independent boundary current \(J^\circ(U_+)\) on bonds touching \(\partial X^\sharp\), because a variation supported in \(X^\sharp\) changes \(S_{\Omega_0}\) and \(S_{X^\sharp}\) by the same amount except on plaquettes crossing \(\partial X^\sharp\), whose first variation is that current. Join the two by \(J_s=sJ^\circ(U_+)\), \(s\in[0,1]\). The \(s\)-derivative of the critical point solves the linearized constrained equation with a force supported on the boundary bonds, of size \(\le C_U\ell^{2r_R}\varepsilon\) by (59). P82 Theorem P bounds such weighted forces with exponential weights \(w(y)/w(z)\le e^{\theta d(y,z)}\) (cp12 D1), so the derivative at removed rows is at most \(C e^{-\theta R_\sharp}\) times the force; integrating in \(s\) gives LOC-decay with room to spare, and existence along \(s\) follows by continuation from \(s=1\) with P82's inverse.

*Exact failure.* P82's geometry (cp12 D1: "separated nested regions \(\Omega_j\)") and A1's "admitted separated determining system" (ST1 Lemma 5, L347) require ST1 (3), \(\operatorname{dist}_\infty(\Omega_{q+1},\Omega_q^c)>\rho_0\xi_q\), with \(\Omega_q^c\supset\Omega_0^c\). For the restricted system \(\Omega'_q=\Omega_q\cap X^\sharp\), \(\Omega'_0=X^\sharp\). A stage component lies in the region being remade, and its quarter-cell enlargement lies in deeper members: SA 17578 (as quoted in geoh-draft Lemma 7.2, unrefereed) gives \(\Omega_i^c\cap X=H_i^{[8]}\), well inside the class component \(X\), so near \(\partial X\) every point lies in \(\Omega_q\) for all \(q\le t\). Wherever a member \(\Omega_q\), \(q\ge1\), meets \(\partial X^\sharp\), \(\operatorname{dist}(\Omega'_q,(\Omega'_0)^c)=0\) and (3) fails. No frozen text proves P82 Theorem P or A1's existence and uniqueness for a determining system whose outer boundary cuts its deep members. Eroding the members near \(\partial X^\sharp\) restores (3) but changes the determining map there; comparing critical points of two different determining maps is what ST1 avoids by design (L761: "it never compares two different determining maps"), and no frozen text supplies it.

### 7.4 Attack 3: a global localized datum and a path

*Idea.* Keep the global determining system, so that (15) applies, and localize the **datum**: \(D^\sharp=\mathsf R(D_+|_{X^\sharp})\) is a global datum equal to \(D_+\) on \(X^\sharp\), and \(V^\sharp=M_-(\Phi(D^\sharp))\) with \(\Phi\) the canonical continued background. The following implication is proved.

**Lemma 10′ (LOC-decay from a path).** Suppose \(D^\sharp\) and \(D_+\) are joined by a piecewise-\(C^1\) path \(s\mapsto D_s\) of admitted real data of the same determining system, with \(D_s(c)\) independent of \(s\) for every row \(c\) within distance \(R_\sharp/2\) of the full stage carriers, and with rowwise angular speed \(|\dot B_s(c)|\le C_{\rm path}\), where \(\dot B_s(c)=i^{-1}\frac{d}{ds}D_s(c)\,D_s(c)^{-1}\). Then, in the canonical (CV) representative,
\[
 h_j\le C'_FC_{\rm path}S_4(a)\,e^{-aR_\sharp/2},\qquad a=\min(1,\theta_4/2),          \tag{7.1}
\]
with \(C'_F\) and \(S_4\) as in F6. Hence LOC-decay holds with \(c_{\rm loc}=a/2\), \(C_{\rm loc}=C'_FC_{\rm path}S_4(a)\), and F6's conclusion follows after a ceiling on \(\gamma\).

*Proof.* By Lemma 5 (L347–359) the canonical continuation is independent of the real centre on each tube (32); so \(D\mapsto\Phi(D)\) is single-valued and real-analytic on admitted real data, and on the chart at \(D_s\) its raw coordinate (6) has derivative \(\dot B_s\) along the path. By (15), at every point of the path (P82° with M1, uniformly on the admitted real layered class: cp12 Theorem 3, conditional on its imports), each row direction \(e_c\) moves \(H,\nabla H,D^{\mathsf T}DH,J,u\) at \(y\) by at most \(C_4e^{-\theta_4d(y,y_c)}|e_c|\), at interior elements. The canonical gauge is a product of local mean contours with bounded Lipschitz constants (Lemma 8 proof, L583–588), and \(M_-\) reads a fixed carrier; so at a removed row \(b\), \(|\frac d{ds}\operatorname{Log}V_s(b)|\le C_F\sum_ce^{-\theta_4d(b,y_c)}|\dot B_s(c)|\). The sum runs over rows at distance at least \(R_\sharp/2\), so Lemma 2's summation (22), exactly as in F6 (L909–911), bounds it by \(C'_FC_{\rm path}S_4(a)e^{-aR_\sharp/2}\). Integrate over \(s\in[0,1]\). For the \(\gamma\) ceiling, F6's last paragraph applies verbatim with \(c=ac_N/8\). ∎

So Attack 3 reduces LOC to the existence of the rule and the path.

**Lemma LOC♮ (Outstanding).** There are a rule \(\mathsf R\) and a constant \(C_{\rm path}\), fixed before \(\kappa\) and independent of \(M,\bar\kappa\), such that for every finite history, every stage (level \(j\), operation level \(t\)), every stage component with quarter-cell enlargement \(X^\sharp\), and every admitted real datum \(D_+\) of the stage:
* **(L1) local:** \(D^\sharp=\mathsf R(D_+|_{X^\sharp})\) is a real datum of the stage's determining system depending only on \(D_+|_{X^\sharp}\) and the geometric record;
* **(L2) agreement:** \(D^\sharp=D_+\) on every row of \(X^\sharp\);
* **(L3) admission:** \(D^\sharp\) is admitted — regular in the sense of A1/F0/REG, with its datum loops obeying (58) with exponents bounded by (56);
* **(L4) path:** \(D^\sharp\) and \(D_+\) are joined as in Lemma 10′;
* **(L5) holomorphy:** \(\mathsf R\) extends holomorphically to the complex chart of ST-test\(^{\rm hol}\), is real on real data, and commutes with CV's canonical representative.

*Exact failure of Attack 3.* (L1)–(L2) and (L5) are a definition. (L3) and (L4) are not supplied by any frozen text, and the constructions available here fail:
1. *Clamped extension* (hm Lemma 3's method, L106–117): it needs one real gauge with \(|A|,|\nabla A|\le1/16\) on the whole box being extended. \(X^\sharp\) has size of order a cell, \(MR_t\) level-\(t\) units; ST1's witnesses give gauges only on cubes of side \(O(LM)\) (L101, L118). A gauge on a collar of \(\partial X^\sharp\) must be patched from these, and for non-abelian data the patching potentials grow with the collar diameter times the curvature; no frozen text bounds them.
2. *Contraction of the outside data in a tree gauge*: scaling non-tree logarithms \(a\mapsto(1-s)a\) keeps curvature small only if the logarithms are small; in a tree gauge they are holonomies of long loops, of size up to (distance)\(\times\)(curvature), and the non-abelian commutator terms then spoil (58) along the path.
3. *Topology*: admitted data on the torus outside \(X^\sharp\) can carry non-trivial non-abelian holonomy around non-contractible cycles (Proposition 10's construction, made non-abelian). A path must change it while keeping every datum loop small. The space \(\mathrm{Hom}(\mathbb Z^4,SU(2))\) of flat holonomies is connected, which suggests (L4) is true, but a lattice retraction of near-flat data onto flat data, with rowwise speed and curvature bounds uniform in volume, is not in the library or in the SA texts read here.

**Status: Outstanding.** LOC♮ is the first DOM statement in proof order that is neither proved nor reduced to another critical-path item: F6 → F4 → (70) → (73) → Theorem 14 at every stage. Its owner is ST1 (stage test design). The only frozen statements it would use are A1/F0/REG, Lemma 5, (15) and Lemma 2's summation.

## 8. ST-test, ST-test\(^{\rm hol}\), BOX and IN1's domain (D7–D10)

### 8.1 ST-test

ST-test (L152) has a design part (the free rows are tested against \(V^\sharp\) at \(\delta'_j\); the reference is local) and a quantitative part ("Every removed row, pivots included, lies within \(r_{\rm sol}/4\) of that reference"). The quantitative part is what F4 reads (L896). I prove it from two readings of ST1 and (L2)–(L3) of LOC♮; it does not need LOC's estimate.

* **(ISO)** Every pivot \(b_0(c)\) lies on a level-\(j\) datum loop \(\tau_p\) inside \(X^\sharp\) whose other three edges are free removed rows or retained rows. *Reading:* F2 (L836) "CH supplies isolated pivots"; L803 "each equation involves its own pivot and no other selected pivot"; ST1's source table (L1626) cites SA 8165–8299 for isolated pivots. A bond lies on six plaquettes; with pivots chosen as positively oriented bonds at block centres, the plaquette on the negative side of any transverse direction contains no other pivot. **This is a reading of CH; the referee should check it against SA 8165–8299.**
* **(RET)** The retained older tests include (58) on every level-\(j\) datum loop of the old datum inside \(X^\sharp\). *Reading:* L152 "Older tests and stored densities are retained exactly"; RUN (L145) "The real stage tests obey (58) in their stated units".

**Theorem 11 (ST-test's quantitative clause).** Assume (ISO), (RET), and (L2)–(L3) of LOC♮. Let \(d(g,g')=|\operatorname{Log}(gg'^{-1})|\) on \(SU(2)\). There is a ceiling on \(\gamma\) such that on the passing set of the free-row test, \(\{d(D_{\rm old}(b),V^\sharp(b))<\delta'_j\ \forall b\in\mathfrak F\}\), every removed row \(b\in\mathfrak E\), pivots included, has \(d(D_{\rm old}(b),V^\sharp(b))<r_{\rm sol}/4\).

*Proof.* Free rows: \(\delta'_j<r_{\rm sol}/4\) after a ceiling, since \(\delta'_j=A_1g_j\ell_j^{p_1}\le A_1F_{p_1}(\gamma)\).
Retained rows in \(X^\sharp\): \(F\) copies retained rows (L781), so \(M_-(U)\) and \(M_+(U)\) agree on them for every field \(U\). Hence \(V^\sharp=M_-(U_+^\sharp)=M_+(U^\sharp_+)=D^\sharp=D_+=D_{\rm old}\) on retained rows of \(X^\sharp\), using (L2) and the fibre constraint \(F(D_{\rm old})=D_+\).
Pivots: \(d\) is a bi-invariant metric (the rotation angle), so \(d(xy,x'y')\le d(x,x')+d(y,y')\) and \(d(x^{-1},x'^{-1})=d(x,x')\). Write the holonomy of \(\tau_p\) as \(P=a\,p^{\pm1}b\,c\) with \(p=b_0(c)\) and \(a,b,c\) the other edges (with orientations). Then \(p^{\pm1}=a^{-1}Pc^{-1}b^{-1}\), and
\[
 d(D_{\rm old}(p),V^\sharp(p))\le\sum_{e\ne p}d(D_{\rm old}(e),V^\sharp(e))+d(\partial D_{\rm old}(\tau_p),I)+d(\partial V^\sharp(\tau_p),I).
\]
By (ISO) the three other edges are free (each \(<\delta'_j\)) or retained (each \(0\)). By (RET), (58) and (56), \(d(\partial D_{\rm old}(\tau_p),I)\le C\,C_{\rm te}C_R^2\ell_m^{2r_R}\varepsilon_m\). By (L3), \(D^\sharp\) is admitted, so its background obeys (59) (Lemma 10, L681), and AV/CURV (L127) bound its averaged datum loops: \(d(\partial V^\sharp(\tau_p),I)\le C\,C_{\rm sm}L^2C_U\ell_m^{2r_R}\varepsilon_m\). Since \(\ell_m^{2r_R}\varepsilon_m\le A_0F_{p_0+2r_R}(\gamma)\), the right side is \(<3\delta'_j+C'A_0F_{p_0+2r_R}(\gamma)<r_{\rm sol}/4\) after a ceiling on \(\gamma\). ∎

**Status of ST-test.** Quantitative clause: **proved given (L2)–(L3)**. Design clause ("formed from data in \(X^\sharp\)"): this is (L1). So ST-test is proved once LOC♮'s rule exists.

### 8.2 ST-test\(^{\rm hol}\)

**Proposition 12.** Assume LOC♮ (L1)–(L5). Put \(r_{\rm hol}=\min(r_B,r_{\rm sol},r_u)/8\) and \(M_*=1\). Then ST-test\(^{\rm hol}\) holds, with its bound \(\|Y\|\le C_Qr_1(i)\) replaced by \(\|Y\|\le C_QL(1+\beta_s)r_1(i)\).

*Proof.* (L5) gives holomorphy, reality and CV. \(V^\sharp\) is holomorphic in the datum because \(\Phi\) is (Lemma 5) and \(M_-\) is a finite analytic average (AV). On the ball of radius \(r_{\rm hol}\) about a real admitted datum, both data lie in the charts of Lemma 5 and F2, and the relative row logarithm is a composition of holomorphic maps with values of size \(\le4r_{\rm hol}<1\), so bounded by \(M_*=1\). Real LOC on the real slice is Lemma 10′ (given (L4)). Real coordinates: \(\|X\|<\delta'_j<r_{\rm hol}/4\) after a ceiling. Imaginary coordinates come from the complex potential through AV's row bound \(|B(c)|\le C_Q\xi_q\sup_{D(c)}|A|\) (L127) and Theorem 3's \(\xi|A'|<L(1+\beta_s)r_1\). Both constants are fixed before \(\kappa\). FC7 uses \(\|Y\|\) only through a ceiling on \(\gamma\) (L1343–1353), so the extra factor \(L(1+\beta_s)\) is harmless. ∎

**Status: proved given LOC♮.**

### 8.3 BOX

**Proposition 13 (BOX, reduced).** Use geoh-draft's Definition 7.1 of \(\mathcal B_t\) (loops with all corners in \(\Lambda^{\rm pr}\)). Then:
1. *Existence clause of BOX-bg.* If the output datum \(D_{\rm out}\) is admitted for the output's separated determining system (ST1 Lemma 2 under GEO-prep), its canonical real regular critical background exists, by ST1 Lemma 5 (A1/F0/REG). **Proved** as an implication.
2. *Unchanged loops.* An output loop that reads no variable changed by the main step has the same datum as before, so the inherited (58) holds, converted to output levels by the three cases of SA 17624 (L673). **Proved.**
3. *Loops in \(\mathcal B_t\).* The bound \(C_{\rm bx}C(M)\varepsilon_t\) is the output test on the box datum (SA 17656's box minimizer with its level-\(t\) test). **Reduced** to the output test definition; I did not read SA 17640–17660 and do not claim more.
4. *BOX-id and BOX-resp.* These are DR's statements for the box source \(S_{\rm bx}\): holomorphy on the full switch polydisc, specification at one, splitting, and the decay \(n_b\le C(M)E_{\bar\kappa}\delta'_te^{-\mu d_+(b,S_{\rm bx})}\); BOX-id is Lemma 12's identification argument (uniqueness in the regular orbit, L805) applied to the box. **Reduced** to item 4 (DR), output instance.
5. *Straddling loops* (reading a changed variable, not in \(\mathcal B_t\)). By BOX-id and Lemma 7 (45), their curvature differs from that of the averaged preceding background by at most \(C\,C(M)E_{\bar\kappa}\delta'_t\), and \(\delta'_t/\varepsilon_t=(A_1/A_0)\ell_t^{p_1-p_0}\to0\). Whether this gives "the inherited (58), converted to their output levels" depends on the formation exponent of a straddling loop, which is the minimum over its stencil and may be the small inherited exponent of its outside corners; geoh-draft Theorem B leaves this clause to BOX-bg ("That is BOX's analytic content"). **Not attacked here.**

BOX is used only at outputs, after the stages of the same operation, so in proof order it comes after LOC♮.

### 8.4 IN1's domain

**Proposition 14 (a specification of \(\mathcal D_j(X)\)).** Let \(\sigma_j\) be the main-step input structure of level \(j\), and for a connected union \(X\) of level-\(j\) \(M\)-cubes put
\[
 \mathcal D_j(X):=\{P \text{ on the reads of }X:\ \text{every record of }\mathcal D_{a|\sigma_j}\text{ whose full read carrier lies in }X\text{ holds at }P\}.
\]
Under R♮ and ST1's inputs: (i) \(\mathcal D_j(X)\) contains "local gauges and potential/current bounds on every required subdomain, existence of the required averaging towers, and their uniform bounds" (IN1 L44) as records (R♮-w and core witnesses; R♮-s and R♮-c; tower records with Lemma 8's open domains); (ii) it is hereditary: \(X'\subset X\) imposes fewer records; (iii) "independent verification at every later read" (IN1 L195): every record is admitted at every later real background with half its radius (Lemma B4, L1527) and at every substituted complex point with half its gap (Theorem 14); (iv) it contains the polydiscs of Proposition 7 about admitted real points.

*Proof.* (i) is Definition R♮ and Lemma 2. (ii) is immediate. (iii) is B4 and (65) with Lemma 2. (iv) is Proposition 7. ∎

IN1 describes \(\mathcal D_j(X)\) "as in SA 5663–5755 (R4–R6)". If that phrase were read as the unweighted level-\(j\) R4 on a multi-layer \(X\), Proposition 4 shows the actual domain does not lie in it. IN1's text calls the core "specified"; Proposition 14 gives the specification that ST1 supplies. Whether IN1's Theorems 10–12 use any property of \(\mathcal D_j(X)\) beyond (i)–(iv) is part of IN1's H-SF and H-E (items 9–10), not checked here. **Status: the domain part is proved; formation stays H-SF.**

## 9. PR1(5b)

**Claim.** PR1(5b) does not belong to DOM. No frozen text on the path to T0 reads it, and frozen ST1 r4 supplies each of its clauses in its own design.

*Evidence.* (a) Readers. Grep counts of "layered-a3", "5b" and "stage-resp" in the frozen texts at this clone: `p82` 0, `in1` 1 (L143: "[layered-a3.md] also leaves actual stage admission conditional. Neither is a proof of H-SF." — a disclaimer, not a use), `hm` 0, `fp1` 0, `cp12` 0, `descent` 0, `st1-r4` 0, `nl1-L` 0, `ag1` 0, `tp1` 0, `pr-lay` 5. Pr-lay's five lines only distinguish (5b) from (5a) and say it "stay[s] open, as stated" (L372); pr-lay does not use it (L330: "It does not prove that actual domain admission or the tower bounds of PR1(5b) can be bypassed", which is a disclaimer, not a use). Layered-a3 (1)'s consumer is `stage-resp.md` (layered-a3 L9), which no frozen text cites.

(b) Replacement in ST1 r4. Layered-a3 (1) has two clauses in the lifted-radius design of `intrinsic-dom.md`:
* "\(\operatorname{dist}_\infty(D_e(t),\mathcal T_e^c)\ge\eta_*>0\)" along the stage path, for every tower record \(e\). In ST1 r4 each frozen tower keeps its own determining map ("This treats the whole fixed function and its open domain; it never compares two different determining maps", L761), and Lemma 8 gives its datum \(\|B(w)\|<C_QL\bar a<\delta_B/4\), "so Lemma 5 gives tube room" (L627), i.e. distance at least \(\delta_B/8\) from \(\mathcal T_e^c\) by (32). This is the first clause with \(\eta_*=\delta_B/8\), at every point of the substitution path \(|z|<\rho_X\), \(|s_\Delta|<e^{\bar\kappa}\) (Theorem 14, first bullet).
* "\(\|\partial_tF_a\|\le Cr_a^{\rm lift}\sum_lu_l\sqrt{1+|m-l|}e^{-D|m-l|}\)": a readout increment bounded by the forcing, spending "less than half each new mark's allowance" of the coefficient (R22) (layered-a3 L47–49). In ST1 r4 this is Lemma 11: the tower increment is at most \(K_{\rm tw}rw(n(x))\) with \(w(m)=\frac12d_*(m)r_0(m)\) and \(d_*\) from Lemma 1′/M2's coefficient (17), "at most one sixteenth of the gap" (L753–761). Unit lifts make \(r^{\rm lift}_a=r_a\) (L89, L1663: "the smoothed lift is unnecessary").
* The path itself, input (A) of stage-resp, is ST1's substitution (75) with F4's stage datum.

So the content PR1(5b) was meant to supply to the stage response is supplied, in ST1 r4's design, by Lemmas 5, 8, 11 and Theorem 14 (conditionally on their imports, which include LOC through F4). Layered-a3's own open lemma (its §20) concerns the lifted design and is not on the path. **PR1(5b) should leave the critical path.** If a referee finds a frozen consumer that reads layered-a3 (1) itself, this claim fails and (1) returns as a separate item.

## 10. Order of the constants

IN1's rule (in1 L223: "A returned constant must precede every choice it bounds"; rows 1–10, L227–236, with Amendment 1's floors \(L>L_0^\natural\) at row 2 and \(\kappa\ge\kappa_0^\natural(L)\) at row 4, L666–675). ST1's rows are given where ST1 fixes the constant (L160–171); ST1 rows 1–6 sit inside IN1 rows 1–3, ST1 row 7 is IN1 row 4, ST1 row 8 is IN1 row 5, ST1 row 9 is IN1 row 6, ST1 row 10 is IN1 row 9.

| Constant (where defined here) | Value or condition | Fixed at | Reads | Before \(\kappa\), free of \(M,\bar\kappa\)? |
|---|---|---|---|---|
| \(c_N\) (Theorem 1) | \(2^{-r}\) | IN1 row 1 (with \(r\)) | \(r\) | yes |
| \(L\)-floor (Theorem 1 remark) | \(L\ge2(2+r\log_LK_1)\), \(K_1=2+r+\log(1+\bar B)\) | IN1 row 2, with \(L>L_0^\natural\) | \(r\), frame constant \(\bar B\) | yes, **if** \(\bar B\le C_*\log L\) |
| \(\lambda_\sigma\), \(C'_\lambda\) (3.2) | \(L^3\); \(\max(2^{2r_R}C_\lambda,L^3)\) | IN1 row 3 (pr-lay §2 step 3) | \(L,r_R,C_\lambda\) | yes |
| \(h\) | \(\min(a_R,a_W,a_h,1/2)\) | IN1 row 3 | R, W | yes |
| \(a_\flat\) (R♮-w) | \(\le h/4\) | ST1 row 4 (IN1 row 3) | \(h\) | yes |
| \(r_{\rm hol},M_*\) (Prop. 12) | \(\min(r_B,r_{\rm sol},r_u)/8\); \(1\) | ST1 rows 2–3 (IN1 row 3) | chart radii | yes |
| \(K_{\rm main}\) (Cor. 9) | \(2C_DC_AC_{\rm lev}C/(ar_*)\) | ST1 row 6 (IN1 row 3) | DR base constants, LEV, \(r_*\), \(\beta_s,\theta_s\) | yes |
| \(w^\natural\) (Prop. 7) | \(c_{\min}r_0(m)/4\) with \(r_*\) of row 6 | ST1 row 6 | \(c_{\min},r_*\) | yes (the radius table itself is late) |
| \(C_{\rm path}\), \(c_{\rm loc}=a/2\), \(C_{\rm loc}=C'_FC_{\rm path}S_4(a)\) (LOC♮, Lemma 10′) | required by LOC♮ | IN1 row 3 (LOC is in ST1 row 2) | \(\theta_4\), \(L\), carrier sizes | **required** by LOC♮'s statement |
| \(M_{\rm dom}\) (Theorem 5) | \(M\ge3+e_c\) | IN1 row 5 (ST1 row 8 locality floor) | \(e_c\) | it is an \(M\) floor |
| \(R_{\rm line}\) (Theorem 3) | any fixed \(\ge1\) | when the consumer fixes its disc (IN1 Lemma 2) | — | before \(\gamma\) |
| \(c_{\rm ct}\) (6.2) | \(\le1/(4E_{\bar\kappa}K_{\rm main})\) | IN1 row 6 (cp12 L544) | \(\bar\kappa\) | no: reads \(\bar\kappa\), as cp12 allows |
| \(\gamma_{\rm dom}\) | (5.3); pr-lay (23) with (3.3); Theorem 1's \(\gamma^{-2}\ge\max(4,2c_5)\); Theorem 11's pivot ceiling; Prop. 12's \(\delta'_j<r_{\rm hol}/4\); Lemma 2's \(a_\flat\) formation ceiling; Cor. 9's pinning term; F6's ceiling | IN1 row 9 | everything above, \(C_0,C_1,A_0,A_1,M,\bar\kappa\) | no (it is the final ceiling) |

No constant fixed before \(\kappa\) reads \(C_0,C_1,A_0,A_1,M,\bar\kappa\) or an activity amplitude \(b_f\). The radii \(a_0,a_1,j_0\) of hm and descent are no longer free choices: they are the functions \(\varrho_\gamma,a_0^\gamma\) of (5.2), and hm (24), descent (7)–(8) become the ceiling (5.3). Raising \(L\) or \(\kappa\) (Amendment 1) weakens no DOM step: the DOM early constants read \(L\) and are fixed after it, and none reads \(\kappa\).

## 11. Statements used wrongly, and what changes elsewhere

No other file was edited. These are findings for the lead.

1. **"Every ST1 chain domain inside R4"** (assembly-status L127 and item 5, L186). False as stated for hm's and descent's unweighted R4 on supports reaching layers \(m\le k-n_0\) (Proposition 4). The correct obligation is Theorem 5 (inclusion in \(\mathcal K^\natural\)) with Theorem 6 (hm and descent proofs read only \(\mathcal K^\natural\)). Descent L285 does not claim the inclusion; it is not wrong.
2. **Hm L33 and descent (2): "imposes SA R4 on \(Y\)".** Read as unweighted level-\(k\) bounds on a multi-layer \(Y\), this is stronger than SA's layered radii (pr-lay L254 cites "SA 6141–6155 defines layer radii on represented domains"). The theorems are true as stated; their hypothesis is never met on the actual domain when \(Y\) reaches shallow layers. A consumer citing hm Theorem 7 or descent Theorem 5 at actual pairs must use the \(\mathcal K^\natural\) reading of Theorem 6. Suggested wording for a later hm/descent amendment: replace "\(P\in\mathcal K(Z;a_0,a_1,j_0)\)" by "\(P\in\mathcal K^\natural(Z;Z_0;\varrho,a_0)\cap\mathrm{Rep}(Z)\), \(\varrho<\min(r_{\rm loc}/2,1/(2H_0))\)".
3. **IN1 L44 "as in SA 5663–5755 (R4–R6)".** Same issue if read unweighted; Proposition 14 gives the own-scale specification.
4. **Pr-lay L254** asks that scale changes "be paid when verifying D and B at current scale". Under R♮ there is no inherited-to-current conversion: each structure carries its own current-scale records, so the layered-a3 (3) loss never arises in D. This resolves the Outstanding mark; it does not contradict it.
5. **ST1 L154, ST-test\(^{\rm hol}\)'s \(\|Y\|\le C_Qr_1(i)\).** With the largest-incident-scale convention the honest bound is \(C_QL(1+\beta_s)r_1(i)\) (Proposition 12). Harmless, since FC7 uses it only through a ceiling on \(\gamma\).
6. **ST1 L1542, "complex input membership remains this hypothesis".** Under R♮ it is not a separate hypothesis: Theorem 8 reduces it to DR, the main-step source supply, LOC♮ and FCON.
7. **cp12 (27) and L565** ("the application must place its evaluation centres and fluctuation shifts in this smaller domain. That coverage is not proved here"). On ST1's route the coverage is Corollary 9, with the new requirement (6.2) on \(c_{\rm ct}\).
8. **Assembly-status L51, L186: "I cannot tell from the texts whether the T0 path still reads PR1(5b)".** It does not (§9).
9. **Possible over-reach to check:** geoh-draft Lemma 7.2's "\(2\le N^0_t\le R_t-1<\mathsf N_t\)" cites CA-I 53773; Theorem 1 proves \(2\le N^0_t\le t\) and the defining identity, not the upper bound \(R_t-1\). I did not read CA-I 53773.

## 12. Status of each step

| Step | Status | Imports |
|---|---|---|
| Lemma 2 (R♮ admissible) | proved | ST1 Lemmas 1′/M2, 9′, 10, 11, B4, Theorem 14 |
| Theorem 1 (RUN-low) | proved for \(t\ge1+\rho_1\); remark conditional on \(\bar B\le C_*\log L\) | SA (R19) |
| Theorem 3 (D) | proved | R♮; pr-lay Lemma 7, Theorem 8 (with R, W, G, B, Q) |
| Proposition 4 | proved (counterexample to the literal R4 inclusion) | ST1 Lemma 8, M2 |
| Theorem 5 (\(\mathcal K^\natural\)) | proved | R♮, (G\(_k\)), hm (23), descent Lemma 1 |
| Theorem 6 | proved by reading; **referee must check items 1–9** | hm L53–327, descent L184–249 |
| Proposition 7 (polydisc room) | proved | ST1 Lemmas 9′, 11, (T2) |
| Theorem 8 (membership) | reduced | DR (item 4), main-step supply, LOC♮, FCON (item 7) |
| Corollary 9 (H-ct ball) | reduced | DR (item 4); PR-H C2–C3 identification (item 2) |
| Proposition 10 (LOC-form impossible) | proved | — |
| Lemma 10′ (LOC-decay from a path) | proved | (15) via cp12 Theorem 3; ST1 Lemma 5, Lemma 2 (22), F6 |
| **Lemma LOC♮** | **Outstanding** (three attacks, §7.2–7.4) | — |
| Theorem 11 (ST-test) | proved given LOC♮ (L2)–(L3) and the readings (ISO), (RET) | ST1 F2, (56), (58), (59) |
| Proposition 12 (ST-test\(^{\rm hol}\)) | proved given LOC♮ | Lemma 5, F2, AV |
| Proposition 13 (BOX) | items 1–2 proved; 3 reduced to the output test; 4 reduced to DR; 5 not attacked | Lemma 5, Lemma 7, Lemma 12 |
| Proposition 14 (IN1 domain) | proved for the domain part | R♮, B4, Theorem 14, Proposition 7 |
| §9 PR1(5b) | settled: not a DOM item | grep of frozen texts; ST1 Lemmas 5, 8, 11 |

## Result

**Proved here.** For the actual roster R♮ (current-scale records at every structure, which is FINISH row 272's design clause (I-G) with ST1's unit lifts; Lemma 2 checks it against frozen ST1): PR-lay's D (19) at every structure, every substituted point and every line disc (Theorem 3); the inclusion of every chain domain in the class \(\mathcal K^\natural\) on which hm Theorems 7–8 and descent Theorem 5 are actually proved (Theorems 5–6); polydisc room at admitted real points (Proposition 7); RUN-low from SA's frame (Theorem 1); IN1's domain specification (Proposition 14); the impossibility of LOC-form for local rules (Proposition 10); LOC-decay from a path (Lemma 10′); ST-test and ST-test\(^{\rm hol}\) from LOC♮'s rule (Theorem 11, Proposition 12). Proposition 4 is a counterexample to the literal clause "every ST1 chain domain inside R4".

**Reduced to other items.** ST1's complex input membership (Theorem 8) and the H-ct ball (Corollary 9) reduce to DR (item 4), the main-step source supply, FCON (item 7) and PR-H's identification (item 2), plus LOC♮. BOX reduces to DR's output instance and the output test, except its straddling-loop clause, which is not attacked here.

**First remaining Outstanding statement: Lemma LOC♮** (§7.4): a local, holomorphic, real localized-datum rule whose output is admitted and joined to the true datum by a path of admitted data, constant near the stage carriers, with bounded rowwise speed. Attack 1 (LOC-form) fails for every local rule (Proposition 10). Attack 2 (regional reference with a boundary current, P82 with forces) fails because the restricted determining system is not separated at \(\partial X^\sharp\), and no frozen text treats such systems or compares two determining maps. Attack 3 (global localized datum, (15) along a path) proves LOC-decay from the path (Lemma 10′) and fails at the existence of the admitted extension and path: clamped extension needs one small gauge on a cell-sized collar, tree-gauge contraction breaks curvature smallness for non-abelian data, and a lattice retraction of near-flat data onto flat data with uniform bounds is not available.

**PR1(5b)** does not belong to DOM and should leave the critical path (§9).

**Imports.** Frozen: `st1-r4.md` (with its own imports), `pr-lay.md`, `hm.md`, `descent.md`, `cp12.md` (Theorem 3 for (15)), `in1.md`, `p82.md` through cp12. Unrefereed, used only as noted: geoh-draft Lemma 2.0 and Lemma 7.2 (for SA 17578), dr-draft (only to name item 4's content). SA (R19) at L6017–6026. Geometry G is item 3.

This text is pass 1. It is research text, not an audit, and grants no status. Not checked by another model.
