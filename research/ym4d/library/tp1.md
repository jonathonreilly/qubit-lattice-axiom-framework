# TP1: Two-point extraction from imported multiscale estimates

Provenance: Codex, pass 2 (distillation), 2026-11-04, checkout e1464b5d12d63c11ce0d15dbaa99373c579a485e. Research text, not an audit; grants no status. Based on Claude's `tp1-draft.md`, with the corrections in `ag1-draft.md`, `ag1-draft2.md`, and `ag1-tt-draft.md`. Source material credited to Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text. All proof steps are written arguments; no computer-assisted discharge.

This is a conditional extraction theorem. It does not establish its multiscale inputs for Wilson theory. In particular, the strengthened comparison assumptions below are not consequences of the ordinary source ball. References to other drafts import their statements with their remaining hypotheses, not a scientific status.

## 1. Definitions

Fix \(G=SU(2)\), \(N=2\), an odd integer \(L>1\), and a construction size \(M=L^{m_0}\ge5\), \(m_0\in\mathbb Z_{\ge1}\). A compatible torus has side \(\ell=2L^m\), \(m\in\mathbb Z\), \(m\ge m_0\). At integer cutoff \(K\), put \(a=L^{-K}\). In this manuscript integer level \(j\) has spacing \(a_j=L^ja\), \(0\le j\le K\); thus \(a_j\) is the draft's \(a_{(j)}\), not its \(a_j=L^{-j}\).

A plaquette index \(p\) includes one of the six unoriented coordinate planes, with one fixed orientation in each plane. Write \(x_p\) for its barycentre,
\[
 a_p(U)=1-\tfrac12\operatorname{Re}\operatorname{tr}U_p,\qquad
 O(f)=\sum_p f(x_p)a_p(U),\qquad
 S_2^T[\rho](f,h)=\rho(O(f)O(h))-\rho(O(f))\rho(O(h)).
\]
On a torus the tests are supported in a contractible patch; distances and integrals below use its Euclidean lift. Periodic Gibbs states mean the periodic Wilson DLR class of LG1, with the translation invariance required in STATE below.

Put \(\theta=1/12000\). A pair belongs to \(\mathfrak T(d;\theta)\) if \(f,h\) are nonnegative, nonzero, \(C^1\), supported in respective radius-\(d\) balls, and
\[
 d\le\operatorname{dist}(\operatorname{supp}f,\operatorname{supp}h)\le6d,\quad
 \int f\ge\theta d^4\|f\|_\infty,\quad
 \operatorname{Lip}f\le(\theta d)^{-1}\|f\|_\infty,
\]
with the same conditions on \(h\). Set \(t_f=\|f\|_\infty\), \(t_h=\|h\|_\infty\), and
\[
 \mathcal K(f,h)=\iint f(u)h(v)|u-v|^{-8}\,du\,dv,\qquad
 C_G=\frac{3(N^2-1)}{\pi^4},\qquad c_*=\frac{11N^2}{12\pi^2},\quad c_0=c_*\log L.
\]

A first-passage datum at \(g\) is an admitted flow \(x_0=\beta,\ x_j=x_{j-1}-b_j\) whose first entry, including time zero, into \((g^{-2},g^{-2}+B_\sharp]\) is at \(K\), with \(\beta\ge g^{-2}+B_\sharp\). Only \(K\ge1\) is used. With the fixed exponent \(\mathfrak p_0>1\), define
\[
 \bar x_s=g^{-2}+B_\sharp(s+1),\quad
 C_W(s)=C_{W,0}(\log\bar x_s)^{2\mathfrak p_0},\quad
 s=s(d)=\min\{s\in\mathbb Z_{\ge0}:L^sd\ge C_W(s)\},\quad D=L^sd,
\]
\[
 k_0=K-s,\qquad n=\lceil2\log_L\bar x_s\rceil,\qquad
 k_1=k_0+n,\qquad x=x_{k_0},\quad g_K(d)=x^{-1/2}.
\]
We require \(k_0\ge n_0\ge1\) and \(n\le s\). All asymptotics below fix \(g\); their bounds are uniform in admitted \((K,\beta)\), compatible volume, pair and position.

The running radius is
\[
 \check R_j=\min\{L^m:m\in\mathbb Z_{\ge0},\quad
 L^m\ge(\log\min_{0\le i\le j}x_i)^r\},\qquad r\ge2.
\]
It uses a running minimum, not an assumed monotone flow. A history cell at level \(j\) has physical side \(M\check R_j a_j\); a localisation cube has side \(Ma_j\). These are distinct from a lattice mesh cell of side \(a_j\). Live components and ancestry are those of the smooth-test construction in AG1. Precisely, for a component \(C\) live at level \(k\), put \(\mathsf Z_k(C)=C\), and recursively let \(\mathsf Z_j(C)\) be the union of live level-\(j\) components contained in \(\mathsf Z_{j+1}(C)\). Its lineage age is \(k-\min\{j:\mathsf Z_j(C)\ne\varnothing\}\); it is not the possibly restarted label age. Let \(\mathfrak L_j^{\ge b}(c)\) be the event that a live component of lineage age at least \(b\) meets history cell \(c\). At \(k_1\), let \(\Lambda\) be the event that a live component of any lineage age meets the prescribed neighbourhood of the supports of physical width \(CM\check R_{k_1}a_{k_1}\). On \(\Lambda\), let \(A\) be the largest contacting lineage age; put \(A=0\) off \(\Lambda\).

## 2. Imports and order of choice

The following are the complete hypotheses of the theorem. Constants in them are fixed, finite and uniform in the run, volume and test pair. All decay rates and disc radii are positive, \(B_\sharp>0\), \(c_2\ge0\), and the logarithmic exponents \(\mathfrak p,q,Q\) are nonnegative. Unnamed \(C,c>0\) may change between estimates. The same smooth-test construction, with \(\kappa_T=1/4\), must supply PRES, REG, AMP and AG.

**FLOW — IN1, OL1 and the constant-source part of SC1.** The admitted flows exist and are independent of unused finer cutoff and torus size. They satisfy \(b_j\le B_\sharp\) and
\[
 b_j=A_j^0-A_{j-1}^0+e_j,\qquad |A_j^0-jc_0|\le c_2,\qquad
 |e_j|\le Cx_{j-1}^{-1/2}(\log x_{j-1})^{\mathfrak p}
                 +Cx_{j-1}^{-\alpha},\quad
 \alpha=(\kappa_0-4)/2>1.                                      \tag{2.1}
\]
The source changes \(\beta\) to \(\beta-t\), with all auxiliary choices frozen. The resulting increments \(b_j(t)\) are holomorphic for \(|t|<2\varrho\), real on real \(t\), and
\[
 s_j=b_j'(0),\quad
 |s_j|\le C\{x_{j-1}^{-3/2}(\log x_{j-1})^{\mathfrak p_0}
                  +\varrho^{-1}x_{j-1}^{-\alpha}\},\qquad
 \zeta_k=1+\sum_{j=1}^k s_j=-\left.\frac{d x_k(t)}{dt}\right|_{0}.
                                                               \tag{2.2}
\]
Write \(\zeta=\zeta_{k_0}\). These are telescoped one-loop bounds; no convergence of individual one-loop increments is assumed.

