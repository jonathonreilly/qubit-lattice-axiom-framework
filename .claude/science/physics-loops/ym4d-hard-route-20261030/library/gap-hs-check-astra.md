# Repo search

The lead's `prior/repo-search-2026-11-08.md` concerns older RG targets, not this check. Its nearest hit is `pr/10114:.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149`. I fetched PR 10114 and read lines 88–155. That Codex note uses the same normalized convolution and an inverse-kinetic quadratic form to prove a positive one-step loop correlation. It does not prove the high-spin count, the deleted-plaquette estimate, or (E17). I reuse the common convolution conventions; no alternative witness proof is attempted. The digest reports the corresponding PR 10133 blob identical at its recorded revisions. I did not infer that current heads remain identical.

The target-specific `prior/gap-hs-check-astra.md` is absent. The task has no additional “Repo prior work” file list. Targeted searches of `open-registry.md` for this check, high spin, double suppression and (E17) found no competing owner. Row 864 expressly assigns this check of row 860; it does not assign a fresh attack on (E17).

The SA index was consulted first: `chunk-02.md:88–101` and neighbours, plus the insertion restriction in `obligations.md:69`. I then read outline lines 2195–2257 and 2313–2335. GL3/GL4 already supply the convolution spectrum and factorial majorant; GL8 supplies the half-kernel transfer. These are reused, credited to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. They are not new results of this check. Targeted searches of the CA 4.12–4.19 index found no matching high-spin or transfer statement. Both requested source files were fetched once into the newly created `/tmp/sa-gap-hs-check-astra.DcOpqW/`; no complete-account theorem is imported here.

Provenance: OpenAI Codex, dispatched as gpt-6-astra xhigh; source checkout `d29c0aa09491d4b7eb5f3ccbdf0af5c1648513d3`; author checked: Claude Fable 5.2 max. Research check only, not an audit; no status is granted. The requested file and verdict format control over the generic main-branch check-record format. No simulation, numerical enclosure or machine enumeration discharges any statement. The author's GUIDE run is not reproduced or verified. Balaban's effective-action work is background to the first-passage program, not an input to the finite-lattice arguments checked here.

References below are to `gap-hs-max.md` at the pinned commit, unless a filename is given. The scope is its analytic HS/OS/DS/P1–P3/B1 claims and its filter-insufficiency argument. Monte Carlo estimates, empirical percolation claims, and the separate filter theorem's full proof are outside the check. The requested constants and the additional beta=2.6 density bound are checked below.

## Theorem HS — HOLDS

Lines 72–86 hold for integer time periods `t >= 2`, with the displayed denominator `Tr(P_+ L^t)`, also when the numerator uses `P_-`. This is not a bound normalized within the odd sector.

Write `N=|E|=|P|`, `s=z^N`, `r=r_(j0)`, and `f_sigma(q)=Tr(P_sigma L^q)`. On the event A, `Pi_A K <= r^(eta N)`. The factorization in line 81 is exact, and its Y is positive trace class. Thus

```math
\operatorname{Tr}(P_\sigma\Pi_A L^t)
 \le r^{\eta N}\operatorname{Tr}(P_\sigma Y)
 \le r^{\eta N}s\|B\|_\infty f_\sigma(t-1).
```

The second inequality uses the congruence of `B^2 <= ||B|| B`, not an invalid commutation of B with K. This also handles `t=2` directly. Twisted traces of `(KB)^q` are positive integrals, including `q=1`, so `f_-(q)<=f_+(q)` for integer q. The argument does not require a geometrically nondegenerate time-one torus.

For the trace ratio, use log convexity: `g(q)=log(f_+(q)/lambda_+^q)` is convex and nonnegative. Interpolation between 1 and t gives `g(t-1)<=g(1)/(t-1)+(t-2)g(t)/(t-1)`. Hence

```math
\frac{f_+(t-1)}{f_+(t)}
 \le\lambda_+^{-1}\left(\frac{f_+(1)}{\lambda_+}\right)^{1/(t-1)}.
```

For `t=2` this follows directly from `f_+(2)>=lambda_+^2`. The normalized constant vector belongs to the even gauge-invariant space. Each spatial plaquette has four distinct links; integrating one makes its holonomy Haar. Consequently its signed Haar mean is zero. Jensen therefore gives `<1,B1>>=1`, and `lambda_+>=s`. Also `f_+(1)<=s e^(beta N) Tr_H K <= e^(2 beta N)`. Substitution gives exactly line 75. The source normalization in `gap-expose-astra.md:88–151` agrees with SA GL3/GL8 after removing the constant Wilson-action shift.

