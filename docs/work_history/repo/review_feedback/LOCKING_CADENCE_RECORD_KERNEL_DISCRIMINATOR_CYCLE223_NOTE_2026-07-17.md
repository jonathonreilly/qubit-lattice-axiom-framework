# Read/reset-cadence channel discriminator — Cycle 223

**Date:** 2026-07-17

**Status:** bounded channel discriminator; audit unset

**Authority:** none

**Constitutional effect:** none

**Packaging:** existing draft parking branch and draft PR #5389 only

Companion runner:

```text
scripts/locking_cadence_record_kernel_discriminator_cycle223_2026_07_17.py
```

## Result up front

This cycle asks a deliberately narrow question of the supplied Cycle-222
proper-cubic candidate update: what happens if a read, a redundant pointer
copy, or a clock tick is modeled as a read/reset intervention in one declared
rank-one frame?

The exact answer is that pointer correlation, redundant copying, and
irreversible commitment are three different operations. One and two coherent
pointer copies induce the same reduced channel. The second copy changes which
systems must be accessed to erase the correlation; it does not make the
modeled joint state irreversible. An operational erasure barrier additionally
requires a supplied access or continuation restriction. The separately
supplied nonselective dephasing channel is one sufficient reduced model of
that barrier, not a physical Record or fundamental global irreversibility.

Conditional on that supplied intervention, cadence is operationally
consequential in this protocol. Every fixed cadence defines its own Markov
kernel after a rank-one reset is supplied, but the kernels do not form one
cadence-independent Chapman–Kolmogorov family. A rank-one read/reset after
every tick is exactly blind to the diagonal force phase used by Cycle 222 to
measure inertia. Coherence must survive across multiple paths before that
force becomes visible.

This is a bounded positive channel result, not a broad record-only no-go. It
does not derive a clock, does not derive a Record, does not select an outcome,
and does not support an axiom conclusion.

## Exact channel statement

For the supplied unitary `U`, declared rank-one projectors `R_a`, and
dephasing map

```text
D_B(X) = sum_a R_a X R_a,
```

define the one-read weights after `k` coherent updates by

```text
K_k[a,b] = |<a|U^k|b>|^2.
```

Every `K_k` is entrywise nonnegative and doubly stochastic. It is an exact
transition kernel only after the rank-one pointer frame, squared-modulus rule,
selective read/reset semantics, and cadence have been supplied. The difference
between one read after `m+n` updates and a read after each interval is

```text
channel_defect_mn
  = D_B Ad_(U^m) (I-D_B) Ad_(U^n) D_B,

Delta_mn = K_(m+n) - K_m K_n.
```

On diagonal inputs, `Delta_mn` is the diagonal matrix representation of the
displayed channel defect. Entry by entry it is exactly the sum of the
interference cross terms between distinct intermediate paths. Here the
`n`-update interval acts first and the `m`-update interval acts second, so the
incoherent schedule is `K_m K_n`. A seeded Haar unitary whose induced `K_2`
and `K_3` kernels do not commute fixes this order independently of the
structured Cycle-222 blocks. The runner
checks that identity to `1.7e-15` and checks that every defect has zero row and
column sum.

For one fixed pair of intervals, those cross terms can cancel accidentally.
For every pair and every duration, closure holds exactly if `U` is monomial in
the declared pointer basis: a permutation with phases.  The forward direction
is immediate.  Conversely, all-time closure gives `K_t=K_1^t`.  Finite-unitary
recurrence supplies a subsequence `U^t -> I`, hence `K_1^t -> I`; the
determinant and equality case of the Hadamard bound then force the doubly
stochastic `K_1` to be a permutation.  This elementary statement is not
claimed as literature-new.

For each Cycle-222 massive direction block, up to a global phase,

```text
C_beta^t = P_scalar + (-1)^t P_even + exp(i t beta) P_vector,
```

and therefore

```text
|C_beta^t|^2 = P_scalar + e_t P_even + v_t P_vector,

e_t = 1                  for t even,
      1/3                for t odd,

v_t = cos(t beta)        for t even,
      -cos(t beta)/3     for t odd.
```

The runner verifies this closed form through twelve updates in all three
blocks to `7.3e-14`.  In particular, two odd intervals always leave an
`8/9 P_even` defect, so no odd-plus-odd pair closes this kernel.

