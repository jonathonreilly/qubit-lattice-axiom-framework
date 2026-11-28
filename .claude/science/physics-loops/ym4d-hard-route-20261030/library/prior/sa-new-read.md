# Repo search

The lead's `repo-search-2026-11-08.md` records searches of `origin/main` and open YM4D PRs #10114, #10133, #10134 and #10141, with targeted follow-ups and source passages. It says the located outside-lane work was useful lineage or conditional support, not a new proof of the then-current targets. I read that note, the nearby FINISH history (rows 605 and 651), and the current SA index. The checkout is `7c21dc19f6e34ff1640168b692bc4cc65fa01b91`; I fetched current `origin/main` read-only to check the mandated workflow rule 9.

The closest prior hit is FINISH row 605: at an earlier SA repository revision it records the addition of BA and LP manuscripts, and gives a status list for the assembly overview. That is a status snapshot, not a read of the nine files at `c7fef8b21b5846e1b5806a7d4f915737b9130c27`; it does not duplicate this inventory. The prior repo-search digest concerns other YM4D claims and older SA outline/account material. No `library/prior/sa-new-read.md` existed before this task. I did not find a prior note covering this nine-file read.

# 1. README.md

At lines 6–11, README gives only project-wide counts, not a mapping from BA, CL, EM, FP, GI, LP, MB, RT or SI folders to topics. It calls YM4's current manuscript unfinished and reports approximately 61k total slop pages and 30k closed pages. Its definition is: “Closed slop is the slop that has been refereed and frozen.” (line 11)

On help, lines 27 and 34–37 ask readers to identify mistakes and unrecoverable undefined terms, and invite collaborative checking and cleaning at a human pace. The quoted contribution list is: “Contributions could take different forms: formalization, verification, restructuring, exposition, code-generation, etc.” (line 37). README also cautions at line 1 that the work is tentative and pending verification. Credit note: its November 10 update asks that credit name Ethan Sussman, Claude and Codex; Levent Alpoge describes his own contribution as herding/following Ethan's outlines (line 32).

# 2. The nine submanuscripts

Line numbers below are lines in the fetched files under `/tmp/sa-new/YM4/`. Abstract descriptions are paraphrases. Statement headings serve as concise content descriptions; this is an inventory of what the manuscripts label, not a check of their arguments. The closest Y section is identified by matching the manuscript's stated subject to the actual Y section heading; where the manuscript does not name a Y section directly, that is marked as a topical correspondence rather than a quoted self-identification.
## BA — `YM4_BA.tex`

**Title and abstract (lines 104–117):** Block averaging and gauge geometry for four-dimensional lattice Yang--Mills theory. Constructs a centered SU(2) block average, one-step Wilson-energy/differential estimates, multiscale gauge coordinates, and an analytic fixed-average fibre density. **Y correspondence:** Y §1, “Background fields and constrained inverses,” especially “Block averages and gauge fixing” (Y 3543, 3547) and “Nonlinear averaging and the Wilson energy” (Y 4677); the file itself does not name a Y section.

**Theorems, propositions and lemmas (26):**

- Lemma `lem:avg-mean` (line 260): Local group mean.

- Proposition `prop:avg-map` (line 412): Properties of the centered map.

- Lemma `lem:avg-comb` (line 533): Comb estimate on a box.

- Theorem `prop:avg-energy` (line 651): One-step energy estimate.

- Lemma `lem:gauge-rigidity` (line 905): Relative transport estimate.

- Proposition `prop:gauge-one-step` (line 1047): One-step derivative.

- Proposition `prop:avg-iteration` (line 1180): Depth-uniform iteration.

- Proposition `prop:avg-complex-curvature` (line 1439): Complex curvature at its own scale.

- Lemma `lem:layered-carriers` (line 1638): Available rows and their carriers.

- Proposition `prop:layered-rigidity` (line 1722): Depth-uniform raw rigidity.

- Proposition `prop:box-complex-frame` (line 1865): Bounded-box complex frame.

- Proposition `prop:gauge-tower` (line 2153): Normalized tower axialization.

