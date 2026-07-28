# Cycle-726 grounding: the DOWN/ACK wavefront-controller compilation gap

## Scope and source notation

This is a static extraction from exactly the three requested Cycle-718 files. No runner or certificate was executed.

- `P` = `scripts/frontier_cycle718_spatial_ack_physical_m2_route_2026_07_26.py`
- `T` = `scripts/frontier_cycle718_token_relative_relay_core_2026_07_26.py`
- `C` = `scripts/frontier_cycle718_carrier_return_core_2026_07_26.py`

All three exact filenames exist. The directory-listing fallback was not needed.

The most important grounding fact is negative: none of these files defines a `DOWN` register, a DOWN-state gate word, or a DOWN/ACK state-transition table. `P` has a transient local `ack` wire in `CommitLayout` (`P:100-116`) and compiles that local ACK handshake inside `commit_segment` (`P:189-284`). That is not a spatial wavefront controller. The files establish enough local predicates and fixed schedules to specify the missing controller boundary, but they do not contain the missing controller law in an already explicit truth table.

## 1. Semantic controller law present in the files

### 1.1 Registers and conventions

`P` sets `RAIL_WIDTH = 39` and `WORK_WIDTH = 47` (`P:94-97`). `make_commit_layout() -> CommitLayout` (`P:119-144`) allocates:

- source/interface bits `pointer`, `left`, and `right`;
- four `law` bits;
- one `head`, four `rotor`, one `identity`, and one persistent `pending`;
- transient `new`, `ack`, and `commit`;
- twelve `hold` bits;
- six 39-bit direction rails; and
- 47 clean work bits.

This totals 310 abstract wires. The 39-bit rail convention is defined by `rail_fields(block)` (`P:147-169`):

- bits 0--33: the full raw packet payload;
- bits 34--38: `identity_tag`, `fresh`, `start`, `cleanup`, and `retry_echo`.

The commit circuit is canonical-seam-local. `commit_word()` emits only `commit_segment(0)` and `commit_segment(1)` (`P:305-309`). For segment 0, `right` is the positive endpoint and `left` the negative endpoint; for segment 1 the roles reverse (`P:195-205`). In the physical placement these two target the A-rail, station 0 blocks (`P:636-656`). The physical shift subsequently acts on all six direction families and all stations (`P:750-772`).

The bank convention in `C` uses two allocator cells plus token, head, rotor, interface, law/admission, and work bits supplied by imported module `A`. One link has one retained `LATCH` and 190 `LINK_WORK` bits (`C:28-32`). `T` fixes three bank bases `(41, 172, 303)`, two edges, and for each edge allocates separate handoff and relay latches, each with 190 work bits (`T:32-51`).

### 1.2 The effective per-step local law

There is no Python `if` deciding whether the local physical commit or shield acts. Those predicates are already coherent reversible gate predicates:

| Decision/action | Decision inputs | Effect/output | Implementation |
|---|---|---|---|
| Park matter while an old event is pending | `pending`; each source matter bit and corresponding clean `hold` bit | Twelve `pending`-controlled swaps move matter into `hold` before the decoded update and restore it afterward | `shield_physical_word(layout)` (`P:724-739`), placed twice at `P:803-809` |
| Select canonical orientation | `pointer=1`; the selected endpoint is 1; the opposite endpoint is 0; all four `law` bits are 1 | Enables one of commit segments 0 or 1 | `commit_segment(direction, ...)` positive/negative controls (`P:189-206`) |
| Recognize a complete blank destination | The orientation controls above; all 39 bits of the selected rail are 0; transient `ack=0` and `commit=0` | Toggles `new` | `zero_controlled(..., target=LAYOUT.new, ...)` (`P:172-182`, `P:208-211`) |
| Append ACK and write the packet | `new=1`, then `ack=1` | `ack` controls predecessor, rotor-before/after, carry, delta, endpoint/binder/valid/orientation/actual/admiss/law, identity tag, frontier swap, start/cleanup/retry handshakes, and pointer cleanup | `P:212-270` |
| Return ACK clean and transfer NEW to FRESH | `new`; then `start & valid` computes transient `commit` | Clears `ack`; swaps `new` into rail `fresh`; clears `commit` | `P:271-284` |
| Preserve a refused event | Common orientation controls; local `start`; persistent `pending` | Reversible local codeword transposition `(pending,start): 00 <-> 11`; `10` remains held after `start` shifts away | `pending_latch_segment(direction)` (`P:287-303`) and its stated semantics/certificate at `P:437-462` |
| Shift exported bundles | No data-state enable in this file | Every complete 39-bit A bundle advances one station through two SWAP layers; B returns blank on the certified domain | `shift_physical_word(layout, omit=None)` (`P:750-772`) |

