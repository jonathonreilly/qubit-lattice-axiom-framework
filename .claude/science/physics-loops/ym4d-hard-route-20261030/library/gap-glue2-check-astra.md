## Repo search

Refs searched in `/Users/jonreilly/Projects/Physics`: `origin/main` = `4d88da5504d356762deb6b1a1c2695336af9fb81`; `pr/10114` = `f76f6c649cff7dffbab664d8976e680e8f287fe9`; `pr/10133` = `89faef229ff6e6bde42baad15ed8270c2f4087d8`; `pr/10134` = `1e70c7211a2cdbc39001e619f1dd89db45e25851`; `pr/10141` = `c73ad7b177d94f89ff37b77386936e3d52b48b05`.

The completed exact-target query was `gap-glue2|cut.and.reglue|Schroedinger.bridge|seam.{0,50}indistinguish|Proposition INS([^a-z]|$)`, using `git grep -n -i -E` on all five refs, `*.md`, `*.tex`, head 30: **no hits**. Earlier broad searches for thermal traces, vacuum projectors and `S_ev` hit their caps or unrelated substrings; they are locators only. A scoped follow-up for `vacuum.*projector|seam.*covariance|swap.*trace|thermal sum` found the following useful earlier method, outside this lane.

| Source read | Exact relevant statement | Closeness / reuse |
|---|---|---|
| `origin/main:research/mass-gap/library/gap-crux-fp.md:319–345` | Lemma COV: for two layer observables bounded by one, cyclic distance `d >= 2`, and `sigma=S(D/2;D^3)<=1/2`, `abs(Cov(A,B)) <= 2(1+sigma) r^(d-1)+5 sigma`. Its proof uses inserted transfer kernels and the decomposition into the vacuum projector and its complement. | Same trace-insertion and vacuum-subtraction method. Already available, credited here. It assumes a small thermal sum and treats the ordinary torus; it does not supply the interpolated seam estimate or check row 920. |
| `pr/10114:.claude/science/toe-ruleset-20261021/agents/ym4d-proof/N5B.md:242–268` (also located on `pr/10133`) | With independent uniform signs `X,E,H`, `F=X+E`, `S=X+H/3`, the covariance conditional on X is zero but the total covariance is one. Replacing the seam conditional mean by `epsilon_a X` makes its contribution `epsilon_a`. | Earlier warning that conditional decay does not remove the remaining conditional-mean covariance. C3 correctly retains that term. This is a toy diagnostic for a rotation seam, not this thermal-seam estimate. |
| This lane, `gap-crux-skeleton-max.md:104–120,190–198` | I1 defines the vacuum Doob chain; I2 identifies its chi-square norm with the thermal trace; I3 identifies the replica swap trace; B1 gives `pi(dU,dU')=Omega(U)T(U,U')Omega(U') dU dU'/lambda_0`, with both marginals `nu`. | Existing inputs for C1 and BR, not new here. B1's probability law is reused; no bridge uniqueness theorem is needed for this check. |
| This lane, `gap-glue-max.md:106–122` and its cited check | G1 is spectral decay; G2 bounds the finite-ring defect between `log(1+S_ev(a))` and that number plus `log(1+S_ev(s))`; G3 gives the even-chain chi-square identity. | Existing spectral algebra. R3 uses G2; it must not be presented as a new bound on the seed. |

The earlier `prior/repo-search-2026-11-08.md` concerns the ultraviolet port obligations. Its covariance and seam hits describe retained coarse covariances and rotation defects, not this thermal seam. `open-registry.md` has no match for `glue2|GLUE-FP|SEAM.*psi|local even mixing|seam.*covariance`. No duplicate check or competing owner was found. FINISH rows 920–921 contain no separate “Repo prior work” line. This is the explicitly assigned check of row 920, not a new attack on the seed.

## Provenance and scope

Check by Codex, configured GPT-6 Astra, xhigh; FINISH row 921. Source checkout: `c31b0d198a58cf6ac53363ba82f871c333caa891`. Research text, not an audit; grants no scientific status. The requested prior file `library/prior/gap-glue2-check-astra.md` is absent. Only this output file is being changed.

Target: `library/gap-glue2-opus.md`, row 920, by Claude Opus 5.5. Check S1, S2, INS/R1–R3, SEAM, C1–C3/I1–I3, E, BR, V and the fact-test reductions. Each verdict will be saved as checked. No computation will discharge a step. Numerical GUIDE runs are outside the proof check.

