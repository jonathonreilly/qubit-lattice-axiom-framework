# Protected recurrent candidate/registration tournament — Cycle 335

Date: 2026-07-18

Branch: `codex/bare-metal-mvp-probes-20260713`

Authority: none

Audit: unset

Constitutional effect: none

Companion runner:

```text
scripts/protected_recurrent_actual_history_selection_cycle335_2026_07_18.py
```

This cycle changes no axiom, foundation, Qualification, primitive, registry,
policy, queue, or audit-status surface. It drafts no axiom language. It uses
the no-go-discipline skill fetched from `origin/main` at
`df24c9086f485a284a8c103c7c7a1e2dccc0d7bd`.

## Result up front

Three bounded mechanics are positive:

1. protected recurrence on a four-slot ring;
2. a moving/exported boundary that relocates one existing blank to the
   incoming register;
3. an append-only finite window with explicit exhaustion and reverse unwind.

The protected ring has period four, four distinct forward states, one blank
protected slot at every step, and an exact inverse. The export route moves the
oldest protected candidate to a previously blank boundary and returns a blank
incoming register. The append route writes exactly one protected candidate per
fresh slot through held `L=6`, rejects the first over-capacity write, and
unwinds exactly.

Every primitive update is a swap on at most six M2. Every route is reversible.
Every tested swap/write deletion, predecessor identity anti-splice, and
single-replica fault changes or suppresses the declared endpoint, with zero
lawful survivors; no physical fault flag is constructed. The identity-bound Cycle-329 comparator
passes at trained `L=3`, held `L=6`, and all 24 proper-cubic frames.

The approved `realized_state_primitive` changes the interpretation of this
campaign. It already supplies one law-admissible actual-history/reference
slot for pointwise evaluation. That slot chain-satisfies dependencies and is
not a wall. It supplies zero state-contingent content: no history, selection or
sampling rule, measure, typicality, boundary, probability, or value.

Cycle 335 therefore tests recurrent candidate mechanics for a future physical
state-dependent registration functional evaluated at the supplied realized
state. It does not test whether the reference exists or treat it as writable
memory. The declared selector-free summary family is identical under a
one-step cyclic translation of the tested protected candidate/blank pattern.
A supplied phase or boundary role distinguishes the two, but that is supplied
program content. Three live routes remain untested, so the broad claim that no
recurrent physical law can supply such a registration functional is not
shipped.

Copying is not a Record. Circuit cycle is not time. Occurrence remains
separate. Member selection remains separate in the precise sense that the
slot's contingent content and selection rule are not derived. Typing remains
separate. Permanence remains separate.

Gate status: FAIL / DO NOT SHIP the broad negative. The disposition is
`partial-attempt-with-named-untested-routes`. No axiom pressure follows.

## 1. Far-side type contract

The controlling authorities are:

- `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`: the framework has an
  approved pointwise realized-state reference, but it supplies no state or
  selector content;
- Cycle 30: a global history/process law and the realized-state reference solve
  different type problems; a measure does not sample the actual history;
- Cycle 332: two physical boundaries can yield a conditional transition and
  close witness, but their realized-history selection remains supplied;
- Cycle 329: predecessor identity and readiness can be physically checked;
- Cycle 22: a circuit count becomes clock count only on a lawful named Record
  chain, with rate and calibration separate.

The typed target is consequently:

```text
supplied law-admissible realized state
  + physical state-dependent registration functional
  -> identified lawful local transition content, pointwise.
```

This cycle supplies recurrent protected close/readiness-flag mechanics only,
not full transition-history payloads. It does not derive the registration
functional.

## 2. Route 1 — protected recurrence

The four protected slots begin as

```text
(111,111,111,000).
```

A right rotation is compiled into three adjacent protected-slot swaps. Its
history is

```text
111 111 111 000
000 111 111 111
111 000 111 111
111 111 000 111
111 111 111 000.
```

| recurrence control | result |
|---|---:|
| exact period | `4` |
| distinct forward states | `4` |
| fresh-slot positions | `3,0,1,2` |
| exact recurrence residual | `0` |
| four-step inverse residual | `0` |
| any single swap-deletion lawful survivor | `0` |
| history apparatus | `16 M2` |
| maximum primitive update support | `6 M2` |

The 16 M2 are twelve protected occupancy bits and a four-M2 one-hot phase
carrier. The phase carrier identifies a location, but its initial phase is
supplied program content.

