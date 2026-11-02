# P1 gate at 2f2ec0f89
Provenance: Codex (GPT-6 family; high effort requested by queue row 76; exact runtime model variant and effort setting are not exposed to this session); repository commit `2f2ec0f892d144359d956a20da577c7bac915dc1`; Sussman–Alpoge source commit `31a47c543775`; research-text check, not an audit, conferring no status or claim of model independence.

## 1. Contract and source control

This report checks the Gaussian partial-sum assertion
\[
 B_k=\sum_{l=1}^k\beta_l^0,\qquad
 |B_k-kc_0|\le C(L),\qquad c_0={11\over3\pi^2}\log L,
\]
including its stated dependencies in mapped Text 3 and the entire mathematical argument of `library/twisted-order-calculus.md`. It does not assert a Yang–Mills construction, nonlinear flow control, or retained status. A shrinking flux neighborhood at each fixed depth is allowed; the bound on the quadratic coefficient must be independent of depth.

Read first: `GOAL.md:1–78` and `FINISH.md:188–223`; queue row 76 is at `FINISH.md:155`. The advertised `docs/ai_methodology/SCIENCE_WORKFLOW.md` and the `docs/` directory are absent from this pinned checkout. The installed physics-claim-reviewer skill supplies review questions only; the explicit single-file, no-audit, no-delegation instructions govern this task. No branch, audit, ledger, or source-proof changes are made.

The external outline was fetched once, with the requested curl command, to `/tmp/sa_ym4.tex`. Credit throughout: **Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text**, `YM4_sketch_500.tex` at `31a47c543775`. Their labels are not proof premises. Balaban is credited for the block-RG and constrained-Gaussian programme. All mathematical checks below are written arguments; no numerical or symbolic run discharges a step.

Verdicts mean: **ADVANCE** for a checked step, including an explicitly stated conditional implication; **CORRECT-NO-ADVANCE** for an unclosed proof obligation without a counterexample to its intended conclusion; **WRONG** for a false assertion or identity as written. An ADVANCE for an isolated identity does not validate its application.

## 2. Result

**P1: CORRECT-NO-ADVANCE.** The first unclosed step in source order is Lemma 3.2: identification of the actual designated Gaussian coefficient with the composite prefactor. The first explicitly false calculation in the Leaf Scalar proof is the higher-derivative bound in (E), line 21. The logarithmic coefficient and substantial conditional algebra check, but the actual uniform symbol and determinant hypotheses remain open. The outline supplies useful saddle-determinant and Ward-identity reductions, re-derived below; it does not close these obligations.

## 3. Step verdicts: mapped Text 3

The verdicts concern the proofs at this revision, not just the plausibility of their conclusions. Detailed checks follow the table. `Conditional` means exactly the premises named in that row; it does not silently discharge them.

| Step (mapped source lines) | Verdict | Result of trying to break it |
|---|---|---|
| Definition and target, 371–374 | CORRECT-NO-ADVANCE | A precise target, but the identification of the designated Gaussian coefficient with the proposed prefactor remains an input. |
| Lemma 3.1 and composition, 381–396 | ADVANCE | The contour is a coarse gradient; geometric sums give the stated transverse smoothing symbol. |
| Lemma 3.2, 404–414 | CORRECT-NO-ADVANCE | Integration in stages is correct conditionally. The unique nondegenerate critical branch, its measure factors, and identification with the designated `Z^(l)` are not proved here. Its own standing note explicitly leaves the last identification open. This is the first unclosed step in source order. |
| Lemma 3.3, 420–425 | CORRECT-NO-ADVANCE | Stationarity and Ward identities check. A critical point is not a minimum merely because the minimum is unique; the missing constrained-branch argument must be supplied. |
| Lemma 3.4, 427–431 | ADVANCE | Conditional on the stated analytic local invariant expansion and its moment bounds: constant curvature extracts the same quadratic curl tensor. It does not prove those hypotheses for the actual composite determinant. |
| Prop. 3.6, 442–457 | CORRECT-NO-ADVANCE | Finite positive-matrix determinant algebra checks. The massless infinite-lattice inverse and the integrations in an indefinite vector form do not follow; replacing determinants by absolute values does not justify divergent Gaussian integrations. |
| Lemma 3.5, 463–469 | ADVANCE | The scalar star-resolvent calculation checks at positive mass, including the signs and factors. |
| Prop. 3.7, 470–475 | ADVANCE | Conditional on the actual vector spin jet: scalar orbital, vector spin, color and action normalizations give `11/(3 pi^2)`. |
| Lemma 3.8, 481–485 | ADVANCE | Diagonal zeroth symbol makes the trace Poisson terms cancel; the off-diagonal spin terms have the stated denominator. |
| Lemma 3.9(a), 487–489 | CORRECT-NO-ADVANCE | The differential-of-exponential formula explains the displayed one-step jet, but the complete actual contour/transport jets and parity cancellations are not displayed. A finite difference is not a substitute. |
| Lemma 3.9(b), 491 | ADVANCE | Conditional on the actual one-step intertwining and jets, composition modulo coarse gradients and multiplication of magnetic phases are exact. |
| Lemma 3.9(c), 493–499 | CORRECT-NO-ADVANCE | Geometric scale weights are summable. The assertion about middle factors for separated replaced positions is not a complete uniform alias estimate; the higher-derivative extension also contains a false bound (Section 5). |
| Lemma 3.10, 501–503 | ADVANCE with local repair | The printed spin calculation is sketched and refers to runs. Section 7.3 re-derives its needed spin jet from the actual on-shell Ward identity, with finite-range scaling and midpoint parity; the displayed polynomial is a Taylor jet. |
| Prop. 3.11(a,b), 505–514 | CORRECT-NO-ADVANCE | The formal Schur/star-inverse reduction is sound, conditional on the unproved uniform alias and actual symbol-jet bounds. It does not establish those bounds. |
| Prop. 3.11(c), 508–514 | ADVANCE | Conditional on (a,b), the remaining singular-integral calculation gives the stated logarithm and an integrable `O(1/epsilon)` error. |
| Prop. 3.12, 516–517 | ADVANCE | Conditional on the actual fine symbol jet, the lattice-to-continuum error is integrable and flux/volume rescaling cancels exactly. |
| Prop. 3.13, 519–520 | CORRECT-NO-ADVANCE | Logarithms cancel correctly at fixed positive mass. Passing the coefficient to zero mass needs the actual constrained saddle, locality and differentiability, not an unqualified massless inverse. The zero-flux coercivity estimate itself checks given Leaf-Q. |
| Lemma 3.14, 522–523 | ADVANCE | The area second moment checks exactly; Section 4 supplies a hand fourth-moment argument, without using a numerical check or an unproved Burkholder invocation. |
| Prop. 3.15, 525–526 | ADVANCE | Heat-kernel splitting gives the stated scalar asymptotic and the uniform fine-minus-coarse cancellation; see Section 4. |
| Leaf Scalar and its application, 528–531 | CORRECT-NO-ADVANCE | The order-count strategy survives conditionally, but (E), differentiability, and the zero-slope input must be separated. (E) alone does not imply the claimed quadratic estimate. |
| Final P1 assembly, 532–535 | CORRECT-NO-ADVANCE | The arithmetic and final implication check; their load-bearing premises have not all been proved. No counterexample to the P1 partial-sum conclusion is established. |

