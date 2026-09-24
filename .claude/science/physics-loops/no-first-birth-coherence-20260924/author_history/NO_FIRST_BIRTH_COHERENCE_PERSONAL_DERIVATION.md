# Apparatus coherence forced by the continuous process's no-first-birth sector

Personal root candidate, fifth campaign, 2026-09-24. Not independently checked
at creation. Preserve this file once sealed. It is a different initial-value
problem from the normalized post-first-birth N=6 variance theorem.

## 1. Original process, target and premises

Use the same supplied lambda=0 compensated cube, original complete resolved
or coherent formation instrument, fixed positive delta,K,kappa, integer spin
S, C=S(S+1) and epsilon^2 C=delta/K. Start the full microscopic original GKLS
process from psi=U_H Omega, the canonical exact Hermitian low-band image of
the bare zero-field all-A-plus vector. This state lies in N=4. The original
marks increase N by two, while H preserves N. Thus the N=4 block of the full
density rho_epsilon(t) is exactly

    omega_epsilon(t)=|v(t)><v(t)|,
    v(t)=exp[t(-iH-kappa Gamma_S/(2epsilon^2))] psi,

where H is the N=4 restriction of the same physical Hamiltonian and
Gamma_S=sum_j j_j* j_j is the complete original loss. Its trace p4(t)=||v||^2
is the no-first-birth probability. There is no external event-time binning
or conditioning at an unknown birth time. A measurement of N commutes with
the full physical H, so extracting this block is covariant.

The proposed resource theorem concerns any finite apparatus R initially in
product with the actual input psi, with all clocks/phase references counted,
and a unitary conserving the additive H_system+H_R. Discarding R produces a
system output whose N=4 block sigma4 satisfies the unhalved trace error

    ||sigma4-omega_epsilon(t)||_1 <= eta_epsilon.

In particular this follows from the same accuracy for the entire original
one-time density rho_epsilon(t). The device, initial product condition,
conservation convention and accuracy are operational premises, not a
physical derivation. No approximation uniform on other inputs is needed.
Fix t>0 independently of epsilon; estimates below can be uniform on [a,b]
with 0<a<b<infinity.

## 2. The rotor no-first-birth probability is explicit

In N=4 every occupied charge is positive, since total charge is four and
there are four occupied sites. On P=1_(W=0), all A sites are positive and
all B sites are vacant. F_infinity P has twelve mutually orthogonal hop
outputs, indexed by the vacant A and occupied adjacent B. Each rotor hop
is unitary in its electric coordinate. Therefore, on the entire physical
N=4 rotor P space,

    P F_infinity* F_infinity P=12 I.

In each such output the vacated A has two other vacant B neighbors. Each
vacant edge has two unit-norm original resolved formation orientations.
Their ranges are orthogonal for an individual edge; the coherent instrument
has the same total loss. Consequently

    Gamma_infinity F_infinity P=4 F_infinity P,
    Lambda4=P F_infinity* Gamma_infinity F_infinity P=48 I,
    ||Gamma_infinity F_infinity u||^2=192 ||u||^2.       (1)

The compensated rotor low Hamiltonian is Hrot4=KD-delta Z*Z/2. C_1=0 on
this cube, as on N=6: when exactly one A is vacant the only possibly nonzero
occupancy gate is centered on that vacancy, where F_a annihilates the state.
The limiting no-event vector is therefore

    u(t)=exp(-24 kappa t) exp(-it Hrot4) Omega,
    S4(t)=||u(t)||^2=exp(-48 kappa t).                  (2)

This is the common target's probability, not a newly selected physical rate.

## 3. Uniform finite-spin control of the exact N=4 components

Let Q_r be the exact Hermitian spectral projections of h=W+epsilon T+
epsilon^2 C_S, and E_r the no-event Riesz projections of
h_eff=h-i kappa epsilon^2 Gamma_S/(2delta). Bare grades r=0,...,4 occur in
N=4. Use the same uniform resolvent/polar/intertwiner construction as the
parent compensation and actual-birth notes. Weighted estimates below use
w=1+sum E_e^2; all finite-hop factors, their adjoints, the bounded diagonal
D/C and Gamma have common ordinary and w-conjugated bounds.

Write z_r(t)=E_r v(t), v_low=z_0=J_0 a_0. The initial Hermitian input has

    ||E_r U_H P||=O(epsilon^(r+2)), r=1,2,3,4.          (3)

Here is a graded justification, rather than an assumed output cancellation.
Introduce a scalar parameter multiplying Gamma in h_eff. At zero parameter,
E_r=Q_r and E_r U_H P=0 for r>0. Every surviving coefficient in the difference
contains at least one Gamma insertion, of epsilon degree two. Grade change
from P to r requires at least r adjacent T factors, each of degree one;
C and Gamma are grade diagonal. This counting also holds in the contour and
polar inverse-square-root series defining U_H. Thus all coefficients of
degree less than r+2 vanish. Common-radius analytic norm bounds give the
uniform O estimate in (3), also in the weighted algebra if needed.

