# Uniform soft-minimizer curvature and residual kernels

Author proof unit for the **u-stripped tree phase** of the supplied SU(N) Wilson / normalized S4′ soft-kernel model. **FC19 follows from the existing linear package with `theta=L^-2`; consequently FC20 gives a depth-uniform neutral quartic jet of the stationary tree value `T_n`.** The new work is the exact identification of that earlier result with this consumer, the separate absolute weighted row and column estimates, and their application to the actual contour spreads. The uniform analytic data-kernel theorem and intermediate-curvature lemma are prior work, explicitly credited below. This unit is awaiting independent review; it supplies no audit verdict.

```yaml
actual_current_surface_status: exact-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Author proof of FC19 and the neutral FC20 consequence in the explicitly supplied model, using the actual previously proved linear data kernels."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

The full Yang–Mills existence and physical continuum mass-gap problem remains **OPEN**. Charged cubic-source exchange, a uniform nonlinear complex neighborhood, conditional fluctuation inverses, the nonlinear RG/sea estimates, continuum OS existence and reconstruction, and the physical Hamiltonian gap are not conclusions of this note.

## 1. Exact target and reusable source

Fix `d=4`, `N>=2`, odd `L>=3`, `0<kappa_-<=kappa_j<=kappa_+<infinity`, depth `n>=1`, and a periodic top torus of side `T>=3`. The requested constant-kappa case is included. The quadratic part at the trivial field of the normalized tree phase, with the overall factor `u=1/g^2` removed, is, for each real colour,

```
E(a_0,...,a_(n-1);v)
 = (1/2)||d_2 a_0||_count^2
   +(1/2) sum_(j<n) kappa_j ||a_(j+1)-Q_root,j a_j||_count^2,
