---
claim_id: native_weyl_gauge_hall_and_cone_flow_bounded_theorem_note_2026-09-13
claim_type: bounded_theorem
claim_scope: "For the specified filled two-node Wilson carrier, derive its free-band Hall coefficient and the leading Maxwell/Hall photon dispersion. Gapped integer-Chern stacks cannot cancel its fractional slice average at fixed node positions. Separately derive Hall-subtracted one-loop relative-metric and birefringent flows, their native logarithmic matching, and the exact exceptions to birefringence in a two-metric photon mixture. The dynamical gauge field and weak-coupling expansion are supplied. No complete native photon phase, all-orders flow, physical parameter selection or axiom-forcing theorem is asserted."
upstream_dependencies:
  - native_edge_record_matter_instrument_and_energy_ledger_bounded_theorem_note_2026-09-05
runner: scripts/native_weyl_gauge_hall_and_cone_flow_2026_09_13.py
---

# Native Weyl gauge response: the Hall term and conditional cone attraction

**Date:** 2026-09-13
**Type:** bounded_theorem
**Status:** proposed_retained

## Result and domain

The selected native two-node fermion has a nonzero anomalous Hall response.
Coupling it to an initially Maxwell dynamical gauge field therefore does not
justify extrapolating a Maxwell-only common-cone flow to arbitrarily low energy.
The leading quadratic response instead has a gapped photon and a photon that
is quadratic along the node-separation axis. This is a concrete obstruction
for this specified carrier, occupation and gauge action; several model-changing
cancellation routes remain open.

There is also a positive conditional result. After supplying Hall cancellation,
the one-loop matter/gauge relative metric is attracted toward equality, with
a coefficient derived below rather than assumed positive. General photon
anisotropy has a slower birefringent sector. A relative metric shear can source
that sector even when the initial photon is described by a single metric.

~~~yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact free-band topology and constitutive algebra, plus formal one-loop coefficients with an explicit native matching argument."
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "A common propagation law for the same native charged matter and a dynamical gauge field."
source_of_blocker_text: user_goal
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Construct and test a native Hall-cancellation mechanism and its surviving light-cone and phase obligations."
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
~~~

The [minimal framework memo](MINIMAL_AXIOMS_2026-06-29.md) supplies the ontology
reference. The conditional even-CAR representation is described in the
[current-main edge source](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md).
The selected Hamiltonian, filled lower band, continuous time, ordinary quantum
composition, Peierls coupling and noncompact Gaussian dynamical gauge field
are explicit inputs here. This note does not construct a finite-qubit photon
phase or identify this model as the uniquely selected physical law. It uses no
unmerged sibling proposal as a theorem premise.

| Statement | Mathematical domain | Boundary |
|---|---|---|
| Nonzero Hall coefficient | Free occupied-band adiabatic response of the specified lattice symbol | No all-orders interacting Hall theorem |
| Gapped/soft photon modes | Leading local Hall plus positive Maxwell quadratic action | No complete interacting spectral or lifetime theorem |
| Relative metric attraction | Formal one-loop expansion with Hall term canceled | No unconditional native infrared fixed point |
| Slower birefringent running and shear source | Linear anisotropy, with a stated second-order extension | No uniform all-orders large-log bound |
| Native logarithmic coefficients | Nonmerging cones, exact Peierls vertices, small-momentum annuli | Finite matching and autonomous gauge realization remain open |

All statements are author proposals pending independent review. External
coefficient comparators were visible during development. The original
Maxwell-only checks passed before the Hall omission was recognized; their
preserved evidence is linked in the review packet. Passing those checks did
not establish the completeness of the assumed photon action.

## The actual carrier and its occupied-band topology

Let a>0, r>0, 1/2<zeta<1, kappa=acos(zeta), v=sqrt(1-zeta^2), and
D=diag(1,1,v). Use dimensionless Brillouin coordinates k_i in (-pi,pi], cell
coordinates y=a D^-1 n, and two orbitals per coarse cell. The selected symbol is

    h(k)=(r/a) h0(k),
    h0(k)=sin(k1) sigma1+sin(k2) sigma2
          +(2+zeta-cos(k1)-cos(k2)-cos(k3)) sigma3.       (1)

Its only zeros are (0,0,+-kappa). The other simultaneous zeros of the first
two components have positive third component in the stated zeta interval.
The node derivatives in y coordinates are r(sigma1,sigma2,+-sigma3).
There are two Weyl cones, hence one four-component Dirac field for the local
loop trace; this counting does not erase their distinct lattice momenta.

