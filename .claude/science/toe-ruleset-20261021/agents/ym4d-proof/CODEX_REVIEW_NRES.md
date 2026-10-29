## PRE-STATED

Independent hostile review of `NODEA_RES55.md`, requested 2026-10-28. These criteria were written before reading the target or its check outputs. Prior exposure: the six claims and numerical witness values in the user's request. All paths below are relative to `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/` unless explicitly marked otherwise.

1. Counterexamples must satisfy every stated hypothesis, including symmetry, strict convexity, quadratic domination and the precise event. Establish the probability inequality analytically with exact constants; a floating-point integral is insufficient. Distinguish refuting the Anderson-type mechanism from refuting (M2) or (LCR°).
2. BL-TILT must state the Hessian lower bound, tilt domination, mean-zero hypothesis, support/regularity and integration domain. Check the factor of two, trace/rank count, volume and spectator dependence, and a valid limiting argument for convex restrictions. Verify the external Brascamp–Lieb inequality against a primary source; any unverified literature recollection is marked [m].
3. Zero mean must follow from invariance of the complete tilted, constrained law and the absence of invariant colour vectors. Check the cubic coefficient directly and do not assume inversion symmetry.
4. Recompute the `nr55_2*` witness using exact arithmetic, including stationarity, admissibility, tangent direction and Hessian normalization. Decimal output alone proves nothing. A negative mode must occur strictly inside the claimed small-field domain, on an allowed lattice and constraint subspace.
5. Proposition NU must use genuinely cutoff-independent Peierls data and account for normalization, denominator positivity and quantifiers. Identify any dependence of the assumed input on the conclusion through c_U.
6. Inspect G5n2 as a control. A non-firing witness is neither a counterexample nor a proof of the desired theorem.

Verdicts are CONFIRMED, NOT-VERIFIED or REFUTED, each tied to a file and locating string. Conditional mathematical results stay conditional. No git commands; no writes outside this file; no retained-status or audit-status changes. Read large sources through grep/rg and bounded sed ranges. Computations use integer/rational or exact symbolic arithmetic only; run code without bytecode or output-file generation. End with an explicit list of exactly what may be banked.

## Verdict and scope

The two counterexamples and the abstract BL-TILT inequality survive review. **The proposed convex-domain approximation is invalid as written; a valid replacement proof is supplied below.** The capped-spectator corollary survives that repair with the stated constant. The Hessian obstruction is confirmed for the two finite Wilson-action patches, with independent exact witnesses. These results do not prove the actual-chain (LCR°), (M2), small-field convexity, or cutoff-uniform Peierls input.

This is one independent mathematical review, not an audit-status action or a landing review. No git commands were run. Only this file was written. The local review-loop and no-go-discipline instructions were used for evidence and scope; their git, landing, and other-file procedures are outside the user's explicit contract. No previous review's verdict was used as mathematical evidence.

Source identity: `NODEA_RES55.md`, SHA-256 `3045e5d939fb8ff9b130326b8916d00185fd5a23177ad6f32687662ae0dfc76b`, including its append-only corrections and Errata E1–E3. Relevant dependencies were inspected by locating strings in `NODEA55.md`, `PLD.md`, `HW.md`, `HIST.md`, `RLARGE.md`, and `SMALLNESS_DAG.md`. This does not certify the rest of those large files. The target's cited `REVIEW_BRIEF_55.md` was absent at the stated directory; the user's explicit review contract supplied the scope.

