# Immutable directional exchange: a positive transport continuation

Primary working derivation, 2026-09-21. Not audited, not a hydrodynamic-limit
claim, and not an adopted primitive. The purpose is to test a concrete escape
from vacancy-only freezing without changing the content of any record.

## Supplied model and provenance

Use a cubic torus of side L>=3 or Z^3. The six contents are v_a in
{+e1,-e1,+e2,-e2,+e3,-e3}; vacancies carry v_0=0. Each occupied record has a
rate-one clock. At its event it moves one step in its own content direction,
exchanging record identities with the occupant if the target is occupied.
The moved contents are unchanged. An exchange between equal contents is
invisible to the content configuration but still moves the two tags. This is
an explicitly supplied interpretation of content as travel direction and an
explicit stochastic time law. It is the streaming part of nearby PR #8550,
without its content-redrawing collision or body rules.

For a bond (x,x+e_i) with endpoint contents a,b, the exchange rate is
c_i(a,b)=1_{a=+i}+1_{b=-i}. Values involving a vacancy use neither indicator.
Thus c_i(a,b)-c_i(b,a)=v_a,i-v_b,i. The model is a special nonnegative-rate
member, bond direction by bond direction, of the multispecies particle-exchange
family with drift-difference antisymmetric rates. The exact current algebra is
standard, rather than a new general exclusion-process theory. Relevant primary
source: Schuetz and Zahra, arXiv:2605.07615v1, sections 2 and 3, especially
(2.8), (2.15), (2.16). The paper treats one spatial dimension and uses a
hydrodynamic framework as motivation; no three-dimensional hydrodynamic theorem
or irreducibility conclusion is imported here. Some of our rates vanish.
Source: https://arxiv.org/abs/2605.07615v1

## Exact stationary laws and continuing activity

On a finite torus, temporarily label all records. The event map for a specified
record is a bijection on the finite set of allowed placements: its inverse
moves that record one step in the opposite direction and exchanges with the
occupant. Consequently uniform placement at fixed labeled contents is invariant
under each record's clock separately. Projecting out tags gives uniform weight
on each fixed-content-count sector; summing sectors gives every homogeneous
product law, with arbitrary probabilities p_0,p_1,...,p_6 summing to one.
This does not prove that a count sector is irreducible or that these are all
stationary measures. Bounded local clocks and finite propagation carry the
product-invariance statement to Z^3.

Each tag has its own rate-one Poisson events, every one of which changes its
position even at full occupancy. Hence it makes infinitely many jumps almost
surely. This is not necessarily unbounded displacement, ballistic motion, or
visible color changes at every site. For a uniform single-color full state,
all content observables are constant while tags move. Tag identity is explicit
bookkeeping, and its physical observability is not assumed.

One may additionally supply uniform vacancy insertion at rate epsilon for each
content. From homogeneous product data, the exact time-dependent product law is

p_0(t)=p_0(0) exp(-6 epsilon t),
p_a(t)=p_a(0)+p_0(0)[1-exp(-6 epsilon t)]/6.

Indeed the exchange adjoint annihilates the product law at every parameter p;
the independent insertion generator supplies its displayed derivative. This
proves the finite-torus forward equation, and then the local infinite-volume
limit. With epsilon>0 each translation-invariant site's expected total births
remain p_0(0), but record motion continues as vacancies disappear. Repeated
formation and perpetual record mobility are distinct resource questions.

## Exact homogeneous product currents

Across the positive-i bond, count a species-a rightward minus leftward crossing
for every exchange. Under an arbitrary endpoint product law p at x and q at y,
its expected current is

j_a,i(p,q)=1_{a=+i} p_a - 1_{a=-i} q_a - p_{+i} q_a + q_{-i} p_a.

The four terms also cancel correctly for equal-content exchanges. For p=q,
write rho=sum_a p_a and g=sum_a p_a v_a. The current vectors become

J_a=p_a(v_a-g),
J_number=(1-rho)g,
J_content=sum_a p_a v_a tensor v_a - g tensor g.

All six content counts are separately conserved by exchange. Number and the
three vector components retain only four combinations. The two independent
axis-population differences are additional conserved densities. No collision
relaxes them in this stipulated immutable-content process.

## Exact finite-time correlation sum rules without a closure

With formation switched off, start in an interior homogeneous stationary
product law. Put C=diag(p)-p p^T and
S_ab(x,t)=Cov(n_a(x,t),n_b(0,0)), with time order as written. Conservation and
the current identity imply the exact finite-time sum rules on Z^3

sum_x S(x,t)=C,
sum_x x_i S(x,t)=t A_i C,       A_i=partial J_i/partial p.

For clarity, these are separate from the hydrodynamic closure below. The
continuity equation gives the derivative of the first spatial moment as
sum_x Cov(j_a,i(x,t),n_b(0,0)). Translation turns this into
sum_y Cov(j_a,i(0,t),n_b(y,0)). Conservation allows the summed density to be
evaluated at time t instead. Product stationarity then gives
sum_y Cov(j_a,i(0,0),n_b(y,0))=sum_c (partial J_a,i/partial p_c) C_cb.
The final equality follows either by differentiating product expectations
with respect to the b fugacity, or directly from the two-site current.
The initial first spatial moment is zero. At each fixed finite time, all
these sums and manipulations are justified by the factorial spatial tail of
bounded-range graphical dependence. One can first sum over a finite box;
the boundary-current covariance tends to zero as the box grows. No infinite
total-particle random variable is subtracted.

