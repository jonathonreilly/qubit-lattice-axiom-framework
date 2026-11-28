# Repo search

**ON FILE (rows 531, 1143–1146, 1384, 1468).** The lead's 8 November digest compared main and PRs 10114, 10133, 10134 and 10141. Its thirteen targets were upstream construction questions. I checked PR 10114 at f76f6c649c, MASS_GAP_LOCAL_BLOCK_ASTRA.md 106–149 and checks/review_massgap_block_literature.md 109–122, 159–172. The first gives a positive one-step plaquette correlation. The second records the missing crossover estimate. PR 10141 contains snapshots of the hard route. Neither cited passage supplies a physical-side purity. The target-specific prior file is absent at the requested source 64b81b278. The nearer work here is row 1143 (Wilson fields on fixed periodic tori, including the logarithmic distribution of the winding radius), row 1145 (thin paths and the determinant of the nonconstant modes), and check 1384 (change of the winding integral in five dimensions). I use their results below. A supplementary bounded search on main and the four PR refs found no named winding colour-rank, extremal-frame or rebased-axis law. A further search over the YM4D Markdown paths of those refs found no two-tree orientation decomposition or susceptibility statement under those names. The scalar fixed-cell determinant on main in docs/NATIVE_ZERO_PENALTY_L4_DELAYED_SPLITTING_NOTE_2026-09-08.md 135–144 concerns a different finite-dimensional splitting. Row 1222 (4)–(5) already pins all windings and gives the four-spin plaquette integral. Stage 10 uses that representation. The open registry's VIR-DOWN, LEV-FAIL, WMIX-SLICE, R10–R12 and TWO-PER entries concern different variables.

**ON FILE (rows 1378, 1386–1387, 1442–1443, 1453, 1468, 1527, 1553–1556, 1605–1607, 1643, 1649–1654).** The target uses the eight temporal twists at both periods, and the continuum implication in the lane is a hand argument in the reconstructed action-density sector. The release witnesses, side and trajectory stay fixed across the infinite subsequence. The fixed-coupling theorem for the full periodic transfer is a different result. The negative inventory has corrections, particularly the growing-box estimate of row 1141. Check 1556 restricts the massless-spectator test to consumer classes admitting the product and the chosen projection. The thermal transport and the whole-slice routes already have their recorded failure points.

**ON FILE (row 244 index and row 1143 source comparison).** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, distinguish the cyclic action-density reconstruction from the richer gauge algebra and the additional spectral input at outline 581–599, 3712–3720, 32486–32490. CA-I 2696–2712 gives the scope of its reconstruction. Their small-field construction follows Tadeusz Bałaban. Both excerpts are from revision 31a47c543775. [Outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L581-L599) · [Complete account I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2696-L2712)

## Stage 1. Select a statistic of the Wilson field

**ARGUED.** A saddle approximation could conserve the partition function to leading logarithmic order and still give the wrong distribution for the noncommuting winding modes. First determine the joint colour and spacetime structure of those modes under the actual finite-volume Wilson law. Then test whether it persists for windings on the growing tori in the seed, and whether a signed inequality comparing the two thermal periods follows. The known partition asymptotic and its radial logarithm are inputs. This note is an author’s hand calculation without independent review.

## Stage 2. The colour carried by a weak periodic box

Write a based, straight winding as a unit quaternion \(h_i\). Fold it by its central sign and let \(x_i=\operatorname{sgn}(\operatorname{Re}h_i)\operatorname{Im}h_i\). The choice on the equator has probability zero. For a four-torus with fixed integer periods \(n_i\ge3\), set \(V=\prod n_i\), \(d_i=V^{1/4}/n_i\), and define a matrix with three colour rows and six spacetime columns by
\[
       C_{ij}=2\sqrt{\beta}\,d_i d_j\,(x_i\times x_j),\qquad i<j.
\]
A common gauge rotation acts on its rows. Write \(\lambda_1\ge\lambda_2\ge\lambda_3\) for the eigenvalues of \(CC^t\), \(L_i=\lambda_i/\operatorname{tr}(CC^t)\) on the positive-trace event. This measures the distribution of the commutator energy across colours. In particular \(1-\tfrac12\operatorname{tr}[h_i,h_j]=2|x_i\times x_j|^2\).

**PROVED (fixed-shape law, using the hand theorems of rows 1143–1146).** As \(\beta\to\infty\) in the normalized periodic Wilson measure, \(C\) converges in law as follows. Choose independently a uniform colour axis \(e\) on \(S^2\) and a uniform unoriented spacetime line \([q]\) in \(\mathbb R^4\). Conditional on these, the limit is a standard Gaussian in the six-dimensional Euclidean subspace
\[
              e^\perp\otimes (q\wedge q^\perp)
                     \ \subset\ \mathbb R^3\otimes\Lambda^2\mathbb R^4 ,
              \qquad |q|=1 .
\]
The quantity \(L_3\) tends to zero in probability and, for \(0\le t\le1/2\),
\[
             \lim_{\beta\to\infty}\Pr(L_2\ge t)=(1-2t)^2 .
\]
The same limits hold in the positive mixture with weights \(Z^z/\sum_y Z^y\) defining the neutral partition function. All periods here are fixed before taking the limit.

**Proof.** Here are the precise prior inputs. Row 1143 §6, checked in 1144, uses triangular plaquette coordinates and the chart in which \(|x_k|=r=\max_i|x_i|\). In the part carrying the normalized mass it writes
\[
 x_k=r e,\quad x_i=r b_i e+(\sqrt\beta r)^{-1}w_i,\quad
 b_k=1,\quad w_k=0,\quad w_i\in e^\perp .
\]
In the limit the chart measure before the Gaussian weight is a constant times \(dv\,de\,db_{\ne k}\,dw_{\ne k}\,d\xi\), where \(0<v=-\log r/\log\beta<1/4\), \(|b_i|<1\) for \(i\ne k\), and \(\xi\) denotes the nonconstant Gaussian variables. The cited proof gives an integrable majorant in \((\xi,w)\) and vanishing normalized mass in its two discarded radial ranges. Thus any bounded continuous insertion in \(C\) passes through that limit. The cross product of the two small transverse terms vanishes since \(\sqrt\beta r^2\to\infty\) in the interior. The limiting \(C_{ij}\) is \(2d_i d_j\,e\times(b_i w_j-b_j w_i)\).

Row 1145 §2, checked in 1146, integrates the Gaussian in the nonconstant links by projecting its seam source onto harmonic two-forms. For clarity on a rectangle, the source in orientation \(ij\) equals \(2e\times(b_iw_j-b_jw_i)\) on the \(ij\) double seam. It is closed because it depends only on those two coordinates. Every nonconstant closed Fourier mode is exact by contraction with the conjugate difference vector divided by its squared norm. The free-link curl spans these exact forms by the tree and four winding gauge conditions in row 1145. Its Gaussian integral therefore gives a determinant independent of \(e,b,w\) times the exponential of minus half the squared norm of the constant part. The mean of each seam indicator is \(1/(n_i n_j)\), hence this norm is exactly \(\sum_{i<j}|C_{ij}|^2\) with \(C\) now denoting the limiting tensor. All four charts use the same determinant and base-coordinate normalization.

Let \(D=\operatorname{diag}(d_i)\), \(p=Db\). In each of the two transverse colours the linear transformation in \(w_{\ne k}\) is \(w\mapsto p\wedge Dw\), up to the common factor two and an orthogonal colour rotation. Its image is \(p\wedge p^\perp\). On the hyperplane with coordinate \(k\) zero the squared metric of \(y\mapsto p\wedge y\) is \(|p|^2 I-p_{\ne k}p_{\ne k}^t\), with volume multiplier \(|p|^2 |p_k|\). The restriction of \(D\) to that hyperplane has determinant \(1/d_k\), since \(\prod d_i=1\), and \(p_k=d_k\). Thus the two colours together leave weight \(|Db|^{-4}\,db_{\ne k}\) after the change to Euclidean volume in their image. Conditional on \(b,e\), the Gaussian there is standard. The radial projection \(p\mapsto p/|p|\) of the plane \(p_k=d_k\) has surface Jacobian \(d_k/|p|^4\), by projecting a surface element normally to the ray and dividing by \(|p|^3\). Multiplication by the tangential Jacobian \(1/d_k\) of \(b\mapsto Db\) gives exactly the preceding weight. The charts partition the unoriented sphere by the largest coordinate of \(D^{-1}q\), ignoring ties. Their sum gives uniform projective direction independent of the uniform \(e\). This proves the tensor limit.

In orthonormal bases of the two subspaces the nonzero matrix is a \(2\)-by-\(3\) matrix with independent standard normal entries. Write its rows \(g,h\), set \(x=(|g|^2-|h|^2)/(|g|^2+|h|^2)\) and \(y=2g\cdot h/(|g|^2+|h|^2)\). The two radial densities are proportional to \(r^2e^{-r^2/2}dr\). Changing to the sum of squared radii and their relative difference gives an \(x\)-density proportional to \(\sqrt{1-x^2}\). Conditional on the radii, the cosine of their independent spherical directions is uniform on \([-1,1]\), so \(y\) is uniform on \([-\sqrt{1-x^2},\sqrt{1-x^2}]\). Hence \((x,y)\) is uniform on the unit disk. The normalized eigenvalue difference is \(\sqrt{x^2+y^2}\) and \(L_2=(1-\sqrt{x^2+y^2})/2\). Disk area gives the stated tail. The limiting trace is positive almost surely, which justifies normalization. Finally, every nonzero temporal twist contains a pair of anticommuting winding directions at an action minimum. Row 1145 (in the paragraph following (13)) bounds its partition function relative to \(Z^0\) by a quantity tending to zero at fixed shape. Thus the mixture has the same limit. \(\square\)

**ARGUED (decision).** The logarithmic radius itself is on file. The tensor limit determines a different observable, invariant under colour rotations and insensitive to any common rescaling of the winding radii. The next test compares its smallest colour fraction in five dimensions and on the actual growing four-tori.


## Stage 3. Two limits of that measurement

**PROVED (the five-dimensional control).** Fix a periodic five-dimensional Wilson box with all periods at least three. Allow any fixed positive direction weights \(d_i\), and form the ten cross-product columns as above. For every deterministic \(\epsilon_\beta\downarrow0\),
\[
                   \Pr_\beta(L_3\le\epsilon_\beta)\longrightarrow0.
\]
In four dimensions at fixed shape a sequence \(\epsilon_\beta\downarrow0\) exists for which this probability tends to one. In compact \(U(1)\) the total commutator energy is identically zero. Thus the nonzero, two-colour limit in Stage 2 has neither of these controls as an instance.

