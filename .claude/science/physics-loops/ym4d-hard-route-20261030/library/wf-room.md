# WF substitution room — queue row 113
Provenance: GPT-6 / Codex (exact backend identifier not exposed), requested effort max (runtime setting not exposed); checkout `dafa3f7fcaee7253785b0d2ca252a4ee4e601bcc`; Sussman–Alpoge commit `31a47c543775f3f74013d06dd5d85962358f3b9e`; research text, not an audit; no scientific status granted.

**Outcome: STOPPED at the session budget.** The full WF substitution-room obligation remains open. The statements proved below are the narrower implications with their named inputs; no actual assigned window substitution leaving its domain was obtained.

## 1. Target and sources

This attacks `sa-ledger.md` rank 4: admission of the actual outer, inner and removed window substitutions, with their assigned currents, to their hereditary pair domains. Success would supply the room premise of the window's Cauchy estimates; a counterexample would require changing the window or its domains before those estimates are available. No numerical calculation is used to discharge a step.

Credit for the outline, its substitutions, domains and proposed proof mechanism: Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text. Source line numbers below refer to `YM4_sketch_500.tex` at the commit above, fetched once into `/tmp/sa_ym4.tex`. Credit for the renormalization-domain construction: Tadeusz Balaban, *Communications in Mathematical Physics* **109**, 249–301, and **119**, 243–285; the local OCR beside those papers is used without copying the papers into this repository. The earlier broad literature records are `lit-balaban.md` and `lit-large-field.md`.

The scope of the existing results matters: `a3-close.md` §2 states Lemma T and Lemma R as implications; `gates/a3-close-meet-gate.md` checks §§1, 3 and 4 of that note, not §2. Lemma R concerns real critical references on single-layer domains. Neither statement is itself admission of a WF3–WF6 or OA7 substitution.

## 2. What the two Balaban papers supply

These are readings of published arguments, **unchecked as imports into this route**. The addresses are printed page and equation numbers. The scan of CMP 119 p. 261 was also inspected because its OCR loses the left sides and some exponents.

1. **CMP 109, pp. 261–263, (1.8)–(1.16).** The second variable replaces the second-derivative expression for the current. The domain has a real/complex splitting, two curvature bounds, first-order bounds on the complex potential, local real gauges, an independent-current bound, and background-of-average conditions on eroded interiors. The paragraph after (1.16) uses the real background regularity theorem to obtain the latter conditions from sufficiently smaller simple radii. This is the ancestor of Lemma T. The window may use this organization, but its every-subdomain hereditary quantifier, its actual contour mean and its unsaturated pair core must replace Balaban's domain and orbit convention. The existing Lemma T is precisely a proposed reconstruction of that extra hereditary assertion; citing p. 263 does not prove it for the window.

2. **CMP 109, p. 272, (3.10)–(3.16).** In an outer substitution the current is expanded as a reference current plus a second-order linear expression and a local remainder. The independent reference current replaces only its designated occurrence. Balaban requires smallness of the potential, its first differences and the displayed projected/second-order quantities in (3.14), and spends fractions of a separate radius in the Cauchy disc. The window changes this to a multiplier-defined reduced current on independently decoupled operators. First-order control of the field alone is not the published hypothesis. The integration-by-parts argument for the new current must be proved for that assignment.

3. **CMP 109, pp. 275–280, (3.24)–(3.53), Lemma 4.** An inner term is evaluated on a box background at the actual nonlinear average. Both the gauge field and the current are transported when putting the datum in a local axial/Landau form. Equations (3.37)–(3.47) first handle the radial path in the unperturbed datum; they extract the factor \((L^{j-1}\eta)^2\), using \((1+7\beta)L^{-2}\le1\). Equations (3.48)–(3.52) then allow an additional datum ball. In particular the restriction \(2B_3\alpha_3\le\beta L^{-2}\alpha_0\) is separate from the potential restriction \(B_3\alpha_3<\alpha_1/2\). Lemma 4 admits the generated background **and its own current** on these domains. The window can follow this proof after replacing the average and backgrounds by the actual ones, replacing its restriction identity by (9.3), tracking the node transformations, and choosing the additional datum radius below both running adjacent radii. A mere estimate \(|B|\le CM\alpha\sigma_j\), fed into the crude bound (9.2), loses the curvature contraction that this proof needs.

