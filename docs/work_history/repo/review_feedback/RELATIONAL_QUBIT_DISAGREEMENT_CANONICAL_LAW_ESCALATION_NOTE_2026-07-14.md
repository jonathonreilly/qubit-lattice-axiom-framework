# Relational Qubit Disagreement And Canonical-Law Escalation

**Date:** 2026-07-14

**Type:** meta

**Authority:** none. This is an exploratory exact reduction and bounded
selection probe. It is not an axiom proposal, primitive, retained theorem,
audit verdict, premise registration, or canonical-law choice. It changes no
axiom, registry, primitive, audit, review queue, or retained surface.

## Framework And Input Surfaces

This cycle retains the full exercise refresher already completed for the
preceding cycles: the current four axioms and Qualification in
[`MINIMAL_AXIOMS_2026-06-29.md`](../../../MINIMAL_AXIOMS_2026-06-29.md), the
complete approved-premise registry and three primitive source notes, the
controlled vocabulary, and the review/no-go authority boundaries. Its direct
research inputs are the bounded selector result in
[`FIRST_PRINCIPLES_LAW_SELECTION_TOURNAMENT_NOTE_2026-07-14.md`](FIRST_PRINCIPLES_LAW_SELECTION_TOURNAMENT_NOTE_2026-07-14.md),
the required-field schema in
[`CANONICAL_LAW_COMPLETENESS_CONTRACT_NOTE_2026-07-13.md`](CANONICAL_LAW_COMPLETENESS_CONTRACT_NOTE_2026-07-13.md),
and the pair-generator classification in
[`QUBIT_SYMMETRY_EXCHANGE_LAW_REDUCTION_PROBE_NOTE_2026-07-14.md`](QUBIT_SYMMETRY_EXCHANGE_LAW_REDUCTION_PROBE_NOTE_2026-07-14.md).

Those notes are exploratory inputs, not retained authority. Every algebraic
claim newly used below is rerun in the companion rather than inherited by
status.

## Question

The preceding tournament found one honest nontrivial winner in a small
permanent-record rule class:

```text
permanence
+ spatial and record-label symmetry
+ finite causal confluence
+ minimum positive trigger support
+ minimum disagreement with the triggering records
    -> copy the two equal records into the open center.
```

Can that last principle be lifted to the actual one-site `M_2(C)` possibility
domain, made relational under qubit-frame change, and then extended with the
fewest further representation-invariant principles into one complete law that
also supplies coherent Bell contexts, formation and actuality, record-only
state, renewal, chirality and matter, a clock, and resource/Green gravity?

This cycle actively seeks a positive unique winner. It does not assume that a
trivial or incomplete answer is inevitable.

## Result In Plain Language

There is a clean quantum version of “copy what the two equal neighbors say.”
If both neighbors carry the same rank-one projector `P`, and a new record is
already required to choose a rank-one projector `Q`, then all four natural
disagreement measures tested here give the same unique answer:

```text
Q = P.
```

Projector overlap, infidelity, squared Hilbert-Schmidt distance, and a
full-rank-regularized relative entropy all order the candidates in exactly the
same way. The equivalent relational exchange energy is ferromagnetic SWAP.
Under common `SU(2)` frame covariance, every two-qubit pair Hamiltonian is,
up to a scalar, a multiple of SWAP. Quotienting a positive clock rescaling and
a scalar energy shift leaves precisely two nonzero orientations. Minimum
disagreement selects the alignment orientation rather than its antialignment
opposite. This is a real, representation-invariant reduction.

It is not yet a formation law. The score is conditional on there being a
write. A no-write candidate has no disagreement and ties the aligned write.
Adding a positive cost for an eligible trigger that remains unwritten makes
the aligned write unique, but that cost is the occurrence principle that was
missing. Reversing its sign selects no write. Also, a coherent universal map
that takes two copies of an arbitrary unknown qubit and leaves three perfect
copies cannot implement the rule: it would change inner products. The rule
can copy orthogonal record alternatives in a supplied context, or can be an
event instrument, but it cannot be an unqualified nonlinear qubit copier.

