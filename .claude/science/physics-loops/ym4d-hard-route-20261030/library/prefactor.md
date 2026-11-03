# The finite two-step Gaussian prefactor
Provenance: Codex (GPT-6 family; queue requests max effort; runtime variant and effort are not exposed); checkout `1b0c7afaf3f1c23037c9ba7f0bc40ce177c5ac63`; Sussman–Alpoge `31a47c543775`. Research text, not an audit; grants no status.

## 1. Question and sources

This note tests row 151, rank 9: does P1's composite prefactor give B3's designated Gaussian coefficient?
The finite identity must precede any estimate uniform in scale or volume.
Equality with the expected numerical coefficient would not answer this question.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text.
Their outline supplies B3, RF8–RF12 and the saddle-determinant route (lines 3986, 20304–20440, 21064 onward).
P1 means `parts/hard-core--mapped.md`, Text 3, especially Lemma 3.2 and its standing note.
The prior P1 check leaves the designated-prefactor identification open.
Balaban's effective-action expansion supplies the comparison of quadratic terms; all identities used below are re-proved.
No mathematical step depends on a computation or a reported numerical check.

## 2. The formula without constraint curvature is false

Here is a diagnostic example, not a Yang–Mills counterexample.
Take \(S(x,y,z)=(x^2+y^2+z^2)/2\),
\(F(x,y,z)=(y+x^2/2,z)\), and \(H(v,w)=v\).
At final datum \(s\), \(|s|<1/2\), the critical point is \((0,s,0)\).
Eliminating the delta gives
\[
 S(x,s-x^2/2,z)=s^2/2+(1-s)x^2/2+x^4/8+z^2/2.
\]
Thus its Gaussian prefactor is \(2\pi/\sqrt{1-s}\).
Restricting the unconstrained Hessian gives \(2\pi\), incorrectly.
The missing logarithm is \(-\tfrac12\log(1-s)\); its second derivative at zero is \(1/2\).
The multiplier is \(s\), and the missing Hessian term is \(-sD^2(HF)\).
Likewise, \(\delta(c(s)x)=|c(s)|^{-1}\delta(x)\) retains a field-dependent factor.
Vacuum subtraction removes neither error.

## 3. The actual finite problem and its normalisations