## Corollaries HS-1 and HS-2 — HOLDS AFTER CORRECTION / HOLDS

HS-1's rate and threshold survive, but line 92's asserted `log(120/1.25^4)>3.895` is false. A hand check is `e^2>sum_(k=0)^10 2^k/k!>7.3889` and `e^(-21/200)>1-21/200+(21/200)^2/2-(21/200)^3/6=0.9003195625`. Their product gives `e^(779/200)>(7.3889)^2(0.9003195625)>49.153>30720/625`. Replace the faulty lower bound by the following argument; no logarithm decimal is needed.

For `beta in [43/20,5/2]`, `r_2 <= 625/30720` and `z=2 I_1(beta)/beta >=1+beta^2/8 >3/2`. The exponential series gives `e<87/32` (sum through degree six, followed by a geometric tail of ratio at most 1/8). Thus `e^4<55`, and `e^(1/8)>9/8` gives

```math
 e^{31/8}<440/9<30720/625,\qquad \log(1/r_2)>31/8.
```

Also `e^(1/4)<3/2`, since `e<(3/2)^4`, so `log z>1/4`. For all `t>=9` the HS exponent is at least

```math
 \frac{31}{8}\eta-\frac{99}{32}
 >\frac{779}{200}\eta-\frac{25}{8}
 \quad(0<\eta\le1),
```

because the difference is `1/32-eta/50>0`. This proves the printed rate `c=3.895 eta-3.125` by a corrected argument. At `eta=803/1000`, its value is `537/200000>0`; at `eta=9/10`, its value is `761/2000>19/50`. Thus `eta>0.803` and the example `c=0.38` are valid. The number 0.803 is sufficient, not the sharp threshold.

HS-2's limiting criterion is correct. Its numerical demonstrations can be replaced by `e<11/4`: `81(11/4)^3=107811/64<1920` and `4096(11/4)^4=234256<322560`. Monotonicity of `beta^4 e^beta` and `beta^6 e^beta` proves the two asserted ranges. “Limit” here means the limiting exponent for each fixed finite spatial torus; it does not introduce a thermodynamic ground-state limit. The GUIDE thresholds 0.50 and 0.37 repeated later in the source must not be used as universal finite-t thresholds: the positive time correction in HS remains.

## Lemma OS — HOLDS AFTER CORRECTION

The main identity, lines 102–106, holds. Moving the half kernels through the trace replaces one temporal convolution kernel `k_beta` by `d_j r_j chi_j`. Gauge averaging restores the temporal links. This yields exactly the displayed Wilson expectation, including the factor `1/k_beta`. The integrand need not be nonnegative; the trace of the positive operator against a projection makes the integrated answer nonnegative. Summation and the half-integer identity in lines 109–110 also hold.

There is a normalization error at line 111. With the unshifted Wilson partition function Z of line 100, deleting the raw plaquette weight `exp(beta x_p)` gives

```math
 \rho_0=z\frac{Z_{\setminus p}}Z,
 \qquad \rho_j=\rho_0 d_jr_j\,\mathbb E_{\nu}[\chi_j(U_p)].
```

Indeed `1/k_beta=z exp(-beta x)`. For a set S the prefactor is `z^|S| Z_(without S)/Z`. Alternatively define deletion using the normalized weight k, and say so; then the author's partition-ratio notation is correct. The character-ratio formula with the actual probability `rho_0` is unchanged. This is material for interpreting deleted partition functions, but it cancels from Lemma DS's probability ratio.

The frozen-environment interpretation in line 113 holds as a limiting conditional-law statement: if every environment coefficient is d_j, normalization gives `rho_0=1/k_beta(1)` and `rho_j=d_j^2 r_j/k_beta(1)`. It does not identify the finite-coupling Wilson vacuum with that frozen law.

## Lemma DS — HOLDS AFTER CORRECTION

The inequality in lines 115–117 holds, including its product form. Correct the deleted-partition prefactor in line 119 as above. The decisive conditional factorization is valid: a timelike plaquette has exactly one time-zero spatial link, and the stipulated separation excludes two selected links from a spatial plaquette. Periods at least three prevent repeated-link degeneracies. After deleting the selected temporal plaquettes, each selected link meets five remaining plaquettes.

