---
claim_id: small_contrast_cochain_gibbs_state_matching_and_spectral_homogenization_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "For the specified small, summably local cochain interactions and free-cube preconditioners, uniform-root finite Gibbs averages converge to a spatially mixing Gaussian-noise factor, inherit the cubic Gaussian remainder through a two-replica argument, and have a covariance whose low-frequency first block is kappa times the continuum coexact projection under full signed-permutation symmetry."
upstream_dependencies:
  - preconditioned_extended_gradient_gaussian_remainder_and_free_cubic_riesz_bounded_theorem_note_2026-09-15
runner: scripts/haar_villain_fixed_coupling_full_score_2026_09_15.py
---

# Thermodynamic matching and spectral homogenization for small cochain interactions

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** proposed_retained

For the specified small, summably local cochain interactions and free-cube preconditioners, uniform-root finite Gibbs averages converge to a spatially mixing Gaussian-noise factor, inherit the cubic Gaussian remainder through a two-replica argument, and have a covariance whose low-frequency first block is kappa times the continuum coexact projection under full signed-permutation symmetry.

This is an author theorem proposal. The written proof and its provisional
upstream sources await independent mathematical review and formal audit.
The supplied continuous-angle law is an explicit model input; it is not
derived from the framework axioms, and no axiom or primitive is changed.

## Status, scope and proof obligations

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: u1_finite_clock_gauge_matter_and_controlled_tame_maxwell_bridge_bounded_theorem_note_2026-09-03
target_blocker_text: "Establish a fixed-law full physical-score limit while preserving the probability law, observable and state."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Independently check this fixed-Haar proof chain, then address the separate quantized electric defects before making a finite-clock inference."
conditional_surface_status: "The explicitly supplied law, cubic exhaustion, carrier conditions and operator smallness conditions in the proof."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "A quantified analytic theorem proposal with finite challenges of distinct calculation paths; the supplied-law and independent-review boundaries remain explicit."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

The single-sentence claim above is the target contract. An auxiliary
Langevin time below is a proof parameter, distinct from all four Euclidean
coordinates. Finite calculations challenge the argument; they do not
execute an infinite-volume theorem or ratify its status.

## Imports, finite-family contract and obligation graph

Use the free-cube preconditioners and even carrier extensions from
[the Gaussian-remainder note](PRECONDITIONED_EXTENDED_GRADIENT_GAUSSIAN_REMAINDER_AND_FREE_CUBIC_RIESZ_BOUNDED_THEOREM_NOTE_2026-09-15.md), including its two explicit
provisional upstream sources. Let mu_L have density proportional to
exp[-(omega,K_L^(-1)omega)/2+R_L(omega)] on range(K_L).
Require uniform coordinate-gradient bounds, deterministic Hessian Schur
row and column bounds delta<1/2, summably vanishing spatial tails, and
bulk convergence of gradients and Hessians after truncating carrier range.
Require full signed-permutation covariance of the chosen extensions.
Section1 verifies these conditions from the stated carrier estimates.
The uniform ell3/third-influence hypotheses are used when inheriting the
Gaussian remainder, not merely for state existence.

| Obligation | Mechanism and status in this proof |
|---|---|
| Unique stationary auxiliary construction | Contraction on the Gaussian OU path probability space, section1 |
| Actual finite-Gibbs to stationary-state match | Nested cochain projections, row-tail covariance control and uniform-root limits, section2 |
| Concentration of root-dependent finite variances | Two independent replicas sharing box geometry, section3 |
| Actual covariance response formula | Finite generator integration by parts and strong product limits, section4 |
| Directional covariance limit | Spatial spectral decomposition and small-contrast resolvent, sections5-8 |
| Scalar Maxwell coefficient | Point-group symmetry after fluctuation elimination, sections9-10 |

No scalar nearest-neighbor homogenization theorem is used as a premise
for this extended vector interaction. The required spectral and Banach
fixed-point machinery is standard mathematics, with its hypotheses checked
below. The physical flux/score identification is a separate companion
proof, not a hypothesis of the present auxiliary result. Independent
review of the written state/response argument is the strongest verification
obligation still outstanding for this target.

## 1. The stationary auxiliary construction

The infinite-lattice preconditioner is explicit. Write
eta_mu(k)=exp(i k_mu)-1, lambda(k)=sum_mu|eta_mu(k)|^2,
and let d_r(k) be exterior multiplication by eta on r-forms. For k!=0,
the Koszul identity d d*+d*d=lambda I gives
Dcal(k)Dcal(k)*=diag(lambda R(k),lambda I_4),
where R(k)=d_2(k)*d_2(k)/lambda is the coexact two-form projection and
I_4 denotes the single top-form orientation, not a four-dimensional block.
Consequently the seven-component preconditioner has multiplier

 m(k)=(1-c lambda(k)) diag(R(k),1), c=1/32.