## Cadence is consequential in the supplied intervention protocol

At a common total duration of sixteen updates, the requested cadence sweep
gives the following maximum-column total variation relative to one final-only
diagnostic. “Final only” means that no intermediate read/reset is applied; a
final diagnostic is still needed to compare diagonal weights.

| `C3` character | `k=1` | `k=2` | `k=4` | `k=8` | final only |
|---:|---:|---:|---:|---:|---:|
| `-2 pi/3` | 0.666667 | 0.241831 | 0.206571 | 0.139615 | 0 |
| `0` | 0.832237 | 0.000959 | 0.000822 | 0.000548 | 0 |
| `+2 pi/3` | 0.666667 | 0.283306 | 0.165732 | 0.322644 | 0 |

The near-closure of some even cadences in the `C3=0` sector is a useful
control: one favorable cadence or state does not establish one Markov law.
The direction-frame `m=n=1` defects are large in all three sectors, with
maximum-column total variations `0.736`, `0.741`, and `0.671`.  In the coin's
eigenbasis every defect vanishes because the kernel is the identity. Thus the
declared projector-valued instrument is operational input, not passive
notation. Monomial relabeling/rephasing preserves the result, and
co-transforming states and projectors under a passive register-basis change
preserves the isolated register-dephasing experiment.

## One pointer, two pointers, and a modeled archive

For one binary mass-sector projector `P`, the controlled pointer write and
copy are

```text
W_1 = (I-P) tensor I + P tensor X,
W_2: |a>|0> -> |a>|a>.
```

An equal two-sector superposition gives the following exact controls. The
two-pointer state is produced both by copying pointer one and by two direct
system-conditioned writes to abstract pointer factors; the states agree
exactly. This does not establish nearest-neighbour generation, causal
independence, or physical witness disjointness.

| construction | reduced-system purity | retained joint-state purity | recovery test |
|---|---:|---:|---|
| one coherent pointer | 0.5 | 1 | pointer inverse restores the state with fidelity 1 |
| two coherent pointers | 0.5 | 1 | reversing the first modeled write while leaving the second pointer untouched leaves reduced purity 0.5; reversing both modeled writes restores fidelity 1 |
| two pointers plus explicit archive/dephase | 0.5 | 0.5 | pointer reversal alone leaves reduced purity 0.5 |

One and two coherent pointer copies induce the same reduced channel.  The
second copy increases erasure redundancy; it does not produce a second
decoherence event, a selected branch, or fundamental irreversibility.  The
matter-mass expectation is identical with zero, one, and two coherent pointer
copies or writes. Only the separately supplied nonselective archive reduces
purity of the retained modeled pointer-history density state. A larger unitary
dilation may retain coherence in an unmodeled environment, so no global
irreversibility is claimed.

This separates an abstract pointer copy from a Record. A coherent pointer can
carry outcome-correlated information while the joint state remains
reversible. The two abstract pointer factors have not been shown to be
spatially disjoint, independently produced nearest-neighbor witnesses. A
permanent realized Record additionally needs an occurrence/selection rule and
a lawful continuation restriction; neither is generated here.

## What per-tick supplied read/reset does to mass

The symmetric fixed-force update has the form

```text
U_f = D_(f/2) U D_(f/2),
```

where `D_f` is diagonal in the declared mass-position-direction frame.
Consequently

```text
|D_left U D_right|^2 = |U|^2
```

exactly.  Per-tick read/reset is therefore exactly blind to `+f`, `0`, and `-f`.
The finite full-walk test agrees below `1.4e-15`, giving zero odd force
response and no finite `F/a` inertia. At three coherent ticks before the next
read/reset,
the central-source forced/unforced differences are `0.000129`, `0.0000238`,
and `0.00122` in Frobenius norm for the three `C3` sectors.  They are unchanged
when the periodic box grows from 13 to 17 sites, so the signal is not supplied
by the boundary discontinuity.  The two-tick cancellation in this fixture is
explicitly not promoted to a theorem.

The per-tick direction kernel instead gives diffusion.  Its exact coefficient
is

```text
lambda = -cos(beta)/3 = (m^2-9) / (3 (m^2+9)),
D = (1/6) (1+lambda)/(1-lambda)
  = (2 m^2+9) / (6 (m^2+18)).
```

