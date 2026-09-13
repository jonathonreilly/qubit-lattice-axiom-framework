---
claim_id: native_weyl_stress_logarithm_and_contact_response_bounded_theorem_note_2026-09-13
claim_type: bounded_theorem
claim_scope: "For the specified free native two-orbital Wilson carrier and joint arithmetic lapse/frame source: derive the seven-source real symmetric even-frequency Hessian including its mixed contact, prove its uniform thermodynamic infrared stress logarithm, and derive the exact continuum two-particle spectral density. Construct a native local density-contact family with the same flat and first-order matter data and different spatial gradient vacuum coefficients. The Hamiltonian, free state, frame, source coupling and time are supplied. The result concerns the seven-source restriction of the leading nonanalytic tensor, not a complete dynamical metric or Einstein action."
upstream_dependencies:
  - native_edge_record_matter_instrument_and_energy_ledger_bounded_theorem_note_2026-09-05
runner: scripts/native_weyl_stress_logarithm_contact_response_2026_09_13.py
---

# Native Weyl stress, its infrared logarithm and local metric contacts

**Date:** 2026-09-13
**Type:** bounded_theorem
**Status:** proposed_retained

## Target and premise account

Derive the stated native lapse/strain Hessian with its contacts, prove its
leading nonanalytic tensor with a uniform remainder, and construct explicit
source couplings that vary its local spatial gradient coefficients while
preserving the given continuum matter operator.

~~~yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "Analytical response and infrared theorems for a specified free native Hamiltonian, with separate exact algebra and finite spectral challenges."
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "A metric source and induced action on the same native matter carrier, with their remaining dynamical choices explicit."
source_of_blocker_text: user_goal
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Test a physical selection principle for the local metric action, its canonical sources and constraints."
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
~~~

| Premise or obligation | Role | Disposition |
|---|---|---|
| Lattice, Qubit, Admissibility and Record | Framework ontology | Used only for the stated conditional placement |
| Ordinary tensor composition and the edge/CAR cycle code | Mathematical realization in the linked current-main source | Supplied representation, with its parity hypotheses |
| Free Wilson Hamiltonian, half-filled negative band and continuous Hamiltonian time | Model and state specification | Supplied; no observed or fitted input selects them |
| Six symmetric strains, lapse and the scalar connection function | Declared source family | Defined explicitly below; its expansion is derived |
| Finite spectral response and contacts | Mathematical subtarget | Derived below and checked against direct position-space matrices |
| Uniform native logarithm | Mathematical subtarget | Node-jet, annulus and integrability proof below |
| Continuum spectral normalization | Separate mathematical check | Exact ellipsoid phase space and dispersion integral below |
| Local density-contact family | Further source construction | Native support, exact expectation and continuum scaling proved below |
| Metric dynamics, shift sources, interacting stress and source selection | Physical continuation | Open; stronger than this free response theorem |

The [framework memo](MINIMAL_AXIOMS_2026-06-29.md) distinguishes its minimal
axioms from a selected Hamiltonian and occurrence law. The strongest missing
physical lemma is a native dynamical metric whose source law and local action
are selected and whose interacting constraints are consistent. No new axiom,
primitive, Newton constant, empirical value or formal audit status is added.

The results below use fixed zeta in [1/2,1); estimates are not uniform at
node merger. Thermodynamic limits precede small external momentum. Finite
numerical challenges use compatible gapped grids and preserve the native
even-parity restriction. The field remains in a neighborhood of the flat
invertible frame and positive lapse when its derivatives are taken.

## Native realization of the source family

The following finite-range placement and occupation dictionary accompany
the source family. Its vertex functions, node jets, connection expansion
and response proofs are specified in this note.

The current-main source
[native edge/CAR theorem](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md)
at b8c9d9d819911c5f3fec98b23d53355e7ff8c8bf, Theorem 1, supplies the
conditional ordinary-tensor edge-qubit cycle code. Its dictionary is

    B_v=product_(e incident v) Z_e=1-2 c_v^* c_v,
    A_vw=-i gamma_(2v) gamma_(2w),
    gamma_(2v)=c_v+c_v^*.

For an ordered simple path p from v to w of length l, canceling the internal
Majoranas gives A_p=i^(l-1) product_p A_e=-i gamma_(2v) gamma_(2w). Thus

    T_p=i A_p(B_v-B_w)/2=c_v^*c_w+c_w^*c_v,
    J_p=-A_p(1-B_v B_w)/2=i(c_v^*c_w-c_w^*c_v).

Both real and imaginary hopping coefficients are therefore finite physical
operators. A cell's n_x is the sum of its two bounded-star occupation
projectors. It is not a single physical edge-Z event. The unaugmented finite
code represents even total fermion parity; choose an even number of cells
for a half-filled state. The 60-cell position checks obey that restriction,
and the thermodynamic argument can use even-volume sequences.

