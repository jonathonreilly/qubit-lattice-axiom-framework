# Repo search

Completed FINISH row 850 check at the pinned checkout. Search terms, refs, relevant source statements and their proximity to this target are recorded below. The conditional handoff needs corrections; its worked landing example fails.

# Gap handoff cross-check

Research text only; no scientific or audit status is granted. No computation discharges a proof obligation.

## Search record and prior statements

Checked by Codex (dispatch designation: gpt-6-astra xhigh), at `fff10a94877681121bbb9951637241f9c090f3da`. FINISH row 850. This is a check of our research text, not an audit. References H below mean `library/gap-handoff-opus.md` at that commit. Source proofs imported below remain named inputs; this does not recheck the vMF theorem, transfer construction, or all of rows 835–836. No numerical run is proof evidence.

The requested `library/prior/gap-handoff-check-astra.md` is absent. The November 8 repo digest concerns other targets; it supplies no handoff check. The registry search for `gap-handoff|O-SEED|O-BC|EXIT|GAP.*(BLOCK|VMF|SEED)` found no owner of this check. FINISH row 851 owns the separate literature search, not this check.

All five-ref searches used `git -C /Users/jonreilly/Projects/Physics grep -n -i -E`, the five requested refs `origin/main pr/10114 pr/10133 pr/10134 pr/10141`, and Markdown/TeX paths, capped with `head`. Exact terms `Lemma DC\*|Lemma PV|Theorem O-SEED|Theorem O-BC|gap-handoff|perturb.{0,35}Dobrushin|Dobrushin.{0,35}perturb` returned no hits. The initial unanchored `O-SEED` search matched unrelated “two-seed” text and is discarded. Broader method terms `Dobrushin|Holley.Stroock|von Mises.Fisher|free.energy defect` hit their cap; they are locators, not absence evidence. A follow-up on the soft-route and `research/ym4d` paths found these relevant sources, read at the indicated ranges:

| Source | Exact statement and closeness |
|---|---|
| `pr/10114:.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MGX.md:145–220` (also a hit on pr/10133) | Equations (6)–(8): `18 beta_W exp(nu)+epsilon_nu <= q_* < 1` implies `abs(Cov(f,g)) <= B_f B_g exp(-nu d)/(1-q_*)`, for an exact global interaction and its weighted mixed oscillations. This already supplies the general non-Wilson perturbation/comparison method. It also says a positive coarse marginal does not imply RP. It does not supply H's chord factor 1/4, star radius, or hypercubic defect constants. |
| `pr/10133:.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_CW_CROSSOVER_ATTACK.md:257–291` | CW′ assumes a reference block coefficient at most `1-2 eta`, a fixed number of RG steps, and `norm_V(gamma_(a,Lambda)-gamma_0) <= delta(eta,V)`, giving a coefficient below `1-eta`; source transport remains separate. It explicitly says nothing there supplies the nonperturbative landing. This is prior conditional handoff architecture, not a proof of EXIT or the specific new defect route. |
| `origin/main:archive/notes/docs/WILSON_STAGGERED_DEEP_FIBER_COARSE_GAUGE_GIBBSIANNESS_BOUNDED_THEOREM_NOTE_2026-07-12.md:125–167` | Equations (3.2)–(3.4) split an exponentially small interaction tail, use weighted Dobrushin comparison on the near part, then integrate a log-partition derivative. This is prior use of the truncation/interpolation method on a different constrained Wilson-staggered carrier, not H's theorem. |

No inspected hit supplies this line-by-line check. Credit the named lane authors, Dobrushin's comparison method, Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text), and Tadeusz Balaban's RG method. No original Balaban paper was available or imported.

## 1. Lemma DC*, first: HOLDS

H 119–131, especially (ii). Put `I=Lambda\D`, `R=(1-1/|I|)Id+Ctilde/|I|` and let `delta` be a column vector. The cited DC′ proof (`gap-seed23-opus.md:172–197`) gives `delta_I(P^t f) <= (R^T)^t delta_I(f)`, uniformly summable. Therefore

`(1/|I|) sum_t delta_I(P^t f)^T b <= delta_I(f)^T [(1/|I|)sum_t R^t] b = delta_I(f)^T G b`.

