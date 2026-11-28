# gap-lit-grok: a third-provider literature search on the crux (FINISH row 742)

**Writer:** xAI Grok 4.7, reasoning effort xhigh, headless single-turn run of the Grok CLI 1.0.77 on the lead's MacBook, 2026-11-11 (about 23:44Z to 23:53Z). Tools used: 65 web searches, 20 web fetches, 9 reads; no shell, no file edits. The prompt is self-contained (the crux and the four means of `library/gap-skeleton-final.md` 13.17); Grok read no file of this repository. This is a reading note only. It proves nothing and grants no status. Below the line is Grok's final answer, verbatim.

**Lead's verification (Claude Opus 5.5), done by script before recording.** All 21 arXiv identifiers cited resolve on the arXiv API, and each title and first authors match the description (hep-lat/9603022, 0707.2179, 0712.2620, 0803.3019, 0808.3442, 0901.4246, 1502.07719, 1604.04777, 1803.01950, 2106.14416, 2201.03487, 2202.10375, 2204.12737, 2307.06790, 2308.07534, 2502.19942, 2505.16585, 2506.00284, 2608.10133, 2610.35286, 2611.11534). Twelve of them do not appear among Grok's web-fetch calls (0707.2179, 0712.2620, 0808.3442, 1502.07719, 1604.04777, 2106.14416, 2201.03487, 2202.10375, 2506.00284, 2608.10133, 2610.35286, 2611.11534); for those, what Grok calls "opened" rests on search-result extracts or ar5iv pages returned by search, not on a fetch the lead can see. DOIs, Zenodo records and the quoted sentences were not checked. The lead did not read the papers. Read every statement below as Grok's reading, GUIDE for any number.

---

No known means supplies a small number, a small dual activity, an exact block-spin closure, or a dichotomy at order-one effective coupling for four-dimensional Wilson SU(2). The results that have the shape of the open step all stop at the same place: a twist or vortex ratio that is small only where a strong-coupling expansion already works.

The Wilson coupling below is the coefficient in the lattice action. For SU(2), Kanazawa writes \(\frac{\beta}{2}\sum_p\mathrm{Tr}\,U_p\). Shen–Zhu–Zhu and Cao–Park–Sheffield use a ’t Hooft-scaled coefficient in front of \(N\beta\,\mathrm{Re}\,\mathrm{Tr}\). Those two conventions differ by factors of order \(N\). Continuum scaling is the direction in which the bare coupling goes to zero and the correlation length, in lattice units, goes to infinity. A bound that holds only for small bare \(\beta\) is a lattice-unit gap on that side of the phase diagram.

## 1. Tomboulis–Yaffe, as stated by Kanazawa

**(a)** Takuya Kanazawa, Annals of Physics 324 (2009) 1634–1665. For Wilson SU(2) on a finite four-dimensional torus, any one-plaquette action that is site-reflection positive, and any \(\beta\): if \(C\) is a rectangle in the \(\mu\nu\)-plane, of area \(A_C\), and \(\mathcal{V}\) is a vortex sheet wrapping the other two directions, then
\[
\langle W(C)\rangle\le 2\Bigl\{\tfrac12\bigl(1-Z_\Lambda^{(-)}/Z_\Lambda\bigr)\Bigr\}^{A_C/(L_\mu L_\nu)}.
\]
For SU(\(N\)), Theorem 2 bounds the Wilson loop in a representation of \(N\)-ality \(N(R)\) by the corresponding electric-flux free energy and by \(1-\langle\mathcal{F}^{[0]}\rangle\), each raised to \(A_C/(L_\mu L_\nu)\). The message he draws from (28) is that exponential decay of the vortex free energy for every nontrivial centre twist is sufficient for the area law. The same shape, Theorem 3, survives coupling to matter of \(N\)-ality zero. He records that Münster’s convergent strong-coupling cluster expansion gives \(-\log\langle\mathcal{O}^{[k]}\rangle\approx e^{-\rho L_\mu L_\nu}\) for SU(2), and by the same method for SU(\(N\)), when the coupling is strong enough, with \(\rho\) equal to the fundamental string tension. The original Tomboulis–Yaffe theorem that Kanazawa cites as proved is the opposite phase: absence of confinement in SU(2) at high temperature.

**(b)** This is a sufficient condition of the shape of seed (ii). The smallness that would turn the inequality into an area law is an input. Where that input is proved, the means is M1 at strong bare coupling.

