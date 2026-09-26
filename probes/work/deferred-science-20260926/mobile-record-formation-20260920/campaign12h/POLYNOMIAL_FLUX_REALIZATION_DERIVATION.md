# Realizing a polynomial current potential by immutable local exchanges

Primary construction, 2026-09-21; the separate pre-source reconstruction agrees. This supplies
microscopic rates for a class of desired current potentials. It is not a
derivation of those potentials from the minimal axioms, and no novelty claim
is made. All updates remain nearest-neighbor exchanges of complete records.
The read footprint grows when the potential degree grows.

The independent report under `independent_polynomial_flux/REPORT.md` was
read in full together with its checker; all 12 artifacts and six dependencies
were hash-verified. Report SHA
`94d8ffa8681f9fbc605bd6ff196c495d6725e3c92fdd9013cee1b840577776e8`;
seal SHA `47f87385cccde288d7cd950cc7bd9860cf0b2379f3527ee133af2f0e75d2f174`.
It independently checks the general construction, applicability of the limit
proofs, the complete linear spectrum and nonlinear defects. This is not a
publication-source review, formal audit or retained-status verdict.

## 1. A telescoping construction of arbitrary finite degree

Let the finite site alphabet include vacancy and the six vector labels. Fix
an integer k>=1 and a bounded symmetric function S_i of k labels for each
axis i. It will be the coefficient tensor of a homogeneous degree-k scalar
polynomial for that current direction. On an i-directed edge (x,x+e_i),
temporarily write x+j for x+j e_i, a=eta_x and b=eta_(x+1).

For j=0,...,k-1, take the j sites immediately to the left of x and the
k-1-j sites immediately to the right of x+1. These k-1 external sites
exclude both endpoints. Define

`U_j^a(x)=S_i(eta_(x-j),...,eta_(x-1),a,eta_(x+2),...,eta_(x+k-j))`,

`U_j^b(x)=S_i(eta_(x-j),...,eta_(x-1),b,eta_(x+2),...,eta_(x+k-j))`,

with an empty list on either side omitted. Set

`h_i(x,eta)=sum_(j=0)^(k-1) [U_j^a(x)-U_j^b(x)]`.              (1)

It reads the 2k consecutive sites from x-k+1 through x+k and is
antisymmetric under swapping the two endpoints. Use the actual rate

`c_i(x,eta)=kappa0+max(h_i(x,eta),0)`, `kappa0>0`,              (2)

or `c_i=K+h_i/2` with K>k max_i ||S_i||_infinity. All rates are bounded,
strictly positive, and satisfy c_i(eta)-c_i(eta^edge)=h_i(eta).
For finite tori assume every period is at least max(3,2k), so the graph is
simple and this read list has distinct sites. The k=1 case is an endpoint-only
rate.

The pointwise periodic line sum of h_i vanishes. For 0<=j<=k-2,

`U_j^a(x)=U_(j+1)^b(x+1)`.

The remaining term U_(k-1)^a(x) reads k consecutive sites ending at x;
it equals U_0^b(x-k), which reads those same sites. Thus every positive
term cancels a translated negative term after summing x. This uses a
literal equality of ordered read lists, not an expectation or closure.

Every homogeneous product law is consequently invariant on a torus:
exchanges preserve its configuration weight, and the remaining stationarity
condition is sum_edges h_i=0. The bounded local process on Z^3 inherits
these stationary products through its finite-volume local limit.

## 2. Exact mean current equals a chemical-potential derivative

Let p include all seven probabilities and define the homogeneous polynomial

`Psi_i(p)=sum_(a_1,...,a_k) S_i(a_1,...,a_k) p_(a_1)...p_(a_k)`.

In a product state, symmetric exchange rates have zero mean current. The
current of any label a is therefore the mean of h_i/2 times its endpoint
indicator difference. For the j-th summand in (1), that mean is

`p_a [E(S_i | the j-th argument is a)-Psi_i(p)]`.

Summing over the k positions gives the exact expression

`J_a^i=p_a[partial_(p_a) Psi_i-k Psi_i]`.                       (3)

Euler's homogeneous-polynomial identity implies sum_a J_a^i=0. With
mu_a=log(p_a/p_0) for the six occupied labels, the full categorical
derivative is

`partial_(mu_a) Psi_i`

` = p_a partial_(p_a)Psi_i-p_a sum_b p_b partial_(p_b)Psi_i`

` = J_a^i`.                                                   (4)

Thus an arbitrary such polynomial potential is actually realized by a
positive immutable exchange process; it has not merely been inserted into
a continuum ansatz. For a polynomial of degree at most k, first homogenize
each lower-degree monomial by powers of sum_a p_a=1. Polarization supplies
a symmetric coefficient tensor S_i. All alphabets remain the same; no
hidden event-phase state or occupied-record redraw is introduced.

If Psi transforms as a vector under the signed cubic label permutations,
its homogeneous symmetric coefficient tensor has the same transformation
law. Reversing an edge reverses both the spatial read order and the sign of
the vector component. Symmetry of S_i makes the read-order reversal
irrelevant; endpoint reversal supplies the second sign, leaving the physical
rate unchanged. Hence (1)-(2) are cubic covariant when the chosen potential is.

