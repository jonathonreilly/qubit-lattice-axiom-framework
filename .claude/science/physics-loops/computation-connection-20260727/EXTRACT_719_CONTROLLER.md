# Cycle-719 two-rail controller + refusal primitive — structured extraction

Source scope:

- `scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py`
  (“core” below).
- `scripts/frontier_cycle719_recurrent_matter_history_controller_2026_07_26.py`
  (“runner” below), restricted to the requested controller/refusal/program/
  station/held-orbit regions.

## 1. Controller program

### `PROGRAM` and 130 stations

- `interleaved_program(bank_count, *, physical_padding=False)` returns station
  rows `(kind, index, local)` (core L90-L124).
- Exact program grammar (core L92-L114):
  - start: `("source", 0, R3.source_compute_word())`;
  - each bank: `("bank", bank, H.PACKET)`;
  - after bank 0: `("cross", bank-1, ())`;
  - before every next bank:
    `("handoff", bank, H.HANDOFF_FORWARD)`,
    `("relay", bank, H.RELAY_LATCH)`,
    `("relay", bank, H.RELAY_SWAP)`;
  - descending reverse edges:
    `("relay", edge, H.RELAY_SWAP)`,
    `("relay", edge, H.RELAY_UNLATCH)`,
    `("handoff", edge, H.HANDOFF_RETURN)`;
  - end: `("finalizer", 0, M.source_finalizer_word(bank_count))`.
- Unpadded length is `8*bank_count-5`: 11/35/91 stations for 2/5/12 banks.
- The physical 12-bank case adds two identities after each nonzero reverse
  edge, 15 identities before the reverse block, then tail identities to
  exactly 130; other padded bank counts are rejected (core L110-L124).
- `held_physical_program_and_track(bank_count)` fixes physical station counts
  11/45/130 for 2/5/12 (core L361-L377). Tracks are rectangular perimeters
  with `len(track)==2*len(program)`; the fixtures are `rectangle_track(3,10)`,
  `(5,42)`, and `(12,120)`.
- Runner constants are `BANKS=12`,
  `PROGRAM, CONTROLLER_TRACK = K.held_physical_program_and_track(BANKS)`,
  `ALLOCATOR=K.program_word(PROGRAM)` (runner L120-L123). Thus runner
  `PROGRAM` is the padded 130-station program, with 91 nonidentity macro
  stations and 39 identities.

### Station-to-macro mapping

- `mapped_macro(row)` returns `tuple(local)` for `source/finalizer`, `()` for
  `identity`, otherwise `H.mapped_action(kind,index,local)` (core L127-L133).
- `program_word(program)` concatenates `mapped_macro(row)` in station order;
  `gate_digest(word)` hashes each gate kind and wire tuple (core L136-L141).
- `controlled_macro(word, control, work)` is the exact controlled-data macro
  lift (core L144-L155):
  - `X(target)` → `A.cn(control,target)`;
  - `CNOT(data_control,target)` →
    `A.tof(control,data_control,target)`;
  - `TOF(c1,c2,target)` →
    `A.mcx((control,c1,c2),target,(work,))`.
- Only X/CNOT/TOF are accepted. `control` is the station’s A bit; original
  data controls/targets are preserved; `work` is the station-local
  decomposer bit for the three-control MCX. A “controlled macro” is this
  lift of the complete mapped station macro, not a single gate.

### A/B/work rails and one-token ring

- `controller_word(program,data_wires)` uses contiguous registers (core
  L162-L178): data; `A[data_wires:data_wires+P]`;
  `B[data_wires+P:data_wires+2P]`; then P work bits. Total width is
  `data_wires+3P`.
- Supplied code/genesis is `A_0=1`, all other A=0, all B/work=0, plus clean
  data-bank/link/route genesis (core L554-L559).
- `swap_word(left,right)` is exactly three CNOTs:
  `CN(left,right), CN(right,left), CN(left,right)` (core L158-L159).
- One step is `H=R Q`: `controller_word` returns `q+r1+r2`.
  Q contains every station’s A-controlled macro; R1 swaps `(A_s,B_s)`; R2
  swaps `(B_s,A_(s+1 mod P))` (core L165-L178). On the one-token code the
  token advances one station, and H^P executes one program orbit.
- `apply_controller_step(data,program,a_tokens,b_tokens,*,reverse=False,
  q_order=None)` implements forward Q/R1/R2 and reverse R2/R1/reversed-Q
  (core L181-L206). Controller ordinals/orbit length P are circuit structure,
  not physical time (core L4-L7, L573-L577).

## 2. `K.controller_word`, widths, and held orbits

### Word builders and runner width