4. **CMP 119, pp. 259–261, (2.28), (2.34)–(2.39), and p. 276.** The running radii are \(\alpha_{i,n}=C_i g_n(\log g_n^{-2})^{q_i}\). The layered bounds contain the coefficient
   \[
   c_{j,n}=1-\beta(1-2^{-(j-n)}).
   \]
   For example the curvature allowance is \(c_{j,n}\alpha_{0,n}\xi^2(L^n\xi)^{-2}\), the independent-current allowance is \(c_{j,n}\alpha_{0,n}(L^n\xi)^{-3}\), and the complex potential/gradient allowances in local units are \(c_{j,n}\alpha_{1,n}\). The real local-gauge bound (2.38) does not carry this coefficient. The backgrounds in (2.35), (2.37) use the localized determining set together with the earlier determining rows, not an unqualified single-layer tower through a seam. On p. 276 the cover is adapted to each layer and the earlier estimates are used with \(\eta\) replaced by \(L^{-n}\). For WF this requires the actual layerwise meets and the every-preceding-structure clauses of SA R22, not only the single-layer Lemma R. The shrinking difference of adjacent coefficients must be retained in the displacement estimate. The elementary comparison with exponential decay is proved below; the paper's transfer statement does not by itself supply the window's independently decoupled maps.

The usable mechanism is therefore: retain the correct current assignment, contract the complete inner reference field using its extra scale, allow a separately small datum perturbation, and compare each layered displacement with its own margin. The published analyticity of an effective action is an input **after** these inclusions, not a proof of them.

## 3. A uniform outer-domain lemma, including all towers

Here is a smaller statement with a complete proof. It is a domain lemma, not yet a bound for the assigned WF response. Its one background input is **Lemma T of `a3-close.md` §2**, at its stated standing: an ungated implication from A1 (8.2), (9.2), the averaging bootstrap and the other inputs listed there. In particular, it supplies existence and holomorphy, not just a formal estimate for already existing tower fields.