The tested selector-free local invariant family contains protected occupancy
count, sorted repetition weights, the multiset of identity flags, cyclic
nearest-neighbor occupancy views, and the occupancy census. It is identical
before and after one cyclic displacement: residual `0`. Reading the supplied
phase distinguishes them. The retained statement is exactly this finite
invariant equality, not an impossibility theorem for other invariants.

Blank capacity recurs, but no candidate is destroyed. Rotation merely moves
the blank and protected redundancy. Forward recurrence and its circuit period
are not permanence or physical time.

## 3. Route 2 — moving/exported boundary

For a window of `L` protected slots, define

```text
(export=000, slots=111...111, incoming=111).
```

A nearest-neighbor swap chain gives

```text
(export=111, slots=111...111, incoming=000).
```

The oldest candidate is not erased; it occupies the exported boundary. The
existing export blank is relocated to the incoming register, so net blank
capacity does not increase. Reversing the same swaps restores the complete
input.

| export control | trained `L=3` | held `L=6` |
|---|---:|---:|
| exported candidate | `111` | `111` |
| relocated incoming blank | `000` | `000` |
| window occupancy | `3/3` | `6/6` |
| inverse residual | `0` | `0` |
| swap-deletion lawful survivors | `0/4` | `0/7` |
| apparatus support | `15 M2` | `24 M2` |

The boundary role can distinguish exported from internal redundancy, but the
boundary location and export grammar are supplied structure. Repeated forward
uses require a new blank export register or a larger external sector; applying
the inverse restores the original export blank but also undoes the export.

## 4. Route 3 — append-only finite window

The finite window begins with `L` blank protected slots. Each forward step
swaps one supplied `111` candidate into the next one-hot phase target and
returns a blank incoming register.

| append control | trained `L=3` | held `L=6` |
|---|---:|---:|
| occupancy prefix | `0,1,2,3` | `0,1,2,3,4,5,6` |
| first over-capacity write | rejected | rejected |
| deleted first write | no slot change | no slot change |
| reverse-unwind candidates | `3` | `6` |
| reverse-unwind blank residual | `0` | `0` |
| apparatus support | `15 M2` | `27 M2` |

The route is append-only only on its declared finite forward domain. It has no
capacity renewal before inverse or export. Its exact inverse returns all
candidates and blanks the window, demonstrating again that forward nonreturn
is not permanence.

## 5. Identity, faults, held size, and covariance

Every occupied protected block is attached to the actual Cycle-329 target or
predecessor identity. The inherited comparator is rerun on rotated actual
Cycle-312 supports, not on a preferred coordinate name. The frame result below
therefore covers the inherited physical matcher and cubic-scalar labels. The
ring, export, and append layouts themselves are abstract register layouts; no
physical cubic embedding of those layouts is claimed.

| control | result |
|---|---:|
| frame-size cases | `48` |
| proper-cubic frames per size | `24` |
| support covariance failures | `0` |
| match/readiness failures | `0` |
| three predecessor identity-splice survivors | `0` |
| nine single-replica fault survivors | `0` |
| malformed-domain rejections | `6/6` |

The protected occupancy and selector-output roles are cubic scalars. A
corrupted predecessor identity cannot borrow a lawful protected bit from a
different slot.

## 6. Reversibility and capacity inventory

| structure | status after Cycle 335 |
|---|---|
| approved realized-history/reference slot | supplied framework primitive; chain-satisfied, not a wall |
| recurrent protected ring | derived, exact period four |
| moving export and relocation of one existing blank | derived conditionally |
| finite append prefix | derived through held `L=6` |
| protected copying/fanout | reversible pointer redundancy, not Record |
| candidate occurrence | prior conditional input |
| pointwise state-dependent registration functional | absent from these mechanics |
| Record typing | absent |
| permanence | absent; exact inverses exhibited |
| clock law, interval, rate, calibration | absent |
| probability, measure, sampling, typicality | absent |

Blank handling is route-dependent. The ring recurs one internal blank. The
export route relocates an export blank to the incoming register without net
capacity creation. The append window does not renew capacity. None of those
facts constructs a state-dependent registration functional at the supplied
realized state.

## 7. Exact route disposition

| route | disposition | retained result | residual |
|---|---|---|---|
| protected recurrence | **positive** | exact period, recurring blank, inverse, declared summary-family equality | phase supplied; no state-dependent registration functional |
| moving/exported boundary | **positive** | oldest candidate exported, existing blank relocated, inverse | boundary/export program and further capacity supplied |
| append-only finite window | **positive until explicit bound** | prefix monotonicity, exhaustion rejection, reverse unwind | no renewal before export/inverse |

