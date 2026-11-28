## Repo search

The target-specific prior digest is absent at `c57644292b2d7374442f5888384ec81102924de1`.
The general digest `prior/repo-search-2026-11-08.md` was read in full. It records searches of main and PRs 10114, 10133, 10134 and 10141, for the November 8 targets. It does not record a target-specific search for MIX, TILT, SHEET, MF, ELL or 4F. No additional “Repo prior work” paths occur in this task's row. Thus its coverage must not be represented as a complete search for row 996.

Its closest method hit is `docs/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md`. I fetched main and read lines 1–35 and 100–150 at `8b11ae2bb95e641494fe75ed83d108ee712fa3a9`. Lines 120–150 apply Brascamp–Lieb after establishing Gaussian tails and a positive Hessian. This is a supplied noncompact Dirichlet Maxwell law, not the compact plaquette law or its random coupling field. It supplies a prior method, not any of the six target propositions. Its covariance-score calculation is acknowledged below.

The registry has no entry matching these named statements or `gap-sepinput`. Its analytic-sheet and annealed-history entries concern different objects. FINISH row 997 is the already completed same-provider check; the present cross-provider check is explicitly requested. No competing owner of this check was found. No other proof lane is opened.

Provenance: OpenAI/Codex, requested gpt-6-astra xhigh; source commit `c57644292b2d7374442f5888384ec81102924de1`; research check, not an audit, no status granted.

## Scope and working checkpoint

Check only `gap-sepinput-max.md` §§5.1–5.3, §5.5 including MF, §6.3 and §6.4.
Do not modify that source or a status file. No numerical or computer-assisted proof step.
The FINISH search exposed the earlier same-provider check's summary; its proofs are not used as evidence here.

1. Record prior work and the indexed Sussman–Alpoge source comparison.
2. Check MIX and all coupling normalizations.
3. Check TILT and its corollaries, including the noncompact analytic hypotheses.
4. Check SHEET's exact finite Haar law and limiting argument, then MF.
5. Check ELL and 4F by Haar disintegration and an analytic curvature test.
6. Record one verdict per statement and one final RESULT line.

Checkpoint: all requested mathematical checks are complete. The source and all status files remain unchanged. The limits of this check are recorded at the end.

## Source comparison

Both requested sources were downloaded once into the new directory `/tmp/sa-gap-sepinput-check-astra.ZYM8sc/`, at Sussman–Alpoge commit `31a47c543775`.
Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.

The outline index README was read, followed by matching chunk rows, neighbouring rows and the relevant obligations. Searches used the names above and `Brascamp`, `elliptope`, `anneal`, `adjoint coupling`, `mean.field`, `heat.flow`, `log.concav`, Haar and quaternion terms. The CA 4.12–4.19 index has no target match. The bounded outline reads were:

| Source lines | What is already there | Relation to this check |
|---|---|---|
| 238–271; index chunk 01, rows 22–33 | Product Haar links, Wilson action and finite-cutoff existence. Definitions and elementary proof. | Fixes `x_p = (1/2) Re tr U_p`; the action differs from the present exponent by a constant. |
| 2773–2795; chunk 03, rows 14–19 | Quaternion trace identity and positive crossing-kernel expansion. | Prior quaternion convention; no trace-density or annealed-coupling theorem in this passage. |
| 27149–27212; chunk 25, rows 15–21; obligations 27151–27198 | Detailed transport proof of marginal log-concavity, GCB3–GCB5. In particular, “its marginal is even” is an additional symmetry conclusion, not needed here. | Reuse GCB5 in the alternative linear-variance check below; do not rebuild this existing result. |
| 28209–28226; chunk 25 obligations | No convexity claim for the resummed interacting conditional density. | It does not identify that density with the finite Haar trace densities here. |

The downloaded CA-I and outline were searched for the more specific target phrases. The CA-I `mean-field` hits concern correlation-theorem means, not a term proportional to the square of total energy. No target proof was located by this bounded reconnaissance. This is not an absence theorem about the complete account. No Balaban result is needed or imported.

## 1. Identity MIX — HOLDS

Source: lines 256–290, especially 275–283. All identities hold for every finite plaquette set, every real `b,v`, and `w>0`.

For eigenvalues `exp(±i theta)`, put `x=cos theta`. The adjoint character is

\[
\chi_1=1+2\cos(2\theta)=4x^2-1.
\]

