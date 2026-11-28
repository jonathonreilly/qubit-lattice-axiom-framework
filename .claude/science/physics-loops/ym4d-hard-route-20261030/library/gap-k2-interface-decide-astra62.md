# Repo search

**Checked sources.** At `f7e33266f` there is no target-specific prior file. The lead's [November 8 search](prior/repo-search-2026-11-08.md) covered main and PRs 10114, 10133, 10134 and 10141. I checked PR 10114, `MASS_GAP_LOCAL_BLOCK_ASTRA.md` 106–149. Its rank-one convolution estimate tests one spatial loop in a transfer kernel. Main's `research/mass-gap/library/gap-form-exercise.md` 139–145 concerns interpolation of twisted partition functions. Neither gives a norm on arbitrary probes of the summed matrices. An additional targeted search on the available refs for those four PRs, 10144 and main found no such test outside the hard-route folder. The [registry](open-registry.md) has no matching owner. The other local hits on `49/225` in the two RTailSOS notes use it as a squared coupling. Row [1485](gap-k2-wilson-interface-astra62.md) supplies the conditional laws (2), reflection comparison (6), bounds (8), (11), and polynomial transfer margin. Row [1475 §5](gap-k2-pivot-environment-astra62.md) gives the consumer. The decision about the sum, for the genuine tilted star, is the work here.

**Checked sources.** The [outline index](sa-index/README.md), its chunk and obligation rows, and the [CA-I index](sa-index/ca-4.12-4.19/README.md) were searched before using the source excerpts. Ethan Sussman and Levent Alpoge's outline and complete account, with Claude and Codex as authors of their text, are at `31a47c543775`. The outline defines the Wilson weight and proves finite normalization at 240–277, and states the additional observable identification needed after a mass-preserving transformation at 394–408. At 1310–1326 its connected-logarithm statement assumes the Kotecký–Preiss criterion. The “pivot matrix” at 27793–27799 acts on flat precision variables. CA-I 56439–56456 assumes the earlier-level representation and 56530–56539 uses a terminal ceiling for Bałaban's weak-coupling hypothesis. These passages provide context for a later join. The open-star test comes from row 1475. [Outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L240-L277) · [CA-I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L56530-L56539)

## Result at \(\beta=23/10\)

**Open.** For the summed Wilson matrices with the zero-transverse-corner pivots, the proved interval is
\[
 \frac{529}{2048}+4\,2^{-2024}<R=3p+3m+o_1
       \le 7-\frac{2966}{495}\,2^{-822}.
\]
Here \(p\) is the maximal correlation on two outgoing perpendicular faces, \(m\) on perpendicular faces of opposite signs, and \(o_1\) on an opposite pair. The new lower bound uses the single-crossing-link law. The upper endpoint and the positive lower bound on \(o_1\) come from 1485 (7), (13). The argument below bounds the whole polynomial-degree remainder at the positive rational weight of 1348. Its finite compression has not been certified below the required threshold. The partition-function trials of 1485 (12) cannot refute the test using only parameters outside \((3/10,2^{15})\). One explicit rational polynomial trial has a positive-row sum between \(6/25\) and \(97/100\) in that polynomial law. These statements are research by Codex for FINISH 1489 at `f7e33266f`, with no audit or change of status.

## The private links regularize the sum

**Proved.** Replace the ten entries of an observed symmetric matrix by the ten coefficients of the function that the matrix defines on unit quaternions, expanded in the constant and the nine entries of the adjoint rotation, and divide by the fixed factor \(12\beta\). This is an invertible linear change of coordinates by the Haar orthogonality used in 1485. In these coordinates the observation is the average of twelve vectors
\[
    V(a,b)=(a_0b_0,\boldsymbol a\boldsymbol b^t)
            \in\mathbb R\oplus\mathbb R^{3\times3}.
\]
Here \(a=A_{st}\) and \(b=r_sD_{st}r_t^{-1}\) in 1485 (1), using that face's source convention. Two perpendicular faces have four central edges in common. Choose the other eight edges on each face. For opposite faces choose any eight. Conditional on all remaining original links under product Haar, the two links at each chosen edge are independent Haar, and all sixteen chosen pairs are independent. Multiplication on the target side by the now fixed relative crossings preserves Haar. The two observations are thus translated independent sums of eight such increments in these coordinates. In particular one can condition on all raw reads of the other face while keeping eight pairs free. To use this fact under the polynomial Wilson law one must still include its density in the integral over those pairs.

**Proved.** The one-face support in these coordinates is exactly the convex body \(K=\{(s,M): |s|+\|M\|_*\le1\}\), with nuclear norm equal to the sum of the singular values. For one increment the inequality follows from the two-dimensional scalar product of \((|a_0|,|\boldsymbol a|)\) with \((|b_0|,|\boldsymbol b|)\). Conversely a scalar \(s\) and a rank-one block of size \(r\ge0\) are attainable whenever \(|s|+r\le1\). For \(s\ge0\) take \(\alpha,\gamma\in[0,\pi/2]\) with \(\alpha+\gamma=\arccos(s-r)\) and \(\alpha-\gamma=\arccos(s+r)\). The sum of these two arccosines is at most \(\pi\) since \(s\ge0\). Set the imaginary directions to the prescribed two axes and use scalar parts \(\cos\alpha,\cos\gamma\). Changing one scalar sign gives negative \(s\). For a general \(M=U\Lambda V^t\), take the four sign vectors \((+++),(+--),(-+-),(--+)\). Their mean outer product is the identity. The four rank-one blocks \((U\sqrt\Lambda\sigma)(V\sqrt\Lambda\sigma)^t\) all have size \(\operatorname{tr}\Lambda\) and average to \(M\). Repeat this list three times using scalar \(s\) in every term. Fixing the crossings, arbitrary tangential pairs can be realized, and positive continuous weighting preserves the image as support. The same argument includes singular \(M\) and the boundary. This describes the *sum* itself.

## An exclusion for the partition-function trial

