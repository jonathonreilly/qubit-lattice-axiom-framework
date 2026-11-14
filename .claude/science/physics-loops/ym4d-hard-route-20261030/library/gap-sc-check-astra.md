## Repo search

Provenance: Codex; requested runner profile GPT-6 Astra, xhigh; row 951; source checkout
`b6bdf145c88e281a8267875fa42682efea769191`. Research-text check, not an audit;
this report grants no status. Author: Claude Fable 5.2 max, row 950.

The target-specific prior note `library/prior/gap-sc-check-astra.md` is absent.
Search and source receipts are recorded below. No mathematics is discharged
by a computation. Only this report is being changed.

### Completed checkpoint

All 645 target lines were read and checked. The load-bearing checks use
endpoint counting, direct entropy duality, covariance disintegration and
displayed hand arithmetic. Existing DW work is cited. No simulations ran.
Raw Mini scripts/logs were unavailable; their production and errors remain
unverified. The next decision belongs to the lead: retain the corrected
implications, and require an equilibrated, controlled frame limit before
using the GUIDE data to choose between SC and its projected alternative.

Target SHA-256:
`bc6b2f8cae19357dda91881b925857ef7907dae2cc31063b86837e581faf9f29`.
This checkout's branch is `lanework`. It has no local `origin/main` ref;
the requested full repository supplied the following refs:

| Ref | Commit |
|---|---|
| origin/main | `3e13676f02af206100abfb2875521904e8f53cda` |
| pr/10114 | `f76f6c649cff7dffbab664d8976e680e8f287fe9` |
| pr/10133 | `89faef229ff6e6bde42baad15ed8270c2f4087d8` |
| pr/10134 | `1e70c7211a2cdbc39001e619f1dd89db45e25851` |
| pr/10141 | `c73ad7b177d94f89ff37b77386936e3d52b48b05` |

### Search receipts and reuse

The full-repository searches used `/Users/jonreilly/Projects/Physics` and
`origin/main`, `pr/10114`, `pr/10133`, `pr/10134`, `pr/10141`, with `*.md`
and `*.tex`. Each command was bounded with `head` and run separately.

* Exact query: `LSI-vac|SG-step|first.step electric|gap-sc-max|gap-sc-check-astra|Hess.*log.*Omega`.
  No hits on the five refs.
* Method query: `log.Sobolev|hypercontract|semiconcav|ground.state.transform|electric.*susceptib`.
  Broad discovery lists reached their caps. They are not absence evidence.
  Follow-ups restricted the paths to the YM4D soft-route and research snapshots,
  and read the primary passages below. A query including generic conditional
  covariance was too broad; its unrelated hits supply no premise here.
  The final targeted query
  `Theorem BL-TILT|ground-state transform of|B11\. The small torus`
  returned 20 lines across the five refs (cap 25), including the two
  soft-route primary files on both pr/10114 and pr/10133 and B11 on main.
  The other common hit, `docs/FINITE_NATIVE_WINDING_CURVATURE_BOUNDED_THEOREM_NOTE_2026-09-15.md`,
  concerns a different rotor ground-state transform; it was not used as a
  Wilson susceptibility input. No search hit already checks row 950.
* The November 8 digest was read. It covers earlier RG obligations, not SC or
  SG-step. The registry search finds SC-two-reference (line 475), a different
  Landau-reference comparison, and FC-MEAN-MATCH/FC-TEST, different contour
  obligations. No competing owner of this row-951 check was found. The existing
  `gap-sc-box-check.md` checks row 683's strong-coupling SC_B, not this SC.

| Relevant hit, source read | Exact statement and closeness |
|---|---|
| `pr/10114:.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_CONSTRUCTION_ASTRA.md:164–190` | The ground-state kernel is `T(U,V)psi_0(V)/(lambda_0 psi_0(U))`; its invariant law is `psi_0^2 dU`. Its minorization constant is `exp(-2 beta n_s)`. This already supplies the normalized finite-box transfer frame, but no volume-free SC bound. |
| Same soft-route prefix, `NODEA_RES55.md:188–220` | BL-TILT assumes a convex domain, H-convex potential, quadratic domination, centered tilted laws and `lambda_bar c_bar<1`. It yields `E exp(lambda_bar a)<=det(I-lambda_bar B)^(-1/2)`. This is the convex tilt method, not a bound for the full compact Wilson slice. No reproof or compact-law import is made. |
| `origin/main:research/mass-gap/library/gap-skeleton-max.md:190–198` | B11 names a cutoff-uniform defective ground-state LSI and positivity improvement as its crux. It proposes a route; it supplies neither input of the present chain. |
| Local `gap-sgstep-opus.md:94–194,239–314` (Claude Opus 5.5) | TG, EF, HV, HSS and CEN already supply the score representation, Hessian identity, sufficient implication and central-slice cancellation. Row 950 extends these; it does not originate them. |
| Local `gap-lsivac-max.md:223–324` (Claude Fable 5.2) | Theorem C0 assumes entropy loss at most `I(g)/(2 alpha_c)` and `I(Pg)<=theta I(g)`, then concludes LSI with `alpha_c(1-theta)`. These are named inputs, not Wilson estimates. |
| Local `gap-sgstep-check-astra.md:130–156` (Codex) | Already corrects the arbitrary-versus-optimal SC constant and supplies a hand certificate for the DW coefficient `3/20`. The certificate is reused below, not rederived. |

