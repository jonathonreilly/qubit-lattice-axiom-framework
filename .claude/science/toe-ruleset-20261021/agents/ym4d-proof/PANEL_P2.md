# PANEL P2 — OS1 without uniqueness or a mass gap

## PRE-STATED — 2026-10-28 22:28:09 UTC

**OPEN — question.** Can one select a continuum/infinite-volume limit of pure four-dimensional SU(N) lattice gauge theory which is E(4)-invariant, reflection positive (RP), gauge invariant, and not free, without assuming uniqueness of the infinite-volume state or a mass gap? The requested target remains OS0–OS3 on R^4; a torus theorem or a symmetry statement alone is not completion.

**OPEN — test contract.** I will test spatial averaging, covariant flowed observables, invariant sets and fixed points, ultraviolet universality, and a direct finite-volume symmetry-defect argument. Success is a complete abstract implication with precise additional estimates genuinely different from uniqueness, together with an honest account of whether those estimates are available for this Yang–Mills construction. A counterexample to an averaging shortcut defeats that shortcut only. I will not promote any lane label to evidence.

**OPEN — what would change my mind.** A common-reflection positivity theorem for the entire rotation orbit would rehabilitate full rotational averaging. A proof that the relevant admissible limit set is convex, rotation invariant, and RP for the same reflection would rehabilitate a fixed-point argument. A local rotational-defect estimate along a single cofinal family of boxes would remove uniqueness from a universality argument. Conversely, a proof that a proposed estimate already implies boundary-condition independence for all local observables would defeat my claim that it is weaker than uniqueness. Failure to find such an estimate is not an impossibility theorem.

**CONDITIONAL — evidence protocol.** The supplied task fixes the model and target. All scientific statements below carry PROVEN (argument supplied here), ARGUED (specified gap), CONDITIONAL (named hypotheses), OPEN, or [m] (unverified literature memory). Definitions and proposed estimates introduce no established Yang–Mills input. References to lane documents use section names/search strings because lines drift. Only this deliverable is written; no git operations are used. PLAN_S26.md will be read only after the independent analysis has been written.

## 1. Independent assessment of the supplied premises

**ARGUED — principal finding.** The necessity claim is too strong. Selecting one symmetric limit requires control of symmetry defects along one family of approximants. Uniqueness requires identifying limits from different subsequences and boundary conditions. These are different obligations. I give a precise selection theorem below, but do not establish its quantitative hypotheses for four-dimensional Yang–Mills.

**PROVEN — what the documents actually say.** PROOF §0 uses the categorical wording that averaging destroys RP, but L9b, Remark R9.1 itself says this is not an impossibility proof. L9b-γ1 says infinite-volume uniqueness is *probably* needed. EXISTENCE §4, X-ROT, makes the same qualification, whereas §5, X-IR, lists universality under a stronger necessity heading. Neither passage supplies a theorem making uniqueness necessary. This is a comparison of the inspected passages, not acceptance of their scientific status.

**OPEN — inputs not certified here.** The continuum local observable algebra, its continuous Euclidean action, uniform source bounds for OS0, the soft-block/physical-observable bridge, local large-field control uniform in volume, and a genuine non-free witness remain obligations. Compactness of compact link variables alone does not discharge them. The distinctions in EXISTENCE §0 between non-flatness, non-Haar behaviour, a nontrivial OS Hilbert space, and exclusion of a free theory must be preserved.

**PROVEN — scope of the layer-1 target.** REVIEW_S22, “Statement (BFT),” concerns critical background fields on a small-field branch, their derivatives, polymer actions, and a slice Hessian. Its BFT-0 uniqueness is uniqueness of a critical point in a prescribed neighbourhood modulo gauges. It is not uniqueness of an infinite-volume probability state. BFT-3's exponential locality is a bound on derivatives of background fields/actions in coarse-block distance; its statement is not a bound on full-measure connected stress-tensor correlations at arbitrarily large physical separations. No rotational Ward identity or renormalized stress-tensor source estimate appears in that statement. These are direct scope comparisons, independent of whether BFT can be proved.

**ARGUED — methodology scope.** The local bounded-investigation and no-go procedures are used for alternative routes, counterexamples and explicit gaps. Their campaign, multi-artifact and landing machinery is outside this one-file panel assignment. The inspected local snapshot supplies methodology only; no scientific authority or remote freshness is inferred from it. No other framework's isotropy premise is imported into pure SU(N) Yang–Mills.

## 2. The positivity algebra and a tested failure of full averaging

**CONDITIONAL — common setting used below.** Let A be a commutative local gauge-invariant observable *-algebra, with compatible Euclidean pullbacks α_g, an antilinear reflection Θ across x_0=0, and positive-half algebra A_+. In formulas, ΘF means the complex conjugate of F pulled back by the reflection. A state is RP if q_ω(F)=ω((ΘF)F)≥0 for every F∈A_+. Assume the indicated products and moments are continuous in the topology used to take limits. This common algebra and topology are hypotheses, not consequences of the soft-block construction.

**PROVEN — elementary closure facts.** The conditions Im q_ω(F)=0 and Re q_ω(F)≥0 are closed real-affine conditions in ω, so states RP for one fixed Θ form a closed convex set. If g preserves the positive half-space and commutes with Θ, α_g takes A_+ into itself and

    q_(g·ω)(F) = q_ω(α_g F) ≥ 0,

up to the immaterial convention of replacing g by g^{-1}. Thus averaging over spatial SO(3) preserves time RP. For a general rotation the right-hand side instead involves a conjugated reflection and a different positive half-space. Its sign is not controlled by time RP. Rotations and convex averaging preserve gauge invariance when the action on the common algebra intertwines gauge transformations.

**PROVEN — explicit stationary counterexample to unrestricted rotational averaging.** This is a scalar test of the operation, not a Yang–Mills counterexample. Let

    φ(x)=A cos(x_1)+B sin(x_1),