Use the norms and the forward derivative of SA R4. For a matrix-valued bond form put
\[
 \|h\|_{1,U}=\max\{\|h\|_\infty,\|\nabla_Uh\|_\infty\}.
\]
All norms below are in level-\(j\) units, with \(\eta=\eta_j\le1\). Fix \(C_0<\infty\). There exist \(a_*>0,c_*>0\), depending on \(C_0\), the fixed matrix norm and Lemma T's constants only, with the following property. Let
\[
 0<a_0\le a_1,\qquad a_1^2\le C_0a_0,\qquad a_0+a_1<a_*.
\]
Suppose the triple \(P=(U,A',\mathbf J)\) satisfies **every** clause of the core at radii \((a_0/2,a_1/2,a_0/2)\), including the real gauge clauses. For fixed complex bond forms \(h,q\), set
\[
 \mathbf U(z)=e^{i\eta zh}e^{i\eta A'}U,
 \quad A'(z)=(zh)\boxplus A',
 \quad \mathbf J(z)=\mathbf J+zq.
 \tag{3.1}
\]
Then
\[
 |z|\bigl(\|h\|_{1,\mathbf U}+\|q\|_\infty\bigr)<c_*a_0
 \quad\Longrightarrow\quad
 (U,A'(z),\mathbf J(z))\in\mathcal U_j^\circ(X;a_0,a_1,a_0).
 \tag{3.2}
\]
The same \(c_*\) works for every \(j,X\), tower depth and volume. The current in (3.1) is the assigned independent shift; no replacement by \(J(\mathbf U(z))\) occurs.

**Proof of the simple estimates.** Write \(b=\|h\|_{1,\mathbf U}\). Since \(\mathbf U_\nu=e^{i\eta A'_\nu}U_\nu\), the series for the exponential and its inverse gives
\[
 \|\nabla_Uh-\nabla_{\mathbf U}h\|_\infty
       \le C\|A'\|_\infty\|h\|_\infty.
 \tag{3.3}
\]
Indeed the difference is \(\eta^{-1}(1-\operatorname{Ad}e^{i\eta A'_\nu})\operatorname{Ad}(U_\nu)h_\mu(x+\eta e_\nu)\); \(U_\nu\) is unitary and \(\|1-\operatorname{Ad}e^{i\eta A'}\|\le C\eta\|A'\|\) on the fixed small ball. Thus \(\|h\|_{1,U}\le Cb\), uniformly in \(\eta\).

On a fixed ball \(|p|+|v|<r_*\), the convergent exponential and logarithm series define
\[
 F_\eta(p,v)=(i\eta)^{-1}\log(e^{i\eta p}e^{i\eta v}),
 \qquad G_\eta(p,v)=F_\eta(p,v)-v.
\]
They give \(|G_\eta|\le C|p|\), \(|D_pG_\eta|\le C\), and \(|D_vG_\eta|\le C\eta|p|\). To see the last estimate, \(G_\eta(0,v)=0\), and the terms of total degree at least two in \(F_\eta-p-v\) all contain both \(p\) and \(v\), with a factor \(\eta\). Termwise differentiation is uniformly absolutely convergent on a smaller fixed ball. The maps commute with conjugation by a unitary matrix. Apply the integral formula for a difference to the endpoint pairs \((zh_\mu,A'_\mu)\), parallel transported by \(U_\nu\). Dividing by \(\eta\) therefore yields
\[
 \|A'(z)-A'\|_{1,U}\le C|z|b
 \quad\text{if }|z|b+a_1<r_*/C.
 \tag{3.4}
\]
This argument controls the logarithm and its derivative; there is no bare-mesh factor left over.

For completeness, the needed curvature difference satisfies
\[
 \eta^{-2}|\partial\mathbf U(z)-\partial\mathbf U|
       \le C|z|b(1+a_0+a_1+|z|b).
 \tag{3.5}
\]
Move the four background links of a plaquette to the right in its ordered product. The term linear in \(zh\) is \(i\eta\) times the sum of the four transported oriented values. Three transports are along the corresponding partial plaquette path; replacing the last path by the inverse fourth link changes the sum by at most \(C|z|b|\partial\mathbf U-1|\). The remaining sum is \(\eta\) times the covariant curl. Its norm is bounded by \(C\eta|z|b\), using (3.3); transports over at most four links have bounded norm. Every term of degree at least two in the four exponentials is bounded, by their absolutely convergent product series, by \(C\eta^2|z|^2b^2\). Finally \(|\partial\mathbf U-1|\le a_0\eta^2/2\). These three estimates prove (3.5), including reversed links by their exact inverse convention.

Choose a fixed \(d>0\) sufficiently small. On the disc
\[
             |z|<R=d a_0/b\qquad(b>0),
 \tag{3.6}
\]
(3.4)–(3.5) put the **field** simple conditions within radii \((2a_0,2a_1)\). The real factor and all its gauges are unchanged. Choose \(a_*\) so these enlarged radii satisfy Lemma T's smallness threshold. Its tower construction does not read the independent current, so no bound on \(\mathbf J(z)\) is needed to apply it on this auxiliary disc.

**All hereditary clauses on one disc.** Fix any \(Z\subset X\), its level \(p\le j\), either erosion rule, and depth \(n\le p\). For one plaquette or one current component on the prescribed eroded interior, let \(f(z)\) denote respectively
\[
 \frac{\partial U_n(Z;P(z))-1}{L^{-(j-p)}\eta_p^2},
 \qquad
 \frac{J(U_n(Z;P(z)))}{L^{-(j-p)}L^{2(n-p)}}.
 \tag{3.7}
\]
Lemma T, including its change-of-units argument, gives holomorphy on (3.6) and
\[
 \|f(z)\|\le A a_0,\qquad A=K^\sharp(2+4C_0).
 \tag{3.8}
\]
At \(z=0\), membership in the half core gives \(\|f(0)\|<a_0/2\). The scalar Schwarz lemma applied to each norm-one linear functional of the matrix \(f(z)-f(0)\) gives
\[
 \|f(z)-f(0)\|\le(A+1/2)a_0|z|/R.
 \tag{3.9}
\]
Thus \(|z|b<d a_0/[4(A+1/2)]\) makes every tower quantity less than \(3a_0/4\). The proof fixed an arbitrary clause and used the same constants, so it proves the universal quantifier without a sum over towers. The real-factor towers do not change. Equations (3.4)–(3.5), after decreasing \(c_*\), put the simple curvature and potential clauses below their full radii. Also \(|\mathbf J+zq|<a_0/2+|z|\|q\|<3a_0/4\). These choices prove (3.2). If \(b=0\), the field and every tower are unchanged and only the last current inequality is needed. \(\square\)

This proof also admits a nonconstant holomorphic curve of shifts on a disc, vanishing at zero, if its first-order supremum on a larger concentric disc has the same bound: use that disc in (3.8)–(3.9). It does not require a bound on any second difference of \(h\). In particular it explains exactly which part of the outer-domain argument can be supplied by Lemma T, and which part still belongs to the response/current construction.

## 4. What the scale and layer arithmetic actually proves

**Running radii.** Suppose \(a_{i,q}=C_i x_q^{-1/2}(\log x_q)^{q_i}\), \(x_q\ge X\ge\max\{D,e^{2\max_i q_i}\}\), and \(x_j-x_{j'}\le D(j'-j)\) for \(j\le j'\). These are explicit hypotheses on the flow; the present note does not prove that the RG generates it. Then
\[
 \frac{a_{i,j'}}{a_{i,j}}\le\sqrt{1+j'-j}.
 \tag{4.1}
\]
If \(x_j\ge x_{j'}\), the logarithm ratio is at most one and the square-root ratio is at most \(\sqrt{1+D(j'-j)/X}\). If \(x_j<x_{j'}\), the function \(x^{-1/2}(\log x)^{q_i}\) is nonincreasing for \(\log x\ge2q_i\), as its derivative is \(x^{-3/2}(\log x)^{q_i-1}(q_i-\tfrac12\log x)\); the ratio is then at most one. This proves (4.1).

For integers \(m\ge1\), \(m+1\le2^m\): it holds at one, and \(m+2\le2(m+1)\) proves the induction. Consequently, for \(L\ge4\),
\[
 L^{-m}\frac{a_{i,j+m}}{a_{i,j}}
 \le(\sqrt2/L)^m<\tfrac12.
 \tag{4.2}
\]
For \(a=k-j\ge0\), the same argument gives
\[
 L^{-a}\max\{1,\alpha_k/\alpha_j\}\le1
 \tag{4.3}
\]
when \(\alpha\) is the minimum of the usable radii of this form. To verify the assertion about a minimum, choose an index attaining that minimum at level \(j\), and bound the minimum at \(k\) by that index's value there. Fixed changes in the conventions merely multiply (4.2)–(4.3) by their stated comparison constants.

**Restriction in units, on a single-layer domain.** Restrict a triple of level \(j+m\) to a region of level \(j\) and replace \((A',\mathbf J)\) by \((L^{-m}A',L^{-3m}\mathbf J)\). Potentials, first differences and current scale by \(L^{-m},L^{-2m},L^{-3m}\), respectively; the link matrices do not change. The curvature allowance scales by \(L^{-2m}\). Each tower read by the lower core was already read by the upper core. Its old bound is exactly
\[
 a_{0,j+m}L^{-(j+m-p)}\eta_p^2
  =(L^{-m}a_{0,j+m})L^{-(j-p)}\eta_p^2,
 \tag{4.4}
\]
and the current bound has the identical coefficient comparison. The tower is the same determining problem in changed units: its real datum and the product defining its logarithmic increment have not changed. A local gauge on a smaller box is obtained by restricting the upper-level gauge; its bounds scale as the potential and derivative do. Hence this restriction lies in the core with radii \(L^{-m}a_{i,j+m}\). Equations (4.2) and (4.4) give the **half-core premise of Section 3** for a regular input from level \(k+1\) at every old level \(j\le k\). No tower estimate has been summed over ages.

**Conditional consequence for the outer WF maps.** Suppose the actual assigned response, including its prescribed current, satisfies on all \(|s_\Delta|<e^{\bar\kappa}\)
\[
 \|h_{t,\nu}\|_{1,\mathbf U_+}
       +\|q_{t,\nu}\|_\infty
       \le C_R(1+|\nu|)\delta_k,
 \qquad 0\le t\le1,
 \tag{4.5}
\]
in level-\(k\) units. Here \(h_{t,\nu}\) is the *complete shift* \((t+\nu\zeta_\square)\mathbf H_k\), not a linearized average, and \(q_{t,\nu}\) is the complete assigned current increment. After conversion to level \(j\), the left side is at most \(C_R(1+|\nu|)\sigma_j\delta_k\): the current actually gains \(\sigma_j^3\). For \(s_k=\delta_k/\alpha_k<c_\nu\) and \(|\nu|<c_\nu/s_k\), this is at most \(2C_Rc_\nu\sigma_j\alpha_k\le2C_Rc_\nu\alpha_j\). Choose \(2C_Rc_\nu<c_*\). Section 3 then admits the complete outer triple at every old level on the common disc. This is a proved implication from (4.5), Lemma T and the stated input core/flow conditions. In particular the age supremum is not the unresolved analytic input.

**Shrinking layered gaps.** For Balaban's ordinary coefficient \(c_{t,m}=1-\beta(1-2^{-(t-m)})\),
\[
              c_{t,m}-c_{t+1,m}=\beta2^{-(t+1-m)}.
 \tag{4.6}
\]
Write \(n=t+1-m\ge1\). If a displacement in a clause is bounded, in units of its layer radius, by \(C|\nu|s_k\sqrt{1+n}\,e^{-D(n-1)}\), its ratio to this gap is at most
\[
 \frac C\beta |\nu|s_k\,2^n\sqrt{1+n}\,e^{-D(n-1)}
       \le\frac{2\sqrt2 C}\beta |\nu|s_k
       \quad(D\ge\log4).
 \tag{4.7}
\]
Indeed \(e^{-D(n-1)}\le4^{-(n-1)}\) and \(\sqrt{1+n}\le2^{n/2}\), so the middle factor is at most \(4\,2^{-n/2}\le2\sqrt2\). This proves the comparison uniformly in the number of layers. Where the actual nested geometry gives a gap of one later-level \(M\)-cube, any path from the source to an element beyond \(n-1\) intervening layers crosses \(n-1\) disjoint intervening shells. In each shell its length in the local metric is at least \(cML\). Adding those lengths gives \(d\ge cML(n-1)\), and a response with decay \(e^{-\theta d}\) supplies \(D=c\theta ML\). Taking \(M\ge(\log4)/(c\theta L)\) proves (4.7). This reasoning requires the asserted gap in the actual sequence; it is not a consequence of an arbitrary separated sequence with an unrelated gap \(\rho\).

Thus a **proved weighted response for each actual clause** would spend the layered margins uniformly. Equation (4.7) does not establish that response. In particular Section 3, applied with a global first-order supremum, cannot replace it: using the smallest of the gaps in (4.6) would make its disc shrink to zero as the number of layers increases.

## 5. The reduced-current calculation that is actually sufficient

The current question can be reduced to a precise multiplier calculation without taking a second difference of a decoupled field. This section proves that calculation; it does not silently identify an unprescribed multiplier with the window's multiplier.

Use the fine pairing \(\eta^4\sum_b\) and the **counting** pairing on the dimensionless determining rows, as in `a3-derivative.md` §3 and Lemma M of `a3-close.md`. Let \(K_A\) be the derivative of the actual straightened average in its exponential chart. Put
\[
 \|A\|_{X,w}=\sup_b w_b\max\{\xi_b|A_b|,\xi_b^2|\nabla A_b|\},
 \quad\|f\|_{F,w}=\sup_b w_b\xi_b^3|f_b|,
 \quad\|\lambda\|_{Y,w}=\sup_c w_c|\lambda_c|.
\]
The row input is (9)–(11) of `a3-derivative.md`, used also at complex references in `a3-clauses.md` and its gate:
\[
 \|K_A^{\mathsf T}\lambda\|_{F,w}\le C_K\|\lambda\|_{Y,w},\qquad
 \|(K_A-K_0)^{\mathsf T}\lambda\|_{F,w}
       \le C_K\|A\|_{X,w}\|\lambda\|_Y.
 \tag{5.1}
\]
Its density factor is essential: a row of length \(\xi_c\) has entries bounded by \(C\eta^4\xi_c^{-3}\); the fine transpose contributes \(\eta^{-4}\), and bounded carrier overlap leaves \(C\xi_b^{-3}\). This is the standing row estimate, not a volume count or a cell-weighted multiplier bound.

There is also a local chart conversion. Define, on each bond,
\[
 E_Ah=\int_0^1\operatorname{Ad}(e^{it\eta A})h\,dt,
 \qquad R_A=(E_A^{\mathsf T})^{-1}.
 \tag{5.2}
\]
Differentiating the exponential by its absolutely convergent power series gives
\[
 \left.\frac d{d\epsilon}e^{i\eta(A+\epsilon h)}
                    e^{-i\eta A}\right|_{\epsilon=0}=i\eta E_Ah.
\]
Hence the chart gradient and the left current are related by
\(F'(A)=E_A^{\mathsf T}J(e^{i\eta A}\mathbf U)\). In particular it is \(R_AK_A^{\mathsf T}\lambda\), not merely the chart gradient, that reconstructs that current at a critical physical pair.

For \(\|A\|_X\le r\), we have \(\eta|A_b|\le r\), because \(\xi_b\ge\eta\). The exponential series in (5.2) gives \(\|E_A-1\|\le Cr\). Choose \(Cr<1/2\); the geometric series for the inverse gives \(\|R_A\|\le2\) and
\[
 |R_A(b)-1|\le C\eta|A_b|.
 \tag{5.3}
\]

For **any specified** holomorphic field/multiplier pair \((A,\lambda)\), with \(A(0)=0\), \(\lambda(0)=\lambda_0\), define the anchored reconstructed increment
\[
 q_{\rm rec}(A,\lambda)
     =R_AK_A^{\mathsf T}\lambda-K_0^{\mathsf T}\lambda_0.
 \tag{5.4}
\]
Then (5.1)–(5.3) prove
\[
 \|q_{\rm rec}\|_{F,w}
 \le C\left(\|\lambda-\lambda_0\|_{Y,w}
             +\|\lambda_0\|_Y\|A\|_{X,w}\right).
 \tag{5.5}
\]
To verify every term, write (5.4) as
\[
 R_AK_A^{\mathsf T}(\lambda-\lambda_0)
 +R_A(K_A-K_0)^{\mathsf T}\lambda_0
 +(R_A-1)K_0^{\mathsf T}\lambda_0.
\]
The first two terms use (5.1) and \(\|R_A\|\le2\). For the third, its weighted value at \(b\) is at most
\(Cw_b\eta|A_b|\,\|\lambda_0\|_Y\le C\|A\|_{X,w}\|\lambda_0\|_Y\), again because \(\eta\le\xi_b\). This proves (5.5) with no second derivative of \(A\). Differentiating the same three factors, or their convergent local series, gives the corresponding first-response estimate
\[
 \|Dq_{\rm rec}\|_{F,w}
 \le C\bigl(\|D\lambda\|_{Y,w}+\|\lambda\|_Y\|DA\|_{X,w}\bigr)
 \tag{5.6}
\]
when the background and \(\lambda_0\) are held fixed. Their derivatives must be included if a removed comparison moves them.

At physical critical parameters, if \(\mathbf J=K_0^{\mathsf T}\lambda_0\) and the output multiplier is the actual constrained multiplier, \(\mathbf J+q_{\rm rec}=J(e^{i\eta A}\mathbf U)\) by (5.2). Away from that locus, (5.4) is one explicit holomorphic continuation preserving the independent baseline \(\mathbf J\). That last sentence is a construction, not uniqueness: values on the physical current graph do not fix an independent-current continuation.

This attack identifies the exact missing identification rather than importing the wrong solution. SA R9 requires the response to vanish at \(B'=0\), and SA 10360–10445 distinguishes its first system from the second system used on global/strip domains. The force-only system (A) of `a3-clauses.md` cannot simply be inserted: at \(\mathbf U=1,B'=0\) its derivative with respect to an independent current is \(-T\mathbf J\), nonzero off \(\operatorname{ran}K_0^{\mathsf T}\), whereas R9's response is identically zero there. The gate of that note further retains the \(J\)-dependent correction for the literal second system. Thus its gated Theorem \(\Sigma\) is not already (4.5). To apply (5.5) to WF, the actual first-system multiplier, its anchored readout, and its node transport have to be matched to (5.4) or to another explicit formula with the same proved bounds.

## 6. The real layered tower estimate

The most direct seam attack is to put a very fine tower under a much coarser ambient layer: the crude complex regularity bound then loses the square of their scale ratio. The following real estimate survives that attack. It proves a smaller part of the layered problem, not the required complex Lipschitz estimate.

**Inputs and standing.** Use A1 (8.2) for real regular data; the local plaquette-of-averages estimates of `a1-balaban.md` §§3.5, 7.6; and the real profile bound (30) of `a3-profile.md`, with the extra column estimate required by its gate. That column estimate is the zero-field instance of (5.1). These are the existing real, conditional library inputs, with their flat/A1 dependencies retained. Work on their admitted torus floors and separated sequences, without inward bonds. No independent-current or decoupling theorem is an input to this section.

Let a localized sequence lie member by member inside an ambient one. Write \(l'(x)\le l(x)\) for their local scales, \(d'\) for the localized metric and \(d\) for the ambient metric. Extend each scale as the bare scale outside its positive-level members. Then \(d\le d'\). Set \(\lambda(x)=l'(x)/l(x)\le1\). Both sequences have gap at least \(\rho\) in the unit of the outer member. Choose \(\rho\) sufficiently large for the fixed averaging carriers, and for \(4\log L/\rho\le\delta/2\), where \(\delta\) is the profile rate. The profile rate may first be fixed on the wider class with a smaller gap, so increasing the admitted gap does not redefine it.

For a real field with
\[
       |\partial U(p)-1|\le\epsilon\eta^2l(p)^{-2},
 \tag{6.1}
\]
let \(V'=M_{\mathbf B'}(U)\) be its actual localized datum and let \(U'\) be the regular critical background of that datum. On elements where its current uses only plaquettes inside the first member,
\[
 \eta^{-2}l(x)^2|\partial U'(x)-1|
       +l(x)^2l'(x)|J(U')(x)|\le C_L\epsilon.
 \tag{6.2}
\]
Here \(\epsilon\) is below a fixed ceiling, and \(C_L\) is independent of the two depths, their difference, the shape and the volume.

**Proof.** First establish the scale comparison used in the profile. If two points have layer indices differing by \(N\), any path between them crosses at least \(N-1\) complete intervening shells. In shell \(r\) the gap has length at least \(\rho\xi_r\), and the local unit is \(\xi_r\). Choose successive first crossings of the nested boundaries; these segments are disjoint and ordered along the path. Their weighted lengths add to at least \((N-1)\rho\). Consequently the ratio of either sequence's local scales at two points is at most
\(L\exp((\log L)\operatorname{dist}/\rho)\), in either direction. Corner and fixed-stencil conventions change only the fixed leading power of \(L\). Apply this to both sequences and use \(d\le d'\):
\[
 \frac{\lambda(y)^2}{\lambda(x)^2}
       \le C_L\exp\bigl((4\log L/\rho)d'(x,y)\bigr).
 \tag{6.3}
\]

The carrier of one datum test has diameter \(C_Ll'(y)\) at its anchor \(y\). Since \(l'(y)\le l(y)\) and the gap exceeds its fixed carrier constant, ambient scales on that carrier differ from \(l(y)\) by at most a fixed adjacent-level factor. The local averaging estimate, applied with the maximum of (6.1) on that carrier, therefore gives
\[
                  |\partial V'(\tau)-1|
                         \le C_L\epsilon\lambda(y_\tau)^2.
 \tag{6.4}
\]
This use is local: a test is controlled by the plaquettes in its own averaging carrier. The uniform constant is that of the actual iterated-average bootstrap, not a product of one-step constants over the depth. Since \(\lambda\le1\), the datum is \(C_L\epsilon\)-regular. A1 gives its regular critical orbit when this radius lies below the fixed existence ceiling.

Apply the real profile theorem to that orbit. It bounds each of
\(\eta^{-2}l'(x)^2|\partial U'-1|\) and \(l'(x)^3|J(U')|\) by
\[
 C_L\epsilon\sup_\tau
       e^{-\delta d'(x,\tau)}\lambda(y_\tau)^2.
\]
The test anchor and its support are a bounded distance apart in \(d'\); absorb this constant. Equation (6.3) and the chosen gap make the last display at most
\[
 C_L\epsilon\lambda(x)^2
       \sup_\tau e^{-\delta d'(x,\tau)/2}
       \le C_L\epsilon\lambda(x)^2.
\]
Divide by \(\lambda(x)^2\) to obtain (6.2). This also explains the current normalization \(l^2l'\) in SA Theorem 5(b); replacing it by \(l^3\) is not what has been proved. \(\square\)

The analogous real estimates for real perturbations of the real factor follow by the plaquette expansion used in Lemma T: their curvature radius in (6.1) is \(C(a_0+a_1^2)\) when both original curvature bounds and the first-order complex-potential bounds hold in the ambient units. However, transplanting Lemma T's **complex** proof is a further step. At an element with \(\lambda(x)\ll1\), (9.2) supplies a crude normalized holomorphic bound of order \(\lambda(x)^{-2}\). A ball defined by one global ambient norm need only have a fixed radius: another part of the tower can have \(\lambda=1\). Its Cauchy remainder is then \(C\lambda(x)^{-2}a_1^2\), rather than the required \(Ca_1^2\). In the single-layer proof the larger radius \(c_TL^{p-n}\) cancels this factor exactly. The real profile proof above does not construct the corresponding localized complex continuation or its weighted derivative. This is where this attempt at the layered analogue of Section 3 stops.

## 7. The inner radial interpolation: a proved estimate, with its endpoint retained

One must not discard the two-power gain of the complete inner reference value. The following elementary argument reconstructs the analytic part of CMP 109 (3.43)–(3.52) and makes its required endpoint explicit.

Let \(f(B)\) be one component of a background's normalized curvature or current, over the identity datum, on an interior where the local level-\(j\) scale is one. Suppose it is holomorphic on \(\|B\|_\infty<r_B\), with \(f(0)=0\) and \(\|f(B)\|\le C\|B\|_\infty\). For the canonical background these are precisely the relevant parts of A1 (9.2). They must be transported with the prescribed gauge if a different representative is used. For \(\|B\|\le r_B/4\), \(\|B'\|\le r_B/4\) and \(0\le t\le1\),
\[
 \|f(tB+B')\|
       \le\|f(B)\|+4C\|B\|^2/r_B+3C\|B'\|.
 \tag{7.1}
\]
To prove it, expand \(f(zB)\) on the disc \(|z|<r_B/\|B\|\). On circles approaching that radius its supremum is at most \(Cr_B\). The sum of its terms of degree at least two, evaluated at any \(t\in[0,1]\), is at most \(2Ct^2\|B\|^2/r_B\). Thus comparison of \(f(tB)\) with \(tf(B)\) costs at most \(4C\|B\|^2/r_B\). At any point of the segment from \(tB\) to \(tB+B'\), the norm is at most \(r_B/2\). A circle of radius \(r_B/4\) in a norm-one direction remains in the \(3r_B/4\)-ball, so its Cauchy derivative bound is \(3C\). Integrating in direction \(B'\) proves (7.1).

In particular, if the **actual endpoint**, in the same representative, satisfies
\[
 \|B\|\le C_BMa\tau,\qquad
 \|f(B)\|\le(1+\beta)a\tau^2,
 \qquad \tau=L^{-(k+1-j)},
 \tag{7.2}
\]
then
\[
 \|f(tB+B')\|
 \le\left(1+\beta+4CC_B^2M^2a/r_B\right)a\tau^2
                                      +3C\|B'\|.
 \tag{7.3}
\]
Choose the field ceiling so \(4CC_B^2M^2a/r_B\le\beta\), and the additional datum radius so \(3C\|B'\|\) is below the allotted fraction of the old curvature/current radius. This retains \(\tau^2\), uniformly in age. The endpoint in (7.2) is supplied in Balaban's proof by the admitted tower of the complete input and its restriction identity, before the radial interpolation. For the WF maps it has to refer to the actual nonlinear average, the actual box tower and its assigned gauge. Neither \(\|B\|\le C_BMa\tau\) alone nor the fact that the increment is small proves that endpoint. Equation (7.1) closes the radial-interpolation subproblem; it does not certify an endpoint or a layered tower that has not been identified.

## 8. An explicit rapid-oscillation test and why it does not refute WF

This tests the strongest tempting replacement of the assigned current. It is the staggered-field mechanism noted at SA 10531, written out here; credit for that observation belongs to the outline's authors named in Section 1.

Take an admissible periodic box with an even number of bare sites in direction 1, \(\eta=L^{-j}\), and \(T=\operatorname{diag}(1,-1)\). For a small fixed \(\epsilon>0\), put
\[
 A_2(x)=\epsilon\eta(-1)^{x_1/\eta}T,\qquad
 A_\mu=0\ (\mu\ne2),\qquad U_\mu=e^{i\eta A_\mu}.
 \tag{8.1}
\]
The only nontrivial plaquettes are
\[
 U_{12}(x)=e^{-2i\epsilon\eta^2(-1)^{x_1/\eta}T}.
\]
Thus \(|\partial U-1|\le2\epsilon\eta^2\), \(|A|\le\epsilon\eta\), and \(|\nabla A|\le2\epsilon\). Use the real factor \(U\), complex potential \(A'=0\), and independent current \(\mathbf J=0\). Choose \(\epsilon\) so \(2\epsilon<a_0/4\), \(2\epsilon<C_{\rm pot}Ma_0/4\), and \(2K^\sharp\epsilon<a_0/4\), as well as Lemma T's fixed smallness ceiling. The displayed real gauge works on every local cube. Lemma T's real-field conclusion admits every tower with strict room. Hence this is a legitimate core input for all \(j\), under that same lemma.

In the normalization \(\sum_p(1-\tfrac12\operatorname{tr}U_p)\), with colour pairing \(\tfrac12\operatorname{tr}\) and fine volume \(\eta^4\), its full Wilson current is
\[
 J_2(U)(x)=2\eta^{-3}\sin(2\epsilon\eta^2)
                         (-1)^{x_1/\eta}T.
 \tag{8.2}
\]
Indeed the two incident \(12\)-plaquettes have opposite angles and opposite derivatives with respect to the link potential, so their action derivatives add to \(2\eta\sin(2\epsilon\eta^2)(-1)^{x_1/\eta}\). Divide by \(\eta^4\). For \(0\le u\le1\), \(\sin u\ge u/2\): integrate \(\cos v\ge1-v^2/2\ge1/2\). Thus \(|J_2(U)|\ge2\epsilon/\eta\) when \(2\epsilon\eta^2\le1\). It exceeds \(a_0\) for sufficiently large \(j\). A different fixed Wilson normalization only multiplies this lower bound by its fixed positive constant.

The map \((U,0,0)\mapsto(U,0,J(U))\) therefore leaves the core on this explicit family. **That map is not the assigned outer WF substitution.** R8 keeps an independent current, R9 vanishes at zero fluctuation, and the inner pair carries the current of its generated critical background, not (8.2). Accordingly this test refutes the current-replacement shortcut, not row 113. It gives no license to report the actual WF obligation REFUTED.

## 9. Exact stopping point

The completed implications are: the outer half-core-to-core lemma including every tower (Section 3); its single-layer age-uniform application under the explicit response bound (4.5); the comparison of shrinking layer margins with exponential decay (4.7); the multiplier-to-current readout (5.5)–(5.6); the real layered tower estimate (6.2); and the inner radial-interpolation estimate (7.1). The explicit configuration in Section 8 kills only the wrong current replacement. None of these is a claim of closure of ledger rank 4.

The unfinished attack is the **localized complex layered tower estimate** at the end of Section 6: one must cancel the factor \((l/l')^2\) while retaining decay from the integrated field, on the actual tower/meet assignments and every preceding structure. The actual first-system and removed-map multiplier/current readouts have not been matched to Section 5 on the independent fine-parameter discs, and the prescribed inner endpoint/gauge has not been checked against (7.2). These are the remaining map identifications and estimates; they cannot be supplied by assuming WF5, OA7, the full current of an arbitrary field, or Theorem \(\Sigma\)'s different off-shell system. No source file, ledger or gate is changed by this stopping report.