Condition on all other links. Write each selected holonomy as `U_e S_e`, reversing orientation when needed; SU(2) characters are real and invariant under inversion. The remaining exponent is `beta x(U_e A_e)` with A_e a sum of five signed unit quaternions. If A_e is nonzero, write `A_e=rho_e W_e`, with `rho_e<=5`; if it vanishes, use Haar measure. Schur orthogonality gives the conditional character mean

```math
 r_{j_e}(\beta\rho_e)\chi_{j_e}(W_e^{-1}S_e).
```

Its absolute value is at most `d_(j_e) r_(j_e)(5 beta)`. The r_j monotonicity follows from the positive adjacent-ratio representation in `gap-q8test-opus.md:157–176`: the derivative of each tilted mean is its variance. The j=0 term is exactly one, including at zero staple sum. Multiplying the independent conditional means, then integrating and using the corrected OS ratio, proves DS. This argument retains signs of twists and does not assume nonnegative individual characters.

## Corollary DS-1 — HOLDS AFTER CORRECTION

The final constants `0.275` and `0.041` hold. Some intermediate roundings in line 122 do not: for example `U_2(12.5)>0.8198`, since `0.8198^2+(2/5)0.8198-1=-0.00000796`. Also the four printed decimal factors multiply to `0.387718733180128`, not a number below 0.3877. Use these outward rational bounds instead:

| n | Upper bound for U_n(25/2) | u² + 2(2n+1)u/25 − 1 |
|---|---:|---:|
| 1 | 0.888 | 0.001664 |
| 2 | 0.820 | 0.000400 |
| 3 | 0.759 | 0.001121 |
| 4 | 0.703 | 0.000369 |
| 5 | 0.653 | 0.001049 |

The positive quadratic root is U_n, so each bound follows by inspection. The first four bounds multiply to `0.38852942832<0.3886`.

Put `a_n=n^2(5/4)^(n-1)/n!`. For n=5,6,7,8,9,10, upper bounds are respectively `0.50863, 0.15259, 0.03709, 0.00757, 0.00134, 0.000206`, by direct rational multiplication. For n>=10,

```math
 \frac{a_{n+1}}{a_n}=\frac{5(n+1)}{4n^2}\le\frac{11}{80},
 \qquad \sum_{n\ge10}a_n<0.000239.
```

Thus `sum_(n>=5) a_n<0.7075`. For the even-n tail, `a_(n+2)/a_n<=3/176` at n>=10, so `sum_(n even,n>=10) a_n<0.00021` and `sum_(n even,n>=6) a_n<0.1604`. Monotonicity in beta and in spin then gives

```math
 \tau_2<0.7075(0.3886)=0.2749345<0.275,
```
```math
 \tau_{\mathrm{half},\ge5/2}
 <0.1604(0.3886)(0.653)
 <0.161(0.389)(0.654)=0.040959366<0.041.
```

All decimals in these checks are exact terminating rationals. The infinite sums are controlled by displayed geometric bounds.

The additional `tau_2<=0.338` at beta<=2.6 (line 213) also survives. At x=13, use `U_1,U_2,U_3,U_4 <= 0.8914,0.8261,0.7664,0.7122`. Substitution into `u^2+(2n+1)u/13-1` gives positive values in all four cases. Their product is `0.4019413782090432<0.402`. For `a_n=n^2(13/10)^(n-1)/n!`, bounds for n=5 through 10 are `0.595021,0.185647,0.046928,0.009961,0.001821,0.000293`. The ratio after n=10 is at most 143/1000, so the tail from n=10 is below 0.000342. Hence the sum is below 0.840 and `tau_2<0.840(0.402)=0.33768<0.338`. This replaces the unnecessary tighter rounded product in the source.

## Corollary DS-2 — HOLDS AFTER CORRECTION

The plaquette-separated product bound and the displayed unconditional bound at line 126 hold. Summing DS over the indicated spins gives `P(all selected high)<=tau^|S|`, since `P(all selected zero)<=1`. Use **balanced** proper 3-colourings of each coordinate cycle; properness alone does not ensure the stated class sizes. Such a colouring follows by concatenating 123 blocks, with a final 1213 or 12312 for lengths 1 or 2 modulo 3 (the size-three case is 123). This gives each colour at least floor(n/3), hence at least n/5. Together with the direction label, there are 27 classes of size at least N/75.

