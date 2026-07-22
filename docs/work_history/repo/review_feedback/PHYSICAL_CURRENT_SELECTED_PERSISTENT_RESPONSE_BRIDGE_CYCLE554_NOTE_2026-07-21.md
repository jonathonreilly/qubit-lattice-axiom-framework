# Physical current-selected persistent response bridge — Cycle 554

Date: 2026-07-21
Authority: none
Audit: unset

## Result

Cycle 554 closes one bounded composition problem.  On the declared local
current/source code, the Cycle-526 outputs `EDGE_PASSED`, `J+`, and `J-` can
drive Cycle 484's persistent source-flag interface and its fixed directional
full-layer response without a host-selected endpoint, source flag, direction,
or sector.  The selected local encoding and physical update obey

\[
E G_{\rm coarse}=G_{\rm physical}E
\]

on the complete lawful Q<=2 code used here.  The construction is local,
constant-overhead per selected seam, reversible, and covariant under all 24
proper-cubic frames.  All 576 frame products close.  The one-particle mass,
Cycle-230 contact, and Cycle-230 seam fixtures remain exact-pinned predecessor
inputs; the appended controller is not claimed to preserve those observables.

This is a current-selected **candidate response coupling**, not a derived
energy-stress source and not a gravity law.  It creates no axiom pressure.

## Exact interfaces read

Cycle 526 supplies the retained physical current word

| name | (`EDGE_PASSED`,`J+`,`J-`) | meaning |
|---|---:|---|
| `NULL` | `(0,0,0)` | no selected seam occupation transfer |
| `PLUS` | `(1,1,0)` | positive oriented number flow |
| `MINUS` | `(1,0,1)` | negative oriented number flow |

The local constraints are `EDGE_PASSED = J+ XOR J-` and `J+ J- = 0`.
Cycle 526 proves the augmented physical update on L5 and held L6 with a
106-M2 selected-seam envelope.  `EDGE_PASSED` is only an event-ready coherent
carrier.  It is not elapsed time, occurrence, or a Record.

Cycle 549 supplies an injective computational-basis encoding of the complete
local source sectors Q0, Q1, and Q2 into the literal 13-M2
M64-times-seven-resource block.  It also supplies the Gray-path,
equality-controlled core, exact Toffoli decomposition, and nearest-neighbor
routing method used below.  Sparse direct sums in the runner are bookkeeping,
not the claimed implementation.

Cycle 484 supplies the selected P8/Suzuki4/B20 directional response, including
the six ten-bit coefficient words, floor arithmetic, product order, dyadic
phase basis, persistent positive source-flag control, inverse convention, and
full-layer delivery controller.  Its tested response implementation was Q1.

The three sources are exact SHA-256 pinned in the runner.  No axiom,
foundation, Qualification, primitive, registry, policy, queue, or audit
surface is edited.

## Selected fixed tensor circuit

For every ordered physical seam install two persistent endpoint flag M2s and
two response blocks.  The local encoding prepares the flags with exactly two
CNOTs:

```text
J-  ──●────────────── retained FLAG_LEFT
      │
0   ──X

J+  ──●────────────── retained FLAG_RIGHT
      │
0   ──X
```

The fixed physical schedule is then

```text
left flagged Suzuki4 response ; right flagged Suzuki4 response
```

Both blocks are always present in the tensor circuit.  The runner constructs
one immutable 115200-slot manifest before seeing a current, sector, or probe.
Every slot records endpoint, Suzuki factor, direction, coefficient-bit
site, flag site, both explicit 13-M2 endpoint words, signed core angle, and
fixed order.  Every literal rotation has twelve data-word equality controls,
one coefficient-bit control, and one persistent-flag control.  Thus:

- `NULL` activates neither block;
- `PLUS` activates the carried right endpoint;
- `MINUS` activates the carried left endpoint.

An independent manifest interpreter traverses that same full installed list
for every case.  Its literal physical input signature is

```text
G_physical(left_word_amplitudes, right_word_amplitudes,
           EDGE_PASSED/J+/J-, two 6x10 coefficient-bit banks,
           retained FLAG_LEFT/FLAG_RIGHT)
```

