# Long-Run Record-Only Append Architecture — Cycle 32

**Date:** 2026-07-14

**Type:** authority-free exact finite/infinite-volume storage, recurrence,
time, thermodynamic, and gravity seam probe

**Authority:** none. This note does not amend an axiom, register a primitive,
select a physical law or boundary, issue an audit verdict, or authorize a
commit, push, PR, or publication. It tests the exact **site-tethered,
append-only** reading of Record. The live words “records are permanent” do not
by themselves settle that reading against migratory record identity.

Companion runner:

```text
scripts/long_run_record_only_append_architecture_cycle32_2026_07_14.py
```

## Question

Can one homogeneous nearest-neighbor law whose complete physical state is a
configuration of permanent, at-most-one-per-site records support all of the
following without hidden mutable state?

1. indefinitely many locally certified trials;
2. a recurring bounded apparatus;
3. transport of fresh outcomes through a fixed boundary;
4. a positive long-run event density;
5. a thermodynamic arrow and reusable clock; and
6. the record-capacity source suggested in the gravity lane.

The routes tested are bounded local append, an expanding front, a sparse
self-similar archive, lossless and aggregate encoding, boundary export,
migratory identity, and a supplied global history.

## Result Up Front

The exact split is sharper than “finite storage versus an infinite lattice.”

### What works

An infinite `Z^3` lattice permits indefinitely many formation events under a
homogeneous nearest-neighbor append law. A single seed can launch an expanding
front, or a growing one-dimensional tape can append one event after another.
No lattice-growth axiom and no hidden mutable state are needed for that narrow
existence result. The permanent record pattern itself is the program counter.

This supplies:

- an unbounded commit count;
- an unbounded spatial corpus;
- an arrow given by strict record inclusion; and
- exact volume, shell, and boundary-channel bookkeeping.

### What does not work

A fixed finite region cannot host indefinitely many **new locally certified**
trials. If each trial leaves at least `c>0` new records in a fixed certification
region `K`, then

```text
number of certified trials <= floor((|K|-initial records in K)/c).
```

Its long-run local formation rate is zero. More strongly, a time-translation-
stationary formation process with at most one formation at each spatial site
has exactly zero spacetime intensity. Positive instantaneous fronts and
positive final spatial record density do not evade that theorem.

Lossless encoding does not recycle site-tethered permanent storage. The source
records remain. An exact archive of `m` independent binary outcomes still
needs at least `m` binary record carriers. Storing only the success count needs
only `ceil(log2(m+1))` bits, but it destroys trial order and is not the same
certified corpus. Migrating a fact can free its old carrier, but that is the
other permanence semantics.

Boundary export also does not free a site-tethered archive. It creates more
records outside. A fixed cut made from `b` one-qubit record carriers cannot
transmit an indefinitely growing collection of independent perfectly readable
binary facts: its distinguishable capacity is at most `b` bits, conditional on
the generated tensor-carrier reading. A moving front avoids the cut only by
moving the experiment.

### The bare-metal meaning

The literal record-only append architecture is viable as a **growing-history
machine**:

```text
fresh space -> new record -> new causal frontier -> next record.
```

It is not a reusable finite computer. Its clock tape, experimental corpus,
and working head all move into fresh sites. At any fixed location, physical
change eventually stops unless some physical state can change without being a
permanent site-tethered record.

That fact does not force a new Record, Admissibility, or generic resource
axiom. Finite saturation already follows from the tested Record reading;
infinite continuation follows from Lattice plus a selected transition law and
seed/boundary. If the intended TOE requires genuinely recurring bounded local
apparatus, the choice is architectural, not a missing storage slogan:

1. distinguish recyclable working state from permanent records;
2. use migratory/encoded record identity with a proved decoder;
3. use a global-history/process law in which nonrecord alternatives are
   law-side rather than mutable physical state; or
4. accept that clocks and apparatus are growing fronts rather than recurring
   local objects.

No current probe selects among those four.

## 1. Exact Premises And Definitions

Let `Lambda` be a set of sites. At history stage `t`, let `R_t` be the set of
sites carrying records. The tested append branch is

```text
R_t subseteq R_(t+1).
```

When a site enters `R_t`, its content and address remain fixed in every later
stage. Define the formation count in `K subseteq Lambda` by

