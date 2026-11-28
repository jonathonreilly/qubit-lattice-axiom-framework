Five numbered conclusions hold and two fail as written, (5) and (7): the first failed quantitative inference is (5d), line 228, which identifies convergence at times tending to zero with convergence of the exact zero-time norms.

## Repo search

The lead's `prior/repo-search-2026-11-08.md` concerns row 531, not this target. Its closest mass-gap hit is a one-step nontriviality witness, not this equivalence. `prior/gap-prior.md` identifies the relevant earlier work. I checked these primary passages:

| Source actually read | Finding and closeness |
|---|---|
| `origin/main` at `3b6e5c0baf4295645a07cbfc99813501c8c08c63`, `docs/CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09.md`, 42–118 | The earlier adjoint repair and conditional finite-dimensional temporal bound. This is the finite-dimensional predecessor of (2), not a proof of a positive YM gap. |
| PR #10133, `89faef229ff6e6bde42baad15ed8270c2f4087d8`, `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASSGAP_2606_PRIMARY_ASTRA.md`, 435–525 | L2 gives a conditional fixed-physical-time comparison. L3 already gives dense-class exponential decay ⇒ unique vacuum and a spectral gap, using positive spectral measures. It also separates a nonempty excited sector. This is the earlier substance of (3), credited to that Codex/Astra text; the present check examines the different proof in row 668, not a new derivation of L3. |
| PR #10134, `1e70c7211a2cdbc39001e619f1dd89db45e25851`, this lane's `library/mass-gap-interface.md`, 1–30 | A neutral distinction between a gap, nontrivial dynamics and nonfreeness. It proves no new gap theorem. |
| This pin, `library/cl1.md`, 61–76, 118–199, 275–324 | The conditional Schwinger-function quotient and contraction are already present. Its generator construction uses functional calculus. The abstract generator proof being checked is different. |
| This pin, `library/gap-transfer.md`, notation, Lemmas A0–A3, §§1–3, (6), (8) and their cited proof steps | The fixed-spacing Wilson trace comparison is already present. Its compact spectral theorem is an actual dependency of (7c). Its §8 explicitly leaves the passage from consistent marginals to one cylinder measure to Kolmogorov extension. |

The target-specific prior check does not exist at this pin. Exact searches for this check, mass gap and spectral gap in `open-registry.md`, and for this target in `open-core.md` and `l17c.md`, found no competing check owner. The neighboring TP1-LIMIT and J6 entries concern reconstruction and qualitative clustering, not this check. Existing equivalence results are credited above; no separate attack on their owned results was undertaken. I did not repeat the lead's unrelated PR #10114/#10141 survey.

I used `sa-index/README.md`, neighboring rows of chunks 01 and 23, and the corresponding `obligations.md` entries before opening the source. The outline at `31a47c543775`, lines 25435–25647, already constructs the quotient and contractions under HB1–HB2. Its generator uses spectral calculus at 25610–25621. Lines 588–599 give the polynomial-decay example. Credit: **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text**. Both requested TeX files were fetched once to the prescribed `/tmp` paths. CA-I's 4.12–4.19 index concerns background/stage estimates; no CA-I theorem is a dependency of the checked abstract argument, so no CA-I proof excerpt was needed. No Balaban paper was needed.

## Provenance, scope and verdicts

Checked by Codex, configured high-effort research checker, against `91b0d27e5b21c8e4dcf242bee21ad11209d7db2a`. The checked text is Claude Opus 5.5's `library/gap-os-equiv.md`, all 310 lines. I did not author or edit it. This is research text, not an audit; it grants no status. No numerical calculation, search certificate or computer-assisted proof was used. Commands only retrieved sources and wrote this report.

All unqualified line numbers below refer to that checked file. The count concerns its seven numbered conclusions **in their stated, narrowed settings**, not whether the author fulfilled every part of the original queue request. In particular (6)'s explicit examples calculate correctly, but do not supply the originally requested uniform-full-gap counterexample. The count treats the false constants assertion as part of (5), and its repetition as part of (7). Qualifiers and overstatements outside the actual implications are listed separately.

| Status item | Verdict | First failure or precise qualification |
|---|---|---|
| (1) | **HOLDS** | (1a–d), with the explicitly added P3 and, in continuous time, P4. Reflection positivity and translation symmetry alone do not give all these conclusions. No continuous-time generator is asserted on the lattice. |
| (2) | **HOLDS** | (2a–c), including the centered norms and even-time monotonicity. The spectral version uses Lemma E, whose proof holds. |
| (3) | **HOLDS** | (3a–d): totality of the vacuum plus the class is sufficient; diagonal eventual bounds suffice. This is not a claim that this particular totality condition is necessary for every possible test class. The absolute wording in (3c)(iii) needs the correction below. |
| (4) | **HOLDS** | The measure versions (4a–c), with the stated support conditions. The lattice rate is indeed at least `m/sqrt(d)`. (4d) is a conditional transfer of the reflected-form argument, not an additional completed Schwinger reconstruction or a uniform bound over all rotations. |
| (5) | **FAILS AS WRITTEN at 228** | (5a–c) and their proof hold, including the strong limit theorem without an assumed bound on member constants. But H2 does **not** imply convergence or boundedness of `u_n(F_n,F_n;0)`. Counterexample R1 below. |
| (6) | **HOLDS in its expressly restricted form** | All three displayed constructions and calculations hold, conditional on the Gaussian product-measure import in 6.8. They do not provide a sequence of full gaps bounded below converging on a total fixed class to a gapless datum. The phrases “class changes” and “limit without a gap” misdescribe the examples; see R3. |
| (7) | **FAILS AS WRITTEN** | The first false sentence is at 275: the pairing does not cease to exist on a time torus. The positive-time domain ceases to be preserved. The first false quantitative assertion is at 281: convergence of member zero-time norms again does not follow from H2. The cylinder gap implication itself holds with the limit datum's hypotheses retained. |

The core conclusions surviving this check are the semigroup/spectral equivalence and the passage of a common gap to a reconstructed limit. The defects do **not** give a counterexample to (5a–c), and do not establish a YM gap.

## 1. Step-by-step mathematical check