The escalation does produce two valuable positive bridges:

1. Exchange at dimensionless angle `pi/4` is Bell-capable.
2. The same quadratic “neighbor disagreement” shape becomes a discrete
   Dirichlet action. Once a source and a zero-mode/boundary prescription are
   supplied, its unique minimizer is an exact finite Green response.

Neither bridge fills the intermediate fields. The exchange angle, relational
measurement programs, physical event instrument, one realized event, phase
scope of records, fresh-capacity policy, relativistic matter carrier,
chirality, metric rate, resource source, universal coupling, and tensor/nonlinear
gravity remain separate physical entries. For each entry the probe constructs
an opposite or tied competitor that preserves everything fixed before it.

A complete winner can be made unique by putting one score term or hard
constraint in for every field. The term-deletion runner verifies that each
such entry removes exactly its own two-way residual. At that point, however,
the cost has become the law. It is no longer a derivation of the complete law
from the original one-line disagreement principle.

This is not a no-go against a deeper unification. One dimensionless invariant
action could still derive all the terms and have one nontrivial global
minimizer/history. No such action is constructed or excluded here.

## 1. Exact Relational Disagreement Functional

Let `P` and `Q` be rank-one projectors in `M_2(C)`. Their pure-state fidelity
is

```text
F(P,Q) = Tr(PQ),       0 <= F <= 1.
```

The following candidate costs are monotone functions of the same scalar:

```text
projector-overlap energy:       -Tr(PQ)
infidelity:                      1-Tr(PQ)
half squared HS distance:        Tr[(P-Q)^2]/2 = 1-Tr(PQ)
regularized relative entropy:   D(P || (3/4)Q+(1/4)(I-Q))
                               = log(4) - log(3) Tr(PQ).
```

Consequently every one is uniquely minimized at `Q=P`. This is continuous,
not merely a result on the runner's six test projectors: `Tr(PQ)=1` for two
rank-one projectors exactly when they are equal.

For two neighbors `P_L,P_R`, the direct extension is

```text
C(Q | P_L,P_R)
  = [1-Tr(QP_L)] + [1-Tr(QP_R)]
  = 2 - Tr[Q(P_L+P_R)].
```

The minimizing `Q` is the top eigendirection of `P_L+P_R` when that eigenvalue
is nondegenerate. Equal references give `Q=P` uniquely. Orthogonal references
give `P_L+P_R=I`, so every `Q` ties. Thus even this unusually natural cost
contains an exact ambiguity rule: it needs a declared eligibility domain,
tie behavior, or wider event instrument.

### The SU(2) Hamiltonian form

Assume common-frame covariance: the same `U in SU(2)` acts on both sites. The
commutant of `U tensor U` is `span{I,SWAP}`. A Hermitian pair generator is
therefore

```text
h = a I + b SWAP.
```

For product projectors, the SWAP expectation is exactly the overlap:

```text
Tr[SWAP (P tensor Q)] = Tr(PQ).
```

With equal recorded neighbors and open center, the conditional alignment
Hamiltonian is

```text
H_align = -J (SWAP_LC + SWAP_CR),       J > 0.
```

Its product-state expectation is minimized by `Q=P`. Reversing the sign
selects the orthogonal center instead. Positive scale and scalar shift do not
remove that sign.

The common-frame reading is itself physical. Independent onsite frame
covariance would leave only identity unless a shared connection, link, or
relational program is supplied. The current phrase “no possibility is
privileged” does not choose between those dynamical readings.

### Clock and energy quotient

Inside a fixed active carrier, the exact channel is unchanged up to global
phase under

```text
(H,t) ~ (alpha H + beta I, t/alpha),       alpha > 0.
```

This correctly quotients clock-unit rescaling and the energy zero. It leaves
the sign of the nontrivial exchange term and the dimensionless interaction
angle `theta=Jt`. Those are physical.

