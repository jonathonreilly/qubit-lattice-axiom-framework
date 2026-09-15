# Thermodynamic matching through a stationary noise factor and two replicas

Personal derivation candidate, 2026-09-15; not independently reviewed.
This develops the earlier matching design into a conditional theorem under
explicit uniform finite-measure and carrier hypotheses. The argument and
its provisional upstream carrier inputs remain subject to review. The
target is continuous Haar-link compact U(1), not a finite clock.

## Finite-family contract and proposed conclusion

Use the actual free-cube preconditioners K_L on the compatible two/four-
form subspaces, and finite laws mu_L proportional to
exp[-(omega,K_L^(-1)omega)/2+R_L(omega)] on those subspaces. Assume R_L
are even C3 extensions with uniformly bounded coordinate gradients,
Hessian Schur bounds delta<1, uniformly vanishing spatial Hessian tails,
and a translation-covariant bulk interaction N=R' with the same bounds.
Require uniform bulk convergence of the coordinate gradients and their
first derivatives after truncating interaction range. The full carrier
mass expansion and local fillings supply these conditions at sufficiently
large fixed beta as explained below; their source proofs are provisional.

The proposed theorem is that uniform-root averages of mu_L converge to a
unique spatially mixing auxiliary law mu; its covariance has the stationary
response formula in the spectral lemma. Two independent replicas show
that root-dependent local expectations concentrate. Consequently a uniform
finite-family third-cumulant remainder passes to mu itself. These are
statements about this specified exhaustion, not uniqueness of every
possible Gibbs state or boundary condition.

## 1. The stationary auxiliary construction

Let K be the infinite-lattice seven-component Hodge multiplier from the
other block21 notes. It is positive with norm at most1 and has a bounded
Fourier density m(k), smooth away from0. Assign the single zero mode0.
Let N=R' be the fixed translation-covariant, point-group-symmetrized local
carrier extension. The required deterministic bounds are

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
 <=delta^2 E sum_i |u_i(0)-v_i(0)|^2.                 (1)

Indeed apply the row bound to each coordinate and then use the column
bound after translating y to0 inside the expectation. Therefore the map

 u_t -> zeta_t+integral_0^infinity exp(-s)K N(u_(t-s))ds       (2)

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
(2) is spatially mixing and ergodic.

Precisely, work in H=L2(Omega;R^7) on the OU path space. A vector u in H
generates its entire spatial configuration by U_x u and its time path by
S_t u. The local carrier derivative defines N(u) in H and(1) makes it
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
column tails. The third-influence bound is M3 from the Gaussianity note.
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

 K_L -> K strongly on deterministic ell2.                    (3)

A simpler direct proof of(3) avoids a boundary Green-function asymptotic.
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
norm bound then gives strong convergence everywhere, establishing(3).
Functional calculus on a common bounded spectral interval also gives
sqrt(K_L)->sqrt(K), hence convergence of the bulk OU noise. The earlier
reflection proof is still needed for ell3 bounds, but not for this ell2
thermodynamic operator limit.

For the finite Gibbs law, strong convexity on range(K_L) gives

 Cov(omega_L)<=I/(1-delta),
 Var((v,N_L(omega_L)))<=delta^2 ||v||_2^2/(1-delta).           (4)

The second follows from the Brascamp-Lieb inequality applied to the
function (v,N_L), whose ambient gradient norm is at most delta||v||2.
Oddness gives zero mean. Thus a row tail of K_L acting on N_L is small
in L2 whenever the deterministic row tail is small in ell2. This avoids
the invalid ell1 summation of a massless projection kernel.

Finite stationary dynamics satisfy the causal equation with OU noise,
and all coordinate drifts have bounded second moments by(4). On a fixed
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
every boundary; (3) identifies the limiting Gaussian noise. Truncate the
spatial K row, time past, and carrier size. The local process limit passes
the truncated causal equation. Bounds(4), (3), and the carrier tail then
remove these truncations. The resulting stationary limit solves(2).

Explicitly, (4) bounds the squared L2 norm of (v,N_L) by
delta^2||v||2^2/(1-delta), uniformly in root and time. For bulk roots,
(3) makes the K_L row tails uniformly small in ell2; boundary-layer roots
have vanishing proportion and row norm at most1. The time integral has
total weight1 and its part before -T has norm at most exp(-T). These
bounds justify taking the local process limit before removing cutoffs.
The limiting stationary N field has covariance bounded by the same
constant on deterministic ell2, hence a bounded spectral density (apply
the inequality to trigonometric-polynomial tests). Convolution by an ell2
row of K consequently agrees in L2 with K_env from the joint spectral
calculus. This identifies the row-limit equation with the Hilbert-space
equation(2), without an ell1-kernel assumption.

On the possibly enlarged limiting probability space, construct the Picard
factor of its own zeta. Both solutions are jointly stationary and (1)
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
 E_root[E_(mu_L,root) f] -> E_mu f.                          (5)

Thus the root-dependent expectations concentrate in L2. For f=omega(h)^2
the uniform sub-Gaussian moment bounds justify passage from bounded tests,
and(5) gives concentration of the finite root-dependent variance. The
same argument applies to any finite list of compactly supported sources.

Uniform exponential moments follow from the finite-family contract:
every real linear tilt has Hessian at least1-delta on its compatible
range. The variance inequality bounds the second derivative of its log
normalization by ||h||2^2/(1-delta). Integrating twice from the centered
law gives E exp(omega(h))<=exp[||h||2^2/(2(1-delta))]. Independent copies
have the corresponding product bound before root averaging. This proves
uniform integrability for the polynomial and exponential observables in
(5). The exact theta family also has its stronger bound with constant1.

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

 Cov((g,omega),(h,omega))=E(g,v).                    (6)