Each amplitude register is a sparse representation of the full 8192-word
13-M2 computational basis.  Neither an instruction row nor the interpreter
contains a Q field or Q argument.  Q appears only while a test constructs `E`,
labels expected coarse blocks, or decodes leakage diagnostics.
Nonmatching literal word, coefficient, and flag controls make slots identity;
no case constructs or host-selects a gate list.  A separately coded coarse
current-controlled direct sum is the comparison target.  Direction is
carried by six physical coefficient banks and the fixed Suzuki factor order.
No global ordering, parity string, source lookup, direction lookup, or runtime
angle oracle occurs.

If the seam orientation convention is reversed, `J+` and `J-`, the two flags,
the endpoint source tensors, and the endpoint coefficient banks swap.  The
test residual for this involution is exactly zero.  Under a carried
proper-cubic frame the ordered endpoint labels are transformed with the seam;
there is no global coordinate resort.

## Explicit E, G, and inverse

Let the coarse space be the direct sum over the three lawful current words,
the lawful endpoint sector pairs

\[
(Q_L,Q_R)\in\{(0,0),(1,0),(0,1),(2,0),(0,2),(1,1)\},
\]

and the fixed Cycle-484 coefficient words.

For each endpoint, `E` maps abstract basis index `i` in sector `Q` to
`Cycle549.basis_word(Q,i)`, a literal 13-M2 computational word.  It copies the
three current rails, retains the six ten-bit coefficient words, and maps

\[
({\rm FLAG}_L,{\rm FLAG}_R)=(J_-,J_+).
\]

The 64 Q0, 448 Q1, and 1344 Q2 words are individually unique and mutually
disjoint, so the Gram residual of this basis encoding is zero.

Define one directional generator in sector Q by

\[
H_d^{(Q)}=H_{\rm recoil}^{(Q)}-
H_{\rm recoil,omit\ d}^{(Q)}.
\]

The actual inspected supports are:

| sector | dimension | disjoint signed two-state pairs per direction |
|---:|---:|---:|
| Q0 | 64 | 0 |
| Q1 | 448 | 16 |
| Q2 | 1344 | 80 |

For every Q and direction, the runner separately verifies Hermiticity, zero
diagonal, only real `+1/-1` off-diagonal entries, disjoint pair coverage, and
exact sparse reconstruction from the pair rows.  All residuals and failure
counts are zero.  Hence Q0 is exactly identity.  Every Q1/Q2 exponential in a
Suzuki factor is a product of literal signed two-state rotations.  Each pair
is identified by two explicit 13-M2 words and compiled with Cycle 549's
supplied equality/Gray/Toffoli method.  Twelve equality controls plus the
coefficient bit plus persistent flag give the Cycle-484 14-control ladder,
requiring thirteen clean conjunction M2s.  After the supplied exact Toffoli
decomposition the maximum primitive support remains two M2s.

`G_coarse` is the independently implemented current-controlled direct sum of
those directional products.  `G_physical` is the immutable left-then-right
115200-slot list with full instruction-stream digest
`3c5d78871ac434ffc1ee3295be63a1e65883d2eba84209e40bc3f12c3dbcd3e3`.
The runner evaluates all three current words on all six
lawful sector pairs.  The tested identity is `E G_coarse = G_physical E`;
maximum `E G_coarse - G_physical E` residual is
`1.30e-15`.  A coherent superposition across all three lawful current words
has residual `1.96e-16`.  A single physical word register coherently spanning
Q0, Q1, and Q2 has residual `1.08e-15`; wrong-sector, off-code, and coherent
off-code terminal leakage are all zero.  Exhaustive basis-control equality
therefore extends linearly, including entanglement with unexamined spectators.

The inverse reverses both fixed endpoint gate lists and conjugates every
two-state core.  The persistent flags remain part of the code word.  When a
blank external interface is required, the two flag-preparation CNOTs are
uncomputed only after the controlled inverse.  The runner tests both CNOT
boundaries explicitly with zero failures.  Maximum inverse residual is
`2.13e-15`; maximum norm residual is `1.45e-15`; equality work is returned
clean by the imported literal compiler.

## Exact tests

The Cycle-554 runner tests the following independently:

1. Exact SHA pins for Cycles 526, 549, and 484.
2. All fourteen Cycle-484 train/held coefficient rows in each of Q0, Q1, Q2,
   for 42 row-sector cases.  The Q1 action agrees exactly with
   `Cycle480.product_action(..., route="suzuki4", discrete=True)`; residual 0.
