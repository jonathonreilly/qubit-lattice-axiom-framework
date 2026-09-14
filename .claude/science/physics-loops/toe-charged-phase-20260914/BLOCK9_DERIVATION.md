# Actual cubic-ice source response, graph conductance and winding histories

Working author derivation. Supplied finite Hamiltonians and source convention;
no native phase, empirical electromagnetic identification or axiom conclusion.
General stochastic-matrix, stiffness/winding and graph variational principles
have prior art. The aim is an exact matched observable and bound for the
current cubic-ice source/phase obligation, with every limit explicit.

## 1. Geometric move graph and finite ground state

Let Omega be a finite connected component of configurations. Each geometric
move e is an unordered edge between distinct configurations x,y, with J_e>0.
Parallel geometric moves remain separate even if their endpoints coincide.
Choose one orientation x->y per edge and antisymmetric real source a_xy=-a_yx.
For arbitrary real diagonal d_x, define

    H(theta)_xx=d_x,
    H(theta)_xy=-sum_(e:x->y) J_e exp(i theta a_e).

Reverse entries are conjugates. H(0) is real stoquastic and irreducible.
A scalar shift of -H(0) gives a nonnegative irreducible matrix with positive
diagonal. Perron-Frobenius therefore gives a simple ground energy E0 and a
strictly positive real normalized vector psi_x, sum psi_x^2=1. Its finite
excited gap is positive. No lower bound uniform in component/volume follows.
The simple branch E0(theta) is analytic near theta=0 and even by conjugation.
A singleton has no source edges and all response formulas below give zero.

Let B be the edge-by-vertex incidence matrix, (B phi)_e=phi_y-phi_x,
and w_e=J_e psi_x psi_y>0. Every edge sum below is over these unoriented
geometric edges once. This fixes all factors of two.

## 2. Exact relaxation is a weighted graph minimization

The first-order eigenvector correction is purely imaginary, because H'(0)
is imaginary antisymmetric and the unperturbed ground vector is real.
Every imaginary tangent vector has the form i psi_x phi_x, modulo the
irrelevant constant phase. Thus second-order minimization over normalized
vectors is exhausted by phases at first order; real amplitudes begin only
at second order and give no extra second-order energy lowering at a stationary
ground state.

Directly, for psi(theta)_x=psi_x exp(i theta phi_x),

    <psi(theta)|H(theta)|psi(theta)>-E0
       =2 sum_e w_e [1-cos(theta(a_e+(B phi)_e))].

Expanding and minimizing the first-order correction therefore gives

    C(a):=E0''(0)=2 min_phi sum_e w_e (a_e+(B phi)_e)^2.       (1)

This can also be obtained by differentiating the finite eigenvalue equation:
C=<psi|H''|psi>-2 sum_(m>0)|<m|H'|psi>|^2/(E_m-E0).
The minimizer solves

    B^T W B phi=-B^T W a,   W=diag(w_e).                    (2)

Connectedness makes the only null vector constant, so fixing one phi or its
psi^2 mean determines a unique solution. A sparse Poisson solve, a complete
spectral sum and the direct phase Rayleigh quotient are different checks.

Consequences hold for every diagonal potential d, not only an RK point:

    0 <= C(a) <= 2 sum_e w_e a_e^2;
    C(a)=0 iff a is a real graph gradient.

The second condition is equivalent to zero circulation on every graph cycle,
including length-two cycles made from distinct parallel moves. If it holds,
a basis rephasing removes the source for every theta, not just to quadratic
order. If it fails, C(a)>0 at every finite d with J_e>0 on this component.
Thus strict positivity of finite component curvature alone does not locate a
thermodynamic phase transition.

For several sources a=A lambda the response is a positive semidefinite
matrix 2 A^T W^(1/2) P_cycle W^(1/2) A, where P_cycle is orthogonal projection
onto ker(B^T W^(1/2)). Its rank is the dimension of the source image in real
graph cohomology. This is a statement about the specified move graph.

## 3. Dual flows supply lower certificates

