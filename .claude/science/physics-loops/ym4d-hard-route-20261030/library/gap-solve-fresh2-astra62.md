## Repo search

**GUIDE.** Codex research, FINISH row 1270, started 2026-11-20 at 11:57 UTC on pinned checkout `b7e73cdc72362cc0c33e00569a975cd4c9a3a04d`. The row-specific prior file is absent. The November 8 search covers main and four PRs. Its directly relevant lead is the one-step Wilson-loop calculation on the soft route. I checked that calculation, the gap part and the indexed outline against the full spectral target.

**OPEN.** The Jaffe–Witten target remains open. It requires a nontrivial continuum SU(2) Yang–Mills vacuum theory on \(\mathbb R^4\), with \(\ker H=\mathbb C\Omega\), nonempty excited space and \(\operatorname{spec}(H|_{\Omega^\perp})\subset[m,\infty)\) for some \(m>0\) in physical units. Bound (5) concerns adjoint colour transport in the Wilson measure. Equation (19) identifies the gauge-invariant correlation for which a physical rate is still missing. This is a research note with no status grant.

**GUIDE.** I checked the following primary passages against the lead’s November 8 search and row 1218’s follow-up. None supplies a cutoff-uniform physical decay rate for the full local algebra.

| Source | What the cited passage gives |
|---|---|
| GUIDE · PR 10114, `f76f6c649c`, soft-route `MASS_GAP_LOCAL_BLOCK_ASTRA.md` 4–14, 106–149 | A finite-coupling positive one-step correlation for a spatial loop. Its strong-coupling contraction uses bare `beta <= 1/32`. |
| GUIDE · Grok, PR 10133, `89faef229f`, soft-route `MASS_GAP_CROSSOVER_REDUCTION.md` 77–86 | The crossover estimate and transport of sources are explicit open inputs. |
| GUIDE · PR 10134, `1e70c7211a`, `library/mass-gap-interface.md`, I1–I5 | Separates nonzero excitations, the lower spectral edge and Yang–Mills identification. |
| GUIDE · PR 10141, `a2f6a430e2`, `research/ym4d/library/fp1.md` 299–315 | Controls a constrained classical fluctuation at one scale. |
| GUIDE · Main, `8b11ae2bb9`, `research/mass-gap/library/gap-phys-seed.md` 305–329 | ZD-c propagates a physical thermal seed under its stated hypotheses. The required Wilson seed remains an input. |

**GUIDE.** The outline index, chunks 01, 29 and 30 and the neighbouring obligation rows point to outline lines 581–599, 31858–31882 and 32486–32490. I checked these and CA-I 2704–2713, 3213–3222 at `31a47c543775`. The scalar action-density reconstruction has limited observable scope, and the account expressly leaves the positive spectral threshold open. Credit for the outline and complete account belongs to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. The index for CA-I 4.12–4.19 addresses the ultraviolet induction. I found no target entry under mass gap, physical Hamiltonian or infrared in `library/open-registry.md`. Row 1270 explicitly assigns this independent attempt. Targeted searches of the five fetched refs outside this lane also returned no matches for the combinations of Wilson-averaged adjoint Green functions or opposite-link double scores used below. [Outline, scalar sector and spectral support](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L31858-L31882) · [Complete account I, scope of the theorem](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2704-L2713)

**GUIDE.** The source comparison in `prior/gap-onebound-read-sol.md` credits Deep Bhattacharjee, Ushashi Bhattacharya, James Montgomery Lockwood, Tristan Romanov, Ikailo John Sessford and Sanjeevan Singha Roy for the thermal-window route, the first four authors for the cube-dynamics route, and Zeng Chunping for the common-rate and tunnelling approaches. I use that reading for provenance. Those estimates retain an infrared input. The competing centre-flux branch has already been addressed for local sources in row 1179. I take that distinction from the repository.

## Propagation of colour in the Wilson measure

**GUIDE.** I will try to obtain infrared decay from the noncommutativity of parallel transport. The first object is the nearest-neighbour adjoint connection Laplacian on the actual four-dimensional Wilson field. The second is the physical time-transfer operator on gauge-invariant observables. An estimate on the first will need a derivation connecting it to the second. I will test that step explicitly.

**GUIDE.** The two-plaquette pinning estimate is already on file. In `gap-crux2-astra62.md`, (3)–(7), let two squares in the first coordinate plane meet only at their base site, one in its positive quadrant and one in its negative quadrant. Their adjoint holonomies are rotations \(A_1,A_2\) of \(\mathbb R^3\). Call the site good if
\[
 \min_{|v|=1}\left(|(I-A_1)v|^2+|(I-A_2)v|^2\right)
       \ge \delta_\beta,\qquad \delta_\beta=[8(1+6\beta)]^{-1}.
\]
Conditionally on links outside the cell of side three, its Wilson probability is at least one half. The proof there conditions one loop edge at a time. Its tilted Haar law sends any given axis into a spherical cap of chord radius \(2u\) with probability at most \(4(1+6\beta)u^2\). Two disjoint chords control the minimum over axes. Earlier deterministic frame estimates are in rows 1011 and 1018. I reuse the conditional lower bound with its actual conditioning. I do not assume independence of the cells.

**GUIDE.** Row 1249, `gap-mini-solve-ac-opus.md` §§3.1–3.6, treats a Dirichlet colour Green function by a deterministic spectral lower bound, following Combes and Thomas. Row 1141, `gap-crux2-astra62.md` (2), gives a high-probability finite-box bound whose denominator grows with box size. I will seek an expectation of the norm of an individual Green matrix element, uniform in the box size, by cancelling short returning paths before taking norms. This permits rare nearly flat boxes anywhere in the volume.

**PROVED (a scalar walk bound after four steps).** Let \(U\) have an ordinary Wilson Gibbs law at \(0\le\beta<\infty\) on \(\mathbb Z^4\). All expectations below are also valid for the Dirichlet probe in a finite box of a larger Wilson lattice, with the box and its one-link collar embedded without winding. On vector functions define
\[
 (P_U f)(x)=\tfrac18\sum_{y\sim x}T_{xy}f(y),\qquad
 T_{xy}=\operatorname{Ad}U_{xy},\quad T_{yx}=T_{xy}^{-1},
 \qquad L_U=8(I-P_U).
\]
For the Dirichlet probe extend \(f\) by zero and kill paths on exit. Write \(p(x,y)=\mathbf1_{x\sim y}/8\), \(q=p^4(0,0)<1\), \(g_x\) for the good-site indicator above, and \(\eta=\delta_\beta/(6\cdot8^4)\). For all sites of the probe,
\[
 \|P_U^4(x,y)\|\le B_U(x,y),\qquad
 B_U(x,y)=p^4(x,y)-\eta g_x\mathbf1_{x=y}.                       \tag{1}
\]
For \(x\ne y\), sum the norms of the orthogonal path transports. For \(x=y\), retain together one four-step backtracking path and the two oriented squares. Their matrices are \(I,A_1,A_2\). The identity
\[
 |(I+A_1+A_2)v|^2
 =9|v|^2-|(I-A_1)v|^2-|(I-A_2)v|^2-|(A_1-A_2)v|^2
\]
is the cancellation in row 1141, (5). It saves at least \(3-\sqrt{9-\delta_\beta}\ge\delta_\beta/6\) on good sites for unit \(v\). Each path weight is \(8^{-4}\). If any of the three paths exits the Dirichlet box, its entire weight is already missing, which gives (1) too. The comparison is entrywise between scalar nonnegative kernels after taking each matrix norm. Matrix multiplication and the triangle inequality iterate it.