Since 0<=lambda<=16, this is positive with norm at most1 and is smooth
away from0. Its directional limit is diag(R_cont(p),1) for p!=0, because
eta(ap)/a->i p. Assign m(0)=0. Its value at that single point does not
change the deterministic ell2 operator K, but will specify its action on
invariant environment vectors.
Let N=R' be the fixed translation-covariant, point-group-symmetrized local
carrier extension. On the infinite lattice this means the absolutely
convergent coordinate-gradient interaction, not an infinite normalized
Lebesgue density or a finite-valued total potential. The required deterministic bounds are

 |DN_(i,x;j,y)|<=t_ij(y-x),
 sup_i sum_(j,z)t_ij(z)<=delta,
 sup_j sum_(i,z)t_ij(z)<=delta<1,

with summable spatial tails, and bounded coordinate N_i. R is even, so N
is odd. Large-carrier derivative tails decay exponentially in their mass.
The free-box extension must be chosen to agree with this bulk extension
for every carrier sufficiently far from the boundary.

On a stationary Gaussian OU path probability space, let zeta have
covariance exp(-|t-s|)K. The commuting spatial translations define K on
L2 of the probability space by their joint spectral calculus. This is a
bounded operator even though its pointwise kernel is not summable in ell1.

This OU/Langevin time is an auxiliary proof parameter. It is distinct
from all four Euclidean lattice coordinates and is not a new physical
time or an added microscopic update law.

For jointly stationary random fields u,v, weighted Cauchy-Schwarz and
stationarity give

 E sum_i |N_i(u)(0)-N_i(v)(0)|^2
 <=delta^2 E sum_i |u_i(0)-v_i(0)|^2.                 (M.1)

Indeed apply the row bound to each coordinate and then use the column
bound after translating y to0 inside the expectation. Therefore the map

 u_t -> zeta_t+integral_0^infinity exp(-s)K N(u_(t-s))ds       (M.2)

is a contraction on the per-site L2 space of stationary path fields.
Equivalently work with u_0 in L2 of the Gaussian path space, using time
translations to define every u_t. Picard iteration gives a unique fixed
point in this space. The iteration is odd under global noise sign reversal
and equivariant under space, time and the chosen lattice point group.

The Gaussian path field is spatially mixing: every finite-time covariance
between fixed finite spatial sets tends to0 by the Riemann-Lebesgue lemma
applied to the bounded Fourier density m. Gaussian cylinder polynomials,
and then their L2 closure, establish mixing of the path probability space.
An equivariant measurable factor preserves mixing, so the fixed point of
(M.2) is spatially mixing and ergodic.

Precisely, work in H=L2(Omega;R^7) on the OU path space. A vector u in H
generates its entire spatial configuration by U_x u and its time path by
S_t u. The local carrier derivative defines N(u) in H and (M.1) makes it
globally Lipschitz. The Bochner operator integral
integral_0^infinity exp(-s)S_(-s)K_env ds has norm at most1. Banach's
fixed-point theorem therefore applies on the complete space H. No
pointwise summation of the massless K kernel is used in this construction.
The resulting process has a continuous version: its difference from the
continuous OU process is the time convolution of a locally L2 process,
and that convolution is locally absolutely continuous in each coordinate.

For the actual carrier family, a cluster of total individual mass S has
filling support in a cube of side at most6S. The rooted mass and filling
bounds therefore bound each coordinate gradient by

 M1=2pi sqrt(beta) d C1 R_t
       sum_(S>=1) S^(d+1)exp(-tS/2)<infinity.

The Hessian bound is delta=beta epsilon_t. Terms coupling coordinates at
distance r have S at least r/10, using a loose geometric constant.
Restricting the same convergent mass sums to S>=r/10 bounds the row and
column tails. The third-influence bound is M3 from the Gaussian-remainder note.
In the infinite bulk, absolute translation-covariant carrier coefficients
give t_ij(z). Finite boundaries need the uniform Schur and tail bounds,
not a falsely translation-invariant boundary potential.

Choose the infinite filling by a translation-covariant anchor and fixed
axis order, then average the extended potential over signed permutations.
Every summand has the same restriction to compatible gradients and the
same norm bounds. In a finite cube use that filling for interior carriers
and the established relative filling for boundary carriers, and average
over cube isometries. At distance r from the boundary all terms with
S<r/10 agree with the infinite extension; the remaining gradient and
Hessian tails tend uniformly to0. This verifies the bulk interaction
contract under the provisional carrier and filling estimates.

## 2. Free-box operator and measure convergence

Embed finite free-box cochains in the infinite lattice by zero outside
their actual cells. Let K_L be the finite preconditioner, and let P_L be
the orthogonal projection Dcal_L H_L^(-1)Dcal_L*. Their norms are at most1.
For any root whose distance from every boundary face tends to infinity,
the bulk operator convergence is

 K_L -> K strongly on deterministic ell2.                    (M.3)

A simpler direct proof of (M.3) avoids a boundary Green-function asymptotic.
On a contractible free four-cube the Hodge decomposition gives exactly

 range(Dcal_L)=ker(d_1,L*) on two-cochains, direct-sum all four-cochains,
 P_L=diag(projection onto ker(d_1,L*),I_4).