For any edge flow j with B^T j=0, Cauchy-Schwarz gives

    C(a) >= 2 (a.j)^2 / sum_e j_e^2/w_e.                    (3)

The denominator must be positive; zero j is omitted. Equality is attained
by j=W(a+B phi) for the minimizing phi. Equivalently,

    C(a)/2 = max_(B^T j=0) [2 a.j-sum_e j_e^2/w_e].         (4)

For one directed cycle with source period h, its unit flow yields
C>=2 h^2/sum_cycle(1/w_e). For edge-disjoint cycles, optimizing their separate
amplitudes gives the sum of these lower bounds. These are constructive finite
lower certificates, not assertions that a useful uniform packing exists.
At RK, w=J/|Omega|. A single rare large cycle gives a bound suppressed by
|Omega|; existence of a nontrivial cycle is therefore much weaker than a
positive thermodynamic stiffness.

## 4. Reversible current diffusion and its exact finite-time bias

Set pi_x=psi_x^2 and let a continuous-time Markov chain jump along each
geometric edge x->y with rate r_xy=J_e psi_y/psi_x. Its generator is

    (L f)_x=sum_y r_xy(f_y-f_x)
           =-[diag(psi)^-1(H(0)-E0)diag(psi) f]_x.

Detailed balance is pi_x r_xy=w_e=pi_y r_yx. This is auxiliary stochastic
time; it is not a physical Record clock. Define the accumulated antisymmetric
source current A_t=sum_jumps a_(X_before,X_after), and start in stationarity.
Its mean is zero. Define the drift b_x=sum_y r_xy a_xy and G=-L on mean-zero
functions. Then pi b=0 and the minimizing phi in (2) satisfies G phi=b.

The finite stationary jump-current variance is

    Var(A_t)/t = d0-(2/t) int_0^t (t-s)<b,exp(-sG)b>_pi ds,
    d0=2 sum_e w_e a_e^2.                                  (5)

One derivation differentiates the tilted Markov generator: its off-diagonal
rates are r_xy exp(lambda a_xy), with unchanged diagonal. Antisymmetry and
detailed balance give pi L'_0 f=-<b,f>_pi, while L'_0 1=b and
pi L''_0 1=d0. Duhamel's second derivative gives (5), including its minus
sign. Evaluating the spectral integral gives the exact identity

    Var(A_t)/t = C(a)
      +(2/t)<b,G^-2(1-exp(-tG))b>_pi.                      (6)

Consequently the finite-time ratio decreases to C(a) from above, and

    0 <= Var(A_t)/t-C(a) <= 2 ||phi||_pi^2/t.               (7)

Here phi has zero pi mean. A known gap gamma gives the weaker explicit bound
2||b||_pi^2/(gamma^2 t). The finite-time error of an exact stationary expectation
is separate from sampling error and from failure to equilibrate. An arbitrary
Monte Carlo acceptance rule changes L and its diffusion coefficient, even if
it preserves pi; the rates must match the supplied Hamiltonian or be corrected.

At RK the wavefunction is uniform on the chosen component and every geometric
jump rate is exactly J, so neither psi nor a population projection is needed.
Away from RK, the exact Doob rates require the ground vector. Section 5 gives
a different positive closed-history representation valid for every V without
knowing that vector.

## 5. Closed positive histories give the exact finite-temperature source observable

For a finite matrix write H(0)=D-T, with positive geometric off-diagonal
hoppings T. Dyson-expand exp[-beta(D-T)] in ordered jump times and close the
configuration path in the trace. Every zero-source history weight is positive:
it is a product of J_e and exp[-sum dwell_time d_x]. There is no sign problem
at theta=0 for this supplied bosonic occupation Hamiltonian. Source insertion
multiplies each closed history by exp(i theta A_history). Hence

    Z(theta)/Z(0)=<exp(i theta A_history)>_(beta,theta=0),
    F_beta''(0)=Var_beta(A_history)/beta,                   (8)
    F_beta=-beta^-1 log Z.

