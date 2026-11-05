# ST1 — round 3 distilled manuscript

Provenance: Codex (GPT-6), 2026-11-04, Pass 2 (distil), round 3, from `st1-r2.md`, Claude’s `st1-draft3.md`, and the design changes in `nl1-L-draft.md`, at repository commit `2afa141308f85e0fb262acd684c25a49e354feb6`. Source material by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, is credited locally below. Research text only; no scientific or audit status is granted.

SA denotes the four-dimensional outline, CA-I its complete account I, and Y3 the three-dimensional manuscript, all at `31a47c543775`. The averaging, gauge, background and stage constructions originate in Tadeusz Bałaban's work; the source formulations and Y3 proof templates used here are credited to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Source line numbers refer to the three files specified in the task, not to the working checkout. No scientific status is assigned to an input or conclusion. This folds the round-3 repairs into the round-2 proof. The active table is (Tq0) below. The conclusions remain conditional; CI and the explicitly identified contour/coordinate supply are not proved by substitution.

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

The scalar comparison core of level \(i\), used in Propositions R0 and R°, \(\mathcal U_i^\circ(X;b_0,b_1)\), \(0<b_0\le b_1\), has the strict conditions
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

A **read record** fixes its function, full carrier, units, radius index and positive base radius. A tower's full carrier includes its determining datum and continuation domain; it is not just its output stencil. A **radius set** is the finite nonempty local stencil on which a coefficient is minimized. It does not replace the full carrier. Frozen records retain both sets and their functions. Gauge records specify the cube, its enlargement, its units and its bound.

**Radius table (Tq0).** Put
\[
 \ell_m=\log\theta_m,\quad g_m=\theta_m^{-1/2},\quad
 \varepsilon_m=A_0g_m\ell_m^{p_0},\quad
 \delta_m=A_1g_m\ell_m^{p_0},\quad\delta'_m=A_1g_m\ell_m^{p_1},\qquad
 r_\iota(m)=\alpha_{\iota,m}=C_\iota g_m\ell_m^q.                 \tag{Tq0}
\]
Here \(C_1\ge C_0>0\), \(q>p_0+2r_R\), and \(p_0-p_1>r>1\). The exponent \(q\) in (Tq0) is fixed; a tower's level index below is a dummy integer. Set **\(\lambda_\tau\equiv1\)** and **\(\Lambda_Q=1\)** in all records. Raw overlap exponents still enter the real tests, not the analytic radii. This is SA's running-radius table (SA 6017–6035), with our explicit choice of record coefficients. It does not identify SA's separate absolute radii with \(C_\iota\).

