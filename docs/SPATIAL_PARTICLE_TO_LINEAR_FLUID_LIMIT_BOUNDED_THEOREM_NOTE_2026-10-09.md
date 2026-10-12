---
claim_id: spatial_particle_to_linear_fluid_limit_bounded_theorem_note_2026-10-09
claim_type: bounded_theorem
claim_scope: "For the supplied tuned D3Q27 spatial population process near its Gibbs reference, a stopped dissipative estimate combines particle fluctuations, nonlinear amplitude, spatial mesh and linear hydrodynamics. An explicit simultaneous scaling yields O(delta) path error with O(delta^2) failure probability on fixed time intervals; a fresh-ancilla realization gives the corresponding fixed-time measured occupation bound."
upstream_dependencies:
  - supplied_finite_velocity_collisions_and_gibbs_equilibration_bounded_theorem_note_2026-10-08
  - d3q27_dissipative_hydrodynamic_approximation_bounded_theorem_note_2026-10-09
  - spatial_quantum_collision_realization_bounded_theorem_note_2026-10-09
runner: scripts/spatial_particle_to_linear_fluid_limit_2026_10_09.py
---

# A simultaneous spatial particle to linear fluid limit

**Date:** 2026-10-09

**Type:** bounded_theorem

**Status:** proposed_retained

Current surface status: conditional-support. Independent retained-status audit has not occurred.

**Source baseline:** `17a95e60d85afc246fc7c163adef8869ab3f4194`; continued from `b178e3a5d4c1d1301255596d10ac4e1bc2aeb192`.

**Runner:** [finite controls](../scripts/spatial_particle_to_linear_fluid_limit_2026_10_09.py).

**Evidence cache:** `logs/runner-cache/spatial_particle_to_linear_fluid_limit_2026_10_09.txt`.

For fixed regular prepared data and time interval, this note proves that an
explicit local finite-particle model approaches linear Stokes/heat flow with
O(delta) path error and O(delta^2) failure probability under one simultaneous
scaling. It also transfers this bound to one-time occupation measurements of
a supplied fresh-ancilla quantum realization.

The [linear hydrodynamic theorem](D3Q27_DISSIPATIVE_HYDRODYNAMIC_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-10-09.md)
provides the H4 kinetic-to-fluid estimate and its constitutive coefficients.
The [finite collision contract](SUPPLIED_FINITE_VELOCITY_COLLISIONS_AND_GIBBS_EQUILIBRATION_BOUNDED_THEOREM_NOTE_2026-10-08.md)
provides the reaction network. Both are provisional supplied-model mathematics;
the former is selectively independently checked in this branch and the latter
has an unaudited ledger row at main `d9b869b97944676aaa759915462c529dc276a04c`. Their physical identification conditions
are inherited. No persistence or external long-time theorem is needed here.

This argument uses dissipation near the Gibbs reference to control a stiff
collision scaling. The separate fixed-amplitude nonlinear kinetic theorem
uses a different local-time estimate; its fixed-prefactor asymptotics are not
substituted into the present simultaneous limit.

| Proof obligation | Disposition |
|---|---|
| Finite drift, weighted collision linearization and uniform grid algebra | Proved in Sections 1–2 |
| Nonlinear small-amplitude control | Proved in Section 3 |
| Stopped particle estimate, including initial fluctuations and jump overshoots | Proved in Section 4 |
| Spatial symbol, cutoff and interpolation comparison | Proved in Section 5 |
| H4 linear kinetic-to-fluid bound and coefficients | Linked hydrodynamic theorem, reproduced constants in Section 5; independently checked provisional dependency |
| Quantum generator and diamond approximation | Linked spatial quantum theorem; its hypotheses are matched in Section 6 |
| Simultaneous scale choice | Proved in Section 6 |
| Native excitation identification and nonlinear fluid limit | Open extensions; not conclusions of the stated theorem |

## 1. Model and target

Use V={-1,0,1}^3, every one of the 288 reversible distinct-four-species
collisions r:{i,j}<->{k,l}, nu_r=e_k+e_l-e_i-e_j. Write e_v=|v|^2 and
M_v=(2/3)^(3-e_v)(1/6)^e_v; hence M_min=1/216. In expressions for velocity
fields below, e denotes the vector (e_v). The nine axial exchanges are
{s e_c-e_a,s e_c+e_a}<->{s e_c-e_b,s e_c+e_b}, where c is one coordinate,
a,b are the other two, s is -1,0,1, and e_a,e_b,e_c are spatial unit vectors.
Let these nine exchanges have rate alpha_* and
all other exchanges rate 1, where alpha_*=(-4579+3sqrt(7614177))/1072.
This is a supplied choice of rates, not their physical derivation.