| Claim | Verdict | File and locating string |
|---|---|---|
| Symmetric strongly log-concave counterexample to constant-one quadratic-tilt anti-correlation | **CONFIRMED** | `NODEA_RES55.md`, `Proposition NO-ONE (i)` |
| Gaussian two-defect counterexample at cutoff one | **CONFIRMED** | `NODEA_RES55.md`, `Proposition NO-ONE (ii)` |
| Smooth Brascamp–Lieb statement and its normalization | **CONFIRMED** | `NODEA_RES55.md`, `Brascamp–Lieb [BL]`; primary source below, equation (1.3) |
| The displayed mollification argument | **REFUTED** as a general construction | `NODEA_RES55.md`, `V_j := (V + j·dist(·, K)²)` |
| BL-TILT, with D1–D4 and the repaired limiting proof below | **CONFIRMED** | `NODEA_RES55.md`, `Theorem BL-TILT` |
| BL-1–BL-3 in their quantitative convex models, including caps | **CONFIRMED** | `NODEA_RES55.md`, `Corollary BL-1`, `Corollary BL-2`, `Corollary BL-3` |
| Global colour invariance gives zero mean in an equivariant chart; cubic odd-trace coefficient is −4 | **CONFIRMED**, with the chart and law qualifications below | `NODEA_RES55.md`, `(D4) mean zero`, `cubic vertex` |
| G5 non-convexity on the specified fixed-boundary patches | **CONFIRMED** | `checks/nr55_2.py`, `setup`, `Q_and_grad`, `G5b` |
| Extrapolation to the lane's admissible threshold, full normalized chain, or multiscale core | **NOT-VERIFIED** | `NODEA_RES55.md`, `Extrapolation to plaquettes below the lane's ε_1`, `on the multiscale small-field core` |
| NU as a conditional finite-volume implication, uniform when all inputs are uniform | **CONFIRMED** | `NODEA_RES55.md`, `Proposition NU` |
| The required Peierls and per-defect inputs, or their purported equivalence to LC-3′ | **NOT-VERIFIED** | `NODEA_RES55.md`, `(NU-ii)`, `equivalently (LC-3′)` |
| Use the input c_U when choosing the cutoff | **CONFIRMED** | `NODEA_RES55.md`, `c_f must use c_U^in` |
| G5n2 supplies no effective independent control | **CONFIRMED** | `NODEA_RES55.md`, `E2 (§0, controls)` |

## 1. Exact counterexamples: what they refute

### 1.1 NO-ONE (i): CONFIRMED

Location: `NODEA_RES55.md`, `On R², let D :=`; check: `checks/nr55_1.py`, `G2`.

For the diamond D and slab K in the source, direct polynomial integration gives

    |D| = 2,  ∫D x₁² = 1/3,  |D ∩ K| = 3/2,  ∫D∩K x₁² = 5/16.

Thus the uniform conditional and unconditional means are 5/24 and 1/6. The extended potential |x|²/18 + indicator-potential(D) is (I/9)-convex. Its density is even; D and K are convex and symmetric. Here “strongly log-concave” allows a convex hard support, exactly as in BL-TILT's statement.

One can make the counterexample more explicit than the source's “all small t.” Set **t₀ = 1/36**. For every s in [0,t₀], the weight

    w_s(x) = exp(−|x|²/18 + s x₁²)

lies between exp(−1/18) and 1 on D. Consequently

    d/ds log μ_s(K)
      = E_{μ_s}[x₁² | K] − E_{μ_s}[x₁²]
      ≥ exp(−1/18) [5/24 − exp(1/9)/6]
      ≥ (17/18) [5/24 − (91/81)/6]
      = 697/34992 > 0.

The exponential estimates are exact: exp(−1/18) ≥ 17/18 and exp(x) ≤ 1+x+x² for 0≤x≤1, the latter following from its series and e<3. In particular,

    log[μ_{1/36}(K)/μ_0(K)] ≥ 697/1259712 > 0,
    2t₀ diag(1,0) ≤ (1/2)(I/9).

This supplies a fixed rational dominated tilt, not a quadrature result or merely an unevaluated derivative. The tilt concerns x₁ and the slab concerns x₂. The strict inequality is therefore a genuine counterexample to the proposed constant-one mechanism under symmetry, strong log-concavity, convex restriction and quadratic domination.

It does **not** refute Anderson's translation theorem: beyond the Gaussian case, quadratic reweighting has not been represented as addition of independent symmetric noise. It also does not refute an estimate with some c₂>1, BL-TILT, or a two-sided small-Hessian-perturbation theorem. The diamond's hard boundary is not such a two-sided small perturbation.

### 1.2 NO-ONE (ii): CONFIRMED

Location: `NODEA_RES55.md`, `Take two *-adjacent constrained cubes`; check: `checks/nr55_1.py`, `Gaussian n=1 derivative-sign certificate`.

Let B be the event that both |g+h| and |g−h| are at least ε. For fixed h≥0, its conditional probability is exactly

    φ(h) = 2 Φ̄(ε+h)                                      (0 ≤ h < ε),
    φ(h) = 1 − 2[Φ(h+ε) − Φ(h−ε)]                        (h ≥ ε).

The second branch includes |g|≤h−ε as well as |g|≥h+ε. Omitting the first interval would reverse the large-h reasoning. The two expressions agree at h=ε, and φ is Lipschitz. Differentiation of E[φ(σZ)] is justified by domination by a constant times |Z|. Writing ϕ for the standard normal density gives

    d/dσ Pσ(B)
      ≤ 4{−ϕ(2ε)[ϕ(0)−ϕ(ε/σ)] + ϕ(0)ϕ(ε/σ)}.

This is negative when

    exp(−2ε²) > exp(−ε²/(2σ²))[1+exp(−2ε²)].

For ε>0 and σ²≤ε²/(4ε²+2 log 2), the right-hand side is at most
exp(−2ε²)[1+exp(−2ε²)]/2, strictly below the left-hand side. Thus the endpoint of the stated sufficient interval is valid too.

At the particular example ε=1, σ₀=1/8, t=8,

    σ₀′² = (1/64)/(1−16/64) = 1/48 < 1/16,
    M = diag(1,64),  2Q_tilt = diag(0,16) ≤ M/2.

The derivative certificate holds throughout 0<σ≤1/4, since

    exp(−6)[1+exp(−2)] ≤ (1/25)(1+1/5) = 6/125 < 1.

Therefore Pσ₀′(B)<Pσ₀(B), and **Pσ₀′(R₁)>Pσ₀(R₁)**. The Gaussian reweighting identity converts this directly into the claimed strict failure of constant-one anti-correlation. All comparison constants above are rational; no normal-probability numerical evaluation was used.

Scope matters. This is an exact two-functional Gaussian cutoff counterexample. It refutes a general Gaussian covariance-increase argument for nonconvex “at most one defect” events. An embedding satisfying every local column, ring, and covariance constraint of the particular four-dimensional chain is not supplied. Nor does it show failure for every n≥1: in this two-cube example R_n is the whole space for n≥2. Read “as soon as n≥1” as failure of a theorem uniform over that entire class, witnessed at n=1.

**REFUTED as written:** the headline `NODEA_RES55.md`, `2. (M2) has no correlation-inequality proof outside the Gaussian convex core`. The counterexamples disprove the constant-one assertion in two specified classes, not every quantitative correlation inequality. The same file's BL-4 supplies an explicit quantitative comparison outside the Gaussian class.

## 2. Brascamp–Lieb and the flagged approximation

### 2.1 The external statement: CONFIRMED

The primary research paper by Carlen, Cordero-Erausquin and Lieb states, for a C² potential V on R^D with positive definite Hessian and integrable exp(−V),

    Varν(f) ≤ Eν[∇fᵀ (∇²V)⁻¹ ∇f].

See [Asymmetric covariance estimates of Brascamp–Lieb type, equation (1.3), p. 2](https://www.numdam.org/item/10.1214/11-AIHP462.pdf). Its Appendix, p. 11, explicitly identifies that inequality as Theorem 4.1 of Brascamp–Lieb (1976); reference [4] gives JFA 22, 366–389. Thus both the formula and the remembered theorem number are corroborated by a primary paper coauthored by Lieb. I inspected this paper, not the original 1976 scan. This citation is verified, not [m].

Taking f(x)=vᵀx and ∇²V≥H′>0 gives Varν(vᵀx)≤vᵀH′⁻¹v. There is no extra factor of two. The non-smooth convex-domain extension below is an independent proof, not something assumed from that citation.

### 2.2 The author's approximation: REFUTED; the extension: CONFIRMED after repair

Location: `NODEA_RES55.md`, `V_j := (V + j·dist(·, K)²)`.

Two problems invalidate this recipe in the stated generality. W is allowed to be +∞, so directly mollifying it need not produce a finite smooth function. Also D1–D2 constrain 𝔞 only on K; V_t=W−t𝔞 need not have any convexity or lower bound outside K.

An exact counterexample to the proposed recipe already has D=1:

    K=[−1,1], H=1, W=x²/2, Q=0, 𝔞(x)=((x²−1)⁺)².

All BL-TILT hypotheses hold: 𝔞=0 on K and ν_t is the same centered truncated Gaussian for every t. But, for any t>0, V_t+j dist(x,K)² has negative leading quartic term −t x⁴. Mollification cannot turn it into an integrable strongly convex potential. The theorem is not refuted; this construction of approximants is.

Here is a valid replacement. For fixed t, set H_t=H−2tQ>0 and define the extended convex function

    F_t(x) = W(x)−t𝔞(x)−xᵀH_t x/2     on K,
             +∞                         off K.

It is proper and convex. If necessary take its lower-semicontinuous hull F. This changes no Lebesgue integrals: its effective domain has nonempty interior because the probability's normalizer is positive, and a convex function agrees with its closure on that interior; the boundary has Lebesgue measure zero. It has an affine minorant F(x)≥b+vᵀx.

For integers j≥1 use the Moreau envelopes

    F_j(x) = inf_y {F(y) + j|x−y|²/2}.

These are finite convex functions, increase pointwise to F, and satisfy

    F_j(x) ≥ b+vᵀx−|v|²/(2j).

Convolve F_j with a smooth compactly supported nonnegative symmetric mollifier ρ_{ε_j}. Choose ε_j→0 small enough that |F_j*ρ_{ε_j}−F_j|≤1/j on the ball of radius j; this is possible by uniform continuity on compact sets. Set

    V_j(x) = xᵀH_t x/2 + (F_j*ρ_{ε_j})(x).

Then V_j is finite, smooth and H_t-convex. Symmetry of the mollifier preserves the affine minorant, so all exp(−V_j), multiplied by any polynomial of degree at most two, share an integrable Gaussian majorant. Also V_j→xᵀH_t x/2+F almost everywhere. Dominated convergence gives convergence of normalizers, means and second moments. Apply the smooth BL inequality to V_j and pass to the limit:

    Cov_{ν_t}(X) ≤ H_t⁻¹.

No symmetry of the approximants is needed: this is a covariance inequality, and D4 is imposed on the limiting law. This closes the flagged weak step under precisely the theorem's hypotheses.

### 2.3 BL-TILT and the constant: CONFIRMED with all hypotheses retained

Location: `NODEA_RES55.md`, `Then for t ∈ [0, λ̄]`; `Corollary BL-1`.

D1 and D4 now give

    E_{ν_t}[𝔞] ≤ E_{ν_t}[XᵀQX]
                = tr(Q Cov_{ν_t}X)
                ≤ tr[Q(H−2tQ)⁻¹]
                = (1/2)tr[B(I−tB)⁻¹].

The strict margin λ̄ c̄<1 supplies integrability, including enough Gaussian domination to differentiate the partition function. Integrating each eigenvalue term gives exactly

    log Eν exp(λ̄𝔞) ≤ −(1/2) log det(I−λ̄B).

The rank bound, not the full volume dimension, controls this trace/determinant. The Q=0 case is harmless: D1 forces 𝔞=0 almost surely and both bounds become identities.

For capped spectators q_s=xᵀQ_sx with Q_s≥0 and fixed caps c_s=θπ_s,

    W = xᵀM_sx/2 + Σ_s (q_s−c_s)⁺,
    M_s = M−2Σ_s Q_s.

Every positive-part term is convex and even. Disjoint action-term budgets yield M_s>0 and 2Q_𝔞≤M_A≤M_s, so B≤I. This does not accumulate a cost proportional to the number of spectators.

For the stated **SU(2) linear model**, the exact count is

    4·8·9³ = 23328 links,
    rank(Q_𝔞) ≤ 3·23328 |A| = 69984 |A|,
    rank(Q_𝔞)/2 ≤ 34992 |A|.

`PLD.md`, `Lemma READ`, clause (i), identifies links with both endpoints in the column descendants. Taking a quotient cannot increase the rank. Hence

    E_{μ_R} exp(λ̄𝔞) ≤ [(1−λ̄)^(−34992)]^|A|,
    E_{μ_{R,λ̄}}[𝔞] ≤ [34992/(1−λ̄)] |A|.

The first expression is the integrated CEM constant; it is sharper than obtaining CEM by multiplying the endpoint mean bound by λ̄. The second is LCR°. Both are volume-uniform provided λ̄ is fixed below one uniformly in the family. For SU(N) the colour dimension is N²−1, not always three.

BL-2's Gaussian comparison also follows with its stated symmetry: for Σ_s=Σ+sΔ with Δ≥0, differentiation gives

    d/ds log P_{Σ_s}(K)
      = (1/2)tr[Σ_s⁻¹ΔΣ_s⁻¹(Cov[X|K]−Σ_s)] ≤ 0.

The conditional mean vanishes because K is symmetric, and BL gives Cov[X|K]≤Σ_s. This verifies the interpolation formula without invoking a Gaussian correlation theorem.

BL-3 also checks: with curvature (1−δ)M_s, the moment base is 1−λ̄/(1−δ), and the endpoint mean constant is **34992/(1−δ−λ̄)**. The source's Erratum E1 is correct; the earlier denominator must not be reused.

**NOT-VERIFIED as an actual-chain application:** plain log-concavity alone is insufficient. One needs quantitative H-convexity, D1–D2, the strict domination margin, mean zero, convex support and the local rank bound. For example, the centered uniform law on [−2,2] is log-concave, but with q=x² and t=1/2 its exponential moment is at least 1+E[x²]/2=5/3>√2. It does not satisfy the rank-one Gaussian constant without the required curvature/domination hypothesis. The source's `using only convexity of the constraint and a mean-zero condition` in §7 item 3 drops essential hypotheses.

**REFUTED literally, harmless after correction:** `NODEA_RES55.md`, `34992·ln 2 ∈ [24254.606142, 24254.606142] (rigorous enclosure)`. Identically rounded endpoints are not a rigorous interval. The exact series in `checks/nr55_1.py`, `ln2_enclosure`, is valid and gives

    24254606142/1000000 < 34992 log 2 < 24254606143/1000000.

### 2.4 BL-4: CONFIRMED as a separate two-sided conditional theorem

Location: `NODEA_RES55.md`, `Corollary BL-4`.

For the unconstrained tilted density, write s=∇V_t and J=E[ssᵀ]. Gaussian tails and the two Hessian bounds justify integration by parts: E[s]=0, E[(X−EX)sᵀ]=I, and J=E[∇²V_t]. The positive semidefinite covariance block matrix of (X,s) therefore gives

    Cov(X) ≥ J⁻¹ ≥ [(1+δ)M−2tQ]⁻¹.

This is the needed Cramér–Rao step, derived here rather than imported from memory. For the constrained law BL gives the upper covariance bound with (1−δ)M. Mean zero on both sides then yields the source's eigenvalue difference

    δb_i / [(1−δ−tb_i)(1+δ−tb_i)]
      ≤ δb_i/(1−δ−λ̄ c̄)².

Integration proves its comparison constant. For a per-column constant, rank(Q)≤69984|A| is still required. The notation 1+O(δ) is uniform only with a fixed positive domination margin. This corollary neither covers hard caps via an upper Hessian bound nor supplies such a bound for the nonabelian chain. BL-1 covers caps by a different, one-sided argument.

## 3. Colour symmetry and the cubic term

**CONFIRMED:** `NODEA_RES55.md`, `(D4) mean zero`, for the complete globally conjugation-invariant law expressed in a conjugation-equivariant chart with integrable coordinates.

For each coordinate X_ℓ in su(N), invariance gives E[X_ℓ]=Ad_h E[X_ℓ] for every h∈SU(N). Such a mean commutes with every h, hence is scalar; being traceless it is zero. This works simultaneously on all links. A conjugation-stable tree gauge leaves this global action available. Gauge-invariant traces and norms, fixed geometric constraint patterns, scalar spectator caps, and the infimum defining the column action are preserved by simultaneous conjugation. The kernel normalizers in `HW.md`, `## 0. Conventions`, are invariant by a Haar change of variables. The group argument therefore does not require central inversion symmetry.

