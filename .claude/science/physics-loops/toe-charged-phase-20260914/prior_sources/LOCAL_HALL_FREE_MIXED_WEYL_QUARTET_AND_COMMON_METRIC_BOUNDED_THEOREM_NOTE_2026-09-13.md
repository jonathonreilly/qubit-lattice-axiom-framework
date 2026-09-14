---
claim_id: local_hall_free_mixed_weyl_quartet_and_common_metric_bounded_theorem_note_2026-09-13
claim_type: bounded_theorem
claim_scope: "For a specified nearest-neighbor four-orbital CAR Hamiltonian with ordinary onsite T squared equal to one, derive its full zero set, simple Weyl charges, occupied-band Hall cancellation and precise local perturbative stability. A nonzero onsite mixing family has exactly equal four-node metrics; generic symmetry-preserving changes of its mixing direction split those metrics. This is a supplied free carrier, not an autonomous native gauge phase, universal physical multiplet, generic common-cone attractor or axiom-forcing theorem."
upstream_dependencies:
  - native_edge_record_matter_instrument_and_energy_ledger_bounded_theorem_note_2026-09-05
runner: scripts/local_hall_free_mixed_weyl_quartet_and_common_metric_2026_09_13.py
---

# A mixed Weyl quartet with zero Hall response and an explicit common metric

**Date:** 2026-09-13
**Type:** bounded_theorem
**Status:** proposed_retained

## Result and supplied domain

A nearest-neighbor four-orbital fermion model can have nonzero onsite flavor
mixing, four separated simple Weyl nodes and exactly zero occupied-band Hall
response. The cancellation follows from ordinary time reversal in the full
mixed model. It does not require separately conserved copies.

For one explicitly selected direction of the onsite mixing, all four Weyl
nodes also have the same positive propagation metric in the same coordinates.
The node phase and Hall cancellation persist under sufficiently small
symmetry-preserving perturbations. Exact equality of the four metrics does
not follow from those symmetries: an arbitrarily small allowed change of
mixing direction produces a calculated metric contrast. This distinction
separates a constructive common-metric carrier from a theorem of dynamical
selection or radiative protection.

~~~yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-range band construction, exhaustive zero-set algebra, local stability proof and explicit metric-equality discriminator."
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "A charged local matter carrier that removes the Hall obstruction while allowing a shared propagation metric."
source_of_blocker_text: user_goal
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Construct the native dynamical gauge phase and determine whether its allowed quantum corrections preserve or attract the required matter/gauge metrics."
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
~~~

The [minimal framework memo](MINIMAL_AXIOMS_2026-06-29.md) is the ontology
reference. The [current edge construction](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md)
is a comparator for conditional even-CAR carriers. Here the CAR algebra,
coarse cells, four orbitals, continuous Hamiltonian time, translation symmetry,
ordinary onsite time reversal and the displayed Hamiltonian are supplied.
They are not selected from the axioms by this note. No unmerged proposal is
used as a theorem premise, no primitive is added, and no quantum gauge phase
is inferred from a Bloch Hamiltonian.