### 1.1 Forms, quotient and elementary operator lemmas

- **S.1–S.3, A1.1–A1.3 (38–52, 67–71): HOLDS.** The polarization weights match the antilinear-first convention. The choices of `z` in A1.3 have the correct conjugates. Null vectors are orthogonal to the entire space, so the quotient in 1.1 is well defined.
- **S.4 (54–59): HOLDS as a conditional measure instance.** The mirror preserves the measure; the translations preserve the measure and intertwine the mirror; the nonnegative-time sigma-algebra is preserved under forward translation. These give P2 and bounded time orbits by ordinary L2 Cauchy–Schwarz. Strong L2 continuity is an extra assumption supplying P4, not a consequence of bare bimeasurability. Wilson reflection positivity is an imported example, not proved here; see §4.
- **S.5 (61): HOLDS conditionally.** Each finite combination of separated compact positive-time tuples has a common positive mirror gap. Forward translation preserves its internal separations and increases the separation from its reflected copy. CL1's position-independent moment bound therefore gives P3. Its telescoping estimate (6) and C1 translation continuity (7) give P4 on those tuples. The upstream moment/RP hypotheses remain supplied.
- **A2.1–A2.3 (73–77): HOLDS.** The equality is `g_k=<T_{(k-1)h}psi,T_{(k+1)h}psi>`. Cauchy–Schwarz gives log-convexity. A first zero after `g_1>0` contradicts the preceding inequality. Thus `g_k>=g_0(g_1/g_0)^k`. Infinitely many natural indices are unbounded, so taking roots gives the asserted bound. If `rho=0`, the hypothesis itself gives a zero `g_k`, and the zero argument applies. No spectral measure is used.
- **A3.1–A3.3 (87–89): HOLDS.** The graph-of-adjoint argument proves closedness. A lower bound gives closed range; orthogonality to the range puts the orthogonal vector in `ker(A-bar(lambda))`. The adjoint convention is correct. In A3.3, the bounded inverse is positive because `A-mu>=0`; applying the positive-form Cauchy–Schwarz inequality to `varphi_n` and `(A-mu)varphi_n` gives the contradiction exactly as written. This establishes the bottom-of-spectrum fact without a spectral theorem.
- **A3.4–A3.5 (90–91): HOLDS.** Phase rotation makes the mixed matrix element real nonnegative. The parallelogram identity bounds it by the supremum of absolute quadratic forms. Lower bounds at nonreal points and at real points outside the norm interval imply surjectivity by A3(b). Applying A3(c) to `B` and `-B` proves the converse and nonempty spectrum.
- **A3.6 (92): HOLDS with an unstated elementary input.** The polynomial factorization uses the fundamental theorem of algebra. It is not a hidden operator spectral theorem, but it is absent from the claimed list of ingredients. All factors are bounded invertible operators because their roots are outside `spec(B)`. This proves the required spectral inclusion, and A3(d) gives the polynomial norm bound. A short factorization proof is supplied in R4.
- **A3.7 (93): HOLDS.** The two displayed inverse formulas solve the possible unbounded-domain problem: `R` maps all of the Hilbert space into `D(A)`, and the reverse inverse is `I+(1+lambda)(A-lambda)^{-1}`, which is bounded. The string `RD=D(A)` is an undefined-symbol typo; it should be `R K=D(A)`.

### 1.2 Statement (1) and Lemma E

- **1.1–1.5 (105–109): HOLDS.** The iteration uses P3 exactly where needed: `2^{-r} log(1+2^r t)` tends to zero. The zero-norm case is handled before division. Quotient preservation, bounded extension, symmetry, the semigroup law and the vacuum projection identity follow on the dense quotient and extend by continuity. On the lattice only `T_{2t}>=0` is obtained; this is the correct limitation.
- **1.6–1.7 (110–111): HOLDS.** P4 controls both time arguments `s` and `2s`. Uniform contraction extends continuity to the completion. The left difference quotient in 1.7 uses a vector in `D(H)`, and strong continuity plus uniform boundedness justifies its limit. No domain exchange is missing.
- **1.8–1.10 (112–114): HOLDS.** The vector integral exists as an improper norm Riemann integral. Its tail is bounded by `exp(-N)||psi||`. Changing variables yields `H R=I-R`; integration by parts for a domain vector gives `R H=I-R`. Hence `I+H` and `R` really are two-sided inverses on the stated domains.
- **1.11–1.12 (115–116): HOLDS.** `R` is injective by `(I+H)R=I`, and its self-adjointness makes its range dense. Symmetry follows from symmetric difference quotients. For any vector in `D(H*)`, the identity `chi=R(chi+H*chi)` puts it in `D(H)`. This proves self-adjointness, not merely symmetry or essential self-adjointness.
- **1.13–1.15 (117–119): HOLDS.** Positivity follows by differentiating a contraction at zero. Zero generator vectors are invariant by the differentiability already proved. The product `T_{t-s}S_s varphi` is differentiated only for `varphi` in the common generator domain, and its derivative vanishes. Density then gives uniqueness on the entire Hilbert space. The optional lattice logarithm at 102 is not used; it is an explicit functional-calculus aside.
- **E.1–E.2 (135–136): HOLDS.** The vacuum projection commutes with translations and preserves the generator domain. The direct sum `D(H)=C Omega + D(H')` and the adjoint-domain argument prove that `H'` is self-adjoint.
- **E.3–E.6 (137–140): HOLDS.** The factor is correct: `||T_{h/2}varphi||^2<=exp(-mh)||varphi||^2`. The lower form bound excludes both real spectral points below `m` and nonreal points. A3(c) gives the reverse lower bound. Differentiation of the squared norm gives `f'<=-2mf`, and the elementary integrating factor gives the norm bound. The zero-dimensional complement is harmless.
- **E.7–E.11 (141–145): HOLDS.** Direct-sum inversion proves (iii) ⇒ (iv). For the converse, resolvent spectral correspondence gives `spec(R) subset [0,alpha] union {1}`. A3(e) gives `||R^k-R^{k+j}||<=alpha^k`; completeness of bounded operators gives a norm limit `P`. Norm-continuity of multiplication proves `P^2=P` and `RP=P`. The invariant-vector hypothesis identifies its range as exactly `C Omega`. Therefore `||R|Omega-perp||<=alpha`, excluding zero even as a non-eigenvalue spectral point of `H'`. This is an elementary polynomial argument; it does not import a spectral projection theorem.
- **E.12 (146): HOLDS.** The lattice conclusion is a bound on the absolute spectral radius of the self-adjoint transfer contraction. A negative eigenvalue of large modulus would violate it. The result is not a lattice logarithm construction.