The full no-event propagator is exactly contractive. Each E_r commutes with
it, so (3) propagates to all t>=0. The first high component has a stronger
decay bound on this sector. Every N=4 bare W=1 word has one vacant A and
three vacant B sites. At least two of those B vertices neighbor the vacant
A. On a vacant edge at any allowed field m, the summed resolved spin loss is

    2(1-m^2/C) >= 2/(S+1).

Hence Gamma_S >= 4/(S+1) Pi_1 on the complete N=4 spin space. For x in
ran(E_1), closeness of E_1 to Pi_1 implies
||Pi_1 x||^2 >= (1-c epsilon^2)||x||^2. Exact dissipativity gives

    d||x(t)||^2/dt
       =-kappa epsilon^-2 <x,Gamma_S x>
       <=-4 kappa(1-c epsilon^2)/(epsilon^2(S+1)) ||x||^2.

In the joint scaling epsilon(S+1) stays between positive constants. Thus

    ||z_1(t)|| <= C epsilon^3 exp(-c0 t/epsilon),
    ||z_2(t)||<=C epsilon^4,
    ||z_3(t)||<=C epsilon^5,
    ||z_4(t)||<=C epsilon^6.                            (4)

No uniform spin-independent bare loss gap is asserted. The shrinking gap
4/(S+1) suffices because the physical loss multiplier is epsilon^-2. The
undamped bare W=4 grade causes no leading contribution by (3).

For the low coordinate, the uniform fourth-order expansion gives

    a_0'=(-iKD+B_epsilon)a_0,
    B_epsilon=-i delta H4_S-kappa Lambda4,S/2+O(epsilon^2),

where B_epsilon and w B_epsilon w^-1 are bounded uniformly. Its initial
coordinate tends to Omega and has a common weighted bound. The bounded
Dyson series about the diagonal unitary exp(-itKD) gives

    sup_[0,b] ||w a_0(t)||<=C_b,
    a_0(t)->u(t) uniformly on [0,b],
    sup_[0,b] ||a_0'(t)||<=C_b.                        (5)

All ingredients in this derivation are on N=4; no N=6 high-tail estimate is
being transplanted into this sector. The no-event low coefficient follows
by replacing C_1 in the general canonical fourth-order expression by
C_1-i kappa Gamma_1/(2delta). Its contribution is exactly
-kappa P F*Gamma F P/2 to the physical-time generator.

## 4. A pointwise no-first-birth variance and Hermitian interband coherence

The exact identity for the physical H is

    H v_low=i J_0 a_0'+i kappa Gamma_S v_low/(2epsilon^2).

Since J_0=P+epsilon F_S P+O(epsilon^2), Gamma_S P=0, and the bounded
operators Gamma_S F_S converge strongly, (5) proves

    epsilon H v_low -> i kappa Gamma_infinity F_infinity u/2.

The high bounds (4) and ||H||=O(epsilon^-4) imply
epsilon H(v-v_low)->0 uniformly on any fixed later [a,b]. Therefore

    epsilon^2 ||H v(t)||^2 -> 48 kappa^2 exp(-48 kappa t). (6)

The mean <v,Hv> is bounded on each such interval. To see this without
mistaking the oblique low subspace for a Hermitian band, use Q_r. For the
low column, (Q_0-E_0)E_0=O(epsilon^3) by the same degree counting and
Gamma P=0. Thus its Hermitian low coordinate differs from a_0 by O(epsilon^3).
The low H block has norm O(epsilon^-2), but applied to a_0 it is bounded
by (5) and the exact KD plus bounded fourth-order expression. This makes
its expectation bounded. All Hermitian high amplitudes of v are O(epsilon^3)
or smaller, so their energies contribute O(epsilon^2) to the mean.
This argument only requires ordinary bounds on the high components.

Together with ||v||^2->S4(t)>0, (6) gives for the normalized conditional ket
phi4=v/||v||,

    epsilon^2 Var_H(phi4(t)) -> 48 kappa^2.            (7)

For the original full ensemble, which has orthogonal N=4,6,8 blocks,
the law of total variance gives

    liminf epsilon^2 Var_H(rho_epsilon(t))
       >= 48 kappa^2 exp(-48 kappa t).                 (8)

This is a lower bound for the original process from the N=4 canonical input.
It does NOT settle pointwise variance of the different problem initialized
in a normalized actual first-birth N=6 ket. No bounded full-ensemble mean
assumption is needed in (8).

