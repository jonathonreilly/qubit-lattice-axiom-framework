## Repo search

**GUIDE (sources).** At checkout `659db0a48`, the target-specific prior file is absent. The lead's November 8 survey searched main and PRs 10114, 10133, 10134 and 10141. Its closest hit is the soft-route one-step plaquette witness. I checked the following primary passages at the fetched revisions.

| | Passage | Bearing on the problem |
|---|---|---|
| GUIDE | PR 10114, `f76f6c649c`, `MASS_GAP_LOCAL_BLOCK_ASTRA.md` 4–14, 106–149 | The loop has positive one-step correlation. The section on contraction assumes small bare coupling. |
| GUIDE | Grok, PR 10133, `89faef229f`, `MASS_GAP_CROSSOVER_REDUCTION.md` 77–86 | Crossover and transport of sources through the renormalization group are open inputs. |
| GUIDE | PR 10134, `1e70c7211a`, `library/mass-gap-interface.md`, I1–I5 | Gives the distinctions between nontriviality, a positive spectral threshold, and identification as Yang–Mills. |
| GUIDE | PR 10141, `a2f6a430e2`, `research/ym4d/library/fp1.md` 299–315 | The coercive estimate is for a constrained classical field at one scale. |
| GUIDE | Main, `8b11ae2bb9`, `research/mass-gap/library/gap-phys-seed.md` 305–329 | Theorem ZD-c relates the physical thermal seed to two estimates on boxes. It supplies a consumer and leaves the estimates as premises. |

**GUIDE (prior literature).** The row 1218 reading credits Deep Bhattacharjee, Ushashi Bhattacharya, James Montgomery Lockwood, Tristan Romanov, Ikailo John Sessford and Sanjeevan Singha Roy for the ascent from a one-scale estimate on a window of periodic thermal traces. It distinguishes the restricted straight-path result of the first four authors and the conditional common-rate and tunnelling results of Zeng Chunping. I use the reading to locate alternatives. No conclusion here depends on their unverified hypotheses.

**GUIDE (account).** The outline index, chunk 29 and its obligation at 31871–31882, lead to the authors' distinction between a reconstructed action-density sector and a gap for the full theory. Outline 31858–31882, 32481–32490 and CA-I 2704–2712, 3213–3222 were checked at `31a47c543775`. Credit for those texts belongs to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. The CA-I 4.12–4.19 index concerns the ultraviolet induction. I found no mass-gap assignment under that name in `library/open-registry.md`. Row 1252 explicitly assigns this independent attempt.

**OPEN (target).** Construct nontrivial pure SU(2) Yang–Mills theory on four-dimensional Euclidean space with the axiomatic properties required by Jaffe and Witten, reconstruct its Minkowski vacuum theory, and prove that for some physical mass m>0 its Hamiltonian has spectrum in {0} ∪ [m,∞), with the vacuum as the only invariant state vector up to scalars in the vacuum representation. A proof needs both full observable identification and a positive threshold in the infinite-volume continuum representation.

## Choice of attack

**GUIDE.** I will look for a lower bound on the relaxation rate of the four-dimensional Wilson measure using its exact conditional distributions. Bhattacharjee, Bhattacharya, Lockwood and Romanov use a cube update to infer physical decay. A single-link or fixed-block update at a cutoff with spacing a could have a relaxation rate of order a². A bound on correlation length proportional to the inverse square root of that rate would then suffice. The conditional projections fix the constant vector exactly and commute on links which share no plaquette. This suggests the detectability lemma of Aharonov, Arad, Landau and Vazirani, its projection proof by Anshu, Arad and Vidick, and the square-root correlation-length estimate of Gosset and Huang for frustration-free systems. The comparison here is on the four-dimensional Euclidean probability space.

**GUIDE (relation to prior work).** `gap-afield-b-max.md`, B1, proposes a local frustration-free comparison for the *physical* transfer and a subsequent patch criterion. The present projections are explicitly defined from the Euclidean Gibbs law. `gap-skeleton-max.md` mentions square-root decay for a Langevin gap. `gap-solve26-astra62.md`, (35)–(36), uses propagation under cube updates and a small-wavelength Wilson test. Those are precedents for the method. I will first establish the physical-unit estimate for conditional projections, then try to prove its required lower bound in the Wilson model. I also test the rate on a model with known massless modes.

## From elementary Wilson updates to two time sublattices

**GUIDE (notation).** On an even periodic four-dimensional lattice of side at least four in every direction, base each positive link at its initial vertex. Take the Wilson probability
\[
 d\mu=Z^{-1}\exp\!\left[\beta\sum_p \tfrac12\operatorname{Tr} U_p\right]\prod_e dU_e ,
\]
with normalized SU(2) Haar measures. The trace is real. In \(L^2(\mu)\), let \(P_e\) condition on every link except \(e\), and set \(Q_e=I-P_e\). Let \(\mathcal V\) be the centered gauge-invariant space. It may additionally be restricted to invariance under the four torus centre flips. Every projection below preserves these spaces because the symmetries preserve the law and each specified coordinate sigma field. Write
\[
 \gamma=\inf_{0\ne f\in\mathcal V}
          \frac{\sum_e\|Q_e f\|_2^2}{\|f\|_2^2}.                         \tag{1}
\]
Each link has rate one in this normalization. Let \(P_E\) integrate all links with even base time conditionally on the odd ones, and let \(P_O\) do the reverse.

**PROVED (projection estimate).** With \(D=18\), on \(\mathcal V\),
\[
 \|P_OP_E\|\le\rho_*=(1+\gamma/D^2)^{-1/2}.                           \tag{2}
\]
Two distinct links outside a common plaquette are conditionally independent given all the others. Indeed the conditional density in those two variables factors. Their conditional projections therefore commute. Each link has six incident plaquettes, each with at most three other links. This supplies the commutation count \(D\) uniformly in volume and coupling.

**PROVED (argument for (2)).** Order the single-link integrations with all even links first. Starting from \(v_0\in\mathcal V\), put \(v_i=P_i v_{i-1}\) and \(b_i=\|v_i-v_{i-1}\|\), using the order to index the projections. Orthogonality gives \(\sum b_i^2=\|v_0\|^2-\|v_N\|^2\) for \(N\) links. Fix \(i\). At step \(i\), \(Q_i v_i=0\). A later commuting integration cannot increase \(\|Q_i v_k\|\), and at any other later step \(k\) it increases by at most \(b_k\), by the triangle inequality. Thus
\[
 \sum_i\|Q_i v_N\|^2\le
 D\sum_i\sum_{k>i:\, k\sim i}b_k^2
 \le D^2(\|v_0\|^2-\|v_N\|^2),
\]
where \(k\sim i\) denotes a shared plaquette. Apply (1) to \(v_N\) to obtain \(\|v_N\|\le\rho_*\|v_0\|\). If \(v_0\in\operatorname{ran}P_E\), every even integration fixes it. If \(w\in\operatorname{ran}P_O\), every odd integration fixes \(w\). Moving the odd integrations to the other side of the inner product gives \(\langle w,v_0\rangle=\langle w,v_N\rangle\). The supremum over unit vectors in these two centered invariant ranges is \(\|P_OP_E\|\). This proves (2), including for continuous link variables.

