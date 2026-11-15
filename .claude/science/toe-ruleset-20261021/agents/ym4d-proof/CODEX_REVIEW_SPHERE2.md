# PRE-STATED — independent hostile review of SPHERE2_55

UTC: 2026-10-29 06:33:39. This section is written before mathematical derivation or execution of checks. Review in progress; nothing below is a certification of the Yang–Mills construction.

Scope: SPHERE2_55.md, its named s2_55_1 / s2_55_1b / s2_55_2 checks, and bounded, string-located passages of the named prior review and PROOF.md where necessary. The two additional reading slots are reserved for the mandatory SCIENCE_WORKFLOW.md and its applicable review procedure. No git; no snapshots or audit ledgers; the sole writable file is CODEX_REVIEW_SPHERE2.md. Calculations will use hand derivations and exact rational/symbolic arithmetic only. This report identifies the reviewer as Codex; no unverified model-identity claim is evidence.

Targets and pre-stated refutation criteria:

1. Proposition M: reconstruct the Haar divergence, signs of the two plaquette orientations, plaquette counting, and the restriction on v. A legal configuration/vector field violating the claimed identity, or a missing geometric restriction, refutes the corresponding statement. Separately check the B_loc bookkeeping.
2. SA-K obstruction and scheme family: derive the coefficient shift; test admissibility and distinguish tree order from the order of the divergence. Test whether the stated Ward hypotheses actually force equality of profile coefficients. A nonzero insertion that fails to identify a variable coefficient is a possible refutation, not a pass.
3. REG and CL: derive every Cauchy constant from the actual analytic domain and track dependence on u, the band width, and profile span. A circle outside the stated domain, an unclosed margin inequality, or a variable-source expansion lacking a uniform remainder defeats the claimed implication.
4. W1: reconstruct the product estimate and distinguish sufficient bounds from necessary ones. Test the coupling/logarithm relation actually needed.
5. Seam: classify low-dimensional operators under the stated symmetries, including gluing fields and field-independent terms. Derive scaling dimensions and the energy comparison. A surviving allowed relevant operator or a coarse-field quantifier not supplied by the hypotheses defeats the corresponding universal claim.
6. Tower and N5′: reconstruct reverse conditioning, covariance decomposition, index ranges, and limit order. Try non-Markov, signed-insertion, and coarse-measurable-observable counterexamples. Conditional-mean contraction must not be silently extended to norms, covariances, or complex measures.
7. Gates and inherited refutations: determine whether each cited gate can fail for the mathematical defect it claims to detect; distinguish algebraic examples from theorem coverage and reruns from provenance verification. Rebuild the paired-diagonal and absolute-bound counterexamples.

Verdicts: CONFIRMED / NOT-VERIFIED / REFUTED for findings; PROVEN / ARGUED / CONDITIONAL / GAP / OPEN for claims. Each finding will identify an exact locating string and current file lines. Refuted numerical claims will receive a corrected derivation. Final sections will give a summary table and exactly what may be banked.

## Findings (appended during review)

### F1 — CONFIRMED: Proposition M, for the displayed field and the stated bulk geometry

Attachment: SPHERE2_55.md:176–213, locating strings `(D-link)`, `(D-plaq)`, `Quadratic collapse`. Claim: PROVEN for the displayed left/right generators; its application at a cutoff or seam retains the explicitly stated boundary qualification.

Independent derivation: for an orthonormal anti-Hermitian basis with inner product −c tr(XY), completeness gives ΣTα² = −(N²−1)/(cN)·1. Since tr Tα = 0,

Σ tr[Tα π(Tα P)] = ½Σ tr[Tα²P + TαP†Tα] = −(N²−1)/(cN) Re tr P.

Differentiating ξ = −v[π(P+)−π(P−)]/(2a) therefore gives div_b Ξ = −(N²−1)/(2Na)·v(Re tr P+−Re tr P−) = N C_F v(s+−s−)/a. The right half is actually identical as a tangent vector, not merely to first order: Q = U⁻¹P⁻¹U implies π(Q) = −Ad(U⁻¹)π(P), so the displayed extra minus sign gives ξ̃ = Ad(U⁻¹)ξ. This establishes its divergence without a second perturbative calculation.

Collect the four incident links of one plaquette. Their coefficient is vν(bottom)−vν(top)+vμ(left)−vμ(right). Centered differences of a quadratic are exactly −a(∂νvν+∂μvμ). Only for the stated conformal fields does this become −2a div(v)/4. Consequently −div Ξ = 2N C_F Σ(div(v)/4)s, and rotations give zero. No continuum approximation or smooth-field restriction enters this identity. It is not an unrestricted identity on seam plaquettes with a nonquadratic cutoff. Direct comparison with the full ROTDEF source lies outside this review's reading allocation; the result here concerns precisely the generator reproduced in the target.

### F2 — CONFIRMED: bookkeeping and leading scheme shift; matching remains CONDITIONAL

Attachment: SPHERE2_55.md:216–226 (`B_loc = C_F + u`), 256–263 (`w^ν_b := 1 + λ`), and 282–288 (`local log-scale change`).