Take zero temperature and chemical potential, filling the negative band.
The temporal gauge charge is n0+n1-1: a fixed neutralizing background of
one opposite unit charge per cell is supplied. This removes the net-charge
obstruction to the periodic Gauss constraint. A dressed Gauss-law state is
not constructed here; the background has no transverse Hall response.
At fixed k3, (1) is a gapped two-dimensional symbol except at the two nodes,
with mass parameter M=2+zeta-cos(k3). For its occupied projector P, fix the
Chern convention

    C(k3)=(1/(2 pi i)) int_T2 tr P[partial1 P,partial2 P] d2k.    (2)

For h0=d.sigma, P=(I-dhat.sigma)/2, the integrand divided by i is
-dhat.(partial1 dhat cross partial2 dhat)/2. Thus C is minus the degree of
the map dhat:T2->S2. This sign convention also fixes the Hall orientation;
reversing orientation changes its sign but none of the conclusions below.

A regular north-pole preimage must have sin(k1)=sin(k2)=0 and d3>0.
At the four corners (0,0),(pi,0),(0,pi),(pi,pi), the masses and local orientation
signs are respectively

    masses       (M-2, M, M, M+2),
    orientations (+1, -1, -1, +1).                           (3)

The degree is the sum of the orientation signs at the positive masses.
For 0<M<2 it is -1; for M>2 it is zero. These are the only slice regimes
encountered in (1). Consequently

    C(k3)=1 for |k3|<kappa, and 0 for |k3|>kappa.           (4)

The exceptional node slices have measure zero. The proof is a degree count,
not an inference from a sampled integer. The primary separately challenges
(4) with eigenvector link phases and integrated differentiated-projector
curvature at several gapped slice masses and resolutions. Slice resolutions
and floating tolerances were selected after exploratory runs; the exact
integer is established by the degree argument.

To connect (2) to the response, differentiating an occupied eigenvector gives
its empty-band matrix element divided by the band energy difference.
The antisymmetric adiabatic Kubo coefficient is therefore the integral of

    2 Im[<u-|partial1 h|u+><u+|partial2 h|u->]
                  /(E+-E-)^2
      = -d.(partial1 d cross partial2 d)/(2 |d|^3).        (5)

This equals the projector expression in (2); r cancels. Each gapped slice
contributes e^2 C/(2pi). The physical third momentum is q3=v k3/a, so

    H = e^2 int (dq3/(2pi)) C(q3)/(2pi)
      = e^2 kappa v/(2 pi^2 a) != 0.                     (6)

Here H denotes the Hall coefficient, with the orientation fixed above, and
e is the charge in a canonically normalized photon action. Near each Weyl
point the curvature is bounded by a constant times |q|^-2 and is integrable
in three dimensions. The Euclidean finite-frequency spectral denominators
are bounded by their zero-frequency gap denominators. Removing small node
balls and then taking their radii to zero justifies the leading adiabatic
coefficient by dominated convergence. Nonanalytic higher-derivative response
is not discarded or identified with this local one-derivative term.

Inversion is an exact symmetry: h0(-k)=sigma3 h0(k) sigma3. The selected model
is not time-reversal invariant. In particular, inversion does not remove its
Hall vector. Restricting attention to parity-even electric and magnetic
quadratic forms would miss (6).

## Consequence for the dynamical photon

The free-band determinant induces a local quadratic Hall term. Choose its
orientation so its real-time density is

    L_H=(H/2) epsilon^(3 mu nu rho) A_mu partial_nu A_rho.    (7)

For constant H on the bulk without boundary, its small-gauge variation is
a total derivative. The local linear-momentum coefficient K_mu_nu=A_mu_nu_rho q_rho
is antisymmetric in mu,nu by quadratic-action reciprocity and in mu,rho by
the Ward identity. It is therefore totally antisymmetric and has the form
epsilon_mu_nu_rho_sigma b_sigma q_rho. The computed xy frequency coefficient
fixes the corresponding z Hall vector. Its inverse kernel is transverse.
Gauge Ward identities therefore permit it; cancellation of a spurious photon mass does not cancel
this term. Boundary/global compact-gauge completion is not proved by (7).

With a unit-speed canonically normalized Maxwell term, Ampere and Faraday
reduce the electric-field wave equation, up to orientation, to

    [(omega^2-k^2) I+k k^T+i omega H C_z] E=0,
    C_z E=zhat cross E.                                   (8)

The determinant contains a nondynamical omega^2 factor. The two physical
roots obey

    (omega^2-k^2)^2-H^2(omega^2-k_perp^2)=0,
    omega_+-^2=k^2+H^2/2 +-sqrt(H^4/4+H^2 k3^2).          (9)