a_n=v.                                                        (US1)
```

These are integrated link variables in each level's own unit lattice, and all adjoints use ordinary counting inner products. US1 is the quadratic part of the **u-stripped normalized tree phase** `F_tree=sum_p s(U_p)+sum_(j,c) kappa_j phi_(M_c(U_j))(U_(j+1),c)`, where `phi_M(V)=N^-1[max_W Re tr(W^-1 M)-Re tr(V^-1 M)]` and the maximum is over `SU(N)`. Its stationary value is the `T_n` used in FC18–FC20. The quadratic contour-spread term cancels in this phase. The exact finite-u negative logdensity also contains the field-dependent logarithm of a Haar integral, whose quadratic spread contribution is nonzero at finite u; US1 is not its full Hessian divided by u. FC18's fourth-order polar terms refer to `F_tree` and `T_n`.

Write `r_j=a_(j+1)-Q_root,j a_j`, `f_j=d_2 a_j`, and `F_j=L^(2(n-j)) f_j`. The older linear package uses the opposite residual sign and calls `F_j` its `f_j`. This sign changes no absolute norm. `z_(j,tau)=theta_tau(a_j)-average_tau theta_tau(a_j)` is the actual S4′ spread attached to a level-(j+1) link; `tau` includes the coordinate ordering and block point. Distances throughout this note are in **top-level lattice units**.

The target is [FC19–FC20](RESIDUAL_FULL_COLOUR_ASTRA.md). Their source SHA-256 is `1ce9460989e5491bd491dcc348add15207e63013a0c537cd6c51caa19f0e3dd7`. The [frozen full-colour review](REVIEW_RESIDUAL_FULL_COLOUR_ASTRA.md), SHA-256 `0b504129260e0269ae8dffa79f2113a6bb94675edc37c084fe8f9be6464e67bc`, confirms FC18 and FC20 as an implication but leaves FC19 open in that reviewed unit. This note supplies the missing producer; it does not edit that frozen review or silently change its disposition.

The necessary prior result is [LINEAR_PACKAGE](LINEAR_PACKAGE.md), §§1.1–1.5, 2.4–2.5, 3.1, 3.4–3.8, 4.1–4.3 and 6.7. Its complete arguments were read in [PROOF_session16_snapshot](PROOF_session16_snapshot.md): the stationary/dual/symbol arguments at lines 2380–2505, the uniform strip proof at 2649–2798, the sharper strip at 3113–3168, and intermediate curvature at 3230–3239. The relevant repairs and their confirmation were read in [REVIEW_S13_S14](REVIEW_S13_S14.md), §§N2-exp and N2-exp′; [REVIEW_S15_CONVERGENCE](REVIEW_S15_CONVERGENCE.md), §§R1314 fixes and Lemma KF; and [REVIEW_S16_S17](REVIEW_S16_S17.md), §§R15 fixes and linear-package assessment. In particular the missing fine-curvature strip condition, invalid rounded rate pairs and periodic-boundary gluing were corrected in the consumed snapshot. Review labels are not used in place of these proofs.

This is a reuse and consumer bridge, not a new uniform-strip theorem or a literature-priority claim. A narrow current-main statement search at coordinator-fetched `ca2bc7ddf64790da96cd43d42017d000fbfe4808` returned no matching landed lane paths; the matching branch originals above take precedence over that absence. Their hashes and exact read ranges are bound in the input manifest. The coordinator owns git, PR, shared summaries, lock and audit operations; this worker edits only this note and `checks/uniform_soft_minimizer_*`.

## 2. Actual root map, counting norms and zero modes

The previously established identity is

```
Q_root = Q_str - d_c alpha,
Q_str a(X,mu) = L^-4 sum_(y in B_X) sum_(t=0)^(L-1) a_mu(y+t e_mu),
alpha(d lambda) = blockavg(lambda)-ev(lambda),
Q_root d = d_c ev.                                            (US2)
```

Credit: LINEAR_PACKAGE §1.2 and [FLOW §89, RFL11-fix S11-7](FLOW.md), with the explicit composite proof in FLOW §98. We do not claim rediscovery. Centering blocks at their roots is a coordinate translation of the supplied centered-block convention.

Let `CoCl_0` denote co-closed top one-forms orthogonal to all four constant one-forms. Its orthogonal complement is the closed space, including both exact and harmonic forms. Differentiate US1 along fine gradients, then apply the intermediate Euler equations. Surjectivity of root evaluation gives successively

```
d* r_j=0,
kappa_(j-1) r_(j-1)=kappa_j Q_root,j* r_j,
d_2* d_2 a_0=kappa_0 Q_root,0* r_0.                           (US3)
```

Since `Q_root*=Q_str*-alpha* d*`, the funnel term vanishes on these residuals. Taking inner products of the bottom equation with constant links, and using `Q_str^(r)(constant)=r(constant)`, also proves that every residual has zero mean. Direct straight averages compose exactly. Thus, with `s=n-j-1`,

```
r_j=(kappa_(n-1)/kappa_j) (Q_str^(L^s))* r_(n-1).               (US4)
```

This is LINEAR_PACKAGE Lemmas 2.4 and 3.1 with the sign dictionary above. For block side `r`, its nonnegative averaging matrix has exactly

```
row_sum(Q_str^(r))=r,     column_sum(Q_str^(r))=r^-3.           (US5)
```

Hence its adjoint contracts the sup norm by `r^-3`, with counting adjoints, not by `r^-1`. The distinction is a factor `r^2` in d=4. Our direct path and sparse-chain checks independently test it.

All gauge and harmonic kernels are kept in this argument. On a periodic lattice, the inverse of the fine scalar/Hodge Laplacian used below is its inverse off the constant space and zero on that space. Gauge ambiguity in `a_j` does not affect `r_j`, `f_j` or the closed contour spreads. If the top datum is a constant one-form, `a_j=L^(j-n)v` is a zero-energy lift and every one of those outputs vanishes. Fine gauge kernels with zero top-root evaluation remain minimizer directions; no nonexistent inverse on them is introduced. Harmonic Gram factors in determinant identities are unchanged by this linear data argument. It neither drops nor reassigns the two graph Gram factors in FC7–FC9.

For completeness, there is an exact hard/soft comparison on `CoCl_0`. Let `P_n` project onto that space, `Q^(r)=Q_str^(r)`, `ell=L^n`, and

```
B_n=P_n Q^(ell) Delta_f^-1 Q^(ell)* P_n,
C_n=P_n [sum_(j=0)^(n-1) kappa_j^-1
                  Q^(L^(n-j-1)) Q^(L^(n-j-1))*] P_n.