Sussman and Alpoge (with Claude and Codex as authors of their account) and Tadeusz Balaban receive credit where their work enters. Their source status will be distinguished from the finite-volume algebra checked here. No order-one clustering estimate or mass gap is being proved.

## Checkpoint

Complete. Source: row 920 with its own Step 8 corrections and Step 9 withdrawal of proposed sizes. All requested statements have verdicts below. The seed, the uniform I1–I3 estimates and an SU(2) bound on the interpolated seam remain open. No source file, registry or scientific status was changed. This report remains local and uncommitted.

## 1. S1 and S2 — HOLDS

Source lines 120–125. Put `n=3b^3`, `lambda=lambda_0`, and write `N_theta` for the source's `Nt_theta`. Work at finite `b>=2`, `beta>0`; use integer `a>=2` below. The Wilson transfer operator, its positive continuous vacuum and its simple maximal eigenvalue are the stated inputs. The vacuum is gauge invariant and centre even because each symmetry fixes its normalized positive representative.

The precise kernel identity behind S1 is

`K_theta(CU,W;CU',W') = K_theta(U,CW;U',CW')`.

It holds term by term before the temporal-link integrations. The two direct plaquettes get either two signs or none; each crossed plaquette gets the same sign on either side of this equation. Changing both `W,W'` by `C` preserves Haar measure and `psi`. Thus `N_theta(CU,CU')=N_theta(U,U')`, which is exactly commutation with `C`. The source's “integral over the change of variables” is read as this change in the defining integral, not as a new pointwise integral identity.

At zero, the `W,W'` integral is `<psi,K psi>=lambda`, so `N_0=T`. At one it factors into `(K psi)(U)(K psi)(U')/lambda`. Symmetry of `K` and `e^(V/2)K psi=lambda Omega` give `N_1=lambda |Omega><Omega|`. No positivity as a quadratic form is assumed for intermediate `N_theta`; its positive kernel suffices.

## 2. INS and cancellation of the reference — HOLDS

Source lines 127–132. A direct normalized-partition check gives the identity and fixes every factor. Let

`Z_theta=Tr(T^(a-1) P_0 N_theta)`, `Phi_theta=<psi tensor psi,K_theta(psi tensor psi)>`, `rho=(T^(a-1)P_0)(U',U)/(lambda^(a-1)Omega(U')Omega(U))`.

Integrating the two positive weights gives

`Z_theta = lambda^(a-2) Phi_theta E_theta^inf[rho]`.

All objects are finite and positive on the compact configuration space. The twist average is positive term by term. Its denominator is therefore nonzero. Differentiating the actual seam exponent gives `Z'_theta/Z_theta=-beta E_theta^a[sum_l delta_l]`, with the minus sign because `delta=A-B`. S2 gives `Z_0=Z_0(a)` and `Z_1=lambda^a`. Hence the integral of this expectation is `log(1+S_ev(a))/beta`.

For the reference, `Phi_0=lambda^2=Phi_1`: at either endpoint the two copies factor, after swapping the primed labels at one. Also `Phi'_theta/Phi_theta=-beta E_theta^inf[sum_l delta_l]`. Therefore its integral is zero, and subtracting gives INS exactly. This cancellation is integrated in theta; it does not assert pointwise zero. Differentiation under the integral is justified by the finite bound `abs(sum delta_l)<=4n`. No numerical quadrature is needed.

## 3. R1–R3 — HOLDS (with R1's size gloss read as an upper bound)

**R1, source line 135.** Swap `U',W'` and send `theta` to `1-theta`. The full integrand, including temporal links, is preserved, while each `delta_l` changes sign. Thus `Phi_theta=Phi_(1-theta)` and the stated oddness hold for each link. The size assertion has the rigorous meaning `abs(log(Phi_theta/lambda^2))<=4 beta n`, by comparison with the zero endpoint. No nonzero lower bound of order `b^3` is proved or needed.

