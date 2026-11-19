# Repo search

**GUIDE.** Row 1157 started on 19 November 2026 at 06:11 UTC on the Mac mini. Plan. Check the lead’s repository search, indexed sources, and row ownership. Verify the row 1155 reduction used here, then test analytic routes to the rectangle bound and record each result with its hypotheses.

**GUIDE.** Science checkout `5fef0732f`. There is no target-specific prior note at this revision. The lead's 8 November digest covers thirteen earlier questions on main and PRs 10114, 10133, 10134 and 10141. The gap supplement identifies the soft-kernel project, the earlier hard-route tree and the existence snapshot. I checked the positive one-step loop witness and the contraction for bare coupling at most \(1/32\) on PR 10114, lines 106–149 and 315–327. PR 10133 has the identical blob. PR 10134 contains an earlier hard-route snapshot in the same lane. On PR 10141, `fp1.md` lines 302–315 control a constrained classical field at one scale. On main `8b11ae2bb9`, the finite-clock Villain note of 14 September, lines 4–9 and 79–94, uses a finite abelian group. None supplies the Wilson trace on a fixed physical cube. The registry's W row points to the T0 tree. I found no other row owning the estimate of 1157. The council's flux-only obstruction and its requirement to keep neutral excitations apply here. [Lead search](prior/repo-search-2026-11-08.md) · [Gap supplement](prior/gap-crux-prior-ym.md) · [Council](gap-council-synthesis.md)

**GUIDE.** Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the positive gauge-projected transfer and the periodic trace identity GL8. I checked outline lines 2313–2336 and 31871–31882, and CA-I lines 2704–2712, at `31a47c543775`. CA-I lists a mass gap among the conclusions it excludes. Credit Tadeusz Bałaban for the renormalization-group method and Sourav Chatterjee for the weak-coupling free-energy method used upstream. The lane's inputs and research labels carry their stated scope. [Outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2313-L2336) · [Complete account](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2704-L2712)

**OPEN.** Fix an admissible physical side \(L\), with \(n=L/a_j\), \(4\mid n\), \(T=n/2\), and \(N=n^3\). The bare inverse coupling is \(\beta_j\to\infty\). Write \(U=F/\|F\|\) for the Wilson transfer on the gauge-invariant slice space. The finite-volume test is whether at some such \(L\)
\[
 \liminf_j \frac{\operatorname{Tr} U^{2T}}{(\operatorname{Tr} U^T)^2}>\frac{1650}{1651}.
\]
The quantifier over \(L\) belongs to the test. A bound at a time much longer than the spatial side does not suffice. Row 1155 is unchecked in this checkout. [Row 720](gap-phys-seed.md) · [Row 1155](gap-solve7-astra62.md)

**GUIDE.** For a spatial box \(H\), \(S(t;H)=\operatorname{Tr}[(F_H/\|F_H\|)^t]-1\) is its full excited thermal sum, with the trace taken after the \(t\)-th power. For a joint law with density \(p(x,y)\) relative to a product measure, its rectangle affinity is the integral of
\[
              \sqrt{p(x,y)p(x',y')p(x,y')p(x',y)}
\]
over two independent copies of each reference coordinate. It is one for independent observations. Equation (25) gives the final unconditioned test, (23) controls its twist statistic, and (33) tests a possible estimate for its two-collar law.

## Two excitations of the same electric character

**GUIDE.** Rows 754 and 876 use the square of one real charged eigenfunction. Their bounds involve its sup norm or its fourth moment. The argument below uses two orthogonal vectors of the same character. It gives an unconditional spectral comparison for the second vector and leaves one possible exception per character. [Earlier fusion inequality](gap-loop-eq-opus.md) · [Row 876 and its correction](gap-brainstorm2-check-astra.md)

**PROVED (a quarter of the neutral Dirichlet gap).** Order the positive Wilson eigenvalues in each electric sector after division by the vacuum eigenvalue. Write \(\rho\) for the first *excited* eigenvalue in the neutral sector. Write \(\lambda_{\chi,2}\) for the second eigenvalue **counting from the bottom energy** in a nontrivial character \(\chi\), including multiplicity. Set a missing second eigenvalue to zero. At every finite cutoff and every integer \(s\ge1\),
\[
 1-\lambda_{\chi,2}^{\,s}\ \ge\ \tfrac14(1-\rho^s).                 \tag{1}
\]
In particular the subspace with \(1-\lambda<(1-\rho)/4\) has dimension at most eight, including the vacuum. This comparison uses the lattice transfer itself.

**PROVED.** Use the positive symmetric magnetic sandwich for \(F\). Its strictly positive vacuum \(\psi\), normalized in slice Haar measure, is fixed by the eight spatial centre flips \(G\). The conjugate \(P f=\psi^{-1}U(\psi f)\) is Markov and reversible for \(\pi=\psi^2\,dx\). With \((X,Y)\) at stationarity \(s\) steps apart, write \(\mathcal E_s(f)=\tfrac12\mathbb E|f(X)-f(Y)|^2\). Neutral functions satisfy
\[
 (1-\rho^s)\operatorname{Var}_\pi(f)\le\mathcal E_s(f)
\]
by spectral decomposition. Vector and complex norms give the sum over real components. The kernel is real and the characters take values in \(\{1,-1\}\), so choose real orthonormal eigenfunctions \(f,g\) for the top two eigenvalues in \(\chi\). Put \(z=f+ig\), \(r=|z|\) and \(w=z^2/r\), with \(w=0\) at \(r=0\). Both \(r,w\) are neutral. In the following calculation the integral is against \(\pi\).
\[
 \int r^2=\int |w|^2=2,\qquad \int rw=\int z^2=0,\qquad
 |\!\int w|^2\le 2-(\int r)^2=\operatorname{Var}(r).
\]
For the last inequality subtract \(r(\int r)/2\) from the constant vector \(1\) before pairing it with \(w\). Cauchy–Schwarz gives the displayed bound. Hence \(\operatorname{Var}(r)+\operatorname{Var}(w)\ge2\).