H_soft=(B_n+C_n)^-1,             H_hard=B_n^-1,                 (US6)
```

where inverses in US6 are only on `CoCl_0`. This follows directly from the exact dual minimum; equivalently it is the covariance of independent soft noises accumulated over all levels. Moreover

```
0<C_n<= [kappa_-^-1/(1-L^-2)] I,
H_soft=H_hard^(1/2)
       [I+H_hard^(1/2) C_n H_hard^(1/2)]^-1 H_hard^(1/2).      (US7)
```

The bound uses both sums in US5, so every level contributes `L^-2s` and the entire accumulation is included. It is an operator comparison, not by itself an exponential-kernel estimate. The actual locality proof is the next section. Applying this bounded covariance claim to the unprojected root-map covariance would be false: its longitudinal part can grow with depth, as FLOW's LONG-n result already records.

## 3. Why the old data-kernel theorem is genuinely uniform

Here is the load-bearing analytic mechanism of N2-exp, included to expose its hypotheses and avoid importing a headline. Let `ell=L^n`, `kappa=kappa_(n-1)`, and define the entire scalar factors

```
D_ell(w)=ell^-1 sum_(t=0)^(ell-1) exp(-i w t/ell),
delta_alpha=D_ell(z_alpha) Dbar_ell(z_alpha),
phi_alpha=2 ell^2[1-cos(z_alpha/ell)],   phi=sum_alpha phi_alpha,
Delta_alpha=2[1-cos z_alpha],          a=kappa product_alpha delta_alpha.
```

`Dbar` denotes the analytic continuation of the real conjugate, not complex conjugation at complex z. The exact Fejer identity is `Delta_alpha=phi_alpha delta_alpha`. In the unconstrained diagonal dual matrix, the zero alias has coefficient `a delta_mu/phi`; the other aliases and all intermediate soft noises are `R_mu`. Thus

```
Pdual_mu=beta_mu/phi,        beta_mu=a delta_mu+phi R_mu,
Psi=1-sum_mu phi_mu R_mu/beta_mu,
Sigma=sum_mu Delta_mu/beta_mu,
a Sigma=phi Psi.                                            (US8)
```

The soft-noise part of `R_mu` is a sum with coefficients at most `kappa_hat L^-2s`; the nonzero-alias part is nonnegative and at most `kappa/9` on the real cube. Consequently

```
1<=R_mu<=Rbar=1+kappa_hat/(L^2-1)+kappa/9,
beta_mu>=b_*=min(kappa,24/pi^2)>0.                            (US9)
```

The transverse residual symbol has two equal formulas, proportional respectively to

```
+a nubar_nu/(beta_mu beta_nu Psi),
+phi nubar_nu/(beta_mu beta_nu Sigma).                        (US10)
```

Use the first near zero and the second away from zero. On a fixed ball `|Re z|<=r0<sqrt(6)`, the real-axis lower bound is

`Psi>=kappa(1-r0^2/6)/(kappa+r0^2 Rbar)>0`.

Outside that ball, `Re Sigma` has a positive lower bound relative to `sum Delta_mu/min beta_mu`. EXP-strip bounds the perturbation of every displayed quantity when `|Im z_alpha|<=eta`, uniformly in ell. Its nonzero-alias denominators obey

`|phi^(K)(z)| >= (1-4 eta^2 cosh(eta)^2/9) phi^(K)(Re z)`,

with `phi^(K)(Re z)>=9` for `K!=0`, after taking the stated representatives. Thus alias poles do not approach this strip as n grows. The retained zero alias is removed algebraically in the curvature symbol: insert US10 into `d Delta_f^-1 Q* r`; its potentially singular bracket is divisible by phi, using `nu_mu D_mu/delta_mu=nu_mu^(ell)` and antisymmetry of the curl. This is the full EXP-id cancellation, not the replacement of `phi` by a continuum `|p|^2`.

The remaining curvature alias majorant is, up to a uniform constant,

`product_alpha (1+|p_alpha+2pi K_alpha|)^-1
 * (1+|p_sigma+2pi K_sigma|)^-1 * (1+|p+2pi K|)^-1`.

It is summable uniformly over the aliases. The extra sigma factor is essential. Summing the other three coordinates by dyadic shells reduces to a convergent series bounded by `sum_(t>=1) t^-2(1+log t)^2`; the complex factors cost only `exp(C eta)`, including the fine-offset phase. Hence the bound is uniform over every fine offset.

The sufficient strip inequalities are strict at eta=0: the beta relative error and Psi perturbation vanish, the away-from-zero Sigma bound has a factor-two margin, and the fine-curvature condition vanishes. Choose one fixed r0 in `(0,sqrt(6))`. Continuity, compactness of `[kappa_-,kappa_+]`, and the depth-independent displayed bounds give a **positive eta independent of n,T**. This existence argument needs no fitted or numerically located singularity. Our separate arithmetic check uses the conservative pair `(eta,r0)=(0.005,0.57)` at `L=3,kappa=1`, including the repaired fine-curvature condition.

Finally the full alias expressions are periodic meromorphic functions: shifting p by `2pi` permutes the alias residues, and the offset phase is periodic in the alias index. The locally bounded formulas above remove their singularities on overlapping translated cubes. This is the repaired periodic gluing argument. Shifting the Fourier integration contours yields, for any smaller positive rate eta, infinite-lattice data kernels

```
|K_(r_top)(X,y)|<=M exp(-eta |X-y|_1),
|K_(F_0)(ell X+u,y)|<=M exp(-eta |X-y|_1),                    (US11)
```

uniformly in n and u. Finite-torus kernels are periodizations, not isolated geodesic exponentials with their images discarded. The datum here is the top **one-form v**, exactly the datum in FC19. An unrestricted Coulomb representative acting on all two-forms can have a power tail; no such representative is used.

Intermediate curvatures already obey Lemma KF. To check its scaling directly, let `A_(i->j)` be the normalized curvature averages, with nonnegative coefficients and row sum one. Curling the actual stationary chain gives

```
F_j=A_(0->j) F_0
       +sum_(i<j) A_(i+1->j) [L^(2(n-i-1)) d_2 r_i].          (US12)