**Proved for the Wilson weight.** Set \(A_t(X)=L_i^{(t)}(X)/L_i^{(0)}\), using the crossing coupling \(t\beta\) of 1485 (12). At zero crossing coupling keep the neighbour's full internal Wilson action. Even at fixed central and neighbour links, the twelve cut traces under the eight independent Haar crossings have mean zero, variance \(1/4\) each, and pairwise covariance zero. In a single edge integral an endpoint crossing makes the plaquette Haar. Two different edges have a leaf each or can be integrated from the leaves of their two-edge tree. Multiplying the crossings on one bipartite class by \(-1\) reverses the entire sum \(S\). Thus \(A_t=A_{-t}\), \(A_0=1\), and \(\mathbb E_0 S^2=3\) even before averaging the neighbour. Since \(x\mapsto\cosh(\beta\sqrt{x})\) has a nonnegative power series in \(x\), Jensen gives the uniform pointwise estimate
\[
      A_1(X)\ge\cosh(\beta\sqrt3)>25 .
\]
For the last inequality \(3\beta^2=1587/100>63/4\). The sum of the terms of orders zero through eight in the hyperbolic cosine at squared argument \(63/4\) exceeds 25 by rational arithmetic.

**Proved.** For the quotient in 1485 (12), with the second-moment *upper bound in its denominator*, put \(F_t=A_t/A_1\). Each of the seven trial lower bounds is at most
\[
      \sup_X\frac{A_t(X)^2}{A_1(X) A_{2t-1}(X)} .
\]
Indeed its numerator is \(|\operatorname{Cov}(F_t(X_i),F_t(X_j))|\le\operatorname{Var}(F_t)\) by the identical one-face marginals. Its denominator is \(\mathbb E F_{2t-1}-(\mathbb E F_t)^2\). If the displayed supremum is \(k\), then \(\mathbb E F_t^2\le k\mathbb E F_{2t-1}\), and \(k\le1\) by Cauchy–Schwarz before integrating the arm. For \(t\ne1\) the denominator is strictly positive since the cut sum varies on open sets of Haar configurations.

**Proved.** For every \(t\le0\), write \(v=-t\). Log convexity gives \(A_v^2\le A_{2v}\) and \(A_{2v+1}/A_{2v}\ge A_1\), by monotonicity of unit secants of \(\log A\). The supremum is at most \(1/625\). For \(0\le t\le1/6\), \(A_t\le A_1^t\) and \(A_{2t-1}\ge1\), so it is at most \(25^{-2/3}<1/8\), as \(25^2>8^3\). In particular choosing parameters from \(( -\infty,1/6]\) for the seven equal-parameter pair tests in (12) cannot give a refutation. At \(t=0\) the sum of those seven lower bounds is at most \(7/625\). This excludes the *partition-ratio certificate* in this range. The actual variance of the spectral probe can give a larger lower bound.

## A stronger lower bound in the Wilson star

**Definitions from 1485.** Write \(X\) for the 32 links of the central two-site-per-direction box. Conditional on \(X\), its eight arms are independent. Here \(q(U)=\operatorname{Re}\operatorname{tr}(U)/2\), \(S_i^{\rm cut}\) sums the twelve cut traces, \(T_i=\operatorname{tr}Q_i/(4\beta)\) and \(K_iF=\mathbb E[F(Q_i)\mid X]\). With \(x(v)=v^tQ_i v\) the probe used below is
\[
   \Phi_i=T_i-\frac{\int x(v)e^{x(v)}\,dv}{4\beta\int e^{x(v)}\,dv}.
\]
The fixed-plane variable on a shared square is \(Y=\sum_{e\subset\square}(q(A_e)^2-1/4)\), summed over its four edges. These definitions use the tilted star unless a different weight is specified.

**Proved.** In 1485 (9)–(10) write \(c\) for one cut plaquette trace. That argument gives \(p\ge (\mathbb E c)^2/(2+\mathbb E c^2)\) using the actual probe \(\Phi\) on the sum. A crossing link of this plaquette occurs in exactly three plaquettes. Conditional on every other link its quaternion \(u\) has density proportional to \(e^{h\cdot u}\) on \(S^3\), with \(t=|h|\le3\beta\), and \(c=d\cdot u\) for a fixed unit \(d\). Write \(r_1(t)=I_2(t)/I_1(t)\) for the mean axial coordinate at positive field. The eigenvalues of its uncentred second-moment matrix are \(1-3r_1(t)/t\) along the field and \(r_1(t)/t\) on the other three axes. Indeed the scalar density along the axis is proportional to \(e^{tx}\sqrt{1-x^2}\). Integrating the derivative of \(e^{tx}(1-x^2)^{3/2}\) gives \(t\mathbb E(1-x^2)=3\mathbb E x=3r_1(t)\). At zero field all four entries are \(1/4\). The recurrence for the positive Bessel coefficients gives \(r_1(t)/t\le1/4\), so the axial eigenvalue is largest.

**Proved.** Put \(x=t^2\). Successive uses of the same recurrence, starting with \(0<I_5/I_4<t/10\) in the expression for \(I_4/I_3\), give
\[
 \frac{t}{r_1(t)}<4+\frac{x}{6+x/(8+x/10)}.
\]
For \(0<x\le(69/10)^2<48\), the fraction on the right is below five precisely when \(x^2<2400\). Hence \(\mathbb E c^2<2/3\). At \(t=23/10\) that same right-hand side is below \(24/5\). The reflected electric estimate of 1485 gives \(\mathbb E c\ge r_1(23/10)>23/48\). Substitution yields
\[
       R\ge3p>\frac98\left(\frac{23}{48}\right)^2
                 =\frac{529}{2048}>\frac14 .
\]
The strict positive contributions from the other four coefficients can also be retained using 1485 (13). This tightens the lower endpoint using the previous spectral statistic. It leaves room on both sides of one.

## Which partition-function trials remain

