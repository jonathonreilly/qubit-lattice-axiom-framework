# Descent for H-M: from the representative class to every R4 triple

Provenance: Claude (Opus 5.5, `claude-opus-5-5`), pass 1 (long draft), 2026-11-05; clone checkout `b003c05f25840a9362459fd875e9b47a47c4254a`. Research text, not an audit; it grants no status. It has not been distilled or refereed. All arguments are hand proofs. No step uses a computation.

**Credit.** The core R4–R6, the pair/splitting/tie conventions, the soft gauge functional, the precision (SA 14096–14102), the UM chapter and the 3D covariant gauge form (Y3 31522–31536) are Ethan Sussman and Levent Alpoge's text, with Claude and Codex as authors of that text. The averaging, axial gauges, background-field and walk methods are Tadeusz Bałaban's; Jonathan Dimock's expositions enter through h-walk. hm, pr-lay, h-walk, st1-r4, nl1-L and IN1 are library notes by Claude and Codex.

Sources (raw files at `31a47c543775`, read in bounded ranges): SA = `ym4.tex`, Y3 = `YM3_I.tex`. Line numbers below are raw-file lines. Library notes are cited by file and line in this clone.

---

## 0. Result

The question is whether hm's envelope (Theorem 7) and Corollary 13.1 hold at every triple of SA's R4, not only on \(\mathcal K=\mathrm{R4}\cap\mathrm{Rep}\). The answer depends on which soft gauge form sits in the precision.

1. **Counterexample (Theorem A).** With the absolute soft gauge Hessian of SA CF2 (SA 8436–8440, 7182) — the reading used by pr-lay (7), h-walk §2.1 and hm — the literal precision fails the real gap at an R4 triple with the same radii. The triple is the flat field after the central gauge \(-I\) at one non-centre site of one block. There \(\mathsf A(P_0^w)(b_\lambda,b_\lambda)=-\mathsf A(P_0)(b_\lambda,b_\lambda)\le-c_L|b_\lambda|^2\). So hm's (25) fails there and FG1 has no positive real reference. Route (a) as phrased (conjugacy of the literal matrices) is false: the two spectra differ. Conditional on R, the covariance clause of W, and G-ID at the flat pair.

2. **Descent proved (Theorem B), by route (a) after one change of definition.** Replace the absolute form by Y3's covariant gauge form \(\mathsf G^{\rm Y}_V\) (Y3 31522–31536). It equals the absolute Hessian at every axial \(V\), hence at every real Rep reference and every physical pair in SA's axial convention (SA 11239–11241). With it, every walk label is covariant under every real site gauge. Every R4 triple has a canonical real Rep representative with the same radii (Lemma 2). Transport then gives hm's Theorems 7–8 and Corollary 13.1 at **every** triple of \(\mathrm{R4}(Z)\), hence of SA's hereditary core, with the **same early constants**. The family is real-gauge covariant. At \(s=\mathbf 1\) it depends only on the pair. No complex gauge is used, so SA 5733–5736 (non-saturation under complex gauges) does not apply.

3. **No-go (Proposition C).** No all-R4 family can at once agree with hm's literal family on \(\mathcal K\) at \(s=\mathbf1\), satisfy the real tie, and be real-gauge covariant. NL1 and ST1 require the last two (nl1-L 585–587; st1-r4 120). So hm's family must change on \(\mathcal K\). The change is the one in item 2. It moves \(\mathcal K\)'s matrices only inside hm's envelope.

**What the contribution can claim.** See §9. In short: H-M (IN1 (9)) and UM4–UM6, UM14 with \(C_0^{\rm UM}\le1\) and \(W_0\) fixed before \(\kappa,\bar\kappa,M\), at every triple of SA's R4 (so at every declared complex input pair of their core), for the precision with Y3's gauge form. This is conditional on hm's imports (R, W with (I1)–(I3), AV, FG/UM), on h-walk's surviving covariance clause, and on G-ID for the physical clause.

**First remaining Outstanding.** Inside the target: none beyond those imports. Outside it, for the real tie at \(s\ne\mathbf1\): **PF-label** (§10). Each walk label depends on a triple only through its pair on its hull. Three attacks are recorded there.

---

## 1. What the sources say (quoted before use)