The matched translation coefficient is u+f₁ and the trace coefficient is 4u+f_D. Integration by parts subtracts 4(u+f₁), leaving f_D−4f₁. Adding F1 gives B_loc = C_F+f_D−4f₁ and differentiating u+f₁ gives κ_W=1+f₁′. This is an implication of the matching expansion, not its proof. Calling vector and trace matching “one clause” repackages the same unresolved trace obligation.

For the scheme shift, put P±=exp X± with X± anti-Hermitian. Through cubic order, Re tr[(π(P+)−π(P−))(P++P−)] = tr(X+²−X−²): cross quadratic terms cancel by trace cyclicity and cubic terms have imaginary trace. Hence E = −λ tr(X+²−X−²)/(2Na²) = λ(s+−s−)/a² + quartic terms. The new link divergence is −λv(s+−s−)/a; collection subtracts 2λ(div v/4)s from −div Ξ. The coefficient is therefore C_F−λ/N, reaching zero at λ=(N²−1)/2 and every real value for finite real λ. The multiplier is local, gauge invariant and reflection even, and tends to 1 at smooth fields; positivity of the multiplier is not needed for an integration-by-parts vector field.

Evaluating the Ward observable on a classical smooth background leaves precisely this measure coefficient; this does not compute quantum matching. A prescribed local coupling profile gives ∂log(s)S_eff = T′∂uS_eff by the chain rule. Identifying that derivative with the matched dilation response would already assume the desired Ward relation. The restricted SA-K-plus-Cauchy argument supplies no quantum trace coefficient. This is not a no-go theorem for every method using SA-K as one ingredient.

### F3 — REFUTED: the claimed complete two-sided seam list omits an allowed dimension-3 operator

Attachment: SPHERE2_55.md:402 (`complete local list`), 415–421 (`Two-sided structure`), 429–437 (`Mixing`, `only candidate (CS)`), 530–531 (`no marginal seam operator`), and 681 (`No seam operator of dimension ≤ 3 survives`). Claim status: GAP in the exhaustive classification and its use to conclude universal absence of tuning; this is not a counterexample to N5-T* itself.

Use exactly the two-sided field space introduced by the target. After transporting the southern connection through the crossing link, both connections transform under the same boundary gauge transformation. Set J_i=A_i^+−A_i^− and F^Σ_ni=F^+_ni+F^-_ni, with one fixed signed normal n. Then

O₃ = Σ_i tr[J_i F^Σ_ni]

is a gauge-invariant local seam operator of canonical dimension 1+2=3. Under θ_eq, J→−J and F^Σ_ni→−F^Σ_ni, so O₃ is even. Under a tangential coordinate reflection both contracted tangential components transform together; there is no orientation tensor, so it is also even. The isotropic contraction already obeys the stated symmetry group; no staircase pseudoscalar is needed. It is not identically zero: in a common Abelian su(N) direction H with tr H²≠0, choose J₁=jH and F^+_n1=F^-_n1=fH, giving O₃=2jf tr H².

The single-connection statement remains correct: there is no nonconstant gauge-invariant curvature polynomial of dimension below four. But the proof switches to that single-connection list while retaining a two-sided J mode. Setting J=0 first, or eliminating O₃ by gluing equations/field redefinitions, requires an additional argument. For example a positive quadratic term K〈J,J〉+c〈J,F^Σ_n〉 can be completed to a square; eliminating J leaves an F² term of order c²/K, which is irrelevant if K~u/a and c is bounded (or grows only logarithmically). Here 〈·,·〉 is a positive Lie-algebra inner product, avoiding the sign of tr(J²) in anti-Hermitian conventions. That is a plausible repair, not a symmetry exclusion and not a uniform conditional-mean estimate at arbitrary crossing data. Correct count: at least one parity-even mixed dimension-3 structure, in addition to the dimension-2 gluing term. Dimension four is still irrelevant on a three-dimensional seam.

### F4 — REFUTED: plain-insertion nonvacuity alone does not prove the appended scheme-independence corollary

Attachment: SPHERE2_55.md:264–275 (`scalar-channel mismatch insertion`, `except at most one`), especially 295–300 (`Part (d) needs only the CONSTANT-weight case`). Claim status: GAP. The earlier, stronger hypothesis testing all relevant weighted/localized insertions must not be replaced by mere nonvacuity of the plain insertion without a response-norm estimate.

The unproved operation is replacing a spatial coefficient c+o(1) by c inside an a-dependent normalized covariance. Here is an exact counterexample to that inference. Let U>1, let X=±1 with equal probabilities, F=X, and define nonnegative insertions S₁=U²(1+X), S₂=(U²−1)(1−X). Their covariance functional is

L_U(w)=Cov(F,w₁S₁+w₂S₂)=U²w₁+(1−U²)w₂.

Thus L_U(1)=1 is uniformly nonvacuous. Take two coupling values u₁=U, u₂=U+1, and the analytic mismatch δ(u)=−1+1/u. Both values converge uniformly to −1, but

