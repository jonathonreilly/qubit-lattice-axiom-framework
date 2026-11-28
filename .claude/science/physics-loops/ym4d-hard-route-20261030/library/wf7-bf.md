# WF7 by the box-first route (row 156)
Provenance: OpenAI Codex, GPT-6 family (exact deployment and runtime effort not exposed; requested effort: max); checkout `3f78ce8739bbe94df51d23794e11cf0c47559e9b`; Sussman–Alpoge commit `31a47c543775`. Research text, not an audit; no status is granted.

## 1. Check of Claude's Section 6

Credit **Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text**, for the SA constructions. SA lines refer to the requested outline, fetched once. Credit Tadeusz Balaban for CMP **109**, (3.18)–(3.25), (3.38), and Claude for the box-first proposal. The named local lemmas retain their authorship and premises.

This checks `gates/wf7-extension-gate.md` Section 6 in its order. Its last paragraph explicitly leaves the route unproved.

1. **Construction.** The composition is defined on the admitted WF3–WF6 domains. Keep Definition D's response inside the actual nonlinear average. The box map returns its own current. It does not return Current-I's independently assigned current.
2. **Physical identity.** Lemma CR applies when the whole old tower lies memberwise in both endpoint sequences. Include its boundary rows and the average's fixed read collars. A constant top layer of level at least \(j\) suffices. Containment at every level through \(j\) is the condition actually used. Equality of currents concerns complete interior stencils, not the outer boundary of \(R_z\).
3. **Grouped terms.** With that same admitted WF4 map, grouping the cutoff directions gives WF13a. WF8–WF10 retain their pointed-cancellation, response and room premises. Grouping does not prove those premises for another box problem.
4. **Non-grouped terms.** The single-map estimate is valid from T4, AV, MS and PW, with the stated distance buffer. The reference to (4.5) with \(\beta=0\) needs correction: that substitution gives zero. The needed expression is \(DF_R(v)v'\), estimated below. AX still controls the prescribed node derivative. No comparison of two different node assignments is needed.
5. **No removed background; sum of directions.** Both statements are algebraically correct for this composition. The derivative at \(\nu=0\) is linear in the cutoff. Its complementary cutoff is \(1-\zeta_{\rm grouped}\).
6. **Heredity.** The box map has a fixed finite read set. Definition D supplies field locality after parameters outside the active domain vanish. This is not locality in \(R_z\) at arbitrary ambient parameters. The local evaluation on \(Y\supset B_z\) must retain the same response specification and all read collars.
7. **Admissibility and the seam warning.** Agreement at complete physical pairs suffices for choosing an off-physical extension. It does not supply the missing endpoint identity at a lower-layer seam. The warning is correct. A change to a meet map would also change the WF4 input to WF8.
8. **Response choice.** Keep Definition D. A separate response on the box would require a new comparison and would undo this reduction.

Checked line by line by Codex. The conditional construction survives with the clarifications above. Its unrestricted layered endpoint identity remains the first unresolved step. The following sections separate the valid implication from that obstruction.

## 2. Exact identity on contained boxes

Let \(T=(T_q(R_z))_{q\le j}\) be WF4's fixed old tower. Let \(S^0,S^1\) be the endpoint sequences. Assume
\[
 T_q(R_z)\subset\Omega_q^0\cap\Omega_q^1
 \quad(0\le q\le j).                                      \tag{C}
\]
The datum means the full determining datum, including the boundary rows; it is not only the top averages. Require \(X\) and its current stencil inside \(T_j(R_z)\). Use the prescribed representatives and actual currents. Retain the common complex room of WF3–WF6 and the named BG, AX, AV inputs.

Write \(F_T\) for this box pair map and \(m_T\) for its actual nonlinear datum map. With Definition D's fixed response \(H=H_k(s;P,B')\), set
\[
 V_t=e^{i\eta_k tH}U_+(P),\qquad
 \Phi_\zeta(s,t,\nu)
 =\widetilde G_{j,z}\!\left(X,
 F_T\!\left(m_T(e^{i\eta_k(t+\nu\zeta)H}U_+(P))\right)\right).
                                                               \tag{1}
\]
This makes explicit the determining rows implicit in WF3–WF4. The finite read collars belong to \(R_z\).