Thus the observable local rule is:

1. if `pending=1`, shield the twelve matter modes;
2. run the decoded Cycle-713 source word;
3. unshield;
4. on exactly one lawful orientation and a completely blank selected rail, create NEW, append ACK-gated packet/handshake data, consume the source pointer, return ACK/work clean, and move NEW to FRESH;
5. if the pointer was not consumed and local `start=0`, latch `(pending,start)=11`; and
6. after source re-encoding, shift every rail one station.

This order is literal in `full_physical_word(layout)`: `decode_prefix + shield_pre + decoded + shield_post + commit + suffix + shift` (`P:775-832`).

It is a fixed global program order, not a DOWN/ACK wavefront transition. `shift` is not selected by a phase bit and there is no per-station phase register. The report explicitly lists “fixed commit-then-shift layer order” and the finite pre-wrap no-return sector as supplied (`P:1255-1262`).

### 1.3 Relay/handoff semantics that approximate a forward/return wave

`C` provides the semantic forward/return scaffold:

- `pre_latch_word()` computes a retained edge predicate from a full lawful left allocator frontier and a fully blank/clean right bank (`C:157-178`).
- `forward_transfer_word()` uses that latch to move token, head, rotor, and endpoint-carrier interface from left to right (`C:181-191`).
- `packet_word_for_bank(bank_index)` applies an admission-gated packet body plus a structural bank-index prefix (`C:85-154`).
- `carrier_return_word()` returns only `POINTER`, `U_TO_V`, `V_TO_U`, and `DIRECTION_OK` across the same latched edge (`C:194-198`).
- `post_latch_word()` recognizes the lawful first-packet postimage and cleans the retained latch/work (`C:201-228`).
- `three_phase_word()` fixes `pre-latch -> forward transfer -> packet -> carrier return -> post-latch` (`C:231-238`).

`T` separates allocator handoff from carrier-only relay. Its `relay_predicate(edge)` recognizes:

- left positives: `POINTER`, `DIRECTION_OK`, and `BINDER/ACTUAL/ADMISS/LAW`;
- right positives: `BINDER/ACTUAL/ADMISS/LAW`;
- left negatives: all `TOKEN`, `ZERO_WORK`, and `TOKEN_OK`; and
- right negatives: `ZERO_WORK`, `TOKEN_OK`, `POINTER`, `U_TO_V`, `V_TO_U`, and `DIRECTION_OK`

(`T:90-104`). `relay_latch_word()` compiles that Boolean predicate into a latch (`T:107-112`), and `relay_swap_word()` uses it to move the four carrier bits (`T:115-121`).

`T.classical_word(deletion=None, edge_local_predecessor=False)` constructs a fixed three-bank/two-edge program (`T:148-211`):

1. compute the carrier at fixed bank 0;
2. for edges 0 then 1, perform allocator handoff, relay-latch compute, and relay swap;
3. attempt the packet word at every bank;
4. for edges 1 then 0, undo the relay swap/latch and run carrier return plus post-latch; and
5. uncompute the source interface.

This is the closest literal forward/ACK-style program in the three files, but the edge sequence is statically unrolled by Python. It does not contain a moving DOWN/ACK state token.

## 2. What is already physical

### 2.1 Placement and emitted words

`physical_layout(length)` (`P:607-690`) places:

- the imported Cycle-713 source cells/carriers;
- six A/B rail loops;
- the source pointer at `source_wire_sites[40]`, canonical endpoint inputs at source sites 1 and 6;
- the four law bits, head/rotor/identity, `pending`, transients, twelve holds, and 47 work bits in a collision-free local box; and
- each commit rail on direction `d`, A bank, station 0.

`controller_sites()` reserves 73 M2 sites (`4+1+4+1+1+3+12+47`) (`P:596-604`). Despite the name, these sites hold the local commit data, latches, and work. They are not sites for a compiled DOWN/ACK phase controller.

The rail placement uses:

- `2 * 6 * length * 39 = 468 * length` rail M2 sites;
- 6,084 rail M2 at held length 13;
- 7,956 rail M2 at held length 17.

`commit_physical_word(layout)` expands `commit_word()` to literal X/H/T/TD/CNOT instructions at `commit_wire_sites` (`P:708-721`). `shield_physical_word(layout)` expands twelve pending-controlled Fredkins at physical source/hold sites (`P:724-739`). `shift_physical_word(layout)` emits two layers of 39 lane-wise physical SWAPs over all six direction loops (`P:742-772`).

Each SWAP is three CNOTs, so the shift contains:

- `2 * 6 * length * 39 = 468 * length` SWAP instances;
- `6 * 2 * length * 39 * 3 = 1404 * length` CNOT instructions;
- 18,252 shift CNOTs at length 13; and
- 23,868 shift CNOTs at length 17.

`full_physical_word()` also physically maps the repetition/target decoders, the imported Cycle-713 decoded word, and the inverse suffix, then concatenates all seven segments (`P:775-832`). The code reports, without hard-coding, decoded gate count, QR residual, each segment’s primitive count, and total physical primitive count (`P:1078-1090`). Because this extraction did not run the runner, runtime-produced totals and hashes are not reproduced here.

### 2.2 Existing semantic, route, and covariance certification

`structured_commit_certificate()` (`P:367-523`) checks the gate word, not a Python reference assignment. It enumerates 256 orientation/head/rotor/identity/pending rows (`P:372-374`), exact inverse, one-event conservation, clean transient/work return, dirty/unlawful refusal, blocked pending behavior, 64 arbitrary-state inverse rows, and active component deletions. Note that the later comment calls this a “128-row equivalence” (`P:1149-1151`); the actual loop has 256 rows once `pending` is included.

`pending_shield_certificate()` checks all 4,096 twelve-mode matter basis rows, vacuum, clean return of one persistent pending M2 and twelve HOLD M2, and deletions (`P:835-910`).

`shift_semantic_certificate(length)` checks all six 39-bit bundle families, the exact reverse, and the declared four-update pre-wrap condition (`P:913-948`).

`routed_layout_certificate(length)` (`P:1056-1105`) builds the full physical
word, routes it, and records:

- assigned/controller/rail/touched/blank-work M2 counts and placement
  collisions;
- all physical segment counts;
- pre-route non-NN failures for the already-local shift;
- routed nearest-neighbor gate count and maximum route distance;
- non-NN, operand-order, and route-return failures;
- detected route-macro deletion and routed-word SHA-256.

For held lengths 13 and 17, `main()` requires zero source/placement collisions, zero shift non-NN failures before routing, zero routed non-NN, operand-order, and route-return failures, and a positive deletion-detection count (`P:1115-1117`, `P:1189-1197`). It also requires linear support slopes: 468 assigned and touched rail M2 per added station and 1,404 physical shift primitives per added station (`P:1118-1148`, `P:1198-1208`).

`active_covariance()` checks 24 proper-cubic frames, 4,096 active endpoint rows per frame, all 576 ordered frame products, two translations, instruction coordinate restoration, and routed NN preservation (`P:951-1053`). The main check requires every corresponding failure count to be zero (`P:1209-1217`).

Therefore the emitted commit/shield/shift WORD is already physical and routed.
The gap is not “turn these three macros into physical instructions.” The gap
is a physical state machine that selects/phases them autonomously.

## 3. What is not compiled

### 3.1 Missing state and transition law