**Proved, fourth Haar moment of the cut.** The preceding one-link second-moment bound applies also to a plaquette in the isolated neighbour at zero crossing coupling, since one of its tangential links belongs to three internal plaquettes. In particular its mean trace has absolute value below \(5/6\). For fixed central and neighbour tangential arrays \(A,D\), integration over the eight Haar crossings gives the exact identity
\[
  \mathbb E_u S^4=\frac{105}{4}
         +\frac38\sum_{\square\subset F} q(A_\square)q(D_\square).
\]
In the fourth power, odd incidence at any site vanishes by the independent crossing sign there. Single-edge fourth moments contribute \(12/8\), and pairs of squared edges give \(6\binom{12}{2}/16\) by the forest integrals. Four distinct surviving edges form one of the six squares. Write each edge term as \(\langle u_t,A_{st}^{-1}u_sD_{st}\rangle\). Its cycle integral is \(4^{-4}\) times the real trace of the product of the four orthogonal edge maps, transposing for backward traversal. Left and right quaternion multiplication give that trace as \(4q(A_\square)q(D_\square)\). This also follows by summing conjugations by \(1,i,j,k\) on a quaternion, which keeps only four times its scalar part. The four-edge ordering multiplicity is 24.

After integrating the isolated neighbour, \(\mathbb E_0 S^4\ge195/8\) uniformly in central \(A\), and \(\mathbb E_0 S^2=3\). The moments \(\mathbb E_0 S^{2k}\) are log convex by Cauchy–Schwarz, hence at least \(3(65/8)^{k-1}\) for \(k\ge1\). The first ten nonconstant terms of the even exponential series already give
\[
 A_1\ge 1+\frac{24}{65}\sum_{k=1}^{10}
          \frac{[(23/10)^2(65/8)]^k}{(2k)!}>130.
\]
Consequently the (12) quotient is at most \(1/16900\) for \(t\le0\), and for \(0\le t\le3/10\) it is at most \(130^{-2/5}<1/7\) since \(130^2>7^5\). All these estimates include the other seven arms in the marginal over the central array.

**Proved, large parameters.** Write \(z(x)=\int e^{xq(g)}dg\). With \(f\) the normalized tangential density of an isolated neighbour, one has \(A_t(A)=z(t\beta)^{12}(C_{t\beta} f)(A)\), where \(C_x\) is the product of twelve normalized one-link convolutions. This is 1348's two-slice integral. More explicitly \(f\) is proportional to \(W(C_\beta W)\), with \(W\) the product of the six spatial plaquette weights of a three-cube. Gauge fixing the eight normal edges of the open box gives this formula, and \(\sup f/\inf f\le e^{24\beta}\) since each of the two factors ranges between \(e^{-6\beta}\) and \(e^{6\beta}\). For \(x\ge1\) axial integration with \(v=1-q\) gives
\[
   \frac{e^x}{9x^{3/2}}\le z(x)\le\frac{e^x}{x^{3/2}}.
\]
For the lower bound integrate \(e^{-xv}\sqrt{v(2-v)}\) on \([0,1/x]\) with factor \(2/\pi\), using \(e<3\) and \(\pi<4\). For the upper bound replace the square root by \(\sqrt{2v}\) and integrate to infinity, giving coefficient \(\sqrt{2/\pi}<1\). For \(t\ge1\), \(z(\beta)\ge1\) and \(\beta>2\), so \(z(t\beta)^2/[z(\beta)z((2t-1)\beta)]\le9e^\beta t^{-3/2}<2^8t^{-3/2}\), using \(e^\beta<e^3<27\). Since every normalized convolution takes values between \(\inf f\) and \(\sup f\), the supremum bounding (12) is then at most \(e^{48\beta}2^{96}t^{-18}<2^{262}t^{-18}\), using \(e^2<8\). For \(t\ge2^{15}\) this is at most \(1/256\). In particular a refutation using just the displayed ratios of 1485 (12) must use a parameter strictly between \(3/10\) and \(2^{15}\) in at least one pair.

**Proved, scope of the electric comparison.** The sharper Wilson bound also gives \(p>529/6144>1/12\). Row 1348 (6)–(7) gives \(r_1(\beta)^4<(49/100)^4<1/16\) for the centred neutral operator between the *two endpoint arrays* with the crossing rotations integrated. Applying this very small number directly to \(p\) would contradict the preceding lower bound. The observation here retains the summed matrix before the pivot is integrated, and the central box is tilted by all eight arms. The GL3–GL4 one-bond inputs are due to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. [1348](gap-blockstep3-astra62.md) · [Outline, GL3–GL4](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2197-L2239)

## A polynomial trial with a certified row on the full star

**Proved, a uniform pivot variance.** For any real symmetric \(4\times4\) matrix \(Q\), give a unit quaternion \(v\) the density proportional to \(e^{v^tQv}\). Then \(\operatorname{Var}(v^tQv)\le10\). Choose a unit top eigenvector \(e\) and write the energy below the top as \(a u\), where \(u=1-(v\cdot e)^2\), and \(a\ge0\) depends only on the unit direction perpendicular to \(e\). Under Haar, \(u\) has beta parameters \(3/2,1/2\) independently of that direction, by the axial density. At fixed direction the tilt is proportional to \(e^{-a u}\). To prove \(\mathbb E[(a u)^2 e^{-a u}]\le10\mathbb E[e^{-a u}]\) for the bare beta variable, multiply by \(e^a\) and compare the positive power series. For order \(k\ge2\) the ratio of coefficients is
\[
   \frac{k(k-1)\mathbb E[u^2(1-u)^{k-2}]}{\mathbb E[(1-u)^k]}
   =\frac{15 k(k-1)}{(2k-3)(2k-1)}\le10.
\]
The beta integrals follow by integration by parts. The cross-multiplied difference is \(5(5k-3)(k-2)\), and the numerator vanishes at orders zero and one. Integrating the inequality over the perpendicular direction bounds the squared deviation from the top eigenvalue. Variance is smaller.