**R2, source line 136.** The twist average projects onto the invariant sector for all three centre flips. Spatial translations or cubic symmetries move a flip plane to a homologous plane; their discrepancy is a vertex gauge transformation. The transfer factors and integrated seam observable are gauge invariant. The latter follows by transforming the `W` variables along with `U` and changing the temporal links. Hence translations, coordinate permutations and orientation reversal preserve the complete integral and permute the `delta_l`. There are exactly `3b^3` unoriented spatial links. Therefore `log(1+S_ev)=3b^3 beta integral Delta_theta dtheta`.

**R3, source line 137.** At finite `s>=2`, use `A=T^(a-1)P_0`, `B=T^(s-1)P_0` and the doubled seam operator. Its endpoint traces are `Z_0(a)Z_0(s)` and `Tr(T^(a+s)P_0)=Z_0(a+s)`: the swap trace contracts `T^a P_0` with `T^s P_0`, and `P_0^2=P_0`. Differentiation gives the claimed finite-s identity. Write `h(t)=log(1+S_ev(t))`. Then `D_ev(a,s)=h(a)+h(s)-h(a+s)`, so the quoted G2 bounds and limit follow from `0<=h(a+s)<=h(s)` and `h(s)->0`.

For the expectation limit, the trace norm of `T^m P_0/lambda^m-|Omega><Omega|` is `S_ev(m)->0`. This follows by dominated convergence of the nonnegative summable eigenvalue ratios. The seam kernel and its differentiated kernel are uniformly bounded on the compact theta interval, so pairing against these kernels preserves the limit. All limits here keep `a,b,beta` fixed. No volume-uniform vacuum convergence has been shown.

## 4. SEAM sufficiency and the necessary average — HOLDS

Source lines 139–144,294–297. Write `L=log(11/10)` and `psi_*=L/(3 beta (24a)^3)`. INS proves

`0 <= integral_0^1 Delta_theta dtheta = log(1+S_ev)/(3 beta b^3)`.

Consequently `sup_theta abs(Delta_theta)<=psi_*` implies the target at `b=24a`. The **signed** average bound is both necessary and sufficient for the target. An average of `abs(Delta)` is only sufficient. No converse from the target to the supremum bound is proved. The “equivalently” assertions at source lines 217 and 270 therefore **FAIL** as equivalences: replace them by “a sufficient route is SEAM; a sufficient route to SEAM is the quantitative C3 criterion below.” The exact identity, not the supremum condition, is equivalent to GLUE-FP.

There is a hand counterexample to deriving that converse from the group-independent algebra. Fix `a>=2`, `b=24a` in Q8. At beta zero its transfer has rank one and `S_ev=0`. The prior fixed-box estimate in section 12.2 gives `S_ev>=1/2` at a finite larger beta. Continuity of the finite matrix and its simple positive top eigenvalue gives some `beta_*>0` with `S_ev=1/10`. At this point INS gives `integral Delta=psi_*>0`, while E gives `Delta_1=0`. Since Delta is continuous, `sup abs(Delta)>psi_*`; otherwise `Delta<=psi_*` everywhere, strictly below it on an interval near one, contradicting its integral. GLUE holds there and SEAM fails. This refutes the group-independent inference, not an additional SU(2)-specific converse in the order-one window; none is supplied.

The illustrative decimals require safe rounding if used as thresholds. At `(a,beta)=(10,23/10)` the denominator is `95,385,600`; at `(15,5/2)` it is `349,920,000`. A hand bound is

`1/10-1/200+1/3000-1/40000 < log(11/10) < 1/10-1/200+1/3000`.

It follows from integrating the alternating geometric expansion for `1/(1+x)` on `[0,1/10]`, with its signed remainder. Multiplication then gives `9.99e-10 < psi_*(10,2.3) < 1.00e-9`, and `2.72e-10 < psi_*(15,2.5) < 2.73e-10`. Thus `1.0e-9` is an approximation, not a certified sufficient upper threshold. Safe sufficient values are `9.99e-10` and `2.7e-10`, respectively. This corrects the literal rounded-threshold wording at source lines 255 and 274; Step 9's exact formula survives. These are arithmetic examples only; no seed size has been established.

## 5. C1 — HOLDS

Source lines 148–153. In the full seam variables, take `P=E_theta^inf` and `Q=E_theta^a`. Their only differing factor is the ring segment kernel. The partition identity in section 2 gives the exact Radon–Nikodym derivative

`dQ/dP=rho/P[rho]`, with `rho=pbar_(a-1)(U',U)>0`.

