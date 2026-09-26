# Paired immutable records: nearest-neighbor formation and a dimer Gauss readout

Status: proposed supplied classical process, with conditional elementary
identities below. Not an axiom-derived model, a quantum instrument, a Coulomb
phase theorem, a wave derivation, or formal retained science. Root authored
2026-09-21 during the second twelve-hour campaign. Independent review pending.

## Purpose and declared choices

The earlier four-record loop birth read sites at distance two when computing
its conditional formation odds at one site. This construction changes both
the record encoding and field readout. It supplies a simpler nearest-neighbor
birth law and an exact constrained field, then exposes the remaining state
selection and dynamical questions instead of importing their answers.

Work on Z^3, or an even periodic side N>=4 when discussing the staggered field.
A site is empty or carries one record with fixed content d in
D={+/-e_1,+/-e_2,+/-e_3}. A record also has a permanent identity used only for
tracking; rates do not inspect identities. The six contents can be associated
with six Bloch directions as a menu choice, but this does not make six
orthogonal states on a qubit or supply any qubit operation. The stochastic
configuration space here is classical. There is no independent link degree
of freedom: link occupancy below is read from the site records.

Admissible occupied configurations obey the reciprocal relation

    eta(x)=d  =>  eta(x+d)=-d.                                  (1)

Thus occupied sites form a nearest-neighbor matching. Every occupied site
has exactly one partner and every empty site has none. This is a fixed
nearest-neighbor support relation, covariant under translations and proper
cubic rotations. The record-direction menu, simultaneous event rules and
positive constants beta,kappa,nu are supplied choices, not consequences of
that covariance or of the framework axioms. The prior September 3 glued-group
note already illustrates the difference between single-record and block
motion. The new content here is the joint birth/immutable-motion model and
its particular matching-field bridge, not invention of block transport.

## One joint event process

**Paired birth.** Each undirected nearest-neighbor edge {x,x+d} whose ends
are empty creates two new records, with contents d at x and -d at x+d,
at rate beta. Both identities persist thereafter. Birth is atomic, involving
two sites. No one-site birth, record deletion, or content rotation is used.

**Dimer translation.** Each occupied pair {x,x+d} attempts each displacement
a in D at rate kappa. Move both records by a simultaneously if every new
site outside the old pair is empty. Their contents and identities are
unchanged. Parallel shifts involve three sites, transverse shifts four.
The inverse shift is admissible and has the same rate.

**Full-cube exchange.** Choose a unit cube and one of its three pairs of
opposite faces. If one face contains two dimers parallel to one of its axes
and the opposite face contains two dimers parallel to the other face axis,
swap the four pairs of facing sites at rate nu. All eight records move one
nearest-neighbor step along the remaining axis. The two face patterns are
exchanged; every content and identity is preserved. The same event is its
own inverse. Include all translated cubes and all three axis choices, with
one channel per cube and axis, not an arbitrary orientation-dependent rate.

Each event preserves (1) and capacity. On a finite torus these bounded local
rates define a finite-state continuous-time chain for the contents; record
identities can be carried along its finitely many births. No infinite-volume
existence or scaling theorem is needed for the statements proved here.

An explicit renewal history starts empty: birth the x-oriented pair at
(0,0,0),(1,0,0), translate it by e_2, then birth a second x-oriented pair on
the original edge. The first two records survive at (0,1,0),(1,1,0), with
unchanged identities and contents. The original sites have formed again.
Each step has positive rate. Arbitrarily many renewals at a fixed site need
a separate space/time construction; this three-event witness asserts two.

A dense-motion witness is the described cube with two x dimers on z=0 and
two y dimers on z=1. Four births from empty prepare it. A full-cube exchange
moves all eight records while preserving full occupancy in that cube. It
does not imply that every fully occupied matching is mobile: a fully packed
columnar state using only x dimers has no cube exchange or translation.

## Exact nearest-neighbor formation odds, and their scope

