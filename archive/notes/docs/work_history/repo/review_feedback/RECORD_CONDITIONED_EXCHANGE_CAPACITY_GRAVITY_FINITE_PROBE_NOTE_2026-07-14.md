# Record-Conditioned Exchange Capacity And Gravity: Finite Probe

**Date:** 2026-07-14

**Type:** meta

**Scope:** exact finite diagnostic of the record-conditioned exchange-capacity
route

**Authority:** none. This note is not an axiom proposal, audit verdict,
retained theorem, empirical result, or universal obstruction. It changes no
axiom, registry, or audit surface. Its negative conclusion is a narrow no-go
for obtaining a gravitational field from the tested edge-weight rule alone.

## Question And Result

Can the promising bare-metal idea

```text
a record consumes local exchange/compute capacity
```

simultaneously explain record permanence, local clock slowing, universal
gravity, a moving source, a `1/r` field, and indefinite renewal?

The exact finite answer is sharply split.

The idea does produce a coherent microscopic candidate. If every exchange
edge incident on a recorded site is shut off, then exchange dynamics cannot
change that site's pointer value. The same rule is exactly covariant under
cubic translations and proper rotations. Its weighted degree is a natural
local throughput variable, and a common edge field gives every species the
same *fractional* throughput loss.

But the direct response is only one edge deep. It is not a `1/r` field. Its
energy effect is a change in gradient/kinetic energy, not a universal onsite
mass potential. Its sign reverses with the still-free exchange sign. An
append-only record archive leaves a trail and eventually freezes a finite
region; an active-source rule moves cleanly but no longer follows from record
permanence. A Poisson inverse does generate a nonlocal approximate `1/r`
window, but only when that inverse is supplied as a separate law.

The route therefore earns a place as a serious full-law architecture, not yet
as axiom language. It can derive post-formation stability and a local capacity
field. It does not yet derive formation, time, the equivalence principle,
attractive gravity, the field equation, or renewal.

## Exact Candidate Tested

On a periodic cubic lattice, let `S_xy` exchange the two qubits at neighboring
sites and let `F` be a set of flagged sites. The tested between-formation
generator is

```text
H_F = J sum_<xy> w_xy(F) (I - S_xy),

w_xy(F) = 1 - gamma       if x or y is flagged,
          1               otherwise,

q_x(F) = (1/6) sum_{y~x} w_xy(F).
```

`gamma=1` is hard edge freezing. `0<gamma<1` is soft capacity reduction.
`q_x` is normalized local exchange capacity; calling it a physical clock rate
is a further identification, tested explicitly rather than assumed silently.

There are two inequivalent meanings of `F`:

- `F=R`, the complete permanent record archive; or
- `F=A`, the sites currently forming/maintaining an active physical source.

The equations do not choose between them. That is the source-identity gap.

The one-excitation restriction of `I-S_xy` is exactly the graph edge
Laplacian. The finite runner therefore uses the weighted graph Laplacian for
large-torus probes and the full qubit exchange matrix for the record-sector
commutator probe.

## What The Finite Probes Establish

### 1. Hard edge freezing gives exact exchange-relative persistence

Before freezing, an incident `I-SWAP` term fails to commute with a projector
onto the site's declared pointer value. After every incident edge is removed,
the remaining exchange Hamiltonian commutes with that projector exactly.

This is a real gain: conditional on exchange being the entire allowed
between-formation operation family, a hard-frozen record cannot be changed by
later exchange.

It is not formation. Some unsupplied event must first select a content, set the
record flag, and switch the generator from `H` to `H_F`. Exchange does not
generate that state-dependent switch. The rule says what happens *after* a
record forms.

Hard freezing also blocks exchange-mediated export from that site. Soft
freezing restores transport but immediately loses exact site-value
persistence. This persistence/export tradeoff is structural in this rule, not
a tuning accident.

The bare-metal reading is consequently the reverse of “the clock locks the
record.” In this model, formation—by an as-yet-unsupplied commit—removes local
exchange channels. If `q_x` is later identified with clock rate, the lock
stops the flagged site's exchange clock. The clock did not cause the lock.

### 2. The rule is exactly cubic-covariant

Translating or properly rotating the whole flag configuration conjugates the
weighted Hamiltonian by the corresponding site permutation. Its spectrum is
unchanged and `q_x` moves with the configuration. No coordinate or preferred
site is introduced by the edge rule.

