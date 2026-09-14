# Constructive ensemble proof and boundary audit for the clock route

Personal working notes, 2026-09-14 approximately 18:53 UTC. These are proposed
proof details, not a completed phase theorem. Keep the boundary audit open.

## Exact finite identities already checked

block7_dual_covariance_check.py and BLOCK7_DUAL_COVARIANCE_CHECK.json compare
primal residue sums with dual character filters for the six-face cube lattice
at N=2,3,4,5,8. Both the partition normalizations and
Cov(n)/beta+Cov(m)/beta_dual=I agree, with beta_dual=N^2/(4pi^2 beta).

On a (5,2,2,2) four-dimensional box with 92 edges, 78 plaquettes and curl
rank 53, two separated loop currents check the selected-link Gaussian
integration against a separate character expansion. The correct coefficient
is beta/2 times sum rho_e^2/n_e. Replacing it by beta times that sum gives
an error .02579986470; replacing the ORIGINAL external phase current by the
renormalized frequency gives an error .02009913352. Both mistakes are rejected.
Positive phase-integral curvature checks pass for 1,3,5 current factors.
A positive function built with a negative mixture coefficient violates the
proposed componentwise log-sum bound, confirming why mixture positivity is
load-bearing. Shifted one-dimensional closed-current cosets approach their
Gaussian covariance uniformly in the sampled shift as beta grows; these
finite observations do not establish the general uniform bound.

## A direct finite positive-ensemble construction

The FS cosine identity can be re-derived algebraically:

 (1+A cos x)(1+B cos y)
 = (1+3A cos x)/3 + (1+3B cos y)/3
   + (1+3AB cos(x-y))/6 + (1+3AB cos(x+y))/6.

Start with at most one occupied oscillator per edge, with frequency
rho_e=2pi k_e. Repeatedly choose two currents whose edge supports are within
Euclidean distance <=1 and apply the identity. Each resulting branch replaces
two currents by one, so the recursion terminates. All mixture coefficients
are positive and sum to one. Supports remain disjoint inside a branch, so
frequency addition/subtraction never cancels an occupied edge. Every final
current support is connected using edge-to-edge distance <=1.

A final current with support S and L edges has amplitude at most

    K(rho) <= 3^(N_1(S)) product_(e in S) z_(|k_e|),

where N_1 counts canonical edges at distance <=1 from S. To justify the
exponent, its merge ancestry contributes at most L-1 operations. Every
retention that drops a neighboring current can be assigned a distinct
initial edge outside S within distance <=1 from an intermediate subset of
S. Dropped initial edges never return in that branch, so these witnesses are
distinct and there are at most N_1(S)-L of them. This count needs a careful
formal reread but does not appeal to the numerical size of the expression.

Use Fejer kernels instead of a formal Dirac comb. With z_k=4 k^2,

 Fejer_h(x)=1+2 sum_(k=1)^h (1-k/(h+1)) cos(2pi k x)

is a positive mixture of the constant 1 and the factors 1+z_k cos(2pi k x):
the latter coefficient is 2(1-k/(h+1))/z_k. The residual constant coefficient
is positive because sum_(k>=1) 2/z_k <1 (the elementary integral bound
sum k^-2 <2 suffices). Products of these mixtures preserve positivity of
all mixture weights. Individual initial factors need not be positive; after
the Gaussian damping they will be.

A canonical edge in Z^4 has exactly 107 canonical edges within Euclidean
distance <=1, counting itself. Proposed hand count: 23 parallel edges and
28 edges of each of three perpendicular orientations. This finite geometric
count must be independently enumerated. Therefore N_1(S)<=107 L. Also
log(4 k^2)<=k^2 log 4 for k>=1. Set

    beta_1=(107 log 3+log 4)/(4pi^2).

Then K(rho)<=exp[beta_1 ||rho||^2]. This is a deliberately conservative
constant, not a claim about a physical critical coupling.

## Exact damping without ambiguous contour factors

Let Q=d^T d on one-form potentials, V=Q^+ on its positive range. For
coclosed currents rho in that range, Gaussian characteristic functions are
exp[-beta rho^T V rho/2]. Choose mutually plaquette-nonadjacent selected
edges B. With u_e=rho_e/Q_ee on B and zero elsewhere,

    rho_tilde=rho-Q u,
    rho^T V rho-rho_tilde^T V rho_tilde=sum_(e in B) rho_e^2/Q_ee.

The selected components of rho_tilde vanish and delta rho_tilde=0. This is
an exact quadratic identity, avoiding the preprint's convention ambiguity.
For a separated ensemble, all selected sets can be combined: cross terms
vanish because supports are disjoint and selected edges share no plaquette.
The identity therefore holds termwise after expanding the entire cosine
product, for arbitrary EXTERNAL phases rho(a).