| `C3` character | phase-mass coordinate | diffusion coefficient |
|---:|---:|---:|
| `-2 pi/3` | 86.181343 | 0.332729 |
| `0` | 1449.401859 | 0.333331 |
| `+2 pi/3` | 0.416797 | 0.085723 |

The numerical tilted-kernel extraction agrees within `6.3e-6` relative.  The
kernel loses the rest phase and the sign of the phase-mass coordinate, and it
compresses the large hierarchy toward `D=1/3`.  It still contains a supplied
invertible function of `|m|`; the result is not a proof that every mass trace
is lost.  It shows that the coherent rest/dispersion/inertia contract is not
inherited by per-tick read/reset.

## Phase, coarse symbols, and target-unfed baseline

One common geometry-fixed tester is used in every massive block: one update
from the opposite `+x/-x` direction pair, with relative phases `0`, `pi/2`,
and `pi`. The three states have identical diagonal weights; in every sector
their largest pairwise coherent-future separation is exactly `8/9`. The rank-one kernel
assigns all three exactly the same future. These are legal vectors in the
supplied working space, but common lawful preparation from one complete
physical record corpus and a physical output Record remain unproved. The test
therefore advances but does not close Cycle 200.

A coarser mass-position symbol is not Markov sufficient either: two states
with the same mass and position but different hidden directions produce next
position distributions separated by `0.321` to `0.333` in total variation.
That can be repaired by retaining direction/phase/history or by supplying a
reset; the test identifies the missing state, not a universal obstruction.

As a target-unfed program-order control, the three sectors are first selected
only by their `C3` characters. Dispersion and fixed-force inertia are measured from
the extracted blocks in a function that receives no mass operator. A separate
function later compares the frozen rows with `M`:

| `C3` | unblinded `M` | dispersion | inertia, windows 128–192 |
|---:|---:|---:|---:|
| `-2 pi/3` | 86.181343 | 86.181279 | 86.180381–86.180537 |
| `0` | 1449.401859 | 1449.400736 | 1449.380259–1449.386752 |
| `+2 pi/3` | 0.416797 | 0.416813 | 0.416779–0.417318 |

Three curvature steps, three force strengths, both force signs, and three time
windows remain within `0.122%`; norm, band-retention, boundary, and
force-even-contamination controls pass.  Only after those rows are frozen are
they unblinded against `M`.  The
coherent mass bridge therefore survives without a target-mass lookup in the
measurement, while per-tick read/reset demonstrably does not inherit it. This
is structural target-unfed execution, not an epistemically blinded experiment.

## Bare-metal interpretation

- **A read is not yet a commit:** the tested bare-metal sequence has four distinct stages:
  an available possibility, a reversible outcome-correlation, redundant
  pointer correlation, and a separately supplied access/commit barrier. Even
  that fourth stage does not choose which outcome occurs.
- **A second copy is not a commit:** a second coherent copy raises the erasure
  burden but does not by itself produce irreversibility or actuality. Calling
  the abstract copies independent physical witnesses would add untested
  geometry, nearest-neighbor production, and conditional independence.
- **Every-tick reset is not a derived clock:** making every background tick a read/reset removes the
  tested inertial response. A different schedule is extra law/protocol content and
  can be observable, although fixed cadences can accidentally coincide. The
  one live route is for formation events to determine when a commit occurs,
  with a clock potentially counting those events afterward—not for an
  unexplained cadence to cause every commit.

The last sentence is the next construction target, not an axiom proposal or a
derived theorem about nature.

## Supplied diagnostic structure

The construction supplies all of the following:

- the Cycle-222 unitary and its 24-dimensional register-direction space;
- a rank-one mass-position-direction frame as the diagnostic pointer frame;
- squared-modulus weights for that frame;
- blank pointer factors and a controlled write/copy;
- a separately supplied nonselective dephasing channel modeled as an archive;
- an inaccessible-history restriction after archival;
- a rank-one reset/repreparation after each selected intervention, or repeated
  nonselective dephasing when only ensemble marginals are retained;
- the number of coherent updates between read/resets;
- a one-axis periodic box and the existing coordinate-kick force law; and
- coherent packet preparation.

The rank-one mass-position-direction frame is supplied; it is not identified
with the framework's physical Record frame. Squared-modulus weights are
supplied; no Born-rule or frequency derivation is claimed. A nonselective
archive state is still not one selected trajectory or realized branch.

