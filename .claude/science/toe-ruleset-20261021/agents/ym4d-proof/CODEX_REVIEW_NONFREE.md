# PRE-STATED — independent hostile review of NONFREE55

UTC: 2026-10-29 05:31:50. Written before deriving any finding.

Scope: NONFREE55.md, beginning with errata E1/E2 and §7; explicitly named supporting files and nf55_a/b/c checks, using bounded ranges located by strings. No git commands; only this deliverable is writable. Exact rational/symbolic Python calculations only. No snapshots or audit ledgers. The two additional local reads, if needed, are the governing science workflow and the applicable review procedure.

Targets and pre-stated falsifiers:

1. T_NF: an allowed free composite, relabelling, or mismatch between labelled-field exclusion and equivalence of OS theories refutes an asserted absolute/free-class distinction.
2. NG1/NG2/NG3: seek an overbroad quantifier, missing positivity/spectral/locality hypothesis, topology mismatch, or generalized-free construction not satisfying its stated bounds. Distinguish exact representation from approximation.
3. FS/SEP-e: seek cancellations, derivative/tensor/mass effects, mixtures, or a free local observable with the prescribed logarithmic damping. Test the pairing used to obtain strict positivity.
4. H-RED^e: reconstruct limit passages and scale/volume/tuning quantifiers. Missing uniform estimates, noncommuting limits, or undeclared normalization refute the reduction as stated.
5. nf55_a/b/c: independently reconstruct Maxwell constants/contractions, coupling factors and Bessel coefficients; ask whether each gate could fail.
6. Trace anomaly, LSZ, literature: distinguish rejection of a proposed witness from impossibility of such a witness, and compare with primary open sources.

Review verdicts: CONFIRMED / NOT-VERIFIED / REFUTED. Claim statuses: PROVEN / ARGUED / CONDITIONAL / GAP / OPEN. No numerical value or source assertion receives CONFIRMED without reconstruction or direct verification. Findings attach to current file:line plus a locating string and will be appended incrementally. The final section will state exactly what may be banked.

## Finding R1 — large-field scale sum: the boundary threshold is wrong

**Verdict: REFUTED. Claim status: GAP in §6.3; this does not by itself refute H-RED^e.**

Attachment: `NONFREE55.md:403-405`, locating strings `Summed over the levels` and `or c > 2 at 2p = 1`; coupling pin `FLOW.md:24-25`, `u_k := 1/g_k²`.

Write U for the inverse coupling at separation λ. At the boundary p = 1/2, the displayed probability is exactly exp[-c log(1/g_j)] = g_j^c = u_j^{-c/2} in FLOW's lane convention. With u_j increasing linearly into the ultraviolet, the required uniform sum has the same tail order as Σ_{n≥0}(U+b n)^{-c/2}. For c > 2, integration between adjacent terms gives this tail asymptotic to U^{1-c/2}/[b(c/2-1)]. Consequently it is o(U^{-2}) **iff c > 6**, not c > 2. At c = 6 it has order U^{-2}, with no little-o margin; at c = 4 it has order U^{-1}. If c is instead redefined in exp[-c log u], the threshold is c > 3. Those two c's must not be conflated. Using standard coupling g_std only introduces a constant factor (2N)^{c/2}, leaving c > 6 unchanged.

For 2p > 1 the superpolynomial tail claim is sound. The stated LF-dec hypothesis uses this strict case, so its proposed conditional route is not defeated by the boundary correction. The large-field decoupling estimate itself remains OPEN.

## Finding R2 — the connected witness is not affine, and adding free Maxwell spoils its upper bound

**Verdict: REFUTED as stated; the componentwise limitation survives after repair.**

Attachment: `NONFREE55.md:138-142`, `The witness of §3 is affine in the state` and `½ω_YM + ½ω_free obeys every bound`; `NONFREE55.md:278`, `Mixture case, S_2^e = ∫S_2^αdν`.

For a mixture of translation-invariant components with mean μ_α, the connected kernel is

S_2^{ω,T}(x-y) = ∫S_2^{α,T}(x-y)dν(α) + Var_ν(μ_α).

Thus the connected witness is affine only when the component means agree (in particular, when all are separately centred). The finite variance term is nonnegative and independent of separation. For common zero means, mixing any positive weight of free Maxwell :F²: into a field obeying AF-e gives liminf λ⁸S_2^{ω,T}(f_λ⊗g_λ) ≥ weight × 48(N²−1)I_8/π⁴ > 0. It fails AF-e's upper half. It is false that an unrestricted free admixture preserves every bound.

Repair: choose a centred free scalar, whose kernel is O(λ^{-2}), or another free composite of leading exponent below 8. Then its contribution is negligible relative to the AF-e lower bound, so AF-e does not exclude every free phase in a mixture. For SEP-e itself, assuming the mixture defines finite separated moments, replace the asserted affine identity by the displayed variance formula: Fatou applies to the nonnegative connected component kernels, and the extra finite constant tends to zero after multiplication by λ^{7.5}. The separation conclusion survives this repair.

## Finding R3 — masses need not be subleading for derivative composites

**Verdict: REFUTED for the mass sentence; the nonnegative-log structural conclusion is not refuted.**

Attachment: `NONFREE55.md:243-244`, `Masses enter only subleading orders`; `NONFREE55.md:265-267`, `masses only multiply higher powers of r`.

Take a massive canonical scalar φ_m and the allowed scalar derivative field χ = □φ_m. The free equation of motion gives χ = −m²φ_m in Minkowski signature, hence at separated Euclidean points S_2^{χ,T}(r) = m⁴G_m(r) = m⁴/(4π²r²) + O(log r). The mass occurs in the leading coefficient, and the massless highest-derivative term cancels. This field is not null for m > 0. Proca propagators already have leading derivative coefficients proportional to m^{-2} in the file's own definition.

Correct statement: after all cancellations for fixed masses, the first nonzero term has integer power and nonnegative log degree; masses can determine its coefficient and which power survives. This weaker statement is all SEP-e needs.