Let v(y) indicate vacancy just before an event. At a vacant site x the hazard
of forming content d and the total hazard are

    h_d(x,eta)=beta v(x+d),   h(x,eta)=beta sum_{a in D} v(x+a).

When h>0, conditioning on a birth at x gives exactly

    P(d | birth at x, eta before birth)=v(x+d)/sum_a v(x+a).    (2)

This varies with, and only uses, the six nearest-neighbor vacancy conditions.
At h=0 no birth occurs; no conditional law on that probability-zero event
is claimed. Distinct sites' events are compatible because they come from
the single edge-clock generator, including the correlations of simultaneous
pair creation. The resulting event law is not independent site sampling.

Equation (2) is a **pre-event conditional formation law**. It is not a DLR
one-site conditional distribution of a stationary matching measure. In such
a measure, conditioning on all other sites fixes whether a neighbor points
into x; a one-site edit cannot create an entire dimer. Thus (1) and (2) do
not by themselves prove that every intended interpretation of the framework's
sitewise admissibility/probability axiom is satisfied. No axiomatic closure
is inferred from the shared phrase 'nearest-neighbor.'

Initially, in the empty state, each site has six independent incident birth
channels. If rho(t) is its translation-invariant occupied density, then
rho'(0)=6 beta. More generally on a finite torus, with V_vac the vacancy
count and E_00 the number of empty-empty edges, the generator gives

    L V_vac = -2 beta E_00.                                  (3)

Conservative moves do not change this count. Equation (3) supplies neither
a uniform birth hazard at each vacancy nor guaranteed eventual full packing:
isolated vacancies have zero instantaneous birth hazard. Its time integral
bounds the expected total births by the initial vacancy capacity globally;
local renewal does not create extra total capacity.

## Matching flux and exact discrete Gauss identity

For a positive coordinate edge define n_i(x)=1 when its ends are paired,
and zero otherwise. Fix sigma_x=(-1)^(x_1+x_2+x_3) and define the derived link
field

    B_i(x)=sigma_x [n_i(x)-1/6].                              (4)

Use the backward divergence div B(x)=sum_i[B_i(x)-B_i(x-e_i)].
Since sigma_(x-e_i)=-sigma_x, and the number of incident matched edges is
the occupied-site indicator o(x),

    div B(x)=sigma_x [sum_i(n_i(x)+n_i(x-e_i))-1]
            =sigma_x[o(x)-1] = -sigma_x v(x).                 (5)

This identity holds for every matching, not only equilibrium samples.
At full packing it is exactly source-free. Vacancies carry formal charges
of opposite sign on the two sublattices; a pair birth removes an adjacent
opposite-charge pair. Empty initial space has a staggered charge background,
so this construction does not maintain zero microscopic charge during
formation. Neither (4) nor these formal charges have yet been identified
with physical electromagnetic observables.

This is the standard bipartite dimer gauge readout, not a new gauge mapping:
Huse, Krauth, Moessner and Sondhi, arXiv:cond-mat/0305318v3, Eq.(1), introduce
the corresponding staggered link field and identify monomers as charges.
Their cubic-dimer Coulomb description is an effective statistical ansatz
supported by simulations of their sampling scheme. It is not a theorem that
this record process, its count sectors, or its formation limit has that law.
Source: https://arxiv.org/html/cond-mat/0305318v3 .

The parity sign in (4) is a readout convention, not an event-rate input or
a privileged origin in the process. Changing the bipartite convention flips
B and charge together. A unit translation, expressed with the same fixed
sigma convention, also flips the translated field's sign. Even field
correlations respect this convention; a physical transformation assignment
for the field remains an explicit bridge. Even periodic N is necessary for
this global convention; no such claim is made on an odd torus.

## A local curl increment implemented by immutable transport