where A,B are independent real standard Gaussian variables. Its law is translation invariant: translating x_1 orthogonally rotates (A,B), and translations in other coordinates do nothing. It is time RP because every sample is independent of x_0, so (ΘF)F=|F|². Average this law over SO(4). The resulting stationary, rotation-invariant law has covariance on the time axis

    C(s)=∫_(S³) cos(s v_0) dσ(v),
    C(0)=1,  C''(0)=-∫v_0²dσ=-1/4.

The last equality follows from coordinate symmetry and Σv_μ²=1. For the positive-time observable F_ε=φ(ε,0)-φ(2ε,0),

    q(F_ε)=C(2ε)-2C(3ε)+C(4ε)
           =-ε²/4+O(ε⁴)<0

for sufficiently small ε>0. Taylor's remainder is bounded because |v_0|≤1; this is an exact analytic sign argument, with no numerical approximation. Narrow smooth smearing of the two evaluations preserves the strict negative sign, by continuity of this covariance. Thus even translation invariance does not rescue the averaging operation. Conversely, an already E(4)-invariant RP state is unchanged by averaging: “always destroys RP” is false; “does not in general preserve RP” is the correct statement.

## 3. Route (a): spatial rotations, with the missing axis exchange exposed

**PROVEN — what spatial averaging buys.** Write K=SO(3) fixing e_0 and P_Kω=∫_K k·ω dk. It gives K-invariance, time RP, and gauge invariance under the hypotheses of §2. Translation invariance is also retained if ω already has it. It supplies neither rotations mixing time and space nor continuous translations if those were absent.

**PROVEN — the crucial group lemma.** A state invariant under the hypercubic group H_4 and all rotations in the single spatial plane (1,2) is invariant under O(4). Indeed, conjugation by signed coordinate permutations turns the (1,2) plane rotations into rotations in every coordinate plane, including (0,i). Coordinate-plane rotations generate SO(4): successively rotate a unit column vector to a coordinate vector and induct on the orthogonal complement, equivalently the elementary Givens elimination of an orthogonal matrix. H_4 contains a determinant-minus-one reflection, giving the other component of O(4). A continuous action is sufficient to replace “all angles” by a dense set of angles. In particular, spatial SO(3) plus one suitable time/space axis exchange already gives the same conclusion.

**PROVEN — why two successive averages do not prove this lemma's hypotheses.** For h exchanging e_0 and e_1,

    h P_Kω = P_(hKh^{-1}) hω.

Even when hω=ω, the subgroup on the right is a different SO(3), so equality with P_Kω has not been shown. Spatial averaging can lose the original axis-exchange symmetry. Subsequently averaging over H_4 acts on states known RP only for the time plane, and the terms with time/space exchanges require spatial-plane RP which the first average did not establish. Only the subgroup of H_4 fixing the time direction belongs to the immediate common-reflection argument. Alternating these projections has the same unresolved positivity step.

**OPEN — exact price if averaging is retained.** For the spatially averaged candidate one must additionally prove, for every local F,

    (P_Kω)(α_h F)=(P_Kω)(F),

with a time/space exchange h, or prove RP for all conjugate planes throughout an averaging scheme. The first condition already supplies the missing rotations by the group lemma; merely naming it does not advance the proof.

**CONDITIONAL — better use of the group lemma.** Keep a single unaveraged subsequence with exact H_4 covariance, and prove only the (1,2) spatial rotational-defect estimate in §7. Then all rotations follow on that same state; its original RP and any non-free witness are preserved without averaging. This requires symmetry restoration, not uniqueness. Exact H_4 symmetry must act on the eventual physical local algebra, not solely on a set of block marginal laws. This is the most useful part of route (a).

## 4. Route (b): covariant flow helps define observables, not their law

**PROVEN — equivariance does not imply invariance.** If the flow map Φ_t obeys Φ_t(gA)=gΦ_t(A), then (Φ_t)_*(g_*μ)=g_*((Φ_t)_*μ). This identity does not assert g_*((Φ_t)_*μ)=(Φ_t)_*μ. A Dirac law at an asymmetric smooth input already disproves the latter inference. An exactly rotation-covariant continuum definition of a flowed observable therefore cannot by itself give OS1 for its random law.

**PROVEN — time smoothing can destroy RP even for a free input.** Consider a free scalar field with positive energy ω_p=(|p|²+m²)^{1/2}, m>0, and apply four-dimensional heat flow for time t>0. At a fixed spatial momentum its covariance is, with a positive normalization suppressed,

    C_t(s;p)=∫_R exp(ip_0s) exp[-2t(p_0²+|p|²)]
                      /(p_0²+ω_p²) dp_0.

It is smooth and even in s, and C_t''(0;p) is strictly negative because it is minus the integral of a strictly positive integrable function. The same positive-time difference used in §2 has RP form C_t''(0;p) ε²+O(ε⁴)<0. Real spatial wave packets give the same sign after integrating against their nonnegative squared Fourier transform. The unsmoothed free field is RP: its reflected covariance is exp[-ω_p(t+s)]/(2ω_p), a positive rank-one kernel for each p. Gaussian exponential moments extend that kernel positivity to the observable algebra. Thus “flow commutes with reflection” is not a support-preservation theorem and does not preserve OS2.

**CONDITIONAL — a valid two-family transfer.** One needs all of the following, on a single joint limiting state:

1. **OPEN (FLOW-LAW):** convergence of joint flowed observables and a genuine rotational-defect bound for their expectations, including products and all transformed test functions. Equivariance is insufficient.
2. **OPEN (LOCAL-BRIDGE):** physical positive-half observables F can be approximated by positive-half lattice/block observables G_j, with the reflected approximations as well, and with errors tending to zero in L². A useful flow version for support distance d>0 is δ(t,d)≤C exp[-c d²/t], together with a renormalized t↓0 limit and adequate product/moment bounds.
3. **OPEN (COMMON-ALGEBRA):** the two descriptions identify the same local state and its Euclidean action, including contact terms and a separating observable family; equality of selected one-point functions is insufficient.
4. **OPEN (SOURCE/NT):** bounds for OS0 and a non-free witness survive that identification and the t↓0 limit.