## Finding R4 — NG1/NG2 omit the zero-momentum sector allowed by OS0–OS3

**Verdict: REFUTED for the OS0–OS3 ⇒ displayed-KL import and unconditional NG1; NOT-VERIFIED for NG2's literal constructions as universal constructions; CONFIRMED conditional on the narrower displayed KL representation. Claim status: GAP in the universal application.**

Attachment: `NONFREE55.md:163-166`, `Common import` / `OS0–OS3`; `:168-180`, `every scalar OS theory`; `:194-210`, `For the separated two-point function S_2 of any scalar OS theory`.

Counterexample, re-derived without a spectral citation: let X be a centred real Gaussian variable with variance 1 and set e(x) = X for every spacetime point. Its Schwinger functions are constant Gaussian moments, tempered and Euclidean invariant. Reflection positivity is E[|P(X)|²] ≥ 0 for every positive-time polynomial; symmetry is immediate. Reconstruction is multiplication by X on L² of its Gaussian law, vacuum 1, and translations U = 1. This satisfies the stated OS0–OS3 setting and its factorial growth bound; it fails clustering, which the target deliberately does not impose. Its connected kernel is S_2^T(x-y) = 1.

Choose nonnegative separated f,g of integral 1, put F_1=f⊗g, and F_2(x,y)=2^{-8}F_1(x/2,y/2). For every positive mass-shell KL kernel, G_s(2z)=¼G_{4s}(z) ≤ ¼G_s(z), since G_s(z) decreases with s. Thus x_2 ≤ x_1/4 for the two values of every finite free-scalar sum. The continuous witness

W(x_1,x_2) = max(0, x_2 − x_1/4)

vanishes on the whole linear canonical-free class in NG1's hypothesis but equals **3/4** on this OS theory. A mixture of the same centred canonical scalars also obeys x_2 ≤ x_1/4, so NG2(b) cannot reproduce the constant kernel either. Global mean subtraction does not remove X: E[X]=0 already.

The connected spectral representation needs an additional positive zero-four-momentum term c_0, or a hypothesis excluding nonvacuum invariant vectors excited by e. Write S_2^T(x)=c_0+∫ρ(ds)G_s(x), with c_0≥0. One may enlarge comparators by independent classical random constants, or restrict the no-go theorem to c_0=0. Neither repair is stated. NG1's approximation proof on the stated KL subclass is valid; it does not prove the advertised universal no-go. NG2(a)'s subtracted-Stieltjes construction likewise treats only the KL part. An independent random constant can repair the GFF construction, but is outside the file's declared KL-only spectral formula. A mixture permitting random component means can repair NG2(b) too: use χ_{s,b}=A_sφ_s+b·1 with E[b]=0 and E[b²]=c_0. Therefore this counterexample refutes the displayed universal construction, not the possibility of a broader free-mixture representation once constant shifts are admitted.

The zero mode is harmless for the ultraviolet SEP-e argument (λ^{7.5}c_0→0), so this finding does not refute that separation theorem. It does refute the stated reason to rule out every fixed finite two-point witness under OS0–OS3 alone.

## Finding R5 — NG3's corrected example works, but the displayed exponent inequalities are reversed

**Verdict: CONFIRMED for χ′ and the restricted counterexample; REFUTED for the still-displayed bound orientation.**

Attachment: `NONFREE55.md:213-220`, `h(s) := 1/log(e + s)`; `:229-234`, `Consequence` / `κ_n ≤ n ≤ κ′_n`; `:453-460`, erratum E3, `χ′ := :ψ₁ψ₂:`. E2 removes the tensor imitation, and E3—not E2—is the erratum that introduces χ′.

Independent derivation: using K_1(u)=∫_0^∞exp(−u cosh t)cosh t dt gives ∫_0^∞u²K_1(u)du=2∫_0^∞sech²t dt=2. The change s=u²/r² therefore yields S_ψ(r)~h(r^{-2})/(π²r⁴). Splitting at u=√r bounds the small-u part of the normalized integral by (r/2)log(e+r^{-2})→0; on the complement the ratio of h's is bounded by 3 and converges to 1. This establishes the claimed asymptotic without numerical quadrature.

For independent copies, χ′=ψ₁ψ₂ has S_2^{χ′}=S_ψ²~1/[4π⁴r⁸log²(1/r)]. This is a Wightman Wick product and its separated Euclidean continuation, not an assertion that pointwise products of the Euclidean random distributions exist. To justify the product, the positive spectral measures of the two factors are tempered and supported in the forward cone. For their convolution, bounding the total energy bounds both individual energies; the convolution is therefore locally finite with polynomial growth. In every fixed higher Wightman contraction graph, energies on an internal line are bounded by sums of external energies crossing a time-order cut; the same argument gives tempered distributions. Finite spectral cutoffs yield positive Wick forms, and their distributional limits preserve positivity. Cross-species independence and the spacelike commutators give locality. Thus these products supply the separated OS data used here. Its connected graphs are alternating even cycles; odd moments vanish by ψ₁↦−ψ₁ symmetry. On nonnegative separated tests with nonzero leading cycle integral, the even connected n-point amplitude is a positive constant times u^{-n}. It meets AF-e and those restricted upper/lower envelopes, so AF-e does not imply NF-GFF. This supplies a concrete consistency example, not a YM construction.

However the original displayed bound is c_n u^{-κ_n}≤|A_n|≤C_n u^{-κ′_n} with κ_n≤n≤κ′_n. For example κ_n=1, n=2, κ′_n=3 would demand c/u≤A/u²≤C/u³: both sides fail at large u for positive fixed constants. The correction is

c_n u^{-κ′_n} ≤ |A_n| ≤ C_n u^{-κ_n}, with κ_n≤n≤κ′_n,