**FREE — FC1 and the free decomposition with a terminal bound.** On each compatible torus the scalar plaquette covariance \(P\) of the standard Gaussian on \(\operatorname{ran}d_1\) has positive semidefinite slice covariances \(G_j\) and residual background covariances \(R_j\), with
\[
 P=\sum_{i=1}^jG_i+R_j,\qquad
 |G_j(p,q)|\le C(a/a_j)^4e^{-\delta |x_p-x_q|/a_j},\qquad
 |R_j(p,q)|\le C(a/a_j)^4.                                    \tag{2.3}
\]
A fixed one-level change in the slice convention is absorbed in \(C,\delta\). For orientations \(P_0,Q_0\), and \(a\le |u|/10\le\ell/100\),
\[
 |a^{-4}P(p_{P_0},q_{Q_0})-\mathbb K_{P_0Q_0}(u)|
 \le C|u|^{-4}\{(a/|u|)^{1/2}+(|u|/\ell)^4\},\quad u=x_p-x_q,
\]
\[
 \mathbb K(u)=\pi^{-2}|u|^{-4}\Lambda^2(I-2\hat u\hat u^{\,T}),
 \qquad \sum_{P_0,Q_0}\mathbb K_{P_0Q_0}(u)^2=6\pi^{-4}|u|^{-8}.
                                                               \tag{2.4}
\]
**Outstanding:** the full volume-uniform package (2.3)–(2.4) is imported, not proved here. In particular, the bound on \(R_j\) is additional to a bound on the slices. The source decomposition does not say \(R_K=0\).

Here is the Gaussian model to which REG must compare. There are nonnegative tents \(h_y^j(p)\), summing to one in \(y\), supported where \(|x_p-x_{p,y}|\le C_hMa_j\). Put
\[
 f_p^0=f(x_p),\qquad f_p^j=\sum_yh_y^j(p)f(x_{p,y}),\qquad s_0=1.
                                                               \tag{2.5}
\]
The tents are independent of the test and preserve plaquette orientation. Let \(\phi_i^\nu\), \(1\le i\le k_1,\ 1\le \nu\le N^2-1\), be independent centred real Gaussian vectors with covariance \(G_i\). Define
\[
 F_{>j}^\nu=\sum_{j<i\le k_1}x_i^{-1/2}\phi_i^\nu,\quad
 \mathcal B(f)=\frac12\sum_{\nu,p}\sum_{j=0}^{k_1}s_jf_p^j(F_{>j}^\nu(p))^2,
 \quad \Gamma(f,h)=\operatorname{Cov}_{G}(\mathcal B(f),\mathcal B(h)).
                                                               \tag{2.6}
\]
In particular \(F_{>k_1}=0\). The terminal covariance in (2.3) is not included in (2.6); its contribution is estimated below.

**PRES — SC1's exact formed-source identity.** At level \(k_1\) there is a positive unsourced law \(\mathbb P\) on retained histories, block fields and stored variables \(y\), and a holomorphic exponent
\[
 Z(z)/Z(0)=\mathbb E_{\mathbb P}e^{\Phi(z;y)},\quad \Phi(0;y)=0,\quad
 \Phi=\Phi^{\rm pt}+\Phi^{\rm reg}+\Phi^{\rm live}+\Phi^{\rm far},
                                                               \tag{2.7}
\]
with differentiation through the expectation valid twice near zero.
Here \(Z\) is the Wilson partition function with source \(z_1f+z_2h\);
\(\Phi^{\rm pt}=\sum_p\varphi_p(z_1f(x_p)+z_2h(x_p);y)\).
The marginal on histories is exactly the law used in AG.
**Outstanding:** [ref-73.md](ref-73.md) establishes an abstract transport identity; identifying its logarithm with this formed exponent, with the following bounds, remains an input.

**REG — strengthened TP-cx and the Gaussian identification.** There is a deterministic common family \(\mathcal D_j\) of localisation domains, with
\(\Phi^{\rm reg}=\sum_{j\le k_1}\sum_{X\in\mathcal D_j} e_j(X;z,y)\).
Each domain has tree size \(m_j(X)\in\mathbb Z_{\ge0}\), a dependence region \(X^+\) of diameter at most \(CMa_j(m_j(X)+1)\), and the number of size-\(m\) domains whose dependence region meets a given level-\(j\) localisation cube is at most \(Ce^{\epsilon m}\). Here \(\kappa>\epsilon\). The energies are independent of a source whose support misses \(X^+\), and holomorphic on
\[
 |z_i|t_i<r_{\rm cx}x_j\quad\hbox{for each source meeting }X^+,
 \qquad (t_1,t_2)=(t_f,t_h).                                  \tag{2.8}
\]
All histories satisfy \(|e_j|\le Ce^{-\kappa m_j(X)}\); each \(e_j(X;\cdot)\) is independent of any source whose support misses \(X^+\). There are deterministic Gaussian energies \(e_j^G(X;z)\) on the same family, bounded by the same estimate, independent of any source whose support misses \(X^+\), and holomorphic on the discs (2.8), such that, on those discs, for every \(y\notin\Lambda\) and every \(j,X\),
\[
 |e_j(X;z,y)-e_j^G(X;z)|
       \le Cx_j^{-1/2}(\log x_j)^q e^{-\kappa m_j(X)},\qquad
 \sum_{j,X}\partial_{12}e_j^G(X;0)=\Gamma(f,h).                 \tag{2.9}
\]
The sums are normally convergent on smaller discs.

**Outstanding:** the draft's TP-cx only compares a domain when its background is regular. Absence of a live component near the supports at \(k_1\) does not by itself make all earlier domains regular, or complete a history-dependent domain list to one deterministic Gaussian list. The all-level comparison and common completion in (2.9) must be supplied, including previously healed regions. Its last equality, called **G-ID**, is also an import: the source-transport formula alone does not prove that these energies have exactly the Gaussian model (2.6). The supremum-norm discs (2.8), including levels \(j>k_0\), are stronger than the ordinary source ball.

**AMP — TP-live, TP-far and the first-derivative oscillation.** There are \(y\)-independent numbers \(c_i\) and a fixed \(Q\) such that, with derivatives at zero,
\[
 \begin{split}
 |\partial_i(\Phi^{\rm pt}+\Phi^{\rm reg})-c_i|
 &\le Cx^{-1}(\log x)^Qt_i(DL^{-n})^2 &&\text{on }\Lambda^c,\\
 |\partial_i(\Phi^{\rm pt}+\Phi^{\rm reg})-c_i|
 &\le Cx^{-1}(\log x)^Qt_i &&\text{on all histories},\\
 |\partial_i\Phi^{\rm live}|&\le Cx^{-1}(\log x)^Qt_i L^{4A}1_\Lambda,\\
 |\partial_{12}\Phi^{\rm live}|&\le Cx^{-2}(\log x)^Qt_ft_h L^{8A}1_\Lambda,\\
 |\partial_i\Phi^{\rm far}|&\le Cx^{-1}e^{-cD}t_i,\qquad
 |\partial_{12}\Phi^{\rm far}|\le Cx^{-2}e^{-cD}t_ft_h .
 \end{split}                                                  \tag{2.10}
\]
The live part vanishes off \(\Lambda\), and the failure of the required top-level small-field condition is included in \(\Lambda\). The contact neighbourhood meets at most \(C(M\check R_{k_1})^4\) cells.
**Outstanding:** these bounds, particularly the factors \(x^{-1},x^{-2}\) and only logarithmic prefactors, are not supplied by SA's displayed age-amplitude bound. That bound also has factors exponential in \(\check R\). We do not claim the weaker AG rate absorbs those factors for arbitrary \(r\).