At complete physical pairs and \(s=1\), \(V_0,V_1\) are the prescribed regular critical endpoints. Lemma CR and (C) give \(F_T(m_TV_i)=P_i\) up to the assigned gauge on \(X\), including its current stencil. Gauge invariance removes that gauge from the member value. At each bond, \(H_b\) commutes with its scalar multiple. Therefore
\[
 \sum_\zeta\partial_\nu\Phi_\zeta(1,t,0)
 =\frac{d}{dt}\widetilde G_{j,z}(X,F_T(m_TV_t)).
\]
Integrating gives exactly
\[
 \widetilde G_{j,z}(X,P_1)-\widetilde G_{j,z}(X,P_0)
 =\sum_\zeta\int_0^1\partial_\nu\Phi_\zeta(1,t,0)\,dt.       \tag{2}
\]
No intermediate \(V_t\) is asserted critical. A cutoff zero on the entire datum read set gives zero. This is Balaban's restriction mechanism, rebuilt from Lemma CR rather than imported from (3.38).

Condition (C) permits a nonconstant top layer. For example, if
\(R_z\subset\Omega_j^0\cap\Omega_j^1\), nesting gives
\(T_q(R_z)\subset R_z\subset\Omega_j^i\subset\Omega_q^i\).
Layers above \(j\) may vary anywhere in the box. The pure tower and each old meet then have identical members, rows and node conventions. BG identifies their maps. This proves the aligned layered case of joint-loc (7.2).

## 3. Bounds for the contained-box construction

Put \(\sigma=\xi_j/\xi_k\). Retain **T4, AX, AV, MS, PW** with the common chart and radius qualifications of wf7-extension Sections 3–4. In particular, T4 holds throughout the datum paths on the full fine-parameter and multiplier discs. These are named inputs, not conclusions of the endpoint identity.

**Small members, complementary directions.** Let \(v(\nu)=m_T(e^{i\eta_k(t+\nu\zeta)H}U_+)\), with \(\zeta=1-\zeta_{\rm grouped}\). AV and PW give, for each raw row \(c\) of scale \(\xi_c\le\xi_j\),
\[
 |v'_c|\le C_R\delta_k\,\xi_c/\xi_k\le C_R\delta_k\sigma.
                                                               \tag{3}
\]
Group all direction windows whose supports meet a fixed \(bM\xi_k\)-neighbourhood of the near region. Bounded overlap gives a fixed number; choose \(R_z\) to include their read collars, as WF13a allows. The complementary cutoff vanishes in that neighbourhood. The derivative is zero if its averaging carrier misses its support. Since every tower scale is at most \(\xi_j\), its old distance from \(X\) is
\[
 D\ge bM/\sigma-C_*,\qquad
 C_* = b_*+(\rho+L\mathfrak M)/(L-1).
\]
The second term bounds the first-rule erosion and fixed read losses. Choose \(M\) after these constants, so \(D\ge bM/(2\sigma)\).

Choose \(2\gamma\) below T4's response rate, with \(\gamma\) above the MS counting rate. Then
\[
 \|DF_T(v)e_c\|_x\le K e^{-2\gamma d_T(x,c)},\qquad
 \sup_x\sum_c e^{-\gamma d_T(x,c)}=S_\gamma<\infty .
\]
Indeed, MS bounds shell \(n\) by \(C(n+2)^q e^{b_{\rm count}n}\), with \(b_{\rm count}<\gamma\); its weighted sum converges. Thus (3) gives
\[
 \|\partial_\nu F_T(v(\nu))\|_{j,X}
 \le C_RKS_\gamma\delta_k\sigma e^{-\gamma D}.
\]
Integration along the complex segment from \(0\) to \(\nu\) proves
\[
 \|F_T(v(\nu))-F_T(v(0))\|_{j,X}
 \le C_R|\nu|\delta_k\sigma e^{-cM/\sigma}.             \tag{4}
\]
This is the small-member WF7 bound for the complementary box directions.

The norm includes the actual current and assigned representative. For an ordered node product \(g=\prod_qg_q\), differentiate one factor at a time. AX bounds the sum of its contour-length ratios by \(C_L\sum_{r\ge0}L^{-r}\). T4 bounds each differentiated factor with the same distance weight, up to a fixed pillar loss. Finally
\(\partial_\nu(gJg^{-1})=gJ'g^{-1}+[g'g^{-1},gJg^{-1}]\).
The existing current bound controls the commutator. This gives the node and current part of (4).