The extra hypotheses in (1) are real. With the ordinary inner product on `C^2`, vacuum `e_0`, and `tau_t=diag(1,exp(t))`, P1, P2 and P4 hold but contraction fails; P3 fails. With `T_0=I` and `T_t=P_Omega` for every `t>0`, P1–P3 hold but strong continuity fails on `Omega-perp`; P4 fails. These are hand-checkable abstract data, not physical models. A reversible two-state chain that swaps the states has a site-reflection-positive path datum, but its one-step operator has eigenvalue `-1`; a nonnegative self-adjoint Hamiltonian cannot exponentiate to that operator. Thus the qualifications of (1c–d) must stay.

### 1.3 Statements (2), (3) and the small class

- **2.1–2.3 (159–161): HOLDS.** The vacuum subtraction places both vectors in the centered space. At even time the diagonal form is a squared norm. For a past observable `A`, `F=overline(Theta A)` has reflected conjugate `A`, so the complex conjugation is correct. Reflection invariance and L2 Cauchy–Schwarz give `||Q[F]||^2<=E|A|^2-|EA|^2`. This avoids the earlier repository adjoint-placement error.
- **2.4 (163): HOLDS as a scope/cross-reference remark.** Once the semigroup and its bound are given, no new growth or rotation estimate is used.
- **3.1–3.6 (176–181): HOLDS.** Even-time diagonal bounds give eventual norm bounds for each class vector. A finite sum has the same exponent by the triangle inequality, without requiring estimates on mixed pairs or a uniform class constant. A2 removes the vector-dependent constant on that finite sum. Taking the closure gives (3a). The decomposition `[F]=Q[F]+b(1,F)Omega` proves the exact stated equivalence of totality conditions. Invariance of `K_C` is not required for this argument.
- **K.1–K.4 (184–187): HOLDS.** Row sums and reversibility give compatible finite path weights. Reversing the past factors makes past and future conditionally independent given `x_0`. The reflected form is exactly the L2(pi) Gram form of conditional expectations. Functions of `x_0` exhaust L2(pi), so this is the whole reconstructed space, not just a subspace. Conditional summation gives `T=P`; Jensen and stationarity make it a contraction. No infinite product measure is needed for this datum.
- **3.7–3.10 (190–193): HOLDS by direct calculation.** The orthonormal sign basis has eigenvalues `1,1-2p,1-2q,(1-2p)(1-2q)`. For the B-only class the centered conditional expectation is `c_F b`, so `u(F,F;t)=|c_F|^2(1-2q)^t`. At `p=0,q=1/2`, `a` is a nonvacuum invariant vector and both other centered eigenvalues vanish. At `0<p<q<=1/2`, the full decay exponent is `-log(1-2p)`, strictly smaller than the B-class exponent. These examples establish failure of a general inference from an arbitrary non-total class.
- **3.11 (195): the polynomial example is correct; “gives nothing” is too strong.** `integral_0^infinity E exp(-(1+t)E)dE=(1+t)^{-2}`, by integration by parts, and the density is positive on every interval above zero. It rules out inference of a positive gap from polynomial decay. Decay to zero on a total class does imply uniqueness of the invariant vacuum: if `eta` is invariant and orthogonal to the vacuum, then `<eta,Q[F]>=<eta,T_t Q[F]>`, while the even-time diagonal decay makes `||T_t Q[F]||` tend to zero. Totality forces `eta=0`.

Totality of the original class is a sufficient certificate, not a minimal necessary test. Indeed (3a) extends to the closed time-translation span of `Q[C]`: for fixed `s`, `||T_t T_s Q[F]||<=C_F^(1/2) exp(-m(t+s))` for all large `t`; finite sums and A2 give the sharp bound on their closure. For example, on a three-dimensional space with eigenvalues `0,m,2m`, the single vector `F=e_1+e_2` is not total with the vacuum, but `F` and `T_sF` span both excited vectors for `s>0`, since `exp(-ms) != exp(-2ms)`. The blanket wording “Nothing beyond (3a) follows” should say only that a global gap does not follow for an arbitrary non-total class. This does not invalidate the sufficient condition or its counterexample.

### 1.4 Directions and rates

**4.1–4.6 (209–214): HOLDS, with the trivial zero-displacement case supplied here.** If v=0 under the stated separation condition, r=0, and ordinary covariance Cauchy–Schwarz proves the bound directly. Otherwise the division by |v| in 4.5 is legitimate. The Householder reflection has `Re=e_d`, including the antiparallel case; the parallel case uses the identity. Localization covariance places the two observables on opposite half-spaces. Invariance preserves expectations and variances. The two radius shifts cost exactly `2r`, not `r`. On the lattice, a signed coordinate permutation suffices for each axis, and the transverse displacement does not change the selected coordinate interval. Hence

`|Cov(A,tau_v B)| <= exp(2mr) sigma_A sigma_B exp(-m ||v||_infinity)`

when `||v||_infinity>=2r`. Since `|v|^2=sum_i v_i^2<=d ||v||_infinity^2`, this gives the asserted rate `m/sqrt(d)`. In the remaining bounded region, ordinary covariance Cauchy–Schwarz gives `|Cov|<=sigma_A sigma_B`; the same weaker bound `exp(2mr-m|v|/sqrt(d)) sigma_A sigma_B` still holds because `|v|/sqrt(d)<=2r`. In four dimensions the resulting rate is `m/2`. No claim of optimality follows.

