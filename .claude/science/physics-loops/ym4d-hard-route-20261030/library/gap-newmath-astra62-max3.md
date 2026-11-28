# Repo search

**ON FILE (rows 531, 1468, 1553/1556, 1656, 1659, 1660).** Lane pin 7a6e07577a4c. The target-specific prior note is absent. The lead's November 8 search of main and PRs 10114, 10133, 10134 and 10141 concerned thirteen upstream construction questions. PR 10141 carries hard-route snapshots. I checked PR 10114 at f76f6c649c, MASS_GAP_LOCAL_BLOCK_ASTRA.md 106–149 and checks/review_massgap_block_literature.md 109–122, 159–172. The former gives a local one-step rank-one bound. The latter records the separate common-parameter problem in twist interpolation. A scoped search of main (8b11ae2bb95e) and the four PR refs also located REVIEW_PUSH_A_CYCLE3_ASTRA.md 76 on a tree-to-Wilson replacement in a different construction. None of these passages supplies a divisibility assertion for the two neutral traces. In this lane rows 1163/1165 treat signed zero counts and the isotropic periodic coupling. Row 1656 (13)–(15) and its check 1659 address individual masses from an anisotropic endpoint. Row 1660 changes the strength of a single-slice observation. The homogeneous two-period question in check 1659 is explicitly open. The registry's TWO-PER concerns a real derivative along a moving period. VIR-DOWN, LEV-FAIL and WMIX-SLICE concern other estimates.

**ON FILE (row 244 index; rows 1468, 1643).** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, give the Wilson bond multipliers and the gauge projection in outline 2195–2239, 2313–2335. Their normalized zero-free lemma at 4693–4714 requires a complex bound. Outline 581–599 and CA-I 2696–2712 specify the action-density reconstruction and the separate spectral requirement. Both texts are at 31a47c543775. The consumer used here is row 1468 §3.1, with all eight twists at each period, one fixed side and the same release witnesses on the subsequence. Its continuum implication is on file as a hand argument. The fixed-coupling periodic Lean theorem takes a different input. [Outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2195-L2239) · [Complete account I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2696-L2712)

The affine-path bounds are (22), (28a) and (29). The three-model thermal comparison is (30). The results with the electric coupling fixed to its actual release value are (32) and (35)–(39).

## Stage 1. Where cancellation would have to read the law

**GUESSED (test fixed before derivation).** Use the path with \(E=\{12,23,34\}\) held at \(\alpha=\beta_K\), \(F=\{13,14,24\}\) at \(t\), and coordinate 4 as time. Cut the \(2u\) circle at its two opposite slices. At a nonreal zero of the short trace, the complex weights of the conditioned \(u\)-slabs depend on both boundary fields. A possible mechanism would be cancellation of the *second phase moment* of those weights under the real law of the two boundaries, with the order needed at the simple or multiple short zero. First test the stronger explanation that the same scalar zero occurs before averaging the boundaries. For a selective proof the necessary comparison line would be control of the phases **after conditioning on a physical pair of boundaries**. A mechanism reading loss of the transmitted phase would need to break there in weak 4D compact \(U(1)\) and weak 5D \(SU(2)\), while allowing loss in their strong-coupling twins. I have no theorem giving that distinction. Neither tree susceptibility, a count of color components, nor positivity of the reflected slab establishes it. I will test the boundary-factor explanation and the exactly equal-coupling case separately. A zero of multiplicity \(m\) in the denominator before squaring needs numerator order at least \(2m\). Holomorphy alone gives no cutoff-uniform bound and does not imply the numerical seed.

**ON FILE (rows 1386, 1442–1443, 1553/1556, 1605–1607, 1610/1613, 1643, 1649–1651, 1659).** Proposition NEG is an inventory with the five-dimensional gapless comparison identified as a belief. The product test of Lemma ALG applies to consumer classes that admit the product and its projection. I take the whole-slice mixing and thermal transport failure points as recorded. The masked pole in row 1656 (16) failed (g3). It is outside this calculation. All new arguments below are hand arguments in research text, with no independent check or standing.

## Stage 2. A boundary factor cannot remove the short zero

**PROVED (open slab at a homogeneous short zero).** Let \(H\) be the neutral gauge-invariant spatial Hilbert space. Put \(A(t)=T(t)^u|_H\), where \(T(t)=M(t)C(t)M(t)\) uses a half spatial weight on either side and the tensor product of the electric bond convolutions in the middle. Gauge averaging restricts to the identity on \(H\). Write \(D(t)=\operatorname{Tr} A(t)\). For all sufficiently late \(K\), at **every** zero \(\zeta\) of \(D\) with \(0<|\zeta|<1\), \(A(\zeta)\) is injective with dense range. In particular no scalar holomorphic factor vanishing there divides all neutral boundary amplitudes. If the zero has order \(m\), \(A(t)/D(t)\) has a pole of exactly order \(m\) in Hilbert–Schmidt norm (an operator-valued pole).

**Proof.** The real part of the trace of a group element in the Wilson action is a real bounded function of the field. Its coefficient \(t\) is continued holomorphically. At finite volume \(M(t)\) and its inverse are bounded entire multiplication operators locally in \(t\). The coefficient on a temporal bond is either the positive real \(\alpha\), or \(t\). For representation dimension \(j\ge1\) its shifted convolution multiplier is \(2e^{-t} I_j(t)/t\), with the removable limit at zero. For \(0<|t|<1\), after factoring \((t/2)^j/j!\) out of \(I_j(t)\), the sum of the moduli after the initial 1 is at most
\[
 \sum_{k\ge1}\frac{(|t|^2/[4(j+1)])^k}{k!}
 \le e^{1/8}-1<1 .
\]
Thus no multiplier vanishes. The fixed-\(\alpha\) multipliers are strictly positive by their series. For the finite product on the spatial bonds the tensor Peter–Weyl basis is complete and all its eigenvalues are nonzero. Gauge and centre transformations intertwine the convolutions, since their kernels are central, and commute with the magnetic factors. Injectivity passes to the restricted product and its adjoint; the adjoint of \(T(t)|_H\) is \(T(\bar t)|_H\). These facts also hold for the \(u\)-th powers. The factorial bound on each compact \(t\)-set sums even after multiplying by the one-bond multiplicities \(j^2\), so the convolutions and their finite tensor products are trace-norm holomorphic. This proves the asserted holomorphy of \(A\) and \(D\). If \(D(t)=(t-\zeta)^m d(t)\), \(d(\zeta)\ne0\), the leading operator coefficient is \(A(\zeta)/d(\zeta)\ne0\). In particular some matrix element between fixed neutral states has a pole of that order. The gauge/centre projection is imposed before taking any trace. Row 1656 (14), checked in 1659, supplies such a \(\zeta\) with \(|\zeta|\le(72+o(1))/\beta_K\); \(D(0)>0\). \(\square\)

**PROVED (failure under coupling changes in whole slabs, with the tree and the Wilson endpoint fixed).** Define
\[
 N(z,w)=\operatorname{Tr}_H A(z)A(w),\qquad
 Q(z,w)=\frac{N(z,w)}{D(z)D(w)},\qquad h_\lambda(t)=t+\lambda t(1-t/\beta_K).
\]
Here \(Q(t,t)=P_K(t)\). For every real \(\lambda\) in \((-1,1)\) outside a single countable exceptional set, at every sufficiently late cutoff the continuation \(Q(t,h_\lambda(t))\) has a pole at **each** zero of the short trace with \(0<|t|<1\). Its order there equals the order of that short zero. Both slab couplings run monotonically over the original real interval. The deformed quantity at either endpoint is the original purity there. The physical region containing the short zero near the tree thus admits no holomorphic bound that survives an arbitrary small open interval of these fractional changes. This concerns the bulk plaquettes throughout a slab.