The physical layout has no `down`, `phase`, `wavefront`, `program_counter`, or
per-edge/per-station ACK-state register. The local `new/ack/commit` bits are
returned clean inside one commit and cannot remember a propagating phase.
Consequently these files do not specify:

- how a DOWN phase is born, advances, stalls, or turns into ACK;
- which station/edge owns the active phase;
- whether commit, shield/decode, or shift is enabled in each phase;
- how ACK propagates back and authorizes source cleanup;
- how phase state behaves at an occupied destination, exhaustion, wrap, or an
  unlawful/off-code input; or
- how the controller returns its own phase/work rails clean.

Those are not merely unlowered Python branches; the state encoding and complete
truth table are absent and must be supplied by the Cycle-726 specification.

### 3.2 Python/host decisions standing above the gate words

The exact host-level decision points are:

| Host decision | Inputs read | Output/action chosen |
|---|---|---|
| Find the active source bank | Every bank’s `A.TOKEN` bits; Python `next(...)` requires token population exactly one | Host integer `source` (`C:271-276`) |
| Decide whether an event exists | External Python tuple `direction`; comparison with `(0,0)` | If nonzero, replace `bank_state[source]` with `event_ready_bank(...)`, thereby setting interface/carrier state (`C:277-279`) |
| Choose forward traversal | Bank count plus optional host `forward_order` | Apply `pre_latch + forward_transfer` to each selected edge (`C:280-288`) |
| Choose where packet words are attempted | Python `enumerate(bank_state)` and structural bank index | Apply `packet_word_for_bank(index)` to every bank; internal admission gates make non-frontier banks inert (`C:289-292`) |
| Choose reverse/ACK traversal | Bank count plus optional host `reverse_order` | Apply `carrier_return + post_latch` on each selected edge (`C:293-296`) |
| Perform final source cleanup | Each bank’s decoded `A.POINTER` bit, tested by Python `if` | Reverse the direction witness, then call semantic `A.clear_interface(bank)` assignment (`C:298-306`). The source calls this “the remaining literal-composition wall.” |
| Repeat a recurrent step | Host `applications` integer | Re-run decoded instrumentation and the classical word (`T:249-268`) |

The decisive noncompiled state-dependent branch is `C:300-305`: Python reads
`POINTER` and performs source cleanup by assignment. The larger
`semantic_chain_step_with_host_source_cleanup(...)` function itself
(`C:258-306`) is only a semantic scheduler; it is not an emitted gate word.

Other Python control is build-time program generation rather than runtime
decoded-state control:

- `P.full_physical_word()` fixes the seven-segment global order
  (`P:775-832`).
- `P.shift_physical_word()` host-loops over six directions, all stations, and
  39 lanes. Those loops do emit literal gates, but emit them unconditionally;
  only the `omit` deletion flag changes the compiled word (`P:750-772`).
- `T.classical_word()` host-loops over two forward then two reverse edges and
  builds a static stage list (`T:148-211`).
- `T.classical_word(edge_local_predecessor=...)` chooses at compile time
  between a six-bit structural prefix and an edge-latch-controlled predecessor
  bit (`T:165-182`).
- `C.structural_prefix_word(bank_index)` reads Python `bank_index` bits to
  decide which HEAD prefix gates exist (`C:128-150`).
- `deletion`/`omit` branches in all three files are certificate mutation
  switches, not candidate controller inputs.
- `instrument_tagged()` branches on `SOURCE_POINTER` only to append diagnostic
  history (`T:227-246`); `state_issues()` and the certificate loops are also
  observers, not controller logic.

`T.classical_word()` does eliminate the hosted cleanup for its fixed
three-bank case by compiling `source_compute_word()` and
`source_uncompute_word()` (`T:124-145`, `T:197-211`). However, it assumes the
source is fixed at bank 0, statically traverses both edges, and uses a supplied
three-bank layout and fixed edge order. It is a useful finite unrolling, not a
token-relative DOWN/ACK wavefront controller.

## 4. Reusable precedents for literal decision logic

The missing controller does not require inventing a Boolean lowering style:

