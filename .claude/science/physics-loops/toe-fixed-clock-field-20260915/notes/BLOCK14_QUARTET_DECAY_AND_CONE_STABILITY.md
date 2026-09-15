# On-shell decay channels in the supplied Hall-free quartet

Personal derivation, 2026-09-15. PROVISIONAL; personal derivation and challenge checks, not an independent audit.
These are leading-order rates in a supplied massless weak-coupling phase.
They do not prove its existence, an isolated charged pole or an empirical
prediction of the minimal framework.

## 1. What real coframe running leaves unanswered

Blocks11 and13 compute real velocity and constitutive coefficients. Unequal
cones also permit emission and pair creation. Their rates are a separate
check on a proposed low-energy particle description. Use a canonically
normalized Maxwell photon with speed one, Coulomb-gauge transverse modes,
and a two-component massless Weyl field

 H_f(p)=sigma dot Vp,   V=V^T>0,
 J_i=e sum_a V_ai sigma_a.

The vacuum fills the negative band and empties the positive band. Node
momenta are separated, so the small-momentum photon couples within each
cone. The full quartet supplies a consistent Hall-free lattice completion;
a lone charged chiral continuum theory is not asserted to be a complete
quantum gauge model. Rate means probability loss per unit Hamiltonian time,
not emitted energy per unit time. Fermion spinors have norm one and photon
normalization is1/sqrt(2|k|). Set hbar=1.

