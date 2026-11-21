# Repo search

**GUIDE.** FINISH row 1283, checkout `be9ec9d1b`. The lead's November 8 search covered main and PRs 10114, 10133, 10134 and 10141. Its digest recovered earlier soft-route steps with their actual-model hypotheses still open. I fetched and read the primary passages relevant to the mass gap. PR 10114 (`f76f6c649c`, `MASS_GAP_LOCAL_BLOCK_ASTRA.md`, lines 4–14, 106–149) gives a positive one-step plaquette correlation and a contraction at small bare inverse coupling. Grok's PR 10133 (`89faef229f`, `MASS_GAP_CROSSOVER_REDUCTION.md`, 77–86) leaves source transport and the crossover estimate open. PR 10134 (`1e70c7211a`, `mass-gap-interface.md`, I1–I5) separates nontriviality, the spectral threshold and Yang–Mills identification. PR 10141 (`a2f6a430e2`, `research/ym4d/library/fp1.md`, 299–315) estimates a constrained classical quadratic form. On main, Theorem ZD-c (`8b11ae2bb9`, `research/mass-gap/library/gap-phys-seed.md`, 311–329) requires estimates on the actual periodic transfer and its thermal multiplicities. [Lead's search](prior/repo-search-2026-11-08.md)

**GUIDE.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, distinguish reconstruction of the action-density sector from full observable identification. Their reflection estimate allows spectral weight arbitrarily close to zero. I used index chunks 01, 03, 10 and 29 and the neighbouring obligation rows before reading outline lines 581–599, 3712–3720, 10978–10982 and 31858–31882. The complete account expressly leaves the mass gap outside its assertion at CA-I 2704–2712 and 3213–3222. Its 4.12–4.19 index concerns the ultraviolet induction. [Outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L31858-L31882) · [Complete account](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2704-L2712)

**GUIDE.** Row 1218 records two particularly close approaches. Deep Bhattacharjee, Ushashi Bhattacharya, James Montgomery Lockwood, Tristan Romanov, Ikailo John Sessford and Sanjeevan Singha Roy propagate a thermal bound on a window of torus shapes. The first four authors also obtain a relaxation estimate for certain straight coarse transports. The reading records the missing fine-field comparison. Zeng Chunping's common decay rate and tunnelling estimates likewise require a weak-coupling input. I use the row for the scope of those proposals. [Published-work reading](prior/gap-onebound-read-sol.md)

**GUIDE.** Row 1141 gives a lower bound in probability on the Neumann adjoint covariant Laplacian, using two independent directions of curvature and scalar Poincaré on blocks. Row 1157 exhibits negative horizontal Wilson Hessian directions in the presence of a positive scalar covariant lower bound. Row 1272 integrates the colour on long prescribed tree paths and leaves the interacting singlet bound (33) open. The task-specific prior file is absent at this pin. I found no registry assignment for the spectral weight of rare nearly parallel sections considered below. [Two-plaquette bound, (2)–(7)](gap-crux2-astra62.md) · [Wilson Hessian test](gap-solve8-astra62.md) · [Previous row, (32)–(34)](gap-solve31-astra62.md)

## Choice of attack

**OPEN.** The target is a nontrivial four-dimensional continuum SU(2) Yang–Mills theory with a positive lower edge of the energy spectrum on the orthocomplement of the vacuum. I will test a possible source of low-energy states directly in the interacting Wilson law. A slowly varying colour field can adapt to the connection and concentrate on a rare favourable region. The earlier typical-block estimate allows this possibility in the infinite-volume-first limit. The first step is to bound how many such modes there are and how long they can persist under the actual time transfer. A distinct step is needed to control the colour-singlet states that remain.


## The spatial spectrum on a Wilson time slice

**GUIDE.** Use the Wilson density proportional to \(\exp(\beta\sum_p w(U_p))\) relative to product probability Haar, where \(w=\tfrac12\operatorname{tr}\), \(\beta\ge0\). Take a spatial \(N^3\) torus and at least four time layers. For the spatial links \(Y\) on one layer define the nonnegative operator \(L_Y\) on \(\ell^2((\mathbb Z/N)^3;\mathbb R^3)\) by its quadratic form
\[
 \langle s,L_Ys\rangle=\sum_x\sum_{i=1}^{3}
       |s_x-\operatorname{Ad}(Y_{x,i})s_{x+\hat i}|^2 .
\]
Here and below the sum ranges over all spatial sites \(x\) and the three positive directions \(i\). Write \(n_Y(u)=(3N^3)^{-1}\operatorname{Tr}{\bf1}_{[0,u]}(L_Y)\) and \(b=1+\beta\). These definitions are gauge invariant. This operator acts on spatial colour vectors. The physical time transfer acts on functions of a whole spatial configuration.

**PROVED.** There are positive absolute constants \(c,C,u_0\) such that for \(0<u<u_0/b\) and \(N\ge C u^{-1/2}\),
\[
 c u^{3/2}\exp[-C u^{-3/2}(b+\log(1/u))]
 \ \le\ {\mathbb E}\,n_Y(u)\
 \le\ \exp[-c u^{-3/2}\log(1/(Cbu))].                         \tag{1}
\]
The constants can be chosen with \(Cu_0<1\) in the upper logarithm. Both inequalities hold uniformly conditional on the exact links off the spatial slice. They therefore also hold on a two-step temporal bridge, with arbitrary ends. In temporal gauge the bridge density of its middle slice has the ordinary spatial plaquettes and two extra single-link terms per bond with coefficients of magnitude at most \(\beta\) each. Integrating endpoint gauges preserves a uniform inequality.

**PROVED.** Here is the upper bound. Use the two plaquettes based at the centre of each \(3^3\) cell, one northeast and one southwest in the \(12\)-plane, from row 1141. If \(D\) is the minimum over unit adjoint vectors of the sum of their two squared displacements around the plaquettes, the proof of (3)–(4) there gives, at every threshold \(v>0\),
\[
 {\mathbb P}(D<v\mid\hbox{links outside the cell})\le C b v.       \tag{2}
\]
Indeed write the imaginary parts of the two unit quaternions as \(u_1,u_2\). When \(|u_1|\ge |u_2|\), \(D\ge2|u_2\times\widehat u_1|^2\), by the determinant and trace of their Gram matrix. With the first loop fixed, expose a private link in the second. The row's one-link cap estimate bounds the probability on the right scale by \(C b v\). Interchange the two roles to cover the other ordering. Each private link has a conditional tilt of Haar with parameter at most \(6\beta\), including with the stated bridge ends. This is where the Wilson law enters. [One-link cap and Gram estimates](gap-crux2-astra62.md)

**PROVED.** In a rectangle \(B\) of sides in \([r,2r]\), \(r\ge6\), use disjoint cells, numbering \(M\ge |B|/6^3\). If at least \(M/2\) roots have \(D\ge v\), the internal-bond Neumann form \(Q_B\) obeys
\[
             \|s\|_B^2\le (C_1 r^2+C_2/v)Q_B(s).                 \tag{3}
\]
For \(f=|s|\) the sum of scalar squared differences is bounded by \(Q_B\), by unitarity. The rectangle variance around its ordinary mean is at most \(6r^2 Q_B\), by replacing the three coordinates in turn between two uniform points. At a good root, telescope transported differences round each of its two four-edge loops. This gives \(v|s_x|^2\le4\sum_{\text{two loops}}|s_z-\operatorname{Ad}(Y_{zy})s_y|^2\). Their edges are disjoint across cells. Bound the constant part of \(f\) using \(\bar f^2\le2(f_x-\bar f)^2+2f_x^2\) at the good roots. Their positive density proves (3), as in row 1141. [Block estimate](gap-crux2-astra62.md)

**PROVED.** Choose \(r=\lfloor\kappa u^{-1/2}\rfloor\) with \(C_1\kappa^2<1/4\), then \(v=K u\) with \(C_2/K<1/4\). Decrease \(u_0\) until \(r\ge6\) and \(C b v\) in (2) is sufficiently small. For any specified \(j\) cells the probability they are all bad is at most \((Cbv)^j\). Successive conditioning works because the previous indicators read links outside the next cell. Thus the probability that a rectangle fails (3) is at most \(2^M(Cbv)^{M/2}\). Partition the torus coordinate intervals into lengths in \([r,2r]\) by merging a final short remainder. Dropping bonds between rectangles decreases the form. Good rectangles have their entire spectrum above \(u\). The min–max principle bounds the eigenvalue count by \(3\sum_{\text{bad }B}|B|\). Taking the expectation gives the right side of (1) since \(M\ge c u^{-3/2}\). This counts localized modes even on volumes where at least one bad rectangle is likely.

**PROVED.** For the lower bound pack side-\(s\) spatial cubes with at least one vacant layer between any nearest pair, where \(s=\lceil 4\pi u^{-1/2}\rceil\). On a torus with \(N\ge4(s+1)\), at least \(c(N/s)^3\) such cubes fit by taking regularly spaced starts in each direction and leaving a periodic gap at the end. In each cube ask that every internal spatial link lie within chord distance \(\eta=\sqrt{u/48}\) of the identity quaternion. Each full one-link conditional density is at least \(e^{-12\beta}\) times probability Haar, by the bound on its tilt. A cap of chord radius \(\eta<1/2\) has Haar measure at least \(c\eta^3\). This follows by parametrizing near the identity by its three imaginary coordinates of length at most \(\eta/2\), whose surface Jacobian is at least one before the constant normalization. Exposing at most \(3s^3\) links bounds the event probability below by \((c e^{-12\beta}u^{3/2})^{3s^3}\), uniformly in the exterior.

**PROVED.** On this event use the product of the three positive Dirichlet sine ground states on \(\{1,\ldots,s\}\), extended by zero, as amplitude \(\phi\) for a constant colour vector \(t\). Its scalar Dirichlet quotient is \(6(1-\cos(\pi/(s+1)))\le3\pi^2/(s+1)^2\), by the sine addition formula. On each internal bond, with \(|t|=1\), the extra energy is \(\phi_x\phi_y|t-\operatorname{Ad}(Y_{xy})t|^2\le4\eta^2\phi_x\phi_y\). The sum of the products is at most \(3\|\phi\|_2^2\). The quotient on this three-dimensional trial space is consequently below \(u\). Distinct packed cubes have orthogonal trial spaces and no form cross terms. Min–max followed by expectation proves the left side of (1). Independence of the cubes is unnecessary.

**PROVED.** In particular every fixed bare coupling has a strictly positive expected fraction of spatial adjoint modes below each sufficiently small positive \(u\), uniformly for arbitrarily large spatial volumes. Along \(\beta=O(\log(1/u))\), (1) gives
\[
        -\log {\mathbb E}n_Y(u)\asymp u^{-3/2}\log(1/u)
        \quad (u\downarrow0,\ N\ge C u^{-1/2}).                         \tag{4}
\]
The constants may depend on the coefficient in the logarithmic upper bound for \(\beta\). This is an estimate for the integrated spectral weight in the original measure, including the rare regions allowed by the earlier typical-cube estimate.


## What the actual time transfer pays for these modes

**PROVED.** Put \(A=\{Y:\lambda_{\min}(L_Y)\le u\}\). From (1), the probability of \(A\) on every two-step bridge is at most
\[
       p=\min\{1,3N^3\exp[-c u^{-3/2}\log(1/(Cbu))]\}.                 \tag{5}
\]
Let \(T\) denote the ordinary positive Wilson time transfer on the gauge-invariant spatial Hilbert space and \(R=T/\|T\|\). In the spatial Haar representation its kernel is the product of the square-root spatial weights at the ends and the temporal Wilson bond factors, averaged over the endpoint gauge. This kernel is pointwise positive. Convolution of the two one-step kernels therefore gives, pointwise,
\(0\le (R{\bf1}_A R)(X,Z)\le pR^2(X,Z)\).
For arbitrary \(f\), replace it by \(|f|\) on both sides of the integral for its quadratic form. Then \(\|{\bf1}_A R\|\le\sqrt p\). On the spectral subspace of \(H_a=-a^{-1}\log R\) of energies at most \(E\), \(R^{-1}\) has norm at most \(e^{aE}\), whence
\[
          \|{\bf1}_A{\bf1}_{[0,E]}(H_a)\|\le e^{aE}\sqrt p .             \tag{6}
\]
The bridge-to-transfer argument is the one used for curvature events in [row 1215, near (21)](gap-solve23-astra62.md). It also applies to the bounded multiplication observable \(n_Y(u)\) by replacing \({\bf1}_A\) by \(n_Y(u)\) inside the kernels and using its square root in the norm on the left. In this version use the upper bound in (1) for \(p\), with no \(N^3\). In particular it controls the expected spectral fraction in *every* normalized state of physical energy at most \(E\).

**PROVED.** On a fixed physical cube the rare slices can be removed even from a thermal trace at physical time. Write \(Q=1-{\bf1}_A\), \(T_Q=QTQ\), and let \(\lambda,\lambda_Q\) be their top eigenvalues. If \(p<1/4\), then
\[
  1-\frac{p}{1-p}\ \le\ \frac{\lambda_Q}{\lambda}\ \le 1,\qquad
  1-kp\ \le\
       \frac{\operatorname{Tr}(T_Q^k)}{\operatorname{Tr}(T^k)}
       \ \le 1\qquad (k\ge4).                                          \tag{7}
\]
Indeed, for a normalized positive vacuum \(\psi\) of \(T\), (6) gives \(d=\|{\bf1}_A\psi\|^2\le p\). The Rayleigh quotient of \(Q\psi\) for \(QRQ\) is at least \((1-2d)/(1-d)\) since \(R\) is positive as an operator. The trace ratio is the probability on the ordinary periodic time circle that all \(k\) slices avoid \(A\). Its complement is bounded by summing the one-slice bridge bounds. The same statements hold in the spatial centre-neutral sector because its projector averages the spatial centre flips, each term in the inserted trace is an integral with positive weight and a centre identification at the seam. The bridge estimate is uniform also with flipped endpoints. The vacuum is centre invariant by uniqueness of the positive top vector, and \(Q\) is centre invariant because \(L_Y\) uses adjoint transport.

**PROVED.** For \(\beta\asymp\log(1/a)\), choose \(u=d_0/(1+\beta)\) with a fixed sufficiently small \(d_0>0\). At \(N=O(a^{-P})\) satisfying (1), (5) tends to zero faster than any power of \(a\) since \(u^{-3/2}\asymp(\log(1/a))^{3/2}\). Equations (7) and \(k=O(1/a)\) show that the vacuum-normalized thermal traces for \(T\) and \(T_Q\) have ratio tending to one, also in the neutral sector. This compares traces as a ratio even when they are large. The one-cube upper bound would follow from the same strict upper bound on the remaining trace. A low-lying mode that depends on concentrating the transfer state on the removed slices cannot supply a missing near-vacuum level by (6).

**OPEN.** On the remaining slices the bare spatial colour Laplacian is coercive at scale \(1/b\), but the Wilson transfer still has its interacting singlet sector. A way to use this information would be to control propagation between separated local curvatures after summing over the paths joining them. The next calculation estimates that sum for the covariant Green function. It permits paths of arbitrary length and repeated visits to the same link.


## A volume-uniform bound for propagation of adjoint colour

**GUIDE.** A related proposal already appears in [row 1244, §3.1](gap-mini-solve-aa-opus.md) and [the subsequent analysis, §§3.1–3.6](gap-mini-solve-ac-opus.md). The latter proves a deterministic Combes–Thomas estimate given a lower spectral bound, and suggests a typical range of order \(\sqrt{1+\beta}\). Requiring a fixed-radius net of good sites throughout an arbitrarily large volume is problematic in view of the lower bound in (1). The following argument estimates a matrix element averaged in the actual Wilson law, including all the bad regions.

**PROVED.** Let \(d=3\) or \(4\), let \(D\) be a finite nonwrapping coordinate box, and take the Dirichlet adjoint covariant Laplacian \(L_{U,D}\) with unit mesh, extending vectors by zero off \(D\). In three dimensions use the spatial links on one time slice. In four use the spacetime links. There are constants \(c,C>0\), depending only on \(d\), for which, for \(x,y\in D\) and \(r=|x-y|_\infty\),
\[
 {\mathbb E}\,\big\| (L_{U,D}^{-1})(x,y)\big\|_{\rm op}
       \ \le\ C(1+r)^{2-d}\exp[-c r/\sqrt{1+\beta}].                    \tag{8}
\]
The estimate is uniform over the size of the box, the torus containing it and the Wilson fields fixed outside its internal links. In \(d=3\) this includes arbitrary two-step bridge ends. Here the norm is the norm of a three-by-three colour matrix. The conclusion includes the path sum with its repeated edges and self-intersections.

**PROVED.** Put \(P_U=I-L_{U,D}/(4d)\), extended as the zero matrix outside \(D\). Inside \(D\), a step stays with weight \(1/2\) and each nearest-neighbour step has weight \(1/(4d)\) times its orthogonal transport. Write \(P\) for the scalar lazy walk with these weights on \(\mathbb Z^d\) and \(p=P^4(0,0)>0\). In four steps from \(z\) to \(z\) there are two specified paths around the northeast and southwest plaquettes used in (2), each of weight \(h=(4d)^{-4}\). The path that stays at \(z\) contributes at least \(hI\). If both loops are internal, combine these three pieces before taking the norm. For their two transports \(A_1,A_2\), the identity behind row 1141, (5), gives
\[
      \|I+A_1+A_2\|\le 3\sqrt{1-D_z/9}\le 3-D_z/6,
      \qquad D_z=\min_{|v|=1}\sum_{i=1}^2|v-A_i v|^2 .
\]
If a loop leaves \(D\), its whole weight \(h\) is missing from the diagonal bound by the full scalar walk. Mark \(z\) good in this boundary case and outside \(D\). At remaining sites mark it good if \(D_z\ge c_0/b\), with \(c_0>0\) small enough in (2). Each mark has probability at least \(1/2\) conditional on all links off its two loops. This remains true if other marks, supported on disjoint links, have been exposed. Thus for some \(0<\gamma<1\) independent of \(\beta\),
\[
       \|P_U^4(z,z')\|\le K_U(z,z'),\qquad
       K_U(z,z')=P^4(z,z')
        \big(1-(\gamma/b)\,{\bf1}_{z=z'}{\bf1}_{z\ {\rm good}}\big).
                                                                         \tag{9}
\]
This is a substochastic scalar kernel. Realize it by a walk with independent increments of law \(P^4(0,\cdot)\), killed with probability \(\gamma/b\) on a holding step at a good site. Conditional on the environment the killing coins are independent. Products of the matrix blocks in (9) give \(\|P_U^{4k}(z,z')\|\le K_U^k(z,z')\).

**PROVED.** The scalar walk has the following estimates, with time counted in four-step increments. If \(S_j\) denotes its position, \(p_j(z,z')=\Pr_z(S_j=z')\), then
\[
 p_j(z,z')\le C(j+1)^{-d/2}e^{-c|z-z'|_\infty^2/(j+1)},\qquad
 \sum_{j\ge0}p_j(z,z')\le C(1+|z-z'|_\infty)^{2-d}.                    \tag{10}
\]
The characteristic function of one original lazy step is
\(\phi(\theta)=1/2+(2d)^{-1}\sum_i\cos\theta_i\), lying in \([0,1]\). On \([-\pi,\pi]^d\), \(1-\phi\ge c|\theta|^2\). Integrating \(\phi^{4j}\) gives the uniform bound \(C(j+1)^{-d/2}\) by Fourier inversion. A single coordinate increment of the four-step walk is symmetric and bounded by four. Its moment generating function is at most \(\cosh(4t)\le e^{8t^2}\). Exponential Markov and optimization give a Gaussian tail for the displacement of a coordinate in \(j\) steps. Split the convolution at \(\lfloor j/2\rfloor\). One of the two displacements in a coordinate realizing \(|z-z'|_\infty\) is at least half that distance in absolute value. Sum that half using the tail and bound the other half by the uniform Fourier estimate, using symmetry to reverse a half if necessary. Small \(j\le1\) are absorbed by increasing \(C\). Summing dyadically over \(j+1\) below and above \((1+|z-z'|_\infty)^2\) gives (10), since \(d>2\).

**PROVED.** Consider \(n\) increments of this scalar walk from an arbitrary site. There are constants \(\delta,c_1>0\) such that with probability at least \(\delta\) it makes holding steps at \(c_1n\) sites at mutual \(\ell^\infty\) distance greater than four, and its displacement in a specified coordinate stays below \(L/2\) throughout. Here take \(n=\lfloor c_2 L^2\rfloor\), with \(c_2>0\) fixed sufficiently small and \(L\) above a fixed constant. For the holding count \(H\), its mean is \(pn\) and its variance is \(p(1-p)n\) by increment independence. Thus \(\Pr(H<pn/2)\le1/8\) for large \(n\). For the count \(J\) of ordered pairs of times in \(\{0,\ldots,n-1\}\) with positions within four of each other, (10) gives \({\mathbb E}J\le C n\sum_{k\ge0}(k+1)^{-d/2}\le C' n\). Except on probability \(1/8\), \(J\le8C'n\). Form the graph of the holding times, joining close positions. There is an independent set of at least \(H^2/J\) times. To see this, order the vertex list uniformly and keep vertices earlier than all their neighbours. The expected count is the sum of reciprocal closed degrees, at least \(H^2/J\) by Cauchy–Schwarz. Use a fixed tie-breaking rule to select a sufficiently large set for each path. Finally the centered coordinate is a martingale of variance at most \(16n\). Stopping its square at the first displacement of size \(L/2\) shows the crossing probability is at most \(64 n/L^2\), which can be made at most \(1/8\). The intersection has the claimed positive probability.

**PROVED.** Set \(L=\lceil C_0\sqrt b\rceil\), choosing \(C_0\) so that \(n\) meets the preceding lower size requirement and \(n/b\) is bounded below. Starting from \(x\), place successive record planes along a chosen directed coordinate at distances \(4L,8L,\ldots\). At the first crossing of a plane the overshoot is at most three. Run the preceding trial for at most \(n\) steps, stopping it early if the walk leaves the slab of width \(2L\) centred on that plane. The trial terminates before the next plane can be reached. For the event just proved all its selected holds are inside the slab, including their two plaquettes with a bounded margin if \(C_0\) is enlarged. Different trials inspect disjoint sets of possible links. Conditional on the path of the trial and all previously inspected marks, each of these separated hold sites is good with probability at least \(1/2\), successively. The probability of surviving all their coins is at most \((1-\gamma/(2b))^{c_1 n}\). To justify conditioning at record times, run the underlying scalar walk independently of the Wilson field. Keep only kills at the selected holds of completed successful trials, disregarding other potential kills. A trial's selection reads only the current segment of the scalar path, and can be resolved at its stopping time, before the next trial starts. Conditional on the past at a record time, the new increments have their original law. The previous tests give information only about links in previous slabs and independent coins. The conditional probability of losing the walk in the new trial is consequently at least \(\delta[1-\exp(-c_1\gamma n/(2b))]\), a positive absolute constant. This also covers paths that leave a finite box since (9) dominates the Dirichlet walk there. Iterating the bound on survival and reaching the next plane proves that the annealed probability of reaching coordinate distance \(R\) alive is at most \(C\exp[-cR/\sqrt b]\). Paths failing to reach the next plane contribute zero to its hitting probability.

**PROVED.** To estimate \(\sum_{k\ge0}{\mathbb E}K_U^k(x,y)\), stop at the first crossing of a plane halfway to \(y\) in a coordinate with displacement \(r\). Any visit to \(y\) requires that crossing. For fixed \(U\), the remaining expected number of visits is bounded by the free Green function from the crossing point. Its distance from \(y\) is at least \(r/2-4\). Equation (10) thus contributes \(C(1+r)^{2-d}\), uniformly in that point. Combine this bound with the annealed crossing probability. Distances \(r\le12\) use (10) directly. The other three residues of the number of lazy steps modulo four append at most three free steps to the kernel. Summing over their starting sites changes the bound by at most an absolute factor. In a finite Dirichlet box the scalar lazy walk has spectral radius below one, since the box can be exited in a bounded number of steps with uniformly positive probability at fixed box size. Hence \(L_{U,D}^{-1}=(4d)^{-1}\sum_{k\ge0}P_U^k\). These arguments prove (8), in fact with the sum of expected block norms of the individual powers in place of the norm of the sum.

**PROVED.** Summing (8) in \(y\) gives \(\sup_x\sum_y {\mathbb E}\|L_{U,D}^{-1}(x,y)\|\le C b\). More generally, for field-dependent colour sources bounded pointwise by deterministic envelopes \(f_x,g_y\), the expected absolute value of their pairing through the Green kernel is bounded by \(\sum_{x,y}C f_x g_y(1+r)^{2-d}e^{-c r/\sqrt b}\). The sources may depend on the links on every path in the sum. This controls mean local pairings uniformly in volume. An operator-norm estimate uniform over all samples would have to account for the rare configurations in (1).


## Testing the colour estimate in the interacting time layer

**GUIDE.** The comparison can be tested on the original Wilson measure without replacing the temporal links by Gaussian variables. In the notation below the distinction matters even after averaging over the two spatial boundary fields. The earlier cut analysis posed a related replica-overlap question for a different conditional law and finite coupling interval. [Conditional overlap in the cut problem, §§5–6](gap-cuttyp-max.md)

**PROVED.** Let \(X,Y\) be the spatial link configurations in two adjacent slices of an ordinary periodic Wilson four-torus of sides \(N\ge 4\). Write \(g_x\) for the temporal link between them. Conditional on \(X,Y\), the law of the \(g_x\)'s is
\[
 \pi_{X,Y}(dg)=Z(X,Y)^{-1}\exp\!\left[\beta\sum_{e=xy}
       g_x\cdot R_e g_y\right]\prod_x dg_x,\qquad
 R_e q=X_e qY_e^{-1},                                                   \tag{11}
\]
where \(u\cdot v=\operatorname{Re}(u^{-1}v)\) on \(\mathbb R^4\). Each plaquette containing one of these \(g\)'s is a side face joining the two slices. All other factors can be integrated out independently of this layer once \(X,Y\) are fixed. In particular \(\int g_x\,d\pi=0\) by simultaneous replacement of all \(g\)'s by \(-g\). Let \(L_{X,Y}\) be the spatial covariant Laplacian with the orthogonal transports \(R_e\).

**PROVED.** On any nonwrapping Dirichlet box \(D\), the estimate (8) holds for \(L_{X,Y,D}^{-1}\) with \(d=3\). Its expectation may even be taken conditionally on \(Y\) and all four-dimensional links outside the internal \(X\)-links of the box, *in the original joint Wilson law*. To prove this replace the two-loop test by a one-loop test. For a square \(p\), let \(\theta_X,\theta_Y\in[0,\pi]\) be the two class angles. Then
\[
       \min_{|q|=1}|q-X_p q Y_p^{-1}|^2
            =2[1-\cos(\theta_X-\theta_Y)] .
\]
Conjugation by \(q\) can align the imaginary axes, which maximizes the scalar product of the two unit quaternions. Centre elements satisfy the same formula. Expose one internal \(X\)-link with the other links fixed. Its tilt has length at most \(6\beta\). The angle-density estimate of [row 1155, proof of (20)](gap-solve7-astra62.md) bounds the density of \(\theta_X\) by \(C\sqrt b\) uniformly in the tilt and its direction. Thus the displayed minimum is below \(c_0/b\) with probability at most \(1/2\) for small \(c_0>0\), also conditional on the links off the square in this experiment. Combine one weight-\(h\) identity return with this plaquette return using \(\|I+A\|^2=4-\min_{|q|=1}|q-Aq|^2\) for orthogonal \(A\). This gives the same loss \(c/b\) on good holding sites in (9). The rest of the crossing proof is unchanged. The conclusion concerns the marginal of a genuine pair of Wilson slices, with no independence assumption on the slices.

**PROVED.** For a fixed pair \(x,y\), the connected spin covariance of (11) is the real four-by-four matrix \(C_{xy}(X,Y)=\int g_y g_x^{\mathsf T}\,d\pi\). For \(y=x+r\hat i,\ 1\le r<N\), it obeys
\[
       {\mathbb E}\|C_{xy}(X,Y)\|_*
           \ \ge\ {\mathbb E}w(U_{1\times r})
           \ \ge\bigl(1-C/\beta\bigr)^r\qquad(\beta\ge 2C).             \tag{12}
\]
Here \(\|\cdot\|_*\) is the sum of the singular values. Along the straight path let \(O q=X_{\rm path}qY_{\rm path}^{-1}\). It is orthogonal and is fixed by \(X,Y\). Contracting \(C_{xy}\) with \(O\) gives the conditional rectangle expectation. Trace duality and averaging prove the first inequality. The second is the thin-rectangle reflection/transfer inequality used in row 1153, which represents the rectangle expectation in the propagation direction as the \(r\)-th moment of a positive eigenvalue ratio under a probability measure (the width-one spatial link, with its two colour indices, acts isometrically). Its first moment is the mean fundamental plaquette, at least \(1-C/\beta\). Jensen gives (12). Credit for the reflection method belongs to Bachas and for the Wilson transfer to Osterwalder–Seiler and Lüscher. [Transfer moment and plaquette estimate](gap-solve6-astra62.md) · [Strip bound (1)](gap-solve13-astra62.md)

**PROVED.** At \(r=\lfloor\beta^{3/4}\rfloor\), \(N>4r\), (12) tends to one, while \(\|C_{xy}\|_*\le1\) since it averages rank-one unit tensors. On the same ordinary ensembles the expected norm of the Dirichlet Green block for \(L_{X,Y}\) is at most \(Cr^{-1}\exp(-c\beta^{1/4})\) by (8). Thus no fixed polynomial in \(1+\beta\) times that expected Green norm can dominate the averaged covariance of the unit spins in (11) on all these boxes. This failure uses the actual interacting boundary distribution. It persists in the weak-coupling regime in which both slices have a coercive spatial adjoint Laplacian with high probability by (5) on polynomial-in-\(1/a\) volumes with \(\beta\asymp\log(1/a)\), because either slice's exceptional event changes the lower bound by at most its probability. This tests the intermediate spin model, where \(C_{xy}\) is a conditional covariance with colour indices.

**PROVED.** A version summed over an entire patch has a gauge-invariant interpretation in two conditionally independent copies of (11). From one root choose coordinate-order paths to sites in a spatial cube \(B\) of side \(\ell<N/4\). Denote their two-sided transports by \(O_x\) and set \(F=|B|^{-1}\sum_{x\in B}O_xg_x\), with the root in \(B\). For paths of at most three straight segments, telescope the end mismatch along the segments. The squared mismatch on a segment of length \(h\) has actual mean at most \(C h/\beta\) by (12) and \(|u-v|^2=2(1-u\cdot v)\) for unit quaternions. Cauchy–Schwarz for the three segments and Jensen for the site average give the first bound below. For the second, \(1-|F|^2\) is the site variance of the transported unit vectors, at most their mean squared distance from the root spin. Thus
\[
 {\mathbb E}|F-g_{\rm root}|^2\le C\ell/\beta,\qquad
 {\mathbb E}\int |F|^2d\pi\ge 1-C\ell/\beta .                           \tag{13}
\]
For the second bound use \(|F|^2\ge2F\cdot g_{\rm root}-1\) and average the individual endpoint squared mismatches. This extra argument retains the linear, rather than square-root, error. For any two sites use the two paths via the root, with at most six segments. Hence the contraction of \(C_{xy}\) with \(O_x^{-1}O_y\) has expectation at least \(1-C\ell/\beta\). Since \(\|O_x^{-1}O_y\|_{\rm F}=2\), Cauchy–Schwarz gives \({\mathbb E}\|C_{xy}\|_{\rm F}^2\ge (1-C\ell/\beta)_+^2/4\). For independent replicas \(g,g'\) conditional on \(X,Y\), put \(s_x=g_x\cdot g'_x\). Direct expansion gives \(\int s_xs_y\,d\pi^{\otimes2}=\|C_{xy}\|_{\rm F}^2\). The replica dot products are invariant under endpoint gauge changes. In particular,
\[
       {\mathbb E}\int\left(|B|^{-1}\sum_{x\in B}s_x\right)^2
           d\pi^{\otimes2}\ge \tfrac14(1-C\ell/\beta)_+^2 .              \tag{14}
\]
The expectation is in the same ensemble as the Green estimate. The scale in (14) is measured in lattice spacings.

**PROVED.** For \(\ell=o(\beta)\) growing, (13) also yields an upper bound on the auxiliary relaxation rate on typical layers. With probability \(1-O(\ell/\beta)\) over \(X,Y\), \(\int |F|^2d\pi\ge1/2\), by Markov applied to its nonnegative deficit from one. Each component is centered and some component has variance at least \(1/8\). Its total squared gradient on the product of unit three-spheres is at most \(1/|B|\) pointwise, because each of the \(|B|\) spins enters with one coefficient of norm \(1/|B|\). The spectral gap for this layer's continuous single-spin gradient form on odd functions is at most \(8/|B|\). There is a corresponding normalized side-\(s\) heat-bath upper bound \(C s^3/|B|\) for \(1\le s\le\ell\), since changing spins in an update cube changes the component by at most twice the intersection size divided by \(|B|\). The sum of the squared intersection sizes is at most \(s^3\sum_z |B\cap(z+[0,s)^3)|=s^6|B|\). Divide by \(s^3|B|^2\) and by the variance. These odd tests concern a conditional three-dimensional layer. The four-dimensional cube tests and the neutral physical transfer have different quantifiers.


## Recovering the adjoint of a temporal link from two spatial slices

**PROVED.** Work on ordinary even \(N^4\) Wilson tori with \(\beta\to\infty\), \(\beta\le B_0\log N\) for fixed \(B_0\). For each \(0<\eta<1/24\), there is a gauge-covariant matrix reading \(\widehat R_x(X,Y)\) of just the two adjacent spatial slices in (11) with
\[
    {\mathbb E}\|\widehat R_x-\operatorname{Ad}g_x\|_{\rm F}^2
           \le C_{\eta,B_0}\beta^{-\eta}.                                \tag{15}
\]
Its spatial radius is \(O(\beta^{1/30})\). No temporal link is read by the estimator. The scale exponent and error here are bounds from the open-box comparison. The comparison of linear curvatures in tree gauge is due to [rows 1151 and 1231](gap-solve26-astra62.md), building on Sourav Chatterjee's weak-coupling free-energy method. The free curvature projection is that of Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. [Open-box density and entropy bounds](gap-solve5-astra62.md) · [Their projection symbol, outline 1733–1762](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L1733-L1762)

**PROVED.** Choose \(2\eta<\gamma<1/12\), \(h=\lceil\beta^\gamma\rceil\), \(m=\lfloor h^{2/5}\rfloor\) and \(K=\sqrt{A\log\beta}\) with \(A\) a sufficiently large fixed number. Use the \(m^3\) spatial \(12\)-plaquette bases \(z\) in \(x+[0,m)^3\), and a coordinate-order path from \(x\) to \(z\) in each slice. Let \(a_z,b_z\) denote \(\sqrt\beta\,\operatorname{Im}U_{12}(z)\) in the respective slice, transported to its root by the adjoint of that slice's path. Write \(T_K\) for Euclidean projection onto the radius-\(K\) ball in \(\mathbb R^3\). Form
\[
                      M_x=m^{-3}\sum_z T_K(a_z)\,T_K(b_z)^{\mathsf T}.    \tag{16}
\]
If \(R=\operatorname{Ad}g_x\), then \(M_x R^{\mathsf T}\) uses both colours in the lower root frame. Under a pair of root gauge rotations \(L,H\), \(M_x\mapsto L M_x H^{\mathsf T}\) and \(R\mapsto L R H^{\mathsf T}\). Thus the loss from a scalar multiple of \(R\) is a gauge-invariant joint test. The fact that \(R\) enters the *proof* of the loss bound permits transporting the second set through the short temporal link while retaining a common frame.

**PROVED.** In the periodic free lattice model write \(P\) for the orthogonal projection on exact real two-forms, and use three independent copies of \(PZ\) with \(Z\) standard Gaussian. Let \(d_N=P((0,12),(\hat t,12))\), between plaquettes at the same spatial coordinates. This scalar is bounded below by an absolute \(d_*>0\) for all sufficiently large \(N\). For a nonzero spatial frequency \(q\), set \(s_i=2\sin(q_i/2)\), \(s^2=\sum_i s_i^2\) and \(\omega=2\operatorname{arsinh}(\sqrt{s^2}/2)\). The time multiplier of the \(12,12\) projection is \((s_1^2+s_2^2)/(s^2+2-2\cos k_t)\). On the infinite time line the Fourier coefficient of its reciprocal denominator at \(j\) is \(e^{-|j|\omega}/(2\sinh\omega)\), by substitution in the second-order difference equation with a unit source at zero. Periodize this summable positive kernel at time period \(N\). At time one a lower bound follows from the unperiodized time-one term for \(q_1\in[\pi/3,2\pi/3]\), with the other two coordinates unrestricted. A fixed positive fraction of spatial frequencies lie there and the numerator and kernel both have positive lower bounds on that set. The zero spatial frequency contributes zero. This is the same covariance as [row 1231, (4)](gap-solve26-astra62.md).

**PROVED.** The *unclipped* free analogue of (16), in common coordinates, has mean \(d_N I_3\), and
\[
          {\mathbb E}_{G}\|M_x^{\rm free}-d_N I_3\|_{\rm F}^2
                   \le C/m^3 .                                          \tag{17}
\]
For one matrix entry pair the four Gaussian colour coordinates at two bases \(z,z'\). After subtracting the means the two pairings are products of two \(P\)-entries, with colour Kronecker factors of absolute value at most one. For fixed \(z\), the sum over \(z'\) of the absolute products is at most one per pairing, because every row of the orthogonal projection has squared norm at most one. Sum over \(z\), divide by \(m^6\), and sum nine entries. Clipping alters the expected Frobenius difference by at most \(C e^{-cK^2}\) by Cauchy–Schwarz and the Gaussian tails (all one-colour variances are at most one).

**PROVED.** The Wilson comparison needed here is for a matrix of products of two vectors in one frame. This calls for tracking both vector transports in the earlier comparison of curvature magnitudes. Apply the bounded test \(H(M)=\min(1,\|M-d_N I_3\|_{\rm F})\) to the common-frame reading and average its spatial and temporal anchor over all \(V=N^4\) lattice sites. The Wilson law is translation invariant. For any pair of arrays the variation of \(H\) on clipped outer products is bounded by the mean over the window of \(K(|\delta a_z|+|\delta b_z|)\). In particular, once transports are removed, the translated average varies by at most \(2K\|\delta F\|_2/\sqrt V\) in a common curl array because each translated offset occurs equally often. This bound has no factor \(m^3\).

**PROVED.** Use the disjoint open \(h^4\) boxes in the cited Wilson comparison. The fraction of translates for which the joint window (including its short temporal link and its paths) crosses a box boundary or lies in a discarded strip is at most \(C[(m+1)/h+h/N]\). For a window in one box the probability its tree logarithms leave the good chart is at most \(C e^{-c\beta/h^8}\). The test lies in \([0,1]\), so these costs need no moment bound. In a good box the whole test can be evaluated in that box's single tree gauge because \(H\) is invariant under conjugation in the common root frame. By (8) of row 1231, replacing \(\sqrt\beta\,\operatorname{Im}U_p\) by its linear curl costs \(O(h^{-1})\) in translated mean norm, from its squared estimate summed over all good boxes and \({\mathbb E}\sum_p\beta(1-w_p)\le CV\). The transports, including \(g_x\), use at most \(3m+1\) links per vector, each with logarithm at most \(h^{-7/2}\). Replacing their adjoint matrices by the identity costs \(O((m+1)h^{-7/2})\) in mean vector norm using the same second moment. In the test multiply these two errors by \(CK\).

**PROVED.** For the remaining linear curl array substitute independent diluted Gaussian draws in bad boxes and put zero on omitted faces, as in the proof of row 1151, (24). Its relative entropy to the corresponding product Gaussian curl law is at most \(CV\Delta_h\) with \(\Delta_h=(\log\beta)(1/h+h/N)\). The translated bounded test is \(CK/\sqrt V\)-Lipschitz on the reference standard normals, since the diluted projection has bounded operator norm. The Gaussian exponential-moment bound and entropy inequality proved in that row give expectation error \(CK\sqrt{\Delta_h}\). Passing from these open Gaussian curls to \(PZ\) uses the projection coupling of row 1231, (1), with mean-square error per face \(C(1/h+h/N)\) including the dilution and zeroed entries. For the translated test this costs \(CK\sqrt{1/h+h/N}\). These uses of entropy and Gaussian integration are analytic inequalities. Combining them with (17) gives
\[
 \begin{split}
 {\mathbb E}H(M_xR^{\mathsf T})\le C\big[&
     m^{-3/2}+e^{-cK^2}+(m+1)/h+h/N+e^{-c\beta/h^8}\\
     &+K(\sqrt{\Delta_h}+h^{-1}+(m+1)h^{-7/2})\big].
 \end{split}                                                            \tag{18}
\]
Here the replacement of the actual test by the average of the full linear-array test on crossing or bad windows costs at most their previously counted fraction. Since \(h^{12}=o(\beta)\), \(N\ge\exp(\beta/B_0)\), and \(2\eta<\gamma\), the right side is \(O_{\eta,B_0}(\beta^{-\eta})\).

**PROVED.** Define \(\widehat R_x\) by projecting \(M_x/d_N\) onto the closed Frobenius ball of radius \(\sqrt3\). This map fixes every rotation, is 1-Lipschitz and respects the left and right root actions. Its squared distance to \(R\) is at most \(C H(M_xR^{\mathsf T})\), using \(d_N\ge d_*\) when the matrix error is small and the diameter of the ball otherwise. Equation (18) proves (15). The estimator is a real matrix and need not itself lie in \(SO(3)\).

**PROVED.** The result sharpens the replica statement to an almost complete determination up to a common sign on mesoscopic cubes. In the setting of (14),
\[
  1- C_{\eta,B_0}\big(\beta^{-\eta}+\ell/\beta\big)
   \ \le\ {\mathbb E}\int
     \left(|B|^{-1}\sum_{z\in B} g_z\cdot g'_z\right)^2 d\pi^{\otimes2}
   \ \le 1 .                                                             \tag{19}
\]
Indeed conditional variance is bounded by the loss of any estimator measurable in \(X,Y\). Two independent draws consequently obey \({\mathbb E}\|\operatorname{Ad}g_z-\operatorname{Ad}g'_z\|_{\rm F}^2\le2C\beta^{-\eta}\). For quaternions the squared matrix difference is \(8(1-(g_z\cdot g'_z)^2)\), by the trace of the relative rotation. The spatial variance of \(s_z=g_z\cdot g'_z\) in \(B\) is at most the average of \((s_z-s_x)^2\) relative to its root \(x\). Each such difference is bounded by \(|O_zg_z-g_x|+|O_zg'_z-g'_x|\), whose mean square is \(O(\ell/\beta)\) by the strip proof of (13). Now use \(1-\bar s^2=\overline{(1-s_z^2)}+\overline{(s_z-\bar s)^2}\). In particular the even uncertainty in the adjoint orientation vanishes as \(\beta\) grows, while (14) had used only the coherence of the odd readings.


## Propagating the relative sign across an arbitrarily large spatial slice

**PROVED.** For the rest of this section take dyadic \(N\), \(\beta\le B_0\log N\), on the ordinary \(N^4\) torus. Take \(h,m\) from (15) rounded down to powers of two and set \(l=4m\). For all large \(\beta\), \(4l\mid h\mid N\). Fix one temporal layer. On the spatial grid of spacing \(l\), call a root \(z\) inaccurate in a sample if
\(\|M_z(\operatorname{Ad}g_z)^{\mathsf T}-d_N I\|_{\rm F}>\epsilon\),
where \(\epsilon>0\) is an absolute constant taken small compared with \(d_*\). The reading \(M_z\) uses (16). For every prescribed set \(S\) of distinct grid roots,
\[
       \Pr(\hbox{all roots in }S\hbox{ are inaccurate})
           \ \le\ \exp[-c\,m^3 |S|/\log\beta].                           \tag{20}
\]
The constants may depend on \(\epsilon,\gamma,A\). The one-root error in (15) allows a sparse set that crosses a macroscopic slice.

**PROVED.** Use four-dimensional tiles of sides \((l,l,l,4)\), with each selected spatial root in the middle of its tile and the two read times one and two units after the lower time face. All paths and squares for that root lie inside the tile. The site-reflection chessboard inequality bounds the probability of a specified product of events by the product of their full-dissemination probabilities to the power \(1/J\) per event, with \(J=N^4/(4l^3)\) tiles. It permits different orientations of the one-tile profile. For completeness, at opposite site planes the action splits into the contributions of the two halves conditional on the common boundary links. Cauchy–Schwarz bounds the square of a pattern's expectation by the product of the two reflected-half expectations. In one direction divide each slab function by its fully reflected expectation to the reciprocal number of slabs. In a maximizing filling by these normalized functions, both reflected fillings maximize. Starting with a constant run, reflection doubles its length until a whole period is constant. That normalized filling has value one. Apply the resulting inequality in successive directions to the products in the slabs, and obtain the stated tile inequality. Zero factors follow by adding a positive constant and taking a limit. This is the chessboard method of Fröhlich, Israel, Lieb and Simon, in the finite-torus form also given by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. [Outline 2811–2818 and 2885–2942](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2885-L2942)

**PROVED.** Write \(V=N^4\) and \(S_W=\beta\sum_p(1-w_p)\). Except on probability at most \(e^{-cV\log\beta}\), \(S_W\le C_0V\log\beta\) for a sufficiently large fixed \(C_0\). Indeed the normalized partition function in deficit convention is at least \(e^{-C V\log\beta}\), by restricting every link to a Haar ball of radius \(\beta^{-1/2}\) and using the plaquette triangle inequality there. On the upper-tail event the unnormalized density is at most \(e^{-C_0V\log\beta}\). Tile by the open side-\(h\) boxes of row 1151. A box outside its good tree chart has internal deficit sum at least \(c/h^8\) by the shelling estimate used in that row. Thus on the displayed total-action event the bad boxes occupy fraction at most \(C h^{12}\log\beta/\beta=o(1)\) of all sites. The fraction of fine tiles whose reading hits an open-box boundary is \(O(l/h)\), by counting layers. The fraction meeting a bad box is \(o(1)\) as well because the tiles have equal volume and bounded aspect in their respective coordinate tilings relative to \(h\), and thickening each bad \(h\)-box by \(O(l)\) has bounded volume ratio. These counts are uniform under shifts of either grid.

**PROVED.** Suppose the inaccurate-root event has been reflected into *every* tile. Consider the average over those tiles of the bounded test \(H\) of (18), using their reflected orientations. On the good noncrossing tiles its Wilson value is at least \(\min(1,\epsilon)\). In the good charts replace the transported colours by the rescaled linear curls. The mean change over these tiles is bounded by
\[
          C K (h^{-1}+l h^{-7/2})\sqrt{S_W/V}=o(1).
\]
Indeed the two face sets in a window have \(m^3\) members each, windows have bounded overlap, and \(Jm^3\) is a fixed positive fraction of \(V\). Use the squared-error sum (8) of row 1231 and Cauchy–Schwarz, followed by the transport bound in the proof of (18). Reflections change an oriented linear curl by a sign or move its base to another corner of the square. Both slices have the same spatial sign, so the corresponding product has the same mean. Time reversal can also transpose the product. The path lengths increase by at most a constant in identifying the corner. The loss \(H\) is invariant under simultaneous orthogonal changes of the colour frame and under transpose. The linear-array average, now with arbitrary assigned entries in bad boxes and zero on omitted faces, must therefore be at least a fixed number \(d>0\) on the full-dissemination, bounded-action event, since the lost tiles are a vanishing fraction.

**PROVED.** Bound the probability of this last deviation. Under the product diluted Gaussian curl law, the expectation of the average is \(o(1)\). To see it, couple its internal curls to \(PZ\) using the projection difference of row 1231, (1), setting the omitted entries to zero. Their total mean-square error is \(O(V/h)\), including the dilution, since \(h\mid N\). The tile average pays at most \(CK/\sqrt h\) by the same multiplicity bound \(Jm^3\asymp V\). Its mean for \(PZ\) is \(O(m^{-3/2}+e^{-cK^2})\) by (17) in each reflected orientation. As a function of the standard Gaussian input the average is \(CK/\sqrt V\)-Lipschitz because a change in the clipped product is bounded by \(K\) times the sum of the two input changes, and each face is read a bounded number of times. The product curl map has bounded norm. The Gaussian exponential-moment estimate used in (18) therefore puts its probability of exceeding \(d\) below \(\exp(-c_d V/K^2)\). To transfer this exponentially small probability one needs a density bound. Row 1151, in the proof of (24), gives the *pointwise density upper bound* \(\exp(CV\Delta_h)\) after replacing bad boxes by independent Gaussian draws. The linear-array deviation forced above holds for every such draw. Thus the full-dissemination probability is at most \(e^{-c V\log\beta}+\exp(CV\Delta_h-c_dV/K^2)\). Here \(K^2=A\log\beta\), \(K^2\Delta_h\to0\). Its \(1/J\)-th power is at most \(\exp(-c m^3/\log\beta)\), uniformly for large \(\beta\), proving (20). An entropy bound by itself would not justify this probability estimate. [Density bound in row 1151](gap-solve5-astra62.md)

**PROVED.** For each positive or negative nearest-neighbour grid edge \(e=zz'\), use the straight two-sided transport \(O_e\) of its \(l\) fine links, choosing either orientation consistently. Mark an edge if \(|g_z-O_e g_{z'}|>\epsilon_1\), for a fixed small \(\epsilon_1>0\). For any prescribed set \(E\) of distinct unoriented grid edges,
\[
                 \Pr(\hbox{all edges in }E\hbox{ are marked})
                        \le \exp[-c\beta |E|/l].                         \tag{21}
\]
The boundary chord of its \(1\times l\) strip is bounded by the sum of its elementary plaquette chords, by cancelling the internal links in a product of conjugates. A marked strip costs \(\sum_{p\ {\rm in\ strip}}(1-w_p)\ge \epsilon_1^2/(2l)\). The strip faces of distinct grid edges are disjoint and are all electric faces on the same time step. On any specified union \(A\) of such faces the half-coupling moment is \({\mathbb E}\exp[(\beta/2)\sum_{p\in A}(1-w_p)]\le C^{|A|}\). In the transfer proof one halves the coupling in the corresponding electric convolutions. Monotonicity of the nontrivial character ratios puts each vacuum-normalized half-coupling convolution below the ordinary one in positive-operator order. Each one-link scalar normalizer ratio in deficit convention costs at most \(C\). Tensor the ordered positive operators, sandwich by the spatial weight and use positivity of the other transfer powers in the trace. These are the one-link deletion and half-coupling bounds of [row 1149, (16)](gap-solve4-astra62.md) and [row 1153](gap-solve6-astra62.md). Exponential Markov gives \(\exp[-c\beta|E|/l+C l|E|]\), which implies (21) because \(l^2=o(\beta)\).

**PROVED.** Draw the two copies of the temporal layer conditionally independently as in (14). Mark a grid bond defective if either endpoint is inaccurate in either copy or if its strip is marked in either copy. For any prescribed \(k\) distinct grid bonds the probability that all are defective is at most \(\vartheta_\beta^k\), with
\[
       \vartheta_\beta\le C\exp[-c\min(m^3/\log\beta,\,\beta/l)] .        \tag{22}
\]
Indeed assign one of the six possible causes to each defective bond, ordering its two endpoints in advance. Some cause occurs at least \(k/6\) times. If it concerns roots, bounded degree six leaves at least \(k/36\) distinct roots in the same copy. Apply (20) or (21) to that copy's ordinary Wilson marginal and sum at most \(6^k\) assignments. This uses no independence of the two *unconditional* Wilson samples.

**PROVED.** Let \(t_z=\operatorname{sgn}(s_z)\) with any convention at zero. Along a nondefective bond, \(t_z=t_{z'}\). Indeed both rotations at a given good endpoint are within \(2\epsilon/d_*\) in Frobenius distance of each other by (16) and the definition of an inaccurate root. The quaternion identity in (19) gives \(|s_z|,|s_{z'}|>3/4\) for small enough \(\epsilon\). The two strip bounds and orthogonality of their common \(O_e\) give \(|s_z-s_{z'}|\le2\epsilon_1\), too small for opposite signs.

**PROVED.** On any coordinate two-torus of the grid the probability that two specified vertices fail to be joined by nondefective bonds is at most \(C\vartheta_\beta\), uniformly in the grid period \(n=N/l\). If they are disconnected, take the edge boundary of the component of the first point. Its crossed dual edges are defective primal bonds, and the dual degrees are even by the mod-two boundary identity round every primal square. Split this finite even graph into simple circuits. A primal path to the second point crosses the boundary oddly. Hence some circuit crosses it oddly. A circuit of length \(k<n\) lifts closed to the square lattice with extent at most \(k\). Its translates bound copies of its interior on the torus, so odd crossing means one of the two points is inside. For instance the coordinate span of a lifted circuit is at most \(k/2<n/2\), so its bounded interior projects injectively and ordinary inside/outside parity applies. A starting dual vertex lies within \(k+1\) of that point. For \(k\ge n\) allow all \(n^2\le k^2\) starts. The total number of candidates of length \(k\) is at most \(C(k+1)^2 4^k\). Each uses \(k\) distinct defective bonds, so (22) and summation give the asserted bound. To join arbitrary grid vertices in three dimensions, take three coordinate runs in turn and use a coordinate two-torus containing each run. A union bound gives the same estimate with a changed \(C\).

**PROVED.** Consequently the following holds uniformly over *all* spatial sites \(x,y\) in the above dyadic Wilson tori:
\[
   {\mathbb E}\int (g_x\cdot g'_x)(g_y\cdot g'_y)\,d\pi^{\otimes2}
                    \ge 1-C_{\eta,B_0}\beta^{-\eta}.                   \tag{23}
\]
For grid roots the probability of opposite signs is at most \(C\vartheta_\beta\). For a site off the grid, use at most three segments of length \(l\) to a nearest root. The mean squared difference between the two replica dot products at their ends is \(O(l/\beta)\) by the telescope in (19). At either site the expected deficit \(1-s_z^2\) is \(O(\beta^{-\eta})\) by (15). Markov then bounds the probability of a sign change on the way to the grid by \(C(l/\beta+\beta^{-\eta})\). For equal signs use \(1-|s_x||s_y|\le(1-s_x^2)+(1-s_y^2)\). For opposite signs the deficit is at most two. This proves (23). In particular the whole spatial mean \(q=N^{-3}\sum_x g_x\cdot g'_x\) has \({\mathbb E} q^2\ge1-C_{\eta,B_0}\beta^{-\eta}\). Its law is symmetric because either entire temporal layer can be flipped. This is an ordered relative sign for replicas given the adjacent spatial fields of the ordinary Wilson measure. Probabilistic bounds here follow from written inequalities.


## What survives through several time layers

**PROVED.** For temporal quaternions at two spatial points let \(\rho(a,b)u=aub^{-1}\) on the real space \(\mathbb H\) of dimension four. Its normalized Frobenius product is
\[
   \tfrac14\operatorname{tr}\big(\rho(a,b)^{\mathsf T}\rho(c,d)\big)
               =(a\cdot c)(b\cdot d).
\]
In fact \(\sum_{e=1,i,j,k}\bar e\,v e=4\operatorname{Re}v\). Taking the trace of \(u\mapsto vu w\) in that basis gives \(4\operatorname{Re}v\,\operatorname{Re}w\), which proves the identity. Thus the left side of (23) is exactly \(\tfrac14{\mathbb E}\|D_{xy}\|_{\rm F}^2\), where \(D_{xy}(X,Y)=\int\rho(g_x,g_y)\,d\pi_{X,Y}\). This matrix transfers a pair of static fundamental colour indices across one time step. A Wilson rectangle is obtained by using its spatial end paths as the two test vectors.

**PROVED.** There is an absolute \(c>0\) such that in *every* pair of boundary fields, with \(b=1+\beta\),
\[
 \|D_{xy}(X,Y)\|_{\rm op}\le e^{-c/b}\quad(x\ne y),\qquad
 \left\|\int\operatorname{Ad}g_x\,d\pi_{X,Y}\right\|_{\rm op}
                       \le e^{-c/b}.                                     \tag{24}
\]
Fix all temporal spins except \(g_x\) in (11). Its density is a translated class density \(e^{r\cos\theta}\) on \(S^3\), with \(0\le r\le6\beta\), since each of six incident edges contributes a unit vector to its field. The interval \((2\sqrt{1+r})^{-1}\le\theta\le(1+r)^{-1/2}\) has probability at least an absolute constant there because its unnormalized integral is at least \(c e^r(1+r)^{-3/2}\) and the full integral is at most \(C e^r(1+r)^{-3/2}\) by \(1-\cos\theta\ge c\theta^2\) and the \(\sin^2\theta\) Haar factor. The mean quaternion in the centred density is the nonnegative scalar \({\mathbb E}_r\cos\theta\) (pair \(\theta\) with \(\pi-\theta\)). It is at most \(1-c/(1+r)\) by this interval. For \(x\ne y\), \(g_y\) is fixed at this conditioning and left multiplication depends linearly on \(g_x\). The same bound applies to the norm of the conditional mean of \(\rho\). The conditional mean adjoint in the centred density is the scalar matrix with coefficient \(1-\frac43{\mathbb E}_r\sin^2\theta\), by rotational symmetry and the trace of the adjoint. The coefficient lies between \(-1/3\) and \(1-c/(1+r)\). Translations multiply these means by orthogonal matrices. Averaging proves (24). This is the one-link character contraction mechanism of [row 1145](gap-solve2-astra62.md), applied after fixing the spatial boundary fields.

**PROVED.** For \(1\le k<N\) let \(G_x=g_{0,x}g_{1,x}\cdots g_{k-1,x}\) be the vertical transport. Condition first on all the spatial slices, denoted by \(\mathcal X\). The temporal layers are then independent, since every electric plaquette uses links from only one temporal layer. The representation law gives
\[
  {\mathbb E}[\rho(G_x,G_y)\mid\mathcal X]
       =D_{xy}(X_0,X_1)\cdots D_{xy}(X_{k-1},X_k).
\]
In particular (24) bounds its norm by \(e^{-ck/b}\) for distinct points. At one point the conditional mean of \(\operatorname{Ad}G_x\) has the same bound. These upper bounds pass to conditioning on \(X_0,X_k\) alone by the tower property. In the opposite direction, (23) and stationarity give
\[
  \tfrac14{\mathbb E}\left\|{\mathbb E}[\rho(G_x,G_y)\mid\mathcal X]\right\|_{\rm F}^2
                \ge 1-C_{\eta,B_0} k\beta^{-\eta}                        \tag{25}
\]
in the dyadic setting of (23). For contractions \(A,B\), the deficit \(4-\|AB\|_{\rm F}^2\) is \(4-\|B\|_{\rm F}^2+\operatorname{tr}[(I-A^{\mathsf T}A)BB^{\mathsf T}]\), at most the sum of the two individual deficits. Iterate and average. Bound (25) uses observations of the intermediate spatial slices.

**PROVED.** Draw two independent interiors of a time slab conditional just on its two spatial endpoint configurations. Put \(s_x=G_x\cdot G'_x\) and \(q=N^{-3}\sum_x s_x\). From the trace identity and (24), pointwise in those endpoints,
\[
 \begin{split}
 0\le {\mathbb E}[s_xs_y\mid X_0,X_k]&\le e^{-2ck/b} \quad(x\ne y),\\
 \tfrac14\le {\mathbb E}[s_x^2\mid X_0,X_k]&\le \tfrac14+\tfrac34e^{-2ck/b},\\
 {\mathbb E}[q^2\mid X_0,X_k]&\le N^{-3}+e^{-2ck/b}.                     \tag{26}
 \end{split}
\]
For the diagonal, \(4s_x^2-1=\operatorname{tr}[(\operatorname{Ad}G_x)^{\mathsf T}\operatorname{Ad}G'_x]\). Conditional independence gives the squared Frobenius norm of the conditional mean in both trace identities. In a tuning with \(\beta\le C\log(1/a)\), any positive fixed physical time has \(k\asymp a^{-1}\gg\beta\). At such times the global overlap goes to zero as \(N\to\infty\), whereas the on-site squared overlap tends to \(1/4\). The loss is proved directly for the Wilson temporal links. It occurs on the lattice time scale \(O(1+\beta)\) in the upper bound.


## Inferring a vertical transport using only the two ends of a growing slab

**PROVED.** In the dyadic ordinary Wilson tori above, assume \(\beta\le B_0\log N\) and \(1\le k\le\beta^{1/256}\), with \(k\) an integer. The intermediate spatial fields can all be hidden. For two independent draws of the slab conditional on \(X_0,X_k\),
\[
   \inf_{x,y}{\mathbb E}\big[(G_x\cdot G'_x)(G_y\cdot G'_y)\big]
          \ge 1-C_{B_0}\beta^{-1/128}.                                   \tag{27}
\]
This holds without any restriction on the spatial separation. It concerns the actual Wilson marginal of the two endpoint configurations. Here is the scale accounting needed because the free signal between the endpoints decreases with \(k\).

**PROVED.** Put \(u=1+k\). In the projection formula preceding (17), take the positive unperiodized term at time \(k\). Restrict all three spatial frequencies to \([1/u,2/u]\). For large \(\beta\), \(N/u\) grows unboundedly, so at least \(c(N/u)^3\) grid points lie in that cube. The numerator is at least \(c/u^2\), \(\sinh\omega\le C/u\) and \(e^{-k\omega}\ge c\). Consequently \(d_N(k)=P((0,12),(k\hat t,12))\ge c/u^4\). Estimate (17) still holds, since its pairing bound uses only row norms of \(P\). Use (16) between the two indicated slices and let \(R=\operatorname{Ad} G_x\). In the common lower frame use the test \(H_k(M)=\min(1,\|M-d_N(k)I\|_{\rm F}/d_N(k))\). Choose dyadic \(h\asymp\beta^{1/16}\), \(m\asymp h^{2/5}\), \(l=4m\) and \(K^2=A\log\beta\) as before. The crossing fraction is \(O((m+k)/h+h/N)\), and every transport in a noncrossing window has length at most \(3m+k+2\). The Lipschitz bounds for the translated product in (18) grow by at most \(C u^4\). More explicitly its Wilson expectation obeys
\[
 \begin{split}
 {\mathbb E}H_k(M_{x,k}R^{\mathsf T})
 \le C\big[ &(m+k)/h+h/N+e^{-c\beta/h^8}\\
       &+u^4\{m^{-3/2}+e^{-cK^2}
             + K(\sqrt{\Delta_h}+h^{-1}+(m+k+2)h^{-7/2})\}\big].
 \end{split}
\]
The first line counts a bounded loss once per bad or crossing window. For the second line average the transported vector errors, apply the open-box entropy comparison to the linear arrays, and use the free mean and pairing bound, exactly with the displayed new Lipschitz constant. Since \(u^4\sqrt{\Delta_h}K=O(\beta^{-1/64}\log\beta)\) and \(u^4m^{-3/2}=O(\beta^{1/64-3/80})\), the whole bound is \(O(\beta^{-1/128})\). Project \(M_{x,k}/d_N(k)\) to the Frobenius ball as in (15). This proves that an estimator using only the endpoint slices has mean-square error \(O(\beta^{-1/128})\) for \(\operatorname{Ad}G_x\). Thus \({\mathbb E}(1-s_x^2)\le C\beta^{-1/128}\).

**PROVED.** For the multiple-root event tile by spatial sizes \(l,l,l\) and time size \(T\), the smallest dyadic integer at least \(4u\). The two times and the straight vertical segment are inside the tile. Declare the event at threshold \(\epsilon d_N(k)\). There are \(J=V/(T l^3)\) tiles and \(Jm^3\asymp V/u\). On the bounded-total-action event of (20), the bad boxes and crossing windows occupy a fraction \(o(1)\), with boundary loss \(O((l+T)/h)\). For the other windows the bound for changing the average \(H_k\) to its linear-array value is
\[
   C K u^{9/2}(h^{-1}+(l+k+2)h^{-7/2})\sqrt{S_W/V}=o(1).
\]
The factor \(u^4\) is the inverse signal bound and \(\sqrt u\) is Cauchy–Schwarz on \(Jm^3\) readings. The same counting bounds the mean open-Gaussian projection error by \(CKu^{9/2}/\sqrt h=o(1)\), and bounds the Lipschitz constant of the linear tile average on independent standard normals by \(CKu^{9/2}/\sqrt V\). Reflected tile shapes have the same covariance \(d_N(k)\) by the projection symbol. The reflected paths and face origins obey the same length bounds. If every tile is inaccurate, the linear average exceeds a fixed positive constant, whatever entries are supplied in the discarded boxes. As \(u^9 K^2\Delta_h=o(1)\), the Gaussian exponential moment and the pointwise density comparison in (20) give probability at most \(\exp[-cV/(u^9\log\beta)]\). Apply the chessboard inequality. The joint probability for any prescribed set \(S\) of inaccurate roots on the spatial grid is at most
\[
                 \exp[-c\,m^3 |S|/(u^8\log\beta)].                       \tag{28}
\]
In particular the small time-volume fraction sampled by the windows has been charged in the exponent.

**PROVED.** Use a strip of size \(k\times l\) for each spatial grid edge. Its boundary error is exactly \(|G_z-O_eG_{z'}|\), with \(O_e\) computed from the two end slices. Its square is at most \(2kl\sum_{p\ {\rm in\ strip}}(1-w_p)\), by shelling the strip and Cauchy–Schwarz. For distinct prescribed edges \(E\), at each time their \(l|E|\) faces are disjoint. The half-tilt estimate in (21) at one time and Hölder with exponent \(k\) over the times give \({\mathbb E}\exp[(\beta/(2k))\sum_{p\ {\rm in\ strips}}(1-w_p)]\le C^{l|E|}\). Thus the probability all their chords exceed a fixed \(\epsilon_1>0\) is at most \(\exp[-c\beta |E|/(k^2 l)+C l|E|]\). Now both copies have the ordinary one-slab Wilson marginal, irrespective of how the hidden intermediate fields in the two copies differ. Apply the defective-edge assignment and planar contour count of (22)–(23), using (28) and this strip bound. Both \(m^3/(u^8\log\beta)\) and \(\beta/(k^2 l)\) grow as positive powers of \(\beta\) up to a logarithm. Across a good grid edge the sign rule applies because *the same observed* two-sided \(O_e\) transports each copy. To pass to an off-grid point, the corresponding strip of spatial length at most \(l\) has mean squared chord \(O(k^2l^2/\beta)\) by the elementary plaquette mean bound and the shelling estimate. At most three such segments are needed. The one-root loss above bounds the probability that the replica dot product is small at either end. These errors total \(O(\beta^{-1/128})\), proving (27).

**ARGUED.** Equations (26) and (27) put a spatially uniform constraint on extrapolating recovery of a time holonomy from its endpoint fields. The same two-slice experiment has nearly perfect global sign agreement out to a growing power of the bare coupling, and vanishing mean squared global overlap when \(k/(1+\beta)\to\infty\). This leaves an interval of time scales between the two estimates. For the physical vacuum gap the remaining question concerns the distribution of the two observed fields.


## Testing the distribution of the observed gauge-invariant fields

**GUIDE.** The conditional layers divide by the unknown scalar \(Z(X,Y)\) in (11). For singlet insertions \(f,h\) on spatial slices, the actual quantity is \(\int f(X)h(Y)\,P_k(dX\,dY)\), where \(P_k\) is the endpoint law on the ordinary torus. I next bound the information in \(P_k\) itself. Write \(Q_k\) for the product of its two marginals. These definitions also apply after passing each slice to its orbit under local gauge transformations and the three spatial flat centre flips. Row 839 gives the thermal chi-square identity for the stationary vacuum chain, and row 1155 treats square-root affinities at half the time period. I use the smeared gauge-invariant curvature observable of row 1231. [Vacuum-chain information](gap-compress-opus.md) · [Antipodal affinities](gap-solve7-astra62.md) · [Smeared curvature, (7)–(11)](gap-solve26-astra62.md)

**PROVED.** Fix \(0<\delta<1/48\), \(k\to\infty\) with \(k\le\beta^\delta\), and dyadic spatial and time periods \(N\) as in (23). Set \(r\) to the largest power of two at most \(k\). There is an event \(A=A(X_0,X_k)\), measurable from separately centre-neutral and gauge-invariant observations on the two spatial slices, such that
\[
         P_k(A^c)+Q_k(A)\ \le\ C\exp[-c(N/k)^3].                         \tag{29}
\]
In particular an extensive amount of information about the *second spatial configuration* survives a growing number of time steps. Its carriers in this estimate are explicit contractible Wilson readings of radius \(O(k)\). The proof must pay for correlations among all the sampled patches to obtain the exponential probability in (29).

**PROVED.** Use a nonzero real smooth \(\phi\) supported in \((-1,1)^3\), separately even, with positive integral. At a site \(x\) use the vector \(A_r=r^{-1}\sum_z\phi(z/r)\operatorname{Ad}U_{\gamma_{x,z}}\sqrt\beta\,\operatorname{Im}U_{12}(x+z)\) from (7) of row 1231, with coordinate-order paths, and record \(O_r=\exp(-|A_r|^2)\). Each \(O_r\in[0,1]\) is a singlet and is invariant under the flat centre. The test at a spatial point is the product of these readings on the two slices. In the periodic Gaussian array \(PZ\) the two endpoint products have different expectations in the joint and independent experiments. When \(k/r\to s\in[1,2]\) the difference tends to
\[
       [(1+2v)^2-4D(s)^2]^{-3/2}-(1+2v)^{-3}>0 ,
 \qquad D(s)=\int e^{-s|p|}|\widehat\phi(p)|^2
       {p_1^2+p_2^2\over 2|p|}\,{d^3p\over(2\pi)^3},\quad v=D(0).
\]
The formula follows from the Gaussian determinant in (11) of row 1231. Its Fourier Riemann-sum proof there also controls the finite time torus used here. The positive image terms at nonzero spatial frequency \(\xi\) have sum at distance \(k\le N/2\) bounded by \(C|\widehat\xi|e^{-c N|\widehat\xi|}/(1-e^{-cN|\widehat\xi|})\), with \(|\widehat\xi|^2=\sum_i4\sin^2(\xi_i/2)\). The square of the weight transform is at most \(C r^4\) and the zero spatial mode contributes zero. Shell counting on the frequency grid bounds the image error by \(C(r/N)^4\). Compactness of \([1,2]\), \(D(2)>0\) and the same bound for the finitely many reflected shapes give a fixed positive separation of means. A spatial reflection changes the sign convention for \(F_{12}\) or its base by a bounded shift. The modulus and its limiting covariance have the invariance used in row 1231. Both ends in a reflected pair use the same shape. Fix a threshold strictly between the independent limiting mean \((1+2v)^{-3}\) and the least joint limiting mean.

**PROVED.** The following deterministic estimate improves concentration of an array of these tests. For a lattice *linear* curl \(F=dB\), put \(a_j=\sum_z f(z)F_{12}(t+j,z)\) with \(f(z)=r^{-1}\phi((z-x)/r)\). The closedness relation \(dF=0\) and summation by parts express \(a_{j+1}-a_j\) as the sum of electric-face readings with weights \(\pm\nabla_1^* f,\pm\nabla_2^* f\), with the shifts dictated by the oriented square convention. In the identity
\[
      a_0=r^{-1}\sum_{j=0}^{r-1}a_j
              -\sum_{j=0}^{r-2}(1-(j+1)/r)(a_{j+1}-a_j)
\]
the total squared weight is bounded by
\[
         C\big(r^{-1}\|f\|_2^2+
                    r\|\nabla_{\rm spatial} f\|_2^2\big)\le C_\phi .      \tag{30}
\]
Indeed \(|f|\le C/r,\ |\nabla_i f|\le C/r^2\) on \(O(r^3)\) sites. This expresses a thin spatial reading as a bounded linear functional of the four-dimensional curls in one prism. The prism has spatial radius \(r+2\) and time length \(r\) and can also extend backwards in time. For a family of prisms of bounded overlap the map from the whole exact curl array to the vector of readings has bounded \(\ell^2\) norm, by Cauchy–Schwarz and (30). The same identity holds in any open box containing the prism, without a boundary condition on \(B\).

**PROVED.** Choose \(4\delta<\gamma<1/12\) and dyadic \(h\asymp\beta^\gamma\). Tile space by cubes of side \(S=8L_0 r\) and time by intervals of length \(T=8r\), where \(L_0\) is a large fixed dyadic integer to be chosen. In each spatial tile use the \(L_0^3\) centres of the subcubes of side \(8r\) and choose the two time positions \(2r,2r+k\) relative to the lower face. Both sets of reading prisms fit inside. Define the tile reading to be the average of the \(L_0^3\) paired products. For the actual Wilson law a deficient tile is one below the threshold. For the product law use two independent entire Wilson tori, one providing each observed slice, and call a tile excessive when it reaches or exceeds the threshold. The two laws have the endpoint marginals stated above. Each full four-dimensional reflection pattern for either law has \(J=V/(S^3T)\) tiles and \(J L_0^3\asymp V/r^4\) pairs of probes. For a product of two independent tori site reflection positivity follows by conditioning both halves on the two sets of boundary links. The gauge frames in the two copies are independent, which is allowed since each individual reading is invariant at its root.

**PROVED.** For a pattern in which every tile is deficient under the joint law, or every tile excessive under the product law, the global average must deviate from its Gaussian expectation by a fixed positive constant. Here are the costs of the Wilson comparison for that statement. Apply the action cutoff \(S_W\le C V\log\beta\) of (20) in each copy. Discard prisms meeting a bad tree box or an open-box boundary. Their fraction is \(O(h^{12}\log\beta/\beta+(S+T)/h)=o(1)\), by the volume counting in (20), which permits discarding whole coarse tiles there. On retained prisms the full-to-linear comparison for a vector costs at most \(\|f\|_2\le C\sqrt r\) times the local Euclidean norm of the colour error. The face sets have bounded overlap, and their common count is \(\asymp V/r^4\). Equations (8)–(9) of row 1231 therefore bound the error in the *global mean* of these bounded Lipschitz products by
\[
       C r^{5/2}(h^{-1}+(r+2)h^{-7/2})\sqrt{S_W/V}=o(1).
\]
The Lipschitz constant of \(u\mapsto e^{-|u|^2}\) is absolute. For the ensuing Gaussian test use only prisms geometrically interior to an open box, setting other readings to zero. This removes \(O((S+T)/h)\) of the tests in each reflected pattern. Forcing the indicated deviation persists for every Gaussian replacement on the bad boxes, since their contribution to the bounded average is \(o(1)\). In particular this selection for the Gaussian test is deterministic and does not require exposing which boxes are bad.

**PROVED.** In the coupling of the product open Gaussian and the periodic Gaussian, the mean total squared curl difference is at most \(CV/h\) by (1) of row 1231. Inside each retained prism their difference is a closed linear curl, so (30) applies also to this difference. The mean error per reading in the global average is at most \(Cr^2/\sqrt h=o(1)\). Under independent copies the calculation uses one such coupling for each copy. For the open-box Gaussians the curl map on standard normals has bounded norm. By (30) the full average of \(J L_0^3\) products has Lipschitz constant \(C/\sqrt{J L_0^3}\) on those normals. Gaussian concentration bounds the probability of the forced fixed-size deviation by \(\exp(-cV/r^4)\). Multiplication by the Wilson density cost \(\exp(CV\Delta_h)\), including two independent factors in the product case, preserves this exponent because \(r^4\Delta_h=o(1)\). The total-action exceptional probability is smaller. The constants in this exponent can be taken independent of fixed \(L_0\) because for sufficiently large \(\beta\) the discarded fraction is arbitrarily small, the overlap bound for the subprisms is absolute, and \(J L_0^3=V/(8^4r^4)\).

**PROVED.** Taking the chessboard root for the \(J\) four-dimensional tiles gives \(\exp(-c L_0^3)\) per prescribed deficient or excessive tile at the original time. Orientations and reflection origins within the slab can vary as in (20). There are \(G=(N/S)^3\) spatial tiles. Let \(A\) be the event that strictly more than half attain or exceed the threshold in the observed pair. Under \(P_k\), \(A^c\) forces at least \(G/2\) deficient tiles. Under \(Q_k\), \(A\) forces at least \(G/2\) excessive tiles. Summing over their choices costs at most \(2^G\). Choose \(L_0\) so large that \(c L_0^3/2>2\log 2\). Then each error is at most \(\exp(-c' L_0^3 G)\), which proves (29). The tile dimensions divide \(N\) for large \(\beta\) on the dyadic sequence.


**PROVED.** Write \(\mathcal A(P,Q)=\int\sqrt{dP\,dQ}\) and \(I_k=D(P_k\|Q_k)\), the Shannon mutual information of the two observations. Splitting the affinity integral on \(A\) and its complement, Cauchy–Schwarz gives \(\mathcal A\le \sqrt{Q_k(A)}+\sqrt{P_k(A^c)}\). Jensen applied under \(P_k\) gives \(D(P_k\|Q_k)\ge -2\log\mathcal A\). Thus (29) implies a lower bound \(c(N/k)^3\) both on the mutual information and on the negative log affinity of the centre-neutral endpoint fields.

**PROVED.** There is a matching order upper bound. Write \(U\) for the full gauge-projected Wilson transfer divided by its Perron eigenvalue, \(K_j\) for its integral kernel to power \(j\) against product probability Haar on spatial links and \(g_j=\log\operatorname{Tr}U^j\). On the ordinary periodic torus, the unquotiented pair density is \(e^{-g_N}K_k(x,y)K_{N-k}(y,x)\). Positive semidefiniteness gives \(K_j(x,y)\le\sqrt{K_j(x,x)K_j(y,y)}\), by taking an inner product of half-kernel rows, or two-point positivity of the continuous positive kernel. These are also nonnegative kernels by their Wilson integral. Let \(\nu\) be the probability with density proportional to \(\sqrt{K_k(x,x)K_{N-k}(x,x)}\). Its normalizer is at most \(\exp[(g_k+g_{N-k})/2]\). Consequently \(P_k\le \exp(g_k+g_{N-k}-g_N)\nu^{\otimes2}\) on the full fields. Subtract the relative entropies of the two marginals to \(\nu\) from \(D(P_k\|\nu^{\otimes2})\) to obtain
\[
   I_k\ \le\ g_k+g_{N-k}-g_N
       \ \le\ \left(1+\frac{k}{N-2k}\right)g_k,\qquad k<N/2.             \tag{31}
\]
The second inequality follows by convexity and monotone decrease of \(g_s=\log\sum_i e^{-sE_i}\), using the adjacent intervals \([k,N-k]\) and \([N-k,N]\), and \(g_{N-k}\ge0\). Passing to the neutral orbit is a measurable map at each endpoint, which decreases relative entropy. By (5) of row 1153, \(g_k=(\pi^2/15+o(1))(N/k)^3\) on the growing weak-coupling cubes here. Its hypothesis \(k^4\beta^{-1/4}[\log(2+\beta)]^{3/2}\to0\) holds throughout the range of (29). Its \(N\) in the volume factor counts spatial sites. It follows that, for the actual pair of *neutral* spatial configurations,
\[
 c\,(N/k)^3\ \le\ -2\log\mathcal A(P_k,Q_k)
       \ \le\ I_k\ \le\ (\pi^2/15+o(1))(N/k)^3 .                       \tag{32}
\]
The two-sided order concerns the ordinary long-period Wilson law at a time \(k\) of vanishing physical duration. Row 1153 supplied the upper thermal input, and row 1231 supplied the individual singlet observable and its limiting two-point function. The extensive lower information estimate here uses the closed-curl prism identity (30) and large-deviation estimates for the observed fields in the joint and independent experiments. [Short-period trace, (3) and (5)](gap-solve6-astra62.md)


## Detecting temporal centre twists from sparse observations of neutral spatial slices

**GUIDE.** A flat spatial centre flip multiplies spatial links by a flat \(\{\pm1\}\) cochain of prescribed holonomy. The eight classes form \(G=H^1(\mathbb T^3;\mathbb Z_2)\). The earlier collar analysis reconstructs a spatial field modulo these flips from four-dimensional adjoint data. The vacuum-chain overlap of two fields related by an independent flip is also known to bound a twisted trace. Here the observations are separately neutral *spatial slices*. The probability estimate below concerns their joint temporal history in the positive sum of the eight temporally twisted Wilson ensembles. [Adjoining collars, row 1155](gap-solve7-astra62.md) · [Shifted pair overlap, row 1161](gap-solve9-astra62.md)

**PROVED.** Take the dyadic \(N\) and \(k\le\beta^{1/256}\) of (27), and the grid of side \(n=N/l\). For a pair of raw spatial slices \(X,Y\) there is a gauge-invariant set of candidate classes \(\mathcal D(X,Y)\subset G\), always nonempty, such that for independent flat flips \(a,b\)
\[
 \begin{split}
   \mathcal D(aX,bY)&=ab\,\mathcal D(X,Y),\\
   P_k\{\mathcal D(X,Y)\ne\{1\}\}
    &\le \epsilon_{N,\beta,k}:=
            C n^3\exp[-c n^2 L_{\beta,k}],\\
   L_{\beta,k}&=\min\{m^3/((1+k)^8\log\beta),\,\beta/(k^2l)\}.
 \end{split}                                                            \tag{33}
\]
Here \(P_k\) is the unshifted two-slice law on the ordinary \(N^4\) torus before quotienting by the separate flat flips. In particular the two laws obtained by flipping only the upper slice by distinct classes admit tests with exponentially small error even though the reference Wilson measure is invariant under a simultaneous flip.

**PROVED.** At each grid vertex compute \(M_{z,k}/d_N(k)\) of (27). Retain a vertex if this matrix is within a fixed small Frobenius distance \(2\epsilon\) of \(SO(3)\). On retained vertices use its polar rotation. It is unique there because all singular values are close to one and the determinant is positive. This map respects independent left and right rotations, and if the input is within \(\epsilon\) of a true rotation its polar factor is within \(2\epsilon\) of that rotation, by nearest-point optimality. At each retained site choose either quaternion lift \(v_z\) of the factor. On a grid edge record the sign of
\[
                v_z\cdot\big(X_{zz'}\,v_{z'}\,Y_{zz'}^{-1}\big)
\]
using the two straight spatial paths. Erase the sign if one endpoint is unretained or the dot product is zero. Define \(\mathcal D\) to be the set of holonomies of *all* flat grid sign cochains minimizing the number of disagreements with the recorded signs on unerased edges. This is a finite definition, without any numerical minimization in the proof. A change of lifts multiplies the edge array by a vertex-sign coboundary on the observed graph, which extends using arbitrary signs at erased vertices. Independent spatial gauge changes have the same effect on the signs after the root rotations cancel. Both leave the minimizing holonomies fixed. Independent spatial flat flips preserve \(M_{z,k}\), since its transports are adjoint and its plaquettes contractible. On straight paths the product of the two flip cochains restricts to a flat grid cochain of holonomy \(ab\). It multiplies all recorded signs by that cochain, establishing the exact covariance in (33).

**PROVED.** In an ordinary Wilson draw put \(t_z\) equal to the lift sign bringing \(v_z\) closer to the true \(G_z\), using arbitrary signs at erased sites. If both endpoint rotations are accurately estimated in the sense of (28), and if the strip chord is small, the recorded bond equals \(t_z t_{z'}\). Indeed the two signed lifts and their true transports differ in quaternion norm by \(O(\epsilon)\), and the transported true quaternions have chord at most \(\epsilon_1\). Taking \(\epsilon,\epsilon_1\) sufficiently small makes the resulting dot product strictly positive. Thus on an unerased, nondefective bond the signs agree with the *single* gradient \(dt\). For every prescribed set of \(j\) defective grid bonds the joint probability is at most \(\exp(-c L_{\beta,k} j)\). Use the union over their two endpoint-root causes and their strip cause as in (22), now for one sample and with (28) and the \(k\)-strip bound. This can be read as an estimate for the event that a given set is contained in the defect set.

**PROVED.** If a cost minimizer has nontrivial holonomy, multiply it by \(dt\). The support of the resulting edge-sign cocycle gives dual plaquettes, closed modulo two. Each edge-connected component \(C\) of the dual plaquettes is itself closed, since all present plaquettes at any dual edge are adjacent there. At least one component has nontrivial cohomology. For that component there is an axial direction whose every one of \(n^2\) disjoint parallel primal periods pairs oddly with it, since the periods are homologous and the component is a cocycle. Hence \(|C|\ge n^2\). Flipping the minimizer on \(C\) is another flat cochain. On every nondefective bond in \(C\) it strictly improves the fit by one, and on any defective bond it can worsen the fit by at most one, including erasures with zero cost. By minimality at least half the bonds of \(C\) must be defective. Rooted connected sets of \(j\) dual plaquettes have at most \(C_0^j\) shapes by traversal of a spanning tree on their bounded-degree adjacency graph. There are at most \(3n^3\) roots and \(2^j\) choices of the defective subset. Summing over \(j\ge n^2\) proves (33), since \(L_{\beta,k}\) grows as a positive power of \(\beta\) up to a logarithm. The argument controls ties involving an incorrect class.

**PROVED.** The same test has a consequence on a full time period of physical length. Take \(k\) dyadic dividing \(N\) in this range, allowing \(k\) to tend to infinity. Write \(Z_c=\operatorname{Tr}(c U^N)>0\) for a temporal twist by a spatial flat class \(c\in G\), \(Z_1=\operatorname{Tr}U^N\), and \(\mathbb M\) for the positive joint law choosing \(c\) with probabilities \(Z_c/\sum_d Z_d\), then a Wilson history with that twist. Positivity here follows from the pointwise positive transfer kernel with the final slice identified with \(cX_0\). Observe only the spatial slices every \(k\) steps, *each modulo local vertex gauges and its own flat flips*. There is a function \(\widehat c\) of these observations with
\[
           \mathbb M\{\widehat c\ne c\}\le 8(N/k)\sqrt{\epsilon_{N,\beta,k}}.
                                                                         \tag{34}
\]
For each observed orbit choose a representative. Use the same representative at the beginning and when closing the time circle. Multiply the unique decoded classes for adjacent representatives, returning a failure symbol if any class is ambiguous. Product and failure are independent of the choices by (33), since every change at a representative acts on two neighbouring factors and \(a^2=1\). Equivalently this defines a measurable function by descent of an invariant finite-valued function of representatives. If all underlying pairs along the actual path, with last endpoint \(cX_0\), decode uniquely to \(1\), the product along the closed representatives is \(c\).

**PROVED.** To bound failure under the twisted mixture, let \(B(x,y)=K_k(x,y){\bf1}_{\{\mathcal D(x,y)\ne\{1\}\}}\), regarded as an integral operator. The following comparison uses the pointwise inequalities \(0\le B(x,y)\le K_k(x,y)\). At a specified block the unnormalized bad weight at twist \(c\) is \(\operatorname{Tr}(c B U^{N-k})\). Cauchy–Schwarz for Hilbert–Schmidt kernels bounds its absolute value by
\[
       \|B U^{(N-2k)/2}\|_{\rm HS}\,\|U^{N/2}c\|_{\rm HS}
                  \le Z_1\sqrt{\epsilon_{N,\beta,k}} .
\]
Indeed the second squared norm is \(Z_1\). In the first squared norm \(\operatorname{Tr}(B^* B U^{N-2k})\), bound the kernel of the second \(B\) by \(K_k\) inside the nonnegative integral. This gives \(\operatorname{Tr}(B^*U^{N-k})=Z_1P_k\{\mathcal D\ne\{1\}\}\). Commutation of \(c\) with \(U\) permits any location of the marked block, including the final identification. Divide by \(\sum_d Z_d\ge Z_1\), sum the eight bounds and then the \(N/k\) time blocks. This proves (34) directly on the ordinary-plus-twisted ensembles, without a lower bound on any individual twisted partition function.

**PROVED.** In particular, for each character \(\chi\) of \(G\), with \(P_\chi=8^{-1}\sum_c\chi(c)c\), the sector-weight ratio at this full period satisfies
\[
 \left|
 { \operatorname{Tr}(P_\chi U^N)\over\operatorname{Tr}(P_{\rm triv}U^N)}
             -{\mathbb E}_{\mathbb M}\chi(\widehat c)
 \right|\le16(N/k)\sqrt{\epsilon_{N,\beta,k}},                           \tag{35}
\]
where one may give the failure symbol value zero. The identity with the true \(c\) is Fourier inversion of the eight positive twist weights. If \(aN\) tends to a fixed length and \(\beta\le B_0\log N\), the error vanishes. Thus (35) represents a finite-physical-time electric-flux observable using only a sequence of neutral spatial configurations with all intermediate temporal links, all intermediate spatial slices between observations and all separate flat-class labels integrated out. The separate probabilities of the decoded winding classes under this neutral path law are still to be evaluated. The neutral thermal count, the denominator in (35), also requires an absolute estimate.


## A bound on singlet correlations at fixed physical times

**PROVED.** Keep \(r\to\infty\) dyadic with \(r\le\beta^\delta\), \(0<\delta<1/48\). On the grid of \(M=(N/(8r))^3\) spatial probe sites from (29), set \(F_z(X)=O_r(z;X)-m_*\), where \(m_*=(1+2v)^{-3/2}\) is the limiting mean of the bounded singlet reading. Write \(F(X)\in\mathbb R^M\) for the vector of readings. For every fixed \(w>0\) there are \(B_w,c_w>0\) such that for sufficiently large \(\beta\), all deterministic real matrices \(D\) with \(\|D\|_{\rm op}\le1\), and *all* integer separations \(B_w r\le t\le N-B_w r\),
\[
  P_t\!\left\{\left|\langle F(X_0),D F(X_t)\rangle\right|>w M\right\}
                  \le 4\,e^{-c_w M}.                                    \tag{36}
\]
Thus even a predetermined linear transformation mixing every sampled spatial site is covered. A union bound includes any family of \(\exp(o(M))\) such transformations at once. The cutoff time in (36) depends on the prescribed signal size \(w\).

**PROVED.** The assertion is immediate for \(w\ge1\). Fix \(0<w<1\). Choose an integer \(B\) so large that the limiting Gaussian mean of the centred product at separation \(Br\) is below \(w/16\). This is possible from \(D(B)\to0\) in the displayed integral before (30), by dominated convergence. Use the bounded tile product \(F_z(X_0)F_z(X_{Br})\) in the proof of (29), now with time tile a dyadic multiple of \(r\) of size at least \(4(B+1)r\). The two reading prisms still fit inside. The mean of the linear Gaussian comparison is eventually below \(w/12\), and a tile is declared excessive if its average exceeds \(w/4\). The closed-curl norm bound (30), the replacement error and the density comparison hold with constants depending on \(B\), and the number of subprisms in the full dissemination is \(\asymp_B V/r^4\). Thus any specified \(j\) excessive tiles have probability at most \(\exp(-c_{w,B} L_0^3j)\). If the spatial mean exceeds \(w/2\), at least a fraction \(w/4\) of the tiles must be excessive, since their averages have magnitude at most one. Increase the fixed dyadic \(L_0\) so the subset count \(2^{(N/(8L_0r))^3}\) is absorbed. The original set of subcube centres can be kept fixed under this grouping. It follows for \(G=\langle F(X_0),F(X_{Br})\rangle\) that \(P_{Br}(G>w M/2)\le e^{-b_w M}\) for some \(b_w>0\). Consequently for \(0<\sigma<b_w/2\),
\[
        {\mathbb E}_{Br}\exp(\sigma G)
                    \le e^{\sigma w M/2}+e^{(\sigma-b_w)M}.
\]

**PROVED.** To propagate this estimate, define the positive semidefinite bilinear form of real slice functions
\[
     [f,h]_t={\operatorname{Tr}(U^{N-t}M_f U^t M_h)\over\operatorname{Tr}U^N}.
\]
Here \(M_f\) denotes multiplication. Positivity follows by taking the Hilbert–Schmidt squared norm of \(U^{(N-t)/2}M_fU^{t/2}\). Symmetry follows from the real symmetric kernel \(K_t(x,y)K_{N-t}(y,x)\). For each \(j\ge1\) the coordinates \(F_I=\prod_{b=1}^j F_{i_b}\) of \(F^{\otimes j}\), with ordered indices \(I\), have a positive semidefinite Gram matrix \(H_j(t)=([F_I,F_J]_t)\). Hence
\[
 \left|{\mathbb E}_t\langle F(X_0),D F(X_t)\rangle^j\right|
       \le\operatorname{tr} H_j(t)
       ={\mathbb E}_t\langle F(X_0),F(X_t)\rangle^j .
\]
Contract the Gram matrix with \(D^{\otimes j}\), of operator norm at most one, to obtain the inequality. Each diagonal form \([F_I,F_I]_t\) is a nonnegative sum of terms \(u_p^{N-t}u_q^t|\langle p,M_{F_I}q\rangle|^2/\operatorname{Tr}U^N\) in a transfer eigenbasis, with \(u_p\ge0\). The sum is symmetric under \(t\leftrightarrow N-t\) and convex on the open interval, as seen termwise on the positive eigenvalues. It decreases up to \(N/2\). Therefore \(\operatorname{tr}H_j(t)\le\operatorname{tr}H_j(Br)\) for \(Br\le t\le N-Br\). The exponential series for both signs of \(\sigma\) converges absolutely since \(|\langle F,D F'\rangle|\le M\). Each moment generating function is bounded by the preceding positive one at \(Br\). Exponential Markov at \(wM\) gives (36), including spatially nonlocal \(D\). This argument propagates a bound on the actual neutral observations without following the charged transports.

**PROVED.** For a fixed physical cube \(aN\to L\in(0,\infty)\), (36) controls matrix elements of the *actual transfer* on every fixed physical-energy band, including all its multiplicities. For \(Br\le t\le N/2\), let \(B_t\) be the kernel \(K_t\) restricted to the event in (36), or to a union over a family of \(\exp(o(M))\) matrices. For any fixed \(E<\infty\),
\[
 \left\|B_t{\bf1}_{[0,aE]}(-\log U)\right\|_{\rm HS}^2
     \le e^{aNE}\exp(g_N)\,P_t\{\text{selected event}\}
     \le \exp[-c'_w M].                                                  \tag{37}
\]
Indeed the spectral projector is bounded above by \(e^{aNE} U^{N-2t}\). As in (34), use \(0\le B_t(x,y)\le K_t(x,y)\) inside the trace of \(B_t^*B_t U^{N-2t}\). At \(2t=N\) this is the direct squared-kernel integral. To absorb \(g_N\), choose \(\delta<\delta'<1/16\) and \(h_0=\lfloor\beta^{\delta'}\rfloor\). Monotonicity and the short-period trace (5) of row 1153 give \(g_N\le g_{h_0}=O((N/h_0)^3)=o(M)\), since \(h_0^4\beta^{-1/4}[\log(2+\beta)]^{3/2}\to0\). At the antipodal time \(t=N/2\) the same exponentially small Hilbert–Schmidt error bound holds on the full Hilbert space, without the energy projector. For \(a t\to\tau\in(0,L/2]\) the estimated time is a positive physical time. The retained endpoint pairs may carry arbitrary correlations in other singlet functions, including functions of subextensively many collective variables.


## Estimating the scalar transfer kernel left by the colour measurements

**GUIDE.** The long-time upper estimate for vertical colour has a stronger predecessor. Row 1145, (16)–(17), bounds all product representations of all vertical lines together, conditional on the full spatial history, and removes the local gauge projection from the physical thermal trace with a vanishing relative error. Its layer argument also applies to a subinterval. Equations (24) and (26) used two low-dimensional consequences to bound the error in extrapolating the short-time reconstruction in (27). For the scalar transfer I use the orbit distance bound of row 1155 and the spanning-tree integration already used for sheets in row 1262. [All temporal lines](gap-solve2-astra62.md) · [Orbit distance, (20)](gap-solve7-astra62.md) · [Spanning-tree integral for a sheet](gap-solve30-astra62.md)

**PROVED.** Put \(v_3=N^3\), \(D_{XY}(g)=\sum_{e=zz'}(1-g_z\cdot R_e g_{z'})\), \(d_{XY}=\min_g D_{XY}(g)\) and \(\mathcal Z_\beta(X,Y)=\int e^{-\beta D_{XY}(g)}\,dg\), with product probability Haar as reference. This is the scalar electric factor of the transfer in deficit convention, prior to multiplication by the spatial weights and the vacuum normalization. A uniform orbit-volume estimate is
\[
 \begin{split}
 \tfrac32(v_3-1)\log(1+s)-C v_3
 &\le -\log\mathcal Z_\beta(X,Y)-\beta d_{XY}\\
 &\le \tfrac32 v_3\log(1+\beta)+C v_3,\qquad
            s={\beta\over1+\beta d_{XY}/v_3}.                            \tag{38}
 \end{split}
\]
For the lower bound on the negative logarithm, use \(D\ge d_{XY}\) in the factor with parameter \(\beta-s\). In the factor with parameter \(s\) drop all bonds except a spanning tree. Integrate its leaves successively. The integral is \(z_s^{v_3-1}\), where \(z_s=\int_{S^3}e^{-s(1-\operatorname{Re} q)}dq\le C(1+s)^{-3/2}\). Also \(s d_{XY}\le v_3\). For the reverse bound centre a product of chord balls of radius \(c/\sqrt{1+\beta}\) at a minimizing field. Along independent shortest sphere geodesics from that field to any point of the balls, the full first derivative of \(D\) at the minimum is zero. Each bond contributes at most \(C/(1+\beta)\) to the absolute second derivative along these paths by the speeds and the sphere geodesic equation. Taylor's formula gives \(D\le d_{XY}+C v_3/(1+\beta)\) there. The balls have product Haar volume at least \([c'(1+\beta)^{-3/2}]^{v_3}\). This proves both inequalities without a choice of a preferred minimizer.

**PROVED.** For the actual pair of adjacent spatial configurations, \(d_{XY}\) is half the squared minimum chord distance between their vertex-gauge orbits. The lower-tail bound (20) of row 1155 gives \(\beta d_{XY}\ge c v_3\) with probability at least \(1-e^{-c'v_3}\) at large \(\beta\). For the other tail evaluate \(D\) on the actual temporal links, then use (21)'s half-tilt estimate for all \(3v_3\) electric faces. This gives \(\Pr(\beta d_{XY}>H v_3)\le e^{-H v_3/2+C v_3}\). On the complementary typical set, (38) implies
\[
  -\log\mathcal Z_\beta(X,Y)
         =\beta d_{XY}+\tfrac32 v_3\log(1+\beta)
                         +O_H(v_3+\log(1+\beta)).
\]
The same error holds in expectation with an absolute constant because the lower bound in (38) differs from \(\frac32(v_3-1)\log(1+\beta)\) by at most \(C v_3[1+\log(1+\beta d_{XY}/v_3)]\), and the preceding tail controls its mean. The coefficient \(3/2\) counts the three local spin coordinates.

**PROVED.** In the raw link coordinates the whole temporal layer \(g\) has product Haar marginal, since the independent vertex gauges at its two ends include arbitrary left multiplication at each lower vertex. Consequently its Shannon mutual information with the pair of adjacent *raw* spatial configurations is
\[
  I\big(g;(X,Y)\big)
     ={\mathbb E}\big[-\log\mathcal Z_\beta(X,Y)-\beta D_{XY}(g)\big]
     =\tfrac32 v_3\log(1+\beta)+O(v_3+\log(1+\beta)).                    \tag{39}
\]
The equality uses the conditional density in (11), and the actual electric action has mean \(O(v_3)\) by the same half tilt. Equation (39) measures information about gauge frames supplied jointly by the two slices. It is quantitatively distinct from (32), in which the two neutral observations are the variables whose mutual information is measured.

**OPEN.** Formula (38) fixes the leading large term in the one-step scalar kernel. Its remainder can still be of order \(N^3\) per time step. The required physical pressure is a difference of vacuum-normalized traces to absolute order one. Multiplication over \(O(N)\) steps on a fixed physical cube does not control that difference from the error in (38).


## The remaining physical estimate

**PROVED.** At the antipodal time, (37) gives an explicit remaining integral for the one-cube neutral trace. Let \(T=N\) initially, let \(C_N\) be the retained pairs from (37), and set \(K^+_t(x,y)=8^{-1}\sum_{c\in G}K_t(x,cy)\). This is the kernel of \(P_{\rm triv}U^t\). Then
\[
 \left|\sqrt{\operatorname{Tr}(P_{\rm triv}U^T)-1}
       -\inf_{\operatorname{rank} A\le1}
         \|{\bf1}_{C_N}(x,y)K^+_{T/2}(x,y)-A(x,y)\|_{L^2(dx\,dy)}
 \right|\le e^{-c_w M}.                                                  \tag{40}
\]
Here the indicator is multiplication of kernel values and \(M=(N/(8r))^3\). Indeed the excluded set is invariant under separate flat flips. Bound the square of the averaged kernel by the average of the squares and change variables in the Haar integral. Its excluded squared norm is at most \(e^{g_T}P_{T/2}(C_N^c)\) by the ordinary pair density. The argument of (37) makes this exponentially small in \(M\). The unrestricted neutral kernel has largest singular value one, with the centre-neutral vacuum as its eigenvector, and squared Hilbert–Schmidt norm \(\operatorname{Tr}(P_{\rm triv}U^T)\). Its distance to operators of rank at most one is the square root on the left. This follows by keeping the vacuum term in the spectral expansion and from the bound one on every unit-vector matrix coefficient. Distance to this set is 1-Lipschitz in Hilbert–Schmidt norm. These facts prove (40).

**PROVED.** Equation (40) also applies at a fixed positive dyadic aspect ratio \(T/N\), in particular \(T=N/2\), on the same dyadic spatial sequence. For the proof of (36) the total number of fine sites becomes \(N^3T\). Every fixed tile divides the temporal period for large cutoff, the open-box boundary area per unit volume is \(O(1/h)\), and the Gaussian time images in the proof of (29) cost \(O_{T/N}((r/N)^4)\). The temporal reflection argument uses \(t\leftrightarrow T-t\). The short-period trace used to bound \(g_T=o(M)\) is that of the same spatial transfer and \(h_0<T\). All estimates needed for the excluded kernel apply with these changes. This includes a finite physical period on the ordinary cube used for the thermal test.

**OPEN.** I do not have an absolute upper bound on the rank-one approximation error in (40) at any fixed physical side sufficient for the thermal criterion. In particular, the positive character ratio in (35) leaves the absolute neutral trace as its denominator. Equation (32) controls the neutral endpoint law only at vanishing physical time. At fixed physical time, (36) excludes an extensive aligned signal from the tested curvature readings. A matrix acting only on \(o(M)\) coordinate sites automatically contributes \(o(M)\) to that test for every pair of fields, even if the readings on those sites agree exactly. Correlations of normalized collective singlet observables on the retained pairs can still contribute to the right side of (40). No estimate above places their energies above a common positive threshold in physical units.

**OPEN.** For the Jaffe–Witten conclusion one needs a nontrivial continuum Yang–Mills vacuum theory and a \(\Delta>0\) with \(\operatorname{spec}(H|_{\Omega^\perp})\subseteq[\Delta,\infty)\). On the route of row 1272 the missing inputs are its interacting bound (33) and matching of a dense family of continuum gauge-invariant states. On the thermal route the published one-scale propagation also requires a strict initial bound in the interacting theory. Both obstructions remain. The arguments here are hand derivations with the cited finite-cutoff inputs. There has been no independent check of the new arguments. [Previous row, (33)–(34)](gap-solve31-astra62.md) · [Published thermal and relaxation hypotheses](prior/gap-onebound-read-sol.md)

RESULT — OPEN. Row 1283. Equations (29)–(32) bound the information shared by neutral Wilson slices at short times. Equation (35) recovers electric-flux sector ratios from neutral spatial histories at a physical time period. Equations (36)–(40) remove the endpoint pairs with an extensive curvature correlation from the physical neutral thermal test. The remaining singlet trace estimate and the nontrivial continuum construction are open. The four-dimensional SU(2) Jaffe–Witten mass gap is unproved here. This research note grants no status.