```

The plus sign follows our residual convention. US4 makes the bracket's kernel bounded by a constant times `L^-(n-i-1)`. Each derivative has four boundary links, and all averaged supports stay within a fixed distance in top units. The sum is at most `sum_(s>=0)L^-s<=3/2`. This proves the intermediate bound from US11 with a depth-independent constant. Equivalently it is the previously proved Lemma KF, whose full geometric sum and offsets are preserved in the frozen snapshot. Thus, with constants depending only on `L,kappa_±,eta`,

```
|K_(r_j)(x,y)| <= C_r L^-3s E_(eta,T)(x,y),  s=n-j-1,
|K_(f_j)(x,y)| <= C_f L^-2(n-j) E_(eta,T)(x,y),
E_(eta,T)(x,y)=sum_(v in Z^4) exp[-eta |x-y+Tv|_1].            (US13)
```

Converting the coarse-cell offset in US11 to the true position x costs only a fixed exponential factor, absorbed in `C_f`.

## 4. Actual contour spreads and both weighted norms

Every S4′ contour has the same endpoints and winding. A contour minus the direct root-to-root straight path is an integer plaquette boundary in a fixed nearby box. This can be seen constructively by exchanging adjacent steps in different coordinate directions, each exchange contributing one plaquette, and canceling adjacent inverse steps after collecting directions. Its length is at most `L+4(L-1)<5L`; fewer than `25L^2` exchanges suffice. All intermediate vertices lie within a box of radius depending only on L. Subtracting the average of these identities proves a local Stokes representation

```
z_(j,tau)(x)=sum_p c_(tau,x,p) f_j(p),
sum_p |c_(tau,x,p)|<=B_L,    dist_n(p,x)<=R_L L^-(n-j),        (US14)
```

with for example an enlarged constant `B_L=50L^2`. It is valid on the torus by lifting the entire fixed contour first; common winding cancels. It involves actual path coefficients, not an assumed form factor. US13 then gives

`|K_(z_j,tau)(x,y)|<=C_z L^-2s E_(eta,T)(x,y)`, `s=n-j-1`.

The fixed factor `L^-2` from `n-j=s+1` and the Stokes multiplicity are absorbed into `C_z`. Colors only give fixed finite multiplicities at the trivial field.

Here is the separate row/column calculation. Fix `0<m<eta` and put

`S(a)=coth(a/2)^4`, `a=eta-m>0`.

For any real x in top units,

`sum_(y in Z^4) exp(-a|x-y|_1)<=S(a)`.

In one dimension the sum on a unit interval is convex and is maximal at an endpoint; four products prove the formula. If outputs lie on the mesh `r^-1 Z^4`, their column sum instead is

```
sum_(x in r^-1 Z^4) exp(-a|x-y|_1)
 =coth(a/(2r))^4 <=r^4 S(a),  y in Z^4.                      (US15)