The Sussman–Alpoge index was consulted before source reads: README; chunk 02
rows for GL3, GL8 and GL13–14 with their neighbours; chunk 25 rows for GCB5
and GCB20–21; obligations 1376–1406; CA full-index rows 870–884.
At the supplied source revision `31a47c543775`, the bounded reads give:

| Source | What it already contains |
|---|---|
| Outline 2197–2231, GL3 | Positive SU(2) convolution coefficients `2 exp(-beta) I_(2l+1)(beta)/beta`, proved by the character integral and positive series. |
| Outline 2315–2335, GL8 | Gauge averaging inserted between layers; a positive trace-class transfer and the torus trace identity. |
| Outline 2456–2498, GL13–14 | Temporal-gauge coordinates and the exact two-neighbour conditional density `C(w,v) exp(-V_j(v;eta)) C(v,w')/z`. This retains every plaquette. It is not the one-sided law after integrating the future. |
| Outline 27149–27212, GCB3–5 | Marginal log-concavity via transport in the stated integrable class. Use as prior work for the convex-class discussion. |
| Outline 27493–27529, GCB20–21 | Centered sub-Gaussian linear marginals and covariance domination for the Gaussian law with even log-concave cutoff. No full Wilson-law identification. |
| CA-II 81804–81858, `8.3:cor-subgaussian-tails` | `nu_H exp(s(F-nu_H F))<=exp(s^2\|ell\|^2/(2 lambda))`, under the explicitly stated coercivity of the window Hamiltonian. The proof follows the linear tilt while preserving coercivity. It supplies the method, not the missing uniform susceptibility. |

Credit these transfer and tilt constructions to Ethan Sussman and Levent Alpoge,
with Claude and Codex as authors of their text. No Balaban paper is imported;
no mathematical step here depends on an unavailable original paper.

## 1. Exact law, Omega, and geometry

Line numbers refer to `gap-sc-max.md` at the pinned checkout. A verdict on an
implication says nothing about its hypotheses holding for Wilson SU(2).

| Statement | Verdict | Check |
|---|---|---|
| 2.1, lines 57–63, exact conditional density | HOLDS | Substituting `Omega=exp(F-V/2)` in the normalized transfer cancels `V(u)/2` and gives exactly (2.1). Boundary data enter the **w-dependent** part only through `beta<u,w>`; `F(u)` is the normalizer. |
| UNROLL, lines 65–72, formula (2.2) | HOLDS | Each interior F occurs once with each sign. The remaining terminal term is F(w_n); every new slice has full `-V(w_t)`. Its first marginal is the same Markov transition for every n. |
| Lines 73–79, free terminal slab and (2.3) | HOLDS AFTER CORRECTION | The endpoint replacement must be **`F(w_n)=+V(w_n)/2`**, not `-V(w_n)/2`, to leave the advertised last-slice factor `exp(-V/2)` and `T_0^(n-1)1`. The printed negative sign gives `exp(-3V/2)` and terminal vector `h=exp(-V)`. Both choices have the same ground-state limit at fixed finite B, so the limiting identity survives. |
| 2.3, lines 81–90, electric covariance interpretation | HOLDS AFTER CORRECTION | Right multiplication by `u_l^*` is orthogonal, hence `<xi_l u_l,w'_l>=<xi_l,Im(w'_l u_l^*)>`. The exact implications are `SC(C) => beta^2 Cov_u(E)<= (C+beta)Id` and `Cov_u(E)<=c Id => Hess F <= (beta^2 c+beta)g`. The printed `O(beta)` equivalence is only existence of box-free bounds, not equality of constants. The Schur bound must sum colour indices too (a fixed factor 3 suffices). |
| TV, lines 92–99 | HOLDS | Conditional on the orbit, the variance of `beta<z,w'>` is the frame variance. Total variance plus HV gives precisely (2.4), including its minus sign. |
| HG and SC-hor, lines 101–116 | HOLDS | A Killing field has constant inner product with a geodesic tangent. Thus a horizontal geodesic remains horizontal, including at singular orbits. Along it, `d^2 log p/ds^2 >= -(C_h+beta)`. Integrating the normalized-density Taylor bound gives the claimed MGF estimate for all real t. Projection to the horizontal part only decreases the tangent norm. |
| Lines 117–118, neither converse holds in general | HOLDS AFTER CORRECTION | Keep only the sufficient arrows. CEN proves pointwise cancellation at central slices, not a counterexample to a **globally quantified** converse. The candidate in section 5 is not such a proof. |
| AV, lines 120–133, SU(2) inequality | HOLDS | Under J, independent gauge rotations at distinct base sites kill cross-site second moments. At one site the colour tensor is `delta_ab c_ll'`; c is positive semidefinite and `tr c=sum_l E\|E_l\|^2/3<=1` for the three outgoing links. Conditional variance is bounded by the conditional second moment. Thus `E_nu Cov_u(E)<=Id`. This does not bound `E_nu \|\|Cov_u(E)\|\|` or a direction chosen after observing u. |
| Lines 130–131 and section 4: AV is false for U(1) | HOLDS AFTER CORRECTION | The **proof** does not apply: the U(1) adjoint action is trivial. No counterexample to the same annealed numerical inequality is supplied. Replace “false” by “not established by this argument.” Dirichlet-slice GUIDE data do not test this vacuum average. |