Thus the printed orientation is **G b**, not its transpose. Conditional expectation under mu_2 gives the telescoping estimate even though mu_2 is not stationary for P. Uniform convergence to h justifies passage to its limit. The boundary variation of h gives the other term exactly as in DC′. Path weights give respectively `alpha/(1-alpha)` and `1/(1-alpha)`; the triangle inequality supplies the two distances. No column-sum hypothesis on C is needed. If I is empty, f is constant and the conclusion is zero; this trivial case must precede the displayed definition of P. This is a complete proof given the stated kernel hypotheses, not merely argued.

## 2. Lemma PV, first leg: HOLDS

H 89–101. Compactness and the Lipschitz hypothesis let us subtract `inf V`. Subtracting the midrange of psi gives `|psi|<=1`. After these independent constant shifts, `N,N'>=1`, `Lip(e^V)<=e^theta ell` and `Lip(psi e^V)<=e^theta(1+ell)`. The exact quotient identity in H 98 uses `|A'/N'|<=1`, so its two terms sum to `e^theta(1+2ell)|F-F'|/4`. The cited Corollary V1 is precisely this transport estimate for any Lipschitz test, after rescaling (`gap-vmf-lip.md:209–220`). A constant test is handled directly. The second leg is valid for bounded measurable V′: dominated differentiation and the interval variance bound give `osc(V′-V)/2`. The sharp unperturbed coefficient is an imported input; its proof is not repeated. Both legs of PV are proved from that input.

## 3. O-SEED distance counts: HOLDS AFTER CORRECTION of the small-size proof

H 177, 179, 181. The two printed losses are correct. A centred support lies within `R+1/2` of `z*`. The seam strip has width `R+1`. Thus

`d(S,D_R) >= n/2-(R+1/2)-(R+1)=n/2-2R-3/2`.

For stars, an event is within R of a block link (Wilson range 1 is at most R). Two star-link midpoints are at distance at most 1. A bad star therefore lies within `2R+2` of the seam in some coordinate. Hence

`d(S,L_D) >= n/2-(R+1/2)-(2R+2)=n/2-3R-5/2`.

With `R=n/6` and `n/8`, these give exactly `e^(3m/2)e^(-mn/6)` and `e^(5m/2)e^(-mn/8)`. The star factor is 2, not `2 alpha`: its comparison series includes a zero-step term. Its weighted sum is a **column** sum because K transports the seminorm column, as BC Theorem R(a),(d) (`gap-blockcrit-opus.md:128–154`) states. With N=2Id, the inverse contributes 1/2 and a link belongs to at most two bad stars; these cancel.

The chord proof invokes DC* only for observables independent of D_R. Its printed weaker distance can be nonpositive at n=8,9, so that invocation needs a detail. Translate the *bounding box centre* of a lift of X, not just one link, to within 1/2 of z* in each coordinate. Its radius is then at most `R/2+1/2`. The seam gap is at least `n/2-3R/2-3/2=n/4-3/2>0` for n>=8. This is stronger than the printed bound. Translation is legitimate before gauge fixing since the original observable and law are translation covariant; its gauge-fixed expectation equals that original expectation. For stars no support exclusion is required by Theorem R(d); alternatively for n<=20 the elementary bound `|mu(h)-nu(h)|<=2 Delta(h)` is already bounded by the printed star coefficient. No correction to either exponential constant is needed. The remaining O-SEED hypotheses, especially the star-zone domain, are checked below.

## 4. Worked size n=226: FAILS as a worked landing example

H 189. With `beta=1/4`, `alpha=1/2`, `m=1`, even W=0 gives a chord left side `(9/8)e>1/2` and a tree left side `(3/4)e>1/2`. For stars `alpha_*(1/4)=17/31>1/2` even at m=0 and W=0. Adding W increases all three on their valid domains. Thus **no zone in the theorem admits these parameters**, independently of the chosen side. Changing n alone cannot repair this example.

The displayed constant is not *equal* to 56.0, but 56.0 is a valid **upward** rounding. The exact constant is `(62/5)e^(3/2)+2/5`. The Taylor sum through degree 6 is `4585/1024`. Starting with degree 7, each next term has ratio at most 3/16. Thus

`e^(3/2) <= 4585/1024 + 243/58240 < 2241/500`,

and the exact constant is below `56`. Replace the printed equality by an upper bound. This arithmetic correction does not repair the failed zone hypotheses.