Line numbers refer to the pinned source, not rendered wrapping. A source inventory and hashes are given at the end.

### 3.1 Gradient removal and telescoping

For a coarse bond `(y,y+L e_mu)`, translation identifies the two block averages in the contour term with `Phi(y)` and `Phi(y+L e_mu)`. Summing around a plaquette cancels every vertex value twice with opposite signs. The path sum contributes `D_L(q_mu)`, and the block average contributes `prod_nu D_L(q_nu)/L`; hence the extra power in direction `mu`. Multiplication of `sin(Lq/2)/sin(q/2)` at successive scales telescopes. On the fine zone, `sin(|q|/(2 ell)) >= |q|/(pi ell)` and the numerator is at most one, proving the stated `S_ell` bound. Coarse gradients remain coarse gradients on subsequent steps because `QD=D_k r`. Thus the transverse composition argument stands.

For a finite, nondegenerate constrained minimum, choose coordinates normal to its gauge orbit and its constraint. Taylor expansion of the action gives a positive quadratic form on the remaining variables. Rescaling those variables by `g` gives the Gaussian prefactor, including the density and constraint Jacobian at the saddle. Integrating those Gaussian variables in stages gives the same determinant by block elimination. This proves the *conditional* composition statement. It does not identify an omitted background-dependent density with a constant. Moving an unknown `g^0` factor into P2 changes the designated split and requires proving P2 for that split; it is not a proof of P1 for the original definition.

The abelian constant-flux first variation vanishes because the oriented divergence of a constant plaquette sine vanishes. Gauge invariance differentiated once more gives `H D=0` at this stationary field. Differentiating covariance of the average gives its stated intertwining. These identities do not supply minimality. For comparison, `V(x)=x^4+x^3` has its unique minimum at `x=-3/4`, while `x=0` is another critical point. A positive constrained Hessian plus the appropriate unique local critical branch would repair the inference, but that branch and the finite-volume/constant-flux convention must be constructed for this map.

For Lemma 3.4, expand each local analytic invariant to second order. On a finite contractible support, linearized gauge invariance annihilates exact bond forms, so the quadratic form factors through plaquette curls. Exponential decay makes the sums of the requisite coordinate moments finite. Constant curvature and the quadratic small-momentum plane-wave term therefore contract the same zero-momentum tensor. Coordinate reflections remove mixed plane components; permutations make the six diagonal plane coefficients equal. A single 12-plane flux reads that coefficient, and `1-cos f=f^2/2+O(f^4)`. This uses locality with moments and full hypercubic symmetry, not merely color invariance.

### 3.2 Gaussian algebra versus its domain

For a finite positive definite `K` and onto `Q`, the density at zero of `QH` under a Gaussian of covariance `K^-1` is proportional to `det(QK^-1 Q*)^-1/2`. Thus
\[
 \log\!\int\delta(QH)e^{-\langle H,KH\rangle/2}dH
 =-\tfrac12\log\det K-\tfrac12\log\det(QK^{-1}Q^*)+\text{constant}.
\]
Integrating a coarse displacement `D_k omega` adds `-1/2 log det(D_k* h D_k)`. Factoring the latter as `X r X` gives the scalar bracket and `r` factors in Prop. 3.6. Fine-orbit volume contributes the other half of the fine scalar determinant; the Feynman-gauge Gaussian along that orbit supplies its compensating half. All these statements require a fixed zero-mode quotient and the relevant positive forms.

The actual vector form at nonzero magnetic flux need not be positive. Even the two-dimensional example `K=diag(-1,1)`, `Q=(1,0)` has a perfectly convergent constrained integral, while the unconstrained Gaussian used in the displayed derivation diverges. Taking `|det K|` does not make that integral converge. Moreover `K=diag(0,1)` with the same constraint has an invertible saddle matrix and a convergent constrained integral, but `K^-1` does not exist. Thus positivity on `ker Q` alone is insufficient for the literal `G=QK^-1Q*` definition. The draft itself acknowledges negative charged modes; it supplies no spectral exclusion of zero for the infinite-lattice inverse. A direct saddle definition is the appropriate repair, proved in Section 7. It repairs this algebraic representation, not the missing uniform estimates or gauge identities.


### 3.3 The conditional composite-symbol estimates

The one-step exponential differential is checked in Section 7.3. For the composite jet, every first flux insertion carries either `s_(j+1)^2` or a pair `s_i s_j` from the magnetic product. Their sums are bounded by geometric series; at degree two there are products of at most two such weights, still summable. This proves the scale-weight part of Lemma 3.9(c). It does not bound the alias-dependent product attached to each weight. The unaliased zeroth symbol is bounded below because each of its five sine ratios is at least `2/pi` on the coarse zone. Its deviation from one and its first derivative are respectively `O(p^2)` and `O(p)` by evenness and bounded second derivatives.

Assume the claimed alias estimates, including the needed differentiated versions. Split the coarse covariance into its unaliased term and `Rbar`. With `Y=tau^{star -1}` on the coarse zone, put `W=Y star Rbar star Y*`. Associativity gives
`G=tau star (K^{star -1}+W) star tau*`, and inverting this identity gives
`h=Y* star K star (1+W star K)^{star -1} star Y`.
This proves the algebra in Prop. 3.11 without dropping the aliased term. At zero flux, all these symbols are diagonal; `W_0>=0`, `Rbar_0=O(p^2)` because every nonzero alias has a vanishing sine numerator, and `Y_0=1+O(p^2)`. Therefore
`h_0=Y_0^2 epsilon_eta/(1+W_0 epsilon_eta)`.
The denominator is at least one, with a uniform upper bound. Subtracting `epsilon` gives errors `O(p^2 epsilon)+O(eta^2 p^4)`, bounded by `C epsilon^2`. Differentiating this quotient once and twice gives respectively `C|p| epsilon+C epsilon^2` and `C epsilon`, using the assumed differentiated bounds. It also gives `h_0>=c epsilon`, needed when dividing by h_0 in the logarithm formula.

At first flux order, the only unsuppressed constant matrix is `Y_0^2 S_eta`; every other non-Poisson term carries epsilon, and the Poisson terms carry a first derivative of `Y_0` and of epsilon, hence `O(p^2)`. Thus `h_1=S_0+O(epsilon)`. At second order no singular inverse of epsilon remains in this factored expression: its inverses are those of tau and `1+WK`, both bounded at zeroth order, and all differentiated factors are bounded. This gives `h_2=O(1)` conditionally. The trace estimate in Section 4 then proves Prop. 3.11(c).

Finally, the zero-flux constrained gap in Prop. 3.13 follows from the same alias estimate: `tau_0(p)H_0=-sum_(n!=0)tau_0(q_n)H_n`, Cauchy–Schwarz with weights `|q_n|^2`, and the lower bound on tau_0 give `|H_0|^2<=C sum_(n!=0)|q_n|^2|H_n|^2`. The higher aliases themselves have `|q_n|>=pi`. Integrating over coarse p bounds the entire norm by the kinetic energy. What is not established by this zero-field inequality alone is the actual infinite-lattice magnetic parameter regularity and the uniform differentiated alias input. All preceding estimates in this subsection are conditional on that input, not replacements for it.

## 4. Independent hand checks of the coefficient and scalar bracket

### 4.1 Scalar and matrix star logarithms