Along the node axis the positive frequencies are

    omega_+-=(sqrt(H^2+4k3^2)+-abs(H))/2.                 (10)

Thus omega_+(0)=abs(H), whereas omega_-=k3^2/abs(H)+O(k3^4).
This is a leading weak-coupling quadratic-response result, not a claim that
an undamped free photon remains the exact interacting excitation. Positive
finite Maxwell corrections cannot cancel the lower-derivative Hall term.
For the model's transverse rotation-symmetric epsilon_perp,b_perp, (10)
is replaced by

    (epsilon_perp omega^2-b_perp k3^2)^2-H^2 omega^2=0;
    omega_-=(b_perp/abs(H)) k3^2+O(k3^4).                 (11)

A two-linear-cone conclusion fails already at this order when H is nonzero.
The Hall-modified propagation mechanism is known; see
[Ying, Burkov and Wang, section II](https://link.aps.org/accepted/10.1103/PhysRevB.107.035131).
Equations (2)-(6) provide the matching calculation for this actual carrier.

There are concrete escapes. A separately supplied noncompact bare Hall
counterterm can cancel (6). A time-reversed charged copy has the opposite
Berry curvature; its contribution cancels after k->-k. Such a copy adds
gapless matter and is not the original two-node model. The primary checks
this cancellation pointwise. Node annihilation, translation-breaking
reconstruction, a different occupation, or an interacting phase transition
also change the hypotheses and are not excluded here.

Fully gapped additional charged bands with the same unit charge and primitive
translation cell supply an integer Chern number n on every k3 slice. Their
contribution shifts the dimensionless slice average to n+kappa/pi. Because
0<kappa/pi<1/3, it cannot vanish. This argument covers ordinary gapped band
additions at fixed original nodes; it does not cover fractionalized states,
new gapless sectors, altered charge assignments or a changed translation cell.

## What remains true after Hall cancellation

The rest of this note computes the Hall-subtracted perturbative model, or a
window where the Hall term is negligible compared with the photon momentum.
Cancellation is an explicit additional model condition. The native charged
model (1) with only a bare Maxwell field does not supply it.

Use the Euclidean action

    S=int [psibar gamma_a E_a_mu(partial_mu+i e A_mu)psi+F^2/4],
    {gamma_a,gamma_b}=2 delta_ab.                          (12)

For the coframe calculation E is real symmetric positive. The physical
statements below restrict to spatial E=diag(1,V), V symmetric positive, near
a common matter/photon metric, without time mixing. Continuous Euclidean
frequency, a massless weak-coupling expansion and a gauge-preserving
regularization are supplied. They are not consequences of the short-range
interacting Weyl theorem; that theorem cannot be applied to a massless
long-range photon exchange.

In Feynman gauge the photon propagator is delta_mu_nu/k^2. The common radial
logarithm is J=log(Lambda/mu)/(8pi^2). Define Gamma_mu=gamma_a E_a_mu.
Clifford multiplication gives

    sum_mu Gamma_mu (gamma.x) Gamma_mu
       =gamma.[(2 E^2-tr(E^2) I)x].                        (13)

Feynman parameterization of k^2 |E(p-k)|^2 uses
A(x)=x I+(1-x)E^2. Completing the square gives a shifted numerator
x E A^-1 p and determinant factor det(A)^-1/2. The inverse-fermion
coefficient of i gamma_a p_b, divided by e^2 J, is therefore

    M(E)=-int_0^1 dx x det(A)^-1/2
                    (2E^2-tr(E^2)I) E A^-1.             (14)

The sign follows from the inverse-propagator correction -<V G V>; in the
Hamiltonian convention its temporal vertex is iI. The native matrix-product
check below uses this convention separately. Expanding E=I+C yields

    M(I+C)=I-(5/3)C+(2/3)tr(C)I+O(C^2)
           =E-(8/3)C_tf+O(C^2).                          (15)

An independent integration path differentiates the unshifted propagator and
uses the S3 moments <n_a n_b>=delta_ab/4 and
<n_a n_b n_c n_d>=(delta_ab delta_cd+delta_ac delta_bd+delta_ad delta_bc)/24.
The primary compares these angular and parameter integrals for generic
positive coframes, as well as their linear derivatives.

Gauge-dependent longitudinal exchange changes the wavefunction, but not
this relative metric coefficient. Put q=E n and

    Y_j=gamma.E_j/q^2-2 (gamma.q)(E^T E n)_j/q^4.

Pointwise Clifford multiplication gives
(gamma.q)Y_j(gamma.q)=-gamma.E_j. The extra coefficient is thus proportional
to the full E, before time normalization. Removing that common factor from
(15) gives the fermion coframe flow

    dot C_f=-(e^2/(3pi^2))(C_f-C_g).                      (16)

A dot denotes differentiation with respect to L=log(mu0/mu). Spatial time
normalization is applied consistently on both sides.

## The photon coefficient and scalar cross-check

The four-component fermion bubble has trace

    4[q_mu(q+p)_nu+q_nu(q+p)_mu-delta_mu_nu q.(q+p)].      (17)

After its Feynman shift, dimensional radial integration by parts makes the
angular l_mu l_nu and l^2 contribution equal the explicit
x(1-x)p^2 delta_mu_nu term. Algebraically the radial factor is
(2/d-1)(d/2)(-2 Delta/(d-2))=Delta. The transverse coefficient is

    8 int_0^1 dx x(1-x) I2 (p^2 delta_mu_nu-p_mu p_nu),
    I2_log=log(Lambda/mu)/(8pi^2).                         (18)

Since int x(1-x)=1/6, the Maxwell increment is e^2/(6pi^2) per L.
The trace counts the two Weyl cones once. A gauge-preserving prescription,
or the full lattice Peierls bubble and contact, removes an apparent
quadratic mass term; the bubble alone is insufficient.

For a coframe E, transform momenta and external vertices by E and the
measure by det(E)^-1. The induced density is

    (1/4) det(E)^-1 (E^T E)_mu_rho (E^T E)_nu_sigma
                     F_mu_nu F_rho_sigma.                 (19)

Its linear coframe part, after photon normalization, gives

    dot C_g=+(e^2/(6pi^2))(C_f-C_g),
    R=C_f-C_g: dot R=-(e^2/(2pi^2))R.                     (20)

The weighted common coframe C_f+2 C_g is stationary at this linear order;
its value is not selected. Equation (20) covers all six symmetric spatial
relative components in the stated sector.

For E=diag(1,r,r,r), the elementary parameter integrals are

    I0=int_0^1 x/[x+(1-x)r^2]^(3/2) dx=2/(1+r)^2,
    Is=int_0^1 x/[x+(1-x)r^2]^(5/2) dx=2(2+r)/(3r(1+r)^2).

The fermion increments are z0=-e^2(1-3r^2)I0/(8pi^2) and
zs=e^2(1+r^2)Is/(8pi^2). Restoring unit photon speed at each step gives

    dot v=r(zs-z0)
      =e^2(1-r)(4r^2+3r+1)/(6pi^2(1+r)^2),
    dot c=e^2(r-1/r)/(12pi^2),
    dot r=dot v-r dot c
      =-e^2(r-1)(r^3+11r^2+9r+3)/(12pi^2(r+1)^2).       (21)

All factors apart from -(r-1) are positive for r>0. This independently checks
the relative eigenvalue in (20). The one-loop scalar speed comparator is
[Anber and Donoghue, section 4](https://arxiv.org/pdf/1102.0789);
[Isobe and Nagaosa, section II](https://arxiv.org/pdf/1205.2427) also treats
running velocities. Away from r=1 their named electromagnetic couplings have
normalization conventions that must not be silently interchanged.

## The slower photon sector

Write the reciprocal parity-even two-derivative photon medium as
L=(Efield^T epsilon Efield+Bfield^T b Bfield)/2 in Euclidean signature.
This paragraph concerns the two-derivative terms after the Hall condition
has been handled. Near identity epsilon=I+a and b=I+d. A spatial metric
coframe C_g gives

    a=2C_g-tr(C_g)I, d=-2C_g+tr(C_g)I,

plus a common scalar normalization. The other five components are

    W=((a+d)/2)_tf.                                      (22)

For W=diag(w,-w,0), epsilon=b=I+W is positive for |w|<1 but has squared
polarization speeds (1-w)/(1+w) and (1+w)/(1-w) along the third axis.
Gauge invariance and positivity thus permit birefringence even after H=0.

Let n=(n0,k) be a unit Euclidean loop direction and C(k)x=k cross x. The
W inverse-kernel insertion is

    K00=k^T W k, K0i=-n0(Wk)_i,
    Kij=n0^2 W_ij+[C(k)^T W C(k)]_ij.                    (23)

For trace-free W, K n=0, tr K=0 and <K>=0. Contracting its propagator
insertion with the differentiated fermion numerator gives 2 K_jnu gamma_nu;
its average vanishes. Thus W produces no linear fermion metric logarithm.
The fermion bubble supplies only a metric at linear order, while photon
normalization gives

    dot W=-e^2 W/(6pi^2), dot(e^2)=-e^4/(6pi^2).         (24)

With z=1+e0^2 L/(6pi^2), the derived truncated equations solve to

    e^2=e0^2/z, R=R0/z^3, W=W0/z.                       (25)

These are exact solutions of the one-loop, linear-anisotropy equations,
not nonperturbative statements about the actual lattice phase. General
Lorentz-violating QED one-loop beta functions provide a comparator in
[Kostelecky, Lane and Pickering, equation 28](https://arxiv.org/pdf/hep-th/0111123).
No empirical charge, energy hierarchy or experimental bound is inserted.

## A finite relative shear can generate birefringence

For a positive symmetric spatial V, (19) gives

    epsilon_f=V^2/det V, b_f=det V V^-2=epsilon_f^-1.

An initially flat photon plus a positive matter-loop weight u has
epsilon=I+u epsilon_f and b=I+u b_f. The commuting product is

    epsilon b=(1+u^2)I+u(epsilon_f+epsilon_f^-1).          (26)

In the shared eigenbasis, equal polarization speeds on all three axes
require epsilon_i b_i to be equal. This is also sufficient: if
epsilon b=Z^2 I, a single metric is reconstructed by
Vnew=Z sqrt(epsilon)/sqrt(det epsilon), with common normalization Z.
If x_i are the eigenvalues of epsilon_f, (26) is scalar exactly when all
x_i+1/x_i coincide. Each x_i is then x or 1/x. Using
x_i=v_i^2/(v1 v2 v3) gives exactly two escape classes:

1. V=v I, a scalar relative speed;
2. V has two eigenvalues one and a third arbitrary positive eigenvalue,
   an arbitrary rotated rank-one coframe change.

Both are genuine exceptions. General anisotropy is not automatically a
counterexample; its eigenvalues must be checked.

For V=diag(1+s,1-s,1), 0<|s|<1, the two squared speeds along the first
axis are (1+u b_f,zz)/(1+u epsilon_f,yy) and
(1+u b_f,yy)/(1+u epsilon_f,zz). Their difference starts at

    -u s^2(4-s^2)/(1-s^2)+O(u^2),                       (27)

which is nonzero with positive kinetic forms. An invertible coordinate or
field normalization cannot turn these two distinct characteristic surfaces
into one. This proves the stated failure of the single-metric family to
remain closed under this loop increment, within the specified domain.

For a small relative coframe R, the infinitesimal source outside the tangent
to the photon metric family at a flat photon metric is
2(R^2-tr(R)R)_tf. It must not be confused with a nonlinear coordinate
definition of exact birefringence: a single finite metric also contributes
quadratic terms to epsilon+b. The constitutive product (26) removes that
ambiguity.

For trace-free initial S0 with W0=0, the one-loop expansion through second
order gives

    R=S0/z^3+O(S0^2),
    dot W=-e^2 W/(6pi^2)+2e^2(R^2)_tf/(6pi^2)+O(S0^3),
    W=(2/5)(S0^2)_tf (z^-1-z^-6)+O(S0^3).               (28)

There is a second derivation. In the original fixed coordinates the linear
fermion metric is f(z)S0, f(z)=(1+2z^-3)/3. The photon accumulates its Maxwell
tensor with weight dz and is normalized by z. Put
m1=z^-1 int_1^z f(t)dt and m2=z^-1 int_1^z f(t)^2dt. The traceless part
of epsilon b is 4(m2-m1^2)(S0^2)_tf; hence W is half of it. Direct integration
gives 2(m2-m1^2)=(2/5)(z^-1-z^-6), agreeing with (28). Unknown second-order
metric corrections cancel from this product at the stated order. For a
nonzero real trace-free symmetric 3-by-3 S0, (S0^2)_tf cannot vanish: three
equal eigenvalue magnitudes cannot sum to zero unless all are zero.
No claim is made that the omitted orders are uniformly controlled as L->infinity.

## Native Peierls vertices and logarithmic matching

The supplied noncompact link field has gauge-fixed Euclidean denominator

    omega^2+sum_i [2 D_ii sin(k_i/2)/a]^2,                (29)

whose only zero is at omega=k=0. This is the Hall-subtracted free propagator
used in the perturbative coefficient calculation. It is not the resummed
asymptotic propagator of (1) with nonzero (6).

The oriented Wilson hoppings are T_i=-sigma3/2-i sigma_i/2 for i=1,2 and
T_3=-sigma3/2; the onsite term is (2+zeta)sigma3. Multiplying each hopping
by exp(i e a A_i/D_ii) gives the spatial vertex (with e removed)
Gamma_i(k)=r partial_i h0(k)/D_ii and its second derivative
r a partial_i^2 h0(k)/D_ii^2. For dimensionless transfer q,

    sum_i [2 D_ii sin(q_i/2)/a] Gamma_i(k)
       =r[h0(k+q/2)-h0(k-q/2)]/a.                       (30)

This exact identity uses the link-incidence momentum, not continuum q.
The two-photon contact is necessary for gauge cancellation. On a finite
3^3-cell band matrix, direct Peierls rebuilding gives the pure-gauge energy
curvature

    Tr(P H'')+2 sum_(occupied o, empty e)
                    |H'_oe|^2/(E_o-E_e)=0.             (31)

The primary constructs H',H'' independently from link phases and checks
both nonzero terms and their cancellation. This is a finite band diagnostic,
not a many-body native photon phase construction.

Common small spatial coframes are available as finite Laurent sources.
In h0 units add sum_aj C_aj D_jj sigma_a V_aj, where

    V_aj=sin k_j                       (a<3,j<3),
    V_a3=(zeta-cos k3) sin k3/v^2       (a<3),
    V_3j=sin k3 sin k_j/v               (j<3),
    V_33=(zeta-cos k3)/v.                               (32)

They vanish at both nodes and give the same physical coframe in the two
opposite chirality bases. Their Fourier support is finite, with paths of
length at most four in coarse coordinates; a fixed protected even-CAR path
representation and any required scheduling are supplied. All node jets
are checked, including off-diagonal sources. For sufficiently small C,
uniform invertibility of the cone derivative excludes extra nearby zeros,
and the positive gap on the compact complementary Brillouin region excludes
other zeros. No such statement is made for arbitrary large C.

Fix a nonmerging node pair and a small cone radius delta. On
mu<|q|<delta/a, the native symbol differs from its linear cone by O(a|q|^2),
its vertices by O(a|q|), and (29) from q^2 by O(a^2|q|^4). Uniform positive
quadratic bounds on these denominators show that the difference of each
logarithmically divergent differentiated integrand has a power-integrable
O(a|q|) relative remainder. Thus its logarithmic coefficient is the one in
(14)-(20). The compact hard region is analytic to the derivative order
needed; transfer near 2kappa reaches another matter node but a gapped photon,
and does not produce another infrared logarithm. Continuous-frequency tails
are integrable after these derivatives.

The actual shell challenge evaluates inverse-fermion matrix products with
both vertex derivatives and the Peierls tadpole. For the photon bubble it
uses the full two-node propagator and transverse time/spatial second
derivatives; its one-link seagull has no p^2 logarithm. Before multiplying
by e^2/(8pi^2), the scalar targets are

    fermion: -(1-3r^2) I0 and (1+r^2) Is,
    photon electric: 4/(3r), magnetic: 4r/3.             (33)

The two nodes are summed once for the photon. At r=0.8,1.2 and successively
halved radii, the symmetric angular averages approach these targets with
O(radius^2) errors. Odd Taylor powers cancel under the sphere symmetry.
The finite thresholds were chosen after exploratory runs and challenge the
written remainder argument; they are not certified universal error bounds.
Finite shell coefficients are not separately gauge-invariant observables.
The hard-region matching, including the Hall term already derived and
remaining finite metric/birefringent terms, cannot be set to zero by this
logarithmic matching argument.

## Scope of the Maxwell running window

Even the formal Hall-free charge running illustrates the limitation of
extrapolating (25). For a fixed node separation and Hall coefficient H0 at
scale mu0, photon
normalization would give H(L)=H0/z while mu=mu0 exp(-L). Therefore

    H(L)/mu=(H0/mu0) exp(L)/z.                           (34)

It grows at weak coupling. If H0/mu0=A e0^2 for fixed positive geometric A,
the end of a fixed small-H/mu window has
L=log(1/e0^2)+O(1)+O(e0^2 log(1/e0^2)). Thus z differs from one by only
O(e0^2 log(1/e0^2)); the Maxwell relative-cone suppression is still close to
one as e0^2->0. This is a perturbative intermediate-window estimate, not a
solution of the subsequent Hall-regime renormalization group. A different
propagator must be used there. Neither (25) nor the scalar positive sign in
(21) establishes the asymptotic common cone of the unsubtracted native model.

The immediate constructive question is whether the same native framework can
supply Hall cancellation with controlled charged content and a dynamical
photon phase. The current result does not force an axiom update.

## No-Go Discipline Gate

This gate concerns the two scoped negative boundaries: the unsubtracted
charged two-node model does not have the asserted Maxwell-only infrared
quadratic action, and two different metric Maxwell kernels can generate
birefringence. It does not claim all admissible models fail or that new axioms
are necessary. The entries are author checks, not retained audit authority.

### N1 — Distinct attack routes

| Family | Attempt and terminal obligation | Outcome and evidence |
|---|---|---|
| Occupied-band topology | **ATTEMPTED:** Recompute the response from the entire lattice band, allowing cancellation outside the cones. | The pole-preimage degree and spectral Kubo calculation give (4)-(6); hard bands do not cancel this carrier's fractional slice average. |
| Gauge variation and contact terms | **ATTEMPTED:** Test whether a Ward identity removes the extra photon term. | The contact cancels pure-gauge curvature in (31); the transverse one-derivative Hall kernel (7) survives. Gauge invariance alone does not remove it. |
| Ordinary gapped-band completion | **ATTEMPTED:** Add fully gapped unit-charge bands while keeping the primitive cell and original nodes. | Their slice Chern index is constant integer n, so n+kappa/pi cannot vanish in this domain. Fractionalized or new gapless completions are outside this argument. |
| Dynamical charge running | **ATTEMPTED:** Let screening suppress the Hall coefficient before it changes photon propagation. | Equation (34) grows relative to momentum; the conditional Maxwell window ends before asymptotic cone attraction. The subsequent Hall-regime flow remains open here. |
| Constitutive/coordinate reconstruction | **ATTEMPTED:** Reconstruct one metric from a positive sum of two metric kernels. | The product criterion (26) is necessary and sufficient in the commuting class. The scalar and rank-one classes survive; the explicit trace-free shear (27) fails. |
| Higher-derivative kinetic correction | **ATTEMPTED:** Change positive Maxwell stiffnesses to recover two linear modes with H nonzero. | The axis polynomial (11) retains the soft quadratic mode; two-derivative corrections cannot cancel a nonzero one-derivative coefficient. |
| Changed gapless content or counterterm | **ATTEMPTED:** Supply an opposite Hall copy or an explicit noncompact bare counterterm. | These are live escapes. The time-reversed copy cancellation is checked pointwise. They change the original model and prevent any universal no-go or axiom-forcing claim. |

These families differ in object and terminal obligation. Multiple numerical
methods for one integral are not counted as additional routes. None is ruled
out solely by an earlier source label.

### N2 — Relations among remaining conditions

For a full native charged continuum theory, G denotes autonomous gauge-field
realization/phase, M denotes finite matching and a mechanism for any required
Hall cancellation, and Q denotes controlled full interacting continuum
behavior. They are named tasks, not a proved independent-wall count.

| Pair | First completion implies second? | Second completion implies first? | Independence proved? |
|---|---|---|---|
| G, M | unresolved | unresolved | no |
| G, Q | unresolved | unresolved | no |
| M, Q | unresolved | unresolved | no |

There is no claimed minimal wall count. In the original free-band model,
nonzero H is a calculated result; changing it is a model-construction task,
not an undiscovered proof that its already computed value was zero. The
choice of a physical law from the framework remains supplied throughout.

### N3 — Hidden-premise scan

The proof's selected objects and limits are explicit: ordinary quantum/CAR
composition, continuous time, the two-orbital Wilson symbol, nonmerging nodes,
filled lower band at zero temperature and chemical potential, a fixed
neutralizing background, common unit charge, Peierls links, supplied noncompact gauge dynamics, and a formal weak
coupling expansion. Canonical normalization is a declared field/time
normalization, not a physical identification theorem. The Hall-subtracted
condition is promoted to the front of the note after the original omission.
The node counterterm, finite matching and source/path implementation are
supplied or open; none is asserted to follow from kinetic isotropy.

### N4 — Residual matching

No prior no-go is used as a witness for (6), (9), or (27).
The [June 18 exchange-matrix source](EMERGENT_LORENTZ_VELOCITY_RG_EXCHANGE_MATRIX_EXACT_SUPPORT_NOTE_2026-06-18.md)
addresses an already supplied positive two-speed matrix; its residual is the
actual interacting vertex calculation. It is a target comparison, not
support that this native model must possess its assumed photon kernel.
The [source-free Maxwell basin theorem](COMPACT_U1_QUADRATIC_BASIN_SOURCE_FREE_MAXWELL_UNIVERSALITY_BOUNDED_THEOREM_NOTE_2026-09-03.md)
explicitly excludes charged quantum matter, so (6) does not refute that
source-free result. These different residuals are not combined into a witness
count.

### N5 — Resolution and rhetoric

The negative photon conclusion is about the leading quadratic response of
the supplied occupied lattice band and gauge action. It is not about every
Admissibility law, every state, or all interacting phases. The single-metric
conclusion is restricted to the positive commuting mixture class (26), with
its exceptions listed explicitly. Primary cached stdout records:

- per_element: Clifford, constitutive and projector matrix identities;
- per_site: finite Peierls link derivatives and native coframe jets;
- per_mode: Hall/birefringent polarizations and logarithmic shells;
- per_block: occupied/empty and two-node trace factors;
- lattice_wide: gapped Brillouin-slice Chern and finite torus gauge checks.

No lattice-wide thermodynamic gauge phase or exact interacting spectrum is
claimed from those finite calculations.

### N6 — Partial closure and primitive scope

The [approved kinetic-isotropy source](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
supplies its stated kinetic-form equality. Its
[B4 application](EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md)
requires a B4-invariant action/measure for the corresponding loop relabeling.
The actual two-node axis and Hall response here do not satisfy that enlarged
symmetry. The primitive is not replaced by an unapproved one, nor extended
to a dynamical photon selection theorem. A common coordinate change or charge
normalization cannot remove the two characteristic surfaces or nonzero Hall
response; a supplied cancellation mechanism can. That is a constructive
model extension to test, not a labeling convention and not automatically a
new axiom.

### N7 — Steelman

A hostile reviewer can correctly object that this carrier is only one
admissible charged model. A time-reversed copy cancels its Hall response;
a different symmetry-protected gapless multiplet could make that cancellation
structural. Even with H=0, scalar or rotated rank-one metric changes avoid
(27), and stronger microscopic symmetries may forbid W. The terminal task is
to construct such a charged multiplet and gauge phase, verify the full
response and allowed perturbations, and show which modes remain gapless.
The explicit time-reversed curvature check is the strongest counterexample
to a broad impossibility claim. It does not make the original two-node
response zero. The note therefore retains the narrow model obstruction and
leaves these constructive mechanisms live.

### N8 — Cross-cycle echo

Fresh searches on origin/main b8c9d9d819911c5f3fec98b23d53355e7ff8c8bf for
anomalous Hall, birefringence, Carroll-Field, Chern-Simons and relative-metric
flow were compared with the closest sources. No matched source supplied this
native filled-band Hall/coupled-photon calculation. Existing dimension-six
Lorentz estimates and unrelated Chern-Simons channel-weight notes do not
settle it. The source-free Maxwell basin theorem already names charged and
parity-odd departures as scope boundaries; this note calculates one concrete
charged response. The B4 kinetic-form route shows a genuine symmetry-based
escape in its own domain. Both live mechanisms are preserved rather than
reclassified as impossible.

**Author gate disposition:** scoped boundaries only; no universal no-go,
retained verdict or axiom-update conclusion. Formal independent review remains
pending.

## Evidence and literature scope

The [primary](../scripts/native_weyl_gauge_hall_and_cone_flow_2026_09_13.py)
is a self-contained author challenge suite. It covers topology, response
matrices, gauge contacts, continuum loop coefficients, actual lattice shells
and positive exceptions. Symbolic proofs and their assumptions are stated
above; numerical agreement is used to challenge them. The
[review packet](work_history/repo/review_feedback/pr8098-evidence/kept/pr8098-REVIEW_HISTORY-3f4cb79c836849bf.md)
records exact source hashes, mutations, cached execution and the preserved
pre-Hall correction. Counts alone supply no independence or retained status.

Primary-source reading used for comparison was section 4 of Anber/Donoghue,
sections II A-C of Isobe/Nagaosa, the one-loop beta functions in equation 28
and the associated running discussion of Kostelecky/Lane/Pickering, and
section II of Ying/Burkov/Wang. Their wider phase or phenomenological claims
are not imported. The distinction between a full lattice electromagnetic
response and a symmetric continuum regulator is also discussed by
[Vazifeh and Franz](https://arxiv.org/pdf/1303.5784) and
[Goswami and Tewari](https://arxiv.org/pdf/1210.6352); only the identified
introductory/model and Hall-response passages were read, not their complete
papers. The native degree and Kubo calculations here fix the coefficient
without choosing it from those comparators.
