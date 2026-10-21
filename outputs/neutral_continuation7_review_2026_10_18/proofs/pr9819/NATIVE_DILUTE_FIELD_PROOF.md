<!-- Original PR9819 source SHA256 a97534a05f909edbb4570043fc67e8ed5612c2cb9caed3f1979ac5e975afe9be. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Native dilute neutral field: operator algebra and finite-time dynamics

Status: conditional-support; focused independent checks pass. No new
physical qubits, oscillator Hamiltonian or interaction is introduced. The
fixed ten-layer slab, weak coupling, microscopic compass Hamiltonian and
prepared dilute states remain premises. This is a nonrelativistic finite-mode,
fixed-occupation limit, not a relativistic quantum field theory or TOE.

## Target and minimal premises

The earlier fixed-occupation ladder established selected matrix elements for
a different, high-energy large-feature family. It did not prove full-vector
annihilation or CCR. Here use the LOW-energy Q4 neutral endpoint mode of
POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md, its later arbitrary-polynomial-grid
relative-bound extension, and the global-ground/character results. The new
target is an operator limit on finitely many dilute modes, with dynamics and
a field extracted from the original ZZ readout. No canonical bosons are
assumed as microscopic constituents.

N counts broken vertical bonds; Q counts bad column plaquettes. A fixed-order
equivariant normal form has global remainder delta<=C J R^2 lambda^M,
exact N blocks and Q blocks inside N0, and vacuum-subtracted coefficients
bounded by C_j Q. Wall sectors remain order J above the flat energy. The
flat-derived actual global ground can be used in the all-positive sector.
The construction also extends to compatible characters for invariant
observables; no thermal preparation dynamics is needed or claimed here.

## Local cluster algebra

For a translated endpoint motif T_a (two adjacent columns, with orientation
included in a), let S_a be its four toggled plaquettes. Set

    b_a^dagger = X_(T_a) P_(F_a,+),

where the fixed finite footprint F_a contains S_a and a positive-plaquette
buffer. Every nonzero creation adds exactly four bad plaquettes. Its adjoint
removes exactly that syndrome. This complete-syndrome projector is essential:
unrestricted X strings could erase defects and coherently return to vacuum.

For normalized delocalized packets f with ||f||_infinity<=C/R define
B_f^dagger=sum_a f(a)b_a^dagger. On any fixed finite-Q sector these maps have
norm O_m(1), not O(R): an output with 4(m+1) defects has only C_m possible
incoming motif labels, and Cauchy-Schwarz over these incoming histories gives
||B_f^dagger v||^2<=C_m sum_C |v_C|^2 sum_(eligible a)|f(a)|^2.

In the ideal symmetric tensor product, pairs of motifs have incompatible
footprints with probability O_m(R^-2). On the compatible configurations the
physical motif states give an exact isometry and creation/removal agree with
the usual symmetric tensor operations. Bounded history multiplicity controls
coherent bad configurations, whose norm is O_m(R^-1). Consequently both the
Fock Gram matrix and the FULL VECTOR lowering identities have errors
O_m(R^-1), as do

    [B_f,B_g^dagger] = <f,g>,   [B_f,B_g]=0,

on the prepared finite-particle span. These are not whole-Hilbert-space
operator identities. See INDEPENDENT_CLUSTER_FOCK_ALGEBRA.md for the explicit
counting proof and its hypotheses.

## From motifs to the native bound mode

At any fixed final order M the single-Q4 reductions produce a localized
finite-order basis with two endpoint orientations. Each retained coefficient
is a finite sum of local paths and diagonal denominators. Truncating after
that fixed order gives a finite list of four-defect patterns, with support
and constants independent of R. Corrections to the endpoint vectors begin
at O(lambda^2). Their Gram matrix is identity plus finite-range small terms;
a fixed-order inverse-square-root expansion orthonormalizes it to the same
remainder order. This does not require convergence of an infinite series.

For clarity, a retained internal transition is realized by projecting onto
its complete source syndrome in a positive buffer, applying its physical
column-X word and diagonal phase, and projecting onto its target syndrome.
Both syndromes have four defects. Pairing with its adjoint realizes the
required Hermitian or anti-Hermitian local transition. The incompatibility
buffer includes every retained Hamiltonian support, pattern and
Gram-correction path, as well as one further retained local action. Retain
BOTH endpoint orientations locally; the small lambda^14 orientation gap is
not inverted to manufacture a local one-orientation transform.

