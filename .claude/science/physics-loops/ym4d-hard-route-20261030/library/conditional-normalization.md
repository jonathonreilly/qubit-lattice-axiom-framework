# Conditional normalization at (BANACH)
Provenance: OpenAI Codex, GPT-6 family (exact serving variant and configured effort not exposed to this session); the filtered copy of commit `169e1d5f3` as supplied; research text, not an audit, granting no status.

## 1. Attack the insertion before expanding the interactions

**Discharged — notation for this calculation.** Write I for parts/hard-core--independent.md. Work in finite-dimensional real Euclidean spaces. Use the quadratic chart notation of mixed-coefficient-2.md: \(M=2^{-1/2}P_{Y,d}\), \(U=(G_{1,Y},G_{2,Y})\), \(\Sigma_0=MM^T>0\). This section proves identities for arbitrary such matrices; applying them beyond the quadratic chart is an implication, not a conclusion about the nonlinear density. Write

\[
 a=\Sigma _0^{-1/2}z,\quad R=\Sigma _0^{-1/2}U,
 \quad V=(I+RR^T)^{-1},\quad
 I_a(\eta)=\exp[-(a-R\eta)^T(a-R\eta)/2].                 \tag{1}
\]

Here \(\eta\) has its original standard product Gaussian law \(\mu\), included exactly once. For complex arguments the transpose in (1) is bilinear, not conjugate linear. The integration variable remains real.

**Discharged — exact normalization, including its potentially large reciprocal.** Completing the square in \(\eta\) gives

\[
 Z_a:=\int I_a\,d\mu
   =\det(I+RR^T)^{-1/2}\exp(-a^TVa/2),
 \qquad q_a:=I_a/Z_a.                                    \tag{2}
\]

Indeed the precision is \(B=I+R^TR\), its inverse is \(C=I-R^TVR\), and \(B^{-1}R^T=R^TV\), as direct multiplication verifies. The square-completion constant is \(-a^T(I-RB^{-1}R^T)a/2=-a^TVa/2\). Diagonalizing the real positive matrix \(B\), changing orthogonal coordinates, and completing the one-dimensional squares evaluates the Gaussian integral. The nonzero eigenvalues of \(R^TR\) and \(RR^T\) agree: the maps \(R\) and \(R^T\) identify their positive-eigenvalue eigenspaces, preserving multiplicities. Thus their determinants after adding the identity agree. This proves (2), first for real \(a\); the Gaussian exponential identity proved in Section 7 gives its entire continuation. No smallness of \(RR^T\) was used.

**Discharged — a bound that does not lose \(e^{C|a|^2}\).** For real \(a,b\),

\[
 \int |q_{a+ib}(\eta)|\,d\mu(\eta)
  =\exp\{b^T(I-V)b/2\}\leq \exp(|b|^2/2).               \tag{3}
\]

The modulus of the numerator is \(e^{|b|^2/2}I_a\); the modulus of its integral is \(Z_a e^{b^TVb/2}\). Their ratio proves (3). In particular a large real observed coordinate does not itself destroy the integrated complex bound. Estimating \(Z_a^{-1}\) separately would discard exactly this cancellation. Equation (3) concerns a fixed real \(R\), not the field-dependent matrix or its coefficient norm.

**Gap — the hardest term, now isolated rather than omitted.** For the full problem the numerator contains the inverse-coordinate Jacobian, \(e^\Psi\), and cuts, and \(R\) also varies with fields and sites. What is needed is an anchored, coefficient-summed estimate of the difference of their normalized integrals, retaining the cancellation in (2). Neither \(I_a\leq1\) at real arguments nor a separate bound on \(Z_a^{-1}\) supplies it. The following sections test this term by all three requested routes.

## 2. Route (a): spectator tails of the normalized insertion

**Discharged — a dimension-free perturbation bound.** For real \(a,R,E\), differentiate along \(R_t=R+tE\). Write \(V_t=(I+R_tR_t^T)^{-1}\), \(C_t=(I+R_t^TR_t)^{-1}\), \(m_t=R_t^TV_ta\), \(r_t=V_ta\). Under \(q_{a,R_t}\mu\), write \(\eta=m_t+X\), with \(X\) centered of covariance \(C_t\). The logarithmic derivative of the *normalized* insertion is the centered score

\[
 S_t=h_t^TX-(X^TH_tX-\operatorname{tr}(H_tC_t)),\quad
 h_t=E^Tr_t-R_t^TE m_t,\quad H_t=\tfrac12(R_t^TE+E^TR_t).       \tag{4}
\]

Differentiate the numerator in (1), whose score is \((a-R_t\eta)^TE\eta\), and subtract its expectation when differentiating \(Z_a\). The singular-value inequalities

\[
 C_t\leq I,\quad |r_t|\leq|a|,\quad |m_t|\leq |a|/2,
 \quad \|C_t^{1/2}R_t^T\|\leq1
\]

follow from \(1/(1+s^2)\leq1\), \(\|V_t\|\leq1\), \(s/(1+s^2)\leq1/2\), and \(s/\sqrt{1+s^2}\leq1\). Hence

\[
 (E S_t^2)^{1/2}
 \leq \tfrac32|a|\|E\|+\sqrt2\|E\|_{\rm HS}.
\]