**(c)** The inequality itself applies to four-dimensional Wilson SU(2) at every \(\beta\), including order-one effective coupling. It does not verify the seed. The ratio \(Z^{(-)}/Z\) is left unestimated once the strong-coupling cluster expansion stops. Centre-even screening is visible in the bound: when the \(N\)-ality vanishes, the right-hand side of (26) tends to 1 as the torus grows, so gluons of zero \(N\)-ality are not forced into an area law.

**(d)** The ar5iv HTML of arXiv:0808.3442v3, through Theorems 1–4 and the strong-coupling discussion in §2. The spin-system half and the triangular-Ising conjecture were not read. The 1985 Tomboulis–Yaffe paper itself was not opened; the inequality is taken from Kanazawa’s restatement, which attributes Theorem 1 to that paper and to a 2008 note of his.

**(e)** arXiv:0808.3442, DOI 10.1016/j.aop.2009.04.002. Opened: https://ar5iv.labs.arxiv.org/html/0808.3442

## 2. Mack–Petkova vortex containers

**(a)** G. Mack and V. B. Petkova, Annals of Physics 125 (1980) 117–134. For a compact gauge group with nontrivial centre, in particular SU(2), they give a sufficient condition for confinement of static quarks by thick vortices constrained to containers \(\Gamma_i\). For SU(2) the confining potential is bounded below by a sum of \(-\log\tanh(\xi_i/2)\), where \(\xi_i\) is the maximum, over boundary conditions, of the free-energy cost of changing the vorticity on \(\partial\Gamma_i\). If that cost stays below a fixed \(\xi\) and the number of containers around a loop of length \(L\) grows so that \(TN(L)\to\infty\), then \(V(L)\to\infty\). For abelian theories in three dimensions they recover the confining Coulomb potential as a lower bound by inserting elementary thin-vortex estimates.

**(b)** Again a sufficient condition of seed shape. The three-dimensional abelian case is closed by a direct estimate, which is M1 on thin vortices. The nonabelian four-dimensional condition is stated and not verified.

**(c)** The criterion is exactly a uniform smallness of a vorticity free energy on boxes of every size. Nothing in the part read produces that smallness for four-dimensional SU(2) at order-one coupling. The paper says it does not discuss approximation schemes.

**(d)** Abstract from ScienceDirect, and the opening of the DESY preprint through the SU(2) statement (1.6a)–(1.7), as returned by search from the DESY PDF. The rest of the preprint was not re-read in this session.

**(e)** DOI of the journal article: the ScienceDirect record is https://www.sciencedirect.com/science/article/abs/pii/0003491680901219 (abstract only; the body is paywalled and was not opened). Preprint text: http://www-library.desy.de/preparch/desy/postpr/1978/desy78-069.pdf

## 3. Kovács: vortex inequalities after a centre split

**(a)** Tamás G. Kovács, Nuclear Physics B 482 (1996) 613–638. Two-dimensional SU(2) principal chiral model, nearest-neighbour ferromagnetic action, any inverse temperature. Exponential decay of the twist \(G(L)\), built from the ratio of twisted and untwisted partition functions, implies a mass gap. After gauging the centre, the model is an SO(3) spin system coupled to \(\mathbb{Z}_2\) link variables. A further duality produces a dual Ising model. A nonzero effective magnetic field in that Ising model is sufficient for the SU(2) mass gap. Certain vortex correlation inequalities, if true uniformly in the volume, would produce such a field. For zero field the inequalities follow from a Ginibre decomposition and are strict. He argues that a neighbourhood of zero field should survive the infinite-volume limit, checks two-vortex probabilities by Monte Carlo at \(\beta=2.0\) on lattices up to \(L=13\), and states that the inequalities and the nonvanishing of the long \(\eta\)-string are not proved. Section 6 says the same scheme applies to three- and four-dimensional SU(2) gauge theory, with \(\mathbb{Z}_2\) monopole loops in place of vortices and the sourceless ’t Hooft loop in place of the twist, and that the confinement problem then reduces to \(\mathbb{Z}_2\) monopole correlation inequalities. Those inequalities are not proved. Monte Carlo for the gauge-theory monopoles is deferred to a later paper.

**(b)** This is an attempt at M4: a correlation inequality with a parameter (the effective field) whose positivity would force exponential decay. The parameter’s positivity is the unproved step. There is no small activity. The SO(3) measure is “blind” to the centre, and the vortex weights are expectations in that measure, not a small fugacity.

