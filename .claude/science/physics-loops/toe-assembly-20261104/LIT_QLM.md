# Quantum-link continuum limits: literature for GA2 Y2 and Y2-W

None of the works verified below supplies T0-start or T0-rate for the repo's fixed finite-register law in 3+1 dimensions without an extra dimension. This is a finding about these sources, not an impossibility theorem. The literature supplies exact quantum-link algebras, coherent-state representations, a large-representation expansion, conditional D-theory reduction, numerical tests, and rigorous finite-time truncation bounds in a different regulator. The useful native target is a quantitative comparison of gauge-invariant correlators, with the actual law, VC1 state, and ZM1 block map fixed. Large-register classicality at selected states does not establish that comparison in the vacuum. Nor does a finite list of matched moments establish membership in the hard core's action class or control its subsequent RG evolution. D-theory explains a possible mechanism, but its extra direction and phase hypotheses remain essential. No citation here discharges a repo proof obligation.

> Source receipt, 2026-11-05. Read both drafts' outcome paragraphs and FINISH blocks first, then their relevant interfaces and `LW1_5_DRAFT.md` §8.1. Observed branch: `toe-assembly-local`; HEAD: `2d0adc0c022753469151385e1789a4f444585ca6`. SHA-256: `GA2_Y2_DRAFT.md` = `812d01cb011915934ce9b441e40ada455902465d28b765f17342b09bbd13ac38`; `Y2W_DRAFT.md` = `f9d8db9c15b4b101d585d52facfef1ba3ad01d1b69b874bce161705d3eff7eaf`; `LW1_5_DRAFT.md` = `ff2f7b51da584c25c12eb94ad614acf910b949d8b1a925005ee5ebf6f21ecf06`. Their author-side results were not independently refereed in this literature lane.
>
> Search receipt. Live searches covered the named authors, D-theory, large representations/rishon flavors, rigorous convergence/universality, fixed-register 3+1 limits, SO(10)/U(5), and later simulation work through 2026. Every arXiv work below had its abstract page fetched and its specified PDF read at the relevant passages. Horn and Orland–Rohrlich predate arXiv; their exceptions are explicit below. Primary PDFs and extracted text are cached in `/private/tmp/qlm-literature-20261105/`. Page estimates describe proposed native proofs, not proofs completed here. Full nonperturbative continuum closure has no defensible page estimate.

## 1. Chandrasekharan–Wiese: the original dimensional-reduction argument

