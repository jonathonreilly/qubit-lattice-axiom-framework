# DR for the actual construction: the regional response, pass 1 (long draft)

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), 2026-11-05. Pass 1 (long draft) of critical-path item 4 of `library/assembly-status.md` (L185), in the draft → distil → referee → freeze process. Written in the lead clone `F`, folder `ym4d-hard-route-20261030`, at its checked-out state; only this file was written. Not checked by another model. Research text, not an audit; it grants no status. No step rests on a computation; every argument is a finite hand proof meant to be Lean-formalizable.

**Credit.** The outline (SA), the complete accounts and the three-dimensional text at upstream revision `31a47c543775` are by **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text**. Their response hypothesis (SA 5775–5802), the system (R9) and its norms (SA 10354–10412), the decoupling mechanisms and the mesh-uniform heat-kernel estimates (BGH) are used below with line numbers. **Tadeusz Bałaban** supplies the programme: background fields, constrained propagators, random-walk decoupling and the local regularity method (CMP 99, 102, 109). **Jonathan Dimock** supplies the flat-propagator exposition behind the flat port (`fp1.md`). Library texts by Claude and Codex keep their own provenance and standing; I say for each one whether it is frozen, distilled or drafted.

**How to read line numbers.** "L n" is line n of the named library file in this clone. "SA n" is line n of `ym4.tex` in the scratchpad `sa/` folder. A quoted phrase is followed by its line. I say what a source proves only after quoting it.

**Status words.** *Proved*: every step is written here from the named imports. *Import*: a statement of another file, with its standing. *Specification*: a definition we fix; it needs no proof. *Outstanding*: not proved.

## 0. Results and status

| Clause (§1 gives the exact text) | Result here | Status |
|---|---|---|
| D-one, specification at one | Proposition 3.1: at \(s\equiv\mathbf1\) the specified equations (drlocp (5)–(7), \(J_*=\mathbf J\)) are ST1 (42)–(43) term by term, given the resummation identities DR1 | **proved** as an implication from DR1 (DR1 for \(H\): O1D Theorem B(a); for \(H_1,\mathfrak G,M_s^{\rm walk}\): imported, same mechanism) |
| D-zero (zero source, zero switches, source-free component) | Lemma 3.2 | **proved** from UNQ |
| D-real, D-cov (real gauges; CV representative) | Lemma 3.3, Lemma 2.2 | **proved** from termwise reality/covariance of the walk terms (import: h-walk W(c), field part, as kept by its gate) |
| D-split, DR-locP, D-res (restriction to wall-components), D-lift (common lifts) | Proposition 3.4 (drlocp Theorem 1 rechecked for \(J_*=\mathbf J\); fine grid identified, Lemma 2.3) | **proved** as implications from D, UNQ, S-loc; restriction on the full declared local domains stays **Outstanding** (drlocp L198) |
| Gauge form | Lemma 2.1: DR does not read the Gaussian gauge form; the Y3 relative form of frozen `descent.md` changes nothing in DR | **proved** |
| Two-current identification (drlocp L69) | Proposition 4.1 and Corollary 4.2: the two continuations are **different** off the physical locus; at \(s=1\) on ST1's locus (33) their difference is exactly \((f_H^{-1}-1)\delta\), nonzero in an explicit example. Theorem 4.3: DR uses ST1's \(J_*=\mathbf J\); every frozen consumer reads that one | **proved** (a counterexample to identification, and a resolution by specification) |
| D-est (16), H-DR (7) with its current, td R's stencil and product-ball clauses | Theorem 5.1: (7), hence (16), follow from [PW], [NL], (O1) and the local row bounds [Rows], with \(E_{\bar\kappa}=e^{48\bar\kappa}\), \(s_D=\epsilon_De^{-64\bar\kappa}\), \(\mu=\theta/2\), \(\theta=\min\{\theta_{\rm PW},\tau_L/8,\log2/(2L)\}\) | **proved** as an implication |
| [PW], the pointwise decoupled bounds | Lemma PW♮ (§6.1). Three attacks (§6.3–6.5). Theorem GA (gauge-direction absorption) is proved; it removes the rough-current term exactly at \(s\equiv\mathbf1\). Lemma F (flat flux Schauder estimate, mesh-uniform) is proved. Theorem R1 reduces [PW] at \(s\equiv\mathbf1\) to the flux extension P\(^{\rm div}\) of frozen P82 Theorem P and four scalar estimates S1–S4 | **Outstanding** — first remaining statement (§6.6) |
| [NL] (nonlinear bounds of \(W_s,\mathcal C\)) | stated; not attacked here | **Outstanding** (second in proof order) |

**First remaining Outstanding statement:** Lemma PW♮ of §6.1, the weighted pointwise bounds for the specified decoupled operators \(H(s),H_1(s),\mathfrak G(s)\) on the whole polydisc. After the three attacks its \(s\equiv\mathbf1\) instance rests on P\(^{\rm div}\) and S1–S4 (§6.6); its decoupled instance rests on a pointwise bound for walk terms that are not solutions of any equation (§6.5, end).

---

## 1. The DR clauses, exactly as the frozen consumers use them

### 1.1 ST1 (frozen `st1-r4.md`)

The input is stated at L138–143. I split it into named clauses. Quotations are exact.

- **D-hol.** L138: "An actual regional response \((H,K)\), holomorphic in its complex input pair, datum and \(|s_\Delta|<e^{\bar\kappa}\), is given".
- **D-real, D-cov, D-res, D-lift, D-split.** L138: "with reality, covariance, restriction consistency, common-lift transport and splitting over face-connected components."
- **D-one.** L138: "At \(s=1\) it uses the reduced action and multiplier formulas of Lemma 6." Lemma 6 fixes them at L460–472, equations (42)–(43), and says at L473: "These finite formulas specify what DR must resum to. They do not prove the weighted estimates for a decoupling of them."
- **D-est.** L138–141: "For source \(S\), it obeys \(n_b(H,K):=\max\{l|H|,l^2|\nabla^UH|,l^3|K|\}\le C_D E_{\bar\kappa} C_A\delta_{\rm src}e^{-\mu d(b,S)}\)." (16). L142–143: "\(C_D,\mu\) are fixed constants; \(E_{\bar\kappa}\ge1\) is a specified parameter factor, for example \(e^{C_E\bar\kappa}\) with fixed \(C_E\). … Likewise write the source-domain threshold explicitly if it is \(\epsilon_D e^{-c_D\bar\kappa}\)."
- **D-zero.** Theorem 14, hypothesis 3, L1543: "DR is given on the full switch polydisc, with (16), specification at one, restriction and component splitting, and it vanishes in a source-free component and at zero switches."
- **Metric and units.** L1467: "If DR is initially stated in the old finer metric, (16) also holds in \(d_+\), since \(d_-\ge d_+\)." L1471: "If DR was expressed in old layer scales, passing to input scales costs at most \(L^3\)".
- **BOX(resp)**, a second consumer of the same clauses, L149–150: "On the full switch polydisc the box response has the DR properties and \(n_b(H,K)\le C(M)E_{\bar\kappa}\delta'_t e^{-\mu d_+(b,S_{\rm bx})}\)."
- **Order.** Row 2 (L163) fixes "DR base constants/rates" with the early constants; row 7 (L168) chooses \(\kappa\), then \(\bar\kappa\); row 10 (L171): "Amplitudes such as \(E_{\bar\kappa}\), \(C(M)\) enter here, not the uniform precision constants."

The real reference of Lemma 6 is "a real regular critical \(U_0\)" with \(\mathbf J=J+\delta\), \(\delta(b)=0\) if \(b\) touches \(\Omega_1\) (L366–369, (33)). Lemma 6's conclusions (34)–(36) are the physical identification at \(s=1\); (35) reads "\(\mathbf J+K=J^\circ(e^{i\eta H}U_0)+f_H^{-1}\delta\)" (L378).

ST1 does not define "restriction consistency" or "common-lift transport" beyond L138 (grep: no other occurrence in `st1-r4.md`). The outline's response hypothesis (SA 5792–5794) lists realness, gauge covariance, compatibility under restriction to wall-components, and transport by common lifts; SA 5607 and 5884 use "common lift" for the identification of non-wrapping regions of different tori. I read D-res and D-lift in that sense (§3.4).

### 1.2 NL1 (frozen `nl1-L.md`, H-DR, L159–174)

- **H1 (joint holomorphy).** L159–162: "For every admitted input pair, \(|s_\Delta|<e^{\bar\kappa}\) and \(\|S\|_{\rm src}<s_D:=\epsilon_De^{-c_D\bar\kappa}\), the response is jointly holomorphic in the complex pair, source and switches, real at real arguments, zero at zero source".
- **H2 (estimate (7)).** L165: "\(n_b(h(s;P,S))\le C_DE_{\bar\kappa}\|S\|_{\rm src}e^{-\mu d_+(b,\operatorname{supp}S)}\), \(E_{\bar\kappa}\ge1\)." Here \(n_b\) is (4) of the same file (L82): \(\max\{l_+|H|,l_+^2|\nabla^UH|,l_+^3|K|\}\).
- **H3 (component reads at fixed pair).** L169–170: "For each face-component \(K'\) of \(\operatorname{supp}s\), the response on the bonds and stencils of \(K'\) depends only on \(s|_{K'}\) and the source rows assigned to \(K'\), at fixed \(P\)".
- **H4.** L171: "Require restriction consistency and the ST1 covariance conventions."
- Its own Outstanding note, L172–174: "this uniform complex-source estimate, including its current, and this precise row-locality clause strengthen the printed ST1 (16). Multiplying one already formed response by a scalar does not prove (7)."

### 1.3 TD (distilled `td.md`, R, L25–33)

R imports "the following strengthened form of ST1's DR" (L25) and adds, beyond H1–H3:

- **R-stencil.** L31: "Its stencil lies in a connected set \(B_b\) of at most 16 fine cubes containing the initial-site cube \(\Delta_b\)."
- **R-ball.** L31: "The source domain is the full ball in the product of assigned row spaces, invariant under row masks and independent complex scalings within that ball. Its norm is the maximum of row norms".
- **R-comp.** L32: "when \(B_b\subset\operatorname{supp}s\), its stencil reads only components meeting \(B_b\)."
- **R-src.** L33: the completed main-step source \(S(v)\), \(v=v_0+u(s\odot\zeta)\), holomorphic on \(\|v\|_\infty<c_{\rm ch}L^{-9}\), Lipschitz \(C_A\), \(\|S(v_0)\|_{\rm src}\le C_A\delta_{\rm src}\), rows reading one neighbour layer. This is a property of the source map, not of the response; it is H-FL's business (nl1-L L140–157) and is not treated here.

TD's verdict line L486: "Keep ST1's actual DR construction open".

### 1.4 drlocp (distilled `drlocp.md`)