**PROVED (summing the holding times).** Let \(J=(p^4-qI)/(1-q)\), the transition kernel which makes a nonzero jump of at most four lattice steps. Write \(S_i\) for its walk and \(w_x=(1+\eta g_x/(1-q))^{-1}\). On the infinite lattice,
\[
 \sum_{n\ge0} B_U^n(x,y)
  =\frac{1}{1-q}\sum_{l\ge0}
     \mathbb E_x\!\left[\mathbf1_{S_l=y}\prod_{i=0}^l w_{S_i}\right].    \tag{2}
\]
Indeed the sum over repeated holds at a visited site is
\((1-q+\eta g_x)^{-1}\). Each move to a distinct site contributes \((1-q)J\). Every path has one more visited site than moves, counted with repetition, giving (2) by nonnegative summation. For a finite Dirichlet comparison, keep only skeleton paths whose visited sites stay in the box. For an upper bound on that sum one can extend \(g\) by one outside the box and then sum on the full lattice.

**PROVED.** Given a fixed walk segment, choose any subset \(S\) of its visited sites with pairwise disjoint three-site-wide cells. For cells outside the Dirichlet box use the deterministic extension just described. The law of \(U\) is independent of the auxiliary walk. By conditioning successively on links outside each cell, and dropping the other factors, each at most one, one has
\[
 \mathbb E_U\prod_i w_{S_i}\le
 \left(1-\frac{\eta}{2(1-q+\eta)}\right)^{|S|}
 \le \exp\left[-\frac{c_0 |S|}{1+\beta}\right],\qquad
 c_0=(1152\cdot8^4)^{-1}.                                          \tag{3}
\]
Here \(1-q+\eta\le2\) and \(1+6\beta\le6(1+\beta)\). A site inside the box uses actual Wilson links from its cell, including its collar where needed. No estimate on the worst exterior is required beyond the conditional good-site probability already proved for these links.

**PROVED (the average adjoint Green kernel on the Wilson field).** There are absolute \(C<\infty\) and \(c>0\) such that at every finite bare coupling, in lattice units,
\[
 \mathbb E_\beta\|G_U(x,y)\|
 \le C\exp\left[-c\,\frac{|x-y|_\infty}{\sqrt{1+\beta}}\right],
 \qquad G_U(x,y)=\tfrac18\sum_{n\ge0}P_U^n(x,y).                   \tag{4}
\]
This applies in the infinite lattice and to the embedded Dirichlet boxes specified above, with the same constants. The norm is inside the Wilson expectation. The infinite-volume series is an entrywise zero-mass Green function. In a finite Dirichlet box it is the inverse of \(L_U\), since the scalar walk exits almost surely with a fixed positive chance over some finite number of steps from every site.

**PROVED (transience used in (4)).** Put \(G_* = \sup_{u,v}\sum_{j\ge0}J^j(u,v)\). Equation (2) with \(g=0\) identifies this sum with \((1-q)\sum_{n\ge0}p^{4n}(u,v)\). The Fourier multiplier of \(p\) is \(\phi(\theta)=\frac14\sum_{i=1}^4\cos\theta_i\). Fourier expansion of a power and the triangle inequality bound the latter sum by the normalized torus integral of \((1-\phi^4)^{-1}\), times \(1-q\). Its only singularities are the points with all angles zero or all angles \(\pi\). Near either point its integrand is bounded by a constant times the inverse square of the distance, which is integrable in four dimensions. Thus \(1\le G_*<\infty\). This argument, including the last zero to three walk steps, gives absolute convergence of the series defining each entry in (4), even before averaging.

**PROVED (how many different cells a crossing samples).** By a change of coordinate and sign write \(r=y_1-x_1=|x-y|_\infty\). Let \(W=\lceil128\sqrt{1+\beta}\rceil\), \(N=\lfloor W^2/2048\rfloor\), and \(\tau_k\) be the first time the \(J\)-walk reaches first coordinate at least \(x_1+kW\). Its overshoot is at most three. Starting at any \(\tau_k<\infty\), the probability during the next \(N\) steps that the first-coordinate displacement from its new start ever exceeds \(W/4\) is at most \(256N/W^2\le1/8\). Indeed the increments are centered and bounded by four. Stop their square submartingale at the first exit to obtain the maximal inequality, using its terminal second moment at most \(16N\).

For these \(N+1\) positions, the expected number of ordered equal-position pairs is at most \(2G_*(N+1)\), by summing the return probabilities over the time difference. With probability at least \(3/4\) there are at most \(8G_*(N+1)\) such pairs. Cauchy–Schwarz applied to the local visit counts then gives at least \((N+1)/(8G_*)\) different sites. Call this part of the crossing successful when both the displacement and range conditions hold. Its conditional chance is at least \(1/2\) at every start. Greedily retaining a site and removing sites at maximum-coordinate distance at most two yields at least \((N+1)/(8G_*5^4)\) roots in disjoint cells. Roots from different successful crossings are separated because their first coordinates lie between \(x_1+kW-W/4\) and \(x_1+kW+3+W/4\). Success at \(k\) is known by \(\tau_{k+1}\). Reaching that level before the \(N\) steps finish already means failure.

**PROVED (completion of (4)).** Use \(m=\max(0,\lfloor r/W\rfloor-1)\) crossings indexed by \(1,\ldots,m\). For \(m\ge1\), every path to \(y\) reaches level \(m+1\). On such a path the successful cells lie within the path prefix before that level. Since \(N+1\ge8(1+\beta)\), (3) gives a factor at most \(b^{K}\), where \(K\) counts successful parts and \(b=\exp[-c_0/(G_*5^4)]<1\). Applying the Markov property at successive levels gives
\[
 \mathbb E_x[\mathbf1_{\tau_{m+1}<\infty}b^K]
 \le [1-(1-b)/2]^m .
\]
This follows by conditioning the last factor on \(\tau_m\), bounding it by \(1-(1-b)/2\), and repeating. After the final level the expected number of visits to \(y\) is at most \(G_*\). Summing (2) is therefore bounded by \(G_*[1-(1-b)/2]^m/(1-q)\). For \(m=0\) the ordinary transient bound suffices. Appending zero, one, two or three steps shifts the endpoint by at most three and costs at most one in each scalar path sum. Applying (1) to all earlier steps and including the factor \(1/8\) proves (4), since \(W\le129\sqrt{1+\beta}\). The argument averages the Wilson field only over disjoint cells chosen from a free walk. It uses no numerical estimate of a spectral edge.

**PROVED (the power prefactor and resolvent derivatives).** For \(s\ge0\) write \(G_{U,s}=(L_U+sI)^{-1}\) entrywise, using (4)'s definition at \(s=0\). Uniformly in \(s\),
\[
 \mathbb E\|G_{U,s}(x,y)\|\le C(1+r)^{-2}e^{-cr/\sqrt{1+\beta}},
 \qquad \|G_{U,s}(x,y)\|\le C(1+r)^{-2},\quad r=|x-y|_\infty .       \tag{5}
\]
A Gaussian integral near the two maxima of \(|\phi|\) and a geometric bound on their complement give \(\sup_z p^n(0,z)\le C(n+1)^{-2}\). Split a path of \(n\ge2\) steps at \(\lfloor n/2\rfloor\). To reach a site at distance \(r\), either half must travel at least \(r/2\) in the designated coordinate. Its probability is at most \(2e^{-r^2/(8n)}\) by the exponential moment bound \(\mathbb E e^{hX}\le\cosh h\le e^{h^2/2}\) for a symmetric step \(|X|\le1\). Sum that half and bound the other by its supremum, reversing the walk for the second case. Thus \(p^n(0,z)\le C(n+1)^{-2}e^{-r^2/(8n)}\). For \(r\ge1\), times above \(r^2\) contribute \(O(r^{-2})\) to the sum. On the dyadic interval from \(2^{-k-1}r^2\) to \(2^{-k}r^2\) the contribution is at most \(Cr^{-2}2^k e^{-2^k/8}\). The scalar Green bound applies to the probe by pathwise domination and to \(J\) by (2) at \(g=0\). In (4)'s proof stop the crossing argument halfway to the endpoint, taking \(m=\max(0,\lfloor r/(2W)\rfloor-1)\). The remaining free Green function after \(\tau_{m+1}\) costs at most \(C/(1+r)^2\). Small \(r/W\) uses the scalar bound directly. A positive \(s\) weights each path length \(n\) in the series by \((8/(8+s))^{n+1}\), which preserves the equal-length cancellation and all upper bounds.