A concrete 32-coloring uses edge orientation (four choices) and the three
transverse coordinate parities (eight choices). Each color has no two edges
in a plaquette. Choosing the color with largest squared-current weight gives
sum_B rho_e^2>=||rho||^2/32. Since Q_ee<=6 in four dimensions,

    z(rho)<=exp[-a ||rho||^2], a=beta/384-beta_1.

For a>0 every final factor 1+z cos is positive. A 19-coloring of the
maximum-degree-18 conflict graph could improve the constant to 1/228;
that optimization is not needed for existence and is not used yet.

## Gauge averaging and Fejer convergence

For a FREE potential graph, average the Fejer product over vertex gauge
rotations modulo one. This is nonnegative. In Fourier form it removes
noncoclosed currents. After the separated-ensemble expansion, disjoint
vertex neighborhoods ensure a signed sum of currents is coclosed only
when each nonzero participating current is coclosed. Thus noncoclosed
factors can be deleted under gauge averaging while keeping positive mixture
coefficients. On a contractible box, coclosed one-forms are in range Q.
The remaining finite Gaussian integral has exactly the desired positive
phase representation.

For a fixed finite graph, the Fejer Fourier coefficients are bounded by one
and tend to one. The coclosed Gaussian Fourier series and all phase
 derivatives converge absolutely, so the partition approaches the theta
function for a shifted integer-curl lattice. Equivalently, the supported
physical field is dA in da+d Z^E. Gauge-volume factors cancel in ratios.
This argument must be written with a precise lattice quotient before it is
used as a universal boundary statement.

## Prospective local surface and packing estimate

For a nonzero coclosed current rho whose connected support has L edges,
its bounding box has side at most 3L. A coordinate-path contraction to a
corner fills each edge difference with at most 3R plaquettes when the box
side is R. Summing over a closed current cancels the paths, producing a
2-form mu with delta mu=rho and

    ||mu||_1 <= 9 L ||rho||_1 <= 9 L^(3/2) ||rho||_2.

Hence |rho(w)|^2 <=81 L^3 ||rho||^2 max_(p in box) |dw(p)|^2.
This proposed homotopy bound needs an explicit chain formula and tests.
In one separated ensemble, supports are disjoint. For fixed L and a
plaquette p lying in a current's box, the whole support lies inside a cube
of side <=9L about p; there are at most 4(9L)^4 edges there. Therefore at
most 26244 L^3 such currents can be assigned to p.

Taking z/(1-z)<=2z once z<=1/2, using ||rho||^2>=(2pi)^2 L, and splitting
exp[-a||rho||^2] into two factors gives the candidate uniform bound

 c(beta) <= (4*81*26244/(a*e))
            sum_(L>=1) L^6 exp[-a (2pi)^2 L/2].

The estimate uses t exp(-a t/2)<=2/(a e). It is intentionally loose and
still decays exponentially as beta grows. It would imply a uniform
phase curvature bound -c(beta)||dw||^2. Neither the geometric constants nor
boundary applicability have been certified in the current source yet.

## Boundary and topology audit: do not skip

The free-potential integer-curl model d Z^E is straightforward. Its dual
partner ker(delta) intersect Z^P on a FREE primal box is represented by
potentials on a relative or wired dual complex. Boundary currents can then
look like open paths ending on the wired boundary. They must not silently
be treated as compactly supported closed currents in Z^4. A local filling
and gauge-averaging argument valid for free potentials does not automatically
cover that relative boundary problem. This is currently unresolved.

A potentially cleaner route is a periodic four-torus. Isotropic periodic
cube measures have translation/cubic symmetry and reflection positivity
before any subsequential limit, removing the need for a finite-Z_N
Ginibre limit argument. Both integer-curl sublattices exist with periodic
potential graphs. Harmonic modes, however, must be retained explicitly.
Condition on electric currents AND harmonic flux to leave a coset of the
integer coexact lattice delta Z^C. On the dual side condition to leave a
coset of the exact lattice d Z^E. Their real projections sum to I-P_harm,
not I. P_harm has finite rank six and fixed local entries tend to zero as
the four-torus volume grows.

Small contractible currents admit the local filling bound. Winding or
large-diameter currents have support length at least order the torus side.
On coexact potential directions, a global Poincare estimate costs only a
power of that side, while their activities decay exponentially in length.
This may give a vanishing correction or a uniform small bound. Harmonic
Gaussian integration can couple winding currents, so they cannot simply be
deleted factor-by-factor; integrate the positive renormalized product over
harmonic angles, and keep its source curvature estimate valid. Precise
periodic integer lattices, flux cosets, large-current packing and limiting
projectors are the next load-bearing tasks.

An isotropic periodic-limit OS phase would still not automatically identify
the selected anisotropic continuous-time clock Hamiltonian or prove finite
spatial transfer gaps converge without a state-limit argument. Keep those
claims separate. No public block-6 or block-7 PR has been opened.
