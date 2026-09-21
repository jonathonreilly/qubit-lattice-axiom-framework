---
claim_id: mobile_records_immutable_transverse_curl_limits_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "For the supplied fifteen-state cubic-lattice process, whose occupied labels carry the displayed axis or cube features and are moved unchanged by positive-floor four-site-context exchanges: every homogeneous product is invariant, the exact currents have potential gamma X cross Y, and every orbit-isotropic interior product with gamma!=0 has four transverse propagating modes and ten zero-speed modes. The finite-alphabet entropy and stationary finite-mode proofs apply; the separately restricted fully occupied fourteen-label model has four propagating and nine zero-speed modes. Uniform microscopic births beta/N give an exact evolving product and the stated fourteen-field Gaussian finite-mode limit, including empty start and the signed integrated phase on equal-per-label trajectories. The declared polar/axial label action gives full cubic covariance and generalized time reversal. The quadratic relative entropy supplies the displayed positive wave energy, flux and conditional stress identity. A finite-mode Gauss preparation is available by an explicitly ordered conditioning limit; independent births subsequently add longitudinal noise. These are conditional classical results, not an axiom-selected alphabet or clock, physical electromagnetism, a microscopic gauge constraint, a nonlinear Maxwell closure, quantum theory, Lorentz invariance or gravity."
upstream_dependencies:
  - minimal_axioms
  - mobile_records_immutable_context_exchange_acoustic_limits_bounded_theorem_note_2026-09-21
runner: scripts/mobile_records_immutable_transverse_curl_limits_2026_09_21.py
---

# Immutable record exchanges can support a transverse curl sector

**Date:** 2026-09-21  
**Type:** bounded_theorem  
**Status:** proposed_retained  
**Author support:** conditional-support; no independent audit verdict.

The supplied construction has two transverse wave polarizations while every
actual record retains its label. The waves remain available when all sites
are occupied, since occupied records can exchange places. Uniform formation
fills vacancies and contributes a separately derived noise term. The result
connects a local stochastic generator to finite-mode continuum fluctuations;
it does not identify these classical fields with physical electromagnetism.

The fourteen occupied labels, two vector-valued observables, exchange tensor,
positive floor, formation law and clock are additional choices. The result
therefore supplies a candidate mechanism to test against the framework,
not a derivation from [the minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).
In particular, no physical qubit readout with these label dynamics has been
constructed. "Maxwell-form" below refers only to the stated linear curl
sector and its carefully specified limit.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "Can immutable finite-capacity records support a transverse propagating sector with controlled fluctuations during and after formation?"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Test microscopic selection of the extra label and rate structure, and analyze correlated formation rules without assuming evolving product fluctuations."
conditional_surface_status: "Explicit local generator, full-field currents and spectrum, finite-alphabet limit proofs, uniform-formation noise, symmetry and quadratic energy identities."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Conditional classical proofs with independently reconstructed currents, complete spectra and finite-mode limit arguments; physical identifications remain open."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## 1. The supplied generator and its invariant products

On Lambda_N=(Z/NZ)^3, N>=4, use vacancy 0 and fourteen occupied labels:

| Labels | e(a) | b(a) |
|---|---|---|
| Six A labels | +/- one coordinate unit vector | 0 |
| Eight B labels | 0 | (sigma_1,sigma_2,sigma_3), each sigma_i=+/-1 |
| Vacancy | 0 | 0 |

The B feature has length sqrt(3). Rescaling it would change the formulas
below; its normalization is part of this specified model. Each site stores
at most one label. Define the symmetric vector-valued pair tensor

```
S(a,d)=(gamma/2)[e(a) cross b(d)+e(d) cross b(a)].
```

On a positive-i edge, let (l,a,d,r) be the labels at
x-e_i,x,x+e_i,x+2e_i, and put

```
h_i(l,a,d,r)=S_i(l,a)+S_i(a,r)-S_i(l,d)-S_i(d,r).
c_i=kappa+max(h_i,0), kappa>0,
    or c_i=K0+h_i/2, K0>|gamma|.
```

The generator L_N sums c_i[F(eta^edge)-F(eta)] over positive coordinate
edges. An event exchanges the two entire endpoint labels; two occupied
labels may exchange. Every parameter is fixed before N grows. The sharp
bounds are |S_i|<=|gamma|/2 and |h_i|<=2|gamma|, giving fixed positive
floors and finite ceilings for both rate implementations. For example,
central A(+e_1),A(-e_1) with both outer labels B(+,+,+) attain
h_3=2gamma.

