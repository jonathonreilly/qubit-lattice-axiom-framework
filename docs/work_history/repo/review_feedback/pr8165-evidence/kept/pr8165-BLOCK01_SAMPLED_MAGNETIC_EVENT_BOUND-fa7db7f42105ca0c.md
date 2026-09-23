# Joint magnetic event bounds for compact rotor ground paths

Author-proposed bounded theorem, 2026-09-16. Personal proof and challenge
checks completed; independent review and retained status are pending.
See [the claim scope](../CLAIM_STATUS_CERTIFICATE.md). This is a theorem
about the supplied Hamiltonian below, not a
derivation of that Hamiltonian from the framework's axioms.

## 1. Domain and proposed conclusion

Let L>=4 be even, N=L^3, and let E and P denote the positively oriented
links and spatial plaquettes of the three-dimensional periodic cubic
lattice. There are 3N links and 3N plaquettes. Angles have normalized
Haar measure on the product of E circles, each R/(2pi Z). Write C for the oriented plaquette-link
incidence matrix and set

    H = -(g^2/2) sum_e partial_e^2 + g^(-2) V(theta),
    V(theta) = sum_p (1-cos((C theta)_p)),       0<g<=1.       (1)

All three link directions have the same electric coefficient and all
plaquettes have the same magnetic coefficient. There is no fermion term,
fixed-angle gauge choice, clock truncation or real Gaussian replacement.
The Hilbert space used initially is the full L^2(T^E). Its normalized,
strictly positive ground state is denoted psi and its ground energy E0.

The stationary ground Euclidean process has cylinder expectations

    <psi, f0 exp[-(t1-t0)(H-E0)] f1 ...
                  exp[-(tr-tr-1)(H-E0)] fr psi>.             (2)

This is a probability law for compact angle configurations, as follows either
from the positive Feynman-Kac kernel or the ground-state Doob transform.
Only bounded gauge-invariant magnetic cylinder events are asserted to be
physical observables here. The auxiliary link paths are used in the proof.

For 0<alpha<pi and sampling interval T>0, define

    c_alpha = 1-cos(alpha/2),
    q(g,tau,alpha) = min(1, exp[-tau c_alpha/g^2]
                           +16 exp[-alpha^2/(128g^2 tau)]),
    C0 = 3pi^2/16 +12(1/3-2/pi^2),
    eps(g,T,alpha) = min(1, exp(C0 T) q(g,2T,alpha)^(1/8)).  (3)

Call a plaquette bad at time nT if its circle-valued flux has distance
at least alpha from zero. For k specified distinct plaquette/time pairs
of one fixed spatial orientation, the proposed bound is

    P_ground(all k pairs bad) <= eps(g,T,alpha)^k.           (4)

For k distinct pairs with arbitrary orientations the bound is

    P_ground(all k pairs bad) <= eps(g,T,alpha)^ceil(k/3).    (5)

The constants do not depend on L. The time variable in (1)-(2) is already
continuous; T is an observation spacing, not a regulator to be removed.
These are joint-event bounds, not an assertion that the events are
independent. Their usefulness is at sufficiently small but fixed g.

## 2. Ground sector and a uniform energy upper bound

The compact elliptic operator (1) has compact resolvent and a strictly
positive heat kernel. Its lowest eigenfunction is strictly positive and
simple. Gauge translations theta->theta+d lambda and constant directional
link shifts commute with H and preserve positivity. They must therefore
fix the normalized positive psi. Consequently this full-space ground
state is gauge invariant and invariant under flat shifts; it is in the
neutral Gauss sector with zero global electric flux. This observation
does not identify a finite-temperature full trace with a Gauss-projected
thermal trace. Only the zero-temperature limit is used below.

An unrestricted trial function may be used to upper-bound E0, since the
full-space minimum itself belongs to this physical ground sector. Let

    a=sqrt(2)g<pi,
    f_a(theta)=sqrt(2pi/a) cos(pi theta/(2a))  for |theta|<=a,
               0                              otherwise.  (6)

This is a periodic H^1 form-domain function. Direct integration gives

    integral f_a^2 dtheta/(2pi) = 1,
    integral |f_a'|^2 dtheta/(2pi) = pi^2/(4a^2),
    integral theta^2 f_a^2 dtheta/(2pi)
                                      = a^2(1/3-2/pi^2).   (7)