For a class of size n, put `k=ceil(eta n)`. The event implies a high subset of size k; hence its probability is at most `binom(n,k) tau^k`. The binomial theorem gives `binom(n,k)<=exp(n H(k/n))`; for `eta>=1/2` the exponent decreases as k/n increases when `tau<=1`. This proves line 126 without an omitted polynomial factor. If the claimed bracket is nonpositive, the displayed right side is already at least 27 and the inequality is trivial.

For `eta=4/5`, `tau<=11/40`, the bracket is at least

```math
 \frac15\log\frac{32^4}{5\,11^4}>\frac{53}{100}.
```

For a hand check of the strict inequality, `e^(53/20)=e^3/e^(7/20)<(87/32)^3/(1+7/20+(7/20)^2/2)<100/7<32^4/(5*11^4)`.

Correct the final phrase “for the P_sigma laws multiply by 2.” The factor two applies to the even-conditioned law, or to either numerator **with denominator `Tr(P_+L^t)`**. It does not apply to the odd-conditioned law, whose denominator may be much smaller. The resulting estimate is `54 exp(-0.53 N/75)`, not directly `exp(-cN)` on every small torus. It gives the latter for sufficiently large N after absorbing 54; for example rate `0.53/150` once `N>=150 log(54)/0.53`. HS-1 already supplies its stated pure exponential bound for a>=9. No small-volume pure-exponential constant is supplied by the DS-2 calculation alone.

## Proposition P1 — HOLDS

Lines 166–172 agree with `gap-expose-astra.md:113–151`. On a spin assignment j, a centre flip at edge e is the scalar `(-1)^(2j_e)`. A centre gauge transformation at a vertex is the identity on the gauge-invariant space. It follows that each surviving assignment has an even number of half-integer edges incident to each vertex. They form a Z_2 cycle C, and

```math
 \Theta_\omega\big|_j=(-1)^{\langle\omega,C\rangle},\qquad
 P_-\big|_j=\mathbf1_{\{\langle\omega,C\rangle=1\}}.
```

Since omega is a cocycle, the pairing depends only on the homology class of C. This proves the probability identification without using a signed spin-foam expansion. Summing OS with the centre sign replaces each selected temporal kernel by `k_beta(-g)`; its ratio to `k_beta(g)` is `exp(-2 beta x(g))`. This proves the last equality at line 170. All selected temporal plaquettes are untwisted in the transfer convention; the seam insertion creates the extra twist.

The conclusion concerns the **specified omega pairing**, not simultaneous triviality of the whole three-component homology class. The cycle fact is prior work in EX, not a new discovery in row 860.

## Proposition P2 — HOLDS

Lines 174–179 follow by decomposing the commuting projection into low and high events. Positivity gives the lower bound, and Theorem HS with sigma minus gives the upper bound, with the corrected HS-1 proof retaining the stated c. Dividing by `Tr L^a` yields the exact useful comparison

```math
 0\le p_m(a)-\frac{\operatorname{Tr}(P_-\Pi_{\rm low}L^a)}{\operatorname{Tr}L^a}
 \le e^{-cN}.
```

The admissible geometry is `c_side,d_side in {a,2a}` (`gap-ext-astra.md:77–106`), so `N=3a c_side d_side>=3a^3`. For `b=-(1/2)log eta_*>0`, `e^(-3c a^3)<=e^(-b a)` once `3c a^2>=b`. It is smaller than any fixed polynomial multiple of that exponential for sufficiently large a. Thus (LS) and (E17) are equivalent as existence bounds, allowing a larger prefactor and a larger starting size. They need not hold with identical finite-size constants. This reduction does not weaken the carrying obligation.

## Proposition P3 — HOLDS AFTER CORRECTION

The transfer estimate and OS identity extend to the stated groups, with OS's normalization repair and HS's unchanged even denominator. For finite subgroups, expand `exp(beta chi_V/2)` in tensor characters. Each coefficient is nonnegative, and every irreducible occurs in a tensor power of the faithful self-dual V. Therefore every convolution eigenvalue is strictly positive. The normalized positive kernel is a Markov convolution, so its operator norm is at most one and its trace is `e^beta/z_G`. The Haar mean of x vanishes. These are precisely the properties used by HS. For U(1), the same statements follow from its Fourier series, with `r_n=I_|n|/I_0`. Use a nonempty irreducible set and a supremum r_R, or a maximum where attained.

