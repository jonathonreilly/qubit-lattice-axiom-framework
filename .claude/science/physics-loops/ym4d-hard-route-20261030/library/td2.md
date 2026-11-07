# TD2: ordinary-distance tree decay and conditional CI closure

Provenance: Pass-2 distillation by Codex of Claude's `td2-draft.md`, in checkout `afb2abc83f0f3a05a76b6f0ee8fca5cd6ad45ccc`; research text, not an audit, granting no status. Material drawn from the Sussman–Alpoge sources is credited to Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text. Not yet refereed.

Theorem 3 (A) proves ordinary-distance decay from the binding TD imports and an additional ordinary carrier tree. Theorem 9 (B) gives CI only with the actual local-domain, Gaussian, filing and remaining formation inputs. Ordinary decay supplies neither external-pair locality nor those inputs. All proofs below are written arguments.

## Definitions and imports

Write TD for [td.md](td.md), CI for [ci-form.md](ci-form.md), and IN1 for the frozen [in1.md](in1.md). Fix a finite main-step history and its supplied open complex fibre \(\mathcal O_\sigma(U)\), with real \(U\) and near stored variables fixed. All bounds are uniform in the history, level, volume and every point of the stated fibre. For a local-domain conclusion, the same hypotheses must hold on every declared local fibre, not merely on restrictions of one global pair.

Fine cubes have side \(M\) in level-\((i-1)\) units; write \(\mathcal C\) for their finite set. Their graph uses corner adjacency and has degree at most 80. Let \(d\) be its periodic graph distance, \(N_c(A)=\{x:d(x,A)\le c\}\), and \(\operatorname{St}(W)\) its least tree edge count covering \(W\), with extra vertices allowed. Each free bond has one owning cube; \(\mathcal C_I\subset\mathcal C\) is the set of such cubes. Let \(|\zeta|_c\) be the largest absolute scalar coordinate owned by \(c\), and let \(\zeta\mathbf1_A\) retain only coordinates owned by \(A\). For nonempty \(W\subset\mathcal C_I\), set
\[
 D_WF(\zeta)=\sum_{A\subset W}(-1)^{|W\setminus A|}F(\zeta\mathbf1_A),\qquad
 m_X(W)=\operatorname{MST}(W\cup\{*\}),                         \tag{1}
\]
where the complete graph has weights \(w(c,c')=d(c,c')\) and \(w(c,*)=d(c,X)\). These root weights need not define a metric.

Constants in denominators and all decay rates are positive; amplitudes are nonnegative. Normalize the imported upper-bound constants so that \(E_{\bar\kappa},C_h^{\rm WF}\ge1\). The binding imports are TD **R, A, X, G, RUN**, with all their qualifications:

* **R (ST1/NL1-L):** the actual jointly holomorphic response \(h(s;P,S)\) on the full row-product source ball \(\|S\|_{\rm src}<s_D\) and \(|s_c|<e^{\bar\kappa}\); its zero-source, reality, restriction and component-read clauses; and
  \(n_b(h)\le C_DE_{\bar\kappa}\|S\|_{\rm src}e^{-\mu_Rd_+(b,\operatorname{supp}S)}\).
  Here \(n_b(H,K)=\max\{l|H|,l^2|\nabla^UH|,l^3|K|\}\); its connected read stencil \(B_b\) contains the initial-site cube \(\Delta_b\) and has at most 16 cubes. The source norm is the maximum row norm; its full product ball admits row masks and independent row scalings within the ball. The metric \(d_+\) is the supplied input-layer metric, not \(d\). R includes the completed source \(S(v_0+u(s\odot\zeta))\), all supported in a fixed row set \(\mathcal S\), the cube-local linear bound \(\|u(\zeta)\|\le c_Tg\|\zeta\|\), source Lipschitz constant \(C_A\), chart radius \(c_{\rm ch}L^{-9}\), one-layer row reads, and \(M\ge R_\sigma+3\). Physical identification at \(s=1\) remains part of the actual-response import. Frozen P82's real-reference inverse does not supply R.
* **A (NL1-L/ST1/LF1):** arbitrary-shift admission on every complete endpoint, pin and stored-slot read, with the V1–V6 and ST1/ST3 admission inputs named in TD. For each old exempt term, let \(\mathcal B_f\) be its reads, \(X(f)=\{\Delta_b:b\in\mathcal B_f\}\ne\varnothing\), and \(X_f\supset X(f)\) its presentation set. The admitted function \(\Phi_f(P,h)\) is holomorphic for \(n_b(h)<A_b=A_Ve^{-\mu_Rd_+(b,\mathcal S)}\). Two-sided terms have bound \(b_f\), kept forms oscillation \(\omega_f\), and islands have \(\operatorname{Re}\Phi_f\le A_f\) together with
  \[
   A_f-\operatorname{Re}\Phi_f(P,h_0(P))\le B_f.                 \tag{2}
  \]
  Set \(\widetilde\omega_f=2b_f,\omega_f,2B_f\), respectively. **Outstanding:** the island deficit (2), uniformly on the complex fibre, is still an import. A real-base estimate does not prove it.
* **X (NL1/LF1):** write \(d_f^{\rm old}\ge0\) for the supplied old length. Boundary and kept-form lengths retain their literal SA relative-tree meaning; island lengths are zero. Require
  \[
  \widetilde\omega_f\le\widehat\omega_fe^{-\kappa d_f^{\rm old}},\qquad
  \sup_c\sum_{f:X(f)\ni c}\widehat\omega_fe^{-\kappa d_f^{\rm old}/2}
       \le N_{\rm ex}\le C_{\rm ex}(M)\ell^{t_{\rm ex}}.          \tag{3}
  \]
  These are bounds on the same admitted complex functions, including their actual multiplicities.
* **G (LF1 geometry):** hubs \(\widetilde H=N_2(H)\) are separated by \(s_0=\check R_i-4\). Each lies in a box of side \(D_H=C_{\rm isl}L\check R_i+6\); these boxes and their fixed collars have nonwrapping lifts. Gas cubes have distance at least \(G_0=10L\check R_i-2\) from every hub and the live set. Retain TD's geometric ceilings (7) and contracted premise (8) as binding inputs, although the ordinary proof below does not use their contracted-length bounds.
* **RUN (IN1/TP1/PAN):** \(\ell=\log\theta_{i-1}\), \(g=e^{-\ell/2}\), \(\theta_{i-1}\ge\gamma^{-2}\), and uniformly \(\check R_i\ge(\ell-1)^r\), \(r\ge2\), below a final coupling ceiling. The running-minimum convention and frame bounds are retained. No adjacent-radius ratio tending to one is assumed. Ordinary potential amplitudes needed by Theorem 9 tend uniformly to zero with \(\gamma\).