```text
A_T(K) = |(R_T intersect K) \ (R_0 intersect K)|.
```

A **locally certified trial in `K`** is a trial whose new preparation,
outcome, or close certificate contains at least one newly formed record in
`K`. More generally its certificate cost is at least `c` when distinct trial
certificates use at least `c` fresh sites of `K`.

This is deliberately stricter than saying that a timeless global record
configuration can be partitioned into trial-shaped blocks. Local certification
requires a new readable difference in the named local region.

Three densities must not be conflated:

1. **final spatial record density:** records per spatial site in a terminal or
   late configuration;
2. **instantaneous formation density:** new formations per spatial site in one
   selected layer; and
3. **spacetime formation density:** formation events divided by spatial sites
   times elapsed layers.

A filled expanding ball has final spatial density one while its spacetime
formation density tends to zero.

The exact results below do not assume that a layer label is already physical
metric time. It is an event-order or causal-depth counter. Relative rates and
proper time remain law theorems, as in Cycle 22.

## 2. Finite-Volume Theorems

### 2.1 Append-capacity theorem

For finite `K`, telescoping gives

```text
A_T(K) = |R_T intersect K|-|R_0 intersect K|
       <= |K|-|R_0 intersect K|.
```

No dynamics, probability, tensor composition, or outcome alphabet is needed.
It follows only from one site entering the permanent record set at most once.

If every locally certified trial consumes at least `c` fresh sites in `K`,
then disjointness of permanent certificates gives

```text
trials_T(K)
    <= floor((|K|-|R_0 intersect K|)/c).
```

This is sharp: a schedule that uses exactly `c` new sites per trial reaches
the bound.

### 2.2 Zero long-run local formation rate

For any finite `K`,

```text
A_T(K)/T <= (|K|-|R_0 intersect K|)/T -> 0.
```

Dividing once more by `|K|` gives zero local spacetime density. A sparse rule
can delay exhaustion, and a rate that decreases sufficiently fast can leave
some sites open forever, but neither produces a positive asymptotic local
formation flux.

### 2.3 No nontrivial bounded record-only cycle

Order finite record configurations by inclusion of their occupied
site/content pairs. Every nontrivial append transition strictly increases
this partial order. The transition graph is acyclic. Therefore a finite
closed apparatus whose complete state is its site-tethered record
configuration cannot return to an earlier physical phase.

A purported cycle has only three readings:

- the record configuration changes, in which case permanence forbids return;
- it does not change, in which case no physical phase has changed; or
- another mutable variable supplies the phase, in which case the physical
  state is wider than the record configuration.

The modular working clock in the earlier capacity note is therefore a valid
recyclable-sector control, but it is not available inside the **literal
record-only** branch unless its changing phase is law-side/gauge or the
Qualification is widened.

### 2.4 Fixed local corpus theorem

Cycle 21 defines certified blocks `(preparation, outcome, close)` on actual
records. If every block uses `c` new local records, an `N`-site local corpus
contains at most `floor(N/c)` such blocks. Birkhoff, mixing, and unique
ergodicity can characterize an already supplied infinite block process; they
do not manufacture an infinite local carrier.

Thus two questions are independent:

```text
Does an infinite certified sequence exist?       occurrence/renewal
What frequency does that sequence have?          process/ergodic law
```

Solving the second does not solve the first.

## 3. Zero Stationary Spacetime Intensity

There is a sharp infinite-volume statement that is easy to miss.

Fix one spatial site `x`. Let `N_x([0,T))` count formations at `x` during a
time interval of length `T`. Site-tethered one-record permanence gives

```text
N_x([0,T)) <= 1.
```

If the formation process is invariant under time translations and has
intensity `lambda`, stationarity gives

```text
E[N_x([0,T))] = lambda T.
```

Since this is at most one for every `T`, `lambda=0`. Therefore:

> A jointly time-stationary, site-tethered, at-most-one-formation-per-site
> process has zero formation intensity, even on infinite `Z^3`.

Equivalently, for every finite or growing spatial region `K_T`,

```text
formation events in K_T x [0,T)
-------------------------------- <= 1/T.
             |K_T| T
```

provided each spatial site appears only once in the interval. The upper bound
does not care how fast `|K_T|` grows.

This theorem does **not** forbid:

- a universe with a distinguished low-record past boundary;
- a nonstationary expanding front;
- a positive density of records in a final spatial slice;
- infinitely many total events spread over infinitely many sites; or
- stationary rereads that form no new records.

It forbids only positive **stationary formation** intensity under the tested
site-tethered semantics.

## 4. Expanding-Front Route

### 4.1 Exact homogeneous nearest-neighbor construction

Take record absence/presence as the minimum comparator. Conditional on one
fixed record content being available, use the same parallel update at every
site:

```text
R_(t+1) = R_t union
          {open x : some nearest neighbor of x belongs to R_t}.
```

The rule is translation covariant, proper-cubic covariant, nearest-neighbor,
deterministic, and record-only. The displayed layer parameter is explicit law
data, not a metric-time derivation. A seed at the origin is boundary/state
data, not a privileged law site. Its layer `r` fills the Manhattan shell at
distance `r`. A fair asynchronous variant gives unbounded continuation but
not the same layer shape unless a schedule-equivalence theorem is added.

The construction proves existence only. It does not supply binary outcome
weights, one-history actuality, the seed, fairness, a metric duration for a
layer, or the exact one-`M2` record decoder. Cycle 26 shows that finite phase
and certificate roles can be compiled into spatial one-qubit record geometry
at large cost; it does not make this minimal front a completed TOE law.

### 4.2 Exact volume and surface accounting

For the `Z^3` Manhattan ball,

```text
|B_r| = (4r^3+6r^2+8r+3)/3,
|S_r| = 4r^2+2                         for r>0.
```

The number of directed nearest-neighbor edges leaving `B_r` is

```text
E_out(r) = 12r^2+12r+6.
```

The first formula is storage volume. The second is the number of new sites in
one exact graph-distance layer. The third is only a channel-count geometry;
turning an edge into one symbol per tick requires a transport law.

As `r` grows,

```text
|S_r|/|B_r|       ~ 3/r,
E_out(r)/|B_r|    ~ 9/r.
```

If `n` certified trials consume at least `c` sites and all their records lie
inside `B_R`, then necessarily

```text
c n <= |B_R|-initial records,
R >= (3 c n/4)^(1/3) + O(1).
```

That lower bound is a volume statement, not a construction of efficient
routing.

### 4.3 Density audit

In the synchronous seed front, the number of new formations at layer `r` is
`4r^2+2`, and the cumulative number is `|B_r|`. Consequently:

```text
instantaneous front fraction = |S_r|/|B_r|  ~ 3/r,
cylinder spacetime density   = 1/(r+1),
causal-cone spacetime density                         ~ 4/r.
```

The total number and even the total layer rate grow without bound, but the
formation fraction and spacetime density vanish. This is the concrete
counterexample that separates infinite continuation from positive stationary
density.

### 4.4 What happened to the apparatus

The seed does not repeatedly reset and conduct trials at the origin. It
launches one computation whose active head is the frontier. Later trial
certificates are farther away. A fixed observer can recover a later result
only if new information crosses back through its bounded neighborhood, which
again consumes finite local record capacity under the tested semantics.

Thus the expanding-front route is a positive answer to “can the record-only
universe continue?” and a negative answer to “does one bounded apparatus
recur?” Those questions must not be merged.

### 4.5 One-shot transport versus a reusable channel

On the isolated sector where every existing front record has the same binary
content `b`, refine the update so each newly reached site locks the same `b`.
The seed fact is then copied to every later shell. This is exact one-to-many
transport of one immutable fact by a homogeneous growing front.

It is not a reusable wire. After the `b` front occupies a corridor, a later
opposite bit cannot replace any carrier on it. A sequence of independent
messages therefore needs fresh parallel support, migratory/mutable carriers,
formation timing as another explicitly decoded channel, or a global law that
does not represent communication as repeated local carrier writes. Collisions
between differently labelled fronts also require a law rule not specified by
the isolated-sector construction.

## 5. Sparse And Self-Similar Routes

Place special trial markers at distances

```text
1,2,4,8,...,2^k
```

along one ray. The number of markers through radius `R=2^k` is `k+1`, so
their three-dimensional spatial density is

```text
(k+1)/|B_(2^k)| -> 0.
```