or, keeping the original order, κ′_n≤n≤κ_n. E3 repeats the exponent ordering without explicitly swapping the earlier displayed inequality, so this needs a separate correction. Arbitrary signed tests may cancel the leading coefficient; arbitrary odd lower bounds and tensor/sign data are not covered. The sweeping wording in §1.4 item 4 and the original NG3 consequence must be read with E2/E3's restricted scope, not as an all-orders no-go theorem.

## Finding R6 — nf55_c cannot identify K_1 from its gates

**Verdict: REFUTED as an independent identification of the K_1 series; CONFIRMED for the checked coefficients and required log structure.**

Attachments: `checks/nf55_c_criteria.md`, `verify the only analytic import` and C1–C3; `checks/nf55_c.py`, `residual_coeffs`, `res['C2']`, `res['C3']`; `NONFREE55.md:431`, C1–C3 record.

The original script was executed without modification and returned PASS. A separate in-memory mutation Y_M↦Y_M+α I_{1,M}, with α an arbitrary symbolic constant, also passes **all three C1/C2/C3 gates**. It changes the coefficient of z² in zY from γ_E/2−1/4 to γ_E/2−1/4+α/2. No source or output file was changed.

Re-derive the ODE: for Y=1/z+Σ_{k≥0}(a_k log(z/2)+b_k)z^{2k+1}, the equation gives a_0=1/2, 4k(k+1)a_k=a_{k−1}, and 4k(k+1)b_k=b_{k−1}−2(2k+1)a_k. It leaves b_0 free. Adding αI_1 is exactly that undetected homogeneous solution. A decay/boundary condition or an independently fixed b_0 is needed to select K_1. C3 is a polynomial-closure identity once zY is constructed as degree one in the formal log variable; it has no ability to test inverse-log asymptotics outside that construction. The stated failure controls do not address this blindness.

