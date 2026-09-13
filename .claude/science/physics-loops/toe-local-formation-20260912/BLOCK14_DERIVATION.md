# Native star low-energy spectral dominance by a pull-through estimate

Author derivation,2026-09-13. Written before the finite checks. The supplied
native Gaussian bath, defect Hamiltonians and star transition are the same
objects as the positive Ward-scalar unit (PR8086). This is a statement about
the free-reference transition spectral measure. It is not an interacting
phase, a renormalization theorem or a physical clock identification.

The first route in BLOCK14_WORKING_PLAN used a quasi-local creator and three
annihilator derivations. The direct resolvent route below gives explicit
constants and avoids importing a separate quasi-local creator theorem.
The earlier route remains a useful general comparison, not a failed proof.

## 1. Objects, conventions and target

Let real Majoranas gamma_j satisfy {gamma_i,gamma_j}=2delta_ij. The supplied
real skew nearest-neighbor matrix is

K_(r,r+e_a)=h(-1)^(sum_(b<a)r_b), h>0.

Use its pure Gaussian Fock representation with covariance I+iK/|iK| and
H0=dGamma(omega), H0 Omega=0. In an eight-site cell r=2n+s, s∈{0,1}³,
k∈[-pi,pi]^3, the positive frequency has multiplicity four and

omega(k)=2h sqrt(sum_a sin²(k_a/2)).

The one-particle positive projector P_+(k) has every diagonal entry1/2:
the Hermitian matrix iK(k) has zero diagonal and squares to omega(k)²I.
The finitely many zero-frequency labels have measure zero. No normalizable
zero mode or band projector at k=0 is required.

For a pair A of the six center-incident legs set d_A,j=-K_(0,j) on those
two neighbors and zero elsewhere. Then ||d_A||=sqrt2h. Put

B_A=i gamma_0 gamma(d_A), D_A=H0+B_A,
R_A(z)=-(D_A+z)^-1, z>=0.

The positive-scalar unit derives the all-parity inequality D_A>=delta=h/4
and the real scalar7<h²alpha<330 with elementary radial suppliers. These
are explicit mathematical inputs to the present continuation. Define the
specified odd star transition vector, with every ordered pair retained, by

chi=(1/8)sum_(A∩C=empty) R_C(0) gamma_0 R_A(0) Omega.          (1.1)

There are90 terms. The original vacuum energy is used in every inverse.
For its free-energy spectral measures write

mu_1([0,E])=||1_(H0<=E) P_(N=1) chi||²,
mu_3plus([0,E])=||1_(H0<=E) P_(N>=3) chi||².

All particle numbers in chi are odd. The target is an explicit E^9 upper
bound for the complete nonlinear sector, an E^3 leading one-particle
measure, and a quantitative comparison. No high-particle sector is simply
discarded.

## 2. Domains and the exact pull-through identity

Choose measurable orthonormal band vectors u_b(k), b=1,...,4, for P_+(k).
The generalized annihilation distributions have measure d³k/(2pi)^3 and

{a(k,b),gamma_(2n+s)}=phi_(k,b)(2n+s)
                  =sqrt2 exp(-ik.n) conjugate(u_b,s(k)).

Thus each local coefficient has modulus at most sqrt2. Smearing gives the
ordinary bounded CAR annihilator a(f). All distribution identities below
are first tested against smooth compactly supported wave functions and
finite-particle test vectors, then extended in the indicated Fock domains.

There is no hidden number-domain assumption. Since B_A is quadratic in
finitely many bounded CAR fields, t↦exp(itN)B_A exp(-itN) is norm smooth to
all orders. H0 commutes with N. The gap delta makes the inverse of its
unitarily conjugate D_A uniformly bounded, so differentiating that inverse
shows that R_A(z) has bounded iterated commutators with N at every fixed
order. It maps Dom N^m to itself for every finite m. The local gamma_0 has
the same property and Omega is smooth for N. Consequently chi belongs to
Dom N^m for every finite m. In particular its integrated triple-annihilation
kernel exists in Fock L². This is established before estimating that kernel.

Put g=gamma_0 and, for lambda=(k,b),

L_A(lambda)=[a(lambda),B_A]
          =i[phi_lambda(0)gamma(d_A)-phi_lambda(d_A)g].       (2.1)

On the finite-particle core, [a(lambda),H0]=omega_lambda a(lambda).
Multiplication by the positive-gap inverses therefore gives

a(lambda)R_A(z)=R_A(z+omega_lambda)a(lambda)
             +R_A(z+omega_lambda)L_A(lambda)R_A(z).         (2.2)