Path reversal makes the mean current zero. Formula (8) is a direct positive
history observable; it does not require imaginary-source continuation or an
assumed single exponential correlation. It is the model-specific application
of the established winding-fluctuation stiffness principle, not its invention.
The trace must specify its component/sector. At finite volume on one simple
component, beta->infinity recovers C(a). With degenerate disconnected components,
differentiation and this limit can fail to commute with taking the global
minimum; section 8 supplies an actual cubic-ice example.

## 6. Actual Cartesian source measures spatial sheet winding

On an even L^3 cubic torus put n_i(r) in {0,1}, require three occupied links
incident at each vertex, and E_i(r)=epsilon(r)(n_i(r)-1/2), epsilon=(-1)^sum r.
A geometric alternating square flip p=(r;i,j) changes

    Delta E=-epsilon(r) s_p partial p,   s_p=2 n_i(r)-1.

The Cartesian xy source attaches a_p=epsilon(r)s_p to xy moves and zero to
other orientations. These are the same definitions as current main's corrected
Cartesian-source note; the missing epsilon defines a different response.
For a closed configuration history, form its signed integer spatial two-chain

    S=sum_jumps epsilon(r)s_p p.

Since the electric configuration returns, partial S=0. Every closed integer
two-chain on the cubic three-torus has three integral homology components.
Pairing with the constant xy two-cochain gives

    A_history=sum_(xy faces) S_p = L^2 W_xy,  W_xy integer. (9)

For an elementary proof, sum the closed-chain boundary equation on x-links
over z. It makes sum_z S_xy(x,y,z) independent of y; the y-link equation
makes it independent of x. This common integer is W_xy. Summing over x,y
then gives (9). Equivalently, cube boundaries pair to zero and a fundamental
xy sheet has L^2 faces. Local plaquette flips preserve the
spatial electric flux, but their closed history can sweep a nonzero spatial
sheet. This W is a magnetic-source history winding, not the spatial electric
flux of one configuration.

For that source, the finite-temperature intensive response is exactly

    chi_L(beta)=L^-3 F_beta''(0)=(L/beta)<W_xy^2>_beta.      (10)

This also proves periodicity in theta with period 2pi/L^2. The source endpoint
unitary on main is consistent with the same integer periods. Open subcomplexes
with no second homology and exact sources have zero closed-history winding;
one must not substitute an arbitrary boundary twist for this observable.
The uniform bound still needed for a nonzero infinite-volume coefficient is
control of <W_xy^2> on the beta/L scale in the actual selected ground phase,
with justified order of limits. Counting flippable faces does not provide it.

## 7. Exact actual L=2 mobile-component result

An independent axis-major construction gives 864 configurations and 3456
unoriented geometric moves, 1152 active for the xy source. At J=V=1 let
Delta=B^T B be the integer graph Laplacian and b=-B^T a. Direct integer
matrix action verifies

    P(Delta)b=0,
    P(z)=z^6-52z^5+1092z^4-11816z^3
                    +69072z^2-204608z+235008.              (11)

Since P(0)!=0, the exact mean-zero Poisson solution is

    phi=[204608-69072 Delta+11816 Delta^2-1092 Delta^3
                   +52 Delta^4-Delta^5]b/235008.          (12)

The equation Delta phi=b is checked on all 864 coordinates with rational
arithmetic, without accepting a floating-point eigenvalue or rational fit.
Substitution in (1) gives

    chi_2=28261/99144,
    direct flippability term=1/3.                         (13)

The exact polynomial certificate fixes this finite number; it is not a
thermodynamic stiffness. Separate full dense spectral sums agree with the
weighted graph solve at V=1,.95,.9, yielding approximately .285050028242,
.286566088925 and .287751063895. These agree with the current source note's
finite numbers; the new certificate and transport interpretation do not
relabel its previous computation as a new phase result.

An all-configuration recursive degree census gives 9600 ice states in 937
move components on L=2. Of these 760 are singleton frozen components.
The cycle-period criterion detects nonzero xy response on 77 components;
100 additional non-singleton components have no active xy move. There is no
active-but-exact xy source component in this finite census. These counts
are checks at L=2 only; no connectivity classification for general L follows.

