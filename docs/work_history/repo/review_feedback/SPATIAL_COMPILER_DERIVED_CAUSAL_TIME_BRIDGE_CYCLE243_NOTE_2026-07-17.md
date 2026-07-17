# Spatial-compiler / derived-causal-time bridge contract — Cycle 243

Date: 2026-07-17

Type: bounded contract and executable probe

Status: constructive bridge fragment retained; physical close, comparison, lapse, and rate laws remain open

Authority: none
Audit: unset

## Result

The smallest explicit bridge for the named fixtures is not a map from a gate
layer, marker phase, update layer, or macrostep to time. It is a typed chain of
partial maps:

1. lawful supported executions, quotiented only by swaps of certified
   independent operations, map to a labeled causal event poset;
2. a separately specified physical close may map an event to an append-only
   commit;
3. a separately justified permanence rule may map commits to framework
   Records;
4. a named commit chain supports an integer count observable;
5. an interval matcher and calibration rule turn pairs of such counts into a
   dimensionless relative clock observable;
6. matter-cone, source/lapse, and instrumented-rate diagrams must then commute
   against those matched physical intervals.

The executable constructive fragment supplies a range-one **block-lattice**
one-particle shift (two microscopic sites per block), a two-site block
isometry, an exact intertwiner, and a first-hit event extractor.
For distances 2 and 3 and a held-out distance 5, the coarse and encoded event
histories have the same causal onset. A separate close creates a commit
candidate, and two named commit chains yield the refinement-invariant ratio
`6/4 = 3/2`. This is a proof of the **shape and typing** of a viable bridge. It
is not the missing physical-M2 compiler for the Cycle-230 CAR cell, it does not
select a clock, and it does not derive lapse or interaction rates.

The narrow retained conclusion is therefore constructive: compiler/update
order can feed framework causal event order through a schedule quotient and
event decoder, while metric clock comparisons remain downstream observables.
No broad minimum-content theorem is claimed. The six conditions below are
independently exposed contract fields for these fixtures, not six axioms.

The current minimal-axiom memo supplies the cubic spatial lattice `Z^3`, its
nearest-neighbor/proper-cubic structure, and one-site algebra `M_2(C)`. It also
states explicitly that Admissibility does not define a time metric. This cycle
therefore treats three-dimensional space as axiomatic input and causal or
metric time as downstream bridge content; it does not try to rederive the
spatial dimension or turn the spatial compiler into a clock.

The Record axiom already supplies the generic statements that Records form,
lock one admissible local possibility, and are permanent. It does not identify
a syndrome outcome, pointer copy, detector branch, compiler update, or commit
candidate as a Record. The open arrow below is that physical identification
and formation rule, not a proposal to redefine Record or add permanence.

## Scope and source boundary

This contract consumes only the relevant retained surfaces:

- the current Minimal Axioms memo: axiomatic `Z^3` spatial sites and one-site
  `M_2(C)`, with temporal evolution and a time metric outside Admissibility;

- Cycle 22: named commit-chain count, monotonicity/additivity, schedule
  invariance, and the separation between causal order and relative rate;
- Cycle 33: schedule independence for commuting local edges and the supplied
  boundary/instrument in a local-to-global process;
- Cycle 172: a causal-layer propagation ratio that is not a measured velocity;
- Cycle 224: stationary first-hit branch support, apparatus covariance, and
  the distinction between an event-ready history and a Record;
- Cycle 230: the intrinsic CAR free-plus-contact update and the explicit gap
  between wrapped interaction phase/generator data and a physical rate;
- Cycle 238: the physical spatial-compiler firewall and its list of compiler
  control variables;
- Cycle 239: the exact finite antisymmetric compiler and the explicit spatial
  Schmidt obstruction to treating its global labels as bounded physical
  sites.

Nothing here edits or proposes axioms, foundation, Qualification, primitives,
registries, policies, queues, or audit state. Thirring is not used. All law
choices introduced by the probe remain supplied toy choices.

## Typed domains and codomains

Partial maps are written with `undefined` available when the physical
precondition has not been established.

