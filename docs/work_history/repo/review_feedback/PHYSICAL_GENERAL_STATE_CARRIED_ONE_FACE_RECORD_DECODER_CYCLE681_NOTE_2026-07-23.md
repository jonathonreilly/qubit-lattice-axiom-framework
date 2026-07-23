# Physical general state-carried one-face record decoder — Cycle 681

Status: **PASS — executed one-face basis-FSM plus physical action/corridor compiler**

Authority: **none**

Audit: **unset**

Constitutional effect: **none**

## Frozen scope and exact grammar

Cycle681 asks whether the pinned Cycle654/Cycle660 one-face program can drive its physical actions from record fields rather than a host dispatcher or one expected/action table per record. The declared grammar is exact: an 8-bit magic, 4-bit coordinate width and 6-bit record count `1..32`; then each record has a routed bit and central count `1..5`. A routed record has a three-coordinate start, run count `1..24`, and direction/length pairs with direction in the six signed cubic axes and length `1..129L-1`. Each central gate has one of `H, SDG, S, X, CNOT`, the semantic arity, and in-torus operands. Binary operands are distinct fine-NN roles of the declared one-face data domain. The typed word ends exactly and its total payload fits the pinned 5,680-bit Cycle660 path.

“Complete” includes routed and nonrouted records, all five opcodes, `1..5` central gates, `1..24` runs, and arbitrary lawful sequences of `1..32` records under that physical payload bound. It excludes opcodes 5–7, malformed counts/directions/lengths/coordinates/arities, non-NN binary actions, trailing untyped bits, other faces, autonomous program genesis or blank renewal, a full M64 encoder `E`, and any efficiency or minimum-overhead statement.

## Executed reversible decoder

The decisive object is a literal reversible basis permutation, not the host-side reference parser. `execute_basis_fsm` receives only the encoded program bits. It executes program-bit-to-register XOR loads, typed program-cursor moves, range/arity checks, run counters, and live field-controlled action dispatch. Routed direction and length registers emit every forward SWAP. Live opcode and operand registers emit each central gate. The machine then rereads the fixed-width run fields backward and emits the reverse excursion.

Every record field is unloaded against the same source bits. At most five program-position bookmark tokens make the variable central fields reversible and are cleared. A reversible record-length scan advances the blank controller to the next record without a record-boundary table. At the typed terminal the program cursor returns to its root, the action head takes one reverse cleanup step for every forward action step without firing data calls, and all field, parser, bookmark, microphase and access-subphase state is blank.

The selected-record expected-value rail of Cycle667 is retired, not multiplied. Its same 180 placed roles hold a 178-bit grammar-level field/counter state, leaving two blank roles. The Cycle667 parser tile, typed program path and exact routed CCX lowering remain. Cycle670's 524-cell one-hot head ring and 17 phase rails are reused for an arbitrary number of actions: the head advances modulo 524 during dispatch and retraces exactly during cleanup.

The independent reference parser is used only as an oracle after execution. The literal FSM emits exactly the unchanged **16,790** L3, **17,307** L6 and **17,306** held-L7 actions, with controller basis residual zero. Fifteen independent fixtures cover all opcodes, all six directions, the 24-run/5-central field maxima, mixed routed/nonrouted words, and the 32-record maximum. A record-concatenation induction extends the same transition invariant to every lawful sequence in the declared finite grammar.

## Physical action and access lowering

Opcode bits select the active phase length: `H:1`, `SDG:2`, `S:2`, `X:1`, `CNOT:15`; routed `SWAP` selects the 17-phase Fredkin word. The unary controlled words are checked as exact matrices. CNOT and SWAP reuse the pinned exact CCX and Fredkin words. Inactive phase rails are identity.

For every token-data atom, decoded operand coordinates and the active phase-token neighbor load a signed torus displacement. A carried axis pointer and step counter emit a compact NN access word. This is not a coordinate table. Its unique literal expansion is opening SWAPs, the local support-one/two atom, and the inverse SWAPs. Thus `S^-1 U S` restores arbitrary, including entangled, borrowed carriers. Data-data atoms act only on the grammar's fine-NN binary operands. The access subphase is widened within the retyped field rail to 16 bits; every actual phase remains below capacity.