The established vacuum-Cherenkov and photon-decay mechanism is discussed in
[Klinkhamer and Schreck](https://arxiv.org/pdf/0809.3217), sectionIII and
AppendixA. Those sections were read and their leading massless coefficients
are used as a comparator. Their photon/charge conventions differ away from
the equal-speed point. No historical experimental bound is imported here.

## 2. Exact kinematic tests for a positive anisotropic coframe

Let G=V^2 and E(p)=sqrt(p^T Gp), p!=0. The electron group velocity is
v_g=Gp/E(p). Convexity gives
 E(p)-E(p-k)<=v_g dot k<=|v_g||k|.
Therefore emission of a speed-one photon is impossible when |v_g|<=1,
apart from the zero-measure equal-cone collinear limit with vanishing
transverse current. If |v_g|>1, choose k initially along v_g. The energy
excess is positive at small |k| and negative at sufficiently large |k|;
continuity supplies a nonzero emission solution. Thus the strict
Cherenkov threshold is

 |Gp|/E(p)>1.                                      (1)

For photon momentum k, the minimum electron-hole energy is
 min_p[E(p)+E(k-p)]=E(k), by the norm triangle inequality, with equality
for collinear nonnegative partitions. The strict pair-creation threshold
is therefore

 |k|>|Vk|.                                        (2)

These are different tests at finite anisotropy: group and phase velocities
must not be interchanged. Equality surfaces require separate threshold
limits. The rate formulas below use strict timelike/spacelike cases.

There is also an exact compact angular formula for the fermion rate. If
|v_g|>1, let w=v_g/|v_g| and integrate photon directions m on the cap
m dot w>1/|v_g|. Define

 a_m=m^T Gm-1, b_m=m dot Gp-E(p),
 k_m=2b_m/a_m, q=p-k_m m, E_q=E(p)-k_m,
 n_p=Vp/E(p), K_m=V(I-mm^T)V,
 T_m=[tr K_m/2](E_q-Vq dot n_p)+(Vq)^T K_m n_p.

Then, with the two photon polarizations summed,

 Gamma_f=e^2/(4pi^2) int_cap [T_m/a_m] dOmega_m.    (2a)

On this cap b_m>0 and Cauchy-Schwarz implies a_m>0 and0<k_m<E(p). Indeed equality in k_m<=E(p) would
require V m=n_p, which would force a_m=0 and is excluded inside the cap.
Conversely a positive on-shell root with positive final energy must lie
on the cap: the same inequality excludes the a_m<0,b_m<0 branch.
The radial energy delta has absolute derivative k_m a_m/(2E_q).
T_m is E_q times the exact transverse Pauli spin sum, written without a
final-spinor denominator. This form remains bounded when E_q is small.
It provides a direct finite integral for a general positive coframe,
without replacing it by an isotropic speed.

## 3. Massless isotropic fermion: derive the full Cherenkov rate

First V=vI, v>1. Put p=|p|, photon magnitude k, q=|p-k| and let c be the
angle cosine between p and k. Energy conservation gives

 q=p-k/v,
 c=1/v+[k/(2p)](1-1/v^2),
 0<k<2pv/(v+1).                                  (3)

With P_n=(I+sigma dot n)/2, the transverse spin sum is

 sum_lambda Tr[P_(p-k) (sigma dot epsilon_lambda)
                   P_p (sigma dot epsilon_lambda)]
       =1-(n_(p-k) dot khat)(n_p dot khat).        (4)

The golden-rule rate, including the vertex v and the photon normalization,
is

 Gamma_f=2pi e^2 v^2 int d^3k/[(2pi)^3 2k]
                S(p,k) delta(vp-vq-k).

The angular delta derivative is vpk/q. Put a=1/v and x=k/p. The remaining
polynomial is

 (q/p)S=(1-a^2)[1-a x+(1+a^2)x^2/4].             (5)

Integrating0<x<2/(1+a) gives

 Gamma_f/E = e^2/(6pi)
              (v-1)(4v^2+3v+1)/[v(v+1)^2],      (6)

where E=vp. There is no factor of two for the two helicities of a Dirac
field: a specified external particle uses one chiral line. Equation(6)
also holds for a Dirac particle of specified helicity in the massless limit.
For v<=1 the corresponding Cherenkov rate is zero.

Weighting the same differential rate by photon energy k gives the distinct
radiated power

 P_f/E^2=e^2/(12pi)
              (v-1)(9v^2+4v+1)/[v(v+1)^3].      (7)

For v=1+u, u>0,

 Gamma_f/E=e^2 u/(3pi)+O(e^2 u^2),
 P_f/E^2=7e^2 u/(48pi)+O(e^2 u^2).               (8)

Both leading coefficients agree with the cited massless small-deformation
limits after matching the relative speed and leading charge normalization.

## 4. Exact anisotropic photon-decay tensor at leading coupling order

For one Weyl cone, choose real orthonormal transverse photon polarizations
e_a dot k=0, a=1,2, and write omega=|k| and
 Q^2=omega^2-k^T Gk.
For Q^2>0 the probability-decay matrix in polarization space is

 Gamma_(ab)= e^2/[24pi omega det V]
       [Q^2 e_a^T G e_b+(e_a^T Gk)(e_b^T Gk)].   (9)

For Q^2<0 it vanishes. A Dirac cone contributes twice(9). Different
separated cones add; they are distinct final states, so their rates cannot
cancel with opposite chirality or opposite shear. The matrix is positive
semidefinite in its allowed domain. It need not be proportional to the
identity at finite anisotropy.

Here is a direct phase-space derivation, without importing a photon pole.
Change variables q=Vp in the two final fermion momenta. The spatial measure
is divided by det V and the external spatial vector is K=Vk. The current
vertex becomes sigma dot(V e_a). Let K=|K| and, for this calculation,
choose the third axis along K. The final energy variable q ranges from
(omega-K)/2 to(omega+K)/2. Its polar angle is fixed by

 cos(theta)=[K^2-omega^2+2omega q]/(2Kq),
 q_other=omega-q.

The angular energy delta contributes q_other/(Kq). The remaining spin
matrix is

 S_ab=(a dot b)(1-n dot m)/2
        +[(n dot a)(m dot b)+(n dot b)(m dot a)]/2,
 a=V e_a, b=V e_b,

where n,m are the directions of the two rescaled final momenta. The
antisymmetric chiral part integrates to zero. Azimuthal integration and
integration over q give

 int dq dphi [q(omega-q)/K] S_ab
     =(pi/3)[Q^2(a dot b)+(a dot K)(b dot K)].

The golden-rule prefactor is e^2/(8pi^2 omega det V), yielding(9).
The formula at K=0 follows by continuity; the displayed angular coordinates
are used only for K>0. For V=vI, v<1, each photon polarization has

 Gamma_gamma,one-Weyl/omega=e^2(1-v^2)/(24pi v).  (10)

As a useful algebraic cross-check, the isotropic rates obey
 Gamma_f/E=-pi beta_v/v for v>1 and
 Gamma_gamma,one-Dirac/omega=-pi beta_c for v<1,
using only the separate fixed-photon fermion and photon coefficients in
source equation21. The full relative-speed beta function is not beta_v.
This comparison is specific to these displayed leading-order formulas.

## 5. Small anisotropy and the actual quartet

Let V=I+C, C=O(delta), and fix a unit direction n with n^T Cn bounded
away from zero as a fraction of delta. Put u(n)=n^T Cn. Equations(1)-(2)
become the positive and negative signs of u(n), respectively, to first
order. Equation(9) immediately gives

 Gamma_gamma,one-Weyl/omega
       =e^2[-u(n)]_+/(12pi)+o(e^2 delta),         (11)

independently of polarization at this leading order. The term
(e_a^T Gk)(e_b^T Gk) begins at second order because e_a dot k=0.
The induced photon birefringence in Block11 is also second order, so it
does not change(11) away from the angular threshold surfaces.

For the fermion the corresponding leading result is

 Gamma_f/E=e^2[u(n)]_+/(3pi)+o(e^2 delta).         (12)

The cap formula(2a) gives a uniform rescaling proof. For u>0 with the
stated margin, write c=m dot w=1-y(1-1/|v_g|),0<=y<=1, and azimuth phi.
Then |v_g|=1+u+O(delta^2), w=n+O(delta), and uniformly on this cap

 a_m=2u+o(delta), k_m/|p|=1-y+o(1),
 T_m/a_m=|p|(1+y^2)/2+o(|p|),
 dOmega_m=(u+o(delta)) dy dphi.

The cancellation in T_m avoids a spurious singularity at y=0. Its bounded
polynomial/rational expression supplies domination, since a_m is bounded
below by a fixed multiple of delta. Integrating(1+y^2)/2 from0 to1 gives
2/3 and proves(12). For u<0 with the stated margin, (1) forbids emission
for sufficiently small delta. This is not uniform as u(n)/delta->0.
For example V=I+d(E_xz+E_zx), p along x has u(n)=0 but
|v_g|^2=(1+6d^2+d^4)/(1+d^2)>1 for d!=0. Thus its exact Cherenkov channel
is open even though the first-order rate vanishes. Along y the same V
leaves both the phase and group velocities exactly one. No blanket
zero-rate inference is made on the leading angular boundary.

For this specific shear and p along x the boundary rate can itself be
derived. At |p|=1 write a photon direction as
 m=(sqrt(1-d^2(y^2+z^2)),d y,d z).
As d tends to zero through nonzero values, the cap becomes the disk
 D={(y,z):y^2+(z-2)^2<5}, and dOmega=d^2[1+O(d^2)]dy dz.
With r^2=y^2+z^2 and a0=1+4z,

 k_m -> 1-r^2/a0,
 T_m/a_m -> F(y,z)
   =[1+4z+8r^2-4zr^2+r^4]/[2(1+4z)^2].         (12a)

On the closed disk a0>=9-4sqrt(5)>0. The denominator-free final-spin form
of T_m gives a bounded integrand even at r=0, where the limiting final
particle is soft. The exact cap, its Jacobian and these coefficients
converge; dominated integration applies. Integrating first in y gives

 int_D F dy dz = int_(2-sqrt5)^(2+sqrt5) sqrt(1+4z-z^2)
 [z^2/30-7z/60+131/480+193/(60(4z+1))
                         +181/(480(4z+1)^2)] dz =7pi/3.

The required semicircle moments are I0=5pi/2, Iz=5pi, Iz2=105pi/8;
the two reciprocal moments are both pi/2. They follow from
 int_-R^R sqrt(R^2-t^2)/(a+b t) dt
   =pi[a-sqrt(a^2-b^2 R^2)]/b^2
and its a derivative, at R=sqrt5,a=9,b=4. Therefore

 Gamma_f/E=7e^2 d^2/(12pi)+o(e^2 d^2)             (12b)

for this fixed coframe family. It is not obtained by substituting the
second-order group-speed excess into(12): that first-order expansion is
not uniform at this angular boundary. A physical quartet at this order
also has the second-order photon metric and birefringence in Blocks11-13;
(12b) is an exact-coframe diagnostic, not its complete boundary width.

For the actual reflected quartet in instantaneous common metric coordinates,

 C_i-C_g=s_i d(E_xz+E_zx)/z+O(d^2),
 u_i(n)=s_i 2d n_x n_z/z+O(d^2),
 e^2=e0^2/z,

with two s_i=+1 and two s_i=-1. At a generic direction n_x n_z!=0 there
are two faster and two slower cones at first order. Every faster fermion
has

 Gamma_f/E =2e0^2 |d n_x n_z|/(3pi z^2)
             +higher coupling/anisotropy orders,          (13)

while the two slower cones together give each photon polarization

 Gamma_gamma/omega=e0^2 |d n_x n_z|/(3pi z^2)
             +higher coupling/anisotropy orders.          (14)

Thus Hall cancellation and zero average shear do not cancel these decay
channels. In the running-coupling approximation their rates become small
relative to energy as z grows. That statement addresses this kinematic
width only. It neither proves a finite quasiparticle residue nor excludes
soft-photon infraparticle behavior. A photon pole, controlled long-time
spectral measure and a full interacting phase remain separate obligations.
No physical energy hierarchy or experimental number is fitted.

## 6. Scope and verification

The exact formulas(6)-(10) are tree-level decay rates, corresponding to
imaginary one-loop self-energies, for the supplied continuum action.
The native application uses only separated-cone small-momentum matching
and the previously derived leading metric contrast. Hard lattice thresholds,
node mergers, additional decay channels, finite density, a compact-gauge
phase, and uniform resummation are not handled.

The companion checks the actual Pauli trace, exact one-dimensional scalar
integrals and power, a separate angular phase-space integration of(9),
the native leading contrast count and the boundary coefficient(12b).
The phase-space momentum triangle uses symmetric longitudinal components
(K+omega x)/2 and(K-omega x)/2 and transverse magnitude
sqrt((omega-K)(omega+K)(1-x)(1+x))/2. This avoids subtracting two nearly
parallel large vectors at a soft endpoint. Its first cancellation failure
is preserved, as is the initial insufficient boundary angular quadrature.
The respective tolerances were retained while construction and resolution
were corrected. Finite checks do not establish an actual lifetime in an
unconstructed microscopic phase.
