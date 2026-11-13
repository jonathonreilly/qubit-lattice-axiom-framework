# Repo search

Searched the statement and method on **origin/main, pr/10114, pr/10133, pr/10134 and pr/10141** in `/Users/jonreilly/Projects/Physics`, with bounded `git grep -n -i -E ... -- '*.md' '*.tex' | head` commands. Terms: `gap-compress`, `SEED-FP`, `(SEED-L)`, `chi.square mutual`, `Renyi.{0,20}telescop`, `Frohlich.Simon.Spencer`, `Fröhlich.Simon.Spencer`, and `Watson.{0,20}integral`. Broad discovery passes hit their caps and establish no absence. The final statement pass returned only five unrelated “gap-compression error” lines in `docs/ENERGY_TRANSFER_CORRELATION_BOUNDED_THEOREM_NOTE_2026-10-12.md:937`; no named target hit. The separate FSS pass completed within head 35.

Ref pins, in that order: `bb4ec020d5ada57c630dd89acc98a68397ade423`, `f76f6c649cff7dffbab664d8976e680e8f287fe9`, `89faef229ff6e6bde42baad15ed8270c2f4087d8`, `1e70c7211a2cdbc39001e619f1dd89db45e25851`, `c73ad7b177d94f89ff37b77386936e3d52b48b05`. No fetch or ref mutation was made.

Relevant hits, their exact content and proximity:

- **Main, vacancy-law note**, `docs/ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_WITH_VACANCIES_THE_INFRARED_STIFFNESS_IS_SET_BY_THE_BINDING_SCALE_LONG_RANGE_ORDER_ABOVE_THE_NEUTRAL_SCALE_AND_NO_FULL_BOUND_AT_IT_BOUNDED_THEOREM_NOTE_2026-09-24.md`, Theorems T2 and T4 (read lines 1–190). It proves `E|sigma-hat^e(k)|^2 <= 1/(beta_A E(k))` on even tori and the corresponding torus magnetization bound; its full-occupancy specialization has beta_A=beta. This is the same Gaussian-domination/Parseval method, already present. Credit its recorded Claude Opus 5.5 attempt and the FSS method. It does not contain TB2's odd-sector trace argument; no duplicate check of row 839 was found.
- **Main, sphere-static note**, `docs/ADMISSIBILITY_RULE_SPHERE_STATIC_LAW_ZERO_FIELD_COMPONENT_FOURIER_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md:58–81`, explicitly supplies `E(k)=2 sum(1-cos k_i)` and the Biskup Gaussian-domination parameter conversion `b=3 beta/2`. It confirms the normalization; it concerns S^2, not the O(4) layer or twist deficit. Both of these files also occur in the four PR-ref searches; only the specified main source ranges are relied on.
- **Main, cubic-walk note**, `docs/ADMISSIBILITY_RULE_CUBIC_WALK_RETURN_SUM_AND_SPHERE_STATIC_MAGNETIZATION_SUFFICIENT_BOUND_BOUNDED_THEOREM_NOTE_2026-09-15.md`, V1–V3 (read 1–180), already gives `6G_3=sum_n p_(2n)` and the exact binomial return formula. V3's sharp interval uses a 1000-term rational runner. Reuse V1; do not treat that certificate as a permitted proof here. Section 6 below supplies only a short hand bound needed for this check.
- **pr/10114 and pr/10133, soft-route `TQ55.md:228–239`**, under `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`, recalls the FSS method but explains that gauge-variant temporal-gauge links do not furnish a full-dimensional Wilson bound. Related warning, not a proof of or obstruction to the flat O(4) layer calculation. Its companion `CODEX_REVIEW_TQ.md:359` is a source locator, not fresh evidence.
- **Lane prior work**, `gap-skeleton-max.md:264–266`, `gap-skeleton-max-b.md:270–273`, already identifies the doubling defect as H_2; `gap-crux-fp.md:371–387` already supplies the flat O(4) identification and one-layer trace-ratio identity; `gap-ext-astra.md:575–620,637–646` already supplies the mixture information term. These are credited and reused, not claimed anew. `gap-vmf-lip.md:404–418` supplies TB1's uniform layer estimate.

The whole `prior/repo-search-2026-11-08.md` was read; its thirteen targets concern other RG obligations and do not cover this check. No row named `gap-compress` or `gap-compress-check` occurs in `open-registry.md`, `open-core.md` or `l17c.md`; the broader registry search produced only unrelated compression/entropy entries. Row 849 is this authorized check, not a new attack on another row's supplier.

**Outline lookup.** Used `sa-index/README.md`, chunk searches and `obligations.md` first. The specific information/seed/Ising/FSS labels have no target match in the outline index (the FILS bibliography and unrelated substring matches are not such a theorem). Read neighbouring rows in chunks 01 and 06, then SA lines 588–599 and 6863–6869 at the supplied `31a47c543775` source. The former explicitly separates polynomial clustering from a mass gap; the latter proves dilation preserves the Wilson weight and Haar measure. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. No assertion here that the entire CA corpus lacks a differently named result; no CA theorem or Balaban-paper claim is used to discharge the information estimates. Tadeusz Balaban's RG method is background attribution only. This is a check of our lane's text, not a new result about their account.