Zero extension of a co-closed two-cochain preserves co-closedness: every
edge in the boundary of an included plaquette is itself an included edge,
so the infinite adjoint applied to the extension is the extension of the
finite adjoint. Likewise d_2* of an included three-cochain is supported on
its included faces. Thus the embedded projection spaces increase with
nested free boxes and are contained in the infinite compatible space.

Their union is dense in that space. To see this for a co-closed ell2
two-form, cut its Fourier transform away from0. On the remaining compact
frequency set the Koszul/Hodge identity expresses it as d_2*phi with
phi=H_3^(-1)d_2 u in ell2. Approximate phi by finitely supported three-
cochains; boundedness of d_2* preserves convergence. Remove the frequency
cutoff. Top-degree forms are approximated directly by finite support.
There is no ell2 harmonic vector at the single zero Fourier frequency.

Monotone orthogonal projections therefore give P_L->P strongly. Moreover,
if a rooted box contains the centered radius-r box, its projection lies
between P_r and P in the order of projections. For every fixed source f,

 ||(P-P_L)f||2^2=(f,(P-P_L)f)
 <=(f,(P-P_r)f)->0.

This gives the needed uniformity for every root receding from all faces.
The local operator Dcal_L Dcal_L* agrees with its infinite counterpart on
compact sources once their support is away from the boundary. Its uniform
norm bound then gives strong convergence everywhere, establishing (M.3).
Functional calculus on a common bounded spectral interval also gives
sqrt(K_L)->sqrt(K), hence convergence of the bulk OU noise. The earlier
reflection proof is still needed for ell3 bounds, but not for this ell2
thermodynamic operator limit.

For the finite Gibbs law, strong convexity on range(K_L) gives

 Cov(omega_L)<=I/(1-delta),
 Var((v,N_L(omega_L)))<=delta^2 ||v||_2^2/(1-delta).           (M.4)

The second follows from the Brascamp-Lieb inequality applied to the
function (v,N_L), whose ambient gradient norm is at most delta||v||2.
Oddness gives zero mean. Thus a row tail of K_L acting on N_L is small
in L2 whenever the deterministic row tail is small in ell2. This avoids
the invalid ell1 summation of a massless projection kernel.

Finite stationary dynamics satisfy the causal equation with OU noise,
and all coordinate drifts have bounded second moments by (M.4). On a fixed
time interval the integral of the drift has a uniformly bounded L2 time
norm; Cauchy-Schwarz gives a uniform one-half Holder modulus for that
integral outside an event of small probability. The Brownian part has
uniform variance and ordinary Gaussian path tightness. This supplies
coordinate path tightness without needing a new fourth-moment theorem.

The finite process is the actual Gibbs process: its drift is K_L times
the gradient of the log density, so integration by parts makes mu_L
invariant. Global Lipschitz continuity and synchronous contraction rate
1-delta give uniqueness. Picard iteration of the finite causal equation
on stationary OU path space also contracts in the ordinary finite-
dimensional L2 norm; its law must be mu_L. Each coordinate drift has
second moment at most2(1+delta^2)/(1-delta), and each Brownian coordinate
has variance rate at most2. These are the path-tightness estimates above.

Average the joint law of (omega_L,zeta_L) over roots chosen uniformly in
the free box. Fixed translations change this average by only a boundary
fraction, so every limit is spatially stationary. Most roots recede from
every boundary; (M.3) identifies the limiting Gaussian noise. Truncate the
spatial K row, time past, and carrier size. The local process limit passes
the truncated causal equation. Bounds (M.4), (M.3), and the carrier tail then
remove these truncations. The resulting stationary limit solves (M.2).

Explicitly, (M.4) bounds the squared L2 norm of (v,N_L) by
delta^2||v||2^2/(1-delta), uniformly in root and time. For bulk roots,
(M.3) makes the K_L row tails uniformly small in ell2; boundary-layer roots
have vanishing proportion and row norm at most1. The time integral has
total weight1 and its part before -T has norm at most exp(-T). These
bounds justify taking the local process limit before removing cutoffs.
The limiting stationary N field has covariance bounded by the same
constant on deterministic ell2, hence a bounded spectral density (apply
the inequality to trigonometric-polynomial tests). Convolution by an ell2
row of K consequently agrees in L2 with K_env from the joint spectral
calculus. This identifies the row-limit equation with the Hilbert-space
equation (M.2), without an ell1-kernel assumption.

On the possibly enlarged limiting probability space, construct the Picard
factor of its own zeta. Both solutions are jointly stationary and (M.1)
forces them to agree. This identifies the averaged free-box auxiliary
limit with the mixing Gaussian-noise factor. The argument does not yet
claim that every arbitrarily placed unaveraged free box has the same limit.