**Proved, an upper margin for 1485's score-corrected trace.** Write \(R_i^{\rm edge}=T_i-S_i^{\rm cut}/4\) for the variable projected to \(\Phi_i\) in 1485 (9), and \(\sigma^2=\operatorname{Var}\Phi_i\). For one outgoing edge write \(a,b\) for its central and transported remote quaternion and \(b_X=\mathbb E[b\mid X]\). Conditioning on all links except a crossing endpoint gives \(|b_X|^2\le2/3\) because the conditional mean of the transported quaternion has norm \(r_1(t)\), whose square is at most the axial second moment already bounded by \(2/3\). Take the conditional expectation again to obtain the assertion. The endpoint gauge rotations act on \(b_X\) as on \(a\), since its law is covariant. Averaging their common scalar coordinate over endpoint gauges gives the conditional-field edge contribution squared norm
\[
    \frac{1}{48}\mathbb E[2|b_X|^2+(a\cdot b_X)^2].
\]
Indeed the gauge average reduces to \((h\cdot a)(h\cdot b_X)-(a\cdot b_X)/4\) for uniform \(h\in S^3\), and the second and fourth moments are those of 1485 (10). The contributions on different edges are orthogonal by averaging a site in just one endpoint set. Since \(\mathbb E[(a\cdot b_X)^2]\le\mathbb E c^2\), comparison with the twelve unprojected edge variances in (10) gives
\[
  \operatorname{Var}(R_i^{\rm edge})-\|K_i\Phi_i\|_2^2\ge1/6.
\]
Conditioned on all internal links and relative crossings, only the pivot fluctuates in \(R_i^{\rm edge}\). Its conditional variance is at most \(10/(16\beta^2)\) by the preceding lemma. Thus \(1/2-10/(16\beta^2)\le\sigma^2\le2/3\). The three positive-pair covariances for this one probe total at most \(\|K_i\Phi_i\|^2\), by the shared-edge orthogonality in 1485 and nonnegativity by reflection. Every mixed and opposite correlation for this probe vanishes by its zero conditional field on an inward face. Its maximum row sum is therefore bounded by
\[
   1-\frac{1/6-10/(16\beta^2)}{\sigma^2}
        \le 1-\tfrac32[1/6-10/(16\beta^2)]<15/16.               \tag{T1}
\]

**Proved, explicit rational polynomial.** Let \(x(v)=v^tQv\), \(E_{256}(x)=\sum_{k=0}^{256}x^k/k!\), \(A=\int E_{256}(x(v))dv\) and \(B=\int x(v)E_{256}(x(v))dv\). These are specified rational polynomials in the entries of \(Q\) by the four-coordinate Haar moment formula. Put \(H=2^{43},\ L=2^{95}\) and set
\[
 F(Q)=\frac{\operatorname{tr}Q}{4\beta}
     -\frac{B}{4\beta H}\sum_{k=0}^{L-1}(1-A/H)^k .           \tag{T2}
\]
The finite sum specifies its coefficients without expanding it. Uniformly on the actual support, \(|x|\le12\beta<28\). Taylor's inequality gives \(|E_{256}(x)-e^x|<2^{-215}\), since \(e^{28}<2^{42}\), \(257!\ge(257/e)^{257}\) by the integral of the logarithm, and \(28e/257<1/2\). Hence \(2^{-43}<A<H\), and \((1-A/H)^L\le e^{-512}<2^{-512}\). The ratio of the exact exponential first moment to its normalizer has magnitude at most 28. Its difference from \(B/A\) is at most \(56\,2^{-215}/A<2^{-166}\). This proves \(\|F-\Phi\|_\infty<2^{-16}\).

**Proved, trial bounds.** Write \(\eta=2^{-16}\). Since \(\sigma>1/2\), the unit normalized centred versions of \(F,\Phi\) differ in marginal norm by at most \(4\eta\) because centring is a contraction and normalization costs at most twice the perturbation divided by the original norm. An absolute pair correlation changes by at most \(8\eta\). Thus the trial row is at most \(15/16+56\eta\) in Wilson. For a perpendicular positive pair, use the fixed-plane square variable of 1485 (8), which has mean zero, standard deviation \(1/2\) and pairing \(\bar c/4\) with \(\Phi\). Reflection Cauchy–Schwarz gives the explicit lower bound
\[
  r_* = \left(\frac{23/96-\eta}{49/60+\eta}\right)^2
  < \operatorname{Corr}_{W}(F_i,F_j).
\]
Here \(\sqrt{2/3}<49/60\). The polynomial-law marginal is obtained by the density-oscillation comparison of 1485 with \(D<251/250\). Apply it on the affine spans of this fixed pair of probes, in both directions. Then the polynomial-law absolute positive-pair correlation exceeds \(1-(251/250)(1-r_*)>2/25\), while its maximum trial row has upper bound \(7-(250/251)(7-15/16-56\eta)<97/100\). In particular (T2) is a genuine finite Haar polynomial test with a positive-row sum between \(6/25\) and \(97/100\) at the degree-ten law. The bounds use analytic Haar inequalities in the tilted measure. The full individual moment numerators have not been expanded. This one statistic rules out its own use for a refutation and supplies a lower check for any compression containing it.

## A quantitative bound on the omitted probe space

**Proved for the degree-ten law.** Use the unchanged continuous observation \(Y_i=Q_i\) in the ten rescaled coordinates above. Let \(D=[-1,1]^{10}\) with uniform probability \(\ell\). Write \(p_i=d\mu_i/d\ell\) for a one-face density. For two different faces, the conditional density \(k_z\) of \(Y_i\) given the other observation \(Y_j=z\) has one square-integrable weak derivative, uniformly in \(z\) up to a null set. The marginal \(p_i\) also has a continuous bounded version. An explicit common bound is
\[
 \|k_z\|_{H^1(D,\ell)}\le C,\qquad \|p_i\|_\infty\le C,
 \qquad C=2^{228}\left[13\left(1+\sum_{h=0}^{10}|P_h|2^{16h}\right)\right]^{312},                 \tag{1}
\]
where \(P(q)=\sum_hP_h q^h\) is exactly 1348 (13). The Sobolev norm squares and sums the function norm and the ten first-derivative norms. The large constant in (1) permits arbitrary tilting by the star plaquettes actually present.

