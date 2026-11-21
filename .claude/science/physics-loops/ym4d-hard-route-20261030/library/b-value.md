# b-value: the Gaussian value clause (row 166)
Provenance: OpenAI Codex (GPT-6; exact backend identifier unavailable), effort max requested; checkout `58151bb5439aa21a9e82a40373058b630ddbc73a`; Sussman–Alpoge `31a47c543775`. Research text, not an audit; grants no status.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, for R3, the straightened-average construction and RF10–RF14. Claude supplied `prefactor-loc.md`; Codex supplied `prefactor.md` and the P1 check. Balaban's CMP **109**, 249–301, and **119**, 243–285, supply the original determinant and extraction framework. All new arguments below are by hand.

## 1. Check of `prefactor-loc.md`

Lemmas A, B, D, Theorem S and Corollary T: **checked line by line by Codex; first failing step none**. Their constants may depend on fixed depth. They do not supply the uniform value estimate.

**Lemma B.** The face injection is a right inverse of each linear average, including on Bloch fibres. A null vector has zero curl and zero contour means. Write it as (d\chi) on the covering lattice. The contour conditions make \(\chi\) constant inside successive blocks. The final constraint makes the node values constant. Thus the vector vanishes. Surjectivity then removes the multiplier null vector. The determinant has no real zero. Compactness gives a complex strip at each fixed depth. Shifting the Fourier contour gives exponential decay. Absolute convergence proves periodisation and uniqueness on polynomially growing fields. No depth-independent strip follows.

**Lemma A.** The path average sends an affine field with constant \(a\) and slope \(C\) to one with constant \(La\) and slope \(L^2C\), modulo a gradient. Assigning \(\chi\) from the coarsest nodes down removes every contour mean and the final gradient error. The resulting field has constant curl. Hence its divergence of curl vanishes, and it solves the saddle equation with zero multiplier. Lemma B gives uniqueness. For a constant datum the response is periodic. The constraint equals \(L\) times its cell mean, so that mean is \(c/L\). These prove both response identities used by Theorem S.

