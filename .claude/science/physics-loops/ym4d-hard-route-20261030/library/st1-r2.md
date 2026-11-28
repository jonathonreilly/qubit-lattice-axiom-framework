# ST1, round 2: hereditary substitution and physical identification

Provenance: Codex (GPT-6), 2026-11-04, checkout e79e626c00d7dd3e8fc05309755dab6bf5e02ab9; pass-2 distillation of Claude's pass-1 drafts; research text, not an audit, no status granted. Source text by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors, at 31a47c543775. Written proofs only; no computer-assisted discharge. Not yet refereed.

This distils `st1-draft2.md`, `lev-core-draft.md`, `p81-crit-draft.md` and `os-draft.md`, all pass-1 drafts by Claude, against the Outstanding list of `st1.md`. The conclusion is a conditional substitution theorem, Theorem 14. The claim that its hypotheses hold at every actual stage is **Outstanding** at the places identified below. In particular, a fibre factorisation conditional on a parametrisation is not a construction of that parametrisation, and a pointwise lifted estimate does not imply a core estimate with the infimum lift.

SA denotes the four-dimensional outline, CA-I its complete account I, and Y3 the three-dimensional manuscript, all at `31a47c543775`. The averaging, gauge, background and stage constructions originate in Tadeusz Bałaban's work; the source formulations and Y3 proof templates used here are credited to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Source line numbers refer to the three files specified in the task, not to the working checkout. No scientific status is assigned to an input or conclusion.

## 1. Definitions

Work on a finite four-dimensional periodic lattice, with odd \(L\ge13\). All cubes and blocks are centred, aligned and nonwrapping. In level-\(i\) units the bare mesh is \(\eta_i=L^{-i}\). Real bond configurations take values in \(SU(2)\), complex ones in \(SL(2,\mathbb C)\); potentials lie in the complexification of the traceless Hermitian matrices. Use the matrix operator norm. Reverse bonds by inversion and reverse potentials by transported negation. Put
\[
 U^g(b)=g(b_-)U(b)g(b_+)^{-1},\qquad
 (\nabla^U_\nu A)_\mu(x)=\eta^{-1}
 [\operatorname{Ad}(U_\nu(x))A_\mu(x+\eta e_\nu)-A_\mu(x)].                 \tag{1}
\]
Every difference uses only its contained stencil. A complete bond star contains **six** plaquettes. Fix \(S_{\Omega_0}(U)=\sum_{\pi\subset\Omega_0}[1-\tfrac12\operatorname{tr}\partial U(\pi)]\), one orientation per plaquette, and its holomorphic extension. Its current \(J^\circ_\eta\) is defined by
\[
 \left.\frac d{dt}S_{\Omega_0}(e^{it\eta B}U)\right|_{t=0}
       =\eta^4\sum_b\tfrac12\operatorname{tr}(J^\circ_\eta(U)(b)B(b)).       \tag{2}
\]
The plain current \(J_+\) equals this current at complete stars and is zero at incomplete ones. These currents are different at a regional boundary.

A determining sequence is \(\Omega_0\supset\cdots\supset\Omega_k\), with \(\Omega_{k+1}=\varnothing\), each member a union of \(M_1\xi_q\)-cubes, \(\xi_q=L^q\eta\), and
\[
 \operatorname{dist}_\infty(\Omega_{q+1},\Omega_q^c)>\rho_0\xi_q.           \tag{3}
\]
Set \(m(x)=\max\{q:x\in\Omega_q\}\), \(l(x)=\xi_{m(x)}\), and define \(d\) as the infimum of coordinate-path lengths with density \(1/l(x)\), taking its lower limiting value at shared faces; outside \(\Omega_1\) the density is \(1/\eta\). A top \(y\in\mathbb T^{(q)}\cap(\Omega_q\setminus\Omega_{q+1})\) has pillar \(B^q(y)\). The pillars partition \(\Omega_0\). The determining rows \(\Gamma_q\) are the level-\(q\) bonds with both endpoints in \(\Omega_0\), an endpoint in \(\Omega_q\) and no endpoint in \(\Omega_{q+1}\). There are no inward rows. An outward row's outer endpoint is a top of level \(q-1\).

Write \(\operatorname{Bd}(X)\) for bonds incident to \(X\), and \(\operatorname{Bd}^{\circ}(X)\) for bonds with both endpoints in \(X\). A bond or stencil is read at its initial or base site; estimates include all neighbouring stencils they use. Array norms are maximum norms and empty maxima are zero. Row endpoints are nodes; a residual gauge is one at all nodes. Criticality over a datum means that the first action variation vanishes on the kernel of the actual determining map's derivative. Both erosion rules are specified nested aligned cubical sequences, supplied as part of GEO.

Write \(\mathbf B=\bigcup_q\Gamma_q\) and

\[
 M_{\mathbf B}(U)=(\mathcal M^qU|_{\Gamma_q})_q.                            \tag{4}
\]

Here \(\mathcal M\) is the actual SA average: if \(\operatorname{av}(V_i)\) solves \(\sum_i\log(V_iV^{-1})=0\), \(U(y,x)\) is that mean over the at most \(4!\) coordinate-ordered shortest paths, \(x'=x+c_+-c_-\), and \(U[c]\) is the straight product, then
\[
 \mathcal M(U)(c)=\exp\left(L^{-4}\sum_{x\in B(c_-)}
 \log[U(c_-,x)U([x,x'])U(x',c_+)U[c]^{-1}]\right)U[c].                   \tag{5}
\]
Only its small-curvature analytic branch is used. Iteration means successive applications of (5). A row reads its double block. The canonical background representative uses combs in order (4,3,2,1). Stored transports below use the **averaged contour convention** of Y3, fixed once; the two conventions are not identified.

For a real regular datum \(V\), \(\Phi_V(B)\) denotes the canonical continued background at the **raw** datum \(e^{iB}V\). The raw coordinate is
\[
 B_V(D)=i^{-1}\operatorname{Log}(DV^{-1}).                                \tag{6}
\]
The reduced row datum \(b_V(B)\) is a different map. It is \(B\) on interior rows; on an outward row \(c\) with outer end \(z=c_+\),
\[
 e^{ib_V(B)(c)}=e^{iB(c)}\operatorname{Ad}(V(c))v_z(B),                   \tag{7}
\]
where \(v_z\) is the one-step block factor formed from the interior lower-level rows in \(B(z)\); use the mirror formula at \(c_-\). This triangular map is locally invertible. Feed (6) to \(\Phi\), and (7) to the response equations. In particular the tower is
\[
 T_e(U,A')=\Phi_{M_e(U)}\bigl(B_{M_e(U)}(M_e(e^{i\eta A'}U))\bigr),         \tag{8}
\]
not \(\Phi_{M_e(U)}(b_{M_e(U)}(B))\).