For admission, use [st1-r3.md](st1-r3.md), Theorem 14 and Corollary 14′, with their actual-domain and F-measure/F-contour qualifications where applicable. The earlier [st1-r2.md](st1-r2.md), Theorem 14, and [st1-draft3.md](st1-draft3.md), §6, do not remove those qualifications. CI-old supplies only already formed activities, never the bound being proved.

Retain TD (4)'s definitions, made explicit here:
\[
\begin{gathered}
 \mathfrak b=C_{\rm win}A_1\ell^{p_0},\quad R=\ell^q,\quad
 \delta_{\rm src}=A_1g\ell^{p_0},\quad p_0>0,\quad q>p_0+2r,\quad C_{\rm win}\ge1,\\
 s_D=\epsilon_De^{-c_D\bar\kappa},\quad D=e^{\bar\kappa}-1,\quad
 a=\tfrac12\log(D/6400),\quad\delta=(8e)^{-1},\\
 \varrho=\frac{\min\{s_D/2,C_Ac_{\rm ch}L^{-9}/2\}}
                 {c_TC_Ae^{\bar\kappa}g},\quad
 A_R=4C_DE_{\bar\kappa}s_DD^{15},\\
 A_V=C_DE_{\bar\kappa}C_A(3\delta_{\rm src}+c_Tge^{\bar\kappa}R),\quad
 K_1=\max\{1,4A_R/A_V\},\quad
 \vartheta=\frac{4K_1\mathfrak b}{\delta\varrho}.                 \tag{4}
\end{gathered}
\]
The fixed window conversion is absorbed in source constants wherever needed. R includes \(C_A\delta_{\rm src}<s_D/2\) and \(\|v_0\|<c_{\rm ch}L^{-9}/2\). Define
\[
\begin{split}
 h_0(P)&=h(\mathbf1;P,S(v_0)),\\
 G(s,\zeta)&=h(s;P,S(v_0+u(s\odot\zeta)))-h(s;P,S(v_0)),\\
 f_W(P;\zeta)&=D_W[\Phi_f(P,h_0+G(\mathbf1,\cdot))](\zeta),\qquad
 V^{\rm ex}(W)=\sum_f f_W.                                    \tag{5}
\end{split}
\]
TD Lemmas 1–4, with R and A exactly as above, give the analytic input
\[
 |f_W|\le\widehat\omega_fe^{-\kappa d_f^{\rm old}}
                 \vartheta^{|W|}e^{-(a-6)m_{X(f)}(W)}           \tag{6}
\]
on \(|\zeta|_c\le\mathfrak b\), whenever \(a\ge12\) and \(\vartheta<1\). Their proof uses the row expansion, Bird's tree allocation and holomorphic composition; it does not identify external carriers with \(W\).

Two additional hypotheses are used here.

**G-ord.** Fix the integer \(C_{\rm isl}\ge1\), integer collar width \(c\ge0\), and projection constant \(C_{\rm pr}\ge1\) with IN1's geometric constants. They precede \(\kappa\), are independent of \(M,\bar\kappa\), and are uniform in the subsequent choice of \(L\). Put
\(\widetilde H^+=N_c(\widetilde H)\) and \(\eta=1+C_{\rm isl}/10\).

**X° (ordinary carrier tree; NL1/LF1 import).** Each \(f\) has a fine-graph tree \(T_f\), with
\[
 |E(T_f)|\le C_{\rm pr}(1+d_f^{\rm old}),                       \tag{7}
\]
such that every \(x\in X_f\) either lies within distance \(c\) of \(T_f\), or lies in \(\widetilde H^+\) for a hub met by \(T_f\). Also \(X_f\) meets a hub or the live set.

**Outstanding — supply of X° and G-ord.** A literal SA relative tree can supply (7) only after proving the scale conversion, read-collar coverage and containment of each excused hull in a current hub. Those are TD's existing carrier-geometry imports, now required before contraction. The single source definition does not prove them. Nor does X° imply TD (8) with the same constant: a collar outside one contracted hub can contain arbitrarily many distinct vertices. We retain (8) separately. The O(1)-cell class rule motivates G-ord; its uniform application to all later standing islands remains LF1 geometry.

## Ordinary-distance decay

**Lemma 1 (paying hub crossings).** If
\[
 10L\check R_i\ge6+2c+\eta(2+c),                              \tag{8}
\]
then, for nonempty \(W\subset\mathcal C_I\),
\[
 \operatorname{St}(W)\le(1+\eta)m_{X(f)}(W)
                  +C_{\rm pr}(1+d_f^{\rm old})+c|W|.           \tag{9}
\]

*Proof.* Root a minimum tree for (1) at \(*\). Realize each ordinary edge by a fine geodesic. Realize each root edge \((c_0,*)\) by a geodesic to a nearest \(x_{c_0}\in X(f)\). Their union \(Q\) has at most \(m=m_{X(f)}(W)\) edges. Every component joins some cube of \(W\) to such an endpoint.

If \(x_{c_0}\) lies within \(c\) of \(T_f\), join it at cost at most \(c\). Otherwise X° places it in a collared hub met by \(T_f\). Both endpoints of a connector then lie in a nonwrapping box of side \(D_H+2c\). Corner adjacency gives a connector of length at most that side. The corresponding root edge costs at least \(G_0-c\). Consequently the number of these second connectors is at most \(m/(G_0-c)\). Their total cost is at most \(\eta m\), because (8) is exactly
\[
 D_H+2c\le\eta(G_0-c).
\]
It also makes the denominator positive. The union of \(Q,T_f\) and all connectors is connected and covers \(W\). Its edge count is bounded by the right side of (9); deleting cycle edges proves the claim. ∎

**Lemma 2 (the gap supplies smallness).** Under X° and G,
\[
 m_{X(f)}(W)+C_{\rm pr}(1+d_f^{\rm old})+2c\ge G_0.            \tag{10}
\]

