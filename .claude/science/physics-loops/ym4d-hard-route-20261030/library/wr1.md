# WR1 — Wightman reconstruction per component

Provenance: Codex, Phase A, pass 2 (distil), at `a456311fd37ebcc1811c1180cff145d7d2b91570`. Research text, not an audit; grants no status. Distilled from `wightman.md`, `pd-port.md`, `cluster-port.md` and their checks, identified below. Every deduction is by hand. This part is not yet refereed as a whole.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, for the direct reconstruction ported here. K. Osterwalder and R. Schrader, *Axioms for Euclidean Green's Functions II*, §IV.1, supply the historical method. Their continuation theorem is not an input to this proof.

## Definitions and imports

Euclidean coordinates are \(y=(\mathbf y,t)\in\mathbb R^3\times\mathbb R\); \(\theta(\mathbf y,t)=(\mathbf y,-t)\), and \(\tau_af(y)=f(y-a)\). A separated tuple \(F=(f_1,\ldots,f_n)\) has \(C_c^1\) entries with pairwise disjoint supports. The empty tuple is \(1\). A polynomial is a finite complex linear combination of tuples, with multilinearity imposed. Concatenation is used only when its entries remain separated. Different summands may overlap. A positive-time tuple has all supports strictly in \(t>0\). Reflection and conjugation act on each slot.

Put \(\Delta_n=\bigcup_{i<j}\{y_i=y_j\}\). The space \(\mathcal S_{\Delta,n}\subset\mathcal S(\mathbb R^{4n})\) consists of functions whose every derivative vanishes on \(\Delta_n\). Its subspace \(\mathcal S_{+,n}\) is also flat wherever some \(t_i\le0\). Both degree-zero spaces are \(\mathbb C\). For Euclidean or Minkowski variables, use the Euclidean norm in
\[
 p_r(F)=\max_{|\alpha|\le r}\sup_y(1+|y|^2)^{r/2}|\partial^\alpha F(y)|.
 \tag{1}
\]

Fix one component \(\sigma=\sigma_\xi\). All the following imports concern this same hierarchy and its same reflection Hilbert space.

**H1 — SR1(4), growth and density.** \(S_0=1\), and the separated moments have their unique continuous extensions to \(\mathcal S_{\Delta,n}\), with
\[
 |S_n(F)|\le C_E^n(n!)^{\kappa_E}p_{k_E n}(F),\qquad
 k_E=20,\quad \kappa_E=k+32.                         \tag{2}
\]
Here \(k\ge1\) is the fixed graded-moment exponent; \(C_E\) is independent of \(n\). Finite sums of separated smooth compact tensors are dense in \(\mathcal S_{\Delta,n}\), including its positive-time version. These are the imports recorded in `growth-qf3.md` (1), used in `wightman.md` §1.

**H2 — RO1 for this component, and SR1(4)/CL1 positivity.** The hierarchy is real, symmetric, and invariant under \(\mathbb R^4\rtimes O(4)\), on separated and diagonal-flat tests. For every finite sequence \(F_n\in\mathcal S_{+,n}\),
\[
 \sum_{n,m}S_{n+m}(\Theta\overline{F_n}\otimes F_m)\ge0,
 \qquad (\Theta\overline F)(y)=\overline{F(\theta y)}. \tag{3}
\]
Every mixed tensor belongs to the specified diagonal-flat space. On compact tuples this gives the same matrix positivity for arbitrary polynomial coefficients.

**H3 — CL1, Hilbert space and cone.** Quotient positive-time polynomials by the null space of

\(\langle[F],[G]\rangle=\sigma(\theta\overline F\cdot G)\), antilinear in its first slot, and complete. The resulting \(\mathcal H\) is separable; the compact tuple classes are dense. It agrees with the completion from (3). Write \(\Omega=[1]\), \(\|\Omega\|=1\). Time and spatial translations are strongly continuous, strongly commuting operators
\[
 T_s=e^{-sH},\quad H\ge0,\quad T_s[F]=[\tau_{se_4}F],\qquad
 U(\mathbf a)[F]=[\tau_{(\mathbf a,0)}F].
\]
The joint spectral measure \(\Pi(dE,d\mathbf q)\) represents \(T_s=\int e^{-sE}\,d\Pi\) and \(U(\mathbf a)=\int e^{i\mathbf a\cdot\mathbf q}\,d\Pi\). It is carried by \(E\ge|q_j|\), \(j=1,2,3\), as in CL1(4). The vacuum is fixed by these translations.

**H4 — RO1(2), the full insertion density.** Use [pd-port.md](pd-port.md) (7), with its \(p=0\) input, for arbitrary outside polynomials. For \(0<\eta\le1\), outside entries strictly above \(\eta/4\), and \(h\in C_c^1(\{|t|<\eta/64\})\),
\[
 |\sigma(\theta\overline F\cdot(h)\cdot G)|
 \le C_{\rm PD}\eta^{-5}\|h\|_1
 \|[\tau_{-\eta e_4/4}F]\|\,
 \|[\tau_{-\eta e_4/4}G]\|.                       \tag{4}
\]
The constant is independent of the numbers of outside entries and their coefficients. Local \(C^1\) continuity is part of this import. A bound only for each fixed outside degree is insufficient. If (4) was proved for the self-centered component, Lemma 1 restores its mean. This is the full four-variable bound (7), not only the bound with a fixed transverse label. Its provenance is [o4-check-1.md](../gates/o4-check-1.md) §§2–3. SA PD13 has exponent \(p+5\); SA L28569–28571 chooses \(p=4\). The exponent five here uses the stronger checked local input, not that weaker choice.

