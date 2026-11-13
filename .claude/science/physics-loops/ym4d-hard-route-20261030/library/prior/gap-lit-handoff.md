# Literature hand-off: Dobrushin openness and torus defects

## Repo search

**Terms:** `Dobrushin`, `Dobrushin-Shlosman`, `block Dobrushin`, `many-body perturbation`, `cluster-expansion regime`, `block-spin hand-off`, `free-energy defect`, `torus defect`, and `gap-handoff`.

**Refs searched:** `origin/main`, `pr/10114`, `pr/10133`, `pr/10134`, and `pr/10141` in `/Users/jonreilly/Projects/Physics`, for `*.md` and `*.tex`, with bounded `git grep` commands piped to `head`. The 2026-11-08 repo-search note is absent. The targeted search for `gap-handoff`, `free-energy defect`, `torus ... free energy`, many-body Dobrushin perturbations, or an effective-action hand-off returned no matches.

**Relevant hit (same blob on all five refs):** `archive_unlanded/historic_intake_originals/branch04/1129_MASSIVE_WILSON_STAGGERED_DOBRUSHIN_SPATIAL_UNIQUENESS_WEDGE_BOUNDED_THEOREM_NOTE_2026-07-12.md`, lines 154–160, 223, 261, 351–354, and 403–410. It states that a per-link influence row sum below one gives a unique DLR state and boundary convergence, while a weighted row sum below one gives exponential boundary influence and covariance decay; its model-specific work bounds the Wilson/rooted-loop influences. It gives an explicit sufficient wedge for a massive Wilson–staggered model. Its own scope table says the Dobrushin–Shlosman block route has no optimized block bound. This is a distinct matter-coupled model and does not state openness under general many-body perturbations, an RG landing theorem, or a free-energy comparison between tori.

**Other relevant hit:** the archived compact Dobrushin subwedge note, in `archive_unlanded/historic_intake_originals/branch01/251_COMPACT_DOBRUSHIN_SUBWEDGE_SEPARATED_POINT_ULTRALOCAL_CONTINUUM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-12.md:198–200, 248, 293`, records a strict Dobrushin interior, says the block criterion was attempted without an optimized block computation, and explicitly keeps the one-link-failure/block-criterion distinction. It is an in-repository Wilson–staggered result and does not cover the requested perturbative openness or hand-off.

**Lane prior work / ownership:** `library/prior/gap-lit-handoff.md` and `library/prior/repo-search-2026-11-08.md` were absent at the specified paths before this file was created. `library/open-registry.md` has no `gap-handoff`, `gap-lit-handoff`, or `EXIT` entry. FINISH rows 846 and 850 own the hand-off theorem and its check; row 851 is the distinct literature follow-up. Existing `library/prior/gap-crux-lit-2.md` sections F1–F2 already record Dobrushin–Shlosman, Stroock–Zegarlinski, Martinelli–Olivieri, and comparison theorems, with no verified compact SU(2) plaquette criterion. I use those as prior work and do not repeat their generic criterion summaries.

## Scope and findings

Completed bounded comparison of the three claims in `library/gap-handoff-opus.md` §§1–3 against published sources. The source's own checkpoint (§0) says no literature search was run and that openness was recalled rather than sourced. No scientific claim or lane status is changed by this reading.

## 1. Perturbative openness of uniqueness conditions

### S. Usuki (2023): an explicit Dobrushin radius for Ising interactions

