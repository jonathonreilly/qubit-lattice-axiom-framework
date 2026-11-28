
## Repo search

The queue says the lead searched `origin/main` and open YM4D PR branches `pr/10114`, `pr/10133`, `pr/10134`, and `pr/10141` before assignment; I am checking the named repo-prior note and row-1710 material before relying on that. The existing `library/prior/repo-search-2026-11-08.md` digest is a different task (soft-route suppliers such as TPI, H-O, W1/W2, and R2); its matches do not address large-N gauge theory or vector/matrix-model literature. No literature claim is accepted from that digest.

## Scope, provenance, and repo-prior work

This note is literature guidance for rows 1708–1709. It contains no proof, computation, status change, or audit finding. The target is a volume-uniform exponential covariance bound (or transfer gap) for a 4D Wilson lattice gauge measure, for all sufficiently large N, in a range that includes order-one ’t Hooft coupling. Strong-coupling results are context, not the requested crossing.

I read `GOAL.md` in full and FINISH.md’s “How we work,” “Working efficiently,” and “Rules.” Published results are inputs only after their assumptions are checked. I keep source claims separate from possible use. This task forbids proof work and computation.

The lead’s repo-first search is recorded in the FINISH row: `origin/main` and PRs #10114, #10133, #10134, and #10141 were searched before queuing. I checked the named `library/prior/repo-search-2026-11-08.md`; it concerns soft-route owners and contains no large-N gauge or vector/matrix-model source. Current local literature records do contain close prior work:

- `library/prior/gap-lit.md` and `gap-math-lit.md` cover Chatterjee, Basu–Ganguly, Cao–Park–Sheffield, finite-group weak-coupling decay, and the difference between loop expectations and a physical mass gap.
- `library/prior/gap-lit-wind.md` records Jafarov’s exact finite-N SU(N) master equation and its strong-coupling 1/N expansion, plus conditional twisted-Eguchi–Kawai equations.
- `library/prior/gap-lit-loops.md` records loop-equation results and the 2025 Cao–Nissim–Sheffield area-law theorems, including their coupling convention.
- `library/prior/gap-lit-xvol.md` records conditional Eguchi–Kawai/volume independence and its symmetry requirements.
- `library/prior/gap-lit-2.md` covers conditional confinement implications and distinguishes them from a proved gap.

I reuse those findings below and add only the distinctions needed for this target. No result found in those records is an order-one-coupling 4D large-N mass-gap theorem.

The lead’s row says no row in `library/open-registry.md` owns this literature question; my scoped grep found no large-N, matrix-model, vector-model, Wilson-loop, or mass-gap match there. This is a registry check, not a scientific status check.

## Outline and account check

I used `library/sa-index/README.md`, searched chunk files and `obligations.md` for large-N, Wilson-loop, clustering, and mass-gap entries, read neighboring rows, then read the cited outline lines. The relevant index entries are chunk 1 and obligations lines 24–27. SA 588–599 gives a spectral example with polynomial clustering but spectrum reaching zero, then states the separate interval-exclusion needed for a positive gap. SA 778–779 says its scalar block gap is not a physical Hamiltonian gap. This explains why loop limits or clustering alone do not meet the build target. The outline supplies no large-N gauge result.

I fetched the two Sussman–Alpoge files once each from commit `31a47c543775`, into the fresh scratch directory `/tmp/sa-gap-largen-lit-luna.2dFuV4/`. The outline has 32,992 lines; CA-I has 166,711 lines. I searched only named anchors in the outline and did not read CA-I wholesale. The CA I 4.12–4.19 index has no large-N/vector/matrix mass-gap entry relevant here. These files add no result to this note. Any text used from them must credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.

## 1. Large-N lattice gauge theory

### Results and regimes

