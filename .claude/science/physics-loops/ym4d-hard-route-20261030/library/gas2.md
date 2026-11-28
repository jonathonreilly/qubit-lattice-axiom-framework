# Kill test of (GAS2): the cut, the chain rule, and the density of old exits
Provenance: OpenAI/Codex (GPT-6 family; exact serving model and runtime effort setting are not exposed), commit `00f9df685ab3ecdea6d6079ade58e18e5ed0af9f`; a different provider from the Anthropic/claude-opus-5-5/max author of `explicit-region-two-step.md`; mapped-side research text, not an audit, granting no status.

## 1. Contract and source discipline

**Discharged (scope).** This is the requested kill test of Section 7, item 1, of `explicit-region-two-step.md`, with Sections 3–4 as its contract. Only this file is written. Source inspection and text editing are the only computer use. No mathematical conclusion rests on a run. The prescribed independence rules were read before the science sources; the independent attempt and excluded library/gate files were not read.

**Discharged (labels).** *Discharged* means a written argument here within its stated finite-dimensional domain, not retained status. *Implication* names the additional premises. *Gap* means an unproved necessary step. *Unchecked* includes expectations and source assertions not independently proved here. Memory is identified explicitly when used for motivation; no recalled theorem supplies a proof.

**Unchecked (target, not premise).** (GAS2) asks for the marginal effect of absorbed exits to have quadratic vanishing and constants summable through every subsequent block integration. Gauge invariance at the identity, smoothness across a chart seam, vanishing of a derivative at a nonzero cut surface, and a uniform bound on a second derivative are four different assertions. They will not be substituted for one another.

**Discharged (current checkpoint).** The pinned source defines a smooth mixture over rough-cell labels, with Haar output on dropped parents (mapped Text 5.2). Its chart cut is a separate partition of unity (Text 5.1). The proposed two-step state in `explicit-region-two-step.md` instead writes a box integral and uses deterministic-fibre notation. The calculation below must retain labels, Haar outputs, the fibre measure, and both parts of the chart split before deciding whether any boundary term survives.

## 2. The actual density, before differentiating

**Discharged (kernel identity).** Use normalized Haar measure throughout. For a label pattern `ell`, write `S_ell` for its retained parent bonds and `H_ell` for its Haar parent bonds. The source's current kernel, not the superseded deterministic extension in Text 5, is

```
p_ell(U) = product_c chi(f_c(U))^ell_c (1-chi(f_c(U)))^(1-ell_c),
K(U,dV) = sum_ell p_ell(U)
          product_(b in S_ell) delta_H(M_ell(U)_b V_b^-1)
          product_b dV_b,
rho_(k+1)(V) = sum_ell integral rho_k(U) p_ell(U)
                       product_(b in S_ell) delta_H(M_ell(U)_b V_b^-1) dU.   (2.1)
```

A Haar bond contributes the density `1`, not a delta constraint or a designated-bond Jacobian. `M_ell` is the surviving-line log-average, with the source's hull and dropping rules. The sum has finitely many patterns on a finite lattice. Formula (2.1) defines a measure even where a density or its derivatives have not yet been justified. Thus a deterministic equation `M U=V` does not describe all its summands.

**Gap (how explicit the supplied map is).** Mapped Text 3.1 specifies the linearized all-lines map, including the contour-gradient term. Texts 5.1–5.2 specify designated-bond elimination and the labelled surviving-line construction. They do not supply a particular smooth profile `chi`, a complete nonlinear formula for every pruned constraint in those coordinates, or its determinant at a changing chart. The profile is a family of choices. No numerical value for `L,a_*,x_*`, the rare-event constant, or the tree constant is fixed. The formulas below retain these quantities; substituting a linear average or a chosen toy cutoff for them would not be a calculation for the actual nonlinear kernel. The additional allowed map notes read below do not furnish those missing determinant bounds.

**Discharged (tree gauge and Haar factors).** On a finite rooted tree, eliminate one leaf gauge variable at a time. Multiplication of the incident bond by that variable preserves Haar measure; its integral is one. Induction removes all non-root tree variables with no determinant. Each remaining SU(2) link can locally be written `exp(i q.sigma)`, where the Pauli matrices satisfy `(n.sigma)^2=1` for a unit vector `n`. Its normalized Haar density relative to `d^3q` is

```
h(q) = (1/(2 pi^2)) (sin r/r)^2,       r=|q|<pi,
D log h(q)[a] = 2(cot r-1/r) (q.a)/r.                         (2.2)
```

Proof: `exp(i r n.sigma)=(cos r, sin r n)` parametrizes the unit three-sphere. Its induced metric is `dr^2+sin^2 r dOmega^2`; its volume is `4 pi integral_0^pi sin^2 r dr=2 pi^2`. Dividing by the Cartesian radial volume `r^2 dr dOmega` gives (2.2). The value and derivative at zero are obtained by the power series of sine. This is a written calculation, not an imported measure formula.

**Implication (the chart density on a regular branch).** Take independent logarithms `(xi,y)` of the non-tree bonds, with `y` the designated ones. Write `m_ell(xi,y)` for the logarithms of the retained parent outputs and `v` for their prescribed logarithms. Suppose `A_ell:=D_y m_ell` is invertible and `y=y_ell(v,xi)` on the branch. Ordinary substitution in the delta integral gives