For the cube witness, put its lower corner at zero, with x dimers on z=0
before and y dimers there after. Its upper face has the opposite change.
For the Fourier convention sum_x exp(-ik.x) B_i(x), direct edge accounting
gives the exact unnormalized increment

    Delta B_hat(k)=(1+exp(-ik_z))
          [(exp(-ik_y)-1)e_x+(1-exp(-ik_x))e_y].              (6)

Its backward-divergence symbol dot product is exactly zero:
(1-exp(-ik_x)) Delta B_x+(1-exp(-ik_y)) Delta B_y=0.
At small k, (6) equals 2i(k_x e_y-k_y e_x)+O(|k|^2).
Thus the paired face exchanges have a first-order curl-shaped field
increment, despite exact conservation of every record-direction count.
They are not single plaquette flips that rotate x records into y records.
The staggered sign is why the two faces add rather than cancel at leading
order. An increment of order |k| is a mobility statement; it is not a wave
frequency, a continuum equation, or a dispersion relation.

At full packing every such local cube event preserves winding flux. With
vacancies, the Gauss charges can move and this preservation is not asserted.
The zero Fourier increment of (6) follows directly, without assuming a
particular equilibrium ensemble.

## State and wave obligations still open

With births off, each transport channel has a reverse of equal rate. Hence
the uniform law on any finite closed connected component is reversible.
Uniform matching laws conditioned on preserved counts, and mixtures of
these components, are also invariant. This stationarity argument does not
establish irreducibility. Weighting a matching by z^(number of dimers) gives
another mixture invariant under the conservative part only; positive births
invalidate stationarity of that finite-volume mixture.

The actual specified conservative generator is symmetric in these measures,
so its finite-state eigenvalues are real and nonpositive. It supplies no
oscillatory eigenmodes there. The exact local curl increment does not change
that conclusion. A different nonreversible or coherent dynamics would be
additional model content requiring construction and checking, including
record-content preservation and the state-selection problem.

The immediate decisions are therefore to test accessibility and long-scale
correlations of the actual matching process, and to identify which admissible
modification could carry a reversible transverse sector. Replacing its moves
by an ordinary dimer sampler or importing a quantum dimer Hamiltonian would
answer a different question. In particular, an orthogonal local matching
basis is not automatically the framework's M_2 qubit carrier.

## Evidence plan

The author runner will check all 64 nearest-neighbor vacancy patterns with
valid surrounding matchings, all 24 proper cubic rotations, identity-preserving
birth/translation/renewal histories, the actual dense cube exchange and its
inverse, (5) on finite matchings, and the exact polynomial Fourier identity
(6). A stationary finite-state check will keep its move support explicit.
Mutation controls must reject no-motion 'transports', unchanged cube moves,
and a missing staggered sign. These are finite controls alongside the
written identities, not evidence of a phase or an emergent wave law.

## Exact reflecting-cube diagnostic

A separate reflecting unit cube permits only the events whose full support
lies in its eight sites. It is not the N>=4 periodic process. There are
108 matchings, with dimer-count census (1,12,42,44,9) for counts 0 through 4.
The conservative generator is exactly symmetric. With beta=kappa=nu=1,
the full birth/transport generator has 91 transient states and 14 closed
components: eleven singleton components and three two-state components.
Eight of those singleton states have three dimers and two opposite-corner
vacancies. Their remaining six sites form alternating dimers on a hexagon.
No allowed reflecting translation, cube exchange or paired birth leaves any
of those states. The other closed states are fully packed.

The exact finite rational absorbing equations give total empty-start
probability **4/21** of ending in one of the unfilled components. The runner
constructs every matching and channel, solves Q_T H=-R for the closed-class
hitting probabilities, and checks the exact equation, positivity and unit
row sums. This is a finite certificate for the reflecting cube, not an
asymptotic estimate or a periodic-lattice jamming claim. It exposes a missing
accessibility premise in any unconditional full-packing argument. Allowing
surrounding sites changes the move graph and needs a new calculation.