The enlarged limiting probability space need not be assumed ergodic.
Its spatial spectral calculus still has norm at most1, with invariant
mode assigned zero. Picard iteration using its zeta stays in the closed
subspace of functions of zeta. Contraction on the full stationary L2
space forces omega to equal that factor. Mixing is thus a conclusion,
not a premise imposed on an unidentified thermodynamic state.

## 3. Two replicas remove an otherwise hidden Gaussianity gap

Averaging finite measures does not automatically preserve the uniform
third-cumulant remainder. Their variances may differ, and a mixture of
Gaussians need not be Gaussian. This must not be hidden inside a limit.

For each chosen root, take two conditionally independent copies of the
finite auxiliary state and its OU noise, sharing only the deterministic
box/root geometry. Repeat the joint compactness and causal-equation proof.
Bulk convergence of the two Gaussian noise covariances makes their limit
independent copies of zeta. Uniqueness of the Picard factor then makes
the two limiting auxiliary states independent copies of the same mu.

Consequently for each fixed local test observable f with controlled
moments,

 E_root[(E_(mu_L,root) f)^2] -> (E_mu f)^2,
 E_root[E_(mu_L,root) f] -> E_mu f.                          (M.5)

Thus the root-dependent expectations concentrate in L2. For f=omega(h)^2
the uniform sub-Gaussian moment bounds justify passage from bounded tests,
and (M.5) gives concentration of the finite root-dependent variance. The
same argument applies to any finite list of compactly supported sources.

Uniform exponential moments follow from the finite-family contract:
every real linear tilt has Hessian at least1-delta on its compatible
range. The variance inequality bounds the second derivative of its log
normalization by ||h||2^2/(1-delta). Integrating twice from the centered
law gives E exp(omega(h))<=exp[||h||2^2/(2(1-delta))]. Independent copies
have the corresponding product bound before root averaging. This proves
uniform integrability for the polynomial and exponential observables in
(M.5). The exact theta family also has its stronger bound with constant1.

Now the finite bound

 exp[Var_L(omega(h))/2-epsilon(h)]
 <=E_(mu_L) exp(omega(h))
 <=exp[Var_L(omega(h))/2+epsilon(h)],
 epsilon(h)=M3 C3^3||h||_3^3/6,

passes through the root average because the variance in its exponent
concentrates and is uniformly bounded. It therefore holds for mu itself.
This closes the mixture loophole conditionally on the matching proof,
without pretending that an average of log-MGFs is the log of an average.
Finite-source approximation and the exponential bound extend the
inherited estimate to ell2-intersect-ell3 sources when needed.

## 4. Passing the source-response identity

There is a second finite-dimensional derivation, independent of source
differentiation of stochastic trajectories. On the compatible subspace
write the positive preconditioned generator

 L=-Tr(K D^2)+(omega-K N(omega)).grad,
 Q=(I+L)^(-1), A=R''(omega).

Integration by parts gives (f,Lg)_mu=E(grad f,K grad g). The Hessian
bound implies Var(f)<=E(grad f,K grad f)/(1-delta), so L has a positive
gap on centered functions. For centered linear f=(h,omega), solve Lu=f.
Finite-dimensional ellipticity on the compatible subspace and Gaussian
tails justify the following differentiated identity, or it follows first
with a positive resolvent and smooth cutoffs:

 grad(Lu)=L grad u+(I-AK)grad u.

Set v=K grad u. Constant K commutes with L acting on vector-valued
functions, hence

 (I+L-KA)v=K h,
 v=(I-K Q A)^(-1)K h.

Here ||Q||<=1 and ||A||<=delta, so the inverse has a convergent Neumann
series. A final integration by parts gives the exact covariance identity

 Cov((g,omega),(h,omega))=E(g,v).                    (M.6)

All matrices in this display act on the compatible finite subspace;
using the ambient extension gives the same K A products because K kills
the orthogonal complement. This derivation fixes the order of Q and A
and does not need an assumed infinite-volume fluctuation-response law.

The generator is self-adjoint in mu, so its stationary process is
reversible. Also Q=integral_0^infinity exp(-s)exp(-sL)ds. Expanding (M.6)
and conditioning successive ordered stationary times identifies each
term with the time-shifted Hessian product in the path-space response.
Stationarity removes the first time shift; the Markov property and
reversibility supply the remaining Q factors. Thus the generator and
path-space formulas agree term by term. This is an independent analytic
check of the load-bearing finite response representation.

In finite dimension the covariance is the mean stationary first response.
Expand it in the convergent Neumann series of K_L and the time-shifted
Hessian. Its nth term has norm at most delta^n; the tail is uniformly
summable. For any fixed term, local convergence of the path law and the
summable deterministic Hessian tails give strong convergence of its
random Hessian operators on deterministic ell2. Combine with (M.3) to pass
the finite product between finitely supported source vectors, then the
time integrals by domination. Finally remove the Neumann cutoff.

