# Physical outward-carrier typed-prefix continuation — Cycle 485

Date: 2026-07-19
Authority: none
Audit: unset

## Result up front

Cycle 485 gives a bounded constructive advance over the exact Cycle-482
fixture.  A single actual Cycle-443 admitted basis packet is placed in cell
zero.  Every other carrier cell enters completely blank.  One fixed,
translation-local, program-free reversible update:

1. checks the current packet's twelve admission bits;
2. writes its 79-bit word and the supplied `111` occupancy/type/lock codes
   into the current archive cell;
3. copies the packet and admission fields into the next blank carrier cell;
4. activates that carrier with a `111` active triple; and
5. advances a two-rail frontier without a cyclic permutation.

On the declared finite code space this realizes, exactly,

\[
E\,G_{\rm coarse}=G_{\rm physical}\,E,
\]

with an exact inverse, zero work leakage, support at most three M2 sites, a
connected nearest-neighbour two-column router, and covariance under all 24
proper-cubic frames.  The frozen scaling law is **train L=3 / H=6 and held
L=6 / H=12**.  Train uses seven cells / 1,386 M2 and 1,335 logical gates per
tick.  Held uses thirteen cells / 2,574 M2 and 2,667 logical gates per tick.

This removes two Cycle-482 imports: future candidate words are not preloaded,
and the frontier never wraps.  The held terminal archive contains twelve exact
typed copies of the one initial packet, with one blank terminal archive cell.
A deliberately forced extra tick does not clear or overwrite any archive bit;
instead the terminal READY bit moves to the terminal MOVED rail, an explicit
out-of-code capacity syndrome.  Its inverse restores the terminal state.

The result does **not** derive renewable physical capacity.  The H blank M2
carrier blocks already exist in the initial state.  A larger initially
supplied strip supports more applications of the identical local rule, and
the held H=6 and H=12 cylinders agree bit-for-bit through six ticks, but no M2
site or blank resource is generated.  Thus the exact disposition is:

- **finite prefix preservation:** derived for H=6 and H=12;
- **conditional finite-horizon extendibility:** derived by identical-rule
  cylinder consistency on a larger supplied blank strip;
- **renewable capacity:** remains open;
- **unbounded permanence:** remains open.

A typed reversible archive prefix is not a Record.  No occurrence, realized
member, Born weight, energy/source law, reset, discarded state, host
allocation during the update, or hidden environment is introduced.  No
no-go, minimum-content, shared-obstruction, or axiom-pressure claim is made.
The runner includes an explicit nearest-neighbour M2 manifest.  Renewable
capacity remains open.  Unbounded permanence remains open.  There is no host
allocation during the update.  Norm is not probability.

Companion runner:

`scripts/physical_outward_carrier_typed_prefix_cycle485_2026_07_19.py`

## Exact target contract

| item | frozen Cycle-485 contract |
|---|---|
| Cycle-482 direct input | packaged Cycle-482 runner SHA-256 `6b6f6242b407714e65b0b34abc34db1492d2dfd0984a308735281dfad8b21fda`; packaged note SHA-256 `35715437191f944849a54d2811b8edf33d6f7b80222cb235ddca1efe7620cd1e` |
| initial physical input | one actual Cycle-443 admitted detector-11 basis packet in cell zero; all later carrier blocks exactly blank |
| attempted mechanism | translation-local outward carrier with separate READY and MOVED frontier rails |
| train / held | train L=3 / H=6; held L=6 / H=12, with H=2L frozen before held evaluation |
| required bridge | exact E/G and inverse on every tested nonterminal lawful basis-prefix state |
| physical locality | bounded 198-M2 cell; one-cell or adjacent two-cell patch; connected nearest-neighbour routed X/CNOT/Toffoli; support at most three |
| covariance | all 24 proper-cubic frames, train and held, 48 rows |
| required controls | repeated continuation, held-size/cylinder consistency, terminal forcing, deletion, malformed-domain, coherent-input, resource, and cold-run limits |
| excluded outputs | framework Record, occurrence, permanence, realized history, probability, source/energy, physical carrier genesis, reset, erasure, environment, or host allocation |
| authority / audit | none / unset |

