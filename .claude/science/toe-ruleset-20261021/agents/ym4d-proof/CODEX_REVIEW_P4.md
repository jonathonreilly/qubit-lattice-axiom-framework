## PRE-STATED

Recorded UTC: 2026-10-28T23:22:26Z. Independent hostile review of `PANEL_P4.md` for the requested four-dimensional Yang–Mills target: OS0–OS3 on R^4, non-free, with no mass-gap requirement. Only this review file may be written; no git operations.

Prior exposure: the user brief and an initial, truncated read exposed the panel introduction, its own pre-statement, lane-source inventory, and the start of its definitions. This pre-statement precedes my complete target read and substantive calculations; it is not claimed to precede all exposure to the target.

Refutation criteria, fixed before the detailed checks:

1. Equatorial RP: a negative OS quadratic form for an admissible proposed regulator, or a demonstrated failure of its asserted proof step, refutes the relevant assertion. An unspecified seam or missing positive-kernel decomposition warrants NOT-VERIFIED, not an impossibility claim about sphere regulators.
2. SO(5): distinguish an action on one cutoff probability space from transport between different embedded lattices. A comparison that silently changes renormalized couplings, seam defects, observable definitions, or state selection does not establish the stated universality implication.
3. UV classification: identify an uncontrolled coarse-scale response, normalization, low mode, or radius-dependent constant in the comparison. Fixed finite volume alone is not accepted as proof that a bound is ultraviolet in the panel's own sense.
4. Flat limit: check convergence of transported observables and transformations, uniformly controlled moments/distribution seminorms, and reflection planes. Compactness without these controls does not establish OS0, E(4) covariance, or non-freeness.
5. L1–L3: derive or disprove the exact mathematical statements with symbolic/rational arithmetic. A counterexample must satisfy the claimed hypotheses; a missing domain or regularity hypothesis is recorded explicitly.
6. Lane criticisms: inspect the actual cited text and dependencies. Confirm only what is supported by a file and a locating string.

Verdict vocabulary: CONFIRMED = independently established in its stated or explicitly narrowed domain; NOT-VERIFIED = missing construction, estimate, or hypothesis; REFUTED = explicit counterexample or invalid asserted implication, with the exact scope identified. Every substantive verdict will carry a source file and locating string. No numerical floating-point evidence will be used. Unverified literature recollections, if any, will be marked [m]. No claim of a particular runtime model identifier is inferred from the user's requested label.

## Source and review boundary

Read [PANEL_P4.md](PANEL_P4.md) in full, including §§8–9. The other panel files were not independently read; P4's accounts of their conclusions are not independent evidence here. Read the relevant original passages of [PROOF.md](PROOF.md) and [EXISTENCE.md](../ym4d-existence/EXISTENCE.md). The latter lives in the sibling `ym4d-existence` directory, not in this lane. The repository science workflow and the applicable mathematical-review/no-go portions of its review skill were read. This is the requested source review, not a branch review, landing operation, or formal claim-audit verdict.

Source identities checked at 2026-10-28T23:32:35Z:

| Source | SHA-256 |
|---|---|
| `PANEL_P4.md` | `57139e4e8ebc79d9aaa9b72545d81818a654b027d43e94a8bcbb406a02e69bf2` |
| `PROOF.md` | `9105139b2ffaad48967595768f077153848970ca295fbd0bfac678545cca8d5e` |
| `../ym4d-existence/EXISTENCE.md` | `14345292370a55e1dabbb0875e70b4a989bfdf096841255bed7eb75771a647f0` |

The mathematical target is existence of one suitably normalized, non-free OS0–OS3 limit. Uniqueness, clustering, and a positive mass gap are not assumed. The assertions below about Gaussian examples establish logical distinctions; they are not counterexamples to existence of SU(N) Yang–Mills theory.

## 1. Attack on reflection positivity across the equator

### 1.1 The matching-link proof survives

**CONFIRMED, on the stated gauge-invariant half-lattice algebra.** Source: `PANEL_P4.md`, locating strings `S1. RP for θ_eq at every cutoff: PROVEN` and `The crossing links form a matching`; comparison source: `PROOF.md`, `Proof re-derived (link reflection θ: t → 1 - t`.