For robustness in trace norm, identify the exact Hermitian high amplitude.
On ran(Q_1), H_1^-1=(epsilon^4/delta)(I+O(epsilon^2)). Projecting the exact
low equation gives

    Q_1 v_low= i H_1^-1 Q_1 v_low'
                 + i kappa H_1^-1 Q_1 Gamma_S v_low/(2epsilon^2).

The first term is O(epsilon^4), hence o(epsilon^3), using (5). The second
has the limit fixed by (1). The high components (4) contribute o(epsilon^3)
to Q_1 v on fixed later intervals. Consequently

    epsilon^-3 Q_1 v(t) -> i kappa Gamma_infinity F_infinity u(t)/(2delta),
    Q_0 v(t)->u(t).                                   (9)

The limiting vectors are compared by the physical-word embedding, with
Q_1 tending to Pi_1 on the finite products involved. In particular if
l=||Q_0v|| and h1=||Q_1v||, then

    l->sqrt(S4),
    h1/epsilon^3 -> (4 sqrt(3) kappa/delta) sqrt(S4).    (10)

## 5. A finite robust apparatus bound for this continuous-process target

Let a=Q_0v/l, b=Q_1v/h1 and A=i(|b><a|-|a><b|), on the N=4 output block.
Extend it by zero on other N sectors. Put Ea=<a,Ha>, Eb=<b,Hb> and
h_epsilon=||H_system-cI|| for any chosen scalar c. Exact energy-band
orthogonality gives

    d=|Tr(omega_epsilon i[H,A])|=2 l h1 |Eb-Ea|,
    q=Tr(omega_epsilon A^2)=l^2+h1^2.                  (11)

Ea is bounded by the preceding low-coordinate argument; even its coarse
O(epsilon^-2) bound would suffice. Eb=delta epsilon^-4+O(epsilon^-2).
Thus epsilon d -> 8 sqrt(3) kappa S4 and q->S4.

The finite SLD Fisher inequality, additivity for the initially independent
system/resource, and covariance of the conserving channel imply

    F_HR(sigma_R) >= [d-2 h_epsilon eta_epsilon]_+^2/(q+eta_epsilon)
                        -F_H(psi).                   (12)

One may insert a mathematical zero-energy number flag because [N,H]=0;
neither a supplied event-time detector nor a noncovariant projection is needed.
The input Fisher is O(1), from its canonical low-band preparation with
D Omega=0 and bounded fourth-order energy action. H_system has norm
O(epsilon^-4) on the finite direct sum N=4,6,8. Therefore

    eta_epsilon=o(epsilon^3)
      implies liminf epsilon^2 F_HR(sigma_R)
         >= 192 kappa^2 exp(-48 kappa t).              (13)

This is an initial apparatus-coherence lower bound, not consumption, mean
energy cost or a selected reservoir. It holds for approximation of the
original full one-time continuous-process output with that accuracy because
projecting onto N=4 cannot increase trace norm. It does not use a fixed marked
amplitude, timestep substitution or unknown first-birth time averaging.

For completeness the elementary finite frequency argument also applies.
The input lies in the exact N=4 low band of width O(epsilon^-2). The Q_0,Q_1
energy separation is delta epsilon^-4+O(epsilon^-2). If the input's coherence
bandwidth plus the apparatus's is smaller than that separation, covariance
forces Q_1 sigma4 Q_0=0. The Hermitian test |a><b|+|b><a| then gives error
at least 2 l h1, whose leading order is

    (8 sqrt(3) kappa/delta) S4(t) epsilon^3.

Hence the same o(epsilon^3) approximation premise implies

    liminf epsilon^4 B_R >= delta,
    liminf epsilon^4 diam(spec H_R) >= delta.          (14)

These are necessary frequency/range conditions, not resonance sufficiency.

## 6. Review obligations and limits

Load-bearing new points are the graded E_r U_H P estimate (3), the finite-
spin first-high dissipative estimate (4), the N=4 weighted low argument (5),
the leading coherence (9), and the distinction between N=4-start full process
and normalized N=6-start problem. Check the factor four in Gamma F and factor
48 in the target survival directly from original physical words.

The finite covariance inequalities reuse the already reviewed resource
machinery from PR9079; their application and scale are new. A full conserving
apparatus, achievable errors, continuous-time uniform approximation, local
interaction strengths, uncounted interaction energy, a reusable reservoir,
and physical selection remain open. Interaction-total conservation alone is
not the assumed additive conservation. No stationary-bath or universal
formation impossibility is asserted, and no new axiom is adopted.

The positive finite autonomous construction remains available under its own
resources and finite-grid accuracy, with no contradiction: its clock and
battery are counted resources and its accuracy must be compared at the
explicit o(epsilon^3) scale before using (13). No result from an unrelated
supplied two-site dynamics clause is imported.