The literal physical lowering consumes only the executed FSM action trace. It does not receive the host reference decode. Every elementary call has support at most two and every displayed bond is fine-NN. Final decoder, head, subphase and borrowed-carrier leakage is zero.

## Controls

Malformed magic, width, record count, central count, run count, direction, run length, route start, opcode, arity, operand range, binary coincidence/nonlocality, truncation and trailing bits are rejected by both the reference semantics and the executed basis machine. Zero/duplicate cursor or head sectors and dirty/saturated scratch are outside the locally declared code sector; no autonomous repair or penalty dynamics is claimed.

Decoder-factor deletion is executed rather than inferred from counts. A routed five-opcode witness is rerun with each concrete XOR-load, cursor, branch, loop, direction, length, dispatch, marker, record-advance or head-cleanup transition removed. Every run rejects/desynchronizes, changes the semantic gate digest, or leaves controller state nonblank. Range/NN/terminal validators use malformed words that are rejected normally but accepted when precisely that validator is disabled. Phase-factor deletion has a positive operator residual, and deleting any emitted access SWAP leaves a nonidentity carrier permutation.

The reused controller has positive K129 capacity margin at L3/L6/held-L7 and adds no roles beyond Cycles667/670/677. Dynamic corridors reserve no vacuum: all nonactive intersections are borrowed and returned. The carried proper-cubic frame rotates axis priority and directions, so the all24/all576 NN, endpoint and composition controls pass. Six unit translations and ordinary K129 block translations preserve the complete rule. Proper-frame aliases are shared serial carriers under the unique program/head/microphase/access state, not hidden distinct roles.

The unchanged Cycle219 mass residual remains below tolerance. Cycle230 contact deletion remains positive and seam failures remain zero.

## Exact theorem and boundary

For each lawful computational-basis one-face record word, arbitrary data amplitudes and arbitrary borrowed-carrier amplitudes, the executed field machine, exact token-gated macros and catalytic corridors compose to

`E G_record = G_physical E`

with symbolic residual zero on the declared code, conditional on the explicitly supplied/inherited support-one/two realization of the grammar-FSM cursor, counter and address-successor transitions. The result is linear in the data and carrier amplitudes. It does not claim coherent superpositions of program words, all-face arbitration, autonomous program preparation/renewal, full M64 `E`, or efficient/minimum overhead.

One implementation boundary remains explicit. The Python `record_length` loop, `runs_start + run_index*(3+width)` address arithmetic, action-list emission and inverse cursor traversal are an executed logical basis permutation plus inherited atom-lowering recipes. Cycle681 does **not** enumerate those controller transitions into one fully enumerated M2 controller call word. It does enumerate and check the field-selected physical action/macro/corridor side. The correct terminal is therefore an executed reversible basis-FSM plus physical action/corridor compiler and a compositional supplied-transition intertwiner—not an unconditional fully literal physical controller circuit.

Reversible parsing, Bennett-style compute/action/uncompute, finite Boolean circuit synthesis, CCX/Fredkin decompositions, torus counters, and SWAP conjugation are standard prior art. The repo-side novelty is the explicit executed composition on the pinned Cycle654/Cycle660 grammar: exact whole-word basis traces at three sizes, reuse and retirement of the selected comparator rail, field-selected phase/access words, complete controller and carrier return, deletion reruns, and proper-cubic/translation controls. No broader novelty is claimed.

## N1–N8, ledger and next campaign

The current origin/main no-go discipline and proof-search governance were followed. Five normalized routes are recorded. The universal streaming FSM and residual-vector access cursor close positively. A per-record comparator is forbidden for this target; buffered-mobile and direct-uncompressed alternatives remain alternatives, not impossibility evidence. No route miss is promoted to a minimum-content, shared-obstruction or constitutional claim.

`C_ref`, `C_wrap` and `C_local` advance from one selected record to the complete declared one-face grammar: field/control incidence is explicit, the literal controller and carriers return, and no host/per-record table remains. `C_num` is exact finite basis/operator/permutation evidence only. `C_int` preserves the mass/contact/seam fixtures without a new matter law. `C_source` is unchanged.

Axiom pressure: **none**.

Next: materialize every executed grammar-FSM cursor/counter/address transition as one complete support-one/two M2 controller word and delete-test that literal word. Only after retention should a separate campaign compile all-face arbitration. Do not infer program genesis, renewal or a full M64 encoder from this one-face result.
