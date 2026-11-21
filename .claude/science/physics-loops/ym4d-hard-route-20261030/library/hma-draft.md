# HM-A: the actual Gaussian family of the step (T0 critical-path item 6), pass 1

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), 2026-11-05, pass 1 (Claude drafts at length). Not distilled, not refereed, not checked by another model. Research text, not an audit; it grants no status. Nothing here goes outward. All arguments are by hand; no step is computer-assisted, and every step is a finite-dimensional statement meant to be Lean-formalizable.

**Credit.** SA, CA-I and Y3 mean the outline `ym4.tex`, the complete account I and `YM3_I.tex` of **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text**, at the pinned revision 31a47c543775 (local copies in `scratchpad/sa/`). Their regular-pair operators, collared Gaussian, unmarked-majorant (UM) chapter, soft axial gauge, and the relative gauge form of Y3 are theirs. The background-field, propagator and walk methods come through the library from **Tadeusz Bałaban**; the parametrix exposition used by h-walk and P82 is **Jonathan Dimock**'s. Library texts by Claude and Codex keep their stated premises.

Line numbers "L" refer to files of this clone (`library/…`), and "SA n" to lines of `scratchpad/sa/ym4.tex`. I read every line I quote.

## 0. Result and status

The gauge form is fixed by the lead's design decision (FINISH row 278): the actual step uses Y3's relative soft-gauge form, as in frozen `descent.md` Theorem B. I do not reopen it. Under that decision this note proves:

| Clause | Statement here | Status |
|---|---|---|
| (a) carriers | Theorem 3.2: the step's Gaussian carriers are the full-read hulls of frozen hm/descent with Y-labels; every clause that IN1 H-M, NL1 CI-Gauss, ci-form H-G/H-S and td J read is supplied on all of R4 with the stated radii | **proved** (conditional on the imports of §2) |
| (b1) local formation bound | Theorem 4.3: the gauge-type potential satisfies UM1 with norm \(a_{\rm GF}\le C_{\rm GF}M^4\delta(\theta)\to0\); Lemma 4.1: no completed-form correction F is needed; Lemma 4.4: no other potential type changes | **proved** (conditional) |
| (b2) vacuum bound | Theorem 5.2: local vacuum decomposition of the step's normalizer \(-\tfrac12\log\det\mathsf A^{\rm Y}\), with heredity, holomorphy, gauge invariance, early rooted bound, Lipschitz bound and polymer bound | **proved** (conditional) |
| UM cost | Corollary 4.5: UM4–UM6, UM14 and \(C_0^{\rm UM}\le1\) with early \(W_0\), and UM12–UM16 for the actual gas, once the non-gauge potential types have UM1 norm \(\le W_0/4\) | **proved** given that one input; the input is item 8's (CI) |
| (c) G-ID, physical clause | Theorem 6.6 and Corollary 6.7: at every admitted complete physical pair in R4 the Gaussian part of the step has precision \(\mathsf A^{\rm Y}(P_W)\) | **proved** (conditional on P81, P82 through a3-derivative §6, and the physical-pair hypotheses PH1–PH4) |
| constants | §7: every new constant is placed in IN1's rows 1–10 with Amendment 1 | **proved** (bookkeeping) |

No item-6 statement is left Outstanding inside this note. The inputs that remain open belong to other critical-path items and are listed in §8 with owners: P81/P82 at the physical background (items 1, 5 and BG1); admission of physical pairs and of every consumer domain into R4 with the radii (24) (item 5, DOM; reduced here in Lemma 6.10); UM1 for the non-gauge potential types (item 8, CI). G-ID here is **G-ID(cov)**, the physical-covariance clause of hm L45 and descent L68. It is **not** TP1's G-ID(TP) (tp1 L130), which stays an import of TP1 (§1.4).

## 1. The clauses exactly as the frozen consumers read them

### 1.1 IN1 (frozen `in1.md`)

**H-M, L99–106** (quoted in full, since every word is a clause):

> "**H-M (actual matrices and UM, FP1/PR1/NL1).** For the actual localized Gaussian functional and its actual carriers, on every disc \(|s_\Delta|<e^{\bar\kappa}\), the covariance datum \(C\) is complex symmetric, \(\Gamma\) is rectangular, and there are real reference matrices \(C_*,\Gamma_*\), with \(C_*\) symmetric positive definite, such that
> \(\|C_*\|+\|C_*^{-1}\|+\|\Gamma_*\|\le K_0,\ \|C-C_*\|+\|\Gamma-\Gamma_*\|\le H_0\{e^{b\bar\kappa-dM}+H_p(M)(a_0+a_1+j_0)\}+C_\tau|\tau-1|.\) (9)
> Here \(K_0\ge1\) and \(H_0,b,d,C_\tau>0\) precede \(\bar\kappa,M\); \(0\le H_p(M)<\infty\) is allowed to follow \(M\). The functional is normalized, hereditary in its declared carriers, wall-factorizing, holomorphic on these discs, and agrees at physical parameters with the actual fluctuation law. Its local dimension is at most \(c_m(LM)^4\) per cube. Import the finite-dimensional Gaussian comparison SA 13904–14089 (FG1–FG11) … Also import the UM carrier counts and logarithm implication SA 14276–14811."

I split it into the clauses used below:

- **HM-1** (matrices): \(C\) complex symmetric, \(\Gamma\) rectangular, real references, \(C_*>0\), and (9) with \(K_0,H_0,b,d,C_\tau\) before \(\bar\kappa,M\).
- **HM-2** (structure): normalized, hereditary in its declared carriers, wall-factorizing, holomorphic on the discs.
- **HM-3** (physical): "agrees at physical parameters with the actual fluctuation law".
- **HM-4** (dimension): at most \(c_m(LM)^4\) coordinates per cube.
- **HM-5** (imports): FG1–FG11 and the UM counts.
- **HM-0** (identity): "For the actual localized Gaussian functional and its actual carriers". This is the identification clause (a).

**Outstanding paragraph, L108**: "Lemma 2 below proves (9) for an auxiliary path-weighted construction under a *global* gap hypothesis. It does not identify that construction with H-M or prove heredity. … The enlarged-disc estimate with constants fixed before \(\bar\kappa,M\) remains an actual-construction obligation. Note: carrier-adopt.md §6 and inv-root.md … may make this item smaller than stated; this is to be checked against H-M."

**Lemma 2, L276–299** proves (21) for the path-weighted family (20) under a global gap; **L329–334** ("Outstanding — heredity is stronger than block factorization") gives the three-site chain in which that family's local covariance reads the exterior edge \(u\). Lemma 2 is therefore not a supplier of HM-0 or HM-2. I use it only to say which family the step does **not** use (§3.4).

**Lemma 3, L336–371**: "Under H-M, its scalar budget can be bounded by one before choosing \(\bar\kappa,M\)." Its proof fixes \(W_0\) by (22) before \(M\), imposes (23) as later floor/ceiling, and concludes \(C_0^{\rm UM}\le1\) and UM14. It reads only HM-1, HM-4, HM-5.

**Constant order, L225–236, rows 1–10**, with **Amendment 1, L666–675** ("\(L>L_0^\natural\)" in row 2; "\(\kappa\ge\kappa_0^\natural(L)\)" in row 4). Row 4 (L230): "H-M's early \(K_0,H_0,b,d,C_\tau\); Gaussian constants \(A=A_{K_0},\varepsilon_0,\rho_0\); geometric \(P,c_m\); fix \(W_0\) by (22). Choose \(\kappa\) …". Row 5 (L231): "Choose \(\bar\kappa,\kappa_1\) … then \(M\), a power of \(L\), meeting (23) and all collar/tower floors." Row 6 (L232): "… set \(\gamma_{\rm tilt}\) by (22). Choose \(A_1\), then \(A_0\); … absolute radii and current ceilings within (23)." Row 7 (L233): "Fix \(E_N,C_E,\ldots\)". Row 9 (L235): "Increase \(X_0\) …; set \(\gamma=X_0^{-1/2}\)."

### 1.2 NL1 (frozen `nl1-L.md`, Theorem 7)

L578–580: "3. **CI-Gauss:** on these full complex domains the actual precision/comparison package holds. This includes the actual matrices, normalization, heredity, wall factorization and early uniform envelope of frozen IN1 **H-M**; a real-background inverse alone is insufficient."

So CI-Gauss = HM-0, HM-1, HM-2 on "these full complex domains", the CI-maps domains of Theorem 7 item 2 (L573–577). Their inclusion in the domain where the family is built is the domain obligation DOM (assembly-status §3 item 5), not item 6.

### 1.3 The supplier texts' own statements of what is left

- `hm.md` L45: "**G-ID (physical clause only).** At an admitted complete physical pair the Gaussian part of the actual step has covariance \(\mathsf A(P_W)^{-1}\). SA 14108–14118 sketches this identification; pr-lay (9) retains physical-current and background-branch identities. This is not TP1's different, still imported, Gaussian-energy identification."
- `hm.md` L371: "To consume it as frozen IN1 H-M, the actual construction must use these full-read carriers, and its whole declared local domain must be admitted to the representative class or supplied with a compatible descent theorem. For the physical clause, pr-lay Theorem 8's global regularity and a small \(r(P_W)\) alone do not imply the stronger real-gauge ceiling (10); full membership in the present working domain and G-ID are required."
- `hm.md` L482: "**Status: frozen**, as a conditional theorem on R4 intersect Rep. Outstanding, named: the all-core conclusion (descent; descent.md (frozen)), G-ID for the physical clause, F for the completed gauge form."
- `descent.md` L68: "**G-ID:** only for physical identification in Theorem B, the admitted complete axial physical precision is the Gaussian precision of the step. These are the identifications sketched at SA 10208 and 14108–14120. They are distinct from TP1's Gaussian-energy identification."
- `descent.md` L285: "An application must use these carriers and supply its potentials, normalization and bounds there. Lemma 7 does not establish that every existing NL1/LF1 formation can be switched while retaining UM1 or the required local vacuum assignment. Nor does this note put every ST1 chain domain inside this R4 domain."
- `descent.md` L297: "**Status: frozen**, as a conditional theorem. Outstanding, named: local formation and vacuum bounds."
- `pr-lay.md` L328: "Theorem 8 supplies the precision hypotheses of frozen IN1 Lemma 2. It does not supply IN1's H-M: that includes the actual collared matrices, their enlarged parameter discs, heredity, wall factorization and physical identification."
- `ci-form.md` (distilled, not frozen) L44–52, **H-G**: the actual \(C,\Gamma\) with (3), \(m\le c_m(LM)^4|Z|\), the FG functional, and "frozen IN1 H-M's early envelope \(\varepsilon\le H_0e^{b_G\bar\kappa-d_GM}+\Delta_\gamma,\ \sup_{\theta\ge\gamma^{-2}}\Delta_\gamma\to0\)" (4); L54, **H-S**: "The assigned Gaussian and potential carriers are hereditary, normalized and wall-factorizing, with the actual finite Mayer/cutoff/decoupling identity. … Physical identification is required only on the complete physical locus."
- `td.md` (distilled) L228–235, **J**: imports H-M's matrix, comparison and structural parts "for these **assigned** functionals and supports", and "IN1 Lemma 3's choices must give \(C_0^{\rm UM}\le1\), with an early \(W_0>0\)".

### 1.4 TP1 (frozen `tp1.md`): kept apart

- L130: "Its last equality, called **G-ID**, is also an import: the source-transport formula alone does not prove that these energies have exactly the Gaussian model (2.6)." This is **G-ID(TP)**: an identity between deterministic Gaussian energies \(e_j^G\) and TP1's model (2.6), summed over levels and domains. It is not a statement about one step's fluctuation covariance. Nothing below proves it, and I do not use it.
- L184: "**Outstanding (IN-order):** c4-order.md flags the need for an early uniform UM cost envelope". Frozen IN1 Lemma 3 supplies that envelope conditionally on H-M (assembly-status §4 item 5). Corollary 4.5 below supplies H-M's numerical part for the actual family, so TP1's IN-order item is supplied under the same remaining input (UM1 of the non-gauge types).

The lead decision of FINISH row 278 renames the two in usage: G-ID(TP) for tp1 L130, G-ID(cov) for hm L45 / descent L68. This note proves G-ID(cov) only.

### 1.5 What item 6 must deliver

From §§1.1–1.3, item 6 is exactly:

- **(a)** HM-0: the actual step's localized Gaussian functional and its carriers *are* a family for which HM-1, HM-2, HM-4 hold on the declared domain, and the structural readers (CI-Gauss, H-G, H-S, J) are served by the same family. (hm L371 first clause; descent L285 first sentence.)
- **(b1)** the local formation bound: the potentials formed relative to that Gaussian satisfy UM1 — specifically, the change of gauge form creates no potential that breaks UM1, and the gauge-type potential itself obeys UM1 (descent L285 "retaining UM1"; L297).
- **(b2)** the vacuum bound: the step's Gaussian normalizer has a local assignment with bounds (descent L285 "the required local vacuum assignment"; L297).
- **(c)** HM-3 = G-ID(cov) at admitted complete physical pairs, for the Y3 form on all of R4 (hm L45, L371 second clause; descent L68).

**Design decision D-Y3 (lead, FINISH row 278).** "the actual step uses Y3's relative soft-gauge form (descent Theorem B), which agrees with the absolute form on Rep". In §2.3 I state the precise reading used here and prove that it is the only reading that agrees with SA's \(\mathrm{GF}_k\) at block-axial references and is real-gauge covariant (Lemma 2.1). This does not reopen the decision; it records what the decision means for each formula.

## 2. Setting, imports and the reading of D-Y3

### 2.1 Geometry, fields and domains

Use frozen hm §1 (L11–35) and descent §"Definitions" (L11–58) verbatim, with one notation: \(\eta=\epsilon_{\rm lat}=L^{-k}\). Odd \(L\ge27\) (and \(L>L_0^\natural\), IN1 Amendment 1); depth \(k\); scales \(\xi_j=L^{j-k}\); the fixed separated longer sequence \(\mathbf S=(\Omega_0,\ldots,\Omega_{k+1})\), cut at depth \(k\) for the operators; free space \(I\) of positively stored, non-pivot level-\(k\) bond coordinates touching \(\Omega_{k+1}\), three real colours per bond, \(n_c=12\) coordinates per site; distance \(d(x,y)=|\hat x-\hat y|_\infty\); fine cubes of side \(M\), coarse cubes of side \(\ell=LM\) (these are the level-\((k+1)\) \(M\)-cubes); the corner collar \(H=Z_0^\sharp\); \(\chi=1_{I_0}\).

Triples \(P=(U,A',\mathbf J)\), \(\mathbf U=e^{i\eta A'}U\), pair \(\mathbf p(P)=(\mathbf U,\mathbf J)\), reference \(P_0=(U,0,0)\), level-\(k\) field \(V=\mathcal M^k\mathbf U\). **R4**\((Y;a_0,a_1,j_0)\) is descent (2) (SA 5665–5694): defects \(<a_0\eta^2\) for \(U\) and \(\mathbf U\), \(|A'|,|\nabla^UA'|<a_1\), \(|\mathbf J|<j_0\), and a real box gauge with \(|A|,|\nabla A|<C_{\rm pot}Ma_0\) on every contained box of side \(\le C_{\rm box}LM\). **Rep** is block axiality of the averaged contours \(c_b(\mathcal M^kU;x)=I\) on the active complete-read blocks \(\mathfrak B(Y)\) (descent L35; hm L33–35). \(\mathcal K=\mathrm{R4}\cap\mathrm{Rep}\). Size \(r_Y(P)\) is hm (3).

A real site gauge \(g\) acts by descent (1); \(\mathcal G\) (or \(\mathcal V\)) is its orthogonal action on \(I\), block diagonal by bond (on bond \(b\) it is \(\operatorname{Ad}(g(b_-))\) on the three colours).

### 2.2 The two gauge forms

