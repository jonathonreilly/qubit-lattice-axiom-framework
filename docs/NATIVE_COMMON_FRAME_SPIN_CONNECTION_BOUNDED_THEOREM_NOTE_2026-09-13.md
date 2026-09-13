---
claim_id: native_common_frame_spin_connection_bounded_theorem_note_2026-09-13
claim_type: bounded_theorem
claim_scope: "For the specified free native two-orbital Wilson model, construct nine finite-range frame vertices with the same principal metric at both Weyl nodes; prove an explicit uniform neighborhood preserving exactly those two nodes, protected paths of length at most four, and a slowly varying operator estimate for a local polynomial spin-connection coupling. Standard metric-dependent spin identities are rederived to fix the continuum target. The frame, dynamics, scale and state interpretation are supplied; no interacting frame or dynamical gravity theorem is claimed."
upstream_dependencies:
  - native_edge_record_matter_instrument_and_energy_ledger_bounded_theorem_note_2026-09-05
runner: scripts/native_common_frame_spin_connection_2026_09_13.py
---

# A common native Weyl metric, its spin connection and a controlled lattice approximation

**Date:** 2026-09-13
**Type:** bounded_theorem
**Status:** proposed_retained

## Target, premises and proof obligations

Construct a finite-range native frame coupling whose two Weyl nodes have the
same spatial metric, prove its small-frame zero-set and slowly varying
operator bounds, and identify the full geometric connection being approximated.

~~~yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "Analytical construction and bounds for a specified free native Hamiltonian, with exact algebra and finite operator challenges."
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "A common full spatial metric coupling for native matter, beyond a scalar lapse."
source_of_blocker_text: user_goal
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Test the metric's own dynamics and interacting stress identities on a common physical carrier."
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
~~~

| Premise or obligation | Role | Disposition |
|---|---|---|
| Lattice, Qubit, Admissibility and Record | Framework ontology | Placement and event domain only |
| Ordinary tensor quantum composition, CAR, native cycle code and Born readout | Conditional realization in the linked current-main source | Supplied representation and preparation |
| Free Wilson coefficients, scale a, frame F and continuum envelope | Model specification | Supplied; no observation or fit selects them |
| Nine common-frame vertices and uniform two-node neighborhood | Native-model construction | Proved below |
| Protected paths and surviving Record intertwining | Even-CAR dictionary plus actual cubic placement | Reconstructed below |
| Torsion-free metric connection and a local Spin lift | Standard geometric interpretation | Explicit mathematical input; signs rederived |
| Full half-density operator and polar frame action | Continuum target | Derived below with its changing-metric convention |
| Neumann polynomial, local derivative stencil and slow-band norm estimate | Native approximation | Proved below |
| Frame register, canonical gravitational momentum, metric action and interacting continuum control | Further physical interpretation | Open; not conclusions of the construction |

The [framework memo](MINIMAL_AXIOMS_2026-06-29.md) separates the minimal
axioms from selected Hamiltonian and occurrence laws. No axiom or primitive
is added here. The strongest missing physical lemma is a native dynamical
metric coupled to this matter with consistent interacting constraints.
That is stronger than the supplied-frame theorem, so the result is
upstream support rather than near closure of the TOE.

All frame-index and coordinate-index sums below run from1 to3. The two
orbitals are an explicit cell encoding. No Standard Model identification,
physical isotropy value, Newton constant or Planck scale is extracted.

## Native dictionary and physical placement

Use Theorems1–2 of the [native edge/CAR source](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md)
at main b8c9d9d819911c5f3fec98b23d53355e7ff8c8bf, with its ordinary tensor
composition and cycle-code hypotheses. A physical edge qubit sits at2v+e_a
for a virtual edge v to v+e_a. With fixed incident-edge orders,

    B_v=product_(e incident v) Z_e,
    A_vw=epsilon_vw X_vw product_(u<_v w) Z_vu
                              product_(u<_w v) Z_wu.

On the positive cycle code, B_v=1-2n_v and A_vw=-i gamma_(2v)gamma_(2w).
For a simple path p of length l, ordered cancellation of its internal
Majoranas gives

    A_p=i^(l-1)product_ordered A_e=-i gamma_(2v0)gamma_(2vlast),
    T_p=(i/2)A_p(B_v-B_w)=c_v^*c_w+c_w^*c_v,
    J_p=-A_p(1-B_v B_w)/2=i(c_v^*c_w-c_w^*c_v).          (N1)