Set Q(f)=sum_r kappa_r nu_r(f_i f_j-f_k f_l), W=diag M,
B=W^{-1}sum_r kappa_r M_i M_j nu_r nu_r^T. The parent proves B>=0 and
its five-dimensional kernel mathcal K=span{1,v_x,v_y,v_z,e}. Define the
symmetric bilinear expression

Gamma(h,g)= W^{-1} sum_r (kappa_r M_i M_j/2) nu_r
 (h_i g_j+h_j g_i-h_k g_l-h_l g_k).

Then Q(M(1+a h))=-a W B h+a^2 W Gamma(h,h), exactly.
Write J_r=sum_{v in r}1/M_v and C_R=sum_r kappa_r M_i M_j J_r=tr B.
All constants below are finite numbers fixed by this finite model.

Space is the torus of side 2pi with normalized measure. Take an odd integer
m>=3, ell=2pi/m, w=m^{-3}, cells centered at x_z=ell*z. Every cell has normalized
weight w, not ell^3. Principal Fourier indices are K_m={-(m-1)/2,...,(m-1)/2}^3.
For a grid field define the DFT with coefficient w sum_z and weighted norm
||g||_{s,m}^2=sum_{k in K_m}(1+|k|^2)^s sum_v M_v |g_hat_v(k)|^2.
The s=0 norm is w sum_{z,v}M_v |g_{z,v}|^2. I_m g is the piecewise constant
cell interpolation, J_m g its trigonometric interpolation. Both preserve
this L2 norm. J_m is only a comparison interpolation, not a positive density.

At total particle number N>=2, let n_{z,v} be nonnegative integer counts
summing to N, and F^N_{z,v}=n_{z,v}/(Nw). For 0<delta<=1, the finite CTMC has:

* hop (z,v)->(z+sign(v_d)e_d,v) at rate |v_d|n_{z,v}/(delta ell),
  for every nonzero component v_d;
* forward/reverse collision r in cell z at rates
  kappa_r n_{z,i}n_{z,j}/(delta^2 Nw) and
  kappa_r n_{z,k}n_{z,l}/(delta^2 Nw).

Every event is local in space, preserves total particle number and the three
label momenta and label energy globally. Local particle number can vary by
transport. No global fiber mixing or product closure of expectations is used.
The process is finite and nonexplosive for every fixed set of parameters.
Its exact drift for F^N is A_m F^N/delta+Q(F^N)/delta^2, where
(A_m g)_{z,v}=sum_d |v_d|[g_{z-sign(v_d)e_d,v}-g_{z,v}]/ell.
This conditional drift is nonlinear; E Q(F^N) is not set equal to Q(E F^N).

Let real U0=rho0(5-3e)/2+3 j0.v be in H_M^4 of this torus, with div j0=0
and spatial mean rho0=0. The latter supplies unit total mean mass. Define
N_s=||U0||_{dot H_M^s}, H=||U0||_{H_M^4}; no smallness of H is assumed.
Let P_m U0 be the Fourier cutoff to K_m and u_m^0 its grid restriction.
Given amplitude a>0, prepare labelled particles iid with one-particle
probabilities p_{z,v}=w M_v(1+a u^0_{m,z,v}); positivity is established below.
This is a supplied initial preparation, not molecular chaos assumed at later
positive times. Define the random relative fluctuation
h^N_{z,v}=(F^N_{z,v}/M_v-1)/a.

The target U(t)=rho(t)(5-3e)/2+3 j(t).v solves
rho_t=(4/49)Delta rho, j_t=(67/361)Delta j from rho0,j0.
We seek a probability bound uniform in t in [0,T] for I_m h^N-U.

## 2. Two uniform finite-dimensional estimates

For complex velocity vectors, triangle and Cauchy--Schwarz give
||Gamma(h,g)||_M <= (C_R/2)||h||_infinity ||g||_M.
Indeed the norm of W^{-1}nu_r is sqrt(J_r), and the four distinct g entries
have sum of absolute values at most sqrt(J_r)||g||_M. We freely enlarge
C_R/2 to C_R when convenient.