The *isolated scalar inequality* with 56.0 and n=226 nevertheless holds by hand. We have `226^4=2608757776<2.61*10^9`. Also `e^3>20` by its Taylor sum through degree 8 (`89641/4480>20`), and `e^(5/3)>5` by the sum through degree 4 (`10009/1944>5`). Hence `e^(113/3)>20^12*5=20480000000000000`. Its first term is less than `0.224`; its second is less than `10^(-10)`. But `log(13/10)>3/10-(3/10)^2/2=51/200`. The expression decreases for n>=226 because `d(log(n^4 e^(-n/6)))/dn=4/n-1/6<0` (likewise for n/3). This confirms the arithmetic test independently while leaving the example invalid as an application. A valid example must first choose a positive zone margin and m, then recompute its size and round constants upward.

## 5. Zone definitions and Wilson thresholds: HOLDS AFTER CORRECTION

H 65–73 needs the domain of its rational star bound. Require `beta>=0` in all three zones, `0<alpha<1`, and, for O_ST,

`6x+u_m<1`, where `u_m=6(lambda(w_m)-1)x+w_m`.

On this domain `1-4x-6x^2>0`, all Neumann series used below converge, and the rational expressions are monotone. Without it the definition admits false branches: at beta=4, W=0 one has `alpha_*=-4/3`, u=0, so the printed O_ST left side is negative for every m and passes every positive alpha. Yet the Wilson free-star matrix has row sum 6x=6 and its resolvent series diverges. Thus H 73's asserted reduction at W=0 is literally false without the domain restriction; rational continuation past a pole is not a block criterion.

On the corrected domain the conditions at W=0 reduce to `beta<2/9`, `beta<1/3`, and `12x^2+10x-1<0`, respectively. The positive root in beta is `(sqrt(37)-5)/3`. Scaling beta,W by s in [0,1] decreases every relevant nonnegative expression and preserves the corrected domain. For fixed m the union over alpha<1 is open in the weighted interaction topology; individual closed-margin zones are not themselves open. The existence of some positive m follows from a strict m=0 inequality when a positive exponential moment is already finite, by dominated convergence. Small w_0 alone does not supply an exponential moment.

## 6. Zone radii: HOLDS AFTER CORRECTION; the 0.0042 star entry FAILS as a safe radius

H 75–85 gives rounded radii, not exact largest admissible w. At m=0 the exact chord/tree radius is the unique root of `c e^(2w)(1+2w)+w=1`, with `c=9 beta/2` or `3 beta`. The exact star radius solves

`6x[e^(2w)(1+2w)-1]+w=(1-alpha_*)(1-6x)/2`.

Strict inequality is required. These increasing functions give uniqueness of each root. A hand bound valid for `0<=t<5` is

`e^t <= U(t):=1+t+t^2/2+t^3/6+t^4/[24(1-t/5)]`.

It follows by bounding the tail from degree 4 geometrically. Substitution of the rational t=2w, followed by multiplication of positive denominators, gives the following strict rational bounds. Thus none rests on the author's script.

| Case | Safe w | Upper bound for lambda(w) | Resulting test |
|---|---:|---:|---|
| DOB, beta=1/9 | 143/1000 | 1713/1000 | `(1/2)lambda+w < 1999/2000 <1` |
| DOB beta=1/5, or LF beta=3/10 | 21/1000 | 1087/1000 | `(9/10)lambda+w < 9993/10000 <1` |
| LF, beta=1/4 | 58/1000 | 1255/1000 | `(3/4)lambda+w < 3997/4000 <1` |
| ST, beta=1/4 | 53/1000 | 123/100 | `u < 557/4000 < 35/248` |
| ST, beta=3/10 | 26/1000 | 1109/1000 | `u < 1501/20000 < 803/10660` |
| ST, beta=7/20 | **41/10000** | 5083/5000 | `u < 2563/200000 < 1007/77320` |

The three star thresholds on the right are exact. Indeed alpha_* is respectively `17/31`, `387/533`, `1827/1933`, and substitution into `(1-alpha_*)(1-6x)/2` gives those fractions.

For the printed w=0.0042 at beta=0.35, `lambda(w)>=1+4w+6w^2`. Hence

`u >= (21/40)(4w+6w^2)+w = 0.013075566 > 1007/77320`.