| Map | Domain | Codomain | Retained status |
|---|---|---|---|
| `J`, schedule/event quotient | lawful supported executions modulo certified independent swaps | finite labeled causal event posets | proved for the bounded commuting fixtures; conditional in general |
| `K`, commit map | finite labeled causal event posets | append-only commit posets or undefined | supplied/open physical close |
| `R`, Record map | append-only commits with a physical close | framework permanent Record histories | commit/Record distinction proved; physical formation open |
| `tau_C`, named clock count | downsets of a Record history and named clock chain `C` | nonnegative integers | proved conditional on named commits in Cycle 22 |
| `M_AB`, interval matcher | pairs of clock-chain intervals | matched interval pairs or undefined | supplied/open |
| `cal_AB`, relative calibration | matched positive clock-count increments | positive rational count ratios | conditional operational observable |
| `Cone`, compiler/cone compatibility | compiled local observables and update opportunities | bounded physical neighborhoods and causal dependencies | exact for the toy; coarse conditional evidence; full compiler open |
| `ell`, source/lapse response | source histories and matched local intervals | positive relative clock responses | open candidate law content |
| `Gamma`, instrumented rate | prepared instrumented histories and calibrated clock intervals | nonnegative event rates | conditional toy only; open for Cycle 230 |

There is deliberately no typed arrow from `gate layer`, `marker phase`,
`macrostep`, `update opportunity`, `circuit depth`, or `wrapped phase` directly
to physical or proper time.

## Contract diagrams and counterfixtures

### 1. Foliation/schedule independence and event identity

For executions whose only difference is an adjacent swap of independently
supported commuting operations, the required square is

```text
execution sigma   -- J -->  labeled event poset H
     | independent swap                ||
execution sigma'  -- J -->  labeled event poset H .
```

The runner realizes a diamond with `X tensor I` and `I tensor Z`. Its two
linear extensions have zero commutator and zero terminal-state residual. The
held-out three-operation antichain has all `3! = 6` foliations and one terminal
state. By contrast, overlapping `H` and `Z` operations do not commute. The
contract then requires a precedence edge; it does not quotient the schedules
or declare either order to be elapsed time.

Event identity is a stable label plus its causal predecessors and physical
support, not an array position in a host schedule. A general `J` remains
conditional because Cycle 230's coin/contact/stream ordering is noncommuting
law content, and Cycle 239's pair-gate order still uses global labels.

### 2. Spatial compiler and common matter transport cone

The required compiler/event square is

```text
coarse trajectories   -- E_* -->  physical trajectories
       | J_coarse                       | J_physical
       v                                v
coarse event posets   --------->  physical event posets ,
```

with `E G_coarse = G_physical E`, bounded support, and matching event labels
on the declared code space. The runner supplies the exact toy instance

```text
E |x> = |2x>,       G_coarse |x> = |x+1>,
G_physical |2x> = |2x+2>.
```

Thus one coarse site uses one fixed two-site physical block, the physical
shift has range one block (two microscopic lattice spacings), and detector
blocks at distances 2, 3, and held-out 5 have no early event and unit first
arrival at the matching update opportunity. This establishes a common matter
transport cone for the toy diagram only. It does not close `C_local` for the
six-mode intrinsic CAR cell: the Cycle-239 spatial-cut witness still blocks
the global-label construction from serving as that compiler.

Deleting the detector leaves `E`, both updates, and their exact intertwiner
unchanged while producing no event label. The causal event extraction is
therefore not hidden inside the compiler identity.

### 3. Event, commit, and Record

The intended partial chain is

```text
event-ready branch support
        | occurrence/identity law
        v
actual causal event -- K(physical close) --> append-only commit
                                              |
                                              R(permanence law)
                                              v
                                        framework Record .
```

Cycle 224 proves normalized first-hit branch support under a supplied
instrument; it does not prove the occurrence arrow. The runner then keeps
`arrival@5` and `close@6` distinct. Deleting `close@6` leaves the event history
but yields no commit. A commit is not automatically a Record: `R` still needs
a physical permanence criterion.

One or two coherent pointer writes are reversible unitaries and give the same
reduced dephasing channel. They do not select a branch or form a Record.
Conversely, a record-visible phase refinement changes the physical transcript
and count input; it cannot be discarded as an invisible schedule refinement.

### 4. Physical clock observable and relative-rate calibration

For a named commit chain `C` and history downset `D_h`, Cycle 22 supplies

```text
tau_C(h) = |C intersect D_h|.
```

This integer is monotone and additive on the named chain. To compare clocks,
the bridge also requires physical endpoint matching:

```text
(Delta C_A, Delta C_B) -- M_AB --> matched pair or undefined
matched positive counts -- cal_AB --> Delta tau_A / Delta tau_B .
```

