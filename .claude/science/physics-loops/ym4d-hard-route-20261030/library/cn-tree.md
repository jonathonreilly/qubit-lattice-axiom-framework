# A forest interpolation at conditional normalization
Provenance: OpenAI Codex, GPT-6 (exact serving variant and configured effort not exposed); the filtered copy of commit `0dbf06c38` as supplied; research text, not an audit, granting no status.

## 1. Scope and the boundary that must be kept

**Unchecked — supplied inputs and memory.** Write I for `parts/hard-core--independent.md` and N for `library/conditional-normalization.md`. The kernel bounds, nonlinear chart bounds and rates in I are inputs here, not newly discharged theorems. The names Battle–Brydges–Federbush and Brydges–Kennedy, and the idea of a minimum-along-path interpolation, come from the question and memory. No theorem under either name is invoked: the finite formula used below is proved. No numerical result in the source is used.

**Discharged — the quadratic reference and its coordinates.** Use N(1):
\[
 d\mu(\eta)=(2\pi)^{-N/2}e^{-|\eta|^2/2}d\eta,\qquad
 I_a(\eta)=e^{-|a-R\eta|^2/2},\qquad
 C=(1+R^TR)^{-1},\quad m=CR^Ta.
 \tag{T1}
\]
These formulas in this section have real \(a,R\). Completing the square shows that \(I_a\,d\mu/Z_a\) is \(N(m,C)\). In particular the product noise occurs once. With \(V=(1+RR^T)^{-1}\), multiplication gives \(C=1-R^TVR\) and \(m=R^TVa\). Thus, for different coordinate blocks,
\[
 C_{ij}=-R_i^TVR_j,\qquad
 (1+\|R\|^2)^{-1}1\le C\le1.
 \tag{T2}
\]
The cuts below are always sets in the original, fixed real coordinates. An auxiliary convolution in a proof is not a replacement of those coordinates or cuts.

**Discharged — sharp cuts do not prevent density differentiation.** Let \(C(t)>0\) be a differentiable covariance, with fixed mean \(m\), and let \(D=\dot C(t)\). For its Lebesgue density \(p_t\), direct differentiation of the determinant and inverse gives
\[
 \dot p_t(x)=\frac12\bigl((x-m)^TC(t)^{-1}DC(t)^{-1}(x-m)
                 -\operatorname{tr}(C(t)^{-1}D)\bigr)p_t(x).
 \tag{T3}
\]
For completeness, differentiating \(C C^{-1}=1\) gives the inverse derivative; expanding the determinant by permutations, then differentiating one column at a time, gives \(\partial_t\det C=(\det C)\operatorname{tr}(C^{-1}D)\). On a compact positive-definite family, all the required density derivatives are bounded by a polynomial times a fixed integrable Gaussian. Consequently
\[
 \partial_t\int_{\mathcal C}f(x)p_t(x)dx
       =\int_{\mathcal C}f(x)\dot p_t(x)dx
 \tag{T4}
\]
for any bounded measurable \(f\) and fixed measurable cut set \(\mathcal C\). Polynomial growth is also allowed. There is no derivative of an indicator in (T4).

**Discharged — what integration by parts would otherwise omit.** In two scalar blocks with only \(\dot C_{12}=\dot C_{21}=k\) nonzero, differentiating the Gaussian explicitly gives \(\dot p=k\partial_x\partial_y p\). On the rectangle \(A\times B=[-p,p]\times[-q,q]\), the fundamental theorem of calculus gives
\[
 \partial_t\Pr(A\times B)=k\{p_t(p,q)-p_t(-p,q)
                                  -p_t(p,-q)+p_t(-p,-q)\}.
 \tag{T5}
\]
Dropping these four corner densities is wrong. More generally, for a differentiable \(F\), the distributional identity is
\[
 \partial_x({\bf1}_{[-p,p]}F)
 = {\bf1}_{[-p,p]}\partial_xF+F(-p)\delta_{-p}-F(p)\delta_p.
 \tag{T6}
\]
It follows by integrating against a compactly supported smooth test function and integrating on the interval. Higher derivatives have higher boundary distributions. This diagnoses the boundary term; it does not break the density formula.

**Discharged — retain precisely N(26)–(27).** For each site state \(r\), at fixed real integration variables, set
\[
 A_{r,1}=\ell_{r,1}+\Psi_{r,1}-\Xi_{r,0}\cdot\Xi_{r,1},\qquad
 A_{r,2}=\ell_{r,2}+\Psi_{r,2}-\Xi_{r,0}\cdot\Xi_{r,2}
                              -\tfrac12\Xi_{r,1}\cdot\Xi_{r,1}.
 \tag{T7}
\]
Here the coefficients, including those of the inverse-coordinate Jacobian, are the actual ones. Writing \(G_{r,2}=A_{r,2}+A_{r,1}^2/2\), the density multiplier is \(1+wA_{r,1}+w^2G_{r,2}+O(w^3)\). Multiplication by its scalar inverse series gives, for a factor \(e(v)\) fixed by these coordinates,
\[
 [w^2]\mathcal T_r[e]=\theta_{r,0}
 \{\operatorname{Cov}_r(e,A_{r,2})+\tfrac12\kappa_{3,r}(e,A_{r,1},A_{r,1})\}
 +\theta_{r,1}\operatorname{Cov}_r(e,A_{r,1})
 +\theta_{r,2}\langle e\rangle_r.
 \tag{T8}
\]
Indeed the inverse multiplier through degree two is

\(1-w\langle A_1\rangle+w^2(\langle A_1\rangle^2-\langle G_2\rangle)\).

Multiplying it out gives all four terms of the third cumulant in N(27). Here \(\theta_r=\widetilde N_r/N_r\), with \(N_r=N_{\rm good}^Z\) on the original cuts and \(\widetilde N_r\) on the replacement cuts. If \(e=e_0+we_1+w^2e_2+\cdots\), use \(e_0\) in (T8) and add \(\theta_0(\langle e_2\rangle+\operatorname{Cov}(e_1,A_1))+\theta_1\langle e_1\rangle\), suppressing the site index in this last expression. Nothing in a Gaussian interpolation sets \(\theta\) equal to one.

## 2. The finite forest formula, including positivity

**Discharged — the formula.** Let \(E_n\) be the pairs of \(n\) labels. A forest \(F\subset E_n\) has no cycle. Assign \(t_e\in[0,1]\) to its edges and set
\[
 s^F_{ii}=1,\qquad s^F_{ij}=
 \begin{cases}
 \min_{e\in\operatorname{path}_F(i,j)}t_e,&i,j\text{ connected in }F,\\
 0,&\text{otherwise}.
 \end{cases}
 \tag{T9}
\]
For a scalar function \(f\) with continuous partial derivatives through order \(n-1\) on the domain described below,
\[
 f(\mathbf1)=\sum_{F\text{ forest}}\int_{[0,1]^F}
                  (\prod_{e\in F}\partial_e)f(s^F(t))\,dt.
 \tag{T10}
\]
The empty forest contributes \(f(\mathbf0)\). It is enough that \(f\) have those derivatives on a neighbourhood of the interpolation matrices used in the following proof; it need not be defined on every point of the full edge cube.