Take a fixed periodic lattice with odd block side \(L\) and two nested blocking levels.
Use at least three final blocks in each direction, so each block is contractible.
Write \(X_i=SU(2)^{E_i}\), with normalized product Haar measures \(dU_i\).
The action is \(S(U)=\sum_p(1-\tfrac12\operatorname{tr}U_p)\).
Use the outline's actual symmetric contour map, R3:
\[
 \mathcal M(U)(c)=
 \exp\!\left\{L^{-4}\sum_{x\in B(c_-)}
 \log[U(c_-,x)U([x,x'])U(x',c_+)U[c]^{-1}]\right\}U[c].       \tag{1}
\]
The contour transport is the small mean satisfying \(\sum_i\log(V_iV^{-1})=0\).
Set \(F=\mathcal M_{01}\), \(H=\mathcal M_{12}\).
Equation (1) is Balaban CMP 109 (0.12).
P1's reference to (0.4) supplies the same vacuum first derivative, not an interchangeable nonlinear map.
At the vacuum, differentiating a path sums its links; differentiating either mean averages those sums.
Every derivative below is of (1), including its contour means.

Here are exact gauge and measure conventions.
For each level, retain gauge values equal to one at the next level's nodes.
Let \(T_{yx}(U)\) be the contour mean from its block node \(y\) to \(x\).
Put \(w(V)=1-\tfrac12\operatorname{tr}V\), and fix a conjugation-invariant cutoff \(\chi=1\) near one.
Use the same cutoff in the numerator and normalizer, as in Balaban's insertion:
\[
 G_{01}(U)=\sum_{x\notin N_1}w(T_{yx}(U)),\quad
 G_{12}(V)=\sum_{x\in N_1\setminus N_2}w(T_{yx}(V)),\quad
 z_g=\int_{SU(2)}\chi(h)e^{-w(h)/g^2}\,dh.                 \tag{2}
\]
The numerator also contains \(\prod_x\chi(T_{yx})\).
This is the normalized exponential gauge insertion of CMP 109 (0.14)–(0.16), with gauge parameter \(g^2\).
Indeed \(T_{yx}(U^h)=T_{yx}(U)h(x)^{-1}\) when \(h(y)=1\).
Haar translation in each independent \(h(x)\) gives
\(z_g^{-r}\int dh\,\prod_x\chi(T_{yx}(U^h))e^{-G(U^h)/g^2}=1\), with \(r\) the number of those vertices.
Thus the two-step denominator is exactly \(z_g^{r_{01}+r_{12}}\).
No gauge volume or residual constant mode is suppressed.
The remaining node variables are prescribed data.

All coordinates are right-translation exponential coordinates centred at the field in question.
Let \(n_i=3|E_i|\), and let \(h_i(0)\) be their product Haar density at zero.
These densities are independent of the centre.
The exact local delta conversion is
\(\delta_{X_i}(e^b)=h_i(0)^{-1}\delta_{\mathbb R^{n_i}}(b)\).
Spacing changes are linear coordinate changes; their determinants belong in these densities and in the constraint rows.
One may instead use RF12a's weighted orthonormal coordinates throughout, with the identical change-of-variables formula.

For completeness, the relevant critical branch exists near the trivial datum on this fixed geometry.
The mean equation has the form \(Y=\overline Z+R(Z,Y)\), with \(DR(0,0)=0\).
On a small ball its right side contracts in \(Y\); the geometric iteration constructs the analytic mean.
The iterates converge uniformly on a smaller complex ball; Cauchy's integral formula passes to the limit there.
Thus (1) is analytic and gauge covariant, directly from products and conjugation of its logarithms.
At the vacuum, put a coarse bond variable on every fine link crossing its block face, and zero internally.
Every straight path in (1) crosses that face once; both internal contour transports are one.
This gives an exact right inverse of one average, and iteration gives one for \(HF\).
Hence both constraint derivatives are onto.

The vacuum Wilson Hessian is \(\|da\|^2\), by expanding each plaquette exponential to second order.
If this vanishes, path sums inside each block are independent of the path.
Backtracks cancel, and elementary plaquette moves exchange adjacent coordinate steps without changing the sum.
Zero gauge Hessian then makes all internal links zero.
The crossing plaquettes make crossing link variables constant on each face.
Repeat on the intermediate lattice: the final average detects every remaining face variable.
Thus the augmented Hessian is positive on the constraint kernel.
This also excludes torus holonomies in that kernel.
Compactness of its finite unit sphere gives a positive minimum; no uniform lower bound is asserted.
The saddle matrix is invertible: its null vector has zero constraint, hence zero quadratic norm, hence zero field component.
Surjectivity then kills its multiplier component.
For the nonlinear saddle equations write \(Kz+R(z)=(0,b)\), with \(DR(0)=0\).
Choose a ball where \(\|K^{-1}DR\|<1/2\).
Iteration of \(z=K^{-1}(0,b)-K^{-1}R(z)\) gives the unique nearby branch and its derivatives.
Continuity preserves positivity on its fibres.
Along the residual orbit the gauge coordinates in (2) can be set to one exactly.
Hence this augmented branch represents the physical constrained branch, with \(G_{01}=G_{12}=0\).
This rebuilds the fixed-geometry argument of `a1-orbit`, Section 5; it claims no uniform A1 theorem.

## 4. Exact integration in stages, with curvature

Centre coordinates at the actual branch \(u=u(v)\), \(v=p(z)\).
In these coordinates \(F(0)=H(0)=0\); write \(A=DF\), \(B=DH\), and \(R=Du\).
Set \(\widetilde S=S+G_{01}\), \(S_1(v)=\widetilde S(u(v))\).
The multiplier equations and their derivatives give
\[
 \widetilde S'=A^T\lambda,\quad S_1'=\lambda=B^T\mu,\quad AR=1,
 \qquad
 T_1=\widetilde S''-\lambda\cdot F'',\quad
 T_1R=A^TS_1'',\quad R^TT_1R=S_1''.                         \tag{3}
\]
Here \(G_{12}'=0\) at the chosen representative.
For example, differentiate \(\widetilde S'(u(v))=DF(u(v))^T\lambda(v)\).
Moving the differentiated \(DF\) term to the left gives the middle identity in (3).
The envelope identity \(S_1'=\lambda\) follows from \(AR=1\).
Thus no assumption that the ambient Wilson Hessian is positive has entered.

The next and composite constrained Hessians are
\[
 \begin{split}
 T_2&=S_1''+G_{12}''-\mu\cdot H'',\\
 T_{02}&=D^2(\widetilde S+G_{12}\circ F)-\mu\cdot D^2(H\circ F)\\
       &=T_1+A^T(G_{12}''-\mu\cdot H'')A.                  \tag{4}
 \end{split}
\]
The second equality uses
\(D^2(HF)[a,a]=H''[Aa,Aa]+B F''[a,a]\) and \(\lambda=B^T\mu\).
This is the required moving-constraint term for the actual two-fold map.

Define the unnormalized Gaussian number and saddle matrix by
\[
 \mathcal G(T,M)=\int_{\mathbb R^n}\delta(Ma)e^{-a^TTa/2}\,da,
 \qquad \mathbb S(T,M)=\begin{pmatrix}T&M^T\\M&0\end{pmatrix}.
\]
If \(M\) is onto and \(T>0\) on \(\ker M\), then
\[
 \mathcal G(T,M)=(2\pi)^{(n-m)/2}|\det\mathbb S(T,M)|^{-1/2}.
                                                                    \tag{5}
\]
To prove this, choose orthonormal bases \(N,W\) of \(\ker M\) and its complement.
The delta eliminates the \(W\) coordinates with factor \(|\det MW|^{-1}\).
Diagonalizing the positive matrix \(N^TTN\) gives its Gaussian factor.
Block elimination in the saddle matrix gives
\(|\det\mathbb S|=\det(N^TTN)\det(MW)^2\).
Indeed the remaining block \(\left[\begin{smallmatrix}D&C^T\\C&0\end{smallmatrix}\right]\)
has determinant \((-1)^m\det C^2\), independently of \(D\).
The one-dimensional Gaussian integral is \(\sqrt{2\pi}\): square it and use polar coordinates.
These facts prove (5), including its delta normalization.

Now write uniquely \(a=n+Rb\), with \(n\in\ker A\).
Its volume element is
\(da=\det(AA^T)^{-1/2}\,dn\,db\).
To check this, replace \(R\) by \(A^T(AA^T)^{-1}\).
The change is a shear in \(\ker A\), with determinant one.
The orthogonal right inverse has precisely the displayed volume factor.
Equations (3)–(4) give
\[
 a^TT_{02}a=n^TT_1n+b^TT_2b,\qquad BAa=Bb.
\]
Consequently, with every power of \(2\pi\) retained,
\[
 \boxed{\mathcal G(T_{02},BA)=\mathcal G(T_1,A)\mathcal G(T_2,B).}       \tag{6}
\]
Both integrations converge by fibre positivity.
This proof never introduces an inverse of an indefinite Wilson Hessian.

The Haar and gauge constants also compose exactly.
For \(U=\exp(i a\cdot\sigma)\), normalized Haar density is
\(h_0(\sin|a|/|a|)^2\), where \(h_0=(2\pi^2)^{-1}\).
Indeed \(4\pi\int_0^\pi\sin^2r\,dr=2\pi^2\).
Thus \(h_i(0)=h_0^{|E_i|}\) and
\(z_g=h_0(2\pi g^2)^{3/2}(1+o(1))\).
For a step \(i\to j\), put
\[
 d_{ij}=n_i-n_j-3r_{ij},\qquad
 P_{ij}=h_0^{|E_i|-|E_j|-r_{ij}}
        (2\pi)^{d_{ij}/2}|\det\mathbb S(T_{ij},M_{ij})|^{-1/2}.        \tag{7}
\]
Its local saddle contribution is \(e^{-S_*/g^2}g^{d_{ij}}P_{ij}(1+o(1))\).
To see this directly, solve the constraint in complementary coordinates and put the tangent variables equal to \(g\xi\).
The constrained action has a positive quadratic term and an \(O(|g\xi|^3)\) remainder.
On a sufficiently small fixed chart its excess is at least \(c g^2|\xi|^2\).
The rescaled density therefore has an integrable Gaussian majorant and converges to (5).
Outside a smaller saddle neighbourhood the local action excess has a positive minimum.
Its contribution is exponentially smaller.
Haar density tends to its centre value; the delta contributes the reciprocal target density.
Division by the exact \(z_g\) factors proves (7).
The same argument proves the displayed asymptotic for \(z_g\).
This is a local saddle statement, not an assertion about unspecified remote saddles or a global extension of (1).

Since \(r_{02}=r_{01}+r_{12}\), equation (6) gives
\[
                         P_{02}(z)=P_{01}(p(z))P_{12}(z).             \tag{8}
\]
The intermediate Haar density cancels; the gauge normalization powers add.
Alternatively, the Haar delta identity
\(\int dV\,\delta(HV\,z^{-1})\delta(FU\,V^{-1})=\delta(HFU\,z^{-1})\)
proves that both saddle calculations concern the same integral.
The smooth amplitude \(P_{01}(V)\) takes its value at \(p(z)\) at Gaussian order.
Its derivatives enter higher orders in \(g\), not (8).

## 5. Which prefactor and which coefficient

Equations (3)–(8) use Balaban's designated quadratic part before coupling-counterterm subtraction.
CMP 109 (1.4) defines \(Z^{(j)}\) by its Gaussian integral with the linear delta retained.
Equation (1.5) includes
\(-2\langle H_{1,j}hC^{(2)}(B),J\rangle\), as well as the gauge quadratic form.
Here \(C^{(2)}\) is the quadratic term of the nonlinear constraint.
CMP 109 (2.11)–(2.14) separates this Gaussian from the remainder.
CMP 119 (3.33) retains the pivot factor:
\(\log Z=\sum_c\log z(c)-\tfrac12\log\det(C^TTC)+\text{constant}\).
These formulas were read on the scanned pages, not inferred from damaged OCR.
CMP 116 is absent from `~/ym4d-papers`; no claim from it is used.

Here is the direct reconstruction of those statements.
Write the actual constraint as \(Aa+C^{(2)}(a)+O(|a|^3)\), and choose \(Ah=1\).
For the full nonlinear remainder \(C\), solve \(D(b)=C(b-hD(b))\) by contraction near zero.
It has \(D(b)=C^{(2)}(b)+O(|b|^3)\).
The change \(a=b-hD(b)\) straightens the constraint exactly to \(Ab\).
Its derivative at zero is one.
Substitution in the action gives the quadratic term
\[
 \tfrac12 b^T\widetilde S''b-\langle\widetilde S',hC^{(2)}(b)\rangle
 =\tfrac12 b^T\widetilde S''b-\langle\lambda,C^{(2)}(b)\rangle
 =\tfrac12 b^TT_1b.                                      \tag{9}
\]
The same substitution into \(S_1+G_{12}\) gives \(T_2\).
Thus (9) supplies both the sign and the factor two in Balaban's formula.
After \(b=g\xi\), the cubic action remainder divided by \(g^2\) tends to zero.
The straightening Jacobian tends to one; Haar density tends to its field-independent centre value.
The Gaussian majorant from Section 4 justifies these limits on each fixed chart.
There is no omitted field-dependent term of order \(g^0\) in this finite split.

For an explicit pivot calculation write \(A=(A_p,A_f)\), with \(A_p\) square and invertible.
The delta sets \(b_p=-A_p^{-1}A_fb_f\), and contributes \(|\det A_p|^{-1}\).
Put \(Cb_f=(-A_p^{-1}A_fb_f,b_f)\).
Then
\[
 \mathcal G(T,A)=|\det A_p|^{-1}
 (2\pi)^{(n-m)/2}\det(C^TTC)^{-1/2}.                      \tag{10}
\]
This proves CMP 119's decomposition and identifies RF9's free-bond and pivot terms.
With those actual compressed matrices, RF9's finite sum telescopes by inclusion–exclusion.
For any proper subdomain, pairing supersets that differ by one missing cube cancels its coefficient.
Only the full-domain logarithm remains; this proves the finite sum rule without a decay estimate.
The factor \(C^TTC\) alone is not the prefactor.
Equation (10) also shows why changing the linear constraint's units must change its pivot factor.

A change of gauge cannot remove a determinant either.
On the physical tangent fibre let \(D\alpha\), \(\alpha\in\mathbb R^{d_G}\), parameterize residual gauges in Haar tangent coordinates.
The constrained Lagrangian Hessian vanishes on those directions, including mixed terms.
Indeed its first variation vanishes and its value is constant along each physical gauge orbit.
If \(LD\) is invertible, then
\[
 \frac{|\det LD|}{(2\pi)^{d_G/2}}
 \int_{\mathbb R^{d_G}}e^{-\|L(a+D\alpha)\|^2/2}\,d\alpha=1.         \tag{11}
\]
Translation followed by \(\beta=LD\alpha\) proves (11).
It proves equality of normalized Gaussian integrals in different gauges, with their Faddeev–Popov factors.
For the contour gauge these orbit coordinates are triangular along the two levels, with diagonal \(\pm1\).
Using a straightened average or a covariant gauge must also transform the constraint and its node factors.
Our formula keeps the plain map (1); it needs no unproved identification of a straightened map's second jet.

Define \(\Gamma_{02}=\log(P_{02}/P_{02}(1))\) and
\(\Phi_i=\log(Z_i/Z_i(1))\), where \(Z_1=\mathcal G(T_1,A)\), \(Z_2=\mathcal G(T_2,B)\).
Equations (9)–(10) identify these \(\Phi_i\) with RF8's designated Gaussian logarithms on this finite branch.
All constants in (7) cancel in these ratios, so (8) gives the functional identity
\[
                  \boxed{\Gamma_{02}=\Phi_2+\Phi_1\circ p.}          \tag{12}
\]
This is P1's composite prefactor with the necessary constrained Hessians.
It holds for all nearby data, not merely for a numerical flux coefficient.

To state its local content, fix the same finite domain, common lift and pointing convention on both sides.
PH18 extracts \(b_h[F]=\sum_u\pi^F_{h,\mu\nu}(u)u_\mu u_\nu\), \(\mu\ne\nu\).
Here \(\pi_h\) uses the average of the three diagonal color Hessians and the prescribed tent weights.
This is a linear contraction of the finite Hessian; additive constants vanish.
Constant color conjugation forces \(D\Phi_1(1)=0\): an invariant vector in the adjoint three-space is zero.
Writing \(R_0=Dp(1)\), differentiation of (12) therefore gives
\[
 b_h[\Gamma_{02}]=b_h[\Phi_2]
       +\mathcal L_h\!\left(R_0^TD^2\Phi_1(1)R_0\right),             \tag{13}
\]
where \(\mathcal L_h\) is that same PH18 contraction.
Thus the designated second-step coefficient is the difference in (13), with the actual averaging response retained.
For any admitted finite flux curve, differentiating (12) gives the corresponding identity as well.
An arbitrary volume-averaged flux derivative does not replace PH18.
In particular, continuous constant flux on a periodic torus is not an admissible shortcut.

## 6. Localisation: the remaining obstruction

The finite composition error in (12) is exactly zero.
The remaining error belongs to replacing its actual Hessian and response by P1's low-jet operators.
Also, (13) has not replaced its last term by \(b_h[\Phi_1]\).
That further step is the actual substitution/localisation requirement RF11a.
It needs affine-response matching, compatible boundary terms and Hessian moments for the very same localized Gaussian family.
RF9's finite inclusion–exclusion identity supplies a sum, not a bound on that sum's absolute moments.

The required derivatives are explicit, but finite invertibility does not bound them uniformly.
For the saddle matrix \(\mathbb K(t)=\mathbb S(T(t),M(t))\),
\[
 (\log Z)''=-\tfrac12\operatorname{Tr}
 \left(\mathbb K^{-1}\mathbb K''
       -\mathbb K^{-1}\mathbb K'\mathbb K^{-1}\mathbb K'\right).      \tag{14}
\]
Differentiate \(\mathbb K\mathbb K^{-1}=1\) and the determinant's multilinear expansion to obtain (14).
The derivatives include those of the multiplier, gauge terms and the full contour map.
The pivot derivative in (10) is already present in (14).
Neither the fixed-geometry contraction argument nor (14) bounds their spatial moments uniformly in depth.
For example, the positive scalar family \(\varepsilon+t^2\) gives
\(( -\tfrac12\log(\varepsilon+t^2))''_{t=0}=-1/\varepsilon\).
This shows the logical limitation of finite positivity; it is not a counterexample for the lattice operators.

No summable bound for the actual low-jet replacement error has been established here.
In particular, no bound \(\sum_j|e_j|<\infty\), or uniform partial-sum substitute, follows from the finite identity.
This does not prove that such a bound is impossible.
The low-jet alternative stops here. The outline's massive trace route stays, with its stated mixed-norm inputs still open.

## Result

Proved here by hand: the finite, near-vacuum two-step identity (12), and its exact local extraction (13).
Inputs are the Wilson action, R3's actual contour average, normalized Haar deltas, and the gauge insertion (2).
The finite critical branch and Gaussian algebra were rebuilt above.
Balaban CMP 109 (1.4)–(1.5), (2.11)–(2.14), and CMP 119 (3.33) identify the designated split, re-derived in (9)–(10).
There is no missing order-\(g^0\) remainder in that finite split.
Dropping constraint curvature or a pivot factor is invalid; Section 2 gives an explicit failure.

Rank 9 stops at the uniform localisation and substitution estimate needed to turn (13) into B3's bulk coefficient sequence.
The low-jet replacement has no proved summable error, and the nonlinear B3 bounds remain untouched.
No value of \(c_0\), full P1 theorem, or B3 theorem is proved here.
This proof has not been checked by the other model; it grants no scientific status.