For (4d), let `g` include the rotation and the shifts used to separate the tuples. Define `A'=g A`, `B'=g B`, and `F'=overline(theta A')`. Invariance identifies the desired connected function with `u(F',B';s)`. Its bound is exactly `exp(-ms)||Q[F']|| ||Q[B']||`. Both norms must appear, and the assumed Schwinger domain must contain the separated reflected concatenations. The abstract argument proves this fixed-motion bound. It supplies neither moments for that domain nor a uniform estimate over different motions. A per-ball moment bound is a sufficient source of such an estimate, not a logically necessary unique mechanism.

## 2. The limit theorem: failure and complete repair

### R1. H2 does not control the exact zero-time norms

Fix `m>0` and let `n>=1`. On `V_n=C^3` use its usual inner product, `1_n=e_0`, and

`tau_t^(n)=diag(1, exp(-mt), exp(-(m+n^2)t)), t>=0`.

This is a datum satisfying P1–P4; its generator is the displayed nonnegative diagonal matrix. Its full centered space has gap exactly `m`, so H1 holds with `S_n=Omega_n-perp`. Let the limit datum be `V_infinity=C^2`, vacuum `e_0`, and `tau_t=diag(1,exp(-mt))`. Set `C={F=e_1}` and `iota_n F=e_1+exp(n)e_2`. The limit class plus the vacuum is total. Direct calculation gives

`u_n(iota_n F,iota_n F;t)=exp(-mt)+exp(2n-(m+n^2)t)`.

For each `t>0` choose `t_n=t`. The second term tends to zero, giving `u_infinity(F,F;t)=exp(-mt)`. At `t=0`, H2 permits `t_n=3/n`; then

`u_n(iota_n F,iota_n F;3/n)=exp(-3m/n)+exp(-n-3m/n) -> 1=u_infinity(F,F;0)`.

All times are in `2 R_+=R_+`, and `t_n->0`. Thus **every hypothesis of (5), including H2 at zero and limit totality, holds**. Nevertheless

`||Q_n[iota_n F]||^2=u_n(iota_n F,iota_n F;0)=1+exp(2n) -> infinity`.

Any constant bounding these functions by `C_n exp(-mt)` for every `t>=0` is at least `1+exp(2n)`. Even requiring all `t>0` with no common positive lower cutoff has the same consequence, by continuity at zero for each member. This refutes the constants assertion, not the limit gap theorem. It is an abstract RP datum in the exact domain of (5); no probabilistic realization or numerical test is needed.

### R2. The valid stronger theorem, with all limit steps

Write `u_n(t)=u_n(iota_n F,iota_n F;t)`. H1 and the centered semigroup identity give, for even member times `v>=w`,

`0<=u_n(v)<=exp(-m_n(v-w))u_n(w)`.

Fix limit times `0<=s<t`. Choose the sequences `s_n,t_n` supplied by H2 for these two times and this one F. They need not agree with sequences used for another pair of times. For large n they are ordered. For `0<epsilon<min(m,t-s)`, eventually

`u_n(t_n)<=exp(-(m-epsilon)(t-s-epsilon))u_n(s_n)`.

Take the limit, then let epsilon decrease to zero. This gives

`0<=u_infinity(t)<=exp(-m(t-s))u_infinity(s)`.

Equality handles `s=t`. Nonnegativity also follows directly from the limit datum. Crucially, at `s=0` the proof uses `u_n(s_n)`, not `u_n(0)`. The limit value is nevertheless `u_infinity(0)=||Q_infinity[F]||^2`. Thus (5a) follows exactly as stated. Applying the checked argument 3.1–3.4 proves (5b); totality and Lemma E prove (5c). This completes the repair without strengthening H2.

If one wants bounded **member** zero-time constants too, add the explicit condition

`u_n(iota_n F,iota_n F;0) -> u_infinity(F,F;0)` for each F.

The sequence is then bounded because every convergent scalar sequence is bounded. This is stronger than the present H2. Alternatively, convergence only at positive limit times still proves the displayed monotonicity for `t>=s>0`; fixing such an s gives an eventual exponential bound and then (3) recovers the sharp limit norm bound. Its provisional constant `exp(ms)u_infinity(s)` initially applies only for `t>=s`.

**5.1–5.4 and 5.5 (231–236): HOLDS.** In 5.2 the displayed estimate is used only for small positive epsilon as above. Reflection positivity/self-adjointness prevents a slower limiting exponential or a nonvacuum invariant component on the controlled total class. Attempts to use the paper's examples fail for exact reasons: 6a-1 loses the common full-space rate, and 6a-2 loses reflection positivity. R1 does preserve all the hypotheses and gives unbounded member constants, but its limit still has gap m. There is consequently no counterexample to the strong gap conclusion within these hypotheses.

## 3. Examples and finite volumes

### R3. What the examples actually establish

**6.1–6.5 (247–251): HOLDS; the description needs correction.** Each finite-path expectation is a finite sum of products of transition probabilities, hence a polynomial in q. The eigenvalues on the centered space are `1/2,1-2q_n,(1-2q_n)/2`. Because `0<q_n<1/4`, their maximum is `1-2q_n`, so the full gaps are positive but tend to zero. The A-only class and its embeddings are fixed, not changing; their centered space is the same one-dimensional eigenspace for every n and for the limit. It has exponent log 2 throughout, but misses the limiting invariant B-spin. This is a failure of **limit totality for the uniformly controlled class**, not an example of uniformly positive full gaps. It cannot refute (5).

**6.6–6.9 (254–257): all calculations HOLD.** For `|t|<n`, both factors of `c_n(t)` are at most one, while `exp(mu(n-|t|))>=1`; outside that interval the covariance is zero. This proves the displayed exponential upper bound. For the Gram factorization, the k-sum is

`sum_{k<=min(s,t)} r^(s+t-2k)=r^|s-t|/(1-r^2)`.

The j-intersection has exactly `(n-|s-t|)_+` integers. Their product with `(1-r^2)/n` is `c_n(s-t)`, and the diagonal sum is one. Thus the weights in 6.7 are correct, including their indicator and normalization. Given a countable independent Gaussian family, square summability gives an L2 limit and the covariance claimed. Finite linear combinations are Gaussian: their finite partial sums have Gaussian characteristic functions, and L2 convergence passes those characteristic functions to the limit. Time shifting merely reindexes the independent Gaussians, proving stationarity.