**Definition R1 (elementwise core, with unit lift).** At a frozen core address \(X\subset\Omega_i\), \(i\ge1\), assign every simple element and every complete tower output element \(e\) a radius set \(\mathrm{Rd}_{\rm rad}(e)\), containing its local stencil. Set
\[
 b_\iota(e)=r_\iota(i)\inf_{x\in\mathrm{Rd}_{\rm rad}(e)}c^*_\sigma(x|i).
                                                                    \tag{R1}
\]
Impose (11) element by element with these radii. For every \(Z,p,n\) of (12), require the same open tower domain and
\[
 |G_n(e)|<b_0(e)L^{-(i-p)},\qquad
 G_n=L^{2p}(\partial T_n-I)\quad\hbox{or}\quad L^{2(p-n)}J_n(T_n),       \tag{R2}
\]
also at \(A'=0\). For every prescribed core cube \(Q\), require a real gauge with
\(|A|,|\nabla A|<C_{\rm pot}M r_0(i)\) on the supplied enlarged carrier. These witness bounds have no coefficient. Other witness families are recorded separately. Write \(\mathcal U_i^{\rm el}(X)\) for this core. Every radius is a single scalar on its own radius set; there is no infimum over the whole address in this definition. Put \(\chi_c=(1+\beta_s)/c_{\min}\). Any two element radii at this address have ratio at most \(\chi_c\); no smoothness of \(c^*\) or diameter-one assertion is needed.

For a finite ordered history, the chain domain \(\mathcal D_{a|\sigma}\) imposes every record born between \(a\) and \(\sigma\). A record \(r\) retains its own function and base radius \(R_r\), while its current radius is \(c_\sigma(r)R_r\). Gauge witnesses and the absolute real curvature ceiling \(a_T/4\) are retained unchanged. New records add conditions. For a transition \(-\to+\), **compatibility with room** means that every target record occurs in the input, with
\[
 c_-(r)-c_+(r)\ge d_*(m_r)>0,\qquad
 \Delta_r=(c_-(r)-c_+(r))R_r,\qquad
 b_r^{\rm mid}=\tfrac12(c_-(r)+c_+(r))R_r.                              \tag{13}
\]
For a core this is required for both radii, with a common scalar shrinkage. All read sets include the stencils needed by their estimates.

Simple record radii are \(c^*_\sigma(x|m)r_\iota(m)L^{-am}\), frozen at their birth structure; \(a=1,2,3\) is the scaling degree. Tower records use the meet of the frozen sequence with either erosion tower and, for \(1\le n\le p\le i\),
\[
 |\partial T_n-I|<L^{i-p}c^*_\sigma(x|\ell)r_0(\ell)L^{-2\ell},\qquad
 \eta_n^3|J_n|<L^{i-p}c^*_\sigma(x|\ell)r_0(\ell)
                 L^{-2\ell-\min(n,\ell)},\quad\ell=\min(m_\tau(x),i).  \tag{14}
\]
Core records are Definition R1. Witness bounds are \(g_Qr_0(i)\), where \(g_Q\) is respectively \(\mathsf oLMB^{cg},BM,C_{\rm pot}M\) for the large, CA-I and core families. Natural cubes require a containing cube with bound \(a_\flat\). Each enlarged carrier must lie in the supplied region and in layers at least \(i-1\). Initial and unfinished layer conventions are separate recorded data; they must satisfy the same radius and gap comparisons and are not silently replaced by this interior table.

A carried activity \(f\) is bounded by \(b_f\) on its declared domain, holomorphic in \((A',\mathbf J)\) with \(U\) fixed, Borel in \(U\) and near stored variables, and jointly holomorphic in far variables and their recorded switches. Each stored slot records its bond, initial site, level, range, near/far class and transport convention. Require simultaneous real gauge covariance and equality at two real splittings of one pair. A **pair function** additionally has equality at complex splittings and holomorphic descent on the relevant common domains. A real tie alone is not that additional assertion.

## 2. Remaining inputs and order of constants

The following are hypotheses, not consequences of a source label.

* **GEO.** The aligned centred block geometry above; both erosion assignments; an injective periodic coordinate chart for every read cube and its required margin; the prepared sets and margins in Lemma 2; memberwise monotonicity along the history being compared; complete stencils at core addresses; and the witness enlargements required in Lemma 10. Turning cells and their two-stencil margins lie in the response wall component on which they act. A stored level-\(l\) slot starts at a level-\(l\) lattice site, outside \(\Lambda_{l+1}\), at distance \(>2\xi_{l+1}+2\eta\) from \(\Omega_{l+2}\), and disappears when its collar is integrated. Mark resets and raw-exponent formation must be specified, rather than inferred from a partial order.
* **AV/CURV.** The actual formula (5), its local analytic row bound \(|B(c)|\le C_Q\xi_q\sup_{D(c)}|A|\) on a fixed weighted value ball; and the real curvature recursion \(v_{n+1}\le L^2v_n+C(L^2v_n)^2\). The resulting test bound is \(2\epsilon\) inside a layer and \(C_{\rm sm}L^2\epsilon\) across a seam. The recursion itself remains imported from `a1-balaban.md` §3.5.
* **A1/F0/REG.** The real regular critical orbit, canonical comb representative, local analytic continuation and restriction theorem in `a1-balaban.md` §§3.5–9, conditional on its flat input F0; and the local regularity conversion REG in `p82-draft.md`. The precise consequence used is Lemma 5. This packaging does not establish F0 or A1.
* **P82°, M1 and the derivative theorem.** At a real curved regular critical reference, the weighted inverse for the outline's pillar-\(R\) slice and straightened \(K_0\), with the multiplier normalization, implies the four-dimensional derivative estimates of `a3-derivative.md` §§6–7. On the whole fixed raw-datum ball, a row direction \(e_c\) satisfies
  \[
  \xi_y|\dot H|,\ \xi_y^2|\nabla\dot H|,\ \xi_y^3|D^{\mathsf T}D\dot H|,
  \ \xi_y^3|\dot J|,\ |\dot u(y)|
        \le C_4e^{-\theta_4d(y,y_c)}|e_c|.                              \tag{15}
  \]
  The current member is required independently of a first-derivative bound on \(H\). P82° is now proved and frozen ([p82.md](p82.md), gate first failing step none); the remaining matching item on this route is M1. The current member of (15) is proved in a3-derivative §7.3 only at bonds whose plaquettes lie in \(\Omega_0\), so (15) is asserted only at interior elements, which is the only place ST1 uses it. We use the stated implication to (15), not an unproved inference from the name P82.
* **PROF/RCG4.** A real critical background has normalized curvature and current bounded by \(C_P\max_\tau e^{-\delta_Pd(x,\tau)}|\partial V(\tau)-I|\). On a cube of side \(s\), with its side-\((s+6)\) enlargement, curvature \(<wL^2\eta_i^2\), matrix divergence \(<2L^3w\eta_i^2\), and \((s+2)L^3w<c_{\rm rg}\), RCG4 gives a real gauge with \(|A|,|\nabla A|<4L^3B_*(s+2)w\). These are the explicit profile and cube-gauge inputs of `a3-profile.md` and `a1-balaban.md` §3.8.
* **OPS/SLICE/UNQ.** All inverses in Lemma 6 exist on the declared regular-pair ball. The repaired local Landau chart and its tangent factorisation (`a3-derivative.md` Lemmas 6.1–6.3) hold. The straightening and response fixed points have unique small solutions, uniformly on their stated balls. No inverse is inferred from formal matrix notation.
* **DR, including its specification at one.** An actual regional response \((H,K)\), holomorphic in its complex input pair, datum and \(|s_\Delta|<e^{\bar\kappa}\), is given, with reality, covariance, restriction consistency, common-lift transport and splitting over face-connected components. At \(s=1\) it uses the reduced action and multiplier formulas of Lemma 6. For source \(S\), it obeys
  \[
   n_b(H,K):=\max\{l|H|,l^2|\nabla^UH|,l^3|K|\}
       \le C_D E_{\bar\kappa} C_A\delta_{\rm src}e^{-\mu d(b,S)}.         \tag{16}
  \]
  Here \(C_D,\mu\) are fixed constants; \(E_{\bar\kappa}\ge1\) is a specified parameter factor, for example \(e^{C_E\bar\kappa}\) with fixed \(C_E\). Keep it in every source budget. It is not an IN1 precision constant. Likewise write the source-domain threshold explicitly if it is \(\epsilon_D e^{-c_D\bar\kappa}\).
* **CH.** The actual average has the pivot support, inverse and Taylor bounds of SA QC18–QC24 on each regional chart. They hold uniformly on the admitted complex reference ball, with its gauge condition numbers charged. Lemma F2 states exactly what is used. CH does not identify a stored stage integral with bare Haar measure.
* **RUN and formation data.** \(\theta_m\ge\gamma^{-2}\), bounded adjacent frame increments, \(N_t=N(\min_{u\le t}\theta_u)\), \(1\le N(\theta)\le C_N(\log\theta)^r\), and \(N\) is nondecreasing. All raw overlap exponents, inherited ones included, satisfy (56) below. The real stage tests obey (58) in their stated units. Neither follows from a history's name.
* **GEO-mark.** A standing mark of level \(s\) contained in a class component of level \(t\) has \(s<t-N_t\); standing windows sharing a point are disjoint. A mark disappears only when contained in a healed component or island at that operation's output. Its recorded number \(\nu\) of completed stages never decreases while it stands. Islands contribute no remake levels. A point belongs to at most one class component per operation level. These are hypotheses about the actual history (SA 6111–6115, 17433–17449).
* **RUN-low.** The cell factors satisfy \(R_i\ge c_N(\log\theta_i)^r\), with fixed \(c_N>0\), \(r>1\), and \(L^{N_t^0-1}=R_{k_\sharp+1}\), \(k_\sharp=t-N_t^0\), \(N_t^0\ge2\). This is a lower bound, additional to RUN's upper bound. It is consistent with the rounded logarithmic cell sizes of SA 6026–6035.
* **GEO-box.** Specify the affected output-loop family \(\mathcal B_t\). Every corner of each such loop lies in the old \(\Omega_{k_\sharp+1}^c\) and is newly healed into output layer \(t\). The box response carrier lies in that top layer, up to the fixed endpoint/stencil enlargement used in Lemma B2. The prepared-box inclusion of CA-I 53786–53804 does not alone prove this assertion for an arbitrary enlarged loop family. This full carrier condition is assumed, including the required metric width of layers.
* **BOX.** (bg) The output background is the canonical real regular critical background of \(D_{\rm out}\). Loops in \(\mathcal B_t\) have curvature at most \(C_{\rm bx}C(M)\varepsilon_t\); all other loops satisfy the inherited (58), converted to their output levels. (id) At real parameters the preceding background is \((e^{i\eta H}U_{\rm out})^g\), with \(g\) real, the correct independent/plain-current identity, and surviving stored transports as in Lemma 12. (resp) On the full switch polydisc the box response has the DR properties and
  \(n_b(H,K)\le C(M)E_{\bar\kappa}\delta'_t e^{-\mu d_+(b,S_{\rm bx})}\).
  The box chart radius \(a_\Lambda\), \(C(M)\), and their source threshold are specified after \(M\), before \(\gamma\). SA 17656 supplies a box-minimizer statement; it is not a proof of all these response clauses.
* **ST-test.** The stage's passing factor tests every free removed row against \(V^\sharp=M_-(U_+^\sharp)\) at \(\delta'_j\). Every removed row, pivots included, lies within \(r_{\rm sol}/4\) of that reference, where \(r_{\rm sol}\) is the converse neighborhood in Lemma F2. The reference is formed from data in \(X^\sharp\), the quarter-cell enlargement of the component, with a specified local boundary rule. Older tests and stored densities are retained exactly. The chosen test is a design input; its compatibility with the rest of the history construction is not inferred merely by reducing a threshold.
* **LOC.** Either (decay) the common-gauge raw discrepancy on removed rows is at most \(C_{\rm loc}e^{-c_{\rm loc}R_\sharp}\), where \(R_\sharp\ge MR_t/4\); or (form) the two references belong to one admitted raw-datum chart, and are connected there by \(D_s=e^{isB_\Delta}D_+\), \(\|B_\Delta\|\le r_B\), with \(B_\Delta\) supported outside distance \(R_\sharp\) of the full stage carriers. The derivative theorem must hold along this entire segment in consistent gauges. Equality of nearby data and real regularity alone do not supply this common chart.
* **Activity and contour supply.** CI below is owned by NL1/LF1. For an asserted identification with their actual \((A_j,B_j)\) integral, the coordinate/density identification and contour hypotheses specified at F3–F5 must also hold. They are not consequences of a formal chart factorization. STRIP, when main-step stored strip variables are used, is the discrepancy bound \(|H^{(j)}|\le C\varepsilon_j e^{-R_j}\) (SA 17521–17526), with all nonanalytic cutoff variables kept in their Borel tier.

Choose constants in this order. Structural constants are independent of \(M,\bar\kappa\); later amplitude factors remain visible.

| Order | Choice |
|---|---|
| 1 | \(0<\beta_s\le1/4\), \(0<\theta_s<1\), \(0<\beta_R\le(1-\theta_s)\beta_s/16\); exponents \(p_0,p_1,r,r_R,q\) as in (Tq0); odd \(L\ge13\), \(2\le L_\flat<L/2\); fixed geometric constants. |
| 2 | Earlier flat/analytic geometry and \(M_1\); AV/CURV, PROF, RCG4, derivative, DR base constants/rates, CH, LOC and levelling constants; RUN bounds and raw-exponent bounds. Set \(\delta=\min(1,\delta_P,\theta_4)\), \(\delta_T=\delta/4\). |
| 3 | \(\rho_0=R_1M_1\ge4L^2\), \(\delta\rho_0\ge64\log L\), \(\rho_0\min(\delta_T,\mu/2)\ge\log16\), above earlier separation floors; \(M'_1\ge\rho_0\). Shrink the continuation/chart balls. A1's reset length is a separate earlier constant. |
| 4 | \(\delta_B\le\min(1/40,r_B/40)\); \(K_a,K_T,a_T\) of Lemma 8; \(K^\sharp=\max(1,e^{4\delta_T}K_T)\), \(C_{\rm os}=18\), \(c_\natural\ge1\), \(a^\sharp\le\min(1/60,a_T)\), \(K^\flat=4\chi_c^2K^\sharp\). An absolute ceiling \(\widehat a\) below all prior balls, including \(a_T/4\) and \(\delta_B/(4C_QL)\). |
| 5 | Fixed formation comparison constants \(C_U,C_g\) of Lemma 10 and \(0<\epsilon_{\rm f}\le c_{\min}^2/[64\max(1,C_g)]\), where \(c_{\min}=1-11\beta_s/8-3\beta_R\). No running-radius coefficient is chosen here. |
| 6 | \(K_{\rm pt},K_{\rm tw},K_{\rm core}\) of Lemma 11, and \(r_*=[8\max(8L^2,K_{\rm pt},K_{\rm tw},K_{\rm core})]^{-1}\), decreased by fixed factors as needed. |
| 7 | Consumer \(\kappa\), then \(\bar\kappa\ge1\). No preceding constant reads an activity amplitude \(b_f\). |
| 8 | Aligned \(M\ge L^4M'_1\), \(LM\ge2\rho_0\), \(M\ge C_{\rm dec}\bar\kappa\) and the fixed locality floor; all cube embeddings. Then BOX's \(C(M),a_\Lambda\). |
| 9 | Test amplitudes \(0<A_1<A_0\); \(C_0>0\), \(C_1\ge C_0\), with any required external admissibility floor such as \(C_1>CM C_0\). These may follow \(M,\kappa,\bar\kappa\), as SA 19469–19470 does. |
| 10 | One ceiling on \(\gamma\) enforcing (T1)–(T3) below, all source budgets, BOX ceilings, F2/F4 chart bounds and F6. Amplitudes such as \(E_{\bar\kappa}\), \(C(M)\) enter here, not the uniform precision constants. |

**Lemma T/T3 (the radius change).** It suffices to impose, uniformly for \(\theta\ge\gamma^{-2}\),
\[
\begin{split}
 C_UA_0(\log\theta)^{p_0+2r_R}&\le\epsilon_{\rm f}C_0(\log\theta)^q, &(T1)\\
 \tfrac12\le r_\iota(m+1)/r_\iota(m)&\le2, &(T2)\\
 (1+\beta_s)M r_1(m)&<c_{\rm abs}, &(T3)
\end{split}
\]
where \(c_{\rm abs}\) is reduced by the finitely many fixed gauge and chart factors, and by BOX's later ceilings when needed. Equation (T1) is stronger than the round-2 formation floor. It absorbs the raw overlap envelope even though record lifts equal one.

*Proof.* The logarithmic derivative of \(\theta^{-1/2}(\log\theta)^q\) is \((-1/2+q/\log\theta)/\theta\). Bounded frame increments imply (T2) after a ceiling on \(\gamma\). The functions \((\log\theta)^{p_0+2r_R-q}\) and \(\theta^{-1/2}(\log\theta)^q\) tend to zero, proving the other uniform ceilings. For the latter limit, put \(x=\log\theta\); the exponential series bounds \(x^q e^{-x/2}\) by a negative power of \(x\) after choosing an integer larger than \(q\). No numerical test is used.

Here is every use of a radius in the proof. Definitions (13)–(14) and R1 replace the table. Lemma 1′ uses only adjacent ratios. Lemmas 7–8 and 9′ use absolute ceilings and homogeneous gaps. Lemma 10 compares real formation bounds with (T1), including gauges and towers. Lemma 11 divides shifts by \(w\) and telescopes the same frozen radius; its witness comparison is homogeneous. Lemma 12 and F1–F7 do not use this table. Lemma 13 and B2 use \(Q_X\) inversely proportional to \(r_0\); their revised ratios are displayed there. Theorem 14 uses these inclusions and CI. Initial/unfinished entries remain explicitly supplied. Thus no substitution constant reads \(C_0,C_1\) or \(b_f\). The uniform IN1 precision constants \((a,H,\mu_0)\) still have to be supplied before \(\kappa\). ∎

The radius choice does not rely on `nl1-L-draft.md` Proposition C. Its proposed function uses a logarithm relative to the triple's real factor \(U\) and fails the required real tie. On a flat one-layer domain, choose a sufficiently small nonzero constant commuting real potential \(A\) in one coordinate direction. The triples \((I,A,0)\) and \((e^{i\eta A},0,0)\) are admissible splittings of the same pair. The first has a nonzero raw average logarithm on a row in that direction, with positive \(\operatorname{tr}B^2\); the second has zero logarithm. Proposition C's proposed function therefore takes different values. Its claimed counterexample to the full activity interface is not proved as stated. The choice (Tq0) is justified directly by the estimates here and SA's table.

## 3. Geometry and the stage reserve

**Definition M1 (permanent mark-debt ledger).** A class component has one of the three fates healed, island or drop-out. For a standing drop-out \(C\) born at operation \(s\), its record has \(0\le\nu_\sigma(C)\le n(C)\) completed stages selected by the recorded sequence. Define
\(\mathrm{Re}_\sigma(x)=\bigcup_{C\ni x\text{ standing}}\{s-N_s,\ldots,s-N_s+\nu_\sigma(C)-1\}\).
For each such drop-out, including one subsequently swallowed, set
\[
 \mathrm{St}(C)=\{s-N_s,\ldots,s-N_s+n(C)-1\},\qquad
 \mathrm{Re}^*_\sigma(x)=\mathrm{Re}_\sigma(x)\cup
 \bigcup_{\substack{C\ni x\\C\text{ swallowed by }\sigma}}\mathrm{St}(C).
                                                                    \tag{M1}
\]
The empty stage set contributes nothing. This is a union of integer sets, not a multiset. A swallowed mark's debt is retained, and is enlarged to all its completed stages if necessary.

**Lemma 1′ / M2 (ledger and coefficient reserve).** Under GEO-mark and RUN, stage-level sets of drop-outs containing a fixed point are pairwise disjoint. The ledger is increasing along every compared history transition. Put \(\bar N(u)=N(\theta_u)\), \(a_u=\beta_s/(8\bar N(u))\). Let \(\mathrm{St}(\sigma)\) be the set of completed global stage indices \((t',n')\), counted once per operation level and phase, not once per component. At level \(t\), for \(0\le m\le t\), define
\[
\begin{split}
 c^*_\sigma(x|m)={}&1-\beta_s+\beta_s2^{-(t-m)}+\varpi_\sigma g_t(m)
 -\beta_R\sum_{u\in\mathrm{Re}^*_\sigma(x)}2^{-|m-u|}
 -\sum_{(t',n')\in\mathrm{St}(\sigma)}a_{j_{t',n'}}2^{-|m-j_{t',n'}|},\\
 g_t(m)={}&\theta_s\beta_s2^{-(t-m)}\ (m<t),\quad g_t(t)=\beta_s,\\
 \varpi_{\rm in}={}&1,\quad\varpi_n=1-n/(2N_t),\quad\varpi_{\rm out}=0,
 \qquad j_{t,n}=t-N_t+n\quad(0\le n<N_t).
\end{split}                                                         \tag{17}
\]
Then \(c_{\min}\le c^*_\sigma\le1+\beta_s\), \(c_{\min}\ge39/64\), and all transitions, including swallowing outputs, have drops at least
\[
 d_*(m)=\begin{cases}
 (1-\theta_s)\beta_s2^{-(t-m)},&\text{main},\ m\le t-1,\\
 a_j2^{-|m-j|},&\text{stage }j,\\
 \tfrac12\theta_s\beta_s2^{-(t-m)},&\text{output},\ m\le t,
 \end{cases}\qquad w(m)=\tfrac12d_*(m)r_0(m).                         \tag{18}
\]
Moreover \(w(m')\le4^{|m'-m|}w(m)\) and \(L^{-a\nu}w(m+\nu)\le w(m)\) for \(a\ge1\), \(\nu\ge0\).

*Proof.* The running minimum makes \(N_t\) nonincreasing, hence \(t-N_t\) strictly increasing. For marks at levels \(s<s'\) containing the point, if the earlier mark still stands at \(s'\), disjoint standing windows give \(s\le s'-N_{s'}\). Otherwise it was swallowed at level \(i<s'\); it cannot be swallowed by a different component of the same operation producing the new drop-out. GEO-mark gives \(s<i-N_i<s'-N_{s'}\). Thus their stage-level sets are disjoint. In fact the ledger's bound below would already follow from its definition as a set. Persistence of \(\nu\), and retention of all \(n(C)\) levels on swallowing, prove monotonicity.

At most \(\bar N(u)\) operations have a stage at level \(u\): such an operation satisfies \(1\le t-u\le N_t\le N(\theta_u)\). Its total stage debt is at most \(\beta_s2^{-|m-u|}/8\). Since \(\sum_{u\in\mathbb Z}2^{-|m-u|}=3\), stage and mark debts are at most \(3\beta_s/8\) and \(3\beta_R\). This proves the coefficient range. At a main transition the base decrease minus the new phase term is the first line of (18); at a stage the decrease is \(g_t(m)/(2N_t)+a_j2^{-|m-j|}\); at output it is \(g_t(m)/2\). New ledger debts can only increase these drops. At \(m=t\) the displayed output bound is conservative. Adjacent geometric factors change by at most two, and (T2) supplies the other factor two. Finally \(4/L<1\). ∎

**Lemma M3 (same-record consumer inclusion).** Define \(c\) by replacing \(\mathrm{Re}^*\) with \(\mathrm{Re}\) in (17), and \(c^{\rm SA}\) by additionally omitting its final stage-debt sum; this is SA's (R22) coefficient in the present indices. With identical functions, carriers and radii, ledger domains are contained in standing-mark domains, which are contained in domains using \(c^{\rm SA}\). Indeed \(c^*\le c\le c^{\rm SA}\), since the first removes more mark debt and the second removes stage debt. Every inequality is monotone in its positive radius. Witness bounds have no coefficient. This does **not** compare our whole domain with a source domain having different cores, carriers or witness constants; that comparison remains part of CI.

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

The enlargement-width convention is an explicit hypothesis: CA-I 53742–53743 names Bałaban's layers without defining their metric width. CA-I 53773–53774 does supply \(N_0\ge2\), needed for the raw-exponent cap. Once GEO-prep and \(LM\ge2\rho_0\) hold, no additional OS analytic import is needed.

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
 +(I-\operatorname{Ad}P)(\operatorname{Ad}(\mathbf U_4)H_3+H_4)\).
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

**Lemma 8 (ambient tower estimate).** Let an ambient separated sequence have scale \(l(x)\), and let a separated subordinate sequence of depth \(p\) have scale \(\xi'(x)\le l(x)\). Choose \(\bar a\) before \(a_T\) with \(\bar a<\delta_B/(4C_QL)\); this ceiling is imposed here, not by row 4's \(\widehat a\). A tower element at \(x\) is **settled** if the two sequences agree in the \(l(x)\)-neighbourhood of its stencil, or the subordinate sequence has reached its final level throughout that neighbourhood. Put \(s(x)=l(x)/\xi'(x)\). Define
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

**Lemma 9′ (CORE for R1).** Let \(i\ge1\), \(0<\tau_0<1\), and \(\sup_e2(b_0+b_1)(e)\le a^\sharp\). Suppose every simple and tower radius of \(P\in\mathcal U_i^{\rm el}(X)\) is reduced by \(1-\tau_0\), with the same witness bounds. If
\[
 |H(b)|,|\nabla^{\mathbf U}H(b)|<
 s(b):=\frac{\tau_0b_0(b)}{18K^\flat(1+c_\natural)},\qquad
 |\mathbf J+K|(b)<b_0(b),                                             \tag{55}
\]
then \(P\dotplus h\in\mathcal U_i^{\rm el}(X)\), holomorphically on its fixed-real-factor slice.

*Proof.* Any stencil bound \(s_e\) is at most \(\chi_c\tau_0b_0(e)/[18K^\flat(1+c_\natural)]\). Equation (46) gives increments at most \(2s_e\) for potential and derivative, and \(4s_e\eta_i^2\) for curvature. They are smaller than the available local gaps because \(K^\flat\ge4\chi_c\). The current condition is assumed and the real factor and witnesses stay fixed.

For a tower of depth \(p\), put \(\lambda_p=L^{-(i-p)}\); this is a change-of-unit factor, not a record lift. Its normalized quantities (48) are exactly the two \(G_n\) in (R2). Equation (46) puts both input potentials in Lemma 8's absolute ball. That lemma gives the open continuation domain and
\[
 |\Delta G_n(e)|\le e^{4\delta_T}K_T
   \max_b e^{-\delta_Td^\circ(x_e,b_-)}
   \max\{\lambda_p|A''-A'|,\lambda_p^2|\nabla^U(A''-A')|\}
 \le\frac{2K^\sharp\chi_c^2}{18K^\flat(1+c_\natural)}
       \tau_0b_0(e)\lambda_p<\tau_0b_0(e)\lambda_p.
\]
The extra \(\chi_c\) safely includes neighbouring stencils. The real tower is unchanged. This proves every core clause without a condition on \(b_1^2/b_0\). The logarithm and tower maps give holomorphy. ∎

## 7. Formation, inherited domains and the actual fibre

**Lemma 10 (formation with unit lift; Proposition U).** Assume A1/F0/REG as well as the stated inputs. At an operation of level \(t\), let \(k_\sharp=t-N_t^0\). For the original layer \(l(x)\), set
\[
 e_j(x)=\begin{cases}
 0,&j\le k_\sharp,\\
 (j-l(x)-1)_+,&j>k_\sharp,\ k_\sharp<l(x)\le j,\\
 j-k_\sharp-1,&j>k_\sharp,\ l(x)\le k_\sharp.
 \end{cases}
\]
On newly raised points set \(\mathcal E=e_j+1\); at healing set \(\mathcal E=e_{t-1}+1\). Inherit all other exponents. The formation input, at every datum loop and inherited carrier, is
\[
 L_\flat^{2\mathcal E(x)}\le C_R^2\ell_{m(x)}^{2r_R},                  \tag{56}
\]
\[
 |\partial V(\tau)-I|\le C_{\rm te}L_\flat^{2\mathcal E(\tau)}
                           \varepsilon_{m(\tau)},\qquad
 C_{\rm te}=6C_{\rm sm}L^4.                                         \tag{58}
\]
A loop exponent means the minimum assigned exponent over its complete test stencil. Under GEO, AV/CURV, PROF/RCG4 and the ceilings (T1)–(T3), all simple, tower, R1-core and witness records form at the plain real triple with base multiplier \(c_{\min}/4\). Natural and absolute clauses have the corresponding strict margin.

*Proof.* New exponents are at most \(N_t^0-1\); the bound on inherited exponents is still an input. The stage-to-layer conversion used in (58) is
\(3L^2L_\flat^{2e_j}\varepsilon_j\le6L^2L_\flat^{-2}L_\flat^{2(e_j+1)}\varepsilon_{j+1}\).
The adjacent ratio for \(\varepsilon\) follows just as (T2). AV/CURV supplies at most \(C_{\rm sm}L^2\) at a seam. An unchanged row keeps its previous test; prepared nesting bounds a retained shell's exponent by that of its last raising stage. These are the three cases of SA 17624. This explains the test comparison; the actual support of those tests remains the formation input.

Write \(D=d(x,x_\tau)\), \(m=m(x)\), \(v=m(x_\tau)\). Lemma 2 gives \(|v-m|\le1+D/\rho_0\). Bounded frame increments give
\(\ell_v^{2r_R}\le C\ell_m^{2r_R}(1+D)^{2r_R}\), and the adjacent test ratios give
\(\varepsilon_v/\varepsilon_m\le2^{|v-m|}\le2e^{\delta D/4}\).
Thus PROF and (56)–(58) imply
\[
 l^2\eta^{-2}|\partial U-I|,\quad l^3|J^\circ_\eta(U)|
 \le C_U\ell_m^{2r_R}\varepsilon_m,                                  \tag{59}
\]
where one may take
\(C_U=2CC_PC_{\rm te}C_R^2\sup_{D\ge0}(1+D)^{2r_R}
 e^{-(\delta_P-\delta/4)D}\).
This supremum is finite: an exponential dominates each fixed polynomial by its power series. All constants precede \(\kappa\). Equations (59) and (T1) give the uniform formation estimate \(\epsilon_{\rm f}r_0(m)\). This is the replacement for the smoothed lift; no record needs that lift.

For \(m\ge i\), (T2) gives
\[
 r_0(m)L^{-a(m-i)}\le r_0(i)(2L^{-a})^{m-i}\le r_0(i),\qquad a=2,3.    \tag{60a}
\]
Simple curvature and current at a core address are therefore at most \(\epsilon_{\rm f}r_0(i)\); the potential is zero. The target element radius, with the formation multiplier, is at least \(c_{\min}^2r_0(i)/4\). Incomplete-star plain currents are zero. Restriction identifies real towers up to a real gauge. For the core's subordinate scale \(\lambda_p\le1\), their curvature and current gain at least \(\lambda_p\) relative to the normalized estimate in level-\(i\) units. Equation (60a) therefore proves (R2). For ordinary tower records use \(\ell=\min(m,i)\):
\(r_0(m)L^{-2m}\le r_0(\ell)L^{-2\ell}\) and
\(r_0(m)L^{-3m}\le r_0(\ell)L^{-2\ell-\min(n,\ell)}\).
P81 and AV give the open datum domains.

For a witness cube of side \(s\) at level \(i\), its enlargement has layers \(\ge i-1\). Equation (60a), including the one adjacent lower layer, bounds its curvature by \(wL^2\eta_i^2\) and current by \(wL^3\), with \(w=2\epsilon_{\rm f}r_0(i)\). The Wilson divergence differs from \(\eta_i^2J^{(i)}\) by at most
\(6\eta_i^{-1}(wL^2\eta_i^2)^2\).
For \(w\le1/(12L)\), this is at most \(wL^3\eta_i^2/2\), also at \(i=0\); hence RCG4 applies when \((s+2)L^3w<c_{\rm rg}\). It gives
\[
 |A|,|\nabla A|<8L^3B_*(s+2)\epsilon_{\rm f}r_0(i).                  \tag{60}
\]
Choose \(C_g\) above the quotients of \(8L^3B_*(s+2)\) by each \(g_Q\). Those quotients are bounded independently of \(M\), since \(s\le C LM\) and every \(g_Q\) contains \(M\). For natural cubes \(s\le12M_1\), use the cube itself as its containing cube and a separate absolute ceiling. The definition of \(\epsilon_{\rm f}\) pays all formation margins, including the coefficient's \(c_{\min}\). The RCG4 and logarithm ceilings follow from (T3) after \(M\). All stencils and enlargements must be supplied; no field is extended across a missing carrier. ∎

**Proposition R0 (old-table counterexample, corrected scope).** Assume \(r_R>0\). For the discarded table \(r_\iota(i)=\alpha_\iota\varepsilon_i\), pointwise bounds (56), (58) do not imply a scalar core formed with \(\inf_X(c\lambda)\), uniformly over arbitrarily large addresses. Here only, define the diagnostic envelope
\(\lambda(x)=\max_z L_\flat^{2\mathcal E(z)}e^{-\delta d(x,z)/4}\).
This is a counterexample for the analytic test class, not a constructed BOX output.

*Proof.* Fix \(K\ge1\) and the old coefficients. Choose an integer \(E\) with \(C_{\rm te}L_\flat^{2E}/4>K(1+\beta_s)\alpha_0\), and then \(\theta_i\) large enough for \(L_\flat^{2E}\le C_R^2\ell_i^{2r_R}\), the coupling ceiling and all smallness conditions below. Use a single-layer determining system \(m=i\) on a sufficiently large finite torus. Put exponent \(E\) on a region containing every datum loop affected by one row \(c_1\), and zero elsewhere. Put \(x_1\) in that region and choose \(x_f\) at distance at least
\((8E\log L_\flat+4\log2)/\delta\) from it. Then \(\lambda(x_1)=L_\flat^{2E}\) and \(\lambda(x_f)=1\). A connected core address containing both has \(\inf_X\lambda=1\), disproving any fixed comparison of \(\lambda(x_1)\varepsilon_i\) with \(\varepsilon_i\inf_X\lambda\).

Set all row values to \(I\) except \(V(c_1)=e^{i\varphi\sigma_3}\), with
\(2\sin(\varphi/2)=C_{\rm te}L_\flat^{2E}\varepsilon_i/2\).
Every affected loop has this curvature and lies in the exponent-\(E\) region; the other loops are flat. The datum is regular for large \(\theta_i\), since a fixed logarithmic power times \(\theta_i^{-1/2}\) tends to zero. A1 supplies its regular background. If \(v\) is the largest normalized fine curvature in one affected loop's averaging carrier, AV/CURV's single-layer bound gives
\(v\ge C_{\rm te}L_\flat^{2E}\varepsilon_i/4\), or else \(v\) already exceeds the fixed analytic ceiling. A scalar radius at most \(K(1+\beta_s)\alpha_0\varepsilon_i\) is violated for large \(E\). Include the full averaging carrier in \(X\). All comparisons are explicit; no run is used. ∎

**Correction to R0 as stated in `st1-draft3.md`.** Its asserted *actual output* is not constructed. SA 17583 supplies an eligible component, not the arbitrary chosen output datum. In particular flat exterior data do not license an arbitrarily prescribed nonflat interior box minimizer. The proof also needs every loop affected by \(c_1\), not just one loop, to have exponent \(E\). The analytic counterexample above supplies that condition. The actual-output strengthening remains **Outstanding** and is not used.

**Proposition R° (scalar formation under the new table).** Under (Tq0) even the scalar comparison core with \(b_\iota=r_\iota(i)\inf_Xc^*\) forms after a ceiling on \(\gamma\). Indeed (59), (T1) and (60a) bound every simple quantity by \(\epsilon_{\rm f}r_0(i)\), uniformly over \(X\). Restriction gives its towers, and (60) gives its gauges with room for the additional factor \(\inf_Xc^*\ge c_{\min}\). Thus R0 does not apply to (Tq0). More generally, if its diagnostic lift were retained, \(\inf_X\lambda\ge1\) only increases those scalar target radii; the same proof works. We retain R1 as requested, but it is no longer necessary to cure a formation obstruction.

**Lemma B1 (output admission).** Under BOX-bg and GEO-box, output formation follows from Lemma 10. If one also wishes to keep the old real-test comparison (58) at the output, RUN-low enforces it by the ceiling
\[
 C_{\rm bx}C(M)\le C_{\rm te}L_\flat^{2(N_t^0-1)}.                    \tag{B1}
\]
*Proof.* On the affected loops GEO-box gives \(\mathcal E=N_t^0-1\). The identity \(L^{N_t^0-1}=R_{k_\sharp+1}\) and RUN-low imply
\(L_\flat^{2(N_t^0-1)}\ge[c_N(2\log\gamma^{-1})^r]^{2\log L_\flat/\log L}\to\infty\).
Thus (B1) holds after \(M\). Other output loops obey the converted inherited tests by BOX-bg. Lemma 10 then applies everywhere, including near the box, using the full profile maximum, not just the loop at the observation point. The BOX curvature/chart ceiling \(C(M)\varepsilon_t<a_\Lambda\) is imposed separately. ∎

**Lemma 11 (half-gap substitution and conditional drift).** For compatible records (13), define
\[
 \|h\|_w=\max_b\frac{\max\{l_+(b)|H|,l_+(b)^2|\nabla^UH|,
                                      l_+(b)^3|K|\}}{w(m_+(b))}.       \tag{63}
\]
Use the input sequence for \(l_+,m_+\). Assume all the absolute ceilings and witness carriers of Section 2, and that on active bonds \(A'\) is in the small logarithm chart. There are fixed constants, for example after fixed increases of
\[
 K_{\rm pt}=2^{15},\quad K_{\rm tw}=64e^{4\delta_T}K_T,\quad
 K_{\rm core}=8L^3C_{\rm os}K^\flat(1+c_\natural)/c_{\min},            \tag{64}
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

For an R1 element let \(b_\iota^{\rm mid}(e)=(b_\iota^-(e)+b_\iota^+(e))/2\). Both indices have the same fractional gap. Monotonicity of the infimum and Lemma 1′ / M2 give
\[
 \tau_e:=\frac{b_0^-(e)-b_0^+(e)}{b_0^-(e)+b_0^+(e)}
 \ge\tau_0:=\frac{d_*(i)}{2(1+\beta_s)}\ge\tfrac25d_*(i),\qquad
 b_0^{\rm mid}(e)\ge c_{\min}r_0(i).
\]
Input radii are \((1-\tau_e)b^{\rm mid}(e)\), hence at most \((1-\tau_0)b^{\rm mid}(e)\). Incident bonds may start in layer \(i-1\); (66) and the adjacent ratio bound give each shift quantity at most \(4L^3rw(i)\). Equation (64), with \(K^\flat\), and the fixed decrease of \(r_*\) put these bounds below (55) for \(\tau_0\); the current remains below its midpoint radius. Lemma 9′ applies simultaneously to every element. Witnesses are unchanged under substitution. Restriction commutes with (10), since \(\eta_iL^{-(j-i)}=\eta_j\).

For drift, work at a fixed frozen record and telescope over transitions. At a physical step write
\(U_{\rm old}=(e^{i\eta H}U_{\rm new})^g\), with \(g\) real. After a real gauge, the reverse shift is \(-\operatorname{Ad}(g)H\). Its covariant-difference norm is not exactly the forward norm: the change of transport is bounded by \(C|H_\mu||H_\nu|\). The small absolute ceiling bounds this by a fixed multiple of the forward norm. Decrease \(r_*\) once to pay it. The already proved increment estimates, applied inductively on each fixed read, then cost at most its coefficient drop divided by \(32\). For physical currents use Lemma 12's exact current identity; for towers use P81's intrinsic reading and real gauge covariance. Potential components of a plain triple are zero.

A real gauge witness is transported, not declared unchanged under drift. In its old real gauge, take the logarithm of \(e^{-i\eta H'}e^{i\eta A}\). The same difference calculation, with \(|A|,|\nabla A|\) below a fixed ceiling by (T3) and (60), bounds the change of both ordinary gauge norms by \(C r_*d_*(i)r_0(i)\). The recorded witness bound dominates \(r_0(i)\); for natural witnesses impose this as another coupling ceiling relative to \(a_\flat\). Choose the fixed reduction of \(r_*\) so the total cost is less than a quarter of that bound.

All coefficient drops telescope and their total is at most
\(1+\beta_s-c_{\min}\le41/64\).
The formation contribution is at most
\((c_{\min}/4)(1+\beta_s)R\); adding \((41/64)R/32\) is strictly below \(c_{\min}R/2\). The absolute real clause follows from the same curvature increment bound and the fixed \(a_T\) ceiling. This proves the conditional drift assertion. Formation is Lemma 10 and B1; ledger gaps are Lemma 1′ / M2. The physical response and coordinate/contour supplies remain explicit premises. ∎

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

### The stage chart and its measure

**Lemma F1 (one strip bond).** For a real traceless Hermitian \(H\), let \(\vartheta\) be smooth, zero on \([0,4/3]\), one on \([5/3,\infty)\). Put \(\theta(e^{iA'})=\vartheta(|A'|/\delta)\), \(\theta(-I)=1\), with \(0<\delta\le1\) and \(8\|\vartheta'\|_\infty|H|\le\delta\). Then
\[
 \Psi_H(W')=W'e^{-i\theta(W')H}e^{iH},\qquad
 f_H(A')=i^{-1}\operatorname{Log}(e^{iA'}e^{-i\theta(e^{iA'})H})           \tag{F1}
\]
defines a real diffeomorphism \(\Psi_H\) of \(SU(2)\), with Haar Jacobian
\(1-\vartheta'(|A'|/\delta)\langle A',H\rangle/(\delta|A'|)\in[7/8,9/8]\).
In the cutoff case \(f_H(A')=A'\) for \(|A'|\le4\delta/3\). In the plain case \(\theta\equiv1\), \(\Psi_H\) is the identity but \(f_H\) generally is not. In either case \(\big||f_H(A')|-|A'|\big|\le\theta|H|\) where the real principal logarithm exists.

*Proof.* Radial differentiation on \(SU(2)\) gives
\(\alpha(X)=\vartheta'(|A'|/\delta)\langle A',X\rangle/(\delta|A'|)\).
The right-trivialized derivative is an adjoint conjugation times \(I-H\otimes\alpha\), whose determinant is \(1-\alpha(H)\). The radial cutoff is constant near both chart poles. In the bi-invariant geodesic metric its Lipschitz constant is at most \(\|\vartheta'\|_\infty/\delta\). For fixed \(W\), the inverse equation
\(W'=We^{-iH}e^{i\theta(W')H}\) is a contraction of constant at most \(1/8\) on the compact group. Thus it has exactly one solution, and the invertible derivative gives a smooth inverse. The last inequality is the group-angle triangle inequality in both directions. This is the SU(2) argument in Y3 46472–46559. ∎

For a stored strip row, SA 17521–17526 gives
\(D=W'e^{-i\theta H}V^{\rm bg}\); its raw datum relative to \(V^{\rm bg}\) is (F1). The cutoff itself is not holomorphic. Its real stored variable belongs to the near/Borel tier. If \(\theta=1\), the product and its small logarithm are holomorphic on their declared complex chart. These statements do not put arbitrary stored strip fields in a small source ball; the main-step source bound remains a supplied premise.

**Lemma F2 (regional fibre chart).** Write \(\mathfrak E=\Gamma^{\rm rm}\), \(\mathfrak C=\Gamma^{\rm ad}\), and \(\mathfrak F=\mathfrak E\setminus\{b_0(c):c\in\mathfrak C\}\). Retained rows are held fixed. Define
\(q_V(a)(c)=i^{-1}\operatorname{Log}(F_c(e^{ia}V)F_c(V)^{-1})\),
\(K_V=Dq_V(0)\), and \(J_c=D_{a(b_0(c))}q_{V,c}(0)\).
Let \(h_Vv\) vanish on free rows and equal \(J_c^{-1}v(c)\) at pivot \(b_0(c)\).
If \(\iota_{\mathfrak F}u\) extends \(u\) by zero on pivots, put
\(\mathsf C_Vu=\iota_{\mathfrak F}u-h_VK_V\iota_{\mathfrak F}u\).
CH supplies isolated pivots and
\[
 q_V(a)=K_Va+R_V(a),\quad K_Vh_V=I,\quad K_V\mathsf C_V=0,\quad
 \|h_V\|\le2L^3,\quad\|\mathsf C_V\|\le C L^4,
\]
where \(h_V\) is supported only on pivots and each equation reads its own pivot. The remainder obeys \(\|R_V(a)\|\le CL^2\|a\|^2\) and \(\|DR_V(a)\|\le CL^2\|a\|\) on the common chart. There are fixed positive radii \(r_1=cL^{-5}\), \(r_u=c_{\rm ch}L^{-9}\) and \(r_{\rm sol}\), chosen smaller if necessary, such that
\[
 d=R_V(t-h_Vd),\quad\Psi_V(t)=t-h_Vd(t),\qquad
 a_V(u)=\Psi_V(\mathsf C_Vu),\quad q_V(a_V(u))=0,\quad a_V(u)|_{\mathfrak F}=u,
\]
\[
 \|a_V(u)\|+\|D_ua_V(u)\|\|u\|\le C_{\rm ch}L^4\|u\|
             \quad(\|u\|<r_u).                                      \tag{F2}
\]
The maps are jointly holomorphic in \(u,V\), and real for real arguments. Any solution with \(\|a\|<r_{\rm sol}\), \(\|a|_{\mathfrak F}\|<r_u\), is this graph. The number \(r_{\rm sol}\) is a small **full-coordinate** uniqueness radius; it is not silently \(c_{\rm ch}/2\).

*Proof.* On \(\|t\|<r_1\) the displayed fixed-point map sends \(\|d\|\le CL^2\|t\|^2\) into itself, for a fixed enlargement of the remainder constant, and has Lipschitz constant at most \(CL^5r_1<1/2\). Its iterates converge geometrically and locally uniformly; hence the solution is unique and holomorphic. Differentiating and summing the Neumann series gives \(\|Dd\|\le CL^2\|t\|\) and \(\|D\Psi-I\|\le CL^5\|t\|\). Conversely \(t=a+h_VR_V(a)\) satisfies \(K_Vt=0\) whenever \(q_V(a)=0\), and has the same free coordinates as \(a\). Choose \(r_{\rm sol}\) so this \(t\) stays in the contraction ball. Then \(t=\mathsf C_V(a|_{\mathfrak F})\), and uniqueness gives the assertion. Finally choose \(r_u\) so \(\|\mathsf C_Vu\|<r_1/2\) and \(\|a_V(u)\|<r_{\rm sol}/2\); the derivative bound proves (F2). For general \(t\) in the ball the same construction gives \(q_V(\Psi_V(t))=K_Vt\), as used in F3. Different equations can share free rows; no product decomposition of the free variables is asserted. These are SA QC22–QC24 (8257–8299), with their actual small-solution converse. ∎

**Proposition F3 (exact local fibre measure).** Fix real retained data and a real reference \(V\) with \(F(V)=W\). In the local chart of F2, define the group-delta fibre measure by the real coordinate change below. Let
\(Q(a)=\tfrac12\operatorname{tr}a^2\), \(S(z)=(\sin\sqrt z/\sqrt z)^2\), interpreted by its entire power series, and let \(\sigma_H>0\) normalize Haar measure. Put \(J_c=D_{a(b_0(c))}q_{V,c}(0)\). For \(u=gB\), the fibre density is
\[
 d\nu_W(B)=(\sigma_Hg^3)^{|\mathfrak F|}
 \left[\prod_{c\in\mathfrak C}(\det J_c)^{-1}\right]
 \det D\Psi_V(\mathsf C_VgB)
 \prod_{b\in\mathfrak E} S(Q(a_V(gB)(b)))\,dB.                       \tag{F3}
\]
In particular the Haar product includes **pivots and nonpivots**. For any nonnegative Borel density \(\omega(D)\), tests \(\chi(D)\) and observable \(\Upsilon(D)\), supported in this chart,
\[
 \int\!\prod_{b\in\mathfrak E}dD(b)
       \prod_{c\in\mathfrak C}\delta_G(F_c(D)W(c)^{-1})
       \chi\omega\Upsilon(D)
 =\int\chi\omega\Upsilon(e^{ia_V(gB)}V)\,d\nu_W(B).                 \tag{F0}
\]
The complex integrable case follows by absolute integrability. All previously stored densities, normalization factors, strip Jacobians and cutoffs belong to \(\omega\) or \(\chi\); none is discarded.

*Proof.* In real coordinates \(D=e^{ia}V\), each Haar factor is \(\sigma_H S(Q(a_b))d^3a_b\), and
\(\delta_G(e^{iv})=\sigma_H^{-1}\delta_{\mathbb R^3}(v)\).
Use \(t=\mathsf C_Vu+h_Vv\), then \(a=\Psi_V(t)\). The first determinant is \(\prod_c\det J_c^{-1}\), and \(q_V(\Psi_V(t))=v\). Eliminating \(v\) leaves \(\sigma_H^{|\mathfrak E|-|\mathfrak C|}\), the determinant of \(D\Psi\), and **all** Haar factors. Now \(|\mathfrak E|-|\mathfrak C|=|\mathfrak F|\) and \(du=g^{3|\mathfrak F|}dB\). In a local real unitary frame \(J_c\) lies within half of \(L^{-3}I\); adjoint frame changes have determinant one. Its determinant is positive, as is \(\det D\Psi\) by \(\|D\Psi-I\|<1/2\). Thus ordinary change of variables and Tonelli prove (F0). This supplies a specified fibre version at each admitted \(W\), rather than drawing a pointwise conclusion from an almost-everywhere disintegration.

This is SA QC25 (8310–8360); Y3 46258–46387 gives the same Haar accounting. Its coefficients continue holomorphically by their positive real branches and \(S(Q(a))\). A complex norm squared is not used in a holomorphic density. No complex measure or complex delta is asserted. If one instead uses the right-trivialized pivot derivative \(N_c(D)\) along the graph, its factor is \((\det N_c(D))^{-1}\); a relative determinant of \(N_c(D)\) enters with a minus logarithm. The draft reversed this factor and omitted the pivot Haar densities. ∎

**Outstanding F-measure (identification with a stored stage presentation).** Formula (F0) gives exact coordinates for the regional Haar/delta integral with its full density. To call it the already stored CA-I \((A_j,B_j)\) stage, its actual conditional law must be exhibited in this form, with every retained factor in \(\omega,\chi\), or an exact change from those coordinates must be supplied. SA 17531 includes stored Gaussian factors; CA-I 54287–54316 specifies two fluctuation integrals. A bare Haar/delta formula with an arbitrary \(\Upsilon\) does not prove this identification. One may **define** the passing operation by (F0), retaining its complementary failing piece; equality with a different previously specified operation remains this input. F1 and F3 are the available real changes of variables, not a proof that every omitted factor equals one.

**Theorem F4 (constructed datum map).** Fix an admitted real reference \(D_+^0\) and let \(U_+=\Phi_{D_+^0}(B_{D_+^0}(D_+))\), \(V=M_-(U_+)\) on its admitted raw-datum chart. Set \(C_{\rm tube}=9/4\) and
\[
 \mathcal T_j=\{B:g_j\|B\|_\infty<C_{\rm tube}\delta'_j\},\qquad
 D_{\rm old}(B;D_+)=e^{ia_V(g_jB)}V\quad\hbox{on }\mathfrak E,          \tag{F4}
\]
and copy \(V\) on retained rows. Suppose \(C_{\rm tube}\delta'_j<r_u\), and let
\(h_j=\max_{b\in\mathfrak E}|i^{-1}\operatorname{Log}(V^\sharp(b)V(b)^{-1})|\le\delta'_j/8\).
For the passing support also require \(h_j<r_{\rm sol}/4\). Then (F4) is jointly holomorphic, real on real data, and
\[
 F(D_{\rm old})=D_+,\qquad
 \|u\|<C_{\rm tube}\delta'_j,\quad\|a_V(u)\|\le C_{\rm ch}L^4 C_{\rm tube}\delta'_j,
 \quad\|b_V(a_V(u))\|<C'_A\delta'_j.                                \tag{70}
\]
Here \(C'_A=C_{\rm red}C_{\rm ch}L^4C_{\rm tube}\), with a fixed analytic reduced-coordinate bound \(C_{\rm red}\). Shrinking the complex reference chart to have \(\|\operatorname{Ad}V\|\le2\), one may take \(C_{\rm red}=2+8C_vL\). This constant includes the factor \(9/4\) missing in the draft's constants table. The separate source constant \(C_A\) in (16), (71) is at least \(C'_A\).

Every real point of the passing support of (F0) has exactly one coordinate \(B\) in \(\mathcal T_j\). The reduced source is supported on removed rows and the outward rows whose block factors read changed rows. Its **full carrier** includes these adjacent double blocks. Under GEO's boundary buffer for this carrier, the physical identification of Lemma 12 holds, with DR's regularity, uniqueness and source-domain ceilings still imposed.

*Proof.* F2 and the finite average give holomorphy and reality. Equation (67) gives \(F(V)=D_+\); F2 gives the same equation for \(D_{\rm old}\), and free logarithms are exactly \(u=g_jB\). On the real passing support the group-angle triangle inequality gives free logarithms relative to \(V\) below \(\delta'_j+h_j\le9\delta'_j/8\), and full logarithms below \(r_{\rm sol}/4+h_j<r_{\rm sol}/2\). F2's converse applies, and the free logarithms determine \(B\) uniquely. F3 then reconstructs the complete integral (F0).

On an outward row use (7). Its one-step factor has \(|v_z-I|\le C_vL\|a\|\). The logarithm series on a fixed smaller ball, including the complex \(\operatorname{Ad}V\) bound, gives \(|b(c)|\le C_{\rm red}\|a\|\). This proves (70) on the whole tube, not just real data. Outside the specified carriers all entries and factors are unchanged. Require their distance from \(\partial\Omega_0\) to exceed \(2\eta\); merely locating the shell in the interior is insufficient. Lemma 6 and uniqueness then give Lemma 12's potential, current, and stored-transport identities. Source smallness alone does not establish those uniqueness hypotheses; they remain the named inputs. ∎

**Lemma F5 (contour containment, conditional).** Put \(b_j=9\delta'_j/(8g_j)\). Every contour point with
\(|\Re B(b)|+|\Im B(b)|<b_j\) on every free row lies in \(\mathcal T_j\). So does a contour with \(|\Re B(b)|<b_j\) and \(|\Im B(b)|\le\epsilon_m b_j\), \(\epsilon_m<1\). Indeed \(g_j|B(b)|\le g_j(|\Re B(b)|+|\Im B(b)|)<9\delta'_j/4\). If \(m_r\) is real and \(|m-m_r|\le\epsilon_m b_j\), a translated contour has this imaginary bound whenever its real part stays in that region.

**Outstanding F-contour.** The draft's full-contour claim needs these inequalities for the *actual* four-dimensional conditional mean and contours, uniformly in the switches and complex external pairs. Y3 51920–51933 assumes the mean bounds; 51984–52014 states its estimate under additional precision and smallness hypotheses. ST-test does not prove them. Moreover its localized-reference passing set becomes
\(\chi(e^{ia_V(gB)}V;V^\sharp)\), generally not a product of balls centered at zero. Inclusion of its real support in \(|B|<b_j\) does not replace that cutoff by the larger ball or make the indicator holomorphic. A valid contour deformation for this exact cutoff, or a separately specified equivalent test and its history bounds, must be supplied. F4 proves a holomorphic map on the tube and F5 proves the stated geometric containment; neither proves that deformation or its integral estimate. Failed stages keep their failure factors and are not included in this passing-support substitution.

**Lemma F6 (localization discrepancy).** Under either stated LOC clause, RUN-low, RUN and (15), \(h_j\le\delta'_j/8\) after a ceiling on \(\gamma\).

*Proof.* For LOC-form, integrate (15) along its **assumed common-chart segment**. AV and the bounded carrier/gauge conversions give
\[
 h_j\le C_F r_B\sum_{c:\,d(c,\mathrm{carriers})\ge R_\sharp}
                    e^{-\theta_4d(b,y_c)}
 \le C'_F e^{-aR_\sharp}S_4(a),\qquad a=\min(1,\theta_4/2).
                                                                    \tag{F6}
\]
Fixed carrier diameters have been included in \(C'_F\), not asserted to equal two. Lemma 2's summation applies since \(a\rho_0\ge16\log L\). For LOC-decay this step is the hypothesis. Now \(R_\sharp\ge MR_t/4\ge c_N\ell_t^r/4\). Also \(t-j\le N_t\le C_N\ell_t^r\); bounded increments give \(|\theta_j-\theta_t|\le C\ell_t^r\), so \(\theta_j/\theta_t\in[1/2,2]\) for small \(\gamma\). Since \(r>1\), for any fixed \(A>0\), \(c\ell_t^r>A\ell_t\) eventually. Hence \(e^{-c\ell_t^r}/(A_1\theta_j^{-1/2}\ell_j^{p_1})\to0\), uniformly over the stage window. Impose its supremum at most \(1/8\). This also gives \(h_j<r_{\rm sol}/4\). ∎

The draft inferred the common raw chart in LOC-form from real regularity of two data. That inference is not valid; the common-chart segment is now explicit, or LOC-decay can be used directly.

**Lemma F7 (test locality).** Assume the quarter-cell localization rule in ST-test uses only its declared data, and the remaining bond/pivot/collar read reach is at most another quarter-cell, as a GEO locality requirement. Non-touching level-\(t\) cell components have distance at least one cell. Their complete test reads then remain disjoint from the other component's changed variables. Thus changing one such component does not change the other's ST-test.

*Proof.* Enlarge one component first by a quarter-cell and then by the read reach. Every read is within half a cell; the other component is at least one cell away. The assertion follows by distance subtraction. The reach bound is enforced by the actual carrier specification and the required size floors; it cannot be inferred just from \(X_1^\sharp\cap X_2=\varnothing\). This verifies the locality part of SA 17449 for this test. It does not prove its older-test implications, failure gains or exact stored-density representation. ∎

For main steps, (F1) supplies the real strip map and (F2) the small fibre graph. Integrated free rows use \(u=gB\); small stored rows use \(u=f_H(A')\). The source and full-coordinate bounds must cover both sets, with cutoff variables treated as Borel. This does not discharge the pre-existing main-step FL supply for arbitrary stored fields. For stages defined by (F0), F4 gives their actual datum map; using another stored presentation requires F-measure and, when a complex contour is consumed, F-contour.

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

For main steps, \(\delta_{\rm src}=\delta_{t-1}=A_1g_{t-1}\ell_{t-1}^{p_0}\). For stages at \(j=t-N_t+n\), \(\delta_{\rm src}=\delta'_j=A_1g_j\ell_j^{p_1}\). All fixed completion and reduced-datum losses are included in the \(C_A\) of (71); this may be larger than F4's tube factor \(9/4\). There are structural constants, independent of \(M,\bar\kappa,C_0,A_1,b_f\), with
\[
\begin{split}
 a_X&\le C_{\rm main}E_{\bar\kappa}\frac{A_1}{C_0}
                  \ell_{t-1}^{p_0-q}
            +D_{\rm src}K_{\rm pin}/\epsilon_{\rm lev}&&\text{(main)},\\
 a_X&\le C_{\rm st}E_{\bar\kappa}\frac{A_1}{C_0}
                  \ell_j^{p_1+r-q}
            +D_{\rm src}K_{\rm pin}/\epsilon_{\rm lev}&&\text{(stage)}.
\end{split}                                                         \tag{73}
\]
Both are uniformly below \(1/2\) by a ceiling on \(\gamma\) after all amplitudes. No precision constant reads these later amplitudes.

*Proof.* Lemma 4 converts the derivative convention and applies its profile bound to \(zH\): the pinning size is at most \(K_{\rm pin}|z|D_{\rm src}E_X\), and the normalized pinned shift is at most \(C_{\rm lev}|z|D_{\rm src}Q_X\). Equation (71) gives (72) and forces levelling throughout the disc; no nonholomorphic cutoff is varied there.

For the source comparison, removal at level \(j\) and one-step averaging change only layers within one of \(j\) in the old sequence. The outward correction uses one adjacent endpoint block. In the input sequence, only member \(j+1\) has changed, so all these carriers have \(|m_+-j|\le2\), with a fixed enlargement allowed in the carrier constant. Apply the separation argument (20) **to the input sequence**. For a read bond of layer \(m\) it gives
\[
 d_+(b,S)\ge\rho_0(|m-j|-3)_+-C_{\rm car}.                             \tag{74}
\]
The fixed \(C_{\rm car}\) pays endpoints of stencils and carriers. At a main step the same argument is one-sided, centred at \(j=t-1\). The draft used \(d_-\ge d_+\) in the wrong direction to transfer a lower bound on \(d_-\); (74) is the required new lower bound.

At a stage, (18) and RUN give
\[
 Q_X\le
 \frac{2e^{\mu C_{\rm car}/2}}{a_jr_0(j)}
 \sup_{\nu\ge0}4^\nu e^{-(\mu\rho_0/2)(\nu-3)_+}
 \le\frac{C}{a_jr_0(j)}.
\]
The supremum is finite by row 3. Since
\(a_j^{-1}=8N(\theta_j)/\beta_s\), \(N(\theta_j)\le C_N\ell_j^r\), and \(\delta'_j/r_0(j)=(A_1/C_0)\ell_j^{p_1-q}\), this proves the second line of (73). There is no factor \(2^{N_t}\).
For the main step replace \(a_j\) by a fixed multiple of \((1-\theta_s)\beta_s\); the same computation gives the first line. Finally \(q>p_0>p_1+r\), and \(g_j\ell_j^{p_0}\to0\), make the main, stage and pinning terms uniformly small. This argument preserves the explicit \(E_{\bar\kappa}\) factor. ∎

**Lemma B2 (output budget).** Use (71) with \(D_{\rm src}=C(M)E_{\bar\kappa}\delta'_t\) and \(S=S_{\rm bx}\). There is a structural constant \(C_{\rm out}\), independent of \(M,\bar\kappa,A_1,C_0,b_f\), such that
\[
 a_X\le C_{\rm out}C(M)E_{\bar\kappa}\frac{A_1}{C_0}\ell_t^{p_1-q}
       +C(M)E_{\bar\kappa}\delta'_tK_{\rm pin}/\epsilon_{\rm lev}.
                                                                    \tag{B2}
\]
Thus \(a_X<1/2\) after a ceiling on \(\gamma\) following BOX's constants.

*Proof.* The output gap gives
\(w(m)=\theta_s\beta_s2^{-(t-m)}r_0(m)/4\ge
\theta_s\beta_s4^{-(t-m)}r_0(t)/4\).
If the source lies exactly in layer \(t\), (20) gives
\(d_+(b,S)\ge\rho_0(t-m-1)_+\). Hence
\[
 Q_X\le\frac4{\theta_s\beta_sr_0(t)}
 \sup_{\nu\ge0}4^\nu e^{-(\mu\rho_0/2)(\nu-1)_+}
 \le\frac{16}{\theta_s\beta_sr_0(t)}.
\]
For GEO-box's fixed carrier enlargement, replace \(\nu-1\) by \(\nu-1-c_{\rm bx}\) and add its fixed distance loss; the supremum is still a structural constant. This is included in \(C_{\rm out}\). Now \(\delta'_t/r_0(t)=(A_1/C_0)\ell_t^{p_1-q}\), and \(E_X\le1\). Insert these in (71). Both terms tend to zero uniformly. Lemma 13 then forces levelling and (72) throughout \(|z|<\rho_X\). ∎

**Lemma B3 (output drift).** BOX-id and B2 give the real background relation required by Lemma 11, with the pinned shift of norm less than \(r_*/2\). Its pinning gauge is real on the physical locus, so it can be composed with BOX-id's real gauge; the current and stored-transport clauses are part of BOX-id. An output that only stops a drop-out and changes its label has zero physical shift and needs no box estimate.

**Lemma B4 (internal consumer admission).** Under all stated analytic and geometric inputs, the formation/support assumptions, the actual main-step source supply, and the stage coordinate identification when it is consumed, every frozen record is admitted at every later **real** background with half its declared radius. All ST1 uses of its witness radii are valid under the stated absolute ceilings.

*Proof.* Simple, tower, core and gauge formation is Lemma 10; box formation is B1. Ledger gaps are Lemma 1′ / M2. Stage physical identities are Lemma 12 and F4 on the reconstructed passing support; main-step identities still use the supplied small stored/integrated source map. Their budgets are (73); box identities and budgets are B2–B3. Lemma 11 now telescopes each frozen read, including swallowed-mark transitions. Initial and unfinished records require their expressly supplied base admission/comparisons. Stopped stages retain their existing records and factors.

For a witness \(W_Q=g_Qr_0(i)\), (T3) makes its potentials small on the actual required carriers for REG/OPS and the logarithm estimates. Real substitution leaves the witness fixed; real drift transports it and costs at most \(Cr_*\sum d_*(i)r_0(i)\), paid by the fixed reduction of \(r_*\) and \(W_Q\ge r_0(i)\) (choose the fixed witness factors at least one). Natural witnesses use the separate ceiling relative to \(a_\flat\). The Borel argument uses only strict bounds. This verifies these bound comparisons; it does not prove the imported operator theorem on the supplied class. Admission of real backgrounds also does not assert that an arbitrary complex point lies in the chain domain. ∎

**CI (external consumer interface; Outstanding, owned by NL1/LF1).** Every carried activity must be defined and bounded by its declared \(b_f\) on the **whole** ST1 chain domain with (Tq0), the permanent ledger, R1 cores, frozen intrinsic tower functions and the prescribed witness carriers/constants. It must have the holomorphic, Borel, covariance, stored-variable and tie properties in Section 1. **No constant fixed before \(\kappa\) reads \(b_f\); in the quantitative substitution conclusion, \(b_f\) enters only the output bound (77).** The amplitudes themselves may be chosen after \(M\), as SA 19469–19470 permits. They do not choose the domain radii, precision constants or source budget.

With \(\lambda=\Lambda_Q=1\), the three lift obstructions in `st1-draft3.md` §4.3 disappear: one is below every nonnegative printed raw lift. This is not a proof of CI. One still has to match the entire domain, its continuation supply, witness constants and hereditary reads, and establish NL1/LF1's formation estimates uniformly at every complex input pair there. A bound on the image of a fluctuation substitution only bounds that image; it does not bound the whole domain and already uses the old activity bound. The inductive reduction in `nl1-L-draft.md` §8.1 is valid **if** its formation estimates and locally uniform integrable/series majorants are supplied. Pointwise bounds on a final sum alone do not supply those majorants or holomorphy.

## 8. ST1

**Theorem 14 (hereditary substitution, physical identification and finite re-expansion).** Fix a finite four-dimensional lattice and a finite history with the records of Section 1. Use the constants in Section 2 in the stated order. Assume:

1. GEO (including GEO-mark, GEO-box and the actual locality/carrier bounds), RUN and RUN-low, AV/CURV, A1/F0/REG, P82°–M1 with (15), PROF/RCG4, OPS/SLICE/UNQ, and CH hold on every system used. The required IN1 precision and derivative constants are fixed before \(\kappa\), independently of \(M,\bar\kappa\). BOX, ST-test and one stated LOC clause are assumed for the transitions that use them.
2. The input point belongs to \(\mathcal D_{a|+}\) and all required R1 working cores. Every absolute, chart, gauge and source ceiling holds. Lemma 1′ / M2 supplies coefficient gaps on persistent identical records; compatibility still requires the target records themselves to be retained. Initial/unfinished entries have their separately supplied comparisons. B4 gives membership at actual real backgrounds; complex input membership remains this hypothesis.
3. DR is given on the full switch polydisc, with (16), specification at one, restriction and component splitting, and it vanishes in a source-free component and at zero switches. The completed source has (70) at chart stages, the supplied main-step bound, or BOX-resp at outputs. The source budget (71), or B2, has \(a_X<1/2\), uniformly over the parameters in use.
4. CI supplies the activity \(f\) on the target domain with bound \(b_f\). Every endpoint pillar and full read carrier is included in (71). Complex splitting descent requires the additional pair-function hypothesis; the real tie yields only the real assertion. No earlier domain or precision constant depends on \(b_f\).
5. For physical identification, use F4's constructed datum at stages, with Lemma 12's regularity, uniqueness and full-carrier boundary buffer; the corresponding actual main-step or BOX identity is supplied at those transitions. Stored slots satisfy GEO's lattice-site, margin and retirement conditions. If the claimed stage is a previously stored \((A_j,B_j)\) presentation, require F-measure's identification. If its full complex contour is claimed, require F-contour's actual mean bounds and valid deformation for the exact tests. Those two assertions are **Outstanding** for the round-3 draft as supplied.

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

*Proof.* Lemma 13 forces levelling on the full \(z\)-disc and gives (72). Lemma 4 makes the pinned shift holomorphic there and preserves stored transports. Lemma 11 puts it inside the target domain with room; Lemmas 5 and 8 supply the continuation domain. Thus composition with \(f\) proves the first bounded-holomorphic assertion. A norm-dependent levelling decision is used only to select a region where it is forced; it is not differentiated.

The formulas use finitely many continuous algebraic maps, fixed branches and the Borel activity interface. Witness existence is Borel as well: exhaust each strict real gauge bound by closed smaller bounds; the bounded real potentials and compact unitary gauges have compact continuous images, and then take a countable union and finite intersections. Near stored coordinates are held fixed. No analyticity in a merely Borel variable is used. Inactive outer coordinates of a bounded activity are constant in \(A',\mathbf J\), since each ranges over a whole complex line; Liouville's theorem allows their projection to zero when a local logarithm chart is needed. Substitution leaves them unchanged.

Lemma 12 identifies the complete physical pair and the boundary plain current. Lemma 4's real common-centre comparison, covariance and the activity's real tie give the second assertion. For complex splitting independence use its complex common-centre continuation and the additional pair-function hypothesis. The main-step rescaling is (9). No independent complex current is set equal to a physical current during this argument.

For (77), the function \(\Phi_Y(s,z)-f_0\) vanishes at \(z=0\) and is bounded by \(2b_f\). Cauchy in the distinct switch variables bounds its mixed derivative along \([0,1]^K\) by \(2b_f(e^{\bar\kappa}-1)^{-|K|}\); Schwarz in \(z\) contributes \(1/\rho_X\). Integrate that derivative over the unit cube to obtain the finite difference (76). This also covers \(K=\varnothing\), for which the subtraction is necessary. Since \(\bar\kappa\ge1\), \(e^{\bar\kappa}-1\ge e^{\bar\kappa-1}\).

Component splitting and the levelling collar property make the reading independent of every switched cell in a component missing the base or its source; its finite difference is zero. Regional consistency identifies readings on smaller \(Y\). Finally sum (76). For a fixed proper subset \(A\) the coefficient is \((1-1)^{|\mathcal C\setminus(X^\uparrow\cup A)|}=0\); the full subset has coefficient one. This is (78). The sum is finite; no convergence or interchange with a stored-field integral is asserted. Induction gives the finite nested identity. ∎

**Corollary 14′ (all admitted actual transitions).** Assume the declared inputs, CI, base formation for the initial/unfinished entries, the main-step coordinate/source supply, and the F-measure identification for every stage presentation being called actual. For statements on the conditional-mean contours, assume F-contour's bounds and exact-cutoff deformation as well. Then Theorem 14 applies, for real-background inputs and for complex inputs assumed to lie in the admitted domain, at every main step, preparatory passing stage and output of each finite history, including swallowed marks; stopped stages keep their unintegrated failure factors.

*Proof.* B4 supplies the real chain membership. Lemma 1′ / M2 supplies reset-stable coefficient gaps, and frozen records supply compatibility. F4 gives the passing stage datum and (70); the main-step map is the named supply. Lemma 13 and B2 give the source/pinning budgets, B3 gives output drift, and CI gives the target activity. These supply the five hypotheses of Theorem 14, with Lemma 12's regularity, uniqueness and source-threshold premises coming from the declared inputs rather than from F4, as F4's proof says. For complex inputs it applies on their admitted domain, and for an asserted integration contour use the additional containment/deformation supply. Induction over the finite ordered history proves the statement. ∎

The draft's phrase “proved, except CI” is too strong for its original input list. F3–F7 construct and bound a chart, but the unsupplied stored-measure and conditional-mean identifications cannot be removed from this corollary. Defining a stage by (F0) settles its measure convention; it does not settle F-contour or prove NL1/LF1's bounds.

## Definitions supplied in distillation

This list includes the inherited definitions needed to read the single manuscript and the round-3 completions. A definition does not establish a named analytic input.

1. Matrix/array norms, oriented bonds and complete stencils; Wilson action normalization and regional versus plain current, (1)–(2).
2. Bare/coarse units, determining rows and outward endpoints, nodes, residual gauges, criticality, pillars and weighted metric, (3)–(5), (9).
3. Raw datum versus reduced response coordinate; canonical comb versus averaged stored transports; intrinsic continuation tube, (6)–(8), (32).
4. Triples with an independent complex current, active-bond substitution, real ties and complex pair descent, (10) and Section 1.
5. The scalar comparison core, both erosion assignments, and R1's active elementwise core; separate radius sets and full function carriers, (11)–(12), R1–R2.
6. Frozen read/witness records, their effective scalar coefficients, chain intersections, midpoint room, formation multiplier, initial/unfinished-entry convention and same-frame radius retention, (13)–(14).
7. The running table (Tq0), test amplitudes \(\varepsilon,\delta,\delta'\), unit record lifts, raw test exponents, \(\epsilon_{\rm f}\), \(C_g\), \(K^\flat\), and the distinction between \(\lambda_p\) as a unit factor and a record lift.
8. Standing and permanent mark-debt sets, the comparison coefficients \(c,c^{\rm SA}\), completed-stage debt counted once per global operation phase, and phase/level indexing, M1 and (17)–(18).
9. Pinnable/levelled tops, forced levelling reads, convex real frames and prescribed transport pins, (23)–(31).
10. Fine/site/row pairings, the scalar mean and masses, projection, inverse, straightening, reduced action and multiplier, and specification at one, (33)–(44).
11. Settled towers, ambient/subordinate scales, weighted value/derivative norms and normalized curvature/current, (47)–(54).
12. Affected output-loop family and complete output source carrier; the strengthened GEO-box, common-chart LOC-form and local-read reach; BOX-bg/id/resp with independent source and chart ceilings.
13. Regional removed/added/pivot/free row sets, the raw constraint \(q_V\), pivot inverse \(h_V\), free-coordinate completion \(\mathsf C_V\), full-coordinate uniqueness radius \(r_{\rm sol}\), real strip map, and the local fibre measure with its chosen fixed-datum version, F1–F3.
14. Exact retained-density convention \(\omega,\chi\), holomorphic Haar polynomial variable \(Q(a)\), complete fluctuation tube, constructed datum map, reduced-coordinate constant and localization discrepancy, F0, F3–F6.
15. Exact-test contour supply and its distinction from support inclusion; source budgets, empty-source scalar radius, restriction map, localization hull and subtracted Boolean coefficient, F5 and (71)–(78).
16. CI on the whole complex chain domain, with the amplitude-order condition that no constant fixed before \(\kappa\) reads \(b_f\).

## Source checks

The SA and CA-I objects were located through `library/sa-index/`: README, neighboring rows in chunks 04–07 and 16–17, the corresponding obligations, and CA-I chunks 05–06, 09–10. Each source below was fetched once at `31a47c543775`; only bounded excerpts were read. The retained line-specific claims were checked against those files. The old broad historical citation inventory is not repeated as a claim of fresh verification.

Sources: [SA outline](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM4_sketch_500.tex), [complete account I](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_I.tex), and [YM3 I](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM3/YM3_I.tex), by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. The underlying averaging, gauges and stage construction originate with Tadeusz Bałaban. The three-dimensional passages are proof templates, not four-dimensional discharge.

| Source passage checked | What it supplies or limits |
|---|---|
| SA 5598–5618, 5663–5750, 6559–6598 | Actual erosion/row definitions; raw tower formula and core quantifiers; independent current and pair tie. ER7 is explicitly assumed and is not our CORE proof. |
| SA 5999–6035 | Running versus absolute radii, frame and waiting depth; the exact running table is at 6033. |
| SA 6108–6173 | Two sequences, mark retirement, coefficients, lifts, stored-variable tiers, and the warning that stage inclusions require analytic hypotheses. |
| SA 7597–7618, 17516–17531 | The strip and conditional mean; stored Gaussian factors that cannot disappear from F3's measure identification. |
| SA 8165–8299 | Isolated pivots, coefficient \(L^{-3}I_3\), real gauge adjoint factor, QC18 smallness, and the proved local chart with a small-solution converse. |
| SA 8310–8369 | QC25's full local fibre measure, pivot Haar factors, positive real determinant branches and holomorphic coefficient continuation. This corrects F3. |
| SA 17375–17449 | Stage test ladder and its stated support, one-\(M\)-cube gaps, fates, waiting marks and locality. These motivate our explicit geometry inputs. |
| SA 17575–17630, 17652–17658 | Eligible components, sharper tests, prepared box, overlap exponents, drop-out factors, and the box-minimizer hypothesis. Eligibility is not R0's asserted actual-output realization. |
| SA 19445–19495 | Supremum ceilings and the order with test/radius coefficients and activity amplitudes after \(M\). |
| CA-I 48520–48578, 49495–49546 | Four printed gauge families and the explicit limitation of the operator theorem's domain supply. |
| CA-I 53737–53832, 53858–53892 | Prepared sequence, \(N_0\ge2\), component restriction, collars and box inclusion. An arbitrary extra loop-neighborhood inclusion is not proved there. |
| CA-I 54236–54330, 54986–55000 | Reconstruction instruction and two fluctuation integrals; the later theorem assumes the stage theorem. |
| Y3 46258–46387, 46472–46559 | Local fibre/coarea template with all Haar factors, and the strip lemma. Its identity-on-small-fields clause is for the cutoff case only. |
| Y3 51852–52014 | Conditional-mean bounds are hypotheses, and the contour estimate has additional Gaussian assumptions and an exact test-domain requirement. |
| Y3 53356–53370, 56309–56340, 56434–56448 | Containing-cube witness, pinned composition and subtracted bracket, and real tie scope. |

## Change log (pass 3 fixes, lead, 2026-11-05)

Applied the findings of `gates/st1-gate.md` (Claude fresh session, first failing step none):
1. P82 is recorded as frozen; M1 is the remaining matching item; (15) is asserted only at interior elements (bonds whose plaquettes lie in Omega_0), where ST1 uses it.
2. Lemma 10's C_U: SA 19469-19470 chooses the frame bound after the amplitudes, so C_U does not precede kappa as row 2 implied. It enters only (T1), a ceiling on gamma; after one gamma ceiling the frame constant is absolute, C = 3^{2 r_R}. Row 2 is read with this correction.
3. Lemma 8's ceiling a-bar < delta_B/(4 C_Q L) is imposed inside Lemma 8, chosen before a_T, not via row 4.
4. Lemma 10 lists A1/F0/REG; F6 lists RUN and (15).
5. Corollary 14' states its scope (real-background inputs, complex inputs assumed in the domain); the 'exactly the five hypotheses' wording is corrected.
6. The exponent condition q > p0 + 2r_R is attributed to ST1, with SA's own conditions stated.
7. K_tw raised from 32 to 64 times e^{4 delta_T} K_T (about 52 is needed); margins hold either way.

**Status: REOPENED (2026-11-05)** by a `wrong` signal: [f-meas-draft.md](f-meas-draft.md) Lemma FC6 shows that with the comb representative of line 41 the conditional mean can leave the test ball (|F_p| >= 2(delta'_j + h_j)), and proposes Amendment CV (the mean-contour axial representative, SA 9669-9676) touching lines 41, 128, 276-277, 339, 345, 581, 1064. Until CV is distilled and refereed, the theorem below is frozen except at those uses. Previously: frozen, as a conditional theorem with three named Outstanding items: CI (NL1/LF1; see rows 273 and the TD draft), F-measure and F-contour. Reopens only on a `wrong` signal or when an import it reads changes.

## Result

The distilled ST1 proves Theorem 14 as a conditional implication: hereditary substitution with half-gap room, physical identification on the specified reconstructed real locus, and the finite holomorphic re-expansion (76)–(78). Corollary 14′ gives its finite-history application with its full premises. The proof retains LEV, P81, CRIT and the ambient tower argument; CORE now uses R1. No ER7 or \(b_1^2\le c_\natural b_0\) assumption is needed for CORE.

The permanent ledger repairs deleted-mark coefficient gaps. SA's table \(r_\iota(m)=C_\iota\theta_m^{-1/2}(\log\theta_m)^q\), used here with ST1's own exponent condition \(q>p_0+2r_R\) (SA's own conditions are \(q>p_0+2r\), \(p_0-p_1>Cr\), \(2p_1-Cr>p_0\); ST1's weaker ones suffice for every use here), absorbs all raw overlap growth by a ceiling on \(\gamma\). Thus the smoothed lift is unnecessary: \(\lambda=\Lambda_Q=1\). R1 forms, and even the old scalar comparison core forms. R0 remains a corrected counterexample for the discarded table's analytic test class; its claimed actual-output realization was not established and is not used. Output and internal consumer admission follow from the stated BOX and geometry inputs.

The principal analytic import remains **P82°/M1 and (15)** uniformly on the admitted layered class. Other imports are A1/F0/REG, AV/CURV, PROF/RCG4, OPS/SLICE/UNQ, CH, the actual DR construction and main-step coordinate/source supply. The added hypotheses **GEO-mark, GEO-box, RUN-low, BOX, ST-test and LOC** are explicit in Section 2. **CI remains Outstanding**, owned by NL1/LF1. F3 proves the exact local chart measure and F4 the datum map on its full tube; identification with an already stored stage measure and the exact conditional-mean contour remain **Outstanding F-measure/F-contour** unless supplied. No Gaussian integration bound, infinite sum, volume limit or LF mass statement follows from the finite substitution theorem.

Corrections to the round-3 draft and the accompanying radius proposal:

1. Adopted (Tq0) everywhere, moved \(C_0,C_1\) after \(M\), replaced the old radius floor by uniform coupling ceilings, and recalculated main/stage/output budgets as \(\ell^{p_0-q}\), \(\ell^{p_1+r-q}\), \(\ell^{p_1-q}\). Structural precision constants retain their earlier order.
2. Removed smoothed lifts from all records. Proved formation from the full PROF maximum, including remote raised loops and output sources, rather than treating a profile bound as local. Established scalar formation under the new table as well.
3. Restricted R0 to the analytic test class, put every loop affected by its nontrivial row in the high-exponent region, and separated this counterexample from an actual BOX minimizer. The stronger actual-output assertion is not proved.
4. Kept R1 but distinguished radius sets from full tower carriers. Removed the unsupported diameter-one convention and used the uniform coefficient ratio with an ample fixed \(K^\flat\). Witness bounds have no shrinking coefficient.
5. Made the ledger a permanent union and limited M3's inclusion to identical records/radii. It does not establish whole-domain inclusion in SA. Compatibility also requires retaining the same functions and carriers.
6. Specified the entire GEO-box loop family, its output layers and response carrier; retained BOX-id's current/stored-slot properties and all BOX chart/source ceilings. Paid the fixed carrier enlargement in B2 instead of asserting its unmodified numerical factor universally.
7. Corrected F1: its small-field identity holds only in the cutoff case. In F2 defined the pivot inverse and free-coordinate completion, supplied a separate full-coordinate uniqueness radius, and shrank the free chart into it; small free coordinates alone do not justify the four-dimensional local converse.
8. Replaced F3's determinant formula by the exact QC25 measure: included pivot Haar factors, corrected inverse-Jacobian accounting, used \(\tfrac12\operatorname{tr}a^2\) for holomorphic Haar continuation, and fixed a fibre version without an almost-everywhere-to-everywhere inference. Retained every stored density and test and exposed F-measure.
9. In F4 included the tube factor \(9/4\) in \(C'_A\), distinguished it from the larger source constant \(C_A\), charged complex adjoint/logarithm bounds, enlarged the source to all outward-row carriers, and kept regularity/uniqueness premises separate from source smallness.
10. Restricted F5 to a proved tube-containment statement and exposed the unsupplied actual mean/deformation and localized-cutoff issues. Strengthened LOC-form by its common-chart segment; gave F7 its full read-reach premise. These prevent the draft's unconditional “except CI” corollary.
11. Limited B4 to real formation/drift and bound comparisons; arbitrary complex membership and imported precision remain hypotheses. Restated CI so no constant fixed before \(\kappa\) reads \(b_f\); its amplitude enters (77).
12. Identified the missing real tie in `nl1-L-draft.md` Proposition C, without using that proposition to justify the new table. In the inherited plaquette expansion, restored the missing plus sign between the curl and curvature-adjoint terms.

All mathematical steps are written arguments. Tools were used only for source retrieval, text navigation and editing, and document consistency checks; no computation discharges a proof. This is research text, not an audit, grants no status, and is **not yet refereed**.
