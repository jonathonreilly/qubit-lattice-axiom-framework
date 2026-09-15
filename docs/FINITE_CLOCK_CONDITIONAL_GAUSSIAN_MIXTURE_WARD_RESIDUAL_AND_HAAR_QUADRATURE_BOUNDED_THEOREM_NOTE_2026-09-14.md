---
claim_id: finite_clock_conditional_gaussian_mixture_ward_residual_and_haar_quadrature_bounded_theorem_note_2026-09-14
claim_type: bounded_theorem
claim_scope: "For finite Villain plaquette complexes with each incident link appearing once per plaquette and positive possibly anisotropic couplings, the one-link conditional weight is an exact positive mixture of translates of a wrapped Gaussian with precision equal to the incident-coupling sum. Its Fourier bound gives uniform conditional finite-clock quadrature and Ward-residual estimates. A hybrid-measure argument compares bounded-frequency integer Wilson characters with the U(1) model with an absolute error linear in link count. Growing clock order can make this error vanish; no fixed-order infrared phase or relative small-Wilson estimate is inferred."
upstream_dependencies: []
runner: scripts/finite_clock_conditional_gaussian_mixture_ward_residual_and_haar_quadrature_2026_09_14.py
---

# Uniform finite-clock Ward and Haar comparison

**Date:** 2026-09-14
**Type:** bounded_theorem
**Status:** proposed_retained

The finite-clock replacement for continuous Haar integration by parts is
an explicit Fourier-alias residual. A positive Gaussian-mixture identity
bounds it uniformly over all neighboring link values, even frustrated ones.
The same identity gives a lattice-wide absolute comparison for integer
Wilson characters with controlled link frequencies.

These are proposed analytic results, pending independent review and formal
audit. The estimates supply a bridge when clock order grows; they do not
prove that the residual is irrelevant at fixed order. No axiom, primitive,
native law or principal-flux Hamiltonian is changed.

