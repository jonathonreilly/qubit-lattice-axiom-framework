## Repo search

**GUIDE.** The source checkout is `fedacc21a43d8ab16ab7508c3cbbeea6946b7e40`. The target-specific prior file and row 1327's check report are absent at this pin. FINISH records the check assignment. The lead's November 8 digest covered main and PRs 10114, 10133, 10134 and 10141. I opened the relevant source passages on those refs. The soft-route one-step plaquette witness on PR 10114 (lines 4–14, 106–149) gives a positive correlation at finite coupling and its contraction proof applies at bare coupling at most 1/32. Grok's crossover reduction on PR 10133 (lines 77–90) still assumes the crossover estimate and source transport. The hard-route interface on PR 10134 (I1–I5) distinguishes nontriviality, a positive threshold and physical identification. PR 10141's FP1 (lines 299–315) estimates a single-scale classical minimizer. The finite-clock Villain note on main concerns a different gauge group. The closest hit is Theorem ZD-c on main at `8b11ae2bb9` (lines 311–320), which propagates a full periodic thermal seed under its hypotheses. [Lead's search](prior/repo-search-2026-11-08.md) · [Theorem ZD-c](gap-phys-seed.md)

## Sources and target

**OPEN.** The target is a nontrivial four-dimensional continuum SU(2) Yang–Mills theory with a unique vacuum, a nonempty excited space and some interval \((0,m_*)\), \(m_*>0\), disjoint from its Hamiltonian spectrum in physical units. Both the continuum construction and the spectral estimate require proof.

**GUIDE.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, give the one-bond convolution and gauge-projected Wilson transfer in GL3 and GL8. Their outline at lines 581–599 and 31858–31882 and their complete account I at 2704–2712 and 3213–3222 delimit the scalar construction and the separate infrared problem. I used the outline index, chunks 01, 02 and 29, and the obligations list to locate the relevant passages. [Outline, GL3](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2195-L2231) · [Outline, GL8](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2315-L2335) · [Account I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L3213-L3222)

**GUIDE.** Row 1218 credits Deep Bhattacharjee, Ushashi Bhattacharya, James Montgomery Lockwood, Tristan Romanov, Ikailo John Sessford and Sanjeevan Singha Roy with a conditional ascent from a small full thermal trace on a window of shapes. Their construction and the uniform starting estimate are distinct inputs. The first four authors also study cube heat-bath relaxation. Zeng Chunping's criteria require a common infrared rate or further microscopic hypotheses. Row 1325, equations (24)–(26), expresses thermal purity through a mean overlap between full-coupling open-cylinder states. Whether its lower limit exceeds \(1650/1651\) at one physical box size remains open. I use its exact target, without assuming its asymptotic error estimates or an unavailable check. The registry's TP1-LIMIT has a separate component-realization target. [Published-work comparison](prior/gap-onebound-read-sol.md) · [Preceding attempt](gap-solve40-astra62.md) · [Registry](open-registry.md)

## Which expansion degrees distinguish the states?

**GUIDE.** A cut comprises the temporal plaquettes joining two consecutive spatial slices. The comparison below interpolates between the full and constant cut kernels on the same Wilson cylinder. Choose disjoint packets of black vertices in one spatial slice. All six temporal plaquettes incident to the corresponding spatial edges at each black vertex belong to its packet. Keep only powers divisible by a chosen integer in the exponential for each packet. Prescribing the half-degree modulo two specifies one bit per packet. With very large period the all-zero residue favors the constant term, which gives a pure open-cylinder state. The test is whether estimates for the original one- and two-cut Wilson integrals control the overlap up to that regime. Row 1325 groups by a single total degree. Row 1151, equations (16)–(17), concerns the different parity of the electric representations on individual links. Neither of those labels is the packet degree used below. [Row 1151](gap-solve5-astra62.md) · [Row 1325](gap-solve40-astra62.md)

**GUIDE.** Set \(V=n^3\) on an even periodic spatial lattice, \(n\ge4\). Use normalized Haar and \(w(U)=\operatorname{tr}(U)/2\). The time length is \(T\ge2\) in one integral and \(2T\) in the other, with cuts at \(0\), or at \(0,T\). The full positive Wilson transfer is \(K=M C_\beta P M\), where \(P\) is vertex-gauge averaging, \(M\) is the magnetic half-weight and \(C_\beta\) is the product of the one-edge convolutions by \(e^{\beta w}\). Scalar factors per layer cancel below. Write \(B=M K^{T-1}M\), \(C=C_\beta P\) on the gauge-invariant space, \(Z_1=\operatorname{Tr}(BC)\), \(Z_2=\operatorname{Tr}(BCBC)\), and \(\Psi=2\log Z_1-\log Z_2\). Thus \(e^{-\Psi}\) is the purity of \(B^{1/2} C B^{1/2}/Z_1\). Electric flux sectors are all included.

**PROVED (positive packet expansion).** Every unoriented spatial edge meets exactly one black vertex in the bipartite spatial torus. Partition the black vertices into packets \(b\), and let \(m_b=6|b|\) count their distinct temporal plaquettes on one cut. Write \(Y_b=\sum_{e\in b^\star}w(U_{0e})\), where \(b^\star\) denotes the incident spatial edges. Flipping the central sign of the temporal link at every black vertex in \(b\) reverses \(Y_b\) and preserves every other packet and every weight off that cut. The Haar sign averages can be taken independently on different packets and cuts. Integrating over these sign choices replaces each \(e^{\beta Y_b}\) by \(\cosh(\beta Y_b)\) in partition integrals. Consequently, conditionally on all \(|Y_b|\) in the original Wilson field, independent auxiliary half-degrees \(J_b\ge0\) with probabilities
\[
 \Pr(J_b=j\mid |Y_b|)=\frac{(\beta |Y_b|)^{2j}}{(2j)!\cosh(\beta |Y_b|)}
 \tag{1}
\]
give the joint positive expansion in those packets, with \(J_b=0\) when \(Y_b=0\). This extends row 1325 (12) to separately variable couplings on disjoint stars. The integrated kernel of any prescribed vector of even powers is also positive semidefinite. Before vertex projection it is convolution by a product of even powers of sums of normalized fundamental characters on disjoint edge sets. Products and positive sums of characters with nonnegative representation coefficients give positive convolution operators by tensor products and Schur orthogonality. They commute with vertex projection because they are central on the edge product group. Sums over any residue choices therefore give positive semidefinite kernels with nonnegative entries.

**PROVED (cost of weakening selected packets).** All quantities below use the ordinary Wilson probability with spatial and temporal coupling \(\beta\). There is an absolute \(C\) such that, with \(D_\beta=\beta-C\log(2+\beta)\), one has the following for \(\beta\ge1\). For any packets on any distinct time layers, and \(0\le u_b\le1\), let \(Z(\boldsymbol u)\) use coupling \((1-u_b)\beta\) on those packets. Then
\[
 \frac{Z(\boldsymbol u)}{Z(\mathbf0)}
 \ \le\ \exp\!\left[-D_\beta\sum_b m_b\min(u_b,1/3)\right].
 \tag{2}
\]
Here and below unnormalized \(e^{\beta w}\) weights are used in ratios with changed couplings. After the independent sign integrations, \(\cosh(tY_b)\) increases for \(t\ge0\). Hence the ratio can only increase on replacing \(u_b\) by \(h_b=\min(u_b,1/3)\). The latter ratio is \(e^{-\beta\sum_b m_b h_b}\mathbb E_\beta e^{\beta\sum_p h_p(1-w_p)}\), with \(h_p=h_b\) on those plaquettes and zero otherwise.

**PROVED.** For this last expectation, split the three temporal plaquette orientations by Hölder with exponent three. In a single orientation, the dissemination argument of row 1151 (21) bounds the log moment of \(\sum_p v_p\beta(1-w_p)\), \(0\le v_p\le1\), by \(\sum_p[p(v_p)-p(0)]\). Here \(p(v)\) is the log partition function per spacetime site in action convention \(e^{-\beta(1-w)}\), with that orientation weakened uniformly by fraction \(v\). To see the variable-weight version, replicate each individual layer along the first axis using trace Hölder, then along the second, third and fourth. In an axis in the marked plane the layer factors have the form \(M C_i P M\), while an axis outside that plane gives \(C^{1/2} P M_i^2 C^{1/2}\) on the physical space. Each is positive, also at zero marked coupling. After the four replications each original plaquette profile is uniform throughout the torus with weight the reciprocal four-volume. This is precisely the proof of (21) with an arbitrary list of real layer profiles. Convexity gives \(p(v)-p(0)\le v[p(1)-p(0)]\). We have \(p(1)\le0\). Restricting every link to a Haar ball of radius \(\beta^{-1/2}\) about the identity gives \(p(0)\ge-C\log(2+\beta)\) because the ball has mass at least \(c\beta^{-3/2}\) by the radial Haar density, each plaquette angle is at most \(4\beta^{-1/2}\), and there are four links and six plaquettes per site. Applying the bound with \(v_p=3h_p\) and taking the cube roots gives (2). This uses the finite trace argument and a cap integral, with no perturbative pressure asymptotics. [Row 1151, (21)](gap-solve5-astra62.md) · [Sussman–Alpoge, finite chessboard inequality](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2885-L2912)

**PROVED (uniform relative accuracy for every specified residue pattern).** Fix an integer \(q\ge2\). On a chosen set \(\mathcal B\) of packets, possibly on multiple cuts, specify \(J_b\equiv r_b\pmod q\). Define
\[
 h(q)=\min\{1-\cos(\pi/q),1/3\},\qquad
 E(\mathcal B,q)=\prod_{b\in\mathcal B}
 [1+(q-1)e^{-D_\beta m_b h(q)}]-1 .
\]
When \(D_\beta>0\), for any bounded observable \(F\) of the original Wilson field, using (1) on that field gives
\[
 \left|q^{|\mathcal B|}\mathbb E_\beta[F\,{\bf1}_{\{J\bmod q=r\}}]
                    -\mathbb E_\beta F\right|
 \le \|F\|_\infty E(\mathcal B,q).                                  \tag{3}
\]
In particular \(F=1\) gives relative error at most \(E(\mathcal B,q)\) against the uniform pattern probability \(q^{-|\mathcal B|}\).

**PROVED.** For a Fourier index \(k\) modulo \(q\), the conditional expectation of \(e^{2\pi ikJ_b/q}\) is \(\cosh(e^{i\pi k/q}\lambda_b)/\cosh\lambda_b\), where \(\lambda_b=\beta|Y_b|\). Its absolute value is at most \(\cosh(c_k\lambda_b)/\cosh\lambda_b\), \(c_k=|\cos(\pi k/q)|\), by the triangle inequality on the two exponentials. For a whole collection of indices, the expectation *of the product of these upper bounds* under the original law equals \(Z((1-c_{k_b})_b)/Z(\mathbf0)\) by the independent black-vertex flips. This use of absolute values before the Wilson integration allows \(F\) to be any bounded function of the history. Apply (2) to the support of the nonzero indices. Each contributes at most \(e^{-D_\beta m_b h(q)}\). Fourier inversion, bounding the \(q-1\) nonzero indices for each such packet, gives exactly the product in (3). No independence of physical plaquette fields is assumed.

**PROVED (overlap after fixing the labels).** For a cut filtered by a full residue vector \(r\), let \(C_r\) be its positive kernel with the original coefficients and no factor \(q^{|\mathcal B|}\). Put \(Z_1(r)=\operatorname{Tr}(BC_r)\) and \(\rho_r=B^{1/2}C_rB^{1/2}/Z_1(r)\). For \(\rho=B^{1/2}CB^{1/2}/Z_1\), and with \(E_2=E(\mathcal B\sqcup\mathcal B,q)<1/4\) for the two cuts,
\[
 \frac{\operatorname{Tr}(\rho_r\rho_s)}{\operatorname{Tr}\rho^2}
 =\frac{q^{2|\mathcal B|}\Pr_{2T}(r,s)}
        {[q^{|\mathcal B|}\Pr_T(r)] [q^{|\mathcal B|}\Pr_T(s)]}
 =1+O(E_2) ,                                                         \tag{4}
\]
uniformly in \(r,s\). The first equality uses \(\operatorname{Tr}(BC_rBC_s)\) in the numerator, including when the choices differ. Each factor in the second expression is within \(E_2\) of one by (3) at \(F=1\). Since \(\rho=\sum_s \Pr_T(s)\rho_s\), expansion of the squared Hilbert–Schmidt norm gives \(\|\rho_r-\rho\|_2^2\le C E_2\,\operatorname{Tr}\rho^2\). In particular the relative estimate holds even along a sequence on which the purity tends to zero. It controls how the state changes when these labels are specified. Its common purity is still a physical Wilson quantity.

**PROVED (an extensive example).** Take \(4\mid n\) and packets of eight black sites, hence \(m_b=48\), \(V/16\) packets per layer. They can be kept local by grouping the four black sites in each \(2^3\) spatial cell with those in its partner along the first axis. Set \(q=2\). If \(\beta/\log n\to b_*=11/(3\pi^2)\) in the Wilson convention, (3) on one or two layers has \(E_2=O(n^{3-16b_*+o(1)})\). On every temporal layer of a bounded-aspect four-torus the bound is \(O(n^{4-16b_*+o(1)})=o(1)\), since \(\pi^2<12\) by the circumscribed regular hexagon. Application to a continuum Yang–Mills trajectory requires identifying its bare schedule. More generally, \(3\) or \(4\) in these powers is compared with \(16\liminf\beta/\log n\), or one may enlarge the packets. For the example, any prescribed list of the \(V/16\) bits per cut gives the same limiting overlap to the relative precision (4). [Earlier use of this bare convention](gap-solve23-astra62.md)

## Comparing the physical transfer operators

**PROVED.** Let \(N_b\) be the number of packets on one cut. Repeat the same packet choice and residue assignment on each time step. Let \(K_r=M C_r M\) be this single-step transfer, with original coefficients, and put \(\widetilde K_r=q^{N_b}K_r\). For \(D_\beta>0\) write \(E_1=E(\mathcal B,q)\). On the full physical slice space one has
\[
             \|\widetilde K_r-K\|_{\rm op}\le E_1\|K\|_{\rm op}.          \tag{5}
\]
This bound applies to each individual excited level.

**PROVED.** In the roots-of-unity formula for \(\widetilde K_r\), a multi-index \(\mathbf k\) changes the coupling in packet \(b\) to \(\beta e^{i\pi k_b/q}\). Integrating the black-vertex signs removes the odd powers. Hence there are \(q^{N_b}\) terms of modulus-one coefficient and the zero index gives \(K\). The absolute value of the position kernel of the term at \(\mathbf k\), including projection and both magnetic half-weights, is bounded pointwise by that of the real transfer \(L_{\mathbf k}\) at coupling \(\beta|\cos(\pi k_b/q)|\) in each packet. This follows by taking absolute values inside the temporal-link Haar integration and reversing signs at the appropriate black vertices. Testing against absolute values of two \(L^2\) functions bounds the operator norm by \(\|L_{\mathbf k}\|\). For every integer \(t\ge2\), applying (2) on each cut of the periodic cylinder gives
\[
 \frac{\operatorname{Tr}L_{\mathbf k}^{t}}{\operatorname{Tr}K^{t}}
 \le \exp\!\left[-tD_\beta
          \sum_{b:k_b\ne0}m_b h(q)\right].
\]
The real transfers are positive trace class. Taking \(t\)-th roots and \(t\to\infty\) at fixed spatial size gives exactly the same bound for \(\|L_{\mathbf k}\|/\|K\|\) with \(t\) removed from the exponent. Sum over the nonzero indices to get (5). In particular no factor equal to the dimension of the physical state space occurs here.

**PROVED.** Let \(u_i\) and \(u_i(r)\) be the decreasing eigenvalues of \(K\) and \(K_r\), respectively, each divided by its own top eigenvalue and counted with multiplicity. For \(E_1<1\), min–max and (5) imply
\[
              \sup_i |u_i(r)-u_i|\le\frac{2E_1}{1-E_1}.                  \tag{6}
\]
Indeed all the eigenvalues before division differ by at most \(E_1\|K\|\) after the scalar \(q^{N_b}\) is included, and the perturbed top is at least \((1-E_1)\|K\|\). If \(a=L/n\) and \(E_1=o(a)\), the physical energies \(-a^{-1}\log u_i\) differ by \(o(1)\) uniformly for levels for which either energy is bounded by a fixed constant. Both eigenvalues there are eventually at least \(1/2\), where the logarithm is \(2\)-Lipschitz. The eight-site example above has \(E_1=o(a)\). The trace statement (4) still matters separately because a bound on individual eigenvalues does not sum their multiplicities.

**PROVED (repeated constraints and the heat trace).** At \(T=O(n)\) use (3) on *every* cut with the same \(r\). For \(E_{\rm all}=E(\mathcal B^{\sqcup T},q)<1/4\),
\[
 \frac{\operatorname{Tr}\widetilde K_r^{\,T}}{\operatorname{Tr}K^T}
                     =1+O(E_{\rm all}).
\]
If in addition \(TE_1=o(1)\) and \(E_{\rm all}=o(1)\), (5) at the top eigenvalue gives
\[
 \frac{\operatorname{Tr}(K_r/\|K_r\|)^T}
      {\operatorname{Tr}(K/\|K\|)^T}=1+o(1).                            \tag{7}
\]
For \(q=2\) and packets of eight black vertices the errors vanish at fixed physical side on the displayed bare schedule, simultaneously in (4), (6), and (7). The filtered transfer has an explicit local kernel. The next issue is whether the allowed powers can be thinned sufficiently to prove a seed for it.

## Attempt to obtain the physical seed from the zero residue

**PROVED (a regime with a small thermal trace).** Choose \(r_b=0\) at every packet, \(s=2q\), and \(A=\beta\max_b m_b\). The unscaled one-packet weight after sign integration is
\[
        F_s(x)=1+\sum_{j\ge1}\frac{x^{sj}}{(sj)!}.
\]
If \(eA/s<1\), set \(d=(eA/s)^s/[1-(eA/s)^s]\) and \(d_0=(1+d)^{N_b}-1\). Then \(1\le F_s(\beta Y_b)\le1+d\) by \(k!\ge(k/e)^k\), which follows by integrating \(\log x\) up to \(k\). After projection the temporal kernel on the whole cut lies between \(1\) and \(1+d_0\) pointwise. In the magnetic sandwich its constant term gives \(K_\varnothing=|v\rangle\langle v|\) with \(v=M{\bf1}\). The remainder is positive semidefinite by the expansion and has trace at most \(d_0\|v\|^2\). Indeed each nonnegative diagonal term in the uniformly convergent character expansion integrates to its trace, and the full diagonal is bounded by \((1+d_0)M^2\). Since \(\lambda_0(K_0)\ge\|v\|^2\),
\[
       \sum_{i\ge1}u_i(0)\le d_0,\qquad
       \operatorname{Tr}(K_0/\|K_0\|)^t-1\le d_0^{\,t},\quad t\ge1.     \tag{8}
\]
Here \(K_0\) means the zero-residue transfer at the displayed \(q\). For packets of eight on the displayed schedule, \(s\) the least even integer above \(2eA+10\log n\) gives \(d_0=o(1)\). This proves a seed for the altered transfer. With a single such cut per period and all other layers at full Wilson coupling one likewise has \(0\le 2\log Z_1(0)-\log Z_2(0,0)\le2\log(1+d_0)\) by comparison with the constant cut, for which the squared one-cut integral equals the two-cut integral.

**PROVED (operator comparison cannot reach (8)).** The original Wilson cube in this regime has \(u_1\to1\). Row 1231 (6), checked in row 1235, supplies the following spectral weight. For \(t=\lfloor\beta^\delta\rfloor,\ 0<\delta<1/192\), the centered neutral plaquette has positive spectral weight in lattice energies between \(1/t\) and \(2/t\) at sufficiently large \(n\) with \(\beta\le B_0\log n\). Thus \(u_1\ge e^{-2/t}\). With the all-zero pattern in (8), \(u_1(0)\le d_0\to0\). The difference of these second eigenvalues is a lower bound on the norm distance between the two *vacuum-normalized* one-step transfers. Its limit is one (the normalized positive operators both lie between \(0\) and \(I\)). Hence even freely rescaling before vacuum normalization cannot carry the one-step estimate (6) into this rank-one limit. The witness has a shrinking lattice energy and a diverging physical energy at fixed \(L\). It imposes no upper bound tending to zero on the physical mass. [Row 1231, (6)](gap-solve26-astra62.md) · [Row 1235, check of (4)–(6)](gap-solve26-check-opus.md)

**PROVED (a local test at a single cut).** The difference also occurs without repeating the large-\(q\) action through time. In a filtered packet as in (8), condition on all fields except its black temporal links, in the sign-integrated law. Their density relative to independent Haar is proportional to \(F_s(\beta Y_b)\) and lies between \(1/(1+d)\) and \(1+d\) after normalization. On Haar, any one incident temporal plaquette has \(\mathbb E w_p^2=1/4\) by the four equal coordinate moments on the unit sphere in \(\mathbb R^4\). Thus the filtered expectation differs from \(1/4\) by at most \(d\), for every exterior. This also applies to the history conditioned using (1) because \(w_p^2\) is invariant under the black-link sign changes. On the unaltered Wilson torus, translation invariance and the single-orientation pressure bound in the proof of (2) give \(\mathbb E_\beta(1-w_p)\le C\log(2+\beta)/\beta\) by Jensen at \(v=1\). Hence \(\mathbb E_\beta w_p^2\to1\). The specified strong filtering at one cut changes a bounded gauge-invariant observable there by \(3/4+o(1)\). Control of the physical-time *ratio* of the two sewings would have to survive this local change.

## A direct estimate on the open-cylinder states

**PROVED (trace norm for \(q=2\)).** The states on the *one-cut* physical cylinder satisfy a stronger indistinguishability estimate than (4) in this case. There is an absolute \(C_1\) such that, writing
\[
 E'_1=\prod_{b\in\mathcal B}
       \left[1+\exp\{-m_b(\beta/3-C_1\log(2+\beta))\}\right]-1,
\]
one has \(\sup_r\|\rho_r-\rho\|_1\le 2E'_1\) whenever the states are defined. For the eight-site packets, the expectation difference is \(o(1)\) uniformly over operators of norm at most one, including projectors chosen after the residue pattern is specified. The number of prescribed bits tends to infinity.

**PROVED.** For a nonzero Fourier bit, the one-edge convolution has kernel \(e^{i\beta w}\). Its scalar on the representation of dimension \(d\) is
\[
 c_d=\frac{2}{\pi d}\int_0^\pi e^{i\beta\cos t}\sin t\sin(dt)\,dt .
\]
This is the character integral from GL3 with complex argument. The smooth odd \(2\pi\)-periodic function \(e^{i\beta\cos t}\sin t\) has third derivative bounded by \(C(1+\beta)^3\). Three integrations by parts on the circle give \(|c_d|\le C(1+\beta)^3/d^4\). Hence the absolute value *as an operator* of this convolution has a continuous position kernel bounded in absolute value by \(\sum_{d\ge1}d^2|c_d|\le C(1+\beta)^3\). The dimension factor uses \(|\chi_d|\le d\). [Sussman–Alpoge, character normalization](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2195-L2231)

**PROVED.** Let \(D_S\) be the projected product convolution with imaginary coupling on the packets \(S\) and ordinary coupling elsewhere. It is normal, since the individual kernels are central, diagonal in Peter–Weyl coordinates, and commute with vertex averaging. Its operator absolute value on the physical space is obtained from the one-edge absolute values and the same projection. For positive \(B\),
\[
 \|B^{1/2}D_S B^{1/2}\|_1\le \operatorname{Tr}(B |D_S|).
\]
The polar phase commutes with \(|D_S|\), so factoring at \(|D_S|^{1/2}\) gives the bound by Hilbert–Schmidt Cauchy–Schwarz. The open kernel \(B\) is entrywise nonnegative. The previous single-edge bound and Haar averaging therefore give
\[
 \frac{\operatorname{Tr}(B |D_S|)}{Z_1}
 \le [C(1+\beta)^3]^{\sum_{b\in S}m_b}
       \frac{Z_{\rm deleted}(S)}{Z_1}
 \le \exp\!\left[-\big(\beta/3-C_1\log(2+\beta)\big)
                             \sum_{b\in S}m_b\right].
\]
The last inequality is (2) with these packets erased from one cut. Summing nonempty \(S\) in Fourier inversion bounds the trace norm of \(2^{N_b}B^{1/2}C_rB^{1/2}/Z_1-\rho\) by \(E'_1\). Its trace difference has absolute value at most \(E'_1\). Normalizing the positive first operator to trace one costs precisely that trace difference in trace norm. This proves the bound.

**PROVED (how much of the constant cut this estimate sees).** If the degree is zero in every packet, its exact one-cut probability is \(p_\varnothing=Z_{\rm deleted}(\mathcal B)/Z_1\). By (2),
\[
                       p_\varnothing\le e^{-D_\beta V},                 \tag{9}
\]
since the cut has \(3V\) temporal plaquettes. In the all-zero *residue* state at \(q=2\), the positive mixture weight of this literal constant kernel is at most \(2^{N_b}e^{-D_\beta V}/(1-E_1)\) when \(E_1<1\), by (3). More generally, on the ordinary cut, for equal-size packets the probability that the positive-degree packets leave only a forest of available spatial edges is at most \(2^{N_b}\exp[-(2V+1)D_\beta/3]\). Indeed a forest contains at most \(V-1\) edges. Thus the zero-degree packets must contain at least \(2V+1\) of the \(3V\) edges. Sum (2) over the possible erased packet sets. This estimate concerns the graph of edges available to the monomials. A monomial can also contract to a trivial representation on edges which are available. Dropping all the other terms on the strength of their probability would discard almost the whole state.

## Prescribing the actual degrees

**GUIDE.** The missing overlap is a ratio of partition integrals, so the failure of a one-step operator comparison leaves a second possibility. Fix an actual central degree in each packet on the long cylinder, where large kinetic energies have already been damped. The scalar cost of fixing the degrees cancels if it is the same per packet on the two cylinders. The following estimates test that cancellation on the original measure. In (3) the law of the original history with auxiliary labels is specified by (1). Identifying a raw observable in the unnormalized even-power integrand further requires invariance under the sign integrations, as in the \(w_p^2\) test above.

**PROVED (central degrees on growing sets).** Use fixed-size packets of \(m\) plaquettes per cut. Work on the two homogeneous rectangles \(n^3\times T\) and \(n^3\times2T\), \(T=n/2,\ 4\mid n,\ \beta\to\infty,\ \beta=O(\log n)\). Let \(s\) be an even integer nearest \(m(\beta-3/4)\), and for sufficiently large \(\beta\) define
\[
 p_s(x)=x^s/(s!\cosh x),\qquad x_s\tanh x_s=s,\qquad
 g_s(x)=p_s(x)/p_s(x_s).
\]
Then \(0\le g_s\le1\). For \(k\) specified disjoint packets of this size on the marked cuts, with constants depending only on \(m\) and the cited uniform moment bound,
\[
 e^{-C_m k/\beta}\ \le\
 \frac{\Pr_\beta(2J_b=s\text{ on every specified packet})}{p_s(x_s)^k}
 \ \le\ e^{-c_m k/\beta}.                                                \tag{10}
\]
In particular, \(k=o(\beta)\) exact central-degree prescriptions retain the relative overlap in (4) with error \(O_m(k/\beta)\), even though their joint probability can tend to zero. Residues on the other packets may still be set as in (3), at additional absolute error \(E_2\) in the probabilities divided by their proposed scalar factors. Indeed the product of the \(g_s\)'s is a bounded observable of the configuration, and the labels are conditionally independent on disjoint packets.

**PROVED (lower bound in (10)).** Write \(X=\beta(m-Y_b)\), \(\lambda=\beta |Y_b|\). Row 1151 (21)–(22a) gives \(\mathbb E e^{X/48}\le C_m\) on both rectangles, by its marked-plaquette estimate. Its source uses Sourav Chatterjee's open-box method for the pressure. Thus \(X\) has bounded second moment and \(\Pr(\lambda<x_s/2)\le C_m e^{-c_m\beta}\), since \(0\le m\beta-\lambda\le X\) and \(x_s=s+O(se^{-2s})\). The latter asymptotic follows from \(x_s\ge s\) and \(x_s=s/\tanh x_s\). On \(\lambda\ge x_s/2\), Taylor's formula at the maximum and \(-(\log p_s)''=s/x^2+\operatorname{sech}^2x\) bound \(-\log g_s(\lambda)\) by \(C(\lambda-x_s)^2/s\). Its expectation on this set is \(O_m(1/\beta)\). [Row 1151, pressure estimate](gap-solve5-astra62.md) · [Check of (21)–(22b)](gap-solve5-check-opus.md)

**PROVED.** To integrate the logarithm at zero, condition on all but one top spatial edge of a temporal plaquette in the packet. Its contribution to \(Y_b\) is the only one containing this link and gives a single rotated quaternion coordinate under its conditional Wilson density. The density of that link against Haar is bounded by \(C(1+\beta)^{3/2}\). Its exponent is \(t\,v\cdot U\) with \(0\le t\le6\beta,\ |v|=1\), and the cap of angular radius \((1+t)^{-1/2}\) has Haar mass at least \(c(1+t)^{-3/2}\) and exponent at least \(t-1\). The Haar coordinate itself has bounded density. Hence \(\Pr(\lambda<v)\le C\sqrt\beta\,v\) for \(\beta\ge1\). On \(0<\lambda<x_s/2\), \(-\log g_s(\lambda)\le s\log(x_s/\lambda)\). In the tail integral of this logarithm, use the smaller of \(C_m e^{-c_m\beta}\) and \(C\sqrt\beta\, x_s e^{-y}\) for \(\Pr(\lambda<x_se^{-y})\), \(y\ge\log2\). Splitting the integral at \(2c_m\beta+O(\log\beta)\) makes the contribution, even after multiplication by \(s\), exponentially small up to a polynomial. Thus \(\mathbb E\log g_s(\lambda)\ge-C_m/\beta\). Jensen on the product in (1) proves the lower bound for every \(k\).

**PROVED (upper bound in (10)).** Fix all spatial and white temporal links. On a marked cut the black temporal links are then independent. At a black vertex \(i\) write its six plaquette terms in the exponent as \(t_i z_i\), where \(z_i\) is a unit-quaternion coordinate and \(0\le t_i\le6\beta\). Conditional on this exterior, \(z_i\) has density proportional to \(e^{t_i z_i}\sqrt{1-z_i^2}\) on \([-1,1]\). Thus \(\lambda=|\sum_{i\in b}t_i z_i|\). If every \(t_i<1\), this is at most \(m/6\), far from \(x_s\). If any \(t_i\ge1\), its variable \(y=t_i(1-z_i)\) has density proportional to \(e^{-y}\sqrt{y(2t_i-y)}\) on \([0,2t_i]\). Integrating from zero to one gives a normalizer at least \(c\sqrt{t_i}\), so the density is bounded by \(C e^{-y}\sqrt y\). Adding the other independent variables and taking absolute value gives a density of \(\lambda\) bounded by an absolute constant. In either case there is a fixed \(\delta>0\) with conditional probability at least \(1/2\) of \(|\lambda-x_s|\ge\delta\). The curvature lower bound \(s/(x_s+\delta)^2\) up to distance \(\delta\) from the maximum and monotonicity beyond it give \(g_s(\lambda)\le1-c/s\) on that event. The conditional mean is at most \(1-c_m/\beta\) on every exterior. The packets are conditionally independent on distinct black links, including at the two cuts. Multiplying proves the upper bound. Thus \(k\gg\beta\) provably defeats the proposed product of the separate *peak* probabilities. This conclusion does not compare the normalized one- and two-period probabilities with each other.

**PROVED (test of a scalar correction).** The \(1/\beta\) loss in (10) has a conditional coefficient which depends on the surrounding field, even on exteriors tending uniformly to the identity on the packet. Put \(\ell=m/6\). The nearest-even convention bounds \(m\beta-s\), so take a subsequence with \(m\beta-s\to D\). Prescribe the exterior so that \(t_i=6\beta-A_i+o(1)\) at the \(\ell\) black vertices, with \(A_i\ge0\) fixed and \(A=\sum_i A_i\). In this conditional Wilson measure,
\[
 \lim_{\beta\to\infty}\beta\left[1-\mathbb E(g_s(\lambda)\mid
                                   \text{exterior})\right]
  =\frac{(A+3\ell/2-D)^2+3\ell/2}{2m}.                                \tag{11}
\]
The independent \(y_i=t_i(1-z_i)\) have densities which converge with all moments to \(e^{-y}\sqrt y/\Gamma(3/2)\) by dominated convergence. The mean and variance of that law both equal \(3/2\), by integration by parts. Before folding the absolute value, \(\sum_i t_i z_i=m\beta-A-\sum_i y_i+o(1)\). A sign reversal has exponentially small probability by the same density bound, with \(\ell\) fixed. At fixed \(y_i\), Taylor expansion of \(\log g_s\) at \(x_s\sim m\beta\) gives \(\beta(1-g_s)\to(D-A-\sum_i y_i)^2/(2m)\). On \(\lambda\ge x_s/2\), the curvature bound used in (10) dominates \(\beta(1-g_s)\) by \(C_m(1+\sum_i y_i)^2\), and the complement has exponentially small conditional probability. This proves (11).

**PROVED.** Both \(A=0\) and \(A=4m\) in (11) occur on legitimate near-flat exteriors. Set the white temporal links and the links of the two spatial slices to the identity. For the second choice rotate two distinct bottom spatial links incident to one chosen black vertex so that their oriented contributions to its six staples are \(e^{i\theta}\) and \(e^{-i\theta}\) in one quaternion circle, with \(2\beta(1-\cos\theta)=4m\). This is possible for all sufficiently large \(\beta\) and \(\theta\to0\). Then \(t_i=\beta(4+2\cos\theta)\) there, and every other black vertex has the unchanged six staples. The coefficients in (11) differ since \(D\in[3m/4-1,3m/4+1]\). One may make the same choice in each of \(k\) packets on one cut because the selected bottom links have distinct black endpoints from packet to packet. Conditional independence then makes the logarithms of the two conditional degree probabilities differ in magnitude by \((c+o(1))k/\beta\) with \(c>0\). The formulas are continuous at these prescribed exteriors, so they also test uniform bounds expressed as essential suprema. A geometry-independent scalar per packet cannot approximate both conditional probabilities with log error \(o(k/\beta)\). Averaging those exterior contributions in the *two actual cylinder laws* remains a different calculation.

## Remaining infrared estimate

**PROVED (what the two-period normalization retains).** Condition on the all-zero \(q=2\) residue vector on the marked cut(s). Let \(p_T\) be the probability, in this conditional expansion on the \(T\)-cylinder, that every actual degree on the cut is zero. Define \(p_{2T}^{(2)}\) with the same condition on both antipodal cuts of the \(2T\)-cylinder. Then
\[
          \frac{p_{2T}^{(2)}}{p_T^2}
        = e^\Psi\,\frac{\Pr_T(r=0)^2}{\Pr_{2T}(r=0,r=0)}
        =e^\Psi(1+O(E_2)).                                             \tag{12}
\]
Before conditioning, erasing the sole cut gives the rank-one kernel \(|{\bf1}\rangle\langle{\bf1}|\), so the numerator with both cuts erased is the square of the one-cut numerator. Dividing by the two torus partition functions and then conditioning gives the first equality. Apply (3) for the second. The absolute rarity in (9) and the bounds in (10) do not yield a relative estimate of \(p_{2T}^{(2)}\) against \(p_T^2\) at the precision required in (12).

**OPEN.** In the setting of Theorem ZD-c, take the dyadic admissible physical sizes \(L\), \(n=L/a_j\) divisible by four, and \(T=n/2\). On schedules with \(E_2\to0\), a sufficient inequality at one fixed \(L\) is \(\limsup_j p_{2T}^{(2)}/p_T^2<1651/1650\). Equivalently for this test, it suffices that the all-zero \(q=2\) state have \(\liminf_j\operatorname{Tr}\rho_0^2>1650/1651\), by (4). Indeed \(\operatorname{Tr}U^{2T}\le\operatorname{Tr}U^T\) for \(U=K/\|K\|\), hence \(\log\operatorname{Tr}U^T\le\Psi\). This would supply the strict \(1/1650\) two-stage seed under the theorem's hypotheses. I obtain neither inequality. Equation (11) explains where a pointwise comparison of the actual-degree probabilities loses the needed precision. It puts no lower bound on the uncancelled error after Wilson averaging. The matched nontrivial continuum theory, its full gauge-invariant observable space, and a positive spectral gap in that theory also remain open. These hand arguments await independent review and grant no scientific status. [Theorem ZD-c](gap-phys-seed.md) · [Earlier overlap criterion, (24)–(25)](gap-solve40-astra62.md)

RESULT — OPEN. Fixing one expansion-degree bit per eight black sites per layer preserves the Wilson thermal trace to vanishing relative error and the bounded physical energies to vanishing absolute error on the stated schedules. The required strict bound on the two-period probability ratio (12) at fixed physical size remains open. The four-dimensional SU(2) Yang–Mills mass gap in the sense of Jaffe and Witten remains unproved here.