The two reflection failures have explicit negative vectors, not just a formal determinant test. At the site mirror use `F=X_1-c_n(1)X_0`. Its reflected square is

`c_n(2)-c_n(1)^2=-r^2/n^2<0`.

For the link form use the coefficient vector `(-c_n(2)/c_n(1),1)`. Since `c_n(1)>0`, its reflected square is

`c_n(3)-c_n(2)^2/c_n(1)=-r^4/(n^2 c_n(1))<0`.

These formulas hold also at n=3, when `c_n(3)=0`. Thus neither reflection is positive. The limit is `r^|t|`, with positive rate `lambda=-log r`; it violates a prescribed bound with any rate `mu>lambda` because `r^t exp(mu t)=exp((mu-lambda)t)` is unbounded. It is **not** an example of a limit with no positive decay rate. The members have no OS gap in the stated reflection datum at all. This example diagnoses loss of a prescribed rate when RP is absent, rather than loss of an OS gap through large constants alone.

**6.10–6.14 (260–264): HOLDS.** Reversibility follows from the symmetric lazy-walk matrix. The root-of-unity sum is zero for distinct k,l because it is a geometric series with ratio different from one and ratio-to-the-N equal to one. Thus the N Fourier vectors form an orthonormal basis. Applying P gives the displayed eigenvalues `cos^2(pi k/N)`. Among k=1,...,N-1, the largest is attained at k=1,N-1; both lie strictly below one for N>=3. This proves the exact full gap and its positivity. For N>=4, put `x=pi/N<=1`, `y=x^2/2<=1/2`. Twice integrating `1-cos x>=0` gives `cos x>=1-x^2/2`; also

`-log(1-y)=integral_0^y (1-z)^(-1) dz <= y/(1-y)<=2y`.

Hence `-2log cos x<=2x^2`. The coefficient of `1_{0}` on each Fourier vector is `1/N`; removing the constant leaves the stated sum, with the two lowest modes giving the lower bound. All arithmetic is by hand.

This example has a further scope limit. For any fixed finite set of spatial sites and times, the probability that any corresponding occupation variable is one is at most the number of those variables divided by N. Thus its local field limit is the deterministic empty field. The example proves finite-volume gap collapse; it does not construct a nontrivial gapless infinite-volume theory. The free massless example mentioned in 6.15 is not supplied. Its spatial zero mode must in particular be specified: for an unrestricted noncompact massless scalar on a spatial torus it prevents the claimed positive full-space gap/normalizable stationary vacuum. Removing that mode would be an additional definition. “The same content” is too broad.

### 3.1 Statements (7a–f), individually

| Clause | Check and repair |
|---|---|
| (7a), 273; 7.1, 286 | **HOLDS as a conditional theorem.** The abstract proofs use only the time datum. P4 is required only in continuous time for the Hamiltonian assertion. The particular Wilson cylinder *measure* is not built in the cited `gap-transfer.md`: its (8e) explicitly leaves Kolmogorov extension unproved. Its consistent slab expectations are built. Distinguish these. |
| (7b), 274; 7.2, 287 | **HOLDS as a statement that the directional implication is unavailable in general.** An orthogonal map descending to the cylinder must preserve the rank-three period lattice and therefore its span; it cannot exchange its orthogonal time axis with a spatial axis. Periodicity makes any spatial connected correlation repeat after ell. For an explicit obstruction, put one stationary reversible two-state spin process, with eigenvalue r in (0,1), identically at every spatial point. K.3–K.4 give its time RP and time gap `-log r`, while the equal-time spatial covariance of the spin is identically one. Thus a time gap alone gives no spatial exponential decay theorem on this class of cylinders. This does not say that every covariance in every cylinder is nonzero. |
| (7c), 275; 7.3, 288 | **FAILS in the first explanation; the restricted trace bound holds.** Bounded or L2 pairings exist for every translation on the torus by Cauchy–Schwarz. What fails is preservation of the chosen half-period localization domain by all forward translations. The cited trace estimate has the hypotheses and lattice units specified below. It does not prove that this particular trace-tail bound is a necessary condition for every possible comparison. |
| (7d), 276–281; 7.4, 289 | **Gap implication HOLDS; constants assertion FAILS at 281.** Retain P1–P3 for the limit datum, as in (5), H2 and limit totality. Apply R2. The requirement that observables in the one fixed W be total is a separate strong hypothesis; mere locality or embedding of W does not prove it. R1 refutes the claimed consequence about member norms. With exact-zero convergence added, those norms are bounded. |
| (7e), 282; 7.5, 290 | **HOLDS conditionally.** A time gap is a statement about the time generator alone. Applying (4) in the limit requires that limit's localization covariance, symmetries and RP datum; no finite-cylinder rotation can supply the missing exchange of time and space. The hypercubic Euclidean-distance rate is m/2. No existence or rotation theorem for the limit is proved here. |
| (7f), 283; 7.6, 291 | **HOLDS.** If sector gaps failed to tend to zero, some epsilon>0 would occur as a lower bound along an infinite subsequence (or use epsilon/2 if a best rate is defined only as a supremum). H2 persists along that subsequence. R2 and (3a) then give `\|\|T_t eta\|\|<=exp(-epsilon t)\|\|eta\|\|` for the nonzero invariant eta in the limiting controlled span, a contradiction at any t>0. No full-space totality is needed for this contrapositive. |

For the source comparison in (7c), the actual inputs are: fixed SU(2) Wilson lattice, spatial `N>=3`, positive finite beta, bounded measurable gauge-invariant **single-slice** A,B, integer time separation `k>=0`, integer period `T>=k+2`, and the positive trace-class transfer operator with simple normalized top eigenvector. Its nonvacuum eigenvalue ratios satisfy `0<=rho_j<1` and are summable. These are the hypotheses supplied by `gap-transfer.md` §§1–5; its §6 then gives

`|<A_0 B_k>_T-<A_0 B_k>_infinity| <= 2||A||_infinity||B||_infinity sum_{j>=1} rho_j^(T-k)`.