- **D (specified response data)**, L27–39: O1D Definition D, the field-read part of HW Theorem W as repaired, LOC-3's endpoint hypotheses; absolutely convergent expansions on \(|s_\Delta|<e^{\bar\kappa}\); every term "carries every parameter cube meeting its full connected enlarged hull" (L27); local reach \(r_g\le8L+1\); floors (4): \(L\ge27\), \(R_1\ge8L^3\), \(M_1\ge\max\{240,16Lr_g\}\), \(\rho_{\mathbf B}=3LM_1\ge80r_g\). L39: "The parameter grid in (3) is required to be the fine switch grid used below."
- **The equations**, L41–55, (5)–(6): \(\alpha=H_1S-\mathfrak GW_s^{\rm red}(\alpha)\), \(h=\alpha-H\mathcal C(h)\), with \(M_s=M_s^{\rm walk}-a_0I\) and the diagonal "**unparameterized**" (L51).
- **UNQ**, L56: existence, uniqueness and holomorphy from DF Proposition 5.1 under [PW], [NL], with \(B=C_{\rm op}e^{16\bar\kappa}\), \(b_*<c_*B^{-4}\).
- **The current**, L58–67, (7): \(F_*(h)=F'_U(h)-F'_U(0)+J_*\), \(\lambda=(I+H^{\mathsf T}\mathcal C'_h{}^{\mathsf T})^{-1}H^{\mathsf T}F_*(h)\), \(\lambda_0=H^{\mathsf T}J_*\), \(j=R_hK_h^{\mathsf T}\lambda-K_0^{\mathsf T}\lambda_0\). L67: "We use \(J_*=\mathbf J\) for the ST1 (43) specification. The choice \(J_*=F'_U(0)\) gives the different continuation in D3L (3)".
- **DR-locP** = Theorem 1, L190: "For two admitted pairs agreeing on \(W\), and equal source rows there, (6)–(7) give identical \((h,j)\) at every coordinate based in \(W\). … The response vanishes on zero-switch cubes and on a component with zero source. The induced function is holomorphic on the image of coordinate restriction. With S-loc the completed response reads \(P\) only in \(N_1(W)\)."
- **Outstanding — actual specification**, L69–75 (the two-current item, quoted in §4), and **Outstanding — full local domains**, L198: "Image-domain descent does not establish a regional solution on every declared \(\mathcal O_\sigma(Y;U)\), nor consistency between different regional constructions."

### 1.5 One name, several statements

1. **"DR" (ST1) and "H-DR" (NL1) are two statements.** ST1 (16) bounds the response *at the source in use*, of size \(C_A\delta_{\rm src}\), with no stated source ball. NL1 (7) is *linear in \(\|S\|_{\rm src}\)* on the full ball \(\|S\|_{\rm src}<s_D\), with joint holomorphy in the source. (7) implies (16) whenever \(\|S\|_{\rm src}\le C_A\delta_{\rm src}<s_D\); the converse fails (NL1 L174 says so). TD's R is (7) plus R-stencil, R-ball, R-comp. Below, "DR" means the strongest form: (7) with R-stencil, R-ball, R-comp, H3, D-one, D-zero and the algebraic clauses.
2. **The metric and rate.** ST1 writes \(d(b,S)\) and \(\mu\); NL1 and TD write \(d_+\) and \(\mu\) or \(\mu_R\). ST1 L1467 reconciles the metrics. I prove (7) in the layer metric \(d_{\mathbf B}\) of SA 9602, which is ST1's \(d\) (density \(1/l(x)\), `st1-r4.md` L26; cp12 Lemma 3.1 identifies SA 9602 with `p82.md` (1)); the input metric \(d_+\le d\) then follows by L1467.
3. **"Restriction consistency".** SA 5793 means restriction to wall-components; drlocp L198 also asks for "consistency between different regional constructions" on full declared domains. These are two statements; the first is proved here (Proposition 3.4(c)), the second stays Outstanding.
4. **"UNQ".** ST1's OPS/SLICE/UNQ (L137) is uniqueness of the straightening and response fixed points on stated balls; drlocp's UNQ (L56) is DF Proposition 5.1's existence-uniqueness-holomorphy implication under [PW], [NL]. The second implies the first for the response at \(s=1\) on DF's ball.
5. **Letters.** \(D\) denotes the covariant difference on site fields (ST1 L388), drlocp's import D, and drlocp's \(D=e^{\bar\kappa}-1\) (L90). \(R\) denotes the scalar projection of ST1 L393, TD's import R, and \(R_h\) of (7). I write "import D", "import R" for the imports.

---

## 2. The actual construction

### 2.1 Setting

Fix a finite history and a main step \((i-1,\mathrm{out})\to(i,\mathrm{in})\), as in frozen `nl1-L.md` D1–D3 (L14–107). The data are:

- **Domains.** ST1's chart-free intrinsic chain domains \(\mathcal D_{a|\sigma}\) (`st1-r4.md` L104), with element cores R1 (L91–102) and the radius table (Tq0) (L82–89): \(r_\iota(m)=C_\iota g_m\ell_m^q\), \(g_m=\theta_m^{-1/2}\), \(\ell_m=\log\theta_m\), \(\lambda_\tau\equiv1\), \(\Lambda_Q=1\) (no lift). These are SA's running radii (SA 6017–6035), as L89 says.
- **Representative.** Amendment CV (L41): the real factor \(U\) of a triple is the canonical mean-contour representative ("\((\mathcal M^nU)(z,x)=I\) at each nonnode with parent \(z\)"). Lemma 5 (L347) gives its continuation \(\Phi_V\).
- **Triples and pairs.** \(P=(U,A',\mathbf J)\), \(\mathbf U=e^{i\eta A'}U\), independent complex current (L57). Shifts by (10) (L61–66).
- **Switches.** \(s=(s_\Delta)\) on the level-\((i-1)\) cubes of side \(M\) (`nl1-L.md` L32–40), \(|s_\Delta|<e^{\bar\kappa}\).
- **Source.** A reduced row datum \(S\) (ST1 L47–51: "Feed (6) to \(\Phi\), and (7) to the response equations"), with the max-of-rows norm \(\|S\|_{\rm src}\).
- **Gauge form of the Gaussian step.** The step's Gaussian precision uses Y3's relative form \(\mathsf A^{\rm Y}\) (frozen `descent.md` (3)–(4), Theorem B, L196).

### 2.2 The specification

**Definition DR♮ (the actual regional response).** For \((s,P,S)\) as above:

1. *Operators.* \(H(s),H_1(s),\mathfrak G(s)\) and \(M_s^{\rm walk}\) are the decoupled operators of O1D Definition D (`o1-decoupled.md` L105–114): \(\mathsf H(s)=\sum_\omega s^\omega[T_\omega]_{A\nu}\), \(H(s)=\mathsf H(s)\mathsf m^{-1}\), \(s^\omega=\prod_{\Delta\in\mathsf P(\omega)}s_\Delta\), \(\mathsf P(\omega)\) the parameter cubes meeting the enlarged hull \([\![\omega]\!]^+\); \(H_1,\mathfrak G,M^{\rm walk}_s\) "are defined the same way from their own expansions" (L114), \(\mathfrak G\) by the composed assignment of `pw-bridge.md` (7.4) (drlocp L33). The parameter partition \(\mathcal P\) is the fine switch grid (Lemma 2.3). All operators are evaluated at the pair itself (PF, `descent.md` L66).
2. *Field equations.* drlocp (5)–(6) (L41–55): \(\alpha=H_1S-\mathfrak GW_s^{\rm red}(\alpha)\), \(h=\alpha-H\mathcal C(h)\), with \(M_s=M_s^{\rm walk}-a_0I\), the diagonal unparameterized.
3. *Current.* drlocp (7) with \(J_*=\mathbf J\): \(\lambda=(I+H^{\mathsf T}\mathcal C'_h{}^{\mathsf T})^{-1}H^{\mathsf T}(F'(h)-F'(0)+\mathbf J)\), \(\lambda_0=H^{\mathsf T}\mathbf J\), \(K:=j=R_hK_h^{\mathsf T}\lambda-K_0^{\mathsf T}\lambda_0\), \(R_h=(E_h^{\mathsf T})^{-1}\), \(E_hv=\int_0^1\operatorname{Ad}(e^{it\eta h})v\,dt\) (`d3-local.md` L78).
4. *Response.* \((H,K):=(h,j)\), the unique solution in DF's balls (drlocp UNQ, L56), whenever it exists.

The specification is a choice. SA allows it: the decoupled operators are "specified linear maps" with their walk coefficients and convergence domains (SA 5775–5783, quoted at O1D L103), and SA "leaves \(\mathsf W_s\) and \(j_s\) unwritten" (`p81-crit-draft.md` L595). Its \(s\equiv\mathbf1\) value is fixed by frozen ST1 (§3.1).

### 2.3 Lemmas on the data

**Lemma 2.1 (DR does not read the Gaussian gauge form).** None of the maps in Definition DR♮ reads \(\mathsf G^{\rm abs}_V\) or \(\mathsf G^{\rm Y}_V\) of `descent.md` (3). Hence DR♮ is the same whether the step uses the absolute CF2 form or Y3's relative form; in particular frozen `descent.md` Theorem B changes nothing in DR. *Status: proved.*

*Proof.* The forms of `descent.md` (3) enter only \(\mathsf A^\bullet(P)=X(\mathbf p(P))+\mathsf C_V^{\mathsf T}\mathsf G^\bullet_V\mathsf C_V\) (descent (4), L54), the precision of the integrated fluctuation. Descent L58: "Changing (3) changes the off-axial precision; it is not a reinterpretation of a fixed matrix." The maps of DR♮ are built from the Wilson action \(F\), the straightened rows (\(\widehat Q,\mathcal C,K_h\)), the scalar objects \(Q',G',R\), the response gauge term \(DRD^{\mathsf T}\) and the walk data of Theorem W (O1D L34–40). The response gauge condition \(RD^{\mathsf T}H=0\) (ST1 (34)) is the background-field slice of the response system, specified in ST1 Lemma 6; it is not a term of \(\mathsf A^\bullet\). The completed source \(S(v)=b_V(a_V(v))\) (`nl1-L.md` L141) is a function of the fluctuation coordinate \(v\) and the chart \(a_V\); the free space \(I\) and its coordinates are the same for both forms (descent L13), and descent Lemma 7 (L275) changes only the split of the integrand measure. So no input of DR♮ changes. ∎

**Lemma 2.2 (representative).** Let \(g\) be a real site gauge. If every operator in Definition DR♮ is covariant under \(g\) (Lemma 3.3), then the response at \(P^g\) with the transformed source is the transform of the response at \(P\). In particular, the response at the CV representative determines the response at every real representative of the same orbit, and conversely. *Status: proved, conditional on Lemma 3.3's imports.*

*Proof.* This is Lemma 3.3(b) applied to the residual gauge that relates two real representatives (`descent.md` Lemma 1, L123–125: two representatives differ by \(r=u_Y(U^g)gu_Y(U)^{-1}\)). ∎

**Lemma 2.3 (the parameter grid is the fine grid).** Take \(\mathcal P\) equal to the level-\((i-1)\) cubes of side \(M\) of `nl1-L.md` D1. If the input layers satisfy \(m_+(b)\le i\) (`nl1-L.md` L132) and
\[
 M\ \ge\ \tfrac L2\,\ell_{\mathsf P},\qquad
 \ell_{\mathsf P}\ \ge\ \max\{8r_1+1,\ 256\bar\kappa/\tau_L\},\qquad r_1=16L^3M_1+4L,
 \tag{2.1}
\]
then O1D's hypothesis (P) (L116) holds and Lemma P (L120) and Theorem B (L135) apply with this \(\mathcal P\). *Status: proved.* This supplies the identification that drlocp L75 asks for ("Nor does the floor \(M\ge C_{\rm dec}\bar\kappa\) by itself identify O1D's parameter partition with the fine grid").

*Proof.* O1D L116: (P) "holds when \(\mathcal P\) is a grid of physical side at least \(\ell_{\mathsf P}\xi_{\max}/2\), with \(\xi_{\max}\) the top scale", because the density of \(d_{\mathbf B}\) is at least \(\xi_{\max}^{-1}\). Since input layers have level at most \(i\), \(\xi_{\max}\le\xi_i=L\xi_{i-1}\). The fine cubes have physical side \(M\xi_{i-1}\ge\ell_{\mathsf P}L\xi_{i-1}/2\ge\ell_{\mathsf P}\xi_{\max}/2\). The floors on \(\ell_{\mathsf P}\) are those of O1D Lemma P and Theorem B. Lemma WC (L129) needs at least three cubes per direction, which is torus room. ∎

**Lemma 2.4 (R-stencil).** If \(M\ge4\), the stencil of \(n_b\) lies in a corner-connected set \(B_b\) of at most \(16\) fine cubes containing \(\Delta_b\). *Status: proved.*

*Proof.* \(n_b(H,K)\) reads \(H\) and \(K\) at \(b\) and the covariant differences \(\nabla^U_\nu H\) at \(b\), each a two-point stencil in direction \(\nu\) (ST1 (1)). All read bonds have both endpoints in the \(\ell^\infty\)-ball of radius \(2\eta\) about the initial site \(x_b\). This ball has \(\ell^\infty\)-diameter \(4\eta<M\eta\le M\xi_{i-1}\), so in each coordinate it meets at most two consecutive grid intervals. The cubes it meets are indexed by \(I_1\times\cdots\times I_4\), each \(I_\mu\) one index or two consecutive ones; there are at most \(2^4\), any two differ by at most one in every index and so are corner-adjacent, and \(\Delta_b\ni x_b\) is among them. ∎

---

## 3. The algebraic clauses

### 3.1 Specification at one (D-one)

**Imports DR1 (resummation at \(s\equiv\mathbf1\)).** (a) \(\mathsf H(\mathbf1)=\mathsf H\), R9's lift \(\mathsf H=\mathsf GQ^{\mathsf T}(Q\mathsf GQ^{\mathsf T})^{-1}\), \(\mathsf G=(\Delta^{\rm W}_{\mathbf U}+DRD^{\mathsf T}+Q^{\mathsf T}aQ-\Delta'_\pi[\mathbf J])^{-1}\) (O1D L36–40). This is O1D Theorem B(a), L137 and L150: "At \(s\equiv1\), \(\sum_\omega[T_\omega]_{A\nu}=[\mathbb K^{-1}]_{A\nu}=\mathsf H\), by Theorem W(a) and (I-b)." (b) \(H_1(\mathbf1)=\ell_1\), \(\mathfrak G(\mathbf1)=\mathfrak G\) of ST1 (38), \(M_{\mathbf1}^{\rm walk}=\Sigma\) and \(a_0=\widehat a\). These are the same statement for the other expansions; they are imports of D, with the coefficient premise for \(\Delta^{(2)}[j]\) flagged in `dec-field.md` L171. (c) The local maps of drlocp (5) are \(\mathcal C\) (nonlinear part of the straightened rows), \(\mathcal C_2=\mathcal C^{(2)}\) (its quadratic part), \(K=K_0=\widehat Q\), and \(N_0(h)=R_F'(h)=F'(h)-J-\Delta h\). These are the identifications that drlocp L69 attributes to [RED].

**Proposition 3.1 (D-one).** Under DR1, at \(s\equiv\mathbf1\):

(i) \(H(\mathbf1)=\ell\), where \(\ell=G\widehat Q^{\mathsf T}\Sigma\) is ST1 (38).

(ii) \(W^{\rm red}_{\mathbf1}=V'_{\mathbf J}\), the derivative of ST1's reduced action (41).

(iii) \((\alpha,h)\) solves drlocp (6) iff \((A_\bullet,H)=(\alpha,h)\) solves ST1 (42) with \(B'=S\): \(A_\bullet=\ell_1B'+A\), \(A=-\mathfrak GW_1(A_\bullet)\), \(H=\mathcal L(A_\bullet)\).

(iv) The current of Definition DR♮(3) equals \(j_1(H)\) of ST1 (43); in particular \(R_h=f_h^{-1}\), \(f_h=f(-i\eta\operatorname{ad}h)\).

Consequently, under ST1's OPS/SLICE/UNQ, Lemma 6's conclusions (34)–(36) hold for DR♮ at \(s\equiv\mathbf1\). *Status: proved, as an implication from DR1.*

*Proof.* (i) Both lifts are characterized by the saddle property of O1D (I-a) (L42–44): \(\mathsf Hf\) is the unique \(A\) with \(QA=f\) and \(M_{\mathbf J}A\in\operatorname{ran}Q^{\mathsf T}\), where \(M_{\mathbf J}=\Delta^{\rm W}_{\mathbf U}+DRD^{\mathsf T}-\Delta'_\pi[\mathbf J]\); the row mass drops out. The same proof applies to ST1's \(\ell\): \(\ell b\) is the unique \(A\) with \(\widehat QA=b\) and \(G^{-1}A\in\operatorname{ran}\widehat Q^{\mathsf T}\), where \(G^{-1}=\Delta_\pi+DRD^{\mathsf T}+\widehat Q^{\mathsf T}\widehat a\widehat Q\) and \(\Delta_\pi=\Delta-\Delta'_\pi[\mathbf J]\), \(\Delta=F''(0)=\Delta^{\rm W}_{\mathbf U}\) (ST1 L366, L408). Indeed \(\widehat Q\ell b=\widehat QG\widehat Q^{\mathsf T}\Sigma b=b\) and \(G^{-1}\ell b=\widehat Q^{\mathsf T}\Sigma b\); uniqueness is O1D's argument with \(\widehat Q\) in place of \(Q\). Now \(\widehat Q=K_0=\mathsf mQ\) with \(\mathsf m\) diagonal invertible (O1D L40), so \(\operatorname{ran}\widehat Q^{\mathsf T}=\operatorname{ran}Q^{\mathsf T}\), and \(G^{-1}A\in\operatorname{ran}Q^{\mathsf T}\) iff \(M_{\mathbf J}A\in\operatorname{ran}Q^{\mathsf T}\). Hence \(\ell b\) is the unique \(A\) with \(QA=\mathsf m^{-1}b\) and \(M_{\mathbf J}A\in\operatorname{ran}Q^{\mathsf T}\), which is \(\mathsf H\mathsf m^{-1}b=H(\mathbf1)b\) by DR1(a).

(ii) Differentiate (41) at \(A'=\alpha\), using bilinear transposes and the symmetry of \(\Sigma-\widehat a\). Write \(\mathcal D=\mathcal D(\alpha)\), \(\mathcal D'\) its derivative, and \(\mathcal L'=I-\ell\mathcal D'\):
\[
 V'_{\mathbf J}(\alpha)=-(\mathcal D'-\mathcal C^{(2)\prime})^{\mathsf T}\ell^{\mathsf T}\mathbf J
 -\widehat Q^{\mathsf T}(\Sigma-\widehat a)\mathcal D
 -\mathcal D'^{\mathsf T}(\Sigma-\widehat a)\widehat Q\alpha
 +\mathcal D'^{\mathsf T}(\Sigma-\widehat a)\mathcal D
 +\mathcal L'^{\mathsf T}R_F'(\mathcal L(\alpha)).
\]
In drlocp (5) at \(s=\mathbf1\): \(d_{\mathbf1}(\alpha)=\mathcal C(h)\) with \(h=\alpha-\ell\mathcal C(h)\). ST1 defines \(\mathcal D(\alpha)=X\), \(X=\mathcal C(\alpha-\ell X)\). Put \(h=\alpha-\ell X\); then \(X=\mathcal C(h)\) and \(h=\alpha-\ell\mathcal C(h)\), so \(d_{\mathbf1}=\mathcal D\) on the common contraction ball (both fixed points are unique there). Then \(d_{3,\mathbf1}=\mathcal D-\mathcal C^{(2)}\), \(p_{\mathbf1}=H(\mathbf1)^{\mathsf T}\mathbf J=\ell^{\mathsf T}\mathbf J\) by (i), \(M_{\mathbf1}=\Sigma-\widehat a\) and \(K=\widehat Q\) by DR1(b),(c), \(Z_{\mathbf1}=I-\ell\mathcal D'=\mathcal L'\), and \(N_0(h)=R_F'(h)\) with \(h=\mathcal L(\alpha)\). The five terms of (5) are the five terms above, in order.

(iii) With \(A_\bullet:=\alpha\), \(B':=S\), the first equation of (6) at \(s=\mathbf1\) is \(A_\bullet=\ell_1B'-\mathfrak GW_1(A_\bullet)\), which is \(A_\bullet=\ell_1B'+A\), \(A=-\mathfrak GW_1(A_\bullet)\) by DR1(b) and (ii). The second equation of (6) is \(h=\alpha-\ell\mathcal C(h)\), whose small solution is \(h=\alpha-\ell\mathcal D(\alpha)=\mathcal L(\alpha)=H\), as in (ii). Uniqueness of both systems on the common balls gives the converse.

(iv) For the bilinear trace pairing, \(\langle\operatorname{Ad}(g)X,Y\rangle=\tfrac12\operatorname{tr}(gXg^{-1}Y)=\langle X,\operatorname{Ad}(g^{-1})Y\rangle\). Hence \(E_h^{\mathsf T}=\int_0^1\operatorname{Ad}(e^{-it\eta h})\,dt=\int_0^1e^{t(-i\eta\operatorname{ad}h)}dt=f(-i\eta\operatorname{ad}h)\), since \(f(z)=(e^z-1)/z=\int_0^1e^{tz}dt\). So \(R_h=f_h^{-1}\). With \(H(\mathbf1)=\ell\), \(K_h=q'(h)\), \(K_0=\widehat Q\), \(\mathcal C'_h=K_h-K_0=\mathcal C'_h\), and \(J_*=\mathbf J\), Definition DR♮(3) reads \(\lambda=(I+\ell^{\mathsf T}\mathcal C_h'^{\mathsf T})^{-1}\ell^{\mathsf T}(F'(h)-F'(0)+\mathbf J)=\omega_1(h;\mathbf J)\) and \(j=f_h^{-1}q'(h)^{\mathsf T}\omega_1-\widehat Q^{\mathsf T}\ell^{\mathsf T}\mathbf J=j_1(h)\), which is (43) at \(T=H=h\).

The final sentence: ST1 Lemma 6's proof (L475–494) derives (34)–(36) from (42)–(43), OPS/SLICE/UNQ and criticality; by (iii)–(iv) its hypotheses are met. ∎

### 3.2 Zero source and zero switches (D-zero)

**Lemma 3.2.** (a) At \(S=0\) the response is \((h,j)=(0,0)\). (b) At \(s=0\) the response is \((0,0)\) for every \(S\). (c) On a face-component of \(\operatorname{supp}s\) on which \(S\) vanishes, the response vanishes. *Status: (a), (b) proved from UNQ; (c) is drlocp Theorem 1 (§3.4).*

*Proof.* (a) \(\mathcal C(0)=0\) and \(\mathcal C'(0)=0\), because \(\widehat Q\) is the linear part of the straightened rows; \(\mathcal C_2'(0)=0\) since \(\mathcal C_2\) is quadratic. The inner equation \(h=0-H\mathcal C(h)\) has the solution \(h=0\), so \(d_s(0)=0\) and \(d_s'(0)=\mathcal C'(0)(I-Hd_s'(0))=0\). Every term of (5) at \(\alpha=0\) then vanishes: \(d_{3,s}'(0)=0\); \(d_s(0)=0\); \(\alpha=0\); and \(N_0(0)=R_F'(0)=F'(0)-J=0\). So \((\alpha,h)=(0,0)\) solves (6) at \(S=0\), and UNQ makes it the solution. For the current, \(h=0\) gives \(\mathcal C'_0=0\), \(R_0=I\), \(K_0=K_h\), \(F_*(0)=J_*\), so \(\lambda=H^{\mathsf T}J_*=\lambda_0\) and \(j=K_0^{\mathsf T}(\lambda-\lambda_0)=0\).

(b) Every walk hull \([\![\omega]\!]^+\supset\kappa_0^\sharp\) is nonempty and meets at least one parameter cube, so \(\mathsf P(\omega)\neq\varnothing\) and \(s^\omega=0\) at \(s=0\). Hence \(H(0)=H_1(0)=\mathfrak G(0)=M_0^{\rm walk}=0\). The first equation of (6) reads \(\alpha=0\); the second gives \(h=0\); then \(\lambda=\lambda_0=0\) and \(j=0\). The unparameterized \(-a_0I\) plays no role, because \(\mathfrak G(0)=0\) multiplies all of \(W_0^{\rm red}\). ∎

### 3.3 Reality and covariance (D-real, D-cov)

**Imports (termwise).** (T1) Each walk term \([T_\omega]\) of every expansion in Definition D is holomorphic in the pair, real at real pairs, and covariant under real site gauges; this is the field part of h-walk W(c) kept by its gate (O1D L150: "for fixed regions, the cutoffs are fixed scalar numbers: this failure does not introduce additional field reads or spoil holomorphy in the fields"; "It is gauge covariant (gate §6: covariance of the algebraic construction survives)"). (T2) The local maps \(\mathcal C,K_h,N_0,F',R_h\) have Taylor series with real coefficients in the real structure and are covariant (they are built from the Wilson action and the actual averages, `descent.md` Lemma 1, (10)).

**Lemma 3.3.** Under (T1), (T2) and UNQ: (a) at real \((s,P,S)\) the response is real; (b) for a real site gauge \(g\), the response at \((s,P^g,S^g)\) is \((h^g,j^g)\). *Status: proved, conditional on (T1), (T2).*

*Proof.* (a) Let \(\kappa\) be the real structure (complex conjugation of the complexified Lie-algebra coordinates). At real arguments every coefficient of (5)–(7) commutes with \(\kappa\), by (T1)–(T2) and absolute convergence. So \(\kappa(\alpha,h)\) solves (6). The norms are \(\kappa\)-invariant, so it lies in the same balls; uniqueness gives \(\kappa(\alpha,h)=(\alpha,h)\). The current is a convergent series of real maps applied to real data. (b) The tags \(s^\omega\) depend only on positions, which a site gauge does not move. By (T1)–(T2) every map in (5)–(7) intertwines the gauge action. So \((\alpha^g,h^g)\) solves the transformed system. Real gauges act unitarily on fibres, so the norms and balls are invariant; uniqueness gives the claim. The current follows termwise. ∎

### 3.4 Splitting, two-pair locality, restriction and common lifts

**Proposition 3.4.** Assume import D (drlocp L27–39), UNQ (L56), S-loc (L85), and Lemma 2.3. Let \(W\) be a face-component of \(\operatorname{supp}s\), \(|s_\Delta|<e^{\bar\kappa}\).

(a) (**H3**, **R-comp**) At fixed \(P\), the response on bonds and stencils of \(W\) depends only on \(s|_W\) and the source rows in \(W\).

(b) (**DR-locP**) For two admitted pairs agreeing on \(W\), with equal source rows there, the responses \((h,j)\) agree at every coordinate based in \(W\); the response vanishes on zero-switch cubes and on a component with zero source; with S-loc the completed response reads \(P\) only in \(N_1(W)\).

(c) (**D-res**, image-domain form) The induced function of \((s|_W,P|_W,S|_W)\) is holomorphic on the image of coordinate restriction, and restrictions compose.

(d) (**D-lift**) Suppose in addition (T3): every walk term whose enlarged hull lies in a non-wrapping region \(Y\) with its collar is the same function on every torus containing a common lift of \(Y\). If \(N_1(W)\), enlarged by \(\rho_{\mathbf B}\), is non-wrapping and lifts to two tori with equal switches, pair and source data, the two responses agree on \(W\).

*Status:* (a)–(c) are drlocp Theorem 1, which I recheck below for \(J_*=\mathbf J\); (d) is proved here from (T3). The extension to every declared \(\mathcal O_\sigma(Y;U)\) and "consistency between different regional constructions" remain **Outstanding** (drlocp L198).

*Proof.* drlocp Theorem 1 (L190–196) proves (a)–(c) for (6)–(7) with any local anchor \(J_*\); L67: "We use \(J_*=\mathbf J\) for the ST1 (43) specification." I check the one place the anchor enters. In (7), \(F_*(h)=F'(h)-F'(0)+\mathbf J\) and \(\lambda_0=H^{\mathsf T}\mathbf J\): \(\mathbf J\) is read bondwise at the bonds where \(H^{\mathsf T}\) evaluates it. drlocp Lemma 2.2 (L176, L186) shows that every term of \(\lambda\) and \(\lambda_0\) begins with a leftmost \(H^{\mathsf T}\), whose kernel entries are split (Lemma 2.1, L155): both endpoints deep in one component, reading only that component's pair and switches. So the bonds where \(\mathbf J\) is read lie in the component's deep set, and \(\mathbf J|_W\) is part of \(P|_W\). Two pairs agreeing on \(W\) have the same \(\mathbf J\) there. This is all the proof uses. The parameter grid identification needed at L39 is Lemma 2.3.

(d) Run drlocp's splice argument (L192–194) on the two tori at once. By (b), on each torus the response on \(W\) is the unique solution, in the common balls, of the system restricted to the deep set of \(W\), and every term contributing there has its enlarged hull inside the \(\rho_{\mathbf B}\)-enlargement of \(N_1(W)\) (drlocp Lemma 2.1, first-exit argument (16)). By (T3) these terms are the same functions on both tori. So the restricted systems coincide, and uniqueness gives equal solutions. The current is a convergent sum of the same terms. ∎

---

## 4. The two current continuations (drlocp L69)

drlocp L69–75: "[RED] identifies (5) with that nonlinear map; it does not identify the two current continuations in (7). They agree on \(\mathbf J=F'_U(0)\), but their difference off that locus is [(8)]. There is no supplied reason for (8) to vanish." Here (8) is
\([R_hK_h^{\mathsf T}(I+H^{\mathsf T}\mathcal C'_h{}^{\mathsf T})^{-1}-K_0^{\mathsf T}]H^{\mathsf T}(F'_U(0)-\mathbf J)\), and \(F'_U(h)\) is "the local Wilson force in the chart at \(\mathbf U\)" (`d3-local.md` L70), so \(F'_U(0)=J(\mathbf U)\) at complete stars.

Write \(j^{\rm ST}\) for (7) with \(J_*=\mathbf J\) (Definition DR♮) and \(j^{\rm D3L}\) for (7) with \(J_*=F'_U(0)\) (`d3-local.md` (3), from `wf-room-2.md` (6.1)).

**Proposition 4.1 (the difference).** (a) For every \((s,P,S)\) in the domain, with the same field solution \(h\),
\[
 j^{\rm ST}-j^{\rm D3L}=\big[R_hK_h^{\mathsf T}(I+H^{\mathsf T}\mathcal C'_h{}^{\mathsf T})^{-1}-K_0^{\mathsf T}\big]H^{\mathsf T}\big(\mathbf J-F'_U(0)\big).
 \tag{4.1}
\]
It vanishes when \(h=0\).

(b) At \(s\equiv\mathbf1\), at a pair \((U_0,0,\mathbf J)\) with \(U_0\) real regular critical and \(\mathbf J=J+\delta\), \(\delta\) satisfying ST1 (33), and under the hypotheses of ST1 Lemma 6,
\[
 j^{\rm ST}-j^{\rm D3L}=(f_H^{-1}-1)\,\delta .
 \tag{4.2}
\]
*Status: proved* ((a) is algebra; (b) uses frozen ST1 Lemma 6 and Proposition 3.1).

*Proof.* (a) The field equations (5)–(6) do not contain \(J_*\); \(J_*\) enters (7) only through \(F_*\) and \(\lambda_0\), affinely. Subtracting the two instances of (7) gives (4.1). At \(h=0\): \(\mathcal C'_0=0\), \(R_0=I\), \(K_0=K_h\), so the bracket is \(K_0^{\mathsf T}-K_0^{\mathsf T}=0\).

(b) At \(s\equiv\mathbf1\), \(H=\ell\) (Proposition 3.1(i)), and \(F'_U(0)=F'(0)=J\) at \(A'=0\). ST1 L488–493: for \(\zeta=\ell^{\mathsf T}\delta\), "\(\zeta(c)=\eta^3\delta(c)\) on bare rows, \(\widehat Q^{\mathsf T}\zeta=\delta\), \(\mathcal C'_T{}^{\mathsf T}\zeta=\Delta^{(2)}[\zeta]=0\)." Hence in (4.1) \((I+\ell^{\mathsf T}\mathcal C_h'^{\mathsf T})^{-1}\zeta=\zeta\), \(K_h^{\mathsf T}\zeta=(\widehat Q+\mathcal C_h')^{\mathsf T}\zeta=\delta\), and \(K_0^{\mathsf T}\zeta=\delta\). With \(R_h=f_h^{-1}\) (Proposition 3.1(iv)) the bracket applied to \(\zeta\) is \(f_h^{-1}\delta-\delta\). ST1 L381 states that \(H\) is unchanged by \(\delta\), so \(h=H\) in both. ∎

As a check, (4.2) agrees with ST1 (35): at \(\delta=0\) the two continuations coincide, \(j^{\rm D3L}\) does not depend on \(\delta\) (its anchor is \(J\), and \(H\), \(\ell\) do not change, since \(\Delta'_\pi[\delta]=0\) by ST1 L432), and ST1 L381 says \(K\) changes by \(f_H^{-1}\delta-\delta\).

**Corollary 4.2 (the continuations are not equal).** There is a real admitted configuration at which \(j^{\rm ST}\neq j^{\rm D3L}\). *Status: proved (a counterexample to identifying them).*

*Proof.* Use the Pauli basis \(T_a=\sigma_a\), orthonormal for \(\tfrac12\operatorname{tr}\) (`nl1-L.md` D1). Take the setting of Proposition 4.1(b). Choose a bare determining row \(b\in\Gamma_0\) (a level-zero bond with no endpoint in \(\Omega_1\)). On interior rows \(b_V(B)=B\) (ST1 L48), so take the real source \(B=\varepsilon\,\mathbf1_b\sigma_2\), with \(\varepsilon\neq0\) small enough for the response ball, and \(\delta=\delta_0\mathbf1_b\sigma_1\), \(\delta_0\in\mathbb R\setminus\{0\}\) small; \(\delta\) satisfies (33) since \(b\) does not touch \(\Omega_1\). By (36), \(\eta H(b)=B(b)=\varepsilon\sigma_2\). Put \(z=-i\operatorname{ad}(\varepsilon\sigma_2)\). From \([\sigma_2,\sigma_1]=-2i\sigma_3\) and \([\sigma_2,\sigma_3]=2i\sigma_1\): \(z\sigma_1=-2\varepsilon\sigma_3\), \(z\sigma_3=2\varepsilon\sigma_1\). So on \(\operatorname{span}\{\sigma_1,\sigma_3\}\), \(z=2\varepsilon\mathsf J\) with \(\mathsf J\sigma_1=-\sigma_3\), \(\mathsf J\sigma_3=\sigma_1\), \(\mathsf J^2=-I\). The power series \(f(z)^{-1}=z/(e^z-1)\) evaluated at \(z=2\varepsilon\mathsf J\) equals the scalar function \(x\mapsto x/(e^x-1)\) at \(x=2i\varepsilon\), with \(i\) replaced by \(\mathsf J\). Since \(2i\varepsilon/(e^{2i\varepsilon}-1)=(\varepsilon/\sin\varepsilon)e^{-i\varepsilon}\),
\[
 f_H^{-1}\sigma_1-\sigma_1=\Big(\frac{\varepsilon\cos\varepsilon}{\sin\varepsilon}-1\Big)\sigma_1+\varepsilon\,\sigma_3 .
\]
By (4.2), \((j^{\rm ST}-j^{\rm D3L})(b)=\delta_0[(\varepsilon\cot\varepsilon-1)\sigma_1+\varepsilon\sigma_3]\), whose \(\sigma_3\)-component \(\delta_0\varepsilon\) is nonzero. All data are real. ∎

**Theorem 4.3 (resolution of the two-current item).** DR's current is \(j^{\rm ST}\) (Definition DR♮(3)). Every frozen consumer of DR reads this one:
- ST1 Lemma 6 (35), L378, and D-one (L138), by Proposition 3.1(iv);
- NL1 H-DR, L172 ("including its current"), which strengthens "the printed ST1 (16)";
- ST1 BOX(id), L149 ("the correct independent/plain-current identity").

The distilled TD (L25) and drlocp (L67) also read ST1's. On the physical locus \(\mathbf J=F'_U(0)\) the two continuations coincide (Proposition 4.1(a)), so `d3-local.md` L92's physical identity \(\mathbf J+j=J(e^{i\eta h}\mathbf U)\) holds for \(j^{\rm ST}\) there. Off that locus they differ (Corollary 4.2). So no identification is available, and none is needed: a consumer that reads \(j^{\rm D3L}\) off the physical locus — `red.md` L59–94 and `loc-4.md` L207 cite it; neither is frozen — must be re-read with \(J_*=\mathbf J\). drlocp's locality proof covers that anchor (§3.4). *Status: proved (the consumer list is by line check of the frozen texts named).*

---

## 5. The complex-source estimate (D-est, H1–H2, R-ball)

### 5.1 Premises

Norms are SA's (`dec-field.md` L229–230): \(\|a\|_{X,w}=\sup_yw(y)\max\{\xi_y|a|_y,\xi_y^2|\nabla_{\mathbf U}a|_y\}\), \(\|f\|_{F,w}=\sup_yw(y)\xi_y^3|f|_y\), \(\|b\|_{Y,w}=\sup_cw(c)|b(c)|\). \(\mathcal W_\theta\) is the class of weights with \(w(b)\le e^{\theta d_{\mathbf B}(b,b')}w(b')\).

- **[PW]** (`dec-field.md` L234–237): on the closed polydisc \(|s_\Delta|\le e^{\bar\kappa}\) and the admitted complex pair domain, for all \(w\in\mathcal W_\theta\), \(0\le\theta\le\theta_{\rm PW}\): \(\|H(s)\|_{Y_w\to X_w},\|H_1(s)\|_{Y_w\to X_w},\|\mathfrak G(s)\|_{F_w\to X_w}\le B:=C_{\rm PW}e^{16\bar\kappa}\). **Outstanding** (§6).
- **[NL]** (`dec-field.md` (5.1)): \(W_s,\mathcal C\) vanish at zero and, on unweighted balls of radius \(r\le r_0/B\), \(\|W_s(a)-W_s(v)\|_{F,w}\le C_WB^2r\|a-v\|_{X,w}\), \(\|\mathcal C(a)-\mathcal C(v)\|_{Y,w}\le C_Cr\|a-v\|_{X,w}\). **Outstanding** (SA 10368–10389 asserts it; `dec-field.md` L245: "its quoted assertion does not constitute its rebuild").
- **(O1)** for \(H(s)\): for \(w\in\mathcal W_\theta\), \(\theta\le\tau_L/8\),
  \(\sup_cw(c)\eta^4\sum_b|H(s)(b,c)|\xi_b^{-3}w(b)^{-1}+\sup_cw(c)\eta^4\sum_p|D_{\mathbf U}H(s)(p,c)|\xi_p^{-2}w(p)^{-1}\le C_H:=C_LB_Le^{16\bar\kappa}K_{\tau_L/8}\).
  This is O1D Theorem B(c) (L139), an implication from Theorem W and (P); (P) is Lemma 2.3. **Import** (O1D: "Same-model and ungated", L16).
- **[Rows]** (local, on \(\|h\|_{X,1}\le r_R\)): with \(\hat n_b(h)\) the maximum of \(\xi|h|+\xi^2|\nabla_{\mathbf U}h|\) over the double blocks of the rows reading \(b\),
  (a) \(|(K_h-K_0)^{\mathsf T}\nu|(b)\le C_R\xi_b^{-3}\hat n_b(h)\max_{c\ni b}|\nu(c)|\); (b) \(|R_h-I|\le C_R\hat n_b(h)\) at \(b\); (c) \(|K_h^{\mathsf T}\nu|(b)\le C_R\xi_b^{-3}\max_{c\ni b}|\nu(c)|\);
  (d) for a field \(v\) and \(|t|\le1\): \(|\langle v,F''(th)h\rangle|\le C_R\,\eta^4\big[\sum_p|D_{\mathbf U}v(p)|\xi_p^{-2}\hat n_p(h)+\sum_b|v(b)|\xi_b^{-3}\hat n_b(h)\big]\).
  (a)–(c) are the finite one-step row bounds (`p82.md` (17); `a3-derivative.md` §4.1–4.2 (9)–(11), gated). (d) is the curl-squared plus curvature-remainder form of the Wilson Hessian (`a3-derivative.md` 7.1, L435–436, and (12) for \(N_0'\)), with the curl at \(e^{i\eta th}\mathbf U\) compared to \(D_{\mathbf U}\) at zero order; it is the pairing that SA L10407 uses, \((D^{\mathsf T}DA,He_c)=(DA,DHe_c)\) (quoted at `red.md` L53). **Import.**

### 5.2 The theorem

**Theorem 5.1 (DR's estimate from [PW]).** Assume [PW], [NL], (O1), [Rows], UNQ, and \(\|\mathbf J\|_{F,1}\le\gamma_0\) on the pair domain. Put \(\theta=\min\{\theta_{\rm PW},\tau_L/8,\log2/(2L)\}\), \(\mu=\theta/2\), and
\[
 s_D:=\min\Big\{c_*B^{-4},\ \frac{1}{16C_RC_HB},\ \frac{r_R}{4B}\Big\},\qquad c_*\le\min\{r_0/4,(16C_W)^{-1},(16C_C)^{-1}\}.
 \tag{5.1}
\]
Then for every admitted pair, \(|s_\Delta|<e^{\bar\kappa}\) and \(\|S\|_{\rm src}<s_D\):

(i) (**H1**) the response \((h,j)\) exists, is unique in DF's balls, and is jointly holomorphic in \((P,S,s)\); it is real at real arguments and zero at zero source;

(ii) (**H2**, (7)) \(n_b(h,j)\le C_DE_{\bar\kappa}\|S\|_{\rm src}e^{-\mu d_{\mathbf B}(b,\operatorname{supp}S)}\), with \(E_{\bar\kappa}=e^{48\bar\kappa}\) and \(C_D=C(L)\,C_{\rm PW}(1+C_LB_LK_{\tau_L/8})^2(1+\gamma_0)\) fixed before \(\kappa\);

(iii) (**D-est**, (16)) if \(\|S\|_{\rm src}\le C_A\delta_{\rm src}<s_D\), then \(n_b(h,j)\le C_DE_{\bar\kappa}C_A\delta_{\rm src}e^{-\mu d(b,S)}\), in ST1's metric \(d\), hence also in \(d_+\) (ST1 L1467);

(iv) (**R-ball**) the source domain \(\{\|S\|_{\rm src}<s_D\}\) is the full max-norm ball in the product of row spaces, invariant under row masks and independent complex row scalings in the ball.

The threshold has ST1's form \(s_D=\epsilon_De^{-c_D\bar\kappa}\) with \(c_D=64\) and \(\epsilon_D\) fixed before \(\kappa\). *Status: proved, as an implication.*

*Proof.* Throughout, \(b:=\|S\|_{\rm src}=\|S\|_{Y,1}\). Write \(\sigma=\operatorname{supp}S\) and \(w_\sigma(y)=e^{\theta d_{\mathbf B}(y,\sigma)}\). Since \(d_{\mathbf B}(\cdot,\sigma)\) is \(1\)-Lipschitz for \(d_{\mathbf B}\), \(w_\sigma\in\mathcal W_\theta\); and \(w_\sigma=1\) on \(\sigma\), so \(\|S\|_{Y,w_\sigma}=b\).

*Step 1 (existence and the unweighted bound).* By (5.1), \(b<c_*B^{-4}\). `dec-field.md` Proposition 5.1 (L247–256), from [PW] and [NL], gives a unique solution with \(\|\alpha\|_{X,1}\le R:=2Bb\), \(\|h\|_{X,1}\le2R\), jointly holomorphic in all specified variables. This is drlocp's UNQ.

*Step 2 (weighted field bound).* All norms are finite at fixed volume. In \(\alpha=H_1S-\mathfrak G W_s(\alpha)\) use [PW] and [NL] in the weight \(w_\sigma\), with \(W_s(0)=0\): \(\|\alpha\|_{X,w_\sigma}\le Bb+B\cdot C_WB^2R\,\|\alpha\|_{X,w_\sigma}\). Here \(C_WB^3R=2C_WB^4b\le1/8\). So \(\|\alpha\|_{X,w_\sigma}\le\frac87Bb\). In \(h=\alpha-H\mathcal C(h)\), with \(\mathcal C(0)=0\): \(\|h\|_{X,w_\sigma}\le\|\alpha\|_{X,w_\sigma}+B\,C_C(2R)\|h\|_{X,w_\sigma}\), and \(2BC_CR=4C_CB^2b\le1/4\). So
\[
 \|h\|_{X,w_\sigma}\le\tfrac43\cdot\tfrac87Bb\le2Bb .
 \tag{5.2}
\]
Hence \(\xi_y|h|_y+\xi_y^2|\nabla_{\mathbf U}h|_y\le4Bb\,e^{-\theta d_{\mathbf B}(y,\sigma)}\). Bonds based in a pillar \(y\) have scale in \([\xi_y,L\xi_y]\) (O1D L59), so \(l(b)\le L\xi_y\); and \(|\nabla^Uh-\nabla_{\mathbf U}h|\le4|A'||h|\) (`a3-clauses.md` L89). Thus \(l|h|+l^2|\nabla^Uh|\le C(L)Bb\,e^{-\theta d_{\mathbf B}(b,\sigma)}\).

*Step 3 (multipliers).* By (O1), for any force \(f\), \(w(c)|(H^{\mathsf T}f)(c)|\le w(c)\eta^4\sum_b|H(b,c)|\xi_b^{-3}w(b)^{-1}\,\|f\|_{F,w}\le C_H\|f\|_{F,w}\). So \(\|H^{\mathsf T}\|_{F_w\to Y_w}\le C_H\), and \(|\lambda_0|=|H^{\mathsf T}\mathbf J|\le C_H\gamma_0\) (unweighted). By [Rows](a), \(\|\mathcal C_h'^{\mathsf T}\nu\|_{F,w}\le C_Re^{2L\theta}\|h\|_{X,1}\|\nu\|_{Y,w}\), the factor \(e^{2L\theta}\) comparing weights at a bond and at the rows reading it (double blocks have \(d_{\mathbf B}\)-diameter at most \(2L\)). With \(\|h\|_{X,1}\le4Bb\) and (5.1), \(\|H^{\mathsf T}\mathcal C_h'^{\mathsf T}\|_{Y_w\to Y_w}\le4C_HC_Re^{2L\theta}Bb\le\tfrac12\) since \(e^{2L\theta}\le2\) by the choice of \(\theta\). So \((I+H^{\mathsf T}\mathcal C_h'^{\mathsf T})^{-1}\) has norm at most \(2\) on \(Y_w\). Write
\[
 \lambda-\lambda_0=(I+H^{\mathsf T}\mathcal C_h'^{\mathsf T})^{-1}\big[H^{\mathsf T}(F'(h)-F'(0))-H^{\mathsf T}\mathcal C_h'^{\mathsf T}\lambda_0\big].
\]
For the first term, \((H^{\mathsf T}(F'(h)-F'(0)))(c)=\int_0^1\langle H(\cdot,c),F''(th)h\rangle dt\); [Rows](d) and both sums of (O1) give \(w_\sigma(c)|\cdot|\le C_RC_He^{2L\theta}\|h\|_{X,w_\sigma}\). For the second, [Rows](a) and Step 3's bound on \(H^{\mathsf T}\) give \(\le C_HC_Re^{2L\theta}\|h\|_{X,w_\sigma}C_H\gamma_0\). Hence
\(\|\lambda-\lambda_0\|_{Y,w_\sigma}\le4C_RC_H(1+C_H\gamma_0)\|h\|_{X,w_\sigma}\).

*Step 4 (current).* \(j=(R_hK_h^{\mathsf T}-K_0^{\mathsf T})\lambda_0+R_hK_h^{\mathsf T}(\lambda-\lambda_0)\). By [Rows](a)–(c), \(\xi_b^3|(R_hK_h^{\mathsf T}-K_0^{\mathsf T})\lambda_0|(b)\le3C_R^2\hat n_b(h)C_H\gamma_0\) and \(\xi_b^3|R_hK_h^{\mathsf T}(\lambda-\lambda_0)|(b)\le2C_R\max_{c\ni b}|\lambda-\lambda_0|(c)\). With Steps 2–3 and the weight comparison,
\[
 \xi_b^3|j(b)|\le C(L)C_R^2C_H(1+C_H\gamma_0)\,Bb\,e^{-\theta d_{\mathbf B}(b,\sigma)} .
\]
Since \(l\le L\xi\), \(l^3|j|\) obeys the same bound with another \(L^3\).

*Step 5 (constants).* \(B=C_{\rm PW}e^{16\bar\kappa}\), \(C_H=C_LB_LK_{\tau_L/8}e^{16\bar\kappa}\), so \(BC_H(1+C_H\gamma_0)\le C_{\rm PW}(1+C_LB_LK_{\tau_L/8})^2(1+\gamma_0)e^{48\bar\kappa}\). Taking \(\mu=\theta/2\le\theta\) only weakens the decay. This proves (ii). In (5.1), \(c_*B^{-4}=c_*C_{\rm PW}^{-4}e^{-64\bar\kappa}\), \((16C_RC_HB)^{-1}\ge c'e^{-32\bar\kappa}\) and \(r_R/(4B)\ge c''e^{-16\bar\kappa}\), so \(s_D\ge\epsilon_De^{-64\bar\kappa}\) with \(\epsilon_D\) depending on early constants only; replace \(s_D\) by \(\epsilon_De^{-64\bar\kappa}\).

*Step 6 (the rest).* (i): holomorphy of the current is that of a convergent Neumann series of jointly holomorphic maps; reality and zero source are Lemmas 3.2–3.3. (iii) is (ii) at \(b\le C_A\delta_{\rm src}\), with \(d=d_{\mathbf B}\) (§1.5 item 2). (iv): the domain is \(\{\max_c|S(c)|<s_D\}\), a product of row balls. ∎

**Remarks.** (1) The decay rate of (7) is a strengthening of the outline: SA 5797–5799 states the size "at most \(Ce^{C\bar\kappa}\sup|B'|\)" in local first-order norms, with no exponential factor. The decay comes from DF's weighted contraction, that is, from [PW] holding in all weights of \(\mathcal W_\theta\). (2) BOX(resp) (ST1 L149) is the same implication for the box system, with its own \([PW]\); its constants \(C(M)\) are chosen after \(M\) (ST1 L151). (3) H1's "real at real arguments" is Lemma 3.3(a).

---

## 6. The first remaining Outstanding statement: [PW]

### 6.1 Statement

**Lemma PW♮ (Outstanding).** There are \(C_{\rm PW}\ge1\), \(\theta_{\rm PW}>0\) and \(0<\beta<1\), depending only on \(L\) and \(\alpha_{\rm H}\), such that for every admitted complex pair \(P\) of the step (ST1 cores at the (Tq0) radii, below the early ceiling \(a_*(L)\) of O1D Theorem A), every \(s\) with \(|s_\Delta|\le e^{\bar\kappa}\) and every \(w\in\mathcal W_\theta\), \(\theta\le\theta_{\rm PW}\),
\[
 \|H(s)b\|_{X,w},\ \|H_1(s)b\|_{X,w}\le C_{\rm PW}e^{16\bar\kappa}\|b\|_{Y,w},\qquad
 \|\mathfrak G(s)f\|_{X,w}\le C_{\rm PW}e^{16\bar\kappa}\|f\|_{F,w},
\]
uniformly in depth, mesh, volume, region shape and \(M_1\) above its floors, for the decoupled operators of Definition DR♮ (or of any specification with DR's algebraic clauses and the \(s\equiv\mathbf1\) value of Proposition 3.1).

This is `dec-field.md` [PW] (L234–237). dec-field L245: "[PW] is the missing pointwise target, not Theorem 4.2"; L367: "The actual \(H(s),H_1(s),\mathfrak G(s)\) supremum estimates … remain open." O1D L28 says the same: "the first system's own decoupled field bounds … need a pointwise upgrade of the walk terms".

### 6.2 The structure of the current correction

Work at a pair with real factor \(U\) and independent current \(\mathbf J\). Write \(\lambda_C=G'RD^{\mathsf T}C\) (ST1 L394) and recall \(G'R=SR\), \(RG'=RS\), where \(S=A_s^{-1}\) is P82's scalar inverse (`a3-clauses.md` L238: "\(G'R=SR\) for every positive top weight"). Brackets of a site field with a bond field are evaluated at the initial site; pairings are the fine ones of ST1 L387.

**Lemma 6.1 (decomposition).** For every field \(C\),
\[
 \Delta'_\pi[\mathbf J]C=E_0[\mathbf J]C+DRG'\,Y[\mathbf J]C+D\big(RG'D^{\mathsf T}Z[\mathbf J]C\big),
 \tag{6.1}
\]
where \(E_0[\mathbf J]\) is zero-order with \(|E_0C|(b)\le c_{\mathfrak g}|\mathbf J(b)|\max_{b_\pm}|\lambda_C|\); \(Y[\mathbf J]C\) is a site field with \(|Y(x)|\le c_{\mathfrak g}\sum_{b\ni x}|\mathbf J(b)|(|C(b)|+|D\lambda_C(b)|)\); and \(Z[\mathbf J]C(b)=-\tfrac i2[\mathbf J(b),\lambda_C(b_-)]\) is a bond field with \(|Z|\le c_{\mathfrak g}|\mathbf J||\lambda_C|\). The last term is a pure gradient \(D\varphi\) with \(\varphi=RG'D^{\mathsf T}Z\in\operatorname{ran}R\). *Status: proved (finite algebra).*

*Proof.* Read ST1 (37) as a linear functional of \(A\) for fixed \(C\), and use \(\langle[X,Y],W\rangle=\langle Y,[W,X]\rangle\) for the trace pairing. The terms \(i[\lambda_C,A]\) and \(-i[A,\lambda_C^+]\) are linear in \(A\) without derivatives: they give the zero-order force \(E_0C\). The terms \(i[\lambda_A,C]\), \(-i[C,\lambda_A^+]\) and \(-i[\lambda_A,D\lambda_C]\) read \(A\) only through the values of \(\lambda_A\) at the endpoints of bonds; collecting them at sites gives \(\langle\lambda_A,Y\rangle_{\rm site}\) with \(Y\) as stated (the transport \(\operatorname{Ad}U(b)\) in \(\lambda^+\) is unitary at real \(U\) and bounded by \(e^{2\eta|A'|}\) at complex links). Since \(\lambda_A=G'RD^{\mathsf T}A\), \(\langle\lambda_A,Y\rangle=\langle A,DRG'Y\rangle\), using the symmetry of \(G'\) and \(R\) in the site pairing. The term \(-i[\lambda_C,D\lambda_A]\) reads \(A\) through \(D\lambda_A\): \(\tfrac12\langle-i[\lambda_C,D\lambda_A],\mathbf J\rangle=\langle D\lambda_A,Z\rangle\) with \(Z\) as stated. Then \(\langle D\lambda_A,Z\rangle=\langle\lambda_A,D^{\mathsf T}Z\rangle=\langle A,DRG'D^{\mathsf T}Z\rangle\). Finally \(RG'D^{\mathsf T}Z\in\operatorname{ran}R\). ∎

The first two terms of (6.1) are bounded forces once \(\lambda_C\) and \(D\lambda_C\) are bounded and \(DRG'\) gains one derivative (S1 below). The third is the only obstruction: \(Z\) is merely bounded, because nothing bounds a difference of the independent \(\mathbf J\) (`dec-field.md` L29: "The regular-pair class (SA 10129–10137) bounds \(m^3|J|\) but imposes no difference bound on the **independent** \(J\)"), and \(DRG'D^{\mathsf T}\) is a second-order singular operator.

**Lemma 6.2 (gauge directions).** Let \(U\) be real and satisfy P82's hypotheses, \(N=\ker Q'\), and \(\varphi\in\operatorname{ran}R\). Put \(\chi_\varphi=S\varphi\). Then \(\chi_\varphi\in N\), \(\Delta_U\chi_\varphi=\varphi\), and:

(a) (P82's system) \(S_q^\circ(D\chi_\varphi,0)=\big(D\varphi+q^{\mathsf T}\mathcal C\chi_\varphi,\ 0\big)\), where \(\mathcal C\chi:=qD\chi\) is the zero-order curvature operator \((\mathcal C\chi)(p)=\eta^{-2}(\operatorname{Ad}T_1(p)-\operatorname{Ad}T_2(p))\chi(x_p)\) for the plaquette curl, \(T_{1,2}\) the two transports round \(p\) from its base \(x_p\) (for the other curl add P82's \(E_c\) terms, L482–489). In particular \(|\mathcal C\chi|(p)\le c\,\eta^{-2}|U(\partial p)-I|\,|\chi(x_p)|\).

(b) (critical reference, physical current) If \(U=U_0\) is a real regular critical reference and \(\mathbf J=J=F'(0)\), then with \(M_J:=\Delta-\Delta'_\pi[J]+DRD^{\mathsf T}\), \(M_JD\chi_\varphi=D\varphi\) and \(\widehat QD\chi_\varphi=0\); so the saddle system at the physical current maps \((D\chi_\varphi,0)\) to \((D\varphi,0)\) **exactly**.

*Status: proved*, from P82 Lemma 2 and ST1 Lemma 6.

*Proof.* P82 L310–311: "If \(Q'\psi=0\), then \(A_s\psi=\Delta_U\psi\) … Conversely \(Q'Sf=0\) implies \(\psi=Sf\in\ker Q'\) and \(\Delta_U\psi=f\)", and \(\operatorname{ran}R=\{f:Q'Sf=0\}\) there. So \(\chi_\varphi\in N\), \(\Delta_U\chi_\varphi=\varphi\). By P82 L305, \(\langle\psi,A_s\psi\rangle=\|D\psi\|^2+\|m^{-1}Q'\psi\|^2\), so \(\Delta_U=D^{\mathsf T}D\) on \(N\) (ST1 L424 checks the missing-neighbour boundary term). Hence \(DRD^{\mathsf T}D\chi_\varphi=DR\varphi=D\varphi\). SLICE (ST1 L424: "\(\widehat QD\chi=0\) on \(\mathcal N\), also at outward rows") gives \(KD\chi_\varphi=0\). (a) follows from \(q^{\mathsf T}q\,D\chi=q^{\mathsf T}(qD\chi)\); the formula for \(qD\chi\) is the commutator of the two covariant differences round a plaquette, which is P82 L477–478 ("Each coefficient is \(\eta^{-2}(\operatorname{Ad}T_1-\operatorname{Ad}T_2)\)"). (b) ST1 L431: "\(\Delta-\Delta'_\pi[J]=\Pi^{\mathsf T}\Delta\Pi\)", with \(\Pi A=A-D\lambda_A\); and L424: "\(\lambda_{D\chi}=\chi\) for \(\chi\in\mathcal N\)". So \(\Pi D\chi_\varphi=0\) and \(M_JD\chi_\varphi=DRD^{\mathsf T}D\chi_\varphi=D\varphi\). ∎

Lemma 6.2(b) says that at the physical current the rough part of the current correction costs nothing: the saddle system solves gradient forces from \(\operatorname{ran}R\) by gauge directions. Lemma 6.2(a) says that on P82's operator the same holds up to a curvature commutator in divergence form.

### 6.3 Attack 1: perturbation from frozen P82 Theorem P

*Plan.* O1D (I-c) (L48–50): \(H=(1+T^\circ E_{\mathbf J})^{-1}H^\circ\), where \(T^\circ,H^\circ\) are the field blocks of P82's \(S^{\circ-1}\) and \(E_{\mathbf J}=M_{\mathbf J}-M^\circ\). Frozen Theorem P (`p82.md` L203–213) bounds \(T^\circ:F_w\to X_w\) and \(H^\circ:Y_w\to X_w\). If \(\|E_{\mathbf J}\|_{X_w\to F_w}\le c(\kappa+\gamma_0)\), a Neumann series gives [PW] at \(s\equiv\mathbf1\).

*Where it fails.* \(E_{\mathbf J}\) contains \(-\Delta'_\pi[\mathbf J]\), and by Lemma 6.1 this contains the force \(D(RG'D^{\mathsf T}Z)\), with \(Z=-\tfrac i2[\mathbf J,\lambda_A]\) merely bounded. Theorem P accepts only forces in \(F_w\), a supremum norm. The map \(Z\mapsto DRG'D^{\mathsf T}Z\) is a second-order singular operator; its flat continuum analogue \(\nabla\Delta^{-1}\nabla\cdot\) (a matrix of second-order Riesz transforms) is unbounded on \(L^\infty\). No frozen or library text bounds it from bounded fields to \(F_w\): O1D L52 states the route "needs no bound on \(E_{\mathbf J}\) in \(X_w\to F_w\), which would require the transpose of \(\lambda_A=G'RD^{\mathsf T}A\)", and `a3-clauses.md` L238: "The transpose needs the column half of BGR11, which neither Theorem P nor Theorem P\(^{\mathsf c}\) asserts." So the premise of the Neumann series is not available, and its continuum analogue is false. **Attack 1 fails** at the third term of (6.1).

*Restricting the current does not repair it.* One might add a Hölder condition on \(\mathbf J\) to the domain. But the physical current itself is rough at the mesh scale. ST1 L488: "Criticality in the straightened fibre implies \(J=\widehat Q^{\mathsf T}\ell^{\mathsf T}J\)". So \(J=\widehat Q^{\mathsf T}\nu\) for a row field \(\nu\). At flat \(U\), "The flat straightened row is the straight-segment average over its pillar" (`a3-clauses.md` L51), so \(\widehat Q^{\mathsf T}\nu\) at a fine bond is a sum, over the rows reading that bond, of fixed averaging weights times \(\nu(c)\). It is constant on the pieces of each double block and changes by \(O(|\nu|)\) across block faces, over one mesh step. Its Hölder seminorm at the mesh scale is therefore of order \(|\nu|\eta^{-\beta}\) whenever adjacent rows have different multipliers. A domain that bounds \(\mathbf J\) in a Hölder norm would exclude physical points. (This remark is not used below.)

### 6.4 Attack 2: the eliminated system, with flux estimates, at \(s\equiv\mathbf1\)

*Plan.* Keep the rough term as a gradient \(D\varphi\) and solve it by Lemma 6.2 instead of bounding it as a force. What remains is a curvature commutator in divergence form, \(q^{\mathsf T}\mathcal C\chi\), with a **Hölder** flux. So one needs P82's Theorem P with divergence-form sources whose flux is Hölder, and four scalar estimates. The flat input of that extension is a mesh-uniform Schauder estimate for divergence-form sources (Lemma F); I prove it here.

#### 6.4.1 The flat flux estimate

Work on \(\eta\mathbb Z^4\) with the notation of cp12 §9.1 (`cp12-draft.md` L301): \(D_i^\pm\), \(\Delta_\eta=\sum_iD_i^-D_i^+\), \(p_t^\eta\), \(G_\mu=\int_0^\infty e^{-\mu^2t}p^\eta_t\,dt\), \(R_\mu f=G_\mu*f\) (measure \(\eta^4\times\)counting). Imports: cp12 Lemma 9.1 (9.3), Lemma 9.2 and Theorem 9.3 (L325–346), drafted, not refereed; they rebuild SA's (BGH2)–(BGH20), SA 12385–12722. For a function \(g\) on a set \(Q\), \([g]_{\beta,Q}=\sup_{x\ne x'\in Q}|g(x)-g(x')|/|x-x'|^\beta\).

**Lemma F.1 (moments).** For \(r\in\{2,3\}\), \(0\le\beta<1\), and any product \(D^r\) of \(r\) differences: \(\sum_x\eta^4|x|^\beta|D^rp_t^\eta(x)|\le C_{r,\beta}t^{(\beta-r)/2}\) for \(t\ge\eta^2\), and \(\le C_{r,\beta}\eta^{\beta-r}\) for \(0\le t\le\eta^2\). *Status: proved from (9.3).*

*Proof.* Let \(t\ge\eta^2\), \(\rho=\sqrt t\). Split into \(|x|<\rho\) and shells \(2^k\rho\le|x|<2^{k+1}\rho\), \(k\ge0\). By (9.3) with \(N=1\) and \(a=0\), resp. \(a=2^k\rho\), the sum is at most \(\rho^\beta C_{r,1}t^{-r/2}+\sum_{k\ge0}(2^{k+1}\rho)^\beta C_{r,1}t^{-r/2}(1+2^k)^{-1}\). Since \(\beta<1\), \(\sum_k2^{(k+1)\beta}(1+2^k)^{-1}\le2\sum_k2^{-k(1-\beta)}<\infty\). For \(t\le\eta^2\) use the second line of (9.3) with \(\rho=\eta\) in the same way. ∎

**Lemma F.2 (the flux operator).** Let \(\mu>0\), \(\mu\eta\le1\), \(0<\beta<1\), and let \(g\) be bounded on \(\eta\mathbb Z^4\) with \([g]_\beta<\infty\). For any two differences \(D_a,D_b\) (forward or backward, any directions), \(w=D_aR_\mu D_bg\) satisfies
\[
 \|w\|_\infty\le C_\beta\mu^{-\beta}[g]_\beta,\qquad [w]_\beta\le C_\beta[g]_\beta .
\]
*Status: proved* from (9.3) and Lemma F.1.

*Proof.* Differences commute with convolution, so \(w=k*g\) with \(k=D_aD_bG_\mu=\int_0^\infty e^{-\mu^2t}D_aD_bp_t\,dt\); the integral converges absolutely in \(\ell^1\) by Lemma 9.2(d). The sum of a difference of an \(\ell^1\) function vanishes, so \(\sum_z\eta^4k(z)=0\) and \(w(x)=\sum_z\eta^4k(z)(g(x-z)-g(x))\). Hence, by Lemma F.1 with \(r=2\) and Fubini,
\[
 |w(x)|\le[g]_\beta\Big(\int_0^{\eta^2}C\eta^{\beta-2}dt+\int_{\eta^2}^\infty e^{-\mu^2t}Ct^{\beta/2-1}dt\Big)\le C[g]_\beta(\eta^\beta+\Gamma(\beta/2)\mu^{-\beta})\le C_\beta\mu^{-\beta}[g]_\beta .
\]
For the seminorm fix lattice points \(x\ne x'\), \(h=x'-x\), so \(|h|\ge\eta\). Write \(w=\int_0^\infty e^{-\mu^2t}w_t\,dt\), \(w_t=k_t*g\), \(k_t=D_aD_bp_t\). For \(t\le|h|^2\), bound \(|w_t(x')|+|w_t(x)|\) as above; the integral over \(t\le|h|^2\) is at most \(C[g]_\beta(\eta^\beta+|h|^\beta)\le2C[g]_\beta|h|^\beta\). For \(t>|h|^2\), using \(\sum k_t=0\) twice,
\[
 w_t(x')-w_t(x)=\sum_z\eta^4\,[k_t(z+h)-k_t(z)]\,(g(x-z)-g(x)) .
\]
Join \(0\) to \(h\) by a coordinate path of at most \(|h|_1/\eta\le2|h|/\eta\) steps \(p_0=0,\dots,p_n=h\). Then \(k_t(z+h)-k_t(z)=\sum_j\eta(D^{(j)}k_t)(z+p_{j-1})\), each \(D^{(j)}\) a unit difference, and \(|z|^\beta\le|z+p_{j-1}|^\beta+|h|^\beta\). By Lemma F.1 with \(r=3\) (and with \(\beta=0\)),
\[
 |w_t(x')-w_t(x)|\le[g]_\beta\cdot2|h|\cdot C\big(t^{(\beta-3)/2}+|h|^\beta t^{-3/2}\big).
\]
Integrating over \(t>|h|^2\) gives \(C[g]_\beta|h|(|h|^{\beta-1}\tfrac2{1-\beta}+2|h|^{\beta-1})\le C_\beta[g]_\beta|h|^\beta\). ∎

**Lemma F.3 (interior flux Schauder estimate).** Let \(R\ge64\eta\), and let \(u\) be defined on \(Q_{2R}\) (centred at a lattice point) with
\(\Delta_\eta u=f+\sum_jD_j^{\pm}g_j\)
at every point the equation needs there. Put \(M=\|u\|_\infty\), \(F=\|f\|_\infty\), \(\Gamma_0=\max_j\|g_j\|_\infty\), \(\Gamma_\beta=\max_j[g_j]_\beta\), all on \(Q_{2R}\). On \(Q_{R/2}\), with differences in its one-mesh enlargement,
\[
 \|Du\|_\infty\le C_\beta(R^{-1}M+RF+\Gamma_0+R^\beta\Gamma_\beta),\qquad
 [Du]_\beta\le C_\beta(R^{-1-\beta}M+R^{1-\beta}F+R^{-\beta}\Gamma_0+\Gamma_\beta).
 \tag{6.2}
\]
*Status: proved* from cp12 Lemma 9.2, Theorem 9.3's proof and Lemma F.2. The constant does not depend on \(\eta\), \(R\) or the volume. It applies componentwise to vector-valued \(u\).

*Proof.* Follow cp12 Theorem 9.3 (L346) with \(\chi=\chi_0(\cdot/R)\), \(v=\chi u\), \(\mu=1/R\). Then \((-\Delta_\eta+\mu^2)v=\chi(-f+\mu^2u)-\chi\sum_jD_j^\pm g_j-[\Delta_\eta,\chi]u\). The discrete product rule gives \(\chi D_j^\pm g_j=D_j^\pm(\chi g_j)-(D_j^\pm\chi)\,\tau_j^\pm g_j\), with \(\tau_j^\pm\) a one-mesh shift. So
\[
 v=R_\mu a-\sum_jR_\mu D_j^\pm(\chi g_j)+\sum_jR_\mu\big[(D_j^\pm\chi)\tau_j^\pm g_j\big]-R_\mu[\Delta_\eta,\chi]u,\qquad a=\chi(-f+\mu^2u).
\]
(i) \(\|a\|_\infty\le F+R^{-2}M\); Lemma 9.2(b),(c) give \(|DR_\mu a|\le CR(F+R^{-2}M)\), \([DR_\mu a]_\beta\le CR^{1-\beta}(F+R^{-2}M)\). (ii) \(|(D_j\chi)\tau g_j|\le CR^{-1}\Gamma_0\); Lemma 9.2(b),(c) give contributions \(C\Gamma_0\) and \(CR^{-\beta}\Gamma_0\). (iii) Extend \(\chi g_j\) by zero. Since \(\chi\) is smooth at scale \(R\) and vanishes outside \(Q_{3R/2}\), \([\chi g_j]_\beta\le\Gamma_\beta+C\Gamma_0R^{-\beta}\) on all of \(\eta\mathbb Z^4\): for two points in the support use \(|\chi(x)g(x)-\chi(x')g(x')|\le|g(x)-g(x')|+|g||\chi(x)-\chi(x')|\) and \(|\chi(x)-\chi(x')|\le\min(1,CR^{-1}|x-x'|)\le CR^{-\beta}|x-x'|^\beta\); if one point is outside, apply the same with \(g(x')\) replaced by \(g(x)\). Lemma F.2 gives \(|DR_\mu D_j(\chi g_j)|\le C_\beta R^\beta(\Gamma_\beta+C\Gamma_0R^{-\beta})\) and \([\cdot]_\beta\le C_\beta(\Gamma_\beta+C\Gamma_0R^{-\beta})\). (iv) The commutator term is bounded exactly as in cp12 L346, by \(CM/R\) for one difference and with Hölder constant \(C_\beta MR^{-1-\beta}\). On \(Q_{R/2}\), \(v=u\) with all differences used. Adding (i)–(iv) proves (6.2). ∎

#### 6.4.2 The local estimate with flux, at real or complex links

**Lemma 5\(^{\rm div}\) (local estimate with a divergence source).** Let \(Q\) be a lattice cube of side \(r\ge128\eta\), \(Q^+\) the concentric cube of side \(2r\), with the equation and its stencils available there. Suppose, in a gauge with \(U=e^{i\eta A_0}\) (real or complex), \(r|A_0|+r^2|\nabla A_0|\le a\), and
\[
 \Delta_Uu=f+\sum_\nu D_\nu^\pm g_\nu+Eu,\qquad |Eu(x)|\le Car^{-2}\max_{|x'-x|_\infty\le2\eta}|u(x')| .
\]
For a fixed sufficiently small \(a\le a_0^{\rm div}\) and \(0<\beta<1\),
\[
 |u|_Q+r|\nabla_Uu|_Q+r^{1+\beta}[\nabla_Uu]_{\beta,Q}
 \le C_\beta\big(r^{-2}\|u\|_{2,Q^+}+r^2\|f\|_{\infty,Q^+}+r\|g\|_{\infty,Q^+}+r^{1+\beta}[g]_{\beta,Q^+}\big).
 \tag{6.3}
\]
*Status: proved* from Lemma F.3 and `dec-field.md` Lemma 3.2, (3.5) (a Codex research text, not refereed; (3.5) is the flat value estimate "\(|u|\le C(r^{-2}\|u\|_{2,\mathrm{outer}}+r|g|+r^2|F|)\)" for \(\Delta_\eta u=D^{\mathsf T}g+F\), L126–129). No Kato inequality is used, so complex links are allowed.

*Proof.* *Step 0 (rewrite).* As in P82 L401–405, componentwise \(\Delta_Uu-\Delta u=\mathcal B\nabla u+\mathcal C_0u\) with \(|\mathcal B|\le Ca/r\), \(|\mathcal C_0|\le Ca/r^2\), and also \(|\nabla\mathcal B|\le Ca/r^2\) (it uses \(\nabla A_0\)). By the product rule, \(\mathcal B_\nu D_\nu^+u=D_\nu^+(\widetilde{\mathcal B}_\nu u)-(D_\nu^+\widetilde{\mathcal B}_\nu)u\) with \(\widetilde{\mathcal B}_\nu(y)=\mathcal B_\nu(y-\eta e_\nu)\). So
\[
 \Delta u=f'+\sum_\nu D_\nu^\pm g'_\nu,\qquad g'_\nu=g_\nu-\widetilde{\mathcal B}_\nu u,\quad f'=f+Eu-\mathcal C_0u+\textstyle\sum_\nu(D_\nu^+\widetilde{\mathcal B}_\nu)u,
\]
with \(|g'|\le|g|+Car^{-1}|u|\), \(|f'|\le|f|+Car^{-2}\max_{2\eta}|u|\), and \([\widetilde{\mathcal B}]_{\beta}\le Car^{-1-\beta}\) on \(Q^+\) (from \(|\nabla\mathcal B|\le Ca/r^2\) and \(|x-x'|\le2r\)).

*Step 1 (value).* Let \(d_+(x)\) be the distance to \(\partial Q^+\) and \(\Phi=\sup_{Q^+}(d_+/r)^2|u|\). For \(d_+(x)\ge32\eta\) apply (3.5) on the cube of side \(d_+(x)/2\) about \(x\), with its enlargement in \(Q^+\). There \(|u|\le4(r/d_+(x))^2\Phi\), so \(d_+|g'|\le d_+|g|+4Ca(r/d_+)\Phi\) and \(d_+^2|f'|\le d_+^2|f|+4Ca\Phi\). Multiplying (3.5) by \((d_+(x)/r)^2\le1\) and using \(d_+\le2r\):
\(\Phi\le C(r^{-2}\|u\|_{2,Q^+}+r\|g\|_\infty+r^2\|f\|_\infty)+Ca\Phi\).
For \(d_+<32\eta\) use \(|u(x)|\le\eta^{-2}\|u\|_2\) and \(d_+<32\eta\). Absorb \(Ca\Phi\) for \(a\) small. This bounds \(|u|\) on the cube of side \(3r/2\) by the right side of (6.3) times \(C\).

*Step 2 (gradient).* On the cube \(Q'\) of side \(3r/2\), let \(d_1(x)\) be the distance to \(\partial Q'\) and \(\Psi=\sup_{Q'}d_1|\nabla u|\). At \(x\) with \(d_1(x)\ge256\eta\), apply (6.2) with \(R=d_1(x)/4\) on \(Q_{2R}(x)\subset Q'\). On \(Q_{2R}(x)\), \(|\nabla u|\le2\Psi/d_1(x)\), and for \(y,y'\) there, \(|u(y)-u(y')|\le C|y-y'|^\beta R^{1-\beta}\Psi/d_1(x)\) by summing differences along a coordinate path (for \(|y-y'|\ge\eta\)). Hence
\(R^\beta[\widetilde{\mathcal B}u]_\beta\le R^\beta(|\widetilde{\mathcal B}|[u]_\beta+[\widetilde{\mathcal B}]_\beta|u|)\le Ca\,\Psi/r+Ca(R/r)^{\beta}r^{-1}\sup|u|\).
Multiplying the first line of (6.2) by \(d_1(x)=4R\le2r\) gives
\(d_1|\nabla u(x)|\le C(\sup_{Q'}|u|+r^2\|f\|_\infty+r\|g\|_\infty+r^{1+\beta}[g]_\beta)+Ca\Psi\).
For \(d_1(x)<256\eta\), one difference and the value bound give \(d_1|\nabla u|\le C\sup|u|\). Absorb \(Ca\Psi\). So \(|\nabla u|\le C(\ldots)/r\) on the cube of side \(5r/4\), whose distance from \(\partial Q'\) is \(r/8\).

*Step 3 (Hölder).* For \(x\in Q\), apply (6.2) with \(R=r/16\) on \(Q_{2R}(x)\), inside the \(5r/4\) cube. Every term on the right is now bounded by Steps 1–2, including \(R^{-\beta}|g'|\) and \([g']_\beta\le[g]_\beta+Car^{-1}r^{-\beta}(\sup|u|+r\sup|\nabla u|)\). Covariant differences differ from flat ones by \(\mathcal B\)-terms of size \(Ca/r\), whose change over distance \(t\) is at most \(C(|\nabla A_0||u|+|A_0||\nabla u|)t\), as in P82 L416–419. This gives the Hölder member of (6.3). ∎

#### 6.4.3 P82 with flux sources, and the scalar estimates

Use P82's notation (§1 of `p82.md`), the cell gauge of its Lemma 1, the weight classes \(\mathcal W_\theta\), and the norms
\[
 \|g\|_{G^\beta,w}=\sup_yw(y)\big(m_y^2|g|_y+m_y^{2+\beta}[g]_{\beta,y^+}\big)\ \ (\text{2-forms}),\qquad
 \|\varphi\|_{\Phi^\beta,w}=\sup_yw(y)\big(m_y^2|\varphi|_y+m_y^{2+\beta}[\varphi]_{\beta,y^+}\big)\ \ (\text{site fields}),
\]
the Hölder seminorms taken in the cell gauge on the pillar's read neighbourhood \(y^+\). On interior cells I take the cell gauge to be the one of cp12 Theorem 9.9 ((9.2): \(|A|\le C_{\rm F}a\xi^{-1}\), \(|\nabla A|\le C_{\rm F}a\xi^{-2}\), \([\nabla A]_\alpha\le C_{{\rm F},\alpha}a\xi^{-2-\alpha}\)); it meets the ceiling of P82 Lemma 5 after fixing \(a\), and it gives the curvature a Hölder bound. \(X^\beta_w\) is \(X_w\) with the Hölder member \(\sup_yw(y)m_y^{2+\beta}[\nabla_Ua]_{\beta,y}\) of (15).

**Proposition P\(^{\rm div}\) (Theorem P with divergence sources).** Under the hypotheses of frozen Theorem P, for every 2-form \(g\) and \(w\in\mathcal W_\theta\), \(\theta\le\theta_0\),
\[
 (a,\ell)=S_q^{\circ-1}(f+q^{\mathsf T}g,\,b):\qquad
 \|a\|_{X^\beta,w}+\|\ell\|_{Y,w}\le C^\circ_{\rm div}\big(\|f\|_{F,w}+\|g\|_{G^\beta,w}+\|b\|_{Y,w}\big),
\]
with \(C^\circ_{\rm div}=C(L,\alpha_{\rm H})\).

**Scalar estimates S1–S4.** Under the same hypotheses, with \(\lambda_a=SRD^{\mathsf T}a\):
- **S1.** \(\|DRSY\|_{F,w}\le C\sup_yw(y)m_y^4|Y|_y\) for site fields \(Y\) (note \(RG'=(G'R)^{\mathsf T}=RS\)).
- **S2.** \(\sup_yw(y)|\lambda_a|_y+\|D\lambda_a\|_{X^\beta,w}\le C\|a\|_{X^\beta,w}\).
- **S3.** \(\|RSD^{\mathsf T}Z\|_{\Phi^\beta,w}\le C\sup_bw(b)m_b^3|Z(b)|\) for bond fields \(Z\).
- **S4.** For \(\varphi\in\operatorname{ran}R\), \(\chi_\varphi=S\varphi\): \(\sup_yw(y)|\chi_\varphi|_y+\|D\chi_\varphi\|_{X^\beta,w}\le C\|\varphi\|_{\Phi^\beta,w}\).

*Status of P\(^{\rm div}\) and S1–S4: proved here only in outline* (Outstanding until the rerun below is written out in full and checked against P82 L342–540). The outline:

1. *Energy (P82 Lemma 4, frozen).* \(q^{\mathsf T}g\in\mathcal X^*\) with \(\|q^{\mathsf T}g\|_{\mathcal X^*}\le\|g\|_2\), since \(\langle q^{\mathsf T}g,v\rangle=\langle g,qv\rangle\) and the energy norm contains \(\|qv\|_2\); likewise \(D^{\mathsf T}Z\) for the scalar system. Pillar- or tile-supported pieces with the normalizations above have \(\|g\|_2\le C\), because a pillar has volume \(m_z^4\). Lemma 4's decay (23) applies unchanged.
2. *Pointwise (P82 Lemma 6 with Lemma 5\(^{\rm div}\)).* For a source \(q^{\mathsf T}(\psi_zg)\) with \(\psi_z\) one of I2's smooth tile cutoffs, row 3 of (8) is unchanged, so (29) holds. Row 1, (30), gains \(q^{\mathsf T}(\psi_zg)\). In the cell gauge, \(q^{\mathsf T}g=\sum_\nu D_\nu^\pm g_{\nu\mu}\) plus zero-order transport terms with coefficients \(\le Ca/r\); the latter are bounded forces. Lemma 5\(^{\rm div}\) replaces Lemma 5 in P82 L499–500. The other forcing terms of (30) are bounded as in L491–498. This gives (27) for the flux piece.
3. *Weights (P82 Lemma 7).* Decompose \(g=\sum_z\psi_z^2g\) with I2's cutoffs (\(|D\psi_z|\le C_L/(M_Ps_z)\), bounded overlap \(N_L\)); \([\psi_z^2g]_\beta\le[g]_\beta+C(M_Ps_z)^{-\beta}|g|\). Sum with I4 as in L511–519.
4. *S1.* \(RSY=SY-PSY\). Here \(\psi=SY\) solves \(A_s\psi=Y\); treating \(Q'^{\mathsf T}m^{-2}Q'\psi\) as a bounded right side as in P82 L456–461, Lemma 5 bounds \(|D\psi|\le Cm^{-3}\). And \(|SY|\le Cm^{-2}\) by the same lemma, so P82 (28) (L433–436, for sources with \(|g|\le m_z^{-2}\)) bounds \(|DPSY|\le Cm^{-3}\). Weights as in P82 Lemma 7.
5. *S2, S4.* Values and first differences by Lemma 5 with bounded right side (\(RD^{\mathsf T}a=D^{\mathsf T}a-PD^{\mathsf T}a\), with \(|D^{\mathsf T}a|\le C_Lm^{-2}\|a\|_X\) by P82 L521). For second differences put \(v=D\lambda_a\) (resp. \(D\chi_\varphi\)): in the cell gauge \(\Delta v=D(RD^{\mathsf T}a)\) (resp. \(D\varphi\)) plus commutator terms of zero and first order with coefficients \(Ca/r^2,Ca/r\); the source is a gradient of a scalar with Hölder bound, a flux of Lemma 5\(^{\rm div}\).
6. *S3.* The value and Hölder estimate for \(A_s\psi=D^{\mathsf T}Z\) with merely bounded \(Z\): flat input \(\|R_\mu D^{\mathsf T}Z\|_\infty\le C\mu^{-1}\|Z\|_\infty\) and \([R_\mu D^{\mathsf T}Z]_\beta\le C_\beta\mu^{\beta-1}\|Z\|_\infty\), which are cp12 Lemma 9.2(b),(c) for the reflected kernel; localization as in Theorem 9.3; then \(RS=S-PS\) with \(PS\) smoothing by (28).

#### 6.4.4 The reduction at \(s\equiv\mathbf1\)

**Theorem R1 ([PW] at \(s\equiv\mathbf1\)).** Let \(U\) be real and satisfy the hypotheses of frozen Theorem P, with curvature parameter \(\kappa\) (cp12 Theorem 4.1's normalization; this \(\kappa\) is P82's \(\kappa_{\rm A3}\), L188, not IN1's rate \(\kappa\), and in this subsection only it has that meaning) and Hölder curvature in the cell gauge, \(m^{2+\beta}[U(\partial p)\text{-coefficient}]_\beta\le C\kappa\) (this is cp12 Theorem 9.9, (9.2)). Let \(\mathbf J\) be an independent current with \(\|\mathbf J\|_{F,1}\le\gamma\). Let \(S_{\mathbf J}=\begin{pmatrix}M_{\mathbf J}&-K^{\mathsf T}\\K&0\end{pmatrix}\), \(M_{\mathbf J}=\Delta+DRD^{\mathsf T}-\Delta'_\pi[\mathbf J]\), \(\Delta=q^{\mathsf T}q+\Delta'\) the Wilson Hessian with its curvature part \(\Delta'\) (`a3-derivative.md` 7.1, L435–436: \(\|\Delta'v\|_{F,w}\le C\kappa\|v\|_{X,w}\)). Assume P\(^{\rm div}\) and S1–S4. Then there is \(c_\sharp=c_\sharp(L,\alpha_{\rm H})>0\) such that, if \(\kappa+\gamma\le c_\sharp\), \(S_{\mathbf J}\) is invertible and
\[
 \|a\|_{X^\beta,w}+\|\ell\|_{Y,w}\le2C^\circ_{\rm div}\big(\|f\|_{F,w}+\|b\|_{Y,w}\big),\qquad(a,\ell)=S_{\mathbf J}^{-1}(f,b),
 \tag{6.4}
\]
for all \(w\in\mathcal W_\theta\), \(\theta\le\theta_0\). In particular \(H(\mathbf1)=\ell\) (the lift, Proposition 3.1(i)) satisfies the \(H\)-part of Lemma PW♮ at \(s\equiv\mathbf1\). *Status: proved, as an implication from frozen Theorem P, P\(^{\rm div}\), S1–S4, a3-derivative 7.1 (gated) and cp12 Theorem 9.9 (drafted).*

*Proof.* \(S_{\mathbf J}=S_q^\circ+\mathfrak V\), \(\mathfrak V=\operatorname{diag}(\Delta'-\Delta'_\pi[\mathbf J],0)\). I show \(\|S_q^{\circ-1}\mathfrak V\|\le C_\sharp(\kappa+\gamma)\) on \(X^\beta_w\oplus Y_w\); then the Neumann series \(S_{\mathbf J}^{-1}=\sum_n(-S_q^{\circ-1}\mathfrak V)^nS_q^{\circ-1}\) converges for \(C_\sharp(\kappa+\gamma)\le\frac12\), and (6.4) follows from P\(^{\rm div}\) at \(g=0\).

(i) \(S_q^{\circ-1}(\Delta'a,0)\): Theorem P and \(\|\Delta'a\|_F\le C\kappa\|a\|_X\).

(ii) By Lemma 6.1, \(\Delta'_\pi[\mathbf J]a=E_0a+DRSY_a+D\varphi_a\) (using \(G'R=SR\), \(RG'=RS\)), with \(\varphi_a=RSD^{\mathsf T}Z_a\). By S2, \(|\lambda_a|\le C\|a\|_X\) and \(m|D\lambda_a|\le C\|a\|_{X^\beta}\), so \(\|E_0a\|_F\le C\gamma\|a\|_{X^\beta}\), \(\sup m^4|Y_a|\le C\gamma\|a\|_{X^\beta}\), \(\sup m^3|Z_a|\le C\gamma\|a\|_{X^\beta}\) (weights carried along; all reads are local). S1 bounds \(\|DRSY_a\|_F\le C\gamma\|a\|_{X^\beta}\); Theorem P handles these two forces.

(iii) The gradient \(D\varphi_a\), \(\varphi_a\in\operatorname{ran}R\): by Lemma 6.2(a), \(S_q^{\circ-1}(D\varphi_a,0)=(D\chi,0)-S_q^{\circ-1}(q^{\mathsf T}\mathcal C\chi,0)\), \(\chi=S\varphi_a\). By S3 and S4, \(\|D\chi\|_{X^\beta}\le C\gamma\|a\|_{X^\beta}\) and \(\sup|\chi|\le C\gamma\|a\|_{X^\beta}\). The flux \(\mathcal C\chi\) has \(\|\mathcal C\chi\|_{G^\beta}\le C\kappa(\sup|\chi|+\sup m|D\chi|+\cdots)\le C\kappa\gamma\|a\|_{X^\beta}\), by Lemma 6.2(a)'s formula, Reg and the Hölder curvature bound. P\(^{\rm div}\) bounds the last term.

Summing (i)–(iii) gives the claim with \(C_\sharp\) depending on \(C^\circ_{\rm div}\) and the constants of S1–S4. For the lift, \(H(\mathbf1)b\) is the field part of \(S_{\mathbf J}^{-1}(0,\mathsf m^{-1}b)\) by Proposition 3.1(i) and O1D (I-a). ∎

**The other two operators at \(s\equiv\mathbf1\).** \(\mathfrak G\) of ST1 (38) is the field block of the saddle inverse with \(M_{\mathbf J}\) replaced by \(G_1^{-1}\)-form \(M_{\mathbf J}-\Pi^{\mathsf T}\Delta^{(2)}[\ell^{\mathsf T}\mathbf J]\Pi\) and constraints \(\widehat QA=0\), \(RD^{\mathsf T}A=0\) (ST1 (39): "\(\widehat Q\mathfrak G=RD^{\mathsf T}\mathfrak G=0\) … \(\mathfrak GG_1^{-1}|_{\mathcal K}=I\)"). \(\Pi=I-P_g\), \(P_ga=D\lambda_a\), and \(P_g^{\mathsf T}f=DRSD^{\mathsf T}f\) is again a gradient from \(\operatorname{ran}R\). With \(|\ell^{\mathsf T}\mathbf J|\le C_H\gamma\) by (O1) and h-walk's absolute second-jet coefficient premise for \(\Delta^{(2)}\) (`dec-field.md` L171), the same three steps apply; so do they for \(\ell_1\). I do not write these out; they add nothing new beyond (i)–(iii). *Status: as Theorem R1, plus the second-jet premise.*

**Complex pairs.** At \(\mathbf U=e^{i\eta A'}U\), replace frozen Theorem P by Theorem P\(^{\mathsf c}\) (`a3-clauses.md` L171: "proved here as an implication on the same inputs as Theorem P … no Kato step is taken at complex links"; same-model, not frozen). Lemma 5\(^{\rm div}\) holds at complex links (no Kato step). Lemma 6.2 is used only at the real factor \(U\); the differences of all operators between \(\mathbf U\) and \(U\) are zero-order in the transports (\(|\operatorname{Ad}e^{i\eta A'}-1|\le C\eta|A'|\)) and enter as further small terms of \(\mathfrak V\) of the three kinds above. *Status: outline; Outstanding with P\(^{\rm div}\).*

*Why Attack 2 stops.* It proves nothing at \(s\ne\mathbf1\). Its engine is that \(H(\mathbf1)\) is a block of an **inverse**: Lemma 6.2 and the Neumann series are statements about solutions of \(S_{\mathbf J}(a,\ell)=(f,b)\). For \(|s_\Delta|<e^{\bar\kappa}\), \(s\ne\mathbf1\), the decoupled \(H(s)\) of Definition D satisfies no equation: "It requires no identity between decoupled sums" (O1D L103, SA mechanism (j), SA 10562), and "Vanishing parameters near a row. Then \(QH(s)=0\) there, not \(1\)" (O1D L162). So the step "solve the gradient force by a gauge direction" has no meaning for \(H(s)\). **Attack 2 fails at \(s\ne\mathbf1\)**, for this reason.

### 6.5 Attack 3: pointwise bounds at \(s\ne\mathbf1\) through a different specification

Lemma PW♮ at \(s\ne\mathbf1\) needs either termwise pointwise bounds for the walk terms of Definition D, or a specification in which \(H(s)\) is assembled from **inverses**, to which Attack 2 applies.

#### 6.5.1 Termwise bounds for Definition D

O1D Definition D sums \(s^\omega[T_\omega]_{A\nu}\) over the walks of h-walk Theorem W for the **unfolded** eight-unknown system \(\mathbb K[S,P,j]\) (O1D L105, L46). There the gauge scalar \(\lambda\) is an independent unknown. Termwise pointwise bounds are `dec-field.md` [PW-term], (6.1) (L293–300), "open". The scalar rows of the unfolded local systems carry the current form (dec-field (3.2), L87): \(\langle\ldots-i[\lambda,D\mu]-i[\mu,D\lambda],J\rangle_f\). In the scalar row this is a divergence \(D^{\mathsf T}([\mathbf J,\lambda])\) with merely bounded flux **plus** the zero-order term \([\mathbf J,D\lambda]\). For the first, Lemma F gives nothing better than a value and Hölder bound for \(\lambda\) (as in S3). The second then needs a pointwise bound on \(D\lambda\), which that gives not. dec-field Proposition 2.1 (L31–60) is the concrete form of this: at flat links an admissible staggered current makes the scalar-slot coefficient of order \(\gamma_0/\eta\). In the eliminated form of Attack 2 the scalar is \(\lambda_a=SRD^{\mathsf T}a\), a smooth function of the field (S2), and the rough flux only ever appears inside a gradient force that the **next** inverse absorbs (Lemma 6.2). A single walk term \(T_\omega\) is a product of local inverses and cutoff remainders and contains no such composition across its factors' boundaries. *Exact reason this part fails:* in Definition D the rough current enters the unfolded local scalar rows, where neither Lemma 6.2 nor Lemma F applies; dec-field L356 records that the repairs ("Eliminating the scalar variables before estimating the field, or proving a mixed-system estimate with a retained flux component") have not been completed, and Attack 2 completes the first only for inverses.

#### 6.5.2 A Boolean specification built from inverses

For a finite set \(\mathcal P\) of parameter cubes and a family \(F(Y)\), \(Y\subset\mathcal P\), of operators, put
\[
 D_XF=\sum_{Y\subset X}(-1)^{|X\setminus Y|}F(Y),\qquad F^{\rm BI}(s)=\sum_{X\subset\mathcal P}s^XD_XF,\qquad s^X=\prod_{\Delta\in X}s_\Delta .
 \tag{6.5}
\]

**Lemma 6.3 (Boolean interpolation).** (a) \(F^{\rm BI}(\mathbf1_Y)=F(Y)\) for every \(Y\). (b) \(F^{\rm BI}\) is a polynomial, affine in each \(s_\Delta\). (c) If \(F(Y)=F_1(Y\cap W)\oplus F_2(Y\setminus W)\) for a fixed \(W\subset\mathcal P\) and all \(Y\), then \(D_XF=0\) whenever \(X\) meets both \(W\) and \(\mathcal P\setminus W\); hence \(F^{\rm BI}(s)=F_1^{\rm BI}(s|_W)\oplus F_2^{\rm BI}(s|_{\mathcal P\setminus W})\). (d) If \(\widetilde F\) is \(C^{|X|}\) on \([0,1]^X\) with \(\widetilde F(\mathbf1_Y)=F(Y)\) for \(Y\subset X\), then \(D_XF=\int_{[0,1]^X}\partial_t^X\widetilde F(t)\,dt\). (e) \(|F^{\rm BI}(s)|\le\sum_X\prod_{\Delta\in X}|s_\Delta|\,|D_XF|\) entrywise. *Status: proved (finite combinatorics and calculus).*

*Proof.* (a) Möbius inversion on the Boolean lattice: \(\sum_{X\subset Y}D_XF=\sum_{Z\subset Y}F(Z)\sum_{Z\subset X\subset Y}(-1)^{|X\setminus Z|}=F(Y)\), since the inner sum is \((1-1)^{|Y\setminus Z|}\). And \(s^X\) at \(s=\mathbf1_Y\) is \(1\) if \(X\subset Y\), else \(0\). (b) Each \(s^X\) is a product of distinct variables. (c) For \(X=X_1\sqcup X_2\), \(X_1\subset W\), \(X_2\subset\mathcal P\setminus W\), both nonempty, \(D_X[F_1(\cdot\cap W)]=\sum_{Y_1\subset X_1}(-1)^{|X_1\setminus Y_1|}F_1(Y_1)\sum_{Y_2\subset X_2}(-1)^{|X_2\setminus Y_2|}=0\), and similarly for \(F_2\). (d) Induction on \(|X|\): for \(X=X'\sqcup\{\Delta\}\), \(D_XF=D_{X'}[F(\cdot\cup\{\Delta\})-F(\cdot)]\), and \(\widetilde F|_{t_\Delta=1}-\widetilde F|_{t_\Delta=0}=\int_0^1\partial_{t_\Delta}\widetilde F\,dt_\Delta\); apply the induction hypothesis to \(\int_0^1\partial_{t_\Delta}\widetilde F\,dt_\Delta\) and use Fubini. (e) is the triangle inequality. ∎

**The specification.** Let \(F(Y)=H_{\rm cut}(Y)\) be the lift (and likewise \(H_1,\mathfrak G\)) of the **cut-down** system on the union of the cubes of \(Y\), with outer Dirichlet conventions at \(\partial Y\) as for any admissible region (P82 L218 "admissible shapes"; L448 "arbitrary outer boundary"). Define \(H^{\rm BI}(s)=F^{\rm BI}(s)\). Then:

- \(H^{\rm BI}(\mathbf1)=H\) (Lemma 6.3(a)), so D-one holds by Proposition 3.1;
- cut-down systems on wall-separated unions are direct sums, so Lemma 6.3(c) gives D-split and, since \(H_{\rm cut}(Y)\) reads the pair only on \(Y\), the two-pair locality of §3.4 on every component;
- holomorphy in \(s\) is polynomial; in \(P\) it is that of each \(H_{\rm cut}(Y)\); reality and covariance hold termwise;
- at every Boolean \(s\), \(H^{\rm BI}(s)\) is an inverse block, so Theorem R1 applies to it (on each cut-down region, given P\(^{\rm div}\) and S1–S4 there).

Lemma PW♮ at complex \(s\) would follow from Lemma 6.3(e) and a bound \(\sup_{b,c}w\text{-weighted}|D_XH_{\rm cut}|\le A\,(e^{-\bar\kappa}/4)^{|X|}\times\)(decay), by the animal count used in O1D Lemma P. By Lemma 6.3(d), \(D_XH_{\rm cut}=\int_{[0,1]^X}\partial_t^XM(t)^{-1}\) for any smooth family \(M(t)\) of systems with \(M(\mathbf1_Y)\) the cut-down systems. Take \(M(t)\) with each wall coupling between cubes \(\Delta,\Delta'\) (plaquettes, scalar stencils and rows that cross the common face) multiplied by \(t_\Delta t_{\Delta'}\): the **weighted-wall systems**. Then \(\partial_t^XM(t)^{-1}\) is a finite sum of ordered products \(\pm M^{-1}V_{\Delta_1}M^{-1}\cdots V_{\Delta_k}M^{-1}\), each \(V_\Delta=\partial_{t_\Delta}M\) or a mixed second derivative supported in a fixed neighbourhood of the walls of \(\Delta\). If every \(M(t)^{-1}\), \(t\in[0,1]^{\mathcal P}\) real, obeyed (6.4) with decay rate \(\theta\), a product visiting the walls of all cubes of \(X\) would carry \(e^{-\theta\,c\,\ell_{\mathsf P}|X|}\), and with \(\ell_{\mathsf P}\ge C\bar\kappa/\theta\) (row 5) this pays \(e^{\bar\kappa|X|}\), the \(|X|!\) orderings and the animal count, exactly as in O1D Lemma P. (This last sentence is a sketch; it is not needed for the failure below.)

*Exact reason Attack 3 fails.* It needs (6.4), uniformly in real \(t\in[0,1]^{\mathcal P}\), for weighted-wall systems \(M(t)\). No frozen or library text treats them: Theorem P is stated for the unweighted system on "admissible shapes" (P82 L218), its local models I1 are flat models with "copied one- or two-scale interface shape" (L148), and Lemma 3's bare cells use the unweighted curl. At a wall with weight \(t\in(0,1)\) the field operator has a coefficient jump of relative size \(1-t\) across one layer of plaquettes. Theorem R1's Neumann series runs in \(X^\beta_w\), with the Hölder member of \(\nabla a\). In the continuum transmission analogue (a divergence-form operator with coefficient \(t\) on one side of a hyperplane and \(1\) on the other) the normal derivative of a solution jumps by the factor \(t\), so a uniform Hölder bound on \(\nabla a\) across the wall is false; on the lattice the same jump occurs across one mesh step, which would make \([\nabla a]_\beta\) grow like \(\eta^{-\beta}\). (I have not written a lattice counterexample; this is the reason the method cannot be applied, not a proof that Lemma PW♮ is false.) A transmission-type local estimate without the Hölder member, and a version of Theorem R1 that does not use it at walls, would be needed. **Attack 3 fails** there.

### 6.6 The remaining statement, exactly

**First remaining Outstanding statement: Lemma PW♮ (§6.1).** After the three attacks:

1. *At \(s\equiv\mathbf1\)* it is reduced, by Theorem R1 (proved as an implication), to **Proposition P\(^{\rm div}\) and S1–S4** (§6.4.3), whose flat input (Lemma F.3) and local estimate (Lemma 5\(^{\rm div}\)) are proved here, and whose assembly is a rerun of P82 Lemmas 4, 6, 7 written here in outline only. This is the first item in proof order.
2. *At \(s\ne\mathbf1\)* no specification is known for which the pointwise bound reduces to estimates on inverses with the Hölder member: Definition D fails termwise (§6.5.1), and the Boolean specification reduces it to **Lemma WW**: the bound (6.4), without loss in \(L,\alpha_{\rm H}\), uniformly in \(t\in[0,1]^{\mathcal P}\), for the weighted-wall systems \(M(t)\), in a norm that the Neumann series of Theorem R1 can use at walls.

The three attacks and their failure points:

| Attack | Idea | Where and why it fails |
|---|---|---|
| 1 (§6.3) | Perturb from frozen P82 Theorem P | The current correction contains \(D(RG'D^{\mathsf T}Z)\) with merely bounded \(Z\) (Lemma 6.1); Theorem P accepts only \(F_w\) forces; no text bounds this map into \(F_w\), and its continuum analogue (second-order Riesz transforms on \(L^\infty\)) is unbounded |
| 2 (§6.4) | Eliminate the scalars; solve the rough gradient force by gauge directions (Lemma 6.2); flux Schauder (Lemma F) | Works at \(s\equiv\mathbf1\) modulo P\(^{\rm div}\), S1–S4 (Theorem R1). Fails at \(s\ne\mathbf1\): decoupled sums satisfy no equation (O1D L103, L162) |
| 3 (§6.5) | Termwise bounds; or assemble \(H(s)\) from cut-down inverses (Lemma 6.3) | Termwise: the rough current sits in unfolded scalar rows, beyond Lemmas 6.2 and F. Boolean: needs weighted-wall systems with Hölder control across walls, which no text supplies and whose continuum analogue lacks it |

A fourth route, not attempted here: an **eliminated-form parametrix** specification, in which the local models are eliminated (field-only) systems on model boxes and each gradient force \(D\varphi\) produced in a remainder is always composed with the following local inverse before tagging. Its walk terms would be products of inverses in the sense needed by Lemma 6.2(a) and Lemma 5\(^{\rm div}\). Its remainder contains the nonlocal difference \(G'-G'_i\) of scalar inverses, which needs its own walk expansion and margin estimate.

---

## 7. Constants and their order

IN1's rule (`in1.md` L221–236, with Amendment 1, L666–675: \(L>L_0^\natural\), \(\kappa\ge\kappa_0^\natural(L)\)): uniform precision constants are fixed before \(\kappa\) and do not depend on \(M\) or \(\bar\kappa\). ST1's table (L160–171) is consistent with it: DR's "base constants/rates" are at its row 2, and \(E_{\bar\kappa}\) enters only at its row 10. Each DR constant and the row where it is fixed:

| IN1 row | Constants of this text | Depend on |
|---|---|---|
| 1 | Hölder exponent \(\beta=\alpha_{\rm H}\in(0,1)\); the (Tq0) exponents \(p_0,p_1,q,r\) | nothing |
| 2 | Odd \(L\) with \(L\ge27\) (drlocp (4)), \(L\ge13\) (ST1), \(L>L_0^\natural\) and IN1's floor; \(r_g\le8L+1\); flat constants: cp12 (9.3)'s \(C_{r,N}\), Lemma 9.2's \(C_{\rm G},C_\alpha\); Lemma F.1–F.3's \(C_{r,\beta},C_\beta\) (absolute, given \(\beta\)); Lemma 5\(^{\rm div}\)'s \(a_0^{\rm div},C_\beta\) (absolute) | \(\beta\) |
| 3 | P82's \(M_P,\alpha_*,h_*,\delta_w,\theta_0,\rho_P,C^\circ\) (P82 §2 steps 1–4); \(C^\circ_{\rm div}\) and the S1–S4 constants (P82's scheme, so the same dependence); Theorem R1's \(c_\sharp,C_\sharp\); Theorem W's \(a_*,\tau_L,B_L,C_W,\nu_1,N_L\) (O1D L142); then \(M_1,R_1\) above drlocp (4), P82 and A1 floors, \(\rho_{\mathbf B}=3LM_1\), \(r_1=16L^3M_1+4L\); \(C_H^{(1)}=C_LB_LK_{\tau_L/2}\); the [PW] constants \(C_{\rm PW},\theta_{\rm PW}\); [NL]'s \(C_W,C_C,r_0\); [Rows]'s \(C_R,r_R\); Theorem 5.1's \(\theta,\mu=\theta/2,c_*,C_D,\epsilon_D\) | \(L,\beta\) only; not \(M\), \(\bar\kappa\), \(\kappa\), depth, mesh, volume, or \(M_1\) above its floor (except that \(r_1\) and Lemma 2.3's floor read \(M_1\)) |
| 4 | IN1's \(\kappa\). DR reads nothing at this row | — |
| 5 | \(\bar\kappa\); then \(B=C_{\rm PW}e^{16\bar\kappa}\), \(C_H=C_LB_LK_{\tau_L/8}e^{16\bar\kappa}\), \(E_{\bar\kappa}=e^{48\bar\kappa}\), \(s_D=\epsilon_De^{-64\bar\kappa}\); then the response-parameter length \(\ell_{\mathsf P}\ge\max\{8r_1+1,256\bar\kappa/\tau_L\}\); then \(M\) with \(M\ge\frac L2\ell_{\mathsf P}\) (Lemma 2.3) and \(M\ge4\) (Lemma 2.4), above all other floors | row 3 and \(\bar\kappa\) |
| 6 | \(A_1,A_0,C_0,C_1\) of (Tq0); the current radius \(\gamma_0\) of the pair domain | as in IN1 |
| 9 | Coupling ceiling: the domain radii below \(a_*(L)\), \(c_\sharp\) (Theorem R1: \(\kappa_{\rm A3}+\gamma\le c_\sharp\)) and the analytic-room ceilings; \(C_A\delta_{\rm src}=C_AA_1g\ell^{p_0}<s_D/2\) | all earlier rows |

No constant of this text reads an activity amplitude \(b_f\), \(C_0\), \(C_1\) or \(M\) before row 5. The only \(\bar\kappa\)-dependence is through \(e^{16\bar\kappa}\) factors and \(s_D\), as ST1 L142–143 requires ("Keep it in every source budget. It is not an IN1 precision constant.").

## 8. Statements used wrongly, stale items, and the other Outstanding inputs

**Frozen texts.** I found no frozen text that uses a DR statement wrongly. Three points of wording:

1. `nl1-L.md` L170 attributes the component splitting to "SA 5797–5801". SA's splitting sentence is SA 5795–5797; SA 5797–5801 continue with the size bound and the \(s=1\) identification. No mathematical consequence.
2. `st1-r4.md` L138 uses "restriction consistency" and "common-lift transport" without a definition in the file. I read them as SA 5792–5794 does (§1.1) and prove the image-domain forms (Proposition 3.4(c),(d)).
3. ST1 (16) has no source ball and NL1 (7) has one; §1.5 item 1 records that they are two statements. Theorem 5.1 proves the stronger.

**Non-frozen texts.**

4. The two-current "identification" asked for in `assembly-status.md` L185 and drlocp L69 is **false** as an identity (Corollary 4.2). It is resolved by specification (Theorem 4.3). `d3-local.md` §3, `red.md` L59–94 and `loc-4.md` L207 read the force-anchored continuation \(J_*=F'_U(0)\); off the physical locus they describe a different object from ST1's DR.
5. drlocp L75's grid identification is supplied by Lemma 2.3.

**Other Outstanding inputs of DR, in proof order after Lemma PW♮.**

- **[NL]** (`dec-field.md` (5.1)): the nonlinear Lipschitz bounds of \(W_s\) and \(\mathcal C\) in the weighted norms. SA 10368–10389 asserts it; no rebuild exists. Its \(W_s\) part reads \(M_s^{\rm walk}\), \(H\), \(\mathcal C\) and the local force; under Lemma PW♮ and [Rows] it is plausible by the same Neumann bookkeeping as Theorem 5.1's Step 3, but I have not written it.
- **Import D, (T1)–(T3), DR1(b):** the walk constructions of h-walk Theorem W for \(H_1,\mathfrak G,M^{\rm walk}_s\), including the second-jet coefficient premise (`dec-field.md` L171), termwise reality, covariance and torus compatibility, and resummation at \(s\equiv\mathbf1\).
- **[Rows]:** the local row and Hessian bounds, from `a3-derivative.md` §4 and 7.1 (gated, not frozen) and `p82.md` (17).
- **(O1):** O1D Theorem B(c), same-model and ungated (O1D L16).
- **Full local domains** (drlocp L198): a regional solution on every declared \(\mathcal O_\sigma(Y;U)\) and consistency between different regional constructions.

## 9. Status of each step

| Step | Status |
|---|---|
| §1 clause statements, name clashes | bookkeeping, with line quotes |
| Lemma 2.1 (gauge form) | proved |
| Lemma 2.2 (CV representative) | proved, given Lemma 3.3's imports |
| Lemma 2.3 (grid) | proved |
| Lemma 2.4 (R-stencil) | proved |
| Proposition 3.1 (D-one) | proved, given DR1 |
| Lemma 3.2 (D-zero) | proved, given UNQ |
| Lemma 3.3 (D-real, D-cov) | proved, given (T1), (T2), UNQ |
| Proposition 3.4 (D-split, DR-locP, D-res image form, D-lift) | proved, given D, UNQ, S-loc, (T3); full local domains Outstanding |
| Proposition 4.1, Corollary 4.2, Theorem 4.3 (two currents) | proved |
| Theorem 5.1 ((7), (16), H1, R-ball) | proved, given [PW], [NL], (O1), [Rows], UNQ |
| Lemma 6.1 (decomposition), Lemma 6.2 (gauge directions) | proved |
| Lemmas F.1–F.3 (flat flux Schauder) | proved, from cp12 (9.3), Lemma 9.2, Theorem 9.3 (drafted) |
| Lemma 5\(^{\rm div}\) | proved, from Lemma F.3 and dec-field (3.5) (unrefereed) |
| Proposition P\(^{\rm div}\), S1–S4 | **Outstanding** (outline only) |
| Theorem R1 ([PW] at \(s\equiv\mathbf1\), real reference) | proved, given P\(^{\rm div}\), S1–S4, frozen Theorem P, a3-derivative 7.1, cp12 Theorem 9.9 |
| \(\mathfrak G,\ell_1\) and complex pairs at \(s\equiv\mathbf1\) | outline |
| Lemma 6.3 (Boolean interpolation) | proved |
| Lemma PW♮ at \(s\ne\mathbf1\) | **Outstanding**; reduced (Boolean route) to Lemma WW |
| [NL] | **Outstanding** |

## Result

**What is proved.** For the actual construction (Definition DR♮: O1D's decoupled operators on the fine grid, drlocp's equations, ST1's current \(J_*=\mathbf J\), ST1's chart-free (Tq0) domains with the CV representative, the Y3 relative gauge form in the Gaussian step), the following DR clauses are proved as implications from named imports: the specification at one (Proposition 3.1, from DR1); zero source, zero switches and source-free components (Lemma 3.2, Proposition 3.4); reality and real-gauge covariance, including independence of the representative (Lemmas 3.3, 2.2); splitting over face-connected components, NL1's row-locality, TD's component and stencil clauses, and drlocp's two-pair locality DR-locP for this specification (Proposition 3.4, Lemmas 2.3–2.4); restriction to wall-components and transport by common lifts on image domains (Proposition 3.4(c),(d)); independence from the Gaussian gauge form (Lemma 2.1). The two-current item is settled: the two continuations are different (Corollary 4.2, an explicit real configuration), DR's current is ST1's, and all frozen consumers read that one (Theorem 4.3). The complex-source estimate (7) with its current, hence (16), with \(E_{\bar\kappa}=e^{48\bar\kappa}\) and \(s_D=\epsilon_De^{-64\bar\kappa}\), follows from [PW], [NL], (O1) and [Rows] (Theorem 5.1).

**New mathematics.** Lemma 6.2 shows that the only rough term of the independent-current correction, a gradient \(D\varphi\) with \(\varphi\in\operatorname{ran}R\), is solved exactly by a gauge direction at the physical current, and up to a Hölder curvature commutator on P82's operator. Lemma F is a mesh-uniform Schauder estimate for lattice divergence-form sources, and Lemma 5\(^{\rm div}\) its covariant local form without a Kato step. Theorem R1 reduces [PW] at \(s\equiv\mathbf1\) to the flux extension P\(^{\rm div}\) of frozen P82 Theorem P and the scalar estimates S1–S4. This answers the obstruction recorded in `dec-field.md` Proposition 2.1 at \(s\equiv\mathbf1\), along the "eliminating the scalar variables" route that dec-field L356 names.

**First remaining Outstanding statement.** Lemma PW♮ (§6.1): weighted pointwise bounds \(B=C_{\rm PW}e^{16\bar\kappa}\) for the decoupled \(H(s),H_1(s),\mathfrak G(s)\) on the whole polydisc. At \(s\equiv\mathbf1\) it rests on P\(^{\rm div}\) and S1–S4 (outline written). At \(s\ne\mathbf1\), after three attacks (§6.6 table), it rests on termwise bounds that the unfolded systems do not support, or on Lemma WW for weighted-wall systems. [NL] and full local domains come after it.

**Constants.** All DR constants are fixed at IN1 rows 1–3, before \(\kappa\), independent of \(M\) and \(\bar\kappa\); \(\bar\kappa\) enters only through \(e^{16\bar\kappa}\)-type amplitudes, \(s_D\), \(\ell_{\mathsf P}\) and the floor \(M\ge\frac L2\ell_{\mathsf P}\) at row 5 (§7).

This is pass 1. It has not been checked by another model. Research text, not an audit; it grants no status.