## A mass estimate in physical units

**PROVED (finite-volume connected correlations).** Let \(f,g\) be centered invariant square-integrable functions of two sets of links at cyclic base-time distance \(d\). For every integer \(k\ge1\) with \(2k+1<d\),
\[
 |\langle f,g\rangle_\mu|
 \le 2\|f\|_2\|g\|_2
       \exp\{-2k\operatorname{arsinh}(\sqrt\gamma/D)\}.                \tag{3}
\]
To see the locality needed here, collect all links based at time \(t\) into one packet. Every Wilson plaquette involves either one packet or two consecutive packets. Conditional on odd packets, distinct even packets are independent, and each conditional density reads just the two odd neighbours. Applying \(P_E\) to a function supported at times \(J\) extends its time support by at most one. Indeed only the even packets of \(J\) need integrating. If \(f\) is supported outside this enlargement, then \(\langle f,P_Eg\rangle=\langle f,g\rangle\). To verify the identity even when \(f\) itself uses other even packets, integrate only the even packets of \(J\). This partial conditional expectation fixes \(f\) and has the same action on \(g\) as \(P_E\). The odd version follows by the same factorization.

**PROVED (polynomial filter).** Put \(B=P_EP_OP_E\). It is positive and has norm at most \(\eta=(1+\gamma/D^2)^{-1}\) on \(\mathcal V\), by (2). The product \(B^j\) uses \(2j+1\) alternating integrations for \(j\ge1\). The preceding identity at each step gives \(\langle f,B^jg\rangle=\langle f,g\rangle\) for \(0\le j\le k\). If \(T_k(\cos u)=\cos(ku)\) is the Chebyshev polynomial, take
\[
 p_k(x)=T_k(2x/\eta-1)/T_k(2/\eta-1).
\]
It has \(p_k(1)=1\). On \([0,\eta]\) its norm is at most \(2\exp[-k\operatorname{arcosh}(2/\eta-1)]\), by the identity \(T_k(\cosh u)=\cosh(ku)\). Substitute \(p_k(B)\) in the inner product and use \(\operatorname{arcosh}(1+2y^2)=2\operatorname{arsinh}y\) to get (3). This proof uses the two *time* sublattices, independently of the spatial supports of \(f,g\).

**PROVED (conditional continuum implication).** Fix a sequence \(a_j\downarrow0\). At cutoff \(j\) assume (1) has lower bound \(\gamma_j\) on an unbounded sequence of even four-tori on which the local laws have the volume limit being used. Suppose its reflected centered correlations have a positive transfer representation at even times. Then every bounded local physical observable in the chosen sector has spectral support, after vacuum subtraction, at physical energy at least
\[
 m_j=a_j^{-1}\operatorname{arsinh}(\sqrt{\gamma_j}/D).                  \tag{4}
\]
Indeed at fixed cutoff take volume to infinity at every fixed time in (3). Reflected translates of a bounded local test are at distance at least their translation minus a fixed number of slices. Thus their connected diagonal is bounded by a finite test-dependent constant times \(\exp(-a_j m_j t)\) at even integer translations \(t\). If its positive spectral measure put positive weight below \(m_j-\epsilon\), that weight would eventually violate this inequality. Exhaust the interval below \(m_j\) by such thresholds. This also excludes a centered atom at zero when \(m_j>0\).

**PROVED (passage with contact terms).** Assume the centered reflected diagonals of matched bounded lattice representatives converge at positive physical times on a family total after centering in the proposed continuum Hilbert space. A representative may have a norm that depends on the cutoff. If \(m=\liminf_j m_j>0\), the spectral support just proved gives \(u_j(t_j)\le e^{-m_j(t_j-s_j)}u_j(s_j)\) at physical even times \(t_j>s_j>0\). Take matched times tending to \(t>s>0\). The limit has no centered weight below \(m\) by the same spectral argument, with the finite positive-time value \(u(s)\) as prefactor. Density then gives the Hamiltonian bound and a one-dimensional kernel. This uses the limit argument already in `gap-os-equiv.md`, §§3, 5. In particular \(\liminf_j\gamma_j/a_j^2>0\) suffices. Full observable matching and construction of a Yang–Mills theory still enter as separate hypotheses.

**PROVED (extension used below).** Replace the individual updates in (1) by conditional integrations of finite sets of links, each set based at a single time. Assume every link is covered and each set meets or shares a plaquette with at most \(D'\ge1\) other sets. Disjoint sets outside a common interaction are conditionally independent given their exterior. The proof of (2) uses this commutation count and the fact that a function of odd packets is fixed by each even update. Equations (2)–(4) therefore hold with the new variational constant and \(D'\). The sums in these formulas give each chosen update rate one.

## Relaxation inside an entire conditional line

**GUIDE.** The distinction between memory along a line and heat-bath relaxation on all functions of that line matters here. Row 1155, `gap-solve7-astra62.md`, (3), gives the Wilson line law. Row 1173, `gap-solve15-astra62.md`, (15), bounds the cross ratio of a three-bond kernel, including arbitrary linear fields. I use both as prior results. The following variance estimate uses them to control nonlinear functions of a whole line, including functions defined by rare events.

**PROVED (a one-dimensional estimate).** Take a periodic nearest-neighbour chain of \(M\) compact spins with a strictly positive continuous density. Allow inhomogeneous positive one-site factors. Suppose the edge factors \(K_i\) have four-point log ratios bounded above by \(b\ge0\), meaning
\[
 K_i(x,y)K_i(x',y')\le e^b K_i(x,y')K_i(x',y)
 \quad\hbox{for every }i,x,x',y,y'.
\]
Put \(r=\tanh(b/4)\), \(l=\lceil4/(1-r)\rceil\), and take \(M\ge l+2\). If \(Q_i\) subtracts conditional expectation off site \(i\), then
\[
 \operatorname{Var} f\le 4l e^b\sum_i\|Q_i f\|^2
                 \le 24 e^{3b/2}\sum_i\|Q_i f\|^2 .                   \tag{5}
\]
All norms and variances use this chain, with no restriction on the one-site factors.

