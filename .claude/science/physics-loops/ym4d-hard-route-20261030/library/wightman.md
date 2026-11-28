# Scalar reconstruction in four dimensions (row 201)
Provenance: Codex (GPT-6; exact variant and runtime effort not exposed; queue requests max), checkout `ee8a587591035641b44ce93aa0fa9ae8c1018e7b`, Sussman–Alpoge commit `31a47c543775`. Research text; not an audit; grants no status.

## 1. Scope and inputs

We work with one supplied component \(\sigma=\sigma_\xi\). All upstream hypotheses remain premises.
Normalize \(S_0=1\), and let \(\Omega=[\varnothing]\).
The requested conclusion is a scalar Wightman theory for its action-density correlations.
It belongs to T0, by GOAL.md's owner decision of 2026-11-03.
The older exclusion in `t0-skeleton.md`, Sections 1–3.1, is superseded.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.
We rebuild their [YM3_I](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM3/YM3_I.tex), L79749–81160, especially Theorem IV-76-59.
The target is their [YM4 outline](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM4_sketch_500.tex), Theorem 0′(4), H3, L4616 and L31688.
The reconstruction method originates with K. Osterwalder and R. Schrader,
[Axioms for Euclidean Green's Functions II](https://doi.org/10.1007/BF01608978), CMP **42** (1975), 281–305, §IV.1.
We do not use its reconstruction theorem as a discharged step.

Use Euclidean coordinates \((\mathbf x,t)\in\mathbb R^3\times\mathbb R\), reflection \(\theta(\mathbf x,t)=(\mathbf x,-t)\), and \((\tau_af)(x)=f(x-a)\).
Write \(p_r(f)=\max_{|\alpha|\le r}\sup_x(1+|x|^2)^{r/2}|\partial^\alpha f(x)|\).
The named inputs are:

* [growth-qf3.md](growth-qf3.md), (1): the unique diagonal-flat extension, with
  \(|S_n(f)|\le C^n(n!)^{k+32}p_{20n}(f)\), including constrained positive-time tensor density.
* [s4-s6.md](s4-s6.md), Sections 5–7: the separable reflection Hilbert space, dense compact tuple classes,
  \(T_s=e^{-sH}\), \(H\ge0\), spatial translations, and their strong continuity.
  Reflection positivity, symmetry and reality hold on this same component.
* [ac-port.md](ac-port.md), Result: full Euclidean invariance on that domain, conditional on D1 and TU10.
* [cluster-port.md](cluster-port.md), Sections 8–9: component clustering and \(\ker H=\mathbb C\Omega\).
* [ui-port.md](ui-port.md), Result, and [pd-port.md](pd-port.md), (7): an insertion bound independent of outside field numbers.

These are inputs about the same hierarchy and Hilbert space. They must not be assembled from different limits.
No nonzero one-point constant is discarded. No Euclidean contact terms are assigned.

## 2. The reconstruction input and point forms

Write \(U(\mathbf a)[F]=[\tau_{(\mathbf a,0)}F]\), and let \(\Pi\) be the joint spectral measure of \(H,U\).
The coordinate cone \(E\ge|q_j|\) belongs to PD's stated input;
[cone-o6.md](cone-o6.md), (7), obtains it from the same S6 and diagonal RP.
Spatial rotations act isometrically on tuple classes, commute with \(H\), and rotate \(\mathbf q\).
Their continuity follows by expanding the squared norm of a rotated tuple difference.
Conjugate the coordinate cone by rotations from a countable dense set.
Outside one spectral null set, \(E\ge|\mathbf n\cdot\mathbf q|\) for every such direction.
Continuity in \(\mathbf n\) gives \(E\ge|\mathbf q|\).

Put \(d(z)=\Re z_4-|\Im\mathbf z|\) and
\[
 T(z)=\int e^{-z_4E+i\mathbf z\cdot\mathbf q}\,d\Pi(E,\mathbf q),
 \qquad \iota(t,\mathbf x)=(\mathbf x,-it),\qquad V(x)=T(\iota x).
 \tag{1}
\]
These are contractions on \(d\ge0\), strongly continuous there and norm holomorphic on \(d>0\).
Indeed, the integrand has modulus at most \(e^{-dE}\).
Dominated convergence proves strong continuity; \(E^m e^{-dE}\le m!d^{-m}\) bounds each interior Taylor series.
Positive margins map into \(\mathcal D_\infty=\bigcap_{j\ge1}\operatorname{Dom}H^j\).

Set \(c_0=1/64\), \(\wp=5\).
PD (7), followed by contraction through \(3\eta/4\), gives
\[
 |\sigma(\theta\bar F\cdot(h)\cdot G)|
 \le C\eta^{-5}\|h\|_{L^1}
 \|[\tau_{-\eta e_4}F]\|\|[\tau_{-\eta e_4}G]\|,
 \quad 0<\eta\le1,                                      \tag{2}
\]
where \(F,G\) lie above \(\eta\), and \(h\) lies in \(|t|<c_0\eta\).
This verifies YM3_I's (Rec4), with all outside degrees allowed.
If (2) is given only after centering, replace each slot by \(h+c\int h\), where \(\sigma(h)=c\int h\).
The resulting triangular map of tuples is invertible, multiplicative on admitted products, and preserves the reflection form.
It therefore identifies the two Hilbert spaces and their translations.
The extra insertion is \(c\int h\) times the identity form.
Cauchy–Schwarz and contraction bound it by the right side of (2) with \(C=|c|\).
Thus replace \(C\) by \(C+|c|\); no centering hypothesis is needed.

Translate both outside tuples by \(\eta e_4\) in (2).
Riesz representation gives a bounded insertion \(I_\eta(h)\), with
\[
 \|I_\eta(h)\|\le C\eta^{-5}\|h\|_{L^1},\qquad
 I_\eta(h)[F]=[(\tau_{\eta e_4}h)\cdot\tau_{2\eta e_4}F]. \tag{3}
\]
Pairing with every tuple class proves the second identity by a common time translation.
The bound kills null vectors and extends the map to \(L^1\).
Scalar matrix elements have \(L^\infty\) densities by \(L^1\) duality.
These densities have continuous analytic representatives, as follows.
For \(0<\eta'<\eta\), translation of (3) gives
\[
 I_\eta(\tau_wh)=
 T((\eta-\eta')e_4+w)I_{\eta'}(h)T((\eta-\eta')e_4-w)
 \tag{4}
\]
when \(|w_4|<c_0(\eta-\eta')\).
Insert a nonnegative unit-integral mollifier at zero, supported in the smaller slab.
The right side is uniformly bounded and holomorphic on
\(|\Re w_4|+|\Im\mathbf w|<\eta-\eta'\).
Cauchy estimates and a diagonal subsequence give locally uniform scalar limits.
On real compact sets the same mollifiers converge in \(L^1\) to the original density.
Thus every such limit represents that density; analytic uniqueness identifies all limits and overlaps.
The original bound and sesquilinearity hold everywhere by continuity.
Riesz representation now gives operators \(b_\eta(x)\), with \(\|b_\eta(x)\|\le C\eta^{-5}\).

Equality of densities in (4) gives
\(b_\eta(x+w)=T((\eta-\eta')e_4+w)b_{\eta'}(x)T((\eta-\eta')e_4-w)\).
Consequently
\[
 \begin{aligned}
 B(s,s')&=T_{s-\eta}b_\eta(0)T_{s'-\eta},
             &&0<\eta\le\min(s,s',1),\\
 T_aB(s,s')T_b&=B(s+a,s'+b),&
 B(s,s')^*&=B(s',s),\\
 \|B(s,s')\|&\le C\min(s,s',1)^{-5},&
 b_\eta(x)&=U(\mathbf x)B(\eta+t,\eta-t)U(-\mathbf x).
 \end{aligned}                                             \tag{5}
\]
The first expression is independent of \(\eta\), by the density identity at zero.
Choosing the largest allowed \(\eta\) proves the bound.
Reality and reflection give \(I_\eta(h)^*=I_\eta(\theta\bar h)\), hence the adjoint identity in (5).
Spatial covariance gives its last formula.
Factoring through a strictly smaller margin proves norm continuity of these operators.
These identities also show uniqueness: (3) determines the continuous density, hence \(b_\eta(0)\), then every \(B(s,s')\).

## 3. A field on one invariant domain

For real \(l>5\), write \(R=(1+H)^{-1}\).
Define the norm-convergent integral
\[
 A_l=\Gamma(l)^{-2}\int_0^\infty\!\int_0^\infty
 (ss')^{l-1}e^{-s-s'}B(s,s')\,ds\,ds'.                   \tag{6}
\]
Its norm is at most \(C[1+2\Gamma(l-5)/\Gamma(l)]\), since
\(\min(s,s',1)^{-5}\le1+s^{-5}+s'^{-5}\).
Interchanging \(s,s'\) proves self-adjointness.
The scalar Laplace integral for \((1+E)^{-a}\), spectral calculus, and (5) give
\[
 R^aA_lR^a=A_{l+a},\qquad T_sA_lT_{s'}=R^lB(s,s')R^l.    \tag{7}
\]
For the first identity, substitute \(v=s+t\) in each convolution and use
\(\int_0^v t^{a-1}(v-t)^{l-1}dt=v^{a+l-1}\Gamma(a)\Gamma(l)/\Gamma(a+l)\).
For the second, move both external semigroups inside (6) and use the shift law.
All integrals are absolutely bounded by (6).
Hence
\[
 q_0(\psi,\chi)=\langle(1+H)^l\psi,A_l(1+H)^l\chi\rangle,
 \qquad q_0(T_s\psi,T_{s'}\chi)=\langle\psi,B(s,s')\chi\rangle.
 \tag{8}
\]
This is a Hermitian form on \(\operatorname{Dom}H^l\).
Equation (7) makes it independent of any larger admissible regularization exponent.
Below fix \(l=6\).

For \(f\in\mathcal S(\mathbb R^{1+3})\), put
\[
 q_f(\psi,\chi)=\int f(x)q_0(V(-x)\psi,V(-x)\chi)\,dx,
 \qquad c_N(f)=\|A_l\|\sum_{r=0}^N\binom Nr\|\partial_t^rf\|_{L^1}.
 \tag{9}
\]
The integrand is continuous and bounded by the two \(l\)-th graph norms.
Differentiating \(e^{-itH}\) on \(\mathcal D_\infty\) and integrating by parts gives
\[
 q_f(H\psi,\chi)-q_f(\psi,H\chi)=i q_{\partial_tf}(\psi,\chi).
\]
There is no boundary term because \(f\) is Schwartz.
Iterate this identity \(l+j\) times with the first vector \(R^l\psi\).
The binomial expansion gives
\[
 |q_f((1+H)^j\psi,\chi)|
 \le c_{l+j}(f)\|\psi\|\|(1+H)^{2l+j}\chi\|.             \tag{10}
\]
At \(j=0\), Riesz gives \(\phi(f)\chi\), with \(\langle\psi,\phi(f)\chi\rangle=q_f(\psi,\chi)\).
For every \(j\), (10) puts this vector in \(\operatorname{Dom}H^j\).
Indeed, test with \(\psi=(1+H)^j1_{H\le N}\phi(f)\chi\), then let \(N\uparrow\infty\).
Thus
\[
 \phi(f):\mathcal D_\infty\to\mathcal D_\infty,\qquad
 \|(1+H)^j\phi(f)\chi\|\le c_{6+j}(f)\|(1+H)^{12+j}\chi\|.
 \tag{11}
\]
The defining form proves Hermiticity and
\(V(a)\phi(f)V(-a)=\phi(f(\cdot-a))\).
Its matrix elements are tempered: in four dimensions
\(\|\partial^\alpha f\|_{L^1}\le Jp_{|\alpha|+6}(f)\),
where \(J=\int_{\mathbb R^4}(1+|x|^2)^{-3}dx=\pi^2/2\).
The last integral follows by polar coordinates and \(u=r^2\).

We will use one consequence of (11).
Products of fields converge in every graph norm when their tests converge in Schwartz space.
One may interleave contractive joint spectral multipliers which converge strongly.
To prove this, telescope one factor, apply (11), and work from the vacuum outward.
Spectral multipliers commute with graph powers, so their strong convergence also holds in each fixed graph norm.

## 4. Euclidean kernels and their analytic continuation

For differences with \(d(\zeta_j)>0\), choose \(0<\eta\le1\) with \(2\eta\le\min_jd(\zeta_j)\).
Writing \(B_\eta=B(\eta,\eta)\), define
\[
 \begin{split}
 W_n(\zeta)&=\langle\Omega,B_\eta T(\zeta_1-2\eta e_4)B_\eta
                  \cdots T(\zeta_{n-1}-2\eta e_4)B_\eta\Omega\rangle,\\
 \Psi_n(z)&=T(z_1-\eta e_4)B_\eta
             \prod_{j=1}^{n-1}[T(z_{j+1}-z_j-2\eta e_4)B_\eta]\Omega.
 \end{split}                                               \tag{12}
\]
For the second line also require \(\eta\le d(z_1)\); products are ordered from left to right.
For \(n=1\), set \(W_1=\langle\Omega,B_1\Omega\rangle\); set \(W_0=1\).
Replacing \(B_\eta\) by \(T_{\eta-\eta'}B_{\eta'}T_{\eta-\eta'}\) proves independence of \(\eta\).
The inserted semigroups combine with their neighbors and fix \(\Omega\) at the ends.
Fixed smaller margins prove holomorphy, including norm holomorphy of \(\Psi_n\), and
\[
 |W_n|,\ \|\Psi_n\|\le(C\eta^{-5})^n.                    \tag{13}
\]

These kernels reproduce ordered tuples.
Suppose \(h_j\) lies in \(|t-t_j|<c_0\eta\), with \(t_{j+1}-t_j\ge2\eta\).
Set \(g_j=\tau_{-t_je_4}h_j\), \(s_j=t_{j+1}-t_j-2\eta\).
Starting at the right in (3), induction identifies
\(I_\eta(g_1)T_{s_1}\cdots I_\eta(g_n)\Omega\)
with \([\tau_{(\eta-t_1)e_4}(h_1,\ldots,h_n)]\).
Its vacuum component is \(\sigma(h_1,\ldots,h_n)\).
If \(t_1\ge\eta\), multiplication by \(T_{t_1-\eta}\) gives the original tuple class.
Insert the density (5), using margin \(\eta/2\), in each factor.
Fubini applies because the density is bounded and the tests are \(L^1\).
Adjacent factors combine exactly as in (12). Thus the scalar and vector kernels are \(W_n\) and \(\Psi_n\).

For \(u\in S^3\), define
\(d_u(z)=\Re(u\cdot z)-|\Im(z-(u\cdot z)u)|\).
For each permutation \(\pi\), use the tube \(d_u(z_{\pi(j+1)}-z_{\pi(j)})>0\).
Rotate \(u\) to \(e_4\) in (12), and permute the arguments.
Euclidean invariance and symmetry identify the resulting kernels on real overlaps, by product approximate identities.
Every complex overlap is convex and contains the real parts of its points.
The identity theorem therefore identifies the kernels throughout each overlap.
They give one symmetric holomorphic function \(\mathcal S_n(z)\) on the union of these tubes.

The real tubes cover all distinct configurations.
Indeed, for uniform \(u\in S^3\), the density of \(u\cdot v\), \(|v|=1\), is
\((2/\pi)\sqrt{1-s^2}\), so \(\Pr(|u\cdot v|<a)\le2a\).
This follows from \(s=\cos\theta\), the area factor \(\sin^2\theta\,d\theta\), and \(\int_{-1}^1\sqrt{1-s^2}ds=\pi/2\).
With \(a=(2n^2)^{-1}\), the union of the \(\binom n2\) forbidden bands has measure less than one.
For minimum separation \(\rho\), some direction therefore gives all projection gaps at least \(\rho/(2n^2)\).
Partition compact separated supports into sufficiently small balls and apply the ordered formula to each product.
Summation proves
\[
 \sigma(f_1,\ldots,f_n)=\int s_n(x)\prod_j f_j(x_j)\,dx,
 \qquad |s_n(x)|\le C^n(4n^2)^{5n}\min(1,\rho)^{-5n},     \tag{14}
\]
The estimate is for \(n\ge2\); \(s_n\) is the real restriction of \(\mathcal S_n\), and \(s_1=W_1\).
Continuity of the kernels also proves their reality and Euclidean invariance from those of \(\sigma\).

For completeness, (14) is integrable against every diagonal-flat Schwartz test.
If \(\rho\le1\), move a closest pair to its midpoint.
The total displacement in the coordinate \(\ell^1\) norm is at most \(2\rho\).
Taylor's remainder at that diagonal, of order \(5n\), gives
\[
 |f(x)|\le e^2\rho^{5n}3^{11n/2}p_{11n}(f)(1+|x|^2)^{-11n/2}.
\]
Here \(2^{5n}/(5n)!\le e^2\); moving at most unit Euclidean distance costs the displayed weight factor.
For \(\rho>1\), use the seminorm directly.
Also \((1+|x|^2)^{-11n/2}\le\prod_j(1+|x_j|^2)^{-3}\) and \(n^n\le e^nn!\).
Integration gives \(\int|s_nf|\le C_1^n(n!)^{10}p_{11n}(f)\).
For \(n=1\), use its constant kernel and the same integrable weight.
This continuous functional agrees with the supplied E0′ extension on separated tensors.
Constrained tensor density identifies them on the whole diagonal-flat domain.

## 5. Tempered boundaries, cyclicity and the vacuum

Sandwich (9) between two positive-margin spectral factors.
Equation (8) replaces the regularized point form by \(B(s,s)\):
\[
 T(w)\phi(f)T(w')=\int f(x)
 T(w-se_4+\iota x)B(s,s)T(w'-se_4-\iota x)\,dx,          \tag{15}
\]
where \(0<s\le\min(1,d(w),d(w'))\).
All factors are bounded by (5); the identity first holds in matrix elements, hence as bounded operators.
Split intermediate semigroups in half and iterate (15).
Fubini gives the vector kernel \(\Psi_n(\sum_{r\le j}w_r+\iota x_j)\) for
\(T(w_1)\phi(f_1)\cdots T(w_n)\phi(f_n)\Omega\).
Letting the intermediate margins decrease to zero, (11) proves
\[
 \begin{split}
 \langle\Omega,\phi(f_1)\cdots\phi(f_n)\Omega\rangle
 =\lim_{\epsilon\downarrow0}\int\prod_jf_j(x_j)\,
 W_n\Bigl((\iota(x_{j+1}-x_j+i\epsilon\alpha_j))_{j=1}^{n-1}\Bigr)\,dx,
 \end{split}                                               \tag{16}
\]
for every \(\alpha_j\in V_+=\{a:a^0>|\mathbf a|\}\).
The spectral contractions \(T(\iota(i\epsilon\alpha_j))\) converge strongly to the identity.

Here is the distributional boundary argument, including general tests.
Suppose a holomorphic kernel on \(z_j=\iota x_j+\eta h_je_4\), \(x\in K\) compact,
is bounded by \(b\eta^{-p}\), where \(p\) is a nonnegative integer.
Write \(I_g(\eta)=\int g(x)F(z)dx\), \(D_h=\sum h_j\partial_{t_j}\), and \(N=p+1\).
Cauchy–Riemann and integration by parts give \(I_g^{(r)}=I_{(-iD_h)^rg}\).
Taylor's integral formula from \(\eta_0\) to \(\eta\) contains the remainder
\[
 \frac{(-1)^N}{(N-1)!}\int_\eta^{\eta_0}
 (s-\eta)^{N-1}I_{(-iD_h)^Ng}(s)\,ds.
\]
Its absolute majorant is \(b\|D_h^Ng\|_{L^1}s^{N-1-p}/(N-1)!\), which is integrable at zero.
The finite Taylor terms and dominated convergence give a limit, with
\[
 \sup_{0<\eta\le\eta_0}|I_g(\eta)|
 \le b\eta_0^{-p}\sum_{r=0}^{N}\|D_h^rg\|_{L^1},\qquad \eta_0\le1. \tag{17}
\]
This also bounds \(I_g'\), on applying the same estimate to \(-iD_hg\).

Apply (17) to (12), with \(h_j=2j\), \(p=5n\), \(b=C^n\), \(\eta_0=1\).
The resulting functional \(\mathcal W_n\) obeys, with \(N=5n+1\),
\[
 |\mathcal W_n(F)|\le C^n(N+1)[n(n+1)]^N J^n p_{N+6n}(F). \tag{18}
\]
Thus it extends from compact tests to all Schwartz tests by smooth cutoffs.
It agrees with (16) on tensors, first compact, then Schwartz, by (11).
Tensor sums are dense: cut off, convolve with a product mollifier, and approximate the compact convolution integral by Riemann sums.
Every fixed derivative converges uniformly on a common compact set; then remove the cutoff.
This proves uniqueness of the tempered distributions and their positive Hilbert metric.
Explicitly, their quadratic polynomial form is the squared norm of the corresponding field polynomial acting on \(\Omega\).

Let \(\mathcal D_0=\operatorname{span}\{\Omega,\phi(f_1)\cdots\phi(f_n)\Omega\}\).
It is invariant under the fields and translations, by (11) and covariance.
To prove density, take \(\psi\perp\mathcal D_0\).
Inserted real translations preserve these polynomial vectors.
Replace those translations, from left to right, by positive-margin \(T(w)\).
After the first replacement, the preceding adjoints put the first vector in \(\mathcal D_\infty\); all field adjoints are legitimate.
The remaining translation matrix element is the Fourier transform of a finite joint spectral measure.
Its vanishing for all translations makes that measure zero, hence also its \(T(w)\) integral.
Fourier uniqueness here follows by convolution with Gaussian approximate identities and ordinary Fourier inversion.
Equation (15) and product approximate identities now give \(\langle\psi,\Psi_n(z)\rangle=0\).
Thus \(\psi\) annihilates every time-ordered positive-time tuple class.

Partition any other positive-time tuple into small cubes of side \(2h\), using nonnegative partitions of unity.
Products whose center heights differ by at least \(4h/c_0\) are time ordered.
The remaining products occupy the union of strips
\(|t_i-t_j|<(4/c_0+2)h\).
Their \(\prod|f_j|\) integral is \(O(h)\), by integrating one time coordinate first.
On the original supports and their reflections, \(s_{2n}\) is bounded: all points there remain distinct.
Equation (14) therefore bounds the squared norm of the remaining sum by \(C[O(h)]^2\).
It tends to zero. All positive-time tuple classes are dense by the supplied Hilbert bridge, so \(\psi=0\).

The translation spectrum of \(V(t,\mathbf x)\) is \((E,-\mathbf q)\in\overline V_+\), in the convention \(e^{ip\cdot x}\).
Finally \(T_s\to1_{H=0}\) strongly.
Component clustering makes \(\langle[F],T_s[G]\rangle\to\overline{\sigma(F)}\sigma(G)\).
Density gives \(1_{H=0}=|\Omega\rangle\langle\Omega|\).
Hence the cyclic vacuum is the unique translation-invariant vector up to scalar multiples.

## 6. Lorentz covariance and locality

Let \(\Lambda\in\mathrm{SO}^+(1,3)\).
The map \(\widehat\Lambda=\iota\Lambda\iota^{-1}\) preserves \(d>0\), since \(\Lambda V_+=V_+\).
For a boost in the first spatial direction, use
\[
 r_z(y_1,y_2,y_3,y_4)=
 (y_1\cos z+y_4\sin z,y_2,y_3,y_4\cos z-y_1\sin z).
\]
Then \(r_{is}=\widehat{B(s)}\).
For real differences with positive fourth coordinates, all \(r_{is}\)-transformed differences stay inside the tube.
A neighborhood of each compact imaginary-angle segment stays inside too.
For small real angles, Euclidean invariance makes \(W_n(r_z\zeta)\) constant.
The one-variable identity theorem continues that equality along the segment.
The identity theorem in the difference variables gives boost invariance throughout the product tube.
Spatial rotations already preserve the kernels.
Every proper orthochronous Lorentz matrix is a product of these transformations:
rotate and boost \(e_0\) to \(\Lambda e_0\); the residual transformation fixes \(e_0\) and lies in \(\mathrm{SO}(3)\).

Change variables by \(\Lambda\) in (16); its determinant is one, and the new approach vectors remain in \(V_+\).
Thus all \(\mathcal W_n\) are Lorentz invariant.
On polynomial vectors define
\[
 V(\Lambda)\phi(f_1)\cdots\phi(f_n)\Omega
   =\phi(f_1\circ\Lambda^{-1})\cdots\phi(f_n\circ\Lambda^{-1})\Omega.
 \tag{19}
\]
Hermiticity expresses their inner products as \(\mathcal W_{m+n}\) values, with the first string conjugated and reversed.
Invariance therefore makes (19) well defined and isometric.
The inverse rule uses \(\Lambda^{-1}\); density gives a unitary on \(\mathcal H\).
The group law and field covariance hold on the spanning polynomial vectors.
Schwartz continuity under linear changes, followed by (11), gives strong continuity there; unitarity extends it to \(\mathcal H\).
Also \(V(\Lambda)V(a)V(\Lambda)^{-1}=V(\Lambda a)\), checked on the same vectors.
Hence \(V(a,\Lambda)=V(a)V(\Lambda)\) represents the proper orthochronous Poincaré group.

It remains to prove local commutativity without importing an analytic-continuation theorem.
First use compact smooth tests and interchange adjacent spacelike-separated slots \(k,k+1\).
On their full compact product support \(K\), put
\[
 \begin{gathered}
 \delta=\min_K(|\mathbf x_{k+1}-\mathbf x_k|-|t_{k+1}-t_k|)>0,\quad A=4/\delta,\\
 M=\max_{K,j<n}(|\mathbf x_{j+1}-\mathbf x_j|+|t_{j+1}-t_j|),
 \quad h_*=2AM+6,\quad \eta_0=\min(1,(2A)^{-1}),\\
 h_k^\lambda=-\lambda/2,\quad h_{k+1}^\lambda=\lambda/2,\\
 h_j^\lambda=-\tfrac12-(k-j)h_*\ (j<k),\qquad
 h_j^\lambda=\tfrac12+(j-k-1)h_*\ (j>k+1),\\
 z_j=\iota x_j+\eta h_j^\lambda e_4,
 \qquad -1\le\lambda\le1,\quad0<\eta\le\eta_0.
 \end{gathered}                                             \tag{20}
\]
Let \(v=(\mathbf x_{k+1}-\mathbf x_k)/|\mathbf x_{k+1}-\mathbf x_k|\), and take
\(u=\cos\theta\,e_4+\sin\theta\,(v,0)\), with \(\sin\theta=A\eta\).
Direct projection gives
\[
 d_u(z_{j+1}-z_j)=\eta\Delta h_j\cos\theta
       +A\eta v\cdot\Delta\mathbf x_j-A\eta|\Delta t_j|.   \tag{21}
\]
For \(j=k\), this is at least \(-\eta+A\eta\delta=3\eta\).
For every other slot it is at least \(\eta h_*/2-A\eta M=3\eta\), since \(\cos\theta\ge1/2\).
Thus (20) stays in the union of tilted tubes, with \(|\mathcal S_n(z)|\le(C\eta^{-5})^n\).
The witnessing direction may vary; the glued holomorphic function is one function.

For \(I_g(\lambda,\eta)=\int g(x)\mathcal S_n(z)dx\), put
\(D_\lambda=\sum h_j^\lambda\partial_{t_j}\), \(D'=\tfrac12(\partial_{t_{k+1}}-\partial_{t_k})\).
Cauchy–Riemann and integration by parts give
\[
 \partial_\eta I_g=I_{-iD_\lambda g},\qquad
 \partial_\lambda I_g=\eta I_{-iD'g}.
\]
The coefficients of \(D_\lambda\) are uniformly bounded.
Estimate (17), with \(p=5n\), therefore bounds \(|I_{D'g}|\) by one finite constant \(Q_g\), independent of \(\lambda,\eta\).
Consequently \(|I_g(1,\eta)-I_g(-1,\eta)|\le2\eta Q_g\to0\).
At the endpoints, (16) gives the two adjacent orders; symmetry of \(\mathcal S_n\) identifies the second labeling.
Their Wightman values are equal.
Pairing with polynomial vectors, and moving their adjoints by Hermiticity, gives
\([\phi(f),\phi(h)]\psi=0\) on \(\mathcal D_0\).
To remove compact support, cut off every Schwartz test inside its original support and use (11).
Spacelike separation is preserved. Thus locality holds for all spacelike-separated Schwartz supports.

## 7. Dimension changes and the first unavailable input

Time is now \(x_4\); there are three spatial momenta and the group is \(\mathrm{SO}^+(1,3)\).
The supplied PD exponent is \(5\), so the point-form regularization uses \(l=6\).
The separating-direction calculation uses the \(S^3\) band density, as computed above.
The three-dimensional weight \((1+|x|^2)^{-2}\) fails in \(\mathbb R^4\): its radial tail is \(\int^\infty dr/r\).
Power \(3\) repairs it, giving six weight orders per slot in (18), rather than four.
The locality deformation still lies in the plane spanned by time and the spacelike separation.
The extra spatial coordinates change none of its inequalities.

**First failing input within the stated conditional reconstruction: none.**
The uniform \(L^1\) insertion estimate (2) is essential to this direct proof; E0′ alone is not substituted for it.
**First unavailable source input for unconditional T0: rooted D1**, beginning at **C1/OH1** in the cited upstream construction.
The AC route also retains **TU10**, and **E1** must supply the admissible cutoff sequence.
These are the open inputs recorded in `s4-s6.md`, Section 8, and `ac-port.md`, Section 7.
This note neither proves their availability nor gives a counterexample to them.

## Result

**Given the named component inputs, the construction proves O11 in four dimensions as a conditional research theorem.**
For each component it gives a separable positive Hilbert space, a common dense field domain,
a Hermitian scalar field, tempered vacuum distributions, Poincaré covariance, the forward spectrum, locality, and a unique cyclic vacuum.
Its Euclidean continuation equals the supplied \(\operatorname{tr}F^2\) action-density hierarchy on separated and diagonal-flat tests.
This reconstructs that scalar sector; it does not construct a gauge potential or specify Euclidean contact terms.
Nontriviality still requires the separate ultraviolet input.
The proof rebuilds the Sussman–Alpoge direct method credited in Section 1, with OS II credited for reconstruction.
Every deduction above is by hand. Proved here by Codex, not yet checked by the other model.
The upstream inputs remain open; this is not an unconditional proof of T0 and grants no status.