```

The inequality follows from monotonicity of `t coth t`. For a torus, summing y and the images in `E_(eta,T)` unfolds exactly into these lattice sums; also `d_T(x,y)<=|x-y+Tv|_1`. Thus no T-dependent image factor is introduced. Orientation, color and contour multiplicities are fixed constants. Apply US15 with `r=L^s` to the residual and spread outputs. Apply it with `r=L^n` to the finest plaquettes. There is a constant A, independent of `n,j,T`, such that for **each actual kernel** required by FC19,

```
sup_x sum_y |R_j(x,y)| exp[m d_T(x,y)] <= A L^-2s,
sup_y sum_x |R_j(x,y)| exp[m d_T(x,y)] <= A L^(4s) L^-2s.      (US16)
```

For `f_0`, take `s=n`. For `r_j` and each spread `z_(j,tau)`, take `s=n-j-1`. The stronger residual amplitude `L^-3s` was only weakened to `L^-2s`. If all contour labels are included in one output index, their `24L^4` multiplicity merely enlarges A. The column bound is not inferred by transposing a row estimate: US15 explicitly counts its different lattice density.

This proves **FC19 with `theta=L^-2<1/L`** in the actual d=4 normalized soft chain. It is a theorem for the linear stationary responses at the trivial field. The proof of uniformity is US8–US15 and the consumed original arguments, not the finite tests.

## 5. Consequence for the actual neutral quartic

FC18 is the complete neutral stationary quartic of the normalized action, including the nonzero Wilson quartic and all polar variance/residual terms. It has no cubic-source exchange only when all four external directions are in the Cartan space; the corresponding cubic source with two commuting inputs vanishes in every possible internal color.

Polarize each of its degree-four products. Anchor one external datum and apply US16's column bound to its leg and the row bounds to the other three. For interaction location x,

`diam(y_1,...,y_4)<=sum_i d_T(x,y_i)`.

Each level therefore costs at most `C A^4 L^(4s)L^-8s`. The Wilson term has `s=n`; the soft terms use `s=0,...,n-1`. Hence

```
|||D^4 T_n(1)|_Cartan|||_m
 <= C(N,L,kappa_±,m) A^4 sum_(s=0)^n L^-4s
 <= C A^4/(1-L^-4),                                          (US17)