```
w_(k,ell)(v,xi) = exp(-F_k(Phi_ell(v,xi))) p_ell(Phi_ell(v,xi)) J_ell(v,xi),
J_ell = product_(non-tree e) h(q_e)
        / [ product_(b in S_ell) h(v_b) |det A_ell| ].            (2.3)
```

Here `q=(xi,y_ell)`. A further change from these coordinates to the source's translated fluctuation coordinates multiplies (2.3) by that change's determinant. It cannot be omitted. To check the denominator: integrate the parent delta against `h(v)dv`; the substitution `m_ell(xi,y)=v` produces `|det A_ell|^-1`. This proves (2.3) locally. Covering all contributing fibres by such regular branches with controlled transitions is an additional premise, not a consequence of writing (2.3).

**Discharged (what a hard cut differentiates).** On such a branch, the box version is `B(v)=integral_K w(v,xi)d xi`, with `K` independent of `v`. Its parent variation is the integral of `D_v w`; there is no derivative of `1_K`. For a moving description `K(t)={f(t,xi)<0}`, direct differentiation of the normal thickness gives

```
d/dt integral_(K(t)) w_t
 = integral_K dot w - integral_(f=0) w dot f/|grad_xi f| dS.    (2.4)
```

The complement has the opposite boundary term. Their sum cancels it exactly when they partition the same weighted integral. A smooth chart cutoff has the same algebra: `D(chi^a w)+D((1-chi^a)w)=Dw`. The source's smooth convex barrier is not itself the indicator box of the two-step note; neither version authorizes discarding the complement.

## 3. An exact first-order hard-cut term, and why it is not yet a refutation

**Discharged (SU(2) overlap test).** Let `B_R={U:angle(U)<R}`, `0<R<pi/2`, and `g_t=exp(i t sigma_3)`. Define

```
C_R(t)=integral 1_(B_R)(U) 1_(B_R)(g_t^-1 U) dU.
```

For `U=cos r+i sin r n.sigma`,

```
cos angle(g_t^-1 U)=cos t cos r+sin t sin r n_3.
```

At `r=R`, the moving radial boundary is `R+t n_3+O(t^2)`, uniformly in `n`. For `t>0` its intersection with `r<R` loses a shell of thickness `-t n_3` on `n_3<0`. Since `integral_(n_3<0)(-n_3)dOmega=pi`, (2.2) gives

```
C_R(t) = (R-sin(2R)/2)/pi - (sin^2 R/(2 pi)) |t| + O(t^2).    (3.1)
```

The constant follows by integrating `sin^2 r`; the same shell computation for `t<0` gives the absolute value. This proves a nonzero first-order term with its exact coefficient. The function is invariant under conjugation. Thus gauge invariance alone does not rule out a linear distance term: differentiability is essential.

**Discharged (the cancellation test).** The complementary integral with `1_(B_R^c)(g_t^-1 U)` equals `vol(B_R)-C_R(t)` and has precisely the opposite coefficient. Their sum is constant for every `t`. This is the simplest explicit way a first-order cut term can be present in one positive contribution but absent from the density. Equation (3.1) is an attack on retaining overlapping sharp indicators. It is **not** a counterexample for the prescribed surviving-line map: no identification of its two balls with that map's successive free-coordinate domains has been proved. The integrate-first construction must be tested after the first cut has been integrated and its complement included.

**Discharged (nonzero ordinary derivative at a nonzero cut is also insufficient).** As a second diagnostic, hold all links but one at the identity in a four-dimensional Wilson lattice. The six incident plaquettes give the unnormalized density in Cartesian logarithmic coordinates

```
w_x(r) = (1/(2 pi^2))(sin r/r)^2 exp[-6x(1-cos r)],
w_x'(R)/w_x(R) = -6x sin R+2cot R-2/R < 0.                    (3.2)
```

The inequality follows from `sin R-R cos R>0`, whose derivative is `R sin R>0`. This includes the chart Haar factor. It is a conditional link density, not the density on a block fibre; restoring a block constraint introduces the designated variables and determinant in (2.3). It therefore supplies no actual-map counterexample. In particular, a nonzero derivative at `R>0` is compatible with quadratic vanishing at zero.

## 4. Level 1: the exact chain rule, including the gas from level 0

**Discharged (indexing and absorption).** Write `rho_1=B_1+E_1`, where `B_1` is the empty-label/chart-cut contribution and `E_1` is its complete positive complement. Extend the good contribution by zero wherever its defining chart is absent, assigning everything else to `E_1`. With `P_1` the actual kernel (2.1) at the next step,

```
rho_2(W)=P_1 B_1(W)+P_1 E_1(W),
Z_B(W)=P_1 B_1(W),       Z_E(W)=P_1 E_1(W),
q_2(W)=Z_E(W)/Z_B(W),    G_2^old(W)=log(1+q_2(W)).             (4.1)
```