- Proposition `prop:pinned-representative` (line 2259): Pinned axial representative.

- Proposition `prop:gauge-products` (line 2452): Products and perturbations of gauge averages.

- Lemma `lem:smooth-node-extension` (line 2918): Extensions of coarse site data.

- Proposition `prop:smooth-finite-gauge` (line 2999): Finite gauge in the strong norm.

- Proposition `prop:smooth-gauge-kernel` (line 3149): Correction to the effective site kernel.

- Lemma `lem:wilson-local-hessian` (line 3290): Plaquette Hessian.

- Lemma `lem:wilson-curvature-expansion` (line 3454): Curvature expansion.

- Lemma `lem:wilson-current-remainder` (line 3615): Quadratic Wilson current remainder.

- Lemma `lem:fibre-taylor` (line 3789): Taylor bounds in physical bond logarithms.

- Lemma `lem:fibre-pivot` (line 3858): Right inverse on the pivots.

- Theorem `thm:fibre-chart` (line 3887): One-step fibre chart.

- Proposition `prop:fibre-density` (line 4067): Local disintegration of product Haar measure.

- Proposition `prop:soft-gauge` (line 4270): Insertion of normalized weights.

- Proposition `prop:guarded-haar` (line 4521): Change of target frame.

## CL — `YM4_CL.tex`

**Title and abstract (lines 107–128):** A scalar continuum theory from lattice Yang--Mills correlations. Assembles separated scalar moments, reflection positivity, phase selection, rotation criteria, scalar reconstruction and a nontrivial phase conditionally on source, running and physical comparison estimates. **Y correspondence:** Y §§3–5: “Couplings, sources and continuum limits” (Y 82548), “Short distances and Euclidean covariance” (Y 100371), and “Reconstruction and canonical components” (Y 115664), especially Y 118215 and 122565; the manuscript introduction discusses these components but does not name a single Y section.

**Theorems, propositions and lemmas (17):**

- Proposition `cl:prop-fixed-spacing` (line 224): Fixed-spacing infinite-volume states.

- Proposition `cl:prop-separated-compactness` (line 397): Separated compactness.

- Proposition `cl:prop-large-torus-recognition` (line 629): Large torus recognition.

- Proposition `cl:prop-flat-extension` (line 761): Flat extension and separated tensor density.

- Lemma `cl:lem-flat-marginal` (line 1043): Integration of omitted slots.

- Proposition `cl:prop-reflection-positivity` (line 1146): Reflection positivity of the limiting moments.

- Proposition `cl:prop-reflection-semigroup` (line 1280): Translations on the reflection Hilbert space.

- Proposition `cl:prop-limit-insertion` (line 1360): Uniform insertion on the actual reflection form.

- Proposition `cl:prop-change-of-mean` (line 1453): Changing the finite phase mean.

- Proposition `cl:prop-fixed-pure` (line 1706): Ergodic Gibbs states.

- Theorem `cl:thm-phase-law` (line 1808): The phase law of a reference limit.

- Proposition `cl:prop-phase-mean` (line 1954): The mean of a phase.

- Proposition `cl:prop-cube-cone` (line 2015): The joint transfer spectrum.

- Theorem `cl:thm-euclidean-rotations` (line 2174): Rotations of the realized limits.

- Proposition `cl:prop-phase-hilbert` (line 2271): The zero-energy space and spatial rotations.

- Proposition `cl:prop-scalar-reconstruction` (line 2408): Applicability of scalar reconstruction.

- Theorem `cl:thm-scalar-continuum` (line 2573): A realized nontrivial scalar phase.

## EM — `YM4_EM.tex`

**Title and abstract (lines 105–123):** Iteration of regular interactions on prescribed coupling prefixes. Bounds two regular-interaction chains on given prefixes, controls inherited remainders and physical coefficient extraction, and proves forward profile stability with explicit one-step and domain inputs. **Y correspondence:** Y §2, “Effective interactions and large fields” (Y 46266), especially “Local interactions and their source response” (Y 47839), plus the flow context in Y §3, “The running coupling and first-passage arithmetic” (Y 82885); topical correspondence, not an explicit Y-section citation in the manuscript.

