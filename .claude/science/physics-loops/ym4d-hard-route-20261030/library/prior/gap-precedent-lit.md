# Repo search

**Writer:** Codex. FINISH assigns this Mini lane as gpt-6-luna, high; I cannot independently verify the runtime identifier. **Full-text read:** Kopper, arXiv:math-ph/9902020. This is a reading note only. It proves no new statement and grants no scientific status.

The lead's library/prior/repo-search-2026-11-08.md is a retroactive digest for FINISH row 531, not this literature question. It records searches of origin/main and PRs #10114, #10133, #10134, and #10141, but its target terms concern retained covariance, histories, and gauge admission. Its closest hit is S/MASS_GAP_LOCAL_BLOCK_ASTRA.md on #10114/#10133, lines 106–149. I fetched #10114 and read those lines. They prove a positive one-time-step plaquette correlation under stated one-link convolution hypotheses. That is a nontriviality witness, not exponential clustering or a positive spectral gap. The digest's hits do not cover this question.

The assigned task-specific library/prior/gap-precedent-lit.md did not exist. The registry has no separate owner for this reading question; FINISH row 736 is the assigned item. Nearby notes contain only partial source work: gap-crux-lit-nonab.md reports the Göpfert–Mack abstract; gap-crux-lit-cross.md identifies Kopper at abstract level and marks the other named papers unread; gap-crux-lit-2.md reports abstracts for Kupiainen, Kopper–Magnen–Rivasseau, and Brydges–Federbush. I did not treat those abstracts as proof readings.

## Outline context

The Sussman–Alpoge text is by Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text; I credit them for the indexed and cited outline material.

I used library/sa-index/README.md, searched the chunk files and obligations.md for gap, clustering, and correlation-length entries, read neighbouring rows in chunk-29.md, then read the cited outline lines. SA 31871–31882 gives a spectral-measure example with polynomially decaying correlations and support down to zero; it says a mass gap requires excluding a whole interval above vacuum. This only separates polynomial clustering from a gap. It does not supply any of the literature mechanisms below. The complete-account index README says its items 4.12–4.19 cover CA-I 42670–56650 and stage/RG arguments. Those items do not identify any of the nine assigned literature precedents. I fetched the outline and CA-I once each, as assigned; I make no claim from unread CA-I source passages.

**Scale and threshold values below are GUIDE.** Page and equation references identify source locations.

## 1. Göpfert and Mack, three-dimensional U(1)

**Read status:** NOT READ past the abstract. The DESY record download returned a bot-challenge page. I stopped at that challenge under the download rule. The repository's earlier note also records only the abstract.

(a) The DESY/INSPIRE abstract reports nonzero string tension for the 3D Villain U(1) model at every coupling, a lower bound in the weak-coupling regime, and a continuum limit at fixed Debye mass that is a free massive scalar. This is a confinement and screening statement; the abstract does not itself give the full correlation theorem or proof.

(b) The abstract defines m_D and says a→0 with m_D fixed. Thus 1/(a m_D)→∞ is the correlation-length/cutoff ratio for the stated continuum scaling. GUIDE. The explicit m_D formula is in the abstract, not a proof passage.

(c) The abstract identifies exact duality to a 3D integer ferromagnet/Coulomb system and Debye screening as the mechanism. The proof's small activity or screening estimate was not read.

(d) The abstract claims a continuum limit and discusses RG aspects. Whether its proof joins an ultraviolet flow to a separate infrared criterion is NOT READ.

(e) NOT READ. I cannot report whether the proof compares two sizes above a criterion threshold, or give a page/equation.