The reference `Z_B` still includes new labels at level 1; it is not the all-good base at level 2. Equation (4.1) isolates the effect of the level-0 complement exactly wherever `Z_B>0`. Every chart contribution is the integral of `[B_1(Phi_ell)+E_1(Phi_ell)]p_ell J_ell`. No positivity of `B_1` on all intermediate fields is assumed: non-class intermediate fields and their live-hole data remain in `Z_E`. This is essential when absorbing a hole only after its parent is class.

**Implication (first variation on a regular fixed domain).** Let `W=W(t)` and let `a=partial_t Phi_ell`, `a_2=partial_t^2 Phi_ell`. A dot includes the dependence of the designated variables. For either `i=B,E`, the unnormalized weight is `w_i=i_1(Phi_ell)p_ell J_ell`; let `mu_i` be its normalized law over charts and labels. Where its logarithm is defined,

```
s_i = D log i_1(Phi_ell)[a] + D log p_ell(Phi_ell)[a]
    + sum_e D log h(q_e)[dot q_e]
    - sum_(b in S_ell) D log h(v_b)[dot v_b]
    - tr(A_ell^-1 dot A_ell),
Delta s = mu_E(s_E)-mu_B(s_B),
dot q_2 = q_2 Delta s,
dot G_2^old = [q_2/(1+q_2)] Delta s.                          (4.2)
```

For logarithmic parent coordinates linear in `t`, designated elimination obeys

```
A_ell dot y = dot v,
A_ell ddot y = -D^2 m_ell[(0,dot y),(0,dot y)].                 (4.3)
```

Extra explicit parameter dependence in a translated chart adds its ordinary chain-rule terms to (4.3). Equations (4.2)–(4.3), with (2.2), give the first variation including the nonlinear constraint and measure on regular branches. They do not evaluate or bound the determinant for the actual map. They follow simply by differentiating a quotient of two integrals. At zeros of a weight use unnormalized derivatives; a uniform bound on `D log p_ell` is generally false. If a chart support moves, add (2.4) before using the score formula. Verifying cancellation at every seam remains a premise.

**Discharged (the globally valid quotient rule).** Without dividing by an intermediate good density, `q_2'=Z_E'/Z_B-q_2 Z_B'/Z_B`. It applies whenever the two integrated densities are differentiable and `Z_B>0`, including when an individual contribution requires boundary terms. On a common regular domain where `B_1>0`, one may additionally put `h_1=E_1/B_1`, normalize `B_1 p_ell J_ell` to `nu`, and obtain `q_2'=nu(Dh_1[a])+Cov_nu(h_1,s_B)` for that restricted pair of integrals. This last representation is not a licence to discard `E_1` where `B_1=0`.

**Discharged (dropped parents).** If the varied parent bond is in `H_ell`, that branch of (2.1) is independent of this parent variable with all other parents fixed; its derivative is exactly zero. This does not make its activity ratio constant: for a fully dropped branch of mass `H` and a varying base `B`,

```
d log(1+H/B) = -[H/(B+H)] d log B.                            (4.4)
```

Haar output therefore removes a constraint derivative, not the derivative of normalization against the good density. Formula (4.2) keeps that normalization.

**Discharged (label transitions).** For one Bernoulli label the kernel derivative contains

```
chi'(f) dot f (K_rough-K_quiet)
       +(1-chi(f)) dot K_quiet+chi(f) dot K_rough.              (4.5)
```

The first term does not cancel by `sum p_ell=1`, since the two kernels differ. It is zero at `f=T,2T`, by the specified flat ends of `chi`; inside the transition it is a genuine term, retained in the probability derivatives of (4.2). Hulls, trees and the Haar set are fixed within a discrete pattern; crossing to another pattern is a sum of measures, not a derivative of an integer-valued dropping rule. If the cell flux is defined using a nonsmooth maximum, scalar smoothness of `chi` alone is insufficient at a tie in `(T,2T)`; a smooth implementation or a separate integrated regularity proof is needed. This is a qualification, not a demonstrated kink of the specified density.

**Implication (tree-frame and sector seams).** On an overlap let `xi=T_W(zeta)` relate two charts of the same fibre. The densities obey `w_new=w_old(T_W)|det D_zeta T_W|`, and the domains must transform as well. Differentiating this change of variables gives a divergence term; its boundary flux cancels the domain-motion term in (2.4). Thus a mere change of tree frame supplies no surviving first-order term if both represent the same integral. No comparison between distinct topological sectors follows: if there is no overlap/path within `D`, this argument says nothing between them. No global differentiable atlas, or its quantitative control at a sector boundary, is supplied by (CHART_k) as printed.

**Implication (the value of the first variation at flat, at every level).** If the cut and labels are gauge invariant, the kernel is equivariant, and the integrated densities are differentiable, then `D q_2(1)=D G_2^old(1)=0`; also `D h_1(1)=0` where this ratio is defined and differentiable. Proof: integration preserves invariance by the change of variables `U -> g.U`. At the all-identity field, constant conjugation by `i sigma_b`, `b!=a`, reverses a single bond variation `i sigma_a` and fixes the base field. Its directional derivative equals its negative. These single-bond colour variations span the tangent space, so the differential is zero. The same proof applies inductively to every integrated level and to invariant marked terms. It gives no growing constant. It cannot exclude the nondifferentiable cusp (3.1), and it does not set (4.2) to zero at a non-flat cut surface.

