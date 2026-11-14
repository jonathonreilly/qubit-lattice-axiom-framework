## Repo search

Check provenance: OpenAI / gpt-6-astra / xhigh; row 942; 2026-11-14; checkout `f529763f248c83b2bb3a7470790efa98628fd7d1`. Research text, not an audit; grants no status.

Terms: `E-to-HC|HC-vac|LSI-vac|SG-step|Hopf.Lax|Bobkov|sub.Gaussian.*score`: no hits on the five refs below. Method search: `hypercontract|log.Sobolev|Harnack|Nelson.*exponent`. Both used `git grep` over Markdown and TeX in `/Users/jonreilly/Projects/Physics`, piped to `head`. The broad line search reached its cap; it is discovery only. A completed filename pass remained below its cap of 160. Bounded source reads followed.

| Ref | Revision |
|---|---|
| origin/main | `4d88da5504d356762deb6b1a1c2695336af9fb81` |
| pr/10114 | `f76f6c649cff7dffbab664d8976e680e8f287fe9` |
| pr/10133 | `89faef229ff6e6bde42baad15ed8270c2f4087d8` |
| pr/10134 | `1e70c7211a2cdbc39001e619f1dd89db45e25851` |
| pr/10141 | `c73ad7b177d94f89ff37b77386936e3d52b48b05` |

Relevant hits, with their actual scope:

| Source | Statement and closeness |
|---|---|
| `origin/main:research/mass-gap/library/gap-skeleton-max.md:190–196` | B11 asks for a defective LSI for the lattice Hamiltonian in its ground-state representation, uniform in spacing, plus uniform positivity improvement. Its hypercontractive-semigroup citation is marked “memory”. Same broad objective; no score-to-Harnack or discrete exponent theorem. |
| `origin/main:research/mass-gap/library/gap-form-exercise.md:91–124` | Records 2D Wilson LSI at all fixed couplings, strong-coupling classical Gibbs LSI, and classical-spin strong-mixing implications. Different measures, dimensions or hypotheses; no proof of this implication. |
| `pr/10114` and `pr/10133`, `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/PLD.md:826–830` | “Route (c) relocates the wall to node A; it does not remove it.” The statement concerns convexity/LSI for a fine Wilson small-field chart or its marginal, not the vacuum slice transition. |
| `pr/10134:.claude/science/physics-loops/ym4d-hard-route-20261030/parts/upper-chain.md:1321,1419` | Conditional deep/far information does not bound direct exterior coupling; rare wells obstruct a proposed LSI. Different conditional measures and consumer; no counterexample under HC1's hypotheses. |
| `origin/main:research/mass-gap/library/gap-skeleton-max-b.md:355`, `gap-zero-transport-check.md:55–65`, `gap-zf-box-s.md:113–117` | Harnack estimates for harmonic functions in complex coupling domains. Different meaning of Harnack; no Markov-kernel estimate. |

Other hits are literature surveys, queue/history echoes, and archived parabolic-Harnack/convexity discussions. No exact target or Hopf–Lax/Bobkov hit appeared on any requested ref. This is a bounded search result, not a novelty theorem.

Read `prior/repo-search-2026-11-08.md` and `prior/gap-lit-hcvac.md`. Their earlier searches supply no completed check of row 940. The latter credits Gross, Diaconis–Saloff-Coste, Miclo and ground-state literature; it supplies no Wilson instance of the inputs. Its references to row 931 as “the outline” must not be read as attribution to Sussman–Alpoge. The PLD source blob is identical on pr/10114 and pr/10133 (`23feebab7605796232530434686729db3c4ccc28`), so it was read once.

Exact-target searches of `open-registry.md`, `open-core.md` and `l17c.md` returned no hit. FINISH rows 940 and 942 own this proof and this check. Row 941 owns the SU(2) input inequalities; this report does not attack them. No duplicate check was found.

The target-specific prior file was absent. Read GOAL.md and FINISH.md's required instructions first.
Scope: a line-by-line check of `library/gap-etohc-opus.md` (454 lines), including every PROVED or CONDITIONAL statement and each fact test.
Source SHA-256: `9f36c9ce4fa88219b6a0dfeac6a18e4f500f094345bab61b430d65f95b5b8030`.