For a level-\(k\) field \(V\) on AV's branch, descent (3): \(W^V_{b,x}(D)=(e^{iD}V)(y_b,x)\), \(\widehat W^V_{b,x}(D)=W^V_{b,x}(D)W^V_{b,x}(0)^{-1}\), and
\[
 \mathrm{GF}(V)=\sum_{b,x}\bigl[1-\tfrac12\operatorname{tr}V(y_b,x)\bigr],\qquad
 \Phi^{\rm Y}_V(D)=\sum_{b,x}\bigl[1-\tfrac12\operatorname{tr}\widehat W^V_{b,x}(D)\bigr],
 \qquad \mathsf G^{\rm Y}_V=\operatorname{Hess}_{D=0}\Phi^{\rm Y}_V .     \tag{2.1}
\]
\(\mathrm{GF}\) is the holomorphic version of SA 7182 (\(\mathrm{GF}_k(V)=\sum_{y,x}[1-\tfrac12\operatorname{Re}\operatorname{tr}V(y,x)]\); on real fields \(\operatorname{tr}\) of an \(SU(2)\) matrix is real, so the two agree). \(\mathsf G^{\rm Y}_V\) is Y3 31522–31536 (read: "\((B_1,\mathsf G_V^{(2)}B_2)=\sum_{y}\sum_{x\in B(y)\setminus\{y\}}\langle\mathsf b_V(B_1)(y,x),\mathsf b_V(B_2)(y,x)\rangle\)" with \(\mathsf b_V\) the relative derivative), as descent Lemma 2 (L127–149) proves. The absolute Hessian is \(\mathsf G^{\rm abs}_V=\operatorname{Hess}_{D=0}\mathrm{GF}(e^{iD}V)\).

The precisions (descent (4), L52–58): \(\mathsf A^\bullet(P)=X(\mathbf p(P))+\mathsf C_V^{\mathsf T}\mathsf G^\bullet_V\mathsf C_V\), where \(X\) is pr-lay (7) without \(K_{\rm GF}\) (active injection \(\iota\), straightened inverse \((QG_1Q^{\mathsf T})^{-1}-\mathsf a\), and \(-E_{\rm amb}[\iota^{\mathsf T}\mathsf H_1^{\mathsf T}\mathbf J]\)), and \(\mathsf C_V\) is the derivative of the actual pivot graph.

### 2.3 The reading of D-Y3

**Definition D-Y3.** For a step with fixed geometry, at every reference pair \(P\) in the step's declared domain:

1. the step's soft-gauge exponent, as a function of the fluctuation \(D\) of the level-\(k\) field about \(V=\mathcal M^k\mathbf U\), is \(-x\,\Phi^{\rm Y}_V(D)\), with the gauge indicator read relatively, \(\mathbf 1\{|\widehat W^V_{b,x}(D)-I|<\varepsilon_k\}\), and the normalizer \(z_{\mathfrak G}^{-1}\) of SA 7181 unchanged;
2. the step's Gaussian precision is \(\mathsf A^{\rm Y}(P)\);
3. the step's UM local functional is hm (28) built from the tagged matrices of descent Theorem B, (14), with \(D_\tau\) of descent (16).

At a block-axial \(V\), \(\widehat W^V=W^V\), so item 1 is SA's \(\mathfrak G_k\) (SA 7181) and item 2 is SA's precision (SA 14096–14102) with \(\mathrm{GF}^{(2)}_V=\mathsf G^{\rm abs}_V=\mathsf G^{\rm Y}_V\) (descent Lemma 2). SA 11239–11240 says the physical step uses block-axial \(V\): "The physical step chooses \(V=V_k^{\rm bg}=\mathcal M^kU\) in block axial gauge." SA 11245–11247 leaves the off-axial choice open: "An absolute contour gauge and its relative version can have different derivatives away from the axial locus; the formula uses the actual gauge definition of the model being considered." D-Y3 is such a choice. It changes nothing on the physical locus.