This does not approximate K in operator norm by finite-range kernels.
A random Hessian acting on a finitely supported vector has uniformly
small output tails by the deterministic column-tail bound. Its finite
entries are continuous local path functions after truncating carriers.
The Hessians therefore converge in the bounded strong-operator topology.
For a precise limiting implementation, use a joint almost-sure
representation of the convergent coordinate path laws on their countable
product of continuous-path spaces. Along a further subsequence the root
distance tends to infinity almost surely, giving strong K_L convergence
on a countable dense set and then on all ell2. Uniformly bounded strong
operators preserve convergent vectors and their finite products. This
passes each fixed-order bounded matrix element almost surely and, by
domination, in expectation. The subsequential identification is unique,
so the full uniform-root sequence has the same limit. At fixed Neumann
order first truncate the positive time increments; their exponential
weights and delta^n bound then remove that truncation.

The finite covariance/response identity requires no infinite-volume
differentiation. Start the source-perturbed finite flow at zero-source
equilibrium at time -T and differentiate its finite random integral
equation. The uniform first and second source-variation bounds from the
Gaussianity lemma justify passage by finite differences as T grows.
At zero source the base process is stationary, so its first response is
exactly the time-shifted Neumann expression used here.

This establishes the infinite covariance response identity from the
actual finite Gibbs identity. It avoids assuming that every stationary
solution of an infinite SDE has an unspecified Gibbs response formula.
The following spatial spectral decomposition therefore applies to this covariance.

## 5. Explicit Hilbert-space hypotheses

Let (Omega,P) carry commuting measure-preserving spatial translations
tau_x, x in Z^d, and a strongly continuous group of time translations
sigma_t commuting with them. Write U_x f=f composed with tau_x and
S_t f=f composed with sigma_t. The spatial action is ergodic. Let

 H=L2(Omega;C^n), P0 f=E f, Q0=I-P0.

Thus the joint spectral projection of all U_x at frequency0 is exactly
P0, acting componentwise. Time translations preserve P0 and Q0.

Let K be a deterministic self-adjoint convolution on ell2(Z^d;C^n), with
matrix multiplier m on the frequency torus. Suppose m is continuous away
from0, ||m(k)||<=1, and for every p!=0,

 m(a p) -> m0(p) as a decreases to0.                       (S.1)

Assume m0 is a matrix-valued degree-zero homogeneous function and a
projection. Set m(0)=0. This choice at a Lebesgue-null point does not
change K on deterministic ell2, but specifies its action on invariant
vectors in the environment spectral calculus.

Let A(omega) be a covariant random operator on ell2 lattice fields,

 (A F)_i(x)=sum_(j,z) a_ij(z,tau_x omega) F_j(x+z).

Suppose deterministic nonnegative t_ij(z) dominate |a_ij(z,omega)| and
have both row and column sums at most delta<1. All sums here include z.
Require their spatial tails to tend to0 uniformly in the finite indices.
This hypothesis implies absolute operator convergence of range cutoffs
and ||A||<=delta. Self-adjointness may hold in applications, but the
resolvent calculation below does not require it.

Define the bounded time-averaged operator on lattice/path fields

 B=integral_0^infinity exp(-s) S_(-s) A ds, ||B||<=delta.

The order S_(-s) A is part of the definition; multiplication by the
environment and time translation need not commute. Define the annealed
deterministic response T by its bilinear form

 (g,T h)=E (g,(I-KB)^(-1)K h),                         (S.2)

initially for finitely supported deterministic sources. The inverse
exists by the norm-convergent Neumann series and ||T||<=1/(1-delta).
Translation covariance makes T a deterministic convolution. Positivity
and symmetry are additional facts when (S.2) is a genuine Gibbs covariance.

## 6. Exact spatial fiber convention

On lattice/path fields introduce the unitary change of variables

 (V F)_x(omega)=F_x(tau_(-x)omega).

Then a direct substitution gives

 (V A V^(-1)G)_i(x)
 =sum_(j,z) a_ij(z,omega) U_z G_j(x+z).

With Fourier convention Ghat(k)=sum_x exp(-i k.x)G_x, the fiber operator
is therefore

 A(k)_ij=sum_z exp(i k.z) M_(a_ij(z)) U_z,              (S.3)

where M denotes multiplication. The operator-valued Schur estimate,
using unitary U_z and the deterministic t bound, gives ||A(k)||<=delta
for every k. The same estimate with factors |exp(i k.z)-1| proves

 ||A(k)-A(0)|| ->0 as k->0.                            (S.4)

Indeed first truncate z, where convergence is uniform, then use the row
and column tails. No mixing rate or summable environment covariance is
used in (S.4).

The same conjugation sends deterministic K to

 K(k)=integral_(frequency torus) m(k+theta) dE(theta),   (S.5)

where E is the joint spectral measure of the spatial unitaries on H.
One can justify (S.5) without summing a nonsummable kernel: approximate the
bounded multiplier m by its Fejer trigonometric approximants (whose
operator norms stay at most1), use the exact
identity for each polynomial, and take the direct-integral limit. The
joint product of Lebesgue measure in k and any finite spectral measure
in theta makes almost-everywhere convergence and bounded domination
valid after translation. Alternatively
use bounded smooth mass regularizations and their strong direct-integral
limits. Equation (S.5) specifies a measurable representative for every k.