Central exchange reverses h, so c(eta)-c(eta^edge)=h(eta). On each
periodic coordinate line,

```
sum_x h_x=sum_x [S(x-1,x)+S(x,x+2)
                  -S(x-1,x+1)-S(x+1,x+2)]=0.
```

The distance-one and distance-two sums each cancel by translation. A
homogeneous product gives equal mass to a configuration and an endpoint
swap. Its master-equation residual vanishes by this pointwise identity.
Every homogeneous product is therefore invariant, including boundary
supports as finite-volume invariant laws. Detailed balance is not asserted.
The later entropy coordinates always use full support on the active alphabet.

## 2. Exact currents and all fourteen linear fields

For probabilities p_a, including vacancy, define
X=sum_a p_a e(a), Y=sum_a p_a b(a), and Psi=gamma X cross Y.
Orient current from the left endpoint toward the right. Averaging the
four-site current under the product gives, for every species including 0,

```
J_a=gamma p_a[e(a) cross Y+X cross b(a)-2X cross Y].
```

To derive it, interchange the central endpoints in half of the product
expectation. The symmetric part of the rate cancels, leaving
2p_a[sum_d p_d S(a,d)-sum_cd p_c p_d S(c,d)], which is the displayed
formula. Both rate implementations have the same product current. In
particular sum_a J_a=0 and J_0=-2p_0 Psi.

For the fourteen independent occupied probabilities, write

```
C=diag(p)-p p^T,
H=C^(-1)=diag(1/p_a)+(1/p_0)11^T,
theta_a=log(p_a/p_0).
J_i=C grad_p Psi_i,        A_i C=C A_i^T,        A_i=D_p J_i.
```

Indeed C is the derivative of p with respect to theta, so J_i is the
theta-gradient of Psi_i and its theta-Hessian is symmetric. This proves
the full nonlinear entropy compatibility H A_i=A_i^T H in the interior.
It is not merely a balanced-state numerical identity.

A complete moment basis is rho_A,rho_B,X(3),Y(3), two A-axis occupation
imbalances, the three B pair characters sigma_i sigma_j, and the B triple
character sigma_1 sigma_2 sigma_3. These fourteen coordinates reconstruct
all occupied probabilities. For any one-site observable F, its exact
product current is

```
J_F=gamma[<F e> cross Y+X cross <F b>-2<F>X cross Y].
```

This also specifies every moment omitted from the displayed vector marginal.
In particular,

```
J_rhoA=(1-2rho_A)Psi,     J_rhoB=(1-2rho_B)Psi,
J_rho=2p_0 Psi,          rho=rho_A+rho_B.
```

At an orbit-isotropic product p_A=rho_A/6, p_B=rho_B/8, let
rho_A,rho_B>0 and p_0=1-rho_A-rho_B>0. Then X=Y=0. Only the vector fields
have nonzero linear current, and their conservation equations are

```
X_t=(gamma rho_A/3) curl Y,
Y_t=-gamma rho_B curl X.
```

For K!=0, define C_K w=K cross w. The directional current block is

```
A_XY(K) = [ 0                    -(gamma rho_A/3) C_K ]
          [ gamma rho_B C_K       0                   ].
```

Since -C_K^2=|K|^2 P_T, the **full fourteen-field** characteristic polynomial is

```
lambda^10 (lambda^2-c^2|K|^2)^2,
c^2=gamma^2 rho_A rho_B/3.
```

For gamma!=0 there are two modes in each propagation direction. The ten
zero-speed modes include the two longitudinal vector components and all
eight other fields. They are semisimple because the complete matrix is
symmetric in a positive entropy metric. At gamma=0 every speed is zero.
The one-site vector covariances are C_X=rho_A I/3, C_Y=rho_B I, C_XY=0.

The linear vector marginal is isotropic. The full nonlinear currents retain
higher moments and the lattice geometry; no closed nonlinear Maxwell system
or nonlinear continuous rotational symmetry follows from this spectrum.

## 3. Microscopic limit statements and checked hypotheses