L_U(δ)=U²(−1+1/U)+(1−U²)(−1+1/(U+1))=0

exactly. This has the asserted asymptotic scheme coefficients B=C_F, B′=C_F−1+1/u, κ=κ′=1, corresponding to λ=N; both tree values have o(1) corrections. The bounded holomorphic coefficient f_D^{new}=−1+1/z satisfies a relative-disc bound. Nevertheless the plain-insertion test cannot exclude their different limiting slopes. The vanishing weighted Ward mismatch plus the stated plain nonvacuity therefore does not imply the corollary. This is a countermodel to the claimed deduction, not a proposed Yang–Mills state or a counterexample to the stronger weighted nonvacuity assumption.

Repair: control the normalized response functional on the actual coefficient error, e.g. |L_a(r_a)|→0 whenever the particular r_a=o(1) occurs; a uniform operator norm on the relevant weights is sufficient. A localized/coercive weighted-insertion hypothesis can also supply the missing information. With that repair and κ→1, at most one λ can have B^fl=o(1). Boundedness B^fl=O(1) by itself follows from bounded f_D,f₁ and does not mean it stays away from zero or has a limit. Under the separately assumed one-loop limit the stated limit 2β₀−C_F is valid; the limit itself remains CONDITIONAL.

The original stronger weighted hypothesis has a valid route: REG makes the mismatch's derivative O(1/u), so its variation on a fixed-width band is o(1). If it stays nonzero anywhere along a subsequence, it has fixed sign and is bounded away from zero across that band. A nonvacuity bound applying uniformly to precisely these a-dependent weights then contradicts the vanishing weighted Ward identity. This proves uniform slope agreement under that stronger hypothesis; it does not establish it from one plain insertion.

### F5 — CONFIRMED for positive measures; REFUTED for the unqualified complex-sector export of the tower bound

Attachment: SPHERE2_55.md:441–455 (`normalised nonnegative kernels`, `Every ... conditional-MEAN clause`), 236–239 (complex-sector `(L-b)`), and 355–357 (`coarse-image part of (L-b)`, `The sector`).

For an actual probability Markov chain, conditioning on U_k separates the earlier and later variables. Therefore E[X|U_n]=E[E[X|U_k]|U_n]. A convex average contracts distance from any constant and the range/oscillation; Jensen gives the L² contraction about EX. Strictly positive finite-lattice densities justify every coarse configuration, not merely almost every one. These are PROVEN statements, restricted to one measure and conditional means. They do not control conditional covariances or compare different theories.

The target exports this to `(L-b)` without restricting its complex coupling/source domain. Positivity is indispensable. An exact signed example uses fine weights w₀=1, w₁=−1/1024, X(0)=1, X(1)=−1, and a strictly positive normalized forward kernel with K(v=0|0)=1/2048, K(v=0|1)=3/4. At v=0,

E[X|v=0] = (1/2048+3/4096)/(1/2048−3/4096) = −5,

whereas sup|X|=1. Normalizing the fine weights does not change this ratio. Such relative phases are compatible even with a relative coupling disc: choose an action gap d=(10 log 2)/u and z=u+iπ/d; then exp(−zd)=−1/1024 and |z−u|/u=π/(10 log 2)<1/2. This toy model does not refute real-coupling N5′; it refutes positivity-based contraction as a general theorem at complex coupling. For complex tilted expectations the correction is a bound on the total variation of the backward kernel (and on partition-function denominators), not contraction with constant one. No such bound is provided here.

This failure is not cured by merely assuming holomorphy and no partition-function zeros on the whole disc. A second exact example takes q=(−3+4i)/5, fine weights (1,q/1024), K(0|0)=1/2048 and K(0|1)=1/2. Then E[X|v=0]=(1−q)/(1+q)=−2i, of magnitude 2, although sup|X|=1. Set d=(10 log 2)/u, θ=arg q=2 arctan 2, z=u−iθ/d and ρ=1/3. Exact rational bounds give θ/(10 log 2)<1/3, so this point is inside the relative disc. Everywhere on that disc |Im(z)d|≤(10/3)log 2<π; a positive two-term conditional partition function can vanish only when the relative phase is π. All conditional and full partition functions are therefore zero-free on this disc, yet contraction by one fails. The needed bound is on complex conditional amplification, not just existence of analytic expectations.


### F6 — CONFIRMED conditionally: REG's estimates and finite-time ODE; the domain/source budget must remain explicit

Attachment: SPHERE2_55.md:229–235 (`a fixed band`, `r_src`), 302–324 (`Hypothesis (H_an)`, `true for a ≤ a_0`). Claim status: PROVEN analytic implication with real coefficients on the real axis, the displayed margin, and a compatible source domain. Actual sector matching is OPEN.

Cauchy's integral formula on |z−u|=ρu gives |f^(j)(u)|≤j!M/(ρu)^j for j=1,2. Thus κ_W=1+f₁′ is at least 1/2 for u≥2M/ρ, provided the matching coefficients are real at real coupling. Holomorphy and an absolute bound alone, without that reality property, give |κ_W−1|≤1/2 rather than an ordered real inequality. The reality condition is natural for real Ward matching and should be explicit in the purely analytic lemma.