- **Positive/negative controlled predicates.** `P.zero_controlled(...)`
  (`P:172-182`), `C.controlled_latch(...)` (`C:43-50`), and
  `T.controlled_latch(...)` (`T:73-83`) convert a conjunction of required-one
  and required-zero bits into an MCX-controlled latch using clean work.
- **Controlled transport.** The three-gate Fredkin macro
  (`P:185-186`, `C:53-54`, `T:86-87`) coherently gates swaps without a host
  branch.
- **Complete-blank refusal.** The commit predicate reads all 39 destination
  bits and refuses dirty, unlawful, zero/two-direction, or zero-pointer states
  (`P:200-211`, `P:413-435`).
- **Persistent refusal/retry state.** `pending_latch_segment()` retains a
  blocked event and later transfers that state to typed `retry_echo`
  (`P:256-267`, `P:287-303`, `P:437-462`).
- **Admission-gated allocator motion.** `safe_packet_body_word()` replaces the
  token-move subword with controls on
  `POINTER/DIRECTION_OK/BINDER/ACTUAL/ADMISS/LAW`, token, and destination-valid
  bits (`C:85-125`).
- **Preimage/postimage latch cleanup.** `pre_latch_word()` computes an edge
  authorization before destructive motion, and `post_latch_word()` recomputes
  it from the packet postimage to clean the latch (`C:157-178`, `C:201-228`).
- **Separate handoff and carrier-only relay guards.** `T.relay_predicate()`,
  `relay_latch_word()`, and `relay_swap_word()` show how an edge-local control
  can distinguish token handoff from carrier return/relay (`T:90-121`).
- **Static ROM/program precedents.** `C.structural_prefix_word(bank_index)`
  compiles Python-provided bank-index bits into HEAD-writing gates
  (`C:128-150`). `T.classical_word()` is an explicit labeled program table of
  forward, packet, reverse, and cleanup stages (`T:148-211`). These are
  precedents for compiling a supplied table, not derivations of its content.

## 5. Synthesis for the Cycle-726 spec writer

### 5.1 Smallest honest target

The smallest honest target is one additional literal, routed M2 gate word,
conceptually:

`wavefront_controller_word(layout, supplied_transition_program)`.

It must:

1. carry an explicit reversible local phase encoding such as
   `IDLE/DOWN/ACK` at each relevant source/edge/station;
2. coherently read, without measurement or Python inspection:
   - phase ownership and phase value;
   - source `POINTER`, endpoint/direction bits, and the four law/admission bits;
   - allocator `TOKEN`, `FRESH`, `HEAD`, `ROTOR`, cell-valid, and interface
     bits;
   - destination packet/rail blankness, link latch/work cleanliness, local
     `pending`, and rail `start/valid/cleanup/retry_echo`;
3. compute clean enable latches for the already-emitted shield/decode/commit,
   forward handoff/relay, shift, return, and source-cleanup macros;
4. gate those macros so only the phase-authorized site/edge acts;
5. update DOWN to the next local site, convert DOWN to ACK only on the defined
   commit/refusal outcome, and propagate ACK back;
6. compile the `POINTER`-conditioned source cleanup now hosted at `C:300-305`;
7. uncompute all enable/phase work and return every nonpersistent controller
   rail clean; and
8. lower, physically place, and nearest-neighbor route the controller together
   with the existing word. No Python state branch, source scan, application
   loop, or edge-order loop may remain in the runtime map.

The existing fixed unrollings are acceptable as a compiler technique: Python
may generate a finite literal word from a supplied topology/program. What must
disappear is runtime semantic selection by Python. A wrapped variant must also
show that adding an “enable” to H/T-containing imported decoded words is
implemented by an actual allowed M2 decomposition, not by treating a whole
macro as magically controlled.

### 5.2 Supplies that may remain explicit

The three files already declare the following supplies, which a narrowly
wrapped Cycle-726 result may continue to state honestly:

- the Cycle-713 decoder/source word and clean
  `BINDER/ACTUAL/ADMISS/LAW`, head/rotor/identity/work genesis
  (`P:1255-1262`);
- six A/B loops, blank transient route sites, one clean persistent pending M2,
  twelve clean HOLD M2, and the finite pre-wrap blank/no-return sector
  (`P:1255-1262`);