If each later marker must be reached by nearest-neighbor causal propagation
from the prior marker and the only changing physical state is permanent
records, the intervening corridor must also acquire a record-defined front.
The support cost through radius `R` is then at least order `R`, not order
`log R`. Sparsifying the **certificates** does not sparsify the causal tape.

A branching self-similar set of dimension `d<3` similarly supports infinitely
many markers but zero three-dimensional density. A set with positive spatial
density consumes order `R^3` sites. These routes offer an exact trade:

```text
infinite events with sparse support, or positive final spatial density with
volume-order storage; neither gives positive stationary formation density.
```

A supplied static global configuration may place sparse markers without
causal bridge records. That changes the route from local formation to a
boundary-selected global history and is treated in Section 8.

## 6. Recyclable-By-Encoding Route

### 6.1 Exact independent-corpus bound

After `m` binary trials there are `2^m` possible ordered corpora. If `k`
one-qubit record carriers must distinguish all corpora perfectly, their
generated tensor carrier has at most `2^k` mutually orthogonal sectors. Hence

```text
2^k >= 2^m,
k >= m.
```

This information form is conditional on the finite tensor-composition
theorem. The simpler fresh-site certificate count is not.

### 6.2 Aggregate compression is a different observable

If only the number of successes is retained, there are `m+1` possible values,
so

```text
k >= ceil(log2(m+1)).
```

But `C(m,j)` distinct ordered corpora share success count `j`. Preparation
ancestry, order, correlations, adaptive branches, and individual outcome
records are gone. This can be enough for one declared statistic; it cannot be
cited as preservation of the certified corpus used in the probability lane.

### 6.3 Why append-only compression does not free space

Suppose an encoder appends a compressed `k`-site representation of `m` old
records. Site-tethered permanence leaves all `m` source records present. The
occupied support becomes at least `m+k`, not `k`. Deleting or clearing the
source after verifying the code is exactly what the tested permanence branch
forbids.

Correlations can lower information rate. A deterministic periodic sequence
can be represented by a short program and phase, and a positive-entropy
stationary source can be compressed toward its entropy rate under the usual
process premises. Neither observation supplies carrier renewal:

- exact old site records remain occupied;
- a positive entropy rate still consumes linearly growing perfect-record
  capacity; and
- a short generator represents a law for outcomes, not independently retained
  records of every trial.

### 6.4 Migratory identity is a real escape

A SWAP can move a readable bit from one carrier to another and clear its old
address. The fact survives, but the `(site,content)` pair does not. An
error-correcting or topological code may likewise preserve a logical record
while changing every microscopic carrier.

This route is not ruled out. It requires an exact identity relation, decoder,
allowed recoding operations, and theorem that all future readouts preserve the
same physical fact. It cannot be silently called site-tethered append-only
permanence.

## 7. Boundary-Export Route

### 7.1 Copying outward is growth, not renewal

For site-tethered records,

```text
interior record before export = still present after export,
exterior copy                 = additional occupied site.
```

Export can prevent one **chosen exterior archive** from filling, because its
support can expand forever. It does not restore open sites in the source
region.

### 7.2 Fixed-cut information pressure

Let a bounded apparatus be separated from the exterior by a finite cut whose
readable record carriers contain `b` one-qubit sites. If the **terminal cut
contents alone** are the readable message, generated finite composition gives
at most `2^b` orthogonal fully occupied sectors. An ordered corpus of `m`
independent binary outcomes has `2^m` possibilities, so that restricted
terminal-content protocol requires

```text
m <= b.
```

The full finite append transcript can carry more than terminal content. If
discrete formation order is itself certified, the number of cut transcripts
of every length through `b` is at most

```text
H_b = sum_(k=0)^b [b!/(b-k)!] 2^k.
```

This includes site choice, order, and binary content. It is larger than
`2^b`, but still finite. Certifying that order also needs causal/clock records
outside the cut; it is not contained in terminal cut content alone.

A continuously resolved formation time could mathematically serve as another
channel. The axioms supply no continuous clock, resolution, timing decoder, or
rate law, and only record content is directly readable. This probe therefore
does not claim a universal `b`-bit bound on every timing protocol. It claims
the exact finite result: only `b` cut sites can themselves undergo formation,
and every discrete site/order/content transcript on that fixed cut is finite.

Static records on the cut can serve forever as a program or boundary
condition. They cannot undergo a fresh record formation on every trial,
because their readable content never changes. An autonomous exterior front
may continue after the cut saturates, but those later facts are not a sequence
of new cut formations from an unchanged interior.

