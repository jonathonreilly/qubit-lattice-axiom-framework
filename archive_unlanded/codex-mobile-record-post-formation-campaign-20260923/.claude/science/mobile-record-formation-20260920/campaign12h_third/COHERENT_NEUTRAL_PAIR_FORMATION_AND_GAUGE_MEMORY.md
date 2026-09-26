# Coherent neutral-pair formation can retain a gauge-loop phase

Date: 2026-09-22. Status: author conditional channel classification and exact
finite preparation. Independent scrutiny is pending. This specifies a quantum
formation instrument; the framework axioms do not select it.

## 1. The same formation loss admits different quantum instruments

Use the qutrit matter and spin-half U(1) link spaces defined in
GAUGE_COVARIANT_PERMANENT_RECORD_DYNAMICS.md. Suppress the rate and put

    V_+ = a_x,+^dagger U_e a_y,-^dagger,
    V_- = a_x,-^dagger U_e^dagger a_y,+^dagger,
    P = |00><00|_(x,y) tensor I_e.

Both maps commute with the local Gauss generators and create one record of
each charge. Their input supports are the two different electric-field
values, and their outputs are orthogonal matter/field configurations. Hence

    V_+^dagger V_- = V_-^dagger V_+ = 0,
    V_+^dagger V_+ + V_-^dagger V_- = P.

The previous choice used two separate environment channels sqrt(beta)V_+
and sqrt(beta)V_-. A different allowed local choice is one coherent channel

    J = sqrt(beta)(V_+ + V_-).

Its loss J^dagger J is also beta P. It preserves the same Gauss law, creates
the same charge counts and annihilates every state with an occupied endpoint.
On the vacant matter/field subspace V=V_++V_- is an isometry. It transports
an input field phase into the joint newly occupied matter/field state.

The distinction is physical: adding Kraus operators before forming their
dissipator is different from summing their separate dissipators. A jump
environment that records only that a pair formed need not record which charge
occupies which endpoint. The two newborn contents can be fixed as one plus
and one minus while their spatial assignment remains coherent in this supplied
quantum interpretation.

This does not keep the reduced field state unchanged. Tracing out the new
matter can remove its off-diagonal entries because the matter and field are
entangled. The preserved quantity is joint gauge-invariant information, not
a duplicated unknown quantum state.

## 2. Complete coarse birth-map family on these two transitions

Restrict to local birth Kraus operators of the form

    J_mu = a_mu V_+ + b_mu V_-.

This fixes the charge-pair output and single-link field shift; it allows an
arbitrary independent local environment and any number of its outcomes within
that transition space. It does not classify instruments with additional
matter outputs, nonlocal field changes or initial environment correlations.

The classification by chi below concerns the birth CP map and generator
after summing over mu. If individual mu outcomes are retained as records,
their separate outcome maps are additional instrument data; chi alone does
not classify that refinement. Unitary rotations of a Kraus list preserve
the summed map while changing its individually marked outcomes.

Requiring the same field-independent vacant-edge hazard beta gives

    sum_mu |a_mu|^2 = sum_mu |b_mu|^2 = beta.

Define chi=beta^-1 sum_mu a_mu conjugate(b_mu). Cauchy-Schwarz gives |chi|<=1.
The complete birth part is

    beta [ V_+ rho V_+^dagger + V_- rho V_-^dagger
         + chi V_+ rho V_-^dagger + conjugate(chi) V_- rho V_+^dagger ].

The loss is always -(beta/2){P,rho}. Conversely every |chi|<=1 is attained by

    J_1=sqrt(beta)[V_+ + conjugate(chi)V_-],
    J_2=sqrt(beta)sqrt(1-|chi|^2) V_-.

The associated coefficient Gram matrix has diagonal entries one and
off-diagonal chi,conjugate(chi); its determinant is 1-|chi|^2. This gives
the complete positivity condition directly. In the two-dimensional input
field basis, the normalized birth map is the isometry V after a channel that
multiplies one off-diagonal by chi and the other by its conjugate.

For the explicit reference-edge reversal that swaps x,y and sends E->-E,
V_+ and V_- are exchanged. Covariance under that representation requires
chi=conjugate(chi). Thus a uniform real chi in [-1,1] gives an edge-reversal
covariant choice, including proper cubic rotations when supplied uniformly
on a cubic lattice. This statement uses the indicated basis and symmetry
action; no unstated physical phase convention is selected.

The separate orientation channels have chi=0. The real choices chi=+1 and
chi=-1 each need just one jump channel and retain the input coherence up to
a relative phase. Occupation-only monitoring distinguishes neither charge
orientation when both endpoints are occupied.

## 3. What transfers to the completion arguments