Checking that source's calculation: put `G_j=lambda_0^(-k)<phi_j,M_A T_P^k M_B phi_j>`, so `|G_j|<=M=||A||_infinity||B||_infinity`. The trace ratio is `(G_0+sum_{j>=1}rho_j^(T-k)G_j)/(1+sum_{j>=1}rho_j^T)`. Subtracting G_0 bounds its modulus by `M sum rho_j^(T-k)+M sum rho_j^T`, which is at most the displayed right side. Absolute convergence follows from summability and `T-k>=2`. This verifies the imported comparison, with all its hypotheses; it is not a new transfer-operator construction.

If L and t denote physical times at spacing a, write `L=Ta`, `t=ka` and use the exponent `(L-t)/a`. This change of units is exact. What remains unproved is a useful **uniform estimate** on that trace tail as spacing and spatial volume vary. For general slab observables the source's §8 gives a different formula with the slab width; a two-single-slice theorem cannot silently be applied to arbitrary slabs or winding observables. Converting raw correlations to truncated ones additionally uses convergence of both one-point functions (the same source covers the single-slice one-point case).

## 4. Imported facts, unproved assertions and the spectral-theorem claim

The phrase “the only cited, not rebuilt, fact” at 304 is false. Here is the dependency inventory; a reference credited only for history is distinguished from an input.

| Use in checked text | Exact fact supplied elsewhere; reading/verification boundary |
|---|---|
| 25–28, 163, 195: earlier repo comparisons | The finite-dimensional gap-to-temporal-decay lemma, L3's dense-class converse, and the compact Wilson variants. These are historical predecessors, not missing steps of the new abstract proofs. The relevant primary statements were read as listed in Repo search. Absence from `git branch -r` did not make the PR #10133 source inaccessible. |
| 58; the Wilson part of 61 | Site/link reflection positivity of the appropriate Wilson states. CL1 Lemma 3 proves inheritance for limit functionals; its **I2 at 61** imports the lattice statement from LG1. `gap-transfer.md` §1 gives trace identities, not a standalone proof of RP for all the infinite-volume states mentioned here. This instance is conditional on that upstream fact. |
| 61, 206, 296: Schwinger instance | CL1's position-uniform moment bounds, normalized symmetric real translation-invariant limiting functional, RP on every finite combination, and continuity on separated tests. CL1 I1–I3 remain conditional on its actual-construction estimates. The cited local deduction of P1–P4 was checked, not those upstream YM estimates. The per-ball moment bound invoked in (4d) is a supplied sufficient uniform estimate. |
| 92: A3(e) | Complex polynomial factorization, implicitly the fundamental theorem of algebra; not proved in the checked file. R4 below supplies a hand proof of the exact fact needed. |
| 102: optional lattice logarithm | Measurable functional calculus defines the densely defined self-adjoint `-a^(-1)log T` when T is a positive injective contraction. This is explicitly not used in any subsequent proof. Its existence is not proved in the file. |
| 119 | Positivity of the Wilson transfer operator through the factorization `T_P=(R* M P)*(R* M P)` in `gap-transfer.md` 3.3. That factorization uses its convergent Gram expansion and Hilbert–Schmidt calculation, which were read. It is an external-to-this-file instance, not needed by abstract (1d). |
| 256: Gaussian realization | Existence of a countable independent family of standard Gaussians, from countable product measure; then completeness of L2 and Gaussian characteristic functions. The product-measure theorem is explicitly not rebuilt. The covariance-sequence counterexample and its RP failures need no probability-space existence theorem. |
| 266 | A positive full Gaussian/Fock-space gap for a finite spatial torus, after an appropriate zero-mode convention, and its order `1/N`. No proof or adequate field/zero-mode specification is supplied. It is not an established example in this file. |
| 273 | Existence of a cylinder probability measure from consistent Wilson slab distributions. `gap-transfer.md` (8e) names Kolmogorov extension and explicitly says it is not rebuilt. Thus calling the slab family a constructed measure adds an unproved step. |
| 275, 288 | The single-slice finite-time-torus/cylinder trace comparison. The source uses its compact positive-operator spectral theorem, trace-class calculus, and simple ground state. Their relevant statements and the comparison proof were read; the comparison's hypotheses are given in §3.1 above. |
| 30: outside historical references | Osterwalder–Schrader, Glimm–Jaffe, Hille and Yosida are marked not read and are not invoked as missing steps in §§1–5. The Sussman–Alpoge polynomial example is used at 195; its exact outline version was read and its integral checked. No verification of the separate YM4_1400 line attribution is claimed. |

Elementary background also includes Hilbert completion, bounded-operator completion, orthogonal complements, Cauchy–Schwarz for ordinary Hilbert/L2 spaces, real/complex elementary calculus and finite-dimensional linear algebra. These are not all rebuilt from axioms. No analytic semigroup theorem, Stone theorem, Hille–Yosida theorem, projection-valued spectral theorem, or logarithmic functional calculus is needed for **the proofs of (1a–c), Lemma E, and (2)–(5)**.

However, **“No spectral theorem is used” for the entire file is false**. The comparison in (7c) imports an eigenbasis expansion from `gap-transfer.md`, whose Lemma A2 is explicitly a spectral theorem for compact positive operators. It is proved there, not secretly assumed in the generator argument. The accurate distinction is: no general spectral theorem in the abstract equivalence proof; a proved compact spectral theorem in the cited thermal comparison.

### R4. Complete proof of the polynomial factorization used in A3.6

Let p be a nonconstant complex polynomial. Its leading term implies `|p(z)|->infinity` as `|z|->infinity`, so continuity on a sufficiently large closed disk gives a global minimizer z_0 of `|p|`. Suppose `a_0=p(z_0)!=0`. Write

`p(z_0+w)/a_0=1+c w^k+sum_{j>k} c_j w^j`,

where k>=1 is the first nonzero coefficient and c!=0. For any small positive rho choose w with `c w^k=-rho`; explicitly choose its modulus `(rho/|c|)^(1/k)` and an argument whose k-fold multiple is `pi-arg(c)`. For `|w|<=1`, the remaining finite sum has modulus at most `C |w|^(k+1)`, with `C=sum_{j>k}|c_j|`. Choose `0<rho<1` small enough that this is at most rho/2. Then

`|p(z_0+w)/a_0|<=1-rho+rho/2<1`,