**Proved, one free pair.** With Fourier variable \(\xi=(\xi_0,\Xi)\), set \(B=\operatorname{diag}(\xi_0,\Xi)\). The phase of one term is \(a^tBb/12\). A monomial in \(a,b\) of degree at most 60 in each has modulus at most one on the spheres. For fixed \(a\), choose the polar axis of \(b\) along \(B^ta\). Its axial coordinate \(x\) has density \((2/\pi)\sqrt{1-x^2}\). Conditional on it, \(b=x n+\sqrt{1-x^2}u\), with \(u\) uniform on the orthogonal unit two-sphere. The monomial in \(b\) has gradient of norm at most 60 in the unit cube, and \(|\partial_x b|=1/\sqrt{1-x^2}\). The axial density multiplied by the conditional monomial vanishes at the endpoints and has derivative of integral norm at most \(2+2\cdot60\). Integration by parts bounds the integral over \(b\) by \(\min(1,1464/|B^ta|)\), with value one allowed at zero. The largest singular value of \(B\) is at least \(|\xi|/2\) in the Euclidean norm of the ten coefficients. For its left unit singular vector \(e\), one has \(|B^ta|\ge(|\xi|/2)|a\cdot e|\) and \(\mathbb E|a\cdot e|^{-7/8}<16\) by the same axial density. Using \(\min(1,u)\le u^{7/8}\) gives the one-pair Fourier bound \(2^{16}\max(1,|\xi|)^{-7/8}\).

**Proved, eight or twelve free pairs.** Freeze all links except the eight private pairs of one face, and change the target links to their relative crossing frames. The conditional joint density before pushing to the sum is a polynomial on independent spheres, divided by its integral. Its sum of absolute monomial coefficients is at most the bracket in (1) to the power 312. In fact a plaquette trace has at most \(4^4\) signed coordinate monomials, and a coordinate of any transformed unit link is a linear form with coefficient sum at most four. Frozen link coordinates have modulus at most one. Thus the trace has coefficient sum at most \(2^{16}\). Products multiply the bounds, and the unnormalized density is at least \(13^{-312}\) by 1348 (13). Each free link is in at most six plaquettes, so the monomial degree in that link is at most 60. For a monomial the eight pair integrals factor, the translation contributes a unit phase, and the resulting Fourier decay is \(\max(1,|\xi|)^{-7}\). The coefficient before this decay is at most \(2^{128}\) times the bracket to power 312. Freezing the other face or conditioning on its observation averages such bounds. For the marginal alone one can instead leave all twelve pairs free, obtaining exponent \(21/2\) with coefficient \(2^{192}\) times that bracket power.

For the eight-pair bound use Plancherel. On \(2^j\le|\xi|<2^{j+1}\) the integral of \((1+|\xi|^2)\max(1,|\xi|)^{-14}\) is at most \(2^{23}2^{-2j}\), by enclosing the ball in a cube. On the unit ball it is at most \(2^{11}\). Their sum is below \(2^{25}\). For the twelve-pair bound use Fourier inversion. The integral of \(\max(1,|\xi|)^{-21/2}\) is below \(2^{10}+2^{20}\sum_{j\ge0}2^{-j/2}<2^{23}\). With the transform defined using \(e^{-i\xi\cdot x}\) the inverse and squared Plancherel factor is \((2\pi)^{-10}\le1\). Changing from Lebesgue density to density against \(\ell\) costs \(2^5\) in the Sobolev norm and \(2^{10}\) in the supremum. These estimates imply (1).