The direct source is Cycle 482 because the scientific question is whether its
typed prefix can continue without its preloaded future tape and cyclic head.
Cycles 359 and 452 are bounded reconnaissance for blank-line continuation and
explicit finite resource motion.  They are not silently imported as direct
laws.  No Thirring engine is used or compared.

## Construction

### One translation-equivalent cell

Each cell contains 198 M2 sites:

| field | M2 |
|---|---:|
| READY frontier rail | 1 |
| MOVED frontier rail | 1 |
| packet inbox | 79 |
| admission inbox | 12 |
| carrier-active code | 3 |
| archive packet | 79 |
| archive occupancy/type/lock | 9 |
| admission prefix work | 12 |
| accept prefix work | 2 |
| total | **198** |

READY is at local coordinate `(0,0)`, MOVED at `(0,1)`, and the remaining
196 sites form a vertical line.  Adjacent cells sit at consecutive horizontal
coordinates.  A local gate routes on one vertical column.  A link gate routes
on a fixed serpentine path down one column, across one horizontal edge, and
back along the adjacent column.  All routing swaps are undone.

The geometry has constant overhead independent of H.  A one-cell route has
197 physical sites and an adjacent-link route 394; these constants are large
but bounded.  This is a constructive locality theorem, not an efficiency
claim.

### Fixed link rule

For every link `i -> i+1`, whether or not it currently carries the frontier,
the schedule contains the same 210 logical gates:

| block | gates |
|---|---:|
| admission conjunction | 12 |
| READY-and-admission accept conjunction | 2 |
| archive packet write | 79 |
| archive occupancy/type/lock write | 9 |
| next packet propagation | 79 |
| next admission propagation | 12 |
| next-carrier activation | 3 |
| accept uncompute | 2 |
| admission uncompute | 12 |
| total | **210** |

All writes are reversible controlled XORs into declared blank targets.  The
packet in the current inbox is retained.  Admission/accept work returns to
zero.  The schedule never inspects a host-side law selector and has no
law-program, occurrence, reset, realized-member, allocation, or environment
service field.

### Non-cyclic frontier transport

One abstract disjoint transport swaps `READY_i` with `MOVED_(i+1)`.  Its NN
implementation uses `READY_(i+1)` only as a restored bridge:

```text
SWAP(READY_i, READY_(i+1))
SWAP(READY_(i+1), MOVED_(i+1))
SWAP(READY_i, READY_(i+1))
```

Every SWAP is three adjacent CNOTs.  A final local
`SWAP(MOVED_i, READY_i)` converts the transported marker to the READY rail.
The full gate count is therefore

\[
210H+9H+3(H+1)=222H+3.
\]

There is no terminal-to-origin edge.  At the boundary, an extra forced update
therefore produces the visible MOVED syndrome rather than wraparound.

## Exact code and theorem

For frontier position `k`, the lawful basis-prefix code requires:

- exactly one READY bit, at cell k, and every MOVED bit blank;
- cells `0..k` carry the same admitted packet and active triple;
- cells `0..k-1` contain exact typed archive copies;
- cells `k..H` have blank archives;
- cells `k+1..H` are entirely dormant and blank in packet/admission/active
  fields; and
- all prefix work is blank.

For `k < H`, the fixed schedule has exactly one lawful successor.  Direct bit
comparison gives zero residual between the physical update and the coarse
map.  Reversing the complete primitive list restores every input and resource
M2.  Induction over the tested finite history gives an exact typed prefix of
length k after k steps.

This is the strongest bounded theorem supported by the probe:

> Given one supplied actual Cycle-443 admitted basis packet, the supplied code
> meanings/cadence/frame convention, and H supplied blank 198-M2 carrier
> cells, a single translation-local reversible proper-cubic family derives H
> future packet copies and preserves an exact no-wrap typed archive prefix for
> H applications, with constant physical overhead per cell/link, exact inverse,
> and no host allocation during those applications.