Place orbital r in {0,1} of cell x at virtual v=(2x1+r,x2,x3), with actual
edge qubits at doubled virtual-edge centers as in the source. Protect every
x,z edge and the y edges whose lower-y tail has even x+y. Each unprotected
y edge has a protected x-plaquette detour. The trigonometric frame vertices
below have only these path types:

| Symbol contribution | Orbital action | Protected path length |
|---|---|---|
| sigma1 or sigma2 times sin k1 | Flip orbital, one x cell | At most 3 |
| sigma1 or sigma2 times sin k2 | Flip orbital, one y cell | 2, choosing the x/y ordering |
| sigma1 or sigma2 times sin k3 or sin 2k3 | Flip orbital, one or two z cells | At most 3 |
| sigma3 sin k3 sin k1 | Same orbital, x and z cell displacement | 3 |
| sigma3 sin k3 sin k2 | Same orbital, y and z displacement | At most 4, with an x detour if needed |
| sigma3 cos k3, scalar sin k3, or on-site terms | Same orbital | At most 1, or the occupation star |

The flat Wilson cos k1 term uses two x edges; cos k2 uses either one
protected y edge or a three-edge x detour; cos k3 uses one z edge. These
statements hold on the infinite graph and on open boxes with enough x width
to take an inward detour. A periodic Fourier regulator is an auxiliary
operator computation, not a short physical wrap edge in an open box.

Record compatibility is only the current-main conditional one: on a
surviving cycle the physical Z projector has a fair isometric restriction,
and every surviving even word intertwines it. A prepared initial code,
ordinary quantum composition, Hamiltonian, state and Born interpretation
remain supplied. This note supplies no formation rate, autonomous control,
strict nearest-neighbor admissibility distribution or axiom-selected metric.

## Strain and joint lapse response

Use the free filled negative band, the specified common-frame coupling,
and the ground-state response convention below.

### 1. Frame coordinates and the contact term

Write D=diag(1,1,v), v=sqrt(1-zeta^2), zeta in [1/2,1), and F=(I+S)D,
where S is a real symmetric matrix field. Use the nine native vertices

    V_aj = sin k_j                              (a<3,j<3),
    V_a3 = (zeta-cos k3) sin k3/v^2              (a<3),
    V_3j = sin k3 sin k_j/v                      (j<3),
    V_33 = (zeta-cos k3)/v.

Indices in these formulas run from 1 to 3. The flat symbol is
d=(sin k1,sin k2,2+zeta-cos k1-cos k2-cos k3). Its only zeros are
(0,0,+/-acos zeta): d1=d2=0 forces k1,k2 to 0 or pi; either pi gives
d3>=1+zeta, and with both zero d3=zeta-cos k3. The principal deformation
is 1/2 sum_aj {S_aj(x) D_jj, sigma_a V_aj(k)}. Its two node tangents
are R_w F, R_w=diag(1,1,w), w=+/-1.

Define the scalar half-density connection coupling by

    C(F)=-1/4 epsilon_abc F_ai (partial_i F_bj) (F^-1)_jc.     (R1)

Its geometric convention can be reconstructed directly. For the orthonormal
frame e_a=F_ai partial_i and metric g=(F^T F)^-1, write
c_ab^c=(F_ai partial_i F_bj-F_bi partial_i F_aj)(F^-1)_jc and
omega_abc=<e_b,nabla_(e_a) e_c>. The Koszul formula gives
epsilon_abc omega_abc=-epsilon_abc c_ab^c/2. In the half-density Dirac
operator, the scalar part of -i sigma_a F_ai A_i, with
A_i=omega_i bc sigma_b sigma_c/4, is epsilon_abc omega_abc/4 by the
Pauli triple-product identity. Substitution gives R1. The vector part,
combined with the half-density volume correction, is the symmetric
first-order expression -i sigma_a(F_ai partial_i+partial_i F_ai/2).
Explicitly, sum_a omega_aac=div_g e_c=partial_i F_ci+Gamma^k_ki F_ci;
the vector part is -i sigma_c div_g e_c/2, and the half-density correction
+i sigma_c F_ci Gamma^k_ki/2 cancels the volume term.
For the opposite node Clifford matrices the scalar has the extra sign w.
The chosen native multiplier B0 below has precisely that value at the node.

Put S=t A(x)+u B(x), each symmetric. Expanding (I+S)^-1 gives

    C_1=0,
    C_2=1/4 epsilon_abc D_aa (partial_a S_bj) S_jc.           (R2)

The linear contraction vanishes because partial_a S_bc is symmetric in bc.
The other quadratic term has S_ai partial_i S_bc and vanishes for the same
reason. For a single fixed polarization S=A phi(x), C_2=0 since A^2 is
symmetric. Mixed noncommuting polarizations need not have zero C_2.

The native scalar coupling is 1/2 {C(F),B0(k)} I2,
B0(k)=sin k3/v (lattice spacing is temporarily one). At the flat filled-band
state, tr_orb P_-(k)=1 for every nonzero-energy k. Hence its total quadratic
ground-energy contact is exactly zero:

    Tr(P_- {C_2,B0}/2)=C_2(q=0) sum_k B0(k)=0.               (R3)