This assertion has a necessary qualification: use a chart/domain and gauge choice that retain the action and cover the law under consideration. It supplies no convexity theorem for that chart. Fixing arbitrary boundary fields in a disintegration generally destroys global conjugation invariance of each conditional law. The source's later replacement of D4 by a forced-mean term is necessary, not optional.

**CONFIRMED:** `NODEA_RES55.md`, `cubic vertex`; `checks/nr55_1.py`, `odd_part_coeffs`.

Using σ₁σ₂=iσ₃ and exp(itσ_j)=cos(t)I+i sin(t)σ_j gives the exact identity

    tr[e^(itσ₁)e^(itσ₂)e^(−itσ₃)] = 2(cos³t − sin³t),
    tr U(t) − tr U(−t) = −4 sin³t.

Thus the requested coefficient is **[t³](tr U(t)−tr U(−t))=−4**. It is not the coefficient of every quantity called a cubic vertex: [t³]tr U(t)=−2 and [t³](1−tr U(t)/2)=+1. This normalization distinction matters. Commuting generators give zero odd trace, as the control reports. The asymmetric plaquette term is an exact obstruction to claiming inversion symmetry in these exponential link coordinates; it does not prove that every conceivable nonlinear chart is asymmetric.

For conditional BL applications, the valid general formula is

    E[𝔞 | datum] ≤ tr(Q Cov[X | datum]) + m_{datum,t}ᵀQ m_{datum,t},
    m_{datum,t} = E[X | datum, tilted at t].