The quotient rule yields the printed bound on G′, while |B_loc|≤C_F+5M and κ_W≥1/2 yield |G|≤M_G=2(C_F+5M). Integrating |T′|≤M_G gives |T−u₀|≤M_G log 2. Continuation on a neighborhood of this compact interval yields existence and uniqueness for the full time interval. The interval is an a priori finite-time enclosure, not an invariant set for all times: the vector field need not point inward at its endpoints.

There is a genuine constant-budget qualification. Since inf b(a)=u₀−M_u, the printed margin u₀−M_G log 2≥inf b(a) reduces to **M_u≥M_G log 2**, independently of a. Merely sending u₀→∞ cannot repair an insufficient band width. Choosing M_u=M_G log 2 as the lemma subsequently does is sufficient only if (H_an) and the tilted clause were proved on that chosen domain. Likewise r_src≥2N M_u is an absolute source-radius condition; it is not made true by large u₀. If M depends on the domain/source radius, those choices must be solved together. These qualifications preserve the valid conditional repair of SEAM F4 and prevent a stale-input inference when M is an output.

The elementary profile bounds |u−u₀|≤M_u, |∇u|≤M_G/R and the traceless coefficient bound 2N M M_G|v|/(ρuR) are correct. Exact membership in the separately defined SA-K Wilson–Hölder norm is NOT-VERIFIED from the permitted excerpts; its norm definition is not reproduced here. The sup and smooth-profile estimates alone do not certify every convention for that norm, seam blocks, or off-small-field data.

### F7 — CONFIRMED as a formal tilted-matching implication: CL; integrated remainder control remains an input

Attachment: SPHERE2_55.md:326–339 (`Proposition CL`, `Exact linearity`), 240–241 (`contact clause`), and 370–374 (`must be stated in this integrated form`).

For plaquette source convention exp(Σh_p s_p), h_x(p)=−2N(ū(p)−u(x)) gives the profiled density exactly. Along one ODE time interval, |u(y)−u(x)|≤M_G log 2, so incident-cell averaging gives |h_x|≤2N M_u; this does not require a factor two beyond the total profile span. Assuming the local matched expansion is valid in that SAME tilted state, insert f₁^full(u)=u+f₁(u) and f_R(u) into the divergence terms. Discrete summation by parts, followed by the smooth-profile expansion, gives −2N(f₁^full)′v·∂u s̄ and −2N f_R′(∂_μu)v^ν S^R_μν. With v·∂log Ω=−div v/4 and T′=−B_T, these are exactly the displayed scalar and traceless coefficients. This establishes the formal local coefficient algebra.

It does not derive the uniform tilted matching hypothesis from untilted matching plus analyticity or unspecified conditional decay. The stated O(a²) insertion error also needs the claimed local discretization and remainder estimates. In particular a pointwise tail a²r⁻⁶ integrates over a≤r≤r_c with the four-dimensional radial volume factor to (1−a²/r_c²)/2, of order one; it is not an integrated vanishing contact estimate. The target's later instruction to strengthen (L-c) to an integrated clause is necessary and is part of the bankable conditional statement. The finite-lattice linearity and summation-by-parts identities are exact; the continuum Taylor remainder is an estimate, not an exact identity. Full CL in the claimed norms is NOT-VERIFIED absent this integrated/local control.

### F8 — CONFIRMED with explicit running and contact budgets; NOT-VERIFIED when those uniformities are omitted

Attachment: SPHERE2_55.md:365–386 (`The product condition`, `o(log(ℓ_0/a))`).

Put t=log(ℓ₀/a). The general sufficient condition is sup_s 𝒲_s(F,S^R)/u_min(a)→0, not a bare logarithmic condition. If u_min(a)≥c t (in particular u is comparable to t), 𝒲=o(t) suffices for the analytic O(1/u) coefficient; with the stronger O(1/u²) derivative, 𝒲=o(t²) suffices. This requires a running bound in addition to (H_an)'s mere u→∞. With only u=√t, f_R(u)=sin(log u) and 𝒲=√t=o(t), the product f_R′𝒲=cos(log u) need not vanish. The function f_R is bounded holomorphic on a fixed relative sector, so analyticity does not supply the missing running comparison.

For a weight r⁻⁴[log(ℓ₀/r)]^p, p≥0, the radial integral is exactly t^(p+1)/(p+1). Multiplying by 1/u=O(1/t) gives an available upper bound O(t^p), which does not guarantee vanishing. An upper bound that fails to tend to zero is not proof that the actual insertion fails to vanish. No necessary lower bound on the actual W1 insertion has been supplied.

The contact split also needs (a/r_c)²𝔏(a)→0 in addition to r_c→0 and a/r_c→0. Those two displayed scale conditions alone do not imply it: for 𝔏=t² and r_c=a√t the missing product is t. Choosing r_c/ℓ₀=(a/ℓ₀)^γ, 0<γ<1, repairs this for any fixed polylogarithm. The isolated “iff c_con→0” at line 371 needs a nonzero lower bound on the multiplying covariance for necessity; boundedness gives sufficiency only. None of these observations changes the correct product-smallness formulation already stated in SEAM F5.