The sum S4^2=sum_{k in Z^3}(1+|k|^2)^{-4} is less than 36. Counting shells by
|k|_infinity=n bounds it by
1+sum_{n>=1}(24n^2+2)n^{-8} <=1+24(6/5)+2(8/7)=1123/35<36;
the zeta bounds here follow by the elementary decreasing-function integral
bound, not numerical summation. Thus ||g||_infinity <= E4 ||g||_{4,m},
E4=6/sqrt(M_min), uniformly in m.

Aliased Fourier addition replaces p+q by its principal representative k;
|k|<=|p+q|<=|p|+|q|. Hence
(1+|k|^2)^2 <=8[(1+|p|^2)^2+(1+|q|^2)^2].
Finite-group convolution Young/Cauchy--Schwarz, together with the previous
pointwise bilinear bound, gives
||Gamma(g,h)||_{4,m} <= G4 ||g||_{4,m}||h||_{4,m},
with the deliberately loose constant G4=96 C_R/sqrt(M_min).
To see each factor: enlarge the velocity bilinear norm to
C_R/sqrt(M_min); the weight inequality contributes 8 to each of two
convolutions, and each unweighted l1 norm is <=6 times its weighted l2 norm.
The same bound holds in the continuum H4 space, using ordinary convolution.

A_m has Fourier diagonal symbol
sum_d |v_d|(exp(-i sign(v_d) k_d ell)-1)/ell,
whose real part is nonpositive. Since B is nonnegative in the M norm,
L_m=A_m/delta-B/delta^2 generates a contraction in each ||.||_{s,m}.
No commutation of A_m and B is assumed: their sum is dissipative at each k.

## 3. Nonlinear deterministic grid comparison

Let g_m solve
 dg_m/dt=L_m g_m+(a/delta^2)Gamma(g_m,g_m), g_m(0)=u_m^0.
Since cutoff is contractive, ||u_m^0||_{4,m}<=H. Assume
 a G4 T H/delta^2 <=1/4,
 a(R0+1)<=1/2, where R0=2 E4 H.
For H=0 the solution is identically zero. Otherwise the mild equation and
the quadratic norm inequality give, by scalar comparison,
||g_m(t)||_{4,m} <= H/(1-a G4 H t/delta^2) <=2H.
This a priori bound gives existence throughout [0,T] by finite ODE continuation.
Thus ||g_m||_infinity<=R0, uniformly in m. The corresponding
f_m=M(1+a g_m) solves the positive mass-conserving upwind reaction ODE.
Initial positivity follows from the displayed smallness; quasipositivity
of transport and mass-action proves it persists. At every fixed m, the
finite mass simplex also provides a separate global continuation argument.

Let l_m(t)=exp(t L_m)u_m^0. Then Duhamel gives
sup_{t<=T}||g_m-l_m||_{4,m} <=4a G4 T H^2/delta^2.
This is a quantitative small-amplitude step, not a nonlinear fluid theorem.

## 4. Stopped particle estimate without a stiff Gronwall factor

Let E=h^N-g_m and r_m=sqrt(w M_min). Stop at
 tau=inf{t>=0: ||E(t)||_{0,m}>=r_m}.
If the initial error exceeds the threshold, tau=0. Before tau every relative
component error is less than 1, so ||h^N||_infinity<=R0+1 and F^N_v<=2M_v.
Each jump can overshoot the threshold; none of the following bounds assumes
otherwise, since rates/drift are evaluated just before the jump.

The error drift is
 L_m E+(a/delta^2)[Gamma(h^N,h^N)-Gamma(g_m,g_m)].
By symmetry and the bilinear bound, twice its energy pairing is at most
 L ||E||_{0,m}^2,
 L=2a C_R(2R0+1)/delta^2,
where we write the bound for the drift of ||E||^2 (the factor 2 is included).
The dissipative linear part contributes a nonpositive term. This is why
no exp(constant*T/delta^2) or exp(constant*T/(delta ell)) is needed.

A hop of velocity v changes two entries of h^N, with squared norm
 2/(N^2 w a^2 M_v).
Before tau, the sum of hopping rates times these squared increments is bounded by
 216/(N w a^2 delta ell),
