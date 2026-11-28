# Literature check: lattice transition tests

Model: Codex, dispatched as gpt-6-luna high. Research text only; this is not an audit and grants no proof status. No proof step uses these transition numbers.

Read in full: Creutz (1979, five-dimensional SU(2)); Knechtli, Luz and Rago (2011, five-dimensional SU(2)); Creutz (1981, SU(5)); Creutz and Moriarty (1982, SU(6)); Lucini, Teper and Wenger (2005, including §10 on bulk transition); Bhanot and Creutz (1981); Rinaldi, Lacagnina, Lucini, Patella and Rago (2012, mixed-action SU(2)); Arnold, Lippert, Schilling and Neuhaus (2000, compact U(1)). Guth’s published abstract was read, but his full article was NOT READ. Fröhlich and Spencer’s authors’ abstract was read, but their full article was NOT READ.

## Repo search

Lead search artifact `library/prior/repo-search-2026-11-08.md` is for a different target (row 531) and reports no check of these transition-test claims. At the pinned commit 649a17386, the requested note is absent. I searched `origin/main` and open refs `pr/10114`, `pr/10133`, `pr/10134`, `pr/10141` and `pr/10144` in the YM4D folder for the five model/topic combinations and found no direct result; PR 10134 had numeric gate artifacts with incidental matches only. The target folder's `open-registry.md` has no row for this literature task. Closest existing hit: `library/gap-crux-fp.md` §§1.1 and 3b.2, which states the same proposed tests but marks these figures GUIDE/RECALLED. The earlier gap-crux literature notes cover abstract-level Guth/Fröhlich–Spencer context, not the requested full theorem details. No duplicate attack or ownership row found.

## Scope and source state

The outline index was searched for the named authors and these model-specific transition claims. No transition-test statement was indexed. Its only Fröhlich hit is a different 1978 reflection-positivity paper (chunk 30, lines 206–209); therefore it is not evidence for the tests here. The fetched outline and account will be used only for source identification/context, not to discharge any proof step.

## (a) SU(2) Wilson in five dimensions

**Michael Creutz, “Confinement and the Critical Dimensionality of Space-Time,” Phys. Rev. Lett. 43 (1979), 553–556.** Full paper read from the author-hosted PDF; saved outside the checkout at `~/ym4d-papers/dl-2026-11-11/creutz-1979-5d/`.

Creutz used a periodic $4^5$ lattice for the five-dimensional run. He places the transition at $\beta_c=1.642\pm0.015$ in eq. (8), p. 555. The five-dimensional system crosses from a strong-coupling confining regime to a weak-coupling spin-wave regime. The two starts settle at different plaquette values in the extended runs, which he calls evidence for a first-order transition (pp. 555–556). The paper describes the weak regime as containing massless gauge bosons (p. 553); this is Monte Carlo evidence and interpretation, not a rigorous theorem.

**Comparison with gap-crux-fp.md:** its F15 GUIDE value “about 1.6” agrees with Creutz’s quoted estimate after rounding. Its description of the weak phase as massless agrees with the paper’s “spin-wave phase” / massless-gauge-boson language. The stronger order classification is supported by Creutz’s separate-start hysteresis evidence, with the paper itself carefully calling it indicative evidence. Later work is checked below.

**Later check: Francesco Knechtli, Magdalena Luz and Antonio Rago, “On the phase structure of five-dimensional SU(2) gauge theories with anisotropic couplings,” arXiv:1110.4210 (2011).** Full paper read. It uses the anisotropic Wilson plaquette action. Its isotropic review (Sec. 3, pp. 8–9) places the bulk first-order transition at $\beta_c\simeq1.64$ and describes the weak side as deconfined with vanishing string tension. Section 4.1, pp. 14–17, reports a first-order bulk transition line for the studied anisotropic couplings; the authors do not find the proposed second-order bulk point in their explored range. Section 4.3, pp. 21–24, calls the deconfined phase’s static potential five-dimensional Coulomb. This corroborates the transition/order and supports a Coulomb-like weak phase, but it is not an independent exact determination of Creutz’s isotropic coupling. Their simulations use finite lattices and numerical methods, so this is literature evidence only.

**Comparison with gap-crux-fp.md:** F15’s rounded coupling and first-order boundary are consistent. “Massless” is a fair description of Creutz’s spin-wave interpretation; the later paper’s more explicit observable is a five-dimensional Coulomb potential on the deconfined side. No mathematical proof step may rely on this simulation evidence.

## (b) SU(N) Wilson in four dimensions

**Michael Creutz, “Phase Transition in SU(5) Lattice Gauge Theory,” Phys. Rev. Lett. 46 (1981), 1441–1443.** Full three-page paper read from the author-hosted scan.

Creutz reports Monte Carlo evidence for a first-order transition for pure SU(5) with Wilson action in four dimensions (p. 1441). In his normalization the observed transition is $g_0^{-2}=1.66\pm0.03$ (p. 1442, eq. (6)); the action writes the Wilson coefficient as $2N/g_0^2$, so that is $\beta=2N/g_0^2$ in that convention. He says the behavior is clear for $N=5$ and “probably begins” at $N=4$ (p. 1441). The SU(4) evidence is explicitly weaker: his run suggests a transition, but it has smaller latent heat (p. 1443). He cites prior work as finding no similar transition in SU(2) or SU(3) (p. 1443).