### F9 — CONFIRMED: qualitative N5′; REFUTED: its unrestricted moving-J rate claim

Attachment: SPHERE2_55.md:457–480 (`Theorem N5′`, `one can optimise J(a)`). Claim status: PROVEN conditional qualitative implication; GAP in the optional rate assertion.

There is an even shorter proof that avoids all top-level estimates. Write k=n−J, F_i=E[F|U_i], S_i=E[𝔖|U_i]. The positive Markov tower gives exactly

Cov(F,𝔖)=Σ_{i<k} E Cov(F_i,S_i|U_{i+1}) + Cov(F_k,S_k).

The first sum is bounded by δ_F(J)Z_e^q by (D). Cauchy–Schwarz and centering S_k at its best constant bound the second by C_F(J)Z_e^q τ_*(a;J). Thus the stronger sufficient bound is

sup_s |Cov(F_s,𝔖)|/Z_e^q ≤ C_F(J)τ_*(a;J)+δ_F(J).

At fixed J, let a→0; then let J→∞. This proves the claimed qualitative conclusion without transparency weighting and without the factor J+1. The target's larger factor is valid, not an erroneous number. All hypotheses still refer to every fixed finer scale; the tower does not manufacture (T-all)_J from (T-all)_0.

The final sentence's substitution J(a)~log log(ℓ₀/a) is not justified by τ≤C(J)(a/ℓ₀)^θ and an exponential tail alone. Neither C(J), C_F(J), nor a₀(J) has any growth/uniformity control. For example let a/ℓ₀=2⁻ᵗ and C(J)=2^(2^(L^J)). At the suggested L^J of order t, C(J)(a/ℓ₀)^θ=2^(2^(L^J)−θt), which grows rather than decays; even any fixed positive proportionality in J~log t eventually fails. An arbitrarily small a₀(J) is a second obstruction to that substitution. A valid rate theorem must specify these dependencies and verify a≤a₀(J(a)). The fixed-J qualitative proof does not need them.

### F10 — NOT-VERIFIED: wild-crossing absorption and a safe κ_K range

Attachment: SPHERE2_55.md:496–513 (`Wild crossing data`, `κ_K below the seam's own crossing stiffness`), 539–543 (`Erratum E1`), 532–537 (`not an infrared problem`). Claim status: ARGUED mechanism; uniform N5-T* remains OPEN.

For a single changed crossing link in an otherwise flat configuration, the displayed counting gives at least three incident crossing plaquettes, each with weight at least (3/4)β. Hence 3·(3/4)·2Nu=(9/2)Nu is the stated lower coefficient multiplying s(Δh). This arithmetic is correct under that isolated-link comparison. The erratum correctly distinguishes the number of edges incident at a seam vertex from k_e, the number of boundary faces incident at an edge. This is not a uniform energy difference at arbitrary surrounding link fields; plaquette holonomies can already be nontrivial, and changing a link can lower their action.

Even in the favorable quadratic model the proposed comparison of endpoint options does not prove that the seam stays smooth. With energy u[A t²+B(Δ−t)²], A=(9/2)N and B=κ_K, minimization gives t/Δ=B/(A+B), not zero whenever B<A. For N=2, κ_K=1, the residual fraction is exactly 1/10. It costs less than either endpoint. This is a counterexample to the endpoint minimization argument, not to the eventual multilevel Yang–Mills transparency claim: a collective jump's coefficient can grow like ℓ/a, which could suppress that compromise. That growth, the block map's response, conditional normalization, other saddles and fluctuation/large-field weights are precisely what a uniform proof still needs.

Consequently κ_K≲(9/2)N is an order-of-magnitude design suggestion, not a proved sufficient or necessary threshold. No corrected universal numerical threshold follows from the supplied information. It must also be compatible with the lower stiffness needed by the bounded-curvature Hessian input in §2.4(β); treating the range as freely selectable does not establish that the two constraints overlap. The tower permits relocation of a real conditional-mean estimate; it supplies neither absorption nor smooth saddles for every datum. Thus “no tuning obstruction found” is defensible as a report of this search; universal “no tuning needed” is NOT-VERIFIED before the two-sided reduction and these estimates. F3 additionally defeats the claimed complete symmetry exclusion.

### F11 — CONFIRMED: the two inherited refutations, with independent witnesses

Attachment: SPHERE2_55.md:609–610 (`H17`, `H18`); CODEX_REVIEW_SEAM.md:86–98 and 122–132, locating strings `absolute-value/triangle bounds` and `paired errors`.

Paired diagonal tests do not imply all-pair invariance. On {0,1} with state δ₀, let F₁(x)=x, F₂(x)=1, g₁=id and g₂ swap the two states. Both paired errors are zero, but the error of (F₁,g₂) is one. The error persists along a constant cutoff/radius sequence. This elementary witness isolates the quantifier defect; the missing Cartesian pairs cannot be recovered by selecting a subsequence. For a countable all-pair hypothesis, enumerate (F_i,g_j), choose a_j small enough to control the first j errors at R_j, and then take the boundedness/equicontinuity subsequence. Each fixed pair is eventually controlled, which is exactly the repaired diagonal mechanism. Extension beyond the controlled observable domain is a separate assumption.