because sum_{v,d}|v_d|=54 and sum_z n_{z,v}<=2N M_v.
A collision jump r has squared norm J_r/(N^2 w a^2).
Each of its two directions has rate <=4 kappa_r Nw M_i M_j/delta^2
in a cell. Summing both directions and all cells bounds its total quadratic
variation density, together with the hopping part, by
 V=[216/(delta ell)+8 C_R/delta^2]/(N w a^2).
This includes the exact falling-factorial convention: all four reaction
species are distinct, so n_i n_j is the correct propensity.

For the multinomial initial counts,
 E||E(0)||_{0,m}^2
 =sum_{z,v} p_{z,v}(1-p_{z,v})/(N w a^2 M_v)
 <=54/(N w a^2),
using p_{z,v}<=2wM_v and sum_z w=1. The probabilities sum to 1 because
mean rho0=0 and the finite Fourier grid integrates the cutoff exactly.

The finite-state jump energy identity, stopped at tau, gives
 E||E(t wedge tau)||^2 <= E||E(0)||^2
   +integral_0^t[L E||E(s wedge tau)||^2+V]ds.
The deterministic g_m is stopped at the same time. Drift and variance terms
are only integrated before tau; replacing them by the right side increases
this inequality. Therefore, with
 D=exp(LT)[54+T(216/(delta ell)+8C_R/delta^2)]/(N w a^2),
we have E||E(T wedge tau)||^2<=D and
 P(tau<=T)<=D/(w M_min)=:Pi.
On the complementary event sup_{t<=T}||h^N-g_m||_{0,m}<=r_m.
This controls the actual random particle path. Pi may exceed 1 for small N;
the useful probability bound is min(1,Pi), not a claim of small error for
arbitrary finite parameters.

## 5. Spatial comparison and the parent's linear fluid bound

For each principal frequency k,
||symbol(A_m)+i diag(v.k)||_M <=ell |k|^2/2,
by |exp(-iy)-1+iy|<=y^2/2. Both the discrete and continuum linear kinetic
semigroups are contractions. Duhamel, with the correct order of matrix
products, gives
 sup_t ||J_m l_m(t)-h_delta(t)||_{L_M^2}
 <= H/[1+((m+1)/2)^2]^2 + T ell N_2/(2delta),
where h_delta is the full continuum linear kinetic solution from U0.
The first term is the Fourier cutoff tail; its estimate uses the H4 norm.

For any grid g, discrete Fourier orthogonality across cell centers gives
||I_m g-J_m g||_{L_M^2} <=sqrt(3)ell ||g||_{1,m}.
One can improve this constant using centered cells, but it is unnecessary.
Consequently the nonlinear g_m interpolation costs at most 2sqrt(3)ell H.
There is no interpolation-error estimate on the noisy field: I_m already
preserves its grid error norm exactly.

For reference, the parent proves sup_t||h_delta-U|| <=delta C1+delta^2 C2.
Writing b=||B^{-1}|mathcal K^perp||, c=sqrt(3), d=67/361,
A_corr=cb+(4/49)sqrt(6/5), its constants are
 C1=2 A_corr N1+T A_corr(d+bc^2)N3,
 C2=2bc A_corr N2+Tbc A_corr d N4.
The bound remains valid with the explicit upper bound
b=6224911145567/509693499350, since all our rates are >=1.
This is a dependency on the parent's checked linear theorem, not a new
independent proof of its constitutive coefficients.

Combining the estimates proves the following supplied-model theorem:
with probability at least 1-min(1,Pi), uniformly for 0<=t<=T,

 ||I_m h^N(t)-U(t)||_{L_M^2}
 <= sqrt(w M_min)+2sqrt(3)ell H+H/[1+((m+1)/2)^2]^2
    +T ell N2/(2delta)+4a G4 T H^2/delta^2+delta C1+delta^2 C2.

Every norm, rate, preparation, supplier and scaling variable is defined above.
Both limiting mechanisms occur on the same process and time interval.

## 6. One explicit simultaneous schedule

Fix T and U0. As delta decreases choose
 a=delta^3,
 m=the least odd integer >=max(3,2pi delta^{-2}),
 N=max(2,ceil(delta^{-23})).