There is one important limit to the energy-shift quotient. If histories or
sectors have different numbers of active edges, adding `beta I` on every
active edge adds `beta N_active`, which is not a common scalar across those
sectors. It changes their relative phase. A record-dependent active graph
therefore needs an exact vacuum/edge-energy convention or a superselection
argument; “energy shift” cannot be discarded before the domain is fixed.

The full three-qubit Hamiltonian also does not have a unique global ground
state. `-(SWAP_LC+SWAP_CR)` has a four-dimensional ground space. The unique
conditional center answer came from holding two neighbor records fixed. It is
not a unique state of the closed quantum triple.

## 2. What Alignment Does And Does Not Select

The successful theorem is conditional:

> Given two equal rank-one reference records, an eligible center write, a
> rank-one event decomposition, and positive relational disagreement cost, the
> unique least-disagreement content is the matching projector.

It does not say that the center writes. If disagreement is charged only when a
write occurs, both aligned write and no write have zero cost. A minimal
occurrence extension is

```text
A_local
  = J times triggered disagreement
  + mu times eligible triggers left unwritten,

J > 0, mu > 0.
```

Now the aligned write wins uniquely. `mu=0` restores the write/no-write tie;
`mu<0` favors no write. `mu>0` is not a normalization of `J`: it adds a new
comparison between different event counts. In bare-metal language it is a
chemical potential for record occurrence.

This distinguishes five operations that cannot be compressed into “read”:

```text
an available/eligible event
    != an event occurrence
    != selected content
    != one actual history member
    != later readout of the locked record.
```

Calling the commit event a “read” is harmless terminology only after an exact
instrument says what commits. A later readout cannot be what first locks a
record under the current ontology: when a record exists, it already locks one
possibility. If a physical read performs the lock, that read and formation are
the same event, not two stages separated by an unlocked record.

### No-cloning implementation boundary

Suppose an isometry copied two arbitrary equal pure inputs into three while
leaving the originals:

```text
|psi>|psi>|blank> -> |psi>|psi>|psi>.
```

For `|0>` and `|+>`, the input inner product is `1/2`; the output inner
product is `1/(2 sqrt(2))`. An isometry cannot change it. Therefore the
relational minimizer is not a universal coherent copying channel on unknown
qubits.

There are live implementations:

- copy one of a supplied orthogonal record menu into a blank register;
- measure a supplied context and prepare its corresponding pointer record;
- transport rather than duplicate a relational reference;
- encode the relation in a larger error-correcting packet; or
- make the write a global-history constraint rather than a local unitary.

Each route must state its event algebra, blank/pointer carrier, and preservation
scope. The disagreement functional does not choose among them.

## 3. Coherent Bell Contexts

Exchange is genuinely Bell-capable. Since `SWAP^2=I`,

```text
U(theta) = exp(-i theta SWAP)
         = cos(theta) I - i sin(theta) SWAP.
```

At `theta=pi/4`, `U` maps `|01>` to a maximally entangled state. A singlet
with relationally co-rotated contexts

```text
A0=Z, A1=X,
B0=(Z+X)/sqrt(2), B1=(Z-X)/sqrt(2)
```

has `|CHSH|=2 sqrt(2)` exactly. This is a positive operational bridge from the
exchange class.

The bridge adds content not selected by static disagreement:

- the prepared two-site sector;
- the dimensionless angle `theta` and when the interaction stops;
- two separately indexed incompatible contexts;
- a relational program that carries their relative angle;
- a joint event decomposition; and
- a causal placement of the joint correlations.

Another covariant relative angle, `pi/6`, gives `|CHSH|=1+sqrt(3)` instead.
“Maximize Bell violation” could select `pi/4` in the displayed one-parameter
family, but that is a new target functional. It also does not create an
outcome or a permanent record.

Static alignment and Bell preparation pull in different directions. The
ferromagnetic pair term puts the triplet sector below the singlet. The singlet
can still be prepared as a boundary/program state or obtained from a different
bond/sign, but minimum local disagreement does not make it the unique vacuum.

