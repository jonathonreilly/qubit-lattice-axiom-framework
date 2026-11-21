# Signed cuts under the inverse chart
Provenance: OpenAI Codex, GPT-6 (exact serving variant and configured effort not exposed to this session); the filtered copy of commit `3b715bd03` as supplied; research text, not an audit, granting no status.

## 1. Scope and the first obstruction to test

**Discharged — conventions.** Write I for `parts/hard-core--independent.md`, N for `library/conditional-normalization.md`, T for `library/cn-tree.md`, and P for `library/pos-beta.md`. The object is P(24), with its original denominator, and the proposed bound is P(25). The interior terms in P(8) are outside this task. A label **implication** retains its stated premises; **gap** does not discharge an input merely because I asserts it. Reading and editing commands supply no mathematical evidence. No external source is used. Ideas recalled from memory are identified where used, and their needed identities are proved below.

**Discharged — distinction needed before estimating a face.** P defines a signed *measure* coefficient on the fixed old-field coordinate space, not only a derivative of its total mass. Existence of scalar shape derivatives does not, by itself, give a measure-valued second derivative. A moving sharp boundary can produce a derivative of a surface delta, which acts on derivatives of a test function and is not a finite signed measure. Whether the spectator pushforward removes this obstruction must be checked for the actual cuts. This issue precedes any estimate of the number of faces.

**Discharged — retained normalization.** For a finite signed-measure germ, put \(D_r=\widetilde P_r-P_r\), \(H_r=D_r/N_r\), \(N_r=N^Z_{\rm good}\). If its coefficients through order two exist as measures, multiplication by the inverse scalar series gives
\[
 H_{r,2}=\frac{d_{r,2}}{n_{r,0}}
 -\frac{d_{r,1}n_{r,1}}{n_{r,0}^{\,2}}
 +d_{r,0}\left(\frac{n_{r,1}^{\,2}}{n_{r,0}^{\,3}}
                    -\frac{n_{r,2}}{n_{r,0}^{\,2}}\right).
 \tag{S1}
\]
If only distributional coefficients exist, the same algebra is valid for distributions; it does not make their total variation defined. In particular a scalar inverse cannot cancel a highest-order boundary distribution using only lower-order coefficients.

## 2. Exact differentiation, including intersections of faces

**Discharged — finite-dimensional shape identity (idea from memory; proof here).** Let \(D(w)=\bigcap_{a=1}^m\{F_a(w,z)<0\}\), let \(q(w,z)\) be a \(C^2\) Lebesgue density, and initially use a smooth compactly supported test \(h(z)\). Assume the active faces are smooth, all active intersections have independent normals, and the relevant derivatives are integrable. These are hypotheses of this identity, not conclusions about the inverse chart. Write \(q_j=[w^j]q\). At \(w=0\), with all integrals below over the full coordinate space and the undisplayed cuts retained,
\[
\begin{split}
 Q_h'&=\int_{D(0)}h q_w
 -\sum_a\int hq F_{a,w}\delta(F_a)\prod_{b\ne a}{\bf1}_{F_b<0},\\
 Q_h''&=\int_{D(0)}h q_{ww}
 -\sum_a\int h(2q_wF_{a,w}+qF_{a,ww})\delta(F_a)
                  \prod_{b\ne a}{\bf1}_{F_b<0}\\
 &\quad-\sum_a\int hq F_{a,w}^{\,2}\delta'(F_a)
                  \prod_{b\ne a}{\bf1}_{F_b<0}
 +2\sum_{a<b}\int hq F_{a,w}F_{b,w}\delta(F_a)\delta(F_b)
                  \prod_{j\ne a,b}{\bf1}_{F_j<0}.
\end{split}                                                    \tag{S2}
\]
Here \(Q_h(w)=\int_{D(w)}hq(w,z)dz\). To prove this, use the active \(F_a\)'s as coordinates. The fundamental theorem of calculus for the scalar step function gives \(\partial_w{\bf1}_{F_a<0}=-F_{a,w}\delta(F_a)\). Differentiate again and apply the product rule. Differentiating two distinct indicators gives the factor 2. These are iterated one-dimensional distribution calculations in independent coordinates; a partition into coordinate patches and interior patches proves (S2). At order two no derivative can strike three distinct indicators. Equivalently regularize each scalar step function, calculate, and pass to the limit in these coordinates. This proof specifies the boundary distributions; a product of unspecified distributions is not being assumed.