Source locator: read the SA-index README instructions, chunk-02:88–105 and neighbouring search rows; searched its chunks and obligations for the target/method and GL8. Read outline 2195–2257 and 2313–2335 at the supplied `31a47c543775`. GL8 constructs `L = G C^(1/2) exp(-V) C^(1/2) G` and `Z_s(0) = Tr L^s`; `G` here denotes gauge projection. This construction is theirs and is reused. The outline and all three account files have no match for `hypercontract|log.?sobolev|harnack|hopf.?lax|bobkov`. This establishes absence of these words, not absence of every equivalent argument. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. No Balaban input is used by this check.

## Main implication

**(E-to-HC): HOLDS AFTER CORRECTION of the local proof error below.** Its conclusion and constant are unchanged. The hypotheses are those of HC1, including positive continuous density, the C^1 positive kernel, stationarity, gauge invariance and positive constants. The two quantitative inputs remain assumptions for Wilson SU(2).

All line numbers below refer to `gap-etohc-opus.md` at the pinned checkout.

1. **SGC, lines 141–147: HOLDS AFTER CORRECTION.** After Gibbs/Jensen, the bound is
   `E_pi[h phi] <= Ent_pi(h)/theta + m theta sigma^2/2`.
   When entropy is zero, take **theta down to zero**, not infinity. For positive entropy and sigma, the printed optimizing theta is correct. If sigma is zero, take theta to infinity instead. This proves the printed conclusion, including its edge cases. This is the first failing proof line, 147; it does not refute the lemma.

2. **RD, lines 149–185: HOLDS**, using corrected SGC. A check in a different variable makes the characteristic transparent. Put
   `J(t,lambda) = Lambda(t,lambda)/(lambda-1)` and `A = sigma^2 d(x,y)^2`.
   The printed entropy identity is `Y=(lambda-1)^2 J_lambda >= 0`. Thus
   `J_t <= lambda sqrt(2 A J_lambda)`.
   On `lambda(t)=ell/t`, with `ell>1`,
   `d J(t,ell/t)/dt <= lambda sqrt(2 A z) - (lambda/t) z <= ell A/2`,
   where `z=J_lambda>=0`. The last inequality is the square
   `(sqrt(z)-t sqrt(A/2))^2>=0`.
   Jensen gives `Lambda>=0`, while the bounded score gives
   `Lambda(t,ell/t)<=ell L d`; hence `J(t,ell/t)->0` at zero.
   Integration gives `Lambda(1,ell)<=ell(ell-1)A/2`, exactly RD.
   The derivatives, boundedness and endpoint use only (K). The Gaussian equality remark and the lambda-down-to-one KL limit hold. A merely averaged score bound does not enter this argument.

3. **H, lines 189–197: HOLDS.** Holder with exponent `p/(p-1)` in RD gives the factor `exp(sigma^2 d^2/[2(p-1)])` before raising to power p. Thus the coefficient is exactly the printed one. For Gaussian equality, the exponential tilt must match the selected pair x,y and Holder's equality condition; arbitrary c is not an equality case for a fixed pair.

4. **R1–R6 and BGL, lines 199–251: HOLD**, with the textbook inputs explicitly named there. R4 needs only a minimizing point and differentiability in x, not differentiability of squared distance at the cut locus. Its upper time derivative has the correct sign. The uniform time-Lipschitz bound on intervals away from zero permits reverse Fatou. For `b=1+alpha s`, direct differentiation gives
   `H' <= alpha Ent_nu(exp(bu))/(b^2 Z) - E_nu[exp(bu)|grad u|^2]/(2Z) <= 0`.
   The LSI cancels the two coefficients exactly. Gauge invariance survives the infimum because the group acts by isometries. Heat smoothing preserves that invariance; bounded density and gradient convergence justify extension from smooth to Lipschitz tests. Rademacher, compact heat smoothing and the Laplace spectral theorem remain named textbook inputs, not results established by a run.