## 4. Formation, Weights, And Actuality

The exact event instrument cannot be recovered from its averaged coherent or
dephasing channel. The runner repeats a sharp qubit control:

```text
K0=P0, K1=P1                         (Luders record events)
L0=I/sqrt(2), L1=Z/sqrt(2)           (random phase events).
```

Both sum to the same nonselective dephasing map. On the tested state, the
first event weights are `(2/3,1/3)` and the second are `(1/2,1/2)`. Their
event meanings are different. Neither channel covariance nor disagreement
selects which decomposition writes physical records.

Once a PVM/instrument and the quantum state rule are supplied, Born weights
are fixed by that instrument. A normalized pair of positive weights still
does not name its actual member. Actuality can be supplied by a sample, a
deterministic boundary/seed, a unique global solution, a sector member, or
another exact selection semantics. Those routes may be physically equivalent
after a theorem, but the static cost does not establish that theorem.

A deterministic local response table cannot replace the Bell event law under
setting independence: all sixteen binary local tables have `|CHSH|=2`. A
deterministic completion remains live if the relevant selector is global,
nonlocal in Bell context, retrocausal, or correlated with settings. That causal
placement is then a new law or boundary atom.

## 5. Record-Only State

The record corpus must be sufficient for every later lawful question, not
only for the context in which it was written. Two GHZ states

```text
(|000>+|111>)/sqrt(2),
(|000>-|111>)/sqrt(2)
```

have the same computational-basis diagonal and hence the same classical
equality/correlation data in that context. A later `X tensor X tensor X`
question distinguishes them with expectations `+1` and `-1`.

There are two serious closures:

1. phase/reference information is itself carried by complete records and
   local relational programs; or
2. after a record write, a proved no-return/superselection law makes the
   hidden phase forever inaccessible.

Both can make “state = records” predictively sufficient. They are not the same
law. The disagreement term supplies neither the phase record nor the allowed
future-operation restriction.

## 6. Renewal And Permanent Capacity

Site-tagged append-only records consume finite capacity. `N` sites permit at
most `N` strict first writes. If each still-open site writes independently
with fixed probability `p`, expected open capacity after `t` rounds is

```text
N(1-p)^t,
```

and the expected next write count is `Np(1-p)^t`. Sparsity delays saturation;
it does not create an indefinite positive local record flux.

Reversible export moves the issue. A shift can transport record information
into fresh cells while preserving it globally, but then:

- the record is not site-tethered;
- a finite cyclic carrier returns the information;
- an infinite blank tape is a boundary resource;
- a directional shift needs a covariant routing law; and
- collisions need an exact archive code or no-return sector.

Irreversible erasure/recycling, mobile record identity, infinite outgoing
capacity, cosmological creation of new support, and algebraic superselection
are distinct renewal architectures. Minimum local disagreement selects none.

## 7. Chirality And Matter

Nearest-neighbor ferromagnetic exchange on the cubic lattice has the
one-particle shape

```text
epsilon(k) proportional to
3-cos(k_x)-cos(k_y)-cos(k_z).
```

It is parity even and begins quadratically near zero momentum. It is not a
Weyl law. A relativistic matter sector therefore needs further block/carrier,
statistics, and interaction content.

The minimal two-band Weyl symbols

```text
H_plus(k)  =  sin(k_x)X + sin(k_y)Y + sin(k_z)Z,
H_minus(k) = -H_plus(k)
```

have identical spectra and opposite velocity-map determinants. No proper
`SU(2)` frame rotation implements inversion of all three axes. Proper cubic
covariance and any spectrum-only or squared-disagreement score therefore
leave the chirality pair tied.

Observed handedness can be owned by a reflection-odd law term or by an
achiral law plus an actual chiral domain/boundary. Stable excitations, fermion
statistics, species, gauge content, masses, and interactions remain additional
matter fields even after one chirality is fixed.

## 8. Clock