Thus the exponent `beta_F x + beta_A chi_1/3` equals
`beta_F x + (v/2)x^2 - beta_A/3` exactly when `v=8 beta_A/3`.
The normalized law drops the constant. The partition function retains
`exp(-beta_A |P|/3)`. A Gaussian representation of K7 uses `beta_A>=0`; the zero case is its degenerate limit.

Multiplying the scalar identity `E exp(sx)=exp(wx^2/2)` over plaquettes gives (a).
The joint density gives (c). Completing its square gives

\[
s\mid U\sim N(wx(U),wI),\qquad
\operatorname{Cov}_{\pi}(s)=wI+w^2C(b,v+w).
\]

The residual Gaussian is independent of `U`; the normalized marginal of `s` is `pi`, not the original independent Gaussian measure.
This checks both the annealed normalization and the covariance identity used by TILT.
Since `|x_p|<=1`, differentiation under the finite Haar integral is valid and gives the stated heat equation.
In Remark MIX, “uniformly log-concave” means **uniformly strongly** log-concave: a strictly positive Hessian lower bound. With that meaning its threshold is exact.

## 2. Proposition TILT — HOLDS

Source: lines 292–305. The noncompact domain causes no missing hypothesis in this application.
Write `N=|P|` and `S=Sigma^2(v)`. For a fixed torus, `F` is real analytic on real coupling space. Its derivatives are cumulants of bounded variables. In particular,

\[
|F(b+s,v)-F(b,v)|\le\|s\|_1\le\sqrt N\,|s|,
\quad |\nabla F|\le\sqrt N,
\quad 0\preceq\nabla^2F=C\preceq NI.
\]

Consequently the hidden density is smooth, strictly positive and integrable on all of `R^N`. It has Gaussian tails, with every polynomial moment finite. Its gradient grows at most linearly. Under `wS<1`,

\[
\kappa I\preceq\nabla^2H(s)\preceq w^{-1}I,
\qquad \kappa=w^{-1}-S>0.
\]

The Brascamp–Lieb inequality used here is: for a normalized density `exp(-H)` on `R^N`, with smooth uniformly convex `H`,

\[
\operatorname{Var}(g)\le
\int\nabla g^{\mathsf T}(\nabla^2H)^{-1}\nabla g\,d\pi,
\]

for locally Lipschitz `g` in `L^2(pi)` with finite right side. These sufficient hypotheses cover `g(s)=a·s`. There is no physical hard cutoff, no boundary condition to impose, and no compact-support requirement on this linear `g`. Smoothness of `F` alone would not suffice; the displayed uniform Hessian bound and tails are essential. Credit H. J. Brascamp and E. H. Lieb for this inequality. The original article's theorem number was not independently checked.

Here is a separate analytic check of exactly the linear-variance bound needed, avoiding reliance on that theorem number. Fix a unit vector `e` and write `s=te+z`, `z` perpendicular to `e`. Define

\[
q(t)=\int_{e^\perp}\exp[-H(te+z)+\kappa t^2/2]\,dz.
\]

The exponent's negative has nonnegative Hessian, since
`Hess H - kappa ee^T` is nonnegative. GCB5 of the credited Sussman–Alpoge outline therefore makes `q` log-concave. Its slice hypotheses hold: all slices are positive and smooth, and their derivatives on compact `t` intervals have Gaussian dominating functions. Thus the marginal density of `t` has potential
`V(t)=kappa t^2/2-log q(t)` with `V''>=kappa`.

Differentiating the marginal also gives
`V'(t)=t/w-E[e·grad F | t]`, whose last term is bounded by `sqrt N`.
The Gaussian tails justify both integrations by parts:

\[
\mathbb E V'(T)=0,\qquad \mathbb E[T V'(T)]=1.
\]

For independent copies `T,T'`, monotonicity of `V'-kappa t` gives

\[
2=\mathbb E[(T-T')(V'(T)-V'(T'))]
\ge\kappa\mathbb E(T-T')^2
=2\kappa\operatorname{Var}(T).
\]

This checks `Cov_pi(s)<=kappa^{-1}I` by a one-dimensional marginal argument, using the already available GCB5. It also uses the score integration-by-parts method found in the main-branch note above, with monotonicity providing an upper bound here.

Subtracting the **positive** term `wI` in MIX now gives

\[
C(b,v+w)\preceq
\frac{\kappa^{-1}-w}{w^2}I
=\frac{S}{1-wS}I.
\]