**Lemma 2.1 (the relative form is the transported absolute form; uniqueness).** Let \(V\) be a real level-\(k\) field on AV's branch, and let \(u_V\) be the canonical real gauge of descent (9): \(u_V(x)=c_b(V;x)\) for \(x\) in a block \(b\in\mathfrak B\), \(u_V=I\) elsewhere. Then for every \(D\) in AV's ball,
\[
 \Phi^{\rm Y}_V(D)=\mathrm{GF}\bigl(e^{i\mathcal V D}V^{u_V}\bigr),\qquad
 \mathcal V=\mathcal G(u_V),                                          \tag{2.2}
\]
and \(V^{u_V}\) is block axial. Consequently:
(i) the same identity holds at complex \(\mathbf U=e^{i\eta A'}U\) with \(V=\mathcal M^k\mathbf U\), for \(A'\) in the working domain, where both sides are continued holomorphically in \(A'\) at fixed real \(U\), with \(u_V\) the continued (complex) contour gauge;
(ii) (uniqueness) if a family \(\Psi_V(D)\), defined for real \(V\) on AV's branch, satisfies \(\Psi_V(D)=\mathrm{GF}(e^{iD}V)\) whenever \(V\) is block axial on \(\mathfrak B\) and \(\Psi_{V^v}(\mathcal G(v)D)=\Psi_V(D)\) for every real site gauge \(v\), then \(\Psi_V=\Phi^{\rm Y}_V\).

*Proof.* The gauge acts on the exponential chart bondwise: \((e^{iD(b)}V(b))^{u}=u(b_-)e^{iD(b)}V(b)u(b_+)^{-1}=e^{i\operatorname{Ad}(u(b_-))D(b)}\,u(b_-)V(b)u(b_+)^{-1}\), so \((e^{iD}V)^u=e^{i\mathcal G(u)D}V^u\). By descent (10), the averaged contour of a transformed field is \(c_b(V^v;x)=v(y_b)c_b(V;x)v(x)^{-1}\). Apply it to \(e^{iD}V\) and \(v=u_V\), with \(u_V(y_b)=I\) (descent L121: disjoint ownership gives \(u(y_b)=I\)) and \(u_V(x)=c_b(V;x)=W^V_{b,x}(0)\):
\[
 c_b\bigl((e^{iD}V)^{u_V};x\bigr)=W^V_{b,x}(D)\,W^V_{b,x}(0)^{-1}=\widehat W^V_{b,x}(D).
\]
At \(D=0\) this is \(I\), so \(V^{u_V}\) is block axial. Summing \(1-\tfrac12\operatorname{tr}\) over \((b,x)\) gives (2.2).

(i) For real \(A'\) (Hermitian), \(e^{i\eta A'}\) is unitary, so \(\mathbf U\) and \(V\) are real and (2.2) holds. Both sides of (2.2) are holomorphic in \(A'\) at fixed real \(U\) on the working domain: the left by descent Lemma 2 (bounded analytic finite-stencil form on AV's domains); the right because \(u_V(x)=c_b(V;x)\) is a holomorphic function of \(V\) on AV's branch (SA QC1–QC4, 7943–8001, as imported by AV), and the gauge action is polynomial in \(u\) and \(u^{-1}\), with \(u^{-1}\) the adjugate since \(\det u=1\). Two holomorphic functions on a connected open set that agree on its real points (a totally real set of full real dimension) agree everywhere.

(ii) For real \(V\), apply the covariance with \(v=u_V\): \(\Psi_V(D)=\Psi_{V^{u_V}}(\mathcal VD)=\mathrm{GF}(e^{i\mathcal VD}V^{u_V})=\Phi^{\rm Y}_V(D)\), using block axiality of \(V^{u_V}\) and (2.2). \(\square\)

*Status: proved*, under AV and descent (9)–(10). Lemma 2.1(ii) is the positive counterpart of descent Proposition C (L251–273): an assignment that agrees with SA's GF at axial references and is real-gauge covariant must be the relative one. It is why D-Y3 is the covariant continuation of SA's physical step, and not a new model.

### 2.4 Imports

Each import is named, with its source and status. None is proved here.

- **[HM]** frozen `hm.md`: Lemmas 1–4, Theorem 5, Lemma 6, Theorems 7–8, Proposition 9, Corollary 13.1, with its imports R, W, AV, FG/UM (L39–49). Frozen on \(\mathcal K\).
- **[DS]** frozen `descent.md`: Lemmas 1, 2, 4, Theorem 5 (B), Proposition 6 (C), Lemma 7, with its imports R, W, AV, W-cov, PF, FG/UM (L60–68) and its order (5)–(8) (L70–97).
- **[CP]** frozen `cp12.md`: D2 (L23), D3 (L25), the imports for (15) (L27), Lemma 1 (L33–49), Theorem 2 (L51–64), Theorem 7 and its PR1 application (L296–345).
- **[A3]** `a3-derivative.md` §6 (L293–423): the gauge-augmented system (28), its solution \((a(B),\nu(B))\), the differentiated system (32), the exact inverse (27), Lemma 6.1 (node factor along a pure gauge), the chart identity (35), Lemma 6.3 and Proposition 6.4 with (37). Read with the repairs of `gates/a3-derivative-gate.md` §6.1 (L10–32: Lemma 6.2 repaired; one rooted tree per connected component). This is exactly the a3-derivative package that frozen cp12 imports (cp12 L27). It is conditional on P81 and P82.
- **[P81]** the background chart of cp12 D3 (L25): "holomorphic \(\Phi\), \(\Phi(0)=U\), prescribed averages, criticality at real data, and the straightened factorization and local Landau identification of a3-derivative §6.1". Not constructed here (cp12 L25: "This definition does not construct backgrounds or admit actual histories").
- **[P82]** frozen `p82.md` Theorem P82 at the real critical reference.
- **[SA-op]** existence of SA's operator chain (pr-lay (6)) at the pair, as part of W (pr-lay L103: "all inverses in (6)–(7) exist").
- **[PR-BQ]** pr-lay B and Q (L219–238), used only in Lemma 6.10.

SA passages used as **definitions** (not as proofs): 7181–7182 (\(\mathfrak G_k\), \(\mathrm{GF}_k\)); 10139–10195 (operators, \(\lambda_A,\lambda_A^+,\mathsf S\) at 10169–10171, the explicit \(\Delta'_\pi\) at 10172–10185); 10208–10214 (the identification claim); 11214–11247 (PX103–PX104 and the gauge-choice remark); 14091–14120 (the step's precision and Gaussian); 14155–14217 (collared Gaussian); 14276–14560 (UM1–UM16); 17257 (\(\varepsilon_k=g_kp_0(g_k)\), \(\delta_k=(A_1/A_0)\varepsilon_k\)); 17540–17545 (the normalizer and its local terms). Two SA *assertions* that I need — the gauge identity \(\Delta^{\rm W}-\Delta'_\pi[J(\mathbf U)]=\mathsf S^{\mathsf T}\Delta^{\rm W}\mathsf S\) (SA 10189–10194, restated 10301) and \(QD\lambda=\bar DQ'\lambda\) (SA 10300) — are **proved below** in the form used (Lemmas 6.2, 6.3), not imported.

## 3. (a) The step's carriers are hm's full-read carriers

### 3.1 What SA leaves to an assignment

SA does not fix the decoupling expansion of the UM Gaussian. SA 14160–14166: "Only coarse cubes outside the collar \(Z_0^\sharp\) carry parameters. Decouple the precision and its inverse root by their respective expansions, and write \(C(Z_0;s)=(\chi\mathsf A(s)\chi)^{-1}\), \(\Gamma(Z_0;s)=-\chi\mathsf A(s)(1-\chi)\mathsf r(s)\). The symbol \(\mathsf r(s)\) denotes the decoupled inverse-root series; it does not denote \(\mathsf A(s)^{-1/2}\)." SA 14406–14412 then makes the structure an assignment hypothesis: "The remaining structural hypotheses are the actual heredity, normalized-functional and wall-factorization identities. … These hypotheses concern the assigned operators and supports. They are not consequences of a numerical Gaussian bound." So "the actual carriers" of HM-0 are whatever carriers the construction assigns, provided the assignment satisfies HM-1, HM-2, HM-4 and is the one every reader uses. The task in (a) is therefore: fix the assignment, prove that it is well defined from the step's data alone, and check it against every reader.

### 3.2 The assignment

**Definition 3.1 (the step's Gaussian family under D-Y3).** Fix a step: depth \(k\), the longer sequence \(\mathbf S\), blocks, active mask, pivots, regular branches, cutoffs. For \(P\) in \(\mathrm{R4}(Z;a_0,a_1,j_0)\):

1. *Precision labels* \(a^{\rm Y}_\omega(P)\): h-walk's fixed-region labels (h-walk §§3–8, with h-walk-gate §§5–8) in which the gauge label is replaced by the Y form (2.1) — descent Lemma 4 (L184–194). Their **full read hulls** \(H_\omega\) are those of hm Lemma 1 (L53–83): uncut read boxes, actual stencils, endpoints, fixed joining paths, the extra read boxes of the zero-length multiplier \(j^{(0)}\), transpose partners with a common enlarged hull. The Y gauge label of block \(b\) reads the contour family of \(b\), inside the block's averaging-read radius \(r_{\rm av}\) (hm L33), so it adds no read outside the existing hull convention (descent L186: "The new gauge labels have the same finite stencil"). Intermediate colours are grouped (descent L194).
2. *Root labels* \(r^{\rm Y}_\alpha(P)\): hm Theorem 5's grouped series (L183–226) built from the \(a^{\rm Y}_\omega\), with hulls \(H_\alpha\) (unions of radius-\(R_*\) endpoint balls and factor hulls), lengths \(t_\alpha\), and the integrated root (18).
3. *Tags* \(s^H=\prod_{\Delta\cap H\ne\varnothing}s_\Delta\) (hm (19)); the discard-before-evaluation rule (hm L235); the matrices \(C,\Gamma,C_*,\Gamma_*\) of descent (14).
4. *Functional* \(\mathcal J(Z_0;s;P)\): hm (28) with \(D_\tau=\tau^{-1}(C+C\Gamma\Gamma^{\mathsf T}C)\) (descent (16)), on the fixed real space \(\mathbb R^{I_0}\), determinant branch continued from the positive reference.

The **step's Gaussian carriers** are the sets \(H_\omega\) and \(H_\alpha\) of items 1–2.

**Lemma 3.0 (the assignment is determined by the step).** The family of Definition 3.1 is a function of the step's fixed data and the pair \(\mathbf p(P)\) alone: no choice depending on \(P\), on \(Z\), or on the history beyond the step's fixed geometry enters any coefficient, hull, length or tag.

*Proof.* The h-walk formulas are explicit fixed-region formulas (descent L63: "Use h-walk's explicit fixed-region formulas, not an arbitrary expansion having the same sum"). Their cut-down regions, cutoffs and boundary spaces depend only on the fixed geometry (descent L188). The Y gauge label is (2.1), a function of \(V=\mathcal M^k\mathbf U\). By PF-label (descent Lemma 4, L188–192) every coefficient is a function of the pair on its full hull. The grouping constants \(r_c,n,\theta,R_*\) are early numbers (hm (12)–(13)); the grouped entries (hm (15)) are fixed polynomials in the short-label entry sums; the hull and length assignments (hm L196) depend only on endpoints. The tag of a hull depends only on the hull and the fixed coarse grid. The region sequence itself is fixed by the step's outcome record: frozen geoh Lemma 2 (L76): "For fixed frame, grid, selectors, test schedule and complete geometric outcome record, the regions, classes, fates and nests are determined." \(\square\) *Status: proved.*

### 3.3 The identification theorem

**Theorem 3.2 (identification and reader check).** Assume D-Y3, the imports [HM], [DS] (R, W, AV, W-cov, PF, FG/UM), the geometry, descent's order (5)–(7) and all hm (23) floors. Then for every step and every \(P\in\mathrm{R4}(Z;a_0,a_1,j_0)\) with (7):

1. **(HM-1)** On every polydisc \(|s_\Delta|<e^{\bar\kappa}\) the series converge normally, \(C=C^{\mathsf T}\), \(\Gamma\) is rectangular, \(C_*,\Gamma_*\) are real, \(C_*>0\), and
\[
 \|C_*\|+\|C_*^{-1}\|+\|\Gamma_*\|\le K_0,\qquad
 \|\tau^{-1}C-C_*\|+\|\tau^{1/2}\Gamma-\Gamma_*\|\le
 H_0\{e^{32\bar\kappa-dM}+L^3(a_0+a_1+j_0)\}+C_\tau|\tau-1|,
\]
with \(K_0,H_0,C_\tau\) of descent (5), \(b=32\), \(d=\theta/4\), \(H_p\equiv L^3\). These precede \(\kappa\) and are independent of \(M,\bar\kappa\).
2. **(HM-2)** \(\mathcal J[1]=1\); the matrices and \(\mathcal J[F]\) for the admitted integrands are jointly holomorphic in \((A',\mathbf J,s)\) at fixed \(U\); restriction from \(Z'\) to \(Z\subset Z'\) with \(s\) extended by zero changes none of \(C,\Gamma,D,\mathcal J\) (heredity in the declared carriers); wall components missing \(H\) carry no parameter dependence and the rest factor (wall factorization); the finite interpolation identity hm (29) holds.
3. **(HM-4)** \(m=|I_0|\le12(LM)^4\#Z\), so \(c_m=12\).
4. **(PT)** Every coefficient is a function of the pair on its full hull, at every \(s\) (pair tie), and every carrier term is real-gauge covariant after colour grouping: \(C(P^g)=\mathcal G_0C(P)\mathcal G_0^{-1}\), \(\Gamma(P^g)=\mathcal G_0\Gamma(P)\mathcal G_I^{-1}\).
5. **(HM-3)** At every admitted complete physical pair in this domain, \(D(\mathbf 1;P_W)\) at \(\tau=1\) is the \(I_0\)-marginal covariance of the step's Gaussian part (Corollary 6.9, using Theorem 6.6).

Consequently: (i) IN1 H-M (L99–106) holds for this family, on the stated domain, with its literal constant order; (ii) NL1's CI-Gauss (nl1-L L578–580) holds on every CI domain that is contained in \(\mathrm{R4}(Z;a_0,a_1,j_0)\) with (7); (iii) ci-form H-G holds with \(K=K_0\), \(b_G=32\), \(d_G=\theta/4\) and \(\Delta_\gamma=H_0L^3(a_0+a_1+j_0)+C_\tau|\tau-1|\), and H-S's Gaussian half holds; (iv) td J's matrix, comparison and structural parts hold for these assigned functionals; (v) hm L371's first requirement ("the actual construction must use these full-read carriers") holds by D-Y3, and its second ("its whole declared local domain must be admitted to the representative class or supplied with a compatible descent theorem") holds with descent Theorem B as the compatible descent theorem on all of R4.

*Proof.* Items 1–3 are descent Theorem 5 (L196–249), whose proof reduces to hm Theorems 7–8 at the canonical representative \(P^{u}\), \(u=u_Z(U)\) (descent Lemma 1), and transports by the exact conjugation (descent L229–233): operator norms, real parts and accretivity are preserved. Item 4 is descent Lemma 4 (PF-label and covariance after colour grouping) and descent L220. Item 5 is §6.

For the consequences, compare clause by clause.

- IN1 HM-0/HM-1/HM-2/HM-4 are items 1–3 with Definition 3.1 as "the actual localized Gaussian functional and its actual carriers". IN1 requires \(K_0\ge1\): descent (5) has \(K_0=1+4/(3c_L)+W+WU_{\rm root}\ge1\). IN1 allows \(H_p(M)\) to follow \(M\); here it is the constant \(L^3\). HM-5 is an import in both texts. HM-3 is item 5, in the sense fixed in §6.0 (Gaussian part; see §8.3 item 1 on the wording of IN1 L106).
- CI-Gauss asks for "the actual matrices, normalization, heredity, wall factorization and early uniform envelope of frozen IN1 H-M" "on these full complex domains". Items 1–3 give these at every \(P\in\mathrm{R4}(Z)\) with (7). Whether the CI-maps domains lie inside that set is a domain statement and stays with DOM.
- ci-form H-G: (3) is item 1 with \(K=K_0\), \(\varepsilon\) the right side; (4) is the same bound, with \(\Delta_\gamma\to0\) whenever the domain radii \(a_0,a_1,j_0\) and \(|\tau-1|\) tend to zero as \(\theta\to\infty\) at fixed \(M,\bar\kappa\). With IN1's running radii (L28–33) and the tube (3), this holds; the early constants precede \(\kappa\). The dimension bound is item 3. H-S's Gaussian half is item 2; its "physical identification … only on the complete physical locus" is item 5.
- td J imports "the matrix, Gaussian-comparison and structural parts of H-M … for these **assigned** functionals and supports" (td L228). That is items 1–3 with the assignment of Definition 3.1. Its last requirement (\(C_0^{\rm UM}\le1\) with early \(W_0\)) is Corollary 4.5.
- hm L371: as stated. \(\square\)

*Status: proved*, as an implication from [HM], [DS] and D-Y3. The new content beyond descent Theorem B is Lemma 3.0 (the assignment is a function of the step) and the clause-by-clause check.

### 3.4 Other series and other readers

**Remark 3.3 (the series the step does not use).**

1. *IN1 Lemma 2's path-weighted family.* Not the step's family. Its local covariance reads exterior edges (in1 L329–334). Frozen hm Proposition 9 (L377–388): the full-read construction "excludes its mechanism; it does not disprove the example". Nothing in Theorem 3.2 uses Lemma 2.
2. *inv-root's series (carrier-adopt §6).* carrier-adopt L169 adopts inv-root (17) for the UM readers. inv-root uses the global gap (A2) on "a fixed complex regular-pair neighbourhood" (inv-root L27–31; carrier-adopt L145). Frozen hm correction 4 (L495): "Extending them to genuinely local data needs Lemmas 1–4 and the local compression in (16)." The step's UM root is hm Theorem 5's grouped series, which adapts inv-root and uses only local gaps. The two series have the same sum at \(s=\mathbf1\) on the whole torus (both give \(\mathsf A^{-1/2}\)); at \(s\ne\mathbf1\) they differ, and no reader needs them to agree (hm correction 5, L496). So IN1 L108's note "may make this item smaller than stated" is answered: the step's carriers are hm's, not inv-root's.
3. *SA's own walk families.* SA statement 5 (SA 10311–10336) lists walk expansions \(\mathsf O_\omega\) of the six propagators, \(1-R\) and \(C^{(k)}(Y)\), and statement 7 decouples them with parameters on cubes of side \(\ell_{\mathsf P}\) (SA 10212: "The cubes \(\square\) that carry parameters (statement 7) have side \(\ell_{\mathsf P}\)"; SA 10552). Those parameters are not the UM coarse parameters of side \(LM\). They feed DR (drlocp, dr-draft), not the UM functional. SA 10335 asserts that each \(\mathsf O_\omega\) "is gauge covariant and real at real pairs". Under D-Y3 this holds for the precision labels after colour grouping (descent Lemma 4); descent L194 notes that a single fixed-colour product need not be covariant.

**Remark 3.4 (readers of the precision outside UM).**

1. *DR.* dr-draft Lemma 2.1 (L112, unrefereed): "None of the maps in Definition DR♮ reads \(\mathsf G^{\rm abs}_V\) or \(\mathsf G^{\rm Y}_V\)". So D-Y3 does not touch DR.
2. *Kept forms (carrier-adopt Definition D, SA 17556–17560).* The stored conditional form is a Schur complement of the step's precision; under D-Y3 it reads \(\mathsf A^{\rm Y}\). carrier-adopt's results are implications from (A2) and (HW) (carrier-adopt L162, L188). (HW) for the Y labels is supplied by descent Lemma 4 ("This supplies exactly the gauge part of W's (I3)", L186). (A2) for \(\mathsf A^{\rm Y}\) at complete pairs: hm Lemma 4's whole-torus clause (L152: "For a whole-torus support use R directly") gives \(\operatorname{Re}\mathsf A^{\rm Y}\ge5c_L/8\) at Rep pairs with \(r<r_{\rm loc}\), and the conjugation of descent L229–233 gives it at every R4 pair; \(\|\mathsf A^{\rm Y}\|\le W\) by (4). So (A2) holds with \(a=5c_L/8\), \(b=W\) instead of carrier-adopt's \(3c_L/4\). The transfer of carrier-adopt Theorem A is a re-reading with these two constants. I have not re-read carrier-adopt Theorem A line by line. *Status: transfer argued, not checked; this is not one of item 6's consumer clauses.* It is listed for the lead in §8.2.
3. *Tests.* Under D-Y3 the gauge indicator is relative. At the step's block-axial representative it equals SA's indicator (SA 7181) exactly, since \(\widehat W=W\) there. Every test that reads only the soft-gauge factor at the step's axial representative is therefore unchanged, so geoh's outcome record (geoh L76–80) is unchanged for those tests. I have not enumerated every test of the history; a test that reads the soft-gauge factor at a non-axial real reference would have to be checked separately. *Status: proved for tests at the axial representative; scope stated.*

## 4. (b1) The local formation bound under D-Y3

### 4.1 Fluctuation coordinates and the box

At a reference \(P\) with \(V=\mathcal M^k\mathbf U\), the fluctuation of the level-\(k\) field on the fibre of the next plain average is \(V(u)=e^{iC_V(u)}V\), where \(u\in\mathbb C^I\) are the free (non-pivot) coordinates and \(C_V(u)\) is the actual pivot graph: its non-pivot part is \(u\), and its pivot part solves the plain one-step constraint \(q_V(C_V(u))=0\), \(q_V(B)=i^{-1}\operatorname{Log}(\mathcal M(e^{iB}V)\mathcal M(V)^{-1})\) (pr-lay (8)). Its derivative at zero is \(\mathsf C_V\). The step's weights carry the coupling \(x\) (SA 7181: \(e^{-x_k(1-\frac12\operatorname{Re}\operatorname{tr}V(y,x))}\)); the normalized variable is \(b=x^{1/2}u\), in which the Gaussian part has precision \(\mathsf A^{\rm Y}\) at \(\tau=1\).

The fluctuation box is SA's (SA 17257: "the fluctuation fields stay below \(\delta_k=(A_1/A_0)\varepsilon_k\)", with \(\varepsilon_k=g_kp_0(g_k)\)), in IN1's notation (2): \(|u(\beta)|<\delta_j=A_1g_j(\log\theta_j)^{p_0}\) on every free bond \(\beta\) that a selected potential reads; in normalized form \(|b(\beta)|<\mathfrak b_j:=\delta_j/g_j=A_1(\log\theta_j)^{p_0}\). IN1 L366: "the scaled box \(\mathfrak b\) grows proportionally to \((\log\theta)^{p_0}\)". Here \(g_j=x_j^{-1/2}\) up to the tube factor, which I suppress (it changes constants by at most \(2\), by IN1 (3)).

**Import (PIV)** (part of AV/W: hm L42 "bounded analytic finite-stencil one-step maps"; pr-lay L95). There are early \(\rho_{\rm piv}>0\), \(C_{\rm piv}\ge1\) and \(r_{\rm piv}\) such that, at every pair of the domain, \(u\mapsto C_V(u)\) is holomorphic on \(|u|_\infty<\rho_{\rm piv}\), \(|C_V(u)|_\infty\le C_{\rm piv}|u|_\infty\), each pivot coordinate reads only free coordinates within \(r_{\rm piv}\) of its coarse bond, and \(C_V\) is real-gauge covariant (descent L65: "the covariance of \(\mathsf C_V\) follows directly from Lemma 1's equation (10)").

**AV bounds** (descent Lemma 2's proof, L144–149, with change-log item 5, L294). There are early \(\rho_{\rm AV}>0\), \(G_{\rm AV}\ge1\) such that \(|W^V_{b,x}(D)|\le G_{\rm AV}\) when \(|D|_\infty<\rho_{\rm AV}\) on the contour stencil of \((b,x)\); and \(|W(0)^{-1}|=|W(0)|\) because \(\det W(0)=1\). Since \(\widehat W^{V^v}=v(y_b)\widehat W^Vv(y_b)^{-1}\) (descent L146) and the operator norm is unitarily invariant, the bound \(|\widehat W^V_{b,x}(D)|\le G_{\rm AV}^2\) holds in every real gauge.

Put \(\rho'=\min(\rho_{\rm piv},\rho_{\rm AV}/C_{\rm piv})\). For \((b,x)\), let \(\mathrm{st}(b,x)\) be the free bonds read by \(D\mapsto\widehat W^V_{b,x}(C_V(u))\): the contour family of \(b\) enlarged by \(r_{\rm piv}\). Its diameter is at most \(2L+2r_{\rm piv}\). Let \(N_{\rm st}=\max\#\mathrm{st}(b,x)\) and \(N_{\rm ov}=\max_\beta\#\{(b,x):\beta\in\mathrm{st}(b,x)\}\); both depend on \(L\) and \(r_{\rm piv}\) only.

### 4.2 No completed-form correction

**Lemma 4.1 (zero gauge gradient; F is vacuous under D-Y3).** For every \(V\) on AV's branch (real or complex, axial or not), \(J^{\rm Y}_{\rm GF}(V):=\nabla_D\Phi^{\rm Y}_V(D)|_{D=0}=0\), and each summand \(1-\tfrac12\operatorname{tr}\widehat W^V_{b,x}\) has zero gradient. Consequently pr-lay's completed form (9), \(A_{\rm full}=A-E_{\rm free}[J_{\rm GF}]\), equals (7) for the Y form, and hm's optional import F (hm L47) is not needed. Also the Hessian of \(u\mapsto\Phi^{\rm Y}_V(C_V(u))\) at \(0\) is exactly \(\mathsf C_V^{\mathsf T}\mathsf G^{\rm Y}_V\mathsf C_V\), with no pivot-curvature term.

*Proof.* \(\widehat W(tD)\in SL(2,\mathbb C)\) and \(\widehat W(0)=I\), so on the branch \(\widehat W(tD)=\exp(iH(t))\) with \(H\) holomorphic, \(H(0)=0\), \(\operatorname{tr}H(t)=0\). Then \(\frac d{dt}[1-\tfrac12\operatorname{tr}e^{iH(t)}]_{t=0}=-\tfrac i2\operatorname{tr}H'(0)=0\). This is descent Lemma 2's "Its gradient at zero vanishes" (L131), termwise. The chain rule gives \(\operatorname{Hess}_u[\Phi^{\rm Y}_V\circ C_V](0)=\mathsf C_V^{\mathsf T}\mathsf G^{\rm Y}_V\mathsf C_V+\langle\nabla\Phi^{\rm Y}_V(0),C_V''(0)[\cdot,\cdot]\rangle=\mathsf C_V^{\mathsf T}\mathsf G^{\rm Y}_V\mathsf C_V\). With \(J_{\rm GF}=0\), \(E_{\rm free}[J_{\rm GF}]=0\) by linearity of \(E_{\rm free}\) in its argument (pr-lay (8)). \(\square\) *Status: proved.*

For the absolute form \(J^{\rm abs}_{\rm GF}(V)\ne0\) at non-axial \(V\) in general, which is why pr-lay and hm carry F (pr-lay L114). Under D-Y3 that bookkeeping disappears.

### 4.3 The gauge indicator on the box

**Lemma 4.2.** Suppose \(\delta_j\le\rho'/2\) and \(A_0>2(1+G_{\rm AV}^2)A_1/\rho'\). At every pair of the domain and every \(u\) in the box on \(\mathrm{st}(b,x)\), \(|\widehat W^V_{b,x}(C_V(u))-I|<\varepsilon_j\). So the relative gauge indicator of D-Y3 equals \(1\) on the box, and the step's integrand there is the same with or without it.

*Proof.* \(h(u)=\widehat W^V_{b,x}(C_V(u))-I\) is holomorphic on \(|u|_{\mathrm{st},\infty}<\rho'\), bounded by \(1+G_{\rm AV}^2\), and \(h(0)=0\). Schwarz's lemma on the complex line through \(u\) (as in the proof of Theorem 4.3) gives \(|h(u)|\le(1+G_{\rm AV}^2)|u|_\infty/\rho'\le(1+G_{\rm AV}^2)\delta_j/\rho'\). Since \(\delta_j/\varepsilon_j=A_1/A_0\), this is \(<\varepsilon_j/2\). \(\square\) *Status: proved*, assuming the gauge indicator's threshold is SA's \(\varepsilon_k\) of SA 17257; if it is \(c\varepsilon_k\), replace \(A_0\) by \(cA_0\). The condition is a floor on \(A_0\) after \(A_1\), allowed by IN1 row 6 ("Choose \(A_1\), then \(A_0\)") and by SA 17386 ("The ratio \(\delta_k/\varepsilon_k=A_1/A_0\) is small").

### 4.4 UM1 for the gauge-type potential

**Definition.** Write the step's soft-gauge exponent as Gaussian part plus potential:
\[
 -x\,\Phi^{\rm Y}_V(C_V(u))=-\tfrac x2\langle\mathsf C_Vu,\mathsf G^{\rm Y}_V\mathsf C_Vu\rangle+V_{\rm GF}(u),\qquad
 V_{\rm GF}(u)=-x\sum_{(b,x)}f_{b,x}(u),
\]
\[
 f_{b,x}(u)=\bigl[1-\tfrac12\operatorname{tr}\widehat W^V_{b,x}(C_V(u))\bigr]
             -\tfrac12\langle\mathsf b_V(\mathsf C_Vu)_{b,x},\mathsf b_V(\mathsf C_Vu)_{b,x}\rangle .   \tag{4.1}
\]
The quadratic term of (4.1) is the \((b,x)\) summand of \(\mathsf G^{\rm Y}_V\) (descent (3), L46–49), so (4.1) and Lemma 4.1 give \(f_{b,x}(0)=0\), \(\nabla f_{b,x}(0)=0\), \(\operatorname{Hess}f_{b,x}(0)=0\). For each \((b,x)\) let \(Y_{b,x}\) be the union of the fine \(M\)-cubes that meet \(\mathrm{st}(b,x)\), and put
\[
 V_{\rm GF}(Y;P,b)=-x\sum_{(b,x):\,Y_{b,x}=Y}f_{b,x}(x^{-1/2}b).                        \tag{4.2}
\]

**Theorem 4.3 (local formation bound for the gauge type).** Assume (PIV), the AV bounds, \(M\ge2L+2r_{\rm piv}+2\), and the coupling ceiling \(\delta_j\le\rho'/2\). Put
\[
 F_*=1+G_{\rm AV}^2+\tfrac12N_{\rm st}C_{\rm piv}^2\rho'^2\,G_{\mathsf b},\qquad
 a_{\rm GF}(\theta_j)=e^{32\lambda_V}F_*\rho'^{-3}N_{\rm ov}M^4\,\delta_j,                 \tag{4.3}
\]
where \(G_{\mathsf b}\) bounds the \((b,x)\) summand of \(\mathsf G^{\rm Y}_V\) (descent Lemma 2: early). Then the potentials (4.2) are a single tagged potential type with:

1. each \(Y\) a corner-connected union of at most \(16\) fine cubes, \(d_f(Y)\le32\);
2. on the box, \(|V_{\rm GF}(Y;P,b)|\le a_{\rm GF}\,e^{-\lambda_Vd_f(Y)}\bigl(1+M^{-4}\sum_{\beta\subset Y}|b(\beta)|^2\bigr)\), which is UM1 (SA 14303–14318) with \(a_Y\le a_{\rm GF}\);
3. \(V_{\rm GF}(Y;\cdot)\) is holomorphic in \(b\) on the complex box and in \((A',\mathbf J)\) at fixed \(U\) (it does not read \(\mathbf J\)), real at real data, and real-gauge covariant: \(V_{\rm GF}(Y;P^g,\mathcal G b)=V_{\rm GF}(Y;P,b)\);
4. \(\sup_{\theta\ge\gamma^{-2}}a_{\rm GF}\to0\) as \(\gamma\downarrow0\), at fixed \(M\); \(a_{\rm GF}\le W_0/4\) is a coupling ceiling of IN1 row 9.

*Proof.* (1) \(\mathrm{st}(b,x)\) has diameter \(\le2L+2r_{\rm piv}<M\), so it meets at most two grid intervals per coordinate, hence at most \(2^4=16\) fine cubes, which are corner-connected; a tree through their common corner region has fine-cube length at most \(32\) (crude). (2) Fix \((b,x)\) and \(u\ne0\) in the box; put \(\nu=|u|_{\mathrm{st},\infty}\le\delta_j\le\rho'/2\). The function \(g(t)=f_{b,x}(tu/\nu)\) is holomorphic for \(|t|<\rho'\), because \(|tu/\nu|_\infty<\rho'\le\rho_{\rm piv}\) and \(|C_V(tu/\nu)|_\infty<C_{\rm piv}\rho'\le\rho_{\rm AV}\). There \(|g|\le F_*\): the first bracket of (4.1) is at most \(1+G_{\rm AV}^2\), and the quadratic term at most \(\tfrac12G_{\mathsf b}|\mathsf C_Vu|^2_{\rm st}\le\tfrac12G_{\mathsf b}N_{\rm st}C_{\rm piv}^2\rho'^2\). Since \(g\) vanishes to order three at \(0\), \(g(t)/t^3\) is holomorphic, and the maximum principle on \(|t|=r\uparrow\rho'\) gives \(|g(t)|\le F_*(|t|/\rho')^3\). At \(t=\nu\): \(|f_{b,x}(u)|\le F_*\rho'^{-3}\nu^3\le F_*\rho'^{-3}\delta_j\nu^2\). Multiply by \(x\) and use \(x\nu^2=|b|^2_{\mathrm{st},\infty}\le\sum_{\beta\in\mathrm{st}(b,x)}|b(\beta)|^2\):
\[
 |x f_{b,x}(x^{-1/2}b)|\le F_*\rho'^{-3}\delta_j\sum_{\beta\in\mathrm{st}(b,x)}|b(\beta)|^2 .
\]
Sum over the \((b,x)\) with \(Y_{b,x}=Y\); each \(\beta\subset Y\) occurs at most \(N_{\rm ov}\) times. So \(|V_{\rm GF}(Y)|\le F_*\rho'^{-3}N_{\rm ov}\delta_jM^4\cdot M^{-4}\sum_{\beta\subset Y}|b(\beta)|^2\), and \(e^{\lambda_Vd_f(Y)}\le e^{32\lambda_V}\) gives (2). (3) Holomorphy: each \(f_{b,x}\) is a composition of holomorphic maps (AV branch, (PIV)); \(V=\mathcal M^k(e^{i\eta A'}U)\) is holomorphic in \(A'\). Reality: at real data every map commutes with complex conjugation of the real coordinates. Covariance: \(C_{V^g}(\mathcal Gu)=\mathcal G C_V(u)\) by (PIV), and \(\widehat W^{V^g}_{b,x}(\mathcal GD)=g(y_b)\widehat W^V_{b,x}(D)g(y_b)^{-1}\) (descent L146), so each bracket of (4.1) is invariant; the quadratic term is invariant by descent (11). The box is a fixed real set of \(b\), invariant under the orthogonal \(\mathcal G\). (4) \(\delta_j=A_1g_j(\log\theta_j)^{p_0}\to0\) as \(\theta_j\to\infty\); all other factors in (4.3) are fixed once \(M\) is. \(\square\)

*Status: proved*, as an implication from (PIV), the AV bounds and descent Lemma 2. Every constant in \(F_*,\rho',N_{\rm st},N_{\rm ov}\) is early (depends on \(L\) and the branch data); \(\lambda_V\) is UM's rate; \(M^4\) and \(\delta_j\) are explicit. The bound is a radius/coupling ceiling after \(M\), the form that descent-draft's IF-pot (descent-draft L362–366) anticipated for the switch term, with the correct sign and no switch.

### 4.5 No other potential type changes, and no switch is made

**Lemma 4.4.** Under D-Y3, on \(\mathcal K\) compared with the absolute reading, and on all of R4:

1. the non-gauge precision \(X(\mathbf p(P))\) is the same function (descent L58: "\(X\) is exactly pr-lay (7) without \(K_{\rm GF}\)");
2. every factor of the step's integrand other than the soft-gauge factor — the Wilson part through \(U_k\), Haar and chart Jacobians, the delta-elimination factors \(z^{(j)}\), older activities, profile and coupling differences, boundary terms, insertions — does not read the soft-gauge functional, so it is the same function;
3. hence every potential type other than the gauge type, formed as (exponent) minus (its part of the Gaussian, read from \(X\)), is the same function under both readings; the gauge type is \(V_{\rm GF}\) of (4.2) under D-Y3.

*Proof.* (1) is descent (4). (2) is by inspection of the factor list in SA 17520–17545 and pr-lay (6)–(7): none of them contains \(\mathrm{GF}\) or \(\mathfrak G_k\). (3) follows from (1)–(2) and the definition of each type as exponent minus its Gaussian share. \(\square\) *Status: proved* (the inspection in (2) covers the factors displayed in SA 17520–17545; a factor not displayed there is not covered).

So the "switch" of descent L285 ("that every existing NL1/LF1 formation can be switched while retaining UM1") reduces to the gauge type, which Theorem 4.3 bounds. Descent Lemma 7's measure-level switch (18), with its marginal determinant ratio, is **not used**: under D-Y3 the step is formed once, relative to \(\mathsf A^{\rm Y}\) on the full fluctuation space, and UM's local functionals are marginals of that one Gaussian. The obstruction noted in descent Lemma 7 ("finite stencil of the full-precision difference does not prove locality of this correction or of its determinant", L283) therefore does not arise.

### 4.6 The UM cost

**Corollary 4.5 (UM4–UM6, UM14, the cost, and the actual-gas term bound).** Assume Theorem 3.2's hypotheses, descent (8), Theorem 4.3 with \(a_{\rm GF}\le W_0/4\), and

> **(UM1-rest)** the potential types other than the gauge type are holomorphic on their declared boxes and cores and satisfy UM1 with total norm \(a_{\rm rest}\le W_0/4\), with the structural interface of ci-form H-S.

Then UM4–UM6 hold with \(K=K_0\), \(R_s=e^{\bar\kappa}>2\), \(c_m=12\), UM14 holds, and \(C_0^{\rm UM}\le1\), with \(W_0\) and the bound one fixed before \(\kappa\) (descent (6)). The total potential norm is \(a\le W_0/2\), so SA's UM12–UM16 (SA 14485–14560) give the term bound UM16 for the actual gas with \(C_0\le1\).

*Proof.* UM4–UM6, UM14 and \(C_0^{\rm UM}\le1\) are descent Theorem 5's last paragraph (L243–249) and hm Corollary 13.1, which do not read \(a\): \(C_0^{\rm UM}=P_dL^4W_0(1+Ac_m)+D_0M^4(\varepsilon+\gamma_{\rm tilt}/2)\) (hm (35)). UM12 requires "\(a\le W_0/2\), so every radius exceeds one" (SA 14496); \(a=a_{\rm GF}+a_{\rm rest}\le W_0/2\). The rest is SA 14497–14560 verbatim, using UM1, UM4–UM6, UM9–UM14. \(\square\)

*Status:* proved given (UM1-rest). **(UM1-rest) is not an item-6 statement**: it is the regular-gas formation of NL1/LF1, item 8 (ci-form H-C, H-W, TD, H-F; nl1-L Theorem 7 CI-form). With it, the row-274 claim "UM4–UM6 and UM14 at every declared complex pair with \(C_0^{\rm UM}\le1\) fixed before \(M\)" holds for the actual family on every pair of \(\mathrm{R4}(Z)\) with (7)–(8). Whether the declared pairs lie in that set is DOM.

## 5. (b2) The vacuum bound

### 5.1 What the vacuum is here

The step integrates the free coordinates against its Gaussian part. In normalized coordinates, for an integrand \(G\),
\[
 \int_{\mathbb R^I}e^{-\frac12b^{\mathsf T}\mathsf A^{\rm Y}(P)b}\,G(b)\,db
 =(2\pi)^{|I|/2}\bigl(\det\mathsf A^{\rm Y}(P)\bigr)^{-1/2}\,
   \mathcal J_{\rm glob}[G],                                              \tag{5.1}
\]
where \(\mathcal J_{\rm glob}\) is the normalized Gaussian on all of \(I\). UM expands \(\mathcal J_{\rm glob}[F_\iota]=\mathcal J(Z_0;\mathbf1)[F_\iota]\) (the marginal) into \(\sum_ZT(Z,\iota)\) (hm (29)), and every local functional is normalized (\(\mathcal J[1]=1\), hm Theorem 8.1). So the only normalizer of the step's Gaussian part is the global factor \((2\pi)^{|I|/2}(\det\mathsf A^{\rm Y})^{-1/2}\), and the change \(u\to b\) adds the number \(x^{-|I|/2}\). SA puts this factor into the effective action as local terms: SA 17541–17545, "The Gaussian normaliser is contained in the last part; it is that part of \(E^{(j+1)}\) which carries \(b^0_{j+1}\). On a label it is a determinant … so by definition it is non-local. It is converted into local terms, \(\sum_c\log z^{(j)}(c)-\tfrac12\log\det(\mathsf C^{\mathsf T}\Delta^{(j)}\mathsf C|_{\Lambda_{j+1}})=\text{number}+\sum_X\mathbf N(X,U_{j+1})\), \(|\mathbf N(X)|\le Ce^{-cMd_{j+1}(X)}\)". The \(z^{(j)}\) factors are delta-elimination Jacobians, finite-stencil and gauge-independent (Lemma 4.4(2)); they are not item 6's. The **vacuum bound** of descent L285/L297 is the local assignment of \(-\tfrac12\log\det\mathsf A^{\rm Y}\) with bounds, at every pair of the declared domain, for the Y family. SA does this "by sums with alternating signs, taken over the sub-regions \(Y\subset X\)" (SA 17545); I use instead the integrated resolvent of hm Theorem 5, which is already local, has an early majorant, and is defined at local pairs.

### 5.2 Two finite-dimensional identities

**Lemma 5.1.** (i) For \(\operatorname{Re}z>0\), \(\operatorname{Log}z=\int_0^\infty[(1+t)^{-1}-(z+t)^{-1}]\,dt\), with the principal branch. (ii) Let \(A\) be an \(m\times m\) complex matrix with \(\operatorname{Re}\langle v,Av\rangle\ge a|v|^2\), \(a>0\). Then every eigenvalue \(\lambda_i\) has \(\operatorname{Re}\lambda_i\ge a\), \(\operatorname{tr}(A+t)^{-1}=\sum_i(\lambda_i+t)^{-1}\) for \(t\ge0\), and
\[
 \sum_x\int_0^\infty\bigl[(1+t)^{-1}-((A+t)^{-1})_{xx}\bigr]dt=\sum_i\operatorname{Log}\lambda_i,
 \qquad \exp\Bigl(\sum_i\operatorname{Log}\lambda_i\Bigr)=\det A .            \tag{5.2}
\]
(iii) If \(A(z)\) is such a matrix for every \(z\) in a connected set, continuous in \(z\), and real symmetric positive at one point, then \(\ell(z):=\sum_i\operatorname{Log}\lambda_i(z)\) is continuous, is a logarithm of \(\det A(z)\), and equals the real \(\log\det\) at that point. It is the branch of \(\log\det\) continued from the positive reference.

*Proof.* (i) For real \(z>0\), \(\int_0^T[(1+t)^{-1}-(z+t)^{-1}]dt=\log(1+T)-\log(z+T)+\log z\to\log z\). For \(\operatorname{Re}z\ge c>0\) the integrand is bounded by \(|z-1|/[(1+t)(c+t)]\), integrable uniformly on compact sets; so the integral is holomorphic in \(z\) on the right half-plane and equals \(\operatorname{Log}z\) by the identity theorem. (ii) If \(Av=\lambda v\), \(|v|=1\), then \(\operatorname{Re}\lambda=\operatorname{Re}\langle v,Av\rangle\ge a\). By Schur triangularization \(A=QTQ^*\) with \(T\) upper triangular, \((A+t)^{-1}=Q(T+t)^{-1}Q^*\), and \((T+t)^{-1}\) is triangular with diagonal \((\lambda_i+t)^{-1}\); the trace is unitarily invariant. Sum (i) over \(i\); Tonelli/Fubini for the finite sum is trivial. The exponential of a sum of logarithms is the product \(\prod\lambda_i=\det A\). (iii) The eigenvalues, as an unordered list, depend continuously on \(A\); \(\operatorname{Log}\) is continuous on the right half-plane, which contains every \(\lambda_i(z)\); a symmetric function of a continuous unordered list is continuous. At the real positive point each \(\operatorname{Log}\lambda_i\) is the real logarithm. \(\square\) *Status: proved.* (Both identities are standard finite-dimensional facts, written out so that the Lean statement is clear.)

### 5.3 The local vacuum terms

Work at a pair \(P\in\mathrm{R4}(Y)\) with (7), at fixed \(U\). Use hm Theorem 5's construction (L183–226) with the Y labels (descent Lemma 4): short labels \(t_\omega\le r_c\), long family \(E\), grouped entries \(N_t,P_t,Q_t\) of hm (15), \(K_t\) = the labelled union of \(Q_t\) entries and products \(-EP_t\), and \(\mathcal R(t)=P_t\sum_{m\ge0}K_t^m\) as a labelled series with intermediate coordinates kept. Work with **bond blocks**: an entry \((x,y)\) is the \(3\times3\) colour block between bonds \(x,y\), normed by the operator norm; the scalar-to-block conversion costs a factor \(c_b\le3\) once (descent L194). The leading term of \(\mathcal R(t)\) is the \(j=0,m=0\) term \((\Lambda_{\rm res}+t)^{-1}I\). For a bond \(x\), let \(\mathfrak A(x)\) be the set of **non-leading** labelled terms \(\alpha\) of \(\mathcal R(t)\) from \(x\) to \(x\), colour-grouped at intermediate coordinates. Each has a full hull \(H_\alpha\ni x\), connected, within \(R_*\) of a tree of length \(t_\alpha\) through \(x\) (hm Theorem 5). Define
\[
 n_\alpha(P)=\int_0^\infty\mathcal R_\alpha(t;P)_{xx}\,dt\quad(3\times3),\qquad
 X(H)=\bigcup\{\Delta\ \text{coarse}:\Delta\cap H\ne\varnothing\},
\]
\[
 \mathbf N(X;P)=\tfrac12\sum_{x}\ \sum_{\alpha\in\mathfrak A(x):\,X(H_\alpha)=X}\operatorname{tr}_x n_\alpha(P),     \tag{5.3}
\]
where \(\operatorname{tr}_x\) is the trace over the three colours of bond \(x\). Coarse cubes have side \(LM\) in level-\(k\) units; they are the level-\((k+1)\) \(M\)-cubes on which \(E^{(k+1)}\) lives.

**Theorem 5.2 (local vacuum decomposition).** Assume the imports of descent Theorem B and hm's choices through (13). Then:

- **(V1) identity.** At every complete pair \(P\in\mathrm{R4}(\mathbb T;a_0,a_1,j_0)\) with (7),
\[
 -\tfrac12\log\det\mathsf A^{\rm Y}(P)=-\tfrac12|I|\log\Lambda_{\rm res}+\sum_X\mathbf N(X;P),       \tag{5.4}
\]
the sum converging absolutely, with \(\log\det\) the branch of Lemma 5.1(iii) continued along \(z\mapsto P_z=(U,zA',z\mathbf J)\), \(z\in[0,1]\), from the real positive reference \(P_0\).
- **(V2) locality and heredity.** \(\mathbf N(X;P)\) depends only on the pair \(\mathbf p(P)\) on the union of the hulls filed at \(X\), which lies in \(X\); it is the same function for every domain \(Y\supset X\) on which \(P\) is admitted; it is defined at local (non-complete) pairs.
- **(V3) analytic structure.** \(\mathbf N(X;\cdot)\) is holomorphic in \((A',\mathbf J)\) on the open working domain at fixed \(U\), real at real data, and real-gauge invariant: \(\mathbf N(X;P^g)=\mathbf N(X;P)\).
- **(V4) rooted bounds (early).** For every bond \(x\),
\[
 \sum_{\alpha\in\mathfrak A(x)}e^{\theta t_\alpha}|n_\alpha(P)|\le2c_bp_{r_c},\qquad
 \sum_{\alpha\in\mathfrak A(x)}e^{\theta t_\alpha}|n_\alpha(P)-n_\alpha(P_0)|\le4c_bp_{r_c}\frac{r_Y(P)}{r_{\rm loc}}
 \quad(r_Y(P)\le r_{\rm loc}/2).                                           \tag{5.5}
\]
- **(V5) polymer bound.** Put \(C_{\rm hull}=2(2R_*+3)^4\). If \(LM\ge\max(4\kappa C_{\rm hull}/\theta,\,8/\theta)\), then for every coarse cube \(\Delta\),
\[
 \sum_{X\ni\Delta}e^{\kappa d_{k+1}(X)}|\mathbf N(X;P)|\le C_{\rm vac}(LM)^4,\qquad
 C_{\rm vac}=48\,n_c\,c_bp_{r_c}\,e^{1/4+\theta R_*/2},                       \tag{5.6}
\]
and the same with \(|\mathbf N(X;P)-\mathbf N(X;P_0)|\) on the left and an extra factor \(2r_Y(P)/r_{\rm loc}\) on the right. Here \(\theta\le1/2\) without loss: replace \(\theta\) by \(\min(\theta,1/2)\) in (5.5)–(5.6); every \(\theta\)-moment bound survives a smaller rate.
- **(V6) physical value.** At an admitted complete physical pair (Theorem 6.6), (5.4) is \(-\tfrac12\log\det\) of the step's Gaussian precision, so (5.1) with (5.4) is exactly the step's Gaussian normalizer in local form; on \(\mathcal K\) at block-axial \(V\) it equals the absolute-form normalizer.

*Proof.* **Bounds on the series.** By hm (16) on the local compression (which uses only hulls in \(Y\) and the \(b_{\rm gap}\) margin, hm L198–208), \(|N_t^j(x,y)|\le(q_*\Lambda_{\rm res}/(\Lambda_{\rm res}+t))^j\mathbf 1_{\{d(x,y)\le jr_c\}}\). At non-Rep \(P\) the same holds: the compression's accretivity and norm are invariant under the conjugation of descent L229–233, and (16) uses only those operator bounds; in bond blocks the entry bound is unchanged. Then, as in hm (17), with \(\Lambda=\Lambda_{\rm res}\),
\[
 |P_t-(\Lambda+t)^{-1}I|_\theta\le\frac{c_b}{\Lambda+t}\sum_{j=1}^{n-1}16n_cr_c^4(j+1)^4q_*^{j/2}\Bigl(\frac\Lambda{\Lambda+t}\Bigr)^j
   \le\frac{c_bp_{r_c}\Lambda}{(\Lambda+t)^2},
\]
using \((\Lambda/(\Lambda+t))^j\le\Lambda/(\Lambda+t)\) for \(j\ge1\). Also \(|Q_t|_\theta\le\frac14(\Lambda/(\Lambda+t))^n\le\frac14\Lambda/(\Lambda+t)\) by the choice of \(n\) in hm (12)–(13), and \(|EP_t|_\theta\le We^{-\mu_Wr_c/2}p_{r_c}/(\Lambda+t)\le\frac14\Lambda/(\Lambda+t)\) by hm's choice of \(r_c\) (\(We^{-\mu_Wr_c/2}p_{r_c}/\Lambda\le1/4\)). So \(|K_t|_\theta\le\frac12\Lambda/(\Lambda+t)\le\frac12\), and \(\sum_{m\ge1}|K_t^m|_\theta\le\Lambda/(\Lambda+t)\) by submultiplicativity (hm L158). With \(|P_t|_\theta\le p_{r_c}/(\Lambda+t)\) (hm (17)), the non-leading part of \(\mathcal R(t)\) has
\[
 |\mathcal R(t)-(\Lambda+t)^{-1}I|_\theta\le\frac{2c_bp_{r_c}\Lambda}{(\Lambda+t)^2},\qquad
 \int_0^\infty\frac{2c_bp_{r_c}\Lambda}{(\Lambda+t)^2}dt=2c_bp_{r_c}.
\]
The diagonal row sum at \(x\) is at most the Schur norm, and Tonelli gives the first half of (5.5). Every bound is a field-independent majorant of each term, so the series converge normally on the working domain.

**(V4) second half.** On the line \(P_z\), \(|z|<r_{\rm loc}/r\), every term is holomorphic (hm L224) and bounded by the same majorant. Schwarz's lemma applied termwise to \([n_\alpha(P_z)-n_\alpha(P_0)]/(2\,\mathrm{majorant})\) at \(z=1\le\frac12\cdot r_{\rm loc}/r\) gives the factor \(2r/r_{\rm loc}\), exactly as hm (14).

**(V1).** On the whole torus, hm L226: \((\mathsf A+t)P_t=I-Q_t+EP_t=I-K_t\), so \(\mathcal R(t)=(\mathsf A+t)^{-1}\) for every \(t\ge0\), with \(\mathsf A=\mathsf A^{\rm Y}(P)\). Hence \(((\mathsf A+t)^{-1})_{xx}=(\Lambda+t)^{-1}I_3+\sum_{\alpha\in\mathfrak A(x)}\mathcal R_\alpha(t)_{xx}\) blockwise. By Lemma 5.1(i) termwise, \(\int_0^\infty[(1+t)^{-1}-(\Lambda+t)^{-1}]dt=\log\Lambda\). Taking colour traces, summing over \(x\), and exchanging sum and integral by the absolute bound,
\[
 \sum_{\rm coords}\int_0^\infty[(1+t)^{-1}-((\mathsf A+t)^{-1})_{xx}]\,dt
 =|I|\log\Lambda-\sum_x\sum_{\alpha\in\mathfrak A(x)}\operatorname{tr}_xn_\alpha .
\]
\(\mathsf A^{\rm Y}(P_z)\) is accretive for \(z\in[0,1]\) (hm Lemma 4 whole-torus clause, transported), continuous in \(z\), real symmetric positive at \(z=0\). Lemma 5.1(ii)–(iii) identify the left side with the continued \(\log\det\mathsf A^{\rm Y}(P)\). Multiply by \(-\tfrac12\) and group the terms by \(X(H_\alpha)\): this is (5.4).

**(V2).** Each \(\mathcal R_\alpha\) is a product of grouped entries and long labels evaluated only from the pair on their hulls (hm L196, L216; descent Lemma 4 PF-label). The integral in \(t\) preserves this. \(H_\alpha\subset X(H_\alpha)\). Only terms with \(H_\alpha\subset Y\) are evaluated (hm's discard-before-evaluation rule), so the definition is local and does not depend on \(Y\supset X\).

**(V3).** Holomorphy and reality: normal convergence of holomorphic, real-at-real terms. Gauge invariance: descent Lemma 4 gives \(\mathcal R_\alpha(t;P^g)=\mathcal G\mathcal R_\alpha(t;P)\mathcal G^{-1}\) after colour grouping; \(\mathcal G\) is block diagonal with block \(\operatorname{Ad}(g(x_-))\) at bond \(x\), so the \((x,x)\) block is conjugated by one orthogonal matrix and its trace is invariant. The filing set \(X(H_\alpha)\) is gauge independent.

**(V5).** *Tree length of the filing set.* \(H_\alpha\) is a nearest-neighbour connected set of sites (hm Lemma 1, Theorem 5: connected full read hulls) within \(R_*\) of a tree \(T\) of length \(t_\alpha\). Place \(\lceil t_\alpha\rceil+1\) points on \(T\), consecutive ones at distance \(\le1\); every site of \(H_\alpha\) is within \(R_*+1\) of one of them, so \(\#H_\alpha\le(2R_*+3)^4(t_\alpha+2)\le C_{\rm hull}(1+t_\alpha)\). A spanning tree of \(H_\alpha\)'s nearest-neighbour graph has length \(\le\#H_\alpha\) (in level-\(k\) units), lies in \(X(H_\alpha)\), and meets every cube of \(X(H_\alpha)\), since each such cube owns a site of \(H_\alpha\). IN1 (4) defines \(d_j(X)\) as such a minimal tree length divided by the cube side, here \(LM\). Hence \(\kappa d_{k+1}(X(H_\alpha))\le\kappa C_{\rm hull}(1+t_\alpha)/(LM)\le\theta(1+t_\alpha)/4\).
*Summation.* A term filed at \(X\ni\Delta\) has \(H_\alpha\cap\Delta\ne\varnothing\), so its root \(x\) satisfies \(\operatorname{dist}(x,\Delta)\le t_\alpha+R_*\), hence \(e^{-\theta t_\alpha/2}\le e^{\theta R_*/2}e^{-\theta\operatorname{dist}(x,\Delta)/2}\). Therefore
\[
 \sum_{X\ni\Delta}e^{\kappa d(X)}|\mathbf N(X)|
 \le\tfrac32\sum_x\sum_{\alpha\in\mathfrak A(x)}e^{\theta/4}e^{\theta t_\alpha/4}|n_\alpha|\,\mathbf 1_{H_\alpha\cap\Delta\ne\varnothing}
 \le\tfrac32e^{\theta/4+\theta R_*/2}\Bigl(\sup_x\sum_\alpha e^{\theta t_\alpha}|n_\alpha|\Bigr)\sum_xe^{-\theta\operatorname{dist}(x,\Delta)/2},
\]
using \(|\operatorname{tr}_x n|\le3|n|\) and \(e^{\theta t/4}=e^{\theta t}e^{-\theta t/2}e^{-\theta t/4}\le e^{\theta t}e^{-\theta t/2}\). The last sum is at most \(n_c\prod_{\mu=1}^4(LM+1+2\sum_{s\ge1}e^{-\theta s/2})\le n_c(LM+1+4/\theta)^4\le16n_c(LM)^4\) when \(LM\ge8/\theta\) (and \(\theta\le1/2\)). With (5.5) this gives (5.6) with \(C_{\rm vac}=\tfrac32\cdot16\cdot2\,n_cc_bp_{r_c}e^{1/4+\theta R_*/2}\). The Lipschitz version uses the second half of (5.5).

**(V6).** By Theorem 6.6 the step's Gaussian part at \(P_W\) has precision \(\mathsf A^{\rm Y}(P_W)\) in the normalized coordinates, so the normalizer in (5.1) is the step's. At block-axial \(V\), \(\mathsf G^{\rm Y}_V=\mathsf G^{\rm abs}_V\) (descent Lemma 2), so the determinants agree. \(\square\)

*Status: proved*, as an implication from hm Theorem 5's construction (with descent Lemma 4's Y labels and conjugation), Lemma 5.1 and IN1's definition of \(d_j\). The rooted bound (5.5) is early: \(p_{r_c},c_b\) are fixed at hm (12). The polymer bound (5.6) has an early constant times the explicit volume factor \((LM)^4\) of one level-\((k+1)\) cube; its \(M\)-floor \(LM\ge4\kappa C_{\rm hull}/\theta\) follows \(\kappa\) and is an allowed row-5 floor.

**Remark 5.3 (size and the "number").** The vacuum is extensive: (5.6) is \(O((LM)^4)\) per coarse cube, as it must be (one \(O(1)\) term per coordinate). SA separates "number \(+\sum_X\mathbf N(X,U_{j+1})\)" (SA 17544). Here the field-independent part is \(-\tfrac12|I|\log\Lambda_{\rm res}\) plus the flat-reference values \(\mathbf N(X;P_{\rm flat})\), whose sum over a translation-invariant flat torus is a number. The field-dependent part \(\mathbf N(X;P)-\mathbf N(X;P_0)\) at fixed \(U\) obeys (5.6) with the factor \(2r_Y/r_{\rm loc}\). The comparison of \(\mathbf N(X;P_0)\) with the flat value at a curved real \(U\) is not proved here: it needs analyticity in the real background, which hm's fixed-\(U\) framework does not supply; through PF it is a function of the pair, and its readout is OL1's one-loop coefficient (IN1 H-OL), not item 6. The IN1 class bound \(\|E\|\le E_0\) does not need smallness of the vacuum part, since \(E_N,E_0\) are fixed at row 7, after \(M\) (IN1 L233).

## 6. (c) G-ID(cov): the physical clause on all of R4

### 6.0 The statement to prove, and its hypotheses

SA's sketch, SA 14109–14120: "At a background pair \(P_W=(U_+,J(U_+))\), the form in (eq:actual-regular-precision) is the Hessian on the fibre of \(A\circ U_k+\mathrm{GF}_k\). Indeed, the multiplier in the background equation is the derivative of the critical action with respect to its datum. Differentiating that equation gives \((Q\mathsf G_1Q^{\mathsf T})^{-1}-a\). A curve in the fibre of the next average has a second derivative in its constraint; pairing it with the multiplier gives the last term … Thus the Gaussian of the step is \(C^{(k)}=\mathsf A(P_W)^{-1}\)." And SA 10208–10210: "At the pair \((U_{k+1},J(U_{k+1}))\) of the step, one has \(\mathsf A=\mathsf C^{\mathsf T}\Delta^{(k)}\mathsf C\). … The only step of substance is the quadratic term of the action of the background, regarded as a function of its datum." SA's scope sentence, SA 14215–14217: "This construction uses the regular operator and core bounds; it does not assert a Gaussian law for the full nonlinear averaging disintegration."

**Definition (Gaussian part).** At a physical pair, the step's leading exponent on the fibre is \(\psi_x(u)=-x\,[\mathcal A(U_k(V(u)))+\Phi^{\rm Y}_{V}(C_V(u))]\), \(V(u)=e^{iC_V(u)}V\), with \(\mathcal A=A_{\Omega_0}\) the inner-plaquette Wilson action and \(U_k(\cdot)\) the level-\(k\) background as a function of its datum. Its **Gaussian part** is the quadratic Taylor polynomial of \(\psi_x\) at \(u=0\), written in \(b=x^{1/2}u\). All other factors of the step's integrand (Jacobians, older activities, profile differences, boundary terms) are potentials, owned by NL1 (Lemma 4.4(2)). This is the reading of hm L45 and of SA 14109–14120; IN1 L106's "the actual fluctuation law" must be read the same way (§8.3).

**G-ID(cov), to prove.** At every admitted complete physical pair \(P_W\) in R4, the Gaussian part is \(-\tfrac12\langle b,\mathsf A^{\rm Y}(P_W)b\rangle\) (plus a constant, with no linear term). Then its covariance is \(\mathsf A^{\rm Y}(P_W)^{-1}\).

**Hypotheses on the physical pair** (complete: \(\Omega_0\) is the torus). Let \(\mathbf V'\) be the step's real regular next datum, \(U_+\) its real critical background in the step's block-axial representative (SA 11239–11240; Amendment CV's averaged-contour axiality, st1-r4 L41, hm L35), \(\mathbf V_0=M_{\mathbf B}(U_+)\) its level-\(k\) determining datum, \(V_{\rm bg}=\mathcal M^kU_+\), and \(P_W=(U_+,0,J(U_+))\).

- **PH1 (chart).** \(U_+\) is a cp12 D3 member for the datum \(\mathbf V_0\) (cp12 L25), and P82 holds there, so that [A3] applies with \(U_0=U_+\).
- **PH2 (criticality for the next datum).** \(U_+\) is critical, in SA 9616's sense as repaired in the a3-derivative gate (L22–28, "Repair of Lemma 6.2"), for the next constraint set \(\mathcal C'=\{U:M_{\mathbf B'}(U)=\mathbf V'\}\). Here \(\mathbf V'\) consists of the next average on the rows of \(\Omega_{k+1}\) and the stored data elsewhere (SA 17528: "On \(\Omega_{j+1}^c\), step \(j+1\) stores \(V_j\) together with its constraint"). So \(\mathbf V'\) is a function of the level-\(k\) datum, and every \(U\) whose level-\(k\) datum lies on the fibre \(\{\mathcal M(V)=\mathbf V'|_{\Omega_{k+1}}\}\), with the other rows unchanged, lies in \(\mathcal C'\).
- **PH3 (operators).** SA's chain pr-lay (6) exists at \(P_W\), including \(G_1\) and \((QG_1Q^{\mathsf T})^{-1}\) ([SA-op]).
- **PH4 (pivots).** (PIV) at \(V_{\rm bg}\).
- **(N) (normalization).** pr-lay (6)–(8) are read in cp12 D2's pairings: counting rows, fine pairing \(\eta^4\), colour pairing \(\tfrac12\operatorname{tr}\). With another fixed positive diagonal row pairing, cp12 (2) rescales the multiplier and every identity below is an identity of bilinear forms, unchanged.

### 6.1 The background action as a function of its datum

By [A3] (with PH1) there is, on a datum polydisc, a holomorphic solution \((a(B),\nu(B))\) of the gauge-augmented system (a3-derivative (28)), \(\omega(B)=\lambda_0+\nu(B)\), with (37): \(RD^{\mathsf T}a=0\), \(F'(a)=K_a^{\mathsf T}\omega\), \(\mathcal Q^{\rm st}(a)=\mathsf b(B)\), and \(\Phi_{\rm ch}(B)=(e^{i\eta a(B)}U_+)^{u_B}\) is the background of datum \(e^{iB}\mathbf V_0\). Here \(F(a)=\mathcal A(e^{i\eta a}U_+)\), \(K_a=q'(a)\), \(q=\mathcal Q^{\rm st}\), and \(F'(0)=J(U_+)=K_0^{\mathsf T}\lambda_0\) (a3-derivative Lemma 6.2, repaired; a3-derivative 7.3). Put \(\Phi(B)=\mathcal A(\Phi_{\rm ch}(B))=F(a(B))\), by gauge invariance of \(\mathcal A\).

**Lemma 6.1 (datum derivatives).** For rows \(e,e'\) of the level-\(k\) top (interior rows, where \(\mathsf b(B)=B\)):
\[
 \Phi'(0)[e]=\langle\lambda_0,e\rangle,\qquad
 \Phi''(0)[e,e']=\langle e,(C_0^{-1}-1)e'\rangle,                              \tag{6.1}
\]
where \(G=(L_0+DRD^{\mathsf T}+K_0^{\mathsf T}K_0)^{-1}\), \(C_0=K_0GK_0^{\mathsf T}\), and \(L_0h=F''(0)h-(DK_0[h])^{\mathsf T}\lambda_0\) (a3-derivative (27), (32)). Moreover \(h_e:=\partial_ea(0)\) satisfies
\[
 RD^{\mathsf T}h_e=0,\qquad K_0h_e=e,\qquad L_0h_e=K_0^{\mathsf T}(C_0^{-1}-1)e .        \tag{6.2}
\]
By cp12 Lemma 1, \(C_0^{-1}-1=(K_0G_{a_r}K_0^{\mathsf T})^{-1}-a_r\) for every symmetric positive row mass \(a_r\) for which these inverses exist.

*Proof.* \(\Phi'(B)[e]=\langle F'(a),h\rangle\) with \(h=\partial_ea(B)\). By (37), \(F'(a)=K_a^{\mathsf T}\omega\), so \(\Phi'(B)[e]=\langle\omega,K_ah\rangle=\langle\omega(B),D\mathsf b(B)e\rangle\) by the differentiated constraint (32). At interior rows \(\mathsf b(B)=B\) (a3-derivative L344 and the gate's triangular-datum check, L12 and L18), so \(D\mathsf b=I\) and \(D^2\mathsf b=0\) there; this is the case for the level-\(k\) rows touching \(\Omega_{k+1}\), which lie deep inside \(\Omega_k\) (separation \(\rho\xi_k\)) and are read by no outward row of the depth-\(k\) sequence. Hence \(\Phi'(B)[e]=\langle\omega(B),e\rangle\), and at \(0\) this is \(\langle\lambda_0,e\rangle\). Differentiating once more, \(\Phi''(0)[e,e']=\langle\dot\lambda_{e'},e\rangle\) with \(\dot\lambda_{e'}=\partial_{e'}\nu(0)\). By (32) at \(B=0\), \((h_{e'},\dot\lambda_{e'})=S_0^{-1}(0,e')\), and by (27) this is \((He',(C_0^{-1}-1)e')\). This gives (6.1). For (6.2): differentiating \(RD^{\mathsf T}a(B)\equiv0\) (R, D fixed at the reference) gives \(RD^{\mathsf T}h_e=0\); \(K_0h_e=e\) is the second equation of (32); the first equation of (32), \((L_0+DRD^{\mathsf T})h_e-K_0^{\mathsf T}\dot\lambda_e=0\), with \(DRD^{\mathsf T}h_e=0\), gives the third. The last sentence is cp12 Lemma 1's mass independence. \(\square\) *Status: proved*, conditional on [A3] (P81, P82).

### 6.2 The gauge identity at the physical current

**Lemma 6.2 (GI2).** Let \(\Delta'_\pi[\mathbf J]\) be SA's explicit form (SA 10172–10185; pr-lay (6)), with \(\lambda_A=G'RD^{\mathsf T}A\), \(\lambda_A^+(b)=\operatorname{Ad}(\mathbf U(b))\lambda_A(b_+)\), \(\mathsf SA=A-D\lambda_A\) (SA 10169–10171), all brackets based at \(b_-\). Define, for a site field \(\chi\) and a bond field \(C\),
\[
 \Pi_{\mathbf J}(\chi,C)=\tfrac12\bigl\langle i[\chi,C]-i[C,\chi^+],\mathbf J\bigr\rangle_{\rm f}.          \tag{6.3}
\]
(i) For every \(\mathbf J\), \(\Delta'_\pi[\mathbf J](A,C)=\Pi_{\mathbf J}(\lambda_A,C)+\Pi_{\mathbf J}(\lambda_C,A)-\tfrac12[\Pi_{\mathbf J}(\lambda_A,D\lambda_C)+\Pi_{\mathbf J}(\lambda_C,D\lambda_A)]\).
(ii) At a complete pair with \(A'=0\) and \(\mathbf J=F'(0)\): \(\Pi_{F'(0)}(\chi,C)=\Delta^{\rm W}(C,D\chi)\).
(iii) Consequently \(\Delta^{\rm W}-\Delta'_\pi[F'(0)]=\mathsf S^{\mathsf T}\Delta^{\rm W}\mathsf S\). This is SA's identity at SA 10189–10194 and 10301, proved here from the display.

*Proof.* (i) Expanding, \(\Pi(\lambda_A,C)+\Pi(\lambda_C,A)=\tfrac12\langle i[\lambda_A,C]-i[C,\lambda_A^+]+i[\lambda_C,A]-i[A,\lambda_C^+],\mathbf J\rangle\): these are the first four terms of SA's display. For the last two, \(\lambda^+=\lambda+\eta D\lambda\) by the definition of the covariant difference (\(D\lambda(b)=\eta^{-1}[\operatorname{Ad}(\mathbf U(b))\lambda(b_+)-\lambda(b_-)]\)). So \(-i[D\lambda_C,\lambda_A^+]=i[\lambda_A,D\lambda_C]-i\eta[D\lambda_C,D\lambda_A]\), and similarly with \(A\leftrightarrow C\). The two \(\eta\)-terms cancel by antisymmetry of the bracket. Hence
\(-\tfrac12[\Pi(\lambda_A,D\lambda_C)+\Pi(\lambda_C,D\lambda_A)]=-\tfrac14\langle2i[\lambda_A,D\lambda_C]+2i[\lambda_C,D\lambda_A],\mathbf J\rangle\), which is SA's last two terms \(-\tfrac12\langle i[\lambda_A,D\lambda_C]+i[\lambda_C,D\lambda_A],\mathbf J\rangle\).

(ii) Let \(X_\chi(A)\) be the gauge generator in the chart, \(e^{i\eta(A+tX_\chi(A)+O(t^2))}U=(e^{i\eta A}U)^{e^{it\chi}}\) (a3-derivative §6.1 notation). Bondwise, \((e^{i\eta A}U)^{e^{it\chi}}(b)=e^{it\chi(b_-)}e^{i\eta A(b)}e^{-it\chi^+(b)}U(b)\) with \(\chi^+(b)=\operatorname{Ad}(U(b))\chi(b_+)\). For \(f(t)=\log(e^{tX}e^Ye^{tZ})\), \(f'(0)=\frac{\operatorname{ad}_Y}{e^{\operatorname{ad}_Y}-1}X+\frac{\operatorname{ad}_Y}{1-e^{-\operatorname{ad}_Y}}Z=X-\tfrac12[Y,X]+Z+\tfrac12[Y,Z]+O(Y^2)\). (Proof: \(\frac d{dt}e^{f(t)}|_0=Xe^Y+e^YZ=\int_0^1e^{sY}f'(0)e^{(1-s)Y}ds\); multiply by \(e^{-Y}\) on the right and invert \(\frac{e^{\operatorname{ad}_Y}-1}{\operatorname{ad}_Y}\), which is invertible for small \(Y\).) With \(X=i\chi\), \(Y=i\eta A\), \(Z=-i\chi^+\):
\[
 X_\chi(A)=-D\chi-\tfrac i2[A,\chi+\chi^+]+O(A^2),\qquad
 DX_\chi(0)[C]=\tfrac12\bigl(i[\chi,C]-i[C,\chi^+]\bigr).
\]
Gauge invariance of the inner-plaquette action on the complete torus gives \(F(A^{e^{it\chi}})=F(A)\), so \(\langle F'(A),X_\chi(A)\rangle=0\) for all small \(A\). Differentiate at \(A=0\) in direction \(C\): \(\langle F''(0)C,X_\chi(0)\rangle+\langle F'(0),DX_\chi(0)[C]\rangle=0\). With \(X_\chi(0)=-D\chi\) and \(F''(0)=\Delta^{\rm W}\) (a3-derivative L435, citing SA 9627), \(\Delta^{\rm W}(C,D\chi)=\Pi_{F'(0)}(\chi,C)\).

(iii) \(\mathsf S^{\mathsf T}\Delta^{\rm W}\mathsf S(A,C)=\Delta^{\rm W}(A-D\lambda_A,C-D\lambda_C)=\Delta^{\rm W}(A,C)-\Pi(\lambda_C,A)-\Pi(\lambda_A,C)+\Delta^{\rm W}(D\lambda_A,D\lambda_C)\) by (ii). By (ii) again and symmetry of \(\Delta^{\rm W}\), \(\Delta^{\rm W}(D\lambda_A,D\lambda_C)=\Pi(\lambda_A,D\lambda_C)=\Pi(\lambda_C,D\lambda_A)\), so it equals their half-sum. Compare with (i). \(\square\) *Status: proved*, from SA's display and gauge invariance; no SA assertion is imported.

### 6.3 Gauge directions inside the constraint fibre

**Lemma 6.3.** (i) For every site field \(\chi\) with \(Q'\chi=0\) at all tops, \(K_0D\chi=0\). (ii) \(Q'G'R=0\); hence \(\lambda_h=G'RD^{\mathsf T}h\) has \(Q'\lambda_h=0\), and \(K_0\mathsf S=K_0\), \(\mathsf S^{\mathsf T}K_0^{\mathsf T}=K_0^{\mathsf T}\). (iii) \(RD^{\mathsf T}\mathsf Sh=0\) for every \(h\), and \(\mathsf Sh=h\) if and only if \(RD^{\mathsf T}h=0\).

*Proof.* (i) Let \(e^{i\eta A_t}U_+=U_+^{e^{it\chi}}\). The plain constraint map is covariant with node values (descent (10); SA 7185–7190): \(m(A_t)(c)=e^{it\chi(c_-)}m(0)(c)e^{-it\chi(c_+)}\), so \(\frac d{dt}m(A_t)(c)|_0=i\chi(c_-)\mathbf V_0(c)-i\mathbf V_0(c)\chi(c_+)\). By the chart identity a3-derivative (35), \(m(A)(c)=v[A](c_-)e^{i\tilde q(A)(c)}\mathbf V_0(c)v[A](c_+)^{-1}\), with \(v[0]=1\), \(\tilde q(0)=0\), \(\frac d{dt}v[A_t](y)|_0=i(\chi(y)-(Q'\chi)(y))\) (a3-derivative Lemma 6.1) and \(\frac d{dt}A_t|_0=X_\chi(0)=-D\chi\). Equating the two derivatives and cancelling,
\[
 (D\tilde q_0\,D\chi)(c)=\operatorname{Ad}(\mathbf V_0(c))(Q'\chi)(c_+)-(Q'\chi)(c_-).
\]
If \(Q'\chi=0\), the right side vanishes. Since \(D\tilde q_0=\mathcal T_0K_0\) with \(\mathcal T_0\) the identity plus a nilpotent part (a3-derivative L392; gate L12, L18), \(\mathcal T_0\) is invertible and \(K_0D\chi=0\). (The displayed identity is SA's \(QD\lambda=\bar DQ'\lambda\), SA 10300, in raw normalization.) (ii) From \(R=I-G'Q'^{\mathsf T}(Q'G'^2Q'^{\mathsf T})^{-1}Q'G'\): \(Q'G'R=Q'G'-Q'G'^2Q'^{\mathsf T}(Q'G'^2Q'^{\mathsf T})^{-1}Q'G'=0\). Then (i) gives \(K_0DG'R=0\), i.e. \(K_0\mathsf S=K_0\); transpose, using that \(R,G'\) are symmetric (cp12 Lemma 1: \(R\) is the fine-orthogonal projection). (iii) \(D^{\mathsf T}D=\Delta\) and \(\Delta G'=I-Q'^{\mathsf T}a_sQ'G'\), so \(R\Delta G'R=R-RQ'^{\mathsf T}a_s(Q'G'R)=R\). Hence \(RD^{\mathsf T}\mathsf Sh=RD^{\mathsf T}h-R\Delta G'RD^{\mathsf T}h=0\). Finally \(\mathsf Sh=h\iff DG'RD^{\mathsf T}h=0\); if \(RD^{\mathsf T}h=0\) this holds; conversely, if \(\mathsf Sh=h\) then \(RD^{\mathsf T}h=RD^{\mathsf T}\mathsf Sh=0\). \(\square\) *Status: proved*, from [A3] (35), Lemma 6.1 of a3-derivative and cp12 Lemma 1.

### 6.4 SA's Schur complement is the datum Hessian

**Lemma 6.4.** Under PH1, PH3 and (N), on the level-\(k\) rows,
\[
 \iota^{\mathsf T}\bigl[(QG_1Q^{\mathsf T})^{-1}-\mathsf a\bigr]\iota=\iota^{\mathsf T}(C_0^{-1}-1)\iota,     \tag{6.4}
\]
with \(G_1\) of pr-lay (6) at \(P_W\) (\(\mathbf J=J(U_+)\)). So \(\Phi''(0)=\iota^{\mathsf T}[(QG_1Q^{\mathsf T})^{-1}-\mathsf a]\iota\).

*Proof.* *Normalizations.* SA 10139: \(\mathcal Q=\mathsf m(Q+C^{(2)}+\cdots)\), so \(K_0=q'(0)=\mathsf mQ\) and \(q''(0)[h,h']=2\mathsf mC^{(2)}(h,h')\) (polarized). With \(a_r=\mathsf m^{-1}\mathsf a\mathsf m^{-1}\), \(K_0^{\mathsf T}a_rK_0=Q^{\mathsf T}\mathsf aQ\). \(F'(0)=K_0^{\mathsf T}\lambda_0=Q^{\mathsf T}\mathsf m\lambda_0\) and \(Q\mathsf H=I\) for \(\mathsf H=GQ^{\mathsf T}(QGQ^{\mathsf T})^{-1}\), so \(\mathsf H^{\mathsf T}J=\mathsf m\lambda_0\). SA's normalization \((A,\Delta^{(2)}[j]A)=2(C^{(2)}(A),j)\) (SA 10155; pr-lay L74) then gives \((h',\Delta^{(2)}[\mathsf m\lambda_0]h)=\langle\lambda_0,q''(0)[h,h']\rangle=\langle h',(DK_0[h])^{\mathsf T}\lambda_0\rangle\). Hence \(L_0=\Delta^{\rm W}-\Delta^{(2)}[\mathsf H^{\mathsf T}J]\).

*SA's saddle.* By pr-lay (6), \(G_1^{-1}=X_{\rm SA}+Q^{\mathsf T}\mathsf aQ\) with
\(X_{\rm SA}=\Delta^{\rm W}-\Delta'_\pi[J]-\mathsf S^{\mathsf T}\Delta^{(2)}[\mathsf H^{\mathsf T}J]\mathsf S+DRD^{\mathsf T}\).
By Lemma 6.2(iii), \(X_{\rm SA}=\mathsf S^{\mathsf T}L_0\mathsf S+DRD^{\mathsf T}\).

*The datum solution solves SA's saddle.* Let \(h_e\) be as in (6.2), \(\omega_e=(C_0^{-1}-1)e\). By Lemma 6.3(iii), \(\mathsf Sh_e=h_e\) and \(DRD^{\mathsf T}h_e=0\). So \(X_{\rm SA}h_e=\mathsf S^{\mathsf T}L_0h_e=\mathsf S^{\mathsf T}K_0^{\mathsf T}\omega_e=K_0^{\mathsf T}\omega_e\) by (6.2) and Lemma 6.3(ii); and \(K_0h_e=e\). Thus \((h_e,\omega_e)\) solves \(X_{\rm SA}h-K_0^{\mathsf T}\omega=0\), \(K_0h=e\).

*Uniqueness.* If \(X_{\rm SA}h-K_0^{\mathsf T}\omega=0\) and \(K_0h=0\), then \((X_{\rm SA}+K_0^{\mathsf T}a_rK_0)h=K_0^{\mathsf T}\omega\), so \(h=G_1K_0^{\mathsf T}\omega\) and \(0=K_0G_1K_0^{\mathsf T}\omega\); since \(K_0G_1K_0^{\mathsf T}=\mathsf m(QG_1Q^{\mathsf T})\mathsf m\) is invertible (PH3), \(\omega=0\), \(h=0\). By cp12 Lemma 1 (1), the unique solution has \(\omega=[(K_0G_1K_0^{\mathsf T})^{-1}-a_r]e=\mathsf m^{-1}[(QG_1Q^{\mathsf T})^{-1}-\mathsf a]\mathsf m^{-1}e\). Comparing with \(\omega_e\), and using \(\mathsf m=\xi_k=1\) on level-\(k\) rows (level-\(k\) units), gives (6.4). With Lemma 6.1 this is \(\Phi''(0)\). \(\square\) *Status: proved*, conditional on PH1, PH3, (N).

This is the step SA calls "the only step of substance" (SA 10208–10210); SA attributes the whole-lattice version to Bałaban (CMP 102, 277, (174); CMP 109, (2.4)–(2.8), (2.11)), which I have not read. The proof above uses only [A3], cp12 Lemma 1 and Lemmas 6.2–6.3. It also uses SA's statement-3 sentence (SA 10305) "\(\mathsf HB\) is a critical point of \(\frac12(A,\Delta^{\rm W}_{\mathbf U}A)\) on \(\{QA=B,\ RD^{\mathsf T}A=0\}\)" nowhere; that is the current-free analogue.

### 6.5 The fibre

**Lemma 6.5 (chain rule on the fibre).** Under PH1, PH2, PH4, with \(\psi(u)=\Phi(\iota C(u))+\Phi^{\rm Y}_{V_{\rm bg}}(C(u))\), \(C=C_{V_{\rm bg}}\):
\[
 \psi'(0)=0,\qquad
 \psi''(0)=\mathsf C_V^{\mathsf T}\bigl[\iota^{\mathsf T}\Phi''(0)\iota+\mathsf G^{\rm Y}_{V_{\rm bg}}\bigr]\mathsf C_V
          -E_{\rm free}[\iota^{\mathsf T}\lambda_0],                                       \tag{6.5}
\]
with \(E_{\rm free}[j]=\mathsf C_V^{\mathsf T}E_{\rm amb}[j]\mathsf C_V\), \(E_{\rm amb}[j](b,c)=\langle h_V^{\mathsf T}j,q_V''(0)[b,c]\rangle\) (pr-lay (8)).

*Proof.* The datum chart at level \(k\) is \(e^{iB}\mathbf V_0\) on rows, and the fibre point is \(e^{iC(u)}V_{\rm bg}\) bondwise; on the level-\(k\) rows these are the same chart, so \(U_k(V(u))=\Phi_{\rm ch}(\iota C(u))\) and \(\mathcal A(U_k(V(u)))=\Phi(\iota C(u))\). *Second derivative.* \(C(u)\) has non-pivot part \(u\) and pivot part fixed by \(q_V(C(u))=0\). Differentiating twice at \(0\): \(q_V'(0)C''(0)[u,v]+q_V''(0)[\mathsf C_Vu,\mathsf C_Vv]=0\). \(C''(0)\) is pivot-supported and \(q_V'(0)\) restricted to pivots is inverted by the pivot-supported right inverse \(h_V\), so \(C''(0)[u,v]=-h_Vq_V''(0)[\mathsf C_Vu,\mathsf C_Vv]\). Then \(\frac{d^2}{ds^2}\Phi(\iota C(su))|_0=\Phi''(0)[\iota\mathsf C_Vu,\iota\mathsf C_Vu]+\Phi'(0)[\iota C''(0)[u,u]]\), and by (6.1) the last term is \(-\langle h_V^{\mathsf T}\iota^{\mathsf T}\lambda_0,q_V''(0)[\mathsf C_Vu,\mathsf C_Vu]\rangle\). The gauge part is Lemma 4.1. *First derivative.* \(s\mapsto U_k(V(su))\) is a \(C^1\) curve through \(U_+\) (by P81's uniqueness, \(U_k(V_{\rm bg})=U_+\) up to residual gauge, since \(\Phi_{\rm ch}(0)=U_+\)). Its next datum is constant: the top rows carry \(\mathcal M(V(su))=\mathbf V'\) on the fibre, and the finer rows are unchanged. So the curve lies in \(\mathcal C'\), and PH2 gives \(\frac d{ds}\mathcal A(U_k(V(su)))|_0=0\). The gauge part has zero gradient (Lemma 4.1). \(\square\) *Status: proved*, conditional on PH1, PH2, PH4.

Since \(\Phi'(0)=\langle\lambda_0,\cdot\rangle\), \(\psi'(0)=0\) says \(\mathsf C_V^{\mathsf T}\iota^{\mathsf T}\lambda_0=0\): the restriction of the multiplier to the level-\(k\) rows annihilates the fibre tangent. This is SA PX103's "the next constraint multiplier is \(h_V^{\mathsf T}\widehat J\)" (SA 11224–11225) in the present notation.

### 6.6 G-ID(cov)

**Theorem 6.6 (G-ID(cov) at block-axial physical pairs).** Assume PH1–PH4 and (N). The Gaussian part of the step at \(P_W\) is \(-\tfrac12\langle b,\mathsf A^{\rm Y}(P_W)b\rangle\), without linear term, where
\[
 \mathsf A^{\rm Y}(P_W)=\mathsf C_V^{\mathsf T}\Bigl[\iota^{\mathsf T}\{(QG_1Q^{\mathsf T})^{-1}-\mathsf a\}\iota+\mathsf G^{\rm Y}_{V_{\rm bg}}
     -E_{\rm amb}[\iota^{\mathsf T}\mathsf H_1^{\mathsf T}J]\Bigr]\mathsf C_V
\]
is pr-lay (7) at \(P_W\) with \(K_{\rm GF}=\mathsf G^{\rm Y}_{V_{\rm bg}}\). Since \(V_{\rm bg}\) is block axial, \(\mathsf G^{\rm Y}_{V_{\rm bg}}=\mathsf G^{\rm abs}_{V_{\rm bg}}\) and \(\mathsf A^{\rm Y}(P_W)=\mathsf A^{\rm abs}(P_W)\), which is SA's precision (SA 14096–14102). Hence the step's Gaussian part has covariance \(\mathsf A^{\rm Y}(P_W)^{-1}\), which is hm L45 and descent L68.

*Proof.* \(\psi_x=-x\psi\). Lemma 6.5 gives \(\psi'(0)=0\) and (6.5); Lemma 6.4 replaces \(\Phi''(0)\) by SA's Schur complement; \(\iota^{\mathsf T}\lambda_0=\iota^{\mathsf T}\mathsf H_1^{\mathsf T}J\) because \(Q\mathsf H_1=I\) and \(J=Q^{\mathsf T}\mathsf m\lambda_0\) with \(\mathsf m=1\) on level-\(k\) rows (as in Lemma 6.4). So \(\psi''(0)=\mathsf A^{\rm Y}(P_W)\). In \(b=x^{1/2}u\), \(-\tfrac x2\langle u,\psi''(0)u\rangle=-\tfrac12\langle b,\mathsf A^{\rm Y}(P_W)b\rangle\). Block axiality gives \(\widehat W=W\), so \(\Phi^{\rm Y}_{V_{\rm bg}}(D)=\mathrm{GF}(e^{iD}V_{\rm bg})\) and the two Hessians agree (descent Lemma 2). With the coefficient ratio \(\tau\), the precision is \(\tau\mathsf A^{\rm Y}\) and the covariance is divided by \(\tau\) (hm L354). \(\square\) *Status: proved*, conditional on PH1–PH4 and (N).

**Corollary 6.7 (all of R4).** Let \(P\) be an admitted complete physical pair in R4 whose real factor is not block axial. Then \(P=P_W^g\) for a block-axial physical pair \(P_W\) and a real site gauge \(g\) (descent Lemma 1: \(g=u_{\mathbb T}(U)^{-1}\)), and under D-Y3 the Gaussian part at \(P\) is \(-\tfrac12\langle b,\mathsf A^{\rm Y}(P)b\rangle\) with \(\mathsf A^{\rm Y}(P)=\mathcal G\mathsf A^{\rm Y}(P_W)\mathcal G^{-1}\). So G-ID(cov) holds on all of R4 under D-Y3.

*Proof.* Each ingredient of \(\psi\) is covariant: \(\mathcal A\) is gauge invariant; \(U_k(\mathbf V^v)=U_k(\mathbf V)^{\tilde v}\) (SA 7185–7190: "for the representative taken at the reference \(U_0=\mathbf 1\), \(U_k(\mathbf V^v)=U_k(\mathbf V)^{\tilde v}\)"; in general, gauge invariance of \(\mathcal A\) makes \(\Phi\) a function of the datum's orbit); the fibre maps \(\mathcal M\) and \(C_V\) are covariant (descent (10), (PIV)); \(\Phi^{\rm Y}\) is covariant (descent (11)). Hence \(\psi_P(\mathcal Gu)=\psi_{P_W}(u)\), and \(\psi_P''(0)=\mathcal G\psi_{P_W}''(0)\mathcal G^{-1}\) (\(\mathcal G\) orthogonal). \(\mathsf A^{\rm Y}\) is covariant by descent Lemma 4 / Theorem 5 (L194, L220). Apply Theorem 6.6 at \(P_W\). \(\square\) *Status: proved.*

**Remark 6.8 (why D-Y3 is needed off Rep).** Descent's central-flip pair \(P^w=(I^w,0,0)\) (descent Theorem A, L151–180) is a flat, hence critical, physical pair in R4 with zero current. With the absolute functional at \(V=\mathcal M^kI^w\), the absolute gauge gradient vanishes (descent L295, referee's addition), so the fibre Hessian of \(x[\mathcal A\circ U_k+\mathrm{GF}]\) is \(x\mathsf A^{\rm abs}(P^w)\), which has the negative direction (13) of descent: no Gaussian exists. Under D-Y3 the fibre Hessian is \(x\mathsf A^{\rm Y}(P^w)=x\mathcal G\mathsf A^{\rm Y}(I,0,0)\mathcal G^{-1}>0\). So G-ID(cov) on all of R4 is a property of the Y form, not of SA's literal absolute GF; SA's indicator (SA 7181) keeps SA's physical step away from \(P^w\) (descent L292), and D-Y3 makes the statement hold everywhere.

**Corollary 6.9 (the physical clause HM-3).** Let \(P_W\) be an admitted complete physical pair in \(\mathrm{R4}(\mathbb T;a_0,a_1,j_0)\) with (7), satisfying PH1–PH4. Then, at \(s=\mathbf1\), \(\tau=1\), \(D(\mathbf1;P_W)=\chi\mathsf A^{\rm Y}(P_W)^{-1}\chi\) (descent L226; hm (30)), and \(\mathcal J(Z_0;\mathbf1;P_W)\) is the \(I_0\)-marginal of the centred Gaussian with covariance \(\mathsf A^{\rm Y}(P_W)^{-1}\), i.e. of the step's Gaussian part (Theorem 6.6, Corollary 6.7). *Status: proved.*

### 6.7 Admission of physical pairs into the working domain

hm L371 says that the physical clause needs "full membership in the present working domain", and that "pr-lay Theorem 8's global regularity and a small \(r(P_W)\) alone do not imply the stronger real-gauge ceiling (10)". Frozen cp12 now supplies the real gauge.

**Lemma 6.10 (reduction of physical admission).** Let \(P_W=(U_+,0,J(U_+))\). Suppose that on every box \(D\) of side \(S\le C_{\rm box}LM\), PR-lay Q's curvature/divergence hypotheses hold on the side-\((S+22)\) enlargement with parameter \(w\), \(|J(U_+)|\le L^2w\), \((S+18)L^3w<c_{\rm rg}\) and \(4L^3B_*(S+18)w\le a_{\rm FH}\); that \(|\partial U_+-I|<a_0\eta^2\) on every plaquette; and that
\[
 w<a_0,\qquad L^2w<j_0 .                                                         \tag{6.6}
\]
Then \(P_W\in\mathrm{R4}(\mathbb T;a_0,a_1,j_0)\), with the box gauges supplied by cp12 Theorem 7. With hm (24) (\(L^2(1+C_{\rm pot}M)a_0<h/16\)), \(P_W\) is in hm's working domain.

*Proof.* \(A'=0\) gives \(|A'|=|\nabla^UA'|=0<a_1\) and \(\mathbf U=U_+\), so both defect clauses are the one assumed. \(|J|\le L^2w<j_0\). cp12's PR1 application (L339–345): Q on the side-\((S+16)\) cube supplies cp12 (8) with \(a=4L^3B_*(S+18)w\); then FH "supplies the **real** part of bx-fix (H), with \(C_{\rm pot}=4L^3B_*(C_{\rm box}L+18)\max(C_F,C_{F,\alpha_{\rm H}})\) and bound \(C_{\rm pot}Mw\)". By (6.6), \(C_{\rm pot}Mw<C_{\rm pot}Ma_0\), which is R4's box clause. hm (24) is then the working-domain ceiling (10). \(\square\) *Status: proved*, as an implication from PR-lay Q (import) and cp12 Theorem 7. Supplying Q and the curvature bound for the actual physical backgrounds of every history, with \(w\to0\) along the run, is DOM/BG1 (assembly-status §3 item 5), together with cp12's own caveat (L345): "This does not manufacture a missing seam gauge or margin. The complex part of (H), actual current supply and RCG4's F0 premise remain imports."

## 7. Order of constants (IN1 rows 1–10, with Amendment 1)

IN1's rule (L223): "A returned constant must precede every choice it bounds. The imported floors and ceilings must be uniform over the earlier admissible choices." Every constant below is uniform in depth, volume, torus, region shape and history, because each comes from a fixed finite stencil or from hm/descent's early constants, which have that uniformity (hm L49; descent L97).

| IN1 row | Constants of this note, and where each is fixed | Depends on |
|---|---|---|
| 1 | none new | — |
| 2 | odd \(L\ge27\), \(L>L_0^\natural\) (Amendment 1); \(c_g\), \(C_{\rm box}\); AV branch data \(\rho_{\rm AV},G_{\rm AV}\) and the Y-form bound \(G_{\mathsf b}\) (descent Lemma 2, "early bound"); (PIV) \(\rho_{\rm piv},C_{\rm piv},r_{\rm piv}\); hence \(\rho'\), \(F_*\), \(N_{\rm st}\), \(N_{\rm ov}\) of §4, and the indicator constant \((1+G_{\rm AV}^2)/\rho'\) of Lemma 4.2. cp12's \(a_{\rm FH}\) (absolute) and \(C_{\rm pot}\) (from \(L,C_{\rm box},B_*\)). | \(L\) and branch data only. Raising \(L\)'s floor (Amendment 1) recomputes them; \(L\) precedes all, so no cycle. |
| 3 | R, W: \(c_L,a_R,a_h,C_h,\delta_h\); \(M_1,R_1,\rho=R_1M_1\); hm Lemma 1's \(W,\mu_W,R_h\), enlarged to cover the Y gauge labels (descent L70); \(h,H_1,r_{\rm loc}\) (hm (7)); \(\ell_{\rm IMS},b_{\rm tail},b_{\rm gap}\) (hm Lemma 4); \(a_s,b_s,\Lambda_{\rm res},q_*,p_{r_c},r_c,\theta,n,R_*,U_{\rm root}\) (hm (12)–(13)). **New here:** \(c_b\le3\); the rooted vacuum constant \(2c_bp_{r_c}\) and its Lipschitz constant \(4c_bp_{r_c}/r_{\rm loc}\) (5.5); \(C_{\rm hull}=2(2R_*+3)^4\); \(C_{\rm vac}=48n_cc_bp_{r_c}e^{1/4+\theta R_*/2}\) (5.6). P82/P81/a3-derivative constants used by Lemmas 6.1–6.4 (cp12 L29: "fixed at IN1 row 3"). G-ID (§6) introduces no constant. | rows 1–2 |
| 4 | \(K_0,H_0,b=32,d=\theta/4,C_\tau,H_p\equiv L^3\) (descent (5)); \(A=A_{K_0},\varepsilon_0,\zeta_0\) (IN1's \(\rho_0\)), \(c_m=12\), \(P_d\), \(D_0=Ac_mL^4\), \(W_0\) (descent (6)); UM's rates \(\lambda_V>\lambda_0>\kappa_f\) (SA 14485–14487, UM9) — the gauge type accepts any \(\lambda_V\) at the cost \(e^{32\lambda_V}\) in \(a_{\rm GF}\). Then \(\kappa\ge\kappa_0^\natural(L)\), \(\Theta\), \(\lambda\). | rows 1–3; **before \(\kappa\), independent of \(M,\bar\kappa\)** |
| 5 | \(\bar\kappa>\log2\) and its floors; then \(M\), a power of \(L\), above: hm (23); \(M\ge2L+2r_{\rm piv}+2\) (Theorem 4.3(1)); \(LM\ge\max(4\kappa C_{\rm hull}/\theta,8/\theta)\) (Theorem 5.2 (V5)); descent (8)'s floor \(H_0e^{32\bar\kappa-dM}\le\varepsilon_*/2\). | all floors; the vacuum floor follows \(\kappa\) |
| 6 | \(\varepsilon_*,\gamma_{\rm tilt}\) (descent (8)); \(A_1\), then \(A_0>2(1+G_{\rm AV}^2)A_1/\rho'\) (Lemma 4.2); radii \(a_0,a_1,j_0\) with descent (7) and (8); \(|\tau-1|\le1/2\) and (8). | after \(M\) |
| 7 | \(E_N\) etc.: the vacuum part of \(E^{(k+1)}\) contributes \(C_{\rm vac}(LM)^4\) per cube (Remark 5.3); this is a row-7 quantity (after \(M\)) and changes no earlier constant. | after \(M\) |
| 8 | none new | — |
| 9 | coupling ceilings: \(\delta_j\le\rho'/2\) (Lemma 4.2, Theorem 4.3); \(a_{\rm GF}(\theta)=e^{32\lambda_V}F_*\rho'^{-3}N_{\rm ov}M^4\delta_j\le W_0/4\) (Theorem 4.3(4)); Lemma 6.10's \(w<a_0\), \(L^2w<j_0\), \((S+18)L^3w<c_{\rm rg}\), \(4L^3B_*(S+18)w\le a_{\rm FH}\) for the actual field size \(w\to0\). Each is met by increasing \(X_0\). | after everything |
| 10 | none new | — |

No constant of this note bounds an earlier choice. The two quantities that carry \(M\) explicitly, \(a_{\rm GF}\propto M^4\delta_j\) and \(C_{\rm vac}(LM)^4\), enter only row-9 ceilings and row-7 bounds. The H-M envelope constants are exactly descent's (5), as Theorem 3.2 states.

## 8. What stays open, for the lead, and what frozen texts say wrongly

### 8.1 Inputs owned by other items

None of these is an item-6 statement. Each is quoted with its owner.

1. **P81/P82 at the physical background** (PH1, PH2). cp12 L25: D3 "does not construct backgrounds or admit actual histories". Owners: BG1/A1 (P81); P82 is frozen, conditional on I1–I8 (assembly-status L47). Item 1 (P82M) is closed conditionally by frozen cp12.
2. **Operator and pivot existence** (PH3, PH4): W and AV, imports of frozen pr-lay and hm.
3. **DOM** (item 5): (i) every CI-maps domain of nl1-L Theorem 7 and every ST1 chain domain lies in \(\mathrm{R4}(Z;a_0,a_1,j_0)\) with descent (7) (descent L285: "Nor does this note put every ST1 chain domain inside this R4 domain"); (ii) the hypotheses of Lemma 6.10 (PR-lay Q with \(w\to0\), the curvature and current bounds) at the physical backgrounds of every history.
4. **(UM1-rest)** (item 8, CI): UM1 for the non-gauge potential types with total norm \(\le W_0/4\), on their declared boxes and cores (ci-form H-C, H-W, TD, H-F; nl1-L Theorem 7 CI-form).

In dependency order, the first of these that blocks the use of this note's Theorem 3.2 inside CI is DOM (i).

### 8.2 Consistency items created by D-Y3 (for the lead; not item-6 clauses)

1. carrier-adopt Theorem A (kept forms) re-read with Y labels and (A2) at \(a=5c_L/8\), \(b=W\) (Remark 3.4(2)). Argued, not checked.
2. FINISH row 278 adds "pr-lay under the relative form off Rep" to the path. Descent Lemma 4 gives hm's estimates for the Y labels on \(\mathcal K\), and the conjugation of descent L229–233 transports operator norms, real parts and accretivity to all of R4. Pr-lay Theorem 3's *entrywise* bounds (15) transport in bond-block form (the conjugation is block diagonal and orthogonal), with the scalar conversion factor \(c_b\le3\). So pr-lay Theorem 3 for \(\mathsf A^{\rm Y}\) holds on all R4 in bond-block entries. Argued here; a distiller should write it out.
3. Tests that read the soft-gauge factor at a non-axial real reference, if any (Remark 3.4(3)).

### 8.3 Statements in frozen texts that are wrong, stale or misleading

1. **IN1 L106**, "agrees at physical parameters with the actual fluctuation law". Read literally this is false: the actual fluctuation law at physical parameters is not Gaussian. SA 14215–14217: "it does not assert a Gaussian law for the full nonlinear averaging disintegration." The correct clause is hm L45's "the Gaussian part of the actual step has covariance \(\mathsf A(P_W)^{-1}\)". No step of IN1 uses the literal reading: Theorem 11's proof (L571) uses Lemma 3 for the UM budget, and Lemma 3 reads only the numerical clauses. **Wording; harmless; should be corrected at the next touch of IN1.**
2. **hm L47 and L482 ("F for the completed gauge form").** Under D-Y3, F is vacuous: \(J^{\rm Y}_{\rm GF}\equiv0\) (Lemma 4.1), so the completed form equals (7). Not wrong; moot after the lead's decision.
3. **hm L45** cites "SA 14108–14118"; the sketch is SA 14109–14120 (its last sentence, on soft gauge fixing, ends at 14120). Trivial.
4. **IN1 L108's note** that carrier-adopt §6 / inv-root "may make this item smaller": answered by Remark 3.3(2). inv-root's series uses a global gap and is not the step's UM series; hm's grouped series is.
5. **Stale:** FINISH row 274 says "descent (distilled)"; descent is frozen (row 275). Assembly-status §4 item 2 says "Which form 'the actual step' uses is not decided"; FINISH row 278 decided it.
6. **Notation:** IN1 L106 and L340 write the Gaussian tilt as \(\rho,\rho_0\); hm and descent use \(\zeta,\zeta_0\), because \(\rho=R_1M_1\) in pr-lay (descent change log item 2, L291). Same quantity.
7. **SA 10335** ("it is gauge covariant") for the walk terms of \(\chi_Y\mathsf A\chi_Y\): under the absolute reading this cannot hold together with agreement on \(\mathcal K\) and the real tie (descent Proposition C); under D-Y3 it holds after colour grouping (descent Lemma 4). This is not a defect claim against SA (descent correction 8, L314); it records which reading makes SA's sentence true.

I found no statement in a frozen text that this note contradicts.

## 9. Checks against failure

Pass 1 must look for counterexamples, not only proofs. These are the places where a step could have failed, and what I checked.

1. *Does the cubic gauge remainder really vanish in the UM norm?* The remainder is cubic in the unnormalized fluctuation, \(O(x|u|^3)\); on the box this is \(O(\delta_j|b|^2)\) (Theorem 4.3), and \(\delta_j\to0\). If the box had been in normalized units of size \(O(1)\) without the factor \(g_j\), the bound would be \(O(x^{-1/2}\mathfrak b|b|^2)\), still \(\to0\). No failure.
2. *Could the gauge gradient be nonzero off the axial locus, as for the absolute form?* No: the relative contour is \(I\) at \(D=0\) at every reference, so each summand's gradient vanishes (Lemma 4.1). This is exactly where the absolute form needs F.
3. *Could SA's explicit \(\Delta'_\pi\) differ from the gauge identity at the physical current?* This would have broken G-ID (pr-lay (7) uses the explicit form). I computed the gauge generator to first order (Lemma 6.2(ii)) and matched all six terms of SA 10172–10185; the two \(\eta\)-terms cancel by antisymmetry. No failure.
4. *Could SA's Schur complement \((QG_1Q^{\mathsf T})^{-1}-\mathsf a\) differ from the datum Hessian because \(G_1\) sandwiches by \(\mathsf S\)?* Only if the datum solution left the Landau slice or the gauge directions left the constraint fibre. [A3] (37) keeps it in the slice, and Lemma 6.3 shows \(K_0\mathsf S=K_0\). No failure.
5. *Could the vacuum terms fail to be local because the grouped entries use compressions?* The compressions are to balls inside the hulls, with the \(b_{\rm gap}\) margin inside the hull (hm L198). No failure.
6. *Could G-ID fail at non-axial physical pairs?* With the absolute form it does fail (Remark 6.8: descent's flip). With D-Y3 it holds (Corollary 6.7). This is the content of the lead's decision.

## 10. Result

Under the lead's design decision D-Y3 (FINISH row 278), and conditional on the named imports, this note proves the three parts of critical-path item 6:

- **(a)** Theorem 3.2 with Lemma 3.0: the actual step's localized Gaussian functional and its carriers are the full-read family of frozen hm/descent with Y labels; it is determined by the step's data alone; and it supplies IN1 H-M's clauses HM-0–HM-4 (with \(K_0,H_0,b=32,d=\theta/4,C_\tau\) before \(\kappa\), \(H_p\equiv L^3\), \(c_m=12\)), NL1's CI-Gauss, ci-form's H-G/H-S Gaussian half and td's J on every pair of \(\mathrm{R4}(Z;a_0,a_1,j_0)\) with descent (7). IN1 Lemma 2's family and inv-root's series are not the step's (Remark 3.3).
- **(b1)** Lemma 4.1 (no completed-form correction: F vacuous), Lemma 4.2 (gauge indicator \(\equiv1\) on the box), Theorem 4.3 (UM1 for the gauge-type potential, \(a_{\rm GF}\le e^{32\lambda_V}F_*\rho'^{-3}N_{\rm ov}M^4\delta_j\to0\)), Lemma 4.4 (no other potential type changes; no switch is made, so descent Lemma 7's obstruction does not arise), Corollary 4.5 (UM4–UM6, UM14, \(C_0^{\rm UM}\le1\) with early \(W_0\), and UM16 for the actual gas, given (UM1-rest)).
- **(b2)** Theorem 5.2: the step's Gaussian normalizer \(-\tfrac12\log\det\mathsf A^{\rm Y}\) has a local assignment \(\mathbf N(X;P)\) on level-\((k+1)\) cube polymers, hereditary, holomorphic at fixed \(U\), real, gauge invariant, with the early rooted bound \(2c_bp_{r_c}\), the Lipschitz bound \(4c_bp_{r_c}r/r_{\rm loc}\) and the polymer bound \(C_{\rm vac}(LM)^4\) under the floor \(LM\ge4\kappa C_{\rm hull}/\theta\).
- **(c)** Theorem 6.6 and Corollaries 6.7, 6.9: G-ID(cov), the physical clause, at every admitted complete physical pair in R4: the step's Gaussian part has precision \(\mathsf A^{\rm Y}(P_W)\) (equal to SA's precision at the block-axial representative), and hm/descent's local functional at \(s=\mathbf1\) is its marginal. The proof supplies SA's "only step of substance" (SA 10208–10210) from a3-derivative §6, cp12 Lemma 1, and two lemmas proved here: the gauge identity for SA's explicit \(\Delta'_\pi\) (Lemma 6.2) and the constraint-fibre property of gauge directions (Lemma 6.3). Lemma 6.10 reduces physical admission to the working domain to PR-lay Q and cp12 Theorem 7.
- **Constants:** §7 places every constant in IN1's rows; nothing new precedes a constant it depends on.

**Imports** (none proved here): R, W, AV, W-cov, PF, FG/UM (frozen hm, descent); P81 and P82 through a3-derivative §6 with its gate repairs (as imported by frozen cp12); (PIV); PR-lay Q for Lemma 6.10. **Remaining open inputs, all owned elsewhere** (§8.1): P81/P82 at the physical backgrounds; DOM, of which the first is the inclusion of the CI domains in \(\mathrm{R4}\) with radii (7); and (UM1-rest) of item 8. TP1's G-ID(TP) (tp1 L130) is a different statement and is not supplied.

**Definitions supplied:** the reading D-Y3 (relative exponent, relative indicator, Y precision, assigned UM family); Lemma 2.1's transported-absolute characterization and its uniqueness; the step's Gaussian carriers; the gauge-type potential (4.1)–(4.2); the Gaussian part of the step at a physical pair; the local vacuum terms (5.3) with bond-block entries and coarse filing sets; hypotheses PH1–PH4 and the normalization (N).

This text is pass 1: not distilled, not refereed, and it grants no status.