**Source policy.** Filesystem reads stayed in the requested checkout, SA directory, and the explicitly requested full Physics repository. The platform requires primary-source verification of recalled specialist literature; the narrow online reads below follow that higher-priority rule despite the repository-only search instruction. No numerical run was made.

Provenance: OpenAI Codex, gpt-6-astra, xhigh; check of FINISH row 839 at `67af92860fbc3dcc30ed291727eab6fd7e284fcb`, for row 849. Research text, not an audit; grants no status. Only this report is edited. The requested prior `library/prior/gap-compress-check-astra.md` was absent. No numerical proof or guide run is used. References to the source below mean `library/gap-compress-opus.md` at this pin. The final section will delimit coverage.

## 1. Lemma Z'' — HOLDS

Source 226–236. Normalize each transfer power to a density operator, denoted `sigma_k` to avoid confusing it with the integer rho. Put `a_k = F(Q_k)`. Direct cancellation gives

\[
\rho^4a_0-a_4=\sum_{k=1}^4\rho^{4-k}(\rho a_{k-1}-a_k).
\]

For the same spatial transfer operator on both tori in term k,

\[
\rho a_{k-1}-a_k=-\log\operatorname{Tr}\sigma_k^\rho
=(\rho-1)H_\rho(\sigma_k).
\]

If its largest eigenvalue is `q_0`, then `sum_i q_i^rho <= q_0^(rho-1) sum_i q_i = q_0^(rho-1)`. Thus each term is nonnegative and at least `(rho-1) log(1+S(T_0;B_k))`. Retaining k=4 proves the asserted coefficient `1/(rho-1)`. This uses positive trace-class transfer operators and axis symmetry for rectangular Wilson tori, already supplied in `gap-transfer.md` and used in `gap-phys-seed.md:247–272`; it does not assume a gap uniform in volume. The improvement over `2/rho` is exactly `rho/[2(rho-1)]`. No new physical input enters.

## 2. Widened (SEED-L) margin — HOLDS AFTER CORRECTION

Source 238–242. The coefficient change is right. State the consequence for the `L >= 25` range of Lemma FL, with the same bare Wilson transfer operators, rectangular-box inputs, and first-passage uniformity. A limsup is not an eventual bound by its own endpoint. Choose

\[
\phi_*<\bar\phi<(L-1)\log(13/10),\qquad
s_0=e^{\bar\phi/(L-1)}-1<3/10.
\]

The uniform limsup then gives `Phi_L <= bar phi` for all sufficiently large first-passage data. Lemma Z'' supplies `S(T_0;(LT_0)^3) <= s_0`. Theorem SH (`gap-seed-shape.md:87–113,125–136`) with `(j,p,q)=(6,6,12)` gives

\[
s_k\le (3.03s_0)^{6^k}/3.03,\qquad
1+S(N;(2N)^3)\le(1+s_k)^E,
\quad E=(6L/(L-1))^3,
\]

whenever `2N >= 6^k LT_0`. Its hypotheses hold: `12T_0<LT_0`, `3.03s_0<0.909<1`, and the final time can only lower S. Take fixed k with `E s_k <= 1/6000`. The elementary series bound `e^x <= 1/(1-x)` gives `S <= 1/5999 < 1/5041`. This k is cutoff-independent. For `ell=2L^m`, the new physical size `6^k L ell` has integral half-time at every cutoff. Thus the new strict margin is valid, conditional on the existing SH inputs; no seed is supplied. The needed correction is the limsup slack (also missing in the source FL substitution) and explicit `L>=25`, not a loss of the factor-two improvement.

## 3. Proposition TB — HOLDS

Source 175–189, parts (a), (b), (c), including the twisted-background extension. For the stationary Doob kernel, `J_*P^t(u,.)=P^t(Ju,.)`. If g is odd, integration against the difference of these probabilities gives `|P^tg(u)| <= eta_t ||g||_infinity`. A top odd eigenfunction divided by Omega is bounded on the compact slice space. Taking its supremum yields `(mu^-)^t <= eta_t`. If the odd restriction is zero, the lower bound is zero and requires no eigenfunction. The density-ratio expression for TV gives `eta_t <= kappa_t`, with the factor one-half exactly as printed.

For (b), cut the trace at t: its positive probability density is proportional to `A^(a-t)(v,u) A^t(u,v)`. The trace with J replaces the second factor by `A^t(u,Jv)`. Hence `2p(a)=E_w(1-ratio)`, and the two upper bounds follow. For (c), the odd trace contains its largest eigenvalue, so `S_-(a)>= (mu^-)^a`.

The background extension is valid in the positive-kernel representation, not by assuming a positive kernel for an arbitrary square root. In `gap-expose-astra.md:95–149`, set `X=z^(|E|/2) B_m^(1/2) K^(1/2)`. Then `L_m=X*X` and `XX*=z^|E| B_m^(1/2) K B_m^(1/2)` has the continuous strictly positive gauge-averaged kernel. X intertwines the centre involution because both factors commute with it. Thus sector spectra and sector traces agree, and the proof applies using the ground state of XX*. For beta=0 take the zero odd spectrum directly. No volume-uniform estimate is proved by TB alone.

## 4. Proposition TB2 — HOLDS AFTER CORRECTION