The constructive result is meaningful: Cycle-332 protected close/readiness
flags can be composed into bounded recurrent and capacity-moving mechanics.
The residual is narrower than “actuality is absent”: the realized-state
reference is approved, while a physical state-dependent registration
functional is not produced here.

## 8. No-Go Discipline Gate

The candidate negative is deliberately narrow during testing: can the tested
declared selector-free protected-candidate summary family distinguish a
one-step cyclic translation of the tested protected candidate/blank pattern?
It cannot; residual zero. The broad negative—no recurrent law can supply a
state-dependent history-registration functional—fails the gate and is not
shipped.

### N1 — Alternative routes

| route | honesty marker | attack and disposition |
|---|---|---|
| protected recurrent ring | **ATTEMPTED** | exact recurrence and capacity succeed; candidate-only tested invariants are displacement invariant |
| moving exported boundary | **ATTEMPTED** | boundary role distinguishes export, but that role/program is supplied |
| append-only finite window | **ATTEMPTED** | ordered prefix succeeds until explicit capacity exhaustion |
| explicit selector tag | **OPEN / UNTESTED** | derive a registration tag from the common dynamics rather than supply its phase |
| environment or asymptotic export sector | **OPEN / UNTESTED** | test whether an infinite/export sector carries a law-selected invariant content |
| topological history charge | **OPEN / UNTESTED** | test a protected invariant not reducible to occupancy and repetition syndromes |

Three live routes make a broad no-go premature. Their `OPEN / UNTESTED`
markers are explicit N1 failure markers, not prescribed shipping markers.

### N2 — Wall-independence audit

The collapsed set excludes the approved actuality slot. It contains only:

- `W_content`: physical state-dependent registration functional;
- `W_typing`: lawful Record typing of candidate data;
- `W_permanence`: physical permanence of typed history.

| first | second | first closes second? | second closes first? | independent? |
|---|---|---|---|---|
| W_content | W_typing | no | no | yes |
| W_content | W_permanence | no | no | yes |
| W_typing | W_permanence | no | no | yes |

Capacity is not inflated into a universal wall because route 1 recurs a blank
and route 2 relocates one without creating net capacity.

### N3 — Hidden-condition scan

Hidden-condition scan result: zero unclassified hits. Explicit conditions are
the supplied selector phase, boundary/export role, incoming candidates, fresh
blanks, finite window size, prior occurrence, and compiled swap program. None
is buried as context.

### N4 — Residual matching

| cited witness (path, line) | witness residual | Cycle-335 residual | match? |
|---|---|---|---|
| `docs/work_history/repo/review_feedback/REDUNDANT_ARCHIVE_PERMANENCE_HISTORY_CYCLE283_NOTE_2026-07-17.md:285` | Cycle 283 reversible-redundancy residual: finite redundant unitary data do not select one history | selector-free protected redundancy | yes, narrow |
| `docs/work_history/repo/review_feedback/PHYSICAL_TRANSITION_OCCURRENCE_CLOSE_TOURNAMENT_CYCLE332_NOTE_2026-07-18.md:63` | Cycle 332 boundary-selection residual: a transition witness still receives the tested boundary pair | recurrent mechanics before pointwise registration | yes, interface continuation |
| `docs/work_history/repo/review_feedback/OUTGOING_CARRIER_NONRECURRENCE_CYCLE286_NOTE_2026-07-17.md:467` | Cycle 286 capacity residual is dropped: outgoing nonrecurrence concerns finite carrier return, not pointwise registration | recurrent registration interface | no |
| `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md:34` | approved pointwise slot with zero contingent content | exact type of `W_content` | yes |
| `docs/work_history/repo/review_feedback/GLOBAL_RECORD_HISTORY_PROCESS_LAW_CYCLE30_NOTE_2026-07-14.md:84` | measure/process law and actual reference solve separate type problems | no sampler inferred from recurrence | yes |

No mismatched capacity result is cited as evidence for member-content
selection.

### N5 — Rhetoric and resolution audit

| resolution | tested? | exact result |
|---|---|---|
| per protected triple | yes | repetition validity and single faults |
| per four-slot ring | yes | candidate-only invariant residual zero under displacement |
| per exported/append window through `L=6` | yes | exact capacity and inverse controls |
| arbitrary larger finite window | no | no negative claim |
| infinite/export sector | no | open route |
| lattice-wide untested | no | no lattice-wide member-selection statement |

Thus “reversible redundancy is not actuality” is narrowed here to: the
declared selector-free summary family cannot distinguish a one-step cyclic
translation of the tested protected candidate/blank pattern.

