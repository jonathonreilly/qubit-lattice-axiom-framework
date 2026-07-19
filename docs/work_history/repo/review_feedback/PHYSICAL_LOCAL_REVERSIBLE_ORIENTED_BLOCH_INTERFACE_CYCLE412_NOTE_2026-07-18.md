# Physical local reversible oriented-Bloch interface — Cycle 412 note — 2026-07-18

Authority: none
Audit: unset

## Question and disposition

Cycle 408 derived a frame-covariant finite effect identifier

\[
Q_{13}(F)=(s,x,y,z)\in\mathbb Z^4
\]

and the proper-cubic action

\[
g\cdot(s,\mathbf v)=(s,g\mathbf v),\qquad g\in O, |O|=24.
\]

Cycle 412 asks whether that already-derived action can be compiled into a bounded local reversible nearest-neighbor M2 interface with a five-M2 proper-cubic frame label, one fixed state-independent circuit, and an exact inverse.

The finite answer is constructive. The interface encodes every one of Cycle 408’s 3,347 installed classes, applies all 24 signed-permutation actions with a fixed X, CNOT, Toffoli, and SWAP circuit, and obeys all 576 products. Every gate in the final circuit is nearest-neighbor on a fixed one-dimensional 182-M2 chain. The reversed gate schedule restores every raw input bit exactly.

Certificate shorthand: all 24 frames; 182 M2; 138-M2 active support union. Invalid frame, overflow, and dirty-work domains reject.

Effect-to-tuple genesis remains supplied, and the 13-decimal resolution remains supplied. This cycle compiles the action on the tuple; it does not physically derive the tuple from an arbitrary effect matrix.

## Register encoding

The installed finite surface has these exact bounds:

- scalar integer: (0\le s\le9{,}389{,}470{,}280{,}759), requiring **44 scalar M2**;
- Bloch magnitude: (max(|x|,|y|,|z|)=4{,}285{,}714{,}285{,}714<2^{42});
- each Bloch coordinate: **one sign plus 42 magnitude M2**;
- proper-cubic frame label: **five M2**, with basis labels 0–23 lawful and 24–31 rejected by the application domain;
- equality flag: one clean M2;
- multi-control work: three clean M2.

Thus tuple storage is

\[
44+3(1+42)=173\ \mathrm{M2},
\]

and the complete interface is

\[
173+5+1+3=\mathbf{182\ M2}.
\]

### Local zero-sign gauge

A sign-magnitude representation has two bit strings that decode to integer zero. Cycle 412 retains the sign of a zero-magnitude coordinate as a local zero-sign gauge. A cubic sign flip therefore acts with one CNOT on the sign bit even when the magnitude is zero. The decoder maps both gauge values to zero.

This choice is load-bearing and explicit:

- raw circuit evolution is a permutation on all register bits;
- composing signed permutations acts exactly on the zero-sign gauge as well as nonzero coordinates;
- reversing the gate list restores the original zero gauge exactly;
- no nonlocal canonical-zero cleanup or host-side repair is invoked.