The last sum is zero on any full momentum grid of length at least two in z,
including a uniform boundary twist; it is also zero on the Brillouin torus.
This is a filled-band expectation, not a claim that the contact operator
vanishes. At a finite gapped grid the Taylor coefficient follows ordinary
finite-dimensional spectral perturbation theory.

### 2. Exact symmetric response

For a real symmetric polarization A define the real vector vertex

    u_A,a(k,q)=sum_j A_aj D_jj [V_aj(k-q/2)+V_aj(k+q/2)]/2.

Let d_-=d(k-q/2), d_+=d(k+q/2), E_+/-=|d_+/-|, n_+/-=d_+/-/E_+/-,
Delta=E_-+E_+. The Pauli trace identity gives

    2 Re tr[P_-(k-q/2) (sigma.u_A) P_+(k+q/2) (sigma.u_B)]
      =(1+n_-.n_+) u_A.u_B
       -(n_-.u_A)(n_+.u_B)-(n_-.u_B)(n_+.u_A) = J_AB.      (R4)

The real symmetric, frequency-even Euclidean response is

    chi_AB(i omega,q)=-int_BZ dk/(2pi)^3
                          Delta J_AB/(Delta^2+omega^2).    (R5)

In its finite-sum version, k-q/2 runs over the original momentum grid and
k+q/2 is its compatible translated grid; the integral notation is the
thermodynamic limit.

At omega=0 the two particle-hole orientations have opposite imaginary Pauli
traces and equal energy denominators, so R5 is the complete static Hessian
for these real traceless vertices. Its energy convention is
delta^2 E/V=sum_q S_A(-q) chi_AB(q) S_B(q). For a nonzero real cosine
source t A cos(q.x), its second derivative per volume is chi_AA(q)/2,
provided q and -q are distinct grid modes. For a constant source it is
chi_AA(0). The position-space checks use these conventions.

At every (omega,q), the symmetric form is nonpositive. This follows directly
from its interband squared matrix elements, not from sign samples. At q=0,
the continuum isotropic dilation has no interband vertex; the lattice
isotropic-strain vertex can differ from h0 by Wilson terms. No exact lattice
uniform-strain null direction is asserted. This response is only the real
symmetric, frequency-even part; parity-odd/Berry response is separate.

For a lapse source n(x), the arithmetic vertex is
sigma.[d(k-q/2)+d(k+q/2)]/2. In the linear cone its addition is equivalent
to replacing A by A+n I. Nonlinear lapse/frame contacts are local and must
be included when specifying the complete local action.

Specify the joint family H[N,S]={N,h_F[S]}/2, with N=1+n. At the flat
background its mixed second derivative is {n,{S_A,O_A}}/4, where
O_A(k)=sigma.u_A(k,0). The scalar C has zero first derivative and its
quadratic filled-band expectation vanishes by R3. The complete seven-source
even Hessian is therefore R5 plus the mixed lapse/strain contact

    chi_nA^contact(q)=-1/4 int_BZ dk/(2pi)^3 n(k).
                   [2u_A(k,0)+u_A(k+q,0)+u_A(k-q,0)].      (R9)

Here n(k)=d(k)/|d(k)| is the unit Bloch vector, distinguished from the lapse
source n(x). There is no n,n contact for this arithmetic choice, and no S,S
expectation contact by R3. Formula R9 follows by tracing the four terms of the nested
anticommutator. It is independent of frequency and a finite Laurent
polynomial in q. At q=0 it is the uniform strain one-point source <O_A>.
R5's nonpositive sign applies to the spectral response alone; the complete
seven-source Hessian includes R9 and need not have that sign. The chosen
joint source family is explicit and is not a selection from the axioms.

### 3. Exact infrared coefficient before the lattice remainder proof

Near a node rescale p=D(k-k_w); external Q=Dq; the measure acquires 1/v.
Use the node Clifford matrices tau_a=(R_w)_aa sigma_a. The continuum vertex
is tau.A p with a centered internal momentum. Set r=|p|, n=p/r,
Q=q0 e3, t=q0/r and w0=omega/q0 for this intermediate calculation. Put
r_+/-/r=sqrt(1+t^2/4+/-t n3). The R5 integrand is minus r times

    f0 (A n).(B n)+f1 (n.A n)(n.B n)+f2 (e3.A n)(e3.B n).

The fourth-order coefficients in t are the following exact polynomials,
with z=n3:

    f0[4]=[35 z^4-50 z^2+15+20 w0^2(1-z^2)+8 w0^4]/128,
    f1[4]=-[63 z^4-70 z^2+15+4 w0^2(5-7 z^2)+8 w0^4]/128,
    f2[4]=[5 z^2-3-2 w0^2]/32.                            (R6)