So 0.0042 lies outside the star allowance. Replace that table entry by the safe radius **0.0041**, or by the implicit root with a strict inequality. The other printed radii are safe at m=0; none licenses the unrelated choice m=1, alpha=1/2. The column heading should read “displayed sufficient radius”, not “largest w”.

## 7. Theorem O-BC(a): HOLDS

H 213–217. All matrices and vectors are nonnegative. Write A=C+Delta C. Its column norm c′<1 implies `1^T(I-A)^(-1)v <= (1-c′)^(-1)1^T v` for v>=0. The resolvent identity gives

`(I-A)^(-1)(b+Delta b) = K+(I-A)^(-1)(Delta C K+Delta b)`.

The latter vector bounds K′ by monotonicity. Since `1^T Delta C K <= gamma 1^T K`, (5.2) follows with exactly the stated constant. The extra row-sum hypothesis ensures applicability of the conditional-law comparison as used here. This is proved, not argued.

## 8. Theorem O-BC(b), star threshold and weights: HOLDS AFTER CORRECTION of “exactly when”

H 219–233. Keep `u<1-6x` as stated. A star has 8 links and 48 distinct exterior Wilson events. For an event opposite corner c, fixing l_c leaves its source `b=x 1_d`, so `sum_j 1^T b_j=48x`. The free graph has row and column sums at most 6x; the W-only events use the unfixed 6-regular star. The prior calculation in BC 178–199 gives `sum_j 1^T K_j/8=alpha_*` from `S=1+x(4S+T)`, `T=1+6xS`, not from numerical enumeration.

N2 gives both row and column perturbation bounds `u=6(lambda-1)x+w_0`, and the total exterior W sources divided by 8 are at most w_0. Sum (5.2) over events to obtain (5.3). Rearranging its right side below 1 gives exactly

`2u < (1-alpha_*)(1-6x)`.

This is **sufficient for the actual block criterion** and equivalent to this *majorant* being below 1. It is not necessary for actual block contraction. For example, take beta=1/4 and `W_p=(1/4)x_p` on each plaquette. The actual density is product Haar, so its block responses vanish. But `w_0=24*(1/4)=6`, far outside (5.4). Thus the “survives exactly when” wording at H 26 and 379 must be “is guaranteed whenever”.

For weights, a walk enters the star through one exterior edge and stays within its diameter-1 midpoint set afterwards. Consequently a Wilson entrance costs at most e^(2m), and a W entrance from X at most e^(m) e^(m diam X). Internal walks need no weight per repeated step: apply the triangle inequality directly from entrance to endpoint. Their unweighted perturbation is bounded by u_m. Weighted exterior W sums are at most e^m w_m, bounded by e^(2m)w_m. This proves the printed weighted majorant, with `lambda(w_0)<=lambda(w_m)` and the corrected positive denominator. Symmetry makes its block average equal the column bound on the hypercubic torus. No additional exponential loss is needed.

## 9. Theorem O-BC(c): HOLDS AFTER CORRECTION of its domain

H 235–239. Require `lambda(w_0)r+w_0<1` and the symmetric fixing/averaging rule used by Lemma SYM. Then the same resolvent calculation with `gamma=(lambda-1)r+w_0` and mean exterior source `(lambda-1)bbar+w_0` proves (5.5). To assert a neighbourhood of W=0 by *this formula*, require both r<1 and alpha<1 at W=0. A criterion verified using only the spectral-radius version of GF need not satisfy the row/column condition r<1. The printed “every block criterion” and “radius tends to 0 only as ... 1-alpha” are too broad: this displayed radius also depends on the resolvent margin 1-r and on bbar. For a fixed finite family with r<1, these constants remain fixed and the ordinary continuity conclusion holds. A weighted-resolvent generalization is not proved here.

## 10. Lemma BOX and its block form: HOLDS

H 133–139. For l outside D_R every coordinate is farther than R+1 from the circular seam. Every interacting k is within R, so its coordinates are farther than 1 from the seam. In representatives modulo n they lie in `{1,3/2,...,n-2}`. In the direction of k its midpoint is a half-integer, hence its endpoints lie between 1 and n-2; in other directions they equal the integer midpoint coordinate. Thus every needed link is wholly inside Q. Conversely every large-torus interaction containing the lifted l stays inside Q and maps to the same small-torus interaction. TC identifies its coefficient/function. Conditioning first on all large-torus links and then on E_Q gives the asserted conditional law by the tower property. For a block avoiding D_R with all its events, the identical argument uses the joint block density. No independence of the exterior is assumed.