All matrices in this display act on the compatible finite subspace;
using the ambient extension gives the same K A products because K kills
the orthogonal complement. This derivation fixes the order of Q and A
and does not need an assumed infinite-volume fluctuation-response law.

The generator is self-adjoint in mu, so its stationary process is
reversible. Also Q=integral_0^infinity exp(-s)exp(-sL)ds. Expanding(6)
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
random Hessian operators on deterministic ell2. Combine with(3) to pass
the finite product between finitely supported source vectors, then the
time integrals by domination. Finally remove the Neumann cutoff.

This does not approximate K in operator norm by finite-range kernels.
A random Hessian acting on a finitely supported vector has uniformly
small output tails by the deterministic column-tail bound. Its finite
entries are continuous local path functions after truncating carriers.
The Hessians therefore converge in the bounded strong-operator topology.
Together with strong K_L convergence, this passes each finite operator
product and its bounded matrix elements in expectation. At fixed Neumann
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
The covariance design's spatial spectral decomposition can then apply.

## 5. Recovering the physical plaquette state and image variance

The exact finite full-flux characteristic uses a Gaussian prefactor with
kernel I+c d_2* T_3 d_2 and a real MGF of omega_first with source -T_2 h.
Here T_r=(I-c H_r)^(-1) has exponentially decaying kernel by its Neumann
series and finite range of H_r. Bulk convergence and uniform exponential
moments pass this identity to the matched auxiliary limit mu.
It uniquely specifies the corresponding averaged physical full-flux law.

The finite T_L operators have norms at most2 on ell2 and ell3. Their
Neumann series have finite-range terms with a geometric tail, giving
uniform strong bulk convergence for compact sources. The centered MGF
bound controls a residual source tail by Cauchy-Schwarz and the mean-
value formula for exponentials. The Gaussian prefactor converges by the
same local series. Every physical finite flux law has centered MGF at
most exp(||h||2^2/2), so its root averages are locally tight and uniformly
integrable. Their limiting characteristic functions are the formula
specified by mu, making the physical local flux limit unique.

Mixing of mu then gives mixing of this full-flux law. For sources h and
a distant translate of g, the Gaussian cross prefactor tends to zero.
The two exponential auxiliary observables decorrelate by mixing after
truncating the exponentially localized T sources. Uniform MGF bounds
control the truncation in L2. Characteristic cylinder observables generate
the local sigma fields, extending this to ordinary mixing.

The plaquette angle is exactly X_p/sqrt(beta) modulo2pi. Its law and the
physical score Y_p, a bounded smooth periodic function of that angle,
are therefore factors of the matched full-flux law. The conditional image
kernel is a product at finite volume and depends only on these plaquette
angles; its finite-dimensional conditional identities pass to the limit.
The mixing plaquette state makes the spatial image-variance average a
constant. This is a stronger route than inferring angle ergodicity merely
from auxiliary ergodicity without an observable map.

Combining the Gaussian remainder, covariance response and symmetry would
give auxiliary covariance kappa R_cont with

 1/(1+delta)<=kappa<=1.

The lower bound follows by the finite Cramer-Rao/score inequality
Cov(omega_L)>=K_L(I+delta K_L)^(-1) on the compatible range, and the upper
bound is the exact theta MGF domination Cov(omega_L)<=K_L. They pass to
the bulk and low-frequency limits. Full flux would then have covariance
I-kappa R_cont, and the score would have covariance
(1-kappa-vbar)I+kappa P_cont, with nonnegative contact coefficient.
Each implication remains conditional until its matching steps are proved.

## 6. Reflection positivity and periodic topology remain separate

The root-averaged free-box state does not inherit reflection positivity
just because a centered free box is reflection positive. Translating a
finite box changes its boundary relative to the reflection plane. This
is a separate microscopic state-matching obligation.

It is not necessary for reconstructing the identified Gaussian limit:
if the full score limit has covariance aI+kappa P_cont with a>=0 and
kappa>0, reflection positivity of that continuum Gaussian is checked
directly. The white contact term vanishes between strictly positive-time
tests and their reflections, and the Maxwell reflection kernel gives the
two transverse polarizations. Thus the fixed-law continuum reconstruction
can use the direct Gaussian check. It must not be described as a proof
that every microscopic state or the specified clock Hamiltonian has the
same reflection-positive phase.

A possible route is to match reflection-positive periodic Haar-Villain
states to the same auxiliary limit. Periodic winding charges have carriers
of mass at least order L; a convergent carrier expansion may bound their
effect. But the harmonic two-form fluxes are also present, and their
integer Gaussian weights depend on the charge-dependent harmonic coset.
They cannot simply be discarded as an exponentially rare defect.

For a periodic integer lift k, its orthogonal harmonic component has six
unit-normalized coordinates z+alpha(q), z in Z^6, while its nonclosed part
is d_2*G_3 q. Summing z produces

 theta_harm(alpha(q))=sum_(z in Z^6)exp[-2pi^2 beta|z+alpha(q)|^2].

This is a bounded but generally nonconstant global weight. Poisson
summation introduces dual harmonic integers ell with weights
exp[-|ell|^2/(2beta)] and charge characters exp[2pi i ell.alpha(q)].
For locally filled charges those characters shift the extended gradient
potential by a uniform first-block field of order ell/(sqrt(beta)L^2).
For each fixed ell this shift vanishes per site, suggesting a contraction
comparison. The ell-tail, positivity, and actual physical observable
identity all require proof. A uniform character bound gives one possible
tail control; it does not itself identify the tilted state.

Keep this additional topology/state step open until it is addressed.
The present design still needs its matching and Gaussian convergence
proofs before a fixed-beta continuum photon conclusion is warranted.
Finite-clock phase, native law, matter, gravity and TOE closure remain
outside the result.