Source 199–207. The finite rectangular-box inequality HOLDS. The unqualified large-cube formula at line 203 FAILS below the ordering threshold: retain a positive part, or state `beta > N G_3`. The corrected statement is

\[
\liminf_{b\to\infty,\ b\ {\mathrm{even}}}
 (1-Z_{\rm anti}/Z_{\rm per})
\ge \frac{[(1-NG_3/\beta)_+]^2}{2N^2}.
\]

(The limit is through even b.) Here and below `G_3=(2pi)^(-3) integral_[−pi,pi]^3 [2 sum_i(1-cos p_i)]^(-1) dp`. The symbol `m^2` in the source denotes a lower bound, which can be negative; it is not an actual squared magnetization. For an explicit failure of the formula without the positive part, Jensen gives `G_3>=1/6`. At N=4 and beta=1/10 its printed right side is at least `289/288>1`, while `0<=1-Z_anti/Z_per<=1`.

**Literature input.** The recalled component bound is correct. Jürg Fröhlich, Barry Simon and Thomas Spencer, *Infrared Bounds, Phase Transitions and Continuous Symmetry Breaking*, CMP 50 (1976), 79–95, Section 2, especially Theorems 2.2–2.3, treats periodic rectangular nearest-neighbour models and arbitrary identical single-site measures with Gaussian moments. With each unordered bond counted once and coupling beta, its bound is `E|s-hat^a(p)|^2 <= |Lambda|/(beta E(p))`. Summing N components gives exactly the coefficient used here. Unit S^3 spins and the two-point Ising single-site measure meet its assumptions. The original transfer/Hölder proof does not require even transverse periods; b is even here for the half-time trace. Primary source checked: [FSS, Sections 2–3](https://math.caltech.edu/SimonPapers/65.pdf). The even-torus Gaussian-domination proof already in the repository is credited in Repo search; it is not a new result of this check.

**Line (i).** Identifying SU(2) with unit quaternions gives `tr(g_x g_y^*)/2=s_x dot s_y`. Thus the flat temporal-layer integral is the O(4) nearest-neighbour partition function at beta_W, with the irrelevant factor `exp(-beta_W |E|)` cancelling. A centre seam changes those scalar products' signs and gives the antiperiodic partition function. The spin transfer is positive: expand `exp(beta s dot s')` into tensor Gram kernels, and sandwich by the positive within-slice multiplier. The slice flip commutes with it. Therefore `Z_anti/Z_per=1-2w_o`.

**Line (ii).** Write A=cd, V=bA and `h(p)=E|M-hat(p)|^2/b`. Parseval and the component bound imply `E|M_tot|^2 >= V^2(1-NG_Lambda/beta)`. The nonzero longitudinal modes give, more precisely,

\[
g(b/2)\ge A^2 m_\Lambda^2
 -\frac{NA(b^2-1)}{12\beta b}
\ge A^2 m_\Lambda^2-\frac{NbA}{12\beta}.
\]

The finite sine identity is exact, without a run: differentiate `sum_{k=0}^{b-1} cot(x+pi k/b)=b cot(bx)`, subtract the singular k=0 term, and let x tend to zero. Since `csc^2 x=x^(-2)+1/3+O(x^2)`, the sum is `(b^2-1)/3`; dividing by four gives `(b^2-1)/12`. The normalized sums `G_Lambda` tend to `G_3` on cubes: away from zero use ordinary Riemann sums; near zero, `E(p)>=4|p|^2/pi^2` and lattice shells bound the omitted contribution by `C delta+O(1/b)`.

**Line (iii).** Every component M changes parity. Thus the two cross terms in the trace are equal. Schatten Hölder gives `||A_even^(1/2) M A_odd^(1/2)||_2 <= ||A_even^(1/2)||_4 ||M|| ||A_odd^(1/2)||_4`. Squaring, dividing by Z, and summing N components gives `g(b/2)<=2NA^2 sqrt(w_e w_o)<=2NA^2 sqrt(w_o)`. This checks both the factor 2 and the factor N. Combining the last two displays yields exactly

\[
1-Z_{\rm anti}/Z_{\rm per}
\ge2\left[\left(\frac{m_\Lambda^2}{2N}-\frac{b}{24\beta cd}\right)_+\right]^2.
\]

**Threshold and decimals.** For N=4 and beta>4G_3 the stated lower bounds `m^4/32` for the deficit and `m^4/64` for kappa_1 follow. Hence (AS-bg), which would force the ratio to one, is impossible there. The exact threshold is **4G_3**, not the literal decimal 1.0109. FSS Section 3 quotes Watson's analytic simple-cubic integral `I(3)=2G_3` with decimal `0.5054620197...`; hence `4G_3` is approximately `1.0109240394...`. The source's `G_3=0.252731` and `4G_3=1.0109` must use approximation signs. Their quadrature supplies no proof of a decimal cutoff. In particular, “every beta_1>1.0109” is stronger than the proved condition and is not licensed. Use beta_1>4G_3, and similarly beta>2G_3 for XY. The examples 0.0098 and 0.0117 remain GUIDE approximations; they are unnecessary. The hand bound G_3<1/3 in Section 6 already proves failure of (AS-bg) for beta>4/3, including the whole window [2.3,2.6], without any decimal evaluation of G_3. This check does not turn the claimed physical critical coupling near 0.94 into a theorem. The obstruction concerns **kappa_1 and (AS-bg)**. TB gives eta_1<=kappa_1, so a lower bound on kappa_1 supplies no lower bound on the Doob TV coefficient eta_1. The table at source 109 and any “one-layer TV = (AS-bg)” reading must be corrected; TB2 does not rule out eta_1 as a separate route.

## 5. Corollary TB1 — HOLDS AFTER CORRECTION

Source 191–197. Require **0<beta_1<2/3**, as the supplying `gap-vmf-lip.md:404–418` does. Its formula for C is undefined at beta_1=0. The case beta=0 itself is harmless: the transfer has rank one, mu^-=0 and E^-=+infinity. At beta_1=0 use that separate statement.

For positive beta_1, (AS-bg) gives `exp(-eps)<=ratio<=exp(eps)`, hence `kappa_1<=(exp(eps)-1)/2`. If `eps<=1`, convexity gives `exp(eps)-1<2eps`, and TB yields `mu^-<=C(|B|/b_nu)exp(-m b_nu)`. Taking minus logarithms proves the printed lower bound, including the power b^2 on cubes. The large-b liminf is `liminf E^-(b^3)/b>=m`; no bound is supplied at order-one beta.

The example has exact constants `m=log(4/3)/2`, `C=64/(3 sqrt(3))` and bound `50 log(4/3)-log(640000/(3 sqrt(3)))` at b=100. The printed decimals are approximations to these expressions, not inputs. The term “string tension” here names this lower bound on the winding electric-flux energy per spatial length; it does not by itself identify a Wilson-loop area-law coefficient.

## 6. Proposition Q — HOLDS AFTER CORRECTION

Source 129–131. The Ising counterexample is valid. Specify **even periodic spacetime cubes**, and write its thermal sum as `S_Ising(b;b^2)` (two spatial dimensions and one transfer direction). Replace the asserted proof of the decimals 0.278 and 0.0193 by the exact `q=1-G_3/(7/20)` and `liminf w_o >= q^2/4`; the quadrature in Section 5 does not certify those decimals. “The two-point function does not decay” refers to the symmetric periodic-limit state, not to truncated correlations in an extremal plus state.

Here is a hand bound that makes the counterexample unconditional without the quadrature or the repository's 1000-term certificate. Reuse the exact return formula V1 of the September 15 cubic-walk note (Repo search): with `phi=(cos p_1+cos p_2+cos p_3)/3` and `p_(2n)=integral phi^(2n)`,

\[
6G_3=\sum_{n\ge0}p_{2n},\qquad
p_{2n}=\frac{\binom{2n}{n}}{6^{2n}}
 \sum_{a=0}^n\binom na^2\binom{2(n-a)}{n-a}.
\]

A coarse tail avoids machine-sized sums. Symmetry under `p -> p+(pi,pi,pi)` and `u^(2n)<=exp(-2n(1-u))` for `0<=u<=1` give

\[
p_{2n}\le2\left[\frac1\pi\int_0^\pi
 e^{-(2n/3)(1-\cos x)}\,dx\right]^3
\le\frac{(3\pi)^{3/2}}{32n^{3/2}}
<\frac{15}{16n^{3/2}}.
\]

The middle bound uses `1-cos x>=2x^2/pi^2` and extends the Gaussian integral to infinity. For the last, `3pi<66/7<(31/10)^2` and `31^3/32000<15/16`. Consequently `sum_(n>9) p_(2n)<15/(8 sqrt(9))=5/8`.

Only nine small finite sums remain. The numerator column is the binomial sum above multiplied by `binom(2n,n)`; each row is checkable directly with at most ten summands. The last column is a rational upper bound on that numerator divided by `6^(2n)`.

| n | Numerator | Strict upper bound |
|---|---:|---:|
| 1 | 6 | 170/1000 |
| 2 | 90 | 70/1000 |
| 3 | 1860 | 40/1000 |
| 4 | 44730 | 27/1000 |
| 5 | 1172556 | 20/1000 |
| 6 | 32496156 | 15/1000 |
| 7 | 936369720 | 12/1000 |
| 8 | 27770358330 | 10/1000 |
| 9 | 842090474940 | 9/1000 |

Thus `6G_3<1+373/1000+5/8=999/500`, so `G_3<333/1000<1/3`. At beta=7/20, `q>1/21`. TB2 with N=1 then gives `liminf w_o>1/1764>1/5041`. Since `S>=S_-` and `S_-/(1+S)=w_o`, the thermal sum stays above the seed threshold for every sufficiently large even cube. This is already enough to refute the proposed lattice criterion. It proves a weaker explicit constant than 0.019, which remains a correctly motivated GUIDE decimal here.

The other half needs no hyperbolic-function evaluation: `tanh(7/20)<7/20`, so `6 tanh^2(7/20)<147/200<1` (and the five-neighbour version is smaller). Parseval's lower bound on volume-averaged correlations prevents decay to zero in the symmetric periodic-limit state. FSS applies to the identical single-site measure `(delta_-1+delta_+1)/2`; no O(N) continuity assumption excludes N=1.

The tree literature is being used at a narrower scope than the slogan after Q. The binary symmetric Ising broadcast channel has squared contraction `tanh^2 beta`, and its regular-tree nonreconstruction threshold is the branching number times that square. That concerns conditionally independent descendants. Q refutes transplanting those edge numbers to an interacting lattice. It does **not** refute valid SDPI or spectral-independence criteria using the lattice's actual conditional distributions. The 2D aside is consistent with the exact square-lattice Ising critical value `log(1+sqrt(2))/2`; it is not needed here.

## 7. Proposition K — HOLDS

Source 82–88. Fix `0<delta<1` and an integer n>=1; take `0<eps<1-delta`. The printed two-state transition matrix is stochastic and reversible because the two stationary edge flows both equal delta eps. Its nontrivial eigenvalue is `mu=1-delta/(1-eps)>0`. Consequently `S(2n)=mu^(2n) -> (1-delta)^(2n)>0`, whereas `0<=I(X_0;X_n)<=h(eps)->0`. This contradicts every proposed Psi tending to zero. For a hand example, delta=1/2 and n=1 make the limiting thermal sum 1/4. No rare-state numerical run or literature theorem is needed. The conclusion is absence of a universal Shannon-only modulus over this class; it does not preclude a modulus under additional bounds on stationary densities or modes.

## 8. Identity I1 and its seed interpretation

**Displayed identities — HOLDS.** Source 36–46. Normalizing Omega in L^2 gives a probability pi. Ground-state division conjugates T/lambda_0 to P. Under pi times pi the density of the two-slice joint law is p_n. Thus

\[
\chi^2(\mathcal L(X_0,X_n)\Vert\pi\otimes\pi)
=\|P^n-\Pi\|_{HS(L^2(\pi))}^2
=\sum_{i\ge1}\mu_i^{2n}=S(2n;B).
\]

Here Pi projects onto constants. This derivation separates the vacuum before taking the Hilbert-Schmidt norm. It also handles the zero modes outside the gauge-invariant subspace. The order-two divergence is `log(1+S(2n))`. Jensen under the joint law gives `I<=log integral p_n^2`, exactly as written.

**Time interpretation — HOLDS AFTER CORRECTION.** Source 46 says `S(n;(2n)^3)` measures information across n layers. For even n its two slices are **n/2 layers apart**, with cross-section `(2n)^3`. Alternatively retain separation n and use `S(2n;B)`. Theorem S still acts on the corresponding quantities, but the factors of two must be kept. This is chi-square information relative to the product marginals; it is not Shannon information, nor every convention named “Rényi mutual information.”

## 9. Identity I2 — HOLDS

Source 48–60. With `q_i=mu_i^t/(1+S(t))`, `q_0=1/(1+S(t))`, so `H_infinity=log(1+S(t))`. Moreover `Tr rho_t^alpha=Z(alpha t)/Z(t)^alpha`. The two elementary estimates

\[
q_0^\alpha\le\sum_iq_i^\alpha\le q_0^{\alpha-1}
\]

give precisely the stated lower and upper bounds for H_alpha. They apply also to real alpha>1 when the spectral powers are used. The alpha=2 free-energy identity is prior work by Claude Fable 5.2 in `gap-skeleton-max.md:264–266` and `gap-skeleton-max-b.md:270–273`; no novelty is claimed.

The decimal gloss at source 60 requires correction: `s_*<1/5041` gives `H_infinity<log(5042/5041)`, not necessarily `<1.98 times 10^(-4)`. Use the exact logarithm (or the looser `1.984 times 10^(-4)`, since `log(1+x)<x` and `1/5041<1.984 times 10^(-4)`). This does not change a seed threshold.

## 10. Identity I3 and the t-layer identity

**Displayed identities and background extension — HOLDS.** Source 62–80. Since Omega is J-even, the odd sector has no vacuum term. Spectrally, `p(t)=S_-(t)/(1+S(t))`. On L^2(pi), the kernel of `P_-P^n` is `(f_u(v)-f_(Ju)(v))/2`, hence

\[
S_-(2n)=\|P_-P^n\|_{HS}^2
=\tfrac14\int\pi(du)\,\|f_u-f_{Ju}\|_{L^2(\pi)}^2.
\]

The twisted-background identification and the t-layer trace calculation were verified in Section 3 above. They retain their exact scalar factors.

**“Twist deficit is exactly chi-square distinguishability” — HOLDS AFTER CORRECTION.** The precise statement is

\[
p(2n)=\frac{\int\pi(du)\|f_u-f_{Ju}\|_2^2}{4(1+S(2n))}.
\]

This is a common-reference L^2 separation, not `chi^2(P^n(u,.) || P^n(Ju,.))`. The latter integrates `(f_u-f_Ju)^2/f_Ju` against pi. For the symmetric two-state kernel with eigenvalues 1,r and n=1, the averaged numerator divided by four is r^2, the deficit is `r^2/(1+r^2)`, and the pairwise chi-square divergence is `4r^2/(1-r^2)`. At r=1/2 these are 1/4, 1/5 and 4/3. Thus the literal identification of these quantities FAILS; the printed integral identity itself is correct.

## 11. Rank-one identity — HOLDS

Source 139–143. Write `R_n=T^n/lambda_0^n=P_Omega+sum_(i>=1) mu_i^n P_i`. Its remainder is positive trace class, so `||R_n-P_Omega||_1=S(n)`. This normalization matters: for the density operator `rho_n=R_n/(1+S(n))`, the norm is instead `||rho_n-P_Omega||_1=2S(n)/(1+S(n))`. The source uses R_n, so its displayed equation is right. The seed recursion gives the stated consequence only on the Wilson/axis-symmetric transfer family satisfying Theorem S, not for arbitrary rank-one approximations. A family of rank-two positive transfer matrices with second eigenvalue tending to the first already shows why bounded rank alone yields no uniform gap. The 1D Ising example supplies exactly such a family; the Z_2 gauge-theory aside is unnecessary to this conclusion.

## 12. Mutual-information area law — HOLDS

Source 133–137. For a finite link partition, let nu be the product Gibbs law after removing crossed plaquettes. Write the removed action as U. Each Wilson term lies in `[0,2 beta_W]`, so `osc U<=2 beta_W |P_d|`. Then

\[
D(\mu\Vert\nu)=-E_\mu U-\log E_\nu e^{-U}
\le\operatorname{osc}U.
\]

For any product nu, the relative-entropy chain rule gives `D(mu||nu)=I_mu(A;A^c)+D(mu_A||nu_A)+D(mu_Ac||nu_Ac)`. This proves the general cut bound without finite-alphabet entropies. For the stationary Doob cylinder, use the source's product of normalized `a(u)du`, where `a=Omega exp(-V/2)`. The extra factor is I(u,v), a layer integral of 3|B| temporal plaquettes. Thus `osc log I<=6 beta_W |B|` and `I(X_0;X_1)<=6 beta_W |B|`. Data processing gives the n>=1 bound. The one-seam factor 6 refers to these cylinder slices; one must not apply a linear-chain Markov argument to two slices of a finite time ring with a second connecting arc. The general cut formula still holds on that ring. Limits with a finite crossing set follow by lower semicontinuity and finite marginals.

The source attribution is correct in scope: Michael M. Wolf, Frank Verstraete, Matthew B. Hastings and J. Ignacio Cirac, *Area laws in quantum systems: mutual information and correlations*, PRL 100, 070502 (2008), proves thermal mutual-information area bounds. The argument above directly covers continuous Wilson link variables; it does not apply their finite-alphabet classical boundary-entropy bound to Haar variables. [Primary paper](https://arxiv.org/pdf/0704.3906). This is a Shannon area bound and supplies no distance decay or chi-square seed.

## 13. Consequence 2 of Z'' — HOLDS

Source 244. Retain `b>=12` divisible by four, as in `gap-phys-seed.md:274–279`. Spectrally, `S(T)<=exp(-(T-T_0)m)S(T_0)`. With T=b/2, T_0=b/4 and the checked Z'' bound,

\[
S(b/2;b^3)\le(e^{\Phi_4/3}-1)e^{-bm/4}
\le e^{\Phi_4/3-bm/4}.
\]

Thus the exact sufficient constant is `bm >= (4/3)Phi_4+4 log(1650)`. The printed 29.64 is larger than `4 log(1650)` and is safe. A finite rational check is `e>1359/500` from its Taylor series through degree six, and `e^(41/100)>sum_(j=0)^5 (41/100)^j/j!`; the product of the latter polynomial with `(1359/500)^7` exceeds 1650. Hence `log(1650)<741/100`. The coefficient changes from 2 to 4/3 exactly as asserted. This supplies a sufficient conditional seed, not the required lower bound on bm.

## 14. Other exact statements in Sections 1–3

**Mixture information, Section 1.5 — HOLDS; broad exclusion — HOLDS AFTER CORRECTION.** `I_pi=I(J;Y)=H(J)-H(J|Y)<=H(pi)<=log M`. This is already `gap-ext-astra.md` (E22)–(E23). If every admitted map costs at least `c a^2`, the mixture costs at least `c a^2-log M`. This excludes subexponentially many such maps as a way to pay an order-a^2 cost. It does not exclude mixing with exponentially many maps, other classes of maps, or other transport constructions. Replace “cannot be closed by mixing” by this quantified restriction.

**Data processing and chain rule, Section 2.1(a)–(c) — HOLDS.** Apply separate deterministic maps, or conditionally independent randomized maps, to the two slices. The Markov chains `RX_0—X_0—X_n—RX_n` give both the f-divergence contraction and the displayed Shannon chain rule. Small coarse information is a lower bound, not an upper bound, on the fine information. No estimate on the two conditional terms is proved. Section 2.1(d) holds as a statement about an exact partition-function representation; it does not identify the coarse marginal with the original Doob process. The SA dilation identity checked above is exact. No extra smallness follows from that identity.

**SDPI and constant-row-sum facts, Section 2.2 — HOLDS.** The fixed-stationary-input chi-square coefficient is `||P^n||_(1-perp)^2=mu_1^(2n)`; expand a mean-zero density perturbation and use self-adjointness. Applying the same bound to each conditional density proves the displayed thermal-sum inequality. A supplied stationary KL contraction gives the stated iterated Shannon bound by the Markov chain and submultiplicativity. For C>=0 with constant row sum r, `C1=r1` and `||C||_infinity=r`, so its spectral radius equals r. The claims about actual Wilson contraction constants or typical pinned matrices are not supplied by this algebra.

**Binary twist-channel language, Section 3.1 — HOLDS AFTER CORRECTION.** Eta_t is the TV distance between the two output laws, maximized over u. It is not itself a KL coefficient. For each binary-input channel with output laws Q_+,Q_- and TV distance d, the unrestricted KL contraction coefficient lies between d^2 and d. The upper bound follows by factoring through an erasure with common output mass 1-d. For the lower bound, perturb the uniform input; the limiting relative-entropy ratio is `integral (q_+-q_-)^2/[2(q_++q_-)]`, at least d^2 by Cauchy–Schwarz. Thus the coefficients have equivalent vanishing, with these inequalities; Pinsker alone is not an equality between them.

**Section 3.5 — no asserted proof of a thick-slab supplier.** Its exact sufficient use of kappa_t follows from TB. Its U(1) sentence “by (c) p(a) does not decay” does not follow from mu^- tending to one alone: (c) retains the denominator `1+S(a;B)`, which needs control. Likewise an upper allowance for large eigenfunction overlaps does not prove a lower bound on necessary slab thickness. These are gaps in the stated heuristic inferences, not refutations of the proposed SU(2) slab estimate. No claim of its impossibility is justified.

## 15. Recalled literature: statements as used

These verdicts check the recalled statements and their attribution. They do not re-prove entire literature theorems or supply missing Wilson hypotheses.

- **Tree broadcasting — HOLDS at the stated binary-symmetric scope.** Evans, Kenyon, Peres and Schulman, *Broadcasting on Trees and the Ising Model*, Ann. Appl. Probab. 10 (2000), is the source for the Ising reconstruction threshold. Kesten–Stigum is not a blanket exact reconstruction threshold for every channel. Q uses only the binary case and a deliberately invalid lattice transplant. [Author-hosted source locator](https://users.cms.caltech.edu/~schulman/Papers/evansKPS00Ising.pdf); its PDF fetch timed out, so no fresh line-by-line literature check is claimed. The counterexample above does not depend on this tree theorem.
- **One-dimensional entanglement area theorems — HOLDS with their domains.** Hastings (2007) concerns gapped local finite-dimensional 1D quantum ground states. Brandão–Horodecki concerns pure 1D quantum states with exponential decay of correlations between separated regions, not merely selected two-point observables. Neither theorem is a 4D thermal trace count. [Hastings](https://arxiv.org/abs/0705.2024), [Brandão–Horodecki](https://arxiv.org/abs/1206.2947).
- **Kuwahara–Kato–Brandão (2020), source 137 — FAILS as a claim of an available proof at the recalled generality.** Their [2025 erratum](https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.134.199901) identifies invalid noncommutative rearrangements and an unjustified subsystem cluster-expansion bound. It does not preserve the original general exponential-CMI theorem. The replacement [Kato–Kuwahara work, v2](https://arxiv.org/html/2504.02235v2) gives results with explicit hypotheses and distinguishes `ABC=Lambda` from proper subsystems. A corrected survey must state the particular available theorem and scope; this is a proof-status failure, not a counterexample to all high-temperature CMI decay.
- **“CMI clustering implies Davies gaps,” attributed to Brandão–Kastoryano (2019), source 137 — FAILS.** [Their 2019 paper](https://arxiv.org/abs/1609.07877) gives efficient preparation assuming correlation decay and an approximate Markov property. It does not assert the implication as quoted. [Kastoryano–Brandão, *Quantum Gibbs Samplers: the commuting case*](https://arxiv.org/abs/1409.3435), relates sampler gaps to a particular **strong clustering** condition. Exact conditional independence across a shield in a classical Gibbs field is not that condition. Replace the source and hypothesis together.
- **Kennedy–Rychkov high-temperature tensor RG — HOLDS at its stated scope.** Their [*Tensor RG approach to high-temperature fixed point*](https://arxiv.org/abs/2107.11464) treats a specified 2D tensor RG map near the trivial fixed point, including high-temperature Ising tensors. It is not a general bounded-rank-to-gap theorem.
- **Brudno rate statement — HOLDS AFTER CORRECTION; “excess entropy is the free-energy defect,” source 151 — FAILS.** Brudno's entropy/complexity theorem and its [Z^d subshift version](https://www.sciencedirect.com/science/article/pii/S0890540117300147) concern symbolic finite-alphabet descriptions (or specified measurable partitions), almost surely under an ergodic invariant measure. Continuous SU(2) samples require an encoding/partition. [Crutchfield–Feldman](https://dpfeldman.github.io/Publications/ruro.pdf) use excess entropy for subextensive **Shannon block entropy**, equivalently past/future information in the 1D stationary setting; this is not a periodic log-partition defect. For a zero-field 1D Ising chain, put r=tanh beta in (0,1). Its excess entropy is `log 2-h((1+r)/2)>0`, while its periodic free-energy correction is `log(1+r^L)->0`. This hand counterexample disproves the identification even in a gapped phase.
- **RSMI, source 155 — HOLDS AFTER CORRECTION.** The objective is correctly attributed to [Koch-Janusz–Ringel](https://arxiv.org/abs/1704.06279). But the statement that the claims are only numerical or Gaussian/1D misses a theorem of [Lenggenhager et al.](https://arxiv.org/abs/1809.09632): perfect information retention does not increase interaction range, with related disorder conclusions. The examples are narrower than that general conditional statement. It supplies no seed or gap estimate here; report that precise missing implication rather than dismissing the literature as entirely numerical.
- **OSSS/monotonic-measure extension — HOLDS with the actual monotonicity hypothesis.** O'Donnell–Saks–Schramm–Servedio gives the decision-tree variance bound for product inputs; [Duminil-Copin–Raoufi–Tassion](https://annals.math.princeton.edu/wp-content/uploads/annals-v189-n1-p02-s.pdf) gives the monotonic-measure extension and sharpness applications. Positive association alone must not replace their hypotheses. No monotone representation of the Wilson SU(2) measure is supplied here; failure of one termwise character expansion does not prove that every possible representation is impossible.
- **Continuum c/F/a-theorem comparison — HOLDS as a domain warning.** The entropic arguments need their relativistic continuum and state hypotheses; for example [Casini–Teste–Torroba](https://arxiv.org/abs/1704.01870) uses Lorentz invariance, strong subadditivity and the CFT-vacuum Markov property. These are not automatic lattice RG inequalities and permit a massless infrared endpoint. No group-selecting estimate follows. The source's numerical/phase heuristics about photons, topological entropy, spectral independence and typical influence matrices remain GUIDE; they are not promoted here to theorems.

Section 2.5's Gibbs variational identity HOLDS when entropy is defined relative to the same Haar reference as Z: `log Z=sup_nu[-E_nu S-D(nu||Haar)]`. Its per-site limit loses subextensive terms; that does not rule out every possible finite-size information-theoretic estimate. Section 2.9's nonnegativity of H_2 HOLDS by the eigenvalue calculation in Section 9; merely naming entropic uncertainty supplies no stronger inequality. The note establishes no general no-go theorem about compression theory.

**TV versus slab control — FAILS as an equivalence (source 109).** A hand example separates them. Take states `0,+,-`, stationary weights `(1-2a,a,a)`, `0<a<1/2`, and J swapping + and -. Let `g(0)=0`, `g(+)=1/sqrt(2a)`, `g(-)=-1/sqrt(2a)` and define the reversible kernel relative to pi by `p(u,v)=1+a g(u)g(v)`. It is strictly positive and has nonnegative eigenvalues 1,a,0. The two rare rows have densities `(1,3/2,1/2)` and `(1,1/2,3/2)`. Hence `eta_1=a` tends to zero, whereas the worst ratio is 3 and `kappa_1=1`. Thus TB2's flat-background slab obstruction cannot, by TB alone, dismiss the Doob TV coefficient. This example checks the inference, not the actual Wilson coefficient.

## 16. Coverage and disposition

Checked the named statements against the pinned source, with hand arguments and the explicitly cited inputs. Lemma Z'', TB, K, the displayed information identities, the rank-one identity, the area law and the 4/3 consequence hold. The widened margin needs limsup slack and the stated L range. TB1 needs its zero-coupling endpoint separated. TB2 needs its positive part, its exact threshold, and restriction of its obstruction to the slab coefficient. Q needs the proof/numerical distinction and the transfer geometry stated correctly; the hand replacement above proves its counterexample without quadrature. The elapsed session produced no numerical proof, test run, audit record, registry edit or source repair.

The substantive failures outside that core are the unqualified TB2 asymptotic below threshold; identifying Doob TV with slab control; literal pairwise chi-square/twist identification; the excess-entropy/free-energy identification; and the recalled quantum-CMI proof/gap attributions. Their corrected scopes are recorded above. The memory-only survey does not justify the source RESULT's universal “no compression or information theory gives a handle” reading. It can report only that this note supplies no order-one seed or thick-slab estimate. The actual slab estimate remains open, as does any quantitative use of the separate Doob coefficient. No mass gap or change of scientific status follows.

Not rechecked: the whole upstream proofs of Theorem SH or the account's RG construction, every phase heuristic, guide-run logs outside the allowed source paths, or the full proofs of the cited literature. A citation checked for its statement remains an import; the source's numerical values do not become hand-certified constants. The unrelated earlier target digest and source indexes are retrieval evidence, not independent mathematical checks. The unavailable tree-paper fetch is recorded above. This report itself has not been checked by a further reader.

Source SHA-256: `5d9803a8487f211b1caaba0b06c7455a3c1e710bca7878fdbfdd85c34ef644d2`. Only `library/gap-compress-check-astra.md` was created; it remains uncommitted in this pinned `lanework` checkout. No push, PR or external message was made.

RESULT: HOLDS for Lemma Z'', TB, K, the displayed spectral/information identities, the rank-one identity, the mutual-information area law and the 4/3 consequence; HOLDS AFTER CORRECTION for the widened (SEED-L) use, TB1, TB2, Q and the dictionary's interpretations; FAILS for the identified overextensions and recalled literature claims; no order-one seed, mass gap, blanket information-theoretic no-go or scientific status is established.