contrary to minimality. Therefore p has a root. Division by its linear factor is exact polynomial division and lowers the degree by one. Induction factors p completely over C. Applying this to `p(x)=q(x)-nu` supplies exactly the factorization in A3.6. This proof uses only compactness/continuity and elementary polar coordinates, not an operator spectral theorem.

## 5. Overstatements and exact corrections

The defects fall into six groups: moving-zero-time convergence (R1–R2); overbroad class/decay wording; misleading example labels and the unconstructed free-field example (R3); time-torus domain, units and measure existence; unacknowledged imports/spectral-theorem wording; and overly general claims of necessity of moment bounds. No correction to the checked file was applied.

In this table, replace the **quoted substring** at the given line; where a full sentence is quoted, replace that entire sentence. Mathematical content of the repairs is proved above. Pure scope changes withdraw unsupported assertions; they do not claim to prove the withdrawn result.

| Line | Old words | Exact new words |
|---|---|---|
| 4 | `and the bounded constants of the row follow from the convergence` | `and bounded member zero-time constants follow only if exact-zero-time convergence is added to (H2)` |
| 4 | `No spectral theorem is used.` | `The abstract equivalence proof uses no general spectral theorem; (7c) imports the compact spectral theorem proved in gap-transfer.md.` |
| 4 | `(the class changes; the members are not reflection positive)` | `(the uniformly controlled class is not total in the limit; the members are not reflection positive)` |
| 25 | `` The branch is not in this checkout (`git branch -r` lists no such branch), so its file was **not read** and its hypotheses could not be checked. `` | `The author did not read that primary file. The checker fetched PR #10133 at 89faef229ff6e6bde42baad15ed8270c2f4087d8 and read MASSGAP_2606_PRIMARY_ASTRA.md, lines 435–525; L3 is the earlier conditional dense-class converse.` |
| 28 | `so that no step of this file uses the spectral theorem.` | `without a general spectral theorem in the abstract proof; the thermal comparison in (7c) separately uses the compact spectral theorem of gap-transfer.md.` |
| 30 | `Every step below is proved here; nothing from these sources is a step.` | `The abstract equivalence proofs below are supplied here. The cited instances, Gaussian realization and thermal comparison retain the external inputs listed in gap-os-equiv-check.md, section 4.` |
| 32 | `Every statement below is proved with Hilbert-space arguments only: Cauchy-Schwarz, completion, Riemann integrals of continuous vector functions, and the definition of the spectrum.` | `The abstract results (1)–(5) use Hilbert-space arguments and elementary calculus; A3.6 also uses complex polynomial factorization. The cited thermal comparison (7c) uses the compact spectral theorem proved in gap-transfer.md.` |
| 58 | `` `library/cl1.md` Lemma 3; `gap-transfer.md` section 1 for the torus with a finite time circle `` | `` `library/cl1.md` input I2 imports the lattice assertion from LG1; its Lemma 3 passes it to limit functionals. `gap-transfer.md` section 1 supplies finite-time trace identities `` |
| 92 | `write $q(x)-\nu=c\prod_{i=1}^k(x-z_i)$, $c\ne0$.` | `By complex polynomial factorization, proved in gap-os-equiv-check.md R4, write $q(x)-\nu=c\prod_{i=1}^k(x-z_i)$, $c\ne0$.` |
| 93 | `$\varphi\in RD=D(A)$` | `$\varphi\in R\mathcal K=D(A)$` |
| 172 | `Nothing beyond (3a) follows when $\mathcal K_{\mathcal C}\ne\Omega^\perp$: Example (3d).` | `For an arbitrary class with $\mathcal K_{\mathcal C}\ne\Omega^\perp$, these hypotheses need not imply the full gap: Example (3d). Totality is sufficient, not necessary for every possible class; the same bound also extends to its closed time-translation span.` |
| 195 | `Polynomial decay on a total class gives nothing:` | `Polynomial decay to zero on a total class excludes additional invariant vectors, but gives no positive lower spectral bound:` |
| 206 | `the same steps give the bound with the constant $\|Q[R\cdot F]\|$ of the rotated tuple.` | `the same steps, on the admissible separated test domain, give $e^{-ms}\|Q[F']\|\|Q[B']\|$, where $A'=g\cdot A$, $B'=g\cdot B$, $F'=\overline{\theta A'}$, and $g$ is the rotation and translation used to place the tuples on opposite sides of the time mirror.` |
| 206 | `a bound uniform over $R$ needs a moment bound per ball` | `a moment bound per ball is sufficient to control these norms uniformly over $R$` |
| 213 | `(4b). Let` | `(4b). If $v=0$, then $r=0$ and covariance Cauchy–Schwarz proves the bound. Otherwise let` |
| 214 | `For the box form, take` | `If $v=0$, then $r=0$ and covariance Cauchy–Schwarz proves the box bound. Otherwise, for the box form, take` |
| 228 | `The row's hypothesis "constants bounded along the sequence" is a consequence, not an input: by (2a) the member constant can be taken to be $\|Q_n[\iota_nF]\|^2=u_n(\iota_nF,\iota_nF;0)$, which converges by (H2) at $t=0$.` | `The member constant in (2a) can be taken to be $\|Q_n[\iota_nF]\|^2=u_n(\iota_nF,\iota_nF;0)$. These constants need not be bounded under (H2), since at $t=0$ that hypothesis allows positive $t_n\to0$. They converge, and hence are bounded, if exact-zero-time convergence is added. None of these extra bounds is needed for (5a)–(5c).` |
| 228 | `with the constant $e^{ms}u_\infty(F,F;s)$.` | `with the constant $e^{ms}u_\infty(F,F;s)$ for $t\ge s$; statement (3) then gives the sharp limit norm bound.` |
| 241 | `*Gaps bounded below, limit without a gap.*` | `*Limits and the hypotheses needed for a common gap or decay rate.*` |
| 241 | `In particular unbounded constants never cause it when the members are reflection positive (5d).` | `Under the full limit-datum, common-rate and total-class convergence hypotheses of (5), unbounded member constants cannot destroy the limiting gap.` |
| 242 | `*The class changes.*` | `*A fixed controlled class is not total.*` |
| 243 | `*The constants are not bounded, members not reflection positive.*` | `*Unbounded constants and loss of a prescribed decay rate without reflection positivity.*` |
| 266 | `For the free massless lattice field on $(\mathbb Z/N)^3\times\mathbb Z$ the same mechanism (lowest nonzero momentum $2\pi/N$) gives a gap of order $1/N$.` | `A free massless lattice-field example is not established here; it requires an explicit field definition, treatment of the spatial zero mode, and a proof of the full reconstructed spectral statement.` |
| 266 | `Example (6b) has the same content with every step finite.` | `Example (6b) proves finite-volume gap collapse with every step finite; its local occupation-field limit is the deterministic empty field, so it does not construct a nontrivial gapless infinite-volume field.` |
| 273 | `the cylinder measure is its slab family (8).` | `its (8) constructs consistent cylinder slab expectations; a probability measure realizing that family additionally uses the Kolmogorov extension theorem, explicitly left unrebuilt in its (8e).` |
| 275 | `the reflected pairing $b(F,\tau_tG)$ exists only while the supports fit in half a period` | `the reflected pairing exists for every translation of bounded or L2 observables, but the chosen half-period localization domain is not preserved by all forward translations` |
| 275 | `` At fixed lattice spacing, `gap-transfer.md` (6a) gives the exact comparison `` | `At fixed lattice spacing $a$, for the SU(2) Wilson operator with $N\ge3$, $\beta>0$, and bounded measurable gauge-invariant single-slice $A,B$, let $L/a$ and $t/a$ be integers with $L/a\ge t/a+2$. Then gap-transfer.md (6a) gives the comparison` |
| 275 | `\rho_j^{L-t}` | `\rho_j^{(L-t)/a}` |
| 275 | `So a statement on the cubic tori transfers to the cylinder only together with a bound on that sum, i.e. on the thermal weight of the excited states at time $L-t$.` | `This estimate transfers the corresponding raw single-slice correlations if its right side tends to zero; truncated correlations also require the one-point comparisons. A suitable bound on that trace tail is sufficient for this route, not a proved necessary condition for every comparison.` |
| 275 | `A version in physical units, uniform in the spacing, is **not proved** here.` | `The conversion to physical units is exact; a useful estimate of the trace tail uniform in the spacing is **not proved** here.` |
| 276 | `let $\mathfrak D_\infty$ be the infinite-volume datum.` | `let $\mathfrak D_\infty$ be an infinite-volume datum satisfying (P1)–(P3), as required in (5).` |
| 281 | `which converges by the convergence hypothesis.` | `which need not converge under (H2); its convergence follows if exact-zero-time convergence is separately assumed.` |
| 281 | `it is an input of the existence of the limit, not of the transfer of the gap.` | `it is one sufficient compactness input for constructing the limit, not an additional hypothesis of the gap-transfer implication once that limit datum and (H2) are given.` |
| 304 | `**Proved, by hand, from the listed properties only:**` | `**Proved, by hand, from the listed properties and the explicitly retained mathematical imports:**` |
| 304 | `The only cited, not rebuilt, fact is the existence of a countable independent Gaussian family in 6.8, and the counterexample (6a-2) does not need it (6.8, last sentence).` | `Cited inputs also enter the Wilson and Schwinger instances, the cylinder-measure existence claim and the thermal comparison; see gap-os-equiv-check.md, section 4. The explicit covariance-sequence counterexample (6a-2) needs no Gaussian realization.` |
| 306 | `uniform moment bounds remain needed to construct the limit.` | `uniform moment bounds are one sufficient input to the chosen limit construction; no universal necessity statement is proved here.` |

