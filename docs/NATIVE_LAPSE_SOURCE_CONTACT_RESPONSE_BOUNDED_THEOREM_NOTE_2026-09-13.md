---
claim_id: native_lapse_source_contact_response_bounded_theorem_note_2026-09-13
claim_type: bounded_theorem
claim_scope: "For the specified native two-orbital Wilson model with supplied positive cell lapses, derive its actual variational energy source and finite arithmetic susceptibility; in the free filled-band model derive both arithmetic and geometric-mean responses at every momentum, their local contact difference, the thermodynamic quartic-log term, global congruence-energy convexity and the stated finite static existence bound. An exact strong-interaction midpoint witness is confined to the declared three-cell, three-particle sector. Physical lapse selection and interacting infrared stress response remain open."
upstream_dependencies:
  - native_edge_record_matter_instrument_and_energy_ledger_bounded_theorem_note_2026-09-05
runner: scripts/native_lapse_source_contact_response_2026_09_13.py
---

# Native lapse sources, contact response and a free static variational solution

**Date:** 2026-09-13
**Type:** bounded_theorem
**Status:** proposed_retained

## Target, premises and obligation structure

For the supplied native Wilson Hamiltonian and two explicit lapse laws, prove
the variational source, complete free static response, its infrared asymptotic
and the finite free static existence result, while keeping the finite
interacting witness in its declared particle-number sector.

~~~yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "Analytical source and response theorems for specified Hamiltonian families, with finite exact and numerical challenges."
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "A reciprocal matter source and its complete susceptibility on a common native carrier."
source_of_blocker_text: user_goal
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Derive or physically select a full metric coupling and test its interacting stress identities."
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
~~~

| Premise or obligation | Role and provenance | Treatment |
|---|---|---|
| Cubic physical placement and one-site M2 domain | Framework ontology in the current memo | Placement only |
| Ordinary tensor quantum composition, CAR, Pauli basis and native cycle code | Conditional representation, linked native source below | Supplied physical realization |
| Wilson coefficients, local quartic strength, lapse fields and bond means | Defined here | Supplied model data, no empirical fit |
| Finite isolated ground eigenvalue or free filled negative band | State and spectral hypothesis | Declared separately for each theorem |
| Native paths and energy-cell operators | Derived below from the linked even-CAR dictionary | Conditional author theorem |
| Source and finite susceptibility | Eigenvalue differentiation, proved below | Author derivation |
| Free integral limit and quartic-log term | Bounded integrand, node charts and uniform Taylor estimate | Proved here, no scaling fit |
| Global free convexity | Finite trace fidelity variational identity | Proved here; physical state selection is supplied |
| Static kappa, g, Laplacian, mean-zero source and boundary convention | Explicit static probe functional | Supplied, no Newton normalization |
| Exact strong-interaction midpoint witness | Frozen trial vectors, direct CAR signs and rational bounds | Finite existence statement |
| Physical metric/clock and interacting stress response | Desired downstream use | Open; no theorem imported for this bridge |

No observed constant, new primitive, axiom amendment or gravity selection is
inferred from this construction. The [framework memo](MINIMAL_AXIOMS_2026-06-29.md)
separates the four axioms from Hamiltonian and occurrence selection. The
strongest missing physical lemma is a selected complete metric coupling on
this carrier with consistent interacting stress and dynamical constraints.
That lemma is stronger than the static results proved here; those results
are not described as near closure of the full TOE.

The motivating current-main source is
`THE_VACUUM_RESPONSE_UNDER_THE_RATE_RULER_ANTI_SCREENS_AND_THE_SEA_REFERENCED_SOURCE_REMOVES_IT_BOUNDED_THEOREM_NOTE_2026-09-04.md`
at `b8c9d9d819911c5f3fec98b23d53355e7ff8c8bf`. Its corrected final section leaves
the complete finite susceptibility action and physical source law open.
Its old axial fits are not a premise or a coefficient input here.

## Native dictionary and protected realization

Use Theorems1–2 of the [native edge/CAR source](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md),
at the same pinned main revision, with ordinary tensor composition and the
specified cycle-code hypotheses. For virtual vertices v place the physical
edge qubit at2v+e_a. With fixed oriented incident-edge orders,

    B_v=product_(e incident v) Z_e,
    A_vw=epsilon_vw X_vw product_(u<_v w) Z_vu
                              product_(u<_w v) Z_wu.