The raw carried relation is (E_{gQ,\gamma'}=U_gE_{Q,\gamma}), where (gamma) is the local zero-sign gauge. After decoding, (D U_g E(Q)=gQ). It would be incorrect to require every output zero to use the positive-zero representative while also claiming the sign flip is a bare reversible CNOT.

## Fixed reversible circuit

For each of the 24 frame labels, the schedule contains a statically compiled branch:

1. temporarily X the zero-valued frame-label controls;
2. compute a one-hot equality flag with a five-control X decomposed into seven Toffolis and three clean work M2;
3. restore the frame-label bits;
4. conditionally permute the three 43-M2 signed registers;
5. conditionally flip the required output sign bits;
6. reverse the equality computation and return flag/work to zero.

Exactly one branch activates for a lawful five-M2 frame label. The source application routine only applies the prebuilt gate tuple; it contains no frame query or program-dependent circuit construction.

### Conditional register permutation

For a frame row (g_{ij}=\epsilon_i\delta_{j,\pi(i)}), output coordinate (i) receives input register (pi(i)). The three-register permutation is synthesized into at most two register transpositions. Each controlled bit SWAP uses

\[
\operatorname{CNOT}(a,b),\quad
\operatorname{Toffoli}(f,b;a),\quad
\operatorname{CNOT}(a,b),
\]

which is identity when flag (f=0) and exchanges (a,b) when (f=1). Negative output rows then CNOT the flag into the corresponding sign bit.

Every primitive is self-inverse. Reversing the complete 4,256-gate logical schedule is therefore the exact inverse, including frame, flag, work, scalar, magnitudes, signs, and zero-gauge bits.

## Nearest-neighbor compilation

The logical circuit uses only X, CNOT, and Toffoli. A fixed gate-by-gate router compiles it to a one-dimensional NN circuit:

- route each logical gate’s operands into a contiguous one-, two-, or three-M2 block with adjacent SWAPs;
- apply the logical gate on that block;
- reverse the same adjacent SWAPs so the global site layout is restored before the next gate.

The compiler checks the routed logical operands, every central gate, every adjacent SWAP, and exact layout restoration for every logical gate. The resulting schedule contains X, CNOT, Toffoli, and SWAP only, is state-independent, and has maximum gate neighborhood three M2. It contains exactly **636,944 routed NN gates**: 272 X, 2,444 CNOT, 1,540 Toffoli, and 632,688 SWAP gates. Its schedule SHA-256 is `6335acb950d74afb61a0fef9cf9bb2e9238f0dfe603757577614cbf5b2a9b7b5`.

This is a conservative router: it minimizes no gate count or depth. No minimum-resource claim is made.

## Exact finite tests

### All classes, frames, inverse, and products

The runner encodes all 3,347 installed Route-B identifiers under all 24 lawful frame labels, giving 80,328 full circuit cases. It verifies:

- decoded circuit output equals the exact Cycle-408 signed-permutation action;
- every scalar bit and frame-label bit is unchanged;
- flag and all work bits return to zero;
- reversing the same fixed circuit restores all 182 raw bits;
- negative-zero gauge outputs occur and decode to integer zero as declared.

It then checks every installed class against all 576 ordered frame products, totaling 1,927,872 class-product tests, plus 80,328 inverse-frame tests. All compare the sequential signed-permutation action to the exact proper-cubic multiplication table.

### Deletion and lawful domain

Three load-bearing gate deletions are attacked independently:

- one sign CNOT;
- one controlled-SWAP core Toffoli;
- one frame-equality target Toffoli.

Each produces visible raw-basis failures on the selected frame’s installed classes; the deleted equality gate also exposes dirty control state where applicable.

The application domain rejects:

- frame labels 24–31;
- scalar or Bloch-magnitude overflow;
- negative scalar or malformed identifier width;
- dirty flag or work ancillas;
- malformed basis-state width or non-bit entries;
- malformed gates and gates outside the 182-M2 chain.

The underlying unitary has an identity extension on invalid frame labels because none of the 24 flags activates. That extension does not make labels 24–31 lawful inputs.

## Locality and overhead

| Quantity | M2 |
|---|---:|
| Scalar spectator | 44 |
| Three signed Bloch registers | 129 |
| Frame label | 5 |
| Flag plus work | 4 |
| **Complete interface** | **182** |
| **Active support union** (Bloch + frame + flag/work) | **138** |
| Maximum primitive gate neighborhood | 3 |

The scalar is a circuit spectator. Combined conservatively with the Cycle-404 cross-program compiler:

- active support union: (32+138=170) M2;
- patch: (68+182=250) M2;
- installed overhead per bank: (35+182=217) M2.

These are constant per compiled cell/bank and do not depend on lattice size or the number of installed classes. The long static gate schedule changes depth, not spatial support or register overhead.

## Held physical and Record spectators

The codec register is disjoint from physical matter/contact and prior Record registers. Its combined action is (U_{\mathrm{codec}}\otimes I_{\mathrm{physical,Record}}). The runner rechecks:

- `E G_logical = G_physical E` at L=3 and held L=6;
- held leakage and role constraints;
- all 24 physical proper-cubic frames;
- the one-particle mass fixture;
- the Cycle-230 contact intertwiner;
- the Cycle-364 prior Record signature;
- the Cycle-399 Record hash.

The prior framework Record identities are spectators and remain unchanged. The codec circuit creates no occurrence, selects no member, appends no framework Record, and adds no dependency edge.

## Supplied structure and residual boundary

Supplied:

- Cycle 408’s 3,347 installed oriented-Bloch identifiers;
- effect-to-tuple genesis and the 13-decimal resolution;
- a five-M2 frame-label basis state for each invocation;
- clean flag and work preparation;
- the physical/Record spectator tensor factorization;
- inherited L3/L6 physical, mass, contact, and Record fixtures.

Derived:

- the 44 + 3 × 43 sign-magnitude encoding;
- the local zero-sign gauge action;
- the fixed 24-branch X/CNOT/Toffoli schedule;
- exact reversed schedule;
- the one-dimensional NN SWAP routing and bounded overhead certificate;
- every finite class/frame/product result above.

Open and not claimed:

- physical effect-to-tuple computation from arbitrary matter/apparatus state;
- a physical derivation of the 13-decimal resolution;
- frames outside the 24-element proper-cubic group;
- effects outside the Cycle-408 finite surface;
- universal effect identity or universal menu eligibility;
- Born selection, probability, actuality, time, interval, rate, source, stress, gravity, or history realization;
- Record creation, minimum content, a global no-go, or axiom pressure.

## N1–N8 discipline gate

### N1 — Alternative route enumeration

Six constructive/adversarial routes are explicit:

1. **ATTEMPTED — sign-magnitude plus zero-sign gauge:** selected constructive route.
2. **ATTEMPTED — exact reverse schedule:** tests full raw reversibility rather than decoded output alone.
3. **ATTEMPTED — all 576 products:** tests composition beyond single-frame action.
4. **ATTEMPTED — NN route-and-restore:** compiles nonlocal logical operands without state-dependent routing.
5. **ATTEMPTED — dirty/invalid/deletion attacks:** tests lawful-domain and load-bearing gates.
6. **LIVE EXTENSION — two’s-complement or arithmetic tuple genesis:** could remove the zero gauge or physically derive tuple arithmetic, but is not needed for the finite action result.

No route disposition is promoted to a minimum or impossibility statement.

### N2 — Condition-independence audit

The conditions are:

- W1: supplied finite Route-B tuple table and 13-decimal resolution;
- W2: sign-magnitude encoding with local zero-sign gauge;
- W3: supplied five-M2 frame label and 24-state lawful code;
- W4: clean flag/work ancillas and fixed multiplexed circuit;
- W5: disjoint physical/Record spectator factorization.

| Pair | Independence result |
|---|---|
| W1–W2 | Tuple values do not uniquely choose a reversible signed representation. |
| W1–W3 | Effect identifiers do not prepare a frame label. |
| W1–W4 | A tuple table does not provide clean circuit work or a gate schedule. |
| W1–W5 | Numerical identity does not imply physical/Record factorization. |
| W2–W3 | Integer encoding and frame-label preparation are separate. |
| W2–W4 | Sign representation does not synthesize the multiplexor or clean work. |
| W2–W5 | Zero gauge and spectator factorization address distinct registers. |
| W3–W4 | A frame label does not itself implement the controlled action. |
| W3–W5 | Frame control does not imply matter/Record identity action. |
| W4–W5 | Circuit ancillas and spectator factors are independently supplied. |

### N3 — Hidden-condition scan

The load-bearing finite tuple table, decimal resolution, sign-magnitude convention, zero gauge, frame preparation, clean work, fixed schedule, and spectator factorization are named. “By construction” is not used to hide a physics import: route-and-restore and tensor-spectator claims have executable structural checks.

### N4 — Residual matching

| Witness | Witness residual | Cycle-412 residual | Match? |
|---|---|---|---|
| Cycle 408 Route B | exact integer signed-permutation action | decoded circuit action | yes |
| Cycle 408 frame table | 24 frames and 576 products | circuit product/inverse tests | yes |
| Cycle 404 physical compiler | E/G, leakage, mass/contact | disjoint spectator preservation | yes |
| Cycles 364/399/406 | prior Record identities/hashes | Record spectator preservation | yes |

Born, time, and source-response residuals are not used as witnesses for the tuple circuit.

### N5 — Rhetoric audit

Tests cover bit, gate, routed segment, complete circuit, installed class, frame, frame product, physical factor, and prior Record identity. The constructive statement is restricted to the finite Route-B action. It is not widened to arbitrary effects, arbitrary rotations, tuple genesis, probability, time, source, gravity, or realization.

### N6 — Partial-closure path scan

Cycle 412 closes the action-compiler interface while leaving tuple genesis and resolution explicitly supplied. A two’s-complement encoding, interval-certified tuple arithmetic, or a physical effect-to-register transducer could retire additional imports without changing axioms. No new primitive or constitutional conclusion follows from this local circuit.

### N7 — Steelman

A hostile reviewer can demand a much smaller arithmetic representation, a depth-optimized three-dimensional NN placement, coherent frame superpositions with physically generated labels, or an exact transducer from the apparatus effect to its integer tuple. Those routes could materially reduce overhead or close tuple genesis. They do not invalidate the present fixed finite compiler, so Cycle 412 makes no optimality or universality claim and names them as next constructive work.

### N8 — Cross-cycle echo

- Cycle 323 physically embedded fixed bounded program carriers.
- Cycle 404 installed a local reversible XOR program rewrite.
- Cycle 408 replaced frame-sensitive re-keying with an exact oriented integer group action.
- Cycle 412 compiles that action into an explicit reversible NN M2 circuit.
- Cycles 364/399/406 provide the prior Record identities preserved as spectators.

The echo is constructive and dependency-tracked; it supplies no shared substrate obstruction.

## Claim status

- Finite Route-B local reversible action circuit: constructive.
- Exact inverse, 24 frames, and 576 products: constructive.
- NN locality and constant overhead: constructive for the declared layout/router.
- Effect-to-tuple genesis: supplied, not physically compiled.
- 13-decimal resolution: supplied, not physically derived.
- Born selection: not claimed.
- Universal effect identity: not claimed.
- Time/source/gravity: not claimed.
- Axiom pressure: not claimed.
- Authority: none.
- Audit: unset.