**Grouped directions.** Their sum uses exactly the same \(F_T\) for every near \(X\). Subtracting the vacuum and the member's own tent action gives WF13a. Retain the pointed Hessian cancellation and the affine/Hölder response bounds used in WF8. The affine field has size \(A=C\alpha_k\sigma^2\); its errors have sizes \(E_H=C\alpha_k\sigma^{2+\alpha_H}\) and \(E_N=C\alpha_k^2\sigma^4/r_{B,j}\). In the Taylor-size regime these errors are at most \(CA\), since \(\alpha_j/r_{B,j}\le C\). Thus their squares are controlled by their cross terms with \(A\). The uncancelled quadratic and cubic terms are bounded by
\[
 Cg_j\{A(E_H+E_N)/\alpha_j^2+A^3/\alpha_j^3\}
 \le Cg_j(\rho_j^2\sigma^{4+\alpha_H}+\rho_j^3\sigma^6).
\]
The fixed diameter polynomials are summed with the allocated input rate. Retain WF8's whole-core treatment when the local Taylor-size parameter exceeds one, and at its finitely many young ages. The \(C_M\sigma^{-4}\) base count gives WF9. For a vacuum-only member, the uncancelled quadratic bound gives WF10 instead. Cauchy's formula on \(|\nu|<c_\nu/s_k\) supplies exactly one \(Cs_k\) factor.

**Long members.** Keep their original outer presentation and its admitted member-core displacement bound. If \(X\) leaves the fixed near region, its tree length in old \(M\)-cubes is at least \(b_1/\sigma\). Split its rate as in SA 16265–16276:
\[
 e^{-\kappa d_j(X)}
 \le e^{-\kappa_{\rm sum}d_j(X)}
     e^{-b_1\kappa_{\rm far}/\sigma}
     e^{-\kappa_{\rm ret}d_j(X)}.                       \tag{5}
\]
The first share sums the domain count and diameter polynomials; the last share remains for output spatial decay. The middle share equals \(e^{-cM/\sigma}\) with \(c=b_1\kappa_{\rm far}/M\). This is an activity bound, not exponential decay of the pair on a large \(X\).

## 4. Heredity and the named consumers

Fix the assigned ambient sequence. Set all fine parameters outside \(Y\supset B_z\) to zero. In Definition D, every surviving walk has its full read hull in \(Y\). The specified response's local nonlinear equations and unique small solution therefore read only the pair on \(Y\). This uses the first-system locality and uniqueness input; it does not compare independently rebuilt operators on different sequences. The datum and \(F_T\) then read only the fixed \(R_z\subset Y\). Composition preserves this exact equality. A wall component missing \(B_z\) contributes nothing.

For a lower tower contained in \(T\), Lemma CR applied to the generated critical box field gives its own-average restriction. AX supplies the assigned node transport. The identity continues from real to complex critical data, then composes with \(v(s,t,\nu)\). The lower-tower room remains the named inner-domain input. No criticality of the original independent-current pair is used.

For a finite fine-cube set \(\Lambda\), put \(B=B_z\). Repeated one-variable fundamental theorems give
\[
 f[K\mid B]=\sum_{A\subset K}(-1)^{|K\setminus A|}f(1_{B\cup A}).
\]
On summing over \(K\subset\Lambda\setminus B\), the coefficient of each corner is
\(\sum_{A\subset K\subset\Lambda\setminus B}(-1)^{|K\setminus A|}\).
Pair subsets differing by a fixed cube outside \(A\): they cancel unless \(A=\Lambda\setminus B\). The surviving coefficient is one. Thus (2) is recovered at complete physical pairs. Joint holomorphy and the uniform bounds of Section 3 give the bracket factor
\((e^{\bar\kappa}-1)^{-|Y\setminus B_z|}\) by mixed Cauchy estimates. Each parameter is differentiated once, so no factorial appears. The \(\nu\) derivative and the \(t\) integral commute with these finite operations.

**WF11–WF12.** Cauchy's inequality in the member core applies to (4), with cost \(Cg_j/\alpha_j\). The \(C_M\sigma^{-4}\) base count gives exactly
\[
 Cs_kg_j\rho_j\sigma^{-3}e^{-cM/\sigma}.                 \tag{6}
\]
Use \(d_j\) for a vacuum-only origin. Equation (5) gives the same tail estimate for long domains, with the retained spatial share. For any fixed \(m\), choose an integer \(n>m\); \(e^{cM/(2\sigma)}\ge(cM/(2\sigma))^n/n!\) bounds \(\sigma^{-m}e^{-cM/\sigma}\). Taking \(m=3+\alpha_H\) or \(3\), and using \(\rho_j\ge1\), proves both WF12 inequalities. No second \(s_k\) factor is taken.