Taking the supremum over `b` and then reciprocals proves TILT exactly. No supremum need be attained.

## 3. Corollaries and Remark POL

**LIP — HOLDS** (lines 309–310). For `w<R(v)` use TILT. For `w>=R(v)`, positivity of `R(v+w)` gives the same inequality immediately. This proves monotonicity of `R(v)+v` for every pair of real arguments; it assumes no differentiability of the supremum.

**K7-A — HOLDS, with its conditional thermodynamic meaning** (lines 311–315). Use the Rayleigh quotient in direction `1/sqrt N`. Under the explicitly hypothetical bound `Sigma^2_Lambda(0)<=S`, and retaining the stated range `0<=v<1/S`, the normalized pressures obey

\[
0\le p_\Lambda''(\beta)\le M_v:=S/(1-vS),\qquad
|p_\Lambda'(\beta)|\le1.
\]

Every locally convergent pressure subsequence has a `C^{1,1}` limit with Lipschitz derivative at most `M_v`. Indeed the derivatives have uniformly convergent subsubsequences on compact intervals; integrating identifies their limit with the derivative of the pressure limit. Every such derivative has the same Lipschitz bound. Thus the conclusion holds for an existing thermodynamic limit and for every subsequential limit. It proves no slope jump and no unbounded finite-volume specific heat. It does not assert continuity of the second derivative, nor exclude every possible kind of transition. The finite-volume pressure is already analytic at every finite coupling.

**K7-B — HOLDS** (lines 316–319). If `vS>=1`, then `S>=1/v>lambda/(1+v lambda)`. Otherwise TILT rearranges to the claimed bound. If `Var(E)/N` diverges, then `lambda_max(C)>=Var(E)/N` diverges, and

\[
\frac{\lambda}{1+v\lambda}
=\frac1v-\frac{1}{v(1+v\lambda)}.
\]

This proves the stated `1/v-o(1)` conclusion at fixed `v>0`; it imports no empirical assertion about K7 coexistence.

**Remark POL — HOLDS AFTER CORRECTION** (lines 326–336). Differentiating the heat equation twice gives exactly the printed matrix PDE. Its stochastic identity needs the process specified: starting at `b_0=b`, use generator
`(1/2)Delta + grad F(.,w-t)·grad` at time `t`, for `0<=t<=w`.
Its drift is bounded and globally Lipschitz on each fixed torus. Ito's formula applied to `C(b_t,w-t)` has drift `-C^2`; expectation gives precisely the printed integral identity. Bounded cumulants justify the expectations. This identifies the intended diffusion. An ordinary derivative of `Sigma^2`, however, is not automatically defined. Read the Riccati statement as an upper Dini-derivative/comparison statement: TILT directly gives `limsup_(h down to 0) [Sigma^2(v+h)-Sigma^2(v)]/h <= Sigma^4(v)`. The original text correctly labels its unexpanded maximum-principle route ARGUED.

## 4. Lemma SHEET — HOLDS AFTER CORRECTION

Source: lines 358–390. The **SU(2) tube calculation holds**. Specify an embedded open tube with four distinct horizontal bonds and four distinct vertical bonds per layer. Ordinary cubical tori with transverse periods at least two, with the usual independent positive bonds, have this property. The stated `m<=n-2` prevents longitudinal wraparound. A side length of one in direction 1 or 2 is not covered by this proof: some listed vertices and bonds coincide, so the claimed four independent horizontal Haar variables are absent. If both transverse periods are one, the cap plaquette is a commutator.

Here is an explicit check of the non-Abelian ordering. Label the base corners `0,1,2,3` around the square. Orient
`h_1:0->1`, `h_2:1->2`, `h_3:3->2`, `h_4:0->3`.
Let `V_a` be the upward vertical link at corner `a`. For a horizontal edge `h:a->b`, put

\[
k=h(i)V_bh(i+1)^{-1}V_a^{-1},\qquad
h(i+1)=V_a^{-1}k^{-1}h(i)V_b.
\]

For fixed lower layer and vertical links this is an inversion followed by translations. It preserves normalized Haar measure. At each layer its four upper horizontal links are distinct; successive elimination is triangular. Thus the new coordinates are exactly
`h(0)`, all `V_a(i)`, and the `4m` side variables `k`.
There are `4+4m+4m=4(m+1)+4m` variables on both sides. The inverse formula proves surjectivity as well as injectivity; no flatness constraint or Jacobian has been omitted. Every unused lattice link integrates to one.