**(c)** The two-dimensional spin theorem does not apply to four-dimensional gauge theory. The last section asserts that the bookkeeping carries over, and that the missing step becomes a monopole correlation inequality of the same kind. That is the open seed again, now for monopole correlators. The Ginibre step he uses is for the effective Ising variables. He does not produce a Ginibre or FKG inequality for the SU(2) spins themselves that would close the vortex bound.

**(d)** ar5iv HTML of hep-lat/9603022, Sections 1 through 3.2 in the fetch, and Sections 4–6 from the saved remainder of the same fetch (the fetch truncated at 30720 of 81600 bytes; the later sections were read from that file). The appendix diagrams were not read in full.

**(e)** arXiv:hep-lat/9603022, DOI 10.1016/S0550-3213(96)00561-5. Opened: https://ar5iv.labs.arxiv.org/html/hep-lat/9603022v1

A shorter Physics Letters B paper with Tomboulis, DOI 10.1016/0370-2693(95)01428-4, states the same conditional inequalities and says the method translates to four-dimensional SU(2) and SO(3) monopoles. Only the ScienceDirect abstract was opened: https://www.sciencedirect.com/science/article/abs/pii/0370269395014284

## 4. Tomboulis’s all-coupling claim, and Ito–Seiler

**(a)** E. T. Tomboulis, arXiv:0707.2179 (15 July 2007). He claims that four-dimensional SU(2) lattice gauge theory, \(d\le 4\), is confining for every bare coupling \(0<g<\infty\), by interpolating Migdal–Kadanoff decimations so that the vortex free energy on the original lattice equals a ratio of Migdal–Kadanoff partition functions at a common interpolation parameter, then invoking the strong-coupling decay of that ratio. Keeping the string tension fixed, he concludes \(g(a)\to 0\) as \(a\to 0\).

K. R. Ito and E. Seiler, arXiv:0803.3019 (20 March 2008) and PoS Confinement8:034 (arXiv:0901.4246). They isolate three unproved steps: existence of the interpolation times \(t_m\), existence of a common \(t_*\) with \(\alpha=\alpha^+\), and extension of the implicit-function branch from \(\lambda=0\) to \(\lambda=1\). Kanazawa’s counter-example \(\Psi(\lambda,t)=e^{-t}-1+2\lambda\) shows that \(\partial\Psi/\partial t\neq 0\) does not give the extension. The extra parameter \(r<1\), introduced to keep \(\alpha\) away from 1, raises the effective dimension. For \(r<1\) and large \(\beta\) the modified recursion flows to the weak-coupling fixed point, so the strong-coupling input is lost. Their numerical iteration for SU(2) at \(r=0.9\), \(\alpha=1\), changes behaviour near \(\beta\approx 4.8\). They record that for U(1) at large \(\beta\) and \(r=1\) the common \(t_*\) does not exist, while for \(r<1\) a \(t_*\) may exist and still does not give confinement, because four-dimensional U(1) deconfines (Guth; Fröhlich–Spencer, cited by them). The Migdal–Kadanoff coefficients \(c_j(n)\to 0\) for \(d\le 4\) both for SU(\(N\)) and for U(\(N\)) when \(r=1\).

**(b)** The intended means is M3, exact closure of a block-spin map, plus M1 on the decimated theory. Ito–Seiler show that the closure (a common interpolation parameter, with the flow still strong-coupling) is not proved.

**(c)** This is the all-coupling attempt aimed at four-dimensional SU(2). The block is the comparison of twisted and untwisted partition functions at one and the same effective action. An argument that never uses the nonabelian structure also applies to four-dimensional U(1), which has a perimeter law at large \(\beta\).

**(d)** Tomboulis 0707.2179: abstract from the arXiv abs page. Ito–Seiler 0803.3019: ar5iv HTML through the discussion in §3.3, including Problems 1–3, the \(r<1\) flow, the Kanazawa example, and the closing discussion. The five-page PoS writeup was opened as PDF text via arXiv in search, not page-imaged in this session.

**(e)** arXiv:0707.2179, https://arxiv.org/abs/0707.2179. arXiv:0803.3019, https://ar5iv.labs.arxiv.org/html/0803.3019. arXiv:0901.4246, DOI 10.48550/arXiv.0901.4246, https://arxiv.org/abs/0901.4246