**Sourav Chatterjee (2015), “Rigorous solution of strongly coupled SO(N) lattice gauge theory in the large N limit,” arXiv:1502.07719.** Theorem 3.1 gives a gauge-string formula for normalized Wilson-loop expectations in the ’t Hooft limit. The formula is an absolutely convergent sum over vanishing lattice trajectories. The rescaled inverse-coupling parameter must lie in an explicit small interval depending on dimension. Trajectory summation gives the convergence. This is a loop expectation result, not a covariance or spectral-gap estimate. **MAY APPLY** as a strong-coupling endpoint and combinatorial template; **UNLIKELY** to cross coupling alone. Reused from `gap-lit.md` and `gap-math-lit.md`.

**Jafar Jafarov (2016), “Wilson loop expectations in SU(N) lattice gauge theory,” arXiv:1610.03821.** Theorem 8.1 gives an exact finite-N master loop equation for admissible loops at arbitrary real coupling. Theorem 1.1 gives a convergent 1/N trajectory/string expansion only in a sufficiently small strong-coupling region. Its coefficients represent topology corrections. Arbitrary-coupling validity of the equation does not imply uniqueness or stability of its limiting solution. **MAY APPLY** as an exact identity; **UNLIKELY** as a gap route without quantitative uniqueness. Reused from `gap-lit-wind.md` and `gap-lit-loops.md`.

**Riddhipratim Basu and Shirshendu Ganguly (2017), “SO(N) Lattice Gauge Theory, planar and beyond,” arXiv:1608.04379, *Communications in Mathematical Physics* 356, 115–145.** This paper describes strong-coupling planar trajectories by decorated trees and noncrossing partitions, and treats higher-order corrections. It also gives a counterexample to a general Wilson-loop area-law lower bound. This is not a mass-gap result. **MAY APPLY** for strong-coupling combinatorics and as a warning against unjustified area-law claims; **UNLIKELY** for crossing coupling. Reused from `gap-lit.md` and `gap-lit-loops.md`.

**Sourav Chatterjee and Jafar Jafarov (2016), “The 1/N expansion for SO(N) lattice gauge theory at strong coupling,” arXiv:1604.04777.** Theorem 1.1 gives an asymptotic 1/N expansion of Wilson-loop expectations in the strong-coupling regime. The leading term has genus zero; later terms have higher-genus trajectories. It gives no volume-uniform estimate on connected correlations. **MAY APPLY** to the strong-coupling series; **UNLIKELY** for the crossing. Reused from `gap-lit-loops.md`.

**Ron Nissim (2025), “U(N) lattice Yang–Mills in the ’t Hooft regime,” arXiv:2510.22788.** I read the full 25-page preprint. Theorem 1.1 gives, for d≥2, N≥2, and β below an explicit dimension-dependent threshold β̃(d), a unique infinite-volume U(N) measure with exponential covariance decay. Constants depend on N and d, not volume. Theorem 1.5 proves large-N concentration and Wilson-loop factorization in the same β range. The proof splits U(N) into a U(1) random environment and an SU(N) field. It uses a conditional cluster expansion for U(1) and Langevin/Poincaré estimates for the SU(N) marginal. The author identifies the regime as strong coupling. It does not prove a gap at order-one β or along a weak-to-strong trajectory. **MAY APPLY** for the strong-coupling base and its field decomposition; **NO** for the requested crossing as stated.

**Hao Shen, Rongchan Zhu, and Xiangchan Zhu (2023), “A stochastic analysis approach to lattice Yang–Mills at strong coupling,” arXiv:2204.12737, *Communications in Mathematical Physics* 399 (2023).** Theorem 1.1 and Corollary 1.5 give infinite-volume uniqueness, log-Sobolev/Poincaré inequalities, large-N Wilson-loop factorization, and exponential decay for many observables. The windows are `|β|<(N−2)/(32(d−1)N)` for SO(N), or `|β|<1/(16(d−1))` for SU(N), in the paper’s ’t Hooft-scaled convention. Langevin mixing follows from a Bakry–Émery curvature bound. These are strong-coupling bounds; the SU(N) interval does not grow with N. **MAY APPLY** for a strong-coupling gap; **NO** for an order-one crossing. This source and its window are summarized in `gap-lit-loops.md` and `gap-lit-2.md`.