For the “iff”, let X=±1 equally, F=X, J₁=X, J₂=−X. Cov(F,J₁+J₂)=0, while |Cov(F,J₁)|+|Cov(F,J₂)|=2. Thus vanishing of the absolute upper bound is sufficient and not necessary. No special Yang–Mills input can be inferred from this example; it refutes the displayed logical equivalence. The inherited corrections are respectively “Cartesian product” and “is ensured if”.

### F12 — CONFIRMED: the ratio bounds; REFUTED: 8.07 as the rounded N=2 value

Attachment: SPHERE2_55.md:277–281 (`8.07 (N = 2)`), 597 (`H5`), 628 (`C_F/(2β_0)`); checks/s2_55_1.py:213–231 (`numbers with rational pi enclosure`). This is a small display correction, not a refutation of the advertised open interval (8.07,10.77).

Direct division, with the target's u=1/g² convention, gives

R_N = [(N²−1)/(2N)]/[11N/(24π²)] = 12π²(N²−1)/(11N²).

It increases with N, so R₂=9π²/11 and the supremum is 12π²/11. Independent exact enclosures were obtained from π=16 arctan(1/5)−4 arctan(1/239) using alternating rational series, and log 2=2Σ_{k≥0}1/[(2k+1)3^(2k+1)] with its geometric remainder bound. The arctangent identity follows because tan(4 arctan(1/5))=120/119 and tan(4 arctan(1/5)−arctan(1/239))=1 in the first quadrant. No floating-point arithmetic was used.

| Quantity | Independently certified rational decimal interval |
|---|---|
| R₂ | (8.075130, 8.075131) |
| R₃ | (9.570525, 9.570526) |
| perturbative β-span, N=2 | (0.257511, 0.257512) |
| perturbative β-span, N=3 | (0.579401, 0.579402) |
| tree β-span, N=2 | (2.079441, 2.079442) |
| tree β-span, N=3 | (5.545177, 5.545178) |

Every displayed decimal endpoint is an exact rational with denominator 10⁶. Thus the N=2 value rounds to **8.08**, not 8.07; 8.07 remains a valid lower endpoint. The two-decimal N=3 value 9.57 and the target's perturbative/tree octave comparisons are correct. For all N≥2, 8.07<R_N<10.77 follows from monotonicity and the same rational enclosure. Under the separately assumed one-loop identification, the formal Λ ratio is 2^(R_N−1); this is conditional physics, not an independently derived running coefficient.

### F13 — CONFIRMED current exact checks; NOT-VERIFIED historical pre-registration and physical coverage

Attachment: SPHERE2_55.md:648–653 (`Check provenance`); the three named check scripts and their matching criteria files; checks/s2_55_1_out_run1.txt:1–22.

All three current scripts were executed without writing any check file. Python bytecode writes were disabled. The first script's informational float calls were replaced IN MEMORY by their exact arguments; all verdict expressions were unchanged. Observed output: s2_55_1 C1–C6 PASS, X1–X6 FIRED; s2_55_1b D1 PASS, D1x FIRED; s2_55_2 G1–G4 PASS, non-vacuity True, Y1 FIRED. The whole-lattice equality was 110845769233/30661230600 on each side. The non-Markov control gave E[X|U₁]=0 and E[X|U₂]=±4/5.

The retained first-run log does show exactly C5 FAIL and X5 DID-NOT-FIRE. An additional in-memory replay removing only the real assumptions on t and λ reproduced exactly those two failures, with the other gates/controls still succeeding. Real t is necessary for tA to be anti-Hermitian, so the correction is mathematically appropriate and matches the current criteria. These observations establish the stated failure mechanism, not the historical command order or that no criterion was edited between runs. That latter provenance claim is NOT-VERIFIED without an immutable prior criteria artifact; the retained log and present comments cannot establish it.

| Gate | Could it fail? What it actually decides |
|---|---|
| C1 / X1 | Yes: the independent symbolic contraction and Hermitian-projection mutation differ. Covers generic matrices for N=2,3; the all-N proof is F1. |
| C2 / X2 | Yes: direct left/right derivatives on four exact SU(2) datasets detect the sign flip. Does not verify the original external generator definition. |
| C3 / X3 | Yes: symbolic centered differences and conformal diagonal derivatives; the nonconformal field fails the latter. It does not invalidate quadratic centered-difference exactness. |
| C4 / X4 | Yes: a nonzero torus rearrangement detects swapped endpoints. It tests a 2D periodic SU(2) example, not sphere-seam geometry. |
| C5 / X5 | Yes: nonzero quadratic coefficients distinguish the missing 1/N. Covers three SU(2) series examples; arbitrary-N and admissibility arguments are supplied in F2. |
| C6 / X6 | Arithmetic bounds on an already supplied formula. X6 is redundant with the lower-bound check, and hi<cap follows directly from the built-in factor 1−1/N². No gate tests the printed two-decimal rounding or derives the physical one-loop identification. |
| D1 / D1x | Yes: a sign flip changes the nonzero linear term. First-order sample checks are supplemented by F1's exact conjugacy identity. |
| G1 / Y1 | Yes: positive Markov examples obey the tower; the non-Markov witness fails. Only finitely many constants are tested; all constants follow from convexity, not enumeration. |
| G2 | Genuine covariance decompositions on three chains, using shared conditional-expectation helpers. F9 gives the independent general telescoping proof. |
| G3, G4 | Nonvacuous top/coarse bounds on those chains and the stated constant grid. They test finite inequalities, not the all-J/a limit, sector positivity, or a Yang–Mills input. |