**OA7.** Replace \(\delta_k\) in (3) by the physical perturbation size \(u\). Sum the T4 kernel without the distance restriction and divide by the allowed radius. This gives \(C_R\sigma_j\alpha_j^{-1}u\) for the box pair. With the complementary support it retains (4)'s exponential. The other defining datum, chart and tower norms still require the full WF5/inner-room input; a pair estimate alone does not prove them. The heredity above is exactly OA7's active-domain restriction for this fixed specification.

These readers therefore accept the contained-box result with its named domain inputs. They do not remove condition (C).

## 5. Stop at a lower-layer seam

For an unrestricted layered box the actual restriction problem is
\[
 S_R^i(q)=\Omega_q^i\cap T_q(R_z).
\]
Lemma CR identifies the physical endpoint with this meet problem. It does not identify it with \(T\) when the two problems differ. SA 16137–16176 fixes an enlarged box and a common near sum. It supplies no containment assertion for every preceding layered structure. LQ quantifies over boxes already contained in \(\Omega_p\); it does not establish that the prescribed full \(R_z\), with its read collars, is such a box. A lower-layer box of size \(M\xi_p\) also supplies distance \(M\xi_p/\xi_j\), not \(M/\sigma_j\) unless \(p=k\).

The Cartan example in joint-loc Section 7 shows why equality of the two maps cannot be assumed. Take \(j=1\), a slab \(\Omega_1\), and an old block \(Q\subset T_1(R_z)\setminus\Omega_1\), away from both collars. A \(3^4\)-site patch inside \(Q\) has \(4\cdot2\cdot3^3=216\) edges and \(81\) vertices. Its divergence-free edge space has dimension \(216-81+1=136\). At most eight old averaging rows read the patch. Rank-nullity gives a nonzero real \(a\) there with
\[
 d^*a=0,\qquad K_Ta=0.
\]
For \(V_\epsilon(b)=\exp(i\epsilon a_b\operatorname{diag}(1,-1))\), the pure tower's datum derivative vanishes. Its actual current derivative is therefore zero. The meet fixes the patch bonds as level-zero rows, so its current derivative is \(d^*da\) there, up to the positive Wilson normalization. This derivative is nonzero: otherwise the energy identity gives \(da=0\); together with \(d^*a=0\), the lattice Laplacian identity makes \(a\) constant. Its compact support forces \(a=0\), a contradiction. Gauge changes add no current derivative at the vacuum. Small nonzero \(\epsilon\) stays in the admitted finite-lattice charts.

Thus the meet and pure-tower maps differ on unrestricted small input domains. This example does **not** prove that an actual complete physical step produces a forbidden \(R_z\). Nor does it disprove every possible layered window identity.

**First failed inference for the requested full theorem:** applying Lemma CR to WF4's pure tower without (C). To continue, the actual window geometry must supply (C) and the stated room and buffer for every use. Otherwise a meet-based filing needs its own WF8–WF10 and scale comparison. SA Theorem 6(c)'s exponentially small mismatch is not the exact identity (2). I stop at this step.

## Result

**Proved as an implication:** the box-first physical identity (2), the single-box WF7 bound (4), the long-domain tail (5), and fixed-sequence heredity. The inputs are **(C), BG/Lemma CR, T4, AX, AV, MS, PW**, Definition D with the specified first-system locality, the admitted **WF3–WF6** domains, and the fixed window buffer. The grouped bounds retain the pointed Hessian and affine/Hölder inputs of **WF8–WF10**. Under these premises, **WF11–WF12** and the relevant **OA7** response and restriction clauses read the result as stated. Nonconstant top layers are included when (C) and these analytic premises hold.

**WF7 and rank 4 remain open.** They stop at the prescribed-box identification and admission for every actual layered \(R_z\). The seam example forbids replacing that obligation by automatic meet/pure-tower equality. These implications are proved by Codex, not yet checked by the other model. All arguments are by hand; file retrieval and editing supply no mathematical evidence.
