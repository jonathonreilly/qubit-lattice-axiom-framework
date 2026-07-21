# Physical relational membrane-frame reference pump — Cycle 547 (2026-07-21)

Authority: none.  Audit: unset.  Constitutional effect: none.

Runner:
`scripts/physical_relational_membrane_frame_reference_pump_cycle547_2026_07_21.py`.

## Result

Cycle 547 closes the target-dephasing defect of the Cycle-544 dynamic
Wilson-sector pump **relative to retained local reference fields**.  It keeps
three membrane-frame bits and three extracted Wilson-syndrome bits, replicates
their six signed copies on unused physical M2, and lifts every target/gauge
Pauli into the enlarged relational algebra.  The resulting branch-controlled
membrane correction exactly intertwines the full target matter algebra.  It
is target-transparent on the declared extracted-syndrome domain; it is not an
exact bare-target channel after the reference fields are erased.

The construction is one fixed physical object under all 24 proper-cubic
frames and all 576 frame products.  It uses 18 additional M2 per coarse cell,
bounded local equality/consensus rules, support-three controlled membrane
factors of physical L1 diameter at most three, no runtime frame selector, no
host parity service, no global ordering, and no postselection.  The new field
M2 have a product/reset-lawful start.  Their flood converges exactly on L5 and
held L6.

The rough-code input remains supplied.  Cycle 547 therefore does **not**
construct the full Cycle-532 rough gauge code from product inputs.  Nor does
it retire the six retained relational bits while preserving arbitrary target
coherences.  Those are explicit residuals, not hidden inside the word
“reference.”

The inherited Cycle-537 target replay retains full-Fock `Gamma(P)`, the
one-particle mass fixture, onsite Givens dynamics, contact, seam, both matter
parities, inverse, leakage, deletion, and lawful domain checks.  The runner
does not call a phase energy, a generator rate, a reset marker a Record, or
this sector transport a full product encoder.

Broad negative gate: **FAIL / DO NOT SHIP**.  The remaining boundaries do not
establish a shared substrate obstruction and create no axiom pressure.

## Exact relational intertwiner

For axis `a`, let `Q_(a,0)` and `Q_(a,1)` be the two signed Cycle-544 dual
membranes, `s_a` the extracted Wilson-syndrome bit, and `b_a` the retained
choice of signed membrane.  Define, for any matter/gauge Pauli `O`,

```text
eta_(a,0)(O) = [O,Q_(a,0)] in F2,
chi_a(O)     = eta_(a,0)(O) XOR [O,Q_(a,1)] in F2,

C = sum_(s,b) |s,b><s,b| product_a Q_(a,b_a)^s_a,

L(O) = O product_a Z(s_a)^eta_(a,0)(O)
                 product_a CZ(s_a,b_a)^chi_a(O).
```

Here `[O,Q]=1` means anticommutation.  Direct branch evaluation gives

```text
C^dagger O C = L(O)
```

on every one of the 64 `(s,b)` branches.  Because the commutation signatures
are characters, `L(O1 O2)=L(O1)L(O2)` including Pauli phase and commutation.
Thus this is an algebra intertwiner, not merely an expectation-value match.
The `CZ(s,b)` term is precisely the side-dependent target action missed when
Cycle 544 reset-averaged the two membranes.

| algebra control | L5 | held L6 |
|---|---:|---:|
| matter generators | 2,625 | 4,536 |
| gauge generators | 500 | 864 |
| all-branch truth tests | 200,000 | 345,600 |
| branch failures | 0 | 0 |
| runtime signature-linearity tests | 2,592 | 2,592 |
| linearity failures | 0 | 0 |
| maximum field factors per displayed generator | 3 | 3 |
| extra relational logical bits retained | 6 | 6 |

The last row matters.  The enlarged code is not claimed to have the exact
Cycle-537 target-times-gauge dimension after the fields are included.  The
positive statement is target-transparent **relational sector transport**.

## Physical field compiler

Cycle 527 installs a microgrid of scale 16.  For signed direction `d`, coarse
cell `x`, and its signed unit vector `D_d`, place

```text
r[frame,d,x]    = 16x + 5D_d,
r[syndrome,d,x] = 16x + 6D_d,
r[marker,d,x]   = 16x + 7D_d              (mod 16L).
```

