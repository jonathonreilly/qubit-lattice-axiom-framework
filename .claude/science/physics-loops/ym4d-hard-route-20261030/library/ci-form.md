# CI-form: formation estimates at complex input pairs

Provenance: Pass 2 distillation of Claude's `ci-form-draft.md`, at repository commit `591c6f44a61d50ff86b57f9e78f6c5f6dd281d37`; prepared by Codex. Source material from Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, is attributed where used. Research text, not an audit; no scientific status is granted.

The main result below is conditional complex-input formation for the regular gas. It does not close CI. The operative inputs are the distilled [IN1](in1.md), [PR-lay](pr-lay.md), [NL1-L](nl1-L.md) and [ST1 round 3](st1-r3.md), rather than the earlier drafts cited by pass 1. All arguments are hand proofs. Source retrieval and file bookkeeping discharge no mathematical obligation.

## Definitions

Fix a finite four-dimensional periodic lattice, a finite history and a main step of level \(i\). Fine cubes have side \(M\); coarse cubes have side \(LM\). Both grids tile the torus. Assign each free bond to exactly one fine cube, with a fixed boundary convention. Write \(I\) for the free bonds and \(B\in(\mathbb R^3)^I\). The block norm is Euclidean; all coordinate-to-matrix conversions are included in the constants below. Put
\[
 \ell=\log\theta_{i-1},\quad g=\theta_{i-1}^{-1/2},\quad
 R=\ell^q,\quad \mathfrak b=C_{\rm win}A_1\ell^{p_0}<R,
 \qquad \theta_j\ge\gamma^{-2}>1,\quad p_0>0,\quad r\ge2,\quad q>p_0+2r.
 \tag{1}
\]
The fixed \(C_{\rm win}\ge1\) covers the actual window convention. The complex fluctuation polydisc uses scalar coordinates, \(\mathbb D_R=\{\max_{b,a}|\zeta_{b,a}|<R\}\). A real bond ball of radius \(\mathfrak b\) lies in its corresponding coordinate box. All radii, rates and fixed multiplicative constants below are positive; amplitudes and perturbation bounds may vanish. The imported \(\beta_s\) is nonnegative.

A **carrier** is a nonempty set of fine cubes containing every fluctuation, stencil, pin and stored-slot read assigned to a term. Connectivity uses face, edge or corner adjacency. Let \(d_f(Y)\) be the minimum number of edges of a tree in this graph meeting all cubes of \(Y\), allowing additional vertices. For connected \(Y\), \(d_f(Y)=|Y|-1\). Define \(d_c\) likewise on coarse cubes and \(\ell_c(Z)=d_c(Z)+5\). Fixed conversions to the source's tree-length convention belong in the geometric constants and rate window. A collar \(Y^\sharp\) is the coarse-cube union meeting a fixed fine neighbourhood of \(Y\); it is not its rectangular hull. Incompatibility means overlap or the assigned wall adjacency, including self-incompatibility. Assume wall adjacency has joining length at most five in the coarse graph; all geometric constants include this fixed convention.

For a connected carrier \(X\), write
\[
 \mathbb S_X=\{s:s|_X=1,\ |s_\Delta|<e^{\bar\kappa}\},
 \qquad K_X(s)=\text{component of }\operatorname{supp}s\text{ containing }X.
 \tag{2}
\]
These are **fine** switches. The independent **coarse** Gaussian parameters are denoted \(t\). Neither changes a sharp integration cutoff.