**Lemma D.** Twice differentiating the finite saddle determinant gives
\[
 H(b,b')=-\tfrac12\operatorname{Tr}(K^{-1}K_{bb'})
 +\tfrac12\operatorname{Tr}(K^{-1}K_bK^{-1}K_{b'}).
\]
The first branch derivative is a column of the inverse saddle. Its second derivative is that inverse applied to a finite-range quadratic vertex. Exponential convolution therefore bounds both differentiated matrices and both traces. Periodised terms with nonzero winding vanish exponentially for fixed external bonds. Constant colour rotations kill the first variation. A coarse gauge change extends constantly inside each final block; it preserves every earlier gauge insertion. Differentiating this invariance kills gradients in the Hessian. To extend this identity to polynomial \(\chi\), truncate \(\chi\) at radius \(R\). Exponential tails dominate the polynomial boundary terms as \(R\to\infty\). Centred blocks and the reversed-path identity give the stated reflections. The chain rule then gives part (d).

**Theorem S.** The Ward identity first gives \(\widehat\pi(0)=0\). Its next derivative and symmetry make the first moment totally antisymmetric. Reflection of one of its three indices kills it. Thus \(\widehat\pi(q)=O(|q|^2)\). With the midpoint phases retained, the exact alias formula is
\[
 \widehat\pi^c(K)=L^4\sum_n
 \rho(-K,-n)^T\widehat\pi((K+2\pi n)/L)\rho(K,n).
\]
The zero alias has \(\rho(0,0)=L^{-1}I\), giving \(L^2\widehat\pi(K/L)+O(|K|^3)\). For each nonzero alias, affine reproduction makes its curl \(O(|K|^2)\). Divide by a nonzero component of the gradient symbol. The response is then a gradient plus \(O(|K|^2)\). Both gradient factors vanish against \(\widehat\pi\); this alias contributes \(O(|K|^4)\). There are finitely many aliases. Equality of the quadratic coefficients follows without a uniform remainder estimate.

**Corollary T.** Apply that equality to the Hessian of the exact finite identity
\(\Psi_l=\Phi_l+\Psi_{l-1}\circ p_l\), then take the fixed-depth bulk limit from Lemma D. Linearity gives
\[
 b_l^0=b[\Psi_l]-b[\Psi_{l-1}],\qquad
 \sum_{l=1}^k b_l^0=b[\Psi_k].                                      \tag{1}
\]
The RF8 identification remains conditional on existence of its localised family. If that family exists, its sum and decaying companion give the same bulk Hessian. Equation (1) itself needs no RF8 estimate. The exact substitution error is zero; finite-torus convergence rates can still depend on depth.

## 2. What the literature supplies

Use the massive route. It avoids P1's false higher-derivative estimate (E) and its massless scalar bracket.

The local copies of Balaban were read at CMP 109 (1.4)–(1.5), (2.10)–(2.14), (5.37)–(5.43), and CMP 119 (3.28)–(3.34). CMP 109, page 259, defers Theorem 2's perturbative proof to another paper. These passages do not prove the requested value bound.

Here are the identities used from them. If a constraint has expansion \(Aa+C^{(2)}(a)+O(a^3)\), choose \(Ah=1\). The substitution \(a=b-hC^{(2)}(b)+O(b^3)\) makes its quadratic action
\[
 \tfrac12 S''[b,b]-\langle S',hC^{(2)}(b)\rangle.
\]
Thus the Gaussian precision includes the constraint curvature. If pivot elimination gives \(a=Cb\) and Jacobian \(\prod_c z(c)\), direct Gaussian integration gives
\[
 \log Z=\sum_c\log z(c)-\tfrac12\log\det(C^TTC)+\text{constant}.
\]
This re-proves the designated split in both papers. In orthonormal coordinates with \(A=(0,A_1)\), the same integral equals
\((2\pi)^{(n-m)/2}|\det\mathbb S(T,A)|^{-1/2}\): eliminate the positive kernel block, then exchange the two remaining block columns. The remaining determinant is \((-1)^m\det(A_1)^2\). No inverse of the unconstrained \(T\) is required.

Balaban's coefficient extraction also follows directly. Exponential moments allow differentiation of \(\widehat\pi(p)=\sum_u\pi(u)e^{ip\cdot u}\). The Ward identity and reflections give its quadratic transverse tensor, as in Section 1. Therefore
\[
 b=-\partial_1\partial_2\widehat\pi_{12}(0)
   =\sum_u u_1u_2\pi_{12}(u).
\]
These are the literature inputs used below; their proofs above do not assign a value to \(b\).

## 3. Constant curvature and the gauge determinant

Put \(\eta=L^{-k}\), and use level-\(k\) length units. Give the 12-plane curvature \(f t_3\), with \(\tfrac12\operatorname{tr}t_3^2=1\). A fine plaquette then has angle \(f\eta^2\). All differentiations below occur at \(f=0\), at fixed \(k\), before volume limits.

The symmetric contour mean of an affine Abelian potential equals its straight-line integral. Indeed, reversing a coordinate order reverses each enclosed signed area. In R3, the remaining loop area is linear in the displacement from the block centre. Its block mean is zero. Thus every iterate gives the same constant curvature in its own units. The Wilson current vanishes: each bond sees two opposite plaquettes with the same sine. The multiplier vanishes too. Consequently constraint curvature contributes zero on this family.

Use this field through its first two jets at zero flux. Fix the contour gauge successively from the coarse nodes down. The resulting jets grow polynomially and solve the differentiated saddle equations. Lemma B gives uniqueness on polynomially growing fields. Thus they equal the bulk branch jets obtained from the finite-torus kernels. This does not require a nonzero constant flux on a periodic torus, or a bounded affine potential on the infinite lattice.

The constant-curvature second derivative per coarse cell reads \(b[\Psi_k]\). Here is the local justification. At fixed depth, the inverse kernels decay exponentially. Resolvent integrals for each positive determinant below give local, gauge-invariant trace densities with exponential derivative moments. In a cube, fix a spanning tree and express each remaining bond by plaquette curls along a filling surface. A path has length \(O(r)\), and such a surface has \(O(r^2)\) plaquettes. These polynomial factors preserve exponential summability. Thus the quadratic density factors through two curls. Its zero-momentum curl tensor gives both the small-momentum Hessian and its value at constant curl. Reflections remove different-plane entries; coordinate permutations identify the diagonal entries. With action density \(f^2/2+O(f^4)\), its second derivative is precisely the second moment defining \(b\).

For completeness, retain the gauge Jacobian. Let \(N\) restrict site fields to final nodes. Write the linear straightening as
\[
 Q=Q^{\rm pl}+D_c\Phi,\qquad R=N+\Phi D,
 \qquad QD=D_cR.
\]
Introduce a coarse site variable \(\nu\) and the constraint \(Q^{\rm pl}a-D_c\nu=0\). Its gauge action is \((a,\nu)\mapsto(a+D\lambda,\nu+N\lambda)\). The shear \(\nu'=\nu+\Phi a\) has Jacobian one. It changes the constraint to \(Qa-D_c\nu'=0\), and the gauge action on \(\nu'\) to \(R\lambda\). The action Hessian kills \(D\), since the background is stationary.

To identify \(R\), differentiate the averaged gauge transformation
\(v(y)\exp\{L^{-4}\sum_x\log[v(y)^{-1}\operatorname{Ad}(U(y,x))v(x)]\}\)
at \(v=1\). The node term cancels. What remains is the mean of transported site fields. Iteration gives
\((R\lambda)(y)=\eta^4\sum_{x\in B^k(y)}T_{yx}\lambda(x)\),
where \(T_{yx}\) is the orthogonal transport along the unique tower of block centres. The blocks are disjoint. Thus
\((RR^T)_{yy'}=\delta_{yy'}\eta^4\sum_{x\in B^k(y)}T_{yx}T_{yx}^T=\delta_{yy'}\).
This identity also holds for the bilinear complex continuation. Put \(P=1-R^TR\) and \(\Delta=D^TD\). In the gauge \(\nu'=0\), use \(PD^Ta\) for the remaining gauge coordinates. Relative to \(\ker R\oplus\operatorname{ran}R^T\), their derivative in \(\lambda\) is triangular. Its determinant is \(\det(\Delta|_{\ker R})\). Here the restriction means compression as a quadratic form. The contour gauge has a triangular derivative with unit diagonal, up to field-independent volume factors. Replacing its delta functions by normalized Gaussians preserves the integral: change variables along the gauge orbit and integrate those gauge coordinates. This proves the linear Faddeev–Popov identity here, including the coarse displacement. Also
\(\det(\Delta|_{\ker R})=|\det\mathbb S(\Delta,R)|\), since \(RR^T=1\).

Define
\[
 K=\Delta^{\rm W}+DD^T,\quad X=K-DR^TRD^T,\quad
 \Xi=X+Q^TQ,\quad M=\Delta+R^TR.
\]
The preceding identity and the saddle calculation in Section 2 give, after vacuum subtraction,
\[
 \Psi_k=-\tfrac12\log\det\Xi
 -\tfrac12\log\det(Q\Xi^{-1}Q^T)
 +\log\det M+\log\det(RM^{-1}R^T).                         \tag{2}
\]
Adding \(Q^TQ\) to the saddle's upper block does not change its determinant: subtract the corresponding multiple of its constraint rows. Then take its Schur complement. The site formula follows by the same operation. All four matrices in (2) are positive at the vacuum. Their logarithms mean the branches there. No massless inverse of \(K\) occurs.

This uses the stationary constant-curvature case of RF12c, rather than its independent-current extension. It suffices for the coefficient. Box boundaries do not change that coefficient: centre the gauge at each trace density, then sum its exponentially decaying distance moments. The boundary contribution divided by volume tends to zero at fixed depth.

## 4. The uniform comparison: the norm issue

The following bounds concern constant-curvature jets only. They do not assert the full external-field strip estimate in the outline.

Use magnetic kernels based at bond midpoints. Remove the straight transport between their endpoints. Composing two such kernels restores the phase of their triangle. Expanding that phase gives, through charged flux degree two,
\[
 A\star B=AB-\tfrac{i\varphi}{2}\{A,B\}
             -\tfrac{\varphi^2}{8}\{\!\{A,B\}\!\},\qquad \varphi=2f.
                                                               \tag{3}
\]
Here \(\{A,B\}=A_1B_2-A_2B_1\), and
\(\{\!\{A,B\}\!\}=A_{11}B_{22}-2A_{12}B_{12}+A_{22}B_{11}\).
For matrix Bloch kernels these are displacement derivatives, including positions inside the cell. The formula follows from the triangle area, bilinear in the two displacements. Integration of a traced bracket is zero by integration by parts. Internal-position terms are commutators and have zero trace. Thus the integrated trace is cyclic for (3).

**Actual averages.** At scale \(s_i=L^{i-k}\), centre an Abelian gauge in the two blocks of one row. Every link and contour there depends analytically on \(f s_i^2\). The implicit contour mean is analytic: its equation has derivative minus the number of paths at the identity. The inverse function theorem therefore supplies a fixed disc, depending only on \(L\). Remove the two node factors before differentiating R3. At zero flux their derivatives cancel the contour terms, leaving the straight segment average.

Normalize forms in physical units. This average has coefficients \(L^{-5}\) for each pair consisting of a block site and a link on its length-\(L\) segment. There are \(L^5\) such pairs per row. Each fine link occurs in \(L\) pairs among all rows. The cell-volume ratio is \(L^4\). Thus both its row norm and weighted column norm equal one. Finite-dimensional analyticity now bounds the corresponding norms of its difference from the flat map by \(C_L|f|s_i^2\). This proves a bound on absolute coefficients, not only signed row sums.

The iterated derivative is the product of these straightened derivatives. Its support has diameter at most \(C_L\sum_i s_i\le C_L\). Triangle phases cost at most \(\exp(C_L|f|(\sum_i s_i)^2)\). Also
\(\prod_i(1+C_L|f|s_i^2)\le\exp(C_L|f|\sum_i s_i^2)\).
Both bounds are independent of \(k\). Apply the same argument to the transported site means. The straightened derivatives compose by the chain rule; their gauge variations compose to the site map just derived. Apply weighted Schur's inequality to the coefficients after removal of straight transport. Cauchy's formula in this fixed flux disc gives, for every fixed multiindex \(\alpha\),
\[
 \|\partial_p^\alpha\partial_f^jQ\|+
 \|\partial_p^\alpha\partial_f^jR\|\le C_{L,\alpha,j},
 \qquad j\le2.                                                \tag{4}
\]
Momentum derivatives multiply kernels by bounded displacements. The norms in (4) are those of the zero-flux Bloch jets. No bounded complex-flux operator on the whole infinite lattice is asserted. This proves (4) without a differentiated alias estimate or a separate factor for each level.

**Flat precision.** Here are details of the uniform gap needed below. Write the fine aliases as \(q=p+2\pi n\), with \(p\in[-\pi,\pi]^4\). The fine Laplacian obeys
\(c|q|^2\le\widehat\Delta(q)\le |q|^2\).
The representatives \(q\) lie in the fine Brillouin zone. Put
\(a_\eta(t)=\eta\sin(t/2)/\sin(\eta t/2)\), with the continuous value at zero. A geometric sum over the \(\eta^{-1}\) centred sites gives this ratio. Summing the straight segment gives one more ratio in its direction. Thus, up to midpoint phases,
\[
 R(q)=\prod_\nu a_\eta(q_\nu),\qquad
 Q_{\mu\mu}(q)=a_\eta(q_\mu)\prod_\nu a_\eta(q_\nu).
\]
For \(n=0\), each ratio has modulus at least \(2/\pi\), using \(\sin t\ge2t/\pi\) on \([0,\pi/2]\) and \(|\sin t|\le|t|\). Every other alias has \(|q|\ge\pi\). Hence
\[
 \|a\|\le C(\|\partial a\|+\|Qa\|),\qquad
 \Delta+R^TR\asymp\Delta+1.                                   \tag{5}
\]
For the first inequality, solve for the zero alias using its invertible \(Q\) symbol, and bound the other aliases by their gradient energy. The scalar proof is identical with \(R\).

It remains to control the removed part of the divergence. For \(p\ne0\), set
\[
 u=D^Ta=v+R^Tg,\quad v=Pu,\quad
 a=t+D\Delta^{-1}u,\quad D^Tt=0,\quad m=R\Delta^{-1}R^T.
\]
The same alias bounds give \(m\asymp|p|^{-2}\),
\(\|m^{-1}R\Delta^{-1}\|\le C\), and \(|D_c(p)|\asymp|p|\).
Indeed, the zero alias gives the lower bound on \(m\); all others have energy at least \(c\pi^2\). Since \(RR^T=1\), they give bounded tails in both \(m\) and \(R\Delta^{-2}R^T\). The latter is at most \(C|p|^{-4}\), proving the second bound.
Apply \(Q\) and use \(QD=D_cR\). Solving the resulting scalar equation gives
\[
 |g|\le C\bigl(|p|\|Qa\|+|p|\|Qt\|+\|v\|\bigr)
       \le C\bigl(\|Qa\|+\|da\|+\|v\|\bigr).
\]
The last inequality uses \(\|Q\|\le1\) at zero flux and
\(|p|\|t\|\le C\|dt\|=C\|da\|\). At \(p=0\), \(g=0\): the divergence has no zero mode, and \(R\) kills every nonzero alias there. The identity
\(\|\partial a\|^2=\|da\|^2+\|D^Ta\|^2\), together with (5), proves
\[
 cW^2\le\Xi_0\le CW^2,\qquad W=(K_0+1)^{1/2}.                \tag{6}
\]

**Mixed bounds.** Let \(E=Q^TQ-DR^TRD^T\), and interpolate
\(H_s=K+1+s(E-1)\), \(0\le s\le1\). Its flat precision is a convex combination of \(K_0+1\) and \(\Xi_0\), so (6) holds throughout. The Wilson stencil gives \(K_0=\Delta_0 I\), a bounded first flux coefficient, and a bounded second flux coefficient. Indeed, each flux derivative contributes a plaquette area \(\eta^2\), against the precision factor \(\eta^{-2}\). Momentum derivatives of the zero-flux stencil have order at most two. Consequently (4), \(\|DW^{-1}\|\le1\), and the product rule give
\[
 \|W^{-1}(\partial_p^\alpha\partial_f^jH_s)_0W^{-1}\|\le C,
 \qquad j\le2,                                                \tag{7}
\]
for every fixed \(\alpha\). To spell out the energy factors, \(D_0\) has midpoint symbol \(2i\eta^{-1}\sin(\eta q_\mu/2)\); its positive momentum derivatives are bounded. Its transport-removed symbol has no flux dependence. Every term from \(DR^TRD^T\) therefore has either \(DW^{-1}\), or a bounded differentiated \(D\), on each end. Every middle factor is bounded by (4). The Wilson stencil has coefficients \(\eta^{-2}\) times analytic functions of \(f\eta^2\); its first and second flux coefficients are respectively \(O(1)\) and \(O(\eta^2)\). This proves all the mixed bounds in (7). The site interpolation uses \(E=R^TR\) and \(W=(\Delta_0+1)^{1/2}\), with the same proof.

Differentiate the inverse equation using (3). Each inverse jet is a finite sum of inverse factors separated by differentiated precisions. Equations (6)–(7) show that each such jet has form \(W^{-1}BW^{-1}\), with \(\|B\|\le C\). For example, a bracket term is \(H_s^{-1}(\partial_1H_s)(\partial_2H_s^{-1})\), which has exactly these outer weights. Ordinary momentum derivatives obey the same inverse recursion. At flux degree two the product rule adds at most four momentum derivatives. This proves every mixed inverse bound used below. An imaginary momentum shift changes the weighted flat precision by \(O(|\operatorname{Im}p|)\), so these calculations hold on a common smaller strip. This supplies the distance moments used in (3).

Finally, both coarse covariances in (2) have eigenvalues between positive constants. For the lower bound, lift a coarse vector using only its zero alias, divided by the invertible zero-alias symbol of \(Q\), or of \(R\). Its energy cost is bounded, since \(|p|\le2\pi\). Cauchy–Schwarz in the precision form gives the claimed covariance lower bound. The upper bound follows from (4) and (6). Their inverse jets and logarithmic trace jets are therefore bounded in fixed dimension.

## 5. Stop the resolvent expansion after three inverses

Let \(G=(K+1)^{-1}\), \(B=E-1\), and let \(\tau\) denote trace per coarse cell. Integrating \(\partial_s\tau\log H_s=\tau(H_s^{-1}B)\) and using the inverse identity twice gives
\[
 \tau\log\Xi=\tau\log(K+1)+\tau(GB)-\tfrac12\tau(GBGB)
       +\int_0^1s^2\tau(GBGBH_s^{-1}B)\,ds.                  \tag{8}
\]
Products mean magnetic products when taking flux jets. The identity follows first in finite dimension; cyclicity from (3) preserves it for the bulk jets.

Terms containing \(E\) have bounded quadratic flux coefficient. Each Bloch fibre of \(E\), and each of its finitely many differentiated factors, has bounded rank. Equations (4) and (7) bound its energy-sandwiched norm. Cycle the energy weights in the trace; the remaining factors have bounded norms. The estimate \(|\operatorname{Tr}T|\le\operatorname{rank}(T)\|T\|\) then applies. This explains why a rank count alone would have been insufficient.

The remaining integral in (8) contains three inverse factors. Every differentiated inverse has bounded Schatten 3-norm, because
\[
 \|W^{-1}BW^{-1}\|_{\mathfrak S^3}
 \le\|B\|\|W^{-1}\|_{\mathfrak S^6}^2,
 \qquad
 \sum_n(1+c|p+2\pi n|^2)^{-3}\le C.                          \tag{9}
\]
For the last bound, the shell of radius \(m\) contains at most \(C(m+1)^3\) integer points. Its tail is bounded by \(C\sum_{m\ge1}m^{-3}\), which converges by integration. Hölder's trace inequality bounds each product of three inverse jets. Flux differentiation via (3) produces only finitely many such products and the finite-rank terms already bounded. Thus (8), through quadratic flux order, is
\[
 \tau\log\Xi=\tau\log(K+1)-\tau G-\tfrac12\tau G^2+O_{f^2}(1).
\]
Here \(O_{f^2}(1)\) means a second derivative at zero bounded independently of \(k\). The scalar interpolation gives the identical formula with \(K,Q,\Xi\) replaced by \(\Delta,R,M\). The coarse logarithms in (2) contribute another \(O_{f^2}(1)\).

All flux jets used here are actual derivatives at zero. At fixed depth, differentiated finite-volume inverse equations have a unique solution. In a gauge centred at a trace density, their insertions grow only polynomially in relative distances. Exponential decay makes these products absolutely summable. Taking the volume limit gives the infinite-kernel inverse equations. Expanding their triangle phases gives (3), hence the same uniquely determined jets. A sixth distance moment bounds the third-order phase remainder. Uniformity of the coefficients comes from (4)–(9), not from a complex-flux radius asserted uniform in volume.

Let \(\widetilde\beta(z)\) be RF13b's massive scalar-minus-half-vector second derivative on the unit bare lattice. Rescaling lengths gives the corresponding coarse-cell coefficient \(\widetilde\beta(\eta^2z)\): fine-site density \(\eta^{-4}\) cancels squared fine flux \(\eta^4\). Applying (8) to (2) therefore proves
\[
 b[\Psi_k]=\widetilde\beta(\eta^2)
 -\eta^2\widetilde\beta'(\eta^2)
 +\tfrac12\eta^4\widetilde\beta''(\eta^2)+e_k,
 \qquad |e_k|\le C_L.                                        \tag{10}
\]
This is the coefficient version of RF13's comparison. It does not claim the outline's stronger full external-momentum comparison.

## 6. The actual massive trace

Work on the unit bare lattice and put
\(\psi(q)=\sum_\mu(2-2\cos q_\mu)\), \(A=\psi+z\), and
\(I_m(z)=\int_{[-\pi,\pi]^4}A^{-m}\,dq/(2\pi)^4\).
Finite-range Wilson operators on the charged colours have magnetic symbol
\[
 K_\varphi(q)=\psi(q)I+\varphi S(q)+\varphi^2T(q)+O(\varphi^3),
\]
with smooth trigonometric coefficients. Its zero-flux value follows by expanding the plaquette action to the squared curl and adding \(DD^T\). The scalar symbol is exactly \(\psi\).

The spin constant needs no eigenvalue computation. Gauge invariance at this stationary field gives \(KD=D\Delta\). Its first flux coefficient, using (3), is
\(S(q)D_0(q)=i\{\psi,D_0\}(q)\).
Since \(D_0(q)=iq+O(|q|^2)\), its linear part says
\[
 S(0)(iq)=(2q_2,-2q_1,0,0),\qquad
 S(0)=\begin{pmatrix}0&-2i&0&0\\2i&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix}.
\]
Thus \(\operatorname{tr}S(q)^2=8+O(|q|)\); \(T\) is bounded.

Here is the numerator calculation. Solve the star-resolvent equation for a symbol \(\psi I+\varphi S+\varphi^2T\), at spectral mass \(z+s\). Its first two coefficients are
\[
 R_1=-S/(A+s)^2,\quad
 R_2=S^2/(A+s)^3-T/(A+s)^2
       -PI/(8(A+s)^3)+\widetilde P I/(4(A+s)^4),
\]
where
\[
 P=8\cos q_1\cos q_2,\qquad
 \widetilde P=8(\sin^2q_1\cos q_2+\sin^2q_2\cos q_1).
\]
The first-bracket cross terms cancel: \(\{R_1,A+s\}+\{(A+s)^{-1},S\}=0\). Integrating \(-R_2\) over \(s\ge0\) gives the logarithm coefficient
\[
 \operatorname{tr}(T/A-S^2/(2A^2))
       +d\bigl(P/(16A^2)-\widetilde P/(12A^3)\bigr).          \tag{11}
\]
For a scalar, set \(S=T=0,d=1\). Integration of
\(\partial_1(\sin q_1\cos q_2/A^2)\), and then its exchanged version, yields the exact orbital coefficient
\[
 u(z)=\tfrac16\int\cos q_1\cos q_2\,A^{-2}\frac{dq}{(2\pi)^4}
     =\tfrac16 I_2(z)+O(1).                                  \tag{12}
\]
For the vector, (11) gives \(v(z)=4u(z)-4I_2(z)+O(1)\). The remainders have mass-independent numerators bounded by
\(C(|q|A^{-2}+A^{-1})\), plus \(C|q|^2A^{-2}\) from (12). Their integrals are uniformly finite: near zero, use \(A\ge c|q|^2+z\) and radial measure \(Cr^3dr\). Multiplying one or two mass derivatives by \(z\) or \(z^2\) only adds bounded factors \(z/A\). Thus these remainder bounds include both scaled mass derivatives.

The neutral colour does have flux dependence, contrary to the sentence at SA line 21388. Its Wilson Hessian changes by
\(-\tfrac12f^2d_{12}^Td_{12}+O(f^4)\). Its contribution to the second derivative is
\(\tfrac12\int(\widehat q_1^2+\widehat q_2^2)A^{-1}dq/(2\pi)^4\).
It and its two scaled mass derivatives are bounded. It adds no logarithm.

Two real charged colours give \(2u-v\) in the determinant pair. Since \(\varphi=2f\), its second \(f\)-derivative is eight times that coefficient. Therefore
\[
 \widetilde\beta(z)=8(4-\tfrac13)I_2(z)+r(z),\qquad
 |r(z)|+|zr'(z)|+|z^2r''(z)|\le C.                            \tag{13}
\]
Finally, \(\psi(q)=|q|^2+O(|q|^4)\). Replacing it by \(|q|^2\) in a fixed small ball costs a bounded integral. The radial integral is
\[
 \frac1{8\pi^2}\int_0^\delta\frac{r^3\,dr}{(r^2+z)^2}
     =\frac1{16\pi^2}\log(1/z)+O(1).
\]
Outside the ball the denominator is bounded below. Also \(I_3\le C/z\) and \(I_4\le C/z^2\), by substituting \(r=\sqrt z\,t\). Equations (13) and these bounds prove
\[
 \widetilde\beta(z)=\frac{11}{6\pi^2}\log(1/z)+O(1),\qquad
 |z\widetilde\beta'(z)|+|z^2\widetilde\beta''(z)|\le C.         \tag{14}
\]
This is a lattice trace calculation with the stated momentum measure. Positive mass precedes the flux derivative and the volume limit throughout.

## 7. The value bound

**Theorem V.** Fix odd \(L\ge3\). For the Wilson SU(2) action, R3 iterate and contour gauge of Section 1, there is a finite \(c_2(L)\) such that
\[
 \left|b[\Psi_k]-k c_0\right|\le c_2(L),\qquad
 c_0=\frac{11}{3\pi^2}\log L,\qquad k\ge1.                  \tag{15}
\]
The coefficient is the bulk coefficient, with volume taken to infinity at each fixed depth.

Proof. Choose the one-step analytic disc first. It depends only on \(L\). Equations (4)–(7) then give constants independent of \(k\). Fix a smaller momentum strip using the flat coercivity constant in (6). The finite-rank bounds and (9) supply a constant \(C_E(L)\) for \(|e_k|\) in (10). Equation (14) supplies constants \(C_R,C_M\) such that
\[
 \left|\widetilde\beta(z)-\frac{11}{6\pi^2}\log(1/z)\right|
 \le C_R,
 \quad |z\widetilde\beta'(z)|+|z^2\widetilde\beta''(z)|\le C_M
 \quad(0<z\le1).
\]
Set \(z=\eta^2=L^{-2k}\) in (10). Its logarithmic term is \(k c_0\). The other terms have total absolute value at most \(C_E(L)+C_R+C_M\). This is a permitted choice of \(c_2(L)\). No limit in \(k\) enters this argument. ∎

Corollary T now gives RF10's first clause in its partial-sum form:
\[
 \left|\sum_{l=1}^k b_l^0-kc_0\right|\le c_2(L).
\]
Subtracting two partial sums also gives
\(\left|\sum_{l=i+1}^j(b_l^0-c_0)\right|\le2c_2(L)\).
This is the shifted bound needed by the flow arithmetic. The Gaussian construction contains no bare coupling, so neither does this coefficient sequence. Identification with a particular RF8 polymer family still requires that family's sum and companion properties, as specified in Section 1.

## 8. What remains for RF10 and B3

**RF10's second clause stays open.** Bounded partial sums do not imply convergence of the increments. The sequence \(b_l^0=c_0+a(-1)^l\), with \(a\ne0\), has bounded partial-sum error and successive differences of magnitude \(2|a|\). Thus (15) alone cannot prove \(|b_{l+1}^0-b_l^0|\le C_\alpha L^{-\alpha l}\). RF14 needs a comparison of the actual Taylor triples \(\mathfrak J_k=(\Delta_k,S_3^{(k)},S_4^{(k)})\). One must prove their geometric Cauchy bound in weighted norms and uniform continuity of the response and trace contractions in those norms. If the successive-difference bound is proved, its geometric tail gives convergence. The partial-sum bound then identifies the limit as \(c_0\).

**The nonlinear terms stay open.** For the actual step, B3 still needs
\[
 b_j=b_j^0+f_j+q_j,\qquad
 |f_j|\le Cx_{j-1}^{-1/2}(\log x_{j-1})^p,\qquad
 |q_j|\le Cx_{j-1}^{-(\kappa_0-4)/2},\quad\kappa_0>4.
\]
For \(f_j\), this requires bounds on the interacting fluctuation integral, the nonlinear substitutions, and the incoming regular families after coefficient extraction. Their derivative domains and local sums must remain uniform in depth and volume. The two-coupling gauge factor must also be shown to have zero coefficient, using its actual gauge splitting (RF15). A Gaussian value calculation supplies none of these bounds.

For \(q_j\), one must construct and estimate the remainder contribution in the same increment. The remainder norm must survive the field derivatives and polymer sums used by extraction, with the displayed power of \(x_{j-1}\). Uniform RF8 localisation and the identification of localized totals with the physical step remain separate requirements. The present calculation only needs the bulk Gaussian logarithm.

## Result

`prefactor-loc.md`, Lemmas A, B, D, Theorem S and Corollary T: **checked line by line by Codex; first failing step none**. Their fixed-depth conclusions stand.

**Theorem V is proved here by hand, not yet checked by the other model.** It gives \(|b[\Psi_k]-k c_0|\le c_2(L)\), hence RF10's first clause through exact telescoping. The massive comparison uses the actual straightened-average jets and retains the gauge determinant. The spin-sign correction leaves the trace of its square unchanged. The neutral Wilson colour contributes a bounded term, which is retained.

RF10's geometric increment bound, RF8's full localisation, and B3's nonlinear \(f_j,q_j\) estimates remain open. This is research text and grants no status.