5. **HC1, lines 255–268: HOLDS**, after the SGC repair. `F=log P(g^p)` is finite, Lipschitz and invariant even for non-invariant input g. The positive minimum of the kernel justifies its logarithm. H gives `p log Pg <= Q_s F` with `s=(p-1)/(p sigma^2)`. BGL and stationarity give the norm estimate at
   `Q=p(1+alpha s)=1+(p-1)(1+alpha/sigma^2)`.
   Truncation and positivity extend it to all L^p inputs. An LSI on invariant tests suffices because F is invariant. An LSI with no corresponding invariance of the kernel would be a different theorem.

6. **Iteration and (HC-vac), lines 270–287: HOLD.** Iterate the affine exponent map. Take `p=1+(1+alpha/sigma^2)^(-m)` to obtain the stated L^p-to-L^2 estimate. The L^2-to-L^q form also follows directly by taking p=2 in part (i). Thus it needs no self-adjointness assumption beyond HC1. The printed duality explanation is valid for the reversible Wilson kernel; HC1's abstract hypotheses alone need not imply self-adjointness. Integers m>=0 include the identity case. There is no extra dimension or volume factor, but alpha and sigma may depend on them.

7. **HC2, lines 396–406: HOLDS.** For a unit vector in the new metric put `v=theta z` in (SG~); this is precisely the directional sub-Gaussian bound with proxy 1. Compactness and positive smooth metric preserve all qualitative regularity. For `g~=sigma^2 g`, the squared gradient is divided by sigma^2 and kappa=alpha/sigma^2. For `g~=s(x)^2 g`, require s smooth and strictly positive, as required of a Riemannian metric. The weighted LSI remains an unsupplied input.

## Gaussian test and entropy endpoint

**One mode, lines 98–116: HOLDS.** Assume beta>0 and omega>0. Write `r=exp(-omega)` and `s^2=1/(2 beta sinh omega)`. Then

`v=(1-r^2)s^2=exp(-omega)/beta`,

`partial_x log p(x,w)=r(w-rx)/v=beta(w-rx)`.

Its conditional variance is `r^2/v=beta exp(-omega)=sigma^2`; its moment generating function is exactly Gaussian. The Gaussian LSI constant is `alpha=1/s^2`. Hence `1+alpha/sigma^2=1/r^2` and `alpha'=omega`. Completing the square in the likelihood ratio gives the exact RD moment `exp(lambda(lambda-1)r^2(x-y)^2/(2v))`.

Here is a separate continuous-semigroup check of the Gaussian step; it does not apply the compact theorem outside its domain. Let R_t be the Mehler operator with mean `exp(-t)x` and variance `s^2(1-exp(-2t))`. Its generator is `s^2 partial_x^2-x partial_x`. For a smooth positive bounded h, bounded away from zero, Gaussian integration by parts and differentiation give

`-d Ent(R_t h)/dt = s^2 I(R_t h)`,

`I(R_t h) <= exp(-2t) I(h)`,

where `I(h)=E[h'^2/h]`. The second inequality follows from `(R_t h)'=exp(-t)R_t h'`, weighted Cauchy–Schwarz and stationarity. The explicit Mehler formula gives entropy tending to zero. Integration proves `Ent(h)<=s^2 I(h)/2`, and thus `Ent(f^2)<=2s^2 E[f'^2]`. Truncation, a positive regularizer and smooth approximation extend the inequality to its Sobolev domain.

For `u=R_t f`, `q(t)=1+(p-1)exp(2t)` and `Z=E[u^q]`, differentiating the log norm gives

`d log ||u||_q/dt = q' Ent(u^q)/(q^2 Z) - s^2(q-1) E[u^(q-2)u'^2]/Z <= 0`.

The Gaussian LSI supplies the last inequality. Positive bounded test functions suffice first; truncation extends it to L^p. This proves sufficiency at the printed Nelson exponent. Necessity is already exact for every nonzero c:

`log ||P exp(cx)||_Q - log ||exp(cx)||_p = c^2 s^2 [1+(Q-1)r^2-p]/2`.

No small-c or large-c limit is needed. The same test gives sharpness of alpha. The affine Hopf–Lax test at lines 240–241 also holds: `Q_s(c x)=c x-c^2 s/2`, and at exponent `1+s` both norms equal `exp(c^2/2)`. This is a Gaussian/noncompact sharpness test, not equality on the compact Wilson manifold.