The theorem quantifies over the declared finite H fixtures tested here.  The
H=6/H=12 shared-cylinder result supports, but does not itself prove, an
infinite quasi-local theorem.

## Exact results and residuals

### Bridge and physical compilation

| case | source L | H | cells | M2 | logical gates/tick | routed NN primitives/tick | E/G bit residual | inverse | work leakage |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| train | 3 | 6 | 7 | 1,386 | 1,335 | 2,702,631 | 0 | exact | 0 |
| held | 6 | 12 | 13 | 2,574 | 2,667 | 5,405,259 | 0 | exact | 0 |

Router trace SHA-256 values are
`518bcec6ee7510398556542b0233761bd17739413fc8959f6369c6e21e8b6386`
for train and
`55316857b94634bcef796bc6f88cbf140bc2689ad2c2ff3893df835a1b1267c5`
for held.  Maximum logical support is three; connected failures are zero.
The held NN-compiled state equals the logical state bit-for-bit.

### Repeated continuation and held-size control

- Train step E/G residuals: `(0,0,0,0,0,0)`.
- Held step E/G residuals:
  `(0,0,0,0,0,0,0,0,0,0,0,0)`.
- Train terminal typed-prefix length: 6; terminal archive blank: yes.
- Held terminal typed-prefix length: 12; terminal archive blank: yes.
- Full train and held history inverse: exact.
- Future candidate packets initially preloaded: zero.
- Identical held-packet H=6 versus H=12 shared seven-cell residuals through
  six ticks: `(0,0,0,0,0,0,0)`.
- Link-template gate counts across all twelve held links: 210 each.

The held fixture doubles Cycle 482's six-step held prefix without refitting a
content word, gate template, type code, or schedule.  The only increased input
is the explicitly counted blank physical strip.

### Boundary and resource control

After held H=12, a forced thirteenth application has:

- archive bit residual from the terminal archive: 0;
- READY population: 0;
- terminal MOVED bit: 1 and total MOVED population: 1;
- exact inverse back to the terminal lawful state;
- one initially supplied packet;
- twelve initially supplied completely blank carrier cells;
- host allocation calls during the update: 0;
- reset/discard operations: 0; and
- hidden-environment M2: 0.

This explicit syndrome is the lawful-domain boundary.  It is not a new
dynamical carrier, and it is not counted as renewable capacity.

### Covariance, deletion, malformed domain, and coherent input

- All 24 proper-cubic frames times train/held give 48/0 exact covariance rows,
  each using the actual frame-rotated Cycle-443 producer packet and rotated
  carrier geometry.
- Admission-prefix, accept, archive-payload, propagation-payload,
  active-carrier, head-transport, and head-conversion deletions are each
  visible and rejected by the lawful code.
- Short packet, zero/two READY, dirty MOVED, bad root active code, dirty
  dormant packet/admission/archive, and dirty work inputs are refused.
- A coherent two-packet input remains support two, has inverse-vector residual
  zero to floating precision, and norm residual below `1e-12`.

Norm preservation is not probability, and no realized member is selected.

### Final runner tally and resource envelope

An independent cold root execution reports **13 pass / 0 fail**.  The
instrumented probe body takes `110.08817295904737 s` against a `360 s` wall cap
and reaches `780,369,920` peak RSS bytes against a
`2,147,483,648`-byte cap.  Complete cold-process timing is `202.34 s` real,
`195.98 s` user, and `3.00 s` system, with the same `780,369,920`-byte maximum
RSS.  Python dependency import occurs before the runner's internal timer is
installed, so the complete cold-process figure is the conservative execution
envelope.  The packaged runner SHA-256 is
`050c979de0f27073815309ad67635997f5c54b3344734b36e4f7fb3ab80ded7c`.

## Cycle-482 comparison