**Sky Cao, Minjae Park, and Scott Sheffield (2023), “Random surfaces and lattice Yang–Mills,” arXiv:2307.06790.** I read the full 131-page source. Theorem 1.8 gives an absolutely convergent embedded-planar-map representation for finite-lattice U(N) Wilson-loop expectations for every N≥1 and β>0. Theorem 1.14, made precise in Theorem 5.7, gives a single-location Makeenko–Migdal/master/Schwinger–Dyson recursion. These are all-β representation and identity statements. They do not give spatial decay, a positive gap, or volume-uniform stability as β crosses order one. **MAY APPLY** if a new decay estimate can be proved on the surface sum; without that estimate, **UNLIKELY**. Reused from `gap-lit.md` and `gap-math-lit.md`.

**Sky Cao, Ron Nissim, and Scott Sheffield (2025), “Dynamical approach to area law for lattice Yang–Mills,” arXiv:2509.04688.** Theorem 1.6 proves rectangular Wilson area bounds in a strong-coupling/’t Hooft regime for U(N), SU(N), and SO(2N). The proof verifies a mass-gap hypothesis for the area-law implication using Langevin dynamics. **MAY APPLY** for an area-law consequence once a gap is known in that small-β range; it is not an order-one result.

**Sky Cao, Ron Nissim, and Scott Sheffield (2025), “Expanded regimes of area law for lattice Yang–Mills theories,” arXiv:2505.16585.** Theorems 4.1 and 1.2 extend strong-coupling area-law ranges for U(N), including a large-N regime. The method treats the master equation as a linear inhomogeneous equation, controls the merger term with a truncated model, and proves an a priori solution bound. The action and β convention matter; `gap-lit-loops.md` records their translation and conditions. This improves a strong-coupling loop window, not a full gap window. **MAY APPLY** for loop estimates; **NO** for the required gap crossing.

### Coupling-range conclusion

The finite-N master equations and Cao–Park–Sheffield’s surface-sum identity hold for all β. These are identities or representations, not all-coupling decay theorems. The rigorous large-N expansions, large-N factorization with a gap, and area laws above remain within strong-coupling windows. I found no 4D SU(N), U(N), or SO(N) theorem proving a volume-uniform mass gap at order-one ’t Hooft coupling. This is a bounded search conclusion, not a nonexistence theorem.

## 2. Vector models: where N pays

### Kupiainen’s lattice O(N) sigma model

**Antti J. Kupiainen (1980), “On the 1/n Expansion,” *Communications in Mathematical Physics* 73, 273–294, DOI 10.1007/BF01197703.** The full publisher PDF request reached a bot/protection page. FINISH says to stop there, so I did not bypass it. I mark the paper itself **NOT FULLY READ**. Its publisher abstract and Kopper’s detailed account in §1 (citing Kupiainen’s Eq. (19)) state that, for the lattice n-vector model in any dimension, the 1/n expansion is asymptotic above the spherical-model critical temperature and a mass gap holds for sufficiently large n. In d=2, Kupiainen’s sufficient condition is reported as

`N > c exp(50 π β)`,

where β is inverse temperature and equals `1/λ` in Kopper’s convention. This is the explicit N price reported by the later primary article. The proof mechanism, as described by Kopper, uses reflection positivity and chessboard estimates around a massive spherical-model saddle. The claimed temperature range is above the spherical-model critical point. **MAY APPLY** as a large-N gap precedent, with this reading limitation. The exact constant c and details beyond Kopper’s report remain **UNVERIFIED** here.

### Kopper’s 2D nonlinear sigma model

**Christoph Kopper (1999), “Mass generation in the large N nonlinear sigma-Model,” *Communications in Mathematical Physics* 202, 89–126, arXiv:math-ph/9902020.** I read the full 44-page text. It studies the 2D O(N) nonlinear sigma model with a smooth UV cutoff. The coupling λ is of order one; λ much above one drives the generated mass toward the cutoff, while small λ makes the mass small and worsens the N bound. Its unnumbered theorem in §4.5 proves exponential decay of the infinite-volume two-point function for all sufficiently large but finite N. The proof introduces an interpolating bosonic field σ, tunes the saddle mass m by a gap equation, and expands around a massive Gaussian covariance.