To verify the quadratic variance used here, diagonalize a real symmetric matrix \(H\) and use independent standard Gaussians: \(E(X^THX-\operatorname{tr}H)^2=2\operatorname{tr}(H^2)\). The required moments \(EX_i^2=1, EX_i^4=3\) follow by integrating the derivatives of \(x e^{-x^2/2}\) and \(x^3e^{-x^2/2}\). The mixed cubic moment with a linear form vanishes by \(X\mapsto-X\). Finally \(\|C_t^{1/2}H_tC_t^{1/2}\|_{\rm HS}\leq\|E\|_{\rm HS}\). Integrating the derivative and using Cauchy–Schwarz gives

\[
 \int|q_{a,R+E}-q_{a,R}|\,d\mu
 \leq (\tfrac32|a|+\sqrt2)\|E\|_{\rm HS}.                 \tag{5}
\]

Differentiation under the integral is justified on the compact \(t\)-interval by completing the square: all differentiated integrands are polynomials times Gaussians of precision at least the identity, dominated by one integrable Gaussian with a finite interval-dependent constant.

**Discharged — complex observed coordinate, still with real matrices.** One also has

\[
 \int|q_{a+ib,R+E}-q_{a+ib,R}|\,d\mu
 \leq e^{|b|^2/2}\|E\|_{\rm HS}
 \{(\tfrac32+|b|)|a|+\sqrt2+|b|+|b|^2/2\}.              \tag{6}
\]

Indeed
\[
 q_{a+ib,R_t}=q_{a,R_t}
 e^{b^T(I-V_t)b/2}e^{\,i b^TR_t(\eta-m_t)}.
\]
The derivative of the first exponent has modulus at most \(\|E\||b|^2/2\). Also
\[
 m'_t=C_tE^TV_ta-R_t^TV_tE m_t,\qquad |R_tm'_t|\leq\|E\||a|,
\]
using \(\|R_tC_t\|\leq1/2\), \(\|R_tR_t^TV_t\|\leq1\), and \(|m_t|\leq|a|/2\). The derivative of the phase has expected modulus at most \(|b|\|E\|(1+|a|)\). These bounds and (5) prove (6).

**Implication — logarithmically distant spectator tails.** Delete the columns of \(R\) outside distance \(r\), obtaining \(R^{<r}\). If
\[
 \sum_{i:\,d(i,Y)\geq r}\|R_i\|_{\rm HS}^2
       \leq B^2e^{-2\lambda r},                            \tag{7}
\]
then (5) costs at most \((3|a|/2+\sqrt2)B e^{-\lambda r}\). For a single site at distance \(r\), weighting by \(e^{\sigma r}\), \(\sigma<\lambda\), leaves \(C(1+|a|)B e^{-(\lambda-\sigma)r}\). At \(r=A\log(1/g)\), \(|a|\leq C(L)p(g)\), and bounded \(|b|\), (6) therefore costs at most \(C(L)p(g)g^{A(\lambda-\sigma)}\). This tends to zero. By hand: with \(x=\log(1/g)\), choose an integer \(j>N\) and use \(e^{\epsilon x/2}\geq(\epsilon x/2)^j/j!\) to bound \(x^N e^{-\epsilon x}\).

**Discharged — shell constants.** If shell \(n\) has at most \(B_0(n+1)^4\) columns, each bounded by \(B_1e^{-\lambda_0 n}\), (7) holds with \(\lambda=\lambda_0/2\) and
\[
 B^2=\frac{24B_0B_1^2}{(1-e^{-\lambda_0})^5}.
\]
For \(n\geq r\), \(e^{-2\lambda_0n}\leq e^{-\lambda_0r}e^{-\lambda_0n}\). Sum using \((n+1)^4\leq24\binom{n+4}{4}\) and \(\sum_{n\geq0}\binom{n+4}{4}q^n=(1-q)^{-5}\), obtained by multiplying five geometric series. Region boundaries can only decrease this count. Actual kernel decay is a premise when applying this calculation.

**Unchecked — limitation.** These estimates control one Gaussian insertion; they do not sum arbitrary mixed site differences or control its correlation with the interacting weight divided by the unconditioned partition function.

## 3. Route (a): joint coefficient norms, including covariance changes

**Discharged — deterministic mean changes.** Let \(\mathcal A\) be a commutative coefficient algebra with positive monomial weights \(w_m\), submultiplicative under multiplication, and norm \(\sum_mw_m|f_m|\). This includes the field powers and finite-site difference algebra when its anchored tree weights satisfy that rule. For a deterministic mean series \(h=\sum_mh_m u_m\), with zero constant coefficient, put
\[
 B_h=\sum_mw_m\bigl(\|(I-V)^{1/2}\Re h_m\|
                          +\|(I-V)^{1/2}\Im h_m\|\bigr).
\]
At a real base \(a,R\), with \(X=\eta-R^TVa\),
\[
 \frac{q_{a+h,R}}{q_{a,R}}
 =\exp\{h^TRX-\tfrac12h^T(I-V)h\},\qquad
 \int\left\|\frac{q_{a+h,R}}{q_{a,R}}\right\|_{\mathcal A}
                    q_{a,R}\,d\mu\leq2e^{B_h^2}.            \tag{8}
\]
The covariance of \(RX\) is \(I-V\). Each real coefficient's normalized linear form is standard normal. Convexity, with weights proportional to its weighted standard deviation, bounds the exponential of the sum of absolute linear forms by a convex combination of \(e^{B_h|N|}\). Its expectation is at most \(2e^{B_h^2/2}\): use \(e^{t|N|}\leq e^{tN}+e^{-tN}\) and complete the square. The quadratic part costs \(e^{B_h^2/2}\). Split complex coefficients into real and imaginary parts. Finite coefficient truncations followed by monotone convergence prove the infinite-series assertion. There is no factor per noise coordinate.