That exact statement must not be confused with moving one material source
through an append-only archive. A current active flag translates covariantly.
If every past source position remains a permanent flag, the next geometry is
the old trail plus the new position, not a translation of the one-source
geometry.

### 3. A capacity clock is available, but time and universality are not derived

For one hard-frozen site:

```text
q(record site)       = 0,
q(nearest neighbor)  = 5/6,
q(all farther sites) = 1.
```

For half-freezing, the corresponding first two values are `1/2` and `11/12`.
These are exact local throughput ratios.

If every clock species has a generator `kappa_s H_F` with the *same* weights,
then division by its unperturbed frequency removes `kappa_s`, and every
species has the same fractional slowdown `q_x`. That is a clean conditional
route to universality.

The common weight field is doing all of the equivalence-principle work.
Allowing `gamma_s` to depend on species produces different fractional
slowdowns immediately. The lattice, qubit, admissibility, and record words do
not currently force common species coupling. Nor do they say that weighted
exchange degree is the quantity measured by every physical clock.

### 4. Permanent archive and active source give different physics

Two histories with the same current active source but different permanent
archives have different archive-coupled Hamiltonians, spectra in general, and
local clocks. Under an activity-only law the two current geometries are
identical. When activity stops, the activity-only geometry returns to the
baseline; the archive-coupled geometry retains a defect forever.

Therefore a permanent record is not automatically active gravitating load.
The law must define the active source observable and its relation, if any, to
record formation and archived content. “Record-conditioned” hides this fork
unless `R` or `A` is named.

### 5. Direct edge loss is not a Newtonian field

For positive `J`, hard edge removal changes the Hamiltonian by a
negative-semidefinite sum of removed edge Laplacians. This lowers exchange
gradient energy, while a spatially uniform mode sees exactly zero shift. It is
not an onsite energy proportional to rest mass. Reversing `J` reverses this
energy effect while leaving the capacity ratios unchanged.

The direct clock deficit `1-q_x` is supported only at the flagged site and its
six neighbors. It is exactly zero at every larger distance. Hence this direct
candidate has no `1/r` far field.

A separately supplied periodic discrete Poisson equation,

```text
Delta phi = delta_source - 1/N,
```

does create a nonlocal response. On the `31^3` torus the exact Fourier solve
has machine-zero equation residual and an axial window from radius two through
nine fit by `a+b/r` with `R^2 > 0.998`. This is evidence that the cubic
substrate is compatible with the right continuum silhouette. It is not a
derivation of the Poisson equation from edge freezing.

Likewise, a resolvent `(H_F + mu^2 I)^(-1)` turns a local defect into a nonlocal
response, but its shape changes with the supplied spectral scale `mu`. A
nonlocal inverse can be useful downstream; choosing which inverse, source, and
observable it represents remains new physics.

### 6. No-renewal archive coupling saturates

As hard-frozen records are appended on a finite torus, active exchange edges
and mean capacity decrease monotonically. When all sites are recorded, the
exchange Hamiltonian and capacity clock are both zero.

Clearing the flags restores the original dynamics but violates append-only
site-tethered permanence. Retaining an immutable archive bit while clearing a
separate working flag is internally consistent, but an independent archive
bit plus working bit has four local classical labels. One `M_2(C)` site has
only two orthogonal pointer labels. The construction therefore adds a carrier,
layer, code, or nonlocal identity map.

The infinite `Z^3` lattice keeps export and fresh support alive as routes, but
hard edge freezing cannot itself transport a record across the edges it has
removed. A separate boundary/export mechanism is still required.

## Exact Gain Versus Remaining Law Atoms

| item | status in the tested model |
|---|---|
| common-basis nearest-neighbor exchange | supplied candidate law |
| exchange sign `J` and scale | supplied, not selected |
| record-to-edge map `w_xy` | supplied candidate law |
| exact record-content stability after hard freezing | derived relative to exchange-only evolution |
| formation trigger, outcome selection, and flag switch | missing |
| cubic covariance | derived |
| local capacity `q_x` | derived |
| clock identification `rate=q_x` | missing |
| active source versus permanent archive | missing |
| common species coupling / universal fractional response | supplied conditional, not derived |
| attractive gravitational sign and lapse map | missing |
| Poisson or other nonlocal field equation | missing |
| approximate `1/r` after a discrete Poisson inverse | derived conditional on that inverse |
| renewal, export, or fresh record support | missing |
| continuum metric, nonlinear self-coupling, Einstein limit | missing |

The smallest stable reference architecture exposed by this cycle is therefore
not just “records reduce capacity.” It contains at least:

```text
EXCHANGE  +  RECORD-EDGE MAP  +  FORMATION SWITCH
          +  ACTIVE-SOURCE MAP  +  CLOCK MAP
          +  COMMON-SPECIES COUPLING
          +  FIELD EQUATION / SIGN  +  RENEWAL
```

Some of these atoms may later derive from one deeper exact law. The finite
model shows that they are logically separate in the current formulation.

## TOE-Lane Consequence

| lane | exact contribution | still open |
|---|---|---|
| records | hard freezing proves exchange-relative post-formation fixation | trigger, selection, allowed-operation completeness, renewal |
| time | local dimensionless throughput ratio | why all physical clocks read it; duration and normalization |
| gravity | a covariant weighted propagation geometry; conditional universal fractional response | active stress, attraction, field equation, `1/r`, nonlinear metric dynamics |
| matter | record defects scatter/slow exchange excitations | relativistic continuum, chirality, species, mass, defect tolerance |
| probability | none | instrument, one actual outcome, weights, preparation link |
| arrow / thermodynamics | monotone loss of working capacity under append-only freezing | energy, entropy, equilibrium, low-entropy boundary, renewal |
| cosmology | a capacity-depletion variable | expansion, vacuum source, homogeneous solution, late-time renewal |

This route helps the Record, clock, matter, and gravity interfaces at once, but
does not close any of those lanes by itself.

## Constitutional Consequence

The strongest compact sentence supported by the probe is a **candidate law**,
not a Record-axiom addition:

```text
Between formations, neighboring unrecorded sites undergo the same
common-basis exchange; an edge incident on a record carries no exchange.
```

That sentence has genuine bare-metal meaning: an immutable fact occupies a
site by removing its working exchange channels. It also has genuine costs:
the exchange generator, common frame, sign, scale, hard record-edge coupling,
and site-tethered interpretation all become physical content. It freezes a
finite archive without supplying renewal, and it says nothing about the event
that first makes the record.

It should therefore be tested as verbatim theorem-import language before any
constitutional use. Adding “a record consumes local capacity” to Record now
would hide the unresolved meanings of capacity, active source, clock, species,
and renewal. Adding “the clock locks it” would reverse the actual causal order
of this candidate: the unsupplied formation switch locks the site and thereby
changes its exchange-clock capacity.

The route remains attractive for the final full-law search because one deeper
law might derive several currently separate atoms. The next decisive probe is
not further prose polish. It is to construct a local formation/renewal rule
that (i) performs the hard switch, (ii) keeps an active source distinct from
an inert archive without a discretionary label, and (iii) produces the
nonlocal universal response rather than appending a Poisson solve by hand.

## Narrow No-Go Discipline Record

The only negative claim licensed here is:

> The tested record-conditioned edge-weight rule, by itself, does not derive a
> universal Newtonian or Einstein gravitational field.

It does not claim that exchange-capacity gravity is impossible or that no
deeper local law can generate the missing maps.

### N1 — Alternative-route enumeration

1. **Hard archive-coupled freezing — ATTEMPTED, PARTIAL.** It proves
   exchange-relative record stability and local slowdown, but leaves a
   permanent history trail, has no direct far field, and saturates.
2. **Soft record weighting — ATTEMPTED, PARTIAL.** It retains transport and a
   tunable slowdown, but any nonzero incident exchange fails exact same-site
   pointer fixation.
3. **Activity-only edge weighting — ATTEMPTED, PARTIAL.** It gives clean
   moving-source covariance and no abandoned trail, but “active” is a new
   source variable not determined by permanent record content.
4. **Direct capacity deficit as the gravitational field — ATTEMPTED, RULED
   OUT for `1/r`.** Its support is exactly one edge deep.
5. **Discrete Poisson inverse of a point source — ATTEMPTED, CONDITIONAL
   SUCCESS.** It gives a nonlocal approximate `1/r` window, but the inverse,
   source, coupling, and sign are supplied.
6. **Exchange resolvent / propagator response — ATTEMPTED, PARTIAL.** It is
   nonlocal, but its profile depends on a supplied spectral/frequency scale and
   does not uniquely define gravitational potential.
7. **Effective-resistance geometry — ATTEMPTED BY REDUCTION, PARTIAL.** The
   resistance metric is built from the same Laplacian pseudoinverse as the
   Poisson route; it supplies a useful geometric observable but does not remove
   the inverse/source or clock-map atom.