This cut statement is deliberately conditional and narrow. It does not rule
out coherent nonrecord carriers, migratory codes, an infinite-width cut, or a
global process law that does not factor through sequential carrier messages.

### 7.3 Surface throughput is not a law

`E_out(r)=12r^2+12r+6` counts available nearest-neighbor edges. A claim such
as “one bit crosses each edge per tick” adds symbol capacity, a tick, collision
rules, and a decoder. The axioms supply none of them. Surface/volume scaling
is therefore a useful design pressure, not a derived bandwidth or energy law.

## 8. Global-History Route

A complete infinite record configuration can contain infinitely many
trial-shaped blocks at positive spatial density. A homogeneous constraint can
accept the configuration, and a spatially ergodic boundary distribution can
give block frequencies. No changing ontic tape is needed if the process
functional is fixed law data, as in Cycle 30.

This route survives the storage objection because it does not demand that one
finite apparatus sequentially create the entire corpus. It pays elsewhere:

1. the global boundary/history must be selected;
2. local nearest-neighbor admissibility must be shown to generate or exactly
   characterize the global process law;
3. causal order and intervention containment must be defined;
4. one actual history and its weights remain different type problems; and
5. a static spatial repetition of apparatus blocks is not yet one apparatus
   recurring in physical time.

There is an elementary chronology separator. The same final set of `N`
records has `N!` possible append orders before contents are considered. The
terminal configuration alone does not select which order occurred. A global
history law may include the order relationally, but the bare record set does
not.

Likewise, the same homogeneous infection law has two different boundary
realizations:

```text
empty initial record configuration -> no seed-triggered formation,
one recorded seed                 -> an unbounded front.
```

Homogeneity of law does not choose the low-record past boundary.

## 9. Thermodynamic Seam

### 9.1 What is derived

Total record count is a Lyapunov function on any history containing
formations:

```text
|R_(t+1)| >= |R_t|.
```

It gives a microscopic orientation whenever at least one strict append occurs.
Finite systems have absorbing or partially jammed future sectors. A uniformly
positive hazard for every remaining open site drives expected open capacity
and formation current to zero.

### 9.2 What is not derived

Monotone record count is not automatically thermodynamic entropy. In the
binary `N`-site comparator, the number of configurations at occupancy `k` is

```text
Omega_N(k)=C(N,k) 2^k,
Omega_N(k+1)/Omega_N(k)=2(N-k)/(k+1).
```

The macrostate count grows only while `3k<2N-1`, ties when equality holds,
and then decreases toward the fully occupied layer. Thus
`log Omega_N(k)` is not monotone along all append histories even though `k`
is.

Nor does irreversible append produce nontrivial finite-volume equilibrium.
For a two-state edge `open -> recorded` with positive forward rate and zero
reverse rate, detailed balance forces every stationary measure to put zero
weight on `open`. The equilibrium is supported on absorbing records, not a
reusable thermal state.

Temperature, heat, Landauer cost, equation of state, fluctuation law, and a
reversible microscopic completion remain absent. If append is a reduced
description of reversible physics, inverse/branch information must persist in
fresh carriers or a boundary, reproducing the storage question at a larger
scale.

## 10. Time Seam

The positive theorem is a growing-tape clock. Along an infinite causal path,
define

```text
tau = number of committed clock records on the path.
```

It is monotone, readable, and unbounded. A front can therefore carry an
indefinite ordinal clock without an external counter.

The negative boundary is local recurrence. If every tick forms a permanent
record in one finite clock region, the clock has finitely many ticks. If the
phase recurs without changing the complete record configuration, it is not a
physical phase in the literal record-only ontology. If a distant front is the
clock head, a bounded observer needs a new return record to learn the latest
tick and its local display again saturates.

Nothing here fixes:

- which commits are clock commits;
- schedule-equivalent coarse graining;
- relative rates of two fronts;
- synchronization;
- continuum proper time; or
- metric response to record load.

The clock remains a consequence of an exact event law, not the cause of a
record lock.

## 11. Gravity And Resource Seam

The record-only append picture supplies real bookkeeping but not gravity.

### 11.1 Exact geometric pressure