**Discharged — proof by successive fundamental theorems of calculus.** Start with \(f(\mathbf1)=f(\mathbf0)+\int_0^1\sum_e\partial_e f(u\mathbf1)du\). After choosing distinct edges \(e_1,\ldots,e_k\) joining different current components, their parameters satisfy \(1\ge t_1\ge\cdots\ge t_k\ge0\). For the current forest, keep every connected pair at the minimum parameter on its path, and set all pairs between different components to a common \(u\in[0,t_k]\). Apply the fundamental theorem to \(\partial_{e_1}\cdots\partial_{e_k}f\) on this segment. Its value at \(u=t_k\) equals its value at \(u=0\), plus the integral of the sum of its derivatives over pairs in different components. Each such pair becomes \(e_{k+1}\), at parameter \(t_{k+1}=u\). To verify the recursion's matching endpoint, compare the forest before and after adding \(e_k\). At parameter \(t_k\), all pairs between its newly merged components have path minimum \(t_k\), and all still-disconnected pairs also have value \(t_k\). Thus the matrix is precisely the preceding segment evaluated at its integration parameter. There is no new derivative in the case of one remaining component.

Each added edge reduces the number of components, so after at most \(n-1\) steps the recursion ends. It produces all ordered forests, integrated over their ordered parameter simplexes. For a fixed forest the orderings partition its parameter cube up to equality hyperplanes of measure zero. The derivatives commute and the resulting matrix depends only on path minima. Summing the simplexes proves (T10). For \(n=1\) the formula is the identity with only the empty forest.

**Discharged — the covariance is positive at every point actually used.** For a forest \(F\), let \(Q_v\) be the label matrix with entry one when two labels are in the same component of the forest retaining edges with \(t_e\ge v\), and zero otherwise. Its diagonal is one. Then
\[
 s^F=\int_0^1 Q_v\,dv.
 \tag{T11}
\]
For coordinate blocks and any real symmetric covariance \(C\) satisfying \(\delta1\le C\le M1\), define \(C(s)_{ij}=s_{ij}C_{ij}\), with diagonal blocks unchanged. For a vector \(x\), and with \(\pi_v\) the partition into the components defining \(Q_v\),
\[
 x^TC(s^F)x
 =\int_0^1\sum_{B\in\pi_v}x_B^TC_{BB}x_B\,dv,
 \qquad \delta|x|^2\le x^TC(s^F)x\le M|x|^2.
 \tag{T12}
\]
The bounds on every principal block follow by extending \(x_B\) by zero. The intermediate segment in the proof of (T10) has the same representation, using one component containing all labels for \(0\le v\le u\), and the components of the current forest retaining edges with \(t_e\ge v\) for \(v>u\). Hence (T12) holds on those segments too. Strict positivity gives an open neighbourhood on which each necessary derivative is defined. Arbitrary independent attenuation of covariance entries need not preserve positivity; (T11), not that incorrect assertion, is the reason this interpolation works.

**Discharged — two distinct ways of retaining the product noise.** For covariance interpolation use the density \(p_{m,C(s)}/p_{0,1}\) as an insertion against the original \(\mu\). Its mean is fixed at \(m\), its block variances at \(C_{ii}\), and only off-diagonal covariances change. At \(s=1\) the insertion equals \(I_a/Z_a\); at \(s=0\) the resulting measure is a product of normalized block measures. The cuts remain fixed. This interpolation is of the normalized Gaussian obtained from (T1).

For a literal interpolation of the off-diagonal quadratic term in (T1), put \(K=R^TR\), \(h=R^Ta\), and
\[
 I_a^{\rm pr}(s,\eta)=e^{-|a|^2/2}
 \exp\left\{\sum_i h_i^T\eta_i-\tfrac12\sum_i\eta_i^TK_{ii}\eta_i
                         -\sum_{i<j}s_{ij}\eta_i^TK_{ij}\eta_j\right\}.
 \tag{T13}
\]
Its total precision with respect to Lebesgue measure is \(1+s\circ K\ge1\), by the proof of (T12) applied to \(K\ge0\). It equals \(I_a\) at \(s=1\), and retains the product noise exactly. Every derivative produces
\[
 \partial_{ij}I_a^{\rm pr}=-(\eta_i^TK_{ij}\eta_j)I_a^{\rm pr}.
 \tag{T14}
\]
Thus it too obeys (T10), with no integration by parts and no differentiability assumption on the cuts. Its covariance is \((1+s\circ K)^{-1}\); it is generally not \(s\circ C\). Confusing these two interpolations would give incorrect edges and normalizations. The constant \(e^{-|a|^2/2}\) can be placed at a distinguished root so that disconnected components factor at zero intercomponent coupling. Normalizing (T13) brings determinant and mean derivatives back into the scores. The finite identity by itself does not bound their inverse series.

In particular, for a fixed measurable factor \(F_0(\eta)\) of at most polynomial growth, the literal off-diagonal-insertion formula is
\[
 \int_{\mathcal C}F_0 I_a\,d\mu
 =\sum_{F\ {\rm forest}}\int_{[0,1]^F}\!dt
    \int_{\mathcal C}F_0 I_a^{\rm pr}(s^F(t),\eta)
              \prod_{ij\in F}(-\eta_i^TK_{ij}\eta_j)\,d\mu.
 \tag{FPR}
\]
This follows by applying (T10) under the integral and then (T14). Since the total precision is at least one and \(h\) is fixed, completing the square bounds all its finitely many differentiated integrands by a polynomial times an integrable Gaussian. That proves the interchange. It also applies to bounded factors supported on the fixed chart cuts. Factorization over forest components requires \(F_0\) to factor over those components; it is not asserted for an arbitrary interacting \(F_0\).

## 3. An all-order bound with sharp factors

**Discharged — derivative bound.** Suppose disjoint coordinate blocks carry bounded measurable functions \(f_i\). Let
\[
 F(s)=E_{m,C(s)}\prod_{i=1}^n f_i(X_i),\qquad
 k_{ij}=\delta^{-1}\sum_{a\in i,b\in j}|C_{ab}|,\qquad
 \delta1\le C\le1.
 \tag{T15}
\]
For a forest \(T\), let \(d_i\) be the degree of vertex \(i\), and write \(\partial_T=\prod_{e\in T}\partial_e\). Uniformly at all the positive interpolation matrices of Section 2,
\[
 |\partial_TF(s)|\le
 \prod_{ij\in T} k_{ij}\ \prod_i\sqrt{d_i!}\ \prod_i\|f_i\|_\infty.
 \tag{T16}
\]
The block entry sum is intentional: replacing it by an operator norm without accounting for directions would not prove this estimate.

**Discharged — proof, without differentiating a cut.** Direct differentiation of a Gaussian density also gives
\[
 \partial_{s_{ij}}p_{m,C(s)}
       =\sum_{a\in i,b\in j}C_{ab}\partial_{x_a}\partial_{x_b}p_{m,C(s)}.
 \tag{T17}
\]
To check it, \(\partial_a\partial_b p=((C(s)^{-1}(x-m))_a(C(s)^{-1}(x-m))_b-(C(s)^{-1})_{ab})p\); summing over the two symmetric off-diagonal blocks reproduces (T3), including its factor \(1/2\). Repetition gives a spatial derivative of total order \(2|T|\) for each choice of endpoint coordinates.