**Discharged — small matrix changes in the same norm.** Write \(a\mapsto a+h\), \(R\mapsto R+E\), with deterministic algebra-valued \(h,E\), both having zero constant coefficient. Under the base conditional probability, write \(\eta=m+C^{1/2}X\), \(X\) standard Gaussian. Put
\[
 r=Va,\quad T=RC^{1/2},\quad u=h-E m,\quad F=EC^{1/2},
\]
\[
 \ell=F^Tr+T^Tu+F^Tu,\quad
 B=-\operatorname{sym}(T^TF)-\tfrac12F^TF,\quad
 A(X)=\ell^TX+X^TBX.                                     \tag{9}
\]
Expanding the two squares in (1), the omitted term is the constant \(-r^Tu-u^Tu/2\); it cancels on normalization. The new conditional density relative to the old one is therefore exactly
\[
                         \frac{e^{A(X)}}{Ee^{A(X)}}.      \tag{10}
\]
For each symmetric coefficient matrix \(B_m\), let \(K_m=|\Re B_m|+|\Im B_m|\), where the absolute value of a real symmetric matrix replaces its eigenvalues by their absolute values. Set
\[
 N=\sum_mw_m(\|\Re\ell_m\|+\|\Im\ell_m\|),\quad
 Q=\sum_mw_mK_m,\quad q=\operatorname{tr}Q,\quad \beta=N+q.
\]
If \(\beta\leq1/64\), then, including the inverse normalizing series,
\[
 E\left\|\frac{e^A}{Ee^A}-1\right\|_{\mathcal A}
                         \leq32\beta.                    \tag{11}
\]

**Discharged — proof and constants in (11).** Define
\[
 U(X)=\sum_mw_m(|(\Re\ell_m)^TX|+|(\Im\ell_m)^TX|)+X^TQX.
\]
Then \(\|e^A-1\|\leq Ue^U\), and
\[
 EU^2\leq2N^2+6q^2,\qquad Ee^{2U}\leq\sqrt2\,e^{4N^2+4q}.
\]
For the first bound use the triangle inequality in \(L^2\) and
\(E(X^TQX)^2=q^2+2\operatorname{tr}Q^2\leq3q^2\).
For the second apply Cauchy–Schwarz to the linear and quadratic exponentials. Convexity as in (8) gives \((Ee^{4\,\mathrm{linear}})^{1/2}\leq\sqrt2e^{4N^2}\). Diagonalizing \(Q\) and completing the one-dimensional squares gives
\[
 (Ee^{4X^TQX})^{1/2}=\det(I-8Q)^{-1/4}
 \leq\exp\{2q/(1-8q)\}\leq e^{4q}.
\]
The determinant inequality follows from
\(-\log(1-s)=\sum_{j\geq1}s^j/j\leq s/(1-s)\).
Consequently
\[
 E\|e^A-1\|\leq
 2^{1/4}e^{2N^2+2q}(2N^2+6q^2)^{1/2}\leq12\beta.
\]
For this loose constant use \(2^{1/4}\leq2\), \(e^{2N^2+2q}\leq2\), and \((2N^2+6q^2)^{1/2}\leq3\beta\), all valid at \(\beta\leq1/64\). The inverse series of \(Ee^A\) has norm at most \((1-12\beta)^{-1}\), by summing its geometric series about 1. Subtracting its mean in (10) gives \(24\beta/(1-12\beta)\leq32\beta\). This proves (11), including nonvanishing throughout the coefficient domain.

**Discharged — sufficient matrix inputs.** Let \(m_0\) be the row dimension of \(R\), \(h_0\) the coefficient sum of Euclidean norms of the real and imaginary parts of \(h_m\), and \(e_0\) the corresponding Hilbert–Schmidt sum for \(E_m\). Then
\[
 N\leq(1+e_0)h_0+(3e_0/2+e_0^2/2)|a|,\qquad
 q\leq\sqrt{m_0}e_0+e_0^2/2.                             \tag{12}
\]
Indeed \(\|T\|\leq1\), \(\|T\|_{\rm HS}\leq\sqrt{m_0}\), \(|m|\leq|a|/2\), and \(|r|\leq|a|\). For the quadratic term use
\(\|T^TF_m\|_1\leq\|T\|_{\rm HS}\|F_m\|_{\rm HS}\) and
\(\|F_m^TF_n\|_1\leq\|F_m\|_{\rm HS}\|F_n\|_{\rm HS}\).
These follow by writing \(A^TB\) as the sum of outer products of corresponding rows, bounding each outer product's trace norm by the product of its vector lengths, and applying Cauchy–Schwarz to that sum. Symmetrizing does not increase trace norm. Splitting real and imaginary parts and using coefficient convolution proves (12) as written.

