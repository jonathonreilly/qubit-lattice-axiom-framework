# Bounded matter dynamics: active personal derivation

2026-09-16 03:02 UTC. UNREVIEWED WORKING ROUTE.
Blocks01--05 are pushed at6c7548b8e7d09a0aba9c6585a8cfdc802d40dc09.
Next complete this connected obligation, then package one coherent milestone
and reassess fixed-g leverage. Deadline13:45:03 UTC; no subagents.

## Exact local residual

Use rooted CAR a_x=U(p_x)^q c_x and coordinate x-then-y-then-z paths on Z^3,
including negative steps. Set p_0=0. The physical final observables are
neutral CAR polynomials. The full rotor/Fock Hamiltonian supplies an
auxiliary dynamics on charged root operators; do not call those physical.
The initial ground state is in N_+=N_-=V, but time evolution of neutral
number-changing observables uses the same supplied Hamiltonian on the full
Gauss Hilbert space, not a falsely closed fixed-number operator algebra.

For the electric energy,

    [calH_E,a_x]
      =g q a_x P(W_E^(1/2)p_x)
           +(g^2 q^2/2)||W_E^(1/2)p_x||^2 a_x.

This follows from E U(p)^q=U(p)^q(E+q p). Magnetic energy commutes with a_x.
For matter, [calH_m,c_x]=-sum_y h_xy(theta)c_y, so

    [calH_m,a_x]=-sum_y h_xy(0) U(p_x+edge_xy-p_y)^q a_y.

The onsite term is exact, and backwards edges have their signed orientation.
The rooted loop of a nearest-neighbor edge has a finite plaquette filling
with at most C(1+|x|_1) faces: coordinate strips, as in Block02, now rooted
at0 without a finite block boundary. Block01 gives each loop defect norm
O(g times filling size), even after multiplying a bounded CAR operator.
Also ||P_l||_rho is uniformly bounded. Therefore

    ||([calH,a_x]+sum_y h_xy(0)a_y)rho^1/2||
        <=C g(1+|x|_1),       0<g<=1.

Adjoints require moving P past a_x^*: the extra commutator is O(g) bounded,
and after the outer g it is O(g^2). Do not assume an operator adjoint has
the same state norm without this step.

For a finite CAR monomial B of degree m, apply the Leibniz rule and move
all residual electric P's to the right. Their commutators with later
dressings are g times weighted path overlaps. Since
|<p_x,W_E p_y>|<=e_max sqrt(len_x len_y)
                  <=e_max(len_x+len_y)/2,
the resulting norm bound is

    ||([calH,j(B)]-j([H_m,free,B]))rho^1/2||
       <= C_m g [1+sum_j |x_j|_1].

The constant depends on the fixed coefficients and degree, not volume or
the locations beyond the displayed weight. Extra fixed charge interactions
would spoil the free commutator, and remain excluded as in Block02.

## Free spreading without torus wrapping

For a local polynomial B set B_t=alpha^free_(-t)(B), so
partial_t B_t=-i[H_m,free,B_t]. Each factor evolves linearly under the
bounded finite-range one-particle matrix, preserving its l2 norm. Weighted
l1 norms with weight1+|x| are bounded by exp(K|t|), because the finite-range
matrix is bounded on that weighted space. Thus the coefficient sum of
the monomial residual above stays bounded uniformly in t in a compact
interval, and uniformly under spatial truncation.

Truncate the evolving one-particle coefficients to the centered cube K_R
and call the resulting fixed-degree polynomial B_t^R. Then uniformly on
|t|<=T,

    ||B_t-B_t^R|| ->0,
    ||partial_t B_t^R+i[H_m,free,B_t^R]|| ->0

as R->infinity. Prove this with the finite-range exponential series: a
term of degree n moves support at most n steps, so tails are bounded by
sum_(n>=R-R0)(T||h||)^n/n!. The derivative defect is the commutator of
the spatial cutoff with h, hence is controlled by the neighboring tail.

Choose R(L)=floor((L-3)/4), so all paths and neighboring sites involved in
the finite-volume commutator embed without wrapping. The polynomial
residual bound is C_(B,T)g independent of R because of weighted l1 control.
With G=calH-E_ground, differentiate

    exp(it G) j_L(B_t^R)rho^1/2.

Use G j_L(B)rho^1/2=[calH,j_L(B)]rho^1/2. This should yield

    ||exp(-itG)j_L(B)rho^1/2-j_L(B_t^R)rho^1/2||
       <=C_(B,T)g+T epsilon_R(T).

No positivity of G outside the initial number sector is needed: only
self-adjoint unitary evolution and G rho^1/2=0. Domains are smooth at
each finite g,L. For final limits, compare B_t^R with a fixed-radius
B_t^r in CAR operator norm, use the Block04 state limit at fixed r,
then r->infinity. Do not apply the fixed-local state theorem directly to
an observable whose radius grows with L.

## Multi-time bounded matter words

The root map is an exact finite-CAR homomorphism, so bounded multiplication
has the same operator norm as in CAR. Ground-state time words can be
rewritten as alternating bounded j(B)'s and unitaries exp(-itG) acting
on rho^1/2. Apply the vector comparison above, approximate each evolved
free polynomial by a fixed finite-radius polynomial, multiply by the next
bounded factor, and iterate. This should prove convergence of every fixed
finite multi-time word of neutral finite-path matter polynomials to the
free Slater CAR dynamics, uniformly on compact sets of the times.

Do not claim arbitrary mixed unbounded gauge/matter multi-time words from
this. Higher field moments are separate. The intended result, combined
with Block05, supplies gauge two-point propagation and bounded fermion
multi-time correlations in the same joint weak-g limit.

## Planned selective challenge

Use the literal charged four-site plaquette ring from Block05, with a
rooted coordinate tree through links0,1,2. In its Gauss basis
E_l=n+sum_(x<=l)Q_x, every rooted neutral CAR monomial leaves n=E_3
unchanged. Thus j(B)=B_Fock tensor I_n exactly, while the actual closing
link hopping shifts n by its charge. The free embedded matter Hamiltonian
has no such shift. Check [H,j(B)]-j([H_free,B]) against the independently
constructed electric difference and compact closing-loop difference;
then compare exp(-itG)j(B)psi with j(alpha_free_(-t)B)psi for a nontrivial
bounded hopping/density polynomial. This tests the current route's signs
and dynamics in a charged model. It is not a thermodynamic phase simulation.
