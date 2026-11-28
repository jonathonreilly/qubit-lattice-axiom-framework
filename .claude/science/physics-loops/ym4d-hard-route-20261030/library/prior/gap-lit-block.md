## Repo search

The lead’s pre-queue search and the repository cross-check are summarized
below. This note covers FINISH row 759 (2026-11-11); it is literature research,
not an audit, proof, or status update. No computer-assisted result is used to
discharge a claim. Numerical thresholds quoted below are **GUIDE**: they
identify hypotheses in the cited sources and are not estimates for the
Wilson model.

The task handoff says the lead searched `main` and PRs #10114, #10133, #10134,
and #10141 before queuing this row. No row-specific “Repo prior work” lines
were supplied. The existing `library/prior/repo-search-2026-11-08.md` is a
530-line digest for a different set of FINISH row 531 targets; it does not
claim a result on finite-size gap criteria. Its own boundary says it is not
an absence theorem. I reused its search provenance, not its conclusions as
evidence here.

I searched the available `origin/main` and those four PR refs for
`PA_g`, Knabe, Gosset/Mozgunov, Nachtergaele, martingale, detectability,
finite-size gap, and block-projection terms. `origin/main` had no relevant
finite-size criterion. The PR hits were broad gauge-invariant/operator
language, not a criterion application. The closest hit was
`MASS_GAP_CROSSOVER_REDUCTION.md` on PR #10133: it posits a transfer operator
on a gauge-invariant subspace, but supplies neither a local frustration-free
criterion nor its local-gap hypothesis. The same family of soft-route and
transfer notes occurs on the other PR refs; it does not establish PA_g.
Within this checkout, `library/gap-crux-exercise-astra.md` §§8.1 and 8.4 is
the direct target, and `library/open-registry.md` has no separate owner row
for this literature question. The older `gap-fullread-2.md` is the reusable
account of the standard criteria; I rely on it rather than repeat its source
reads.

The task’s prior-source check found no `library/prior/gap-lit-block.md` to
read before starting. I also checked the requested nested output path; this
file did not exist before this search.

## Questions and result in brief

**Has a Knabe/Gosset–Mozgunov/Nachtergaele/Lemm–Mozgunov/detectability-type
finite-size or block criterion been proved for a continuous-group lattice
gauge theory?** I found no such application in the sources searched through
2026-11-11. The named theorems below concern finite-dimensional spin
Hamiltonians with local projector constraints, frustration-free kernels,
or one-dimensional GVBS chains. Their algebra suggests possible abstract
extensions, but those are not source theorems and do not identify the Wilson
transfer operator with a local projector Hamiltonian.

There is a **separate, direct continuous-group claim**: Eriksson’s 2026
viXra preprint states a volume-uniform Poincaré inequality for four-dimensional
lattice Yang–Mills with `SU(N_c)`, for gauge-invariant observables, at
sufficiently large β. It is conditional on a Balaban RG input and an
additional RG-normalized disintegration assumption; it is not a Knabe-type
finite-size criterion. The archived v1 has not undergone peer review or
scientific correctness screening. It is a relevant claim to track, not a
verified supplier for PA_g or the 4D Wilson mass gap.

**Does a cited finite-size criterion use only gauge-invariant functions?**
None of the named spin criteria is stated as a gauge-invariant-subspace
theorem. Their projector conditions act on the model’s local tensor-product
Hilbert space. An invariant-subspace restriction could be valid if the
local projectors and all hypotheses descend to that subspace, but I found no
source that carries this out for continuous link variables or 4D Wilson
`SU(2)`. Eriksson’s conditional Poincaré claim explicitly concerns
gauge-invariant observables. Shen–Zhu–Zhu give a separate strong-coupling
functional-inequality result for continuous `SU(N)`/`SO(N)` lattice gauge
models; their cited abstract does not describe it as a finite-size
criterion restricted to gauge-invariant functions.

## What PA_g asks for

The local target in `library/gap-crux-exercise-astra.md` §8.1 (PA) is an
all-exterior bound on the angle between two conditional-expectation
projections, uniform in location, torus size, and cutoff at one fixed
physical block size. It acts on the full `L^2` fibre. Section 8.4 replaces
that with PA_g: the same pair-projection bound, but restricted to functions
invariant under gauge rotations at vertices whose incident links lie in the
patch. The note argues conditionally that PA_g implies its scalar GAP
corollary (GC4); it does not prove PA_g for Wilson `SU(2)`. The full-space
condition PA is separately challenged by open-link gauge-variant
correlations (GC1–GC3), which do not refute PA_g.