**Theorems, propositions and lemmas (14):**

- Lemma `em:lem-age-kernel` (line 307): Summability of regular ages.

- Lemma `em:lem-remainder-load` (line 382): Squared-radius loads.

- Proposition `em:prop-common-restriction` (line 757): Restriction of the same step.

- Proposition `em:prop-prefix-formation` (line 826): Formation along prescribed prefixes.

- Proposition `em:prop-marked-recursion` (line 914): Uniform marked recurrence.

- Lemma `em:lem-physical-radius` (line 1001): A physical ball in the pair domain.

- Proposition `em:prop-physical-polarization` (line 1092): The radius cost in the polarization.

- Proposition `em:prop-companion-coefficient` (line 1173): The companion coefficient.

- Theorem `em:thm-coefficient-envelope` (line 1338): The coefficient bounds on the two domains.

- Lemma `em:lem-affine-pointing` (line 1481): Affine test of a complete pointing.

- Proposition `em:prop-anchor-transport` (line 1557): Transport after summing old anchors.

- Lemma `em:lem-adapted-norm` (line 1724): A norm adapted to transport.

- Lemma `em:lem-profile-cauchy` (line 1814): Derivatives on the buffered profile domain.

- Theorem `em:thm-profile` (line 1843): Uniform forward profile bounds.

## FP — `YM4_FP.tex`

**Title and abstract (lines 107–127):** Physical short-distance asymptotics of the lattice Yang--Mills action density. Derives a conditional separated two-point action-density law using the free coefficient, source response, reference comparison and a common analytic cell normalizer; it does not assert continuum existence. **Y correspondence:** Y §4, “Short distances and Euclidean covariance” (Y 100371), especially “The short-distance coefficient and nontriviality” (Y 100375); topical correspondence.

**Theorems, propositions and lemmas (16):**

- Lemma `fp:lem-shape-kernel` (line 291): Size and scaling of the comparison integral.

- Proposition `fp:prop-free-reference` (line 376): Free reference at a blocked scale.

- Lemma `fp:lem-free-kernel-bounds` (line 427): Bounds for the raw background and slice kernels.

- Proposition `fp:prop-witness` (line 553): Choice of scale.

- Proposition `fp:prop-source-normalization` (line 720): The physical source factor.

- Proposition `fp:prop-pointed-insertion` (line 810): Pointed first derivatives.

- Lemma `fp:lem-ordinary-response-sums` (line 930): The summed ordinary source bounds.

- Lemma `fp:lem-exact-insertion` (line 1103): Derivatives of the actual source integral.

- Lemma `fp:lem-witness-errors` (line 1154): Removal of the other witness source derivatives.

- Lemma `fp:lem-retained-covariance` (line 1405): Transport of polynomial readouts.

- Proposition `fp:prop-clean-reference` (line 1506): The reference covariance.

- Lemma `fp:lem-replicated-partition` (line 1607): Replication of a reflected source.

- Lemma `fp:lem-vacuum-density` (line 1684): Comparison of vacuum densities.

- Proposition `fp:prop-shared-normalizer` (line 1737): One analytic cell subtraction for both measures.

- Lemma `fp:lem-local-transfer` (line 1843): Transfer of a local covariance.

- Theorem `fp:thm-two-point` (line 1891): The short-distance two-point law.

## GI — `YM4_GI.tex`

**Title and abstract (lines 105–121):** Gaussian block integration and free action-density correlations. Develops constrained Gaussian integration, gauge normalization and complex Gaussian estimates, then computes/compares separated free-curvature action-density correlations. **Y correspondence:** Y §1, “Background fields and constrained inverses” (Y 3543), and the free/Gaussian comparison material in Y §4, including “The normalized Gaussian comparison on a finite run window” (Y 109340) and Appendix “Correlations of the free curvature” (Y 123739); topical correspondence.

**Theorems, propositions and lemmas (18):**

- Theorem `gi:thm-constrained-gaussian` (line 211): Constrained minimizer and fluctuation law.