**Comparison with gap-crux-fp.md:** F15’s GUIDE statement “SU(N) Wilson for $N\ge5$ has a first-order bulk transition” matches the clear SU(5) result and is appropriately narrower than Creutz’s tentative SU(4) indication. This paper alone does not establish a universal theorem for every $N\ge5$; Moriarty and later large-$N$ work follow.

**Michael Creutz and K. J. M. Moriarty, “Phase transition in SU(6) lattice gauge theory,” Phys. Rev. D 25 (1982), 1724–1726.** Full three-page paper read from Creutz’s author-hosted scan.

With the Wilson action, they see a clear first-order transition in pure SU(6) on a $4^4$ lattice, at their inverse-temperature convention $\beta_c=12/g_0^2=24.0\pm1.0$ (abstract, p. 1724; repeated p. 1725). Ordered and disordered starts approach distinct plaquette values at $\beta=24$, unlike the runs away from the transition (pp. 1724–1725). The authors say first-order transitions had been found in SU(4) and SU(5) and extend their analysis to SU(6) (p. 1724). They also caution that action modifications can create a spurious transition without changing the continuum physics (p. 1726).

**Comparison with gap-crux-fp.md:** F15’s $N\ge5$ GUIDE boundary is consistent with the observed SU(5) and SU(6) cases. This source confirms SU(6), not all higher ranks as a theorem; the 2005 Lucini–Teper–Wenger paper supplies later numerical coverage and a distinction between the weak SU(5) transition and robust $N\ge6$ transitions.

**Biagio Lucini, Michael Teper and Urs Wenger, “Properties of the deconfining phase transition in SU(N) gauge theories,” arXiv:hep-lat/0502003 (2005).** Full paper read from arXiv, including §10 (printed pp. 26–27).

This paper separates the finite-temperature deconfinement transition from the four-dimensional lattice bulk transition. In §10, it describes SU(2) and SU(3) as having a rapid strong/weak-coupling crossover, says that the crossover strengthens for SU(4), becomes weakly first order for SU(5), and is robustly first order for SU($N\ge6$). It reports bulk transition measurements for $5\le N\le12$ in Table 16. The authors note that for $N\ge6$ their observed hysteresis makes the location uncertain. This is numerical evidence, not a proof for all ranks.

**Comparison with gap-crux-fp.md:** F15’s GUIDE threshold $N\ge5$ agrees if read as “first order is observed beginning at SU(5).” Clarify the strength: SU(5) weakly first order; SU($N\ge6$) robustly first order; SU(4) is reported as crossover, despite Creutz’s earlier tentative first-order indication. The Lucini–Teper–Wenger abstract’s $N\ge4$ robust first-order claim is about *thermal deconfinement*, not this bulk transition; §10 is the relevant location for the present question.

## (c) Mixed fundamental-adjoint SU(2)

**Gyan Bhanot and Michael Creutz, “Variant actions and phase structure in lattice gauge theory,” Phys. Rev. D 24 (1981), 3212–3217.** Full six-page paper read from Creutz’s author-hosted scan.

Their normalized plaquette action is eq. (3), p. 3212: $S_P=\beta_F(1-\mathrm{Tr}U_P/2)+\beta_A(1-\mathrm{Tr}_A U_P/3)$, with $\mathrm{Tr}_A U=|\mathrm{Tr}U|^2-1$ (eq. (4), p. 3213). Their Monte Carlo phase diagram has a triple point near $(\beta_F,\beta_A)=(0.55\pm0.03,2.34\pm0.03)$ and a critical endpoint at $(1.48\pm0.05,0.90\pm0.03)$ (p. 3214). The paper describes the endpoint as where the first-order line terminates and the latent heats in the two plaquette observables vanish (p. 3214). The abstract likewise says the first-order lines merge at a triple point and continue to a critical endpoint.

The weight, up to a constant, is $w(x)=\exp\{\beta_Fx+\beta_A(4x^2-1)/3\}$ for $x=\mathrm{Tr}U/2\in[-1,1]$. Its derivative is $\beta_F+(8\beta_A/3)x$, so it is increasing throughout this interval when $\beta_A\le3\beta_F/8$. At the 1981 endpoint, $3\beta_F/8=0.555$ while $\beta_A=0.90$; the endpoint lies above the monotonicity boundary. These are hand calculations from the printed normalization, not a numerical proof step.

**Comparison with gap-crux-fp.md:** F15’s GUIDE endpoint $(1.5,0.9)$ agrees with Bhanot–Creutz’s $(1.48\pm0.05,0.90\pm0.03)$ after rounding. The monotonicity boundary cited in §3b.2 follows directly from their eqs. (3)–(4). A later endpoint determination is checked next because later literature quotes a visibly shifted location.