**Proved, probe-degree remainder.** Let \(b\) be any rational polynomial in the ten observed coordinates. Let \(J\ge0\) and use coordinatewise degree \(d=J+\deg_{\max} b\), where \(\deg_{\max}\) is the maximum of the ten individual degrees. If \(f\) is orthogonal to those polynomials in the *actual polynomial-law marginal* and has norm one, then every unit probe \(g\) on a different face satisfies
\[
 |\mathbb E_P f(Y_i)g(Y_j)|\le
 E_i(J,b):=\sqrt C\,\|1-bp_i\|_{L^4(K,\ell)}
      +\frac{C^{3/2}\|b\|_{\infty,D}}{J+1}.                     \tag{2}
\]
For \(h(y)=\int g(z)k_z(y)\,d\mu_j(z)\), Minkowski and Cauchy–Schwarz give \(\|h\|_{H^1}\le C\). Denote the tensor Legendre projection of degree at most \(J\) in each variable against \(\ell\) by \(h_J\). The estimate \(\|h-h_J\|_2\le C/(J+1)\) follows by the one-variable identity \(-[(1-x^2)L_n']'=n(n+1)L_n\). For normalized product Legendre polynomials, integration by parts and Bessel's inequality for the weighted coordinate derivatives bound the sum of the squared coefficients times \(\sum_i n_i(n_i+1)\) by the gradient energy. Every omitted index contributes at least \((J+1)(J+2)\). The endpoint factor vanishes. Smooth approximation gives the same bound in \(H^1\).

In \(\int f h\,d\ell\), the part with factor \(1-bp_i\) is \(\mathbb E_P[f(Y_i)(1-bp_i)(Y_i)g(Y_j)]\). Cauchy–Schwarz, followed by \(\|k_z\|_2\le C\) on \(K\), gives the first term of (2). In the remaining part \(\int f b h\,d\mu_i\), one may subtract \(h_J\) by the specified orthogonality. The \(L^2(\mu_i)\) norm of \(b(h-h_J)\) is at most \(\|b\|_\infty\sqrt C\|h-h_J\|_{2,\ell}\). This gives the second term. In particular there is no assumption that replacing Haar by finitely many link values also discretizes all the probes.

**Proved, finite evaluation of the error test.** Let \(u\) be a rational polynomial and \(N\) an auxiliary integer. Write \(p_{i,N}\) for the Legendre projection of \(p_i\) onto degrees at most \(N\) in each variable. A rationally enclosable upper bound for the norm in (2) is
\[
 \|1-bu\|_{4,K}
 +\|b\|_{\infty,D}\sqrt{C+\|u\|_{\infty,D}}\,
    \sqrt{\|u-p_{i,N}\|_{2,\ell}+C/(N+1)} .                       \tag{3}
\]
Indeed \(\|u-p_i\|_4^2\le\|u-p_i\|_\infty\|u-p_i\|_2\) and \(p_i\) obeys the same projection estimate as \(h\). Ordinary Legendre polynomials with value one at 1 have rational coefficients and rational squared norms against the uniform probability. Each coefficient of \(p_{i,N}\) is therefore an ordinary one-face moment divided by a rational squared norm. These moments include the Wilson polynomial weights of *all* 312 plaquettes. They and the two-face moments below are quotients of finite polynomial Haar integrals, normalized by the integral of their product weight. On a quaternion the integral of an all-even monomial of exponents \(2a_j\) is \(\prod_j(2a_j-1)!!/[2^{\sum a_j}(1+\sum a_j)!]\). An odd exponent gives zero. This is the sphere integral in 1485.

The integral over \(K\) in (3) can be bounded by rational interval sums. On dyadic boxes in \(D\) discard a box if some rational \(T\) with \(I-T^tT\succeq0\) and one choice of sign satisfy \(\pm s+\operatorname{tr}(T^tM)>1\) at every vertex. On retained boxes multiply an interval upper bound for \((1-bu)^4\) by the rational box mass. Every exterior point is strictly separated by such a test, by the singular value decomposition, scaling the dual maximizer slightly into the operator-norm ball and approximating it rationally. The boundary of \(K\) has volume zero by comparison with its interior dilates. Refining boxes and enumerating rational separators therefore yields arbitrarily sharp upper sums. Supremum bounds on \(D\) and square or fourth roots also admit rational enclosures. No floating-point integration is required.

**Proved, convergence on this particular support.** The marginal is positive at almost every point of \(K\). In its interior outside \(s=0\) and \(\det M=0\), use the sign-vector construction above. For each rank-one term the map from its two angles to its scalar and imaginary length is locally invertible, since \(\alpha+\gamma\) and \(\alpha-\gamma\) are strictly between zero and \(\pi\) in absolute value at \(|s|+r<1\), \(|s|r>0\). With its left direction fixed, the right direction and length vary the whole right three-vector. Three linearly independent left directions occur because \(M\) is invertible. These variations give nine independent matrix directions, and an independent scalar variation gives the tenth. The submersion change of variables in a small product chart, where Haar and the tilted weight have strictly positive smooth densities, gives a strictly positive lower marginal density locally. The excluded sets have Lebesgue measure zero. Given any positive tolerance, \(1-p_i/(p_i+\delta)\) tends to zero in \(L^4(K,\ell)\) as \(\delta\downarrow0\). Since \(p_i\) is continuous on \(D\), rational polynomials can approximate \(1/(p_i+\delta)\) and \(p_i\) uniformly. Choose \(b\) first, then \(u\), then \(N,J\) large. Consequently the rational upper bounds (2)–(3) can be made arbitrarily small. This proves compactness of each pair's correlation operator and gives a test of its polynomial-degree remainder.

**Proved, finite upper and lower tests.** In each face use the centred monomials through coordinatewise degree \(d_i\). Omit the constant. Form their exact marginal Gram matrices \(G_i,G_j\) and cross matrix \(H_{ij}\). The Gram matrices are positive definite by the interior density argument. A rational number \(a_{ij}\ge0\) bounds the norm of the polynomial compression if and only if
\[
     \begin{pmatrix}a_{ij}G_i&H_{ij}\\ H_{ij}^t&a_{ij}G_j\end{pmatrix}\succeq0 .
\]
This is the two-sided bilinear norm inequality after optimizing the relative lengths of two real vectors. If (2) is bounded by \(e_i,e_j\) for the two faces, the full pair coefficient is at most \(a_{ij}+e_i+e_j\). Indeed for the centred conditional operator \(T\) and the two marginal polynomial projections \(P_i,P_j\), write \(T-P_iTP_j=(I-P_i)T+P_iT(I-P_j)\), applying (2) on each side. Lower bounds use ordinary rational trial vectors in the same Gram matrices.

For the polynomial measure, the perpendicular reflection order from 1485 (6) still applies. In 1348 (13) set the truncated coefficients \(I_j^{[16]}\) to zero for \(j>10\) when taking the character coefficients of the polynomial. Since \(2T_j=U_j-U_{j-2}\) for \(j\ge1\) with \(U_{-1}=0\), the coefficients of the SU(2) characters \(U_j\) are \(I_j^{[16]}-I_{j+2}^{[16]}\), with a further subtraction of \(2^{-21}\) at zero. Termwise \(I_{j+2}^{[16]}/I_j^{[16]}\le (23/20)^2/[(j+1)(j+2)]\le529/800\) for the retained terms. Since \(I_0^{[16]}\ge1\), all coefficients are positive. Thus \(P(q(U^{-1}V))\) is a positive kernel by the matrix-coefficient inner product for each character. This proves the required diagonal reflection positivity with these weights. The gauge projections and coordinate symmetries of 1485 (6) still hold. The three compressions for a positive perpendicular, a mixed perpendicular and an opposite pair therefore suffice. A certified upper sum including the three errors with multiplicities \(3,3,1\) of at most \(122/125\) would pass the Wilson test via 1485.

**Proved, a smaller input for the finite calculation.** For an outward polynomial \(F\) invariant under the private right rotation, its unnormalized arm numerator is
\[
   N_F(A)=\int F\!\left(\tfrac1{12}\sum_e V(A_e,B_e)\right)
      W(B)(C^P W)(B)\prod_e P(q(A_e^{-1}B_e))\,dB .
\]
Here \(W\) is the product of the six internal plaquette polynomials of one three-cube and \(C^P\) is convolution with the twelve *unnormalized* one-link weights \(P\). First set the crossings to identities by the neighbour frame change of 1485 (3). The private pivot then acts by a right rotation on the probe, already averaged. In the neighbour box set its eight normal links to identities by changing frames in its outer slice. Integration of the outer twelve tangential links now gives \(C^P W\). All factors in this formula are polynomials with rational coefficients after Haar integration. For an incoming arm use 1485 (5) on the numerator, including its inversion and rooted gauge average. The denominator \(N_1(A)\) is gauge invariant. The joint moment numerator is the 32-central-link integral of the central internal weights times one \(N_F\) per arm, using \(F=1\) on unmarked arms. The common central integral with eight \(N_1\)'s is its denominator. For an arbitrary raw polynomial \(F\), use its private rotation average in the first moment and the private rotation average of \(F^2\) in the diagonal moment. Both averages are polynomial Haar integrals. An off-diagonal Gram entry on the same observed face uses the average of the product. This factors the moments through three-cube integrations and retains every arm tilt.

For the opposite pair, the original raw read sets are disjoint. Integrating the complement leaves a polynomial joint density in the two raw arrays, of degree at most 60 in each quaternion. Expanding it as a sum of separated monomials shows that the opposite-pair operator at \(P\) has finite rank already. Its range is spanned by the Haar conditional expectations of the left monomials given the observed sum, divided by the positive marginal density ratio to its Haar pushforward. Those conditional expectations need not be polynomials in the sum. For a perpendicular pair the four shared links prevent this disjoint-set factorization.

## An explicit cutoff at error \(1/1024\)

**Proved.** Equations (2)–(3) admit a fixed cutoff without first finding a reciprocal-density polynomial numerically. A small marginal event obeys, for every pair and almost every opposite observation,
\[
     \Pr_P(Y_i\in E\mid Y_j)\le8C^2\,\mu_i(E)^{1/13}.                 \tag{4}
\]
To see this, first use product Haar. Fix the four shared tangential links to \(x\), writing \(F_E(x)\) for the conditional event probability. For an opposite pair designate four links on the first face and average them at the end. The other face's remaining raw reads are independent of all variables used by this first face. Couple the residual four partner links and the crossings identically when changing \(x\). If the maximum chord displacement of the four quaternions is \(r\), the translation of the private sum changes by at most \(4r/12\). This follows from \(\|V(a,b)-V(a',b)\|\le |a-a'|\) and the corresponding inequality on the right. The eight-pair Haar density has global integrable gradient of norm integral at most \(C\), by the eight-pair proof of (1), Cauchy–Schwarz and support in \(D\). Hence the integral norm of its difference under a translation \(h\) is at most \(C|h|\), by integration along a segment, also for weak derivatives by smooth approximation. Thus \(F_E\) is \(C\)-Lipschitz in the maximum chord distance independently of the Borel event.