- Builder stack:
  `interleaved_program → mapped_macro → controlled_macro → Q`;
  `swap_word → R1/R2`; `controller_word → Q+R1+R2`.
- In the runner, `K.controller_word` is that core function.
  `CONTROLLER_DATA_WIDTH = M.R12.TOTAL_WIRES` is symbolic, not hard-coded
  (runner L129).
- Exact runner layout constants (runner L129-L136):
  `CONTROLLER_STATIONS=len(PROGRAM)`;
  `CONTROLLER_H_WORD=K.controller_word(PROGRAM,CONTROLLER_DATA_WIDTH)`;
  A base=data width; B base=A base+P; work base=B base+P; full width=work
  base+P.
- `fast_classical_word(word)` maps X/CNOT/TOF to opcodes 0/1/2 without
  changing wires/order. `CONTROLLER_H_FAST` compiles H;
  `CONTROLLER_H_INVERSE_FAST=tuple(reversed(CONTROLLER_H_FAST))`
  (runner L139-L145).

### Held 2/5/12 certificates

- `run_orbit(data,program,*,token_positions=(0,),reverse=False,q_orders=None)`
  constructs A from `token_positions`, B=0, applies exactly P controller
  steps, and records `(live_A_before,live_A_after,sum(B))` (core L209-L223).
- `held_certificate(bank_count)` uses the unpadded 11/35/91-station programs
  and runs `2*bank_count` alternating endpoint events (core L226-L271). Each
  event checks:
  - H^P data equals `M.global_allocator_word(bank_count)`;
  - A returns to A0 and B returns zero;
  - reverse H^P restores data/A/B exactly;
  - decoded graph equals the Cycle-610 chain;
  - pointer, bank transient/work, and links meet the clean postimage.
- Exact counters are `logical_failures`, `fixed_word_failures`,
  `inverse_failures`, `postimage_failures`, `token_return_failures`.
  Core `main()` calls `held_certificate` for 2/5/12 and requires all zero
  (core L492-L507).
- `physical_controller_certificate(bank_count)` separately uses physical
  11/45/130 fixtures, builds H, and routes H and reversed H; core `main()`
  runs it for 2/5/12 (core L432-L496).

### Actual compiled H^130 and held matter/history

- `controller_full_input(data_basis)` sets only A0; `controller_register_rows`
  decodes data/A/B/work (runner L608-L627).
- `compiled_H_orbit_certificate()` executes the actual 61,562-gate H word
  130 times on all six Cycle-713 origin-0 branches, compares with
  `K.run_orbit`, checks A/B/work return, reverses H 130 times, and requires
  exact full-register restoration (runner L630-L738).
- Exact counters: `compiled_host_equality_failures`,
  `compiled_inverse_failures`, `controller_register_return_failures`,
  `suffix_decoded_domain_failures`; row checks:
  `compiled_equals_host`, `A0_return`, `B_vacuum_return`, `work_return`,
  `inverse_exact`.
- `actual_compiled_H_orbit` requires six branches, 61,562 gates/H,
  130 H/orbit, 8,003,060 gate applications/branch, all four failure counters
  zero, and active packet/finalizer/source deletion controls (runner
  L1331-L1343).
- `recurrent_certificate(origin,steps,transition,*,inverse=False)` checks
  decoded logical intertwining, norm, decode/pointer/transient/number
  failures, packet count/support, and optional joint inverse (runner
  L501-L544). Runner `main()` holds all 12 origins for two steps, origin 0
  for five, and origin 0 through 24 packets (runner L1257-L1259). Only the
  first-event six branches literally execute compiled H^130; longer held
  recurrence uses the proven-equal host orbit (runner L1459-L1464).

## 3. Exact refusal primitive

- Signature: `local_refusal_primitive()` (runner L741-L800).
- Five M2/wires are `a,b,work,syndrome,data=range(5)` on collinear sites
  `(0,0,0)`…`(4,0,0)` (runner L743, L771).
- Exact semantic word (runner L744-L751):

  ```text
  CNOT(B, syndrome)
  CNOT(work, syndrome)
  TOF(B, work, syndrome)
  X(syndrome)
  TOF(A, syndrome, data)
  X(syndrome)
  ```

- First three gates compute
  `syndrome ^= (B OR work)`. For supplied syndrome=0, output
  `syndrome := B OR work`; data flips iff `A AND NOT syndrome`. A/B/work are
  unchanged.
- Clean-syndrome truth row is exactly
  `(A,B,W,0,D) → (A,B,W,invalid,D XOR (A AND NOT invalid))`,
  `invalid=B OR W` (runner L752-L763).
- It exhausts 16 clean rows; `truth_failures` must be zero. Exactly six live
  invalid rows are refused: A=1, any of three nonzero `(B,W)`, either D.