Cycle 223 inherits every conditional input and scope wall in its branch-local,
unaudited predecessor chain:

- [Cycle 219 common matter/field coin](./COMMON_MATTER_FIELD_COIN_FAMILY_CYCLE219_NOTE_2026-07-16.md);
- [Cycle 220 generated beta-phase register](./GENERATED_BETA_PHASE_REGISTER_CYCLE220_NOTE_2026-07-16.md);
- [Cycle 221 operator-mass equivalence](./OPERATOR_MASS_EQUIVALENCE_CYCLE221_NOTE_2026-07-17.md); and
- [Cycle 222 conditional mass compiler](./CONDITIONAL_FLAVOR_MASS_OPERATOR_COMPILER_CYCLE222_NOTE_2026-07-17.md).

In particular, this cycle does not promote the supplied coin family, register
seed/population, inverse-Cayley compiler, force profile, or Green/source vertex
to origin authority or a retained law.

## Cross-lane effect

### O — operational quantum

The one/two-pointer/archive split is exact, and the same-diagonal phase-fibre
witness directly exposes what a rank-one reset kernel deletes.  Physical
record formation, a common reachable preparation history, selection, and
frequency remain open.

### T — time

Read/reset cadence is extra operational content and changes outcomes in this
protocol. A background tick cannot be identified with a commit for free. A
clock may count formation events, but no trigger, formation rate, comparison
law, or time normalization has been derived.

### I — matter

The target-unfed coherent baseline preserves the Cycle-222
dispersion/inertia/operator agreement. Per-tick read/reset converts the tested
motion to diffusion and eliminates the tested force response. This favors
coherent intervals or a richer record/history state for this fixture; it does
not select a universal matter ontology. The `1/2/4/8/final-only` sweep is
complete for the population channel, but full dispersion, inertia, and force
transport have not yet been rerun at every cadence.

### G — gravity

The same phase-gradient response used by the conditional source lane requires
coherent paths between read/resets. No autonomous source, tensor geometry,
nonlinear field equation, or record-energy ledger is added.

### B — boundary/history

Fresh append-only archive factors, their blank preparation, their capacity,
and their accessibility are physical inputs.  A mutable current-label kernel
is not yet a permanent record history or a cosmological boundary condition.

## Re-ranked next target

The optimum continuation is an endogenous sparse-formation tournament.  Use
one fixed local trigger derived from the evolving candidate state—rather than
a scanned external cadence—to choose rare archive events, then rerun the
phase-fibre, dispersion, force, redundancy, reachability, and history-capacity
controls.  In parallel, test whether a finite record-derived decoder or
history state can retain exactly the phase information the rank-one kernel
loses.  This directly discriminates “formation events make the clock” from
“the clock causes formation.”

## No-Go Discipline Gate — FAIL

The broad claim “record-only physics cannot reproduce the Cycle-222 result”
has status **FAIL — partial attempt with named untested routes** and is not
shipped. Only the bounded positive channel identities above are carried
forward.

### N1 — alternative routes

| route | status | evidence and unresolved part |
|---|---|---|
| explicit coherent working sector | **ATTEMPTED** | Cycle 223 preserves the Cycle-222 mass bridge between interventions; its ontology and preparation are supplied |
| direct global history/process law | **LIVE — PRIOR PARTIAL ATTEMPT** | [Cycle 30](./GLOBAL_RECORD_HISTORY_PROCESS_LAW_CYCLE30_NOTE_2026-07-14.md) closes finite Bell/interference/process consistency, but not homogeneous nearest-neighbor generation |
| record-derived coherent decoder | **LIVE — PRIOR PARTIAL ATTEMPT** | [Cycle 48](./RECORD_DERIVED_COHERENT_CARRIER_DECODER_CYCLE48_NOTE_2026-07-14.md) closes a finite stabilizer grammar; arbitrary non-Clifford state and unbounded-reference closure remain open |
| sparse causal-close commit | **LIVE — PRIOR PARTIAL ATTEMPT** | [Cycle 16](./DELAYED_LOCKING_CAUSAL_CLOSE_CYCLE16_NOTE_2026-07-14.md) generates a bounded local close; an endogenous trigger for the present mass process remains untested |
| append-only growing history | **LIVE — PRIOR PARTIAL ATTEMPT** | [Cycle 32](./LONG_RUN_RECORD_ONLY_APPEND_ARCHITECTURE_CYCLE32_NOTE_2026-07-14.md) permits an expanding tape but proves a fixed finite certification region exhausts its fresh sites |
| reversible export/fresh carrier dilation | **LIVE — PRIOR PARTIAL ATTEMPT** | [Cycle 11](./INFINITE_REVERSIBLE_RECORD_EXPORT_QCA_CYCLE11_NOTE_2026-07-14.md) supplies an exact dilation and exposes rather than removes the access/fresh-resource wall |
| relational pointer selected by interaction | **LIVE — PRIOR PARTIAL ATTEMPT** | [relational pointer Cycle 16](./RELATIONAL_POINTER_CONTEXT_SELECTION_CYCLE16_NOTE_2026-07-14.md) selects a pointer axis conditional on a supplied exact interaction; it does not select that interaction |