**Product statement, lines 117–119 and 438: HOLDS AFTER CORRECTION of its domain.** For a finite product of positive-frequency Gaussian photon modes, the score covariance is diagonal. Its largest eigenvalue is `beta exp(-omega_min)` and its LSI constant is `2 beta sinh omega_min`. Tensorization follows by conditional entropy decomposition, applying the one-coordinate LSI, and Cauchy–Schwarz when differentiating square roots of conditional second moments. Single-coordinate tests attain the weakest constant. The product photon chain therefore has `alpha'=E_1=omega_min`.

The parenthetical “(FP)” must mean **the photon factor of FP**. The actual FP definition in `gap-seam-max.md:88–119` also includes three compact Polyakov phases. Their eigenvalue ratios are `exp(-|e|^2/(2 beta b))`. Consequently the full model has

`E_1(FP)=min(omega_min,1/(2 beta b))`,

and the equality `E_1(FP)=omega_min` generally fails. This correction does not change the one-mode exponent test. No inequality for the toron factor was checked or supplied by row 940.

**Entropy endpoint, lines 120–123 and 280–281: HOLDS.** Put `K=1+alpha/sigma^2` and take p=1+epsilon, Q=1+K epsilon. For a bounded density g, differentiating `log ||g||_p` at p=1 gives `Ent(g)`. HC1 yields `K Ent(Pg)<=Ent(g)`, so rho=1/K. For a general density of finite entropy, truncate and normalize g. The truncations converge in L^1 and entropy; the bounded kernel makes their images converge uniformly. Passing to the limit gives the same inequality. Infinite input entropy is trivial. This is an endpoint consequence of HC1, not a derivation of HC1 from entropy contraction alone.

## Kernel and seed consumer

**Kernel choice and standing setting, lines 48–64, 132–139, 295–301 and 390–394: HOLD.** Use the outline's already constructed convolution C and gauge projection G. With `M=exp(-V/2)` and `A=M C^(1/2) G`, one has

`A* A=G C^(1/2) exp(-V) C^(1/2) G=L`,

`A A*=M C G M=T`.

The nonzero eigenvalues, with multiplicity, agree: A maps an eigenspace of A*A at lambda>0 bijectively to the corresponding eigenspace of AA*, with inverse A*/lambda. The kernel of CG is the gauge average of a strictly positive product Wilson kernel. Thus T is strictly positive and smooth. It is invariant in each argument separately. A convention using `exp(beta sum x_p)` instead of `exp(-beta sum(1-x_p))` only rescales T; all normalized eigenvalues, X and the ground-state chain are unchanged.

With the positive normalized ground state assumed in the setting, its eigenvalue equation makes Omega C^1. The printed p is normalized, symmetric and stationary, and its centered score identity follows by differentiating its normalization. The full-support positive density justifies upgrading an almost-everywhere SG bound to every x; continuity alone with an arbitrary singular nu would not justify that upgrade. In the stated slice setting the required full support is present.

**Thermal bound, lines 289–290: HOLDS conditionally.** Read the actual Proposition HC and HOT proof in `gap-direction-max.md:199–206,305–320`. Its argument applies to the same gauge-projected p. For a density h bounded by H, `||h||_q<=H^((q-1)/q)<=H^(q-1)`. Since `log sup p_1<=36 beta |B|`, HC-vac and the Hilbert–Schmidt trace identity give

`X(2m+2;B)<=72 beta |B| exp(-2 alpha' m)`.

The gap conclusion also follows without the trace argument: linearize HC1 at `g=1+epsilon f`, with f centered. The second-order norm terms give `||Pf||_2^2 <= K^(-1)||f||_2^2`. Apply this to a nonconstant eigenfunction. Thus `E_1>=log(K)/2=alpha'`. This remains a conditional estimate on the stated box.

**The assertion “Form W ... follows” at lines 291–293 and 440 FAILS as the stated deduction.** The threshold `x_*=log(22/17)` is a consequence of Form W, not a sufficient condition for its two clauses. The source itself defines Form W by `S_ev<=1/10` and `Q_0<=1/20` (`gap-direction-max.md:179–184`). Lemma SPLIT (`gap-crux-core-max.md:265–273`) gives

`S_ev<=S`, `Q_0<=S/(1+S)`, and `Form W => 1+S<=22/17`.