- `K.streaming_route(word,sites)` expands this to 34 physical primitives and
  60 routed NN gates. Returned route fields are `physical_primitives`,
  `routed_NN_gates`, `maximum_route_distance`, and `route_failures`, the last
  summing non-NN, operand-order, and route-return failures (runner L771-L794).
- Dirty initial syndrome is compared with clean over all 16 A/B/W/D rows;
  `dirty_syndrome_rows_changing_action=16` (runner L764-L770).
- Deletions are exact:
  `deleted_or=word[:2]+word[3:]` and
  `deleted_guard=word[:4]+word[5:]`. Over syndrome=0 rows,
  `deletion_rows_changed=6` (four OR-Toffoli rows plus two guard rows)
  (runner L773-L782).
- `diagnostic_local_dirty_refusal` requires truth/route failures=0,
  `invalid_live_token_rows_refused==6`, and positive dirty-syndrome/deletion
  counters (runner L1370-L1375).
- Integration status: diagnostic at one Q station, leaves a syndrome receipt,
  still assumes clean syndrome genesis, and is **not wrapped around every
  controlled data macro** (runner L795-L799, L1436-L1454).
  `CONTROLLER_H_WORD` and `physical_controller_block` still call unwrapped
  `K.controller_word` (runner L131, L885).

## 4. Dirty-sector controls today

### Unlawful token orbits

- Core `order_and_domain_controls()` checks shuffled-Q equality, inert/returning
  zero-token sector, conserved-but-different two-token output, packet deletion,
  and R-before-Q falsifier (core L307-L349). Core requires all booleans true.
- Runner `sparse_controller_orbit` reports `token_return_failures` and
  `B_vacuum_return_failures` (runner L363-L387).
- `controller_sector_controls()` compares lawful A0 with no token, adjacent
  `(0,1)`, distant `(0,P//2)`, and offset `(1,)`, then reverses lawful output
  (runner L560-L605).
- Exact returned fields are:
  `lawful_token_return_failures`, `lawful_inverse_residual`,
  `lawful_inverse_token_failures`,
  `zero_token_data_residual_from_unallocated_matter`,
  `zero_token_residual_from_lawful`,
  `adjacent_two_token_residual_from_lawful`,
  `distant_two_token_residual_from_lawful`,
  `offset_token_residual_from_lawful`, and zero/adjacent/distant/offset
  `*_token_return_failures`.
- `hostile_controller_sectors` requires lawful return counters=0, lawful
  inverse `<TOL`, zero-token unallocated-data residual `<TOL`, all four
  residuals from lawful `>1e-3`, and all hostile return counters=0 (runner
  L1356-L1368). These diagnose sectors; they do not enforce unique-token
  genesis.

### Dirty B/work

- Core `controlled_truth_certificate()` returns `clean_rows`,
  `clean_failures`, `clean_work_return_failures`,
  `dirty_rows_outside_domain`, `dirty_rows_changing_declared_action`
  (core L274-L304). Dirty decomposer-work is outside its domain; core requires
  zero clean failures/returns and positive dirty-action differences.
- Runner refusal adds the exact 16-row B/work truth surface and counts above,
  but only locally and with clean incoming syndrome. No full H uses it.

## 5. Routing/covariance surfaces

### Core

- `streaming_route(semantic_word,wire_sites)` expands via `A.expanded`, routes
  two-site gates on Manhattan paths, and returns:
  `physical_primitives`, one/two-M2 counts, `routed_NN_gates`,
  `maximum_route_distance`, non-NN/operand-order/route-return failures,
  route-swap deletion count, touched M2, and route digest (core L380-L429).
- `physical_controller_certificate` uses shared data sites, alternating A/B
  track sites, and work `(x,y-1,z)` below A (core L432-L449). It checks
  placement collisions, cyclic rail NN, forward/inverse routes, all proper
  cubic frames, all ordered frame products, and two translations. Exact
  counters are at core L470-L489; core `main()` reruns them for 2/5/12 and
  requires zero failures (core L513-L529).

### Runner same-chart composition

- `source_physical_caps(layout)` reconstructs/reroutes Cycle-713
  decode/instrument/encode caps, calls
  `M.R12.active_frame_certificate(word,routed)`, and binds pointer sites and
  routed digest/counts (runner L803-L873).
- `physical_controller_block(bank_count)` maps the same data/A/B/work order,
  calls `K.controller_word`, expands physical instructions, and checks
  placement (runner L876-L909).
- `stream_route_instructions(instructions)` returns physical/routed and
  one-/two-M2 counts, max distance, three failure counters, and flat digest
  without retaining routed gates (runner L912-L954).
