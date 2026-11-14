lead: Codex (gpt-6-luna high)
lease_until: 2026-11-12 15:02:43 UTC

# Repo search

The lead's `library/prior/repo-search-2026-11-08.md` is a search digest for
unrelated soft-route suppliers (TPI, M3, GEOH, H-C-MARK, and others); it does
not cover F-h. I read the digest, including its bounded Sussman–Alpoge
cross-check. The closest local work is `library/prior/gap-lit-flux.md`, which
already records Tomboulis–Yaffe, Kanazawa, Borgs–Seiler, Münster, and related
twist results, and `library/gap-es1-opus.md` §5, which states the open F-h
target and its proposed two-string motivation. I use those as prior work and
do not repeat their broader conclusions. `library/open-registry.md` has no
F-h/fusion owner; FINISH row 752 has no separate `Repo prior work` paths.

I checked `origin/main` and `origin/pr/10114`, `pr/10133`, `pr/10134`,
`pr/10141`, and `pr/10144` at the lead's requested refs. No result in those
refs states a lower bound on an even thermal sum by the square/product of
flux-sector weights. The closest is the existing flux review; PR 10134 carries
this lane, not an independent proof. The other hard-route hits concern the
seed-sum/control problems summarized in `gap-lit-flux.md`, not fusion. No
outside row or branch hit changes the F-h owner or closes this question.

## Target and scope

In `library/gap-es1-opus.md` §5, F-h asks for a finite-scale estimate of the
the form `p_z <= K S^(1/2)` for each heavy sector `z` outside a set `L` of
four light sectors, with `S := eps_cd = S_ev(a; (a,c,d))`; equivalently,

\[
  S_{\rm ev} \;\geq\; K^{-2}p_z^2,
\]

with constants controlled in the lane's specified box and coupling regime.
A pair of flux excitations should contribute to an even state at no more than
roughly twice their one-flux cost. The source
motivates this by two fundamental electric strings combining into a
centre-even state, but labels the Wilson-SU(2) step expected rather than
proved. Its Z2 example at `a=3` also warns that a universal estimate at every
box scale cannot be inferred just from the one-flux weight. The intended
application is the particular 4D Wilson SU(2) finite-volume sum, not merely an
asymptotic string-tension comparison.

## Literature results relevant to F-h

Numerical constants below are symbolic theorem constants; no empirical or
fitted number is used. Any numerical values imported from the literature
would be marked GUIDE; none is used as evidence here.

### Reflection positivity and twisted partition functions