In the product trial state over all links, a raw plaquette curl has mean
zero and variance 4a^2(1/3-2/pi^2). The pointwise inequality
1-cos x<=x^2/2, valid for every real x, bounds its magnetic contribution
by 4(1/3-2/pi^2). Its kinetic contribution per link is pi^2/16. Thus

    0<=E0<=C0 N,                 C0=3.418842417788148... .   (8)

The trial state is not assumed gauge invariant. Its raw angles are used
only for this variational estimate, not as a global physical flux lift.

## 3. Reflection positivity of the actual loop measure

For finite inverse temperature beta, use the normalized full trace
Tr(exp(-beta H)) and its compact Brownian loop representation. The
reference law is a product, over links, of independent circle Brownian
loops with generator g^2 partial_theta^2/2. Weight it by

    exp[-g^(-2) integral_0^beta V(theta(s)) ds].               (9)

No time discretization or winding exclusion is made.

Spatial reflection is through two parallel planes of vertices at x_i=k
and x_i=k+L/2. Reflect the geometry and pull back oriented link angles;
an edge reversed relative to the chosen positive orientation acquires a
minus sign. Boundary variables are the entire time paths of links lying
parallel within the two reflection planes. Every elementary plaquette
belongs to one closed half or entirely to a boundary plane. In particular,
there is no elementary plaquette straddling the interior of a plane of
vertices. Conditional on the boundary paths, the reference loops and
the weighted interactions in the two open halves factor. Reflection
identifies these two conditional factors. Cosines are unchanged by
orientation reversal and circle Brownian loops are invariant under sign.

For a bounded real function f supported in one closed half, integration
over its interior produces a real boundary function h_f. The unnormalized
expectation of f times its reflection is the integral of h_f^2 against
the positive boundary measure. For f and h this produces the symmetric
bilinear form integral h_f h_h. Normalization preserves its positivity.
This proves reflection positivity through each such spatial site plane.
Shared boundary link paths are essential in this argument; they are not
assigned independent copies.

Time reflection is through two slices s and s+beta/2. Conditional on the
two full angle configurations at those slices, the Brownian bridges of
the two temporal halves factor and are related by time reversal. The
potential is instantaneous and time independent. The same conditional
square proves time reflection positivity. Space and time reflections
preserve the corresponding support algebras. All coordinate translations
and the required reflection operations preserve the loop measure.

We apply the algebraic chessboard estimate, Theorem 5.8 in Biskup,
math-ph/0610025v2, PDF44-47. Its inputs are these positive half-space
bilinear forms, their Cauchy-Schwarz inequalities, consistent reflected
block supports and the even periodic block counts. For spatial unit
cubes times intervals of duration T, take beta=MT with M even. There
are N M cells. Rectangular block counts L,L,L,M are allowed: the proof
iterates the one-dimensional Cauchy-Schwarz argument independently in
each coordinate and requires no permutation symmetry between axes.
Link-midpoint variables and entire path segments replace vertex spins;
the just-verified half-algebra properties are the needed algebraic inputs.
Neighboring cells share boundaries, as do the blocks in that theorem.
Null directions are treated by the positive-semidefinite quotient in
the usual Cauchy-Schwarz argument.

Consequently, for nonnegative cell functions f_j in distinct cells t_j,

    E_beta product_j Theta_tj f_j
       <= product_j [E_beta product_all_cells_t Theta_t f_j]^(1/(NM)).
                                                               (10)

We use only indicators. No spin-model infrared bound, diagonal spatial
reflection or generic quantum reflection-positivity assertion is imported.
In particular, Biskup's PDF68 warning that generic noncommuting quantum
models need not have site reflection positivity is not bypassed by a
label: (9) and the conditional-square proof are specific to (1).

## 4. A dense bad slice has a small compressed heat norm

Suppose a starting configuration has J edge-disjoint plaquettes bad at
threshold alpha. On each of the four edges of one plaquette, freely lift
the Brownian increment to g W_e(s) on R. If all four increments obey

    sup_(0<=s<=tau) |g W_e(s)| <= alpha/8,

then the flux remains at circle distance at least alpha/2 from zero for
the whole interval. That plaquette's contribution to (9) is bounded by
exp(-tau c_alpha/g^2). Reflection plus the Gaussian Chernoff bound gives

    P(sup_(s<=tau)|gW_e(s)|>alpha/8)
                                  <=4exp[-alpha^2/(128g^2 tau)].