All these instruments have exactly the same positive operator Gamma=sum J^dagger
J, the same creation count and the same absorbing full-occupation subspace.
Therefore the stationary-support proofs in
OCCUPATION_MONITORING_AND_PAIR_BIRTH_COMPLETION.md and the partial-bijection
criterion continue to apply whenever their respective hopping and monitoring
hypotheses hold. If Tr(Gamma rho)=0 for a positive stationary rho, every
J_mu rho vanishes separately for any chi; no orientation-dephasing step is
used in those proofs.

This preserves the stated sufficient completion conclusions, not all
transient histories in every interacting model. Subsequent coherent motion
can turn different retained phases into different populations. The exact
example below has identical complete occupation clocks while its final
joint quantum state depends on chi.

## 4. Complete four-link gauge-loop preparation

Use a four-cycle with cyclic link-reference orientation, four qutrit matter
vertices, and four spin-half links. On the zero-Gauss sector every electric
bit word b=(b_0,...,b_3), b_i in {0,1}, determines

    Q_i=b_i-b_(i-1),  indices modulo four.

All sixteen bit words are valid because Q_i is always 0,+1 or -1. Zero
charge means vacancy in this model. The two uniform field words have no
matter records. Start with the supplied pure gauge-loop state

    |psi_empty>=(|0000>+|1111>)/sqrt(2).

Supply equal beta>0 formation on all four edges with a common real chi.
There is no ordinary hopping in this preparation control. Arbitrary
occupation-monitoring strengths are allowed. Optional pure-field plaquette
and occupied-record-cycle Hamiltonians will commute with the entire
trajectory described below.

The first birth can occur on any edge; its total rate is 4 beta. Its output
has two occupied endpoints. Exactly the opposite edge remains eligible,
with rate beta; its next birth completes occupation. For each first edge,
let rho_e be its normalized one-birth output. It has two equal diagonal
weights and off-diagonal chi/2 between the two possible matter/field branches.
The second birth gives the same density rho_F for every first edge.

In integer bit-mask ordering, the two fully occupied field words are
5 and10, i.e. the alternating words. In their physical matter/field basis,

    rho_F = (1/2) [[1,chi^2],[chi^2,1]].

The complete density at time t is

    rho(t)=p0(t) rho_empty + w(t) sum_(e=0)^3 rho_e + pF(t) rho_F,
    p0(t)=exp(-4 beta t),
    w(t)=[exp(-beta t)-exp(-4 beta t)]/3,
    pF(t)=1-[4 exp(-beta t)-exp(-4 beta t)]/3.

Each rho_e and rho_F has trace one, so p0+4w+pF=1. The mean completion time
is the survival integral

    E[tau]=1/(4 beta)+1/beta=5/(4 beta).

gauge_coherent_pair_birth_check.py constructs the complete sixteen-dimensional
physical density generator and verifies d rho/dt=L(rho) over symbolic beta,
t and real chi, entry by entry. It checks trace, initial condition, final
stationarity, exact Gauss/count identities and the complete local eighteen-
dimensional birth algebra. It does not merely fit a population trajectory.

## 5. A gauge-invariant phase observable and its limits

The full-occupation observable

    X_cycle=|5><10|+|10><5|

acts between states satisfying the same Gauss law. It is the restriction of
the gauge-dressed whole-record circulation: on this alternating-charge
four-cycle, forward and reverse terms both contribute, so
H_cycle=2g X_cycle. It preserves every existing record and exchanges their
locations. The final joint gauge-invariant coherence and purity are

    Tr(X_cycle rho_F)=chi^2,
    Tr(rho_F^2)=(1+chi^4)/2.

For chi=+1 or -1 the final joint state is pure with unit cycle coherence.
For chi=0 it is the equal incoherent mixture, with purity one half and zero
cycle coherence. These states have identical terminal record counts and
the identical completion probability pF(t).

All terms of rho(t) commute with every occupation n_x, so occupation monitoring
does not disturb this trajectory at any strength. The pure-field plaquette
connects only the two uniform empty words; rho_empty is its eigenstate density.
The occupied-record cycle acts only on the full sector, where rho_F commutes
with X_cycle. Thus either Hamiltonian can be included at arbitrary finite
strength without changing the displayed solution. The runner checks both
commutators for the complete symbolic trajectory.

The initial phase is a supplied resource. This construction preserves it
through formation; it does not generate a coherent loop vacuum from an
initial incoherent mixture. A gauge-invariant mathematical observable is also
not yet a native record-only readout prescription. The qubit-per-site encoding,
the formation instrument and its environment, and a long-distance photon
phase remain separate questions. No physical value of chi is predicted.

The first checker run stopped at a structural symbolic equality between
(chi^4+1)/2 and chi^4/2+1/2. The complete density equation had already passed.
The exact expanded difference was zero; the source and full failed logs are
preserved in coherent_pair_birth_exploration/structural_purity_equality.
Changing only that comparison to an expanded-difference check gave a complete
successful run. No physical counterexample was discarded.