They follow by expanding the two square roots, or by multiplying the static
series by 1-omega^2/(r_-+r_+)^2+omega^4/(r_-+r_+)^4 to fourth order.
For uniform sphere average, odd monomials vanish and
<n1^(2a)n2^(2b)n3^(2c)>=(2a-1)!!(2b-1)!!(2c-1)!!/[2(a+b+c)+1]!!.
Exact contraction of R6 for arbitrary symbolic symmetric A,B gives

    <f[4]>= [tr(R A4 R B4)-tr(R A4)tr(R B4)/3]/80,          (R7)

where K=(w0,0,0,1), R=(1+w0^2)I4-K K^T,
A4=diag(0,-A), B4=diag(0,-B). This identity is polynomial in all twelve
polarization components and w0; selected channels are not its proof.

The two nodes and angular measure 4pi/(2pi)^3 produce the
nonanalytic response, with K=(omega,Q), kappa=|K| and P=I4-K K^T/kappa^2:

    chi_AB^log(K)=-kappa^4 log(1/kappa)/(80 pi^2 v)
                  [tr(P A4 P B4)-tr(P A4)tr(P B4)/3].      (R8)

For lapse plus strain replace A4 by diag(n,-A). This is equivalent in R8
to diag(0,-(A+n I)), since the difference is n I4 and the tensor annihilates
the four-dimensional trace. At zero frequency, writing P3=I3-Qhat Qhat^T,
the bracket for strains is tr(P3 A P3 B)-tr(P3 A)tr(P3 B)/3.
Unit-Frobenius TT polarizations have bracket one; the normalized transverse
spatial trace has bracket 1/3; longitudinal static strains have bracket zero.
A=B=I gives 2/3 and hence the lapse coefficient
-|Q|^4 log(1/|Q|)/(120 pi^2 v).

The coefficient in R8 has been obtained by a continuum annulus calculation.
The uniform remainder argument below transfers it to the
native R5 after subtracting its local constant and quadratic Taylor terms.
The source-coordinate hypotheses are retained in that argument. Independent
review of the author proposal remains pending.

### 4. Independent continuum normalization comparator

Osborn and Petkou, hep-th/9307010v2, equations 2.23, 5.2--5.6 and 8.7--8.12,
were read for this comparison. Their free four-component Dirac field in d=4
has C_T=2/pi^4. Their differential two-point formula is
C_T Delta_T [1/x^4]_R /320. Fourier transformation of the regulated 1/x^4
has nonlocal term -pi^2 log(K^2), so the stress covariance has coefficient
-1/(160 pi^2) K^4 log(K^2) P_TT. It is +1/(80 pi^2) K^4 log(1/|K|) P_TT.
Our ground-energy/negative-log-partition Hessian is minus the connected
covariance, accounting for the sign in R8; the two Weyl nodes are one Dirac
degree count. Metric perturbation h=2 diag(n,-A) enters the continuum action
with h T/2, accounting for the absence of an additional factor of four.

