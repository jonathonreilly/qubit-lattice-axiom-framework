# Decoupled response locality, joint composition, and CI filing

Provenance: Codex (session model and reasoning setting), 2026-11-05; Pass 2 of Claude's 585-line [drlocp-draft.md](drlocp-draft.md), at repository commit 9d869d76aedfcdf38da2b030b615b9da207bddba. Research text, not an audit; grants no status. Not yet refereed.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, supply the R9 specification, walk interpolation, component argument and relative-length framework used here, at revision 31a47c543775. The component proof follows their YM3 Proposition I-91-59. The library supplies its conditional Balaban-based walk construction and the TD/TD2 tree estimates, including Bird's allocation. No run discharges a mathematical step.

## 1. Definitions, imports and order of choice

Work at a fixed finite main step, with fixed regions, cutoffs, coordinate assignments and a real reference \(U\). The independent complex pair coordinates are \(P=(A',\mathbf J)\). Comparisons use the same geometry and coordinate spaces. A restriction \(P|_Y\) retains precisely the coordinates based in cubes of \(Y\); boundary assignments are fixed once. Holomorphy below is on this fixed-\(U\) fibre.

Fine cubes have side \(M\) in level-\((i-1)\) units. Their graph has corner adjacency, degree at most \(80\), periodic distance \(d\), neighbourhoods \(N_r\), and covering-tree length \(\operatorname{St}\), allowing extra vertices. Assign each free scalar fluctuation coordinate to one cube; \(|\zeta|_c\) is the maximum modulus of coordinates owned by \(c\), zero if none. Wall-components instead use face adjacency. All graph lengths here are in fine-cube units. For a nonempty set \(X\), define \(m_X(V)\) as the MST weight on \(V\cup\{*\}\), with
\[
 w(v,v')=d(v,v'),\qquad w(v,*)=d(v,X),\qquad m_X(\varnothing)=0.
 \tag{1}
\]
These root weights need not form a metric. We use the proved finite-graph facts of TD Lemma 1: rooted \(n\)-cube animals number at most \(6400^{n-1}\); \(\operatorname{St}\le\operatorname{MST}\le2\operatorname{St}\); for \(s\ge6\),
\[
 \sup_x\sum_y e^{-sd(x,y)}\le2,\qquad
 \sum_{|Z|=n}e^{-s\operatorname{MST}(Z\cup\{x\})}\le2(2e)^n.
 \tag{2}
\]
Bird's allocation assigns MST parent costs \(l_v\) with total \(m_X(V)\) and \(\sum_{v\in A}l_v\le\operatorname{MST}(A\cup\{*\})\).
Realizing edges as geodesics joins every terminal to \(X\), at total length at most \(m_X(V)\); in particular \(m_X(V)\ge d(v,X)\).

The following are imports, not conclusions about the actual Yang–Mills response.

**D — specified response data.** Use O1D ([o1-decoupled.md](o1-decoupled.md)) Definition D, the field-read part of HW ([h-walk.md](h-walk.md)) Theorem W as repaired in [h-walk-fix.md](h-walk-fix.md), and the endpoint/read hypotheses of [loc-3.md](loc-3.md) Lemma C. Each separately assigned operator \(H,H_1,\mathfrak G\), and the walk part of \(M_s\), has an absolutely convergent expansion on \(|s_\Delta|<e^{\bar\kappa}\). A term carries every parameter cube meeting its full connected enlarged hull
\[
 \bigcup_{\kappa\in\omega}\kappa^\sharp,\qquad
 \kappa^\sharp\text{ has side }8L^2M_1\xi_\kappa.
 \tag{3}
\]
Its output lies in \(\kappa_0^{(2)}\), its input within layer-metric distance \(r_g\) of \(\kappa_n^{(1/4)}\), and its pair reads lie in that enlarged hull. Branches carry their own enlarged cells. In particular \(\mathfrak G\) uses [pw-bridge.md](pw-bridge.md) (7.4): compose its undecoupled coefficients first, then tag each cube of that coefficient's full read union once. Subsequent products of already assigned maps in (5), (7) retain their actual monomials, including repeated powers. All local maps, their coefficient reads and transpose stencils have reach at most \(r_g\le8L+1\); choose
\[
 L\ge27,\quad R_1\ge8L^3,\quad
 M_1\ge\max\{240,16Lr_g\},\quad \rho_{\mathbf B}=3LM_1\ge80r_g.
 \tag{4}
\]
Here \(d_{\mathbf B}\) is the layer metric, distinct from \(d\). The separated-layer geometry gives local scale at most \(L\xi_\kappa\) throughout \(\kappa^\sharp\). The parameter grid in (3) is required to be the fine switch grid used below.

Use exactly NR9 ([nl-r9.md](nl-r9.md)) (4.3)–(4.4), including
\[
\begin{split}
 &M_s=M_s^{\rm walk}-a_0I,\quad d_s(\alpha)=\mathcal C(h),\quad h=\alpha-H\mathcal C(h),\\
 &p_s=H^{\mathsf T}\mathbf J,\quad d_{3,s}=d_s-\mathcal C_2,\quad Z_s=I-Hd_s',\\
 &W_s^{\rm red}(\alpha)=-d_{3,s}'{}^{\mathsf T}p_s-K^{\mathsf T}M_sd_s
       -d_s'{}^{\mathsf T}M_sK\alpha+d_s'{}^{\mathsf T}M_sd_s
       +Z_s^{\mathsf T}N_0(h).
\end{split} \tag{5}
\]
The auxiliary field is denoted \(\alpha\) to distinguish it from the decay rate \(a\) below; derivatives in (5) are evaluated at \(\alpha\). The diagonal \(-a_0I\) is **unparameterized**. The equations are
\[
 \alpha=H_1S-\mathfrak G W_s^{\rm red}(\alpha),\qquad h=\alpha-H\mathcal C(h).
 \tag{6}
\]
**UNQ** is the existence, uniqueness and holomorphy implication of DF ([dec-field.md](dec-field.md)) Proposition 5.1, with its [PW], [NL] hypotheses for these very maps. With \(B=C_{\rm op}e^{16\bar\kappa}\ge1\), take \(b_*<c_*B^{-4}\), \(c_*\le\min\{r_{\rm an}/4,(16C_W)^{-1},(16C_C)^{-1}\}\), in that proposition's notation. On \(\|S\|<b_*\), solutions are unique in \(\|\alpha\|_X\le R_*=2Bb_*\), \(\|h\|_X\le2R_*\). The norm is the original weighted supremum of field values and elementary covariant-difference stencils, whose connection coefficients have local reads, with fixed geometry and weights. Require also the absolute Neumann majorants in NR9 §5 and D3L ([d3-local.md](d3-local.md)) §3 on this common ball, in particular \(B C_{\rm der}(2R_*)\le1/2\). The analytic radius \(r_{\rm an}\) is not the geometric reach \(r_g\). When combining D with R below, their response and row normalizations must agree and \(s_D\le b_*\).

For the current specify a local anchor \(J_*(P)\) and put
\[
\begin{split}
 F_*(h)&=F'_U(h)-F'_U(0)+J_*,\\
 \lambda&=(I+H^{\mathsf T}\mathcal C'_h{}^{\mathsf T})^{-1}H^{\mathsf T}F_*(h),
 \quad \lambda_0=H^{\mathsf T}J_*,\\
 j&=R_hK_h^{\mathsf T}\lambda-K_0^{\mathsf T}\lambda_0 .
\end{split} \tag{7}
\]
Here \(R_h\) acts bond by bond, \(K_h\) is the local row derivative and \(\mathcal C'_h=K_h-K_0\). We use \(J_*=\mathbf J\) for the ST1 (43) specification. The choice \(J_*=F'_U(0)\) gives the different continuation in D3L (3); the locality proof covers it too.

**Outstanding — actual specification.** D and UNQ must hold for the maps consumed on every required move. [RED] identifies (5) with that nonlinear map; it does not identify the two current continuations in (7). They agree on \(\mathbf J=F'_U(0)\), but their difference off that locus is
\[
 [R_hK_h^{\mathsf T}(I+H^{\mathsf T}\mathcal C'_h{}^{\mathsf T})^{-1}
       -K_0^{\mathsf T}]H^{\mathsf T}(F'_U(0)-\mathbf J).
 \tag{8}
\]
There is no supplied reason for (8) to vanish. Nor does the floor \(M\ge C_{\rm dec}\bar\kappa\) by itself identify O1D's parameter partition with the fine grid. Both identifications must be supplied. The field-read gate preserved locality at fixed regions; it did not prove locality of changing region traces.

**R, A and TD (5) — analytic response and admission.** Import TD ([td.md](td.md)) R for the pair-valued response \(\mathfrak h=(h,j)\), independently of whether D has been established. It is jointly holomorphic on the switch polydisc and the full product source ball \(\|S\|_{\rm src}<s_D=\epsilon_De^{-c_D\bar\kappa}\), is zero at \(S=0\), and satisfies
\[
 n_b(\mathfrak h)\le C_DE_{\bar\kappa}\|S\|_{\rm src}
          e^{-\mu_Rd_+(b,\operatorname{supp}S)}.
 \tag{9}
\]
Here \(n_b(h,j)=\max\{l|h|,l^2|\nabla^Uh|,l^3|j|\}\). Its complete stencil lies in a connected set \(B_b\) of at most \(16\) fine cubes containing \(\Delta_b\). At fixed \(P\), a wall-component reads only its switches and source rows; a stencil with \(B_b\subset\operatorname{supp}s\) reads only components meeting \(B_b\). Source norms are maxima of assigned row norms.

The completed source is \(S(v_0+u(s\odot\zeta))\), with cube-local linear \(u\), \(\|u(\zeta)\|_\infty\le c_Tg\|\zeta\|_\infty\). It is holomorphic in the chart \(\|v\|_\infty<c_{\rm ch}L^{-9}\), has Lipschitz constant \(C_A\), and \(\|S(v_0)\|\le C_A\delta_{\rm src}<s_D/2\); \(\|v_0\|_\infty<c_{\rm ch}L^{-9}/2\). Its rows read one neighbour layer, with the imported floor \(M\ge R_\sigma+3\), and all sources are supported in \(\mathcal S\). **S-loc** additionally requires this locality for the external pair, stored data and pins; datum-locality alone does not assert it. Actual-response identification, reality, pair ties and regional restriction remain R's separate clauses.

Retain TD2's window conversion and power floors: \(\ell=\log\theta_{i-1}\), \(g=e^{-\ell/2}\), \(R_{\rm run}=\ell^q\), \(\mathfrak b=C_{\rm win}A_1\ell^{p_0}\), \(\delta_{\rm src}=A_1g\ell^{p_0}\), \(C_{\rm win}\ge1\), \(p_0>0\), \(q>p_0+2r_{\rm RUN}\), \(r_{\rm RUN}\ge2\). Fixed window factors are absorbed in source constants as in TD2. Define
\[
\begin{gathered}
 D=e^{\bar\kappa}-1,\quad Q=6400/D=e^{-2a}\le\tfrac12,\quad
 \delta=(8e)^{-1},\quad\delta_J=\delta/3,\\
 \varrho=\frac{\min\{s_D/2,C_Ac_{\rm ch}L^{-9}/2\}}
                   {c_TC_Ae^{\bar\kappa}g},\quad
 A_R=4C_DE_{\bar\kappa}s_DD^{15},\\
 A_V=C_DE_{\bar\kappa}C_A(3\delta_{\rm src}+c_Tge^{\bar\kappa}R_{\rm run}),\quad
 K_1=\max\{1,4A_R/A_V\},\\
 \beta_c=2K_1|\zeta|_c/\varrho,\quad
 \vartheta=4K_1\mathfrak b/(\delta\varrho),\quad
 \eta_1=C_DE_{\bar\kappa}C_A\delta_{\rm src}/A_V,\qquad
 8\eta_1D^{15}\le1\quad\text{(TJ)}.
\end{gathered} \tag{10}
\]
The letter \(q\) in \(R_{\rm run}\) is a fixed power; the switch weight below is \(q_{\rm sw}\).

For each exempt term \(f\), A specifies nonempty complete reads \(\mathcal B_f\), \(X(f)=\{\Delta_b:b\in\mathcal B_f\}\), and \(X_f\supset\bigcup_{b\in\mathcal B_f}B_b\). The function \(\Phi_f(P,v)\), including its restriction and pins, reads \(P\) in \(X_f\) and is holomorphic on \(n_b(v)<A_b=A_Ve^{-\mu_Rd_+(b,\mathcal S)}\). Its bound is \(|\Phi_f|\le b_f\), or oscillation at most \(\omega_f\), or \(\operatorname{Re}\Phi_f\le A_f\). In the last case import TD (5),
\[
 A_f-\operatorname{Re}\Phi_f(P,\mathfrak h_0(P))\le B_f,\qquad
 \mathfrak h_0(P)=\mathfrak h(\mathbf1;P,S(v_0)).
 \tag{11}
\]
Set \(\widetilde\omega_f=2b_f,\omega_f,2B_f\), respectively. All bounds are uniform on the complex fibre. **Outstanding:** the actual complex island deficit (11), arbitrary-shift admission with complete pins, and the strengthened response R are not consequences of frozen P82. P82 concerns real curved references. ST1's response remains imported, and TP1 does not make its running minimum monotone.

**X, G, X°, G-ord, RUN — filing geometry.** Import TD/TD2's following data. Put \(d_o=d_f^{\rm old}\). Uniformly in \(P\),
\[
 \widetilde\omega_f\le\widehat\omega_fe^{-\kappa d_o},\qquad
 \sup_c\sum_{f:X(f)\ni c}\widehat\omega_fe^{-\kappa d_o/2}
       \le N_{\rm ex}\le C_{\rm ex}(M)\ell^{t_{\rm ex}}. \tag{12}
\]
Hubs \(\widetilde H=N_2(H)\) are separated by \(s_0=\check R_i-4\), lie in nonwrapping boxes of side \(D_H=C_{\rm isl}L\check R_i+6\), and gas cubes are at distance at least \(G_0=10L\check R_i-2\) from hubs and the live set. G-ord fixes integers \(C_{\rm isl}\ge1,c=c_{\rm col}\ge0\) and \(C_{\rm pr}\ge1\) before \(L,\kappa\), uniformly in subsequent \(L,M,\bar\kappa\). Each \(f\) has an ordinary fine tree \(T_f\) with at most \(C_{\rm pr}(1+d_o)\) edges. Every cube of \(X_f\) lies within \(c\) of \(T_f\), or in \(\widetilde H^+=N_c(\widetilde H)\) for a hub met by \(T_f\). Also \(X_f\) meets a hub or the live set. This is X°; the ordinary tree is essential. TD's contracted premise and its other geometric ceilings remain binding for that route; the present bound does not use its contracted-length conclusions.

Let \(\eta_H=1+C_{\rm isl}/10\). Under \(10L\check R_i\ge6+2c+\eta_H(2+c)\), TD2 Lemmas 1–2 give
\[
\begin{split}
 \operatorname{St}(W)&\le(1+\eta_H)m_{X(f)}(W)
                         +C_{\rm pr}(1+d_o)+c|W|,\\
 m_{X(f)}(W)+C_{\rm pr}d_o&\ge G_0-C_{\rm pr}-2c
 \quad(\varnothing\ne W\text{ gas}).
\end{split} \tag{13}
\]
RUN is \(\check R_i\ge(\ell-1)^{r_{\rm RUN}}\), \(r_{\rm RUN}\ge2\), uniformly over histories with \(\ell\ge\log\gamma^{-2}\). It implies \(\vartheta\to0\) with all preceding constants fixed, as in TD2.

**Order.** Retain every applicable IN1/ST1/CI floor; the additions here follow this order.

1. Fix the powers, window conversion \(C_{\rm win}\), G-ord constants and constants used to choose \(L\), uniformly in subsequent \(L\). Choose \(L\) with the rate-window floors below, then the remaining early geometry \(r_g,R_1,M_1,c_G,c_{\rm inc}\), margins and base response/chart/operator constants, satisfying (4) and the existing floors. All precede \(\kappa\) and are independent of \(M,\bar\kappa\). The value \(C_4\) in (15) is determined by these early data. Fix once
   \[
    0<\eta\le\eta_{\max}:=[16(C_{\rm isl}+1)L]^{-1}.
    \tag{14}
   \]
   This is an early geometric constant, not \(4\lambda_P/(a/2-6)\).
2. Choose \(\kappa,\lambda_V\) in the full amended IN1 window, with \(\lambda_T=\lambda_V+1\) and \(\lambda_TC_{\rm pr}\le\kappa/4\). Concretely, TD2 (13) uses \(A_o=(1+4\beta_s)C_h^{\rm UM}c_\ell\), \(B_o=\lambda_0+\sigma_0+C_h^{\rm UM}(3+c_\ell g_*)/L\), \(u=\min\{(2C_h^{\rm WF})^{-1},(4C_{\rm pr})^{-1}\}\), an early \(L\) with \(A_o/L<u/2\), and \(\kappa\ge2(B_o+\varepsilon_{\rm rate}+1)/(u-A_o/L)\), \(\lambda_V=A_o\kappa/L+B_o\). If also keeping the natural route, use its common-window slope/intercept in both choices. Define
   \[
    C_4=C_{\rm pr}+(2c+3)^4(C_{\rm pr}+1),\qquad
    \lambda_P=\min\{\kappa/(16C_4),[4(2c_G+1)^4]^{-1}\}>0 .
    \tag{15}
   \]
3. Choose \(\bar\kappa\ge\lambda_V+2\) above the imported response/bracket floors and the filing floors (30) below. This fixes \(D,a,s_D,A_R\) and the prescribed \(E_{\bar\kappa}\). Choose the post-\(\bar\kappa\) preparation constants, then \(M\), a power of \(L\), satisfying all imported floors and O1D's \(\ell_{\mathsf P}\ge\max\{8r_1+1,256\bar\kappa/\tau_L\}\). This last floor gives convergence, not a larger read collar.
4. Choose the late radii, \(A_1\), prefactors \(C_{\rm ex}(M)\), and Gaussian budgets in IN1's internal order. Finally decrease \(\gamma\) for (TJ), \(\vartheta<2/3\), (13), the scalar ceilings (25), (30), and all imported admission/source/activity ceilings. Torus room in (25) remains a separate geometry premise. The running quantities in (10) are not early constants. No upper bound on \(M\) is introduced.

**Main statement.** Under D and UNQ, the specified response (6)–(7) has exact two-pair component locality with collar \(0\); with S-loc its completed-source collar is \(1\) (Theorem 1). Under R, A, (11), complete stencils, (TJ) and \(\vartheta<2/3\), the pieces (19) satisfy \((\mathrm{JC}_\tau)\) for \(5\le\tau\le2a-24\) (Theorem 2). Combining these hypotheses, including D/R identification and S-loc, with X, G, X°, G-ord, RUN and (25), (30) gives the summable pair-labelled bound (31), with intrinsic relative length and the collared excused family (24) (Theorem 3). This is a conditional producer bound. Identifying that family with IN1's inductive class and forming the actual CI activities remain separate obligations.

## 2. Depth and the nonlinear equations

A point is *deep in \(W\)* if every parameter cube meeting \(B_{\mathbf B}(x,\rho_{\mathbf B})\) belongs to the wall-component \(W\). Denote this set by \(\operatorname{Dp}(W)\). A map is *split* if its nonzero kernel entries have both endpoints deep in one component and read only that component's pair and switches.

**Lemma 2.1 (depth and reads).** Under D, each assigned walk sum and its transpose is split. Local maps between split factors cannot move their dependence to a different component if their consecutive reach is less than \(\rho_{\mathbf B}\).

*Proof.* A surviving term has nonzero switches on every cube meeting its connected enlarged hull. With the convention that every cube meeting a boundary point is tagged, these cubes form one face-component (O1D Lemma WC). Its pair reads therefore lie there.

The output margin inside \(\kappa^\sharp\) is \((4L^2-5/2)M_1\xi_\kappa\). Before its first exit, a layer-metric path of length \(\rho_{\mathbf B}\) travels physical distance at most \(3L^2M_1\xi_\kappa\), strictly less than that margin. Thus it cannot exit. The input margin is controlled by
\[
 L(\rho_{\mathbf B}+r_g)
       =3L^2M_1+Lr_g<(4L^2-3/4)M_1.
 \tag{16}
\]
This also is a first-exit argument; it does not assume the scale bound after leaving the cell. Both endpoints are deep.

For the zero-length multiplier in a tree walk, the field-read box \(\lambda^{(4)}\) is within \(21M_1\xi_\lambda/4\) of its row \(x\), while \(x\in\kappa^{(7/2)}\). The repaired adjacent-layer geometry gives \(\xi_\lambda\le L\xi_\kappa\). Allowing two further local stencils costs at most \(2r_gL\xi_\kappa\le M_1\xi_\kappa/8\). The total half-side is bounded by
\[
 (33/8+21L/4)M_1\xi_\kappa<4L^2M_1\xi_\kappa .
 \tag{17}
\]
Thus those reads fit the same tag; branch reads fit their own tags. This checks the margin for the imported endpoint structure, not the existence of the expansions.

Transposition exchanges endpoints without changing reads. If two deep endpoints can be joined through local stencils of total reach less than \(\rho_{\mathbf B}\), they belong to the same component: every cube at that distance from the first endpoint is in its component. Absolute convergence passes these termwise properties to the sums. ∎

**Lemma 2.2 (reach of the specified equations).** On solutions of (6), \(\alpha,h\) are supported on \(\bigcup_W\operatorname{Dp}(W)\). For any such supported candidate satisfying the inner equation, evaluating the right sides on deep points requires only the candidate, pair, switches and source in that component. Between consecutive split factors the largest local reach is \(2r_g\). Formula (7) has support within \(r_g\) of the deep sets and the same component reads.

*Proof.* The first equation has split outer factors \(H_1,\mathfrak G\); the second gives \(h=\alpha-H\mathcal C(h)\). This proves the support assertion. Differentiating its inner equation gives, with \(A=\mathcal C'_h\),
\[
 d_s'{}^{\mathsf T}=A^{\mathsf T}(I+H^{\mathsf T}A^{\mathsf T})^{-1}
     =\sum_{n\ge0}A^{\mathsf T}(-H^{\mathsf T}A^{\mathsf T})^n .
 \tag{18}
\]
The imported absolute majorant justifies this series. Each \(H^{\mathsf T}\) resets the endpoint to a deep point. In (5), the only two consecutive local reaches arise from the diagonal part of \(K^{\mathsf T}M_s\mathcal C(h)\), \(d_s'{}^{\mathsf T}M_sK\alpha\), or \(d_s'{}^{\mathsf T}M_s\mathcal C(h)\). They cost at most \(2r_g\); all other local strings cost at most this. The subtraction \(\mathcal C_2'\), the local force \(N_0\) and their coefficients obey the same reach assumption. Lemma 2.1 applies after each split factor. In particular it would be incorrect to treat all of \(M_s\) as split.

The series for \(\lambda\) starts with a leftmost \(H^{\mathsf T}\) in every term, so \(\lambda,\lambda_0\) are deep-supported. The force and all intermediate local derivatives stay within the same component. The final \(K_h^{\mathsf T}\) adds reach \(r_g\); \(R_h\) is bondwise. The budget (4) keeps this readout strictly inside that component, including all coefficients. No monomial is replaced by the product over its union of cubes. ∎

## 3. Two-pair locality

**Theorem 1 (DR-locP).** Assume D and UNQ. Let \(W\) be a face-component of \(\operatorname{supp}s\), \(|s_\Delta|<e^{\bar\kappa}\). For two admitted pairs agreeing on \(W\), and equal source rows there, (6)–(7) give identical \((h,j)\) at every coordinate based in \(W\). The result depends only on \(s|_W,P|_W,S|_W\), also when exterior switches change while \(W\) remains a component. The response vanishes on zero-switch cubes and on a component with zero source. The induced function is holomorphic on the image of coordinate restriction. With S-loc the completed response reads \(P\) only in \(N_1(W)\).

*Proof.* Let \((\alpha,h)\), \((\widetilde\alpha,\widetilde h)\) be the two solutions. In the equations for \(\widetilde P\), splice in \(\alpha,h\) on \(\operatorname{Dp}(W)\) and retain the tilded solution elsewhere. A value or elementary difference stencil that sees a nonzero deep value sees nonzero values from at most one component: its diameter is less than \(\rho_{\mathbf B}\). On that stencil the splice is exactly one original field. If it uses the untilded field, its norm coefficients read inside \(W\) and agree with the tilded coefficients; otherwise the entire stencil is the tilded one, or is zero. Hence the splice remains in the **original** \(R_*,2R_*\) balls. These common balls use the upper bound \(b_*\) in DF's contractions, not the possibly different individual source norms. A pillar supremum is a supremum of elementary stencils; the whole pillar is not asserted to have radius one.

First verify the inner equation for the splice: \(H\) is split and \(\mathcal C\) has reach \(r_g\), so it agrees with the corresponding original equation on each component and is zero off the deep sets. Its small-ball uniqueness identifies \(\mathcal C(h)\) with the \(d_s(\alpha)\) used in (5). Lemma 2.2 then verifies the first equation component by component, with both sides again zero off the deep sets. UNQ identifies this solution with the tilded solution, and Lemma 2.2 identifies the current. The same splice argument with distinct exterior switch/source values proves their independence. A zero-source component can instead be spliced with zero: (5) vanishes at zero, and (7) has \(\lambda=\lambda_0\), \(j=0\). Support and (4) give zero on zero-switch cubes.

For holomorphy, write coordinates as \((Q,P_{\rm ext})\). The projection of the global open domain is open. Near a point with lift \(P_0\), fixing \(P_{\rm ext}=P_{0,\rm ext}\) gives a holomorphic local section; the just-proved independence makes its value independent of the lift. These sections agree on overlaps. Coordinate restrictions compose, which gives consistency on these image domains. If the domains and equations are conjugation invariant, reality follows by comparing a lift and its conjugate when \(Q,s,S|_W\) are real; a real exterior lift need not exist. Finally source completion adds exactly its one neighbour layer, including stored data and pins by S-loc. ∎

**Outstanding — full local domains.** Image-domain descent does not establish a regional solution on every declared \(\mathcal O_\sigma(Y;U)\), nor consistency between different regional constructions. For that extension require the same uniformly contracting holomorphic local solver, common balls and admission on the full local domain, and identify its coefficients with the restriction. Uniqueness alone does not imply holomorphic dependence or existence. Covariance, ties between different real-reference representations and changing-region trace locality are also not supplied here.

**Proposition 3.2 (bounds and fixed-pair splitting are insufficient).** Joint holomorphy, (9), reality, zero-source vanishing and the switch/source component clauses at fixed \(P\) do not imply pair-locality with any uniform fixed collar. This is not a counterexample to the actual-equation, physical-identification or regional-consistency parts of R.

*Proof.* On arbitrarily large finite four-dimensional cube tori, take \(|p_c|<1/8\), \(T_{cc'}=t(1+p_c)(1+p_{c'})\) for face neighbours and zero otherwise. Each absolute row sum is less than \(11t\). For \(11t\le1/2\),
\[
 B=(I-T)^{-1}=\sum_{n\ge0}T^n,\qquad
 |B_{cc'}|\le2(11t)^{d_1(c,c')},
\]
where \(d_1\) is face distance. Fix a face geodesic \(\pi(c,c')\), including both endpoints, with \(\pi(c,c)=\{c\}\). Set
\[
 B^s_{cc'}=B_{cc'}\prod_{v\in\pi(c,c')}s_v,\qquad
 h=0,\quad j=\epsilon B^sS .
\]
Use single-cube current coordinates at scale one and \(d_+=d\), so \(n_b(0,j)=|j_b|\). Choose \(11te^{\bar\kappa}=e^{-\mu-8}\). Since \(d_1\ge d\), (2) gives
\[
 |j_c|\le4\epsilon e^{\bar\kappa}\|S\|
                    e^{-\mu d(c,\operatorname{supp}S)} .
\]
Taking \(\epsilon\) small supplies any prescribed positive prefactor. Holomorphy, reality and zero-source vanishing follow from the convergent series. Every surviving path lies in one face-component, proving its switch/source clauses at fixed pair.

At \(s=\mathbf1_{\{c_0\}}\), take \(S_{c_0}=s_*\in(0,s_D)\) and all other source rows zero. Then \(j_{c_0}=\epsilon s_* B_{c_0c_0}\). At \(P=0\), all entries of \(B\) are positive and \(\partial_{p_z}T\) is nonzero and nonnegative. Therefore \(\partial_{p_z}B_{c_0c_0}=(B\,\partial_{p_z}T\,B)_{c_0c_0}>0\) for every \(z\). A small real change arbitrarily far from \(c_0\) changes this admitted response. Path-tagging an already global inverse therefore does not give the full-hull locality of D. ∎

## 4. Joint composition

For a finite cube set \(W\), let \(D_WF(\zeta)=\sum_{B\subset W}(-1)^{|W\setminus B|}F(\zeta\mathbf1_B)\). Fix \(N\supset X_f\), \(V\subset\mathcal P\setminus N\), and nonempty gas \(W\); neither \(X_f\) nor \(N\) must be connected. Define
\[
\begin{split}
 F_f(s,\zeta)&=\Phi_f(P,\mathfrak h(s;P,S(v_0+u(s\odot\zeta)))),\\
 f_{W,V}&=\sum_{A\subset V}(-1)^{|V\setminus A|}
                       D_W F_f(\mathbf1_{N\cup A},\zeta).
\end{split} \tag{19}
\]
Finite Boolean inversion gives \(\sum_{V\subset\mathcal P\setminus N}f_{W,V}=f_W\), where \(f_W=D_WF_f(\mathbf1,\zeta)\): the coefficient of a proper subset \(A\) in the sum is \((1-1)^{|\mathcal P\setminus(N\cup A)|}\).

**Lemma 4.1 (joint response coefficients).** For \(B\subset W,A\subset V\), let \(g_{B,A}\) be the joint Boolean coefficient, in fluctuation masks \(t\) and switch masks \(\sigma\), of
\[
 g(t,\sigma)=\mathfrak h\bigl(s(\sigma);P,
              S(v_0+u(s(\sigma)\odot\zeta\mathbf1_t))\bigr),
 \qquad s(\sigma)=\mathbf1_N+\mathbf1_\sigma.
\]
For \(b\in\mathcal B_f\), \(n_b(g_{B,A})=0\) unless some corner-connected \(Y\) satisfies
\(B\cup A\cup B_b\subset Y\subset N\cup A\). Moreover, for \(|\zeta|_c<\varrho\),
\[
\begin{array}{ll}
 B\ne\varnothing:&
 n_b(g_{B,A})\le A_Re^{-\mu_Rd_+(b,\mathcal S)}
       Q^{\operatorname{St}(B\cup A\cup\{\Delta_b\})}
       \prod_{c\in B}2|\zeta|_c/\varrho,\\
 B=\varnothing\ne A:&
 n_b(g_{\varnothing,A})\le(A_b/4)(8\eta_1D^{15})
                         Q^{\operatorname{St}(A\cup\{\Delta_b\})},\\
 B=A=\varnothing:&
 g_{\varnothing,\varnothing}=\mathfrak h_0^N:=
             \mathfrak h(\mathbf1_N;P,S(v_0)),\quad n_b(\mathfrak h_0^N)\le A_b/3 .
\end{array} \tag{20}
\]

*Proof.* Test the stencil by a linear functional of dual seminorm at most one; taking their supremum recovers \(n_b\). Scale each fluctuation by a complex \(z_c\). Formula (10) keeps the chart and source admitted on \(|s_c|<e^{\bar\kappa}\), \(|z_c\zeta_c|<\varrho\). Expand the scalar response by the fundamental theorem of calculus in every switch except those in \(B_b\), which are held at one:
\[
 \varphi(s;z)=\sum_{Y'\subset\operatorname{supp}s\setminus B_b}
 I_{Y'}(z),\qquad
 I_{Y'}=\int_{[0,1]^{Y'}}\partial_s^{Y'}\varphi(\mathbf1_{B_b}+\tau_{Y'};z)\,d\tau .
\]
The mixed \(A\)-difference selects exactly \(Y'\cap V=A\), with \(Y'\subset(N\setminus B_b)\cup A\), by finite inclusion–exclusion. If \(Y=B_b\cup Y'\) has a corner-component disjoint from \(B_b\), the response stencil is independent of a switch in that component. Indeed its read face-components meet \(B_b\), and their source rows reach only one corner-neighbour layer. Thus that derivative vanishes. If \(c\in B\setminus Y\), its fluctuation is masked by \(s_c=0\), so the \(B\)-difference vanishes too. This proves the support assertion.

For \(B\ne\varnothing\), subtract \(\varphi(s;0)\). Its difference from \(\varphi(s;z)\) has modulus at most \(2C_DE_{\bar\kappa}s_De^{-\mu_Rd_+}\). Cauchy circles about \(\tau_c\in[0,1]\), of radii tending to \(D\), give \(D^{-|Y'|}\). Repeated Schwarz in \(z_c\), after the \(B\)-difference, gives \(\prod_{c\in B}2|\zeta|_c/\varrho\). For \(B=\varnothing\), use \(|\varphi(s;0)|\le C_DE_{\bar\kappa}C_A\delta_{\rm src}e^{-\mu_Rd_+}\) instead.

A surviving \(Y\) has at least \(\operatorname{St}(B\cup A\cup\{\Delta_b\})+1\) vertices, and \(|Y'|\ge|Y|-16\). The animal count gives, for any such lower bound \(n_0\),
\[
 \sum_YD^{-|Y'|}
 \le\sum_{n\ge n_0}6400^{n-1}D^{16-n}
 \le2D^{15}Q^{n_0-1}.
\]
The constants in (20) now follow from (10). Its last line follows directly from (9) and \(\eta_1\le1/3\). ∎

**Lemma 4.2 (two labels per cube).** Suppose \(\Phi\) is holomorphic on \(h_*+\{v:n_b(v)<A_b/4\}\), with \(|\Phi-\Phi(h_*)|\le\omega\). Let \(\Lambda\) have at most two labels per cube, projection \(\pi\), \(X=\{\Delta_b\}\), and \(a_J\ge12\), \(0<\beta_\lambda<\delta_J\). If
\[
 n_b(g_I)\le(A_b/4)\prod_{\lambda\in I}\beta_\lambda\,
                   e^{-a_J\operatorname{MST}(\pi I\cup\{\Delta_b\})}
 \quad(\varnothing\ne I\subset\Lambda),
\]
then, for \(F(t)=\Phi(h_*+\sum_{I\ne\varnothing}t^Ig_I)\),
\[
 |D_\Lambda F(\mathbf1)|\le
 \omega\prod_{\lambda\in\Lambda}(2\beta_\lambda/\delta_J)
                 e^{-(a_J-6)m_X(\pi\Lambda)}. \tag{21}
\]

*Proof.* Apply Bird's allocation to the labelled complete graph, joining duplicate cube labels at zero cost. Its MST is \(m_X(\pi\Lambda)\), and
\(\sum_{\lambda\in I}l_\lambda\le\operatorname{MST}(\pi I\cup\{\Delta_b\})\).
Take radii \(r_\lambda=(\delta_J/\beta_\lambda)e^{(a_J-6)l_\lambda}>1\).
A shift term on this polydisc is at most
\((A_b/4)\delta_J^{|I|}e^{-6\operatorname{MST}(\pi I\cup\{\Delta_b\})}\).
For \(Z=\pi I\) there are at most \(3^{|Z|}\) choices of \(I\), and \(\delta_J^{|I|}\le\delta_J^{|Z|}\). Equation (2) bounds the sum of all shifts by
\[
 (A_b/4)\,2\sum_{n\ge1}(2e\delta)^n=(A_b/4)\,2/3.
\]
The polydisc is therefore admitted. Its Boolean difference vanishes on each \(t_\lambda=0\) and has modulus at most \(2^{|\Lambda|}\omega\). Repeated Schwarz gives (21). Zero \(\beta_\lambda\) follows by continuity. ∎

**Lemma 4.3 (corner amplitude).** Under (11) and (TJ), for every \(N\supset X_f\),
\[
 A_f-\operatorname{Re}\Phi_f(P,\mathfrak h_0^N)\le3B_f.
 \tag{22}
\]

*Proof.* At zero fluctuation, the expansion in Lemma 4.1 expresses \(\mathfrak h_0-\mathfrak h_0^N\) as the sum of terms whose \(Y'\) leave \(N\). Dropping that restriction in its absolute bound gives
\(n_b(\mathfrak h_0-\mathfrak h_0^N)\le(A_b/4)\epsilon\),
\(\epsilon=8\eta_1D^{15}\le1\), uniformly in \(b\).
For \(\epsilon>0\) put \(v=(\mathfrak h_0^N-\mathfrak h_0)/\epsilon\).
Since \(n_b(\mathfrak h_0)\le A_b/3\), the function
\(\psi(z)=\Phi_f(P,\mathfrak h_0+zv)-\Phi_f(P,\mathfrak h_0)\)
is holomorphic for \(|z|<2\), has \(\psi(0)=0\), and \(\operatorname{Re}\psi\le B_f\). The half-plane Schwarz bound gives
\(|\psi(\epsilon)|\le2B_f\epsilon/(2-\epsilon)\le2B_f\epsilon\).
Adding (11) proves (22); \(\epsilon=0\) is immediate. ∎

**Theorem 2 (\(\mathrm{JC}_\tau\)).** Assume R, A, (11), complete stencils, (TJ), and \(\vartheta<2/3\). For \(5\le\tau\le2a-24\) and \(|\zeta|_c\le\mathfrak b\),
\[
 |f_{W,V}|\le\omega_f^N
       \prod_{c\in W}\frac{2\beta_c}{\delta_J}
       (48e^{1-\tau})^{|V|}
       e^{-(a-6-\tau/2)m_{X(f)}(W\cup V)},\qquad
 \omega_f^N\le3\widetilde\omega_f . \tag{23}
\]
Here \(\omega_f^N=2b_f,\omega_f,6B_f\), respectively. Also \(f_{W,V}=0\) unless \(W\subset N\cup V\) and every \(v\in V\) is joined to some \(B_b\) inside \(N\cup V\). No connectivity of the whole base or union is asserted.

*Proof.* Give \(c\in W\) a fluctuation label of weight \(\beta_c\), and \(v\in V\) a switch label of weight \(e^{-\tau}\); there are at most two labels per cube. Set \(a_J=a-\tau/2\ge12\).
Because \(A\subset V\) misses \(N\ni\Delta_b\), \(|A|\le\operatorname{St}(B\cup A\cup\{\Delta_b\})\). Hence
\[
 Q^{\operatorname{St}}\le e^{-\tau|A|}
             e^{-(2a-\tau)\operatorname{St}}
       \le e^{-\tau|A|}e^{-a_J\operatorname{MST}}.
\]
For \(B\ne\varnothing\), \(4A_R/A_V\le K_1\) and \(K_1\ge1\) turn (20) into the coefficient hypothesis of Lemma 4.2. For \(B=\varnothing\ne A\), (TJ) does so. The multilinear interpolant of the Boolean response equals \(g\) at all corners, so composing it with \(\Phi_f\) gives exactly (19)'s difference.

The base is \(\mathfrak h_0^N\), with seminorm at most \(A_b/3\). A shift of seminorm \(A_b/4\), even doubled radially, stays in A. Two-sided and oscillation bounds give the asserted amplitude; for islands, the half-plane Schwarz bound on the doubled disc and (22) give \(6B_f\). Moreover \(\beta_c\le\delta\vartheta/2<\delta_J\), and \(e^{-\tau}<\delta_J\): \(\tau\ge5\) and \(e^4>24\), directly from its positive series. Lemma 4.2 gives (23). The support assertion follows from Lemma 4.1: an absent fluctuation label is masked, and a switch label unconnected to all read stencils occurs in no nonzero coefficient. ∎

The interval is nonempty only for \(a\ge29/2\). The choice \(\tau=12\) requires \(a\ge18\) and gives rate \(a-12\) with a fixed switch factor. The choice \(\tau=a\) requires \(a\ge24\) and gives rate \(a/2-6\) with switch factor \(48e(6400/D)^{1/2}\). Thus the simultaneous rate and factor in TD2-draft's original (JC) remain unproved. A switched-polydisc island amplitude is unnecessary for (23); the complex deficit (11) is still necessary.

## 5. Collars and filing

For each hub let \(s_H\ge1\) be the number of fine cubes along the longest side of a containing box of \(\widetilde H^+=N_c(\widetilde H)\), with \(s_H\le D_H+2c\). Using the early \(\eta\) from (14), define
\[
 \rho_H=\lceil\eta s_H\rceil,\quad
 \widehat H=N_{\rho_H+2}(\widetilde H^+),\quad
 F_H=N_1(\widehat H)=N_{\rho_H+3}(\widetilde H^+),\quad
 \mathsf H=\{F_H\},
 \qquad
 N_f=X_f\cup\bigcup_{\widetilde H:T_f\cap\widetilde H\ne\varnothing}\widehat H .
 \tag{24}
\]
This is a proposed excused family. It is not SA's existing family of uncollared standing-island hulls.

Require
\[
 \check R_i\ge128(1+c),\qquad D_H\ge2c,
 \quad\text{room on the torus for the enlarged containing boxes.} \tag{25}
\]
The last condition means that each chosen box enlarged by \(\rho_H+3\) has a nonwrapping lift. A sufficient condition is a torus period in each fine-cube direction greater than \((1+2\eta)(D_H+2c)+8\). A nonwrapping original box alone does not imply this, and RUN does not supply it. Put \(b_H=c+\rho_H+3\). Equations (14), (25) give
\(b_H\le\check R_i/16+2c+5\), hence \(2b_H\le s_0/2\).
Consequently distinct \(F_H\)'s are separated by at least \(s_0/2\), gas cubes are at distance at least \(G_0/2\), and each \(F_H\) lies in a nonwrapping box of side
\((1+2\eta)s_H+8\le2D_H\).
Also \(G_0-c\ge\rho_H+3\). The gap bounds follow by subtracting neighbourhood radii; the box bound uses \(\eta\le1/32\) and \(D_H\ge4c+16\), consequences of the early choices and (25). No shape assumption on the hub is used.

For a finite nonempty label \(Z\), define the **intrinsic** relative length \(\ell^{\rm rel}_{\mathsf H}(Z)\) by minimizing the edge count over trees **contained in \(Z\)** and subfamilies \(\mathsf F\subset\mathsf H\) whose whole members lie in \(Z\). The tree must meet every cube of \(Z\setminus\bigcup\mathsf F\) and each member of \(\mathsf F\). Crossings of members are charged. If no such tree exists the length is infinite; set the empty label's length to zero. This uses the contained-tree convention confirmed by CA-II/III. The comparison of fine-graph units with the final SA scale remains a separate filing input.

**Lemma 5.1 (read-rooted forest sum).** For nonempty \(R\), finite allowed set \(\mathcal V\), \(s\ge6\) and \(0<q_{\rm sw}\le1/(4e)\), put \(\Xi_R=\sum_{v\in\mathcal V}e^{-sd(v,R)}\). Then
\[
 \sum_{V\subset\mathcal V}q_{\rm sw}^{|V|}e^{-sm_R(V)}
       \le \exp(2q_{\rm sw}\Xi_R). \tag{26}
\]

*Proof.* The exponential of minus the minimum tree weight is at most the sum of the corresponding products over all trees rooted at \(*\). Removing \(*\) gives a rooted forest on \(V\), whose roots pay \(e^{-sd(v,R)}\). Write a set of \(n\) distinct vertices as \(n!\) orderings and then drop distinctness. For a fixed labelled forest, sum nonroot positions leaf first; each costs at most \(2\) by (2), while each root costs \(\Xi_R\). A component of size \(m\) has \(m^{m-1}\) rooted labelled trees. Partitioning the labels into components, and summing their independent weights, therefore gives
\[
 \sum_Vq_{\rm sw}^{|V|}e^{-sm_R(V)}
 \le \exp\!\left(\sum_{m\ge1}\frac{q_{\rm sw}^m}{m!}
                          m^{m-1}\Xi_R\,2^{m-1}\right).
\]
This exponential formula also follows directly by expanding the exponential and dividing by the permutations of the components. Since
\(\log(m!)\ge\int_1^m\log x\,dx=m\log m-m+1\),
\(m^{m-1}/m!\le e^{m-1}\). The exponent is at most
\(q_{\rm sw}\Xi_R\sum_{m\ge1}(2eq_{\rm sw})^{m-1}\le2q_{\rm sw}\Xi_R\). ∎

Thus each attached cluster pays its distance from the **reads** once, at its root; its other vertices pay their edges and \(q_{\rm sw}\). With the collar itself collapsed to the root, \(N\) cubes one step outside it instead give \(\Xi\ge Ne^{-s}\), not \(N\). This still grows without bound and does not repair TD2 (26). The read-rooted estimate does retain the collar-width decay.

**Lemma 5.2 (contained filing tree).** Assume X°, G and (25). For \(W\ne\varnothing\) gas, \(V\subset\mathcal P\setminus N_f\), \(W\subset N_f\cup V\), put \(m=m_{X(f)}(W\cup V)\). There is a fixed choice of a connected graph \(U_{f,W,V}\) such that, with
\[
 Y_{f,V}=N_1(N_f\cup V),\qquad
 Z_{f,W,V}=Y_{f,V}\cup\operatorname{Vert}(U_{f,W,V}),
\]
one has
\[
 \ell^{\rm rel}_{\mathsf H}(Z_{f,W,V})
 \le C_4(1+d_o)+(81+c+\eta^{-1})m+c|W|. \tag{27}
\]
Under Theorem 1, S-loc and A, \(f_{W,V}\) is holomorphic and a function of \(P|_{Y_{f,V}}\), hence of \(P|_{Z_{f,W,V}}\), on image domains.

*Proof.* Start with \(T_f\) and a spanning tree of \(N_{c+1}(x)\) at every vertex \(x\in T_f\). The cost is at most \(C_4(1+d_o)\). These trees meet every cube of \(N_1(X_f)\) outside the members \(F_H\) for hubs met by \(T_f\); those whole members lie in \(Y_{f,V}\), and \(T_f\) meets each.

Realize the root MST on \(W\cup V\) as paths to root points in \(X(f)\), of total length at most \(m\). Connect each root point to \(T_f\). A point within \(c\) costs at most \(c\). Otherwise X° puts it in \(\widetilde H^+\) for a hub met by \(T_f\); a connector inside its containing box costs at most \(s_H\). Its root child \(v\) has edge cost at least \(\rho_H+3\ge\eta s_H\): for \(v\in V\), it is outside \(\widehat H\); for \(v\in W\), use \(G_0-c\ge\rho_H+3\). All such connectors together cost at most \(m/\eta\).

Add the \(80\)-edge neighbour star at each \(v\in V\). Every \(v\notin X(f)\) has positive integer parent cost, so \(|V|\le m\). The first kind of connector costs at most \(c|W\cup V|\le c|W|+cm\). The resulting connected graph \(U\) has the edge bound (27) and meets all unexcused cubes of \(Y_{f,V}\). Its own added vertices are already met. A spanning tree of \(U\), now contained in \(Z_{f,W,V}\), is admissible for the intrinsic length. Fix choices by a total order; covariance of those choices is not claimed.

At each corner in (19), Theorem 1 and S-loc give pair reads in \(N_1(N_f\cup A)\), while A reads \(X_f\). Finite differences preserve this locality and holomorphy. Adding unused coordinates to a carrier preserves both. ∎

The enlargement from \(Y\) to \(Z\) is necessary for this argument: the draft's connector tree need not lie in \(Y\), which may be disconnected. An ambient-tree bound is not a bound for the intrinsic length.

**Lemma 5.3 (collar sum without a box-shaped hub).** Put
\[
 \Psi_\eta=\sup_{x\ge1}x^4e^{-6\eta x}
       \le\left(\frac{2}{3e\eta}\right)^4 .
 \tag{28}
\]
For \(X=X(f)\),
\[
 \Xi_X:=\sum_{v\notin N_f}e^{-12d(v,X)}
 \le2(C_{\rm pr}+1)(1+d_o)\big[(2c+1)^4+\Psi_\eta\big].
 \tag{29}
\]

*Proof.* The reads within \(c\) of \(T_f\) number at most
\((2c+1)^4(C_{\rm pr}+1)(1+d_o)\). Summing the distance kernel from each costs at most \(2\) by (2). For one remaining collared hub, every allowed \(v\) has \(d(v,\widetilde H^+)\ge\rho_H+3\). Thus
\[
 \sum_{v\notin N_f}e^{-12d(v,\widetilde H^+)}
 \le e^{-6(\rho_H+3)}\sum_v e^{-6d(v,\widetilde H^+)}
 \le2|\widetilde H^+|e^{-6(\rho_H+3)}
 \le2s_H^4e^{-6\eta s_H}\le2\Psi_\eta.
\]
There are at most \((C_{\rm pr}+1)(1+d_o)\) hubs met by \(T_f\), since they are disjoint and each contains a vertex of that tree. This proves (29). Maximizing \(x^4e^{-6\eta x}\) over \(x>0\) gives (28). A shell outside a hub cannot be replaced by a shell outside its containing box; this proof makes no such replacement. ∎

**Theorem 3 (filing bound).** Assume all hypotheses used in Theorems 1–2, S-loc, X, G, X°, G-ord, RUN, and (25). Use the early \(\eta\), (15), and set
\[
 \mathfrak r=a/2-6,\quad q_{\rm sw}=48e^{1-a},\quad
 \vartheta_P=6\vartheta e^{(\lambda_P+\lambda_T)c+1},\quad
 \nu=\min\{\kappa/(8C_{\rm pr}),3\}.
\]
Require
\[
\begin{gathered}
 \lambda_PC_4\le\kappa/16,\qquad\lambda_TC_{\rm pr}\le\kappa/4,\\
 \mathfrak r\ge96,\quad \lambda_P/\eta\le\mathfrak r/4,\quad
 \mathfrak r/2\ge\lambda_P(81+c)+2\lambda_T(1+\eta_H),\\
 q_{\rm sw}\le1/16,\qquad
 4q_{\rm sw}(C_{\rm pr}+1)[(2c+1)^4+\Psi_\eta]\le\kappa/16,\qquad
 \vartheta_P<1 .
\end{gathered} \tag{30}
\]
Then, for every nonempty gas set \(W\), uniformly on the admitted complex pair domain and \(|\zeta|_c\le\mathfrak b\),
\[
 \boxed{\displaystyle
 \sum_f\sum_{V\subset\mathcal P\setminus N_f}
       \sup|f_{W,V}|\,e^{\lambda_P\ell^{\rm rel}_{\mathsf H}(Z_{f,W,V})}
 \le a_P(\ell)e^{-\lambda_T\operatorname{St}(W)},\quad
 a_P=6e^{\kappa/2}\vartheta_PN_{\rm ex}
                  e^{-\nu(G_0-C_{\rm pr}-2c)} .\ } \tag{31}
\]
The supremum of \(a_P\) over all allowed histories with \(\ell\ge\log\gamma^{-2}\) tends to zero as \(\gamma\downarrow0\), with preceding choices fixed.

*Proof.* Terms failing Theorem 2's support condition vanish. For the others, set \(m=m_{X(f)}(W\cup V)\). Since \(a\ge24\), use \(\tau=a\) in (23). Equations (10), (12) give
\[
 |f_{W,V}|\le3\widehat\omega_fe^{-\kappa d_o}
                   (3\vartheta)^{|W|}q_{\rm sw}^{|V|}e^{-\mathfrak r m}.
\]
We need \(m_{X(f)}(W)\le2m\). Indeed, in the metric closure of the complete graph with \(X(f)\) collapsed to \(*\), double a realized tree for \(W\cup V\), shortcut to \(W\cup\{*\}\), and delete its closing edge. The closure replaces an ordinary edge only by a shorter route through \(*\); replacing those shortcuts by their root edges does not increase an MST. This proves the inequality.

Multiply by the two exponential weights in (27), (13). Conditions (30), including \(\lambda_P/\eta\le\mathfrak r/4\), leave
\[
 3e^{5\kappa/16}\widehat\omega_fe^{-11\kappa d_o/16}
 [3\vartheta e^{(\lambda_P+\lambda_T)c}]^{|W|}
 q_{\rm sw}^{|V|}e^{-24m}.
 \tag{32}
\]
Split the last exponential into rates \(12,6,6\).

For the first rate, write \(V=(V\cap W)\sqcup V'\). There are at most \(2^{|W|}\) choices of the first part; discard its factor \(q_{\rm sw}^{|V\cap W|}\le1\). Contracting \(W\) into the root lowers the tree cost, so \(m\ge m_R(V')\), \(R=X(f)\cup W\). Lemma 5.1 applies to \(V'\subset\mathcal P\setminus(N_f\cup W)\), and
\(\Xi_R\le\Xi_X+2|W|\), by (2). Lemma 5.3 and (30) give
\[
 \sum_V q_{\rm sw}^{|V|}e^{-12m}
 \le e^{\kappa(1+d_o)/16}\,2^{|W|}e^{4q_{\rm sw}|W|}
 \le e^{\kappa(1+d_o)/16}e^{|W|}.
\]
Here \(q_{\rm sw}\le1/16\) implies \(q_{\rm sw}\le1/(4e)\) and \(2e^{4q_{\rm sw}}\le e\); \(e<4\) and \(e^{3/4}>2\) follow from their elementary series.

From the remaining \(e^{-10\kappa d_o/16}\) reserve \(e^{-\kappa d_o/8}\) for the gap. By (13) and \(6m\ge3m_{X(f)}(W)\),
\[
 \kappa d_o/8+6m\ge\nu(G_0-C_{\rm pr}-2c).
\]
The last factor \(e^{-6m}\), together with \(e^{-\kappa d_o/2}\), sums over \(f\). Fix \(c_0\in W\) and assign each \(f\) to a nearest read cube; (2), (12) give
\[
 \sum_f\widehat\omega_fe^{-\kappa d_o/2}
                         e^{-6d(c_0,X(f))}\le2N_{\rm ex}.
\]
The last two bounds are uniform in \(V\), so they may be extracted before the forest sum. Combining them with (32), and using \(\vartheta_P^{|W|}\le\vartheta_P\), yields (31) with the stated, slightly enlarged prefactor.

For the limit, \(N_{\rm ex}\) is polynomial in \(\ell\), \(\vartheta_P\to0\), and \(G_0\ge10L(\ell-1)^{r_{\rm RUN}}-2\). The exponential gap dominates every fixed power: \(e^x\ge x^n/n!\) with \(r_{\rm RUN}n>t_{\rm ex}+1\) gives a uniform vanishing tail. Finally the choices are feasible in their stated order, conditional on the geometric and analytic imports. With early \(\eta>0\), \(\Psi_\eta\) is fixed; increasing \(\bar\kappa\) makes \(\mathfrak r\) large and \(q_{\rm sw}\) arbitrarily small, enforcing all its floors in (30). Decreasing \(\gamma\) enforces (TJ), the scalar lower bounds in (25), (13) and \(\vartheta_P<1\) by RUN and \(q>p_0\). Enlarged torus room remains a separate premise. ∎

## 6. The remaining CI interface

**Proposition 6.1 (class pieces).** Suppose CI H-C has a presentation of the explicit form \(F_f\) in (19), using Theorem 1, S-loc and A's complete pair reads, and satisfies \(F_f(P;s,0)=f_0(P)\) for all admitted switches. Then CI Lemma 1's class piece indexed by \(Y\supset X_f\) is pair-local on \(N_1(Y)\). For connected \(Y\),
\(\ell^{\rm rel}_{\mathsf H}(N_1(Y))\le81|Y|-1\).

*Proof.* All switch vectors in the defining mixed derivative/integral are supported in \(Y\). Theorem 1 and S-loc place their pair reads in \(N_1(Y)\). At \(Y=X_f\), the subtracted \(f_0\) has those same reads by the H-C zero-fluctuation identity evaluated at \(\mathbf1_{X_f}\); it cannot be dropped from the argument. Switch derivatives and integrals preserve this locality. A connected \(Y\) and its neighbour stars give a connected graph on at most \(81|Y|\) cubes; its spanning tree, contained in \(N_1(Y)\), proves the length bound even without excusing a member. ∎

**G-P — actual Gaussian pair locality (import).** The assigned Gaussian functional for a union \(X\) of gas supports reads \(P\) only on \(N_{c_G}(X)\), factorizes as required by CI H-S, and exists holomorphically on the actual regional domains with coherent branches. D3L §2 proves the relevant algebra conditionally on separately tagged precision and inverse-root series and regional existence. One must invert the live block, not a globally singular zero extension; the inverse root has its own assignment. IN1's path-decoupled global matrix construction does not supply heredity. G-P is additional to the response locality proved above.

**Proposition 6.2 (conditional transfer of a labelled cluster majorant).** Suppose the **already formed** CI activities on gas supports admit absolutely convergent decompositions
\(z(W)=\sum_Yz(W,Y)\), with pair reads in \(Y\), \(W\subset Y\), and gas anchors outside every excused member. Each incompatibility edge must admit anchors in its two supports at fine-graph distance at most \(c_{\rm inc}+1\). Put
\[
 \|z\|_P(W)=\sum_Y\sup|z(W,Y)|e^{\lambda_P\ell^{\rm rel}_{\mathsf H}(Y)}.
\]
Assume G-P and that
\[
 e^{\lambda_P[c_{\rm inc}+1+(2c_G+1)^4|W|]}\|z\|_P(W)
\]
satisfies the actual absolute activity majorants used in CI Lemma 4/Theorem 5, in their prescribed support units. Then the cluster logarithm has pair-labelled pieces with the same weighted absolute majorant as CI (28).

*Proof.* Expand the activity labels in each connected cluster term. For each label choose an admissible covering tree; a gas anchor is unexcused, so that tree meets it. Along an incompatibility tree, join the corresponding gas anchors by paths of length at most \(c_{\rm inc}+1\). Add spanning trees for the Gaussian read neighbourhoods, costing at most \((2c_G+1)^4\sum_j|W_j|\). File the term on the union of all original labels **and all these paths and neighbourhoods**. The resulting connected tree is contained in its new label. Excusing the union of the original excused subfamilies gives
\[
 \ell^{\rm rel}_{\mathsf H}(Z)
 \le\sum_j\big[\ell^{\rm rel}_{\mathsf H}(Y_j)
                    +c_{\rm inc}+1+(2c_G+1)^4|W_j|\big].
\]
G-P bounds the pair reads by this label. Absolute convergence permits expansion and regrouping. Replacing each scalar activity modulus in CI's rooted-tree proof by the assumed weighted majorant proves the assertion, with its same constants. This argument asserts neither those input majorants nor covariance of the chosen paths. ∎

**Outstanding — formation and class matching.** Theorem 3 bounds exempt **potentials**; Proposition 6.2 assumes weighted **activities** after the actual Gaussian, Mayer, cutoff and coarse-switch formation. The intervening weighted estimates, domains and carrier rules have not been supplied. Connected regrouping may add non-gas cubes; those cubes and all joining paths must remain in the labels and their costs must be paid. The numerical unit slack \(\lambda_T-\lambda_V=1\) alone is not a proof of this interface.

Likewise, **(Cls)** remains a proposed change to IN1: replace its excused standing-island hulls by the \(F_H\) of (24) and prove the entire class induction, per-cube bounds, formation and restriction rules for those lengths. Equations (25), (27), (31) prove separation, a containing-box bound and a conditional producer estimate. They do not prove that changing only \(C_{\rm isl}\) to \(2C_{\rm isl}\) preserves the other hypotheses. In particular \(\lambda_P>0\) must still be compared, after scale conversion, with IN1's required boundary rate. Retained birth-level bounds in SA 19523 do not establish nesting of the new collars under coarsening. That requires an actual scale/hull comparison, including rounding and region histories.

The draft's three proposed obstructions have correspondingly limited force. Its uncollared-hull argument uses the size of a chosen overlarge carrier, not a lower bound for every possible decomposition; its \(s_H^4\) shell lower bound also needs a shape assumption. A logarithmic collar does not pay the \(s_H\)-long connector by the present root-edge allocation, but this is a failure of that estimate, not an impossibility theorem. SA's eight/ten-cell quiet boxes give no stated exterior collar around all reads. None proves a no-go for another filing construction. Besides (Cls), actual DR/[RED]/current identification, S-loc, full regional domains, (11), G-P, weighted formation, restriction/overlap/covariance and scale conversion all remain imports or Outstanding obligations.

## 7. Source and definition record

External sources are the pinned [SA outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex), [CA-I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex), [CA-II](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex), [CA-III](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_III.tex), and [YM3-I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM3/YM3_I.tex). Each was fetched once; none was read whole. The outline index README, matching chunk rows and neighbours, obligations, and the CA 4.12–4.19 index were consulted before bounded source reads. The table covers the draft's direct external quotations and the additional decisive comparisons. It checks what the passages state, not the truth of all their hypotheses.

| Lines checked | Finding |
|---|---|
| SA 5721–5805, including 5738–5739, 5762–5770, 5782–5785, 5794–5802 | Coordinate restriction, specified maps and R9 are as cited. Holomorphy is on fixed real-reference slices; independent-current continuation and physical ties are distinct. Existence, uniqueness and splitting are substantive response inputs. |
| SA 10354–10412 | The reduced prescription, weighted norms, operator/contraction assertions and one-sentence uniqueness/splitting argument are present. They do not supply the missing [PW]/[RED] proofs. |
| SA 6180–6214 | Relative trees meet unexcused cubes and chosen whole members, rather than filling excused members; the declared family is standing-island hulls. R23 gives the class bound. |
| SA 17573–17585 | Eight/ten-cell quiet geometry and nonwrapping are conditional class conditions. They do not imply an exterior read collar or torus room for our later enlargement. |
| SA 17903–17926 | Walk tags, switch interpolation and bracket localization are as cited; inherited domains remain an input. |
| SA 19515–19524 | Carried terms keep birth-level domains/lengths/bounds. The draft's geometric coarsening/nesting inference does not follow. |
| YM3-I 49115–49182, including the quoted 49131–49168 | The local component argument retains the identity term, protects local maps by interior neighbourhoods and uses uniqueness. It explicitly permits local pair iteration without a global extension. This supports the credited method, not automatic four-dimensional domain supply. |
| YM3-I 52578–52594 | Tags attach to individual coefficient/string hulls; this corroborates the full-read convention. |
| CA-II 16013–16045; CA-III 3510–3528 and 12278–12295 | Relative trees are contained in their domain. Traversing a member is charged. The draft's ambient-tree construction therefore needed the label enlargement in Lemma 5.2. |
| CA-I 49495–49547 and 54985–55008 | Application admission/drop-out conditions are not furnished by the operator statement; the preparatory theorem assumes its stage/profile inputs. These passages supply no missing local response or CI domain. |

The complete pass-1 draft, TD, TD2 and CI were read. Context checks used the relevant assembly interfaces; frozen P82's scope, IN1's class/order/H-M and amendment, TP1's running minimum; ST1-r2's theorem/imports and ST1-draft3's CI caveat; the draft-cited ST1-r3 (43) and CV qualification; O1D, HW and its repair/gate; LOC-3 and its gate; DF, NR9, D3L and its gate; PW-bridge's §6 hypotheses and §7 composed assignment; WF-room-2 (6.1); NL1-L H-DR; CRIT's uniqueness formulation; and TD2-draft's joint-estimate proposal. Gate verdict words were not treated as proofs. In particular HW's gate preserves field reads at fixed regions, LOC-3's gate is conditional, and D3L's gate does not identify a different independent-current completion.

Definitions supplied or sharpened here are:

1. Fixed coordinate restrictions and switch supports, the separate fine and layer metrics, \(r_g\) distinct from an analytic small radius, deep sets, split maps, auxiliary field \(\alpha\) distinct from rate \(a\), and the original common solution balls used for two-pair splicing.
2. The required identity of parameter and fine switch grids, full-data S-loc, and the local anchor \(J_*\) distinguishing the two current prescriptions.
3. The mixed coefficients \(f_{W,V},g_{B,A}\), complete fixed stencils, duplicated cube labels, \(\delta_J\), and the precise \(\tau\)-range and corner amplitudes.
4. Read-rooted \(m_R\) without a metric assumption, the allowed-vertex forest sum, and the intrinsic relative length (infinite when no contained tree exists).
5. The early collar fraction \(\eta\), box side \(s_H\), explicit enlarged-torus premise, \(\rho_H,\widehat H,F_H,N_f\), raw reads \(Y\), filed labels \(Z\) including \(U\), and fixed choices of connectors.
6. The arbitrary-hub sum \(\Psi_\eta\), separate old length \(d_o\) and output \(\operatorname{St}(W)\), rates \(\lambda_P,\mathfrak r,q_{\rm sw}\), amplitude \(\vartheta_P,a_P\), and its uniform history-tail limit.
7. Pair-labelled activity norms, joining-path labels and the distinction between a potential bound, a formed-activity majorant and full class induction.

## Result

Theorem 1 proves exact two-pair locality for the specified equations and current, conditional on the assigned expansions, their field hulls, the common solver and its uniqueness. The depth \(3LM_1\) exceeds the actual consecutive reach \(2r_g\); the completed source adds one cube layer under S-loc. Theorem 2 proves the read-rooted \((\mathrm{JC}_\tau)\) family under R, A, the complex island deficit and (TJ). Lemma 5.1 preserves collar-width decay. Theorem 3 proves a summable intrinsic pair-filing bound under the additional amplitude and ordinary-tree/hub/RUN imports, for the proposed collared excused family and enlarged filed labels. These are conditional mathematical implications, not established actual-response or CI closure.

Corrections made in distilling the draft:

1. Retain the unparameterized \(-a_0I\) in \(M_s\); it is local, not split. Verify the derivative series and all five nonlinear terms with maximum local reach \(2r_g\). Distinguish the once-tagged coefficients of the separately assigned \(\mathfrak G\) from products of already assigned operators.
2. Replace the unsupported reduced-variable ball correspondence by splicing the original \(\alpha,h\) solutions in their original common balls, with matching source normalization and \(s_D\le b_*\) when using R. Use elementary norm stencils, not a radius-one assertion about an entire pillar. Make the first-exit depth argument and tree-read margin explicit.
3. Make the fine-grid identity an import. Distinguish image-domain descent from the uniformly holomorphic local solver needed on full declared domains; repair the unjustified real-extension choice by conjugation, when its hypotheses hold.
4. Distinguish D3L's force-anchored current from ST1's independent-current formula. Specify both via (7); do not infer their equality from physical-locus agreement.
5. Restrict Proposition 3.2 to the analytic/bound/component clauses it verifies, use a current-only response with the actual kind of stencil seminorm, and replace the draft's unit source by an amplitude inside the prescribed source ball. Its derivative-positivity argument is valid; it is not a Yang–Mills counterexample.
6. Preserve complete stencils and the read-rooted expansion for (JC). State the exact nonempty \(\tau\)-range and the conditions for \(\tau=12,a\). The old simultaneous \(a-12\) rate and \(D^{-1/2}\) switch factor are not proved; calling the whole family simply “stronger” would obscure that tradeoff.
7. Keep the valid corner-amplitude reduction and forest sum. Correct the collapsed-collar comparison from \(\Xi\ge N\) to \(\Xi\ge Ne^{-s}\).
8. Replace the invalid bounding-box shell estimate for an arbitrary hub by (29). Include connector vertices in \(Z\), so the filing tree really is contained in its domain.
9. Strengthen the scalar collar ceilings and state enlarged torus room separately. Fix \(\eta\) before \(\kappa\), independently of \(M,\bar\kappa\); replace the draft's late equality \(\eta=4\lambda_P/\mathfrak r\) by the later floor \(\lambda_P/\eta\le\mathfrak r/4\). Retain TD2's \(C_{\rm win}\) and stronger binding power floors. Use \(\operatorname{St}(W)\), not an \(f\)-dependent symbol after summing over \(f\), and state the uniform tail limit.
10. Require the explicit localized presentation and H-C's zero-fluctuation identity for the class-piece argument. In the labelled cluster implication require nearby gas anchors and include connecting paths in the filed support; retain G-P, live-block inversion, actual activity majorants and full regional existence as hypotheses.
11. Withdraw the claim that Theorem 3 alone feeds the complete CI activity construction, that doubling \(C_{\rm isl}\) proves (Cls), or that SA's birth-level rule proves collar nesting. The three failed approaches are limitations of those arguments, not universal obstructions.

The draft's four proposed corrections to other notes have these dispositions. Dropping NL1-L's “at fixed \(P\)” is justified **only for the identified specification and under Theorem 1/S-loc's imports**; it is not an unconditional edit to H-DR. Replacing TD2-draft's (JC) by (23) is a valid sufficient alternative, with its explicit tradeoff; TD2 Corrections 9–10 remain correct, and (31) answers the latter only for the stated labels and family. Dropping (5-sw) is valid for this route, while retaining the complex deficit (11). Replacing IN1's excused family is a proposal still requiring (Cls), not an established correction to frozen IN1.

Only this manuscript and its source/checkpoint records were written. No frozen note, gate, ledger, editable prompt file or platform instruction was changed. Retrieval, hashing and file checks supplied no mathematical evidence. **This text is not yet refereed.**
