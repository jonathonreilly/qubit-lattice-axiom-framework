# Native strain response: working analytical derivation

Author proposal, 2026-09-13. Free filled negative band, a specified common-frame
coupling, and the ground-state response convention below. Independent review
is pending. No gravitational field equation is assumed or obtained here.

## 1. Frame coordinates and the contact term

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

The half-density connection derived in BLOCK06 is

    C(F)=-1/4 epsilon_abc F_ai (partial_i F_bj) (F^-1)_jc.     (R1)

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

## 2. Exact symmetric response

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

At omega=0 the two particle-hole orientations have opposite imaginary Pauli
traces and equal energy denominators, so R5 is the complete static Hessian
for these real traceless vertices. Its energy convention is
delta^2 E/V=sum_q S_A(-q) chi_AB(q) S_B(q). For a nonzero real cosine
source t A cos(q.x), its second derivative per volume is chi_AA(q)/2,
provided q and -q are distinct grid modes. For a constant source it is
chi_AA(0). These conventions will be challenged in position space.

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
source n(x). There is no n,n contact for this arithmetic choice, and no S,S expectation
contact by R3. Formula R9 follows by tracing the four terms of the nested
anticommutator. It is independent of frequency and a finite Laurent
polynomial in q. At q=0 it is the uniform strain one-point source <O_A>.
R5's nonpositive sign applies to the spectral response alone; the complete
seven-source Hessian includes R9 and need not have that sign. The chosen
joint source family is explicit and is not a selection from the axioms.

## 3. Exact infrared coefficient before the lattice remainder proof

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

The two nodes and angular measure 4pi/(2pi)^3 produce the candidate
nonanalytic response, with K=(omega,Q), kappa=|K| and P=I4-K K^T/kappa^2:

    chi_AB^log(K)=-kappa^4 log(1/kappa)/(80 pi^2 v)
                  [tr(P A4 P B4)-tr(P A4)tr(P B4)/3].      (R8)

For lapse plus strain replace A4 by diag(n,-A). This is equivalent in R8
to diag(0,-(A+n I)), since the difference is n I4 and the tensor annihilates
the four-dimensional trace. At zero frequency, writing P3=I3-Qhat Qhat^T,
the bracket for strains is tr(P3 A P3 B)-tr(P3 A)tr(P3 B)/3.
Unit-Frobenius TT polarizations have bracket one; the normalized transverse
spatial trace has bracket 1/3; longitudinal static strains have bracket zero.
A=B=I gives 2/3 and recovers the earlier lapse coefficient
-|Q|^4 log(1/|Q|)/(120 pi^2 v).

The coefficient in R8 has been obtained by a continuum annulus calculation.
The uniform argument in BLOCK07_IR_PROOF.md proposes its transfer to the
native R5 after subtracting its local constant and quadratic Taylor terms.
That analytical argument, including the source-coordinate hypotheses, remains
subject to author challenges and independent review.

## 4. Independent continuum normalization comparator

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
constant. Primary source: https://arxiv.org/pdf/hep-th/9307010 . The sections
on general three-point structures have not been read in full or imported.

## 5. A source of exact local-contact freedom to examine next

One may add to a specified native Hamiltonian an on-site term

    delta H_c[S]=c sum_x sum_i tr[(S(x+e_i)-S(x))^2] n_x.    (R10)

It vanishes for every constant S, and its value and first derivative vanish
at S=0. The half-filled flat state has <n_x>=1, so its exact quadratic energy
contribution is the displayed local difference functional. Arbitrary real c
therefore changes a two-derivative strain coefficient without changing the
flat matter or its first source vertex. This is a proposed family of source
couplings, not a change of the axioms or a physical choice of c. Its scaling,
full tensor extension and compatibility with the controlled one-particle
limit require explicit checks before a stronger conclusion is made.