Represent \(X=m+Z+\sqrt\delta\,Y\), with \(Y\) independent standard Gaussian coordinates and \(Z\) Gaussian of covariance \(C(s)-\delta1\ge0\). A positive semidefinite Gaussian, including a singular one, is defined by diagonalizing its covariance, multiplying independent scalar normals by the square roots of its nonnegative eigenvalues and rotating back. Put every spatial derivative on the density of \(\sqrt\delta Y\), before integrating against the \(f_i\). For coordinate \(a\) used \(\nu_a\) times this produces \(\delta^{-\nu_a/2}H_{\nu_a}(Y_a)\), up to a sign.

The identity \(E H_j(Y)H_k(Y)=\mathbf1_{j=k}j!\) used here has a short derivation. Define \(H_j\) by \(e^{ty-t^2/2}=\sum_j H_j(y)t^j/j!\). Completing a square gives
\[
 E e^{tY-t^2/2}e^{uY-u^2/2}=e^{tu}.
\]
Differentiate at zero, justified by Gaussian domination on bounded parameter sets, and compare coefficients. Differentiating the scalar Gaussian density gives the same polynomials, since its translate has this generating function. Independence of the \(Y_a\), followed by Cauchy–Schwarz, bounds each endpoint-coordinate term, before multiplying by its edge entries, by
\[
 \delta^{-|T|}\Bigl(\prod_a\nu_a!\Bigr)^{1/2}
 \left(E_{m,C(s)}\prod_i|f_i(X_i)|^2\right)^{1/2}.
 \tag{T18}
\]
For each block, \(\prod_{a\in i}\nu_a!\le(\sum_{a\in i}\nu_a)!=d_i!\), because the corresponding multinomial coefficient is a positive integer. Sum the endpoint choices absolutely and use the suprema to prove (T16). This proof is for the original fixed cuts, not for a smoothed approximation to them.

**Discharged — integrated smallness for many forbidden cuts, when there is a margin.** Suppose a subset \(B\) of the vertices has
\[
 |f_i(x_i)|\le a_i\mathbf1_{\max_{a\in i}|x_a|>p_i},\quad
 |m_a|\le p_i/2\ (a\in i),\quad q_i=\dim i.
 \tag{T19}
\]
At the other vertices assume \(|f_i|\le a_i\). Then (T16) improves to
\[
 |\partial_TF(s)|\le
 \prod_{ij\in T}k_{ij}\prod_i\sqrt{d_i!}\prod_i a_i
                 \prod_{i\in B}(2q_i)^{1/2}e^{-p_i^2/16}.
 \tag{T20}
\]
Here is a joint-tail proof, avoiding a volume-dependent union bound. For every bad block choose an offending coordinate and its sign. Put \(v_a=\pm p_i/2\) in that coordinate and zero elsewhere. On the indicated joint event,
\[
 v\cdot(X-m)\ge\sum_{i\in B}p_i^2/4.
\]
Gaussian square completion and \(C(s)\le1\) give \(Ee^{v\cdot(X-m)}\le e^{\sum p_i^2/8}\). Markov's inequality bounds the event by \(e^{-\sum p_i^2/8}\). There are at most \(\prod_{i\in B}2q_i\) choices. Insert this joint probability into (T18). Its square root is precisely the last product in (T20). This proves an all-order cut-inclusive estimate in the auxiliary setting.

**Discharged — a growing root can be included.** If vertex \(0\) instead carries a measurable \(e(X_0)\) with finite fourth moment, a second Cauchy–Schwarz inequality gives
\[
 |\partial_T E(e(X_0)\prod_{i\ne0}f_i(X_i))|
 \le \prod_{ij\in T}k_{ij}\prod_i\sqrt{d_i!}
 (E|e(X_0)|^4)^{1/4}\prod_{i\ne0}a_i
                 \prod_{i\in B}(2q_i)^{1/4}e^{-p_i^2/32}.
 \tag{T21}
\]
Indeed \(E(|e|^2\mathbf1_{\text{joint bad}})\le(E|e|^4)^{1/2}\Pr(\text{joint bad})^{1/2}\), before the square root in (T18). The fourth moment is under the interpolated law, so a uniform bound on it is still required. This is not a supremum estimate for the growing old factor.

**Discharged — connected functions are trees in this setting.** Apply (T10) to \(E\prod f_i\). At \(s^F\), the Gaussian and its edge derivatives factor over forest components. Thus the moment is the sum over set partitions of products of the connected-tree integrals on their blocks. The same relation holds for the cumulants of N(19). To see this without a combinatorial theorem, introduce commuting variables \(z_i\) with \(z_i^2=0\), expand the formal logarithm of \(1+\sum_{A\ne\varnothing}M(A)z^A\), and then exponentiate it. The coefficient of \(z^A\) in the exponential partitions \(A\) into unordered nonempty blocks: its \(1/k!\) cancels their \(k!\) orders. The partition relation determines each connected term by induction on \(|A|\), since the one-block term has coefficient one. Hence the cumulant equals the sum of tree integrals. This is a finite identity even with sharp cuts.

**Unchecked — the disjointness restriction matters.** Two interaction supports in N(25) can overlap. Copying their shared coordinate into two distinct blocks produces a singular covariance when the copies are identified, losing the uniform \(\delta>0\). One must first group overlap-connected interactions, or supply a joint expansion with overlap edges. The theorem above is not by itself an all-order theorem for the interacting chart. It does settle the objection that a sharp indicator makes the finite Gaussian forest formula meaningless.

## 4. Entropy and the actual smallness parameter

**Discharged — an explicit tree sum.** Suppose the integrated vertex bounds are \(a_i\ge0\), and let
\[
 Q=\sup_i\sum_{j\ne i}k_{ij}a_j.
 \tag{T22}
\]
For a fixed root position, sum all other positions of a labelled tree, relaxing distinctness only in this upper bound. Remove non-root leaves successively. Each leaf sum costs at most \(Q\). Thus a tree with \(n\) vertices costs at most \(a_0Q^{n-1}\prod_i\sqrt{d_i!}\), with the root moment bound substituted when using (T21).

The following count includes degree growth:
\[
 \sum_{T\text{ on }n\text{ labels}}\prod_i d_i!
       =(n-2)!\binom{3n-3}{n-2}\quad(n\ge2).
 \tag{T23}
\]
Repeatedly remove the smallest labelled leaf and record its neighbour, stopping at two labels. The word has length \(n-2\); label \(i\) occurs \(d_i-1\) times. Conversely, join the smallest remaining label absent from the remaining word to its first letter, delete that letter and label, and finally join the last two labels. This inverts the removal procedure. Thus the number with \(d_i=k_i+1\) is \((n-2)!/\prod_i k_i!\). Multiplying by \(\prod_i d_i!\), sum \((n-2)!\prod_i(k_i+1)\) over \(\sum k_i=n-2\). Since \(\sum_{k\ge0}(k+1)x^k=(1-x)^{-2}\), multiplication of \(2n\) geometric series gives (T23).