- Proposition `gi:prop-successive` (line 313): Gaussian composition.

- Proposition `gi:prop-free-slices` (line 430): Independent curvature slices.

- Proposition `gi:prop-plain-straight-curvature` (line 494): The flat curvature law in two gauges.

- Theorem `gi:thm-relative-gauge` (line 661): Relative gauge normalization.

- Proposition `gi:prop-physical-normalizer` (line 968): Normalized physical Gaussian.

- Proposition `gi:prop-action-gauge-powers` (line 1062): The two action-weight powers.

- Proposition `gi:prop-gauge-stage-factors` (line 1106): Successive residual gauge factors.

- Theorem `gi:thm-complex-sector` (line 1180): The relative covariance sector.

- Proposition `gi:prop-auxiliary-gaussian` (line 1360): Eliminating an auxiliary Gaussian.

- Lemma `gi:lem-gaussian-radial` (line 1500): Conditional supports and radial weights.

- Proposition `gi:prop-gaussian-cutoff-flux` (line 1593): Normalized cutoff flux.

- Proposition `gi:prop-complex-chart` (line 1782): A constrained integral in fixed coordinates.

- Lemma `gi:lem-curvature-reflection` (line 2029): The curvature tensor away from coincidence.

- Proposition `gi:prop-free-continuum-cycles` (line 2073): Separated connected Gaussian densities.

- Proposition `gi:prop-free-lattice-kernel` (line 2262): Separated comparison of curvature kernels.

- Proposition `gi:prop-free-density-limits` (line 2387): Limits of the separated lattice cumulants.

- Theorem `gi:thm-free-separated-comparison` (line 2555): The uniform separated two-point comparison.

## LP — `YM4_LP.tex`

**Title and abstract (lines 101–115):** Periodic Wilson states and reflection positivity. Treats fixed-spacing periodic Gibbs states, finite reflection forms, common reflection periods, all admissible mirrors and chessboard domination; it disclaims continuum and mass-gap conclusions. **Y correspondence:** Y Appendix “Link reflections of periodic Gibbs states” (Y 124445) and “Reflection positivity of periodic Wilson states” (Y 125074); topical correspondence.

**Theorems, propositions and lemmas (9):**

- Lemma `lem:lp-compactness` (line 249): Local Gibbs limits.

- Proposition `prop:lp-finite-rp` (line 363): Finite reflection positivity.

- Lemma `lem:lp-borel-rp` (line 465): Completion of the half-space algebra.

- Lemma `lem:lp-chessboard` (line 492): One-direction chessboard inequality.

- Lemma `lem:lp-lower-tangent` (line 587): Gibbs lower tangent.

- Theorem `lp:thm-link-symmetry` (line 657): Bond-reflection symmetry.

- Lemma `lp:lem-fold-domination` (line 982): Domination by a reflected state.

- Theorem `lp:thm-all-mirrors` (line 1114): All admissible mirrors.

- Theorem `thm:lp-board-domination` (line 1196): Fixed-spacing chessboard domination.

## MB — `YM4_MB.tex`

**Title and abstract (lines 104–119):** Linear lattice PDE with block constraints. States mesh/depth-uniform scalar and gauge operator bounds, constrained inverses, Green families, row lifts and physical fluctuation gaps, while leaving nonlinear background admission as input. **Y correspondence:** Y §1, “Background fields and constrained inverses” (Y 3543), especially “Constrained propagators and local decay” (Y 16033) and later local inverse/response subsections; topical correspondence.

**Theorems, propositions and lemmas (42):**

- Lemma `mb:metric-growth` (line 297): Growth and scale ratios.

- Lemma `mb:weighted-composition` (line 347): Weighted composition.

- Proposition `mb:prop-flat-heat` (line 459): Free kernel bounds.

- Proposition `mb:prop-flat-lp` (line 543): Second differences on \(L^p\).

- Proposition `mb:prop-flat-schauder` (line 681): Discrete Schauder multiplier.

- Proposition `mb:prop-flat-poisson` (line 749): Interior Poisson estimates.