*Proof.* Follow the root-tree path from a gas cube to some endpoint \(x\in X(f)\); it costs at most \(m=m_{X(f)}(W)\). If \(x\) lies in a collared hub, another \(c\) edges reach that hub. Otherwise reach \(T_f\) within \(c\) edges. Choose \(y\in X_f\) in a hub or the live set. If \(y\) is within \(c\) of \(T_f\), traverse \(T_f\) and then reach \(y\). Otherwise X° gives a hub met by \(T_f\), which the same traversal reaches. This produces a walk of length at most the left side of (10) from a gas cube to a hub or the live set. G bounds every such distance below by \(G_0\). ∎

**Theorem 3 (A: ordinary TD).** Assume R, A, X, G, RUN, X° and G-ord. Choose the ordinary gas rate \(\lambda_V\) as specified below and put
\[
 \lambda_T=\lambda_V+1,\quad\vartheta_T=\vartheta e^{\lambda_Tc},\quad
 a_1=a-6-\lambda_T(1+\eta),\quad
 \nu=\min\{\kappa/(4C_{\rm pr}),a_1/2\}.
\]
Require (8) and
\[
 \lambda_TC_{\rm pr}\le\kappa/4,\qquad a_1\ge12,
 \qquad\vartheta_T<1.                                       \tag{11}
\]
Then (5) is an exact fluctuation-local decomposition of the exempt exponent difference, holomorphic in \((P,\zeta)\) and real at real data, with
\[
 |V^{\rm ex}(W;P,\zeta)|\le a_T(\ell)e^{-\lambda_T\operatorname{St}(W)},\qquad
 a_T(\ell)=2e^{\kappa/4}N_{\rm ex}\vartheta_T
                 e^{-\nu(G_0-C_{\rm pr}-2c)}.                 \tag{12}
\]
The bound holds throughout \(|\zeta|_c\le\mathfrak b\). Its uniform envelope over all histories with \(\theta_{i-1}\ge\gamma^{-2}\) tends to zero as \(\gamma\downarrow0\), with all preceding choices fixed.

*Proof.* Put \(m=m_{X(f)}(W)\) and \(d_o=d_f^{\rm old}\). Equations (6) and (9) give
\[
 e^{\lambda_T\operatorname{St}(W)}|f_W|
 \le e^{\lambda_TC_{\rm pr}}\widehat\omega_f\vartheta_T^{|W|}
       e^{-(\kappa-\lambda_TC_{\rm pr})d_o-a_1m}.
\]
Leave \(\kappa d_o/2\) and \(a_1m/2\) for summation. The remaining exponent is at least
\[
 \kappa d_o/4+a_1m/2\ge\nu(C_{\rm pr}d_o+m)
                     \ge\nu(G_0-C_{\rm pr}-2c)
\]
by (10). Also \(e^{\lambda_TC_{\rm pr}}\le e^{\kappa/4}\) and \(\vartheta_T^{|W|}\le\vartheta_T\).

Fix \(c_0\in W\). A root-tree path gives \(m\ge d(c_0,X(f))\). Assign each \(f\) to a nearest read cube \(\Delta_f\). Since \(a_1/2\ge6\), (3) and TD Lemma 1's distance sum yield
\[
 \sum_f\widehat\omega_fe^{-\kappa d_o/2-a_1m/2}
 \le\sum_\Delta e^{-6d(c_0,\Delta)}
              \sum_{f:X(f)\ni\Delta}\widehat\omega_fe^{-\kappa d_o/2}
 \le2N_{\rm ex}.
\]
This proves (12). Finite Boolean inversion gives
\(\sum_{W\ne\varnothing}f_W=\Phi_f(P,h_0+G(\mathbf1,\zeta))-\Phi_f(P,h_0)\).
Finite composition and summation preserve holomorphy and reality. The definition of \(D_W\) gives exactly the claimed fluctuation reads.

For fixed preceding constants, (4) gives
\(\vartheta\le C(g\ell^{p_0}+\ell^{p_0-q})\to0\).
RUN and (3) bound (12) by a fixed constant times
\(\ell^{t_{\rm ex}}\vartheta_Te^{-\nu[10L(\ell-1)^r-2-C_{\rm pr}-2c]}\).
For large \(\ell\), its exponential dominates every fixed power: use \(e^x\ge x^n/n!\) with an integer \(rn>t_{\rm ex}+1\). This proves a tail bound tending to zero, hence the asserted supremum limit. No numerical estimate is used. ∎

**Order of choice and feasibility.** Retain every applicable IN1/ST1/CI floor and ceiling. The following additions do not move a later constant into an earlier choice.

1. Fix powers, margins, type count, window conversion, \(C_{\rm isl},c,C_{\rm pr}\), and all rate-window geometry in IN1 rows 1–2. Write
   \[
   A_o=(1+4\beta_s)C_h^{\rm UM}c_\ell,\qquad
   B_o(L)=\lambda_0+\sigma_0+C_h^{\rm UM}(3+c_\ell g_*)/L.
   \]
   Choose odd \(L\ge27\) with
   \(L>\max\{4C_h^{\rm WF},8C_{\rm pr}\}A_o\), retaining IN1 Amendment 1's existing floors. Every constant used to choose \(L\) is uniform in \(L\).
2. Before \(\kappa\), independently of \(M,\bar\kappa\), fix TD Theorem 10's **base** response/chart/admission constants \(C_D,\mu_R,C_A,c_T,c_D,\epsilon_D,c_{\rm ch},R_\sigma\), the prescribed parameter law for \(E_{\bar\kappa}\), and the actual Gaussian reference/envelope constants and \(W_0\) required by CI/IN1. This does not fix the later source thresholds, radius coefficients or activity amplitudes. Let \(u=\min\{(2C_h^{\rm WF})^{-1},(4C_{\rm pr})^{-1}\}\). Choose
   \[
   \kappa\ge\frac{2[B_o(L)+\varepsilon_{\rm rate}+1]}{u-A_o/L},\qquad
   \lambda_V=A_o\kappa/L+B_o(L),                              \tag{13}
   \]
   with all imported floors. The denominator is positive. Indeed \(A_o/L<u/2\). Thus \(u\kappa-\lambda_V>\varepsilon_{\rm rate}+1\), giving both IN1 (24) and \((\lambda_V+1)C_{\rm pr}\le\kappa/4\). If the natural route is kept simultaneously, use TD (32)'s common-window slope and intercept in both the \(L\)-floor and (13).