Therefore, for every bounded measurable seam function `f`, `Q[f]=P[f rho]/P[rho]`; subtract `P[f]` to obtain C1. The vacuum has a positive minimum at each finite box, so the denominators and these integrals are finite. Use the kernel formula for `pbar`; its spectral series can be read in `L^2(nu tensor nu)`. No unproved pointwise eigenfunction-series interchange is required.

## 6. C2 — HOLDS; its equivalence reading HOLDS AFTER CORRECTION

Source lines 155–158. Let `P_l,Q_l` be the two sigma-l marginals, with

`h_l=dQ_l/dP_l=P[rho | sigma_l]/P[rho]`.

The convention is `d_TV=(1/2) integral abs(h_l-1) dP_l` and `chi2=integral (h_l-1)^2 dP_l`, directed from `Q_l` to `P_l`. Each trace lies in `[-1,1]`, so `delta_l` lies in `[-4,4]`. Subtracting the midpoint of this interval gives `abs(Delta)<=8 d_TV`; Cauchy–Schwarz gives `2d_TV<=sqrt(chi2)`. Both constants in C2 hold.

Correct source line 158 to: **“Local total variation at most psi/8 is sufficient for SEAM.”** A bound on one expectation does not imply total-variation closeness of the full marginal. For example, on three points with observable values `-1,0,1`, the probabilities `(1/4,1/2,1/4)` and `(3/8,1/4,3/8)` have the same mean but total-variation distance `1/4`. This hand example refutes the inference, not a claim about the actual Wilson seam laws. C2 itself makes only the valid forward inference.

## 7. C3 — HOLDS

Source lines 160–162. Fix `d>=1` with `2d<=a-3`; set `n=a-1-2d>=2`. Count `d` ordinary transfer edges from `U'` to `Y`, and `d` from `Y'` to `U`; the seam is the remaining special edge. Put the centre twist in the complementary segment. This is possible because `P_0` commutes with every ordinary transfer factor. The near slab thus has the same positive conditional kernel in both measures, including the entire second copy.

For fixed `Y,Y'`, the far factor is `(T^n P_0)(Y,Y')` under Q, and `lambda^n Omega(Y)Omega(Y')` under P. Hence the endpoint law has density `q/P[q]`, where `q=pbar_n(Y,Y')`. Integrating the common conditional law gives `Q[delta]=Q[F_d]`, `P[delta]=P[F_d]`, and the claimed covariance identity. This also specifies unambiguously the step count in the source.

Let `A=sigma(Y_R,Y'_R)`, `F_R=P[F_d|A]`, and `G=F_d-F_R`. The marginal density is `h_R=P[q|A]/P[q]`. Then

`Q[F_R]-P[F_R]=P[(F_R-P[F_R])(h_R-1)]`.

Cauchy–Schwarz and contraction of conditional expectation bound this by `||F_d-P[F_d]||_2 sqrt(chi2_R)`. The remaining difference is `Q[G]-P[G]`, bounded by `Q[abs G]+P[abs G]`. This is exactly C3. In fact `P[G]=0`, so its final nonnegative term could be dropped; keeping it causes no error.

## 8. Reduction to I1–I3 — HOLDS AFTER CORRECTION

Source lines 164–169,217,270. Here is an exact sufficient formulation. For a chosen `d,R`, require, **uniformly in theta and in the boxes under consideration**,

`||F_d-P[F_d]||_2 <= A_d`,

`Q[abs(F_d-F_R)] <= B_R^a`, `P[abs(F_d-F_R)] <= B_R^inf`,

`chi2(Q_R || P_R) <= C_(a,d,R)`.

Then C3 gives `sup_theta abs(Delta_theta) <= A_d sqrt(C_(a,d,R))+B_R^a+B_R^inf`. This proves SEAM only when this whole right side is at most `psi_*`. In particular, the displayed I2 must cover **both** laws; its unnamed expectation alone is insufficient. None of these uniform estimates is supplied by C3.

I3 compares the ring and vacuum **seam** marginals. Its reference is not generally `nu_R tensor nu_R`: the two endpoint slices remain coupled through the near slab. For example, at theta zero that slab is an ordinary vacuum segment of length `2d+1`. Calling I3 independence, or the same input at a smaller ordinary periodic box, changes the reference measure. A multiscale use needs this family of reference measures as an explicit hypothesis.