The skill permits only `ATTEMPTED` for a route tested in Cycle 223 or `RULED
OUT BY PRIOR` for one closed by retained authority. Six rows satisfy neither:
they are live prior partial attempts. That honesty-marker failure is itself an
N1 failure, so the broad no-go cannot ship. The next campaign directly tests
the sparse-trigger and record-derived-history rows.

### N2 — wall independence

The raw inputs are first collapsed into six operationally meaningful walls:

- `W_L`: the supplied Cycle-222 candidate law, mass compiler, and kick;
- `W_I`: the supplied instrument package—frame, squared-modulus weights, and
  reset/repreparation semantics;
- `W_C`: the supplied intervention schedule and absent endogenous trigger/rate;
- `W_R`: the absent Record commit package—occurrence, selection, access
  restriction, and permanence;
- `W_P`: physical/local implementation, including spatially disjoint and
  independently produced witnesses; and
- `W_H`: repeated append-only history, blank carriers, capacity, and cost.

The frame, weights, and reset are bundled in `W_I` because all three are
needed before `K_t` is the tested intervention kernel. Occurrence, access, and
permanence are bundled in `W_R` because Cycle 223 does not separately close
any of them.

| pair | closing first closes second? | closing second closes first? | independent? | control |
|---|---|---|---|---|
| `W_L/W_I` | no | no | yes | one unitary has different kernels in different instruments; an instrument does not select the law |
| `W_L/W_C` | no | no | yes | a law does not choose the tested schedule; a schedule does not derive the law |
| `W_L/W_R` | no | no | yes | coherent dynamics supplies no occurrence/commit; a commit rule does not select this dynamics |
| `W_L/W_P` | no | no | yes | abstract blocks can be exact without a nearest-neighbor apparatus; local compilation need not select these blocks |
| `W_L/W_H` | no | no | yes | one update says nothing about repeated fresh storage; an archive architecture does not derive the update |
| `W_I/W_C` | no | no | yes | the frame is fixed while schedules vary; a schedule leaves the frame/weights unspecified |
| `W_I/W_R` | no | no | yes | a normalized nonselective instrument selects no realized branch; Record occurrence does not derive this PVM |
| `W_I/W_P` | no | no | yes | declared projectors need not be locally implemented; local hardware does not uniquely choose a PVM |
| `W_I/W_H` | no | no | yes | one reset map supplies no fresh tape; tape capacity supplies no transition weights |
| `W_C/W_R` | no | no | yes | a host schedule is not an endogenous commit; a commit event supplies no comparison/rate law |
| `W_C/W_P` | no | no | yes | timing can be supplied without a local apparatus; locality alone supplies no trigger |
| `W_C/W_H` | no | no | yes | sparse timing does not provide blank carriers; capacity does not set event cadence |
| `W_R/W_P` | no | no | yes | a formal irreversible map lacks witness geometry; disjoint copies remain reversible without commit content |
| `W_R/W_H` | no | no | yes | one commit does not solve repeated capacity; fresh capacity does not choose or commit an outcome |
| `W_P/W_H` | no | no | yes | a local one-event compiler need not be reusable; an expanding tape need not implement the pointer interaction |

No pair collapses further under the tested controls. This prevents law,
instrument, cadence, actuality, locality, and capacity from being counted as
one generic “record wall” or as inflated subwalls.

### N3 — hidden-condition scan