The [immutable acoustic note](MOBILE_RECORDS_IMMUTABLE_CONTEXT_EXCHANGE_ACOUSTIC_LIMITS_BOUNDED_THEOREM_NOTE_2026-09-21.md)
proves the canonical-block, entropy and stationary martingale estimates used
here. Their hypotheses are checked anew for this alphabet: fixed finite
range, finite state set, bounded rates, positive floor on every unequal-label
swap, invariant homogeneous products, polynomial current and the entropy
compatibility above. Sorting neighboring transpositions still connects all
arrangements in a fixed count sector. A deliberately loose canonical
Poincare bound for a block of M sites is 2M^2 q^M for q active labels;
its derivation uses at most M^2 swaps and at most q^M configurations.
Thus replacing q=7 by q=15 changes constants, not the proof mechanism.

Given a C2 periodic solution of p_t+sum_i partial_i J_i(p)=0 on fixed [0,T],
all fifteen probabilities bounded below, initial relative entropy o(N^3)
against its sampled product profile remains o(N^3), uniformly in time.
The empirical species profiles converge weakly at fixed times. Uniform
per-label microscopic births beta/N add source beta p_0 to each occupied
species and retain this conditional smooth-profile result. The absolute
entropy budget changes from N^3 log15 to N^3(log15+beta T). No global
existence or post-shock result is asserted.

For a fixed stationary interior product without births, put

```
Y_N(K,t)=N^(-3/2) sum_x exp(-i K.x/N)[xi_x(t)-p],
K=2pi m, m in Z^3 fixed,
```

on macroscopic generator N L_N. The full fourteen-component field satisfies

```
sup_(t<=T) E|Y_N(K,t)-exp(-i A(K,p)t)Y_N(K,0)|^2 -> 0.
```

The supremum is outside expectation. To spell out the finite-alphabet step,
use a cube of side ell, M=ell^3 sites, and average current only over anchors
whose entire support lies inside it. Canonical centering and block overlaps
give inverse-Dirichlet bound C M^3 15^M. The stationary forward/reversed
martingale bound gains 1/N. The slow canonical Taylor residual has squared
norm O(1/M); exact Fourier filters control averaging errors by O(ell/N).
Exchange jump brackets are O(1/N). The resulting L2 error is bounded by

```
C_(T,K,p)[N^(-1/2)+ell/N+M^(-1/2)+sqrt(M^3 15^M/N)].
```

Choose ell tending to infinity with ell^3<=log N/(2 log15). The error
vanishes. The product initial CLT then gives joint Gaussian limits for
finitely many fixed modes and times, including the corresponding cross-mode
conjugacy rules. For example,

```
E[X_K(t) X_K(0)^*] -> (rho_A/3)[P_L+cos(c|K|t)P_T].
```

The longitudinal term has been retained. Parameters, product, horizon and
mode list are fixed before N grows; this proves neither damping at fixed
lattice wave number nor propagation for arbitrarily long times at fixed N.

At exactly p_0=0, restrict the generator to its fourteen occupied labels.
If each has positive probability, this is a full-support product on that
smaller alphabet. Choose one occupied label as reference, giving thirteen
independent probabilities q and nonsingular metric
H_13=diag(1/q_a)+11^T/p_ref. Product balance and current compatibility
survive; use count-sector bound 2M^2 14^M. The same conservative proofs
apply directly. The spectrum is

```
lambda^9 [lambda^2-gamma^2 rho_A(1-rho_A)|K|^2/3]^2.
```

There are four propagating and nine static modes. This is a theorem about
a restricted model, not an interchange with a singular vacancy-density
limit. At equal occupied probabilities, c=2|gamma|/7.

## 4. Declared polar/axial symmetry and generalized time reversal

The proper cubic rotations preserve both label sets. For full signed
coordinate symmetry declare, explicitly,

```
e -> R e,     b -> det(R) R b.
```

The six A and eight B labels are closed under this action, which respects
composition of signed permutation matrices. The cross product then gives
S(Ra,Rd)=R S(a,d). A negative transformed edge direction also reverses the
four-site word; these two orientation changes give covariance of the actual
rate. If instead both features are treated as polar, improper rotations
supply an extra determinant and that claimed covariance would fail. The
polar/axial assignment is supplied structure, not a derived interpretation
of the framework's qubit orientations.

Let Theta fix e and flip b. Then h(Theta eta)=-h(eta)=h(eta^edge).
For homogeneous products the exchange adjoint reverses each edge rate, and
the global identity sum_edges h=0 also matches total escape rates. Hence

```
L_N^*=Theta L_N Theta.
```