**PROVED (long interval updates).** Choose uniformly one of the \(M\) cyclic intervals of length \(l\) and resample its interior. For two exteriors differing only at the left neighbouring site, couple a left-to-right sample, keeping the right boundary fixed. At each internal site the one-step law has density proportional to \(K_i(x,y)w(y)\). Here the same positive \(w\) in both samples includes the complete remaining bridge to the common right boundary. The relative tilt for two inputs has maximum divided by minimum at most \(R=e^b\). For a tilt normalized before reweighting to lie in \([1,R]\) with mean \(z\), its total variation change is at most \((z-1)(R-z)/(z(R-1))\). This follows by bounding the positive part of the tilt minus its mean by the chord on \([1,R]\). Maximizing in \(z\) gives \(r\), with zero change when \(R=1\). A coupling that first samples the common part of the densities has discrepancy probability equal to total variation. After agreement use identical samples. The expected number of discrepancies inside is at most \(\sum_{j=1}^l r^j\le r/(1-r)\). Reversing the chain gives the estimate for a differing right neighbour.

**PROVED.** From a single disagreement, \(l\) interval choices remove it, two can propagate it, and all others leave it alone. Thus one random update contracts the Lipschitz seminorm for Hamming distance by at least the factor \(p=1-l/(2M)\), in the sense \(\mathrm{Lip}(Kf)\le p\,\mathrm{Lip}(f)\) for the random update operator \(K\). The one-disagreement inequality extends to any pair by changing the differing sites in order. Every bounded function has finite Hamming seminorm. Iteration gives \(\operatorname{osc} K^t f\le M p^t\mathrm{Lip}(f)\). The operator is a positive self-adjoint average of conditional projections. For a bounded centered \(f\), this oscillation estimate bounds \(\langle f,K^t f\rangle\) by a finite multiple of \(p^t\). Hence its positive spectral measure vanishes on \((p,1]\), by testing any interval bounded away from \(p\). Density of bounded centered functions yields
\[
 (l/2)\operatorname{Var}f\le\sum_{I:\,|I|=l}\mathbb E\operatorname{Var}(f\mid X_{I^c}).
\]

**PROVED (comparison within an interval).** Fix its exterior. Draw two independent interval configurations \(x,y\). Replace the coordinates of \(x\) by those of \(y\) in order. The law of a hybrid prefix and suffix has density at most \(e^b\) relative to the conditional interval law. In the joint weight of the two paths interchange the prefixes, a product reference measure preserving involution. One edge at the cut changes and the joint likelihood ratio is exactly a four-point ratio. Endpoint factors and one-site terms cancel. Integrating the other hybrid proves the bound, also at the empty and full cuts. Consecutive hybrids agree off site \(i\), hence their conditional expectations of \(f\) off \(i\) are equal. The squared difference of their \(f\) values is at most twice the sum of their squared deviations from this common value. Cauchy–Schwarz on the \(l\)-term telescoping sum and the two-copy formula for variance give
\[
 \operatorname{Var}_I f\le 2l e^b\sum_{i\in I}
               \mathbb E_I\operatorname{Var}_i f .
\]
Average over the exterior and count the \(l\) intervals containing each site. This gives the first inequality in (5). The second follows from \((1-r)^{-1}=(1+e^{b/2})/2\) and \(l\le 6e^{b/2}\). Truncation extends the proof to \(L^2\).

## Application to the isotropic SU(2) Wilson measure

**PROVED (a bound for five-link updates, given row 1173, (15)).** Fix a spatial coordinate direction. A line \(C\) consists of all positive links of **one** orientation whose base vertices run along that coordinate line. Take its period \(3M\). At fixed exterior, and for transverse link orientation, the line law has the quaternion density
\[
  Z_C^{-1}\prod_t \exp[\beta u_t\cdot R_tu_{t+1}+h_t\cdot u_t]\,du_t .
\]
The plaquette between consecutive parallel links gives the orthogonal transport \(R_t\) from the two fixed sides. The other plaquettes give linear fields, as in row 1155, (3), by permutation of lattice axes. For longitudinal link orientation the conditional law is a product, since no plaquette contains two of the chosen links.

**PROVED.** In the transverse case retain \(z_i=u_{3i}\). Conditional on all \(z_i\), the pairs \(W_i=(u_{3i+1},u_{3i+2})\) are independent bridges. The marginal on the retained sites has edge kernels obtained by integrating three consecutive bonds. On each such arc an orthogonal change of coordinates removes the transports and rotates the fields and endpoints. An endpoint field is a one-sided factor and cancels from the four-point ratio. Row 1173, (15), therefore gives a common log-ratio bound
\[
 b_\beta=3\beta+C_1\log(2+\beta)+C_2\qquad(\beta\ge1),                 \tag{6}
\]
with numerical nonnegative constants independent of the exterior. The factor 3 here, in place of the elementary single-bond bound 4, is from that row's continuous exchange of two paths in SU(2).

**PROVED.** Let \(B_i=W_{i-1}\cup\{z_i\}\cup W_i\), a set of five consecutive links. For any square-integrable function \(f\) on the line, including a function with arbitrary fixed exterior parameters, let \(h=\mathbb E[f\mid z]\). Independence of the bridges and the product variance inequality give
\[
 \mathbb E\operatorname{Var}(f\mid z)\le \sum_i\|Q_{W_i}f\|^2
                                     \le \sum_i\|Q_{B_i}f\|^2 .
\]
The product inequality follows by revealing the independent coordinates one by one and bounding each squared martingale increment by the corresponding conditional variance using Jensen. For the coarse single-site variance, let \(P_z\) condition on all retained variables. The law of the bridges other than \(W_{i-1},W_i\), given \(z\), depends only on \(z_{\ne i}\). Given those latter retained variables, these distant bridges are independent of \((W_{i-1},z_i,W_i)\), by the one-dimensional density. Consequently \(P_z P_{B_i} f=\mathbb E[h\mid z_{\ne i}]\), and
\[
 \|h-\mathbb E[h\mid z_{\ne i}]\|^2
       =\|P_z Q_{B_i} f\|^2\le\|Q_{B_i}f\|^2 .
\]
Use (5) for \(h\) and add the two contributions to \(\operatorname{Var} f\). The product-law case satisfies the same inequality by independent-coordinate tensorization, assigning each coordinate to one containing block. Thus, for \(M\ge 2+\lceil4/(1-\tanh(b_\beta/4))\rceil\),
\[
 \operatorname{Var}_C f\le K_\beta\sum_i\mathbb E_C\operatorname{Var}_{B_i} f,
 \qquad K_\beta=1+24e^{3b_\beta/2}
           \le C(2+\beta)^q e^{9\beta/2}.                               \tag{7}
\]
This is uniform in the entire exterior field and the length of the line in that range. All couplings on and off the line are the original isotropic Wilson coupling.