For U(1), the factorial estimate gives, for positive integer n>=3 beta,

```math
 \frac{I_n(\beta)}{I_0(\beta)}
 \le\frac{(\beta/2)^n}{n!}
 \le\left(\frac{e\beta}{2n}\right)^n
 \le(e/6)^{3\beta}<e^{-\beta}.
```

Here `log(n!)>=integral_1^n log x dx>=n log n-n`; the final inequality follows from `e^4<216`. Apply this to |n|. The complex staple sum also proves the U(1) version of DS, with dimension one and `r_|n|(5 beta)`. These are valid high-charge estimates at sufficiently large time, without a phase conclusion.

Correct the finite-group sentence: the quaternion reduction **does not extend by this proof** to a finite subgroup. Failure to express a staple sum as `rho W` with W in that subgroup does not refute every possible finite-group DS inequality. At a flat environment the conditional coefficient is indeed `r_rho^G(5 beta)`, near one at large beta, but that is not a counterexample to the same bound. Keep the finite-group failure as a failure of this proof step. The decimal 2T example remains GUIDE, not a verified premise.

## By-product B1 — HOLDS AFTER CORRECTION

The displayed trace inequality at lines 216–218 holds. Interpret the unbounded conjugation through its positive trace-class closure Y from HS, or first use finite spectral projections of K. HS steps 3–6 directly bound `Tr(P_sigma Y)`. The inequality still uses `Tr(P_+L^t)` on the right.

The unconditional one-slice exponential moment also has the displayed bound. To see this without incorrectly adding two sector bounds, run the same log-convexity argument with `f(t)=Tr L^t` and the largest eigenvalue of L; its trial-vector lower bound is again `z^N`. It also holds for the even-conditioned law. It does **not** establish that moment for the odd-conditioned law.

The ground-state energy bound has a direct domain-safe proof, avoiding an interchange of an unbounded moment with a low-temperature limit. For any normalized top even eigenvector Omega with eigenvalue lambda>=s=z^N, the eigenvalue equation implies

```math
 K^{-1/2}\Omega=\frac{s}{\lambda}BK^{1/2}\Omega,
 \qquad
 \|K^{-1/2}\Omega\|^2
 \le\frac{s^2\|B\|}{\lambda^2}
       \langle\Omega,K^{1/2}BK^{1/2}\Omega\rangle
 =\frac{s\|B\|}{\lambda}\le e^{\beta N}.
```

Thus Omega is in the needed form domain. Jensen in its spin-projection probability measure gives `sum_e E log(1/r_(j_e))<=beta N`, exactly as claimed for Omega_+.

The sector qualification matters. On the spatial 3-by-3-by-3 torus, every odd winding cycle has at least three half-integer edges. At beta=1/100, `r_(1/2)<=beta/4=1/400`, so every odd-conditioned state has mean electric energy per edge at least `log(400)/27>1/27>beta`. Thus an extension of the ground-state claim to the normalized odd sector would be false. The printed even-ground-state statement is valid.

## Verdict V1: the U(1) argument for filter insufficiency — FAILS

The failure starts at line 187's assertion that the comparison theory shares every relevant input. P3 proves group-blind **high-irrep tail bounds in each group's own labels**. It does not identify those events with the filter's representation.

Read the actual filter in `gap-q8test-opus.md:189–207`: on `H=Sym^5 V`, SU(2) has operator norm `r_(5/2)<=M(beta)`, whereas the restriction to U(1) contains charges `±1,±3,±5` and has norm at least `I_1(beta)/I_0(beta)>M(beta)`. Thus U(1) does **not** satisfy that same bound on that same charged space. On the requested interval this separation has an elementary independent check: `M<= (5/4)^5/720=3125/737280<1/200`, while `I_1/I_0>=beta/(2 e^beta)>43/1080>1/200`, using `e^beta<=e^3<27`. Replacing it by the tail `|n|>=3 beta` discards precisely the low-charge alias which the filter distinguishes. The filter theorem need not be re-proved to see this mismatch between its stated hypothesis and V1's purported comparator.

There are two further independent missing steps in the argument:

