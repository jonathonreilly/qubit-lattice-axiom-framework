# Repo search

OpenAI Codex, configured gpt-6-astra/xhigh; 2026-11-13. Research-text check of FINISH 863 for row 879, not an audit. No status is granted. No computation discharges any statement. Source `gap-crux-skeleton-max.md` is abbreviated **S**; all its line numbers refer to the pinned checkout.

Searched `/Users/jonreilly/Projects/Physics` with `git grep -n -i -E`, on `origin/main`, `pr/10114`, `pr/10133`, `pr/10134`, `pr/10141`, restricted to Markdown/TeX and bounded by `head`. Terms: `Schr[oöe]+dinger.bridge`, `Hopf.{0,50}(bound|theorem)`, `cut.and.reglue`, `electric.only`, `SEED-FP`, `M5-G`, `BASE-Phi`; then `transfer (operator|matrix)`, `electric.flux`, `twist (deficit|ratio)`, `thermal (sum|trace)`, `Casimir`. The first query returned only unrelated atomic Schrodinger bridges, U(1) electric-only linear algebra, Hopf-loop and Poincare-Hopf references. No matching bridge, Hopf contraction, reglue lemma or named seed supplier was found by that query. Broad transfer searches reached their caps; they are locators, not evidence of absence. Relevant bounded follow-ups and exact statements are recorded below as read.

Local search located `gap-skeleton-final.md`, `gap-assume-opus.md`, `gap-finishline-opus.md`, `gap-phys-seed.md`, `prior/gap-lit-geom.md`, `gap-compress-opus.md`, and `gap-brainstorm-max.md`. These contain the earlier seed, variational, path and free-energy architecture; S itself credits them. This task checks S, and does not reopen those owned proof targets. `open-registry.md` has no match for the target name, SEED-FP, M5-G, BASE-Phi, bridge or Hopf. The requested task-specific prior file is absent. The older `prior/repo-search-2026-11-08.md` concerns UV/history suppliers, not this finite-box check; its snapshot copies are not independent evidence.

SA-index README, relevant chunk-02 rows 90–110 and obligations entries 24, 27, 135, 156 were consulted. The outline already supplies the one-link spectrum and transfer construction: SA 2195–2257 gives `c_l = 2 exp(-beta) I_(2l+1)(beta)/beta`, factorial decay and the positive product kernel; SA 2313–2336 defines `L = P C_E^(1/2) exp(-V) C_E^(1/2) P`, states it is positive and trace class, and proves `Z_s(0)=Tr L^s`. This is the existing input to A2/B1/B2, not a new contribution here. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Tadeusz Balaban is credited for the RG estimates used by the upstream account; no original Balaban paper is available or imported here.

Requested source revision: `6deb28f38`; account revision: `31a47c543775`.


The five refs resolved during the search to `993f5e4f6d11`, `f76f6c649cff`, `89faef229ff6`, `1e70c7211a2c`, `c73ad7b177d9`, respectively. Additional exact outside-lane hits read:

| Ref and file | Exact statement and closeness |
|---|---|
| `origin/main:docs/WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY_BOUNDED_NOTE_2026-05-30.md:302–331` | Establishes only gauge convolution-kernel positivity; the mixed interacting transfer representation is explicitly open. Same positive-kernel method, different SU(3)/fermion object; no A2, bridge or uniform-gap supplier. |
| `pr/10114:.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md:90–150` | The actual conditional ground-state density has Haar lower comparison `exp[-2 beta p_B-4 beta b]`; it contains no decay or useful fixed-physical-block uniformity. Also `kbar_B W_C=r_f^b W_C`, with SU(2) `r_f=I_2/I_1`, yields a positive one-step loop witness. Close prior for electric loop eigenvalues and finite-energy bounds, not A2's trace seed or B2's magnetic-independent gap. Credit the Codex author of that file. |
| `pr/10114:.claude/science/toe-ruleset-20261021/agents/ym4d-existence/EXISTENCE.md:2528–2548` (also a search hit on `pr/10133`) | Its soft-route Polyakov signal is conditional and confined to a fixed physically small spatial torus; no local-observable, infinite-spatial-volume, clustering or mass-gap conclusion is delivered. Same electric-flux vocabulary, different conditional soft block law; it does not refute or supply this check's target. |

The outside-lane search found no existing check of S or owner of row 879. The older named results are used and credited, not re-attacked. Searches yielding unrelated matches or reaching a cap are not absence theorems. The expanded `YM4_1400` manuscript and original Balaban papers were not read. Upstream assertions here use the supplied outline and bounded CA-I passages, not unverified claims about those unread texts.

# Statement checks

This report checks S's displayed statements, their proofs, its final skeleton and its source map. It does not prove a mass gap, supply any open first-passage input, certify historical check records, or verify recalled numerical physics. FAILS can mean a false formula or an unsupported claimed proof; the text distinguishes them. Only this report is edited. The requested pinned checkout is retained.


## 1. A2: electric-only trace and polymer bound — HOLDS AFTER CORRECTION

**S 150–153, 371.** Use the normalized electric transfer operator: divide the physical operator by its constant one-link eigenvalue on every bond. Then `lambda_0=1`; the ratios and S are unchanged. With S 40's original weight, the literal physical eigenvalue is instead `[exp(-beta_t)c(beta_t)]^(3|B|)`, where `c(beta)=2I_1(beta)/beta`. S switches normalization without saying so.

With that convention the trace formula holds. Integrating each bond variable gives `u_j^t chi_j(h_x) chi_j(h_y)` by character orthogonality. A chosen bond subset with a degree-one vertex integrates to zero. A nonempty connected survivor has at least four edges on the stated simple tori. Each absolute activity is bounded by `eps_t^n`.

Here is a hand check of the counting constant, rather than an invocation of a polymer theorem. The bond adjacency graph has degree ten. Connected n-vertex subsets through a specified root are bounded by `10^(n-1) n^(n-2)/(n-1)!`: choose a labelled spanning tree (Pruefer codes), embed from its root, then divide by the `(n-1)!` labellings. The factorial estimate gives at most `(10e)^(n-1)`. Sum over the `3|B|` root bonds; this overcounts, which is harmless. Dropping compatibility between components bounds the polymer sum by the exponential of their absolute activities. Thus

`log(1+S) <= 3|B| sum_(n>=4) (10e)^(n-1) eps_t^n <= 6(10e)^3 |B| eps_t^4`

when `10e eps_t <= 1/2`. This verifies the precise constant and inequality. For any fixed finite beta_t, positivity on the compact group gives a nontrivial spectral bound q<1, and trace class gives `eps_t <= q^(t-1) eps_1`. Therefore S tends to zero for `B=(2t)^3`; this proves the claimed existence of a seed at each fixed beta_t. At beta_t=0, S=0 directly. This is an anisotropic seed; the isotropic axis-exchange theorem cannot be applied to it.


## 2. A2's numerical example — HOLDS AFTER CORRECTION

