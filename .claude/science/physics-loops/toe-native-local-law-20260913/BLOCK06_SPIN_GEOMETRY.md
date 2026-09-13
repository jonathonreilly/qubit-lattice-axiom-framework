# Metric-dependent spin transport and a native connection term

Author derivation, conditional on a supplied smooth positive frame and the
standard torsion-free metric connection. This does not derive a dynamical
metric, canonical gravitational momentum or Einstein constraints from the
minimal axioms. The finite-range native construction is the new carrier
question; the spin geometry below is established mathematical machinery,
rederived here to fix its signs and hypotheses.

## 1. Polar frame action on the metric and spinor together

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
local action on the PAIR (E,psi). A global statement uses a specified spin
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
with the D of BLOCK06_DERIVATION.md.

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

## 2. Full spatial Dirac operator on half-densities

Now allow an arbitrary smooth real invertible frame F with positive determinant,
using INTERNAL rows and coordinate columns: e_a=F_ai partial_i. Set
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

    F=[[A(z),B(z),0],[B(z),D(z),0],[0,0,c]], c>0,
    C=-c[(A-D)B'+B(D'-A')]/[4(AD-B^2)].                 (P10)

Thus even in the positive gauge a generic nonuniform frame needs this term.
For F=I+t S(x), S symmetric, its first variation vanishes: the contraction
of epsilon_abc with partial_a S_bc is zero. This recovers the linear response
used in (D5) in unit-speed coordinates; it is not a claim at every anisotropic
base frame in the same coordinate gauge.

Levi-Civita uniqueness under pullback, (P8), and the chain rule imply

    h_E' U_phi,E=U_phi,E h_E                            (P11)

for (P1)-(P2); multiplication by a lapse transforms by scalar pullback, so
H_E'[N o phi^(-1)] U=U H_E[N]. In (P11) the operator and its frame BOTH
change. This is spatial covariance of a supplied geometric Dirac operator,
not closure of normal deformations of dynamical geometry.

## 3. The two native cones need opposite scalar terms

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
intertwining. This is a SPECIFIED derivative-dependent frame coupling.
The derivative defining C may be supplied analytically for sampled smooth
fields, or approximated by a local frame stencil with its error quantified.
No exact native diffeomorphism symmetry is claimed.

For constant F, C=0 and the earlier global two-node preservation proof applies
under its stated smallness bound. For nonuniform F, this note makes no global
momentum or exact two-node zero-set assertion; (P12) is a local continuum
statement. Periodic nonuniform frames can admit a Bloch description. The full
frame source varies both the principal part and C(F). Interacting RG bounds,
finite-spacing spin covariance and a dynamical origin of F remain open.

## 4. Planned checks and next proof obligation

Independently construct the Christoffel connection from rational frame jets
and compare its full matrix term to (P9). Check both orientation signs and
the nonzero rotation and positive-frame examples. Challenge (P3) using
successive noncommuting matrices, and (P6) using independently differentiated
polar factors. Then establish a quantitative slowly varying lattice bound
for (C6)+(P13); test an actual variable frame rather than only a constant cone.

Literature used as context and convention checks: Godina--Matteucci,
math/0504366, the specific portions recorded in the campaign reading ledger;
Chervova--Downes--Vassiliev, arXiv:1209.3510v2 (currently abstract and section1
read; section6 and Appendix A to be read); Dąbrowski--Dossena,
arXiv:1209.2021 (PDF located, detailed proof not yet read). The spectral
characterization and global spin-bundle claims are not imported here.

## 5. Normal/normal identity with the complete curved operator

Let nabla_i^hd=partial_i+A_i-Gamma^k_ki/2 act on spinor half-densities.
For real smooth N,M define a^i=G^ij(N partial_j M-M partial_j N) and
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
Normal transformations of the metric require additional canonical variables
and a gravitational Hamiltonian. The second-quantized matter bracket also
requires a chosen representation and control of possible continuum central
terms. None follows from one-particle identity (P14).

## 6. Completed source reading and author checks

The connection and polar-action checker first passed128 checks. Adding the
curved normal/normal comparison yields160 checks, all PASS, in53.185seconds;
source SHA9ab3118e8e27ef539f3df2d8dd4cef3d2192f62aecb9cabb4b2c754cc6f98ef5.
The separate variable-frame checker passes103 finite challenges. These are
author checks of load-bearing calculations, not independent review.

Reading update: Chervova--Downes--Vassiliev, arXiv:1209.3510v2, section1,
section6 lemma/proof, section7 proof, and Appendix A in full, including the
spin-structure obstruction example and the half-density conjugation(A.19).
The spectral theorem's sections2-5 were not fully read or imported. Their
lemma6.1 is a primary comparison for a scalar subprincipal term, and the
rotation example agrees with the independently fixed sign above.
Dąbrowski--Dossena, arXiv:1209.2021, sectionsV-VII, propositions2-3 and their
proofs were read, with the introductory spin-bundle definitions only partly
read. This supplies context for changing the metric and retaining the spin
lift. The local formula here uses the explicitly checked Pauli/Koszul
normalization, not an unexamined transcription of their connection notation.