Each of these corrected local patterns can be extended to a creation
operator by its complete-syndrome positive projector. Its fixed finite
pattern list preserves the history and norm bounds above. Finite-order
orthonormalization gives the corresponding one-particle Gram bounds. On
well-separated features, every local vacuum-subtracted Hamiltonian term
acts on at most one feature. Terms touching multiple features are confined
to the same fixed incompatibility relation. Their action on delocalized
fixed-m products has norm at most C_m J lambda^4/R: coefficients start at
lambda^4, collision-vector norm is O_m(1/R), and local predecessor counts
are bounded at fixed Q. Disconnected vacuum terms are absent by the
relative-bound construction, not discarded by an extensive norm estimate.

Let h_M(q) be the native two-orientation single-feature matrix including ALL
common diagonal corrections through the chosen order. Diagonalize it at
each of a fixed finite set of distinct momenta q_j, and take its lower
branch. This is a mode choice after deriving the matrix. At |q_j|~lambda^s,
s>1, its orientation vector is (A+B)/sqrt(2)+O(lambda^(2s-2)+lambda^2).
The single-particle dispersion relative to q=0 is

    epsilon(q)-epsilon(0)
      = J(kappa/2) lambda^12 |q|^2
        + O(J lambda^14 |q|^2 + J lambda^10 |q|^4)
        + O(J R^2 lambda^M).

Here kappa=4gamma^2/v, gamma=12155/33554432, v=45/16384, all inherited
microscopic coefficients. The rest energy epsilon(0) is kept; it is not
replaced by its leading order over the long time below.

For a fixed finite maximum occupation m_max and fixed number of modes, let
W map normalized symmetric occupation vectors to these physical products,
apply their finite Gram correction, and undo the normal-form dressing.
The resulting isometry obeys, on this finite space,

    ||(H-E_g)W - W dGamma(epsilon)||
        <= C_m J [lambda^4/R + R^2 lambda^M].                 (1)

The same local counting applies to linear combinations in this fixed space.
The actual-ground replacement uses ONE common near-identity rotation after
constructing W, not repeated bare creation on a slightly changed vacuum.
Let v be the dressed flat vector and g the exact ground, phased so
v=c g+s h with h orthogonal to g. The inherited gap bound gives
s=O(R^2 lambda^(M-4)); the residual gives ||(H-E_g)v||=O(delta), hence
||(H-E_g)h||=O(delta/s). The rotation V in span(g,h) sending v to g
has ||V-I||=O(s) and ||[H,V]||=O(delta): its off-diagonal coefficients
are O(s), and its diagonal changes O(s^2). This avoids both an extensive
||H|| bound and amplification by repeated global creation operators.
Apply V once to the whole embedding. Its dynamical error is O(delta).
If needed project each occupation sector into its exact Q-cluster and
repeat its finite Gram correction; the normal-form band separation gives
O(delta/(Jlambda^4)) state errors and O(delta) residual errors. The
contact term stays inside fixed Q and is not charged to this projection.

## A resolved native time window

Choose s=2, R~lambda^-14, and final remainder order M=80. Select allowed
momenta q_j such that q_j/lambda^2 tends to fixed distinct k_j. Rounding is
O(1/R) and negligible. Set tau=J lambda^16 t and remove the common rest
phase epsilon(0) times occupation. Equation (1) and Duhamel give contact
error O_m(lambda^2) and global-tail error O_m(lambda^36), uniformly for
bounded tau. The dispersion errors are O(lambda^2) on this time scale.
Thus the prepared finite-mode dynamics converges to

    dGamma( (kappa/2)|k|^2 ).                                (2)

This is a derived nonrelativistic scalar dispersion. The packets are very
dilute extended modes: their carrier wavelength is lambda^-2 while the box
is lambda^-14. This does not describe finite density, localized collisions,
or propagation across the box on its much longer crossing time.

## Field from the original readout, not an added oscillator

Let C_q be the original normalized two-step vertical ZZ readout. For each
fixed m, let P_m be the EXACT microscopic spectral cluster corresponding
to N0,Q=4m. Such clusters exist for small lambda: their leading centers are
m J Delta lambda^4, Delta=L/16, their fixed-m widths are O_m(Jlambda^6),
neighboring integer-Q bands are separated by order Jlambda^4, and all wall
sectors are order J away. Global remainder perturbation changes their
projectors by O(R^2 lambda^(M-4)). These are energy projectors, not a new
interaction or an assumed conserved particle number.