The cycle S_C=i^length product_ordered A_e is central. On its positive code,
B_v=1-2n_v and A_vw=-i gamma_(2v)gamma_(2w). For a simple path p,
A_p=i^(length-1)product_ordered A_e=-i gamma_(2v0)gamma_(2vlast), by ordered
cancellation of all internal Majoranas. Therefore

    T_p=(i/2)A_p(B_v-B_w)=c_v^*c_w+c_w^*c_v,
    J_p=-A_p(1-B_v B_w)/2=i(c_v^*c_w-c_w^*c_v).

Real and imaginary parts of every hopping below are these even words.
The quartic onsite factor is lambda B_(x,0)B_(x,1)/4. Nonbridge single-edge
Z readout has branch isometry sqrt(2)Q_z on the incoming code and preserves
all surviving even words: an incoming cycle anticommutes with that Z, so
P_code Z P_code=0; surviving words commute with Q_z. The candidate matching
below leaves a protected detour for each measured edge, even after other
candidate deletions. Thus every stated energy cell and lapse-weighted term
intertwines the event. This is conditional algebraic compatibility with
supplied Born readout, rather than an autonomous formation or lapse law.

For v(x,r)=(2x1+r,x2,x3), the required virtual displacements are2e_x for
same-orbital x hops, e_x or3e_x for different-orbital x hops, e_y and e_z
for same-orbital hops, and plus/minus e_x plus/minus e_y for offdiagonal y
hops. All x,z edges are protected. A candidate y hop uses its x-plaquette
detour. In a diagonal xy path, choose x first or last so the y tail has even
x+y. Each path has length at most3. In a finite open model box, the virtual
x width is at least2; use the negative-x detour at its maximum x boundary
and positive-x elsewhere. No exiting model hop is included. Periodic
wrap bonds in the spectral calculation are a finite regulator; they are
not claimed to be bounded physical paths in an open cubic embedding.

## 1. One native Hamiltonian, explicit energy cells

Use two orbitals per model cell x, with Fourier convention
c_x=V^-1/2 sum_k exp(-ik.x)c_k. Fix zeta in[1/2,1), and set

    W1=(-sigma3+i sigma1)/2, W2=(-sigma3+i sigma2)/2,
    W3=-sigma3/2,
    O_x=(2+zeta-nu)(n_x0-n_x1)
                       +lambda(n_x0-1/2)(n_x1-1/2),
    B_xa=c_x^* W_a c_(x+a)+c_(x+a)^* W_a^* c_x,
    h_x=O_x+(1/2)sum_a(B_xa+B_(x-a),a),
    H0=sum_x h_x.                                           (S1)

Omit absent boundary bonds in an open box. The numbers lambda and nu are
supplied. At lambda=nu=0, the one-body symbol is h(k)=d(k).sigma with

    d=(sin k1,sin k2,2+zeta-cos k1-cos k2-cos k3).            (S2)

The nodes are (0,0,+/-acos zeta). Their derivative determinants have magnitude
v3=sqrt(1-zeta^2), with velocity matrices diag(1,1,+/-v3). Nothing below
imports an interacting response theorem from the interacting Weyl propagator.

Use the following protected native geometry. Virtual
orbitals lie at v(x,r)=(2x1+r,x2,x3); physical vertices are2v and edge qubits
2v+e_a. Candidate y edges have tail x+y odd, form a matching, and are deleted
on scalar-effect Record events. Other edges are protected. Each used hopping
has a protected simple path of length at most3; a candidate y segment is
replaced by its x-plaquette detour. The native even-CAR dictionary supplies
the real/imaginary hopping and B_v=1-2n_v. All these words commute with
candidate Z_e and cycle stabilizers. Hence every h_x, not just their sum,
is intertwined by the scalar-effect candidate Record branch isometry.
Multiplying their terms by the lapse coefficients below does not alter this
algebra. Lapse variables are independent supplied apparatus/geometry data;
their physical Record encoding and genesis remain open. A fixed global-even
code can represent an odd-particle filled band by adding one idle occupied
spectator fermion; all sources here are even and unchanged by that spectator.

