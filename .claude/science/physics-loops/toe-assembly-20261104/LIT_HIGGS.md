# Exact gauge symmetry and Higgs-type infrared content: literature for CH1-5O-i

Exact local `Spin(10)` invariance does not by itself forbid a Higgs description with a proper residual stabilizer `K` containing the SM image. It does forbid a nonzero local expectation value in a representation with no gauge singlet, in the invariant state required by CH1-5O-i. These statements concern different objects. The closest constructive result is the Fröhlich–Morchio–Strocchi (FMS) orbit construction. It supplies gauge-invariant composites and strings adapted to representations of a stabilizer, without changing the exact gauge law. Its group theory is rigorous; its identification of particle poles needs dynamics. Complementarity proves analyticity in specified fully Higgsed lattice models. It does not prove partial `Spin(10)` reduction. The SPT papers give exact examples and useful nonlocal diagnostics with additional protecting symmetries. They do not select the SM subgroup. The first native task should therefore define CH1-5O-i(a) through relational observables, screening and spectral data, then construct those observables from the existing registers. Proving the required stationary state and its infrared spectrum remains open. Here `H_SM` denotes the draft's `H`, and `K` denotes its proposed `G_∞`; this avoids confusing the SM image with the larger residual group. No literature citation below discharges a repo proof obligation.

## 1. Elitzur: the original local-symmetry result

**Source.** S. Elitzur, 1975, *Impossibility of spontaneously breaking local symmetries*, Physical Review D **12**, 3978–3982. [Publisher abstract](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.12.3978). **arXiv ID/version: none located; no arXiv abstract page found.** The publisher abstract was fetched. The original full text could not be fetched. Original theorem/equation number, precise hypotheses and proof: **NOT VERIFIED**. Abstract excerpt: “a spontaneous breaking of local symmetry”. This is historical attribution, not a substitute for checking the original proof. Sections 2–3 give accessible primary treatments.

**Result and hypotheses.** The abstract describes an argument without gauge fixing, demonstrated for Abelian lattice gauge fields. The familiar rigorous conclusion must be stated using the gauge average: the component with zero orbit average has zero expectation. A non-invariant operator can also have a singlet component. Its whole expectation need not vanish.

**Map to the law.** `LW1_5_DRAFT.md`, Lemma H, already uses compact-group averaging. CH1-5O-i explicitly requires a gauge-invariant state. That hypothesis directly supports the averaging argument, including for a stationary Floquet state. It does not require a Euclidean action or a Gauss-singlet vector.

**Native rebuild: 1–2 pages.** Credit Elitzur and prove the finite-support selection rule directly. For a finite set of sites `S`, define

\[
 E_S(A)=\int_{\operatorname{Spin}(10)^S}\alpha_g(A)\,dg.
\]

Show that `E_S` is a positive, unital projection onto the invariant algebra and that `ω(A)=ω(E_S(A))` for an invariant state. Thus `E_S(A)=0` implies `ω(A)=0`. Apply this separately at the endpoints of charged correlators. A bare separated charged two-point function can vanish identically; a correctly contracted transporter can avoid that selection rule. This settles the meaning of a local Higgs expectation. It does not determine `K` or any mass.

## 2. Splittorff: positivity and the order of limits