**S 154.** The decimal Bessel values and `eps_t about ...` are not hand error bounds. A weaker, sufficient rational check is as follows. Use the source's positive series

`I_d(5/2)=sum_(k>=0) (5/4)^(d+2k)/(k!(d+k)!)`.

Its first five terms give `I_1>251/100` and, including the geometric tail, `I_2<32/25`. For the latter, the successive-term ratio after k=4 is at most `25/(16*5*7)=5/112`; bounding the tail by that geometric series proves the displayed upper bound. Hence `u_(1/2)<51/100`. GL4 further gives `I_d/I_2 <= (5/12)^(d-2)` for d>=2. Therefore

`eps_15 < (51/100)^15 [4 + sum_(d>=3) d^2 (5/12)^(15(d-2))] < 4.01(51/100)^15 < 1/6000`.

For the middle inequality put `z=(5/12)^15<1/100000`; the bracket is `4+z(9-11z+4z^2)/(1-z)^3<4.01`. For the last, `(51/100)^5=0.0345025251<0.03451`, whose cube is below `0.0000411`. Since e<11/4, the exponent in A2, with |B|=27000, is less than `6*28^3*27000/6000^4<3/10^6`. The series inequality `exp(x)-1<=x/(1-x)` now gives `S<1/300000<1/5041`. These are displayed hand estimates, not evaluated machine certificates. The stated `1.7e-6` remains an approximation; it is unnecessary. The large-beta claim `t of order beta log beta` needs a uniform coefficient-tail estimate absent from S; keep it as a guide, not part of A2.


## 3. B1: two-slice bridge — HOLDS

**S 194–198, 372.** Substitution gives the stated positive joint density. Integrating its second argument gives `Omega(U)(T Omega)(U)/lambda_0=Omega(U)^2`, and symmetry gives the other marginal.

The needed uniqueness has a short proof here, so no unread Beurling/Csiszar theorem is needed. If positive densities pi and q have the two fixed marginals and are both multiplicative scalings of k, then `log(pi/q)=h(U)+h'(U')`. Consequently

`D(pi||q)+D(q||pi)=integral (pi-q) log(pi/q)=0`.

The equality uses just the identical marginals. Nonnegativity of relative entropy follows from `log x<=x-1`; equality forces pi=q. Compactness and positive continuous factors ensure integrability. Moreover, for any coupling eta with the same marginals, its relative entropy against the normalized reference k differs from that of pi by `D(eta||pi)`: the additive log scaling integrates to the same number. Thus pi is indeed the static entropy-minimizing bridge. Its disintegration determines P and its spectrum. This holds for the infinite-time ground-state slice law, not an arbitrary finite periodic marginal; that distinction matters at INC-FP below.


## 4. B2: Hopf bound — HOLDS AFTER CORRECTION

**S 202–205, 373, E3.** The SU(2) bound and constant hold. The extension to an unspecified compact-group action needs the actual hypothesis `exp(-beta_t)/c <= w <= exp(beta_t)/c`, and nonnegative spectrum if `E_1=-log r_1` is to be read literally. Normalized real-character Wilson weights meet the range hypothesis. Compactness alone does not set a kernel's oscillation.

A hand derivation verifies the Hopf constant without importing its proof. Ground-state conjugation turns T into P and preserves cross-ratios. For two rows of P the density ratio h lies in [m,M], with `M/m<=kappa` and mean one. Convexity of `(h-1)_+` gives total variation at most `(1-m)(M-1)/(M-m)`. Its maximum, subject to `M/m<=kappa`, is `(sqrt(kappa)-1)/(sqrt(kappa)+1)`, attained at `m=1/sqrt(kappa)`, `M=sqrt(kappa)`. Thus

`osc(Pf) <= tanh(log(kappa)/4) osc(f)`.

A nonconstant eigenfunction has positive oscillation; apply the inequality to it. Eigenfunctions with nonzero eigenvalue are continuous by the continuous kernel. This proves the quoted spectral bound. The factors `exp(-V/2)` cancel in the cross-ratio. Averaging products of N_b bond kernels keeps their range, so `kappa<=exp(4 beta_t N_b)` and `r_1<=tanh(beta_t N_b)`. Finally, with `q=exp(-2 beta_t N_b)`,

`-log tanh(beta_t N_b)=log((1+q)/(1-q))>=2q`.

Since N_b=3|B|, the claimed `E_1>=2 exp(-6 beta_t|B|)` follows. At beta_t=0 the kernel has rank one and the excited energy is infinite. No bound uniform in spatial volume or cutoff follows. S's further sharpness assertions at b=infinity are not established by this argument.


## 5. T2: cut and reglue — HOLDS; four-direction consequence — HOLDS AFTER CORRECTION

**S 271–273.** Cancelling the two positive junction kernels under the product measure leaves exactly the 2t-cycle integrand. All spatial potentials remain once per slice. This proves `E[R]=Z(2t x B)/Z(t x B)^2=Tr rho_t^2`.

**S 274.** The claimed four-factor product misses powers. Write Z_j for the torus with j sides doubled and let `q_j=Z_(j+1)/Z_j^2` be the successive reglue expectations. The correct formula is

`exp(-16 D_0)=q_0^8 q_1^4 q_2^2 q_3`,

not the product of four unweighted means. This follows by cancelling each intermediate log Z_j. Calling `Tr rho_t^2` a collision probability holds for independent draws from the spectral probabilities `lambda_i^t/Z(t)`. It is not the probability that two continuum-valued field configurations coincide. S 280, 291, 376 draw an additional, invalid inference from that phrase; see section 8 below.


## 6. Free-energy bounds at beta=2.5 — HOLDS AFTER CORRECTION

**S 281–284, 364, 377.** Three corrections are necessary: use the unshifted weight `exp(beta sum A_p)`; specify the thermodynamic free energy for the stated Holder upper bound; round the lower bound downward. S 40 instead uses `exp[-beta sum(1-A_p)]`. For that convention every free energy below is decreased by beta.

Put `c(x)=2I_1(x)/x`, and let f be the thermodynamic log partition function divided by the number of plaquettes, for the unshifted weight. The valid statement is

`(1/2)log c(beta) <= f(beta) <= (1/3)log c(3 beta)`.

For the lower bound, the electric-only partition function is `c(beta)^(3V) Tr(K^t Pi_G)>=c(beta)^(3V)`. Jensen on the spatial action contributes zero mean. The zero mean itself holds: multiplication by a fundamental spatial plaquette changes the parity of the representation on each of its four distinct bonds, while K and Pi_G preserve every bond-spin block. Thus its diagonal trace vanishes. The time-like plaquettes are **not independent on a periodic torus**; this trace argument supplies the correct lower bound nonetheless.

For the upper bound, Holder with exponents 3 separates the three disjoint orientation pairs. Within each pair, each factor is a two-dimensional gauge theory. On a periodic plane of A plaquettes its partition function is

`c(3 beta)^A sum_(j>=0) u_j(3 beta)^A`,