The exchange generator supplies a continuous ordering parameter, and record
append order supplies an event order. Neither is a metric clock without a rate
map. Twelve events can represent twelve or six duration units under rates one
and two while preserving the same event order.

The clock-rescaling quotient removes a conventional scale only after the
physical clock observable has been identified. It does not select:

- the dimensionless interaction phase at which a Bell or commit operation
  occurs;
- a formation rate relative to another physical process;
- lapse response to record/resource density;
- one common rate for all matter species; or
- the arrow/no-return boundary.

The clock can count formations after they occur. Making the clock transition
cause the first formation simply relocates the unsupplied trigger into the
clock law.

## 9. Resource And Green Response

The most promising unification found in this cycle is the extension from
projector disagreement to a scalar neighbor-disagreement action:

```text
A_G[phi]
  = (1/2) sum_<xy> (phi_x-phi_y)^2
    - sum_x s_x phi_x.
```

On a finite periodic cubic lattice, quotient the constant zero mode and use a
neutral source. The unique stationary point satisfies

```text
L phi = s,
```

where `L` is the cubic graph Laplacian. The runner solves the exact rational
`3 x 3 x 3` system and verifies uniqueness on the zero-mean subspace. This is
a real finite Green-response construction from the same mathematical shape as
minimum disagreement.

The source term does the physics. Without `s`, the minimum is constant and no
field appears. A record count, formation current, capacity deficit, energy,
or stress tensor must be identified with `s`; its sign and coefficient must be
fixed; the zero-mode/asymptotic boundary must be stated; and matter clocks
must couple universally. Source reversal gives the opposite field with the
same quadratic norm.

The scalar Green action does not yet supply attraction, the equivalence
principle, spatial/tensor metric response, nonlinear self-source, lensing,
gravitational radiation, or a controlled continuum equation. It is a useful
resource/propagation interface, not complete gravity.

## 10. Field-By-Field Augmentation Ledger

Every row states the narrow positive addition and an exact opposite or tied
competitor that survives the preceding rows.

| augmentation | new physical atom | gain | opposite or tied competitor |
|---|---|---|---|
| relational content | positive SWAP/disagreement orientation on a common-frame pair quotient | equal records select matching `Q` | reversed sign selects `I-Q`; full quantum ground space remains degenerate |
| occurrence | positive missed-trigger cost or exact eligibility-to-event clause | aligned eligible write beats no write | zero cost ties no write; negative cost favors no write |
| coherent Bell contexts | prepared sector, dimensionless exchange angle, relational setting program | exact `2 sqrt(2)` Bell-capable context | idle/other angle has same covariance and different correlations |
| physical event instrument | joint effects/Kraus maps and calibrated weight rule | event decomposition and weights | Lüders and random-phase instruments share one averaged channel |
| actuality | sample, unique extension, or global member rule | one event/history rather than a measure | another positive-weight sample or boundary member |
| record-only future scope | phase-complete records or proved no-return operation scope | equal record corpora have equal futures | opposite GHZ phases share one classical diagonal and later differ |
| renewal/export | mobile identity, fresh tape, recycling, or expanding support | indefinite local experimentation can be typed | finite site-tethered archive saturates; finite reversible tape returns |
| matter | exact block/Fock carrier, kinetic term, statistics, species, and interactions | stable relativistic excitation sector | cubic exchange magnons are stable but nonrelativistic and achiral |
| chirality | reflection-odd law sign or actual domain rule | one observed hand | `H_plus` and `H_minus` are isospectral proper-cubic partners |
| metric clock | physical rate observable and universal lapse/coupling map | duration beyond causal order | rates one and two preserve the same event order |
| resource/gravity | source identity, coupling, Green boundary, common matter response, tensor/nonlinear completion | exact scalar finite Green response and a path toward gravity | zero/opposite source, nonuniversal species couplings, and scalar-only response |