The union bound over four edges therefore bounds the one-plaquette
survival expectation by q in (3). It is legitimate to cap the bound at1.
The real lifts only track increments of circle Brownian motion. Their
use includes, rather than deletes, every compact winding history.

Drop all other nonnegative plaquette potentials. Since the selected
plaquettes use disjoint edge Brownian motions, the remaining expectation
factors, even though the full interacting measure does not. Uniformly
over this set A of starting configurations,

    (exp(-tau H) 1)(theta) <= q(g,tau,alpha)^J, theta in A.  (11)

Let P_A be multiplication by its indicator. The positive symmetric kernel
of B=P_A exp(-tau H) P_A has row sums at most q^J. Symmetry gives the same
column bound, so Schur's test yields

    ||B|| <= q^J.                                           (12)

B is a positive trace-class operator. This is a killed heat-kernel norm,
not an estimate of the physical spectral gap or ground-state density.

## 5. Dissemination geometry and the zero-temperature limit

Place the base ij-plaquette on either face, b=0 or1, normal to the
remaining coordinate k of a unit cube. Under reflected dissemination,
a base coordinate s in [0,1] maps into cell x by

    s -> x_r+s       if x_r is even,
    s -> x_r+1-s     if x_r is odd.                          (13)

All distinct ij-plaquettes in the resulting event lie on the parity-b
normal planes. There are N/2 distinct plaquettes, each imposed twice by
the N cells. In each such plane, choose the checkerboard parity of the
two tangential anchor coordinates. These form N/4 edge-disjoint
plaquettes. L>=4 avoids the degenerate two-site torus incidence issues.

Likewise, a lower- or upper-time-endpoint event disseminates to M/2
distinct time slices, each repeated twice, with spacing 2T. Thus a dense
dissemination is A at m=M/2 slices separated by tau=2T. The spatial and
time repetitions cannot be counted as additional independent constraints.
The selected J for (12) is N/4, not N or N/2.

For m>=1, its finite-temperature probability is

    Tr[(P_A exp(-2TH))^m] / Z_(MT)
      = Tr[(P_A exp(-2TH)P_A)^m] / Z_(MT),
    Z_(MT) = Tr exp(-MT H).                                 (14)

The equality follows by cyclicity and P_A^2=P_A. Set B as in (12). Since
B is positive,

    Tr B^m <= ||B||^(m-1) Tr B
            <= q(g,2T,alpha)^[(N/4)(m-1)] Tr exp(-2TH),
    Z_(MT) >= exp(-MT E0).                                  (15)

For fixed finite L, the trace in the numerator is finite. Take the
1/(N M) power required by (10), then let M->infinity through even
integers. The trace factor tends to1 and (8) gives

    limsup disseminated_probability^(1/(NM))
            <= exp(C0 T) q(g,2T,alpha)^(1/8).                (16)

For a fixed finite collection of sampled events, the normalized thermal
trace converges to (2), since the finite-box ground state is simple and
isolated. This limit uses no gap uniform in L. Every requested plaquette
at spatial anchor x and time nT can be assigned to cell (x,n): choose
the inverse-reflected base normal face b according to x_k parity, and
the inverse-reflected base time endpoint according to n parity.
For a fixed orientation these anchor cells are distinct. All base face
and endpoint choices have the same bound (16), proving (4).

For arbitrary orientations, at least ceil(k/3) of the pairs have one
common orientation. The full intersection is contained in that subevent,
so (5) follows. This loss must not be silently removed. Capping every
factor at1 gives exactly (3)-(5).

## 6. An explicit weak-coupling range for sampled magnetic defects

The choice

    T_alpha = alpha/[16 sqrt(2) sqrt(c_alpha)],
    a_alpha = 2 T_alpha c_alpha = alpha sqrt(c_alpha)/(8sqrt(2))

balances the two exponential rates in q and implies

    eps(g,T_alpha,alpha)
      <= min(1,17^(1/8) exp[C0 T_alpha-a_alpha/(8g^2)]).      (17)

At alpha=pi/3, T_alpha=0.126439394990932821... and
a_alpha=0.033879333779300190... . These constants are deliberately
conservative. No empirical physical coupling is being fitted.

At each sampled time define the principal magnetic cube charge

    Q_c = (1/(2pi)) sum_(faces p of c) z_cp principal((Ctheta)_p),
    principal values in [-pi,pi).                           (18)