Tomboulis’s reply, arXiv:0712.2620, was opened only as an abstract (via a secondary index). He says the disputed inequality is used only at strong coupling. That does not supply the missing common \(\alpha_*\).

## 5. Centre comparison, and Ising lattice gauge theory

**(a)** Ryu Ikeda and Kei-Ichi Kondo, PTEP 2021, 103B06. They compute double-winding Wilson loops in \(\mathbb{Z}_N\) lattice gauge theory by a character expansion and recover the \(N\)-dependent area laws previously found for SU(\(N\)) at strong coupling (difference of areas for \(N=2\), max of areas for \(N=3\), sum of areas for \(N\ge 4\)). They attribute to Fröhlich a rigorous centre dominance: confinement in the \(\mathbb{Z}_N\) theory implies confinement in the SU(\(N\)) theory, including with Higgs fields in a centre-trivial representation, and the comparison extends from single loops to multiple windings. Their own explicit formulae are leading-order. They state that for spacetime dimension \(D>2\), once \(\beta\gg 1\) the higher-order terms are of the same order as the leading term, so the evaluation from the leading diagram holds only for \(\beta\ll 1\).

Malin P. Forsström and Fredrik Viklund, arXiv:2502.19942v2 (17 November 2025). Ising lattice gauge theory, every \(\beta\ge 0\): a random-current expansion and a switching lemma, summation over surfaces, non-negative Wilson loops, Griffiths’ second inequality, and monotonicity of Wilson loops in \(\beta\). Area law is proved for sufficiently small \(\beta\). Exponential decay of correlations is proved for small \(\beta\) and for large \(\beta\). The HTML extract of the note says the area-law estimate is the only place a restriction on \(\beta\) is required, and that the current expansion near the critical value is left open.

Paul Duncan and Benjamin Schweinhart, arXiv:2308.07534v2, Communications in Mathematical Physics (2025). Sharp area-to-perimeter transition for Wilson loops in \((d-2)\)-dimensional \(q\)-state Potts hyperlattice gauge theory on \(\mathbb{Z}^d\), dual to Potts, and for \((d-1)\)-dimensional plaquette percolation. Unconditional for Ising. For \(q>2\) it uses a slab regularity conjecture for the random-cluster model.

**(b)** Fröhlich’s comparison is a correlation inequality. Forsström–Viklund’s Griffiths inequality is the spin-model inequality in the Ising gauge setting; the area law they deduce is M1 at small \(\beta\). Duncan–Schweinhart is an M4 sharpness theorem for a percolation representation.

**(c)** Centre dominance would give an SU(2) area law from a \(\mathbb{Z}_2\) area law. In four dimensions the \(\mathbb{Z}_2\) gauge theory has a deconfining transition, so a bound by the centre theory at weak coupling is a perimeter bound. Forsström–Viklund’s inequalities hold at all \(\beta\) for the Ising theory and do not force the area law through the transition. Duncan–Schweinhart’s plaquettes have codimension one in the lattice dimension they treat. Four-dimensional Wilson theory has two-dimensional plaquettes. Neither paper treats SU(2).

**(d)** Ikeda–Kondo: ar5iv HTML through the strong-coupling discussion after (23). The displayed Fröhlich formula with the factor \(2\dim(G)\beta\) was not on the pages read; the citation is qualitative. Forsström–Viklund: abstract from the arXiv abs page, plus one HTML extract of the area-law paragraph from a search hit on arXiv HTML. Duncan–Schweinhart: abstract from https://arxiv.org/abs/2308.07534. The proofs were not read.

**(e)** arXiv:2106.14416, DOI 10.1093/ptep/ptab114, https://ar5iv.labs.arxiv.org/html/2106.14416. arXiv:2502.19942, https://arxiv.org/abs/2502.19942. arXiv:2308.07534, DOI 10.48550/arXiv.2308.07534.

Sylvester’s 1980 counter-examples to Ginibre’s inequality for spin dimension at least 3 were not opened. Recalled, not opened: SU(2) is the three-sphere, so the classical Ginibre/Griffiths route for vector spins stops at spin dimension 2.

## 6. Log-Sobolev and stochastic quantisation