**Source:** Shunsuke Usuki, “Stability of Uniqueness and Coexistence of Equilibrium States of the Ising Model under Long Range Perturbations,” *Osaka Journal of Mathematics* 60(4) (2023), 733–752, [published article and PDF](https://doi.org/10.18910/93057).

**Exact result:** Theorem 1.3(1) says that for every dimension $d\ge2$ there are $0<\beta_h<\beta_c$ and $\delta>0$ such that if $0<\beta\le\beta_h$ and $\Psi$ is translation invariant with the paper’s $d$th-order decaying norm $|||\Psi|||<\delta$, then $\Phi_\beta+\Psi$ has a unique Gibbs state. Proposition 2.4 gives the explicit sufficient Dobrushin condition $\|\Phi\|_{\rm var}<2$; equation (2.2) gives $\|\Psi\|_{\rm var}\le2|||\Psi|||$, and the nearest-neighbor Ising interaction has $\|\Phi_\beta\|_{\rm var}=4d\beta$. Thus the paper’s own estimates yield the concrete sufficient radius

$|||\Psi||| < 1-2d\beta, \quad 0<\beta<1/(2d)$.

This applies to arbitrary translation-invariant many-body perturbations in that decaying norm; it is a high-temperature finite-state Ising theorem. The theorem statement itself packages the smallness as existence of $\beta_h,\delta$; the displayed radius is the direct arithmetic consequence of its Proposition 2.4 and norm bounds. It does not cover compact Lie-group link variables, gauge-invariant plaquette interactions, or a block criterion. **Closeness: strong for the general “uniqueness is open under many-body perturbation” question and an explicit radius; limited model match.**

### Dobrushin–Shlosman block conditions

The previously recorded Dobrushin–Shlosman finite-volume criterion is a strict finite-box influence inequality: a suitable box condition implies uniqueness. The source review already in `library/prior/gap-crux-lit-2.md` records its finite-state Kantorovich form and its scope. The sources read for this item did not supply an explicit perturbation radius for the Dobrushin–Shlosman box criterion in a many-body compact-gauge norm. A strict finite-dimensional inequality may be stable by continuity, but that observation is not the cited theorem or a gauge-theory estimate. **Closeness: general qualitative openness is standard; an explicit gauge or block-Dobrushin radius was not located.**

## 2. RG hand-off to a mixing or cluster-expansion regime

### T. Balaban (1988): pure lattice-gauge small-field RG

**Source:** Tadeusz Balaban, “Renormalization group approach to lattice gauge field theories. II. Cluster expansions,” *Communications in Mathematical Physics* 116 (1988), 1–22, [publisher record and abstract](https://doi.org/10.1007/BF01239022).

**Exact result stated by the publisher:** The paper represents the fluctuation-field integral by an exponentiated cluster expansion, proves that its terms satisfy the inductive assumptions, and thereby completes the sequence of effective actions **in the small-field approximation**. That is a real multiscale gauge-theory cluster-expansion result. The stated endpoint remains Balaban’s inductive small-field class; it does not say that the effective action becomes a global Gibbs density in a Dobrushin or Dobrushin–Shlosman region, does not give a perturbative openness radius for such a region, and does not state the requested comparison of free energies on two tori. The lane’s `lit-balaban.md` table (unchecked against Balaban’s papers, but mapped through the account) likewise identifies the RG/R-operation sequence and explicitly records several printed-without-proof inputs. **Closeness: direct gauge RG and cluster expansion, but not the proposed global landing criterion or defect comparison.**

### D. Brydges, J. Dimock, T. R. Hurd (1998): iteratable scalar-field RG estimates

**Source:** “Estimates on Renormalization Group Transformations,” *Canadian Journal of Mathematics* 50(4) (1998), 756–793, [article and DOI](https://doi.org/10.4153/CJM-1998-041-5).

**Exact result stated in the abstract:** They analyze an RG transformation on functional measures for scalar quantum fields represented as a polymer expansion times an ultraviolet-cutoff Gaussian measure. Their definitions and estimates are sufficiently general to iterate the transformation, analyze complete RG flows, and construct a variety of scalar quantum field theories. The paper details fluctuation, extraction, and scaling estimates and discusses scalar models including infrared $\phi^4_4$ and non-Gaussian $\phi^{4-\epsilon}$. It is a rigorous block/multiscale RG framework, but its stated models and measure are scalar-field theory; it does not establish a pure lattice-gauge effective action landing in a Dobrushin or Dobrushin–Shlosman region, nor a gauge-theory torus-defect comparison. **Closeness: strong RG iteration precedent, no target gauge hand-off or uniqueness radius.**

### T. Balaban, J. Z. Imbrie, A. Jaffe (1988): Abelian Higgs effective action and clustering

**Source:** “Effective Action and Cluster Properties of the Abelian Higgs Model,” *Communications in Mathematical Physics* 114 (1988), 257–315, [publisher record and abstract](https://doi.org/10.1007/BF01225038).

**Exact result stated by the authors in the abstract:** They construct a multiscale cluster expansion for high-frequency modes within iterated RG; the expansion yields decoupling properties needed for exponential correlation decay, and produces a gauge-invariant unit-lattice theory with a deep Higgs potential. Their introduction says the final cluster expansion and proof of clustering/mass gap are to be completed in another paper. This is a gauge-theory RG route toward a cluster regime, but for the Abelian Higgs model in two and three dimensions, with a Higgs potential and small-coupling restrictions. It is not pure four-dimensional SU(2), not an openness theorem for arbitrary many-body perturbations of a Wilson action, and not a torus free-energy defect theorem. **Closeness: nearest gauge-theory hand-off analogue found, with materially different model and endpoint.**

### L. Bertini, E. N. M. Cirillo, E. Olivieri (1999): RG under strong mixing

**Source:** “Renormalization-Group Transformations under Strong Mixing Conditions: Gibbsianness and Convergence of Renormalized Interactions,” *Journal of Statistical Physics* 97 (1999), 831–915, [arXiv record and full text](https://arxiv.org/abs/cond-mat/9905434).

**Exact result:** The abstract states that for block averaging of a class of finite-range lattice gases satisfying suitable strong-mixing conditions, block decimation, cluster expansion, and comparison of ensembles prove Gibbsianness and convergence to a trivial Gaussian/product fixed point; the application is the two-dimensional standard Ising model above critical temperature at arbitrary magnetic field. In the body, Theorem 2.2 says global uniform strong mixing implies the renormalized measure is Gibbsian for a translation-invariant potential with bounded interaction norm at sufficiently large block size; Theorems 2.3 and following give finite-volume versions under local mixing assumptions. This is an explicit precedent for converting a mixing regime into a controlled RG image and using cluster expansion. It does not cover lattice gauge variables, gauge covariance, or an effective action produced by Balaban’s pure-gauge flow. **Closeness: strong abstract RG/mixing analogue; not the gauge-theory EXIT claim.**

### K. Gawędzki and A. Kupiainen (1983): block RG and partially resummed cluster expansion

**Source:** “Renormalization Group for a Critical Lattice Model: Effective Interactions Beyond the Perturbation Expansion or Bounded Spins Approximation,” *Communications in Mathematical Physics* 88 (1983), 77–94. The paper’s abstract says it develops expansion and analyticity methods for Kadanoff–Wilson RG in critical unbounded-spin models, applied to a nonlocal hierarchical dipole-gas model; it explains how block-spin scaling expands analyticity and how partial resummation controls large block fields. **Closeness: RG/cluster-expansion method only; scalar/hierarchical model, not lattice gauge theory or a Dobrushin landing result.**

### P. G. Federbush (1981): mass-zero cluster expansion with block modes

**Source:** “A Mass Zero Cluster Expansion. Part 1. The Expansion,” *Communications in Mathematical Physics* 81 (1981), 327–340; Part 2, “Convergence,” pp. 341–360. Part 1 develops a cluster expansion for a massless three-dimensional lattice scalar field perturbed by a fourth-power gradient interaction, in special block-spin modes with vanishing moments; Part 2 proves convergence. The paper says the methods may extend to the lattice dipole gas and related scalar models, and explicitly does not know whether they apply to rotator or Heisenberg models. **Closeness: multiscale cluster method and convergence, but not gauge theory, Dobrushin stability, or a pure-gauge hand-off.**

### J. Magnen, V. Rivasseau, R. Sénéor (1993): continuum SU(2) with fixed infrared cutoff

**Source:** “Construction of YM4 with an Infrared Cutoff,” *Communications in Mathematical Physics* 155 (1993), 325–383, [DOI](https://doi.org/10.1007/BF02097397).

**Exact result stated in the abstract:** They construct Schwinger functions for pure SU(2) Yang–Mills in four dimensions in the trivial topological sector, with fixed infrared cutoff and no ultraviolet cutoff, in a regularized axial gauge; their proof controls large-field positivity and small-field integrals/counterterms restoring cutoff-broken gauge invariance, and establishes the corresponding Slavnov identities. This is a substantial nonperturbative continuum construction, but it is not a finite-lattice block-spin flow landing in a global Gibbs Dobrushin/cluster-expansion zone. It does not state an explicit openness radius for many-body action perturbations or a finite-torus free-energy defect comparison. **Closeness: same pure SU(2) theory and constructive control, different RG direction and target statement.**

## 3. Free-energy defect comparison between tori

### R. Kotecký and D. Preiss (1986): abstract polymer expansion and finite-volume pressure

**Source:** “Cluster Expansion for Abstract Polymer Models,” *Communications in Mathematical Physics* 103 (1986), 491–498, [publisher record and DOI](https://doi.org/10.1007/BF01211762), [article text](https://www.math.ucla.edu/~biskup/290k.1.24w/PDFs/Kotecky-Preiss.pdf).

**Exact result:** Under their weighted Kotecký–Preiss summability condition (1), every finite polymer partition function is nonzero and its logarithm has a convergent cluster expansion (2) with weighted absolute bound (4). Their discussion after the theorem says that for geometric lattice polymers this gives a bulk free-energy formula and control of boundary terms when comparing finite-volume $\log Z$ with bulk pressure. This is the general mechanism from which exponentially small periodic-torus corrections follow when all clusters that distinguish the tori must wrap a distance comparable to the shortest period and the expansion has an exponential weight. The paper’s explicit proposition is not itself the row-846 inequality comparing two gauge-theory torus defects; the identification of wrapping clusters and the uniform constants for a given gauge effective action still have to be supplied. **Closeness: strong general cluster-expansion precedent for finite-volume free-energy errors; not the target’s gauge-specific two-torus defect bound.**

### Scope conclusion

Some ingredients are established in nearby settings: (i) Dobrushin uniqueness has quantitative perturbation neighborhoods, including an explicit one for high-temperature Ising interactions with general many-body perturbations in a decaying norm; (ii) strong-mixing-to-RG/cluster-expansion hand-offs are established for lattice gases and the Abelian Higgs model, and Balaban constructs the small-field pure-gauge effective-action sequence; (iii) convergent polymer expansions control finite-volume pressure and boundary errors. I did not locate a published theorem combining these into the requested result for Balaban’s pure four-dimensional lattice gauge effective action: an explicit many-body perturbation radius for a global compact-gauge Dobrushin/block criterion, a stable RG landing in that zone, and a uniform comparison of the resulting free-energy defect across the specified tori.

This is a bounded literature result, not a proof of absence. Publisher abstracts and accessible full texts are distinguished above. The Balaban papers themselves were not downloaded; their status here uses the exact publisher abstract and the quotations/citation map in this checkout. Nothing here verifies the new constants in `gap-handoff-opus.md`, changes a scientific status, or makes a proof claim.