Use \(\sqrt{d_i!}\le d_i!\), divide by the rooted-series factorial \((n-1)!\), and bound a binomial coefficient by \(2^{3n-3}\). Then
\[
 \sum_{n\ge1}\frac1{(n-1)!}
 \sum_{\text{positions, trees}}\text{the majorant in (T16)}
       \le \frac{a_0}{1-8Q},\qquad 8Q<1.
 \tag{T24}
\]
The \(n=1\) term is \(a_0\). This supplies a concrete sufficient number, \(8Q\); “exponential decay” alone does not supply its smallness.

**Discharged — comparison with the volume loss.** N(25) leaves \(S^{n-1}\) after one attachment, where \(S\) can grow like region size times the activity. In (T24) it is replaced by \(Q^{n-1}\), independent of the region. If shell \(r\) has at most \(B_0(r+1)^4\) sites, an edge bound \(k_{ij}\le K e^{-\lambda d(i,j)}\), with a tree weight \(e^{\sigma d}\), gives
\[
 Q_\sigma\le {24B_0Ka_*\over(1-e^{-(\lambda-\sigma)})^5},
 \qquad a_*:=\sup_i a_i,\quad\lambda>\sigma.
 \tag{T25}
\]
Use \((r+1)^4\le24\binom{r+4}{4}\) and multiply five geometric series. With a minimum positive distance one may omit the \(r=0\) term. If \(\lambda\le\sigma\), this shell majorant is not summable over unbounded regions. Failure of that test is not a lower bound on a true coefficient.

**Implication — which available factors become small.** As a premise, I:640–650 supplies a summable interaction activity of size
\[
 H_0=C(L,M,\epsilon_1,\alpha)(gp^3+C_Egp),\qquad
 p=(\log(1/g))^{p_0},\quad p_0>2.
 \tag{T26}
\]
If overlap grouping and coefficient norms give \(a_*\le C_*H_0\), (T25) gives the explicit sufficient test
\[
 8Q_\sigma\le
 {192B_0KC_*H_0\over(1-e^{-(\lambda-\sigma)})^5}<1.
 \tag{T27}
\]
At fixed \(L\), fixed positive rate gap and fixed constants, this is small for sufficiently small \(g\). For forbidden cuts satisfying (T19), substitute \(a_*=(2q_*)^{1/2}e^{-p_*^2/16}\), or \((2q_*)^{1/4}e^{-p_*^2/32}\) with a growing root. These numbers also become small and include tree entropy.

**Discharged — neither Gaussian edge has a factor \(g\).** For covariance interpolation the actual edge is
\[
 k_{ij}={1\over\delta}\sum_{a\in i,b\in j}|(R_i^TVR_j)_{ab}|.
 \tag{T28}
\]
For precision interpolation it is \(R_i^TR_j\) multiplied by endpoint-noise moments, as (T14) states. I:699–711 splits the covariance with the fixed factor \(1/2\): \(G_1=2^{-1/2}C_1^{1/2}(1-\Delta)^{1/2}\), while the local part is \(2^{-1/2}P\). Forming \(R=\Sigma_0^{-1/2}U\) cancels their common scale; neither contains a spare \(g\). The source explicitly imposes no smallness on the real spectator amplitude. Its decaying kernel is not asserted to be a small perturbation of product noise in this normalization.

**Discharged — hand diagnostic, not an SU(2) counterexample.** The abstract quadratic choice \(R=(1,1)\) has
\[
 C=\begin{pmatrix}2/3&-1/3\\-1/3&2/3\end{pmatrix},\quad
 \delta=1/3,\quad k_{12}=1.
 \tag{T29}
\]
For cut factors bounded only by one, \(8Q=8\) on these two blocks. For \(R=(r,r)\), (T28) gives \(k_{12}=r^2\). The finite forest identity still holds. Thus positivity, \(C\le1\), and decay away from a finite root do not imply \(8Q<1\). This is not a realization of the SU(2) chart and does not refute (CN). For the actual chart the number is (T28) with its actual matrices; the supplied upper bounds do not certify its smallness for near cuts.

**Discharged — the dimensionless precision coupling is not small either.** In (FPR) the natural local precision is \(D_i=1+K_{ii}\), so the off-diagonal matrix measured in its two local Gaussian forms is
\[
 \widehat K_{ij}=D_i^{-1/2}K_{ij}D_j^{-1/2}.
 \tag{P-edge}
\]
For the two scalar columns \(R=(r,r)\), this is \(r^2/(1+r^2)\), already \(1/2\) at \(r=1\), and arbitrarily close to one as \(r\) increases. Endpoint means measured in these forms are \(D_i^{-1/2}h_i\), which can grow proportionally to \(p\). These exact numbers give neither a vanishing coupling nor small endpoint moments. Formula (T24) is the derivative majorant for covariance interpolation; applying it unchanged to the precision edges of (FPR) would be unjustified.

**Implication — anchoring still has to be preserved.** The zero-coupling covariance reference has means \(m_i\) and variances \(C_{ii}\); it is not the original product law with zero means and unit variances. Thus subtraction of the original normalizer in N(25) must also subtract its diagonal and mean changes, not just connected off-diagonal trees. For a single block, the deletion estimate N(5) gives a bound \((3|a|/2+\sqrt2)\|R_i\|_{\rm HS}\|f_i\|_\infty\), which attaches that change to the observed set. It has a polynomial cost in \(p\). The source proves that estimate for the quadratic insertion. Preserving these root attachments after overlap grouping, nonlinear scores and cut division is an additional use to be justified, not a consequence of independence at \(s=0\).

## 5. The inverse normalizer can be included when the margins hold

**Discharged — a genuine cut gas, beyond a formal connected coefficient.** Continue with the disjoint Gaussian blocks, no nonlinear interactions, and assume (T19) at every block. Put
\[
 b_i=\mathbf1_{\max_{a\in i}|X_a|>p_i},\quad \chi_i=1-b_i,\quad
 z_i=E_{m_i,C_{ii}}\chi_i,\quad
 u_i=(2q_i)^{1/2}e^{-p_i^2/16}/z_i.
 \tag{T30}
\]
Suppose \(2q_i e^{-p_i^2/8}\le1/2\). Then \(z_i\ge1/2\), by the proof of (T20). Apply the forest formula to \(E\prod_{i\in A}\chi_i\). Components of size one give \(z_i\). For a tree on \(B\), \(|B|\ge2\), replace each \(\chi_i\) in its derivative integrand by \(-b_i\). This is exact: a term with one factor replaced by the constant one has no dependence on any covariance entry incident to that label after marginalization, and the tree derivative contains such an entry. Its derivative is zero.

Dividing by \(\prod_{i\in A}z_i\) therefore gives the exact finite gas
\[
 {E\prod_{i\in A}\chi_i\over\prod_{i\in A}z_i}
 =\Xi(A)=\sum_{\substack{\{B_1,\ldots,B_k\}\\
           B_j\subset A,\ |B_j|\ge2,\ B_j\text{ disjoint}}}
                \prod_j v(B_j),
 \tag{T31}
\]
where \(v(B)\) is the connected-tree integral divided by \(\prod_{i\in B}z_i\). By (T20),
\[
 |v(B)|\le\sum_{T\text{ on }B}\prod_{ij\in T}k_{ij}
                                  \prod_{i\in B}u_i\sqrt{d_i!}.
 \tag{T32}
\]
These are integrated activities, not suprema of indicators.