**PROVEN — quantitative positivity transfer.** If ||F-G||_2≤δ, ||ΘF-ΘG||_2≤δ, ||ΘG||_2=||G||_2≤M, and G is positive-half local, expansion of F=G+(F-G) and Cauchy–Schwarz give

    Re ω((ΘF)F) ≥ -2Mδ-δ².

The corresponding imaginary part tends to zero with δ. Hence vanishing error transfers RP. At fixed d,t>0 an exponentially small error is still nonzero and proves only approximate RP. One must actually send δ to zero. This is the distinction relevant to EXISTENCE, X-ARP and H-loc.

**ARGUED — strength and usefulness.** The bridge can be proved along one selected sequence and requires no boundary-condition uniqueness. FLOW-LAW is still the central symmetry obligation; flow does not remove it. Four-dimensional global flow for the limiting rough fields, source renormalization, and the local bridge are additional analytic work. Spatial-only flow avoids spreading across the time plane, but its definition distinguishes time and therefore reopens the axis-exchange obligation of §3.

**CONDITIONAL — literature scope, independently checked.** Lüscher–Weisz establish finiteness of positive-flow-time correlation functions *to all orders of perturbation theory*, after usual four-dimensional renormalization; this is not the required nonperturbative limit/positivity theorem ([arXiv:1101.0963](https://arxiv.org/abs/1101.0963)). Cao–Chatterjee construct a state-space framework on the three-dimensional unit torus under GFF-type hypotheses; this is a template, not a four-dimensional input ([arXiv:2111.12813](https://arxiv.org/abs/2111.12813)). These scope statements were checked against the authors' abstracts; neither full proof is imported here.

## 5. Route (c): invariant sets, fixed points, and decomposition

**PROVEN — the usable compact-group statement.** Let C be a nonempty compact convex set of admissible states, invariant under a continuous affine SO(4) action, and contained in the RP cone for the *same* time reflection. The Haar barycentre of any ω∈C belongs to C (as a limit of convex combinations), is SO(4)-invariant by Haar invariance, and remains RP by closed convexity. If all members are translation invariant and one retains a coordinate reflection, the result is E(4)-invariant. No uniqueness, extremality or mass gap is used.

**PROVEN — where the proposed application hides its cost.** A rotation-stable set C contained in that common RP cone automatically has every member RP for every rotated plane: apply common-plane RP to g·ω and conjugate back. Constructing such a C therefore requires all-plane positivity, or an equivalent bridge, not just RP for the plane aligned with each individual lattice. The union of rotated lattice limit sets has orbit closure, but lacks this common-reflection property. Intersecting with the time-RP cone restores positivity but need not preserve rotation stability.

**PROVEN — convexity and provenance are separate issues.** The limit-point set of a sequence need not be convex: a sequence alternating between two different states has just those two limit points. Its convex hull adds new states. For lattice measures, mixtures over boundary conditions or orientations must be explicitly included in the allowed approximating family or shown realizable by that family. An abstract barycentre in a larger state space is not, on that fact alone, a subsequential limit of the prescribed deterministic Wilson measures. A Gibbs-specification convexity theorem, if available with the required continuum control, could address provenance, but is a named extra input here.

**CONDITIONAL — translations in a fixed-point construction.** If C is also translation stable and every translate remains in the same RP cone, averaging over larger and larger boxes and taking a limit gives translation invariance: for any fixed shift, the average changes by at most 2||F|| times the relative symmetric-difference volume, which tends to zero. SO(4) averaging can then be performed in the translation-invariant part of C. The assumption about translates amounts to control of displaced reflection planes as well; E(4) has no normalized Haar probability with which to bypass this step.

**PROVEN — extremality is not a symmetry selector.** On the compact convex set of probability measures on S³, rotations act continuously and the extreme points are point masses. No point mass is rotation invariant, whereas uniform measure is. Thus “choose an extreme point of a rotation-invariant set” is not a fixed-point argument. Nothing in OS0–OS3 requires making this choice in the first place.

**PROVEN — RP is not hereditary under arbitrary decomposition.** On two spins X_+,X_-∈{−1,1}, reflection exchanges the spins. The independent uniform law is RP, since E[(ΘF)F]=|E F(X_+)|². It is half the aligned law (X_-=X_+) and half the anti-aligned law (X_-=-X_+), each with a fair sign. For F(X_+)=X_+, the anti-aligned law has RP form −1. Both component laws are reflection invariant. Thus a decomposition theorem needs a positivity argument; linearity of RP does not give one. This finite example does not assert that a specific translation-ergodic decomposition of the Yang–Mills state fails.

**CONDITIONAL — when a decomposition argument could work.** Suppose the sector parameter ξ is reflection invariant and bounded sector functions h(ξ) have uniformly bounded positive-half approximants H_n satisfying H_n→h(ξ) and ΘH_n→overline{h(ξ)} in L². For bounded F∈A_+, apply RP to H_nF and pass to the limit:

    ∫ |h(ξ)|² q_(ω_ξ)(F) dν(ξ) ≥ 0.

Varying h and a countable determining set of F gives RP in almost every component. The two-sided approximation and invariance of ξ are the substantive assumptions. Even then rotations can permute components; RP components need not be rotation-invariant components. OS4 is outside the requested theorem, so decomposition is an unnecessary risk unless it supplies a separate useful estimate.

**OPEN — exact price of route (c).** Exhibit a nonempty *admissible* compact convex rotation-stable subset of the common-reflection RP cone, with the local algebra and source bounds already under control. This is a genuine sufficient condition weaker than a singleton limit set, but there is no construction of that subset in the inspected layer-1 theorem. Calling the enlarged set “all limit points” does not establish its convexity, positivity or admissibility.

**CONDITIONAL — a weaker averaging repair.** Common-plane RP for every orbit member is sufficient, not necessary. For ν_n=∫g·μ_n dg it is enough to prove, for each positive-half F,

    Re ∫ μ_n(α_g[(ΘF)F]) dg ≥ -ε_n(F),  ε_n(F)→0,

and vanishing imaginary part, together with the continuity needed to pass to the limit. This only controls the angular average of the RP defect. It avoids uniqueness, but is currently a restatement of the missing positivity for this candidate unless accompanied by a new estimate or positive-kernel representation. Its lattice-limit provenance must also be checked. Replacing an oblique plane by a doubled half-lattice does not localize all changes to a thin seam: reflection changes the lattice orientation throughout the opposite half-space, so a regulator-comparison estimate is still needed.

## 6. Route (d): what ultraviolet universality can and cannot propagate

**PROVEN — leading UV behaviour, hypercubic symmetry and coordinate RP do not force rotations.** A second scalar diagnostic makes all three hypotheses coexist. Let φ be the sum of a massless four-dimensional Gaussian free field and four independent stationary one-dimensional Gaussian processes η_μ(x_μ) of covariance exp(-|s-t|), all independent. Its covariance away from the free-field diagonal is

    C(x-y)=1/(4π²|x-y|²)+Σ_(μ=0)^3 exp(-|x_μ-y_μ|).

Existence of the added processes follows from the nonnegative spectral density 2/(1+p²); the free covariance has nonnegative Fourier density 1/p². The law is translation invariant and H_4-invariant. It is time RP: the μ=0 summand has reflected kernel exp[-(t+s)], of rank one and positive; the other three processes are time independent and hence RP. The free part has reflected spatial-Fourier kernel exp[-|p|(t+s)]/(2|p|), also positive. For completeness, positivity of these reflected Gaussian covariance kernels extends to Gaussian exponential observables: their RP matrix is a positive diagonal rescaling of the entrywise exponential of a positive matrix, which is positive by the power series and tensor-power Gram matrices. Bounded cylinder observables follow by L² approximation. Coordinate permutation gives RP in each coordinate direction.

Under the UV rescaling φ_λ(x)=λφ(λx), the added covariance is λ²Σexp(-λ|x_μ-y_μ|), tending to zero, while the free covariance is unchanged. Yet the added covariance is not radial. At vectors (r,0,0,0) and (r/2,r/2,r/2,r/2), of the same Euclidean length r>0, the difference is

    3+e^{-r}-4e^{-r/2}=(u-1)(u-3)>0,  u=e^{-r/2}∈(0,1).

Thus the same leading rotationally invariant UV singularity, H_4, translations and coordinate RP leave a genuinely anisotropic long-distance covariance possible. This field has extra nonlocal degrees of freedom and is not an SU(N) Yang–Mills example. It identifies exactly the inference that the proposed UV argument must supplement.

**ARGUED — perturbation theory does not close the remaining inference.** A term proportional to exp(-1/g²) times an anisotropic covariance has zero formal power series at g=0, yet is nonzero at a fixed renormalized coupling. Even agreement to every perturbative order needs a nonperturbative remainder estimate. Declaring rotation-breaking operators irrelevant by power counting is not that estimate: their correlations are integrated over all positions and can be amplified by long-distance response or by phase selection.

**CONDITIONAL — one possible propagation theorem.** If every renormalized n-point distribution is represented by a real-analytic function on the connected domain of mutually distinct points, and exact rotation identities hold on a nonempty open subset of that domain, the analytic identity theorem propagates those identities throughout that domain. In four dimensions the configuration domain of finitely many labelled distinct points is connected. One must separately control distributions supported on coincidence sets, so anisotropic contact counterterms do not remain. This uses exact identities on an open set, not a short-distance asymptotic series. Analyticity must be established without assuming the Euclidean invariance one is trying to prove; invoking the desired OS reconstruction to obtain it would be circular.

**OPEN — usable UV-to-all-distance input.** For a chosen family of approximants, let D_n^{rot} be the renormalized rotational-variation insertion, including regulator, observable and measure terms. One needs a bound of the form

    |ω_n(δ_J F)|
      ≤ |⟨F;D_n^{rot}⟩| + observable-discretization error
      ≤ ε_n(F),             ε_n(F)→0,

for every local F in a determining algebra and its rotated versions. A small coefficient of D_n^{rot} is insufficient without control of the connected insertion. This concerns selected correlations on one sequence, and does not identify all thermodynamic states. §7 gives a more structured candidate estimate instead of treating this formula as an explanation of itself.

## 7. Route (e): a constructive selection theorem and the estimate to pursue

### 7.1 A single-sequence theorem

**PROVEN — conditional selection lemma.** Assume the following data and bounds, labelled S0–S4. The conclusion below is an implication from them, not a proof that Yang–Mills satisfies them.

- **S0 (named input):** one common local continuum algebra A with a continuous E(4) action, a countable determining family of local observables and products, and tight lattice approximants μ_(a,R) on reflection-symmetric hypercubic tori of side comparable to R. All limiting moments used below exist. Uniform source/moment bounds provide the required OS0 regularity, uniform integrability, and continuity in test functions and Euclidean motions.
- **S1 (named input):** gauge invariance, time RP, and H_4 invariance of these approximants transfer to A. Positive-half observables have approximants supported on positive-half links, or the vanishing-error bridge of §4. This includes the correct tensor action, if the observables have indices.
- **S2 (named input):** for each local test F, translations τ_z can be approximated by exact lattice translations τ_(z_a), z_a→z, with

      |μ_(a,R)((α_(τ_z)F)_a)-μ_(a,R)((α_(τ_(z_a))F)_a)|→0

  on the chosen family. Exact lattice-translation invariance then controls the remaining difference. A sufficient form is a uniform test-function/moment modulus C_F|z-z_a|^γ. Joint distributions, not merely individually shifted marginal means, must be covered.
- **S3 (named input):** let r_θ be the rotation in the spatial (1,2) plane. For every test F and every angle in a countable dense set,

      |μ_(a,R)((α_(r_θ)F)_a)-μ_(a,R)(F_a)|
        ≤ C_(F,θ)(R)(a/ℓ_F)^κ + b_(F,θ)(R),       (D)

  where κ>0, ℓ_F>0 is fixed, C_(F,θ)(R)<∞ at every admissible R, and b_(F,θ)(R)→0 as R→∞. Uniform continuity extends the resulting identities to all angles. The finite constants need not be uniform in volume. Estimates must hold for all sufficiently small admissible a at fixed R and along a common cofinal set of R for all tests. A common bare-coupling trajectory fixing the intended physical scale is part of S0, not a separately retuned theory for each test.
- **S4 (named input for “not free”):** there is a fixed continuous functional N of finitely many identified local moments, with N=0 for every free comparator permitted by the target and |N(μ_(a,R))|≥c>0 along the selected family. More general separating families are possible, but a block non-flatness bound is not a substitute. The physical identification and the free comparator class are part of this input.

**Proof (PROVEN).** Enumerate the required pairs (F,θ), translation tests, RP products and moments. Choose R_n increasing so that the first n supports fit and all first n boundary errors b_(F,θ)(R_n) are less than 1/(2n). Choose an allowed a_n→0 small enough that the corresponding finitely many cutoff errors in (D), translation-approximation errors and support-approximation errors are less than 1/(2n). This is possible despite growth of C(R_n), since there are only finitely many constraints at step n. S0 gives a convergent subsequence with all the relevant moments. For each fixed test the defects tend to zero. Consequently the limit is translation invariant by S2, invariant under r_θ by S3 and continuity, and H_4-invariant by S1. The group lemma gives O(4), hence E(4). RP passes through each finite reflected-product inequality by S1 and moment convergence, and gauge invariance passes through the gauge-invariant algebra. OS3 is inherited symmetry of commuting Euclidean observable products; S0 supplies OS0. Finally |N|≥c passes by continuity, excluding the specified free class. At no point are two different subsequential limits compared, and no spectral-gap or cluster estimate is used. ∎

**PROVEN — the strength distinction.** Even if (D) holds for every limit point, it asserts symmetry of each point, not equality between them. A set containing two distinct E(4)-invariant RP states already demonstrates the logical distinction: the constant-field laws δ_(φ≡0) and δ_(φ≡1), and all their mixtures, have those symmetries and RP while remaining different states. Adding a common independent massless Gaussian field supplies nonzero-energy excitations with energies arbitrarily close to zero without removing the distinction. This is a diagnostic in a larger class, not a claim of phase multiplicity for pure Yang–Mills. For a fixed common continuum specification, orientation control of a selected phase has strictly fewer boundary/subsequence quantifiers than uniqueness. Conversely, uniqueness for each of two discretizations does not by itself identify their continuum specifications; universality needs that bridge even in a unique-phase setting.

**ARGUED — what this does and does not buy.** Lemma S0–S4 is a concrete route to the full stated target without uniqueness, if its inputs are proved. Its symmetry part alone is not near completion merely because it has been named. With all qualitative estimates suppressed, “defects tend to zero on the chosen subsequence” is essentially the symmetry conclusion written before the limit. The scientific advance would be deriving (D), particularly b(R)→0, from local RG and a restricted response estimate. Infinite-volume uniqueness is not needed for the diagonal choice, and C(R) need not remain bounded.

### 7.2 A rotational Ward estimate with a specific infrared price

**ARGUED — proposed mechanism, not yet a lattice derivation.** Let J generate the spatial (1,2) rotation. Choose a smooth cutoff χ_R equal to 1 on a ball containing all supports of F and zero outside a ball of radius 2R. The compactly supported vector field v_R(x)=χ_R(x)Jx rotates F but changes variables only in a bounded region. If a renormalized symmetric stress tensor T_(μν), its Ward identity, and all observable/contact/Jacobian terms have been constructed, the rotational variation has the schematic but precisely testable decomposition

    |ω(δ_JF)| ≤ UV/renormalization residual
      + |∫_(R<|x|<2R) (∂_μχ_R)(Jx)_ν ⟨F;T_(μν)(x)⟩ dx|.       (W)

The interior contraction χ_R J_(νμ)T_(μν) vanishes by symmetry of T and antisymmetry of J. The remaining term is a boundary torque, not an arbitrary boundary perturbation. This cancellation identifies why the insertion estimate can be narrower than complete boundary-condition independence.

**OPEN — an explicit sufficient estimate package.** Derive (W) from finite-lattice changes of variables with correctly renormalized insertions and a remainder bounded by C_F(R)(a/ℓ_F)^κ. Then prove, along the selected cofinal family and uniformly over the relevant rotated tests,

    |∫_(R<|x|<2R) (∂_μχ_R)(Jx)_ν
              ⟨F;T_(μν)(x)⟩_(a,R_box) dx| ≤ b_F(R)+o_a(1),
    b_F(R)→0,                   R_box>4R.                      (TORQUE)

Here R_box is the actual box size; cutoff radius R and box size are separate. The estimate can be imposed first at fixed R with a→0 and R_box→∞, and then R→∞, with a common diagonal; or directly along a chosen joint sequence. It must hold for the actual selected full measure, not just a small-field conditional integrand. Integrating the angular derivative of ω(α_(r_θ)F) then gives (D), with the error integrated over a bounded angle interval. This derivative step also requires its stated test-function regularity.

**PROVEN — a sufficient massless bound.** One sufficient version of TORQUE is

    |⟨F;T_(μν)(x)⟩| ≤ A_F (1+|x|/ℓ_F)^(-4-η),  η>0,

in the relevant shells, with constants independent of cutoff and outer box on the selected family. Since |∂χ_R|≤C/R, |Jx|≤C'R, and the shell has volume at most C''R⁴, the absolute value in (W) is O(R^{-η}). This is a power-law bound and imposes no positive spectral gap. Angular cancellation could establish TORQUE without this stronger pointwise bound. The requirement concerns connected insertions of the stress tensor against local F; it is not decay of every connected pair nor comparison of arbitrary boundary conditions. It leaves open coexistence of symmetric phases differing in other observables.

**ARGUED — logical and practical strength.** TORQUE is narrower than full uniqueness and can in principle hold in each of several symmetric phases. It is nevertheless infrared information: calling it “UV locality” would be wrong. A bound valid only for distances below a fixed weak-coupling scale does not permit R→∞. This is the exact hole in the proposed route. Source-renormalized Ward identities are another input; symmetry of the classical continuum action alone does not supply them for the lattice probability measure.

**PROVEN — a restricted ultraviolet algebraic advantage.** In the class of local gauge-invariant polynomial action densities built from F and covariant derivatives, with canonical dimensions [F]=2 and [D]=1, the only parity-even, H_4-invariant quadratic curvature term of dimension four is a multiple of Σ_(μ<ν) tr(F_(μν)F_(μν)). Independent coordinate sign flips force the two antisymmetric index pairs in a quadratic curvature term to coincide; permutations force equal coefficients. A single traced F or its covariant derivatives vanishes for su(N), and the parity-odd epsilon contraction is excluded by coordinate reflections. Up to constants and total derivatives, this gives the rotationally invariant dimension-four term in this restricted class. It is an algebraic classification, not a bound on the full quantum effective action or its state.

**ARGUED — concrete layer-1 extension worth testing.** This classification suggests that the rotational defect should live in irrelevant marked interactions after all marginal source counterterms are fixed. To use it, strengthen the RG output to control a rotational or metric-variation insertion and its observable response, with an actual vanishing cutoff factor as in (D), plus local large-field errors. BFT-4's bounded polymer norm alone does not give that vanishing factor. BFT-3 supplies potentially useful ingredients for the local insertion calculation, but not TORQUE. Choosing R_box comparable to 8R in the latter estimate would fit the diagonal lemma without exchanging uncontrolled limits.

**CONDITIONAL — verified literature template only.** Del Debbio–Patella–Rago study translations along the Yang–Mills gradient flow and the associated lattice Ward identities for energy-momentum-tensor renormalization ([arXiv:1306.1173](https://arxiv.org/abs/1306.1173)). This motivates the insertion/renormalization side of (W). It does not, on the scope of its checked abstract, supply the constructive four-dimensional continuum measure, TORQUE, or the local RP bridge. No theorem number from that paper is asserted here.

### 7.3 Boundary geometry and regulator alternatives

**ARGUED — invariant finite-volume construction.** An exactly O(4)-covariant continuum construction in balls with an RP-compatible boundary prescription would retain rotations in a ball-exhaustion limit without uniqueness. But lattice balls do not have exact continuum rotations; that construction still needs a finite-volume regulator-independence argument. Moreover, an origin-centred exhaustion does not by itself prove translations or RP at displaced planes. Averaging translations of a merely origin-RP state repeats the different-plane problem. This is a distinct possible mechanism for reducing the rotational boundary term, not a completed escape.

**OPEN — a new isotropic regulator.** A gauge-invariant continuum regulator with exact E(4) symmetry and a common-reflection positive kernel would bypass rotational restoration. It must be constructed, controlled, and compared with the prescribed lattice sequence. Averaging actions instead of measures changes the approximation scheme and does not establish positive-kernel factorization. A smooth four-dimensional flow cutoff fails the elementary RP test in §4. No such regulator is supplied by BFT as stated.

## 8. Non-freeness and the route comparison

**PROVEN — non-Gaussianity of a mixture can be spurious.** An equal mixture of centered Gaussian variables of variances 1 and 2 has second moment 3/2 and fourth moment 15/2, hence fourth cumulant 15/2−3(3/2)²=3/4. This positive cumulant comes entirely from mixing free variances. Moreover, a composite observable of an individual free Gaussian field can already have nonzero connected higher moments. Thus “a connected four-point function is nonzero” needs the identified fundamental/composite observable and its free comparator before it excludes a free gauge theory. Rotation averaging supplies neither that identification nor an interacting dynamics.

**CONDITIONAL — robust preservation criteria.** On the original sequence, the continuous finite-moment separation S4 passes to the limit without changing the state. Under averaging, a nonlinear cumulant does not commute with the averaging operation. A sufficient replacement is an affine moment witness W, vanishing for every allowed free comparator, with a common signed bound (g·μ_n)(W)≥c>0 for every averaged g; then ν_n(W)≥c. Alternatively prove directly that the averaged state stays a positive distance from the entire free comparator class. Neither criterion is established for the lane by this panel. RP and symmetry closure cannot manufacture it.

**CONDITIONAL — table conventions.** “Preserved” below assumes the common algebra, convergence and support conditions stated above. Every route still needs the source bounds for OS0 and the specified non-free witness; the table does not certify any Yang–Mills input.

| Route | E(4) invariance | RP | Gauge invariance | Not free | Exact additional price; relation to uniqueness |
|---|---|---|---|---|---|
| (a) Spatial average | PROVEN: only spatial rotations; full group needs axis exchange and translations | PROVEN: time RP preserved | PROVEN: preserved by intertwining action | OPEN: mixing can change witnesses | OPEN: exchange identity on the averaged state, or spatial defect on the unaveraged H_4 state; fewer state-selection quantifiers |
| (b) Flowed observables | OPEN: needs FLOW-LAW, not just equivariance | CONDITIONAL: LOCAL-BRIDGE with error tending to zero; fixed-time flow is insufficient | CONDITIONAL: gauge-covariant flow and gauge-invariant outputs | CONDITIONAL: identified witness and common-state transfer | OPEN: joint convergence, rotational defect, local t↓0 bridge, source bounds; no uniqueness required |
| (c) Convex invariant set | PROVEN: Haar barycentre if the set has the stated properties and translations | CONDITIONAL: common-plane cone stable under the action, or vanishing averaged RP defect | PROVEN: convex/rotational preservation | CONDITIONAL: uniform affine separator or a direct averaged-state bound | OPEN: nonempty admissible invariant RP set; does not require a singleton, but construction is unresolved |
| (d) UV universality | PROVEN: leading UV asymptotics alone are insufficient | CONDITIONAL: retained if one keeps the same RP sequence | CONDITIONAL: retained in gauge-invariant insertions | OPEN: UV non-flatness is insufficient | OPEN: all-distance response/Ward bound, or exact short-distance identities plus independent analytic continuation and contact control; no uniqueness implication |
| (e) Selected-sequence defect/Ward route | PROVEN implication: S0–S3 give E(4) | PROVEN implication: inherited on the same subsequence | PROVEN implication: inherited | CONDITIONAL: S4 | OPEN: (D), with (W)+TORQUE a proposed mechanism; polynomial stress-channel decay can suffice, no gap or uniqueness |
| Ball exhaustion / isotropic regulator | CONDITIONAL: exact finite-volume covariance or exact regulator symmetry | OPEN: compatible boundaries/all needed planes or a common positive kernel | OPEN: must be built into the construction | OPEN: needs the same physical witness | OPEN: translations, regulator comparison and lattice provenance; no necessity of uniqueness established |

## 9. Adversarial self-check and negative-claim scope

**ARGUED — N1, actual route families.** The six rows above have different primary objects or mechanisms: group averaging, flowed observables, convex state sets, propagation of UV information, marked Ward insertions, and geometry/regulator construction. The first five were tested analytically here; geometry/regulator variants were scoped but not constructed. No route to Yang–Mills is declared impossible. Tested counterexamples defeat only the particular implication they instantiate. This is a single-panellist analysis, not a second independent review or a retained audit verdict.

**OPEN — N2, dependency audit.** The terminal inputs are A (common local algebra/source bounds), B (symmetry defect), C (positive-half/RP bridge), and D (a physical non-free separator). They are listed as a sufficient package, not as four proved-independent walls. The pairwise audit is:

| Pair | Implication established here | Remaining relation |
|---|---|---|
| A, B | PROVEN: regular Gaussian examples can lack rotations (§6) | OPEN: no general reverse implication is claimed |
| A, C | PROVEN: smooth flowed Gaussian examples can fail RP (§4) | OPEN: no general reverse implication is claimed |
| A, D | OPEN: none established | OPEN: source regularity alone does not supply the specified separator |
| B, C | PROVEN: invariant averaged example fails RP (§2); H_4/RP example lacks rotations (§6) | PROVEN: neither symmetry nor RP alone supplies the other in these broader classes |
| B, D | PROVEN: an invariant free field has no non-free separator | OPEN: no general reverse implication is claimed |
| C, D | PROVEN: a free field is RP | OPEN: no general reverse implication is claimed |

**PROVEN — N3, hidden-input check.** All uses of continuum pullbacks, source regularity, countable determining tests, tightness, support preservation, exact H_4 symmetry, the stress tensor, lattice Ward identities, contact terms and the free comparator are explicitly conditional or open above. In particular, the exp(-m_0 tree) in BFT is not substituted for a full-measure infrared estimate. The optional perfect-action convergence in BFT-4 would still need a quantum-state and observable comparison.

**PROVEN — N4, residual matching.** R9.1 concerns positivity after rotating measures; §§2 and 5 address that residual. X-ROT's “probably H-uniq” concerns comparison of states; §7 replaces comparison of all states by a selected-sequence estimate. BFT concerns background minimization/locality; it is used only to identify potential input to a marked insertion estimate. None of those statements is cited as a proof of a mass gap, uniqueness, OS1, or a no-go theorem.

**ARGUED — N5, resolution of negative statements.** The exact tests concern a rotationally averaged stationary scalar field, a heat-smoothed free covariance, a two-spin decomposition, and an H_4-invariant Gaussian UV diagnostic. The corresponding failures occur at the state/observable level explicitly displayed. No finite test of a block, Hessian, or mode is extrapolated into a no-go result for continuum SU(N). All arithmetic is symbolic; no floating-point experiment was run.

**ARGUED — N6, partial closures.** The group lemma removes five independent-looking plane-rotation tasks. The diagonal lemma removes uniqueness and volume-uniform cutoff constants from the sufficient symmetry package. The flow bridge remains useful for defining observables, and a convex argument becomes valid with the correct common-reflection hypothesis. These are mathematical reductions, not new physical axioms.

**ARGUED — N7, strongest challenge to my recommendation.** TORQUE may be harder than necessary. A direct positive-kernel representation for orientation-averaged reflected products, or an exactly covariant finite-volume construction with controlled translations, could select a symmetric RP state even when my pointwise stress-decay bound fails. The averaged-defect criterion in §5 explicitly allows this. Neither failed naive averaging nor failure of a particular stress estimate would exclude those alternatives. Conversely, without a marked insertion estimate, my own preferred route risks merely renaming OS1.

**ARGUED — N8, prior-route comparison.** The inspected PROOF and EXISTENCE passages already contain the two-family and universality ideas; I claim no novelty for them. The proposed correction is the quantifier change, the H_4-plus-one-plane reduction, and the explicit torque/diagonal estimate separating restoration of symmetry from equality of all infinite-volume states. The independent analysis has not used PLAN_S26 or other panel opinions. This scoped self-check claims no formal packet PASS or retained-grade status.

## 10. Independent ranked conclusion, before reading the lead's plan

1. **CONDITIONAL — first choice:** retain one gauge-invariant, H_4-invariant, time-RP sequence; prove a rotational defect for one spatial plane and a continuum translation modulus; take a diagonal limit. Lemma S0–S4 proves the desired implication without uniqueness or a gap. Pursue a renormalized marked Ward insertion and TORQUE; their validity for this Yang–Mills scheme is **OPEN**.
2. **CONDITIONAL — second choice:** use the two-family construction to obtain a common continuum local algebra and positive-half bridge. It helps the first route, but FLOW-LAW remains **OPEN**; flow covariance alone does not give OS1.
3. **CONDITIONAL — third choice:** repair rotational averaging through an admissible invariant common-RP set or a vanishing angularly averaged RP defect. The abstract averaging theorem is **PROVEN**; the required set/estimate for Yang–Mills is **OPEN**.

**ARGUED — answer at the independent checkpoint.** Uniqueness and a mass gap are not logically required by the proposed OS1 selection route. The lane has not supplied the needed symmetry-defect and local-field estimates, so the full theorem is not proved here. The least certain step is whether the soft-block RG can deliver a renormalized rotational insertion and vanishing boundary torque without an uncontrolled appeal to long-distance universality.

**PROVEN — process checkpoint, 2026-10-28 22:44:45 UTC.** Sections 1–10 above were written before the first read of PLAN_S26.md. The comparison below is subsequent and does not supply premises for the independent argument.

## 11. Subsequent comparison with PLAN_S26 §§1–2 and §7

**PROVEN — read order.** I first located PLAN_S26's section headings after writing the preceding checkpoint, then read only the requested §1–§2 and §7 ranges. The comparison and arithmetic check in this section were added afterward; the primary counterexamples and selection argument were already written.

**ARGUED — agreement with §1's diagnosis and §7's correction.** Completing background-field/propagator work does not itself establish Euclidean invariance of an infinite-volume state. OS1, the common local observable algebra, OS0, and physical non-freeness need explicit deliverables. The owner's full R^4 target must remain the target; finite volume is a useful milestone. The correction in §7 appropriately treats the previous out-of-reach judgment as a claim requiring evidence, not as a theorem.

**ARGUED — disagreement with the old §1 recommendation.** The record does not justify calling the finite-torus target finishable while parking R^4 by default. This panel supplies a specific no-uniqueness route, with the exact open estimates exposed, so OS1 has work that can be assigned now. A rotationally covariant family is not enough by itself (§4); full averaging is not forbidden in every case (§2); and no theorem equating orientation independence with infinite-volume uniqueness was supplied (§7.1). The revised §7 should not retain “IR control comparable to a mass gap” as an established equivalence. A stress-channel power law would suffice for the proposed mechanism; whether Yang–Mills satisfies it remains open.

**ARGUED — qualification to §7's “every route” sentence.** Within the chosen RG programme, ultraviolet control and finite-volume estimates are essential infrastructure. It does not follow that one must first prove a separate full T_fin theorem, let alone uniqueness/convergence of the entire cutoff sequence on every torus. The diagonal construction in §7.1 can take a joint cutoff/volume limit using selected finite-volume estimates. Thus “T_fin is milestone 1” is a sensible project arrangement, not a logical prerequisite proved for every possible route to T_OS. This distinction should keep a useful milestone from becoming a hidden extra theorem.

**ARGUED — agreement with the transfer caution in §2.** Changes to the blocking kernel require verification of the hypotheses of any imported background-field and propagator estimate. A diagrammatic resemblance to Balaban's construction does not establish those hypotheses. Reading the actual source theorem before pricing a replacement is sound. The particular claims in §2a–§2b about which published estimates solve which soft-scheme walls were not independently checked by this panel and remain **OPEN** here. I do not adopt their asserted equivalence from the lead's summary.

**ARGUED — qualification to §2's constants discussion.** An acyclic smallness hierarchy is preferable to arbitrary decimal margins. But the type of uniformity matters. The rotational cutoff constant C_F(R) in (D) may grow with volume and still permit a joint diagonal limit; uniform source bounds on fixed physical supports and a surviving non-free witness are different requirements and cannot be discarded. Conversely, making the coupling smaller as the box grows cannot silently change the physical renormalization condition. A common physical scale must remain fixed. Sending the effective coupling to zero at that fixed scale to keep all boxes perturbative risks selecting the free limit, not removing the infrared obligation.

**OPEN — soft-variable continuity deserves a separate gate.** EXISTENCE, X-CONT, specifically distinguishes the joint two-grid estimate from a vacuous equality of shifted marginal means, and records a nonvanishing independent-kernel-noise floor for literal L² comparisons of different soft branches. I have not independently certified that branch calculation. The selection theorem therefore does not assume it away: S0–S2 require a verified common physical observable family and its joint translation modulus, possibly through an appropriate conditional projection/OS-seminorm bridge. Artificial soft noise cannot be used as evidence of physical non-freeness.

**ARGUED — concrete change I recommend to the work plan.** Add an OS1 work item with this deliverable: a renormalized rotational Ward identity for one spatial plane on the physical local algebra, a bound on its irrelevant marked insertion with an actual vanishing cutoff factor, and a separately stated TORQUE estimate or an alternative boundary prescription that removes that term. Require the worker to state which constants may depend on the physical box and which must be uniform along the selected family. Retain the flow/common-algebra bridge as supporting work, and keep S4 as its own physical non-free test. Do not make this assignment “prove uniqueness,” “prove a gap,” or “prove covariance of the flow.”

**PROVEN — exact arithmetic verification, 2026-10-28 22:46:31 UTC.** Plain Python using only `fractions.Fraction` checked the displayed coefficients and a coordinate-conjugation instance, with no files written by the check:

    Taylor second-derivative multiplier: 1
    Sphere-averaged RP coefficient: -1/4
    Gaussian-mixture fourth cumulant: 3/4
    independent RP form: 0
    aligned RP form: 1
    anti-aligned RP form: -1
    Spatial-plane to time-space-plane conjugation: True

**PROVEN — meaning of that check.** The last line used a (1,2) rotation with entries 3/5 and 4/5 and conjugated it by the exchange of coordinates 0 and 1, yielding the corresponding (0,2) rotation. This finite check confirms the arithmetic instance; the all-angle/all-plane proof is the group argument in §3. The counterexamples rely on the written analytic proofs, not on numerical extrapolation. No check of the full Yang–Mills construction was run or claimed.

**PROVEN — final precision correction.** During the post-plan self-check I made the real/imaginary parts of the closed RP conditions explicit in §2. This changes no estimate or conclusion and imports no premise from the lead's plan.

**CONDITIONAL — final ranked answer.**

1. **First:** the unaveraged selected-sequence route, S0–S4. It gives E(4), RP, gauge invariance and non-freeness without uniqueness or a gap if its named bounds hold. The group and diagonal implications are **PROVEN** here; their Yang–Mills inputs are **OPEN**.
2. **Second:** flow plus a verified common local algebra, vanishing support error and a law-level symmetry estimate. It is useful infrastructure; covariance of the flow alone is insufficient.
3. **Third:** rotational averaging repaired by common-reflection positivity or a vanishing averaged RP defect, with admissible lattice provenance and a surviving free-theory separator. Fixed-point terminology alone establishes none of those inputs.

**OPEN — least certain.** Whether the soft Balaban-type RG can produce the renormalized rotational insertion and vanishing boundary torque for a chosen full-measure sequence, while retaining a common physical local algebra and non-free witness. The panel has removed uniqueness as a logical prerequisite; it has not proved the full four-dimensional Yang–Mills theorem.