3. All three lawful current words on all six lawful endpoint Q pairs; 18
   representative product-spanning tensor cases.  Maximum independent
   manifest/coarse intertwiner residual is `1.30e-15`; a coherent current
   direct-sum probe gives `1.96e-16`.  `G_physical` receives no Q argument.
4. One literal word register coherently spanning Q0/Q1/Q2; residual
   `1.0700337582051244e-15`, with zero wrong-sector and off-code leakage.
5. Explicit uniqueness of 1856 physical 13-M2 code words and literal endpoint
   words for all 576 directional signed pairs.
6. For all 18 Q/direction generators: Hermiticity, zero diagonal, real signed
   entries, disjoint cover, and exact pair reconstruction; zero failures.
7. The immutable manifest has exactly 115200 installed slots and digest
   `3c5d78871ac434ffc1ee3295be63a1e65883d2eba84209e40bc3f12c3dbcd3e3`.
8. All 24 carried proper-cubic schedules independently in Q0, Q1, and Q2;
   maximum covariance residual 0.
9. All 576 proper-cubic frame products in the coefficient-lane and Q-sector
   representations; zero failures.
10. Seam-orientation reversal, including `J+`/`J-`, flags, tensor axes, and
   coefficient-bank swap; residual `5.63e-17`.
11. Word-space manifest deletions, all with zero terminal wrong-Q/off-code
    leakage:
    - selected persistent flag: signal `3.0123026437110273e-1`;
    - one active coefficient bit: signal `4.750210624199579e-4`;
    - first Suzuki factor: signal `3.564512684427616e-2`.
12. Four unlawful current words are rejected; flag preparation and inverse
    uncompute have zero boundary failures.
13. All Q0/Q1/Q2 directional generators commute exactly with local matter
    number.

L5 and held L6 do not select different response circuits.  They enter through
the exact-pinned Cycle-526 current interface, and the identical local
Cycle-554 manifest is appended at either size.  This runner does not repeat
Cycle 526's expensive full-Fock L5/L6 proof; it pins that runner rather than
silently weakening or refitting its result.

## Preservation boundary

The following retained fixtures are neither edited nor refitted:

- Cycle-219 one-particle mass: `0.45340565417488515`;
- Cycle-230 complete contact: 4047 nontrivial columns;
- Cycle-230 seam/free-plus-contact physical update and inverse;
- Cycle-526 L5 and held-L6 augmented intertwiner;
- Cycle-484 Q1 response action.

These are spectator/exact-pinned predecessor facts only.  Cycle 554 does not
apply the appended current-selected controller to the full mass eigenray or to
the Cycle-230 contact/seam observables, so it makes no preservation claim for
those composed outputs.  Q0 is identity.  Q1 exactly matches Cycle 484's local
response.  Q2 is a new literal extension of the same supplied directional
factor law; it preserves matter number and its declared Q code, but does not
derive correlated physical preparation beyond the tested sectors.

## Resource inventory

The maximum live local controller interface is conservatively counted as:

| item | M2 |
|---|---:|
| two literal 13-M2 endpoint source blocks | 26 |
| `EDGE_PASSED`, `J+`, `J-` | 3 |
| persistent left/right flags | 2 |
| two six-by-ten-bit coefficient banks | 120 |
| shared clean equality-conjunction work | 13 |
| **maximum live controller interface** | **164** |

There are 115200 installed coefficient-bit controlled pair-rotation slots for
both endpoint blocks across the complete declared Q<=2 code.  Q0 contributes
no nonidentity pair.  This is a fixed finite count, not a runtime allocation.
The literal gate-list digest is emitted by the runner.

The exact pre-routing logical counts are derived row by row from all 115200
actual word pairs, not scaled from Q1.  Every row has Hamming distance four.
The Cycle-549 least-significant-bit-first path gives six 12-control Gray X
calls, while the adjacent Cycle-484 B20 core has twelve equality controls plus
coefficient and flag.  Exact counts are `17,510,400` Toffoli, `230,400` CNOT,
`12,825,600` negative-control NOT, `230,400` H, `1,290,737,664` repeated `Z20`
or inverse, and `691,200` Gray equality MCX.  As a cross-check, the 9600-row
left-Q1 subset reproduces every Cycle-484 flagged count exactly, including its
`1,180,800` NOT calls.  There are also two flag-preparation CNOTs and two
terminal inverse-boundary flag-uncompute CNOTs.