## 5. The second variation, then level 2

**Implication (the full second variation).** On regular domains set `u_i=partial_t^2 log w_i` and `L_i=mu_i(u_i)+Var_(mu_i)(s_i)`. Direct differentiation gives `(log Z_i)''=L_i`, hence

```
q_2'' = q_2[(Delta s)^2+L_E-L_B],
(G_2^old)'' = [q_2/(1+q_2)](L_E-L_B)
               +[q_2/(1+q_2)^2](Delta s)^2.                  (5.0)
```

These formulas include different numerator and denominator supports, subject to the boundary qualifications in Section 4. Directly checking without logarithmic scores gives `q_2''=Z_E''/Z_B-2Z_E'Z_B'/Z_B^2-q_2 Z_B''/Z_B+2q_2(Z_B'/Z_B)^2`, the same result. At a differentiable flat parent both mean scores vanish, but the difference of second moments in (5.0) remains.

**Implication (each chain term on their common regular part).** Where the restricted ratio has the expectation representation of Section 4, put `f=h_1(Phi_ell)`, `s=partial_t log w_B`, `u=partial_t^2 log w_B`, and let `kappa` denote the third joint cumulant. Twice differentiating that normalized integral gives

```
q_2'' = nu(D^2h_1[a,a]) + nu(Dh_1[a_2])
        +2 Cov_nu(Dh_1[a],s) + Cov_nu(h_1,u)
        +kappa_nu(h_1,s,s),
(G_2^old)'' = q_2''/(1+q_2) - (q_2')^2/(1+q_2)^2.             (5.1)
```

Here `q_2` denotes the restricted ratio only. For verification, the derivative of the normalized density is its density times `s-nu(s)`; its second derivative is its density times `(s-nu(s))^2+u-nu(u)-Var(s)`. Substitution gives exactly (5.1), with `kappa(f,s,s)=nu((f-nu(f))(s-nu(s))^2)`. No integration-by-parts identity or unproved correlation lemma is being used; outside the common domain one must use (5.0) or the unnormalized quotient rule.

**Discharged (the missing terms are identifiable).** In `u`, the constraint determinant contributes

```
-tr(A^-1 A'') + tr(A^-1 A' A^-1 A'),                          (5.2)
```

and each Haar factor contributes its logarithmic Hessian and acceleration. With `g(r)=2(cot r-1/r)` and `n=q/r`,

```
D^2 log h(q)[a,a] = 2(-csc^2 r+1/r^2)(n.a)^2
                    + (g(r)/r)(|a|^2-(n.a)^2).               (5.3)
```

At zero this is `-(2/3)|a|^2`. Also present are `D^2 log p_ell[a,a]+D log p_ell[a_2]` and the corresponding `log B_1` terms. In particular, `Dh_1[a_2]` is not zero merely because `Dh_1(1)=0`: most points `Phi_ell(1,xi)` on a fibre are not the flat field. The score covariances do not vanish by that symmetry either. Controlling (5.1), not cancelling the differential at one point, is the quantitative first propagation test.

**Implication (the second propagation, with no omitted chain term).** Write `Z` for the level-3 parent, `W=Phi_2(Z,xi_2)` and `V=Phi_1(W,xi_1)`, with both labels retained. The old level-0 contribution is now

```
rho_3(Z)=P_2 P_1(B_1+E_1)(Z),
q_3(Z)=P_2 P_1 E_1(Z)/P_2 P_1 B_1(Z).                        (5.4)
```

For a parent direction `H`, put `b=D Phi_2[H]`, `b_2=D^2 Phi_2[H,H]`. On the common regular part the actual composition differentiates as

```
V'  = D Phi_1[b],
V'' = D^2 Phi_1[b,b]+D Phi_1[b_2],
(h_1(V))'' = D^2h_1[D Phi_1 b,D Phi_1 b]
             +Dh_1[D^2 Phi_1[b,b]]+Dh_1[D Phi_1 b_2].         (5.5)
```

For the full ratio use (5.0) with the two joint weights `i_1(V) p_ell1(V) J_1(W,xi_1) p_ell2(W) J_2(Z,xi_2)`, `i=B,E`. On their common regular part (5.1) applies to `h_1(V)` and the joint reference law. This includes both determinants, both label derivatives, all Haar factors and the score cross terms. A dropped parent removes only its own constraint as in (4.4). Matched hard faces cancel as in (2.4); a chart change must transform both domains. Subject to differentiability and invariant cuts, `D q_3(1)=0` by the same conjugation proof. No evaluation of the nonzero quantities in (5.5) for the nonlinear pruned map has been obtained here.

**Gap (where the proof actually stops).** Neither the printed (CHART_k) nor the printed (MODE_k) bounds the sum of the last four terms of (5.1) in the required local norm. In particular they give no uniform parent derivative estimate for (5.2), or a rare-weighted estimate when label scores diverge at a flat endpoint. The mapped Text 5.3 proposes a vector field on surviving quiet lines to replace repeated designated-bond transport. Its first-derivative argument is an input to test; “iterate X” does not compute the derivative of that field, its divergence, its changing normalization, or the covariances in (5.1). I have not proved these estimates or found an actual-map counterexample to them.

