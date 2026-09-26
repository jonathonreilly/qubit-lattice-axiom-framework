# Two transverse wave polarizations from supplied immutable exchanges

2026-09-21. Primary construction; independent reconstruction is pending.
This uses a larger classical record alphabet than the seven-state acoustic
model. It is a test of mathematical compatibility, not a derivation of
electromagnetism, a qubit implementation, or a selection from the axioms.

## 1. Explicit additional alphabet and vector observables

There are fifteen local states: vacancy; six axis labels A,+/-e_j; and eight
cube labels B,(sigma_1,sigma_2,sigma_3), sigma_j in {+1,-1}. If label contents
are represented as unit direction tags, the B direction is sigma/sqrt(3).
There is no duplicate direction tag and no changing of an occupied content.
The split into these two cubic orbits is an additional model choice.

Define two fixed vector observables on one site:

    e(a)=+/-e_j on an A label, zero otherwise,
    b(a)=(sigma_1,sigma_2,sigma_3) on a B label, zero otherwise.

The second observable is deliberately scaled by sqrt(3) relative to its
unit direction tag. The symbols e and b label observable functions; their
names do not identify electric or magnetic fields physically. Every event
swaps complete nearest-neighbor endpoint states. Consequently all fourteen
global occupied-label counts, and both vector totals, are exactly conserved
in the absence of formation. Individual records never acquire a new label.

Use a fixed real gamma and the symmetric two-label tensor

    S_i(a,b)=(gamma/2)[e(a) cross b(b)+e(b) cross b(a)]_i.    (1)

On the four-site collinear context (l,a,b,r) around an i-edge set

    h_i=S_i(l,a)+S_i(a,r)-S_i(l,b)-S_i(b,r),
    c_i=kappa+max(h_i,0), kappa>0,

or c_i=K0+h_i/2 with K0>|gamma|. Here |S_i|<=|gamma|/2 and
|h_i|<=2|gamma|, attained by opposite transverse A endpoints and equal
appropriately oriented B contexts. Rates are bounded and every unequal
endpoint swap has a fixed positive floor. The read footprint has four sites;
the update has two. Coordinate periods at least4 give distinct footprints.

Equation (1) transforms as a vector under the 24 proper cubic rotations,
so the positive-edge rule is covariant under those joint spatial/label
rotations. With both e and b transformed as ordinary vectors, their cross
product is axial under improper rotations. No natural-inversion symmetry,
electromagnetic parity assignment or time-reversal symmetry is asserted.
An additional polar/axial state action is analyzed separately in
`MAXWELL_POLAR_AXIAL_SYMMETRY_EXTENSION.md`; it is an extra assignment and
does not change the failed literal-inversion control here.

Endpoint interchange gives c(eta)-c(eta^edge)=h. Periodic telescoping of the
symmetric-pair expression gives sum_x h_i=0 pointwise. Thus every homogeneous
product law is invariant. This proof is unchanged for fifteen rather than
seven states. Positive-floor swaps connect exactly the arrangements of each
fixed multiset; no record relabeling collision is used.

## 2. Exact current potential and complete linearization

For the occupied probabilities p_a, write

    rho_A=sum_(a in A) p_a, rho_B=sum_(a in B) p_a,
    rho=rho_A+rho_B, p0=1-rho,
    X=sum_a p_a e(a), Y=sum_a p_a b(a),
    Psi_i=gamma (X cross Y)_i.

The symmetric tensor (1) has this product expectation. The exact product
species current for all fifteen labels is

    J_a^i=gamma p_a [e(a) cross Y+X cross b(a)-2X cross Y]_i. (2)

For vacancy both vector functions vanish, so J_0=-2p0 Psi and the total
occupied-density current is 2p0 Psi. The separate orbit-density currents are

    J_(rho_A)^i=(1-2rho_A)Psi_i,
    J_(rho_B)^i=(1-2rho_B)Psi_i.                            (3)

For fourteen independent occupied probabilities, C=diag(p)-p p^T and
J_i=C grad_p Psi_i. Therefore A_i C=C A_i^T for A_i=D_p J_i, by the same
categorical entropy identity as in the acoustic construction. This is
entropy compatibility, not a physical energy or action assignment.

Fix an interior orbit-isotropic product

    p_a=rho_A/6 on A, p_a=rho_B/8 on B,
    rho_A>0, rho_B>0, rho_A+rho_B<1.                        (4)

Then X=Y=0, E[e e^T]=(rho_A/3)I, E[b b^T]=rho_B I, and E[e b^T]=0.
All covariances of X,Y with the orbit densities or the remaining shape
observables vanish. Since both Psi and its first derivative vanish at (4),
the complete linear current acts only in the six X,Y coordinates:

    partial_t delta X = a curl delta Y,
    partial_t delta Y = -b curl delta X,
    a=gamma rho_A/3, b=gamma rho_B.                        (5)

