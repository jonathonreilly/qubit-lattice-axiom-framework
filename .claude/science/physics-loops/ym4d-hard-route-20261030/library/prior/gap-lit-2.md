# Mass-gap literature, second reading

Reading note for FINISH row 661, 2026-11-10. Literature report only: no proof, audit, or status is claimed. The quotations below are short extracts from the pages listed. A missing detail is marked “not stated” or “not read”; I do not fill it in from memory.

## Repo search

The task's named `library/prior/repo-search-2026-11-08.md` is absent in this checkout, and row 661 of `FINISH.md` contains no separate “Repo prior work” lines. The neighboring `library/prior/gap-prior.md` records the closest earlier repo scan: it reports that the SU(2) one-step positive plaquette-correlation result in PR #10114 is fixed-spacing and is not a gap bound; the crossover and aligned-response work leave physical crossover and continuum gap open. I reuse that as a report of the earlier search, not as primary evidence.

I fetched `origin/main` at `bf92a1d763030836ed55631d5d7a7ef3b288f284` and the available open-PR refs #10114, #10133, #10134, #10141, and #10144. I attempted a scoped `git grep` for “mass gap”, “spectral gap”, small volume, vortex free energy, Tomboulis–Yaffe, Mack–Petkova, and Gross–Neveu; it returned no hits before the PR #10114 read stalled at the command limit, so this is not a complete clean search result. The source task itself does not provide the lead's branch/file hits. The earlier `gap-prior.md` is the closer repo result: conditional finite-model gaps and one-step response estimates, but no uniform physical-scale continuum gap. I did not find another repo result that covers this literature-reading row.

## Outline and account boundary

The full-read SA index was used first: `library/sa-index/README.md`, the relevant rows in `chunk-01.md`, and the specified `ca-4.12-4.19/README.md` and matching chunks. The outline and CA-I were already present at the prescribed paths, with 32,992 and 166,711 lines respectively; I did not fetch duplicates. The bounded outline excerpts read were `/tmp/sa_ym4.tex` lines 66–130, 588–599, and 766–779. Theorem 0 states a volume-first subsequential continuum limit for four-dimensional Wilson SU(2), for the `tr(F^2)` sector, with the listed OS axioms and clustering. Lines 588–599 give a polynomially decaying spectral example whose support reaches zero; lines 766–779 prove a scalar block-constrained estimate and expressly distinguish it from a physical Hamiltonian gap. These are Ethan Sussman and Levent Alpoge's text, authored with Claude and Codex; credit all four for any use of the outline/account.

The CA-I item 4.12–4.19 index concerns RG stages and localized bounds, not a physical mass-gap theorem. Its README points to CA-I 49,495–49,546 for application conditions outside an operator theorem and 54,986 onward for a preparatory-boundary theorem that assumes Balaban's stage theorem. This is technical construction material, not evidence of exponential decay for the full physical measure.

## 1. Small volume

**M. Lüscher, “Some analytic results concerning the mass spectrum of Yang-Mills gauge theories on a torus” (1983).** The arXiv API title/author search returned no relevant item. Crossref identified DOI `10.1016/0550-3213(83)90436-4`; the DOI URL `https://doi.org/10.1016/0550-3213(83)90436-4` returned a redirect page rather than an abstract, so I stopped there. Identifier/abstract page: **not found**. The theorem statement, group, dimension, torus volume, coupling range and observables are **not read**. The page read does not establish a proved spectral gap.

**B. van Baal, “QCD in a finite volume.”** The title/author arXiv API query did not identify the paper; the follow-up API request was refused with HTTP 429. The journal DOI URL tried, `https://doi.org/10.1016/0370-1573(86)90029-0`, returned HTTP 404. Identifier/abstract page: **not found**. The theorem and its group, dimension, volume, coupling and observables are **not read**.

The additional arXiv API search for a theorem proving a Yang–Mills Hamiltonian or transfer-matrix gap on a small torus returned no matching theorem; its five results were unrelated or did not state such a result. I found no proof source in the pages read. Perturbative finite-volume spectra are not counted as a proof of a spectral gap. A rigorous theorem of the requested small-torus type: **not found in this search**.