For a Theta-invariant stationary product, its path law equals the law of
the Theta-transformed reversed path, including waiting times. Ordinary
detailed balance is generally false. Theta compares different histories;
it is not an actual event that rewrites a record during forward evolution.
The full moment basis has Y and the B triple character odd under Theta;
its linear current matrix obeys T A(K) T=-A(K).

## 5. Exact uniform formation law and its Gaussian noise

Add independent vacancy-to-a births, each at microscopic rate beta/N,
beta>0. A birth creates a record only at vacancy. For every homogeneous
initial product, the exact finite-volume law remains the product with

```
p_0(t)=v0 exp(-14 beta t),
p_a(t)=p_a(0)+[v0-p_0(t)]/14.
```

Exchange annihilates each product on this curve and births supply its time
derivative, so the finite forward equation proves the identity. Generator
semigroups need not commute. This identity does not hold for the previously
studied neighbor-dependent formation mechanism.

For a fixed interior initial product, the full fourteen-species fluctuation
limit on fixed finite modes and times is

```
dY_K=[-i A(K,p(t))-beta 11^T]Y_K dt
                         +sqrt(beta p_0(t)) dW_K.
```

Here E[dW_K dW_L^*]=I delta_(K,L)dt,
E[dW_K dW_L^T]=I delta_(K,-L)dt; opposite modes are conjugates and the zero
mode is real. The initial Gaussian has covariance C(p(0)) and is independent
of the new noise. Birth-event counts fluctuate, so the noise is beta p_0 I,
not the covariance of a fixed number of categorical draws.

The nonstationary replacement needs an argument beyond the stationary
martingale shortcut. On an interval [a,b], solve the finite backward problem
(partial_t+G_N)u_t=-F_t, u_b=0, using the actual evolving law mu_t. Its exact
energy identity is

```
d/dt E_mu |u_t|^2 = 2 Re E_mu[conj(u_t)(partial_t+G_N)u_t]
                                           +E_mu Gamma_G(u_t).
```

The squared norm of integral F_t(eta_t)dt equals
E|u_a|^2+integral E Gamma=2 Re integral <u,F>. If
|<F,h>|<=a_t sqrt(E_0(h)) and the exchange floor gives
E Gamma>=2N c_* E_0, Cauchy-Schwarz yields

```
E|integral_a^b F_t(eta_t)dt|^2 <= (2/(N c_*)) integral_a^b a_t^2 dt.
```

At every time the exact product has uniform conditional arrangements given
block counts. The same canonical comparison therefore gives
 a_t^2<=C M^3 15^M for its centered current residual. Polynomial Taylor
bounds and exact Fourier filters handle the other terms. This proves the
current replacement under the evolving law. Using a stationary weighted
adjoint without its time-dependent score would invalidate this step.

A species-a birth at x has Fourier jump exp(-i K.x/N)/sqrt(N^3), and its
exact bracket with conjugated species-d mode L is

```
d<M_a(K),conj(M_d(L))> = delta_(a,d) (beta/N^3)
                  sum_x exp[-i(K-L).x/N] 1_(eta_x=0) dt.
```

At each time the spatial product variance is O(N^-3); its integrated
fluctuation thus vanishes without assuming temporal mixing. Jumps vanish
as N^-3/2. The finite-dimensional compensated-exponential martingale
argument yields the Gaussian noise, jointly independent of initial fields.
Exchange martingales vanish at this scale. With Phi_K the fundamental
matrix of the displayed drift, the precise prelimit approximation is

```
Z_N(K,t)=Phi_K(t,0)Y_N(K,0)+integral_0^t Phi_K(t,s)dM_N^birth(K,s),
sup_(t<=T) E|Y_N(K,t)-Z_N(K,t)|^2 -> 0.
```

Martingale isometry and this L2 estimate also yield the covariance limit,
not just convergence in distribution. The normalization is checked by

```
C'=D_K C+C D_K^*+beta p_0 I,
E[Y_K(t)Y_K(s)^*]=Phi_K(t,s)C(s),       t>=s.
```

The orbit-isotropic vector noises are Q_X=2beta p_0 I,
Q_Y=8beta p_0 I, Q_XY=0. The other fields remain in the theorem. For example,
total density has drift -14beta and noise14beta p_0; the orbit contrast
4rho_A-3rho_B has zero drift and noise168beta p_0. A quadrupoles and B
pair/triple characters have zero leading drift but nonzero formation noise.