Replacing the last term by an unspecified “boundary-forced configuration” is **NOT-VERIFIED** unless that term actually controls this tilted mean and any action outside the conditional region. Even a one-dimensional Gaussian with potential (x−b)²/2 and tilt t x² has mean b/(1−2t), so its mean-square charge is b²/(1−2t)², not b². Location: `NODEA_RES55.md`, `(LC-1′)`, `the mean is now the boundary-forced configuration`. The corrected constant in Erratum E1 is sound once the required conditional estimate and disintegration are supplied; those inputs have not thereby been proved.

## 4. Exact rerun of nr55_2 and nr55_2b

### 4.1 What was actually executed

Files: `checks/nr55_2.py`, `checks/nr55_2_criteria.md`, `checks/nr55_2_out.txt`, `checks/nr55_2b_out.txt`. Locators: `setup`, `assemble_H`, `Q_and_grad`, `lowest_vec_float`, `G5a`, `G5b`, `G5c`, `G5d`, `G5n2`.

The original entrypoint executes a floating-point proposal search. I did **not** run that entrypoint. I loaded only its exact definitions through line 138 using sed, assembled its rational Hessian, and generated replacement integer directions by the deterministic integer iteration reproduced below. Every reported certificate uses rational arithmetic. This is a rerun of the witness geometry and Hessian checks with independently chosen exact directions, not a claim to have recovered the author's unsaved rounded vector.