The absence of an explicit factor `b^3` in C3 does not prove volume-independent constants in I1–I3. The “about twice the size” reading also needs separate premises. If I1 has rate `m_1` and **chi2** in I3 is bounded by `C exp(-m_3 n)`, the first term has rate `m_1 d + m_3 n/2`. For `d` near `a/4`, this is `(m_1+m_3)a/4` up to fixed shifts, as the source suggests. The two spatial errors must independently meet the same target; their constants and the growth of R remain to be bounded. No universal factor-two loss or induction is established by the algebra.

## 9. E — HOLDS

Source lines 173–176. At theta zero the two copies factor. A crossed plaquette has zero expectation: apply the central vertex gauge transformation `-I` at one endpoint of its primed spatial link in the other copy, changing that copy's adjacent temporal links as well. The probability law is unchanged; the mismatched trace changes sign. The endpoints are distinct when `b>=2`. This is a direct sign proof of the Haar-average argument, with no gauge fixing. The two actual A plaquettes have expectations `u_(a,ev)^t` and `u_inf^t` under Q, and both have expectation `u_inf^t` under P. Thus `Delta_0=u_(a,ev)^t-u_inf^t`.

At theta one, the A plaquettes are mismatched and the same vertex sign argument kills their means. The B gluing joins the finite segment between two vacuum half-lines. Successive integrations use `T Omega=lambda Omega`; a centre twist on that segment disappears against the even vacuum. Each of the two B plaquettes therefore has exactly the vacuum mean under either law. Both expectations of `delta_l` equal `-2u_inf^t`, giving `Delta_1=0`. This is valid for the stated `a>=2`; it does not identify the two entire seam laws at theta one.

## 10. BR — HOLDS

Source lines 178–182. At theta zero, integrating the second copy gives the joint law `pi(dU,dU')=Omega(U)T(U,U')Omega(U')dU dU'/lambda`. This is precisely the existing B1 law. At theta one, integrating `W,W'` gives `nu(dU)nu(dU')`, because `psi(U)(K psi)(U)=lambda Omega(U)^2`.

The normalization identity in section 2, evaluated at the endpoints, now gives `P_0[rho]=1+S_ev(a)` and `P_1[rho]=1`. This checks the endpoint factors without exchanging a spectral sum and an integral. Differentiating the same identity, or using C1, gives

`d/dtheta log P_theta[rho] = -beta sum_l (Q_theta[delta_l]-P_theta[delta_l]) = -3b^3 beta Delta_theta`.

The interpolation thus has the claimed two endpoint marginals. At intermediate theta, BR does not assert that either marginal stays equal to nu, or that the whole path is a family of bridges with fixed marginals. Only its theta-zero law uses B1.

## 11. V — HOLDS; its electric-energy gloss HOLDS AFTER CORRECTION

Source lines 191–194. Keep beta_s fixed. Differentiating the positive twisted partition integral gives `partial_(beta_t) log Z_0(a)=3ab^3 u_(a,ev)^t`. The mixture over twists is weighted by their partition functions after normalization; it is not the uniform mixture of their normalized states.

A separate vacuum calculation avoids interchanging a long-time limit and a derivative. The simple positive eigenvalue has

`partial_(beta_t) log lambda = <Omega,T' Omega>/lambda = 3b^3 u_inf^t`.

The last equality follows by differentiating the temporal-link kernel, retaining the insertion of its actual plaquette sum. Positivity and simplicity persist at each positive anisotropic coupling; the kernel is differentiable in operator norm on every bounded coupling interval. Subtracting `a log lambda` and using E proves V, with its factor `3ab^3` and its sign.

For a differentiable eigenvalue branch `E_i=-log(lambda_i/lambda)`, differentiating `r_i^a=exp(-a E_i)` gives the displayed `-E_i'` weighted sum wherever the branch sum is justified; at crossings the differentiated trace is the unambiguous formulation. Correct the sentence after that sum to: **“The beta_t derivative measures the excess temporal plaquette insertion relative to the vacuum.”** It is not an identity with the Hamiltonian electric-energy operator at finite lattice anisotropy. The separate Hamiltonian virial identity uses a different family, as check 896 already states.

## 12. Fact-test reductions

### 12.1 U(1) endpoint reduction — HOLDS; claimed endpoint failure — FAILS