The runner's matched counts `(6,4)` give `3/2`; a common visible refinement to
`(12,8)` preserves `3/2`. The same causal event-order type with counts `(6,3)`
gives `2`, so order alone does not determine relative rate. Deleting `M_AB`
makes the comparison undefined, not zero elapsed time.

This is the physical clock observable available now: a dimensionless ratio of
matched, named, physically recorded counts. The choice of chain, endpoint
matcher, and calibration remains supplied or open.

### 5. Lapse/source response

Any future source/lapse proposal must test a square of the form

```text
source history + matched interval -- ell --> predicted relative clock response
                 |                              |
          physical preparation          compare with counts
                 v                              v
        realized Record history ----> observed clock-count ratio .
```

Positivity, monotonicity, and the same causal order do not determine `ell`.
For the same source values `(0,1,2,3)`, the runner's two lawful toy candidates
`1/(1+s)` and `1/(1+2s)` agree at zero and disagree thereafter. Deleting the
source response gives a flat candidate without altering the event order.
Cycle 22's capacity-classification fixture and Cycle 230's number operator do
not supply a gravity source or a lapse law.

### 6. Interaction phase-to-rate conversion

The required process is

```text
(U_g, preparation, repeated instrument, boundary)
                     --> normalized first-detection history
normalized history + calibrated clock intervals -- Gamma --> event rate .
```

For `U_g = exp(-i g X)`, the amplitude derivative at `g=0` is nonzero while
the one-opportunity transition-probability derivative is zero. At nonzero
`g`, the runner constructs normalized geometric first-detection histories at
horizons 4, 8, and held-out 13. The identical gate and event order yield rates
differing by a factor of two when the calibrated interval is changed from one
to two clock units. Deleting the detector removes the event rate while leaving
the gate unchanged. Also `U_g = U_(g+2 pi)`, so wrapped phase cannot itself be
an injective rate coordinate.

This is an interaction phase-to-rate conversion contract, not a derived
Cycle-230 rate. Preparation, repeated instrument, boundary, matched clock, and
the selected estimator are supplied in the toy.

## Proved, conditional, and supplied inventory

| Requested bridge item | Already proved at retained scope | Conditional or supplied | Open residual |
|---|---|---|---|
| Foliation/schedule independence | commuting bounded fixtures in Cycles 22/33 and this runner | certified support independence and lawful schedules | general noncommuting schedule quotient |
| Event identity | stable first-hit branch labels and causal onset in Cycle 224/toy | detector, boundary, occurrence criterion | framework event occurrence law |
| Commit/Record distinction | pointer copies do not select; close deletion separates event and commit | close and permanence criteria | physical Record formation |
| Physical clock observable | named commit-chain count and matched count ratio | named chain, endpoint matcher, calibration | clock selection/universality |
| Relative-rate calibration | ratio calculation once intervals are matched | signal/coincidence matching | derivation from substrate |
| Common matter transport cone | Cycle-172 coarse propagation and exact toy compiler/event square | code space and event decoder | physical M2 CAR compiler and its cone theorem |
| Lapse/source response | underdetermination counterfixture only | both monotone toy laws | source identity and physical lapse law |
| Interaction phase-to-rate conversion | normalized toy histories and calibration dependence | preparation, instrument, boundary, clock | Cycle-230 repeated process and physical rate |

The supplied structure inventory is therefore: execution support relation,
independence certificate, operation labels, boundary convention, code-space
encoder, update maps, event instrument, occurrence/close criterion, permanence
criterion, named clock chains, endpoint matcher, calibration, source variable,
lapse ansatz, preparation, repeated instrument, and rate estimator. None is
silently upgraded to constitutional status.

## Six bridge conditions and independence controls

The retained contract fields are:

- `W_event`: schedule quotient, event labels, supports, and precedence;
- `W_commit_record`: physical close and permanence distinction;
- `W_clock_compare`: named chains, matched intervals, and calibration;
- `W_matter_cone`: bounded compiler/event/cone commutation;
- `W_source_lapse`: source identity and relative clock-response law;
- `W_process_rate`: preparation, repeated instrument, boundary, and rate map.

The following table records the pairwise audit. “No / no” means neither field
derives the other in the explicit retained counterfixtures.