**Source.** K. Splittorff, 2003, *Impossibility of spontaneously breaking local symmetries and the sign problem*, [arXiv:hep-lat/0305013v1, abstract](https://arxiv.org/abs/hep-lat/0305013v1), [paper](https://arxiv.org/pdf/hep-lat/0305013v1). Both were fetched. **Exact locator:** the unnumbered “general criterion” in section IV, printed p. 4, following equations **(18)–(20)**. Excerpt: “If all bounded, local, and gauge invariant operators have finite vacuum expectation values”.

**Result and hypotheses.** This is an analytical criterion in the compact Abelian angular models actually treated. Equations (1)–(4) specify site angles, compact `U(1)` links and a periodic gauge-invariant action. The criterion concerns a bounded local operator with zero orbit average and the source-removal limit after the volume limit. Positive Euclidean weights satisfy the bounded-expectation requirement. Section V gives a signed-weight example with a volume-dependent coupling and a divergent bounded-observable expectation. It is not an ordinary positive quantum state. The paper explicitly leaves extension beyond its Abelian setting open.

**Map to the law.** A unitary tick is not a positive Euclidean Boltzmann weight. Conversely, a positive normalized operator-algebra state obeys `|ω(A)|≤||A||`. The signed-functional example does not invalidate compact averaging in the invariant state postulated by CH1-5O-i. It warns against deriving that state or its source limits from an unspecified path integral.

**Native rebuild: 2–3 pages.** Prove the norm bound and distinguish an invariant state from a singular source-selected functional. If a Euclidean representation is later introduced, prove its positivity and the required limiting statements separately. Do not transplant the Abelian criterion as a general `Spin(10)` theorem.

## 3. Tada and Koma: an explicit rigorous fermionic version

**Source.** Yasuhiro Tada and Tohru Koma, 2016, *Two No-Go Theorems on Superconductivity*, [arXiv:1605.06586v2, abstract](https://arxiv.org/abs/1605.06586v2), [paper](https://arxiv.org/pdf/1605.06586v2). Both were fetched. **Exact locator:** **Theorem 3.1**, equation **(3.6)**, with the limit defined in **(3.5)**. Excerpt: “The spontaneous magnetization for the Cooper pair is vanishing”.

**Result and hypotheses.** This is a rigorous thermal statement for their lattice fermion model. Section 3 uses spin-1/2 fermions, nearest-neighbor hopping with compact classical `U(1)` link phases, density interactions, a plaquette weight and explicit sources. The theorem removes those sources in the specified order after taking infinite volume, at fixed finite inverse temperature. It also treats the zero-flux limit; the text says the result holds at finite plaquette coupling. The proof uses a local transformation and a volume-independent source bound, equations (3.10)–(3.13). This theorem does not prove the Meissner effect.

**Map to the law.** It confirms that fermions do not make a local charged condensate an acceptable gauge-invariant order parameter. Its annealed classical links and thermal trace differ from the finite quantum links and stationary tick of `L5-O`. Its fixed-temperature estimate does not supply a zero-temperature or general Floquet theorem.

**Native rebuild: 3–5 pages if source limits are needed.** Reproduce the local-unitary/Duhamel bound for a specified bounded finite-register Hamiltonian and local source. Check constants uniformly in volume. For CH1-5O-i's already invariant state, section 1's shorter averaging proof suffices. Neither proof establishes a Higgs phase.

## 4. Osterwalder and Seiler: constructive lattice gauge theory

**Source.** Konrad Osterwalder and Erhard Seiler, 1978, *Gauge field theories on a lattice*, Annals of Physics **110**, 440–471, [publisher record and abstract](https://www.sciencedirect.com/science/article/pii/0003491678900398). **arXiv ID/version: none located; no arXiv abstract page found.** The abstract was fetched. Publisher PDF access failed; the publisher API returned metadata, not the paper. **Original theorem/equation number and full hypothesis set: NOT VERIFIED.** Abstract excerpt: “a rigorous treatment of the Higgs mechanism”.

**Result and verification boundary.** The abstract reports physical positivity, a positive self-adjoint transfer matrix, strong-coupling infinite-volume analyticity and a Higgs treatment. Those are reports from the authors' abstract. I cannot certify their exact theorem statements from that abstract. Fradkin–Shenker's accessible original appendix explicitly develops a fixed-length specialization of this work; section 5 below records the hypotheses and equation numbers actually read there. Numbers quoted there as references to Osterwalder–Seiler are not independently verified Osterwalder–Seiler locators here.

**Map to the law.** A positive transfer matrix would be useful for a Euclidean spectral construction. `L5-O` currently supplies a finite-depth unitary tick. Its quantum link entries are operators, rather than independent compact-group integration variables. Exact gauge covariance supplies neither a positive transfer matrix nor the cluster-expansion estimates.

**Native rebuild.** First specify an actual Euclidean action or transfer operator. Prove positivity, existence of the thermodynamic state and the relevant expansion estimates for that object. Estimate **20–40 pages for a narrowly specified comparison model**, not for a general bridge to `L5-O`. A faithful rebuild of the original theorem cannot be scoped until its full text is available. No unverified Osterwalder–Seiler theorem is imported here.

## 5. Fradkin and Shenker: what complementarity actually covers

**Source.** Eduardo Fradkin and Stephen H. Shenker, 1979, *Phase diagrams of lattice gauge theories with Higgs fields*, Physical Review D **19**, 3682–3697. [Publisher abstract](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.19.3682); [primary preprint, SLAC-PUB-2238, November 1978](https://inspirehep.net/files/3463fbf4f84192503347459aeed77d1f). Both were fetched; the preprint was read for the following locators. **arXiv ID/version: none located.** These are preprint equation numbers, not a claim about journal numbering. **Exact locators:** equation **(4.1)** and appendix equations **(A.1), (A.9), (A.14)**, printed pp. 36 and 43–47. Excerpt from the appendix: “H(U) has one maximum at U=I”.

**Rigorous content and hypotheses.** The convergent expansion establishes an analytic connection between confinement-like and Higgs-like regions for bounded local gauge-invariant observables, with exponential clustering in its domain. The appendix assumes compact Haar link variables, fixed-length Higgs fields removable in unitary gauge, and a link Higgs weight with a unique maximum at the identity. In their notation `K` multiplies plaquettes and `β` multiplies the Higgs link term. Equation (A.9) supplies a smallness condition; (A.14) supplies clustering. Section IV uses a group-valued `SU(N)` Higgs matrix. It explicitly explains that one fundamental vector generally does not fully Higgs `SU(N)`, and chooses the matrix realization instead.

**Limits of the result.** An analytic connecting corridor does not exclude transitions elsewhere. The appendix is a proof sketch relying on constructive estimates. Its local-observable result does not establish analyticity of every infinite string, boundary diagnostic or source-limit order parameter. The broader phase-diagram discussion also includes physics arguments; it is not all a theorem.

**Map to the law.** The central hypothesis is a trivial residual stabilizer, not the word “fundamental” alone. A `10` of `Spin(10)` cannot be assumed to satisfy it. A desired continuous `K⊇H_SM` deliberately leaves a nontrivial stabilizer. The draft also has no supplied classical Higgs field or verified Haar-link action. Complementarity therefore neither constructs CH1-5O-i nor excludes its partial-Higgs target. Exponential clustering of all local observables would, moreover, require care if the intended regime retains massless observable channels.

**Native rebuild: 15–30 pages for a controlled toy model.** Rebuild the polymer counting, partition-function ratios, convergence domain and clustering bound with explicit constants. Use that model to test proposed phase diagnostics. A transfer to finite quantum `Spin(10)` links requires new estimates. It is not a substitution of the group name in the old expansion.

## 6. Fröhlich, Morchio and Strocchi: the constructive bridge closest to this item

**Source.** J. Fröhlich, G. Morchio and F. Strocchi, 1981, *Higgs phenomenon without symmetry breaking order parameter*, Nuclear Physics B **190**, 553–582. [IHES record](https://archives.ihes.fr/document/P_81_12.pdf); [primary IHES/P/81/12 manuscript](https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/FROHLICH/1981-2002/P_81_12/P_81_12.pdf). The record and complete PDF were fetched. **arXiv ID/version: none located.** **Exact locators:** section **5.1**, the **unnumbered Theorem, Parts I–III**, printed pp. 24–27; the **unnumbered Lemma in section 6**, pp. 36–37; equations **(5.2), (6.1), (7.2)**. Excerpt from Part I: “there is a linear correspondence”. These manuscript locators were checked directly.

**Rigorous content and hypotheses.** For a finite-dimensional representation of a compact Lie group, fix a classical Higgs orbit and its stabilizer. The section 6 lemma extends an equivariant function on that orbit to an equivariant polynomial restricted to the orbit. The proof uses polynomial approximation, Haar averaging and finite dimensionality. Parts II–III construct covariant projections corresponding to stabilizer representations, and replace stabilizer-invariant strings by full-group-invariant strings. Projector identities hold on the selected orbit; the proof does not give globally idempotent polynomial matrices on the entire representation space.

**Physics content.** Sections 5.3 and 7 relate this construction to mass matrices and ordinary perturbation theory. Equation (7.2) fixes the matching at a chosen orbit point. Small-fluctuation spectral matching is a physics argument. It does not prove a nonperturbative mass gap, orbit selection or equality of exact particle spectra. The paper also leaves limits that create isolated charged states from strings as dynamical questions.

**Map to the law.** This addresses the central conceptual issue. Gauge-invariant observables can resolve stabilizer-adapted content without a nonzero gauge-variant local expectation. However, FMS starts with commuting classical Higgs coordinates. A fermion bilinear or a quantum-link tensor in this repo has noncommuting components. Substitution into a classical polynomial does not automatically preserve projector identities. Nor can the construction manufacture a forbidden local `16`: the draft's center restrictions on available operators still apply. Charged residual-group fields require a specified dressing or charge-sector construction. Bare local charged fields cannot simply be declared physical SM propagators.

**Native rebuild, with the decisive obligations exposed.** Rebuild the orbit lemma and projectors first, with credit to FMS. For a representation `R` of `G=Spin(10)` and an orbit label `v`, set `K=Stab_G(v)`. An orthogonal projector `P_i^0` onto a `K`-invariant summand gives

\[
 P_i(gv)=R(g)P_i^0R(g)^{-1}.
\]

Prove independence of the chosen coset representative and covariance. This part is **4–6 pages**. Keep the distinction between an orbit label and a quantum field explicit.

Then do the actual-law bridge, estimated **8–15 further pages for kinematics**:

1. Find an available bosonic covariant composite `Φ_x` in the existing site/link algebra. Prove its representation, locality and center kernel. Identify an orbit with `H_SM⊆K⊊Spin(10)`. Do not add an elementary Higgs variable as an unnamed premise.
2. Construct ordered composite operators and transporter contractions in that algebra. Prove gauge invariance directly. For example, with compatible representation indices, test operators of the form

   \[
   O_{ij}(x,y;\Gamma)=\Psi_x^\dagger P_i[\Phi_x]\,
   T_\Gamma\,P_j[\Phi_y]\Psi_y.
   \]

   Covariance can establish invariance even when a quantum-link transporter is not a group-valued unitary. Projector identities and spectral interpretation still need separate proofs.
3. Define “long-distance group `K`” operationally through these channels, screening sectors and effective interactions. A stabilizer calculation alone does not establish an infrared gauge theory. Check the exact global form of `K`, not just its Lie algebra.
4. Prove existence and stationarity of a suitable `ω`, the suppression of unwanted channels and the claimed light spectrum. State whether the result concerns an intermediate energy window or an asymptotic limit. A Floquet spectral measure lives on the unit circle; a positive-energy continuum interpretation is another bridge.

As a comparison calculation, rebuild the classical Higgs Gram matrix `M²_AB∝Re⟨T_Av,T_Bv⟩` and prove `ker M²=Lie(K)` in **2–3 pages**. This explains why exact covariance and a proper stabilizer are compatible. It gives no mass formula for `L5-O` until the required kinetic term and effective field are derived. **No responsible proof-size estimate exists yet for step 4.** That is the frontier obligation, not a routine consequence of FMS.

**Concrete first probe, proposed here.** The existing even bilinears `M_x^{ab}=(i/2)γ_{x,a}γ_{x,b}` supply an adjoint covariant tensor. Test a classical adjoint orbit label `A₀=diag(J,J,J,2J,2J)`, with `J` the real two-dimensional complex structure. Its proposed stabilizer is the inverse image of `U(3)×U(2)` under `Spin(10)→SO(10)`. Rebuild the centralizer calculation in **1–2 pages**: commuting with `A₀²` preserves the six-plus-four split; commuting with `A₀` then imposes the two unitary blocks. Check inclusion of the actual Case I SM image using `CG1_KILL_DRAFT.md`, Lemma C. This retains additional Abelian generators, so the family's charges and CH1-5O-i(c) still matter. This orbit is a comparison label, not `ω(M_x)`, which averaging makes zero. Its selection and a valid quantum realization are unproved. The proposal tests the FMS machinery without adding a Higgs degree of freedom or claiming a new physical breaking mechanism.

## 7. Borgs and Nill: a rigorous gauge-fixed broken phase

**Source.** Christian Borgs and Florian Nill, 1986, *Symmetry breaking in Landau gauge—a comment to a paper by T. Kennedy and C. King*, Communications in Mathematical Physics **104**, 349–352. [Publisher abstract](https://link.springer.com/article/10.1007/BF01211600). **arXiv ID/version: none located; no arXiv abstract page found.** The abstract was fetched. Full-text requests returned a subscription page. **Theorem/equation number, exact parameter inequalities and full proof: NOT VERIFIED.** Abstract excerpt: “there are states parametrized by an angle”.

**Reported result and hypotheses.** The abstract reports a family of Landau-gauge states of the noncompact Abelian lattice Higgs model with a positive scalar expectation at one angle and the corresponding phase rotation at other angles. The parameter range is referred to another work; it cannot be recovered from this abstract. This is a report of a rigorous result in a gauge-fixed model, not a verified native theorem here.

**Map to the law.** The broken symmetry is a remnant global symmetry after gauge fixing. The exact local automorphisms of `L5-O` are a different object. A Landau-gauge expectation cannot certify `K` independently of the gauge prescription. Conversely, the result should not be misreported as a theorem that all Higgs phenomena are impossible with exact gauge symmetry.

**Native rebuild.** Once the full proof is available, reproduce its state construction before using its parameter region; proof size is **not estimable from the abstract**. A useful independent comparison lemma takes **1–2 pages**: Haar-average a finite-volume state over local transformations, show that gauge-invariant expectations are preserved, and pass to an invariant weak-* limit. This restores invariance of the state. It does not prove the original state had the desired spectrum or that a chosen remnant subgroup is physical.

## 8. Borgs and Nill: the Abelian phase-diagram review

**Source.** Christian Borgs and Florian Nill, 1987, *The phase diagram of the Abelian lattice Higgs model. A review of rigorous results*, Journal of Statistical Physics **47**, 877–904. [Publisher abstract](https://link.springer.com/article/10.1007/BF01206163). **arXiv ID/version: none located; no arXiv abstract page found.** The abstract was fetched. The PDF request returned the subscription page. **Exact theorem/equation numbers and individual theorem hypotheses: NOT VERIFIED.** Abstract excerpt: “Higgs mechanism (gauge-independent) and spontaneous symmetry breaking (gauge-dependent)”.

**Scope and verification boundary.** The review covers compact `U(1)` and noncompact `R` lattice Higgs models and discusses Gribov copies. Its abstract confirms that scope and the distinction in the excerpt. It does not expose enough detail to certify a particular mass, long-range-order or analyticity theorem. No such theorem is attributed a guessed number here. This review is a source map, not an original proof used by this lane.

**Map to the law.** Compactness, gauge prescription, representation and observable all matter. In particular, an Abelian noncompact theorem cannot be transferred to finite quantum `Spin(10)` registers by analogy. A gauge-fixed condensate, a gauge-invariant screening criterion and a photon mass answer different questions.

**Native rebuild.** Rebuild definitions of the diagnostics actually selected for CH1, with an explicit state and order of limits; allow **2–4 pages**. A particular theorem rebuild remains **unscoped until its primary text and hypotheses are available**. This entry identifies an access gap, not evidence for or against CH1-5O-i.

## 9. Greensite and Matsuyama: a nonlocal custodial diagnostic

**Source.** Jeff Greensite and Kazue Matsuyama, 2018, *What symmetry is actually broken in the Higgs phase of a gauge-Higgs theory?*, [arXiv:1805.00985v2, abstract](https://arxiv.org/abs/1805.00985v2), [paper](https://arxiv.org/pdf/1805.00985v2). Both were fetched. **Exact locators:** equations **(12)–(16)**, particularly **(15)** for `Φ[U]`; action **(2)**. Excerpt: “Such an order parameter must be inherently non-local”.

**Result and hypotheses.** In the Wilson `SU(2)` model with a single fixed-length fundamental doublet, the scalar sector has an additional global custodial `SU(2)`. At fixed gauge links, the scalar average transforms covariantly. Its modulus gives a gauge-invariant diagnostic. Equation (15) takes infinite volume before infinite fictitious sampling time. The authors also study a fixed-length fundamental `SU(3)` model with a global `U(1)`. The plotted transition lines are **numerical evidence**. The proposed coincidence with a separation-of-charge confinement transition is explicitly a **conjecture** in this version. The order parameter's nonlocal limits fall outside a finite-local-observable analyticity theorem.

**Map to the law.** This detects a specified global scalar-sector symmetry. It does not detect a literal breaking of all exact local transformations, nor does its value identify a residual gauge subgroup. No corresponding custodial scalar symmetry has been established for `L5-O`. Freezing classical link matrices also has no immediate meaning for all noncommuting quantum-link entries.

**Native rebuild: 3–5 pages for covariance and definitions.** First identify an actual commuting conditioning algebra or a valid quantum replica construction. Then prove covariance, invariance of the diagnostic and the meaning of its limits. A nonzero value would diagnose that construction. It would still need a separate bridge to `K` and the SM spectral channels. Monte Carlo extrapolations could guide that bridge but could not prove it.

## 10. Greensite and Matsuyama: a source-defined spin-glass order parameter

**Source.** Jeff Greensite and Kazue Matsuyama, 2020, *The Higgs phase as a spin glass, and the transition between varieties of confinement*, [arXiv:2001.03068v1, abstract](https://arxiv.org/abs/2001.03068v1), [paper](https://arxiv.org/pdf/2001.03068v1). Both were fetched. **Exact locators:** definitions **(8)–(15)**, gauge covariance **(23)**, gauge invariance **(26)** and the phase criterion **(32)**. Excerpt following (26): “which establishes the gauge invariance of the spin glass order parameter”.

**Result and hypotheses.** The paper defines a conditional scalar average from a positive thermal diagonal kernel, adds a source, optimizes its orientation, and averages the modulus over spatial gauge fields with the prescribed marginal distribution. The changes of variables in (16)–(26) establish covariance and invariance. Source removal follows infinite volume. Their setting is `U(1)` or `SU(N)` with a single fundamental scalar; `SU(2)` is the numerical example. These identities are analytical results. A nonzero thermodynamic limit and a universal physical characterization do not follow from covariance alone. Figure 1 is **numerical evidence**; the broader confinement interpretation uses further arguments and assumptions.

**Map to the law.** The source prescription improves the precision of the diagnostic. It still needs an actual scalar-sector symmetry, a positive kernel and well-defined conditioning. A general invariant stationary state of a quantum circuit supplies none of those particular constructions automatically.

**Native rebuild: 4–6 pages.** Prove a quantum version of the conditional/replica observable for the chosen algebra, and its covariance under exact `Spin(10)`. Define any optimization by its supremum value, without assuming uniqueness of a maximizing configuration. Prove the limiting state exists. Treat the claim that this diagnostic identifies the desired `K` as a separate spectral obligation. Use it as a secondary diagnostic after the FMS operator construction.

## 11. Verresen, Borla, Vishwanath, Moroz and Thorngren: discrete Higgs as SPT

**Source.** Ruben Verresen, Umberto Borla, Ashvin Vishwanath, Sergej Moroz and Ryan Thorngren, 2022; version revised 2024, *Higgs Condensates are Symmetry-Protected Topological Phases: I. Discrete Symmetries*, [arXiv:2211.01376v2, abstract](https://arxiv.org/abs/2211.01376v2), [paper](https://arxiv.org/pdf/2211.01376v2). Both were fetched. **Exact locators:** hard Gauss law **(18)**, Hamiltonian **(19)**, fixed-point stabilizers **(20)**, open string **(21)** and boundary action **(23)**. Excerpt from section 4.2: “the former is simply the Gauss law”.

**Exact content and hypotheses.** The model has vertex and link qubits in `2+1D`, `Z₂` gauge symmetry, Ising matter and the hard constraint `G_v=X_v∏σ_l^x=1`. At the large-hopping fixed point, (20) is an exactly checkable commuting-stabilizer description. The gauge-invariant open string has unit expectation there. Magnetic one-form symmetry is exact when the electric-field perturbation `h` vanishes. On the rough boundary used in section 4.4, the matter symmetry acts through boundary links, equation (23). Anticommuting symmetry actions yield exact degeneracy statements. Extension across a gapped symmetry-preserving phase requires phase-stability assumptions. The boundary phase diagram at nonzero `h` includes **tensor-network numerical evidence**, not a general theorem.

**Map to the law.** This is a concrete model with exact gauge symmetry and nontrivial Higgs diagnostics. The additional matter and magnetic symmetries are essential. On a closed constrained lattice the product of Gauss laws makes the total matter parity trivial; boundaries, extra matter or an emergent constraint affect its interpretation. `L5-O[S_+]` has no demonstrated counterpart of these protecting symmetries. Its draft also reports no local Gauss-singlet sector with the uniform register choice. One must not silently replace invariance of a state under conjugation by the paper's hard singlet constraint.

**Native rebuild: 3–5 pages for the exact toy algebra.** Rebuild the stabilizers, string expectation and boundary symmetry algebra analytically. Then inventory which operators and symmetries actually survive in the finite-register `Spin(10)` law. This gives a useful check of diagnostic definitions. It does not produce partial non-Abelian Higgsing or an SM family.

## 12. Thorngren, Rakovszky, Verresen and Vishwanath: continuous Higgs response

**Source.** Ryan Thorngren, Tibor Rakovszky, Ruben Verresen and Ashvin Vishwanath, 2023, *Higgs Condensates are Symmetry-Protected Topological Phases: II. U(1) Gauge Theory and Superconductors*, [arXiv:2303.08136v1, abstract](https://arxiv.org/abs/2303.08136v1), [paper](https://arxiv.org/pdf/2303.08136v1). Both were fetched. **Exact locators:** Landau–Ginzburg action **(56)**, infrared constraint **(63)**, response **(64)** and partial-Higgs response **(65)**. Excerpt: “a symmetry-enriched topological (SET) phase rather than an SPT”.

**Result and hypotheses.** For a gapped Higgs regime in `d≥2` spatial dimensions, the scalar has gauge charge `m` and charge `q` under an independent global matter `U(1)`. Absence of monopoles supplies magnetic `(d−2)`-form symmetry. Integrating the fixed-point constraint gives, for `m=1`,

\[
 S_{\mathrm{SPT}}=\frac{q}{2\pi}\int B_{\mathrm{mag}}\wedge dA_{\mathrm{mat}}.
\]

For `m>1`, residual discrete gauge structure requires an SET description. The derivation is an **effective-field-theory argument**, supported by quantization and anomaly reasoning. It is not a constructive existence theorem for an arbitrary microscopic lattice action. In `3+1D`, exact magnetic one-form symmetry needs the stated monopole restriction. Section 3.1 explains that spectators or other structure may be needed to distinguish global matter charge from gauge charge.

**Map to the law.** This classifies a response after the Higgs regime and protecting symmetries are supplied. Exact `Spin(10)` alone supplies neither that independent global `U(1)` nor a monopole-free Abelian magnetic symmetry. The subgroup `U(1)_N` inside a gauge group is not automatically an independent protecting global symmetry. A partially Higgsed theory with light continuous gauge sectors is also outside the simplest fully gapped SPT target.

**Native rebuild: 4–8 pages for a specified Abelian comparison sector.** Use integral lattice cochains to rebuild gauge invariance, response quantization and boundary variation. Verify the actual charge lattice, defects, monopoles and possible residual topological order. Only apply the response after those microscopic hypotheses are proved. It can then distinguish candidate regimes; it cannot select `K⊇H_SM` or establish the chiral spectrum.

**Source checkpoint and remaining decision.** Searched live on 2026-11-05 through arXiv, publisher records, INSPIRE, IHES and author/institutional-copy routes. Every listed arXiv abstract and pinned PDF was fetched. The older works have no located arXiv version; the unavailable originals are explicitly marked above. Exact locators refer to the pinned PDFs, not regenerated HTML. Downloaded evidence is under `/private/tmp/lit-higgs-20261105/`. Repo baseline: actual branch `toe-assembly-local`, HEAD `2d0adc0c022753469151385e1789a4f444585ca6`; no branch switch or fetch. Read the full CH1-5O-i statement in `CH1_5_DRAFT.md` section 5.2, its conventions, `LW1_5_DRAFT.md` sections 4.4 and 8.1, the relevant center statements in `LW1_5O_DRAFT.md`, and `CG1_KILL_DRAFT.md` Lemma C with its proof and embedding conventions. SHA-256: `CH1_5_DRAFT.md` = `879002bdde3b9ddb0a4d4ae39ed2e35ecb5c44f973f6e67ef66d0a8192f1bf2d`; `LW1_5_DRAFT.md` = `ff2f7b51da584c25c12eb94ad614acf910b949d8b1a925005ee5ebf6f21ecf06`; `LW1_5O_DRAFT.md` = `992096e18a3fdbfe6887a7ae410796d424f5fb13f06122ddeb6764034b8fc8cf`. `CG1_KILL_DRAFT.md` = `46ce7c0695ef74aae258bf6e2e39aed6d5c5f31a11e8caaf6e68d987f11ec58d`. These are provisional drafts, not retained science. The live decision is which available composite and relational spectral criterion to test first. The failed transfers are explicit: local condensate, full-Higgs complementarity without its hypotheses, classical polynomial substitution into noncommuting fields, and SPT classification without its protecting symmetries. This literature survey supplies no independent proof check, audit status or stationary-state existence proof. Page estimates concern ordinary written proofs, not Lean line counts.

## Rebuild candidates

| Priority | Native candidate and credit | Estimated proof size | Movement on CH1-5O-i |
|---|---|---|---|
| 1 | FMS orbit/projector lemma; adjoint-bilinear orbit probe; actual-law relational composites | 4–6 pp. group theory; 1–2 pp. centralizer; 8–15 pp. operator bridge | Tests a concrete proper stabilizer containing the Case I SM image. Quantum orbit selection and direct noncommutative checks remain open. |
| 2 | FMS-informed classical Gram-matrix comparison, followed by an actual-law spectral theorem | 2–3 pp. comparison; dynamical proof unscoped | Identifies the decisive gap: prove `K`-type light channels and suppression of unwanted channels in a stationary state. A classical mass matrix alone does not close it. |
| 3 | Elitzur compact averaging; thermal source bound following Tada–Koma when applicable | 1–2 pp.; 3–5 pp. with source limits | Settles which expectations can be nonzero and forces a precise reading of clause (a). Does not select a subgroup. |
| 4 | Fradkin–Shenker/Osterwalder–Seiler expansion in an explicitly matched comparison model | 15–30 pp.; original OS text still needed | Controls a limited analytic regime and tests phase diagnostics. Fully Higgsed hypotheses do not yet match the target. |
| 5 | Greensite–Matsuyama quantum conditional/replica diagnostic | 4–6 pp. definitions and covariance; phase proof unscoped | Adds an invariant diagnostic if the needed global symmetry and limits exist. No subgroup or spectrum theorem follows from covariance. |
| 6 | Verresen–Borla–Vishwanath–Moroz–Thorngren stabilizer/string/boundary algebra | 3–5 pp. | Gives an exact small-model check. Requires a new bridge to this law's algebra and constraints. |
| 7 | Thorngren–Rakovszky–Verresen–Vishwanath cochain response in a derived Abelian sector | 4–8 pp. | Classifies an already established regime with verified protecting symmetries. Does not establish partial `Spin(10)` content. |