For the terminal limit, fixed B is essential. The positive continuous kernel
on compact M has a strictly positive ground state and a strict spectral
separation at that B. Applying one kernel maps L2 convergence into uniform
convergence, since its L2 row norms are uniformly bounded. Thus
`lambda_0^(-n) T_0^n h -> <Omega,h> Omega` uniformly, with `||Omega||_2=1`.
Both h above are positive. Bounded first-layer observables then converge in
mean and second moment. This proves (2.3) at fixed B; it gives no uniform rate
in B, and supplies no error estimate for the simulated thickness T=6.

The Omega factor encodes the integrated future of this half-cylinder. Its
presence preserves the local **space-time** representation, not a finite-range
one-slice interaction. SC is a bound on linear boundary susceptibilities;
calling it equivalent to general strong mixing or to the absence of every
kind of boundary order is stronger than the proved statement.

## 2. SC, FC, LSI-vac, and the Gaussian tests

| Statement | Verdict | Check |
|---|---|---|
| 3.1, lines 190–194, C2/SC dictionary | HOLDS AFTER CORRECTION | Use the temporal-gauge law in row 941, and define `C_*=sup Hess F[u;z,z]` over unit vectors (horizontal for SC-hor). Then `C_*-beta <= sup sigma_tilde^2 <= C_*+beta`. The lower inequality is false for an arbitrary loose upper bound C_F. Example: free links have F constant but also satisfy SC with C_F=100 beta. This correction already appears in row 945. The all-ambient COV bound does imply SC with `beta^2 kbar+beta`. |
| 3.2, lines 196–202, reverse LSI and reverse Poincare | HOLDS | The duality can be checked directly as below; no remembered theorem is needed. The factors 2 and sigma squared agree with the stated entropy convention. |
| 3.2, lines 203–208, curvature reading | HOLDS AFTER CORRECTION | `Ric-2 Hess log Omega` is the diffusion curvature tensor. Its lower bound is an analogy and a sufficient route, not an equivalence between SC and SG-step for this discrete kernel. A fixed connected compact manifold does have a gap; the intended point is that a lower-curvature bound alone gives no **uniform positive gap over a family**. |
| 3.3, lines 210–215 | HOLDS | Stationarity gives `I(Pg)<=2 sigma^2[Ent(g)-Ent(Pg)]`; C1-av gives `I(Pg)<=(sigma^2/alpha_c) I(g)`. C0 then gives `alpha=alpha_c-sigma^2` only if positive. SC-hor supplies the sufficient proxy `sigma^2=C_h+beta`. |
| 3.4, lines 217–219; photon fact test | HOLDS | For the Gaussian modes, `sigma^2=Hess F=beta exp(-omega)`, `alpha=2 beta sinh(omega)`, and the optimal Fisher contraction is `exp(-2 omega)`. As the lowest positive mode tends to zero, SC remains bounded while the latter two rates degenerate. This disproves an unrestricted model-class implication; it is not a counterexample within Wilson SU(2). Remove or regulate zero modes before forming a Gaussian probability law. |
| 3.5(i), lines 222–225 | HOLDS | Completing the square gives conditional covariance `A^-1` and mean `beta A^-1 u`. The stationary precision is `A-beta^2 A^-1`. It is positive exactly when every eigenvalue of A exceeds beta. Hence `beta^2 A^-1<beta Id`. |
| 3.5(ii), lines 226–233 | HOLDS AFTER CORRECTION | Retain the cited convex-marginal and Brascamp–Lieb premises **and** a positive normalizable ground state obtained as a limit of log-concave iterates (for example under a confining convex U). Convexity alone does not provide a vacuum: U=0 on R^d has no L2 ground state. The F used for `Hess F=beta^2 Cov` is `log Omega+U/2+beta\|q\|^2/2`; omitting the kinetic self-term changes its Hessian. With these conventions the bound holds. |
| 3.6, lines 235–244; “separate input” in sections 3 and 8 | HOLDS AFTER CORRECTION | The reverse non-implication is explicitly unproved. Averages versus suprema are not a logical counterexample. No explicit R_0 with the required uniform LSI/FC is supplied, and Wilson vacuum massiveness is not available as a premise. Say “no implication from LSI-vac or FC to SC is established here.” Two-way independence has not been proved. |