It does not reverse the last arrow. For example, one even excited level of thermal weight 1/5 gives `X=log(6/5)<log(22/17)` but `S_ev=1/5>1/10`. A positive two-state transfer matrix with eigenvalues 1 and `(1/5)^(1/a)` realizes this spectral example. This refutes the proposed inference from X alone; it is not a counterexample to an unproved Wilson-specific strengthening.

Two repairs have written proofs:

- Keep `x_*`: conclude the **full thermal threshold** `S<=5/17<3/10`. This is sufficient for the ratio-at-least-24 threshold stated in `gap-seed-shape.md:114–125`, subject to that separate theorem's hypotheses. It does not establish the named split Form W.
- Keep Form W: use `x_W=log(20/19)`. Then `S<=1/19<1/10` and `Q_0<=1/20`. Replace the right-hand constant by `log(72 beta 24^3 / log(20/19))`. The sufficient condition is therefore
  `alpha'(a-2) >= log(72 beta 24^3 / log(20/19)) + 3 log a`,
  for even integer a>=2. This stronger condition proves both clauses on that box.

The exact `x_*` constant is `log((11446272/5)/log(22/17))` at beta=23/10. It is **not exactly 16.0**. Nevertheless 16 is a safe upper bound for this weaker thermal target. A hand certificate is

`log(22/17) > 2(5/39+(5/39)^3/3) > 1289/5000`,

`exp(4) > sum_{j=0}^{13} 4^j/j! > 5459/100`,

`(5459/100)^4 (1289/5000) > 11446272/5`.

Thus `exp(16) log(22/17)>72(23/10)24^3`. These finite rational inequalities, not a decimal run, justify rounding upward to 16. The printed equality should be replaced by an upper bound. The integer-time corollary needs even a; for arbitrary integer a>=2, put `m=floor((a-2)/2)` and replace a-2 by 2m. Monotonicity of X then gives the bound at a.

## Remaining fact tests and GUIDE

**Fact tests at lines 125–128: HOLDS AFTER CORRECTION of scope.**

- **U(1):** the calculation is for the defined Gaussian photon model, not the full compact Wilson U(1) measure. In that model `omega_min=2 asinh(sin(pi/b))<=2pi/b`. Thus, at b=24a, the sharp photon rate obeys `alpha'(a-2)<=pi/12`, far below the displayed seed requirement. Adding torons cannot improve it. At each finite b the Gaussian LSI does hold; what fails is the required quantitative size dependence, not existence of an LSI. No compact-Wilson U(1) theorem follows from this test.
- **Frozen Q_8 and 2T:** the connected-manifold gradient assumptions do not describe a finite configuration space. The theorem makes no frozen-group prediction. This domain exclusion holds; it is not a computation of a discrete-group LSI or hypercontractive rate.
- **SMALL-BOX:** HC1 assumes the inequalities and their constants. It asserts no Wilson estimate at large beta on a fixed box. This qualification holds. Row 940 performs no separate small-box computation.
- **Ceilings:** no numerical ceiling is a premise of HC1, so those numerical threshold tests are not applied here. However, HC1 still uses a supremum over conditional starting slices. Finiteness on each compact box gives no adequate box-uniform rate. HC2 shifts the requirement to a weighted LSI; it does not supply that inequality. The text's bimodality discussion at lines 407–413 remains ARGUED and is not checked as a theorem.

**Rotor formulas, lines 305–314: HOLDS for the described model, with numerical bounds qualified.** For `T(u,w)=exp(V(u)/2+beta cos(u-w)+V(w)/2)`, differentiation gives `V'(u)/2-beta sin(u-w)`. Centering removes the first term, exactly as stated. In the continuum uniform case, with I_n the circle integral of `exp(beta cos theta) cos(n theta)`,

`r_1=I_1(beta)/I_0(beta)`, `E_1=-log r_1`,

`Var_pi(phi)=beta^2 E_pi[sin^2 theta]=beta I_1(beta)/I_0(beta)`,

`E_pi exp(t phi)=I_0(beta sqrt(1+t^2))/I_0(beta)`.