3. Next choose \(\bar\kappa\) with every response/bracket floor, \(\bar\kappa\ge\lambda_V+2\), and
   \[
   \log(e^{\bar\kappa}-1)\ge
   \max\{\Theta_{\rm CI},\ 2\lambda_T(2+C_{\rm isl}/10)+36+\log6400\}.
                                                                  \tag{14}
   \]
   This is exactly the additional condition \(a_1\ge12\). Retain the natural-route floor too if that route is required. Fix \(s_D,E_{\bar\kappa},D,a,A_R\) afterwards.
4. Choose the post-\(\bar\kappa\) response/preparation parameters in IN1 row 5 before \(M\). Then choose \(M\), a power of \(L\), above the imported matrix, collar, source and decay floors. Choose the late radii, \(A_1\), amplitude prefactors \(C_{\rm ex}(M)\), Gaussian tilt and other late IN1 constants in rows 6–8's internal order. Finally decrease \(\gamma\) for (8), \(\mathfrak b<R\), \(\vartheta_T<1\), TD's retained ceilings, and the imported source, admission and gas-amplitude ceilings. RUN makes (8) and the retained logarithmic geometric ceilings hold. The quantities \(\varrho,A_V,K_1,\vartheta\) are running functions of \(\ell\), not constants frozen before \(\gamma\). No new upper bound on \(M\) occurs.

There are **three different constants**: \(C_{\rm isl}\), TD's geometric \(C_0\) in \(D_H\); \(C_0^{\rm rad}\), CI row 5/IN1 row 6's radius coefficient in \(\alpha_{0,j}=C_0^{\rm rad}g_j(\log\theta_j)^q\); and the Gaussian budget \(C_0^{\rm UM}\le1\). The late radius coefficient stays late. TD Theorem 10 step 4's placement of its geometric \(C_0\) is corrected here; it is not a reason to move CI's radius coefficient.

**Corollary 4 (connected fluctuation supports).** Choose one minimum covering tree for each nonempty \(W\), by a fixed total order, and let \(\widehat W\) be its vertex set. For connected fine sets \(Y\), put
\[
 V^\circ(Y)=\sum_{\widehat W=Y}V^{\rm ex}(W).
\]
Then \(\sum_YV^\circ(Y)=\sum_WV^{\rm ex}(W)\), each term reads fluctuations only in \(Y\), and
\[
 |V^\circ(Y)|\le2a_Te^{-\lambda_V\operatorname{St}(Y)}.          \tag{15}
\]

*Proof.* A minimum tree has \(|Y|=\operatorname{St}(W)+1\) vertices. Since \(Y\) is connected, \(\operatorname{St}(Y)=|Y|-1\). There are at most \(2^{|Y|}\) possible subsets \(W\subset Y\). Apply (12) and \(1>\log2\). Exactness is finite regrouping. ∎

The trees may use cubes without free bonds. An actual gas must admit these supports, or supply a separate support conversion. A total order need not preserve lattice covariance or hereditary restriction; those properties of the filed family remain Theorem 9's inputs.

The payment in Lemma 1 is response decay across \(G_0-c\) against a crossing of at most \(D_H+2c\). Their ratio is bounded by \(1+C_{\rm isl}/10\), with no extra factor of \(L\). Travel between distinct hubs of one carrier is paid by the **ordinary** tree (7), not by a contracted path.

## What the contracted premise alone cannot give

The next two examples test analytic and numerical interfaces. They are not Yang–Mills histories and do not satisfy an identification with the actual ST1 response. In Proposition 6 only, replace X's source-length interpretation by **X-num**: the two inequalities (3), with an arbitrary nonnegative old length. This distinction is essential.

**Lemma 5 (mixed differences).** Suppose the gas has exactly two cubes \(c_1,c_2\). Let \(F=\sum_WV(W)\), where \(W\) runs over their nonempty subsets, \(V(W)\) reads only its owned fluctuations, and \(|V(W)|\le a_*e^{-\lambda\operatorname{St}(W)}\). At four points in the stated box, define \(\Delta_1\Delta_2F=F(t_1,t_2)-F(t_1,0)-F(0,t_2)+F(0,0)\), using one scalar coordinate per cube. Then
\[
 |\Delta_1\Delta_2F|\le4a_*e^{-\lambda d(c_1,c_2)}.             \tag{16}
\]
If instead the decomposition has one term for every nonempty fine carrier \(Y\), possibly with non-gas cubes, then for \(\alpha_e=\log12800\), \(\lambda>\alpha_e\),
\[
 |\Delta_1\Delta_2F|\le
 \frac{8a_*}{1-e^{-(\lambda-\alpha_e)}}
                   e^{-(\lambda-\alpha_e)d(c_1,c_2)}.          \tag{17}
\]

*Proof.* Terms missing either coordinate cancel. For (16), only the two-cube term remains; its four evaluations give the factor four. For (17), a carrier containing \(c_1\) with Steiner length \(n\) has a chosen covering tree with \(n+1\) vertices. Encode its vertex set by a rooted tree traversal and its terminals by binary flags. TD Lemma 1 gives at most \(6400^n2^{n+1}=2\cdot12800^n\) possibilities. A carrier containing both cubes has \(n\ge d(c_1,c_2)\). Summing the geometric series and multiplying by four proves (17). ∎

**Proposition 6 (hub chain, without a radius ratio).** Fix a sufficiently large \(\ell\) and a rounded radius \(\check R_i\) satisfying G's ceilings. Under the numerical/analytic clauses of R and A, X-num, G and TD (8), there is no volume-uniform ordinary-TD amplitude at any fixed \(\lambda_T\ge5\kappa/L\), even when \(C_{\rm isl}\) is early. This assertion concerns decompositions indexed by gas subsets. It also holds for arbitrary fine carriers when \(\lambda_T-\alpha_e\ge5\kappa/L\), as permitted by CI's early entropy choices.

*Proof.* Write \(D_H=D_h\), \(s_0=s\), \(G_0=G\), and choose an integer \(m\ge1\). On one axis set
\[
 p_1=G+1,\quad p_{k+1}=p_k+D_h+s+1,\quad
 \widetilde H_k=[p_k,p_k+D_h-1]\times[0,D_h-1]^3.
\]
Take a torus, tiled by the required grids, whose side exceeds twice the whole configuration diameter plus its margins. This prevents periodic shortcuts. Shrinking each displayed hub by two layers gives its hull. Consecutive hubs have distance \(s+2\). At a common transverse centre put
\(c_1=(0,\bar x')\) and \(c_2=(p_m+D_h+G,\bar x')\).
They are the only gas cubes; the live set is empty. Both hub distances are \(G+1\). Set
\[
 d_m=d(c_1,c_2)=2G+1+mD_h+(m-1)(s+1),\qquad
 q_m=2(G+1)+(m-1)(s+2).                                    \tag{18}
\]
Let \(X_f\) be the axis connector together with all hubs, and let \(X(f)=\{c_1,c_2\}\). After contraction, the axis tree covers \(\pi X_f\) with \(q_m\) edges. Thus TD (8) holds with \(C_{\rm pr}=1\) and \(d_f^{\rm old}=q_m\).