Here is a direct check of the reverse-LSI equivalence. Fix u and a unit z;
write `X=phi_(u,z)` and `mu=pi_u`. X is centered, smooth, bounded and
gauge invariant as a function of w. For a density h relative to mu, Jensen
gives `t E_mu(hX)<=Ent_mu(h)+log E_mu exp(tX)`. The sub-Gaussian bound and
optimization in t give `(E_mu hX)^2<=2 sigma^2 Ent_mu(h)`.
Taking `h=g/Pg` and the supremum over unit z yields (3.1).
Conversely (3.1) bounds each directional derivative. For
`h_t=exp(tX)/E_mu exp(tX)`, let `L(t)=log E_mu exp(tX)`.
The directional inequality gives
`(L')^2<=2 sigma^2(tL'-L)`.
Equivalently,
`(L'-sigma^2 t)^2+2 sigma^2 L-sigma^4 t^2<=0`, so
`L(t)<=sigma^2 t^2/2`. The case sigma=0 follows by taking the second-order
limit, which forces X=0. The reverse-Poincare equivalence follows from
`d_z Pf=Cov_mu(X,f)`; testing f=X gives the converse. These arguments use
the projected score throughout.

For the Gaussian contraction check, put `r=exp(-omega)` and
`v=exp(-omega)/beta`. Then `Pf(q)=E f(rq+sqrt(v)Z)` and the stationary
variance is `v/(1-r^2)`. Cauchy–Schwarz gives
`I(Pg)<=r^2 I(g)`. Exponential g attain equality. Exponential tilts also
bound the LSI constant above by `(1-r^2)/v=2 beta sinh(omega)`; the Gaussian
LSI gives the reverse bound. This checks the constants without a numerical run.
The mode list was read at `gap-seam-max.md:86–113`: its nonzero transverse
modes have `cosh(omega_k)=1+sum_i 4 sin^2(k_i/2)/2`. This makes the lowest
positive omega tend to zero with the box. That note also includes three
compact Polyakov phases. The computation here concerns the transverse
Gaussian sector, not an identification with the full compact Wilson law.

## 3. Remaining hand arguments and fact tests