**Proof.** Use the restricted rectangular integral comparison of row 1143 (1), with its dimension-five extension in check 1384. The comparisons hold with an indicator depending on the winding tuple inserted, because they integrate the other links at fixed windings. Writing \(M=5V-(V-1)-5\), integration of the other links gives an upper bound \(C\beta^{-3M/2}\exp(-c\beta\sum_{i<j}|x_i\times x_j|^2)\) against winding Haar, and the total mass is at least \(c'\beta^{-3M/2-15/4}\). All constants in this proof may depend on the fixed box. Signs of scalar parts can be folded without changing the bounds.

Put \(r=\max_i|x_i|\), \(Y_i=\beta^{1/4}x_i\). The radial bound of check 1384 with its radial indicator gives, after division by the lower bound, an upper bound proportional to
\[
  \beta^{15/4}\int_{M_0\beta^{-1/4}}^1
  \frac{r^{14}}{\sqrt{1-r^2}(1+c\beta r^4)^4}\,dr
       \ \le\ C/M_0+C\beta^{-1/4},\qquad M_0\ge1 .
\]
For \(r\le1/2\) bound the denominator's last factor below by \(c^4\beta^4r^{16}\) and integrate \(r^{-2}\). The part above \(1/2\) uses integrability of \((1-r^2)^{-1/2}\). The scaled \(Y\)'s are tight. On \(\max|Y_i|\le M_0\) their joint density relative to fifteen-dimensional Lebesgue measure is bounded by a box-dependent constant for all sufficiently large \(\beta\) because the Haar factors are bounded there and the Jacobian \(\beta^{-15/4}\) cancels the remaining power. The first three columns of \(Y\) span three-space except on the zero set of a nonzero determinant polynomial, a Lebesgue-null set (integrate along one column at a time). Their pairwise cross products then span three-space as well. Positive column weights preserve this rank. Consequently \(L_3(Y)>0\) almost everywhere on each compact set. The compact-volume bound and dominated convergence give the claim after \(M_0\to\infty\). Stage 2 gives the four-dimensional assertion by taking successively smaller thresholds along a diagonal sequence. At \(\beta=0\) even a four-dimensional fixed box has independent Haar windings, with three-dimensional colour span almost surely. This comparison uses the change of the Wilson law within the same group and dimension. \(\square\)

**PROVED (failure of single-frame approximations at the seed aspect).** On the four-tori \(n^3\times v\), \(v=u,2u\), at \(\beta_K=O(\log n)\), use one common base vertex and either any of the eight twist laws or their neutral mixture. Let \(\nu_K\) be the true law of its colour fractions. Then \(\nu_K(L_3\le a_K)\to0\) for every \(a_K\downarrow0\). For every sequence of proposed laws \(\mu_K\) with \(L_3\to0\) in probability and positive commutator trace with probability tending to one, the total variation distance between their colour-fraction laws and the Wilson laws tends to one. This allows arbitrary fluctuating colour planes, radial distributions and correlations between columns. An atom at zero trace may be recorded as a separate outcome.

**Proof.** Row 1145 (1)–(3) compares the joint winding density with product Haar. For the stated rectangles omit the two end links on each coordinate circuit. All remaining links may be kept as independent pivots conditional on their complement. Indeed, collinear links cannot belong to a common plaquette, and two perpendicular selected lines at the common vertex have lost both end links. A sign stack changes a staple sum, preserving the bound on its length. With \(h=\min(n,v)\), the relative density is between \((1-\eta)^4\) and \((1+\eta)^4\) when \(\eta=\sum_{j\ge2}j^2\exp[-(j-1)(h-2)/(1+6\beta_K)]<1\). It tends uniformly to one and the bounds are preserved by positive mixtures. Credit for the Bessel convolution used in row 1145 goes to the Sussman–Alpoge outline 2197–2231, with Claude and Codex as authors of their text. Under product Haar the first three folded vectors span three-space almost surely. At either fixed aspect the \(d_i\) are fixed positive numbers independent of \(K\), so continuity from above gives the small-eigenvalue assertion. For any proposed \(\mu_K\) as stated, choose \(a_K\downarrow0\) sufficiently slowly that \(\mu_K(L_3\le a_K,\operatorname{tr}>0)\to1\). This event separates the measures. \(\square\)

**ARGUED (failure and next stage).** A fixed base frame loses the weak-box colour constraint on the very tori where the two partition functions must be compared. Row 1145 already demonstrated the failure of transplanting its radial saddle using a single trace. The conclusion here also excludes models that repair every common radial scale but keep a nearly missing colour in the normalized commutator tensor. The next attempt lets the base point be chosen from the field itself.


## Stage 4. Selecting the least noncommuting winding frame

At a base point form the \(D\) coordinate windings, \(D=4,5\). Use \(d_i=V^{1/D}/n_i\) and set
\[
 B_{ij}=2d_i d_j x_i\times x_j,\qquad A=\sum_{i<j}|B_{ij}|^2 .
\]
Thus \(B=C/\sqrt\beta\) in Stage 2. The colour fractions are unchanged. In what follows the aspect ratios and hence the \(d_i\) are fixed.

**PROVED (small-energy volume with its angular law).** Write \(F_D(a)\) for the probability of \(A\le a\) for independent Haar windings. As \(a\downarrow0\),
\[
 F_4(a)\sim\frac{a^3\log(1/a)}{384\pi^2},\qquad
 F_5(a)\sim c_5 a^{15/4},\quad 0<c_5<\infty .
\]
In dimension four, conditional on \(A\le a\), \(B/\sqrt a\) tends in law to the uniform point of the unit six-ball in the random subspace of Stage 2. The orientation is independent of the radius, so the two large colour fractions have exactly the same limiting law as in that stage. In dimension five the limiting colour fractions conditional on \(A\le a\) are all strictly positive almost surely.

**Proof.** Folded Haar has density \(\pi^{-2}(1-|x|^2)^{-1/2}\) in the three-ball, by projecting the two hemispheres of the unit three-sphere. Let \(r=\max |x_i|\). With four windings the part \(r\le a^{1/4}\) is \(O(a^3)\). The part \(r\ge1/2,\ A\le a\) is also \(O(a^3)\) by bounding the indicator by \(\exp(1-A/a)\) and applying row 1143 §2's radial estimate on this range with parameter a fixed positive multiple of \(1/a\), since the \(d_i\) are fixed and positive. On the intermediate range put \(r=a^v\) and in the largest-index chart write \(x_k=re\), \(x_i=r b_i e+(\sqrt a/r)w_i\) as in Stage 2. The product of Lebesgue elements becomes \(a^3\log(1/a)\,dv\,de\,db_{\ne k}\,dw_{\ne k}\). Here \(de\) is ordinary surface area. On \(A\le a\) the pairs \(ki\) force \(|w_i|\le1/(2d_i d_k)\). Also \(|b_i|\le1\) and all Haar denominators are bounded. At fixed \(0<v<1/4\) the normalized columns tend to \(2d_i d_j e\times(b_iw_j-b_jw_i)\). The limiting cutoff is a six-ball after the invertible linear change on \(w\) in Stage 2, so its boundary has measure zero. This proves dominated convergence, also with any bounded continuous insertion in \(B/\sqrt a\). No Tauberian converse about a logarithmic asymptotic is needed.

For the coefficient, combine the four Haar factors \(\pi^{-8}\), the \(v\)-interval of length \(1/4\), colour sphere area \(4\pi\), projective three-sphere area \(\pi^2\), transverse Jacobian \(2^{-6}\), and unit six-ball volume \(\pi^3/6\). The projective area already sums over the four choices of largest coordinate and the folded Haar density already counts both hemispheres. Their product is \(1/(384\pi^2)\). These Euclidean areas follow by integrating the ordinary Gaussian in polar coordinates. The same change of variables gives the conditional uniform-ball law. The disk calculation of Stage 2 applies to its direction, since the direction of a standard Gaussian is uniform on the unit sphere.

For five windings put \(x_i=a^{1/4}y_i\). On \(\max|y_i|\le R\) the rescaled density after division by \(a^{15/4}\) tends uniformly to \(\pi^{-10}\). The rescaled cutoff is the fixed set
\[
       \mathcal D=\{y:\ \textstyle\sum_{i<j}|2d_id_j y_i\times y_j|^2\le1\}.
\]
The discarded part divided by \(a^{15/4}\) is at most \(C/R+Ca^{1/4}\), by the same exponential indicator bound and radial integral as in Stage 3. Thus \(c_5=\pi^{-10}|\mathcal D|\) is finite and positive, and the limiting \(y\)-law is uniform volume on \(\mathcal D\). Its first three vectors are linearly independent with probability one, giving the rank claim. \(\square\)

**PROVED (extremal law on the calibrated rectangles).** Put \(m=\lfloor u/4\rfloor\) on both periods. Use the base points \((4j,\ldots,4j)\), \(0\le j<m\), and at each such point measure \(A\). Let \(A_*\) be the minimum, with the associated fractions \(L_{i,*}\). Set \(\kappa=1/(384\pi^2)\) and \(a_m=(3/(\kappa m\log m))^{1/3}\) for \(m>1\). On either neutral four-dimensional rectangle, and separately in every twist,
\[
 \Pr(A_*>a_m s)\longrightarrow e^{-s^3}\quad(s\ge0),\qquad
 L_{3,*}\longrightarrow0,\qquad
 \Pr(L_{2,*}\ge t)\longrightarrow(1-2t)^2 \quad(0\le t\le1/2).
\]
The limiting energy and colour fractions are independent. In particular the event
\[
                           0<A_*\le m^{-1/3}                                      \tag{1}
\]
has probability tending to one. For five-dimensional Wilson \(SU(2)\) on \(n^4\times v\), at any \(\beta=O(\log n)\), its probability tends to zero. For four-dimensional compact \(U(1)\) it is zero at every coupling. This distinction uses actual Wilson measures at growing lattice sizes.

**Proof.** Different base points differ by at least four in cyclic distance in every coordinate. Segments from two different frames along different axes still differ in at least \(D-2\) fixed coordinates. The private links of Stage 3 consequently work simultaneously for these \(Dm\) windings. The conditional joint density relative to product Haar is between \((1-\eta)^{Dm}\) and \((1+\eta)^{Dm}\), with
\[
 \eta=\sum_{j\ge2} j^2\exp\{- (j-1)(u-2)/(1+2(D-1)\beta)\}.
\]
Indeed each link sees at most \(2(D-1)\) signed staples, each of unit length. Row 1145's one-link bound depends only on the resulting tilt length. Deterministic connectors and inversion preserve the Fourier matrix norm and give its product estimate (2). Here \(Dm\eta\to0\), uniformly over twists. It suffices to prove all assertions for independent Haar frames. The polynomial \(A\) has no atoms under their absolutely continuous vector coordinates, since it is nonconstant and a nonzero polynomial's zero set has Lebesgue measure zero. There is a unique minimum almost surely.

At fixed \(s>0\), \(mF_4(a_ms)\to s^3\). The survival probability is \((1-F_4(a_m s))^m\). For a bounded continuous function \(f\) of the fractions, write \(F_f(a)=\mathbb E[f(L)1_{A\le a}]\). The ball law above gives \(F_f(a)/F_4(a)\to c_f\), its average over the stated limiting directions. Normalization at the origin is harmless since the origin has zero ball volume. On bounded rescaled intervals, \(m\,dF_f(a_m s)\) tends weakly to \(c_f\,d(s^3)\), first on intervals by subtraction, then for continuous functions by step approximations and the bound \(|f|\le\|f\|_\infty\). The winning mark has measure \(m(1-F_4(a_m s))^{m-1}\,dF_f(a_m s)\). Its weight factor converges uniformly on compact intervals to \(e^{-s^3}\) by monotonicity and continuity of the limit. The survival bound controls the remaining tail. This proves the claimed joint law. For (1), \(mF_4(m^{-1/3})\sim(\kappa/3)\log m\), whereas \(mF_5(m^{-1/3})\sim c_5 m^{-1/4}\). The independent minimum formula gives the first limit and a union bound gives the second. The Abelian commutators vanish pointwise. \(\square\)

**ARGUED (selectivity and the next test).** At a prescribed frame on the physical torus, all three colour fractions survive. Selecting the least noncommuting frame instead recovers the two-colour weak-box law, even though the exact Wilson partition functions have not changed. The four-dimensional logarithm in the frequency of almost-commuting frames is the point at which the five-dimensional proof differs. This is a test of a probability law. It also succeeds at fixed strong coupling in four-dimensional \(SU(2)\), and inspecting an \(SU(2)\) factor alone preserves it in a product with a spectator. Thus (1) passes the two specified comparison models but cannot by that fact alone supply the abstract consumer of check 1556. Next test the mass gained by selecting or pinning these frames.


## Stage 5. What pinning the selected frames does to the sixteen masses

**PROVED (a bound uniform even over rare-event conditioning).** For each of the sixteen measures of row 1468 §3.1, let \(f_{v,z}\ge0\) be any measurable function of the single-base winding frames of Stage 4, with arbitrary finite strictly positive product-Haar integral \(I_{v,z}\). Insert \(f_{v,z}/I_{v,z}\) in the *unnormalized* twisted partition function. Call the resulting neutral mixture and ratio \(\widetilde Z_+(v),\widetilde P_K\). Write \(N=4m\) and \(\eta\) as in Stage 4 with \(D=4\). Then, eventually,
\[
 \frac{(1-\eta)^N}{(1+\eta)^{2N}}
 \ \le\ \frac{\widetilde P_K}{P_K}\
 \le\ \frac{(1+\eta)^N}{(1-\eta)^{2N}} .
\]
In particular this ratio tends to one regardless of how small the Haar masses of selected events become. This rules out an order-one change of the purity from any such normalized positive insertion, including an adaptive choice from all these frames. No conclusion about crossing a threshold by a vanishing amount follows.

**Proof.** Integrate each nonnegative function against the pointwise density bounds of Stage 4 and then restore the original twisted mass. Positive summation over the eight twists preserves the same two factors. Take the ratio at \(2u\) and \(u\), using the same \(m\) for both. Truncation and monotone convergence handle unbounded functions. Without Haar normalization, even a common pin of Haar mass \(p_K\) at both periods introduces a factor \(1/p_K\) in the resulting numerical ratio. That factor by itself gives no bound on the original trace ratio. \(\square\)

**ON FILE (rows 1145, 1161, 1227, 1460 and checks 1146, 1162, 1230, 1463).** The private-link estimate and the loss of one chosen transport per straight circuit are prior work. Row 1161 (23) even takes all parallel circuits in all four directions. The bound above applies that method to the mass ratio. The sharp angular and selected-frame laws in Stages 2 and 4 are the additional calculations.

**ARGUED (next attempt).** Row 1161 (23) fixes one base point per circuit. It leaves open what can be seen by retaining the conjugated winding at both ends of a segment on the *same* circuit. Row 1178's nearby family of local plaquette data uses additional data. Its fixed-length reconstruction in gap-solve18-astra62.md uses two independent based plaquette vectors on the same edge. Here each segment has only one winding axis. I test how much of its adjoint transport one can nevertheless read and whether an alignment at the selected site is transported around a physical rectangle.


## Stage 6. Reading one circuit at several vertices

**PROVED (joint law at separated marks).** Fix \(D=4\) or \(5\), an even common divisor \(p\ge2\) of the torus periods, and any signed Wilson plaquette action of coupling \(\beta\). Mark finitely many deterministic vertices on each of a set of distinct straight coordinate circuits. The marks split the used circuits into \(J\) oriented arcs, including a whole circuit if it has one mark. Suppose each arc contains at least \(k\) pivot links, no plaquette anywhere contains two pivots, and all are on the arcs they serve. Set
\[
 \eta(k)=\sum_{j\ge2}j^2 e^{-(j-1)k/(1+2(D-1)\beta)} .
\]
Conditionally on all other links, if \(\eta(k)<1\) the joint law of the marked windings is bounded above and below, **as measures**, by \((1\pm\eta(k))^J\) times the following law. Draw one Haar conjugacy angle per circuit, independently. At every marked vertex draw an independent uniform axis on \(S^2\). Form the corresponding \(SU(2)\) elements with the common angle on their circuit. The angle here is the usual \([0,\pi]\) angle before central folding. All repeated traces on a circuit agree exactly.

**Proof.** The jointly private Wilson links have independent translated central densities at fixed exterior, with tilt lengths bounded by \(2(D-1)\beta\). Apply row 1145 (1)–(2) separately on each arc, then multiply bounds. The reference law for the arc transports is product Haar. For one circuit with \(s\) marks, let \(G_1,\ldots,G_s\) be those transports. Their successive prefixes \(P_j=G_1\cdots G_j\), \(1\le j\le s\), are independent Haar by triangular Haar changes of variables. The first winding is \(P_s\), and the remaining ones are \(P_j^{-1}P_sP_j\), \(1\le j<s\). Conditional on \(P_s\) their axes are independent uniform rotations of its axis. That first axis is itself uniform independent of the conjugacy angle. Pushforward preserves the measure inequalities, including on events of arbitrarily small positive reference probability. Equators and the two central elements do not affect the argument.

For an explicit choice when all spacings are at least \(h\), use the colouring of row 1161 (23) with this refinement for possibly unequal arcs. For the sum of coordinates modulo \(p\), allocate even residues \(2a\), \(0\le a<p/2\), to direction \(1+(a\bmod D)\). Select only links of the allocated direction. On a plaquette the starting residues are \(s\) and \(s+1\), and at either residue its two links have different directions. On an interval of length \(H=\min(h,p)\) there is at most one wrap in the residues. Each of its at most two pieces supplies at least its number of even residues divided by \(D\), less one, to each direction. Thus \(k=\max(0,\lfloor H/(2D)\rfloor-3)\) works on every arc. For \(p=u,\ \beta_K=O(\log n)\), polynomial \(J\), and \(H/[(1+\beta_K)\log n]\to\infty\), both bounds tend to one. A field-dependent choice among the declared marks is a measurable function of this same law. This statement conditions only on the specified exterior. \(\square\)

**PROVED (what happens across a short marked segment).** Let \(\Gamma\) be a lattice rectangle, traversed with four oriented sides of transport \(S_1,\ldots,S_4\) and root \(x\). At a corner \(y\) take the dot product of the unit winding axes of its two incident coordinate lines, both defined at \(y\). Denote by \(B(\Gamma)\) the product of the four dot products. It is gauge invariant and \(|B(\Gamma)|\le1\). Oriented winding axes can all be taken in their positive coordinate directions and folded as above. Write \(a,b\) for the axes of the first and last side at \(x\) and \(R=\operatorname{Ad}(S_1S_2S_3S_4)\). Hold all four side transports fixed, and on the *complementary* arcs of their four full circuits use private pivots. In the product-Haar reference for those arcs,
\[
 \mathbb E[B(\Gamma)\mid a,b,\text{fixed segments}]=
       \frac{(a^tb)(a^t R b)}9,\qquad
 \mathbb E[B(\Gamma)\mid\text{fixed segments}]=\frac{\operatorname{tr}R}{81}.       \tag{2}
\]
The same reference may include independent unused winding directions at the root. The true conditional law before further conditioning has relative bounds \((1\pm\eta)^J\) as above. In particular a nonnegative insertion \(1+t B(\Gamma)\), \(|t|\le1\), averages in the reference to \(1+t\,\chi_{\rm adj}(U_\Gamma)/81\). For rectangles using disjoint coordinate circuits, the product of these positive insertions averages to the product of the corresponding adjoint factors with the same single joint relative bounds, if all the side transports are in the exterior.

**Proof.** Write \(R_i=\operatorname{Ad}S_i\). The winding based at the end of a segment of transport \(S\) is its starting winding conjugated by \(S^{-1}\). Hence its axis at the end is \(R_S^t\) times the starting axis, also when the segment is traversed backwards. Conditional on the fixed segments, a Haar complementary arc makes the winding at one chosen end Haar. Use an independent starting axis \(c\) on the second side and \(d\) on the third. The four factors multiply to
\[
 (a^t b)(a^t R_1 c)(c^t R_2 d)(d^t R_3R_4 b).
\]
Uniform spherical axes have \(\mathbb E[cc^t]=I/3\) by rotations and trace one. Integrating \(c,d\) gives the first formula. Integrating independent \(a,b\) gives the second. All variables for distinct circuits are independent in this reference, and the Wilson density bound transfers every positive product without division by its smallest possible pointwise value. \(\square\)

**ARGUED (decision).** A scalar function of windings at repeated base points can retain an actual Wilson loop through (2). This is the case that is lost if one replaces conjugated windings at consecutive vertices by fresh independent axes. Equation (2) provides a way to test whether selecting the least noncommuting frames can carry alignment from small to physical rectangles.


## Stage 7. A local alignment that is lost over a physical distance

Use the \(m\) sites of Stage 4. From each site \(j\) draw a rectangle \(\Gamma_j\) in directions \(1,D\) (one spatial direction and time), with side lengths \(1\le r_i\le n_i/2\). Rectangles are translates on different transverse slices. Call site \(j\) selected if \(0<A_j\le m^{-1/3}\) for its root frame, put \(N_m=\#\{j\text{ selected}\}\), and define the observed alignment
\[
          S_m(\Gamma)=N_m^{-1}\sum_{j\ {\rm selected}} B(\Gamma_j),
          \qquad S_m=0\text{ if }N_m=0 .
\]
This statistic uses only winding matrices at the stated vertices. The conjugacy angle weights in \(A\) and all four corner dot products matter.

**PROVED (conditional comparison in four dimensions).** Write \(f_m=F_4(m^{-1/3})\), and let \(q_m\) be the Haar conditional mean of \((a^tb)^2\) given selection, for the two root axes. Then \(q_m\to1\), \(N_m/(mf_m)\to1\) in probability and, in each twisted law and its neutral mixture at \(\beta=O(\log n)\),
\[
 S_m(\Gamma)-\frac{q_m}{27m}\sum_{j=1}^m\operatorname{tr}\operatorname{Ad} U_{\Gamma_j}
                       \ \longrightarrow\ 0\quad\hbox{in probability}.                  \tag{3}
\]
The estimates are uniform over the allowed side lengths. The proof of (3) includes length one.

**Proof.** Use one mark at the root on each of its \(D\) circuits and one at a side endpoint on each of the two opposite side circuits. These are \(D+2\) distinct circuits per rectangle. Different roots have two different fixed transverse coordinates in four dimensions. Even an extra root winding in a transverse direction leaves the *other* transverse coordinate fixed, so it cannot coincide with a side circuit of another rectangle. All used circuits are distinct across rectangles. Keep the full four side segments in the exterior. Each used circuit has a complementary interval of length at least \(u/2\), and on an extra transverse circuit the whole circuit is available. Apply Stage 6's colouring with \(p=u\) to choose at least \(\lfloor u/(4D)\rfloor-3\) pivots per complementary interval. The joint reference error, for \(J=(D+2)m\), tends uniformly to zero conditional on this exterior.

In that reference the root windings are Haar independent of the fixed segments, independent across frames, so \(N_m\) is binomial with mean \(mf_m\sim(\kappa/3)\log m\). In Stage 4's dominating chart \(x_i/r\to b_i e\) and all \(b_i\ne0\) almost everywhere, including \(b_k=1\). On the selected event the root unit axes thus become parallel up to sign. The small-energy proof with this bounded insertion gives \(q_m\to1\). Common colour-rotation invariance gives \(\mathbb E[(a^t b)b a^t\mid{\rm selected}]=q_m I/3\), since the matrix commutes with every rotation and has trace \(q_m\). Equation (2) now gives mean \(f_m q_m\operatorname{tr}\operatorname{Ad}U_{\Gamma_j}/27\) for \(1_{\rm selected}B(\Gamma_j)\) at fixed segments. These marked variables are conditionally independent and their conditional variances are at most \(f_m\). Chebyshev's inequality for their sum divided by \(mf_m\), and for the binomial count at the same normalization, proves (3) in the reference. The conditional measure comparisons, then integration over the actual exterior, prove (3) in the Wilson laws. The denominator substitution is legitimate since \(|\operatorname{tr}\operatorname{Ad}U|\le3\). \(\square\)

**PROVED (the two scales and their controls).** For \(\beta_K\to\infty,\ \beta_K=O(\log n)\) in four dimensions,
\[
 \begin{array}{ll}
 S_m(\Gamma)\to 1/9 & \text{for elementary plaquettes},\\
 S_m(\Gamma)\to 1/9 & \text{also for strips of area }b_K
                \text{ with } b_K^2(1+\log\beta_K)/\beta_K\to0,\\
 S_m(\Gamma)\to 0 & \text{if at least one side }r_K/(1+\beta_K)\to\infty .
 \end{array}                                                                        \tag{4}
\]
All limits are in probability, at each period. The first line is false for weak four-dimensional compact \(U(1)\) and for five-dimensional \(SU(2)\) at \(\beta=O(\log n)\). It is also false within the *same* four-dimensional \(SU(2)\) action at every fixed \(0\le\beta\le1/12\), where \(\Pr(S_m>1/18)\to0\).

**Proof of the small-area estimates.** For a temporal twist \(z\) there exists a zero signed-action field on the rectangle. Take all nonwrapping links equal to one. On the wrapping hyperplanes take time holonomy \(i\) and spatial holonomy \(j\) if the corresponding bit is one, \(1\) otherwise, with \(i,j\) orthogonal quaternion units. The spatial wrapping holonomies commute and the required time–space commutators are the prescribed signs. A ball of linkwise radius \(c/\sqrt\beta\) around this field has product-Haar mass at least \((c'\beta^{-3/2})^{4V}\) for \(\beta\ge2\), by three-sphere volume. Every signed face has action at most \(C/\beta\) on this event by telescoping the four unitary factors. Thus \(-\log Z^z(\beta)\le C V(1+\log\beta)\) with shape-independent constants in the convention \(e^{-\beta A_{\rm signed}}\). Convexity of \(\log Z^z\) and \(Z^z(\beta/2)\le1\) give \(\mathbb E_\beta A_{\rm signed}\le 2[-\log Z^z(\beta)]/\beta\), where the derivative is with the twist fixed.

Each signed plaquette action has the same expectation at every translation of a fixed orientation. To move a stack by one spatial unit, flip the time links at its time cut over the one transverse coordinate layer swept out. A time translation flips the corresponding spatial links at their spatial cut in the swept-out time layer. These sign changes preserve Haar and match the translated signed actions. Composing the changes handles several bits. Positivity of the other orientation sums then bounds the expectation for each face by \(C(1+\log\beta)/\beta\). Tile a rectangle of area \(b_K\) by its faces. Successively peeling a row expresses its signed boundary holonomy as the ordered product of \(b_K\) conjugated signed faces, with internal bonds cancelling. Unitary invariance and Cauchy–Schwarz give its squared chordal distance to one at most \(b_K\) times the sum of their squared chordal distances. Since \(3-\operatorname{tr}\operatorname{Ad}g=4(1-(\operatorname{Re}g)^2)\le8(1-\operatorname{Re}g)\), and the adjoint is insensitive to the overall sign, the mean adjoint deficit is at most \(C b_K^2(1+\log\beta)/\beta\). Positivity and Markov's inequality control the sample average in (3), without decorrelation of the true plaquettes. This proves the first two lines.

**Proof of the long-side and strong-coupling estimates.** For the true marginal of the rectangles alone, condition on everything except the links on one side of length \(r_K\) on each rectangle, in the same direction. These pivots share no plaquette. In the dimension-three irreducible representation the expected product matrix around a given rectangle has norm at most \(e^{-2r_K/(1+6\beta)}\), by the \(j=3\) term of row 1145 (1), with the deterministic connectors unitary. The conditional traces for distinct rectangles are independent, bounded by three. The average differs from its conditional mean by \(o(1)\) in probability by Chebyshev. This proves the third line. At \(r=1,\ \beta\le1/12\), the upper bound on the absolute conditional trace is \(3e^{-4/3}<3/2\) (use \(e^{4/3}>1+4/3>2\)). Inserting this strict bound in (3) gives the stated strong-coupling test. For either comparison theory in the question the reason is different. \(U(1)\) has \(A\equiv0\). In dimension five Stage 4 gives no selected sites with probability tending to one. No assertion about a five-dimensional infinite-volume gap is used. \(\square\)

**ARGUED (failure of a carry).** The local reading \(1/9\) detects a typical property of the weak four-dimensional Wilson law and fails even at small coupling parameter \(\beta\) of the same action. On physical rectangles it goes to zero under the very same measure. Equation (3) identifies the lost information as transport around the contour in the adjoint representation. One cannot use this local alignment as a lower bound uniform along a sequence of thin rectangles reaching the seed aspect. The next test allows reweighting the entire field to try to preserve the alignment.


## Stage 8. Minimum cost of making the alignment persist

**PROVED (entropy obstruction with matching rate).** Fix either period and any positive fractions of its lengths for the two sides of the large rectangle, bounded away from zero and from a full winding. Use a deterministic set of \(m\) root frames as above. One can take \(m\asymp n^3\) in four dimensions and use the same roots for both elementary and large rectangles. Replace the selection threshold by
\[
 a=m^{-4/15}(\log m)^{-1/3},\qquad \lambda=mF_4(a)\sim (4\kappa/15)m^{1/5}.
\]
For every \(0<s<1\), with \(E_s=\{N_m>0,\ S_m(\Gamma)\ge s\}\) on the **large** rectangles, the true Wilson probability \(W_K\), in each twist and in the neutral mixture, satisfies
\[
 \lim_{K\to\infty}-\frac{1}{\lambda}\log W_K(E_s)
 =J(s)=1-\min_{t\ge0} e^{-ts}\,
       \mathbb E\exp(t X_1X_2X_3),\qquad 0<J(s)<1,                    \tag{5}
\]
where the \(X_i\) are independent uniform variables on \([-1,1]\). On the **elementary** rectangles \(S_m\to1/9\) in the weak calibrated four-dimensional law. In five dimensions \(mF_5(a)\to0\) with this same choice of threshold, and \(U(1)\) has an empty selection. Thus for every \(0<s<1/9\) an actual small-scale signal has the explicit positive cost (5) at the physical scale.

In particular, for **every** sequence of alternative full-field laws \(Q_K\ll W_K\) with \(D(Q_K\|W_K)=o(m^{1/5})\), \(Q_K(E_s)\to0\). Among sequences satisfying \(Q_K(E_s)\to1\), the infimum of \(\liminf D(Q_K\|W_K)/\lambda\) equals \(J(s)\). The comparison is to the same torus, twist or mixture, and coupling on each side. This quantifies changes of measure that try to transport this specific signal. It places no requirement on a proof using another observable.

**Proof of placement.** For a root list the straight circuits used by its frame and by the two rectangles anchored there. The list contains at most \(D+4\) circuits. Declare a pair of *distinct* roots incompatible if any two parallel circuits in their lists coincide or are transverse lattice neighbours. For a fixed root and pair of line types, all but the longitudinal coordinate of the other root are fixed up to one of \(1+2(D-1)\) offsets. Thus at most \(C_D n\) roots conflict with a point on these rectangles for a fixed \(C_D\). Successively retaining one point and discarding its conflicts provides at least \(V/(1+C_D n)\) points. Conversely each root uses a distinct spatial circuit in a longest direction, so \(m\le V/n\). This proves the order in four dimensions, also for fixed aspect \(1/512\). The adjacent lines of a single elementary square are permitted. The colouring of Stage 6 still allocates long complementary intervals, and the single-side pivots in the marginal plaquette argument of Stage 7 are face-disjoint across roots. All those estimates therefore hold for this placement, separately at either shape. They use \(mf_m\to\infty\) and \(a\downarrow0\) for (3)–(4). The formula for \(\lambda\) follows from Stage 4, while \(m a^{15/4}=(\log m)^{-5/4}\).

**Proof of (5).** On each large rectangle mark both endpoints on every side circuit. Keep the single mark on the other root circuits. All arcs have length at least \(c u\), and the total number is \(O_D(m)\), so Stage 6 compares all the observations, even on exponentially rare events, within factors \(\exp(o(1))\) of its independent-axis reference. In that reference the angular variables at the three nonroot corners are independent of all root data. At each of these corners the dot product is uniform on \([-1,1]\). The shared line angles between endpoints affect only the root selection. Consequently the selected mark \(B\) has the law \(D_aX_1X_2X_3\), where \(D_a\) is the root dot product conditioned on \(0<A\le a\) and independent of the \(X_i\). Here \(|D_a|\to1\) in probability by the chart argument of Stage 7. Its sign does not affect the symmetric product distribution. The rectangles are independent in this reference.

Write \(f=F_4(a)\) and \(Y=1_{\rm selected}(B-s)\), so \(E_s\) requires \(\sum Y\ge0\) with nonempty selection. The one-frame moment generating function is \(1+f(H_a(t)-1)\), where \(H_a(t)=\mathbb E[e^{t(B-s)}\mid{\rm selected}]\). By boundedness the three conditional functions \(H_a,H_a',H_a''\) converge at each fixed \(t\) to \(H,H',H''\), where \(H(t)=e^{-ts}\mathbb E e^{tX_1X_2X_3}\). In particular the logarithm for the whole independent sum, divided by \(\lambda=mf\), tends to \(H(t)-1\). The function \(H\) is strictly convex, \(H(0)=1,\ H'(0)=-s\), and \(H(t)\to\infty\) because the product exceeds \(s\) with positive probability. Its minimizer \(t_*>0\) is unique. Exponential Markov at \(t_*\) gives the upper probability bound.

For the reverse bound tilt the reference by \(\exp(t\sum Y)\) with \(t>t_*\). Independence persists, the mean of \(\sum Y/\lambda\) tends to \(H'(t)>0\) by differentiating the finite product, and the variance of \(\sum Y\) is \(O_t(\lambda)\), since each squared contribution requires a selection. Thus with tilted probability tending to one the sum divided by \(\lambda\) lies in \([H'(t)/2,3H'(t)/2]\). This event implies nonempty selection. Undoing the tilt gives a lower limit for \(\lambda^{-1}\log\Pr(E_s)\) at least \(H(t)-1-3tH'(t)/2\). Let \(t\downarrow t_*\). This proves (5). The expectation in (5) also has the exact series \(\sum_{k\ge0}t^{2k}/[(2k)!(2k+1)^3]\) by the three independent even moments. No numerical minimization enters.

Finally, the two-event log-sum inequality gives \(D(Q\|W)\ge Q(E_s)\log(1/W(E_s))-\log2\). It follows by Jensen's inequality for \(x\log x\) on the event and its complement. Conditioning \(W\) on \(E_s\) gives this event probability one at entropy exactly \(\log(1/W(E_s))\), so (5) gives both necessity and attainment. \(\square\)

**ARGUED (boundary of the obstruction).** This kills persistence at small relative entropy for all full-field tilts, including nonlocal ones. It does not bound the entropy of an exact Yang–Mills blocking step. Row 1434 had a relative-entropy cost for a heat factor on a coarse link. Equation (5) concerns a transport event in the measured Wilson field, with its own matching upper and lower rate. I next test whether positive use of *all* the marked axes, even at unlimited entropy, can recover the missing transport.


## Stage 9. A circle of transport invisible to every positive tilt of the records

**PROVED (uniform postselection obstruction).** Use the large rectangles and all marks of Stage 8. Write \(\mathcal E\) for the exterior with the private pivot links omitted, \(Y\) for **all** marked winding matrices, and \(W\) for one normalized Wilson twist law. Allow any nonnegative \((\mathcal E,Y)\)-measurable weight \(w\) with \(0<\mathbb E_W w<\infty\), and let \(W_w=wW/\mathbb E_W w\). Choose any rectangle \(j=j(\mathcal E,Y)\) measurably after seeing these same data. If \(L=(1-\eta)^J,\ U=(1+\eta)^J\) are the joint arc bounds of Stage 6, then for \(0<\epsilon<\sqrt2\),
\[
 W_w\!\left(\min_{\pm}|U_{\Gamma_j}\mp1|\le\epsilon\right)
 \ \le\frac UL\,\frac4\pi\arcsin(\epsilon/2).                                 \tag{6}
\]
For the irreducible \(SU(2)\) character of spin \(h\), dimension \(d_h=2h+1\),
\[
 \left|\mathbb E_{W_w}\frac{\chi_h(U_{\Gamma_j})}{d_h}\right|
 \ \le \frac{\mathbf 1_{\{h\ {\rm integer}\}}}{d_h}+\frac UL-1 .                \tag{7}
\]
Here \(U/L\to1\). Both bounds allow weights with arbitrarily large entropy. They also hold for the neutral mixture, even with weights depending on the twist, by applying the argument conditionally and mixing with the updated positive weights. For spin one, in the reference with Haar arc transports, the **conditional mean** of the character given \(\mathcal E,Y\) is exactly \(B(\Gamma_j)\).

**Proof.** Keep the true \(\mathcal E\)-marginal and replace the conditional arc transports by independent Haar, as in Stage 6. The law of \((\mathcal E,\text{arc transports})\) in the original experiment has density between \(L\) and \(U\) relative to this reference. After any declared tilt and renormalization these bounds become \(L/U\) and \(U/L\).

On one side circuit write \(S\) for a segment and \(G\) for its complement. In the reference \(S\) and \(H=SG\) are independent Haar. The marked windings give \(H\) and \(H'=S^{-1}HS\). Given these two noncentral matrices the conditional law of \(S\) is uniform on the coset of the circle centralizing \(H'\) among the solutions of \(S H'S^{-1}=H\). To see the disintegration, fix \(H\), choose a measurable rotation taking the axis of \(H'\) to that of \(H\), and integrate a uniform stabilizing phase after this rotation. Uniform spherical direction times this uniform phase gives Haar transport by rotational invariance (or by invariance under every left translation). The reconstruction gives the stated pair. The central exceptions are Haar null and remain null under a finite-density tilt. The four sides are on distinct circuits, so these conditional phases are independent. The chosen index is already fixed under the conditioning.

Keeping three phases fixed, the loop holonomy is a left and right translate of a uniform circle \(\{\cos t+\omega\sin t\}\) in the unit quaternions. Its scalar part therefore has the form \(a\cos t+b\sin t\) with \(a^2+b^2\le1\). Near either centre point the required condition is \(|a\cos t+b\sin t|\ge1-\epsilon^2/2\). The fraction of angles is at most \(2\arccos(1-\epsilon^2/2)/\pi\), giving (6). In spin \(h\) integration over the stabilizing circle is an orthogonal projection of rank zero for half-odd-integer spin and rank one for integer spin. Indeed in the degree-\(2h\) symmetric power of the defining representation the monomials have weights \(-2h,-2h+2,\ldots,2h\), each once. The trace against unitary factors has modulus at most the rank. In the adjoint representation the mean side matrix is \(a_{\rm start}a_{\rm end}^t\), because the circle rotation fixes just the oriented axis. The trace of the four rank-one matrices is \(B(\Gamma_j)\). Finally the error in a normalized character expectation from the tilted density ratio is bounded by \(U/L-1\), since its absolute value is at most one. \(\square\)

**ARGUED (positive carries tested).** Even a postselection that buys the event in (5) and enforces nearly perfect agreement at every observed corner leaves the circle in (6). For a short Wilson plaquette at weak coupling its distance to the centre tends to zero in probability by Stage 7. Equation (6) rules out transporting that concentration to a long thin rectangle by *any* such positive use of the marked frames and their declared exterior. The stage concerns a particular observation of a Wilson field. It gives no inequality for a general blocked action or for the relative normalizations of different tori.


## Stage 10. Keeping the partition functions in a change of variables

**ON FILE (rows 720, 863/879, 1016, 1145, 1161, 1189, 1222).** The torus character formula in two dimensions, the Hölder split of the six plaquette orientations into three disjoint pairs at coupling \(3\beta\), and the temporal-gauge symmetry construction are earlier work. Check 879 keeps the finite-plane character sum in the Hölder bound. The private-link estimate for all straight circuits is (23) of row 1161. Row 1222 (4)–(5) already uses that estimate to pin every straight winding, keep the periodic doubling defect, and express the result as the local spin integral below. Row 1189 Lemma A0 has the corresponding four-site word in the frozen-plane model. The extension here uses all temporal twists, the actual even common period, and the partition into two trees.

**PROVED (signed and weighted extension of row 1222, preserving all sixteen masses to relative error \(o(1)\)).** At every site introduce independent Haar matrices \(g_i(x)\), one per coordinate direction, and define
\[
 U_i(x)=g_i(x)g_i(x+\hat i)^{-1}.
\]
Write \(D^z(v;\beta)\) for the integral of the original signed Wilson weight in these variables. For each period and twist,
\[
 (1-\eta)^{N_{\rm lines}}\le D^z(v;\beta)/Z^z(v;\beta)
                                    \le(1+\eta)^{N_{\rm lines}},                    \tag{8}
\]
with \(N_{\rm lines}=\sum_i V/n_i,\ k=\lfloor u/(2D)\rfloor-3,\ \eta=\eta(k)\) of Stage 6 for sufficiently large \(u\). The same assertion holds with any subset of the orientations active and all their couplings between zero and \(\beta\). The relative error is \(o(1)\) for \(\beta=O(\log n)\).

**Proof.** Under raw product Haar on the links of one circuit, replace the last link by the based circuit product \(h\). This change has unit Haar Jacobian and leaves all other links independent. Conditional on \(h=1\), an explicit version has the first \(n_i-1\) links independent Haar and the last their inverse product. Independent periodic \(g_i(x)\) give exactly this law by triangular Haar changes along the line. Different circuits have disjoint links and independent coordinates. Integrating the continuous Wilson weight in the other coordinates gives a continuous function of all \(h\)'s, whose value divided by \(Z^z\) is the joint Wilson density relative to product Haar. At the all-identity point the numerator is exactly \(D^z\). Stage 6 with one mark per circuit bounds this density almost everywhere, hence everywhere by continuity and full support of Haar. Inactive faces and smaller couplings only decrease the uniform staple bound. This proves (8), with no conditioning on an unspecified version at a null point. \(\square\)

**PROVED (two spanning trees of the direction graph).** Use labels \(1,2,3,4\) for the spacetime axes. Partition the six orientations into
\[
 E=\{12,23,34\},\qquad F=\{13,14,24\}.
\]
Each list is a spanning tree. At each site put \(h_{ij}=g_i^{-1}g_j\). The three \(h\)'s on either tree are independent Haar under the unweighted reference, by integrating from a root of the tree. If the first triple is \((a,b,c)\) in the displayed order, the second is exactly \((ab,abc,bc)\). The inverse map is \(a=st^{-1},\ b=ts^{-1}r,\ c=r^{-1}s\) for \((r,s,t)\) in the second list.

For any subset \(G\) of the six orientations write \(A_G^z\) for its signed Wilson action in the \(g\)-variables and \(D_G^z(\alpha)=\int e^{-\alpha A_G^z}dg\). The action in orientation \(ij\) uses just the one site field \(h=h_{ij}\). Its trace is the trace of
\[
            h(x+i)\,h(x+i+j)^{-1}\,h(x+j)\,h(x)^{-1}.
\]
This is direct cancellation inside the plaquette trace. Consequently the density \(e^{-\alpha A_E^z}/D_E^z(\alpha)\) factors in its three tree coordinates over all coordinate two-planes, and likewise for \(F\) in its own coordinates. Each factor is a two-dimensional plaquette spin integral with the inherited face signs. Haar changes at the unused tree root have unit mass.

Let \(\nu_E,\nu_F\) be these two probability measures at \(\alpha=2\beta\), on the *same* product \(g\)-space, and let \(\mathcal A_v^z=\int\sqrt{d\nu_E\,d\nu_F}\) denote their Hellinger affinity. The signed weights are positive, so pointwise multiplication of their square roots gives the exact identity
\[
           D^z(v;\beta)=
             \sqrt{D_E^z(2\beta)D_F^z(2\beta)}\,\mathcal A_v^z .                  \tag{9}
\]
This is a change of coordinates for finite volumes. The group products in the second tree have the indicated order and use the same underlying Haar variables in both densities.

**PROVED (normalizers of the trees).** With \(I(\alpha)=\int_{SU(2)}e^{-\alpha(1-\operatorname{Re}h)}dh\), at the calibrated aspect
\[
                      D_G^z(2\beta)=I(2\beta)^{3V}(1+o(1)),\qquad G=E,F .
\]
For a single plane of area \(A=n_i n_j\), its plaquette spin integral is exactly the all-line identity pin of the ordinary two-dimensional Wilson gauge integral, by the same tree-coordinate change with just two directions. The plane version of (8) compares these two integrals uniformly within \((1\pm\eta_{\rm pl})^{n_i+n_j}\), with \(k\ge\lfloor u/4\rfloor-3\) and one-link tilt at most \(2\alpha\). For a two-dimensional torus with seam parity \(\epsilon\) the latter integral is
\[
 I(\alpha)^A\left[1+\sum_{j\ge2}\epsilon^{\,j-1}
      (I_j(\alpha)/I_1(\alpha))^A\right].
\]
Here \(I_j\) are the modified Bessel functions and \(j\) denotes representation dimension. This is the torus character formula of rows 720 and 879. After expanding the normalized face class weight as \(\sum_j j(I_j/I_1)\chi_j\), Schur integration of each edge identifies neighbouring labels and contributes \(1/j\). Each contracted vertex index contributes \(j\). Thus the overall power of \(j\) is faces minus edges plus vertices, zero on the torus. A central sign has eigenvalue \((-1)^{j-1}\). Absolute convergence at fixed positive coupling follows from the Bessel series. Row 1145 (1) bounds the absolute sum of the nontrivial terms by \(\sum_{j\ge2}\exp[-(j-1)A/(1+\alpha)]\). Over at most \(3n^2\) planes per tree, the product of both types of relative errors tends to one since \(u=n/512\) and \(\alpha=2\beta=O(\log n)\). Each orientation contributes total area \(V\). This proves the assertion and includes twisted planes.

**ARGUED (test against the consumer).** Equations (8)–(9) yield
\[
 P_K=(1+o(1))\,
       \frac{8^{-1}\sum_z\mathcal A_{2u}^z}
            {(8^{-1}\sum_z\mathcal A_u^z)^2}.                                   \tag{10}
\]
The factors \(I(2\beta)^{3V}\) cancel, since the long volume is twice the short one. The multiplicative comparison is proved, including for exponentially small affinities. A lower bound with a fixed margin would transfer. Rewriting the original threshold, including an uncontrolled \(o(1)\) at equality, supplies no proof. The tree decomposition also works for compact \(U(1)\) with a linear change in the angles. In five dimensions two trees have eight edges in total and cannot cover the ten orientations. Counting these edges is no phase test. The question with mathematical content is whether the two separately solvable measures have sufficiently controlled overlap when the time period changes.


## Stage 11. The two tree measures are separated extensively

**PROVED (law on an omitted plane).** For either tree measure and any omitted orientation \(ij\), the site field \(h_{ij}\) on an entire fixed \(ij\)-plane is a product of independent Haar variables, at every finite coupling and for every choice of signed faces. Under the other tree it has the two-dimensional plaquette spin law. Consequently, at either period and in each twist along the calibrated sequence,
\[
 \frac{D(\nu_E\|\nu_F)}{\beta_K V}\to 6,\qquad
 \frac{D(\nu_F\|\nu_E)}{\beta_K V}\to 6 .                                    \tag{11}
\]

**Proof.** On a single active \(kl\)-plane, with coordinates \(a,b\) in directions \(k,l\), the action is invariant under \(h(a,b)\mapsto L_b h(a,b)R_a\) for arbitrary row and column matrices. In the displayed plaquette word in Stage 10 the inner pairs cancel these transformations and the residue is a conjugation. Thus a fixed row has independent Haar entries (apply independent \(R_a\)), and a fixed column does too. Different parallel planes are independent in these coordinates. The omitted \(ij\)-plane meets each plane of any active orientation in at most one row, one column or one point. Each active tree field restricted to this entire \(ij\)-plane is therefore product Haar. The tree fields are independent of one another. The path product along the tree from \(i\) to \(j\) gives \(h_{ij}\), hence it too is product Haar on this plane. Its plaquette trace has mean zero, since its four sites are distinct.

In particular \(\mathbb E_{\nu_E}A_F^z=3V\) exactly. Meanwhile \(\mathbb E_{\nu_E}A_E^z\le[-\log D_E^z(2\beta)]/\beta=O(V(1+\log\beta)/\beta)\) by convexity, \(D_E^z(\beta)\le1\) and Stage 10. Taking the expectation of the log density ratio gives \(2\beta\,\mathbb E_{\nu_E}(A_F^z-A_E^z)+\log(D_F^z(2\beta)/D_E^z(2\beta))\). The last term is \(o(1)\) by the tree normalizers. Interchange the two trees for the other direction. \(\square\)

**PROVED (optimal common entropy cost).** Let
\[
 h_\Delta=\int_{[-\pi,\pi]^4}\log\!\left(4\sum_{i=1}^4\sin^2(k_i/2)\right)
                           \frac{d^4 k}{(2\pi)^4},\qquad
 c=3h_\Delta-\tfrac92\log2>\tfrac32\log2 .
\]
Uniformly over the sixteen boxes and twists at cutoff \(K\),
\[
 -\frac{\log\mathcal A_v^z}{V}\ \longrightarrow c,\qquad
 \inf_Q\frac{D(Q\|\nu_E)+D(Q\|\nu_F)}{2V}\ \longrightarrow c .                 \tag{12}
\]
The infimum is over **all** probability laws on the common spin variables. In particular no choice of intermediate law can be at relative entropy \(o(V)\) from both solvable references. Equation (11) shows why using an endpoint itself has a still higher cost. These statements use the weak Wilson pressure on file.

**Proof.** Write \(f_\beta\) for the ordinary thermodynamic log partition function per site in the shifted convention of this note. At any fixed finite shape \(n_i\) and coupling, \(|V^{-1}\log Z^0-f_\beta|\le C\beta/\min n_i\). Indeed remove the plaquettes using wrapping bonds to compare a finite torus to an open box of the same vertices. Tile a large multiple torus by those vertex boxes and remove all plaquettes using an inter-box bond. In both comparisons the number removed per box is at most \(C V/\min n_i\). Unused links integrate to one, and each omitted weight lies in \([e^{-2\beta},1]\). Taking the thermodynamic limit in the tiled comparison gives the estimate. Inserting a sign stack changes the log mass by at most \(2\beta\) per flipped face, of which there are at most \(3V/(\min n_i)^2\). These errors **per site** tend to zero at the calibrated aspect.

Rows 1143 (16) and 1145 (7), checked in 1144 and 1146, give
\[
 f_\beta=-\tfrac92\log\beta+3\log h_0+\tfrac92\log(2\pi)-3h_\Delta+o(1),
 \qquad h_0=1/(2\pi^2).
\]
This is the previously derived Wilson bulk pressure and scalar graph determinant. Credit Sourav Chatterjee for the weak-coupling pressure comparison method in the \(U(N)\) setting, as credited by those rows. Also \(I(2\beta)=h_0\pi^{3/2}\beta^{-3/2}(1+o(1))\). In the quaternion exponential chart this follows by setting the radius to \(s/\sqrt\beta\), for which the rescaled integrand tends to \(e^{-s^2}\), and \(1-\cos r\ge 2r^2/\pi^2\) on \([0,\pi]\) gives Gaussian domination. Equations (8)–(9) now give \(V^{-1}\log\mathcal A_v^z=f_\beta-3\log I(2\beta)+o(1)\), proving the constant. For its strict sign, arithmetic versus geometric mean gives \(h_\Delta>\log4\) because \(\int_{-\pi}^{\pi}\log(4\sin^2(t/2))\,dt/(2\pi)=0\) and the four summands are unequal almost everywhere. For the integral, if \(J=\int_0^{\pi/2}\log\sin t\,dt\), reflection also gives \(J=\int_0^{\pi/2}\log\cos t\,dt\). The double-angle identity yields \(2J=J-(\pi/2)\log2\) with integrable logarithmic endpoints. This proves the bound for \(c\).

The normalized geometric mean \(d\mu=(d\nu_E d\nu_F)^{1/2}/\mathcal A_v^z\) is the full pinned spin law. Direct subtraction of log densities gives
\[
 \tfrac12[D(Q\|\nu_E)+D(Q\|\nu_F)]=D(Q\|\mu)-\log\mathcal A_v^z .
\]
At every finite box the densities are positive and bounded above and below, so measures singular to Haar have infinite cost and the identity applies to every finite-cost competitor. Jensen gives \(D(Q\|\mu)\ge0\), with equality at \(\mu\). \(\square\)

**ARGUED (where the direct attack stops).** The full weak-coupling law is exponentially atypical with respect to at least one of the two exact plane references in the sense of (12). The leading log-affinity is proportional to \(V\). Its contribution cancels exactly at the level of the term \(-cV\) in \(2\log Z_+(u)-\log Z_+(2u)\). Neither the sign nor the size of the residual follows from an \(o(V)\) remainder. Estimating an individual overlap to subexponential *relative-to-volume* accuracy is therefore insufficient for the seed. A sign or order-one error in the **difference between the periods** would be new information. Equation (10) asks for precisely that information and is not counted as a sufficient new estimate.


## Stage 12. Turning on the three omitted orientations

**ON FILE (rows 710, 1145, 1189, 1222).** The electric transfer with the magnetic action deleted, the one-link Fourier bound, row and column symmetries of the plaquette spin action, and preservation of finite link insertions under a long line pin are earlier inputs. I use the two trees to identify *which* omitted plaquettes have a nonzero covariance. This allows a test on the difference of periods itself.

**PROVED (covariance at the tree endpoint).** Keep \(E=12,23,34\) at common coupling \(\alpha\) and leave \(F=13,14,24\) inactive. Write \(\sigma_p\) for the prescribed face sign, \(W_p=\sigma_p\operatorname{Re}U_p\), and \(X=\sum_{p\in F}W_p\), where the sum includes all translates of the three orientations. Let \(\rho=I_2(\alpha)/I_1(\alpha)\). At \(\alpha=\beta_K\) on either seed torus, for each twist, the ordinary unpinned Wilson integral, the pinned integral, and their respective neutral mixtures all obey
\[
 \frac{\operatorname{Var}(X)}{V}
     = \frac14\left(1+2\frac{1+\rho^4}{1-\rho^4}\right)
       +O\!\left(n^{C}e^{-c u/(1+\alpha)}\right)
     \ \sim\ \frac{\alpha}{6}.                                                    \tag{13}
\]
Here \(c>0,C<\infty\) are independent of the cutoff and twist. The mean vanishes exactly in the pinned law. In the unpinned law its absolute value is at most the displayed exponential times a polynomial in \(n\). Interchanging the two paths on the four direction labels gives the same statement for the other tree.

**Proof of the support of the covariance.** In the pinned model an omitted fundamental plaquette involves the site field \(h_{ij}\) at its four vertices. Its mean is zero by Stage 11 and its square has mean \(1/4\), the second moment of one coordinate of a uniform unit quaternion. Write \(h_{ij}\) as the tree path product. For each edge \(e=kl\) of that path, one may change the central sign of its field on any single \(k\)-line or \(l\)-line inside its plane, by the symmetry in Stage 11. This flips the omitted trace just when an odd number of the four vertices of its square lie on that line. For an axis of \(e\) outside \(\{i,j\}\), there are four distinct such lines. Every edge on the path has at least one axis outside this pair. An edge outside the path has no effect at all.

For two omitted plaquettes to have nonzero product mean, these line parities must agree for every edge. In particular they must have the same tree path and therefore the same orientation. For each intermediate axis \(k\) on that path, projection of their four vertices along \(k\) must give the same square. This fixes the displacement to be parallel to \(k\). Periods at least three ensure that a unit coordinate square has a unique base in this projection. For orientation \(14\) there are two distinct intermediate axes, so only the diagonal survives. For \(13\) and \(24\) the only surviving possibilities are displacements parallel to \(2\) and \(3\), respectively. These conclusions are exact, including with arbitrary signed active weights.

**Value on the surviving line.** Let \(i,k,j\) be a path of length two. The other tree variable integrates independently. Put \(s_i=g_k^{-1}g_i,\ s_j=g_k^{-1}g_j\). The site gauge transformation by \(g_k^{-1}\) makes the \(k\)-links identity and the other two link increments \(s_d(x)s_d(x+\hat d)^{-1}\), \(d=i,j\). In each fixed three-dimensional slice the two active actions in these increments are just the signed Wilson weights between successive \(k\)-levels of the same spatial link. Before weighting, their joint law is independent link Haar with the identity product on every \(i\)- and \(j\)-line at each level. This follows by the circuit change in Stage 10. Temporarily remove those spatial line constraints. Each spatial edge now carries its own periodic one-dimensional \(SU(2)\) chain along \(k\), independently of all other edges.

Removing the constraints affects any product reading on at most eight specified spatial links by \(O(n^C e^{-cu/(1+\alpha)})\) when the reading has absolute value at most one. In fact keep those links in the exterior when applying the colouring of Stage 6 to all the spatial pins. At most eight pivots are lost per line, each remaining staple tilt is at most \(2\alpha\), and the number of lines is polynomial. Bayes' formula at the identity divides the conditional density of all the pins by their marginal density. Both are between \(1-\delta\) and \(1+\delta\) for \(\delta=O(n^C e^{-cu/(1+\alpha)})\). Continuity of the integrated kernels, or elimination of a pivot outside the observed links, gives the prescribed version. This is the signed special case of row 1222 (4). Applying the same argument to all directions in the original \(E\)-only Wilson integrals compares their bounded two-plaquette readings with those in the pinned model at the same precision.

In any one of the independent chains, let \(L=n_k\), and compare two levels at shorter cyclic distance \(r\le L/2\). The joint law of the endpoint links has one Haar initial value. Its increment density is proportional to the \(r\)-fold convolution of the normalized Wilson kernel times the complementary \((L-r)\)-fold convolution, each with the centre sign for its arc. The complementary density is \(1+O(n^Ce^{-cu/(1+\alpha)})\) pointwise by row 1145 (1)–(2). Dropping it and normalizing has that same uniform multiplicative accuracy. For \(r=0\) the endpoints coincide. In the resulting open chain the conditional fundamental matrix at the second level has expectation equal to the initial matrix times \(\rho^r\) and the arc sign. This follows from the Fourier multiplier of the two-dimensional defining representation in the one-link character formula, or by integrating each central increment. It also holds for an inverted spatial link by taking adjoints.

The square uses four independent spatial edges. Integrating their increments gives \(\rho^{4r}\) times the original fundamental plaquette reading up to the product of their arc signs. Multiplying the two omitted-face signs cancels that product because the six signs on each elementary \(ijk\) cube multiply to one for the temporal twists, and stacking the cubes cancels interior faces. The second moment of the initial normalized trace is \(1/4\). Thus the signed pair expectation is \(\rho^{4r}/4+O(n^C e^{-cu/(1+\alpha)})\). This calculation identifies positive correlations along each of the two allowed lines. It includes the case of distinct temporal periods for an intermediate direction.

Sum over all plaquette pairs and absorb the polynomial count into \(n^C\). On each such line the sum of \(\rho^{4r}\) differs from \((1+\rho^4)/(1-\rho^4)\) only by the exponentially small tail, since \(\rho\le e^{-1/(1+\alpha)}\) by row 1145. For \(14\) just the diagonal remains. This gives (13), including the unpinned variance after subtracting its exponentially small squared mean. The mixture adds at most the squared range of the component means. Finally \(1-\rho\sim 3/(2\alpha)\). Indeed \(\rho\) is the one-link mean of \(\operatorname{Re}h=\cos r\) against the tilted Haar measure. Rescaling \(r=s/\sqrt\alpha\) in numerator and denominator gives \(\alpha(1-\rho)\to\frac12\int_0^\infty s^4e^{-s^2/2}ds/\int_0^\infty s^2e^{-s^2/2}ds=3/2\) by integration by parts. The Gaussian majorant from Stage 11 applies with the extra polynomial. This proves the asymptotic and all the error assertions. \(\square\)

**PROVED (the first two derivatives of the period difference).** Let \(G_v(t)\) be the log of the unpinned neutral partition function with \(E\) at \(\alpha=\beta_K\) and \(F\) at variable coupling \(t\), including the usual shift in each signed Wilson action. Then \(G_v'(0)=-3V+O(n^C e^{-cu/(1+\alpha)})\) and \(G_v''(0)=\operatorname{Var}(X)\). This follows by differentiating the finite integral. Formula (13) has the same main term per site at both periods. Consequently the constant, linear and quadratic Taylor coefficients of \(G_{2u}-2G_u\) at zero are all \(O(n^C e^{-cu/(1+\alpha)})\), uniformly even after multiplication by \(\beta_K^2\). For the constant term use (8) and the two-dimensional character formula at coupling \(\alpha\), with the explicit errors in their proofs. The same calculation applies to each individual twisted difference.

**ARGUED (next test).** The first two coefficients cancel in the required period comparison. Their values alone say nothing about \(t=\alpha\). The individual second derivative grows like \(\alpha V/6\) even though \(X/V\) is bounded. This suggests testing whether a Taylor expansion of each log mass from the soluble endpoint can possibly reach the isotropic coupling.


## Stage 13. Complex zeros obstruct expansion from a solvable tree

**ON FILE (rows 677, 988/991, 1165).** These rows concern zero-free regions of Wilson integrals. Check 991 bounds a logarithm on compact subsets once a zero-free domain is known. Row 1165 gives a zero-free neighbourhood of a moving *isotropic* endpoint. Here the question is the opposite bound at the *anisotropic* tree endpoint, where the measured curvature is (13).

**PROVED (zeros of the individual physical masses).** Start with \(E=12,23,34\) at \(\alpha=\beta_K\) and the other three orientations at zero. Consider each unpinned \(Z^z\) on either period, or the neutral sum on either period, as an entire function of their common missing coupling \(t\). Each has a nonreal zero at
\[
                              |t|\le (72+o(1))/\alpha .                            \tag{14}
\]
The bound is uniform over these choices and holds for the pinned integrals as well. In particular the ordinary Taylor series at \(t=0\) for the log of *each individual mass* cannot converge at \(t=\beta_K\) for any sufficiently late cutoff. An absolutely convergent multivariate log expansion at the isotropic point centred on this tree is ruled out too. Thus the cancellation of its first two terms in the period difference does not validate a termwise expansion of the two log masses at the desired point.

**Proof.** Remove the trivial shift \(e^{-3Vt}\) and divide by the mass at zero. The resulting entire function is \(M(t)=\mathbb E e^{tX}\), with the appropriate normalized endpoint law. Here \(|X|\le3V\). If there is no zero in \(|t|<R\), take \(f=V^{-1}\log M\) there with \(f(0)=0\). For \(r<R\), \(\operatorname{Re}f(re^{i\theta})\le3r\). The nonnegative circle function \(3r-\operatorname{Re}f(re^{i\theta})\) has average \(3r\). Its absolute second Fourier coefficient is at most that average, and the power series of \(f\) identifies the coefficient's absolute value as \(r^2|f''(0)|/4\). Therefore
\[
                     R\le 12/f''(0),\qquad f''(0)=\operatorname{Var}(X)/V .
\]
Take the supremum of all zero-free radii and use (13). The finite bound guarantees existence of a nearest zero because \(M(0)=1\) and \(M\) is entire. It is nonreal by strict positivity on the real axis. The log cannot be analytic across a zero. Absolute convergence of a multivariate power series at the isotropic vector would give convergence on every smaller complex diagonal disk, contradicting (14). \(\square\)

**PROVED (affine paths, including the overlap interpolation).** More generally keep the same tree endpoint and vary the six couplings by \(t b_{ij}\) with arbitrary fixed real \(b_{ij}\). If \(b_{13}^2+b_{24}^2>0\), the nearest zero of any of the same integrals satisfies
\[
     |t|\ \le\ \frac{48\sum_{i<j}|b_{ij}|}
                      {(b_{13}^2+b_{24}^2)\alpha}\,(1+o(1)).                      \tag{15}
\]
This applies at a starting value \(\alpha=2\beta_K\) as well. In particular changing the active couplings at the same time, at fixed slopes, does not remove the obstruction. To get the path in (9), start at \(2\beta_K\) and use \(b_E=-1,\ b_F=1\), for which the full pinned integrand occurs at \(t=\beta_K\).

**Proof.** Remove the linear shift as before and set \(X_b=\sum_p b_{\operatorname{or}(p)}W_p\). An omitted \(W_p\) has zero covariance with *every* active \(W_q\) in the pinned reference. The single line flip used to kill its mean preserves each active plaquette trace pointwise. The unpinned and mixture errors in the sum of covariances are still \(O(n^C e^{-cu/(1+\alpha)})\) by the bounded two-insertion comparison. Distinct omitted orientations have zero pinned covariance by Stage 12. Keeping the nonnegative variance from all the active terms only improves the lower bound. Equation (13)'s line calculation thus gives
\[
          \operatorname{Var}(X_b)/V
                    \ \ge\ (\alpha/12)(b_{13}^2+b_{24}^2)(1+o(1)).
\]
Use \(|X_b|\le V\sum|b_{ij}|\) in the same circle argument. \(\square\)

**ARGUED (scope and failure of the expansion).** For these bounds it matters that the actual solvable endpoint has coherent fluctuations along each intermediate direction. At \(\alpha=0\) disjoint fundamental plaquettes have zero covariance and the susceptibility in (13) is \(3/4\). This upper bound on a Taylor radius is an obstruction to one class of proofs. It is compatible with analytic continuation in smaller steps, with a direct estimate on the period ratio, or with cancellation of zeros between numerator and denominator. Deciding such cancellation requires information about the two different volumes. In particular no singularity on the positive real coupling axis is implied.

**PROVED (comparison of endpoint susceptibilities).** The numerical coefficient in (13) changes in each comparison theory. For the four-dimensional compact \(U(1)\) Wilson cosine action the same path gives \(\operatorname{Var}(X)/(\alpha V)\to1\). For five-dimensional \(SU(2)\) with the path \(12,23,34,45\) active and all six complementary orientations measured it tends to \(1/4\). For \(U(1)\), local sign flips by \(-1\) impose the same path and projection constraints. A normalized Haar circle coordinate has variance \(1/2\) and a one-chain fundamental Fourier coefficient with \(1-\rho\sim1/(2\alpha)\), by the same rescaled cosine integral with radial volume \(dr\) instead of \(r^2dr\). The four independent edge chains give pair covariance \(\rho^{4r}/2\) because the conditional complex loop at the second level is the first complex loop times \(\rho^{4r}\) and the stack sign, before taking its real part. Long circular convolution tends uniformly to Haar here as well. For completeness the one-circle Fourier multipliers are \(I_m(\alpha)/I_0(\alpha)\), \(m\in\mathbb Z\). For \(m\ge1\) the recurrence \(I_{m-1}-I_{m+1}=2mI_m/\alpha\) and the positive decreasing sequence \(I_m\) give \(I_{m+1}/I_{m-1}\le(1+2/\alpha)^{-1}\). The first ratio \(I_1/I_0=1-1/(2\alpha)+o(1/\alpha)\) treats the remaining mode. Monotonicity can be seen directly from \(I_{m+1}/I_m=\mathbb E_m[\cos\theta]<1\) on \([0,\pi]\) for the density proportional to \(e^{\alpha\cos\theta}\sin^{2m}\theta\), obtained by integration by parts in the integral for \(I_m\). These estimates give a summable geometric Fourier tail after any arc of length at least \(c u\). For the line pin comparison at a variable local tilt below \(2\alpha\), the same bounds are uniform because \(\mathbb E_0\cos\theta\) increases with tilt since its derivative is a variance. At zero tilt all nonconstant coefficients vanish. There are two paths of length two and one longer omission, which gives the stated limit. In the five-dimensional path there are three length-two omissions, each with the same \(SU(2)\) value \(\alpha/12+o(\alpha)\). Each longer omission has only its diagonal covariance by the same projection argument. The private-link estimates use the five-dimensional staple bound. This proves the comparison. It concerns the stated anisotropic endpoints. Under the isotropic, calibrated law it is (4), together with the specified selection, that gives the separate typical-field test against both models. \(\square\)


**PROVED (all spanning trees of four axes).** For a tree \(T\) let \(m_2=\sum_{k=1}^4\binom{\deg_T k}{2}\), the number of omitted pairs joined by a two-edge path. The proof of (13) for a pair uses only the independent fields on its path. The proof for the other pairs uses only their two distinct intermediate axes. It follows that the expression in parentheses in (13) for an arbitrary tree is \(3-m_2+m_2(1+\rho^4)/(1-\rho^4)\). The path has \(m_2=2\) and the star \(m_2=3\), exhausting the trees on four vertices. The nearest zero for a common missing coupling is at most \((144/m_2+o(1))/\alpha\). The star need not have a solvable complementary tree for this conclusion.

## Stage 14. Testing cancellation directly in a two-period observable

**ON FILE (rows 667, 1145, 1165, 1222).** Spectral expansions of a repeated slice insertion, including the nonnegative squares of its matrix elements, and the distinction between individual and uncancelled zeros in a thermal ratio already occur in these rows. Here I use a new, explicitly specified positive slice insertion on the actual isotropic calibrated theory. It permits a direct test of cancellation. The analytic variable in this test changes one slice weight and is distinct from the homogeneous coupling in (14).

**PROVED (a selective pole of a perturbed neutral purity).** In each spatial slice, of dimension \(d=3\) or \(4\), use \(m=\lfloor n/4\rfloor\) diagonal base points as in Stage 4 and just the \(d\) *spatial* windings at each. Use the unweighted energy \(A=\sum_{i<j}2(1-\operatorname{Re}[h_i,h_j])\). Set \(M=1\) if some frame has \(0<A\le m^{-2/5}\), and zero otherwise. Let \(w_p=\operatorname{Re}U_p\) on one fixed elementary spatial plaquette of the slice and \(B=Mw_p\). The bounded slice operator \(D(z)\) is multiplication by \(\cosh(zB)\). With \(\operatorname{Tr}_0\) the trace on the centre-neutral gauge-invariant space, define
\[
 R_K(z)=\frac{\operatorname{Tr}_0[D(z)T^uD(z)T^u]}
                {(\operatorname{Tr}_0[D(z)T^u])^2},\qquad R_K(0)=P_K .
\]
For sufficiently late \(K\) this meromorphic function has an **uncancelled double pole** at \(z=i y_K\), with \(y_K\to\pi/2\). Its leading Laurent coefficient after division by \(P_K\) has nonzero magnitude \(O((1+\log\beta_K)/\beta_K)\). On the real axis, for every \(r_K\ge0\) with \(r_K(1+\log\beta_K)/\beta_K\to0\),
\[
                         \sup_{|r|\le r_K}|R_K(r)/P_K-1|\ \longrightarrow 0 .       \tag{16}
\]
In compact \(U(1)\) the inserted ratio is constant in \(z\). In five-dimensional \(SU(2)\) at \(\beta=O(\log n)\) the normalized ratio converges to one uniformly on every fixed compact complex disk and has no poles there eventually.

**Proof of the slice selection.** Each spatial circuit still has \(n-2\) private links as in Stage 4. In three spatial dimensions lines from distinct diagonal frames in different directions differ in the remaining transverse coordinate by cyclic distance at least four. Therefore the joint comparison to \(d m\) independent Haar matrices holds at every twist, also for this single slice. For three Haar windings, impose radii in \([1/4,1/2]\) and require the last two axes to lie within angle \(c\sqrt a\) of the first. A spherical cap has area \(2\pi(1-\cos(c\sqrt a))\), bounded below by a positive constant times \(a\) for small \(a\). With sufficiently small \(c>0\) the resulting energy lies in \((0,a]\) almost surely. Thus \(F_3(a)\ge c'a^2\). At \(a=m^{-2/5}\) the probability of \(M=0\) in four-dimensional \(SU(2)\) is at most \(2e^{-c' m^{1/5}}\) eventually, by the uniform density comparison. In five dimensions the spatial frame consists of four windings and Stage 4 gives \(\Pr(M=1)=O(m^{-1/5}\log m)\). In the Abelian model all commutators are one, so \(M=0\) identically.

In the weak four-dimensional law, Stage 7 gives \(\mathbb E(1-w_p)\le C(1+\log\beta_K)/\beta_K\), uniformly at both periods and in every twist. The spatial plaquette has positive face sign. Denote the right-hand order by \(\delta_K=(1+\log\beta_K)/\beta_K\). The selection bound then gives \(\mathbb E(1-|B|)=O(\delta_K)\) in both periods. This last input uses the actual action. For example at \(\beta=0\) the mask still tends to one, but the plaquette has the Haar trace distribution. Its expectation of \(\cos(\pi w_p/2)\) is strictly positive, so there is no short-period zero tending to \(i\pi/2\) in that four-dimensional comparison.

**Proof of the pole.** The short trace normalized by \(Z_+(u)\), evaluated at \(z=iy\), is \(\phi_K(y)=\mathbb E_u\cos(yB)\). On fixed bounded real intervals \(\phi_K,\phi'_K\) approach \(\cos y,-\sin y\) uniformly with error \(O(\delta_K)\) by the Lipschitz bounds in \(|B|\) for the two integrands. Thus there is a unique simple real zero in \((\pi/3,2\pi/3)\), at \(y_K=\pi/2+O(\delta_K)\).

For any such \(y\), \(D(iy)\) is a real bounded self-adjoint operator on the neutral slice space. The mask and the plaquette are gauge and centre invariant. The long trace is
\[
           \left\|T^{u/2}D(iy)T^{u/2}\right\|_{\rm HS}^2>0 .
\]
Indeed the finite-volume Wilson transfer restricted to this space is injective at \(\beta>0\). Its electric convolution is a product with strictly positive Fourier multipliers \(I_j(\beta)/I_1(\beta)\) for every finite representation dimension. The two spatial Boltzmann multipliers are strictly positive with bounded inverses at finite volume. Gauge and centre projection restrict the resulting positive quadratic form to the stated space. Hence \(T^{u/2}\) has dense range there. Moreover \(D(iy)\) acts nontrivially on the constant function because the open set where \(|w_p|<1/10\) has positive spatial Haar measure and \(\cos(yB)>0\) on it. A bounded operator vanishing in all matrix elements on a dense range would be zero. This proves strict positivity at the short trace zero. Both traces are entire by the uniformly convergent multiplier series on compact disks and the trace-class powers of \(T\). Thus the zero gives a double pole. For its coefficient, \(\mathbb E_{2u}|\cos(y_K B)|^2=O(\delta_K)\) by \(|y_K-\pi/2|=O(\delta_K)\), the bound on \(1-|B|\), and \(|\cos|\le1\). Cauchy–Schwarz for its two slice readings bounds the normalized long numerator by that same order. The short derivative in modulus tends to one. This gives the claimed nonzero coefficient bound.

For real \(r\), \(0\le1-\cosh(rB)/\cosh r\le |r|(1-|B|)\) by the mean-value theorem. The deficit of a product of two numbers in \([0,1]\) is at most the sum of their deficits. Apply this at both insertions under the positive neutral Wilson mixture and use the single-insertion estimate at the short period. This proves (16) without assumptions on the correlation between slices. In five dimensions \(\cosh(zB)=1\) off the event \(M=1\) and it is uniformly bounded on each compact disk. The one- and two-insertion normalized traces each converge uniformly to one by the probability bound on this event in either slice. The short trace stays away from zero there. The compact \(U(1)\) assertion follows pointwise from \(B=0\). \(\square\)

**ARGUED (where the last test stops).** The pole concerns repeated insertions that are positive for real source strengths in the calibrated theory. It disappears in both comparison models at the slice-selection step. Its leading Laurent coefficient tends to zero even as the sequence of poles stays at finite distance. Thus seeking a complex disk free of singularities for every such perturbation is too strong even for the real stability property (16). The pole belongs to the specified slice source. Whether the homogeneous tree-to-Wilson deformations in (14) have common zeros at the two periods is still open. None of these results estimates the unperturbed value \(R_K(0)\).

RESULT — (c), quantified obstructions for the stated methods.
PROVED by hand in (13)–(15) that the complex radius of an individual log mass expanded from any spanning tree of the four axes is at most \((144/m_2+o(1))/\beta_K\) along the common omitted coupling, where \(m_2=2\) for a path and \(3\) for a star.
PROVED in (4)–(7) the weak four-dimensional winding-alignment limit, its loss at physical separation, the sharp entropy cost of maintaining it, and the unobserved circle of transport under arbitrary positive selection.
PROVED in (16) that a specified slice insertion preserves the real purity to relative error tending to zero on a growing interval, while its two-period ratio has a double pole tending to \(i\pi/2\) that disappears in the two comparison models.
The tree overlap in (10)–(12) determines the bulk term, which cancels between periods. The residual needed for \(P_K\ge457/625\) remains uncontrolled.
The seed and the Jaffe–Witten mass gap remain open. The new hand proofs have no independent or Lean check.