These encode both real and imaginary hopping coefficients. The finite
checker also derives the occupation signs directly on five fermion modes,
then compares(N1) for path lengths1 through4.

Use virtual orbital placement v(x,r)=(2x1+r,x2,x3). All x,z edges and y edges
whose lower-y tail has even x+y are protected. The remaining y edges form
a matching of candidate Records. A candidate edge has an x-plaquette detour
containing only protected edges. For its nonbridge Z readout, the incoming
cycle that anticommutes with Z implies P_code Z P_code=0. Thus sqrt(2)Q_z is
the branch isometry on the code, and every surviving even word commutes
with Q_z and intertwines it. This is conditional compatibility with supplied
Born readout, not an autonomous frame or formation law.

Fix zeta in[1/2,1). The base hopping matrices are

    W1=(-sigma3+i sigma1)/2, W2=(-sigma3+i sigma2)/2,
    W3=-sigma3/2,
    h0=(2+zeta)sigma3 onsite plus W_a and its adjoint on each bond.

With c_x=sum_k exp(-ik.x)c_k, they give
 d(k)=(sin k1,sin k2,2+zeta-cos k1-cos k2-cos k3).
The new frame paths are proved below. All boundary statements refer to
open boxes: omit exiting model hops and use the inward x detour at a box
boundary. Periodic Fourier regulators do not represent short physical
wrap paths in an open cubic box.

## An explicit naive-frame witness

Write v=sqrt(1-zeta^2), F0=diag(1,1,v),

    u=(sin k1,sin k2,(zeta-cos k3)/v),
    r=2-cos k1-cos k2,
    d=F0 u+e3 r.

The two nodes are k_w=(0,0,w acos zeta), w=+/-1. The apparently natural
constant-frame family d_naive(F,k)=F u+e3 r has tangent

    D_w^naive=F R_w,  R_w=diag(1,1,w).

Its two quadratic cone metrics are R_w F^T F R_w. For a symmetric frame

    F=[[1,0,t],[0,1,0],[t,0,v]],

one gets offdiagonal inverse-metric entry G13=+/-t(1+v), with opposite signs at
the two cones when t is nonzero. This is a finite explicit two-cone witness
in that supplied family. It is not a general obstruction to a common metric.

## A finite-range two-cone coupling

Let F=F0+f be any real constant 3-by-3 matrix. Define the following nine real
trigonometric vertex functions, indexed by Pauli row a and physical column j:

    V_aj(k)=sin k_j,                       a=1,2; j=1,2,
    V_a3(k)=(zeta-cos k3)sin k3/v^2,        a=1,2,
    V_3j(k)=sin k3 sin k_j/v,              j=1,2,
    V_33(k)=(zeta-cos k3)/v.

Set

    d_F,a(k)=d_a(k)+sum_j f_aj V_aj(k).                   (C1)

Every added vertex vanishes at both native nodes. Its first derivative there
is exactly

    partial_l V_aj(k_w)=(R_w)_aa delta_jl.

Since the original tangent is R_w F0, the deformed tangent is

    D_w=R_w F,      D_w^T D_w=F^T F.                    (C2)

Both tangents have the same quadratic form F^T F. For invertible F this
is a positive metric, and the two node chiralities remain opposite. No coefficient was extracted
from a fit. The trigonometric functions are an explicitly supplied constructive
choice; many higher-order additions could share their node data.

## A global two-node preservation estimate

Let D=|d(k)| and b=zeta-cos k3. Then r>=0 and b>=-1/2. If r>=1,
 d3=r+b>=r/2, so r<=2D. If r<=1, put a_j=1-cos k_j. Since 0<=a_j<=1,

    sin^2 k1+sin^2 k2=sum_j a_j(2-a_j)>=r.

Thus D>=sqrt(r)>=r in this region. Globally r<=2D and

    |b|<=|d3|+r<=3D.                                    (C3)

Also sin^2k1+sin^2k2<=D^2 and v<=1. For either of the first two rows,

    sum_j |V_aj|^2 <= D^2+9D^2/v^4 <=10D^2/v^4.