**Work.** S. Chandrasekharan and U.-J. Wiese, *Quantum Link Models: A Discrete Approach to Gauge Theories*. Preprint 1996; journal 1997. [arXiv:hep-lat/9609042v2](https://arxiv.org/abs/hep-lat/9609042v2), [primary text](https://arxiv.org/pdf/hep-lat/9609042v2).

**Result and hypotheses.** Section 5, Eqs. (5.4)–(5.7). The coupling relation is Eq. (5.6): “1/g² = β/e².” Start with a quantum model on a four-dimensional lattice. Its Euclidean evolution supplies a fifth direction of extent β. Assume a massless five-dimensional non-Abelian Coulomb phase and a suitable low-energy gauge action. Fix A5 = 0. The argument predicts four-dimensional Yang–Mills after reduction, with an exponentially large correlation length relative to β. The non-Abelian mass-generation step explicitly uses the confinement hypothesis. **Classification: physics-level effective-action and universality argument, not a rigorous correlator convergence theorem.**

**Map and native rebuild.** This paper explicitly constructs U(1) and SU(2), not the repo's U(5) or SO(10) laws. Rebuild the constant-mode reduction and coupling normalization, conditional on its effective action, in 2–4 pages. A separate proof must bound discarded modes and establish the starting phase. Reducing the repo's three spatial directions plus time by one direction would leave three Euclidean dimensions. **T0-start: no. T0-rate: no.** The paper's concluding speculation about three-dimensional quantum-link Hamiltonians is not such a theorem.

## 2. Brower–Chandrasekharan–Wiese: rishons and QCD

**Work.** R. Brower, S. Chandrasekharan and U.-J. Wiese, *QCD as a Quantum Link Model*. Preprint 1997; journal 1999. [arXiv:hep-th/9704106v1](https://arxiv.org/abs/hep-th/9704106v1), [primary text](https://arxiv.org/pdf/hep-th/9704106v1).

**Result and hypotheses.** Section 3, Eqs. (3.1)–(3.5), gives the reduction mechanism. Eq. (3.5) states “Z = Tr exp(−βH).” Section 4, Eqs. (4.2)–(4.6), constructs fermionic rishons and fixed-number representations. **Classification: exact finite-dimensional algebra for the rishons; physics-level continuum argument.** The reduction assumes the appropriate five-dimensional Coulomb phase. The conclusions explicitly leave its occurrence in the small 20-dimensional SU(6) representation unresolved.

**Map and native rebuild.** Set N = 5 in the algebra. The repo's fixed-number register is the one-column antisymmetric representation Λ^m C^10. The scalar total-number generator accounts for the difference between its u(10) notation and the paper's su(10) embedding. The determinant construction can remove the extra U(1), with a nonzero single-flavor determinant at m = N. It changes the gauge symmetry; it is not an identification of the existing U(5) law with pure SU(5).

Rebuild the CAR algebra, representation map, and determinant selection rule in 4–7 pages. Derive the repo's actual plaquette dynamics separately. **T0-start: no. T0-rate: no.**

**Correction to the draft's recollection.** Eqs. (3.3)–(3.5) omit the Gauss projector in fifth-direction evolution. They do not introduce fifth-direction quantum links with their own Gauss laws. The four-dimensional Hamiltonian lattice still exceeds the repo's three spatial dimensions. The dimension mismatch survives; that particular description of it should not be reused.

## 3. Schlittgen–Wiese: the detailed large-representation calculation

**Work.** B. Schlittgen and U.-J. Wiese, *Low-Energy Effective Theories of Quantum Link and Quantum Spin Models*. Preprint 2000; journal 2001. [arXiv:hep-lat/0012014v1](https://arxiv.org/abs/hep-lat/0012014v1), [primary text](https://arxiv.org/pdf/hep-lat/0012014v1).

**Result and hypotheses.** Section 6 chooses rectangular SU(2N) representations with N rows and large column number n. Eqs. (6.20)–(6.29) expand around an aligned classical minimum, retain low orders, and integrate quadratic fluctuations. They produce a five-dimensional gauge action with e² = 8/(n⁴|J|). Eq. (6.30) follows under the qualification: “assume that the correlation length is much larger than the extent”. Eq. (6.31) gives the expected exponential correlation length. **Classification: exact coherent-state ingredients followed by a semiclassical, derivative-expansion argument.** It does not provide uniform remainder bounds or a constructive Yang–Mills universality theorem. Section 7 leaves small representations unresolved.

**Map and native rebuild.** At N = 5, n = 1 corresponds to m = 5 in the relevant one-column family. The repo cannot send n to infinity within fixed `L5-U`. The source Hamiltonian also includes a U(1)-breaking determinant, unlike that law. For `L5-O`, the method suggests an analogous calculation, not an already proved SO(10) result.

Rebuild coherent symbols and the Gaussian calculation in 10–15 pages. Proving concentration near the minimum and bounding all omitted terms is a separate research task. Do not equate an expansion about a chosen coherent state with VC1's vacuum. **T0-start: no. T0-rate: no.**

## 4. Bär–Brower–Schlittgen–Wiese: many flavors are a register parameter

**Work.** O. Bär, R. Brower, B. Schlittgen and U.-J. Wiese, *Quantum Link Models with Many Rishon Flavors and with Many Colors*. Preprint 2001; proceedings 2002. [arXiv:hep-lat/0110148v1](https://arxiv.org/abs/hep-lat/0110148v1), [primary text](https://arxiv.org/pdf/hep-lat/0110148v1).

**Result and hypotheses.** Eqs. (5)–(6) introduce M rishon flavors and the constraints selecting an Nc-row, M-column representation. Eqs. (9)–(11) give coherent states and their symbols; Eq. (9) says “the identity operator can be resolved as” an integral of coherent-state projectors. Eqs. (12)–(15) give the semiclassical five-dimensional action and its reduction. **Classification: exact representation/coherent-state identities; physics-level large-M continuum expansion.** It assumes scale separation and uses the confinement hypothesis. Its separate large-Nc strong-coupling analysis is not a continuum theorem at fixed Nc = 5.

**Map and native rebuild.** M counts rishon flavors. It is neither the repo's occupancy m nor a ZM1 block size. The existing `L5-U` has one flavor and no unbounded M parameter. A block tensor product contains large representations, but does not automatically select this constrained irrep or its aligned state.

Rebuild the projector resolution, moment identities, and irrep constraints in 5–8 pages. Then ask whether the actual block map realizes them. **T0-start: no. T0-rate: no.** The source supplies a useful expansion parameter only after choosing a different representation family.

## 5. Brower–Chandrasekharan–Riederer–Wiese: the SO(10) match

**Work.** R. Brower, S. Chandrasekharan, S. Riederer and U.-J. Wiese, *D-Theory: Field Quantization by Dimensional Reduction of Discrete Variables*. Preprint 2003; journal 2004. [arXiv:hep-lat/0309182v1](https://arxiv.org/abs/hep-lat/0309182v1), [primary text](https://arxiv.org/pdf/hep-lat/0309182v1).

**Result and hypotheses.** Section 4.5, Eqs. (4.39)–(4.42), constructs SO(N) quantum links from so(2N) generators and Majorana rishons: “The rishon representation takes the form” given in Eq. (4.41). **This algebraic construction is exact.** Section 5.3, Eqs. (5.7)–(5.11), gives the conditional continuum argument. Eq. (5.11) predicts SO(N) correlation-length scaling with N−2 replacing the SU(N) color factor. It uses perturbative beta coefficients and the presumed mass-generation mechanism. **This is a physics-level scaling prediction, not a rigorous SO(N) convergence theorem.**

**Map and native rebuild.** N = 10 gives exactly the repo's so(20) embedding, after checking Majorana normalization and link orientation. Rebuild the commutators and gauge-invariant plaquette in 3–5 pages. A coherent-state construction for a specified SO(20) representation family would take roughly 8–15 further pages before any vacuum-control problem. The Lie algebra alone does not fix Spin(10) versus SO(10), allowed bundles, or matter representations.

The source's generalization of D-theory still needs five dimensions, a Coulomb phase, and controlled reduction. Substituting N−2 = 8 into its scaling formula proves none of those hypotheses. **T0-start: no. T0-rate: no.**

## 6. Beard et al.: numerical dimensional-reduction evidence

**Work.** B. B. Beard, R. C. Brower, S. Chandrasekharan, D. Chen, A. Tsapalis and U.-J. Wiese, *D-Theory: Field Theory via Dimensional Reduction of Discrete Variables*. Preprint 1997; proceedings 1998. [arXiv:hep-lat/9709120v1](https://arxiv.org/abs/hep-lat/9709120v1), [primary text](https://arxiv.org/pdf/hep-lat/9709120v1).

**Result and hypotheses.** Eqs. (25)–(27) state the gauge reduction scenario; Eq. (27) is “1/g² = β/e².” Eq. (37) defines the U(1) quantum-link Hamiltonian. Figures 8–9 report cluster-size scaling in its (4+1)- and (3+1)-dimensional versions. The paper also tests dimensional reduction in the Heisenberg/O(3) setting. **Classification: numerical evidence plus an effective-field-theory argument.** The simulations of five-dimensional non-Abelian Coulomb behavior discussed here use Wilson gauge fields; they do not establish that phase for the repo's small non-Abelian registers.

**Map and native rebuild.** Use its distinction between a phase diagnosis and the reduction argument. Rebuild the finite-volume transfer and suitable gauge-invariant diagnostics in 4–6 pages. Simulations could guide a phase search, but neither cluster growth nor an O(3) example proves the required U(5)/SO(10) vacuum statement. Finite-β behavior also does not settle the zero-temperature Hamiltonian limit.

**T0-start: no. T0-rate: no.** Its scaling plots cannot establish uniform action-class bounds or an error exponent p.

## 7. Chandrasekharan: a large-spin route without dimensional reduction

**Work.** Shailesh Chandrasekharan, *Confinement, Chiral Symmetry Breaking and Continuum Limits in Quantum Link Models*. Preprint 1998; proceedings 1999. [arXiv:hep-lat/9809084v1](https://arxiv.org/abs/hep-lat/9809084v1), [primary text](https://arxiv.org/pdf/hep-lat/9809084v1).

**Result and hypotheses.** Section 3, Eqs. (5)–(7), studies the U(1) plaquette Hamiltonian at vanishing bare electric coefficient. Eq. (7) is a tree-level, “low energy, large j effective” Hamiltonian. It contains an induced electric energy and predicts g_eff² of order 1/sqrt(j(j+1)). Figure 1 is a conjectured phase diagram. **Classification: physics-level large-j expansion, not a proof of a Coulomb phase at small fixed j.** The finite-order strong-coupling results in Eqs. (3)–(4) do not prove the weak-coupling scenario.

**Map and native rebuild.** This directly informs Y2-W's bare-corner attack: a small bare coefficient need not mean a small effective coupling. The useful exact precursor is a restricted-flux ladder comparison. From normalized spin matrix elements, prove an O((M+1)²/j²) error against a rotor shift on |electric flux| ≤ M, away from the cutoff. That should take 2–4 pages. Do not assume the canonical phase relation used in Eq. (6) holds globally on a finite register.

This is Abelian and requires increasing j. It does not address fixed `L5-U` SU(5) block loops. **T0-start: no. T0-rate: no.**

## 8. Tong et al.: a rigorous nearby theorem, with different quantifiers

**Work.** Yu Tong, Victor V. Albert, Jarrod R. McClean, John Preskill and Yuan Su, *Provably accurate simulation of gauge theories and bosonic systems*. Preprint 2021; revised/published 2022. [arXiv:2110.06942v2](https://arxiv.org/abs/2110.06942v2), [primary text](https://arxiv.org/pdf/2110.06942v2).

**Result and hypotheses.** Appendix Theorem 5 bounds state leakage. Theorem 6, Eq. (65), bounds Hamiltonian-truncation error; its statement requires “all projection operators … commute with each other”. Eq. (24) assumes a preserving part and a part changing a local quantum number by at most one, with restricted norm at most χ(Λ+1)^r, 0 ≤ r < 1. Start in a bounded-number subspace. The error decays exponentially in cutoff separation relative to a time-dependent scale, with polynomial prefactors and a commutator-norm factor. Theorem 12 also bounds eigenstate tails, assuming an isolated eigenvalue “with multiplicity 1”, spectral gap δ, and finite mean absolute local number. Its cutoff depends on δ^−1 and that mean. **Classification: rigorous truncation theorems.** Gauge applications are checked for U(1) and SU(2).

**Map and native rebuild.** Its regulator is a projection of an infinite-dimensional Hamiltonian, not the repo's rishon or so(20) quantum link. No equality between those truncations is supplied. Rebuild the leakage and Duhamel/Trotter argument in 12–20 pages, then prove the Hamiltonian comparison and initial-state tail bound actually needed here. Constants must be tracked along any changing lattice coupling.

**T0-start: no. T0-rate: no.** A cutoff chosen for time, volume, and accuracy does not prove a fixed-register vacuum limit. Theorem 12 supplies neither a uniform continuum gap nor a vacuum identification for the repo's laws.

## 9. Zache et al.: a quantitative lower-dimensional benchmark

**Work.** Torsten V. Zache, Maarten Van Damme, Jad C. Halimeh, Philipp Hauke and Debasish Banerjee, *Towards the continuum limit of a (1+1)d quantum link Schwinger model*. Preprint 2021; revised/published 2022. [arXiv:2104.00025v2](https://arxiv.org/abs/2104.00025v2), [primary text](https://arxiv.org/pdf/2104.00025v2).

**Result and hypotheses.** Eq. (3) gives the Gauss-law-reduced constrained spin Hamiltonian: “The resulting Hamiltonian has the form” displayed there. Eq. (4) counts its physical Hilbert space for the periodic, even-length chain used in the paper. **These are exact finite-system algebra/combinatorics results.** The continuum spectrum in Figure 1 comes from exact diagonalization and infinite matrix-product-state calculations, with extrapolation. The text specifies the order S → infinity, then volume → infinity, then a → 0. **The continuum comparison is numerical evidence.** The large-spin functional-integral treatment of the theta angle is a separate physics-level argument.

**Map and native rebuild.** This model has one spatial dimension and no magnetic plaquettes. It cannot settle non-Abelian 3+1 dynamics. Rebuild the reduced Hamiltonian and state counting in 4–7 pages as a test of a proposed regulator-comparison method. Keep integer/half-integer spin and the background/topological sector fixed.

**T0-start: no. T0-rate: no.** Good numerical accuracy at modest S is not a uniform theorem at one fixed register.

## 10. Wiese 2013: what the simulation review actually guarantees

**Work.** U.-J. Wiese, *Ultracold Quantum Gases and Lattice Systems: Quantum Simulation of Lattice Gauge Theories*. 2013. [arXiv:1305.1602v1](https://arxiv.org/abs/1305.1602v1), [primary text](https://arxiv.org/pdf/1305.1602v1).

**Result and hypotheses.** Section 4.3, Eqs. (4.10)–(4.14), records the embedding algebra, rishon realization, extra U(1), and determinant. The commutation relations “can be realized using fermionic rishons” in Eq. (4.12). **These identities are exact.** The discussion after Eq. (4.14) separates large-rishon-flavor recovery of Wilson links from the D-theory continuum route. Figure 5 depicts dimensional reduction and domain-wall quarks. **Those continuum claims use physics-level universality and phase assumptions; the review provides no new rigorous fixed-register universality theorem.**

**Map and native rebuild.** The U(5) construction maps directly at the algebra level. The reference to SO(N) embeds it in so(2N), but the review does not prove SO(10) vacuum convergence. Rebuild an explicit normalization dictionary and determinant test in 3–5 pages, reusing the earlier papers' native algebra proofs.

**T0-start: no. T0-rate: no.** Hardware implementability, exact Gauss symmetry, and a finite register do not imply the repo's action lies in `𝒜_k(g)`.

## 11. Wiese 2021: later review, with the extra direction made spatial

**Work.** Uwe-Jens Wiese, *From Quantum Link Models to D-Theory: A Resource Efficient Framework for the Quantum Simulation and Computation of Gauge Theories*. 2021 preprint. [arXiv:2107.09335v1](https://arxiv.org/abs/2107.09335v1), [primary text](https://arxiv.org/pdf/2107.09335v1).

**Result and hypotheses.** Eqs. (3.9)–(3.10) identify the SU(2N) and SO(2N) embeddings. Section 3(e), Eqs. (3.16)–(3.17), starts in a (4+1)-dimensional Coulomb phase. Its stated condition is “Assuming that ξ ≫ L′”. It reduces a fourth spatial direction of extent L′ and obtains 1/g² = L′/(e²c), with the expected exponential correlation length. **Classification: exact algebraic accounting; conditional physics-level effective-field-theory reduction.** It is not a new convergence theorem.

**Map and native rebuild.** This presentation preserves physical time and adds a spatial direction. The earlier presentation uses auxiliary Euclidean evolution on a four-dimensional lattice. Neither obtains 3+1 Yang–Mills by merely renaming the time direction of the repo's three-dimensional Hamiltonian lattice. The c factors also depend on the convention used for that direction.

Rebuild the conditional reduction and anisotropy normalization in 3–5 pages. Establishing the phase, reducing fluctuations, and controlling matter remain separate. **T0-start: no. T0-rate: no.** The finite local register does not remove the growing extra extent L′.

## 12. Bañuls et al.: a broad quantum-simulation review

**Work.** M. C. Bañuls, R. Blatt, J. Catani, A. Celi, J. I. Cirac, M. Dalmonte, L. Fallani, K. Jansen, M. Lewenstein, S. Montangero, C. A. Muschik, B. Reznik, E. Rico, L. Tagliacozzo, K. Van Acoleyen, F. Verstraete, U.-J. Wiese, M. Wingate, J. Zakrzewski and P. Zoller, *Simulating Lattice Gauge Theories within Quantum Technologies*. 2019 preprint. [arXiv:1911.00003v1](https://arxiv.org/abs/1911.00003v1), [primary text](https://arxiv.org/pdf/1911.00003v1).

**Result and hypotheses.** The introductory gauge-field discussion separates truncating Wilson links from quantum-link regularization. Section 4.1.3, Eq. (2), specifies a (1+1)-dimensional U(1) quantum-link Hamiltonian. Its statement is “The Hamiltonian is invariant under local U(1) symmetry transformations”. **Classification: exact symmetry of a specified model, alongside reviewed numerical and experimental results.** This is not a non-Abelian continuum-universality theorem.

**Map and native rebuild.** Use the explicit Hamiltonian to test Gauss-law-preserving implementations and observable definitions. Rebuild that toy-model dictionary in 2–4 pages if it tests a proposed Y2 comparison. The Ising critical behavior reviewed for this chain does not identify four-dimensional SU(5) or SO(10) Yang–Mills. Experiments establish neither the needed infinite-volume vacuum nor the hard core's uniform estimates.

**T0-start: no. T0-rate: no.** The review supplies methods and benchmarks, not the missing quantifiers.

## 13. Ludwig–Jakobs–Urbach 2026: retain the finite-register warning

**Work.** Paul Ludwig, Timo Jakobs and Carsten Urbach, *Scaling and Luescher Term in a non-Abelian (2+1)d SU(2) Quantum Link Model*. 2026. [arXiv:2602.23213v3](https://arxiv.org/abs/2602.23213v3), [primary text](https://arxiv.org/pdf/2602.23213v3). This is the July revision, not the earlier abstract returned by search.

**Result and hypotheses.** The model uses the five-dimensional SO(5) link representation on a hexagonal spatial lattice. Eq. (14) defines the fitted potential, V(r) = σr + γ/r + μ + O(r^−3). Sections V–VI and Figures 10 and 14 discuss scaling and systematic errors. The conclusion reports that “a continuum limit does not appear to exist” in the traditional sense. **Classification: numerical evidence, with a finite-order strong-coupling calculation.** The authors report substantial finite-size effects for γ and uncertain fit-error coverage. This is not a proved obstruction.

**Map and native rebuild.** It concerns a different group, embedding, representation, and dimension. It is a concrete warning against inferring a weak continuum corner from exact gauge symmetry alone. Rebuild the static-charge-sector definition and perturbative diagnostic in 3–6 pages on a suitable toy lattice. Applying it to the repo requires a separately specified plaquette class and state.

**T0-start: no. T0-rate: no.** Preserve the unfavorable evidence without exporting it as a no-go for either repo law.

## 14. Horn: the original finite-matrix construction

**Work.** D. Horn, *Finite Matrix Models with Continuous Local Gauge Invariance*. 1981, Physics Letters B 100, 149–151. [Primary author-hosted text](https://www.tau.ac.il/~horn/publications/horn1981.pdf), [publisher record](https://doi.org/10.1016/0370-2693(81)90763-2). **arXiv ID/version: NOT VERIFIED; none located for this pre-arXiv work.**

**Result and hypotheses.** Eqs. (1)–(11) give explicit five-state SU(2) link matrices. Eq. (10) is the vanishing plaquette/Gauss commutator, “thus guaranteeing gauge invariance”. **Classification: exact finite-matrix construction.** The article distinguishes its nonunitary V from a conventional group-valued link. Its expectation of shared physical features is not a universality proof. The later SU(N)×U(1) construction has restrictive dynamics in the sectors analyzed; that statement is about those matrices and Hamiltonian.

**Map and native rebuild.** This establishes historical credit and a simple algebraic test case. It does not analyze the repo's antisymmetric u(10) or spinorial so(20) register. Rebuild Eqs. (7)–(11), including normalizations and orientations, in 2–3 pages if needed as an independent small example. Do not transfer the article's special-sector spectral behavior to `L5-U`.

**T0-start: no. T0-rate: no.** No continuum convergence or error-rate theorem is established by this construction.

## 15. Orland–Rohrlich: primary-text access remains incomplete

**Work.** Peter Orland and Daniel Rohrlich, *Lattice Gauge Magnets: Local Isospin from Spin*. 1990, Nuclear Physics B 338, 647–672; preprint NBI-HE-89-33, 1989. [Publisher record](https://doi.org/10.1016/0550-3213(90)90646-U), [author's institutional abstract](https://cris.bgu.ac.il/en/publications/lattice-gauge-magnets-local-isospin-from-spin-2/). **arXiv ID/version: NOT VERIFIED; none located. Primary body and numbered theorem/equation locator: NOT VERIFIED.** The publisher body fetch failed; the INSPIRE record supplied no full-text document. No numbered result from this paper is imported here.

**Verified abstract-level claim.** The institutional abstract describes finite-dimensional SU(2) gauge magnets and an SO(5) realization. It reports excitations “gapless and nonrelativistic at the tree level”. It also describes an argued relation to topologically massive Yang–Mills in 2+1 dimensions. **Classification: reported tree-level/physics-level claims; body verification incomplete.** Neither report establishes the requested four-dimensional non-Abelian universality statement.

**Map and native rebuild.** Credit this work as an early gauge-magnet study. Fetch the body before using its dispersion calculation or model-specific conclusions. A native quadratic dispersion calculation for fully specified matrices should take roughly 3–6 pages; an estimate for reproducing this paper's unverified derivation is premature. **T0-start/T0-rate: no verified supply from the accessible material.**

## rebuild candidates

Order reflects potential movement of the actual open item, not how easy a lemma is. All remain proposed work. Fix `𝒜_k(g)`, the ZM1 map, the loop list, and VC1's state before claiming a comparison. A fixed one-scale moment error δ needs its own propagation bound before it can enter T0-rate.

| Priority | Native rebuild, with credit | Estimated proof size | Movement and remaining obligation |
|---|---|---|---|
| 1 | Exact coherent-state representation and observable dictionary for the actual `L5-U` update; use Brower et al., Schlittgen–Wiese, and Bär et al. | 8–15 pages for finite identities | Makes Y2's proposed start explicit. Must still prove positivity/reflection positivity, small-field control, and the VC1-state comparison. The U(1)-blind SU(5) loops need a fixed definition. |
| 2 | Finite-register block-loop moment bounds for Y2-W-L, using the explicit rishon algebra | 4–8 pages per bounded lemma; full dynamical estimate unknown | Directly tests the fixed `L5-U` window. Tensor-product representation content alone supplies no alignment or RG estimate. |
| 3 | SO(20) normalization, coherent symbols, and quantitative errors for one specified large highest-weight family; credit Brower et al. | 10–20 pages | Advances the available `L5-O[R]` register route. A chosen coherent state still needs comparison with the actual vacuum; a residual R-dependent error remains. |
| 4 | Restricted-flux operator comparison plus finite-time leakage/truncation bound; credit Chandrasekharan and Tong et al. | 15–25 pages including matching hypotheses | Gives a rigorous regulator-error component if the Hamiltonians and state tails match. Does not yield vacuum universality or uniform RG rates. |
| 5 | Conditional D-theory zero-mode reduction and coupling normalization; credit Chandrasekharan–Wiese and Brower et al. | 3–5 pages for the conditional leading action | Clarifies a route requiring an extra dimension. A full phase/reduction/error proof is open and does not apply directly to the current law. |
| 6 | Lower-dimensional benchmark and static-potential diagnostics; credit Zache et al., Beard et al., and Ludwig et al. | 4–8 pages for algebraic definitions | Tests proposed estimates and preserves failed corners. Numerical agreement or disagreement remains evidence, not proof of Y2 or its negation. |