The actual imported formula agrees with [NIST DLMF 10.31.1](https://dlmf.nist.gov/10.31#E1), specialized to n=1. Its factorial denominators and harmonic-number coefficients give convergence on compact punctured domains by the ratio test. Derivatives preserve the degree in log; finite products give nonnegative log powers. Thus this gate weakness does **not** defeat the analytic input needed for FS. It limits what the recorded PASS establishes.

## Finding R7 — T_NF can hold for a strictly Gaussian field; the asserted comparison with non-Gaussianity is false

**Verdict: REFUTED for “stronger than the φ⁴ notion”; CONFIRMED as a precisely delimited comparator definition; NOT-VERIFIED as unrestricted absolute/net non-freeness.**

Attachment: `NONFREE55.md:103-121`, definitions of 𝔉_can, 𝒞, T_NF, NF-GFF; `:125-135`, `under any field assignment`; `:154-156`, `stronger than the φ⁴ notion`; `:86`, `Every functional ... automatically identification-free`.

A direct Gaussian counterexample: take a scalar GFF q with positive tempered spectral density

ρ_q(ds) = s²/[log(e+s)]² ds.

The same substitution as in R5 gives

S_q(r) ~ 192/[π²r⁸ log²(r^{-2})] = 48/[π²r⁸ log²(1/r)].

Here ∫_0^∞u⁶K_1(u)du=720∫_0^∞sech⁶t dt=720∫_0^1(1-v²)²dv=384, and the prefactor is 1/(2π²r⁸). The small-u/dominated-convergence argument is the R5 argument with u⁶K_1 and the squared log ratio; its small-u contribution is O(r³log²(1/r)), hence vanishes. The positive covariance can be defined with the finite contact subtractions used in NG2(a), which do not affect the separated data. This field obeys AF-e, hence the repaired SEP-e gives T_NF, but **all its connected n-point functions with n≥3 vanish**. Conversely, free Maxwell :F²: is non-Gaussian and fails T_NF. Therefore the two properties are not ordered by implication on the declared OS class.

The definition is defensible if stated verbatim as exclusion of scalar finite Wick polynomials, with finitely many derivatives, in finitely many canonical free fields, plus the specified ENV mixtures. It excludes a free realization under every assignment *in that class*. It does not prove exclusion of all generalized free fields, arbitrary relatively local fields, or every abstract embedding of a local net. Extending the polynomial class to all tempered local fields would require the applicable classification theorem, including its precise multi-species/spin hypotheses; the file explicitly disclaims dependence on its memory-only Borchers assertion. Do not then use that assertion implicitly in “every local composite” or “any field assignment.”

A functional of labelled {S_n^e} is invariant under field-preserving equivalence of the reconstructed theory. It is not automatically an invariant after forgetting the field or allowing arbitrary new generators. The all-polynomial quantifier is what removes the chosen comparator identification inside 𝒞. HINT2's rule is different: `HINT2_55.md:146-153` defines O^♮=½D²O(1)[A,A]. For O=O_2+O_4+…, (O²)^♮=0 while (O^♮)²=O_2² in general; this is not a multiplicative observable-algebra identification. Its profile separation relative to ID♮ cannot substitute for T_NF.

## Finding R8 — independent Maxwell reconstruction confirms the corrected witness and strengthens E1

**Verdict: CONFIRMED. Claim status: PROVEN for separated free Maxwell correlators in the stated convention.**

Attachments: `NONFREE55.md:420-424` / `D_{μν,ρσ}`; `:342-346` / connected four-point; `:439-442` / E1; `checks/nf55_a.py`, `PAIRS`, `CONF3`, `R1`, `a4`.

Independent route: on the six unordered two-form components put I(z)=1−2zzᵀ/r² and B(z)=Λ²I(z). Direct differentiation of G_0=1/(4π²r²) gives D(z)=B(z)/(π²r⁴). B is orthogonal. With Q=:Σ_{μν}F_{μν}F_{μν}:=2Σ_{A=1}^6:F_A²:, Wick's two-point contraction is 8 tr[D(z)D(z)ᵀ]=48/(π⁴r⁸). Independent colours multiply this by N²−1. The ordered-index squared sum is 4tr(DDᵀ)=24/(π⁴r⁸), hence 384 after removal of (4π²)^{-2} and multiplication by r⁸.

Let J be Euclidean Hodge star on two-forms. For an orthogonal orientation-reversing I, J(Λ²I)=−(Λ²I)J. Thus every D(z) anticommutes with J. An odd cycle product also anticommutes with J and has trace zero. The connected three-point contraction is 64tr[D_12D_23D_31] in the six-component convention; it vanishes at **every** separated configuration. This proves the three-point statement algebraically, without assuming the memory-only EM-duality argument or extrapolating from three tests. The same argument kills every odd connected cycle of Q.

For R1={(0,0,0,0),(1,0,0,0),(0,2,0,0),(0,0,1,3)}, set D̃=4π²D. Exact Fraction matrix multiplication gave the three six-component cycle traces

−96/214375, −552/456533, 168/831875.

At each vertex the factor in Q is 2. Each unoriented connected four-cycle has 2⁴ Wick assignments; therefore the prefactor is 2⁴×2⁴=256. Their sum times 256 is exactly

**−106278912/285333125 × (4π²)^{-4}.**

The disconnected part is exactly **214287181703424/13731656640625 × (4π²)^{-4}**. No number in the corrected Maxwell record is refuted.

The original nf55_a was also rerun and returned PASS: 40 changed components in A1-F, 384 at each of six A2 points, 304 for A2-F, three zero A3 results, scalar control 2/5, 48 connected A4 matchings and 12 disconnected matchings. Independent code used six-component inversion matrices and Fraction arithmetic, not the script's symbolic differentiation or 12-component matching enumeration. A1 is additionally verified generally: antisymmetrized derivatives of ∂_α∂_βH cancel because derivatives commute off coincidence. These are discriminating checks; the four-point identity alone would not independently check a common error in both implementations' propagator, which is why the separate inversion derivation matters.

Consequently “non-Gaussian e” is **not sufficient** for canonical-free exclusion. Calling it “vacuous” should mean this lack of discrimination, not that every gauge-invariant field in every theory must be non-Gaussian.

## Finding R9 — the restricted spectral no-go arguments are sound; one ENV quantifier is not

**Verdict: CONFIRMED conditional on KL with no invariant-sector term; REFUTED for “ENV fails whenever supp ρ is unbounded.”**

Attachments: `NONFREE55.md:173-180`, NG1 proof; `:196-208`, NG2(a)/(b), especially `K₀` and `ENV fails whenever supp ρ is unbounded`.

Reconstruction of NG1 on its actual domain: if F is Schwartz and flat on x=y, then F̃(z)=∫F(y+z,y)dy is Schwartz and flat at zero. For each M, |F̃(z)|≤C_M|z|^M near zero. Substituting w=√s z in ∫F̃G_s gives O(s^{-1-M/2}); the complement has exponential mass decay. Hence φ_F(s) decays faster than any power and is continuous down to s=0, using G_s≤G_0. A positive tempered spectral measure can be truncated at finite mass and replaced on that compact interval by positive atomic quadrature. The error tends to zero simultaneously for any finite list of F's. Atomic weights are exactly squared real coefficients of finitely many independent free scalars. Continuity of W then gives the stated no-go **on this KL subclass**. This proves density, not exact finite-free representability, and does not cover R4's constant kernel.

NG2(a): the subtracted identity is the finite geometric-series identity. For integer K≥K₀, its remainder has sign (1−u)^K. For u≥1, |S_K(u)|≤A|1−u|^K with A=∫ρ(ds)/(1+s)^{K+1}; for 0<u<1 it is nonnegative. Adding A(1+u)^K makes a positive radial tempered covariance. Its polynomial part is supported only at coincidence in position space and vanishes in positive-time reflected pairings. The remaining reflected form is an integral of nonnegative free-scalar forms. This gives the desired Gaussian separated two-point data. NG2(b)'s probability reweighting is likewise an exact identity when 0<Z<∞; the zero measure is a separate trivial case. These algebraic constructions do not eliminate the zero-mode omission in R4.

Counterexample to the ENV sentence: let ρ(ds)=exp(−s)ds and K₀=0. Then Z=1, ν=ρ, and every component is the unrescaled free scalar χ_s=φ_s. Although supp ρ is unbounded, G_s(r)≤G_0(r) gives ENV with B=1/(4π²), J=0 uniformly in s. Correct: the displayed construction has unbounded amplitudes when K₀>0 and support is unbounded; under those conditions no fixed logarithmic envelope controls them at r≈s^{-1/2}. Unbounded spectral support alone does not imply failure of ENV. For the AF-e examples the spectral mass is infinite, so their representation really does need a growing amplitude and falls outside ENV.

## Finding R10 — the core FS/SEP-e exclusion survives the hostile tests after the stated repairs

**Verdict: CONFIRMED for the finite-polynomial comparator class, with R2's mixture repair and R3's mass-sentence correction. Claim status: PROVEN.**

Attachments: `NONFREE55.md:242-267`, Theorem FS; `:270-284`, Corollary SEP-e; `:103-118`, comparator and ENV definitions.

Re-derived free side: each free propagator is a finite differential polynomial in a scalar G_m. The convergent Bessel expansion has an analytic power series plus one log times an analytic power series; derivatives introduce integer powers and never inverse logs. A finite Wick polynomial's separated two-point function is a finite sum of finite products of these entries, including all fermionic signs and cross-terms. It therefore has a convergent expansion in integer powers of r with log degree bounded by a fixed finite integer J. Scalar covariance makes its coefficients radial. If every coefficient vanished the separated analytic function would vanish, so a nonnull field has a first nonzero power and then a highest log degree at that power. Reflection positivity for the centred scalar, tested by approximate point supports on opposite sides of a time plane, makes S_2^T(r)≥0. Its nonzero leading coefficient is consequently positive when written with |log r|. This gives C r^{-γ}|log r|^j(1+o(1)), γ∈Z, j≥0, C>0. C and the surviving γ may depend on masses, as R3 shows.

For f,g≥0 with disjoint nonempty supports, I_γ=∫f(x)g(y)|x−y|^{-γ}dxdy>0. The expansion is uniform over d≤|x−y|≤D, so the smeared kernel is C I_γ λ^{-γ}|log λ|^j(1+o(1)). γ≥8 contradicts λ⁸S_2→0. For integer γ≤7, λ^{15/2}S_2→0 contradicts the lower half at η=1/2. Null fields fail the lower half directly. Derivatives and tensor products do not escape: derivatives were included in the expansion and a finite tensor product is just a finite enlarged field list.

For a mixture, use the variance-corrected formula in R2. Nonnegative component kernels and Fatou force every nonnull component to have γ_α≤7 almost surely. ENV, at λD≤r_0<1, bounds their average by B′λ^{-7}(|log λ|+c)^J. The finite mean-variance term contributes only O(1). Multiplying by λ^{15/2} again tends to zero. Thus the exclusion covers **every finite mixture** and **every specified ENV mixture**, not mixtures with arbitrary mass-dependent amplitudes. For finite mixtures take a common smaller r_0<exp(−1), the largest finitely many log degrees and constants; this establishes ENV directly. Null connected components can be omitted and their constant means handled separately.

The two AF-e clauses are substantive: a dimension-eight free composite defeats the lower clause alone, and a lower-dimension free scalar defeats the upper clause alone. The Gaussian GFF in R7 satisfies both, so their conjunction is not an unsatisfiable gate. What it separates is exactly the bounded canonical class just proved.

## Finding R11 — H-RED^e is a valid conditional limit argument, not a produced Yang–Mills witness

**Verdict: CONFIRMED for the implication and same-test-space interface; NOT-VERIFIED for its Yang–Mills hypotheses. Claim status: CONDITIONAL; TS-e-up, TS-e-low and the required regularity remain OPEN.**

Attachments: `NONFREE55.md:286-314`, especially `K ≥ m + d₀`, `Lemma TS`, `Theorem H-RED^e`; `:521-531`, OSLEAF addendum; `FLOW.md:433-437`, Theorem F-tune; `OSLEAF55.md:149-173`, D2/D5/D8/D9; `:311-324`, H_reg-sep and extension proof; `:343-347`, H_int-sep; `:484-505`, ALG/DET.

Symbol pin: g in F-tune is g_lane, u_k=g_k^{-2}, whereas g in NONFREE55 §4.1 is explicitly g_std. Their relation is g_std²=2N g_lane². F-tune gives, after substituting k=K−m,

U_−(m)=g_lane^{-2}+β_−m log L−R_F ≤ u_{K−m} ≤ g_lane^{-2}+β_+m log L+R_F=U_+(m).

Here R_F is FLOW's bounded additive flow error, not torus radius R, and the TS exponents κ,κ′ are not the SRC-κ label or a blocking stiffness. This bracket is uniform in K and the torus and has positive slope β_−. For sufficiently large m the upper TS bound tends to zero as U_−^{-κ}. Consistency of the two TS bounds for arbitrarily large u forces κ′≥κ>0; the lower bound then gives L^{ηm}c_−U_+(m)^{-κ′}→∞ for each η>0. No fixed bare coupling is substituted for the tuned output.

For each fixed m, take the continuum/infinite-volume subsequence first: K_j≥m+d₀ eventually, and compact supports fit for large R_j. Uniform bounds survive convergence of that one separated value. Only afterwards let m→∞. This order needs neither exchange of limits nor a uniform-in-m convergence rate. It applies to every admissible tuned limit point possessing the named value convergence. To conclude a reconstructed OS theory, the other OS/reconstruction requirements remain necessary; omitting H_Euc from this particular comparator contradiction does not produce Euclidean invariance.

The test f_{λ_m}⊗g_{λ_m} is smooth, compactly supported and stays off coincidence for every fixed m. It is in OSLEAF D2's 𝒟_2, uses D8's already-centred field, and for Z=1 its lattice value is exactly the TS connected covariance. The dense-family extension needed here is elementary: approximate this fixed test by a member of the determining family in the uniform regularity seminorm; the two approximation errors are uniform in the cutoff, and the middle difference tends to zero. Thus convergence on D plus H_reg-sep supplies the witness values. Full reconstruction from OSLEAF and its general estimates are not independently certified by this interface check.

This removes the *logical need* for the old flowed-observable MOM-E, flow-time interpolation and ID♮ inputs for this new target. It does not derive any of the new TS estimates from those old inputs. In particular, a positive lower bound at one coarse scale cannot replace TS-e-low at every short scale. Constant finite field rescalings preserve AF-e and the comparator class; cutoff-dependent Z(a)→0 or ∞ do not. No nonperturbative proof of the normalized lower bound on this actual clover field has been supplied here. That is the most dangerous unverified mathematical obligation.

The claim that LF-inst leaves this *displayed implication* is correct: it is absent from the hypotheses. The stronger practical claim that proving TS-e needs no comparably difficult large-field control remains NOT-VERIFIED. LF-dec is an OPEN decoupling estimate, and its summation must use R1's corrected threshold if the boundary case is entertained.

## Finding R12 — E2's tensor obstruction is valid on its stated positive Bianchi spectral class

**Verdict: CONFIRMED. Claim status: PROVEN with the stated positive spectral representation.**

Attachment: `NONFREE55.md:443-452`, E2, especially `Σ_{ij}T^I_{ij,ij}(p) = 4|p⃗|²` and the coefficient `6K_1(1)/π²`.

For the ordered spatial pairs i,j∈{1,2,3}, the tensor trace is Σ_{ij}(p_i²+p_j²−2δ_ij p_i p_j)=4Σ_i p_i². At a time-axis point the separated magnetic kernel is therefore −4Δ_3S(te_0)=−12S′(t)/t. A single mass shell contributes

−12G_s′(t)/t = 3[ z²K_0(z)+2zK_1(z) ]/(π²t⁴), z=√s t.

The positive integral representation of K gives K_0(z)>0, and differentiation gives (zK_1(z))′=−zK_0(z). For 0≤z≤1, zK_1(z)≥K_1(1). Integrating only s≤t^{-2} yields exactly t⁴C_mag(t)≥[6K_1(1)/π²]ρ([0,t^{-2}]). For nonzero positive locally finite ρ, the right side is eventually bounded below by a strictly positive constant. Contact polynomials vanish at this separation. Thus t⁴C_mag(t) cannot tend to zero. No tensor imitation of the withdrawn form is available. This says nothing against the scalar χ′ or Gaussian q examples in R5/R7, whose spectral dimensions differ.

## Finding R13 — nf55_b's normalization arithmetic is correct, with physical inputs still separate

**Verdict: CONFIRMED for B0–B4 as algebra under the stated definitions; NOT-VERIFIED for a renormalized operator identity e∝Θ.**

Attachments: `NONFREE55.md:320-330`, `g = g_std`, `e_a = (4a⁴)⁻¹`, `Θ = −(11N²/(24π²))·e`; `checks/nf55_b.py`, B0–B4; `FLOW.md:24-26`, Wilson normalization.

Re-derivation: Re tr exp(iX)=N−tr X²/2+… and tr(t^at^b)=δ^{ab}/2 give s(U_p)=a⁴g_std²(F^a_{μν})²/(4N)+…. Multiplying by u=2N/g_std² and summing μ<ν gives ¼Σ_{μν,a}(F^a_{μν})². Replacing u by 1/g_std² reduces this coefficient by **1/(2N)**. Four clover terms cancel the prefactor 1/4, while summing μ≠ν counts each unordered plane twice, giving e=g_std²F²/(4N)=F²/(2u). In the SU(2) check 2(1−cos(θ/2)) has θ² coefficient 1/4, as recorded.

Given β(g_std)=−b_0g_std³+… and b_0=11N/(48π²), Θ/e=−2Nb_0=−11N²/(24π²). Multiplying the independently derived free-Maxwell two-point coefficient by (2u)^{-2} gives **12(N²−1)/(π⁴u²)**. The original nf55_b rerun returned PASS, including its factor-2N failure control. No recorded coefficient is refuted.

The renormalized anomaly convention βF²/(2g) is present in [Tanaka, arXiv:1811.07879](https://arxiv.org/abs/1811.07879). That checks the cited formula's convention, not its constructive application to this lattice field. This review has not rederived the one-loop beta function, constructed a stress tensor or proved its Ward identities, matched renormalized composite operators, or supplied Z=1 nonperturbatively. B3 hard-codes b_0 and the anomaly formula; B4 is just amplitude arithmetic. Their PASS cannot certify those physical premises.

## Finding R14 — trace and scattering rejections are route-specific, not universal impossibility results

**Verdict: CONFIRMED for rejecting “Θ≠0” as a class-wide witness and for the absence of a supplied scattering route; REFUTED for treating a gap/isolated shell as a universal necessity of scattering theory.**

Attachments: `NONFREE55.md:331-337`, trace rejection; `:149-151`, `isolated mass shells, i.e. a gap`; `:349-353`, LSZ/Haag–Ruelle rejection.

Free massive counterexample: the improved scalar stress tensor in four dimensions has trace m²:φ²: on the free equation of motion, up to the overall signature convention. This follows by adding (1/6)(η_{μν}□−∂_μ∂_ν)φ² to the canonical tensor, taking its trace, and using □φ=−m²φ. The trace is nonzero in a free theory. For m=0 an unimproved tensor can have a nonzero derivative trace which the improvement removes. Thus a trace value without the tensor/Ward identification cannot exclude the whole comparator class. The leading algebra in R13 does not prove that every possible trace-anomaly witness is equivalent to AF-e; “subsumed” is a description of the proposed amplitude test only.

A mass gap and an isolated one-particle shell are distinct: the even subtheory generated by :φ_m²: has a positive two-particle threshold and no isolated single-particle state. Conversely, [Dybalski, Haag–Ruelle scattering theory in presence of massless particles](https://arxiv.org/abs/hep-th/0412226) constructs scattering of stable massive particles without a mass gap, under a Herbst regularity hypothesis. This is a counterexample to a blanket gap necessity, not a new scattering construction for this lane. Ordinary Haag–Ruelle's isolated-shell route, extended stable-particle routes, and massless routes all require hypotheses not furnished by this e-only OS0–OS3 package. “Not available from these inputs” is justified; “all scattering or higher-cumulant routes are impossible” is not.

## Finding R15 — the primary literature does not identify T_NF with the full target theorem

**Verdict: CONFIRMED for the cited Φ⁴_3 non-Gaussian result; NOT-VERIFIED for an equivalence between T_NF and the literature's Yang–Mills target. Claim status: ARGUED as a proposed intermediate criterion.**

Attachments: `NONFREE55.md:123-159`, target choice and literature comparison; `:505-508`, OWN-free recommendation; `OSLEAF55.md:493-495`, e-cyclic subtheory only.

[Jaffe–Witten, Quantum Yang–Mills Theory, §§3–4, PDF pp.5–6](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf) asks for a quantum gauge theory with gauge-invariant curvature-polynomial operators, short-distance behavior matching asymptotic freedom, a stress tensor and OPE structure, and a positive mass gap. Its preceding axiom discussion includes uniqueness of the vacuum. It does not define nontriviality as T_NF or provide the file's finite-polynomial-plus-ENV classification. An e-cyclic theory with AF-e is therefore an intermediate scalar observable result, not by itself the stated Yang–Mills existence theorem. Its restricted comparator exclusion is useful but cannot replace these other requirements.

[Gubinelli–Hofmanová, arXiv:1810.01700](https://arxiv.org/abs/1810.01700), abstract, does assert non-Gaussianity of every limiting elementary-field law. It also distinguishes the OS properties proved there from rotation invariance and clustering. That verifies the file's narrow literature comparison, not the claimed implication ordering rejected in R7. There is no contradiction between using a labelled elementary-field criterion in that construction and requiring a richer free-composite comparator for the gauge-invariant e-field here.

Recommendation for the theorem statement: say precisely “the e-correlators are not realizable by a finite scalar Wick polynomial in finitely many canonical free fields, nor by a mixture satisfying ENV.” Keep NF-GFF and the ID♮-relative target distinct. Do not call this a literature-certified definition of unrestricted interacting Yang–Mills theory.

## Finding R16 — NG1 does not refute PANEL_P1 item 4 at arbitrary moment order; one inherited line citation has drifted

**Verdict: REFUTED for the inference to unrestricted finite-moment impossibility and for the inherited current-line citation; NOT-VERIFIED for NG1′.**

Attachments: `NONFREE55.md:181-192`, NG1 consequence and NG1′; `:487`, summary item 21; `:492`, inherited PANEL_P1 verdict; `:507-508`, replacement recommendation; `PANEL_P1.md:63`, `A specified continuous finite-moment witness W`; `FLOW.md:38-42`, evolving PROOF pointer.

PANEL_P1 item 4 permits general finite moments. NG1 concerns only two-point values, and its own all-orders extension is explicitly OPEN. Even with a no-zero-mode hypothesis repairing R4, NG1 supplies no impossibility result for a four-point or other higher-order witness. Thus the proposed asymptotic family is a valid replacement route, not a deduction that PANEL_P1's literal unrestricted contract is unsatisfiable. R4 additionally shows that its advertised “every OS theory” two-point conclusion needs repair.

NONFREE55 itself gives locating strings rather than numerical PROOF line references in these arguments. The supporting FLOW pin still says in its latest local erratum that the β′_B line is `PROOF l.4162`. That current line instead discusses a constrained-stability partition-function ratio. String search locates the displayed conversion **β′_B≈2N·2b_0=4Nb_0=11N²/(12π²)** at **PROOF.md:4437** (rechecked 2026-10-29 05:55:42 UTC), under `[R56-fix: one normalisation, Balaban's.]`; the encompassing LF-count proposition starts at line 4419. Correction: 4162 → 4437 at that timestamp for this one pointer, not a global offset. During this review the same conversion moved from line 4436 to 4437; the locating string, not a fixed offset, is authoritative. The conversion itself is unchanged and agrees with the independently checked factor 2N.

## Gate audit, symbol/quantifier audit, and reading receipt

| Gate | Could the tested equality fail? | What it actually establishes |
|---|---|---|
| nf55_a A1 / A1-F | Yes; the symmetric-derivative control changes 40 components | Four configurations in the script; the commuting-derivatives argument proves gauge-term cancellation generally |
| nf55_a A2 / A2-F | Yes; dropping the term gives 304 instead of 384 | Exact normalization; independently reconstructed for arbitrary direction with Λ²I |
| nf55_a A3 / A3-F | Yes; scalar control is 2/5 rather than 0 | Three exact configurations; the Hodge-star proof supplies the all-configuration statement |
| nf55_a A4 / A4-F | Yes; nonzero connected part, independent pairing count, nonzero disconnected control | The quoted four-point value; propagator correctness additionally checked by the separate six-component route |
| nf55_b B0 | Yes, as a Taylor-coefficient check | 1/4; no nonperturbative physics |
| nf55_b B1 / B1-F | Yes; wrong Wilson convention gives the factor 1/(2N) | Algebra under the plaquette expansion and generator normalization |
| nf55_b B2 | Yes, if the specified index/clover factors are changed | Algebra for the stated e definition, not operator renormalization |
| nf55_b B3 | Yes, for an algebra error; physical formula and b_0 are inputs | −11N²/(24π²) conditional on those inputs |
| nf55_b B4 | Only an arithmetic error | Multiplication of the imported amplitude by (2u)^{-2} |
| nf55_c C1 / C1-F | Yes for ODE residuals; no for an added αI_1 solution | Truncated ODE recurrence, not unique K_1 identification |
| nf55_c C2 | Some coefficients could be wrong; absence of inverse logs is built into the ansatz | Structure of the polynomial supplied to the checker |
| nf55_c C3 | No independent decision once C2's structural ansatz is fixed | Polynomial closure; the αI_1 mutation also passes |
| AF-e / TS-e pair | Yes; γ≥8 fails its upper half and γ≤7 its lower half | A real canonical-free separator; GFF counterexamples prove it is satisfiable |
| H-RED^e | No numerical gate is claimed | A conditional sequential-limit argument; existence of its estimates remains OPEN |

The symbol checks that affect conclusions are: g_lane versus g_std (R11/R13); c multiplying log(1/g), versus a redefined coefficient multiplying log u (R1); κ in an upper bound versus κ′ in a lower bound, versus the SRC-κ name (R5/R11); γ as the free-field leading exponent versus FLOW's admissibility threshold (R3/R10); and a full second moment versus a connected one under mixtures (R2/R4). The propagator pin is G_s with s a mass squared (`NONFREE55.md:62`); FS's G_m formula instead uses m as a mass (`:250-251`), so s=m². The m in λ_m is a scale index. These uses are not interchangeable. “FS” is explicitly this file's free-side theorem, not OSLEAF's distinct forced-normalization proposition. No ε, θ or c_1/C_1 comparison from other lane results was accepted by symbol alone.

The quantifiers that were actually checked are: fixed g_lane as F-tune input with g_bare an output; fixed m before K,R limits; constants independent of K,R; the lower bound at **every** short scale; uniform ENV constants across mixture components; and the c=2p boundary comparison **after**, not before, summing scales. The core F-tune bracket passes this check; the scale-sum threshold and NG3 exponent orientation do not.

Local reads were restricted to the target and named supporting sources/checks, the methodology explicitly named in the supplied AGENTS instructions, and two discretionary sources: `/Users/jonBridger/.codex/skills/review-loop/SKILL.md` and `FLOW.md`. Supporting source content inspected: OSLEAF definitions/closure/ALG, PANEL_P1's witness contract, HINT2's ID♮ definition and target, the previous assembly review's relevant strings, and narrow PROOF excerpts at the located normalization/cited lines. No snapshot or audit ledger was opened. No git command was run. Only this deliverable was intentionally written; the original scripts were read and run with bytecode writes disabled, and independent arithmetic ran in memory.

Process disclosure: the initial reconnaissance rg pattern accidentally matched every line of NONFREE55; the tool capped and truncated the returned excerpt. Subsequent substantive reads used targeted matches and bounded ranges. PROOF was never read in full. The PRE-STATED section was created before derivations; findings were then appended incrementally. No source status was treated as proof. No external sentence was quoted; literature claims above are paraphrased with primary-source links.

## Summary table

| Finding | Review verdict | Claim status / result that survives |
|---|---|---|
| R1 — summed LF boundary | REFUTED | GAP: c>2 must be c>6 in the displayed g convention; strict 2p>1 route survives |
| R2 — affine connected witness / arbitrary free admixture | REFUTED | PROVEN after variance repair: SEP-e still excludes ENV mixtures; low-dimension free phases may coexist |
| R3 — masses only subleading | REFUTED | PROVEN: masses can enter leading C or change γ; nonnegative-log FS form survives |
| R4 — universal KL/NG1 | REFUTED; NG2 universal construction NOT-VERIFIED as written | GAP: invariant zero-momentum sector omitted; NG1 is PROVEN only on the declared KL subclass |
| R5 — χ′ / NG3 bound orientation | CONFIRMED example; REFUTED ordering | PROVEN: χ′ meets AF-e; even-order restricted envelopes need correctly ordered exponents and nonzero pairings |
| R6 — Bessel gate completeness | REFUTED identification; CONFIRMED required series structure | PROVEN: αI_1 ambiguity passes all gates; independently checked analytic log structure remains sufficient |
| R7 — T_NF versus Gaussianity / unrestricted assignments | REFUTED implication ordering; unrestricted extension NOT-VERIFIED | ARGUED target choice: Gaussian q satisfies T_NF; polynomial scope must be explicit |
| R8 — corrected Maxwell results | CONFIRMED | PROVEN: stated two-/four-point constants and identically vanishing separated three-point function |
| R9 — spectral constructions / unbounded support | CONFIRMED on KL subclass; REFUTED ENV quantifier | PROVEN: atomic approximation and subtracted covariance; support alone does not force ENV failure |
| R10 — FS/SEP-e core | CONFIRMED with explicit repairs | PROVEN: excludes finite Wick polynomials, tensor products, finite mixtures and ENV mixtures |
| R11 — H-RED^e / YM estimates | CONFIRMED implication; hypotheses NOT-VERIFIED | CONDITIONAL reduction; TS-e-up, TS-e-low, H_reg and LF-dec remain OPEN |
| R12 — E2 Bianchi obstruction | CONFIRMED | PROVEN under positive Bianchi spectral representation, with exactly 6K_1(1)/π² |
| R13 — nf55_b normalization | CONFIRMED algebra; physical matching NOT-VERIFIED | CONDITIONAL anomaly interpretation; no 2N error in recorded coefficients |
| R14 — anomaly / LSZ rejection | CONFIRMED as route assessment; REFUTED blanket gap necessity | OPEN alternative routes; Θ≠0 cannot distinguish every free theory |
| R15 — literature / theorem target | CONFIRMED narrow citation; equivalence NOT-VERIFIED | ARGUED intermediate target, not full Jaffe–Witten compliance |
| R16 — PANEL inference / line drift | REFUTED inference and citation; all-orders no-go NOT-VERIFIED | OPEN NG1′; 4162→4437 as of the recorded UTC read |

## Exactly what may be banked

1. **PROVEN:** for a nonnull Hermitian scalar finite Wick polynomial in the declared finite canonical-free class, the separated two-point kernel has a first nonzero integer power with nonnegative log degree and positive coefficient. Delete the assertion that masses are always subleading. With the connected-mixture variance correction, **AF-e excludes this class, every finite mixture, and the stated ENV mixtures**.
2. **CONDITIONAL:** fixed-scale TS-e bounds plus the uniform F-tune bracket and convergence on the separated e-test family imply AF-e for every admissible limit point. This is a witness on OSLEAF's produced separated algebra, with Z=1 as specified. It does not establish the hypotheses or the rest of OS reconstruction.
3. **PROVEN:** NG1's finite-atomic approximation and NG2's spectral constructions on the **no-zero-mode KL subclass**. The universal OS0–OS3 import is not bankable. A Gaussian random constant gives the explicit NG1 counterexample W=3/4; NG2 needs the separately handled invariant sector.
4. **PROVEN:** the scalar GFF composite χ′ meets AF-e and the corrected restricted even-order envelopes; the direct Gaussian q example also meets AF-e. Thus this witness does **not** establish NF-GFF or non-Gaussianity. E2's positive Bianchi-tensor obstruction is independently established within its stated class.
5. **PROVEN:** the corrected free-Maxwell values 48(N²−1)/(π⁴r⁸), identically zero separated three-point function, and −106278912/285333125·(4π²)^{-4} at R1; the stated Wilson/clover normalization arithmetic and factor-2N control. The anomaly-to-e operator identification is not banked.
6. **PROVEN corrections:** the summed boundary threshold is c>6 for p=1/2 with p(g)=(log(1/g))^p; NG3's lower/upper exponents must be swapped in the displayed inequality; the connected witness is not affine without common means; masses can enter leading terms; nf55_c cannot distinguish K_1 from K_1+αI_1; the inherited PROOF line pointer is stale. **NOT banked:** a Yang–Mills non-freeness theorem, unrestricted free-net exclusion, an all-orders finite-moment no-go, elimination of the large-field difficulty, or full Jaffe–Witten compliance. **Single most dangerous unverified item: TS-e-low, uniformly at every short scale for the very same correctly normalized clover e field whose separated OS limits are constructed.**