| Lines read | Short quote | What it states |
|---|---|---|
| SA 5665–5670 | "A triple is a splitting of its pair." | Triple \(P=(U,A',\mathbf J)\), \(U\) real; pair \((\mathbf U,\mathbf J)\), \(\mathbf U=e^{i\eta_jA'}U\). |
| SA 5673–5684 | "in the real gauges described below" | R4: plaquette defects of \(U,\mathbf U\) below \(a_0\eta_j^2\); \(|A'|,|\nabla_UA'|<a_1\); \(|\mathbf J|<a_2\); on boxes of side \(\le C_{\rm box}LM\) a real gauge with \(|A|,|\nabla A|<C_{\rm pot}Ma_0\). No gauge condition on \(U\). |
| SA 5696–5721 | "These are quantifiers over every allowed \(Z,p,n\)" | R5–R6 tower conditions; the hereditary core is R4–R6. |
| SA 5724–5736 | "The core itself is not saturated by complex gauge transformations." | The tie (agreement at two splittings), gauge invariance of activities, and the non-saturation warning for **complex** gauges. |
| SA 5654–5662 | "the background input is a regular critical orbit" | The background is an orbit; representatives and gauge are part of the input. |
| SA 7178 | "the Hessian at the minimum vanishes" | Without gauge fixing, \(3(L^4-1)\) block-gauge directions per block are zero modes. |
| SA 7182 | \(\mathrm{GF}_k(V)=\sum_{y,x}[1-\tfrac12\operatorname{Re}\operatorname{tr}V(y,x)]\) | Absolute soft gauge functional. |
| SA 8436–8455 | "For a gradient, \(\gamma_{y,x}(df)=f(x)-f(y)\)." | CF2–CF3: at the identity, \(\mathrm{GF}(e^{ita})=\tfrac12t^2\|Ga\|^2+O(t^3)\); internal paths contain no crossing pivot. |
| SA 10139 | "Relative to \(\mathbf U\), the straightened \(j\)-fold average" | Rows \(Q\), site map \(Q'\) and \(\Delta^{\rm W}\) are formed at the complex field. |
| SA 10166 | "All operators are formed at the same reference \(\mathbf U\)" | The operators of (6) are functions of the pair. |
| SA 10200 | "the quadratic part of the soft axial gauge fixing" | Definition of \(\mathsf G^{(2)}_V\) in the 4D precision; the functional is not restated there. |
| SA 11236–11247 | "An absolute contour gauge and its relative version can have different derivatives away from the axial locus" | PX104; the physical step uses \(V\) in block axial gauge (11239–11241). |
| SA 14093–14102 | "Let \(P=(\mathbf U,\mathbf J)\) be a regular complex pair." | \(\mathsf A(P)=\mathsf C_V^{\mathsf T}(\mathrm{GF}^{(2)}_V+\Delta_k(P))\mathsf C_V\), \(V=\mathcal M^k\mathbf U\). |
| SA 14108–14120 | "on which the critical action has zero Hessian" | At \(P_W\) the form is the fibre Hessian of \(A\circ U_k+\mathrm{GF}_k\); soft gauge supplies positivity on orbit directions. Sketched. |
| SA 14122–14150 | "and then, in this gauge, with the flat operator" | The gap sketch; at 14144 it asserts \(\operatorname{Re}\mathsf A(P)\ge\tfrac12\gamma_0\). |
| SA 14373–14412 | "uniformly on independent coarse parameter discs" | UM4–UM6 and the structural hypotheses (heredity, normalization, wall factorization). |
| SA 14776–14786 | "One must verify (UM4)--(UM6) and (UM14)" | The simultaneous-choice recipe; no assertion for an uncontrolled family. |
| Y3 31522–31536 | \(\mathsf b_V(B)(y,x)=\frac1i\frac d{ds}\big|_0\log((e^{isB}V)(y,x)V(y,x)^{-1})\) | Y3's gauge form \((B_1,\mathsf G^{(2)}_VB_2)=\sum\langle\mathsf b_V(B_1),\mathsf b_V(B_2)\rangle\). |
| Y3 31554–31564 | "\(T_Y=\mathsf C^{\mathsf T}(\mathsf G_V^{(2)}+\Delta_k)\mathsf C\)" | Y3's precision uses that form. |
| hm 33, 35, 37 | "R4, and the additional R5–R6 conditions ... do not imply Rep." | \(\mathcal K\) = R4 ∩ Rep; Rep is averaged-contour block axiality; the all-core gap is Outstanding. |
| hm 106–117 | "This algebraic identity holds for arbitrary real site gauges" | Lemma 3: nonlinear covariance (8) of \(\mathcal M^k\) and of averaged contours. |
| hm 494 | "activity gauge invariance does not supply descent" | The first Outstanding of hm. |
| pr-lay 60 | "Full gauge covariance of the soft gauge Hessian is not asserted." | Fixed representative. |
| h-walk 69 | "Full gauge covariance of the terms is impossible" | §2.1: the absolute \(G^{(2)}_V\) is not covariant. |
| h-walk 378 | "A^G_ω and A^E_ω are covariant under every gauge transformation" | (H3), given (I2); \(A^{\rm loc}_\kappa\) only under block-constant gauges. |
| h-walk-gate 22, 108 | "Translations and gauge covariance of the algebraic construction survive" | The covariance clause survives the gate; 2.1's sign corrected. |
| st1-r4 120 | "Require simultaneous real gauge covariance and equality at two real splittings of one pair." | ST1's activity interface. |
| nl1-L 578–587 | "on these full complex domains" | CI-Gauss needs H-M on whole domains; CI-form preserves real ties and covariance. |

The 4D text does not restate the functional behind \(\mathsf G^{(2)}_V\) at SA 10200. pr-lay (7), h-walk §2.1 and hm read it as the Hessian of CF2. Theorem A uses that reading. Theorem B uses Y3's form. Both readings agree at axial \(V\) (Lemma 5(b)).

---

## 2. Definitions

**2.1 Triples and real gauges.** Use hm §1's geometry, units and norms. A real site gauge is a map \(g\) from bare sites to \(SU(2)\). It acts on triples by
\[
 U^g(b)=g(b_-)U(b)g(b_+)^{-1},\quad A'^g(b)=\operatorname{Ad}(g(b_-))A'(b),\quad
 \mathbf J^g(b)=\operatorname{Ad}(g(b_-))\mathbf J(b).                   \tag{2.1}
\]
Then \(\mathbf U^g=e^{i\eta A'^g}U^g\) is the gauge transform of \(\mathbf U\), and the pair transforms as in SA 7174. Composition is \((P^{g_1})^{g_2}=P^{g_2g_1}\). On free coordinates write \(\mathcal G=\operatorname{Ad}(g)\) at each base point. It is real orthogonal on the three colour coordinates of each bond and commutes with every coordinate projection \(\chi_S\) whose set \(S\) is a set of base points.

A **central gauge** takes values in \(\{\pm I\}\). Then \(\mathcal G=\mathrm{id}\), since \(\operatorname{Ad}(-I)=\mathrm{id}\).

**2.2 Blocks, contours, Rep.** Level-\(k\) sites are bare sites. A next-level block \(b\) has centre \(y_b\) and \(L^4\) level-\(k\) sites. Write \(V=\mathcal M^kU\) and \(c_b(V;x)=V(y_b,x)\), the averaged contour (hm 35). Let \(\mathfrak B(Y)\) be the set of active next-level blocks whose complete averaging read neighbourhood lies in \(Y\). **Rep on \(Y\)** means \(c_b(\mathcal M^kU;x)=I\) for all \(b\in\mathfrak B(Y)\) and all level-\(k\) \(x\in b\) (hm 33). A **residual gauge** for \(Y\) is a real site gauge with \(g(x)=g(y_b)\) at every level-\(k\) site \(x\) of every \(b\in\mathfrak B(Y)\). It is arbitrary at other bare sites.

**2.3 The two gauge forms.** For a level-\(k\) field \(V\) on its regular branch, a block \(b\), a level-\(k\) site \(x\in b\setminus\{y_b\}\) and a small bond field \(D\), put
\[
 W_x(D)=(e^{iD}V)(y_b,x),\qquad \widehat W_x(D)=W_x(D)W_x(0)^{-1}.          \tag{2.2}
\]
Write \(\langle X,Y\rangle=\tfrac12\operatorname{tr}(XY)\), bilinear, and \(|X|^2=\langle X,X\rangle\) for Hermitian \(X\).

* The **absolute form** \(\mathsf G^{\rm abs}_V\) is the Hessian at \(D=0\) of
\(\Phi^{\rm abs}_V(D)=\sum_{b,x}[1-\tfrac12\operatorname{tr}W_x(D)]\).
On real fields and real \(D\) this is CF2 (SA 8436–8440), since \(\operatorname{tr}\) is real on \(SU(2)\). Its holomorphic continuation replaces \(\operatorname{Re}\operatorname{tr}\) by \(\operatorname{tr}\).
* The **Y3 form** \(\mathsf G^{\rm Y}_V\) is defined by
\[
 (D_1,\mathsf G^{\rm Y}_VD_2)=\sum_{b}\sum_{x\in b\setminus\{y_b\}}
   \langle\mathsf b_V(D_1)(x),\mathsf b_V(D_2)(x)\rangle,\qquad
 \mathsf b_V(D)(x)=\tfrac1i\tfrac d{ds}\big|_{0}\log\widehat W_x(sD).      \tag{2.3}
\]
This is Y3 31522–31536, read in the 4D block geometry. A different fixed normalization of the pairing only rescales the form; Lemma 5(b) fixes this one.

Let \(\mathsf A^{\rm abs}(P)\) and \(\mathsf A^{\rm Y}(P)\) be pr-lay (7) with \(K_{\rm GF}\) replaced by \(\mathsf G^{\rm abs}_V\) and \(\mathsf G^{\rm Y}_V\), respectively, \(V=\mathcal M^k\mathbf U\). Write
\[
 \mathsf A^\bullet(P)=X(P)+\mathsf C_V^{\mathsf T}\mathsf G^\bullet_V\mathsf C_V,\qquad \bullet\in\{\rm abs,Y\}.  \tag{2.4}
\]
Here \(X\) collects everything except the gauge form. In h-walk's decomposition (h-walk 365–372) this is the sum of all \(A^G_\omega\), \(A^E_\omega\) and of \(\theta_\kappa\mathsf C_V^{\mathsf T}(-\mathsf a)\mathsf C_V\). hm's family is the \(\rm abs\) family on \(\mathcal K\). Let **hm\(^{\rm Y}\)** denote hm's construction (9)–(21) with \(\mathsf A^{\rm Y}\) in place of \(\mathsf A^{\rm abs}\), labels for \(\mathsf G^{\rm Y}\) placed in \(A^{\rm loc}_\kappa\).

**2.4 Imports.** All of hm's imports, unchanged: R, W (h-walk (I1)–(I3), Lemma U, h-walk-gate §§5–8), AV, FG/UM, and G-ID for the physical clause. In addition:

* **W-cov.** The covariance clause of h-walk (H3) (h-walk 378): given (I2), \(A^G_\omega\), \(A^E_\omega\) and \(\mathsf C_V\) are covariant under every real gauge, and the construction is covariant under block-constant gauges. h-walk-gate 108 records that this survives "when the translated data include all cutoff read sets". It is part of W's (I2)–(I3), but hm did not use it.
* **PF.** The operators of (6)–(7) are functions of the pair \((\mathbf U,\mathbf J)\) (SA 10166). Used only for ties.
* **G-ID(flat).** G-ID at the flat pair \(P_W=(I,0)\): there \(\mathsf A^{\rm abs}\) is the fibre Hessian of \(x_k(A\circ U_k+\mathrm{GF}_k)\) (SA 14108–14118; also SA 10208–10209). Used only in Theorem A.

---

## 3. Real gauges and the core

**Lemma 1 (exact real-gauge invariance of R4).** For every real site gauge \(g\), \(P\in\mathrm{R4}(Y;a_0,a_1,j_0)\) iff \(P^g\in\mathrm{R4}(Y;a_0,a_1,j_0)\). Also \(r_Y(P^g)=r_Y(P)\), and \(P\in\mathcal R_{\rm loc}(Y;\alpha)\) iff \(P^g\in\mathcal R_{\rm loc}(Y;\alpha)\).

*Proof.* A plaquette holonomy based at \(x\) changes to \(g(x)\,\partial U(p)\,g(x)^{-1}\). Unitary conjugation preserves the operator norm, so \(|\partial U^g(p)-I|=|\partial U(p)-I|\). The same holds for \(\mathbf U\). Also \(|\operatorname{Ad}(g)A'|=|A'|\) and \(|\operatorname{Ad}(g)\mathbf J|=|\mathbf J|\). For the covariant derivative (hm (2)),
\[
 \operatorname{Ad}(U^g_\nu(x))A'^g_\mu(x+\eta e_\nu)
 =\operatorname{Ad}(g(x))\operatorname{Ad}(U_\nu(x))A'_\mu(x+\eta e_\nu),
\]
so \(\nabla^{U^g}A'^g=\operatorname{Ad}(g(x))\nabla^UA'\) and its norm is unchanged. The reversal convention transforms the same way. If \(h\) is a real gauge on a box with \(U^h=e^{i\eta A}\), then \(hg^{-1}\) gives \((U^g)^{hg^{-1}}=U^h\) on that box, with the same \(A\). All inequalities are therefore preserved as equalities of the bounded quantities. Read stencils and boxes are geometric. The same argument gives \(r_Y\) and \(\mathcal R_{\rm loc}\). \(\square\)

**Status: proved.**

**Lemma 2 (canonical Rep representative).** Let \(P\in\mathrm{R4}(Y)\). Define \(u=u_Y(U)\) by
\[
 u(x)=c_b(\mathcal M^kU;x)\quad(b\in\mathfrak B(Y),\ x\in b\text{ level-}k),\qquad u=I\text{ elsewhere}.  \tag{3.1}
\]
Then \(u\) is real, depends only on \(U\) on the read neighbourhoods of \(\mathfrak B(Y)\), and \(P^u\in\mathcal K(Y;a_0,a_1,j_0)\) with the same radii. If \(U\) is Rep on \(Y\), then \(u=I\).

*Proof.* The contour means of \(\mathcal M^kU\) exist on their regular branch for these blocks: this is AV, which hm Lemma 3 already uses for fields with small curvature. They lie in \(SU(2)\) because \(U\) is real. The transport from \(y_b\) to itself is the empty path, so \(u(y_b)=I\). By hm (8), \(\mathcal M^k(U^u)=(\mathcal M^kU)^{u|_{\text{level-}k}}\) and
\[
 c_b(\mathcal M^kU^u;x)=u(y_b)\,c_b(\mathcal M^kU;x)\,u(x)^{-1}=I .
\]
So \(U^u\) is Rep on \(Y\). Lemma 1 gives R4 with the same radii. If \(U\) is already Rep, every \(c_b=I\), so \(u=I\). \(\square\)

**Status: proved, given AV (an hm import).** This answers route (a)'s representative question. Every R4 triple has a Rep representative in its **real** gauge orbit, with the core's own radii. Complex gauges are not needed, so SA 5733–5736 does not bite.

**Lemma 3 (gauges that preserve Rep).** If \(U\) is Rep on \(Y\), then \(U^g\) is Rep on \(Y\) iff \(g\) is residual for \(Y\).

*Proof.* By hm (8), \(c_b(\mathcal M^kU^g;x)=g(y_b)\,I\,g(x)^{-1}\). This equals \(I\) iff \(g(x)=g(y_b)\). \(\square\) **Status: proved.**

**Lemma 4 (equivariance of the canonical gauge).** For every real \(g\),
\[
 (U^g)^{u_Y(U^g)}=(U^{u_Y(U)})^{r},\qquad r=u_Y(U^g)\,g\,u_Y(U)^{-1},     \tag{3.2}
\]
and \(r\) is residual for \(Y\).

*Proof.* At a level-\(k\) site \(x\) of \(b\in\mathfrak B(Y)\), \(u_Y(U^g)(x)=c_b(\mathcal M^kU^g;x)=g(y_b)u_Y(U)(x)g(x)^{-1}\), so \(r(x)=g(y_b)\). Elsewhere both canonical gauges are \(I\) and \(r=g\). Use the composition rule. \(\square\) **Status: proved.**

**Remark 3.1 (R5–R6).** For the bounds below only \(P^u\in\mathcal K\) is used, not \(P^u\in\mathcal U^\circ\). For completeness: R6 reads curvature and current of tower configurations, which are orbit invariants. So real gauges preserve R5–R6 if the continued background \(\Phi_V(B)\) is covariant, \(\Phi_{V^v}(\operatorname{Ad}(v)B)=\Phi_V(B)^{\tilde v}\). SA 5654–5662 places this in the background input; st1-r4 Lemma 5 gives the canonical real representative and its continuation. **Status: conditional on that covariance, and not used.**

---

## 4. The two gauge forms under gauge transformations

**Lemma 5 (Y3 form).** On the regular branch:

(a) \(\mathsf G^{\rm Y}_V\) is the Hessian at \(D=0\) of
\(\Phi^{\rm Y}_V(D)=\sum_{b,x}[1-\tfrac12\operatorname{tr}\widehat W_x(D)]\), and the gradient of \(\Phi^{\rm Y}_V\) at \(0\) is zero, at every \(V\).

(b) If \(W_x(0)=I\) for all \(b,x\) in the stencil (axial \(V\)), then \(\mathsf G^{\rm Y}_V=\mathsf G^{\rm abs}_V\). In particular this holds at every real Rep reference \((U,0,0)\), on the blocks of \(\mathfrak B\).

(c) For every real level-\(k\) gauge \(v\), \(\mathsf G^{\rm Y}_{V^v}=\mathcal V\mathsf G^{\rm Y}_V\mathcal V^{-1}\), with \(\mathcal V=\operatorname{Ad}(v)\) on bond coordinates.

(d) \(\mathsf G^{\rm Y}_V\) is a finite analytic function of \(V\) with the stencil of its blocks, real at real \(V\). Its entries are bounded by a constant depending only on \(L\) and the branch. So (I3) holds with \(\mathsf G^{\rm Y}\) in place of \(\mathsf G^{(2)}\).

*Proof.* (a) Fix \(D\) and write \(\widehat W_x(sD)=\exp(iH(s))\), with \(H(s)=s\,\mathsf b+s^2\beta+O(s^3)\) traceless. For traceless \(H\in\mathfrak{sl}(2,\mathbb C)\), Cayley–Hamilton gives \(H^2=(\tfrac12\operatorname{tr}H^2)I\). Hence
\[
 \tfrac12\operatorname{tr}e^{iH}=\cos\sqrt{\tfrac12\operatorname{tr}H^2}=1-\tfrac14\operatorname{tr}H^2+O(|H|^4),
\]
where the cosine is the entire even series in \(\tfrac12\operatorname{tr}H^2\). Thus \(\Phi^{\rm Y}_V(sD)=\tfrac14s^2\operatorname{tr}\mathsf b^2+O(s^3)\). The linear term vanishes, and the second derivative is \(\tfrac12\operatorname{tr}\mathsf b^2=\langle\mathsf b,\mathsf b\rangle\). Polarization gives (2.3).

(b) If \(W_x(0)=I\), then \(\widehat W_x=W_x\), so \(\Phi^{\rm Y}_V=\Phi^{\rm abs}_V\). At a real Rep reference, \(V=\mathcal M^kU\) has \(c_b=I\) on \(\mathfrak B\).

(c) For a real level-\(k\) gauge, \((e^{iD}V)^v=e^{i\operatorname{Ad}(v)D}V^v\), because \(v\) acts at base points. Covariance of contour means is hm Lemma 3's argument: the mean equation conjugates and its regular solution is unique. It holds for complex fields, since the argument is algebraic. So
\[
 W^{V^v}_x(\operatorname{Ad}(v)D)=v(y_b)W^V_x(D)v(x)^{-1},\qquad
 \widehat W^{V^v}_x(\operatorname{Ad}(v)D)=v(y_b)\widehat W^V_x(D)v(y_b)^{-1}.
\]
The trace is invariant, so \(\Phi^{\rm Y}_{V^v}\circ\operatorname{Ad}(v)=\Phi^{\rm Y}_V\). Differentiate twice.

(d) \(\mathsf b_V(D)(x)\) is linear in \(D\). Its coefficients are derivatives of the contour mean, which reads only bonds of block \(b\) and is analytic on the branch (AV). On a fixed ball, Cauchy estimates bound them by a constant depending only on \(L\) and the branch radius. At real \(V\) and real \(D\), \(\widehat W\in SU(2)\), so \(\mathsf b\) is Hermitian and the form is real. \(\square\)

**Status: proved, given AV.** Thus Y3's form is the Hessian of the **relative** contour gauge at its own base point. This is the "relative version" of SA 11245–11247, taken relative to \(V\) itself.

**Lemma 6 (absolute form under a central flip).** Let \(w\) be the central gauge with \(w(x)=-I\) at one level-\(k\) site \(x\in b\setminus\{y_b\}\) and \(w=I\) elsewhere. Let \(K_x\) be the Hessian at \(0\) of the single term \(1-\tfrac12\operatorname{tr}W_x(D)\). Then
\[
 \mathsf G^{\rm abs}_{V^w}=\mathsf G^{\rm abs}_V-2K_x .                                   \tag{4.1}
\]
At axial \(V\), \(K_x(D,D)=|\gamma_{y,x}(D)|^2\), with \(\gamma_{y,x}\) of SA 8441–8446.

*Proof.* Since \(\mathcal W=\mathrm{id}\), \(e^{iD}V^w=(e^{iD}V)^w\). The \((y_b,x)\) contour of this field is \(w(y_b)W_x(D)w(x)^{-1}=-W_x(D)\). So that term becomes \(1+\tfrac12\operatorname{tr}W_x(D)=2-[1-\tfrac12\operatorname{tr}W_x(D)]\), and its Hessian changes sign. Every other contour has endpoint gauges \(I\) and is unchanged. At axial \(V\), \(W_x(D)=\exp(i\gamma_{y,x}(D)+O(D^2))\), and the expansion of Lemma 5(a) gives \(|\gamma|^2\). \(\square\) **Status: proved.**

---

## 5. Theorem A: the literal family fails at a central flip

**Lemma Z (orbit zero mode at the flat pair).** Let \(P_0=(I,0,0)\) on the torus. Fix an active block \(b\) deep in \(\Omega_{k+1}\), and \(x=y_b+e_1\) in level-\(k\) units. All eight level-\(k\) bonds at \(x\) are internal to \(b\), hence non-pivot (SA 8452). Let \(\lambda=e\,\delta_x\), with \(e\) Hermitian, \(|e|=1\). Let \(b_\lambda\) be the free part of \(D_I\lambda\). Then \(\mathsf C_Vb_\lambda=D_I\lambda\), and, under G-ID(flat),
\[
 X(P_0)(b_\lambda,b_\lambda)=0 .                                                       \tag{5.1}
\]

*Proof.* \(D_I\lambda\) is supported on the eight internal bonds at \(x\), so its pivot components are zero. Since \(\lambda\) vanishes at all next-level sites, hm (8) gives \(\mathcal M(V^{e^{it\lambda}})=\mathcal M(V)\). Differentiating, \(D_I\lambda\) lies in the kernel of the linearized constraint. That kernel is the graph of the pivot map, so \(\mathsf C_Vb_\lambda=D_I\lambda\).

By G-ID(flat), \(\mathsf A^{\rm abs}(P_0)\) is the fibre Hessian of \(f+x_k\mathrm{GF}_k\) at \(V=I\), where \(f(V)=x_kA(U_k(V))\). Since \(\mathrm{GF}_k\ge0=\mathrm{GF}_k(I)\), its gradient at \(I\) is zero and its fibre Hessian is \(\mathsf C^{\mathsf T}\mathsf G^{\rm abs}\mathsf C\) in the same normalization. So \(X(P_0)\) is the fibre Hessian of \(f\).

\(f\) is invariant under real level-\(k\) gauges: the constraint set for \(V^v\) is the gauge transform of that for \(V\) (hm (8)), the Wilson action is invariant, and the background is an orbit (SA 5654). Also \(f\ge0=f(I)\), because the Wilson action is nonnegative and vanishes at \(I\). So \(I\) is a minimum and the chart gradient of \(f\) is zero. The curve \(t\mapsto I^{e^{it\lambda}}\) stays in the fibre, and its chart preimage has tangent \(b_\lambda\) (up to the sign convention of \(D\)). \(f\) is constant on it. Hence
\[
 0=\tfrac{d^2}{dt^2}f=\operatorname{Hess}f(b_\lambda,b_\lambda)+\nabla f\cdot b''(0)=X(P_0)(b_\lambda,b_\lambda). \qquad\square
\]

**Status: proved, conditional on G-ID(flat)** and on the \(C^2\) chart regularity included in it. SA asserts the same zero mode at 7178 and 14119–14120.

**Theorem A (central-flip counterexample).** Read \(\mathsf G^{(2)}_V\) as \(\mathsf G^{\rm abs}_V\). Let \(P^w=(I^w,0,0)\), with \(w\) as in Lemma 6 at the site \(x\) of Lemma Z. Assume R, W, W-cov and G-ID(flat). Then:

1. \(P^w\in\mathrm{R4}(Y;a_0,a_1,j_0)\) for every \(Y\) and all radii, and \(P^w\in\mathcal R_{\rm loc}\). Rep fails at \(b\).
2. \(\mathsf A^{\rm abs}(P^w)=\mathsf A^{\rm abs}(P_0)-2\mathsf C_V^{\mathsf T}K_x\mathsf C_V\).
3. \(\mathsf A^{\rm abs}(P^w)(b_\lambda,b_\lambda)=-\mathsf A^{\rm abs}(P_0)(b_\lambda,b_\lambda)\le-c_L|b_\lambda|^2\).
4. For every \(Y\supset N_{b_{\rm gap}}(x)\) and every \(S\ni x\) with \(N_{b_{\rm gap}}(S)\subset Y\), \(\chi_S\mathsf A^{{\rm abs},Y}(P^w)\chi_S\) has a unit vector with real quadratic form at most \(-\tfrac78c_L\). The same holds with real part at most \(-\tfrac34c_L\) for complex \(P\) on the fibre of \(U=I^w\) with \(r_Y(P)<r_{\rm loc}\).
5. hm (25) fails at \(P^w\): the reference \(C_*=(\chi\mathsf A^{{\rm abs},H}(P^w_0)\chi)^{-1}\) is not positive definite, or does not exist. FG1 then has no admissible real reference, so UM4 fails for this family at \(P^w\).

*Proof.* (1) \(I^w\) is a real gauge transform of the flat triple; apply Lemma 1. \(c_b(\mathcal M^kI^w;x)=w(y_b)w(x)^{-1}=-I\).

(2) By W-cov, \(X(P^w)=\mathcal WX(P_0)\mathcal W^{-1}\) and \(\mathsf C_{V^w}=\mathcal W\mathsf C_V\mathcal W^{-1}\), with \(\mathcal W=\mathrm{id}\). A direct check gives the same: every non-gauge ingredient of (6)–(8) reads the field through \(\operatorname{Ad}\) of links, closed holonomies, or log-charts \(\log(\mathcal M(e^{iB}W)\mathcal M(W)^{-1})\), and central gauges leave all three unchanged. Add Lemma 6.

(3) By Lemma Z, \(X(P_0)(b_\lambda,b_\lambda)=0\). Lemma 6 and SA 8454 give \(K_x(D_I\lambda,D_I\lambda)=|\lambda(x)-\lambda(y_b)|^2=1\). Every other gauge term vanishes on \(D_I\lambda\): for \(x'\ne x\) in \(b\), \(\gamma_{y,x'}(D_I\lambda)=\lambda(x')-\lambda(y_b)=0\), and other blocks do not read the bonds of \(b\). So \(\mathsf A^{\rm abs}(P_0)(b_\lambda,b_\lambda)=1\) and, by (2), \(\mathsf A^{\rm abs}(P^w)(b_\lambda,b_\lambda)=-1\). R gives \(1\ge c_L|b_\lambda|^2\).

(4) As in hm Lemma 4, labels that distinguish \(\mathsf A^{{\rm abs},Y}\) from \(\mathsf A^{\rm abs}\) on vectors at \(x\) have tree length at least \(b_{\rm gap}-R_h\ge b_{\rm tail}-R_h\). They cost at most \(c_L/8\) in form norm. Normalize \(b_\lambda\). For the complex fibre, hm Lemma 2 bounds the displacement by \(H_1r\le c_L/8\); Lemma 2's disc argument uses only R4 data, not Rep.

(5) \(H\supset N_M(Z_0)\) and \(M\ge b_{\rm gap}\), so (4) applies to \(\chi\mathsf A^{{\rm abs},H}(P^w_0)\chi\) whenever \(x\in Z_0\). A real symmetric matrix with a negative Rayleigh quotient has no positive definite inverse. \(\square\)

**Status: proved, conditional on R, W, W-cov and G-ID(flat), under the CF2 reading.**

**Remarks.** (i) Route (a) asked for conjugacy of the literal matrices. Item 3 refutes it: \(\mathsf A^{\rm abs}(P_0)\) is positive definite, \(\mathsf A^{\rm abs}(P^w)\) is not, and \(\mathcal W=\mathrm{id}\).

(ii) \(P^w\) lies in SA's hereditary core \(\mathcal U^\circ\) whenever \(P_0\) does, provided R5–R6 are orbit-invariant (Remark 3.1). For a real triple with \(A'=0\), the tower configurations are the real background orbits of the data \(\mathcal M_{\mathbf B'}(I)^{w'}\). Their curvature and current are zero. So, under the CF2 reading, SA 14144's "\(\operatorname{Re}\mathsf A(P)\ge\tfrac12\gamma_0\)" fails at a core pair. SA's sketch compares \(\mathsf A(U,0)\) "in this gauge" with the flat operator (SA 14131). That step needs covariance of \(\mathsf A(U,0)\) under the local real gauge. It fails for CF2 (h-walk §2.1; h-walk-gate 22). It holds label-wise for Y3's form (Lemma 8). At the step's axial representative (SA 11239–11241) the sketch is consistent with hm Lemma 4.

(iii) The failure has nothing to do with smallness. \(P^w\) has the same radii as the flat field. Every R4 ceiling, however small, admits it.

---

## 6. Theorem B: descent for the covariant family

**Lemma 7 (hm on \(\mathcal K\) for the Y3 form).** All results of hm (Lemmas 1–4, Theorems 5, 7, 8, Corollary 13.1) hold for hm\(^{\rm Y}\) on \(\mathcal K\), with the same proofs and with early constants that depend on the same data.

*Proof.* Check each place where hm or its imports read the gauge form.

* R is a statement at real Rep references \(P_0\). There \(\mathsf G^{\rm Y}=\mathsf G^{\rm abs}\) (Lemma 5(b)), so \(\mathsf A^{\rm Y}(P_0)=\mathsf A^{\rm abs}(P_0)\ge c_LI\).
* W reads \(\mathsf G^{(2)}_V\) only through (I3): a finite analytic function of \(V\) with finite stencil and bounded entries (h-walk 359). Lemma 5(d) supplies (I3) for \(\mathsf G^{\rm Y}\). The labels \(A^{\rm loc}_\kappa=\theta_\kappa\mathsf C_V^{\mathsf T}(\mathsf G^{\rm Y}_V-\mathsf a)\mathsf C_V\) keep range \(O(1)\) and norm \(\le C_L\). So hm Lemma 1 holds with the same proof; its constants change only through \(C_L\).
* hm Lemma 2 uses Schwarz on labels holomorphic at fixed \(U\). \(\mathsf G^{\rm Y}_V\) is holomorphic in \(V=\mathcal M^k\mathbf U\) (Lemma 5(d)).
* hm Lemmas 3–4 compare labels at \(U\) and at the global axial extension \(\widetilde U\) on matching neighbourhoods, then apply R at \(\widetilde U\). Labels are local, and at the real axial \(\widetilde U\) the two forms agree.
* Theorems 5, 7, 8 and Corollary 13.1 use only Lemmas 1, 2, 4, the geometry and FG/UM.
* hm's F (completed form) is not needed for the gauge part: \(J^{\rm Y}_{\rm GF}=0\) at every \(V\) (Lemma 5(a)). \(\square\)

**Status: proved, given hm's imports.**

**Lemma 8 (label covariance).** Assume W-cov. For every real site gauge \(g\) and every label \(\omega\) whose local class contains \(P\),
\[
 a^{\rm Y}_\omega(P^g)=\mathcal G\,a^{\rm Y}_\omega(P)\,\mathcal G^{-1},\qquad
 r^{\rm Y}_\alpha(P^g)=\mathcal G\,r^{\rm Y}_\alpha(P)\,\mathcal G^{-1},                      \tag{6.1}
\]
with the same hulls and lengths.

*Proof.* \(A^G_\omega\) and \(A^E_\omega\) are covariant by W-cov. In \(A^{\rm loc}_\kappa\), \(\mathsf C_V\) is covariant (W-cov; h-walk 359, 389) and \(\mathsf G^{\rm Y}_V\) is covariant (Lemma 5(c)). \(\theta_\kappa\) and \(\mathsf a\) are scalar weights at base points and commute with \(\mathcal G\). Hm's transpose pairing of labels (hm 83) commutes with \(\mathcal G\), because \(\mathcal G\) is orthogonal and acts at both endpoints. Hulls, tree lengths and the split \(t_\omega\le r_c\) are geometric. So \(\mathsf A_<\) and \(E\) of hm (15) are covariant, and so are \(N_t\), \(P_t\), \(Q_t\) and \(K_t\), entry by entry. The hm (18) integral is linear. \(\square\)

**Status: proved, given W-cov.** Without W-cov, the next theorem's bounds still hold for the transported family of Remark 6.2.

**Theorem B (all-R4 envelope).** Assume R, W, W-cov, AV, the fixed geometry, (23)–(24) of hm, and the Y3 form. Let \(P\in\mathrm{R4}(Z;a_0,a_1,j_0)\), with **no** Rep condition. Then:

1. The matrices \(C,\Gamma\) of hm (19)–(20) for hm\(^{\rm Y}\) exist on every disc \(|s_\Delta|<e^{\bar\kappa}\), are jointly holomorphic at fixed \(U\), and \(C=C^{\mathsf T}\).
2. The references \(C_*,\Gamma_*\) of hm (21) are real, \(C_*>0\), and hm (25)–(26) hold with the **same** \(K_0,H_0,b,d,C_\tau\) as hm\(^{\rm Y}\) on \(\mathcal K\) (Lemma 7). These are hm's formulas (22) evaluated with W's constants for the Y3 form. They are fixed before \(\kappa\), and they are not claimed to equal hm's numerical values.
3. Theorem 8, clauses 1–6, holds. Clause 6 gives \(D(\mathbf1;P)=\chi\mathsf A^{\rm Y}(P)^{-1}\chi\) at complete pairs.
4. Corollary 13.1 holds: UM4–UM6 with \(c_m=12\), UM14, and \(C_0^{\rm UM}\le1\), with \(W_0\) fixed before \(\kappa,\bar\kappa,M\).
5. The family is real-gauge covariant: \(C(s;P^g)=\mathcal GC(s;P)\mathcal G^{-1}\), \(\Gamma(s;P^g)=\mathcal G\Gamma(s;P)\mathcal G^{-1}\), and the same for the references and \(D\).
6. Given PF, \(\mathsf A^{\rm Y}(P)\) depends only on the pair of \(P\). So \(C(\mathbf1;P)\), \(D(\mathbf1;P)\) and the functional at \(s=\mathbf1\) satisfy the tie on common domains.

*Proof.* Let \(u=u_Z(U)\) (Lemma 2), so \(P^u\in\mathcal K(Z)\) with the same radii, and \(r_Z(P^u)=r_Z(P)\) (Lemma 1). Write \(\mathcal U=\operatorname{Ad}(u)\). It is real orthogonal and commutes with \(\chi\), \(\chi_S\), hull restriction and tags.

*Matrices.* Each surviving label at \(P\) equals \(\mathcal U^{-1}\)(the same label at \(P^u\))\(\mathcal U\), by Lemma 8. The labels are defined at \(P\) directly, since \(P\in\mathcal R_{\rm loc}\) (Lemma 1 and hm Lemma 2). Tags are geometric. Hence, on every disc,
\[
 \mathsf A(s;P)=\mathcal U^{-1}\mathsf A(s;P^u)\mathcal U,\quad
 \mathsf r(s;P)=\mathcal U^{-1}\mathsf r(s;P^u)\mathcal U,\quad
 C(s;P)=\mathcal U^{-1}C(s;P^u)\mathcal U,\quad
 \Gamma(s;P)=\mathcal U^{-1}\Gamma(s;P^u)\mathcal U .
\]
The majorants of hm Theorem 5 and (27) are moduli of entries, and \(\mathcal U\) preserves them up to the colour-norm conversion already included in hm's constants. Normal convergence at \(P\) follows from that at \(P^u\). The reference triple satisfies \((P_0)^u=(P^u)_0\), so \(C_*(P)=\mathcal U^{-1}C_*(P^u)\mathcal U\) and \(\Gamma_*(P)=\mathcal U^{-1}\Gamma_*(P^u)\mathcal U\). These are real, and \(C_*(P)\) is positive definite.

*Bounds.* Operator norms and \(\operatorname{Re}(\cdot)\) commute with real orthogonal conjugation. So Lemma 7's (25)–(26) at \(P^u\) give (25)–(26) at \(P\), with the same constants and the same \(r_Z\). The \(\tau\)-scaling is scalar.

*Theorem 8.* Clause 1: FG4 applies to \(D(P)=\mathcal U^{-1}D(P^u)\mathcal U\) directly. Normalization \(\mathcal J[1]=1\) is algebraic. Holomorphy at fixed \(U\) holds labelwise, because \(u\) depends only on \(U\). Clause 2: every surviving label is evaluated from data on its own hull, at \(P\) itself, so hm's heredity proof applies verbatim; \(u\) does not enter the definition. Clause 3: hulls are connected; the same proof. Clause 4: geometric. Clause 5: the fundamental theorem of calculus on \([0,1]^{\Lambda\setminus H}\). Clause 6: at a complete pair, \(\mathsf A^{\rm Y}(P)=\mathcal U^{-1}\mathsf A^{\rm Y}(P^u)\mathcal U\) has the gap (R at the global axial representative, hm Lemma 4). So hm Theorem 5's whole-torus root exists, and the Schur identity follows.

*Corollary 13.1.* FG6/FG12 read only the matrices, the fixed real cutoff sets and the integrand bounds. The matrices at \(P\) satisfy FG1 with \(K=K_0\) and \(\varepsilon\le\varepsilon_*\). The integrand \(F_\iota(P;\cdot)\) is used at \(P\) on real \(b\); no integrand is transported. The rest of hm §8's arithmetic is unchanged.

*Covariance.* Apply Lemma 8 at \(P\) and \(P^g\). Equivalently, by Lemma 4, the representatives of \(P\) and \(P^g\) differ by a residual gauge.

*Pair function.* The operators of (6) are formed relative to \(\mathbf U\) (SA 10139, 10166). \(\mathsf C_V\) and \(\mathsf G^{\rm Y}_V\) are functions of \(V=\mathcal M^k\mathbf U\). So \(\mathsf A^{\rm Y}\) is a function of \((\mathbf U,\mathbf J)\). \(\square\)

**Status: proved, conditional on R, W (with (I1)–(I3)), W-cov, AV and FG/UM. Clause 6 also uses PF. The physical clause of Theorem 8.6 also uses G-ID.**

**Physical identification.** The physical step uses \(V=\mathcal M^kU\) in block axial gauge (SA 11239–11241), so admitted physical pairs are real Rep pairs. There \(\mathsf G^{\rm Y}=\mathsf G^{\rm abs}\) and \(\mathsf A^{\rm Y}=\mathsf A^{\rm abs}\). G-ID therefore applies to hm\(^{\rm Y}\) unchanged. At a physical pair presented in another real gauge, \(\mathsf A^{\rm Y}\) is the transported axial precision, which is what that step computes. The completed form (9) adds nothing for the gauge part, because \(J^{\rm Y}_{\rm GF}=0\).

**Order of constants.** Unchanged from hm 49. The only new constant is (I3)'s bound for \(\mathsf G^{\rm Y}\). It depends on \(L\) and the branch radius and is fixed with W's constants, before \(\kappa\). Lemma 2's gauge introduces no constant.

**Remark 6.1 (difference from hm on \(\mathcal K\)).** On \(\mathcal K\), hm\(^{\rm Y}\) differs from hm only through \(\mathsf G^{\rm Y}_V-\mathsf G^{\rm abs}_V\), with \(V=\mathcal M^k\mathbf U\) and \(\mathbf U\) complex or real but non-axial. Its entries are at most \(C_\Delta r_Z(P)\), with \(C_\Delta\) early. Proof: the difference is holomorphic on hm Lemma 2's disc, bounded there by an early constant, and zero at \(z=0\); apply Schwarz. References agree exactly. Both families therefore lie inside one envelope.

**Remark 6.2 (transport of the absolute family).** Without changing the form, define \(a^\natural_\omega(P)=\mathcal U^{-1}_{H^+}a^{\rm abs}_\omega(P^{u_{H^+}})\mathcal U_{H^+}\). Here \(H^+_\omega\) adds to \(H_\omega\) the averaging read neighbourhoods of all next-level blocks meeting \(H_\omega\), and \(u_{H^+}\) is Lemma 2's gauge on those blocks. If \(H^+_\omega\subset Y\), then \(u_Y=u_{H^+}\) on \(H_\omega\), so \(a^\natural_\omega\) does not depend on \(Y\) and heredity holds. Theorem B's items 1–4 hold for this family, with \(R_h\) and \(R_*\) increased by the early amount \(r_{\rm av}+L\), and **without** W-cov. On \(\mathcal K\) it equals hm. Under W-cov it is covariant (Lemma 4, plus block-constant covariance of \(\mathsf G^{\rm abs}\), h-walk-gate 22). By Proposition C it then fails the real tie. **Status: proved; not recommended for consumers.**

---

## 7. Proposition C: agreement with hm on \(\mathcal K\) excludes tie with covariance

**Proposition C.** Assume PF and W-cov. Read \(\mathsf G^{(2)}\) on \(\mathcal K\) as \(\mathsf G^{\rm abs}\). There is no map \(P\mapsto\mathfrak A(P)\) on torus triples of R4 with all three properties:

* (K) \(\mathfrak A(P)=\mathsf A^{\rm abs}(P)\) for \(P\in\mathcal K\);
* (T) \(\mathfrak A(P_1)=\mathfrak A(P_2)\) for two real splittings of one real pair;
* (G) \(\mathfrak A(P^g)=\mathcal G\mathfrak A(P)\mathcal G^{-1}\) for real \(g\).

The same holds for the functionals at \(s=\mathbf1\): with whole-torus support, \(D=\mathfrak A^{-1}\), so the functional determines \(\mathfrak A\).

*Proof.* Take \(U=I\), the block \(b\) and site \(x\) of Lemma Z, and a unit traceless Hermitian \(\sigma\). Fix a bump \(\chi\) on bare sites, with \(\chi(x)=1\), \(\chi=0\) at every other level-\(k\) site and outside the level-\(k\) ball of radius \(\tfrac12\) about \(x\), and first and second bare difference quotients at most \(4\) and \(16\) in level-\(k\) units. For \(0<\varphi<\min(a_0,a_1,j_0)/16\) put \(g_\varphi(z)=\exp(-i\varphi\chi(z)\sigma)\). Let
\[
 P_0=(I,0,0),\quad P_1=(I,A'_\varphi,0),\quad P_2=(I^{g_\varphi},0,0),\qquad
 e^{i\eta A'_\varphi}=I^{g_\varphi}.
\]
All factors commute, so \(\eta A'_\varphi(b)=-\varphi(\chi(b_-)-\chi(b_+))\sigma\), a real Hermitian form with \(|A'_\varphi|\le4\varphi\) and \(|\nabla A'_\varphi|\le16\varphi\). Both fields are flat up to gauge, and \(\mathbf J=0\). So \(P_0,P_1\in\mathcal K\) and \(P_2\in\mathrm{R4}\). \(P_1\) and \(P_2\) are real splittings of the real pair \(I^{g_\varphi}\), and \(P_2=P_0^{g_\varphi}\). If (K), (T), (G) held, then with PF
\[
 \mathsf A^{\rm abs}(I^{g_\varphi})=\mathfrak A(P_1)=\mathfrak A(P_2)=\mathcal G\mathfrak A(P_0)\mathcal G^{-1}=\mathcal G\mathsf A^{\rm abs}(I)\mathcal G^{-1}.   \tag{7.1}
\]
By W-cov, \(X\) and \(\mathsf C_V\) satisfy (7.1). So (7.1) says \(\mathsf G^{\rm abs}_{V^v}=\mathcal V\mathsf G^{\rm abs}_V\mathcal V^{-1}\) on the range of \(\mathsf C\), with \(V=I\) and \(v=g_\varphi|_{\text{level-}k}\). Then \(v(x)=e^{-i\varphi\sigma}\), and \(v=I\) at all other level-\(k\) sites.

Evaluate both sides at \(\mathcal V\,\mathsf C b_{\lambda'}=\mathcal V D_I\lambda'\), \(\lambda'=e\,\delta_x\). Only the \((y_b,x)\) term differs. Its value at \(V^v\) is \(1-\tfrac12\operatorname{tr}(W_x(D')e^{i\varphi\sigma})\), with \(D'=s\,D_I\lambda'\). Write \(W_x(sD_I\lambda')=e^{iH}\), \(H=s\gamma+s^2\beta+O(s^3)\), where \(\gamma=\gamma_{y,x}(D_I\lambda')=e\) up to sign and \(\beta\) does not depend on \(\varphi\). For traceless \(H\), \(e^{iH}=c(H)I+i\,\mathrm{s}(H)H\), with \(c(H)=\cos\sqrt{\tfrac12\operatorname{tr}H^2}=1-\tfrac14\operatorname{tr}H^2+\dots\) and \(\mathrm{s}(H)=1+O(|H|^2)\). Hence
\[
 \tfrac12\operatorname{tr}(e^{i\varphi\sigma}e^{iH})
 =\cos\varphi\,c(H)-\sin\varphi\,\mathrm{s}(H)\langle\sigma,H\rangle,
\]
and the second \(s\)-derivative of the term at \(0\) is
\[
 \operatorname{Hess}_\varphi=\cos\varphi\,|\gamma|^2+2\sin\varphi\,\langle\sigma,\beta\rangle .
\]
The right side of (7.1) gives \(|\gamma|^2=1\). So (7.1) requires \(\Delta(\varphi):=(\cos\varphi-1)+2\sin\varphi\langle\sigma,\beta\rangle=0\) for every admissible \(\varphi\). But
\[
 \Delta(\varphi)+\Delta(-\varphi)=2(\cos\varphi-1)<0 \qquad (0<\varphi<2\pi).
\]
So \(\Delta(\varphi)\ne0\) or \(\Delta(-\varphi)\ne0\), and \(g_{-\varphi}\) satisfies the same bounds. Contradiction. \(\square\)

**Status: proved, conditional on PF and W-cov.** When \(\beta=0\), \(\Delta\) is h-walk-gate 22's \(\cos\varepsilon-1\). The \(\pm\varphi\) pairing removes the unknown second-order coefficient \(\beta\).

**Consequence.** NL1's CI-form preserves "real ties, gauge covariance" (nl1-L 585–587). ST1 requires "simultaneous real gauge covariance and equality at two real splittings of one pair" (st1-r4 120). So no family that agrees with hm on \(\mathcal K\) can serve these consumers on the whole core. hm\(^{\rm Y}\) satisfies (T) (Theorem B.6) and (G) (B.5), and gives up (K) only away from real axial data, inside the envelope (Remark 6.1). Remark 6.2's family satisfies (K) and (G), so it fails (T).

---

## 8. Routes (b) and (c), and the consumers

**Route (b): restrict the declared domain to the Rep-saturated core.** The consumers ask for whole domains.

* IN1 H-M (in1 99–106) asks for "the actual localized Gaussian functional and its actual carriers", normalized, hereditary, wall-factorizing, holomorphic, and physical at physical parameters. No Rep restriction is stated.
* NL1 CI-Gauss (nl1-L 578–581): "on these full complex domains the actual precision/comparison package holds", including frozen IN1 H-M.
* ST1 CI (st1-r4 1533–1537): every carried activity "must be defined and bounded ... on the whole ST1 chain domain". ST1 Theorem 14.2 keeps complex input membership as a hypothesis. ST1 §1 requires real gauge covariance.
* LF1: there is no LF1 note in this clone's library; IN1 imports it as H-LF. Not read.

A Rep-restricted domain is preserved only by residual gauges (Lemma 3). So ST1's real gauge covariance could not even be stated on it without a change of interface. Fixed-real-factor shifts (SA R8; st1-r4 (75)) keep \(U\), hence keep Rep, and restriction is hereditary (hm 33). Real drift and real substitution change \(U\). No frozen text shows that every real part reached is CV-selected; st1-r4 1144 explicitly calls CV "a changed representative and test convention". **Route (b) is therefore not supported by the frozen consumers. With Theorem B it is not needed.**

**Route (c): a direct proof on all of R4.** With the Y3 form, Lemma 8 and Lemma 2 are that proof: each label at \(P\) is the conjugate of the same label at a Rep triple. A proof avoiding representatives would still need a real gap at non-axial real references. Lemma 3 of hm builds that gap from axial extensions, and covariance is how a non-axial reference reaches one.

**Interface IF-pot (bookkeeping, proved).** A consumer defines its non-Gaussian exponent relative to the Gaussian in use. If such an exponent was written relative to \(\mathsf A^{\rm abs}\) on \(\mathcal K\), switching to \(\mathsf A^{\rm Y}\) adds the free quadratic potential
\[
 q_\kappa(B)=\tfrac12\big\langle\mathsf C_VB,\theta_\kappa(\mathsf G^{\rm abs}_V-\mathsf G^{\rm Y}_V)\mathsf C_VB\big\rangle .
\]
It is holomorphic, has finite stencil, vanishes at real axial data, and has entries at most \(C_\Delta r\) (Remark 6.1). On a fine domain of one cube, \(|q_\kappa|\le C r M^4\cdot M^{-4}\sum_b|B(b)|^2\), so UM1 holds with \(a_Y\le C_q rM^4\). This is a radius ceiling chosen after \(M\), as hm 49 and SA 19466–19480 allow. Physical pairs are unaffected, because the forms agree there. **Status: proved as bookkeeping**; the consumer must actually use \(\mathsf A^{\rm Y}\).

---

## 9. What the UM contribution can claim

**Claim (conditional).** Use the 4D precision of SA 14096–14102 with \(\mathsf G^{(2)}_V\) read as Y3's covariant gauge form (Y3 31522–31536). This form coincides with the CF2 Hessian at every block-axial \(V\), hence at every admitted physical pair (SA 11239–11241). Then, at **every** triple of SA's R4 with their radii, and hence at every declared complex input pair of their hereditary core:

1. the collared matrices \(C=(\chi\mathsf A(s)\chi)^{-1}\) and \(\Gamma=-\chi\mathsf A(s)(1-\chi)\mathsf r(s)\) (SA 14164–14166) with full-read carriers exist on every disc \(|s_\Delta|<e^{\bar\kappa}\), with real references and IN1 (9): \(K_0,H_0,b,d,C_\tau\) fixed before \(\kappa,\bar\kappa,M\) and \(H_p\equiv L^3\);
2. normalization, fixed-\(U\) holomorphy, heredity, wall factorization, local dimension \(\le12(LM)^4\#Z\), the interpolation identity (UM3), and the Schur identity at \(s=\mathbf1\);
3. UM4–UM6, UM14, and \(C_0^{\rm UM}\le1\), with \(W_0\) and the bound one fixed before \(M\) (hm (32)–(35));
4. real-gauge covariance of every carrier term, and dependence on the pair at \(s=\mathbf1\).

**Premises.** R, W with (I1)–(I3), W-cov, AV, FG/UM, IN1's other rate/count constraints; G-ID for the physical clause; PF for item 4's pair dependence. These are hm's premises plus W-cov and PF.

**What it cannot claim.**

* That SA's literal precision with CF2's absolute gauge functional has these properties on the core: Theorem A refutes this at a central flip.
* That any extension of hm's \(\mathcal K\)-family has the real tie together with covariance: Proposition C.
* The tie at \(s\ne\mathbf1\): this needs PF-label (§10).
* Any statement about R5–R6 beyond membership.
* Physical identification beyond G-ID.
* That the abstract Gaussian implication, the inverse-volume cost strategy or the 3D covariant form are new. They are Sussman and Alpoge's (SA 13894–14089; Y3 39839–40569, 43564–43604, 31522–31536).

**What is new relative to the sources read.** (i) The 4D all-core supply itself, which um-novelty found not established (um-novelty 174). (ii) The observation that the 4D outline's gauge functional must be the covariant (Y3) one for that supply; with the absolute one it fails (Theorem A). (iii) The no-go, Proposition C. (iv) Exact descent by the canonical real representative, with the same radii and constants.

---

## 10. Outstanding

**Inside the target.** None, relative to the premises listed in §9. The imports themselves (R, W, AV, FG/UM, G-ID) keep their library status (hm 41–47). This text does not change it.

**First remaining Outstanding (outside UM4–UM6): PF-label.**

> **PF-label.** For every label \(\omega\) of W's fixed-region expansion, and every two triples \(P_1,P_2\) in its local class whose pairs agree on its hull \(H_\omega\), \(a_\omega(P_1)=a_\omega(P_2)\). The same holds for the root labels.

The root clause follows from the precision clause by hm (15)–(18). PF-label gives the tie, real and complex, for hm\(^{\rm Y}\) at every \(s\). ST1 needs only the real tie (st1-r4 120), so PF-label at real data suffices for ST1.

*Attack 1 (from the operator definitions).* SA 10166 forms all operators of (6) at \(\mathbf U\). h-walk Theorem W(c) (h-walk 281) says each local inverse is "the inverse of a matrix whose entries are holomorphic functions of the data on \(\Omega^\kappa_0\)". If "data" is the pair, PF-label follows factorwise. **Failure point:** h-walk 281 does not say whether "data" includes \(U\) apart from \(\mathbf U\). The local class (h-walk (C4), line 111) does read \(U\) through its real gauges and real curvature. So the attack proves PF-label only if those enter as domain conditions and not as ingredients. A line check of h-walk §§3–7 is needed (Lemma C cut-downs, Lemma L, the zero-length multiplier \(j^{(0)}\), Theorem T vertices).

*Attack 2 (identity theorem).* A label is holomorphic in \(A'\) at fixed \(U\). Two real splittings \((U_1,A'_1),(U_2,A'_2)\) of one pair have \(U_1\ne U_2\). Holomorphy in \(A'\) at each fixed \(U\) relates values on two different fibres only through a common function of \(e^{i\eta A'}U\). **Failure point:** that common function is the content of PF-label. The identity theorem cannot produce it from fibrewise holomorphy alone.

*Attack 3 (redefine labels through the pair).* Define each label as the h-walk formula with every operator written as a function of \((\mathbf U,\mathbf J)\), and use \(U\) only to certify membership in the local class. Then PF-label holds by definition. W's bounds hold wherever some splitting is in the class, because the bounds are proved at a triple and the formula does not read \(U\). **Failure point:** this is legitimate only if h-walk's construction has no step that chooses something depending on \(U\) beyond the class. h-walk 24 and 77 state "no gauge choice" for the local models. That is the same unperformed line check as Attack 1.

**Precise remaining lemma.** PF-label, reduced by Attacks 1–3 to: no ingredient of h-walk §§3–7 reads the real factor \(U\) except through membership in the local class.

**Other open interfaces, unchanged by this text.** G-ID (hm 45). hm's actual-family/stage interface (hm 371), except that its "whole declared local domain must be admitted to the representative class or supplied with a compatible descent theorem" is now supplied by Theorem B for the Y3-form family. R5–R6 invariance under real gauges (Remark 3.1), which is not needed here.

---

## Corrections and checks against other notes

1. hm 37 and 494 are right for the literal family: activity gauge invariance does not supply descent. Theorem A shows more: the literal matrices do not descend at all.
2. hm-draft 134 ("the supremum over a core equals the supremum over its triples in the representative") is wrong for the CF2 family, by Theorem A. It is right for the Y3 family, by Theorem B.
3. h-walk §2.1 and h-walk-gate 22 identify the non-covariance. Lemma 5 removes it by Y3's form. The h-walk (H3) phrase "A itself is covariant exactly under" block-constant gauges, already narrowed by the gate, becomes "every term is covariant under every real gauge" for the Y3 form.
4. pr-lay 60 ("Full gauge covariance of the soft gauge Hessian is not asserted") stays true for CF2. For the Y3 form it is now proved (Lemma 5(c)).
5. SA 14131's "in this gauge" step is valid label-wise for the Y3 form and fails for CF2 (Theorem A, Remark (ii)). SA 10200 does not say which form is meant.
6. No frozen note or gate was edited.

These are research implications and a counterexample. They are not refereed. **This text grants no scientific or audit status.**