A filled ball contains order `r^3` permanent records while its active shell
and boundary cut contain order `r^2` sites/edges. The ratios scale as `1/r`.
This is a genuine geometric fact and can motivate a capacity-pressure model.
It is not the lattice Green theorem, a Newtonian potential, or curvature. A
Poisson operator, source map, constitutive response, and coefficients must
still be selected or derived.

### 11.2 Vacancy is not yet a universal scheduler

Let `q` be a local vacancy or usable-capacity fraction. Infinitely many lapse
maps share the intuition that clocks slow as capacity falls, for example

```text
L_1(q)=q,
L_2(q)=q^2,
L_3(q)=q/(2-q).
```

They agree at empty and exhausted endpoints and disagree in between. Capacity
does not select one. Even a selected common scalar lapse does not fix spatial
transport or the tensor response required for full light bending.

### 11.3 Literal record-only pressure on the existing candidate

Cycle 9's stationary conservative resource field uses a recyclable working
occupation process while a permanent archive grows elsewhere. Cycle 10 and
Cycle 11 expose the same separation through reversible carriers and exported
inverse information. Those are constructive exact-law candidates, but their
working variables are not a finite site-tethered permanent record archive.

If Qualification is read literally and exhaustively, a recyclable occupation
or clock phase must be record-derived, law-side, or nonphysical. The gravity
lane therefore needs an explicit ontology map:

```text
working resource state -> record configuration / law calculator / widened state.
```

Without that map, “storage pressure causes gravity” mixes an append-only
archive with a reusable transport medium.

### 11.4 No generic resource clause follows

The finite capacity `|K|` is already a theorem of the tested Record semantics.
Calling vacancy “resource” adds no dynamics. A physical resource requires an
invariant current or conservation/renewal law and a proved coupling to record
formation, matter, clocks, and transport. Those are fields of the exact law,
not a consequence of the word permanent.

## 12. TOE-Lane Classification

| lane | exact result from site-tethered append | still needed |
|---|---|---|
| formation | each site can lock once; homogeneous fronts exist conditionally | occurrence rule, outcome selection/weights, boundary, schedule |
| probability | an infinite spatial corpus can exist | recurring certified-block law, process consistency, actual-history and frequency theorem |
| time | append order and path commit count give an ordinal clock | recurring local clock or growing-head interpretation, relative rate, metric theorem |
| matter/transport | permanent patterns can encode finite apparatus and moving fronts | efficient one-`M2` law, stable particles, repeated interactions through fixed cuts |
| thermodynamics | record count is monotone and finite regions absorb/jam | entropy identification, reversible completion, temperature, heat, typicality |
| resource | open-site count is exact finite capacity | invariant resource current, renewal/allocation, coupling and empirical decoder |
| gravity | volume/surface pressure and archive/source separation are explicit | Poisson/tensor dynamics, universal matter coupling, coefficients, continuum limit |
| cosmology | a low-record boundary can launch unbounded growth | why that boundary, homogeneity/isotropy of history, observed late-time regime |

The architecture closes none of those lanes by the storage theorem alone. It
does identify which proposed closures are type-consistent.

## 13. Constitutional Placement Decision

### Record

No additional “fresh capacity,” “clock locks,” “read locks,” or “records
export” sentence is forced. The finite theorem already follows if permanence
is site-tethered. If Nature uses migratory logical records, a same-site
continuation sentence would be false and Record eventually needs an
identity-preservation formulation backed by the exact decoder.

### Admissibility

No renewal clause belongs here. Admissibility says which possibilities are
available from nearest-neighbor conditions. It does not choose an occurrence,
seed, schedule, transport current, rate, or boundary.

### Generic resource axiom

No generic storage/compute-budget sentence is justified. It would restate a
counting bound while hiding the physical choices: what is conserved, what can
move, what can be reused, and how load affects matter and clocks.

### Law and boundary

The following belong to the exact law or its state/boundary interface unless
derived:

- front trigger and outcome rule;
- causal/schedule semantics;
- record-identity and export decoder;
- blank/fresh-support boundary;
- global process weights and actuality interface;
- resource current and renewal;
- clock comparison and metric rate; and
- scalar/tensor gravity response.

### Qualification pressure

If a completed TOE requires a finite bounded apparatus to undergo infinitely
many physically distinct phases, the exact site-tethered record-only branch
cannot supply it. That is not evidence for another sentence inside Record or
Admissibility. It is evidence that at least one of these must be true in the
final exact architecture:

1. mutable working degrees are physical state in addition to records;
2. record identity is migratory rather than site-tethered;
3. the apparent local process is a section of a global record history; or
4. the physical apparatus is an unbounded growing structure.

The exact law must decide. Constitutional wording should follow that decision,
not pre-empt it.

## 14. Assumptions Exercise

| premise | layer | status in this note | function | failure consequence |
|---|---|---|---|---|
| current four axioms | framework | supplied target | ontology and covariance baseline | a future constitutional rewrite changes the target |
| scale reference is units only | approved primitive | supplied boundary | blocks importing storage energy or gravity strength | physical coefficient remains open |
| kinetic isotropy is structural only | approved primitive | supplied boundary | blocks importing a rate/metric theorem | clock and transport remain open |
| realized-state reference is pointwise only | approved primitive | supplied boundary | permits an actual record history without weights | actuality selection remains open |
| site-tethered permanence | semantic branch | explicit conditional | makes finite append theorem | migratory records evade local exhaustion |
| record configuration is complete physical state | literal Qualification reading | explicit target | excludes hidden mutable phases | global-law or widened-state route remains |
| at least `c` fresh records per local trial | protocol condition | explicit conditional | yields trial cap | rereads or remote/nonlocal certificates are different protocols |
| finite tensor composition | theorem/import where used | explicit conditional | yields independent-bit and cut bounds | site-count bounds survive without it |
| synchronous/fair front schedule | law field | explicit construction input | realizes shell growth | homogeneous trigger alone does not fix timing |
| seed/low-record boundary | state/boundary | explicit construction input | starts the front | empty state is static under seed-triggered law |
| vacancy-to-lapse response | open law field | not supplied | would connect storage to clock/gravity | many inequivalent responses survive |

## 15. No-Go Discipline Gate

The narrow negative claim is:

> Under site-tethered at-most-one-record-per-site permanence, a fixed finite
> region cannot sustain a positive asymptotic rate of newly locally certified
> formation events; a time-stationary formation process has zero intensity.

This is **not** a no-go against infinite global computation, global record
histories, migratory records, reversible nonrecord carriers, global process
functionals, or an exact law deriving effective recurring laboratory physics.

### N1 — Alternative-route enumeration

Attempted routes: finite local append; sparse local append; a growing
one-dimensional tape; a three-dimensional expanding front; sparse powers-of-
two markers; self-similar branching support; lossless corpus compression;
aggregate-statistic compression; migratory/SWAP identity; copy-and-export;
fixed-cut transport; infinite-width boundary transport; static global record
history; record-side program counters; law-side process functionals;
recyclable nonrecord working state; reversible export of inverse information;
and vacancy/resource scheduling.

The growing-front, migratory-identity, global-history, and widened-working-
state routes remain live. That is why the negative is local and semantic.

### N2 — Wall-independence audit

The following walls are independent:

- finite local capacity follows without a rate law;
- zero stationary intensity follows even in infinite volume;
- infinite continuation follows without local recurrence;
- corpus information cost is distinct from certificate site cost;
- thermodynamic entropy is not record count;
- a scalar capacity response is not tensor gravity; and
- boundary selection is not law homogeneity.

One complete exact law may close several jointly, but none is renamed as a new
axiom because it remains open.

### N3 — Hidden-wall scan

`Formation`, `trial`, `local`, `certificate`, `recurring apparatus`,
`permanent`, `site-tethered`, `migratory`, `export`, `encoding`, `event
density`, `stationary`, `clock`, `resource`, and `global history` are typed in
the sections above. Layer number is not assumed to be metric time. Edge count
is not called bandwidth. Vacancy is not called energy. A final spatial record
density is not called an event rate.

### N4 — Exact residual matching

| control | resolves | does not resolve |
|---|---|---|
| telescoping append count | finite local formation/trial cap | which trials occur |
| stationary one-event/site bound | formation intensity | reread or nonrecord currents |
| Manhattan front census | infinite continuation and volume/surface scaling | outcome law, physical rate, efficient decoder |
| powers-of-two ray | sparse-marker density and causal corridor cost | all self-similar local laws |
| Hilbert dimension count | perfect independent binary archive under composition | approximate/semantic/migratory codes |
| success-count compression | aggregate versus full corpus | which statistic Nature retains |
| fixed-cut terminal dimension and finite schedule census | once-written terminal-message pressure and finite discrete cut transcript | continuously timed channels, coherent mutable carriers, or global process laws |
| binary macrostate census | record count versus combinatorial entropy | physical thermodynamic entropy |
| multiple lapse maps | capacity does not select gravity response | whether one exact law derives a response |