| Statement | Verdict | Check |
|---|---|---|
| Free-link test, lines 250–251 and 328 | HOLDS | The constant function is the positive eigenfunction when V=0. Differentiate the constant `int exp(beta<u,w>) dw` twice along a unit-sphere geodesic: `beta^2 Var(<z,w>)=beta A(beta)\|z\|^2`. Independence of links gives the product formula. |
| DW test, lines 252–253 | HOLDS AFTER CORRECTION | In the abstract RS chain, with trivial gauge group, total variance gives `beta^2 c_epsilon^2 N/2`; HV subtracts at most beta. The exact formula in row 944 is correct. Its rounded Bessel estimate was not a proof of `0.15`. Use row 945's existing hand certificate, lines 140–156, which proves `c_epsilon^2/2>3/20` at `epsilon=1/beta`, `beta=23/10`. Thus the displayed lower bound holds. It is not a Wilson example or a universal characterization of how SC can fail. |
| Frozen Q_8 and 2T, lines 254–255 | HOLDS | No tangent/Hessian inequality of this type was defined on the finite configuration space. Domain exclusion supplies no positive or negative test of a separate discrete inequality. |
| U(1) differential identities, lines 256–263 | HOLDS AFTER CORRECTION | The exponential-family, total-variance, horizontal-geodesic and SC-hor implications extend to S1 with its metric. The electric component is now scalar. Omit the SU(2)-specific CEN assertion in the last sentence of 2.5 and the unsupported assertion that AV's numerical inequality is false. Real-slice conjugation makes the raw electric mean zero, but does not itself bound or lower-bound the projected variance. |
| SMALL-BOX, lines 264–268 | HOLDS AFTER CORRECTION | The stated small-gap premise can constrain the combined HC rate. The proposed `C_F` of order `beta^2 N`, and consequently `alpha/sigma^2` of order `1/beta`, have not been proved: the required low-temperature concentration and an upper bound on alpha are absent. The raw-frame covariance also is not the optimal projected sigma. Retain this as a conditional compatibility discussion, not a fact-test computation or proof of beta dependence. |
| FT-CEIL, lines 269–271 | HOLDS in its stated scope | A ceiling for a different fully conditioned law or a positive-curvature criterion does not automatically bound this one-sided susceptibility. None of the numerical ceilings is used to prove a lemma here; they were not recomputed. |
| Small-beta neighbour count, lines 272–274 and 306 | HOLDS AFTER CORRECTION | The temporal-gauge **first** free layer has 12 spatial neighbours and one free temporal neighbour (the other temporal neighbour is fixed). Bulk spatial links have 14, not 13. An all-half-space Dobrushin argument needs the bulk influence matrix and an actual influence bound. No threshold `1/13` is proved. In the original unfixed four-dimensional link variables, an interior link meets six plaquettes, with 18 other-link incidences. |
| REC, lines 278–293 | HOLDS | Simultaneous right translation preserves the kernel and Haar measure. Twice differentiating the log integral gives the displayed expectation plus variance. `Z(w)=w eta` is indeed left-invariant and its integral curves are geodesics. The iterated formula is verified below. |
| Gaussian check of REC, line 295 | HOLDS | For the difference-kernel convention `F_tilde''=beta(e^-omega-1)` and `U''=beta(e^omega+e^-omega-2)`. Thus `(F_tilde-U)''=beta(1-e^omega)`; its linear force has variance `beta(1-e^omega)^2 e^-omega`. Their sum is `beta(e^-omega-1)`. |
| REC noncontraction, lines 296–309 | HOLDS as a failed estimate | Taking suprema returns C_F with coefficient one and adds the nonnegative force variance. This particular bound does not close. It is not an impossibility theorem for every use of the recursion. |
| 6.1, lines 314–324, covariance form and seed use | HOLDS AFTER CORRECTION | The printed covariant-divergence equation is exactly horizontality of `z_l=xi_l u_l`. HV gives `C_h<=beta^2 c_E+beta`; HSS gives proxy `beta^2 c_E+2 beta`. Exponential entrywise decay is sufficient, stronger than the operator-norm bound. A box-free c_E alone does not deliver the seed: the other chain inputs and their quantitative rates, in particular a usable LSI-vac, remain required. |
| 7.1, lines 443–450, FR and pointwise Hessian identity | HOLDS | CEN sets the projected score to zero. Subtract the HV/TV expression from the conditional log-integral Hessian; both variance terms and the local cosine difference have exactly the printed signs. At `w=u` with central u, the factors u cancel and the frame density is `exp(beta sum Re(g_x g_y^*))`, the stated O(4) model. |
| 7.1, lines 451–454, conclusion about HS | HOLDS AFTER CORRECTION | For a divergence-free xi, the linear spin-wave term sums to zero by discrete summation by parts. This removes only that linear term. It does not bound the full finite-beta frame variance uniformly in volume. The claimed HS failure therefore remains an unproved mechanism, even before the GUIDE extrapolation. |
| 7.2, lines 456–462, pattern equivalence and odd score | HOLDS | For the SU(2) patterns in one common colour direction, choose a constant c with `Ad_c n=-n`. It fixes central u and maps one pattern to the other. In U(1) the xy plaquette phases are `pi +/-4 theta epsilon_p`; differing imaginary parts distinguish the gauge orbits when `sin(4 theta)!=0`. Joint conjugation gives `p(u*,w*)=p(u,w)`; differentiating at real u gives the odd projected score. No global inverse map on noncommuting SU(2) links is needed. |
| 7.2, lines 462–468, projected U(1) lower bound | HOLDS AFTER CORRECTION | Gauge inequivalence and oddness allow this mechanism; neither proves a nonzero frame factor or a volume-growing covariance. The claimed order and frame factor are still separate unproved inputs. |
| 7.3, lines 474–484, SG-step/SG2 and Proposition W substitution | HOLDS | `beta(Ebar-E Ebar)` is the projected score in body coordinates. It is horizontal pointwise; vertical components cancel by gauge invariance. Its covariance bound is exactly reverse Poincare. With the same conditional Poincare premise gamma_c, W becomes `\|grad Pf\|^2 <= (sigma_2^2/gamma_c) P\|grad f\|^2`. SG2 is only a necessary second-order condition for SG-step. |
| 7.3, lines 484–487, a violation needs a first-order tie | HOLDS AFTER CORRECTION | A tie is a candidate mechanism, not a necessary characterization. A diverging susceptibility at continuous criticality could also violate SG2; a failure of a uniform MGF bound need not first appear in its variance. CEN only excludes an SU(2) central slice **itself** for the projected score. |
| 7.4, lines 489–498, frame heat bath and limiting covariance | HOLDS AFTER CORRECTION | The outgoing and incoming terms give the printed quaternion heat-bath parameter. The limit is correct for stationary, exact slab samples and an ergodic frame chain. Its covariance is under the finite-slab first-layer law until T tends to infinity; the function Ebar itself is unchanged. The displayed finite-lag factorization in its proof is invalid; use the disintegration proof below. No finite lag is identified with the limit. |