**Discharged — the inverse series and a quantitative zero-free test.** Assume
\[
 u_*:=\sup_i u_i\le1,\qquad Q_u:=\sup_i\sum_{j\ne i}k_{ij}u_j\le1/128.
 \tag{T33}
\]
The counting proof of (T24), with \(2u_j\) at every non-root vertex, gives
\[
 \sup_i\sum_{B\ni i}|v(B)|\,2^{|B|-1}
 \le u_*{16Q_u\over1-16Q_u}\le1/7.
 \tag{T34}
\]
The equality between sums over distinct sets and ordered labels divided by \((n-1)!\) accounts for all positions in this assertion; allowing repetitions was only an upper bound in its proof.

Here is a complete inverse argument. Removing \(i\) in the gas (T31) gives
\[
 {\Xi(A)\over\Xi(A\setminus i)}
 =1+\sum_{\substack{B\subset A\\i\in B}}v(B)
                {\Xi(A\setminus B)\over\Xi(A\setminus i)}.
 \tag{T35}
\]
Induct on \(|A|\), starting with \(\Xi(\varnothing)=1\). Remove the \(|B|-1\) other elements of \(B\) one at a time in the quotient on the right. If the inverse of every smaller single-removal ratio has modulus at most two, that quotient costs at most \(2^{|B|-1}\). Thus (T34) places (T35) within \(1/7\) of one. It is nonzero, and its inverse is the convergent geometric series with norm at most \(7/6<2\). This closes the induction for arbitrary finite \(A\). The proof also works in any unital complete submultiplicative coefficient algebra, provided the bound (T34) holds in that algebra. It then proves convergence of the inverse series, not merely scalar nonvanishing. No bound independent of volume is claimed for the inverse of the entire extensive product \(\prod_i z_i\Xi(A)\); connected ratios are the quantities that stay controlled.

**Implication — the actual numerical test for far cuts.** If \(k_{ij}\le K e^{-\lambda d(i,j)}\), \(q_i\le q_*\), and \(p_i\ge p_*\) with the mean margin, a sufficient version of (T33) with rate weight \(\sigma\) is
\[
 {48B_0K(2q_*)^{1/2}e^{-p_*^2/16}
       \over(1-e^{-(\lambda-\sigma)})^5}\le {1\over128},
 \qquad
 2(2q_*)^{1/2}e^{-p_*^2/16}\le1.
 \tag{T36}
\]
The factor two is the proven \(z_i^{-1}\le2\). At fixed scale these inequalities eventually hold as \(g\) decreases. This establishes the proposed cure, including inverse normalization, for the Gaussian cut gas with margins. It does not establish those margins for the conditional near cuts.

**Discharged — a limitation of conditioning before summing.** From (T2), \(|m_i|\le\|R_i\||a|\), while the replacement observation permits \(|a|\le C(L)p\). No supplied estimate forces \(|m_i|\le p_i/2\) for all nearby cut coordinates. For example \(R=(1,1)\), \(a=6p\) gives \(m_1=m_2=2p\); the event \(|X_i|\le p\) is then a lower tail rather than a high-probability cut. This diagnoses the missing premise of (T33), not an admissible SU(2) counterexample. Dividing by its small \(z_i\) invalidates that test. The following argument shows that this particular loss can be avoided in the quadratic problem by retaining the observed coordinate as a root.

**Discharged — a polynomial enlargement alone is insufficient for the desired constant.** Suppose the column bound is \(\|R_i\|\le B e^{-\lambda d(i,Y)}\). To make the mean margin for cuts \(p_i=c_i p\), with \(|a|\le C_a p\), it is enough that \(B C_a e^{-\lambda d}\le c_i/2\); this radius is independent of \(g\), when \(C_a,c_i\) are uniform. Thus it would be incorrect to claim that failure of the margin necessarily creates a \(\log(1/g)\) core. Nevertheless this can leave a fixed, scale-dependent collection of strong cut blocks. Bounding their normalized integrals separately by \(1/\prod z_i\) can cost \(e^{C(L)p^2}\). It cannot be paid by a power of \(p\) or by \(P_P\). No such reciprocal loss is a counterexample to the true normalized integral.

**Discharged — keeping the observation integrated repairs this Gaussian loss.** Let \(a\) now be integrated, and let \(q=\dim a\). The joint density
\[
 (2\pi)^{-(q+N)/2}
       e^{-|\eta|^2/2-|a-R\eta|^2/2}\,da\,d\eta
 \tag{J1}
\]
has total mass one: integrate the translate \(a-R\eta\) first. Its covariance is
\[
 C^{\rm joint}=
 \begin{pmatrix}1+RR^T&R\\R^T&1\end{pmatrix}
 =T T^T,\qquad
 T=\begin{pmatrix}1&R\\0&1\end{pmatrix}.
 \tag{J2}
\]
Since \(\|T\|,\|T^{-1}\|\le1+\|R\|\), it lies between
\(\delta_*1\) and \(\delta_*^{-1}1\), where
\(\delta_*=(1+\|R\|)^{-2}\). This proves positivity without conditioning on a possibly large \(a\). It is an identity in the same fixed coordinates and retains the original product noise.

Treat all components of \(a\) as the single root block 0, and the spectator blocks as the other vertices. Apply covariance interpolation to (J2). Its only off-diagonal edges are \(0i\), of matrix \(R_i\). Every interpolant has exactly the same root marginal, and its entire spectator marginal remains the original product standard Gaussian. Keep the root cut inside a root factor \(e_0(a)\); no derivative or smallness assumption on that cut is needed. Put \(z_i=E\chi_i\ge1/2\) for the spectator cuts, and
\[
 k_{0i}^*=\delta_*^{-1}\sum_{\alpha\in0,b\in i}|(R_i)_{\alpha b}|,
 \qquad
 v_i={(2q_i)^{1/4}e^{-p_i^2/8}\over z_i},\qquad
 L_*=\sum_i k_{0i}^*v_i,\quad
 G_*=(E|e_0(a)|^4)^{1/4}.
 \tag{J3}
\]
The moment in \(G_*\) is independent of the forest parameters. The tail exponent is \(1/8\), because each spectator is centered standard Gaussian: its joint bad probability is at most \(\prod_i2q_i e^{-p_i^2/2}\), and the proof of (T21) takes its fourth root. The derivative proof (T18) only needs a positive lower covariance bound, so it applies with \(\delta_*\); no upper bound on the root covariance is needed for this spectator-tail estimate. For a Euclidean block cut of radius \(p_i^{\rm ball}\), the same argument uses the component threshold \(p_i=p_i^{\rm ball}/\sqrt{q_i}\), since exceeding the ball implies that some component exceeds that threshold.