## 11. Lemma TRUNC: HOLDS

H 141–145. Midrange zero and a coordinate-by-coordinate change give `||W_X||_infinity <= sum_(k in X)delta_k(W_X) <= |X| dbar(W_X)`. The omitted exponent is bounded in supremum by `|E(T)| w_m e^(-mR)`. If `|a-a′|<=c`, then `e^(-c) integral e^a′ <= integral e^a <= e^c integral e^a′`; taking logarithms proves the claim. Here `|E(T)|` means the **number of links**, not the vacuum constant also denoted E_T. At the two tori the link counts sum with the rho^4 factor to `8(rho n)^4`, giving the exact coefficient in O-SEED. The estimate is deliberately an overcount and remains valid for multiply incident supports.

## 12. Identity PHI: HOLDS

H 147–158. A nonzero translation stabilizing a nonempty link set forces its midpoint projection to contain a coset of a cyclic subgroup of order k>=2. Its circular diameter is `floor(k/2)n/k>=n/3`. Thus every support with diameter <n/3 has exactly n^4 translates. For the finite-range data TC makes the orbit types identical on the two tori. With `h=-beta x_p` or W_X, bounded differentiation gives `F′_T(s)=-|T|e_T(s)`. Haar probability gives F_T(0)=0. Therefore

`rho^4 F_n(1)-F_(rho n)(1)=(rho n)^4 integral_0^1(e_(rho n)-e_n) ds`.

The sign, site factor, and six plaquette types are correct. No transfer matrix or reflection positivity is used in this identity.

## 13. Vacuum cancellation: HOLDS, conditional on TC and the stated tail bound

H 160–163. The same free-orbit count cancels every common term of diameter <n/3 exactly. A term of diameter >=n/3 pays `e^(-mn/3)` in the e_m norm, including equality at the cutoff. The triangle inequality and the two link counts give `8(rho n)^4 e_m e^(-mn/3)`. For the full density, `log integral rho_T=-E_T+F_T(1)`, so the sign of its vacuum contribution is reversed, but the absolute bound is unchanged.

This does **not** say every label-dependent account constant is already an extensive common density. The outline calls RF62 a “quantitative hypothesis on the vacuum term” (SA 22292–22302); it supplies a magnitude bound, not the present cancellation. TC is a separate EXIT input. Moreover EXIT's uniform bound on *all* of e_m is stronger than this argument needs. An arbitrary cutoff-dependent **common** extensive constant cancels exactly and need not have a uniform size; only the uncancelled tail needs the uniform estimate. The current implication remains valid with its stronger assumption. Do not claim that a uniform ebar for the account's full vacuum has been established.

## 14. Norm consequences N1–N4: HOLDS AFTER CORRECTION of N4's scope

H 34–59. N1–N3 hold: the chord diameter is 2, and summing over the second incident link gives exactly the |X| factor in the norm. Both the row and column bounds in N2 follow; no symmetry of the raw c_lk is needed.

N4's first equality is false for arbitrary torus supports. An orbit with stabilizer H_X contributes `Delta(W_X)/|H_X|` per site, not `Delta(W_X)`. For example X can be the full link set, and W_X a nonconstant translation-invariant sum of plaquette traces, centred to midrange zero. Its orbit has size one. Correct N4 to the **diameter <n/3 subfamily**, whose stabilizers are trivial, or include `1/|H_X|` in the general orbit formula. O-SEED uses N4 only after truncation to R<n/3, so its needed estimate `sum_orbits Delta(W_X)<=4w_0` is unchanged.

The “Balaban-type terms” paragraph (H 61) remains **ARGUED**, not proved. CA-I 58187–58290 is a conditional theorem about nonwrapping localized terms on a polydisc, under (1)–(7) and H_j; it does not give the requested global SU(2) norm. Even on a smaller polydisc, Cauchy estimates require a radius loss and the sum over supports requires an entropy margin in kappa-m. Merely writing m<kappa does not establish that sum for every such m.

## 15. INF-W and the extended G, F, GF-W: HOLDS