Use positive mass throughout this calculation. Write `A=T_0+s` and `R=(T+s)^{star -1}`. The zeroth coefficient is `A^-1`. At first order the Poisson bracket of `A^-1` and `A` vanishes, so `R_1=-T_1/A^2`. At second order the two first-bracket terms cancel by the ordinary chain rule, and
\[
 R_2={T_1^2\over A^3}-{T_2\over A^2}
       -{P[A,A]\over8A^3}+{\widetilde P[A]\over4A^4}.
\]
Since `log T=-integral_0^infty((T+s)^-1-(1+s)^-1) ds`, integration gives exactly Lemma 3.5. There is no unexplained sign choice left: the outer minus sign changes the last two resolvent terms to `+P/(16T_0^2)-Ptilde/(12T_0^3)`.

For a diagonal matrix `A`, the diagonal entries of the first-bracket cross terms cancel componentwise. The terms with two `h_1` factors have trace `sum_mu,nu |h_1,mu nu|^2/(A_mu^2 A_nu)`. Pairing `(mu,nu)` with `(nu,mu)` uses
\[
 \int_0^\infty\left[{1\over(a+s)^2(b+s)}
             +{1\over(b+s)^2(a+s)}\right]ds={1\over ab},
\]
obtained by differentiating `1/((a+s)(b+s))`. This proves the matrix formula, including equal eigenvalues by continuity.

For `epsilon=p^2+t^2`, direct differentiation gives `P=8`, `Ptilde=8(p_1^2+p_2^2)`. The orbital integrand is
\[
 {1\over2\epsilon^2}-{2p_\perp^2\over3\epsilon^3}.
\]
On a four-dimensional sphere, the mean of `p_perp^2` is `p^2/2`, because the four squared components have equal means. The angular measure divided by `(2 pi)^4` is `1/(8 pi^2)`. The logarithmic part therefore has coefficient `(1/2-1/3)/(8 pi^2)=1/(48 pi^2)` in front of `log(1/t)`. Replacing a ball cutoff by the Brillouin cube changes only a bounded integral away from zero.

The vector spin eigenvalues `2,-2,0,0`, **if verified for the actual lattice Hessian**, contribute `-tr(S_0^2)/(2 epsilon^2)=-4/epsilon^2`. Four orbital terms plus this spin term give
\[
 {4\over48\pi^2}-{4\over8\pi^2}=-{5\over12\pi^2}.
\]
Two real charged colors are one complex vector: their bosonic Gaussian contributes `-log det_c K`; the real ghost trace contributes `2 log det_c X`. Thus the charged logarithmic coefficient is
\[
 {5\over12\pi^2}+{2\over48\pi^2}={11\over24\pi^2}.
\]
Finally `theta=2f` and the action is `f^2/2+O(f^4)` per coarse cell. Multiplication by four and then by two gives `11/(3 pi^2)`. These numerical constants were obtained by written differentiation and radial integration, not by a run.

If the symbol errors in Prop. 3.11(a,b) hold, substitution into this formula leaves `O(1/epsilon)`. Its integral is bounded by a constant times `integral_0^1 r^3/(r^2+t^2) dr <= 1/2`. The same estimate absorbs the fine-lattice error `|p|_eta^2-p^2=O(eta^2 |p|^4)`. Fine-site density is `eta^-4`, while squared fine flux is `theta^2 eta^4`; their cancellation proves the scaling in Prop. 3.12. Subtraction of the two vector logarithms gives `5 log(1/eta)/(12 pi^2)` with a uniformly bounded remainder **provided** those uniform symbol estimates are established.

### 4.2 Area moments, with the fourth moment rebuilt

Expand the heat semigroup in nearest-neighbor walks. A closed walk's magnetic phase is the exponential of its signed projected area, so the return kernel is `J_0(t)^4 E_bridge cos(theta A)`. For `T(q)=sum_mu(2-2 cos q_mu)`, solving the star heat equation to order two gives
\[
 [\theta^2]e_\star^{-tT}
 =e^{-tT}\left(-{t^2\over16}P[T,T]
                  +{t^3\over24}\widetilde P[T]\right).
\]
Indeed the inhomogeneous term at time `u` is `e^{-uT}(-u P+u^2 Ptilde)/8`; integrate in `u` from zero to `t`. Here `P=8 cos q_1 cos q_2` and `Ptilde=8(sin^2 q_1 cos q_2+sin^2 q_2 cos q_1)`. Integration by parts of `sin q exp(-2t(1-cos q))` gives
\[
 \int {dq\over2\pi}\sin^2q\,e^{-2t(1-\cos q)}={J_1(t)\over2t}.
\]
The two terms are consequently `-t^2 J_1^2 J_0^2/2` and `+t^2 J_1^2 J_0^2/3`. Comparing with `-J_0^4 E[A^2]/2` proves the exact second moment.

For the fourth moment, work first with the free planar rate-one walk in each signed coordinate direction and its area `A=(1/2) integral(x dy-y dx)`. Its generator, applied to powers, gives
\[
 {d\over dt}E A^4=3E[A^2(x^2+y^2)]+{E(x^4+y^4)\over8}.
\]
The two possible x jumps change area by `+/- y/2`, and the two y jumps by `+/- x/2`; expanding fourth powers proves this identity. Similarly `E x^2=2t`, `E x^4=12t^2+2t`, with x and y independent. Therefore, for `M(t)=E A^4`, Cauchy–Schwarz gives
`M'(t) <= C(1+t) sqrt(M(t))+C(1+t)^2`.
The comparison function `B(1+t)^4`, with `B` chosen so `4B>C sqrt(B)+C`, is a supersolution starting above `M(0)=0`; a first-crossing argument proves `M(t)<=B(1+t)^4`. This is `O(t^4)` for `t>=1`.

The planar return kernel is between `c/(1+t)` and `C/(1+t)`: in its Fourier integral, use `c q^2 <= 2-2 cos q <= q^2` on `[-pi,pi]`, and integrate over `|q|<=min(1,t^-1/2)` for the lower bound. Every transition kernel is at most the return kernel by Cauchy–Schwarz applied at half time. Consequently the first half of a bridge of duration `t>=1` has density at most a constant relative to the free half-walk. Reverse the second half and start it at the common origin; its area has the same bound. The full loop area is the difference of these two areas, and `|a-b|^4<=8(|a|^4+|b|^4)`. This proves the bridge bound for `t>=1`. For `t<=1`, nonzero closed-loop area requires at least four jumps. If `N` is the Poisson jump count, `|A|<=N^2`, and `sum_{n>=4} n^8 (4t)^n/n! <= C t^4`; conditioning on return divides by a probability at least `e^-4`. This completes the fourth-moment estimate by hand.

### 4.3 The scalar logarithm and its uniform cancellation

The scalar logarithm is the convergent heat integral
\[
 u(\theta)=\int_0^\infty {dt\over t}J_0(t)^4
                    E[1-\cos(\theta A)].
\]
For `t<=|theta|^-1`, expand the cosine and use the preceding fourth moment. The error is bounded by `C theta^4 integral_0^{|theta|^-1} t^3(1+t)^-2 dt <= C theta^2`. For larger `t`, the bound `1-cos<=2` gives another `C theta^2`.