These exact logical counts are separate from routing bounds.  Expanding each
Toffoli through the supplied 15-call decomposition gives a conservative
`1,566,680,064` bare one-/two-M2 calls before routing.  Cycle 549's maximum
route length is 24 adjacent edges.  Treating every bare call as worst case
gives an additional routing bound of at most `216,201,848,832` CNOT calls for
gather/un-gather.  That is deliberately an upper bound, not an exact routed
count and not time.

For a deliberately conservative non-overlap bound, retain the entire 106-M2
Cycle-526 seam envelope, two complete 49866-M2 Cycle-484 full-layer cell
envelopes, and two Cycle-549 invariant `13^3 = 2197` route grids: 104232 M2.
This overcounts reusable delivery/work/route structure but is a safe constant
bound per selected seam.  No lower or minimum-content claim is made.

## Supplied structure and open walls

Supplied rather than derived here:

- the Cycle-526 selected seam, encoder, current-correlated preparation, edge
  orientation, current rail convention, contact/free law, and K carrier;
- the choice that a receiving signed-current event activates the response;
- the Cycle-484 coefficient law, P8 floor arithmetic, six ten-bit word width,
  Suzuki4 selection/order, B20 basis, angle `theta=0.8m`, and response delivery;
- Cycle 549's 13-M2 code, equality controls, arbitrary one-/two-M2 cores,
  Toffoli decomposition, routing geometry, and off-code completion;
- blank persistent flags, clean work M2s, coefficient preparation, and tested
  current/source correlations.

Still open:

- physical source normalization and the reason this candidate coupling has
  the supplied coefficient law;
- correlated preparation beyond the tested sectors;
- a local energy-stress object and conservation/response identity;
- a gravity field equation, inverse-square or relativistic limit, equivalence
  principle, and feedback of response onto source;
- physical energy, clock calibration, proper time, and realized-history close;
- Born/probability derivation.

Depth is not time.  Wrapped or dyadic phase is not energy.  A generator
element is not a rate.  Response is not force or gravity.  Pointer copying is
not a Record.  A schedule carrier is not proper time.

## Fresh no-go discipline: N1–N8

The fresh `no-go-discipline` skill and proof-search governance were read before
making any negative or minimum-content assessment.

### N1 — alternative route enumeration

| route | marker | terminal obligation | exact retained result |
|---|---|---|---|
| R1: signed rails -> two flags -> dual installed blocks | ATTEMPTED | fixed manifest equals signed coarse direct sum | Cycle-554 runner: 115200-slot manifest; all lawful comparisons pass |
| R2: `EDGE_PASSED`-only symmetric activation | ATTEMPTED | recover receiver/sign discrimination from `EDGE_PASSED` | `physical_selected_seam_event_current_adapter_cycle526_2026_07_21.py`: `PLUS` and `MINUS` both have `EDGE_PASSED=1` |
| R3: recompute flags from endpoint occupation | ATTEMPTED | stable joint-code occupation decoder | Cycle-526 runner: naive single-cell decoder has 18528 failures; persistent pre-reduction shadows remain a repair |
| R4: persistent one-hot receiver token | OPEN | compile token prepare/unprepare and compare resources/covariance | no retained result rules it out |
| R5: opposite signed responses at both endpoints | OPEN | state candidate law; test conservation and held predictions | Cycle-526 runner retains `J+`/`J-`; route not tested here |
| R6: time-multiplex one response block | OPEN | reversible local schedule carrier and all24/576 audit | Cycle-484 runner supplies a fixed schedule; multiplex route not tested |

### N2 — full pairwise wall-independence audit

The collapsed load-bearing open set for this Cycle-554 claim is:

- W1: select/derive the structural coupling law among receiver-only,
  dual-endpoint, and token routes;
- W2: derive the coefficient, angle, and physical source-normalization law;
- W3: autonomously prepare correlated current/source/coefficient inputs;
- W4: derive a local energy-stress observable and conservation identity;
- W5: derive a response-feedback/long-distance kernel conditional on an
  arbitrary supplied source, without identifying it as gravity.

Clock/proper-time and Born questions are broader TOE lanes, but are not
load-bearing for this local controller theorem and therefore are not inflated
into this wall count.