The estimate that spends N is visible at several explicit points. Proposition 2 gives the small-field operator estimate `||A_s|| ≤ O(1) N^(−2/5)`. The derivative analysis in §4.4 turns this into a small factor per tree/cluster derivative. For the two-point function, §4.5 extracts `ε ≍ o(N^(−1/10))` per link on the connecting tree and sums

`Σ_{n≥2} (R' N^(−1/10) m^(−7/2))^n ≤ 1/2`

for N sufficiently large (Eq. (207)). Thus a sufficient threshold has the form `N ≥ C m^(−35)`, with C depending on the fixed constants in that paper. The spatial link sum costs `m^(−7/2)`; the N factor pays it. The introduction also states the equivalent qualitative requirement `N^(−1/6) < c e^(−4π/λ)` for its cluster expansion. These bounds are not sharp. The paper says the method should extend to connected 2n-point functions by a Mayer expansion, but proves two-point decay in detail.

The auxiliary field is scalar. The small factor comes from the N-flavor determinant and the 1/N expansion. This gives a vector-model precedent, not a matrix gauge proof. Gauge links are group-valued and plaquettes couple them. No matrix-valued auxiliary field with the same positive massive saddle and tree-factor bound is supplied. **MAY APPLY** as an architecture for paying correlation-volume costs by N; **UNLIKELY** as a literal transfer.

### Kopper–Magnen–Rivasseau Gross–Neveu model

**Christoph Kopper, Jacques Magnen, and Vincent Rivasseau (1995), “Mass generation in the large N Gross-Neveu-Model,” *Communications in Mathematical Physics* 169(1), 121–180, DOI 10.1007/BF02101599.** The journal abstract confirms a 2D Euclidean Gross–Neveu model with discrete chiral symmetry and a UV cutoff. For large finite N, suitable boundary conditions give at least two pure phases and exponential decay of the fermion two-point function. The author-copy route reached bot protection, so I stopped. I did not independently read the full 60-page article. The existing row-1702 result reports a close read and identifies the proof as a cluster expansion around an auxiliary-field saddle. I preserve that as prior work, not as a fresh independent check.

Row 1702 reports the decisive Eq. (207) bound:

`Σ_{n≥2} (R' N^(−1/10) m^(−7/2))^n ≤ 1/2`.

It requires N to dominate a constant times `m^(−35)`. The model is 2D, with a suitable UV cutoff and coupling λ of order one; Kopper’s discussion notes a separate small-λ technical problem and a cutoff-scale mass for large λ. The small factor comes from flavor loops and derivatives around the scalar auxiliary-field saddle. The factor `m^(−7/2)` pays spatial/tree summations. This estimate is **REPORTED FROM ROW 1702, NOT RE-READ HERE**.

I found no proof that ports this auxiliary-field mechanism to a lattice gauge matrix. Constructive matrix expansions exist, but they do not control the Wilson plaquette measure’s spatial gap. **MAY APPLY** as a vector-model design; **NO** as an established matrix-model analogue.

### Later vector-model work

Row 1702 also reports two comparisons. First, Kazuo Ito and Hiroshi Tamura (1986), “Mass Generation in the Large N Nonlinear Sigma-Model,” proves analyticity of the free energy for the 2D lattice Heisenberg model when `N > c exp(400πβ)` and β is large. It does not treat correlations. **UNLIKELY** as a gap supplier. I did not retrieve its full text; this is **REPORTED BY KOPPER, NOT VERIFIED**. Second, Kopper’s 1999 paper improves the estimate and proves correlation decay by the auxiliary-field cluster expansion above.