In these coordinates the side weight factors, leaving independent Haar `h(0),V` and independent `k` with density proportional to `exp(B Re k)`. Multiplying the four inverse formulas gives

\[
U_{p_{i+1}}=V_0^{-1}
k_1^{-1}h_1k_2^{-1}h_2h_3^{-1}k_3h_4^{-1}k_4
V_0.
\]

This is exactly the ordering printed at lines 373–374. With every `k=1`, it is conjugate to `U_{p_i}`.

For completeness, concentration here is analytic. Outside any neighbourhood of the identity, `Re k<=1-delta` for some `delta>0`. A smaller neighbourhood `A` has positive Haar mass and `Re k>=1-delta/2`. Its tilted complement probability is at most `Haar(A)^{-1} exp(-B delta/2)`. Each `k` therefore tends to the identity. There are only finitely many of them at fixed `m`. Uniform continuity of the displayed group products then gives `x_{p_i}-x_{p_0}->0` in probability, and boundedness upgrades this to `L^2`.

The product `U_{p_0}` is Haar for every `B`. SU(2) Haar is uniform on `S^3`; its four coordinate squares have equal integrals and sum to one. Hence its real part has mean zero and variance `1/4`, without numerical integration. Therefore every covariance tends to `1/4`. The Rayleigh quotient of the cap indicator gives `(m+1)/4`; choosing `m=n-2` gives `Sigma^2_Lambda(0)>=(n-1)/4`.

The two-dimensional extension in the remark also works if its selected sides follow a spanning path. On a nonwrapping rectangular array of parallel caps in directions 3 and 4, take a path that traverses successive rows in alternating directions. Freeze only the four side faces between each consecutive pair of caps. Each step introduces a new cap's four horizontal variables and distinct connecting links, so the same triangular proof applies. For `(n_3-1)(n_4-1)` caps it gives that number divided by four. Freezing every adjacency, including cycles, is unnecessary and is not justified by the triangular argument.

Continuity of `C` in finite `b` also justifies the next paragraph: if `n-1>4/w`, a sufficiently large **finite** `B` already gives an eigenvalue above `1/w`. This persists on an open set of coupling fields. That set has positive Gaussian and hidden-law probability. Thus global strong convexity really fails on large enough tori. The result rules out a volume-independent bound for this supremum; it does not refute finite-volume bounds or bounds on a restricted or typical set of couplings.

**The general-group assertion FAILS as written** (lines 379–380 and its use at 389–390 and in the RESULT). The failing assertion is that this proof, including its covariance limit, needs only a class function with positive variance. Two repairs are needed; the examples below do not purport to compute the full coupling supremum for another group.

First, replace `1/4` by `sigma_f^2=Var_Haar(f)`. Even for `U(1)` with `f=Re g`, the cap variance is `1/2`, so the asserted covariance limit `1/4` is not group-independent.

Second, positive variance and conjugation invariance alone do not force `k->1`. An explicit counterexample is the cyclic group of order three, with `f(1)=0` and `f(a)=f(a^2)=1`. This is a real class function with Haar variance `2/9`. As `B->infinity`, each side `k` is uniform on `{a,a^2}`, not at the identity. For one cube, the abelian cap ratio is a product of four independent such variables (inversions do not change their laws). Of the sixteen sign choices for its exponent, only the six choices with two plus signs sum to zero modulo three; hence the ratio equals `1` with probability `3/8`. The cap covariance is consequently

\[
\frac{1}{3}\frac{3}{8}-\frac{1}{9}=\frac{1}{72},
\]

not `2/9`. This disproves the sentence that positive variance is the only input.
A sufficient corrected extension is a continuous real class function on a compact group, with positive Haar variance and a unique maximum at the identity. The same argument then works with `sigma_f^2`. The actual SU(2) function meets these hypotheses.

## 5. Proposition MF — HOLDS AFTER CORRECTION

Source: lines 392–402. Its quantitative inequality is correct. Put `N=|P|` and write `F_0(beta)=F(beta 1,0)`. Integrating `s~N(0,w/N)` adds exactly `wE^2/(2N)` to the exponent. Conditional on the links,

\[
s\mid U\sim N(wE/N,w/N),\qquad
\operatorname{Var}(s)=w/N+(w/N)^2\operatorname{Var}_{\rm MF}(E).
\]