For REC, write `A_t=ZF(w_t)`, `B_t=ZV(w_t)` and
`M_t=A_t-sum_(s=1)^t B_s`. Its increment is
`A_t-B_t-A_(t-1)`, with conditional mean zero by the first REC identity.
The conditional variance is `Var(Z(F-V)(w_t)|w_(t-1))`.
Martingale increments are orthogonal in L2. Summing the second REC identity
therefore gives exactly the printed iterated formula, with `Var(M_n)` and
the negative sum of `Hess V`. All functions are bounded on a fixed compact box.

For 7.4, disintegrate an equilibrium first-layer sample by its gauge orbit Q.
Let rho_Q be its conditional frame law and K_Q the frame heat-bath kernel.
The time-independent gauge move changes only the first temporal plaquettes,
so it preserves rho_Q. For a chosen electric component f, put
`m_Q=E_(rho_Q) f` and `f_0=f-m_Q`. Stationarity gives

`Cov(f(W_0),f(W_n)) = Var(m_Q) + E_Q <f_0,K_Q^n f_0>_(rho_Q)`.

At fixed finite box, full-support heat baths on compact groups have a
minorization after a complete sweep; thus the second term tends to zero.
The same argument applies componentwise to the covariance matrix. It does
not license replacing `E[f(W_0)f(W_n)|Q]` by the product of conditional
means before taking the limit. Starting the auxiliary gauge variable at 1
is valid because the sampled representative W_0 is already distributed
according to rho_Q. It is not a fresh equilibrium gauge draw for a fixed,
nonrandom representative. Slab equilibration is therefore an essential input.

The design has a useful exact control: at central SU(2) u, its limiting
projected covariance is zero, independent of how large its raw covariance is.
It follows that a large finite-lag covariance alone cannot refute SG2.

## 4. GUIDE model, arithmetic, and inference

**Evidence boundary.** The source names Mini files under `/tmp/gap-sc-950/`:
`slab_xy.py`, `slab_u1.py`, `slab_proj.py`, `slab_u1p.py`, and five batch logs.
None was found in this checkout by a hidden-file-inclusive filename search.
Those paths refer to the author's machine; no search of /tmp or another machine
was performed. Thus the heat-bath implementation, seeds, samples, error bars,
timestamps, lock use, and sampler checks are **not verified**. No simulation
was rerun. The verdicts below check the written model and the arithmetic of
the displayed values, not their production or statistical accuracy.

For an even periodic L, put `s(x)=(-1)^(x+y)` and
`epsilon_x=s`, `epsilon_y=-s`, `epsilon_z=0`. The pattern in 5.1 has
zero divergence: the outgoing-minus-incoming x contribution is 2s and the
y contribution is -2s. Its xy circulation is 4s; its xz and yz circulations
vanish. The stated background has xy holonomy -1 and the others +1.
Consequently the common-colour ansatz has one-step cost per site
`2 beta(1-cos theta)+beta(1+cos 4theta)`.
Its nonzero stationary angles obey `16 cos^3(theta)-8 cos(theta)-1=0`.
This supports the approximate angle 0.70 and sine 0.65 **for that ansatz**.
It does not solve a half-space minimization or estimate its thermal law.
The quoted twist stiffnesses require a precise rule assigning the varying
colour to each link, which is absent; the recalled Heisenberg critical value
and deconfinement extents are not verified or used as proof inputs.

The Fourier normalization also checks. If `E_i^a(x)=sine(theta) epsilon_i(x)n^a`
with a uniformly rotated unit n, the normalized tie-mode amplitude is
`X_a=sqrt(2L^3) sine(theta)n^a`. Thus its colour-averaged second moment is
`(2/3)L^3 sine^2(theta)`. The U(1) sign-mixture value is
`2L^3 sine^2(theta)`. These are model calculations, not proofs that either
sampled law has those configurations. At central SU(2) u, colour isotropy
makes the averaged colour block equal each one-colour block in exact
equilibrium. At real U(1) u, conjugation gives zero mean in exact equilibrium.