**Discharged — geometric form of the same identity.** Choose \(F_a\) to be signed distance, positive outside, near each face at every \(w\). Put
\[
 \Gamma_a=\{F_a=0,F_b<0\ (b\ne a)\},\quad
 n_a=\nabla F_a,\quad H_a=\operatorname{div}n_a,\quad
 v_a=-F_{a,w},\quad a_a=-F_{a,ww}.
\]
Thus \(v_a\) is outward normal velocity. The symbol \(a_a\) means this specific signed-distance acceleration. Put
\(\Gamma_{ab}=\{F_a=F_b=0,F_j<0\ (j\ne a,b)\}\),
\(c_{ab}=n_a\cdot n_b\), and \(s_{ab}=\sqrt{1-c_{ab}^2}\). Define
\[
 U(h)=\sum_a\int_{\Gamma_a}h q_0v_a\,dS,
\]
\[
\begin{split}
 V(h)={}&\sum_a\int_{\Gamma_a}
 \{2v_a hq_1+(a_a+H_av_a^2)hq_0
                         +v_a^2\partial_{n_a}(hq_0)\}\,dS\\
 &+\sum_{a<b}\int_{\Gamma_{ab}}hq_0
       \frac{2v_av_b-c_{ab}(v_a^2+v_b^2)}{s_{ab}}\,dS_{ab}.
\end{split}                                                     \tag{S3}
\]
Then \(Q_h'(0)=\int_D hq_1+U(h)\) and \(Q_h''(0)=2\int_D hq_2+V(h)\).
For the conversion, the Jacobian of \(z=y+t n_a(y)\) has derivative \(H_a(y)\) at \(t=0\). Integrating \(\delta'(F_a)\) differentiates \(hqF_{a,w}^2\) and this Jacobian with a minus sign. Also \(\partial_{n_a}F_{a,w}=0\), obtained by differentiating \(|\nabla F_a|^2=1\) in \(w\). Differentiating a remaining indicator in the \(n_a\) direction contributes \(-c_{ab}\delta(F_b)\). The normal Jacobian of the coordinate pair \((F_a,F_b)\) is \(s_{ab}\): its squared determinant is the determinant \(1-c_{ab}^2\) of their normal Gram matrix. Combining the two ordered contributions with the last term of (S2) proves (S3). Orthogonal product faces therefore have the corner contribution \(2v_av_b\), not zero. Curved ball cuts additionally have the \(H_av_a^2\) term.

**Implication — substitution of the actual density.** In N's fixed inverse coordinates, include all Gaussian spectator densities in \(q\), once each. At a real base,
\[
 q_1=q_0 A_1,\qquad q_2=q_0(A_2+A_1^2/2),\quad
 A_1=\ell_1+\Psi_1-\Xi_0\cdot\Xi_1,\quad
 A_2=\ell_2+\Psi_2-\Xi_0\cdot\Xi_2-\tfrac12|\Xi_1|^2.
                                                               \tag{S4}
\]
These follow by expanding \(J e^\Psi e^{-\Xi\cdot\Xi/2}\). The normal score in (S3) is the explicit \(\partial_n\log q_0\), including spectator Gaussian scores when \(n\) has spectator components. A ball cut on a three-component label \(X_a(w,z)\), with threshold \(t_a\), may be used directly in (S2) as
\[
 F_a=|X_a|^2-t_a^2,\quad
 F_{a,w}=2X_a\cdot X_{a,w},\quad
 F_{a,ww}=2|X_{a,w}|^2+2X_a\cdot X_{a,ww},\quad
 |\nabla F_a|=2|(D_zX_a)^T X_a|.                    \tag{S5}
\]
There is no uncomputed “derivative of the cut” left in this specification. Applying (S2) or (S3) to the actual map still requires their regularity and integrability hypotheses. A \(C^2\) diffeomorphism of a product of balls preserves independence of the active normals; a *uniform* angle bound requires bounds on its derivative and inverse.

For explicit conversion from the defining function in (S5), put \(b=|\nabla F|\) and \(n=\nabla F/b\), on the face. The data in (S3) are
\[
 v=-F_w/b,\qquad
 H=\{\operatorname{tr}D_z^2F-n^TD_z^2Fn\}/b,\qquad
 a=-\{F_{ww}+2v\,n\cdot\nabla F_w+v^2 n^TD_z^2Fn\}/b. \tag{S5a}
\]
The middle formula differentiates \(\nabla F/|\nabla F|\). For the last formula differentiate \(F(w,z(w))=0\) twice along a path with \(z'=vn\); since \(n\cdot n'=0\), the normal component of \(z''\) is the normal acceleration. Signed distance has zero normal derivative of its normal speed, so this is precisely its \(a=-F_{ww}\) used in (S3). Thus (S5a) computes the acceleration without requiring a closed formula for the signed distance.

**Discharged — the signed coefficients and normalizer, in surface notation.** Let \(\widetilde D\) be the fixed replacement domain and set
\[
 E_j(h)=\int_{\widetilde D}h q_j-\int_{D(0)}h q_j.
\]
For the original and replacement integrals with the same density,
\[
 d_0(h)=E_0(h),\quad d_1(h)=E_1(h)-U(h),\quad
 d_2(h)=E_2(h)-\tfrac12V(h),                              \tag{S6}
\]
\[
 n_0=\int_Dq_0,\quad n_1=\int_Dq_1+U(1),\quad
 n_2=\int_Dq_2+\tfrac12V(1).                            \tag{S7}
\]
Equations (S1), (S3), (S6) and (S7) give the first and second signed-mass derivatives, including the inverse-normalizer subtractions. For a curvature direction use the first and second directional derivatives of the prescribed coarse-field path in the same formulas. For a site difference compute the entire expression in each state and subtract. No sign or cancellation in that subtraction is assumed.

**Discharged — the suggested Cauchy–Schwarz argument controls exactly the bulk part.** Let \(\Delta_0=\widetilde D\mathbin{\triangle}D(0)\), \(d\mu_0=q_0dz\), and \(G_0=1\), \(G_1=A_1\), \(G_2=A_2+A_1^2/2\). Before pushforward the signed bulk coefficient is \(({\bf1}_{\widetilde D}-{\bf1}_{D(0)})G_j\,d\mu_0\). Pushforward cannot increase weighted variation, so
\[
 \|E_j\|_{\mathcal W}
 \le\int_{\Delta_0}\mathcal W(\pi(z))|G_j|\,d\mu_0
 \le\mu_0(\Delta_0)^{1/2}
       \left(\int_{\Delta_0}\mathcal W(\pi(z))^2|G_j|^2d\mu_0\right)^{1/2}.
                                                               \tag{S7a}
\]
The first inequality follows by taking absolute values against every test bounded by \(\mathcal W\); the second is Cauchy–Schwarz. Independence is unnecessary. This proves the suggested argument for \(E_j\). It leaves \(U,V\) in (S6) and division in (S1). If both domains were fixed in these same observation coordinates, \(U=V=0\).

**Discharged — why a scalar shape calculation is insufficient for (25).** In one dimension let \(P_w(dx)={\bf1}_{x\le w}\phi(x)dx\), where \(\phi(x)=(2\pi)^{-1/2}e^{-x^2/2}\). For a smooth test \(h\),
\[
 \left.\frac{d^2}{dw^2}P_w(h)\right|_{w=0}
       =\phi'(0)h(0)+\phi(0)h'(0)=\phi(0)h'(0).
\]
The tests \(h_K(x)=\sin(Kx)\) have supremum one and give \(\phi(0)K\). No finite signed measure represents this functional, since integration against one would be bounded by its total variation. At threshold \(p\), use \(h_K(x)=\sin(K(x-p))\): the result is \(\phi(p)K\), still unbounded in \(K\) despite its exponentially small prefactor. This refutes the *general inference* from small boundary mass to a measure-valued second coefficient. It is not a configuration of I and does not refute (25).

**Gap — the actual pushforward must be used.** Integrating spectator and kernel coordinates can remove this obstruction. One precise way is integration by parts along a vector field \(T_a\) satisfying \(D\pi\,T_a=0\) and \(T_aF_a=1\), where \(\pi\) is the old-field observation. Expanding
\[
 0=\int\operatorname{div}
 \bigl(h(\pi)qT_a\delta(F_a)\prod_{b\ne a}{\bf1}_{F_b<0}\bigr)
\]
moves \(\delta'(F_a)\) onto \(qT_a\) and the other cuts without differentiating \(h\). Compact support first, followed by an integrable cutoff limit, justifies this identity. It gives face and corner measures if those integrals are bounded. Existence with uniform bounds of these fiber directions is not a consequence of surjectivity alone. In a linear chart \(v=Mx\), the fiber projection is \(K=1-M^T(MM^T)^{-1}M\); a face gradient must have a nonzero \(K\)-component. A right inverse gives no such lower bound: \(M=(1,0)\) is surjective but \(K(1,0)^T=0\). This is not asserted to be the actual matrix. I's redundant local noise may supply the directions; that has not been proved here. The scalar checkpoint below avoids claiming their existence.

## 3. Counting faces: what locality pays

**Discharged — an arbitrarily large independent product does not by itself defeat a surface-to-tail comparison.** For independent three-dimensional standard Gaussian labels cut at radius \(p\ge1\), let \(z\) be one ball's probability, \(\epsilon=1-z\), and \(s=4\pi p^2(2\pi)^{-3/2}e^{-p^2/2}\) its Gaussian surface integral. Integrating the radial density only from \(p\) to \(p+1/p\) proves
\[
 \epsilon\ge p^{-1}e^{-3/2}s.
\]
Indeed \(r^2\ge p^2\) and \(((p+1/p)^2-p^2)/2\le3/2\). For \(m\) labels, the sum of face integrals and the sum over unordered pair intersections are respectively
\[
 ms z^{m-1}\le e^{3/2}p(1-z^m),\qquad
 \binom m2s^2z^{m-2}\le e^3p^2(1-z^m).                 \tag{S8}
\]
For the first inequality, \(m\epsilon z^{m-1}\) is the probability of exactly one failed cut. For the second, \(\binom m2\epsilon^2z^{m-2}\) is the probability of exactly two. Each is at most the probability of at least one failure. This proves a polynomial loss with no face-count factor, even when \(m\) is unbounded. It compares *unnormalized* surfaces with unnormalized exterior mass.

**Discharged — a local collar version not requiring independence.** Here is a precise sufficient hypothesis for the same mechanism. Each face \(\Gamma_a\) admits an injective outward collar \(T_a(y,t)\), \(0<t<h=(1+p)^{-1}\), which keeps cut \(a\) violated, changes only coordinates on which at most \(D_0\) cuts depend, and has volume Jacobian at least \(e^{-A}\). Suppose throughout the collar
\(q(T_a(y,t))\ge e^{-A}q(y)\).
Then
\[
 \sum_a\int_{\Gamma_a}q\,dS
       \le D_0 e^{2A}(1+p)\int_{D^c}q\,dz.             \tag{S9}
\]
Proof: integrate \(q\) on each collar, obtaining at least \(h e^{-2A}\int_{\Gamma_a}q\). A point in that collar violates \(a\), and all its violated cuts belong to the affected set of size at most \(D_0\), since its preimage was on one face and inside all other cuts. Its possible collar labels therefore number at most \(D_0\). Sum and divide by \(h e^{-2A}\). The density must be defined on these collars; an extension past the chart is not implicit.

For pair faces suppose, additionally, that an injective two-parameter outward collar retains both violations, affects at most \(2D_0\) cuts, and its Jacobian and density ratio are each at least \(e^{-2A}\). The identical argument gives
\[
 \sum_{a<b}\int_{\Gamma_{ab}}q\,dS_{ab}
       \le (2D_0)^2e^{4A}(1+p)^2\int_{D^c}q\,dz.       \tag{S10}
\]
At an image point both chosen labels belong to its violated set, of size at most \(2D_0\); this bounds the number of label pairs. Neither statement requires a collar to remain clear of other boundaries.

**Implication — checking the collar hypotheses.** A bound \(|\nabla\log q|\le A_1(1+p)\) along a unit-speed length \(h\) collar gives its density ratio by integrating the derivative of \(\log q\). A normal collar has tangential Jacobian \(\prod_j(1+t\kappa_j)\): its derivative in a principal tangent direction is multiplication by \(1+t\kappa_j\). For \(|t\kappa_j|\le1/2\), integration of \(1/(1+u)\) gives \(\log(1+t\kappa_j)\ge-2|t\kappa_j|\). A bound on \(\sum|\kappa_j|\) therefore supplies the Jacobian bound. These are inputs additional to local dependence. Locality alone is insufficient: place \(K\) alternating kept intervals and \(K\) omitted gaps of equal length in \([p,p+1/p]\), keep \((-\infty,p]\), and omit \([p+1/p,\infty)\). The omitted Gaussian mass is at most \(\Pr(X>p)\), while there are at least \(2K-2\) internal boundary points of density at least \(\phi(p+1/p)\). At fixed \(p\) their ratio grows with \(K\), although only one coordinate is read. This oscillating cut is not I's ball cut.

**Discharged — global division is a different issue.** Even the independent example has
\[
 \frac{\sum_a\int_{\Gamma_a}q}{\Pr(D)}=\frac{ms}{z}.
                                                               \tag{S11}
\]
At fixed \(g>0\) this is unbounded as \(m\to\infty\). Also \(1-z^m\to1\), so (S8) has no uniformly exponentially small right side. Neither a polynomial surface-to-mass bound nor \(e^{-cp^2}\) makes an arbitrary unanchored sum over the whole region finite after normalization. This obstructs that proposed *proof step*, not the connected quantity (S1).

**Discharged — only the changed root coordinates create moving faces in P(24).** In I:(MOM), the inverse change replaces \(\xi_d\) by \((v,\xi_d^\perp)\) and leaves \((\xi_{\mathrm{off}\ d},\xi')\) fixed. The state-A and spectator cuts on these unchanged variables are independent of \(w\). The moving faces in (S2) are the original cuts on the changed coordinates; unchanged cuts have \(F_{a,w}=F_{a,ww}=0\). Any original state-\(x\) cuts affected by this change must also be included in this root set. The locality radius in I:(LOCAL), with the finite enlargement prescribed by (R2), makes that set a finite enlargement of \(d\). Thus there can be arbitrarily many fixed spectator cuts, but not arbitrarily many moving faces for one fixed root. For the small polymers to which I applies smoothing, \(D_e\ll L\), this root has at most a scale-dependent number of labels; the number and its square are affordable in \(C(L,M)\). I treats long polymers separately. Fixing \(L,M\) does not bound \(\operatorname{Vol}(Z)\) for an unrestricted old polymer. Here the difficult extensive terms are density scores and division by \(N_r\), rather than an automatic torus-volume factor in (S3).

**Gap — conclusion about the actual density.** Equations (S8)–(S10) show that a polynomial face loss is possible and specify sufficient local hypotheses. They do not prove those hypotheses, with an exponentially small exterior mass, for the nonlinear divided density in (S1). At fixed \(v\) a conditional spectator mean need not lie a fixed fraction inside its cut. The covariance bound \(C\le1\) supplies no such mean margin. One must integrate \(v\) as well, or prove a connected trace estimate retaining the denominator. Taking a supremum over \(v\) and then a reciprocal conditional cut probability can cost \(e^{C(L)p^2}\). A polynomial in \(p\) does not pay that loss without a comparison of the exponential constants. No such reciprocal is taken here.

## 4. Can the recursion use a different cut?

**Discharged — the fixed-noise proposal is already present, but it fixes different variables.** I:4.7 defines \(N_{\rm good}\) with \(|\xi_i|\le p\), \(|\xi'_i|\le p_4\), on real noise independent of \(W\). Thus its *scalar* integral already permits density/integrand differentiation on a fixed domain. In term (ONE), near labels instead use \(\mu_i\), with \(|x_i|\le p_2\), where \(x=\xi+s_{\rm tot}\). Fixing \(x\) keeps the near old field independent of distant \(W\), by (LOCAL). I:(MOM) then changes coordinates once more to keep the old field \(v\) fixed even under the near-field deformation used for smoothing. Fixed cuts in the first coordinates need not remain fixed in the last ones. Choosing the first coordinates again makes an arbitrary measurable \(e(V)\) depend on \(w\); it does not justify differentiating that function.

**Implication — a legitimate local redesign, with the unpaid part identified.** For each chosen old root \(Z\), one can *define* its main term using \(\widetilde D=\{|v|\le gp_3,\ |\xi_d^\perp|\le p_3\}\) and keep the exact complementary signed integral as another root activity. This algebraic identity uses no positivity of the complement. It preserves the full recursion only if that activity, divided by the original \(N_{\rm good}\), satisfies the required root norm. For real near fields its small supremum could be placed in \(B_{k+1}\), avoiding near-field Taylor coefficients of the error. But its far-variable/site coefficients still need a bound; enlarging the rough set to include every distant variable is not allowed by (R2)'s fixed thickness. Under (LOCAL), faces whose defining functions read only the fixed near data have zero velocity for such far variables. That removes those particular surface terms. It does not remove the connected density scores or the original normalizer. This is a potentially weaker replacement task than (25); its required bound is not proved here.

**Discharged — a root-dependent inverse cut is not automatically a new universal \(N_{\rm good}\).** Both \(v\) and the kernel complement used in (MOM) depend on the chosen \(Z\) and real-base frame. Distinct overlapping old roots give different changes of coordinates. Nothing in their definition identifies all those cut measures with a single label-by-label reference measure for the full gas. Moreover the cut \(|v|\le gp_3\) is justified in the small-\(t\) comparison near the flat field; \(gp_3\to0\). A regular coarse field with curvature of fixed nonzero size need not have its saddle's radial-gauge field of that size. A cut about zero cannot simply replace a cut about that saddle for every regular \(W\). A recentered definition would have to specify its dependence on \(W\), its overlaps and its complementary activities.

**Discharged — what a Gaussian-smoothed indicator gives (idea from memory; identity here).** In one coordinate define
\[
 \chi_{p,\epsilon}(z)=\frac1{\sqrt{2\pi}\epsilon}
       \int_{-p}^{p}\exp\!\left(-\frac{(z-y)^2}{2\epsilon^2}\right)dy,
       \qquad \epsilon>0.
                                                               \tag{S12}
\]
Integration of its uniformly convergent power series on each compact \(z\)-set makes it entire. It satisfies \(0<\chi_{p,\epsilon}(x)<1\) at every real \(x\), and
\[
 |\chi_{p,\epsilon}(x+iu)|
       \le e^{u^2/(2\epsilon^2)}\chi_{p,\epsilon}(x).      \tag{S13}
\]
This follows by taking the modulus inside the integral. Replacing the interval by a ball gives an adjoint-rotation-invariant cut, with \(u^2\) replaced by \(|u|^2\).

For a scalar standard Gaussian \(X\), let \(Z\) be an independent standard Gaussian. Then \(E\chi_{p,\epsilon}(X)=\Pr(|X+\epsilon Z|\le p)\), by Fubini. Completing squares gives the variance \(1+\epsilon^2\) of this sum. Exponential Markov with parameter \(p/(1+\epsilon^2)\) gives
\[
 E|\chi_{p,\epsilon}(X)-{\bf1}_{|X|\le p}|
 \le \Pr(|X|>p)+\Pr(|X+\epsilon Z|>p)
 \le4e^{-p^2/(2(1+\epsilon^2))}.                         \tag{S14}
\]
Thus fixed \(\epsilon\) retains a real Gaussian tail, in this reference problem. Formula (S13), however, costs
\(\exp(\sum_i|\operatorname{Im}z_i|^2/(2\epsilon^2))\) for a product of cuts. A volume-independent bound needs a bound on this *sum*, not separate analyticity of each factor.

**Discharged — identification of readers affected by a change of cut.** Each entry states the status of its mathematical assertions.

| Reader | Effect of the proposed replacement |
|---|---|
| (EI) | **Discharged:** its displayed small activity \(H_0=C(L,M)(gp^3+C_Egp)\) uses the deterministic support bound \(|\xi_{\rm eff}|\le2p\). The soft cut is nonzero at arbitrarily large real noise, so that support implication is false. **Gap:** no replacement integrated activity bound on that enlarged domain is supplied. |
| Chart and (CUT) | **Discharged:** the analytic remainder and inverse chart are supplied only on their chart domain. A nonzero soft weight does not define an integrand outside it. Retaining an outer hard cut retains a moving boundary, albeit at a larger threshold. **Implication:** it could be handled as an additional bad activity after a bound for that activity, not by discarding it. |
| Rough sets (R1)–(R3) | **Discharged:** these rules assign real-field neighborhoods to particular hard/state-\(G\) labels and rely on strict support locality. A root inverse-coordinate cut reads a collection of labels and requires the corresponding enlarged rough set. A soft “good” label has no deterministic small-field guarantee. **Gap:** the same fixed-point thickness and tail weights have not been checked for a new assignment. |
| Good/bad decomposition | **Discharged:** \(1=\chi+(1-\chi)\) remains an exact real partition, with both terms nonnegative. A sharp near/far case distinction and its costs do not follow from it. Telescoping a product gives an error sum over labels, which still needs attachment after normalization. |
| Positivity | **Discharged:** multiplication by (S12) preserves a positive real integrand. An exact split plus its complement leaves the full positive integral unchanged, even if the root comparison correction is signed. Dropping that correction changes the model. |
| RP | **Discharged:** if the total measure is exactly unchanged, every reflection quadratic form is unchanged; no separate RP assertion about a sector is needed. Positivity alone does not protect RP after changing the total measure. On two reflected binary sites, the positive symmetric weights \(w_{00}=w_{11}=1/2,\ w_{01}=w_{10}=1\) give \(\sum_{i,j}(1,-1)_i(1,-1)_j w_{ij}=-1\). Thus an arbitrary positive symmetric cutoff need not preserve RP. **Unchecked:** no new globally modified cutoff law with RP has been constructed here. |

**Gap — decision on exchanging definitions.** Neither “fixed coordinates” nor “soft analytic” gives a proved exchange with the same consequences. A local fixed-\(v\) main term with its exact remainder is allowed algebraically, but proving its remainder norm is still necessary. An everywhere nonzero soft cut additionally loses the support premise of (EI) and the chart. These failures of the proposed shortcuts do not rule out a carefully rebuilt decomposition.

## 5. Attachment and the actual margins

**Discharged — a face can retain a Gaussian tail after arbitrarily many density derivatives.** This auxiliary estimate addresses a possible factorial obstruction. Define \(H_n\) by
\(e^{tx-t^2/2}=\sum_{n\ge0}H_n(x)t^n/n!\).
Differentiating the Gaussian translate proves \(\phi^{(n)}(x)=(-1)^nH_n(x)\phi(x)\). Integrating the generating series on the circle \(|t|=r\) against \(e^{-in\theta}\) extracts its \(n\)-th coefficient, hence
\[
 |H_n(x)|\le n!r^{-n}e^{r|x|+r^2/2}.
\]
For \(n\ge1\) choose \(r=\sqrt n/2\), use \(r|x|\le x^2/4+r^2\), and use \(n!\le n^n\). This gives
\[
 |\phi^{(n)}(x)|\le(2\pi)^{-1/2}\sqrt{n!}\,
             (2e^{3/8})^n e^{-x^2/4}.                  \tag{S15}
\]
The \(n=0\) bound also holds. For a \(q\)-dimensional product Gaussian and a multi-index \(\nu\), multiply these estimates and use \(\prod\nu_i!\le|\nu|!\). Its derivative's integral over the sphere of radius \(p\) is at most
\[
 |S^{q-1}|(2\pi)^{-q/2}p^{q-1}e^{-p^2/4}
          (2e^{3/8})^{|\nu|}\sqrt{|\nu|!}.              \tag{S16}
\]
The surface area factor follows by scaling the unit sphere. Thus, in the independent Gaussian reference, a face insertion has a polynomial-in-\(p\) tail and the same square-root factorial type as T(16), with an explicit extra constant per endpoint. If applied at both endpoints of every edge, this constant replaces \(K\) below by \((2e^{3/8})^2K\). This is not a trace estimate for the nonlinear conditional density.

**Implication — the precise forest hypothesis that would attach an actual boundary insertion.** T Sections 3–5 prove a tree majorant for disjoint coordinate blocks with fixed measurable factors: an edge contributes
\(k_{ij}=\delta^{-1}\sum_{a\in i,b\in j}|C_{ab}|\),
a vertex of degree \(d_i\) contributes \(\sqrt{d_i!}\), and a bad-cut vertex with a mean margin contributes its integrated tail. A growing root costs its fourth moment, not its supremum. To use that theorem here one must first represent or integrate the actual face/corner insertions so that the same majorant holds, and group overlapping interaction supports without losing the covariance bound. A raw \(\delta(F_a)\) is not a bounded measurable factor in that theorem. Replacing it by \(h^{-1}{\bf1}_{0<F_a<h}\) and using a supremum loses \(h^{-1}\). Formula (S16) shows how density differentiation avoids that loss in a product reference; it does not certify it at all nonlinear forest interpolants.

Suppose that, *after taking the specified field coefficient and site difference*, those local reductions give exactly this tree majorant with boundary root activity
\(a_\partial\le C_d g^{-B}p^b e^{-c p^2}\). All costs of the differentiated marked vertices for \(c,S\) must be included in that root/edge/vertex majorant; the undifferentiated theorem does not supply them. Define its weighted row sum
\[
 Q_\sigma=\sup_i\sum_{j\ne i} e^{\sigma d(i,j)} k_{ij}a_j.
\]
Then the rooted absolute tree sum is at most \(a_\partial/(1-8Q_\sigma)\) when \(8Q_\sigma<1\). Here the root includes the changed cut support \(d\). To see the constants, sum a non-root leaf position first; it costs \(Q_\sigma\). Repeating costs \(Q_\sigma^{n-1}\). The leaf-word encoding in T(23) gives
\(\sum_T\prod_i d_i!=(n-2)!\binom{3n-3}{n-2}\).
Replacing \(\sqrt{d_i!}\) by \(d_i!\), dividing by \((n-1)!\), and bounding the binomial coefficient by \(2^{3n-3}\) gives \((8Q_\sigma)^{n-1}\). Sum the geometric series. The marked vertices have to connect to the root in this series; otherwise this argument estimates an extensive disconnected term. The inverse-normalizer subtractions are essential to that connectedness.

**Discharged — spatial weights do not create a new volume factor once a connected tree is available.** If a tree joins \(d,c,S\), its total edge length is at least the minimal joining-tree length. Thus \(e^{\sigma\tau(d;c,S)}\le\prod_{ij\in T}e^{\sigma d(i,j)}\). Replacing \(d\) by \(Y'\) changes this by at most a fixed enlargement factor when their separation is bounded by the prescribed root radius. Field-radius factors such as \(\rho(c)^2\) must be included in the marked-vertex estimates. The crude bound \(\rho(c)\le\rho_e\) permits a fixed power \(g^{-B}\); it does not supply spatial attachment. A finite root permits constants depending on its size. No root-size-independent column bound is inferred from a point-root estimate.

**Discharged — T(42)–T(45) checked in the source units.** Per coarse link, write
\[
 \lambda=\kappa_G/M,\quad
 \sigma=c_3=\kappa_G/(C_{\rm rate}M^4),\quad
 \Delta=\lambda-\sigma
   =\frac{\kappa_G}{M}\left(1-\frac1{C_{\rm rate}M^3}\right).
                                                               \tag{S17}
\]
The explicit sufficient choice \(C_{\rm rate}M^3\ge2\) gives
\(\Delta\ge\kappa_G/(2M)\ge2\log L/M>0\).
This choice concerns the constant defining the weaker weight \(c_3\); it is not an increase of an allowed site distance. It is compatible with I's order of constants: \(M\ge8P\), \(P\ge1\), and taking the free absolute \(C_{\rm rate}\ge1\) gives \(C_{\rm rate}M^3\ge512\). If only \(C_{\rm rate}M^3>1\) is supplied without that choice, use the exact positive \(\Delta\) in every formula below.

For at most \(B_0(r+1)^4\) sites in shell \(r\), \(k_{ij}\le K e^{-\lambda d(i,j)}\) gives
\[
 Q_\sigma\le
 24B_0K a_*(1-e^{-\Delta})^{-5}
 \le24B_0K a_*\left(\frac{1+\Delta}{\Delta}\right)^5.     \tag{S18}
\]
The first inequality uses \((r+1)^4\le24\binom{r+4}{4}\) and five geometric series. For the second, the positive exponential series gives \(e^\Delta\ge1+\Delta\). Consequently
\[
 a_*\le\frac1{384B_0K}
             \left(\frac{\Delta}{1+\Delta}\right)^5
       \quad\Longrightarrow\quad 8Q_\sigma\le\tfrac12. \tag{S19}
\]
For the two-leg bound of T(44), use \(K=B^2/\delta\), with its stated finite-root column constant included in \(B\).

For the cut-gas inverse in T(36), explicit sufficient inequalities are
\[
 6144B_0K(2q_*)^{1/2}
       \left(\frac{1+\Delta}{\Delta}\right)^5e^{-p_*^2/16}\le1,
 \qquad 2(2q_*)^{1/2}e^{-p_*^2/16}\le1.                \tag{S20}
\]
They imply \(Q_u\le1/128\). T's removal recursion then places each single-removal ratio within \(1/7\) of one and bounds its inverse by \(7/6<2\): remove the other vertices of each polymer, cost \(2^{|B|-1}\), sum at most \(16Q_u/(1-16Q_u)\le1/7\), and invert by a geometric series. This controls connected ratios, not the reciprocal of an extensive product probability.

When \(p_*=a p\), \(a>0\) fixed after \(L,M\), both conditions eventually hold. For a three-component ball use the scalar component threshold \(p_{\rm ball}/\sqrt3\); a ball violation forces a component violation at that threshold. The spectator value \(p_4=p/(2C_s(L))\) therefore still gives a positive \(a\). The required mean margin remains a hypothesis. Substituting \(a_*=1\) supplies no small parameter in (S19). Using the precision supremum \(p_i p_j\sum|K_{ab}|\) of T(45) instead grows like \(p^2\); that test does not improve as \(g\downarrow0\).

**Discharged — the prescribed far distance has enough room for polynomial losses, not arbitrary power losses by itself.** In the uncapped case
\(r'/2=(2c_1)^{-1}\log(\rho_e/(C(L)g))\).
The remaining slow kernel is a fixed constant times \(g^{\Delta/(2c_1)}\). With \(\eta=c_3/(8c_1)\),
\[
 \frac{\Delta/(2c_1)}{\eta}
       =4(C_{\rm rate}M^3-1)\ge4
       \quad\hbox{if }C_{\rm rate}M^3\ge2.             \tag{S21}
\]
This verifies the \(g^{4\eta}\) scale against the actual slow rate and weight. It does not assert \(\Delta/(2c_1)>B\) for every fixed loss \(g^{-B}\). If the torus caps \(r'\), keep the actual exponential in the capped distance; replacing it by the uncapped power of \(g\) would be incorrect.

**Implication — T(46)–T(48) and the old growth.** Under their real Gaussian variance and shell premises, integrate the tail
\(\Pr(U>u)\le C_\alpha N e^{-u^2/(4v_0)}\), splitting at \(u_0^2=4v_0\log(\max(e,C_\alpha N))\).
The identity \(EU^{12}=\int_0^\infty12u^{11}\Pr(U>u)\,du\) follows by writing \(U^{12}\) as an integral and using nonnegativity. On the upper part substitute \(t=u^2/(4v_0)\) and integrate \(t^5e^{-t}\) by parts five times. This gives a constant times \(v_0^6\log(\max(e,C_\alpha N))^6\). Hence a root growing like \(t_Y^2+t_Y^3\), with \(t_Y\le c+\sqrt N U\), has fourth moment bounded by a constant times \(1+N^{3/2}(\log(eN))^{3/2}\). This verifies the proposed polynomial cost for fixed \(N=\operatorname{Vol}(Z)\) in that reference. It does not prove the same moment after the actual cut normalization.

**Discharged — T(49), including collar entropy.** Put \(x=\log(1/g)\) and \(p=x^{p_0}\). For fixed \(B,b,C_0,c>0\) and \(p_0>2\), choose \(x_0\) so that, for \(x\ge x_0\),
\[
 Bx+|b|p_0\log x+C_0x^4\le(c/2)x^{2p_0}.
\]
Such \(x_0\) exists because each exponent on the left is strictly smaller than \(2p_0\), and \(\log x\le x\) for \(x\ge1\), by integrating \(1/t\le1\). Then
\[
 g^{-B}p^b e^{C_0x^4}e^{-cp^2}\le e^{-(c/2)p^2}.       \tag{S22}
\]
Thus fixed powers of \(g^{-1}\), fixed polynomial losses in \(p,N\), and the prescribed \(r_2^4=O(x^4)\) collar count are affordable *once the boundary insertion has a connected majorant carrying that tail*. No numerical evaluation is used in (S17)–(S22). The missing premise is the insertion estimate, not the sign or size of these rate margins.

## 6. Far variables, the original ratio, and the continuation disc

**Implication — for genuinely far variables one can avoid moving the original cut.** This is a useful consequence of the actual definitions, narrower than a change of recursion. Use \(x_i\), with \(|x_i|\le p_2\), on all near labels \(NV(Z)\), and use the original \(\xi,\xi'\) elsewhere. The integration domain in these mixed coordinates is fixed. If \(w_c\), or a site change, leaves the real \(W\) data within the (R2) neighborhood unchanged, (LOCAL) makes \(V|_{N_1(Z)}\) independent of that variable at fixed \(x_{NV(Z)}\). The Gaussian dependence is then explicitly in
\[
 \prod_{i\in NV(Z)}\phi_3(x_i-s_{{\rm tot},i}(W,\xi')),
                                                               \tag{S23}
\]
and in the analytic remainder. In a fixed local field frame this representation pushes forward by a map independent of that far variable. At each finite volume, assuming I's analytic chart and a compact parameter neighborhood staying inside it, differentiation of this density on the compact cut domain gives finite signed-measure coefficients on the root field space. Its replacement version has fixed \(v,\xi_d^\perp\) cuts and has the same finite-volume property. This follows by a uniform bound on the finitely many continuous density derivatives on that compact set and integration against bounded tests. No uniform-in-volume bound on those derivatives follows from compactness.

Thus the non-measure example in Section 2 is not a refutation of the actual far-variable coefficient in (25): (S23) supplies another coordinate representation for that case. It does not cover a curvature deformation changing the local \(W\) data. Nor does it bound the connected, normalized derivative uniformly, even in the far case. A site difference must retain the two original states in (S23), rather than retuning the coordinates or radii independently.

**Discharged — the original-normalizer ratio needs lower coefficients as well.** Put
\[
 R(w)=N_{\rm good}^Z(w)/N_{\rm good}(w),\qquad
 \widehat H(w)=D(w)/N_{\rm good}(w)=R(w)H(w).
\]
Then
\[
 \widehat H_2=R_0H_2+R_1H_1+R_2H_0.                    \tag{S24}
\]
For two site states,
\(\widehat H_{1,2}-\widehat H_{0,2}
=\sum_{j=0}^2\{R_{1,j}(H_{1,2-j}-H_{0,2-j})
+(R_{1,j}-R_{0,j})H_{0,2-j}\}\).
These identities follow by multiplying series. A bound on \(R_0-1\), or a real bound on \(R(w)-1\), cannot replace bounds on \(R_1,R_2\) and their site differences. Even a proof of the degree-two version of (25) alone would not control every term of (S24). The quotient must be handled in a coefficient algebra or through all the explicitly displayed lower coefficients. I:(ONE)'s asserted algebra bound for this ratio is a needed input, not proved by a real probability estimate.

**Discharged — Cauchy for one analytic factor is not the coefficient norm of (BANACH).** If \(f(w)=\sum_\alpha f_\alpha w^\alpha\) is analytic and bounded by \(M\) on a finite polydisc of radii \(R_i\), coefficient extraction by integration over its coordinate circles gives
\[
 |f_\alpha|\le M\prod_iR_i^{-\alpha_i},\qquad
 \sum_\alpha\rho^\alpha|f_\alpha|
 \le M\prod_i(1-\rho_i/R_i)^{-1}\quad(\rho_i<R_i).       \tag{S25}
\]
The extraction follows by integrating the uniformly convergent series against the corresponding Fourier monomial; interior circles followed by a limit cover a bound stated on the closed polydisc. The product in (S25) can grow with the number of variables. More fundamentally, scalar analyticity supplies no spatial weights: the single monomial \(w_c/R_c\) is bounded by one on its disc regardless of how far \(c\) is from the root, while its weighted coefficient is \((\rho_c/R_c)e^{c_3d(c,Y')}\).

Even without a spatial weight, a bound on the same polydisc is not a bound on the absolute coefficient sum. The polynomial
\[
 f(z_1,z_2)=\frac{1+z_1+z_2-z_1z_2}{2\sqrt2}
\]
has modulus at most one on the unit bidisc: use
\(|1+z_1|+|1-z_1|\le2\sqrt{1+|z_1|^2}\le2\sqrt2\).
Its coefficient sum there is \(\sqrt2\). Products on \(m\) disjoint pairs still have supremum at most one and coefficient sum \(2^{m/2}\). This is an analytic counterexample to that inference, not to the RG bounds.

**Implication — the valid use of the continuation disc.** If the full root quantity is already analytic with values in the complete weighted coefficient algebra and has norm at most \(M\) on \(|\zeta|\le R=c_{\rm disc}/t_\#\), the same circle extraction gives
\(\|[\zeta^n]F\|\le M R^{-n}\).
On a smaller radius \(r<R\), summing gives \(M/(1-r/R)\). In particular the quadratic coefficient costs \((t_\#/c_{\rm disc})^2\). This is the Cauchy step needed by (BANACH). It assumes the coefficient-algebra norm, including site and tree weights, before taking the \(\zeta\) coefficient. Soft cut factors alone supply neither that norm nor a uniform inverse normalizer.

**Discharged — real positivity does not certify the disc.** A positive real polynomial \(1+A w^2\), \(A>0\), has zeros at \(w=\pm i/\sqrt A\). Hence positivity of the original real normalizer cannot exclude complex zeros. The inverse-gas argument recalled in (S20) does exclude them when its hypotheses hold *in the coefficient algebra*. The real inequalities in Section 5 and the scalar entire function (S12) do not verify those hypotheses for the nonlinear density. The chart-domain obstruction to a global soft cut also persists on the disc.

**Gap — conclusion for item (4).** A soft analytic cut does not directly give the continuation-disc and coefficient-sum statement. It would do so only after a proof of an integrable complex majorant on its actual domain, the rooted field/site coefficient bounds, and the connected inverse-normalizer bound. Those are not consequences of (S12)–(S14). The real degree-two estimate and the all-order continuation problem remain different tasks.

## 7. A strictly smaller stopping inequality

**Discharged — specify a single test, not a new operator norm.** Take a single old cube \(Y\), its prescribed zone \(Z\), and one fixed plaquette \(\square\) strictly inside \(Y\). Use the full regular torus, the flat coarse field, and the nearest admissible field link \(c\) outside the prescribed near-data neighborhood, in the same relative placement at every depth and sufficiently large admissible torus. Use the unit colour direction and radius \(\rho(c)\) of T Section 8, no site change, and its single real \(\zeta_{\rm r}=\min(1,c_{\rm disc}/(2t_\#))\). Equivalently the nonzero coarse link in the field germ is \(W_c(w)=\exp(i\zeta_{\rm r}wT)\). Retain the exact nonlinear integrand and the original \(N^Z_{\rm good}\). Define the one fixed probe
\[
 h_\square(v)=
 \frac{|V_\square(v)-1|^2}{g^2+|V_\square(v)-1|^2}.       \tag{S26}
\]
It is smooth at every real \(v\), gauge invariant, bounded by one, and independent of \(w\) in the fixed root field coordinates. It is an admissible bounded test; it is not asserted to be an old factor produced by a previous RG step. For fixed \(g>0\) its derivatives on the compact local chart are finite. They are not replaced by bounds for arbitrary measurable tests.

**Gap — the single remaining checkpoint, a scalar surface inequality.** In precisely this configuration, form \(E_j(h_\square),U(h_\square),V(h_\square)\) from (S3)–(S6), and \(n_0,n_1,n_2\) from (S7), with all unchanged cuts and spectator integrations retained. The checkpoint is
\[
 \boxed{\quad
 \rho(c)^2\left|
 \frac{E_2(h_\square)-V(h_\square)/2}{n_0}
 -\frac{n_1\{E_1(h_\square)-U(h_\square)\}}{n_0^2}
 +E_0(h_\square)
       \left(\frac{n_1^2}{n_0^3}-\frac{n_2}{n_0^2}\right)
 \right|
 \le C_*p^{b_*}e^{-c_*p^2}.
 \quad}                                                   \tag{SC1}
\]
There must exist \(C_*<\infty\), \(b_*<\infty\), \(c_*>0\), and \(\gamma_*>0\), depending only on the fixed scales and choices already specified, such that this holds for every \(0<g\le\gamma_*\) at every allowed depth and arbitrarily large admissible torus. Existence of the finite-volume scalar derivatives follows from the smooth chart and face hypotheses used above, or from the fixed mixed-coordinate representation (S23) for this far variable. The unresolved assertion is the uniform inequality. No coefficient of an unknown operator is substituted for the displayed bulk, surface, corner, and scalar-normalizer integrals.

**Discharged — why (SC1) is strictly smaller.** The no-site version requested with (25), specialized to this flat state and this one link, implies (SC1): (S6)–(S7) identify its left side with
\(\rho(c)^2|\int h_\square\,dH_2|\), and \(0\le h_\square\le1\le\mathcal W\) bounds that by the proposed weighted total variation. Conversely (SC1) tests one real number, not all bounded or growing functions, not a site response, not the ratio to \(N_{\rm good}\), not a curvature deformation of the near data, and not a complex disc or other coefficients. Its kernel on signed coefficient data is nontrivial: choose two root fields \(u\ne v\) with the same plaquette value at \(\square\), differing on a disjoint local link. Then \(A(\delta_u-\delta_v)\) contributes zero to (SC1), while its unweighted variation is \(2|A|\). Also adding any \(Mw_c^3\) coefficient leaves (SC1) unchanged. These are demonstrations of strict loss of information, not proposed SU(2) counterexamples. Unlike (BC2), the checkpoint has no site difference and probes a specified nonconstant local observable.

**Gap — where the proof of this smaller inequality stops, and expectation.** I expect (SC1) to be true. Only a fixed root's cuts change; (S8), (S15)–(S16), and (S22) show enough tail and derivative margin in the Gaussian reference, and (S23) avoids differentiating the probe for this far variable. But I have not bounded the *connected normalized* expression in (SC1) for the actual nonlinear density. In particular I have not converted its integrated face terms and density scores into an activity satisfying the forest majorant uniformly in all the unchanged cuts, while retaining the subtractions involving \(n_1,n_2\). An unconditional tail followed by a separate reciprocal of \(n_0\) is invalid by (S11); conditioning on the observation and taking a near-cut reciprocal may lose the tail as described in Section 3. The expectation rests on the local structure and the explicit margins, not on an estimate of either reciprocal.

**Unchecked — decision on the requested item.** No admissible configuration violating (25), its no-site or curvature version, or the required original-normalizer ratio has been exhibited. The auxiliary counterexamples refute only the identified shortcuts: a scalar shape derivative need not be a measure, positivity need not imply RP, and scalar analyticity need not control the weighted coefficient sum. There is also no proved replacement recursion with the same consequences. The next mathematical task is (SC1), with its exact specified integrals. The interior part of (NC-square) was not attacked.

**Discharged — reading and procedure.** GOAL.md and FINISH-rules.md were read first. Subsequent reads were bounded passages and text-location searches within P, T, N, and I, covering their cut, chart, (ONE), (MOM), (BANACH), rough-set, coefficient, and rate definitions. A broad text-location search in I also returned unrelated lines; none is used as a proof input. No gate file, git history, mapped-side file, outside-directory source, or external proof account was opened. Only this output file was written. There was no mathematical computation or enumeration, numerical or symbolic proof run, audit, subagent, commit, push, or posting. Every discharged estimate here is a written argument. The shape-calculus, Gaussian/Hermite generating-function, and Cauchy ideas were familiar from memory; their identities and bounds used here were derived explicitly. Other source-dependent assertions retain the implication or gap labels.

STOPPED