In a nonzero forest component containing the root, all its edges are \(0i\): it is a star. Every other component is a singleton. Replace the spectator cut by its forbidden complement at each star leaf as in (T31). Divide by \(\prod_i z_i\). The component with \(n\) leaves has degree factor \(\sqrt{n!}\); summing distinct leaves is bounded by \(L_*^n/n!\). Thus the full, absolute forest sum satisfies
\[
 {|\ E_{C^{\rm joint}}e_0(a)\prod_i\chi_i\ |\over\prod_i z_i}
 \ \le\ \text{absolute forest sum}
 \ \le\ G_*\sum_{n\ge0}{L_*^n\over\sqrt{n!}}
 \ \le\ \sqrt2\,G_*e^{L_*^2}.
 \tag{J4}
\]
For the last inequality, write the summand as
\(2^{-n/2}(\sqrt2L_*)^n/\sqrt{n!}\) and apply Cauchy–Schwarz to the two series. Their squared sums are \(2\) and \(e^{2L_*^2}\). This includes every cut order in this quadratic rooted numerator. More explicitly, if \(q_i\le q_*\), \(p_i\ge p_*\), and \(K_1=\sum_i\sum_{\alpha,b}|(R_i)_{\alpha b}|<\infty\), then
\[
 L_*\le 2\delta_*^{-1}(2q_*)^{1/4}K_1e^{-p_*^2/8};
 \quad
 4\delta_*^{-1}(2q_*)^{1/4}K_1e^{-p_*^2/8}\le1
       \ \Longrightarrow\ \text{(J4)}\le3G_*.
 \tag{J5}
\]
Indeed the condition gives \(L_*\le1/2\), and
\(\sqrt2e^{1/4}\le2/(1-1/4)=8/3<3\), by the power series for the exponential. With a summable root kernel and \(p_i\) proportional to \(p\), this is small after choosing \(g\). With spatial weights the same estimate replaces \(K_1\) by its weighted row sum, using the positive gap in (T42).

**Unchecked — what (J4) does and does not settle.** This is a useful repair, not a claim that all near-root cuts are an obstruction. The weak edge parameter for the Gaussian cut leaves is the explicit \(k_{0i}^*v_i\), not \(k_{0i}^*\) alone. The star series even converges for every finite \(L_*\); arbitrary interaction trees still need a test such as (T27). Formula (J4) gives neither the inverse of the actual original-cut normalizer nor the ratio between its domain and the replacement domain. After the nonlinear inverse-coordinate map, (T7), (T8) and (T52) remain to be estimated. No all-order small-activity representation of those particular boundary terms has been established by (J4).

## 6. The two proposed boundary repairs

**Discharged — interpolation invisible to the cuts is usually incomplete.** Let the cuts read linear coordinates \(L_\beta X\), and let \(U=\bigcap_\beta\ker L_\beta\). A covariance interpolation whose spatial derivative endpoints are all invisible to the cuts can vary only its \(U\times U\) part. It cannot remove a covariance edge between two cut-visible blocks. With cuts on both coordinates in (T29), \(U=0\) and this proposal performs no interpolation at all. More generally, holding the visible marginal fixed retains its non-product cut probability. Conditional integration over \(U\) does not turn that marginal into a product. The source's good-sector spectator cuts at \(p_4\), and its near cuts at \(p_3\), are cut-visible variables. Consequently the proposal can handle an uncut sector, but does not provide the missing cut attachments in (T8). Keeping a boundary derivative on the density as in Section 3 is the available exact alternative.

**Discharged — a smooth outward cut.** There is a smooth scalar function \(\psi\) with \(0\le\psi\le1\), \(\psi=1\) on \((-\infty,0]\) and \(\psi=0\) on \([1,\infty)\). On \(0<u<1\), define \(\psi(u)=\int_u^1 b(t)dt/\int_0^1 b(t)dt\), where \(b(t)=e^{-1/(t(1-t))}\) on \(0<t<1\), extended by zero. Repeated differentiation of \(b\) is a rational function times \(b\), tending to zero at either endpoint because \(x^{-N}e^{-1/x}\to0\) for every \(N\). The latter limit follows by bounding \(e^{1/(2x)}\) below by any chosen term of its positive power series. Put
\[
 \chi_{p,\epsilon}(x)=\psi((|x|-p)/\epsilon),\qquad 0<\epsilon\le p.
 \tag{T37}
\]
It is smooth also at zero because it is constant there, and
\[
 0\le\chi_{p,\epsilon}-\mathbf1_{[-p,p]}
       \le\mathbf1_{|x|>p},\qquad
 \|\chi_{p,\epsilon}^{(r)}\|_\infty\le D_r\epsilon^{-r},
 \quad D_r:=\|\psi^{(r)}\|_\infty.
 \tag{T38}
\]
This is outward smoothing, within the small-field range \(2p\).

**Implication — the rate supplied by (CUT).** Using precisely the real shifted-Gaussian bound supplied by I:(CUT), item 3, the one-block integrated smoothing error is at most
\[
 (ML)^4 e^{-p^2/9}.
 \tag{T39}
\]
There is no need to weaken this particular exponent to \(1/16\): the error is supported outside the original threshold \(p\). Formula (T39) is an implication of that source estimate, with its real mean and Gaussian-margin hypotheses; it is not asserted for the conditional law when those hypotheses fail. A spectator threshold must use its own corresponding tail bound, not silently the white-noise threshold \(p\).

**Discharged — what smoothing does not buy.** For \(N\) cut blocks,
\[
 \left|\prod_i\chi_{p_i,\epsilon_i}-\prod_i\mathbf1_{[-p_i,p_i]}\right|
 \le\sum_i\mathbf1_{|X_i|>p_i},
 \tag{T40}
\]
by telescoping products of numbers in \([0,1]\). Combining only (T39) with this identity costs \(N(ML)^4e^{-p^2/9}\). It is not uniform over arbitrary regions. A connected cancellation can improve it, but has to be proved after normalization.

Putting derivatives on the smoothed cut instead of the density costs \(D_{d_i}\epsilon_i^{-d_i}\) at a vertex. With \(\epsilon_i=\epsilon\), the edge cost includes \(\epsilon^{-2}\), since \(\sum_i d_i=2(n-1)\). No all-order bound on the \(D_r\) adequate for the tree series follows from smoothness. Taking a broad smoothing interval can reduce the powers of \(\epsilon^{-1}\), but does not remove its error or supply those all-order bounds. Section 3 avoids this derivative loss exactly. Smoothing alone proves neither a connected coefficient bound for its error nor a bound on the coefficient series of the original cut ratio. Small real probability is not an estimate of an absolute Taylor series.

## 7. Rates, growth and the continuation disc

**Implication — rate accounting with the source's units.** I:240 and I:709 give the slow spectator rate
\[
 s_P={1\over2\rho_P}\quad\hbox{per fine link},\qquad
 \lambda=L s_P={\kappa_G\over M}\quad\hbox{per coarse link},\qquad
 \kappa_G\ge4\log L.
 \tag{T41}
\]
The coefficient weight in (CN) has rate
\[
 \sigma=c_3={\kappa_G\over C_{\rm rate}M^4},\qquad
 \lambda-\sigma={\kappa_G\over M}
                    \left(1-{1\over C_{\rm rate}M^3}\right)>0
 \tag{T42}
\]
once \(C_{\rm rate}M^3>1\). Thus this weight does not exhaust the slow Gaussian rate. A kernel crossing a coarse distance \(r=A\log(1/g)\) leaves
\[
 e^{-(\lambda-\sigma)r}=g^{A(\lambda-\sigma)}.
 \tag{T43}
\]
If a bound loses a fixed power \(g^{-b}\), it needs \(A(\lambda-\sigma)>b\); the positivity of the rate gap alone is insufficient. If it loses only \(p^b\), every fixed \(A>0\) suffices. The available far-site threshold cannot be increased after the fact merely to make this inequality true.