## Status and proof obligations

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: u1_finite_clock_gauge_matter_and_controlled_tame_maxwell_bridge_bounded_theorem_note_2026-09-03
target_blocker_text: "Replace continuous Haar integration by parts by an exact finite-clock identity, and identify the error needed to transfer a controlled observable theorem."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Independently review the mixture and hybrid comparison, then prove an infrared estimate for the fixed-clock residual and physical-score connected correlations."
conditional_surface_status: "Supplied finite Villain measure with positive couplings, incidence coefficient plus or minus one, integer bounded-frequency observables and the stated Gaussian-tail inequalities."
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "Self-contained positive-mixture, Fourier-alias and hybrid-ratio derivations with finite direct-sum challenges."
```

| Obligation | Status |
|---|---|
| Conditional Gaussian mixture | Exact completion of squares in section1 |
| Uniform Fourier and quadrature estimate | Positive mixing and explicit Gaussian alias sums in section2 |
| Discrete Ward replacement | Exact sampled derivative and explicit residual in section3 |
| Whole-lattice Wilson comparison | Positive hybrid measures and a one-step normalized ratio bound in section4 |
| High-frequency alias control | Explicit charge-N counterexample in section5 |
| Fixed-order phase and physical-score limit | Open; the displayed sufficient growing-order family is not a fixed-order theorem |

The proof has no repository theorem premises. Its finite geometry, Villain
weight and observable frequencies are supplied data. Primary literature
is context for selecting the proof obligation, not an imported phase result.

## 1. Positive conditional mixture

Let phi_b(u)=sum_{k in Z} exp[-b(u-2pi k)^2/2]. A single oriented link theta
in a finite plaquette complex has conditional weight

 P(theta)=prod_{j=1}^r phi_{b_j}(s_j theta+alpha_j), b_j>0, s_j in {+1,-1}.

Each incident plaquette must traverse this link once, with coefficient+/-1;
self-wrapping complexes with repeated incidence need separate treatment.
By evenness set c_j=s_j alpha_j, Gamma=sum_j b_j. Unwrap each factor and
write k_j=m+n_j with n_r=0. Put d_j=c_j-2pi n_j,
bar_d=Gamma^{-1}sum_j b_j d_j, and

 A_n=exp[-(1/2)sum_j b_j(d_j-bar_d)^2]>0.

Completing the square and summing m gives the EXACT identity

 P(theta)=sum_{n in Z^(r-1)} A_n phi_Gamma(theta+bar_d).

The residual quadratic form is positive definite on n_r=0, so sum_n A_n
converges. All derivatives converge locally uniformly by Gaussian tails.
For r=1 the mixture has a single term. Consequently the normalized continuous
conditional density is a positive mixture with weights A_n/sum_m A_m of
translates of a wrapped normal with precision Gamma. If p_hat(m)=(2pi)^-1 integral P(theta)e^-imtheta dtheta,

 p_hat(m)=p_hat(0) exp[-m^2/(2Gamma)] E_n[e^{im bar_d}],
 |p_hat(m)|<=p_hat(0) exp[-m^2/(2Gamma)].                 (1)

The background may be arbitrarily frustrated. No lower bound on min P and
no replacement of a random neighbor field by its mean occurs.

## 2. Uniform quadrature errors

Q_N F=N^-1 sum_{a=0}^{N-1}F(2pi a/N), Q_infty F=(2pi)^-1 integral F.
Fourier aliasing yields Q_NP=sum_{q in Z}p_hat(qN). Define

 epsilon_K(N,Gamma)=2 sum_{q>=1}exp[-(qN-K)^2/(2Gamma)], 0<=K<N.

Then |Q_NP/Q_infty P-1|<=epsilon_0. More generally, if
f(theta)=sum_{|k|<=K}f_hat(k)e^{iktheta},

 |Q_N(Pf)-Q_infty(Pf)|
 <=Q_infty P * ||f_hat||_1 * epsilon_K.                 (2)

The q=0 Fourier coefficient gives the continuous expectation exactly; for
q nonzero use |qN-k|>=|q|N-K and (1). This is an absolute error estimate,
not a relative estimate when the observable expectation is very small.

A closed geometric upper bound is obtained from q=1+n:
(qN-K)^2>=(N-K)^2+n(3N^2-2NK), n>=0. Therefore

 epsilon_K<=2 exp[-(N-K)^2/(2Gamma)]
              /[1-exp(-(3N^2-2NK)/(2Gamma))].           (3)

This bound only claims sufficiency. An r=1 translate at bar_d=0 saturates
epsilon_0 for the partition-function error.

## 3. Ward residual and its correction

Let J(theta)=-P'(theta)/P(theta). In the isotropic four-dimensional Villain
gauge model r=6 and J= sqrt(beta) sum_{p incident e} s_p Y_p, where
Y_p=-phi_beta'(dtheta_p)/(sqrt(beta) phi_beta(dtheta_p)) is the actual
bounded score. The continuous conditional Ward identity is
E_infty[f'-J f]=0. For the clock measure the numerator is Q_N[(Pf)'], hence

 E_N[f'-J f]= [sum_{q !=0} i qN (Pf)_hat(qN)] / Q_NP.   (4)

For epsilon_0<1 and f bandlimited as above,

 |E_N[f'-J f]|
 <= ||f_hat||_1 D_K/(1-epsilon_0),
 D_K=2N sum_{q>=1}q exp[-(qN-K)^2/(2Gamma)].             (5)

With rho=exp[-(3N^2-2NK)/(2Gamma)],
D_K<=2N exp[-(N-K)^2/(2Gamma)]/(1-rho)^2.
In particular |E_N J|<=D_0/(1-epsilon_0). The sign in the exact f=1
identity is E_N J= -sum_{q !=0} iqN p_hat(qN)/Q_NP.
This conditional mean need not vanish. The local correction
R_e(theta_other)=E_N[J_e|theta_other] produces the exact conditional
mean-zero variable J_e-R_e. Its existence alone is not a long-distance
Gaussian theorem. Nor may R_e simply be discarded at fixed N,beta because
it is exponentially small in N^2/beta.

For a source f not bandlimited, (4) remains exact under sufficient Fourier
summability, but (5) must be replaced by the full convolution sum. We do not
apply a finite-frequency bound to exponentials of nonlinear scores by fiat.

## 4. Full lattice comparison without a volume-exponential loss

Uncoupled integrated links compare exactly for frequencies |j_e|<N and
may be removed first. Let E be the number of remaining integrated links,
Gamma_e=sum_{p incident e}b_p, and
Gamma_*=max_e Gamma_e. Clock and U(1) models use the same positive Villain
plaquette product and normalized a priori one-link measures; no gauge fixing
is needed in finite volume. Fix or integrate boundary links consistently.
Assume Gamma_*>0 and epsilon_0(N,Gamma_*)<1. Define the E+1 hybrid measures
by replacing one link measure at a time from Haar to N-clock. The conditional
bounds are uniform over the remaining links, regardless of whether those
links are clock or continuous.

Write Z_i,A_i for unnormalized partition function and Fourier-character
numerator at hybrid i, F_j(theta)=exp[i sum_e j_e theta_e], |j_e|<=K<N.
Integrating the one changed link and then the positive measure of the rest,

 |Z_i-Z_{i-1}|<=epsilon_0 Z_{i-1},
 |A_i-A_{i-1}|<=epsilon_K Z_{i-1},
 |A_{i-1}|<=Z_{i-1}.

It follows by a one-step ratio estimate and telescoping that

 |<F_j>_clock-<F_j>_U(1)|
 <=min[2, E*(epsilon_K+epsilon_0)/(1-epsilon_0)].        (6)

The partition functions separately obey
 (1-epsilon_0)^E <=Z_clock/Z_U(1)<=(1+epsilon_0)^E.      (7)

For a finite Fourier polynomial F, sum (6) with its coefficient absolute
values. It also extends to absolutely convergent Fourier series with the
corresponding mode-dependent bound summed, when finite, using the trivial
bound2 for any mode whose link frequency is at least N. This does not
assert total-variation closeness of atomic and continuous angle measures.
Gauge-invariant integer Wilson characters are included in (6), with max
link charge K. A relative Wilson ratio still requires the absolute error
small compared with the denominator: (6) alone does not supply that.

A useful sufficient family, with delta>0 fixed, is

 N-K >= sqrt[2 Gamma_* (1+delta) log E],

provided rho is bounded away from1. Then E epsilon_K ->0 (E->infinity),
while E epsilon_0<=E epsilon_K. For example fixed Gamma_*, fixed K and
N=ceil[K+sqrt(2 Gamma_* (1+delta) log(2E))] works. At fixed beta this costs
clock order of order sqrt(log E), but transfers only those U(1) conclusions
whose observables and absolute error tolerances meet (6). It does not prove
an intrinsic continuum limit for fixed clock order.

For local force residuals (5), the extra factor N and any number of tested
links must also be included. A volume sum E D_K ->0 follows, for example,
from the same family at fixed Gamma_*,K and delta>0 because N~sqrt(log E).
The total local Fourier frequency of an observable, not merely a nominal
charge label, controls which estimate applies.

## 5. Sharp distinctions and elementary controls

For r=1, theta shift c nonzero, the conditional force generally has a
nonzero mean because the trapezoidal derivative has nonzero aliases.
At N=2,c=pi/2 the symmetry can force this mean back to zero; use a generic
shift such as c=0.37 to test it. Some symmetric backgrounds have zero mean;
there is no uniform nonzero lower bound.

At r=1,c=0, the clock expectation of e^{iN theta} is exactly1. The U(1)
expectation is exp[-N^2/(2Gamma)], which may be arbitrarily small. Thus an
unrestricted Fourier/Wilson observable comparison cannot follow from a
small epsilon_0. The K<N condition and shifted Gaussian tail matter.

A positive product of strongly concentrated factors can make min P tiny.
The mixture estimate avoids dividing by that minimum, retaining the natural
alias exponent N^2/(2Gamma). Its weakness for fixed N as E grows remains
real for this uniform telescoping proof. It is not evidence that the actual
fixed-clock Coulomb phase is absent.

## 6. Relation to the fixed-law research target

Driver1987 uses Haar integration by parts on closed-test current observables.
Equations(4)-(5) display precisely the finite-clock replacement. Its current
limit is not imported here as a theorem identifying the full photon field. The next nontrivial step is control of the connected
physical-score correlations or a renormalization argument proving the
alias operators irrelevant, not silently reinstating Haar differentiation.

Dario-Wu, Massless Phases for the Villain Model in d>=3, author PDF dated
March27,2023, section3pp16-36, maps a low-temperature rotator Coulomb gas
through a one-step Gaussian split and cluster expansion to a small gradient
perturbation of a vector Gaussian field, then studies a Helffer-Sjostrand
operator. That does not directly treat a finite-clock gauge field with both
electric and magnetic defects. Its connected-defect method is a promising
next construction, with a fresh representation and hypotheses to prove.

[Driver1987, author-hosted paper](https://mathweb.ucsd.edu/~bdriver/DRIVER/Papers/Drivers_Papers/A1-U%281%29_4-Lattice.pdf)
[Dario-Wu2023, author-hosted manuscript](https://pauldario.pages.math.cnrs.fr/webpage-of-paul-dario/Villain3D__short_version_.pdf)


## 7. Evidence and negative-claim discipline

The self-contained executable tests five finite families: four conditional
mixtures (one,two,three and six incident factors), fifteen Ward/alias cases,
three sharp one-factor alias controls, nine two-square Wilson comparisons,
and four growing-order scales. The largest direct clock sum has7^7=823543
states. Gaussian image sums and fine-grid Fourier sums are finite numerical
checks; the written Gaussian-tail argument carries the infinite-sum claim.
No thermodynamic or continuum limit is executed by the runner.

### N1 — Distinct attempted inference routes

| Honesty | Inference attempted | Finding |
|---|---|---|
| ATTEMPTED | Replace the product by one Gaussian centered at the average background | Completion of squares retains a positive mixture over relative image integers; deleting this mixture generally changes the weight. |
| ATTEMPTED | Carry over Haar integration by parts exactly | Generic shifted one-link examples have a nonzero clock mean force; equation4 is the exact replacement. |
| ATTEMPTED | Use only the zero-mode quadrature error for all Wilson frequencies | Charge N is exactly aliased to the constant on the clock and can have a tiny Haar expectation; the shifted tail is required. |
| ATTEMPTED | Turn an absolute Wilson comparison into a relative ratio estimate | Division requires a separate nonvanishing scale or an error below the denominator; this is left explicit. |
| ATTEMPTED | Infer small total variation between the two angle measures | Clock and Haar measures are atomic and continuous respectively; only the stated observable comparison is obtained. |
| ATTEMPTED | Replace a fixed-order infrared estimate by a volume-dependent clock family | The sufficient family changes clock order and is labeled accordingly; the fixed-order phase remains open. |

No route is marked ruled out by prior retained authority. These are tests
of different inference steps, not independently established physical walls.

### N2 — Dependence

The mixture identity underlies both Fourier bounds and the hybrid argument;
they are not independent proofs of a phase. The growing-order estimate is
sufficient for specific absolute observable errors. The relationships among
fixed-order irrelevance, actual-Hamiltonian phase and native-law selection
remain unknown. No failed comparison is promoted to an axiom obstruction.

### N3 — Hidden assumptions

Every plaquette containing the link uses coefficient plus or minus one;
repeated-incidence self-wrapping complexes are excluded. Couplings are
positive, and fixed or integrated boundary links are treated consistently.
The simple Ward bound assumes a Fourier polynomial with the stated degree.
An exponential of a nonlinear score has no such automatic frequency bound.
The hybrid estimate uses the same plaquette law and normalized a priori
measures at every step. It gives absolute errors, not relative Wilson ratios.

### N4 — Matching residuals

The single-link positive mixture matches the actual Villain conditional
weight, including arbitrary neighboring angles. The nonzero force controls
match the finite-clock sampling operator. The two-square gauge complex
checks actual integer boundary characters by direct link enumeration and
separate plaquette sums. It is not a simulated four-dimensional phase.
Driver's continuous-angle argument is contextual; the exact alias formula
shows which step changes. Dario-Wu's rotator theorem is not imported as a
finite-clock gauge theorem.

### N5 — Resolution

Substantive per-element, per-site, per-mode, per-block and lattice-wide
lines are printed. The finite sums execute those domains. Uniform infinite
image tails, all-background estimates and the general E-link telescoping
argument are checked and not executed; their proofs remain subject to
independent review. Finite PASS lines do not establish universal validity.

### N6 — Partial progress

The estimate can transfer a separately proved continuous-angle conclusion
when its observable degree and absolute accuracy fit the stated bound.
Fixed-order renormalization, a direct score-cumulant estimate, and exact
finite-group identities remain alternatives. The small conditional residual
has not been proved irrelevant in an infrared limit.

### N7 — Steelman

A reviewer should object that the clock order grows with the volume and
that an absolute Wilson error can be useless when its expectation is very
small. Both objections are correct and restrict the conclusion. The result
still supplies the exact finite-clock derivative residual and a uniform
comparison on its stated observable class. It does not manufacture a phase.

### N8 — Cross-cycle comparison

The earlier growing-coupling Maxwell construction used direct lattice
Gaussian estimates; this result instead bounds the finite-angle quadrature
step. The fixed-coupling image-noise distinction remains relevant to any
full-field continuum theorem. A Gaussian current-sector limit still does
not by itself identify all physical photon observables. These results are
compatible and none forces an axiom change.

## 8. Personal review status

All work and checks were performed personally without subagents. Distinct
product/mixture, derivative/Fourier, and direct-link/plaquette calculations
challenge the derivation. Independent proof review, formal audit and main
landing remain pending. The next scientific obligation is fixed-law control
of the physical score or a carrier-preserving connected-defect expansion.