Here is the finite-dimensional proof, including the gauge-fixing step that could have failed. Let the two interior graphs be reflected copies. Let (C_v) be the crossing link from (v_-) to (v_+). With the convention (U_{xy}\mapsto h_xU_{xy}h_y^{-1}), choose (h_{v_+}=C_v), (h_{v_-}=1), and identity at the other positive vertices. The matching property makes these prescriptions consistent. Every (C_v) becomes identity. For a boundary edge (e=(v,w)), its northern variable becomes

\[
 V'_e=C_vV_eC_w^{-1},\qquad
 U_eC_wV_e^{-1}C_v^{-1}=U_e(V'_e)^{-1}.
\]

For each fixed collection (C_v), all remaining link changes are left/right Haar translations. Thus their product measure is unchanged. Interior plaquette weights and gauge-invariant observables supported wholly inside either half are unchanged. The unused integrals over the (C_v)'s equal one for normalized Haar measure. This is an exact change of variables; there is no continuum gauge-fixing determinant or smooth-extension requirement.

After identifying the reflected graphs, the density consequently has the form

\[
 h(U)h(V)\prod_{e\in\partial\Lambda_-}K_{c_e}(U_e,V_e),
 \quad h\geq0,\quad
 K_c(A,B)=\exp\{c\,\operatorname{Re}\operatorname{tr}(AB^\dagger)\},
 \quad c_e=\beta_e/N\geq0.
\]

Each kernel is positive definite. An explicit expansion, with multi-indices over matrix entries, is

\[
 K_c(A,B)=\sum_{r,s\geq0}
 \frac{(c/2)^{|r|+|s|}}{r!s!}
 A^r\overline A^{\,s}\,
 \overline{B^r\overline B^{\,s}}.
\]

It converges absolutely on the compact group. Multiplying these expansions and integrating gives

\[
 Z\,\omega(\overline{F\circ\theta}\,F)
   =\sum_\alpha d_\alpha
      \left|\int F(U)h(U)\Psi_\alpha(U)\,dU\right|^2\geq0,
 \qquad d_\alpha\geq0.
\]

This covers bounded measurable gauge-invariant (F) supported in one half. The two interior actions must be mirror copies, including their coupling assignments. A spatially varying coupling does not otherwise affect this proof. Nor does stereographic distortion: the positivity argument uses the graph involution, Haar measure, and the crossing kernels, not flat Euclidean edge lengths.

The seam therefore does **not** invalidate the Osterwalder–Seiler-type factorization. No negative RP witness was found, and the displayed argument rules one out in this domain. The proof does not cover arbitrary gauge-fixed, non-gauge-invariant fields, nonlocal reconstruction maps, or additional crossing interactions without their own positive-kernel decomposition.

Geometric housekeeping remains: choose the digital ball inside the hemisphere, avoid duplicate fixed vertices or treat them by a site-reflection construction, and specify an actual boundary complex. These are requirements for the proposed geometric regulator, not failures of the finite-graph RP theorem.

### 1.2 RP does not establish a transparent seam

**REFUTED as a general implication from the stated admissible weights.** Source: `PANEL_P4.md`, locating strings `Weights β_p ≥ 0 on the crossing plaquettes` and `It is irrelevant by the same counting: no gauge-invariant local operator of dimension ≤ 3 exists`.

The allowed choice

\[
                 \beta_p=0\quad\text{for every crossing plaquette}
\]

gives, exactly at every cutoff, two independent hemisphere measures. For gauge-invariant half-observables (F_-,G_+),

\[
 \omega(F_-G_+)=\omega(F_-)\omega(G_+).
\]

This regulator is RP, but it imposes no dynamical matching across the interface. Its construction cannot be declared a transparent approximation to the sphere merely because the missing layer has thickness (O(a)). Any continuum limit retaining nonzero connected correlations within a hemisphere would distinguish this interface: connected correlations across it vanish identically. A rotation moving such a pair across the interface then exposes the defect. The exact factorization is the counterexample to the asserted automatic gluing, not a claim that an interacting continuum limit of these halves has been constructed.

There is also a precise reason that the bulk operator count misses the issue. Before transparency is established, the fields on the two sides are independent boundary connections. The crossing transporter (h) transforms as

\[
 h\mapsto u_-hu_+^{-1},\qquad
 D_i h=\partial_i h+A^-_ih-hA^+_i.
\]

The interface expression

\[
 \int_{S^3}\operatorname{tr}\big((D_i h)^\dagger D_i h\big)
\]

is gauge invariant and reflection even after exchanging the two sides and (h\leftrightarrow h^{-1}). Its engineering dimension is two on a three-dimensional interface. In the gauge (h=1), it measures (A^-_i-A^+_i). A smooth-side expansion of a crossing plaquette gives a positive quadratic term of order (eta_p a^2|A^-_i-A^+_i|^2); summing (O(a^{-3})) such plaquettes gives an interface stiffness of order (eta_p/a). Its limit depends on the chosen weights. This counting identifies a missing matching condition; it is not a nonperturbative derivation of that limit.

Counting only bulk operators evaluated on an already continuous connection assumes the very transparency that must be proved. Even excluding a Chern–Simons term would not exclude the reflection-even matching term above. P4 does not specify a scaling or geometric normalization of the crossing weights that resolves this.

**NOT-VERIFIED for a suitably tuned, ordinary-strength seam.** Same source and locating strings. This review does not exclude choosing positive crossing weights that produce the desired continuum gluing. It rejects the inference that nonnegativity plus the quoted bulk dimension count suffices.

## 2. Attack on the SO(5) action and the required comparison

### 2.1 Moving poles is legitimate transport between regulators

**CONFIRMED as a transport identity, not as a symmetry of a fixed cutoff lattice.** Source: `PANEL_P4.md`, locating string `Since E_{g𝒦}[O] = E_𝒦[g^{-1}·O] exactly`.

Let (\mathcal K) denote the complete decorated regulator: embedded graph, both chart poles and frames, seam, weights, and observable prescription. An isometry (g) produces (g\mathcal K), transporting **all** this data. Link labels identify the two finite product spaces, and transported weights give an exact pushforward of measures. In general (g\mathcal K\ne\mathcal K); there is no SO(5) automorphism action on the single finite graph.

To make the identity about a common continuum observable (O) meaningful, one needs discretization/reconstruction maps (I_{\mathcal K}) satisfying

\[
 I_{g\mathcal K}(O)\circ T_g
       =I_{\mathcal K}(g^{-1}\!\cdot O),
\]

where (T_g) transports link configurations. Then the expectation identity follows by change of variables. If instead one re-creates a lattice using the original fixed poles, re-tunes parameters independently, or uses a new noncovariant observable prescription, it does not follow by definition. P4's geometrically covariant algebra and the maps (I_{\mathcal K}) are obligations, not supplied constructions. Their half-space locality is also needed separately for RP transfer.

### 2.2 Difference-form universality really would suffice

**CONFIRMED as a conditional implication; NOT-VERIFIED as an estimate for this regulator.** Source: `PANEL_P4.md`, locating strings `S2. SO(5) invariance from universality in DIFFERENCE form` and `E7-type convergence is not needed`.

At each fixed (R), suppose the relevant Schwinger functions have subsequential limits on one common algebra, the transport identity holds, and

\[
 D_{a,R}(g,O):=
 \omega_{\mathcal K_{a,R}}(I_{\mathcal K_{a,R}}O)
 -\omega_{g\mathcal K_{a,R}}(I_{g\mathcal K_{a,R}}O)
       \longrightarrow0
\]

for a countable dense subgroup and a determining set of local observables **and their products**. Every limit then has equal expectations of (O) and (g^{-1}O). Continuity of the group action on the test-function algebra extends the equality to SO(5). Full cutoff-sequence convergence and uniqueness of the limit are unnecessary.

The needed statement is genuinely a fixed-volume comparison along the isometry orbit of the regulator. It is weaker than universality across all cellulations, and no (R)-uniform rate is needed if the continuum limit is taken first at each radius. Conversely, in a tight family with continuous observable evaluations, vanishing of these defects is essentially equivalent to SO(5) invariance of every subsequential fixed-(R) limit. Naming the comparison does not reduce its difficulty by itself.

It is stronger than the following incomplete substitutes: agreement of classical continuum actions; perturbative agreement away from the seam; a common beta function; convergence of each scheme to an unspecified limit; or agreement of conditional observables with uncontrolled coarse marginal weights. Rotating the seam into an observation region makes interface universality part of S2, not a disposable detail.

**CONFIRMED given this construction and limit statement.** Source: `PANEL_P4.md`, `S3. RP for every great sphere: PROVEN given S2`. Conjugating the equatorial reflection by SO(5) transports both the positive algebra and the RP inequality. The cutoff measure is also invariant under its equatorial reflection; if this invariance passes with the observable maps, SO(5) plus that reflection gives O(5). This supplies the improper rotations needed for the full Euclidean group later.

### 2.3 The coupling prescription is an asymptotic proposal

**NOT-VERIFIED beyond classical consistency and the proposed asymptotic matching.** Source: `PANEL_P4.md`, locating strings `Classical 4D YM is conformally invariant` and `f(g_0(x)) = aΛ_phys Ω(x)/C_W`.

The classical cancellation (\sqrt g\,g^{-1}g^{-1}=\Omega^4\Omega^{-4}) is correct. A cutoff of physical size (a\Omega(x)) also motivates the stated local scale matching. But a two-loop formula and a flat Wilson-action conversion factor are not a construction of a nonperturbatively matched curved-background measure, its seam, and its composite observables. The comparison must fix the same physical renormalization conditions, sector prescription, and local observable subtractions across rotated regulators and across radii.

Quantum conformal covariance cannot be substituted for isometry covariance. For example, the explicitly inspected one-loop Yang–Mills calculation in [Bautista–Benevides–Dabholkar, §3.2, equations (3.8)–(3.9)](https://arxiv.org/pdf/1711.00135) contains an anomalous Weyl-factor contribution together with the flat nonlocal effective action. This is evidence that the classical cancellation alone is insufficient, not a theorem against P4's matching proposal. Purely background-dependent normalization terms can cancel in normalized expectations; source-dependent terms and observable mixing still require control.

## 3. Attack on “this is ultraviolet”

### 3.1 The precise unsupported step

**NOT-VERIFIED. The claimed inference from compactness is invalid.** Source: `PANEL_P4.md`, locating string `Compactness of SU(N) bounds the coarse curvature` and the following assertion `O((a/ℓ_0)^θ) per block`.

Compactness bounds a plaquette's group distance from identity. It does not put every configuration into a weak-field chart, bound derivatives of conditional densities, control competing constrained minimizers, or compare two block maps. At fixed (\ell_0), curvature of order (\ell_0^{-2}) means order-one coarse plaquette holonomy, not the small plaquette assumed by a perturbative small-field estimate. Compactness also supplies no power-law rate in (a).

The finite-volume expectation after integrating fine variables has the schematic exact form

\[
 \omega_a(O)=
 \frac{\int_{\mathcal C_R}q_a(V)o_a(V)\,dV}
      {\int_{\mathcal C_R}q_a(V)\,dV}.
\]

Comparing (o_a)'s uniformly does not compare (q_a)'s. The elementary compact-space counterexample is (\mathcal C=\{0,1\}), identical conditional kernels and the same (o(V)=V), but coarse weights ((1,1)) and ((1,2)). The expectations are (1/2) and (2/3), a difference of (1/6). This refutes the inference from conditional-observable agreement to state agreement, not any particular Yang–Mills estimate.

That is the entry point for information from scales (\ell_0) through (R): the normalized coarse law, its large-field sectors, and its response to changes in the action or interface. A finite number of compact variables does not remove those scales. If (R\gg\ell_0), the finite sphere contains modes and correlations far below the weak-coupling scale even though it has no thermodynamic limit at that fixed radius.

### 3.2 A sufficient comparison that really avoids IR decay

**CONFIRMED as a sufficient conditional mechanism.** Source being tested: `PANEL_P4.md`, locating strings `The summed error is O((R/ℓ_0)^4 (a/ℓ_0)^θ)` and `It needs a common coarse space for two different grids`.

The strongest fair defense of P4 is the following. Construct a common coarse space and positive unnormalized weights (q_a,\widetilde q_a). After a field-independent normalization (c_a), prove

\[
 \sup_V\left|\log\frac{\widetilde q_a(V)}{q_a(V)}-c_a\right|
       \leq\delta_{a,R}\longrightarrow0,
 \qquad
 \sup_V|\widetilde o_a(V)-o_a(V)|\leq\varepsilon_{a,R}\longrightarrow0.
\]

For normalized laws (P_a,\widetilde P_a), this gives

\[
 e^{-2\delta_{a,R}}\leq
 \frac{d\widetilde P_a}{dP_a}\leq e^{2\delta_{a,R}},\qquad
 |\widetilde\omega_a(O)-\omega_a(O)|
 \leq\varepsilon_{a,R}
      +\|o_a\|_\infty(e^{2\delta_{a,R}}-1).
\]

Unbounded fields additionally require appropriate uniform integrability. If the logarithmic error is a sum of (O((R/\ell_0)^4)) uniformly bounded local errors of size (O((a/\ell_0)^\eta)), then at fixed (R) the argument works without clustering, uniqueness, or a mass gap. No low-energy susceptibility can defeat this **proved uniform bound**. This supports the possibility of P4's strategy.

But it is not a bound obtained merely by compactness. It requires matching the entire effective density, including large fields and the seam, on the common space. A weaker normalized-law comparison might suffice; the displayed supremum estimate is sufficient and potentially substantially harder than necessary.

The equivalent response formula exposes what happens without such control:

\[
 \frac{d}{ds}\omega_s(O)
   =\omega_s(\partial_sO)-\operatorname{Cov}_s(O,\partial_s S_s).
\]

If (\partial_sS_s=\sum_X r_X) is bounded in supremum norm, finite-volume counting works. If its control is only perturbative, averaged, or restricted to small fields, the covariance with the remaining coarse theory must be estimated. That is precisely where low-mode and large-distance information may enter. The bound `a^η·Vol(S^4_R)·sup|Cov|` in P4 §9.2 requires a cutoff-independent bound on the **renormalized** covariance; bare composite covariances need not have one.

**Verdict on classification: NOT-VERIFIED.** Source: `PANEL_P4.md`, `S2 ... OPEN, UV-type (ARGUED)`, `No IR statement enters T_OS`, and `The sphere route is the instance of THEIR selection lemma in which b ≡ 0`. The closed sphere removes a boundary-at-infinity torque term, which is a real advantage. It does not prove the remaining regulator defect vanishes. A uniform conditional UV comparison could avoid an additional IR decay theorem; P4 has not proved that comparison. Equally, this review has not proved that an IR uniqueness theorem is unavoidable. Fixed volume is not a synonym for ultraviolet, and absence of uniqueness is not absence of all volume control.

## 4. Attack on the contraction to R^4

### 4.1 Geometry and conditional transfer

**CONFIRMED with the uniformity and observable hypotheses below.** Source: `PANEL_P4.md`, locating string `S5. R → ∞: ARGUED, given volume-uniform local bounds`.

For (N=(0,0,0,0,R)), the normal-coordinate embedding is

\[
 \chi_R(x)=\left(R\frac{\sin(|x|/R)}{|x|}x,
                      R\cos(|x|/R)\right),\qquad |x|<\pi R,
\]

with its continuous value at zero. It is used only on fixed compact sets, eventually inside its injectivity domain. The stabilizer of (N) acts there exactly by SO(4). A great-sphere reflection whose ambient hyperplane contains (N) acts exactly by the corresponding tangent-space hyperplane reflection. Thus positive-half-space supports are mapped to the correct hemisphere without an approximation error.

For a fixed (v), rotate in the ambient plane spanned by (v) and (N), with angle (|v|/R), taking (N) to (\chi_R(v)). Then

\[
 \chi_R^{-1}g_R(v)\chi_R(x)\longrightarrow x+v
\]

in every fixed finite differentiability norm on compact sets. This follows directly by expanding the displayed sine and cosine expressions; no numerical contraction argument is needed. Density Jacobians and tensor-index transport must be included in the observable pullback, and converge in the same way.

Assume continuum sphere states (\omega_R) have already been constructed, with O(5) invariance, great-sphere RP on the chosen local algebra, and compatible field normalizations. For each compact (K\subset\mathbb R^4), a sufficient local condition is equicontinuity of every pulled-back Schwinger functional in a fixed test-function seminorm, together with moment control strong enough to pass products. For example, it suffices to have position-uniform unit-ball estimates

\[
 \sup_{R\geq R_0}\mathbb E_R|\Phi_R(f)|^n
       \leq A^n(n!)^b\,p(f)^n,
\]

with (A,b) and the finite derivative order in (p) independent of (R,n), in uniformly controlled local orthonormal charts. Species and tensor transformation laws must be fixed as part of the algebra.

A diagonal extraction on a countable dense collection of compactly supported tests then has these consequences:

1. The moment bounds extend convergence from that collection to all such tests and give continuity uniformly in (R).
2. Invariance under (g_R(v)) passes to translation invariance: the error is bounded by a common seminorm of the transported test minus its translate, which tends to zero.
3. Tangent rotations pass directly. The inherited reflection invariance supplies improper rotations.
4. Each polynomial RP expression is a finite sum of convergent moments. RP passes for planes through zero; translation invariance moves it to every affine hyperplane.
5. OS3 passes as symmetry of the moments.

Weak convergence alone is enough for bounded continuous half-algebra observables. For unbounded local fields the moment or uniform-integrability hypotheses above are indispensable; weak convergence alone does not preserve expectations of their products.

### 4.2 OS0 needs specified uniform bounds

**CONFIRMED as a conditional local-to-global estimate.** Source: `PANEL_P4.md`, locating string `2.1 OS0 on R^4 needs no decay of correlations`.

Once the limiting local fields exist with a common position-uniform bound, take a smooth unit-cube partition (f=\sum_Q f\chi_Q). For a sufficiently strong Schwartz seminorm (p_k\),

\[
 p(f\chi_Q)\leq C_k(1+|c_Q|)^{-k}p_k(f),\qquad k>4.
\]

Minkowski and Hölder give

\[
 |S_n(f_1,\ldots,f_n)|
 \leq (AC'_k)^n(n!)^b\prod_{j=1}^n p_k(f_j).
\]

This yields tempered Schwinger distributions and a uniform factorial moment hierarchy, without a decay-of-correlations assumption. The required seminorm order and factorial exponent must remain fixed as (n) and (R) vary; merely saying “OS0-type” does not specify those quantifiers. On general, non-factorized test functions one also has to use the associated continuous tensor-product bound; continuity on separate smeared fields is not a license to change the reconstruction theorem's growth hypothesis.

The argument assumes genuine linear smeared random fields with the stated absolute moments. A source functional for a renormalized composite with unresolved contact subtractions does not automatically supply those random variables or those bounds. The lane itself identifies this problem: `EXISTENCE.md`, `X-SRC-GAP`, explicitly says the naive exponential-moment form fails for its dimension-four lattice composites. Bounds at one positive flow time do not give constants uniform as that time goes to zero, and do not by themselves give exact local RP.

### 4.3 What compactness does not give

**NOT-VERIFIED for Yang–Mills; REFUTED if “pure compactness” drops the named hypotheses.** Source: `PANEL_P4.md`, locating strings `R → ∞ is then pure compactness`, `Non-triviality as §2.2, OS0 as §2.1`, and `given volume-uniform local bounds`.

An exact counterexample to the unconditional compactness assertion is the constant scalar field on (S^4_R) with values (+R,-R), each of probability (1/2), taking integer (R\to\infty). It is O(5)-invariant and RP for every great sphere: reflection fixes the random configuration, so the OS form is an ordinary squared norm. It is smooth and has every moment at each finite radius. Its local laws are not tight. Compactness of the underlying manifold and all its symmetries do not provide field compactness or OS0 bounds uniform in (R).

Likewise the constant field with values (+1/R,-1/R) is non-Gaussian at each finite (R), with fourth cumulant exactly (-2/R^4), but converges to the deterministic zero field. Non-freeness is not a closed property. P4 needs a fixed-scale, correctly normalized observable witness separated by a positive amount from its calibrated free Yang–Mills comparator, uniformly in both cutoff and radius. A nonzero formal running coupling is not such a witness. Nonzero cumulants of gauge-invariant composites alone are not sufficient either, because a free underlying gauge field can have non-Gaussian composites.

There is no need to solve uniqueness if those bounds and that witness are proved. But P4's volume-uniform input is a substantive theorem, even if one hopes to prove it with conditional UV methods. Fixed-(R) constants (A_R) do not suffice. The safe order is continuum extraction for each (R), followed by (R\to\infty). A single joint sequence instead needs explicit control of the cutoff errors along that sequence, including the (R)-dependent rotations used for translations.