**Discharged — the two-leg root edge and its number.** If, at a fixed root point \(y\),
\[
 b_i:=\sqrt{q_i}\|R_i\|_{\rm HS}\le B e^{-\lambda d(i,y)},
\]
then Cauchy–Schwarz on matrix entries gives
\[
 k_{ij}\le\delta^{-1}b_i b_j,\qquad
 \sup_i\sum_j e^{\sigma d(i,j)}k_{ij}a_j
 \le {24B_0B^2a_*\over\delta(1-e^{-(\lambda-\sigma)})^5}.
 \tag{T44}
\]
For the first inequality use \(\|V\|\le1\), the product bound for Hilbert–Schmidt norms, and the fact that a \(q_i\)-by-\(q_j\) matrix has entry sum at most \(\sqrt{q_iq_j}\) times its Hilbert–Schmidt norm. For the second use \(d(i,j)\le d(i,y)+d(j,y)\) and the shell calculation of (T25). For an extended root, this estimate requires a corresponding root-column bound with its explicit root-size constant; it is not asserted with a size-independent \(B\) automatically.

The certified tree test from these data is \(192B_0B^2a_*/[\delta(1-e^{-(\lambda-\sigma)})^5]<1\), or the stricter cut-gas test (T36). With \(a_*=H_0\) or a margin-qualified tail it is small after choosing \(g\). With \(a_*=1\) it contains no parameter tending to zero with \(g\). A large rate per cube only makes sufficiently separated cubes weakly coupled; it does not separate coordinates across a shared cube face. Grouping the finitely many strongly coupled blocks is possible in principle, but it changes the root integral that must satisfy (T8).

**Discharged — the precision version has a worse naive cut bound.** On coordinate cuts \(|\eta_a|\le p_i\), (T14) has the supremum bound
\[
 |\eta_i^TK_{ij}\eta_j|
       \le p_i p_j\sum_{a\in i,b\in j}|K_{ab}|.
 \tag{T45}
\]
For \(p_i\) proportional to \(p\), this grows as \(p^2\) on any fixed nonzero edge. It therefore cannot serve as a uniformly small coupling per edge for the cut-only expansion. This is failure of a particular supremum majorant, not divergence of the integrated tree term: Gaussian integration can greatly improve (T45).

**Implication — the old factor's moment can pay its growth, but a cut reciprocal cannot.** Suppose a centered real Gaussian reference for the curvature noise has component variances at most \(v_0>0\), and shell \(r\) outside its root has at most \(B_0N(r+1)^4\) components, \(N=\operatorname{Vol}(Z)\ge2\). Set \(U=\sup_x e^{-\alpha d(x,Z)/2}|X_x|\), with \(\alpha>0\). For \(u^2\ge2v_0\), a scalar exponential Markov bound and a union over these shells give
\[
 \Pr(U>u)\le C_\alpha N e^{-u^2/(4v_0)},\qquad
 C_\alpha={48B_0e^{-1/2}\over(1-e^{-\alpha/2})^5}.
 \tag{T46}
\]
Indeed split \(e^{-u^2e^{\alpha r}/(2v_0)}\) into two equal factors, bound the first by \(e^{-u^2/(4v_0)}\), and the second by \(e^{-e^{\alpha r}/2}\le e^{-1/2}e^{-\alpha r/2}\). Sum by (T25). Integrating \(12u^{11}\min(1,C_\alpha N e^{-u^2/(4v_0)})\) proves
\[
 (EU^{12})^{1/12}\le C(v_0,\alpha,B_0)
                                  \sqrt{\log(eN)}.
 \tag{T47}
\]
For an explicit finite constant, split at \(u_0^2=4v_0\log(\max(e,C_\alpha N))\). Above it, set \(t=u^2/(4v_0)\); five integrations by parts give \(e^{-t_0}\sum_{j=0}^{5}5!t_0^j/j!\) for \(\int_{t_0}^{\infty}t^5e^{-t}dt\). This bounds the twelfth moment by a fixed multiple of \(v_0^6\log(\max(e,C_\alpha N))^6\), proving (T47).

If \(t_Y\le c+N^{1/2}U\) and \(|e|\le cc_j\omega_P(t_Y^2+t_Y^3)\), this yields
\[
 (E|e|^4)^{1/4}\le C\,cc_j\omega_P
                         N^{3/2}(\log N)^{3/2}
                       =C\,cc_j\omega_P P_P.
 \tag{T48}
\]
Insert this moment in (T21), not the supremum \(O(g^{-3})\). This proves the asserted comparison under the stated Gaussian variance and mean premises, and introduces no new factorial with the tree order. The actual interacting, cut-normalized measure is not this reference. In particular an unproved loss \(e^{C(L)p^2}\) from its core normalization cannot be absorbed into (T48). Even a polynomial-in-\(p\) bound at each fixed observation would not by itself give (T48); the observed Gaussian must still be integrated.

**Discharged — the error rates beat fixed powers, if they are obtained in the required norm.** Put \(x=\log(1/g)\). For fixed positive \(c\) and finite \(b,N_0\),
\[
 g^{-b}p^{N_0}e^{-cp^2}
   =\exp\{bx+N_0p_0\log x-cx^{2p_0}\}\longrightarrow0.
 \tag{T49}
\]
For sufficiently large \(x\), both positive terms are at most \(cx^{2p_0}/4\), since \(2p_0>1\). The same argument beats a possible \(\exp(Cr_2^4)\) count when \(r_2=O(x)\) and \(p_0>2\). Thus a cut tail at the rate in (CUT) has ample numerical strength against the specified distance and a fixed polynomial growth loss. What is missing is the connected coefficient estimate carrying that tail, not a comparison of these scalar rates.

**Gap — extending the bounds to the whole disc.** All positivity and probability arguments above use real \(a,R,C\). At complex \(\zeta\) there is no positive conditional Gaussian to which (T19) can simply be applied. One can use a real reference and expand the complex change. For deterministic mean and matrix changes, N(9)–(12) prove the sufficient coefficient condition \(\beta\le1/64\), including an inverse normalizing series of norm at most \((1-12\beta)^{-1}\). That is useful only if it is verified uniformly at the forest interpolants and with the prescribed site/field weights.