| scanned phrase | hidden atom exposed | disposition |
|---|---|---|
| “record-only” | current record label versus full history/process law | split into named N1 routes |
| “read” | pointer correlation, instrument, reset, selection, and archive | each operation named separately |
| “dephase” | reduced channel versus globally irreversible dynamics | only a supplied reduced model claimed |
| “independent witnesses” | tensor-factor copies versus spatial and causal independence | witness language rejected for this runner |
| “clock” | schedule, event trigger, comparison, and rate | only a supplied schedule tested |
| “probability” | squared-modulus frame weight, branch occurrence, and frequency | only the first is supplied here |
| “mass erased” | loss of phase/sign versus loss of every mass statistic | replaced by the exact residual invertible `|m|` dependence |

The skill-prescribed literal scan also checked `we assume`, `by
construction`, `as is standard`, `the framework provides`, `bridge context`,
`background`, `naturally`, `obviously`, `standard QFT`, `registered`, and
`canonical` across the runner and both notes. The only load-bearing hits were
the three uses of “background”: one described prior literature and two
described an every-tick schedule. The literature use is non-load-bearing; the
schedule uses are the explicit `W_C` condition above. No additional hidden
condition was found.

### N4 — residual matching

| cited witness and line | residual attacked there | Cycle-223 residual compared | match? |
|---|---|---|---|
| [Cycle 200 target:117](./PHASE_SENSITIVE_RECORD_FIBRE_STATE_DISCRIMINATOR_CYCLE200_TARGET_NOTE_2026-07-16.md) | whether complete records determine future-sensitive phase information | whether two legal equal-diagonal vectors give different futures | no—lawful same-record preparation/output remains absent |
| [Cycle 11:54](./INFINITE_REVERSIBLE_RECORD_EXPORT_QCA_CYCLE11_NOTE_2026-07-14.md) | exact reversible record export on enlarged cells | reversibility of one/two abstract pointer copies | yes, for reversibility only; neither establishes formation |
| [causal-close Cycle 16:23](./DELAYED_LOCKING_CAUSAL_CLOSE_CYCLE16_NOTE_2026-07-14.md) | bounded close works while silence cannot close an unbounded channel | endogenous trigger for the present mass event | no—the present trigger has not been compiled |
| [commit-clock Cycle 22:22](./CLOCK_AS_COMMIT_COUNT_AND_RATE_CLASSIFICATION_CYCLE22_NOTE_2026-07-14.md) | commit count follows generated commits but supplies no trigger/rate | supplied cadence is not a derived clock | yes, for trigger/rate typing |
| [process-law Cycle 30:15](./GLOBAL_RECORD_HISTORY_PROCESS_LAW_CYCLE30_NOTE_2026-07-14.md) | a global non-Markov history law survives finite quantum controls | the current rank-one Markov family fails cadence closure | no—it is a constructive counterroute, not negative support |
| [append-history Cycle 32:43](./LONG_RUN_RECORD_ONLY_APPEND_ARCHITECTURE_CYCLE32_NOTE_2026-07-14.md) | expanding history works but a fixed finite append region exhausts | repeated fresh archive capacity and cost | yes, for the capacity residual only |
| [decoder Cycle 48:25](./RECORD_DERIVED_COHERENT_CARRIER_DECODER_CYCLE48_NOTE_2026-07-14.md) | finite stabilizer records plus decoder determine future statistics | the common Cycle-223 phase tester under a different candidate law | no—non-Clifford/general decoder closure is open |
| [relational pointer Cycle 16:22](./RELATIONAL_POINTER_CONTEXT_SELECTION_CYCLE16_NOTE_2026-07-14.md) | an exact interaction can conditionally select a pointer axis | Cycle 223 supplies rather than derives its rank-one frame | yes, for the instrument-selection seam only |

All `no` rows are dropped as negative witnesses. They remain cited only as
targets or live counterroutes. The four `yes` rows are used only for their
exactly matching subresiduals, never as authority for a broad no-go. Cycle 200
is a target specification, not negative authority. The existing instrument
and kernel interfaces support supplied maps only; they do not derive this
frame, cadence, archive, or physical Record production.

The Cycle-223 residual ledger itself is:

| target | result actually matched | unmatched residual |
|---|---|---|
| Cycle-200 phase fibre | one common tester has maximum pairwise separation `8/9` among equal-diagonal states | common lawful preparation and physical output Records |
| Cycle-222 mass bridge | target-unfed coherent dispersion and inertia agree with `M` | all-cadence transport and derivation of the candidate unitary |
| record formation | pointer-copy and modeled erasure stages are separated | endogenous occurrence, selection, freshness, permanence under all lawful continuations |
| time | schedule changes the tested channel | event trigger, local rate, cross-clock comparison, normalization |
| gravity/source | coherent intervals reveal the supplied diagonal kick | autonomous source, geometry, field equation, universal coupling |
| boundary/storage | one modeled history factor is retained | repeated append, blank preparation, capacity, cost, and cosmological boundary |

### N5 — rhetoric audit

| rejected wording | safe wording |
|---|---|
| “locking cadence is physical” | “read/reset cadence is operationally consequential in this protocol” |
| “two witnesses make a Record” | “two abstract coherent copies raise the erasure-access burden” |
| “per-tick records erase mass” | “the supplied per-tick kernel loses rest phase/sign but retains an invertible function of `|m|`” |
| “records cannot carry the state” | “the declared coarse symbol is not Markov sufficient for this update” |
| “clock ticks destroy inertia” | “the supplied every-tick read/reset is blind to the tested diagonal kick” |

| negative boundary | element/site | block/sector | finite walk | all-lattice/all-law |
|---|---|---|---|---|
| every-tick kernel is kick-blind | exact matrix-entry identity for diagonal phases | all three supplied sectors | boxes 13 and 17, declared kick | untested; no universal force claim |
| coarse symbol is not Markov sufficient | explicit pair of same-symbol states | all three sectors | one-step one-axis future | untested; only this symbol/update rejected |
| two pointer copies are not globally irreversible | exact finite joint-state reversal with both factors | one binary sector pair | no spatial apparatus built | untested; global claim explicitly rejected |
| candidate kernels do not form one all-time family | exact general finite-unitary criterion | closed formula for all three sectors | cadence sweep at total 16 | no continuum, infinite-lattice, or arbitrary-instrument claim |
| modeled archive is not a selected Record | one nonselective density-state construction | one sector pair | no repeated append process | no all-continuation permanence or occurrence theorem |

Every application-specific result is restricted to the finite Cycle-222 blocks, named
frame, tested one-axis box, and declared schedules. No all-lattice, all-basis,
all-instrument, or all-record claim is made.

### N6 — partial closures

| partial path | present status | next discriminator |
|---|---|---|
| cadence kernels | exact conditional closure per fixed schedule | derive an endogenous schedule |
| coherent working sector | mass bridge carried forward conditionally | derive it from records/law or type it explicitly |
| record-derived decoder | finite stabilizer closure in Cycle 48 | add the common non-Clifford phase tester |
| non-Markov history/process law | finite positive construction in Cycle 30 | compile from a homogeneous nearest-neighbor law |
| sparse local close | bounded positive construction in Cycle 16 | couple close to the candidate matter event without host timing |
| append-only history | unbounded growing tape, finite-region capacity bound | cost repeated fresh carriers and source response |
| relational pointer selection | conditional pointer-axis theorem | derive/select the exact interaction and occurrence map |

These are constructive exits, not rhetorical exceptions. No primitive or
axiom recommendation follows.

The import-bearing shape is explicit condition → bounded theorem → later
import-retirement audit. Deriving a frame, schedule, decoder, or commit rule
from a selected local law would retire an import; it would not automatically
constitute new axiom content. This note makes no primitive-exhaustion claim,
gives no proposed primitive premise weight, and does not invoke a
constitutional minimum-content conclusion.

### N7 — hostile steelman

The strongest record-sufficient steelman uses permanent preparation and
lineage records plus one fixed law to reconstruct the full predictive process
state only when needed; it commits sparsely through locally generated causal
closes and stores the append-only history on fresh carriers. Amplitudes are
then calculational law data rather than additional ontic state. Cycles 16, 30,
32, and 48 establish nontrivial pieces of that construction. Its unresolved
joint locality, non-Clifford closure, fresh-capacity, occurrence, and rate
conditions prevent either acceptance or rejection here.

### N8 — cross-cycle echo