**(a)** Hao Shen, Rongchan Zhu, and Xiangchan Zhu, arXiv:2204.12737 (27 April 2022). Lattice Yang–Mills in any dimension \(d>1\), gauge group SO(\(N\)) or SU(\(N\)), ’t Hooft scaling. If \(|\beta|<(N-2)/(32(d-1)N)\) for SO(\(N\)), or \(|\beta|<1/(16(d-1))\) for SU(\(N\)), the Langevin dynamics has a unique infinite-volume invariant measure, the finite-volume measures converge to it, and log-Sobolev and Poincaré inequalities hold. Wilson loops factorise at large \(N\), and a large class of observables clusters exponentially. For \(d=4\) the SU(\(N\)) window is \(|\beta|<1/48\). They present this as an improvement of Osterwalder–Seiler under ’t Hooft scaling: the small-\(\beta\) neighbourhood is uniform in \(N\).

Jack Piazza and Hao Shen, arXiv:2610.35286 (26 October 2026). Log-Sobolev for the two-dimensional SU(\(N\)) Wilson measure at every fixed \(\beta\), with constant \(C_{N,\beta}\) independent of the area. The proof is a two-scale disintegration. They write that Poincaré and log-Sobolev inequalities in all dimensions are in Shen–Zhu–Zhu, only at strong coupling, and that a mass gap in two dimensions is essentially trivial because Wilson loops decorrelate.

Ajay Chandra, Ilya Chevyrev, Martin Hairer, and Hao Shen, arXiv:2201.03487v2, Inventiones Mathematicae (2024). Stochastic quantisation of Yang–Mills–Higgs on the three-dimensional torus. Local-in-time solutions of the renormalised equation, gauge covariance in law, and a Markov process on gauge orbits up to possible finite-time blow-up. The abstract and the opening paragraph do not construct an invariant measure and do not claim a mass gap.

**(b)** Shen–Zhu–Zhu is M1: the Bakry–Émery curvature is positive when \(|\beta|\) is smaller than an explicit constant. Piazza–Shen removes the smallness in dimension two, where the geometry factorises. Chandra–Chevyrev–Hairer–Shen constructs a short-time flow.

**(c)** The four-dimensional SU(2) log-Sobolev constant is proved only for \(|\beta|<1/48\) in their normalisation, which is strong bare coupling. The two-dimensional all-coupling log-Sobolev uses a disintegration that the authors describe as special to dimension two. The three-dimensional stochastic quantisation does not produce the invariant measure whose spectral gap would be the mass gap, and it is not four-dimensional.

**(d)** Shen–Zhu–Zhu: ar5iv HTML, abstract and the comparison with Osterwalder–Seiler. Piazza–Shen: abstract and Theorem 1.1 from the arXiv PDF text returned by search. Chandra–Chevyrev–Hairer–Shen: abstract and the first paragraph of the HTML, which fixes \(d=3\).

**(e)** arXiv:2204.12737, https://ar5iv.labs.arxiv.org/html/2204.12737. arXiv:2610.35286, https://arxiv.org/abs/2610.35286. arXiv:2201.03487, DOI 10.1007/s00222-024-01264-2, https://arxiv.org/abs/2201.03487

## 7. Large \(N\) and surface sums

**(a)** Sourav Chatterjee, Communications in Mathematical Physics 366 (2019) 203–268, arXiv:1502.07719. Wilson loops of strongly coupled SO(\(N\)) lattice gauge theory, any dimension, in the large-\(N\) limit, as an absolutely convergent sum over lattice-string trajectories. Chatterjee and Jafar Jafarov, arXiv:1604.04777: the \(1/N\) expansion in the same regime, with \(|\beta|\le\beta_0(d,k)\) for the expansion through order \(k\). Riddhipratim Basu and Shirshendu Ganguly, the planar combinatorics of that model at strong coupling: opened only as the INSPIRE abstract, which also records an example in which a Wilson-loop area-law lower bound fails in full generality. Chatterjee’s survey arXiv:1803.01950 states that the rigorous construction of quantum Yang–Mills, especially in dimension four, is open. Abstract only.