**GUIDE — Tomboulis–Yaffe (1985), finite-temperature SU(2).** The paper relates
Wilson-loop behavior to twisted-sector/vortex observables and obtains
finite-temperature confinement criteria. The nearby use in F-h is the
twisted partition ratio as a flux diagnostic. It is not a lower bound on an
even-sector thermal sum in terms of two single-flux weights. **Transfer:** no
direct transfer to F-h; the direction and observable differ. **Wilson SU(2):**
the gauge group/model is relevant, but the cited criterion does not give the
required finite-box product estimate. **Read:** bibliographic record and
abstract only here; theorem-level summary cross-checked against the existing
`gap-lit-flux.md`, not a fresh full-paper read. [DOI
10.1007/BF01206134](https://doi.org/10.1007/BF01206134).

**GUIDE — Kanazawa (2009), generalized Tomboulis–Yaffe inequality.** For a reflection-
positive lattice system with the specified twist operation, the theorem
bounds a Wilson-loop expectation from above by a power of the normalized
twisted partition function (vortex expectation); the exponent is the loop
area divided by the transverse torus area. Its spin-system version likewise
bounds selected correlations from above. This is useful for deriving loop
decay from sufficiently small vortex expectation, but has the wrong direction
and object for `S_ev >= const * p_z^2`. It does not compare the even thermal
sum with two independent flux weights. **Wilson SU(2):** the gauge version
includes SU(N), hence SU(2), under its reflection-positivity and geometry
hypotheses; the missing lower estimate remains. **Read:** arXiv HTML theorem
and surrounding discussion, including the stated hypotheses and inequality.
[arXiv:0808.3442](https://arxiv.org/abs/0808.3442); [published version,
DOI 10.1016/j.aop.2009.04.002](https://doi.org/10.1016/j.aop.2009.04.002).

These results explain why reflection positivity and chessboard estimates are
not already a fusion theorem. The Sussman–Alpoge outline's ordinary Wilson
DLR reflection-positivity/chessboard argument bounds averages of positive
slab insertions by disseminated partition functions. The read passage treats
untwisted periodic Wilson measure; it neither inserts two twist sectors nor
proves a lower estimate on an even-sector sum. That is a method analogy, not
an F-h supplier. The outline and complete-account indexes were searched for
flux fusion, twisted partition sums, and even-sector bounds. No directly
relevant SA result was located. Source credit: Ethan Sussman and Levent
Alpoge, with Claude and Codex as authors of their text; no F-h claim is
imported from them.

### String-tension and cluster-expansion results

**GUIDE — Borgs–Seiler (1983), finite-temperature inequalities.** Their paper
establishes a chain of inequalities among Wilson, Polyakov-loop, and
't Hooft-loop string tensions in finite-temperature lattice gauge theory;
the abstract describes consequences for critical coupling and a weak-coupling
deconfining region. This compares asymptotic tensions of different probes; it
does not state a finite-volume lower bound on a neutral partition sum by a
product of flux-sector partition weights. **Wilson SU(2):** relevant gauge
context, but no stated F-h inequality or even-sector spectral sum. **Read:**
publisher/bibliographic abstract only; no full text available in this pass.
[DOI 10.1007/BF01208780](https://doi.org/10.1007/BF01208780).

**GUIDE — Mack–Petkova (1980), thick-vortex confinement criterion.** They
derive a sufficient condition for confinement in terms of the change in free
energy caused by a vorticity-changing boundary twist on a finite vortex
container; the abstract also reports the three-dimensional Abelian Coulomb
potential as a lower bound. This is a rigorous relation between a thick-vortex
free-energy cost and a Wilson/static-quark observable, but not a product lower
bound on an even partition sum. **Wilson SU(2):** the method was developed for
lattice gauge theory and is related to SU(2) vortex criteria; its finite
container hypotheses and observable do not establish the F-h finite-box
sector estimate. **Read:** publisher abstract only. [DOI
10.1016/0003-4916(80)90121-9](https://doi.org/10.1016/0003-4916(80)90121-9).

**GUIDE — Kovács–Tomboulis (1999), tagged-vortex string-tension bound.** For
SU(2) lattice gauge theory with their specified plaquette action and large
coupling parameters, they bound the Wilson loop by an area exponential whose
coefficient is proportional to the logarithm of one tagged, winding-vortex
excitation expectation. Nonvanishing of that expectation at large volume
therefore suffices for a positive string tension. The paper also says its
derivation uses a factorization inequality: the expectation for `n` tagged
vortices is related by an inequality to the product of the expectation for
`n-1` tags and for one tag. This is the closest located gauge-theory product
inequality, but it concerns tagged winding vortices in a constrained
SO(3)×Z2 representation, and supports a Wilson-loop upper bound; it is not a
lower bound on the even thermal sum by two heavy-sector weights. The stated
action includes an adjoint plaquette coupling, and the paper says details of
the factorization proof will appear elsewhere, so a direct pure Wilson-action
transfer is not supplied here. **Read:** full arXiv HTML to the end, including
the bound and the paragraph stating the factorization input; the proof of that
input is not in this short paper. [arXiv:hep-lat/9908031](https://arxiv.org/abs/hep-lat/9908031).

**GUIDE — Münster (1981), strong-coupling/high-temperature expansion.** In SU(2) and
Z2 lattice gauge theories in three and four dimensions, the paper develops
convergent high-temperature (strong-coupling) expansions for vortex free
energy; it reports an area law and equality of the vortex area coefficient
with the static-quark string tension in that regime. This gives rigorous
control of a single vortex free energy and string tension, not the pair-fusion
lower bound F-h asks for. **Wilson SU(2):** SU(2) and 4D are included, but the
expansion regime is strong coupling and its conclusion is an area-law
coefficient, not a comparison with `S_ev`. **Read:** publisher abstract and
metadata only; the previous flux note also records the result. No proof
details were read here. [DOI
10.1016/0550-3213(81)90153-X](https://doi.org/10.1016/0550-3213(81)90153-X).

**GUIDE — Fröhlich–Spencer (1982), Abelian gauge and spin systems.** They
prove a deconfining transition to a massless QED phase in 4D U(1) lattice
gauge theory and an intermediate QED phase in 4D ZN models for sufficiently
large N; the methods also establish phase transitions in related Abelian
Higgs and spin systems. This is foundational rigorous vortex/defect-phase
work, but it concerns Abelian models and phase existence, not an SU(2)
center-flux fusion inequality or an even-sector partition lower bound.
**Wilson SU(2):** no direct transfer. **Read:** abstract only. [DOI
10.1007/BF01213610](https://doi.org/10.1007/BF01213610).

**GUIDE — Simon–Yaffe (1982), Wilson-loop perimeter upper bound.** For an
arbitrary lattice gauge theory under their operator-kernel assumptions, the
Wilson-loop expectation decays at least as fast as an exponential in the
perimeter. This is a rigorous correlation upper bound, not a tension
subadditivity result or an even-sector lower bound. **Wilson SU(2):** the
general lattice-gauge formulation applies, but the observable and inequality
direction do not supply F-h. **Read:** abstract only. [DOI
10.1016/0370-2693(82)90815-2](https://doi.org/10.1016/0370-2693(82)90815-2).

**GUIDE — Pfister–Velenik (1997), sharp triangle inequality for 2D Ising surface
tension.** For all subcritical temperatures, the interface tension satisfies
`tau(x)+tau(y)-tau(x+y) >= kappa^(-1)(||x||+||y||-||x+y||)`, with `kappa` the
maximum curvature of the Wulff shape. This is a genuine quantitative
subadditivity/strict-triangle result for concatenated interface orientations.
It is the closest spin-model analogue found, but the inequality concerns
geometric direction of a single Ising interface, not two twisted flux weights
feeding an even thermal state. **Wilson SU(2):** no transfer; it is a 2D Ising
surface-tension theorem (and any gauge-duality use would require a separate
dimension/model map and matching observables). **Read:** arXiv abstract with
the theorem statement; full paper not read. [arXiv:cond-mat/9704018](https://arxiv.org/abs/cond-mat/9704018).

**GUIDE — Meisinger–Ogilvie (2010), k-string tension bound.** In a high-temperature
confined SU(N) theory with light adjoint fermions, a semiclassical dual
effective theory gives an upper bound on the ratio of k-string to fundamental
string tensions, `sigma_k/sigma_1 <= sqrt(k(N-k)/(N-1))`. This is a rigorous
nearby tension inequality, but it does not concern twists, even-sector sums,
or fusion weights. **Wilson SU(2):** the matter content and regime differ;
for N=2 there is no nontrivial k-string comparison. **Read:** arXiv abstract
and stated result, not a full proof read. [arXiv:0905.3577](https://arxiv.org/abs/0905.3577);
[DOI 10.1103/PhysRevD.81.025012](https://doi.org/10.1103/PhysRevD.81.025012).

### Defect fusion and recent twisted-sector criteria

**GUIDE — Choi–Cordova–Hsin–Lam–Shao (2022), non-invertible duality defects.** They
construct a codimension-one defect by gauging a one-form symmetry on half of
spacetime and determine its fusion rule; constructions include non-Abelian
gauge theories and ZN lattice gauge theory. This is exact defect/operator
fusion algebra, not a positive-measure estimate: an algebraic fusion channel
does not bound its thermal weight below by a product of two flux weights.
**Wilson SU(2):** the general construction is relevant to one-form symmetry,
but no pure Wilson SU(2) finite-volume F-h estimate is stated. **Read:** arXiv
abstract and selected construction/fusion passages; no partition-sum lower
bound there. [arXiv:2111.01139](https://arxiv.org/abs/2111.01139); [DOI
10.1103/PhysRevD.105.125016](https://doi.org/10.1103/PhysRevD.105.125016).

**GUIDE — Hayashi–Tanizaki (2026), center-vortex and monopole condensation.** They
propose torus and lens-space one-form-symmetry twisted partition functions as
gauge-invariant condensation criteria, analyze their leading contributions
in an adjoint-Higgs phase, and prove a relation between center-vortex and
monopole condensation in the stated gapped-phase/TQFT framework. This is a
relation among phase diagnostics under gap/locality assumptions, not the
finite-lattice pair-weight lower bound in F-h. **Wilson SU(2):** twisted
partition functions are directly relevant, but the theorem's hypotheses and
condensation observables do not establish the pure Wilson finite-volume
estimate. **Read:** arXiv abstract and stated theorem/conclusion passages;
not a full proof audit. [arXiv:2606.17708](https://arxiv.org/abs/2606.17708).

## Method assessment and remaining gap

The literature gives three distinct nearby structures:

* Reflection positivity (including the generalized Tomboulis–Yaffe method)
  turns twist information into upper bounds on Wilson-loop or spin
  correlations. Its known direction does not yield F-h's lower bound on an
  even-sector sum.
* Strong-coupling cluster expansions control vortex free energy and tension.
  Münster's theorem is the closest gauge-theory expansion result, but it
  identifies an area-law coefficient rather than proving finite-scale fusion
  into an even thermal state. A cluster expansion with explicit two-defect
  placement and a controlled connected correction could be a candidate
  route; no such F-h estimate was found in the sources searched.
* Spin-model surface-tension inequalities and generalized-symmetry fusion
  rules establish geometric or algebraic composition. Neither alone gives
  the positivity and quantitative normalization needed to compare the
  projected thermal sums in F-h. No applicable FKG/GKS inequality for these
  nonlocal twist-sector observables was located.

The cited “Lieb–Simon style” concavity search did not locate a theorem about
concavity/subadditivity of 't Hooft flux free energies that implies F-h. The
nearby Wilson-loop and thick-vortex estimates above have a different
observable or direction. Exact fusion rules for line/duality defects, even
when they apply to non-Abelian gauge theories, remain algebraic statements
unless accompanied by a positive finite-volume estimate of the relevant
sector traces.

Thus no located theorem proves a rigorous flux-free-energy subadditivity or
fusion estimate of F-h's form for 4D Wilson SU(2) in the lane's target regime.
This is a bounded literature-search conclusion, not an absence theorem: the
closest statements have different observables, direction, phase assumptions,
or coupling regime. No computer-assisted result was used. The outline and
complete account were fetched once as requested; only indexed/cited ranges
were searched and read. No paper was downloaded into the checkout or used as
computer-assisted evidence.

RESULT: No applicable rigorous F-h lower-bound/fusion inequality for the target 4D Wilson SU(2) even thermal sum was found; closest results do not close the finite-volume product estimate.