Here is a response that avoids the draft's unsupported single-bond gradient assertion. Use a uniform-layer model and only the current component: \(H=0\), and on the two read bonds set
\[
 l^3K_{b_j}(s;S)=\epsilon s_{c_j}S_j,\qquad
 \epsilon=e^{-\bar\kappa}\min\{1,C_D\}>0,
\]
with all other outputs zero. Use two independent scalar source rows, \(S(v)=v\), \(v_0=0\), \(u(\zeta)=c_Tg\zeta\). The response is holomorphic, real, zero at zero source and at zero switches, and component-local. Its seminorm is \(|\epsilon s_{c_j}S_j|\); its gradient entry is zero. A nonzero output has its own source row present, so its source distance is zero. This proves R's size bound on the entire switch disc. The source/chart ceilings hold for sufficiently large \(\ell\).

Write \(k_j=l^3K_{b_j}\), and take
\[
 \Phi_f(h)=\tfrac12e^{-\kappa q_m}(k_1/A_V)(k_2/A_V).
\]
At these source bonds \(A_{b_j}=A_V\), so A holds with \(b_f=e^{-\kappa q_m}/2\). Take \(\widehat\omega_f=N_{\rm ex}=1\); (3) holds. At \(s=1\),
\[
 F(\zeta)=\tfrac12e^{-\kappa q_m}
                (\epsilon c_Tg/A_V)^2\zeta_1\zeta_2.
\]
Use (16) at fixed nonzero real \(|t_j|<\mathfrak b\). Every decomposition then requires
\[
 a_*\ge c(\ell)
  \exp\{(m-1)[\lambda_T(D_h+s+1)-\kappa(s+2)]\},             \tag{19}
\]
where \(c(\ell)>0\) is independent of \(m\). Since
\[
 \lambda_T(D_h+s+1)-\kappa(s+2)
 \ge(5C_{\rm isl}-1)\kappa\check R_i>0,
\]
the amplitude diverges with volume. For arbitrary fine carriers, use (17) and replace \(\lambda_T\) by \(\lambda_T-\alpha_e\) in this calculation.

The bound \(5\kappa/L\) follows from IN1 (24): \(C_h^{\rm UM}\ge1\), \(c_\ell\ge5\), and \(\beta_s\ge0\). The first two inequalities follow by testing the collar bound and \(d_c(Z)+5\le c_\ell|Z|\) on a singleton. Choosing CI's entropy rates with \(\lambda_0+\sigma_0\ge\alpha_e\) gives the condition for (17) as well.

Only the **single current radius** \(\check R_i\) occurs in (18)–(19). No adjacent-radius ratio is used. An ordinary tree approaching both gas endpoints within fixed distance \(c\) has length at least \(d_m-2c\), so X° fails with \(C_{\rm pr}=1\) for large \(m\). A literal SA relative tree likewise cannot omit the intervening hub crossings. Thus this example does not satisfy X's boundary-length convention and does not refute SA or TD's full import package. ∎

**Proposition 7 (an uncontrolled late island size).** Fix \(\kappa,\bar\kappa,\lambda_V>0\). The numerical interfaces, even with X°, do not guarantee ordinary TD uniformly over all subsequent choices of \(C_{\rm isl}\). For gas-subset decompositions it fails if
\[
 C_{\rm isl}>20(\bar\kappa+2)/\lambda_V-20,
 \qquad\lambda_T\ge\lambda_V.                               \tag{20}
\]

*Proof.* Use one hub of side \(D_h\), with two gas cubes on opposite faces at distance \(n=G_0+1\). Its two face read bonds are \(b_L,b_R\). Take \(X_f\) to be the hub, \(d_f^{\rm old}=0\), and \(T_f\) one hub vertex. Then X°, TD (8), and G hold. Choose a uniform-layer lattice metric \(d_+\), with the near source nearest at each face. This is an explicit model choice, not an unproved property of the actual ST1 metric.

Use \(H=0\) again. For \(j=L,R\), let \(r_j\) be the near source row and \(\pi_j\) the straight segment of \(n\) edges from its cube to the face. Put
\[
 l^3K_{b_j}(s;S)=\epsilon e^{-\mu_Rd_+(b_j,r_j)}
       e^{-(\bar\kappa+2)n}\Big(\prod_{c\in\pi_j}s_c\Big)S_j,
 \qquad \epsilon=e^{-\bar\kappa}\min\{1,C_D\}.
\]
All other outputs vanish. A nonzero term lies in one face-component with its source. The product has \(n+1\) switches, hence on the full disc its modulus after the path weight is at most \(e^{\bar\kappa}e^{-2n}\). If \(S_j\ne0\), then \(d_+(b_j,\operatorname{supp}S)\le d_+(b_j,r_j)\). These facts prove R's bound, holomorphy and component reads, without a gradient estimate.

Write \(k_j=l^3K_{b_j}\). Take \(\Phi_f=(k_L/A_{b_L})(k_R/A_{b_R})/4\), with \(A_f=1/4\), \(B_f=1/2\), \(\widehat\omega_f=N_{\rm ex}=1\). Since \(h_0=0\), A and (2)–(3) hold. At each read the layer-distance factor cancels its factor in \(A_b\). Applying (16), with \(t_j\) a fixed fraction of \(\mathfrak b\), gives
\[
 a_*\ge c(\ell)\exp\{\lambda_T(2G_0+D_h+1)
                              -2(\bar\kappa+2)(G_0+1)\}.       \tag{21}
\]
Equation (4) gives \(c(\ell)\ge c_*\ell^{-2(q-p_0)}\) for large \(\ell\), with \(c_*>0\) fixed. The exponent in (21) has coefficient
\(\lambda_T(20+C_{\rm isl})-20(\bar\kappa+2)>0\)
in front of \(L\check R_i\). RUN makes this beat that polynomial. Hence no amplitude tending to zero exists. For arbitrary fine carriers, (17) proves the same statement with \(\lambda_V\) replaced in (20) by \(\lambda_V-\alpha_e>0\). ∎