| Source computation | Verdict on the displayed arithmetic/model |
|---|---|
| 5.1–5.2, lines 138–181: pattern, power and code controls | HOLDS AFTER CORRECTION. The pattern and energy calculation above hold. The fully ordered size ratio is `216/64=27/8=3.375`. Quaternion errors, VMF mean errors and smoke-run values have no available raw evidence. Stiffness and recalled critical couplings remain heuristics. A growth ratio threshold can classify a GUIDE trend, not decide a uniform theorem. |
| 5.5, lines 349–370: code/power/hot-cold comparisons | HOLDS for arithmetic on reported values. Relative differences from row 944 are `0.0007/0.2991` (about 0.23%) and `0.0055/0.4503` (about 1.22%); both are below 3%. `38.65/11.91` is about 3.25. `0.03/2.55` is about 1.18%, below 15%. No independent-code or equilibration verdict follows without the files. |
| 5.5, lines 371–386: size ratios and Hessian sizes | HOLDS AFTER CORRECTION. `2.46/2.03` is about 1.21; `22.62/4.19` is about 5.40; `2.6^2·22.62=152.9112`. Also `2.3^2·2.5=13.225`, and subtracting the **reported** local term 1.2 gives 12.025. The local expectation producing 1.2 is not tabulated. Without it, HV only guarantees a directional Hessian at least `13.225-2.3=10.925` for that exact covariance. At beta 2.4 and lambda=8, the corresponding lower value is `46.08-2.4=43.68`. None is an upper bound on C_h or sigma over all slices; “sigma about 14” is not established. These remain finite-slab estimates. |
| 6.3 and 5.6, lines 337–347,388–409: U(1) | HOLDS AFTER CORRECTION. `331.6/41.3` is about 8.03, close to, not exactly, 8. `0.430/0.413` is about 1.04; `1.11/1.25=0.888`. The identity-slice values are near `1/beta=10/23`, not an exact compact-Wilson photon equality. With `m_st` as the printed unnormalized order parameter, `(L^3/2)m_st^2` gives 41.2232, about 139.619, and about 331.531 at L=4,6,8, consistent with the displayed second moments and small fluctuations of its absolute amplitude. This checks normalization, not a phase or half-space limit. |
| 5.7, lines 411–425: growth and thickness ratios | HOLDS for arithmetic. `7.57/8=0.94625`; `42.73/16.42` is about 2.60; `64.87/22.62` is about 2.87. Hot/cold difference `0.23/22.62` is about 1.02%; thickness difference `0.69/22.62` about 3.05%. These pass the written 15% comparisons of reported means. They give no error bound for T tending to infinity. |
| 5.7, lines 426–427: `0.024+0.16/L` fit within 3% at all five sizes | FAILS as printed. At L=6 this fit predicts `0.024·216+0.16·36=10.944`, versus 11.34 (about 3.49% low). At L=10 it predicts 40, versus 41.59 (about 3.82% low). Rounding may describe a different fit, but no other coefficients are supplied. The displayed normalized lambda values themselves are consistent with division by L cubed. |
| 5.7 predictions and 5.8, lines 438–441,518–541 | HOLDS AFTER CORRECTION. The printed beta-2.5 coefficients `0.010+0.18/L` predict 87.04 and 152, not exactly 86 and 150. The latter could reflect unreported fitted digits. `144/42.73` is about 3.37. At beta 2.45, `39.96/11.86` is about 3.37 and `39.96/24.89` about 1.61; its declared test is inconclusive. The L=20 quarter values average to 144.025; the last three average to 158.8, confirming the reported initial drift. Growth is not exact L cubed: at beta 2.5 the ratio from 12 to 20 is about 3.37 against the volume ratio `125/27`, about 4.63. The stated critical-like exponents are only descriptive fits over these sizes. |
| 7.5–7.6, lines 500–516,543–558: projected-mode size comparisons | HOLDS AFTER CORRECTION. The displayed radial X plateau ratio is `0.023/0.024=23/24`, below 1.3. The Y ratio is `0.183/0.133`, about 1.38, in the inconclusive band. These are **finite-lag averages**, not verified projected variances. No error analysis supports equality of constants across beta or a `1/tilt` law from two tilts. The largest printed radial plateau is 0.034, rounded to 0.03 in the summary. |
| 7.6, lines 559–565: validation V and stationarity | HOLDS for the reported validation failure. `0.64/2.63=64/263`, about 24.3%, exceeds 10%. The late tail ratio `0.64/1.12=4/7` over 32 sweeps corresponds to `32/log(7/4)`, about 57 sweeps. It is compatible with slow decay, not a mixing bound. Marginal variances staying near their initial values tests stationarity, not loss of autocorrelation. The claimed errors “about 3%” and “within noise” are unverified. |
| 7.6, lines 566–577: U(1) frame-lag criterion | HOLDS AFTER CORRECTION for the ratios; FAILS as a verified projected-covariance test. `139.8/140.0` is about 0.999; `139.8/19.7` about 7.10; using batch 2's 41.3 instead gives about 3.39. The source explicitly says its L=4 run was not in equilibrium; replacing it by a different run does not validate the advertised lag-64 comparison. Finite-lag persistence also does not establish the infinite-lag frame factor. |
| 7.6, lines 578–584: rounded cone explanation | HOLDS AFTER CORRECTION to a heuristic. The local cone interpretation and location of all possible failures are not proved. A horizontal bound at all slices cannot be inferred from a few radial and angular amplitudes. |

There are two distinct inference failures, independent of any sampler bug.