by integrating the character expansion on the torus (the dimension power is Euler characteristic zero). The second factor exceeds one at positive coupling. It cannot be omitted in a finite-torus upper bound. Its logarithm per area tends to zero as both plane sides grow: trace summability bounds the sum uniformly for A>=1. Thus the displayed Holder bound follows in the thermodynamic limit. For a finite four-torus the missing correction is `1/(18V)` times the sum of these logarithms over the six families of coordinate planes.

The printed `0.350` rounds **up** from `(1/2)log c(5/2)` and is not the lower endpoint proved by that calculation. A safely stated hand interval is `0.349 < f(5/2) < 1.40`. Here are reproducible rational checks, using `c(x)=sum_(k>=0)(x^2/4)^k/[k!(k+1)!]`:

* The first five terms at x=5/2 exceed 201/100, while the exponential series with its geometric tail gives `exp(349/500)<201/100`. This proves the lower endpoint.
* Put `t_k=(225/16)^k/[k!(k+1)!]`. Then `c(15/2) <= sum_(k=0)^11 t_k + t_12/(1-225/(16*13*14)) < 200/3`. On the other hand `sum_(n=0)^16 (21/5)^n/n! > 200/3`. These finite rational inequalities, obtained by common denominators, prove `log c(15/2)<21/5` and hence the upper endpoint. No Bessel decimal is an input.

To see the rounding issue directly, the same series gives `c(5/2)<2.0134`, whereas the first six exponential terms give `exp(7/10)>2.0134`. The result of the lower-bound formula is strictly below 0.350. This does not refute the possibly stronger true inequality `f>=0.350`; it refutes its stated derivation and numerical endpoint.

**S 364 — HOLDS AFTER CORRECTION.** For the specific fully disseminated event `A_p<=a` on one orientation, the five remaining orientations and Holder give the thermodynamic bound `log q <= beta a + (5/3)log c(3 beta)-6 f_lower`. The factor 5/3 is correct. The safe numbers just proved give `log q < 2.5a+7-2.094=2.5a+4.906`. This upper estimate is greater than one after exponentiation for all a>=-1, hence uninformative. It says nothing about all chessboard events. Finite-torus applications must retain the plane corrections. The recalled true value 0.78 and the asserted required accuracy 0.1 are guides, not proved facts.


## 7. The four claimed refutations

### 7.1 Coulomb lower bound — FAILS as a proved refutation

**S 235, 383.** The text invokes small-volume tunnelling, attributed to Luescher and van Baal, without a stated estimate, its hypotheses, or a proof. It labels the paragraph ARGUED but later calls it refuted. No exact finite-volume asymptotic is derived here. The conclusion “no Gauss-law lower bound ... exists” is also broader than the one displayed Coulomb candidate. The available evidence supports only: *the proposed Coulomb lower bound is challenged by recalled small-volume electric-flux asymptotics; it has not been refuted by a written argument in this note*. This verdict does not assert that the recalled asymptotic or the physical objection is false. No Coulomb bound is used downstream.


### 7.2 Integrating the Hessian commutator by parts — HOLDS AFTER CORRECTION

**S 226, 384.** The naive replacement of an individual plaquette gradient by the Gibbs score is invalid. If `S=beta sum_q s_q`, Haar integration by parts in a link direction X gives exactly

`beta E[(X s_p)F] = E[XF] - beta sum_(q!=p) E[(X s_q)F]`.

It produces the displayed remainder rather than eliminating beta. This checks the stated failure of that substitution. It does not refute every integration-by-parts reorganization. The size “about sqrt(beta) per link” is not derived, and needs field-size information about the measure. Correct the claim to the explicit identity and the failure of the naive substitution; delete the unproved remainder scale and the blanket refutation.


### 7.3 Independent-plaquette upper bound — HOLDS AFTER CORRECTION

**S 284, 385.** Its universal upper-bound interpretation is false, but the asserted value near beta=2.5 is numerical guidance, not a refutation there. A separate hand counterargument for sufficiently large beta is enough to disprove the universal claim.

Use unshifted weights on a four-torus. Restrict every link's SU(2) class angle to `delta=1/(4 sqrt(beta))`, beta>=1. A plaquette angle is at most 4delta, so `A_p>=1-1/(2 beta)`. Haar probability of this cap is at least `8 delta^3/(3 pi^3)=beta^(-3/2)/(24 pi^3)`, using `sin theta>=2theta/pi`. There are 4V links and 6V plaquettes. Thus, in every such volume,

`f(beta) >= beta - 1/2 - log beta - (2/3)log(24 pi^3)`.

Meanwhile `cos theta<=1-2theta^2/pi^2` and `sin theta<=theta` give

`c(beta) <= C exp(beta) beta^(-3/2)`,

where `C=(2/pi) integral_0^infinity x^2 exp(-2x^2/pi^2) dx` is a finite explicit constant. Hence `f-log c >= (1/2)log beta - 1/2 -(2/3)log(24 pi^3)-log C>0` for sufficiently large beta. This is a hand refutation, independent of Monte Carlo and Bessel decimal values. It does not prove `f(2.5)>log c(2.5)`. The first failing step in S's advertised beta=2.5 refutation is using its GUIDE value as evidence.


### 7.4 Coupling path as an equivalent restatement — FAILS

**S 231, 386.** The forward implication holds: for a differentiable eigenbranch, `T'=-(NT+TN)/2` gives `E_i'=<N>_i-<N>_0`; the stated logarithmic derivative bound implies the Gronwall lower bound. At crossings one needs the corresponding almost-everywhere branch or minimum-eigenvalue formulation. At the normalized electric endpoint and spatial sides >=4 the shortest nontrivial spin network is a four-edge fundamental loop, so `E_1(0)=-4 log u_(1/2)`.

The first false implication is “Conversely a positive differentiable E_1 has such a C at each b. So ... equivalent ...”. The forward premise asks for C **uniform in B**, with enough control to integrate along the path. Pointwise positivity in each finite box supplies neither. Even positive smooth functions uniformly separated from zero, `E_L(b)=2+(1/2)sin(Lb)`, have no volume-uniform bound on `|E_L'|/E_L`. This is a counterexample to the claimed analytic inference, not a model of Wilson theory. B2 already proves positivity in each finite box for the entire magnetic path; that fact plainly supplies no thermodynamic seed.

Correct conclusion: the uniform path inequality is a sufficient, still-open estimate. S does not show it equivalent to absence of a critical point, or prove that every path method is merely a restatement. Its own attempt supplies no bound for SHIFT. That limited negative conclusion holds.


## 8. T2's probabilistic obstruction — FAILS

**S 280, 285, 291, 376, 431.** Jensen and `E log R=-2J` hold. Since `E R=Tr rho_t^2<=1`, Jensen also proves J>=0. But no estimate in S proves that J is extensive, that R is negligible on typical configurations, or that rare near-coincidences dominate its mean. The actual normalized likelihood ratio of the reglued law against the two-copy law is `R/E[R]`. It is not the adjacent-slice versus independent-slice likelihood ratio asserted here.