**H5 — PH1 and the bounds of [cluster-port.md](cluster-port.md) §§8–9.** On fixed separated support containers, moments are bounded and locally \(C^1\)-continuous. In its notation,
\[
 |\sigma(F)|\le M_n(\delta;R)\prod_i\|f_i\|_\sharp,\quad
 |\sigma(F)-\sigma(F')|
 \le M_n(\delta;R)\sum_i\|f_i-f'_i\|_\sharp
       \prod_{j\ne i}\max(\|f_j\|_\sharp,\|f'_j\|_\sharp),       \tag{5}
\]
where \(\|f\|_\sharp=\max(\|f\|_\infty,c_M\|\nabla f\|_\infty)\), \(c_M>0\). The constants are position-independent, including for separated reflected tuples. For fixed tuples and all sufficiently large real \(v\),
\[
 |\sigma(F\cdot\tau_vG)-\sigma(F)\sigma(G)|
       \le C(F,G)|v|^{-2}.                              \tag{6}
\]
Finite sums inherit these statements. The constants and thresholds are uniform over the component family when that family is used. In the PH1 realization the common centering states satisfy \(\nu_j\in\mathcal G_{a_j,\beta_j}\), as required by [cluster-check.md](../gates/cluster-check.md) A3. Each component is realized by periodic-state limits with that common centering; its own mean \(\sigma(f)=c_\xi\int f\) need not vanish. PH1(5)'s unique vacuum is also recovered from (6) in Lemma 8.

The RO1 input is componentwise. Its producer must carry the insertion estimates and the required TU10 bound uniformly in the approximating states. Covariance of the averaged limit does not supply H2. This retains [o4-check-2.md](../gates/o4-check-2.md) §4's correction.

## Order of choice

All upstream choices retain [in1.md](in1.md), “Constant order”, rows 1–10, including Amendment 1. In that order: reserve, margins and power-count exponents; geometric constants and odd \(L\); local gauge, inverse, walk and tower data; early matrix/Gaussian constants, then \(\kappa,\Theta,\lambda\); \(\bar\kappa,\kappa_1\), response/profile data, then \(M\); post-\(M\) charts and radii; list, boundary, certificate, entropy and volume constants; remaining source, floor, flow and tube constants; \(X_0\), then \(\gamma=X_0^{-1/2}\) and the returned flow constants; finally \(g\), admissible grid/torus and \(\beta\). In particular \(L>L_0^\natural\) precedes \(\kappa\ge\kappa_0^\natural(L)\). No choice below changes those constants or supplies an upstream missing input.

After those choices and the common component hierarchy, fix the imported \(k,C_E,c_M,M_n,C(F,G),C_{\rm PD}\) and its mean \(c_\xi\). Set the slab constant \(c_{\rm sl}=1/64\), insertion exponent \(\wp=5\), and \(C_{\rm ins}=\max(1,C_{\rm PD}+|c_\xi|)\). Then fix the regularization integer \(l=6>\wp\), and the integrable weight power \(3\). These symbols do not rename IN1's flow coefficient \(c_0\). The constants \(C_{\rm flat}\) and the boundary bounds below are returned estimates. For a kernel configuration, choose its positive margin \(\eta\) last; a smaller margin and then a mollifier radius follow it. For locality, choose the compact tests, then \(\delta,M,A,h_*,\eta_0\), in Lemma 10's order, and finally \(0<\eta\le\eta_0\).

## Reconstruction

**Lemma 1 (round cone and the reconstruction insertion bound).** H2–H4 give a joint spectrum in \(E\ge|\mathbf q|\). They give
\[
 |\sigma(\theta\overline F\cdot(h)\cdot G)|
 \le C_{\rm ins}\eta^{-5}\|h\|_1
       \|[\tau_{-\eta e_4}F]\|\,\|[\tau_{-\eta e_4}G]\|,       \tag{7}
\]
when \(F,G\) lie above \(\eta\) and \(h\) lies in \(|t|<c_{\rm sl}\eta\). Put
\[
 d(z)=\Re z_4-|\Im\mathbf z|,\quad
 T(z)=\int e^{-z_4E+i\mathbf z\cdot\mathbf q}\,d\Pi,
 \quad z^*=(-\overline{\mathbf z},\bar z_4).             \tag{8}
\]
On \(d\ge0\), \(T\) consists of strongly continuous contractions, with \(T(z)^*=T(z^*)\) and the additive semigroup law. It is norm holomorphic on \(d>0\), and its range there lies in \(\mathcal D_\infty=\bigcap_{j\ge1}\operatorname{Dom}H^j\).

*Proof.* Spatial rotations act isometrically on tuple classes by H2 and preserve their dense span. They commute with \(H\) and rotate the spatial spectral variables. Conjugate the coordinate cone by rotations giving a countable dense set of directions. Off the union of their spectral null sets, \(E\ge|\mathbf n\cdot\mathbf q|\) for every such direction. Continuity in \(\mathbf n\) gives \(E\ge|\mathbf q|\).

In (4), \( [\tau_{-\eta e_4/4}F]=T_{3\eta/4}[\tau_{-\eta e_4}F]\). Contraction gives (7). If (4) holds only after self-centering, expand each slot as its centered slot plus \(c_\xi\int f\). This triangular map has inverse obtained with \(-c_\xi\). It commutes with reflection, conjugation and translations, is multiplicative on admitted products, and identifies the two reflection forms. The inserted scalar contributes \(c_\xi\int h\) times the identity form. Cauchy–Schwarz, contraction and \(\eta^{-5}\ge1\) bound that term as in (7) with constant \(|c_\xi|\).

The multiplier in (8) has modulus at most \(e^{-d(z)E}\). Dominated convergence gives strong continuity. Interior derivatives are bounded using \(E^m e^{-dE}\le m!d^{-m}\); the exponential series converges uniformly on smaller neighborhoods. This proves norm holomorphy and all graph-domain assertions. The adjoint and semigroup laws follow by multiplying spectral functions. \(\square\)

*Origin:* `wightman.md` §2; `pd-port.md` (7); `o4-check-2.md` §4 and `o4-check-1.md` §3. Y3 L79749–79824 and L80079–80124.

**Lemma 2 (bounded point insertions).** There are bounded operators \(B(s,s')\), \(s,s'>0\), with, for \(a,b\ge0\),
\[
 \begin{gathered}
 T_aB(s,s')T_b=B(s+a,s'+b),\qquad B(s,s')^*=B(s',s),\\
 \|B(s,s')\|\le C_{\rm ins}\min(s,s',1)^{-5}.            \tag{9}
 \end{gathered}
\]
They are norm continuous. For \(0<\eta\le1\), the bounded insertion \(I_\eta(h)\) has density
\[
 \begin{aligned}
 I_\eta(h)[F]&=[(\tau_{\eta e_4}h)\cdot\tau_{2\eta e_4}F],
 &\|I_\eta(h)\|&\le C_{\rm ins}\eta^{-5}\|h\|_1,\\
 I_\eta(h)&=\int h(y)b_\eta(y)\,dy,
 &b_\eta(y)&=U(\mathbf y)B(\eta+t,\eta-t)U(-\mathbf y),
                                                               \tag{10}
 \end{aligned}
\]
on \(h\in L^1(\{|t|<c_{\rm sl}\eta\})\), with the class formula for compact \(C^1\) tests and positive-time polynomials \(F\). The density is norm continuous, has analytic scalar matrix elements, and obeys \(\|b_\eta(y)\|\le C_{\rm ins}\eta^{-5}\).

*Proof.* Translate both outside polynomials by \(\eta e_4\) in (7). The bounded form kills null vectors, so Riesz representation gives \(I_\eta\). A common time translation in its matrix element proves the class formula. The inserted support is below the remaining shifted tuple. The bound extends to \(L^1\); scalar matrix elements have \(L^\infty\) densities.

For \(0<\eta'<\eta\), \(h\) in the smaller slab and real \(|w_4|<c_{\rm sl}(\eta-\eta')\), translation gives
\[
 I_\eta(\tau_wh)=T((\eta-\eta')e_4+w)I_{\eta'}(h)
                        T((\eta-\eta')e_4-w).           \tag{11}
\]
Insert nonnegative unit-integral mollifiers at zero, of radius tending to zero inside the smaller slab. The right-hand scalar matrix elements are bounded and holomorphic on

\( |\Re w_4|+|\Im\mathbf w|<\eta-\eta'.\)

Cauchy bounds and diagonal selection on compact subsets give locally uniform subsequential limits. On the smaller real slab these are mollifications of the original density and converge to it in local \(L^1\). Thus each limit represents that density. Letting \(\eta'\downarrow0\) exhausts the slab; continuous representatives agree on overlaps. Sesquilinearity and the original norm bound, initially almost everywhere, hold everywhere by continuity. Riesz representation defines \(b_\eta(y)\).

Equality of continuous densities in (11) gives the same translation identity for \(b\). Hence

\(B(s,s')=T_{s-\eta}b_\eta(0)T_{s'-\eta}\), \(0<\eta\le\min(s,s',1)\),

is independent of \(\eta\). It has the shift law, and the largest allowed \(\eta\) gives (9). The density identity with real translations gives (10). Reflection and reality give \(I_\eta(h)^*=I_\eta(\theta\bar h)\), hence the adjoint relation. Factoring through a strictly smaller margin gives norm continuity by Lemma 1. The continuous density in (10) also proves uniqueness of this construction. \(\square\)

*Origin:* `wightman.md` §2, (3)–(5); `o4-check-2.md` §4. Y3 L79826–80005, Lemma IV-75-22 and Proposition IV-75-27.

**Lemma 3 (point form and a common field domain).** There is a complex-linear map \(f\mapsto\phi(f)\), \(f\in\mathcal S(\mathbb R^{1+3})\), from \(\mathcal D_\infty\) into itself. It is Hermitian and translation covariant. With \(l=6\),
\[
 \|(1+H)^j\phi(f)\chi\|
 \le c_{6+j}(f)\|(1+H)^{12+j}\chi\|,\qquad j\ge0,       \tag{12}
\]
where \(c_N(f)=\|A_6\|\sum_{r=0}^N\binom Nr\|\partial_t^rf\|_1\) and \(A_6\) is defined below. All matrix elements are tempered.

*Proof.* For real \(l>5\) and \(R=(1+H)^{-1}\), set
\[
 A_l=\Gamma(l)^{-2}\int_0^\infty\!\int_0^\infty
       (ss')^{l-1}e^{-s-s'}B(s,s')\,ds\,ds'.             \tag{13}
\]
The bound \(\min(s,s',1)^{-5}\le1+s^{-5}+s'^{-5}\) gives norm convergence and

\(\|A_l\|\le C_{\rm ins}[1+2\Gamma(l-5)/\Gamma(l)]\).

Interchanging the variables proves self-adjointness. For \(a>0\), spectral calculus gives \(R^a=\Gamma(a)^{-1}\int_0^\infty t^{a-1}e^{-t}T_t\,dt\), where \(\Gamma(a)=\int_0^\infty t^{a-1}e^{-t}dt\). Insert this integral on both sides of \(A_l\) and use (9). The substitution \(v=s+t\), with

\(\int_0^v t^{a-1}(v-t)^{l-1}dt=v^{a+l-1}\Gamma(a)\Gamma(l)/\Gamma(a+l)\),

gives \(R^aA_lR^a=A_{l+a}\). Moving external semigroups inside (13) gives \(T_sA_lT_{s'}=R^lB(s,s')R^l\). Absolute convergence justifies both interchanges. Therefore
\[
 q_0(\psi,\chi)=\langle(1+H)^l\psi,A_l(1+H)^l\chi\rangle,
 \quad q_0(T_s\psi,T_{s'}\chi)=\langle\psi,B(s,s')\chi\rangle       \tag{14}
\]
is a Hermitian form, independent of any larger admissible exponent on the common domain.

For Minkowski coordinates \(x=(t,\mathbf x)\), put \(\iota x=(\mathbf x,-it)\) and \(V(x)=T(\iota x)\). This is a strongly continuous unitary translation representation. Define

\(q_f(\psi,\chi)=\int f(x)q_0(V(-x)\psi,V(-x)\chi)\,dx\).

The integrand without \(f\) is continuous and bounded by the two \(l\)-th graph norms. Differentiation on \(\mathcal D_\infty\), then integration by parts, gives

\(q_f(H\psi,\chi)-q_f(\psi,H\chi)=i q_{\partial_tf}(\psi,\chi)\).

There is no boundary term. Iteration gives
\[
 q_f((1+H)^N\zeta,\chi)
   =\sum_{r=0}^N\binom Nr i^r q_{\partial_t^rf}(\zeta,(1+H)^{N-r}\chi).
\]
Take \(\zeta=R^l\psi\), \(N=l+j\), with integer \(l=6\). The form bound yields

\( |q_f((1+H)^j\psi,\chi)|\le c_{l+j}(f)\|\psi\|\|(1+H)^{2l+j}\chi\|.\)

At \(j=0\), Riesz gives \(\phi(f)\chi\). To establish its \(j\)-th domain membership, test with \(\psi=(1+H)^j1_{H\le N_0}\phi(f)\chi\), then let \(N_0\uparrow\infty\). This proves (12). The form gives \(\langle\psi,\phi(f)\chi\rangle=\langle\phi(\bar f)\psi,\chi\rangle\) and \(V(a)\phi(f)V(-a)=\phi(f(\cdot-a))\). The spectral cutoffs \(1_{H\le N_0}\) have range in \(\mathcal D_\infty\) and converge strongly to the identity, so this domain is dense. The displayed adjoint relation therefore also makes each smeared field closable.

In four dimensions,
\[
 J:=\int(1+|x|^2)^{-3}dx
   =2\pi^2\int_0^\infty r^3(1+r^2)^{-3}dr=\pi^2/2,
 \quad \|\partial^\alpha F\|_1\le J^n p_{|\alpha|+6n}(F).       \tag{15}
\]
The radial substitution \(u=r^2\) gives the integral. For the second bound use

\((1+\sum_i|x_i|^2)^{-3n}\le\prod_i(1+|x_i|^2)^{-3}\).

Thus (12) proves temperedness. It also proves continuity of field products in every graph norm under Schwartz convergence of their tests. Contractive joint spectral multipliers converging strongly can be interleaved: telescope the products from the vacuum outward and commute each multiplier with the graph powers. \(\square\)

*Origin:* `wightman.md` §3, (6)–(11); `o4-check-2.md` §4. Y3 L80006–80079 and L80472–80668, Lemma IV-75-41, Proposition IV-76-25 and Lemmas IV-76-35/38. The weight power three and \(l=6\) are the four-dimensional choices.

**Lemma 4 (analytic kernels and Euclidean recovery).** Put \(B_\eta=B(\eta,\eta)\). For \(d(\zeta_j)>0\), define
\[
 \begin{aligned}
 W_n(\zeta)&=\langle\Omega,B_\eta T(\zeta_1-2\eta e_4)B_\eta
                 \cdots T(\zeta_{n-1}-2\eta e_4)B_\eta\Omega\rangle,\\
 \Psi_n(z)&=T(z_1-\eta e_4)B_\eta
       \prod_{j=1}^{n-1}[T(z_{j+1}-z_j-2\eta e_4)B_\eta]\Omega.    \tag{16}
 \end{aligned}
\]
Choose \(0<\eta\le1\), \(2\eta\le\min_jd(\zeta_j)\); the vector formula also requires \(\eta\le d(z_1)\) and the same bounds on consecutive differences. Products run from left to right. Set \(W_0=1\) and \(W_1=\langle\Omega,B_1\Omega\rangle\). These definitions are independent of the margin, holomorphic (in norm for \(\Psi_n\)), and bounded by \((C_{\rm ins}\eta^{-5})^n\).

There is a symmetric holomorphic kernel \(\mathscr S_n\) on the union of the tubes
\[
 d_u(z_{\pi(j+1)}-z_{\pi(j)})>0,\qquad
 d_u(z)=u\cdot\Re z-|\Im(z-(u\cdot z)u)|,\quad u\in S^3,        \tag{17}
\]
over all permutations \(\pi\). Its real restriction \(s_n\) is real, Euclidean invariant, and recovers every separated tuple by integration. If \(n\ge2\) and \(\rho=\min_{i<j}|y_i-y_j|\), then
\[
 |s_n(y)|\le C_{\rm ins}^n(4n^2)^{5n}\min(1,\rho)^{-5n}.       \tag{18}
\]

*Proof.* Substitute \(B_\eta=T_{\eta-\eta'}B_{\eta'}T_{\eta-\eta'}\) in (16). Neighboring semigroups combine and endpoint semigroups fix \(\Omega\). This proves independence of the margin. Locally choosing a strictly smaller fixed margin proves holomorphy. Contraction proves the bound.

Suppose \(h_j\) lies in \(|t-t_j|<c_{\rm sl}\eta\), with \(t_{j+1}-t_j\ge2\eta\). Set \(g_j=\tau_{-t_je_4}h_j\) and \(a_j=t_{j+1}-t_j-2\eta\). The class formula (10), starting at the right, gives
\[
 I_\eta(g_1)T_{a_1}\cdots I_\eta(g_n)\Omega
       =[\tau_{(\eta-t_1)e_4}(h_1,\ldots,h_n)].          \tag{19}
\]
In the induction step the intervening shift is \(a_j+\eta-t_{j+1}=-t_j-\eta\), and insertion adds \(2\eta\). Taking the vacuum component gives \(\sigma(h_1,\ldots,h_n)\). If \(t_1\ge\eta\), applying \(T_{t_1-\eta}\) gives the original class.

In each factor of (19), use

\(b_\eta(u)=T(u+\eta e_4/2)B_{\eta/2}T(-u+\eta e_4/2)\).

This follows from (9)–(10). All margins are positive on the slab. Boundedness and the \(L^1\) tests justify Fubini. In the \(j\)-th integral change the slab variable \(u_j\) to \(y_j=u_j+t_je_4\), so \(g_j(u_j)=h_j(y_j)\). Consecutive factors then combine into \(T(y_{j+1}-y_j-\eta e_4)\). Thus the scalar integral has kernel \(W_n\), and the class integral has kernel \(\Psi_n\), both with margin \(\eta/2\).

Rotate an ordering direction \(u\) to \(e_4\) and permute the entries. H2 gives the ordered integral with the correspondingly rotated \(W_n\). On a real overlap, products of approximate identities in small balls identify the continuous kernels. Each complex overlap is convex and contains the real part of each point. It therefore has an open real subset. The identity theorem, applied successively in the variables and then on the connected overlap, identifies the kernels there. This constructs one function \(\mathscr S_n\).

For a fixed unit vector \(v\in\mathbb R^4\), the projection of uniform \(u\in S^3\) onto \(v\) has density \((2/\pi)\sqrt{1-s^2}\). The area element is proportional to \(\sin^2\theta\,d\theta\); \(s=\cos\theta\) and \(\int_{-1}^1\sqrt{1-s^2}\,ds=\pi/2\) give this normalization. Hence \(\Pr(|u\cdot v|<a)\le2a\). With \(a=(2n^2)^{-1}\), the union of the \(\binom n2\) forbidden bands has measure less than one. Some direction gives every projection gap at least \(\rho/(2n^2)\). Use \(\eta=\min(1,\rho/(4n^2))\) in (16) to prove (18).

For compact separated supports, partition each test into finitely many sufficiently small balls. The preceding direction argument orders each product of pieces with a positive common margin. Apply (19) and sum. This gives the integral formula for every separated \(C_c^1\) tuple. Its uniqueness under product tests transfers reality and all real Euclidean symmetries to \(s_n\). For \(n=1\), the insertion formula gives \(s_1=c_\xi=W_1\). \(\square\)

*Origin:* `wightman.md` §4, (12)–(14); `o4-check-2.md` §4. Y3 L80126–80400, Proposition IV-75-61, kernels IV-75-66/68 and Proposition IV-75-78. The separating-direction calculation uses \(S^3\), not \(S^2\).

**Lemma 5 (the supplied diagonal-flat extension is recovered).** For every \(F\in\mathcal S_{\Delta,n}\),
\[
 S_n(F)=\int s_n(y)F(y)\,dy,\qquad
 \int|s_nF|\le C_{\rm flat}^n(n!)^{10}p_{11n}(F),        \tag{20}
\]
with one finite \(C_{\rm flat}\), independent of \(n\).

*Proof.* For \(n\ge2\) and \(\rho\le1\), move a closest pair to its midpoint, giving a diagonal point \(y^*\). The displacement has Euclidean norm at most one and coordinate \(\ell^1\) norm at most \(2\rho\). Taylor flatness to order \(5n\) gives
\[
 |F(y)|\le e^2\rho^{5n}3^{11n/2}p_{11n}(F)(1+|y|^2)^{-11n/2}.  \tag{21}
\]
Indeed the remainder coefficient is \((2\rho)^{5n}/(5n)!\), with \(2^{5n}/(5n)!\le e^2\). On the Taylor segment \(1+|y|^2\le3(1+|y'|^2)\), which gives the weight factor. When \(\rho>1\), use the unmodified seminorm bound. Multiplication by (18) cancels the near-diagonal singularity. The remaining weight is bounded by \(\prod_i(1+|y_i|^2)^{-3}\). Its integral is \(J^n\). Also \(n^n\le e^nn!\), since \(e^n\ge n^n/n!\). These inequalities yield (20), for example with

\(C_{\rm flat}=e^2\max(1,C_{\rm ins}4^5e^{10}3^{11/2}J)\).

The constant kernel handles \(n=1\); degree zero is immediate. The integral functional is continuous on the flat space and agrees with \(S_n\) on separated smooth tensors by Lemma 4. H1's constrained density identifies the two functionals everywhere. \(\square\)

*Origin:* `wightman.md` §4 after (14); `o4-check-2.md` §4. Y3 L80404–80471, Proposition IV-75-87. H1 remains the imported extension and density assertion; (20) identifies it after the stronger insertion input has been used.

**Lemma 6 (a boundary estimate).** Suppose a holomorphic \(F\) is defined near

\(z_j=\iota x_j+\eta h_je_4\), \(x\in K\), \(0<\eta\le\eta_0\le1\),

where \(K\) is compact, \(h_j\in\mathbb R\), and \(|F(z)|\le b\eta^{-p}\) for an integer \(p\ge0\). For \(g\in C_c^\infty\) supported in \(K\), define \(I_g(\eta)=\int g(x)F(z(x;\eta))dx\), \(D_h=\sum_jh_j\partial_{t_j}\) and \(N=p+1\). Then the limit at zero exists and
\[
 \sup_{0<\eta\le\eta_0}|I_g(\eta)|
       \le b\eta_0^{-p}\sum_{r=0}^N\|D_h^rg\|_1.        \tag{22}
\]

*Proof.* Cauchy–Riemann and integration by parts give \(I_g^{(r)}=I_{(-iD_h)^rg}\). Taylor's formula from \(\eta_0\) to \(\eta\) has remainder
\[
 {(-1)^N\over(N-1)!}\int_\eta^{\eta_0}
              (s-\eta)^{N-1}I_{(-iD_h)^Ng}(s)\,ds.      \tag{23}
\]
Its absolute majorant is \(b\|D_h^Ng\|_1s^{N-1-p}/(N-1)!\), integrable at zero because \(N-1-p=0\). Dominated convergence proves the limit. Each finite Taylor term is bounded by \(b\eta_0^{-p}\|D_h^rg\|_1\). The remainder is at most \(b\eta_0\|D_h^Ng\|_1/(N-1)!\), which is bounded as in (22). Applying (22) to \(-iD_hg\) also bounds \(I_g'\) uniformly. \(\square\)

*Origin:* `wightman.md` §5, (17); `o4-check-2.md` §4. Y3 L80670–80717, Lemma IV-76-23. The integer-power Taylor estimate is the checked note's sharper version.

**Lemma 7 (tempered Wightman distributions).** There are unique \(\mathcal W_n\in\mathcal S'(\mathbb R^{4n})\) such that
\[
 \begin{aligned}
 \mathcal W_n(f_1\otimes\cdots\otimes f_n)
 &=\langle\Omega,\phi(f_1)\cdots\phi(f_n)\Omega\rangle\\
 &=\lim_{\epsilon\downarrow0}\int\prod_jf_j(x_j)
 W_n\bigl((\iota(x_{j+1}-x_j+i\epsilon\alpha_j))_{j<n}\bigr)\,dx,   \tag{24}
 \end{aligned}
\]
for any \(\alpha_j\in V_+=\{(t,\mathbf x):t>|\mathbf x|\}\). They have a positive Hilbert metric.

*Proof.* From the definition of \(q_f\) and (14), for \(w,w'\) in the open tube and \(0<s\le\min(1,d(w),d(w'))\),
\[
 T(w)\phi(f)T(w')=\int f(x)T(w-se_4+\iota x)B_s
                              T(w'-se_4-\iota x)\,dx.    \tag{25}
\]
First verify it in matrix elements: the two positive margins put both vectors in \(\mathcal D_\infty\), and splitting \(T_s\) from each factor permits (14). The remaining multipliers are contractions, so the integral is bounded. Split each intermediate semigroup in half and append \(T_s\Omega=\Omega\) on the right. Iterating (25), with Fubini justified by the point bound and \(L^1\) tests, gives the kernel \(\Psi_n(\sum_{r\le j}w_r+\iota x_j)\) for the regularized product.

Take its vacuum component with \(w_1=e_4\), \(w_{j+1}=\iota(i\epsilon\alpha_j)\). The fixed factor \(T(w_1)\) disappears against \(\Omega\). The factors \(T(w_{j+1})\) have positive margins \(\epsilon(\alpha_j^0-|\boldsymbol\alpha_j|)\) and converge strongly to the identity. Lemma 3's graph continuity proves (24) on Schwartz tensors, with no interchange of an uncontrolled pointwise boundary limit and an integral.

For general compact tests apply Lemma 6 to \(F(z)=W_n(z_2-z_1,\ldots,z_n-z_{n-1})\), with \(h_j=2j\), \(p=5n\), \(b=C_{\rm ins}^n\), \(\eta_0=1\). Consecutive margins equal \(2\eta\). Since \(\sum_jh_j=n(n+1)\), (15) gives, for \(N=5n+1\),
\[
 |\mathcal W_n(F)|\le
 C_{\rm ins}^n(N+1)[n(n+1)]^NJ^n p_{N+6n}(F).             \tag{26}
\]
Cutting off at infinity extends this continuous functional to all Schwartz tests. It agrees with (24) first on compact tensors, then on Schwartz tensors by graph continuity. Finite tensor sums are dense: cut off a test, convolve with a product mollifier, and approximate that compact convolution integral by Riemann sums. Each fixed collection of derivatives converges uniformly on a common compact set. Diagonal choice over derivative orders and removal of the cutoff give Schwartz density. This proves uniqueness. Degree zero is \(1\); degree one is \(W_1\int f\).

For finite sums of tensor polynomial tests, Hermiticity identifies the Wightman quadratic form with the squared norm of the corresponding field polynomial on \(\Omega\). It is nonnegative. Tensor density and continuity extend this positivity to arbitrary finite Schwartz sequences. \(\square\)

*Origin:* `wightman.md` §5, (15)–(18); `o4-check-2.md` §4. Y3 L80584–80786, Lemma IV-76-35 and the tempered-distribution proposition.

**Lemma 8 (cyclicity, spectrum and vacuum).** The polynomial domain
\[
 \mathcal D_0=\operatorname{span}\{\Omega,
              \phi(f_1)\cdots\phi(f_n)\Omega:\ f_j\in\mathcal S(\mathbb R^{1+3})\}
                                                               \tag{27}
\]
is dense, lies in \(\mathcal D_\infty\), and is invariant under the fields and translations. The translation spectrum is in \(\overline V_+\). The vacuum is the unique translation-invariant vector up to scalar multiples.

*Proof.* The domain assertions except density follow from Lemma 3. Suppose \(\psi\perp\mathcal D_0\). Translation covariance makes

\(\langle\psi,V(a_1)\phi(f_1)\cdots V(a_n)\phi(f_n)\Omega\rangle=0\)

for every set of translations. Replace \(V(a_j)\) successively, from left to right, by \(T(w_j)\) with positive margins. For the first replacement no field is moved across \(\psi\). For each later replacement, the first preceding adjoint \(T(w_1)^*\) puts \(\psi\) in \(\mathcal D_\infty\). Moving the remaining preceding factors across is legitimate by Lemma 3 and Hermiticity. The expression is now \(\langle\chi,V(a_j)\chi'\rangle\), the Fourier transform of a finite joint spectral measure. Its vanishing for every \(a_j\) makes that measure zero: convolution with Gaussian approximate identities and Fourier inversion prove this uniqueness. Its integral against the bounded multiplier defining \(T(w_j)\) therefore also vanishes. Induction proves vanishing for all regularized products.

Their vector integral formula from (25), followed by product approximate identities, gives \(\langle\psi,\Psi_n(z)\rangle=0\) for every allowed \(z\). Formula (19) now makes \(\psi\) orthogonal to all time-ordered positive-time classes.

For any other positive-time tuple, partition each entry by nonnegative smooth functions supported in cubes of side \(2h\). Products whose center heights differ by at least \(4h/c_{\rm sl}\) are ordered with margin \(2h/c_{\rm sl}\), for sufficiently small \(h\). Their classes are already annihilated. The sum of the remaining product cutoffs is at most one. Its support lies in the union of strips \(|t_i-t_j|<(4/c_{\rm sl}+2)h\). Integrating one time variable first bounds its integral against \(\prod_i|f_i|\) by \(C_Fh\). All configurations in the original supports and their reflected copies remain distinct. Lemma 4 therefore bounds \(s_{2n}\) on this compact product set by some \(M_F<\infty\). The squared norm of the remainder is at most \(M_F(C_Fh)^2\), and tends to zero. Density of compact tuple classes in H3 gives \(\psi=0\).

With Minkowski product \(p\cdot x=p^0t-\mathbf p\cdot\mathbf x\), \(V(x)=\int e^{ip\cdot x}d\mathsf E(p)\), where \(p=(E,-\mathbf q)\). Lemma 1 gives its forward-cone support. Finally \(T_s\to P_0=1_{H=0}\) strongly. H5, applied to the reflected left tuple, gives

\(\langle[F],P_0[G]\rangle=\overline{\sigma(F)}\sigma(G)\).

Density yields \(P_0=|\Omega\rangle\langle\Omega|\), recovering PH1(5). Every translation-invariant vector has zero energy and hence is a multiple of \(\Omega\). \(\square\)

*Origin:* `wightman.md` §5 after (18); `cluster-port.md` (19) and §9; `o4-check-2.md` §4; `cluster-check.md` A2. Y3 L80788–80865; SA L31410–31439 and L31456–31527.

**Lemma 9 (Poincaré covariance).** There is a strongly continuous unitary representation \(V(a,\Lambda)\) of the proper orthochronous Poincaré group. It fixes \(\Omega\), preserves \(\mathcal D_0\), extends the translations above, and satisfies
\[
 V(a,\Lambda)\phi(f)V(a,\Lambda)^{-1}
       =\phi\bigl(f(\Lambda^{-1}(\,\cdot-a))\bigr)
       \quad\hbox{on }\mathcal D_0.                    \tag{28}
\]

*Proof.* The map \(\iota\) identifies \(\mathbb R^{1+3}+iV_+\) with \(d>0\). Thus \(\widehat\Lambda=\iota\Lambda\iota^{-1}\) preserves this tube. For a boost \(B(s)\) in the first spatial direction use
\[
 r_z(y)=(y_1\cos z+y_4\sin z,y_2,y_3,y_4\cos z-y_1\sin z).
\]
Direct substitution gives \(r_{is}=\widehat{B(s)}\). For real differences \(\zeta_j\) with positive fourth coordinates,

\(d(r_{is}\zeta_j)=(\zeta_j)_4e^{-|s|}>0\).

A connected neighborhood of each compact segment of the imaginary-angle axis stays inside the product tube. For small real angles, H2 and Lemma 4 make \(W_n(r_z\zeta)\) constant. The one-variable identity theorem continues this equality to \(z=is\). The identity theorem in the difference variables extends boost invariance to the full product tube. Spatial rotations already preserve the kernels. Every \(\Lambda\in SO^+(1,3)\) is a product of these transformations: rotate and boost \(e_0\) to \(\Lambda e_0\); the residual transformation fixes \(e_0\) and belongs to \(SO(3)\).

Change variables by \(\Lambda\) in (24). Its determinant is one and the transformed approach vectors remain in \(V_+\). This proves Lorentz invariance of \(\mathcal W_n\) on tensors; continuity and tensor density extend it to all tests. Define
\[
 V(\Lambda)\phi(f_1)\cdots\phi(f_n)\Omega
       =\phi(f_1\circ\Lambda^{-1})\cdots\phi(f_n\circ\Lambda^{-1})\Omega.
                                                               \tag{29}
\]
Hermiticity writes the inner product of two polynomial vectors as a Wightman value, with the first string conjugated and reversed. Lorentz invariance preserves every such inner product, so (29) respects all linear relations and is isometric. The inverse rule uses \(\Lambda^{-1}\). Density gives a unitary on \(\mathcal H\), with the group law and field covariance on \(\mathcal D_0\).

As \(\Lambda\to1\), \(f\circ\Lambda^{-1}\to f\) in Schwartz space: the chain rule and uniform Schwartz decay for matrices near the identity bound each seminorm. Lemma 3 gives strong continuity on polynomial vectors; unitarity extends it to all vectors. On the same dense domain, translation covariance gives \(V(\Lambda)V(a)V(\Lambda)^{-1}=V(\Lambda a)\). Consequently \(V(a,\Lambda)=V(a)V(\Lambda)\) has the Poincaré group law and is strongly continuous. Every transformation fixes \(\Omega\) by construction. \(\square\)

*Origin:* `wightman.md` §6 through (19); `o4-check-2.md` §4. Y3 L80867–80989, Proposition IV-76-44, with \(SO^+(1,3)\) and three spatial directions.

**Lemma 10 (locality).** If \(f,h\in\mathcal S(\mathbb R^{1+3})\) have spacelike-separated supports, then \( [\phi(f),\phi(h)]\psi=0\) for every \(\psi\in\mathcal D_0\). Here spacelike separation means \(|\mathbf x-\mathbf y|>|x^0-y^0|\) for every pair in the two supports.

*Proof.* First take compact smooth tests. By Hermiticity it suffices to interchange adjacent spacelike-separated slots \(k,k+1\) in a vacuum value. Let \(K=\prod_j\operatorname{supp}f_j\); zero tests give zero. Choose in order
\[
 \begin{gathered}
 \delta=\min_K(|\Delta\mathbf x_k|-|\Delta t_k|)>0,\qquad
 M=\max_{K,j<n}(|\Delta\mathbf x_j|+|\Delta t_j|),\\
 A=4/\delta,\qquad h_*=2AM+6,\qquad \eta_0=\min(1,(2A)^{-1}),\\
 h_k^\lambda=-\lambda/2,\quad h_{k+1}^\lambda=\lambda/2,\\
 h_j^\lambda=-\tfrac12-(k-j)h_*\ (j<k),\qquad
 h_j^\lambda=\tfrac12+(j-k-1)h_*\ (j>k+1),\\
 z_j=\iota x_j+\eta h_j^\lambda e_4,\qquad
 -1\le\lambda\le1,\quad 0<\eta\le\eta_0 .              \tag{30}
 \end{gathered}
\]
Here \(\Delta x_j=x_{j+1}-x_j\). Put \(v=\Delta\mathbf x_k/|\Delta\mathbf x_k|\) and choose \(u=\cos\theta\,e_4+\sin\theta\,(v,0)\), with \(\sin\theta=A\eta\). Since \(A\eta\le1/2\), \(\cos\theta\ge\sqrt3/2\). The imaginary part of each difference is \(-\Delta t_je_4\), and the perpendicular projection of \(e_4\) has norm \(\sin\theta\). Therefore
\[
 d_u(z_{j+1}-z_j)
  =\eta\Delta h_j\cos\theta+A\eta v\cdot\Delta\mathbf x_j
                                  -A\eta|\Delta t_j|.   \tag{31}
\]
For \(j=k\) this is at least \(-\eta+A\eta\delta=3\eta\). For \(j\ne k\), \(\Delta h_j\ge h_*\), including the two neighboring slots, and (31) is at least \(\eta h_*/2-A\eta M=3\eta\). Thus (30) lies in the union (17), with \(|\mathscr S_n(z)|\le(C_{\rm ins}\eta^{-5})^n\). Its witnessing direction can vary; the holomorphic function is one fixed function.

For a smooth \(g\) supported in \(K\), put \(I_g(\lambda,\eta)=\int g(x)\mathscr S_n(z)dx\). Define \(D_\lambda=\sum_jh_j^\lambda\partial_{t_j}\) and \(D'=\tfrac12(\partial_{t_{k+1}}-\partial_{t_k})\). Differentiation and integration by parts give
\[
 \partial_\eta I_g=I_{-iD_\lambda g},\qquad
 \partial_\lambda I_g=\eta I_{-iD'g}.                    \tag{32}
\]
For each positive height the support has an open neighborhood in the tube union, so these operations are legitimate. The coefficients of \(D_\lambda\) are uniformly bounded. Lemma 6, with \(p=5n\), bounds \(|I_{D'g}|\) by one finite \(Q_g\), uniformly in \(\lambda,\eta\). Hence

\( |I_g(1,\eta)-I_g(-1,\eta)|\le2\eta Q_g\longrightarrow0.\)

For \(g=\bigotimes_jf_j\), the heights at \(\lambda=1\) increase in the original order; at \(-1\) they increase in the swapped order. Formula (24) applies to both endpoints, with positive vertical approach gaps. Symmetry of \(\mathscr S_n\) identifies the second labeling. The two Wightman values are equal.

Pairing with polynomial vectors and using Hermiticity gives the operator commutator identity for compact tests and compact polynomial entries. Cut off all other Schwartz entries and pass by Lemma 3's graph continuity. Density of polynomial vectors then gives the vector identity. Finally multiply \(f,h\) themselves by expanding compact cutoffs. Their supports remain subsets of the original spacelike-separated supports. Graph continuity proves the assertion for the original Schwartz tests. \(\square\)

*Origin:* `wightman.md` §6, (20)–(21); `o4-check-2.md` §4. Y3 L80991–81103, Proposition IV-76-52. The deformation uses the plane of time and the selected spatial separation; it works in four dimensions with the displayed projection.

**Theorem 11 (WR1 — Wightman reconstruction per component).** Let \(\sigma\) be a component with: E0′ from SR1(4), \(k_E=20\), \(\kappa_E=k+32\); invariance under \(\mathbb R^4\rtimes O(4)\) on separated and diagonal-flat tests (RO1 for \(\sigma\)); reflection positivity on positive-time diagonal-flat sequences (SR1(4), CL1); symmetry and reality; the cone and unique vacuum (CL1(4), PH1(5)); the plate density of RO1(2), `pd-port.md` (7); and the bounds of `cluster-port.md` §§8–9. Interpret these imports as H1–H5, with the order of choice above.

Then there are a separable Hilbert space, a dense invariant domain \(\mathcal D_0\), one Hermitian tempered scalar field, a strongly continuous unitary representation of the proper orthochronous Poincaré group with spectrum in \(\overline V_+\), locality, and a unique cyclic vacuum, whose Euclidean continuation is the \(\operatorname{tr}F^2\) hierarchy of \(\sigma\) on separated and diagonal-flat tests.

*Proof.* Use H3's separable Hilbert space. Lemmas 1–3 construct the field with tempered matrix elements and an invariant energy-smooth domain. Lemma 7 constructs its tempered vacuum distributions and their positive metric. Lemma 8 gives the dense polynomial domain, cyclicity, forward spectrum and unique vacuum. Lemmas 9–10 give Poincaré covariance and locality on that same domain. Lemma 7 identifies the analytic functions of the vacuum distributions as \(W_n\); Lemma 4 recovers the given hierarchy on separated \(C_c^1\) tuples. Lemma 5 recovers its unique supplied extension on diagonal-flat tests. All constructions used the same component. \(\square\)

*Origin:* skeleton WR1 in `ym4-assembly.md` §§4–5; `wightman.md`, Result; `o4-check-2.md` §4. Y3 L81105–81159, Theorem IV-76-59, is the direct three-dimensional source.

## Definitions supplied in distillation

The text makes explicit: separated tuples, their polynomial span and admitted concatenations; the diagonal-flat and positive-time test spaces, reflection of a test sequence, and the graded seminorm; the reflection quotient, vacuum and joint spectral variables; the common centering convention and local sharp norm; the slab and its degree-uniform insertion bound; the complex tube, adjoint involution, Minkowski embedding and momentum-sign convention; the point density, resolvent form, graph domain and smeared field; the scalar and vector kernels and their tilted ordering tubes; boundary approach vectors and derivative operators; the polynomial field domain and spacelike separation. The proof defines every auxiliary margin and locality deformation when it is chosen. These unpack the notes' interfaces; they add no physical assumption.

## Source record

SA and Y3 below are pinned at `31a47c543775`. The relevant `sa-index` README, chunk rows and neighboring rows, and `obligations.md` entries were read before the SA excerpts. The cited source ranges were read in bounded excerpts. All three library notes named in WR1 (`wightman.md`, `pd-port.md`, `cluster-port.md`) and `o4-check-2.md` were read whole, as were the supporting `o4-check-1.md` and `cluster-check.md`.

| Source | Lines checked and role |
|---|---|
| [SA outline](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM4_sketch_500.tex) | L4570–4640, H1–H3: H3 is explicitly an “imported theorem”; reconstruction “remains external”. L31533–31889 gives the test domains, RC1 and the per-component restriction. These statements specify the target, not the direct proof used here. |
| Same outline | L28527–28571 and L28701–28794: the conditional full insertion bound has exponent \(p+5\); its displayed choice \(p=4\) is weaker than the local input used here. L31135–31162 fixes the centering state inside the periodic DLR class. L31370–31527 supplies the conditional clustering/vacuum interface. |
| [Y3, `YM3/YM3_I.tex`](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM3/YM3_I.tex) | L79749–81160, read in consecutive bounded excerpts: (Rec1)–(Rec4), IV-75-22 through IV-76-59. These give the direct reconstruction in detail in three dimensions. Lemmas 1–10 carry that proof into four dimensions with the changes stated above. |

The checked-note provenance for every lemma is given at its end. `o4-check-2.md` records a line-by-line check by Claude of `wightman.md`, with first failing step none. That check applies to the note, not to this newly assembled part.

## Result

WR1 proves the conditional scalar reconstruction in Theorem 11, including its common dense domain, tempered distributions, Poincaré covariance, forward spectrum, locality and unique cyclic vacuum. Its imports are SR1, CL1, RO1 and PH1, precisely H1–H5. It reconstructs the supplied \(\operatorname{tr}F^2\) sector. Euclidean contact terms, nontriviality, and the upstream Yang–Mills construction are not conclusions of this part.

Corrections and explicit completions made in this distillation:

1. Retained the gate's componentwise scope: covariance and the uniform insertion/TU10 inputs belong to each realized component. The averaged hierarchy cannot replace it.
2. Retained the centering correction \(\nu_j\in\mathcal G_{a_j,\beta_j}\), and restored the component's own mean by the triangular shift in Lemma 1.
3. Removed the obsolete “D1 begins at C1/OH1” pointer. Upstream availability is governed by the imported parts and their actual hypotheses, not that historical pointer or the notes' old queue status.
4. Distinguished the full insertion bound from a fixed-label plate estimate, and the checked exponent five from SA's weaker displayed exponent nine. Kept local \(C^1\) continuity and uniformity over every outside polynomial.
5. Supplied the definitions, retained IN1's choice order, and renamed the slab constant \(c_{\rm sl}\) to avoid collision with IN1's \(c_0\). Made the four-dimensional choices explicit: \(l=6\), weight power three, \(J=\pi^2/2\), the \(S^3\) band estimate, and \(SO^+(1,3)\).
6. Wrote out slab exhaustion in the density construction, the graph-domain criterion and adjoint relation, general-test positivity, the ordered-tuple approximation in cyclicity, and the locality cutoff passage. Explicitly distinguished the slab integration variables from the original insertion positions, and the fixed initial regularizer from the vanishing boundary regularizers. These complete compressed steps in the checked note without changing the theorem.

No internal **Outstanding** step remains in this conditional argument after the hand check. Availability of H1–H5 is not proved here; their upstream dependencies remain imports. This is a distillation of a checked direct proof, with the listed completions. It is **not yet refereed as a whole part**, and grants no scientific or audit status.
