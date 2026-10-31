# PRE-STATED

Independent hostile review of `NODEA55.md`, requested 2026-10-28. This section is recorded before the substantive proof review. All paths below are relative to `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/` unless stated otherwise. No git operations; this report is the only authorized write. Source content is inspected through targeted searches and `sed` ranges. This is a local-source mathematical review, not a landed audit or a claim of current-main provenance.

Verdicts: **CONFIRMED** means the precisely stated claim follows from the checked premises; **REFUTED** requires an explicit counterexample, contradiction, or invalid claimed inference; **NOT-VERIFIED** records a missing hypothesis or incomplete argument without claiming the conclusion false. Each substantive verdict will identify its file and locating string. Literature recollections, if any, will be marked `[m]`; checked external statements will be identified separately. Numerical checks use integers, rational arithmetic, or exact symbolic expressions only.

Attack order and acceptance criteria:

1. **F-UNIV:** build admissible boundary data at `k = 1`, identify what conditioning actually fixes, prove a positive lower bound on column energy for every compatible interior, and compare the normalized conditional moment with the claimed uniform right-hand side. Distinguish direct moment refutations from the additional defect/probability implications.
2. **LT and spectators:** check both normalization and energy domination, including compactness, positivity, cutoff constraints, the small-field denominator, exact support, repeated factors, lowest scales, and every named consumer (`CRC-2T′` step (5), `CRC-HW`, and `Φ_{−1}`). A fixed-volume polynomial bound cannot establish a volume-uniform column bound.
3. **E2-RED^H:** check the two Hölder exponents, all rate and sign restrictions, the defect-pricing law, geometric charging, and whether each input accepts the actual spectator and target sets.
4. **Route (4°):** independently derive the relaxed-pair count and shadow inflation, inspect `na55_geo` G1–G5, and trace every induction and edge case. Separate the `Y = ∅` positive-level reduction from any remaining level-zero input.
5. **Gaussian residual:** identify the actual weight, its marginal, symmetry and convex superlevel sets; verify precisely which Anderson/Prékopa–Leindler statement applies, Gaussian nondegeneracy, the determinant/rank bound, and the claimed decoupling constant `1`.
6. **Cutoff uniformity:** track dependence on `n_♯` through laws, spectators, constants and induction; check input `c_U` versus output `2ε_2` and any circular choice of constants.
7. **Prior refutations:** locate and independently adjudicate each of the nine claims that NODEA55 calls refuted, distinguishing false statements from insufficient proofs and identifying any surviving repair.

An obstruction will be banked only on its proved quantified domain; failure of a universal conditioning assertion will not be promoted to failure of the restricted unconditional route, the Gaussian model, or Yang–Mills construction generally. Final disposition will state exactly what may be banked and what remains open.

## Review disposition

**NODEA55 is not confirmed wholesale.** The universal-conditioning obstruction, the restricted fixed-volume Laplace test, the fixed-neighbourhood relaxation, and the explicitly Gaussian convex-core theorem contain bankable mathematics. The Hölder statement needs a missing set restriction and strict rate bounds. The claimed nine refutations include two misclassified corrections and a domain mismatch for B3. None of the actual-chain, volume-uniform moment obligations is discharged.

Review scope correction after reading F-UNIV: the pre-stated phrase “every compatible interior” is too strong for its probabilistic conclusion. Flat interiors remain compatible with the boundary. What is required, and checked below, is a strict action gap followed by conditional concentration. No claim of deterministic incompatibility is banked.

## 1. F-UNIV and its probability corollary