- Lemma `mb:lem-scalar-subsolution` (line 847): Scalar subsolution and covariant modulus.

- Proposition `mb:prop-scalar-block-gap` (line 898): Mean, gap, and projection.

- Proposition `mb:prop-scalar-block-decay` (line 982): Off-diagonal scalar block inverse.

- Lemma `mb:lem-covariant-lower` (line 1120): Exact lower-order terms.

- Lemma `mb:lem-site-connection-change` (line 1155): A left change of the connection.

- Proposition `mb:prop-local-scalar` (line 1215): Local site bootstraps.

- Proposition `mb:prop-coulomb-frame` (line 1524): A small real Coulomb frame.

- Proposition `mb:prop-flat-effective` (line 1680): The flat effective action.

- Lemma `mb:lem-outer-geometry` (line 1874): The outer curl and contour inequality.

- Lemma `mb:lem-site-lift` (line 2092): Compact lifts of the actual site average.

- Proposition `mb:prop-site-gram` (line 2165): Normalized site Gram matrix and restoration.

- Lemma `mb:lem-field-lift` (line 2362): A right inverse of the determining field rows.

- Proposition `mb:prop-site-pointwise` (line 2490): Local norms of the site Green operator.

- Lemma `mb:lem-flat-decomposition` (line 2723): A regular decomposition at a real flat connection.

- Theorem `mb:thm-layered-gap` (line 2898): Uniform layered form gaps.

- Proposition `mb:prop-compressed-gap` (line 3240): The compressed zero-current estimates.

- Proposition `mb:prop-flat-slice-kernel` (line 3432): Kernel of a flat curvature slice.

- Proposition `mb:prop-moving-saddle` (line 3572): The moving-slice saddle.

- Lemma `mb:lem-site-woodbury` (line 3663): Balanced site bounds and positive elimination.

- Proposition `mb:prop-current-completion` (line 3694): Current completion.

- Theorem `mb:thm-coarse-schur` (line 3743): Normalized Schur matrices and coupled response.

- Proposition `mb:prop-unfolded-response` (line 3839): Unfolded response.

- Proposition `mb:proper-site-inverse` (line 3949): Strong proper site inverse.

- Lemma `mb:lem-positive-carrier-walks` (line 4056): Local positive Green families.

- Lemma `mb:lem-coarse-carrier-inverse` (line 4124): Inversion of a positive coarse family.

- Theorem `mb:thm-current-families` (line 4256): Connected coefficients for the named propagators.

- Lemma `mb:lem-wilson-component-stencil` (line 4341): The interior Wilson stencil.

- Lemma `mb:lem-strong-positive-columns` (line 4353): Strong columns of the positive primitives.

- Lemma `mb:lem-strong-restoration-family` (line 4408): Strong restoration family.

- Theorem `mb:thm-strong-families` (line 4460): Strong current and row response families.

- Lemma `mb:lem-physical-schur` (line 4664): The top curl after row-mass subtraction.

- Theorem `mb:thm-physical-outer-gap` (line 4772): The proper outer fluctuation gap.

- Theorem `mb:thm-filed-covariance` (line 4934): Filed covariance and logarithm.

- Proposition `mb:edge-schur` (line 5089): Uniform edge Schur correction.

- Proposition `mb:window-schur` (line 5383): Uniform restrictions and weighted perturbations.

- Lemma `mb:fibre-gauge-null` (line 5479): Gauge null splitting.

## RT — `YM4_RT.tex`

**Title and abstract (lines 108–125):** Coupling trajectories and partition stability in lattice Yang--Mills theory. Builds a conditional coupling trajectory, first-passage estimates, tuning and normalized partition bounds from local formation, coefficient, large-field closure and history inputs. **Y correspondence:** Y §2, “Effective interactions and large fields” (Y 46266), especially “Large-field histories and induction” (Y 61901), and Y §3, “Couplings, sources and continuum limits” (Y 82548), especially “The running coupling and first-passage arithmetic” (Y 82885); topical correspondence.

**Theorems, propositions and lemmas (28):**

- Lemma `rt:lem-mass` (line 226): Mass and retained variables.