| dependency | Cycle 482 | Cycle 485 |
|---|---|---|
| initial candidate content | one admitted packet in every finite tape cell | one admitted packet only at cell zero |
| later candidate words | supplied | derived by local propagation |
| frontier | cyclic one-hot rail | two-rail outward frontier with no terminal-origin edge |
| tested held prefix | 6 | 12 |
| forced boundary behavior | second lap clears archive and cycles to initial | archive unchanged; terminal MOVED syndrome leaves code |
| host action during run | none | none |
| physical capacity | finite supplied tape | finite supplied blank carrier strip |
| actual capacity renewal | not derived | not derived |
| unbounded permanence | not derived | not derived |

The advance is therefore genuine but narrow: Cycle 485 derives future content
and removes cyclic overwrite.  It does not convert a finite supplied M2 strip
into a renewable substrate.

## Supplied / derived / open

### Supplied

1. one actual Cycle-443 admitted detector-11 basis packet at cell zero;
2. H initially blank physical carrier cells and their terminal boundary;
3. basis, admission, occupancy, type, lock, and active-carrier code meanings;
4. the fixed update cadence and the train/held test law H=2L; and
5. the proper-cubic frame convention and M2 primitive interpretation.

### Derived

1. every future packet/admission field from the single initial packet;
2. one unique nonterminal append successor per lawful basis state;
3. exact `E G_coarse = G_physical E` and exact inverse;
4. train H=6 and held H=12 typed-prefix preservation;
5. no cyclic overwrite and an explicit terminal capacity syndrome;
6. translation-local constant cell/link overhead and all-24 covariance; and
7. held H=6/H=12 finite-cylinder consistency without parameter refit.

### Open

1. genesis or renewal of physical M2 sites and blank carriers;
2. an infinite-volume or all-time prefix theorem;
3. lawful framework Record formation, occurrence, and permanence;
4. independent event provenance and realized-member selection;
5. Born weights or probability; and
6. energy/source/thermodynamic cost of capacity and persistence.

## Dependency effect

| wall | Cycle-485 movement | still open |
|---|---|---|
| `C_ref` | bounded advance: one admitted packet now produces and preserves a longer exact typed physical prefix without preloaded future words or wrap | Record occurrence, lawful typing/actualization, permanence, independent provenance, realized-member selection |
| `C_num` | unchanged | amplitude-to-frequency/count bridge, Born rule, continuum/error control |
| `C_wrap` | small conditional advance: an ordered local append depth can extend outward on supplied capacity | physical time unit/rate, synchronization, proper-time and OS/Z4 bridge |
| `C_int` | unchanged | interaction-generated occurrence/source content and cross-lane close |
| `C_local` | material implementation advance: fixed adjacent-cell rule, constant block overhead, exact NN routing, all 24 frames, no cyclic parity/order service | physical capacity genesis/renewal, thermodynamic accounting, infinite-volume law |
| `C_source` | unchanged | energy/stress/source/lapse/metric law and resource accounting |

No maturity score changes are warranted from this bounded implementation
advance alone.  The operational quantum/Records lane gets stronger evidence
inside its current rounded score, while time, inertia/matter, gravity/source,
and Born/probability remain unchanged.

## No-Go Discipline

Full N1-N8 is applied because phrases such as “renewable capacity is not
derived” can otherwise be inflated into impossibility or axiom pressure.

### N1 — alternative route enumeration

| route | status | disposition |
|---|---|---|
| cyclic fixed-capacity tape | **ATTEMPTED** | Cycle 482 is positive through H; forced recurrence exposes its boundary |
| outward blank-carrier activation | **ATTEMPTED** | Cycle 485 is a finite no-wrap positive; the blank ray is supplied |
| explicit finite reset sink | **ATTEMPTED PRIOR** | Cycle 452 makes reset data/resource motion explicit; sink renewal remains open |
| one-root blank-line continuation | **ATTEMPTED PRIOR** | Cycle 359 constructs finite successors; repeated program/formation/cap imports remain |
| dynamical carrier-pair creation | **OPEN / UNTESTED** | must preserve M2 accounting and retain inverse information |
| infinite quasi-local carrier algebra | **OPEN / UNTESTED** | could define consistent all-finite-cylinder dynamics without a finite terminal cap |
| Record-typed absorbing sector | **OPEN / UNTESTED** | could use existing permanence authority after lawful formation/typing |