For the third row the bound is 10D^2/v^2<=10D^2/v^4.
Cauchy-Schwarz, applied row by row, therefore gives

    |d_F(k)-d(k)| <= (sqrt(10)/v^2)||f||_F D.             (C4)

Consequently the explicit condition

    ||f||_F < v^2/sqrt(10)                              (C5)

implies |d_F(k)|>0 wherever |d(k)|>0. Since every added vertex vanishes at
k_w, the zero set remains exactly the original two nodes. Also
sigma_min(F)>=v-||f||_F>0 under(C5), so both nodes are simple. This is a
uniform Brillouin-zone proof for fixed zeta, not a search on sampled momenta.
It exposes its shrinking allowable frame neighborhood as the nodes merge.

The naive and repaired families agree at F=F0. At a generic small shear,
(C2) has a different physical consequence from the explicit naive witness.
Neither family is claimed as an axiom-selected metric law.

## Physical native support and actual frame source

The new coefficients are finite Laurent polynomials. In particular,

    V_a3=zeta sin k3/v^2-sin(2k3)/(2v^2), a=1,2,
    V_3j=[cos(k3-kj)-cos(k3+kj)]/(2v), j=1,2.

For the orbital map (2x1+r,x2,x3), the sigma1,2 sin(2k3) term needs an
offdiagonal-orbital path with displacement plus/minus e_x plus/minus2e_z:
length3, using only protected x,z edges. A diagonal sigma3 xz term needs
plus/minus2e_x plus/minus e_z: length3. A diagonal yz term has length2 if
its y edge is protected; otherwise its x-plaquette detour followed by z has
length4. The remaining terms use the already specified paths of length at
most3. Thus every new hopping has a protected path of length at most4.
An open-box boundary must retain the same one-step x detour choice used in
the native construction; model terms exiting the box are omitted.

For a site-dependent real f_aj(x), use the Hermitian operator

    h_F^lat=h0+(1/2)sum_aj {f_aj(x), sigma_a V_aj} .          (C6)

The finite-stencil native words are unchanged by these coefficients and
remain intertwined by candidate Record isometries. Differentiation gives the
actual frame source at site x:

    partial h_F^lat/partial f_aj(x)={P_x,sigma_a V_aj}/2.     (C7)

Equation(C7) is the source of the principal coupling. The connection added
below has its own frame variation: for the scale-a full operator the source
is {P_x,sigma_a V_aj}/(2a)+{partial C_m^a/partial f_aj(x),B}/2.
The derivative of C here means differentiation of the explicit local
polynomial controls at every affected site, not just at x. Thus the full
variational source is fixed once the coupling is specified. It is not a
selected physical stress law.

## Continuum spin identities used by the construction

In unit-speed coordinates on smooth compactly supported spinors, put
h=-i sigma.grad, H[N]={N,h}/2 and a=N grad M-M grad N. Pauli multiplication
and the product rule give

    i[H[N],H[M]]=D[a],
    D[a]=-i(a.grad+div a/2)+sigma.curl a/4.               (D2)

The second-derivative coefficient cancels through NM-MN. The Pauli
anticommutator leaves -a.grad in the commutator, its scalar term is
-div(a)/2, and the remaining matrix term is
-[sigma.grad N,sigma.grad M]/4. This proves(D2) for arbitrary spinors.
The spin term is sigma.Omega/2 for a rigid rotation a=Omega cross x.

For S(a)=(J_a+J_a^T)/2, J_a,ij=partial_j a_i, direct expansion also gives

    K[S]=-i sigma_j(S_ij partial_i+partial_i S_ij/2),
    i[D[a],H[N]]=H[a.grad N]-{N,K[S(a)]}/2,             (D4)
    i[D[a],D[b]]-D[[a,b]]
       =(1/4)sigma_k epsilon_kij [S(a),S(b)]_ji.         (D6)

For(D6), expand the curl of [a,b] and use the Pauli commutator: the
antisymmetric Jacobian contributions cancel, leaving the commutator of the
two symmetric strains. The exact generic-function checker retains every
first and second derivative of a,b and the spinor. A concrete example is
a=(x1,0,0), b=(x2,x1,0), which gives residual -sigma3/2. The next section
supplies the metric variation that cancels this particular fixed-frame
residual. No general obstruction to spinor transport is inferred.