H 103–113 and 199–209, with beta>=0. N1 and PV give `lambda(w_0)` on the staple term. Changing k changes V_l by at most `c_lk |Delta U_k|` in supremum, hence at most twice that in oscillation; PV's factor 1/2 cancels the 2. Thus (3.1) is correct. There are six plaquettes and three other links per plaquette, each at midpoint distance at most 1, so (3.2) has coefficient `18 beta/4=9 beta/2`. In the line-field gauge the imported LF construction leaves two free partners per plaquette off the seams, giving `12 beta/4=3 beta`.

For a general gauge-invariant Lipschitz W, the forest change of variables remains Haar preserving and leaves the density invariant. Fixed-link restrictions cannot increase a coordinate seminorm. Thus the gauge-fixed conditional law has exactly the PV form. For Lemma G(iv), replace the Wilson proof's word “smooth” by “Lipschitz”: positivity on the finite compact product and the Lipschitz exponent give a Lipschitz normalized kernel. In GF-W the shared gauge rotation and its exterior independence remain valid, so (5.1) follows from the same conditional-discrepancy comparison. These extensions are proved given the named vMF and forest inputs, not an estimate of the account's effective density.

## 16. Theorem O-SEED(a),(b),(c): HOLDS AFTER CORRECTION

H 165–181. Clause (a) holds with the small-size centering detail in §3 above; its constants remain unchanged. Clause (b) holds given the imported LF construction and forest identities (`gap-seed23-opus.md:150–162,301–350`): even n makes the period-2 patterns agree, and their difference is confined to the removed seams. The small-torus free seam variables may have degenerate marginals under the larger gauge; DC* allows arbitrary mu_2 there. Local kernels off D_R still agree. Gauge-invariant means can be translated before fixing the gauge, so the orbit sum remains legitimate. The LF pattern's construction itself is an input, not rechecked here.

Clause (c) holds with the **corrected O_ST domain** of §5, given BC's star comparison. Its weighted proof is supplied in §§3 and 8. The event sets used here belong to the truncated interaction; the bad stars lie in the stated wider seam strip. The original untruncated norms bound all truncated norms.

For all three clauses: TRUNC contributes `8w_m e^(-mR)`, the vacuum term contributes `8e_m e^(-mn/3)`, and PHI contributes the local comparison constant times `24 beta+4w_0`. Along interpolation, `s beta,sW` remain in the corrected zone and `Delta(h)` refers to the derivative of the *unscaled* action, so no extra s or 1/s occurs. These prove the claimed absolute defect bound. The word “PROVED” here means this implication from the explicitly named inputs; it supplies no EXIT datum.

## 17. Corollary SEED-HO: HOLDS given the corrected O-SEED and bare transfer input

H 183–187. Lemma Z′ (`gap-phys-seed.md:268–272`) states precisely `log(1+S(T_0;(rho T_0)^3)) <= (2/rho)Phi_rho(T_0)`. Its input is the bare theory's partition functions, including their common normalization. Exact total masses identify their hypercubic defect with the landed defect. Therefore `(2/rho)(rho n)^4=2rho^3 n^4`, as printed. The finite constants and positive exponential rate make this bound tend to zero; exponentiating gives any prescribed positive seed target at sufficiently large n. The positivity and full-sector meaning of S are imported from the bare transfer construction. They do not follow from an arbitrary effective Gibbs density.

## 18. The spectral warning and untwisted/full-sector consequences: HOLDS AFTER CORRECTION of proof status

H 191–195. The positive bare transfer operator and exact partition identities suffice; the effective theory needs no transfer operator. Lemma Z′ uses only the two untwisted hypercubic partition functions, although its proof invokes bare transfer theory on intermediate rectangular tori. Thus no *RG run* on twisted or rectangular tori is needed. Its S is the full bare thermal sum, so any sector sub-sum is bounded too.

However H supplies neither an RP-violating perturbation arbitrarily small in its norm nor a topological theorem about the spectral seed. “The spectral seed is not open” is **ARGUED**, not proved here. The proved statement is narrower: the hypotheses of O-SEED do not include or prove a positive effective transfer operator, so they license only the defect conclusion; the subsequent spectral conclusion uses the bare transfer input. The older MGX passage already makes this distinction.

## 19. Perturbed contraction, block gap and decay: HOLDS given BC Theorem R

H 241–243. With the corrected star criterion, the nonnegative response matrix satisfies the same column contraction as BC Theorem R, hence its heat-bath contraction, `2(1-alpha^W)` block variance bound, and comparison follow. For exponentially decaying W use the weighted series in §8 rather than the finite-range wording of R(e); exponential covariance decay follows by tilting the measure with a bounded local test, as in R(e). Uniformity in centre signs follows because the response majorants use absolute staple changes. These are consequences for the specified effective measures, not the account's unestimated measure.