8. **Separate immutable archive and recyclable working layer — ATTEMPTED,
   CONDITIONAL SUCCESS FOR RENEWAL.** It restores capacity while keeping
   content, but requires extra local states, encoded/nonlocal identity, or
   fresh support beyond one independent bit at one site.

### N2 — Wall-independence audit

The routes collapse into four independent walls:

- **formation/persistence wall:** hard freezing protects a selected value but
  does not select it or generate the flag switch;
- **source/renewal wall:** permanent archive, current activity, and recyclable
  working support are different variables;
- **gravity-map wall:** a local capacity deficit becomes a far field only
  through an additional inverse/continuum equation and sign/lapse map; and
- **universality wall:** common fractional clock response follows only when
  every species is coupled to the same weight field.

Poisson, resistance, and resolvent routes are not independent escapes from the
gravity-map wall; each introduces a nonlocal inverse. Hard and soft weighting
trade persistence against transport rather than removing that wall.

### N3 — Hidden-wall scan

The following innocent-sounding phrases would hide independent content:

- **“capacity”** does not yet mean physical time, energy, storage, or action;
- **“record-conditioned”** does not choose active source or inert archive;
- **“freezing”** does not mean attraction;
- **“moving record”** conflicts with site-tethered append-only identity unless
  it means translation of the whole configuration or migratory identity;
- **“universal slowdown”** assumes common species coupling; and
- **“the response”** assumes a field equation and observable map.

### N4 — Exact residual matching

The residual target is an exact rule that, from the framework's lawful state
alone, identifies active source, performs formation and persistence, couples
all matter clocks universally, selects an attractive response, produces the
appropriate long-range/continuum field equation, and renews or exports record
capacity. The tested rule supplies only the weighted local operator,
exchange-relative fixation after the switch, cubic covariance, and a local
throughput field.

This residual matches the missing atoms in the table above; no broader
impossibility statement is needed.

### N5 — Resolution and rhetoric audit

Resolution is finite and operator-level: cubic tori, exact permutation
covariance, exact qubit commutators, finite spectra, and a periodic Fourier
Poisson comparator. The result is diagnostic, not an empirical gravitational
calculation. “RULED OUT” is used only for the direct local deficit as a `1/r`
field. The broader exchange-capacity program remains live.

### N6 — Partial-closure path

Retain four constructive pieces:

1. symmetry-reduced `I-SWAP` exchange as the reversible working law;
2. hard incident-edge removal as an exact post-formation persistence
   mechanism;
3. normalized weighted degree as a measurable capacity candidate; and
4. the 3D lattice Poisson Green function as a downstream continuum target.

The next closure attempt should try to derive the source and inverse from the
same local renewal dynamics, rather than registering them separately.

### N7 — Strongest steelman

The strongest version of the route says that the weighted exchange graph *is*
the operational geometry: records occupy finite processing capacity, every
matter species propagates on the same graph, local throughput defines clock
rate, and the low-energy Green function of that graph produces the `1/r`
response in three dimensions. On this reading, equivalence and geometry could
emerge from one common substrate rather than being appended as separate laws.

The probes strengthen that steelman: covariance is exact, common fractional
slowdown is possible, and the cubic Poisson Green function has the correct
finite silhouette. They do not yet make it a derivation because source
identity, common coupling, sign, the inverse/low-energy selection, and renewal
remain choices. The steelman is convincing enough to block any broad no-go and
to justify the next constructive cycle.

### N8 — Cross-cycle echo

This result reproduces, at a more exact operator level, three earlier walls:

- the archive/active-load split in
  `BARE_METAL_RECORD_FORMATION_FINAL_PROBE_RESULTS_AND_AXIOM_NEED_NOTE_2026-07-13.md`;
- the finite saturation and site-tethered/migratory split in
  `RECORD_CAPACITY_RENEWAL_CONSTITUTIONAL_PRESSURE_NOTE_2026-07-14.md`; and
- the sign/scale, actuality, clock, matter, and gravity gaps in
  `QUBIT_SYMMETRY_EXCHANGE_LAW_REDUCTION_PROBE_NOTE_2026-07-14.md`.

The new information is the partial closure: hard record-conditioned exchange
does prove a precise persistence theorem, while its local clock response and
its failure to generate a direct far field are now exact rather than verbal.

## Verification

Run:

```bash
python3 scripts/record_conditioned_exchange_capacity_gravity_probe_2026_07_14.py
```

The PASS count contains related checks and is not an independent evidence
count.