The exact incidence identity d C=0 makes Q_c integer. If Q_c!=0 then
some face is bad at threshold pi/3. For n specified distinct cube/time
cells, choose one witness face of each. There are at most6^n choices.
A distinct face/time pair witnesses at most two cells, so any assignment
has at least ceil(n/2) distinct pairs. Equation (5), with eps<=1, gives

    P(Q_c!=0 at all n cells) <= [6 eps^(1/6)]^n.             (19)

Set p_def=min(1,6 eps^(1/6)). On the nearest-neighbor graph of cubes
times sampled times, degree is at most8. The count of connected sets
of size s containing a specified cell is at most8^(2s-2): encode a
deterministically chosen spanning tree by its depth-first traversal of
2s-2 steps. Hence the occupied connected component at that cell satisfies

    P(component size >=s) <= 8^(2s-2) p_def^s.              (20)

Use a connected size-s subset if the component is larger. For g=0.01,
(17) gives the conservatively rounded bounds eps<8.903e-19,
p_def<0.005885, and64p_def<0.37664<1. The bound is therefore exponentially
decaying in s at this explicit fixed positive coupling and at any smaller
g with the same T. No claim that this range is sharp is intended.

This corollary concerns sampled principal magnetic-defect clusters. It
does not identify them with all continuous-time monopole worldlines.
Events between the sampling times and electric winding defects have not
been bounded by (19)-(20).

## 7. Spatial subsequential limits and the precise remaining obligation

Periodically extend the finite-torus processes on the countable set of
spatial links and sampled times. Compactness of the product of circles
gives subsequential weak limits as L->infinity through even integers.
Every fixed finite set embeds without wrap identifications for large L.
The event inequalities survive in these sampled-time angle laws, but
one must use the correct Portmanteau direction. For alpha'<alpha, the
closed threshold-alpha event is contained in the open event with every
distance strictly greater than alpha'. Portmanteau bounds the latter
limit probability by the liminf of its finite-volume probabilities;
these are bounded by eps(g,T,alpha') to the required power. Let
alpha' increase to alpha at fixed T, using continuity of (3).
The deterministic implication from (18) to bad faces then transfers
(19)-(20), without assuming continuity of the principal-branch charge.

This constructs only subsequential stationary sampled-time angle laws.
It proves neither their uniqueness nor continuum-path tightness in
infinite spatial volume. These torus limits have not been identified
with the cofinal free-box equal-time state of draft PR8164.

Sparse sampled magnetic defects alone do not prove a Maxwell phase.
Small principal plaquette flux does not supply a global real lift with
small raw curl. Continuous-time excursions, compact winding sectors,
and the physical transverse susceptibility or source characteristic
functional still require control. There is no photon pole, continuum
Lorentz symmetry, matter spectrum or native Hamiltonian selection
conclusion in (4)-(20). The positive local defect floor from PR8164 is
compatible with rare clusters; density need not be exactly zero.

## 8. Sources, checks and dependency boundaries

Primary reflection-positivity source: Marek Biskup, *Reflection Positivity
and Phase Transitions in Lattice Spin Models*, math-ph/0610025v2,
27 April 2009, https://arxiv.org/abs/math-ph/0610025 . PDF SHA256
0895449a770754915ad6d3cf44049b92d4981b1ace6dfeac76cf0380768a8733.
The conditional-square mechanism, algebraic chessboard estimate,
Feynman-Kac formula, Schur test and compact-ground projection are
standard tools, not claimed inventions. The model-specific content is
their carrier, support, sector and constant matching in this argument.

This note is self-contained relative to those mathematical tools and
the supplied Hamiltonian (1). It does not assume any theorem in draft
PR8164. That draft's exact head is
c4a31d8d1bc43096080bd5f88b16ffcf24344146; it supplies contextual targets
and separately provisional comparisons only. Base main is
e0ef7cf4633034a8c1e6d57f5812cc4275bf1349.

Completed personal challenge checks cover actual reflected
periodic incidence, face/time multiplicities, disjoint-edge packing,
independent trial integrals, Brownian/rotor semigroup comparisons and
the constants in (17)-(20); see [the review](../review/PERSONAL_REVIEW.md).
Finite checks cannot establish (10) or a
thermodynamic phase. A finite-clock chain has jump paths and is not a
valid substitute for the Brownian estimate (11).