For any fixed normal n, A(n)C is symmetric and C is positive definite. Choose
R with R C R^T=I and R A(n) R^-1 diagonal. The diagonal mode autocorrelations
then have integrated mass one and first moment along n equal to their
characteristic velocity times t, exactly for every finite t. These signed
correlations need not be positive probability densities, narrow peaks or
propagating poles. The identity establishes their centers of mass, not their
widths, damping, or Euler-scale limits. This is the standard conservation-law
current/correlation sum-rule mechanism applied to the present rates.

## The conditional Euler system and its entropy symmetrizer

If local equilibrium replacement is valid, the candidate leading transport
system is partial_t p_a+div[p_a(v_a-g)]=0. This conditional PDE uses the exact
stationary current, but deriving its hydrodynamic limit from the stochastic
process is an open obligation here. Time-dependent inhomogeneous product laws
are not generally exact solutions of the microscopic process.

For a wave normal n, put q_a=v_a dot n, u=sum p_a q_a. Its flux Jacobian is

A(n)=diag(q-u)-p q^T.

For strictly positive p_a and p_0=1-rho>0, let

H=diag(1/p_a)+(1/p_0)11^T.

It is the Hessian of sum_a p_a log p_a+p_0 log p_0, hence positive definite.
A direct multiplication gives

H A=diag[(q_a-u)/p_a]-(u/p_0)11^T,

which is symmetric. Thus the conditional PDE is symmetrizable hyperbolic in
the interior. This identifies real characteristic speeds and a convex entropy;
it does not prove the microscopic replacement step or a physical light cone.

## Isotropic reference composition has several transport branches

At p_a=rho/6, 0<rho<1, g=0. For wavevector k,
A(k)=(I-(rho/6)11^T) diag(kx,-kx,ky,-ky,kz,-kz).
For generic nonzero, distinct squared components, its six roots satisfy

1-(rho/3) sum_i k_i^2/(k_i^2-omega^2)=0.

This rational expression must be used after clearing denominators; degenerate
poles cannot be discarded. Along a lattice axis the eigenvalues are
+/-sqrt(1-rho/3)|k| and four zeros. Along a body diagonal, they are
+/-|k|/sqrt(3), each twice, and +/-sqrt((1-rho)/3)|k|, each once.
These are eigenvalues of the conditional six-field PDE, not established
stochastic spectral poles. Their directional differences persist in its
leading long-wavelength symbol.

For an initial isotropic composition density perturbation, delta p_a=delta rho/6,
the axis-directed conditional Euler density response is

G_axis(k,t)=2/(3-rho)+(1-rho)/(3-rho) cos(sqrt(1-rho/3)|k|t).

Along a body diagonal that same perturbation excites the acoustic pair only,
with G_diag(k,t)=cos(sqrt((1-rho)/3)|k|t). Therefore a single scalar sound-speed
fit would discard modes and direction dependence for this immutable model.
These formulas concern the conditional Euler system and small perturbations
about an interior state, not an exact finite-density microscopic propagator.

## Exact one-record control and finite-wavevector linearization

For a single uniformly chosen content, the exact Fourier density propagator is

G_1(k,t)=(1/3) sum_i exp[(cos k_i-1)t] cos[t sin k_i].

It follows by averaging the characteristic functions of six rate-one directed
Poisson walks. It has damped oscillations without content-redrawing collisions.
This does not imply a single acoustic field or coherent quantum propagation.
For small k and time of order 1/|k| it tends to six ballistic beams; the axis
and body-diagonal responses differ even in this exact dilute control.

There is a useful but separate product-closure check at finite wavevector.
Writing D_a=exp(-i k dot v_a)-1 and Omega=2 sum_i(1-cos k_i), linearization
of the endpoint-product current equation about p_a=rho/6 gives

M(k)=diag(D)-(rho/6) Omega I-(rho/6)1 D^T.

The exact derivative at t=0 for an initially perturbed product law agrees with
this matrix. Repeated use of M at later times is a closure assumption. Its
leading term is -i A(k), which checks the signs of the Euler symbol above.

## Primary checks and remaining obligations

The first complete primary run passed: 52,650 event-map inverse checks for
three labeled records on a side-three cubic torus; all 2,401 states of a
four-site periodic x-direction generator; the same number of biased product
insertion forward equations; 36 exact initial-response entries; 18 symbolic
bond-current identities; the entropy symmetrizer and generic characteristic
polynomial; 54 matrix-exponential PDE-response cases; and 20 exact one-record
transition-matrix controls. These finite controls are recorded in
`IMMUTABLE_STREAMING_RESULTS.json`. The subsequent extension also checks all 108 symbolic entries of the
current/conserved-density covariance coefficient. The infinite spatial-moment
proof needs its own scrutiny; local coefficient checks do not certify the
infinite sums or a hydrodynamic limit.

1. Independently enumerate finite labeled event maps and full color generators;
   verify stationarity and biased homogeneous product insertion evolution.
2. Check the current, symmetrizer, characteristic polynomial and density
   responses symbolically, including degenerate direction cases.
3. Compare a microscopic stochastic response with the closure only after exact
   small-system calibration. Do not promote a finite-scale fit to a limit.
4. Obtain a selective separate-context derivation before packaging a theorem
   claim. The three-dimensional hydrodynamic limit remains a distinct task.