This comparator checks the coefficient and conventions; it does not prove
native continuum covariance, derive a physical regulator or fix Newton's
constant. Primary source: [Osborn and Petkou](https://arxiv.org/pdf/hep-th/9307010). The sections
on general three-point structures have not been read in full or imported.

### 5. A local-contact family

One may add to a specified native Hamiltonian an on-site term

    delta H_c[S]=c sum_x sum_i tr[(S(x+e_i)-S(x))^2] n_x.    (R10)

It vanishes for every constant S, and its value and first derivative vanish
at S=0. The half-filled flat state has <n_x>=1, so its exact quadratic energy
contribution is the displayed local difference functional. Arbitrary real c
therefore changes a two-derivative strain coefficient without changing the
flat matter or its first source vertex. These are specified source couplings,
with no change of the axioms or physical choice of c. Their scaling and spatial tensor extension
are proved in the local-contact section below.

## Uniform native stress logarithm

For the real symmetric frequency-even response R5 above, fix zeta<1;
constants need not be uniform at node
merger. A and B range over a bounded subset of real symmetric matrices.
Take the thermodynamic momentum integral first. Let K=(omega,Dq) and
kappa=|K|. The theorem is

    chi_AB(K)=c_AB+d_AB omega^2+e_AB,ij Q_i Q_j
              -kappa^4 log(1/kappa) T_AB(Khat)/(80 pi^2 v)
              +O(kappa^4),                              (U1)

where T_AB is the four-dimensional transverse-traceless contraction R8.
The local coefficients are its ordinary Taylor coefficients formed from the
zeroth and second derivatives, which exist. This theorem does not assert they have
Einstein values or symmetry. The remainder is uniform over all K directions,
including Q=0 and omega=0. Changing the fixed logarithm scale changes only
the O(kappa^4) term.

### 1. Smooth annulus family with derivative bounds

Choose disjoint ellipsoidal neighborhoods of the two simple zeros. Write
the centered internal momentum there as k=k_w+D^-1 r n, |n|=1. At shifted
momenta and for Q=r eta,

    d(k+/-q/2)/r=R_w(n+/-eta/2)+r b_+/-(r,n,eta),
    u_A(k,q)/r=R_w A n+r a_A(r,n,eta).                   (U2)

The functions b and a extend smoothly, in fact analytically in the radial
parameter, to r=0. This follows by Taylor's integral formula for the finite
trigonometric d and V; their values and first derivatives at the zeros follow
from the explicit vertex functions above. On |eta|<=1/4 the two
normalized energy norms are bounded below uniformly. Set omega=r xi.

The full R5 integrand, including its minus sign, is therefore r times a
smooth function G(r,n,eta,xi) on the compact set
0<=r<=delta, n in S2, |eta|+|xi|<=1/4. All derivatives needed through order
five in eta,xi, and one additional r derivative, are bounded. At r=0 this
is exactly the linear-cone family. Consequently its m-th external derivative
is bounded by C_m r^(1-m), and its fourth derivative differs from the linear
cone derivative by at most C r^-2. This argument controls all external
directions at once; it does not divide by |Q|.

For r>=8 kappa, Taylor expansion in the external K gives the terms of degree
zero, two and four, with remainder bounded by C kappa^5/r^4. Odd total
degrees vanish: the integrand is even under q->-q and separately under
omega->-omega. This also excludes omega*Q mixed quadratic terms. The native
fourth Taylor term differs from the cone fourth term by C kappa^4/r^2.
After multiplying by r^2 dr both errors integrate to O(kappa^4):

    kappa^5 int_(8kappa)^delta r^-2 dr=O(kappa^4),
    kappa^4 int_(8kappa)^delta 1 dr=O(kappa^4).             (U3)

The cone fourth term has radial dependence r^-3, so its integral supplies
log(delta/(8 kappa)). Its angular polynomial is exactly R6--R7. Restoring
both nodes and the Jacobian 1/v gives R8's coefficient.

### 2. The inner region and lower Taylor coefficients

For sufficiently small neighborhoods, the simple-zero property gives
E_-+E_+ >= c (r+|Q|), including near either shifted zero. The vertices are
bounded by C(r+|Q|). Projectors have norm one almost everywhere, hence

    |Delta J_AB/(Delta^2+omega^2)| <= C (r+|Q|).            (U4)

Undefined projectors exactly at a zero affect a null set. In r<8 kappa the
integral is O(kappa^4), uniformly also when Q=0. The zero-order integrand at
K=0 is O(r); the second external derivatives are O(r^-1) by U2. Their
integrals exist, and their omitted inner-ball contributions, multiplied by
their external Taylor monomials, are respectively O(kappa^4) and
kappa^2 O(kappa^2). They may therefore be extended to the full node balls.
This defines c,d,e in U1 by the native integrals, without fitting them.

### 3. Complement of the nodes and the limit order

On the fixed complement, both shifted energies stay uniformly away from
zero for small K, so the integrand is smooth with bounded derivatives.
Its constant and quadratic terms join the node terms; its fourth term and
remainder are O(kappa^4). Smooth radial partitions can be used instead of
hard balls. The difference lies in a fixed gapped annulus and is analytic
to the needed order, leaving the logarithmic coefficient unchanged.

Finite-volume Kato response tends to the stated integral on any sequence
of compatible gapped momentum grids whose mesh tends to zero. Away from
the finitely many shifted zeros this is ordinary Riemann convergence. Near
them, U4 bounds the possible contribution by the volume times a bounded
continuous envelope; the values at an exactly zero mode may instead be
excluded by a boundary twist. The theorem is about the integral followed
by K->0, and does not assert interchange with a finite-grid infrared limit.

### 4. Lapse mixing and actual limits of the conclusion

A first-order lapse adds sigma.[d_-+d_+]/2 to the vertex. Its node value and
first jet are the same as A=I in U2. Replacing A by A+n I therefore proves
the same logarithm for the seven lapse/strain sources, including mixed terms.
The nonlinear specified lapse law changes contact terms, which are local
for finite-range source couplings; these have no logarithm at quadratic
order. In the stated joint family, R9 adds directly to the constant and
spatial quadratic Taylor coefficients without changing R8. A time-dependent
full spacetime frame may also need a temporal spin
connection. This note addresses the real symmetric even-frequency kernel;
it does not identify the parity-odd response or silently assume those
additional geometric contacts vanish.

The four-dimensional projector is an exact tensor statement about this
leading nonanalytic term. It does not make the full lattice Hessian
transverse, remove its local elastic terms, establish full nonlinear
diffeomorphism invariance, or derive the Einstein two-derivative coefficient.

## Independent two-centre derivation of the stress spectral weight

This is a separate analytical route for the linear-cone coefficient in R8.
It uses the exact interband phase space, rather than an expansion at large
internal momentum. The native-lattice remainder uses the preceding uniform
remainder proof.

For positive real frequency Omega and spatial transfer Q, let
s0=Omega^2-|Q|^2. The symmetric retarded susceptibility is defined by
continuing R5 from omega to -i(Omega+i0). Its positive spectral density is
rho_AB=-Im chi_R,AB/pi. From the spectral denominator,

    rho_AB(Omega,Q)=sum_nodes int dp/[(2pi)^3 v]
                        J_AB(p,Q) delta(Omega-r_--r_+)/2. (S1)

It vanishes below the two-particle threshold Omega<|Q|. For Omega>|Q|,
take Q=q e3 and use prolate variables

    r_-+r_+=q u,   r_+-r_-=q eta,
    p3=q u eta/2,
    p_perp=q sqrt((u^2-1)(1-eta^2))/2,
    d^3p=q^3(u^2-eta^2) du d eta d phi/8.                (S2)

Here u>=1 and -1<=eta<=1. The delta function sets u=Omega/q and contributes
1/q. Writing J=N/(r_- r_+), the Jacobian, 1/2 in S1 and this delta factor
combine to N/4. On the ellipsoid,

    N=(s0/2)(A p).(B p)-2(p.A p)(p.B p)
                         +(q^2/2)(e3.A p)(e3.B p)
      =1/2 p^T A L B p-2(p^T A p)(p^T B p),
    L=s0 I3+Q Q^T.                                     (S3)

The ellipsoid is p=L^(1/2) n/2 with n uniformly distributed on the unit
sphere under d eta d phi. Therefore

    <p_i p_j>=L_ij/12,
    <p_i p_j p_k p_l>=(L_ij L_kl+L_ik L_jl+L_il L_jk)/240,
    <N>=[tr(A L B L)-tr(A L)tr(B L)/3]/40.               (S4)

All polarizations are retained in this contraction. With two Weyl nodes,
the exact continuum spectral density is

    rho_AB(Omega,Q)=1_(Omega>|Q|)/(160 pi^2 v)
                      [tr(A L B L)-tr(A L)tr(B L)/3].     (S5)

For the combined lapse/strain sources use A+n I and B+m I in this formula,
as follows directly from their linear-cone vertices.

The formula extends continuously to Q=0 by an ordinary spherical-shell
integral. For A=B it is nonnegative: L is positive definite above threshold,
and the bracket is the squared Frobenius norm of the traceless part of
L^(1/2) A L^(1/2). A pure isotropic lapse A=n I gives the constant-in-Omega
weight n^2 |Q|^4/(240 pi^2 v), and has no response at Q=0. This is the
spectral version of the lapse logarithm above.

### Dispersion calculation of the logarithm

Introduce a fixed positive upper pair-energy cutoff Lambda only for this
continuum comparator, with |Q|<Lambda. The Euclidean response is

    chi_AB(i omega,Q)=-int_(|Q|)^Lambda
                       2 Omega rho_AB(Omega,Q)/(Omega^2+omega^2) d Omega.

Set x=Omega^2. The S5 bracket is a degree-two polynomial P_AB(x). Polynomial
division gives

    P(x)/(x+omega^2)=a x+(b-a omega^2)+P(-omega^2)/(x+omega^2).

The first two terms and the upper-limit logarithm supply local terms through
the order of interest. The lower-limit logarithm is

    +P_AB(-omega^2) log(omega^2+|Q|^2)/(160 pi^2 v).        (S6)

At x=-omega^2, L=-(kappa^2 I3-Q Q^T). Thus P_AB(-omega^2) is precisely
the polynomial kappa^4 T_AB(Khat) obtained in the annulus derivation, proving
the same sign and 1/(80 pi^2 v) logarithm coefficient by a different route.
Changing the cutoff affects local terms; no native UV identification or
Newton coefficient follows from this auxiliary cutoff.

This exact spectral density is for the linear continuum cones and the
specified real symmetric stress vertices. The lattice proof transfers its
leading nonanalytic even response. It does not equate the full lattice
spectral density, parity-odd terms or high-frequency behavior with S5.

## Explicit native local-contact family and its scaling

This is a positive construction of additional specified source couplings
with the same flat carrier and first source vertex. The parameters remain
explicit choices of the model family.

Let s_A(x), A=1,...,6, be the components of S(x) in a fixed orthonormal basis
of real symmetric matrices. On the finite native carrier, n_x is the sum of
the two orbital occupations at a cell. Each occupation is (1-B_v)/2, where
B_v is the product of Z over the incident physical edge qubits. It is a
bounded-star projector, not a single physical-site projector. No new hopping
or quantum register is needed. Choose
any real finite coefficient array c_AB^ij with the symmetry needed to make
the following scalar real, and define

    Q_c[S](x)=sum_ABij c_AB^ij
                 [s_A(x+e_i)-s_A(x)] [s_B(x+e_j)-s_B(x)],
    delta H_c[S]=sum_x Q_c[S](x) n_x.                     (C1)

The scalar coefficients depend only on neighboring cell source values.
This is a bounded-support Hamiltonian coupling, not a derivation of the
framework's strict physical nearest-neighbor admissibility law.
The extra operator is bounded for a bounded field on a finite lattice. It
vanishes for every constant S, and its zeroth and first source derivatives
vanish at S=0. Thus it preserves all constant-frame spectra and node data,
the flat ground state, and every linear strain vertex. It changes neither
the first-jet common-metric construction nor the scalar spin-connection
term to first order.
It also preserves the common empty-fermion-vacuum energy zero, since every
n_x annihilates that vacuum. It is a matter operator, not a history-dependent
scalar subtraction.

At the flat half-filled state <n_x>=1 exactly: its one-particle occupied
projector is translation invariant and has orbital trace one per momentum.
Because C1 starts at second order, its exact energy-Hessian contribution
comes only from the first-order expectation of that second-order operator:

    E_c''[0]-E_0''[0]=sum_x (Q_c[S](x))''.                (C2)

No susceptibility of n_x enters until higher source order. On a finite
gapped grid this follows from ordinary spectral perturbation theory; the
quadratic coefficient has the thermodynamic value by the explicit density
identity. The Fourier polynomial is an explicit local contact. In particular,
for Q_c=c sum_i tr[(Delta_i S)^2],

    delta chi_AB(q)=2c sum_i 4 sin^2(q_i/2) tr(A B).       (C3)

The factor of two is the Hessian convention in R5. A real cosine source has
half this kernel as its second derivative per cell, checked against the
full finite Hamiltonian's eigenvalue sum.

### The same one-particle continuum limit can have different vacuum contacts

Restore physical coordinates x=a n and h_a=h_lat/a. For a fixed smooth
source field, |Delta_i S|<=a sup|partial_i S|. Thus C1 changes the
one-particle operator by a multiplication operator whose norm is O(a):

    ||delta h_a|| <= a C(c) sum_i ||partial_i S||_infty^2. (C4)

It therefore tends to zero even in full operator norm on the lattice
one-particle Hilbert space. For completeness, the baseline continuum
consistency needed here has a short direct proof. Let S have bounded smooth
derivatives through order three, with F uniformly invertible, and let psi be
a smooth compactly supported test spinor. Sample it as
psi_a(n)=exp(i k_w.n) psi(a n), using the norm squared a^3 sum_n |psi_a(n)|^2.
For any Laurent vertex V(k)=sum_r c_r exp(i k.r), its action on that
modulated sample is sum_r c_r exp(i k_w.r) psi(x+a r). The zero and first
moments are V(k_w)=0 and sum_r c_r exp(i k_w.r) r_j=-i partial_j V(k_w).
Taylor's theorem with the finite second moments gives O(a) norm error after
division by a, also for the anticommutator with a smooth coefficient.
The scalar term in the dimensionless lattice operator has coefficient a C;
after division by a its multiplier B0 has node value w and an O(a) error.
The resulting continuum operator is

    -i tau_a(F_ai partial_i+partial_i F_ai/2)+w C(F),
    tau_a=(R_w)_aa sigma_a.

Compact support bounds the sampled remainder norm by its O(a) pointwise
bound times a fixed volume factor. This proves consistency on these test
spinors, without a long-time or interacting convergence assertion. C4
preserves that consistency with an additional O(a) operator error.

Physical vacuum energy per physical volume, however, is the dimensionless
lattice energy divided by a^4 V. The contact density in C1 is O(a^2), so
its physical contribution is c/a^2 times the corresponding spatial gradient
quadratic form. If c is replaced by a^2 c_R, the one-particle error is
O(a^3), but the physical vacuum functional instead receives the finite
coefficient c_R multiplying that gradient form. All these versions have
the same constant-field spectra and first-order continuum matter operator.
The new coefficients are choices, not measured or derived values.

An arbitrary real quadratic form in first spatial derivatives can be
realized by C1. For example, select coefficients giving the three-dimensional
Fierz-Pauli spatial quadratic expression

    partial_k S_ij partial_k S_ij
    -2 partial_i S_ij partial_k S_kj
    +2 partial_i S_ij partial_j tr S
    -partial_k tr S partial_k tr S.                      (C5)

For comparison with the matter cones, these derivatives can be taken in
the fixed coordinates y=D^-1 x; the factors D_ii are then absorbed into
the coefficient array in C1.

Its continuum TT and transverse-trace signs differ. A corresponding local
finite-difference form follows by replacing the derivatives in this exact
expression. Multiplying it by any c_R realizes that static coefficient
while C4 still holds. This does not establish a stable dynamical metric,
temporal constraints, a nonlinear generally covariant completion, or the
physical value/sign of c_R. It exhibits an explicit remaining source choice.

The universal logarithm derived above is unchanged: C1 has no first
vertex and its second derivative is a finite Laurent polynomial in q.
The logarithm coefficient is identical throughout this explicit family.
The construction is a native matter realization of the local contact, and
leaves physical selection of its coefficients as a separate obligation.

## No-Go Discipline Gate

This is a positive conditional response theorem and an explicit family of
source constructions. It submits no axiom-wide impossibility, exhausted
route set or negative-packet PASS. The local coefficients in C1 are varied
within a specified family; no assertion quantifies over every possible
physical source law. The following scope review records N1--N8 without
turning successful derivations into fabricated failed routes.

**N1 — Routes.** Spectral perturbation, annulus expansion, ellipsoid phase
space and local contact construction are successful parts of this theorem.
They are not five failed routes to a no-go. No such route count or packet
PASS is claimed. The constructive statement is the family C1--C5 itself.

**N2 — Dependencies.** No independent wall count is asserted. Ordinary
quantum composition and the supplied free state support the response
calculation; the common vertices support both the node proof and its
infrared limit. The source-law choice and possible metric dynamics can
interact, so their independence is not presumed. Independent review is a
validation requirement, not an additional physical axiom.

**N3 — Hidden-condition scan.** The flat background, free filled band,
continuous Hamiltonian time, boundary twist, cycle-code representation,
source function, frame smoothness, invertibility, and order of limits are
explicit hypotheses. Torsion-free spin geometry and the continuum CFT
formula are stated mathematical conventions and a normalization comparator.
No selected coefficient or observed datum is hidden in the frame vertices.

**N4 — Residual matching.** The linked native edge theorem supplies the
conditional code and occupation dictionary, not a gravity obstruction.
The linked framework memo supplies the premise boundary, not a no-go.
Osborn and Petkou supplies the continuum stress normalization, not a native
UV or metric-selection result. None is used as a witness that an axiom
update is forced. The uniform native coefficient is proved here.

**N5 — Resolution.** At individual-Record resolution no occurrence law is
derived. At cell resolution the occupation dictionary and density contact
are checked. At mode resolution the exact generic strain tensor, node jets
and continuum spectral shell are checked. At finite-block resolution the
position matrices and energy derivatives are checked. The infinite-volume
remainder is an analytical proof with explicit limit order; finite grids
are challenges only. The primary emits each of these scope statements.

**N6 — Partial closure.** A physical principle selecting a source family,
a geometric action or measured renormalization conditions could determine
the remaining coefficients. This note does not exclude those routes or
classify them as requiring a new axiom. The framework memo's separation of
ontology and selected laws is respected; no primitive-absence claim is made.

**N7 — Steelman.** A dynamics-derived source prescription might fix the
entire local action and its nonlinear contacts, with constraints selecting
the allowed sector. The constructed C1 family establishes what varies
before such a prescription is imposed. It does not establish what a
successful native prescription would permit. The concrete next obligation
is to construct and test that prescription against the same carrier and
its interacting source identities.

**N8 — Prior scope.** A focused current-main search of the full-W Hessian,
stress-seagull and minimal-axiom notes found the existing explicit local
improvement discussion. The June 9 full-W source itself leaves different
improvements and continuum scaling open. Its three-dimensional Euclidean
operator is a different model; its finite signs do not prove an obstruction
for the present Hamiltonian. No prior negative conclusion is inherited.
The search is bounded, not an exhaustive axiom-wall survey.

## Reproduction and author review record

The single primary is
`scripts/native_weyl_stress_logarithm_contact_response_2026_09_13.py`, with
receipt `outputs/native_weyl_stress_logarithm_contact_response_2026_09_13.json`
and the matching canonical cache under `logs/runner-cache/`. It declares a
60-second timeout and binds this note as its only package-local input.
It reads no external scientific data; its own source is read for integrity.
All finite and symbolic code is in that primary; no helper-runner registry
or unmerged sibling premise is required.

The anticipated tensor and earlier scalar coefficient were known during
development. No prefactor was fitted: the generic angular contraction and
the subsequent exact ellipsoid calculation derive it from the specified
vertices. These are distinct mathematical routes by the same author,
not a claim of independent review. The position-space construction and
momentum symbol calculation share the stated model but use separate
implementations. The continuum primary source was read in equations
2.22--2.24, 5.1--5.6 and 8.1--8.12; its general three-point analysis is not
an imported proof input.

Author review corrected the initial affine seven-source calculation by
including the mixed contact of the stated joint family. It also corrected
the physical occupation support to a star projector, retained the finite
even-parity condition, and limited the spacetime tensor claim to its seven
sources and even-frequency part. The first-order continuum consistency
argument is reconstructed here, without importing a sibling PR's bound.
The geometric vector and scalar parts are separately checked using Koszul
coefficients and Pauli products. No source correction or status claim about
the earlier gravity notes is included in this new theorem.

Independent review and formal audit remain pending. The later exact
integrated landing candidate still requires the full pipeline, strict lint
and changed-evidence checks. Author source checks and a fresh canonical cache
are not an integrated landing PASS or a retained-status decision.