The six copies of each kind rotate as a set.  A frame bit `b_a` is stored as
the complementary signed activation pair `(b_a,1-b_a)`, so a rotation that
flips an axis acts by site permutation rather than by changing an implicit
control polarity.  A local anti-equality constraint enforces that pair.
Syndrome copies are equal on opposite signs.  Like-directed neighboring
copies of both kinds obey equality constraints.  All constraint incidences
have routed distance at most 16.  The runner verifies that relation type as
well as coordinates is preserved under every frame.  The three kinds are
mutually collision-free and avoid every installed rough-code M2.

| layout control | L5 | held L6 |
|---|---:|---:|
| rough M2 | 2,750 | 4,752 |
| new field M2 | 2,250 | 3,888 |
| field M2 per cell | 18 | 18 |
| frame / syndrome / marker M2 | 750 each | 1,296 each |
| local field-constraint edges | 2,250 | 3,888 |
| frame opposite anti-equalities | 375 | 648 |
| frame-neighbor equalities | 750 | 1,296 |
| syndrome equalities | 1,125 | 1,944 |
| maximum equality-router distance | 16 | 16 |
| site / rough collisions | 0 / 0 | 0 / 0 |
| all-24 coordinate failures | 0 | 0 |
| all-24 constraint-relation failures | 0 | 0 |
| all-576 group failures | 0 | 0 |

This is constant overhead per coarse cell.  An equality route may contain a
constant number of nearest-neighbour M2 swaps; 16 is independent of L.

## Product/reset genesis and autonomous replication

Each complementary one-hot frame pair at the root cell is generated from
local reset randomness; all other values and all markers start reset zero.
The syndrome root values come from the Cycle-544 local routed Wilson
extraction.  A seven-cell local rule preserves a marked value or lets an
unmarked cell copy the common value of its marked nearest neighbors.
Conflicting marked neighbors are outside the declared lawful domain.  The
same isotropic rule is used for every signed direction; markers are reset and
reused after the frame flood for the syndrome flood.

The lawful local truth table has 512 cases and zero failures.  Bit-complement
covariance has zero failures.  From the root, all 125 L5 cells are reached in
six rounds and all 216 held-L6 cells in nine, exactly their maximum periodic
Manhattan radii.  Exhaustive transformation of all eight one-hot frame roots
under all 24 frames has zero legality or decoded-frame failures.  This is a
local product/reset channel with no postselection.  It is dissipative and is
not assigned a unitary inverse.  The round count is a compiler schedule, not
physical time.

Genesis is still supplied structure: a macro origin, reset randomness, an
entropy sink, and the rough-code state's three Wilson values.  The relational
orientation is generated as three random signed-pair bits rather than chosen
by a host.  It transforms with the fields, so no preferred orientation is
selected by the law.

## Bounded branch-controlled correction

At every membrane face, the syndrome and frame copies immediately adjacent
to that face control the corresponding matter/gauge Pauli factor.  Negative
faces use the equal copy in the neighboring cell across the face; this is the
nearest representative of the same relational bit.  Each primitive has
support three M2 and maximum periodic physical L1 diameter three at L5 and
held L6.  There are 150 controlled factors at L5 and 216 at L6.

The six signed membranes permute exactly under all 24 proper-cubic frames,
with zero failures.  Every one of the 9,216 frame/branch/direction control
incidences maps to the correct transformed signed control, with zero failures.
Before field dephasing/reset, the coherent controlled circuit has its reverse
dagger.  The frame and syndrome fields are then retained as part of the lawful
relational state, not discarded as leakage.  Deleting one membrane factor
produces the inherited local syndrome counts `(4,4,4)`; it is detected rather
than silently accepted.

The equality constraints and the local correction are distinct: equality
makes neighboring copies represent one bit, while correction couples only a
face and its nearest copies.  No membrane-wide classical callback occurs.

## Inherited target physics and scope

Cycle 547 replays the complete Cycle-537 certificate, not only its rank
numbers.  The local-fill factor is the Cycle-529 full-Fock target `Gamma(P)`
with the Cycle-532 gauge quotient; both matter parities remain nonempty and
share the correct center.  Mass, onsite mixing, quartic contact, seam update,
and their inverses replay.  Stabilizer commutation, target/gauge commutation,
leakage, single-factor deletion, lawful-domain, and held-size tests replay.

The intertwining identity says how these observables are represented after
the branch correction.  It does not add a new matter Hamiltonian, causal
clock, gravity/source law, Born rule, or realized-history rule.

## Supplied-structure inventory

Supplied rather than derived here:

- the Cycle-527 scale-16 microgrid and ordinary nearest-neighbour routing;
- the lawful Cycle-532 rough-code input and its target/gauge interpretation;
- the macro origin used to seed consensus;
- local reset M2, reset randomness, and an entropy sink;
- the existing Wilson extraction circuit and membrane-factor Pauli data;
- finite periodic L5 and held-L6 geometries.

Constructed and tested here:

- one fixed all-24 field placement with constant overhead;
- local equality incidences and the lawful consensus truth table;
- random relational membrane-frame genesis without a host-selected frame;
- all 64 branch identities for the full displayed matter/gauge algebra;
- the exact relational lift and bounded local controlled correction.

Not constructed:

- a product/reset encoder for the initial rough local code;
- autonomous retirement of the six relational bits while retaining arbitrary
  target coherence;
- an end-to-end recurrent physical update including field refresh/cleanup.

## No-go discipline N1–N8

### N1 — Alternative-route enumeration

1. **Retained relational membrane frame (this cycle):** constructive for
   target-transparent Wilson-sector transport; incomplete for bare-factor
   field retirement and full rough-code preparation.
2. **Reversible puncture transport:** create a local puncture/defect pair,
   carry the syndrome branch locally, close the noncontractible membrane, and
   uncompute the puncture.  Not yet attempted at physical M2 level.
3. **Non-CSS subsystem/gauge pump:** replace membrane application by local
   gauge fixing whose center selects the Wilson sector.  Not yet attempted.
4. **Finite-depth local-Clifford preparation:** synthesize the complete rough
   stabilizer state plus arbitrary target input using initialized ancillas.
   Not yet attempted.
5. **Dissipative local stabilizer pumping:** autonomously cool all local
   checks while protecting target logicals, then use this relational sector
   transport.  Not yet attempted.
6. **Erase/average the membrane side:** attempted in Cycles 535 and 544;
   falsified for target transparency because the two sides differ by target
   logical action.

The constructive result disposes only of route 6's dephasing by retaining the
missing relation.  It does not dispose of routes 2–5.

### N2 — Wall-independence audit

Two residual walls survive:

- `W_rough-encode`: prepare the entire lawful Cycle-532 rough local code from
  declared product/reset inputs while preserving arbitrary target data.
- `W_field-retire`: close or operationally interpret the six retained frame
  and syndrome bits without reintroducing target dephasing.

They are independent.  A hypothetical rough-code encoder can feed this
construction while leaving the fields retained.  Conversely, a reversible
puncture or closed relational-reference mechanism can retire the fields while
still assuming a supplied rough state.  They therefore cannot be silently
collapsed into one “nonlocality” wall.

### N3 — Hidden-wall scan

The macro origin, genesis randomness, orientation bits, membrane side,
puncture/branch data, Wilson extraction, local reset bath, rough-code input,
microgrid embedding, periodic boundary, and finite sizes are all declared.
The consensus schedule is explicit.  No host branch, parity oracle, global
Jordan–Wigner string, runtime selector, postselection, or preferred ordering
is hidden.  The root is a supplied genesis defect and not derived covariance.

### N4 — Residual matching

Cycle 535 observed target dephasing under an unrecorded signed-membrane
average.  Cycle 544 reproduced it after an exact local Wilson-sector pump.
Cycle 547 matches that residual algebraically: `chi_a(O)` is exactly the
difference between the two side actions, and the retained `CZ(s_a,b_a)`
factor cancels it branch by branch.  Cycle 537 supplies the target/gauge
factor and full physics replay; Cycle 542 supplies the physical-cap and
preparation-boundary comparison.  The new positive does not contradict the
prior negative because the missing branch relation is now an explicit
physical subsystem.

### N5 — Rhetoric audit

- “Target-transparent” means exact relational-algebra intertwining, not bare
  target invariance after tracing out fields.
- “Product/reset” applies to the new field M2, not to the supplied rough code.
- “Local” means bounded primitive support/diameter and constant per-cell
  overhead; total consensus depth and membrane count may grow with L.
- “Reference” means retained physical bits with equality constraints, not a
  host convention.
- “Inverse” applies to the coherent controlled correction before dissipative
  reset; the consensus channel itself is not invertible.
- “Lawful” excludes conflicting marked-neighbor inputs and includes the
  retained terminal fields; these are not mislabeled leakage.
- No result is called a Record, physical energy, rate, or realized history.

### N6 — Partial-closure path scan

The immediately actionable closure paths are:

1. compose a local stabilizer-pump or local-Clifford rough-code encoder with
   the present relational transport and test arbitrary target-state survival;