Gaussian rescaling in the defining one-dimensional integrals gives `J_0,J_1=(4 pi t)^-1/2(1+O(t^-1))` for `t>=1`. To check the error, use `2-2cos q=q^2+O(q^4)` and `cos q=1+O(q^2)` near zero; the Gaussian integrals of `t q^4` and `q^2` are relative `O(t^-1)`. Outside a fixed neighborhood the error is exponentially small. For `t<=1`, `J_1=O(t)` by expanding the bounded exponential under the integral. Thus the quadratic term of the heat integral is
\[
 {\theta^2\over6}\int_0^{|\theta|^{-1}}t J_1(t)^2J_0(t)^2dt
 ={\theta^2\over96\pi^2}\log(1/|\theta|)+O(\theta^2).
\]
Write the remainder as `theta^2 e(theta)`, `|e|<=C`. Then
\[
 2[\eta^{-4}u(\eta^2\theta)-u(\theta)]
 ={\theta^2\over24\pi^2}\log(1/\eta)
       +2\theta^2[e(\eta^2\theta)-e(\theta)].
\]
The last bound is independent of `eta` and hence of `k`. No exchange of a singular Taylor series with an infrared integral is needed.

## 5. Leaf Scalar: verdicts and the first false calculation

| Step in `twisted-order-calculus.md` | Verdict | Scope |
|---|---|---|
| LS statement and (E), 9–19 | CORRECT-NO-ADVANCE | These specify the intended physical operators, but their asserted uniform hypotheses are not established. The quadratic conclusion needs an extra zero-slope input. |
| Derivation of (E), line 21, part (i) | WRONG | The claimed `N`th derivative decay `C_N/r^(N+1)` omits derivatives of the numerator. Explicit counterexample below. |
| (E), part (ii) | ADVANCE | Geometric scale sums bound the unaliased products, conditional on the actual one-step jets and their parity. |
| (E), parts (iii,iv) | CORRECT-NO-ADVANCE | Formal inversion and Fourier decay are valid given the requisite uniform derivatives, but the omitted alias estimates cannot be inferred from the false part (i). |
| Magnetic product, A1–A3, 25–37 | ADVANCE | Exact on sufficiently weighted kernels; inverse differentiation additionally needs existence and differentiability of the inverse. |
| Analyticity assertion, 39 | CORRECT-NO-ADVANCE | A gap and spatial exponential decay do not by themselves prove analyticity in magnetic flux in a fixed weighted algebra. Only two real flux derivatives are needed, but must be justified. |
| Lemma 1 and trace bound, 43–47 | ADVANCE | Direct magnetic commutator and heat-walk bounds prove the gap and `tau(X^-1)<=W_4<infinity`. |
| Order closure rules, 51–53 | ADVANCE | Exact multiplication, adjunction and interpolation rules on the stated domains. |
| Lemma 2, 55–57 | ADVANCE | Polynomial conjugation bound holds for each fixed `s` with enough moments. Finite `N_0` must not be interpreted as bounds for every real `s` simultaneously. |
| Lemma 3, 59–65 | ADVANCE | Form bound, commutator induction and interpolation give the stated orders. |
| Lemma 4, 67–73 | ADVANCE | Successive discrete primitives and the magnetic phase correction prove orders up to four, with the finite weighted losses retained. |
| Orders of E and G, 79–89 | ADVANCE | Conditional on (E) and two real derivatives, shrinking `theta_k` absorbs `C_k` without making the constants depth-dependent. |
| Lemma 5, 91–93 | ADVANCE | Each kernel flux derivative costs two orders, including the two-derivation product terms. |
| Lemma 6, 97–103 | ADVANCE | Positivity follows with an explicit cutoff and a margin in the square-root argument; the local repair is given below. |
| Inverse orders, 105 | ADVANCE | Finite geometric identity, not an infinite Neumann series, proves the required weighted inverse bounds. |
| Resolvent derivative and `L''`, 109–125 | ADVANCE | Conditional on the preceding differentiability/positivity inputs, all terms are bounded; the sole order-minus-two term is trace integrable in four dimensions. |
| Removal of linear term, 129 | CORRECT-NO-ADVANCE | It imports the actual determinant identity and analyticity/evenness of its other terms; this is additional to (E). Without that input the conclusion is false. |
| Claimed application to P1, 131 | CORRECT-NO-ADVANCE | Neither (E) for the actual operators nor all the identity/regularity inputs have been discharged. |
| Retired methods and numerical/hostile checks, 133–162 | CORRECT-NO-ADVANCE | Historical checks supply no proof. In particular `tau(X^-1)` is bounded **by** `W_4`, not shown equal to it as hostile-check item 5 says. |

### 5.1 A hand counterexample to the derivative bound in (E)

Set `M=ell'=1/s` and
\[
 E(q)={\sin(q/2)\over M\sin(q/(2M))}.
\]
For an integer `n` not divisible by `M`, differentiation at `q=2 pi n` gives exactly
\[
 E'(2\pi n)={(-1)^n\over2M\sin(\pi n/M)}.
\]
Choose `n=floor(M/4)` along the allowed arbitrarily large powers `M=L^j`. Then `r=n`, `r` is comparable to `M`, and `|E'|>=1/(2M)`. The asserted `C_1/r^2` is at most a constant times `C_1/M^2`. No fixed `C_1` can make that inequality hold for all such `M`. This is an exact elementary refutation, not a numerical one.

The local repair is to use Leibniz's rule on numerator and denominator: terms with derivatives on the numerator retain only `C_N/r` decay, while derivatives on the denominator improve some other terms. The weaker `1/r` bound is still square summable in a single residue interval. This does **not** yet complete the alias proof: repeated residue classes, the lower and intervening products for separated replaced positions, matrix indices, and all needed derivatives must be summed with the scale weights. The source's “middle factors supply the same” is the point requiring an actual estimate. The Fourier implication, once `C^(N_0+5)` is established in a consistent periodic bond convention, is elementary: integrating by parts in a largest coordinate gives Fourier decay `(1+|y|)^(-N_0-5)` and the weighted sum converges in four dimensions. It cannot manufacture the missing uniform derivative norm.

### 5.2 (E) alone allows a linear term

For every magnetic flux, take the bond-matrix perturbation
\[
 E_\theta=\theta D_\theta D_\theta^*.
\]
It is Hermitian and finite range. Its kernel coefficients are analytic finite sums of magnetic phases, so it has an expansion of the form in (E) with uniformly bounded weighted coefficients and remainder derivatives. Here `e_0=0`; at zero flux the symbol of `e_1` is `s_mu conjugate(s_nu)`, vanishing to order two. Thus every moment requirement in (E) holds, the flat error bound is trivial, and `r_0=1` satisfies its flat positivity requirement. But associativity gives exactly
\[
 Y_\theta=X^{-1}D^*(\theta DD^*)DX^{-1}=\theta I,
 \qquad L(\theta)=\log(1+\theta).
\]
Its second derivative is uniformly bounded near zero, while `L(theta)-L(0)` has slope one. Hence **“(E) implies the quadratic Leaf Scalar estimate” is WRONG**. This is not a counterexample to the actual Wilson-derived `E`: the latter has additional physical identities. It shows why those identities cannot be omitted from the theorem's premise list. Defining `h=K+E` realizes the formal difference in (E); it does not purport to realize the actual RG saddle.