For \(s>0\), differentiating \((L_U+s)G_{U,s}=I\) in one unit left link direction at \(e=uv\) gives \(\partial_eG_{U,s}=-G_{U,s}(\partial_e L_U)G_{U,s}\). The middle factor has two entries of norm at most two, between \(u\) and \(v\), since \(|[a,b]|\le2|a||b|\) for imaginary quaternions. By Cauchy–Schwarz, each of the two terms at \((x,y)\) is bounded in mean by
\[
 C\,k(x,u)k(v,y),\qquad
 k(x,y)=(1+|x-y|_\infty)^{-2}e^{-c'|x-y|_\infty/\sqrt{1+\beta}},
                                                                    \tag{6}
\]
with \(u,v\) interchanged for the other term. Indeed (5)'s two inequalities bound the second moment of each factor by \(C k^2\) after halving the exponent. These estimates also justify taking \(s\downarrow0\) in individual derivative terms by dominated convergence. They give \(\sum_y k(x,y)\le C(1+\beta)\), by counting \(O((1+r)^3)\) sites at radius \(r\).

**PROVED (rare flat boxes).** At each fixed finite \(\beta\), the bottom of the spectrum of the infinite-lattice \(L_U\) is nevertheless zero almost surely in every Wilson Gibbs state. For a box of side \(R\) require every internal link to be within quaternion chord distance \(1/R\) of the identity. Its probability conditionally on all outside links is at least \([cR^{-3}e^{-12\beta}]^{4R^4}\) for \(R\ge2\). The single-link density relative to Haar is at least \(e^{-12\beta}\) because the tilt length is at most \(6\beta\). A chord ball has Haar volume at least \(cR^{-3}\) by the radial density proportional to \(\sin^2\theta\). Successive conditioning gives the stated bound. For each fixed \(R\), in any infinite list of disjoint boxes the probability that the first \(j\) of them all fail is at most \((1-p_R)^j\) for this positive \(p_R\). Apply the same assertion to every tail and then to every integer \(R\).

In a successful box use a fixed unit colour vector times the product of the first Dirichlet sine waves in its four coordinates, extended by zero. Its ordinary discrete gradient quotient is \(8(1-\cos(\pi/(R+1)))\). Inside the box \(\|I-\operatorname{Ad}U_e\|\le2/R\). Squaring the sum of the ordinary difference and the transport error gives a connection energy quotient at most \(C/R^2\), including the outer Dirichlet bonds. Positivity and \(R\to\infty\) give the assertion. In particular a fixed-radius density of strong pins throughout arbitrarily large boxes cannot be assumed at fixed \(\beta\). Equation (4) controls a mean matrix element despite arbitrarily small Rayleigh quotients of the same operator.

## The equation for a physical plaquette

**GUIDE.** I now try to pass from (5) to a connected gauge-invariant correlation. For the Wilson action and the covariant-shift calculation the relevant Sussman–Alpoge passages are outline 238–269, 10978–10982, 11008–11012, 11354–11361 (PX119), and 12787–12803, located in index chunks 01, 10 and 11. PX119, on one-forms, identifies the error made by commuting two covariant shifts. Its proof credits the curvature of the elementary square. I use that calculation on two-forms below. The source’s estimate for its Green function includes a block mass. Equations (1)–(5) concern an operator with no added block mass.

**PROVED (Wilson equation and the cubical Bianchi remainder).** Work on the whole lattice. Use the left tangent at the tail of each positive link. Let
\[
 T_i f(x)=\operatorname{Ad}U_i(x) f(x+e_i),\quad D_i=T_i-I,\quad
 d=\sum_i\varepsilon_iD_i,\quad d^*=\sum_i\iota_iD_i^* .
\]
Here \(\varepsilon_i\) wedges with the \(i\)-th basis covector and \(\iota_i\) contracts with its dual vector. The fibre norm sums one component per increasingly ordered list. Let \(W_{ij}(x)\) be the plaquette along \(i,j,-i,-j\), based at \(x\). Write \(F_{ij}=\operatorname{Im} W_{ij}\), \(u_{ij}=|1-W_{ij}|\), and \(E_{ij}=1-\operatorname{Re}W_{ij}\). In particular \(F_{ji}=-F_{ij}\), \(u_{ij}^2=2E_{ij}\), and \(2E_{ij}=|F_{ij}|^2+E_{ij}^2\). If \(\partial_e\) denotes the left link gradient, the gradient of the sum of the six action terms incident to link \(e\) is \((d^*F)_e\). Indeed the forward \(ij\) plaquette contributes \(F_{ij}(x)\) and the backward one contributes \(-T_j^*F_{ij}(x)\) to the gradient on \((x,i)\), by cycling the quaternion trace in the link derivative. Summing over \(j\ne i\) gives the stated formula. The logarithmic derivative of the Boltzmann weight is therefore \(-\beta d^*F\).

For \(i<j<k\), compare the two sequences of adjacent interchanges which turn the three-link path \(ijk\) into \(kji\). Equality of the path products at their common root gives
\[
 W_{ij}\,(T_jW_{ik})\,W_{jk}
       =(T_iW_{jk})\,W_{ik}\,(T_kW_{ij}).                         \tag{7}
\]
In (7) the shifts act on group-valued fields by conjugation. For any three unit quaternions \(A,B,C\), the difference of \(ABC-I\) from \((A-I)+(B-I)+(C-I)\) has norm at most \(uv+uw+vw\), with \(u=|A-I|,v=|B-I|,w=|C-I|\). Expand the first two factors and use \(|AB-I|\le u+v\) before multiplying the third. Comparing imaginary parts in (7), the linear difference is \(-(dF)_{ijk}\). Consequently \(R=dF\) is bounded componentwise by the sum of those three pair products on each side of (7). This is a bound for the actual cube and includes large plaquettes.

**PROVED (the spin term).** The exterior algebra identity \(\iota_j\varepsilon_i+\varepsilon_i\iota_j=\delta_{ij}I\) gives on two-forms
\[
 dd^*+d^*d=L_U+K_U,\qquad
 K_U=\sum_{ij}\varepsilon_i\iota_j[T_i,T_j^*].
                                                                    \tag{8}
\]
Here \(L_U=\sum D_i^*D_i\) acts componentwise. Each nonzero shift commutator compares the two paths from \(x\) to \(x+e_i-e_j\). Its coefficient is a transported \(\operatorname{Ad}W-I\) and hence has norm at most \(2u_{ij}(x-e_j)\). In particular
\[
 L_U F=d(d^*F)+Q_U,\qquad Q_U=d^*R-K_UF .                        \tag{9}
\]
Each component of \(Q_U\) is bounded by a finite sum of products of nearby plaquette defects \(u_pu_{p'}\), with absolute coefficients. For \(d^*R\) this follows from (7) and unitarity. For \(K_UF\) it follows from (8) and \(|F_p|\le u_p\). Equation (9) keeps the relative signs of these terms.

**PROVED (an identity for a neutral correlation).** At a fixed oriented plaquette \(p=(x,ij)\) let \(h_p\) be the two-form supported there with value \(F_{ij}(x)\). Define \(X_s=G_{U,s}h_p\) componentwise and \(V_s=d^*X_s\), a link vector field. For a real smooth bounded cylinder observable \(B\) let \(\partial_e B\) be its three left link derivatives. At fixed \(\beta>0\), take the entrywise \(s\downarrow0\) limits \(X,V\), and define the scalar random variable
\[
 Y_p=E_p^2+\sum_{z,I} X_I(z)\cdot(Q_U)_I(z)
             +\beta^{-1}\sum_e\operatorname{div}_e V_e .             \tag{10}
\]
The capital index \(I\) ranges over the six ordered coordinate planes with increasing indices. The divergence in (10) is the sum, over the three imaginary quaternion basis vectors, of the left derivative of the corresponding component of \(V_e\). All series in (10) converge in \(L^1\). Then
\[
 2\operatorname{Cov}_\beta(E_p,B)=
   \operatorname{Cov}_\beta(Y_p,B)
     +\beta^{-1}\sum_{e\in\operatorname{supp}B}
                          \mathbb E_\beta[V_e\cdot\partial_e B].    \tag{11}
\]
At a link a distance \(r\) from \(x\), the absolute value of its last summand, including \(\beta^{-1}\), is bounded by
\[
 \frac{C}{\beta}\|\partial_e B\|_\infty(1+r)^{-2}
                        e^{-cr/\sqrt{1+\beta}} .                    \tag{12}
\]

**PROVED (justification of (10)–(12)).** At \(s>0\) the sum over the norms of each row of the Green function is at most \(1/s\), by scalar path domination. Pair (9), with \(sF\) added to both sides, against \(X_s\). The resulting left side is \(|F_p|^2\) because the massive resolvent is a two-sided inverse on bounded functions by its convergent walk series. On the right, summation by parts gives \(\sum_e(V_s)_e\cdot(d^*F)_e+\langle X_s,Q_U+sF\rangle\). Multiply by \(B\). Conditional integration by parts in Haar measure on one link replaces the first sum in expectation by
\[
 \beta^{-1}\sum_e\mathbb E_\beta
 [B\operatorname{div}_e(V_s)_e+(V_s)_e\cdot\partial_e B].
\]
For fixed \(s>0\) the resolvent and its single-link derivatives converge uniformly by their massive series (or the resolvent identity), so the conditional operation applies. For the limit, \(|F|\), its single-link derivatives and \(|Q_U|\) are bounded by absolute constants. Each term from differentiating \(G_{U,s}(z,x)\) has the product bound (6), and (5) controls the undifferentiated entries. In \(\operatorname{div}_e(V_s)_e\) the first argument \(z\) lies at distance at most one from \(e\), so one factor of (6) is bounded and the other is summable in \(e\) at fixed \(\beta\). Derivatives of \(h_p\) occur on only four links. These bounds give uniformly summable tails in expectation. At fixed sites the kernels converge by the transient scalar bound, and their derivative products converge by the same bound. This proves the claimed \(L^1\) limits by first restricting to a finite set. The term with \(sF\) is bounded in mean by \(Cs(1+\beta)\). Add \(E_p^2\), use \(2E_p=|F_p|^2+E_p^2\), and subtract the identity with \(B=1\) times \(\mathbb E B\). This gives (11). Finally \(V_e\) is a sum of at most finitely many transported entries of \(X\) within one step, so (5) gives (12). The conditioning and the derivative term in (11) use the original Wilson law.

**OPEN.** The unestimated term in (11) is the connected correlation of the explicit neutral random variable \(Y_p\) with \(B\). Bounds on how far the coloured kernels travel estimate (12). They leave the law of the neutral remainder in (10) in the first term of (11). Even a proof of the required decay for \(E_p\) would still need extension to a total family of continuum observables.

## Estimating the neutral remainder

**PROVED (a derivative gains one lattice power).** Fix \(x\), and in each column of \(G_{U,s}(z,x)\) write \(g(z)=G_{U,s}(z,x)v\) for a fixed unit vector. For dyadic \(R\ge4\) use a real cutoff \(\chi\) equal to one on the ends of the links with tail in \(R\le |z-x|_\infty<2R\), supported in \(R/2\le |z-x|_\infty\le4R+2\), with bond differences at most \(C/R\). Pair the homogeneous equation \((L_U+s)g=0\) there with \(\chi^2g\). On an unoriented edge \(uv\) the real part of the energy pairing is
\[
 |\chi_ug_u-\chi_vT_{uv}g_v|^2
       -(\chi_u-\chi_v)^2\operatorname{Re}\langle g_u,T_{uv}g_v\rangle .
\]
The mass term is nonnegative. Squaring (5) by its deterministic upper bound therefore gives
\[
 \sum_{R\le |z-x|_\infty<2R}\sum_i
       \mathbb E\|D_iG_{U,s}(z,x)\|^2
       \le C R^{-2}e^{-cR/\sqrt{1+\beta}}.                           \tag{13}
\]
Indeed the enlarged annulus contains \(O(R^4)\) sites and the expected squared norm there is at most \(CR^{-4}e^{-cR/\sqrt{1+\beta}}\). Apply the vector argument to an orthonormal basis of the three-dimensional fibre. The finitely many small radii use (5). By Cauchy–Schwarz over sites, then summing dyadic radii,
\[
 \sum_{z,i}(\mathbb E\|D_iG_{U,s}(z,x)\|^2)^{1/2}
     \le C\sqrt{1+\beta},\qquad
 \sum_z(\mathbb E\|G_{U,s}(z,x)\|^2)^{1/2}\le C(1+\beta).
                                                                    \tag{14}
\]
The first sum is bounded by \(C\sum_{R\text{ dyadic}}R e^{-cR/\sqrt{1+\beta}}\), the second by (5). Both estimates hold at \(s=0\) by entrywise convergence.

**PROVED (what absolute values give in the periodic Wilson state).** For this estimate take any infinite-volume limit of ordinary periodic Wilson tori at coupling \(\beta\ge1\). Use the previously proved marked-plaquette moment, row 1155, `gap-solve7-astra62.md` (9), at one marked plaquette. It gives \(\mathbb E\exp(c\beta E_p)\le C\) uniformly, hence \(\|u_p\|_k\le C_k\beta^{-1/2}\) at every fixed finite \(k\), by bounding a power by an exponential. With \(X=G_Uh_p\),
\[
 \mathbb E|\langle dX,R\rangle|\le C/\beta,\qquad
 \mathbb E|\langle X,K_UF\rangle|\le C/\sqrt\beta .                  \tag{15}
\]
To see this, \(dX\) contains covariant differences of the first argument of \(G_U\), acting on the fixed vector \(F_p\) for the sampled configuration. For every local product of two defects bounding \(R(z)\), the \(L^2\) norm of its product with \(|F_p|\) is at most \(C\beta^{-3/2}\) by Hölder with three sixth moments. This also holds with repeated plaquettes. Apply Cauchy–Schwarz in expectation and the first sum in (14). For \(K_UF\), (8) gives two defect factors again, but the kernel has no difference. The second sum of (14) gives the second bound. Summation by parts \(\langle X,d^*R\rangle=\langle dX,R\rangle\) follows first at \(s>0\) and then in mean by (13)–(14). The input mean energy obeys \(\mathbb E E_p\le C/\beta\). Thus these absolute estimates leave the spin term one power of \(\sqrt\beta\) too large even at the level of this upper-bound comparison. They give no contraction of the connected correlations in (11).

**PROVED (size of the squared scalar Green function).** For the same periodic limits and all sufficiently large \(\beta\),
\[
 c\log(2+\beta)\ \le \mathbb E\sum_z\|G_U(z,x)\|_{\rm HS}^2
       \ \le C\log(2+\beta).                                       \tag{16}
\]
The upper bound follows from (5), using the deterministic estimate times the averaged one and summing \((1+r)^{-1}e^{-cr/\sqrt{1+\beta}}\). For the lower bound, regularize by \(s>0\). The squared norm sum is the trace at \((x,x)\) of \((L_U+s)^{-2}\). Its walk series has coefficient \((n+1)(8+s)^{-2}(8/(8+s))^n\) in front of \(P_U^n(x,x)\). Odd lengths give zero on the infinite hypercubic lattice. Every even block \(P_U^{2j}(x,x)\) is positive semidefinite, since it is the diagonal block of \((P_U^j)^*P_U^j\). This positivity allows us to retain entire even lengths before averaging. As \(s\downarrow0\), the summable bound (5) on the tails in \(z\) and convergence at each fixed site give the massless squared norm sum in expectation.

For a single closed path of length \(n\), sorting its coordinate directions and cancelling inverse steps fills it using at most \(n^2\) elementary plaquette interchanges. Each interchange costs at most \(2u_p\) in operator norm for the change of adjoint transport, regardless of the intervening transporters. The selected plaquette positions and orientations are fixed by the path. The marked-plaquette bound therefore gives \(\mathbb E\|I-T_{\rm path}\|\le Cn^2/\sqrt\beta\). For \(n\le c_1\beta^{1/4}\) with \(c_1\) small, the expected trace is at least \(3/2\) for every closed path of that length. The scalar return probability satisfies \(p^{2j}(x,x)\ge c(j+1)^{-2}\), by integrating \(\phi^{2j}\ge0\) on a ball of radius \(c/\sqrt{j+1}\) about zero. The retained terms in the limit dominate \(c\sum_{1\le j\le c_1\beta^{1/4}/2}j^{-1}\), giving (16). This controls an actual Wilson average. The one-loop model comparison in row 1244 and its correction in row 1263 concern a different response. Equation (16) gives no sign for that response or for the covariance in (11).

**PROVED (a limit on absorbing the spin term).** For any \(\alpha>0\) and \(\epsilon>0\) there is a finite periodic SU(2) configuration with \(\max_p u_p<\epsilon\), and a real two-form \(v\) equal to its own imaginary plaquette curvature times a scalar cutoff, such that
\[
  0\le \|dv\|_2^2+\|d^*v\|_2^2
       <\alpha\langle v,L_Uv\rangle,\qquad \langle v,L_Uv\rangle>0.
                                                                    \tag{17}
\]
This tests the signed quadratic-form inequality \(K_U\ge-(1-\alpha)L_U\) that would permit a strict relative absorption in (8). The construction discretizes the instanton of A. A. Belavin, A. M. Polyakov, A. S. Schwartz and Yu. S. Tyupkin.

Identify \(\mathbb R^4\) with the quaternions in the orientation \(1,\mathbf i,\mathbf j,\mathbf k\), put \(s=|x|^2\), \(b=\operatorname{Im}(\bar x\,dx)\), and take the imaginary-quaternion connection \(A=b/(1+s)\). Since \(b=\bar x\,dx-ds/2\), we have \(db=d\bar x\wedge dx\). Off the origin the unit quaternion \(g=x/|x|\) obeys \(g^{-1}dg=b/s\). Differentiating \(g^{-1}g=1\) gives \(d(g^{-1}dg)=-(g^{-1}dg)\wedge(g^{-1}dg)\), so \(b\wedge b=ds\wedge b-s\,db\). Both sides extend smoothly through zero. Thus
\[
 \mathcal F=dA+A\wedge A=\frac{d\bar x\wedge dx}{(1+s)^2}.
\]
The coefficients of its numerator in the \(0i\) and complementary cyclic \(jk\) planes are respectively \(2\mathbf e_i\) and \(-2\mathbf e_i\), where \(x_0\) is the real coordinate. Hence \(*\mathcal F=-\mathcal F\). The covariant exterior derivative \(d_A=d+[A,\cdot]\), with the graded bracket, gives \(d_A\mathcal F=0\) by expanding \(d(dA+A\wedge A)+A\wedge\mathcal F-\mathcal F\wedge A\). Consequently \(d_A^*\mathcal F=-*d_A*\mathcal F=0\). The norm of the curvature is a positive constant times \((1+s)^{-2}\). The ordinary derivative of that norm is bounded pointwise by the full covariant derivative norm, since commutators with \(A\) are skew. In particular the squared full derivative has a strictly positive integral on \(1<|x|<2\).

Choose \(R>3\) and a smooth radial \(\chi_R\) equal to one through radius \(R\), supported in radius \(2R\), with \(|\nabla\chi_R|\le C/R\). For \(v=\chi_R\mathcal F\) the continuum numerator in (17) is at most \(CR^{-2}\int_{R<|x|<2R}|\mathcal F|^2\le CR^{-6}\) because both derivatives fall on \(\chi_R\). Its full covariant-gradient energy is bounded below by the annular integral above. Choose \(R\) so the quotient is smaller than \(\alpha/2\). Smoothly extend the potential to zero outside radius \(3R\), keeping it equal to \(A\) on a neighbourhood of the support of \(\chi_R\), and periodize on a fixed cube of side greater than \(8R\).

On that torus take mesh \(h\downarrow0\) dividing the side, and links \(U_i(x)=\exp(h A_i(x))\) of this smooth potential. Multiplying the four exponentials, Taylor expansion through order two gives \(W_{ij}=1+h^2(\partial_i A_j-\partial_j A_i+[A_i,A_j])+O_R(h^3)\). Indeed the two translated links supply \(h^2(\partial_iA_j-\partial_jA_i)\) and the constant-matrix group commutator supplies \(h^2[A_i,A_j]\). The error and its first spatial derivatives are \(O_R(h^3)\) by the same Taylor formula on the fixed smooth compact torus. Therefore the test \(v^h=\chi_R\operatorname{Im}W/h^2\) and its first ordinary derivatives converge uniformly, interpreting the sampled formula as a smooth function of its base point. The shifts give \(h^{-1}D_i v^h\to (\partial_i+[A_i,\cdot])v\) and \(h^{-1}D_i^*v^h\to-(\partial_i+[A_i,\cdot])v\) uniformly. Multiplying each lattice squared-difference sum by \(h^4/h^2\) converts both sides to Riemann sums for the continuum energies. Their quotient thus has the required strict inequality for all small \(h\), while every plaquette defect is \(O_R(h^2)\). Multiplying the test by \(h^2\) leaves its quotient unchanged. This proves (17) for a cutoff of the actual lattice curvature.

**PROVED (scope in the Wilson measure).** Both inequalities in (17) persist on an open set of link configurations when the test is chosen by the same rule \(v=\chi_R F(U)\). That set has strictly positive probability at every finite coupling, since the finite Wilson density is strictly positive relative to product Haar measure. Multiplying the test by its event indicator precludes the same positive form comparison in expectation for *all* field-dependent tests, even with a small-plaquette support condition. The indicator can be chosen gauge invariant since the plaquette condition and both quadratic forms are gauge invariant. This argument supplies no lower bound on the frequency or contribution of that event for the particular source \(h_p\) in (10). The signed estimate for that source remains open.

## Removing the scalar remainder for Wilson loops

**PROVED (the pole at the negative centre element is integrable).** Set \(a(W)=\operatorname{Im}W/(1+\operatorname{Re}W)\) away from \(-1\). Then \(a(W)\cdot\operatorname{Im}W=1-\operatorname{Re}W\) exactly. Conditional on all links except one edge of the plaquette, its holonomy density relative to Haar is at most \(C(1+\beta)^{3/2}\). Indeed the conditional tilt has length \(\kappa\le6\beta\), and integration on a ball of radius \((1+\kappa)^{-1/2}\) about the tilt maximum bounds its normalizer below by \(c e^\kappa(1+\kappa)^{-3/2}\). At chord distance \(t=|W+1|\) from \(-1\), the source has size \(O(t^{-1})\) and its first link derivatives have size \(O(t^{-2})\). This follows from \(1+\operatorname{Re}W=t^2/2\), \(|\operatorname{Im}W|\le t\), and \(|\partial\operatorname{Re}W|\le|\operatorname{Im}W|\). The Haar radial element there is \(O(t^2dt)\). Thus at every finite coupling \(a(W)\in L^p\) for \(p<3\), and its first derivatives are in \(L^q\) for \(1\le q<3/2\). Cutting it off smoothly for \(t<\varepsilon\) converges in these norms, including the derivative term of the cutoff supported on \([\varepsilon,2\varepsilon]\).

In periodic limits with \(\beta\ge1\), the norm of \(a(W)\) in any fixed \(L^p\), \(1\le p<3\), is at most \(C_p/\sqrt\beta\). On \(\operatorname{Re}W\ge0\) use \(|a|\le u_p\) and row 1155. On the other half the same moment gives probability at most \(Ce^{-c\beta}\). Hölder with \(p<p'<3\) and the polynomial Haar density bound above absorb this event. The derivative has bounded \(L^q\) norm for \(1\le q<3/2\) by the same argument with \(q<q'<3/2\).

**PROVED (any fixed contractible Wilson loop).** Write \(w_C=\operatorname{Re}U_C\) for a finite lattice loop in \(\mathbb Z^4\). Choose a plaquette filling by interchanging adjacent steps in its word, sorting by coordinate direction and deleting cancellations. Interchanging steps of distinct directions changes the word by a conjugate of one elementary plaquette or its inverse. Thus \(U_C=Z_1\cdots Z_m\), with \(Z_l=P_l W_{p_l}^{\sigma_l}P_l^{-1}\) for fixed stems from the common base, \(\sigma_l=\pm1\). Each \(W_{p_l}\) uses the increasing-index orientation and the chosen base of that elementary square. Each cyclic change of base contributes to \(P_l\). For \(H_{l-1}=Z_1\cdots Z_{l-1}\), the quaternion product gives
\[
 1-w_C=\sum_{l=1}^m h_l\cdot F_{p_l},\qquad
 h_l=(\operatorname{Re}H_{l-1})a(W_{p_l})
       +\sigma_l\operatorname{Ad}(P_l^{-1})\operatorname{Im}H_{l-1}.   \tag{18}
\]
Indeed each summand equals \(\operatorname{Re}H_{l-1}-\operatorname{Re}H_l\). The identity holds almost surely, including for repeated plaquettes. Put \(h_C=\sum_l\delta_{p_l}h_l\), \(X_C=G_Uh_C\), \(V_C=d^*X_C\), and
\[
 Z_C=\langle X_C,Q_U\rangle+\beta^{-1}\sum_e\operatorname{div}_e(V_C)_e .
\]
The letter \(Z_C\) here denotes a scalar observable. Applying (9) to (18) yields
\[
 \operatorname{Cov}_\beta(1-w_C,B)=\operatorname{Cov}_\beta(Z_C,B)
          +\beta^{-1}\mathbb E_\beta\sum_e(V_C)_e\cdot\partial_eB .    \tag{19}
\]
To justify the integration, first use the smooth cutoffs on the singular terms of \(h_l\). The argument for (11) holds for any such local two-form, with left side its inner product with \(F\). Remove the cutoffs in \(L^2\) for \(h_l\) and \(L^{4/3}\) for its derivatives. Every fixed finite moment of a Green entry retains the spatial power in (5) and an exponential rate divided by the order of the moment, by combining the two bounds in (5). In (6) use Hölder with exponents \(4,4,2\) for the two Green entries and the source, or \(4,4/3\) for a Green entry and a source derivative. This supplies summable tails at fixed \(\beta\) and justifies (19). The regularized left side converges to (18). The new identity has removed \(E_p^2\) from (11), including on the far side of the group.

**PROVED (physical scale of the last term).** In the periodic limit at \(\beta\ge1\) let \(d_0\) be the least lattice distance between the filling plaquette bases and links of \(B\) (using either endpoint changes constants). The absolute value of the last term of (19) is bounded by
\[
 C\beta^{-1}m\left(\sum_e\|\partial_e B\|_\infty\right)
                 (1+d_0)^{-2}e^{-c d_0/\sqrt{1+\beta}}.               \tag{20}
\]
In fact \(\|h_l\|_2\le C\) independently of the prefix and stem, by unitarity and the preceding single-plaquette estimate. Apply Cauchy–Schwarz with the squared version of (5) to the finitely many terms of \((d^*G_U h_C)_e\). In particular (20) tends to zero at fixed positive physical separation if \(a\downarrow0\), \(\beta=O(\log(1/a))\), and the filling count, the derivative sum and any source normalization factors grow at most polynomially in \(1/a\). The assertion is for families with fillings at the stated separation. Finite sums of trace words obey the summed estimate. Products of SU(2) traces at finite cutoff resolve into single trace words using \(w(A)w(B)=[w(AB)+w(AB^{-1})]/2\) after joining bases. This trace reduction is prior work, used by Vladimir Kazakov and Zechuan Zheng and recorded in `prior/gap-fullread-1.md` §5. Moment matching and totality of any chosen continuum family remain separate requirements.

**OPEN.** Equation (19) puts the full separated signal of these loop families in \(\operatorname{Cov}(Z_C,B)\) at their continuum limit. Absolute colour propagation proves (20). A physical infrared estimate must still control the connected expectation involving the signed curvature and divergence in \(Z_C\).

## Keeping the signed terms together

**PROVED (a mean-square bound which improves (15)).** In an ordinary periodic Wilson limit at \(\beta\ge1\), the specific smooth-source remainder (10) satisfies
\[
                  \|Y_p\|_{L^2(\mu_\beta)}\le C/\beta.               \tag{21}
\]
Use the three left derivatives \(X_i\) per link, with \(i\) now denoting a link and a colour component only in the following divergence calculation. Put \(J_i=X_i\sum_p E_p\), understood as the derivative of the incident terms, and \(\delta V=\sum_i(-X_i+\beta J_i)V_i\). This is the adjoint of the configuration gradient in the Wilson measure. From (9)–(10) before taking expectations,
\[
                       Y_p=2E_p-\beta^{-1}\delta V,\qquad
                V=d^*G_U h_p,\quad h_p=\delta_p F_p.                 \tag{22}
\]
All terms on the right are defined as in (11). In particular this calculation uses the smooth \(F_p\) source.

For any finite collection of smooth link vector components \(v_i\), conditional integration by parts gives
\[
 \|\delta v\|_2^2\le C\mathbb E\left[
 (1+\beta)\sum_i|v_i|^2+\sum_{i,j}|X_i v_j|^2\right].               \tag{23}
\]
In the squared norm move one adjoint derivative across, then commute \(X_i\) past \(-X_j+\beta J_j\). The result is the sum of \((X_j v_i)(X_i v_j)-v_i[X_i,X_j]v_j+\beta v_i(X_iJ_j)v_j\) in expectation. The first term is bounded by the derivative squares. The Lie brackets are combinations with bounded coefficients of the three derivatives on one link, and vanish between distinct links. Young’s inequality bounds the bracket term by the first two sums in (23) with absolute constants. The bounded entries \(X_iJ_j\) vanish unless both links lie on the same plaquette, including the same-link case. The number of entries per row and column is bounded. This proves (23). Weighted Haar scores and their contact contributions also occur in row 1018, Lemma FLOW. The test field here contains the full bare Green function.

For any finitely supported two-form \(f\),
\[
 \|d^*G_{U,s} f\|_{\ell^2}^2
 \le C\langle G_{U,s} f,L_U G_{U,s} f\rangle
 \le C\langle f,G_{U,s} f\rangle\le C\|f\|_{\ell^1}^2 .
\]
The first inequality uses \(\|D_i^*g\|_2=\|D_i g\|_2\) for unitary shifts, and the last uses the deterministic kernel bound. Hence \(\mathbb E\|V_s\|_{\ell^2}^2\le C\mathbb E|F_p|^2\le C/\beta\). Differentiate \(V_s=d^*X_s\) in one link \(e=uv\). The differentiated \(d^*\) costs at most \(C(|X_s(u)|+|X_s(v)|)\) in \(\ell^2\). The rest is \(d^*G_{U,s}(\partial_e h_p-(\partial_e L_U)X_s)\). The parenthesis has \(\ell^1\) norm at most \(C(\mathbf1_{e\in p}+|X_s(u)|+|X_s(v)|)\). Summing the squared bound, including all three derivatives, gives \(C(1+\|X_s\|_{\ell^2}^2)\). By (5) and Hölder,
\[
 \mathbb E\|X_s\|_{\ell^2}^2\le
   (\mathbb E|F_p|^4)^{1/2}\sum_z(\mathbb E\|G_{U,s}(z,x)\|^4)^{1/2}
       \le C\,\log(2+\beta)/\beta .
\]
Apply (23) to finite link restrictions of \(V_s\). At \(s>0\) truncating the massive walk series approximates it and its first two link derivatives by smooth cylinder functions for each fixed component, since the polynomial factors in path length are summable against the mass weight. The preceding estimates bound \(\|\delta V_s\|_2\) by an absolute constant. Take expanding link restrictions and then \(s\downarrow0\), using the \(L^1\) convergence proved for (10) and (22) and lower semicontinuity of the squared norm. Combining the resulting bound \(\|\delta V\|_2\le C\) with (22) and \(\|E_p\|_2\le C/\beta\) gives (21). This cancellation controls the size of the neutral variable in the actual ensemble.

**PROVED (removal of a fixed fraction of the one-plaquette variance).** Write \(D_p=\beta^{-1}\delta V\). It has zero mean and \(\|D_p\|_2^2\le C_1/\beta^2\). There are absolute \(t>0,\gamma>0\) such that
\[
      \operatorname{Var}(E_p-tD_p)\le(1-\gamma)\operatorname{Var}(E_p)
                  \qquad(\beta\ge1).                                 \tag{24}
\]
For the original plaquette in plane \(ij\), its link gradient is exactly \(d^* h_p\), by the single-face derivative above. Thus
\[
 \mathbb E(E_pD_p)=\beta^{-1}\mathbb E\langle d^*h_p,d^*G_Uh_p\rangle .
\]
Only the two components belonging to directions \(i,j\) occur in this pairing. With \(L_a=2-T_a-T_a^*\) it equals, inside the expectation, \(\sum_{a=i,j}\langle h_p,L_aG_U h_p\rangle\). Each summand is at least \(|F_p|^2/12\), as follows.

The diagonal matrix \(G_U(x,x)\) is at least \(I/8\) in quadratic form. The term with no steps gives \(I/8\) and each even return block is positive semidefinite. At any neighbour \(y\), scalar domination gives \(\|G_U(y,x)\|\le1/12\). For the latter constant let \(g_0=\sum_n p^n(0,0)\). The scalar sum from a neighbour is \(g_0-1\) by symmetry and the first step. Map the eight one-step directions to all eight sign triples by assigning the four positive directions to \((1,1,1),(1,1,-1),(1,-1,1),(1,-1,-1)\) and each negative to the opposite triple. This is a linear map on \(\mathbb Z^4\), and the three image coordinates are independent symmetric walks. Thus \(p^{2n}(0,0)\le [4^{-n}{2n\choose n}]^3\le(3n+1)^{-3/2}\). The last inequality follows by induction from \((2n+1)^2(3n+4)\le(2n+2)^2(3n+1)\). The sum for \(n\ge1\) is at most the integral from zero to infinity of \((3u+1)^{-3/2}\), which is \(2/3\). Including the Green normalization gives the neighbour estimate. Subtracting the two neighbour contributions in \(L_aG_U\) leaves \((2/8-2/12)|F_p|^2=|F_p|^2/12\).

In row 1141’s single-loop cap estimate (3), choose any fixed axis and squared cap parameter \(1/[8(1+6\beta)]\). Its exceptional probability is at most one half, which gives \(\mathbb E|F_p|^2\ge c/(1+\beta)\). We obtain \(\mathbb E(E_pD_p)\ge c_1/\beta^2\) at \(\beta\ge1\). Taking \(t=c_1/C_1\) subtracts at least \(c_1^2/(C_1\beta^2)\) from the variance. Since \(\operatorname{Var}E_p\le C_E/\beta^2\), (24) follows with any sufficiently small \(\gamma>0\). By (11) the subtracted variable correlates with a separated smooth local test only through the derivative estimate (12). Thus (24) removes genuine local fluctuations while preserving separated continuum correlations for polynomially normalized tests as in (20).

**PROVED (testing the variance argument on collective neutral observables).** At \(\beta\ge1\) in the same periodic Wilson limits, for each elementary face \(p\) there is a smooth gauge-invariant scalar \(D'_p\) supported on the plaquettes incident to two opposite links of \(p\). It obeys
\[
 \mathbb E D'_p=0,\qquad \mathbb E[D'_p E_q]=\beta^{-2}\mathbf1_{p=q},
 \qquad \left\|\sum_p c_p D'_p\right\|_2^2\le C\beta^{-2}\sum_p|c_p|^2
                                                                    \tag{25}
\]
for every finitely supported array of coefficients, without separation of the plaquettes. For a test whose support omits either of the two links, its expectation against \(D'_p\) is zero. The mixed-score method has predecessors in row 1018, Lemma NAB, and the opposite-link Wilson chart in `gap-solve3-astra62.md` (two links of one plaquette). Row 1204 uses two private variables for a product of two oscillatory plaquette readings. Here the source paired in (25) is the ordinary fundamental energy on each face.

Fix the two opposite links \(e,f\) and put \(H_{ab}=X_{f,b}X_{e,a}E_p\), differentiating in orthonormal imaginary quaternion directions. For fixed links,
\[
                         \sum_{a,b}|H_{ab}|^2=2+(\operatorname{Re}W_p)^2 .
\]
To verify this, cyclically place the first insertion at the root of the loop. The second derivative inserts the other unit imaginary quaternion at its own position in the word. Moving the two insertions to the root gives, up to signs, \(\operatorname{Re}(a' b' W'_p)\), where \(a'\) and \(b'\) are separately rotated orthonormal bases and \(W'_p\) is the plaquette at that root. Inversely traversed links give a sign and a conjugation of the inserted generator. The two derivatives initially act on distinct link factors. The bilinear form has symmetric matrix \(-wI\) and skew part the cross product with \(\operatorname{Im}W'_p\), up to signs and orthogonal changes of basis. Its squared Hilbert–Schmidt norm is \(3w^2+2(1-w^2)\). Set \(M_{ab}=H_{ab}/(2+w^2)\) and define
\[
 D'_p=\beta^{-2}\sum_{ab} X_{e,a}^{\dagger} X_{f,b}^{\dagger} M_{ab},
 \qquad X_{e,a}^{\dagger}=-X_{e,a}+\beta X_{e,a}\sum_q E_q .
\]
The last term in the adjoint acts by multiplication. Its intrinsic mixed-gradient pairing, or the orthogonal transformation of both bases under vertex gauges, shows gauge invariance. Twice integrating by parts leaves \(\beta^{-2}\sum M_{ab}X_{f,b}X_{e,a}B\) in expectation for any smooth cylinder test \(B\). This is identically \(\beta^{-2}\) for \(B=E_p\) and zero for every other elementary face energy. Only \(p\) uses both opposite links. The conclusion for bounded tests omitting either link follows as well, by integrating out that link or by bounded approximation on the other variables.

All derivatives of \(M\) through second order are bounded by absolute constants, as each link occurs once and \(2+w^2\ge2\). Each unweighted force \(J_{e,a}\) is bounded by the sum of six plaquette defects and has fourth moment norm \(\le C/\sqrt\beta\). Expanding the two adjoints gives a second derivative of \(M\), terms with one force or one bounded mixed derivative of the action times \(\beta\), and one term with two forces times \(\beta^2\). Thus \(\|D'_p\|_2\le C/\beta\). For a given \(p\), the expectation \(\mathbb E D'_pD'_q\) vanishes outside a fixed neighbourhood by the two integrations by parts. Each row and column has an absolute number of potentially nonzero entries. Cauchy–Schwarz on entries and \(2|c_p c_q|\le |c_p|^2+|c_q|^2\) prove (25).

Write \(A_c=\sum_p c_p(E_p-\mathbb E E_p)\), \(D'_c=\sum_p c_pD'_p\). For one absolute \(t'>0\),
\[
 \|A_c-t'D'_c\|_2^2\le \|A_c\|_2^2-t'\beta^{-2}\sum_p|c_p|^2.      \tag{26}
\]
Expand the square and take \(t'\le1/C\) in (25). For separated sets of faces, replacing the energy by \(E_p-t'D'_p\) preserves their joint moments exactly whenever the enlarged supports are mutually disjoint. In each term of the expansion containing a score, integrate one \(D'_p\) against the other factors. For a single replacement in a product, it suffices that the product of all other factors omit one of the selected links. This removes a positive contact contribution in every linear combination. To obtain a fixed fractional reduction of the *total* variance in (26) one would need an upper bound on \(\|A_c\|_2^2\) of the corresponding order. Even such a bound on these unsmeared energies would not specify the low-energy support of their separated correlations.

**PROVED (the same subtraction in a massless gauge-invariant channel).** To test whether (25) can supply the next variance reduction by itself, use the free lattice magnetic curvature from row 1204, `gap-solve21-astra62.md`, “Testing the sum rule at a two-particle threshold.” There is an exact version of (25) in that field. In ordinary lattice exterior calculus put \(F=dA\), using four independent centered Gaussian link components with scalar covariance \(L_0^{-1}\), and put \(J=d^*F\). Only \(F,J\) occur in the observables. In Fourier variables the curvature covariance is \(C=dL_0^{-1}d^*\). At nonzero momentum \(dd^*+d^*d=L_0 I\) and \(d^2=0\) give \(d^* C=d^*\) almost everywhere. Consequently
\[
 \mathbb E[J_e F_q]=(d^*)_{eq},\qquad
 \mathbb E[J_e J_f]=(d^*d)_{ef}.
\]
These covariances are the signed incidence matrix and a finite-range matrix respectively. Write colons for subtraction of the Gaussian mean from a quadratic product. For a face \(p\) with opposite boundary links \(e,f\), put
\[
 O_p={:F_p^2:},\qquad
 D^{\rm free}_p=\frac{{:J_eJ_f:}}{2(d^*)_{ep}(d^*)_{fp}}.
\]
Gaussian pair contraction gives \(\mathbb E[D^{\rm free}_p O_q]=\mathbf1_{p=q}\). It gives finite-range, uniformly bounded covariance for the \(D^{\rm free}_p\) as well. In fact \(C^2=C\) follows from \(d^*C=d^*\), so \(C\) is a real orthogonal projection and \(\sum_q |C_{pq}|^2=C_{pp}\le1\). The covariance of the \(O_p\) has entries \(2C_{pq}^2\) and has row and column sums at most two. Hence \(\operatorname{Var}\sum c_p O_p\le2\sum|c_p|^2\). At unit normalization, the subtraction in (26) removes a fixed fraction even for arbitrary collective energy sources in this model.

For two identical spatial \(12\) faces separated by \(n\) time steps, row 1204’s free curvature formula, with axes permuted, gives the time covariance of \(F\) as the spatial momentum integral of
\[
 \frac{\widehat k_1^2+\widehat k_2^2}{2\sinh\omega(k)}e^{-n\omega(k)},
 \quad \widehat k_i=2\sin(k_i/2),\quad
 \cosh\omega(k)=1+\tfrac12\sum_{i=1}^3\widehat k_i^2.
\]
The integrand is positive. On \(n^{-1}<|k|<2n^{-1}\), \(|k_1|>|k|/2\), it is at least \(c/n\) for large \(n\), on volume at least \(c'n^{-3}\). Squaring the integral and multiplying by two gives \(\mathbb E[O_p O_{p+ne_0}]\ge c'' n^{-8}\). The contact subtraction therefore coexists with spectral weight down to zero in the very gauge-invariant observable being improved. This tests the proposed iteration of (24)–(26). It gives no counterexample to the interacting SU(2) claim.

## The physical energy still to be bounded

**PROVED (which scale a surviving correlation requires).** Let a matched, vacuum-subtracted source have positive physical-time transfer correlation at cutoff \(j\),
\[
 C_j(n)=\int_{[0,\infty)}e^{-nE}\,d\nu_j(E),\qquad
 b_j=\inf\operatorname{supp}\nu_j ,
\]
with \(E\) in lattice units. Two ordered positive physical separations \(t_1<t_2\) suffice for this test. Suppose \(n_{ij}a_j\to t_i\) and \(C_j(n_{ij})\to C(t_i)\) with \(0<C(t_2)\le C(t_1)<\infty\). Then
\[
 \limsup_{j\to\infty}\frac{b_j}{a_j}
       \le \frac{\log(C(t_1)/C(t_2))}{t_2-t_1}.                      \tag{27}
\]
Indeed \(C_j(n_{2j})\le e^{-(n_{2j}-n_{1j})b_j}C_j(n_{1j})\). In particular an all-large-time estimate with exponential rate \(c/\sqrt{1+\beta_j}\) in lattice units, even with a finite source- and cutoff-dependent prefactor, would put \(b_j\ge c/\sqrt{1+\beta_j}\). Any positive spectral mass below that rate would contradict the estimate as \(n\to\infty\) at fixed \(j\). When \(a_j\sqrt{1+\beta_j}\to0\), (27) rules out assigning this colour rate to the whole surviving neutral correlator. This argument uses separated times and permits divergence of the unseparated variance.

**OPEN (the outstanding inequality).** Take the infinite-volume state at each cutoff, then the continuum limit at each fixed physical separation in a common, identified Yang–Mills vacuum theory. For a total family of matched positive-time local sources \(A\), a sufficient remaining estimate is a single \(m>0\) such that the connected reflected autocorrelation of each \(A\) at time \(t\) is at most \(C_A e^{-mt}\) for all sufficiently large \(t\). In (19) the term involving \(Z_C\) is where this estimate is still needed for the stated Wilson-loop tests. The marked-plaquette moment controls local size, (17) rules out the proposed uniform spin absorption, and (21) and (26) control variance. The Maxwell calculation shows why these variance bounds do not yield the required support exclusion. The common-rate spectral implication is the one already recorded on the soft route and in row 1218. Existence, full field identification and vacuum reconstruction also remain open here.

**GUIDE.** These are author-side hand arguments. They have not received an independent check. No computation served as proof.

RESULT — OPEN. The four-dimensional SU(2) Jaffe–Witten mass gap is unproved here. The hand bound (5) gives exponential decay of the Wilson-averaged adjoint Green kernel. The neutral loop identity (19) and variance bounds (21), (24)–(26) leave the common physical decay rate of the connected gauge-invariant correlations and the full continuum construction open.