The runner's term-deletion audit treats the eleven rows as independent binary
physical branches. With all eleven preference terms present, one bookkeeping
winner exists. Removing any one term restores exactly two minimizers; reversing
that term selects its competitor. This is not an evidence count and not a
physical candidate construction. It is a precise check that the proposed
“single selector” has only become unique by storing every field choice.

## 11. Did A Complete Unique Winner Emerge?

Not from minimum disagreement alone.

The strongest coherent positive package reached here is:

```text
common-frame SU(2) exchange class
+ positive alignment orientation
+ positive occurrence chemical potential
+ a supplied Bell interaction phase/program
+ a supplied physical event instrument and realized-member semantics
+ phase-complete or no-return record scope
+ supplied renewal/export architecture
+ supplied relativistic matter/chiral sector
+ supplied metric rate
+ supplied record/resource source and Green action.
```

One can combine these entries into a composite exact history action or
instrument law and then minimize/sample it. If its carrier, coefficients,
boundary, event quotient, and sample/global-solution semantics are all exact,
it may be a complete canonical-law candidate. But the composite functional
contains the requested answers. The cost has become the law.

The best compression achieved is real:

- four pure-qubit disagreement measures reduce to one overlap scalar;
- common `SU(2)` covariance reduces pair generators to one SWAP coefficient;
- clock/energy quotient removes a positive scale and one scalar shift on a
  fixed carrier;
- `pi/4` exchange supplies an entangling Bell kernel; and
- the quadratic disagreement form supplies a finite Green kernel.

What remains is not eleven arbitrary prose axioms. Most entries should be
fields of one exact law and theorems derived from it. The search target is a
single action/instrument whose internal consistency forces the occurrence,
event, archive, matter, clock, and source terms together. This cycle has not
found that forcing theorem.

## Consequence For Axiom Need And Language

No disagreement sentence is ready for the Record axiom. In particular,

```text
A record forms where disagreement is minimized.
```

would hide the candidate domain, common-frame relation, sign, trigger cost,
tie behavior, physical event algebra, implementation, actual member, and
renewal scope. It would also falsely suggest that the conditional content
selector produces occurrence and Bell statistics.

Nor does this cycle justify adding SWAP, fidelity, relative entropy, a Bell
angle, a sampling rule, chirality, or a Green equation separately to the four
axioms. Those are exact-law fields.

If a future invariant action is uniquely derived, no new constitutional
sentence may be needed beyond the existing one-fixed-rule reference. If the
action must be supplied, the minimum constitutional content is a stable exact
reference to that complete law or physical equivalence class, not the slogan
that it minimizes disagreement. This cycle leaves verbatim drafting to the
full synthesis after the other probes report.

## No-Go Discipline Gate

The licensed negative statement is bounded:

> In the tested common-`SU(2)` pair-Hamiltonian class, pure-projector
> disagreement functionals, finite Bell/instrument controls, finite permanent
> archives, two Weyl-symbol partners, and finite cubic Green system, minimum
> relational disagreement does not uniquely determine a complete
> record-forming TOE law without additional field-specific physical atoms.

The positive alignment and Green reductions are explicit exceptions. No claim
is made against a richer invariant action, global consistency law, or exact
unique QCA on the full quasilocal algebra.

### N1 — Alternative-Route Enumeration