The variance identity follows by integrating the derivative of `sin(theta) exp(beta cos theta)`. Completing the cosine/sine linear combination gives the last identity. A variance is a lower bound on a sub-Gaussian proxy; proving a uniform upper proxy needs the whole moment-generating function. For the actual N-point uniform grid the exact eigenvalues instead are the finite Fourier sums

`lambda_j=N^(-1) sum_{k=0}^{N-1} exp(beta cos(2pi k/N)) cos(2pi j k/N)`,

and the score variance is `beta^2(1-lambda_2/lambda_0)/2`. These identities specify which arithmetic can be compared with the grid. They do not identify a sampled supremum with the full proxy.

**GUIDE refutation criteria, lines 309–324: FAILS as a claimed refutation of RD/HC1.** A maximum over finitely many tilts and slices is a lower estimate of the required supremum, not a proved SG constant. A violation using it can reveal an underestimated proxy. For HC1, the grid law is atomic and does not satisfy the positive-density hypothesis used by BGL. A transplanted continuum Holley–Stroock constant is not a demonstrated LSI constant for an unspecified grid derivative. Thus even a violation at the printed `alpha_low` would not, by itself, refute HC1. A repaired criterion is: “test the chosen discrete surrogate inequality at these sampled constants.” It can guide, but does not certify or refute the continuum theorem without a matching argument.

There is also a concrete inconsistency in the lower-bound definition. At V=0 the positive circulant matrix has constant Omega. Hence `exp(-osc log Omega^2)=1` exactly, at every N. Lines 313–314 define alpha_low by this expression, while lines 343–344 say alpha_low is about 0.99995. Those statements cannot both be the literal calculation. A grid-dependent prefactor might explain the number, but neither its derivative convention nor its formula is supplied. The L-BFGS value is at most a variational upper estimate for its specified discrete objective; it is not a proved upper bound for the continuum LSI constant.

**Displayed arithmetic at lines 333–352: HOLDS to the displayed rounding, where it is recoverable from the table.** Substituting the seven printed `(alpha_up,sigma^2)` pairs into `log(1+alpha_up/sigma^2)/2` gives respectively about

`1.578, 0.588, 0.231, 0.178, 0.000885, 0.174, 0.0627`.

Each is smaller than the printed E_1. The two displayed ratios are `0.231/0.299`, about 0.77, and `0.0627/0.067`, about 0.94. In the uniform rows, `sigma^2/beta` is consistent at the table's precision with `exp(-E_1)`. These are arithmetic consistency checks of rounded numbers, not verification of their computed origins. The three nonuniform entries' eigenvalues, proxies and variational estimates have no supplied raw calculation to check. No Gaussian-limit theorem for the optimized rotor constants is established by these seven rows; retain that limiting remark as heuristic.

**Positive-control threshold: HOLDS; reported magnitudes are unverified.** If Pf=r f, E f=0 and f is bounded, put `g=1+epsilon f>0`. Then, for Q-1=K(p-1),

`log ||Pg||_Q-log ||g||_p = epsilon^2 (p-1)(K r^2-1) E[f^2]/2 + o(epsilon^2)`.

Thus `K>exp(2E_1)` must produce a violation for small epsilon in this one-step model. This checks the sign and location of the proposed positive control. It does not check the numerical optimizer values `2.7e-4`, `1.3e-3`, `7.5e-4`, `3.9e-3`, or their reported range. Below this linear threshold the perturbation test says nothing about global nonlinear maximizers.

**Run record and pass counts, lines 325–355 and 443: HOLDS AFTER CORRECTION to an explicitly unverified author report.** There is no `hc_guide.py`, `hc_guide.log` or `positive_control.log` in the allowed checkout. The cited paths are the author's Mac-mini `/tmp/gap-etohc-940/` artifacts, not a supplied local source. This check did not search another machine or existing `/tmp` directories. Therefore the seven RD maxima, all optimizer maxima/pass counts, resource record and positive-control magnitudes are **not verified**. Neither their truth nor their falsity is established here. The planned N=512 and reported N=256 are different; the latter is the only claimed run model. Read every numerical “PASS” as “the author reports no violation found in the run”, not as a norm bound or a checked run receipt. No new GUIDE job was run.

## Statement coverage and disposition