## Polar frame action on the metric and spinor together

Work in an oriented coordinate patch with a chosen spin lift near the identity.
Let E(x) be a symmetric positive definite matrix, with coordinate rows and
internal columns. Its inverse metric is G=E^2. For a smooth orientation-
preserving diffeomorphism x=phi(y), J=Dphi(y), define

    E'(x)=[J E(y)^2 J^T]^(1/2),
    O(phi,E;x)=E'(x)^(-1) J E(y).                        (P1)

Then O O^T=I and det O=1. If S(O) is the continuously chosen spin lift,
S(O) sigma(v) S(O)^*=sigma(O v), define the spinor half-density action

    psi'(x)=(det J)^(-1/2) S(O(phi,E;x)) psi(y).          (P2)

The norm integral of psi^*psi against coordinate volume is unchanged.
For two successive coordinate maps, the intervening positive frame cancels:

    O(phi,eta_*E;x) O(eta,E;y)=O(phi o eta,E;x).          (P3)

The determinant factors also compose. Therefore (P1)-(P2) give an exact
local action on the pair (E,psi). A global statement uses a specified spin
structure and lifted diffeomorphisms; the double-cover sign is not discarded.

For phi_t(x)=x+t a(x)+O(t^2), set J_a,ij=partial_j a_i. The infinitesimal
rotation Omega_a(E) is the unique antisymmetric solution of

    E Omega_a+Omega_a E=J_a E-E J_a^T.                  (P4)

Existence and uniqueness follow by diagonalizing positive E: the ij entry is
divided by the strictly positive sum of the ith and jth eigenvalues. The
variations are

    delta_a E=-a.grad E+J_a E-E Omega_a,
    delta_a psi=-(a.grad+div a/2)psi+r(Omega_a)psi,
    r(Omega)=(1/4)sum_ab Omega_ab sigma_a sigma_b.        (P5)

At E=I, Omega_a=(J_a-J_a^T)/2 and delta_a E=S(a), whereas
r(Omega_a)=-i sigma.curl(a)/4. Thus delta_a psi=-i D[a]psi
with D from(D2).

Differentiating (P4) at E=I along delta_a E=S(a) gives

    delta_a Omega_b=(1/2)[S(b),S(a)].                   (P6)

Their antisymmetrized variation is -[S(a),S(b)]. It supplies exactly the
spin term omitted in a commutator at frozen metric. In the convention
(delta_a delta_b-delta_b delta_a)psi, functional differentiation also
reverses the order of the fixed differential operators: delta_a acts on
psi inside the expression delta_b psi. If R is the residual in (D6), that
fixed contribution is -i(D[[a,b]]+R), while r(-[S(a),S(b)])=+iR.
The sum is delta_[a,b] psi. Equation (P3) is the finite form of this
cancellation and avoids treating a changing metric as a fixed background.

## Full spatial Dirac operator on half-densities

Now allow an arbitrary smooth real invertible frame F with positive determinant,
using internal rows and coordinate columns: e_a=F_ai partial_i. Set
G=F^T F, g=G^(-1), and theta^a_i=(F^(-1))_ia. The positive gauge above has
F=E^T=E. All the following formulas are local; use smooth compactly supported
spinors, or a compact manifold and its chosen spin structure, when integrating.

Let Gamma^j_ik be the Levi-Civita connection of g and define

    omega_i b c=g_mn F_bm (partial_i F_cn+Gamma^n_ij F_cj),
    A_i=(1/4)sum_bc omega_i b c sigma_b sigma_c.         (P7)

Metric compatibility makes omega antisymmetric in b,c. The Clifford identity

    partial_i gamma^j+Gamma^j_ik gamma^k+[A_i,gamma^j]=0,
    gamma^j=sum_a sigma_a F_aj,                         (P8)

follows directly from (P7) and the Pauli commutator. Conjugating the geometric
spinor operator by (det g)^(1/4) gives the half-density operator

    h_F=-i gamma^i(partial_i+A_i-Gamma^k_ki/2)
       =-i sum_a sigma_a(F_ai partial_i+partial_i F_ai/2)
         +C(F) I,
    C(F)=(1/4)epsilon_abc F_ai omega_i b c
        =-(1/4)epsilon_abc F_ai (partial_i F_bj)(F^(-1))_jc.
                                                               (P9)