**PROVED.** For \(z=r e^{i\theta},z'=v e^{i\phi}\), put \(d=\theta-\phi\). Then
\[
 |r-v|^2+|w-w'|^2=2(r-v)^2+4rv\sin^2 d
 \le 4|z-z'|^2 .
\]
The formula extends to a zero radius. Apply it to the stationary pair and then apply the neutral inequality. This gives
\[
 2(1-\rho^s)\le \mathcal E_s(r)+\mathcal E_s(w)
 \le4[\mathcal E_s(f)+\mathcal E_s(g)]\le8(1-\lambda_{\chi,2}^{\,s}).
\]
This proves (1), including degenerate top levels. No fourth moment or pointwise eigenfunction bound enters.

**PROVED (sharp constant for this argument's class).** For heat evolution through time \(h>0\) on a circle of length \(2\pi\), with the half-turn as the flip, the two leading odd functions are sine and cosine of frequency one. The neutral excitation has frequency two. Fourier integration gives the ratio \((1-e^{-h})/(1-e^{-4h})\to1/4\). Thus degree two of the phase map has a spectral cost that cannot be decreased in this class. The example establishes sharpness for reversible positive transfers with a flip. It assigns no numerical value to a Wilson eigenvalue. The same circle occurs as a test of the fourth-moment formula in the check of row 876.


## The part of the heat trace above the seven exceptional levels

**PROVED.** Write \(Z_\chi(v)=\operatorname{Tr}(P_\chi U^v)\), \(S_+(v)=Z_+(v)-1\), and \(b_\chi=\lambda_{\chi,1}\) for \(\chi\ne+\). Put \(b_+=1\). At integers \(3\le v<T\),
\[
 0\le \operatorname{Tr}U^T-\sum_\chi b_\chi^T
 \le S_+(T)+7[1+S_+(v)]\left(\frac{3+\rho}{4}\right)^{T-v}.       \tag{2}
\]
Indeed \(Z_\chi(v)\le Z_+(v)\). In the electric Fourier sum all twisted Boltzmann integrals are nonnegative, so replacing each character sign by one gives this bound. It is already used in row 876. In each charged sector remove its top level once. In the other levels retain \(v\) steps in the trace and pay \(((3+\rho)/4)^{T-v}\) by (1) on the rest. Summing proves (2). The same right side bounds the omitted trace at \(2T\), by monotonicity of every normalized weight. Thus the purity differs from
\[
 \frac{\sum_\chi b_\chi^{2T}}{(\sum_\chi b_\chi^T)^2}
\]
by at most three times the right side of (2). To see this, vary the numerator first with denominator at least one, then the denominator with numerator at most the unperturbed denominator's square and use \(1-(1+x)^{-2}\le2x\).

**PROVED (order of the limits).** At a fixed physical size let \(v=T/2\). If \(\limsup_j S_+(v)<d<1\), then \(\rho^v\le d\) eventually. Consequently the upper limit of the right side of (2) is at most
\[
 d^2+7(1+d)d^{1/4}.                                                 \tag{3}
\]
Here \(S_+(2v)\le S_+(v)^2\), and \(((3+d^{1/v})/4)^v\to d^{1/4}\) by differentiating the logarithm at zero. Along any family of sides for which this neutral bound tends to zero after the cutoff limit, all charged multiplicity beyond the seven stated levels drops out in absolute trace units. The hypothesis concerns a **shorter physical period** than the target. It remains OPEN. Control of the seven bottoms alone cannot pay for the shorter neutral trace.

**PROVED (the surviving ambiguity is real in the comparison class).** Take a product of a rank-one neutral projection with the convolution \(cI+(1-c)\Pi\) on the uniform eight-element group, where \(\Pi\) averages over that group and \(0<c<1\). The transfer is positive, has strictly positive kernel on the finite group, and commutes with translations. The neutral excited heat trace vanishes. Each exceptional level is \(c\). The exact purity at \(T\) is \((1+7c^{2T})/(1+7c^T)^2\). Choosing \(c=e^{-u/T}\) supplies the full range between the limits \(1/8\) and \(1\) as \(u\) varies. This obstruction allows positivity, translation symmetry of the eight flips and a perfect neutral trace. The remaining task for this route is a Wilson estimate on transport of the exceptional signs.


## Which single charged states can evade (1)?

**PROVED.** At a fixed \(s\ge1\) write \(\gamma=1-\rho^s>0\), \(\delta_\chi=1-b_\chi^s\). Define \(h_\chi\) as the infimum of \(\mathbb P(\sigma(X)\ne\sigma(Y))\) over measurable signs with \(\sigma(bx)=\chi(b)\sigma(x)\) almost everywhere, for the stationary \(s\)-step Wilson pair used in (1). Then
\[
 \delta_\chi\ \le\ 2h_\chi\ \le\
 (1+\sqrt{2/\gamma})^2\delta_\chi,\qquad
 h_{\chi\eta}\le h_\chi+h_\eta .                                     \tag{4}
\]
Such signs exist. One example is the sign of the product of the straight winding-loop traces in the directions selected by \(\chi\). Its zero set has Haar measure zero because each loop has a Haar-distributed holonomy under product Haar. The finite-cutoff vacuum is absolutely continuous there. Equivariance and all identities may be restricted to a common invariant full-measure set.

**PROVED.** Every test sign has Dirichlet value twice its disagreement probability. For a real unit top eigenfunction \(f\) in \(\chi\), contraction under absolute value and the neutral gap give \(\operatorname{Var}(|f|)\le\delta_\chi/\gamma\). Round \(f\) to its sign \(\sigma\), using the preceding test sign on its zero set. With \(a=\int |f|\,d\pi\) one has \(\|\sigma-f\|_2^2=2(1-a)\le2(1-a^2)\). Since \(0\le P^s\le I\) in operator order, the Dirichlet seminorm of \(\sigma-f\) is at most its ordinary norm. The triangle inequality in that seminorm gives the upper bound of (4). Products of test signs have character \(\chi\eta\), and a change of their product requires at least one change, proving the last bound.

**PROVED (classification at a separated spectral scale).** Consider any sequence of boxes and step counts with \(\inf\gamma>0\). Pass to a subsequence on which the seven \(b_\chi^s\) have limits. The characters with limit one, including \(+\), form a subgroup \(H\). This follows in both directions needed for closure from (4). For each basis character take a rounded sign with disagreement tending to zero. Together the signs give a map onto \(\{\pm1\}^{\dim H}\) with the exactly uniform law under the vacuum. Indeed a centre translation acts by the prescribed character values and, by independence of the basis characters, acts transitively on these sign tuples. With probability tending to one the tuple is unchanged in an \(s\)-step transition. Its Walsh products are orthonormal and give one nearly invariant vector per element of \(H\). Equation (1) places every second level of their respective characters at Dirichlet distance at least \(\gamma/4\). In particular a slow charged level in this regime is visible in principle as one nearly conserved binary reading. The functions can depend on the entire spatial field.

**PROVED (the obstruction to this route).** The finite-group comparison following (3) leaves \(\gamma=1\) and makes \(h_\chi=(1-c^s)/2\) as small as desired. Here each character has, up to a constant sign, only one equivariant sign on the group. Thus a lower bound on \(\gamma\) alone gives no positive lower bound on \(h_\chi\), even with the multiplicity comparison (1). Earlier straight winding readings lose their low-energy overlap on a fixed physical grid by row 1145 (4). They test one set of signs, whereas a lower bound for the infimum in (4) must cover every equivariant sign. [Row 1145](gap-solve2-astra62.md)


## Reading the twist on a transverse slice

**GUIDE.** Mack and Petkova's centre decomposition and row 1155 (29) give a minimum-area estimator using the whole four-torus. Here the estimator sees only a three-dimensional slice, or even a strip in that slice. This change of support matters because two distant spatial slices can then be compared inside the *same* mixed probability law. [Centre decomposition](gap-cr-tomboulis-max.md) · [Whole-torus estimator](gap-solve7-astra62.md)

**PROVED (input from the Wilson action).** Give \(b\in G\) mass \(Z_b/\sum_c Z_c\) in the mixture of temporal twists at period \(p=T\) or \(2T\), and take its adjoint field. For a specified set of \(k\) faces the probability that all their *true twisted* fundamental traces are negative is at most \(8(Ce^{-c\beta})^k\), with absolute constants for large \(\beta\). Here are the transfer details from row 1155 used in applying this estimate. Divide each twisted integral by the untwisted partition function. For marks in an electric orientation, reduce their plaquette couplings to \(\beta/2\). The unnormalized vacuum convolution mass increases by at most a constant per mark, since its Haar integral with weight \(e^{-b(1-w)}\) is comparable to \((1+b)^{-3/2}\) by the SU(2) polar integral. Each normalized convolution decreases in positive operator order. Its spin multipliers are \(I_d(b)/I_1(b)\). The successive ratios \(I_{k+1}/I_k\) are increasing, as follows from the differential equation and strict upper barrier in row 1145 (1). The tensor convolutions commute, so sandwiching them with the unchanged magnetic multiplier and gauge projection preserves the order. Schatten Hölder over the layers, with the unitary twist at the seam, bounds the tilted integral by \(C^k\). Indeed each layer's Schatten \(p\)-norm is bounded by the corresponding scalar factor times that of the homogeneous positive transfer, whose \(p\)-th power has trace \(Z_0\) in the original normalization.

**PROVED.** For marks of one spatial orientation use the electric square roots on each side of the modified magnetic multiplier. The \(p\)-th power of this positive layer has trace the *untwisted* partition with that pattern repeated \(p\) times. Rotate one of the marked directions to time on this repeated torus. The electric estimate with no twist gives the scalar cost \(C^{p k_t}\) for \(k_t\) marks on the layer. Take \(p\)-th roots and use Hölder in the original time direction to remove the unitary seam. Finally ordinary Hölder in the positive tilted path measure combines the six orientations, reducing the exponent in the exponential moment by six. On each negative face \(1-w^b\ge1\). Markov's inequality gives the stated suppression after summing eight unnormalized measures, since \(\sum_b Z_b/Z_0\ge1\). This verifies the local probabilistic input without a bound on \(Z_0/Z_b\). No sampling or enumeration is used.

**PROVED (two bits on one slice).** Choose a spatial direction \(j\). At \(x_j=z\) take the whole three-torus in the other two spatial directions and time. Let \(c_j\) be the two entries \(b_i,\ i\ne j\), of the temporal twist. The adjoint links internal to this slice determine an estimate \(d_j(z)\) such that
\[
       \mathbb P\{d_j(z)\ne c_j\}\le C n^3 e^{-c\beta n}.             \tag{5}
\]
Choose representative link lifts there and their negative-face cochain \(D\). Among all \(D'\) with \(D'+D\) closed on the slice minimize \(|D'|\) with deterministic ties, and take the two space-time periods of \(D'+D\). Addition is modulo two. A lift change adds an exact cochain to \(D\), leaving the feasible face sets and their periods relative to \(D\) unchanged. Vertex gauge transformations also preserve the result. Ignoring traces identically zero is valid by absolute continuity and the continuous one-plaquette Haar law.

**PROVED.** The true twisted negative set \(D_0\) restricted to the slice is feasible and has the required two periods relative to \(D\). If a reported bit is wrong, the closed difference \(D'+D_0\) has a connected component \(C\) with that nonzero period. Adjacency means lying on a common elementary cube. Each component is closed, since the faces incident to any one cube cannot be split between components. All parallel translates of the detecting two-torus pair equally with \(C\). They are disjoint, so \(|C|\ge n\) for either of the two reported bits. Flipping \(C\) in \(D'\) was feasible, hence \(|D'\cap C|\le |C|/2\). At least half of \(C\) is truly negative. A chosen connected set of size \(k\) has at most \(2^k\) candidate half-sets. The preceding probability bound pays \(e^{-c'\beta k}\) after this choice. There are at most \(C n^3 C_1^k\) candidate connected sets, by rooting and walking a doubled spanning tree on a bounded-degree graph. The geometric sum for \(k\ge n\) proves (5).

**PROVED (smaller support).** For bit \(b_i\) the slice can itself be restricted to \(\mathbb T_i\times\mathbb T_{\rm time}\times I\), where \(I\) is an interval of \(w\) vertices in the remaining spatial direction, \(2\le w\le n\). For \(w=n\) use the full circle or omit its closing bonds. Cohomology need only be tested on the specified two-tori. Successive translates bound the slab between them, so a nonzero period costs at least \(w\) faces. Cube adjacency and minimization work also at free boundary cubes. The same argument gives
\[
        \mathbb P\{\widehat b_i\ne b_i\}\le C n^2 w e^{-c\beta w}.     \tag{6}
\]
Thus three such strips read the full twist at **one** period. They may intersect. A union bound suffices. A width \(\lceil A(1+\log n/\beta)\rceil\), increased to at least two, gives any specified inverse power accuracy by choosing \(A\). Even the union of all three uses \(O(n^2w)\) links. Row 1155 used a four-dimensional classifier for this quantity.


## A directional obstruction in the actual adjoint measure

**PROVED.** At period \(T\) let \(A_t=\operatorname{Tr}U^{2T}/(\operatorname{Tr}U^T)^2\) be the full untwisted purity. In the temporal-twist mixture let \(A_j\) be the rectangle affinity of the raw adjoint fields on two different slices perpendicular to spatial direction \(j\). They can be any distance apart. For large \(\beta\),
\[
 A_j\le \frac14\left(1+
             \sum_{\substack{\chi\ne+\\\chi_j=0}}\frac{p_\chi(T)^2}{p_+(T)^2}
                      \right)+O(n^{3/2}e^{-c\beta n})
 \le \frac14\left(1+\left(\frac{1-A_t}{A_t}\right)^2\right)
                      +O(n^{3/2}e^{-c\beta n}),                         \tag{7}
\]
where \(p_\chi(T)=Z_\chi(T)/\operatorname{Tr}U^T\). In particular, at a size satisfying the strict test the upper limit of each transverse affinity is at most \((1+1650^{-2})/4\). Direction-uniform near independence of full adjoint slices in the measure (35) of row 1155 is therefore incompatible with the desired temporal conclusion.

**PROVED.** Apply (5) to the two slices. Their decoded pair has total variation distance at most \(2Cn^3 e^{-c\beta n}\) from the diagonal pair \((c_j,c_j)\). Separate channels can only increase rectangle affinity, by Cauchy–Schwarz on their fibres. For joint laws at TV distance \(\epsilon\), their independent squares are at TV distance at most \(2\epsilon\), so their square-root densities differ by at most \(2\sqrt{\epsilon}\) in \(L^2\). Taking the inner product with the copy with second coordinates exchanged changes the affinity by at most \(4\sqrt{\epsilon}\). If \(q\) is the law of \(c_j\), the diagonal pair has rectangle affinity \(\sum q^2\), since independent labels must agree for the exchange to preserve its support.

**PROVED.** Write \(\theta_b=Z_b/\sum_c Z_c\). Fourier projection of the temporal twist at the seam gives \(\sum_b\chi(b)\theta_b=p_\chi/p_+\), with \(8\theta_0=1/p_+\). Thus \(\sum q^2=\frac14\sum_{\chi_j=0}(p_\chi/p_+)^2\) by the four-character orthogonality formula. Finally, the purity of a positive density matrix is at most its largest eigenvalue. The vacuum lies in the neutral sector, so \(A_t\le1/\operatorname{Tr}U^T\le p_+\). Bounding a sum of squares by the square of the sum proves (7). The argument concerns the temporal-twist mixture. The true untwisted ensemble fixes the topological label in (5).

**PROVED (what the lost affinity measures).** At a seed with \(A_t\) tending to one along larger dyadic sizes, both decoded bits become uniform in their joint law. The error in reading them at either end of *any* transverse separation tends to zero. In fact the Fourier formula above bounds the sum of their three nontrivial Fourier coefficients by \((1-A_t)/A_t\). Conditioning on these two bits removes this particular obstruction. A purely local estimate on the likelihood of a negative plaquette proves accurate recognition of the bits. It supplies no estimate of their frequency as the examples in row 1155 after (30) show.


## How much of a true slice can its adjoints determine?

**PROVED (failure of pointwise recovery in the Wilson model).** On one time slice take the \(M=n^3/8\) direction-one bonds based at sites with all coordinates even. For each, mark its positive \(12\)-plaquette. Denote the signs of their fundamental traces by \(V=(V_1,\ldots,V_M)\). These are invariant under vertex gauge transformations and flat centre flips. Give a decoder the **entire adjoint spacetime field**, the true values of all unselected fundamental links, and the twist label, if any. There are absolute \(c,C>0\) such that any rule returning at most \(K\) candidates satisfies
\[
 \mathbb P\{V\text{ lies in the list}\}
 \le K e^{-M q(6\beta)},\qquad
 c\sqrt{1+s}\,e^{-s}\le q(s)\le C\sqrt{1+s}\,e^{-s}\quad(s\ge0).    \tag{8}
\]
The probability bound is uniform in the supplied exterior before the selected adjoints are revealed. It holds also for an estimate of the actual fundamental slice modulo gauge and flat flips, since each output slice specifies one sign tuple.

**PROVED.** No plaquette contains two selected links. Conditional on the fundamental exterior, their laws are independent. A unit quaternion \(u\) has density proportional to \(\exp(k\cdot u)\), with \(s=|k|\le6\beta\), including at a twist seam. Knowing its adjoint leaves the pair \(u,-u\). The better guess is the member with \(k\cdot u\ge0\), with any fixed tie rule. Its error probability averaged over the adjoint reading is
\[
 q(s)=
 \frac{\int_{-1}^{0} e^{st}\sqrt{1-t^2}\,dt}
      {\int_{-1}^{1} e^{st}\sqrt{1-t^2}\,dt}.
\]
At \(s=0\) this gives \(1/2\). Exponential tilting in \(t\) makes \(q(s)\) nonincreasing, by the covariance of a decreasing indicator with \(t\). For \(s\ge1\) the numerator is between \(c/s\) and \(1/s\), by restriction to \([-1/(2s),0]\) for the lower bound. In the denominator the substitution \(u=1-t\) and the bound \(\sqrt{u(2-u)}\le\sqrt{2u}\) give the upper bound \(Ce^s s^{-3/2}\) and \(0\le u\le1/s\) gives the matching lower bound. Continuity handles \(s\le1\).

**PROVED.** Each marked trace sign reverses upon flipping its own selected link and is unchanged by the other selected flips. Zero traces are null. Conditional on the exterior and the \(M\) adjoints, the maximum posterior mass of a tuple is the product of the \(M\) individual maxima. The adjoints themselves are conditionally independent. The expectation of this product is \(\prod_e(1-q(|k_e|))\le e^{-M q(6\beta)}\). A list can have at most \(K\) times the maximum posterior mass. Randomizing the rule with independent randomness preserves this bound. This proves (8).

**PROVED (consequence on the trajectory).** If \(\limsup_j\beta_j/\log n<1/2\), then \(M q(6\beta)\to\infty\) at least as a positive power of \(n\). Exact recovery of the actual slice fails with probability tending to one even for \(\log K=o(M q(6\beta))\). This slope condition follows from the one-loop flow **given** the formation, drift and coefficient inputs of Sussman and Alpoge's RF10, RF20, RF23–RF28. At fixed physical side \(x_K=O(1)\), \(\beta=x_K+c_0K+o(K)\), and \(\log n=K\log L_{\rm block}+O(1)\). For SU(2), \(c_0/\log L_{\rm block}=11/(3\pi^2)<1/2\). The finite-cutoff assertion (8) uses no flow hypothesis. [Outline, RF10](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L20348-L20363) · [Outline, RF28](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L20865-L20878)

**PROVED (which information this excludes).** For a deterministic \(S\) among these bonds consider any signed unit-modulus reading \(\sigma\) of a slice that changes by \(-1\) under each individual flip in \(S\), with no condition on its adjoint dependence. Reveal all links other than those in \(S\) and all their adjoints. Given these readings, the magnitude of its posterior mean is the product of the individual lift biases. Averaging over the independent adjoints, and using \(\mathbb E|\mathbb E(\mathrm{sign}\mid\mathrm{adjoint})|=1-2q(|k_e|)\), gives
\[
 |\mathbb E[\sigma(X)G]|\ \le\
        \|G\|_\infty e^{-2|S|q(6\beta)}                                 \tag{9}
\]
for every bounded \(G\) measurable with respect to the revealed data, including every reading of another time slice. These bounds hold for arbitrary time length at fixed spatial cube. By the positive compact transfer's simple vacuum, cylinder expectations on two fixed slices tend to the vacuum Markov expectations as the period tends to infinity. Indeed the normalized transfer powers converge in trace norm to the vacuum projection, by domination by a fixed trace-class power. Thus (9) excludes such a sign from being a slowly changing reading in (4) whenever \(|S|q(6\beta)\to\infty\). A general centre-charged sign is required to be odd only under a *whole flat flip*. That condition does not imply the individual-flip hypotheses on \(S\).

**GUIDE.** Equation (8) concerns recovering the realized field. A local stochastic channel in (34) of row 1155 reproduces a **law**. Its coupled proof can exchange lift fluctuations between paths. Equation (8) explains why replacing that proof by unique determination of the realized slice would fail.


## A one-period test using raw observations

**PROVED, using the centre-quotient recovery estimate of row 1155.** Observe the raw adjoint fields on two complete spatial collars in the temporal-twist mixture at period \(T\). Each collar contains \(h\) steps, and each intervening gap contains \(d=T/2-h\) steps. For definiteness take \(h=\lfloor T/4\rfloor\). A shift by one lattice step to accommodate a central slice has no effect on the argument. Write \(A_{\rm obs}\) for their rectangle affinity. Estimate the twist with the three strips in (6), and put \(u=\mathbb P(\widehat b=0)\) under the same law. At each fixed \(L\), for any fixed \(k\) choose the strip widths large enough. Then
\[
  \frac{1}{Z_+(T)^2 Z_+(2d)^4}\ \le\ A_{\rm obs},\qquad
  \frac{A_{\rm obs}}{8u}\ \le\ \frac{1}{\operatorname{Tr}U^T}
                            +O(n^{-k}).                                  \tag{10}
\]
The lower bound is exact. Both observations on the right-hand test use the single period \(T\). They are raw adjoint data and a finite minimization on three strips.

**PROVED (upper comparison).** Row 1155 recovers, from two short adjoint collars in this mixture, the pair of central slice orbits for \(G\) acting on the spatial gauge quotient. Its TV error is \(O(n^{-2k})\) after increasing the short-collar width. The only part used here is recovery *modulo* the flat flips. To see its mechanism, draw a second twisted path conditionally on each collar's adjoints, independently for the two collars. Each draw marginally has the true mixed law. Move its seam, and the original seam, outside the collars. A relative sign curvature is closed there. A component reaching from a central face to a collar boundary has size at least a constant times the collar radius. A prescribed set of differing faces has at least one negative plaquette per face in one of the paths. Assign the faces to paths and use Cauchy–Schwarz and the preceding tilted bound. Rooted connected-set counting bounds the exceptional probability by \(Cn^4 e^{-c\beta r}\). Outside this event, also excluding components of size \(\ge r/10\) touching the centre by the same bound, every component touching it bounds a dual three-chain in a box strictly inside the collar. Contract that box to a corner and take the prisms of its cells to get a filling. Switch both paths' link signs by these fillings. On their boundary the plaquette weights are exchanged. Everywhere else they are fixed. The choice depends only on the relative curvature, so the switch is a measure-preserving involution. The switched original and the unswitched draw have the same central spatial curvature signs and the same adjoint links. Their remaining sign difference there is a flat flip times a vertex sign gauge. The two collars have disjoint interiors. This proves the required coupling estimate with the full-period conditional channel, which suffices for the inequality.

**PROVED.** Choose the short collars strictly inside the observed ones. The channels can discard the remainder. To identify the exact pair law, write \(K_s\) for the positive symmetric kernel of \(U^s\). Put \(k_s(x,y)=8^{-1}\sum_b K_s(x,by)\). Summing the twist at the seam gives one \(k_{T/2}\) and one \(K_{T/2}\) for the two intervening transfers. Averaging the central representatives on \(G\)-orbits turns both into \(k_{T/2}\). Thus on the quotient the exact pair density is \(k_{T/2}^2/Z_+(T)\). The square root is a positive operator with squared singular values the neutral thermal probabilities. Its rectangle affinity is their squared sum, at most their largest, \(1/Z_+(T)\). Data processing and TV continuity as in (7) give \(A_{\rm obs}\le1/Z_+(T)+O(n^{-k})\). Finally \(1/(8\theta_0)=p_+=Z_+(T)/\operatorname{Tr}U^T\), and \(|u-\theta_0|=O(n^{-k})\) by (6), with \(\theta_0\ge1/8\). This proves the right inequality. No sign readings need be attached to the observed central slices.

**PROVED (lower comparison).** Use two independent stationary fundamental vacuum path segments of length \(h\) as a product reference. Include all the links of the observed segments, using their original conditional laws within the individual transfer steps. Write \(p_d\) for the \(d\)-step vacuum-chain density relative to \(\pi=\psi^2dx\), and \(q_d(x,y)=8^{-1}\sum_b p_d(x,by)\). Call the endpoints of the segments \(x,x'\) and \(y,y'\). In the periodic mixed integral the two missing transfers, after division by \(Z_+(T)\), have factors \(p_d(x',y)q_d(y',x)\). This is the vacuum transform of the two ordinary magnetic sandwiches. Its endpoint vacuum factors cancel against the stationary endpoints. For adjoint observations a centre flip of the entire second segment preserves the reference and the observations. Averaging that flip makes the first factor \(q_d\) as well. Hence the desired observed law is the pushforward of the reference tilted by \(q_d(x',y)q_d(y',x)/Z_+(T)\).

**PROVED.** Put \(v(x,y)=\sqrt{q_d(x,y)}\). The tilted law's affinity to the product reference is
\[
 Z_+(T)^{-1/2}\langle v,(P^h\otimes P^h)v\rangle_{\pi\otimes\pi}
 \ \ge\ Z_+(T)^{-1/2}\left(\int v\,d\pi\,d\pi\right)^2 .
\]
Pair \((x',y)\) with \((x,y')\) using reversibility in the first segment. Positivity of \(P^h\) and its fixed constants give the inequality. Now \(\int q_d=1\) and \(\int q_d^2=Z_+(2d)\) by Hilbert–Schmidt squaring of the projected transfer. Hölder gives \(1=\int q_d\le(\int\sqrt{q_d})^{2/3}(\int q_d^2)^{1/3}\). Under separate observations the product reference remains a product and the affinity can only grow. The affinity to *any* product measure is at most the largest singular value of the square-root joint-density kernel, by the two unit-vector test. Its fourth power is bounded by the rectangle affinity, the sum of the fourth powers of all singular values. This proves (10). This is the neutral mixed-ensemble version of the padding argument in row 1155 (15).

**PROVED (equivalence over admissible sizes).** With the lane's checked propagation of a seed, (W) is equivalent to the existence of one fixed admissible \(L\) at which
\[
              \liminf_j \frac{A_{\rm obs}}{8u}>\frac{1650}{1651}.        \tag{11}
\]
Sufficiency follows from (10) and the shape-two seed. Conversely a seed of row 720 gives, at some dyadic base size, the shape-four inequality \(S(n/4;n^3)<1/25\) with uniform margin below the contraction threshold. This is the two-stage passage from shape two in Theorem SH. Its shape-four recursion makes \(\limsup_j S(n/4;n^3)\) arbitrarily small on further fixed dyadic sides. In (10), \(2d\ge n/4\). Thus both neutral trace factors tend to one in this order of limits. Also \(p_+\ge1/\operatorname{Tr}U^T\to1\), since the full excited sum obeys the same monotonicity in time. For some one of these larger fixed sides (11) holds strictly. The reverse implication can change the physical side. It does not claim an equality at a prespecified side. The raw-collar lower bound and the obstruction (7) therefore concern different orientations in the very same law. [Shape propagation, including the lead's corrections](gap-seed-shape.md) · [Row 720](gap-phys-seed.md)


## What a single unbuffered plane reads

**PROVED (the bare plane-sign test loses the twist bit).** Let \(\Pi\) be a coordinate \(i\)-time two-torus at fixed transverse coordinates in the same mixed measure. The most direct estimator from the plane alone is
\[
       C_\Pi=\prod_{p\in\Pi}\operatorname{sgn} w_p(\widetilde U),
\]
where \(\widetilde U\) are arbitrary lifts of its adjoint links. Each link appears twice, so the product is lift-independent. It equals \((-1)^{b_i}\prod_{p\in\Pi}\operatorname{sgn}w_p^b(U)\) for the true twisted path. For some \(c,C>0\), and all large \(\beta,n\),
\[
 \big|\mathbb E[C_\Pi H]\big|
 \le \|H\|_\infty\{C e^{-c\beta n^2}
                   +\exp[-c n^2 e^{-4\beta}]\} .                       \tag{12}
\]
Here \(H\) may depend on the twist label and on **all fundamental links** except the boundary links of a specified collection of disjoint plaquettes in \(\Pi\), as described below. In particular on \(\limsup\beta/\log n<1/2\) the bare plane sign guesses the true bit with probability tending to \(1/2\), irrespective of its class probabilities. This addresses this particular estimator. It does not rule out other functions of a single plane.

**PROVED (finite local change).** Choose \(m\ge c n^2\) central plaquettes at spacing at least five in each direction of \(\Pi\). One can use every sixth row and column outside a six-row and six-column seam margin. Call the four boundary links of each chosen plaquette a block. Every plaquette affected by the block contains exactly one of its links, except for the central plaquette, which contains four. There are twenty other affected plaquettes. The sets of affected plaquettes of different blocks are disjoint, and no plaquette couples the blocks. Given the twist and all other links, the four-link integrations factor.

**PROVED.** Call a block good for an exterior if a completion puts all 21 affected, twist-adjusted plaquette holonomies within a small geodesic distance \(\epsilon\) of the identity. For such an exterior choose one such completion for the argument. The twist cochain is exact in the contractible neighbourhood of the block, so a fixed change of local link lifts removes the boundary signs in this argument. Gauge transformations put three successive links around the central plaquette at the identity, leaving the fourth within \(\epsilon\) of the identity in the positive traversal convention. Insert a rotation of angle \(\theta=\pi/7\) about a common axis on all four links in that convention. The new central holonomy lies within \(\epsilon\) of the rotation of angle \(4\theta\) by bi-invariance. Every other affected holonomy lies within angle \(\theta+\epsilon\) of the identity, since only one link was changed. Consequently exactly the central trace has become negative. The action summed over these faces is bounded, at zero error, by
\[
    1-\cos(4\theta)+20(1-\cos\theta)<4 .
\]
Indeed \(4\theta=\pi/2+\pi/14\), \(\sin(\pi/14)<1/4\), and \(\theta<1/2\). The latter bounds the second term by \(20\theta^2/2<5/2\). The strict margin permits fixed positive \(\epsilon\) and a fixed positive ball radius on each of the four links. In these product balls both the sign pattern and the upper bound 4 persist. The corresponding four balls about the initial completion have all traces positive and action below 4. Their product Haar volumes have a common positive lower bound. The block conditional denominator with the action \(1-w^b\) is at most one, after cancelling all exterior factors. Thus either parity of the affected plane faces has conditional probability at least \(c e^{-4\beta}\).

**PROVED.** If \(\ell\) specified blocks are bad for their exterior, every realized completion has an affected face in each with \(1-w_p^b\ge 1-\cos\epsilon\). The exponential-moment argument preceding (5) applies with this fixed threshold. Choose one of 21 faces in each block. Their distinctness gives total mixed probability at most \(8(C_\epsilon e^{-c_\epsilon\beta})^\ell\). A union over at most \(2^m\) subsets bounds the probability that at least half the blocks are bad by \(C e^{-c'\beta m}\). On the remaining exteriors the conditional mean of the total plane parity has absolute value at most \((1-2ce^{-4\beta})^{m/2}\), by the product of the conditional block biases. The class sign is exterior-measurable. Integrating proves (12). This uses a hand construction in a fixed block, with no count of configurations by machine.

**PROVED (comparison with the corrected reading).** Equations (6) and (12) use the same bare coupling and the same path law. The direct two-torus product loses its information even with a perfect prediction of the true class supplied as the test \(H\). A bounded-width correction in a transverse direction reads the bit with vanishing error when \(\liminf\beta/\log n>0\). Thus approximating the unknown class frequency \(u\) in (11) by unbiased signs from uncorrected planes would artificially predict equidistribution.


## All plane signs together, and the neutral spectrum

**PROVED (simultaneous estimate).** Let \(S\) be any deterministic set of distinct plaquettes. Greedily pick centres in \(S\) with disjoint affected face sets and no face coupling different four-link blocks. Each choice forbids only an absolute number of other choices in the four-dimensional cubical lattice. Hence at least \(c|S|\) centres can be kept. The two sign patterns constructed above differ **only at their central plaquette** among all affected faces. Therefore the proof of (12) gives
\[
 \left|\mathbb E\left[H\prod_{p\in S}\operatorname{sgn} w_p^b\right]\right|
 \le \|H\|_\infty\{C e^{-c\beta |S|}+e^{-c |S| e^{-4\beta}}\},        \tag{13}
\]
for any test measurable off the chosen blocks, including a function of \(b\). This argument applies to the untwisted cylinder with constants uniform in its time length (at least four), since its tilted bounds need no division by a twist weight. It applies to the mixed cylinders at the two physical periods as above.

**PROVED (all coordinate two-tori are simultaneously blind).** Let \(B\) be the vector of bare plane signs \(C_\Pi\) for *every* coordinate two-torus in all six orientations, on the physical \(n^3\times T\) torus. Let \(m\le6n^2\) count these planes. Then
\[
 \|\mathcal L(B,b)-\mathrm{Unif}(\{\pm1\}^m)\otimes\mathcal L(b)\|_{\rm TV}
 \le C\{(1+e^{-c n^2e^{-4\beta}})^m-1\}.                              \tag{14}
\]
For any \(k\) distinct planes, the corresponding face sets are disjoint even when the geometric planes intersect along edges. Their union has size at least \(kn^2/2\). Their joint sign differs from the product of the true face signs by a function of \(b\) of modulus one. Apply (13) with a test of \(b\) chosen to take the sign of each conditional Fourier coefficient. The sum over \(b\) of the absolute joint coefficients is at most \(C e^{-c k n^2e^{-4\beta}}\). Inverting the Walsh expansion and summing its nonconstant terms gives (14) by the binomial formula. Along every slope strictly below \(1/2\) the right side tends to zero. Even optimal postprocessing of **all** the unbuffered plane products can do no better at identifying the class than the best constant guess, up to a vanishing error. Equation (6) uses the additional adjoint face information *between* planes. The subcase of planes at fixed transverse coordinates in (12) alone would not justify (14).

**PROVED (a whole algebra excluded from the physical low levels).** On a single spatial slice let \(B_x\) consist of the \(3n\) signs of its coordinate two-tori. They are functions of the spatial adjoints alone and belong to the neutral sector. Let \(\nu\) be the uniform bit law. For the stationary Wilson vacuum pair \((X,Y)\) one ordinary time step apart, the joint density of \((B_X,B_Y)\) relative to \(\nu\otimes\nu\) lies between \(1-\epsilon_j\) and \(1+\epsilon_j\), where
\[
 \epsilon_j=C\{(1+e^{-c n^2e^{-4\beta}})^{6n}-1\}.                    \tag{15}
\]
Indeed for the \(6n\) plane bits on the two indicated slices, any \(k\)-fold product selects at least \(kn^2\) different faces. At different time slices these are different spatial faces. Apply (13) in the untwisted cylinder uniformly in its length. Walsh inversion bounds the *relative pointwise* likelihood error by the sum of the bounds on its nonconstant coefficients. Pass to the vacuum pair at fixed spatial size as for (9). This proves (15) even for readings supported on rare bit strings.

**PROVED.** For every \(\nu\)-mean-zero function \(f\) of the \(3n\) bits, put \(v(X)=f(B_X)\) in \(L^2(\pi)\). For the transfer energy in lattice units \(\mathcal H=-\log P\) on its positive spectrum,
\[
       \frac{\|\mathbf1_{[0,E]}(\mathcal H)v\|_\pi^2}{\|v\|_\pi^2}
         \le \frac{e^E\epsilon_j}{1-\epsilon_j}.                        \tag{16}
\]
By (15) in \(\langle v,Pv\rangle\), the independent term vanishes and the error is at most \(\epsilon_j\|f\|_{L^1(\nu)}^2\). Its one-slice consequence gives \(\|v\|_\pi^2\ge(1-\epsilon_j)\|f\|_{L^2(\nu)}^2\). Finally \(\mathbf1_{[0,E]}(\mathcal H)\le e^E P\). The quotient is for nonzero \(f\), and conjugation by \(\psi\) gives the corresponding statement on the original slice Hilbert space. If \(\limsup\beta/\log n<1/2\), one may take \(E=c' n^2e^{-4\beta}\to\infty\) with \(c'>0\) sufficiently small. Thus the entire nonconstant bare-plane algebra has uniformly vanishing overlap with these low levels. Row 1145 (4) gave a related exclusion for straight, sparsely blocked fundamental holonomies. Here every spatial plane is kept, with all nonlinear functions of their adjoint signs. The open neutral count comes from other readings.


## Integrating the sign sum in (35) at fixed physical size

**GUIDE.** The next route attacks the measure in (11) itself. It uses Mack–Petkova's centre decomposition in row 1155 (35). The aim is a density on adjoint links with bounded-range factors, allowing the three global magnetic constraints that the problem actually imposes. The errors below compare normalized measures in total variation.

**PROVED (localization of possible sign defects).** Work on either physical period with \(\beta/\log n\ge\kappa>0\) eventually. Fix \(k>0\). For the adjoint field \(v\), put \(\alpha_p=|w_p|\). Choose arbitrary link lifts, let \(D\) be their negative-face set and put \(M=dD\) on elementary three-cubes. The syndrome \(M\) and the magnitudes are gauge and lift invariant. Use the face graph in which faces of a common three-cube are adjacent. Choose \(0<a<1\), fixed. Mark every face with \(\alpha_p<a\), and every face incident to a cube with \(M=1\). For the true negative set \(\xi\), \(d\xi=M\). Under the mixed measure, outside probability \(O(n^{-k})\), both of the following hold with constants independent of the cutoff.

1. Every connected component of \(\xi\) has at most \(R\) faces.
2. For any further *fixed* integer \(D_1\), connect marks at graph distance at most \(D_1\). Every component of marks then has at most \(B\) marks.

**PROVED.** A specified connected set of \(l\) negative faces has probability at most \(8(Ce^{-c\beta})^l\) by the tilted estimate. Sum over its at most \(Cn^4 C_0^l\) rooted supports and choose \(R\) sufficiently large relative to \((k+4)/\kappa\). To prove the second assertion, each marked face witnesses an affected face in its bounded neighbourhood with \(1-w_p^b\ge1-a\). Indeed a cube with \(d\xi=1\) has a negative face. For \(l\) prescribed marks choose one witness per mark in at most \(C_1^l\) ways. Any witness can be chosen at most a bounded number \(d_0\) of times, so there are at least \(l/d_0\) distinct expensive faces. The tilted estimate at threshold \(1-a\) bounds the probability by \(8(C_a e^{-c_a\beta})^l\), with changed constants. The graph with range \(D_1\) has finite degree independent of \(n\), so the same connected-set sum gives \(B\). The order of choice is \(R\), any required \(D_1\), then \(B\). Thus the geometric restriction on \(v\) can be tested locally because a forbidden component contains a connected set of \(B+1\) marks of bounded diameter.

**PROVED.** For good \(v\) split a configuration with components of size at most \(R\) into components that meet a mark and those that do not. Call their unions \(\zeta\) and \(\eta\), respectively. Every component of \(\eta\) is closed. At any cube with \(M=1\) all faces are marked. At the other cubes the parity is even, and different components cannot supply faces to the same cube. Thus \(d\zeta=M\). Each component of \(\eta\) is a compact dual two-cycle in a box of bounded diameter and is exact on the full lattice by the cubical contraction used in (10). Its Boltzmann activity is
\[
                         z_\gamma=\exp[-2\beta\sum_{p\in\gamma}\alpha_p].
\]
It is bounded by \(e^{-2a\beta|\gamma|}\). Two such components are incompatible precisely when they intersect or touch in the face graph. They must also avoid the marks and the closed one-neighbourhood of \(\zeta\).

**PROVED (an especially simple physical-slope form).** Suppose \(\liminf\beta/\log n>1/3\). Choose \(a<1\) with \(12a\liminf\beta/\log n>4\). Then with probability \(1-o(1)\) every component of \(\xi\) meets a mark. In fact a nonempty bounded closed component has at least six faces. In its dual two-cycle pick a face in directions \(i,j\). Projection of the cycle to the \(ij\)-plane is a finite mod-two two-cycle there and vanishes because the boundary equation makes the coefficient constant across each edge. Thus a second parallel face projects to the same square and is disjoint from the first. The four edges of the first each require another incident face, and no other unit square can share two of these edges. This gives six. In the conditional sign sum at fixed \(v\), erasing any specified bounded clean component preserves the allowed class and is an injection with weight ratio \(z_\gamma\). Its event probability is at most \(z_\gamma\), even before truncation of other components. Summing the rooted supports gives \(C n^4 e^{-12a\beta}\) for bounded clean components, and components larger than \(R\) cost \(O(n^{-k})\) in the joint law. On the account's conditional one-loop slope \(11/(3\pi^2)>1/3\), since \(\pi^2<11\). In this regime one may discard *all* the clean components at vanishing absolute probability. The contribution of the marked regions still has to be integrated.


**PROVED (finite sums on the marked regions).** First use the \(o(1)\) version just proved. Take \(D_1>4R+10\). For a mark component \(C\) form the \(R\)-neighbourhood \(V_C\) in the face graph. The \(V_C\)'s are separated by more than two face steps. In \(V_C\) list all face sets \(\zeta_C\) such that every component meets \(C\), has size at most \(R\), and has, *in total*, the prescribed coboundary on cubes incident to \(V_C\). The prescribed value is \(M\) there, including zero on boundary cubes. Equivalently extend the set by zero and use its coboundary on the whole torus, with the nonzero syndrome cubes assigned to this component. Every such cube belongs to just one component because all its faces are marks. Write \(\mathcal D_C\) for this finite list. The lists define finite sums analytically. Distinct choices of \(\zeta_C\) differ by a closed cochain supported in a bounded box of the torus. Lifting this cochain to the dual lattice in a slightly enlarged box shows it is exact. Thus, if all lists are nonempty, the class
\[
       b(v)=[D+\textstyle\sum_C\zeta_C]\in H^2(\mathbb T^4;\mathbb F_2)
\]
is independent of the choices. Empty lists give zero density. All these boxes have uniformly bounded size since \(C\) uses at most \(B\) marks joined by \(D_1\)-steps, and \(R,D_1,B\) were fixed first.

**PROVED.** In the restricted integral, the density relative to product \(SO(3)\) Haar is proportional to
\[
 {\bf1}_{\,b(v)_{\rm spatial}=0}\ e^{\beta\sum_p\alpha_p}
 \ {\bf1}_{\,\text{mark bound}}\
 \prod_C \left(\sum_{\zeta_C\in\mathcal D_C}
              e^{-2\beta\sum_{p\in\zeta_C}\alpha_p}\right).              \tag{17}
\]
Use zero when a list is empty, before evaluating the class indicator. Indeed the allowed negative sets in (35) have \(d\xi=M\) and \([\xi+D]_{\rm spatial}=0\), and the number of sign-link preimages is constant. With the stated restrictions, all configurations are exactly the independent choices in the lists. The temporal component of \(b(v)\) is the true twist. The discarded joint probability is \(O(n^{-k}+n^4e^{-12a\beta})\). Conditioning away that event changes the joint law by its probability in TV, and pushing forward to \(v\) cannot increase it. This proves (17) to \(o(1)\) in the stated slope regime, at *both* periods with the same rules. Aside from the three spatial periods, (17) has only local factors of bounded range. For example distribute each positive region factor to its marks by its \(|C|\)-th root. A mark can determine the region and test the bound inside a fixed ball. A violation has a bounded local certificate. Only the magnetic class requires a global restriction.

**PROVED (arbitrary inverse powers, and smaller positive slopes).** For every fixed \(\kappa>0\), \(k>0\) and \(\beta\ge\kappa\log n\), (17) can be modified by explicit bounded-range positive weight factors to give TV error \(O(n^{-k})\). No assumption \(12a\kappa>4\) is needed. Keep all clean components of size at most \(R\), with \(R\) chosen for this \(k\). There are at most \(C_R n^4\) possible closed connected sets \(\gamma\) of these sizes. Their incompatibility graph has degree at most \(D_R<\infty\), since each occupies at most \(R\) faces of bounded degree. Assign activity zero to sets meeting a mark, and otherwise \(z_\gamma\) as above. After choosing \(\zeta\), assign activity zero also to sets meeting or touching it. This last rule separates clean components from the others. All activities are now in \([0,z]\) for \(z=e^{-2a\beta}\). The clean sum is the hard-core partition function \(\mathcal Z\) on this list. It includes the empty family. All its components are exact, so imposing the spatial class restricts only the marked lists.

**PROVED (local formula for its logarithm).** On any induced list \(\Lambda\) and \(i\in\Lambda\) define
\[
 r_i(\Lambda)=z_i\frac{\mathcal Z(\Lambda\setminus N[i])}
                         {\mathcal Z(\Lambda\setminus\{i\})},
\]
where \(N[i]\) includes \(i\) and its incompatible neighbours. Splitting an independent set according to membership of \(i\) gives \(\mathcal Z(\Lambda)/\mathcal Z(\Lambda\setminus\{i\})=1+r_i(\Lambda)\) and \(0\le r_i\le z\). Remove the neighbours in any fixed order from \(\Lambda\setminus\{i\}\). Telescoping the corresponding ratios writes \(r_i=z_i\prod_j(1+r_j(\Lambda_j))^{-1}\), where \(\Lambda_j\) is the remaining list before removing neighbour \(j\). The map on the child values has each partial derivative bounded in absolute value by \(z\) on the nonnegative cube. Replace values at depth \(l\) by zero. By induction the root error is at most \(z(D_R z)^l\). Sum \(\log(1+r_i)\) along successive removals of the complete ordered list. Each logarithm is one-Lipschitz for nonnegative arguments. The truncated sum, denoted \(\mathscr L(z_\bullet)\), satisfies
\[
          |\log\mathcal Z-\mathscr L(z_\bullet)|
                       \le C_R n^4 z(D_R z)^l .                          \tag{18}
\]
Choose a fixed \(l\) so \(2a\kappa(l+1)>k+4\). The right side is \(O(n^{-k})\). Every term then reads only the graph within \(l\) incompatibility steps, including the order comparisons there. One can average this finite expression over independent uniform continuous priorities on the fixed list to remove the choice of ordering. The comparisons have the same distribution in every isometric neighbourhood and (18) is uniform in the order. This proves the approximation by hand without using a convergence test on computed activities.

**PROVED (summing over the near configurations).** Each summand of \(\mathscr L\) depends on the face data and exclusions in a ball of radius at most \(d_*=4(l+3)(R+3)\) in the face graph, since intersecting or touching sets of at most \(R\) faces extend a path by at most \(2R+1\) per step. Call \(\mathscr L_0\) the sum with marks excluded but no \(\zeta\) exclusions. Now take \(D_1>4(d_*+R+3)\) before choosing \(B\). Turning off activities for contacts with \(\zeta\) changes each summand through at most one region \(C\). Therefore
\[
       \mathscr L(z_\bullet(\zeta))
          =\mathscr L_0(v)+\sum_C L_C(v,\zeta_C),
\]
where \(L_C\) is the summed local change obtained by introducing just the exclusions of \(\zeta_C\). Every term changed lies a bounded distance from that region. In (17) multiply the common density by \(e^{\mathscr L_0(v)}\) and the summand for \(\zeta_C\) by \(e^{L_C(v,\zeta_C)}\). This is the promised bounded-range formula. All weights are nonnegative. At fixed \(v,\zeta\) (18) changes the clean sum by a factor between \(e^{-\epsilon_n}\) and \(e^{\epsilon_n}\), \(\epsilon_n=O(n^{-k})\). Positive summation and normalization change the restricted joint-law density by at most factors \(e^{\pm2\epsilon_n}\). The true restrictions on large components and marks cost \(O(n^{-k})\) by the earlier joint bound. This proves the TV assertion, also jointly with the temporal twist, since it is \(b(v)_{\rm temporal}\) on the retained configurations. All radii are fixed in lattice units before the cutoff limit. Equations (17)–(18) replace the extensive constrained sign sum of (35). The continuous adjoint Haar integrations still have their original spatial and temporal extent.


## A periodic adjoint model and a bounded-cost conditioning

**GUIDE.** Use the six 't Hooft twist bits \(b=(m,e)\), three magnetic and three temporal. The comparison \(Z_{m,e}\le Z_{0,0}\) is already (S2) of the flux exercise. Its proof removes the temporal flips in each successive frame by positivity of the transfer with the remaining static magnetic action. The Fourier components in a fixed magnetic sector are nonnegative traces. These facts also hold on a rectangular torus. [Sector order, section 5](gap-flux-exercise-check.md)

**PROVED (conditioning cost).** Put \(H_m=\sum_e Z_{m,e}\). Then
\[
       H_m\le H_0,\qquad \frac{H_0}{\sum_{m'}H_{m'}}\ge\frac18,
       \qquad \frac{Z_{0,0}}{\sum_{m',e'}Z_{m',e'}}\ge\frac1{64}.       \tag{19}
\]
For the first inequality choose a spatial direction \(i\) as time and fix the two \(e_j,\ j\ne i\). They are static twists in that frame. Sum over \(e_i\) at the seam, which inserts twice the orthogonal projection onto the even sector of the flip in the old time direction. The remaining seam contains the involutions for magnetic components \(b_{ij}\), \(j\le3,\ j\ne i\). They commute with that projection and the positive static transfer. In their simultaneous decomposition dropping them increases the trace, as each eigenvalue of their product is \(+1\) or \(-1\). This zeros all magnetic components incident to \(i\) and retains the sum over \(e_i\). Restore the two other sums and repeat in the spatial directions until no magnetic component remains. This proves the first inequality, and summation gives the second. The third follows directly from (S2).

**PROVED.** Allow all 64 twists, with their partition weights. For specified faces of one orientation, choose a time direction in the plane of that orientation. With the other twist bits static, the electric convolution comparison in the proof of (5) and trace Hölder remove the seam and bound the tilted integral by \(C^k Z_{m',0}\) for \(k\) reduced couplings in this frame. Here \(m'\) denotes all its static bits. Apply (S2) and ordinary Hölder over the six orientations. The denominator of the full mixture is at least \(Z_{0,0}\). This proves the same exponential suppression of expensive faces, with 64 in place of 8. It also proves (5) and (6) on any chosen slice or strip for the components of the now unrestricted twist that pair with its two-tori.

**PROVED (only bounded-range weights before observation).** In (17) remove the spatial indicator and keep the local validity and marked-region factors. Use the correction (18) for inverse-power accuracy if needed. This defines a probability \(\mathbb Q\) on periodic adjoint links alone after normalization. Denote the cohomology read from its finite lists by \((m(v),e(v))\). To check the density, at fixed \(v\) and fixed true face set \(\xi\) with \(d\xi=M\), exactly one class \(b=[D+\xi]\) permits \(\xi\). The number of link-sign configurations realizing it is the size of the kernel of the link coboundary, the same for every \(\xi,v,b\). The two localization arguments for (17)–(18) now apply with the full-mixture bound above. Thus \(\mathbb Q\) and its six readings approximate the entire Wilson adjoint and twist law with the stated TV errors. No global constraint enters its density. Conditioning on \(m(v)=0\) recovers the original joint law up to the same order of error by (19). For an event of mass \(p>0\), TV error \(\delta<p/2\) enlarges by at most \(2\delta/p\) on conditioning. Each magnetic bit can equally be read with (5) on one fixed old-time spatial slice. In that three-torus the \(n\) disjoint parallel two-tori give the same distance estimate for each of the three bits.

**PROVED (test for this local model).** Let \(\mathcal A_{\mathbb Q}(\,\cdot\mid m=0)\) be the rectangle affinity of the two temporal adjoint collars in (10), under the indicated conditioning. With the same ordered limits and existence of an admissible size as in (11), (W) is equivalent to
\[
  \liminf_j
  \mathcal A_{\mathbb Q}(\text{two collars}\mid m=0)\,
    \frac{\mathbb Q(m=0)}{8\,\mathbb Q(m=0,e=0)}
            >\frac{1650}{1651}.                                           \tag{20}
\]
Indeed (19) controls both denominators, and the square-root continuity used in (7) passes the affinity to the limit. This puts all observables in one model at one period. The normalization of that model cancels from the twist ratio.


## What finite range and small defect density give on this trajectory

**PROVED (a diverging number of nonzero cube parities).** In either Wilson twist mixture on the physical torus there are constants \(c_i>0\) such that
\[
 \mathbb P\!\left\{\#\{q:M_q=1\}<c_1 n^4e^{-4\beta}\right\}
       \le c_2 e^{-c_3\beta n^4}+\exp[-c_4 n^4e^{-4\beta}] .            \tag{21}
\]
Choose \(m_*\ge c n^4\) spaced four-link blocks as in (12) in all four directions, each with a designated three-cube adjacent to its central plaquette. Space the blocks so distinct designated cubes see no links from each other's blocks. Fix the twist and the exterior links. Each good block has two sets of completions of conditional mass at least \(q_*=ce^{-4\beta}\) whose true sign patterns on its affected faces differ just at the central face. Therefore the cube parity is one on at least one of these two sets, whatever the other face signs in that cube. It equals the adjoint syndrome since the twist cochain is closed. The designated parities are independent conditional on the exterior and twist. Except on \(C e^{-c'\beta m_*}\), at least half the blocks are good by the bad-block estimate used in (12). For \(M_*\ge m_*/2\) independent indicators each of mean at least \(q_*\), the exponential Markov bound for \(e^{-\sum I}\) gives probability at most \(\exp[-(1-e^{-1}-1/2)M_*q_*]\) of at most \(M_*q_*/2\) successes. This proves (21). On \(\limsup\beta/\log n<1\), replacing the local model by a measure supported on \(M=0\) costs TV tending to one. The same conclusion holds for dropping all marked regions. A vanishing *fraction* of affected cubes is consistent with (21).

**PROVED (single-link total-variation influence).** In the simple adjoint density (17) without the spatial indicator, let \(c_{\ell j}\) be the supremum TV distance between conditional laws at an adjoint link \(\ell\) for exteriors differing only at \(j\). The same assertion holds with the spatial indicator. Along \(\beta\to\infty\) on the slopes of (17), for each \(j\ne\ell\) on a common plaquette,
\[
                          c_{\ell j}\longrightarrow 1 .                 \tag{22}
\]
Take first the identity exterior. In the second exterior change that one neighbour to the class of a fixed \(v=\exp(Ih)\) for a small \(h>0\) and a unit imaginary quaternion \(I\). Up to changing \(I\) to \(-I\), the exponents at \(u\) representing the target link are \(\beta\,6|u\cdot 1|\) and \(\beta(5|u\cdot1|+|u\cdot v|)\), plus constants. On \(S^3/\{\pm1\}\) the respective unique maxima are \([1]\) and \([(5\cdot1+v)/|5\cdot1+v|]\). Indeed the second maximum is the greater of \(|5\cdot1+v|\) and \(|5\cdot1-v|\), by maximizing over signs first. The two maxima are distinct. At small fixed \(h\) all plaquettes near both respective maxima have positive representative traces and magnitude above \(a\). There are no marks and the class is zero there. For arbitrary \(u\) only a fixed number of nearby marks are possible in these exteriors. The other factors in (17) are bounded above by a constant independent of \(\beta,n\), since there are boundedly many local choices, each of weight at most one. At each maximum these factors are exactly one on a neighbourhood. Compactness and integration on a still smaller positive-volume neighbourhood show exponential concentration in disjoint balls about the two maxima. The same bounds with a smaller exponent hold for small open perturbations of the exteriors, with the two comparisons sharing their other links. This supplies witnesses also for the essential supremum. Thus (22) holds, and already two distinct neighbours exclude a Dobrushin row sum below one. This obstruction is to a uniform one-link TV estimate on the adjoint links. Block estimates or estimates on gauge-invariant observations have different hypotheses.


## Can one transverse magnetic reading control every twist weight?

**GUIDE.** The earlier flux exercise gives Fourier positivity in each choice of time and the order (S2). The earlier Pfaffian exercise compares a signed sum on the six bits. Here the input is the *ordinary probability of a zero restriction* on one coordinate three-torus, in the positive all-twist mixture. No assertion about the sign of the six-dimensional Fourier transform is needed. [Flux exercise, section 8](gap-flux-exercise.md) · [Pfaffian comparison](gap-kappa-order.md)

**PROVED (one transverse statistic on a spatially cubic box).** Put \(f(B)=Z_B/Z_0\) and \(\theta(B)=f(B)/\sum f\) for \(B\) on the six edges of the complete graph of the four coordinate axes. In direction \(i\) the three incident edges form the temporal star and its complement \(C_i\) is the triangle of static components. Write \(p_i(c)=\theta(B|_{C_i}=c)\). On any rectangular torus let \(\delta=\max_{1\le i\le3}(8p_i(0)-1)\). On the spatially cubic torus any one spatial direction gives this maximum. At every cutoff,
\[
     0\le 1-\min_B f(B)\le 256\,\delta .                               \tag{23}
\]
Conversely if all \(f\ge1-r\), \(0\le r<1\), then \(0\le\delta\le r/(1-r)\). Thus the null-class probability on just one transverse three-torus controls even the crossed twists on a spatially cubic box. The zero here means zero on all three two-tori *in that slice*.

**PROVED.** By (19) in each frame, \(p_i(c)\le p_i(0)\). For any nontrivial character supported in one of the three triangles \(C_i,\ i\le3\), its mean under \(\theta\) has magnitude at most \(\delta\). Indeed, subtract the marginal from the constant array \((1+\delta)/8\), whose excess is nonnegative with sum \(\delta\). Fix any axis \(j\). In the star variables \(t\), at fixed complementary \(c\), the Fourier coefficient
\[
                 h_{j,c}(\eta)=\tfrac18\sum_t f(c,t)(-1)^{\eta\cdot t}
\]
is nonnegative by the transfer projector in that frame. Its sum over \(c\) is the six-bit character mean multiplied by \(\sum f/8\le8\). Thus if the nonempty support of \(\eta\) also lies in a tested triangle then \(0\le h_{j,c}(\eta)\le8\delta\) for **every** \(c\). This is the use of positivity that prevents different complementary classes from cancelling each other.

**PROVED.** Toggling two edges incident to axis \(4\) changes \(f\) by at most \(64\delta\). Indeed exactly four characters on that star change sign. Each selects exactly one of the toggled edges and possibly the third, so its support is contained in a triangle omitting a spatial axis. Inversion gives \(2\cdot4\cdot8\delta\). Toggling two *spatial* edges meeting at a spatial axis \(i\) has the same bound. Each affected character selects just one of these two and possibly \(i4\), so again its support is in a tested triangle. Any two configurations having the same two parities, the sum of their three spatial edges and the sum of their three temporal edges modulo two, can be joined by at most one toggle of each kind. Their \(f\)-values differ by at most \(128\delta\).

**PROVED.** Fix the two parities of an arbitrary \(B\). On \(C_1\) alone one can realize them by a configuration \(c\), since that triangle contains a spatial edge and a temporal edge. From \(c\) the star at 1 can adjust both parities to even independently. For the resulting \(c+t\), \(f(c+t)\ge f(0)-128\delta\). By the trace order in that star \(f(c)\ge f(c+t)\). Replacing \(c\) by \(B\) costs at most \(128\delta\) once more. This proves (23). The converse follows by bounding the mass of eight classes above by \(8\) and the sum of all weights below by \(64(1-r)\). On each transverse slice the minimum-area reading (5) estimates all three restricted periods, with distance at least the shortest side of that slice for each nonzero period. Its probability of a zero reading therefore differs from \(p_i(0)\) by \(O(n^3e^{-c\beta n})\) on the physical rectangles. This also holds in the local model up to its TV error.


## What a periodic seed would imply for crossed twists

**GUIDE.** The earlier Remark 2.A(d) describes the eight nearly degenerate magnetic vacua in a confining phase as a physical expectation. Here the hypothesis is just the untwisted thermal seed (W). Doubling the time in *each static magnetic sector* supplies the estimate on the crossed twists. [Remark 2.A](gap-crux-fp.md) · [Twisted transfer and vacuum](gap-transfer-twisted.md)

**PROVED (finite-box comparison).** Fix a spatial box, a time \(q\) and the torus at time \(2q\). Suppose on **both** tori the untwisted excited thermal sums are at most \(\eta<1/20\) in every coordinate time frame. Set \(X_m=\operatorname{Tr}(F_m/\lambda_0)^q\), \(a_m=(\lambda_m/\lambda_0)^q\), with \(\lambda_m=\|F_m\|\). Then
\[
 a_m\ge\frac{1-4\eta}{1+\eta},\qquad
 0\le X_m-a_m\le6\eta,\qquad
       1-12\eta\le Z_{m,e}(q)/Z_{0,0}(q)\le1 .                         \tag{24}
\]
In any frame a twist supported on its star has \(f\ge1-2\eta\). The unique untwisted vacuum contributes \(+1\) after vacuum normalization and the remaining trace is at most \(\eta\). An untwisted-time magnetic configuration uses at most the three edges of a triangle. Any proper subset is supported on a star. For the full triangle choose a vertex and let \(c\) be the opposite edge and \(t_1,t_2\) its two star edges. Positive Fourier coefficients on that star and \(1-xy\le(1-x)+(1-y)\) for signs imply
\[
       f(c+t_1+t_2)\ge f(c+t_1)+f(c+t_2)-f(c)\ge1-4\eta .
\]
Thus at \(q\) and \(2q\) the all-magnetic, zero-electric ratio is at least \(1-4\eta\). Its upper bound is (S2). The untwisted trace divided by \(\lambda_0^q\) is in \([1,1+\eta]\), with the corresponding statement at \(2q\). Hence
\[
 1-4\eta\le\operatorname{Tr}(F_m/\lambda_0)^{2q}
           \le a_m X_m,\qquad X_m\le1+\eta .
\]
This gives the first two estimates of (24). The positive top eigenvector of \(F_m\) is invariant under all commuting centre flips by simplicity. Therefore \(Z_{m,e}(q)/\lambda_0^q\ge2a_m-X_m\). Dividing by the untwisted trace gives the lower bound \(2(1-4\eta)/(1+\eta)^2-1\ge1-12\eta\). This also shows \(\operatorname{Tr}(F_m/\lambda_m)^q\le(1+\eta)^2/(1-4\eta)\) in every magnetic sector.

**PROVED (the shapes needed in the implication).** Under (W), take successively larger fixed dyadic physical sides and then the limit in cutoff at each side. Equivalently all vanishing assertions here mean that their cutoff limsups tend to zero as the dyadic side increases. We can arrange \(8\mid n\) on these enlarged sides. Put \(b=n/4\) and \(\tau=b/2\). By the two-stage shape bootstrap used in (11), \(s=S(\tau;b^3)\) has arbitrarily small cutoff limsup along these sides. For every spatial rectangle \(H\) with its sides in \([b,4b]\), Proposition B3 with reference cube \(b^3\), \(p=q'=1\), gives \(1+S(\tau;H)\le(1+s)^{512}\) because each enlargement factor is at most \(4b/(b-\tau)=8\). All time lengths used at \(q=n/4,n/2\) and at their doubles are at least \(\tau\) in every rotated frame. The untwisted excited sums on them are therefore bounded by \(\eta=(1+s)^{512}-1\). Apply (24) with this \(\eta\) once it is small. On the physical torus \(n^3\times(n/2)\) all 64 twist ratios tend to one in the indicated limits. The eight magnetic top states each have relative weight tending to one, and the sum of all other weights tends to zero for each \(q=n/4,n/2\), in units \(\lambda_0^q\). In particular the zero reading on a transverse slice tends to \(1/8\). This conclusion includes twists with nonzero Pfaffian.


## A test with no conditioning and no ratio of partition functions

**PROVED.** In the single all-twist adjoint model of (19)–(20) let \(\mathcal A\) be the rectangle affinity of the two **unconditioned** temporal collars in (10). Let \(s_\perp\) be the probability of a zero three-bit minimum-area reading on one slice perpendicular to a spatial axis. Both are raw measurements in that one model on \(n^3\times(n/2)\). On the logarithmic trajectories in (18), (W) is equivalent, over admissible fixed physical sides, to the existence of such a side with
\[
 \limsup_j\left(64\,|\mathcal A-1/8|
                    +4352\,(8s_\perp-1)_+\right)<\frac1{1651}.         \tag{25}
\]
The constants are sufficient. Under (W) the left side can be made arbitrarily small on further fixed dyadic sizes. The all-twist affinity being tested is near \(1/8\) because the two observations share a readable magnetic class.

**PROVED (accounting for the shared label).** First use the exact all-twist Wilson law. Write \(p_m=\theta(m)\) for its temporal-frame magnetic marginal and \(A_m\) for the raw temporal collar affinity conditional on this \(m\). Adjoin \(m\) to each of the two observations. Their square-root joint-density operator is a direct sum of the conditional operators weighted by \(\sqrt{p_m}\), so its fourth trace is \(\sum p_m^2 A_m\). On either collar a single time slice reads all three magnetic periods with total error \(O(n^3 e^{-c\beta n})\), by (5) applied to the intersecting three-torus. Appending the local estimate on either side leaves the affinity exactly the same since each observation retains its original coordinates. Replacing both estimates by the true label changes it by \(o(1)\) by (7). Thus
\[
               \mathcal A=\sum_m p_m^2 A_m+o(1).                        \tag{26}
\]
The same formula applies after transfer to the local law, with its TV error included.

**PROVED (sufficiency).** Put \(r=256\delta\) from (23). The strict bound in (25) ensures eventually \(r<1/2\), allowing \(o(1)\) for the readings. Thus \(\sum p_m^2\le\max p_m\le1/[8(1-r)]\le1/8+r/4\). By (19), \(p_0\ge1/8\), so (26) gives
\[
 1-A_0\le64\,|\mathcal A-1/8|+16r+o(1).
\]
The factor multiplying \(A_0\) in (20) is \(\frac18\sum_e f(0,e)\ge1-r\). Therefore its product with \(A_0\) falls below one by at most \(64|\mathcal A-1/8|+17r+o(1)\). Cubic symmetry and the readable-slice estimate in (23) give \(\delta=(8s_\perp-1)_++o(1)\). Since \(17\cdot256=4352\), the strict margin proves (20).

**PROVED (necessity).** By (24), all \(p_m\to1/8\) and \(s_\perp\to1/8\) in the same ordered limits. In the law conditional on \(m\), sum temporal twists as in the lower comparison of (10), using the actual static magnetic transfer \(F_m/\lambda_m\) and its positive centre-invariant vacuum. The stationary-segment calculation with these replacements bounds \(A_m\) below by the product of the inverse square of the neutral trace at \(T\) and the inverse fourth power at \(2d\), both normalized by \(\lambda_m\) at their respective times. Here \(2d=n/4\) on the enlarged sides. Each full trace at these times tends to one by (24), and a projected trace lies between one and the full trace. This proves \(A_m\to1\) for all eight \(m\). Equation (26) gives \(\mathcal A\to1/8\). The TV comparison (18) and the continuity in (7) pass both measurements to the single finite-range adjoint model in (25). An observed collar supplies its full array of periodic adjoint links. No fundamental link, sector label or conditioned measure is an input to that test.


## Trying to move between the classes

**PROVED (support of the measurements).** In (25) the two temporal collars can each have a fixed number of lattice layers on any trajectory \(\beta\ge\kappa\log n\). Choose the short-collar radius in the proof of (10) with \(Cn^4e^{-c\beta r}=O(n^{-4})\) and include those short collars strictly inside the observed ones. Their centres remain separated by \(T/2\). The upper comparison in (10) needs only those layers. In the lower comparison \(d=T/2-h\) then has \(2d\ge n/4\) for large \(n\), so the magnetic trace at \(2d\) is at most its normalized trace at \(n/4\). This preserves necessity in (25). On the transverse three-torus each of its three bits can also be read on a strip of fixed width by (6). Thus the two sets of temporal observations have \(O(n^3)\) links altogether and the transverse observation needs \(O(n^2)\). Their law still involves the full four-dimensional interacting field.

**PROVED (contractible changes).** In the exact Wilson all-twist adjoint law, let \(V,V'\) be any stationary pair with identical links off a possibly data-dependent coordinate box of side lengths less than half the corresponding periods. Use fixed reference slices and (5) to define the six-bit reading \(\widehat b\). Then
\[
                \mathbb P\{\widehat b(V)\ne\widehat b(V')\}
                            \le C n^4 e^{-c\beta n}.                     \tag{27}
\]
In a single path the probability that *any* of the \(O(n)\) coordinate three-tori fails on any of its three bits is at most the displayed bound, by a union bound in the joint mixture. Hence with this accuracy all readings on all slices agree on the bits they share. Apply that assertion to both endpoints of the stationary pair. For any component \(b_{ij}\), choose a slice in a third direction outside the update box. It contains the two-torus needed for this reading and its internal links are identical at both ends. This proves (27), including for adaptively selected boxes. Consequently a stationary chain using such moves over \(M\) steps has probability at most \(CMn^4 e^{-c\beta n}\) of changing the reading. If the variance of a decoded bit is bounded below, its indicator in the reversible Dirichlet quotient gives a relaxation gap at most \(C'n^4 e^{-c\beta n}\) for this dynamics. By (24) that hypothesis holds at sufficiently large dyadic physical sizes under (W). This obstructs a proof by fast mixing of the *unconditioned* local updates. The estimate concerns an auxiliary update chain.

**GUIDE.** The earlier twist-insertion brainstorm identifies the cost of a constant noncentral rotation on one seam. A possible way around it is to spread the rotation, let it differ at both endpoints of every link, or choose a sheet from many backgrounds after seeing the sample. The bounds below apply to endpoint rotations on arbitrary links. [Earlier seam observation, item 14](gap-brainstorm2-max.md)

**PROVED (mean action cost of arbitrary fixed endpoint rotations).** For every oriented link \(\ell=xy\) choose \(L_{x,\ell},L_{y,\ell}\in SU(2)\) and set
\[
                  (\Phi U)_\ell=L_{x,\ell}U_\ell L_{y,\ell}^{-1}.
\]
The choices may depend on the size and coupling. For a target twist \(B\) with \(b_{ij}=1\), let \(M=n_k n_l\) be the number of parallel \(ij\)-planes, where \(\{i,j,k,l\}\) are the four axes. Let \(S_B=\beta\sum_p(1-\epsilon_p^B w_p)\) be the twisted action, and \(\mu_0\) the actual periodic fundamental law. For all sufficiently large \(\beta\), uniformly in the periods,
\[
        \mathbb E_{\mu_0}[S_B(\Phi U)-S_0(U)]
                       \ge \tfrac12(1-2^{-1/2})\,\beta M .              \tag{28}
\]
To see this, independently Haar-rotate the local frames at all vertices. This preserves \(\mu_0\). At a corner \(x\) of \(p\) between links \(\ell,\ell'\) it conjugates \(L_{x,\ell}^{-1}L_{x,\ell'}\) by an independent Haar variable. The conjugation integral is the scalar \(h_{p,x}=L_{x,\ell}\cdot L_{x,\ell'}\) in the unit-quaternion inner product. The four vertices are distinct. At fixed original links the gauge-orbit mean of the transformed trace is exactly \(w_p\prod_{x\in p} h_{p,x}\). Also \(\mathbb E_{\mu_0}w_p\ge1/2\) for every face at sufficiently large \(\beta\), by the one-face tilted bound at any fixed small action threshold. The mean cost is therefore the sum of the nonnegative terms \(\beta\,\mathbb E_{\mu_0}w_p(1-\epsilon_p^B\prod_x h_{p,x})\).

**PROVED.** In each parallel \(ij\)-plane there must be a face with \(\epsilon_p^B\prod_x h_{p,x}\le2^{-1/2}\). Otherwise every corner has \(|h|>2^{-1/2}\) and the corner-product sign equals \(\epsilon_p^B\) on every face. At each vertex of the plane consider its four endpoint quaternions on the four incident in-plane links in cyclic order. Align successive signs along that cycle by the shorter projective angle. Every step on \(S^3\) has length \(<\pi/4\). An odd product of the four corner signs would give a path from a quaternion to its antipode of length \(<\pi\). Thus the product of the four corner signs at each vertex is positive. Multiplying first over vertices and then over faces contradicts \(\prod_{p\in\Pi}\epsilon_p^B=-1\). The selected faces are distinct over the \(M\) planes, proving (28). All link maps above preserve product Haar. Jensen applied to their action increment gives only \(\exp[-\mathbb E(S_B\circ\Phi-S_0)]\) as a lower bound for \(Z_B/Z_0\). Even its supremum over these maps is at most \(\exp(-c\beta M)\).


**PROVED (change-of-measure obstruction, including adaptive selection).** More strongly, let \(\mathcal F_n\) be any list of prescribed endpoint rotations of size \(K\). A map may select from the list after seeing \(U\), with arbitrary extra randomness. Write \(\nu\) for the resulting path law, \(\mu_B\) for the normalized true twisted law and \(\widetilde\mu_B=f(B)\mu_B\). With \(M\) as in (28), for absolute \(c,C>0\) at sufficiently large \(\beta\),
\[
      \int\sqrt{d\nu\,d\widetilde\mu_B}
         \ \le\ \sqrt{CKe^{-cM}}+\sqrt{CK e^{-c\beta M}}.              \tag{29}
\]
To prove it, for each fixed map select one offending face per parallel plane as in (28). Distinct planes have disjoint vertex sets. In an original untwisted sample at least half these faces have nonnegative trace except on \(Ce^{-c\beta M}\), by the specified-face estimate and a union over subsets. Now randomize the original vertex gauges. On every such face the conditional mean of the new signed trace is at most \(2^{-1/2}\). This follows from the exact gauge-orbit formula and \(0\le w_p\le1\). The signed action \(1-\epsilon_p^Bw_p(\Phi U)\) is between zero and two. If \(b_*=1-2^{-1/2}\), it is at least \(b_*/2\) with conditional probability at least \(b_*/4\). These events use disjoint vertex Haar variables and are independent conditional on the original sample. The indicator bound used in (21) therefore gives at least \(b_*M/16\) such faces except on \(Ce^{-cM}\). Unconditional gauge invariance transfers this bound to the stated source law and map.

**PROVED.** For this fixed list take \(E\) to be the **union** of these target-field events over its selected face sets. With probability at least \(1-CKe^{-cM}\) the original sample has the requisite excess on the output of *every* candidate when tested on that candidate's own face set. Thus \(\nu(E^c)\le CKe^{-cM}\) even for adaptive selection. In the true twisted integral the expensive-face estimate before division by \(Z_B/Z_0\) gives \(\widetilde\mu_B(E)\le CKe^{-c\beta M}\), after choosing the expensive subset from the \(M\) nominated faces for each candidate. Cauchy–Schwarz on \(E,E^c\), using \(\widetilde\mu_B(1)\le1\), proves (29). The argument also holds if the family admits a net of size \(K\) at a sufficiently small fixed radius in the maximum endpoint geodesic distance. Approximating a map then moves any plaquette angle by at most eight times that radius, so use \(b_*/4\) for the target test. For \(\log K=o(M)\) and \(f(B)\) bounded away from zero, the normalized path laws have TV distance tending to one. In particular a near-lossless transport of the kind needed by (23) would require order \(n^2\) in the logarithm of the number of distinguishable rotation choices, or a map outside this family. The estimate on overlap leaves the actual ratio \(f(B)\) undecided.


## Testing a curvature argument inside the zero class

**GUIDE.** Row 1141 already gives a Wilson-probability lower bound on the *scalar adjoint covariant Laplacian* in a block, including adapted colour axes. The earlier tree distinguishes an integrated curvature estimate from pointwise curvature, and the brainstorm mentions a charged spin-one instability in constant magnetic flux. I tested whether a scalar lower bound together with small plaquettes and zero class could suffice for a pointwise convexity estimate on the remaining continuous fields. [Row 1141, equation (2)](gap-crux2-astra62.md) · [Integrated curvature proposal](gap-tree-astra.md) · [Earlier instability observation, item 11](gap-brainstorm-max.md)

**PROVED (pinned scalar colour and many negative horizontal directions).** There are mark-free, zero-class backgrounds on the physical tori for which every plaquette angle is \(O(\beta^{-1})\), the periodic spatial adjoint scalar Laplacian is bounded below by \(c/\beta\), and the Wilson action Hessian has a horizontal subspace of dimension at least \(c'n^2/\beta\) on which it is \(\le-c''I\). Here \(\beta\to\infty\), \(\beta=O(\log n)\), and the metric is the product unit-quaternion metric. The simple adjoint weight (17) has the same negative log density relative to adjoint Haar, up to a constant, on a neighbourhood of these configurations.

**PROVED.** Take the spatial 1- and 2-links constantly \(\exp(I\theta)\) and \(\exp(J\theta)\) with perpendicular unit imaginary quaternions, and all other links equal to one. Choose \(1/\sqrt\beta<\theta<2/\sqrt\beta\), avoiding the finitely many values for which either corresponding full winding is central or a half-turn in \(SO(3)\). The two winding axes give a trivial common stabilizer in the adjoint group. The \(12\)-plaquette scalar is \(1-2\sin^4\theta\) by quaternion multiplication, and the other plaquettes are the identity. The plaquette angle is \(O(\theta^2)\), all signs are positive in these lifts, and all local marked correction factors of (17) are one near the configuration.

**PROVED (scalar pin).** Fourier transform on the spatial torus. With \(R_I,R_J\) the adjoint rotations through \(2\theta\), the scalar form on any unit complex colour vector \(v\) contains
\[
             \|(e^{ik_1}R_I-1)v\|^2+\|(e^{ik_2}R_J-1)v\|^2 .
\]
Its infimum over all real momenta and \(v\) is at least \(c\theta^2\) for all small \(\theta\). Otherwise take \(\theta\downarrow0\) and a sequence with both norms \(o(\theta)\). Since \(\|R-1\|=O(\theta)\), reduce the phases modulo \(2\pi\) to obtain \(k_i=O(\theta)\). Pass to limits of \(k_i/\theta\) and \(v\). Expansion of the two rotations shows the limiting unit vector is an eigenvector of both cross-product generators \(I\times\) and \(J\times\). Their commutator is \((I\times J)\times\), so this vector is parallel over \(\mathbb C\) to \(I\times J\). Its cross product with \(I\) rules out that eigenvector. This proves the lower bound uniformly in the periods.

**PROVED (action Hessian).** Take any real \(u(x_3,x_4)\) and change the two angles to \(\theta+t u\) and \(\theta-t u\). These are product geodesics. The tangent at each site is orthogonal to gauge directions because it commutes with its own link, and its coefficients are constant along directions 1 and 2, so the two directional covariant divergences vanish. The \(12\)-plaquette action along the path is \(2\beta(\sin^2\theta-\sin^2(tu))^2\). Each mixed plaquette between directions \(1,2\) and \(3,4\) contributes \(\beta(1-\cos(t\nabla_i u))\) for the corresponding transverse difference. Dividing the second derivative by the squared tangent norm \(2\sum_x u^2\) gives
\[
   \frac{\mathrm{Hess}\,S[\dot U,\dot U]}{\|\dot U\|^2}
       =\beta\,\frac{\sum_{x,\,i=3,4}|\nabla_i u|^2}{\sum_x u^2}
                            -4\beta\sin^2\theta .                       \tag{30}
\]
On transverse momenta with \(|k_3|,|k_4|\le\sin\theta/2\) the first quotient before multiplication by \(\beta\) is at most \(2(\sin\theta/2)^2\). There are at least \(c\,n_3n_4\theta^2\) real dimensions there, by counting the integer frequencies in each of the two intervals and pairing complex conjugates. Equation (30) is uniformly negative on this whole subspace. All these variations preserve the zero magnetic and electric class for small \(t\). This refutes uniform convexity under the stated pointwise conditions, even after removing the gauge orbit. A weighted, integrated Hessian estimate would need additional control on the path measure.


## Is the negative curvature confined to atypical backgrounds?

**PROVED (typical horizontal instability of the actual Wilson action).** In the ordinary Wilson law, or either twist mixture, there are with probability at least \(1-Ce^{-c\beta n^4}-e^{-c n^4e^{-7\beta}}\) at least \(c n^4e^{-7\beta}\) mutually orthogonal horizontal directions spanning a subspace with action Hessian \(\le-c'\beta I\). Here and below the constants can depend on a fixed padding radius. This gives a growing index when \(\limsup\beta/\log n<4/7\).

**PROVED.** Choose disjoint four-link blocks with a fixed surrounding neighbourhood, as in (21). On a good exterior start with the small-curvature completion as in (12) and now use four rotations of angle \(\theta=\arccos(3/4)\) in the positive traversal direction. At zero initial error, the signed central scalar is \(\cos4\theta=8(3/4)^4-8(3/4)^2+1=-31/32\) and each of the twenty other affected scalars is \(3/4\). The sum of the 21 actions divided by \(\beta\) is \(223/32<7\). The curvature coefficient is \(16(-31/32)+20(3/4)=-1/2\). Both inequalities have fixed margins. Finite product Haar balls around the rotated completion therefore have conditional mass at least \(c e^{-7\beta}\), central scalar near \(-31/32\) and the other twenty near \(3/4\). Require also that all unmodified faces in the padding have true holonomy within a fixed small angle of the identity. A bad exterior then witnesses an expensive face among a bounded number of faces of its block or padding. Spacing the blocks far enough makes these witness sets disjoint. The tilted estimate and the binomial argument of (21) show that at least the stated number of blocks realize the pattern with the claimed probability.

**PROVED.** On each such four-link loop choose a unit Lie axis commuting with the central holonomy and parallel-transport it around the four corners. Vary the four positively traversed links by unit-speed left geodesics with those axes, using the inverse variation for a negatively oriented coordinate link. At every corner the outgoing axis equals the parallel transport of the incoming one. The resulting link tangent is horizontal. In the central product all four rotations add, giving the scalar of \(\exp(4tI)U_p\) in the initial frame. On any other affected face just one link rotates, with speed one. The signed action therefore has second derivative
\[
                   \beta\left(16w^b_{\rm centre}
                                  +\sum_{\rm other\ 20} w^b_p\right)    \tag{31}
\]
in a direction of squared norm four. On the stated open pattern this is \(\le-c\beta\). Distinct chosen tangents have disjoint supports, and even the sets of affected faces are disjoint, so every cross term is zero. This proves the assertion for the full subspace.

**PROVED (after summing out every centre sign).** In fact assume \(0<\liminf\beta/\log n\le\limsup\beta/\log n<4/7\). Let \(S_{\rm ad}\) be the *exact* negative log density of the adjoint Wilson marginal relative to adjoint product Haar, in either twist mixture or the untwisted law. With probability tending to one its Hessian on the horizontal link directions obeys
\[
 \#\{\text{horizontal Hessian eigenvalues of } S_{\rm ad}\le-c\beta\}
                            \ \ge\ c' n^4e^{-7\beta}.                   \tag{32}
\]
The derivatives here refer to the exact finite sum over signs. TV approximation of a density alone need not approximate those derivatives.

**PROVED.** Draw a second sign configuration conditionally on all the adjoint links of a true path. Denote the twisted negative sets by \(\xi,\xi'\). Their difference \(D_*=\xi+\xi'\) is closed. For any prescribed set of \(j\) differing faces, assign each face to a replica in which it is negative. The union over assignments and Cauchy–Schwarz with the two true marginals bound its probability by \((C e^{-c\beta})^j\), allowing a fixed multiplicative constant. The rooted connected-set estimate gives \(C n^4e^{-c\beta R}\) for any component of \(D_*\) having at least \(R\) faces. Choose \(R\) fixed to make this probability \(O(n^{-8})\). Markov's inequality shows that except on an \(O(n^{-4})\) set of first paths, the conditional probability of any such component in the second draw is \(O(n^{-4})\).

**PROVED.** Use padding of face-graph radius \(R+3\) about the affected faces in (31). In each realized pattern the true negative set there is just its central face and every magnitude is above \(a_0=2/3\). A smaller component \(C\) of \(D_*\) touching any affected face is closed, fits inside the padding, is exact, and contains at least six faces by the dual-cycle argument for (17). At fixed first path, erase this specified component from the second configuration by changing its signs on \(C\). This is an injection on the allowed second negative sets, with constant sign-link multiplicities. On \(C\) the second signs are the opposite of the first ones. Hence the relative weight of the configuration before erasure is at most \(\exp[-2\beta(5a_0-1)]\). This accounts for the possible central face with negative first sign, and all other faces have positive first sign. Only boundedly many sets of size below \(R\) meet the 21 faces. On all the realized blocks simultaneously, the posterior probability of any mismatch on its 21 faces is therefore at most \(O(n^{-4})+C_R e^{-2\beta(5a_0-1)}=o(1)\) *per block*. The \(O(n^{-4})\) exceptional set of first paths is global.

**PROVED.** Use smooth local lifts through the sampled configuration to differentiate the sign sum, keeping each summand's twist fixed. The Hessian of the negative log sum is the posterior mean of the signed action Hessians minus the posterior covariance of their gradients. The latter subtraction is negative semidefinite. All lifts give the same adjoint parallel transport used to choose each loop tangent. Formula (31) in any lift has magnitude at most \(36\beta\). In the displayed posterior mean its value is negative by a fixed multiple of \(\beta\) on each of the chosen directions, since the mismatch probability there tends to zero. The action Hessians of different blocks have zero cross terms in every lift, so the posterior *mean* is negative on their whole span. The covariance subtraction preserves that inequality. The construction holds with joint probability tending to one and its Hessian conclusion depends on the adjoints alone, proving (32). Thus uniform nonnegative action curvature cannot be restored by discarding a set of vanishing Wilson measure or by performing the exact sign integration. An estimate exploiting cancellation of the negative directions in the functional integral remains OPEN.


**PROVED (after integrating the entire space between the measured collars).** Let \(Y\) be either one of the two temporal collars in (25), or their union. Choose the allowed, fixed collar width sufficiently large depending only on a lower logarithmic slope. For the *exact Wilson marginal* on \(Y\) in the all-twist law, the temporal-twist law or the ordinary law, put \(S_Y=-\log(d\mu_Y/d{\rm Haar}_Y)\). On
\[
    0<\liminf\beta/\log n\le\limsup\beta/\log n<3/7
\]
one has, with probability tending to one,
\[
 \#\{\text{horizontal eigenvalues of }\mathrm{Hess}\, S_Y
                          \ \le-c\beta\}\ \ge\ c_R n^3e^{-7\beta}.      \tag{33}
\]
In particular this index diverges on the conditional SU(2) one-loop slope, since \(11/(3\pi^2)<3/7\) follows already from \(\pi>3\). This is a statement on the very data in the last test. It applies after all fundamental lifts and all unobserved continuous variables have been integrated out.

**PROVED.** Place spatial plaquette centres on one time slice in the interior of an observed collar, with separation exceeding twice the fixed padding radius \(R+3\) and sufficient margin to its temporal boundaries. There are at least \(c_R n^3\) disjoint padded blocks there. The first-path argument for (31) works with this number in place of \(c_Rn^4\). For the posterior draw now condition on *only* the adjoints in \(Y\). Both full path marginals are still true Wilson marginals. On faces whose four links are observed the relative negative set is defined as before, and it is closed on every cube whose links are all observed. Any connected component touching one of the 21 faces and reaching an unobserved cube has size at least \(R\). The estimate \(Cn^4 e^{-c\beta R}\) for connected sets of observed differing faces follows from the same assignment and Cauchy–Schwarz proof, regardless of what happens on unobserved faces. A smaller component touching the block fits strictly inside the observed collar and is a compact closed cochain in the full torus. Erasure changes only link signs, so preserves the conditioning on \(Y\) as well as product Haar on the unobserved links. The same posterior mismatch bound follows for each planted block. Differentiating the finite-dimensional compact integral for the exact marginal gives the same mean Hessian minus gradient covariance formula. The 21 affected faces for each variation are wholly observed, so (31) gives its Hessian in every completion. The block count now tends to infinity because \(n^3e^{-7\beta}\to\infty\), proving (33). Thus pointwise nonnegative Hessian for the actual marginal fails on every set of probability tending to one in this range. Even independent collars could have negative eigenvalues in their individual log densities. Their interaction is a separate quantity.


## Removing the collar interiors and identifying the remaining dependence

**PROVED (conditional independence at the local interaction range).** Use the range \(r_*\) of (18) in the all-twist model, enlarged by a fixed lattice step to cover the diameters of its factors. In each of two disjoint collars keep its two inside boundary layers of thickness \(r_*\), writing \(J_1,J_2\) for their unions at the respective collars. The collars may have any larger thickness compatible with (10). At fixed \(J_i\), all factors involving the remaining interior of collar \(i\) are internal to that collar. Thus adjoining those interiors to the joint boundary law uses two independent kernels, each depending only on its own \(J_i\). This follows by factorizing the Haar integral, including local zero-weight constraints on the support. Marginalizing gives the inverse deterministic channels. The two-collar rectangle affinity equals the two-boundary affinity exactly in this model. Moreover the exact all-twist Wilson collar law is within \(O(n^{-k})\) of reconstruction from its *actual* pair of boundary readings by these two kernels: approximate the full law by (18), independently reconstruct in that law, and use TV contraction for the difference of boundary marginals. This removes interior dependence across the two collars. The joint distribution of their boundaries is still needed.

**PROVED (ordinary probability interpretation).** For any joint probability \(P_{XY}\) with square-root kernel and rectangle affinity \(A\),
\[
 \|P_{XY}-P_X\otimes P_Y\|_{\rm TV}\le3\sqrt{1-A},\qquad
 A\ge(1-\|P_{XY}-P_X\otimes P_Y\|_{\rm TV})^4 .                       \tag{34}
\]
Indeed the squared singular values of the kernel sum to one and their squared sum is \(A\). Its largest singular value is at least \(\sqrt A\) and can be achieved on two nonnegative unit vectors by taking absolute values in the integral. Their squares specify a product law of Hellinger affinity at least \(\sqrt A\) to the joint law. Its TV distance is at most \(\sqrt{1-A}\) by Cauchy–Schwarz on the sum and difference of the square roots. Each true marginal lies within this distance of the corresponding product factor. Applying the triangle inequality proves the first inequality. In reverse, Hellinger affinity to the product of true marginals is at least one minus TV and at most the largest singular value, proving the other inequality.

**PROVED (what would remain shared under a seed).** By (24), (26) and (34), under (W) the true two-collar law in the unrestricted twist mixture tends in TV, in the ordered limits above, to the following comparison law at the same cutoffs. Draw \(m\) uniformly among its eight values and, conditional on that choice, draw each collar *independently* from its actual one-collar law in sector \(m\). Both collars recover \(m\) separately by (5). For example the event that their decoded magnetic triples coincide has probability tending to one in the joint law and to \(1/8\) in the product of its unconditioned marginals. Consequently unconditioned temporal decorrelation in TV is impossible under a seed. Within each magnetic sector ordinary asymptotic independence of the boundary data is the remaining neutral estimate. Conversely vanishing sectorwise TV errors of this kind and \(s_\perp\to1/8\) imply (25) on some sufficiently large fixed side, by (23), (26) and the second inequality of (34).


**PROVED.** The corresponding unconditioned TV distance tends to exactly \(7/8\) under (W). For the upper bound, take the two magnetic labels first. The TV distance between the shared-label law of \((m,m)\) and the independent-label law is \(1-\sum p_m^2\). Drawing the two conditionally independent collars is a probability channel and cannot increase this distance. The sectorwise product approximation above costs \(o(1)\). The coincidence event gives the matching lower bound. This quantifies the obstruction to proving ordinary mixing in the unrestricted measure.

## What remains at fixed physical size

**PROVED (limits of the available inferences).** The charged comparison (1) leaves at most seven exceptional levels. The comparison following (3) leaves their weights free even with perfect neutral relaxation. The high-accuracy readings in (5)–(6) determine realized classes, while (14) rules out inferring their frequency from all bare plane products. Finite range in (18) gives conditional independence across a known boundary. The shared label in (27) obstructs using fast unconditioned local dynamics to determine its frequency. For a nonzero target flux, (28)–(29) obstruct near-lossless insertion by prescribed endpoint rotations or by choosing adaptively from subexponentially many such rotations in transverse area.

**PROVED (limits on the neutral route).** The checked Proposition SEP of the earlier glue analysis already preserves every flux ratio and crossing identity while a neutral factor changes the excited count. Row 1155's exact-cell construction preserves the genuine one-collar marginals and any given finite antipodal cell table while its square-root affinity drops by an arbitrary integer factor. These are comparisons of possible inferences. For a quadratic replacement, the earlier free transverse field has a neutral two-photon state of energy \(4\pi/L\), including the cubic scalar, zero-momentum channel. At time \(L/2\) this one weight is \(e^{-2\pi}>1/1650\), since \(2\pi<13/2\) and \(e^{13/2}<3^{13/2}<1458\). In the interacting Wilson measure itself (30) defeats pointwise convexity from scalar pinning, and (33) defeats nonnegative marginal Hessian on a set of probability tending to one even for the two observed collars. None of these arguments estimates the residual joint boundary density in (34). [Checked product obstruction, section 5](gap-glue-check-astra.md) · [Exact-table construction](gap-solve7-astra62.md) · [Two-photon comparison, equation (33)](gap-channel-astra.md)

**OPEN.** The missing physical estimate is a bound on \(s_\perp\) and on the boundary dependence within the magnetic sectors strong enough for (25) at some fixed admissible \(L\). Uniformity of the twist classes alone leaves the neutral trace undetermined. The count of local sign defects and the negative local Hessian directions occur already inside a single collar. Estimating their frequency does not give the dependence between distant collars. The earlier pressure comparison with Bałaban and Chatterjee controls the bulk normalization to its stated accuracy. It does not bound this joint boundary law or the twist ratios to the strict required accuracy. On a trajectory for which a positive lower logarithmic slope has not been established, (11) is the raw Wilson test and the bounded-range conclusion (18) retains its stated hypothesis. The exact all-twist version of (25) follows from (5), (10) and (23)–(26) without that lower slope on the lane grid \(\beta\to\infty\), allowing the short reading windows to grow as \(1+\log n/\beta\). [Earlier pressure comparison](gap-solve7-astra62.md)

**GUIDE.** Research note at the pinned revision. The uses of row 1155 are identified with the corresponding hand arguments. I found no failed step in the inputs used here. Row 1156's review was unavailable at this revision, and the claims in this note have no independent review or status. No numerical run was used.

RESULT: Row 1157. PROVED by hand here, (W) has the one-period unconditioned adjoint test (25), with bounded-range weights under (18). One transverse zero-class probability controls all 64 twist ratios by (23). A periodic seed forces near-vacuum dominance in all eight magnetic sectors by (24). Equations (29) and (33) obstruct low-complexity twist insertion and typical collar convexity, respectively. OPEN are the transverse class frequency and the neutral inter-collar dependence at a fixed physical size. The four-dimensional SU(2) mass gap remains unresolved.
