# Gauge-covariant permanent records: a finite positive construction and a truncation test

Date: 2026-09-22. Status: author conditional constructions and exact controls;
independent check pending. This note supplies gauge fields and dynamics. It
does not identify those fields with the framework's native site algebra or
derive a physical gauge symmetry from the minimal axioms.

## 1. Why couple the movement to a field?

The earlier occupation model allows any neighboring record and vacancy to
exchange their complete internal states. An electromagnetic interpretation
needs more: moving charge must also change the local electric field while
preserving Gauss's law. That requirement changes the allowed hopping blocks.
It is therefore a new hypothesis test, not an automatic application of the
earlier completion theorem.

Finite quantum-link descriptions and gauge-covariant matter couplings are
established constructions. For context, the model and Gauss generators in
Osborne et al., *Large-scale 2+1D U(1) gauge theory with dynamical matter in a
cold-atom quantum simulator*, Communications Physics 8, 273 (2025), equations
1-2, were read at https://www.nature.com/articles/s42005-025-02144-8 . Their
staggered matter Hamiltonian and proposed simulator are not being imported
as this model or as a proof of a photon phase. The local identities below
are checked directly for the different permanent-record instruments stated.

## 2. A supplied spin-half U(1) link model

At each matter vertex use orthogonal states |0>, |+>, |->, with

    Q_x = |+><+| - |-><-|,   n_x = |+><+| + |-><-|,
    a^dagger_(x,+) = |+><0|, a^dagger_(x,-) = |-><0|.

Each oriented link e=(x,y) carries a separate spin-half field space with
E_e = diag(-1/2,1/2) and U_e = |+1/2><-1/2|. Define

    G_x = sum_outgoing E_e - sum_incoming E_e - Q_x.

The zero-Gauss sector is physical for this supplied model. Both charge species
are permanent records: hopping moves their entire states, births add one of
each, and no annihilation channel is included. The link-local operators are

    H_e/kappa = a_(x,+) U_e^dagger a^dagger_(y,+)
                + a_(x,-) U_e a^dagger_(y,-) + h.c.,
    J_(e,+) = sqrt(beta) a^dagger_(x,+) U_e a^dagger_(y,-),
    J_(e,-) = sqrt(beta) a^dagger_(x,-) U_e^dagger a^dagger_(y,+).

For example a positive record moving x -> y lowers Q_x and raises Q_y, so
the link field must fall by one. Pair birth with positive charge at x raises
both Q_x and the oriented electric field by one. These signs ensure

    [G_v,H_e] = [G_v,J_(e,+)] = [G_v,J_(e,-)] = 0

for every vertex v. Monitoring sqrt(d_x)n_x or diagonal electric-field
monitoring also commutes with Gauss's law. The hopping Hamiltonian conserves
each species count. Every birth raises each species count by one. Its total
loss operator, summing both charge orientations, is

    J_(e,+)^dagger J_(e,+) + J_(e,-)^dagger J_(e,-)
       = beta |00><00|_(x,y) tensor I_e,

because U^dagger U + U U^dagger = I on a spin-half link. Thus every pair of
vacancies is eligible, with the field determining which charge orientation
can be born. Opposite-charge records never annihilate in this generator.

For each plaquette one may also add the usual closed-loop product of U and
U^dagger plus its adjoint. Its field changes cancel at each vertex, so it
commutes with every G_v and every n_v. Diagonal electric/charge energies also
preserve these operators. All of these are supplied Hamiltonian terms.

`gauge_record_local_algebra_check.py` verifies the complete 18-dimensional
two-vertex/one-link commutators, count identities and birth loss identity over
exact rational matrices. It also verifies that U is not unitary. The latter
fact matters: a saturated link can block a record hop altogether. The
ordinary occupation model's unitary identification between two neighboring
occupation blocks is absent.

The companion `U1_EXTREME_FLUX_RECORD_TRAPPING.md` gives an explicit reachable
trapping construction in this model, including the elementary plaquette
Hamiltonian. It is an actual restriction of this specified finite-field
model, not a no-go against gauge-covariant record dynamics in general.

## 3. A finite Z2 gauge field with an invertible shift

Here is a different supplied model in which the movement/formation theorem
does survive an exact local gauge constraint. It is a Z2 gauge theory, not
an approximation that has already been proved to contain a U(1) photon.