A literal tautology does occur at checks/s2_55_1.py:210–211: `CF(NN) - CF(NN) * NN / NN`, asserted to vanish. It remains zero for any substituted function CF and contributes no independent evidence for the scheme coefficient. It is ancillary to the meaningful C5 gate, so it does not invalidate C5. No gate tests the missing mixed seam operator, the response-norm gap in F4, actual sector matching, complex backward-kernel bounds, wild-data absorption, or the moving-J rate. All current PASS outputs coexist with those defects.

### F14 — CONFIRMED symbol separation; CONFIRMED citation drift

Attachment: SPHERE2_55.md:98–113 (`Symbols`), 303–317 (`f_R`, `M_G`), 461–474 (`C_F(J)`), and 79 (`line 604 at read time`).

| Symbol and current source | Object checked |
|---|---|
| u, β_p — SPHERE2_55.md:98–101 | u=1/g², β_p=2Nu. No numeric comparison here uses ROTDEF's differently normalized action parameter. |
| C_F — SPHERE2_55.md:101 | Fundamental Casimir (N²−1)/(2N). |
| C_F(J) — SPHERE2_55.md:461–474 | Observable-dependent L² bound, unrelated to the Casimir. Rename to C_obs(J) in downstream use; it has no established growth bound. |
| κ_W, κ_flow, κ_K — SPHERE2_55.md:103–104 | Ward derivative, flow contraction exponent, and soft-kernel stiffness respectively. No bound on one controls another. |
| f₁ — SPHERE2_55.md:303 versus CODEX_REVIEW_SEAM.md:63 | The target uses uϑ₁; the previous review used u(1+ϑ₁). Hence κ_W is 1+f₁′ in the target and f₁′ in the previous review. Both are consistent when kept distinct. |
| M, M_G, M_u, r_src — SPHERE2_55.md:229–235, 303–317 | Uniform analytic envelope; slope bound; absolute coupling-band radius; source-polydisc radius. Their compatibility, not u₀ alone, closes the domain budget. |
| λ and λ_seam — SPHERE2_55.md:110–111, 418 | Arbitrary real scheme parameter versus positive dimensionless gluing strength. |
| h_i and J — SPHERE2_55.md:107–108, 457–480 | Chart spacing aL^i and number of removed top levels. Limits in N5′ are at fixed J first. |

Current PROOF.md:604 says `are marked **[S9]**...`; `Decision 4 is MADE` is now at **605**. The target's historical numerical locator is stale by one line. Its historical [S26-BANKED] interval 5–48 also ends before the current sphere bullet at **49**. The string locators recover both objects. This establishes present drift, not that the author misreported an earlier read time. The kernel interval was located independently at PROOF.md:2285 (`with κ_- ≤ κ_i ≤ κ_+`); it supplies no checked numerical upper bound compatible with the suggested seam threshold.

## Summary table

The pre-stated review above is now complete. No claim of a completed constructive Yang–Mills proof is made. Source target: the 707-line SPHERE2_55.md read in this review; the numbered locations are supplemented by locating strings because other lane files are moving.

| Finding | Review verdict | Claim status / disposition |
|---|---|---|
| F1: measure term | CONFIRMED | PROVEN for the displayed generator and bulk plaquette geometry; retain cutoff qualification. |
| F2: matching algebra, scheme shift, circularity | CONFIRMED | PROVEN algebra and leading shift; actual quantum matching CONDITIONAL/OPEN. |
| F3: exhaustive two-sided seam classification | REFUTED | GAP: allowed parity-even J·F_n operator of dimension three omitted. Single-connection count survives. |
| F4: plain-insertion corollary | REFUTED | GAP: small coefficient errors need response control. Strong weighted version remains CONDITIONAL. |
| F5: tower lemma / sector export | CONFIRMED / REFUTED | PROVEN for positive Markov measures; GAP in the unqualified complex-sector export. |
| F6: REG | CONFIRMED / NOT-VERIFIED | PROVEN conditional analytic/ODE estimates; retain reality, band and source budgets. Exact external SA-K norm membership not verified. |
| F7: CL | CONFIRMED / NOT-VERIFIED | PROVEN coefficient algebra under tilted local matching; integrated contact/discretization estimates remain inputs. |
| F8: W1 | CONFIRMED / NOT-VERIFIED | CONDITIONAL logarithmic budget with u≥c log(ℓ₀/a), appropriate contact radius and uniform path control. |
| F9: N5′ / moving-J rate | CONFIRMED / REFUTED | PROVEN qualitative implication; GAP in claimed rate without J-dependent controls. |
| F10: wild data and kernel threshold | NOT-VERIFIED | ARGUED mechanism; uniform absorption and compatible stiffness interval OPEN. |
| F11: inherited H17/H18 | CONFIRMED | PROVEN counterexamples to paired invariance and necessity of absolute bounds. |
| F12: arithmetic | CONFIRMED / REFUTED | PROVEN ratio/span bounds; N=2 two-decimal display is 8.08. |
| F13: checks and history | CONFIRMED / NOT-VERIFIED | Current exact replays and complex-symbol failure mechanism reproduced; historical unchanged-criteria order not established. |
| F14: notation/citations | CONFIRMED | Distinct constants tracked; current line drift documented. |