| route | strongest tested form | result |
|---|---|---|
| projector overlap | maximize `Tr(PQ)` for equal rank-one neighbors | unique matching `Q`, conditional on write |
| fidelity/infidelity | minimize `1-F(P,Q)` | same unique conditional content |
| Hilbert-Schmidt distance | minimize `Tr(P-Q)^2` | exactly twice infidelity |
| relative entropy | regularize candidate projector to full rank | same strict overlap ordering |
| exchange energy | classify common-`SU(2)` pair Hamiltonians modulo scale/shift | two nonzero signs; alignment sign selected by disagreement |
| global ground state | minimize the full three-qubit alignment Hamiltonian | ground space remains four-dimensional |
| missed-trigger action | penalize eligible no-write cases | positive coefficient closes occurrence in the local class; coefficient is new physics |
| coherent unitary copy | clone two arbitrary equal qubits into three | fails exact inner-product preservation |
| orthogonal pointer copy | restrict to a supplied record context | works; context/pointer becomes law content |
| maximum Bell capability | use quarter-exchange and optimize a setting angle | exact Bell kernel; target, phase, context, and instrument remain |
| sampled instrument | use Lüders joint events and Born trace weights | closes weights after instrument/state supplied; sample member remains |
| deterministic local actuality | preassign binary outcomes by local settings | bounded by `|CHSH|=2`; global/boundary deterministic routes remain live |
| phase-complete records | encode all future-relevant relational phase | live positive closure, exact decoder not supplied here |
| no-return superselection | forbid every future phase recombination | live positive alternative to phase records |
| sparse formation | reduce finite-site write rate | delays but does not close renewal |
| reversible export | move information into a fresh tape/sector | positive finite-time route; boundary, collision, and return remain |
| exchange matter | use cubic magnons | stable but quadratic and achiral |
| Weyl block | add a two-band relativistic symbol | mirror pair remains |
| event-count clock | use append order/frequency | order positive; metric rate and lapse remain |
| Dirichlet/Green action | extend disagreement to a scalar lattice field | exact finite Green response after source and zero mode supplied |
| one complete invariant action | derive all terms as one unique minimizer/history law | strongest live route; neither built nor excluded |

The search includes positive stochastic, deterministic, local, global,
reversible, irreversible, phase-record, superselection, finite-capacity,
infinite-export, matter, clock, and Green alternatives. The bounded conclusion
does not rest on one favored ontology.

### N2 — Wall-Independence Audit

The principal walls are independent in the tested controls:

| pair | independent counterexample |
|---|---|
| content vs occurrence | aligned write and no write both have zero disagreement |
| occurrence vs weights | a forced write can use different normalized instruments |
| weights vs actuality | two positive weights do not select one member |
| actuality vs permanence | one sample can still be coherently erased without a preservation scope |
| permanence vs record sufficiency | opposite GHZ phases share the readable diagonal but have different futures |
| record sufficiency vs renewal | a complete finite archive still saturates |
| renewal vs matter | an infinite blank tape carries records without producing Weyl excitations |
| matter vs chirality | the two Weyl signs have the same spectrum |
| chirality vs clock | either Weyl sign permits arbitrary rate calibration |
| clock vs resource source | a common tick exists with zero, positive, or opposite scalar source |
| scalar Green response vs gravity | `L phi=s` does not impose WEP or tensor/nonlinear metric dynamics |

Closing one row does not close its neighbor. A future unified theorem may bind
several walls; if so, the wall count must be collapsed rather than quoted.

### N3 — Hidden-Wall Scan

The probe exposes rather than hides: common versus independent frame action;
rank-one event domain; equal-neighbor eligibility; exchange sign; positive
scale orientation; active-edge sector; missed-trigger coefficient; tie rule;
orthogonal pointer context; blank register; interaction phase; preparation;
relational setting program; physical Kraus/effect decomposition; trace-weight
reading; actual sample/global member; Bell causal placement; record identity;
future-operation scope; phase/reference decoder; finite versus infinite
capacity; export direction; collision handling; boundary blankness; matter
block/Fock composition; statistics; masses/interactions; chirality ownership;
metric rate; lapse; resource identity; source sign and strength; Green zero
mode/asymptotic boundary; common coupling; and scalar-to-tensor/nonlinear
gravity completion.

The runner's eleven-term bookkeeping winner is explicitly not promoted to a
physical candidate.

### N4 — Exact Residual Matching

The preceding tournament residual was “copy versus opposition after a
trigger.” This cycle closes exactly that residual for equal pure-qubit
references. It does not reuse the closure as proof of occurrence.

The exact-law inventory separated domain, context, event decomposition,
weights, actuality, preservation, decoder, renewal, boundary, and clock. The
remaining entries here match those fields one for one. The matter and gravity
entries are additional TOE interfaces rather than relabeled formation walls.