**CONFIRMED — the universal-F moment bounds fail already at k = 1.** Sources: `NODEA55.md`, “Proposition F-UNIV”, steps (i)–(v); `HW.md`, “For k = 0, F^col_A(U_0)”; `PLD.md`, “(CEM^{COL})_k [node A”, “(ACT′)_k”, “(BCH-1)_k”. Here is an independent exact version of the action-gap calculation.

Take a torus large enough to contain the indicated collar without wrapping, and the block B = [0,8]^4. Fix the outside-outside collar links near the uniform abelian field C of NODEA55. Initially take the exact boundary values and 0 < b ≤ 1/100. There are 81 planar slices, each containing 100 affected (1,2)-plaquettes, 64 inside B and 36 in its annulus. Direct vertex enumeration independently gives totals 8100 and 5184. Every boundary-loop link is outside-outside, so the conditioning is in the permitted sigma-field.

The loop holonomy in each slice is exp(100ibσ_3). Since sin(50b) ≥ (9/10)50b,

    sum over all slices of ||1 − hol(loop)|| ≥ 7290b.

Suppose the whole column energy E = F^col_Q is at most b². The total norm contributed by the 5184 inner (1,2)-plaquettes is at most sqrt(10368E) ≤ 810b. The lasso product inequality therefore forces the annular norm sum to be at least 6480b. Using s(V) = ||1−V||²/2 and 2916 annular plaquettes gives

    action of any such completion ≥ 6480²/(2·2916) · b² = 7200b².
    action of the uniform completion C ≤ 8100·b²/2 = 4050b².

Thus the gap is at least 3150b². This proves more than the flat-interior comparison needed for compactness. Continuity preserves a positive gap for a sufficiently small positive-radius boundary neighbourhood and for a positive-volume neighbourhood of C. Conditional Laplace comparison gives

    Pr(E ≤ b² | boundary neighbourhood) ≤ C exp(−c u_0),
    E[exp(θY^f_Q) | boundary neighbourhood]
        ≥ (1 − C exp(−c u_0)) exp(24θu_1b²).

All constants here are independent of g. The fully relaxed pattern, empty history, F_< = 1, and w = 1 already give an admissible counterexample for every cutoff; its boundary neighbourhood has positive measure. A fixed shadow allowance cannot absorb the divergence.

For the local constrained generators, the additional justification is monotonicity, not the assertion that b < ε_1 makes every minimizer defect-free. Choose b small enough that the uniform competitor and its neighbourhood have no affected level-0 defects. At any outside configuration having an admissible completion, deleting those variable defects preserves the component-size constraint, including fixed declarations. The competitor neighbourhood is therefore allowed. Lemma BUF makes the future weight independent of the free links. The same conditional denominator comparison works without proving anything about the defects of all minimizers.

**NOT-VERIFIED as written — A.4(v)'s step from an unspecified O(b) to defect-free minimizers merely by taking b < ε_1.** Source locating strings: “the minimisers' plaquettes are ≤ O(b)” and “take 0 < b < ε_1”. The missing constant prevents that inference. This is a proof gap, not a counterexample to the minimizer property: the competitor argument above avoids it, and the stronger minimizer argument below proves the needed small-b case. The summary's “every law and every F_<” must retain the stated read-set and generator hypotheses; the k = 1 original class itself forces F_< = 1.

**CONFIRMED — the obstruction propagates to ACT′, LCR^act′, and EQ-bc plus BCH-1 with universal F.** At k = 1, the minimized column action is u_0E. Its conditional mean on the boundary event grows at least as u_0b²(1−o(1)), and its positive exponential moments diverge. Already at λ = 0, EQ-bc forces the boundary charge to exceed this mean minus B_0, so BCH-1 cannot have a fixed B_1 under all F. This uses neither PLD's disputed factorization of the constrained conditional law nor its claim that CEM-2 has disappeared.

**NOT-VERIFIED — NODEA55's written deduction of F-UNIV′ from positive column energy and PLD's linear-order value 9b.** Sources: `NODEA55.md`, “Corollary F-UNIV′”, and `PLD.md`, “The curvature (lasso) form, computed”. Positive total curvature does not imply a particular coarse centre exceeds ε_1, and the conditional minimizers have not been identified in that deduction. Linearization at a prescribed uniform field does not identify the field selected by boundary conditioning.

**CONFIRMED — the k = 1 F-conditioned NA-PRICE^{E+} conclusion is nevertheless false, by the following additional argument.** This argument is supplied by this review, rather than attributed to NODEA55's proof. Work with the fully relaxed generator. For sufficiently small b, the uniform completion actually minimizes the conditional Wilson action. Indeed its action is below 1. Every minimizing plaquette therefore has principal SU(2) angle α < π/2. In each planar slice, the bi-invariant angular triangle inequality gives Σα ≥ 100b. Convexity of 1−cos α on [0,π/2] gives

    Σ_slice (1−cos α) ≥ 100(1−cos b).

The uniform completion attains equality in all 81 slices, with every other affected plaquette trivial. Equality forces equal angles and aligned transported plaquette holonomies: equality in the SU(2) geodesic triangle inequality follows the unique short geodesic. Planar lasso reconstruction, together with trivial plaquettes in the other orientations, identifies its interior gauge orbit with the uniform field. This is also a direct way to supply the minimizer step missing from F-UNIV′.

For that field the centre curvature is **exactly** 9b, not merely its derivative at zero: `HIST.md`, “Proposition CF (constant-curvature chain” and “the reflection x_2”, prove that paired S4′ contours give a positive real multiple of the straight transporter. The axial field used here is gauge-equivalent to CF's symmetric gauge. Take b = ε_1/2 for the recorded small threshold; for example 0 < ε_1 ≤ 1/100 suffices. Then

    2 sin(9b/2) ≥ 9b − (9b)³/24 > ε_1.

All exact-boundary minimizers therefore have a strict coarse-defect margin. Compactness preserves the margin near the minimum for sufficiently close boundary data. Conditional Wilson concentration, followed by concentration of the finitely many nondegenerate SU(2) kernels around their centres, gives Pr(Q ∈ D_1 | boundary neighbourhood) → 1. This contradicts C_A exp(−a_Au_1) for a_A > 0. Neither a fixed shadow factor nor the size of the conditioning event changes the conclusion.

**NOT-VERIFIED — this k = 1 example refutes REVIEW_PLD_S5 B3 on B3's original domain.** Sources: `REVIEW_PLD_S5.md`, “Binding fix B3” / “B3 (statement)”; `PLD.md`, “Theorem NA-PRICE^E (i)” in §17.4, explicitly **k ≥ 2** and condition (C_S). NA-PRICE^{E+}'s later k ≥ 1 formulation is refuted above. A k = 1 counterexample is not a counterexample to the original k ≥ 2 formulation with its different set/law class. NODEA55 supplies no matching-domain construction for that separate assertion.

## 2. Lemma LT, spectators, and actual consumers

**CONFIRMED — Lemma LT(a) as a fixed-volume polynomial upper bound, uniform in the cutoff.** Sources: `NODEA55.md`, “Lemma LT”, steps (1)–(7); `HW.md`, “Lemma TILT (exact)”, “Lemma DJ”, and “R_{S,E}”; `HIST.md`, “(A1)” / “(A2)”. With fixed finite K and torus, disjoint column terms and DOM′ give

    Z_A F_< ≤ exp(λ_f A),     F_< ≥ 1.

For SU(2), φ_M(V) = r(1−cos α), 0 ≤ r ≤ 1. A Haar ball of angular radius (κu_m)^(−1/2) supplies the stated polynomial lower bound on each kernel normalizer, also when r = 0. Hence the numerator is at most C u_max^(3N_links/2). A ball about the identity of radius c u_max^(−1/2) has A ≤ 1, no defects at any level, and volume at least c′u_max^(−D/2). It lies in every R_n and satisfies the buffer-good condition. This gives a polynomial after rounding the total exponent upward to an integer.

Only smoothness near the identity is needed for that ball; global analyticity of the polar-part energy, asserted in LT, is unnecessary and should not be assumed at singular centres. The zero-energy flat chain is indeed defect-free. The estimate is independent of the cutoff and of the chosen spectator subproduct, but its degree and constants depend on the finite lattice and K. **It does not prove CEM°, W0, or an O(1) moment as g → 0.** Sources for the overreach to avoid: `NODEA55.md`, C.4 “(M1) = (CEM-1^free)” and the lead summary “both … hold at fixed volume”. LT only supplies its displayed polynomial estimate.

**CONFIRMED — LT(b)'s existential exponential obstruction for universal F_<, at k = 2.** Use the fully relaxed pattern, empty history and an indicator fixing U_0 near a sufficiently small uniform-curvature configuration on the relevant column. This is an allowed arbitrary U_{<1} spectator in the original class. The U_1 links concentrate around the nonflat centres, whose curvature is exactly 9b by HIST's CF argument. Compactness and the zero-energy characterization of F^col imply a strictly positive column-energy minimum on a sufficiently small neighbourhood of those centres. The resulting moment grows as exp(cu_2). This avoids LT(b)'s unproved assertion that an arbitrary constrained conditional kernel law gives the same concentration. It proves existence, which is all the universal-quantifier refutation needs.

**CONFIRMED — the named HW consumers use the restricted spectator class.** Locators: `NODEA55.md`, A.1 “Definition (𝔖^cap” and A.2; `HW.md`, “Lemma TEL-f”, §30.4 “(5) *Price the animal”, §30.5 “μ^{(k)}”, and §36 “[RHW5-fix NIT, item 4.]”.

| Consumer | Actual input and check |
|---|---|
| CRC-2T′ step (5) | The spectator subproduct is unchanged by every pattern relaxation. It reads levels at most m−1, the condition actually needed by the level-m mismatch peel. No factor is squared or duplicated. |
| CRC-HW at k ≥ 1 | Π_{k′<k}Φ_{k′} consists of history cubes at levels 0 through k. It is exactly a member of 𝔖^cap_𝔥(k). |
| CRC-HW at k = 0 | F_< = Φ_{−1}, which reads U_0. This violates the old U_{<k_0} wording at k_0 = 0, but satisfies the actual peel requirement because m ≥ 1. TILT permits a bounded function of the fields retained in the past law. |
| TEL-f at k = −1 | No spectator; the observable is Φ_{−1} itself. Its required moment remains a separate bottom-level input. |
| CRC, K8, single-cube application | F_< = 1, as expressly recorded in HW §36. |

P-lo, P-hi and the needed disjointness follow from (A2), ancestry, and DJ, without the component-size clause (A1). At the lowest levels, replace the repeated shorthand “reads levels ≤ k_0−1” by **“reads levels ≤ max{0,k_0−1}”**. At j = k_0 = 1, both Φ_{−1} and Φ_0 read U_0; B.1's assertion that only Φ_{j−1} does is literally incomplete. P-dis/ancestry excludes both from a far target, so this does not obstruct the consumer repair.

## 3. E2-RED^H

**CONFIRMED — Hölder repairs the conditioning step on the actual far-Y consumer domain, with strict rates. NOT-VERIFIED — the universally quantified E2^𝔉′_res implication as presently written.** Sources: `NODEA55.md`, “Corollary E2-RED^H”, step (4), and “Corrected … allowance bookkeeping”; `PLD.md`, “Proposition FAR”; `HW.md`, §30.4 step (4).

The missing set hypothesis is consequential. Step (4) needs S = Y ⊔ x(Γ_1) to avoid A_j(𝔥). Its justification invokes **non-R-free** cubes, whereas E2^𝔉′_res only asks Y to be outside col Γ with N_1(col Γ ∪ Y) R-free. Choose a nonempty history at level j, Γ = ∅, Y containing one of its cubes, and relax all constraints. The printed E2 hypotheses hold, but S ∩ A_j(𝔥) ≠ ∅. Thus the claimed set inference is **REFUTED**. This does not prove the final E2 inequality false; it proves the supplied NA-PRICE^{E+}_res application is outside its hypotheses.

Repair: require **Y ∩ A_j(𝔥) = ∅**, or explicitly quantify only the sets non-free before the specified relaxation. Both actual HW callers supply this: their Y consists of non-free cubes for the earlier pattern; every cube in A_j(𝔥) has unconstrained ancestors already. The children of Γ also avoid A_j by ancestry/(A2). The j = k_0 case is then covered after including the Φ_{−1} exception identified above.

The exact rate calculation, writing r = 1+2Rg_0², is

    1/p + 1/q = 1,
    24pθr < 1,     qθ/6 ≤ θ′ < 1/(24r),
    λκε_1²/256 ≥ qθa_bad.

Balancing the first two constraints gives p = 7/6, q = 7 and

    θ < 1/(28r).

**REFUTED as an admissible endpoint — “θ ≤ 1/28”.** Even at r = 1, θ = 1/28 forces 24pθ = 1 and θ′ ≥ 1/24, violating strict integrability. At positive Rg_0² the upper supremum is smaller still. Taking a strict margin and, for instance, θ′ = pθ supplies the intended repair. The limiting mismatch condition at r = 1, λ = 1/2 and a_bad = ε_1²/1797760 is κ ≥ 1/14045; this exact arithmetic agrees with the file.

The appended allowance constants can be justified without inflating the printed C_fc^H. Here c_A is a common upper bound for the two input allowance constants. Let P = col Γ ∪ Y and S = Y ⊔ x(Γ_1). Since |P|−|S| = 81|Γ|−|Γ_1| and every higher shadow is monotone,

    |S| + ||S||_sh ≤ ||P||_sh + |Y|,
    ||col S||_sh ≤ 81(||P||_sh + |Y|).

Consequently the valid constants are

    c_A^H = c_A/p + 81c_A/q,
    C_A^H = (C_A exp(81c_A))^(1/q),
    C_fc^H = c_cem(pθ)^(1/p) + 81 C_A^(1/q) exp(θa_bad R).

The unused base-layer cubes of P absorb the Γ_1 charge; the extra per-cube exponential is needed only for Y. This supplies a detail absent from the appended bookkeeping and resolves the initial concern about C_fc^H.

One interface clarification is still necessary: when the moment rate is pθ or θ′, its law must retain spectators at the **original history rate θ**. A statement in which changing the rate also changes 𝔖^cap to the new rate does not automatically cover that law. State the two rates independently, or admit spectator exponents up to the moment rate. No monotonicity of normalized expectations in spectator strength has been proved.

Finally, removing F′ ≤ 1 before the moment in NA-PRICE^{E+}_res is valid. Its final normalized expectation is E_{ν′}[1] = 1. This avoids the erroneous general comparison E_{ν′}[F] ≤ E_ν[F] in `PLD.md`, §18.7.1 “(5) *Assemble*”: inclusion of unnormalized constraint indicators alone does not order normalized expectations.

## 4. Route (4°), geometry, and what node A still owes

**CONFIRMED — the geometric cost and the conditional CRC-2T° argument.** Sources: `NODEA55.md`, B.2 “(3°) Relax”, “(4°) The count”, and “(5°) Price”; `HW.md`, “Corollary H-geo′”, “Lemma COL′”, and §36 “induction on the finite integer N(R)”. The geometry can be proved without the random samples:

    π(N_8(col D)) = N_3(D),
    π(N_3 X) ⊂ N_1(πX),
    π(N_1 X) ⊂ N_1(πX).

For the first identity in one coordinate, the child interval [3q,3q+2] thickens to [3q−8,3q+10], whose projected interval is [q−3,q+3]. Products and unions give the general identity. The other containments follow from the integer floor bound. The first relaxed level therefore has at most 7^4 n cubes; each later level is contained in the corresponding shadow of D. With M = K−1−m,

    |Col(N_8(col D))| ≤ 2401n + Σ_{s=1}^M |Σ^s D|
                       = 2400n + ||D||_sh
                       ≤ 12401n + 10000M.

This includes M = 0. Projection on a compatible torus can only identify elements in these image counts; the inequalities persist. The closed column [D] is contained in this relaxed set. An arbitrary, possibly disconnected history set still obeys the first bound with its own shadow norm; only the last animal bound uses connectedness.

The induction is noncircular: the relevant law is R_{t−1}, with N(R_{t−1}) < N(R); the fixed relaxation is upward closed and starts at level m ≥ k_0+1. The source has a harmless membership slip: “D ⊂ S^{(m)}_{R_{t−1}}” is false because x_t is not yet constrained. The correct inclusion is **D ⊂ S^{(m)}_{R_t} ⊂ S^{(m)}(𝔥)**, which gives exactly the required Γ-clause.

At the relaxed pattern the mismatch peel applies, including m = 1 and F_< = Φ_{−1}. The remaining expectation is precisely the Y = ∅, empty-buffer moment. The counts give, exactly,

    b_n° = 12401c_U + 810162c_A,
    b_D° = 10000c_U + 810000c_A,

because 81·10002 = 810162 and 81·10000 = 810000. The factor exp(b_D°M) is controlled by the stated (T°), and the finite telescoping product closes using (S2°). The factor 2 per animal from the former Y-sum is absent. The implication still assumes (CLS-min) for HW's bad-window estimate and assumes the moment; it proves neither input.

**CONFIRMED — Corollary CRC-HW° with a separate bottom-level moment and common constants.** Sources: `NODEA55.md`, “Corollary CRC-HW°”, B.3 “(W0)_λ”; `HW.md`, “Lemma TEL-f”. For k ≥ 0, past constraints are unchanged by Col(N_8(col U_{k+1})), so the displayed partition-function ratio is exact. The bounds

    |C_k°| ≤ 2400|U_{k+1}| + ||U_{k+1}||_sh,
    ||col U_{k+1}||_sh ≤ 81(|U_{k+1}| + ||U_{k+1}||_sh)

give the stated allowance. At k = −1 use Col(N_8(U_0)), CRC at k_0 = 0 with no spectator, and the **separate Wilson-window moment**. The looser bound |C_{−1}°| ≤ 2401|U_0| + ||U_0||_sh suffices. Taking C_fc and c_A large enough for both the positive-level and bottom-level inputs gives

    C_fc′ = C_fc exp(2401c_U + 81c_A),
    c_f° = c_U + 81c_A.

**CONFIRMED with that qualification — “node A owes only Y = ∅”.** It means CEM°_k for k ≥ 1 **and W0**. The notation “j ≥ k_0 (j = −1: the level-0 window)” does not literally include j = −1 when k_0 ≥ 0; the separate clause must be retained. W0 covers two region types: 3^4-site cube interiors and 9^4-site level-1 regions, at the appropriate rates. Their packaging as one uniformly quantified statement is valid; a theorem about only the first region type has not automatically proved the second. No level-0 defect probability is consumed on route (4°).

On the original Y-route, both bottom consumers really need defect factors: the Wilson-window consumer needs (0a⁺), and the level-1-column consumer needs (0b). This checks B.3's consumer analysis, without promoting “no route exists” to an impossibility theorem.

**CONFIRMED — G1–G5's intended geometric statements, with the proof/evidence distinction preserved.** Sources: `checks/na55_geo.py`, “G1”, “G3 + G4”, and “def one_d_sizes”; `NODEA55.md`, “Lemma PD”. G2–G5's random samples are not exhaustive proofs. The coordinate arguments above prove G1–G4. For G5,

    ||x(S)||_sh ≤ |S| + 81|S| + 16(||S||_sh−|S|)
                = 16||S||_sh + 66|S|.

The factor 16 follows because, after the first step, every shadow is N_1-thickened and its extra N_1 thickening is covered by 2^4 translates. This proves the bound for arbitrary sets, not just sampled animals.

The existing scripts were inspected, not re-run as independent evidence: they contain decimal diagnostics, while this review uses only exact checks. A separate in-memory Python check performed 183 residue cases, 25 full-child interval checks, direct boundary-plaquette enumeration, exact integer/rational coefficient checks, and independent one-dimensional shadow recurrences. The one-cube G3 equality is 2482 = 2401+81. At D = 20000 the recurrence gives

    ||S||_sh = 1620001,
    ||x(S)||_sh = 5120082,
    excess = 3500081 > 3073362,
    16||S||_sh + 66 − ||x(S)||_sh = 20800000.

These are actual results of this review's command, not copied PASS labels. No script or log file was written.

## 5. The Gaussian-model residual and Anderson's hypotheses

**CONFIRMED — Proposition GAUSS for exactly its stated Gaussian, uncapped-spectator, convex-core model.** Source: `NODEA55.md`, C.2 “Proposition GAUSS”, steps (1)–(5). The positive-definite quotient, invariance of the observables under its removed null directions, PSD quadratic forms, disjoint column term sets, and the domination 2Q_Q ≤ λ_f M_Q are explicit model assumptions. This is not a proof that the nonlinear chain has those properties.

The hypotheses used in the Anderson step are met:

| Object | Property actually used |
|---|---|
| Spectator-tilted Gaussian density | M_s = M−2ΣQ_s > 0, so its density is even and log-concave; its superlevel sets are centered ellipsoids. |
| Constraint core K | An intersection of origin-symmetric convex slabs, or norm cylinders for vector-valued linear curvature. It is convex, symmetric, measurable, and has positive Gaussian probability. |
| Future core likelihood | Given the past, the future Gaussian has a linear mean and a covariance independent of the past. Integrating its density times the joint convex-core indicator therefore gives an even log-concave function of the past. |
| Past and buffer cores | Symmetric convex indicators. Their product with that likelihood is again even and log-concave. |

The marginalization theorem was checked in the primary source: [Prékopa, *On logarithmic concave measures and functions* (1973), Theorem 6, printed p. 342](https://acta.bibl.u-szeged.hu/14411/1/math_034_335-343.pdf). NODEA55's translated-integral proof then establishes the needed Anderson inequality directly; no literature recollection is being used in place of its hypotheses.

In particular, disjointness gives M_s ≥ M_A and thus 2Q_A ≤ λ_f M_s, not merely a bound with a second factor (1−λ_f) in its denominator. With Σ = M_s^(−1) and Σ′ = (M_s−2Q_A)^(−1),

    E_Σ[exp(xᵀQ_Ax) | K]
       = det(I−2Σ^(1/2)Q_AΣ^(1/2))^(−1/2) · Pr_{Σ′}(K)/Pr_Σ(K).

PSD inverse order gives Σ′−Σ ≥ 0. The translated integral of the even log-concave density over K is even and log-concave in the displacement parameter, hence maximized at zero. Adding an independent centered Gaussian with covariance Σ′−Σ therefore reduces the probability of K. The determinant has at most rank(Q_A) nontrivial eigenvalues, all at most λ_f. Independently counting internal links gives

    4·8·9³ = 23328,
    rank(Q_A) ≤ 3·23328|A| = 69984|A|,
    c_cem = (1−λ_f)^(−34992),    c_2 = 1.

Here c_2 = 1 is an admissible, class-optimal constant (the unconstrained K = R^D gives equality), not an assertion of equality for every constraint. It belongs to **CEM-2^all**, with the past constraints on the K side; this proof does not establish constant 1 for PLD's different comparison using an already past-constrained reference law. For a constant uniform in g ≤ g_0, freeze λ_f at an upper bound λ_bar = 24θ(1+2Rg_0²) < 1; do not call a g-dependent expression a fixed constant.

**REFUTED — C.2(iv)'s explanatory claim that “every factor the law carries” is quasi-concave and that the bound “fails as soon as a factor is not”.** Uncapped spectators exp(q_s) with q_s positive quadratic are not quasi-concave; they were absorbed into the Gaussian precision. Symmetry and convexity are sufficient for the displayed Anderson argument, not necessary for every valid bound. For independent centered Gaussian coordinates x,y, a target exp(x²/4) is independent of the nonsymmetric constraint 1 ≤ y ≤ 2, so c_2 = 1 still holds. This exact counterexample refutes the asserted necessity without affecting Proposition GAUSS.

**NOT-VERIFIED — extension of this c_2 result to the actual cutoff constraint, capped spectators, or general log-concave perturbations.** Locators: `NODEA55.md`, C.2(v) “The cutoff allowance”, C.4 “For Gaussian and for log-concave perturbations”. For two adjacent scalar defect coordinates at threshold 1, the n = 1 permitted set contains (4,0) and (0,4), but not their midpoint (2,2). Its indicator is symmetric but not quasi-concave. Also, a general quadratic tilt of a non-Gaussian log-concave law is not represented by adding independent Gaussian noise; Anderson's translation inequality alone supplies no such comparison. The theorem explicitly replaced capped spectators by uncapped ones. Those replacements must remain visible in every downstream citation.

**CONFIRMED — C.1's product decomposition as a sufficient reduction. NOT-VERIFIED — actual-chain M1/M2.** Locators: “The weight, removed exactly (TILT)” and “What is missing, precisely”. TILT and normalization prove CEM° from CEM-1^free and CEM-2^all. They do not prove either estimate. C.4's moment of exp(λ_f a^col_A) is a sufficient strengthening of CEM-1^free's moment of Z_A, rather than literally the same statement. The model theorem and LT cannot be cited as a volume-uniform, all-cutoff proof of these actual-chain inputs.

## 6. Cutoff uniformity and the c_U choice

**CONFIRMED — the bookkeeping diagnosis, conditional on obtaining the uniform moment inputs.** Sources: `NODEA55.md`, Part D; `SMALLNESS_DAG.md`, “3.1 The n_♯ loop”; `HW.md`, §30.6 “Order of constants” and §24.1 “B_0 := c_f + 2”. The geometry, kernel peel, local read-set identities, SPEC, and LT introduce no cutoff-dependent constants. The actual moment constants are only **required** to be independent of n_♯; they remain open. Excluding arbitrary F_< prevents a cutoff-selected adversarial indicator, but does not by itself prove uniformity of the remaining constrained measures.

The Gaussian convex-core proof covers n = 0. Removing all constraints covers a cutoff at least as large as every possible defect component. It does not cover all intermediate n. A fixed-volume polynomial uniform over n is also insufficient for the volume-uniform hierarchy.

The sound selection order is

    cutoff-uniform C_fc,c_A → fixed c_U^in ∈ (0,1]
      → c_f° = c_U^in + 81c_A, B_0, b_n°, b_D°
      → n_♯ satisfying both lower bounds
      → g_0 making (S2°) and the other smallness conditions hold.

Then c_U^out = 2ε_2° ≤ c_U^in is a conclusion. **CONFIRMED — use the input bound when choosing c_f and hence n_H.** A sharper output value may be reported afterwards, or bounded by the fixed input throughout; it cannot be fed back into its own prerequisite choice without a new argument. Thus “must use input” concerns the ordering and the uniform certificate, not a prohibition on subsequently using a smaller proved estimate.

## 7. The nine advertised refutations, individually adjudicated

The verdict below evaluates the **refutation claimed by NODEA55**, rather than silently reversing which claim is being reviewed.

| # | Prior claim and locating strings | Verdict on NODEA55's refutation |
|---|---|---|
| 1 | `PLD.md`, “Corollary E2-RED”, especially (D1); `NODEA55.md`, na55-09 | **CONFIRMED** as a withdrawal of a usable input/proof route. The universal-F premise is false. This does not refute a formal implication from that premise, nor establish falsity at its particular adjacent-defect F. The latter is explicitly only argued in NODEA55. |
| 2 | `REVIEW_PLD_S5.md`, “Binding fix B3”; `PLD.md`, §17.4 “k ≥ 2”; `NODEA55.md`, na55-08 | **NOT-VERIFIED** on B3's original domain. The supplied k = 1 construction does not match it. The later E+ assertion is the next row. |
| 3 | `PLD.md`, “Theorem NA-PRICE^{E+} (i)”, universal F; `NODEA55.md`, “Corollary F-UNIV′” | **CONFIRMED** at k = 1 with the additional minimizer/CF argument in §1 of this report. NODEA55's positive-energy-plus-linearization deduction alone does not establish it. |
| 4 | `PLD.md`, “(CEM^{COL})_k”, “(ACT′)_k”, “(LCR^act′)_m”, “(BCH-1)_k”; `NODEA55.md`, na55-07 | **CONFIRMED** for their universal-F, nonzero-rate claims, with the law/read-set qualifications in §1. |
| 5 | `HW.md`, §37 “l.1530's clause is withdrawn as ill-formed”; `NODEA55.md`, na55-17 | **REFUTED** as a refutation of ill-formedness: NODEA55 itself acknowledges that col(Γ) is undefined in that clause. Repairing it by Γ∪Y proves that (0a⁺) is a viable third reading; it does not make the original expression well-formed. The restriction to only (0a)/(0b), and omission of the consumer's (0a⁺), deserve correction. |
| 6 | `PLD.md`, §19.7 “(0a) is the weaker, and strictly” and §19.11 “only, and drop (0b)”; `NODEA55.md`, B.3 | **CONFIRMED** against dropping (0b) on the Y-route: CRC at m = 1 needs it, and TEL-f's other bottom consumer needs (0a⁺). **NOT-VERIFIED** as a theorem about strict logical ordering of the differently typed (0a)/(0b) statements; counting open proof ingredients does not establish that order or its negation. |
| 7 | `REVIEW55_HWPLD.md`, F12 “1 + 4Rg_K²”; `NODEA55.md`, Part F “valid only … ≤ 3/8” | **REFUTED** in that literal form. The factor 4 is unnecessary, but is a valid looser bound on the entire domain where the factor 2 is valid. The narrower restriction belongs to an unsuccessful intermediate estimate, not to the bound itself; see the exact calculation below. |
| 8 | `PLD.md`, §16.6(b) “the excess sh(x_Q) − sh(Q) … is depth-free”; `NODEA55.md`, Part E | **CONFIRMED.** The one-cube family has excess 81+175D for arbitrarily large depth D. No fixed per-cube additive constant can bound it. |
| 9 | `PLD.md`, §16.7 “Δ_sh is a per-cube constant”; `NODEA55.md`, Part E | **CONFIRMED.** The full child column contains the chosen child from row 8, so its excess is no smaller. Moving all excess into c_sf is invalid. The HW route avoids this charge because PLD's LI^U constant is zero there; that constant is distinct from HW's CRC c_U. |

For row 7, let x = Rg_K² ≤ 1/2. The correct exact derivation is

    u_k/u_i ≤ 1 + R/u_i,
    R/u_i ≤ x/(1−x) ≤ 2x,
    hence u_k/u_i ≤ 1+2x ≤ 1+4x.

Thus DOM′'s λ_f = 24θ(1+2Rg_K²) is **CONFIRMED** despite PLD's incorrect intermediate assertion g_k ≤ g_K. The alternative intermediate bound (1−x)/(1−2x) is ≤ 1+4x only for x ≤ 3/8. At x = 2/5 it equals 3 > 13/5, while the correct bound is 9/5. Failure of that intermediate route cannot refute the weaker factor-4 inequality. This also means NODEA55's “NOT-VERIFIED 0” and unqualified nine-refutation tally should not be banked.

For rows 8–9, take q = 3(3^D−1)/2 in every coordinate and the child at 3q. The coordinate shadow recurrence [a,b] ↦ [floor(a/3)−1, floor(b/3)+1] gives

    ||{Q}||_sh = 1+81D,
    ||{x_Q}||_sh = 82+256D,
    difference = 81+175D.

A sufficiently large torus realizes every finite D without wraparound. The limiting ratio 256/81 also rules out a universal multiplicative coefficient below 256/81 with a fixed additive per-cube term. The proved coefficient 16 and additive 66 are safe. This proves a geometric obstruction to the cited allowance, not an obstruction to the fixed-neighbourhood route.

Negative-claim scope: the alternatives actually checked were restriction of spectators, restriction of conditioning, Hölder combination, fixed-neighbourhood relaxation, and the Gaussian convex-core mechanism. Several survive. No exhaustive “no route exists” claim, new physical premise, or retained-status promotion is made. The B3 level mismatch is explicitly excluded from the counterexample's scope; the remaining nonlinear moments are open estimates, not impossibility results. The original sources, rather than agreement among earlier reviews, supply the evidence.

## Exactly what may be banked

1. **The universal-conditioning moment obstruction at k = 1**, and its consequences for ACT′/LCR^act′/EQ-bc plus BCH-1. The **k = 1 E+ probability obstruction** may also be banked with this report's additional minimizer and exact-CF argument. The original B3 claim at k ≥ 2 is not settled here.
2. **SPEC, the named consumers' restricted spectator fit, and cutoff-uniform polynomial LT at fixed finite volume**, with Φ_{−1} handled explicitly. No volume-uniform moment follows from LT.
3. **Hölder's repaired consumer implication**, after adding the far-Y hypothesis, freezing the spectator rate, using the appended allowance constants, and imposing θ < 1/[28(1+2Rg_0²)]. Not the printed unrestricted implication or endpoint.
4. **The fixed-neighbourhood geometry, conditional CRC-2T°/CRC-HW° reduction, and exact constants**, retaining both CEM° and W0 as open inputs and choosing c_f from c_U^in.
5. **The Gaussian convex-core theorem**, with uncapped quadratic spectators, positive-definite quotient, c_cem = (1−λ_bar)^(−34992), and decoupling constant 1. No extension to the actual finite-cutoff nonlinear law is banked.
6. **The multiplicative push-down bound, the explicit refutation of depth-free additive excess, and DOM′'s factor 1+2Rg_K².** Neither the blanket nine-refutation tally nor “node A closed” may be banked.