## 6. All depths: the required constants and the failed induction step

**Unchecked (a precise sufficient induction, not a proved decomposition).** A usable local state could assign every connected absorbed contribution to a birth level `j`, subtract its vacuum, and retain a gauge-invariant `C^2` local function `r_(j,k)` at level `k`. In local curvature coordinates, or an explicitly equivalent gauge-invariant variation norm, it would obey

```
r_(j,k)(0)=Dr_(j,k)(0)=0,
sum_(X contains c) exp(mu |X|) ||D_F^2 r_(j,k)(X)|| <= B_(j,k),
B_(j,j+1) <= A x_j^p exp(-alpha x_j),
B_(j,k+1) <= (1+epsilon_k) B_(j,k),
sup_K sum_(j<K) B_(j,K) < infinity.                           (6.1)
```

Here `alpha>0` includes the actual threshold and entropy loss, `A,mu>0` and the nonnegative integer `p` are fixed after the source's geometric constants, and `epsilon_k` must have a stated bound. Mixed connected terms must be assigned and estimated too; (6.1) is not an assertion that logarithms of positive gases add independently. A local curvature representation and its transition control are part of the hypothesis, since plaquette variables are not globally independent coordinates.

**Implication (the dimension-four cancellation and its limit).** If a fine flux response is exactly `L^-2` per level, two derivatives cancel the `L^4` descendants per cell. This scaling is exact for a commuting constant-flux test of the all-lines map on a contractible patch in its principal-log range: every coarse plaquette spans `L^2` fine plaquettes, products commute, and the contour-gradient contributions telescope. This is a local test, not a continuously variable constant flux on a fixed periodic bundle. It has not been proved here for the nonlinear pruned response on each fluctuating fibre. If its one-step bound instead has a fixed multiplicative loss, call the resulting Hessian-budget loss `A_0>=1`; the naive induction gives `A_0^(k-j-1)`. Equations (5.1) and (5.5) are precisely where such losses enter. The vanishing first differential supplies none of the missing estimate `1+epsilon_k`.

**Discharged (what the flow can pay).** Set `n=K-j` on an affine comparison flow `x_j=x_K+b n`. A proposed birth bound `x_j^p exp(-alpha x_j)`, propagated with loss `A_0^n`, has exponential ratio `A_0 exp(-alpha b)`. Thus it is summable if `log A_0<alpha b`; a bound with the reverse inequality gives no summable majorant. An actually surviving linear flux term introduces `L^(2n)` instead, requiring `2 log L+log A_0<alpha b`. Divergence of a proposed upper bound is not an explicit nonzero term or a refutation.

Polynomial losses in `n` are paid by any positive `alpha b`. Even a factor `(1+a/x_k)` at each step gives at most

```
product_(r=0)^(n-1) (1+a/(x_K+b r))
 <= exp(a/x_K) (1+b n/x_K)^(a/b),                             (6.2)
```

because `log(1+t)<=t` and the decreasing reciprocal sum is bounded by its first term plus its integral. A factor `1+a/sqrt(x_k)` similarly gives at most `exp[a/sqrt(x_K)+(2a/b)(sqrt(x_K+bn)-sqrt(x_K))]`. Both are paid. A fixed geometric loss requires the strict rate comparison above; merely increasing `x_K` changes its prefactor, not that comparison.

**Implication (an explicit summable budget if the transport loss is bounded).** The actual conditional lower flow bound in mapped Text 5.10 is

```
x_j >= x_K/2+b_- (K-j),       b_- = (11/(6 pi^2)) log L.       (6.3)
```

If the contribution after transport is bounded by `A x_j^p exp(-alpha x_j)` with no geometric loss, then

```
sum_(j<K) A x_j^p exp(-alpha x_j)
 <= A p! (2/alpha)^p exp(-alpha x_K/4)
                    / (1-exp(-alpha b_-/2)).                 (6.4)
```

Indeed `exp(alpha x/2)>=(alpha x/2)^p/p!`, and (6.3) bounds the remaining geometric series, enlarged to start at `n=0`. Formula (6.4) is the requested level-sum with explicit constants conditional on the term estimate. The induction fails before it: the source does not establish the needed transport bound on the displayed score/Jacobian terms. This is not a claim that such a bound is false.

## 7. HOLES and the last scales: the numerical coefficients actually specified

**Discharged (a direct SU(2) lower bound, including boundary slack).** The HOLES mechanism can be checked without its Gaussian-integral estimate. Condition on all links except one. Its six staples sum, as quaternions, to `sR`, `0<=s<=6`, so its angle relative to `R` has density proportional to `sin^2 phi exp(kappa cos phi)`, `kappa=xs<=6x`. If all six plaquettes have angle at most `T`, then `s cos phi>=6 cos T`, hence `phi<=T`. On `[T,2T]`, for `T<=1/2`, `sin phi>=phi/2>=T/2` and `cos phi>=1-2T^2`. The numerator mass is at least `(T^3/4) exp(kappa-2kappa T^2)`; the whole denominator is at most `(pi/2) exp(kappa)<2 exp(kappa)`. Consequently