- clean downstream banks/link tubes, one-hot allocator token, fixed
  forward/reverse edge order, and a structural bank-index prefix ROM
  (`T:433-438`, `C:546-553`);
- finite topology/length, clean rails, and the event/interface input itself.

### 5.3 New supplied data required

The following information is not present in the three files and must be newly
supplied or derived before “compile the DOWN/ACK controller” is a determinate
task:

- **NEW SUPPLY:** exact controller-state encoding and wire/site layout
  (`IDLE/DOWN/ACK`, ownership, and any epoch/parity bits);
- **NEW SUPPLY:** complete local transition/output table, including successful
  commit, pending/refusal, empty event, dirty/unlawful destination, exhaustion,
  boundary, and pre-wrap/wrap cases;
- **NEW SUPPLY:** wavefront genesis/boundary injection and which phase initially
  owns the source;
- **NEW SUPPLY:** whether shift is a global clocked layer or a phase-gated local
  action, and its exact relation to commit and ACK return;
- **NEW SUPPLY:** finite topology/program length and boundary behavior if these
  are not fixed compiler parameters;
- **NEW SUPPLY unless replaced by an edge-local derivation:** the six-bit
  structural bank-index ROM contents used by `structural_prefix_word()`;
- **NEW SUPPLY unless derived:** clean controller ancillas and clean
  DOWN/ACK/rail genesis.

The current files do not justify silently choosing any of these.

### 5.4 Certificates a wrapped variant must rerun

To establish “lawful behavior unchanged,” the wrapped controller must rerun at
least these existing surfaces:

- `P.structured_commit_certificate()`: packet, full 34-bit raw payload,
  controller, transient/work, one-event, inverse, refusal, pending-latch,
  arbitrary-inverse, and deletion checks;
- `P.pending_shield_certificate()`: all 4,096 matter rows, vacuum, returned
  work, and shield deletions;
- `P.shift_semantic_certificate(13/17)`: bundle shift, inverse, and pre-wrap;
- `P.routed_layout_certificate(13/17)`: placement, all segment counts, pre-route
  shift locality, routed NN/operand-order/return/deletion, support scaling, and
  the routed hash;
- `P.active_covariance()`: 24 frames, 576 products, translations, and routed
  NN covariance;
- repeated `S.clean_domain_certificate(13/17)` acceptance as invoked at
  `P:1149-1237`, including applications 1/2/4, intertwiner, norm, particle
  leakage, and bad packet/auxiliary weight;
- `T.domain_certificate()` and `T.deletion_certificate()`: identical-word
  recurrence at applications 2 and 4 and active relay/handoff/source-cleanup
  deletions (`T:335-394`);
- `C.certificate()` and `C.persistent_chain_certificate()`: all 32 rotor/
  direction rows, exact inverse and clean link work, carrier-return deletion,
  all `3^6` mixed sequences, held 2/5/12-bank fills, and forward/reverse
  edge-order comparisons (`C:369-439`, `C:442-589`).

The controller needs additional certificates not currently present:

- exhaustive equivalence of the controlled wrapper to the existing fixed word
  on every declared lawful phase/input row;
- identity/refusal on every declared non-enabled and off-code controller row;
- DOWN/ACK transition-table coverage and active deletion witnesses for each
  branch;
- exact arbitrary-state inverse and clean return of all controller work;
- conservation of the single active wavefront/ACK ownership token;
- no early source cleanup and no shift/commit before the authorized phase; and
- fresh placement, NN routing, covariance, and support-scaling results with
  the controller gates/sites included.

## COMPLETENESS

This extraction identifies the available local semantic predicates, exact
host-side scheduling and state branches, physical word/layout conventions,
static counts, existing decision-logic precedents, required retained
certificates, and every controller datum that is absent from the three scoped
files. The precise gap is narrower than “make the WORD physical” but deeper
than a mechanical lowering pass: the commit/shield/shift words are already
physical, while the autonomous DOWN/ACK phase state and its complete
transition/output table are not specified here and therefore are not compiled.