The categorical susceptibility C and current Jacobian A_i automatically
obey A_i C=C A_i^T, since (4) makes A_i C a Hessian. This supplies the
nonlinear entropy condition needed in the smooth-profile argument. Finite
alphabet, finite read range, product invariance and a fixed swap floor are
also the premises of the separately drafted stationary fluctuation proof.
Applying either limiting theorem still requires checking its precise scope;
this construction is not an independent review of those proofs.

## 3. A six-site cubic example improving the nonlinear current

Keep d=3, rho=sum occupied p, q_i=p_(+i)+p_(-i), g_i=p_(+i)-p_(-i),
and S_i=2rho-3q_i. Choose the homogeneous degree-three potential

`Psi_i^(3)=alpha [rho S_i g_i+3 g_i^3]`.                        (5)

A symmetric microscopic coefficient tensor is

`S_i^(3)(a,b,c)`

` = (alpha/6) sum_(all six argument permutations)`

`                 n(a) [2n(b)-3 f_i(b)^2] f_i(c)`

`   +3alpha f_i(a)f_i(b)f_i(c)`.                               (6)

Its product expectation is (5), directly. Formula (1) now has three
endpoint differences and a six-site read footprint; it gives positive
bounded rates through (2). No numerical data have yet been used for this
new generator.

At an isotropic product g=0,q_i=rho/3, its linear current equations are

`delta rho_t+3alpha rho^2(1-rho) div delta g=0`,

`delta g_t+alpha rho^2 grad delta rho=0`,

`delta r_i,t=0`, `r_i=q_i-rho/3`.

Thus the current acoustic pair remains isotropic at every 0<rho<1, with

`c_s^2=3alpha^2 rho^4(1-rho)`.                                 (7)

The change from the quadratic potential also changes the supplied speed;
there is no attempt to hold a previous numerical fit fixed.

## 4. What improves, and what remains anisotropic

Evaluate the exact nonlinear currents on the axis-isotropic submanifold
q_i=rho/3, while allowing g to be nonzero and remaining in the probability
simplex. Using (4) before imposing that submanifold gives

`J_rho^i=3alpha(1-rho)[rho^2 g_i+3g_i^3]`,                      (8)

`J_(g_j)^i=alpha[(rho^3/3)delta_ij`

`                 +3rho(1-rho)g_i g_j-9g_i^3 g_j]`,            (9)

`J_(r_j)^i=9alpha g_i^3(delta_ij-1/3)`.                         (10)

The term -3alpha rho diag(g_i^2) from the rho-times-quadratic potential
is canceled by the derivative of +3alpha g_i^3. Equation (9) is rotationally
covariant through quadratic order in g. Its remaining anisotropic term is
quartic. The density current in (8) retains a cubic anisotropy, and (10)
generates quadrupole imbalance at cubic order. In particular the submanifold
q_i=rho/3 is no longer an exact nonlinear invariant manifold for this rule.

Counting a small density perturbation, g and initially zero r in a smooth
small-amplitude expansion, the density/vector equations through second
order are rotationally covariant. This is a statement about their Taylor
coefficients. It is not an exact SO(3) symmetry of the complete nonlinear
equations, nor an assertion that higher-order terms can always be removed.
The six-site construction resolves the specific quadratic tensor defect
by moving the remaining deviations to higher orders and extra modes.

Uniform per-label births still preserve homogeneous product evolution
exactly. On microscopic rate beta/N, their macro source is beta p_0 for
each occupied label. Equations (7)-(10) do not remove the changing density,
the vanishing sound coefficient at full occupancy, or the need to check
nonstationary fluctuation response separately.

## 5. Outstanding scientific work

The telescoping construction, polarization, current identity and nonlinear
currents require exact controls and separate scrutiny. It is enough to
check the microscopic cubic tensor and its transitions on a full finite
alphabet; simulations are secondary to these identities. A new simulation
must use the six-site footprint and its own calibration rather than
repurposing an existing four-site result.

This offers a concrete way to search for improved continuum currents while
respecting immutable records and one record per site. It also exposes the
remaining choice: the desired polynomial potential is supplied. The minimal
axioms have not selected it, the clock, the scale alpha, or a relation to
quantum mechanics and gravitation. A successful rate realization is a
mathematical construction, not evidence for a desired TOE identification.

## 6. Primary controls and prior-art scope

The primary `polynomial_flux_check.py` now passes 14 exact groups, including
all 7^6 endpoint strings for antisymmetry and the length-six balance control,
longer periodic integer controls, direct six-site product currents under two
positive rate choices, chemical-potential symmetry, the complete linear
field matrix, and the nonlinear rotation residuals. These finite/symbolic
controls do not replace separate checking of the general construction.

Polynomial flux engineering has earlier precedents. Bahadoran, Guiol,
Ravishankar and Saada's [constructive Euler hydrodynamics review](https://arxiv.org/abs/1701.07994)
gives an exclusion-with-overtaking example in section 6 (printed pages 52-53,
equations 117-121) with a tunable scalar polynomial flux. Those pages and
the corresponding introductory scope were inspected. That example permits
jumps over intervening occupied sites. The present candidate specifies
nearest-neighbor swaps of multiple immutable labels and a growing read
footprint. This comparison identifies different hypotheses, not a novelty
proof or an exhaustive literature search. The scalar attractive-process
hydrodynamic theorem is not being imported for this multi-species generator.