```
P(at least one incident plaquette rough | rest)
 >= (T^3/8) exp(-12xT^2) >= (T^3/12) exp(-12xT^2).             (7.1)
```

The elementary trigonometric bounds follow by integrating `cos t>=1-t^2/2` on `[0,1]`; `pi<4` follows, for example, by comparing a circle's area with its circumscribed square. For a cell of side `N>=4`, choose direction-1 links with every base coordinate in `{1,...,N-2}`, choosing the more populous parity in each coordinate. There are at least `(N/4)^4` such links; none share a plaquette and all their plaquettes are inside the cell. Given the other links the events are independent. Thus one may safely replace the source's boundary-sensitive `N^4/16` by `N^4/256`, obtaining

```
P(no rough fine plaquette in a top cell) <= exp(-nq),
nq >= (T^3/3072) exp[4K log L-12x_0 T^2].                    (7.2)
```

This harmless slack avoids assuming a particular parity or boundary rounding. The exponential comparison is unchanged.

**Implication (insert the actual printed flow bounds).** The source's one-loop coefficient and rigorous conditional comparison slopes are

```
b_0 = (11/(3 pi^2)) log L,
b_- = b_0/2,       b_+ = 3b_0/2,
x_0 <= x_K+b_+ K+2C(L),       x_K in [x_*,x_*+B),
B=3b_0/2+2C(L),               T=a_*/L^2.                     (7.3)
```

For `T<=1/2`,

```
12 b_+ T^2/log L = 66T^2/pi^2 <= 33/(2pi^2) < 11/6 < 2.     (7.4)
```

Here `pi>3` follows since each of the six unit chords of an inscribed regular hexagon is shorter than its arc. Combining (7.2)–(7.4) gives

```
nq >= (T^3/3072)
      exp[2K log L-12T^2(x_K+2C(L))].                        (7.5)
```

For fixed terminal parameters this diverges with depth; a union bound covers any fixed finite number of top cells. This verifies the HOLES conclusion on the conditional flow, including its larger upper comparison slope, not just the nominal coefficient. It concerns the original Wilson ensemble, not a conditional probability on a prescribed flat parent. Dense microscopic exits do not imply that newly born *renormalized* polymers have order-one activity: their vacuum part has already been integrated.

**Implication (last-three-scale cost table).** Put `epsilon=cT^2` for whichever actual rare-event rate is being used. For the proposed factor `exp(-epsilon x_(K-n))`, (6.3) gives a common upper prefactor `exp(-epsilon x_K/2)`. The remaining factors, before any polynomial or transport loss, are:

| Age `n` | Raw count, no field gain | One flux variation | Two flux variations |
|---|---|---|---|
| 0 | `1` | `1` | `1` |
| 1 | `L^(4-lambda)` | `L^(2-lambda)` | `L^(-lambda)` |
| 2 | `L^(8-2lambda)` | `L^(4-2lambda)` | `L^(-2lambda)` |

**Discharged (table arithmetic).** `lambda=11cT^2/(6pi^2)`. The factors are respectively `L^(4n)`, `L^(2n)`, and `1`, multiplied by `exp(-epsilon b_- n)`. At the actual top itself the cost is `exp(-epsilon x_K)`, stronger than the common prefactor. On the nominal affine slope replace `lambda` by `2lambda`. These are bounds on a proposed rate, not computed values of the activities.

**Implication (the FIB numbers).** The rate actually displayed in Section 3 of the two-step note is `c_FIB=gamma eps_q^2/1600`. It gives

```
lambda_FIB = 11 gamma eps_q^2 a_*^2/(9600 pi^2 L^4),
x_* >= 1536 n_P/(gamma eps_q^2 T^2)
    ==> c_FIB x_* T^2 >= (24/25) n_P.                        (7.6)
```

The source also writes `gamma(L)=c_gamma/(L^2 C_tree(L))`, so the first rate in (7.6) contains `L^-6/C_tree(L)` after substitution. Choosing the weaker valid normalization `gamma<=1`, `eps_q<=1` and `T<=1/2` already gives `lambda_FIB<1/30000`, by `pi^2>9`. With these permitted normalizations this rate pays the quadratic column with a potentially enormous geometric-series constant; it cannot pay an `L^2` loss each step. This does not exclude a stronger true rarity estimate. The one-fibre threshold in (7.6) alone does not compare the source's unspecified entropy constants with the rate. FIB prices the stated non-quiet chart event; identifying every labelled or amplitude exit with an event having this rate is itself an input, not proved by this substitution.

**Discharged (the entropy inequality that has to hold at the top).** On a graph of degree at most `Delta`, the number of connected `m`-cell sets containing a fixed cell is at most `Delta^(2(m-1))`: choose a spanning tree by a fixed ordering and record its depth-first walk; the walk visits exactly the set and has length `2(m-1)`. Thus `2log Delta` per cell suffices as a combinatorial upper cost. Fixed types and one-step branching add finite costs, including `4log L` if all possible children are charged. The source's continuous-data cost is `C(L)d_x(x)^4 log x`; with its proposed logarithmic collar it is bounded by `E(log x)^5` for `x>=e`, after including the growing graph degree. Consequently a sufficient own-level small-activity condition is