### Perturbed Langevin constant: HOLDS given D1, with the following completion

H calls `3e^(-2w_0)(1-6lambda x-w_0)` **ARGUED**. Its bounded-perturbation step has an elementary proof. If dnu=r dmu with 0<a<=r<=b, then

`Var_nu(f) <= b Var_mu(f) <= (b/3)mu(|grad f|^2) <= b/(3a) nu(|grad f|^2)`.

For the one-link tilted law, b/a<=e^(2w_0), so D1's imported vMF gap 3 becomes at least `3e^(-2w_0)`. On the eight-link star, both influence row and column sums are at most `q=6lambda x+w_0<1`. The singleton heat-bath variance inequality gives `sum_c E Var_c(f)>=(1-q)Var(f)`. Combining its eight conditional Poincare inequalities gives exactly the displayed c_*. This fills the short argument, conditional on D1 and the heat-bath comparison, without importing an unread Holley–Stroock theorem.

### Majorant ceiling: HOLDS

H 245 uses `C′=lambda C+c(W)>=C`, so its spectral radius is at least `(2+sqrt(10))beta/4` by BC CEIL (`gap-blockcrit-opus.md:266–268`). Thus this particular family of majorants cannot work above `4/(2+sqrt(10))`; beta>=0.775 is a valid rounded sufficient exclusion. This is not a ceiling on the true perturbed response or on every possible block method. A cancelling W, as in §8, illustrates the distinction.

## 20. First-passage reading and exclusion claim: HOLDS AFTER CORRECTION

H 249–253. The SA-index was used first: chunk-06 62–86 (first passage and torus frame), chunk-16 7–20 (density and exact total mass), chunk-01 36–49 (mass preservation), chunk-20 100–111 (vacuum), and the matching obligations entries. Direct SA source reads were 394–416, 6854–6861, 17257–17286, 22283–22302. The CA-full index locates Theorem 4.38 at CA-I 58187; its hypotheses and localized-term conclusion were read through 58290.

These sources do say: first passage stops at a small reference g; the displayed density sums labelled operations with characteristic functions; its Wilson action is evaluated on the constrained **background** U_K(V); its nonwrapping regular terms have common lifts on their analytic domains; and its total integral is the bare Z. The account's theorem statements are conditional on their named packages. This check neither supplies those packages nor replaces their proofs.

Correct H 253 to: **the supplied representation and estimates do not establish membership in any corrected landing zone.** A sum containing labels or characteristic functions does not prove that the summed density lacks a bounded global log potential: already `chi+chi^c=1` disproves that inference. Likewise x_K multiplies the background action, not an already identified Wilson plaquette action of the final V-links. To use R1 as a numerical exclusion, first identify that coefficient with the beta of (2.1) and make the small-g range explicit. Global norms and resummation remain unproved. The author's later qualification “whether a resummation ... lies in a zone is OPEN” (H 310) is the appropriate scope. No impossibility of landing or resummation has been proved.

## 21. EXIT definition: HOLDS AFTER CORRECTION of the zone reference

H 255–267 is a hypothesis, not a theorem of existence. E0 follows from integration of a normalized probability kernel; it gives total masses, not general observable transport. E1–E4 are meaningful uniform global-form, pairwise torus-consistency, norm, and cutoff requirements once E3 refers to the corrected zones of §5 and `0<alpha<1` is explicit. Odd L and coarse sides `2L^(p-n_*)` give the even integers required by LF, after choosing p sufficiently large. Equality of local functions at *different* cutoffs is not required by E2; each fixed cutoff needs common functions on its two tori and the same bounds uniformly in K. No existence of these kernels or bounds is asserted here.

## 22. Theorem HO: HOLDS AFTER CORRECTION of its imported star domain

H 269–279. With corrected EXIT/O-SEED, for each admitted coarse side the defect estimate is uniform in K. Increasing a coarse side along the account's unbounded geometric family makes `n^4 exp(-cn)` tend to zero for every c>0. A least admissible side satisfying the displayed inequality therefore exists; no monotonicity from n=8 is needed. Replace w_0 by wbar using w_0<=w_m<=wbar, and beta,e_m by their common bounds. Apply §17 to get precisely