This is equivalently the minus-energy shift in the negative-energy
resolvent convention. More explicitly, the annihilation map A sends a
smooth number-domain vector psi to the Fock-valued L² function
(A psi)(lambda)=a(lambda)psi. It obeys

A(D_A+z)psi=(D_A+z+omega_lambda)(A psi)(lambda)
                                         +L_A(lambda)psi.

Here the first operator on the right is a direct-integral self-adjoint
operator bounded below by delta. For a smooth psi, integrated graph norms
are finite because H0<=2sqrt3h N and the necessary number moments are finite.
Apply the identity to R_A(z)psi, already known to be smooth, and invert that
direct-integral operator. This proves(2.2) as an L² identity and hence almost
everywhere, without assigning an operator norm to a generalized annihilator.
Repeated application is legitimate because each shifted inverse and each
local linear insertion preserves all finite number domains.

Applying(2.2) twice and using a(lambda)Omega=0 gives the exact vector identity

a(lambda)chi=(1/8)sum_(A,C)[
 phi_lambda(0) R_C(omega)R_A(0)
 +R_C(omega)L_C(lambda)R_C(0)gR_A(0)
 -R_C(omega)gR_A(omega)L_A(lambda)R_A(0)]Omega.               (2.3)

Both local source corrections and both shifted inverses remain. Its vacuum
component is the one-particle transition amplitude.

## 3. Uniform higher-particle bound without a sector truncation

The local fields in(2.2) satisfy uniform bounds