- `ordered_route_composition_certificate(caps)` certifies ordered
  `prefix; H^P; suffix` and inverse RLE manifests. Full P=130 is not flat
  materialized/digested. Held P=11 independently compares direct/RLE forward
  and inverse digests, counts, max distance, and failures (runner L957-L1110).
- `composed_physical_certificate()` binds caps,
  `K.physical_controller_certificate(12)`, ordered route, shared data map,
  pointer M2, route/covariance failures, 24 frames/576 products, counts, and
  digests (runner L1179-L1250).
- Covariance scope is passive transported coordinates, NN routes,
  translations, and proper-cubic closure; program content is not
  independently executed in every frame (runner L1244-L1248).
- A wrapped variant must rerun these same surfaces and failure criteria.
  Controller counts/digests may change; data-map, cap, route correctness,
  covariance, forward/inverse, and held direct/RLE invariants may not.

## 6. REUSE PLAN for Cycle 723

### Hook and required extensions

1. Preserve program rows, `mapped_macro`, R1/R2, and Q-before-R.
2. Add a parameterized builder beside `controlled_macro`, conceptually
   `refusing_controlled_macro(word,A_s,B_s,work_s,syndrome_s,...)`.
   It must guard every X/CNOT/TOF in `word`, not add one sample data-X.
3. Replace the Q call at core L165-L169. Hook once per station macro; do not
   independently recompute refusal before every primitive. Empty identity
   macros can remain `()` unless Cycle 723 explicitly requires receipts at
   all 130 stations.
4. Add per-station syndrome (and any extra clean decomposition ancillas) to
   `controller_word`, all runner base/full-width constants,
   `controller_register_rows`, `controller_full_input`, core/runner physical
   layouts, placement, route, covariance, and M2 accounting.

### “Lawful behavior unchanged”

For A0-only, B/work/syndrome=0, and the same clean data genesis:

- projected data after H^P equals the old allocator/host result;
- A returns exactly to A0; B/work/syndrome return zero;
- reverse H^P restores the complete input exactly;
- Q/R order, token motion, program/deletion semantics, shared data map, and
  Cycle-713 prefix/suffix interface are unchanged.

Rerun/extend:

- core `controlled_truth_certificate`, `order_and_domain_controls`,
  `held_certificate(2/5/12)`, and
  `physical_controller_certificate(2/5/12)`;
- runner `controller_sector_controls`, `compiled_H_orbit_certificate`,
  all `recurrent_certificate` held cases, `suffix_domain_certificate`, and
  deletion controls;
- runner `source_physical_caps`, `physical_controller_block`,
  `stream_route_instructions`, `ordered_route_composition_certificate`
  including held-P11 forward/inverse direct-vs-RLE, and
  `composed_physical_certificate`;
- inherited matter residuals and the independent Cycle-713 EG anchor checked
  in runner `main()` (runner L1253-L1391).

Regenerate, do not copy, the current 61,562/8,003,060 count assertions,
`controller_H_word_sha256`, route/manifest digests and counts, and controller
M2 totals.

### Coupling traps

- The diagnostic is not a drop-in wrapper: it guards one X only.
- Its receipt update is XOR: `syndrome ^= B OR work`. Q includes every
  station block on every H, so an unconditional splice toggles persistent
  dirt repeatedly. Receipt production must occur exactly on the live A visit,
  or use another rigorously reversible design; then re-prove inverse/held
  recurrence.
- Dirty `work_s` cannot also be trusted as MCX decomposition scratch.
  Negative-syndrome control also increases MCX arity, especially for lifted
  data TOF. Add independently clean bounded ancillas or prove a
  dirty-ancilla-safe decomposition.
- Clean syndrome remains supplied; refusal does not enforce unique token.
- Keep `CONTROLLER_H_WORD` in self-inverse classical X/CNOT/TOF gates unless
  `fast_classical_word` and inverse construction are deliberately extended.
- Sample B/work before station-local scratch use and before R.
- Do not share retained syndrome/scratch across station blocks; that breaks
  station-block independence and shuffled-Q reasoning.
- New sites need fresh collision, NN route, frame, translation, forward/
  inverse, and M2 certification.
- Longer 5/24-step recurrence is host-orbit evidence; do not relabel it as
  literal compiled-H execution without adding that execution.

## COMPLETENESS

- [x] Program/stations, H=RQ, gate lift, rails, one-token convention.
- [x] Builders, data width, held 2/5/12 and compiled-orbit certificates.
- [x] Five-M2 refusal, 34/60 construction, exact truth/deletion counters,
  and nonintegration.
- [x] Unlawful-token and dirty B/work residual/counter surfaces.
- [x] Routing/covariance surfaces and bounded Cycle-723 reuse plan/traps.