This table covers every PROVED/CONDITIONAL item in the result table and the auxiliary marked statements. A “HOLDS” verdict covers only its stated assumptions and domain. The source text was not edited.

| Target lines / statement | Verdict |
|---|---|
| 48–64, 132–139: vacuum chain, centered score, regularity | HOLDS in the positive-density gauge-projected setting |
| 98–116: one-mode Gaussian constants, Nelson exponent, RD equality | HOLDS; omega>0, beta>0 |
| 117–119: product Gaussian modes | HOLDS AFTER CORRECTION to the photon factor; full FP includes torons |
| 120–123, 439: entropy endpoint | HOLDS, with finite-entropy extension given above |
| 125–128: U(1), frozen groups, SMALL-BOX and ceilings | HOLDS AFTER CORRECTION to the precise scope described above |
| 141–147, 431: SGC | HOLDS AFTER CORRECTION; theta decreases to zero in the zero-entropy case |
| 149–185, 432: RD and its KL corollary | HOLDS using corrected SGC |
| 189–197, 433: Harnack | HOLDS |
| 199–251, 434: R1–R6, BGL, affine test, smooth approximation | HOLDS with the named textbook inputs |
| 255–268, 435: HC1 | HOLDS conditionally on its complete hypotheses |
| 270–287, 436: E-to-HC and all exponent forms | HOLDS AFTER CORRECTION of SGC; rate unchanged |
| 289–290, first clause of 440: X bound and spectral gap | HOLDS conditionally |
| 291–293, Form-W clause of 440 | FAILS as the stated inference; corrected thermal or stronger split-seed conclusions are proved above |
| 390–394, 441: A*A / AA* kernel choice | HOLDS; common normalization or normalized spectra |
| 396–406, 437: metric corollary HC2 | HOLDS conditionally on the weighted LSI and dominating metric |
| 309–324: GUIDE criteria as theorem-refutation criteria | FAILS; sampled constants and atomic model do not meet the asserted hypotheses |
| 333–352: derived alpha-prime values and displayed comparisons | HOLDS as rounded arithmetic; raw parameter estimates remain unverified |
| 343: uniform alpha_low about 0.99995 from the defined formula | FAILS literally; the defined expression equals 1 |
| 345–349: positive-control threshold | HOLDS; optimizer magnitudes unverified |
| 325–355, 443: seven-case numerical run and counts | HOLDS AFTER CORRECTION to unverified author-reported GUIDE observations |

Lines 357–388 credit Wang, Bobkov–Gentil–Ledoux, Nelson and Gross. Their proofs or methods are credited as in the source, with the Gaussian argument supplied above. This check did not fetch the papers, confirm bibliographic metadata, or certify the claim of novelty. The SA word search and GL8 source passage were independently checked. Lines 407–413 are explicitly speculative; line 444 keeps the SU(2) inputs OPEN. Lines 422–425 and 454 inherit the corrected scope: no counterexample exists **within HC1's full class**, but neither its hypotheses at the seed rate nor the claimed split-seed constant has been established for Wilson SU(2).

## Final checkpoint

Checked line by line by Codex (gpt-6-astra, xhigh), including a separate derivation of the RD characteristic bound and the Gaussian semigroup exponent. First failing proof line: 147, repaired above. The main conditional implication survives. The split-seed inference fails and has explicit replacement conclusions. The full FP gap identification needs the photon-only qualification. The GUIDE record is unverified and its refutation criteria are invalid as stated.

Only this report was written, at checkout `f529763f248c83b2bb3a7470790efa98628fd7d1`. No source note, registry, queue, audit record or status was changed. No numerical proof, numerical job, external post, commit or push was made. The report is left in the requested checkout for the lead. Open obligations remain the SU(2) input inequalities at the needed size-dependent constants, owned by row 941. This check supplies research text and grants no status.

RESULT: (E-to-HC) HOLDS AFTER CORRECTION of SGC's zero-entropy limit, with alpha' = (1/2) log(1+alpha/sigma^2) unchanged and the Gaussian photon Nelson exponent exact; the inference to Form W at the printed threshold FAILS and is repaired above; full FP requires toron modes; GUIDE theorem-refutation criteria FAIL and raw run claims remain unverified; SU(2) seed inputs remain OPEN.
