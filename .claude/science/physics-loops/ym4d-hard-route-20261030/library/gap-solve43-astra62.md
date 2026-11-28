# Repo search

**GUIDE.** Row 1334 starts at `dd0ed8042`. No row-specific prior file was present. This is author research. PROVED labels mark hand arguments with their stated premises. This record grants no status.

**GUIDE.** The November 8 digest records searches of main and PRs 10114, 10133, 10134 and 10141, chiefly for ultraviolet obligations. I checked the following gap-related primary files identified by row 1218. PR 10114, `MASS_GAP_LOCAL_BLOCK_ASTRA.md`, lines 4–14 and 106–149, gives a single-plaquette witness and a small-bare-coupling contraction. Grok's PR 10133, `MASS_GAP_CROSSOVER_REDUCTION.md`, lines 77–90, leaves the crossover and source transport open. PR 10134, `mass-gap-interface.md`, I1–I5, distinguishes an excited space, a positive lower spectral edge and identification of the theory. PR 10141, `fp1.md`, lines 299–315, controls a classical constrained minimizer at one scale. The closest result on main is Theorem ZD-c at `8b11ae2bb9`, which consumes a uniform bound on the full physical periodic trace at one physical size. I found no competing row for that infrared estimate in the ownership registry. [Lead's search](prior/repo-search-2026-11-08.md) · [Main seed theorem](gap-phys-seed.md) · [Registry](open-registry.md)

**GUIDE.** The closest prior on the replica argument is row 1131, §3. It already matches all bare-plaquette terms whose incidence graph has even temporal winding, and uses a one-plane contour to show that their fraction on the split cover tends to zero. Its Haar rotation uses the junction observation of row 1121, Proposition J. Row 1118, §4.2, gives the earlier cellwise minimum over exchanges. I use these results as prior work. The questions treated below are the largest common mass after erasing the label of *every individual link*, its scale on *both* covers, the data needed to determine the closing condition, and what survives gauge invariance. I found no ownership entry for these questions. The exchange-cluster background cited by row 1131 credits Kandel and Domany, Niedermayer, Redner, Machta and Chayes, and the finite gauge-group covariance construction of Adhikari and Cao. [Row 1131](gap-council-prob-astra.md) · [Cell exchange](gap-conv-in-law-astra.md) · [Junction estimate](gap-conv-in-law-check-opus.md)

## Sources and target

**GUIDE.** Row 1218 reviews work by Deep Bhattacharjee, Ushashi Bhattacharya, James Montgomery Lockwood, Tristan Romanov, Ikailo John Sessford and Sanjeevan Singha Roy. Their thermal ascent requires a small full thermal trace on a window of shapes. The first four also study relaxation under cube updates. Zeng Chunping's common-rate and tunnelling criteria require additional infrared estimates. Applying these results to the tuned Wilson measure requires proving their hypotheses there. [Primary-reading record](prior/gap-onebound-read-sol.md)

**GUIDE.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, distinguish scalar reconstruction from the full observable algebra and positive spectral threshold. The relevant primary passages at `31a47c543775` are outline 581–599, 773–779 and 31860–31882, and CA-I 2704–2712 and 3213–3222. I used the outline's indexed chunks and obligations to locate them. Row 1333 checks row 1330's restricted thermal test and supplies an additional hypothesis for its application, namely a two-sided logarithmic bound on the bare coupling along the chosen trajectory. The strict thermal estimate in that row remains open. [Outline index](sa-index/README.md) · [Outline, scalar reconstruction](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L31860-L31882) · [Complete account I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2704-L2712) · [Row 1330](gap-solve42-astra62.md) · [Row 1333](gap-solve42-check-opus.md)

## Two periodic histories and one double period

**OPEN.** The Jaffe–Witten target requires a nontrivial continuum SU(2) Yang–Mills theory on four-dimensional space-time, with its full physical observable space, a unique vacuum and a strictly positive lower spectral edge above it in physical units. On a trajectory constructing that theory, take the dyadic physical lengths \(L=2^i\ell_1\), \(i\ge0\), of Theorem ZD-c, where \(\ell_1/(4a_j)\) is an integer at least three for all large \(j\). Seek one such \(L\) for which, with \(n_j=L/a_j\) and \(T_j=n_j/2\),
\[
 \limsup_{j\to\infty}\frac{Z(n_j,T_j)^2}{Z(n_j,2T_j)}<\frac{1651}{1650}.
 \tag{1}
\]

**GUIDE.** Here \(Z(n,u)\) is the ordinary SU(2) Wilson partition function on the periodic \(n^3\times u\) box, at the same coupling in numerator and denominator. If \(\lambda_i\) are its nonnegative transfer eigenvalues, \(z_u=\sum_i(\lambda_i/\lambda_0)^u\) and \(z_{2u}\le z_u\). Thus \(Z(n,u)^2/Z(n,2u)=z_u^2/z_{2u}\ge z_u\). This is the existing sufficient route from (1) to the two-stage seed of ZD-c. Its continuum use requires the reconstruction and observable matching of that route. I use the original Wilson measure at both periods. The extra coupling bounds in row 1333 concern the restricted measure of that row.

**GUIDE.** The matching test underlying row 1131 would succeed if a positive part common to both occupied more than \(1650/1651\) of the split weight uniformly. Its one-plane bound excludes that for its chosen expansion. I test whether more general matchings that preserve the unordered link pairs can do better. Row 1321's [two-replica transfer calculation](gap-solve38-astra62.md), §§“Keeping the signs around a physical time circle” and “Testing the physical parity bias”, exchanges whole slices and measures their continuation signs. Proposition SW in [the pinned O(4) sheet](gap-pinu-ev.md) uses exchange clusters on spin pairs. Here the elementary factors are the four-link plaquettes of the original four-dimensional Wilson law. The test concerns the integrated weights of the two covers. Credit for the physical trace identification is to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, outline GL3 and GL8, lines 2195–2228 and 2313–2336.