```

uniformly in n and T. This is FC20 with its actual producer supplied. No cancellation of individual nonzero quartic terms was assumed. In particular the fine Wilson neutral finite coefficient `-(N-1)/4` remains nonzero; the separate fixed-depth full-colour residual cancellation has the prescribed volume-first then external-momentum order. US17 does not interchange those limits.

A bound for the complete full-colour finite-part increment still requires the charged cubic/quartic data and its exchange terms. The neutral one-loop finite-part consumer can now be checked separately against US17 and the uniform quadratic ellipticity; that additional coefficient extraction is not asserted here.

## 6. Original-literature comparison for each key block

The two external sources have import class **non-derivation analogy**. They are primary-source comparisons, not adopted substitutes for the model-specific proof. Each is used to check geometry and hypotheses; neither provides derivation closure for FC19 or FC20. Full PDFs and extracted text remain only under `/tmp/uniform_soft_minimizer_primary/`; versions, exact hashes, successful TLS retrieval and the preserved initial CA-bundle failure are in the [source records](checks/uniform_soft_minimizer_primary_sources02.json) and [first attempt](checks/uniform_soft_minimizer_primary_sources.json).

| Block | Original source read | Exact dictionary and use |
|---|---|---|
| Gauge projection and the constrained/soft Schur comparison, US2–US7 | Dimock, [Covariant Axial Gauge, arXiv:1410.2798v3](https://arxiv.org/abs/1410.2798v3), Prop.5/Eqs.(75)–(84), Prop.6/Eqs.(86)–(99), and Prop.7/Eqs.(110)–(140); PDF pp.12–20, with p.21 for the companion resolvent | Abelian hard averaging, projection onto `Delta ker Q`, axial constraint `tau A=0`; the fluctuation lower bound assumes `QA=0`. Our US6 compares operators on co-closed mean-zero fields and includes every finite-kappa noise. The paper's constrained covariance is not silently identified with our soft-chain inverse. |
| Data-kernel locality, scale factors, row/column densities, US8–US16 | Dimock, [Multiscale block averaging for QED in d=3, arXiv:1712.10029v3](https://arxiv.org/abs/1712.10029v3), Eqs.(189)–(204), (284)–(303); PDF pp.26–27 and 38–40 | Hard multiscale averages on nested regions, weighted integration measures and sufficiently large M. Its kernel convention explicitly includes the source-cell volume. Its printed d=3 `L^-4` is `L^-3` volume average times `L^-1` edge-length conversion; our d=4 `L^-4` is volume average only. US5/US15 use counting norms directly. |
| Curvature control and local Stokes step, US12–US14 | The same original sources: axial-gauge Eqs.(89)–(94), and multiscale Lemmas16–17/Theorem1, Eqs.(316)–(376); PDF pp.41–49 | Theorem1 assumes a restricted minimizing orbit, earlier axial data, nested regions, `p_(j')/p_j<=L^|j-j'|`, and large M; it supplies a local gauge representative in d=3. Its entire theorem proof through p.49 was read. Our exact trivial-field soft data theorem and local integer Stokes filling need no import of those different hypotheses. |
| Uniform neutral quartic, US17 | Actual normalized action and FC18 in the frozen full-colour source, with its independent review | This model-specific fourth derivative is obtained from the supplied normalized density, not from a generic hard-constraint theorem. The external papers above concern Gaussian minimizers/covariances and do not supply its polar coefficients or delete its neutral finite term. The anchored four-leg estimate is proved explicitly in §5. |

The external sources are useful for checking geometry, conventions and possible later constrained-covariance work. The sufficient uniform data estimate used here is the existing **actual d=4 soft** theorem, with its complete local proof checked. No d=3 theorem, physical gap, empirical value, new axiom or new framework primitive is adopted. The current axiom memo, primitive procedure and registry were read at the immutable methodology revision; none grants the separately supplied Wilson dynamics or the requested continuum conclusion.

## 7. Independent implementation evidence and preserved limits

The [criteria](checks/uniform_soft_minimizer_01_criteria.md) preceded the new [implementation](checks/uniform_soft_minimizer_01.py). It imports no predecessor or reviewer helpers. It constructs all `4*24*3^4=7776` directed S4′ contours from individual coordinate steps, with the same ordering at both endpoints. A separate direct straight matrix and a Fourier diagonal Laplacian inverse give the independent dual prediction. Sparse least squares solves the actual root-contour chain without inverting its gauge kernel. It compares curvature/residual observables, so the solver's representative is immaterial.

| Invocation | Preserved output | Result and scope |
|---|---|---|
| `--mode bloch` | [stdout](checks/uniform_soft_minimizer_01_bloch_out.json), [stderr](checks/uniform_soft_minimizer_01_bloch_err.txt) | 81/81 predicates; depths 1 and 2, generic nonzero Bloch momenta, constant and nonconstant positive kappas. Actual root and straight minima agree; the separate FFT/dual formula and every tested residual transport agree. Harmonic lifts and counting factors are tested separately at zero momentum. |
| `--mode periodic` | [stdout](checks/uniform_soft_minimizer_01_periodic_out.json), [stderr](checks/uniform_soft_minimizer_01_periodic_err.txt) | 62/62 predicates; complete top `3^4`, fine `9^4` torus, all four datum impulses. Weighted row and column sums are computed separately. For coarse-scaled fine curvature at `m=.003`, the largest row is about 1.132 while the columns are about 113.859, illustrating why their densities cannot be identified. |
| `--mode strip` | [stdout](checks/uniform_soft_minimizer_01_strip_out.json), [stderr](checks/uniform_soft_minimizer_01_strip_err.txt) | 64/64 predicates; fresh implementation of EXP-strip's sufficient inequalities verifies a conservative rate, rejects an over-wide strip, and checks the geometric fourth-order scale sum and its uncurled mutation. |

The first 56 path predicates repeat in each invocation; these are **not 207 independent controls**. Each of these three invocations ran once with empty stderr and exit zero. The numerical minimizer comparisons have tolerance `2e-8`; the observed stationary errors are much smaller, and solver iteration/termination data are preserved. Tests reject a missing endpoint path, the wrong d=3 length factor, the wrong counting-adjoint scaling, omission of output-cell density, an excessive strip, and the uncurled `L^-s` quartic summation. A rejected sufficient strip is not proof of a singularity there.

The separate [second criteria](checks/uniform_soft_minimizer_02_criteria.md) and [integer filling program](checks/uniform_soft_minimizer_02.py) strengthen the actual Stokes check. Its [output](checks/uniform_soft_minimizer_02_out.json) has 53/53 predicates and [empty stderr](checks/uniform_soft_minimizer_02_err.txt). It checks all 7,776 contour boundaries and all 7,776 mean-subtracted spread boundaries by exact integer arithmetic. The largest constructed individual surface has coefficient norm 19; the largest spread norm is about 24.05, within the stated general bounds. Deleting a plaquette fails the boundary equation. It also rejects the omitted-density bound on the actual saved periodic kernel: 113.859 exceeds 67.616. Selection of that particular successful output for the extra mutation occurred after seeing it, and is disclosed in the second criteria. The first code and outputs were preserved unchanged.

The arithmetic tests are floating-point checks, not interval certificates; the integer boundary checks just described are exact. Their positive depth-uniform rate is justified analytically in §3. The finite-depth solves do not establish any unbounded-depth statement. The initial system-CA download failure is preserved; using a verified certifi CA bundle succeeded. No failed scientific predicate was erased or threshold relaxed.

The [input manifest](checks/uniform_soft_minimizer_inputs.json) binds source bytes and read ranges. The [receipt](checks/uniform_soft_minimizer_receipt.json) binds this note, criteria, code, outputs and retrieval metadata. It is an author handoff, not independent review or audit authority. Any changed consumed mathematical source requires affected rechecking. The next independent review should concentrate on the US1 sign/scale dictionary, inherited uniform strip and aliases, periodized column counting, actual Stokes spread, and the neutral-only boundary of US17.