Since V commutes with time shifts,

 B(k)=integral_0^infinity exp(-s) S_(-s) A(k) ds,
 ||B(k)-B(0)|| ->0.                                   (S.6)

Deterministic sources become constant environment vectors under V. Thus
the Fourier multiplier of (S.2) is

 That(k)=P0(I-K(k)B(k))^(-1)K(k)P0,                   (S.7)

identified as an n-by-n matrix on the constant subspace.

## 7. Strong low-frequency limit

For fixed p!=0 and any f in H, the matrix spectral calculus and bounded
convergence give

 K(a p)f -> [Kenv Q0+m0(p)P0]f,
 Kenv=integral m(theta)dE(theta), Kenv P0=0.           (S.8)

For theta!=0, continuity gives m(ap+theta)->m(theta); at theta=0 use (S.1).
All multipliers have norm at most1. The only exceptional frequency is0,
whose spectral projection was separated explicitly. The environment may
have singular continuous spectrum or other atoms; these do not spoil
pointwise convergence away from0. Spatial ergodicity is what makes the
invariant projection consist of constant vectors only.

Let Kp=Kenv Q0+m0(p)P0 and B0=B(0). Equations (S.6),(S.8), uniform boundedness,
and induction show convergence of every term in the resolvent series.
Its norm tail is at most delta^(N+1)/(1-delta), independently of a. Hence

 That(a p) -> P0(I-Kp B0)^(-1)Kp P0.                  (S.9)

This convergence is in ordinary matrix norm because the constant source
and target spaces have finite dimension n. It is a directional limit of
the full response, not just a covariance bound or a guessed tensor.

## 8. Finite effective matrix from the environment fluctuations

Solve v=(I-Kp B0)^(-1)Kp h with constant h, and write v=bar_v+tilde_v
according to P0,Q0. The fluctuation equation is

 tilde_v=Kenv Q0 B0 P0 bar_v+Kenv Q0 B0 Q0 tilde_v.

Its inverse has norm at most1/(1-delta). Eliminating tilde_v gives

 bar_v=m0(p)[h+B_eff bar_v],

 B_eff=P0 B0 P0
   +P0 B0 Q0(I-Kenv Q0 B0 Q0)^(-1)Kenv Q0 B0 P0.      (S.10)

This n-by-n matrix is independent of p, and ||B_eff||<=delta/(1-delta).
For delta<1/2 this bound directly guarantees invertibility in

 T0(p)=(I-m0(p)B_eff)^(-1)m0(p).                     (S.11)

For larger delta<1 the original Schur-complement inverse in (S.9) still
exists, but no larger regime is needed here. The second term in (S.10)
must be retained; replacing B_eff by E A discards environmental response
and also ignores the time ordering inside B0.

## 9. Four-dimensional form symmetry

In the intended application n=7: six two-form components and one four-form
component. The potential depends only on the first six coordinates, so
A and B have zero seventh row and column. Formula (S.10) has the same zero
row and column. The zero-frequency Hodge projection is block diagonal,
with first block R_cont(p)=d*Delta^(-1)d and last block1. The off-diagonal
blocks vanish by d squared=0.

Assume the joint state and extended potential are invariant under all
signed permutations of four coordinate axes. The lattice action includes
the orientation-dependent basepoint translations of reflected cells.
Those translations act trivially on constant environment vectors, so
B_eff's first block commutes with the usual action on Lambda^2(R^4).

For distinct oriented pairs I,J there is a coordinate axis belonging to
exactly one pair. Reflection of that coordinate has opposite eigenvalues
on I and J, and forces the corresponding off-diagonal matrix entry to0.
Permutations act transitively on the six pairs and force all diagonal
entries equal. This applies to a general matrix, without assuming it
symmetric. Therefore B_eff=b I on the first block. Equation (S.11) gives

 T0,first(p)=kappa R_cont(p), kappa=1/(1-b).           (S.12)

In this application all underlying lattice and time-shift operators
preserve real fields, so B_eff and b are real. The complex Fourier fibers
do not introduce a complex physical covariance coefficient.

The environment can be symmetrized only in a way that preserves its
spatial ergodicity and the physical extension. Randomly selecting a global
anisotropic orientation and averaging it is not a substitute: that label
is translation invariant. Instead symmetrize the potential itself over
the finite group before constructing its unique noise-factor state.

## 10. Continuum covariance and physical qualifications

For smooth compactly supported sources h_a(x)=a^(d/2)f(ax), the Fourier
sum converges after k=ap to the ordinary continuum transform. Uniform
boundedness of That and smooth-source Fourier tails justify passing (S.9)
inside the bilinear integral. One elementary tail bound uses repeated
finite differences of f: their ell2 norms are O(a^r), which controls the
rescaled Fourier mass outside |p|<=R uniformly as R grows. On a bounded
p region, the rescaled Fourier sums converge by Riemann sums. The point
p=0 has zero Lebesgue measure. Cell averages and orientation-basepoint
shifts have the same limit. Thus (S.9)-(S.12) identify the continuum covariance.