A 2026 OpenAI preprint, “Exponential decay in two-dimensional classical O(n) models,” reports exponential spin-correlation decay for each fixed n≥3 at every positive temperature. Its companion, “Sharp mass bounds for the two-dimensional O(4) model,” reports a positive full transfer gap for the periodic O(4) model at every finite β. These are later nonlinear sigma-model results, but they are fixed-N, two-dimensional spin systems, not large-N gauge results. I saw catalogue/abstract material, not the primary manuscripts, so I do not use them as evidence for a proof. **MAY APPLY** as evidence that other methods can cross coupling in vector models; **NO** as a 4D gauge transfer. Direct primary reading is still needed before a proof lane relies on these results.

## 3. Matrix, large-N, and related techniques

### Schwinger–Dyson and loop equations

**Thierry Lévy (2017; preprint 2011), “The master field on the plane,” *Astérisque* 388, arXiv:1112.2452.** Theorems 5.19 and 5.22 construct the large-N master field for 2D continuum Yang–Mills on the plane for unitary, orthogonal, and symplectic groups, and give deterministic Wilson-loop limits. The paper proves Makeenko–Migdal equations at finite N and in the limit. The coupling is the 2D area parameter; there is no strong-coupling restriction in this continuum setting. The proof uses Brownian motion on classical groups, convergence of noncommutative distributions, and an area-based recursion. **MAY APPLY** for testing a uniqueness approach in 2D; **UNLIKELY** for direct 4D gap transfer.

**Antoine Dahlqvist and Thibaut Lemoine (2023), “Large N limit of Yang-Mills measure on compact surfaces II: Makeenko-Migdal equations and planar master field,” arXiv:2201.05886; and (2023), “Large N limit of Yang-Mills partition function and Wilson loops on compact surfaces,” *Probability and Mathematical Physics* 4, 849–895, arXiv:2201.05882.** Their theorems prove large-N limits for stated loop classes on compact orientable surfaces, including all loops on the torus. The master field satisfies loop equations. This is 2D continuum Yang–Mills, not a 4D lattice gap. **UNLIKELY** for direct transfer.

An arbitrary-coupling loop equation is not itself a crossing theorem. Limiting loop equations may have multiple solutions. A new 4D proof could use them if it proves uniqueness and a quantitative contraction uniform in volume and β. That is a **MAY APPLY** direction, not an existing result.

### Free probability and second-order freeness

Basu–Ganguly use free probability to describe strong-coupling planar SO(N) loops. Lévy uses free unitary Brownian motion for the 2D planar master field. **James A. Mingo, Piotr Śniady, and Roland Speicher (2007), “Second order freeness and fluctuations of random matrices: II. Unitary random matrices,” *Advances in Mathematics* 209, 212–240, arXiv:math/0405258.** They prove second-order freeness and derive global trace fluctuations for Haar unitary matrices and invariant ensembles. These results control normalized trace limits and fluctuations for their stated ensembles. They do not control spatial separation or a transfer spectrum for the interacting 4D plaquette measure. **MAY APPLY** for a covariance expansion after the gauge law is controlled; **UNLIKELY** as a standalone gap proof.

### Concentration on U(N)^E and constructive matrix expansions

Haar-measure curvature/concentration does not directly survive an interacting Wilson density. The interaction adds a plaquette Hessian. A volume-uniform Poincaré or log-Sobolev estimate needs the interaction curvature to remain below the group curvature, or needs another mixing argument. SZZ’s strong-coupling Bakry–Émery proof is a concrete instance. Nissim’s U(N) proof instead conditions on U(1), applies a cluster expansion there, and proves a Poincaré inequality for the SU(N) marginal. Neither argument gives an order-one interval. **MAY APPLY** if one can prove a new curvature, entropy, or conditional-mixing bound at order-one coupling; no such gauge theorem was found.