The other eight coordinates have zero linear current. One full invertible
fourteen-field coordinate system is: rho_A,rho_B; the three X and three Y
components; two A diagonal quadrupoles; the three B products sigma_i sigma_j
with i<j; and the B product sigma_1 sigma_2 sigma_3. These account for all
fourteen independent probabilities, so no hidden field is discarded.

For a nonzero spatial wave vector K, define c=|gamma|sqrt(rho_A rho_B/3).
The full directional-current matrix has characteristic polynomial

    lambda^10 [lambda^2-c^2 |K|^2]^2.                     (6)

If gamma!=0 it has rank4 and is diagonalizable: two positive and two negative
wave eigenvalues, with ten zero modes. Within X,Y the zero modes are their
two longitudinal components; the other eight are the remaining conserved
fields. Divergence of each vector in (5) is constant in time. Thus the
subspace div X=div Y=0 is preserved by this LINEAR equation. No microscopic
Gauss constraint is imposed by the generator.

After normalizing X by sqrt(rho_A/3) and Y by sqrt(rho_B), (5) is the
source-free Maxwell curl system with common speed c and the overall sign
of gamma. Equivalently, its transverse sector obeys the wave equation with
two polarizations. The quadratic invariant is proportional to
3|X|^2/rho_A+|Y|^2/rho_B. This normalization is about the fixed background (4).
It is not a derivation of electromagnetic units, charge or photon statistics.

## 3. Microscopic long-wavelength consequence and proof obligations

The already established smooth-profile and stationary finite-mode proofs
use only a fixed finite alphabet, product invariance, finite fixed read
range, a strictly positive nearest-neighbor exchange floor, polynomial
currents and categorical entropy compatibility. All those hypotheses have
been identified above. Changing seven to fifteen states changes constants:
the finite canonical Poincare bound may use 15^M instead of7^M; concentration
has fourteen occupied components; footprint sampling remains four/eight
sites. No estimate uses the specific six-axis alphabet or the acoustic
spectrum. At fixed block size every canonical constant remains finite.

The primary conclusion is therefore that, for the actual process in (4),
on Euler time N L_N and with fixed finite T and fixed nonzero Fourier modes,

    sup_(t<=T) E|Y_N(K,t)-exp[-i A(K)t]Y_N(K,0)|^2 ->0,    (7)

now for all fourteen conserved species, with the supremum outside expectation.
Initial product CLT yields the corresponding finite-mode, finite-time
Gaussian process. Applicability of this alphabet extension and all signs
and multiplicities in (5)-(7) require a separate check before publication.
There are no births in this stationary result.

Let P_L=K K^T/|K|^2 and P_T=I-P_L. The predicted vector autocovariances are

    E[X_K(t) X_K(0)^*]=(rho_A/3)[P_L+cos(c|K|t)P_T],
    E[Y_K(t) Y_K(0)^*]=rho_B[P_L+cos(c|K|t)P_T].           (8)

Here equality denotes the limiting microscopic covariances. If C_K v=K cross v,
the cross covariance is

    E[X_K(t)Y_K(0)^*]
       =i gamma rho_A rho_B/(3c|K|) sin(c|K|t) C_K.       (9)

These expressions retain the static longitudinal fluctuations; replacing
P_L+cos P_T by cos I would incorrectly propagate those modes. There is
no finite-wave-number damping prediction, growing-mode limit or claim of
exact microscopic Maxwell trajectories.
Equation (9) is written for gamma!=0. At gamma=0 all limiting fields are
static and this cross covariance is zero, also obtained by continuous extension.

## 4. Nonlinear and physical scope

Equations (2)-(3) are nonlinear and contain additional moment fields. A
finite-amplitude Maxwell equation does not follow from (5). Changes in the
orbit densities or their shape tensors feed the vector currents. Formation
can change those densities and introduces noise. Charges, coupling to bodies,
Gauss-law preparation, gauge redundancy, relativity and quantization have
not been supplied by this construction.

The additional vector degree of freedom is explicit: two disjoint cubic
orbits of immutable contents. It is not hidden in a variable renamed from
the original six-label acoustic model. The original site-qubit bridge is
still open; a classical process that reads and distinguishes these labels
is not automatically a quantum instrument on a two-dimensional Hilbert space.

The useful research result, if checked, is narrower: positive local Markov
exchange of immutable contents can support a transverse curl sector as a
controlled stationary long-wavelength limit. One must still justify why a
physical theory would choose this alphabet and cross-product potential.
Inverse design of that potential is not a TOE selection principle.

## 5. Prior-art boundary

Lattice recovery of Maxwell equations is established prior art. Mendoza and
Munoz, arXiv0806.2678, and Hanasoge, Succi and Orszag, arXiv1108.2651, provide
relevant lattice-Boltzmann constructions. Their macroscopic field recovery
does not by itself verify the positive immutable-label exchange process
specified here. No novelty claim is made for lattice Maxwell equations,
two transverse polarizations, entropy symmetrization, or the curl system.
Source inspection and a precise comparison are recorded separately before
any publication packet is prepared.