```
s_0(L)+E(log x)^5 <= cT^2 x/2,       for all x>=x_*.          (7.7)
```

This is an explicit comparison, not an additional decay factor supplied by depth. If `epsilon=cT^2`, it holds on choosing `x_*=exp(Y)` with

```
Y >= max{1, 4E*6!/epsilon, log(max(1,4s_0/epsilon))}.          (7.8)
```

Proof: `exp(y)>=y^6/6!` makes `E y^5<=epsilon exp(y)/4` for all such `y`; the remaining constant costs another `epsilon exp(y)/4`. Then the full per-cell activity is bounded by `exp(-epsilon x/2)` and its spatial animal sum converges once this number is sufficiently small. Larger polynomial prefactors can be put into the same cost. Thus the order of choices in the source *allows* top-scale entropy to be paid if the rate and local activities have first been proved. It does not pay a fixed per-depth factor in Section 6.

**Gap (no missing decimal can be supplied honestly).** There are no selected numerical values for `L,a_*,gamma,eps_q,n_P,E,s_0,x_*` at this pin. Equations (7.3), (7.6) and (7.8) are the comparison with the actual coefficients and the actual last-scale parameter range. A numerical top-scale margin would require inventing those missing choices. Neither HOLES nor an arbitrarily large permissible `x_*` proves the transport estimate.

## 8. Exactly what (CHART_k), (MODE_k), and fd-local would have to supply

**Gap (chart requirements).** The calculation needs a gauge-covariant fixed-domain atlas for the full positive decomposition, including pruned and partly Haar branches, compatible changes of tree, and enough parent regularity to differentiate the inverse determinant twice. In the displayed coordinate formula this reads third derivatives of `m_ell` and an inverse bound for `D_y m_ell`, not merely convexity in `xi`. It also needs integrable derivatives of the label weights at their zeros and matching boundary measures when charts meet. To propagate (6.1), the parent-response and score-covariance estimates must have the stated level budgets. A lower bound on `D_xi^2 S` alone supplies none of these mixed derivative bounds.

**Discharged (logical insufficiency of convexity plus a small mode).** In a fixed Euclidean ball take `S_v(xi)=(x+N|v|^2)|xi|^2/2` and the mark `a(xi)=1_(|xi|>r)`, `0<r<R`. Every member has Hessian at least `x` and mode zero, for arbitrary `N>0`. At `v=t e_1`, its marked probability has second derivative at zero

```
-N Cov_(v=0)(a,|xi|^2).
```

The covariance is positive: it equals `p(1-p)` times the difference between the outside and inside conditional means of `|xi|^2`. Thus this derivative is arbitrarily large with the same convexity and mode constants. This rotationally invariant example is not the actual SU(2) map; it proves only that the two printed inequalities do not logically contain parent-regularity estimates. A genuine map estimate is indispensable.

**Discharged (source comparison for fd-local).** `fd-local.md` Section 4 writes compact flat constraint corrections and the flat gauge commutator, and obtains flat coercivity **conditional on the one-jump coercivity and its geometry**. Section 5 explicitly leaves the curved support-preserving estimate `(LC_U)` open. This does not prove (MODE_k) as stated, even with a flat top parent: that statement quantifies over arbitrary allowed values off `P`, which need not have a flat conditional minimizer. An inverse/decay estimate still has to turn those boundary values and the actual nonlinear action, gas and Jacobian into the numerical `Dev_b<=eps_q^2 T^2/16` bound.

**Implication (the very restricted flat case).** With parent and exterior data all identity, an invariant differentiable chart action has zero gradient at zero by the colour-rotation argument. Strong convexity then makes zero its unique minimizer, so its deviation is zero. That is not the “any exterior values” quantifier of (MODE_k). At genuinely curved class-fill backgrounds the localization route of `fd-local.md` needs `(LC_U)` in addition to the other saddle and source estimates; `(LC_U)` alone would not establish (MODE_k). No curved F-D theorem or mode estimate has been imported from its flat calculation.

## 9. The strictly smaller inequality on which this attempt stops

**Gap (S2: one label, two integrations, one direction, finite volume).** Fix once a finite periodic lattice large enough for one hull and two block steps; for definiteness take its side at level 2 to be `m=4 ceil(2L+S_*+d_1+2)`. Fix all construction profiles and tree/constraint choices. Let `E_(1,c)(V)` be the level-1 density contribution in (2.1) with the single level-0 rough label `c` and every other level-0 label quiet. Sum its entire amplitude-cut partition, so its internal hard-cut complements are retained. Let `B_1` be the all-good level-1 contribution used in (4.1). Apply the **full** level-1 kernel, including all its labels and Haar branches, to each. For one level-2 bond set `W_b(t)=exp(i t sigma_3)` and set every other parent bond to the identity. Define

```
r_c(t;x) = log[1+(P_1 E_(1,c))(W(t))/(P_1 B_1)(W(t))],
x=x_0.
```

The smaller target is the single inequality

```
limsup_(t -> 0) |r_c(t;x)+r_c(-t;x)-2r_c(0;x)|/t^2
    <= C_2 x^2 exp(-alpha_2 x T^2),       for every x>=x_2*,    (S2)
```