| Pair | First implies second? | Second implies first? | Counterfixture |
|---|---:|---:|---|
| event / commit-Record | no | no | first-hit event with close deleted / append-only transcript with unspecified schedule |
| event / clock-compare | no | no | same event poset with ratios `3/2` and `2` / abstract named counts without event decoder |
| event / matter-cone | no | no | pointer-event diamond without transport / compiled shift with detector deleted |
| event / source-lapse | no | no | identical event order under two lapse laws / source response with occurrence map absent |
| event / process-rate | no | no | detector deleted / supplied geometric process with schedule labels quotiented |
| commit-Record / clock-compare | no | no | single close without second clock / matched count sequences with permanence unspecified |
| commit-Record / matter-cone | no | no | local close without transport / exact compiler with close deleted |
| commit-Record / source-lapse | no | no | commit chain with flat response / lapse candidates without permanence law |
| commit-Record / process-rate | no | no | commits without interaction instrument / normalized history without Record law |
| clock-compare / matter-cone | no | no | two counters without matter carrier / toy shift with matcher deleted |
| clock-compare / source-lapse | no | no | ratio observable with source response deleted / lapse ansatz with endpoint matcher absent |
| clock-compare / process-rate | no | no | clocks with detector deleted / same process with two calibrations |
| matter-cone / source-lapse | no | no | compiled free shift with source response deleted / source-clock ansatz without compiler |
| matter-cone / process-rate | no | no | detector-free compiled shift / local geometric process without spatial compiler |
| source-lapse / process-rate | no | no | source response with detector deleted / interaction process with source response deleted |

This pairwise table prevents one demonstrated bridge fragment from being
reported as closure of all downstream physics.

## Deletion, held-out, and lawful-domain controls

- **Held-out foliation size:** one- and two-operation antichains fix the
  factorial rule; a three-operation antichain predicts six terminal-equivalent
  schedules.
- **Held-out transport distance:** onset at distances 2 and 3 predicts the
  distance-5 first hit under the same local update.
- **Held-out history horizon:** normalized first-detection histories at 4 and
  8 opportunities extend to horizon 13.
- **Deletion of event instrument:** preserves the update and compiler
  intertwiner while removing event labels.
- **Deletion of physical close:** preserves event history but removes the
  commit candidate.
- **Deletion of interval matcher:** makes the clock comparison undefined.
- **Deletion of source response:** preserves event order and produces a flat
  comparison candidate.
- **Deletion of detector:** preserves the interaction gate while removing the
  event rate.
- **Lawful-domain restriction:** only certified disjoint commuting operations
  are quotiented. Overlapping noncommuting operations retain precedence.

## No-go discipline for the narrow minimum/negative boundary

The only minimum-like statement retained is fixture-relative: a claimed
physical clock comparison or interaction rate cannot be obtained from the
tested compiler-control data alone without exposing the relevant downstream
map. This is not a universal no-go and not a claim that the six fields must be
fundamental.

### N1 — alternative-route enumeration

| Route | Honesty marker | Actual attempt and bounded disposition |
|---|---|---|
| gate/layer index as time | ATTEMPTED | commuting foliations and visible refinement change layer descriptions without fixing a physical count ratio |
| causal layer or macrostep as duration | ATTEMPTED | Cycle 172 transports one lattice step per causal layer but supplies no measured duration or speed |
| marker or wrapped phase as a clock | ATTEMPTED | `2 pi` aliasing and Cycle 230 retain a gate while leaving calibration unspecified |
| first nonzero branch or pointer copy as Record | ATTEMPTED | Cycle 224 plus the reversible one/two-copy control separate branch support from occurrence and permanence |
| commit count as a complete metric | ATTEMPTED | the same event order supports `3/2` and `2`; chain and matcher choices remain open |
| matter cone as physical speed | ATTEMPTED | the toy and Cycle 172 give causal onset per opportunity, not distance per physical clock interval |
| number/resource variable as lapse source | ATTEMPTED | two positive monotone lapse maps share the same source history and order but disagree |
| generator derivative as event rate | ATTEMPTED | a nonzero amplitude derivative coexists with zero probability derivative at the origin; calibrated intervals also rescale the rate |

These attempts close only the named identifications on the tested lawful
domains. A relational construction that derives several maps jointly remains
live.

### N2 — wall-independence audit

All 15 pairs among the six `W_*` fields are recorded above with explicit
no/no counterfixtures. The runner checks the complete pair count and retains
all fields separately. This is evidence against collapsing these contract
fields in the present fixtures, not proof that nature needs six independent
laws.