- Lemma `rt:lem-history-insertion` (line 294): Bounded insertions and positive history kernels.

- Lemma `rt:lem-vacuum-normalization` (line 396): Common normalization and redistribution of constants.

- Lemma `rt:lem-haar-normalizer` (line 497): A truncated Haar normalizer.

- Proposition `rt:prop-vacuum-count` (line 587): Regional counts and comparison of prefix scalars.

- Lemma `rt:lem-coherent-supply` (line 776): A conditional construction of coherent coefficients.

- Lemma `rt:lem-constant-order` (line 892): Order of the numerical choices.

- Theorem `rt:thm-joint-trajectory` (line 960): The joint trajectory through first passage.

- Proposition `rt:prop-torus-realization` (line 1080): Finite realization and the torus floor.

- Proposition `rt:prop-depth-envelopes` (line 1111): Terminal-depth bounds.

- Lemma `rt:lem-scale-sums` (line 1156): Sums of running powers.

- Theorem `rt:thm-ultraviolet-law` (line 1216): Uniform ultraviolet asymptotics.

- Lemma `rt:lem-dilation` (line 1281): Change of lattice units.

- Proposition `rt:prop-common-prefix-units` (line 1306): Common prefixes under change of units.

- Lemma `rt:lem-polydisc-slope` (line 1407): A product-disc derivative bound.

- Proposition `rt:prop-frozen-slopes` (line 1434): Slope along a frozen prefix.

- Proposition `rt:prop-independent-marked-slope` (line 1505): Slope with an independent marked polydisc.

- Theorem `rt:thm-frozen-tuning` (line 1593): Full tuning in the canonical interval.

- Theorem `rt:thm-homogeneous-tuning` (line 1706): Homogeneous terminal tuning.

- Proposition `rt:prop-presentation-matching` (line 1835): Matching on common all-small-field windows.

- Lemma `rt:lem-weighted-two-run` (line 1994): A weighted two-run estimate.

- Lemma `rt:lem-component-majorant` (line 2056): Majorizing coupled integrals.

- Lemma `rt:lem-genealogy-charge` (line 2365): Own-scale charge of a standing genealogy.

- Lemma `rt:lem-history-code` (line 2457): Rooted record count.

- Proposition `rt:prop-history-upper` (line 2483): Upper bound for the history sum.

- Proposition `rt:prop-loaded-upper` (line 2588): The loaded history estimate.

- Lemma `rt:lem-small-field-event` (line 2731): Admitting a product of link balls.

- Theorem `rt:thm-partition` (line 2814): Common-normalized partition bounds.

## SI — `YM4_SI.tex`

**Title and abstract (lines 107–125):** Scalar sources and uniform insertions for lattice Yang--Mills fields. Develops fixed-reference scalar-source transport, local energies, all-state source normalization, graded moments and reflected insertion bounds, conditional on local analytic/history estimates. **Y correspondence:** Y §2 “Source formation and volume bounds” (Y 80401), and Y §3 “Sources, local energies, and separated correlation bounds” (Y 95813) / “Source bounds for periodic Wilson states” (Y 98244); topical correspondence.

**Theorems, propositions and lemmas (28):**

- Lemma `si:lem-finite-derivatives` (line 269): Finite source derivatives.

- Proposition `si:prop-frozen-transport` (line 353): Transport of the bare source.

- Proposition `si:prop-block-observables` (line 391): Block observables outside replaced interiors.

- Proposition `si:prop-source-profiles` (line 507): Scalar shifts and their source range.

- Proposition `si:prop-same-frame-source` (line 620): A real shift in the same frame.

- Lemma `si:lem-source-vertex` (line 749): The fixed-reference source vertex.

- Lemma `si:lem-source-switches` (line 807): Rooted localization of the Wilson insertion.

- Lemma `si:lem-source-first-variations` (line 857): First variations at fixed reference.

- Lemma `si:lem-source-data-line` (line 933): Comparison on a local data line.

- Proposition `si:prop-member-formation` (line 972): Formation and old-origin summation.