**Vincent Rivasseau (2007), “Constructive Matrix Theory,” arXiv:0706.1224, *Journal of High Energy Physics* 09 (2007), 008.** The constructive/loop-vertex expansion controls connected matrix-model functions in its stable coupling domain, with estimates uniform in matrix size. The article’s application includes noncommutative φ⁴ theory. This is a real matrix analogue of constructive large-N expansion tools, but not of the gauge sigma/Gross–Neveu mass-gap mechanism: it supplies no compact-link Wilson measure, plaquette interaction, or spatial clustering theorem. **MAY APPLY** as an expansion-design source; the gauge adaptation is new and unproved.

### Eguchi–Kawai and volume reduction

**Tohru Eguchi and Hikaru Kawai (1982), “Reduction of Dynamical Degrees of Freedom in the Large-N Gauge Theory,” *Physical Review Letters* 48, 1063–1066.** The reduction identifies large-N neutral-sector observables with a reduced model when factorization and unbroken center symmetry hold. Related rigorous equivalence formulations retain center and translation symmetry conditions. If center symmetry breaks, reduction fails; identical loop equations do not imply equivalence when the equations have multiple solutions. These conditions and limits are summarized in `gap-lit-xvol.md`. **UNLIKELY** for a direct gap proof. There is no finite-N error bound down to N=2, nor a gap estimate uniform in volume.

### Gross–Witten and Douglas–Kazakov transitions

**David Gross and Edward Witten (1980), “Possible Third-Order Phase Transition in the Large-N Lattice Gauge Theory,” *Physical Review D* 21, 446–453; Spenta Wadia (1980), “N = ∞ Phase Transition in a Class of Exactly Soluble Model Lattice-Gauge Theories,” *Physics Letters B* 93, 403–410.** The one-plaquette unitary matrix integral is solved at N=∞ and has a third-order transition as its coupling changes. These papers do not number a theorem. This is an exact one-plaquette/2D matrix saddle, not a 4D gap. **MAY APPLY** as a benchmark and phase-transition warning; **NO** as a gap supplier.

**Michael R. Douglas and Vladimir A. Kazakov (1993), “Large N Phase Transition in Continuum QCD₂,” *Physics Letters B* 319, 219–230, arXiv:hep-th/9305047.** Their large-N two-sphere partition function has a third-order transition in the area. The strong-area phase has a branched-cover expansion. The weak-area phase does not have the simple area law. There is no 4D clustering claim. **UNLIKELY** for the target; useful as a warning that a coupling crossing can pass a phase transition.

**David J. Gross and Andrei Matytsin (1995), “Some Properties of Large-N Two-Dimensional Yang-Mills Theory,” *Nuclear Physics B* 437, 541–584, arXiv:hep-th/9410054.** The paper relates the Douglas–Kazakov cylinder transition to a gap in Wilson-loop eigenvalue support and treats transitions on discs with general boundary holonomy. This is a spectral gap in an eigenvalue distribution, not a spatial mass gap or transfer gap. **NO** as a physical mass-gap input.

### Two-dimensional Yang–Mills and mass gap

Two-dimensional continuum Yang–Mills is controlled by heat-kernel/Brownian holonomies and area-preserving geometry. Lévy and Dahlqvist–Lemoine prove large-N Wilson-loop/master-field results in that setting. They do not describe 4D plaquette interactions. A “gap” in the Gross–Matytsin eigenvalue-support result means a hole in unit-circle support, not a physical spatial mass gap.

I found no rigorous large-N 4D lattice theorem in these sources that gives exponential clustering outside the strong-coupling window. The direct mass-gap results remain SZZ and Nissim at small inverse-coupling β. The 2D papers give loop limits, not the requested 4D mass gap. **NO** result transfers without a new estimate.

## Classification for rows 1708–1709