The source's Section 7 correctly identifies a possible additional input: if the physical identity
`L=C_k+scalar_bracket-Gamma_c` holds, `C_k` and `Gamma_c` have zero first derivative, and the scalar bracket is `O_k(theta^2)`, then the one-sided slope vanishes. That is a valid conditional implication, but it reads precisely the determinant and regularity steps whose application remains open. Evenness alone would not suffice: `|theta|` is even and has bounded second derivative away from zero.

## 6. Redoing the order-calculus proof, step by step

1. **Product and inverse rules.** In a product of `n` magnetic kernels the phase is `exp(i theta sum_{i<j} w(y_i,y_j))`. Differentiating the coefficients gives the first sum in A1; differentiating each pair phase gives `(i/2) eps^(mu nu) delta_mu` on factor `i` and `delta_nu` on factor `j`. Also `delta(ab)=(delta a)b+a(delta b)` since the output index is the sum of the input indices. At output index zero, `tau(delta a)=0`; integration by parts under this trace gives A2 because `delta_mu delta_nu` is symmetric. Differentiating `aa^-1=1` with these rules gives both formulas A3 with the displayed plus sign in the magnetic term. The kernels of `X=sum(2-T_mu-T_mu*)` and `D_mu=T_mu-1` themselves have no flux dependence. These are exact algebraic identities. Legality for inverses of the actual operators is a separate regularity requirement; citing exponential spatial decay does not prove complex-flux analyticity. For two real derivatives one can instead control the first two phase difference quotients in weighted kernel norms and prove inverse differentiation there. This repair must retain enough kernel moments; it need not assert analyticity.

2. **Gap.** Put `c_mu=T_mu+T_mu*`, `s_mu=(T_mu-T_mu*)/i`, and `d_mu=2-c_mu`. Since `0<=d_mu<=4`, `s_mu^2=d_mu(4-d_mu)<=4d_mu`. Expanding the four commutators using `T_1T_2=e^(i theta)T_2T_1` gives `i[s_1,s_2]=tan(theta/2){c_1,c_2}`. Positivity of `(s_1 +/- i s_2)*(s_1 +/- i s_2)` gives either sign of the commutator as a lower bound for `s_1^2+s_2^2`. On the spectral subspace `X_12<=1/3`, `||d_mu psi||^2<=4<d_mu>` and hence `|<{d_1,d_2}>|<=8/3`. Thus `<{c_1,c_2}> >=8-4/3-8/3=4`. For positive flux this gives `<X_12> >=tan(theta/2)>=theta/2`; for negative flux choose the other sign. The complementary spectral subspace has energy at least `1/3>=|theta|/2`. This proves the stated gap, including the endpoint range. Closed-walk expansion gives `tau(e^-tX_theta)<=tau(e^-tX_0)`, and integration in `t` gives `tau(X_theta^-1)<=W_4`. The finite value follows from `|q-hat|^2>=c|q|^2` and `integral_0^1 r^3/r^2 dr<infinity`.

3. **Order closure and translations.** Inserting `X^(-s-m/2)X^(s+m/2)` between two factors proves addition of orders. Boundedness of `X` proves downward inclusion; taking adjoints gives the stated transformed exponent. The three-lines argument is legitimate for each nonzero flux, since `X` is then boundedly invertible. The gap makes the scalar `theta` an order-two object. Conjugating a translation changes `T_nu` by a phase of size at most `|theta||y|`; hence `XW_y=W_y(X+Delta_y)`. Expanding one commutator at a time gives the induction in Lemma 2, with `|theta| ||X^-1||<=2`. Thus each extra integer conjugation costs at most one power of `1+|y|`. Adjoints and interpolation cover negative and noninteger exponents. A finite weighted norm only licenses the corresponding finite range of exponents. The proof's blanket definition “for each real s” should be restricted to the finite exponents actually consumed, or supplied with all weighted norms.

4. **Differences and words.** The form inequality `D_mu*D_mu<=X` proves order one at `s=0`, also for `D_mu*`. In the commutator induction the `sin(phi)` term contains one more difference and costs `|theta| ||X^-1||`; the `1-cos(phi)` term costs at most `theta^2 ||X^-3/2||<=C|theta|^1/2`. Both are bounded. Adjoints give exponents at most `-1/2`, and interpolation bridges the remaining interval. Direct kernel differentiation yields `delta X=-(T-T*)`, `delta^2 X=-(T+T*)`, and `delta D=T`, as required.

   For a kernel with `m` vanishing moments, successively subtract its restrictions to each coordinate hyperplane in Fourier space and divide the difference by `exp(iq_mu)-1`. This constructs discrete primitives `a_mu` with `m-1` vanishing moments, losing one weight per primitive. Magnetic quantization differs from ordinary multiplication by
   `Op(d_mu a)=D_mu Op(a)-T_mu Op((1-exp(-i theta w(e_mu,.)))a)`.
   Expand the last coefficient as `i theta w a+theta^2 b`, `|b|<=w^2|a|/2`. The first term has order `2+max(m-2,0)`, the second order four. Together with the order-one difference times an order-`m-1` primitive, these prove order `m` for `m<=4`. This is exactly where the maximum moment order four is used. There is no improvement from a commutator beyond counting `theta` as order two.

5. **E, inverses, and Y.** The three leading terms of (E) have orders `4`, `2+2`, and `4+0`. A spatial derivation loses at most one moment; a kernel flux derivative loses two orders. For the remainder, `C_k |theta|^3 ||X^-2||<=4C_k|theta|`; after one flux derivative the required loss is again absorbed by `C_k|theta|`, and after two derivatives the norm is `O(C_k|theta|)`. Choosing a smaller neighborhood for each `k` makes all these constants uniform. This validates the six entries in the E table, conditionally on its weighted remainder bounds.

   `G=X^-1` has order `-2`. Its spatial derivative is `-G(delta X)G`, of order `-3`; differentiating again gives orders `-4`. Its magnetic derivative is a sum `G(delta X)G(delta X)G`, of order `-4`; another spatial or magnetic derivative gives orders `-5` and `-6`. These yield every entry in the G table. In `Y=G D* E D G` the starting total order is `-2+1+4+1-2=2`. A flux derivative either differentiates one factor or inserts spatial derivatives on two distinct factors; each option loses at most two. Thus the six Y orders are `2,1,0,0,-1,-2`. Expanding these finite words is also how the needed finite conjugation exponents and moment budget must be read; no assertion for arbitrarily large `s` is used in the trace estimate.

6. **Positivity with the constants repaired.** Write `c` for the flat lower bound; `c<=1` because `Y_0(q)->0` at zero momentum. Take `P=1_[0,lambda)(X)`, `Q=1-P`. The order-two form bound gives `||PYP||<=C lambda` and `||PYQ||<=C sqrt(lambda)`. Choose a smooth `chi` between zero and one, zero below `lambda/2` and one above `lambda`, and put `g(x)=chi(x)/x`. Then `QG=Qg(X)`. At zero magnetic parameter the symbol in the source is exactly
   `f=1+chi(x(q))^2 Y_0(q)`, so `f>=c` everywhere, including the transition band. The source's unspecified cutoff needs this bound.

   Smooth functional calculus and the weighted product estimate give `QrQ=Q Op_theta(f)Q+o(1)` for fixed `lambda`, uniformly in `k` after the stated remainder shrinkage. To see what is required, first approximate `g` and the smooth symbols by polynomials/Fourier polynomials in the norms controlling their summable kernels. For a finite product, `|exp(i theta w)-1|<=|theta||w|` bounds its error. The approximation errors are uniform by the assumed finite smooth norms. Apply the same argument to the smooth square root of `f-3c/4`; this gives `Op_theta(f)>=3c/4-o(1)`. Choose `lambda` so the P block is at least `3c/4` and the off-diagonal block at most `c/16`, then take the flux small enough that the Q block is at least `5c/8`. The quadratic-form bound is then at least `c/2`. This supplies the margin missing from the source's `c_1/2-o(1)` wording. It remains conditional on (E), not on a numerical spectrum.