The exact interacting continuity identity at N=1 is

    dot h_x + sum_y j_xy=0,  j_xy=i[h_x,h_y]=-j_yx.          (S3)

Only overlapping finite energy cells contribute, because disjoint even CAR
operators commute. This is energy continuity with a bounded-range current.
It does not supply the spatial momentum identities needed for a complete
symmetric gravitational stress tensor.

## 2. Arithmetic lapse and its actual variational source

For real positive cell lapses N_x define

    H_A[N]=sum_x N_x h_x
          =sum_x N_x O_x+sum_(x,a) (N_x+N_(x+a))B_xa/2.     (S4)

In the free one-body model this is {N,h0}/2, with N acting equally on both
orbitals at a cell. Its derivative is exactly h_x. A concrete reciprocal finite model uses a
supplied classical canonical pair(Phi,Pi), normalized quantum state psi and
energy H_g(Phi,Pi)+<psi|H_A[1+gPhi]|psi>. With

    dot Phi=partial_Pi H_g,
    dot Pi=-partial_Phi H_g-g<psi|h_x|psi>,
    i dot psi=H_A[1+gPhi]psi,

the chain rule cancels the geometry/matter exchange terms and conserves that
time-independent total energy for every smooth solution in the positive-lapse
domain. The Schrödinger contribution from H_A commutes with itself. Thus one
specified coupling supplies both source force and matter evolution. This
finite mean-field model is supplied; Einstein constraints, metric selection
and a physical clock remain separate targets.

For finite volume assume an isolated simple many-body ground state Omega of
H0 in the declared sector, and let E_A[N] be its ground energy near N=1.
The source and Hessian are

    rho_x[N]=partial E_A/partial N_x=<h_x>_N,
    chi_A,xy=-2 Re <Omega|h_x Q(H0-E0)^-1 Q h_y|Omega>.      (S5)

The reduced inverse is on Q=I-|Omega><Omega|. Differentiating the normalized
eigenvalue equation proves (S5); a finite gap is its hypothesis. Thus chi_A
is real symmetric negative semidefinite. E_A itself is concave, since it is
an infimum of linear functions of N. Also chi_A 1=0, because sum h_x=H0
has no ground-to-excited matrix element. Exactly E_A[c1]=cE0 for c>0.
These finite statements include the local quartic interaction, provided its
coefficient and the counterterm are also multiplied by N as in(S4).

A fixed reference only adds a linear functional. For example

    R_A[N]=E_A[N]-E_A[1]-sum_x(N_x-1)rho_x[1]               (S6)

has the same Hessian. R_A[c1]=0. Subtracting a newly dressed ground energy
from itself instead defines zero and removes the response by choice.
At a general inhomogeneous N, sum_x(rho_x[N]-rho_x[1]) equals
<Omega_N|H0|Omega_N>-E0>=0; it need not vanish beyond linear order.
A projected linear zero mode therefore gives no cosmological conclusion.

The source is not generally the energy density of the N-dependent Hamiltonian.
In the free model it is Re tr_orb[h0 P_N]_(x,x), because H_A'={P_x,h0}/2.
The readout Re tr_orb[h_A[N]P_N]_(x,x) uses a different operator. For N=c1,
the source stays fixed but this readout is multiplied by c. In particular,
feeding the latter into a response equation can create a uniform derivative
which is absent from the actual variation. This is an exact finite separator,
not a diagnosis of every previous source convention.

## 3. All-momentum free response, with normalization fixed

Take a periodic free lattice without a zero one-body eigenvalue, fill its
negative band, and use the whole Fock ground energy. Equivalently fix its
particle number while the gap stays open. Write E=|d(k)|, E'=|d(k+q)|,
n=d/E, n'=d'/E'. If Phi_x=sum_q exp(-iq.x)Phi_q, define

    (E_A[1+epsilon Phi]-E_A[1]-linear)/V
            =(epsilon^2/2)sum_q chi_A(q)|Phi_q|^2
                            +o(epsilon^2).                 (S7)