**AG — AG-k1*.** For the same positive stopped law and smooth-test construction, uniformly in \(j,c\),
\[
 \sum_{b\ge0}L^{8b}\mathbb P^{(j)}(\mathfrak L_j^{\ge b}(c))
       \le C_{\rm AG}e^{-c_{\rm AG}(\log x_j)^2}.                \tag{2.11}
\]
We use it only at \(j=k_1\). This is the \(\check R\)-form of [ag1-draft2.md](ag1-draft2.md) (8.1) combined with the running-minimum step \(\min_i x_i\ge x_j-2c_2\) of this text (§4); ag1-draft2's own passage from \(\check R_k\ge(\log x_k)^r\) to the \((\log x)^2\) rate omits that step and must be repaired there. It is the output of ag1-draft2 §8, with the trigger input supplied conditionally by [ag1-tt-draft.md](ag1-tt-draft.md). Its named upstream inputs are (K)+(MI), (COV), (SM), (RS), (BGL), (R0)–(R3), (LT), LG1(3), and, in place of (TT), the conditional-law package (CL) with its strengthened room (5.4′).
**Outstanding:** (CL)(P) requires derivative and Hessian bounds on the non-Gaussian conditional exponent throughout the small-field region. Its proposed analytic supplier (P-an) is drafted in [pan-draft.md](pan-draft.md), which recasts (P-an)(d) as a uniform Kotecky-Preiss statement, proves (P-an) as an implication, and names (L) ([nl1-L-draft.md](nl1-L-draft.md)) as its first input. None of this is refereed. Other upstream imported estimates, including (LT), also remain imports. Neither (2.11) nor those estimates are asserted here unconditionally. The running-minimum convention is retained; if the upstream bound is first stated as \(e^{-c\check R_j}\), Lemma 4.1 yields (2.11) after reducing \(c_{\rm AG}\).

**STATE — LG1 and SR1.** Compatible torus measures have subsequential local limits that are periodic Gibbs states. Every state in this class is invariant under lattice translations. There are a fixed cell containing a unit ball with positive boundary buffer, constants \(Q_0\ge1,r_0>0\), and a source norm satisfying
\(\|F\|_\sharp\le C(\|F\|_\infty+\operatorname{Lip}F)\), such that for any two real tests in that ball there is one state-independent holomorphic \(E_C(z)\) for which
\[
 h_\omega(z)=e^{-E_C(z)}
       \omega(e^{z_1O(F_1)+z_2O(F_2)}),\qquad
 h_\omega(0)=1,\quad |h_\omega|\le Q_0
\]
on \(\sum_i|z_i|\|F_i\|_\sharp<r_0\), for every periodic Gibbs state \(\omega\) at the datum. This includes signed tests, finite sums of translates and overlapping supports. The common normalizer, not an estimate separately normalized for each state, is essential.

**LIMIT — CL1 and PH1.** Along the specified volume-first limits, centred first and second moments converge on separated test tuples. Every component under consideration has its own all-state realization, including convergence of its centred first and second moments (used in Lemma 7.1), with OS vectors built from centred fields, by periodic Gibbs states at admitted data with \(K\to\infty\); a mixture identity alone does not suffice. The limits and realized components are normalized real functionals with the reflection-positive OS construction. Write \(\vartheta(u_1,u_2,u_3,u_4)=(u_1,u_2,u_3,-u_4)\) and \((\vartheta f)(u)=f(\vartheta u)\). The vacuum \(\Omega=[1]\) has norm one, \(\langle\Omega,[O(f)]\rangle=\sigma(O(f))\), and for real positive-time \(f\), the vector \(v_f=[O(f)]-\sigma(O(f))\Omega\) satisfies
\(\|v_f\|^2=S_2^T[\sigma](f,\vartheta f)\). In each realized component the nonnegative self-adjoint Hamiltonian \(H\) satisfies \(\ker H=\mathbb C\Omega\); uniqueness of the vacuum is not required of a mixture. Conclusions for components have exactly the qualification of this realization input, for example almost every component if that is what PH1 supplies.