### N6 — Partial-closure paths

- The primitive-registry check finds `realized_state_primitive` in
  `docs/audit/data/axiom_premise_nodes.json`, with `current_path`
  `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`. The approved primitive
  already closes the pointwise type slot; it is chain-satisfied, is not a
  wall, and does not supply content. The open question is a physical
  state-dependent registration functional evaluated at the supplied realized
  state.
- A selector-tag import-retirement path could derive the presently supplied
  phase from dynamics and then audit whether the tag is redundant.
- An environment/export path could enlarge route 2 and test asymptotic sector
  invariants.
- Cycle 30's fixed process-law route could determine history weights or lawful
  registration structure without treating a measure as sampler.
- Record typing and permanence remain separate from pointwise registration and
  need not be folded into one wall.

No claim that a new axiom is required is made.

### N7 — Hostile steelman

A hostile reviewer should reject the broad negative: the open environment or
asymptotic export sector could carry a superselection label or stable boundary
functional that is absent from every finite reversible window tested here.
The approved realized-state primitive already supplies the pointwise slot, and
Cycle 30 shows that a complete process functional can add law-side history
content without turning a finite candidate copy into a sampler. A derived
selector tag or topological charge would also defeat the claimed closure.
Therefore only the exact finite invariant equality survives.

### N8 — Cross-cycle echo

Prior “reversible redundancy alone” boundaries in the primary-source audits
were explicitly limited to finite unitary copying and left infinite-volume or
environmental sectors open. Cycle 98's moving allocator kept moving/export
routes live. Cycle 332 retired the supplied aggregate occurrence bit by adding
two-boundary transition structure. The same retirement mechanism could apply:
add a physical selector/export/topological structure and audit whether its
content is derived rather than supplied.

Gate status: FAIL / DO NOT SHIP the broad negative.

Retained output: positive bounded mechanics plus residual zero for the exact
selector-free tested invariant family. No axiom pressure follows.

## 9. TOE dependency ledger and maturity

| wall | Cycle-335 movement | still open |
|---|---|---|
| `C_ref` | approved realized-state reference is correctly chain-satisfied; identity-bound protected candidates can be evaluated pointwise | physical state-dependent registration functional remains open |
| `C_num` | unchanged | no coefficient selection or numerical grade |
| `C_wrap` | period-four recurrence, moving export, bounded append prefix, and explicit capacity semantics | pointwise registration, typed permanence, named clock, interval, and rate |
| `C_int` | unchanged | candidate mechanics do not derive interaction occurrence |
| `C_local` | bounded six-M2 swaps, inherited matcher frame tests, deletion, inverse | physical embedding of recurrence layouts, autonomous registration, larger recurrent network, primitive integration |
| `C_source` | unchanged | no energy, stress, lapse, source, or gravity response |

Using the packaged Cycle-330/Cycle-332 baseline:

| lane | integrated | strict floor | conditional | maturity | Cycle-335 disposition |
|---|---:|---:|---:|---:|---|
| operational quantum / Records | 67% | 33% | 94% | 3.8/5 | bounded recurrent protected-candidate mechanics; still no typed Record |
| causal time / clock | 38% | 20% | 70% | 2.2/5 | recurrence/capacity advance; circuit period is not time |
| inertia / matter | 77% | 38% | 98% | 4.4/5 | unchanged |
| gravity / source / resource | 42% | 17% | 70% | 2.3/5 | unchanged |
| Born / probability / realized history | 34% | 14% | 85% | 2.0/5 | approved slot respected; no content selector, measure, or probability law |

These are planning scores, not truth probabilities or audit verdicts.

## 10. Novelty, next campaign, and verification

The retained repository result is the integration of Cycle-332 protected
candidates and Cycle-329 identity controls into three bounded recurrent
mechanics with exact capacity, inverse, fault, held-size, and frame ledgers.
Cyclic shifts, swap registers, repetition codes, exported buffers, and finite
append logs are prior-art mechanisms. No global novelty priority is claimed.

Thirring machinery is not used or compared.

The next optimal campaign is one of the three open N1 routes: derive rather
than supply a selector tag; attach the exported candidate to an explicit
environment/asymptotic sector; or build a topological history charge. The
approved actuality slot must remain chain-satisfied and must not be relabeled
as absent. Any later negative again requires full N1-N8.

Run from the repository root:

```text
python3 scripts/protected_recurrent_actual_history_selection_cycle335_2026_07_18.py
```