The vertex is V(k,q)=[h(k+q)+h(k)]/2. Between a negative-band state at k
and a positive-band state at k+q it gives

    <+,k+q|V|-,k> = (E'-E)<+,k+q|-,k>/2,
    |<+,k+q|-,k>|^2=(1-n.n')/2.                            (S8)

Finite eigenvalue perturbation theory, including both Hermitian Fourier
directions in(S7), therefore gives

    chi_A(q)= -(1/V)sum_k
          [(E'-E)^2/(4(E+E'))](1-n.n').                    (S9)

This is every q in the finite reciprocal lattice, not an axial fit. The
thermodynamic response replaces V^-1 sum by integral_T3 d^3k/(2pi)^3.
The integrand extends boundedly at its zero-energy exceptional points by
the estimate (E'-E)^2/(E+E')<=E+E'. It is Riemann integrable; its values at
the isolated nodes do not affect the integral. A limiting response is thereby
defined without silently assuming an infinite-volume gapped ground state.
Both finite and integral responses are even in q, nonpositive, and zero at q=0.
For a commensurate q requiring a box with an untwisted zero mode, use an
antiperiodic boundary condition in the first direction: k1=(2n+1)pi/L1.
It never reaches the native nodes' k1=0, while the source transfers remain
2pi m/L. This supplies gapped finite approximants for every transfer sequence.
The twist tends to zero in the thermodynamic limit. Uniform boundedness and
uniform convergence outside arbitrarily small neighborhoods of the finitely
many exceptional points justify the corresponding Riemann-sum limit.

The cancellation in(S8) is essential: substituting a charge-density vertex
would remove the factor(E'-E)^2 and gives a different infrared response.

## 4. Quartic-logarithmic infrared term

For fixed zeta<1 set Q=(q1,q2,v3 q3), D=v3. The integral asymptotic is

    chi_A(q)= -|Q|^4/(120 pi^2 D) log(1/|Q|)+O(|q|^4).      (S10)

This takes the thermodynamic limit first and then q->0. Its constants may
depend on zeta and are not uniform near node merger zeta->1. Changing the
dimensionless logarithm's fixed scale changes only the O(q^4) remainder.

Here is the leading-term calculation; the complete uniform estimate is in section10. Outside fixed
small node neighborhoods, E is bounded below. Each factor E'-E is O(q),
and 1-n.n'=(1/2)|n'-n|^2 is O(q^2); the exterior integral is O(q^4).
At one simple node use p=d(k) as local coordinates. Its Jacobian density is
D^-1+O(|p|), and d(k+q)=p+V_node q+O(|p||q|+|q|^2). In the inner ball
|p|<=C|q|, the integrand is O(|q|), hence its integral is O(q^4).
In the annulus C|q|<|p|<delta, Taylor expansion gives the integrand of minus
chi_A, to leading order,

    [(p_hat.Q)^2 (|Q|^2-(p_hat.Q)^2)]/(16 |p|^3 D).       (S11)

The angular integral of cos^2(theta)(1-cos^2(theta)) is8pi/15. Together with
(2pi)^-3 and1/16, one node contributes |Q|^4/(240pi^2D) times the radial
integral dr/r. The two nodes have the same |Q| and |det V|.
The nonlinear-coordinate/Jacobian remainder is bounded by C q^4/r^2;
the next finite-transfer Taylor remainder by C |q|^5/r^4, on that annulus.
Multiplication by r^2dr and integration bounds both by O(q^4). Boundary
cutoff changes also contribute O(q^4). The complete uniform annular estimates are proved in section10. The proof
uses a fixed nondegenerate-node chart and no fitted exponent or coefficient.

## 5. A global bound for the arithmetic response

Let L(q)=sum_i4sin^2(q_i/2). The increment d(k+q)-d(k) is M p(q), where

    M=[[cos(k1+q1/2),0,0],
       [0,cos(k2+q2/2),0],
       [sin(k1+q1/2),sin(k2+q2/2),sin(k3+q3/2)]].

Its squared Frobenius norm is2+sin^2(k3+q3/2)<=3, so
(E'-E)^2<=3L(q). Using overlap<=1 and
1/(E+E')<=(1/E+1/E')/4 in(S9) yields

    0<=-chi_A(q)<= (3/4) I1 L(q),
    I1=integral_T3 [1/E(k)]d^3k/(2pi)^3.                  (S12)

The same finite bound uses I1,V=V^-1 sum1/E where the finite band is gapped.
For the integral, E>=sqrt(sin^2k1+sin^2k2). Fold each coordinate to[0,pi/2]
and use sin x>=2x/pi. Since integral_[0,a]^2(dxdy/sqrt(x^2+y^2))
=2a asinh(1), one gets I1<=2 asinh(1). Thus

    -chi_A(q)<= [3 asinh(1)/2] L(q).                      (S13)

This is deliberately loose, but it is global and has no fitted susceptibility.
In a supplied mean-zero static functional

    F_A[Phi]=kappa Phi.L.Phi/2+R_A[1+g Phi]+g rho_ext.Phi, (S14)

the linear Hessian is kappa L+g^2 chi_A. It is positive at every nonzero
integral momentum if kappa>3g^2 asinh(1)/2. In finite volume the bound uses
3g^2 I1,V/4; the exact finite eigenvalues can also be checked directly.
For a finite gapped model a positive Hessian gives a unique nearby stationary
branch for sufficiently small mean-zero external source by the ordinary
finite-dimensional implicit-function theorem. No global large-field claim or
physical G follows. By(S10), this particular free vacuum correction does not
change the leading small-q Laplacian coefficient.

## 6. A competing local lapse law: contact terms change the answer

The arithmetic rule is NOT the only positive local homogeneous lapse law.
Define a geometric-mean rule on the same bonds,

    H_C[N]=sum_x N_x O_x+sum_(x,a) sqrt(N_x N_(x+a)) B_xa. (S15)

It agrees with H_A at uniform N and to first order about N=1. In the free
one-body theory it is exactly sqrt(N) h0 sqrt(N), a congruence. It has the
same native word supports and Record intertwining. It preserves the inertia
of finite h0 for every positive N; if h0 has a gap delta, its singular values
remain at least (min N)delta. This is an additional mathematical advantage,
not selection by the axioms.
Its actual free source at general N is
rho_C,x[N]=Re tr_orb[h_C[N]P_N]_(x,x)/N_x, obtained by differentiating both
square roots. Thus a local energy readout must be divided by its lapse to
give this family's source. This is a consequence of(S15), not a universal
rule for every physical energy observable.

For a diagonal perturbation Phi,

    h_C[1+epsilon Phi]=h0+epsilon{Phi,h0}/2
                           -epsilon^2[Phi,[Phi,h0]]/8+O(epsilon^3).

Thus the second derivative adds the contact operator
-[Phi,[Phi,h0]]/4. If E_i<0<E_j are the one-body energies, the arithmetic
paramagnetic Hessian contribution for a matrix element Phi_ji is

    -(E_i+E_j)^2 |Phi_ji|^2/[2(E_j-E_i)],

and the contact contribution is(E_j-E_i)|Phi_ji|^2/2. Their sum is

    -2 E_i E_j |Phi_ji|^2/(E_j-E_i)>=0.                  (S16)

Occupied-occupied pairs cancel in the contact trace. Consequently the full
free congruence response at every lattice momentum is

    chi_C(q)=(1/V)sum_k [E E'/(E+E')](1-n.n')>=0.        (S17)

The signs in(S9) and(S17) are opposite even though the uniform Hamiltonian
and first-order source vertex are identical. The second-order lapse law is
therefore a load-bearing physical input. The two explicitly constructed families are the stated discriminator.
Physical selection of a complete gravitational coupling remains an open target.

Let b_a=<B_xa>_0 per cell. The same contact term gives the exact local identity

    chi_C(q)-chi_A(q)=-(1/4)sum_a b_a 4sin^2(q_a/2).      (S18)

It follows either from the bond expansion or by summing the positive
interband contact matrix elements. In the integral model,

    b_a=-integral E(k)|partial_a n(k)|^2 d^3k/(2pi)^3<0.  (S19)

To derive(S19), write d=d0+sum_a d_a with partial_a^2 d=-d_a and integrate
partial_a^2 E=0 over the torus. The node boundary term vanishes in three
dimensions. Each n depends nontrivially on each coordinate, so the integral
is strictly positive. Thus the congruence response has a positive quadratic
term, plus the SAME negative quartic-logarithmic term(S10), and analytic
quartic terms from the lattice sine factors. No cosmological mass term is
created. The coefficients b_a and kappa remain selected-model quantities.

## 7. Global free convexity and a finite static existence result

The positive congruence Hessian has a global explanation. For any finite
Hermitian one-body h0 and N>0,

    E_C[N]=(Tr N h0 - F(N,h0 N h0))/2,
    F(A,B)=Tr sqrt(sqrt(A) B sqrt(A)).                     (S20)

Indeed the second term is Tr|sqrt(N)h0 sqrt(N)|, and the sum of negative
eigenvalues is(Tr h-Tr|h|)/2. The fidelity variational identity is

    F(A,B)=inf_(X>0) [Tr A X+Tr B X^-1]/2.                (S21)

For A>0 set C=sqrt(A)Xsqrt(A), D=sqrt(A)Bsqrt(A).
The Hilbert-Schmidt norm of C^1/2-C^-1/2 D^1/2 squares to
Tr C+Tr D C^-1-2Tr D^1/2, proving the bound; C=D^1/2 attains it when
D>0. Singular cases follow by continuity. Substituting B=h0 N h0 makes
each objective linear in N, so F is concave and E_C is convex. This proof
is included rather than treating a source label as evidence of the sign.

On a finite connected torus with mean(Phi)=0, replace R_A in(S14) by the
tangent-subtracted R_C. It is nonnegative and convex for1+gPhi>0. If kappa>0,
the resulting static functional is strictly convex, hence has at most one
interior stationary point. Let lambda1 be the first positive eigenvalue of L.
For a mean-zero source and g>0, the condition

    2g^2 ||rho_ext||_2 < kappa lambda1                     (S22)

ensures existence of an interior minimizer: on the positivity boundary some
Phi_x=-1/g, so||Phi||>=1/g, while
F_C>=kappa lambda1||Phi||^2/2-g||rho_ext|| ||Phi||>0 there.
The mean-one nonnegative lapse simplex is compact, its energy extends
continuously to the boundary, and F_C(0)=0. The unique minimizer is therefore
interior. At stationarity convexity gives the sharper bound
||Phi||<=g||rho_ext||/(kappa lambda1). These are finite mathematical facts
for a supplied static field functional and free filled-band matter.

## 8. Boundaries to keep open

The free congruence identity(S20) is a one-body filled-band fact. The local
quartic extension(S15) is not a global congruence of the many-body Hamiltonian.
Neither global convexity nor the free q^4 log q coefficient may be exported
to it. The arithmetic finite spectral formula(S5) remains valid under its
gap hypothesis. Interacting infrared stress response, geometry-dependent
counterterms and metric contact terms require their own proof.

The static Laplacian in(S14) is a supplied scalar field functional. A full
metric variation, conserved spatial stress and dynamical constraints remain
separate mathematical targets. The lapse data are
supplied, and the pure scalar-effect native Record events do not measure the
matter energy. Quantum-to-Record calibration, a common physical clock,
formation of the lapse/controller data, actual law selection and independent
review remain open. No axiom update is forced by either construction.

## 9. Exact finite interacting witness and author review

The following is an existence witness in a declared finite canonical sector.
Use three open cells, W1 hopping only, onsite mass5/2, lambda=-20 and three
particles in six orbitals. Set N^+=(1.001,0.998,1.001) and
N^-=(0.999,1.002,0.999). Their midpoint is1 and all lapses are positive.
The frozen rational vectors in the primary runner
and its direct occupation-basis verifier establish exactly

    E_C[1] > -8.34999098,
    (E_C[N^+]+E_C[N^-])/2 < -8.35007260.

The first inequality follows from20 strictly positive rational LDL pivots
and exact reconstruction of H_C[1]+8.34999098 I. The second follows from
Rayleigh upper bounds on two fixed Gaussian-integer trial vectors; rational
square-root brackets enclose the geometric bond factors. The midpoint gap
exceeds8/100000. The checker constructs occupation-basis CAR signs directly,
without importing the other Fock checker or calling an eigensolver. Numerical
search found the vectors, but does not establish the inequalities.
This witness concerns a fixed three-particle sector at strong attraction.
No small-coupling theorem is invoked for this parameter. The witness supplies
no statement about its grand-canonical ground sector or thermodynamic limit.

Section10 gives the complete uniform infrared proof, including a
separate exact prolate-coordinate cone integral. All finite source and
contact identities have been challenged using the actual position-space
Hamiltonian and a separate literal Fock construction. Cold review found a
nonzero-current guard with mismatched matrix dimensions; the corrected guard
passes and the original bytes are preserved. A weak two-cell response fixture
and a finite-difference truncation failure are preserved separately.
Independent review is still pending. The review record below identifies the
source revisions and the scope of the author checks.

## 10. Uniform infrared remainder and exact cone coefficient

Define for nonzero p,p+t

    f(p,t)=[(|p+t|-|p|)^2/(4(|p+t|+|p|))]
                              [1-p.(p+t)/(|p||p+t|)].

It is nonnegative. The bound f<=(|p|+|p+t|)/2 extends it boundedly across
the exceptional points in any bounded region. For |t|<=|p|/2, write r=|p|,
u=p/r. Homogeneity gives f(p,t)=r f(u,t/r). On the compact set |u|=1,
|t/r|<=1/2, all derivatives through order5 in t/r are bounded. Moreover,

    |p+t|-r=u.t+O(|t|^2/r),
    1-u.(p+t)/|p+t|=|t-u(u.t)|^2/(2r^2)+O(|t|^3/r^3).

The denominator is8r+O(|t|). Multiplication gives the uniform estimate

    | f(p,t) - (u.t)^2[|t|^2-(u.t)^2]/(16r^3) |
                         <= C |t|^5/r^4.                  (IR1)

The compact derivative bound justifies the constant uniformly over all
directions, including u.t=0. No division by a directional scalar is used.

At each simple node k*, d is a diffeomorphism in a fixed neighborhood.
Use a fixed p-ball |p|<delta in its image and its inverse k(p). For all small q,

    t(p,q)=d(k(p)+q)-p=V_* q+R(p,q),
    |R(p,q)|<=C(r|q|+|q|^2),
    |det Dk(p)|=1/|det V_*|+O(r).                        (IR2)

These follow from the bounded second derivatives of d and bounded first
derivatives of k(p). Choose a fixed A large enough that r>=A|q| implies
|t|<=r/2. Inside r<A|q|, the bound on f and(IR2) gives f<=C|q| and the
volume is O(|q|^3); this entire part is O(q^4).

On A|q|<=r<=delta apply(IR1). Its error is C|q|^5/r^4. Replacing t by
Q_*=V_*q in the quartic numerator changes it by at most
C|q|^3|R|/r^3 <= C(|q|^4/r^2+|q|^5/r^3).
The latter term is bounded by a constant times |q|^4/r^2 on this annulus.
Replacing the Jacobian by |det V_*|^-1 contributes another C|q|^4/r^2.
After multiplying by the spherical measure r^2dr, the integrated errors are

    C |q|^4 integral_(A|q|)^delta dr
    + C |q|^5 integral_(A|q|)^delta dr/r^2 = O(|q|^4).    (IR3)

The region outside the fixed node p-balls is compact and bounded away from
zero energy; its integrand is O(q^4). These fixed regions partition the
original Brillouin zone, so no omitted moving-cutoff term is required.
The leading node integral is

    |Q_*|^4/[240 pi^2 |det V_*|]
                        log(delta/(A|q|)).                (IR4)

For fixed invertible V_*, log|Q_*|-log|q| is uniformly bounded on the unit
q-sphere. Replacing the logarithm by log(1/|Q_*|) changes only O(q^4).
Both native nodes have |det V_*|=sqrt(1-zeta^2) and the same |Q_*|, proving

    chi_A(q)=-|Q|^4/[120 pi^2 sqrt(1-zeta^2)]
                              log(1/|Q|)+O(|q|^4).

The estimates prove a bounded fourth-order remainder, not an analytic one.
No uniform constants at the merging-node endpoint are asserted.

### A separate exact cone integral

For one exactly linear cone in p coordinates, let Q=|Q_*|>0 and use the
prolate spheroidal variables with foci0 and-Q_*:

    u=(E+E')/Q in[1,infinity), v=(E'-E)/Q in[-1,1],
    E=Q(u-v)/2, E'=Q(u+v)/2,
    1-n.n'=2(1-v^2)/(u^2-v^2),
    d^3p=Q^3(u^2-v^2)du dv dphi/8.

Substitution into the arithmetic integrand gives the exact product

    f d^3p = Q^4 v^2(1-v^2)du dv dphi/(16u).

With the DECLARED ellipsoidal cutoff E+E'<=Lambda, Lambda>Q, angular and v
integration yields exactly

    integral f d^3p/(2pi)^3
                    =Q^4 log(Lambda/Q)/(240pi^2).         (IR5)

Division by |det V_*| gives the anisotropic cone coefficient independently
of the Taylor expansion. This auxiliary cutoff is a check of the logarithmic
coefficient. It is not the actual Brillouin-zone integral and does not fix its
fourth-order constant or any induced Newton coefficient. In particular,
continuum unbounded Dirac sea traces and their contact terms cannot be moved
cyclically as finite traces without a regulator. The complete second-order
arithmetic/congruence comparison is made on the finite lattice in(S16)-(S18),
where all such operations are legitimate.

## No-Go Discipline Gate

The shipped statements are positive conditional theorems and two explicitly
constructed lapse families, plus one finite canonical existence witness.
No family of physical gravity laws or axiom realizations is declared
impossible. N1: the actual constructions examined are arithmetic and
geometric bond coupling, finite interacting canonical energy, and a free
static source functional; these are not five exhausted routes, and no
exhaustion PASS is claimed. N2: no independent wall count is asserted.
N3: supplied quantum representation, state, coupling and geometric functional
are explicit premises above. N4: the only load-bearing external repository
source is the native code dictionary, used for exactly that algebra; the
vacuum-response note is motivating provenance only. N5: site, mode, block and
integral domains are stated explicitly and emitted by the runner. The strong
interaction statement has one finite sector, not an untested generalization.
N6: no new axiom or primitive is proposed. N7: a physical lapse law with
additional contact terms, nontrivial state selection or a different interacting
regime is a live downstream construction; these results do not close it.
N8: the corrected prior vacuum-response note already separates fixed and
dressed references and withdraws axial full-zone inference; this note uses
that lesson and supplies a different explicit native-model derivation.
This is a scope audit, not a negative-theorem packet PASS.

## Review record and verification limits

Author derivations and finite checks are proposals awaiting independent
review. All three finite families are in the primary runner; no unmerged
campaign runner, sibling PR or helper registry change is required.
The free position-space checker tests all27 momenta of a3-by-3-by-3 torus,
finite source derivatives, actual bond contact terms and a nonlinear static
stationary solution. A separate literal six-mode Fock construction checks
nine couplings in the three-particle sector, and direct occupation-basis
rational LDL verifies the midpoint witness without an eigensolver.
The native Pauli commutation check uses a4-by-2 virtual rectangle; the
general native code theorem is the linked premise, not that finite fixture.

The free thermodynamic limit and uniform infrared remainder are analytical
arguments. The exact cone integral checks the logarithmic coefficient under
its declared auxiliary cutoff. Neither a finite torus nor the cone cutoff
establishes the entire infinite-zone fourth-order remainder. The global
convexity proof uses finite trace variational algebra; no unregulated
infinite Dirac-sea trace is moved cyclically.

A two-cell fixture with a zero source response was replaced by a three-cell
fixture that exercises the response. A strong-coupling finite-difference
failure was resolved by a preserved45-digit step-refinement calculation:
its error decreased by the expected fourth-order factor. The primary uses
a smaller step in that declared regime at the original tolerance. Cold
review also repaired a nonzero-current guard comparing different matrix
sizes. The original bytes and failures are preserved in the review packet.
Vocabulary/diff checks, effective mutations, canonical cache and direct
readiness evidence are recorded in the packet. Full integrated pipeline and
independent review/audit belong to the later landing path. No science is
merged by this author milestone.