At each vertex use a vacancy/occupied qubit, with n_x=|1><1| and
a_x^dagger=|1><0|. At every edge use a gauge qubit with Pauli X_e,Z_e. Define

    G_x = (-1)^n_x product_(e incident to x) Z_e,

and take G_x=+1 at every vertex. On a connected graph the product of these
constraints fixes the total occupied-record parity to be even. For an even
number V of vertices this is the even-vacancy sector needed for completion.

Supply nonzero coherent hopping on every graph edge, positive occupation
monitoring at every vertex, and pair birth on any nonempty edge subset:

    H_hop = sum_e kappa_e (a_x^dagger X_e a_y + h.c.),
    D_x = sqrt(d_x) n_x,
    J_e = sqrt(beta_e) a_x^dagger X_e a_y^dagger.

Every hop and birth anticommutes with the matter parity and the incident link
parity at each endpoint twice, so it commutes with all G_x. Every birth adds
two records and J_e^dagger J_e = beta_e q_x q_y because X_e is unitary.
One can add any Hermitian H_0 that preserves every occupation pattern and
the Gauss constraints, including electric Z terms and closed magnetic X loops.

For a fixed allowed occupation pattern, the link parity equations have
2^(E-V+1) solutions on a connected graph. To see this, choose a spanning
tree, freely choose its E-V+1 non-tree edge bits, and successively determine
the tree bits from leaf constraints. The final constraint holds precisely
because total occupied parity is even. Their spans define the same finite
block dimension for every allowed occupation pattern.

A neighboring record/vacancy exchange maps one such block bijectively to
the other by X_e. This map is unitary and transports the Gauss constraint
with the record. Thus the proof in
`OCCUPATION_MONITORING_AND_PAIR_BIRTH_COMPLETION.md` applies to these blocks,
even though the physical Hilbert space does not factor into independent
site-content spaces after imposing Gauss's law:

1. Monotone vacancy count forces any stationary state to have zero weight
   on every configuration with vacancies at a birth-source edge.
2. The Hilbert-Schmidt dephasing identity makes a stationary state block
   diagonal in the occupation pattern.
3. The off-diagonal Hamiltonian commutator equates neighboring blocks by
   the invertible map X_e and therefore equates their traces.
4. Connectedness of the exclusion configuration graph makes those weights
   equal within each vacancy-number sector. A positive source edge forces
   every nonfull even sector to vanish.
5. Finite dimension, absorbing full occupation and the Cesaro/semigroup
   argument give convergence, an exponential tail for each fixed model,
   and a finite mean. No size-uniform bound is supplied.

Arbitrary initial matter-field entanglement within the physical sector is
allowed. After filling, the gauge state can keep evolving under H_0; no
unique stationary gauge state is claimed. For coherences between vacancy
numbers, the counted completion distribution uses the initial Q measurement
convention described in the earlier theorem, which leaves occupation
probabilities unchanged.

## 4. Exact finite control and interpretation

The checker builds the full zero-Gauss sector for a four-cycle. It has
dimension 16: each of the eight even occupation patterns has a two-dimensional
gauge block. With hopping, birth and monitoring coefficients one, a magnetic
loop coefficient 2/3 and electric coefficient 1/7, the transient Hilbert space
has dimension 14. Its complete 196-dimensional trace-decreasing Liouvillian
has exact rank 196 over the Gaussian rationals. This supports the analytic
finite-graph argument without suppressing gauge coherences or magnetic terms.
It is one finite control, not a thermodynamic phase calculation.

The positive Z2 construction and the spin-half U(1) test separate two issues:
local charge-field conservation itself is compatible with permanent creation
and site reuse, while a particular field truncation can impose additional
kinetic constraints. Replacing a bounded raising operator with a cyclic
unitary shift also changes the gauge theory. It cannot be used to claim that
a U(1) obstruction has been repaired while preserving U(1) physics.

No result here derives gauge fields, qubit placement, the Born rule, time,
Lorentz symmetry, a gapless photon, gravity, or the Standard Model from the
framework. The matter and link spaces are additional explicit model data.
The conditional construction is a test of compatibility and of which
assumptions a future native realization must actually supply.