7. **Weighted inverse bounds.** Since `R` commutes with `Y`, the exact finite identity is
   `R=sum_{i<2n}(-Y)^i+Y^n R Y^n`.
   For `n>=|s|`, the order of `Y^n` makes both `X^sY^n` and `Y^nX^-s` bounded. Positivity controls the middle `R`. For a resolvent parameter `u>=0`, write `S=(r+u)^-1=(1+u)^-1(1+(1+u)^-1Y)^-1` and repeat; each S contributes a bound `C_s/(1+u)`. This proves the inverse-order assertion without assuming `||Y||<1`.

8. **Second derivative, including every kind of term.** Differentiate the resolvent integral for the logarithm using A3. This gives exactly
   `L'=tau(R dr)-(i/2) eps^(ab) integral tau(S delta_a r S delta_b r S) du`.
   For the first term, A1 contributes `tau(dR dr)+tau(R d^2r)`; its two-factor phase term vanishes by A2. Substitution of A3 yields the three explicit terms displayed in the note. Their orders are respectively `-2,0,2`.

   In the integral there are three S positions and two `delta r` positions. A derivative on an S produces either `-S dr S` (order zero) or `S delta r S delta r S` (order two); including the other two `delta r` factors gives orders two or four. A derivative on one `delta r` gives order minus one, paired with order one on the other, total zero. A phase derivative on two S positions gives total order four; on one S and one `delta r` gives two; on both `delta r` positions gives zero. These exhaust the five single-factor choices and ten factor pairs. There are always at least three resolvents, so `integral_0^infty(1+u)^-3 du<infinity` controls the resolvent parameter. Nonnegative total order means bounded operator norm, and hence bounded finite trace.

   For the remaining term set `B=X^1/2(d^2r)X^1/2`. The order-minus-two assertion makes B bounded. Cyclicity and trace Cauchy–Schwarz give
   `|tau(R d^2r)|=|tau((X^-1/2 R)(X^-1/2 B))| <= ||R|| ||B|| tau(X^-1)`.
   Thus `|L''|<=C` follows under the identified inputs. This four-dimensional integrability step is sound.

9. **The linear term and final implication.** The bound on `L''` makes `L'` Lipschitz on each side of zero. If the value at zero is the continuous limiting trace and the physical identity in Section 5.2 gives `L(theta)-L(0)=O_k(theta^2)`, the one-sided slope is zero. Integrating `|L'(t)|<=C|t|` then proves `|L(theta)-L(0)|<=C theta^2/2`. This establishes the intended *conditional* Leaf Scalar argument; it does not establish its additional physical premises. The explicit counterexample above prevents dropping them.

## 7. Comparison with Sussman–Alpoge and what actually shortens the argument

Source: [the pinned outline](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM4_sketch_500.tex), **Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text**. The borrowed reductions below are credited to that text and re-derived here. Their derivation of the constrained determinant belongs to the Balaban programme; no claim of originality for that elementary identity is made.

### 7.1 CP2 is the same partial-sum target, not a proof

At lines 31941–31953, CP2 requires `b_i=b_i^0+f_i+q_i`, `c_0=11 N^2 log L/(12 pi^2)` and `|sum_(i<=r)(b_i^0-c_0)|<=C_0`. For `N=2`, its Gaussian numerical target agrees exactly with P1. It additionally stipulates independence of the bare coupling and admissible torus. It expressly requires an actual lattice trace and zero-mode convention. **Verdict: CORRECT-NO-ADVANCE as evidence for P1; ADVANCE as the identification of the target.**

B3 at 3986–4004 asks for geometric approach of individual increments to `c_0`, or a suitable substitute, and controlled nonlinear `f_j,q_j`. RF10 at 20348–20363 additionally asks for geometric bounds on differences of successive increments. These assertions are stronger than P1 and are not supplied by it. For a hand discriminator, take `b_j^0=c_0+a(-1)^j`, `a!=0`. Every partial-sum error is bounded by `|a|`, while increments do not converge and their absolute errors are not summable. On the other hand, if the successive differences are summable, the increments have a limit; bounded partial-sum errors force that limit to equal `c_0` by averaging. Thus the distinctions in their statement matter. **Verdict: ADVANCE for these logical distinctions; B3 remains CORRECT-NO-ADVANCE as an unproved input.**

### 7.2 Borrowed and re-derived: a saddle determinant that never divides by K

The outline's lines 21090–21111 use `S(T,M)=[[T,M*],[M,0]]`. This is a real shortening of the representation step in mapped Prop. 3.6 and of the definition of `h` in (E).

Let `M:R^n->R^m` be onto and `T` symmetric, positive on `ker M`. In orthonormal coordinates for `ker M` and its orthogonal complement write
\[
 M=(0,R),\qquad T=\begin{pmatrix}A&B\\B^*&C\end{pmatrix},
 \quad A>0,\quad R\text{ invertible}.
\]
The delta function sets the second coordinate to zero with Jacobian `|det R|^-1`. Consequently
\[
 I(T,M)=(2\pi)^{(n-m)/2}(\det A)^{-1/2}|\det R|^{-1}.
\]
Eliminate the A block from `S(T,M)`. Its remaining block is
`[[C-B* A^-1 B,R*],[R,0]]`, whose determinant is `(-1)^m det(R)^2` by exchanging its two block columns. Hence
\[
 I(T,M)=(2\pi)^{(n-m)/2}|\det S(T,M)|^{-1/2}.
\]
No positivity or invertibility of T on the complementary space was used. This proves the formula including its Jacobian.

It also gives a nonsingular definition of the effective precision:
\[
 h=-[S(T,M)^{-1}]_{\text{multiplier,multiplier}}
   =R^{-*}(C-B^*A^{-1}B)R^{-1}.
\]
When `T^-1` and `MT^-1M*` exist this equals `(MT^-1M*)^-1`, by block elimination. Otherwise the saddle definition still makes sense. This is the repair needed for a constrained vector form whose unconstrained low modes can be negative or zero. In a finite-dimensional analytic family with A positive and M onto, the saddle inverse and its determinant are analytic near the base point simply because their determinant is nonzero.

**Verdict: ADVANCE for this finite-dimensional repair.** It does not prove uniform thermodynamic magnetic derivatives, exponential locality, the gauge-orbit Jacobians, or (E). Those are the remaining application obligations. Use the saddle definition and retain those obligations explicitly; do not retain an unqualified massless `K^-1` as an actual bounded inverse.

### 7.3 Borrowed and re-derived: the Ward identity determines the spin constant

The outline at 21418–21426 proposes reading the spin coefficient from the intertwining with the covariant gradient. This usefully shortens the sketch in mapped Lemma 3.10; it requires no eigenvalue run.

