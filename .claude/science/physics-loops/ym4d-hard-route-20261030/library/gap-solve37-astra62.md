## Repo search

**GUIDE.** At the requested pin, `ffbd23e2c`, the row-specific prior is absent. I checked the lead's November 8 hits on main and the four named PRs. On main (`8b11ae2bb9`), Theorem ZD-c, `research/mass-gap/library/gap-phys-seed.md` 311–320, relates the periodic thermal criterion to the energy and free-energy defect of cubes. PR 10114 (`f76f6c649c`), `MASS_GAP_LOCAL_BLOCK_ASTRA.md` 4–10, 106–149, gives a one-time-step plaquette witness and a contraction in a fixed small-coupling interval. Grok's PR 10133 (`89faef229f`), `MASS_GAP_CROSSOVER_REDUCTION.md` 77–86, leaves its crossover and source transport open. PR 10134 (`1e70c7211a`), `mass-gap-interface.md` I1–I5, distinguishes a nonempty excited sector from a positive threshold. PR 10141 (`a2f6a430e2`), `research/ym4d/library/fp1.md` 299–315, bounds a constrained classical field at one scale. PR 10144 (`1f20846b80`) indexes the second snapshot of local notes. [Lead's search](prior/repo-search-2026-11-08.md) · [Paths and source readings](prior/gap-onebound-read-sol.md)

**GUIDE.** The closest result on this branch is row 1317, (7)–(11). It compares the Wilson transfer with one modified by a single-slice weight. Row 1318 is listed as started at the pin and its check file is absent. I searched the registry, earlier gap notes and YM4D paths on the fetched refs for an interaction that couples rapid plaquette readings on consecutive slices. The closest comparisons use a single-slice weight or a separate product system. I found no matching result or owner. [Row 1317](gap-solve36-astra62.md) · [Registry](open-registry.md)

## A proposed way to obtain an infrared estimate

**OPEN.** Construct the required four-dimensional SU(2) Yang–Mills theory and prove that its Hamiltonian has a strictly positive spectral gap above the vacuum.

**GUIDE.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, explicitly distinguish scalar reconstruction and positive spectral exclusion. I used the README, chunks 01 and 29 and the obligations in their outline index to locate the passages, then read the two sources at `31a47c543775`. Their decaying scalar example has spectral weight in every interval above zero. CA-I expressly leaves a physical mass gap open. [Outline 581–599](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L581-L599) · [Outline 31860–31882](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L31860-L31882) · [Complete account I 2704–2712](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2704-L2712)

**GUIDE.** Row 1218 records the one-scale thermal criterion of Deep Bhattacharjee, Ushashi Bhattacharya, James Montgomery Lockwood, Tristan Romanov, Ikailo John Sessford and Sanjeevan Singha Roy. It also records block-dynamics criteria of the first four authors and the separate microscopic hypotheses in Zeng Chunping's tunnelling proposal. I use the repository's reading for those attributions. [Published-work reading](prior/gap-onebound-read-sol.md)

**GUIDE.** Give a rapidly oscillating part of the magnetic action a positive interaction across one time step. Try to control the one-scale thermal defect by choosing that interaction to have a known gap. The test is whether the modification raises the Wilson excitation energies, leaves them in the spectrum, or introduces other low levels. The arguments use Haar integration, transfer operators, conditional probability and Fourier analysis. All estimates below are analytic.

**GUIDE.** Use a periodic spatial torus with all three sides at least four. Write \(w(q)=\tfrac12\operatorname{tr}q\), use probability Haar measure, and give each plaquette weight \(e^{\beta w(U_p)}\), \(\beta\ge0\). Let \(U\) be the Wilson time transfer divided by its vacuum eigenvalue, on the Hilbert space of square-integrable gauge-invariant spatial functions. I use the Osterwalder–Seiler and Lüscher transfer conventions of rows 1215 and 1317. In particular \(U\) is compact, positive as an operator, and has a positive continuous integral kernel with vertex averaging. A two-step bridge at ends \(x,y\) has middle density proportional to \(U(x,z)U(z,y)\). Before averaging the end frames, one middle link has two temporal staples and four spatial staples. All positive normalizations at fixed ends cancel. [Transfer conventions](gap-solve34-astra62.md) · [Two-step bridge](gap-solve36-astra62.md)

## One rapidly oscillating reading of an elementary plaquette

**PROVED.** Select a spatial plaquette and mark one of its links. Conditional on the other links in an ordinary Wilson torus, the marked link is a unit quaternion \(x\) with law \(e^{h\cdot x}dx/Z(h)\), where \(dx\) is probability Haar and \(|h|\le 6\beta\). Its plaquette trace is \(s=v\cdot x\) for a unit four-vector \(v\) fixed by the exterior. These assertions follow by cyclicity of the trace and linearity in a quaternion or its conjugate. They hold in a two-step temporal-gauge bridge as well, with its two end frames fixed. Averaging the frames preserves bounds uniform in those frames.

**PROVED.** At every real frequency \(M\ge1\), the reading \(z=Ms\bmod 1\) has a density \(g\) on the unit circle with
\[
                  |g(z)-1|\le \epsilon,\qquad
                  \epsilon=C(1+\beta)^{3/2}/M .                         \tag{1}
\]
Indeed put \(\alpha=h\cdot v\), \(b=|h-\alpha v|\), \(r(s)=\sqrt{1-s^2}\). In \(x=sv+r(s)\omega\), the transverse unit vector \(\omega\) has reference law uniform on \(S^2\), and the reference density of \(s\in[-1,1]\) is \(2r(s)/\pi\). A Cartesian coordinate on \(S^2\) is uniform on \([-1,1]\) by the spherical area element. The density of \(s\) is therefore
\[
   f(s)=\frac{2 e^{\alpha s}}{\pi Z(h)}
         \begin{cases}\sinh(b r(s))/b,&b>0,\\ r(s),&b=0.\end{cases}
\]
It vanishes at the endpoints and is log-concave in the interior because \(r\) is concave and both \(\log\sinh u\) and \(\log u\) are increasing and concave for \(u>0\). Thus its total variation after extension by zero is \(2\max f\). The cap of angular radius \((1+|h|)^{-1/2}\) about a maximizer of \(h\cdot x\) gives \(Z(h)\ge c e^{|h|}(1+|h|)^{-3/2}\). This follows by integrating \(\sin^2\theta\) radially and using \(1-\cos\theta\le\theta^2/2\). The integrand in the reference angular average for \(f\) is at most \(e^{|h|}\). Finally \(g(z)=M^{-1}\sum_{j\in\mathbb Z}f((j+z)/M)\). On each interval \([j/M,(j+1)/M]\) the error between this sample and the integral is at most \(1/M\) times the variation there. Summation proves (1).

**PROVED.** For \(B\) readings in a slice, choose their marked links so that each belongs only to its own selected plaquette and no Wilson plaquette contains two marked links. Conditional on the other links and the end frames, their densities multiply. One obtains a positive density on an even cube by selecting direction-one links at sites with all coordinates even and using the \(12\)-plaquette based at each such site. For a single reading no spacing choice is needed. Partition the circle or the product circle into finitely many measurable sets of positive uniform probabilities \(p_i\). Write \(M_i\) for multiplication by the indicator of label \(i\). Integration of (1) gives the pointwise bound on the physical space
\[
 |U M_i U-p_i U^2|(x,y)\le \delta p_i U^2(x,y),\qquad
           \delta=(1+\epsilon)^B-1,\quad \epsilon<1.                    \tag{2}
\]
The lower density bound \((1-\epsilon)^B\) is at least \(1-\delta\), by the binomial theorem. This version can use just one elementary plaquette per circle coordinate. Row 1317, (7), supplies an alternative to (1) for a sum of ordinary action variables over many plaquettes at a lower frequency. Neither choice changes the Wilson time transfer in (2).

## Spectrum when successive readings interact

**PROVED.** Suppose (2) holds with \(\delta<1\). Choose a real symmetric matrix \(A\) with nonnegative entries, positive semidefinite as a quadratic form, and \(\|A\|=1\) on ordinary Euclidean label space. Write \(i(x)\) for the label of a slice. On the same gauge-invariant Hilbert space form the transfer with kernel
\[
       V(x,y)=U(x,y)\frac{A_{i(x)i(y)}}{\sqrt{p_{i(x)}p_{i(y)}}}.
                                                                        \tag{3}
\]
Then \(V\) is compact and positive. Let \(d_j\) list the products of the eigenvalues of \(A\) and \(U\), in decreasing order with multiplicity, with \(d_0=1\). Write \(v_j\) for the ordered eigenvalues of \(V/\|V\|\). For \(\delta\) small enough that \((2+\delta)\delta<1\),
\[
             |v_j^2-d_j^2|\le 2(2+\delta)\delta\quad\hbox{for all }j.
                                                                        \tag{4}
\]
In particular the estimate has no factor equal to the inverse probability of a label, the number of labels, or the inverse gap of \(A\).

**PROVED.** Put \(\mathcal H=L^2_{\rm inv}\), \(D=A\otimes U\) and define \(J:\mathcal H\to\bigoplus_i\mathcal H\) by \((Jf)_i=p_i^{-1/2}M_i f\). Then \(V=J^*DJ\) and \(JJ^*=\operatorname{diag}(M_i/p_i)\). The \(ij\) kernel of \(C_1=D JJ^*D\) is
\[
                \sum_l A_{il}A_{lj} U M_l U/p_l.
\]
Since all coefficients are nonnegative, (2) bounds its pointwise difference from \((D^2)_{ij}\) in absolute value by \(\delta(D^2)_{ij}\). Testing on componentwise absolute values gives \(\|C_1-D^2\|\le\delta\). The nonzero spectra with multiplicity of \(C_1=(DJ)(DJ)^*\) and \(B_1=J^*D^2J=(DJ)^*(DJ)\) coincide because, at each eigenvalue \(\lambda>0\), \(DJ\) and \((DJ)^*/\lambda\) are inverse maps of the respective eigenspaces. Thus \(\|B_1\|\le1+\delta\). As \(J,J^*\) act by nonnegative multipliers and summation, \(V^2=J^*C_1J\) has pointwise kernel error bounded by \(\delta B_1\) relative to \(B_1\), giving \(\|V^2-B_1\|\le\delta(1+\delta)\). The variational characterization of each ordered eigenvalue of a compact positive operator bounds its change by the norm of a perturbation. Applying this twice, with zeros appended if necessary, bounds the change from \(d_j^2\) to the unnormalized \(j\)-th eigenvalue of \(V^2\) by \((2+\delta)\delta\). Vacuum normalization costs at most the same amount because every squared eigenvalue is bounded above by the top one. This proves (4). The argument uses the pointwise bridge estimate on the kernels before and after multiplying by \(D\). The conversion to an operator-norm estimate uses componentwise absolute values. Row 1317, (8), treats the one-slice multiplier, corresponding here to a rank-one label matrix.

**PROVED.** For every periodic integer time length \(T\ge3\),
\[
 (1-\delta)^T\le
   \frac{\operatorname{Tr} V^T}{\operatorname{Tr} U^T\,\operatorname{Tr} A^T}
   \le(1+\delta)^T .                                                     \tag{5}
\]
For a fixed string of labels \(i_0,\ldots,i_{T-1}\), write its Wilson probability as the expected product of the \(T\) indicators. Conditional on all slices except one, that slice has its two-end bridge law. All other prescribed labels are measurable outside it. Remove the indicators one at a time using (2). The resulting probability is between \((1-\delta)^T\prod_t p_{i_t}\) and \((1+\delta)^T\prod_t p_{i_t}\). Multiply by the nonnegative factors in (3) around the circle and sum. The \(p_i\)'s cancel at each site and the remaining label sum is \(\operatorname{Tr}A^T\). Omitting or restricting strings gives the same relative bounds for any nonnegative function of the entire path of labels, with the corresponding finite label sum. In particular the estimate applies even to a very rare path.

**PROVED.** For a positive transfer \(F\) define \(\Psi_F(T)=2\log\operatorname{Tr}F^T-\log\operatorname{Tr}F^{2T}\). Multiplication of \(F\) by a positive scalar cancels. Equation (5) at \(T,2T\) gives, for \(\delta\le1/2\),
\[
       |\Psi_V(T)-\Psi_U(T)-\Psi_A(T)|\le8T\delta .                      \tag{6}
\]
Also \(\Psi_A(T)\ge0\), by expanding the square of the sum of its nonnegative eigenvalues to the \(T\)-th power and retaining the diagonal terms. Thus if \(T\delta=o(1)\), this class of interactions cannot decrease the original Wilson doubling defect by a fixed positive amount. The same conclusion for the first physical gap follows from (4) when \(\delta=o(a)\) and the first energy under comparison stays bounded in physical units.

## A low excitation carried by one elementary loop in the modified theory

**PROVED.** Use one plaquette and set \(\sigma=+1\) for \(Mw_p\bmod1\in[0,1/2)\), \(-1\) otherwise. Choose \(A_{ij}=(1+\rho i j)/2\) for \(i,j\in\{-1,1\}\), \(0\le\rho<1\). The two eigenvalues of \(A\) are \(1,\rho\). The factor in (3) is the strictly positive, gauge-invariant, nearest-time interaction \(1+\rho\sigma(x)\sigma(y)\). The two signs in each interaction are readings of original links on consecutive slices. The transfer being estimated here has a different action from Wilson's. Its time-reflection positivity follows from \(V=J^*(A\otimes U)J\) and the symmetric slice weights. For a link plane the reflection pairs the two halves by the positive form of \(V\), and reflection in a site plane gives an integral of squared half-path amplitudes.

**PROVED.** Put \(M=\lceil\exp(\log^2(1/a))\rceil\) for \(0<a<1\), \(\beta=O(\log(1/a))\), and \(\rho=e^{-a^2}\). Here \(a\) is the numerical spacing in fixed physical length units. Equation (4) gives
\[
              -a^{-1}\log v_1\le a+o(a).                                \tag{7}
\]
Indeed the second product eigenvalue is at least \(\rho\) and \(\delta=o(a^k)\) for every fixed \(k>0\). The finite-volume kernel in this example is bounded above and bounded strictly away from zero at each fixed cutoff, up to versions on the sign boundaries. To see simplicity of the vacuum, take the modulus of a real top eigenfunction. This attains at least the original Rayleigh quotient, with strict increase for a sign change of positive measure. A nonnegative top eigenfunction is positive almost everywhere by the integral equation. Two orthogonal top eigenfunctions are then impossible. Thus (7) concerns an excited state on the gauge-invariant space.

**PROVED.** In the same model
\[
 \Psi_V(T)=\Psi_U(T)+
            \log\frac{(1+\rho^T)^2}{1+\rho^{2T}}+O(T\delta).
                                                                         \tag{8}
\]
For all \(3\le T\le t_0/a\) the extra term tends uniformly to \(\log 2\). Every \(\Psi_U(T)\ge0\) by the same eigenvalue argument as for \(A\). The model (3) therefore fails the thermal input `A-B**` throughout the window \(2T\le s_i<48T\), where the required upper bound is at most \(y_0/16\) for \(0<y_0\le1/20\). The full normalized-trace criterion `A-B*` also fails because (7) places a second term tending to one in that trace for these \(T\). The constants in (1) for one plaquette are independent of the spatial size. These conclusions allow any starting Wilson defect, including an arbitrarily small one.

**PROVED.** For the unmodified \(U\), let \(\Pi_r=\mathbf1_{[r,1]}(U)\), \(0<r\le1\), and let \(g\) be a function on the labels with \(\sum_i p_i g(i)=0\). With \(M_g\) the corresponding multiplication operator, (2) and positivity give
\[
                  \|\Pi_r M_g\Pi_r\|
               \le r^{-2}\delta\sum_i p_i|g(i)|.                        \tag{9}
\]
This follows from \(\|U M_g U\|\le\delta\sum_i p_i|g(i)|\) by inverting \(U\) on \(\operatorname{ran}\Pi_r\) on both sides. In particular no unit physical state with energy at most a fixed \(E\), and no matrix element between two such states, can distinguish these centered readings with order-one amplitude for \(r=e^{-aE}\), \(\sum_i p_i|g(i)|\le1\). This is an estimate on actual Wilson states. It leaves their matrix elements against the rest of the local algebra undetermined.

## Which measurements can distinguish the change of action?

**PROVED.** Let \(F\) be a bounded observable on a periodic spacetime torus. Suppose its Lipschitz constant in each marked link separately, for the round distance and with all other links fixed, is at most \(L_F\). Set \(H_F=\|F\|_\infty+L_F\). In the experiment above keep the \(B\) disjoint readings per slice and use a product partition into intervals of the individual circles (binary intervals suffice). If there are \(P=BT\) readings, put
\[
      e_0=C(1+\beta)^{3/2}/M,\qquad e_1=C(1+\beta)^{5/2}/M .
\]
For every prescribed path of all interval readings, of product-uniform probability \(p>0\),
\[
 \left|\frac{\mathbb E_U[F\,\mathbf1_{\rm path}]}{p}
                  -\mathbb E_U F\right|
       \le P e_1 H_F (1+e_0)^{P-1}.                                    \tag{10}
\]
Here \(\mathbb E_U\) denotes the ordinary periodic Wilson path law. Constants are absolute after enlargement.

**PROVED.** In the coordinates preceding (1) let \(D(s,\omega)=2r(s)e^{h\cdot x(s,\omega)}/(\pi Z(h))\). Holding the other links and \(\omega\) fixed, \(|\partial_s x|=1/r(s)\), and \(\int_{-1}^1 |r'(s)|\,ds=2\). The total variation in \(s\) of \(D(s,\omega)F(x(s,\omega))\), extended by zero, is at most \(C(1+\beta)^{5/2} H_F\). Indeed differentiating \(r\) costs its total variation, while the other derivatives cost at most \(|h|\|F\|_\infty+L_F\) after multiplication by \(r\). The cap lower bound controls the factor \(e^{|h|}/Z(h)\). A Lipschitz \(F\) is absolutely continuous on every closed interior arc and the integrated bounds extend to both endpoints. The shifted Riemann-sum estimate of (1), integrated over \(\omega\) and over a prescribed interval, gives error at most \(e_1 H_F\) after division by that interval's length. This estimate holds conditional on every other raw link. All the other label indicators are measurable there, including those at adjacent times. Telescope the product of the normalized indicators against 1, applying this bound to one marked link in each term. By (1), successively removing any remaining normalized indicators bounds their joint expectation by \((1+e_0)^{P-1}\). This proves (10) without dividing by an uncontrolled probability.

**PROVED.** The probability of the prescribed path divided by \(p\) is at least \((1-e_0)^P\). Conditional expectations of \(F\) for *all* such paths therefore differ from its original Wilson expectation by at most \(2 P e_1 H_F (1+e_0)^{P-1}/(1-e_0)^P\), enlarging \(C\) if needed. Under (3) the conditional law given the label path is exactly its Wilson conditional law. It follows that on boxes with \(P\) polynomial in \(1/a\), every family with \(H_F\) polynomial in \(1/a\) has the same expectations up to \(o(a^k)\) for every fixed \(k>0\), for the frequency and bare-coupling range of (7). This includes products of polynomially many normalized Wilson loop traces with polynomial total path length because telescoping a unitary product bounds the Lipschitz constant by its number of uses of the varied link. The estimate also permits polynomial scalar rescalings when both bounds on \(F\) remain polynomial. The bit field in (7) lies outside this regularity class. Agreement on these tests does not control arbitrary cutoff-dependent observables.

**PROVED.** The added mode has a time-correlation test that also works with the time-volume limit taken first. With \(\rho=e^{-am}\), \(m>0\), condition a time interval of the marked line on its two endpoint spins and every link outside its interior private links. All other raw variables may be held fixed. The one-private-link estimate (1), now conditional on the other interior links too, compares the unmodified probabilities of every interior bit string to the product of fair bits, with factors between \((1-e_0)^l\) and \((1+e_0)^l\) for \(l\) interior sites. The interaction in (3) then gives the nearest-neighbour chain with transition \(A\) and these fixed end spins, up to a normalized density ratio between \(((1-e_0)/(1+e_0))^l\) and its reciprocal. This is uniform in both endpoints and the rest of the torus. In the reference chain \(A^d_{ij}=(1+\rho^d i j)/2\). Hence on an interior interval at distance at least \(q\) from both ends the density relative to the stationary reference string is the product of two end factors \(1+\rho^{d}i j\), divided by the analogous factor for the full interval. It tends uniformly to one whenever \(\rho^q\to0\). Take \(q=\lceil a^{-1}\log^2(1/a)\rceil\) and two interior times separated by \(\lfloor\tau/a\rfloor\), so \(l e_0\to0\). In the modified model their means tend to zero and their correlation tends to \(e^{-m\tau}\). The bounds hold for every enclosing torus long enough to contain this interval. They separate a dynamical mode with any chosen \(m>0\) from a purely time-independent random sign. This single marked plaquette singles out a spatial location and a time axis.

## A four-dimensional comparison using only gauge links

**GUIDE.** Three prior comparisons matter here. Row 1175, (29), adjoins a separate sign system and can leave all Wilson path marginals identical. Row 1192, (44)–(50), changes a single analytic plaquette weight and finds an extremely slow neutral level and measurements that detect the change. Row 1317, (16), uses a separate scalar lattice action with bare mass equal to spacing squared. I now put that last action on a *local reading of the original link variables*, with the same interaction rule in all four coordinate directions. This tests whether the usual Wilson measurements and Euclidean reflection positivity would exclude a massless local channel in such a comparison. [Row 1175](gap-solve16-astra62.md) · [Row 1192](gap-solve20-astra62.md) · [Row 1317](gap-solve36-astra62.md)

**PROVED.** Fix \(b=32\) and take fine periodic lengths divisible by \(b\). A coarse cell at \(u\) has interior vertices \(bu+\{1,\ldots,b-1\}^4\). Let \(S_u\) be the sum of the normalized Wilson traces over all unoriented elementary plaquettes with vertices in that interior, counting each elementary square once. Let \(z_u=MS_u\bmod1\). Keep all fine links except eight per cell exactly. In the eight private links keep only their bins, of round diameter at most \(h\le1\) and probability Haar mass at least \(c h^3\). Such a partition is given by Voronoi cells of a maximal \(h/2\)-separated set, breaking ties measurably. Each contains a ball of radius \(h/4\) up to its boundary, and the spherical area element gives the stated mass. Call these exact links and bins the data \(\mathcal D\). The choice of private links is used only for estimates. The actions below do not use that choice.

**PROVED.** In the ordinary Wilson law, conditionally on \(\mathcal D\), the joint law of the \(B\) cell readings has density relative to product uniform measure within \(\Delta_B\) of 1, where
\[
        s_0=C h^{-24} e^{100\beta}/M^2,\qquad
        \Delta_B=(1+s_0)^B-1,\qquad s_0<1 .                             \tag{11}
\]
Take the private links as the outgoing 1- and 2-links at each of the four vertices \(bu+(4+5j,4,4,4)\), \(j=0,1,2,3\). The two at a vertex are together in just one plaquette. No plaquette uses links from different pairs. Given the other links, the pairs are independent, including after the bin restrictions. On one pair \((x,y)\), the part of the Wilson exponent that varies is \(\beta(x\cdot Oy+a_1\cdot x+a_2\cdot y)\) for a fixed orthogonal \(O\) and \(|a_i|\le5\). Its bin-restricted normalization against unrestricted probability Haar is at least \(c h^6 e^{-11\beta}\). The part of \(S_u\) that varies on this pair is \(x\cdot Oy\) plus one-variable terms.

**PROVED.** Here I use the high-frequency Haar estimate in row 1317, (5). Its proof bounds the modulus of the integral of \(A(x)B(y)e^{i t x\cdot Oy}\) by \(C(1+|t|)^{-1/2}\) when both amplitudes are bounded by one. In particular bin indicators and the two separate phases are allowed. To include the real Wilson density in the numerator, the two linear exponentials cost \(e^{10\beta}\), and expansion of \(e^{\beta x\cdot Oy}\) into products of four coordinate pairs costs at most \(e^{4\beta}\) in sum of absolute coefficients. Dividing by the lower normalization above gives \(C h^{-6}e^{25\beta}(1+|t|)^{-1/2}\) for one pair. For a nonzero integer Fourier index \(l\) use \(t=2\pi lM\) and multiply the four pair bounds for a cell. The absolute sum over \(l\ne0\) is at most \(s_0\), since \(\sum_{l\ge1}l^{-2}<\infty\). The absolutely convergent Fourier series gives the density since integration against trigonometric polynomials identifies the measure, and these are uniformly dense in continuous periodic functions. Conditional independence across cells proves (11). [Haar estimate and proof](gap-solve36-astra62.md)

**PROVED.** Consequently a nonnegative integrable weight \(W(z)\), of positive uniform integral, changes the joint law of \(\mathcal D,z\) as follows. Its density relative to the product of the **original** law of \(\mathcal D\) and the probability \(W(z)\,dz/\int W\) is between \((1-\Delta_B)/(1+\Delta_B)\) and the reciprocal, if \(\Delta_B<1\). This is division of (11) by the normalizer in the same bounds. In particular this relative error contains no inverse factor \(\int W\). For a parameter \(n\to\infty\), choose
\[
 h=e^{-(\log n)^{3/2}},\qquad M=\lceil e^{(\log n)^2}\rceil,\qquad
 \beta=O(\log n).
\]
On any family with \(B\) polynomial in \(n\), both \(\Delta_B\) and \(h\) are \(o(n^{-k})\) for every fixed \(k>0\). The same construction works at other prescribed \(\beta_n\) by increasing \(M\) in (11). A Wilson observable \(F\) of polynomial supremum norm and polynomial separate link Lipschitz bounds can be replaced uniformly by its value at bin representatives with error at most \(8Bh L_F\). Thus on these tori every such measurement has the same expectations to all algebraic orders under the two link laws. Joint expectations with a function of \(z\) obey the same absolute-error estimate times its absolute moment under \(W(z)\,dz/\int W\), with the errors from \(F\) and (11) added. This statement allows the number of cells and the weight to change along the sequence.

## A massless local reading in the comparison

**PROVED.** For \(0<\eta<1\), let \(Y_u\) be the inverse distribution function of the centered real normal law of variance \(\eta^{-2}\) at \(z_u\). Assign a finite value at the null endpoint. Multiply the Wilson density by
\[
             W=\exp\!\left[-\tfrac12
                    \sum_{u,\mu}(Y_{u+\hat\mu}-Y_u)^2\right].            \tag{12}
\]
Every \(Y_u\) is a gauge-invariant function of links within one cell. The new factors use only adjacent cells. Coarse translations and the hypercubic symmetries of the cell array preserve (12). On an even rectangular array the modified law is reflection positive through the planes between cells perpendicular to each of the four axes. These planes pass through fine lattice sites. For the original Wilson weight, conditioning on the tangential seam links on the two fixed planes splits the path integral into mirror half-integrals. A face lies on one side or on a seam and its weight there can be split into equal half-weights. Thus a reflected square integrates to a squared modulus averaged over seam data. The intra-half terms of (12) multiply the two halves by reflected factors. For a crossing pair of cells, expand its factor using
\[
    e^{-(y-y')^2/2}=\int_{\mathbb R}e^{i t y}e^{-i t y'}
                                    e^{-t^2/2}\,dt/\sqrt{2\pi}.
\]
Reflection carries the local reading into the identical reading on the opposite cell, since reversing a square preserves its real normalized trace. The product of the crossing factors is an average of reflected squares, which proves the assertion. No fine-lattice reflection through the interior of a cell is needed for this claim.

**PROVED.** Under the uniform reference on \(z\), the \(Y_u\)'s are independent normals of variance \(\eta^{-2}\). After (12) their exact reference law is the periodic Gaussian of precision \(-\Delta_{\rm cell}+\eta^2 I\), where \(-\Delta_{\rm cell}\) is the positive nearest-neighbour graph Laplacian. By (11) all its normalized expectations of integrable functions of \(Y\) agree with those in the modified gauge-link integral to relative density error at most \(2\Delta_B/(1-\Delta_B)\). This gives, in particular, an absolute bound by this number times the Gaussian absolute moment for a signed function. Uniform one-cell frequency mixing in the original measure and this comparison are statements about distinct Gibbs laws.

**PROVED.** Let the coarse spacing be \(d=ba=1/n\) with even \(n\), put \(\eta=d^2\), and take even tori. In the one-direction doubling defect for coarse time lengths \(T,2T\), (12) adds the Gaussian defect up to an absolute error at most \(6\max(\Delta_B,\Delta_{2B})\) when both errors are at most \(1/2\). Indeed each log partition differs from the sum of its Wilson and Gaussian logs by at most \(2\Delta\), with the Gaussian integral normalized by one factor \(\eta/\sqrt{2\pi}\) per cell. These factors cancel on doubling. In units of the fine lattice the original time lengths are \(bT,2bT\). The Gaussian determinant from row 1317 gives a nonnegative contribution from each spatial momentum to the defect. Its zero momentum contributes
\[
            \log\frac{1+e^{-T\omega}}{1-e^{-T\omega}},\qquad
                       \omega=2\operatorname{arsinh}(\eta/2).
\]
For \(dT\to t>0\) this diverges, even on spatial sides \(2T\) in coarse units. The modifying interaction has obtained a worse thermal bound while preserving all polynomial-resolution Wilson measurements specified after (11). [Gaussian determinant, row 1317](gap-solve36-astra62.md)

**PROVED.** There is also spectral weight at strictly positive arbitrarily small energies in a *local continuum limit* of the \(Y\) readings, without using the torus zero mode. Take physical side \(L=n^2\) in each of the four directions, so each side has \(N=L/d=n^3\) coarse cells. Work on the box centered about the origin and take \(f\) smooth with compact support on \(\mathbb R^4\). For cell centers \(x_u\), define
\[
                Y_d(f)=d^3\sum_u f(x_u)Y_u .
\]
In the reference Gaussian its covariance with \(Y_d(g)\), conjugating the first test, is
\[
 \frac1{L^4}\sum_p
 \frac{\overline{\widehat f_d(p)}\,\widehat g_d(p)}
      {d^2+4d^{-2}\sum_{\mu=1}^4\sin^2(dp_\mu/2)},\qquad
 \widehat f_d(p)=d^4\sum_u f(x_u)e^{-ip\cdot x_u}.                      \tag{13}
\]
Here \(p\in(2\pi/L)\mathbb Z^4\) in one Brillouin cube. Fourier modes on the finite periodic graph diagonalize its Laplacian, and \(\eta^2/d^2=d^2\), giving (13). The shift to cell centers contributes cancelling phases.

**PROVED.** The zero-mode term of (13) is \(O(L^{-4}d^{-2})\to0\). On the Brillouin cube the denominator is at least \(4|p|^2/\pi^2\). On \(0<|p|\le\varepsilon\), bounded numerators therefore give total magnitude at most \(C(\varepsilon^2+L^{-2})\). In fact the \(j\)-th integer shell in the maximum norm has at most \(C j^3\) points by taking the difference of two fourth powers, and every point on it has \(|p|\ge 2\pi j/L\). At high momentum, applying \(k\)-th finite differences to \(f\) in a largest momentum coordinate yields \(|\widehat f_d(p)|\le C_k(1+|p|)^{-k}\). The differences divided by \(d^k\) are integrals of a bounded derivative over \(k\) unit intervals and have uniformly bounded support. The Fourier difference factor has magnitude at least \(2d|p_\mu|/\pi\). These two estimates make the tails uniformly negligible. On every fixed annulus the spatial Riemann sums converge uniformly to \(\widehat f,\widehat g\), and the momentum sum converges to the integral with measure \(d^4p/(2\pi)^4\). Sending the annulus ends to zero and infinity proves the limit
\[
                  \int_{\mathbb R^4}
                   \frac{\overline{\widehat f(p)}\,\widehat g(p)}
                    {|p|^2}\,\frac{d^4p}{(2\pi)^4}.                    \tag{14}
\]
For a finite list of tests the joint Gaussian characteristic functions converge by the covariance formula. All their fixed absolute moments stay bounded, by the corresponding one-variable finite normal moments and Hölder's inequality. Since \(B=N^4\) is polynomial in \(n\), (11)–(12) transfer the characteristic functions and all joint moments to the modified gauge theory. This proves a massless Gaussian scalar limit for this specified family of local link readings.

**PROVED.** For a real nonnegative test \(f\) of nonzero integral supported a positive distance inside \(t>0\), its connected reflected two-point function at additional time separation \(\tau\ge0\) in (14) is
\[
 \int_{\mathbb R^3} e^{-\tau|\mathbf p|}
  \left|\int f(t,\mathbf x)e^{-t|\mathbf p|}
                   e^{-i\mathbf p\cdot\mathbf x}\,dt\,d^3\mathbf x\right|^2
                  \frac{d^3\mathbf p}{(2\pi)^3\,2|\mathbf p|}.           \tag{15}
\]
The inverse time Fourier transform of \((p_0^2+r^2)^{-1}\) is \(e^{-r|t|}/(2r)\) for \(r>0\), as follows by solving the one-dimensional Green equation with derivative jump \(-1\) at zero. The squared amplitude in (15) tends to \(|\int f|^2>0\) as \(\mathbf p\to0\). Thus the positive measure for this one local vector gives weight to every \((0,m)\), \(m>0\), and has no atom at zero. Equivalently, restricting (15) to a sufficiently small momentum ball with radius less than \(m/2\) gives a positive multiple of \(e^{-\tau m/2}\) as a lower bound. A gap \(m\) on the vacuum complement is impossible in this scalar channel. This conclusion is for (12). The undeformed Wilson action is the reference measure in (11).

## Returning to the unmodified Wilson law

**PROVED.** There is a volume-uniform conclusion for ordinary Wilson fields. Take \(k\) of the cells in any region and condition on every link except their private pairs, retaining also the bins of those pairs. The proof of (11) applies with \(k\) in place of \(B\), independent of the number of cells outside. Thus for any integrable \(G\) of their phases with mean zero under product uniform measure \(dz\), and any integrable exterior reading \(H\),
\[
        |\mathbb E_{\rm W}(HG)|\le
        \Delta_k\,\mathbb E_{\rm W}|H|\,\int |G|\,dz .                  \tag{16}
\]
In particular choose \(k\) cells in a bounded positive-time physical region disjoint from its reflection, using a plane between cells. Apply (11) to these \(2k\) cells, with \(G\) on the positive cells and its reflected conjugate on the negative cells. Independence under the reference product makes the reference integral zero and gives
\[
       0\le \mathbb E_{\rm W}[(\theta\overline G)G]
                       \le\Delta_{2k}\left(\int|G|\,dz\right)^2 .        \tag{17}
\]
The lower bound is ordinary site reflection positivity. The upper bound holds uniformly over the entire space of measurable \(G\) with the displayed norm bound, including functions varying with the cutoff. With the frequencies of (11) and \(k\) and the norm polynomial in \(n\), the reflected squared norm tends to zero faster than any inverse power. The bound holds on every sufficiently large periodic torus at each cutoff and for its periodic-state limits for these readings. Indeed for fixed cutoff one can approximate interval tests in product-uniform \(L^1\) by continuous local tests. The relative density estimate bounds the approximation error uniformly in volume, and the continuous tests pass by weak convergence. For general integrable functions, approximation in that same \(L^1\) on each reflected half works by the joint density bound on the two halves. For (16) with unbounded \(H\) the finite-torus conditional inequality is the assertion used. There is no assumed volume-cutoff exchange in (17).

**PROVED.** One can see the difference between (12) and the physical Wilson transfer by using the *identical* unbounded cell reading. Under ordinary Wilson at the same \(\eta=d^2\), the field \(d^4\sum_u f(x_u)Y_u\) has Gaussian white-noise limits for compactly supported tests. Under the uniform product reference its covariance is \(d^8\eta^{-2}\sum_u\overline{f(x_u)}g(x_u)=d^4\sum_u\overline{f(x_u)}g(x_u)\to\int\overline f g\). Its finite collections are Gaussian there. Apply (11) just on the cells meeting the supports to transfer characteristic functions and moments, uniformly in any larger volume. The white noise contributes zero reflected norm for centered linear tests separated from the mirror. Even with the larger normalization \(d^3\) of (13), its separated reflected covariance goes to zero by (17) because its product-reference absolute moments grow only polynomially. A massless local state in (15) is therefore a consequence of the extra interaction in (12). It gives no upper bound on the physical mass in ordinary Wilson theory.

**PROVED.** The elimination in (17) misses even an elementary unwrapped Wilson fluctuation. Fix a spatial plaquette \(p\) and set \(X=\beta(1-w_p)\). For the same \(k\) cells, and uniformly over the torus, the conditional mean of \(X\) given their phases satisfies
\[
  \left\|\mathbb E_{\rm W}[X\mid (z_u)]-\mathbb E_{\rm W}X\right\|_\infty
        \le C\beta\left(h+\frac{\Delta_k}{1-\Delta_k}\right)
                                                        \quad(\Delta_k<1/2).
                                                                         \tag{18}
\]
For this assertion \(\mathcal D\) uses bins only on the \(8k\) private links. Replacing the links of \(p\) by representatives, when necessary, changes \(X\) by at most \(4\beta h\). This follows by telescoping the holonomy and using the round distance. The replacement is \(\mathcal D\)-measurable and bounded by \(2\beta\). Under Wilson, the conditional density of \(\mathcal D\) given almost every phase vector, relative to its unconditioned law, is between \((1-\Delta_k)/(1+\Delta_k)\) and its reciprocal, by (11). This proves (18). On the other hand row 1317, (6) and its unwrapped variance consequence, bounds the two-end conditional variance of \(X\) below by an absolute constant for \(\beta\ge1\). It applies here on every time circle of length at least three by conditioning on the other slices, hence \(\operatorname{Var}_{\rm W}X\ge c>0\). [Unwrapped variance](gap-solve36-astra62.md)

**PROVED.** Conditional expectation is the best squared-error predictor among all functions of the observed phases. Writing \(P\) for conditional expectation and expanding \(|X-PX+PX-g|^2\) shows that the cross term integrates to zero. From (18), when \(k\) grows polynomially and \(1\le\beta=O(\log n)\), it follows that
\[
     \inf_g \mathbb E_{\rm W}|X-g((z_u))|^2
          = \operatorname{Var}_{\rm W} X-o(1)\ge c-o(1).                \tag{19}
\]
No smoothness, degree or norm restriction on the predictor \(g\) improves this bound. This is a failure of recovery in the ordinary Euclidean probability space. A positive one-slice Euclidean variance by itself gives no lower bound on the continuum reflected norm of \(X\). Equations (9), (17), and (19) explain why excluding all the rapidly varying phases fails as a proof of a uniform spectral lower edge.

**OPEN.** For the actual, isotropic Wilson action the term still needed in (6) is \(\Psi_U(T)\). Concretely, in the one-scale route of row 1218, fix \(t_0>0\) and \(0<y_0\le1/20\). At every sufficiently large physical volume index and every sufficiently fine matched cutoff there, one needs a common integer \(3\le T\le t_0/a\) such that for all integer \(2T\le s_i<48T\),
\[
      2\log Z_{\rm W}(s,T)-\log Z_{\rm W}(s,2T)
                 \le \frac{y_0 s_1s_2s_3}{2(96T)^3}.                  \tag{20}
\]
Here the spatial shape and bare coupling are identical in the two partition functions. The scalar normalization of the transfer cancels. This sufficient input and the matching continuum construction have not been obtained. An alternative proof would need a common positive lower edge on a total set of local states in the constructed nontrivial Yang–Mills vacuum representation. The class removed in (17) has vanishing reflected norm, while (19) leaves the unwrapped physical observables to be estimated.

## Testing the finite-degree Wilson space

**GUIDE.** The remaining question in (20) could in principle have been hidden by the norm restriction on \(F\) in (10). A polynomial of low degree in each link can have a very large supremum norm relative to its \(L^2\) norm on a whole slice. Row 1192, (6)–(7), already gives a finite-cube, magnetic-half-weighted polynomial space approximating all normalized low-energy Wilson vectors, of link degree \(O(\beta+\log n)\) at prescribed power accuracy. I use its scope and do not repeat that truncation. Here is a relative, volume-accounted test for polynomial observables in the *periodic Euclidean path law*. [Row 1192, low-energy subspace](gap-solve20-astra62.md#which-physical-energies-survive-the-replacement)

**PROVED.** Use the elementary readings and disjoint private links of (10). Let \(F\in L^2\) be a polynomial of total degree at most \(D\) in the four real coordinates of each private link with the other links fixed. Its coefficients on all other links can be arbitrary. Put
\[
            \zeta=C(1+\beta)^{5/2} e^{12\beta}(D+1)^6/M .
\]
If \(\zeta<1\), for every prescribed path of intervals of product-uniform probability \(p\),
\[
    (1-\zeta)^P\,\mathbb E_{\rm W}|F|^2
       \le p^{-1}\mathbb E_{\rm W}\big[|F|^2\mathbf1_{\rm path}\big]
       \le(1+\zeta)^P\,\mathbb E_{\rm W}|F|^2 .                         \tag{21}
\]
This bound incurs no ratio between the global supremum and the global \(L^2\) norm.

**PROVED.** At one link let \(q\) be its polynomial with all other links fixed. The space of degree at most \(D\) has dimension at most \(\binom{D+4}{4}\) by counting monomials. For an orthonormal basis in Haar \(L^2(S^3)\), the sum of the squared absolute basis values at a point is constant by rotation invariance and change of basis. Integration gives that constant as the dimension. Thus \(\sup |q|^2\le C(D+1)^4\int |q|^2 dx\). On a great circle \(q\) is a trigonometric polynomial of degree at most \(D\), because a unit-speed great circle has coordinates linear in \(\cos t,\sin t\). Each Fourier coefficient is at most \(\sup|q|\) in modulus, so differentiation gives \(\sup |q'|\le D(D+1)\sup|q|\). The one-link Lipschitz constant of \(|q|^2\) is at most \(2D(D+1)\sup|q|^2\). Finally the actual one-link law dominates \(e^{-2|h|}dx\), with \(|h|\le6\beta\). Applied to \(|q|^2\), the single-link bound proved in (10) has error at most \(\zeta\,\mathbb E(|q|^2\mid\text{other links})\) after dividing by interval length. The other indicators are measurable on that exterior. Iteration proves (21).

**PROVED.** For any positive reweight of the interval paths, the ratio of squared norms on this entire polynomial space, reweighted to Wilson, is between \((1-\zeta)^P/(1+e_0)^P\) and \((1+\zeta)^P/(1-e_0)^P\). Sum (21) against the path weights and use (1) for the normalizer. By polarization, the absolute inner-product error for \(F,G\) is at most the maximum deviation of these bounds from one times \(\|F\|_{L^2({\rm W})}\|G\|_{L^2({\rm W})}\), since the two quadratic-form bounds put its Gram operator between the corresponding multiples of the identity. At the frequency of (7), polynomial \(D,P\) and logarithmic \(\beta\), this error is smaller than every inverse power on the unit ball. Nevertheless (7)–(8) hold for the indicated reweight. The test thus preserves even all these normalized polynomial inner products on polynomial periods while introducing a slow level. The estimates are on Euclidean path norms. Neither (21) nor the finite-cube spectral truncation of row 1192 bounds the vacuum-normalized sum of the remaining Wilson eigenvalues at (20).

## Taking volume first in the test of the scalar channel

**PROVED.** The massless scalar conclusion for (12) also holds when one first takes periodic-volume limits at each cutoff. There is a volume-independent comparison for the \(Y\) fields, although the joint relative-density comparison with the underlying Wilson measurements in (11) costs the number of cells. Write \(s=C e^{100\beta}M^{-2}\) with a sufficiently large absolute \(C\). The proof of (11) for one cell works with no bins, conditioning on all raw links except its four private pairs. Given that exterior, the density of \(z_u\) in ordinary Wilson differs from 1 by at most \(s\). In (12) only the eight Gaussian edge factors incident to this cell vary. Completing the square shows that its modified conditional law for \(Y_u\) has density relative to
\[
          N\!\left(\frac{\sum_{v\sim u}Y_v}{8+\eta^2},
                              \frac1{8+\eta^2}\right)                    \tag{22}
\]
between \((1-s)/(1+s)\) and its reciprocal. The same bounds hold conditional on just the exterior scalar readings. Indeed (22) is determined by those readings, and conditional expectation preserves both inequalities for each bounded nonnegative test.

**PROVED.** At fixed \(\eta>0\) and \(0<s<1/4\), on any sufficiently large finite coarse torus, write \(X\) for the exact reference massive Gaussian and \(Y\) for the reading under (12). For each fixed \(1\le p<\infty\) their laws admit couplings with
\[
       \max_u\|Y_u-X_u\|_{L^p}
               \le C_p(8+\eta^2)\eta^{-2}s^{1/p}+\varepsilon            \tag{23}
\]
for arbitrary \(\varepsilon>0\), uniformly in the torus. To see the one-coordinate error, let \(\nu\) be a probability with density within \(C s\) of 1 relative to a normal \(\gamma\) of variance \((8+\eta^2)^{-1}\) and mean \(h_*\). Couple the common part identically, then pair the residuals independently after normalization. The residual submeasures are each bounded above by \(C s\gamma\). The integrated cost on them is at most \(C_p s\int |y-h_*|^p\,d\gamma\) by the triangle inequality to the common center, also when the residual mass is zero. Thus the one-coordinate \(L^p\) cost is at most \(C_p s^{1/p}\), independently of \(h_*\). The conditional laws on the finite standard Borel spaces may be sampled by their one-real-variable distribution functions, which makes this a measurable coupling.

**PROVED.** Start from any coupling of the two equilibrium measures with finite \(p\)-th moments. At fixed finite volume these moments exist, since the unbinned product bounds \((1-s)^B,(1+s)^B\) compare the full reweighted marginal to a finite multiple of its Gaussian law. Update one coordinate in each measure from its own conditional law. Couple the modified coordinate first to the normal in (22) for its own neighbors and translate that sampled normal by the difference of the two neighbor means to obtain the other coordinate. The equilibrium marginals are preserved. If \(D\) bounds the current maximum \(L^p\) discrepancy, the updated discrepancy is at most \(C_p s^{1/p}+\alpha D\), where \(\alpha=8/(8+\eta^2)\), by Minkowski's inequality. Take the starting bound at least \(D_*=C_p s^{1/p}/(1-\alpha)\). No step increases it, and after updating all coordinates once the new maximum is at most \(D_*+\alpha(D-D_*)\). Iterating these complete sweeps proves (23). This is a coupling argument, with no numerical updates required.

**PROVED.** For \(d=1/n,\ \eta=d^2\), the \(L^p\) error for the smeared fields from (23) is bounded by \(C_{f,p}d^{-1}(8+\eta^2)\eta^{-2}s^{1/p}\), taking the infimum over the arbitrary slack. This uses \(d^3\sum |f(x_u)|\le C_f/d\) once the volume contains its support. It vanishes faster than every power of \(d\). At fixed cutoff the Gaussian covariances on enlarging tori converge by Riemann sums on the compact Brillouin cube since \(\eta>0\). Their local moments are bounded uniformly in that volume. The coupled bounds give tightness of each finite family of \(Y\)'s at fixed cutoff, and apply to every subsequential periodic limit. If a joint limit with the links is taken, the identity \(e^{2\pi i M S_u}=e^{2\pi i\Phi_\eta(Y_u)}\), with \(\Phi_\eta\) the normal distribution function, passes by continuity. A finite real \(Y_u\) puts \(\Phi_\eta(Y_u)\) strictly inside \((0,1)\). Thus the same reading is obtained in the joint limit. After the volume limit, the infrared and ultraviolet bounds in (13) apply directly to the momentum integral. Hölder's inequality and (23), for arbitrarily large fixed \(p\), transfer all fixed smeared moments, giving (14) and (15) in this order of limits as well. This argument compares the scalar readings uniformly in volume. Agreement of the underlying ordinary Wilson measurements under the deformation was proved on the polynomial-size tori specified after (11).

**PROVED.** One boundary comparison for the ordinary link measurements also survives independently of total volume. Fix any collection of \(k\) cells and leave variable the links with both vertices inside each of their open interiors. Condition on all other raw links. The exterior cell readings are fixed, and the incident factors of (12) form a positive integrable function of the \(k\) interior readings with the prescribed exterior as parameter. The four-pair proof still gives (11) at fixed exterior. Hence the conditional laws of the finite-resolution data in this region under Wilson and (12), at the *same* raw exterior, have density ratio between \((1-\Delta_k)/(1+\Delta_k)\) and its reciprocal. This statement holds regardless of how unlikely the prescribed exterior might be. Passing from such conditional comparisons to an assertion about which unwrapped Wilson state is selected in infinite volume would require control of the exterior marginal.

## Conclusion

**OPEN.** Every eigenvalue of the original Wilson transfer occurs among the product eigenvalues approximated in (4). Its thermal defect enters (6) additively. The direct Wilson estimates (9) and (17) remove a definite family of candidate low-energy readings. They leave the unwrapped correlations in (19) and the partition functions in (20) uncontrolled at the physical scale. I obtain neither the nontrivial Yang–Mills continuum construction with the required observable algebra nor a common positive lower spectral edge above its vacuum. The derivations are author-side research and have not received an independent check.

RESULT — OPEN. The four-dimensional SU(2) Jaffe–Witten mass gap remains unproved here. For the original Wilson law, (9) and (17) exclude the specified rapidly oscillating plaquette readings from surviving low-energy matrix elements and reflected states at the stated normalizations. The transfer comparison (4)–(6) and the local construction (12)–(15), (23) show why giving these readings their own dynamics cannot supply the missing Wilson thermal estimate (20).