No witness is used outside its resolution.

### N5 — Resolution and rhetoric audit

The finite result is theorem-grade for the named semantic branch. The front is
an existence construction, not Nature's selected law. “Can continue” is not
written as “recurs locally.” “Storage pressure” is not written as gravity.
No finite enumeration is extrapolated to all codes, QCAs, process functionals,
or global boundaries.

### N6 — Partial-closure paths

Live closures include:

1. prove an exact one-`M2`, homogeneous, collision-safe growing history law;
2. prove a migratory/topological record-identity theorem;
3. derive a global history/process functional from the nearest-neighbor rule;
4. widen Qualification with an exact recyclable working algebra and prove the
   record quotient fully abstract;
5. prove archive decoupling and recurrence for certified blocks;
6. derive an invariant resource current and its record cost; and
7. derive common clock/transport and tensor response from that same law.

The local-capacity theorem remains useful under every closure because it tells
which object is doing the recycling.

### N7 — Strongest surviving steelman

A hostile reviewer should insist that a record-only ontology need not be a
step-by-step local tape. One fixed positive global process functional can map
complete recorded intervention contexts to a consistent infinite record
history while amplitudes, virtual paths, and memory remain law-side
calculators. Apparent recurring laboratories can then be repeated relational
substructures in one global history, not a bounded Markov machine that erases
its tape. Alternatively, a topological logical record can remain permanent
while every microscopic carrier is recycled. Neither route is excluded by the
finite site-tethered theorem.

This steelman blocks the broad claim that “state is records” is incompatible
with observed recurring physics. What is established is narrower: the naive
site-addressed append implementation cannot be the entire recurrence
mechanism.

### N8 — Cross-cycle echo

- The prior capacity note proved finite saturation but allowed a recyclable
  working clock. This cycle shows that the recyclable phase sits outside the
  literal record-only/site-tethered branch.
- Cycle 22 derived clock count after event identity and left rate open. The
  growing front supplies an unbounded count, not a relative-rate theorem.
- Cycle 21 derived conditions for frequencies of an infinite certified
  corpus. This cycle prices the carrier needed for that corpus.
- Cycle 26 compiled a finite record-state one-`M2` fortress at a cost of 5,202
  sites per successful block plus debris. Repeating it indefinitely requires
  unbounded fresh support or another semantics.
- Cycles 9–11 constructed recyclable resource/export mechanisms and exposed
  their working-sector and boundary costs. Literal record-only append cannot
  silently inherit those mechanisms.
- Cycle 30 preserves the global-history/process-law steelman and explains why
  no Record amendment follows from the local capacity result alone.

Cross-cycle agreement narrows the design fork; it does not close the TOE.

## 16. Final Decision Surface

The bare-metal answer is now exact enough to guide axiom language:

```text
permanent site-local records + record-only physical state
    => finite local history capacity
    => no recurring bounded physical phase
    => infinite continuation only by growing support or nonlocal/global law.
```

Therefore:

1. do not add a generic storage-limit axiom;
2. do not make every tick, read, or microscopic interaction a permanent local
   record;
3. do not call copy/export “recycling”;
4. do not identify monotone record count with thermodynamic entropy;
5. do not infer gravity from the `1/r` surface/volume ratio; and
6. do not finalize same-site permanence until the exact law has chosen between
   site-tethered and migratory record identity.

The next constitutional question is not “how much storage does the universe
have?” It is:

> Are records the whole changing physical state, or are they the permanent
> quotient of a recyclable/global law?

The tested science favors keeping formation, renewal, boundary, rate, and
resource response in the exact law. Only after that law is known can the
minimum Record/Qualification language be made both bare-metal true and
long-run viable.

## Verification

Run:

```bash
python3 scripts/long_run_record_only_append_architecture_cycle32_2026_07_14.py
```

The PASS total contains related checks and is not an independent evidence
count.