This shows why some size/rate relation is needed. It does not prove that G-ord, or X°, is the unique possible repair. In this manuscript their early order is the IN1-compatible sufficient choice. The draft's unverified hypothesis (Mon) is unnecessary for this explicitly chosen model, and remains unproved for the actual layered response.

The draft's separate argument that island mass cannot pay because its gain is bounded is **incorrect**. IN1's creation bound contains \((2-\varepsilon_{\rm rar})P_{i_0}\), as well as \(\kappa_1|X|_{i_0}\); the first term grows with the creation coupling. Keeping one island fixed also does not send its later running-minimum radius to infinity. The valid distinction is structural: a stored-measure mass bound is not a factor multiplying the exponent coefficient \(f_W\). Using that mass here would require an additional formation/refiling identity. Theorem 3 uses none.

## External carriers and CI

**Outstanding — external-pair locality.** For example, \(F(P,\zeta)=\epsilon p_z\zeta_c\) remains dependent on a remote \(p_z\) after Boolean localization in \(\zeta\). Theorem 3 bounds this function but does not remove that read. The same issue applies to \(h_0(P)\), source completion, pins and stored variables.

The draft's **DR-locP** would require the response on a face-component \(K'\) of \(\operatorname{supp}s\) to depend on \(P\) only through \(N_{c_P}(K')\), with fixed early \(c_P\), on the whole switch/source domain. NL1-L H-DR states component reads at fixed \(P\); it does not prove DR-locP. Even with DR-locP, one must supply the corresponding locality of source completion and stored-source data, and functions on the entire declared local domains.

**Lemma 8 (what switched inversion supplies).** Suppose the following extra switched amplitude hypothesis, **A-sw**, holds:
\[
 F_f(P;s,\zeta)=\Phi_f(P,h(s;P,S(v_0+u(s\odot\zeta))))
\]
is holomorphic for \(s|_{X_f}=1\), \(|s_c|<e^{\bar\kappa}\), \(|\zeta|_c<R\), and
\(|F_f-f_0|\le\omega_f^{\rm sw}\), where \(f_0\) is independent of \(\zeta\). For \(V\subset\mathcal C\setminus X_f\), define
\[
 f_{W,V}=\sum_{A\subset V}(-1)^{|V\setminus A|}
                   D_WF_f(P;\mathbf1_{X_f\cup A},\zeta).       \tag{22}
\]
Then
\[
 f_W=\sum_Vf_{W,V},\qquad
 |f_{W,V}|\le2^{|W|}\omega_f^{\rm sw}D^{-|V|}.                \tag{23}
\]
Also \(f_{W,V}=0\) unless \(W\subset X_f\cup V\). If \(X_f\) includes every read stencil and R's component/source-locality clauses apply, every surviving component of \(X_f\cup V\) meets \(X_f\). This does **not** make the union connected when \(X_f\) is disconnected.

For the next bound require \(B_b\subset X_f\) for every read, \(\mathfrak b<R\), \(a\ge12\), \(\vartheta<1\), and A's deficit/oscillation bound with the same \(\widetilde\omega_f\) at every corner base \(h(\mathbf1_{X_f\cup A};P,S(v_0))\). Then
\[
 |f_{W,V}|\le(\widetilde\omega_f\omega_f^{\rm sw})^{1/2}
       (2\vartheta)^{|W|/2}(2/D)^{|V|/2}
       e^{-(a-6)m_{X(f)}(W)/2}.                              \tag{24}
\]

*Proof.* Finite Möbius inversion in the switches gives (23)'s identity. Express the corner difference as the integral of its mixed switch derivative over \([0,1]^V\). The \(W\)-difference has modulus at most \(2^{|W|}\omega_f^{\rm sw}\). Cauchy circles of radius increasing to \(D\) give its bound in (23). Masking kills each coordinate of \(W\) outside \(X_f\cup A\). A component missing all read stencils cannot affect a read; toggling one of its cubes cancels its alternating sum. First-neighbour source reads do not cross a missing corner-adjacency layer.

For (24), all \(B_b\subset X_f\) switches remain one. TD Lemma 2's expansion at a corner therefore retains just those coefficient sets contained in \(X_f\cup A\); its bound is unchanged. TD Lemma 4 applies about that corner base under the additional uniform amplitude hypothesis. Summing its bound over \(2^{|V|}\) corners gives \(2^{|V|}\widetilde\omega_f\vartheta^{|W|}e^{-(a-6)m_{X(f)}(W)}\). Its geometric mean with (23) proves (24). ∎

**Outstanding — correcting draft Proposition 8.1.** Its connectivity conclusion needs connected \(X_f\), which TD/X° did not assume. Already \(V=\varnothing\) and a product of two disjoint read variables give a nonzero disconnected example. Its corner proof also needs all read stencils fixed to one, as stated in Lemma 8. External locality further needs DR-locP and complete external/source/pin reads; global-fibre holomorphy does not supply a local-domain extension. The switch bound (23) and, with these extra premises, (24) are valid. They do not close the filing sums: a large hull has an unbounded number of possible boundary attachments at fixed per-cube cost.

**Outstanding — the proposed logarithmic-collar repair.** Put \(C=N_\rho(X_f)\), with the draft's \(\rho\) proportional to \(\log D_H\). Its proposed joint-composition bound JC uses
\[
 (C_*/D)^{|V|/2}e^{-(a-12)m_C(W\cup V)}.                     \tag{25}
\]
JC itself is unproved. Even granting it, the draft's summation replaces distance to \(C\) by distance to \(X_f\), which is invalid. A cube just outside \(C\) has distance one to \(C\), not \(\rho+1\).

The failure persists after the support cancellations in Lemma 8. For a cubical hub, choose a path \(V_0\) of \(n\) cubes from \(C\) to a gas cube \(W=\{w\}\). Choose \(N\) other cubes on one outer face of \(C\), with \(N\) of order \(D_H^3\). For every subset \(A\) of those cubes, \(V=V_0\cup A\) contains \(W\) and is attached to \(C\), while \(m_C(W\cup V)\le n+|A|\). Writing \(t=(C_*/D)^{1/2}>0\), the sum of the majorant (25) over these sets is at least
\[
 (te^{-(a-12)})^n(1+te^{-(a-12)})^N.                         \tag{26}
\]
Here \(n=O(\check R_i)\) and \(N\) grows cubically in \(\check R_i\). All rates are fixed before \(\gamma\). Thus (26) is unbounded; logarithmic enlargement does not create the claimed \(e^{-(a-12)\rho}\) factor. This refutes the proposed **majorant summation**, not convergence of the actual coefficients. A stronger joint estimate, matching the original reads, and a proved filing construction remain needed.

For the theorem below, **J°** means TD's actual Gaussian input J with every potential type ordinary and connected. Its numerical and algebraic requirements are: actual holomorphic Gaussian matrices and an early uniform envelope as in CI H-G/IN1 H-M; their finite-dimensional Gaussian domination, local dimension and tilt budget; normalized functionals; the exact finite Mayer/cutoff/interpolation formula; factorization on separated assigned supports; fixed integration/cutoff sets; and supplied reality, covariance and Borel dependence. The supports must admit Corollary 4's extra non-gas cubes. All these requirements concern the **assigned** functionals. A precision estimate or an auxiliary path-matrix envelope is not their identification. In the global-fibre version, J° makes no external-local-domain claim.

**Theorem 9 (B: ordinary-gas estimate and conditional CI closure).** Assume Theorem 3, J°, and the ordinary potential bounds TD (17) at rate \(\lambda_V\), with total ordinary amplitude \(a_{\rm base}\to0\). Those bounds may be supplied by CI H-D, H-C and H-W; actual complex identification and their complete hypotheses are retained. Use CI's constant choices with (13)–(14), counting all tagged types, and set
\[
 \mathfrak a=a_{\rm base}+2a_T^*(\gamma)+a_F+w\le a_*,\quad
 p_*=c_b(LM)^4e^{-\gamma_{\rm tilt}\mathfrak b^2/2},\quad
 \tau=e^{\Theta_{\rm CI}}(A_a\mathfrak a+p_*)\le\tfrac12.       \tag{27}
\]
Here \(a_T^*\) is the uniform envelope in Theorem 3; \(a_*,A_a,C_{\rm act},B_*,g_*\) are CI (12), (16)–(18)'s constants. Optional free/insertion types require CI H-F/H-O and their reserved budgets; otherwise \(a_F=w=0\). Put \(\mu=(1+4\beta_s)\kappa\), \(\Lambda=\mu+g_*\), and \(\ell_c(X)=\operatorname{St}_c(X)+5\).

Then the gas formed from the connected potentials has, on the supplied common fibre,
\[
 |H(Z;P)|\le C_{\rm act}(\mathfrak a+p_*)e^{-\Lambda\ell_c(Z)},\qquad
 |E_{\rm raw}(X;P)|\le C_{\rm act}B_*(\mathfrak a+p_*)e^{-\mu\ell_c(X)}.  \tag{28}
\]
The absolute cluster majorants converge locally normally. The functions are holomorphic, real and Borel on the supplied loci. On a contained polydisc of radii \(r_j\),
\[
 |\partial^\alpha E_{\rm raw}(X)|\le
 \alpha!r^{-\alpha}C_{\rm act}B_*(\mathfrak a+p_*)e^{-\mu\ell_c(X)}.      \tag{29}
\]
The finite gas equals \(\exp(\sum_XE_{\rm raw}(X;P))\).

For **CI in the existing class**, additionally assume the full filing input of TD Theorem 9: actual external-pair/stored-variable carriers and their entire chain domains; exact regrouping with summable multiplicities, restriction, overlap and covariance; and the class-length/amplitude bounds on the **filed** supports, including the usual scale/hull comparison. Also supply NL1-L Theorem 7's CI-base, CI-maps and remaining CI-form hypotheses at every formation time, and the actual local CI-Gauss/H-G/H-S package on every required fibre. Island creation and other stages need their separate formation bounds, including LF1's Size-isl/Loc-isl and the required dominated stored-variable integrals. Under these inputs, CI propagates through the finite history. None is proved by (28).

*Proof.* Corollary 4 supplies one connected ordinary type of norm at most \(2a_T^*\); the other norms are the stated inputs. Apply CI Lemmas 2–4 with \(\lambda=\lambda_V\), amplitude \(\mathfrak a\), and J°'s actual integration interface. These lemmas' Gaussian, collar, selection and tree estimates are uniform in the external parameter. Their numerical proof therefore works at a common global \(P\), without identifying \(P\) with a local pair \(P_X\). It gives (28), the incompatibility room and the absolute majorants. Cauchy's formula and the finite graph expansion, exactly as in CI Theorem 5, give (29), holomorphy and the exponential identity. J° supplies the preserved real/Borel identities. Theorem 3 and RUN make (27) a final coupling ceiling.

With the additional filing/domain input, the same functions or their supplied exact regrouping are activities on the required full local domains. CI's local theorem now applies with those actual carriers and bounds. Induct over formation time: CI-old supplies the already formed activities; the separately supplied maps admit each composition; the gas estimate supplies the regular logarithms; the remaining formation inputs supply the other outputs and their domination. This is NL1-L Theorem 7's induction, without using a new activity to bound itself. ∎

The ordinary length in (28) removes TD's specific problem of an uncontained remote island being used as a free contraction. On the **same support**, SA's relative length is at most the ordinary length after the supplied scale comparison. It does not follow that enlarging a raw support to its actual external carrier preserves its bound. Thus the draft's replacement of the full filing condition by its first two bullets is unjustified unless the third is independently supplied. Its claim that CI Theorem 5 already applies to local \(P_X\) before filing is corrected to the global-fibre statement (28).

## Source and definition record

SA, CA-I/II/III and YM3-I denote the pinned [outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex), [account I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex), [account II](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex), [account III](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_III.tex), and [YM3 manuscript](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM3/YM3_I.tex). Each was fetched once. The outline index README, relevant chunk rows and neighbours, obligations, and the CA admission index were consulted before bounded source reads. The following records every external passage directly quoted by the draft, and the decisive inherited CA comparisons. Index classifications are navigation aids, not evidence of correctness.

| Source lines read | Checked content and use |
|---|---|
| SA 5792–5804 (draft 5794–5797) | Splitting is a response hypothesis, with existence and uniqueness required. It does not construct our DR-locP. |
| SA 6185–6213 (draft 6191–6205) | Literal tree meeting requirements and R23 are as quoted. No zero-length hub contraction is defined. |
| SA 17315–17335 (draft 17317–17334) | Boxing, ten-cell evolution and rounded running-minimum radii are present; actual geometry remains imported. |
| SA 17573–17585 (draft 17575–17583) | Small quiet boxes and nonwrapping are conditional class geometry, not a proof of all later hub/read identifications. |
| SA 17903–17925 | The walk/bracket localization is sketched; it is not a proof of the multipoint composition or filing used here. |
| SA 19523 | Standing masses retain creation-level domains and bounds. This does not make the rarity exponent coupling-independent. |
| SA 14293–14318; 14406–14433 | UM1 and actual structural identities are hypotheses. UM7 has a covering-tree proof, also for disconnected terminal sets. |
| YM3-I 52578–52592 (draft 52582–52585) | Products of switches are attached to individual coefficient/string hulls. This supplies the credited device, not a four-dimensional response theorem. |
| CA-II 16013–16045; CA-III 3510–3528, 12278–12295 | The relative length is the length of a tree in the domain meeting unexcused cubes. A path between two such cubes still pays its intervening length. |
| CA-I 49495–49547; 54985–55008 | Application admission and drop-out spaces remain conditions; the preparatory theorem assumes its stage theorem. No new ST1-domain supply follows. |

The analytic/large-field methods are credited to Tadeusz Balaban as in these sources; the tree cost allocation used by TD is Bird's. No Dimock theorem is used as an additional unproved shortcut here.

The local checks used TD in full, CI in full, IN1 (2), H-M, its class bound, constant table, Lemma 3 and Amendment 1; TP1's running-minimum definition and Lemma 4.1; P82's stated real-reference scope; the ST1 statements identified above; NL1-L H-DR and Theorem 7; and PAN §§1.2, 4.3, 8.3, 9 and F3–F4. The relevant `nl1-L-gate`, `st1-gate`, `in1-gate`, `carrier-check`, `kept-cov-check` and `r-inv-check` clauses preserve actual-domain, assigned-series and covariance qualifications. None proves the new X° or filing inputs. In particular, `carrier-check` supplies an envelope for its specified replacement series, not heredity for every assigned Gaussian.

Definitions supplied or sharpened in this distillation are: (i) the fine-cube sets, fixed source set, separate lengths \(d_f^{\rm old},\operatorname{St}\), and constants \(C_{\rm isl},C_0^{\rm rad},C_0^{\rm UM}\); (ii) the graph collar \(N_c\), ratio \(\eta\), ordinary tree X° and its relation to the retained contracted premise; (iii) the uniform tail amplitude \(a_T^*(\gamma)\), window conversion and explicit rate choices; (iv) the connected regrouping and its support/symmetry limitations; (v) the mixed difference, carrier entropy rate \(\alpha_e\), X-num and scalar-current countermodels, distinguished from actual physical identification; (vi) A-sw, complete pinned stencils and the corrected component claim in switched inversion; (vii) J°, the global raw logarithm, and the full local filing/formation condition. The other notation is the binding TD/CI notation restated above.

## Result

Theorem 3 proves **ordinary-distance TD**, with complex-polydisc control and a uniform amplitude tending to zero, conditional on TD's R, A, X, G, RUN and complete admission inputs, plus X° and G-ord. The ten-cell payment and the \(\bar\kappa\) floor (14) hold by the written geometric and exponent estimates. Theorem 9 proves ordinary raw-gas convergence under J° and the ordinary potential inputs; **existing-class CI remains conditional on the full actual filing/domain and remaining formation packages**. The complex island deficit, actual response, amplitude sums, hub/projection geometry and actual Gaussian identification remain imports. DR-locP, switched admission, joint composition and a summable local filing are not established here.

Corrections made, including the draft's proposed changes to other notes:

1. **TD (8)/X°:** the ordinary tree is a valid sufficient additional premise, not a consequence of the contracted inequality. Nor does a fixed-width collared-hub statement alone imply (8). Keep the source projection/containment obligation and the original imports explicit.
2. **TD Theorem 10/CI row 5:** the suspected name clash is confirmed by IN1 (2), row 6 and c4-order row 16. Move only the geometric island constant early; keep the radius coefficient late and distinguish the Gaussian budget. The draft's illustrative fixed-point claim for every \(L\ge2\) is false: its map \(n\mapsto\lceil n/L\rceil+20\) has fixed point 40 at \(L=2\); 21 is fixed for the allowed \(L\ge27\). This illustration is not a proof of G-ord.
3. **Theorem A/IN1 Amendment 1:** preserve the valid gap payment and exact floor, make the entire window and \(\kappa\)-floor explicit, retain the binding IN1 floors, and state the uniform supremum limit. The natural-gas estimates are not used by the ordinary proof; that does not authorize deleting frozen floors.
4. **C3 payment:** withdraw the bounded-mass-versus-growing-length argument. The creation rarity exponent was omitted. The missing transfer from stored mass to exponent coefficients is the relevant limitation.
5. **Proposition 6/TDd Proposition 7.1:** the radius-ratio repair is right for the contracted numerical premise. Use a current-only response, ensure no torus shortcut, and use mixed differences to address every local decomposition, with an entropy bound for enlarged carriers. The literal SA boundary length and actual-response identification remain outside this countermodel; no claimed SA correction is restored.
6. **Proposition 7:** replace the unverified metric monotonicity by an explicitly chosen uniform-layer countermodel. It shows failure with an uncontrolled late island size, not necessity of these exact hypotheses for every possible proof or failure of the actual response.
7. **Corollary A′:** retain the factor two in the connected gas amplitude. Extra non-gas cubes, covariance and hereditary carrier choices require their actual interface.
8. **Theorem B/TD Result/CI:** ordinary decay removes the specific contracted-length obstruction only. It does not supply local \(P_X\) functions or pay enlargement to actual external carriers. Keep all three filing clauses and every other CI formation import.
9. **Proposition 8.1:** correct disconnected-base cancellation, require complete fixed stencils and uniform corner amplitudes, and separate source/external locality from fluctuation locality. The valid finite estimates are (23)–(24).
10. **JC summation:** withdraw the claimed closure even conditional on the displayed JC estimate. Collapsing the logarithmic collar loses the collar-width decay; (26) shows the resulting boundary-attachment majorant is unbounded. This is not a divergence proof for the actual expansion.

This is a proof of a conditional step sketched by the source route, and a correction/distillation of our draft. No frozen note, gate, ledger or editable prompt file was changed. Only `library/td2.md` was written in the repository. Source retrieval and identity checks discharge no mathematics. **The text is not yet refereed.**