Source lines 236,258,302,304. E gives the valid implication

`sup_theta abs(Delta_theta) >= abs(u_(a,ev)^t-u_inf^t)`.

To disprove SEAM by this route one must actually show the right side exceeds `L/(3 beta (24a)^3)` at the chosen box and coupling. No such lower bound appears in the cited sources. The frozen-group-independent algebra can be adapted to the chosen involutions of U(1), but that alone computes no U(1) expectation.

The first erroneous inference is source line 236, “about a^(-4) ... so ... fails”. Step 9 line 302 retains the error after withdrawing the numerical size. Even granting the GUIDE law `abs(Delta_0)=C a^(-4)` with a fixed positive coefficient, its ratio to the required threshold is

`3 beta 24^3 C / (L a)`,

which tends to zero. A faster-decaying power does not exceed the slower-decaying threshold at every unknown size. The exponent alone supplies neither a finite-size failure nor failure for all a. This does **not** prove that U(1) satisfies GLUE or SEAM: an interior theta value, or the exact thermal trace, could still refute them. Correct the conclusion to: **“The endpoint is a necessary test; its U(1) value and the U(1) seam failure remain unproved here.”**

The cited `gap-glue-check-astra.md:425–429` already separates the periodic Villain Langevin obstruction from the Wilson transfer trace. That prior result must keep its model and observable; it supplies no missing endpoint value.

### 12.2 Frozen Q8 and 2T — HOLDS at a fixed box

Source line 237. Reuse, without redoing, `gap-crux-exercise2-check-astra.md:227–260`, read at its source, and check 896:405–424. The two flat holonomy classes `(1,1,1)` and `(i,1,1)` survive the centre-even projection. The prior estimate gives `S_ev(a;B)>=1/2` when

`beta >= d_G^(-1) log(16 E (|G|-1) a)`, `E=3b^3`, `d_Q8=1`, `d_2T=1/2`.

The seam identities apply to these finite subgroups with Haar sums. INS therefore yields

`sup_theta Delta_theta >= log(3/2)/(3b^3 beta) > L/(3b^3 beta)`.

This is the claimed failure of SEAM at each specified box for sufficiently large **finite** beta. It does not prove failure at every box for one fixed beta, or at beta 2.3. At the exactly frozen limit, vacuum simplicity is lost, so apply INS before taking that limit; do not use its simple-vacuum proof directly at beta infinity.

The source's further localization of this failure specifically in I2 is **HOLDS AFTER CORRECTION** to: **“The quantitative I1–I3 bounds cannot jointly meet the C3 budget on these boxes.”** Neither INS nor the prior flat-state count singles out I2. The spatial region, the two marginal laws and their limiting estimates would have to be supplied to establish that stronger attribution.

### 12.3 Frozen Z2 — HOLDS as a signed-integral statement

Source line 238. `gap-es1-opus.md:157–168` gives `S_ev(t;B)<=C_B u^(4t)->0` at each fixed box, using the one-dimensional even flat subspace. Thus INS's signed integral, multiplied by `3b^3 beta`, tends to zero. This is consistent with GLUE and forces no failure. It does **not** imply a small supremum of `abs(Delta_theta)`; cancellations could remain. The source does not prove the stronger assertion that frozen Z2 passes SEAM.

### 12.4 Averaged tests and coupling scope — HOLDS AFTER CORRECTION

Source lines 239–240. C1–C3 use the actual laws and do not impose a supremum over boundary configurations. Worst-environment caps therefore cannot simply be substituted for these averaged quantities. Uniformity over theta, boxes and first-passage data is still necessary for the respective proposed conclusions. The numerical transition points are unused; no transition or first-passage theorem is established by this one-coupling algebra.

Route L, source lines 203–207, remains an **unproved proposal**, as correction 8.0(4) acknowledges. In the displayed four-slice measure the factor `psi=e^(V/2)Omega` is a full-slice function with no proved finite-range logarithm. Calling that marginal a finite-range Gibbs measure is not justified. One can keep the vacuum half-lines instead, but must then prove uniform estimates and their passage to the limit. Moreover a covariance estimate involving `grad rho` does not by itself bound the two localization errors and the local chi-square distance in I1–I3. Correct this route to require those additional estimates explicitly. Its use of a Lie-group gradient distinguishes its formal method from finite groups; it is not proof of the required SU(2) bounds or of which I-input fails in Q8/2T.