The claimed implication from T2 is false within its own class. Take beta_t=0, so `k_orb=1`, with any magnetic potential V. Then `T=h tensor h`, `h=exp(-V/2)`, S=0, R=1 for every pair of configurations, and J=0 in every volume. The seed is exact and ordinary configurations supply its entire mean. A less degenerate positive rank-one kernel gives the same cancellation. Thus T2 does not rule out typical-configuration estimates or require a collective rare-event proof. For order-one Wilson coupling, whether Jensen loses an extensive exponent remains a separate unproved estimate. The identity holds; this claimed obstruction does not.


## 9. Skeleton N1–N8 and the split of N6

### N1 and the target introduction — HOLDS AFTER CORRECTION / FAILS at S 16

**S 49, K0.** The representation and exact mass statement match SA 17255–17290 and CA-I 2533–2583. They remain conditional/cited upstream inputs. CA-I 4209–4221 explicitly assumes `g_0,...,g_K in (0,gamma]`; `lit-balaban.md:147` records precisely this small-coupling hypothesis for Tadeusz Balaban's CMP 122b Theorem 1. The outline's first-passage definition, SA 6854–6882, fixes a **small** reference g. This contradicts S 16's claim that those steps reach order-one effective coupling. Correct S 16 to: *They reach first passage at a fixed small reference coupling. Control through the later order-one regime is missing.*

An `exp(O(ell^4))` residual control does not establish a small doubling defect. S 290's claimed cancellation of all extensive local terms is withdrawn correctly at S 363. Neither locality nor equal total mass identifies the block-field law with a nearest-neighbour Wilson transfer chain. Use the bare Wilson transfer operator for the spectral identities, and the effective density only through its exactly preserved total mass. This distinction is explicit in `gap-finishline-opus.md:136–150` and CA-I 2556–2560.


### N2 — HOLDS

**S 51, K1.** For the bare positive-coupling Wilson theory on the stated finite spatial torus, SA 2195–2257 and 2313–2336 supply the positive trace-class transfer construction. The sandwiches `K^(1/2)e^(-V)K^(1/2)` and `e^(-V/2)K e^(-V/2)` have the same nonzero spectrum and traces. The strictly positive orbit kernel gives a simple positive top eigenfunction. Each centre flip preserves positivity and commutes with T, so it fixes that eigenfunction rather than negating it. Inserting the temporal seam yields `Tr(T^t C^k)` and the stated sector expansion. At beta=0 remove the assertion that every excited eigenvalue is positive; the operator has rank one. This endpoint is used only with S=0. No assertion about a transfer operator for the RG block law follows.


### N3 — HOLDS

**S 53–57.** The finite group average of `(-1)^(k.e)` is one for e=0 and zero otherwise. Dividing its trace by Z proves (a); factoring the even trace proves (b). This is exactly `gap-mid-max.md:219–227`, Identity FL. The split is established prior work; no new flux estimate follows.


### N4 — HOLDS AFTER CORRECTION

**S 59–63.** The identity, `S(2t)<=S(t)^2`, and the two printed inequalities hold. The proof of `D<=1/10 implies S<=D` skips the premise S<=1 that it uses. Supply it without assumption: also `S(2t)<=S(t)`, so `exp(D)>=(1+S)` and `S<=exp(1/10)-1<=1/9`. Then

`D >= 2 log(1+S)-log(1+S^2) >= 2S/(1+S)-S^2 >= S`

for `0<=S<=1/9`. The middle inequalities follow by integrating `1/(1+x)` and using `log(1+x)<=x`. This repairs the proof and verifies its constant. The purity interpretation is spectral, as distinguished in section 5.


### N5 — HOLDS

**S 65.** In the original normalized-action convention, `d log Z/db=<A>-#p`. Since the doubled torus has twice as many plaquettes, the constants cancel in `2 log Z(t)-log Z(2t)`. Haar gives Z=1 at b=0. Integrating proves the formula. It estimates nothing until the finite-size shift is bounded. The prior isotropic version is Proposition MIX; the anisotropic path identity below is the same differentiation with only spatial plaquettes varied.


### N6 — HOLDS as the stated open hypothesis

**S 67.** This is precisely SEED-FP in `gap-finishline-opus.md:115–123`, with the integer requirement `ell/(2a_K)>=3`, a fixed physical ell and a fixed strict margin, for every sufficiently fine first-passage datum. It is not newly proved, and no number in S verifies it. It refers to the bare Wilson transfer spectrum.


### N7 — HOLDS as the cited conditional implication

**S 69, K3.** `gap-crux-restate.md:170–223` supplies Theorem S and the repaired Corollary S3': `s=S(N;(2N)^3)<1/5041`, N>=3, gives `m(L^3)>=log(1/(5041s))/N` for every integer L>=2N. The corrected all-integer-side statement, not the false binary-factorization proof of the older S3, is required. The source assumes positive transfer traces in all directions, axis exchange and a finite pressure lower bound. These hold for the bare isotropic Wilson model. They do not follow from time-reflection positivity alone and do not apply to A2's anisotropic endpoint. The coefficient is correctly copied; no reproof of this existing theorem is claimed.


### N8 — HOLDS AFTER CORRECTION

**S 71, K4.** Retain the continuum reconstruction/convergence datum as a named open input. The source `gap-finishline-opus.md:152–163` marks its matching step (e) and composition (f) ARGUED, not proved. Given those inputs and N7, the physical rate is correctly converted:

`[log(1/(5041s_*))/N]/a_K = 2log(1/(5041s_*))/ell`.

The conclusion concerns the reconstructed tr(F^2) Hilbert space and its volume-first limits. It is not automatically a theorem about every observable of Yang–Mills, nor about every continuum limit procedure. K4 states this conditional boundary more honestly than the abbreviated N8.


### C-a, C-b, C-c and W-fl, W-gap, W-hs — HOLDS AFTER CORRECTION

**S 75–80, 124–132.** The flux average gives `1-p_0<=7s_a/8`. For the even excited spectrum the half-time bound gives `S_ev(t)<=M exp(-mu ell/4)`; hence the displayed bound on 1+S is correct. State explicitly `7s_a/8<1` and

`[1+M exp(-mu ell/4)]/[1-7s_a/8] <= 1+s_*`.

Positive mu and finite M alone do not guarantee the target seed at a preselected ell. At the half-times use integer divisibility or real spectral powers; no literal fractional lattice slice is defined. W-hs at n/4 is the Hilbert-Schmidt bound for P^(n/4), whose square is the even trace at n/2. W-gap gives its further decay to time n.

The three bounds are sufficient conditions. Calling them *the conjunction equivalent to WINDOW* needs either these explicit constants or a quantified formulation allowing the gap and state count to be extracted from an already small full seed. A single upper bound on the **signed integral** SHIFT is not equivalent to a pointwise gap/multiplicity estimate at every intermediate coupling. Cancellations along that integral are allowed. No such path equivalence was proved in S 168–170.


## 10. Remaining identities and local calculations