At a stationary constant abelian field, differentiating gauge invariance gives `H_theta D_theta=0`; therefore the Feynman operator obeys `K_theta D_theta=D_theta X_theta`. At zero field its symbol is `epsilon_eta I`, while `X` has scalar symbol `epsilon_eta` and no linear flux coefficient. In the source's magnetic-product sign convention, write `K=epsilon_eta I+theta S_eta+...`, `D_0(p)=ip+O(eta |p|^2)`. Any first flux variation of D cancels between the scalar zeroth-order symbols. The remaining first-order intertwining is
\[
 S_\eta(p)D_0(p)=-i\{\epsilon_\eta,D_0\}(p).
\]
The linear part at zero momentum is therefore
\[
 S_0(ip)=(-2p_2,\,2p_1,\,0,\,0).
\]
Since this holds for every real p, it determines
\[
 S_0=\begin{pmatrix}0&2i&0&0\\-2i&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix},
 \qquad \operatorname{spec}S_0=\{2,-2,0,0\}.
\]
Reversing the convention for the magnetic product reverses the matrix's sign, not its squared trace eight. In midpoint variables, inversion of all four coordinates fixes the 12-flux and changes both bond-vector indices' signs; their product is positive. Thus the first flux coefficient is even in p. Finite range and the fine-spacing scaling then give `S_eta(p)=S_0+O(eta^2 |p|^2)`: each momentum derivative contributes a fine spacing, while the first flux derivative cancels the Hessian's `eta^-2` by the plaquette area `eta^2`. The second flux coefficient has prefactor `eta^2` and a finite smooth trigonometric symbol, so is uniformly bounded. The zeroth symbol follows from expanding each plaquette to the square of its linear curl and adding `DD*`.

**Verdict: ADVANCE for the low-momentum spin jet and the finite-range scaling/parity argument**, conditional on the actual on-shell covariant Hessian and consistent midpoint convention. This fills the load-bearing low-momentum content of Lemma 3.10 more economically than enumerating a numerical Hessian. It does not establish the composite alias estimates. Lemma 3.10's displayed polynomial must be read as a Taylor jet through degree two; finite-range Wilson operators have higher flux terms, which cannot be discarded at finite flux.

The exponential/logarithm part of Lemma 3.9(a) can likewise be checked without its run: differentiating `exp A` gives, in right logarithmic coordinates, `(exp(ad A)-1)/(ad A)` on a variation; differentiating its local logarithm gives the inverse factor. On a charged Cartan background `ad A` is the scalar `xi=2i phi`. Applying the inverse to each loop, averaging, then applying the exponential differential gives the displayed factor `(exp(xibar)-1)/xibar` times the average of `xi/(exp xi-1) X_loop`; differentiating the final coarse link gives `exp(xibar)X_c`. These scalar factors have removable singularities at zero. Bounded one-step loop areas give finite Taylor jets depending only on L. This validates the local differential formula. Matching all their transported kernels to the actual `Q^o` and bounding the composed aliases remain separate tasks.

### 7.4 What their remaining one-loop section does and does not prove

| Outline step and location | Verdict | Effect on our proof |
|---|---|---|
| Gaussian integration in stages, 21073–21088 | ADVANCE conditionally | Same Schur-complement telescoping; requires actual critical backgrounds, Jacobians and coefficient-preserving substitution. It does not settle our identification issue. |
| Saddle representation, 21090–21111 | ADVANCE at finite dimension | Supplies the concrete repair in Section 7.2. |
| Flat coercivity and common momentum strip, 21122–21156 | CORRECT-NO-ADVANCE | The outline of gradient/mean control is not the full estimate for the actual multilevel averages and their differentiated symbols. |
| Independent-current cancellation, 21158–21327 | ADVANCE as a conditional coefficient argument | If the stated covariant local jets exist, no invariant adjoint vector implies `w(1)=0`; gauge covariance kills gradients in `Dw`, so its mixed symbol is `O_k(p)`. Current jets of order `p^2` then give only `O_k(p^3)` or `O_k(p^4)`, with zero quadratic coefficient. Construction of those actual jets and their affine-reproduction property is still required. Our constant-flux route already sets the current to zero, so this does not shorten our chosen route. |
| Massive comparison and stopped expansion, 21330–21381 | CORRECT-NO-ADVANCE | The text explicitly still requires the mixed energy bounds for actual differentiated averages/constraints. A coarse-rank count and `integral(1+q^2)^-3 dq<infinity` do not prove them. |
| Positive mass, then flux derivative, then thermodynamic limit, 20437–20486 and 21383–21395 | ADVANCE as an order-of-limits prescription | Avoids using an indefinite massless Gaussian as a positive integral. Uniform estimates for taking the indicated limits remain necessary. |
| Magnetic numerator grouping, 21396–21448 | CORRECT-NO-ADVANCE | It explicitly still asks to match the actual vector numerators. The Ward spin calculation and our explicit scalar/matrix resolvent calculations supply useful pieces, not its entire uniform comparison. |
| Mass-derivative estimates, 21431–21456 | ADVANCE conditionally | For a fixed bounded numerator, multiplying a resolvent derivative by z introduces `z/(psi+z)<=1`; the claimed remainder bounds follow once that actual decomposition is proved. |
| RF13 to bounded sums, 20494–20503 | ADVANCE conditionally | With `z=eta_k^2`, `11 log(1/z)/(6 pi^2)=k c_0`; the two scaled mass derivatives and the comparison error are bounded. Its premises remain open. |

One caution in their finite calculation directly affects a comparison: at 21388 the outline says the neutral color has no flux dependence. **WRONG for the actual Wilson Hessian** appearing in RF13a. Neutral fluctuations of a 12-plaquette have quadratic weight `cos f`, not one. In unit-lattice variables their Feynman Hessian is `K_0-(f^2/2)d_12* d_12+O(f^4)`. Therefore their contribution to `-1/2 log det K` is
\[
 {f^2\over4}\int {dq\over(2\pi)^4}
 {\widehat q_1^2+\widehat q_2^2\over\widehat q^2+z},
\]
which is positive and tends to `f^2/8` as `z` decreases to zero. The ratio's limiting mean is one half by coordinate permutation symmetry. On the fine lattice the squared flux is `f^2 eta^4`, and the density `eta^-4` cancels it. The coarse determinant response is `O(f^2 eta^4)`: the perturbation satisfies `|delta K|<=C f^2 eta^4 K_0`, so its covariance compression has the same relative bound and finite coarse rank. This verifies the bounded neutral correction in our final P1 assembly. It changes no logarithmic coefficient. Their sentence can be repaired to say “no logarithmically divergent neutral contribution”; their entire coefficient is not refuted by this local defect.

**Does either proof shorten the other?** Yes, locally: their saddle determinant removes our problematic inverse-based representation, and their Ward-identity observation replaces our unsupported spin-eigenvalue check by a short hand derivation. These are adopted above. Conversely, our explicit star-logarithm calculation supplies the orbital constant and matrix trace cancellation that their magnetic-numerator paragraph only describes, and our scalar area argument gives an exact fine-minus-coarse cancellation. Neither direction supplies the missing actual uniform comparison/alias estimates. Neither text presently furnishes a complete P1 proof that can simply replace the other.

### 7.5 Balaban CMP 109: source limit