The reversible-QCA and capacity cycles separated transport/export from
formation and renewal. This note does not count a finite cyclic shift as
permanence or treat a Green inverse as a source law.

### N5 — Resolution And Rhetoric Audit

- The commutant statement is for common `SU(2)` covariance of a two-qubit
  pair generator, not every qubit QCA.
- Uniqueness of `Q=P` is conditional on two equal rank-one references and an
  already eligible rank-one write.
- The no-cloning result targets universal coherent duplication of unknown
  states, not orthogonal record copying or global-history formation.
- Bell capability is not called Bell sampling or actuality.
- The archive result is finite and site-tagged; infinite algebraic sectors
  remain live.
- The Weyl pair is a symbol-level chirality control, not a complete fermion
  construction.
- The Green result is an exact finite scalar solve, not tensor gravity or an
  empirical `1/r` closure.
- “The cost has become the law” means every exact field was inserted into the
  composite selector; it is not a claim that variational laws are illegitimate.

### N6 — Partial-Closure Path

The lowest-cost constructive route after this cycle is:

1. retain overlap/SWAP as the unique relational content selector for equal
   recorded references;
2. search whether a conservation or consistency theorem fixes the sign and
   positive occurrence coefficient together, rather than registering both;
3. compile an orthogonal relational record packet into nearest-neighbor qubit
   operations, avoiding the universal-cloning reading;
4. use quarter-exchange as the coherent Bell kernel, then derive or state one
   physical joint instrument and global causal placement;
5. prove either phase-complete record transport or a no-return sector theorem;
6. integrate renewal with the same conserved current used as the Green source;
7. test whether the resulting covariant block law forces a Weyl pair, one
   domain, a common clock coupling, and a tensor response; and
8. only then test whether one invariant action has a unique complete minimizer
   or sampled/global-history law.

Any success can retire several ledger atoms. The current four axioms and
approved primitives do not supply the missing coefficients or maps by name.

### N7 — Strongest Steelman

The strongest live opponent is a single dimensionless action on complete
quasilocal histories modulo common qubit-frame conjugation, clock rescaling,
energy zero, update-schedule gauge, record recoding, and operational future
equivalence. Its local term is exchange/disagreement; its topological sector
forces a chiral relativistic block; its conserved current both exports inverse
information and sources geometry; its unique low-record boundary supplies
fresh capacity; and its stationary/global consistency equation produces one
actual record history whose context frequencies obey the quantum instrument.
The same action fixes its clock through the current and makes every matter
block couple to one emergent tensor metric.

If that action is derived from the existing algebra/lattice and has one
nontrivial solution modulo the quotient, it defeats the bounded conclusion
and may remove any new axiom need. If it must be supplied, it is still an
excellent TOE candidate—just the exact physical law rather than a theorem of
the one-line disagreement score. This cycle neither constructs nor rules it
out.

### N8 — Cross-Cycle Echo

The prior finite tournament already found that disagreement breaks the
copy/opposition tie. The new information here is the exact qubit lift, the
equivalence of four metrics, the two-sign `SU(2)` quotient, the no-write and
no-cloning boundaries, the quarter-exchange Bell bridge, and the finite Green
bridge.

Earlier exact-law, record-capacity, matter, and reversible-export probes found
separate event, boundary, phase, chirality, and source residuals. They are not
recounted as independent evidence. This cycle asks whether the strongest
positive selector absorbs them. It partially absorbs coherent exchange and
the Green kernel, but not their source, event, archive, matter, clock, or
gravity interfaces.

**No-go-discipline status:** PASS for the bounded class statement. A universal
no-go against a unique invariant action would fail the steelman and is not
made.

## Verification

Run:

```bash
python3 scripts/relational_qubit_disagreement_canonical_law_escalation_probe_2026_07_14.py
```

The PASS count is a contract and exact-control count, not a count of
independent scientific facts. No external literature was used as a premise in
this assumptions/first-principles slice; the separate literature slice owns
that comparison.