The target is an explicit model and its boundaries. Time-reversal-invariant
Weyl semimetals and their vanishing anomalous Hall response are established
prior art; see [Halasz and Balents](https://arxiv.org/pdf/1109.6137), sections
I and II. The contribution here is the stated local family, its complete
root algebra and mixed-sector metric discriminator. It is not a claim to
have discovered the general time-reversal mechanism.

## A local mixed carrier

Use dimensionless k in the three-torus, 0<b<pi/2, 1/2<zeta<1, and real
mixing parameters mu,theta. Sigma matrices act on the two orbital components
inside each flavor; tau matrices act on flavor. Tensor identities are omitted.
Define

    H(k)=sin(ky) sigma2 + A(k) sigma1 + B(k) sigma3,
    A=a I+b1 tau_z+m1 tau_x,     B=c I+d tau_z+m3 tau_x,
    a=-cos(kx) sin b,            b1=sin(kx) cos b,
    c=2+zeta-cos(kx)cos b-cos ky-cos kz,
    d=-sin(kx) sin b,
    m1=mu sin theta,             m3=mu cos theta.                 (1)

At zero mixing this is diag(h0(k-b xhat),h0^*(-k-b xhat)), where

    h0(k)=sin kx sigma1+sin ky sigma2
          +(2+zeta-cos kx-cos ky-cos kz) sigma3.                  (2)

The real-space operator is the CAR second quantization of H. Four modes
per coarse cell have a 16-dimensional on-cell Fock space. This does not by
itself replace three-dimensional fermion statistics with tensor-product
qubit locality; any protected even-CAR realization remains a separately
specified representation condition.

For an explicit finite-range realization write

    H(k)=H_on+sum_i [T_i exp(i k_i)+T_i^dagger exp(-i k_i)],
    H_on=(2+zeta)sigma3+tau_x(m1 sigma1+m3 sigma3),
    T_i=(C_i-i S_i)/2,
    C_x=-sin b sigma1-cos b sigma3,
    S_x=tau_z(cos b sigma1-sin b sigma3),
    C_y=C_z=-sigma3, S_y=sigma2, S_z=0.                        (3)

All hoppings are nearest-neighbor cell hoppings and the mixing is onsite.
A factor r/a, with r,a>0, can multiply the entire symbol; it changes energies
and units without changing its zeros, projectors or Hall cancellation.

The exact antiunitary and reflection actions are

    T=tau_x K,  T^2=+I,   T H(k) T^-1=H(-k),
    Mz:kz->-kz,           H(kx,ky,kz)=H(kx,ky,-kz).             (4)

K is complex conjugation in this displayed orbital basis. These are chosen
model symmetries, not an identification with every encoded framework time
reversal. The full [current-main discrete-symmetry note](DISCRETE_SYMMETRIES_P_T_AND_CPT_OF_THE_EMERGENT_FERMION_BOUNDED_THEOREM_NOTE_2026-09-03.md)
concerns a different supplied staggered Hamiltonian, finite geometries and
an eight-dimensional massless corner kernel. Its higher degeneracy and
encoded symmetry action are not premises for the simple-node argument here.

The displayed family has an additional fixed-momentum spectral
anti-symmetry J=sigma2 K, with J^2=-I and J H(k) J^-1=-H(k).
It pairs positive and negative energies. It is not a same-energy Kramers
statement and is not required of the general perturbations below.

For mu!=0, no momentum-independent nontrivial flavor projector commutes with
all H(k). Indeed the separate Fourier coefficients sigma2 and sigma3 force
a commuting matrix to be flavor-only. The sin(kx) coefficient then forces
it to commute with tau_z, and the nonzero onsite mixing forces it to commute
with tau_x. Their joint commutant is scalar. Thus a constant onsite change
of basis cannot turn this mixed family into independently conserved copies.
A momentum-dependent spectral decomposition is a different operation and
is not excluded or used as a protecting local symmetry.

## Complete zero-set algebra

Since sin(ky)sigma2 anticommutes with the rest of H,

    H^2=sin^2(ky) I+[A sigma1+B sigma3]^2,

and a zero requires sin ky=0. In the sigma2 eigenbasis the remaining operator
has off-diagonal blocks Q and Q^dagger, where Q=B+i A. Thus

    det H|_(sin ky=0)=|q|^2,  q=det Q.

For arbitrary k the two squared energy magnitudes are

    E_+-^2=S+-2 sqrt(U),
    S=sin^2 ky+a^2+b1^2+c^2+d^2+mu^2,
    U=(a b1+c d)^2+(a m1+c m3)^2+(b1 m3-d m1)^2.             (5)

To derive (5), H^2 has scalar part S and the three pairwise-anticommuting
non-scalar matrices tau_z, tau_x and sigma2 tau_y, with coefficients
2(a b1+c d), 2(a m1+c m3) and 2(b1 m3-d m1). The spectral anti-symmetry
then gives energies -E_+,-E_-,E_-,E_+.

Put L=2+zeta-cos ky-cos kz, t=cos kx. Directly expanding det Q gives

    q=L^2-2Lt exp(i b)+exp(2i b)-mu^2 exp(2i theta).          (6)

The imaginary and real parts after multiplication by exp(-i b) are

    Im=sin b(1-L^2)-mu^2 sin(2theta-b),
    Re=cos b(1+L^2)-2Lt-mu^2 cos(2theta-b).                 (7)

L is strictly positive everywhere on ky=0 or pi. Define

    R^2=1-mu^2 sin(2theta-b)/sin b,
    X=[cos b-mu^2 sin(2theta)/(2sin b)]/R.                  (8)

If R^2<=0 there are no zeros. Otherwise use its positive square root R.
If |X|>1 there are no zeros. In the remaining cases every zero, and only a
zero, is obtained from

    kx=+-acos X,
    ky=0:  cos kz=1+zeta-R,   if zeta<=R<=2+zeta;
    ky=pi: cos kz=3+zeta-R,   if 2+zeta<=R<=4+zeta.         (9)

Duplicated endpoint roots are counted once on the torus. This is a full
algebraic classification, not a grid search. Interior values in either
R interval with |X|<1 give four separated nodes in that plane. Endpoint
values have merging roots and are outside the simple-node statements.
For R outside both intervals or |X|>1, compactness gives a positive
zero-energy gap. The special R=2+zeta can have roots in both ky planes;
these have sin kz=0 and are not simple Weyl nodes.

## Local metric and chirality from the determinant

At a root let x,y,z denote its coordinates, c=R-X cos b, and define

    Delta^2=E_+^2=4(sin^2 b+mu^2 cos^2 theta),
    q_x=2 sin x R exp(i b),
    q_z=2(c-i X sin b)sin z.                                (10)

The zero subspace has dimension two and the spectators have energies
+-Delta. This follows either from (5) and q=0 or from the rank-one Q block;
Delta>0 because sin b>0. Its squared low-energy dispersion has metric

    G_yy=1,  G_xy=G_yz=0,
    G_ij=Re(q_i^*q_j)/Delta^2,  i,j in {x,z}.               (11)

One way to prove the normalization is E_-^2 E_+^2=|q|^2 on ky=0,pi.
The ky derivative is cos y sigma2, giving the unit y coefficient and no
cross terms. This derives (11) without fixing eigenvector phases.

For completeness, a smooth two-band basis at the node can be chosen from
the positive and negative sigma2 eigenspaces. In that basis the effective
matrix is [[cos y delta ky,f^*],[f,-cos y delta ky]], and to first order
f is q divided by a nonzero complex spectator factor of magnitude Delta.
Thus the Pauli-Jacobian determinant is

    det V=-cos y Im(q_x^*q_z)/Delta^2
         =4 cos y sin x R^2 sin b sin z/Delta^2.             (12)

Interior roots of (9) are therefore simple, with chirality
sign(cos y sin x sin z). The occupied projector carries the opposite Chern
charge with the convention C=(1/(2pi i)) integral tr P[dP,dP]. The x-z
metric determinant is [Im(q_x^*q_z)]^2/Delta^4>0.

The primary separately projects the full 4 by 4 velocity matrices onto the
zero subspace, reconstructs its three Pauli components, and compares the
metric and orientation with (10)-(12). Closed occupied-frame link products
on small cubes challenge the local Chern charges without using those formulas.
The finite checks support the analytic argument; they do not exhaust its
continuous parameter domain.

## An aligned nonzero mixing with one common metric

Choose theta=b and mu^2<1-zeta^2. Now R=sqrt(1-mu^2), X=R cos b,
and the complete zero set reduces to

    (kx,ky,kz)=(+-x*,0,+-z*),
    x*=acos(R cos b), z*=acos(1+zeta-R).                    (13)

All four are simple: R>zeta>0, x*,z*>0 and x*,z*<pi. The onsite mixing is
mu tau_x(sin b sigma1+cos b sigma3), which is nonzero for mu!=0 and has
the scalar commutant proved above. At these nodes

    Delta=2 sin x*,
    q_x=2 sin x R exp(i b),
    q_z=-2i R sin b exp(i b)sin z,
    G=diag(R^2,1,R^2 sin^2 b sin^2 z*/sin^2 x*).             (14)

The two complex derivatives are orthogonal as real vectors, so G_xz=0.
Every entry of G is identical at the four nodes in the same original
coordinates. This is exact, including nonzero mixing. At mu^2=1-zeta^2,
opposite charges meet at z=0. At larger mu^2 the aligned family is gapped;
the argument includes mu^2>=1 because (7) then has no positive L solution.

For the overall symbol (r/a)H, a common coordinate normalization
D=sqrt(G), y=a D^-1 n gives physical momenta delta k=a D^-1 p and a common
squared matter dispersion r^2 |p|^2. This names a common matter metric; it
does not derive a physical length calibration, a photon metric or dynamical
spacetime. In fixed coordinates the anisotropic G in (14) remains the result.

## What equality does and does not survive

Inside a simple four-node phase, (8) gives

    X-R cos b=mu^2 sin(2(theta-b))/(2R sin b),
    Re(q_x^*q_z)=4 sin x R sin z(R cos b-X).                 (15)

For mu!=0, exact equality of the four metrics in this displayed family
therefore requires theta=b modulo pi/2. Those directions are allowed,
explicit escapes from a claim that mixing must split the cones. The second
direction theta=b+pi/2 has R=sqrt(1+mu^2) and also gives a common metric
whenever (9) is in its simple-node domain; it is not ruled out.

But theta=b+epsilon, for arbitrarily small generic nonzero epsilon,
preserves T and Mz, keeps the separated nodes, and gives opposite signs of
nonzero G_xz at opposite chiralities. A common invertible coordinate change
cannot make distinct matrices equal: B^T G_1 B=B^T G_2 B implies G_1=G_2.
An onsite unitary only changes the Pauli frame and leaves G unchanged.
Thus symmetry-related cones need not have equal metrics in common coordinates.
Their equal eigenvalue sets under a spatial reflection are weaker than equality.

For example, the simpler choice theta=pi/2 has m3=0. If
mu^2<min(sin^2 b,1-zeta^2), its roots have X=cos b/sqrt(1-mu^2),
Delta=2sin b, and

    G_xz=-sin x cos b mu^2 sin z/sin^2 b != 0.              (16)

This was the first tested mixing. The aligned construction (13)-(14) was
found after preserving that mismatch, so the negative result was not used
to declare a universal obstruction. For still more general T,Mz-symmetric
Hamiltonian perturbations, additional reflected metric components can vary;
(15) is not a classification of every local Hamiltonian.

## Stability of the node phase and common filling

Fix any member with four simple nodes strictly inside the first interval
of (9). Allow finite-range, translation-invariant, number-preserving
Hermitian four-band perturbations V(k), small in the uniform C2 norm and
preserving (4). There is a positive smallness threshold, depending on the
chosen member and its distance to the merging boundary, such that H+V has
exactly four simple type-I nodes at a common energy mu_F and no other Fermi
surface at chemical potential mu_F. No uniform threshold at a merger is
claimed. The spectral anti-symmetry J need not be preserved.

Here is a local estimate proof. Choose four disjoint balls about the nodes,
related by T and Mz. Their middle two bands are uniformly separated from the
spectators. A smooth spectral projector, followed by polar orthonormalization
against a fixed local reference plane, gives a smooth exact two-band matrix

    d0(k) I+d(k).sigma.

At each unperturbed center, d=0, d0=0, and the derivative V0 of d is
invertible. In fact d0 vanishes throughout these unperturbed balls by the
spectral pairing. Let s be the smallest singular value of V0. Shrink the
ball so that the unperturbed derivative differs from V0 by at most s/4.
Small C2 perturbations keep that derivative difference below s/2 and make
|grad d0|<s/4. They can also make |V0^-1 d(center)|<r/4.

The map k->k-V0^-1 d(k) is then a contraction with Lipschitz constant at
most one half on the radius-r ball and maps it into itself. It has a unique
zero k*. For any k in the ball, integration of the derivative bound gives
|d(k)|>=(s/2)|k-k*|. At mu_F=d0(k*),
|d0(k)-mu_F|<=(s/4)|k-k*|, so the two energies d0+-|d| lie strictly on
opposite sides of mu_F off the node. This excludes local type-II pockets
and any second Fermi surface in the ball. The spectral projector construction
and these norm bounds persist by continuity of separated spectral subspaces.

T and Mz map each unique node to the node in the corresponding ball.
The four nodes form one orbit, hence their energies are equal. A compact
positive gap away from the balls persists under sufficiently small C0
perturbations and the small common chemical-potential shift. The spectators
stay separated as well. This completes the global no-other-Fermi-surface
statement within the specified neighborhood.

An explicit challenge adds

    delta [tau_y sigma3+0.31 tau_z sigma2
       +(0.4cos kx+0.23cos ky+0.17cos kz) I].               (17)

It preserves T and Mz but breaks J and the extra x reflection of the
original family. The four roots move, acquire a common nonzero energy and
remain type I for the tested small delta. This tests the distinction between
symmetry-enforced common energy and an incorrectly assumed fixed zero energy.
The numerical root solve is a challenge, not the proof of the C2 neighborhood.

## Hall cancellation in the actual occupied four-band model

Fill the two lower bands at zero temperature and chemical potential zero
for (1), or at the common mu_F in the stability neighborhood. The charge
per cell is n1+n2+n3+n4-2, with a supplied static background of two opposite
unit charges. There are two occupied bands at every non-node momentum,
so this removes the net-charge obstruction to a periodic Gauss constraint.
It does not construct a locally gauge-dressed many-body state.

For the occupied rank-two projector, ordinary time reversal gives
P(-k)=T P(k) T^-1 and hence its real Berry-curvature two-form obeys
F_ij(-k)=-F_ij(k). The Kubo representation is

    F_ij(k)=2 Im sum_(o occupied,e empty)
       <o|partial_i H|e><e|partial_j H|o>/(E_o-E_e)^2.      (18)

It remains valid across degeneracies internal to the occupied or empty
subspace by taking the corresponding projectors; only their mutual gap is
needed. Integrating (18) over the torus gives zero Hall vector exactly.
Near a simple type-I node, the curvature is O(|q|^-2), locally integrable
in three dimensions. Removing symmetric small balls and then shrinking them
makes the cancellation and the occupied-band adiabatic limit well-defined.
There is no uncanceled integer-Chern background hidden by counting nodes only.

There is a stronger slice statement. On every gapped constant-kz slice,
T gives C(kz)=-C(-kz), while Mz gives C(kz)=C(-kz). Thus its total occupied
Chern number is zero. Opposite local charges still occur at distinct kx
positions on each node plane; zero total slice Chern does not gap them.
The primary uses both the full Kubo sum and occupied-frame link products.

If a coupled state, action and regulator preserve unbroken T, a local
zero-field Hall coefficient remains forbidden by that symmetry. This is a
conditional symmetry statement, not a proof that a dynamical interacting
phase exists or avoids spontaneous T breaking. Nonlinear Hall effects,
higher-derivative optical activity and other allowed responses are not
excluded by this zero linear Hall coefficient.

## Gauge coupling and the remaining native obligation

Give all four orbitals the same unit charge. Peierls-dress every hopping
in (3) by a link phase; onsite mixing is gauge invariant without a link.
For this nearest-neighbor symbol the finite-momentum spatial Ward identity is

    sum_i 2sin(q_i/2) partial_i H(k+q/2)=H(k+q)-H(k).        (19)

The two-photon contact is the second link derivative, not an optional
addition. On a finite periodic torus, a pure gauge transformation conjugates
the full hopping matrix. The second derivative of its occupied energy is

    tr(P H'')+2 sum_(o,e) |<o|H'|e>|^2/(E_o-E_e)=0.        (20)

The primary rebuilds the Peierls links and verifies their covariance,
filled-band spectrum and cancellation in (20), with each term nonzero.
These finite free-fermion checks do not supply a quantum link Hilbert space,
Gauss-law ground state, deconfined photon, interacting continuum or renormalized
matter/gauge common cone. Those are the next construction obligations.

## Scoped minimum content

In an ordinary Bloch band problem with onsite T^2=+1, suppose the only
Fermi-level degeneracies are simple isolated twofold Weyl nodes and the
occupied bundle is gapped elsewhere. A non-invariant momentum node has a
T partner of the same chirality: curvature reverses under T, while inversion
of the enclosing sphere reverses its orientation. Total occupied monopole
charge on the Brillouin torus is zero by Stokes after deleting node balls.

A simple twofold Weyl node cannot sit at a T-invariant momentum in this
specified T^2=+1 setting. In its two-dimensional subspace choose T=K.
The linear Hamiltonian must then be purely imaginary Hermitian, so only
one Pauli matrix can occur and its three-direction Jacobian has rank at
most one. Therefore simple nodes occur in same-charge pairs, and at least
two pairs are needed to cancel total charge. The construction attains four.

This is a scoped band lemma, not a selection of the physical particle
multiplet. T^2=-1 Kramers-Weyl systems, projective translation/time-reversal
actions, higher-multiplicity degeneracies, extra Fermi surfaces and interacting
topological order are outside its hypotheses. The current-main staggered
corner example has a higher-dimensional degeneracy and does not contradict it.

## No-Go Discipline Gate

### N1 — Distinct routes and actual scope

Five real ways of pursuing a shared propagation law were examined here:

| Approach family | Actual disposition |
|---|---|
| Antiunitary symmetry of the full occupied band | Exact Hall cancellation survives mixing; nodes and filling have a local stability proof |
| Onsite mixing construction | The first sigma1 choice splits metrics; the aligned direction repairs equality exactly, with a second aligned direction also allowed |
| Common coordinate or spinor-frame redefinition | Cannot turn distinct metric matrices into one; common normalization is valid only after equality is established |
| Topological and symmetry protection under generic local perturbations | Protects the node phase and Hall cancellation in the stated neighborhood; allowed angle changes disprove protection of metric equality |
| Local electromagnetic gauge covariance | Both aligned and unequal-metric carriers satisfy the exact Ward identity and finite gauge-contact cancellation, so gauge covariance alone does not select equality |

These are not five proofs of impossibility or an exhaustive inventory of
Admissibility laws. The positive aligned escape is central to the result.
Dynamical interaction and microscopic symmetry selection remain additional
live routes; their quantum gauge phase is not executed here.

### N2 — Wall relations

The native gauge phase, quantum correction to metric equality, and selection
of the physical multiplet are distinct unresolved questions with potentially
shared dependencies. No independence count is assigned. The first metric
mismatch is not an extra universal wall: it has been repaired within the
same local family by an explicit coupling choice.

### N3 — Hidden inputs

CAR composition, coarse-cell translation, continuous time, the four-orbital
symbol, ordinary T and Mz, common charge, half filling, neutralizing background
and external Peierls field are supplied. The aligned coupling relation is
explicitly selected. A common coordinate normalization is a convention once
one common metric exists; it is not a force that makes unequal cones equal.

### N4 — Residual matching

The current-main discrete-symmetry source addresses a supplied staggered
finite system, not robustness of these separated nodes. The edge source
provides a conditional carrier comparison, not a quantum photon phase.
Neither source is used as a no-go witness. The exact angle discriminator
answers a more specific question than full emergent Lorentz dynamics.

### N5 — Resolution and rhetoric

The source proves exact statements for this free local band family and a
specified small-perturbation neighborhood. Primary cached stdout distinguishes
per-element algebra, per-site hopping and vertices, per-mode nodes and
metrics, per-block occupied projectors, and lattice-wide slice/finite-torus
checks. No finite check is identified with an interacting thermodynamic phase.

### N6 — Partial closure and primitive scope

Hall cancellation and even exact bare matter-metric equality are concrete
partial closures. Neither needs a new framework axiom. The selected symmetry
and coupling relation are conditions on a model; promoting either to a
universal primitive would be a separate owner decision and is not done here.
The dynamical gauge construction remains an open route, not a dismissed one.

### N7 — Steelman

The strongest counterargument to a broad metric obstruction is the aligned
nonzero mixing in (13)-(14), proved in this note. A further microscopic
symmetry, parameter-selection mechanism or interacting attraction could
remove the tuning obligation. Conversely, an interacting instability could
invalidate a proposed gauge phase even though the free Hall coefficient is
zero. Both possibilities remain live. The precise surviving negative claim
is only that T and Mz alone do not enforce equal metrics under all their
allowed small Hamiltonian perturbations.

### N8 — Cross-cycle echo

Current-main searches at b8c9d9d819911c5f3fec98b23d53355e7ff8c8bf covered
Weyl mixing, separated nodes, four-node and quartet terms, and the closest
discrete-symmetry source was read fully. The established literature already
uses time reversal to cancel Hall response and construct four-node phases;
that mechanism is applied rather than recast as unavailable. The campaign's
initial sigma1 mismatch and later aligned repair are both preserved in the
review packet. No failed route is promoted to an axiom-forcing conclusion.

**Author disposition:** conditional constructive theorem and explicit scope
boundary, pending independent review. No universal no-go or retained audit
verdict is issued.

## Evidence and reading scope

The [primary](../scripts/local_hall_free_mixed_weyl_quartet_and_common_metric_2026_09_13.py)
is self-contained. Its symbolic identities, projected velocities, occupied
Chern calculations, finite-gauge contacts and symmetry-preserving perturbation
fixtures challenge different load-bearing parts of the proof. Their counts
are not a measure of independence or TOE completion. Floating tolerances and
resolutions were selected with exploratory outputs visible.

The [review packet](../.claude/science/physics-loops/local-hall-free-mixed-quartet-20260913/REVIEW_HISTORY.md)
records canonical execution, source hashes, mutations and preserved discoveries.
Independent review, integrated validation and formal audit remain separate.
Halasz/Balents sections I and II were read fully; their realistic-material
sections and transport predictions were not imported. The current-main
September 3 discrete-symmetry note was read fully as a scope comparator.
The displayed determinant and stability arguments stand on their stated
hypotheses rather than a claimed full-paper or full-repository review.