**GUIDE (row 1131's common positive integral and notation).** Fix \(n\ge8\) divisible by four, \(T=n/2\) and \(\beta>0\). Denote the split cover of the \(n^3\times T\) torus by \(c=0\), and the connected cover of time period \(2T\) by \(c=1\). Write \(Z_0=Z(n,T)^2\), \(Z_1=Z(n,2T)\). Give each positively oriented base link \(e\) an ordered pair \(x_e=(x_e^0,x_e^1)\) of SU(2) variables, with product normalized Haar measure. Orient every elementary plaquette. Label the lifts of links and plaquettes locally. Write \(\alpha_{pe}^c\in\mathbb F_2\) for the lift of \(e\) used by lift zero of \(p\). Lift one uses the complementary links. Take \(\alpha^0=0\). The inversions of links traversed backwards are the same on both sheets. Put \(a(g)=1-\operatorname{Re}\operatorname{tr}(g)/2\) and \(w(g)=e^{-\beta a(g)}\). Let \(W_p(s;x)\) be the product of the two \(w\)'s obtained by taking the plaquette word first with assignment \(s\in\mathbb F_2^4\) and then with its complement. In particular \(W_p(s+\mathbf1;x)=W_p(s;x)\). Each \(Z_c\) is the integral of \(\prod_p W_p(\alpha_p^c;x)\).

**GUIDE (row 1131, §3).** Set
\[
 m_p(x)=\min_s W_p(s;x),\qquad
 h_p^c(x)=W_p(\alpha_p^c;x)-m_p(x).
\]
Expand the product in \(Z_c\) by using \(h_p^c\) on a subset \(F\) and \(m_p\) elsewhere. All summands are nonnegative. Conditional on the original Wilson fields on cover \(c\), the face choices are independent and
\[
 \mathbb P_c(p\notin F\mid x)=m_p(x)/W_p(\alpha_p^c;x).                 \tag{2}
\]
Let \(G\) be the event that there exist bits \(u_e\) and \(v_p\) with \(\alpha_{pe}^1=u_e+v_p\) for every \(p\in F,\ e\in\partial p\). Equivalently, the cover has trivial sheet permutation on every cycle of the graph whose nodes are links and selected faces, joined at incidences. The equivalence follows by integrating the incidence bits along paths from one root in each component. Swapping the link pairs at the \(u_e=1\) preserves Haar measure and every \(m_p\). On \(F\) it transforms \(W_p(0;x)\) into \(W_p(\alpha_p^1;x)\) because flipping all four bits only exchanges the two scalar factors. The integrated summand is therefore the same for both covers whenever \(G\) holds. The empty set has positive weight, so
\[
 Z_0\mathbb P_0(G)=Z_1\mathbb P_1(G)>0,\qquad
 \frac{Z_0}{Z_1}=\frac{\mathbb P_1(G)}{\mathbb P_0(G)}
 \le \frac1{\mathbb P_0(G)}.                                           \tag{3}
\]
The event itself depends only on the marked faces. This argument makes no assertion that the terms on its complement agree.

## Reading which links belong to one lifted plaquette

**GUIDE.** To bound the right side of (3) I tested how much information about the cover survives erasure of each link's sheet labels. The observation on link \(e\) is the unordered pair \(\{x_e^0,x_e^1\}\) of raw group elements in the Wilson integral. Vertex gauges are integrated with normalized Haar measure. This observation retains gauge-frame information. A bound for methods preserving it has precisely that scope.

**PROVED (joint estimate for false pairings).** Call a face ambiguous if any of its seven alternative complementary pairings has Wilson weight at least that of the actual pairing. For either cover and any set \(D\) of vertex-disjoint base faces of one orientation,
\[
 \mathbb P_c(\text{every }p\in D\text{ is ambiguous})
 \le q_\beta^{|D|},\qquad
 q_\beta=\min(1,C(1+\beta)^{-3/2}),                                     \tag{4}
\]
with a numerical \(C\) independent of box size. Ambiguity is unchanged by a relabelling of the two values on any link.

**PROVED (tilting the true plaquettes).** For any set \(S\) of plaquettes of one orientation on either ordinary torus,
\[
 \mathbb E\exp\!\left(\frac{\beta}{2}\sum_{p\in S}a(U_p)\right)
 \le [J(\beta/2)/J(\beta)]^{|S|}\le C_0^{|S|},                         \tag{5}
\]
where \(J(b)=\int e^{-b a(g)}\,dg\). Use the normalized convolution ordering of row 1149, (16), and its many-layer trace argument. Halving the couplings on \(S\) gives exactly the moment in (5) as a ratio of unnormalized partition functions. Take a direction of this orientation as time. Halving the coupling decreases the normalized electric convolution on the marked edges of layer \(i\) in positive-operator order. Its spin-\(j\) multiplier \(I_{2j+1}(\beta)/I_1(\beta)\) is nondecreasing in \(\beta\) by the neighboring Bessel ratio ordering proved there. The other electric factors, the magnetic half-weights and the gauge projection preserve the comparison \(0\le F_i\le F\) of the individual sandwiches. At period \(h\), trace Hölder and min–max give \(\lvert\operatorname{Tr}\prod_i F_i\rvert\le\prod_i(\operatorname{Tr} F_i^h)^{1/h}\le\operatorname{Tr}F^h\). Restoring the scalar normalization gives the first bound. The Haar integral has upper bound \(C(1+b)^{-3/2}\) by the radial estimate immediately below and lower bound \(c(1+b)^{-3/2}\) by the ball of radius \((1+b)^{-1/2}\) about one. These prove the second bound. The argument also holds with other homogeneous, nonnegative orientation couplings. [Normalized convolution ordering and trace comparison](gap-solve4-astra62.md) · [Single-plaquette version](gap-solve6-astra62.md)

**PROVED.** Fix a false pairing relative to the actual lift at each \(p\in D\). It exchanges a proper nonempty subset of the four links. The membership bit changes at some corner of the face, so a mixed plaquette word arrives at one lifted vertex and departs from its other lift. Randomize the gauge at one of these two vertices by independent normalized Haar \(h\). The actual two plaquette actions are gauge invariant. In the first mixed word the variable \(h\) or \(h^{-1}\) occurs exactly once, between fixed group elements, because the four base vertices are distinct. Its mixed holonomy is therefore Haar for every initial field. The chosen gauge variables belong to disjoint base faces and can be averaged independently. This works also for faces crossing the seam in the connected cover.

**PROVED.** Set \(u=1/2\). Bound the indicator that all selected false weights exceed or equal the true ones by the product of their ratios to the power \(u\). In each numerator retain the first mixed plaquette weight and use \(w^u\le1\) on the second. Gauge invariance of the actual Wilson law and the preceding Haar average give the factor \(J(u\beta)^{|D|}\), where
\[
 J(b)=\int e^{-b a(g)}\,dg
 =\frac2\pi\int_0^\pi e^{-b(1-\cos\theta)}\sin^2\theta\,d\theta
 \le C_1(1+b)^{-3/2}.
\]
Indeed \(\sin^2\theta\le\theta^2\) and \(1-\cos\theta\ge2\theta^2/\pi^2\) on this interval, and \(J(0)=1\). The product of the reciprocal true weights to power \(u\) has expectation bounded by \(C_0^{2|D|}\), by (5) for the \(2|D|\) lifted faces. On the split cover apply (5) on its two independent tori. There are seven alternative pairings modulo complement on each face. Summing proves (4).

## The probability of confusing the two covers

**PROVED (determining the cover from unordered link pairs).** Let \(\nu_c\) be the law of the unordered pairs under the normalized Wilson measure on cover \(c\). There is a single decision rule \(d\) on these observations and there are positive numerical \(b,\beta_0,n_0\) such that for \(n\ge n_0\), \(T=n/2\), \(\beta\ge\beta_0\),
\[
 \nu_0(d=1)+\nu_1(d=0)\ \le\ 2e^{-b n^3\log(2+\beta)}.                \tag{6}
\]
All assertions about probabilities integrate the Wilson fields. Gauge frames at the two lifts of a vertex are free in these integrals.

**PROVED.** In each of the \(n^2\) planes of orientation \((t,1)\) at fixed \(x_2,x_3\), order the two observed values on each link by a fixed Borel order on the unit quaternions. For each square \(p\) choose bits \(s_{pe}\) giving a largest \(W_p(s;x)\), using a fixed tie convention. On the nearest-neighbour graph of square centres put \(y_{pq}=s_{pe}+s_{qe}\) on its bond crossing the common link \(e\). All cochains in this paragraph and the next are mod two. The true values, calculated with the actual lifts, give a flat cochain \(a^c_{pq}=\alpha^c_{pe}+\alpha^c_{qe}\). Its time holonomy is \(c\) and its space holonomy is zero. Indeed this sum transports a sheet label from one square centre across the common link to the next centre. It has no change around a square enclosing a base vertex, and one traversal of time ends in the other sheet precisely for \(c=1\). Changing the link order adds the same bit to both incidents and cancels. A change of the chosen lift of a square adds a vertex coboundary. On an unambiguous square the maximizing assignment agrees with the actual one up to its common flip and the link reorderings. Choose the square flips to realize this agreement there and arbitrarily on the ambiguous squares. This gives a representative \(a\) of the true flat class such that every bond with \(y\ne a\) meets an ambiguous square centre.

**PROVED.** Among all flat cochains on this plane choose one \(z\) with smallest Hamming distance to \(y\), allowing both holonomies to vary and resolving ties lexicographically in a fixed bond order. Take its time holonomy as the plane's decision. If it is wrong, the bonds where \(z\ne a\), drawn as dual edges, have even degree at every dual vertex by flatness. They decompose into edge-disjoint simple cycles by cutting closed walks at repeats. Odd intersection with a time circle forces at least one cycle \(\gamma\) with odd spatial winding, of length \(k\ge n\). Flipping \(z\) on bonds crossed by this cycle alone preserves flatness. Minimality then gives at least \(k/2\) crossed bonds with \(y\ne a\), since on the cycle exactly one of \(a,z\) agrees with \(y\) on each bond. Those bonds touch at least \(k/8\) distinct ambiguous square centres, since a square has four neighbours. Among them at least \(k/72\) have mutually vertex-disjoint base squares. Greedily choosing a square deletes at most the nine squares in its \(3\)-by-\(3\) neighbourhood. Distinct planes in use here do not share base vertices.

**PROVED.** For a specified cycle the candidate centres form a set of at most \(2k\) sites, so a union bound and (4) give at most \(4^k q_\beta^{k/72}\) for the needed subset. There are at most \(nT\,4^k\) walks of length \(k\) with an assigned start. The same count can be multiplied for any selected set of planes because (4) applies to the union of the disjoint squares selected on all the cycles, without an independence assumption on Wilson plaquettes. Consequently the probability of errors on each of \(m\) specified planes is at most
\[
 \left[nT\sum_{k\ge n}(16q_\beta^{1/72})^k\right]^m.                   \tag{7}
\]
For all sufficiently large \(\beta\), \(16q_\beta^{1/72}\le(2+\beta)^{-b_1}\) for one \(b_1>0\), by (4). The factor \(nT\) and the geometric denominator are absorbed by decreasing \(b_1\) and increasing \(n_0\). Use the majority of the \(n^2\) decisions. An error needs at least \(n^2/2\) erroneous planes, and the choices of planes cost at most \(2^{n^2}\). This proves (6) on both covers. The minimization is a definition of a finite observable. The finite contour argument proves its error estimate for every allowed size.

**PROVED (the size of the common part).** For the event \(G\) of (3) there are numerical \(0<b'<B'<\infty\) such that at all sufficiently large \(n,\beta\), on both covers,
\[
 e^{-B'n^3\log(2+\beta)}
 \ \le\ \mathbb P_c(G)
 \le e^{-b'n^3\log(2+\beta)}.                                           \tag{8}
\]
For the lower bound on the split cover, take the seam between \(T-1\) and 0. At most \(7n^3\) base links occur in its \(3n^3\) temporal plaquettes (the two spatial slices and the intervening temporal links). Partition SU(2) into at most \(C r^{-3}\) cells of diameter at most \(r=(1+\beta)^{-1}\). A maximal \(r/2\)-separated net suffices because the disjoint \(r/4\)-balls have Haar volume at least \(c r^3\). The two independent histories have identical marginal laws on this set of seam links. The probability that their cell words coincide is \(\sum_j p_j^2\ge1/\#\{j\}\), hence at least \((C r^{-3})^{-7n^3}\). On a coincidence, mixing the two sheets on any seam plaquette changes each of its holonomies by round distance at most \(4r\), by the bi-invariant triangle inequality. The action \(a\) is 1-Lipschitz. Thus \(m_p/W_p\ge e^{-8\beta r}\), and by (2) the conditional chance of leaving every seam face unselected is at least \(e^{-24n^3}\). All other plaquettes admit the ordinary sheet labelling. This gives \(G\) and the asserted lower bound. Since \(Z_0/Z_1=z_T^2/z_{2T}\ge1\), (3) gives the lower bound for the connected cover too.

**PROVED.** For the upper bound, a specified set of vertex-disjoint faces of one orientation can all be unselected with probability at most \(q_\beta^{|D|}\). Indeed in (2) each ratio is at most \((W_p(\text{one fixed false pairing})/W_p(\text{true pairing}))^u\), since the minimum includes both and \(0<u<1\). Independence conditional on the fields and the Haar average in (4) give the assertion. If \(G\) holds, the time-odd cochain of the connected cover on any one of the preceding planes is a coboundary on all edges between selected square centres. This follows by adding the two incidence equations defining \(G\) at the shared link. Use row 1131's dual-barrier argument, now simultaneously in every parallel plane and for the joint estimate on either cover. Extend the square bits arbitrarily over the unselected squares and subtract their coboundary on the whole plane. The remaining closed cochain has odd time period. Its dual contains a cycle of spatial winding and length \(k\ge n\), all of whose edges meet an unselected square on the primal graph. At least \(k/4\) distinct unselected squares, and hence \(k/36\) vertex-disjoint ones, are available. Applying the count of (7) on all \(n^2\) planes bounds the probability under either Wilson law by the upper bound in (8).

**PROVED (optimal overlap for the raw observations).** Let
\(\mathcal O=\int\min(d\nu_0,d\nu_1)\), with densities taken against \(\nu_0+\nu_1\). The error probability for the best equal-prior decision between the covers is \(\mathcal O/2\), obtained by choosing the larger of the two densities at each observation. In particular \(\mathcal O\le\nu_0(d=1)+\nu_1(d=0)\). The field swaps in the proof of (3) preserve every unordered link pair. Integrating on \(G\) therefore gives the same *measure on the observations*, of mass \(Z_0\mathbb P_0(G)\), under the two unnormalized covers. Dividing by \(Z_0\) gives a measure dominated by both \(\nu_0\) and \(\nu_1\), since \(Z_1\le Z_0\). Together with (6) and (8),
\[
 -\log\mathcal O=\Theta\!\big(n^3\log(2+\beta)\big).                    \tag{9}
\]
This also bounds every positive matching that can change the assignment of sheet labels arbitrarily while preserving each unordered raw pair. Such a matching has common mass at most \(Z_0\mathcal O\). The explicit matching on \(G\) attains the order of the exponent. This excludes the large common fraction needed for the matching test, including nonlocal choices of the swaps that obey this preservation requirement.

## A thin strip and the relative weights

**PROVED (a strip suffices).** Use only \(w\) consecutive columns of face centres in one \((t,1)\)-plane, with all \(T\) times, \(3\le w<n\). Minimize Hamming distance over flat cochains on this cylinder, imposing flatness only on its elementary squares. If the resulting time holonomy is wrong, the difference from the true representative is dual to a collection containing a path between the two spatial boundaries. To see this, give each dual edge at the edge of the cylinder an endpoint on its boundary. The interior vertices have even degree, and each boundary has an odd number of endpoints since the true and estimated periods differ on its time circle. Wiring each boundary separately gives a path between the two odd vertices. Keeping it simple, its length \(k\) is at least \(w-1\). Flipping this path alone preserves every flatness constraint. The minimal-distance and disjoint-square arguments leading to (7) give
\[
 \mathbb P_c(\text{wrong period on the strip})
 \le C wT\sum_{k\ge w-1}(16q_\beta^{1/72})^k.                           \tag{10}
\]
There are at most \(CwT\,4^k\) paths because the starting boundary edge has at most \(T\) choices and all interior degrees are at most four. In particular for any fixed \(p>0\) the error is \(O(n^{-p})\) using
\(w=3+\lceil C_p\log(2+n)/\log(2+\beta)\rceil\) on the large-\(\beta\) range of (7). This reads only the links bounding the strip.

**PROVED (fixed angular resolution).** A single finite partition of SU(2), independent of the cutoff, suffices if \(w=3+\lceil C_p\log(2+n)\rceil\). Report on each link the unordered pair of its cell indices. Replace each element by a representative within distance \(\delta\), then compute the same decision. Each sum \(A\) of the two plaquette actions changes by at most \(8\delta\). A falsely preferred pairing therefore has \(A_{\rm false}\le A_{\rm true}+\varepsilon\), with \(\varepsilon=16\delta\). On faces where \(A_{\rm true}\le\varepsilon\), this requires the first mixed plaquette alone to have action at most \(2\varepsilon\). Haar measure of that cap is at most \(C\varepsilon^{3/2}\), by the spherical integral used in (4). For a prescribed set \(R\) of vertex-disjoint faces of one orientation with \(A_{\rm true}>\varepsilon\) at each, (5) gives probability at most
\([C_0^2 e^{-\beta\varepsilon/2}]^{|R|}\). Gauge averaging at the smooth faces leaves the rough-face event unchanged. Splitting the set of disjoint faces by \(R\) and summing the seven alternatives, the joint error bound is as in (4) with
\[
 q=7\big[C\varepsilon^{3/2}+C_0^2e^{-\beta\varepsilon/2}\big].
\]
Choose \(\delta>0\) small, then \(\beta_0\) large, to make \(16 q^{1/72}\le1/2\) for \(\beta\ge\beta_0\). A finite partition with the stated resolution exists by compactness. Equation (10) now proves the claim. In physical units at fixed side \(L\), the width is \(O(L\log n/n)\) and the observation uses \(O(n\log n)\) unordered pairs of finite-valued readings.

**PROVED (a single positive measure).** Here is a way to ask for the missing relative weight without providing the decision rule a sheet label. Put a bit \(b_e\) on each base link. Sum with counting measure over flat bit fields with zero periods in the three spatial directions, letting the time period vary. Make a cover from \(b\) by sending \((v,i)\) along \(e=vv'\) to \((v',i+b_e)\). Attach the two raw group variables to the two forward lifts of each link. Flatness closes each lifted elementary plaquette. Integrate the product of ordinary Wilson plaquette weights for this cover, then normalize the entire sum once. Denote the resulting probability by \(\mathbb Q\), and let \(Y=(-1)^{\oint_t b}\). Any two bit fields with the same four periods differ by a vertex gradient. Integrating their difference from a root defines the vertex function because flatness and the vanishing periods give path independence. Each choice of the time period therefore has exactly \(2^{V-1}\) assignments, \(V=n^3T\). Relabelling the two sheets at vertices acts on the link pair by a permutation at its tail and preserves its unordered values. Conditional on the time period \(c\), the law of the observations is thus \(\nu_c\), and
\[
 \mathbb E_{\mathbb Q}Y=\frac{Z_0-Z_1}{Z_0+Z_1}.                        \tag{11}
\]
Only the common Wilson weights and local flatness with the prescribed spatial periods define this measure.

**PROVED (what the strip measures).** Write \(D=(-1)^{d_{\rm strip}}\) for the fixed-resolution decision on the strip. By (10), \(\lvert\mathbb E_{\mathbb Q}D-\mathbb E_{\mathbb Q}Y\rvert=O(n^{-p})\), uniformly in the sector weights. For a trajectory with \(\beta_j\to\infty\), (1) is therefore equivalent at the same \(L\) to
\[
 \limsup_j\mathbb E_{\mathbb Q_j}D<1/3301.                              \tag{12}
\]
Indeed \(r\mapsto(r-1)/(r+1)\) takes \(1651/1650\) to \(1/3301\) and has continuous inverse near that value. Row 1321 already relates the mean of a replica closing sign to the thermal ratio. The additional conclusions here are the original-plaquette decision, its fixed-resolution thin strip, and the sharp common-mass cost (9). Accuracy conditional on either cover does not fix the mean in (12).

## Integrating the independent vertex gauges

**PROVED (why the decision uses gauge frames).** On the ordered variables of the split cover, an observable invariant under both independent vertex gauges and an arbitrary swap of the pair on each individual link is constant. More generally partition the base links into blocks and allow an independent whole-block swap on each. The common invariants are functions of the unordered pair of gauge orbits *of each block separately*, where each block has its own copies of its vertex gauges.

**PROVED.** At a vertex \(v\), apply gauge \(h\) on sheet zero, then compose with the inverse of its conjugate by the swap of block \(B\). All incident transformations outside \(B\) cancel. On the incidences of \(B\) this generates the pair of ordinary gauge transformations \((h,h^{-1})\) at \(v\). These pairs generate \(SU(2)\times SU(2)\). Indeed products with \(h=g,k,(gk)^{-1}\) give \((1,g^{-1}k^{-1}gk)\). To express any element of SU(2) as a commutator, conjugate it to a diagonal element \(d\), choose a diagonal square root \(g\) of \(d^{-1}\), and take a Weyl element \(k\) inverting the diagonal subgroup. Then \(g^{-1}k^{-1}gk=g^{-2}=d\). The first factor is generated as well. Thus each block has independent local gauges on both sheets. The converse follows because an ordinary vertex gauge restricts to such gauges on every block. The compact group orbits give the asserted measurable quotient (one can fix a spanning tree in each connected block component, leaving simultaneous conjugation at its root). On a one-link block either sheet can take any group value by a change at an end, so its quotient is a point. For invariance understood in \(L^2\) of product Haar the same conclusion follows by averaging over the generated compact group. The Wilson densities at finite coupling are strictly positive. This locates the observable in (12) in the enlarged positive integral. Its definition needs the two gauge frames.

**GUIDE.** Row 1131 identifies integrating relative gauge frames as a possible escape from its one-plane obstruction. I next test a direct lower bound for the crossed seam *after all temporal links on that seam have been integrated out*. This is an actual one-step Wilson integral. Row 1330, (29), concerns a different kernel at a heat-flow midpoint. Its spanning-tree estimate for frame integrals is useful here. [Gauge-frame bound in row 1330](gap-solve42-astra62.md)

**PROVED (the integrated seam at equal elementary plaquette actions).** Let \(V_3=n^3\), and let \(x,y\) be two spatial configurations. Write the temporal part of the gauge-projected one-step kernel as
\[
 J_\beta(x,y)=\int_{SU(2)^{V_3}}
  \exp\!\left[-\beta\sum_{e=vv'}a\!\left(x_e^{-1}g_v y_e g_{v'}^{-1}\right)\right]\,dg .
\]
It is symmetric by inverting the frames and using invariance of the action under inversion and conjugation. In a split pair the pre- and post-seam arrays \((x,y)\), \((x,y)\) give \(J_\beta(x,x)J_\beta(y,y)\). Crossing the seam gives \(J_\beta(x,y)^2\). All spatial half-weights cancel in this quotient. For all sufficiently large \(\beta\) and even \(n\ge C\beta^{1/4}\) there are \(x,y\) for which **every oriented elementary spatial plaquette in both fields** has \(\beta a=3/4\), yet
\[
 c\,V_3\sqrt\beta\ \le
 -\log\frac{J_\beta(x,y)^2}{J_\beta(x,x)J_\beta(y,y)}
 \ \le\ C\,V_3\sqrt\beta.                                                \tag{13}
\]
Taking \(y=x\) gives ratio one with the identical list of elementary plaquette actions. Thus even the complete list of those actions cannot specify the logarithm of the sewn weight uniformly to \(o(V_3\sqrt\beta)\).

**PROVED (fields and loops).** Use an Abelian circle \(s\mapsto e^{\mathbf i s}\) of unit quaternions. Choose \(\theta\in(0,\pi)\) by \(1-\cos\theta=3/(4\beta)\). Let \(k\) be the largest even integer at most \(\theta^{-1/2}\). Then \(1/4\le k^2\theta\le1\) for large \(\beta\), and \(k\asymp\beta^{1/4}\). Assume \(n\ge8k\). On the cyclic first coordinate construct an integer function \(F\), starting at zero. In each full block of length \(4k\) take \(2k\) successive increments \(+1\), then \(2k\) increments \(-1\). Fill the even remainder by alternating \(+1,-1\). This is periodic and \(0\le F\le2k\). Put \(P(j)=j\bmod 2\) with values 0 and 1. At spatial site \(z\), the forward links of \(x\) are
\[
 1,\quad e^{\mathbf i\theta F(z_1)},\quad
 e^{\mathbf i\theta(P(z_1)+P(z_2))}.
\]
Use the same links for \(y\) with \(F\) replaced by \(P\). Each plaquette in either field has flux \(+\theta\) or \(-\theta\), by taking the corresponding forward differences. This proves the assertion about every elementary action.

**PROVED.** At a fixed positive fraction of all anchors, the entire interval of \(k\) first-coordinate increments lies in a rising run of \(F\) because each full block contributes at least \(k\) starts and there are at least \(n/(8k)\) blocks. The \(k\)-by-\(k\) square in plane \(12\) based there has \(x\)-holonomy \(e^{\mathbf i k^2\theta}\). Its \(y\)-holonomy is the identity because \(k\) is even. This remains the identity in every vertex gauge. Set \(\ell_e=d(x_e,g_vy_e g_{v'}^{-1})\) in round distance. Bi-invariance and the triangle inequality for the two loop products give \(\sum_{e\in\partial R}\ell_e\ge k^2\theta\ge1/4\) for every such square. Hence \(\sum_{\partial R}\ell_e^2\ge c/k\). A spatial edge can lie on at most \(2k\) of their perimeters. Summing and using \(a\ge 2d(1,\cdot)^2/\pi^2\) proves
\[
 \sum_e a(x_e^{-1}g_vy_eg_{v'}^{-1})\ge c\,V_3/k^2\quad\text{for every }g. \tag{14}
\]

**PROVED (frame integration).** Use half the exponent in \(J_\beta(x,y)\) to pay (14). In the other half drop all edges outside a spanning tree. Integration of each leaf frame gives the same \(J(\beta/2)\) as in (4), so the remaining integral is at most \((C\beta^{-3/2})^{V_3-1}\). Each diagonal kernel is at least \((c\beta^{-3/2})^{V_3}e^{-C V_3}\) by restricting all frames to distance \(\beta^{-1/2}\) from one. Consequently the log of the ratio in (13) is at most \(-c\beta V_3/k^2+C V_3+3\log(1+\beta)\), which gives its stated suppression. For the converse, \(d(x_e,y_e)\le (2k+1)\theta\le C/k\). The same frame restriction gives \(J_\beta(x,y)\ge(c\beta^{-3/2})^{V_3}\exp[-C V_3(1+\beta/k^2)]\). Both diagonal kernels are at most one. Since \(\beta/k^2\asymp\sqrt\beta\), these estimates prove (13) in both directions. Continuity gives positive-volume neighbourhoods violating any proposed uniform order-one lower bound in an open elementary-action window about \(3/4\). Their Wilson probability in the physical limit remains to be estimated.

## Restricting the seam integral using Wilson loops

**PROVED (a restriction in the actual integrated law).** Write \(\overline a_{r,s}^{ij}(x)\) for the average of \(a(U_{\partial R})\) over the \(V_3\) translates of a spatial \(r\)-by-\(s\) rectangle in plane \(ij\). Put \(K_\beta=[\log(2+\beta)]^4\). At each of the four spatial end slices involved in sewing the two histories, impose
\[
 \beta\,\overline a_{r,s}^{ij}\le K_\beta\,rs
 \quad(ij=12,13,23;\ r,s\text{ powers of two},\ 1\le r,s<n).            \tag{15}
\]
This changes \(\log Z_0-\log Z_1\) by \(o(1)\) as \(\beta\to\infty\), on the physical boxes. In fact row 1171, (4), gives \(\beta\,\mathbb E a(U_{\partial R})\le C rs\) for rectangles shorter than their periods. It uses the reflection-positivity argument of Constantin Bachas and the finite-period open-line transfer calculation of row 1153. The spatial directions can each serve as the transfer direction. It follows by Markov's inequality and translation invariance that each test fails with probability at most \(C/K_\beta\) under either true closing. For \(K_\beta rs\ge2\beta\) the test is automatic. There are \(O(\log^2(2+\beta))\) remaining dyadic shapes and a fixed number of slices and orientations. The deleted probability on each cover is \(O(1/\log^2(2+\beta))\). Taking the difference of the two log survival probabilities gives the claim. In particular the first choice of fields in (13) need not be representative. [Rectangle bound](gap-solve14-astra62.md) · [Its check](gap-solve14-check-opus.md) · [Finite-period strip bound](gap-solve6-astra62.md)

**PROVED (residual mismatch inside the restriction).** Suppose \(n/\sqrt\beta\to\infty\) and \(\beta\to\infty\). There are two fields with every elementary \(\beta a=3/4\), satisfying (15) with slack even **pointwise at each rectangle and for all integer side lengths** \(1\le r,s<n\), for which
\[
 -\log\frac{J_\beta(x,y)^2}{J_\beta(x,x)J_\beta(y,y)}
             =\Theta(V_3 K_\beta).                                     \tag{16}
\]
To construct them choose \(k\) even with \(k\asymp c_*\sqrt{K_\beta}\), with a sufficiently small fixed \(c_*>0\) chosen below. Use the same \(F,P,\theta\) as above, with this new \(k\), and write \(\Delta F(j)=F(j+1)-F(j)\). The forward links are now
\[
 x_1=1,\qquad x_2=e^{\mathbf i\theta F(z_1)\Delta F(z_2)},\qquad
 x_3=e^{\mathbf i\theta(P(z_1)+P(z_2))\Delta P(z_3)} .
\]
For \(y\) replace both occurrences of \(F\) by \(P\). The flux of any \(12\) rectangle of sides \(r,s\) is the product
\(\theta[F(z_1+r)-F(z_1)][F(z_2+s)-F(z_2)]\). The other planes give the corresponding product with \(P\). For \(y\) all three use \(P\). Every elementary flux has magnitude \(\theta\). Since \(|F(j+r)-F(j)|\le\min(r,2k)\), \(\min(r,2k)^2\le 2kr\), and \(\beta\theta^2\le C\), the pointwise value of \(\beta a(U_{\partial R})\) is at most \(C k^2rs\). Choose \(c_*\) so this is at most \(K_\beta rs/2\).

**PROVED.** A fixed positive fraction of the \(k\)-square anchors now have \(k\) rising increments in both directions. There the \(x\)-holonomy has angle \(k^2\theta\), tending to zero, and the \(y\)-holonomy is one. Keeping the actual square of that angle in the perimeter argument gives \(\sum_e a(x_e^{-1}g_vy_e g_{v'}^{-1})\ge c V_3 k^2\theta^2\) for every \(g\). Tree integration as in (14) bounds the negative log ratio below by \(c V_3 k^2-C V_3-3\log(1+\beta)\). Conversely \(d(x_e,y_e)\le Ck\theta\). Restricting the mixed frames to the small balls and keeping a spanning tree for each *diagonal upper bound* gives the upper bound \(C V_3(1+k^2)+3\log(1+\beta)\). These prove (16), since \(k^2\asymp K_\beta\). Thus the restriction which costs \(o(1)\) in the physical trace still does not justify discarding the relative gauge-integrated sewing weight pointwise. Estimating the contribution of such fields to the normalized integral requires their probability as well.

## The mean cost after integrating the seam

**PROVED (an estimate for the interacting slices).** Let \(X,Y\) have the spatial-slice marginals of the isotropic periodic Wilson histories at either of the two periods, with arbitrary coupling of the marginals. Suppose \(\beta\ge2\) and all periods exceed \(C_2\sqrt\beta\), with \(C_2\) a sufficiently large numerical constant. For
\[
 d_*(X,Y)=\min_g\sum_{e=vv'}a(X_e^{-1}g_vY_eg_{v'}^{-1}),\qquad
 L_\beta(X,Y)=-\log\frac{J_\beta(X,Y)}
                     {\sqrt{J_\beta(X,X)J_\beta(Y,Y)}},
\]
one has
\[
 \mathbb E\,\beta d_*(X,Y)\le C V_3\log^3(2+\beta),\qquad
 0\le L_\beta(X,Y),\qquad
 \mathbb E L_\beta(X,Y)\le C V_3\log^3(2+\beta).                       \tag{17}
\]
The frame construction used here is that of row 1171, (5)–(8), with its original adjoint representation changed to left multiplication on the unit quaternions. The squared variation estimate below saves one logarithm in this application. The rectangle moment is the existing Wilson input of that row.

**PROVED (fundamental frames).** In one such four-dimensional history let \(T_{vw}q=U_{vw}q\) on \(\mathbb R^4=\mathbb H\). Choose \(b\) the largest dyadic integer at most \(\sqrt\beta\). Use the unnormalized row maps \(D_l(v)=C^{[l]}(v)\) of [row 1171, (6)–(7)](gap-solve14-astra62.md), built separately for dyadic \(l\le b\), with four rows. Here are the precise inputs from that construction, with \(s_l(v)\) the least row singular value. For a bond \(e=vw\),
\[
 \|D_l(v)-T_{vw}D_l(w)\|_{\rm F}\le C/l+E_l(e),\quad
 \mathbb E E_l(e)^2\le C\log^2(2l)/\beta,\qquad
 \Pr(s_l(v)<2\gamma)\le C l^2/\beta                                  \tag{18}
\]
for a fixed \(\gamma>0\). To verify the change of representation, its transport around a rectangle is \(L_H:q\mapsto Hq\), with \(\|L_H-I\|_{\rm F}=2|H-1|\). Thus the rectangle-interchange error in the dyadic recursion is \(O(r/\sqrt\beta)\) in \(L^2\) at scale \(r\), by row 1171, (4). The coincident half of the parents and the straight comparison of the other half are unchanged. The coefficient of this error at unit scale is \(1/r\), giving the first two bounds. For the last bound the reference block row at endpoint \(z\) is \(w_z T(v,z)\) with the deterministic weights of that construction. Its row covariance is \((\sum_z w_z^2)I_4\), bounded below by \(cI_4\) by the same support count and Cauchy–Schwarz. Sorting the transported paths to coordinate order uses a bounded number of rectangles per scale at cost \(Cr/\sqrt\beta\), summing geometrically to \(Cl/\sqrt\beta\). The sum of squared block errors is bounded in mean by \(Cl^2/\beta\) because \(\sum_z w_z^2\le1\). The Lipschitz inequality for the least singular value gives (18). These arguments use only orthogonality and the indicated rectangle bound on the original torus.

**PROVED (squared variation).** As in row 1171, let \(\alpha(s)\) rise linearly from 0 at \(\gamma\) to \(\pi/2\) at \(2\gamma\), constant outside. Set \(t_l(v)=\cos\alpha(s_l(v))\) and \(B_l(v)=\sin\alpha(s_l(v))(D_lD_l^{\mathsf T})^{-1/2}D_l\), with \(B_l=0\) below the cutoff. Stack column blocks \(F_l=[B_l,t_l F_{l/2}]\), starting with the isometric \(F_1=D_1\). Then \(F_lF_l^{\mathsf T}=I_4\). Both \(B_l\) and \(t_l\) are uniformly Lipschitz on contractions in Frobenius norm. For \(s\ge\gamma\) this follows from the resolvent formula for the inverse square root on matrices bounded below by \(\gamma^2 I\), and at the threshold the vanishing sine absorbs the difference. The construction commutes with orthogonal transport on the left. Write \(H_l(e)=\|F_l(v)-T_{vw}F_l(w)\|_{\rm F}^2\). For two row isometries \(A,B\) with four rows,
\[
 \|tA-uB\|_{\rm F}^2=4(t-u)^2+tu\|A-B\|_{\rm F}^2 .
\]
The orthogonal column blocks therefore give
\[
 H_l(e)\le C\,[l^{-2}+E_l(e)^2]+t_l(v)t_l(w)H_{l/2}(e).
\]
In the iteration the coefficient of \(l^{-2}\) at every \(l<b\) vanishes unless \(s_{2l}(v)<2\gamma\). Its mean contribution is at most \(C/\beta\) by (18), which also bounds the contribution of the bottom term. The error squares sum without taking square roots. Thus
\(\mathbb E H_b\le C b^{-2}+C\beta^{-1}\sum_{l=1,2,4,\ldots,b}(1+\log^2(2l))
\le C[b^{-2}+\beta^{-1}\log^3(2b)]\).

**PROVED.** With independent standard Gaussian coordinates \(\xi\) in the column space put \(h_v=F_b(v)\xi/|F_b(v)\xi|\in SU(2)\). Given the links \(F_b(v)\xi\) is standard in \(\mathbb R^4\). For any two such row isometries \(A,B\), decompose \((A-B)\xi\) into its part determined by \(A\xi\) and the independent Gaussian part from \(I-A^{\mathsf T}A\). The former has squared norm at most \(\|A-B\|_{\rm F}^2|A\xi|^2\), the latter has mean square at most \(\|A-B\|_{\rm F}^2\), and \(\mathbb E|A\xi|^{-2}<\infty\) by the four-dimensional radial integral. Normalization changes the difference by at most \(2|(A-B)\xi|/|A\xi|\). Hence \(\mathbb E|h_v-U_e h_w|^2\le C\mathbb E H_b(e)\). Apply this to each marginal history. In the minimum defining \(d_*\) choose \(g_v=h_v^X(h_v^Y)^{-1}\). The sum of the two frame errors bounds the chord mismatch at each edge. The construction may be sampled conditionally on each slice if only its marginal coupling is given. Squaring, summing and using \(b\asymp\sqrt\beta\) proves the first bound in (17). No invariance of the Wilson measure under a field-dependent change of variables is required.

**PROVED.** The one-step electric convolution and its gauge projection are positive semidefinite by GL3. Approximating point evaluations by normalized balls in the continuous kernel gives \(J_\beta(X,Y)^2\le J_\beta(X,X)J_\beta(Y,Y)\). For an upper bound on \(L_\beta\), restrict the frames to balls of radius \(\beta^{-1/2}\) about a minimizing frame, which exists by compactness. The perturbed sum of actions is at most \(2d_*+CV_3/\beta\), by the chord triangle inequality and \(a(u^{-1}v)=|u-v|^2/2\). Use the tree upper bound \(J(\beta)^{V_3-1}\) on either diagonal. This gives \(L_\beta\le2\beta d_*+CV_3+C\log(2+\beta)\), proving (17).

**PROVED (independent slices still cost volume in the minimizing action).** For slices \(X,Y\) of two independent ordinary Wilson histories on these boxes,
\[
 \Pr\{\beta d_*(X,Y)<cV_3\}\le e^{-c' V_3}                             \tag{17a}
\]
at sufficiently large \(n,\beta\). This concerns the action before the frame integral and applies, for example, to a crossed pair of ends under the split law. Row 1141 uses local holonomy defects to constrain adjoint frames on a single field. Here the test compares gauge-invariant plaquette radii of the two independent fields. [Earlier single-field estimate](gap-crux2-astra62.md)

**PROVED.** Choose \(M\ge c_1V_3\) spatial \(12\)-plaquettes with their anchors at pairwise periodic supremum distance at least four. Greedy selection removes at most \(7^3\) anchors at each choice. Designate their lower forward \(1\)-edges. No plaquette in the four-dimensional action contains two designated edges. Put \(r_p(U)=\sqrt\beta\,|1-U_p|\). With probability at least \(1-e^{-c_2 M}\), at least \(M/2\) of the \(Y\) readings are at most a fixed \(K\). Indeed \(r_p^2=2\beta a(U_p)\), so (5) and exponential Markov give the exceptional bound \([C_0 e^{-K^2/8}]^M\). Choose \(K\) large first.

**PROVED.** Given \(Y\) and all but the designated \(X\)-edges, the latter have independent conditional densities. Each is proportional to \(\exp(t\langle u,h\rangle)\) for some unit quaternion \(h\) and \(0\le t\le6\beta\), since the six incident plaquettes supply linear functions of \(u\) on the unit sphere. Consequently the density relative to Haar is bounded by \(1/J(t)\le C(1+\beta)^{3/2}\). The holonomy on the selected face differs from that edge by fixed multiplications and possibly inversion. Under Haar the chord \(q=|1-u|\) has density \((2/\pi)q^2\sqrt{1-q^2/4}\) on \([0,2]\), by \(q=2\sin(\theta/2)\). For any \(r_p(Y)\le K\), this bounds the conditional probability of \(|r_p(X)-r_p(Y)|\le\delta\) by \(C(K+1)^2\delta\), for \(0<\delta\le1\), uniformly over the exterior. Choose \(\delta\) so the bound is at most \(2^{-12}\). Among the \(M/2\) or more eligible faces, the chance that at least \(M/4\) match is bounded by \(2^M(2^{-12})^{M/4}\). Thus outside an exponentially small event, at least \(M/4\) radii differ by more than \(\delta\). For every gauge \(g\) the difference of their two chord radii is bounded by the sum of the four link chord mismatches, by conjugation invariance and the product triangle inequality. Squaring and summing over these edge-disjoint faces gives \(\beta d_*(X,Y)\ge c_3 M\). This proves (17a). The entropic terms in \(J_\beta\) are essential when passing from this action statement to a statement about normalized weights.

**PROVED (relative entropy before and after seam integration).** On the ordered raw variables write \(\mu_c=f_c\,dx/Z_c\). Let \(\mu_c^*\) be the marginal obtained by integrating the two crossing temporal links at every spatial site, keeping all the other variables. On the boxes of (17) the symmetrized relative entropies satisfy
\[
 \begin{aligned}
 D(\mu_0\Vert\mu_1)+D(\mu_1\Vert\mu_0)&=12\beta V_3+O(V_3),\\
 D(\mu_0^*\Vert\mu_1^*)+D(\mu_1^*\Vert\mu_0^*)&\le C V_3\log^3(2+\beta).
 \end{aligned}                                                          \tag{19}
\]
Use the canonical seam labels. Exactly \(6V_3\) lifted plaquettes differ in the two evaluations. For each, the wrong word uses the other sheet's spatial edge at the upper end and therefore has zero expected trace in the true measure, by a single unmatched Haar gauge rotation at a corner. The mean of the normalized true trace is \(1-O(1/\beta)\) by the one-plaquette input to row 1171, (4). Thus the expectations of the *unnormalized* log density ratio \(\log(f_0/f_1)\) are \(6\beta V_3+O(V_3)\) on cover zero and \(-6\beta V_3+O(V_3)\) on cover one. Their difference cancels the log normalizers and proves the first line. The entropy here compares the ordered raw histories. Equation (9) measures the overlap after projecting to unordered link pairs.

**PROVED.** After integration let \(x_0,x_1\) denote the pre-seam arrays and \(y_0,y_1\) the post-seam arrays in the fixed order. All other weights agree in the two unnormalized densities. The four diagonal normalizers in \(L_\beta\) cancel to give their exact log ratio
\[
 B=L_\beta(x_0,y_1)+L_\beta(x_1,y_0)
           -L_\beta(x_0,y_0)-L_\beta(x_1,y_1).                          \tag{20}
\]
Each array has a true Wilson slice marginal under either closing. Equation (17) therefore bounds \(\mathbb E_c|B|\) by \(C V_3\log^3(2+\beta)\) on each. Subtracting its two expectations proves the second line of (19). This is an integrated gain from doing the gauge integral. The normalizers which contain the thermal defect cancel in the symmetric relative entropy.

**PROVED (a further restriction and the missing number).** Let \(\mathcal A\) require (15) on the four ends and require all four \(L_\beta\)'s in (20) to be at most \(V_3[\log(2+\beta)]^{7/2}\). On either normalized cover, (15), (17) and Markov's inequality give \(\mu_c^*(\mathcal A)=1-O([\log(2+\beta)]^{-1/2})\). This also removes the configurations in (16), at vanishing total cost in the log of either partition function. Exactly,
\[
 \frac{Z_1}{Z_0}
  =\frac{\mu_0^*(\mathcal A)}{\mu_1^*(\mathcal A)}
          \mathbb E_{\mu_0^*}\!\left[e^{-B}\mid\mathcal A\right].        \tag{21}
\]
It follows by integrating the unnormalized crossed density on \(\mathcal A\). Bounds (17)–(20) and Jensen give a lower bound \(\exp[-C V_3\log^3(2+\beta)]\) on the conditional expectation. Its required lower limit at some fixed physical side is **strictly greater than \(1650/1651\)**. The large pointwise losses in (13) and (16) do not refute this. Conversely, the survival probability of the restriction does not establish it.

## Testing the missing weight along the magnetic coupling

**PROVED (a remote action insertion).** For this step take \(\beta=\beta_j\to\infty\), \(\beta_j\le B_0\log n_j\), at a fixed allowed physical side. Keep the temporal plaquette coupling \(\beta\) and increase the spatial coupling \(s\) from 0 to \(\beta\) in the positive measure of (11), writing \(\mathbb Q_s\). The fixed-precision estimate (10) is uniform throughout this interpolation. It uses only \(01\) faces, whose coupling stays at \(\beta\), and the proof of (5) allows the other homogeneous nonnegative couplings between 0 and \(\beta\). Use \(p=7\) in the choice of strip width. The electric endpoint of row 863 and row 1145, §7, has \(Z_0/Z_1\to1\) on these boxes. In fact its normalized one-period trace tends to one by the product electric convolution bound there. The real magnetic interpolation and the signed action response themselves are prior work. [Electric endpoint and real interpolation](gap-solve2-astra62.md)

**PROVED.** For each spatial orientation \(ij\), let \(A_{ij}\in[0,4]\) be the sum of the two true lifted actions of *one* base plaquette. Choose each at transverse coordinate \(x_2=n/2\) with the strip at \(x_2=0\). At the isotropic endpoint, \(V=n^3T\) and
\[
 \frac{Z_0-Z_1}{Z_0+Z_1}
 =- V\int_0^{\beta}\sum_{ij=12,13,23}
            \operatorname{Cov}_{\mathbb Q_s}(D,A_{ij})\,ds+o(1).          \tag{22}
\]
Indeed the derivative of \(\mathbb E_{\mathbb Q_s}Y\) is minus its covariance with the sum of all spatial actions, by differentiating the bounded finite-volume integrals. Translation invariance of the flat-period classes and of \(Y\) replaces the sum by \(V\) times the three displayed covariances with \(Y\). Substituting \(D\) costs \(O(n^{-7})\) in each bounded covariance, uniformly in \(s\). The integrated error \(O(\beta V n^{-7})\) tends to zero. The initial value tends to zero by the electric endpoint. This also gives an actual regime where the accurate discrimination (6) coexists with a thermal ratio tending to one.

**OPEN.** What would finish this thermal step is an upper limit below \(1/3301\) for the right side of (22), or the lower limit in (21), at one fixed physical side along a matched trajectory. To see why a within-cover bound misses it, let \(p_c=\mathbb Q_s(\oint_t b=c)\). Exactly,
\(\operatorname{Cov}_{\mathbb Q_s}(Y,A_{ij})
=2p_0p_1(\mathbb E_{0,s}A_{ij}-\mathbb E_{1,s}A_{ij})\).
The local decision errors can be removed at a cost tending to zero even after the space-time sum. The signed difference of the two magnetic action means still needs control at that normalization. The bounds in (17) and (19) grow with spatial volume. Independently, the full nontrivial continuum construction and the transfer of a physical gap to its full observable Hilbert space have not been established here. The arguments are by hand, with no new independent check and no status change.

RESULT — OPEN. For the full Wilson two-period problem, the optimal overlap of the unordered raw link-pair laws has negative logarithm of order \(n^3\log(2+\beta)\). Integrating the seam gauge variables gives the actual mean estimate (17) and leaves the order-one comparison (21) open. I did not prove the four-dimensional SU(2) Yang–Mills mass gap in the sense of Jaffe and Witten.