Choose the phase of the lower mode so its vacuum source amplitude is
positive. With g=sqrt(2/L) gamma beta, beta=165/17, define the spectrally
raising part of the ORIGINAL operator

    A_q^dagger = (g lambda^10)^-1 sum_m P_(m+1) C_q P_m,
    A_q = (A_q^dagger)^dagger.                              (3)

Keep two extra occupation levels when testing all commutators (one extra
level suffices only for a mixed raising/lowering commutator). The extracted
field is nonlocal through energy filtering; implementation of this
measurement is not derived. The unfiltered C_q has much larger high-energy
response and is NOT claimed to be a closed scalar field.

In the N0 effective algebra, all Q-changing terms require column windings;
the leading Q+4 part of C_q is the derived endpoint source at lambda^10.
More explicitly, the N0 source through orders below ten is diagonal in
column Z. Its first nonconstant term is order four. The first Q-changing
Hamiltonian is winding order ten, so the Q-normal-form generator starts at
order six; commuting it with the order-four source contributes at order
ten and is already included in g. Its commutator with the scalar lower
source terms vanishes. Thus the charge reduction introduces no earlier
raising term. This is the same vacuum-rotation subtraction used in the
single-pole source proof.
Terms missing all existing defects create that same four-defect motif;
terms meeting an existing defect have only O_m(1) allowed centers and,
after Fourier normalization, norm O_m(1/R). Their exceptional finite-pattern matrix has BOTH bounded outgoing and
incoming degree at fixed Q: the center lies near an initial bad plaquette;
for the inverse local change it lies near a final bad plaquette. Schur's
bound therefore gives O_m(1/R), not a bound based on only one degree. Higher creation coefficients give
relative O(lambda^2); the lower/upper orientation mismatch is
O(lambda^(2s-2)). Lower-order diagonal terms cannot connect Q to Q+4.
This proves a UNIFORM O_m(1) norm for (3) between finite-Q clusters, as
well as the full-vector relations

    A_(q_j)^dagger W = W a_j^dagger + O_m(lambda^2+R^-1),
    A_(q_j) W = W a_j + O_m(lambda^2+R^-1),                 (4)

up to projector/remainder errors bounded conservatively by
O(R^3 lambda^(M-14)). At the displayed scales this is O(lambda^24).
The uniform finite-sector norm, rather than the global bound R/lambda^10,
allows composition of (4). Therefore [A_i,A_j^dagger]W=delta_ij W+o(1)
and the same-sign commutators vanish on the fixed prepared occupation
space away from its artificial top cutoff.

Equations (2)-(4) derive a dilute bosonic scalar operator sector and its
readout normalization from one-qubit spins. The symbols a_j only label
the limiting symmetric tensor space; they were not added to H.

## Remaining assumptions and prior-art boundary

The Hamiltonian, small lambda, fixed height, state/packet preparation,
finite occupation and measurement filtering remain conditional. No
fermionic statistics, Lorentz cone, measured gravitational coupling,
cosmological state, finite density or full CCR at finite volume follows.
No observation was fitted or independently tested.

Lattice Haag-Ruelle theory already constructs bosonic scattering spaces
under its own infinite-volume gap and particle-spectrum hypotheses:
Bachmann, Dybalski and Naaijkens, https://arxiv.org/abs/1412.2970.
That is prior-art context, not a theorem applied here: the present argument
uses a finite-volume joint limit and does not assert its fixed-coupling
infinite-volume hypotheses. The new content is the conditional native
mode/readout realization and explicit scale window for this Hamiltonian.

## Reproducible checks and numerical limits

The exact sparse motif control includes both orientations and a two-step
positive buffer, at R=10,14,18. For two identical uniform modes its squared
norm is exactly 2-99/R^2 and its full lowering deficit is 99/R^2; independent
excluded-center counting reproduces 99. The finite R18 deficit is still
0.30556, so these small grids are not near the dilute limit. Cross-mode
controls preserve their similarly substantial finite-size errors.
The separate 70-digit two-orientation matrix check resolves q=lambda^2 k
and the predicted scaled dispersion. It evaluates derived coefficients,
not the enormous R=lambda^-14 physical Hamiltonian. No practical numerical
threshold for the analytic remainder constants is claimed.

Independent cluster algebra, dynamics, source and final checks pass after
explicit source-order, ground-rotation and buffer clarifications. No formal
audit verdict is applied. The gap and locality proofs remain analytic inputs;
the scripts do not certify them by finite-size extrapolation.