||g||=1, |{a(lambda),g}|<=sqrt2<3,
||L_A(lambda)||<= (2+2sqrt2)h <5h,
|{a(lambda'),L_A(lambda)}|<=8h <3(5h).                       (3.1)

For the second line, |phi(0)|<=sqrt2, ||gamma(d_A)||=sqrt2h and
|phi(d_A)|<=2sqrt2h suffice. The last line follows by substituting(2.1)
and retaining both products. It does not use a vacuum expectation.
Give g the assigned norm bound1 and each L the assigned bound5h.
Contraction of either field costs at most three times its assigned bound.

Consider any word produced by commuting annihilators through
R_C g R_A. It has r shifted inverses and ell linear fields. A further
annihilator has one insertion branch for each inverse and one scalar
contraction branch for each field; its final annihilator kills Omega.
Passing an inverse adds L and one inverse. Passing a field contracts it
or moves the annihilator with its graded sign. All shifted inverse
parameters stay nonnegative, hence their norms stay at most1/delta.
A word bound means its coefficient absolute value times delta^-r and
the assigned field bounds; it is not the possibly smaller actual word norm.
The sum of bounds after this operation is at most

[r(5h/delta)+3ell] times the preceding word bound.

After j annihilators, r<=2+j and ell<=1+j. With delta=h/4 this multiplier
is at most43+23j. Therefore for every fixed m>=1, almost every ordered
m-tuple of one-particle labels, and the full Fock-valued amplitude,

||a(lambda_m)...a(lambda_1)chi|| <= C_m,
C_m=(180/h²) product_(j=0)^(m-1)(43+23j).                   (3.2)

The initial180/h² is(90/8)delta^-2. This bounds all resulting words and
all remaining particle sectors, rather than evaluating only the vacuum
component of a multiple-annihilation amplitude. In particular

C_3=45,464,760/h².                                         (3.3)

Let N_E count one-particle modes with omega<=E. Positive free energies
imply the commuting-projector inequality

1_(H0<=E) P_(N>=3) <= binom(N_E,3).

On the left, every particle lies in the low one-particle subspace and
there are at least three of them. The number-domain result permits the
standard integrated CAR identity

<chi,binom(N_E,3)chi>
 =(1/6) integral_(omega_1,omega_2,omega_3<=E)
          ||a(lambda_3)a(lambda_2)a(lambda_1)chi||² dlambda³. (3.4)

The1/6 is essential because the integral counts ordered annihilations.
For |k_a|<=pi, sin(|k_a|/2)>=|k_a|/pi. Thus

nu(E)=4 integral_(omega<=E) d³k/(2pi)^3
 <=4 volume_ball(pi E/(2h))/(2pi)^3
 =pi E³/(12h³).                                           (3.5)

The enclosing ball may extend outside the Brillouin cube; that only loosens
this upper bound. Combining(3.2)–(3.5) gives the all-energy estimate

mu_3plus([0,E]) <= K E^9,
K=45,464,760² pi³/(10368 h^13).                            (3.6)

More generally, replacing3 by m controls sectors N>=m by C_m² nu(E)^m/m!.
The constants are deliberately coarse. No independence of particles or
Gaussianity of chi is assumed; Gaussianity belongs to the supplied free
reference and its Fock representation.

## 4. The node amplitude equals the certified Ward scalar

For a cell vector u define its coefficient label at k=0 by phi^0_u(2n+s)=u_s.
This is solely an input to the finitely supported L_A formula, not an
operator or a vacuum annihilator. Set omega=0 in the bounded right side of
(2.3), take its vacuum expectation, and call the resulting linear functional
F0(u). Every term is a bounded original-vacuum matrix element.

Reflection of coordinate a, restored by the gauge gamma_r↦(-1)^(r_a)
gamma_(reflection_a r), preserves the actual K, the Gaussian reference,
and the entire two-bond defect family. The origin and its gamma_0 are fixed.
On the zero-cell coefficient labels it multiplies u_s by(-1)^(s_a).
Consequently F0 is invariant under each of these three diagonal sign maps.
All components with s!=0 are odd under at least one map, so

F0(u)=a0 u_0.                                              (4.1)

This uses only the covariance of the displayed bounded functional; no value
of a discontinuous band projector at k=0 is chosen. For q=e_0 in cell space,
phi_q(d_A)=0 and L_A(q)=i gamma(d_A)=J_A/2, where J_A=2i gamma(d_A).
Hence a0 is the bounded expression

(1/8)sum_(A,C)<R_C R_A+(1/2)R_C J_C R_C g R_A
                         -(1/2)R_C g R_A J_A R_A>.

Write x_A=R_A Omega and v_A=R_A J_A R_A Omega. Since R_A is self-adjoint,
J_A is anti-Hermitian and the ordered-pair matrix T is real symmetric,
the two half-corrections combine to minus Re<x,Tg v>. The direct term is
<x,T x>, a real number. Thus a0 is exactly the real alpha defined and
certified in the positive-scalar unit:

8a0=Re[<x,T x>-<x,Tg v>]=8alpha.                            (4.2)

This reconstructs the needed projected node bridge directly. The earlier
infinite-node source reached this identification through a smooth creator;
its numerical or quasi-local conclusions are not needed in this argument.
The physical derivation of the selected model and of the star transition
itself from framework axioms remains a separate task.

## 5. An explicit small-energy one-particle lower bound

For an actual normalized band vector at k, compare its local phi_lambda
with phi^0 having the same sqrt2 conjugate(u_b,s(k)) coefficients. The
origin coefficients agree. Only negative-neighbor cell phases differ.
Because the selected negative neighbors use distinct cell components,
Cauchy–Schwarz and |exp(ik_a)-1|<=|k_a| give

||L_A(phi_lambda)-L_A(phi^0)|| <=sqrt2 h|k|<=2h|k|.           (5.1)

For opposite pairs there is only one negative neighbor, so the same bound
holds. The resolvent identity gives
||R_A(omega)-R_A(0)||<=omega/delta².
In(2.3), the direct term has one shifted inverse, the first source term
has one, and the last source term has two. Using(3.1) and(5.1) therefore
bounds the one-particle amplitude remainder, for each band, by

(90/8)[sqrt2 omega delta^-3+15h omega delta^-4
                                   +4h|k|delta^-3]
 <=47,520 |k|/h²,                                         (5.2)

where omega<=h|k|, delta=h/4 and sqrt2<2 were used. The four-band vector
remainder has norm at most95,040 |k|/h². Its leading vector has entries
sqrt2 alpha conjugate(u_b,0(k)) and norm |alpha|, because(P_+)_(00)=1/2.
Thus its norm is at least|alpha|/2 whenever

|k|<=7/190,080,                                           (5.3)

using h²alpha>7. This argument needs no continuous choice of individual
band vectors at the node.

If0<E/h<=1/32768, the ball |k|<=E/h satisfies(5.3), lies in the Brillouin
cube, and has omega<=E. Integration over just this ball yields

mu_1([0,E]) >=alpha² E³/(24pi²h³)
            >49 E³/(24pi²h^7).                            (5.4)

The nonlinear-to-linear ratio is consequently bounded by

mu_3plus([0,E])/mu_1([0,E])
 <[45,464,760² pi^5/(432*49)] (E/h)^6.                     (5.5)

At E/h<=1/32768 this is less than10^-12, as an exact rational comparison
using pi<22/7 verifies. This is a deliberately conservative free-reference
energy window, not an experimentally calibrated crossover or a finite-
coupling phase claim. The bound applies to the complete higher odd sectors.

## 6. Leading spectral and imaginary-time asymptotics

Equation(5.2) gives the squared band-amplitude sum alpha²+O(|k|), uniformly
in direction. For E<2h, put y_a=2sin(k_a/2). The exact sublevel measure is

integral_(omega<=E) d³k/(2pi)^3
 =(1/(2pi)^3) integral_(|y|<=E/h)
      product_a(1-y_a²/4)^(-1/2) d³y
 =E³/(6pi²h³)+O(E^5).

The source remainder integrates to O(E^4). Therefore

mu_1([0,E])=alpha² E³/(6pi²h³)+O(E^4),
mu_3plus([0,E])=O(E^9).                                   (6.1)

The leading coefficient is tied to the actual positive Ward scalar, not an
unrelated local trial. Since the spectral measure is positive and finite,
Laplace integration by parts gives as tau→infinity

<chi,exp(-tau H0)chi>
 =alpha²/(pi²h³ tau³)+O(tau^-4).                            (6.2)

The entire higher-particle contribution separately obeys

<chi_3plus,exp(-tau H0)chi_3plus> <=9! K tau^-9, tau>0,      (6.3)

by(3.6). The high-energy remainder in the asymptotic argument is exponentially
small at any fixed cutoff; no large-time simulation is used.

The same measure bounds place chi_3plus in Dom H0^-p for every0<p<9/2.
The one-particle lower asymptotic makes chi fail to belong to Dom H0^-p
for p>=3/2. This follows from the layer-cake integral of the positive
spectral measure, not from a formal value at the Dirac node. These are
operator-domain conclusions in the supplied free reference only.

## 7. Sharpness in the class of local odd sources

This comparison concerns the E^9 upper exponent for the class of local odd
sources after their one-particle part is removed, not a nonzero cubic
coefficient of the particular star chi. Choose same-cell Majoranas g1,g2,g3
with internal labels0,2,4, from three distinct Γ_z pairs. Define the bounded
Wick-ordered operator

Y3=g1 g2 g3-<g1 g2>g3+<g1 g3>g2-<g2 g3>g1.

The Gaussian Wick identity shows that Y3 Omega has exactly three particles;
its one-particle term is subtracted with all three signs retained. In the cell convention of section2, put Γ_z=Z tensor Z tensor X,
with the usual two-by-two Pauli matrices. Along the positive z ray the
literal native iK(k)/omega(k) tends to -Γ_z, so the limiting positive
projector is (I-Γ_z)/2. Its compression to these three labels is I3/2. Projecting the three coordinate vectors and orthonormalizing them,
then adding the fourth band vector, gives a continuous band frame on a
sufficiently small angular cone around this ray and at small positive radius.

At the limiting central ray the matrix of the three selected band
coefficients sqrt2 conjugate(u_b,s_j) is I3. Therefore, for a fixed smaller
cone and sufficiently small radii, the determinant formed with any three
momenta in that cone, assigned respectively to these three bands, has
modulus at least1/2. This follows by continuity of its nine entries, not
from a numerical sample of the cone.

The three-particle wave function is precisely that determinant. Its squared
norm uses the ordered-label integral divided by3!. For small E, restrict
each of the three momenta to that cone with radius between E/(6h) and E/(4h).
Each frequency is at most E/4, so the total energy is below E. Each shell
has a fixed positive multiple of (E/h)^3 measure. The determinant lower
bound then gives a positive constant times (E/h)^9 spectral weight.
The corresponding upper E^9 bound follows either from the same bounded
three-field wave function or the local triple-annihilator estimate.

Thus E^9 is attained by a local comparison source in this native bath.
Additional symmetries of a specific star can suppress its cubic coefficient;
sections1–6 require only the upper bound and make no contrary assertion.

## Author validation state

The first32 checks pass: exact constants and native cell/reflection algebra,
a shifted four-mode Fock comparator for full-matrix pull-through and triple
word recursion, a nonvacuous factorial moment, the paired half-Ward identity,
and Wick subtraction. The ratio comparison is at most2.4188e-14 at the
chosen window, below the stated10^-12 bound. These are same-author checks,
not an independent source review or an infinite proof by enumeration. The
number-domain and direct-integral arguments above are the analytical
justification. The subsequent complete cold source pass is recorded separately.
Canonical packaging and independent source review remain pending. No independently retained status, source landing or new axiom is
claimed.