## 13. Source scope and checks not performed

The SA-index README was read. Searches for transfer kernels, first passage and the mass gap led to neighbouring rows in `chunk-02:95–109`, `chunk-06:55–74`, `chunk-01:67–72`, and `obligations:20–29`. Bounded outline reads were `2313–2352`, `6836–6869` and `588–600` at the supplied revision `31a47c543775`. The exact-target index query `cut.and.reglue|Schroedinger.bridge|centre.even|center.even|thermal.sum|chi.square` found no matches. The broader word “seam” finds layered averaging and gauge seams, which are different objects.

The outline's GL8 is the positive trace-class layer representation `Z_s(0)=Tr L^s`, already proved there and reused through `gap-transfer.md:34–51,108–183`. The latter's Wilson weight differs from row 920's by a positive constant per transfer step; all eigenvalue ratios and normalized expectations are unchanged. Credit belongs to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Their passage at 6854 explicitly says “We fix a small reference coupling g” and defines the first-passage window `g^(-2)<=x<=g^(-2)+B_sharp`. Their passage at 588–600 distinguishes polynomial decay from a positive spectral gap. Neither passage supplies an order-one seam estimate.

Correct the blanket “the account supplies no input” reading to this scoped statement: **“The cited account passages supply no bound on this interpolated seam at order one.”** They do supply the earlier transfer machinery. The bounded reads are not a full absence proof across CA-I–III. No new CA theorem is imported. Balaban's estimates are not used by row 920's algebra; no claim about his original papers is made, and none was fetched or re-proved.

No numerical script was run or used to discharge a statement. The source's GUIDE script is outside the allowed source locations and was not opened. Its twelve-digit agreements and its maximum ratio are not verified here. There is also an internal arithmetic error at source line 232: `4.00e-2/3.37e-2=400/337<6/5`, not 1.58. A maximum of 1.58 could refer to another theta, but the displayed theta-half values do not establish it. Treat the numerical refutation as an unverified GUIDE report, not a hand counterexample. The proof that two convex log-partition functions need not have a convex difference is sound; it establishes no endpoint domination.

Not checked as additional theorems: the withdrawn box-size forecasts, the old gas comparison for G5, the entire Langevin literature or its numerical coupling floors, a uniform first-passage seed, or a mass gap. The useful exact reduction stops before any such claim.

## 14. Verdict table

| Statement | Verdict |
|---|---|
| S1; S2 | HOLDS |
| INS and integrated cancellation of the reference | HOLDS |
| R1 symmetry; R2 link count; R3 finite-s identity and fixed-box limit | HOLDS; R1's size gloss means an upper bound only |
| SEAM sufficiency; necessity of its signed theta-average | HOLDS |
| GLUE/SEAM/I1–I3 described as equivalent | FAILS as an inference; only the forward sufficient routes are shown |
| C1 | HOLDS |
| C2 inequality | HOLDS |
| C2 described as equivalent to local indistinguishability | HOLDS AFTER CORRECTION to a sufficient condition |
| C3 exact localization inequality | HOLDS |
| I1–I3 as sufficient quantitative inputs | HOLDS AFTER CORRECTION: both L1 errors, exact seam reference, uniformity and total budget |
| E | HOLDS |
| BR | HOLDS |
| V identity | HOLDS; electric-energy gloss HOLDS AFTER CORRECTION |
| U(1) endpoint reduction | HOLDS |
| U(1) failure inferred from the photon exponent | FAILS |
| Q8/2T fixed-box failure from the existing flat-state bound | HOLDS |
| Attribution of the finite-group failure specifically to I2 | HOLDS AFTER CORRECTION to a failure of the joint quantitative budget |
| Z2 fixed-box signed-integral limit | HOLDS |
| Averaged-test interpretation and Route L as a supplier | HOLDS AFTER CORRECTION; Route L remains an unproved proposal |

RESULT: Row 921: S1, S2, INS/R1–R3, SEAM sufficiency and its necessary signed average, C1–C3, E, BR and V hold in their stated finite-volume domains; the local-input and physical readings need the corrections above, and the claimed U(1) endpoint failure fails. The fixed-box Q8/2T reduction holds. No order-one seed or mass gap is proved; research check only, no status granted.