Then ell is comparable to delta^2, w is comparable to delta^6, the two
smallness conditions eventually hold, and LT=O(delta).
The right-hand error bound is O(delta). Its failure probability is O(delta^2):
N w^2 a^2 is comparable to delta^{-5}, while the dominating hopping bracket
is O(delta^{-3}). The deterministic interpolation and noise threshold terms
are respectively O(delta^2) and O(delta^3); the cutoff tail is O(delta^8).
These exponents are sufficient and deliberately nonoptimal. They are not
physical scaling predictions or computationally practical particle counts.

The [spatial quantum realization](SPATIAL_QUANTUM_COLLISION_REALIZATION_BOUNDED_THEOREM_NOTE_2026-10-09.md)
constructs this exact generator on supplied labelled position–velocity registers.
In its notation choose b=delta^{-1}, c=delta^{-2}; write its gate step as eta.
Its mark-rate sum is

\[
\Lambda=\frac{54N}{\delta w\ell}
       +\frac{(N-1)K}{\delta^2w^2},\qquad K=\sum_r\kappa_r.
\]

Prepare any quantum density matrix whose occupation law is the multinomial
law specified in Section 1; the product diagonal preparation is one example.
For eta Lambda<=1/4, perform the supplied gate schedule up to
floor(t/eta) macrosteps, then measure occupations. Let E_bound denote the
complete right side of the classical error bound in Section 5. Measurement
contracts trace distance, so the quantum realization's channel estimate gives

\[
\sup_{0\le t\le T}\Pr_{\mathrm{readout\ at}\ t}
 \bigl(\|I_m h^N-U(t)\|_{L_M^2}>E_{\rm bound}\bigr)
 \le\min\{1,\Pi+\tfrac43T\eta\Lambda^2+\eta\Lambda\}.
\]

This follows by total-variation comparison with the classical count law at
that time, then the stronger classical path bound. No amplitude factor is
lost in the comparison: total variation controls every occupation event,
including the rescaled-error event above.

Under the same simultaneous schedule, Lambda=O(delta^{-37}). Choosing
eta=delta^{76} makes the extra failure bound O(delta^2), with
eta Lambda<=1/4 eventually. The measured quantum model therefore has O(delta)
error and O(delta^2) failure probability, uniformly in the choice of one
measurement time on [0,T]. This is a family of one-time measurements; it does
not specify a repeated-measurement record. The classical result controls a
whole CTMC path. These are distinct quantifiers.

## 7. Scope and verification obligations

New supplied choices: position/velocity particles, multiple occupancy per
cell, directed nearest-neighbor hop law, local binary collisions, rates,
clock, iid initial diagonal, fluctuation normalization and joint scaling.
They are mathematical hypotheses, not additions to the framework premises.
Permanent single-site Records are not silently rewritten as moving labels.
No physical species, viscosity, nonlinear Navier--Stokes or empirical prediction
is identified. No long-time or arbitrary-amplitude limit is claimed.

Selective independent review covers: alias-uniform H4 algebra/embedding;
linear dissipation with noncommuting streaming and B; stopped energy estimate
including jump overshoots and random initial error; volume factors and reaction
multiplicities in the bracket; mean-zero initial mass and positivity; continuum
symbol/cutoff/interpolation bounds; parent theorem's exact initial-data map;
simultaneous scaling exponents. Suggested later Lean targets are finite
operator identities and the stopped-energy bound under explicitly matched
finite-state assumptions; no Lean verification is claimed.

## 8. Evidence and review record

The primary runner reconstructs the finite network, weighted polynomial and
jump identities, tests spatial Fourier/interpolation controls, and checks the
scaling powers with failing perturbations. These finite controls support the
written argument; they do not prove its infinite-dimensional estimates by
sampling. The source-bound `COMPOSITION_INDEPENDENT_REVIEW.md` in the loop
pack independently checks the analytic proof and records its separate exact
calculations. The source-bound quantum review checks the inherited finite
channel bound. The endpoint count schedule explicitly enforces N>=2.

The strongest missing step toward the physical target is a native carrier
and dynamics whose decoded observables satisfy this supplied local process
with controlled error. No physical supplier has been adopted as a framework
axiom. The published scope is a conditional mathematical chain; no physical
collision rate, empirical transport prediction or nonlinear fluid theorem is claimed.


```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Compose microscopic spatial dynamics with controlled macroscopic transport."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Derive a native carrier-to-population approximation, then test finite-amplitude fluid closure."
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Simultaneous supplied-model particle, spatial and weak-amplitude linear-fluid limit with a quantum measurement approximation."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