The actual changes in \(\Xi\) depend on the integration variables, and (T7) includes \(\ell_1,\ell_2,\Psi_1,\Psi_2\). They are not those deterministic Gaussian perturbations. Neither the real cut estimate (T39) nor the real nonvanishing in (T35) establishes the algebra-valued bounds for these changes on \(|\zeta|\le c/t_\#\). The proof of (T35) shows exactly how the inverse series would be controlled once such bounds were supplied; it does not supply them. This distinction is material even for (15), because (T8) contains the cut-ratio derivatives as well as the connected scores.

## 8. A strictly smaller stopping inequality: one boundary coefficient

**Discharged — isolate the boundary contribution before asking for another all-order estimate.** Fix the one real point
\[
 \zeta_{\rm r}:=\min\{1,c_{\rm disc}/(2t_\#)\}>0
\]
of the required disc; \(c_{\rm disc}\) is its constant denoted \(c\) in (CN), distinguished here from the link \(c\). Fix one allowed field variable \(w=w_c\) and one allowed site \(S\), with its two original states \(r=0,1\). All other field variables are zero. The reference fields and radii are fixed as in the original site difference, not chosen anew in each state. We avoid \(\zeta=0\), where a scaled near variable would disappear identically. Use the actual integrals at this real point, not their quadratic truncations:
\[
 N_r(w)=\sum_{k\ge0}n_{r,k}w^k=N_{\rm good}^Z(W_r(w)),\qquad
 \widetilde N_r(w)-N_r(w)=\sum_{k\ge0}d_{r,k}w^k.
 \tag{T50}
\]
The replacement cuts and the original cuts are exactly those of N(27). At \(w=0,\zeta=\zeta_{\rm r}\), \(n_{r,0}>0\) by the real good integral. There is no assumption here that their difference is the integral of a positive function: it is the signed change of the cut domain, including the change-of-variables Jacobian.

Ordinary division through degree two gives the single scalar boundary expression
\[
 B_r:={d_{r,2}\over n_{r,0}}
       -{d_{r,1}n_{r,1}\over n_{r,0}^2}
       +d_{r,0}\left({n_{r,1}^2\over n_{r,0}^3}
                         -{n_{r,2}\over n_{r,0}^2}\right)
       =[w^2]\theta_r.
 \tag{T51}
\]
This retains the inverse normalization. On the replacement domain its second numerator coefficient is exactly
\[
 [w^2]\widetilde N_r
  =\int_{\widetilde{\mathcal C}}
       J_{r,0}e^{\Psi_{r,0}}\phi_d(\Xi_{r,0})
                         (A_{r,2}+\tfrac12A_{r,1}^2)\,d\nu,
 \tag{T52}
\]
with the fixed coordinates and measure of N Section 6. Its first coefficient has \(A_{r,1}\) in place of the parentheses. Subtract the original-domain coefficients to obtain \(d_{r,1},d_{r,2}\). This specifies the boundary quantity with the exact scores, rather than hiding it in “small cut error”.

**Gap — the one inequality at which this attempt stops.** The remaining concrete checkpoint is
\[
 \boxed{\quad
   \rho(c)^2 e^{c_3\tau(Y';\{c\},S)}
           |B_1-B_0|\le C_{\partial},
   \qquad \zeta=\zeta_{\rm r}.
 \quad} \tag{BC2}
\]
The constant must be absolute in the sense of (CN), uniformly over the allowed regions, depths, old zones and site pairs, including their prescribed distances proportional to \(\log(1/g)\). There is one field variable, one degree-two coefficient, one site difference, and no old factor in (BC2). There is no supremum over the continuation disc and no sum over multi-indices. Only the specified real point is tested. The expression is (T51), not an unknown normalized-density operator.

**Discharged — why this is strictly smaller than (CN).** Take the bounded probe \(e=1\). The covariance and third-cumulant terms of (T8) vanish identically, so \(\mathscr K_r(1)=\theta_{r,2}=B_r\). Select just \(\alpha=2\mathbf1_{\{c\}}\), \(\mathcal S=\{S\}\), and \(\zeta=\zeta_{\rm r}\) in the nonnegative sum defining (CN). Its bounded-factor right-hand side is \(C\), and it gives precisely (BC2). Conversely (BC2) says nothing about either score covariance for a nonconstant \(e\), any degree other than two, any multi-site coefficient, or any nonreal \(\zeta\). As a statement about coefficient data it remains unchanged upon adding \(M w_c^3s_S\) to an operator, whereas its (CN) norm can then grow without bound as \(M\) grows. Thus this is a strict necessary projection, not an equivalent reformulation of (CN) or of (15). It isolates only the boundary term that remains even when both connected score terms vanish.

**Gap — why (BC2) has not been proved here, and expectation.** I expect (BC2) to be true. The replacement was chosen at \(p_3=C(L)p\); at real fields its signed mass change is supposed to be exponentially small. The exact boundary formulas (T5)–(T6) suggest that two field derivatives should add a finite polynomial cost, and a distant site should add a response kernel. If these estimates hold after the subtractions in (T51), (T42)–(T49) leave room to pay them. This is a reason for the expectation, not a bound on the actual \(d_{r,k}\).

The missing step is specifically a bound on the signed second cut-mass derivative combined with the three inverse-normalizer subtractions in (T51), with its site response. The source's real (CUT) estimate bounds a mass, not this combination. For example \(\varepsilon(1-\cos(Mw))\) is at most \(2\varepsilon\) on the real axis while its \(w^2\) coefficient is \(\varepsilon M^2/2\); real smallness alone cannot supply a derivative estimate. This example is only a logical test of that inference. The margin-qualified Gaussian theorem proves neither (T52) for the nonlinear inverse coordinate nor the required cancellation with \(n_{r,1},n_{r,2}\). Even granting favourable overlap grouping and far-cut sums, this explicitly identified boundary coefficient remains unbounded by the arguments written here.

**Unchecked — decision boundary.** No actual admissible SU(2) configuration violating (BC2), (15), or (CN) has been constructed. No term of the exact applicable tree series has been shown to diverge. The large values of the sufficient tests in (T29) and (T45) are failures of upper bounds, not refutations. The Gaussian forest identity, positivity, degree-sensitive bound, margin-qualified inverse cut gas, and integrated-root star bound have been discharged above. Their application to the full normalized nonlinear chart on the required disc has not been established. Accordingly this text proves neither (CN) nor a substitute yielding (15).

## 9. Reading and procedure

**Discharged — provenance of inputs and work.** GOAL.md and FINISH-rules.md were read first. Subsequent reads were confined to bounded ranges and text-location searches in this filtered directory: N; the exact-score and coefficient passages of mixed-coefficient.md and mixed-coefficient-2.md; I around the Gaussian split, (CUT), parameter rates, (EI), (MOM), growth and (BANACH); and the product cluster library's normalization proof. A text-location search also returned equation locations in tail-two-step.md; no additional mathematical result from it was used. No mapped-side file, gate file, git history, external source or other account was read. Only this file was written. There was no numerical or symbolic proof run, audit, subagent, commit, push or posting. Every discharged estimate above has a written argument; reading and editing commands are not mathematical evidence.

**Unchecked — foundations and memory boundary.** The elementary finite-dimensional spectral decomposition and Gaussian integral are used as in N Section 7, whose hand derivations were read; they are not inferred from a computation. The forest organization, leaf-word tree encoding, Hermite-polynomial idea and inverse-gas induction were familiar from memory. Their specific identities and bounds used here have been rebuilt in Sections 2–5. The source's lattice and nonlinear estimates remain supplied premises at every application labelled implication.

STOPPED