Numerical and discrete corrections: the rounded N=2 factor is 8.08, with exact value 9π²/11 in (8.075130,8.075131); “zero allowed dimension-3 two-sided operators” becomes “at least the mixed J·F_n operator”; complex mean contraction with constant one fails, giving magnitude 2 even on a zero-free disc (and magnitude 5 in the signed example); current Decision-4 locator 604 becomes 605, and the sphere banked bullet is at 49, beyond the historical 5–48 range. The (9/2)N isolated-link arithmetic is not refuted; its use as a universal stiffness threshold is NOT-VERIFIED. Replacing N5′'s J+1 prefactor by 1 is a proved strengthening, not correction of a false bound.

**Single most dangerous unverified item in this target:** uniform N5-T* for arbitrary coarse crossing data, after a controlled elimination of the two-sided seam fields. The allowed mixed dimension-3 operator, finite-kernel compromise, and missing uniform saddle/fluctuation estimates all meet at that step. Positive gluing stiffness and the tower identity alone do not establish it.

Not banked: actual LCS-a; plain-insertion scheme independence; full sector transfer by contraction; a universal no-tuning theorem; a safe numerical κ_K interval; an N5′ rate; the full SA-K coefficient-class inclusion or full CL remainder norm from the stated excerpts; any full OS-algebra bridge, mass gap, or unconditional constructive Yang–Mills result.

## Exactly what may be banked

1. **PROVEN:** Proposition M for the generator reproduced in §1.1, including its all-configuration Casimir coefficient, exact right/left agreement, quadratic centered-difference identity and zero bulk rotational divergence. Keep the nonquadratic cutoff/seam qualification.
2. **PROVEN algebra / CONDITIONAL matching:** B_loc=C_F+u(ϑ_D^p−4ϑ_1^p), κ_W=1+(uϑ_1^p)′, and scalar cancellation for the corresponding Ward profile, once the matched expansion holds. Combining trace and vector matching into one clause does not prove that clause.
3. **PROVEN:** the local scheme family's leading coefficient C_F−λ/N and its range over all real numbers. A classical-background computation plus coupling analyticity alone supplies no quantum matching coefficient. The profile derivative by itself cannot identify the independent Ward response.
4. **CONDITIONAL:** scheme-profile agreement under the stronger uniform weighted nonvacuity/response hypothesis and the stated two-scheme Ward inputs. The narrowed plain-insertion version is excluded from this item. Under an additionally supplied one-loop limit, the corrected ratio and octave arithmetic of F12 apply.
5. **PROVEN analytic implication / CONDITIONAL application:** REG's Cauchy estimates, κ_W≥1/2 for real coefficients at u≥2M/ρ, bounded slope and finite-time ODE continuation on a compatible band/source domain, and the resulting O(g²) traceless coefficient. The formal CL coefficient algebra may be used with actual tilted local matching and integrated contact/remainder estimates as named inputs.
6. **PROVEN sufficient-condition bookkeeping:** vanishing of the normalized coefficient–insertion bounds uniformly along paths is sufficient. W=o(log) is sufficient when u≥c log; W=o(log²) is sufficient with the stronger derivative order and the same running comparison. Small coefficients alone do not establish these products' vanishing; absolute bounds are sufficient, not necessary.
7. **PROVEN:** the conditional-mean tower contractions for one positive probability Markov chain, and the qualitative N5′ implication from (T-all)_J, (E′_J), and (D) at every fixed J. The direct-cut bound is C_obs(J)τ_*(a;J)+δ_F(J), with a→0 before J→∞. No complex-measure contraction or moving-J rate is included.
8. **PROVEN in the specified local classes:** the single-connection curvature count and reflection exclusions; dimension four is irrelevant on a three-dimensional seam; a two-sided dimension-two gluing operator and the parity-even dimension-three mixed operator are allowed. Tree-level stiffness growth is a mechanism, not an all-coarse-field transparency theorem.
9. **PROVEN logical repairs:** Cartesian-product diagonal testing and replacement of the inherited absolute-bound “iff” by a sufficient condition. Their extension to a full OS observable algebra remains a separate obligation.