The statements in §8 comparing names and assertions of `gap-skeleton.md` are not independently verified by this check. In particular, statements that a particular construction supplies totality, or that a particular moment bound is necessary for its existence proof, must remain references to that plan's own hypotheses. This report does not judge that plan.

## 6. Every use of a name from gap-skeleton.md

Listed only, without judging the plan:

| Line | Occurrence |
|---|---|
| 12 | `gap-skeleton` row 662; `gap-skeleton-max` row 669. |
| 19 | `library/gap-skeleton.md`, sections 0–2; names `(G-ell)`, `(G-inf)`; §8 comparison. |
| 30 | `gap-skeleton.md` §1.1 as the intermediary for the Sussman–Alpoge example. |
| 206 | `gap-skeleton.md` §1.2; `(c)(2)`. |
| 282 | `gap-skeleton.md` §1.4, `(J2)`. |
| 293 | Section heading naming `gap-skeleton.md` §1. |
| 295 | `(G-inf-T)`, §1.2, `mathfrak P_+`. |
| 296 | `(S) => (D)`, `(c)(2)`, §1.2, rate m/2, `W_4`. |
| 297 | `(J)`, §1.4, `(G-ell)`, `(c)(2)`, `S^sharp`. |
| 298 | `(G-ell)`, §1.3, the cyclic sector and `ker H_ell=C Omega`. |
| 299 | `(U)`, §1.4, compared with `(U_ell)`. |
| 300 | `(T) => (S)`, §1.2. |
| 306 | `(G-ell) => (G-inf)`. |
| 310 | `(G-ell)`, `(G-inf)`, skeleton node `A1`, `(J2)`. |

Section 0's provenance/coverage statements are reporting statements rather than mathematical proof steps; current sources and access limits are recorded in Repo search. Section 8's plan-name comparisons are inventoried above, as requested. Section 9.1 overstates the import count; 9.2 retains the valid limit implication with the stated correction; 9.3 correctly identifies the sensitive steps; 9.4 remains a list of unproved targets, not a proof of any of them.

Only this output file was written. I did not edit the checked file, registry, FINISH row, audit state or plan. Other working-tree changes appeared during this session; they were not made or examined by this checker. The checkout moved concurrently to detached HEAD `55ce386ce589b9e49d1e27bab1f79e265ca4b9d6`. A final comparison verified that gap-os-equiv.md, cl1.md and gap-transfer.md still match the requested pin. The local branch `check/gap-os-equiv-20261110` remains at that pin; this report is uncommitted and unpushed in the supplied checkout. No external post or push was authorized or made.