| pair | closing first automatically closes second? | closing second automatically closes first? | independent? |
|---|---|---|---|
| W1/W2 | no | no | yes |
| W1/W3 | no | no | yes |
| W1/W4 | no | no | yes |
| W1/W5 | no | no | yes |
| W2/W3 | no | no | yes |
| W2/W4 | no | no | yes |
| W2/W5 | no | no | yes |
| W3/W4 | no | no | yes |
| W3/W5 | no | no | yes |
| W4/W5 | no | no | yes |

The definitions deliberately separate structural choice, quantitative
normalization, state preparation, conserved observable, and an uninterpreted
conditional response kernel.  In particular, W5 can close against a supplied
test source without producing W4, and W4 can close without selecting field
dynamics.  A physical gravity identification is the downstream conjunction
W4+W5, not a sixth independent wall.  No pairwise closure above implies the
other wall; no further collapse is licensed.

### N3 — hidden-wall scan

The response coefficient law, angle, Suzuki order, and B20 basis are promoted
to W2; supplied current/source correlations are W3; candidate
current-to-response selection is W1.  Blank controls and off-code completion
are explicit compiler inputs.  Clock and Born mentions are non-load-bearing
broader context for this theorem.

### N4 — residual matching

Cycle 526's signed-current residual matches the flag-control interface.  Cycle
549's literal Q<=2 factor residual matches the physical directional compiler.
Cycle 484's flagged Q1 response matches the Q1 equality test.  Cycle-219/230
mass/contact/seam residuals do **not** match appended-controller observable
preservation, so they are retained only as spectator predecessor pins and are
dropped as witnesses for any stronger preservation claim.

### N5 — rhetoric audit

`J+ - J-` is signed number flow only.  The persistent M2 is a source-control
flag only.  At the tested local resolution, Cycle 554 supplies no tested
identification of response as force/gravity, phase as energy, a generator
element as a rate, or schedule as time.  Per-mode, per-block, and lattice-wide
negative claims were not tested and are not made.  No “necessary”, “minimum”,
“cannot”, or constitutional language is licensed.

### N6 — partial-closure path scan

The controller manifest closes.  W1-W5 remain import-retirement targets, not
proposed axioms.  Existing Cycle-484 and Cycle-549 compiler imports show a
constructive bound-theorem/retire-import path; no convention or reframing found
here closes a quantitative physics wall.

### N7 — steelman

A hostile reviewer can choose R5 because the retained rails already carry the
sign needed for a two-end response, or R6 because a reversible local token may
trade controller width for schedule depth.  Neither route was tested, and R4
is also constructively open.  Therefore Cycle 554 cannot support a
route-independent obstruction or select its candidate coupling as a law.

### N8 — cross-cycle echo and claim gate

Cycles 484 and 549 retired earlier primitive/compiler walls constructively;
that same import-retirement pattern may apply to W1-W5.  Cycles 526 and 549
are exact-pinned here, and Cycle 484's Q1 action is reproduced rather than
renamed.  Earlier failures to derive energy, stress, proper time, or gravity do
not become evidence against the open alternatives.

Broad negative gate: FAIL / DO NOT SHIP.  No impossibility, minimum-content,
or axiom-pressure claim ships from Cycle 554.

## TOE dependency disposition

This raises the local source/controller bridge, not gravity itself.  A compact
wall ledger is:

| wall | disposition after Cycle 554 |
|---|---|
| `C_ref` | unchanged; frame covariance closes for this controller |
| `C_num` | improved locally; signed number current now controls response |
| `C_wrap` | unchanged; B20 phase remains supplied and is not energy |
| `C_int` | improved for the tested bounded composition; coupling law supplied |
| `C_local` | improved; fixed 2-M2-resolved local controller through Q2 |
| `C_source` | improved from source/current to response control; stress/gravity source open |

The optimal next campaign is not another compiler pass.  It is an adversarial
tournament among locally conserved candidate current-to-response laws,
including R1 and R5, asking whether any yields an independently normalized
energy-stress/source identity and a quantitative long-distance response
without importing the answer.  Until then this cycle remains a bounded
controller theorem with authority none and audit unset.

## Artifacts

- `scripts/physical_current_selected_persistent_response_bridge_cycle554_2026_07_21.py`
- this note