For the equality, expand sigma_a sigma_b sigma_c as
 delta_ab sigma_c+delta_bc sigma_a-delta_ac sigma_b+i epsilon_abc I.
The vector term reduces using
 sum_b F_bi omega_i b c=partial_i F_ci+Gamma^k_ki F_ci.
For the scalar term, write [e_a,e_b]=c_ab^c e_c. The Koszul formula gives
 epsilon_abc omega_a b c=-(1/2)epsilon_abc c_ab^c;
expanding the bracket gives the second expression for C. This also proves
formal symmetry: the displayed first-order part is symmetrically ordered,
and C is real.

Sign check: e_1=(cos theta(z),sin theta(z),0),
e_2=(-sin theta(z),cos theta(z),0), e_3=(0,0,1), give
C=-theta'(z)/2. This equals the scalar term in U h_I U^* for
U=exp(+i theta(z) sigma_3/2). It is not zero merely because the metric is flat.
For the positive symmetric frame

    F=[[A(z),B(z),0],[B(z),D(z),0],[0,0,c]],
    A>0, AD-B^2>0, c>0,
    C=-c[(A-D)B'+B(D'-A')]/[4(AD-B^2)].                 (P10)

Thus even in the positive gauge a generic nonuniform frame needs this term.
For F=I+t S(x), S symmetric, its first variation vanishes: the contraction
of epsilon_abc with partial_a S_bc is zero. This gives delta h=K[S] in unit-speed coordinates; the statement is scoped
to that base frame and coordinate gauge.

Levi-Civita uniqueness under pullback, (P8), and the chain rule imply

    h_E' U_phi,E=U_phi,E h_E                            (P11)

for (P1)-(P2); multiplication by a lapse transforms by scalar pullback, so
H_E'[N o phi^(-1)] U=U H_E[N]. In (P11) the operator and its frame both
change. This is spatial covariance of a supplied geometric Dirac operator,
not closure of normal deformations of dynamical geometry.

## The two native cones need opposite scalar terms

For the common-frame vertices (C1), cone w has coefficient R_w F. Use the
same metric connection but Clifford matrices tau_a=(R_w)_aa sigma_a. Their
triple product has orientation w. Consequently its half-density operator is

    h_F,w=-i sum_a tau_a(F_ai partial_i+partial_i F_ai/2)
           +w C(F) I.                                 (P12)

The scalar term can be supplied by a native one-step z hopping. If the
physical lattice scale is a and B(k)=sin k3/v, set

    h_a,F=h_a,principal+(1/2){C(F)(x),B(k)} I.           (P13)

Because B(k_w)=w, its leading slow-mode scalar is w C(F). In the unscaled
lattice Hamiltonian the extra coefficient is a C. It uses diagonal-orbital
protected z edges, and thus is compatible with the same native code
intertwining. This is a specified derivative-dependent frame coupling.
The derivative defining C may be supplied analytically for sampled smooth
fields, or approximated by a local frame stencil with its error quantified.
No exact native diffeomorphism symmetry is claimed.

For constant F, C=0 and the global two-node result holds under(C5).
This note makes no global two-node zero-set assertion for nonuniform F;
(P12) is a local continuum statement. Interacting RG bounds,
finite-spacing spin covariance and a dynamical origin of F remain open.

## Normal/normal identity with the complete curved operator

Let nabla_i^hd=partial_i+A_i-Gamma^k_ki/2 act on spinor half-densities.
Set H_F[N]={N,h_F}/2. For real smooth N,M define
a^i=G^ij(N partial_j M-M partial_j N) and
 a_j=g_ji a^i. Write antisymmetrization with weight one half. Then

    i[H_F[N],H_F[M]]=D_F[a],
    D_F[a]=-i[a^i nabla_i^hd+(nabla_i a^i)/2
                  +(1/4)gamma^i gamma^j nabla_[i a_j]].       (P14)

This holds on smooth compactly supported spinors, with the same connection
as (P7). At a point choose normal metric coordinates and a parallel frame,
so Gamma, A and first gamma derivatives vanish there. All second-order
operator terms, including derivatives of the zeroth-order connection,
carry the symmetric factor NM and cancel in the commutator. The remaining
terms are exactly the already derived flat calculation (D2), with
nabla_[i a_j]=partial_i N partial_j M-partial_i M partial_j N.
Both sides are covariant differential operators, which proves the identity
in any frame. Equivalently, in the original coordinate trivialization the
zeroth-order term of the RHS is

    -i (partial_i a^i)I/2-i a^i A_i
        -(i/4)gamma^i gamma^j
                    (partial_i N partial_j M-partial_i M partial_j N).

The rational-jet checker independently composes the first-order operators
at nonflat frame values and gradients, including the lapse Hessians and
both orientations. Derivatives of the connection cancel before any choice
of second frame jets, so those jets are not assumed to vanish.

This still does not close the full hypersurface-deformation algebra of
a gravitational theory. D_F is the metric-dependent spin transport
operator; the metric variation must accompany spatial transformations.
This note has not supplied canonical metric variables or a gravitational
Hamiltonian for normal transformations. The second-quantized matter bracket also
requires a chosen representation and control of possible continuum central
terms. None follows from one-particle identity (P14).

## Laurent bounds for the nine vertices

For V(k)=sum_r c_r exp(i k.r) vanishing at k_w, the elementary inequality
|exp(i u)-1-i u|<=u^2/2 gives the global momentum estimate

    |V(k_w+a p)/a-grad V(k_w).p| <= a L_V |p|^2,
    L_V=(1/2)sum_r |c_r| |r|^2.                         (B1)

For the vertices (C1), convenient exact Laurent constants are

    L_aj=1/2,                       a=1,2; j=1,2,
    L_a3=(zeta+2)/(2v^2),            a=1,2,
    L_3j=1/v,                       j=1,2,
    L_33=1/(2v).                                         (B2)

The connection hopping B(k)=sin k3/v obeys

    |B(k_w+a p)-w| <= a |p|/v.                          (B3)

These estimates hold at both nodes. They do not rely on fitting a polynomial
to sampled lattice energies.

## A local polynomial approximation of the spin connection

Let F(x)=F0+f(x), F0=diag(1,1,v). Assume f is a real finite Fourier sum with
frequency support |q|<=B_f. Assume, for all x,

    ||F0^(-1) f(x)||_op <= rho < 1,
    ||F(x)||_op <= M0,
    [sum_i ||partial_i F(x)||_op^2]^(1/2) <= M1.

The stronger small-frame condition (C5), imposed pointwise if desired,
implies invertibility but is not needed separately for the estimates below.
For integer m>=0 define

    Q_m(x)=sum_(n=0)^m [-F0^(-1) f(x)]^n F0^(-1).

The Neumann identity gives

    ||Q_m||_op <= 1/[v(1-rho)],
    ||F^(-1)-Q_m||_op <= rho^(m+1)/[v(1-rho)].          (B4)

Replace the inverse in (P9) by Q_m to obtain the real scalar C_m. Its Fourier
support lies in |q|<=(m+2)B_f. There are six nonzero epsilon entries. For
each, Cauchy-Schwarz in i bounds the directional derivative row by M0 M1,
and the Q column has norm at most ||Q||. Hence

    ||C_m-C||_infinity <= eta_m,
    eta_m=3 M0 M1 rho^(m+1)/[2v(1-rho)].                (B5)

A literal native control stencil may also replace partial_i F by

    D_i^a F(x)=[F(x+a e_i)-F(x-a e_i)]/(2a).

If M3=[sum_i sup_x ||partial_i^3 F(x)||_op^2]^(1/2), central Taylor's
integral remainder gives ||D_i^a F-partial_i F||_infinity <=
a^2 sup||partial_i^3 F||/6. The resulting C_m^a is still a real finite
Fourier sum with the same bandwidth and obeys

    ||C_m^a-C||_infinity <= eta,
    eta=eta_m+a^2 M0 M3/[4v(1-rho)],
    ||C_m^a||_infinity <= c_m,
    c_m=3 M0(M1+a^2 M3/6)/[2v(1-rho)].                 (B6)

The stencil uses the frame at x and nearest coordinate neighbors, and no
matrix inverse or nonlocal solve is needed at a site. This is a bounded local
control rule for the supplied frame; a physical frame register and its
Hamiltonian still have to be constructed.

## Operator estimate and exact sampling domain

Use the native Fourier convention and envelope coordinate x=-a n.
For a continuum L2 spinor with Fourier support |p|<=K,
modulation by exp(-i k_w.n) followed by a^(3/2) sampling at -a n is isometric
whenever its support remains within the associated Brillouin window.
Finite Fourier multiplication by a coefficient of bandwidth B increases
support by at most B. Define

    P=K+(m+2)B_f,       a P < acos(zeta).                (B7)

This keeps all intermediate and output bands for the following operator
inside their node window; it also separates the two nodes. Define the
native envelope operator using the exact trigonometric symbols

    h_a,m=h0(k_w+a p)/a
          +(1/2)sum_aj {f_aj(x),sigma_a V_aj(k_w+a p)/a}
          +(1/2){C_m^a(x),B(k_w+a p)} I.                (B8)

For a Laurent term c_r exp(i k.r), the hopping matrix acts from n-r to n
with coefficient c_r; this fixes the Fourier sign. On this band,
modulation/sampling intertwines(B8) exactly with the stated
finite-range lattice hopping operator. There is no projection of a product
onto a smaller computational band in this assertion.

Let h_F,w be the full continuum operator (P12), including exact C(F), and
q_aj=||f_aj||_infinity. The Wilson estimate below and(B1)-(B6) imply

    ||(h_a,m-h_F,w) psi|| <= epsilon_a,m(K) ||psi||,
    epsilon_a,m(K)=delta_a(P)+a P^2 sum_aj q_aj L_aj
                    +c_m a P/v+eta,
    delta_a(P)=a P^2/2+a^2 P^3/6.                        (B9)

Proof: in each anticommutator, the Fourier error acts either before f,
on the K band, or after f, on the K+B_f band. Each half is bounded by
q_aj a L_aj P^2/2. The scalar hopping similarly has two halves bounded
by c_m a P/(2v). The remaining scalar multiplication error is at most eta.
For the base symbol, |sin u-u|<=|u|^3/6 and 1-cos u<=u^2/2 imply
 delta_a(P)=aP^2/2+a^2P^3/6: sum_i |p_i|^3<=|p|^3, and zeta,v<=1.
Summing proves(B9).
Although exact C need not have finite Fourier support, its difference from
C_m^a is bounded as a multiplication operator on the full continuum L2
space. Thus (B9) includes that tail; it does not silently identify the exact
continuum output with a band-limited sampled function.

For a real finite Fourier lapse N with bandwidth B_N and sup norm n0,
H[N]={N,h}/2 satisfies the corresponding estimate n0 epsilon_a,m(K+B_N),
with the separation condition enlarged to a[K+B_N+(m+2)B_f]<acos(zeta).
This is an operator bound on the stated input band, not a claim that time
evolution preserves that band indefinitely.

Taking m proportional to log(1/a) for fixed rho<1 makes eta_m=O(a), while
P=O(log(1/a)). Equation (B9) is then O(a log^2(1/a)) at fixed K,B_f and
bounded smooth frame, and the no-alias condition holds for sufficiently
small a. This supplies a convergent sequence of finite-range Hamiltonians:
raising m changes the local polynomial of external frame values, not the
maximum quantum hopping path length. It does not supply a uniform
interacting bound or control long times without an additional propagation
estimate.

## Boundaries, source context and author validation

The constant-frame zero-set proof covers zeta in[1/2,1) and the stated
Frobenius neighborhood. In the base model the sine components vanish only
at k1,k2 in{0,pi}; any pi gives r>=2 and nonzero d3. The remaining solutions
are the two stated nodes. The bound shrinks as v tends to zero; the merged
node endpoint is excluded. Nonuniform frames have no global Bloch zero-set
claim. Smooth frame fields, finite Fourier data and the stated frequency
windows are explicit hypotheses of the approximation. The continuum
operator domain is smooth compact support, or a specified compact spin
manifold. Global spin structures and lifts are retained as data.

The native edge/CAR source is the sole load-bearing repository theorem.
The spin geometry is established machinery, reconstructed here rather than
claimed as a novel theorem of the axioms. Primary comparisons are
[Godina and Matteucci](https://arxiv.org/abs/math/0504366), for the Kosmann
lift and its fixed-metric nonhomomorphism;
[Chervova, Downes and Vassiliev](https://arxiv.org/abs/1209.3510), for the
half-density operator and scalar subprincipal term; and
[Dąbrowski and Dossena](https://arxiv.org/abs/1209.2021), for covariance
when the metric and spinor space both change. The local normalizations are
fixed by the explicit Pauli calculation above.

The checked source portions include Godina--Matteucci theorem4.11,
remark4.14, definitions5.1-5.7 and example5.8; example4.15 and later
reductive-lift discussion through propositions5.19-5.20 were partly read;
Chervova--Downes--Vassiliev v2 section1, sections6-7 and Appendix A;
Dąbrowski--Dossena sectionsV-VII and propositions2-3 with proofs. The latter
paper's introductory bundle definitions were only partly read. No spectral
characterization theorem, interacting curved-space RG theorem or quantum
metric measure is imported.

The self-contained primary runner checks arbitrary-function flat spin
identities, exact symbolic two-node frame jets, separately constructed
Laurent coefficients, all applicable protected paths on open boxes of
shape(3,3,3),(1,3,3),(2,2,3), rational nonflat connection jets, and both
orientations of the curved normal commutator. It also compares the exact
polar map under successive noncommuting matrices. Direct occupation signs
check the even-CAR path dictionary through length4.

The variable-frame challenge is a periodic envelope Fourier comparison,
not a claim of physical wrap bonds at each sampled spacing. It uses
zeta=1/2, initial p_z in{-1,0,1},
p_x=0.7,p_y=-0.4, and both native nodes. One frame has xy shear; the other
also has xz and yz shear. The exact connection is bounded by a degree20
Neumann reference tail, and a128-point Fourier grid integrates the
polynomial norm matrix without a mode projection. In these examples,
errors decrease from about0.071 at spacing0.12 to about5.75e-7 at spacing1e-6.
Omitting the connection leaves a nonzero error in these same examples.
The analytic estimate, not these samples, is the general theorem.

## No-Go Discipline Gate

N1: No physical route or axiom class is declared exhausted. The naive-frame
shear and the fixed-frame spin residual are explicit existence witnesses;
the constructed vertices and polar metric action repair them in this same
note. Five failed route families have not been established, and no
negative-packet PASS is claimed.

N2: There is no numbered collection of independent walls. A supplied metric,
its dynamics, interacting control and physical selection are distinct open
obligations whose implications have not been classified as independent.

N3: The assumption table exposes tensor composition, selected Hamiltonian,
frame controls, scale, Fourier regularity, metric connection and spin lift.
The native code dictionary is linked main science; none of these supplied
choices is relabeled as an axiom consequence.

N4: No external negative witness is cited as proving an axiom boundary.
The two-cone vertex equations address the naive shear; the polar variation
addresses the precise strain commutator; the connection formula addresses
the missing subprincipal term. These matches are explicit in the proof.

N5: Per-element identities, per-site jets, per-mode comparisons and finite
box paths are checked in their declared domains. The uniform lattice
bound is analytical. No result quantifies over every metric coupling,
interaction, spin structure or dynamical gravitational construction.

N6: No axiom amendment is proposed. Frame choice, coordinate orientation and
spin lift are explicit conventions or supplied geometry; the dynamically
selected metric remains a physical construction problem.

N7: A stronger completion could add metric canonical variables and prove
coupled constraints, or establish an interacting scaling limit of this
frame family. Both are concrete untested mechanisms. The present result
supports those investigations and supplies no evidence excluding them.

N8: Current-main searches for common two-cone metrics and Kosmann/polar
frames found no matching native construction. The nearby Dirac--Kahler
cochain/Hodge Ward and shifted-origin overlap notes use different carriers
and derivative structures; their earlier local-frame issues motivated
checking actual support here. Their walls are not imported or counted.

## Review record and landing conditions

Author derivation and self-checking only. Independent review and the formal
retained audit path remain pending. One primary runner contains every
load-bearing finite check, so no helper registry or dependency-policy change
is required. The canonical cache, mutation receipt and intended graph delta
must match the final reviewed bytes. The note adds two repository links:
minimal axioms and native edge/CAR. No audit verdict, source epoch change,
axiom edit, main landing or metric-selection claim is part of this delta.
The later integrated landing candidate still requires the full pipeline,
strict lint and changed-science evidence-readiness pass.