Sky Cao, Minjae Park, and Scott Sheffield, arXiv:2307.06790v4 (26 September 2025). Wilson loops as sums over embedded surfaces for U(\(N\)), SU(\(N\)), O(\(N\)), SO(\(N\)), and Sp(\(N/2\)), any \(N\ge 1\), any \(\beta>0\), any \(d\ge 2\). Section 7, which was read, says: in \(d=2\) the area law holds for general groups at every \(\beta\); in \(d=3\) the U(1) area law holds at every \(\beta\), hence so does U(\(N\)), while SU(\(N\)) at large \(\beta\) is unknown; in \(d=4\) the U(1) area law holds at small \(\beta\) and fails at large \(\beta\), and “it remains a major open problem to prove the area law for any non-commutative group when \(\beta\) is large, \(N\ge 2\) and \(d=4\).” The same sentence, for exponential decay of Wilson-loop correlations, is open problem 2. Open problem 7: the surface sum contains terms of both signs, and a grouping that makes the cancellation manifest is known to them only for \(d=2\) and \(N=\infty\), in work they list as upcoming.

Sky Cao, Ron Nissim, and Scott Sheffield, arXiv:2505.16585v3. Area law for pure U(\(N\)), every \(d\ge 2\), every \(N\ge 1\), for all \(\beta\le\beta_0(d)\), improving Osterwalder–Seiler. The PDF text of the first pages, as returned by search, says the method is expected to extend to SU(\(N\)) and SO(\(N\)) after adjustments, and that the paper treats U(\(N\)). The same pages say that area law for \(\beta\) of order \(N\), or for small \(N\) and large \(\beta\), is open and would need near-cancellation of positive and negative surface weights. They cite earlier area laws that assume a strong mass gap as conditional on that gap.

**(b)** Chatterjee is M2: after the \(1/N\) string expansion the activity is small because \(|\beta|\) is small and \(N\) is large. Cao–Park–Sheffield is an exact change of variables at every \(\beta\), without a small activity. Cao–Nissim–Sheffield is M1 in an enlarged strong-coupling window for U(\(N\)).

**(c)** For SU(2), \(1/N=1/2\) is not small, and Chatterjee’s group is SO(\(N\)). The surface identity does apply to SU(\(N\)) in four dimensions at every \(\beta\), including order one. The authors list the large-\(\beta\) area law and the mass gap as open, and they list the both-sign cancellation as open outside two dimensions at infinite \(N\). The U(\(N\)) area law of Cao–Nissim–Sheffield is still inside a \(\beta\le\beta_0(d)\) disk.

**(d)** Chatterjee and Chatterjee–Jafarov: abstracts, plus Theorem 3.1’s small-\(\beta\) hypothesis from the PDF text of 1604.04777 returned by search. Basu–Ganguly: INSPIRE abstract only. Cao–Park–Sheffield: PDF pages 1–2 and 116–119, read as images. The proofs in §§2–6 were not read. Cao–Nissim–Sheffield: abstract and the opening theorem from the arXiv PDF text in search; the body past the first pages was not read.

**(e)** arXiv:1502.07719, DOI 10.1007/s00220-019-03353-3, https://arxiv.org/abs/1502.07719. arXiv:1604.04777, https://arxiv.org/abs/1604.04777. arXiv:1803.01950, https://arxiv.org/abs/1803.01950. arXiv:2307.06790, local PDF of v4 (ar5iv HTML failed). arXiv:2505.16585, https://arxiv.org/abs/2505.16585

## 8. Finite groups at large \(\beta\)

**(a)** Arka Adhikari and Sky Cao, Annals of Probability 53 (2025) 140–174, arXiv:2202.10375v3. Finite gauge groups, possibly nonabelian, dimension four in the paper, large \(\beta\): exponential decay of correlations for gauge-invariant functions, including arbitrary functions of Wilson loops. They state the Lie-group conjecture separately: decay for every \(\beta\ge 0\), with correlation length tending to infinity as \(\beta\to\infty\). High-temperature expansions cover Lie groups at small \(\beta\). The large-\(\beta\) proof uses defects. For finite nonabelian groups the defects do not factorise when they are linked, Borromean rings give a three-body interaction, and they say a cluster expansion is not available. The gap \(\Delta_G=\min_{g\neq 1}\mathrm{Re}(\chi(1)-\chi(g))\) is positive because the group is finite and the identity is isolated.

**(b)** M1 at large \(\beta\), with the small parameter the defect activity \(e^{-\beta\Delta_G}\).

**(c)** SU(2) has no spectral gap away from the identity in the group metric. The defect activity does not become small as the bare coupling goes to zero. The authors present the Lie-group statement at all \(\beta\), with \(\xi(\beta)\to\infty\), as the open conjecture.

**(d)** ar5iv HTML through the definitions and the discussion of abelian versus nonabelian defects. The theorem proofs were not read.