2. implement a reversible puncture/branch carrier and ask whether it
   uncomputes `b,s` without a membrane-wide residual;
3. retain the fields permanently and construct a recurrent update whose
   lifted target algebra evolves autonomously and covariantly;
4. reduce the 18-M2 field overhead using shared markers only after preserving
   the exact branch algebra and all-24 placement.

Any of these would be meaningful progress without a general theorem.

### N7 — Steelman

The strongest constructive rival is a local-Clifford/subsystem encoder.  A
topological code can admit local check measurements and gauge fixing even
when a particular membrane-reset realization dephases logical data.  Such an
encoder might generate the rough state and carry the Wilson syndrome through
temporary punctures, then uncompute every auxiliary.  Cycle 547 has not
implemented or excluded it.  The strongest steelman of the retained-frame
route is to regard `b,s` as legitimate relational degrees of freedom and
compile the future dynamics into `L(A)` rather than insisting that they be
erased; that recurrent closure is also untested.

### N8 — Cross-cycle echo

The repeated evidence is narrow: Cycles 535 and 544 show that forgetting a
membrane-side branch dephases target observables; Cycle 547 shows the effect
disappears when that branch is retained and locally represented.  Cycle 544's
open-chain dressing growth is a different static-gadget failure.  Neither
repetition survives the constructive alternatives above as a shared
substrate obstruction.  A general impossibility, minimum-content statement,
or axiom-pressure claim therefore remains blocked.

## Six-wall and TOE dependency update

| wall | Cycle-547 effect |
|---|---|
| `C_ref` | Advances materially: a target-transparent relational membrane-frame and Wilson-reference transport is explicit.  Genesis origin and final field interpretation remain supplied. |
| `C_num` | Not closed: six relational logical bits remain, so exact bare Cycle-537 target-times-gauge dimension is not claimed. |
| `C_wrap` | No new closure: inherited wrapped-phase/seam checks replay; no phase is called energy. |
| `C_int` | Advances conditionally: mass/contact/seam observables have exact relational lifts, but a recurrent physical update on the enlarged fields is not built. |
| `C_local` | Advances: 18 M2/cell, bounded equality routes, seven-cell consensus, and support-three diameter-three corrections are explicit.  Full rough-code product preparation remains open. |
| `C_source` | Unchanged: no autonomous gravity/resource/source law is supplied. |

Framework maturity is unchanged outside the operational/local reference lane:
operational quantum/records `3/5`, time `1/5`, inertia/matter `2/5`,
gravity/source `1/5`, Born/probability `1/5`.  The operational score is not
raised because the retained fields are not yet an autonomous recurrent Record
and the rough-code input is still supplied.

## Disposition and next campaign

Cycle 547 is a bounded constructive result worth retaining: it turns the
Cycle-544 branch-dependent correction into an exact relational compiler and
shows that the observed target dephasing was missing-reference information,
not a route-independent impossibility.

The highest-value next campaign is a reversible puncture/branch-carrier
implementation at physical M2 level, tested for exact uncomputation of the
six relational bits.  In parallel scientific order, a product/reset rough
stabilizer encoder should be attempted independently.  Only if those and the
non-CSS/local-Clifford/dissipative alternatives fail under matched contracts
would a broader locality or minimum-content claim become eligible for another
N1–N8 audit.

## Cold certificate

The final cold command was:

```text
/usr/bin/time -lp python3 \
  scripts/physical_relational_membrane_frame_reference_pump_cycle547_2026_07_21.py \
  --mode relational-frame-certificate
```

It passed `10/10` top-level tests.  Internal elapsed time was
`155.15806245803833 s`; external wall time was `156.68 s`.  Maximum RSS was
`126,009,344` bytes, with zero process swaps.  The relational L5/L6 portion
finished at `2.796574875013903 s`; the remainder was the pinned Cycle-537
full target replay.  The hard wall was 1,200 seconds.

Cold-certificate residuals were zero for field collisions, all-24 coordinate
and constraint covariance, all-576 group composition, lawful consensus,
signed one-hot frame covariance, all algebra-branch intertwining, signature
linearity, signed membrane covariance, branch-control covariance, inherited
`Gamma(P)` low/high-sector tests, inverse roundtrips, and terminal code
leakage.  Nonzero falsifier controls remained nonzero: deleting one membrane
factor produced `(4,4,4)` local syndromes, the inherited contact deletion
residual was `0.36789306705608243`, and the inherited FSWAP fourth-term
deletion residual was `1.0`.