Queue row 76 also names Balaban's *Renormalization group approach to lattice gauge field theories. I*, CMP **109** (1987), 249–301, [DOI 10.1007/BF01215223](https://doi.org/10.1007/BF01215223). The outline lists it at line 32959. An attempted primary-source fetch through [Project Euclid](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-109/issue-2/Renormalization-group-approach-to-lattice-gauge-field-theories-I-Generation/cmp/1104116842.pdf) returned an anti-bot wrapper; the wrapper's link failed. No bypass was attempted, and no local copy was found by filename search. I did **not** verify its equations (0.14)–(0.16) or (1.4), nor import their validity. The corresponding prefactor-identification issue therefore remains explicit. Bibliographic access is not mathematical verification.

## 8. Ranked defects and final disposition

1. **Actual coefficient identity is open — CORRECT-NO-ADVANCE.** Lemma 3.2, especially its standing note, does not establish that the designated `beta_l^0` is the composite prefactor coefficient with all background-dependent measure factors retained. Its input critical branch is not rebuilt. Lemma 3.3 then uses an invalid general inference from a unique minimum to an arbitrary stationary point. These break the connection of the determinant calculation to the stated target. Repair needed: fix the coefficient/zero-mode/measure convention, prove the local constrained branch and its identification, and establish Gaussian composition for those actual objects. The finite Gaussian argument here is a conditional reduction, not that construction.

2. **Massless inverse and Gaussian domain — CORRECT-NO-ADVANCE for Prop. 3.6; the unqualified integration rule is WRONG.** A form positive only on the constrained kernel need not have an unconstrained convergent Gaussian or an inverse. The explicit two-by-two examples in Section 3.2 prove this. The finite saddle repair in Section 7.2 is in hand. Uniform magnetic locality/differentiability and the gauge-orbit application are not proved by that repair.

3. **The uniform symbol input is not proved — WRONG derivative estimate, CORRECT-NO-ADVANCE for (E).** The exact derivative in Section 5.1 refutes line 21's bound. A weaker derivative bound is available, but the complete alias sum for separated replaced factors and all required derivatives is still missing. This is load-bearing for the uniform coefficient, independently of the elementary one-loop arithmetic. Finite-range one-step jets and the spin calculation do not replace it.

4. **Leaf Scalar's premise list is incomplete — WRONG if asserted from (E) alone; CORRECT-NO-ADVANCE for its physical application.** `E_theta=theta DD*` satisfies the displayed quantitative conditions and gives `L=log(1+theta)`. The extra zero-slope identity and continuity/differentiability at zero must therefore be explicit. The intended second-derivative proof is sound conditionally, as expanded in Section 6; it cannot itself remove a linear or cusp term. Fixed-depth spatial decay also does not, without a parameter argument, establish the asserted analytic flux dependence.

5. **Two local bookkeeping repairs — ADVANCE at the corrected scope.** The positivity proof needs a controlled cutoff and a strict margin; Section 6 supplies them. Finite `N_0` gives a finite range of order norms, not every real conjugation exponent. Neither defect refutes the intended finite-word trace estimate, but its application must retain exactly the needed weighted norms. The draft's claimed identity `tau(X^-1)=W_4` in its hostile check should be the inequality actually proved.

6. **External neutral-color sentence — WRONG literally, harmless to the logarithm after repair.** The actual Wilson neutral Hessian has the bounded flux response computed in Section 7.4. The outline's “no flux dependence” cannot be imported. This defect does not refute its proposed logarithmic coefficient and gives no shortcut around its explicit mixed-energy and numerator-grouping obligations.

**Final P1 verdict: CORRECT-NO-ADVANCE. First failing proof step in source order: Lemma 3.2's unestablished identification/composition for the actual designated Gaussian coefficient.** If that critical-branch and prefactor package is explicitly granted as an additional input, Lemma 3.3's minimality inference and Prop. 3.6's operator-domain justification are the next unresolved applications. **First explicitly false calculation in the Leaf Scalar proof: the `C_N/r^(N+1)` derivative estimate in (E), line 21.** No counterexample to `|B_k-kc_0|<=C(L)` itself has been obtained.

The final arithmetic, assuming the correctly identified determinant and all its uniform estimates, is
\[
 \Gamma_k(f)-\Gamma_k(0)
 ={11\over6\pi^2}f^2\log(1/\eta)+O(f^2),
 \qquad B_k={11\over3\pi^2}k\log L+O(1).
\]
A depth-dependent flux radius suffices: divide by `f^2` and take `f->0` separately at each fixed depth, retaining the common bound on the remainder coefficient. Thus the quantifier choice is not the defect. What is missing is the proof of that common bound for the actual RG objects and their identification with `B_k`.

This report supplies two concrete borrowed reductions (saddle determinant and Ward spin jet), the checked scalar/matrix logarithm arithmetic, a hand scalar-bracket proof, and the conditional order-calculus argument. It supplies no audit status and no closure of B3's nonlinear or geometric-convergence requirements.

## 9. Reading, verification limits, and recovery state

Bounded reads covered: `GOAL.md:1–78`; `FINISH.md:188–223` plus its heading/queue anchors; mapped `parts/hard-core--mapped.md:365–548` (the entire P1 argument and hostile check), with focused rereads of 459–535 and contextual 263–310; `library/twisted-order-calculus.md:1–162`, read in separate ranges. The numerical-record paragraphs were inspected as claims of evidence only; no test or checker was executed. No result relies on their reported outputs.

External bounded reads: outline 3980–4035 (B3), 20304–20535 (Gaussian requirements, RF10–RF14 and conventions), 21055–21580 (the complete one-loop subsection, plus adjacent context), 31920–31990 (CP2/CP3), and isolated search/bibliography anchors. Long search output was used for navigation, not as verification. A combined tool result that truncated a boundary was followed by smaller targeted rereads, including all of Leaf Scalar Section 6 and the final mapped estimates. The rest of the approximately 33,000-line outline was not read. The old raw “book”, its Definition 2.6/(2.7), `FLOW55.md`, Balaban 102b, and Balaban 109 were not verified; filename searches found no local copies of those cited sources. The new outline's explicit coefficient convention was used for the comparison, not silently substituted as a proof of the old definition's equivalence.

Source SHA-256 identities:

| Source | SHA-256 |
|---|---|
| `parts/hard-core--mapped.md` | `30b73d7b0b8de2a1010bab949468868bf333176f923a84b7cb58211b907323d5` |
| `library/twisted-order-calculus.md` | `b6f8d342efe9db3a9663395e47cb750833492423a7b01d35ff2a6bb07d53502a` |
| `/tmp/sa_ym4.tex` | `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` |

Recovery checkpoint: retain the counterexamples and the two finite-dimensional/low-jet repairs. The next decisive work would be the actual prefactor convention/critical-branch construction and the uniform multilevel alias estimates in a declared finite set of weighted kernel norms. The failed routes are an unconstrained massless Gaussian justified by absolute determinants, the false improved derivative decay, and deriving the zero slope from (E) or evenness alone. Neither P1 nor an audit is to be marked complete on this report's basis.

Only `gates/p1-gate-2f2ec0f89.md` was written in the repository. The separately requested source fetch wrote `/tmp/sa_ym4.tex`. No other repository file or editable prompt changed; no commit, push, PR, post, audit, or subagent was used.