## 2. Chatterjee, “Yang-Mills for probabilists”

Sourav Chatterjee, arXiv:1803.01950. API title query found this identifier. Read the abstract and HTML: [abstract](https://arxiv.org/abs/1803.01950), [HTML](https://arxiv.org/html/1803.01950). The article presents the following three open problems:

- Problem 4.1 (area law): for compact non-Abelian Lie `G ⊆ U(N)`, `N ≥ 2`, any infinite-volume limit of four-dimensional lattice gauge theory at inverse coupling `β`, prove `|E W_{γR,T}| ≤ C(β)e^{-c(β)RT}` for rectangular loops, with positive constants depending only on `β,G`. It says the large-`β` four-dimensional non-Abelian case remains elusive.
- Problem 5.1 (mass gap): for the same stated group/dimension and any infinite-volume limit at `β`, let `f_β(x)` be the connected correlation of the plaquette nearest 0 and the plaquette nearest `x`. The exact requested limit is `lim_{|x|→∞} log f_β(x)/|x| = −1/ξ(β)` for some `ξ(β)∈(0,∞)` for every `β>0`, and also `lim_{β→∞} ξ(β)=∞`. The text interprets `ξ` as reciprocal lightest glueball mass. The page calls it a problem, not a theorem.
- Problem 5.2 (continuum limit): for a compact non-Abelian `G ⊆ U(N)`, `N≥2`, in an infinite-volume limit of four-dimensional lattice gauge theory, as `β→∞`, find `ε(β)→0`, `c(β)→∞` and nonzero `d` such that for all rectangular side lengths `R,T`, `log E W_{γ_{R/ε,T/ε}} = −c(R+T)−dRT+o(1)`. The paper says this is unproved and explicitly says it is unclear whether the perimeter renormalization term is necessary.

No additional open problems are listed under the article's “Problem” headings. The paper does not give a theorem solving these problems. It describes the mass-gap definition through this plaquette-correlation limit; this is its lattice formulation, not a continuum OS mass-gap theorem.

## 3. Chatterjee, “A probabilistic mechanism for quark confinement”

Sourav Chatterjee, arXiv:2006.16229. API title query found it. Read the abstract and HTML: [abstract](https://arxiv.org/abs/2006.16229), [HTML](https://arxiv.org/html/2006.16229). In §2.4, Definition 2.3, the hypothesis called for in this task the “strong mass gap” is exponential decay under **arbitrary boundary conditions**: for every finite cube, every boundary condition, and bounded local edge functions `f,g` with values in `[-1,1]`, there are `K1,K2>0` depending only on `G,β,d` such that `|E(fg)−Ef Eg| ≤ K1 exp(−K2 dist(f,g))`. The constants do not depend on the cube or boundary condition.

Theorem 2.4 says that this hypothesis implies unbroken center symmetry; if a finite-dimensional irreducible representation acts nontrivially on the center, every infinite-lattice Gibbs measure satisfies Wilson's area law for rectangular loops. The setting is pure lattice gauge theory on `Z^d` with a compact matrix group, fixed `β`, and a nontrivial center for the area-law conclusion; the result has no continuum limit. The article's abstract states the sufficient condition as nontrivial group center plus exponential decay under arbitrary boundary conditions. The paper says area law at weak coupling above dimension two remains largely open, especially four-dimensional SU(3); it also notes the conjectured large-`β` decay may not include this strong, all-boundary-condition form. No finite-volume theorem is turned into a continuum gap here.

## 4. Adhikari and Cao, weak-coupling correlation decay

Arka Adhikari and Sky Cao, arXiv:2202.10375. API title query found it. Read the abstract and HTML: [abstract](https://arxiv.org/abs/2202.10375), [HTML](https://arxiv.org/html/2202.10375). Theorem 1.1 is for a **finite group** `G`, in four dimensions, on finite rectangular boxes `Λ ⊂ Z^4`, at inverse coupling `β ≥ Δ_G^{-1}(114+4 log|G|)` (with `Δ_G` defined in the paper). For conjugacy-invariant functions of finitely many Wilson loops supported in disjoint rectangles, it bounds the covariance by a support-size prefactor times `exp(−(β/2)Δ_G(L−1))`, where `L` is their separation. The exponential rate is uniform in box size and the observables for fixed supports; the prefactor grows exponentially in the total rectangle volume. This is a high-`β`, weak-coupling lattice theorem, not a continuum result and not a Lie-group theorem. The introduction says the general four-dimensional non-Abelian Lie-group decay problem is open; the paper does not state another open problem specific to its finite-group result.

## 5. Tomboulis and Ito–Seiler

**E. T. Tomboulis, “Confinement for all values of the coupling in four-dimensional SU(2) gauge theory,”** arXiv:0707.2179. The API title/author search found the source. Read the abstract and HTML: [abstract](https://arxiv.org/abs/0707.2179), [HTML](https://arxiv.org/html/0707.2179). Its abstract claims a derivation “from first principles” that SU(2) is confining for `0<g<∞`, lattice spacing `a` as UV regulator, and spacetime dimension `d≤4`, using approximate RG decimations and an exact interpolation of partition-function bounds. This is a claim about confinement/vortex free energy, not a theorem of continuum mass gap. The abstract does not specify a continuum limit or local correlation observable. The paper's later discussion associates an area-dependent vortex free-energy behavior with flux spreading and mass-gap creation, but it does not state a proved continuum mass-gap theorem. Its claim is disputed in the next paper.

**K. R. Ito and E. Seiler, “On the recent paper on quark confinement by Tomboulis,”** arXiv:0711.4930. Read the abstract and HTML: [abstract](https://arxiv.org/abs/0711.4930), [HTML](https://arxiv.org/html/0711.4930). They say Tomboulis's argument relies on an unproved claim. Their specific obstruction is the asserted inequality `A(α)>A⁺(α)` for large `β`, which they say is shown only when character coefficients are small and the high-temperature expansion converges. Their §3 calculation says the implicit-function continuation can fail because `Ψ_t(λ,t)=0` at an intermediate `λ`; thus the claimed solution need not continue to the endpoint. Their conclusion is that the confinement proof has not been established by the stated argument, not a counterexample to confinement. Tomboulis's reply and two later Ito–Seiler discussions were also fetched as HTML (`0712.2620`, `0803.3019`, `0901.4246`) for context; they are follow-up debate, not independent proof. No mass-gap theorem was found in them.

## 6. Tomboulis–Yaffe and Borgs–Seiler

**Tomboulis and Yaffe (1985), “Finite temperature SU(2) lattice gauge theory.”** Read Springer abstract at [DOI](https://doi.org/10.1007/BF01206134), identified by the arXiv title search only as a non-arXiv paper. The abstract says the paper proves absence of confinement at sufficiently high temperature in pure SU(2) lattice gauge theory, and absence of spontaneous chiral symmetry breaking at sufficiently high temperature with massless fundamental fermions. It does not state a vortex-free-energy/Wilson-loop inequality. Exact theorem, coupling/volume range and that inequality: **not read/not found on the abstract page**.

**Borgs and Seiler (1983), “Lattice Yang-Mills theory at nonzero temperature and the confinement problem.”** Read Springer abstract at [DOI](https://doi.org/10.1007/BF01208780). The abstract says they clarify relationships among Wilson, Polyakov and ’t Hooft confinement criteria by a string of inequalities between string tensions, and establish upper and lower bounds on a critical coupling, including a weak-coupling nonconfining regime at nonzero temperature in three or more space dimensions. The abstract does not give the exact vortex-free-energy/Wilson-loop inequality. Exact formula, its hypotheses and full theorem: **not found on the abstract page; full article not read**. I do not reconstruct either requested inequality from memory.

## 7. Mack and Petkova

G. Mack and V. B. Petkova (1979), “Comparison of lattice gauge theories with gauge groups Z2 and SU(2).” Crossref identified two DOI records, but the two ScienceDirect DOI requests (`10.1016/0003-4916(79)90276-8` and `...90346-4`) returned redirect pages, not abstracts; the arXiv API title search found no paper. The article's exact sufficient condition, theorem, volume, and coupling range are **not read**. Chatterjee 2018 cites older work for strong-coupling area law, but that is not a substitute for Mack–Petkova's condition. Sufficient condition: **not found**.

## 8. Magnen, Rivasseau and Sénéor

Jacques Magnen, Vincent Rivasseau and Roland Sénéor (1993), “Construction of YM4 with an infrared cutoff,” DOI `10.1007/BF02097397`. Read Springer abstract at [DOI](https://doi.org/10.1007/BF02097397); API title search did not identify an arXiv version. The abstract's exact scope is a construction basis for Schwinger functions of pure four-dimensional SU(2) Yang–Mills, trivial topological sector, fixed infrared cutoff and no ultraviolet cutoff, in regularized axial gauge; it says the combined small-field and gauge-restoring-counterterm effect is stabilizing for certain momentum cutoffs and Slavnov identities hold nonperturbatively. The fixed infrared cutoff is retained, so removal of that cutoff / an infinite-volume mass-gap statement is not claimed in the abstract. Coupling range and detailed observables: **not stated in the abstract**. The paper's exact open-problem list: **not stated in the abstract; full text not read**.

## 9. Balaban: ultraviolet stability versus full-measure decay

The local-paper set was read from `/Users/jonBridger/ym4d-papers/README.txt`. The formulas in the OCR of CMP 119 were checked against the corresponding PDF scan, rendered at `/tmp/gap-lit-2/pages/balaban119-p22.png`.

Balaban's CMP 119 (1988), “Convergent renormalization expansions for lattice gauge theories,” Corollary 3 (Ultraviolet Stability), p. 264, states under Theorem 1's assumptions that constants `E_-`,`E_+`, independent of the lattice mesh `η` and torus `T` but depending on the running coupling `g_k`, give

`χ_k(T_η) exp[−g_k^(−2) A(U_k(V_k)) − E_- |T_η|] ≤ ρ_k(V_k) ≤ exp[E_+ |T_η|]`.

This is the effective density on the periodic lattice/torus `T_η`, with a volume-exponential lower and upper bound uniform in mesh and torus size under the stated RG hypotheses. It is an ultraviolet-stability bound, not decay of correlations of the full measure. CMP 109 (1987), Theorem 1, separately gives small-field effective-action bounds in dimension four for SU(2), with the running coupling constrained to a sufficiently small interval; it says the corresponding coupling trajectory theorem is a separate result. The other permitted local Balaban papers are listed in the README, but I did not extract a stronger physical gap theorem from them.

In the local texts inspected, propagator, constrained Gaussian, and RG-kernel exponential decay are auxiliary estimates. **No statement of exponential decay of correlations of the full Yang–Mills measure was found.** The final ultraviolet-stability statement above does not imply one.

## 10. Functional inequalities and conditional continuum-gap implications

The earlier note `library/prior/gap-lit.md` read Hao Shen, Rongchan Zhu and Xiangchan Zhu, arXiv:2204.12737: their abstract states Log-Sobolev and Poincaré inequalities plus exponential correlation decay and a positive gap for lattice SU(N) when `|β|<1/[16(d−1)]`, `d>1`, and for SO(N) when `|β|<(N−2)/[32(d−1)N]`. This is the strong-coupling side in the usual Wilson inverse-coupling convention. It is not a continuum-limit theorem.

The weak-coupling finite-group result of Adhikari–Cao above proves decay for a finite group, but states no Poincaré/Log-Sobolev inequality or Dobrushin uniqueness conclusion. The other fetched papers did not supply such an inequality outside the strong-coupling range. A theorem of that requested functional-inequality type: **not found in the sources read**.

No source read gives a single-scale hypothesis implying a four-dimensional non-Abelian continuum mass gap. The Gross–Neveu comparison requested in the task is C. Kopper, J. Magnen and V. Rivasseau (1995), “Mass generation in the large N Gross-Neveu-Model,” [Springer DOI](https://doi.org/10.1007/BF02101599), whose abstract I read. It says that for a large but finite number of fermion components, with a suitable ultraviolet cutoff and discrete chiral symmetry, there are at least two pure phases under suitable boundary conditions and the fermion two-point function decays exponentially. The abstract does not state an explicit one-scale hypothesis, a continuum-removal statement, or a numerical coupling range; those details and any open-problem discussion are **not stated in the abstract/full text not read**. This is a lower-dimensional asymptotically-free comparison result, not a bridge theorem for YM4.

For the two-dimensional O(N) sigma model, no primary theorem page was found or read in this pass. Its exact continuum mass-gap status is **not assessed here**; I make no memory-based claim.

## Regime table

| Regime | Group | What is proved or claimed in the source read | Source/read status |
|---|---|---|---|
| Small-volume torus | SU(N) in Lüscher; QCD group in van Baal title | No proof of a small-torus Hamiltonian/transfer spectral gap found; detailed spectra not read | Lüscher DOI redirect; van Baal identifier/page not found |
| Infinite-volume lattice, arbitrary β | Compact non-Abelian `G⊆U(N)`, d=4 | Chatterjee states mass-gap and continuum-limit problems for Wilson-loop/plaquette correlations | arXiv:1803.01950 abstract + HTML read; problems not solved |
| Fixed-coupling lattice, all boundary conditions | Compact matrix `G`, `Z^d` | Strong mass-gap condition implies unbroken center; with nontrivial center, area law for suitable Wilson loops | arXiv:2006.16229 abstract + HTML read |
| Weak coupling, finite lattice group | Finite `G`, d=4 | Uniform-in-box exponential covariance rate for separated Wilson-loop functions, with support-size prefactor | arXiv:2202.10375 abstract + HTML read |
| All-coupling confinement claim | SU(2), d≤4, fixed lattice spacing | Tomboulis claims confinement for `0<g<∞`; Ito–Seiler identify an unproved large-β inequality / failed continuation step | arXiv:0707.2179 and 0711.4930 abstracts + HTML read; claim disputed |
| Nonzero temperature | SU(2) (Tomboulis–Yaffe); lattice Yang–Mills (Borgs–Seiler) | Abstracts report high-temperature nonconfinement and inequalities among string tensions; requested vortex/Wilson inequality not found | Springer abstracts read; full statements not read |
| Gauge-group comparison | Z2 and SU(2) | Mack–Petkova sufficient condition not recovered | DOI redirects; not read |
| Continuum construction with fixed IR cutoff | SU(2), d=4, trivial topological sector | Schwinger-function construction basis with fixed IR cutoff and no UV cutoff | Springer abstract read; no IR-cutoff removal claim |
| Ultraviolet stability | Balaban RG on periodic `T_η`; CMP 119 assumptions | Effective-density bounds uniform in mesh and torus size, volume-exponential | CMP 119 Corollary 3 PDF page read; not full-measure correlation decay |
| Strong-coupling lattice gap | SU(N), SO(N), d>1 | LSI/Poincaré and exponential decay in explicit small-β ranges | arXiv:2204.12737 abstract read in prior `gap-lit.md`; no continuum limit |
| Weak-coupling functional inequality outside that range | Not identified | No qualifying LSI/Poincaré/Dobrushin theorem found in the read sources | Not found in this search |
| Lower-dimensional asymptotically-free comparison | Gross–Neveu, large finite N | With suitable UV cutoff: at least two pure phases and exponential fermion two-point decay | Springer abstract read; continuum removal / one-scale implication not stated |
| Two-dimensional O(N) sigma-model continuum gap | O(N) | No conclusion reported | Not read |