**Implication — applicability on the whole disc requires actual input bounds.** If the linear Gaussian field and site series give \(h_0\leq c/100\), \(e_0\leq C(L)g^\epsilon\), uniformly on \(|\zeta|\leq c/t_\#\), with \(|a|\leq C(L)p\), then (12) is at most \(1/64\) after taking \(c\) small and then \(\gamma\) small. Equations (10)–(11) then control all mixed insertion coefficients. This is conditional on those coefficient sums, not a substitution of scalar analyticity for them. The actual near row \(P_{Y,d}\) must retain its stated strict locality; a far site cannot be allowed to change that row.

**Gap — where route (a) stops.** The actual nonlinear change in \(\Xi\) depends on the integrated variables, and adds \(J\), the interacting weight, and cuts. Its logarithm is not the deterministic quadratic \(A(X)\). Bounding the whole interacting exponential before its connected normalization costs the whole region. The insertion alone is controllable by the preceding estimates; the connected interacting correction is not yet controlled.

**Implication — growing radius versus the slow spectator kernel.** The slow rate must be converted to coarse-link units before this test: \(\lambda=s_PL\), whereas the coefficient weight has rate \(\sigma=c_3<\lambda\) in those units. Suppose the kernel coefficient estimate of I:813, item (v), after summing its second leg, yields
\[
 e_0\leq C_*\sum_{n\geq0}B_0(n+1)^4
                  e^{-(\lambda-\sigma)n}
                  \min(\rho_e,Dg e^{c_1n}).               \tag{13}
\]
Here \(D\) includes the maximum scaling \(c/t_{\rm fl}\); it is independent of \(g\). Set \(\vartheta=\min(1/2,(\lambda-\sigma)/(2c_1))>0\). The elementary inequality \(\min(x,y)\leq x^{1-\vartheta}y^\vartheta\), checked separately for \(x\leq y\) and \(y\leq x\), proves
\[
 e_0\leq
 \frac{24C_*B_0\rho_e^{1-\vartheta}D^\vartheta}
 {(1-e^{-(\lambda-\sigma)/2})^5}\,g^\vartheta.             \tag{14}
\]
There is no factor depending on the cap distance or torus size. Thus a radius proportional to \(\log(1/g)\) does not defeat the *Gaussian* matrix estimate even though \(s_PL<c_1\). This application remains conditional on the summed kernel premise (13), including mixed site coefficients if they are present. It does not prove that premise for the full inverse coordinate.

## 4. Route (b): exact whitening and the cuts it produces

**Discharged — a localizable square root, without a small-covariance assumption.** Put \(H=RR^T\), \(S=(I+H)^{1/2}\), \(K=S^{-1}(S+I)^{-1}\). Then
\[
 C^{1/2}=T_0:=I-R^TKR,\quad 0\leq K\leq\tfrac12 I,\quad
                 \eta=R^TVa+T_0\chi,\quad \chi\sim N(0,I).
                                                               \tag{15}
\]
To verify this, on a singular direction of \(R\) with singular value \(s\), \(T_0\) acts by
\(1-s^2/[\sqrt{1+s^2}(1+\sqrt{1+s^2})]=1/\sqrt{1+s^2}\).
On \(\ker R\) it is the identity. Squaring gives \(C\) on every direction. The same scalar formula gives \(K\leq I/2\). For block columns \(R_i,R_j\),
\[
 \|(T_0-I)_{ij}\|\leq\tfrac12\|R_i\|\|R_j\|,\qquad
 |(R^TVa)_i|\leq\|R_i\||a|.                              \tag{16}
\]
Thus the transformed interaction has tails passing through the observed set; merely knowing \(C\leq I\) would not have supplied this locality. If \(\|R_i\|\leq B e^{-\lambda d(i,Y)}\), (16) gives the explicit two-leg tail
\(\tfrac12B^2e^{-\lambda(d(i,Y)+d(j,Y))}\).

**Discharged — whitening does not retain the original product cuts.** A cut on one original spectator coordinate becomes
\[
 {\bf1}_{\left|
 (R^TVa)_i+\chi_i-\sum_jR_i^TKR_j\chi_j
 \right|\leq p_i}.                                      \tag{17}
\]
Whenever some \(R_i^TKR_j\ne0\), \(j\ne i\), it reads another coordinate. For example, for the two scalar columns \(R=(r_1,r_2)\), with \(r_1r_2\ne0\), its cross coefficient is
\(-r_1r_2/[\sqrt{1+r_1^2+r_2^2}(1+\sqrt{1+r_1^2+r_2^2})]\ne0\).
This is a calculation about the coordinate change, not a counterexample to the SU(2) bound. The actual Gaussian kernels have tails rather than a specified zero pattern. The same issue applies to a fixed cut on a linear combination of noises.

**Discharged — a real tail estimate and its limits.** Under the uncut conditional Gaussian, a scalar coordinate has variance at most 1 and mean \(m_i\). If \(|m_i|\leq p_i/2\), then
\[
 \Pr(|\eta_i|>p_i)\leq2e^{-p_i^2/8}.                      \tag{18}
\]
For a centered Gaussian of variance \(v\leq1\), completing the square gives \(Ee^{tX}=e^{vt^2/2}\leq e^{t^2/2}\); Markov's inequality with \(t=p_i/2\) bounds each tail. The mean bound reduces the event to those tails. This proves (18) and shows exactly why it is unavailable for all near-root observed coordinates: \(|m_i|\) can be as large as \(\|R_i\||a|\), with \(|a|\) of order \(p_3=C(L)p\). No uniform \(p_i/2\) margin follows there.

**Gap — where route (b) stops at the same connected correction.** Analytic local interactions can be composed with (15) only on their analytic domain; arbitrary \(\chi\) do not remain there. The actual restrictions are (17), not independent restrictions on \(\chi_i\). For complex fields their moving inequalities are not a holomorphic integrand on real \(\chi\). Returning to fixed real integration domains restores analyticity of the *density*, but returns precisely to route (a). Even where (18) applies, a union bound over cuts costs \(|\Lambda|e^{-p_i^2/8}\), not a region-independent error. A connected estimate could cancel this extensive part; that estimate is the one still needed. No replacement of the cut ratio by 1 is justified by (18).

## 5. Route (c): rebuild the connected expansion and test its summation

**Discharged — auxiliary setting, with its scope stated.** In this section \(R,a\) are real and fixed, \(\mu\) is the product Gaussian, \(\nu=q_{a,R}\mu\), and \(H_X\) are bounded measurable functions depending only on coordinates in \(X\). They form a finite family. This is an auxiliary Gaussian problem; no extension of the actual chart beyond its cuts is being assumed. Set
\[
 H=\sum_XH_X,\quad
 h=\sup_i\sum_{X\ni i}\|H_X\|_\infty,\quad
 h_1=\sup_i\sum_{X\ni i}|X|\|H_X\|_\infty,\quad
 b_i=\|R_i\|_{\rm HS},\quad B_1=\sum_i b_i.
\]
For exponentially decaying root columns, the shell calculation in Section 2 makes \(B_1\) independent of region size, with a constant depending on the root. For interactions satisfying a summable polymer majorant, \(h,h_1\) are finite uniformly in region size. Those are explicit premises of the bounds below.

**Discharged — exact connected subtraction as a formal series.** Define
\[
 L(u)=\log E_\nu e^{uH}-\log E_\mu e^{uH}.
\]
For a probability \(\pi\), define its joint cumulant by the finite formula
\[
 \kappa_\pi(f_1,\ldots,f_n)=
 \sum_{\mathcal P}(-1)^{|\mathcal P|-1}(|\mathcal P|-1)!
                  \prod_{B\in\mathcal P}E_\pi\prod_{j\in B}f_j,
                                                               \tag{19}
\]
where \(\mathcal P\) runs over partitions of \(\{1,\ldots,n\}\).
Expanding \(\log(1+x)=\sum_{k\geq1}(-1)^{k-1}x^k/k\) proves the formula: a partition into \(k\) blocks has \(k!\) orders in the \(k\)-fold product, and division by \(k\) leaves \((k-1)!\). Consequently
\[
 L(u)=\sum_{n\geq1}\frac{u^n}{n!}
 \sum_{X_1,\ldots,X_n}
 \{\kappa_\nu(H_{X_1},\ldots,H_{X_n})
             -\kappa_\mu(H_{X_1},\ldots,H_{X_n})\}.         \tag{20}
\]
For sufficiently small \(u\) this is an analytic identity: if \(S=\sum_X\|H_X\|_\infty\), then
\(|E_\pi e^{uH}-1|\leq e^{|u|S}-1<1\) at \(|u|S<\log2\). This argument gives a radius depending on \(S\), hence on the whole region. It does not justify \(u=1\) uniformly.

**Discharged — the first connected coefficient has an anchored, region-independent bound.** Delete the columns \(R_X\), obtaining a reference insertion independent of the coordinates of \(X\). Its marginal on \(X\) is precisely \(\mu_X\). Applying (5) to this deletion, and then restricting to \(X\), gives, with \(A_a=3|a|/2+\sqrt2\),
\[
 |E_\nu H_X-E_\mu H_X|
 \leq A_a\|H_X\|_\infty\|R_X\|_{\rm HS}
 \leq A_a\|H_X\|_\infty\sum_{i\in X}b_i.
\]
Summing proves
\[
                         |[u]L(u)|\leq A_a h B_1.       \tag{21}
\]
This controls the first interacting correction by a polynomial in the observed coordinate, not by \(e^{C|a|^2}\).

**Discharged — a Gaussian two-block covariance bound, valid even for sharp bounded factors.** Suppose a Gaussian covariance \(C\) has \(C\geq\delta I\), and \(f,g\) depend on disjoint coordinate blocks \(A,B\). Then
\[
 |\operatorname{Cov}(f,g)|
 \leq\delta^{-1}\|f\|_\infty\|g\|_\infty
                                      \|C_{AB}\|_{\rm HS}. \tag{22}
\]
Keep the mean fixed and interpolate the covariance from
\(\operatorname{diag}(C_{AA},C_{BB})\) to the joint marginal covariance. Every interpolant \(C_t\) is at least \(\delta I\), by convexity. With \(D=\bigl(\begin{smallmatrix}0&C_{AB}\\C_{BA}&0\end{smallmatrix}\bigr)\), differentiating the Gaussian density gives its centered score
\[
 \tfrac12\{X^TC_t^{-1}DC_t^{-1}X-\operatorname{tr}(C_t^{-1}D)\}.
\]
The variance calculation following (4) gives its \(L^2\) norm
\(\|C_t^{-1/2}DC_t^{-1/2}\|_{\rm HS}/\sqrt2
\leq\|C_{AB}\|_{\rm HS}/\delta\).
The change in expectation of \(fg\) is bounded by this number times the two suprema. At \(t=0\) the blocks are independent with the same marginals as at \(t=1\). Integrating in \(t\) proves (22). No differentiation of \(f\) or \(g\) is used. Dominated differentiation follows from the uniform positive lower eigenvalue on this finite interval.

**Discharged — the second connected coefficient is also controlled in the auxiliary problem.** For \(\nu\),
\[
 \delta=(1+\|R\|^2)^{-1},\qquad
 C_{AB}=-R_A^TVR_B,\qquad
 \|C_{AB}\|_{\rm HS}\leq
                 \left(\sum_{i\in A}b_i\right)
                 \left(\sum_{j\in B}b_j\right).
\]
For disjoint \(X,Z\), the product reference has zero covariance. By (22), the sum of absolute conditional covariances over those pairs is at most \(\delta^{-1}h^2B_1^2\).
For overlapping \(X,Z\), apply the deletion argument to \(X\cup Z\) in each of the three terms
\[
 (E_\nu-E_\mu)(H_XH_Z)
 -(E_\nu-E_\mu)H_X\,E_\nu H_Z
 -E_\mu H_X\,(E_\nu-E_\mu)H_Z .
\]
Its modulus is at most
\(3A_a\|H_X\|_\infty\|H_Z\|_\infty
\sum_{i\in X\cup Z}b_i\).
Now \(\sum_{Z:\,Z\cap X\ne\varnothing}\|H_Z\|_\infty\leq|X|h\).
Sum separately over \(i\in X\) and \(i\in Z\); the two sums together are at most \(2B_1hh_1\). Thus
\[
 |[u^2]L(u)|
 \leq 3A_aB_1hh_1+\tfrac12\delta^{-1}h^2B_1^2.           \tag{23}
\]
This is a genuine connected subtraction; an unconditioned partition-function bound by itself would not give it.

**Discharged — why the support rule in the product library cannot just be reused.** Take two distinct scalar coordinates \(i,j\), mean zero, with \(C_{ij}\ne0\), and the bounded local factors \(\cos(t\eta_i)\), \(\cos(t\eta_j)\). Completing the Gaussian square, or integrating its characteristic function, gives
\[
 \operatorname{Cov}_\nu(\cos(t\eta_i),\cos(t\eta_j))
 =e^{-t^2(C_{ii}+C_{jj})/2}\{\cosh(t^2C_{ij})-1\}>0
 \quad(t\ne0).                                         \tag{24}
\]
The identity follows by writing each cosine as a sum of two exponentials and using
\(Ee^{iv^T\eta}=e^{-v^TCv/2}\). The strict inequality follows from
\(\cosh x-1=\sum_{n\geq1}x^{2n}/(2n)!\).
Here \(C_{ij}=-R_i^TVR_j\); the edge passes through the root and is not an overlap of the two supports. Equation (24) diagnoses the missing edge type. It is not an explicit failing configuration for the statement under investigation: (22) supplies precisely a decaying bound for this term.

**Discharged — the direct all-order majorization loses the needed connections.** Delete the columns of \(R\) in \(U=\bigcup_jX_j\). In each term of (19), telescope the product of block expectations between \(\nu\) and \(\mu\). A partition with \(k\) blocks costs at most \(k A_a(\sum_{i\in U}b_i)\prod_j\|H_{X_j}\|_\infty\). Multiplying by \((k-1)!\) and summing partitions costs at most \(n!2^{n-1}\): every ordered partition can be produced by a permutation of the \(n\) labels and a choice of cuts in its \(n-1\) gaps, so their number is at most \(n!2^{n-1}\). Summing the interaction labels therefore gives the valid but insufficient estimate
\[
 \sum_{X_1,\ldots,X_n}|\kappa_\nu-\kappa_\mu|
 \leq A_a n!2^{n-1}n hB_1 S^{n-1}.                       \tag{25}
\]
Only one of the \(n\) labels has been connected to the root in this estimate. The other \(n-1\) labels supply \(S^{n-1}\). This is the concrete failure of the direct insertion bound at higher connected order, not an inference that the true coefficient grows with the volume.

**Gap — where route (c) stops.** Formula (20) is rebuilt, and its first two connected orders have the explicit bounds (21), (23). I have not replaced (25) by a summable bound at all orders, with the field/site coefficient norm and actual cut insertions. An auxiliary sufficient estimate would bound its left side by \(n!K_Y(C h_1)^n\), with \(K_Y\) at most a fixed power of \(p\), uniformly in the region, while retaining the tree weights for sites. Treating each forbidden-tail indicator as an activity gives supremum 1, not \(H_0\); (18) is only an integrated single-tail estimate. The nearby conditional means need not have its margin. A proof at higher orders must keep the Gaussian connections and cut normalizations together. No general Gaussian cluster theorem is cited in place of that missing proof.

## 6. The single stopping inequality and its exact coefficient

**Gap — named stopping inequality: the connected conditional-normalization bound (CN).** Use precisely the inverse coordinate, Jacobian, fixed real cuts, and original denominator of the question. Write
\[
 \mathcal T_\zeta[e](w,s)=
 \frac{\displaystyle\int d\nu\,
 {\bf1}_{\mathcal C}J_\zeta e^{\Psi_\zeta}
             \phi_d(\Xi_\zeta(v,\chi;w,s))\,e(V_\zeta)}
 {N_{\rm good}^Z(W_\zeta)} .
\]
Here \(\chi=(\xi_d^\perp,\xi_{\mathrm{off}\ d},\eta)\);
\(d\nu=dv\,d\xi_d^\perp\,d\mu(\xi_{\mathrm{off}\ d})d\mu'(\eta)\);
and \(\phi_d\) is the normalized Gaussian on all the original \(\xi_d\) coordinates. Thus the Gaussian on \(\xi_d\) is not also in \(d\nu\). The variables \(s\) encode the stated finite site differences, without changing the two site states or their admissible distance. With the prescribed radii and tree weight, the remaining inequality is
\[
 \boxed{\quad
 \sup_{|\zeta|\leq c/t_\#}
 \sum_{\alpha,\mathcal S}\rho^\alpha
 e^{c_3\tau(Y';\,\operatorname{supp}\alpha,\mathcal S)}
 \left|[w^\alpha s^{\mathcal S}]\mathcal T_\zeta[e]\right|
       \ \leq\ C\,cc_j\omega_P P_P .
 \quad}                                                   \tag{CN}
\]
The quotient is initially a germ at the real base; the claimed bound requires its continuation throughout the disc. The estimate is required uniformly in the region, depth, and all allowed site positions and sizes, including distances proportional to \(\log(1/g)\), for the admissible growing old factors in the question. Here
\(P_P=\operatorname{Vol}(Z)^{3/2}(\log\operatorname{Vol}(Z))^{3/2}\)
is the stated moment factor. For bounded factors its right side is \(C\sup\|e\|\). The constant \(C\) must be absolute in the sense of (BANACH). This is the actual operator inequality; the partial lemmas above do not replace its density, norm, cuts, or denominator.

**Discharged — connection to source equation (11), with normalization retained.** At a site state \(r=0,1\), expand at fixed real integration coordinates
\[
 \Xi_r=\Xi_{r,0}+w\Xi_{r,1}+w^2\Xi_{r,2}+\cdots,\quad
 \log J_r=\ell_{r,0}+w\ell_{r,1}+w^2\ell_{r,2}+\cdots
\]
and \(\Psi_r=\Psi_{r,0}+w\Psi_{r,1}+w^2\Psi_{r,2}+\cdots\). The local logarithm of \(J_r\) is taken at its nonzero real-base value.
The log-density scores are
\[
 A_{r,1}=\ell_{r,1}+\Psi_{r,1}-\Xi_{r,0}\cdot\Xi_{r,1},
\quad
 A_{r,2}=\ell_{r,2}+\Psi_{r,2}-\Xi_{r,0}\cdot\Xi_{r,2}
                         -\tfrac12\Xi_{r,1}\cdot\Xi_{r,1}. \tag{26}
\]
This is exactly equation (11) of the source: multiply out \(-\Xi_r\cdot\Xi_r/2\). The cuts have no derivative in these fixed coordinates.

**Discharged — connection to source equation (13a).** Let \(\widetilde N_r(w)\) be the numerator integral with \(e=1\), on the replacement cuts, and let \(\theta_r=\widetilde N_r/N_{\rm good}^Z\). Let \(\langle\cdot\rangle_r\) normalize the replacement-cut density at \(w=0\). For a local test \(e(v)\), independent of \(w\) in these coordinates, division of its two power series gives
\[
 K_r(e)=\operatorname{Cov}_r(e,A_{r,2})
                  +\tfrac12\kappa_{3,r}(e,A_{r,1},A_{r,1}),
\]
\[
 [w^2]\mathcal T_r[e]
 =\mathscr K_r(e)
 =\theta_{r,0}K_r(e)
 +\theta_{r,1}\operatorname{Cov}_r(e,A_{r,1})
 +\theta_{r,2}\langle e\rangle_r.                         \tag{27}
\]
For direct verification, the unnormalized density multiplier is
\(1+wA_1+w^2(A_2+A_1^2/2)\).
The inverse of its expectation through order two is
\(1-w\langle A_1\rangle+w^2(\langle A_1\rangle^2
-\langle A_2+A_1^2/2\rangle)\).
Multiply the numerator by this inverse and then by \(\theta\).
The resulting third cumulant is
\(\langle eA_1^2\rangle-\langle e\rangle\langle A_1^2\rangle
-2\langle eA_1\rangle\langle A_1\rangle
+2\langle e\rangle\langle A_1\rangle^2\).
Thus (27) includes every connected subtraction and every cut-ratio term. For a general factor with its own \(w\)-coefficients, the additional terms are
\(\langle e_2\rangle+\operatorname{Cov}(e_1,A_1)\), before multiplication by \(\theta\); they cannot be dropped.

**Implication — (CN) gives precisely the necessary test (15).** A single term of the nonnegative sum in (CN), with \(\alpha=2\,{\bf1}_{\{c\}}\) and one site \(S\), is
\[
 \sup_{|\zeta|\leq c/t_\#}\rho(c)^2
 e^{c_3\tau(Y';\,\{c\},S)}
 |\mathscr K_{1,\zeta}(e)-\mathscr K_{0,\zeta}(e)|
                  \leq C\,cc_j\omega_P P_P.              \tag{28}
\]
It is the source's (15). The site coefficient is the difference of the two states by the definition of its finite-difference series. Equations (26)–(27) identify its actual interacting and normalization contributions. A Gaussian-only estimate of them, or setting \(\theta=1\), would not establish (28).

**Gap — why all three routes stop at (CN).** Route (a) controls the full normalized *quadratic* insertion, including an all-coefficient matrix perturbation estimate, but the interacting expansion presently gives the volume factor \(S^{n-1}\) in (25). Route (b) supplies the exact square root and its two-leg locality, but the transformed cuts (17) prevent using a fixed product probability measure on their support; their connected replacement error is part of (CN). Route (c) supplies the connected expansion and two nontrivial orders of its sum, but not the all-order, cut-inclusive coefficient sum on the continuation disc. These are three attempted approaches to one inequality, not three independent asserted failures of the original statement.

**Gap — what would settle this stop.** A rooted expansion of the actual fixed-cut inverse-coordinate density must attach every interaction or cut-boundary contribution either to \(d\) or to another contribution already attached to \(d\), allowing the extra Gaussian edges in (24). It must give a summable absolute majorant for those connected families *after* all field and site coefficients and the inverse normalizing series are included. The bound must be uniform for the stated growing site distance, and retain the cut-ratio coefficients in (27). The quadratic reference estimates (5), (11), (14), (16), and (22) are available pieces of such a proof. They do not supply the missing family estimate. An explicit violation using the actual SU(2) chart and its admissible sites would settle the question in the other direction; none is exhibited here.

**Unchecked — scope of the mathematical conclusion.** No explicit configuration satisfying the exact hypotheses has been shown to violate (CN). The non-product law, the nonzero covariance (24), and the failure of the majorant (25) are not counterexamples. Conversely, the polynomial-in-\(p\) Gaussian estimates do not establish (CN). Hence (15) is not obtained, and (BANACH) does not close by this work.

## 7. Reading and proof boundary

**Discharged — procedure.** Read GOAL.md and FINISH-rules.md first. Further reads were confined to this directory: bounded passages in the independent part around the chart, cuts, Gaussian split, parameter rates, good-sector expansion and Lemma 4.7c; the product cluster library; mixed-coefficient-2.md; and the specific coefficient/normalization passages in mixed-coefficient.md and tail-two-step.md needed to locate the user's (11), (13a), and (15). No mapped-side account, gate file, git history, outside-directory source, numerical job, audit, or subagent was used. Only this output file was written. Commands were for reading and writing text, not mathematical evidence.

**Discharged — finite-dimensional foundations recalled from memory and rebuilt here.** For a real symmetric matrix \(A\), maximize \(x^TAx\) on the unit sphere. Compactness gives a maximizer \(x\); differentiating along every tangent vector \(y\perp x\) gives \(y^TAx=0\), so \(Ax\) is a multiple of \(x\). Symmetry makes \(x^\perp\) invariant. Induction on dimension yields the orthonormal eigenbasis used above; positive roots act by positive scalar roots in that basis. Apply this to \(R^TR\). For each positive eigenvalue \(s^2\), \(u\mapsto Ru/s\) preserves inner products on its eigenspace and produces the corresponding eigenspace in the range. This proves the singular-direction identities used in the estimates. For the Gaussian exponential identity, \(F(t)=E e^{tX}\) with a standard scalar normal \(X\) is differentiable for complex \(t\), since on each bounded \(t\)-set its differentiated integrands are dominated by a polynomial times \(e^{B|x|-x^2/2}\). Integration by parts gives \(F'(t)=tF(t)\), with vanishing boundary terms. Thus the derivative of \(e^{-t^2/2}F(t)\) is zero, and \(F(0)=1\) gives \(F(t)=e^{t^2/2}\). Orthogonal diagonalization and products give the multivariate version, including (24).

**Unchecked — imported estimates and memory boundary.** No Gaussian cluster theorem or locality theorem from memory is used to discharge a claim. The independent part's kernel and inverse-coordinate estimates remain supplied premises where invoked as implications. The normalization formulas, tail estimates, coefficient majorants, and first two connected orders claimed discharged above have their arguments displayed; no remembered estimate for the unproved interacting family sum is being assumed.

**Gap — decision.** The single named inequality remaining is (CN), with the exact scores (26) and cut normalization (27). It is neither proved nor refuted here.

STOPPED
