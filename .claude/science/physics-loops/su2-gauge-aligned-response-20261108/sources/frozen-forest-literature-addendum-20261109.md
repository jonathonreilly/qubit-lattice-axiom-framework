# Frozen covariance and forest literature addendum (2026-11-09)

## Scope and source coverage

This is a bounded literature comparison for the proposed SU(2) connected-response construction. I read the full local `connected-response-literature-scan-20261109.md` and the complete section 11 (“Scope, primary comparisons and remaining interfaces”) of Git revision `89faef229ff6e6bde42baad15ed8270c2f4087d8:.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MARKED_COMPACT_CHART_ASTRA.md`. The primary-source checks below cover the relevant Gaussian example in Abdesselam–Rivasseau section V.A, Lohmann’s theorem and cutoff scope, and the Clay Mathematics Institute’s current problem page. These are source-scope comparisons, not independent verification of the local construction.

## Abdesselam–Rivasseau: forest formula and Gaussian example

**Identity.** Abdelmalek Abdesselam and Vincent Rivasseau, “Trees, forests and jungles: a botanical garden for cluster expansions,” arXiv:hep-th/9409094v1, posted 16 September 1994; published in *Constructive Physics*, Lecture Notes in Physics 446 (1995), pp. 7–36. [arXiv primary text](https://arxiv.org/html/hep-th/9409094v1) · [arXiv record](https://arxiv.org/abs/hep-th/9409094).

Section II gives the Brydges–Kennedy forest formula for a function of pair variables, with forest edges carrying derivatives and the interpolation parameter on a non-forest pair given by the minimum parameter along its forest path. Section V.A applies a Taylor forest formula to a massive free bosonic Gaussian measure perturbed by an interaction such as \(e^{-g\int_\Lambda\phi^4}\). The interpolated object is the covariance; differentiation with respect to a covariance interpolation parameter is evaluated by Gaussian integration by parts, producing paired field derivatives acting on the interaction. The resulting terms integrate against normalized Gaussian measures with positive interpolated covariances and factor over forest components (V.A.5–V.A.9).

**Relation and boundary.** This is direct architectural precedent for forest interpolation and positive Gaussian covariance interpolation. In the cited Gaussian example, the forest derivatives act on the interaction through Gaussian integration by parts. The local proposed route instead freezes the Gaussian covariance and differentiates its normalized density under a covariance-parameter heat identity, while retaining potentially merely measurable insertions unchanged. Therefore Abdesselam–Rivasseau supports the forest architecture, but does not automatically supply that frozen-covariance density identity, its insertion regularity, or the full compact SU(2) fourth-response estimate.

## Lohmann: theorem scope and compact measurable insertions

**Identity.** Martin Lohmann, “Single Scale Cluster Expansions with Applications to Many Boson and Unbounded Spin Systems,” arXiv:1411.1107v1, posted 4 November 2014. [arXiv primary text](https://arxiv.org/html/1411.1107v1) · [arXiv record](https://arxiv.org/abs/1411.1107).

Theorem 1 treats a finite site set with a massive (possibly complex) Gaussian covariance and quantitatively controlled analytic local and pair interactions. Its generating function includes a cutoff \(\chi_R\) that is a product of single-site cutoffs; the paper explicitly notes that its result does not apply to more general characteristic functions (Theorem 1 and the discussion at HTML lines 190–207, especially 207). The framework also discusses parameter derivatives of Gaussian integrals and weak differentiation of characteristic functions in the particular local cutoff setting. That does not establish a general theorem for arbitrary compact measurable insertions: those would need to meet the stated locality, field-analyticity/activity, and derivative or weak-derivative bounds of the applicable result.

**Relation and boundary.** Lohmann supplies relevant Gaussian forest and cluster-expansion machinery under explicit Euclidean covariance, interaction, cutoff, and norm hypotheses. The SU(2) proposal’s point is to keep the insertion fixed and measurable and place the derivatives on the normalized Gaussian density. Thus a theorem requiring analytic interactions or a product of single-site cutoffs cannot be applied to the full compact-group insertion merely because it is measurable or compactly supported. Whether any particular insertion can be represented in Lohmann’s admissible class is a separate hypothesis check.

## Clay Mathematics Institute status

The Clay Mathematics Institute’s official page labels “Yang-Mills & the Mass Gap” **Unsolved** and states that no proof of the mass-gap property is known. [Official CMI problem page](https://www.claymath.org/millennium/yang-mills-the-maths-gap/). This current status is context only; the bounded forest-literature check supplies no evidence of progress toward solving the Clay problem.

## Naming and inference notes

The local section 11 calls the source “Abdesselam–Rivasseau” and links the right arXiv identifier. Its formal arXiv title is *Trees, forests and jungles: a botanical garden for cluster expansions*; the “explicit large versus small field multiscale cluster expansion” title sometimes associated with these authors is a different later work. For Lohmann, the local note’s title and author match the arXiv record. “Frozen covariance, differentiated normalized density” is the local construction’s described architecture; the comparison above does not certify that identity or its estimates, and makes no novelty or correctness claim.