Source: [INSPIRE record for DESY 81/036](https://inspirehep.net/literature/166542), with the paper's bibliographic record and abstract. The full source is [Göpfert and Mack, Communications in Mathematical Physics 82 (1981), 545](https://doi.org/10.1007/BF01961240).

## 2. Kopper, large-N O(N) nonlinear sigma model

**Read status:** FULL TEXT, arXiv:math-ph/9902020, 44 pages. I read from the UV-regularized model setup through the cluster expansion and exponential-decay theorem.

(a) For a 2D Euclidean O(N) sigma model with UV cutoff set to 1, Kopper proves exponential decay of the infinite-volume two-point function for sufficiently large finite N. The model uses a softened quartic constraint with K of order 1. The theorem is p. 41, (171)–(177); the expansion and polymer criterion are §§4.1–4.5.

(b) The generated mass obeys m²=c_m exp(-4π/λ), with cutoff 1, (21), p. 8. The stated working interval is 2/π<λ<π, (22), p. 8. Hence the correlation length in cutoff units is 1/m, of order exp(2π/λ) up to c_m. This is of order 7 to 23 across that interval. GUIDE. The paper does not prove a parametrically unbounded ratio within this interval.

(c) The carrier is the large-N small factor in the cluster expansion. The introduction gives N^(-1/6)<c exp(-4π/λ), p. 4. The proof identifies a factor tending to zero with N for each cluster link, plus a factor exp(-N^(1/8)) per large-field square; see (120), (143), and (155)–(170), pp. 24, 31, 36–39. The sufficiency test is the polymer sum (143), not a comparison of partition functions at two box sizes.

(d) No UV RG flow is joined to an infrared criterion. The proof starts with a UV-regularized continuum model at fixed cutoff, controls its thermodynamic limit by cluster/Mayer expansions, then extracts exponential decay.

(e) No inequality between two system sizes above a criterion threshold appears in the proof read. The proof uses a fixed-cutoff polymer convergence condition (143) and tree-path convolution bounds (173)–(177), pp. 31, 40–41. These compare polymer sums and convolution kernels, not two volumes or two lattice sizes.

Source: [Kopper, arXiv:math-ph/9902020](https://arxiv.org/abs/math-ph/9902020).

## 3. Gawȩdzki and Kupiainen, hierarchical O(N) sigma model

**Read status:** NOT READ. The Springer PDF URL returned an HTML article page rather than the paper; no full text was opened.

(a) The bibliographic record identifies “Continuum Limit of the Hierarchical O(N) Nonlinear Sigma-Model,” CMP 106 (1986), 533–550. The theorem statement and whether it proves a gap or clustering are NOT READ.

(b) NOT READ.

(c) NOT READ.

(d) NOT READ.

(e) NOT READ; no page/equation can be supplied.

The title and citation are in Kopper's reference list, pp. 41–42. This is bibliographic context, not a reading of their proof.

## 4. Pordt and Reiss, hierarchical sigma model

**Read status:** NOT READ. My first Numdam URL returned 404. I did not find a readable full-text copy in the allowed locations.

(a) The identified paper is “On the renormalization group iteration of a two-dimensional hierarchical nonlinear sigma-model,” Annales de l'Institut Henri Poincaré 55 (1991), 545–587. Its theorem and gap/clustering claim are NOT READ.

(b) NOT READ.

(c) NOT READ.

(d) NOT READ.

(e) NOT READ; no page/equation can be supplied.

Kopper's reference list, p. 42, supplies the bibliographic pointer only.

## 5. Kopper, Magnen and Rivasseau, Gross–Neveu at large N

**Read status:** ABSTRACT ONLY. The Springer PDF endpoint returned an HTML access page. The earlier local literature note also has only the abstract.

(a) The abstract reports at least two pure phases for a 2D Euclidean Gross–Neveu model with discrete chiral symmetry, under suitable boundary conditions and a suitable UV cutoff, for sufficiently large but finite N; it reports exponential decay of the fermion two-point function.

(b) The abstract gives no mass-to-cutoff ratio or explicit N threshold. NOT STATED in the material read.

(c) The proof mechanism and exact small quantity are NOT READ. The abstract supports only the model and conclusion.

(d) NOT READ.

(e) NOT READ; no page/equation can be supplied.

Source: [Kopper, Magnen and Rivasseau, Communications in Mathematical Physics 169 (1995), 121–180](https://doi.org/10.1007/BF02101599).

## 6. Kupiainen, the 1/n expansion

**Read status:** ABSTRACT ONLY. The Springer full-text endpoint did not provide a PDF. Kopper's introduction also summarizes this source, but that is secondary evidence.

(a) The abstract says the lattice n-component nonlinear sigma model in arbitrary dimension has a mass gap above the spherical-model critical temperature for sufficiently large n.

(b) The abstract gives no correlation-length/lattice-spacing ratio or explicit n threshold. NOT STATED in the material read.

(c) The abstract points to the asymptotic 1/n expansion of correlation functions and free energy. Kopper's introduction says Kupiainen's gap proof uses reflection positivity/chessboard estimates and quotes N>c exp(50πβ) for d=2, p. 4. That threshold is GUIDE from Kopper's summary; the cited primary proof and equation (19) were not read.

(d) NOT READ. Kopper's summary describes a chessboard argument, not an ultraviolet-flow-to-infrared-criterion bridge.

(e) NOT READ; no primary page/equation was checked for a two-size inequality.

Source: [Kupiainen, Communications in Mathematical Physics 73 (1980), 273–294](https://doi.org/10.1007/BF01197703).

## 7. Ito and Tamura, CMP 202 (1999)

**Read status:** ABSTRACT only. The Kanazawa repository returned HTML instead of the PDF.

(a) The accessible abstract is “N Dependence of Upper Bounds of Critical Temperatures of 2D O(N) Spin Models.” It says that if a phase transition exists for large N, its critical inverse temperature obeys a lower bound proportional to N log N. This is not itself a proved mass-gap or exponential-clustering result.

(b) No correlation length or gap ratio is given.

(c) The bound concerns the possible transition temperature; it is not a displayed gap criterion. Proof details NOT READ.

(d) NOT READ.

(e) NOT READ; no proof page/equation was available.

Source: [Kanazawa University repository record](https://kanazawa-u.repo.nii.ac.jp/record/10102).

## 8. Ito on Migdal–Kadanoff models (CMP 95 (1984); PRL 55 (1985))

**Read status:** The 1984 article was NOT READ. The APS abstract for the 1985 Letter was read; its PDF was not obtained.

(a) The 1984 bibliographic record identifies “Analytic studies of the Migdal–Kadanoff recursion formula,” CMP 95 (1984), 247–255. The 1985 APS abstract states permanent quark confinement for 4D hierarchical lattice gauge theories in which Migdal–Kadanoff recursion formulas hold exactly. This is not, from the abstract alone, an exponential correlation-decay or spectral-gap theorem.

(b) NOT STATED in the readable abstracts. No correlation-length ratio was found.

(c) The 1985 abstract names exact Migdal–Kadanoff recursion as the mechanism. Details and the 1984 paper's contribution are NOT READ.

(d) The exact recursion iterates across hierarchical scales, per the abstract; whether that constitutes an ultraviolet flow joined to a separate infrared criterion is NOT READ.

(e) NOT READ. The abstract does not provide a two-size inequality, threshold, page, or equation.

Sources: [1985 APS record](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.55.558); the 1984 bibliographic record lists the paper and pages at [EurekaMag](https://bastion.eurekamag.com/research/074/057/074057110.php).

## 9. Brydges and Federbush, Debye screening

**Read status:** ABSTRACT ONLY. The University of Michigan PDF endpoint returned HTTP 503; the Springer PDF endpoint returned HTML. The earlier local note also records only the abstract.

(a) The abstract reports existence and exponential clustering for correlations of a classical Coulomb system at low density or high temperature. It attributes the proof to constructive QFT methods, the sine-Gordon transformation, and the Glimm–Jaffe–Spencer expansion about mean field.

(b) There is no lattice spacing in the stated continuum Coulomb system. A screening length is relevant, but its ratio to a lattice spacing/cutoff is NOT APPLICABLE as stated.

(c) The abstract names low density/high temperature and the transformed cluster expansion. The exact small activity and convergence inequalities are NOT READ.

(d) No ultraviolet RG-to-infrared criterion is identified in the abstract; full proof NOT READ.

(e) NOT READ; no page/equation can be supplied.

Source: [Brydges and Federbush, Communications in Mathematical Physics 73 (1980), 197–246](https://doi.org/10.1007/BF01197700).

RESULT (2026-11-11): Partial source reading; only Kopper (math-ph/9902020) read in full; the four means cannot be compared across this read set, and the above-threshold two-size test remains unresolved. B4 not established; no audit or status granted.