For equal occupied-label probabilities p_a=rho/14, let U=2X,V=Y. Then

```
rho=1-v0 exp(-14beta t),
U_t=c_signed(t) curl V,   V_t=-c_signed(t) curl U,
c_signed(t)=2gamma rho(t)/7,
Q_U=Q_V=8beta p_0 I,      Cov(U)=Cov(V)=4rho(t)I/7.
```

The drift matrices commute on this special trajectory. Its signed phase is

```
theta_K(t,s)=(2gamma|K|/7)
       [(t-s)-v0(exp(-14beta s)-exp(-14beta t))/(14beta)].
```

Writing L=P_L+cos(theta_K)P_T, the vector propagator has diagonal blocks L,
upper-right i sin(theta_K)C_K/|K|, and its negative in the lower-left.
The two-time covariance equals that propagator times4rho(s)/7. These
formulas include longitudinal noise; a static longitudinal drift is not a
noiseless field. Unequal initial orbit ratios generally give noncommuting
matrices and require the time-ordered propagator. At beta=0 use the
continuous constant-density phase; gamma=0 gives zero phase.

For completely empty initial state, the field at t=0 is deterministic zero
and the exact product is interior at every fixed delta>0. Apply the interior
theorem from delta to any fixed finite list of later times. The product CLT
at delta and the covariance identity give results independent of that
chosen delta, and the limiting continuous-coefficient SDE can start at zero.
For the stronger L2 approximation across [0,T], use that the backward-energy
identity divides by no reference probability. Its canonical-sector bounds
and polynomial fourth-moment bounds are uniform on the closed simplex.
Alternatively the centered-current integral on [0,delta] is bounded in L2
by C delta, while initial covariance and birth bracket there are O(delta).
Then take N to infinity at fixed delta and delta to zero. Neither route
substitutes a singular entropy inverse into an interior theorem.

Empty-start randomness is supplied by formation noise. The early phase is
2gamma beta |K|t^2+O(t^3); the late speed tends to2|gamma|/7. These are
properties of the continuum limit taken first on each fixed time interval,
not eternal undamped propagation on a fixed finite stochastic lattice.

## 6. Positive wave energy, flux and the limits of the stress analogy

Let h(p)=sum_(a including 0) p_a log p_a. Its entropy flux is
q_i=theta.J_i-Psi_i: differentiating gives dq_i=theta.dJ_i because
J_i=C grad_p Psi_i. Thus smooth conservative Euler solutions satisfy
h_t+div q=0. Subtract the affine tangent at an orbit-isotropic product pbar
to obtain a nonnegative relative entropy and relative flux
(theta-thetabar).J-Psi.

For a smooth one-parameter solution with first-order perturbations only
X,Y, the quadratic relative entropy and its flux are

```
E_wave=3|X|^2/(2rho_A)+|Y|^2/(2rho_B),
S_wave=gamma X cross Y,
partial_t E_wave+div S_wave=0.
```

All eight other field directions also have positive quadratic entropy;
this equation concerns the vector sector. It follows either by expanding
the exact entropy flux or directly from the two curl equations. Normalize
E=X/sqrt(rho_A/3), B=Y/sqrt(rho_B) and c=gamma sqrt(rho_A rho_B/3).
Then E_wave=(|E|^2+|B|^2)/2 and S_wave=c E cross B.
For gamma!=0, define momentum P=E cross B/c and
T_ij=E_wave delta_ij-E_iE_j-B_iB_j. The exact linear identity is

```
partial_t P_i+partial_j T_ij=-E_i div E-B_i div B.
```

It is source free when both Gauss constraints hold. Those constraints have
not been imposed on the unconditioned product ensemble.

There is also a precise second-order record-transport relation. Expand a
smooth conservative solution as p=pbar+epsilon p1+epsilon^2 p2+... without
factorials and take p1 in the vector sector. From the exact orbit and total
currents above,

```
partial_t[rho_A^(2)-(1-2rhobar_A)E_wave]=0,
partial_t[rho_B^(2)-(1-2rhobar_B)E_wave]=0,
partial_t[rho^(2)-2pbar_0 E_wave]=0.
```

These quantities retain arbitrary initial spatial offsets; the result does
not equate total record count with wave energy. Other moment perturbations
are generally generated at second order. The positive energy here is a
functional of probability profiles, not an additive immutable energy
assigned to each microscopic label, and no physical stress-energy coupling
has been supplied.