A Haar chord ball of radius \(r\le1\) has mass at least \(r^3/64\). Around the identity it contains the graph \((\sqrt{1-|v|^2},v)\), \(|v|\le r/2\), whose area density is at least \(1/(2\pi^2)\) after normalization. Its mass is at least \(r^3/(12\pi)>r^3/64\). If \(F_E(x)=a>0\), integrate over the product of four balls of radius \(a/(2C)\). This gives \(\Pr_{\rm Haar}(E)\ge a^{13}/(2^{37}C^{12})\). Finally the ratio of maximum to minimum of the unnormalized polynomial tilt is at most \((13\sum_h |P_h|)^{312}\le C\). This bounds the tilted probability of \(E\) conditional on the other raw reads by \(C\) times the Haar one, and the Haar marginal by \(C\mu_i(E)\). Taking the conditional expectation given the other observed sum proves (4). The comparison costs occur before and after the thirteenth root.

**Proved.** One can use the same \(C\) in the Hölder bound \(|p_i(y)-p_i(y')|\le C|y-y'|^{1/4}\). In the twelve-pair inversion proof multiply the integrand bound by \(2|\xi|^{1/4}|y-y'|^{1/4}\). The dyadic sum is bounded using \(\sum 2^{-j/4}<8\), within (1)'s allowance. For \(n\ge1\) form a polynomial \(u_n(y)\) as follows. For each coordinate set \(t=(1+y_l)/2\), draw \(k\) with binomial parameters \(n,t\), and then \(T_l\) with beta parameters \(k+1,n-k+1\), independently by coordinate. Put \(u_n(y)=\mathbb E p_i(2T-1)\). This describes *integrals*, with no sampling. The coefficients in the tensor Bernstein basis are \((n+1)^{10}\) times the integrals of the corresponding basis polynomials against \(\mu_i\), hence rational by finite Haar integration. Also \(0\le u_n\le C\). In one coordinate the beta variance is at most \(1/[4(n+3)]\), its conditional mean is \((k+1)/(n+2)\), the variance of that mean is at most \(n/[4(n+2)^2]\), and the absolute bias from \(t\) is at most \(1/(n+2)\). These identities follow by integration of the beta monomials and the binomial first two moments. Therefore \(\mathbb E|2T-1-y|^2\le60/(n+1)\) in ten dimensions. Jensen and the Hölder bound give \(\|u_n-p_i\|_\infty\le C[60/(n+1)]^{1/8}\).

**Proved.** Fix \(\varepsilon=1/1024\) and define the cutoff by
\[
 \delta=\left(\frac{\varepsilon^2}{128 C^2}\right)^{13},\quad
 m=\left\lceil\frac{4C}{\varepsilon\delta}\right\rceil,\quad
 n=\left\lceil60(8m/\varepsilon)^8\right\rceil,\quad
 J=\left\lceil4Cm/\varepsilon\right\rceil,\quad
 d=J+n(m-1).
\]
Use \(b=C^{-1}\sum_{k=0}^{m-1}(1-u_n/C)^k\). It has coordinatewise degree at most \(n(m-1)\), satisfies \(0\le b\le m/C\), and \(\|p_i-u_n\|_\infty\le C\varepsilon/(8m)\le\delta/2\). On \(p_i\ge\delta\),
\[
 |1-bp_i|\le (1-u_n/C)^m+\varepsilon/8
    \le (1+m\delta/(2C))^{-1}+\varepsilon/8\le5\varepsilon/8.
\]
On the complementary event it is at most \(1+\varepsilon/8\le9/8\). That event has \(\mu_i\)-mass at most \(\delta\), since \(\ell(D)=1\). By (4) its probability at fixed opposite observation is at most \(\varepsilon^2/16\). Hence the first Cauchy–Schwarz term in the proof of (2) is at most \(\varepsilon\sqrt{25/64+81/1024}<3\varepsilon/4\). The second is at most \(\sqrt C\,m/(J+1)\le\varepsilon/4\). This proves an all-probe remainder of less than \(1/1024\) on one projected side, at the specified finite \(d\), for the genuine polynomial tilt on the full star.

**Proved implication.** A compressed positive row sum at most \(24/25\) at this \(d\) implies \(R_P\le24/25+14/1024<122/125\). The factor 14 accounts for two projected sides in each of seven summands. The explicit bound is very costly. Already \(C\ge2^{228}\) and \(J>2^{228}\). The one-face space has \((d+1)^{10}-1\) centred monomials. A dense exact Gram calculation at this cutoff exceeds the stated memory allowance even for one bit per diagonal entry. This size is a property of this cutoff and matrix representation. The adaptive bound (2)–(3) and sparse or symmetry-reduced bounds remain alternatives.

## Exact arithmetic and proof scope

**Checked by the Lean kernel.** The source below was run with Lean 4.36.0, single-threaded, using `nice -n 15` and Lean's 768 MB memory setting. Maximum reported resident size was 641,024,000 bytes on the timed run. Each of the four printed theorems reported the same axioms, `propext`, `Classical.choice` and `Quot.sound`. The trusted base for those closed rational inequalities is the Lean kernel and the imported `Std` definitions with those axioms. The proofs use `decide +kernel`. The Haar, gauge, reflection and regularity arguments above are written mathematical proofs. The arithmetic check does not evaluate the star Gram matrices or verify the analytic arguments.

```lean
import Std

namespace Interface1489

def fac : Nat → Nat
  | 0 => 1
  | n + 1 => (n + 1) * fac n

def coshPartial (squaredArg : Rat) (n : Nat) : Rat :=
  ((List.range (n + 1)).map fun k =>
    squaredArg ^ k / (fac (2 * k) : Rat)).sum

def x : Rat := (23 / 10 : Rat) ^ 2

theorem besselBounds :
    (69 / 10 : Rat) ^ 2 < 48 ∧ (48 : Nat) ^ 2 < 2400 ∧
    4 + x / (6 + x / (8 + x / 10)) < 24 / 5 ∧
    (9 / 8 : Rat) * (23 / 48 : Rat) ^ 2 = 529 / 2048 ∧
    (1 / 4 : Rat) < 529 / 2048 := by decide +kernel

theorem crossingBounds :
    (25 : Rat) < coshPartial (63 / 4) 4 ∧
    (63 / 4 : Rat) < 3*x ∧
    12 / 8 + 6*66/16 - 24*6*(5/6)/64 = (195 / 8 : Rat) ∧
    (2 / 3 : Rat) < (5 / 6 : Rat) ^ 2 ∧
    130 < 1 + (24 / 65 : Rat) * (coshPartial (x * (65/8)) 10 - 1) ∧
    (7 : Nat) ^ 5 < 130 ^ 2 := by decide +kernel

theorem remainderMargins :
    (25 / 64 + 81 / 1024 : Rat) < (3 / 4 : Rat) ^ 2 ∧
    (24 / 25 + 14 / 1024 : Rat) < 122 / 125 ∧
    (529 / 800 + 1 / (2 : Rat) ^ 21) < 1 ∧
    (2 : Nat) ^ 37 < 8 ^ 13 := by decide +kernel

def eta : Rat := 1 / (2 : Rat)^16

def rTrial : Rat := ((23/96 - eta) / (49/60 + eta))^2

theorem trialBounds :
    (1 / 2 - 10 / (16*x) : Rat) > 1/4 ∧
    (1 / 6 - 10 / (16*x) : Rat) > 0 ∧
    (1 - (3/2)*(1/6-10/(16*x)) : Rat) < 15/16 ∧
    (2 / 3 : Rat) < (49 / 60 : Rat)^2 ∧
    (2 / 25 : Rat) < 1 - (251/250)*(1-rTrial) ∧
    (7 - (250/251)*(7-15/16-56*eta) : Rat) < 97/100 ∧
    (529 / 6144 : Rat) > 1/12 ∧
    (49 / 100 : Rat)^4 < 1/16 := by decide +kernel

#print axioms trialBounds
#print axioms besselBounds
#print axioms crossingBounds
#print axioms remainderMargins

end Interface1489
```

## Consequence for the pure-Wilson pivot

**Proved implication from 1475 §5 and 1485.** A pass would supply a local contraction on this isolated open star. A refutation would exclude using this seven-exit row criterion for a pure-Wilson contraction. Either conclusion still requires its own finite certificate. The ordered auxiliary environment in 1475 is a different input. For the pure Wilson model the exact torus masses after the pivot are \(Z^z(\tau)=c_2^{V_\tau}\mathcal I^z_\tau\). The eight twists at each of two periods enter \(P=Z_+(2v)/Z_+(v)^2\). A common site pressure cancels because \(V_{2v}=2V_v\). Per-mass log error \(\delta_0\) after that adjustment costs at most \(3\delta_0\) in log purity. The normalized pivot marginal is product Haar by the forest argument. The present local estimates supply neither the needed finite compression bound nor control of the sixteen scalar errors. [Pivot and pressure](gap-k2-pivot-environment-astra62.md) · [Pure-Wilson application](gap-k2-wilson-interface-astra62.md)

## Next two rows and their decisive outcomes

1. **Sketched. Certify the finite perpendicular and opposite forms.** Use the three-cube arm numerators above for the three exact Gram forms. The test (T2) supplies a positive-pair lower check of \(2/25\). An upper sum of \(24/25\) on the explicit compression would decide the local Wilson test. A smaller adaptive space suffices if its certified Gram norms and (2)–(3) give a total of at most \(122/125\), counting both omitted sides. Exact rational polynomial trials with row sum at least \(257/251\) would decide it in the opposite direction. The concrete obstruction to the dense calculation is the degree in the explicit cutoff. Sharpening the actual conditional-density bounds or bounding the finite forms without materializing their matrices is required for that approach under 4 GB.
2. **Sketched, conditional on a pass. Test the first join.** Keep the charged shared links, the four-linear corner tensors and all sixteen unnormalized masses. A contraction stable under the join with a common bulk pressure and the winding error needed for the \(1/100\) budget, or a strict decrement with quantified scalar error, advances the pure-Wilson step. A charged boundary probe violating that proposed contraction refutes this extension. A local refutation in the first row ends the proposed use of this criterion before a join. [End-class contract](gap-k2-end-class-fable.md)