**Later check: Enrico Rinaldi, “Scaling properties of SU(2) gauge theory with mixed fundamental-adjoint action,” arXiv:1212.0635 (2012).** Full paper read from arXiv; downloaded outside the checkout to `~/ym4d-papers/dl-2026-11-11/rinaldi-lacagnina-2012-mixed/`.

This later study reports a first-order bulk line whose hysteresis weakens as the adjoint coupling decreases. In Sec. 2 (printed pp. 2–3), the authors estimate the line’s endpoint at approximately $\beta_{\rm adj}\lesssim1.25$; Fig. 3 places its neighborhood near $\beta_{\rm fund}\approx1.2$. They explicitly say their aim is to identify the endpoint’s neighborhood, not pin down its location precisely, and note the $\beta_{\rm adj}=1.25$ run has substantial uncertainty. This is a later, visibly shifted estimate from the 1981 coordinates, not a precise replacement or a consensus determination. The paper also flags that the endpoint’s nature had remained controversial.

**Comparison with gap-crux-fp.md:** the GUIDE value $(1.5,0.9)$ agrees with Bhanot–Creutz (1981), but not with the later paper’s approximate endpoint neighborhood near $(1.2,1.25)$. Record both as literature estimates with their dates and uncertainty. The monotonicity boundary $\beta_A=3\beta_F/8$ follows from the normalized action and is independent of which endpoint estimate is used; either quoted endpoint lies above that boundary. Neither estimate is a proof step.

## (d) U(1) Wilson in four dimensions and the rigorous Coulomb-phase results

**G. Arnold, Th. Lippert, K. Schilling and Th. Neuhaus, “Finite size scaling analysis of compact QED,” arXiv:hep-lat/0011058 (2000).** Full paper read from arXiv; saved outside the checkout at `~/ym4d-papers/dl-2026-11-11/compact-u1-2000-transition/`.

For the four-dimensional compact U(1) theory with the Wilson action, the authors quote the transition at $\beta_T=1.011128(11)$ (abstract and eq. (10), p. 4 in the proceedings pagination). They report evidence for a first-order transition, including a nonzero plaquette-energy gap, while noting the order had been debated and their finite-size analysis is evidence rather than a theorem. This is a later high-statistics estimate, not the Guth/Fröhlich–Spencer theorem’s coupling normalization.

**Comparison with gap-crux-fp.md:** the F-numbered GUIDE value near $\beta\simeq1.01$ agrees with this Wilson-action estimate. Do not identify it with Guth’s Villain coupling $g^2$.

**Alan H. Guth, “Existence proof of a nonconfining phase in four-dimensional U(1) lattice gauge theory,” Phys. Rev. D 21 (1980), 2291–2307.** The APS published abstract was read; the full article was **NOT READ**. The published abstract states that Guth proves a lower bound on the Wilson-loop expectation for a four-dimensional U(1) model with a Villain-form action, for $g^2<0.168$. The lower bound has Coulomb-interaction form, so it rules out electric-charge confinement in that range. It uses strong-coupling results to infer at least one phase transition. This is a different weight and coupling parameter from the Wilson-action Monte Carlo value $\beta_T\approx1.0111$. The full proof and any finer normalization details are NOT READ.

**Jürg Fröhlich and Thomas Spencer, “Massless phases and symmetry restoration in Abelian Gauge theories and spin systems,” Commun. Math. Phys. 83 (1982), 411–454.** The authors’ abstract was read; the full article and its theorem statements were **NOT READ**. The abstract says they give a proof of a deconfining transition to a massless QED phase in four-dimensional U(1) lattice gauge theory. It does not expose the action weight, a numerical coupling range, or a named correlation with a lower bound, so those requested details remain NOT READ and are not inferred here. Attempts to retrieve the institutional IHES scan yielded an HTML record and then a zero-page PDF; the author-upload link returned 404. Retrieval stopped there.

**Comparison with gap-crux-fp.md:** the broad claim that Guth and Fröhlich–Spencer establish a weak-coupling nonconfining/massless regime is consistent with their published abstracts. The exact Guth statement agrees on a Villain Wilson-loop lower bound for $g^2<0.168$. Any more specific Fröhlich–Spencer claim in the GUIDE text about action weight, numerical range, or correlation is not verified by the abstract and should not be repeated as established from this read.

## (e) Four-dimensional $\mathbb Z_2$ gauge theory

**Bhanot and Creutz (1981), already cited above.** Their four-dimensional pure $\mathbb Z_2$ Wilson gauge model has the self-dual coupling $\beta_{sd}=\tfrac12\log(1+\sqrt2)=0.4406868\ldots$ (eq. (7), p. 3213; the fixed point solves $\tanh\beta=e^{-2\beta}$). They identify a first-order transition there. The paper’s neighboring discussion says the first-order lines in the mixed-action phase diagram meet at a triple point and continue toward a critical endpoint; that mixed-action statement is separate from the pure-$\mathbb Z_2$ transition.

**Comparison with gap-crux-fp.md:** its rounded self-dual value $\beta\approx0.44$ and first-order classification agree with the cited equation and text. This is a statement about the discrete gauge model, not a proof input for the Yang–Mills task.