1. **A finite size sequence cannot refute existence of an unspecified
   box-free constant.** Any finite list of finite covariances has a finite
   maximum. For example, a sequence agreeing with every reported value up
   to L=20 and constant thereafter is consistent with those values and
   bounded. It is not proposed as a Wilson law; it exhibits the missing
   inference. A theorem establishing further growth, or an explicit fixed
   upper threshold contradicted by controlled measurements, is needed.
   Neither is supplied. Moreover the samples use finite T, whereas (2.3)
   first takes T to infinity at each B.
2. **A finite frame lag cannot certify the projected covariance.** The
   residual term in section 3 need not have decayed. In a two-state reversible
   example with eigenvalue `r=1-epsilon`, a centered observable has lag-n
   covariance `r^n Var(f)` but zero limiting covariance. For small epsilon,
   lags 16,32,64 look flat. This elementary example shows the logical problem
   with the test, not a replacement for the Wilson dynamics. The source's
   own central-SU(2) control demonstrates slow residual covariance where
   the correct projected limit is exactly zero.

Thus the phrases “no box-free constant on boxes up to 20,” “REFUTED at GUIDE
level,” a proved transition at beta 2.45–2.5, and “the upper window is closed”
**FAIL as conclusions** (lines 325–327,333–335,375–381,401–409,428–435,
470–473,531–541,569–571,609–613,618–629,645). The honest GUIDE conclusion is:
the author reports strong finite-slab growth at this boundary family and
large uncertainty about its continuation and frame projection. This
provides a reason to investigate the projected condition; it does not
refute SC, SC-hor, HS, SG2, or SG-step in the stated half-space models.

## 5. Disposition of the final result

The substantive corrections, ranked by what they affect, are these eight
groups. The tables above give a verdict for every asserted result and
fact-test; these are not additional scientific claims.

1. **Finite-size and finite-thickness inference.** Delete the claimed
   refutations, proved phase labels and instruction to drop SC for the upper
   window. The reported trends do not close that route.
2. **Frame projection and controls.** Correct 7.4's proof and distinguish the
   infinite-lag quantity from the reported lag averages. Validation V failed;
   the U(1) L=4 comparison also was not equilibrated. “All controls pass” in
   line 609 is false. “All controls but one pass” in line 645 does not cover
   the admitted U(1) defect. The tilted-slice plateaux remain GUIDE observations.
3. **Implication scope.** One Gaussian non-implication is established.
   Neither two-way independence from FC/LSI-vac nor the converse separations
   in 2.5 have been proved. A first-order tie is a possible mechanism, not a
   necessary condition for failure.
4. **Terminal law.** Change the replacement in 2.2 to `+V/2`, or explicitly
   change the terminal vector to `exp(-V)`. The first option matches the
   advertised half-weight simulation.
5. **Constants and domains.** Use the optimal Hessian constant in 3.1;
   normalize Omega; state the Gaussian kinetic self-term and the confining
   ground-state premise. Observed directional lower bounds are not upper
   bounds on the universal proxy. The rest of the seed hypotheses remain.
6. **Fact-test strength.** Reuse row 945's DW certificate. Keep AV's U(1)
   inequality, the SMALL-BOX growth estimate, and the full HS frame estimate
   unproved. SC is a linear susceptibility condition; general strong mixing
   is a sufficient stronger condition, not a proved equivalent.
7. **Numerical arithmetic.** The printed 3% fit fails at L=6 and L=10.
   Predictions from rounded coefficients, exact-volume language, inferred
   Hessian constants and finite-lag “projected” labels need the corrections
   in section 4. Raw computations and error estimates remain unverified.
8. **Small-beta counting.** A boundary link's 13 neighbours are not the
   bulk half-space Dobrushin count. No asserted threshold is proved.

Applied to section 8's result table: rows 597–608 inherit the mathematical
verdicts in sections 1–3 above. Rows 609–611 become author-reported finite-slab
GUIDE trends with the failed controls retained. Rows 612–613 do not establish
refutations. Rows 614–615 correctly retain open inputs, but the same OPEN
designation must include SC and SC-hor throughout beta 2.3–2.6. SG2 remains
only the variance-level part of SG-step, not its replacement for HC.

No source note, registry, tree, FINISH row, audit record, or remote state was
changed. Only this report was written. It grants no scientific status.

RESULT: HOLDS for the exact one-step law, UNROLL, TV, HG/SC-hor, SU(2) AV, REC, FR, reverse-LSI/reverse-Poincare equivalence, and the named conditional entropy implication; HOLDS AFTER CORRECTION for the terminal slab, constants, domains, fact-test scopes and frame-limit proof; FAILS for the printed 3% fit, claimed two-way independence as an established result, and finite-GUIDE refutations or route closure. SC, SC-hor, HS and projected SG-step for Wilson SU(2) throughout beta 2.3–2.6 remain OPEN; the GUIDE raw runs are unverified. Research-text check only; no status granted.