### I1 — HOLDS

**S 106–110.** Normalize Omega in Haar L^2. Ground-state conjugation is unitary onto L^2(nu), preserves eigenvalues after division by lambda_0, and maps Omega to 1. With `g=e^(-V/2)Omega`, the eigenvalue equation gives `Kg=lambda_0 e^V g`; substitution gives the printed kernel. Here K means the gauge-projected electric orbit kernel. A product-kernel lift acts identically on invariant functions, but is not the pointwise orbit kernel. In particular the statement at S 136 about the product conditional law must be read in such a lift, not as deleting gauge averaging between two fixed orbits.


### I2 — HOLDS

**S 112–115.** The spectral expansion of `P^s-Pi_1` has Hilbert-Schmidt square `sum_(i>=1) r_i^(2s)=S(2s)`. This equals the integral of `(p_s-1)^2` against nu times nu and hence chi-square divergence. Trace class on the compact finite lattice gives the required convergence for integer s>=1. The statement about slices is for the stationary **infinite-time** chain; n/2 must be an integer for a literal slice interpretation. It is not the two-slice marginal of the n-periodic thermal measure.


### I3 — HOLDS

**S 117.** In a tensor eigenbasis, `Tr[(T^t tensor T^t)SWAP]=sum_i lambda_i^(2t)`. The antisymmetric projection is `(I-SWAP)/2`. Dividing its trace by `(Tr T^t)^2` gives half the purity deficit exactly. This is the odd sector of replica swap, not the electric centre sector. It introduces no estimate.


### I4 — HOLDS AFTER CORRECTION

**S 119.** The seam insertion identity holds. Centre flips leave the spatial potential unchanged, so inserting C in one junction changes just its orbit kernel. Dividing the twisted integrand by the untwisted one and averaging gives the displayed ratio. Unlike I2, this expectation is correctly taken in the finite periodic time measure.

**S 120, corrected at 360.** The h integral is a three-dimensional SU(2) spin model with rotations specified by both backgrounds; at a flat representative it reduces to the ordinary O(4) interaction, with the corresponding twist. No proof in S establishes a global supremum over all backgrounds at that representative. The useful checked claim is the conditional flat-background countertest from row 839, not extremality. Its Froehlich–Simon–Spencer input remains the named external premise of that earlier result.


### A1 — HOLDS AFTER CORRECTION

**S 144–146.** For SU(2), a centre-odd spin network has an odd number of half-integer edges crossing each homologous cut. The disjoint n_2 cuts therefore require at least n_2 nontrivial bonds. Since each such bond has normalized eigenvalue at most `u_(1/2)`, the operator bound follows. The same method works for another compact group only after defining the supremum q of the one-link eigenvalues carrying odd centre character; its conclusion is `K|H_odd<=q^n_2`. The symbol `u_(1/2)` and the Bessel formula are SU(2)-specific. Magnetic multiplication commutes with the centre flips; it changes energies within flux sectors, not the conserved sector labels themselves.


### Path identity 3.3 — HOLDS

**S 159–162.** Differentiate `log Tr T^t-t log lambda_0` in the spatial coupling. The simple ground eigenvalue obeys Hellmann–Feynman; the derivative of each half-potential contributes one half of the same slice action expectation. The result is the finite periodic expectation minus t times the infinite-time slice expectation. The constants in `1-A_p` cancel as in N5. The signed integral identity is exact. The comparison of this unestimated integral with pointwise mixing or gap bounds in S 168–170 is not an equivalence; section 9 states the corrected scope.


### B3 — HOLDS AFTER CORRECTION

**S 209–214.** Reversibility gives `E_pi[(f'-f)^2]=2<f,(I-P)f>`. The Rayleigh principle proves the formula, with the infimum over nonconstant mean-zero functions. On the even sector replace r_1 by its largest **even excited** eigenvalue. Nonnegative spectrum makes this equivalent to the operator-norm contraction with `1/(2C)=1-exp(-mu a)`.

The continuous-time sentence is correct only for the separately specified electric Hamiltonian `H=-Delta/2+V` in the stated metric. Ground-state conjugation then gives the form `(1/2)integral |grad f|^2 dnu`. The logarithm of a finite-time Wilson transfer operator is not asserted or shown to have that local differential form. It cannot be substituted without a continuous-time limit argument.

The one-mode Gaussian calculation holds if sigma denotes **variance**. If c is the covariance of the two coordinates, the Gaussian inverse-covariance cross term fixes `c/(sigma^2-c^2)=1/eps`; solving gives exactly `r=c/sigma=sqrt(1+(eps/(2sigma))^2)-eps/(2sigma)`. Its small-eps/sigma expansion gives `-log r~eps/(2sigma)`. The photon interpretation remains the stated free-field comparison, not a new statement about compact U(1) at all couplings.


### Hessian calculation and curvature discussion — HOLDS AFTER CORRECTION

**S 218–225.** For the Casimir metric `|X|^2=-2tr X^2`, SU(2) is the round three-sphere of radius 2, so Ric=1/2. With `X=i x.sigma/2`, `Y=i y.sigma/2`, the identity `XY=-(x.y)I/4-i(x cross y).sigma/4` gives the printed mixed Hessian when y is transported to the specified ordered base point. The diagonal second derivative is `beta cos(theta)|x|^2/4`. Reversing a bond or the ordered insertion requires the corresponding transported sign; the formula is not orientation-free.

For the electric continuous-time Hamiltonian, Haar has `phi=0`; the Ricci criterion yields the loose bound 1/4. The first gauge-invariant loop has four fundamental links, with energy `4*(3/4)/2=3/2`, provided the torus sides are at least four. This is consistent with A2, but it is not the finite-time Wilson gap in B2.

The estimate from 18 neighbouring links is a crude worst-case sufficient-condition test, not a proof that the ground-state law has negative curvature. S 227 conflates the Hessian of the full four-dimensional action with the Hessian of `-2log Omega` on a slice. The former's loss of a pointwise Bakry–Emery lower bound does not prove the latter fails. Correct STOP 1/2 to: *No lower bound for the vacuum-density Hessian was supplied; the direct raw-action criterion fails outside its small-coupling regime.* The exact-one-form Witten reformulation is an equivalence for the specified continuous-time diffusion, and supplies no new estimate. Section 7.2 treats the integration-by-parts attempt.


### T1(a)–(d) — HOLDS

**S 251–256.** Interpret isotropic reflection positivity here as the full trace hypothesis N2 in every direction, with a finite bulk pressure. Relabelling proves (a); monotonicity of sequence l^p norms proves (b). The decreasing pressure net has infimum p_inf; comparison with any fixed rectangle proves (c), including iterated limits. For (d), the limiting pressure with spatial box B fixed is at least p_inf and increasing three sides lowers pressure. Consequently `log(1+S(n;(2n)^3))<=8F(n)`. This is precisely the ratio-2 case of the earlier Proposition Delta, `gap-mid-max.md:144–146`, not a new reduction.