## 7. A finite-mode Gauss preparation and the effect of later births

At a fixed stationary interior background use the normalized E,B above.
Select finitely many nonzero Fourier modes, one from each conjugate pair.
Their longitudinal coordinates K.E_K/|K| and K.B_K/|K| have nondegenerate
Gaussian real and imaginary parts in the product CLT. Condition the initial
microscopic product on all these real coordinates lying in [-epsilon,epsilon],
for fixed epsilon>0. Denote the event by A_(N,epsilon).
Its probability tends to a positive Gaussian box probability p_epsilon.

The conditioned path law has density1_A/pi(A) against the original path
law, so every nonnegative squared propagation remainder is bounded in
expectation by its unconditioned value divided by pi(A). The stationary
L2 approximation therefore transfers at fixed epsilon. The joint initial
CLT also transfers because the box boundary has zero limiting probability.
Its intermediate limit is a truncated Gaussian, not generally Gaussian.

Now send epsilon down to zero **after** N tends to infinity. Longitudinal
and transverse coordinates are independent in the isotropic Gaussian.
The former become zero, while transverse covariances remain P_T. The
resulting Gaussian vector sector satisfies the Gauss constraints at all
fixed observation times and has the same propagator with the longitudinal
covariance removed. All eight additional static fields remain present.
The conditioning entropy cost is -log pi(A), bounded in N at fixed epsilon.
This is an available preparation, not a mechanism selecting it. No uniform
bound for a simultaneous epsilon_N limit or conditioning all lattice modes
has been established. The fully occupied restricted theorem gives the same
construction with seven other static fields.

Independent uniform births change this conclusion during formation. On
the equal-per-label trajectory, prepare U=2X,V=Y with zero selected
longitudinal modes at a fixed positive time s. Applying the same bounded
conditioning to the growing limit and then epsilon->0 gives, for t>=s,

```
Var(K.U_K(t)/|K|)=Var(K.V_K(t)/|K|)
             =integral_s^t 8beta p_0(u)du
             =(4/7)[rho(t)-rho(s)].
```

The field is therefore driven longitudinally while independent births
continue. This is a property of this supplied rule, not a classification
of other formation mechanisms or charge sectors.

## 8. Evidence and remaining physical choices

The canonical runner executes the attached author controls on copied
sources in a temporary directory, records their complete results, and
provides explicit mutations of rate/current, normalization, parity, energy
and noise formulas. These finite controls support identities; the limit
statements rest on the proofs and the stated hypotheses.

The separate reconstruction of the generator, complete currents, spectrum,
finite-alphabet proofs, full-occupancy restriction, uniform birth noise and
empty-start extension was sealed before primary sources were accessed.
Its report SHA is
`9de24aa5265ec720e24f8ce0d95b34fa7760d1112baed3cbca7cb05e44689dcf`;
seal SHA is
`35138e3ac676833b4a4764225853fca20828956928bf734b92baa271ff7856c3`.
It retains all three checker attempts and a corrected bookkeeping failure.
The two failed checker attempts were exact-zero simplification issues;
the repaired checks did not change any scientific target. Raw sealed
capsules and their mathematical dependencies are attached, with portable
byte verification. The original both-polar parity counterexample and the
author's failed development controls are also preserved.

Parity extension, quadratic energy and the finite-mode conditioning argument
are additions to that pre-source reconstruction and require final-source
review on their own arguments. They must not be described as part of its
blind reconstruction. Formal retained status still requires independent audit.

Lattice-Boltzmann Maxwell solvers already use enlarged population sets and
antisymmetric field structures; examples include Mendoza and Munoz,
[arXiv:0806.2678](https://arxiv.org/abs/0806.2678), and Hanasoge, Succi and
Orszag, [arXiv:1108.2651](https://arxiv.org/abs/1108.2651). Their constructions
are methodological context, not proofs of this stochastic generator or a
novelty comparison. The present distinction is the specified immutable-label
exchange process and the particular conditional limit proved here.

Physical questions remain open: why this record menu and tensor, how a
qubit dynamics realizes them, what fixes the clock and field units, how
charges and Gauss constraints arise, and how the extra static modes and
nonlinear currents behave. The demonstrated wave mechanism does not by
itself answer those questions or establish a TOE.