- Its cited rigorous leg is about the **Villain Langevin generator**, not the Wilson-cosine transfer's odd flux sector. I read `gap-tu-retry.md:61–102,448–507`: Theorem V concerns Fourier coefficients `exp(-n^2/(2 beta))` and a Poincaré gap; its Wilson extension (W-score) is explicitly open. P3 and the five-staple reduction use the cosine action and Bessel coefficients. These are different measures and different spectral quantities.
- Even masslessness of the matching Wilson model would not, by itself, negate (E17). A bridge to the particular twisted-torus odd-sector fraction is required. For clarity, an abstract family with `L_a=diag(1,exp(-1/a),exp(-1))` and `Theta=diag(1,1,-1)` has a closing even-sector gap but `Tr(P_-L_a^a)/Tr(L_a^a)<=exp(-a)`. This is an elementary illustration of the missing implication, not a Wilson counterexample. The nearby scope note `gap-u1-audit-opus.md:9–28` already warns about analogous geometry and observable bridges; it is credited as prior diagnosis, not adopted as a theorem.

The beta=1.09 comparison is expressly GUIDE and supplies neither a rigorous phase threshold nor a comparison of full trace ratios. At large beta, quantitative low-spin constants also change. An impossibility claim for *every argument using upper kinetic bounds* cannot ignore their values, multiplicities, spatial multiplier and selected representations.

Correct conclusion: HS and DS alone are group-blind tail estimates; P2 leaves (LS) equivalent to (E17). **This note does not prove that the actual filter together with those estimates cannot imply (LS).** It also does not prove that they can. No decision to discard the filter follows from V1.

## V2 and the replacement recommendations — HOLDS AFTER CORRECTION

The limited claim “high-spin exposure is not mandatory for every odd configuration” holds: P1 permits a winding spin-1/2 cycle, and the already cited `gap-q8test-opus.md:277–279` records its transfer/surface realization. This is prior work, not new evidence of typical exposure.

The stronger conclusions at lines 189, 197 and 198 do not follow. A small one-slice marginal density does not bound the probability of visiting that set over an arbitrarily long history, its contribution conditional on winding, or its effect on spectral splitting. The single-seed finite-volume run does not refute every mechanism using such visits. Keep its numbers as unverified GUIDE; do not call them a uniform vacuum theorem or use them to delete a proof route. The same restriction applies to the Z_2 and 2T comparisons in line 229, whose phase inputs are recalled there.

R1 can retain the corrected HS and DS results. R2's instruction to drop the filter is unsupported. R3 can retain only the exact omega-pairing formulation of (E17). The claims that a proof must use a particular fusion identity, must establish percolation, or cannot use any Peierls argument are proposed strategies, not consequences of the checked identities. Comparing a correlated edge law with the independent-bond percolation threshold does not prove percolation.

## Chessboard paragraph, line 200 — FAILS as a stated obstruction

This paragraph is not used by HS, DS or P1–P3. Its last inference equates a one-edge density with an all-edge homogeneous-pattern probability. Even independent edges of density 1/3 have homogeneous-pattern probability `(1/3)^n`; density alone gives no asserted lower bound of order one. Consequently that sentence cannot rule out a chessboard route to (LS). The preceding character-factor observation does not supply the missing homogeneous-pattern estimate or a full reflection-positive representation for every spatial twist. No such extension is established in this check. The first-passage aside at line 214 must also distinguish fixed spin, where `r_j(5 beta)` tends to one, from a spin threshold growing with beta. Its approximate scaling describes a sufficient factorial-majorant choice, not a proved typical-spin law or a uniform first-passage estimate.

## Disposition

The requested finite-lattice inequalities survive with the corrections above. In particular the constants requested in HS-1 and DS-1 remain valid. P1 and P2 identify the existing remaining obligation; they do not solve it. The broad U(1) exclusion of the filter is not sound as written. No mass gap, (E17), (FQ), or first-passage seed is established by this check.

Only this report was changed. The checked source, FINISH, registry, ledgers and audit files were not edited. No GUIDE computation was rerun. Downloads remain in the named fresh scratch directory. The report is local and uncommitted on `check/gap-hs-astra-d29c0aa09`. No external post or push was performed.

RESULT: HOLDS — Theorem HS, HS-2, P1 and P2; HOLDS AFTER CORRECTION — HS-1, OS, DS, DS-1, DS-2, P3, B1 and the limited V2 claim; FAILS — V1's U(1) argument that the filter plus HS cannot force LS, and line 200's chessboard obstruction. The numerical endpoints survive; (E17) remains open. Research check only; no status granted.