### TORUS threshold and the two formulas for F — HOLDS AFTER CORRECTION

**S 258.** Use the strict inequality `F(n)<(1/8)log(1+1/5041)` to obtain the strict seed N6. The printed non-strict endpoint gives only `S<=1/5041`, which does not give N7's positive rate. A safely smaller non-strict constant also works. The decimal `2.48e-5` is a rounded guide, not the exact threshold.

**S 259 — HOLDS.** Put `G_k=log Z((2^k n)^4)` and `D_k=G_k-G_(k+1)/16`. Then

`sum_(k=0)^m 16^(-k)D_k=G_0-16^(-(m+1))G_(m+1)`.

The last term tends to `n^4 p_inf`. Thus the printed decaying weights are correct; D_k>=0 by pressure monotonicity. This also resolves the preliminary concern mentioned during this check.

**S 260 — HOLDS AFTER CORRECTION.** The thermodynamic pressure is convex and uniformly Lipschitz in beta on finite intervals, so it is absolutely continuous and differentiable almost everywhere. Define `P_inf=p_inf'/6` almost everywhere in the unshifted convention, or `(p_inf'+6)/6` in the original convention. Then the fundamental theorem of calculus gives the formula. Do not silently replace this derivative by an arbitrary state's mean at a coexistence coupling. A null set of such couplings does not affect the integral. This is the same convention already noted in the correction to Lemma 4.2 of `gap-mid-max.md:10`.


### Physical tests and additional claimed obstructions — HOLDS AFTER CORRECTION

**S 82, 86–100, 132, 136, 233–236, 262–267, 374–375, 413.** These are comparisons or proposed obstructions, not discharged steps. Keep the U(1), finite-subgroup, adjoint-matter, numerical coupling and glueball-gas claims as GUIDE or named external premises. In particular:

* The admission of the small-reference-coupling first-passage density is conditional. It does not imply that all three seed quantities depend only on physical ell, without residual datum/subsequence dependence (S 86).
* The small SU(2) Hessian calculation does not prove the proposed response bound, or that every successful method must use an average over typical backgrounds. F2 is only a test of a class that includes its matter theory, as S 361 correctly says.
* The Mermin–Wagner paragraph S 236 supplies no quantitative bound for the lowest adjoint covariant-Laplacian eigenvalue under the actual measure. An exactly covariantly constant axis is sufficient for an abelian reduction, not proved necessary for every useful deformation. The older `gap-crux-restate.md:157–159` already gives a restricted obstruction for deterministic link multiplications. Retain that scope; S's broader argument is not a new proved refutation.
* **S 265 — FAILS for its exact counting formula.** With normalized counting Haar measure in the flat limit of a finite group, `Z_flat=|G|^(-3V-1)|Hom(Z^4,G)|` on a four-torus. Its bulk-subtracted constant is `log(|Hom(Z^4,G)|/|G|)`, a sum weighted by inverse stabilizer sizes, not the logarithm of the number of gauge classes on the four-torus. Equivalently Burnside's lemma identifies it with the number of commuting triples up to conjugacy on the **spatial three-torus**. For a group with a nontrivial centre (including Q_8 and 2T), every stabilizer has at least two elements, so the two counts cannot coincide. For Z_2 the correct constant is log 8, not log 16. This flat-limit counting does not itself prove the finite-beta phase assertion. The qualitative warning about flux multiplicity survives.
* F(n)->0 is sufficient for a small seed by T1. S has not proved its converse from a gap alone, or an equivalence to the physical phrase “gapped and no topological sectors” without state-count assumptions.
* S 374's flat-slice step-variance estimate, its Z_2 area exponent, and the analytic neighbourhood width in S 375 are not derived. B2 supplies a finite-box real gap only. Analytic continuation needs a perturbation-norm bound as well; its neighbourhood is not quantified by the real gap alone.
* INC excludes every slow mode in the tested sector, including a tunnelling/bottleneck mode. S 413's identification of INC specifically with absence of massless soft coordinates is too narrow. Its finite-volume energy lower bound is not an asymptotic determination of the actual splitting.

The negative conclusions that survive are limited: none of S's three attempted estimates closes WINDOW. They are not an exclusion of all tools of the named kinds.


## 11. Step 6 map, checked against the earlier statements

These verdicts concern the stated correspondence, not a new check of every prior theorem. A previous label “checked” is reported provenance, not evidence replacing its source. The source statements below were read. In particular, `gap-mid-max.md` and `gap-means-max.md` credit Claude Fable 5.2; `gap-means-astra.md` credits Codex gpt-6-astra; `gap-compress-opus.md`, `gap-finishline-opus.md` and `gap-handoff-opus.md` credit Claude Opus 5.5. The Sussman–Alpoge and Balaban inputs retain the limits already recorded.