## 8. A genuine global-versus-component limit boundary at RK

For every even L, define the periodic electric configuration

    E_x(r)=(-1)^y/2, E_y(r)=(-1)^z/2, E_z(r)=(-1)^x/2.     (14)

Each component is independent of its own coordinate, so div E=0, and every
spatial electric flux vanishes by even-period cancellation. On an xy square
the two y-links have the same electric sign and cannot participate in an
oriented circulation. The corresponding statement holds for yz and zx.
Thus no square is flippable. In occupation variables this is

    n_x=(1+(-1)^(x+z))/2,
    n_y=(1+(-1)^(x+y))/2,
    n_z=(1+(-1)^(y+z))/2.

Every V>=J ring Hamiltonian with arbitrary plaquette phases is

    H(theta)=J sum_p P_p(theta)+(V-J) N_f,

where P_p(theta) is the positive unnormalized two-state RK projector. The
configuration (14) is annihilated by every term. Therefore the global ground
energy in the full zero-electric-flux sector is exactly zero at every theta,
for every V>=J, including RK. Its globally minimized source curvature is zero.
This coexists with (13), because the mobile component is a different sector
choice inside the same electric-flux sector.

On L=2 at RK, the zero-flux sector consists of the 864-state mobile component
and sixteen singleton frozen components. At theta=0 the trace has seventeen
zero-energy vectors. At fixed nonzero theta near zero the mobile branch has
positive energy, while the sixteen frozen branches stay at zero. Hence

    lim_(beta->infinity) [L^-3 F_beta''(0)] = chi_mobile/17,
    L^-3 [d²/dtheta² lim_(beta->infinity) F_beta(theta)]_0=0. (15)

Differentiation and zero-temperature limiting do not commute for this
specified disconnected degenerate ensemble. A uniform superposition of all
880 configurations is another RK ground state, with different component
weights; neither is forced by the local Hamiltonian alone.
For V<J the uniform mobile RK vector has trial energy (V-J)<N_f><0, so
on this L=2 zero-flux sector the ground state lies in the mobile component.
The limit V increases to J selects its positive curvature. General-volume
mobile-component selection and a stable detuned photon phase remain open.


## 9. Constructive membrane cycles on every even torus

Let Omega_L be the component containing n_i(r)=r_i mod 2. On a plane z=z0,
the corresponding xy electric field is the boundary of the face height

    h(x,y)=(-1)^z0 [(-1)^x-(-1)^y]/4.

Indeed E_x(x,y)=h(x,y)-h(x,y-1) and
E_y(x,y)=-h(x,y)+h(x-1,y). Neighboring heights differ by 1/2.
Order all L^2 xy faces by decreasing initial h and flip each exactly once.
When a face is reached, each initially higher neighbor has already decreased
by one and each initially lower neighbor has not moved. Every neighbor is
therefore 1/2 below the current face. The face is flippable with coefficient
epsilon s_p=+1, and its flip lowers its height by one. This proves the full
sequence is allowed. The final height differs by a constant, so every electric
link and occupation returns to its starting value. The source period is L^2.

The three height classes +1/2,0,-1/2 have respectively L^2/4,L^2/2,L^2/4
faces. No two faces within a class share a link, so the sequence has three
parallel rounds of local flips. This supplies a closed history, not a claim
about its stochastic probability or physical time. The L distinct planes give
edge-disjoint cycles in the configuration graph, meeting only at the common
starting configuration.

For every real V and J>0, the positive Perron weights make each cycle's dual
bound (3) strictly positive on Omega_L. At RK, w=J/|Omega_L|. Summing the L
edge-disjoint cycle bounds gives

    chi_L >= 2J/|Omega_L| > 0.                            (16)

The source is one xy orientation and chi_L=C/L^3. This is an explicit finite
lower bound; it can decay exponentially with volume and is not a positive
thermodynamic K. It proves why a finite positive response at every L is
compatible with the remaining phase uncertainty. The global frozen-state
result in section 8 continues to apply when the full zero-flux sector, rather
than Omega_L, is minimized at V>=J.