The order of constants is part of the hypotheses, not a consequence of this extraction argument. Retain IN1's order (SA 19469–19485):
\[
 \begin{gathered}
 (r,\mathfrak p_0,\mathfrak p_1,q,\kappa_0,\beta_s,\theta_s,\theta_c)
 \prec L\prec(M_1,R_1)\prec\kappa\prec(\bar\kappa,\kappa_1)
 \prec M_1'\prec M_2\prec(\Theta_1,\varpi_T)\prec M\\
 \prec\sigma_\star\prec a_\Lambda
 \prec(A_1,A_0,C_0,C_1,\alpha_1,\alpha_0,E_0,M_0,\alpha',\mathsf B)
 \prec(\underline\lambda,c_5,\bar B)\prec\gamma\prec(\varrho,c_a)
 \prec\text{later coupling ceilings}\prec(g,\ell,\beta,K).
 \end{gathered}                                                \tag{2.12}
\]
The weak frame constants \((\underline\lambda,c_5,\bar B)\) are fixed from earlier one-loop envelopes before \(\gamma\); returned \(B_\sharp,\lambda_\sharp\) do not feed back into their selection. Only finitely many age moments are requested; fix them before \(c_a\).

AG's smooth-test fraction is fixed first. Its geometric constants and tile integer are fixed before \(\kappa\), independently of \(M,\bar\kappa\), using the early weak flow envelope \(\bar B\) in place of any later returned \(B_\sharp\); subsequent requirements on \(M\) are floors. Constants depending on the later amplitude ratio \(A_0/A_1\) feed only the final coupling ceiling. Keep the room conditions, including (5.4′), at their existing IN1 positions.

**Outstanding (IN-order):** [c4-order.md](c4-order.md) flags the need for an early uniform UM cost envelope; [in1-draft.md](in1-draft.md), Part A, is a proposed supplier with its own inputs. Writing (2.12) does not establish that envelope or erase the flagged dependency cycle.

After this ordered package, fix the constants returned by FREE, PRES, REG, AMP, AG and STATE, and fix \(C_{W,0}\ge1\) and \(n_0\ge1\). Choose a new ceiling
\(\gamma_W\le\min(\gamma,\gamma_{\rm AG})\), where \(\gamma_{\rm AG}\) is the coupling ceiling of the AG inputs, including \(g^{-2}\ge\max(X_F,X_{TT})\) (ag1-tt-draft L419), after \(\varrho,c_a\), so that all imported ceilings hold, the error per step in (2.1) is at most \(\min(c_0/2,1)\), and the summation bound in Lemma 4.1 is at most \(1/3\). This does not redefine the earlier \(\gamma\). Fix \(0<g\le\gamma_W\) next. Choose \(d_0(g)>0\) last to enforce all geometric separations and error bounds below. No choice depends on a later cutoff or volume.

## 3. Main theorem

**Theorem 3.1 (conditional TP1).** Assume FLOW, FREE, PRES, REG including G-ID, AMP, AG, STATE and LIMIT with the order (2.12). There are \(\gamma_W,n_0\) as above and, for every \(0<g\le\gamma_W\), a \(d_0(g)\in(0,1/10)\) and a nondecreasing \(\varepsilon_g(d)\downarrow0\) as \(d\downarrow0\), with \(\varepsilon_g(d)\le1/2\), such that for every admitted datum with \(K-s(d)\ge n_0\), every \(d\le d_0(g)\), and every pair in \(\mathfrak T(d;\theta)\),
\[
 S_2^T[\rho](f,h)
   =C_G\zeta^2x^{-2}\mathcal K(f,h)(1+r_\rho),\qquad
 |r_\rho|\le\varepsilon_g(d),                                 \tag{3.1}
\]
both for compatible torus Wilson measures and for every periodic Gibbs state at the datum. Moreover, uniformly in these data,
\[
 \frac{x}{c_*\log(1/d)}\longrightarrow1,\qquad \zeta\longrightarrow1,\qquad
 0\le S_2^T[\rho](f,h)\le C[\log(1/d)]^{-2}t_ft_h.              \tag{3.2}
\]
Every limit and every realized component in LIMIT satisfies
\[
 S_2^T(f,h)=C_G[c_*\log(1/d)]^{-2}\mathcal K(f,h)(1+\eta),
 \qquad |\eta|\le\eta_g(d)\longrightarrow0,                   \tag{3.3}
\]
with \(\eta_g\le1/2\) after reducing \(d_0(g)\), and the same TU10 upper bound. In each such component the restriction of \(H\) to \(\Omega^\perp\) is nonzero.

The proof is given by the numbered lemmas below and concluded in §7.

## 4. Flow and geometric estimates

**Lemma 4.1 (telescoping and normalization).** For a sufficiently small ceiling chosen as in §2,
\[
 x_j>g^{-2},\qquad
 \tfrac{c_0}{2}(k-i)-2c_2\le x_i-x_k
       \le(c_0+1)(k-i)+2c_2\quad(0\le i\le k\le K).             \tag{4.1}
\]
At the witness scale,
\[
 x=c_0s+O_g\!\left(1+\sqrt{s}\,[\log(g^{-2}+s)]^{\mathfrak p}\right),
 \qquad x\asymp_g\bar x_s,\qquad
 x/[c_*\log(1/d)]\longrightarrow1.                            \tag{4.2}
\]
For every \(k\le K\),
\[
 |\zeta_k-1|
 \le C\{x_k^{-1/2}(\log x_k)^{\mathfrak p_0}
                  +\varrho^{-1}x_k^{1-\alpha}\}\le1/3.        \tag{4.3}
\]
For \(k_0\le j\le k_1\), \(x_j=x+O(n+1)\), \(x_j\in[x/2,2x]\), and
\[
 \sum_{k_0<j\le k_1}|s_j|\le Cn\sigma(x),\quad
 \sigma(x)=x^{-3/2}(\log x)^{\mathfrak p_0}
                         +\varrho^{-1}x^{-\alpha}.            \tag{4.4}
\]

*Proof.* Before first entry, an \(x_j\) above the window cannot jump below its lower endpoint because \(b_{j+1}\le B_\sharp\). Induction gives \(x_j>g^{-2}\). Telescoping (2.1) gives
\(x_i-x_k=c_0(k-i)+O(2c_2)+\sum_{i<j\le k}e_j\).
The chosen ceiling bounds each \(|e_j|\) by \(\min(c_0/2,1)\), proving (4.1). No sign of an individual increment has been used.

The functions \(t^{-b}(\log t)^q\) decrease for sufficiently large \(t\), for fixed \(b>0,q\ge0\). From (4.1), \(x_{j-1}\ge g^{-2}+(c_0/2)(K-j+1)-2c_2\). Choose the ceiling also so that \(g^{-2}\ge4c_2+2\). Summing the two errors in (2.1) over the last \(s\) steps gives respectively at most
\(C\sqrt{s}[\log(g^{-2}+s)]^{\mathfrak p}\) and \(C_g\), since \(\alpha>1\).
The endpoint lies in the fixed first-passage window, proving the first formula in (4.2). Also \(x\le\bar x_s\) by \(b_j\le B_\sharp\), while (4.1) gives \(x\ge g^{-2}+(c_0/2)s-2c_2\).

Minimality of \(s\), for \(s\ge1\), gives
\[
 C_W(s)\le D<LC_W(s),\qquad s\log L=\log(1/d)+\log D.
\]
Thus \(s\asymp\log(1/d)\), \(D\asymp_g(\log x)^{2\mathfrak p_0}\), and
\(\log D=O_g(\log\log(s+2))\); (4.2) follows. In particular \(n=O_g(\log x)=o(s)\), so \(n\le s\) after reducing \(d_0(g)\).

For \(b>1\), splitting \(X+\lambda m\) into intervals
\([2^\nu X,2^{\nu+1}X)\) proves
\[
 \sum_{m\ge0}(X+\lambda m)^{-b}[\log(X+\lambda m)]^q
       \le C_{\lambda,b,q}X^{1-b}(\log X)^q.                  \tag{4.5}
\]
Indeed the \(\nu\)-th interval has at most \(C_\lambda2^\nu X\) terms and contributes at most
\(CX^{1-b}(\log X)^q2^{-(b-1)\nu}(1+\nu)^q\); that geometric series converges. Apply (4.5), (4.1) and (2.2) with \(b=3/2,\alpha\), shifting \(X\) by \(2c_2\), to obtain (4.3). The same proof bounds \(\sum_{j\le K}|s_j|\) uniformly by \(1/3\). On the \(n\) following levels, (4.1) bounds \(|x_j-x|\) by \(C(n+1)\), and summing (2.2) gives (4.4). ∎

The second term of (4.3) is retained: \(\kappa_0>6\) gives convergence, but by itself does not imply an \(O(x^{-1/2}\log^{\mathfrak p_0}x)\) bound. IN1's stronger choice \(\kappa_0>8\) is compatible with this statement.

**Lemma 4.2 (shape and tent bounds).** For the shape class,
\[
 10^{-8}\theta^2t_ft_h\le\mathcal K(f,h)\le v_4^2t_ft_h,
 \qquad v_4=\pi^2/2.                                         \tag{4.6}
\]
For \(j\le k_0\),
\[
 \|f^j-f^0\|_\infty\le C(\theta D)^{-1}t_f,\qquad
 \operatorname{supp}f^j\subset
       \{\operatorname{dist}(\,\cdot\,,\operatorname{supp}f)\le C_hMa_j\}.
                                                               \tag{4.7}
\]
For every \(j\), \(\|f^j\|_\infty\le t_f\), and its support has at most
\(Ca^{-4}(d+C_hMa_j)^4\) plaquettes. If two bounded profiles are supported in radius-\(2d\) balls separated by \(d/2\), then, for \(a\le d/20\),
\[
 \sum_{p,q}|u_pv_q|a^8|x_p-x_q|^{-8}\le C\|u\|_\infty\|v\|_\infty.
                                                               \tag{4.8}
\]

*Proof.* All distances between the two original supports lie between \(d\) and \(10d\). Bounding the kernel by these endpoints and using the mass and support assumptions proves (4.6). The nonnegative partition and its support radius prove the supremum, support and Lipschitz estimates in (4.7), since \(a_{k_0}=d/D\). Counting lattice cubes in an enlarged support ball proves the cardinality bound; \(a_j\ge a\) absorbs boundary cubes. For (4.8), each support has at most \(C(d/a)^4\) plaquettes, and the kernel is at most \(2^8d^{-8}\). Multiplication proves the estimate. ∎

No assertion that the tents preserve an \(L^1\) norm is needed or follows from their partition of unity.

## 5. Gaussian extraction

**Lemma 5.1 (exact derivative identity).** Under PRES, writing \(\Phi_i=\partial_i\Phi(0;y)\) and \(\Phi_{12}=\partial_{12}\Phi(0;y)\),
\[
 S_2^T(f,h)=\operatorname{Cov}_{\mathbb P}(\Phi_1,\Phi_2)
                              +\mathbb E_{\mathbb P}\Phi_{12},
 \qquad \partial_{12}\Phi^{\rm pt}=0.                         \tag{5.1}
\]

*Proof.* On a finite torus,
\[
 Z(z)=\int\exp\!\left[-\sum_p
    \{\beta-z_1f(x_p)-z_2h(x_p)\}a_p(U)\right]\,dU .
\]
It is entire by boundedness \(0\le a_p\le2\) and finiteness of the sum. Its logarithm exists near zero because \(Z(0)>0\). Differentiating \(\log Z\) yields the connected covariance. Differentiating (2.7), using \(\Phi(0;y)=0\), yields the right-hand side of (5.1). Every pointed summand depends on at most one of \(z_1,z_2\), since \(f(x_p)h(x_p)=0\); hence its mixed derivative vanishes. ∎

This exact locality of a source change does not establish the discs or comparison estimates in REG.

**Lemma 5.2 (Gaussian main term).** Under FLOW and FREE,
\[
 \Gamma(f,h)=C_G\zeta^2x^{-2}\mathcal K(f,h)
                         +x^{-2}t_ft_h\,o_g(1).              \tag{5.2}
\]
The error is uniform in the sense specified in §1.

*Proof.* A centred Gaussian pair \(X,Y\) obeys
\(\operatorname{Cov}(X^2/2,Y^2/2)=\operatorname{Cov}(X,Y)^2/2\).
To verify this, differentiate
\(\mathbb E e^{uX+vY}
=\exp((u^2\mathbb EX^2+2uv\mathbb EXY+v^2\mathbb EY^2)/2)\)
twice in each variable. This formula also holds for degenerate covariances by realizing the vector as a linear image of independent Gaussians. With
\[
 C_{>j}(p,q)=\sum_{j<i\le k_1}x_i^{-1}G_i(p,q),
\]
independence of slices and colours gives exactly
\[
 \Gamma=\frac{N^2-1}{2}
       \sum_{p,q}\sum_{j,l=0}^{k_1}s_js_l f_p^jh_q^l
                              C_{>\max(j,l)}(p,q)^2.         \tag{5.3}
\]
Plaquette indices already include orientations; there is no second orientation trace in this formula.

We first treat \(j,l\le k_0\). Reduce \(d_0\) so that \(C_hM/D\le1/8\). Their profiles then remain separated by at least \(d/2\), with all cross-distances at most \(11d\).
The geometric-scale sum
\(\sum_i (r/a_i)^4e^{-\delta r/a_i}\) is bounded uniformly in \(r>0\):
for \(r/a_i\le1\) use the geometric fourth powers, and for \(r/a_i\ge1\) use exponential decay and geometric spacing. Hence, on these separated supports,
\[
 |C_{>j}(p,q)|\le Cx^{-1}(a/r)^4,\quad r=|x_p-x_q|,
\]
because (4.1) gives \(x_i\ge x_{k_1}-2c_2\ge x/3\) for every \(i\le k_1\), the only range used. Slices with \(i\le k_0\) have \(r/a_i\ge D/2\), so their absolute sum, with or without \(x_i^{-1}\), is bounded respectively by
\[
 Cx^{-1}(a/r)^4D^4e^{-cD},\qquad C(a/r)^4D^4e^{-cD}.
\]
Consequently every \(C_{>\max(j,l)}\) in this part can be replaced by \(C_{>k_0}\) at a cost bounded by \(Cx^{-2}D^4e^{-cD}t_ft_h\), using (4.8) and \(\sum|s_j|\le1/3\).

From (2.3), keeping the terminal background,
\[
 P=\sum_{i\le k_0}G_i+\sum_{k_0<i\le k_1}G_i+R_{k_1}.
\]
On the middle sum \(|x_i^{-1}-x^{-1}|\le C(n+1)x^{-2}\) by (4.1). Also
\[
 |R_{k_1}(p,q)|\le C(a/r)^4(DL^{-n})^4.
\]
It follows that
\[
 |C_{>k_0}(p,q)-x^{-1}P(p,q)|
 \le Cx^{-1}(a/r)^4\varepsilon_{\rm ker},\quad
 \varepsilon_{\rm ker}=\frac{n+1}{x}+D^4e^{-cD}+(DL^{-n})^4.
                                                               \tag{5.4}
\]
This is where the residual bound, missing from the draft's asserted decomposition, is used.

After replacing these kernels, the combined profile is
\[
 f^0+\sum_{j=1}^{k_0}s_jf^j
       =\zeta f^0+\sum_{j=1}^{k_0}s_j(f^j-f^0).
\]
By (4.7), its error relative to \(\zeta f^0\) has supremum at most
\(C(\theta D)^{-1}t_f\). Equations (4.8), (5.4) therefore replace the entire early-level part of (5.3) by
\[
 \frac{N^2-1}{2}\zeta^2x^{-2}\sum_{p,q}f(x_p)h(x_q)P(p,q)^2
\]
with error at most \(Cx^{-2}t_ft_h(\varepsilon_{\rm ker}+D^{-1})\).

For the remaining pairs let \(v=\max(j,l)>k_0\). No separation of the tent supports is assumed. The slice bound instead gives
\[
 |C_{>v}(p,q)|\le Cx^{-1}(a/a_v)^4.
\]
Both supports have at most \(Ca^{-4}(d+C_hMa_v)^4\) plaquettes, so
\[
 \sum_{p,q}|f_p^jh_q^l|\,C_{>v}(p,q)^2
          \le Cx^{-2}(1+D)^8t_ft_h.
\]
The sum of \(|s_js_l|\) over these pairs is at most \(Cn\sigma(x)\) by (4.3)–(4.4), including \(s_0=1\). Their total is thus at most
\[
 Cx^{-2}(1+D)^8n\sigma(x)t_ft_h=o_g(x^{-2})t_ft_h.             \tag{5.5}
\]
This support-count proof replaces the draft's invalid \(L^1\)-preservation step.

Finally (2.4), the lattice sum bound and a Riemann sum give
\[
 \frac{N^2-1}{2}\sum_{p,q}f(x_p)h(x_q)P(p,q)^2
      =C_G\mathcal K(f,h)
          +O_\theta\!\left((a/d)^{1/2}+(d/\ell)^4+a/d\right)t_ft_h.
                                                               \tag{5.6}
\]
Here are the details needed for uniformity. The matrix \(\Lambda^2(I-2\hat u\hat u^{\,T})\) is orthogonal, so the squared entries of \(\mathbb K(u)\) sum to \(6\pi^{-4}r^{-8}\); each entry and its derivative are bounded by \(Cr^{-4}\) and \(Cr^{-5}\). Squaring (2.4) incurs the first two errors in (5.6), using (4.8). For each orientation pair, the function
\(f(u)h(v)\mathbb K_{P_0Q_0}(u-v)^2\) is supported away from the diagonal, has gradient bounded by \(C_\theta d^{-9}t_ft_h\), and has support volume at most \(Cd^8\). Comparing each shifted mesh cube with its barycentre therefore gives error \(C_\theta(a/d)t_ft_h\). Boundary cubes obey the same bound by extending the tests by zero. Summing the six-by-six orientation pairs proves (5.6).

Now \(a/d=L^{-k_0}/D\le L^{-n_0}/D\to0\), \(\ell\ge2L^{m_0}\), \(L^n\ge\bar x_s^2\), \(D\) is a fixed power of \(\log x\), and \(n=O_g(\log x)\). Every error in (5.4)–(5.6) tends to zero. This proves (5.2). ∎

**Lemma 5.3 (weighted contact estimate).** Under AG, with
\(\mathcal A=\mathbb E[L^{8A}1_\Lambda]\),
\[
 \mathbb P(\Lambda)\le\mathcal A
 \le CC_{\rm AG}M^4L^4(\log(2x))^{4r}
             e^{-c_{\rm AG}(\log(x/2))^2}=:\mathcal A_*(x).     \tag{5.7}
\]
For every fixed \(q\), both \((\log x)^q\mathcal A_*(x)\) and
\((\log x)^q\mathcal A_*(x)^{1/2}\) tend to zero.

*Proof.* For a history in \(\Lambda\), a maximal-age contacting lineage meets some contact cell. Thus
\[
 L^{8A}1_\Lambda
 \le\sum_{c\ {\rm contact}}\sum_{b\ge0}
                  L^{8b}1_{\mathfrak L_{k_1}^{\ge b}(c)}.
\]
Take expectations, apply the bound for each cell in (2.11), then use the contact-cell count in AMP. Lemma 4.1 gives
\(x/2\le x_{k_1}\le2x\), while the definition using the running minimum gives
\(\check R_{k_1}\le L(\log x_{k_1})^r\).
This proves (5.7), exactly the replacement (6.3*) in AG1.

If an upstream version uses \(e^{-c\check R_j}\), (4.1) gives
\(\min_{i\le j}x_i\ge x_j-2c_2\ge x_j/2\); hence \(r\ge2\) gives (2.11), with a smaller fixed rate. Finally set \(y=\log x\). For large \(y\),
\((\log(x/2))^2\ge y^2/4\), and \(q\log y-cy^2/4\to-\infty\).
This also applies to the square root. ∎

The estimate concerns the unsourced law only. No claim about replication preserving source insertions is required.

**Lemma 5.4 (regular and live mixed derivatives).** Under REG, AMP and AG,
\[
 \mathbb E\Phi_{12}=\Gamma(f,h)+o_g(x^{-2})t_ft_h.              \tag{5.8}
\]

*Proof.* Only domains whose dependence region meets both supports contribute. Root such a domain in a cube meeting the first support. There are at most \(C(1+d/a_j)^4\) possible roots. Its diameter must be at least \(d\), so
\(m_j(X)+1\ge c\,d/(Ma_j)\). Summing the rooted entropy bound against \(e^{-\kappa m}\), with \(\kappa>\epsilon\), gives
\[
 B_j:=\sum_{X:\ X^+\ {\rm meets\ both}}e^{-\kappa m_j(X)}
           \le C(1+d/a_j)^4e^{-c d/a_j}.
\]
Since \(d/a_j=DL^{k_0-j}\),
\[
 \sum_{j\le k_1}B_j\le C\{D^4e^{-cD}+n(1+D)^4\}=:T(x).       \tag{5.9}
\]
The first part is a geometrically spaced exponential tail; the last \(n\) summands are each bounded by \(C(1+D)^4\). In particular \(T(x)\) is bounded by a fixed power of \(\log x\).

For a holomorphic function bounded by \(A_0\) on a bidisc of radii \(r_1,r_2\), two applications of the Cauchy integral formula give
\(|\partial_{12}\psi(0)|\le A_0/(r_1r_2)\).
Use radii \(r_{\rm cx}x_j/(2t_i)\) in (2.8). On \(\Lambda^c\), (2.9), normal convergence and \(x_j\ge x/3\) give
\[
 |\partial_{12}\Phi^{\rm reg}-\Gamma|
       \le Cx^{-5/2}(\log x)^qT(x)t_ft_h=o_g(x^{-2})t_ft_h.
                                                               \tag{5.10}
\]
For much larger \(x_j\), the same inequality follows from eventual decrease of \(t^{-5/2}(\log t)^q\), not from an upper bound on early couplings. On all histories the crude bound gives
\(|\partial_{12}\Phi^{\rm reg}|\le Cx^{-2}T(x)t_ft_h\).
The pointed mixed derivative is zero. By Lemma 5.2, \(|\Gamma|\le Cx^{-2}t_ft_h\).
On \(\Lambda\), the expected crude regular error is at most
\(Cx^{-2}(T(x)+1)\mathbb P(\Lambda)t_ft_h\), and the live error is at most
\(Cx^{-2}(\log x)^Q\mathcal A t_ft_h\).
The far error is \(Cx^{-2}e^{-cD}t_ft_h\).
Lemma 5.3 makes all these errors \(o_g(x^{-2})t_ft_h\), proving (5.8). ∎

**Lemma 5.5 (first-derivative covariance and reference law).** Under AMP and AG,
\[
 |\operatorname{Cov}_{\mathbb P}(\Phi_1,\Phi_2)|
                                      =o_g(x^{-2})t_ft_h.     \tag{5.11}
\]
Consequently (3.1) holds for all compatible torus measures with a uniform relative error tending to zero.

*Proof.* Subtract \(c_i\) from (2.10). Splitting \(\Lambda,\Lambda^c\), applying the triangle inequality in \(L^2(\mathbb P)\), and using \(L^{4A}1_\Lambda\) squared equal to \(L^{8A}1_\Lambda\), gives
\[
 \|\Phi_i-c_i\|_2
 \le Cx^{-1}t_i
  \left[(\log x)^Q\{(DL^{-n})^2+\mathcal A^{1/2}\}+e^{-cD}\right].
\]
The bracket tends to zero by \(L^n\ge\bar x_s^2\) and Lemma 5.3.
Cauchy–Schwarz bounds the covariance by the product of these two norms: subtracting the expectation can only decrease the \(L^2\) norm. This proves (5.11). Combine (5.1), Lemma 5.2 and Lemma 5.4. Dividing the absolute error by the main term is legitimate by (4.3) and (4.6), and yields the relative error. Every estimate is uniform in the compatible torus side. ∎

## 6. Transfer to all periodic Gibbs states

**Lemma 6.1 (common-normalizer comparison).** Under STATE, any two periodic Gibbs states \(\rho,\nu\) at the same datum satisfy, for \(a\le d/40\),
\[
 |S_2^T[\rho](f,h)-S_2^T[\nu](f,h)|\le C_\theta d^2t_ft_h.
                                                               \tag{6.1}
\]

*Proof.* First let \(F_1,F_2\) be any two tests admitted by STATE, and put \(u_i=\|F_i\|_\sharp\). If a test is zero there is nothing to prove. On the bidisc
\[
 |z_i|\le r_i=\frac{r_0}{4(Q_0+1)u_i},
\]
Schwarz's lemma on each complex ray gives \(|h_\omega(z)-1|\le1/2\). Indeed, with \(s=\sum|z_i|u_i\), apply Schwarz to
\((h_\omega(\lambda z)-1)/(Q_0+1)\) on \(|\lambda|<r_0/s\).
The convergent logarithm series then gives \(|\log h_\omega|\le\log2\).
Cauchy's formula bounds its mixed derivative by \(\log2/(r_1r_2)\).
The \(E_C\) derivatives cancel between the two states, so the bilinear difference
\(\Delta(F_1,F_2)=S_2^T[\rho](F_1,F_2)-S_2^T[\nu](F_1,F_2)\) obeys
\[
 |\Delta(F_1,F_2)|\le
 32(\log2)(Q_0+1)^2r_0^{-2}\|F_1\|_\sharp\|F_2\|_\sharp.       \tag{6.2}
\]

For completeness the packing uses lattice translations only. The two radius-\(d\) support balls have centres at distance at most \(8d\), and their union fits in a radius-\(5d\) ball about the midpoint. A lattice translation brings that midpoint within \(2a\) of the centre of the fixed unit ball. Use a lattice grid of spacing
\(v=a\lceil40d/a\rceil\in[40d,41d]\) in a fixed smaller cube inside that ball. For small \(d\) it contains \(J\ge c d^{-4}\) translates of the whole pair, with their containing radius-\(6d\) balls mutually disjoint and still inside the unit ball.

For signs \(\epsilon_k=\pm1\), define
\(F_1^\epsilon=\sum_{k=1}^J\epsilon_k f(\,\cdot-v_k)\) and
\(F_2^\epsilon=\sum_{k=1}^J\epsilon_k h(\,\cdot-v_k)\).
Disjointness gives \(\|F_i^\epsilon\|_\infty=t_i\). Their Lipschitz constants do not exceed those of the single tests: along a segment between distinct support balls, use the exit and entrance points, where the extended tests vanish; the two segment lengths sum to at most the original distance. Thus
\(\|F_i^\epsilon\|_\sharp\le C_\theta d^{-1}t_i\).
Apply (6.2), then average over independent signs. Bilinearity kills the terms with distinct translate indices; lattice-translation invariance makes each remaining term \(\Delta(f,h)\). Hence
\[
 J|\Delta(f,h)|\le C_\theta d^{-2}t_ft_h.
\]
Using \(J\ge cd^{-4}\) proves (6.1). This averaging is an exact finite identity, not a computational enumeration. ∎

**Lemma 6.2 (all-state law).** Equation (3.1) holds for every periodic Gibbs state, with one uniform error \(\varepsilon_g(d)\to0\).

*Proof.* For each fixed datum take a local subsequential limit \(\nu_*\) of compatible torus measures with sides tending to infinity, as supplied by STATE. For each fixed test pair, \(O(f),O(h),O(f)O(h)\) are bounded continuous local functions. Their expectations converge. Lemma 5.5 puts the torus covariance in a closed interval independent of volume; the same interval contains the covariance of \(\nu_*\). Local weak convergence applies to every such function, so no pair-dependent subsequence is needed.

Compare an arbitrary \(\rho\) with \(\nu_*\) using Lemma 6.1. By (4.3), (4.6) and \(x\asymp_g\log(1/d)\), the relative change is at most
\(C_\theta d^2[\log(1/d)]^2\to0\).
All estimates have deterministic bounds uniform in the data. If \(e_g(d)\) is their sum, replace it, on a sufficiently small interval, by
\(\sup_{0<t\le d}e_g(t)\). This is nondecreasing and tends to zero; enlarge it to include the torus error and reduce \(d_0\) until it is at most \(1/2\). This proves the claim. ∎

## 7. Limits and nontriviality

**Lemma 7.1 (TU10 and passage to limits).** Equations (3.2)–(3.3) hold under the hypotheses of Theorem 3.1.

*Proof.* The normalization statements in (3.2) are Lemma 4.1. Equations (3.1), (4.3) and (4.6), with \(x\ge(c_*/2)\log(1/d)\) (after one further reduction of \(d_0\)), give
\[
 0<S_2^T[\rho](f,h)
 \le\frac32\frac{16}{9}C_Gv_4^2(c_*/2)^{-2}
                              [\log(1/d)]^{-2}t_ft_h.         \tag{7.1}
\]
This is TU10; it is a statement on the specified nonnegative separated shape class.

For the continuum passage set
\[
 a_g(d)=\sup_{\rm admitted\ data}
 \left|\zeta^2\left(\frac{c_*\log(1/d)}x\right)^2-1\right|.
\]
Lemma 4.1 gives \(a_g(d)\to0\). The relative error after replacing the normalization in (3.1) by the continuum normalization is at most
\[
 \eta_g(d)=a_g(d)+(1+a_g(d))\varepsilon_g(d)\longrightarrow0.
\]
For fixed \(d\), every sufficiently fine datum in LIMIT satisfies \(K-s(d)\ge n_0\). Connected covariance is unchanged by subtracting arbitrary deterministic constants:
\[
 \rho((O(f)-c_f)(O(h)-c_h))
       -\rho(O(f)-c_f)\rho(O(h)-c_h)=S_2^T[\rho](f,h).
\]
Convergence of both first and second centred moments therefore gives convergence of connected covariances. The bounds (3.3) and (7.1) are closed, independent of datum, and pass to each volume-first limit. Apply the identical argument to the individual all-state realization of each component supplied in LIMIT. No inference from the covariance of a mixture is used. Finally reduce \(d_0(g)\) until \(\eta_g\le1/2\). ∎

**Lemma 7.2 (nonzero Hamiltonian on the vacuum complement).** Every realized component in LIMIT has \(H|_{\Omega^\perp}\ne0\).

*Proof.* Let \(\phi(u)=(1-|u|^2)^2\) on the closed unit ball and zero outside. It is \(C^1\), has supremum one, Lipschitz constant at most four, and
\[
 \int_{\mathbb R^4}\phi
 =2\pi^2\int_0^1r^3(1-r^2)^2\,dr=\pi^2/12>\theta.
\]
For \(c=(0,0,0,3d/2)\), put \(f(u)=\phi((u-c)/d)\).
Its support lies in positive time, and \((f,\vartheta f)\) is in
\(\mathfrak T(d;\theta)\): the reflected support gap is \(d\), the mass is \((\pi^2/12)d^4\), and \(4/d\le1/(\theta d)\).
By (3.3) and (4.6),
\[
 \|v_f\|^2=S_2^T[\sigma](f,\vartheta f)>0,\qquad v_f\perp\Omega.
\]
This does not assert \(v_f\in\operatorname{Dom}H\). Instead set
\(w=(1+H)^{-1}v_f\). The resolvent of a nonnegative self-adjoint operator is injective, maps into \(\operatorname{Dom}H\), and preserves \(\Omega^\perp\), since \((1+H)^{-1}\Omega=\Omega\). Thus \(w\ne0\) and \(w\perp\Omega\).
If \(Hw=0\), the imported identity \(\ker H=\mathbb C\Omega\) would force \(w=0\), a contradiction. Hence \(Hw\ne0\). ∎

*Proof of Theorem 3.1.* Lemmas 5.5 and 6.2 give (3.1), Lemmas 4.1 and 7.1 give (3.2)–(3.3) and TU10, and Lemma 7.2 gives the last assertion. The choices described after (2.12) suffice: after \(g\) is fixed, every required error tends to zero with \(d\), independently of cutoff and volume. ∎

## 8. Source checks and withdrawn reduction

Line numbers in this section refer to the files at Sussman–Alpoge commit
31a47c543775. The outline was located through [sa-index/README.md](sa-index/README.md), the neighbouring chunk rows and [sa-index/obligations.md](sa-index/obligations.md), then read in bounded source ranges. CA-I was consulted through [its 4.12–4.19 index](sa-index/ca-4.12-4.19/README.md). The sources are:

- [SA, the four-dimensional outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex).
- [CA-I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex) and [CA-III](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_III.tex).
- [YM3-I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM3/YM3_I.tex).

Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, are credited for these sources and the architecture used here. Balaban's free-slice method is used through the explicitly named FREE import; no proof of that import is attributed to the calculations in this manuscript.

| Draft citation or claim | Source check and consequence |
|---|---|
| SA 4165–4176; 4252–4415: D3, F1–F3, TU10 and phase realizations | These passages require persistence rather than creation rarity alone, a volume/state/position-uniform extraction, and a matched normalization. They explicitly allow an infinite-volume reference if its estimates are uniform in volume. Their TU10 deduction does not itself prove F2–F3. These qualifications are retained in FREE, STATE, LIMIT and Theorem 3.1. |
| SA 6844–6856: observable normalization and half-square approximation | The Wilson observable and small-field half-square normalization occur here. An approximation is not an exact identification with (2.6). That identification is G-ID; the Gaussian half-square calculation itself is proved in Lemma 5.2. |
| SA 17317–17334; 23258–23276: tests, propagation, waiting and healing | A recent creation excludes healing during the waiting window, and the previous live region is propagated into the next large-field region. This invalidates the draft's attempt to derive (H) from the healing rules; see Lemma 8.1. The radius uses the running minimum. |
| SA 19435–19489: induction and constant order | The stage statement is conditional on class membership and frame/tube conditions. The order, finite-age-parameter restriction, retained margins and weak-frame cycle cut are as recorded in (2.12). The IN-order obligation remains separate. |
| SA 22345–22407; 22562–22585; 22861–22891: sources, stored variables and formed energies | These passages supply source norms, transport and the running-shift structure. They do not establish this manuscript's all-history completion, coupling-sized supremum-norm comparison through \(k_1\), or G-ID. Abstract mass-one transport does not identify the formed exponent. |
| SA 23833–23903; 23929–23952; 26765–27086: common normalizer and transfer | The same normalizer is used for the states being compared; the cell statement includes signed and overlapping tests. Lemma 6.1 uses this stronger reading explicitly. The finite-reference transfer criteria ET8–ET10 are not used, because Lemma 5.5 is uniform in the torus side. |
| SA 26002–26012; 26073–26084: shape, witness and slope | The draft's shape citation to 26020–26030 and witness citation to 26062–26070 are displaced. These are the relevant definition passages. The slope estimate has two summable terms; (4.3) retains both. |
| SA 26028–26060; 26133–26176: free decomposition and extraction | The free increments are differences of successive background covariances. Their finite sum is \(P-R_j\), not \(P\). The final subtracted covariance must be bounded. The outline's recursion is not a proof of REG or G-ID; those are the additional inputs of the draft's alternative route. |
| SA 26085–26132; 26178–26180: derivative identity, ages and live terms | The covariance-plus-mean identity is re-proved in Lemma 5.1. The label age can restart at an island and is no larger than lineage age. The displayed live estimates contain \(L^{C\check R}\), and do not give AMP as written. A rate \(e^{-c(\log x)^2}\) suffices here because AMP is separately assumed with only logarithmic prefactors. |
| SA 28195–28226: GCB52 and the interacting conditional law | The complete-force term is present in field integration by parts; the requisite interacting convexity/symmetry/force estimates are not asserted there. This extraction does not perform field integration by parts. Its analytic replacement is still an input; AG's conditional-law assumptions are also not discharged by this observation. |
| CA-III 111180–111205; 111230–111252; 111383–111400; 111418–111436 | The lists mark old-region rarity (8.12) and exit bounds as proof outstanding, and record source/kernel, arrest and history-covariance gaps elsewhere. Arrest is in the later incomplete-proof list, not simply the first list's items 1–3. Nonconvergence of first-passage offsets is not used. None of these lists supplies a proof of an imported TP estimate. CA-I 49495–49517 and 54986–55006, read through the supplied index, retain conditional stage hypotheses; they do not close these gaps. |
| YM3-I 735–801, particularly 745–747 and 791–797 | The overview describes complex plaquette coefficients and the three-dimensional treatment of early large-field histories. It does not prove the four-dimensional coupling-sized uniform discs in REG. |
| YM3-I 87705–87812 | Corollary IV-68-44 is a small-torus result, includes a volume-dependent error, and uses a geometric coupling envelope in three dimensions. Its estimate cannot be imported as a volume-uniform four-dimensional reference law. The logarithmic witness construction is adapted, with (4.1)–(4.2) proved here. |
| YM3-I 88890–88925 | The connected-function passage and Lemma IV-69-33 support the reflected-vector construction. Lemma 7.2 additionally supplies the operator-domain step needed to infer a nonzero Hamiltonian from a unique vacuum. |

**Lemma 8.1 (the proposed healing reduction is unavailable).** The healing rule alone does not supply the draft's (H), which demands a fresh failure at each step of a surviving lineage.

*Proof.* At level \(i-1\), take a live component containing a creation of that step. The waiting rule excludes it from the healing operation at level \(i\). The definitions at SA 17320-17325 include its propagated region in \(\Omega_i^c\), then in \(Z_i\), independently of the outcomes of the fresh level-\(i\) tests. Thus survival of this component at the next step does not, by the rules, demand a fresh failure. A theorem forcing such a failure from additional field constraints would be a separate input. This is the rule-level conclusion of AG1, Lemma 2.3; it is not an assertion that a particular quiet history has positive Wilson probability. ∎

The draft's stagewise-product proof is therefore withdrawn. Even a separately assumed (H) would need a justified count of possible failure chains: a bound depending on the diameter of an arbitrary live component is not a uniform per-step branching constant. AG-k1* replaces this route.

The older attempts in [rarity-fresh-x.md](rarity-fresh-x.md) and [its cited gate](../gates/rarity-fresh-x-0e8a5a4e7.md) stop at a constrained-versus-free comparison; they do not prove AG. The divergent creation-union upper bound in the draft likewise proves no lower probability statement, so its claim that almost every coarse cell contains a creation is deleted. Neither failed attack is needed for the conditional theorem.

## 9. Definitions supplied in distillation

The following conventions or objects had to be made explicit for the argument to be a definite implication.

1. A plaquette index includes its orientation; the Gaussian covariance in (5.3) is scalar in that index. This prevents counting the six orientations twice.
2. The physical scale \(a_j=L^ja\), the Euclidean lift of a torus test pair, the first-passage convention including time zero, and the uniformity meaning of \(o_g(1)\).
3. The distinction between the running-minimum radius, history cells, localisation cubes, lineage age, the contact event \(\Lambda\), and its maximal age \(A\), with \(A=0\) off that event.
4. The residual background covariance \(R_j\), retained in the finite free decomposition.
5. The transported profiles \(f^j\), the precise finite Gaussian model \(\mathcal B\), and its covariance \(\Gamma\), with \(s_0=1\) and the terminal fluctuation field zero.
6. The common domain family, rooted entropy count and history-independent completion in REG; the separate equality G-ID. These are definitions of strengthened hypotheses, not constructions proved here.
7. The centering constants \(c_i\) in AMP, the weighted contact moment \(\mathcal A\) and its explicit majorant \(\mathcal A_*\).
8. The scope of the normalizer for signed sums and overlapping tests, the bilinear state difference \(\Delta\), and a packing made only of lattice translates.
9. The summation and error shorthands \(\sigma(x),C_{>j},\varepsilon_{\rm ker},B_j,T(x),e_g\), the uniform relative-error majorant \(\varepsilon_g\), the normalization error \(a_g\), and the continuum error \(\eta_g\).
10. The time reflection \(\vartheta\), normalized OS vacuum, qualification “realized component” from LIMIT, and domain vector \(w=(1+H)^{-1}v_f\) used in the Hamiltonian conclusion.

## Change log (pass 3 fixes, lead, 2026-11-04)

Applied the findings of `gates/tp1-gate.md` (Claude fresh session, first failing step none):
1. REG now gives the energies source-locality, and the Gaussian energies source-locality and holomorphy on (2.8), with (2.9) on those discs.
2. Lambda is the event that a live component of any lineage age meets the neighbourhood.
3. gamma_AG is defined (including g^{-2} >= max(X_F, X_TT)); (2.11) is cited as the R-check form of ag1-draft2 (8.1) plus this text's running-minimum step; ag1-draft2 (8.1) must be repaired.
4. The (P-an)(d) description now matches pan-draft (Kotecky-Preiss, first input (L)).
5. LIMIT includes convergence of each component's centred first and second moments, with centred OS vectors.
6. x_i >= x/3 restricted to i <= k_1; the bound x >= (c_*/2) log(1/d) notes the extra reduction of d_0.
7. SA 17325 -> SA 17320-17325.

The AG hypothesis rests on unrefereed drafts (ag1-draft, ag1-draft2, ag1-tt-draft, pan-draft); this does not affect the conditional implication.

**Status: frozen.** Reopens only on a `wrong` signal or when an import it reads changes.

## 10. Result

The distilled TP1 proves a conditional implication: FLOW, FREE, PRES, strengthened REG with G-ID, AMP, AG-k1*, STATE and LIMIT, supplied in the stated IN1 order, imply the uniform two-point law F2, running normalization F3, TU10, the corresponding continuum law for every realized component, and a nonzero Hamiltonian on each component's vacuum complement. The proof uses only written identities and estimates.

The corrections to the draft are:

1. Replace the stronger requested age rate by AG-k1* and (6.3*); withdraw the healing-rule reduction (H), its unsupported uniform chain count, and the probability conclusion drawn from a divergent upper bound.
2. Keep AG conditional on its named upstream inputs, including the trigger conditional law and its still outstanding analytic healed-factor package. Require the same smooth-test construction throughout.
3. Restore the terminal free covariance and its bound; specify the Gaussian model and expose G-ID, the common completion and the all-level regular comparison as additional outstanding inputs.
4. Distinguish AMP from SA's weaker displayed live bounds. The weaker AG rate is sufficient for AMP, not automatically for prefactors exponential in the running radius.
5. Replace the false tent \(L^1\)-preservation step by a support-count estimate, and remove the extra orientation trace.
6. Use telescoping instead of an unproved increment law or monotonicity; retain the running minimum, both normalization-slope terms and the correct sign \(\zeta_k=-x_k'(0)\).
7. Make the volume uniformity, signed-source normalizer, lattice packing and per-component realization hypotheses explicit; pass connected covariances using both first and second moments. The uniform errors yield the stronger limiting relative error \(\eta_g(d)\to0\).
8. Repair the Hamiltonian-domain inference by the resolvent, correct the displaced source references and the CA arrest-list attribution, and retain the unresolved IN-order input. Remove unused dilation and failed rarity attacks from the proof.

The outstanding points are marked at their use in §2. This manuscript does not prove those imports for Wilson theory, does not prove a four-dimensional Yang–Mills construction, and grants no status. It is **not yet refereed**.


*Referee status (lead, 2026-11-05): refereed line by line by a fresh Claude session; see the change log above and `gates/tp1-gate.md` (st1-r4: `gates/st1-r4-gate.md`). The "not yet refereed" sentence in the Result above predates that check.*