The one-dimensional hidden potential satisfies
`H''=N/w-F_0''(beta+s)>=N(1/w-X_Lambda)>0`.
Its Gaussian tails and linear derivative growth justify the same two-copy integration-by-parts argument from section 2, now with no marginalization. Thus

\[
\frac{\operatorname{Var}_{\rm MF}(E)}{N}
\le\frac{X_\Lambda}{1-wX_\Lambda}.
\]

The converse inference from a divergent normalized variance is also correct. Writing it as `Y_Lambda=Var_MF(E)/N`, the two cases `wX_Lambda>=1` and `<1` give
`X_Lambda>=Y_Lambda/(1+wY_Lambda)`.
If `Y_Lambda->infinity` at fixed `w>0`, this is `1/w-o(1)`.

Two wording corrections matter. A “double peak” must mean macroscopic coexistence: for example, two energy-density intervals separated by a fixed positive distance, each of probability bounded below. That implies `Var(E)` of order `N^2` by the independent-copy variance formula. Mere bimodality at one finite volume does not imply the needed divergence.

At lines 398–400, replace “is the same statement as” by “implies, quantitatively”. The proof establishes
`sup_Lambda X_Lambda<=M` implies a uniform MF susceptibility bound for every `0<w<1/M`.
The phrase “stable under a small mean-field energy coupling” is undefined; absence of a first-order transition alone is weaker than the variance bound used here. No converse to that weaker formulation is proved. This correction also applies to the equivalence wording at lines 517–518. Claims about transitions of `Z_2`, `Q_8` or `2T` are marked RECALLED in the source and are not inputs to this calculation or verified here.

## 6. Proposition ELL — HOLDS

Source: lines 419–430. Haar measure on `S^3` gives real-coordinate density
`rho_1(x)=(2/pi)sqrt(1-x^2)`. Conditional on the real coordinate, the imaginary direction is uniform on `S^2`; the two quaternions are independent. The scalar product of two independent uniform `S^2` directions is uniform on `[-1,1]`, by the spherical area element `2 pi d(cos theta)`.

Set `s_i=sqrt(1-x_i^2)`. The conditional density of `x_3` is therefore `1/(2s_1s_2)` on the interval in the source. Multiplication by the two real-coordinate densities leaves exactly `2/pi^2`.
The support inequality is

\[
(x_3-x_1x_2)^2\le(1-x_1^2)(1-x_2^2),
\]

which expands to the printed determinant inequality. Together with `|x_i|<=1`, these are precisely the principal-minor conditions for the corresponding `3` by `3` correlation matrix. Its positive-semidefinite cone section is convex. Boundary points have zero volume and do not affect the density identity. The constant positive density on its interior is log-concave, with zero Hessian of its negative logarithm there; it has no strictly positive uniform convexity constant.

## 7. Proposition 4F — HOLDS AFTER CORRECTION

Source: lines 430–445. The law, constant, interval and derivative formula all hold. The last sign check must be an inequality, not rounded trigonometric values.

Let `h=g_1g_2` and `y=Re h`. Given `h`, the law of `(x_3,x_4)` depends only on its conjugacy class, hence only on `y`. This is the ELL conditional law. Since `h` is Haar, disintegration gives

\[
\rho_4(x)=\int
\frac{\rho_3(x_1,x_2,y)\rho_3(y,x_3,x_4)}{\rho_1(y)}\,dy
=\frac{2}{\pi^3}\int_{\text{both supports}}
\frac{dy}{\sqrt{1-y^2}}.
\]

The endpoints `y=±1` are null sets and the integrable singularities cause no extra mass.
For a pair of angles `theta_a,theta_b` in `[0,pi]`, changing to `delta=arccos y` turns its support into

\[
|\theta_a-\theta_b|\le\delta\le
\min(\theta_a+\theta_b,2\pi-\theta_a-\theta_b).
\]

Intersect the pairs `(1,2)` and `(3,4)`. Reversal of integration orientation under `y=cos delta` removes the minus sign and yields precisely `(2/pi^3)|J|`.

Fix `theta_2=theta_3=theta_4=2/5`. For `2/5<theta_1<6/5`, the lower endpoint is `theta_1-2/5` and the upper endpoint is `4/5`. Thus
`ell=6/5-theta_1=6/5-arccos x_1` throughout this open interval. Its derivatives and logarithmic curvature are exactly

\[
\ell'=\frac1{\sin\theta_1},\quad
\ell''=\frac{\cos\theta_1}{\sin^3\theta_1},\quad
(\log\ell)''=
\frac{\ell\cos\theta_1-\sin\theta_1}
{\ell^2\sin^3\theta_1}.
\]