### N3 — hidden-condition scan

- “local” refers to bounded support in the stated toy code, not to the open
  Cycle-230 physical-site compiler;
- “event” means the output of a supplied event decoder, not every nonzero
  amplitude and not an update label;
- “commit” requires a supplied physical close; “Record” additionally requires
  permanence;
- “clock” means a named commit-chain count; “comparison” additionally requires
  matched endpoints;
- “source” and “lapse” are typed placeholders, not number, energy, capacity, or
  gravity by renaming;
- “rate” requires an instrumented repeated process and calibrated interval;
- all exact equalities are finite toy equalities on their declared code space.

No hidden condition is promoted to a law by terminology.

### N4 — residual matching

| Claimed identification | Explicit residual/counterfixture |
|---|---|
| schedule order = elapsed time | two commuting schedules, one event poset and terminal state |
| causal-layer count = physical duration | Cycle-172 ratio has no clock calibration |
| pointer copy = Record | reversible copy deletion and identical reduced channel |
| event = commit | deleting close preserves event and removes commit |
| event order = relative rate | ratios `3/2` and `2` on the same order type |
| transport cone = physical speed | event onset is indexed only by update opportunity |
| source order = lapse law | `1/(1+s)` versus `1/(1+2s)` |
| phase/generator = rate | `2 pi` alias, detector deletion, and clock rescaling |

Every narrow negative used in the result has a matching executable or retained
finite counterfixture. The open full spatial compiler is not used as a generic
excuse for unrelated failures.

### N5 — rhetoric and resolution audit

The note uses “smallest” only for the explicit bridge extracted from the named
fixtures. It does not say “impossible,” “cannot ever,” “only possible,” or
“fundamentally independent.” Failed identifications are narrow and typed.
Constructive diagrams and exact residuals precede all negative conclusions.

### N6 — partial-closure paths

Several walls may still close together. A substrate event law could jointly
derive occurrence, close, and permanence. A relational clock protocol could
jointly derive interval matching and calibration. A physical M2 compiler could
make the matter cone and schedule quotient one theorem. A source-dependent
matter law could jointly fix lapse and interaction-rate conversion. The
contract allows these reductions; it merely requires that the derived arrows
be exhibited and tested.

### N7 — steelman

The strongest alternative is a fully relational construction in which there
is no extra metric-time primitive: local causal events form Records, recurring
matter subsystems serve as clocks, coincidences match their intervals, and
source-dependent dynamics predicts all observed ratios. On that route, every
map above is derived from one substrate update plus boundary conditions, and
absolute duration is unnecessary. Nothing in this cycle rules that route out.
It instead supplies the diagrams that such a construction must make commute.

### N8 — cross-cycle echo

The same distinction recurs independently across Cycle 22 (count versus
rate), Cycle 33 (commuting schedule versus metric time), Cycle 172 (causal
layer versus measured velocity), Cycle 224 (branch history versus Record),
Cycle 230 (wrapped phase/generator versus rate), Cycle 238 (compiler controls
versus physical time), and Cycle 239 (global compiler labels versus bounded
physical sites). Cycle 243 does not upgrade that repetition to constitutional
evidence; it converts it into one typed test surface.

## Dependency-ledger effect

- `C_ref`: unchanged; reference/physical clock selection remains supplied.
- `C_num`: unchanged; no number/resource variable becomes a source or clock.
- `C_wrap`: unchanged; wrapped phase remains gate data, not a rate.
- `C_int`: clarified, not closed; the preparation-instrument-clock inputs to a
  rate are now typed and executable in a toy.
- `C_local`: clarified, not closed; a toy bounded compiler/event square works,
  while the Cycle-230 physical M2 CAR compiler remains open.
- `C_source`: unchanged; two lapse counterfixtures expose the missing response
  law.

There is no axiom pressure from this cycle. The residuals span unfinished
constructive implementations and explicitly supplied maps, not one
route-independent substrate obstruction.

## Exact verification

Run:

```bash
python3 scripts/spatial_compiler_derived_causal_time_bridge_cycle243_2026_07_17.py
```

The runner checks source/documentation scope, typed-map exclusion of direct
compiler-control-to-time arrows, commuting and noncommuting schedule fixtures,
the exact block-compiler/event square, event/commit/Record deletion controls,
clock ratios, lapse underdetermination, interaction-history normalization,
held-out sizes, all 15 independence pairs, and status separation.