`T_0=L^(K+n_*)n_1` bare sites, and `T_0 a_K=n_1 L^(n_*)` first-passage units.

Thus the physical size and seed margin are independent of K. The factors A_tau, k_tau and `2rho^3` are those checked above. This is a proved conditional implication, with the LF/star and bare-transfer inputs named. It does not prove EXIT or a continuum mass gap.

### HO to SEED-FP and GAP: HOLDS AFTER CORRECTION as an ARGUED composition only

H 281 contains a literal error: for rho>=25, `t(rho)=3/10`, so `s_0=t(rho)<3/10` is false. For the cited Lemma FL choose any fixed `s_0<3/10` (for example 1/4) and choose n_1 by the stronger inequality with `log(1+s_0)`. The same exponential limit supplies it uniformly. This repairs the strict-margin mismatch. The subsequent use of FL and its continuum/GAP chain remains **ARGUED in H**, not a new proved continuum theorem in this check. FL 128–134 and the SH threshold statement were read for their interfaces; their entire downstream reconstruction/limit chain was not rechecked.

## 23. Remaining scope and order-one claims: HOLDS AFTER CORRECTION to ARGUED/GUIDE

H 283–330 and its summary table repeat the preceding results. The exact-mass/defect route and lack of an effective RP requirement hold conditionally as above. The split G1–G3 and the proposed controls P1–P7 are a research programme, **ARGUED**, not a proof that such steps exist or are necessary in that particular form. In particular:

- P4's equality of local terms across all cutoffs is stronger than HO needs; uniform bounds and pairwise torus consistency at each cutoff suffice.
- A generic extensive error in exactness can spoil the defect, but a common exactly extensive error cancels. Thus P1's statement that approximate maps necessarily “would ruin” it needs that qualification.
- The source does not justify saying Balaban's weak-coupling method already proves P6, which asks for the new **global** resummation and Lipschitz domain. CA-I 4.38 supplies conditional localized polydisc information, not that claim.
- The band lengths 10–600, masses, and resulting step counts are **GUIDE** only. This check does not verify empirical scaling numbers or their extrapolation to order one. An integer count would require rounding `log(ratio)/log L` upward. The asserted minimum of one post-passage step is not a proved exclusion of a resummation at the present scale.
- The chord-diameter observation in H 330 holds *if* the actual test threshold exceeds 2. It does not prove that the account's admissible parameter choices reach that threshold or that all other tests disappear.

The orders of magnitude of generated terms, claims that no small-parameter method applies, and estimates of which improvement saves an RG step are not theorems established by H. EXIT remains OPEN. The source's “PROVED” summary and final RESULT must inherit the corrections above rather than upgrade these readings.

## Completion record

All of H 1–379 was read. The new checks are appended statement by statement above. No earlier check of H was found or used. The underlying vMF theorem, full LF construction, full BC library, bare transfer construction, continuum limit chain, and external empirical/literature claims were not rechecked. Where used, their exact interfaces are named. No computation, machine enumeration or interval bound discharged any step. No source note, registry, FINISH row, audit record or scientific status was edited.

The bounded index search for `Dobrushin|von Mises|hand.off|block criterion|thermal sum|free.energy defect` found no hit in the outline chunk files or obligations. This is a label/method search, not proof of absence of related mathematics. The actual account passages used here are listed in §20. The five searched repo refs resolve, in the order recorded at the top, to `bb4ec020d5ada57c630dd89acc98a68397ade423`, `f76f6c649cff7dffbab664d8976e680e8f287fe9`, `89faef229ff6e6bde42baad15ed8270c2f4087d8`, `1e70c7211a2cdbc39001e619f1dd89db45e25851`, and `c73ad7b177d94f89ff37b77386936e3d52b48b05`. The supplied account revision is `31a47c543775`; only bounded source ranges were read.

RESULT: HOLDS AFTER CORRECTION as a conditional handoff: DC*, PV, BOX, TRUNC, PHI and vacuum cancellation hold; O-SEED and HO retain their constants after the stated domain/proof repairs; the n=226 landing example FAILS its zone hypotheses and the 0.0042 star radius FAILS (0.0041 is safe); block thresholds are sufficient, the HO-to-FL use needs a strict seed margin, and EXIT, order-one control and the continuum-gap composition remain unproved; no status is granted.