An input is \(P=(U,A',\mathbf J')\), with \(U\) real and fixed on each analytic fibre; \(\mathbf J'\) is independent of the complex field. Let \(\mathcal O_\sigma(Q;U)\) denote the prescribed open ST1 chain domain on a carrier \(Q\), with Tq0, the permanent ledger, R1 cores, frozen tower functions, all witness carriers and absolute ceilings. Its restriction maps, overlap identifications and Borel real/stored parameters are part of the supplied domain data. Suprema below range over **every point of each declared local domain**, not just restrictions of one global field. Initial and unfinished entries retain their own radius indices. No intersection with a new pointwise envelope is silently substituted for this domain.

The seven exponent kinds are W (Wilson, Jacobian and profile remainders), S (strip), Z (elimination logarithms), E/R (regular/remainder terms), B (boundary), K (kept forms) and I (standing islands). Write \(f_0(P)=F_f(P;\mathbf1,0)\) for each term's zero-fluctuation value. A term is **exempt** if its carrier meets the live large-field region or its boundary-hull definition exempts an island. The remaining terms are called **class terms**. This partition supplies no size estimate.

## Imports and outstanding hypotheses

Each hypothesis below is required uniformly in level, history, cutoff, volume and all declared local input domains. Late constants may depend on earlier choices. These H-labels are local to this note; IN1's packages are explicitly qualified when used. The named owners retain the obligations indicated here.

**H-D (full-domain supply).** NL1-L Theorem 4's H-ST, H-FL, H-DR, H-ACT and radius/source budgets hold on these entire fibres, with old activities already supplied there. The centred substitutions represent the actual exponent at complex independent-current pairs. The required real ties, gauge covariance, near/far stored-variable rules and restriction/overlap identities hold. For the precision, assume PR-lay's R, W, G, B, Q and D; use its optional F only for the completed gauge form. D is its current-layer envelope (19), on every required bond and stencil, with the actual initial/boundary/top radius assignments.

**Outstanding — domain and identification.** Record retention and equality of radius tables do not prove H-D. PR-lay Theorem 8 is conditional on D. NL1-L Theorem 4 identifies its constructed family with the actual formation formula only under the additional complex-pair identification. Agreement on real critical pairs does not determine independent-current dependence.

**H-G (actual local Gaussian family).** For every selected support and every coarse polydisc \(|t_\Delta|<R_s=e^{\bar\kappa}\), supply the actual jointly holomorphic symmetric \(C\), rectangular \(\Gamma\), real at real parameters, and real references \(C_*>0,\Gamma_*\), with
\[
 \|C_*\|+\|C_*^{-1}\|+\|\Gamma_*\|\le K,\qquad
 \|C-C_*\|+\|\Gamma-\Gamma_*\|\le\varepsilon.
 \tag{3}
\]
The scalar local dimension is \(m\le c_m(LM)^4|Z|\). In dimension zero the functional is evaluation at the empty vector. Otherwise it is SA FG4, equivalently integration on the **fixed real space** against the normalized covariance \(D=C+C\Gamma\Gamma^{\mathsf T}C\). Import SA FG1–FG11's comparison, with constants \(A_K,\varepsilon_0(K),\rho_0(K)\), independent of the auxiliary dimension. Require frozen IN1 H-M's early envelope
\[
 \varepsilon\le H_0e^{b_G\bar\kappa-d_GM}+\Delta_\gamma,
 \quad \sup_{\theta\ge\gamma^{-2}}\Delta_\gamma\longrightarrow0
 \quad(M,\bar\kappa\text{ fixed}),                              \tag{4}
\]
where the last term includes the actual complex-pair perturbation and coefficient-ratio error. All reference bounds, \(H_0,b_G,d_G\), and coefficient-ratio constants precede \(\kappa\).

**H-S (structural formation).** The assigned Gaussian and potential carriers are hereditary, normalized and wall-factorizing, with the actual finite Mayer/cutoff/decoupling identity. Regions, reference integration measures and cutoff sets are fixed while analytic parameters vary. Physical identification is required only on the complete physical locus. All data are jointly Borel in real and near stored variables; their specified real/gauge/tie/overlap identities are compatible with integration.

**Outstanding — H-G/H-S.** PR-lay supplies a precision estimate under H-D, not these whole interfaces. IN1 Lemma 2 proves an auxiliary path-matrix bound under a global gap; its explicit counterexample separates that bound from heredity. Its discussion also retains the distinction from the locally gapped mutilated matrix. Do not substitute that construction for H-M without identification. SA 14406–14412 makes the structural identities separate hypotheses.

**H-C (class oscillations and carrier sum).** For every non-W class term there is a connected complete carrier \(X_f\) and a jointly holomorphic presentation \(F_f(P;s,\zeta)\), real at real data, with \(F_f(P;s,0)=f_0(P)\), exact component locality as in NL1-L Theorem 4(2), and
\[
 |F_f-f_0|\le\omega_f\quad\text{on }\mathbb S_{X_f}\times\mathbb D_R,
 \qquad
 \sup_\Delta\sum_{f:X_f\ni\Delta}\omega_f e^{\alpha|X_f|}
       \le N_C<\infty,\quad \alpha=\kappa/2.                  \tag{5}
\]
The sum is over complete carriers, and \(N_C\) is fixed before \(\gamma\). These are PAN's L-S/L-Z/L-reg/L-B inputs in the **oscillation form actually needed here**.

**Outstanding — H-C.** A forgetting-weighted numerical list norm cannot replace \(2b_f\) in Schwarz's lemma unless it bounds this same holomorphic difference on the whole switched polydisc. OSF3 includes a separate renormalization/formation assertion. Even a bound \(e^{-\kappa d_f(X)}\) would not alone give the draft's sum weighted by \(e^{\kappa|X|}\): the majorant for one path of each length already has constant summands. Applying R23's exempt-metric bound to \(d_f\) also needs the actual metric comparison. The half-rate weight in (5) leaves entropy room. If at most \(J_B\) boundary terms have each connected complete carrier and each has oscillation \(\le2\mathsf B e^{-\kappa d_f(X)}\), their contribution is at most \(2J_B\mathsf B e^{\kappa/2}S_{\kappa/2}\). Actual carrier multiplicities and any change of carrier remain inputs.

**H-W (actual local remainder decomposition).** Supply NL1-L Lemma 3 at every complex input: \(F_f(P;B)=\phi_f(P;w_f(B))\), an affine read of range \(R_W\), with
\[
 \|w_f(\zeta)\|\le\delta_0+c_Tg|\zeta|_\infty,\quad
 \delta_0=C_{\rm st}A_1g\ell^{p_0},\quad
 |\phi_f|\le B_f\text{ on }\|w\|<c_W,
 \quad \partial_w^j\phi_f(P;0)=0\ (0\le j<k_f),\quad k_f\in\mathbb N_{>0}.
 \tag{6}
\]
Assume each complete W carrier lies in a cube of diameter at most \(2R_W+2\), \(M>2R_W+2\), \(\delta_0+c_TgR<c_W/2\), and at most \(C_WM^4\) summands with any one carrier, including all W subtypes. Set
\[
 a_W=2C_WM^4e^{15\lambda}
       \max_f B_f[(\delta_0+c_Tg\mathfrak b)/c_W]^{k_f}.
 \tag{7}
\]
Require \(\sup_{\theta\ge\gamma^{-2}}a_W\to0\). The four supplied pairs \((B_f,k_f)\) listed in NL1-L Lemma 3 give this via a constant times \(g\ell^{3q+r}\). Their constants may follow \(M\).

**Outstanding — H-W.** CA-II 79920–80013 displays Bałaban's exponent and attributes its derivation to him. It does not prove (6), finite range of the coupling-profile background dependence, or those vanishing orders at independent currents.

**TD (exempt formation; Outstanding).** The actual exempt exponent difference must have an exact local decomposition into nonempty fine carriers,
\[
 \sum_{f\ {\rm exempt}}[F_f(P;\mathbf1,B)-f_0(P)]
     =\sum_{W\ne\varnothing}V^{\rm ex}(W;P,B),\qquad
 |V^{\rm ex}(W;P,B)|\le a_Ee^{-\lambda_Td_f(W)},\quad\lambda_T\ge\lambda,
 \tag{8}
\]
on its real boxes, jointly holomorphic on the declared complex boxes/cores, with the same structural interface and \(\sup_{\theta\ge\gamma^{-2}}a_E\to0\). If no exempt term occurs, take \(a_E=0\). Lemma 6 below separates exact algebraic localization from this unproved bound.

**H-O (ordinary parameters; optional).** The source box is SA 4880–4893, including its boundary and stored-exponent coordinates. H-D, H-G, H-S, H-C, H-W, TD and H-F must hold jointly and uniformly where applicable on this box, with fixed integration sets and a fixed finite number of combined potential types. OSF3–OSF5 and actual domain inclusions are needed to identify the claimed regular input constants. An optional SC1 insertion is a further local potential type satisfying (25), with norm \(w\le a_*/2\) and the H-S interface; its actual formation estimate is an additional hypothesis. Put \(w=0\) when no insertion is used.

**H-F (additional free potentials; optional).** If the actual formula requires globally defined free potentials, supply their joint holomorphy, H-S interface and (25) with total norm \(a_F\), uniformly tending to zero as \(\gamma\downarrow0\). Otherwise set \(a_F=0\).

**Definition (the formed gas).** Combine the class, W, exempt, free and insertion potentials into the fixed finite number of types. A tag records the type. Their total UM1 norm is at most \(a\) in (18). For selected tagged domains \(\mathcal D\), let \(Y_0\) be their box-required free bonds and let \(P_0\subset I\setminus Y_0\) consist of distinct failed bonds. Put
\[
 F_{\mathcal D,P_0}=(-1)^{|P_0|}\chi_{Y_0}
       \prod_{b\in P_0}(1-\chi_b)\prod_{Y\in\mathcal D}(e^{V(Y)}-1),
 \quad \chi_b=\mathbf1_{\{|B(b)|<\mathfrak b\}}.
 \tag{9}
\]
Here \(\chi_{Y_0}=\prod_{b\in Y_0}\chi_b\); the integrand is zero off its required boxes. \(Z_0\) is the union of the selected complete carriers and the cubes owning failed bonds, with any fixed enlargements included in the collar convention. For nonempty wall-connected \(Z\supset Z_0^\sharp\), define
\[
 T(Z,\mathcal D,P_0)=\int_{[0,1]^{Z\setminus Z_0^\sharp}}
       \partial_{t_{Z\setminus Z_0^\sharp}}
       \mathcal J_{C(t_Z),\Gamma(t_Z)}[F_{\mathcal D,P_0}]\,dt,
 \qquad H(Z)=\sum_{(\mathcal D,P_0)\ne(\varnothing,\varnothing)}T.
 \tag{10}
\]
Here \(t_Z=1\) on the collar and zero off \(Z\). Sum only selections assigned to \(Z\) by H-S. For a list, let \(\phi(Z_1,\ldots,Z_n)\) be the alternating sum over connected spanning subgraphs of its incompatibility graph; \(\phi(Z)=1\). Repetitions are allowed. The union-filed logarithm is
\[
 E(X;P_X)=\sum_{n\ge1}\frac1{n!}\sum_{\cup_jZ_j=X}
       \phi(Z_1,\ldots,Z_n)\prod_j H(Z_j;P_X|_{Z_j}).       \tag{11}
\]
H-S specifies each restriction; actual fields outside \(X\) are never introduced.
For a finite coarse region \(Q\) and \(P_Q\) in its declared local domain, define
\[
 \mathcal Z_Q(P_Q)=
 \sum_{\substack{\mathcal A\text{ mutually compatible}\\ Z\in\mathcal A\Rightarrow Z\subset Q}}
       \prod_{Z\in\mathcal A}H(Z;P_Q|_Z),
\]
including the empty collection with product one.

## Constant order

Use frozen IN1's complete order, retaining the internal dependencies of c4-order. The following are the additional choices used here; \(a\) below is a **potential amplitude**, not a precision gap.

1. Fix margins, reserve requests, exponent requirements and the finite type count. Fix \(q>p_0+2r\), with every stronger imported exponent inequality, and \(c_R=1\). Fix the stencil range \(R_W\), window/enlargement ratios, geometric constants of Lemma 3, \(\lambda_0,\sigma_0>\kappa_f\), \(\varepsilon_{\rm rate}\ge1\), and a gap \(g_*>\kappa_D+C_v\) so that
   \[
   B_*:=\frac{C_De^{2C_v-5g_*}}{1-e^{-(g_*-\kappa_D-C_v)}}
       \le c_{\rm adj}^{-1}.                                   \tag{12}
   \]
   Choose odd \(L\ge27\) above IN1's rate-window floor \(4C_h^{\rm WF}C_hc_\ell(1+4\beta_s)\), enlarging \(C_h^{\rm WF}\ge1\) before this choice. Fix flat/averaging and one-loop constants and the weak frame triple. Then, in IN1 rows 3–4: local gauges/inverses and reference ceilings; propagator/profile/walk rates; \(M_1\), then \(R_1\), then their gap; seam, A2/A3 and tower bounds/radii. The local walk size \(M_1\) is not \(M\).
2. Before \(\kappa\), obtain H-G's \(K,H_0,b_G,d_G\), and the Gaussian constants. With \(K\ge1\), set
   \[
   B_K=K+K^4,\quad c_K=B_K^{-1},\quad
   \varepsilon_0\leftarrow\min\{\varepsilon_0,1,[20K^2(K+1)^3B_K]^{-1}\},
   \quad \rho_0\leftarrow\min\{\rho_0,c_K/8\}.
   \tag{13}
   \]
   Enlarge \(A=A_K,P_d,c_m\ge1\), where \(P_d\) bounds the two potential-density constants of Lemma 3. Set
   \[
   W_0=\min\{[3P_dL^4(1+Ac_m)]^{-1},\rho_0/(2P_d)\},\qquad D_0=Ac_mL^4.
   \tag{14}
   \]
3. Choose \(\kappa\) large, put \(\alpha=\kappa/2\), \(\mu=(1+4\beta_s)\kappa\), \(\Lambda=\mu+g_*\), \(K_*=2+c_\ell\Lambda\), \(\Theta=C_h(1+K_*)\). Choose \(\lambda\) in
   \[
    \lambda_0+\sigma_0+\Theta/L\le\lambda
      <\kappa/(2C_h^{\rm WF})-\varepsilon_{\rm rate},
    \qquad\varepsilon_{\rm rate}\ge1.
    \tag{15}
   \]
   Thus \(\lambda+1\le\alpha\). The \(L\) floor makes this window nonempty for sufficiently large \(\kappa\). Set
   \[
   A_a=2c_fL^4S_{\sigma_0}/W_0,\quad
   a_*=\min\{W_0/2,(4e^\Theta A_a)^{-1}\},\quad
   C_{\rm act}=e^\Theta\max(A_a,1).
   \tag{16}
   \]
4. Choose \(\bar\kappa,\kappa_1\), with all imported floors and
   \(\bar\kappa\ge\lambda+2, \log(e^{\bar\kappa}-1)\ge\Theta\).
   Choose response-parameter length and small decoupled radii, \(M'_1\), then \(M_2\), preparation/profile constants, \(\Theta_1,\varpi_T\); then \(M\), a power of \(L\), above all collar, source and W floors and so that
   \[
    H_0e^{b_G\bar\kappa-d_GM}\le\varepsilon_*/2,
    \quad\varepsilon_*:=\min\{\varepsilon_0,(3D_0M^4)^{-1}\},
    \quad\gamma_{\rm tilt}:=\min\{2/(3D_0M^4),\rho_0\}.
    \tag{17}
   \]
5. Choose post-\(M\) box, joint-chart, comparison and cutoff constants; \(A_1\), then \(A_0\); \(C_0\), then \(C_1\); absolute/current radii, response room and age constants. Next choose the normalizer and regular amplitudes before the weighted-list bound; the boundary-origin bound before volume costs. Follow IN1 rows 7–8 for certificates, genealogy, envelopes, entropy, reserve, prepared-form, label/floor, flow and tube constants. Fix \(N_C,C_W,C_{\rm st},c_T,c_W\), the actual W amplitudes, and island constants at their allowed late positions. None selects \(R_W\) or an earlier rate. Finally take \(X_0\) large and set \(\gamma=X_0^{-1/2}\) for H-D and all imported ceilings, (1), (6), \(\Delta_\gamma\le\varepsilon_*/2\), and uniformly for \(\theta\ge\gamma^{-2}\),
   \[
    a:=(\mathfrak b/R)N_C+a_W+a_E+a_F+w\le a_*,\quad
    p_*:=n_b e^{-\gamma_{\rm tilt}\mathfrak b^2/2}\le(4e^\Theta)^{-1},
    \quad n_b=c_b(LM)^4.
    \tag{18}
   \]
   For a reserved insertion slot require the base amplitude \(\le a_*/2\) and \(w\le a_*/2\). All late \(b_f\) are read only by output bounds and subsequent late ceilings, never by an earlier choice. Returned flow errors follow \(\gamma\); any stronger source ceilings restrict the allowed coupling without redefining earlier constants. Run data and frame choices come last, and each new coefficient is formed before its next frame entry.

**Lemma 1 (class and W potentials).** Under H-C/H-W and this order, the corresponding exponent difference has exact local potentials on the real boxes, holomorphic on their declared complex boxes, with
\[
 |V^C(Y;P,B)|\le (\mathfrak b/R)N_Ce^{-\lambda d_f(Y)},
 \qquad |V^W(Y;P,B)|\le a_We^{-\lambda d_f(Y)}.             \tag{19}
\]
Both have the supplied reality and external-variable interface.

*Proof.* For a fixed direction \(u\), \(\|u\|_\infty=1\), divide \(F_f(P;s,zu)-f_0(P)\) by \(z\). The singularity at zero is removable. The maximum principle on \(|z|=R'<R\), followed by \(R'\uparrow R\), gives

\[
 \sup_{|\zeta|_\infty\le r,s}|F_f-f_0|\le\omega_f r/R.
 \tag{20}
\]

For \(Y\supset X_f\), set switches to zero off \(Y\), to one on \(X_f\), and to \(s\in[0,1]^{Y\setminus X_f}\) elsewhere. Define \(f_Y\) by integrating the mixed switch derivative of \(F_f-f_0\); for \(Y=X_f\), take its value with those switches. Repeated fundamental theorems of calculus give
\[
 \sum_{Y\supset X_f}f_Y=F_f(P;\mathbf1,B)-f_0(P),\qquad
 |f_Y|\le\omega_f(\mathfrak b/R)
                      (e^{\bar\kappa}-1)^{-|Y\setminus X_f|}.
 \tag{21}
\]
For the inequality, take one Cauchy circle of radius \(r'<e^{\bar\kappa}-1\) about each real switch and let \(r'\uparrow e^{\bar\kappa}-1\). Distinct first derivatives introduce no factorial. Component locality makes the integrand independent of a switch in any component missing \(X_f\); thus disconnected \(Y\) gives zero. It reads \(B\) only on \(Y\); if \(Y\) has no free bond, (20) makes its difference zero. Finite integration on a compact real cube preserves holomorphy by integrating Cauchy's formula; it also preserves reality.

Sum (21) over \(f\) with \(X_f\subset Y\). For connected \(Y\), \(d_f(Y)=|Y|-1\); also \(\bar\kappa\ge\lambda+2\) gives \(\log(e^{\bar\kappa}-1)\ge\lambda+1\). Thus
\[
 e^{\lambda d_f(Y)}|V^C(Y)|
 \le(\mathfrak b/R)e^{-|Y|}
       \sum_{X_f\subset Y}\omega_fe^{(\lambda+1)|X_f|}
 \le(\mathfrak b/R)|Y|e^{-|Y|}N_C
 \le(\mathfrak b/R)N_C.
\]
The middle bound charges each term to one of its carrier cubes and uses (5). Carriers remain \(Y\), including any non-gas cubes used for localization; deleting those cubes and summing again would require another estimate.

For W, division of \(\phi_f(P;zu)\) by \(z^{k_f}\) gives \(|\phi_f(P;w)|\le B_f(\|w\|/c_W)^{k_f}\). Apply this at \(w_f(B)\) and \(w_f(0)\). Their carrier meets at most two fine cubes in each direction, hence at most sixteen; its tree length is at most fifteen. The multiplicity bound in H-W and (7) prove (19). No locality of a background composition is inferred from locality of the pivot map. \(\square\)

**Lemma 2 (local Gaussian domination and budget).** Under H-G and (13)–(17), local integrals of jointly Borel functions, holomorphic in the analytic parameters and satisfying \(|F(P;b)|\le F_0e^{\rho|b|^2}\), \(0\le\rho\le\rho_0\), are holomorphic in the fixed-\(U\) fibre and coarse parameters. The Gaussian comparison gives cost \(e^{A(\varepsilon+\rho)m}\). For the potential and cutoff tilts of Lemma 4, its coarse-cube budget satisfies \(C_0^{\rm UM}\le1\).

*Proof.* For \(D_*=C_*+C_*\Gamma_*\Gamma_*^{\mathsf T}C_*\),
\[
 D_*\ge K^{-1}I,\quad \|D_*\|\le K+K^4=B_K,\quad
 \|D-D_*\|\le5(K+1)^3\varepsilon.
\]
The last bound follows by telescoping the four-factor product once in each factor, together with \(C-C_*\). Transposition preserves the Euclidean operator norm. Equation (13) and the inverse identity yield
\[
 \|D^{-1}\|\le2K,\qquad
 \|D^{-1}-D_*^{-1}\|\le2K^2\|D-D_*\|\le c_K/2.
\]
Consequently \(\operatorname{Re}(b^{\mathsf T}D^{-1}b)\ge(c_K/2)|b|^2\) for real \(b\). The determinant root is the analytic continuation in this small matrix ball from its positive reference value. On any compact parameter set its modulus is bounded. The product of the density with \(F\) is therefore dominated by a constant times \(e^{-c_K|b|^2/8}\). Integrating Cauchy's formula, justified by this integrable bound, proves joint holomorphy. The cutoffs stay real and fixed. The normalized identity and dimension-only comparison are precisely the imported FG6 theorem, whose proof extends through FG11 at SA 14089.

The potential-density bound uses \(\rho=P_dW_0M^{-4}+\gamma_{\rm tilt}/2\le\rho_0\). With \(m\le c_m(LM)^4N\),
\[
 C_0^{\rm UM}
 =P_dL^4W_0(1+Ac_m)+D_0M^4(\varepsilon+\gamma_{\rm tilt}/2)
 \le\tfrac13+\tfrac13+\tfrac13=1.
 \tag{22}
\]
Every shrinkage in (13) depends only on the early \(K\), so it preserves IN1's order. \(\square\)

**Lemma 3 (geometric sums).** There are geometric constants, independent of \(M,L\ge2\), volume and history, such that
\[
\begin{gathered}
 |Y^\sharp|\le C_h(1+d_f(Y)/L),\quad
 N\le C_h\{r+L^{-1}\sum_{Y\in\mathcal D}d_f(Y)+v+h\},\\
 S_\xi:=\sup_q\sum_{\text{tagged }Y\ni q}e^{-\xi d_f(Y)}<\infty
       \quad(\xi>\kappa_f),\quad
 \sum_{Y:Y^\sharp\subset Z}e^{-\xi d_f(Y)}\le c_fL^4S_\xi N.
\end{gathered}
 \tag{23}
\]
Here \(r=|\mathcal D|\), \(v=|P_0|\), \(h=|Z\setminus Z_0^\sharp|\), \(N=|Z|\). At most \(n_bN\) failed bonds have collars in \(Z\). Also \(\ell_c(Z)\le c_\ell N\), \(N\le C_v(d_c(Z)+1)\), and the number of coarse polymers through a fixed cube with \(m\le d_c(Z)<m+1\) is at most \(C_De^{\kappa_Dm}\). Incompatible polymers contain a cube among at most \(c_{\rm adj}N\) neighbours of \(Z\). For a connected incompatibility list,
\[
 \ell_c(\cup_jZ_j)\le\sum_j\ell_c(Z_j).                    \tag{24}
\]

*Proof.* Double a covering tree. Cutting its walk into pieces of length at most \(L\) gives at most \(C(1+d_f(Y)/L)\) pieces. Each piece and its fixed fine collar meet a bounded number of coarse cubes. Union preservation gives the second bound, adding the fixed collar of each failed bond and the \(h\) extra cubes. On the fine graph, of degree at most (80), a rooted tree of length \(n\) has a traversal of \(2n\) steps. Encode the subset \(Y\) among the visited vertices by binary flags. At most \(80^{2n}2^{2n+1}\) codes suffice; the fixed type count multiplies this by a constant. Summing this geometric bound proves \(S_\xi<\infty\) above a fixed entropy rate. Charging each domain to a cube in \(Z\) gives its \(c_fL^4N\) factor. Cube volume bounds the bond count. The same traversal count proves the coarse entropy and size estimates. Wall adjacency has bounded degree. Joining covering trees along an incompatibility spanning tree costs at most five per join; adding five to each length gives (24). The arguments use the periodic graph directly, so no volume factor enters. \(\square\)

**Lemma 4 (activity and absolute cluster bounds).** Suppose (3)–(4), H-S and the choices (12)–(18) hold. Suppose every potential type satisfies
\[
 |V(Y;P,B)|\le a_Ye^{-\lambda d_f(Y)}
       (1+M^{-4}\sum_{b\in Y}|B(b)|^2),\qquad
 \sum_{\rm types}\sup_Y a_Y\le a,                         \tag{25}
\]
on its required real box, or everywhere on the real space for a free type. Assume the declared holomorphy. Set \(p=e^{-\gamma_{\rm tilt}\mathfrak b^2/2}\) and \(\tau=e^\Theta(A_aa+p_*)\le1/2\). This \(\tau\) is an activity budget, distinct from IN1's coefficient-ratio error. Then
\[
\begin{split}
 |T|&\le e^N(2a/W_0)^r e^{-(\lambda-\lambda_0)\sum_Yd_f(Y)}
                         p^v(R_s-1)^{-h},\\
 \sum_{\mathcal D,P_0}|T(Z,\mathcal D,P_0)|
       &\le\tau e^{-\Lambda\ell_c(Z)},\\
 \sum_{Z'\not\sim Z}\widehat w_{Z'}e^{|Z'|}&\le |Z|/2,\\
 e^{\mu\ell_c(X)}\sum_{n\ge1}\frac1{n!}
       \sum_{\cup Z_j=X}|\phi(Z_1,\ldots,Z_n)|
                           \prod_j|H(Z_j;P_X|_{Z_j})|
       &\le\tau B_*\le C_{\rm act} B_*(a+p_*).
\end{split}
 \tag{26}
\]
Here \(\widehat w_Z=e^{\mu\ell_c(Z)}\sup_{P_Z}|H(Z;P_Z)|\), using the entire local core. Bounds also hold on every hereditary subsystem.

*Proof.* If \(a>0\), give each selected potential a coupling \(z_Y\) with radius

\[
 \mathcal R_Y=(W_0/a)e^{(\lambda-\lambda_0)d_f(Y)}\ge2.
\]

Equation (23), first for the constant term and then rooted at each bond for the quadratic term, gives
\[
 \sum_{Y\in\mathcal D}|z_YV(Y)|
       \le P_dW_0L^4N+P_dW_0M^{-4}|B|^2.
\]
The Mayer product is at most \(2^r\) times the exponential of this sum. Distinct failed blocks give
\[
 \prod_{b\in P_0}(1-\chi_b)
 \le p^v\exp\{(\gamma_{\rm tilt}/2)\sum_{b\in P_0}|B(b)|^2\}.
\]
Lemma 2 therefore bounds the enlarged-coupling integral by \(2^re^Np^v\), uniformly on the coarse polydisc. The integral vanishes when any \(z_Y=0\). Divide successively by these variables, using their removable zeros and the maximum principle on smaller polycircles. At \(z_Y=1\) this contributes \(\prod_Y\mathcal R_Y^{-1}\), without a factorial. Cauchy circles about the real \(t\in[0,1]\), with radii tending to \(R_s-1\), contribute \((R_s-1)^{-h}\). Lemma 2 justifies all analytic differentiations under the fixed real integral. This proves the first line. If \(a=0\), nonempty Mayer selections vanish and the same argument applies to cutoff-only selections with \(r=0\).

By (23), the factor \(e^{(1+K_*)N}\) is paid by \(\Theta[r+L^{-1}\sum d_f(Y)+v+h]\). Conditions (15) and (17)'s preceding radius choice imply
\[
 |T|\le e^{-K_*N}\prod_{Y\in\mathcal D}u_Y\prod_{b\in P_0}q_b,
 \qquad u_Y=(2a/W_0)e^\Theta e^{-\sigma_0d_f(Y)},\quad q_b=pe^\Theta.
\]
Drop only the disjointness restriction between \(P_0\) and \(Y_0\) in the nonnegative sum. All collars still lie in \(Z\). Thus
\[
 \sum_{(\mathcal D,P_0)\ne(\varnothing,\varnothing)}\prod u_Y\prod q_b
 \le\prod_{Y:Y^\sharp\subset Z}(1+u_Y)
       \prod_{b:b^\sharp\subset Z}(1+q_b)-1
 \le e^{\tau N}-1\le\tau e^{2N}.
\]
The subtraction removes the empty selection. Since \(K_*-2=c_\ell\Lambda\), this proves the second line of (26), including its **absolute** selection sum.

Coarse entropy now gives
\[
 \sup_q\sum_{Z\ni q}\widehat w_Ze^{|Z|}
 \le\tau\sum_{m\ge0}C_De^{\kappa_Dm+C_v(m+2)-g_*(m+5)}
 =\tau B_*.
 \tag{27}
\]
The incompatibility-neighbour count and (12) prove the third line.

For completeness, the rooted polymer argument is the one proved by Sussman–Alpoge at SA 1223–1347, attributed there to the Kotecký–Preiss criterion. Order the edges of an incompatibility graph. An edge of that graph is eligible if its endpoints are joined in the selected edge set by a path of strictly smaller edges, whether or not the edge itself is selected. Toggle the smallest eligible edge. Earlier eligibility and connectedness survive the toggle, so this pairs terms with opposite signs. Survivors are spanning trees, because a cycle's largest edge would be eligible. Hence the absolute connected coefficient is bounded by the spanning-tree sum. The rooted sums of height at most \(h\) satisfy
\[
 T_Z^{(0)}=1,\qquad
 T_Z^{(h+1)}=\exp\Big(\sum_{Y\not\sim Z}\widehat w_YT_Y^{(h)}\Big).
\]
Deleting the root gives an unordered collection of child trees; the exponential factorial and the multinomial assignment of labels give exactly the factor \(1/(n-1)!\). By the third line of (26), induction bounds \(T_Z^{(h)}\le e^{|Z|}\). These nonnegative sums increase with \(h\), so their full sum has the same bound. For fixed \(q\in X\), mark a vertex of every list in (11) whose polymer contains \(q\). This enlarges the absolute sum and changes \(1/n!\) to \(1/(n-1)!\). Use (24), then the rooted bound **within \(Z_j\subset X\)**. The result is bounded by the left side of (27). This proves the last line. \(\square\)

**Theorem 5 (main theorem: conditional CI-form at complex inputs).** Assume H-D, H-G, H-S, H-C and H-W on every prescribed local fibre, the constant order above, TD whenever exempt terms occur, and H-F whenever free types occur. Any insertion satisfies H-O's local norm and interface requirements. Then the regular gas formed by (9)–(11) satisfies
\[
 |H(Z;P_Z)|\le C_{\rm act}(a+p_*)e^{-\Lambda\ell_c(Z)},\qquad
 |E(X;P_X)|\le C_{\rm act} B_*(a+p_*)e^{-\mu\ell_c(X)},             \tag{28}
\]
with the absolute majorants (26), incompatibility room \(1/2\), and local normal convergence on the entire declared fixed-\(U\) domains. The functions are holomorphic, real at real inputs, Borel in their specified real parameters, and inherit H-S's covariance, ties, stored-slot and overlap identities. On any parameter polydisc of coordinate radii \(r_j\) contained in the declared domain,
\[
 |\partial^\nu E(X)|\le\nu!\prod_jr_j^{-\nu_j}
                 C_{\rm act} B_*(a+p_*)e^{-\mu\ell_c(X)}          \tag{29}
\]
at its centre. With H-O the same conclusions hold jointly on the ordinary source box, independently of its number of labels. The finite gas satisfies
\(\mathcal Z_Q(P_Q)=\exp(\sum_{X\subset Q}E(X;P_Q|_X))\ne0\).
Its identification with the physical regular integral uses H-S on the complete physical locus.

*Proof.* Lemma 1, TD and the inserted/free bounds give (25); Lemma 2 gives its analytic Gaussian budget. Lemma 4 proves (28) and a parameter-independent summable majorant for (11). Each finite term is holomorphic by Lemma 2 and compact switch integration. Cauchy's formula passes through its normally convergent series, proving holomorphy and (29). The same finite integrals and convergent sums preserve the Borel and algebraic identities supplied in H-S. This requires those identities for the complete integrands; separate noncovariant pieces need not satisfy them.

Expand the finite gas polynomial using ordered lists and the factors \(1-\mathbf1_{Z_i\not\sim Z_j}\). Decomposition of each graph into its connected components shows coefficient by coefficient that its formal logarithm is (11) summed over \(X\). Replace every activity by \(uH\). For \(|u|<1\) the absolute majorant proves analyticity, so the formal identity near zero extends throughout that disc. Dominated convergence at \(u\to1\) proves the asserted exponential identity and nonvanishing. This does not claim nonvanishing on the larger **potential-coupling** polydisc used in Lemma 4.

Under H-O exactly the same majorants apply jointly to the added parameters. Nothing in (20)–(27) counts their labels. The coarse interpolation variables in (10) have already been differentiated and integrated; (29) concerns surviving external parameters. Uniformity on an additional unintegrated decoupling family requires H-G/H-S and the whole argument uniformly in that family; it is not a conclusion on the boundary of the original Cauchy discs.

Finally the choices exist **conditional on the uniform imports**. The slope of the lower endpoint of (15) is smaller than the upper endpoint's slope by the prescribed \(L\) floor. For fixed \(\bar\kappa\), \(M^4e^{-d_GM}\to0\), so (17) is a floor on \(M\). For any \(n>4\), this limit follows from \(e^{d_GM}\ge(d_GM)^n/n!\). After all late constants, \(\mathfrak b/R\to0\), \(g\ell^N\to0\) for fixed \(N\), and \(\mathfrak b\to\infty\). The second limit follows similarly from the exponential series with an integer power larger than \(N\). H-W, TD, H-F and (4) supply their stated uniform limits. Taking suprema above \(\gamma^{-2}\) permits all ceilings in (18) simultaneously. No late amplitude chooses an early constant. \(\square\)

**Outstanding — regular-gas scope.** Even when the exempt set is empty, this theorem still needs full-domain H-D, actual H-G/H-S, and the formation estimates H-C/H-W. It is not unconditional CI for island-free histories. Filing \(E(X)\) into IN1's regular/boundary slots additionally uses the specified scale and hull comparison; it does not supply pointed counterterm cancellation, companions, normalizer bounds or the full induction. Finer marked/typed B4 estimates and the small-field map's separate radius ratios are not conclusions of Theorem 5.

**Lemma 6 (what cube Möbius inversion supplies).** For a jointly holomorphic exempt term on the declared input domain times \(\mathbb D_R\), with the supplied reality, use the disjoint bond ownership fixed above and put, for nonempty \(W\subset\mathcal C_I:=\{\Delta:\Delta\text{ owns a bond in }I\}\),
\[
 f_W(P;B)=\sum_{A\subset W}(-1)^{|W\setminus A|}
                 F_f(P;\mathbf1,B\mathbf1_A).
 \tag{30}
\]
Then \(\sum_{W\ne\varnothing}f_W=F_f(P;\mathbf1,B)-f_0(P)\). Each piece reads only \(W\) and is holomorphic and real on its declared locus. If \(|F_f-f_0|\le\omega_f\) on a radius \(R_f\), then
\[
 |f_W(P;B)|\le 2^{|W|}\omega_f(\mathfrak b/R_f)^{|W|}
 \qquad(\mathfrak b<R_f).                                  \tag{31}
\]

*Proof.* In the double sum including \(W=\varnothing\), the coefficient of a fixed \(A\subset\mathcal C_I\) is \((1-1)^{|\mathcal C_I\setminus A|}\). Only the full set remains. Remove the empty coefficient \(f_0\). The locality, holomorphy and reality assertions follow term by term. Introduce one scalar multiplier for each block \(B|_\Delta\). The finite difference vanishes whenever any multiplier is zero and has modulus at most \(2^{|W|}\omega_f\) when every multiplier has modulus \(<R_f/\mathfrak b\). Repeated Schwarz gives (31). Empty or zero blocks give zero coefficients. \(\square\)

**Outstanding — TD is a bound, not this identity.** Equation (31) has no mutual-distance factor. For islands only a one-sided bound is supplied; a two-sided \(\omega_f\) must not be inserted without an additional oscillation estimate. The one-variable bound depends on \(B_f-\operatorname{Re}f_0(P)\), not on a real centre at complex \(P\).

The draft's three routes do not establish TD or its impossibility. Fine-switch localization pays only for cubes outside the original carrier, with no decay through an exempt island. Its decoration count lower-bounds a chosen **upper majorant**, not an actual potential; the asserted boundary count for every carrier was not proved. Shell localization pays radius, but its assigned carrier can contain many cubes. Cube inversion gives (31), without mutual-distance decay. NL1-L Lemma 5 caps a *guaranteed* radius, not maximal analytic continuation; its distance is to the full source, including stored sources. Thus the draft's claimed strongest-available bounds, quantitative failure threshold and unconditional sufficiency of PAN shells are withdrawn. A row/walk expansion plus a composition and exempt-geometry summation theorem is a possible approach. The draft's proposed rooted-forest factor leaves travel through the island unpaid, so it does not itself imply (8). YM3 52582–52588 supplies a string-wise hull construction for its Gaussian; it is not a proof of the proposed nonlinear DR-row estimate.

**Lemma 7 (conditional island and excess bounds).** At an island's formation assume **H-I**: on its whole prescribed fibre, with stored variables fixed, the complete exponent is holomorphic and real at real inputs, and has a pointwise modulus decomposition
\[
 \Phi_\omega=\Phi_\omega^\circ-\tfrac12q_\omega+V_\omega,
 \quad\Phi_\omega^\circ\in\mathbb R,\quad q_\omega\ge0,
 \quad |V_\omega|\le C_I N_0(\omega).                      \tag{32}
\]
Here \(N_0\) counts stored sites at their own levels, including the prescribed collars and coordinate multiplicities; it is additive over the outer and swallowed records. The \(V\) bound may be supplied by terms each anchored at a stored site, with the sum of their absolute bounds per site at most \(C_{V,1}+C_{V,2}=C_I\). A one-sided old bound is not an absolute bound for that sum. For the uniform exponential bound also supply a finite real ceiling \(\Phi_{\omega,*}^\circ\ge\sup_P\Phi_\omega^\circ(P)\). Then, with \(\Psi_\omega=\Phi_\omega-\Phi_\omega^\circ\),
\[
 \operatorname{Re}\Psi_\omega\le C_I N_0(\omega),\qquad
 \sup_P|e^{\Phi_\omega}|\le e^{\Phi_{\omega,*}^\circ+C_IN_0(\omega)}.
 \tag{33}
\]
For a separately supplied OSF11 excess recursion, assume OSF12's two bounds, with Wilson constant \(C_W^{\rm OSF}\), on the whole complex data box, additive site counts, and absolute old-excess bounds \(|\Psi_{\omega'}|\le fN_{\omega'}\). Then
\[
 |\Psi_\omega|\le\max\{C_W^{\rm OSF}\bar c+2c_{\rm int}(1+\bar c),f\}N_\omega.
 \tag{34}
\]

*Proof.* Drop the nonpositive \(-q_\omega/2\) in the real part of (32), and use \(\operatorname{Re}V\le|V|\). If the per-site version is used, assign each term to its supplied anchor and sum at most \(C_I\) per site. Exponentiating and using the reference ceiling gives (33). Holomorphy belongs to the complete exponent in H-I; it is not inferred for the splitting-dependent summands. No assertion that \(q_\omega\) is constant on a fixed-\(U\) fibre is needed.

For (34), the new portion has modulus at most \(c_{\rm new}N_\omega^0\), where \(c_{\rm new}=C_W^{\rm OSF}\bar c+2c_{\rm int}(1+\bar c)\). Adding the old portions bounds the full modulus by \(c_{\rm new}N_\omega^0+f\sum N_{\omega'}\), which is at most the displayed maximum times their total. This proves the recursive estimate without increasing its constant at each nesting. \(\square\)

**Outstanding — H-I and LF formation.** SA 17822 and 18044–18098 sketch (32) on their admitted pair domains. They do not prove this interface on the entire new ST1 domain. The fixed-real-factor argument in pass 1 does not establish its coverage, the constancy of the stored fluctuation \(B\) in \(q_X\), or separate holomorphy of \(q_X,V_X\). Supply either full creation-domain admission and (32) there, or a direct proof of (32) on the required domain. Small \(r(P)\) alone proves neither. Equation (33) is not an absolute bound on \(\Psi\), so it cannot substitute for the old-excess hypothesis of (34). Neither equation supplies carrier oscillation or the integrable, external-parameter-independent Borel envelopes in IN1 H-E/H-O. Fixed-pair integral bounds cannot replace a bound with the supremum inside the integral.

**Theorem 8 (the part of the CI induction supplied here).** Order the structures of a finite history by formation time. Assume NL1-L Theorem 7's CI-base and CI-maps on their full domains. At each main step assume Theorem 5's hypotheses from earlier activity bounds, without using any bound on the activity then being formed. At each island creation assume H-I and all additional interface clauses in CI-form. At every other stage/output, and for every remaining formed object, supply CI-form's bounds, locally normal or integrable majorants, and identities separately. Then the regular logarithms formed at main steps have the bound in (28); island exponents have (33); and CI propagates over this history.

*Proof.* Induct in the specified finite order. At each main step apply Theorem 5 to its separately supplied inputs, including the oscillation/carrier and Gaussian estimates; CI alone does not supply them. The theorem gives positive absolute majorants and the regular logarithm's analytic interface. Lemma 7 supplies the stated pointwise island bound. Its other interface and integration requirements are the explicit additional hypotheses. At other transitions use the separately supplied formation rule. Borel dependence and identities pass through the allowed dominated integrals and normally convergent series. Overlap agreement assembles the fibre functions into the prescribed domains. CI-base starts the induction. No main-step radius \(R=\ell^q\) is assigned to a preparatory stage without its separate budget. \(\square\)

## Definitions supplied in distillation

1. Disjoint bond ownership, coordinate versus bond-block norms, the window conversion \(C_{\rm win}\), fine/coarse graph tree lengths, collars, self-incompatibility and the distinction between fine switches and coarse parameters.
2. Full local-domain fibres and their restriction/overlap data; the distinction between their suprema and restrictions of one global field; the distinction between domain supply and redefining a domain by intersection.
3. Complete carriers, class/exempt membership, the zero-fluctuation value \(f_0\), an oscillation bound on the actual switched presentation, the half-rate carrier sum and its multiplicity requirement. Forgetting weights are not silently declared to be oscillation bounds.
4. The W affine reads, stored-datum scaling, subtype multiplicity and amplitude (7); the effective covariance, its positive-reference determinant branch and corrected early constants (13).
5. The selected-domain gas, fixed cutoffs, actual support, local restrictions, connected coefficient and absolute union-filed majorant; the optional free/inserted type budgets.
6. The density allowance \(W_0\), amplitude threshold \(a_*\), aggregate amplitudes \(a,p_*\), rate choices \(\alpha,\mu,\Lambda,K_*,\Theta\), and cluster constants \(A_a,B_*,\tau,C_{\rm act}\), with the order in which they may be read.
7. The block Möbius coefficients, stored-site anchors and count, and uniform real-reference ceiling; the distinction between a one-sided island exponent and an absolute OSF excess, and the additional transition hypotheses in Theorem 8.

## Source checks

All external sources are by **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text**, at `31a47c543775`. SA is their [YM4 outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex); CA-I/II are their [complete account I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex) and [II](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex); YM3 is [YM3_I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM3/YM3_I.tex). Each was fetched once. CA-II was needed because the draft actually cites II, not I. The outline index, neighbouring rows and obligations were read before bounded source excerpts. The table covers the draft's external citations and the added proof passages; the mathematics above does not depend on scratch files.

| Source lines checked | Finding and precise scope |
|---|---|
| SA 1150–1347, especially 1273–1326 | Detailed finite polymer proof under the stated criterion; the tree cancellation and root recursion used in Lemma 4 are present. |
| SA 3910–3935; 4006–4037; 4880–4898; 5066–5091; 7569 | B1/B4 are actual-construction requirements. The ordinary box includes boundaries and stored exponents. Finer derivatives, actual matrix/core verification and the map's radius ratios remain separate. |
| SA 5696–5727; 6026–6038; 6141–6158; 6191–6206 | Confirms the towers, Tq radii, initial/top exceptions and exempt metric. Restriction/stage inclusions are hypotheses, not consequences of the radius table. The no-decay-across-islands statement is at **6198**, not 6196. |
| SA 13894–14089 | FG1–FG11 prove the finite-dimensional Gaussian implication. Sharp cutoffs stay real. The draft's \(K+K^3\) estimate is its own error; SA uses an unspecified \(K\)-dependent bound. |
| SA 14091–14217, with 14219–14270 | The precision, separately decoupled root, references and local comparison are described conditionally on the actual operator/core package. A global independent-current Gaussian is not supplied. |
| SA 14276–14811 | UM1 and the actual Gaussian/structural package are hypotheses. UM7–UM30 derive the majorants, with the local-core supremum explicit at 14673–14684. The insertion slot is conditional on its own norm. |
| SA 17266–17278; 17317–17334; 17558–17564; 17648–17654 | Confirms class bounds, boxing and retention. These do not prove every exempt carrier's boundary lower bound. The background-difference filing sentence is at **17564**, not 17562. |
| SA 17794–17838; 17872–17957; 17959–18098 | Mass uses a supremum inside the stored-variable integral. Localization, stage amplitudes, healing and the pair modulus argument are sketched. SA gives splitting-dependent \(q_X,V_X\), and holomorphy of their complete sum; it does not license the draft's separate holomorphy proof. |
| SA 19466–19521; 19571–19729 | Confirms late amplitudes and supremum-form ceilings. OSF3 is an assumed formation estimate; OSF6 only sums it. OSF12, additive recursion and absolute old bounds imply OSF13. Carrier oscillation remains additional. |
| CA-I 49495–49546; 54985–55005 | The indexed operator scope leaves application admission/drop-out spaces as conditions; the preparatory theorem assumes its stage input. Neither identifies the new ST1 chain domains. |
| CA-II 79910–80013 | The Bałaban exponent and stored/free split are present; the derivation is expressly not reproduced. This citation does not prove H-W. |
| YM3 52567–52600, especially 52582–52588 | Each Gaussian coefficient/string receives its own hull product of switches. This supports the analogy only, not nonlinear DR-row or TD in four dimensions. |

The local source check uses current NL1-L Theorems 4/7, PR-lay Theorems 3/8, IN1 H-M/Lemmas 2–3 and ST1 Theorem 14. PAN §4's per-kind inputs remain hypotheses. The intrinsic-action result in um1/um1-fix does not cover all layered/seam or exempt terms. The covariance checks retain their clauses: [kept-cov-check](../gates/kept-cov-check.md) requires relative-form carriage and the native action; [r-inv-check](../gates/r-inv-check.md) requires its specified formation rules and polymer-wise naturality. They do not supply domain admission or a new unrestricted covariance theorem. The process review specifies draft–distil–referee; this text completes only distillation.

## Result

Theorem 5 proves the regular-gas CI-form implication, including positive absolute majorants and fixed-\(U\) holomorphy at every **supplied** complex input. Lemma 1 supplies localization for class terms with actual oscillation/carrier bounds. Lemma 7 gives the conditional island and excess estimates. Theorem 8 states exactly how these feed CI. This is an IN1 **input**, not a new proof of IN1: the distilled IN1 proves its matrix/budget, genealogy and stopping implications and conditional induction under its own H-M, H-OL, H-SF, H-LF, H-G, H-C, H-E, H-O and H-SUM. Its hypotheses are not discharged by this text.

Imports here are H-D, actual H-G/H-S, H-C, H-W, TD/H-F where present, H-O for ordinary sources and insertions, H-I and the separate OSF12/old-excess inputs for islands, plus the base and remaining transition formation packages in Theorem 8. **Outstanding** actual-domain, Gaussian-identification, forgetting/carrier, W, TD and LF domination/oscillation obligations remain in place. TD is not the sole remaining input.

Corrections to pass 1:

1. Replaced obsolete draft-only closure claims with the current full-domain, precision-versus-actual-Gaussian and complex-identification hypotheses. Restored local-core suprema, inherited current-layer indices and overlap/structural requirements.
2. Replaced the full-rate carrier sum by a half-rate sum with entropy room; made weighted oscillation, metric comparison and complete-carrier multiplicity explicit. Removed the unsupported replacement of \(2b_f\) by a numerical forgetting weight. Removed the unnecessary factor two in the resulting class amplitude.
3. Corrected Gaussian domination from \(K+K^3\) to \(K+K^4\), shrinking only early \(K\)-dependent constants. Retained the actual coefficient-ratio envelope as an import, rather than deriving it from the auxiliary path construction.
4. Corrected W's stored-variable scaling and allowed late amplitudes and all subtype multiplicities. Kept its finite-range/vanishing-order decomposition conditional; the Bałaban display alone does not prove it.
5. Proved absolute selection and cluster majorants, handled \(a=0\), kept cutoffs fixed, and separated integrated coarse variables from surviving external parameters. Replaced the ambiguous boundary-distance derivative formula by explicit contained polydiscs. Limited ordinary-source uniformity to the full uniform input package.
6. Kept TD open without claiming failure of the actual potentials. Withdrew the universal decoration/shell geometry claims, maximal-radius interpretation, quantitative A3 threshold, claimed sufficiency of DR-row alone, and unsupported PAN closure.
7. Replaced island fixed-\(U\) constancy/separate-holomorphy claims by the required pointwise nonnegative decomposition and complete-exponent holomorphy; required a uniform real-reference ceiling for a supremum bound. Restored absolute old-excess bounds and additive recursion for OSF13; kept site counts, reserve volumes, oscillation and integrated mass distinct.
8. Restricted the induction to its separately supplied main, island, stage and output formation packages. Made IN1's full order visible and corrected source pinpoints and scope as recorded above. No other manuscript or prompt file was changed.

This is a distillation and conditional extension of the sources' formation arguments, with corrections to our draft. It claims no correction of the Sussman–Alpoge text and no Yang–Mills closure. **The text is not yet refereed.**