An independent implementation represented SU(2) matrices as aI+i(v·σ), with multiplication

    (a,u)(b,v) = (ab−u·v, av+bu−u×v),

and multiplied degree-two link-exponential polynomials around plaquettes. It independently reconstructs backgrounds, plaquette order and inverses. It agrees exactly with both the author's assembled Hessian and direct matrix-polynomial action on each new witness. The author's two paths alone are not independent of one another: `assemble_H` and `Q_and_grad` both call `plaq_trace_poly`.

One initial reviewer harness attempt failed its agreement assertion because integer zeros entered Python `/2` in the new quaternion code. That attempt was discarded, and its output supplies no certificate. The corrected harness explicitly uses Fraction zeros/divisors and asserts Fraction-valued results. A first exact 2000-step run already gave negative directions; the reported 20000-step run refined them. No archived source or output file was changed.

### 4.2 Exact results: CONFIRMED

Use S=Σ_P(1−tr U_P/2), Q_C(v)=d²S(εv)/dε² at ε=0, and the coordinate norm Σ_ℓ(a_ℓ²+b_ℓ²+c_ℓ²). These are the source's conventions. The Rayleigh quotients below belong to the new directions; they are not claims about exact smallest eigenvalues.

| Quantity | τ=1/4, N=8 | τ=1/8, N=12 |
|---|---|---|
| Variable links / real coordinates | 112 / 336 | 264 / 792 |
| Nonzero gradient coordinates | 0 / 336 | 0 / 792 |
| Fine plaquette norm squared | 4/17 | 4/65 |
| Fine plaquette norm, exactly | 2/√17 | 2/√65 |
| Rational enclosure of Q_C(v)/‖v‖² | (−1072788/10⁶, −1072787/10⁶) | (−524805/10⁶, −524804/10⁶) |
| Rational enclosure of Q_1(v)/‖v‖² | (2229350/10⁶, 2229351/10⁶) | (2196359/10⁶, 2196360/10⁶) |
| Blocked plaquette norm squared | 307894033924/118587876497 | 67069232592107524/20711912837890625 |

The exact negative quotients are respectively

    −47717287861131025708616435463762800286
      /44479717554827449142572526323911160417,

    −6989000145345774903844344665086169001332323260780718420801588
      /13317348220618331313433813727251203982279613363742828369140625.

The fine norms are strictly between 485/1000 and 486/1000, and between 248/1000 and 249/1000. This corroborates the sign and scale of the archived −1.07 / −0.52 witnesses. The precise archived rounded-vector quotients −1.072701 and −0.5247369 are **NOT-VERIFIED as identical-vector reproductions**: the rounded vectors were not persisted. The replacement certificates are strictly more negative, so this provenance limitation does not weaken the non-convexity conclusion. Their different free-field quotients are expected for different directions.

Stationarity also has a direct explanation: first-order charged variations have zero trace against a diagonal background, and the diagonal first-order contributions of the two plaquettes adjacent to an unfrozen link cancel. Thus this is a critical point of the fixed-boundary patch action. At a critical point the Hessian's inertia is invariant under smooth coordinate changes on that patch. Gauge directions are null there, so a strictly negative direction is not pure gauge.

The backgrounds lie strictly inside single-level cuts ε=1/2 and ε=1/4 respectively, since 4/17<1/4 and 4/65<1/16. By continuity the witness curves remain in those open cuts for sufficiently small parameter. G5d is also exact: both blocked norm squares exceed the corresponding fine norm square, and exceed these chosen cut squares. These examples therefore need not lie in a core with all blocked levels small.

### 4.3 Required limitation on the chain claim: NOT-VERIFIED

Location: `NODEA_RES55.md`, `H-convexity of the chain potential`, `Extrapolation to plaquettes below the lane's ε_1`; `checks/nr55_2_criteria.md`, `2D lattice patch`.

What has been proved is non-convexity of the **raw SU(2) Wilson action on a finite two-dimensional patch with its specified fixed boundary links**. One can copy the field and variation constantly into two additional periodic directions and set those extra links to identity; all mixed plaquettes then remain identity, so the Wilson-action quotient is unchanged on that fixed-boundary product geometry. This still is not the claimed all-level, periodic-torus, gauge-fixed probability density.

The script contains neither the normalized interlevel kernels nor a Haar/gauge-chart Jacobian, and it proves no smallness statement for those additional terms. The particular finite witnesses also do not reach the lane's admissible ε₁: `RLARGE.md`, `TH-ch″`, explicitly distinguishes its tiny allowed thresholds from illustrative order-one cuts. A uniform family reaching arbitrarily small ε₁ would require an error-controlled scaling and boundary construction, which the source labels ARGUED and does not provide. Likewise, negative curvature of the raw action alone does not certify the full chart density at every coupling.

The phrases “Nielsen–Olesen” and “Atiyah–Bott mechanism” remain **[m]** as literature identifications in this review. No continuum spectral theorem is used to replace the finite exact certificate. Multiscale convexity, its δ=O(ε₁) claim, and an application of BL-TILT to the actual chain remain **NOT-VERIFIED**.

### 4.4 G5n2: non-firing disclosure CONFIRMED

Location: `NODEA_RES55.md`, `E2 (§0, controls)`; `checks/nr55_2.py`, `vab =`; archived outputs, `Q_C(v_abelian) = 0.000000e+00`.

The source's revised disclosure is appropriately cautious. Its output does not establish whether the discarded charged vector had no neutral component or had a neutral null direction. In either case zero energy makes this particular projected control uninformative. A PASS printed for `not (qab < 0)` does not establish that a nonzero perturbation was tested.

For a neutral variation c, the exact formula at this background is

    Q_C(c) = cos(α) Σ_P (dc)_P²,
    cos(α) = (1−τ²)/(1+τ²),