A triple \(P=(U,A',\mathbf J)\) has real \(U\), independent complex \(A',\mathbf J\), and pair \(\mathbf p(P)=(\mathbf U,\mathbf J)\), \(\mathbf U=e^{i\eta A'}U\). Restriction discards outside bonds. Changing from level \(u\) to level \(v\le u\) sends
\[
 (U,A',\mathbf J)\longmapsto(U,L^{-(u-v)}A',L^{-3(u-v)}\mathbf J).         \tag{9}
\]
For a shift \(h=(H,K)\), define, on active bonds,
\[
 P\dotplus h=(U,A'',\mathbf J+K),\qquad
 A''=(i\eta)^{-1}\operatorname{Log}(e^{i\eta H}e^{i\eta A'}).              \tag{10}
\]
On inactive bonds keep \(A''=A'\). The real factor stays fixed. The current in (10) is not replaced by the physical current at complex parameters.

The level-\(i\) core \(\mathcal U_i^\circ(X;b_0,b_1)\), \(0<b_0\le b_1\), has the strict conditions
\[
 |\partial U-I|,|\partial\mathbf U-I|<b_0\eta_i^2,\quad
 |A'|,|\nabla^UA'|<b_1,\quad |\mathbf J|<b_0.                            \tag{11}
\]
Every contained cube of side at most \(C_{\rm box}LM\) must admit a real gauge with \(|A|,|\nabla A|<C_{\rm pot}Mb_0\). At every allowed subdomain \(Z\subset X\) of level \(p\le i\), both recorded erosion rules and every \(1\le n\le p\), (8) must exist and, on \(Z^{\wr p}\), satisfy
\[
 |\partial T_n-I|<b_0L^{-(i-p)}\eta_p^2,\qquad
 |J_n(T_n)|<b_0L^{-(i-p)}L^{2(n-p)}.                                    \tag{12}
\]
Here \(Z^{\wr p}\) removes two layers of level-\((p-1)\) \(M\)-cubes, and \(J_n\) is in level-\(n\) units. Impose (12) also for \(A'=0\). Core membership includes the open continuation domains, not merely the inequalities.

A **read record** fixes its function, stencil or domain, units, radius index, lift and positive base radius. Its function is one of (11), a settled tower quantity in (8), or a core (11)–(12); its witness records specify actual gauge cubes and bounds. A core radius is a single scalar. If its coefficient or lift varies spatially, take the infimum of the **whole product** over its read set. Equivalently its base radius is \(R_\iota=\alpha_\iota\varepsilon_i\inf_X\lambda\) and its effective coefficient is \(\inf_X(c_\sigma\lambda)/\inf_X\lambda\). Taking only the infimum of the lift while writing an unspecified \(c_\sigma(i)\) does not define a radius.

For a finite ordered history, the chain domain \(\mathcal D_{a|\sigma}\) imposes every record born between \(a\) and \(\sigma\). A record \(r\) retains its own function and base radius \(R_r\), while its current radius is \(c_\sigma(r)R_r\). Gauge witnesses and the absolute real curvature ceiling \(a_T/4\) are retained unchanged. New records add conditions. For a transition \(-\to+\), **compatibility with room** means that every target record occurs in the input, with
\[
 c_-(r)-c_+(r)\ge d_*(m_r)>0,\qquad
 \Delta_r=(c_-(r)-c_+(r))R_r,\qquad
 b_r^{\rm mid}=\tfrac12(c_-(r)+c_+(r))R_r.                              \tag{13}
\]
For a core this is required for both radii, with a common scalar shrinkage. All read sets include the stencils needed by their estimates.

The round-2 records have simple radii \(c_\sigma(x|m)\lambda_\tau(x)\alpha_\iota\varepsilon_mL^{-pm}\), frozen at their birth structure \(\tau\); \(p=1,2,3\) is the scaling degree. Tower records use the meet of that frozen sequence with each erosion tower and, for \(1\le q\le p\le i\), the bounds
\[
 |\partial T_q-I|<L^{i-p}c_\sigma(x|\ell)\lambda_\tau(x)\alpha_0\varepsilon_\ell L^{-2\ell},
\quad
 \eta_q^3|J_q|<L^{i-p}c_\sigma(x|\ell)\lambda_\tau(x)\alpha_0\varepsilon_\ell
                 L^{-2\ell-\min(q,\ell)},\quad \ell=\min(m_\tau(x),i).    \tag{14}
\]
Core records use \(b_\iota=\alpha_\iota\varepsilon_i\inf_{X_r}[c_\sigma(x|i)\lambda_\tau(x)]\). Witness bounds are \(g_Q\Lambda_Q\alpha_0\varepsilon_i\), where \(\Lambda_Q=\sup_{Q^+}\lambda_\tau\), \(Q^+\) is the recorded enlarged cube, and \(g_Q\) is respectively \(\mathsf oLMB^{cg}, BM,C_{\rm pot}M\) for large, CA-I and core families. Natural cubes require a containing cube with bound \(a_\flat\). Enlargements must lie in the region on which the field is supplied.

A carried activity \(f\) is bounded by \(b_f\) on its declared domain, holomorphic in \((A',\mathbf J)\) with \(U\) fixed, Borel in \(U\) and near stored variables, and jointly holomorphic in far variables and their recorded switches. Each stored slot records its bond, initial site, level, range, near/far class and transport convention. Require simultaneous real gauge covariance and equality at two real splittings of one pair. A **pair function** additionally has equality at complex splittings and holomorphic descent on the relevant common domains. A real tie alone is not that additional assertion.

## 2. Remaining inputs and order of constants

The following are hypotheses, not consequences of a source label.

* **GEO.** The aligned centred block geometry above; both erosion assignments; an injective periodic coordinate chart for every read cube and its required margin; the prepared sets and margins in Lemma 2; memberwise monotonicity along the history being compared; complete stencils at core addresses; and the witness enlargements required in Lemma 10. Turning cells and their two-stencil margins lie in the response wall component on which they act. A stored level-\(l\) slot starts at a level-\(l\) lattice site, outside \(\Lambda_{l+1}\), at distance \(>2\xi_{l+1}+2\eta\) from \(\Omega_{l+2}\), and disappears when its collar is integrated. Mark resets and lift formation must be specified, rather than inferred from a partial order.
* **AV/CURV.** The actual formula (5), its local analytic row bound \(|B(c)|\le C_Q\xi_q\sup_{D(c)}|A|\) on a fixed weighted value ball; and the real curvature recursion \(v_{n+1}\le L^2v_n+C(L^2v_n)^2\). The resulting test bound is \(2\epsilon\) inside a layer and \(C_{\rm sm}L^2\epsilon\) across a seam. The recursion itself remains imported from `a1-balaban.md` §3.5.
* **A1/F0/REG.** The real regular critical orbit, canonical comb representative, local analytic continuation and restriction theorem in `a1-balaban.md` §§3.5–9, conditional on its flat input F0; and the local regularity conversion REG in `p82-draft.md`. The precise consequence used is Lemma 5. This packaging does not establish F0 or A1.
* **P82°, M1 and the derivative theorem.** At a real curved regular critical reference, the weighted inverse for the outline's pillar-\(R\) slice and straightened \(K_0\), with the multiplier normalization, implies the four-dimensional derivative estimates of `a3-derivative.md` §§6–7. On the whole fixed raw-datum ball, a row direction \(e_c\) satisfies
  \[
  \xi_y|\dot H|,\ \xi_y^2|\nabla\dot H|,\ \xi_y^3|D^{\mathsf T}D\dot H|,
  \ \xi_y^3|\dot J|,\ |\dot u(y)|
        \le C_4e^{-\theta_4d(y,y_c)}|e_c|.                              \tag{15}
  \]
  The current member is required independently of a first-derivative bound on \(H\). P82° is the principal analytic import still open on this route. We use the stated implication to (15), not an unproved inference from the name P82.
* **PROF/RCG4.** A real critical background has normalized curvature and current bounded by \(C_P\max_\tau e^{-\delta_Pd(x,\tau)}|\partial V(\tau)-I|\). On a cube of side \(s\), with its side-\((s+6)\) enlargement, curvature \(<wL^2\eta_i^2\), matrix divergence \(<2L^3w\eta_i^2\), and \((s+2)L^3w<c_{\rm rg}\), RCG4 gives a real gauge with \(|A|,|\nabla A|<4L^3B_*(s+2)w\). These are the explicit profile and cube-gauge inputs of `a3-profile.md` and `a1-balaban.md` §3.8.
* **OPS/SLICE/UNQ.** All inverses in Lemma 6 exist on the declared regular-pair ball. The repaired local Landau chart and its tangent factorisation (`a3-derivative.md` Lemmas 6.1–6.3) hold. The straightening and response fixed points have unique small solutions, uniformly on their stated balls. No inverse is inferred from formal matrix notation.
* **DR, including its specification at one.** An actual regional response \((H,K)\), holomorphic in its complex input pair, datum and \(|s_\Delta|<e^{\bar\kappa}\), is given, with reality, covariance, restriction consistency, common-lift transport and splitting over face-connected components. At \(s=1\) it uses the reduced action and multiplier formulas of Lemma 6. For source \(S\), it obeys
  \[
   n_b(H,K):=\max\{l|H|,l^2|\nabla^UH|,l^3|K|\}
       \le C_D E_{\bar\kappa} C_A\delta_{\rm src}e^{-\mu d(b,S)}.         \tag{16}
  \]
  Here \(C_D,\mu\) are fixed constants; \(E_{\bar\kappa}\ge1\) is a specified parameter factor, for example \(e^{C_E\bar\kappa}\) with fixed \(C_E\). Keep it in every source budget. It is not an IN1 precision constant. Likewise write the source-domain threshold explicitly if it is \(\epsilon_D e^{-c_D\bar\kappa}\).
* **FL/CH/BOX and activity interface.** The actual stage-coordinate map, with its complex contour bound, is the input specified in Lemma 12; CH supplies the indicated restricted pivot graph. BOX supplies the separate box-output background and response estimates, with its declared \(C(M)\). NL1/LF1 supply the carried activities, their bounds, joint stored-variable structure and the sums in which they occur. None of these is proved by a Cauchy estimate on a hypothetical composition.
* **RUN and formation data.** \(\varepsilon_m=\theta_m^{-1/2}(\log\theta_m)^{p_0}\), up to the fixed common normalization, \(\theta_m\ge\gamma^{-2}\), bounded adjacent frame increments, \(N_t=N(\min_{u\le t}\theta_u)\), \(1\le N(\theta)\le C_N(\log\theta)^r\), with \(N\) nondecreasing and \(p_0-p_1>r\). The stage tests and raw lifts are as in Lemma 10, and their global smallness is required on every recorded carrier.

Here is an acyclic order; all constants in rows 1–6 precede \(\kappa\) and are independent of \(M,\bar\kappa\).

| Order | Choice |
|---|---|
| 1 | \(0<\beta_s\le1/4\), \(0<\theta_s<1\), \(0<\beta_R\le(1-\theta_s)\beta_s/16\); \(p_0,p_1,r\); \(L\ge13\), \(2\le L_\flat<L/2\); fixed geometric family constants. |
| 2 | Fix the earlier flat/analytic geometry, \(M_1\) after its own floors, and prior chart radii. Take AV/CURV, profile, derivative and DR base constants and rates uniform for all larger separation gaps, including \(C_E,c_D\); CH/FL's fixed chart and completion constants, including \(C_A\); the RUN bounds \(C_N,C_\theta\), and lift bounds \(C_R,r_R\); then the pillar and levelling constants of Lemmas 3–4. Set \(\delta=\min(1,\delta_P,\theta_4)\), \(\delta_T=\delta/4\). |
| 3 | \(R_1\) and \(\rho_0=R_1M_1\) above all earlier floors, \(\rho_0\ge4L^2\), \(\delta\rho_0\ge64\log L\), \(\rho_0\min(\delta_T,\mu/2)\ge\log16\); then \(M'_1\ge\rho_0\). Shrink the prior continuation radii to \(\bar\varepsilon,r_B\) and the local chart radii as needed, retaining the earlier estimates. A1's reset length is a separate earlier constant, not \(\rho_0\) itself. |
| 4 | \(\delta_B\le\min(1/40,r_B/40)\); \(K_a,K_T,a_T\) and the intermediate fixed radii from Lemma 8; then \(K^\sharp=\max(1,e^{4\delta_T}K_T)\), \(C_{\rm os}=18\), \(a^\sharp\le\min(1/60,a_T)\). Choose an absolute ceiling \(\widehat a\) below all analytic, levelling and tube ceilings, including \(a_T/4\) and \(\delta_B/(4C_QL)\). |
| 5 | Fix \(C_{\rm RA},C_{\rm mb}\) from the prior constants as in Lemma 10, then \(\alpha_1\ge\alpha_0\ge16\max(1,C_{\rm mb})C_{\rm RA}/c_{\min}^2\), where \(c_{\min}=1-11\beta_s/8-3\beta_R\). This floor pays the fixed stage-to-layer \(L^2\) loss. |
| 6 | \(K_{\rm pt},K_{\rm tw},K_{\rm core}\) from Lemmas 7–9 and \(r_*=[8\max(8L^2,K_{\rm pt},K_{\rm tw},K_{\rm core})]^{-1}\), decreased by fixed factors whenever needed below. |
| 7 | The consumer's \(\kappa\), then its \(\bar\kappa\ge1\), without redefining rows 1–6. |
| 8 | Aligned \(M\) with \(LM\ge2\rho_0\), \(M\ge L^4M'_1\), \(M\ge C_{\rm dec}\bar\kappa\) for the DR construction; require GEO's cube and margin embeddings in the chosen torus. |
| 9 | \(A_1/A_0\) small enough for Lemma 13's main-step bound. |
| 10 | \(\gamma\) small enough for adjacent radius ratios, all analytic ceilings, \(M\sup\lambda\alpha_1\varepsilon\ll1\), \(2(b_0+b_1)<a^\sharp\), the stage bound of Lemma 13, FL's chart radius and the separately stated BOX ceilings. |

The constants \(C_{\rm os},K^\sharp\) are in **row 4**, after the tower estimate; fix \(c_\natural\ge1\) there. No \(b_1^2\le c_\natural b_0\) hypothesis is needed for the Lipschitz proof of CORE below. \(C(M)\) is a box-operation input chosen after \(M\); it is not an IN1-uniform stage constant. **IN1 requires its precision constants \((a,H,\mu_0)\), and the uniform background/tower bounds feeding them, to be fixed before \(\kappa\), independently of \(M,\bar\kappa\).** This is a hypothesis on the P82/REG supply on the whole admitted class. Neither \(E_{\bar\kappa}\) nor \(C(M)\) may be absorbed into those constants. They enter only the later amplitude and coupling ceilings. The stronger claim \(E_{\bar\kappa}\le2\) is not proved here and is not used.

## 3. Geometry and the stage reserve

**Lemma 1 (stage reserve).** Write \(\bar N(u)=N(\theta_u)\), \(a_u=\beta_s/(8\bar N(u))\); \(a_u\) is unrelated to IN1's \(\kappa\). Count completed stages once per operation level, not per component. Set
\[
\begin{split}
c_\sigma(x|m)={}&1-\beta_s+\beta_s2^{-(t-m)}
 +\varpi_\sigma g_t(m)-\beta_R\sum_{u\in\mathrm{Re}_\sigma(x)}2^{-|m-u|}
 -\sum_{(t',n')\in\mathrm{St}(\sigma)}a_{j_{t',n'}}2^{-|m-j_{t',n'}|},\\
g_t(m)={}&\theta_s\beta_s2^{-(t-m)}\ (m<t),\quad g_t(t)=\beta_s,\\
\varpi_{\rm in}={}&1,\quad\varpi_n=1-n/(2N_t),\quad\varpi_{\rm out}=0,
\qquad j_{t,n}=t-N_t+n .
\end{split}                                                            \tag{17}
\]
Here \(0\le n<N_t\) indexes a stage from phase \(n\) to phase \(n+1\), so \(t-N_t\le j_{t,n}\le t-1\). Then \(c_{\min}\le c_\sigma\le1+\beta_s\), \(c_{\min}\ge39/64\). With unchanged marks at main and output transitions and only added marks at a stage, the drops dominate
\[
d_*(m)=
\begin{cases}
(1-\theta_s)\beta_s2^{-(t-m)},&\text{main step},\ m\le t-1,\\
a_j2^{-|m-j|},&\text{stage at level }j,\\
\frac12\theta_s\beta_s2^{-(t-m)},&\text{output},\ m\le t ,
\end{cases}
\qquad w(m)=\tfrac12d_*(m)\alpha_0\varepsilon_m.                          \tag{18}
\]
Also \(w(m')\le4^{|m'-m|}w(m)\) and \(L^{-p\nu}w(m+\nu)\le w(m)\) for \(p\ge1,\nu\ge0\).

*Proof.* A stage at level \(u\) occurs in an operation \(t\) only if \(1\le t-u\le N_t\le N(\theta_u)=\bar N(u)\). At most \(\bar N(u)\) stages have that level. Their total debt is at most \(\beta_s2^{-|m-u|}/8\). The sum of \(2^{-|m-u|}\) over integer \(u\) is \(3\); the mark set has no repeated level. This proves the range. Subtracting (17) gives the main drop in (18), the stage drop \(g_t(m)/(2N_t)+a_j2^{-|m-j|}\) plus new-mark debts, and the output drop \(g_t(m)/2\). Bounded frame increments imply \(1/2\le\varepsilon_{m+1}/\varepsilon_m\le2\) for small \(\gamma\), since the logarithmic derivative of \(\theta^{-1/2}(\log\theta)^{p_0}\) tends to zero. Each geometric factor changes by at most two per level. Finally \(4/L<1\). ∎

**Outstanding M (deleted marks).** SA 6111–6113 and 17433–17440 allow a swallowed mark to disappear. If \(D\) is the set of deleted marked levels, the drop in (17) loses \(\beta_R\sum_{u\in D}2^{-|m-u|}\). The draft's output calculation omits this term. At an old index \(m=u\ll t\), it need not be paid by \(g_t(m)/2\). Supply a reset comparison for affected records, or a permanently retained debt ledger with its consumer domains verified. Theorem 14 assumes the actual gaps (13); the same-marks calculation does not establish them at a reset.

**Lemma 2 (prepared sequences and metric bounds; OS).** Assume GEO-prep as follows. In level-\(k\) units, \(u_i=L^{i-k}\), \(a_i=MR_iu_i\); the global sets \(\Lambda_i^c\) are increasing with no component joining during \(h<i\le k\). Fix one class component \(Z\), and inside it write \(Z_i=Z\cap\Lambda_i^c\), as CA-I 53747–53753 prescribes. Put \(k_0=k-N_0\), \(N_0\ge2\), \(L^{N_0-1}=R_{k_0+1}\). The prepared \(Z''_i\subset Z\cap\Omega_i^c\) are nested. For \(i>k_0\) successive members have an intervening layer of level-\(i\) \(M\)-cubes; for \(h<i\le k_0\), \(Z''_i=Z\cap(\Omega_i^{\sim5})^c\); for \(i\le h\), \(Z''_i=Z_i\). Assume
\[
 Z_{i+1}\supset(Z_i)^{+10a_{i+1}},\quad
 \Omega_{i+1}^c\supset(Z_i)^{+5La_{i+1}},\quad Z''_{h+1}\supset Z_h,        \tag{19}
\]
and a five-layer enlargement of width at most \(5a_{i+1}\).
After \(n\) stages replace \(\Omega_i\cap Z\) by \(Z\setminus Z''_i\) for \(h<i\le h+n\). New internal gaps are at least \(LM\) in earlier-level units; the full sequence has gap at least the minimum of \(LM\) and the original label gap. In particular it is \(\rho_0\)-separated under (3) and \(LM\ge2\rho_0\). Its meets with separated erosion sequences are separated. Overlapping integration collars do not impair this statement.

For a separated sequence,
\[
 |m(x)-m(z)|\le1+d(x,z)/\rho_0.                                         \tag{20}
\]
A site-to-top coordinate path has weighted length **less than 2**; a pillar diameter is less than \(4\). For a subordinate sequence of depth \(p\), scales \(\xi'\le l\), and \(s=l/\xi'\),
\[
 d'\ge d,\quad d'(x,z)\ge|x-z|_\infty/\xi_p,\quad
 s(x)/s(z)\le L^{2+2d'(x,z)/\rho_0}.                                    \tag{21}
\]
If \(a\le1\), \(a\rho_0\ge16\log L\), assign each row its initial endpoint top. Then
\[
 \sum_c e^{-ad(x,y_c)}
 \le S_4(a):=2000L^9\sum_{r\ge0}(r+2)^5e^{-ar/2}<\infty.                 \tag{22}
\]

*Proof.* Inside \(Z\), two remade high members have the prepared one-cube gap; two low ones have gap \(5(L-1)a_{i+1}\) by (19). At the first unremade member use \(Z''_i\subset Z_i\) and (19). At \(i=h\), use \(\Omega_h^c\cap Z\subset Z_h=Z''_h\), not equality with a remade member. Two unremade members have the label gap. Across \(\partial Z\), a complementary point outside \(Z\) belongs to another global component of \(\Lambda_k^c\); its connected \(10a_{i+1}\)-neighbourhood cannot reach \(Z\), by the class margins. In the reverse direction, the deeper outside point is in the original \(\Omega_{i+1}\), while a new complementary inside point is still in \(\Omega_i^c\); use the original gap. The newly prepared lengths are at least \(LMu_i\), and the other comparisons retain the original gap. Complements of meets are unions.

Each intervening layer crossing costs \(\rho_0\), proving (20). Four centre-to-site coordinate displacements total at most \(2(L^q-1)\eta<2\xi_q\). Comparing path densities and applying (20) to both sequences proves (21). For (22), the shell \(r\le d(x,y)<r+1\) has at most \(3(r+2)\) possible levels. Its tops are within radius \((r+1)\xi_{m(x)+1+(r+1)/\rho_0}\), with spacing at least \(\xi_{m(x)-1-(r+1)/\rho_0}\). There are at most \(81(r+1)^4L^{8+8(r+1)/\rho_0}\) tops per level and four positive rows per site. Multiply by \(e^{-ar}\), use \(8\log L/\rho_0\le a/2\), and sum. ∎

The enlargement-width convention is an explicit hypothesis: CA-I 53742–53743 names Bałaban's layers without defining their metric width. CA-I 53773–53774 does supply \(N_0\ge2\), needed for the lift cap. Once GEO-prep and \(LM\ge2\rho_0\) hold, no additional OS analytic import is needed.

## 4. Averaging and pinned levelling

**Lemma 3 (uniform pillar calculus).** Under AV/CURV, sufficiently small normalized real curvature and complex value perturbations on a height-\(q\) pillar give holomorphic actual averages, contour variables and relative node factors. Write \(a_n\) for the dimensionless relative potential at the \(n\)-th straightened average and \(v_n\) for its relative node factor. If \(\epsilon=\xi_q\sup|H|\), then
\[
 |a_n|\le2\epsilon L^{n-q},\quad
 |v_n^{\pm1}-I|\le C_v\epsilon L^{n-q}\ (n<q),\quad
 |v_q^{\pm1}-I|\le C_v\epsilon.                                         \tag{23}
\]
The constants are independent of \(q\).

*Proof.* Convergent exponential and logarithm series on a fixed small ball give, for \(\ell(X,Z)=\log(e^Xe^Z)-X-Z\),
\[
 |\ell(X,Z)|\le C|X||Z|,\qquad
 |\ell(X,Z)-\ell(X,Z')|\le C|X||Z-Z'|.                                  \tag{24}
\]
Indeed \(\ell\) vanishes on both axes; bound its absolutely convergent series on a twice larger ball, apply Schwarz in each argument and then Cauchy. The analogous estimate in \(X\) follows in the same way.
Writing \(V_i=e^{w_i}V_1\), the Federbush equation is
\(X=\bar w+N^{-1}\sum_i\ell(w_i,-X)\).
Choose \(C\max|w_i|<1/4\). Contraction on \(|X|\le2\max|w_i|\) proves uniqueness, holomorphy and Lipschitz bounds uniform in \(N\le24\). Conjugating the equation proves covariance within the branch; uniqueness under \(g\mapsto(g^*)^{-1}\) proves reality.

For the real comb gauge take the root-to-\(x\) path \(P(x)\) and set **\(g(x)=U(P(x))\)**. This kills its tree bonds under (1). Moving any other bond to the tree crosses at most \(3m\) plaquettes, so unitary telescoping gives \(|U^g(b)-I|\le3m\varpi\). The inverse used in the pass-1 proof has the wrong sign.
Writing \(\varpi_n\) for the real averaged curvature, normalize CURV by \(w_n=L^{2(q-n)}\varpi_n\). Its quadratic errors sum as \(\sum_{n<q}L^{2(n+1-q)}\); small initial curvature gives \(w_n\le2w_0\). The comb bound supplies small gauges at every scale.

Differentiating (5) and its block factor at the identity cancels the endpoint means:
\[
 D_a\mathcal Q^1(I,0)a=L^{-4}\sum_{x\in B(c_-)}a([x,x'])=:Q^sa,
 \qquad\|Q^s\|_{\infty\to\infty}=L.                                    \tag{25}
\]
The upper bound counts \(L\) bonds per path; a constant form attains it. The finite analytic formula and Cauchy yield
\(|\mathcal Q^1(W,a)|\le L|a|[1+C_1L(|\omega|+|a|)]\) in a gauge \(W=e^{i\omega}\).
Let \(c\) bound the terminal normalized real curvature and \(\epsilon'\) the normalized complex reference perturbation. For \(t_n=L^{n-q}\), \(p_n=|a_n|/t_n\), changes of gauge and reference give
\[
 p_{n+1}\le p_n(1+C_2\epsilon't_n)^2
                 [1+C_3L(c\,t_n^2+p_nt_n)].
\]
Both \(\sum_{n<q}t_n\) and \(\sum_{n<q}Lt_n\) are uniformly bounded. Using \(1+x\le e^x\), choose \(c,\epsilon',\epsilon\) so that the product, under \(p_n\le2\epsilon\), is less than two. A first-crossing induction gives this bound at every level. Each block-factor logarithm is at most \(CL|a_n|\); summing proves (23). Apply this first relative to the real reference, then to the additional perturbation. All lower blocks and paths stay in the pillar; no folding extension is needed. ∎

**Lemma 4 (LEV).** Assume Lemma 3, the fixed weighted ceilings on \(A',\nabla^UA',\mathbf J\) from Section 2, and real cell gauges with
\(\xi_o|A^g|,\xi_o^2|\nabla A^g|<c_{\rm rt}\) on each positive-order turning cell \(B^o(a)\). A top is pinnable if its level \(q\ge2\), or if \(q=1\) and its \(2\eta\)-neighbourhood has only levels zero and one. For a pinnable top use cells \(B^{q-1}(a)\), \(a\in B(y)\); otherwise use \(B^1(y)\). Its read set \(\mathrm{Rd}(y)\) is the pillar bond set, enlarged by \(2\eta\) at pinnable level-one tops. A top is levelled when \(\widehat\epsilon_y=\xi_q\sup_{\mathrm{Rd}(y)}|H|<\epsilon_{\rm lev}\).

There is a Borel gauge \(u=I\) off the active endpoint set, with \(\operatorname{cn}(u)\le5/4\), and a shifted pair \(h^\delta=(H^\delta,K^\delta)\), such that
\[
 e^{i\eta H^\delta}\mathbf U=(e^{i\eta H}\mathbf U)^u,\qquad
 \mathbf J+K^\delta=\operatorname{Ad}(u)(\mathbf J+K).                    \tag{26}
\]
At levelled tops \(u(y)v_q(y)=I\). At pinnable levelled tops the fixed averaged stored transports are preserved. If \(n_b(h)\le A e^{-\mu d(b,S)}\), then
\[
 n_b(h^\delta)\le C_{\rm lev}A e^{-\mu d(b,S)/2},\qquad
 \widehat\epsilon_y\le K_{\rm pin}A e^{-\mu d(y,S)/2}.                    \tag{27}
\]
These constants are independent of depth and \(M,\bar\kappa\). Holomorphy at specified output bonds holds where every relevant endpoint top is levelled.

*Proof.* Write \(T_W(a)=(\mathcal M^{q-1}W)(y,a)\), \(E=e^{i\eta H}\mathbf U\), and prescribe
\[
 p(a)=T_{\mathbf U}(a)^{-1}v_q(y)^{-1}T_E(a),\qquad
 \zeta(a)=i^{-1}\log p(a)^{-1}.                                         \tag{28}
\]
At a nonpinnable top prescribe only \(p(y)=v_q(y)^{-1}\); put zero logarithms at unlevelled cells. Lemma 3 gives \(|\zeta|\le C_m\epsilon_y\).
On each positive cell choose the unique minimizer of \(\sum_x\|T(x)\|_{\rm HS}^2\), subject to \(T(a)=I\), \(\xi_o|\nabla^UT|\le1\), \(\xi_o^2|\nabla^U\nabla^UT|\le1\). The trial \(T_0(x)=\operatorname{Ad}(w(x)^{-1}w(a))\) is strictly feasible: normalized differences are bounded by \(2e^c c\) and \(2e^c c+4e^{2c}c^2\), both below \(1/2\) for small \(c=c_{\rm rt}\). Closed convex constraints, coercivity and strict convexity give existence and uniqueness. A four-dimensional centre path gives \(|T|<3\); its complexification has norm at most \(6\). Convex mixing with the strict trial gives continuity in \(U\); invariance of the minimization under orthogonal conjugation gives covariance.

Use \(\phi(s)=(1-9s^2)^3\) for \(|s|<1/3\), zero otherwise, and set
\[
 \mu(x)=\prod_{\nu=1}^4\phi((x_\nu-a_\nu)/\xi_o)T(x)\zeta(a),
 \qquad u=e^{-i\mu};                                                   \tag{29}
\]
at a singleton set \(\mu(a)=\zeta(a)\). Since \(|\phi'|,|\phi''|\le54\), the product rule gives
\[
 |\mu|\le6z,\quad\eta|\nabla^U\mu|\le C L^{-o}z,\quad
 \eta^2|\nabla^U\nabla^U\mu|\le C L^{-2o}z,\quad z=|\zeta(a)|.             \tag{30}
\]
The mixed difference has four terms: the second difference of \(T\), two products of first differences, and the second difference of the bump times \(T\). Extension by zero preserves these bounds because the support's two-step neighbourhood lies in the cell for \(L^o\ge13\). At singletons pinnability supplies the required low levels.

Define \(H^\delta\) by the logarithm of \(u_-e^{i\eta H}\mathbf Uu_+^{-1}\mathbf U^{-1}\); retain \(H\) itself when both turns equal \(I\). Transport four turn values to one base point. Expansion of the difference of the two exponential products, followed by the log series, gives
\[
 |\Delta\log|\le C\{|\Delta(\eta H)|+|\Delta_1\Delta_2\mu|
     +|\Delta_1\mu||\Delta_2\mu|+\eta|H||\Delta_1\mu|\}.                  \tag{31}
\]
Every mixed term contains either a mixed increment or both first increments. Changing transport from \(U\) to \(\mathbf U\) adds
\(C(\eta|A'|\,|\Delta\mu|+\eta^2|\nabla A'|\,|\mu|+\eta^2|A'|^2|\mu|)\), of the same scale. On positive cells \(q\le o+1\), so conversion costs at most \(L^2\); singleton stencils have only levels zero and one. The current is \(K\) plus the bounded conjugation change of \(\mathbf J\). Thus \(n_b(h^\delta)\le C_m\max_{y'\in\mathrm{nb}(y(b))}\|h\|_{y'}\).

Pillar diameters cost less than four, a \(2\eta\) displacement costs at most eight, neighbouring pillars at most 16 and their enlarged read sets at most 24. These bounds imply (27), after a fixed transport-norm conversion. Decreasing \(\epsilon_{\rm lev}\) places all touched logs in their branch and gives the condition-number bound.
At centres \(u(a)=p(a)\). Exact covariance of (5) gives
\(T_{E^u}(a)=u(y)T_E(a)u(a)^{-1}=T_{\mathbf U}(a)\).
This preserves the convention chosen in (28), not also a different comb convention. With the real frames fixed, the formulas are holomorphic on each forced-levelled set; finitely many cutoff patterns give Borel dependence. ∎

For ties, allow the pins to vary independently in twice their small balls; the same estimates hold. Two splittings of one real pair have the same prescribed centre values. Their turns differ by a real gauge equal to \(I\) at stored sites, so real gauge invariance and the tie identify their reads. Holomorphy continues that equality on a connected common-centre domain. A complex pair-function assertion additionally requires the pair-function hypothesis in §1; the core is not declared complex-gauge saturated.

## 5. Intrinsic backgrounds and the physical response

**Lemma 5 (P81 and intrinsic tube).** Under A1/F0/REG, every admitted separated determining system has one real regular critical orbit and its canonical comb representative. It has a holomorphic continuation \(\Phi_V(B)\) on \(\|B\|<r_B\), with actual datum \(e^{iB}V\), real at real \(B\), regular at \(C(\varepsilon+\|B\|)\), and with the local carrier gauges required by OPS. Restriction to a memberwise smaller separated sequence agrees, modulo its node-fixing gauge, when the restricted datum has radius \(CL^2\varepsilon\le\bar\varepsilon\).

On
\[
 \mathcal T_e=\{e^{iB}V:V\in\mathcal R_e\ {\rm real},\ \|B\|<\delta_B\},
                                                                            \tag{32}
\]
the canonical continuation is independent of the real centre. If \(\|B\|<\delta_B/2\), its datum has distance at least \(\delta_B/8\) from \(\mathcal T_e^c\), in the product matrix norm relative to \(SL(2,\mathbb C)^e\).

*Proof.* A1 supplies the orbit, its representative and local holomorphic chart. REG converts its local gauges to the declared carrier class, using only fixed \(O(M_1)\) enlargements and one adjacent-level factor \(L\); choose its radius after \(M_1\), not after \(M\). The restriction assertion is A1's restriction implication: fixing the finer determining data fixes the coarser data by iteration of (5), so a restricted critical field is critical for its own datum; AV/CURV bounds that datum and uniqueness identifies its orbit. This does not assert equality of two chosen representatives without their gauge.

For centre independence, if \(e^{iB_0}V_0=e^{iB_1}V_1\) with \(\|B_i\|<\delta_B\), then \(V_1V_0^{-1}\) has small logarithm of norm \(<3\delta_B\). The coordinate change
\(B\mapsto i^{-1}\log(e^{iB}V_0V_1^{-1})\) is holomorphic on the \(\delta_B\)-ball about zero and stays inside the \(r_B\)-ball. Both continuations agree for real \(B\) near zero by uniqueness of the canonical real representative. The identity theorem on this connected ball proves agreement at the given datum.
For tube room, write \(D=e^{iB}V\), \(\|B\|<\delta_B/2\). If \(\|D'-D\|<\delta_B/8\), then
\[
 \|D'V^{-1}-I\|\le e^{\delta_B/2}-1+\delta_B/8 .
\]
The log series majorant \(\sum_{n\ge1}r^n/n\), with \(\delta_B\le1/40\), is less than \(\delta_B\) at this \(r\) (use \(e^x\le(1-x)^{-1}\)). Its trace is zero since the determinant is one and the branch is near zero. Thus \(D'\in\mathcal T_e\). ∎

**Lemma 6 (CRIT, with the independent boundary current).** At a real regular critical \(U_0\), let \(F(A)=S_{\Omega_0}(e^{i\eta A}U_0)\), \(J=F'(0)\), \(\Delta=F''(0)\), and \(q(A)=\widehat QA+\mathcal C(A)\) be the nonlinear straightened constraint. Suppose
\[
 \mathbf J=J+\delta,\qquad
 \delta(b)=0\quad\text{if }b\text{ touches }\Omega_1.                    \tag{33}
\]
Under OPS/SLICE/UNQ and DR's specification below, the response at \(s=1\), with reduced source \(b_V(B)\), obeys
\[
 q(H)=b_V(B),\quad RD^{\mathsf T}H=0,\quad
 (e^{i\eta H}U_0)^{u_B}=\Phi_V(B),\quad u_Bv_q[H]=I\text{ at tops}.       \tag{34}
\]
For real \(B\) the pair and gauge are real. Its independent current obeys
\[
 \mathbf J+K=J^\circ(e^{i\eta H}U_0)+f_H^{-1}\delta,\qquad
 f_H=f(-i\eta\operatorname{ad}H),\quad f(z)=(e^z-1)/z.                   \tag{35}
\]
Changing the initial current by \(\delta\) leaves \(H\) unchanged and changes \(K\) by \(f_H^{-1}\delta-\delta\). On a bare determining row,
\[
                         H(b)=\eta^{-1}B(b).                           \tag{36}
\]
For the plain current, \(K=0\) at incomplete stars if the raw source is zero on all bare bonds meeting the \(2\eta\)-neighbourhood of \(\partial\Omega_0\).

*Proof.* We give the finite algebra, since “criticality at \(s=1\)” does not specify a response. Fine and site pairings include \(\eta^4\); row pairings are unweighted sums of \(\frac12\operatorname{tr}\). All complex transposes are bilinear. Put
\(D\chi(b)=\eta^{-1}[\operatorname{Ad}(U_0(b))\chi(b_+)-\chi(b_-)]\).
Here \(Q'\) is the scalar pillar mean induced by the actual node-factor linearization, \(\Delta_{\rm site}\) is its covariant Dirichlet scalar Laplacian (diagonal \(8\eta^{-2}\)), and \(a,\widehat a\) are the fixed positive diagonal masses in the declared scalar and raw-row pairings. Their normalization is part of M1/OPS. Set
\[
\begin{gathered}
 G'=(\Delta_{\rm site}+Q'^{\mathsf T}aQ')^{-1},\quad
 R=I-G'Q'^{\mathsf T}(Q'G'^2Q'^{\mathsf T})^{-1}Q'G',\\
 \lambda_A=G'RD^{\mathsf T}A,\quad \Pi A=A-D\lambda_A,\quad
 \lambda_A^+(b)=\operatorname{Ad}(U_0(b))\lambda_A(b_+).
\end{gathered}
\]
Specify the independent-current continuation by
\[
\begin{split}
\langle A,\Delta'_\pi[\mathbf J]C\rangle
=\tfrac12\langle&
i[\lambda_A,C]+i[\lambda_C,A]
-i[A,\lambda_C^+]-i[C,\lambda_A^+]\\
&-i[\lambda_A,D\lambda_C]-i[\lambda_C,D\lambda_A],\mathbf J\rangle .
\end{split}                                                            \tag{37}
\]
Let \(\Delta_\pi=\Delta-\Delta'_\pi[\mathbf J]\), and define in this order
\[
\begin{gathered}
G=(\Delta_\pi+DRD^{\mathsf T}+\widehat Q^{\mathsf T}\widehat a\widehat Q)^{-1},
\quad \Sigma=(\widehat QG\widehat Q^{\mathsf T})^{-1},
\quad \ell=G\widehat Q^{\mathsf T}\Sigma,\\
\langle A,\Delta^{(2)}[\zeta]A\rangle=2\langle\mathcal C^{(2)}(A),\zeta\rangle,
\quad
G_1=(G^{-1}-\Pi^{\mathsf T}\Delta^{(2)}[\ell^{\mathsf T}\mathbf J]\Pi)^{-1},\\
\ell_1=G_1\widehat Q^{\mathsf T}
       (\widehat QG_1\widehat Q^{\mathsf T})^{-1},\quad
\mathfrak G=G_1-G_1DRD^{\mathsf T}G_1-\ell_1\widehat QG_1 .
\end{gathered}                                                          \tag{38}
\]
Here \(\widehat a\) is the row mass in raw row units. Invertibility is OPS.

Put \(\mathcal N=\ker Q'\), \(\mathrm{Sl}=\ker RD^{\mathsf T}\), \(\mathcal K=\ker\widehat Q\cap\mathrm{Sl}\). The displayed projection gives \(Q'G'R=0\), \(\operatorname{ran}R=\Delta_{\rm site}\mathcal N\) and \(\lambda_{D\chi}=\chi\) for \(\chi\in\mathcal N\). At sites with a missing neighbour, \(\chi=0\), since such sites are level-zero tops. Thus the four-dimensional boundary term \(\eta^{-2}(8-n(x))\chi(x)\) vanishes. Differentiating the exact gauge covariance and endpoint factors of the straightened average gives \(\widehat QD\chi=0\) on \(\mathcal N\), also at outward rows; the induced scalar mean at an outer endpoint is evaluated at its own level. This is the SLICE factorisation, not the false identity for the plain average.

Expand the gauge coordinate:
\[
 A^v=A-Dv+\tfrac12\{i[v_-,A]-i[A,v_+]-i[v_-,Dv]\}+O(3).
\]
Gauge invariance of the inner-plaquette action, comparison of the first two homogeneous degrees, and polarization give
\(D^{\mathsf T}J=0\) and \(\Delta-\Delta'_\pi[J]=\Pi^{\mathsf T}\Delta\Pi\).
If \(\delta\) satisfies (33), both endpoint values of every \(\lambda_A\) vanish on its support, so \(\Delta'_\pi[\delta]=0\).
Consequently direct multiplication in (38) gives
\[
\begin{gathered}
G_{(1)}DR=DG'R,\quad RD^{\mathsf T}\ell_{(1)}=0,\quad
\widehat Q\mathfrak G=RD^{\mathsf T}\mathfrak G=0,\\
\mathfrak G\widehat Q^{\mathsf T}=\mathfrak GDR=0,\quad
\mathfrak GG_1^{-1}|_{\mathcal K}=I,\quad
\Delta_\pi\ell=\widehat Q^{\mathsf T}(\Sigma-\widehat a).
\end{gathered}                                                          \tag{39}
\]
For example \(G_{(1)}^{-1}D\chi=D\Delta_{\rm site}\chi\) on \(\mathcal N\); taking \(\chi=G'Rf\) proves the first identity. Substitution in \(\mathfrak G\) proves its annihilations and inverse property. Its symmetry follows from the symmetry of both subtracted terms.

Solve \(X=\mathcal C(A'-\ell X)\) by UNQ, writing \(X=\mathcal D(A')\), \(T=\mathcal L(A')=A'-\ell\mathcal D(A')\). Then
\[
 q(\mathcal L(A'))=\widehat QA',\quad
 \mathcal L'=(I+\ell\mathcal C'_T)^{-1},\quad
 \mathcal L'\mathcal K=\ker q'(T)\cap\mathrm{Sl}.                         \tag{40}
\]
Set \(R_F(A)=F(A)-F(0)-\langle J,A\rangle-\frac12\langle A,\Delta A\rangle\), and define the actual reduced action
\[
\begin{split}
 V_{\mathbf J}(A')={}&-\langle\ell^{\mathsf T}\mathbf J,\mathcal D(A')-\mathcal C^{(2)}(A')\rangle
 -\langle\widehat QA',(\Sigma-\widehat a)\mathcal D(A')\rangle\\
 &+\tfrac12\langle\mathcal D(A'),(\Sigma-\widehat a)\mathcal D(A')\rangle
 +R_F(\mathcal L(A')). 
\end{split}                                                            \tag{41}
\]
The required **specification at one** is
\[
 W_1=V'_{\mathbf J},\quad A_\bullet=\ell_1B'+A,\quad
 A=-\mathfrak GW_1(A_\bullet),\quad H=\mathcal L(A_\bullet),               \tag{42}
\]
and
\[
 \omega_1(T;\mathbf J)
 =(I+\ell^{\mathsf T}\mathcal C'_T{}^{\mathsf T})^{-1}
       \ell^{\mathsf T}(F'(T)-F'(0)+\mathbf J),\qquad
 j_1(T)=f_T^{-1}q'(T)^{\mathsf T}\omega_1
                -\widehat Q^{\mathsf T}\ell^{\mathsf T}\mathbf J.        \tag{43}
\]
These finite formulas specify what DR must resum to. They do not prove the weighted estimates for a decoupling of them.

At \(\mathbf J=J\), insertion of \(T=A'-\ell\mathcal D\), (39), and the quadratic term of \(\mathcal C\) gives on \(\mathrm{Sl}\)
\[
 F(\mathcal L(A'))=F(0)+\langle J,A'\rangle
 +\tfrac12\langle A',\Delta_1A'\rangle+V_J(A'),\quad
 \Delta_1=G_1^{-1}-DRD^{\mathsf T}-\widehat Q^{\mathsf T}\widehat a\widehat Q.
                                                                            \tag{44}
\]
The cross term is \(-\langle\widehat QA',(\Sigma-\widehat a)\mathcal D\rangle\); the \(\mathcal D^2\) term and the linear-current subtraction are exactly the other terms of (41). Differentiating (44) and using (39) shows that stationarity on \(\ker q'(T)\cap\mathrm{Sl}\), with \(q(T)=B'\), is equivalent in the contraction ball to (42). Criticality supplies a multiplier: the SLICE chart takes curves in the straightened fibre to curves in the actual fibre by their node gauges, so the derivative annihilates its tangent kernel; surjectivity of \(q'(T)\) identifies its annihilator with \(\operatorname{ran}q'(T)^{\mathsf T}\).

Near real zero the local Landau pair from SLICE is critical, so (40)–(44) and UNQ identify it with the response. Holomorphy extends the potential and multiplier identities to the common connected datum ball. The gauge also extends: in each component choose a top as root and a spanning tree; set \(u(y_0)=v(y_0)^{-1}\), and along \(b=(x,x')\) define
\(u(x')=\Phi_V(B)(b)^{-1}u(x)(e^{i\eta H}U_0)(b)\).
This is holomorphic. The non-tree bond and remaining top identities hold near real zero and hence throughout the ball. This proves (34) without asserting a complex norm bound from real unitarity.

Finally \(F'(T)=f_TJ^\circ(e^{i\eta T}U_0)\), by differentiating the exponential and using the bilinear transpose. The series for \(f\) is invertible in the small ball. Criticality in the straightened fibre implies \(J=\widehat Q^{\mathsf T}\ell^{\mathsf T}J\): the derivative annihilates \(\ker\widehat Q\), and \(\widehat Q\ell=I\). At the natural current, (43) therefore gives \(J+j_1=J^\circ(E)\). On bare rows \(q(A)=\eta A\), so \(\mathcal C\) and all its derivatives vanish there. For \(\zeta=\ell^{\mathsf T}\delta\), the **four-dimensional** fine volume and unweighted row pairing give
\[
 \zeta(c)=\eta^3\delta(c)\text{ on bare rows},\quad
 \widehat Q^{\mathsf T}\zeta=\delta,\quad
 \mathcal C'_T{}^{\mathsf T}\zeta=\Delta^{(2)}[\zeta]=0.
\]
Thus all operators and (41)'s derivative are unchanged, while (43) changes by the term in (35). Equation (36) follows from (34). If the source avoids the specified boundary neighbourhood, all bonds of each remaining plaquette of an incomplete star have \(H=0\); its regional current is unchanged. With \(\delta=J_+-J^\circ(U_0)\), (35) then gives \(K=0\) there. Merely saying the source is “interior” would not prove this. ∎

## 6. Towers and outer-core substitution

**Lemma 7 (local substitution estimates).** Put \(D=A''-A'\) in (10). On a sufficiently small fixed value ball,
\[
\begin{split}
 \eta|D|&\le5\eta|H|,\\
 \eta^2|\nabla^UD|&\le13\eta^2|\nabla^UH|
                          +96\eta|H|\eta^2|\nabla^UA'|,\\
 |\partial(e^{i\eta H}\mathbf U)-\partial\mathbf U|
 &\le2^{12}\{\eta^2g+\eta h(\eta h+\eta a+|\partial\mathbf U-I|)\}.
\end{split}                                                            \tag{45}
\]
Here \(h,g,a\) are the maxima of \(|H|,|\nabla^UH|,|A'|\) on the contained plaquette stencils. In the constant-scale core, if \(\eta\le1/13\), \(|A'|,|\nabla^UA'|\le\beta_1\), \(|\partial\mathbf U-I|\le\beta_0\eta^2\), \(|H|,|\nabla^{\mathbf U}H|\le s\), and \(\beta_0,\beta_1,s\le1/60\), the sharper sufficient bounds are
\[
              |D|,|\nabla^UD|\le2s,\qquad
 |\partial(e^{i\eta H}\mathbf U)-\partial\mathbf U|\le4s\eta^2.          \tag{46}
\]

*Proof.* Expand exponentials absolutely and then \(\log(I+Z)\) on \(|Z|<1\). For \(\ell(X,Y)=\log(e^Xe^Y)-X-Y\), the geometric series gives \(|\ell|\le12(|X|+|Y|)^2\) on \(|X|+|Y|\le1/4\). Cauchy's estimate on a smaller ball, followed by the zero \(\ell(0,Y)=0\), gives
\(|\ell(X,Y)-\ell(X,Y')|\le96|X||Y-Y'|\) on the \(1/16\)-ball. Split a transported difference first in \(X=i\eta H\), then in \(Y=i\eta A'\). Decrease the fixed ball so the first-variable derivative is at most \(5\); this proves the first two bounds in (45), with room for neighbouring value bounds.

For a plaquette with positively oriented edges \(1,2\) and reversed edges \(3,4\), write \(P=\partial\mathbf U\) and move all four exponentials left. Their generators are
\[
 H_1,\quad\operatorname{Ad}(\mathbf U_1)H_2,\quad
 -\operatorname{Ad}(P\mathbf U_4)H_3,\quad-\operatorname{Ad}(P)H_4.
\]
Their sum is
\(\eta(\nabla^{\mathbf U}_\mu H_\nu-\nabla^{\mathbf U}_\nu H_\mu)
 (I-\operatorname{Ad}P)(\operatorname{Ad}(\mathbf U_4)H_3+H_4)\).
Also \(|\nabla^{\mathbf U}H-\nabla^UH|\le2.1a h\) on the chosen ball. The remainder of the four exponential products is bounded by
\(\frac12(\sum|X_i|)^2e^{\sum|X_i|}\). These estimates give (45).

For (46), set \(\epsilon_*=1/380\); both \(e^{i\eta H}e^{i\eta A'}\) and \(e^{i\eta A'}\) are in the \(\epsilon_*\)-ball about \(I\). The logarithm has Lipschitz constant \((1-\epsilon_*)^{-1}\), giving \(|D|<1.1s\). For its difference, let \(E_j=e^{a_j}e^{c_j}\), \(F_j=e^{c_j}\), \(D_j=E_j-F_j\) at the two transported endpoints. Telescoping the logarithm series gives
\[
 |(\log E_2-\log F_2)-(\log E_1-\log F_1)|
 \le\frac{|D_2-D_1|}{1-\epsilon_*}
 +\frac{(|E_2-E_1|+|F_2-F_1|)|D_1|}{2(1-\epsilon_*)^2}.
\]
Use \(|c_2-c_1|\le\eta^2\beta_1\),
\(|a_2-a_1|\le\eta^2s[1+2\beta_1(1+\epsilon_*)]\), and
\(|D_1|\le(1+\epsilon_*)\eta s\). Dividing by \(\eta^2\), the right side is \(<2s\), using only \(\eta\le1/13\) and \(\beta_1,s\le1/60\). In the plaquette calculation the four transported generators have norm \(<1.01s\), their sum has norm at most \(\eta s(2+4.1\beta_0\eta)\), and the exponential remainder is at most \(8.3\eta^2s^2\). Thus the curvature increment is at most
\((1+\beta_0\eta^2)\eta^2s(2+4.1\beta_0\eta+8.3s)<4s\eta^2\). These are dimension-free single-plaquette calculations. ∎

**Lemma 8 (ambient tower estimate).** Let an ambient separated sequence have scale \(l(x)\), and let a separated subordinate sequence of depth \(p\) have scale \(\xi'(x)\le l(x)\). A tower element at \(x\) is **settled** if the two sequences agree in the \(l(x)\)-neighbourhood of its stencil, or the subordinate sequence has reached its final level throughout that neighbourhood. Put \(s(x)=l(x)/\xi'(x)\). Define
\[
\begin{split}
 n(w;b)&=\max\{l(b)|w(b)|,l(b)^2|\nabla^Uw(b)|\},\\
 E_w^a(x)&=\max_b e^{-ad(x,b_-)}n(w;b),\\
 E_U^a(x)&=\max_\pi e^{-ad(x,x_\pi)}
                    l(x_\pi)^2\eta^{-2}|\partial U(\pi)-I|.
\end{split}                                                            \tag{47}
\]
The tower quantities are
\[
 G(U,w;e)=l(x)^2\eta^{-2}(\partial T_e-I)
       \quad\hbox{or}\quad l(x)^2\xi'(x)J_{\rm bare}(T_e).              \tag{48}
\]
Assume \(E_U^0,\sup n(w)\le a_T\). From AV/CURV, PROF, (15), Lemmas 2–3 and P81, fixed \(K_a,K_T,a_T>0\) can be chosen, independently of depth, volume, \(M,\bar\kappa\), so that
\[
 |G(U,w;e)|\le K_a(E_U^{\delta_T}+E_w^{\delta_T})(x)\le1,\qquad
 |G(U,w_1;e)-G(U,w_0;e)|\le K_TE_{w_1-w_0}^{\delta_T}(x).               \tag{49}
\]
The towers exist on open continuation domains with tube room \(\delta_B/8\), are holomorphic at fixed real \(U\), and at real \(w\) equal the canonical real backgrounds of their actual averaged data.

For a meet with either erosion tower of \(Z\), (49) holds at every complete element of \(Z^{\wr p}\). Replacing sites by their ambient tops costs **\(e^{4\delta_T}\)**.

*Proof.* This gives the argument behind the estimate, including the scale cancellation. First, the real average is regular: iterate CURV on each double block, as in Lemma 3, using the local bound \(l^2\eta^{-2}|\partial U-I|\le a_T\); at a seam pay \(C_{\rm sm}L^2\). For real \(w\), (45), AV and PROF give
\[
 |G(U,w;e)|\le C_R\{E_U^{\delta/2}(x)+E_w^{\delta/2}(x)\}.             \tag{50}
\]
To check the weights, the change of scale between two read sites is at most \(L^{2+2d'/\rho_0}\) by (21); its fourth power costs at most a fixed \(L\)-factor times \(e^{8(\log L)d'/\rho_0}\). The chosen \(\rho_0\) leaves at least half the profile decay. Stencils and double blocks have bounded weighted diameter. The linear term of (45) contributes \(n(w)\); its quadratic terms are absorbed by the fixed small ceiling. This proves (50) without a depth-dependent factor.

Let \(B(w)\) be the **raw** datum (6), \(\|w\|'=\max_b\xi'_-(b)|w(b)|\), with \(\xi'_-\) the smaller endpoint scale. AV and Cauchy's estimate on its half-ball give a fixed \(r_w>0\) with
\[
 \|B(w)\|_\infty<r_T<r_B/2\quad(\|w\|'<r_w),\qquad
 |\Delta B(c)|\le2C_QL
       \max_{b\in D(c)}s(b)^{-1}l(b)|\Delta w(b)|.                     \tag{51}
\]
Here \(r_T\) is reduced below every local derivative and gauge ceiling. The carrier comparison used is \(\xi_q\le L\xi'(b)\) and \(\xi'_-(b)\ge\xi'(b)/L\). Thus \(T=\Phi(B(w))\) exists on that value ball.

Put \(\mathcal F=s^{-2}G\), normalized at the subordinate scale. Integrate (15) along a datum segment. The current estimate follows from its current member. For curvature, the infinitesimal left velocity of
\(W(B)=e^{i\eta H(B)}U_0\) is
\[
 V_B=\int_0^1\operatorname{Ad}(e^{it\eta H(B)})\dot H(B)\,dt,
\]
not \(\dot H(B)\). Its value and first covariant difference are bounded by a fixed multiple of those of \(\dot H\), plus the product of \(\eta|\dot H|\) with the first difference of \(H\). Equation (15) and a fixed small bound on \(H,\nabla H\) control this product. Apply the differential version of (45) to \(V_B\). This corrects the draft's noncommuting-exponential differentiation.

The canonical gauge at a site \(x\) in a pillar with top \(y\) is the product of its top block factor and the successive comb transports from block centres to \(x\). The exact recursion is \(u_B(x)=u_B(z)(\mathcal M^nW_B)(\Gamma_{z,x})\). At level \(n<q\) there are at most \(2(L-1)\) bonds, and
\(\sum_{n<q}2(L-1)\xi_n\le2\xi_q\). Lemma 3 and AV therefore give
\[
 |u_B(x)^{\pm1}-I|\le C_u\xi_q\sup_{\text{pillar}}|H|,\quad
 |\Delta u_B(x)|\le C'_u\xi_q\sup_{\text{pillar}}|\Delta H|
\]
on a fixed smaller ball. This supplies the needed bound at non-top sites; a top-only estimate would not suffice. Conjugate the Landau estimates by this gauge. The row sum (22), after decreasing \(r_T\), gives
\[
 |\mathcal F(B)|\le3/2,\quad
 |\mathcal F(B_1)-\mathcal F(B_0)|
 \le(C_X+C_h|\mathcal F(B_0)|)
          \sum_c e^{-\delta d'(x,y_c)}|\Delta B(c)|.                   \tag{52}
\]
All constants used here depend on earlier inputs only.

Choose a piecewise linear \(\chi\), equal to one within distance \(l(x)\) and zero beyond \(2l(x)\). On its stencil support, \(l(b)/l(x)\in[L^{-1},L]\). With \(C_\chi=1+L^2\) and \(n_{\rm nr}\) the maximum over distance \(3l(x)\),
\[
 n(\chi v)\le C_\chi n_{\rm nr}(v),\quad
 \|\chi v\|'\le L^2s(x)^{-1}n(\chi v),\quad
 n_{\rm nr}(v)\le e^{12L\delta_T}E_v^{\delta_T}(x).                    \tag{53}
\]
The middle bound uses settlement if \(s(x)>1\). If a holomorphic \(F\) is bounded by \(M_0\) on a radius-\(r\) ball, its Taylor series on complex lines yields
\[
 |F(z)|\le3|F(0)|+|F(\Re z)|+|F(\Im z)|
                           +6M_0\|z\|^2/r^2 \quad(\|z\|\le r/2).
\]
Apply this to \(F(w)=G(U,w;e)\), for which (52) gives \(M_0=3s(x)^2/2\). The factor \(s(x)^2\) cancels the \(s(x)^{-2}\) in (53). The remainder is at most \(9L^4 n(\chi w)^2/r_w^2\), hence a fixed multiple of \(n(\chi w)\). Use (50) on \(\Re(\chi w)\) and \(\Im(\chi w)\).

For a far change \(v\), vanishing within \(l(x)\), put \(D=d'(x,b_-)\). Settlement gives \(s(x)\le1+D\), and (21) gives
\[
 \frac{s(x)^2}{s(b)}\le(1+D)L^2e^{\delta D/32}.
\]
Use (51)–(52); the carrier is within a fixed \(6L\) of \(y_c\). Split the remaining exponential into shares \(8/32,8/32,15/32\), after paying \(1/32\) for the scale quotient. The first absorbs \(1+D\), since \((1+D)e^{-\delta D/4}\le4/\delta\); the second leaves \(e^{-\delta_TD}\); the last sums by (22). Consequently
\[
 |F(w)-F(\widetilde w)|
 \le(C_X+C_h|F(\widetilde w)|)C_{\rm far}E_{w-\widetilde w}^{\delta_T}(x).
                                                                         \tag{54}
\]
Combining near and far bounds chooses \(K_a\); then a fixed small \(\bar a\) ensures \(|F|\le1\).

For Lipschitz continuity, split \(v=w_1-w_0=\chi v+(1-\chi)v\). The far part is (54). For the near part put \(n_v=C_\chi n_{\rm nr}(v)\), \(E=E_U^{\delta_T}+E_{w_0}^{\delta_T}\). If \(E>0\), on the disc \(|z|<1+E/n_v\) the size estimate bounds \(F(w_0+z\chi v)-F(w_0)\) by \(4K_a(1+E/n_v)n_v\), provided \(a_T\le\bar a/(5C_\chi^2)\). Schwarz's lemma at \(z=1\) gives \(4K_an_v\). If \(E=0\), the size bound itself gives the result; the case \(n_v=0\) is immediate. This proves (49).

AV also gives \(\|B(w)\|<C_QL\bar a<\delta_B/4\), so Lemma 5 gives tube room. The eroded interior is settled because
\(2M\xi_{p-1}-2\xi_p>3M'_1\xi_p\) under \(M\ge L^4M'_1\). Moving each of two sites to its top costs less than \(2\), by Lemma 2, and gives \(e^{4\delta_T}\). The two definitions of the localized tower have the same actual datum; real uniqueness and the identity theorem identify their holomorphic continuations. ∎

**Lemma 9 (CORE).** Let \(i\ge1\), \(0<\tau<1\), \(0<b_0\le b_1\), \(2(b_0+b_1)\le a^\sharp\), and \(c_\natural\ge1\). Suppose
\[
 P\in\mathcal U_i^\circ(X;(1-\tau)b_0,(1-\tau)b_1),\quad
 |H|,|\nabla^{\mathbf U}H|<
 s:=\frac{\tau b_0}{18K^\sharp(1+c_\natural)},\quad
 |\mathbf J+K|<b_0.                                                    \tag{55}
\]
Then \(P\dotplus h\in\mathcal U_i^\circ(X;b_0,b_1)\), with the stated pair and fixed real factor, holomorphically on its fixed-real-factor fibre.

*Proof.* Equation (46) gives potential increments at most \(2s\) and curvature increment at most \(4s\eta_i^2\). Since \(s\le\tau b_0/36\), these are smaller than the available simple gaps. The real curvature and real gauge witnesses are unchanged, and their old bounds are stricter; the current is the last hypothesis in (55).

Fix \(Z,p,n\) in (12), and put \(\lambda_p=L^{-(i-p)}\). On \(Z\subset\Omega_i\) the ambient sequence truncated at \(p\) has scale \(\lambda_p\) in level-\(i\) units. Its meet with the erosion sequence is exactly the core's determining system. Its quantities (48), in level-\(n\) units, are
\[
             L^{2p}(\partial T_n-I),\qquad L^{2(p-n)}J_n(T_n).
\]
Thus (12) says precisely \(|G|<b_0\lambda_p\). Both \(A'\) and \(A''\) satisfy Lemma 8's absolute hypotheses, by (46) and \(2(b_0+b_1)\le a^\sharp\). Its open-domain statement supplies existence, not just formal bounds. Moreover
\[
 |\Delta G|\le e^{4\delta_T}K_T
       \max\{\lambda_p|D|,\lambda_p^2|\nabla^UD|\}
 \le2K^\sharp\lambda_p s<\tau b_0\lambda_p.
\]
Every complex tower therefore has room; every real tower is unchanged. Holomorphy follows from the logarithm and the continued towers. No bound on \(b_1^2/b_0\) was used. ∎

## 7. Formation, inherited domains and the actual fibre

**Lemma 10 (what the real tests admit).** In an operation of level \(t\), put \(k_\sharp=t-N_t^0\), \(N_t^0\ge2\), with \(L^{N_t^0-1}=R_{k_\sharp+1}\). For original layer \(l\), define
\[
 e_j(x)=
 \begin{cases}
 0,&j\le k_\sharp,\\
 (j-l(x)-1)_+,&j>k_\sharp,\ k_\sharp<l(x)\le j,\\
 j-k_\sharp-1,&j>k_\sharp,\ l(x)\le k_\sharp.
 \end{cases}
\]
On the set raised to level \(j+1\) set the raw exponent \(\mathcal E=e_j+1\); inherit it elsewhere. At the output use \(e_{t-1}+1\) on newly healed points. Outside these sets use the declared formation exponents. Assume the inherited exponents, as well as newly set ones, obey
\[
 L_\flat^{2\mathcal E(x)}\le C_R^2(\log\theta_{m(x)})^{2r_R},\qquad
 \lambda(x)=\max_z L_\flat^{2\mathcal E(z)}e^{-\delta d(x,z)/4}.          \tag{56}
\]
Every newly set exponent is at most \(N_t^0-1\). The lift satisfies
\[
 1\le L_\flat^{2\mathcal E(x)}\le\lambda(x),\quad
 \lambda(z)\le e^{\delta d(x,z)/4}\lambda(x),\quad
 \lambda(x)\le C_\lambda(\log\theta_{m(x)})^{2r_R}.                    \tag{57}
\]
Suppose each tested datum loop obeys
\[
 |\partial V(\tau)-I|\le C_{\rm te}L_\flat^{2\mathcal E(\tau)}
                         \varepsilon_{m(\tau)},\quad
 C_{\rm te}=6C_{\rm sm}L^4.                                           \tag{58}
\]
Then the actual regular critical background at this structure satisfies, at complete elements,
\[
 l^2\eta^{-2}|\partial U-I|,\quad l^3|J^\circ_\eta(U)|
 \le C_{\rm RA}\lambda(x)\varepsilon_{m(x)},\qquad
 C_{\rm RA}=2C_PC_{\rm te}.                                           \tag{59}
\]
The pointwise, absolute and tower records at formation, and their prescribed gauge families, are admitted with every base radius multiplied by \(c_{\min}/4\), subject to the stated carrier and smallness conditions. **The core records require the additional comparison described below.**

*Proof.* The exponent bound follows from \(j\le t-1\), and from \(N_t^0\ge2\) when \(j\le k_\sharp\). It is a bound on newly assigned values, not on arbitrary inherited values. The first two parts of (57) follow from the maximum and the triangle inequality. For the last, write \(D=d(x,z)\), \(m=m(x)\), \(q=m(z)\). RUN gives
\(\theta_q\le\theta_m+C_\theta|q-m|\), and (20) bounds \(|q-m|\le1+D/\rho_0\). Since \(\theta_m\ge e\),
\[
 (\log\theta_q)^{2r_R}
 \le C(\log\theta_m)^{2r_R}(1+D)^{2r_R}.
\]
The supremum of \((1+D)^{2r_R}e^{-\delta D/4}\) is finite. This proves the global smoothed-lift ceiling from the local raw-lift ceiling.

For (58), an unchanged label row uses its inherited test. A row raised from \(j\) to \(j+1\) pays the conversion
\[
 3L^2L_\flat^{2e_j}\varepsilon_j
 \le6L^2L_\flat^{-2}L_\flat^{2(e_j+1)}\varepsilon_{j+1};
\]
AV/CURV adds at most \(C_{\rm sm}L^2\). The exponent of a retained shell is no larger than the value assigned at the last stage that raised it, by the prepared nesting in Lemma 2. These are the three stage cases of SA 17624. Thus the stage tests imply (58); output boxes are addressed separately below. PROF, (57), and
\(\varepsilon_{m(\tau)}/\varepsilon_m\le2^{|m(\tau)-m|}
\le2e^{\delta d(x,\tau)/4}\)
give (59), leaving positive exponential decay.

Here is the gauge argument with its carrier requirement. For a recorded cube \(Q\) of side \(s\) in level-\(i\) units, require its side-\((s+6)\) enlargement to lie in the supplied region and in layers at least \(i-1\). Set \(\Lambda_Q=\sup_{Q^+}\lambda\). From (59), the curvature on it is \(<wL^2\eta_i^2\), with \(w=2C_{\rm RA}\Lambda_Q\varepsilon_{i-1}\). The Wilson divergence differs from \(\eta_i^2J^{(i)}\) by at most six quadratic plaquette terms, so
\[
 |D_U^{\mathsf T}\partial U|
 \le6\eta_i^{-1}(wL^2\eta_i^2)^2+\eta_i^2|J^{(i)}|
 <2L^3w\eta_i^2
\]
after the fixed smallness ceiling. RCG4 gives
\[
 |A|,|\nabla A|<16L^3B_*(s+2)C_{\rm RA}\Lambda_Q\varepsilon_i.          \tag{60}
\]
For large, CA-I and core cube families, divide by their factors
\(\mathsf oLMB^{cg},BM,C_{\rm pot}M\); \(s\) is bounded by a fixed multiple of \(M\), so the quotient is bounded independently of \(M\). For natural cubes \(s\le12M_1\); choose the containing cube to be \(Q\) itself. Choose \(C_{\rm mb}\) above these finitely many quotients. The hypotheses needed are
\[
 8L^3(s+2)C_{\rm RA}\Lambda_Q\varepsilon_{i-1}<c_{\rm rg},\qquad
 C_{\rm mb}C_{\rm RA}\Lambda_Q\varepsilon_i<a_\flat/4.                 \tag{61}
\]
They follow by decreasing \(\gamma\) after \(M\), using (57). At level zero use \(\varepsilon_0\) in place of \(\varepsilon_{i-1}\) and impose \(w\le1/(12L)\). Then \(6wL\eta_i\le1\) also for \(\eta_0=1\), so the same divergence estimate and RCG4 apply.

The four CA-I families in 48527–48565 have printed exponents
\((m-k_0)_+,(p-k_0)_+,p-\bar m,0\). Equation (60) uses the recorded supremum \(\Lambda_Q\), which can exceed those printed lifts. It proves the stated witness clauses, not the original printed consumer bounds. For pointwise formation, the floor in row 5 gives
\(C_{\rm RA}\lambda\varepsilon_m\le c_{\min}^2\lambda\alpha_0\varepsilon_m/16\).
This pays the \(c_{\min}/4\) multiplier **and** the current coefficient \(c_\sigma\ge c_{\min}\); the draft paid only one of these two factors. Potential reads vanish at the plain triple. Incomplete-star plain currents vanish by definition. The absolute ceiling follows from row 10.

For tower formation, restriction makes the real tower a real gauge transform of the restricted background. At \(\ell=\min(m,i)\),
\(\varepsilon_mL^{-2m}\le\varepsilon_\ell L^{-2\ell}\) and
\(\varepsilon_mL^{-3m}\le\varepsilon_\ell L^{-2\ell-\min(q,\ell)}\);
the same pointwise lift occurs on both sides of (14). This proves its formation bounds. AV and P81 supply the open datum domain and tube room. ∎

**Outstanding R (minimum-lift core formation).** The bound (59) is pointwise in \(\lambda(x)\). A core radius is
\(\alpha_\iota\varepsilon_i\inf_X(c_\sigma(x|i)\lambda(x))\).
The draft's Proposition 5′ infers the latter from the former without comparing their lifts. Even for \(m(x)=i\), slow variation yields only
\(\sup_X\lambda/\inf_X\lambda\le e^{\delta\,\operatorname{diam}_d(X)/4}\), which is not a fixed constant on arbitrary core addresses. The same issue affects core gauges: (60) uses \(\Lambda_Q\), whereas (11)'s core gauge uses the single core \(b_0\). A sufficient repair would prove, on every core read and gauge carrier,
\[
 \lambda(x)\varepsilon_{m(x)}L^{-a(m(x)-i)}
 \le C_{\rm c}\varepsilon_i\inf_X\lambda,\qquad a=2,3,                \tag{62}
\]
with \(C_{\rm c}\) fixed before \(\kappa\), and the corresponding enlarged-cube bound. Then (59)–(60), restriction and a fixed increase of the radius floor prove core formation. Neither (56) nor the quoted real tests prove (62). Replacing the infimum by a supremum changes the consumer domain and requires its own verification. The conditional theorem below names core formation explicitly.

**Outstanding B (output and consumer formation).** BOX is still an input at the output of an operation. Its displayed condition
\(C(M)\le c_{\min}\alpha_0L_\flat^{2(N_t^0-1)}/4\)
does not by itself imply (58), whose constant \(C_{\rm te}\) is independent of \(\alpha_0\), nor does an upper bound on \(N_t^0\) show that decreasing \(\gamma\) enforces it. Supply the appropriate BOX admission inequalities directly, or a lower-growth bound and the necessary comparison. Also verify the activity consumers for the enlarged CA-I witness radii and the retained chain of reads. These are separate from the proved gauge estimate.

**Lemma 11 (half-gap substitution and conditional drift).** For compatible records (13), define
\[
 \|h\|_w=\max_b\frac{\max\{l_+(b)|H|,l_+(b)^2|\nabla^UH|,
                                      l_+(b)^3|K|\}}{w(m_+(b))}.       \tag{63}
\]
Use the input sequence for \(l_+,m_+\). Assume all the absolute ceilings and witness carriers of Section 2, and that on active bonds \(A'\) is in the small logarithm chart. There are fixed constants, for example after fixed increases of
\[
 K_{\rm pt}=2^{15},\quad K_{\rm tw}=32e^{4\delta_T}K_T,\quad
 K_{\rm core}=8L^3C_{\rm os}K^\sharp(1+c_\natural)/c_{\min},            \tag{64}
\]
such that \(r=\|h\|_w\le r_*\) implies
\[
        P\in\mathcal D_{a|+}\quad\Longrightarrow\quad
        P\dotplus h\in\mathcal D_{a|-},                               \tag{65}
\]
with at least half of every gap left. This holds also for a pinned shift satisfying (63). The real witnesses remain unchanged.

Suppose in addition that every record is admitted at formation with base multiplier \(c_{\min}/4\), all actual gaps (13) hold, and successive real backgrounds are related by the physical response with \(r<r_*/2\), including a corresponding BOX relation. Then earlier records and their witnesses are admitted at all later real backgrounds with half their declared radii.

*Proof.* Freezing records makes the target functions, units, lifts and base radii identical to functions already imposed at the input. By GEO-monotonicity, a frozen index \(m^\circ\) is at most \(m_+\). Equation (18) gives
\[
 L^{-a(m_+-m^\circ)}w(m_+)\le w(m^\circ),\qquad a=1,2,3.               \tag{66}
\]
Thus (45), with a fixed neighbouring-stencil factor, bounds every simple-read increment by \(K_{\rm pt}rw(m^\circ)\) in its own normalized units, while its gap is at least \(2w(m^\circ)\). Our \(r_*\) makes the increment at most one sixteenth of the gap.

For a frozen tower, use that same ambient sequence in Lemma 8. Equation (66) transfers the shift to its scales. For the truncated index \(n(b)\), (20) and the floors on \(\rho_0\) give
\[
 e^{-\delta_Td^\circ(x,b)}w(n(b))
 \le4^{1+d^\circ(x,b)/\rho_0}e^{-\delta_Td^\circ(x,b)}w(n(x))
 \le4w(n(x)).
\]
Equations (45), (49) and the top factor give (64)'s tower bound. The additional normalization \(L^{p-i}\) in (14) is at most one. This treats the whole fixed function and its open domain; it never compares two different determining maps.

For a core put \(b_\iota^{\rm mid}=(b_\iota^-+b_\iota^+)/2\) and
\(\tau=(b_\iota^--b_\iota^+)/(b_\iota^-+b_\iota^+)\). Both radii have the same \(\tau\). With the infimum of the whole coefficient-lift product,
\[
 \tau\ge \frac{d_*(i)}{2(1+\beta_s)}\ge\tfrac25d_*(i),\qquad
 b_0^{\rm mid}\ge c_{\min}\alpha_0\varepsilon_i .
\]
Indeed the difference of infima is at least \(d_*(i)\inf_X\lambda\), while each infimum is at most \((1+\beta_s)\inf_X\lambda\). Incident boundary bonds may start in layer \(i-1\); restriction and (66) bound each required shift quantity by \(4L^3rw(i)\). Equation (64) makes this smaller than
\(\tau b_0^{\rm mid}/[C_{\rm os}K^\sharp(1+c_\natural)]\).
The current stays below \(b_0^{\rm mid}\), so Lemma 9 applies at the midpoint. The real clauses are unchanged. Restriction commutes with (10), since \(\eta_iL^{-(j-i)}=\eta_j\).

For drift, work at a fixed frozen record and telescope over transitions. At a physical step write
\(U_{\rm old}=(e^{i\eta H}U_{\rm new})^g\), with \(g\) real. After a real gauge, the reverse shift is \(-\operatorname{Ad}(g)H\). Its covariant-difference norm is not exactly the forward norm: the change of transport is bounded by \(C|H_\mu||H_\nu|\). The small absolute ceiling bounds this by a fixed multiple of the forward norm. Decrease \(r_*\) once to pay it. The already proved increment estimates, applied inductively on each fixed read, then cost at most its coefficient drop divided by \(32\). For physical currents use Lemma 12's exact current identity; for towers use P81's intrinsic reading and real gauge covariance. Potential components of a plain triple are zero.

A real gauge witness is transported, not declared unchanged under drift. In its old real gauge, take the logarithm of \(e^{-i\eta H'}e^{i\eta A}\). The same difference calculation, with \(|A|,|\nabla A|\) below a fixed ceiling by (61), bounds the change of both ordinary gauge norms by \(C r_*d_*(i)\alpha_0\varepsilon_i\). The recorded witness bound dominates \(\alpha_0\varepsilon_i\); for natural witnesses impose this as another coupling ceiling relative to \(a_\flat\). Choose the fixed reduction of \(r_*\) so the total cost is less than a quarter of that bound.

All coefficient drops telescope and their total is at most
\(1+\beta_s-c_{\min}\le41/64\).
The formation contribution is at most
\((c_{\min}/4)(1+\beta_s)R\); adding \((41/64)R/32\) is strictly below \(c_{\min}R/2\). The absolute real clause follows from the same curvature increment bound and the fixed \(a_T\) ceiling. This proves the conditional drift assertion. Its formation and reset assumptions are not supplied by this argument. ∎

**Lemma 12 (stage fibre and physical identification).** At a preparatory stage let \(M_-,M_+\) be the actual determining maps, the latter obtained by enlarging member \(j+1\). On the admitted datum charts there is a local map \(F\) which copies retained rows and averages the removed level-\(j\) rows into the added level-\((j+1)\) rows, such that
\[
                   M_+=F\circ M_-,\qquad
                  \ker DM_-\subset\ker DM_+.                         \tag{67}
\]
Let \(U_+\) be the new real regular critical background and \(V=M_-(U_+)\). If the actual old datum satisfies \(F(D_{\rm old})=M_+(U_+)\), agrees with \(V\) on retained rows, and is in the restricted CH chart, then
\[
 D_{\rm old}=e^{ia_V(u)}V,\qquad
 u=\left.i^{-1}\operatorname{Log}(D_{\rm old}V^{-1})\right|_{\rm free},
 \quad \|a_V(u)\|\le C_{\rm ch}L^4\|u\|,\quad \|u\|<c_{\rm ch}L^{-9}.
                                                                         \tag{68}
\]
Only the removed rows are varied. Feed \(B'=b_V(a_V(u))\), including changed outward rows, to DR.

Assume this response stays in the regularity and uniqueness balls, has specification (42)–(43) at \(s=1\), and its source avoids the \(2\eta\)-neighbourhood of \(\partial\Omega_0\). Then the pinned substituted plain triple represents the actual old critical pair, with every surviving stored transport unchanged. At complete stars the current equals \(J^\circ(e^{i\eta H}U_+)\); at incomplete stars \(K=0\). On a bare determining row,
\[
                             H=\eta^{-1}B',                           \tag{69}
\]
which need not vanish. At a main step convert the input current by \(L^{-3}\) as in (9).

*Proof.* An added coarse row reads only its double block. Because members are unions of aligned coarse blocks, both endpoint blocks of a row newly outside the old deeper member are disjoint from that member. Separation puts the entire double block inside the preceding member. Its lower bonds are therefore old determining rows, with no inward-row exception. Iteration of (5) proves (67). The construction is invariant under old residual gauges; the kernel inclusion is its chain rule.

CH's pivot correction changes only the selected pivot for each added equation. Once the free rows are fixed, each equation involves its own pivot and no other selected pivot. Restricting the full chart to these equations and keeping retained rows fixed therefore gives \(a_V(u)\). The fibre equation for the actual logarithm is \(q_V(a)=0\), so local uniqueness of that graph gives (68). Shared free rows can occur in different equations; this is not an independent product decomposition of all their variables.

The new critical point is also critical for the old fibre by (67), for the same regional action. Reduced and raw data are related by (7), not identified. Lemma 6 then identifies the response with the old critical background, up to its node factors. Smallness of (16), (45), and the real background bounds keeps its curvature and current in the regular orbit's uniqueness class. The node gauge removes the return factors. The current statement follows from (35); (69) and the boundary buffer give \(K=0\) at incomplete stars exactly as in Lemma 6.

For stored slots, their initial sites being level-\(l\) lattice sites is essential. If the site's current layer is at most \(l\), it is its own top. Otherwise GEO's margin permits only layer \(l+1\). For \(l\ge1\) that top is pinnable; for \(l=0\), the whole pillar's \(2\eta\)-neighbourhood avoids \(\Omega_2\), which is precisely the extra level-one pinning condition.

This classification persists through a prepared operation. Above the last remade level use the label argument. A surviving slot of an already integrated level lies in \(Z''_{l+1}\), hence outside every remade deeper member by nesting, and is its own top. Below the first remade level the label argument still applies; in the single interface case \(l+2=h+1\), the prepared gap from \(Z_h\subset Z''_{h+1}\) supplies the same margin. Lemma 4 therefore preserves all the surviving averaged transports, and its common-centre property transfers the real tie. This proves physical identification. ∎

**Outstanding F (the actual fluctuation map).** Equation (68) is a fibre chart, not a construction of the stage's \((A_j,B_j)\)-map. The draft's FC′ assumes a real-analytic \(D_{\rm old}(\xi;D_+)\), then defines \(u(\xi)\) by its logarithm. It must still construct that function for the actual conditional means and strip change of variables, prove retained-row and boundary identities, and prove on the full complex contour
\[
 \|u(\xi)\|<C_A\delta'_j,\qquad
 \|b_V(a_V(u(\xi)))\|<C'_A\delta'_j.                                  \tag{70}
\]
SA 7601 and 7614 describe changes which cannot be omitted. CA-I 54287 instructs this reconstruction; it does not supply it. FL means precisely this map and bound here. Neither a formal composition nor the assertion that any existing parametrization factors through a chart closes this obligation.

**Lemma 13 (source budget).** Let \(S\) include the changed determining rows, their averaging carriers and changed outward-row carriers. Let \(\mathcal R_X\) contain every stencil and pillar read by the substitution on \(X\). Use the input metric and input layers in
\[
\begin{split}
 D_{\rm src}&=C_DE_{\bar\kappa}C_A\delta_{\rm src},\\
 Q_X&=\max_{b\in\mathcal R_X}
             \frac{e^{-\mu d_+(b,S)/2}}{w(m_+(b))},\qquad
 E_X=\max_{y\text{ endpoint top of }X}e^{-\mu d_+(y,S)/2},\\
 a_X&=D_{\rm src}\max\{C_{\rm lev}Q_X/r_*,
                                      K_{\rm pin}E_X/\epsilon_{\rm lev}\},
 \qquad \rho_X=(2a_X)^{-1}. 
\end{split}                                                            \tag{71}
\]
At \(a_X=0\), set \(\rho_X=\infty\). If DR is initially stated in the old finer metric, (16) also holds in \(d_+\), since \(d_-\ge d_+\). For \(|z|<\rho_X\), every endpoint top is levelled and
\[
            \|\rho_X^{\rm res}(zh_Y)^\delta\|_w<r_*/2.                 \tag{72}
\]
Here \(\rho_X^{\rm res}\) denotes restriction and change of units, not the scalar radius \(\rho_X\); pin after multiplying by \(z\). Take \(C_A\) to include both fixed completion and reduced-datum losses in (70). If DR was expressed in old layer scales, passing to input scales costs at most \(L^3\), since one transition raises a site by at most one level. Include this fixed factor in \(C_D\).

For main steps, \(\delta_{\rm src}=(A_1/A_0)\varepsilon_{t-1}\). For stages at the actual level \(j=t-N_t+n\),
\(\delta_{\rm src}=(A_1/A_0)(\log\theta_j)^{-(p_0-p_1)}\varepsilon_j\).
There are fixed constants \(C_{\rm main},C_{\rm st}\), chosen before \(\kappa\) and independent of \(M,\bar\kappa\), for which
\[
\begin{split}
 a_X&\le C_{\rm main}E_{\bar\kappa}(A_1/A_0)
                       +D_{\rm src}K_{\rm pin}/\epsilon_{\rm lev}
                                                   &&\text{(main)},\\
 a_X&\le C_{\rm st}E_{\bar\kappa}(A_1/A_0)
          (\log\theta_j)^{-(p_0-p_1-r)}
                       +D_{\rm src}K_{\rm pin}/\epsilon_{\rm lev}
                                                   &&\text{(stage)}. 
\end{split}                                                            \tag{73}
\]
Thus \(a_X<1/2\) uniformly in stage level and waiting depth by rows 9–10 of the constant order. BOX needs its own version of (71).

*Proof.* Lemma 4 converts the derivative convention and applies its profile bound to \(zH\): the pinning size is at most \(K_{\rm pin}|z|D_{\rm src}E_X\), and the normalized pinned shift is at most \(C_{\rm lev}|z|D_{\rm src}Q_X\). Equation (71) gives (72) and forces levelling throughout the disc; no nonholomorphic cutoff is varied there.

For the source comparison, removal at level \(j\) and one-step averaging change only layers within one of \(j\) in the old sequence. The outward correction uses one adjacent endpoint block. In the input sequence, only member \(j+1\) has changed, so all these carriers have \(|m_+-j|\le2\), with a fixed enlargement allowed in the carrier constant. Apply the separation argument (20) **to the input sequence**. For a read bond of layer \(m\) it gives
\[
 d_+(b,S)\ge\rho_0(|m-j|-3)_+-C_{\rm car}.                             \tag{74}
\]
The fixed \(C_{\rm car}\) pays endpoints of stencils and carriers. At a main step the same argument is one-sided, centred at \(j=t-1\). The draft used \(d_-\ge d_+\) in the wrong direction to transfer a lower bound on \(d_-\); (74) is the required new lower bound.

At a stage, (18) and RUN give
\[
 Q_X\le
 \frac{2e^{\mu C_{\rm car}/2}}{a_j\alpha_0\varepsilon_j}
 \sup_{\nu\ge0}4^\nu e^{-(\mu\rho_0/2)(\nu-3)_+}
 \le\frac{C}{a_j\alpha_0\varepsilon_j}.
\]
The supremum is finite by row 3. Since
\(a_j^{-1}=8N(\theta_j)/\beta_s\) and \(N(\theta_j)\le C_N(\log\theta_j)^r\),
this proves the second line of (73). There is no factor \(2^{N_t}\).
For the main step replace \(a_j\) by a fixed multiple of \((1-\theta_s)\beta_s\); the same computation gives the first line. Finally \(p_0-p_1-r>0\) and \(\theta_j\ge\gamma^{-2}\) make the stage and pinning terms uniformly small. This argument preserves the explicit \(E_{\bar\kappa}\) factor. ∎

## 8. ST1

**Theorem 14 (hereditary substitution, physical identification and finite re-expansion).** Fix a finite four-dimensional lattice and a finite history with the records of Section 1. Use the constants in Section 2 in the stated order. Assume:

1. GEO, AV/CURV, A1/F0/REG, P82°–M1 with (15), PROF/RCG4, and OPS/SLICE/UNQ hold on every determining system and carrier used. In particular the precision and derivative constants needed by IN1 are fixed before \(\kappa\), independent of \(M,\bar\kappa\).
2. For the transition in question the **actual** gaps (13) hold, the input point is in \(\mathcal D_{a|+}\) and all required working cores, and every absolute, logarithm, gauge and source-domain ceiling of Section 2 holds. The initial/unfinished radius-table entries, when used, satisfy these same comparisons; they are not identified with the simplified interior table.
3. DR is given on the full switch polydisc, with (16), specification at one, restriction and component splitting. Its component response vanishes when there is no source and at zero switches. The actual completed source has the FL bound, and (71) has \(a_X<1/2\).
4. The activity \(f\), supported on \(X\), has the bound \(b_f\) and the holomorphic, Borel, covariance and stored-slot interface in Section 1. Every relevant endpoint pillar is among the reads in (71). For complex pair descent assume \(f\) is a pair function; for a real tie only the real conclusion is asserted.
5. For identification with the old physical activity, the actual map (70), the regularity hypotheses of Lemma 12 and its boundary buffer hold. Stored slots have the initial-site, margin and retirement properties in GEO.

Let the localization partition have finitely many cells \(\mathcal C\). Let \(X^\uparrow\) contain the cells meeting \(X\) and its required read carriers. For \(Y\supset X^\uparrow\), with switches on its cells, define
\[
 \Phi_Y(s,z)=
 f\!\left(\rho_X^{\rm res}
       \bigl(P\dotplus(zh_Y(s;P,\xi))^\delta\bigr);\mathfrak q_X\right).
                                                                         \tag{75}
\]
For an activity without stored slots one may use the unpinned shift. All stored coordinates \(\mathfrak q_X\) remain fixed. Then:

* (75) is defined and holomorphic in \(z\) on \(|z|<\rho_X>1\), in the switches on \(|s_\Delta|<e^{\bar\kappa}\), and in all declared complex variables at fixed real factor. It is bounded by \(b_f\). Every target read retains half its gap and every datum remains in its open continuation tube. It is Borel in the declared real and near variables, hereditary under restriction, and has the stated real gauge and conjugation covariance.
* At \(s=\mathbf1,z=1\) on the physical locus, (75) is exactly the old activity at the actual reconstructed background, with its stored transports. It preserves the real tie. Under the pair-function hypothesis it also descends through complex splittings on their common admitted domains.
* For \(K=Y\setminus X^\uparrow\), put \(f_0=f(\rho_X^{\rm res}P;\mathfrak q_X)\) and define the Boolean coefficient
  \[
   V_f(Y)=\sum_{A\subset K}(-1)^{|K\setminus A|}
       [\Phi_Y(\mathbf1_{X^\uparrow\cup A},1)-f_0].                    \tag{76}
  \]
  Switches outside the indicated set are zero. Then
  \[
   |V_f(Y)|\le \frac{2b_f}{\rho_X}
                         (e^{\bar\kappa}-1)^{-|K|}
             \le\frac{2b_f}{\rho_X}e^{-(\bar\kappa-1)|K|}.              \tag{77}
  \]
  Terms with a switched component disconnected from the base, or from every source in that component, vanish. If no source reaches the base, the entire excess vanishes. Several components may survive when the base itself has several components.
* With all regional maps chosen consistently,
  \[
   \sum_{X^\uparrow\subset Y\subset\mathcal C}V_f(Y)
                 =\Phi_{\mathcal C}(\mathbf1,1)-f_0.                 \tag{78}
  \]
  Iterating (78) along any finite admitted chain gives the corresponding nested substitution identity.

If formation, FL, BOX and all reset comparisons hold at every actual transition, Lemma 11 supplies the chain admission needed to apply this theorem at every transition. The present drafts do not establish those additional premises at Outstanding M, R, B and F.

*Proof.* Lemma 13 forces levelling on the full \(z\)-disc and gives (72). Lemma 4 makes the pinned shift holomorphic there and preserves stored transports. Lemma 11 puts it inside the target domain with room; Lemmas 5 and 8 supply the continuation domain. Thus composition with \(f\) proves the first bounded-holomorphic assertion. A norm-dependent levelling decision is used only to select a region where it is forced; it is not differentiated.

The formulas use finitely many continuous algebraic maps, fixed branches and the Borel activity interface. Witness existence is Borel as well: exhaust each strict real gauge bound by closed smaller bounds; the bounded real potentials and compact unitary gauges have compact continuous images, and then take a countable union and finite intersections. Near stored coordinates are held fixed. No analyticity in a merely Borel variable is used. Inactive outer coordinates of a bounded activity are constant in \(A',\mathbf J\), since each ranges over a whole complex line; Liouville's theorem allows their projection to zero when a local logarithm chart is needed. Substitution leaves them unchanged.

Lemma 12 identifies the complete physical pair and the boundary plain current. Lemma 4's real common-centre comparison, covariance and the activity's real tie give the second assertion. For complex splitting independence use its complex common-centre continuation and the additional pair-function hypothesis. The main-step rescaling is (9). No independent complex current is set equal to a physical current during this argument.

For (77), the function \(\Phi_Y(s,z)-f_0\) vanishes at \(z=0\) and is bounded by \(2b_f\). Cauchy in the distinct switch variables bounds its mixed derivative along \([0,1]^K\) by \(2b_f(e^{\bar\kappa}-1)^{-|K|}\); Schwarz in \(z\) contributes \(1/\rho_X\). Integrate that derivative over the unit cube to obtain the finite difference (76). This also covers \(K=\varnothing\), for which the subtraction is necessary. Since \(\bar\kappa\ge1\), \(e^{\bar\kappa}-1\ge e^{\bar\kappa-1}\).

Component splitting and the levelling collar property make the reading independent of every switched cell in a component missing the base or its source; its finite difference is zero. Regional consistency identifies readings on smaller \(Y\). Finally sum (76). For a fixed proper subset \(A\) the coefficient is \((1-1)^{|\mathcal C\setminus(X^\uparrow\cup A)|}=0\); the full subset has coefficient one. This is (78). The sum is finite; no convergence or interchange with a stored-field integral is asserted. Induction gives the finite nested identity. ∎

## Definitions supplied in distillation

The following conventions or missing completions were supplied explicitly; their occurrence in this list does not discharge an input.

1. Matrix and array norms, oriented bonds, contained stencils, the Wilson normalization and regional versus plain currents: (1)–(2).
2. Mesh conversion, actual rows including outward endpoints, nodes/residual gauges, criticality, weighted path metric and carrier conventions: (3)–(5), (9).
3. Raw datum versus reduced response datum, the canonical comb representative versus averaged stored transports, and the intrinsic continuation tube: (6)–(8), (32).
4. A triple with independent complex current, active-bond substitution, and the real tie versus complex pair-function requirement: (10), Section 1.
5. Complete core membership, both erosion rules and all subordinate tower reads, enlarged witness cubes and natural containing cubes: (11)–(12).
6. Frozen read and witness records, chain domains, the scalar core radius as the infimum of the whole product, effective core coefficients, midpoint room and formation multiplier: (13)–(14), Lemmas 10–11.
7. Stage indexing, the stage-debt ledger counted once per operation level, marks as a set, and the separate profile \(a_u\) rather than IN1's \(\kappa\): (17)–(18).
8. Relative averaged potentials and node factors, pinnable/levelled tops, levelling read sets, the convex real frame and prescribed transport pins: (23)–(31).
9. Fine/site/row pairings and all straightening, projection, inverse, reduced-action and multiplier operators; the actual specification at \(s=1\): (33)–(44).
10. Settled tower elements, ambient/subordinate scales, weighted value/first-difference norms and normalized tower curvature/current: (47)–(54).
11. Raw capped formation exponents, their smoothed lift, the fibre map on retained/removed rows, and the actual free fluctuation coordinate required from FL: (56)–(58), (67)–(70).
12. Completed source carriers, input-metric source budgets, pinning radius, localization hull, localized composition and the subtracted Boolean coefficient: (71)–(78). Empty-source radii and the distinction between scalar radius and restriction are included.

## Source checks and the round-1 questions

The SA outline and CA-I were located through the README, neighbouring chunk entries and obligations in the supplied full-read index; the three source files were fetched once at the requested commit and read only in bounded excerpts. The quotations and line references in all four pass-1 inputs and the round-1 distillation were checked against those files. The sources are [the SA outline](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM4_sketch_500.tex), [CA-I](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_I.tex), and [YM3 I](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM3/YM3_I.tex), by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. The 3D arguments are templates; their line numbers do not prove a 4D claim.

| Checked source passages | Consequence for this manuscript |
|---|---|
| SA 5610–5618, 5663–5861, 6080–6173, 6559–6665 | Core/substitution definitions and tables; 6155–6158 warns that inclusions are hypotheses; stored gauge law is 6160–6162. ER7 remains an input in its source and is not used for Lemma 9. |
| SA 7063–7108, 7180–7188, 7741–7747, 7911–7914, 8257–8299 | Actual averaging, distinct transport conventions, exact first-order row and the local pivot graph. QC24 is at 8289–8296. |
| SA 9593–9791, 9886–9896, 9908–9916, 9987–10001 | Separated backgrounds, datum charts, continuation, derivative/tower statements and restriction. The seam constant at 9667 is \(CL^2\), not a specified \(2L^2\). The row-incidence count at 9987–9997 is not a right inverse for all field constraints. |
| SA 10103–10212, 10296–10308, 10340–10470, 10558–10582 | Actual independent-current operators and specification at one; these are not identities valid after arbitrary decoupling. The parameter-length argument retains its corner factor. |
| SA 7597–7618, 17255–17259, 17398–17447, 17455–17462, 17544–17551, 17575–17656, 19408–19473 | Conditional-mean/strip changes, stage geometry, mark retirement, tests in the stage's scale, running minimum, BOX and constant order. Overlapping collars do not contradict separated determining sequences. |
| SA 4006–4012, 18108–18128 | B4 and integrated activity majorants need their own hypotheses; pointwise composition bounds do not supply them. |
| CA-I 9840–9848, 9953–9965, 42907–42916, 48520–48568 | Retained lower rows in restricted towers, the \(N_0\) relation and the four gauge families. The first two ranges are CA-I, not SA outline line numbers. |
| CA-I 49495–49546, 53737–53832, 54236–54330, 54986–54998, 65655–65661 | Background and stage supplies are hypotheses in these passages. The prepared nest includes \(N_0\ge2\); 54287 instructs reconstruction. The enlargement's metric width remains explicitly assumed in Lemma 2. |
| Y3 26236–26256, 26770–26816, 28228–28470, 33100–33290, 33440–33647 | Gauge, Hessian, reduced action, multiplier and critical-response algebra used in Lemma 6, with 4D volume and degree corrections. |
| Y3 41978–41990, 42080–42480, 49560–49700 | Local core substitution and averaging templates. Lemma 7 instead supplies its direct product-series estimate; Lemma 9 uses the Lipschitz tower route. |
| Y3 52979–54090, 54441–55130, 55200–55262 | Admission, source-domain margins, boundary-current identity, levelling, and the stored-site argument. The containing-cube clause is 53362–53367. |
| Y3 55448–56340, 56420–56757 | Tower/half-gap/substitution and tie proofs. Composition is at 56309–56318; 56330–56338 defines the subtracted increment. The real tie is at 56442–56444, not 56461–56463. |

Here is the disposition of the six questions that round 2 set out to close.

| Round-1 question | What is now established |
|---|---|
| (a) Four-dimensional ambient tower bound | Lemma 8 proves the implication, including current control, non-top gauge factors and the scale cancellation. P82° through (15), and the other named upstream inputs, remain. |
| (b) Real admission and every cube family | Lemma 10 proves pointwise/tower formation and the stated cube-gauge estimate with carrier margins. Minimum-lift core admission and output/consumer formation remain **Outstanding R, B**. |
| (c) Actual stage reconstruction and physical identification | LEV and CRIT are folded into Lemmas 4 and 6; Lemma 12 proves physical identification given the actual datum map. Constructing that map on its complex contour remains **Outstanding F**. |
| (d) Source level and no-new-mark stage reserve | Lemmas 1 and 13 repair the \(2^{N_t}\) loss, use the actual stage level and input metric, and keep \(E_{\bar\kappa}\) explicit. Reset deletion is a separate **Outstanding M**. |
| (e) Changed reads and full-radius comparisons | Frozen functions give compatibility and Lemma 11 gives half-gap substitution and conditional drift. Formation, actual physical shifts and reset gaps are still required. |
| (f) Application at every actual stage, including overlaps | OS is reduced to the explicit prepared geometry and existing uniform analytic inputs by Lemma 2. The assertion that all actual stages satisfy Theorem 14 is **not yet proved**, because M, R, B and F remain. |

## Result

This ST1 proves Theorem 14 as a conditional implication: hereditary half-gap substitution, the physical identification when the actual stage map is supplied, and bounded holomorphic finite re-expansion. LEV, CORE, P81 and CRIT are numbered lemmas with their hypotheses and proofs. They are no longer unexplained ST1 imports. CORE does not require ER7 or \(b_1^2\le c_\natural b_0\).

The principal remaining analytic import is **P82°**, with M1 and the derivative implication (15), uniformly on the admitted layered class. The other declared supplies are A1/F0/REG, AV/CURV, PROF/RCG4, OPS/SLICE/UNQ, the actual decoupled DR construction, FL/CH/BOX, GEO/RUN and NL1/LF1's activity interface. Application still requires the specific repairs **M** (deleted-mark gaps), **R** (minimum-lift cores), **B** (output and changed-consumer admission), and **F** (actual collar-variable map). No full B4, infinite-volume summability, stored-field integral bound or LF mass conclusion follows from the finite theorem alone.

Corrections made in distillation:

1. Replaced bare-row \(H=0\) by \(H=\eta^{-1}B\), and required the \(2\eta\) boundary buffer for \(K=0\) at incomplete stencils.
2. Replaced the 3D site-to-top \(3/2\) by \(<2\), hence \(e^{3\delta_T}\) by \(e^{4\delta_T}\); used four-coordinate counts, six-plaquette stars, the degree-eight scalar boundary term and 4D volume weights.
3. Moved \(C_{\rm os},K^\sharp\) to constant row 4. Kept every structural/precision constant before \(\kappa\), independent of \(M,\bar\kappa\); retained \(E_{\bar\kappa}\) and \(C(M)\) only in later smallness conditions, without claiming the unproved optional uniform response factor.
4. Separated raw and reduced datum coordinates, the two transport conventions, and physical versus independent currents; made the response's specification at one and its inverse/chart assumptions explicit.
5. Corrected the comb gauge's inverse sign, retained the exact first-order averaging norm \(L\), and supplied the non-top complex gauge bound without using real unitarity at complex parameters.
6. Inserted the left logarithmic velocity when differentiating \(e^{i\eta H}\), and paid the quadratic transport correction in the reverse drift norm. Used conservative hand-proved \(2s,4s\) local bounds for CORE.
7. Corrected the source-distance comparison by proving it in the input metric, retained its scale-conversion factor, and used the stage-level debt and running minimum instead of the old \(2^{N_t}\) estimate.
8. Defined core radii using the infimum of the whole coefficient-lift product and exposed the missing uniform minimum-lift comparison. Increased the formation floor to pay both factors of \(c_{\min}\).
9. Included deleted-mark debts, inherited-lift hypotheses, the \(N_0\ge2\) case and a proof of the smoothed lift's polynomial ceiling; restricted prepared sets to their chosen component, completed the boundary cases and imposed strict separation through \(LM\ge2\rho_0\).
10. Limited the fibre-chart conclusion to a supplied actual parametrization, removed the false independent-product reading of overlapping free variables, and kept FL's complex contour bound explicit.
11. Separated BOX admission and changed witness/chain consumer domains from the proved gauge bounds. Repaired the level-zero gauge estimate by its actual smallness condition.
12. Restricted holomorphy to forced-levelled fibres, distinguished real ties from complex pair descent, supplied inactive-coordinate handling and the empty-bracket subtraction, and corrected the source locations recorded above.

All proofs are by hand. Retrieval, citation inventory and text editing supplied no mathematical discharge. This is research text, grants no status, and is **not yet refereed**.