| earlier echo | consequence for Cycle 223 |
|---|---|
| [Cycle 11 reversible export](./INFINITE_REVERSIBLE_RECORD_EXPORT_QCA_CYCLE11_NOTE_2026-07-14.md) | coherent export alone does not establish irreversible Record formation |
| [Cycle 16 causal close](./DELAYED_LOCKING_CAUSAL_CLOSE_CYCLE16_NOTE_2026-07-14.md) | silence is not a trigger; bounded close facts can be |
| [Cycle 22 commit clock](./CLOCK_AS_COMMIT_COUNT_AND_RATE_CLASSIFICATION_CYCLE22_NOTE_2026-07-14.md) | generated commits may define a count; a clock cannot supply its own trigger |
| [Cycle 30 process law](./GLOBAL_RECORD_HISTORY_PROCESS_LAW_CYCLE30_NOTE_2026-07-14.md) | current-record Markov failure does not defeat a non-Markov history law |
| [Cycle 32 append architecture](./LONG_RUN_RECORD_ONLY_APPEND_ARCHITECTURE_CYCLE32_NOTE_2026-07-14.md) | repeated permanence requires explicit fresh capacity or another semantics |
| [Cycle 48 decoder](./RECORD_DERIVED_COHERENT_CARRIER_DECODER_CYCLE48_NOTE_2026-07-14.md) | a record-derived predictive state can close a nontrivial quantum subtheory |

Cycle 223 therefore carries forward only the exact channel/cadence
discriminator. The
broad record-only no-go fails.

The prescribed repository search for earlier “structurally undecidable,”
primitive-exhaustion, new-axiom, and `A_min`-underivation claims was rerun,
together with the available physics-loop `NO_GO_LEDGER.md` files. The relevant
retirement mechanisms were constructive reframing through an explicit
instrument, decoder, history law, causal close, fresh carrier, or convention.
Every applicable mechanism is represented in N1/N6 above. Their existence is
why this gate is `FAIL` for the broad negative claim rather than a no-go
certificate.

## Attribution and novelty boundary

Projective instruments, unistochastic kernels, decohered quantum walks,
process-tensor descriptions of intervention history, measurement-cadence
effects, and the failure of squared unitary entries to compose as coherent
amplitudes do are prior work. Cycle 223 contributes the executable Cycle-222
specialization and a self-contained elementary closure lemma; neither is
asserted to be literature-new, and global novelty has not been established.

Primary comparison sources include Davies and Lewis,
<https://doi.org/10.1007/BF01647093>; Ozawa,
<https://doi.org/10.1063/1.526000>; Życzkowski, Kuś, Słomczyński, and Sommers,
<https://doi.org/10.1088/0305-4470/36/12/333>; Pollock, Rodríguez-Rosario,
Frauenheim, Paternostro, and Modi,
<https://doi.org/10.1103/PhysRevA.97.012127> and
<https://doi.org/10.1103/PhysRevLett.120.040405>; Benoist, Cuneo, Jakšić, and Pillet,
<https://doi.org/10.1007/s10955-021-02725-1>; Kendon and Tregenna,
<https://doi.org/10.1103/PhysRevA.67.042315>; and Chandrashekar,
<https://doi.org/10.1103/PhysRevA.82.052108>.

The following branch-local, unaudited repo interfaces remain upstream support
only:

- [record-dephasing broadcast interface](../../../RECORD_DEPHASING_BROADCAST_INTERFACE_2026-06-05.md);
- [record-instrument kernel interface](../../../RECORD_INSTRUMENT_KERNEL_INTERFACE_2026-06-05.md);
- [post-record transition-kernel interface](../../../POST_RECORD_TRANSITION_KERNEL_INTERFACE_2026-06-06.md); and
- [record Markov-generator boundary](../../../RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06.md).

## Scope boundary

Cycle-200 remains open because the phase-fibre states in this runner are legal
vectors in the supplied working space but are not yet shown to arise from one
common lawful complete-record preparation history. The construction does not
derive a physical pointer frame, record-writing interaction, dephasing,
outcome selection, Born weights, frequencies, clock normalization, strict
nearest-neighbour one-qubit encoding, or archive cost. It is not a mass-spectrum
derivation, gravity theory, measurement solution, no-go theorem, or TOE.

No foundation, axiom, primitive, registry, policy, audit, or queue surface is
changed. There is no axiom conclusion.

## Verification

```text
python3 scripts/locking_cadence_record_kernel_discriminator_cycle223_2026_07_17.py
```