not literally the unweighted free Hessian. Here the factors are 15/17 and 63/65, both positive. The corrected reviewer harness uses a nonzero unit neutral coordinate, giving

    Q_1=2,  Q_C=30/17       at τ=1/4,
    Q_1=2,  Q_C=126/65      at τ=1/8.

These are non-vacuous exact controls. Also Q_1(v)=Σ_P |(dv)_P|²≥0 for every variation at the trivial background, which proves the free control's sign independently of a searched vector. The report does not count the original G5n2 as an additional successful discriminating control.

## 5. Cutoff uniformity and the c_U loop

### 5.1 Proposition NU: CONFIRMED as an implication

Location: `NODEA_RES55.md`, `Proposition NU`; constraint definition: `HW.md`, `R_{S,E} :=`.

Work at finite volume and finitely many levels, with μ_∅(R_n)>0. The sets F_D={𝒟=D} partition configuration space, and R_n is determined by D. If declared defects E are present, define the allowed collection using the components of **D∪E**, restricted to S; the proof's shorthand `components ≤ n` must include this fixed datum. For any allowed D of positive probability,

    μ_{R_n}(· | F_D) = μ_∅(· | F_D).

For nonnegative multipliers the finite identity

    E_{μ_{R_n}} Π_{x∈𝒟}(1+ρ_A(x))
      = Σ_Y [Π_{x∈Y}ρ_A(x)] μ_{R_n}(Y⊂𝒟)

is exact, including Y=∅. NU-i, NU-ii and NU-iii therefore imply

    E_{μ_{R_n}} exp(λ̄𝔞)
      ≤ c^|A| Π_x[1+ρ_A(x)η(x)]
      ≤ (c exp b)^|A|.

There is no extra division by μ_∅(R_n) left in this calculation: it is already present in the **constrained** probabilities assumed in NU-ii. This is precisely why an unconstrained Peierls estimate cannot simply be substituted. Infinite-volume extensions, if needed, require a limiting law; this finite-volume proof itself has no infinite-volume assertion.

If the same c,b,ρ_A,η work for all n and all other consumer data, the conclusion is uniform over that family. The proposition supplies no such inputs. Under this ansatz, NU-i and NU-iii are n-independent assumptions, so NU-ii is the remaining location at which n can enter. That is a conditional accounting fact, not a proof that every conceivable approach has only that dependence.

**NOT-VERIFIED:** the Gaussian-model suggestion following NU. Conditioning on defect *values* can give a Gaussian conditional law; conditioning only on the pattern F_D is truncation by inequalities and is generally not Gaussian. One must still integrate amplitudes with appropriate uniform bounds. The file correctly marks this part ARGUED.

**NOT-VERIFIED:** §7 item's `equivalently (LC-3′)`. An all-subset probability product bound and a first moment of a forced action are different inputs. For example, perfectly correlated defect indicators with probability p have joint event probability p, not p^|Y|, while a bounded weighted forced action can still have a bounded first moment. Conversely a small defect probability controls no arbitrarily large forced amplitude without an amplitude estimate. No equivalence follows from either displayed definition.

The proposed joint induction with CRC remains **NOT-VERIFIED**: each invocation must actually use a strictly smaller constraint pattern with common constants. Stating that ordering is a design condition, not a completed induction.

### 5.2 c_U-input warning: CONFIRMED

The dependency trace is present in the source files:

| Definition or dependency | File and locating string |
|---|---|
| c_f°=c_U+81c_A | `NODEA55.md`, `Corollary CRC-HW°`, `c_f° :=` |
| B₀=c_f+2 | `HW.md`, `Order of constants (non-circular): a, C_ℓ, c_f` |
| c_B=38416 B₀/log L and n_H=⌊(4+c_B)/(aβ_−)⌋ | `HIST.md`, `Theorem HIST-sum`, `c_B :=` |
| Sharper geometric coefficient 10000 in c_B | `HW.md`, `hence **c_B := 10000B_0/log L**` |
| n_♯≥n_H, followed by choosing g₀ | `HW.md`, `→ n_H(a, B_0) → n_♯` |
| ε₂°=6400^n_♯(C_ℓ exp(b_n°+aR−a/g_K²))^(n_♯+1) | `NODEA55.md`, `ε_2° :=` |
| c_U^out=2ε₂°, with 2ε₂°≤c_U^in | `NODEA55.md`, `(S2°)`; `NODEA_RES55.md`, `c_U^out = 2ε_2°` |

Using the output in the initial definition would create

    c_f → B₀ → c_B → n_H → n_♯ → ε₂° → c_U^out → c_f.

Fix c_U^in∈(0,1] first and define c_f with it. After choosing n_♯, lower g₀ to establish c_U^out≤c_U^in. Then the output may improve an already established estimate without retroactively changing how the cutoff was chosen. `HW.md`, `[RHW5-fix SYM-1]`, explicitly makes this distinction. The coefficient improvement in c_B does not alter the dependency argument.

This confirms the warning, not unconditional acyclicity of the entire unfinished proof. Node-A moment constants must themselves be established uniformly before this ordering can be used. The file's `No further cycle` is justified only conditional on the n-free hypotheses it has just imposed.

## 6. Additional consequential overstatement: same-rate moments versus means

**REFUTED:** `NODEA_RES55.md`, §4, `equivalently, by Lemma IMPL (ii)`. The lemma proves the forward implication from an endpoint tilted-mean bound to an exponential-moment bound. Its converse at the same endpoint is false, even for bounded nonnegative random variables.

For a positive integer m, let 𝔞=m with probability 2^(−m), otherwise 𝔞=0, and take λ̄=log 2<1. Then exactly

    E exp(λ̄𝔞) = 2−2^(−m) < 2,
    E_{λ̄}[𝔞] = m/(2−2^(−m)) > m/2.

Thus the moment has a uniform constant while the tilted mean diverges with m. Each member of the family has a bounded 𝔞, as required for the differentiation argument. The example need not be log-concave because the claimed equivalence and Lemma IMPL concern general bounded column observables before convex hypotheses are imposed.