| S line and item | Earlier statement read; verdict on the map |
|---|---|
| 317, N2 | **HOLDS.** The same positive transfer-trace input; SA GL3/GL8 and `gap-crux-restate.md:170–176` fix its actual scope. No block-law transfer theorem is added. |
| 318, N3 | **HOLDS.** `gap-mid-max.md:219–227`, Identity FL, is exactly `1+S=(1+S_0)/(1-U)`, with `U=1-p_0`. |
| 319, N4 | **HOLDS AFTER CORRECTION.** `gap-seed-shape.md:165–181`, D-shape, gives `g<=Phi_B<=2g` and a sufficient defect threshold. It does not say `S<=t` iff `Phi_B<=log(1+t)` at the same t. `gap-compress-opus.md:16–20,38–53` records the purity/Renyi and chi-square forms. |
| 320, N5 | **HOLDS.** D-shape(d) and `gap-mid-max.md:254–275`, MIX, already express the defect as an integrated plaquette shift. `gap-skeleton-final.md:630–644` maps the even-seed shifts. |
| 321, N6 | **HOLDS.** `gap-finishline-opus.md:115–123` is the exact SEED-FP definition. It is open, not a result ported as true. |
| 322, N7/N8 | **HOLDS AFTER CORRECTION.** Theorem S/S3' and `gap-seed-shape.md:87–126` give the stated thresholds, `1/1650` at ratio 2 and `1/25` at ratio 4. The continuum datum remains an extra premise (`gap-finishline-opus.md:152–163`). Thresholds do not by themselves prove that datum. |
| 323, C-a/b/c | **HOLDS.** Identity FL and `gap-means-astra.md:617–682` distinguish the even gap from the additional state count M5-H. Neither is supplied at order one. |
| 324, F1–F3 | **HOLDS AFTER CORRECTION.** `gap-crux-fp.md:270–274` requires a countermodel in the tool's actual class with its hypotheses true. The numerical subgroup/adjoint comparisons are guides. The genuine model-specific ceiling in `gap-blockcrit-opus.md:266` concerns its particular influence matrix, not every curvature or averaging method. |
| 325, I1/B3/INC | **HOLDS AFTER CORRECTION.** M5-G (`gap-means-astra.md:617–644`) is at fixed **physical time**, on the infinite-time ground-state law, uniformly in cutoff and large spatial cubes. The discrete increment identity is the same variational mechanism; changing these quantifiers is not an identical statement. |
| 326, I2 | **HOLDS.** `gap-compress-opus.md:38–46` gives exactly `I_chi2(X_0;X_n)=S(2n;B)`. S uses the correct factor two. |
| 327, I3 | **HOLDS.** `gap-compress-opus.md:16–20,49–53` records the order-2 purity/free-energy identity. Replica swap is an algebraic restatement; the antisymmetric-sector wording is not a new estimate. |
| 328, I4 | **HOLDS.** `gap-crux-fp.md:367–386`, Identity L, is the same background-layer ratio with the same periodic expectation. Its Durhuus–Frohlich provenance is credited there as a recalled method. The area-law note supplies a different conditional covariance/slab argument, not a new proof of I4. |
| 329, A1 | **HOLDS AFTER CORRECTION.** `gap-hs-max.md:168–181`, P1/P2, already gives odd cut parity and the high-spin restricted-trace comparison. It supplies the same parity mechanism. Its interacting high-spin estimate is not literally a stronger version of A1's electric-only operator norm at all j and volumes. |
| 330, A2 | **HOLDS within the searched corpus.** `gap-brainstorm-max.md:317`, idea 32, names the anisotropic endpoint and continuation; it contains no A2 trace/polymer estimate. A2's quantitative statement is additional to that idea, with the normalization and numerical corrections above. No claim of worldwide novelty follows. |
| 331, SHIFT | **HOLDS AFTER CORRECTION.** MIX gives an isotropic sufficient mixing input; S gives an anisotropic identity; `gap-exit-max.md` PATH is another signed path comparison. They expose a related unestimated quantity, not identical quantified premises. |
| 332, “virial = no critical point” | **FAILS as an equivalence.** `gap-mid-max.md:118–140` states TR and LEV as sufficient conditions; it does not justify S's missing volume-uniform converse. Theorem CRIT describes the boundary of the seed set, a different exact assertion. |
| 333, curvature | **HOLDS AFTER CORRECTION.** `gap-mid-max.md:10` explicitly narrows BE to a ceiling beta<=1/3, without proving the positive side. This is about its raw-action criterion. It does not establish S's asserted failure for the unknown vacuum-density Hessian. K7 remains a model-class guide. |
| 334, B1 | **HOLDS within the searched corpus.** No prior bridge-scaling lemma was located under the searched terms. The ground-state transform itself was already in M5-G. The new structural observation supplies no gap estimate. |
| 335, B2 | **HOLDS AFTER CORRECTION.** `gap-compress-opus.md:20` expressly lists the unread Birkhoff lead. B2 answers that finite-kernel lead, with the kernel-range hypothesis in section 4; it is not a bound for arbitrary unspecified compact-group actions. |
| 336, 4.6 | **HOLDS AFTER CORRECTION.** `gap-skeleton-final.md:547–564` labels small-volume flux degeneracy **recalled**. `gap-crux-restate.md:157–159` already discusses a restricted Mermin–Wagner deformation obstruction. S's covariant-axis explanation is an additional heuristic, not a new refutation. `gap-sep-check-astra.md:244,258` indeed rejects the exhaustive six-candidate exclusion. |
| 337, T1/TORUS | **HOLDS.** `gap-mid-max.md:144–146`, Proposition Delta, already gives `g(a;b^3)<=(b/a)^3 Delta(a^4)`. S's bound is its r=2 case. Theorem S's `Phi<=1.9e-4` uses two finite tori; S's F needs the bulk pressure. The older BDD-Delta/Z-UNB architecture is recorded at `gap-skeleton-final.md:555–564`. |
| 338, two tests in F | **HOLDS AFTER CORRECTION.** The earlier qualitative comparisons already exist; they do not prove S's four-torus flat-class counting formula, which fails as recorded in section 10. |
| 339, T2/Stage 1 | **HOLDS AFTER CORRECTION.** M/MIX (`gap-mid-max.md:254–275`) is a marginal-cut/mixing argument, not T2's reglue expectation. T2 is additional algebra. Neither M/MIX nor the source's label “annealed” proves that all typical-configuration estimates fail. |
| 340, hand f bounds | **HOLDS AFTER CORRECTION.** `gap-s1-opus.md:240–254`, BAD, is stated for beta>=1, not only large beta; its explicit bound is useful only when its prefactor is overcome. It does not provide S's order-one two-sided pressure calibration. That calibration needs the repairs in section 6. |
| 341, F2 matter guide | **HOLDS only as a search/proposal report.** No matching guide was located in these searches. It was not read as a theorem and cannot refute tools outside the matter theory's class. |

### Step 6.2 and Step 7 corrections

**S 345–346 — HOLDS AFTER CORRECTION.** `gap-finishline-opus.md:165–170` records the centre-blind limit route. The exact ES definition and Theorem R are `gap-means-max.md:206–226`: `eps<=1e-7`, `delta<=1e-7` give **two of three** sector seeds; the third has `S_w>2`. ES does not imply the full periodic seed without determining which sector is excluded. The even scalar limit route is the appropriate alternative. This distinction survives the wording “one form for both halves”.

**S 347 — HOLDS as an open-input map.** `gap-sdcyl-ca-astra.md:250–270` gives the corrected physical-rate comparison `8Q_F<=K_F rho_CA^(A/(3d))<=K_F sqrt(S_ev)` **given** SD-cyl-CA and E17-phys-CA. It explicitly leaves the flux estimate and the glue estimate unproved. The current C2/EXC records do not close them: `gap-ha-astra.md:714` and `gap-exc-astra.md:419` both end OPEN. The dual wrapping surface is the Poincare dual of the odd electric cycle; the cycle itself is not a surface in the original lattice.

**S 348, 367 — HOLDS AFTER CORRECTION.** EXIT and HO are genuinely different sufficient architecture (`gap-handoff-opus.md:255–282`). EXIT requires exactness, a global Gibbs form, cross-torus consistency including the vacuum datum, entry to the open zone, and cutoff-uniform constants. Row 861 does not reduce this to locality alone: `gap-exit-max.md:840–850,875–883` also retains the vacuum constant and withdraws its optimistic soft-step claim through VAC/VAC2. Its PATH remains open. Do not drop that scalar normalization obligation when calling PIN-MIX “the crux”.

**S 349, 360–361, 365–366 — HOLDS AFTER CORRECTION.** The change from “frozen abelian” to flat background is right. Keep the conditional theorem/class qualification, and retain GUIDE on the subgroup transition values, K7 and adjoint-matter example. They are not newly checked phase diagrams.

**S 350, 362 — HOLDS as citations with scope.** The block theorem's exact endpoint is `(sqrt(37)-5)/3` (`gap-blockcrit-opus.md:176–187`), so 0.3609 is safely inside it. `gap-arealaw-opus.md:40–53` states the beta<2/3 rectangular area bound, with rectangle sides at most half the torus sides and its cited input lemmas. Theorem SH's threshold numbers match its table. These are lattice ranges, not cutoff-uniform continuum estimates.