For the matched auxiliary Gibbs covariance T, the finite inequalities

 K_L(I+delta K_L)^(-1)<=Cov(omega_L)<=K_L

give 1/(1+delta)<=kappa<=1 after the bulk and scaling limits. Here the lower inequality follows from an explicit finite-dimensional
score identity. On Gamma let S=K_L^(-1)omega-R_L'(omega), projecting
the derivative onto Gamma. Integration by parts gives ES=0,
E[S omega^T]=I_Gamma and Cov(S)=E[K_L^(-1)-R_L'']<=K_L^(-1)+delta I.
Cauchy-Schwarz, or the Schur complement of the joint covariance of omega
and S, gives Cov(omega)>=(Cov S)^(-1)>=K_L(I+delta K_L)^(-1).
Gaussian tails justify the boundary terms. Null ambient directions are
removed before inversion.

The upper inequality is specific to the actual theta family, and has a
separate proof. Put A_phi=beta(G_3-cI), let Q be the closed integer
three-charge lattice and
Z(s)=sum_q exp[-2pi^2 beta(q,G_3q)+2pi i(q,s)].
The carrier law is the pushforward of
Theta(phi) gamma_(A_phi)(dphi)/Z(0), with
Theta(phi)=sum_q exp[-2pi^2 beta c||q||^2+2pi i(q,phi)]>0.
Poisson summation on span(Q) proves positivity. For real j, completing the
Gaussian square gives
E exp(j.phi)=exp[(j,A_phi j)/2] Z(A_phi j)/Z(0).
The ratio is positive by the same Gaussian/theta representation and at
most one by the positive symmetric q weights. Pushing forward by
beta^(-1/2)Dcal gives E exp(h.omega)<=exp[(h,K_L h)/2].
Thus Cov(omega_L)<=K_L. This proof does not assert the upper bound for
an arbitrary convex perturbation; the paired runner includes a positive
variance counterexample to that substitution.

Section3 transfers the uniform third-cumulant remainder to this state.
It and the covariance limit give joint auxiliary Gaussian convergence.
The physical full-flux map and score/image conditional law are proved in
the companion physical-observable note. No microscopic periodic-state
reflection-positivity claim is used here.

## Finite evidence and No-Go Discipline Gate

The paired runner reads no repository scientific input or package-integrity
file and writes only stdout. It constructs integer cochains, compares
independent positive Gaussian/image integrations and Poisson sums, inverts
Gaussian precision on an independently chosen compatible basis, and solves
symmetry commutants exactly. Floating errors and quadrature cutoff changes
are reported as observed comparisons, not rigorous interval certificates.
The all-volume assertions are carried by the written proof and await
independent review. One shared runner supplies the complete finite packet
for the three companion notes; no undeclared helper is required.

### N1 — Attempted inference controls

| Honesty | Attempted inference | Witness and actual conclusion |
|---|---|---|
| ATTEMPTED | Treat the auxiliary factor as a characteristic function | `three_cube` compares the original magnetic sum, Poisson comb and positive integral; the wrong-sign factor disagrees for nonclosed sources. The exact map uses a real MGF. |
| ATTEMPTED | Use the same zero-extension rule for closed charges and co-closed gradients | `nested_projection` embeds exact finite cochains: codifferentials extend, while the specified closed three-charge develops a nonzero exterior derivative. The proof uses the appropriate space. |
| ATTEMPTED | Infer diffuse-source Gaussianity from a small Hessian alone | `collective_control` has a dimension-independent non-Gaussian collective coordinate; its third-influence constant grows. The uniform third-order hypothesis is retained. |
| ATTEMPTED | Substitute the mean Hessian for the effective covariance response | `layered_checks` compares full Gaussian precision with the response and its Schur limit; the mean-Hessian shortcut has a persistent discrepancy. The fluctuation term is retained. |
| ATTEMPTED | Obtain an ergodic Gaussian limit by averaging a global anisotropic orientation | `invariant_mixture_control` has a positive fourth cumulant, computed as three times the variance of component variances. The actual proof symmetrizes the potential and constructs an ergodic factor. |
| ATTEMPTED | Infer theta upper domination from small uniform convexity | `theta_upper_hypothesis_control` gives variance greater than the Gaussian reference. The physical theta inequality is a separately derived structural fact. |
| ATTEMPTED | Count four reflected current components as photon polarizations | `image_score_and_reflection` imposes current conservation and obtains a positive rank-two projector; the unreduced time metric has a negative direction. |

These are explicit positive counterexample witnesses and proof-hypothesis
checks. None is a no-go for a physical phase or an axiom update. No route
is marked RULED OUT BY PRIOR.

### N2 — Dependencies and collapse