At `theta_1=1/2`, `ell=7/10`. The elementary bounds `sin t<=t` and `cos t>=1-t^2/2` for `t>=0` give

\[
\ell\cos(1/2)-\sin(1/2)
\ge\frac7{10}\frac78-\frac12
=\frac9{80}>0.
\]

The denominator is positive. All active endpoints remain the same on a neighbourhood of this interior point. The displayed positive curvature therefore violates concavity of `log rho_4` along an affine `x_1` line. This is a written counterexample without numerical evaluation. Replace lines 441–443's decimal sign justification by this inequality; the decimal curvature value and the character-series run are unnecessary.

**Scope:** ELL and 4F concern the explicitly stated product-constrained Haar group variables. A four-face product relation is not automatically a marginal relation among elementary faces of a hypercubic lattice. Consequently 4F alone, as presented in the source, is not a proof of the source's later full-torus claim at lines 460–464. The six-face numerical experiment at lines 449–458 remains GUIDE and was not used. SHEET does analytically refute a volume-independent strictly positive DOS convexity constant. This check makes no additional claim about full-torus plain log-concavity.

## Verdicts and limits

Checked line by line by Codex, from the pinned source and the primary passages identified above. The table separates the propositions from their broader readings.

| Statement | Verdict | Exact qualification or first failing step |
|---|---|---|
| MIX (a)–(c), heat equation and `v=8 beta_A/3` | HOLDS | The independent Gaussian is the annealing prior; the posterior coupling law is `pi`. |
| TILT | HOLDS | Gaussian tails, smoothness and uniform positive Hessian meet the noncompact hypotheses. Section 2 separately verifies its required linear-variance estimate using GCB5. |
| LIP | HOLDS | Includes all real `v`, without differentiating the supremum. |
| K7-A | HOLDS | Conditional on the uniform bound, at `0<=v<1/S`; applies to every pressure limit. No assertion of full analyticity or exclusion of every transition. |
| K7-B | HOLDS | Requires the stated diverging variance per plaquette at fixed positive `v`. |
| POL | HOLDS AFTER CORRECTION | Specify the time-dependent diffusion at lines 333–335 and use a Dini derivative/comparison, not an assumed ordinary derivative of the supremum. |
| SU(2) SHEET | HOLDS AFTER CORRECTION | Make the embedded, nondegenerate tube hypothesis explicit at lines 360–361. Its Haar change of variables, matrix ordering and `1/4` limit hold. |
| SHEET's unrestricted group extension | FAILS | Line 379's “positive variance and nothing else” fails for the explicit cyclic-group example. Use the identity-maximizer hypothesis and the actual Haar variance instead. |
| MF | HOLDS AFTER CORRECTION | The bound holds. At lines 398–400 specify divergent variance/macroscopic coexistence and replace the undefined equivalence by the proved implication. |
| ELL | HOLDS | Density `2/pi^2` on exactly the stated convex elliptope. |
| 4F | HOLDS AFTER CORRECTION | Density and `J` hold. Replace lines 441–443's rounded sign test by the exact lower bound `9/80`. |

The source's SU(2) obstruction to a volume-uniform covariance supremum survives. None of these checks supplies the seed or resolves the order-one mass-gap obstruction. No source proof was edited. No registry, FINISH row, audit record or scientific standing was changed.

No numerical experiment, quadrature, machine enumeration, formal verification or test runner was used. The source's one-plaquette numbers, cube experiment, recalled phase-transition claims and character-series control were not verified. Brascamp–Lieb is credited, but its historical theorem numbering was not checked; the applied linear bound has the separate analytic argument above. GCB5 remains the explicitly identified published input. No outward post or push was made by this check.

Source receipts (SHA-256, bookkeeping only):

- `gap-sepinput-max.md`: `424b1b4914b5747adff281aca6ea2c595946a189ac43572e8cb3de930d6cb1f6`.
- Downloaded outline: `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f`.
- Downloaded CA-I: `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93`.

RESULT: MIX, TILT, LIP, K7-A, K7-B and ELL HOLD; POL, SU(2) SHEET, MF and 4F HOLD AFTER CORRECTION as specified; SHEET's extension from positive variance alone FAILS. The SU(2) tube obstruction survives, and no seed or mass-gap input is supplied. Research check only; no status granted.