**Proof.** The numerator is jointly entire. At each such zero,
\[
             N(\zeta,\bar\zeta)=\|A(\zeta)\|_{\rm HS}^{\,2}>0 .
\]
The affine map \(\lambda\mapsto h_\lambda(\zeta)\) has nonzero slope because \(\zeta\) is nonreal. Hence \(N(\zeta,h_\lambda(\zeta))\) is a nonidentically-zero entire function of \(\lambda\). The same holds for \(D(h_\lambda(\zeta))\), since \(D(0)>0\). Their two zero sets are discrete. Exclude their real members for all the indicated zeros and all cutoffs, a countable union since each \(D\) is entire and \(D(0)>0\). The local order of the quotient now follows by division. The endpoint and monotonicity assertions follow from \(h_\lambda(0)=0,\ h_\lambda(\beta_K)=\beta_K,\ h'_\lambda(t)=1+\lambda(1-2t/\beta_K)>0\). At positive real couplings the products have their usual positive path-integral interpretation, with half spatial weights from adjacent slabs at the join. \(\square\)

**ARGUED (failure and next test).** This kills cancellation by a common analytic normalization of the entire boundary operator, and cancellation stable under the given changes of real slab couplings. In particular it is possible that \(\lambda=0\) is exceptional at every cutoff. Reflection gives a norm only at conjugate arguments. It does not identify \(N(\zeta,\zeta)\) with that norm. The same obstruction applies in the weak comparison models: check 1659 supplies their short zeros and the circle-bond Fourier series in 4D \(U(1)\) has the same nonvanishing small-argument bound (with index \(|j|\), including 0, for which \(e^{1/4}-1<1\)). In 5D the finite product has more factors. This obstruction is not a positive selective input. Next test the scalar diagonal directly and find how much of its Taylor series is actually supplied by the solvable endpoint.


## Stage 3. The scalar ratio on the exactly homogeneous path near the tree

**PROVED (contact through a growing number of orders).** Use time axis 4, a leaf of the tree. Write \(P(t)=\operatorname{Tr}_H T(t)^{2u}/(\operatorname{Tr}_H T(t)^u)^2\). There are absolute \(c,C>0\) such that for each fixed \(0<\epsilon<1\), for all sufficiently late \(K\),
\[
 \max_{0\le m\le(1-\epsilon)u}
       \big|[t^m](P(t)-1)\big|
 \le \exp[-c\epsilon un/(1+\alpha)].                                      \tag{1}
\]
Also \(P\) is holomorphic on \(|t|\le c/n^3\), with \(|P-1|\le C\,2^{-u}\) there. The unperturbed single-slice magnetic potential may be any bounded real gauge- and centre-invariant function at each finite cutoff, the same on each slice. Constants do not use its oscillation. The perturbed magnetic potential here is the one on the specified path. Rows 1656/1659 compare the first two derivatives by an omitted-plaquette covariance calculation. Here the estimate comes from cutting through the one surviving electric direction.

**Proof.** Omit the spatially constant exponential shifts and divide the real strong electric kernels by their trivial representation coefficients. These factors, one per time step, cancel identically in \(P\). At \(t=0\), temporal convolutions in directions 1 and 2 average their spatial links over Haar. The remaining spatial graph consists of \(n^2\) disjoint straight circuits in direction 3. Gauge averaging gives a class function of the holonomy on each circuit. More explicitly the complete tensor kernel on gauge-invariant functions after this averaging is
\[
 k_0(x,y)=\prod_{L}\left(1+
       \sum_{j\ge2}\rho_j^n\chi_j(H_L(x))\chi_j(H_L(y))\right),
 \qquad \rho_j=I_j(\alpha)/I_1(\alpha) .
\]
Indeed the independent vertex rotations on a circuit put all its links except the wrapping one to the identity and leave conjugation at the base. Products of the usual orthonormal characters of these winding matrices thus span the surviving subspace. A character with label \(j\) uses each of the \(n\) links in representation \(j\), so the tensor convolution multiplies it by \(\rho_j^n\). Transverse-link averaging annihilates the orthogonal complement. This gives the kernel against full spatial Haar and also gives its centre-projected version by averaging the translate of one argument. Equivalently it is obtained by averaging the nonnegative electric link kernel over all vertex gauges and centre translations. With
\[
 \eta=\sum_{j\ge2}j^2e^{-(j-1)n/(1+\alpha)},\qquad
 \delta=(1+\eta)^{n^2}-1 ,
\]
we have \(|k_0-1|\le\delta\), also after centre averaging. Use the bound on \(\rho_j\) in row 1145 (1), and expand the product after subtracting 1. For \(n/(1+\alpha)\to\infty\) the geometric series and its first two derivatives bound \(\eta\le C e^{-n/(1+\alpha)}\). Hence \(\delta\le C n^2 e^{-n/(1+\alpha)}\) eventually. This cut estimate uses the full spatial winding length \(n\).

Let \(M_0>0\) denote the unperturbed half magnetic weight, \(p(dx)=M_0(x)^2 dx/\int M_0^2\), where \(dx\) is product Haar. The unitary map \(g\mapsto M_0g/(\int M_0^2)^{1/2}\) from \(L^2(p)\) to \(L^2(dx)\) respects the symmetries. Conjugate the transfer and divide by \(\int M_0^2\). Its neutral representative \(B(t)\) on \(L^2(p)\), using the projections as kernels, now has kernel \(k_0\) at zero. Extend it by zero on the orthogonal complement of the physical subspace. On the physical subspace the traces entering \(P\) are exactly those of \(B\) up to the cancelled scalar powers. Let \(J=|1\rangle\langle1|\) in \(L^2(p)\). The two new electric orientations contribute \(2n^3\) bounded traces of modulus at most one to the coefficient of \(t\). The new magnetic orientation contributes two half-slices of \(n^3\) such traces. At fixed boundaries these exponentials are integrated against the positive gauge- and centre-averaging measure with the old electric weights. Thus the full kernel obeys
\[
 \|B(t)-J\|_{\rm HS}\le d(t):=\delta+(1+\delta)(e^{3n^3|t|}-1).             \tag{2}
\]
The estimate is pointwise before taking the Hilbert–Schmidt norm. It uses no positivity at complex \(t\).

Here are details of the complex-power estimate. Write \(B=J+E\) with \(\|E\|_{\rm HS}\le d\le 1/32\). On \(|z-1|=1/2\), \(\|(z-J)^{-1}\|\le2\); the resolvent identity and the Neumann series give the spectral projection \(\Pi\) with \(\|\Pi-J\|\le 2d/(1-2d)\le3d\) by contour integration. Its rank is one since two projections at norm distance less than one restrict injectively to each other's ranges. The eigenvalue \(\lambda\) on its range obeys \(|\lambda-1|\le d\): any point farther than \(d\) from \(\{0,1\}\) belongs to the resolvent by the same Neumann argument. Put \(S=B(I-\Pi)\). Then
\[
 \|S\|_{\rm HS}\le\|E\|_{\rm HS}\|I-\Pi\|+
                  \|J(J-\Pi)\|_{\rm HS}\le 5d .
\]
For the second term use rank one; for the first, \(I-\Pi=(I-J)+(J-\Pi)\). Since \(\Pi S=S\Pi=0\), for \(v\ge2\)
\[
 \operatorname{Tr}B^v=\lambda^v(1+e_v),\qquad
 |e_v|\le(5d/(1-d))^v\le(6d)^v .
\]
This follows from \(\|S^v\|_1\le\|S\|_{\rm HS}^2\|S\|^{v-2}\). Substituting \(v=u,2u\) gives \(|P-1|\le C(6d)^u\). Equations (2) and this estimate prove the fixed disk assertion by decreasing the absolute \(c\).

On the smaller circle \(|t|=\delta/(12n^3)\) we have \(d(t)\le2\delta\) eventually. Cauchy's coefficient bound gives \(C(12\delta)^u(12n^3/\delta)^m\). Its logarithm is at most
\[
 -(u-m)n/(1+\alpha)+O(u\log n)
\]
uniformly for \(0\le m\le u\); here \(\delta^{u-m}\) has nonnegative exponent. Since \(\alpha=O(\log n)\) the first term wins for \(m\le(1-\epsilon)u\). This proves (1), including \(m=0\). \(\square\)

**ARGUED (scope and next stage).** The two-period subtraction makes the Taylor coefficients exponentially small through orders proportional to a period. Both traces are zero-free on the disk just proved. Their more distant zeros are unlocated by this estimate. The cut works for compact \(U(1)\) as well and for a time leaf on the five-axis path. Nothing in (1) supplies (g3). Next test whether an analytic continuation argument could make the distinction using this contact together with a wide neighborhood.


## Stage 4. A second-order cut and a test that could decide bounded continuation

**PROVED (the error of one cut starts at degree two).** In the notation of Stage 3, let \(k_t\) be the gauge- and centre-averaged electric kernel, keeping the strong kernels normalized and using \(e^{t\operatorname{Re}h}\) on the weak bonds. Then \(k'_0(x,y)=0\) for every pair of fields. A term of this derivative puts a single weak bond between two different direction-3 circuits. In the integral over the vertex gauges at the join, change all gauge matrices on one of those circuits by the common sign \(-1\). Every strong electric weight stays fixed and that single trace changes sign. This change is available also at each centre translate. It follows by Taylor's inequality inside the positive zero-coupling integral that
\[
 |k_t-k_0|\le(1+\delta)(2n^3|t|)^2 e^{2n^3|t|}/2 .
\]
The new magnetic half-weight \(m_t=e^{t\sum_{p\parallel 13}\operatorname{Re}U_p/2}\) is a multiplication operator on a slice. Removing the strong scalar factors as before, write
\[
 B(t)=m_tJm_t+E_t,\quad
 \|E_t\|_{\rm HS}\le C(\delta+n^6 |t|^2),\qquad |t|\le c/n^3 .             \tag{3}
\]
The first summand has rank one and trace \(a(t)=\int m_t^2\,dp\). For small absolute \(c\), \(|a(t)-1|\le e^c-1<1/4\) and \(J_t=m_tJm_t/a(t)\) is a projection of norm at most 2. Apply the contour proof of Stage 3 to \(B(t)/a(t)=J_t+E_t/a(t)\). For an idempotent of norm at most two, its resolvent is \(J_t/(z-1)+(I-J_t)/z\), bounded by 10 on the contour used there. Thus the spectral projection changes by at most \(C\|E_t\|_{\rm HS}\), its eigenvalue differs from 1 by at most \(C\|E_t\|_{\rm HS}\) (or use the rank-one trace on that projection), and the remaining operator has Hilbert–Schmidt norm at most \(C\|E_t\|_{\rm HS}\), as in Stage 3. In particular for
\[
            r=\sqrt{\delta}/(12n^3),\qquad
            \max_{|t|\le r}|P(t)-1|\le C(C\delta)^u .                       \tag{4}
\]
Applying Cauchy's bound on this circle also extends the estimate (1) up to \(m\le(2-\epsilon)u\), with a possibly smaller absolute \(c\). No zero locations have been inferred from Taylor coefficients alone.

**ARGUED (decisive next test).** At a very small positive \(t_*=n^{-5}\) the weak electric coefficient on each transverse fundamental link is proportional to \(t_*\). A contractible rectangle uses two of them. There are order \(\alpha^2\) different rectangles in one thin strip with independently movable endpoints. If their magnetic trace fluctuations are coherent in the actual spatial measure, the second eigenvalue can be at least a constant times \(\alpha^2 t_*^2\) relative to the first. Its \(u\)-th power can then be compared with (4) by the maximum principle. This would test *bounded* holomorphic continuation on the exact diagonal, without assuming anything about the seed. The needed sign is a real covariance in a specified Wilson measure; orthogonality of spin networks against Haar alone would give no such gain.


## Stage 5. Coherent rectangles in a magnetic slice

**PROVED (a real excitation seen by the homogeneous path).** There is an absolute \(b_1>0\) such that, at \(t_*=n^{-5}\) and all sufficiently late cutoffs, the two largest neutral eigenvalues in nonincreasing order satisfy
\[
       \lambda_2(T(t_*))/\lambda_1(T(t_*))\ \ge\ b_1\alpha^2t_*^2.          \tag{5}
\]
In particular for **every** integer \(v\ge2\), with the same \(n,\alpha,t_*\),
\[
          1-P_v(t_*)\ge \tfrac12(b_1\alpha^2t_*^2)^v,\qquad
          P_v(t)=\frac{\operatorname{Tr}_H T(t)^{2v}}
                           {(\operatorname{Tr}_H T(t)^v)^2}.                 \tag{6}
\]
This test concerns the actual homogeneous transfer at positive anisotropic couplings. All rectangles below are contractible and centre neutral.

**Proof of the magnetic estimate.** On a spatial slice at \(t=0\) the magnetic law \(p\) has weights only on faces 12 and 23, at \(\alpha\). Choose a fixed strip in the 23-plane, one step wide along 2. Write \(W_{ab}=\chi_2(U_{ab})=2\operatorname{Re}U_{ab}\) for its rectangle from longitudinal coordinate \(a\) to \(b\) along 3; the subscript on the character is representation dimension. On a common stretch of length \(O(\alpha)\), the joint law of all these traces differs in total variation by \(o(1)\) from that of \(\chi_2(G_{a+1}\cdots G_b)\), with independent \(G_j\) of density proportional to \(e^{\alpha\operatorname{Re}G_j}\) on \(SU(2)\).

To see this, fix axial gauge along 2 on each 2-circuit, leaving its wrapping link \(H\) at the seam, away from the strip step. The successive prefix gauges are triangular changes of Haar variables: integrating each nonwrapping 2-link gauges it to the identity, translates its incident transverse links on the left or right and preserves their Haar measures, leaving normalized Haar for the unused gauge and the winding. Given all \(H\)'s, each transverse spatial edge now has its own length-\(n\) chain along 2 with the central one-link transition at \(\alpha\); at closure the endpoint is a left and right translate of the initial edge by the two windings. The chains are independent conditionally. The marginal of two successive chain levels has density proportional to the single-step kernel times the complementary \((n-1)\)-step kernel at translated arguments. The latter normalized density is within \(\sum_{j\ge2}j^2\rho_j^{n-1}\) of 1 everywhere by the character expansion. Discarding this factor and renormalizing costs \(1+O(e^{-(n-1)/(1+\alpha)})\) multiplicatively per observed edge, uniformly in \(H\). This holds for all \(O(\alpha)\) observed edges at once. In the resulting reference the bottom variables \(L_j\) are independent Haar, and the upper variables \(U_j\) have independent central increments \(U_jL_j^{-1}\), independent of the full bottom row. Set \(S_{j+1}=S_jL_j\) starting with the identity at the left end. The upper edges in the gauge making the bottom row identity are \(S_jU_jS_{j+1}^{-1}\), conditionally independent central increments with the same law. The end vertical links stay identity. Inverting the loop leaves its trace unchanged. This proves the joint comparison including arbitrary bounded functions of the overlapping intervals.

Put \(L=\lceil2\alpha\rceil\), and take all \(a\in\{0,\ldots,\lfloor h\alpha\rfloor\}\), \(b\in\{L,\ldots,L+\lfloor h\alpha\rfloor\}\) with a small absolute \(h>0\). Let \(q\) be their number and \(Y=q^{-1}\sum_{a,b}W_{ab}\). Then
\[
                         q\ge c\alpha^2,\qquad \operatorname{Var}_p Y\ge c . \tag{7}
\]
Indeed \(W_{0L}\) has reference mean \(2\rho_2^L\to 2e^{-3}\), since \(1-\rho_2\sim3/(2\alpha)\) by row 1656 (13). Its second moment is \(1+3\rho_3^L\ge1\) from \(\chi_2^2=1+\chi_3\). For a product on \(d\) sites its squared quaternion chordal distance from identity has mean \(2(1-\rho_2^d)\le2d(1-\rho_2)\). By adding and removing the two end segments, the triangle inequality in \(L^2\), bi-invariance of this distance and \(|2\operatorname{Re}U-2\operatorname{Re}V|\le2|U-V|\) give \(\|W_{ab}-W_{0L}\|_2\le C\sqrt h\). The same bound holds for their average. Centering is an orthogonal projection in \(L^2\), so a sufficiently small fixed \(h\) gives a strictly positive lower variance. The preceding measure comparison transfers it since \(|Y|\le2\). At \(t_*\) the magnetic slice law \(p_*\propto M(t_*)^2 dx\) has density ratio to \(p\) between \(e^{-2n^3t_*}\) and \(e^{2n^3t_*}\), preserving the lower bound for all large \(n\).

**Proof of (5) and (6).** For this real calculation normalize *all* electric convolutions to have trivial multiplier 1; this changes no eigenvalue ratio. Under spatial Haar the \(W_{ab}\) are orthonormal. Each simple loop has Haar holonomy and its character has squared integral one; distinct chosen loops have a link used by precisely one, whose fundamental matrix coefficient integrates to zero. Each is an eigenfunction of the electric product, with eigenvalue \(\rho_2(t_*)^2\rho_2(\alpha)^{2(b-a)}\), since its two transverse spatial bonds have temporal coupling \(t_*\) and all its long bonds have temporal coupling \(\alpha\). The series gives \(\rho_2(t_*)/t_*\to1/4\), and \(b-a\le(2+h)\alpha+1\). All other real electric eigenvalues are nonnegative. Thus the electric operator dominates the constant projection plus \(c t_*^2\sum_{a,b}|W_{ab}\rangle\langle W_{ab}|\). Conjugating the magnetic sandwich to \(L^2(p_*)\) and dividing by the magnetic integral, as in Stage 3, turns this into the same quadratic-form inequality with inner products now in \(L^2(p_*)\). Cauchy–Schwarz in the list of rectangles bounds the sum below by \(q|Y\rangle\langle Y|\). The two nonzero eigenvalues of \(J+c q t_*^2 |Y\rangle\langle Y|\) have product \(c q t_*^2\operatorname{Var}_{p_*}Y\) by its two-vector Gram determinant. Their sum is \(1+c q t_*^2\|Y\|_2^2\le2\). The min-max principle therefore gives the required lower bound on the second eigenvalue in this normalization. The top eigenvalue is at most 2 eventually: the positive electric kernel before weak-bond normalization is bounded pointwise by \(e^{2n^3t_*}(1+\delta)\), and the weak-bond trivial coefficients are at least 1 by Jensen. This is also an operator norm bound against the probability \(p_*\). Dividing proves (5). Finally \(P_v\le 1/(1+s_v)\) with \(s_v=\sum_{i>1}(\lambda_i/\lambda_1)^v\). Its first summand is at least \((b_1\alpha^2t_*^2)^v\le1\), giving (6). \(\square\)

**ARGUED (decision).** The factor \(\alpha^2\) comes from coherence in the magnetic law of different loops. If the endpoint traces were replaced by independent Haar readings the variance of their average would be \(1/q\). This is a property of the interacting endpoint. The same coherent strip also exists in the weak abelian model and in a five-dimensional path with time at a leaf, so (5) does not select the desired phase. It can, however, contradict a bounded analytic disk for the four-dimensional law itself. Next compare (4) and (6) without deforming either slab.


## Stage 6. Bounded continuation on the homogeneous diagonal fails

**PROVED.** There is an absolute \(W>0\) such that for all sufficiently late \(K\) and every integer \(v\ge u\), on \(|t|\le W/\alpha\) either \(P_v\) has a pole or \(\sup|P_v-1|\ge e^v\). In particular a holomorphic, cutoff-uniformly bounded continuation to a tube about \([0,\beta_K]\) of width \(\omega(1/\beta_K)\) is impossible already at its tree end, with both slabs at the **identical** coupling. This does not yet decide whether every short zero could be removable in a pole-free but unbounded family.

**Proof.** In (4) replace \(u\) by any \(v\ge2\); the one-step proof is unchanged. Put \(w=W/\alpha\) and \(t_*=n^{-5}\). For fixed \(W>0\) eventually \(r<t_*<w\). If \(P_v\) is holomorphic there, let \(M=\max(1,\sup_{|t|\le w}|P_v-1|)\). On the annulus from \(r\) to \(w\), the logarithm of the modulus of a holomorphic function has the harmonic upper bound affine in \(\log |t|\) with its two boundary maxima. This follows by the maximum principle for the subharmonic logarithm, also at its zeros. Apply it to \(P_v-1\). By (4),
\[
 \frac1v\log |P_v(t_*)-1|
   \le \frac{\log M}{v}
       +\frac{\log\delta+O(1)}{\log(w/r)}\log(w/t_*).
\]
Here \(\log(w/r)=(-\log\delta)/2+O(\log n)\), \(-\log\delta\ge c n/(1+\alpha)\), and \(\log(w/t_*)=O(\log n)\). Thus the last term is \(-2\log(w/t_*)+o(1)\) uniformly for \(v\ge u\), since \((1+\alpha)(\log n)^2/n\to0\). By (6) the left side is at least \(\log b_1+2\log\alpha+2\log t_*-(\log2)/v\). Consequently
\[
                       v^{-1}\log M\ \ge\ \log(b_1 W^2)-o(1).               \tag{8}
\]
Choose \(W\) with \(b_1W^2>e^2\). \(\square\)

**ARGUED (next question).** An entire function can grow very fast in a complex disk. The numerator could have uncancelled zeros even if all short zeros were removable. To resolve what follows without a bound assumption, count the actual signed divisor of the homogeneous ratio. Row 1165 (25) used a polynomial times a logarithmic derivative for the isotropic periodic ratio, with a conditional real endpoint witness. Here (4) and (6) supply an unconditional witness at \(n^{-5}\) on the anisotropic, centre-projected path.


## Stage 7. Unpaired zeros and poles in the exact ratio

**PROVED (a count without any boundedness assumption).** There are absolute \(C_0,c_0>0\) such that for all sufficiently late \(K\) and all integers \(v\ge u\), the meromorphic function \(P_v\) has at least \(c_0 v/\log n\) **distinct** zeros or poles in \(|t|\le C_0/\alpha\), counted after cancellation. All are nonreal. At the seed period this is a statement about the actual homogeneous, centre-projected ratio. It counts the union of the two signs.

**Proof.** Write \(D_v(t)=\operatorname{Tr}_H T(t)^v\), omitting the scalar Wilson shifts, and \(F_v=D_v/D_v(0)\). The integral in the neutral mixture at \(t=0\) gives \(F_v(t)=\mathbb E e^{tX}\), \(|X|\le3n^3v\); the twist is one of the variables averaged with positive weights. In particular \(\log|F_v(t)|\le3n^3v|t|\). Real \(D_v(t)>0\) follows from the same positive twisted integrals, also at negative real \(t\). Let \(w=W/\alpha\) with a sufficiently large *fixed* absolute \(W\). Jensen's circle formula bounds the number of zeros of \(F_v,F_{2v}\), with multiplicity, in \(|z|\le4w\) by \(Cn^3vw\) in total: each contributes at least \(\log2\) at radius \(8w\), and both functions equal 1 at 0. Jensen's identity here follows by subtracting the logarithms of the disk zero factors and applying the harmonic mean-value identity. Boundary zeros may be treated by a limit.

We give the local partial fraction bound used below. Choose \(s\in(3w,4w)\) avoiding both zero sets on its circle. Divide each \(F\) by its finite disk Blaschke product with factors \(s(z-a)/(s^2-\bar a z)\), including multiplicity. The zero-free quotient has a log whose real part on the circle is \(\log|F|\). The normalized circular integral of \(|\log|F||\) is at most \(C n^3 v w\), because the positive part is so bounded and Jensen gives a nonnegative mean. On \(|z|\le w\) the derivative of this log is bounded by \(C n^3v\). Indeed the Schwarz integral kernel \((s e^{i\theta}+z)/(s e^{i\theta}-z)\) has derivative bounded by \(C/w\); its real part is the Poisson kernel, and two analytic functions with the same real part differ by an imaginary constant. Each disk factor adds \(1/(z-a)+\bar a/(s^2-\bar a z)\) to the log derivative. The second summand and the first summands with \(|a|>2w\) cost \(C/w\) each. Subtract twice the short log derivative from the long one. Thus, as a meromorphic identity on \(|z|\le w\),
\[
 H(z):=P'_v(z)/P_v(z)=\sum_{a\in S}\nu_a/(z-a)+G(z),\quad
 |G|\le Cn^3v,\quad \sum_{a\in S}|\nu_a|\le Cn^3vw .
\]
Here \(S\) consists of the distinct points in \(|z|\le2w\) with nonzero signed order \(\nu_a=\mathrm{ord}_a D_{2v}-2\mathrm{ord}_a D_v\). Put \(p_S(z)=\prod_{a\in S}(z-a)/(3w)\), including each point once. On \(|z|\le w\), \(|p_S|\le1\), and \(p_SH\) is holomorphic, bounded by \(Cn^3v\) there by the last identity (even if \(S\) is empty).

On \(|z|\le r/2\), (4) applied with \(v\) and Cauchy's bound on the small logarithm give \(|p_SH|\le C(C\delta)^v/r\). Use the annulus estimate of Stage 6 between \(r/2\) and \(w\), evaluating at radius \(t_*\), and the maximum principle on its interior. This gives
\[
 \sup_{|z|\le t_*}|p_S H(z)|
   \le \exp\{v[-2\log(w/t_*)+o(1)]\},                                      \tag{9}
\]
uniformly for \(v\ge u\). In detail, the outer log bound divided by \(v\) is \(o(1)\) uniformly in this range. The extra inner term \(\log(1/r)/v\), multiplied by \(\log(w/t_*)/\log(2w/r)\), is \(O(\log n/v)=o(1)\). The other error is \(O((1+\alpha)(\log n)^2/n)\) as in (8). All divisors are outside \(|z|\le c/n^3\) by the separated leading eigenvalue in Stage 3, at both periods. Hence for \(0\le x\le t_*\),
\[
                     |p_S(x)|\ge (c'/(3wn^3))^{|S|}.
\]
Along this real interval take the real logarithm. Equation (6) gives \(-\log P_v(t_*)\ge (b_1\alpha^2t_*^2)^v/2\). At zero (4) bounds \(|\log P_v(0)|\le C(C\delta)^v\), exponentially smaller relative to this displayed lower bound, uniformly for \(v\ge u\). Integrate \(H\) between the two points and use (9), multiplying by the reciprocal of the polynomial bound. Rearrangement yields
\[
        \frac{|S|}{v}\log(3wn^3/c')\ \ge\ \log(b_1W^2)-o(1).
\]
The additional factor \(t_*\) in integration can be discarded since \(t_*<1\). Choosing \(W\) as in Stage 6 proves the assertion with \(C_0=2W\). \(\square\)

**PROVED (short zeros do survive on repeated time doublings).** Keep one sufficiently late spatial box \(n\) and \(\alpha=\beta_K\) fixed. Start at any integer \(v_0\ge u\), and put \(v_j=2^jv_0\). There is an absolute \(C_1\) such that among any \(1+\lceil C_1 n^3\log n/\alpha\rceil\) successive doublings there is a \(j\) for which the total **pole** multiplicity of \(P_{v_j}\) in \(|t|\le C_0/\alpha\) is at least \(c_0 v_j/(4\log n)\).

**Proof.** Let \(B_j\) be the zero count of \(D_{v_j}\) in this same closed disk, with multiplicity, and \(b_j=B_j/v_j\). The Jensen bound above gives \(0\le b_j\le C n^3/\alpha\), uniformly in \(j\). If \(N_j^+,N_j^-\) denote positive and negative divisor masses of \(P_{v_j}\) there, then
\[
 b_{j+1}-b_j=(N_j^+-N_j^-)/(2v_j),\qquad
 N_j^++N_j^-\ge c_0 v_j/\log n .
\]
As long as \(N_j^-<c_0 v_j/(4\log n)\), \(b_j\) increases by at least \(c_0/(4\log n)\). Its upper bound limits every such run as claimed. A boundary zero presents no issue because all counts use the identical closed disk. This supplies actual poles at arbitrarily long periods on each fixed late box. It does not assign one to \(v_0=u\). \(\square\)

**ARGUED (next stage).** At a fixed spatial cutoff, the transfer spectrum might identify the sign at *every* sufficiently long period by comparing the two zero-counting measures per unit time. Such convergence would still need a rate in \(n\) to determine the sign at \(u=n/512\). I will test that approach independently of the real seed.


## Stage 8. Separating the signs at fixed spatial cutoff

**PROVED (both signs at all sufficiently long time periods).** There is an absolute \(C_2\) such that, for each sufficiently late fixed \(n,\alpha\), there exists \(v_{\rm long}(n,\alpha)<\infty\) with the following property. For every integer \(v\ge v_{\rm long}\), the total multiplicity of the poles of \(P_v\) in \(|t|<C_2/\alpha\) is at least \(c_0v/(3\log n)\), and the same is true of its zeros. The time threshold obtained here is nonuniform. The proof uses spectral asymptotics at a fixed spatial size. Row 680 and its check rebuild the compact-operator trace argument and Vesentini's spectral-radius lemma; the following argument also has to rule out different eigenvalues with persistently equal moduli.

**Proof of the spectral limit.** Let \(T(z)\) be the holomorphic neutral transfer of this fixed box, \(D_v(z)=\operatorname{Tr}T(z)^v\), and \(r_T(z)\) its spectral radius. We show
\[
               v^{-1}\log|D_v|\longrightarrow \log r_T
                         \quad\text{locally in }L^1(\mathbb C).              \tag{10}
\]
First fix a unit complex number \(c\ne1\). A *common branch* at a nonzero spectral value \(\lambda\) means a local analytic spectral component on which both \(\lambda\) and \(c\lambda\) are eigenvalues as the parameter varies. We give details to distinguish a persistent relation from a coincidence at an isolated parameter. In disjoint small spectral circles about \(\lambda\) and \(c\lambda\), the resolvent projections have finite constant rank near that parameter by the Neumann series on each circle. Transport a basis by each projection to obtain two finite analytic matrices. Form their monic characteristic polynomials in the *same* spectral variable after rescaling the second circle by \(c^{-1}\). Their monic greatest common divisor over meromorphic germs gives the common components. Its coefficients extend holomorphically at the parameter since its roots on a punctured disk belong to the bounded spectral circles and the coefficients are elementary symmetric functions. The residual coprime polynomials have nonzero resultant off a discrete set (equivalently use their polynomial Bézout identity over the meromorphic germs). Thus the common-component description agrees on overlaps even at isolated coincidences by continuation.

Let \(R_c(z)\) be the greatest modulus of a nonzero point on such a component over \(z\), or zero if none exists. The logarithm of \(R_c\), valued \(-\infty\) at zero, is subharmonic or identically \(-\infty\). To verify this locally above any positive spectral threshold, only finitely many spectral circles need be considered: the complement outside these circles and above the threshold stays in the resolvent on nearby compact sets, with \(\|T\|\) locally bounded. At a positive maximum this gives locally the maximum log modulus of roots of finitely many monic common factors. Away from the discrete discriminants of their square-free parts, this is a finite maximum of logarithms of moduli of analytic roots. It is subharmonic there and extends subharmonically across each exceptional point by continuity of the root multiset (or by taking circular means). At \(R_c=0\) the same finite-circle description at every positive threshold gives upper semicontinuity, and the submean inequality is automatic. This proves the assertion. On an open interval of positive real \(z\) the transfer is positive self-adjoint. No two nonzero eigenvalues there have ratio \(c\). Thus \(\log R_c=-\infty\) on the interval and hence throughout the plane. For the last implication, in a half disk with diameter in the interval compare to the harmonic function with boundary value \(-A\) on the diameter and a fixed upper bound on the arc. The diameter has positive harmonic measure in the interior. Sending \(A\) to infinity gives \(-\infty\) there; the submean inequality propagates this open set across a connected domain. Endpoints of the diameter can equivalently be avoided by using a shorter subinterval as boundary data.

The ordinary \(\log r_T\) is subharmonic by row 680's proof: the decreasing subharmonic functions \(2^{-j}\log\|T^{2^j}\|\) tend to it by the spectral radius formula. It is finite at positive real \(z\), so \(r_T=0\) only on a set of area zero. Indeed a positive-area set with value \(-\infty\) would force the submean over a disk to be \(-\infty\) on a neighborhood, then everywhere. Locally where \(r_T>0\), resolve the finitely many eigenvalues above a smaller threshold into analytic roots off their discrete square-free discriminants. The set where two *different* such roots have equal modulus is area-null: a nonconstant analytic ratio takes the unit circle on a null set by local inversion away from discrete critical points, and a constant unit ratio different from 1 was just excluded. Countably many charts suffice. Thus almost everywhere there is a single distinct eigenvalue \(\lambda\) of maximal modulus, of some finite algebraic multiplicity \(m\ge1\). Its trace contribution is \(m\lambda^v\), also for a Jordan block. For the complementary Riesz restriction \(S\), with \(r(S)<|\lambda|\), \(|\operatorname{Tr}S^v|\le\|S\|_1\|S^{v-1}\|\) is \(o(|\lambda|^v)\) by the spectral radius formula. This proves pointwise almost-everywhere convergence in (10).

For local integrability and convergence fix a disk \(|z|\le R\) at this spatial cutoff. The \(L^2\) norms on it of \(v^{-1}\log|F_v|\) are bounded uniformly in \(v\). Use the disk factorization of Stage 7 at a radius between \(2R\) and \(3R\), with zero count \(O_{n,R}(v)\) by Jensen. The harmonic log modulus after removing these factors is bounded on \(|z|\le R\) by \(O_{n,R}(v)\) using the Poisson kernel and its circular \(L^1\) bound. Each log modulus of a disk factor has bounded \(L^2\) norm there, uniformly in the zero position: the only unbounded part is \(\log|z-a|\), whose square is integrable on a common larger disk after translation. The triangle inequality gives the assertion. The scalars \(v^{-1}\log D_v(0)\) are bounded by positivity of the tree transfer, its nonzero top eigenvalue and its finite trace norm. Uniform \(L^2\) boundedness gives uniform integrability in \(L^1\) by Cauchy–Schwarz, so the almost-everywhere limit proves (10).

Choose a nonnegative smooth cutoff \(\phi\le1\), equal to 1 on \(|z|\le C_0/\alpha\), supported in \(|z|<2C_0/\alpha\). With the spatial box fixed, (10) implies
\[
 \frac{1}{v}\sum_a \big(\mathrm{ord}_aD_{2v}-2\mathrm{ord}_aD_v\big)\phi(a)
                     \longrightarrow 0 .
\]
Indeed integrate each log modulus against \(\Delta\phi/(2\pi)\); near a zero \(a\) of order \(k\) the log is \(k\log|z-a|\) plus a harmonic function, giving \(k\phi(a)\) by integration on small circles. The two limits cancel. By Stage 7 the total **absolute** signed order weighted by \(\phi\), divided by \(v\), is at least \(c_0/\log n\). The two conclusions give the stated lower bound for each sign, with \(C_2=2C_0\). \(\square\)

**ARGUED (where the sign proof stops).** The local \(L^2\) bound and the separation of eigenvalues in (10) depend on the spatial volume. The proof gives no estimate making \(v_{\rm long}\le n/512\). At the stipulated aspect, the proved alternatives are the signed-union count and the failure of bounded continuation, not a sign-resolved count. I next test a different real interpolation, on which magnetic freezing changes the law of the spatial slice. That test can distinguish the weak comparison models without attaching a selection mask to a plaquette.


## Stage 9. A separate real limit of the unmodified neutral trace

**ARGUED (route and comparison line).** Take the temporal star as the active tree, so every electric face has coupling \(a>0\) and every spatial face has coupling \(s\). This is another member of the tree paths in row 1656. Now hold the spatial side \(n\) and time period \(v\ge2\) fixed. Send \(s\to+\infty\) first, then \(a\to+\infty\). The selection to test is in the **spatial Wilson probability measure** integrated at every time slice. In three spatial dimensions regular commuting triples may carry mass arbitrarily close to the all-central strata with a singular, integrable density. A fourth spatial winding changes that mass concentration. For compact \(U(1)\), even with only the same order-two centre translations projected out, electric evolution on the flat spatial torus can have a different normalized trace because its flat probability density is translation invariant. Strong magnetic disorder has support beyond flat orbits in all these families. These are hypotheses about a real positive measure, with no extra observable inserted. They must be tested quantitatively. This changes the order of limits in the question, so any physical carry would require a separate comparison with \(s=a=\beta_K\).

**ON FILE (rows 884, 1028, 1143/1144, 1145/1146, 1384, 1656).** The finite-group frozen examples already retain several centre-neutral classes of commuting triples. Row 1143 supplies a conditional comparison between the Wilson integral at fixed windings and a commutator integral, with the comb-tree pivots from row 1028. Check 1384 analyzes the critical dimension of that integral. The scalar fluctuation determinant for untwisted *four*-dimensional weak fields was computed in row 1145. I use those arguments, with the spatial torus as its own Wilson system. The extra PR 10114 hit LCONV55.md 197 concerns perturbation of a six-dimensional nullspace. It does not give this spatial probability law or its time transfer.


## Stage 10. The spatial law when the magnetic coupling goes to infinity

**PROVED.** For a fixed spatial cube of side \(n\ge3\), put \(N=n^3\), and let \(\mu_s\) be the normalized spatial \(SU(2)\) Wilson measure with coupling \(s\), pushed to the quotient by vertex gauges and centre translations. As \(s\to\infty\) it converges to a probability on flat connections. Write the commuting winding matrices as \(e^{\theta_i e}\) on a common unit quaternion axis. The quotient coordinates are \(\theta\in(\mathbb R/\pi\mathbb Z)^3\) modulo simultaneous inversion. Away from the all-central point their limiting density, up to a constant fixed by total mass, is
\[
 h_n(\theta)=
   \prod_{p\in(\mathbb Z/n)^3}
    \left[4\sum_{i=1}^3
          \sin^2\!\left(\frac{2\pi p_i+2\theta_i}{2n}\right)\right]^{-1}.    \tag{11}
\]
In particular it behaves as \(H_n|\theta|^{-2}(1+o(1))\) at zero, with \(0<H_n<\infty\) after normalization. It has no atom there. In four spatial dimensions the corresponding neutral quotient instead converges to the point mass on the trivial flat orbit. For compact \(U(1)\) it is uniform on the torus of flat windings modulo the chosen centre translations.

**Proof of control near singular flat fields in three space dimensions.** Gauge-fix a comb tree as in row 1143 (1). Keep the three wrapping-edge windings. In dimension three the number of residual Haar pivots is \(M=3N-(N-1)-3=2N-2\). At fixed winding tuple the two bounds of row 1143 apply with positive constants depending on \(n\): a lower integral \(I(C_ns)^M e^{-C_ns A_h}\) and an upper integral \(I(c_ns)^M e^{-c_ns A_h}\), with \(A_h=\sum_{i<j}(1-\operatorname{Re}[h_i,h_j])\) and \(I(b)=\int e^{-b(1-\operatorname{Re}g)}dg\asymp b^{-3/2}\). For clarity, put all interior background links to 1 and the wrapping links in direction \(i\) to \(h_i\). Telescoping face products bounds the action above by a fixed sum of the pivot link deficits plus \(C_n A_h\). For the reverse bound, replace each free pivot successively by a distinct triangular plaquette using the first earlier nonzero coordinate, with interior edges before wrapping edges, as in row 1143 lines 37–44. The action dominates the sum of their deficits, and each winding commutator is a product of conjugates of the faces of its fundamental rectangle, giving \(A_h\le C_n A\). Both changes preserve product Haar conditional on the windings. The one-link power follows by the quaternion polar integral with \(\sin^2 u\,du\) near 0.

In winding polar coordinates write \(r_i=|\sin\theta_i|\), \(r=\max r_i=r_k\). The identity \(1-\operatorname{Re}[h_i,h_j]=2r_i^2r_j^2|\omega_i\times\omega_j|^2\) bounds the whole sum above and below by constant multiples of \(r^2\sum_{i\ne k}r_i^2|\omega_i\times\omega_k|^2\). The upper bound uses the triangle inequality for perpendicular parts against \(\omega_k\). Given \(\omega_k\), a uniform axis has uniform cosine to it on \([-1,1]\); integrating the exponential of minus \(b\) times the squared sine gives bounds \(c/(1+b)\) and \(C/(1+b)\), by \(1-|x|\le1-x^2\le2(1-|x|)\). The quotient of the upper angular mass element by \(s^{-2}\) is bounded by
\[
           C s^2\prod_i r_i^2\prod_{i\ne k}(1+c s r^2r_i^2)^{-1}
                       \,d^3\theta\ \le\ C' r^{-2}d^3\theta .
\]
On a fixed regular angular patch with all \(r_i\) bounded below, the lower comparison gives at least \(c_n s^{-2-3M/2}\) total mass by the same angular integral. Dividing, the probability that every winding is within angular distance \(\eta\) of a central element is at most \(C_n\eta\) for small \(\eta\), since \(r^{-2}\) is locally integrable in three variables. Off the zero set of the spatial action, positive action bounded away from zero costs exponentially in \(s\), against this polynomial lower mass. This excludes lost mass in the singular stratum. The on-file four-dimensional crossover for winding radii, used below, has a different power at this step.

**Proof of (11) on regular flat fields.** A flat field is determined up to gauge by its three commuting winding matrices: transport from a base point on the universal cover is path independent modulo the prescribed windings by cancellation across faces. At a regular flat triple its common stabilizer is a circle. Locally the flat fields are parametrized by the three angles and the vertex gauge group modulo this circle, up to the discrete Weyl identification. One can choose the axis smoothly using any noncentral winding. Take a representative with constant links \(e^{\theta_i e/n}\). The derivative of a vertex gauge is the covariant difference from vertex to edge; the linearized plaquette is its covariant curl. In the colour along \(e\) these have the ordinary Fourier differences. Identify the perpendicular real colour plane with one complex coordinate. Its covariant shifts have symbols
\[
       z_i=\exp[i(2\pi p_i+2\theta_i)/n]-1 .
\]
Indeed conjugation by a link rotates this plane by \(2\theta_i/n\). The maps on this mode are \(q\mapsto z q\) and \(X\mapsto z\wedge X\), up to unitary choices of link or face frame. For \(z\ne0\), \(|z\wedge X|^2=|z|^2|X|^2-|\bar z\cdot X|^2\). The one complex gauge direction contributes \(|z|^2\) to the volume Jacobian of the gauge orbit. Each of the two complex normal directions contributes \(|z|^{-2}\) from its Gaussian integral. Their product gives \(|z|^{-2}\) per charged momentum, precisely the factor in (11). The neutral-colour nonzero modes are independent of the angles. Its zero modes are the constant stabilizer and the three angular tangents; the latter have fixed norms and are orthogonal to gauge differences by summation of a discrete derivative. The stabilizer has constant volume on this regular set. This accounts for the full orbit-volume factor, necessary when integrating with product Haar.

To justify the Gaussian use, the second variation of \(1-\operatorname{Re}U_p\) at a flat field is the squared norm of the linearized curl in the quadratic Taylor term with coefficient \(1/2\). The Fourier computation identifies its kernel exactly with the tangent directions just parametrized. On a compact regular patch, normal coordinates and ordinary Taylor expansion therefore give a common positive quadratic lower bound on the action in a tube and a cubic remainder. Rescale normals by \(\sqrt{s}\); dominated convergence by a Gaussian gives their determinant factor, with the smooth volume density evaluated on the flat locus. Off a smaller tube on compact support the action has a positive minimum. A finite cover and partition of unity give this assertion with any continuous insertion supported on the patch. There are \(9N-(3N-1+3)=6N-2\) real normal variables, in agreement with the power \(s^{-(3N-1)}=s^{-3M/2-2}\) above. Exhausting the regular locus and using the central mass bound proves the normalized limit. In the folded fundamental cell only \(p=0\) is singular near \(\theta=0\), with \(|z|^2\sim4|\theta|^2/n^2\); the other factors stay positive. Translation by \(\pi\) in one angle permutes the momenta. This proves the density assertion on the neutral quotient.

For four spatial dimensions the earlier fixed-four-torus theorem, row 1143 §6 (checked in 1144; see 1384), gives \(-\log(\max_i|\operatorname{Im} h_i|)/\log s\) converging in law to uniform on \([0,1/4]\). Hence \(\max_i|\operatorname{Im}h_i|\to0\) in probability. Positive-action configurations again lose all mass by compactness and a polynomial lower bound from a ball of radius \(s^{-1/2}\) about the identity. Flat central windings form one orbit after the centre quotient. For \(U(1)\), magnetic face weights are invariant under *every* translation of a winding by a circle element, for all \(s\). All weak limits are flat by the same action bound, and on flat fields this invariance forces Haar probability on the remaining winding torus (a point for the full centre). \(\square\)

**PROVED (entry to the thermal comparison).** Take the continuous electric transfer kernel \(k_a(x,y)\) averaged over gauges and the specified centre, with its shifted bond weights \(e^{-a(1-\operatorname{Re}g)}\). If \(\mu_\infty\) is the limit just found, the frozen ratio at any finite \(a>0,\ v\ge2\) is the purity of this kernel acting on \(L^2(\mu_\infty)\). Indeed the original trace of length \(v\) divided by the \(v\)-th power of the one-slice magnetic integral is exactly the integral of \(\prod_{i=1}^v k_a(x_i,x_{i+1})\) against \(\mu_s^{\otimes v}\) with cyclic indices. The convolution and magnetic weights commute with the group projections, so one may average at every join. This continuous bounded integrand passes to the product weak limit; its integral is strictly positive. Iterated kernel composition gives the trace for \(v\ge2\). The ratio cancels the magnetic integrals. In 5D \(SU(2)\) the frozen purity is consequently 1 at every \(a>0\). In 4D \(SU(2)\) a continuum of neutral winding angles remains. The next test is whether the second temporal limit preserves a nontrivial fraction of the trace on these angles.


## Stage 11. A universal neutral transfer in the iterated weak limit

**PROVED.** On the three-dimensional spatial cube at each fixed \(n\ge3\) and integer \(v\ge2\), the unmodified neutral purity satisfies
\[
 \lim_{a\to\infty}\lim_{s\to\infty}P_{n,v}(a,s)
       =\frac{\operatorname{Tr}\mathcal K^{2v}}{(\operatorname{Tr}\mathcal K^v)^2},
 \qquad
 \mathcal K(A,B)=e^{-(|A|^2+|B|^2)/2}
                    \frac{\sinh(A\cdot B)}{A\cdot B}.                       \tag{12}
\]
The fraction in the kernel has value one at zero. The Hilbert space can be taken as the even part of \(L^2(\mathbb R^3,d^3A/|A|^2)\); the kernel annihilates the odd part. An overall positive constant drops out of the trace ratio. In particular the right side is independent of \(n\).

**Proof of the local electric limit.** Lift the density (11) to the symmetric fundamental cell \([-\pi/2,\pi/2]^3\) for the angles modulo \(\pi\), retaining both \(\theta\) and \(-\theta\) with an overall constant. Boundary representatives have zero measure. Use constant-link representatives and normalize Haar at each vertex. The electric kernel is the average over centre translates of the integral over \(g_x\in SU(2)\) of the product of link weights with relative link \(U_i(x)^{-1}g_x V_i(x)g_{x+i}^{-1}\). Set \(\theta=A/\sqrt{an}\), \(\theta'=B/\sqrt{an}\). For fixed \(A,B\), up to a constant \(d_n>0\),
\[
       a^{3(N-1)/2} k_a(\theta,\theta')\ \longrightarrow\
                                  d_n\mathcal K(A,B).
\]
For the trivial centre term at \(\theta=\theta'=0\) the minimizing vertex fields are the constant \(g_x=g\). Fix the root value \(g\), and in the remaining variables use \(g_x=\exp(\xi_x/\sqrt a)g\), \(\xi_{\rm root}=0\). At the scaled angles, the linearized mismatch on direction \(i\) in units \(a^{-1/2}\) is
\[
       \xi_x-\xi_{x+i}+ n^{-3/2}(B_i\operatorname{Ad}(g)e-A_i e).
\]
The sign convention for the difference has no effect on the expression below. The constant term is orthogonal to every discrete gradient by telescoping on the periodic cube. Summing half the squared mismatches gives the rooted scalar gradient quadratic form in three colours and the separate term \((|A|^2+|B|^2-2(A\cdot B)e\cdot\operatorname{Ad}(g)e)/2\), since \(N=n^3\). The rooted gradient form is positive definite. The Haar Jacobian after rescaling tends to a fixed positive constant. For dominated convergence, the action for these near-identity links is bounded below by a fixed positive multiple of \(\sum_{xy\ {\rm tree}}|g_x-g_y|^2\) minus \(C_{n,A,B}/a\), by the triangle inequality and squaring. On a finite tree this sum bounds \(\sum_x|g_x-g|^2\) times a positive constant; quaternion chordal distance on the principal exponential chart bounds the log distance below by a constant multiple. This gives a Gaussian majorant in all rooted chart variables, uniformly in the root. The angular average of \(\exp[(A\cdot B)e\cdot\operatorname{Ad}(g)e]\) is the stated hyperbolic-sine factor because that cosine is uniform on \([-1,1]\). A nontrivial centre translate has a winding mismatch bounded below as the two angles tend to zero. The following global estimate gives its exponential suppression. All constants from the root Gaussian and the trivial translate are independent of \(A,B\).

**Proof of a global majorant and of trace convergence.** For any two flat representatives, gauge-equivalently in seam gauge, choose a nonwrapping spatial spanning tree. From half the electric action keep the positive tree terms, and integrate its vertex variables conditional on the root. Successive changes from vertex spins to the relative link on the tree have unit Haar Jacobian; this factor costs at most \(C_n a^{-3(N-1)/2}\) for \(a\ge1\). From the other half of the action keep the lower bound from the three based coordinate windings. Telescoping the mismatches on each winding gives its squared chordal distance, after conjugation by the root, at most \(C_n\) times that half-action before multiplication by \(a\). Conjugacy class angle distance is no larger than group geodesic distance and on the compact quaternion sphere the latter is bounded by a constant times chordal distance. Folding the class angle by sign of the centre cannot increase distances. Thus for all centre translates, uniformly on the angle cell,
\[
        0\le k_a(\theta,\theta')\le C_n a^{-3(N-1)/2}
              \exp[-c_n a\sum_i (|\theta_i|-|\theta_i'|)^2].                \tag{13}
\]
Before folding, a translate changing a sign indeed incurs a fixed positive mismatch when both original angles are small. Both bounds follow from the same action split, without dividing by a possibly small integral.

At scale \(\sqrt{an}\) the pushed-forward measure in (11), multiplied by \(\sqrt{an}\), has density with respect to \(d^3A/|A|^2\) bounded by \(C_n\) and tending pointwise to \(H_n>0\). This uses the one central singularity and smooth bounded density off it. Extend by zero outside the expanding cell. Transfer the kernel to this fixed Hilbert space by multiplying by the square roots of the two density factors, then remove the scalar \(a^{-3(N-1)/2}(an)^{-1/2}\) from the operator. Its kernel converges pointwise to \(d_nH_n\mathcal K\), and (13) supplies a Hilbert–Schmidt majorant. Indeed, after folding into octants, the squared norm is bounded by a constant times
\[
           \int_{\mathbb R^3\times\mathbb R^3}
             \frac{e^{-c_n|x-y|^2}}{|x|^2|y|^2}\,dx\,dy<\infty .
\]
At a fixed nonzero displacement \(z\), the integral of \(|x|^{-2}|x-z|^{-2}\) is \(C/|z|\) by rotation, scaling, integrability at its two separated singularities and decay as \(|x|^{-4}\) at infinity. The last Gaussian integral against \(|z|^{-1}\) is finite. Dominated convergence gives Hilbert–Schmidt convergence. For powers \(v\ge2\), convergence of their traces follows by telescoping the powers, using two Hilbert–Schmidt factors in each trace bound and bounded operator norms for the rest. The limiting kernel is nonzero and positive semidefinite by its power series in even tensor powers of \(A\cdot B\). This proves (12). \(\square\)

**PROVED (size and selectivity of the effect).** For the very same numerical threshold as the seed, all \(v\ge2\) obey
\[
 \frac{457}{625} < \left(\frac{25}{29}\right)^2
 \ \le\ \frac{\operatorname{Tr}\mathcal K^{2v}}
                 {(\operatorname{Tr}\mathcal K^v)^2}\ <1 .                 \tag{14}
\]
In 5D \(SU(2)\) the iterated purity equals 1. In 4D compact \(U(1)\), if only the same order-two centre translations are projected out it equals 0, and if the entire continuous centre is projected out it equals 1. These alternatives specify the comparison without relying on a choice of abelian projection to obtain the strict intermediate value in (14).

**Proof of (14).** Put \(f(A)=e^{-|A|^2/2}\). The series of positive finite-rank kernels \(f(A)f(B)(A\cdot B)^{2k}/(2k+1)!\) has sum of traces
\[
 4\pi\int_0^\infty \frac{1-e^{-2r^2}}{2r^2}\,dr
     =4\pi\sqrt{\pi/2}=\sqrt{2}\,\|f\|_2^2,\qquad
                 \|f\|_2^2=2\pi^{3/2}.
\]
Integration by parts gives the integral. Summability of the nonnegative traces gives trace-norm convergence and identifies the trace sum with that of \(\mathcal K\). The Rayleigh quotient on \(f\), keeping the first two terms, is at least \((73/72)\|f\|^2\). Under the probability proportional to \(f^2\,d^3A/|A|^2\), the radial second moment is \(1/2\) and independent unit directions have mean squared dot product \(1/3\). Thus the second term relative to the first is \((1/2)^2/(3\cdot 3!)=1/72\). If \(\Lambda\) is the top eigenvalue, the excitation sum at one step satisfies \(\operatorname{Tr}\mathcal K/\Lambda-1\le72\sqrt2/73-1<2/5\), using \(\sqrt2<17/12\). At \(v\ge2\) the sum of the \(v\)-th powers of the excited ratios is at most \((2/5)^2=4/25\). The ground term in the numerator alone now gives the lower bound in (14). The strict upper bound follows from rank at least two: the \(k=1\) positive kernel has among its range functions \(f(A)A_1^2\), independent of \(f\). The square of the sum of the positive powered eigenvalues then strictly exceeds their sum of squares. All inequalities here are hand estimates.

For 5D and the full abelian centre the point-support conclusion of Stage 10 gives the result. For the abelian order-two quotient the frozen angle measure remains uniform on a three-torus and the kernel is a convolution by a positive function \(g_a(\theta'-\theta)\). This follows by cancelling the commuting flat link phases in the electric integral. On this torus, \(g_a/\int g_a\) tends to the point mass at zero as \(a\to\infty\). Away from coincidence modulo the projected translations the winding mismatch has a fixed positive lower bound on compact sets, giving exponential suppression. The denominator has a polynomial lower bound by integrating angles within \(a^{-1/2}\) and all vertex phases within \(a^{-1/2}\) of a common phase, where the shifted action times \(a\) is bounded. The normalized convolution has top eigenvalue 1 and every fixed Fourier multiplier tends to 1; all multipliers are nonnegative by electric positivity. For any finite number of distinct Fourier modes the vacuum-normalized \(v\)-trace has lower limit at least that number. Hence it diverges and the purity tends to zero by \(\sum r_i^{2v}\le\sum r_i^v\). This uses fixed \(v\) before either coupling limit. \(\square\)

**ARGUED (what the comparison reads).** The transition to a point mass in four spatial dimensions occurs in the spatial *Wilson* winding law. The enhancement \(h_n(\theta)\sim H_n/|\theta|^2\) in three spatial dimensions supplies exactly the integrable Hilbert–Schmidt envelope in (12). The abelian flat law with a discrete projection has no such enhancement; its infinitely many translation modes survive the second limit. There is no mask, and the real trace itself has three different outcomes under the same discrete convention. At small positive couplings and fixed spatial size all three real finite-volume transfers with this convention have full-support magnetic measure and more than one neutral state, hence purity strictly between zero and one. For example the positive constant and a contractible plaquette character are independent in \(L^2\) and both electric Fourier channels have strictly positive multipliers. Thus neither group nor dimension fixes the rank collapse of the frozen law for all couplings. A three-dimensional compact \(U(1)\) model with discrete projection also loses purity in the same iterated limit; this is not a test of its physical mass gap. A product with a spectator need not preserve the numerical purity since traces multiply. The limit order in (12) remains the decisive restriction. Next compare it with the actual equal-coupling law and test an escape from the fixed-box limit.

**Decision after Stage 11.** The strict intermediate value reads a probability law at the two limits. The lower bound alone passes in 5D as well. Moving the estimate to the isotropic endpoint would require comparing two different spatial laws as the cutoff grows. I next test whether there is even a fixed-box comparison of their purities.

## Stage 12. The two weak limits on a fixed box disagree

**ON FILE (rows 1143/1144, 1227/1230, 1642).** Row 1143 (11) computes the leading fixed-rectangle *untwisted periodic* partition function in four dimensions. Its subscript \(+\) in that equation labels periodic signs. I denote that trace by \(Z^{\rm per}\) here. Rows 1227 and 1642 already settle the continuum quartic Hamiltonian and thermal time of the one-spatial-vertex model, including the failure of a homogeneous spatial restriction at the bare coupling. I use that result for comparison. The calculation below integrates the nonconstant modes of the whole \(n^3\)-site slice at a different joint limit.

**PROVED (loss of the frozen bound at the isotropic endpoint for fixed periods).** For each fixed \(n,v\ge3\), with \(N=n^3\), the neutral isotropic purity obeys
\[
             P_{n,v}(a,a)\asymp_{n,v} a^{-3/2}/\log a
                      \qquad(a\longrightarrow\infty).                     \tag{15}
\]
Indeed the on-file formula with shifted Wilson weights gives \(Z^{\rm per}(w)\sim c_{n,w}a^{-(9Nw-3)/2}\log a\), \(w=v,2v\), with positive constants. Each of the eight real twisted integrals is positive. The trace on an invariant subspace is at most the full periodic trace by positivity of the transfer. Thus \(Z^{\rm per}(w)/8\le Z_+(w)\le Z^{\rm per}(w)\). Inserting these inequalities at both periods proves (15). All normalizations that are a scalar per time step cancel. In particular for each such fixed box, however large, the actual isotropic purity eventually lies below \(457/625\) while its iterated magnetic-first limit in (14) lies above. This does not disprove a seed with \(a=O(\log n)\). The constants and crossover coupling in (15) depend on the box.

**ARGUED (next test).** A divergent ratio \(s/a\) might appear to suffice to enter (14). Test the intermediate scaling \(s=\gamma n^3a^2\) on the full cube, \(\gamma>0\) fixed. The real estimate that must discriminate is the thermal law of the based winding vectors after integrating the nonconstant magnetic fluctuations. In the abelian theory all winding commutators vanish. In four spatial dimensions even the magnetic-first probability collapses to the central orbit by Stage 10. A calculation at fixed \(\gamma\) in three spatial dimensions alone will not establish a comparison at the calibrated endpoint.

## Stage 13. A simultaneous limit of the full Wilson transfer

**PROVED (joint magnetic and electric scaling at fixed box and period).** Fix \(n\ge3,\ v\ge2,\ 0<\gamma<\infty\). In the temporal-star family,
\[
 \lim_{a\to\infty}P_{n,v}(a,\gamma n^3 a^2)
      =p_v(\gamma):=\frac{\operatorname{Tr}K_\gamma^{2v}}
                           {(\operatorname{Tr}K_\gamma^v)^2}.              \tag{16}
\]
For \(X=(X_1,X_2,X_3)\in(\mathbb R^3)^3\) use Lebesgue measure, write
\(U(X)=\sum_{i<j}|X_i\times X_j|^2\), and use normalized rotation Haar measure. The positive Hilbert–Schmidt operator is
\[
 K_\gamma(X,Y)= e^{-\gamma U(X)}\,
        \int_{SO(3)}e^{-\frac12\sum_i|X_i-RY_i|^2}\,dR\,
          e^{-\gamma U(Y)}.                                                \tag{17}
\]
The three spatial links per vertex fluctuate before this limit. The integration over their nonconstant modes produces the harmonic mean of a seam curvature. No spatial link-equality constraint is imposed. The overall normalization of (17) is immaterial.

**Proof, winding and plaquette coordinates.** Fold the sign of each of the three spatial windings, independently on each slice. The centre-averaged electric kernel is invariant under these flips in either argument, and spatial plaquettes are invariant. Work in the comb gauge of Stage 10. The coordinates per slice are three winding matrices \(h_i\) and the \(M=2n^3-2\) triangular plaquette variables \(p_e\). Haar measure is a product, up to constants for the folded cells. For zero pivot curvature \(p_e=1\), the reconstructed field is the seam field, all nonwrapping links 1 and each \(i\)-wrapping link \(h_i\). This field has exactly the prescribed selected plaquettes and windings, hence is the unique triangular reconstruction. Near the central cell write
\[
             h_i=\exp(X_i/\sqrt{an}),\qquad p_e=\exp(\xi_e/\sqrt s).
\]
For bounded \(X,\xi\), the Haar factors after extracting \((an)^{-9/2}s^{-3M/2}\) tend to fixed positive multiples of Lebesgue measure. Put \(\chi_i(x)=1\) on \(x_i=n-1\) and 0 elsewhere. On the \(ij\)-faces the rescaled log curvature tends to
\[
            (dL\xi)_{ij}(x)
         +\frac{2\sqrt s}{an}\,(X_i\times X_j)\,\chi_i(x)\chi_j(x).
                                                                            \tag{18}
\]
Here \(L\) is the linearized reconstruction of link coordinates for perturbations of the pivot variables at identity. Indeed the seam plaquette is 1 except at a double seam, where it is the group commutator and its second-order log is twice the cross product. Perturbing the pivots adds their linearized curl, because the derivative of reconstruction tends to its derivative at identity. Taylor remainders after multiplication by \(\sqrt s\) tend to zero, uniformly on bounded scaled sets, since the seam logarithms are \(O(a^{-1/2})\), the pivots \(O(a^{-1})\), and \(\sqrt s=O_n(a)\). A change of orientation reverses both face coordinates together.

The range of \(dL\) consists of all exact periodic two-forms, in each colour. To see this, start from any one-form, subtract a gradient to set its tree links to zero, then subtract three closed seam one-forms to kill its three based winding periods. Those forms vanish on the nonwrapping tree. What remains is an arbitrary linearized free-link variation, parametrized invertibly by the triangular plaquette coordinates. Furthermore \(dL\) is injective since each of the selected curls is its own pivot variable. The second term in (18) is closed, as an \(ij\) component is independent of coordinates other than \(i,j\). Its orthogonal projection off exact two-forms is its spatial mean. At every nonzero Fourier momentum the differential is exterior multiplication by a nonzero vector of differences; contraction by the conjugate vector divided by its squared norm gives a contracting homotopy. Only the constant Fourier modes remain. The mean of \(\chi_i\chi_j\) is \(1/n^2\). Since the Wilson action tends to half the sum of squared rescaled curls, Gaussian integration in \(\xi\) therefore gives a positive constant independent of \(X\), times
\[
       \exp\!\left[-\frac{n^3}{2}
                 \left(\frac{2\sqrt s}{an^3}\right)^2 U(X)\right]
           = e^{-2\gamma U(X)} .
\]
In particular no angle-dependent determinant was discarded at this scale.

**Proof, electric integration.** Apply the rooted vertex change of variables of Stage 11 to neighbouring slices with bounded \(X,Y,\xi,\xi'\). For the identity translate the electric mismatch in units \(a^{-1/2}\) is a rooted vertex gradient plus the seam one-form \(\chi_i(RY_i-X_i)/\sqrt n\), with \(R\) the adjoint of the root gauge. Pivot fluctuations are \(O(a^{-1})\) and vanish at this scale. This seam one-form is closed. Its difference from its constant mean is an exact gradient by the same Fourier identity, and can be absorbed by a translation of the rooted Gaussian variables. The squared norm of the constant part is \(\sum_i|RY_i-X_i|^2\). The determinant of the rooted Gaussian is independent of every endpoint. The local majorant follows from the same tree gradient estimate as in Stage 11. At bounded scaled endpoints all nontrivial centre translates have a winding mismatch bounded below, so after averaging only a fixed scalar survives. Thus \(a^{3(n^3-1)/2} k_a\) tends to a positive constant times the central kernel in (17), including the root rotation average.

**Proof, uniform tails for the cyclic integrals.** A bound of type (13) holds for *arbitrary* spatial slice fields with folded based winding angles \(\varphi_i,\varphi_i'\in[0,\pi/2]\). The tree integrals with half of the electric action cost at most \(C_n a^{-3(n^3-1)/2}\), also in the presence of arbitrary deterministic spatial links on that tree by Haar translation. The other half bounds the squared differences of the three based angles by telescoping mismatches on their paths, as in Stage 11. Put \(r_i=\sqrt{an}\,\varphi_i\). After removing the scalar per electric kernel the resulting bound is \(C_n\exp(-c_n|r-r'|^2)\). The winding marginal under the unnormalized magnetic measure, after removing \(s^{-3M/2}(an)^{-9/2}\), is bounded on the positive octant by
\[
 C_n\prod_i r_i^2\prod_{i\ne k}(1+c_{n,\gamma}r_k^2 r_i^2)^{-1}\,d^3r
       \ \le\ C_{n,\gamma}|r|^{-2}d^3r,\qquad r_k=\max_i r_i .
\]
This follows from the commutator marginal bound in Stage 10, using \(\sin\varphi\asymp\varphi\) on the folded interval and \(s/(an)^2=\gamma n\). The cyclic product of the resulting Gaussian majorants against these radial measures is integrable for any \(v\ge2\). Indeed the Gaussian kernel on the octant is Hilbert–Schmidt for measure \(|r|^{-2}d^3r\) by the displacement integral following (13); the cyclic integral on truncated domains is bounded by its Hilbert–Schmidt norm to power \(v\), then use monotone convergence. Removing the part where any \(r\) exceeds \(B\) therefore costs \(o_{B\to\infty}(1)\) uniformly in \(a\). At bounded \(r\) the original magnetic action dominates the sum of the selected plaquette deficits. For principal logarithms this supplies \(e^{-c\sum_e|\xi_e|^2}\) globally, with bounded rescaled Haar Jacobians. It justifies truncating all \(\xi\)'s before the local limits above.

Consequently the cyclic integral divided by the \(v\)-th power of
\(s^{-3M/2}(an)^{-9/2}a^{-3(n^3-1)/2}\) tends to a constant per slice times the cyclic integral of (17). Splitting each \(e^{-2\gamma U}\) into its two equal factors gives the displayed kernel. Positivity follows from Gaussian convolution composed with the commuting rotation projection, conjugated by the positive multiplier. Its Hilbert–Schmidt bound follows from the same radial argument directly in \(\mathbb R^9\), since angles between colour vectors integrate to the same commutator bound. The nonzero kernel has strictly positive thermal traces. The per-slice constants cancel at the two periods, proving (16). \(\square\)

**Decision after Stage 13.** This gives a full-box reduction at fixed positive \(\gamma\) with a finite time step. Row 1227 previously obtained a continuous-time quartic oscillator in its one-vertex problem. I next test which side of the seed inequality this new limit takes as \(\gamma\) varies, and what its bare substitution would predict at the physical aspect.

## Stage 14. The crossover and its failure at the bare physical parameters

**PROVED.** The function \(p_v(\gamma)\) of (16) is continuous on \((0,\infty)\) for each \(v\ge2\), and
\[
     \lim_{\gamma\downarrow0}p_v(\gamma)=0,\qquad
     \lim_{\gamma\to\infty}p_v(\gamma)
          =\frac{\operatorname{Tr}\mathcal K^{2v}}
                         {(\operatorname{Tr}\mathcal K^v)^2}.               \tag{19}
\]
In particular \(p_v\) takes the value \(457/625\) and takes values strictly on either side. This is an existence assertion about crossings.

**Proof near zero, including varying periods.** Normalize Gaussian convolution in nine dimensions to have operator norm one. On simultaneous rotation invariants put \(h=\gamma^{1/3}\) and make the unitary dilation \(X=\gamma^{-1/6}Y\). The operator (17) then has the same eigenvalue ratios as
\[
            S_h=e^{-hU}e^{h\Delta/2}e^{-hU}                                \tag{20}
\]
on invariant \(L^2(dY)\). This is a positive contraction. For any finite \(m\) choose \(m\) orthonormal smooth compactly supported invariant test functions, for instance functions of \(|Y|\) on disjoint shells. On their span the supports, Dirichlet integrals and \(U\) are uniformly bounded for unit vectors by constants depending on \(m\). Thus \(\|(e^{-hU}-1)f\|\le C_m h\) and \(\langle f,e^{h\Delta/2}f\rangle\ge 1-(h/2)\|\nabla f\|^2\) by the Fourier multiplier. Min-max gives \(\lambda_m(S_h)\ge1-C'_m h\). The top eigenvalue is at most one. At any sequence \(h\downarrow0,\ v\ge2,\ vh\to0\), the vacuum-normalized \(v\)-trace has lower limit at least \(m\), by keeping those \(m\) terms. The purity is at most the reciprocal of that trace. Sending \(m\) to infinity proves the first part and the stronger conclusion
\[
          v\,\gamma^{1/3}\longrightarrow0,\quad \gamma\downarrow0
                \quad\Longrightarrow\quad p_v(\gamma)\longrightarrow0 .    \tag{21}
\]
For \(\gamma\) in a compact subinterval of \((0,\infty)\), the squared kernels in (17) are dominated by the squared kernel at the smallest \(\gamma\), integrable by Stage 13. Hilbert–Schmidt continuity, telescoping powers and positivity of the traces give continuity of \(p_v\).

**Proof at infinity.** For \(X_i\in\mathbb R^3\) let \(r_i=|X_i|\). Consider \(\nu_\gamma=\gamma^2e^{-2\gamma U(X)}d^9X\). Its radial marginal is bounded by \(C|r|^{-2}d^3r\), uniformly for \(\gamma>0\): condition on the axis of the longest vector and bound the two remaining angular integrals by \(C/(1+c\gamma r_k^2r_i^2)\), just as in Stage 10. On every compact set \(\nu_\gamma\) converges weakly against continuous tests to a constant times
\[
       \int_{\mathbb R^3}\int_{S^2} \delta_{(A_1e,A_2e,A_3e)}
                                  \,de\,\frac{d^3A}{|A|^2}.
\]
Here \(de\) is uniform area measure, with arbitrary fixed normalization. To compute it, partition by a longest vector \(X_k=r e\), \(r>0\). Write \(X_i=A_i e+w_i/(\sqrt\gamma r)\), \(w_i\in e^\perp\), \(i\ne k\), and set \(A_k=r,\ w_k=0\). The measure \(\gamma^2d^9X\) becomes \(r^{-2}dr\,de\,d^2A_{-k}\,d^4w\), where \(d^2A_{-k}\) denotes the two remaining scalar coordinates. For \(r\) bounded away from zero the limiting exponent is
\[
            -2r^{-2}\sum_{i<j}|A_iw_j-A_jw_i|^2 .
\]
The terms with \(k\) dominate \(2\sum_{i\ne k}|w_i|^2\) in the negative exponential weight, giving Gaussian domination. In each of the two transverse colours the quadratic form before the common factor 2 has matrix
\((|A|^2 I_2-A_{-k}A_{-k}^{\,t})/r^2\), of determinant \(|A|^2/r^2\). Gaussian integration in both colours multiplies the density by a constant times \(r^2/|A|^2\). Chart ties impose boundaries \(|A_i|=r\) of zero Lebesgue measure. The radial majorant makes the omitted region \(r<\epsilon\) cost \(O(\epsilon)\). Summing charts gives both simultaneous sign representatives with a common factor, since changing \(A,e\) to \(-A,-e\) preserves \(X\). This proves the asserted local limit.

Use these measures at each join of the cyclic trace, extracting \(\gamma^{-2}\) per slice. The averaged Gaussian linking two matrices is at most \(\exp(-|r-r'|^2/2)\) by the reverse triangle inequality on each vector. Its cyclic product against the radial majorants has finite integral by Stage 13; removing large radial entries is uniform in \(\gamma\). Inside compact cutoffs the continuous cyclic integrand passes to the product-measure limit. For \(X_i=A_i e,\ Y_i=B_i e'\), the rotation average is precisely \(\mathcal K(A,B)\), independent of the two unsigned axes, because \(e\cdot Re'\) is uniform on \([-1,1]\). The scalar factors per slice cancel. This proves the second part of (19), and (14) and continuity give the stated crossings. \(\square\)

**PROVED (obstruction to a magnetic-to-electric ratio criterion).** Take any prescribed increasing sequence \(n_j=\ell b^{K_j}\), \(v_j=n_j/512\ge2\), and any divergent lower bounds \(L_j\). There are pairs of actual anisotropic four-dimensional Wilson systems on exactly these boxes, at the **same** electric coupling \(a_j\ge L_j\), with both \(s_j^-/a_j,s_j^+/a_j\ge L_j\), such that
\[
            P_{n_j,v_j}(a_j,s_j^-)<457/625<
                        P_{n_j,v_j}(a_j,s_j^+).
\]
For each \(j\), (19) supplies two finite positive parameters \(\gamma_j^\pm\) giving strict opposite inequalities. Set \(s_j^\pm=\gamma_j^\pm n_j^3a_j^2\). The ordinary fixed-\(j\) limits in (16) give the two strict inequalities for every sufficiently large \(a_j\); increase it to enforce both requested ratios. In consequence a premise consisting solely of weak couplings and an arbitrarily divergent magnetic-to-electric ratio, with this spatial and temporal geometry, cannot guarantee the numerical seed. The electric sequence here is freely chosen, not the release trajectory.

**PROVED (the formal substitution has the wrong answer).** If one evaluates the *limiting operator* at the bare isotropic parameters of the requested tori, its coupling would be \(\gamma=\beta_K/(\beta_K^2 n^3)=1/(\beta_K n^3)\). Then \(v\gamma^{1/3}=1/(512\beta_K^{1/3})\to0\) for \(v=u\), so by (21) its purity tends to zero. This agrees with the thermal-time obstruction for the different one-vertex spatial restriction in row 1227. It is a statement about the operator (17). Extending (16) with vanishing error to those particular \((n,\gamma,a)\) would imply a disproof of the seed; the fixed-parameter proof of (16) supplies no such estimate. Conversely it is impossible to prove the requested lower bound by verifying it for this bare matrix operator and then controlling a vanishing error.

**Decision after Stage 14.** Sending \(s\) to infinity and recovering a positive numerical seed loses control precisely where the magnetic winding law changes. The critical scaling shows that taking both couplings large with \(s/a\) large does not repair the issue. Next test directly which part of this approximation the calibrated Wilson samples already contradict.

## Stage 15. Testing the winding coordinates on the release boxes

**ON FILE (rows 1145/1146, 1161/1162, 1227/1230, 1656/1659).** At \(v=u,2u\) and \(\beta_K=O(\log n)\), in each twisted law the three based straight *spatial* windings have density \(1+o(1)\) relative to product Haar, uniformly in the winding tuple. They share no links. The private-link bound also allows a positive mixture of the twists. Row 1656 Stage 3 and row 1227 (17), (21) give the corresponding winding and array tests. Thus the calibrated law gives vanishing probability to a shrinking neighbourhood of commuting spatial triples: the Haar probability of exactly commuting is zero by conditioning on a noncentral first matrix and using its measure-zero circle centralizer. Stage 10 puts probability one on that commuting set in the magnetic-first limit. At fixed \(\gamma,n,v\), the tail domination in Stage 13 also implies concentration at central windings on the original unscaled group in the critical-scaling limit, even after the cyclic thermal weighting. Both of these whole-field approximations therefore fail a directly observable test when transplanted with their fixed-parameter concentration. This does not compare traces of two *different* probability laws or imply that two scalar purities must differ.

**ARGUED (decision).** The measured winding triples in the physical boxes fail the concentration test of the fixed-box law. The proof of (16) integrates their fluctuations with a bound \(C_{n,\gamma}|r|^{-2}\), with no growing-box control. I leave that proposed substitution here. There is a further test for the sign of the homogeneous divisor at \(v=u\): the functions \(D_v\) are Laplace transforms of bounded Wilson observables, attain both ends of their support on real configurations, and obey a bound on the whole real coupling line. This supplies a way to estimate the cost of poles alone in a larger disk, without passing to long times first.

## Stage 16. Counting actual poles at the prescribed time

**PROVED.** There are absolute \(A,c>0\) such that for every sufficiently late \(K\) and **every** integer \(v\ge u\), the exactly homogeneous neutral ratio \(P_v\) has total pole multiplicity at least \(c v/\log n\) in
\[
                 |t|\le A n^3\log n/\alpha,\qquad \alpha=\beta_K.          \tag{22}
\]
In particular at the prescribed period \(u\), some zeros of \(D_u\) fail to cancel with double multiplicity against \(D_{2u}\). This is a global nondivisibility result with a finite radius bound. The radius in (22) is substantially larger than the \(O(1/\alpha)\) radius of the signed-union count.

**Proof of the real and area bounds.** Use the unshifted plaquette exponentials, which leave \(P_v\) unchanged. With \(L=3n^3v\), the normalized entire function \(F_v(t)=D_v(t)/D_v(0)\) has \(\log|F_v(t)|\le L|\operatorname{Re}t|\) by the Laplace representation in Stage 7. It is even. Indeed multiply direction-3 links by \((-1)^{x_1}\), direction-4 links by \((-1)^{x_1+x_2}\), and leave the others alone. These periodic signs reverse exactly the 13, 14, 24 plaquette signs, commute with every twist, and leave the tree faces fixed. Hence \(0<P_v(x)\le1\) on the whole real axis for \(v\ge2\), by the real positive transfer at \(|x|\). For \(x\ge0\),
\[
             0\le Lx-\log F_v(x)
                       \le C n^3v\log(2+\alpha+x).                         \tag{23}
\]
For the lower bound on \(F_v(x)\) keep the periodic term of its numerator, with factor \(1/8\). Restrict all \(4 n^3v\) links to the group ball of radius \((1+\alpha+x)^{-1/2}\) about identity. Its one-link Haar volume is at least \(c(1+\alpha+x)^{-3/2}\) by the sine-squared radial density. Each plaquette then has deficit at most \(C/(1+\alpha+x)\) by the group triangle inequality. The numerator on this region has integrand at least \(\exp(3n^3v\alpha+Lx-Cn^3v)\). The normalizing integral is at most \(\exp(3n^3v\alpha)\). This proves (23).

On the right half-plane set \(H(z)=L\operatorname{Re}z-\log|F_v(z)|\). It is nonnegative and superharmonic, with value \(+\infty\) at zeros. For \(R\ge1\) and \(0\le x\le R\), use the half-plane to the right of \(x\), evaluated at \(2R\). The Poisson kernel on \(x+iy,\ |y|\le R\), is \((2R-x)/[\pi((2R-x)^2+y^2)]\ge c/R\). Thus
\[
              \int_{-R}^{R} H(x+iy)\,dy\le C R H(2R).
\]
For this inequality first minorize the boundary values by continuous bounded nonnegative functions supported on the segment. Their Poisson extensions tend to zero at infinity and lie below \(H\) by comparison on expanding half-disks, since \(H\ge0\). Take the monotone limit, truncating the logarithmic singularities. Evenness gives the corresponding bound in the left half-plane. Apart from a null zero set,
\(\log^+|P_v(z)|\le 2(L|\operatorname{Re}z|-\log|F_v(z)|)\), using \(P_v(0)\le1\) and the type bound on \(F_{2v}\). Integration in \(x\) and (23) now give
\[
    \int_{|\operatorname{Re}z|,\,|\operatorname{Im}z|\le R}
              \log^+|P_v(z)|\,d^2z
                   \le C R^2 n^3v\log(2+\alpha+2R).                       \tag{24}
\]
This bound controls the positive part even in the presence of poles. In particular it does not assume what it will be used to prove.

**Proof of (22).** Fix \(w=W/\alpha\) as in Stage 6 with \(\log(b_1 W^2)>2\). Put \(R=B n^3\log n/\alpha\) and choose \(S\in(R,2R)\) whose boundary contains no pole. In \(|z|<S\) form the product \(J_S\) of the disk Blaschke factors \(S(z-d)/(S^2-\bar d z)\) at all poles \(d\) of \(P_v\) with their multiplicities. The function \(G=J_S(P_v-1)\) is holomorphic, and \(|J_S|\le1\) in this disk. Since \(\log^+|P_v-1|\le\log2+\log^+|P_v|\), (24) and the disk area submean inequality applied to \(\log^+|G|\) give
\[
                 \sup_{|z|\le S/2}\log^+|G(z)|
                        \le C n^3v\log(2+\alpha+2S).
\]
On the real diameter \(|G|\le1\). At \(|z|\le w\ll S\) the harmonic measure of the semicircle of the upper or lower half-disk of radius \(S/2\) is at most \(C w/S\). For example, harmonic extension of the boundary data one on the semicircle and zero on the diameter has the sine series with coefficients \(4/(\pi k)\) for positive odd \(k\), multiplied by \((2|z|/S)^k\). The maximum principle therefore bounds \(\sup_{|z|\le w}\log^+|G|/v\) by \(C n^3(w/S)\log(2+\alpha+2S)\le1/4\) upon choosing a sufficiently large fixed \(B\).

At the inner radius \(r\) in (4), \(|G|\le C(C\delta)^v\). The same annular interpolation as in (8) yields
\[
              v^{-1}\log |G(t_*)|
                      \le -2\log(w/t_*)+1/4+o(1).
\]
All poles have modulus at least \(c/n^3\) by Stage 3. Each disk factor at \(t_*=n^{-5}\) consequently has modulus at least \(c'/(Sn^3)\). If \(m\) is the pole count in the disk, (6) gives
\[
  \frac{m}{v}\log(Sn^3/c')\ \ge\ \log(b_1 W^2)-1/4-o(1).
\]
The errors are uniform for \(v\ge u\), and \(\log(Sn^3/c')=O(\log n)\). This proves (22). \(\square\)

**Decision after Stage 16.** Exact divisibility fails on the homogeneous diagonal at \(v=u\), and bounded continuation already fails at distance \(O(1/\alpha)\). The argument does not force a denominator pole at that small distance because (23) pays for all \(n^3\) spatial sites in every time step. A lower bound on the distance to complex zeros of the short trace alone cannot remove the volume factor. I next test the finite-time matrix limit on the growing-period scale, where there is a separate question about the actual degrees of freedom it retains.

## Stage 17. The aspect at which the intermediate model crosses the threshold

**ON FILE (rows 1227/1230, 1642).** The Friedrichs Hamiltonian on rotation invariants
\(H=-\Delta/2+2U\) has discrete spectrum \(e_0<e_1\le\cdots\) and finite positive-time heat traces. Row 1227 (4)–(8) treats this Hamiltonian and the compact one-vertex Wilson transfer. Here the question is convergence of the discrete *Gaussian* transfer (20) obtained from the entire spatial cube in (16), including its trace, and the scaling of all its crossings.

**PROVED.** Write
\[
 q(\tau)=\frac{\operatorname{Tr}_{\rm inv} e^{-2\tau H}}
                   {(\operatorname{Tr}_{\rm inv}e^{-\tau H})^2}.
\]
It increases strictly from zero to one. If \(v\to\infty\) and \(v\gamma_v^{1/3}\to\tau\) in the closed extended nonnegative line, then \(p_v(\gamma_v)\to q(\tau)\), with the endpoint values just specified. Consequently every choice of crossings \(p_v(\gamma_v)=457/625\) obeys
\[
            v^3\gamma_v\longrightarrow \tau_*^3,\qquad
                      q(\tau_*)=457/625.                                   \tag{25}
\]
This specifies the constant by a convergent spectral trace. It requires no numerical spectral input.

**Proof of heat-trace convergence for positive finite \(\tau\).** Put \(h=\gamma^{1/3}\), \(t=vh\). Let \(g_t(x,y)=(2\pi t)^{-9/2}e^{-|x-y|^2/(2t)}\), the ordinary heat kernel. The trace of \(S_h^v\) on invariants is an integral over \(x\in\mathbb R^9\), a rotation \(R\) and the Gaussian bridge from \(x\) to \(Rx\) of duration \(t\), with outside factor \(g_t(x,Rx)\) and insertion
\[
               \exp\!\left(-2h\sum_{j=0}^{v-1}U(X_{jh})\right).
\]
This is the iterated Gaussian kernel with the simultaneous rotation projection placed at the final join, which commutes with every factor. Equivalently the projection may be inserted at any subset of joins. On a compact set of \(x\), for \(t\to\tau>0,\ h\to0\), use a unit-time bridge shifted by the linear segment from \(x\) to \(Rx\) and multiplied about that segment by \(\sqrt t\). Its continuous trajectories give convergence of the Riemann sums to \(2\int_0^\tau U(X_s)ds\) almost surely. The weights are bounded by one.

Here is control over \(x\) at infinity, where a one-insertion estimate would diverge along the commuting matrices. Put \(k=\lfloor v/2\rfloor\), and use cyclic indices. By the arithmetic-geometric mean inequality the discrete insertion is bounded above by
\[
        v^{-1}\sum_{j=0}^{v-1}
                   \exp[-tU(X_{jh})-tU(X_{(j+k)h})].
\]
Both separating time intervals lie between \(t/3\) and \(2t/3\) for \(v\ge2\). For a term in this bound integrate all joins except the two displayed points. The resulting integral has two rotation-averaged heat kernels at those intervals, with weights \(e^{-tU}\) on the two points. At \(t\) in a compact positive interval it is bounded by an integrable majorant in the two radius vectors \(r,r'\): a constant times \(\exp(-c|r-r'|^2)d^3r\,d^3r'/(|r|^2|r'|^2)\), by the angular bound in Stage 13. The contribution when either displayed matrix has norm \(>B/2\) tends uniformly to zero. If both have norm \(\le B/2\), condition on them and the two rotations at those joins. At any intermediate time the conditional Gaussian bridge has mean on the segment between two (possibly rotated) endpoints of norms \(\le B/2\), and covariance bounded by \(tI\). Its probability of norm \(>B\) is at most \(C_\tau e^{-c_\tau B^2}\). This also bounds the event at the original time zero: its radial indicator is rotation invariant, so the seam carrying the final rotation may be moved to either displayed join before conditioning. If it coincides with one of them this event is empty. This proves uniform tightness of the original one-point trace measure, since the majorant bounds the total two-point masses uniformly. In particular the compact-base convergence gives convergence of the complete trace.

The limiting bridge with insertion \(e^{-2\int U}\) represents \(e^{-\tau H}\). One way to justify this identification is to replace \(2U\) by \(\min(2U,J)\). For bounded potential, expansion of the exponential inside the bridge into ordered time integrals gives the norm-convergent Duhamel series for the bounded perturbation of the heat operator; each term is the corresponding product of heat kernels by Gaussian conditioning. As \(J\uparrow\infty\), the forms increase to the closed kinetic-plus-potential form (smooth compactly supported functions are a core by truncation and mollification). The resolvents converge strongly by the variational minimum for the strictly positive shifted forms: their minimizers are bounded in the first form norm, weak limits have all the finite-\(J\) bounds, and the limiting minimizer is unique, with strong \(L^2\) convergence by strict convexity. The spectral calculus then gives strong semigroup convergence by uniform polynomial approximation in the shifted resolvent. Monotone convergence of the bridge weights on finite endpoint integrals identifies its kernel. Composition at half the time and the Hilbert–Schmidt square identity identify the diagonal integral with the trace, also after rotational projection. Finiteness follows from the two-point bound above and Fatou. This proves convergence at \(t=\tau\) and \(t=2\tau\), hence of their quotient.

For any positive transfer, its purity increases with the positive time exponent wherever these traces converge. In the spectral representation with energies \(E=-\log\lambda\) (an overall scalar is irrelevant), the logarithmic derivative is \(2(\mathbb E_t E-\mathbb E_{2t}E)\); the thermal mean decreases since its derivative is minus the variance. For the finite-step operator it is enough to use time exponents \(>2\), then take the continuous limit from above at 2 by summability. For \(H\) the inequality is strict at every positive time by its distinct energies and trace summability at half that time. Infinitely many states and a simple lowest energy imply \(q(0+)=0,\ q(+\infty)=1\) by the same trace comparisons as in Stage 14.

Equation (21) gives the small-time endpoint of (25). For \(vh\to\infty,\ h\to0\), compare by monotonicity to \(\lfloor t/h\rfloor\) at any fixed positive \(t\), then send \(t\to\infty\). If \(\gamma\) instead tends to a positive finite value, compare to a fixed large period and use continuity in \(\gamma\); the limiting finite-step kernel has simple top eigenvalue since its positive kernel is strictly positive everywhere (taking absolute values in the top Rayleigh quotient enforces a common sign, excluding an orthogonal top eigenvector). At \(\gamma\to\infty\) use (19) at that fixed period and simplicity of the top eigenvalue of \(\mathcal K\), also implied by (14)'s one-step excitation bound. These exhaust the subsequential possibilities. Strict increase of \(q\) and compactness of the extended nonnegative line now force every sequence of crossings to satisfy (25). \(\square\)

**PROVED (a noncommuting pair of limits in the Wilson law).** At the geometry of the problem one obtains the exact nested limit
\[
 \lim_{\substack{n=\ell b^K\to\infty\\v=n/512}}\ \lim_{a\to\infty}
       P_{n,v}(a,\kappa a^2)=q(\kappa^{1/3}/512),\qquad \kappa>0,          \tag{26}
\]
by taking \(\gamma=\kappa/n^3\) in (16), then (25). Thus \((512\tau_*)^3\) separates the two strict seed inequalities in this ordered limit of actual four-dimensional Wilson tori. A simple measured observable proves a failure of exchanging the limits of the *thermal laws*. Let \(B=\frac13\sum_i|\operatorname{Im}h_i|^2\) for the three based spatial windings on one slice. Taking \(a\to\infty\) first gives limiting mean zero at every fixed \(n,v\) by the uniform scaled radial tails in Stage 13. Taking \(n\to\infty\) first with \(a,\ s=\kappa a^2\) fixed gives limiting mean \(3/4\). In fact the private-link proof of row 1145 applies with the staple norm bounded by \(6\max(a,s)\) on every twist. Its one-link multiplier bound yields a uniform \(1+o(1)\) density against three independent Haar windings whenever \(n/(1+6\max(a,s))\to\infty\), using \(n-O(1)\) private links on each of these three spatial lines. Under Haar each quaternion component has second moment \(1/4\). The same \(3/4\) conclusion holds on the calibrated electric sequence with \(s=\kappa a^2,\ a=\beta_K=O(\log n)\), and at the isotropic endpoint. This is a measured obstruction to a uniform replacement of the winding law even on the crossover scale (26); it gives no equality or inequality between the two orders of limits for the purity itself.

**Decision after Stage 17.** The full-box intermediate theory has a sharply specified thermal scale. Its winding distribution fails on the growing lattices before one even reaches the isotropic endpoint. To test an alternative that avoids extrapolating this distribution, I return to the two-period holomorphy question on a constrained slice of Wilson parameters.

## Stage 18. Both signs near the tree for identical slabs on nearby paths

**PROVED (scale and multiplicities).** For each sufficiently late cutoff there is a monotone real-analytic tree-to-Wilson interpolation with the **same** interpolation in every time slab, the same original tree and the same isotropic Wilson endpoint. Every individual real plaquette coupling differs from that on the specified linear path by at most \(C/\alpha\), uniformly on \([0,\alpha]\). On this interpolation, for every even \(v\ge u\) (including \(u,2u\)), the neutral two-period ratio has at least \(c v\) pole multiplicity **and** at least \(c v\) zero multiplicity after cancellation in
\[
                         c'/\alpha<|t|<C'/\alpha .                          \tag{27}
\]
Both counts are also \(O(v)\) in the indicated disk, after choosing its outer radius as in the proof. This test changes the rates at which different spatial bonds turn on. It does not change the length, coupling, or boundary rule of one slab relative to another.

**The paths.** Keep the tree plaquettes at \(\alpha\). From Stage 5 select just the direction-2 spatial bonds at the starts and ends of the rectangles on its chosen strip. These are \(O(\alpha)\) bonds in each time cut; give their electric plaquettes coupling \(t\). Fix constants \(W,B>0\), in that order, as below and put \(b'=B/\alpha,\ t_0=8b'\). Choose an even integer \(m\ge20\log(2n)\). Define \(d(t)=1-e^{-(t/t_0)^m}\). On the remaining weak electric bonds use \(f(t)=t\,d(t)/d(\alpha)\). On the weak magnetic faces use \(g(t)=t\,d(t)\operatorname{erf}(t/t_0)/(d(\alpha)\operatorname{erf}(\alpha/t_0))\), with \(\operatorname{erf}(x)=2\int_0^x e^{-y^2}dy/\sqrt\pi\). Both functions are entire, \(f\) odd and \(g\) even. On \([0,\alpha]\) the factors increasing from zero to one make the paths monotone with the stated endpoints. Their distance from \(t\) is \(O(t_0)\), since \(x e^{-x^m}\) and \(x(1-\operatorname{erf}x)\) are bounded uniformly for \(x\ge0,\ m\ge2\) (use the Gaussian tail for the latter). On the complex disk \(|t|\le4b'\),
\[
          |f(t)|+|g(t)|\le C\,2^{-m}|t|,\qquad
          \sum_{\rm weak\ per\ step}|\text{coupling}|\le C\alpha |t| .       \tag{28}
\]
The first follows by \(|t/t_0|\le1/2\) and the two denominators tending to one, the second by the marked bond count and \(n^3 2^{-m}\le1\). Constants in (28) are independent of \(B\) for all sufficiently late cutoffs at each fixed \(B\).

**Two estimates at the tree.** Denote the new ratio by \(P\) for the current period \(v\). The unperturbed strong magnetic probability and \(k_0,\delta\) are those of Stage 3. For a fixed pair of boundary configurations, the linear term of the electric exponential in its weak-bond amplitudes integrates to zero against the unperturbed gauge average, by the sign flip on a single strong circuit in Stage 4. Its remainder is bounded by a constant times \((\alpha|t|)^2e^{C\alpha|t|}\) using (28). The magnetic factors still multiply on either side of the rank-one kernel. Thus the proof of (3) gives a separated rank-one spectral projection throughout \(|t|\le c'/\alpha\), and
\[
       |P-1|\le C(C\delta)^v
                 \quad\text{for } |t|\le r'=\sqrt\delta/(C\alpha).
\]
The long and short traces each have no zeros in the larger \(c'/\alpha\) disk. At \(t_*=n^{-5}\) the real excitation lower bound (6) still holds with an absolute constant \(b_1>0\). Indeed every weak electric bond on each of the rectangles is marked. Its real Haar multiplier is the very same as before; unused bonds have trivial normalized multiplier one. The magnetic change in the probability of Stage 5 has likelihood ratio within \(e^{\pm 2n^3 g(t_*)}=1+o(1)\). The top operator norm after the same normalization is at most 2 by (28), and (7) and its two-vector Gram argument apply.

**Two bounded axes.** In the representation on the fixed magnetic probability of Stage 3, call the one-step operator \(B(t)\), retaining strong scalar normalization only. For imaginary \(t\), the weak electric couplings are purely imaginary. Multiplying every vertex gauge on the electric join by \((-1)^{x_1+x_2}\) negates the weak terms and leaves the strong terms fixed. The centre projection commutes with these signs. The adjoint of the projected electric operator is therefore itself, since complex conjugation of all these weak couplings has exactly this effect. The weak magnetic coupling \(g(t)\) is real on this axis, so the magnetic sandwich is self-adjoint as well. On the real axis self-adjointness holds directly. On both axes in \(|t|\le 2b'\), \(B(t)\ne0\): the constant electric multiplier is nonzero by the small-argument series in Stage 2 (and positive on the strong bonds), and the magnetic factors are invertible. Thus \(B(t)^v\) is positive at even \(v\) and \(0<P(t)\le1\) on both axes. For their inverses let \(A(t)=\langle 1,B(t)1\rangle\) in the fixed probability representation, taking the scalar product linear in the operator argument. It is holomorphic with \(A(0)=1+O(\delta)\), \(|A(t_*)|\ge1/2\). For any nonzero self-adjoint Hilbert–Schmidt \(B\) and even \(v\ge2\),
\[
  P^{-1}\le\left(\frac{\operatorname{Tr}|B|^v}{\|B\|^v}\right)^2
       \le\left(\frac{\|B\|_{\rm HS}}{\|B\|}\right)^4 .
\]
On \(|t|\le 4b'\), \(\|B(t)\|_{\rm HS}\le (1+\delta)e^{C\alpha|t|}\) by (28) and positivity of the unperturbed pointwise gauge integral. It follows that \(|A|^4|1/P-1|\le e^{C(1+B)}\) on the two axes of the smaller disk. The bound has no factor \(v\) in its logarithm.

**Counting poles of each sign.** Choose \(W\) with \(\log(b_1 W^2)>2\), write \(w=W/\alpha\), and choose \(S\in(b',2b')\) avoiding all divisor points on its boundary. Apply the following argument twice to \(H=P-1\) and \(H=A^4(1/P-1)\). For the second argument use disk factors at *all* zeros of \(P\) with multiplicity, even if \(A^4\) has removed some. For the first use all poles of \(P\). In each case the product \(J_S H\) is holomorphic on the disk. The entire normalized traces of both periods have \(\log|F_j(t)|\le C\alpha j|t|\) there by the real tree measure, the path integral and (28), \(j=v,2v\). Their values at zero are one. Jensen gives a circular average bound \(C\alpha j\rho\) for the negative log part on each circle of radius \(\rho\le 4b'\) from the bound on the positive part. Since \(P(0)=1+O((C\delta)^v)\), the disk-area average of \(\log^+|H|\) on \(|t|<S\) is at most \(C(1+\alpha v S)\) in both cases, using also \(|A|\le\|B\|_{\rm HS}\). The area submean gives this same bound with a fixed multiplicative constant on \(|t|\le S/2\) for \(\log^+|J_SH|\).

In each quadrant the boundary bounds on both axes are \(C(1+B)\) for this log. Squaring the coordinate maps the quarter disk to a half-disk. Its circular arc has harmonic measure at most \(C(w/S)^2\) on \(|t|\le w\), by the half-disk estimate of Stage 16. Consequently
\[
      v^{-1}\sup_{|t|\le w}\log^+|J_SH|
              \le C(1+B)/v+C\alpha w^2/S\le 1/4
\]
for a sufficiently large fixed \(B\) and all large \(n\). Here \(W\) is chosen first. At the inner radius \(r'\), both \(|H|\) are at most \(C(C\delta)^v\). At \(t_*\) both are bounded below by \(c(b_1\alpha^2t_*^2)^v\), using \(|A(t_*)|\ge1/2\). Each factor of \(J_S\) at \(t_*\) has modulus \(\ge c''/(\alpha S)\ge c''/(2B)\) because the two trace divisors avoid \(|t|\le c'/\alpha\). Annular interpolation as in (8), with \(r'\) in place of \(r\), gives for the respective count \(m_S\)
\[
       (m_S/v)\log(2B/c'')\ \ge\ \log(b_1W^2)-1/4-o(1).
\]
The interpolation error still tends to zero since \(-\log\delta\ge c n/(1+\alpha)\). This proves (27) with a common outer radius \(2B/\alpha\). Jensen at \(4B/\alpha\) bounds both individual trace zero counts inside that radius \(2B/\alpha\) by \(O(v)\), and hence both signed counts too. \(\square\)

**Decision after Stage 18.** At the seed aspect the near-tree zeros survive with both signs even with identical time slabs and real couplings differing from the linear path by only \(O(1/\beta_K)\). The proof needs the sparse set of early temporal bonds and the real magnetic weight on the imaginary axis. Neither property holds for the exact linear homogeneous path. It tests sensitivity to the interpolation, not the value of its real endpoint.

## Stage 19. A zero-free disk for the original affine path

**ON FILE (rows 863/879, 1145/1146, 1656/1659; gap-solve2-astra62.md §§8–11 and its check).** I first considered time blocking on the temporal star. The proposed (KS-ZONE) of row 863, including the strip of magnetic size \(c/(1+\alpha)\), is already proved in gap-solve2-astra62.md and checked in gap-solve2-check-opus.md. I stopped that line. The present affine path instead has strong orientations \(12,23,34\), with time at its leaf 4. In particular its \(12\) magnetic plaquettes stay at \(\alpha\). I use the earlier block-bridge expansion idea, now eliminating the \(1\)- and \(4\)-links along different coordinates and retaining the dependence through the \(3\)-links.

**PROVED.** For the originally specified *linear* path of Stage 1 put
\[
       L=\left\lceil A_0(1+\alpha)\log(2+\alpha)\right\rceil .
\]
There are absolute \(A_0,c,C>0\) such that for every sufficiently late cutoff and every \(v\ge u\), each \(D_v,D_{2v}\) is zero-free and
\[
       |P_v(t)-1|\ \le\ C n^3 v e^{-cv}
                         \qquad (|t|\le c/L^2).                             \tag{28a}
\]
In particular this puts the first possible uncancelled pole outside a disk whose radius depends on the running coupling through a power and a logarithm. Stage 3's direct rank-one argument gave \(c/n^3\).

**Two levels of independent bridges.** Work first with a specified temporal centre twist, represented by signed faces at the temporal seam. Remove scalar shifts and normalize each strong face by the trivial coefficient of \(e^{\alpha\operatorname{Re}g}\). Its positive normalized kernel is \(w_\alpha\). Fix axial gauge along direction 2 independently on each 2-line: every nonwrapping 2-link becomes 1 and its final link is the winding \(H\). The \(H\)'s have product Haar before weighting. Integrating the unused gauge variables costs one, by the Haar triangular prefix transformation described in Stage 5.

For fixed 2-links the \(12\) and \(23\) terms are the transition weights of 1-link and 3-link chains along direction 2, independently for each transverse line and each type. A single transition as a function of its new link is \(w_\alpha\) at the mismatch with a left and right translate of its old link. The two translates are the two adjacent 2-links and may include the face sign. Once the 3-links are fixed, the \(34\) terms are the same kind of transition weights of 4-link chains along direction 3, with the two adjacent 3-links furnishing the background. This uses every strong face exactly once. A segment of \(j\) consecutive such transitions, with any fixed background and two fixed end links, integrates to a rotated \(w_\alpha^{*j}\) at the two endpoints. This follows by iterating convolution since a central increment remains central in law under left-right transport of the old link. By the character multiplier bound of row 1145 (1),
\[
                 \sup |w_\alpha^{*j}-1|
                  \le \sum_{d\ge2}d^2e^{-(d-1)j/(1+\alpha)} .
\]
Divide each cyclic spatial coordinate 2 and 3 into intervals of lengths from \(L\) to \(2L\), possible for \(n\ge2L\). Call the right side at \(j=L\) \(\eta_L\). By increasing \(A_0\), \(L\eta_L\) is as small as any prescribed absolute constant at all sufficiently late cutoffs.

Keep independent Haar anchor links at the starts of the segments of each chain. Given its two anchors and its prescribed background, sample the interior of each segment by its *normalized* positive bridge law. This divides its raw weight by the rotated \(w_\alpha^{*j}\), denoted \(b_\sigma\) for that segment \(\sigma\). Sample first all 1- and 3-link bridges, then all 4-link bridges given the resulting 3-links. Different bridges at each level are conditionally independent. Every bridge can be sampled with a separate independent uniform random seed and just its two local anchors and background segment, for example by sequential conditional integration in fixed Haar coordinates and inverse distribution functions. Thus all underlying inputs are independent: the \(H\)'s, the anchors, and these seeds. The exact normalized Wilson integral is their expectation of the product of **all** \(b_\sigma\), times the omitted-face exponentials. This statement follows by undoing the two levels of normalized conditional integration in reverse order. It does not assert joint independence of the two levels.

Index cells by a single coordinate along axes 1 and 4 and one interval each along axes 2 and 3. Assign a segment factor to the cell where its segment begins, and each weak face to its base cell. Define
\[
       1+f_C=\prod_{\sigma\ {\rm assigned\ to}\ C} b_\sigma\,
               \exp\!\left(t\sum_{p\ {\rm assigned\ to}\ C}
                                    \sigma_p\operatorname{Re}U_p\right).
\]
There are at most \(6L\) segment factors (two types along 2, one along 3) and \(12L^2\) weak faces in one cell. Hence
\[
                \|f_C\|_\infty\le e^{6L\eta_L+12L^2|t|}-1 .
\]
Each \(f_C\) is a function of independent inputs in a bounded neighbourhood of \(C\) in *cell* coordinates, uniformly in \(L\). More explicitly, a weak face uses links at its base or one lattice step away. A 4-link adds its one 3-segment's anchors, seed and the 3-links on that segment and at the adjacent time. A 1- or 3-link adds its one 2-segment's anchors, seed and its 2-links, which equal 1 except at the wrapping seam. Assign each nontrivial \(H\) to that wrapping cell. No 4-link is used to generate a 3-link. The same dependencies suffice for each segment factor. Five cells in either direction of each coordinate suffice to include all these inputs. In particular overlap defines a graph on cells of absolute bounded degree \(D\), also when the time period changes. We may use the fixed graph joining all cells at coordinate distance at most ten for bookkeeping. For any required \(\epsilon_0>0\) first choose \(A_0\) and then \(c\) so that \(\|f_C\|_\infty\le\epsilon_0\) on the claimed disk.

**Connected coefficients and the two time periods.** For any subset \(A\) of cells write \(Z_A(\lambda)=\mathbb E\prod_{C\in A}(1+\lambda f_C)\) in the independent-input representation. In expanding the product, the expectation factors over the graph components of each selected subset. A nonempty connected subset \(X\) has weight \(\lambda^{|X|}\mathbb E\prod_{C\in X}f_C\). Distinct components have no adjacent cells. For \(i\in A\), separate configurations according to the component containing \(i\), or its absence. This gives the exact deletion formula
\[
 Z_A=Z_{A-i}+\sum_{\substack{i\in X\subset A\\X\ {\rm connected}}}
       \lambda^{|X|}\mathbb E\!\prod_{C\in X}f_C\;\,Z_{A\setminus N[X]},
\]
where \(N[X]\) includes \(X\) and all its neighbours. On \(|\lambda|\le2\), induction in \(|A|\) gives \(|Z_A/Z_{A-i}-1|\le1/2\) for every \(i\). Indeed in each term after division, the smaller-domain quotient costs at most \(2^{(D+1)|X|}\) by deleting one cell at a time. There are at most \((D+1)^{2j}\) connected \(j\)-sets containing \(i\), by recording a depth-first traversal of a spanning tree with fixed neighbour order. The sum is at most \(\sum_{j\ge1}[(D+1)^2 2^{D+1}2\epsilon_0]^j\le1/2\) for a small absolute \(\epsilon_0\). This proves nonvanishing. Deleting cells successively also gives the branch of \(\log Z_A\) zero at \(\lambda=0\) and bounded in modulus by \(C|A|\) on this disk, from the convergent logarithm of each quotient.

Give each cell its own formal variable before identifying them all with \(\lambda\). A monomial in \(\log Z\) has connected support: if its support splits into separated subsets, setting all other variables to zero factors \(Z\) into independent expectations. A term of total degree \(j\) consequently uses a connected set of at most \(j\) cells. When \(j<c_1 v\) for a sufficiently small absolute \(c_1\), its whole dependence neighbourhood lifts to an ordinary time interval of length \(<v/2\). To verify this, lift one time coordinate and then use steps of length \(\le10\) on a spanning tree of at most \(j\) cells. The support and its five-cell buffers lie within a time interval of length \(\le20j+11\); for \(j<c_1v\) this is \(<v/2\), and alternative paths cannot differ by \(v\). The moment of each subproduct used in that coefficient is the same in this interval for all temporal centre twists. One may move the twist seam outside the interval by multiplying each spatial link on intervening time slices by the corresponding spatial wrapping-link signs. These preserve the axial gauge (a 2-sign acts only on \(H\)) and each Haar anchor law. Each normalized bridge transforms covariantly by the same link substitutions, since its numerator and its integrated endpoint factor transform together. Thus the equality holds also for the reference sampling law of any local list of \(f_C\)'s. The argument may be made before introducing random seeds by integrating the normalized bridges on the list's dependence neighbourhood; unused normalized conditional kernels integrate to one. It also proves equality with the moments of each lift to the period \(2v\). The two lifts of each connected monomial preserve its powers; every short connected monomial at \(2v\) arises this way. Consequently the coefficients through degree \(<c_1v\) are independent of the twist and double exactly when the time period doubles.

Cauchy's inequality in \(\lambda\) bounds all remaining coefficients by \(C|\{\mathrm{cells}\}|2^{-j}\). Summing them at \(\lambda=1\) costs \(C n^3 v e^{-cv}\). Restore the unshifted strong normalization, a fixed positive scalar per time step. It follows uniformly on the complex \(t\)-disk that every twist mass is its periodic counterpart times \(1+O(n^3v e^{-cv})\), and that the periodic long mass divided by the square of the short one is \(1+O(n^3v e^{-cv})\). The individual masses have already been shown nonzero by deletion. The neutral mixtures therefore have no zero there at late \(K\), and their ratio satisfies (28a). This proves the claimed bounds. \(\square\)

**PROVED (sharper count on the original path).** There are absolute \(C,c>0\) such that for all sufficiently late \(K\) and \(v\ge u\),
\[
 \#\{\,d:\ |d|\le C/\alpha,\ \operatorname{ord}_dP_v\ne0\,\}
                        \ \ge\ c\,v/\log(2+\alpha).                        \tag{29}
\]
These points are distinct. Indeed in Stage 7 the factor at any such point on \(0\le x\le t_*\) now has \(|(x-d)/(3w)|\ge c/(w L^2)\) by (28a), since \(t_*=n^{-5}\ll L^{-2}\). The rest of (9) and its real lower witness are unchanged. Replace \(\log(3wn^3/c')\) by \(\log(Cw L^2)=O(\log(2+\alpha))\) in its last inequality. At the calibrated rate the denominator in (29) is of order \(\log\log n\). This still counts the union of both signs in the short disk.

**Decision after Stage 19.** The exact affine ratio is close to one throughout a growing-box disk of order \(1/[(1+\beta_K)\log(2+\beta_K)]^2\). Its bounded expansion fails by order \(1/\beta_K\). The block estimate pays for an entire \(L\)-by-\(L\) group of weak faces. The missing sign and the real calibrated endpoint lie beyond this argument; weak \(U(1)\) and a five-dimensional model with an extra inactive spatial direction admit the same local type of estimate.

## Stage 20. A numerical seed inequality that distinguishes the comparison laws in the ordered limit

**PROVED.** Use the unmodified Wilson neutral traces, the same spatial aspect \(v=n/512\), the same electric coupling \(a\) and the same magnetic coupling \(s=\kappa a^2\). For each fixed \(\kappa>0\) take \(a\to\infty\) first at fixed \(n,v\), then \(n=\ell b^K\to\infty\). The three purities in this ordered limit are
\[
 \begin{array}{c|c}
    \text{Wilson system} & \displaystyle\lim_{K\to\infty}\lim_{a\to\infty}
                                    P_{n,n/512}(a,\kappa a^2)\\ \hline
    4{\rm D}\ SU(2) & q(\kappa^{1/3}/512)\\
    5{\rm D}\ SU(2) & 0\\
    4{\rm D}\ U(1),\ \text{order-two flips} & 0 .
 \end{array}                                                               \tag{30}
\]
For \(U(1)\) with its whole continuous centre in the projector the entry is 1. For \(\kappa>(512\tau_*)^3\), the four-dimensional nonabelian entry lies strictly between \(457/625\) and 1. With the same discrete projection the numerical lower bound itself fails in both comparison systems. With the whole abelian centre its strict intermediate value still fails. This improves on magnetic-first (14), whose numerical lower bound also passes in 5D. Neither the group nor the dimension nor the geometry changes when the 4D \(SU(2)\) entry crosses the threshold as \(\kappa\) changes.

**Proof for the five-dimensional Wilson law.** The spatial slice now has \(d=4\) directions and \(N=n^d\) vertices. At first \(n,v\) are fixed. In comb gauge there are \(d\) winding matrices and \(M=(d-1)(N-1)\) triangular pivot plaquettes. This is the dimension-general construction of row 1143 and check 1384; it integrates the actual spatial Haar links. Use exactly the segment of the proof of (16) that treats bounded scaled windings and pivots, now with
\[
  h_i=\exp[X_i/\sqrt{a n^{d-2}}],\qquad
  p_e=\exp[\xi_e/\sqrt s],\qquad
  \gamma_d=s/(a^2 n^d),\qquad U_d=\sum_{i<j}|X_i\times X_j|^2 .
\]
Indeed the squared norm of a constant electric mismatch is \(n^d/(n^2 n^{d-2})=1\) in these coordinates. The magnetic source on an \(ij\) double seam has size \(2\sqrt{s}/(a n^{d-2})\) times \(X_i\times X_j\). It is closed, and its spatial average again divides by \(n^2\). Orthogonal projection off exact two-forms therefore leaves the magnetic exponent \(2sU_d/(a^2 n^d)=2\gamma_d U_d\). At every nonzero momentum the same wedge/contraction identity from (18) gives exactness in any dimension. The rooted electric determinant and pivot determinant remain independent of \(X\). The change of variables is on all links, with no assumption that generic colour vectors commute in the critical limit.

For the tails put \(r_i=\sqrt{a n^{d-2}}\varphi_i\). The magnetic marginal after removing \(s^{-3M/2}(a n^{d-2})^{-3d/2}\) is bounded by
\[
 C_{n,\kappa}\prod_i r_i^2\prod_{i\ne k}(1+c_{n,\kappa}r_k^2r_i^2)^{-1}
      \,d^d r\ \le\ C'_{n,\kappa}(1+|r|)^{-2(d-2)}d^d r .
\]
Use only the commutators with the longest vector \(k\) in the spatial Wilson upper bound. For \(r_k\ge1\) the factor for each other index is at most \(C/r_k^2\), and for \(r_k\le1\) the product is bounded. The electric bound from tree integration and the \(d\) based winding mismatches costs \(a^{-3(N-1)/2}\) times a Gaussian in \(r-r'\). Here \(w(r)=(1+|r|)^{-2(d-2)}\) is in \(L^2(\mathbb R^4)\), so \(\int w(r)w(r-z)dr\le\|w\|_2^2\) and the squared Gaussian integral against the radial product is finite. This gives tight cyclic tails for \(v\ge2\) exactly as in Stage 13, and the selected plaquette action still gives Gaussian tails in the \(\xi\)'s at bounded \(r\). Consequently the fixed-box purity is that of (17) on \(d\) three-colour vectors, with rotation projection, \(U_d\), and parameter \(\gamma_d=\kappa/n^d\), in the limit \(a\to\infty\). In this statement the fourth winding is measured by the full Wilson law and participates in the commutator action.

After the same dilation the Gaussian transfer is \(e^{-hU_d}e^{h\Delta/2}e^{-hU_d}\) with \(h=(\kappa/n^d)^{1/3}\). The compactly supported invariant trial spaces in (21) apply in \(\mathbb R^{3d}\): the number of eigenvalues \(\ge1-C_m h\) is at least \(m\) for each fixed \(m\). At \(d=4\), \(v h=\kappa^{1/3}n^{-1/3}/512\to0\). Arbitrarily many neutral eigenvalues retain their full relative weight at the prescribed period, so the purity tends to zero. At \(d=3\) that time instead tends to a strictly positive number; Stage 17 gives the first entry of (30). The different thermal occupations here follow from integrating the nonconstant modes and testing the powered transfer.

**Proof for the compact abelian Wilson law.** At \(d=3\), fixed \(n,v\), the abelian seam factors commute. The comb reconstruction is a product of a seam winding and a function of the pivots, by triangular reconstruction or linearity of group words on the torus. Hence all magnetic plaquettes depend only on pivots, the \(d\) windings are independent Haar, and the pivot integral is \(\asymp_n s^{-M/2}\) for \(s\ge1\), \(M=(d-1)(N-1)\) real pivots. The upper bound uses the selected plaquette deficits and the lower bound restricts all pivot angles to \(s^{-1/2}\); all other magnetic angles are then \(O_n(s^{-1/2})\). The thermal weight still couples winding angles on neighbouring slices.

On the torus of winding angles modulo the order-two flips, the distance for each coordinate is the circle distance modulo \(\pi\). Splitting the electric action and integrating vertex gauges on a spatial spanning tree as in (13) bounds the kernel by \(C_n a^{-(N-1)/2}\exp[-c_n a\,\mathrm{dist}(\theta,\theta')^2]\) on arbitrary slice fields. There is no conjugation ambiguity for abelian windings. In a cycle of \(v\) slices, retaining a tree of \(v-1\) Gaussian angle differences and integrating gives the fixed-\(n,v\) upper estimate
\[
  Z_+(v)\ \le C_{n,v,\kappa}\big[s^{-M/2} a^{-(N-1)/2}\big]^v
                                                a^{-d(v-1)/2}.
\]
Use shifted action conventions. A matching lower bound follows by keeping every slice's pivots within \(c/\sqrt s\), the other \(v-1\) winding vectors within \(c/\sqrt a\) of the first arbitrary vector on the circle torus, and the nonroot vertex phases at each join within \(c/\sqrt a\) of its arbitrary root phase. Representatives can be lifted locally to the first winding angles; equivalently keep the suitable term of the finite centre average. Every spatial mismatch then costs \(O_n(s^{-1/2})\) in plaquette angle and every electric mismatch \(O_n(a^{-1/2}+s^{-1/2})\); at \(s=\kappa a^2\) the shifted weights are bounded below by a positive fixed-\(n,v,\kappa\) constant. The restricted Haar volumes give exactly the stated powers. Taking the ratio at \(2v,v\) yields \(P_{n,v}\asymp_{n,v,\kappa}a^{-d/2}\to0\) even before increasing \(n\).

If the entire winding torus is averaged at every join, the projected kernel depends only on the pivots. At bounded rescaled pivots \(\sqrt s\,\log p_e\), electric mismatch from them is \(O_n(s^{-1/2})=o(a^{-1/2})\). In the integral over a relative winding shift and the vertex phases, rescale the winding mismatch and rooted vertex deviations by \(\sqrt a\). The squared linearized mismatch is a rooted gradient plus a closed seam one-form. Its constant harmonic part has nondegenerate norm in the \(d\) winding coordinates, and the gradient form is nondegenerate on rooted phases. The Gaussian integral therefore gives a strictly positive constant independent of the pivot values, after extraction of \(a^{-(N-1+d)/2}\). Domination follows by the spatial tree estimate for the rooted phases, the winding mismatch Gaussian for the relative angles, and the magnetic pivot Gaussian for the remaining outer integration, as in Stages 11 and 13. Equivalently combine the two coercive lower bounds by taking half their sum on bounded scaled pivot sets; off those sets the integrated kernel has the same uniform power upper bound by the tree/angle split. Thus the normalized cyclic integral factors into one common positive scalar per slice up to \(1+o(1)\) at fixed period. The purity tends to 1. \(\square\)

**Decision after Stage 20.** Formula (30) is a selective thermal statement for the actual Wilson measures in a specified order of limits. Relative to the calibrated isotropic problem it has a concrete failure point: the same windings to which these proofs assign angles of order \(a^{-1/2}\) at fixed \(n\) become Haar along \(a=\beta_K,\ s=\kappa a^2\), by Stage 17. In particular varying \(\kappa\) in (30) supplies a law-dependent sign in this anisotropic experiment, but does not carry that sign to \(s=a=\beta_K\).

## Stage 21. What propagates in the selective limit

**PROVED (a local test of a proposed continuum use of (30)).** On a spatial slice consider any fixed list of plaquettes, any bounded continuous or polynomial function of their scaled deficits \(s(1-\operatorname{Re}U_p)\), and its spatial translates \(\Phi_x\). Use coefficients with \(\sum_x c_x=0\). At fixed \(n,v\), \(s=\kappa a^2\), in the true neutral Wilson thermal circle,
\[
       \lim_{a\to\infty}\mathbb E\!
           \left[\left(\sum_x c_x\Phi_x(j)\right)\Psi\right]=0             \tag{31}
\]
whenever \(\Psi\) is a bounded continuous or polynomial function of such readings on slices different from \(j\). This assertion permits a nonzero limiting equal-time variance. In contrast a specific difference of two elementary spatial plaquette deficits has strictly positive one-time-step covariance in the **calibrated isotropic** limit. The comparison uses couplings in their respective natural plaquette normalizations.

**Proof in the ordered anisotropic limit.** Keep the rescaled curls in (18) as insertions instead of just evaluating their integral. Conditional on the matrices \(X\) in the limiting thermal cycle, the curvature on each slice is
\[
        G_{ij}(x)+\frac{2\sqrt{s}}{a n^3}\,(X_i\times X_j).
\]
Here \(G\) is a standard three-colour real Gaussian on the image of the *spatial* curl, with its Euclidean two-form inner product, and there are independent copies on the different slices. Indeed \(dL\) maps the pivot coordinates invertibly onto that image with constant Jacobian. Completing the Gaussian square shifts out precisely the exact projection of the double-seam source. The remaining constant is its harmonic mean. The electric kernel in (17) depends only on the \(X\)'s, so the integrations over these exact Gaussian parts are independent even conditionally on the entire matrix cycle. The action of a single face multiplied by \(s\) converges to half the squared norm of that face coordinate. These are gauge-invariant scalar insertions in the original integral. Stage 13's tightness proves convergence for bounded continuous tests. For convergence with polynomial insertions, at fixed \(n,v,\kappa\) the joint moment generating function of \(\sum_{j,p}s(1-\operatorname{Re}U_p(j))\) at any fixed \(0<\epsilon<1\) is bounded as \(a\to\infty\). It is the ratio of shifted thermal masses with \(s\) replaced by \((1-\epsilon)s\) and with \(s\) unchanged. Stage 13's unnormalized integral asymptotics give the same powers of \(a\) with strictly positive finite coefficients at both positive \(\kappa\)'s. This proves uniform integrability of every polynomial in the local deficits. Conditional on the matrix cycle the slice Gaussian has translation-invariant law because the spatial curl image is translation invariant. The conditional mean of \(\Phi_x(j)\) is independent of \(x\). Independence from the other slice noises gives (31). For example a difference of neighbouring \(12\)-deficits has positive conditional variance: a spatial exact two-form supported on the curl of one link can be nonzero at the first face and zero at the second, and the Gaussian has full support on its image. The resulting difference of squared norms is a nonconstant polynomial there.

**ON FILE (rows 1151, 1231, 1371/1372, 1375/1376, 1660).** The finite-graph Wilson comparison gives the local limit on the isotropic neutral circles, with \(n^3\times u\) or \(n^3\times 2u\), for all plaquette holonomies of a fixed contractible graph between movable time cuts. The shape correction and exponential moment bounds for \(\beta_K(1-\operatorname{Re}U_p)\) are given in row 1660 Stage 1. The covariance is now the projection onto the *four-dimensional* curl image on the infinite lattice. Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, give the free exact-form projection and its Fourier symbol in outline 1673–1686 and 1733–1762. Row 1231 (3)–(4) gives the curvature-square covariance and evaluates the time Fourier integral. [Outline, exact projection](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L1733-L1762)

**PROVED (strict discrepancy at two adjacent times).** Put \(D(j)=\beta_K[(1-\operatorname{Re}U_{12}(0,j))-(1-\operatorname{Re}U_{12}(\hat1,j))]\) in the isotropic system. The four faces at \(j=0,1\) and fixed connecting edges fit in the graph just described. Trace readings are independent of the choice of local colour frame. Convergence in law and the one-plaquette exponential moments give convergence of their products by Cauchy–Schwarz and truncation. Write \(B(x)\) for the one-colour covariance of the \(12\)-curvatures separated by one time step and spatial vector \(x\). Then
\[
       \lim_{K\to\infty}\mathbb E[D(0)D(1)]
                  =3\big(B(0)^2-B(\hat1)^2\big)>0 .                       \tag{32}
\]
In fact the covariance of two half squared three-colour norms is \(3B(x)^2/2\) by Gaussian pairing. The four differences give the coefficient in (32). To see strictness, \(B(x)\) is the Fourier coefficient at \(x\) of the even nonnegative function
\[
       \frac{(\widehat k_1^2+\widehat k_2^2)e^{-\omega(k)}}{2\sinh\omega(k)},
       \qquad \widehat k_i=2\sin(k_i/2),\quad
                 2\cosh\omega(k)=2+\textstyle\sum_i\widehat k_i^2 .
\]
The formula follows by solving the scalar time difference equation for the inverse of the denominator of the curl projection, as in row 1231 (4). The function is integrable and positive on an open set on which \(e^{ik_1}\) has nonconstant phase. The strict triangle inequality after integration gives \(|B(\hat1)|<B(0)\). In (31) at the same two sites, with \(s\) as the plaquette scale, the expectation of the difference times its translate in time is zero after the first limit, for every \(n,v\ge2\). Thus an approximation by the solved anisotropic theory preserving even this local covariance cannot be asymptotically exact for the calibrated laws. Equation (32) probes one lattice time, not a positive physical time in the continuum. It uses an established short-distance Gaussian input, not evidence for either physical phase.

**Decision after Stage 21.** The proof of the strict numerical inequality in (30) retains the propagation of spatially constant winding modes. It loses spatially varying curvature correlations already at one lattice time by (31)–(32). It gives neither a new continuum consumer nor a counterexample to the real calibrated seed.

## Stage 22. Local curvature where the electric coupling actually grows logarithmically

**ON FILE (rows 1143/1144, 1151, 1231 and their checks).** The open-box pressure comparison credited there to Sourav Chatterjee, the Gaussian concentration comparison for plaquette radii in row 1151 (24), and the exact-space projection comparison in row 1231 (1) are prior. Row 1151 §8 uses an anisotropic source with comparable positive plaquette coefficients. In the following application \(s/a\) tends to infinity. In an arbitrary fixed gauge the quadratic error from the weakly controlled temporal links could be multiplied by \(s/a\). I use a spatial comb in each time slice to remove that loss.

**PROVED.** On the actual \(n^3\times v\) neutral Wilson circles, \(v=u,2u\), let \(a=\beta_K\) on electric faces and \(a\le s\le a^p\) on spatial faces for a fixed \(p\), with \(s/a\to\infty\). The joint law of the radii
\[
                    R_\pi=\sqrt{s}\,|1-U_\pi|
\]
on any fixed finite list of spatial plaquettes at fixed spacetime displacements converges to that of the norms of a three-colour standard spatial exact-form Gaussian on \(\mathbb Z^3\), with independent copies at distinct lattice times. In particular every \(\kappa>0\) has the same local limit at \(s=\kappa a^2\). This is a finite-dimensional distribution statement for the true growing tori. It uses the probability measures normalized separately at each period.

**Weighted open boxes.** Write \(W=\sum_\pi c_\pi(1-\operatorname{Re}U_\pi)\) with \(c_\pi=s\) on spatial and \(a\) on electric plaquettes; use the signed face on a twist seam. Let \(b_0=\lceil[\log(2+a)]^3\rceil\), and tile by disjoint vertex boxes with sides between \(b_0\) and \(2b_0\), placing the temporal seam between boxes. Below write \(b'=b_0\). In each box choose the ordinary comb tree with the three spatial axes ordered first, then time: it consists of a spatial comb on every slice plus the temporal edges at one spatial root. Each spatial nontree link can be shelled down to tree links using at most \(C b'\) spatial plaquettes only. For an \(i\)-edge use the plaquette in the first earlier nonzero coordinate and reduce that coordinate, as in row 1143 (14). For temporal nontree links the same shelling uses the whole box. Triangle and Cauchy–Schwarz bound the square of each distance from identity by \(Cb'\) times the sum of the corresponding plaquette deficits. Their linear versions apply to the comb link logarithms \(X\) and the linear curl \(dX\). Counting at most \(C b'^4\) links and using \(s\ge a\) gives
\[
 s\sum_{\rm spatial}|X_e|^2+a\sum_{\rm temporal}|X_e|^2
          \le C b'^5\sum_\pi c_\pi |(dX)_\pi|^2 .
\]
The same bound holds for chordal link distances and nonlinear deficits, up to constants, by the group shelling just given. Additional links fixed at identity do not affect these inequalities.

On the chart \(\max |X_e|\le\eta=b'^{-7/2}\), expansion of four exponentials gives \(|U_\pi-1-(dX)_\pi|\le C\eta\sum_{e\in\partial\pi}|X_e|\). For a spatial face all four links are spatial. For a temporal one its weight is only \(a\). Consequently the sum of squared errors with weights \(c_\pi\) is at most \(C\eta^2 b'^5\sum_\pi c_\pi |(dX)_\pi|^2\), and the nonlinear action is within relative \(C/b'\) of the quadratic action. The Haar density changes from its value at identity by factors between \(e^{-C\eta^2}\) and 1 per link. Outside the chart the open action is at least \(c a/b'^8\) by the single-edge shelling. Its integral there is negligible compared with the comb Gaussian normalization \(G\), which is at least \(e^{-C b'^4\log(2+s)}\) by the upper form bound \(CsI\). The Gaussian cost of leaving the chart is \(o(1)\) as well: the smallest precision is at least \(c a b'^{-5}\), and the expected sum of squared log coordinates divided by \(\eta^2\) is at most \(C b'^{16}/a\). Thus the open Wilson log normalizer differs from \(\log G\) by \(O(b'^3)\), uniformly also with any subset of links fixed at identity or with all coefficients multiplied by \(1+O(1/b')\).

Let \(V=n^3v\). For the positive neutral mixture the product of open normalizers divided by the full normalizer is at most \(\exp(C V\log(2+s)/b')\). To see the needed lower bound on the latter keep \(1/8\) of the periodic term; after fixing the internal trees, restrict crossing links and all free links tangent to the boxes' outer faces to distance \(s^{-2}\) from one. There are \(O(V/b')\) restrictions, costing \(O((V/b')\log(2+s))\) in the logarithm. Replacing the restricted links by one makes every crossing plaquette trivial. Squaring the triangle inequality with parameter \(1/b'\) bounds the action by \(1+1/b'\) times that on the remaining links plus \(C b's^{-3}\) per affected face. The Gaussian normalization with restricted links set to zero differs in log from the unrestricted one by \(O(\log(2+s)+\log b')\) per removed coordinate: the Schur complement eigenvalues lie between \(c a b'^{-5}\) and \(Cs\), by minimizing the full quadratic form over the other entries. The open estimates finish the bound. Dropping crossing faces gives the reverse normalizer inequality since their shifted weights are at most one. The unrestricted crossing-link Haar and the tree gauge changes have unit mass.

**Local comparison.** Under the neutral mixture the total expected signed action is \(O(V\log(2+s))\). In fact \(\mathbb E e^{W/2}=Z(c_\pi/2)/Z(c_\pi)\le e^{CV\log(2+s)}\), bounding the numerator by 1 and the denominator below by a periodic ball about identity for all links of radius \(s^{-1/2}\). Jensen proves the mean bound. Translation of a twist stack preserves the signed observable by a link-sign change, so each orientation of signed face has expected weighted deficit at most \(C\log(2+s)\). A given open box therefore leaves the above chart with probability \(\le C b'^{12}\log(2+s)/a=o(1)\), using its energy lower bound and Markov. In particular one need not assume a volume-independent pointwise Gaussian law.

Compare first to independent open Wilson boxes. The true density in the tree gauges is at most the normalizer ratio just bounded times their product density (include independent Haar on crossing edges); each twist term obeys this pointwise since its signed crossing factors are at most one. On a good chart keep the coordinates, and on a bad chart replace them by a fresh Gaussian from the precision diluted by \(1-C_0/b'\) for a sufficiently large fixed \(C_0\). For a single independent open Wilson box the resulting density is bounded by \(1+\exp(C b'^3)\) relative to that diluted Gaussian, by the pointwise chart and normalizer estimates. Applying these same replacement kernels to the true law gives relative entropy at most \(C V\log(2+s)/b'\) against the product Gaussian. The replacement is used only to compare expectations.

For a bounded Lipschitz test of a fixed list of \(m\) radii, average it over all common translations. At most \(O_m(1/b')\) of the translates meet a crossing face. Bad charts have vanishing average probability by the preceding bound. On the good charts the mean squared error per local radius from replacing \(\sqrt{s}|1-U_\pi|\) by \(\sqrt{s}|(dX)_\pi|\) is \(O(b'^{-2}\log(2+s))\) after translation averaging: sum the weighted Taylor error over boxes and use the expected action bound. In the diluted product Gaussian the vector of weighted curls \(\sqrt{c_\pi}(dX)_\pi\) is the image of independent standard normals by a map of norm bounded by two, since its undiluted covariance is an orthogonal projection. The translation average of the test has Lipschitz constant \(C_m/\sqrt V\) on those normals, by Cauchy–Schwarz over translates. The Gaussian concentration and entropy inequality proved in row 1151 following (24) bounds the error of means by \(C_m\sqrt{\log(2+s)/b'}=o(1)\). Specifically a Lipschitz function of constant \(K\) has centred log moment bound \(C t^2 K^2\); Jensen with the density adds \(D/t\) to the mean bound and optimization gives \(C K\sqrt D\). This establishes the local test comparison. Translation invariance of the original gauge-invariant spatial radii identifies their means with these translation averages.

Remove the \(1+O(1/b')\) Gaussian covariance dilution. Put arbitrary independent standard Gaussian coordinates on the crossing faces, affecting only \(O_m(1/b')\) of translated tests. Projection onto the direct sum of the weighted open-box exact spaces and all crossing coordinates then contains the global weighted exact space \(\operatorname{im}(\sqrt c\,d)\). Its excess dimension is \(O(V/b')\) by the boundary rank count in row 1231 (1): weighting by an invertible diagonal matrix preserves both dimensions and the inclusion. Coupling both projections on the same white noise bounds the mean squared coordinate discrepancy by \(O(1/b')\) after translation averaging, since the trace of their difference equals this rank. The remaining Gaussian comparison is thus the one global weighted curl on the actual torus.

**Fourier limit.** At a frequency \((k_0,k)\) put \(z_j=e^{ik_j}-1\) and \(z=(z_1,z_2,z_3)\). For \(z\ne0\) the magnetic block of this projection is
\[
             \frac{s|z|^2}{s|z|^2+a|z_0|^2}\,\Pi^{(3)}_{\rm ex}(k),        \tag{33}
\]
where \(\Pi^{(3)}_{\rm ex}\) projects onto the spatial curl image. Indeed a transverse link vector \(A\perp z\) maps to \((\sqrt{s}\,z\wedge A,\sqrt a\, z_0 A)\), of squared norm \((s|z|^2+a|z_0|^2)|A|^2\); longitudinal spatial and temporal components give only the orthogonal longitudinal electric image. At \(z=0\) the magnetic block is zero. The matrix norm is at most one. For \(|z|\ge\epsilon\) the scalar prefactor tends uniformly to one, while the spatial grid fraction with \(|z|<\epsilon\) is \(O(\epsilon^3)+o(1)\). Taking Fourier coefficients at the finitely many displacements gives exactly the spatial projection kernel, with a Kronecker delta in the time difference. Different colours are independent. Finite-dimensional Gaussian convergence, the radii comparison and bounded Lipschitz determination of weak convergence complete the proof. \(\square\)

**Decision after Stage 22.** With \(a=\beta_K\) and \(s=\kappa a^2\), the real growing-box law loses the local propagation measured in (32) even though its based windings remain Haar. Both statements can hold together. I next test whether *all* these local magnetic laws, even if matched throughout an approximation, can decide the seed inequality on genuine Wilson tori.

## Stage 23. Matched local Wilson laws on opposite sides of the seed inequality

**PROVED.** Fix \(0<\kappa_-<(512\tau_*)^3<\kappa_+\) and any prescribed lower bounds \(A_j\to\infty\). On any increasing sequence of release geometries \(n_j=\ell b^{K_j},\ v_j=n_j/512\), one can choose the same electric \(a_j\ge A_j\) for two Wilson \(SU(2)\) systems, with uniform spatial couplings \(s_j^\pm=\kappa_\pm a_j^2\), such that their neutral purities converge to \(q(\kappa_\pm^{1/3}/512)\) on opposite sides of \(457/625\). Yet their **complete families of limiting joint laws of local plaquette radii are identical**, including all six orientations at arbitrarily many fixed spacetime offsets, at either of the two time periods. The radii are \(\sqrt{c_\pi}|1-\sigma_\pi U_\pi|\), in each plaquette's own Wilson normalization. The common limits also agree with those of Stage 22 at calibrated electric coupling and any fixed positive \(\kappa\) on the same parabolic family. No measurement or selection mask modifies any thermal mass in this example.

**Proof.** In the proof of (16), keep both the spatial curvatures and the electric mismatches used in the positive path integral. On each slice the spatial curvatures after rescaling are the Gaussian plus harmonic constant in Stage 21. Conditional on the matrix path and the root rotations at its joins, the electric mismatches in colour frames after scaling by \(\sqrt a\) are
\[
       d\phi_j+\big(n^{-3/2}(R_j X_{j+1,i}-X_{j,i})\big)_{i=1}^3 .
\]
Here \(d\phi_j\) is a standard colour Gaussian on the image of the spatial vertex gradient. Indeed in Stage 13 the nonconstant exact part of the seam forcing was absorbed by translating the rooted vertex Gaussian. Its image under the gradient then has the stated law, with identity covariance on its image, and the remainder is just the spatial mean. The rooted Gaussian factor in each integral is independent of the pivots, matrices and rotations. Its gradient and the magnetic exact-form Gaussians are independent across all slices and joins. A local frame conjugation has no effect on the norm used for the observable. The dominant centre translate at each join was already accounted for by the fold; equivalently move a twist seam away from the observed local list. Bounded continuous insertions pass through the same truncations as in Stage 13. This proves the fixed-box inner law.

At \(s=\kappa a^2,\ \gamma=\kappa/n^3\), the rescaled coordinate \(Y_j=\gamma^{1/6}X_j\) is tight as \(n\to\infty\) at either period. Its one-point distribution is exactly the normalized discrete Gaussian trace measure of Stage 17 after the dilation (20). The two-bridge estimate there is uniform when \(v\gamma^{1/3}\) ranges in a compact positive interval; this is the case here. Time translation and a union bound give tightness on any fixed list of slices, without asserting independence of the \(Y_j\)'s. Hence \(X_j=O_{\mathbb P}(n^{1/2})\) there. The electric harmonic constants in the preceding display are \(O_{\mathbb P}(n^{-1})\), and the magnetic harmonic constants in Stage 21 are \(O_{\mathbb P}(n^{-2})\). Only the Gaussian pieces survive in these local readings. The projection kernels for the two spatial Gaussian images converge on fixed displacements by their bounded Fourier symbols, continuous away from spatial zero. Both are independent of \(\kappa\).

For the actual growing boxes in Stage 22 its weighted open-box proof applies unchanged to temporal radii with weight \(a\), by the displayed weighted sum of **all** Taylor errors. Away from a chosen twist seam these are ordinary temporal loops, and moving the seam gives translation invariance for the signed radii. In the notation of (33), the electric projection block for \(z\ne0\) is the projector onto the spatial longitudinal component plus
\(a|z_0|^2/(s|z|^2+a|z_0|^2)\) times the transverse projector. The mixed-block norm is bounded by \(\sqrt{as}|z||z_0|/(s|z|^2+a|z_0|^2)\). These statements follow from the same two orthogonal images used in (33). The small-spatial-frequency argument then leaves only the longitudinal projector, with zero mixed block and no dependence on temporal frequency. This is precisely the independent spatial-gradient electric noise just found, jointly with the independent spatial-curl magnetic noise.

Finally choose a growing window of integer offsets around a common origin, with side tending to infinity below a quarter of \(v_j\). At the \(j\)-th finite box, convergence of (16) and of bounded continuous insertions allows \(a_j\) large enough that both purities are within \(1/j\) of their inner limits and the joint radius measures on that finite window are within \(1/j\) in bounded-Lipschitz distance of the corresponding inner measures. Impose this for both choices of \(\kappa\) and both periods, and also \(a_j\ge A_j\). Every fixed subwindow then has the asserted common limit, while (26) gives the different purity limits. This proves the stated quantifiers. In particular, on this class of genuine anisotropic Wilson tori **no rule depending only on all these limiting local distributions** can determine on which side of the seed threshold a sequence lies. The theorem does not cover quantitative errors at growing supports or rules that also use an estimate specific to the isotropic calibrated trajectory. \(\square\)

**Decision after Stage 23.** Local weak-field limits can now be matched in every plaquette orientation at both periods while the selective trace inequality changes sign on the same geometry. Carrying a sign to the real isotropic endpoint would need information beyond these limits. The finite-box and calibrated local arguments supply neither that carry nor the sign of a particular short divisor on the exact path.

## Stage 24. How many mesoscopic curvature observations can still miss the sign

**PROVED.** The examples in Stage 23 can also agree on growing windows. In each circle of \(w=v\) or \(2v\) time steps allow on each slice \(j\) a spatial cube of side \(R_{e,j}\le n/10\) for the electric readings and a possibly different cube of side \(R_{m,j}\le n/10\) for the magnetic readings. Include every plaquette of the requested types based in these cubes. Write \(V_e=\sum_j(1+R_{e,j})^3,\ V_m=\sum_j(1+R_{m,j})^3\), omitting terms on slices where that type is not observed. In the fixed-box inner theory at either \(\kappa_\pm\), the relative entropy of this entire radius record against the *same* finite-\(n\) Gaussian radius record is at most
\[
             C_{\kappa_\pm}\left(\frac{V_e}{n^3}
                                  +\frac{V_m}{n^3 w}\right) .               \tag{34}
\]
The constants are uniform as \(n\to\infty\) at the two specified aspects. Thus for magnetic readings alone the cube can have side \(o(n)\) on **every** time slice. For both types together one may, for example, observe them throughout the time circle on cubes of side \(o(n^{2/3})\).

**Proof of the harmonic signal bounds.** Write \(Z_w(\gamma)=\operatorname{Tr}\!\left(\big[(2\pi)^{-9/2}K_\gamma\big]^w\right)\), the trace of the normalized Gaussian transfer raised to power \(w\), and use the positive integral over matrices and root rotations with this mass. For \(\gamma=\kappa/n^3\), \(Z_w(c\gamma)\) has a positive finite limit for each fixed \(c>0\) by Stage 17. At the two periods the effective times tend to \((c\kappa)^{1/3}/512\) and twice that. Comparing the magnetic integral at \(\gamma/2\) and at \(\gamma\) gives exactly
\[
       \mathbb E\exp\!\left(\gamma\sum_jU(X_j)\right)
                                =Z_w(\gamma/2)/Z_w(\gamma).
\]
Similarly halving the coefficient of the electric Gaussian squared distance and changing variables \(X'_j=X_j/\sqrt2\) gives
\[
       \mathbb E\exp\!\left(\frac14\sum_j|X_j-R_jX_{j+1}|^2\right)
                              =2^{9w/2} Z_w(4\gamma)/Z_w(\gamma).
\]
The norm here sums all nine components. Jensen and cyclic invariance imply
\(\mathbb E U(X_j)\le C_\kappa/(w\gamma)\) and
\(\mathbb E|X_j-R_jX_{j+1}|^2\le C_\kappa\). In the conditional Gaussian law of Stage 23 let \(b_j\) denote the constant magnetic two-form and \(e_j\) the constant electric spatial one-form. Their squared norms per spatial site therefore satisfy
\[
                 \mathbb E|b_j|^2\le C_\kappa/(n^3 w),\qquad
                 \mathbb E|e_j|^2\le C_\kappa/n^3 .
\]
The second bound uses the actual one-step increment, rather than separately estimating its two endpoints.

**Proof of the local shift estimate.** The unshifted comparison record consists, at every slice, of one independent Gaussian on exact spatial two-forms and one on spatial gradients, in three colours, followed by taking the same radii. A constant one-form \(e\) on a cube \(Q\) can be extended to a periodic gradient with squared norm \(\le C(1+R)^3|e|^2\). Take the gradient of \(\chi(x)\sum_i e_i(x_i-x_i^0)\) in a lifted neighbourhood of \(Q\), where \(\chi\) is one through a one-link buffer of \(Q\), supported on a cube of side \(O(1+R)\) and has nearest-neighbour differences \(O(1/(1+R))\). The choice \(R\le n/10\) permits a periodic cutoff of this kind. For a constant two-form \(b\) on \(Q\) use the curl of the one-form \(\chi(x)\sum_{k<i} b_{ki}(x_k-x_k^0)\) in its \(i\)-th component. It agrees with \(b\) on the requested faces and has squared curl norm \(\le C(1+R)^3|b|^2\) by the same product difference estimate. These constructions act componentwise on colours.

Conditional on all matrices and rotations, use these exact shifts on the independent full Gaussians. Their restrictions on the observed cubes have precisely the shifted law, and the entropy for the full Gaussian product is half the sum of squared shift norms, by the translated Gaussian density. Passing to coordinates and radii decreases entropy by conditional Jensen; mixing the conditioning variables costs at most the mean conditional entropy by convexity of \(x\log x\). The signal bounds therefore give (34). In particular the square of the total variation distance is bounded by half its right-hand side, by the entropy inequality for probability measures.

**PROVED (finite Wilson realizations with arbitrary prescribed resolution).** Suppose \(M_j\ge1\) independent records are to be observed and \(M_j(V_e/n_j^3+V_m/(n_j^3 v_j))\to0\) at both periods. Fix any strictly positive measurement resolution \(\epsilon_j\), however small, for independent centred Gaussian noise of variance \(\epsilon_j^2\) per recorded scalar. The common \(a_j\) in Stage 23 can be chosen so the total variation distance between the two systems' noisy \(M_j\)-sample laws tends to zero, while their true unmodified purities have opposite limiting strict inequalities. Indeed (34) is additive for independent samples against the common comparison law, and cannot increase under the noise. At each finite \(j\) the unnoised Wilson records converge weakly to the corresponding inner records. After convolution with the fixed Gaussian density, their densities converge pointwise by weak convergence and hence in \(L^1\) since all have integral one (integrate their pointwise minimum with the limiting density). Choose \(a_j\) large enough that each one-record variation error is \(o(1/M_j)\), together with the previous purity requirements. Tensorizing by telescoping bounds the total error, also if the sample contains independent records at both periods. The same choice argument, using bounded-Lipschitz distance instead of smoothing, gives vanishing expectation difference for bounded unnoised tests with any prescribed finite Lipschitz constants at each \(j\), by increasing \(a_j\) accordingly. Measurement noise enters only this statistical assertion; the Wilson weights and the seed inequalities in both examples are original ones. \(\square\)

**Decision after Stage 24.** Even records on growing spatial cubes through every time slice can have vanishing discrimination at stated sampling budgets. What is missing in this class is the collective, spatially constant component of the signal, for which the exact periodic Gaussian spaces provide no global extension. This is an obstruction for the stated observations on an anisotropic class. It does not exclude a genuinely global estimate on the calibrated neutral transfer.

## Stage 25. The frozen spatial law and its electric kernel uniformly in the box

**PROVED (uniform flat density).** On the neutral angle cell \([-\pi/2,\pi/2]^3\), with both simultaneous sign representatives retained, the probability density in (11) satisfies
\[
                       c|\theta|^{-2}\le h_n^{\rm prob}(\theta)
                                    \le C|\theta|^{-2}                      \tag{35}
\]
for all \(n\ge3,\ \theta\ne0\), with absolute constants. To see the uniformity, write \(D_n\) for the product of the eigenvalues in (11), before taking its reciprocal. In direction \(i\), at fixed transverse grid mode \(p_\perp\), define \(\omega\ge0\) by \(2\cosh\omega-2=4\sum_{j\ne i}\sin^2((2\pi p_j+2\theta_j)/(2n))\). The product in the \(i\)-coordinate is exactly \(2(\cosh(n\omega)-\cos(2\theta_i))\): factor each term \(2(\cosh\omega-\cos x)=e^{-\omega}|e^\omega-e^{ix}|^2\) over the roots of \(z^n=e^{2i\theta_i}\). Hold the transverse angles fixed and replace \(\theta_i\) by \(\pi/4\). For centered representatives \(p_\perp\ne0\), \(n\omega\ge c|p_\perp|\), by the sine lower bound on the centred grid, including the edge of the cell. The log of the corresponding product ratio is bounded by \(C e^{-c|p_\perp|}\), since \(|\cos(2\theta_i)|\le1\). Its sum is bounded independently of \(n\). At \(p_\perp=0\), \(n\omega\asymp|\theta_\perp|\), and \(\cosh(n\omega)-\cos(2\theta_i)\asymp |\theta|^2\) throughout the cell. Thus the ratio of \(D_n\) at the two angle vectors is comparable to their ratio of squared norms. Changing all three coordinates in succession telescopes these squared norms. Inverting and normalizing by the finite integral of \(|\theta|^{-2}\) proves (35).

**PROVED (uniform electric localization and lower bound at flat endpoints).** Let \(Z_{\rm spin}\) be the untwisted zero-angle electric join before centre averaging. For \(a\) sufficiently large, every even \(n\ge4\), and the frozen electric kernel from Stage 10,
\[
 \frac18 e^{-C an(|\theta|^2+|\theta'|^2)}
       \ \le\ \frac{k_a(\theta,\theta')}{Z_{\rm spin}}
       \ \le\ C\exp[-c an\,\textstyle\sum_i(|\theta_i|-|\theta_i'|)^2].
                                                                            \tag{36}
\]
Here the comparison of the two winding triples uses the Wilson *probability law* of a three-dimensional spin system. No saddle expansion with a box-dependent error enters (36).

**Proof of the lower bound.** In the integral over the electric vertex gauges \(g_x\), view unit quaternions as unit four-vectors. For flat constant-link representatives and the identity centre term the integrand is the nearest-neighbour \(O(4)\) spin weight with a fixed rotation \(Q_i\in SO(4)\) on each direction-\(i\) bond, acting by left and right torus multiplication with angles \(\theta_i/n,\theta'_i/n\) up to signs. These rotations commute. The scalar shifts are the same as at zero. Under the zero-angle spin measure, spatial inversion \(x\mapsto-x\) leaves the law invariant and transposes each \(Q_i\) in the inserted energy. Average the two real exponentials. Their mean is at least the exponential with each \(Q_i\) replaced by \((Q_i+Q_i^t)/2\), by convexity. The operator norm of \((Q_i+Q_i^t)/2-I\) is at most \(C(|\theta_i|+|\theta'_i|)^2/n^2\) by the two rotation angles of left-right multiplication. All spins have norm one. Summing the \(n^3\) bonds per direction proves the lower bound on keeping this one positive term of the centre average.

**Proof of the upper bound.** Move constant bond rotations to seams by site changes of spin variables. The resulting boundary rotation in direction \(i\) is \(O_i=Q_i^n\), allowing also the appropriate central sign for each translate. Dropping any one of these twists can only increase the real partition integral. Indeed transfer in its own direction has the usual positive untwisted interplane convolution, sandwiched by positive intraplane multiplication that contains all the other twists. The convolution on unit spins has positive kernel as a quadratic form by the nonnegative tensor-power expansion of \(e^{a u\cdot v}\). The omitted boundary rotation gives a unitary twist in the trace of a positive power. The other commuting rotations allow it to be moved through the intraplane weights. The modulus of the twisted trace is at most the untwisted trace by diagonalizing the positive operator. Drop the two twists other than \(O_i\) in this way.

For completeness, let \(m_0,m_1\) be the average spins in two opposite planes normal to this remaining axis, under the fully periodic untwisted spin measure. The shifted-partition bound of Fröhlich, Simon and Spencer, with the even-period reflection proof for these sphere spins in row 1375 (12), gives \(\mathbb E e^{\langle f,g^k\rangle}\le e^{\langle f,G f\rangle/(2a)}\) for every component \(k\) and mean-zero \(f\), where \(G\) is the inverse spatial Laplacian on mean-zero fields. Row 1375 uses a different aspect; on the cubic spin torus the same shell sum gives \(\|G\|\le Cn^2,\ \operatorname{Tr}G\le Cn^3\). Integrating the component bound against a centred Gaussian of covariance \(2t\) on the mean-zero subspace, for \(t=c a/n^2\), gives \(\log \mathbb E e^{t\sum_x |g_x^k-\bar g^k|^2}\le C t n^3/a\), by \(-\log(1-x)\le2x\) at \(0\le x\le1/2\). Hölder gives the vector bound after decreasing \(t\). Since \(\sum |g_x-\bar g|^2=n^3(1-|\bar g|^2)\), exponential Markov gives \(\Pr(|\bar g|<3/4)\le C e^{-c an}\) uniformly at large \(a\). For either plane, subtract its average from the volume average. Its scalar test has Green variance at most \(n^{-3}\sum_{r=1}^{n-1}[4\sin^2(\pi r/n)]^{-1}\le C/n\) since it has only normal frequencies. The component bound and a union bound thus give
\(\Pr(|m_i-\bar g|>x)\le C e^{-c an x^2}\). In particular the two plane means are close to each other and have size at least \(1/2\) with these tail bounds.

Write \(A(x,y)\) for the positive symmetric half-period spin-transfer kernel on configurations of the two planes. Their joint density is \(A(x,y)^2/Z_{\rm spin}\). The single-twist quotient is its Hellinger affinity with its transform by rotating the first configuration by \(O_i\): multiply the two half kernels, using symmetry and global rotational invariance. Put \(\delta_i=\min_{|q|=1}|(1-O_i)q|\). The event \(|m_0|\ge1/2,\ |m_1-m_0|<\delta_i/8\) cannot hold both before and after the rotation when \(\delta_i>0\). Its complementary untwisted probability is at most \(C e^{-c an\delta_i^2}\) by the preceding estimates. Splitting the affinity over the event and its complement and applying Cauchy–Schwarz bounds the one-twist quotient by twice the square root of that probability. The bound by 1 suffices at \(\delta_i=0\). For left-right quaternion rotation the two complex rotation angles are \(\theta_i\pm\theta_i'\) up to the centre sign. On the folded cell \(\delta_i\ge c\,||\theta_i|-|\theta_i'||\) for either sign: taking angles modulo \(\pi\) and then modulo inversion can only reduce their circle distance, and chord and geodesic distances are comparable. Using the best of the three single-axis bounds and averaging the eight signs proves (36). \(\square\)

**Decision after Stage 25.** Bounds (35)–(36) are uniform when \(a=\beta_K\) and \(n\) grows on the actual release geometry. They bound the full electric join without needing its limiting helicity modulus. I next use their lower and upper bounds together to test the neutral heat trace.

## Stage 26. The same release electric coupling, with the spatial coupling still free

**PROVED.** There exist \(0<r_0<1\) and \(C,a_0<\infty\), independent of even \(n\ge4\) and \(a\ge a_0\), for which the magnetic-first limit on the SU(2) spatial cube satisfies
\[
        0\le 1-\lim_{s\to\infty}P_{n,v}(a,s)\ \le C r_0^{\,v-2}
                        \quad(v\ge2),                                      \tag{37}
\]
at least for \(an\) above an absolute constant. In particular for the **actual \(a=\beta_K\)** and \(v=u=n/512\), the frozen purity tends to one. At every sufficiently late \(K\) there is a finite \(s_0(K)\) such that for all \(s\ge s_0(K)\), keeping precisely the release electric coupling, side and time period, \(P_{n,u}(\beta_K,s)>457/625\). This conclusion is about the three spatial couplings after taking them sufficiently large. It gives no upper bound \(s_0(K)\le\beta_K\).

**Proof of the spectral estimate.** Take the frozen operator of Stage 10, rescale the angles to \(A=\sqrt{an}\,\theta\), and remove the scalar \(Z_{\rm spin}/\sqrt{an}\), which cancels in purity. Transfer the operator to the fixed measure \(d\mu(A)=|A|^{-2}d^3A\) on \(\mathbb R^3\) by multiplying its kernel by square roots of the transformed density at its two arguments, extending it by zero off the scaled cell. Formula (35) bounds those two density factors above and below by absolute positive constants inside the cell after the scalar is removed. By (36) the resulting positive self-adjoint kernel \(K\) is bounded above by
\(C\exp[-c\sum_i(|A_i|-|B_i|)^2]\). This majorant is Hilbert–Schmidt for \(\mu\) by the displacement integral after (13). On every fixed ball of radius \(R\) inside the cell the kernel is bounded below by \(d_R>0\). If the cell is smaller, the same lower bound holds on its intersection with the ball. The ball of radius one is contained for the stated \(an\), so its indicator gives \(\lambda_1(K)\ge l>0\) by the Rayleigh quotient. The Hilbert–Schmidt norm is bounded by an absolute constant. The kernel is positive on the cell, and the top eigenfunction \(h\) may be taken strictly positive there, normalized in \(L^2(\mu)\). Simplicity follows by strict positivity in the absolute-value Rayleigh inequality. Odd functions have zero transfer; all these estimates therefore apply to the neutral quotient.

For clarity, a common lower bound on each compact ball alone would not give a uniform spectral gap on the expanding cell. The common square-integrable majorant also gives \(\|\mathbf1_{\{|A|>R\}}K\|_{\rm HS}\le\epsilon_R\to0\). Every unit eigenfunction with eigenvalue at least \(l/2\) consequently has norm at most \(2\epsilon_R/l\) outside the ball. On the ball \(h\) is bounded above uniformly in \(n,a\) by its eigenvalue equation and the supremum there of the majorant's one-row \(L^2(\mu)\) norm, which is finite by Gaussian decay at infinity and local integrability of \(\mu\). Denote this upper bound by \(H_R\). Write \(D\) for the ball intersected with the cell. For a second real normalized eigenfunction \(f\perp h\) with \(\lambda_2\ge l/2\), the identity
\[
 \lambda_1-\lambda_2=\frac12\iint K(x,y)h(x)h(y)
                     \big|f(x)/h(x)-f(y)/h(y)\big|^2\,d\mu(x)d\mu(y)
\]
follows by expanding the square and the two eigenvalue equations. Restrict it to \(D^2\) and use \(K(x,y)\ge (d_R/H_R^2)h(x)h(y)\). The resulting bound is
\[
 \lambda_1-\lambda_2\ge(d_R/H_R^2)
   \left(\|\mathbf1_Dh\|^2\|\mathbf1_Df\|^2
                 -|\langle\mathbf1_Dh,\mathbf1_Df\rangle|^2\right).
\]
For \(R\) fixed sufficiently large the parenthesis is at least \(1/2\) by the tail bounds and orthogonality. For \(\lambda_2<l/2\) there is already a gap at least \(l/2\). This proves a common relative bound \(\lambda_2/\lambda_1\le r_0<1\). Finally \(\sum_{j>1}(\lambda_j/\lambda_1)^v\le r_0^{v-2}\|K\|_{\rm HS}^2/l^2\). Positivity and retaining the ground term in the purity give (37). The finite-\(s\) conclusion follows by ordinary fixed-\(K\) convergence of both cyclic integrals (Stage 10), with a strict limiting margin.

**PROVED (comparison on this same electric sequence).** For weak compact \(U(1)\) with the three half-turn projections, the corresponding limit is zero when \(v=u,\ a=\beta_K\to\infty\). Indeed on flat windings it is convolution on the angle torus of period \(\pi\), with a nonnegative transfer kernel. Estimates (36) for the abelian join hold with \(\mathrm{dist}(\theta-\theta',0)\) on that torus, with the lower estimate localized around coincidence. The proof uses the two-component unit spin instead of the four-component spin. The reflection, quadratic-shift, and plane-mean arguments above use only unit length, positive dot-product convolution, and a fixed number of components. In one angular plane a twist moves every unit spin by the same chordal distance; the identity centre term gives the local lower bound by inversion as before. The uniform winding measure from Stage 10 and the two Gaussian bounds imply that the normalized convolution density has mean squared angular displacement at most \(C/(an)\), by integrating the upper bound and integrating the lower bound on a ball of radius \(1/\sqrt{an}\) in its denominator. Thus its Fourier multipliers satisfy \(1-\lambda_k/\lambda_0\le C|k|^2/(an)\) for the surviving frequencies, by the cosine inequality and symmetry. At \(v=n/512\), arbitrarily many fixed \(k\)'s have \((\lambda_k/\lambda_0)^v\to1\), so the purity tends to zero. With the entire abelian centre, and for 5D \(SU(2)\), the frozen law remains a point and its purity is exactly one. Therefore (37) alone does not select against 5D. The different, sign-selective assertion against both systems is (30).

**Decision after Stage 26.** This reaches the release electric coupling and proves the desired numerical bound on a nonempty tail of the real magnetic-coupling axis for every sufficiently late cutoff. The full-space magnetic law is concentrated on flats at that end. At the required point the windings are Haar and (32) shows spatially varying curvature propagating. The sign of the real purity change across that interval is still missing.

## Stage 27. A lower limit on the spatial coupling for transporting the frozen winding law

**PROVED.** Put \(a=\beta_K,\ v=u\) or \(2u\). In the true neutral Wilson circle at arbitrary real \(s\ge0\), let \(\varphi_i\in[0,\pi/2]\) be the distance of the \(i\)-th based straight spatial winding angle to the centre. In the frozen circle use the identical observation. Then
\[
 \Pr_{a,s}\!\left(\max_i\sqrt{an}\,\varphi_i\le b\right)
   \ \le\ C b^9\left(\frac{1+(4s+2a+1)/n}{an}\right)^{9/2}
                   \quad(b>0),                                             \tag{38}
\]
whereas in the frozen circle the probability is at least \(c b\) for \(0<b\le1\), uniformly at late cutoffs. If \(s=o(a n^2)\) the total variation distance of these *three scalar winding-angle laws* tends to one. If \(s\le L_0 a n^2\) along a subsequence, for any fixed \(L_0<\infty\), that distance has strictly positive lower limit there. Thus a vanishing-error transport of this winding law from the proved seeded endpoint (37) requires \(s/(a n^2)\to\infty\). This necessary condition is for transporting the observation, not for the scalar seed inequality.

**Proof on the growing finite-\(s\) tori.** Use row 1145's private-link construction on the three based lines, omitting their first and last bonds. No face touches two of the remaining selected bonds; condition on all unselected links and the twist. Each selected variable is independent tilted quaternion Haar with staple length \(\le B=4s+2a\). In the one-link bound of row 1145 (1) its proof gives the stronger adjacent ratio
\[
  I_{k+1}(x)/I_k(x)<\exp[-\operatorname{arsinh}((k+1/2)/x)]\quad(k\ge1).
\]
The proof there uses the differential equation of the ratio and its strictly increasing positive comparison root. Multiplying the ratios for dimension \(d\) and retaining the last half of the summands in the exponent yield
\(I_d(x)/I_1(x)\le\exp[-c\min((d-1)^2/(1+B),d-1)]\) for \(d\ge2,\ 0<x\le B\), using \(\operatorname{arsinh}y\ge c\min(y,1)\); zero tilt is exact Haar. With \(m=n-2\) private links in a winding the representation matrix norms multiply. Fourier inversion with term bound \(d^2\) times that product shows its conditional Haar density is at most \(C(1+(1+B)/m)^{3/2}\). Indeed below \(d-1=1+B\) sum the Gaussian series by comparison with the integral of \(r^2 e^{-c m r^2/(1+B)}\) and a constant, and above it sum the exponential tail. This works with arbitrary fixed intervening transports. The three conditional densities multiply. The Haar probability of distance at most \(b/\sqrt{an}\) from either centre point is bounded by \(C(b/\sqrt{an})^3\) by quaternion polar integration. Multiplication proves (38), also in any positive mixture of the twists. The sharpening of the density at large \(B/n\) matters to the scale in (38).

**Proof in the frozen thermal circle.** In the representation of Stage 26, the positive top eigenfunction \(h\) has an absolute lower bound on \(|A|\le1\). Indeed choose the same fixed \(R\) so \(\int_D h^2\ge 3/4\). The uniform bound \(h\le H_R\) there gives \(\int_D h\ge3/(4H_R)\); the eigenvalue equation, the lower kernel bound \(d_R\) and \(\lambda_1\le C\) give the assertion. The thermal one-slice density is the convex mixture of \(|h_j|^2 d\mu\) with weights \(\lambda_j^v/\operatorname{Tr}K^v\). By (37)'s proof the top weight tends uniformly to one. The ball \(|A|\le b\) has \(\mu\)-mass \(4\pi b\) and is contained in the event in (38). This proves the lower bound. The same thermal measures of \(A\) are uniformly tight by the top eigenfunction tail estimate of Stage 26 and the vanishing excited fraction. Thus when \(s=o(a n^2)\), (38) makes the true probability of every fixed rescaled ball vanish, while the frozen probabilities approach one on sufficiently large balls uniformly in late \(K\). This gives variation distance tending to one. When \(s\le L_0 a n^2\), (38) gives \(C_{L_0} b^9\) at late cutoffs; choose fixed \(b>0\) sufficiently small that this is \(<c b/2\). The positive lower distance follows. \(\square\)

**Decision after Stage 27.** This tests the real route at the same \(a=\beta_K\) without extrapolating a fixed-box integral. The magnetic tail is seeded and its measured winding mechanism fails all the way down through \(s=O(\beta_K n^2)\), in particular at \(s=\beta_K\). A proof carrying the scalar sign while replacing that mechanism would need a different global observable or a controlled renormalization of the winding field. Rows 1145, 1227 and 1642 already distinguish bare winding arrays from flowed observations; their required growing-box comparison remains unsupplied here. The two-period derivative reformulations in TWO-PER and VIR-DOWN do not fill this gap.

## Stage 28. Checking the untruncated local test and the remaining real comparison

**PROVED (uniform moments for the actual anisotropic comparison).** The convergence of local radii in Stages 22–23, for \(a=\beta_K,\ a\le s\le a^p,\ s/a\to\infty\), also holds for fixed polynomial moments. For a plaquette with its own weight \(c_\pi\) and the prescribed twist sign, uniformly at both periods,
\[
                     \mathbb E_+ e^{c_\pi(1-\sigma_\pi\operatorname{Re}U_\pi)/2}
                                     \le C_p .                              \tag{39}
\]
The weighted open-box Gaussian proof in Stage 22 applies both to the original coefficients and to half of all coefficients (use the same box partition). The log error per site tends to zero and the two Gaussian normalizers differ in log by at most \(C V\), since halving a precision multiplies each real coordinate's integral by \(\sqrt2\). This bounds \(V^{-1}\log[Z^{\rm per}(c/2)/Z^{\rm per}(c)]\) by a constant, in shifted conventions. The single-orientation dissemination inequality of row 1151 (21) applies with the directional coefficients held fixed: transfer in each of the four directions has positive layer factors when the coefficient of the marked plaquette is halved. Trace Hölder in successive directions gives a one-plaquette periodic log moment at most the per-site log cost of halving its whole orientation. Positivity of all the shifted deficits bounds that cost by the one for halving all orientations. To pass to the neutral expectation, its denominator is at least \(1/8\) the periodic one. For a spatial one-face positive insertion its projected numerator is at most the full periodic one by the positive sandwich of the insertion and a transfer power. For an electric one-face change the modified single-step transfer \(T'\) is positive, since its convolution still has positive multipliers; the same comparison follows by sandwiching \(T'\) by \(T^{(v-1)/2}\). The projection commutes with all these operators. This proves (39). Hölder and truncation give the moment conclusion. In particular the one-step *untruncated* covariance of the spatial difference in (32), with its new normalization \(s\), tends to zero for the parabolic magnetic coupling at the actual \(a=\beta_K\). The spatial mean \(s\,\mathbb E(1-\operatorname{Re}U_{ij})\) tends to 1 and the electric mean \(a\,\mathbb E(1-\sigma_\pi\operatorname{Re}U_{i4})\) to \(1/2\): the limiting spatial and electric projection blocks have ranks 2 and 1 in their respective three directions at nonzero momentum, are isotropic after grid integration, and have three independent colours. The two periods share these local limits. Their difference at the precision needed for the thermal ratio is undetermined.

**ARGUED (where the attacks stop).** At the exact linear tree interpolation there is a zero-free inner disk, an upper limit on bounded continuation and global failure of double divisibility at the prescribed \(u\). The nearby-pole proof on modified paths needs boundedness on the imaginary axis; the weak magnetic factor of the linear path there is a phase, so its self-adjointness argument fails. At real couplings the two proven seeded regimes at the release electric coupling are the small magnetic strip of row 1145 and the large magnetic tail of (37). Neither argument bounds the minimum of the purity between them. Formula (30) supplies a law-dependent selective comparison, but (31)–(32), (34), (38) show precisely what is lost in taking it as a substitute for the calibrated transfer. No sign for the intermediate isotropic thermal comparison, and no disproof of the on-file reduction, follows from these results.

**RESULT — (c), quantified obstructions and a selective anisotropic Wilson law.**
**PROVED by hand.** At the prescribed period, the affine ratio is close to one on (28a), cannot be uniformly bounded and holomorphic on a disk of radius \(C/\beta_K\), and has at least \(c u/\log(2+\beta_K)\) distinct uncancelled zeros or poles there. Actual poles occur within (22); their presence in the smaller disk at \(u\) remains undecided.
**PROVED by hand.** At the same release electric coupling, side and period, every sufficiently large spatial magnetic coupling gives purity above \(457/625\) by (37). Its frozen winding law stays separated from the actual one through \(s=O(\beta_K n^2)\) by (38).
**PROVED by hand.** In the ordered weak limit (30), 4D \(SU(2)\) passes the threshold for \(\kappa>(512\tau_*)^3\); 5D \(SU(2)\) and 4D compact \(U(1)\) with the identical discrete projection both give zero. Formula (34) gives Wilson examples on opposite sides with indistinguishable mesoscopic curvature records at the stated resolution.
**OPEN.** No estimate carries the sign to the isotropic point \(s=a=\beta_K\). Neither (PUR-io) nor its negation nor the Jaffe–Witten mass gap is established. This is unreviewed research text; no numerical or Lean proof step was used.