There is no asserted collection of independent physical walls, so the
pairwise physical-wall table is empty and the physical-wall count is zero.
The controls are not added as independent evidence of phase failure.
Source unfolding, finite cumulant control, thermodynamic identification,
replica concentration and spectral response instead form one dependent
positive proof chain. Failure of a linked input invalidates its dependents;
it does not prove a separate axiom obstruction. The two averaging controls
challenge different steps of that same state/covariance chain and are not
counted as two independent phase exclusions.

### N3 — Hidden-hypothesis scan

The law, continuous link domain, counting metric, free cubic boundaries,
integer topology, order of limits, real sources, smallness conditions and
carrier bounds are explicit. The auxiliary time is distinguished from
physical Euclidean time. Standard SDE, interpolation, spectral and Gaussian
machinery is mathematical input with checked domains, not an imported
photon phase. The source has no assumed Maxwell covariance or Gaussian
limit at a terminal step. The provisional parent proofs and independent
review requirement remain explicit. No framework primitive is introduced.

### N4 — Residual matching

| Packet witness | Residual tested | Match and limit |
|---|---|---|
| `scripts/haar_villain_fixed_coupling_full_score_2026_09_15.py:180` (`exact_hodge`), `three_cube` | Actual source, sign, Gaussian split and covariance normalization | Yes, exact finite cochains and the same normalized three-cube flux; no all-volume proof is executed |
| `scripts/haar_villain_fixed_coupling_full_score_2026_09_15.py:63` (`reflection`), `nested_projection` | Boundary incidence and compatible-space embedding | Yes, finite instances of the specified free-box construction |
| `scripts/haar_villain_fixed_coupling_full_score_2026_09_15.py:115` (`positive_integrals`), `collective_control` | Finite source derivatives and the third-influence hypothesis | Yes, positive finite measures with the stated comparison geometry |
| `scripts/haar_villain_fixed_coupling_full_score_2026_09_15.py:306` (`layered_checks`), `symmetry_commutant`, `invariant_mixture_control` | Fiber convention, fluctuation elimination and invariant sector | Yes, explicitly quadratic comparison models and exact group algebra; not simulations of the nonlinear Gibbs state |
| `scripts/haar_villain_fixed_coupling_full_score_2026_09_15.py:404` (`image_score_and_reflection`) | Local score/image normalization and conserved continuum reflection form | Yes, the supplied image kernel and exact finite momentum algebra |

No numerical witness is cited as executing the nonlinear thermodynamic
or continuum theorem. Written lemmas supply those obligations.

### N5 — Resolution and rhetoric

The primary cached stdout contains substantive per_element, per_site,
per_mode, per_block and lattice_wide certificates. Finite cochains,
quadratures, spectra and algebra are executed. Uniform Riesz estimates,
carrier expansions, state matching, ergodic averaging and continuum
reconstruction are checked and not executed; their analytic proofs are
the evidence at that resolution. No number of PASS lines supplies
independent review. The actual score's nonsummability conclusion, when
used in the companion physical theorem, follows from its nonconstant
low-frequency covariance symbol, not from a finite numerical tail fit.

### N6 — Remaining positive paths

The supplied Haar law is a concrete positive comparison route. Its finite-
clock counterpart retains quantized electric defects, which can be studied
through the exact coupled representation, its positive integer marginal,
or a direct physical-score argument. None is excluded by this theorem.
A new axiom is not requested or inferred. No primitive inadequacy claim
is made, so no primitive-registry exclusion is needed.

### N7 — Strongest objection

A hostile reviewer can correctly reject a full physical conclusion if the
carrier extension fails the uniform local bounds, if an averaged state is
misidentified, or if the source map loses a defect or noise term. The proof
therefore gives each of those steps explicitly and keeps the parent
sources in the reviewed dependency closure. The finite checks cannot settle
the remaining independent examination of the infinite-state argument.
Even a correct Haar theorem would leave finite-clock electric defects and
the native-law identification as distinct open targets. A broad TOE or
axiom-wall claim would be unsupported and is not made.

### N8 — Prior-route comparison

The parent carrier/filling argument supplied uniform convexity and exact
source control, while leaving a physical infrared limit open. This proposal
adds source-derivative control, an actual mixing-state construction,
replica concentration and spectral response. Earlier growing-coupling
constructions remove entire defect sectors by changing their parameters;
that is not used here. The image-noise distinction is retained and proved
for this Haar law. No previous failed route is promoted to an impossibility
claim, and no claim is made that this method includes finite clocks.

## Review record

All derivation and checks were performed personally without subagents.
This is an author check, not independent review, audit or main landing.
The parent f8e7219b5e79bcb271bb3c1df635ecdeeb57dbe8 and all three companion
notes form a provisional dependent chain. Hard review/landing condition:
review the needed parent content in the same frozen cumulative unit or
wait for it to land, and independently examine the complete final source.
Focused execution, mutation, cache and conformance receipts are recorded
in the branch-local handoff. Combined current-main pipeline, strict lint
and changed-evidence validation remain required at authorized integration.