| Item | Proved scope and regime | Verdict for 4D order-one large-N gap |
|---|---|---|
| Chatterjee; Jafarov; Chatterjee–Jafarov; Basu–Ganguly | Strong-coupling SO/SU Wilson-loop limits, trajectories, master equations, and 1/N expansions, any dimension | **MAY APPLY** for identities and strong-coupling start; **UNLIKELY** to cross unaided |
| Cao–Park–Sheffield | All-β finite-lattice surface sum and master equation; loop expectations only | **MAY APPLY** if a new decay/contraction estimate is proved |
| SZZ; Nissim | Volume-uniform mass gap and large-N factorization at small β | **MAY APPLY** at strong coupling; **NO** crossing |
| Cao–Nissim–Sheffield area laws | Improved small-β area-law windows, not full gap windows | **MAY APPLY** for loop bounds only |
| Kupiainen O(N) | 2D lattice sigma gap for large N; reported `N>c e^(50πβ)`; source not fully read here | **MAY APPLY** as precedent; primary proof remains unread |
| Kopper O(N) | 2D UV-cutoff sigma gap; N beats a correlation-volume power by auxiliary-field cluster factors | **MAY APPLY** as architecture; **UNLIKELY** as literal gauge transfer |
| Kopper–Magnen–Rivasseau | 2D UV-cutoff Gross–Neveu gap; row 1702 reports N^(−1/10) per derivative against `m^(−7/2)` tree cost; not reread | **MAY APPLY** as vector-model design; no established matrix analogue |
| Rivasseau constructive matrices; free probability; second-order freeness | Matrix correlators and trace limits for their own ensembles | **MAY APPLY** as tools; no gauge mass-gap theorem |
| Eguchi–Kawai | Conditional neutral-sector equivalence at N=∞ with symmetry hypotheses | **UNLIKELY**; no finite-N error or gap |
| Gross–Witten; Douglas–Kazakov; 2D Yang–Mills | Exact/rigorous 2D large-N transitions and loop laws | **NO** as a 4D gap input; useful benchmarks |

## Search record and limits

First-author searches in `library/` and `library/prior/` used: `Chatterjee`, `Jafarov`, `Basu`, `Cao`, `Kupiainen`, `Kopper`, `Magnen`, `Rivasseau`, `Nissim`, `Levy`, `Dahlqvist`, `Eguchi`, `Gross`, `Witten`, `Wadia`, `Douglas`, `Kazakov`, `Mingo`, `Shen`, and `Zhu`. The close reusable matches are the `gap-lit*` files listed above. The vector-model estimate appears in existing row-1702 material; it is marked as reported there where it was not independently re-read. Search hits alone are not treated as proof evidence.

Literature search terms included: `large N lattice gauge Wilson loop master loop equation`, `SU(N) U(N) SO(N) 1/N expansion`, `random surface string trajectory`, `large N O(N) sigma model mass generation`, `Kupiainen 1980 1/n expansion`, `Kopper nonlinear sigma mass generation`, `Gross-Neveu large N mass generation`, `matrix model Schwinger-Dyson uniqueness`, `second-order freeness`, `U(N)^E concentration lattice gauge`, `Eguchi-Kawai volume reduction rigorous`, `Gross-Witten`, `Douglas-Kazakov`, `two-dimensional Yang-Mills large N`, and `large N lattice gauge mass gap clustering`.

Full-text checks in this pass: Chatterjee–Jafarov–Basu–Ganguly sources and Cao–Nissim–Sheffield area-law papers are reused from the local prior summaries; Kopper (1999), Cao–Park–Sheffield (2023), Nissim (2025), and SZZ (2023) were read in full. The Sussman–Alpoge outline was searched at indexed anchors and read only at the cited line ranges. CA-I was not read wholesale. Kupiainen (1980) and Kopper–Magnen–Rivasseau (1995) copies hit bot protection; the latter's statements and estimate are reported from row 1702, not a new full-text check. The 2026 vector-model results were seen only in abstracts/catalogue records. No paper was placed in the repository. Downloads are in `/tmp/sa-gap-largen-lit-luna.2dFuV4/`.

This is a bounded literature note. It does not claim that no stronger theorem exists. Its conclusion is narrower: among the sources checked, the all-coupling identities and 2D matrix results do not prove the target 4D gap, while the direct 4D clustering results remain in small-β strong-coupling windows. Nothing here supplies an order-one crossing estimate.