Thus a Hamiltonian spectral-gap bound is not automatically PA_g. PA_g is a
boundary-uniform conditional projection-angle estimate on a specified
physical function space. To import a Hamiltonian criterion would require a
proved operator representation, compatible local kernels and boundary
patches, a local gap on the required patches, and a theorem connecting that
Hamiltonian gap to the transfer/scalar quantity in the lane. No source
located supplies this chain for 4D Wilson `SU(2)`.

## Closest established finite-size criteria

### Knabe and Gosset–Mozgunov

Knabe’s original 1988 work introduced a finite-size criterion for periodic
frustration-free quantum spin chains (DOI
[10.1007/BF01019721](https://doi.org/10.1007/BF01019721)). The original
article was not reread for this task. Its standard 1D estimate, restated in
the later spin literature, is
\(\epsilon_m^{\rm circ}\ge\frac{n-1}{n-2}(\epsilon_n-\frac1{n-1})\)
(GUIDE), for the periodic/open frustration-free nearest-neighbour projector
chain with \(m>n>2\). Thus a local gap above \(1/(n-1)\) (GUIDE) implies a
size-uniform periodic gap. The following improved formula is from the full
Gosset–Mozgunov preprint and the repository’s full-read note.

Gosset and Mozgunov, “Local gap threshold for frustration-free spin
systems,” arXiv:[1512.00088](https://arxiv.org/abs/1512.00088), DOI
[10.1063/1.4962337](https://doi.org/10.1063/1.4962337), published 2016.
**Read:** full 23-page preprint, as recorded in
`library/prior/gap-fullread-2.md` §4. In 1D, for a translation-invariant,
nearest-neighbour periodic chain of finite-dimensional qudits with
frustration-free projector interactions, an open-chain gap
\(\epsilon_n>6/[n(n+1)]\) (GUIDE) implies for periodic sizes \(m>2n\)
(GUIDE)
\[
 \epsilon_m^{\rm circ}\ge {5\over6}{n^2+n\over n^2-4}
 \left(\epsilon_n-{6\over n(n+1)}\right).
\]
Their 2D theorem gives
\(\epsilon_m^T\ge\tfrac34(\epsilon_n^P-8/n^2)\) (GUIDE) for the stated
frustration-free nearest-neighbour square-torus projector model, even
\(n>2\), and the paper’s particular \(n\times(n+2)\) patch, when
\(m>2(n+2)\) (GUIDE). The patch geometry is part of the theorem.

**Bearing on PA_g / Wilson:** a useful local-to-global pattern—verify local
gaps, then propagate them—but the local input is a Hamiltonian spectral gap
above a common frustration-free kernel. It is not a conditional-expectation
angle and does not require gauge invariance. The paper contains no continuous
compact-group or gauge-link application. It provides no Wilson transfer
representation, no all-exterior conditional estimate, and no transfer-trace
bridge. **Applicability to 4D Wilson `SU(2)`: GUIDE only; no direct use.**

### Lemm’s arbitrary-dimensional nearest-neighbour criterion

Marius Lemm, “Finite-size criteria for spectral gaps in \(D\)-dimensional
quantum spin systems,” arXiv:[1902.07141](https://arxiv.org/abs/1902.07141).
**Read:** arXiv HTML abstract, model setup, and Theorem 3.1; not the complete
paper. For a translation-invariant, frustration-free periodic Hamiltonian
of finite-dimensional spins on \(\mathbb{Z}^D\), with nearest-neighbour
projector interactions, Theorem 3.1 applies for \(D\ge3\), \(n\ge3\), and
whole-box size \(N\ge2n+1\) (GUIDE):
\[
 \gamma_N\ge\gamma_{\mathcal B_n}-{1\over n}-{2\over n^2}.
\]
Here \(\mathcal B_n=[0,n]^D\) is the open local box. A local gap exceeding
\(1/n+2/n^2\le3/n\) (GUIDE) yields a positive periodic-system lower bound.
The theorem permits any spatial dimension, including four, **for
nearest-neighbour spin interactions**. The paper’s separate arbitrary
finite-range extension is only stated in three dimensions.

**Bearing on PA_g / Wilson:** this is the closest dimension match among the
finite-size spin criteria surveyed. It remains a finite-dimensional
frustration-free Hamiltonian theorem: it neither treats continuous links nor
uses a gauge-invariant-only subspace. Wilson plaquette interactions are
multi-link terms, and no source constructs a nearest-neighbour projector
Hamiltonian representation of the Wilson transfer problem, proves its
local box gap, or connects its gap to PA_g. **Applicability to 4D Wilson
`SU(2)`: GUIDE only; no direct use.**

### Lemm–Mozgunov boundary criteria

Marius Lemm and Evgeny Mozgunov, “Spectral gaps of frustration-free spin
systems with boundary,” arXiv:[1801.08915](https://arxiv.org/abs/1801.08915),
DOI [10.1063/1.5089773](https://doi.org/10.1063/1.5089773), published 2019.
**Read:** theorem/setup/proof sections for Theorems 2.5 and 3.10, not the
entire paper; recorded in `gap-fullread-2.md` §5. The 1D open-boundary result
uses local bulk and edge gaps in a frustration-free projector chain; one
simple threshold is
\(\min(\gamma_n^B,\gamma_{n-1}^E)>2\sqrt6 n^{-3/2}\) (GUIDE), yielding a
positive global bound with the theorem’s prefactor. Its 2D finite-range
result requires frustration-freeness on specified rhomboidal patches and
local gaps above a source-defined \(C_2n^{-3/2}\) (GUIDE) threshold. Boundary
intersections are part of the local input.

**Bearing on PA_g / Wilson:** this strengthens the lesson that block
boundaries and their local gaps cannot be dropped. It still assumes local
projector Hamiltonians and does not formulate gauge constraints, invariant
functions, or conditional Wilson fibres. It supplies neither PA_g nor a
Wilson transfer gap. **Applicability: GUIDE only; no direct use.**

### Nachtergaele martingale/projector criterion

Bruno Nachtergaele, “The spectral gap for some spin chains with discrete
symmetry breaking,” *Communications in Mathematical Physics* 175 (1996),
565–606; open preprint [cond-mat/9410110](https://arxiv.org/abs/cond-mat/9410110),
DOI [10.1007/BF02099509](https://doi.org/10.1007/BF02099509). **Read:** the
author preprint’s Theorems 2 and 3 and §6 proof/bounds; the journal version
was not separately compared (see `gap-fullread-2.md` §7).

The 1D result assumes a GVBS ground-state face and exact stabilization of
finite-volume local kernels. Its general criterion combines an energy
comparison, a nontrivial local common kernel with a local gap, and a
quantitative overlap/mixing estimate for adjacent support projections. In
the notation of the source, the lower bound has the form
\((\gamma_{l+1}/d_{l+1})(1-\epsilon_l\sqrt{l+1})^2\) (GUIDE), under its
conditions C1–C3. This is a 1D spin-chain martingale mechanism, not a
continuous-gauge theorem.

**Bearing on PA_g / Wilson:** the support-projection overlap is conceptually
near block-angle control, but it is not the PA_g conditional projection
estimate and has different local-kernel/mixing hypotheses. No result
establishes those hypotheses on the physical `L^2` Wilson fibres, uniformly
over fixed exteriors, or connects its Hamiltonian gap to the four-dimensional
transfer sum. **Applicability: GUIDE only; no direct use.**

### Detectability lemma

Dorit Aharonov, Itai Arad, Zeph Landau, and Umesh Vazirani, “The Detectability
Lemma and Quantum Gap Amplification,” arXiv:[0811.3412](https://arxiv.org/abs/0811.3412).
**Read:** the local-projector/layer setup and the stated lemmas, §§2–5.2, as
recorded in `gap-fullread-2.md` §6. The result assumes finitely many local
projector constraints on qubits, bounded overlap, a finite layer
decomposition into \(g\) layers, and a uniform overlap parameter
\(0<\theta<1\). For a state of nonzero ground energy \(\epsilon_0\),
Lemma 5.1 states that if
\(0\le\ell<(1/r)(\epsilon_0/f-1/(1-\theta))\) (GUIDE), then some layer
has probability at least \(\Delta^2(\ell)/(2g)^2\) (GUIDE) of more than
\(\ell\) violated constraints; the source defines \(r,f,\Delta\) from
\(\theta\), locality, and layer parameters. The authors distinguish this
constraint-violation statement from amplification of a spectral gap.

**Bearing on PA_g / Wilson:** it is not a finite-size local-gap theorem for
the frustration-free case and not a gauge-invariant-subspace result. A
compact continuous link law with a smooth Wilson plaquette weight is not the
finite constraint family in the paper. It gives no physical conditional
projection angle, Wilson local gap, or transfer trace bound. **Applicability:
GUIDE only; no direct use.**

### Forward-citation check through 2026: Hunter-Jones–Lemm

Nicholas Hunter-Jones and Marius Lemm, “Two classes of quantum spin systems
that are gapped on any bounded-degree graph,” arXiv:[2509.22438](https://arxiv.org/abs/2509.22438)
(2025 preprint). **Read:** arXiv abstract and HTML theorem/proposition
sections. It proves gaps with high probability for random rank-one
projectors and for Haar projectors on bounded-degree graphs, at sufficiently
large finite local dimension, by verifying generalized Knabe-type criteria.
Its graph criterion is an extension in graph geometry, not in gauge group
or local variable type. It retains finite-dimensional spin/projector
hypotheses. The forward search found no 2026 citation applying it to a
continuous-group lattice gauge model or a gauge-invariant link subspace.

**Bearing on PA_g / Wilson:** illustrates that block combinatorics can be
extended beyond regular chains/lattices while the finite-dimensional
projector input remains. It supplies neither invariant-subspace local angle
bounds nor Wilson transfer structure. **Applicability: GUIDE only; no direct
use.**

### 2026 hierarchy of frustration-free gap certificates

Kshiti Sneh Rai, Ilya Kull, Patrick Emonts, Jordi Tura, Norbert Schuch, and
Flavio Baccari, “A Hierarchy of Spectral Gap Certificates for
Frustration-Free Spin Systems,” *Quantum* 10, 2065 (2026),
arXiv:[2411.03680v3](https://arxiv.org/abs/2411.03680), DOI
[10.22331/q-2026-04-13-2065](https://doi.org/10.22331/q-2026-04-13-2065).
**Read:** journal abstract, summary, and metadata only. It formulates lower
gap certification for frustration-free quantum Hamiltonians as a hierarchy
of semidefinite programs; Knabe and subsequent finite-size criteria appear
as particular certificates in the hierarchy. Demonstrations are on
one-dimensional spin chains. The source does not state a continuous-gauge
application or a gauge-invariant-subspace theorem.

**Bearing on PA_g / Wilson:** it broadens certificate search for a supplied
finite-dimensional frustration-free Hamiltonian, but does not construct
one from Wilson conditional expectations or produce PA_g. The method uses
semidefinite optimization; under this task’s rule, any computation could
guide/refute a candidate only and would not discharge a Wilson estimate.
**Applicability: GUIDE only; no direct use.**

## Continuous-group and gauge-invariant neighboring results

### Eriksson’s conditional multiscale Poincaré claim

Lluis Eriksson, “Uniform Poincaré Inequality for Lattice Yang–Mills Theory
via Multiscale Martingale Decomposition,” viXra:[2602.0040v1](https://www.ai.vixra.org/pdf/2602.0040v1.pdf), submitted February 2026; no arXiv ID or DOI found. The v1 was archived as AIRR record
[ARR-2026-6RKVSY9K529RTVRV](https://airr.science/papers/ARR-2026-6RKVSY9K529RTVRV/versions/v1/).
**Read:** complete 11-page v1 PDF. The AIRR record identifies the v1 as a
historical import, not peer reviewed and not scientifically assessed; a
later viXra v2 is outside the version read here.

Theorem 1.1 claims a Poincaré constant \(\alpha\ge\alpha_*>0\) (GUIDE),
uniform in lattice size, for 4D Wilson lattice Yang–Mills with continuous
group `SU(N_c)` and sufficiently large β, on gauge-invariant observables.
The claim is conditional on the stated Balaban RG theorem and on the
RG-normalized disintegration property in Assumption 2.6. The latter is an
assumption in this paper, not derived there. The claimed proof also depends
on uniform conditional fast-mode inequalities and summable cross-scale
commutator estimates. The paper itself says its route does not establish a
continuum limit or OS axioms and that its Poincaré inequality alone does
not imply exponential spatial correlations.

**Bearing on PA_g / Wilson:** this is the only located continuous-group
claim in the surveyed set that explicitly restricts to gauge-invariant
observables. It is materially closer in physical function space than the
spin criteria, but it proves/claims a global measure Poincaré inequality
under different, multiscale assumptions—not the PA_g pairwise conditional
projection angle at a fixed physical block size and every exterior. Its large-β (weak-coupling) regime, unproved-in-paper RG-normalized
disintegration, and unreviewed status prevent treating it as an established PA_g estimate or a
4D Wilson `SU(2)` result. Mark **GUIDE / conditional claim; unverified**.

### Shen–Zhu–Zhu strong-coupling result

Hao Shen, Rongchan Zhu, and Xiangchan Zhu, “A stochastic analysis approach
to lattice Yang–Mills at strong coupling,” arXiv:[2204.12737](https://arxiv.org/abs/2204.12737), DOI
[10.1007/s00220-022-04609-1](https://doi.org/10.1007/s00220-022-04609-1).
**Read:** arXiv abstract only in the repository’s `gap-lit.md`; not a new
full-text read for this task. The abstract states that for `SU(N)`,
\(|\beta|<1/[16(d-1)]\) (GUIDE), the infinite-volume measure has
Poincaré and log-Sobolev inequalities and a strictly positive mass gap for
a large class of observables. This is a continuous-group lattice gauge
result at strong coupling, but not a Knabe/finite-size block criterion; the
abstract does not state a gauge-invariant-only domain. It is outside the
order-one/physical-block PA_g question and does not provide its all-exterior
projection norm.

## Gauge variants, quantum links, and scope boundary

Searches combined the named criteria with “lattice gauge theory,” “quantum
link model,” “gauge-invariant subspace,” “gauge-invariant functions,”
“quantum double,” and “frustration-free parent Hamiltonian,” then followed
the bounded-degree Knabe extension’s available 2026 citation trail. They
returned no source applying Knabe, Gosset–Mozgunov, Lemm–Mozgunov,
Nachtergaele’s martingale estimate, or detectability to a continuous-group
gauge-invariant link sector. Finite-group and quantum-link hits were not counted as criterion
applications absent a source applying the criterion with its hypotheses to
that model. No quantum-link result found supplied
the PA_g all-exterior conditional-angle input for `SU(2)`.

Gauge-variant open-link functions must be kept separate from physical
functions satisfying Gauss invariance. The target’s full-`L^2` PA can fail
because of gauge redundancy without saying anything decisive about PA_g.
Conversely, citing a spin criterion on the kinematic link Hilbert space
does not prove its hypotheses after restricting to the physical subspace:
one must show the local constraints preserve that subspace and that the
restricted local kernels, boundary gaps, and overlap estimates remain the
ones required by the theorem. No source located performs those steps for
4D Wilson `SU(2)`.

## Sussman–Alpoge outline cross-check and provenance

Using `library/sa-index/README.md`, the matching outline chunk rows and
neighbours, `obligations.md`, then the cited outline source lines: the outline
states at lines 588–599 that polynomial decay may coexist with spectral
support arbitrarily close to zero; lines 766–779 distinguish its scalar
block gap from vector-field coercivity and a physical Hamiltonian mass gap;
lines 3717–3720 say a gap above the invariant subspace is not proved there.
The complete-account index for items 4.12–4.19 contains no finite-size
gauge-gap criterion. Credit Ethan Sussman and Levent Alpoge, with Claude and
Codex as the authors of their text. These checks prevent attributing PA_g or
a physical mass-gap theorem to the outline/account; they do not validate
their arguments independently.

## Literature search record and limits

Search coverage included the original finite-size families and later
generalizations through 2026: Knabe; Gosset–Mozgunov; Lemm’s arbitrary-
dimension nearest-neighbour result; Lemm–Mozgunov; Nachtergaele;
detectability; the 2026 gap-certificate hierarchy; parent/projector
Hamiltonians; quantum links, quantum doubles, and gauge-invariant subspaces.
The forward-citation pass on the 2025 generalized Knabe paper found no
continuous-group gauge application. Primary open sources were used for the theorem statements
listed above; their exact theorem readings are recorded in the cited local
full-read notes. For Shen–Zhu–Zhu only the abstract was read. For Knabe’s
original paper only its bibliographic/abstract-level record was checked;
the stated exact thresholds are from the fully read Gosset–Mozgunov and
Lemm–Mozgunov sources. The Eriksson result is the complete v1 copy, with its
conditional hypotheses retained.

The Eriksson v1 PDF was downloaded to the empty scratch directory
`/tmp/gap-lit-block.AtglqU/` and extracted with Python `-I`; neither paper
content nor extracted text was copied into this checkout. Other cited papers
were read from open arXiv sources or the repository’s prior full-read notes;
no downloaded paper was added to the repository.

“None found” is a bounded search result, not a proof of nonexistence. This
note does not test the literature claims, derive PA_g, or confer scientific
status. Existing close method notes are `library/gap-skeleton-max.md`
(gauge-invariant Langevin generator formulation) and
`library/gap-means-max.md` §2.5 (what an all-boundary Knabe-type criterion
would need at correlation length); these are internal proposals, not
published supplier theorems.

## RESULT

RESULT: No surveyed Knabe/Gosset–Mozgunov/Lemm–Mozgunov/Nachtergaele/detectability finite-size criterion is established for a continuous-group lattice gauge theory or its gauge-invariant link subspace, and none supplies PA_g for 4D Wilson `SU(2)`; Eriksson’s 2026 gauge-invariant `SU(N_c)` Poincaré claim is a separate conditional, unreviewed multiscale result, not a verified block criterion. All quoted numbers are GUIDE.