**(e)** arXiv:2202.10375, DOI 10.1214/24-AOP1702, https://ar5iv.labs.arxiv.org/html/2202.10375

## 9. Claims of a four-dimensional mass gap, 2015–2026

Tomboulis 2007 is the claim in §4. Ito–Seiler’s critique is the reception that has stayed in the literature.

D. C. Jacobsen, arXiv:2506.00284. The v1 abstract claims a Wightman theory and a strictly positive mass gap for pure SU(3) on \(\mathbb{R}^4\), by a five-dimensional orbifold regulator and a polymer expansion uniform in the continuum and infinite-volume limits. On 13 June 2025 arXiv admin withdrew the submission: it does not meet arXiv’s research-content quality standards. The PDF is withdrawn. Abstract and withdrawal notice opened at https://arxiv.org/abs/2506.00284. A related Zenodo record, 10.5281/zenodo.15786684, repeats a mass-gap claim; only the Zenodo description was opened.

Aleksandar Mihajlovic, arXiv:2611.11534 (8 November 2026). Abstract opened. It certifies a three-link conditioning functional through Wilson coupling 0.354, conditional on block-comparison hypotheses, and states that a nontrivial four-dimensional spatial-cutoff construction and a positive spectral bound along it are not established.

solidSF, Zenodo 10.5281/zenodo.24095337 (9 November 2026). The description, which was opened, says the record does not solve existence and does not prove a positive mass gap. Clustering, a unique continuum limit, and a positive physical decay rate are listed as open. An earlier record, 10.5281/zenodo.22904674, had claimed a mass gap; the description says that claim was wrong and is withdrawn.

A Zenodo campaign record, 10.5281/zenodo.19699784 (22 April 2026), describes a sketch of a lattice gap at all \(\beta\) by combining Bauerschmidt–Bodineau–Dagallier multiscale log-Sobolev inequalities with Shen–Zhu–Zhu, and says the continuum argument stalls on a circularity between the spectral gap and the correlation length, reported there as a factor of 23. The description calls the all-coupling lattice statement a proof sketch. Abstract only.

OpenAI’s October 2026 Lean submission, shepherded by Michael R. Douglas, David J. Gross, Arthur Jaffe, Igor R. Klebanov, and Nikita Nekrasov. The committee’s third statement, 9 November 2026, was read in full (one page). It announces publication, on 10 November, of the Lean code and of a validation which “proves the existence of pure Yang-Mills theory according to the problem statements which are standard in physics and mathematics.” It does not mention a mass gap. The 35-page assessment PDF was not opened (the raw GitHub URL is not a page this session retrieved). Papex’s 11 November 2026 explainer, opened in full, quotes the assessment’s opening: a relativistic theory satisfying the Wightman axioms can be constructed as a scaling limit of four-dimensional Wilson lattice gauge theory for any simple compact gauge group, and “It does not prove that the infinite-volume limit is unique or that there is a mass gap.” Papex also quotes the assessment: “The construction provides no evidence for or against a mass gap,” and lists a uniform mass gap, Wilson loops, and the area law among what Section 8 does not address. The explainer says the group writes “We do not claim to fully understand the proof yet,” and that the assessment rests on the Lean sources, not on the unreleased informal manuscript. Those sentences are Papex’s quotations of a PDF this session did not open.

The following were not re-opened in this session. Recalled, not opened: Kaushik Santhanam, Zenodo 10.5281/zenodo.17100103; Harold D. Kirk, Zenodo 10.5281/zenodo.18827354; V. P. Nair, arXiv:2608.10133; an Academia.edu note on stochastic quantisation with a monopole source. From the preceding session of this task, none of those closes a verified seed at order-one coupling, and Kirk’s dichotomy is a restatement of the missing upper bound on the lattice gap.

Göpfert–Mack, the three-dimensional U(1) area law at all couplings, was not opened. It appears inside Cao–Park–Sheffield §7.1(b), which was read, as the case where a dual monopole activity stays small at every \(\beta\). The same paragraph says the SU(\(N\)) question in three dimensions at large \(\beta\) is open.

RESULT: No known means applies to four-dimensional Wilson SU(2) at order-one effective coupling; the closest is Kanazawa’s form of the Tomboulis–Yaffe inequality, which is the seed, together with Kovács’s unproved vortex inequalities in the two-dimensional SU(2) chiral model.