**CONFIRMED:** the explicitly typed implications in Lemma IMPL (i)–(iii), and the positive implications in (iv). In particular LCR° implies CEM°; (M1^mean)+(M2^mean) implies LCR°. The exponent-form pair implies CEM°, not automatically LCR°. The untyped statements in §6 row nr-06 and §7 item 1 must retain this distinction. A moment bound at a strictly larger rate could supply a smaller-rate mean bound, but that is an additional margin, absent from the asserted equivalence.

## 7. Scope discipline and execution record

The negative conclusions are restricted to explicit universal claims and their counterexamples, not to Yang–Mills construction as a whole. The no-go checks are recorded here within the user's one-file contract:

- **N1:** The actual alternatives are constant-one Anderson comparison (refuted in the two broader classes), direct BL-TILT (confirmed under its hypotheses), two-sided BL/Cramér–Rao comparison (confirmed), the NU defect expansion (conditional), conditional DLR with forced means (not completed), and reflection/chessboard methods (not certified here). This is a map of real alternatives, not a claim that five or more approaches have been exhausted.
- **N2:** No independence or numerical count of “walls” is asserted. Curvature, support, tilted means, defect amplitudes and Peierls bounds can interact. NU and LC-3′ are not silently identified.
- **N3:** Quantitative curvature, support convexity, chart equivariance, normalization positivity, fixed rank per column and constant uniformity remain explicit assumptions.
- **N4:** The diamond is a counterexample in the stated strong-log-concavity class; the two-defect Gaussian is a counterexample to the general cutoff mechanism; G5 is a finite patch certificate. None is silently substituted for an admissible full-chain counterexample.
- **N5:** No inference from these two patch sizes to every scale or every smaller ε₁ is made. No claim of a smallest eigenvalue is made.
- **N6:** The repaired convex extension and direct tilted-mean method are mathematical repairs, not new physical axioms.
- **N7:** The strongest counterpoint to any broad negative conclusion is already constructive: BL-TILT proves the moment in the quantitative convex class, BL-4 proves a quantitative comparison, and a constrained Peierls analysis could extend the cutoff result. These routes remain open for the chain.
- **N8:** `NODEA55.md`, `Proposition GAUSS` and `(v) The cutoff allowance`, already distinguish the Gaussian convex core from the intermediate cutoff. `SMALLNESS_DAG.md`, `The n_♯ loop`, already isolates the uniformity issue. The present witnesses narrow those mechanisms; they do not turn an earlier open question into a global impossibility theorem.

Exact checks performed: G1–G4 and their applicable controls from `nr55_1.py` were run in memory with formatting removed and the floating quadrature omitted; all 11 executed gates were true, including exact cubic coefficient −4. The analytic arguments above establish the all-real probability inequalities independently of G3's finite grid. Both G5 geometries were recomputed with integer proposals and rational certificates; a quaternion implementation cross-checked the final action derivatives. A finite two-defect expansion also checked NU's product identity at cutoffs 0, 1 and 2; the general finite-set proof is the one given above.

No source correction was applied. All fixes and narrowings are review findings in this file. No retention, formal audit, full pipeline, git status, commit or branch claim is made. The source's remembered statements about Holley–Stroock, Bakry–Émery, Ginibre, Balaban and continuum instability mechanisms remain **[m] / NOT-VERIFIED** here unless replaced by an explicit derivation above; they are not ingredients in the banked conclusions.

### Reproducible exact Hessian check

Run the following from the repository root with `PYTHONDONTWRITEBYTECODE=1 python3 -B`. It writes no files. The integer iteration is only a proposal generator: its convergence is not assumed, and the final strict rational inequality is the certificate. The vector hashes in the observed run were `81127856d3ad95acd627bb5b61d122e3805f0c6372b64bdd04716e2bf70f2069` and `945bf150173a7ac1f0cc30480c8e64c523a83c5cb89087850bbb3cbbb3dc670e` in the table's order.