with fixed `C_2<infinity`, `alpha_2>0`, `x_2*`, allowed to depend on this finite lattice, `L,a_*` and the fixed construction profiles. Existence of the indicated density values and positive denominator is included. This formulation does not presume differentiability and therefore tests the cusp directly. When the regular chart formulas apply, its left side is the absolute second derivative calculated in (5.0) for this one marked contribution, with (5.1) on any common regular part. Gauge invariance makes `r_c(t)=r_c(-t)` but does not bound that quotient.

**Discharged (why S2 is strictly smaller).** It has one marked birth cell, exactly two integrations, one parent direction at the identity and a fixed finite volume. It asks for neither arbitrary parent sectors, a spatial decay norm, multiple interacting holes, the mode under arbitrary exterior data, nor any constant uniform in depth or volume. It is a restricted term estimate of the kind required by the requested termwise (GAS2) proof, and its success would not imply (6.1). Its failure could identify a genuine hard-cut or singular-fibre obstruction at the first propagation; the toy term (3.1) has an infinite left side and so illustrates exactly what S2 tests. It is not a renaming of the all-level claim.

**Unchecked (expectation, with reason).** I expect S2 to hold for a fully specified, gauge-covariant smooth-label implementation with regular surviving-line charts and matched cuts. There are only finitely many label patterns and chart dimensions; a single rough label requires positive Wilson energy, while the flat all-good denominator has a zero-energy configuration. Derivative costs and finite-dimensional normalization powers can then be absorbed into a smaller positive exponent. Complete cut complements remove the explicit overlap cusp. This suggests a finite-dimensional proof after verifying the pruned constraint Jacobians and chart transitions. It is not that verification: those determinants and the transition contributions have not been bounded here. A singular retained constraint or an unmatched hard domain would invalidate the expectation.

**Discharged (decision scope).** I have not produced an uncancelled first-order term for the actual mapped kernel within its hypotheses. The SU(2) term (3.1) is explicit but is cancelled by its true complement and has not been realized by the actual map. Conversely, the exact chain rules leave the quantitative term (S2) unproved already at the first propagation. The all-level constants therefore cannot be asserted. This stops at S2, not at the words “prove GAS2”; it neither kills the integrate-first route nor establishes this form of its gas.

## 10. Scope check and recovery record

**Discharged (negative-claim discipline, narrowed to this file-only task).** The pinned [no-go-discipline skill](../../../../../docs/ai_methodology/skills/no-go-discipline/SKILL.md) was inspected and applied only to the scope of the conclusion. The explicit single-file/no-commit/no-audit instruction overrides its packet and landing operations. No packet status is claimed. N1: actual attacks were the sharp-cut overlap, Haar/label transitions, the two successive chain rules and the depth/entropy comparison; these are not five certified excluded route families. N2: regularity, transport and mode estimates have unresolved dependence; no independent-wall count is claimed. N3: regular branches, invariant cuts, conditional flow and entropy bounds are named premises. N4: (3.1) attacks unmatched sharp indicators, not the actual kernel; HOLES attacks persistent microscopic regions, not absorbed activities. N5: the written SU(2) calculations are finite-dimensional; no lattice-wide actual-map counterexample is claimed. N6: specifying profiles and proving chart matching require mathematics, not a new physical axiom. N7: a finite-chart proof of S2 followed by the source's proposed quiet-line response and connected covariance estimates remains a concrete possible route. N8: mapped Text 5.3 already records the failed per-level designated-bond estimate and proposes that replacement; its failure has not been assumed to rule out the replacement.

**Unchecked (memory and verification limits).** Moving-boundary differentiation, normalized-score calculus and the spanning-tree count are familiar patterns recalled from memory; the specific identities used here are proved above. No literature theorem, external account, numerical run or independently checked scientific result is a premise. Exact serving-model/effort metadata are unavailable, so the target's model-floor setting cannot be certified here. The installed physics-loop entry point was inspected for applicability; no campaign, delegation or delivery workflow was launched. The workflow and no-go/freshness instructions were read from the pinned git blobs because the sparse checkout omits `docs/`.

**Discharged (source record).** Instructions: `GOAL.md:1–75`, `FINISH.md:115–149`, `AGENTS.md` and the pinned workflow/freshness/no-go blobs. Primary mathematical ranges inspected: `explicit-region-two-step.md:1–33,48–171,198–216`; mapped `:1–32,263–333,376–415,560–664,754–765,947–975,989–1021`; `fd-local.md:1–38,87–207,223–251`. Map-support inspection: `block-poincare-energy-package.md:1–26,60–86`, `analytic-lift.md:7–18`, `lift-nonlinear.md:32–70`; Laplace-note hypotheses `:11–34`. These are inspection ranges, not certification of their arguments. Targeted heading/line searches also touched the allowed `relative-density-bound.md` and the map notes; these searches supplied no proof. Some search/read outputs were truncated and were not treated as verification; the passages on which a calculation here relies were subsequently available in bounded, untruncated reads. The forbidden files, their gates, the independent attempt and the external Sussman–Alpoge account were not opened. No other file or editable prompt was changed.

STOPPED
