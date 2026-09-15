# Thermodynamic matching and the state-mixture problem

Personal proof design, 2026-09-15; not independently reviewed. This records
the next load-bearing steps for the covariance response design. Statements
labelled obligations are not established merely by writing a proof route.
The target remains continuous Haar-link compact U(1), not a finite clock.

## 1. Why a stationary auxiliary construction is plausible

Let K be the infinite-lattice seven-component Hodge multiplier from the
other block21 notes. It is positive with norm at most1 and has a bounded
Fourier density m(k), smooth away from0. Assign the single zero mode0.
Let N=R' be the fixed translation-covariant, point-group-symmetrized local
carrier extension. The intended deterministic bounds are

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
(2) is spatially mixing and ergodic. This constructs a candidate state; the
next steps must show it is the actual auxiliary thermodynamic limit.

## 2. Free-box convergence ingredients to prove

Embed finite free-box cochains in the infinite lattice by zero outside
their actual cells. Let K_L be the finite preconditioner, and let P_L be
the orthogonal projection Dcal_L H_L^(-1)Dcal_L*. Their norms are at most1.
For any root whose distance from every boundary face tends to infinity,
the intended bulk operator convergence is

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

Average the joint law of (omega_L,zeta_L) over roots chosen uniformly in
the free box. Fixed translations change this average by only a boundary
fraction, so every limit is spatially stationary. Most roots recede from
every boundary; (3) identifies the limiting Gaussian noise. Truncate the
spatial K row, time past, and carrier size. The local process limit passes
the truncated causal equation. Bounds(4), (3), and the carrier tail then
remove these truncations. The resulting stationary limit solves(2).

On the possibly enlarged limiting probability space, construct the Picard
factor of its own zeta. Both solutions are jointly stationary and (1)
forces them to agree. This identifies the averaged free-box auxiliary
limit with the mixing Gaussian-noise factor. The argument does not yet
claim that every arbitrarily placed unaveraged free box has the same limit.

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

Now the finite bound

 exp[Var_L(omega(h))/2-epsilon(h)]
 <=E_(mu_L) exp(omega(h))
 <=exp[Var_L(omega(h))/2+epsilon(h)],
 epsilon(h)=M3 C3^3||h||_3^3/6,

passes through the root average because the variance in its exponent
concentrates and is uniformly bounded. It therefore holds for mu itself.
This closes the mixture loophole conditionally on the matching proof,
without pretending that an average of log-MGFs is the log of an average.

## 4. Passing the source-response identity

In finite dimension the covariance is the mean stationary first response.
Expand it in the convergent Neumann series of K_L and the time-shifted
Hessian. Its nth term has norm at most delta^n; the tail is uniformly
summable. For any fixed term, local convergence of the path law and the
summable deterministic Hessian tails give strong convergence of its
random Hessian operators on deterministic ell2. Combine with(3) to pass
the finite product between finitely supported source vectors, then the
time integrals by domination. Finally remove the Neumann cutoff.

This establishes the infinite covariance response identity from the
actual finite Gibbs identity. It avoids assuming that every stationary
solution of an infinite SDE has an unspecified Gibbs response formula.
The covariance design's spatial spectral decomposition can then apply.

## 5. Recovering the physical plaquette state and image variance

The exact finite full-flux characteristic uses a Gaussian prefactor with
kernel I+c d_2* T_3 d_2 and a real MGF of omega_first with source -T_2 h.
Here T_r=(I-c H_r)^(-1) has exponentially decaying kernel by its Neumann
series and finite range of H_r. Bulk convergence and uniform exponential
moments should pass this identity to the matched auxiliary limit mu.
It uniquely specifies the corresponding averaged physical full-flux law.

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