**PROVED (comparison on the full four-torus).** Partition the links into the lines just specified, over all base lines and link orientations. Write \(\mathcal E_5(f)=\sum_{C,i}\|Q_{B_i}f\|^2\) and \(\mathcal E_{\rm line}(f)=\sum_C\|Q_C f\|^2\), now in the ordinary Wilson law. Apply (7) conditionally on each line exterior and integrate. This gives
\[
                    \mathcal E_{\rm line}(f)\le K_\beta\mathcal E_5(f).\tag{8}
\]
Each link belongs to at most two of the five-link sets. Their commutation count is at most \(2\cdot5\cdot19=190\), counting even a set itself in this upper bound. They lie at one base time, so (4) applies with \(D'=190\) and the variational constant for \(\mathcal E_5\). Equations (7)–(8) require no gauge-invariance restriction on \(f\).

**PROVED (physical scale of the estimate).** Measure length in fixed physical units. Suppose \(\beta_j\to\infty\) and \(\liminf_j\log(1/a_j)/\beta_j>9/4\). On a line of fixed positive physical length, with lattice periods divisible by six, the size condition in (7) holds eventually because its right side grows at most polynomially times \(e^{3\beta_j/2}\). It also holds in the volume-first limit at each cutoff. Then \(a_j^2K_{\beta_j}\to0\). In particular every sequence of unit vectors with \(\mathcal E_5(f_j)=O(a_j^2)\) satisfies
\[
                  \sum_C\|f_j-\mathbb E[f_j\mid C^c]\|_2^2\to0 .       \tag{9}
\]
The one-loop slope \(3\pi^2/11\) in the Wilson convention \(\beta=4/g_0^2\) would meet this hypothesis, since \(\pi>3\). The slope of the actual tuned trajectory is a premise here. The sum in (9) includes every line of the chosen foliation, with all link orientations, and allows arbitrary dependence of \(f_j\) on the cutoff and the torus.

## Can conditional line estimates be combined?

**PROVED (two neighbouring lines can transmit a bounded physical reading almost perfectly).** Use spatial coordinates 1, 2, 3 and time 4. Take a periodic time length divisible by six and spatial periods at least six. Write \(q=\cos(2\pi/3)+\mathbf i\sin(2\pi/3)\) in unit quaternions. Consider the following admissible Wilson configuration:
\[
       U_1=U_2=U_4=1,\qquad U_3(x,t)=q^t .                              \tag{10}
\]
Choose two adjacent lines of 3-links, parallel as sets of base points to direction 1, at time zero, the same third coordinate, and adjacent second coordinates. Fix the exterior of these two lines to (10). If their variables are \(u_s,v_s\), with period \(n\) along direction 1, the conditional law is exactly
\[
 \pi(du,dv)\ \propto\ \exp\left\{\beta\sum_{s=1}^n
       (u_s\cdot u_{s+1}+v_s\cdot v_{s+1}+u_s\cdot v_s)\right\}
                 \prod_s du_s\,dv_s .                                    \tag{11}
\]
The longitudinal plaquettes give the two chain terms. The plaquette joining the lines gives the rung. At each unknown link the remaining neighbour in direction 2 is 1 and the two neighbours in time are \(q,q^{-1}\). Their sum is zero. This uses all six incident plaquettes at full Wilson coupling. The sheet construction in `gap-solve22-astra62.md`, (1), is prior work on conditional Wilson ribbons. Here the exterior cancels the fields simultaneously for every adjacent pair of lines in the plane.

**PROVED.** Let \(H\) be the sum over the \(3n\) edges of this ladder of \(1-x\cdot y\), and \(Z_b=\int e^{-bH}\) with probability Haar reference. For \(\beta\ge2\),
\[
                        \mathbb E_\beta H\le Cn/\beta .                  \tag{12}
\]
For the upper bound on \(Z_{\beta/2}\), discard every edge outside a spanning tree. Leaf integration gives at most \((C\beta^{-3/2})^{2n-1}\), since the radial Haar factor on \(S^3\) is proportional to \(\sin^2\theta\,d\theta\) and \(1-\cos\theta\ge2\theta^2/\pi^2\). For the lower bound on \(Z_\beta\), leave one spin free and put the remaining \(2n-1\) spins within angular distance \(\beta^{-1/2}\) of it. Their product Haar probability is at least \((c\beta^{-3/2})^{2n-1}\), by \(\sin\theta\ge 2\theta/\pi\) there. On this set \(\beta H\le6n\). The ratio of the two bounds gives \(\log(Z_{\beta/2}/Z_\beta)\le C'n\). The derivative of \(-\log Z_b\) is the decreasing function \(\mathbb E_b H\). Integration from \(\beta/2\) to \(\beta\) proves (12).

**PROVED.** Translation along the ladder gives \(1-\mathbb E(u_s\cdot v_s)\le C/\beta\). Law (11) is invariant under simultaneous \(O(4)\) rotations. For any fixed unit four-vector \(d\), both \(u_s\cdot d\) and \(v_s\cdot d\) have mean zero and variance \(1/4\), and their correlation coefficient is \(\mathbb E(u_s\cdot v_s)\). These tests can be taken to be genuine local gauge-invariant, centre-neutral functions before conditioning. For each unknown link take the normalized trace of the rectangular Wilson loop through its parallel return link two time steps away, with the temporal sides at the two ends. At (10) this return link is \(q^2\) and the temporal sides are 1, so the readings are precisely the two projections with \(d=q^2\).

**PROVED (the failing estimate).** For two adjacent line labels \(i,j\) let \(c_{ij}(X)\) be the maximal absolute correlation between readings of the two lines in their conditional joint law given their common exterior. The displayed loop readings, with their exterior legs fixed, give \(c_{ij}(X)\ge1-C/\beta\) at (10), for **both** neighbours in direction 2 of every line in the chosen plane. At each finite volume the conditional means, variances and covariance of these particular loops are continuous functions of the exterior. Their variances are nonzero there. Thus the simultaneous strict lower bounds with any slightly larger error hold on an open set of positive Wilson measure. In particular a uniform weighted row-sum bound \(\sum_{j\sim i}c_{ij}(X) w_j/w_i<1\) for every row and almost every exterior, with positive weights, is false at sufficiently large \(\beta\). On this cyclic family take a row of least weight. Its two neighbours alone give a sum exceeding one. This counterexample concerns absolute conditional pair influences. It gives neither a low eigenvalue of the full Wilson dynamics nor a gapless physical state.

## Testing whether the obstruction is confined to rough plaquettes

**PROVED (removing one class of bad configurations from a slow vector).** At (10) each link separately maximizes its conditional Wilson density. The six staples sum to six times the link in directions 1 and 2. In directions 3 and 4, the four aligned terms plus the conjugate temporal-spatial pair give three times the link. There is nevertheless a profitable move on a single time slice. Let \(S\) contain the 3-links based on a \(b\)-by-\(b\) square in coordinates 1 and 2 at fixed third coordinate and time zero, without wrapping. Write \(Y_S=\sum_p w_p\) over plaquettes meeting \(S\) in an odd number of links, with \(w_p=\tfrac12\operatorname{Tr}U_p\). At (10) the \(2b^2\) temporal terms have \(w_p=-1/2\), and the \(4b\) spatial boundary terms have \(w_p=1\). Thus \(Y_S=-b^2+4b\). For every exterior and \(s>0\),
\[
          \mu(Y_S\le-s\mid S^c)\le e^{-2\beta s}.                       \tag{13}
\]
Multiplying every link of \(S\) by the central element \(-1\) is a Haar-preserving involution taking the event to \(Y_S\ge s\) and multiplying its Wilson weight by at least \(e^{2\beta s}\).

**PROVED.** Enlarge the update family by all spatial translates and time translates of the square with \(b=6\). The commutation count is finite independently of the torus, so (4) still applies to the enlarged variational form \(\mathcal E\). For \(\|f\|_2=1\), the squared mass of \(f\) on \(Y_S\le-s\) is at most \(2\|Q_S f\|^2+2e^{-2\beta s}\). Split \(f=Q_S f+P_S f\) and use (13) on the second term. On an \(N^4\) torus with \(N>12\), the mass on the union of these events over all translates is therefore at most
\[
                       2\mathcal E(f)+2N^4e^{-2\beta s}.                \tag{14}
\]
Taking \(s=10\) includes a neighbourhood of (10), for which the sum is \(-12\). At fixed physical side and \(\log(1/a)/\beta\to3\pi^2/11\), the second term is \(o(a^2)\), since \(6(3\pi^2/11)<20\). This estimate applies to cutoff-dependent normalized vectors and to rare-event indicators. The union bound has the displayed volume dependence. To use (13) on a fixed patch one can take the volume limit first.

**GUIDE.** This suggests estimating conditional influences only on fields with small local action. I tested that repair at an exactly flat SU(2) connection. The following calculation uses continuous, centre-neutral Wilson-loop tests in the conditional space.

**PROVED (flat-background obstruction).** On an even four-torus of side \(n\) put \(U_1=q_0^{1/n}\) at every site, where \(q_0=\exp(\pi\mathbf i/4)\) and the indicated root uses that angle divided by \(n\). Put every transverse link equal to 1. All plaquette holonomies are 1. For lines running along coordinate 1 with link orientations in \(\{2,3,4\}\), consider pairs that share an elementary plaquette of the transverse three-dimensional lattice. Every one of these lines has twelve such neighbours, three in each of four plaquettes. For sufficiently large \(n\) and \(\beta\) the conditional maximal correlation for **each** of these pairs exceeds \(1/10\) at this same exterior configuration.

**PROVED (conditional law at the flat connection).** For each such pair write the unknowns on the two lines as \(u_s,v_s\). The common transverse plaquette supplies one interaction per \(s\). Up to inverting one of the two quaternion variables along its whole line it is \(u_s\cdot v_s\). Each of the other three transverse plaquettes at each link contributes its real coordinate. The two plaquettes along coordinate 1 give the chain bonds with an orthogonal rotation \(R=\operatorname{Ad}(q_0^{\pm1/n})\) between consecutive spins. Quaternion inversion preserves these dot products, commutes with conjugation and leaves the real coordinate fixed. Thus the nonnegative action in units of \(\beta\) is
\[
 H=3\sum_x(1-\operatorname{Re}u_x)
       +\sum_{xy}(1-u_x\cdot R_{xy}u_y),                               \tag{15}
\]
where \(x\) runs over the two rows of the ladder, \(R_{xy}=I\) on rungs, and the longitudinal rotations tend to the identity as \(n\to\infty\). The notation \(u_x\) includes both rows. The conditional density is proportional to \(e^{-\beta H}\).

**PROVED (local weak-coupling limit, uniform along sequences of growing lengths).** In logarithm coordinates \(X_x=\sqrt\beta\log u_x\in\mathbb R^3\) choose the quaternion angle in \([0,\pi)\), ignoring the Haar-null antipode. Dropping the bond deficits in the upper bound for \(Z_{\beta/2}\) and putting all spins in the identity cap of radius \(\beta^{-1/2}\) in the lower bound for \(Z_\beta\) gives \(\log(Z_{\beta/2}/Z_\beta)\le Cn\) by the radial estimates in (12). All longitudinal rotations fix 1. Hence \(\mathbb E H\le C'n/\beta\). Translation along the rows and \(1-\cos\theta\ge2\theta^2/\pi^2\) imply a common bound on \(\mathbb E|X_x|^2\).

**PROVED.** Along any sequence \(n,\beta\to\infty\) this second-moment bound makes the finite-dimensional distributions tight. In a fixed interval of the ladder, with the two neighbouring boundary columns prescribed in bounded logarithm coordinates, the conditional distribution converges to the Gaussian with onsite energy \(3|X_x|^2/2\) and edge energies \(|X_x-X_y|^2/2\). Indeed the Taylor expansion of each term of \(\beta H\) gives the displayed quadratics uniformly on compact sets, since \(R_{xy}\to I\). In logarithm coordinates the normalized Haar Jacobian, apart from its constant and the scale factor \(\beta^{-3/2}\), is \((\sin\theta/\theta)^2\le1\). The onsite term dominates \(c\sum |X_x|^2\) throughout the integration domain. The normalizers are bounded below on compact boundary sets by integrating over a fixed unit ball in every internal coordinate after rescaling. This proves uniform convergence of the conditional expectations of bounded continuous cylinder tests there. The chance of boundary data outside a fixed large compact set is small uniformly, by the moment bound. Passing the conditional identities against bounded continuous exterior cylinder tests to a diagonal weak limit gives these Gaussian conditional laws in every finite interval.

**PROVED.** These conditional laws determine every such limit. For one colour the precision on the infinite ladder is \(6I-A\), with \(A\) its adjacency matrix of degree three. In a finite interval, the conditional means solve \(m_x=\sum_{y\sim x}m_y/6\) using the given exterior values at the ends. Iterating, the influence on a fixed site of boundaries at distance \(h\) is bounded in \(L^2\) by \(C2^{-h}\), since each internal iteration has row sum at most \(1/2\) and the boundary second moments are bounded. The conditional covariance is \((6I-A_{\rm int})^{-1}\), whose geometric series converges to \((6I-A)^{-1}\) at each fixed pair as the interval expands. Taking expectations of Gaussian characteristic functions therefore gives the centered Gaussian with this covariance, independently for the three colours. All subsequences give the same local laws.

**PROVED (the coefficient).** In the Fourier coordinate along the rows the two-by-two precision on one colour has diagonal \(d(k)=6-2\cos k\) and off-diagonal \(-1\). Hence the correlation coefficient between the two variables at the same position on opposite rows is
\[
 \frac{\int_{-\pi}^{\pi}(d(k)^2-1)^{-1}\,dk}
      {\int_{-\pi}^{\pi}d(k)(d(k)^2-1)^{-1}\,dk}\ \ge\ \frac18 .        \tag{16}
\]
The sign can reverse when one row was inverted. A fixed odd clipping of the linear test at a sufficiently large level has absolute Gaussian correlation greater than \(1/10\), by \(L^2\) convergence as the clipping level increases. Use this bounded clipping of \(\sqrt\beta\,\operatorname{Im}_{\mathbf i}u_s\) on the Wilson ladder. The rescaled imaginary component and the corresponding logarithm component agree in the limit on compact rescaled sets. The convergence just proved carries both variances and the covariance of the clipped readings. This proves the coefficient bound along all sequences with both parameters tending to infinity. There are only the finitely many orientation and inversion conventions just described.

**PROVED (gauge tests and small plaquettes).** A short transverse rectangle can be chosen through one tested link with all its other edges outside either tested line. Of the four transverse plaquettes through that link only one contains the other line. At the flat exterior its loop holonomy is the tested quaternion or its inverse. The loop going twice around coordinate 1 from its base has fixed holonomy \(q_0^2=\mathbf i\) and uses only exterior links. The real trace of the product reads the required imaginary component up to sign. The test is gauge invariant and invariant under every centre flip. The twelve neighbours all belong to the transverse line family. Its row of least weight thus has weighted sum greater than \(12/10\), even on this absolute action minimum. This concerns the conditional pair criterion for full lines.

**PROVED (contractible tests arbitrarily close to the same minimum).** At fixed sufficiently large \(n,\beta\), multiply the prescribed 1-links by \(\exp(\epsilon(-1)^{x_2}\mathbf i)\), leaving all transverse links equal to 1. All plaquettes are within angle \(2\epsilon\) of the identity. A nearby \((1,2)\) plaquette away from both lines now has exterior holonomy \(J=\exp(\pm2\epsilon\mathbf i)\). Carry it to the tested base along exterior links. Such a path can be chosen in the transverse grid with the two tested edges deleted. A blocked edge can be bypassed around a unit square, using a perpendicular side avoiding the second blocked edge. The reference plaquette can be placed a fixed number of transverse steps away. All prescribed links commute with \(\mathbf i\). If \(R_0\) is the short transverse plaquette through the tested link, the difference of the real traces of \(JR_0\) and \(J^{-1}R_0\), normalized using \(w=\tfrac12\operatorname{Tr}\) and divided by \(2\sin(2\epsilon)\), gives the same imaginary reading up to sign. These loops are contractible. On the prescribed exterior the normalized tests, before clipping, read the same coordinate for every nonzero \(\epsilon\). At this finite volume the conditional ladder integrals are continuous as \(\epsilon\downarrow0\), so all the strict pair bounds persist for sufficiently small \(\epsilon>0\). For each such fixed \(\epsilon\) continuity supplies an open neighbourhood of positive Wilson probability. The plaquette bound on that neighbourhood can be made arbitrarily small. Thus excising fields detected by (13), or requiring arbitrarily small plaquettes, does not establish absolute row-sum contraction. The conclusion quantifies over exteriors, without any estimate on how frequently these nearly flat fields occur.

## Cubes and a joint cutoff and volume limit

**PROVED (diffusive cube criterion).** Let \(P_x\) integrate the links based in \(x+[0,b)^4\) on an even four-torus of side \(N\ge8b\), with integers \(b\ge1\). Suppose, on the whole chosen centered invariant space,
\[
 b^{-4}\sum_x\|(I-P_x)f\|^2\ge\omega\|f\|^2,\qquad 0<\omega\le1.       \tag{17}
\]
This is the full cube form used by Bhattacharjee, Bhattacharya, Lockwood and Romanov. Partition each coordinate circle into intervals of sizes in \([b,2b)\), using intervals of length \(b\) and adding the remainder to the last one. For each product cell \(A\) take the larger box \(D_A\) consisting of that cell and its successor in each coordinate, meaning the product of the four two-interval unions. Every cube starting in \(A\) is contained there, and at most \((2b)^4\) cubes start in \(A\). Monotonicity of conditional variance under larger updates gives \(\sum_A\|Q_{D_A}f\|^2\ge(\omega/16)\|f\|^2\). Two large-box updates commute if they share neither a link nor a plaquette interaction. For each box, every other noncommuting box starts within three cell indices in all four directions, giving the uniform bound \(D_0=7^4\) on their number. Greedy colouring uses at most \(L=D_0+1\) colours.

**PROVED.** A sweep \(W\) of all boxes in colour order satisfies \(\|W\|^2\le(1+\omega/(16D_0^2))^{-1}\) on this space by the telescoping proof of (2). One colour integrates conditionally independent interiors and extends time support by at most \(h_b=4b+2\) slices. Indeed each interval union has length less than \(4b\), and the plaquettes read at most one further base time. As in (3), only the boxes meeting the current support need integrating. For \(2Lh_b k<d\), applying the same Chebyshev argument to \(W^*W\) gives the connected-correlation bound with exponent \(-2k\operatorname{arsinh}(\sqrt\omega/(4D_0))\). Thus the exponential rate per lattice slice may be taken to be
\[
 v_{b,\omega}=\frac{\operatorname{arsinh}(\sqrt\omega/(4D_0))}{Lh_b}
             \ge c\frac{\sqrt\omega}{b} .                              \tag{18}
\]
Rounding \(k\) down in this estimate costs an absolute multiplicative constant. At a cutoff, the prefactor is at most that constant times the two centered \(L^2\) norms. Here (17) was used on the vectors produced during the sweep. A cyclic estimate for just the initial observable is a different input.

**PROVED (finite-torus transfer to the diagonal limit, under explicit growth and matching).** Suppose \(a_j\downarrow0\), \(a_jN_j\to\infty\), and (17) holds on the actual fine-field tori in this sequence, with \(\liminf_j v_{b_j,\omega_j}/a_j=m>0\). Suppose each fixed matched physical observable is represented by a bounded slab functional \(F_j\) of bounded physical thickness, its centered reflected diagonals converge at positive physical separations, and
\[
                  \log^+\|F_j\|_\infty=o(a_jN_j).                       \tag{19}
\]
For a total family in a reconstructed vacuum theory, its centered Hamiltonian spectrum starts at least at \(m\). A polynomially divergent source norm satisfies (19) if \(a_jN_j/\log(1/a_j)\to\infty\). This implication concerns the matched joint limit.

**PROVED (positive interpolation).** Write \(T\) for the positive Wilson transfer in the spatial magnetic half-weight convention. Its positivity follows from the positive one-link character coefficients and orthogonal vertex-gauge projection, and its periodic trace from integrating the time links. Credit for the corresponding formulas GL3 and GL8 in outline 2197–2214, 2313–2335 belongs to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Cut a slab of width \(w\) with half spatial weights at its ends. Its kernel with the bounded insertion is obtained by integrating the interior at fixed endpoints. Reversing time with conjugation gives its adjoint by invariance of Haar and of the action. The empty slab gives \(T^w\). Subtract the periodic mean times \(T^w\) to obtain the centered insertion \(A\). With \(p=N-2w\), positive clear gaps of \(k\) and \(p-k\) slices on its two sides give diagonal
\[
 u(k)=\operatorname{Tr}(A^*T^k A T^{p-k})/\operatorname{Tr}T^N .
\]
This follows by multiplying the four endpoint kernels and integrating the seam variables. The earlier note `gap-assume-opus.md`, §3.2, already observes torus log-convexity. Explicitly the trace numerator is a sum of \(|A_{ij}|^2\lambda_i^k\lambda_j^{p-k}\) with nonnegative eigenvalues. Zero eigenvalues contribute nothing at interior separations. Hölder on this sum bounds an intermediate value by the geometric interpolation of the two endpoint values.

**PROVED.** For fixed positive clear separations \(s<t\), take matched lattice gaps \(k_s,k_t\) with \(a_jk_s\to s\), \(a_jk_t\to t\). Take \(k_*\) within two slices of \(p/2\), using allowed reflection parity. The cyclic distance between the observed supports there is at least \(k_*-O(1)\). By (18),
\[
 u_j(k_*)\le C\|F_j\|_\infty^2 e^{-v_{b_j,\omega_j}(k_*-O(1))}.
\]
Interpolate between \(k_s\) and \(k_*\) with exponent \(\theta_j=(k_t-k_s)/(k_*-k_s)\) on the far endpoint. Then \(\theta_j\to0\), \(\theta_j\log^+\|F_j\|_\infty\to0\) by (19), and \(a_j\theta_j k_*\to t-s\). This gives \(u(t)\le u(s)e^{-m(t-s)}\), first with any finite lower rate below \(m\), and then by a limit. If \(u(s)=0\) the same interpolation gives zero. The positive continuum spectral measure and totality give the assertion as after (4). No thermal multiplicity bound, nor a cutoff-uniform contact norm, enters this interpolation. For the published straight-path estimate, (17) for the **fine** field and full continuum matching still have to be supplied.

## Which observed fields can carry a slow Wilson update?

**GUIDE.** The straight-path law in the published cube argument is much smoother than the fine gauge field. Row 1161, `gap-solve9-astra62.md`, (23), constructs private links for all straight windings on one four-torus. Row 1227, (19)–(22), bounds a trace for the physical transfer observed through such windings. I use the actual **four-dimensional fine-field** single-link form (1). The conditional near-Haar estimate used below is prior work. See also `gap-mini-solve-p-fable.md`, Proposition H and Lemma NULL, for the coarse form and one exterior.

**PROVED (fine-field Dirichlet bound on a whole observation algebra).** Let \(Y_1,\ldots,Y_P\) be oriented path products. Suppose each path has \(M\) private links traversed once, none appearing on another path, and no plaquette meets two private links in their union. Given all remaining links, they are independent translated central SU(2) variables with tilt at most \(6\beta\). Set \(B=1+6\beta\). The dimension-\(d\) Fourier multiplier of one such link has norm at most \(e^{-(d-1)/B}\) for \(d\ge2\), by row 1145, (1), used in row 1161, (23). Fixed intervening group factors and reversal preserve the norm bound. Thus a product containing \(m\) such independent links has Haar density within \(\eta(m/B)=\sum_{d\ge2}d^2 e^{-(d-1)m/B}\) of 1, by character inversion. Assume \(M\ge4\), \(\eta(\lfloor M/2\rfloor/B)\le1/2\) and \((1+\eta(M/B))^P\le 5/4\). Then for every square-integrable \(F(Y)\),
\[
       \sum_e\|Q_e F(Y)\|^2\ge c\,\frac{M}{1+\beta}
                                  \operatorname{Var}_\mu F(Y).         \tag{20}
\]
The left side updates the original Wilson links while keeping their actual exterior fixed.

**PROVED.** Choose a private link \(e\) among the last \(\lfloor M/2\rfloor\) on path \(i\). Write \(Y_i=A u B'\), where \(u\) is the oriented link. Compute the single-link variance by drawing \(u,u'\) independently from its conditional law and halving the mean squared difference. Conditional on the nonprivate links, the suffix and other paths, the prefix \(A\) has density at least \(1/2\) against Haar by the preceding estimate. Replace its integral by this lower Haar bound, which is valid for the nonnegative integrand. With \(A\) Haar, \(y=A u B'\) is Haar independently of \(u,u'\), and the second reading is \(y (B')^{-1}u^{-1}u' B'\). The convolution by the latter increment has Fourier norm at most \(e^{-2/B}\) on every nontrivial representation, by independence of the two draws and the squared one-link multiplier bound. Thus the integrated half squared difference is at least \((1-e^{-2/B})\operatorname{Var}_{H,i}F\) for the fixed other readings, before accounting for the factor \(1/2\). The law of the other readings, given the nonprivate links, dominates \((1-\eta(M/B))^{P-1}\) times their product Haar law. This factor is bounded below by an absolute positive constant: Bernoulli's inequality gives \(P\eta(M/B)\le1/4\) from the hypothesis. The full law of \(Y\) is bounded above by \(5/4\) times product Haar. Sum the bounds over the private links and use product variance tensorization in Haar, and then \(\operatorname{Var}_\mu F\le(5/4)\operatorname{Var}_{H^{\otimes P}}F\). Finally \(1-e^{-2/B}\ge c/B\) for \(B\ge1\). This proves (20).

**PROVED (overlap with arbitrary slow vectors).** Split the private links on each path into \(k=\lfloor M/m\rfloor\ge1\) disjoint batches of \(m\) links, and denote the union for batch \(j\) over all paths by \(S_j\). Write \(\delta=(1+\eta(m/B))^P-1\le1/4\). Given the exterior of *any one batch*, the density of the whole reading lies between \(1-\delta\) and \(1+\delta\) against the same product Haar probability. Indeed the lower product bound follows from \((1-x)^P\ge1-Px\) and \(Px\le(1+x)^P-1\). The unconditional density obeys the same bounds. For every centered \(F(Y)\), this gives \(\|P_{S_j}F\|_2\le 2\delta(1-\delta)^{-1/2}\|F\|_2\), by subtracting the unconditional expectation in the Haar integrals. If \(v\) is any centered fine-field vector, test it against a unit such \(F\) and move \(Q_{S_j}\) to \(v\) in the complementary inner product. The private links in one batch are conditionally independent, hence \(\|Q_{S_j}v\|^2\le\sum_{e\in S_j}\|Q_e v\|^2\) by conditional tensorization. The batches are disjoint. Choosing the batch with smallest energy proves
\[
 \|\mathbb E[v\mid Y]\|_2
 \le 3\delta\|v\|_2+
          \left(k^{-1}\sum_e\|Q_e v\|_2^2\right)^{1/2}.                 \tag{21}
\]
This permits a different normalized test at every cutoff and controls its projection onto all functions of \(Y\).

**PROVED (applications).** On the \(N^4\) torus with \(4\mid N\), row 1161 supplies \(M=\lfloor N/8\rfloor\) private links for each of the \(4N^3\) full straight windings. On a coordinate grid of spacing \(b\mid N\), \(b\ge4\), the \(P=4(N/b)^4\) straight coarse edges instead have \(M=b-2\) private links each: omit the first and last link. Adjacent coarse paths meet only at endpoints, and no two retained links lie on a common plaquette. For either experiment, \(\eta(x)\le C e^{-x}\) for \(x\ge1\) by summing the convergent series. For fixed \(A_0>0\) take \(m=\lceil C_{A_0}(1+\beta)\log(2+N)\rceil\) large enough to make \(\delta\le N^{-A_0}\). When \(M/m\to\infty\), (20) supplies the lower rate of order \(M/(1+\beta)\) on these readings, and (21) controls their overlap with every slow mode of the full auxiliary process. The complement may retain curvature observables and arbitrary joint functions of omitted links.

## Testing the remaining estimate

**PROVED (where coarse-path conditioning leaves the variance).** For any centered \(f\) in (21), denote its single-link energy by \(E(f)\). Orthogonal decomposition and (21) give
\[
 (1-18\delta^2)\|f\|^2
            \le \mathbb E\operatorname{Var}(f\mid Y)+(2/k)E(f).         \tag{22}
\]
In particular take \(\delta\le1/8\). To obtain a rate of order \(a^2\) it suffices to bound the **averaged conditional variance of every fine observable** by \(C a^{-2}E(f)\), uniformly at the required tori and cutoffs. The converse follows from conditional variance being at most total variance. Equations (20) and (21) handle the observable part that survives averaging over the fine links at fixed paths. They leave the term on the right of (22) for the fine observables themselves.

**PROVED (a test on the ordinary Wilson measure, given the covariance of row 1231).** Let \(r=\lfloor\beta^\delta\rfloor\), \(0<\delta<1/48\), on even four-tori with \(\beta\to\infty\) and \(\beta\le B_0\log N\) for a fixed \(B_0\). Row 1231, `gap-solve26-astra62.md`, (7), (11) and the finite-torus statement following (35), gives a bounded centered, centre-neutral, single-slice Wilson test with covariance at distance \(\lfloor sr\rfloor\) tending to \(K(s)\) for each fixed \(s\ge0\), where \(K(0)>0\) and \(K(s)\asymp s^{-8}\) for large \(s\). For any whole-sector variational lower bound \(\gamma\) as in (2), including the five-link families with uniform commutation count,
\[
                              r^2\gamma\longrightarrow0.                \tag{23}
\]
Otherwise a subsequence has \(r\operatorname{arsinh}(\sqrt\gamma/D)\ge c>0\), since \(r\to\infty\). In (3) choose the largest admissible \(k\). At each sufficiently large fixed \(s\) pass to that subsequence. The cyclic time distance is \(\lfloor sr\rfloor\) eventually, giving \(K(s)\le 2K(0)e^{-c' s}\), contrary to its power law. This sharpens the rate test for these update families at a shrinking physical wavelength. Since \(r a\to0\) on a one-loop trajectory, (23) remains compatible with \(\gamma\) of order \(a^2\).

**PROVED (why even excellent conditional line relaxation need not give a physical gap).** As a separate exact comparison, consider three independent real Gaussian one-forms on a periodic four-lattice with precision \(d^*d+\mu^2 I\), \(\mu>0\); here \(d\) is the oriented plaquette curl. Give a fixed transverse link orientation a coefficient \(v_e=\cos(2\pi t/N)\) at every base time \(t\) and set all other coefficients to zero, choosing a spatial orientation different from the line direction 1. Then \(v\) is divergence free and its coefficients sum to zero on the torus, and
\[
 (d^*d+\mu^2 I)v=\lambda v,\qquad \lambda=\mu^2+4\sin^2(\pi/N).
\]
Indeed only the time differences contribute to its curl and the backward time difference gives the displayed multiplier. In one colour, \(X=\sum_e v_e A_e\) has variance \(V=\|v\|^2/\lambda\). Conditional on the exterior of one direction-1 line of the chosen orientation, its precision on that line is the cycle Laplacian plus \((4+\mu^2)I\): the diagonal from six incident plaquettes is \(6+\mu^2\), and the two longitudinal off-diagonals are \(-1\). The conditional variance of \(X\) is therefore \(s_C=\sum_{e\in C}v_e^2/(4+\mu^2)\), because the coefficients are constant along the line. It is zero on updating a line of any other orientation.

**PROVED.** Take \(f=\sum_{h=1}^3(X_h^2-V)\). It is invariant under linearized gauge shifts and common colour rotations. A Gaussian of conditional mean \(m_C\) and variance \(s_C\) has conditional variance of its square equal to \(4m_C^2s_C+2s_C^2\). Since \(\mathbb E m_C^2=V-s_C\), independence of the three colours gives
\[
 \frac{\mathcal E_{\rm line}(f)}{\operatorname{Var} f}
                    \le \frac{2\lambda}{4+\mu^2}.                       \tag{24}
\]
The conditional line's precision stays bounded below by 4 at arbitrarily small \(\mu\). Yet, with \(\mu/a\to0\) and \(Na\to\infty\), the right side of (24) is \(o(a^2)\). The obstruction is a collective fluctuation. Equation (24) is a calculation in the regulated Gaussian model. Its gauge-shift-invariant observables can be used even though the regulator in the probability density breaks gauge-shift invariance. It supplies no conclusion on the existence of such a fluctuation in SU(2) Wilson theory.

**OPEN (Wilson infrared estimate).** For example, in the volume-first formulation it would suffice to prove that for some \(c>0\), at every sufficiently fine tuned cutoff and on an unbounded matching sequence of even tori, the sum of the conditional variances from all spatial lines is at least \(c a^2\operatorname{Var}_\mu f\) for every centered gauge-invariant \(f\) invariant under the torus centre flips. Applying this to the full vacuum representation requires totality of the matched observables there. For updates of whole lines the time-local proof of (4) still applies. Their commutation count is at most 18 because any line sharing a plaquette with a given line already shares one with its representative link after a translation along the line. One can instead use (17)–(19) on a matched diagonal sequence. The full matched nontrivial Yang–Mills construction is a further open premise of both implications. The single-line and observed-path estimates do not bound collective neutral fluctuations at fixed physical wavelength. The absolute pair-influence argument fails even near flat fields. I have no signed or averaged Wilson estimate that controls the remaining fluctuations.

**GUIDE (provenance).** This is an author-side research argument at pin `659db0a48`. The labels refer to the hand arguments and the premises displayed beside them. No numerical proof step or independent proof check was used. The note grants no scientific status.

RESULT — OPEN. I did not prove the Jaffe–Witten SU(2) mass gap. A diffusive lower bound on Wilson heat-bath relaxation would suffice under the stated reconstruction hypotheses. I obtained conditional single-line relaxation and fine-field bounds for straight-path observables, and found a flat-background obstruction to summing absolute line influences. The uniform infrared bound on collective neutral modes and the full continuum construction remain open.