- Proposition `si:prop-first-source-response` (line 1192): First-source response at fixed reference.

- Lemma `si:lem-retained-source-excess` (line 1360): Source excess and retained mass.

- Lemma `si:lem-common-gaussian` (line 1483): A common Gaussian majorant.

- Lemma `si:lem-phase-zero` (line 1524): A phase can cancel a tested integral.

- Lemma `si:lem-source-count` (line 1567): Rooted domain counts.

- Proposition `si:prop-local-energies` (line 1629): Locality, entropy and the vacuum difference.

- Lemma `si:lem-local-log` (line 1771): A local logarithm.

- Lemma `si:lem-separated-energy` (line 1841): Separated derivatives of local energies.

- Proposition `si:prop-cutoff-comparison` (line 1899): A sufficient comparison of two cutoffs.

- Proposition `si:prop-ordinary-stability` (line 2063): Ordinary complex-source stability.

- Lemma `si:lem-cell-normalizer` (line 2277): A holomorphic cell normalization.

- Theorem `si:thm-state-transfer` (line 2336): One source normalization for all periodic states.

- Lemma `si:lem-scale-cell-price` (line 2513): One-cell cost across scales.

- Theorem `si:thm-graded-moments` (line 2558): Graded separated moments.

- Lemma `si:lem-reflected-cell-operator` (line 2687): Cell multiplication and a time shift.

- Theorem `si:thm-lattice-insertion` (line 2751): A centered lattice insertion.

- Proposition `si:prop-limit-insertion` (line 2801): Insertion for already convergent separated moments.

- Proposition `si:prop-running-stop-mirror` (line 2941): Running-stop estimate for separated pairs.

# 3. Search of the nine files for topics A–F

The search was across all nine TeX files. “Found” below means the file contains the named item or a clearly related formulation; it does not mean that the text establishes Y's claim. No argument here evaluates correctness.