```python
from fractions import Fraction as F
from math import lcm
import subprocess,hashlib
p='.claude/science/toe-ruleset-20261021/agents/ym4d-proof/checks/nr55_2.py'
ns={};exec(compile(subprocess.check_output(['sed','-n','1,138p',p],text=True),p,'exec'),ns)
def qm(a,b):
 s,x,y,z=a;t,u,v,w=b
 return (s*t-x*u-y*v-z*w,s*u+t*x-y*w+z*v,s*v+t*y-z*u+x*w,s*w+t*z-x*v+y*u)
def qs(a,s):return tuple(s*x for x in a)
qi=(F(1),F(0),F(0),F(0))
def poly(P,Q):
 return tuple(tuple(sum(qm(P[i],Q[d-i])[k] for i in range(d+1)) for k in range(4)) for d in range(3))
def independent(N,tau,links,v):
 cs=(1-tau*tau)/(1+tau*tau);sn=2*tau/(1+tau*tau);powers=[qi]
 for j in range(N):powers.append(qm(powers[-1],(cs,F(0),F(0),-sn)))
 data={l:tuple(v[3*k:3*k+3]) for k,l in enumerate(links)}
 def link(i,j,mu,inverse):
  a=data.get(((i,j),mu),(F(0),)*3);b=powers[j] if mu==1 else qi
  E=(qi,(F(0),)+a,(-sum(x*x for x in a)/F(2),F(0),F(0),F(0)))
  if inverse:
   b=(b[0],-b[1],-b[2],-b[3]);E=(E[0],qs(E[1],-1),E[2]);return tuple(qm(b,x) for x in E)
  return tuple(qm(x,b) for x in E)
 Q=F(0);grad=F(0)
 for i in range(N):
  for j in range(N):
   P=poly(poly(poly(link(i,j,1,False),link(i+1,j,2,False)),link(i,j+1,1,True)),link(i,j,2,True))
   Q-=2*P[2][0];grad-=P[1][0]
 return Q,grad
for N,tau in [(8,F(1,4)),(12,F(1,8))]:
 G=ns['setup'](N,tau);H=ns['assemble_H'](G);n=len(H);print('ASSEMBLED',N,tau,n,flush=True)
 assert all(H[j].get(i,0)==h for i,row in enumerate(H) for j,h in row.items())
 bad=0
 for k in range(n):
  e=[F(0)]*n;e[k]=F(1);_,g,im=ns['Q_and_grad'](G,e);bad+=int(g!=0 or im!=0)
 assert bad==0
 den=lcm(*(h.denominator for row in H for h in row.values()))
 rows=[[(j,int(h*den)) for j,h in row.items()] for row in H]
 shift=1+max(sum(abs(h) for h in row.values()).__ceil__() for row in H)
 seed=1;v=[]
 for k in range(n):
  seed=(1103515245*seed+12345)%(2**31);v.append(seed-2**30 if k%3!=2 else 0)
 for it in range(20000):
  y=[shift*den*v[i]-sum(h*v[j] for j,h in row) for i,row in enumerate(rows)];norm=max(abs(x) for x in y);v=[x*10**9//norm for x in y]
 vf=list(map(F,v));norm=sum(x*x for x in vf)
 qa=ns['quad_exact'](H,vf);qd,gd,im=ns['Q_and_grad'](G,vf);qq,gq=independent(N,tau,G['var'],vf);q0,g0=independent(N,F(0),G['var'],vf)
 print('AGREEMENT',qa==qd,qd==qq,'NEGATIVE',qd<0,'GRADIENTS',gd,gq,'IMAG',im,'FREE_POSITIVE',q0>0,flush=True)
 assert qa==qd==qq and qd<0 and gd==gq==0 and im==0 and q0>0
 assert all(isinstance(x,F) for x in (qa,qd,qq,q0))
 assert all(v[k]==0 for k in range(2,n,3))
 ray=qd/norm;free=q0/norm;ab=[F(0)]*n;ab[2]=F(1);qab,_=independent(N,tau,G['var'],ab);qab0,_=independent(N,F(0),G['var'],ab)
 assert qab==((1-tau*tau)/(1+tau*tau))*qab0 and qab>0
 nw=4*tau*tau/(1+tau*tau);w9=ns['cpow'](G['w'],9);nb=(1-w9[0])**2+w9[1]**2;assert nb>nw
 low=F(ray.numerator*10**6//ray.denominator,10**6);flo=F(free.numerator*10**6//free.denominator,10**6)
 print('N',N,'tau',tau,'nonzero_gradients',bad,'variables',n,'shift',shift,'iterations',20000)
 print('RQ_EXACT',ray);print('RQ_ENCLOSURE',low,low+F(1,10**6));print('FREE_RQ_ENCLOSURE',flo,flo+F(1,10**6))
 print('PLAQUETTE_NORM_SQUARED',nw,'BLOCKED_NORM_SQUARED',nb)
 print('ABELIAN_UNIT_CONTROL',qab,'FREE',qab0,'CHARGED_VECTOR_ABELIAN_NORM',0)
 print('VECTOR_SHA256',hashlib.sha256(','.join(map(str,v)).encode()).hexdigest(),flush=True)
print('ALL_EXACT_WITNESS_CHECKS_COMPLETED')
```

## Exactly what may be banked

1. **CONFIRMED:** NO-ONE (i) and (ii) as exact counterexamples to constant-one quadratic-tilt anti-correlation in their specified probability models. The first has the explicit rational endpoint t=1/36 above; the second has n=1, σ₀²=1/64 and σ₀′²=1/48. They refute the proposed general mechanism, not (M2) with arbitrary finite c₂ and not an explicitly realized full-chain instance.
2. **CONFIRMED:** BL-TILT under its complete H-convexity, D1–D4 and positive-normalizer hypotheses, using this review's convex-domain limiting proof. The source's displayed mollification recipe itself is **REFUTED**. The smooth BL input and remembered theorem number are corroborated by the cited primary paper.
3. **CONFIRMED:** BL-1–BL-3 for the stated quantitative convex models, including fixed capped quadratic spectators. For the SU(2) rank bound, CEM has c_cem=(1−λ̄)^(−34992), c_A=0; LCR has B=34992/(1−λ̄). With curvature loss δ, use B=34992/(1−δ−λ̄), and the corresponding integrated moment base 1−λ̄/(1−δ). These constants are uniform only when the stated hypotheses and margin are uniform.
4. **CONFIRMED:** BL-4's quantitative comparison under its additional two-sided Hessian bound and zero means; the colour-invariance argument in an equivariant chart for an invariant law; and the precisely normalized odd-trace cubic coefficient −4. None supplies zero conditional mean after arbitrary boundary fields are fixed.
5. **CONFIRMED:** non-convexity of the specified finite Wilson-action patches at exact plaquette norms 2/√17 and 2/√65, with the new exact negative directions, criticality, free-field positivity and larger blocked plaquettes recorded above. G5n2 remains non-discriminating; the added nonzero neutral controls are valid. Arbitrarily small thresholds, multiscale convexity, and the full normalized-chain conclusion are **NOT-VERIFIED**.
6. **CONFIRMED:** Proposition NU as the finite-volume implication from its three stated inputs, including the constrained-law Peierls estimate; cutoff uniformity only if those inputs are uniform. The input/output c_U distinction and the conditional order of constants are confirmed. The inputs themselves, the proposed joint induction, and NU-ii/LC-3′ equivalence are **NOT-VERIFIED**.
7. **CONFIRMED:** the explicitly typed forward moment/mean/comparison implications in Lemma IMPL and the exact rank arithmetic. The same-rate moment/mean equivalence and the blanket exclusion of correlation proofs beyond the Gaussian convex core are **REFUTED**. No other theorem, actual-chain closure, or scientific-status promotion is banked by this review.