Several positive and open routes exclude a universal negative conclusion.

### N2 — wall-independence audit

The collapsed walls are `W_prefix` (finite exact continuation), `W_capacity`
(fresh physical room), `W_form` (lawful Record formation), `W_permanence`
(all-time protection after formation), and `W_resource` (source/cost accounting).
All ten pairs remain distinct: a finite prefix does not create capacity;
capacity does not select a lawful occurrence; formation does not specify an
energy/source account; source accounting does not guarantee permanence; and
permanence authority does not by itself construct blank M2 sites.  No pair is
collapsed to manufacture a shared obstruction.

### N3 — hidden-condition scan

The basis packet and admission meanings, type/lock/active meanings, cadence,
blank-carrier geometry, terminal boundary, proper-cubic frame convention, and
H=2L finite scaling law are all supplied.  “Outward,” “blank,” and “active”
are physical code descriptions, not resource-genesis claims.

### N4 — residual matching

| cycle | retained positive | matching residual |
|---|---|---|
| 359 | one-root propagation on a finite blank line | program, enable, cap, occurrence |
| 452 | finite local ratchet and explicit reset export | renewable sink/capacity and lawful typing |
| 482 | deterministic typed prefix through fixed H | preloaded future tape and cyclic recurrence |
| 485 | future words derived; no wrap through held H12 | blank physical ray supplied; actual renewal and permanence open |

The residuals match rather than contradict one another.

### N5 — rhetoric audit

| phrase | licensed meaning | forbidden inflation |
|---|---|---|
| outward-growing | a frontier advances on a pre-existing finite strip | creation of M2 sites |
| conditional extension | a larger supplied strip supports more identical local steps | self-renewing capacity |
| typed archive | reversible physical code carrying supplied `111` meanings | framework Record |
| no overwrite through H | every tested prefix bit is retained for H steps | all-time permanence |

A typed prefix is not a Record.  No universal “cannot” is asserted.

### N6 — partial-closure paths

Live paths include larger finite cylinders with the identical rule; an
infinite quasi-local cylinder theorem; explicit carrier-pair genesis with
conserved inverse data; lawful Record typing followed by the existing
permanence clause; and a renewable sink/resource lane with explicit source
accounting.

### N7 — steelman

A translation-invariant quasi-local algebra can define one rule on an infinite
carrier ray.  Every finite prefix might then stabilize with no per-tick host
action.  Cycle 485's exact H=6/H=12 cylinder agreement is compatible with that
route and does not refute it.  Likewise, a physical carrier-production law
could explicitly retain its inverse data and resource source.  Neither route
has been attempted here.

### N8 — cross-cycle echo

Cycle 359's finite blank-line cap, Cycle 452's finite receipt/reset-sink
boundary, Cycle 482's cyclic recurrence, and Cycle 485's terminal MOVED
syndrome all expose finite resource boundaries in different constructions.
That echo motivates the next constructive lane but is not route-independent
constitutional evidence.

**Gate disposition: FAIL — partial-attempt-with-named-untested-routes.**  The
bounded positive theorem ships.  No no-go, minimum-content, shared-obstruction,
or axiom-pressure claim ships.

## Optimal next campaign

The next high-value constructive target is the distinction Cycle 485 makes
visible: attempt either an infinite quasi-local cylinder theorem for this
exact rule or a finite local carrier-pair genesis/renewal circuit with explicit
inverse-data and source accounting.  The first can test whether the terminal
cap is merely a finite-fixture artifact; the second can test genuine physical
renewal.  Neither should be called Record permanence until lawful formation
and the existing permanence clause are separately connected.