**S 363 — HOLDS as a withdrawal.** The earlier cancellation assertion is not available; the source of BASE-Phi is the proposed architecture at `gap-skeleton-final.md:564`. BASE-Phi is an unproved proposed supplier, not a theorem that every possible proof of SEED-FP must use it. S 364's chessboard correction was checked separately above.


## 12. Final node statements and proposed next statements

| Final node, S 396–409 | Verdict and exact boundary |
|---|---|
| K0 | **HOLDS AFTER CORRECTION.** Conditional first-passage representation at small g; exact masses, not a known effective Wilson transfer law. See N1. |
| K1 | **HOLDS** for the bare Wilson operator with the positive-coupling/end-point conventions of N2. |
| K2 | **HOLDS AFTER CORRECTION.** The algebraic identities hold with N4's repaired inference, the stationary-law interpretation of I2, and T1's finite-pressure hypothesis. None is a seed estimate. |
| K3 | **HOLDS** with the trace/axis symmetry hypotheses, integer sides and strict seed margin recorded for N7. |
| K4 | **HOLDS** as a conditional chain retaining the open continuum datum and the tr(F^2) scope. It grants no theorem about a larger physical Hilbert space. |
| K5a | **HOLDS AFTER CORRECTION.** FL is a sufficient comparison using two admissible account tori and their preserved total masses. BASE-Phi remains a proposed open supplier. Exact bulk cancellation is neither established nor logically forced as the only possible route. |
| K5b | **HOLDS AFTER CORRECTION.** The even gap plus a suitable state count gives the glue bound. SHIFT/PATH are different sufficient or integrated formulations, not all proved equivalent to INC with the same quantifiers. The source's “equivalences are PROVED” is too strong. |
| K5c | **HOLDS AFTER CORRECTION.** The cited flux identities and conditional E17-phys-CA consumer are genuine prior inputs; C2/EXC remain open. A dual surface is not the original spin cycle. No transfer of these bare identities to an unproved twisted effective-block law is allowed. |
| K5' | **FAILS if read as equality of the full periodic seed and ES.** SEED is sufficient for the full periodic criterion. ES yields two of three sector seeds and the even-scalar route; it need not yield the periodic one. Correct the row to list these as different sufficient routes to their respective limit targets. |
| K5'' | **HOLDS AFTER CORRECTION.** HO is conditional on all EXIT clauses, including cross-torus vacuum normalization. PIN-MIX alone does not close the soft-step seed route; VAC/VAC2 explicitly preserves this additional obligation. |
| E1 | **HOLDS AFTER CORRECTION.** A2 gives an electric-only seed at each fixed beta_t after scalar normalization; its magnetic-coupling identity is exact but unestimated. |
| E2 | **HOLDS** as the scoped earlier lattice claims, with beta<0.3609 and beta<2/3 respectively. No statement at order-one coupling or along a continuum trajectory follows. |
| E3 | **HOLDS AFTER CORRECTION.** B2's SU(2) bound, and its extension to kernels with the stated log-oscillation bound. “Every group” alone is insufficient. |
| E4 | **HOLDS** for the infinite-time ground-state law and the electric orbit reference kernel. |

**S 411 — HOLDS AFTER CORRECTION.** The chi-square criterion is exact for stationary slices separated by **half the thermal time**: `S(n;(2n)^3)` measures slices separated by n/2. If “a box” means spatial side 2n, the separation is one quarter of that side, not half. “Twenty correlation lengths” is a guide, not a proved sufficient universal size. The thermal sum controls both flux and even excitations; an even-only criterion has the different ES consumer just described.

### KS-ZONE, S 419–426 — HOLDS only as an open proposal

The proposed uniform anisotropic estimates have not been proved in S. A2 proves the beta_s=0 seed for each fixed beta_t; it does not establish the proposed common `C beta_t log beta_t` time scale with the stated exponentially growing volume range. Its normalized electric spectrum does give the exact beta_s=0 gap. Extension to positive beta_s, a uniform expansion radius, and the assertion for the comparison groups remain unproved. Replace “provable now” and “it holds for ... as well” by “conjectured here”. This check does not start that separately proposed proof task.


### INC-FP, S 428–431 — FAILS as the stated B1/B3 identification

It switches from the infinite-time ground-state law to “the periodic cube” and then invokes B1/B3 as if the laws agreed. They do not. With temporal period T, the two-slice density is proportional to

`T^d(x,y) T^(T-d)(y,x)`,

whereas the stationary law is `Omega(x)T^d(x,y)Omega(y)/lambda_0^d`. Even the one-slice marginals generally differ. This is an operator identity issue, not a small boundary correction already known to vanish.

For a hand example, take the symmetric two-state Markov matrix with eigenvalues 1 and r, 0<r<1. Both slice marginals are uniform. Its stationary adjacent pair has correlation r. On a periodic ring of length T, the adjacent-pair correlation is

`(r+r^(T-1))/(1+r^T)`,

which is strictly greater than r for T>1. The same electric kernel and the same marginal therefore do **not** make this finite-ring pair the bridge of B1. One must keep the ground-state setting in that lemma.

Corrected proposal: use the bare Wilson **infinite-time** law `nu_K=Omega_K^2 dU`; let the pair law be `nu_K(dx) P_K^d(x,dy)`, `d=ceil(delta/a_K)`, on mean-zero gauge-invariant centre-even functions. Seek a uniform C in the increment inequality and a separate M5-H state count. Then the eigenvalue bound is `r_ev^d<=1-1/(2C)` and, for `a_K<=delta`, the physical gap is at least `-log(1-1/(2C))/(2delta)` (with the rank-one endpoint handled separately). This is the existing M5-G proposal in corrected notation. It remains open. B1 uniquely determines the one-step chain from `(k_orb,nu_K)`; it does not remove the unknown ground-state law or the state count.

## Disposition

The corrected A2, B1, B2 and T2 statements are finite-volume results. The conditional seed-to-gap architecture survives with the explicit law, normalization, threshold and continuum premises above. The claimed path converse and universal reglue obstruction do not survive. Neither the finite-periodic law nor ES can be substituted for its different ground-state or full-periodic counterpart. The Coulomb objection remains unsupported as a proved refutation; the exact flat four-torus class count is false as printed.

Only this research report was written. No source claim, registry entry, FINISH row, audit record or scientific status was changed. No numerical run, simulation or computer-assisted proof was used; shell operations performed source retrieval and file bookkeeping only. This check did not reprove the cited prior theorems or verify the recalled numerical phase and spectroscopy claims. The report is local and uncommitted; nothing was pushed.

RESULT: FAILS as written: the path converse, universal reglue obstruction, finite-periodic/ground-state identification, full-periodic/ES identification and flat four-torus class count fail; the core finite-volume lemmas and conditional skeleton hold with the corrections above. No open mass-gap input is discharged and no status is granted.