- **A — Large-field geometry and histories: FOUND, partial (RT; also SI for source accounting).** First, Y's `prop:large-field-2-3` is at Y 62080; its display at Y 62081–62084 includes `dist_infinity(Z_j, Omega_{j+1}) >= LM` and `Omega_{j+1} subset Lambda_j^{~ -1}`. RT defines how an island/drop-out contributes to its mass and cost (YM4_RT.tex 2157–2163), and treats labels whose large-field components have been healed (2034–2035); SI mentions island-boundary and outside-drop-out source terms (YM4_SI.tex 2018–2019). Short quote from RT: “An island includes its assigned core Wilson factor.” (2157). RT has conditional proofs for its own history-sum estimates, but the searched files do not state the complete requested Y geometry package: the nested Omega/Lambda/Omega sequence, the LM gap, stopping vectors, and the full healed-component geometry were not found together. Search words: `prop:large-field-2-3`, `Omega`, `Lambda`, `Z_j`, `LM`, `island`, `drop-out`, `stopping vector`, `healed component`, `large-field`.
- **B — Comparison of \check R scales: FOUND (EM).** YM4_EM.tex 452–455 states `\check R_j/\check R_{j+1} \in \{1,L\}`, then deduces `L^j\check R_j` is nondecreasing; its proof immediately above derives the one-step drop bound from the rounded running minimum. At 731–732 it also gives `\check R_i \le L^{j-1-i}\check R_{j-1}` for earlier levels. Short quote: “Thus `L^j\check R_j` is nondecreasing.” (453). The manuscript gives a proof in the stated frame/floor assumptions. The exact `h_t`-to-`t` comparison is not separately named.
- **C — Coupling ceiling below the generic `gamma < e^{-1/2}` condition: FOUND (RT).** Y states that generic bound at Y 1103. YM4_RT.tex 870–875 says the fixed choice triple precedes selection of an upper coupling ceiling `gamma`; Lemma `rt:lem-constant-order` (line 892, proof 919–934) requires a floor involving `gamma^{-2}` and explains that `varsigma=C_* gamma^{kappa_0-8} <= min(c_0/4,1)` can be arranged by reducing the ceiling (for `kappa_0>8`). Short quote: “The triple is fixed before the upper coupling ceiling `\gamma` is chosen.” (870). The text proves this parameter-order/reduction step under its inputs.
- **D — Action-region own-level cell unions and `s_j=M\check R_j` or `M`: NOT FOUND as the requested statement.** Y 1475–1477 chooses `s_j=M check R_j` when `Lambda_j` is a union of those cubes and `s_j=M` otherwise. Nearest hit: YM4_RT.tex 2567–2570 defines determining regions, action-sequence small-field regions and their complements, but does not say the action regions are unions of their own-level cells and does not give Y's `s_j` choice. Search words: `action region`, `action sequence`, `union of cells`, `own level`, `s_j`, `M\check R_j`, `M R_j`, `cell side`.
- **E — Y's phi/psi profiles, island base points, and `L_flat^2 < L`: NOT FOUND as the requested package.** Y defines island-extended base points one layer of `M check R_j` cells inside `Lambda_j^+` (Y 83993–83999), states `varphi_j h_z=h_z` at each such base point (Y 84108–84109), and gives the witness factor `2 psi_l epsilon_l` and condition `L_flat^2 < L` (Y 65477–65481). Near matches are distinct uses: YM4_SI.tex 464–481 defines a source-stage `varphi_j` profile; YM4_RT.tex 1680–1695 uses `psi_j` for a forward coupling profile. RT/SI also mention island costs, but no searched passage ties those functions to Y's island base points. Search words: `phi_j`, `varphi_j`, `psi_l`, `psi_j`, `base point`, `island`, `L_flat`, `L_{flat}`, `L_flat^2`, `rim profile`.
- **F — Y's minimiser-in-a-box proposition and main-step tree gauge: NOT FOUND as that paired result.** Y's proposition is `prop:large-field-2-4` at Y 71488–71491 (it begins “There exist a radius a_Lambda and a constant C(M)”). The main-step tree gauge is specified at Y 63856–63858 as the axial tree gauge of the box, including its external bond. Nearest hits: YM4_GI.tex `gi:thm-constrained-gaussian` (211) is a finite-dimensional constrained Gaussian minimizer/fluctuation statement; YM4_BA.tex discusses coordinate/local tree gauges (for example 155, 867–869). They do not name Y's localized Wilson-action minimizer in a large-field box or its main-step tree gauge. Search words: `minimiser in a box`, `minimizer in a box`, `prop:large-field-2-4`, `tree gauge`, `main step`, `critical gauge orbit`, `large-field box`.

**Provenance and scope:** The nine manuscript files and README are from Sussman and Alpoge's repository revision `c7fef8b21b5846e1b5806a7d4f915737b9130c27`; credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. The SA outline at `31a47c543775` and complete account were each fetched once to the requested `/tmp` locations. Before using the outline, I consulted `library/sa-index/` and its neighboring rows in chunks 16 and 19, then the cited outline excerpts; the index records a reader's status, not an independent check. CA-I was not read whole. `YM4_1400.tex` was fetched at the requested commit and read only at bounded cited ranges. No proof was attempted, no computer-assisted result was used, and no scientific or audit status is assigned.

# Parts of Y not covered

These nine files provide focused modules corresponding to parts of Y, but their own abstracts and introductions leave major inputs conditional. They do not cover the full “Background fields and constrained inverses” section (Y §1): BA and MB state local averaging/operator results, while nonlinear critical-background admission and some actual propagator/response inputs remain separate. They do not cover the full “Effective interactions and large fields” section (Y §2), especially the detailed large-field region geometry and complete retained-history formation; EM, RT and SI use such one-step, formation or history estimates as inputs. They do not close all of “Couplings, sources and continuum limits” (Y §3): RT assumes local formation/coefficient/closure data and SI assumes source formation and retained-mass estimates. FP's two-point law is conditional and does not cover all of “Short distances and Euclidean covariance” (Y §4), while CL gives conditional scalar-phase/reconstruction deductions rather than every step of “Reconstruction and canonical components” (Y §5). LP expressly remains fixed-spacing, with no continuum-limit or mass-gap conclusion.
