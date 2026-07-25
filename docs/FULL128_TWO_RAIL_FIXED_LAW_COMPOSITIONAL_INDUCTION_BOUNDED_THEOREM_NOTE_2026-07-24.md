# Full128 two-rail fixed-law compositional induction

**Date:** 2026-07-24

**Type:** bounded_theorem

**Authority:** none

**Audit:** unset

**Framework substrate:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

**Bounded circuit input:**
[`FULL128_LOCAL_M64_SEAM_M2_BARE_FRAME_INTERTWINER_BOUNDED_THEOREM_NOTE_2026-07-24.md`](FULL128_LOCAL_M64_SEAM_M2_BARE_FRAME_INTERTWINER_BOUNDED_THEOREM_NOTE_2026-07-24.md)

**Fixed-law core:**
[`scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py`](../scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py)

**Primary runner:**
[`scripts/frontier_full128_two_rail_fixed_law_cycle656_probe_2026_07_24.py`](../scripts/frontier_full128_two_rail_fixed_law_cycle656_probe_2026_07_24.py)

**Receipt:**
[`outputs/frontier_full128_two_rail_fixed_law_compositional_induction_receipt_2026_07_24.json`](../outputs/frontier_full128_two_rail_fixed_law_compositional_induction_receipt_2026_07_24.json)

**Runner cache:**
[`logs/runner-cache/frontier_full128_two_rail_fixed_law_cycle656_probe_2026_07_24.txt`](../logs/runner-cache/frontier_full128_two_rail_fixed_law_cycle656_probe_2026_07_24.txt)

## Controlled claim

On the exact supplied finite genesis specified below, there is an explicit
time-homogeneous bounded circuit law

```text
A_auto = R Q,
```

where chronological execution is selector `Q` first and packet shift `R`
second. The executable follows all 3,908 applications and obtains

```text
A_auto^3908 E_combined = E_combined G_coarse.
```

This is a compositional induction certificate. The runner does not form or
execute the exponentially large matrix on all physical `M2` factors. Instead,
it exhausts the fixed-law packet/selector trace, verifies every local selector
and routing factor, binds the selected factor sequence to the exact Cycle-655
word, and composes that sequence with the Cycle-655 full128 decoded
intertwiner. The maximum inherited full128 residual is
`8.40686768501364e-15`.

The theorem domain is exactly one live token at station zero, one Cycle-655
`E_full` packet at the same station, the fixed program record at every station,
vacuum on all B packets and inactive A packets, and zero selector flag, match
scratch, and bypass work at every station. This domain is supplied. It is not
dynamically prepared or enforced.

## Repo-native input

The bounded input is the final repo-native Cycle-655 package. Its combined
word has 3,907 nearest-neighbor factors on 115 touched `M2` wires and SHA-256

```text
a2e461d4984e4901fa0e8902c289ed2543da7545370891b96f2b50c6ba7f0fbf.
```

One explicit identity instruction pads that word to 3,908 factors. The padded
factor-sequence SHA-256 is

```text
f8f1ca483eafdfc99020c06c6c661e6cb0f6a2a852f2f6f58c3547820d0c5be5.
```

The Cycle-656 modules use ordinary repo-local imports. They contain no
`/private/tmp` or campaign fallback, no network call, and no archived-object
read. Every source in the literal `AUDIT_INPUT_PATHS` closure is below 40,000
bytes.

## Exact definitions

### Packet and station layout

The sorted Cycle-655 touched support supplies 115 packet-data lanes. Lane 115
is the transported live-token bit, giving 116 transported packet lanes.

There are 3,908 A stations and 3,908 B stations alternating around a square
perimeter of side 1,955. Each A station has:

- the 116 packet factors;
- 33 stationary program bits;
- one selector flag;
- 32 match scratch bits; and
- two bypass-work bits.

Thus an A column contains 184 `M2` factors and a B column contains 116. The
complete isolated fixed-law footprint is

```text
3908 * (184 + 116) = 1,172,400 M2.
```

### Fixed program

Every station holds one 33-bit record with fields

```text
valid, address, matrix opcode, arity, first lane, second lane.
```

The address is the padded factor index. There are 3,908 distinct lawful
records and 26 exact matrix opcode classes: nine one-`M2` classes and 17
two-`M2` classes. Semantic gate names may alias only when their action matrices
are exactly equal; the maximum within-opcode matrix difference is zero.

The record array is stationary supplied program memory. It is not transported
with the packet and is not derived from the framework axioms.

### Selector `Q`

`Q` is an explicit lazy blueprint containing all 3,908 ROM blocks, replicated
at every A station. Each block:

1. applies negative controls for its zero pattern bits;
2. computes the 34-input AND of the live token and 33 program bits using 33
   exact Toffoli factors;
3. applies its hard-wired factor when the selector flag is one;
4. uncomputes the match chain; and
5. restores every negative control.

One-`M2` actions use an exact two-`M2` controlled lift. Two-`M2` actions use
two clean bypass-work factors: controlled Fredkins move the data into work,
the exact opcode acts on work, and inverse Fredkins return the data. Every
two-`M2` opcode fixes the blank work state exactly.

All logical one- and two-`M2` selector factors are replaced by explicit
route-and-return circuits along the 184-factor A column. The longest distance
is 183. The route certificate checks every distance `1,...,183`, 33,489
instantiated nearest-neighbor edges, and exact endpoint/return order.

### Shift `R`

`R` is two explicit SWAP layers:

```text
R1: A[s,lane] <-> B[s,lane]
R2: B[s,lane] <-> A[s+1 mod 3908,lane].
```

Each layer contains 453,328 nearest-neighbor SWAPs. Within each layer there
are zero repeated edges, zero shared vertices, and zero non-nearest-neighbor
edges. Executing `R1` and then `R2` co-shifts all 115 data lanes and the live
token by one station and returns every B packet to vacuum on the declared
genesis.

### Law `A_auto = R Q`

Circuit products act on column vectors from right to left. Therefore
`A_auto = R Q` means:

1. execute the full stationwise selector `Q`; then
2. execute rail layers `R1` and `R2`.

This order is part of the law. Reversing it is a hostile control, not an
equivalent convention.

### Encoding `E_combined`

`E_combined` appends the finite controller genesis to the Cycle-655 encoding:

```text
E_combined |psi>
  = E_full |psi> in A[0] packet data
    tensor |1> in A[0] live token
    tensor |0> in every other live-token factor
    tensor the fixed 3908-record program
    tensor |0> on every B packet
    tensor |0> on every flag, scratch, and bypass-work factor.
```

Every inactive A packet is also vacuum. The Cycle-655 `E_full` portion retains
its supplied cycle auxiliaries, repetition blanks, pair-register blanks,
corridor blanks, labels, couplings, and factor order.

## Exhaustive compositional induction

The primary trace executes the actual `AutoLaw.apply` path 3,908 times. Each
step calls the exact clean-ancilla `q_apply` semantics and then the two literal
SWAP loops implementing `R`.

The induction invariant before step `s` is:

```text
the unique live E_full packet is at A[s];
its selected-factor history is (0,1,...,s-1);
all B packets are vacuum;
all programs equal the fixed program array; and
all selector ancillas equal their zero genesis.
```

At station `s`, record uniqueness makes ROM block `s` the only live block.
`Q` appends factor `s` and restores the station work. `R` moves the entire
packet to station `s+1 mod 3908` and returns B to vacuum. This establishes the
next invariant.

After 3,908 steps, the packet returns to A station zero with history
`(0,1,...,3907)`. The observed sequence digest equals the padded-word digest.
The final identity pad has zero action, so the selected physical word is the
Cycle-655 3,907-factor word. Composing with its bounded full128 intertwiner
gives the controlled claim.

The executable trace reports:

- trace SHA-256
  `d2d9cd8e422397b0f063b158f25e6f61107450be02386d106d75d61df0b382cd`;
- 3,908 selected events;
- 15,268,556 token-zero station visits;
- first event `(station=0, factor=0, origin=0)`;
- last event `(station=3907, factor=3907, origin=0)`; and
- zero token-count, B-vacuum, program-change, ancilla-change, return, or
  factor-order failures.

## Local selector exhaustion

The ROM certificate explicitly compares all

```text
3908 * 3908 = 15,272,464
```

lawful record/block pairs. Exactly 3,908 pairs match, one for each record. It
also executes the logical match network for every exact match, every token-zero
exact record, and every one-bit record mismatch. The 128,964 mismatch cases
have zero fires. All clean flag and scratch factors reset.

The maximum local residuals are:

| check | maximum residual |
|---|---:|
| opcode unitarity | `9.42129743476075e-16` |
| Toffoli decomposition | `7.346882794269506e-16` |
| Fredkin decomposition | `7.346882794269506e-16` |
| controlled one-`M2` action | `0` |
| controlled one-`M2` unitarity | `4.440892098500626e-16` |
| two-`M2` bypass action | `0` |
| two-`M2` work leakage | `0` |
| two-`M2` blank-fixed action | `0` |

## Hostile controls and exact domain

The controls are part of the positive domain certificate. They do not assert
an impossibility outside that domain.

| control | executable result |
|---|---|
| `R` before `Q` | selects cyclic history `(1,2,...,3907,0)`, not the lawful word |
| token initially at station 1 | returns to station 1 with the same cyclic history |
| dirty last match-scratch bit, token zero | selector falsely fires and returns the scratch to its dirty input |
| dirty bypass work, token zero | a reverse-FSWAP witness changes the work branch by norm `2` |
| zero tokens, clean ancillas | no factors selected; a marked payload cycles and returns unchanged |
| tokens at stations 0 and 1 | 7,816 factors selected; the packets acquire inequivalent cyclic histories |
| delete ROM block 17 | exactly factor 17 is omitted |
| flip station-17 opcode | the record matches no ROM block and omits nonidentity `outer_decode`, with `||U-I||=2` |

These controls show why station zero, exactly one token, the fixed program, and
clean scratch/flag/bypass work are load-bearing supplied conditions. No local
constraint or preparation theorem is inferred from rejecting the hostile
inputs.

## Resource law

The resource census distinguishes the physical circuit law for one application
from the number of factors executed by its 3,908th power.

| resource | exact count |
|---|---:|
| transported packet `M2` | `116` |
| A-column `M2` | `184` |
| B-column `M2` | `116` |
| complete isolated footprint `M2` | `1,172,400` |
| ROM blocks per station | `3,908` |
| logical `Q` factors per station | `4,216,662` |
| routed `Q` NN factors per station | `86,464,312` |
| `Q` NN instances across all stations | `337,902,531,296` |
| `R` NN SWAP instances per `A_auto` | `906,656` |
| NN instances in one fixed `A_auto` circuit | `337,903,437,952` |
| NN factor executions in `A_auto^3908` | `1,320,526,635,516,416` |

The last row is an execution count, not a larger physical footprint. No
optimality or minimum-resource claim is made.

## The seven executed checks

| # | Executed check | Exact result |
|---:|---|---|
| 1 | repo-native dependency and size closure | all declared inputs present; no external input; every source below 40,000 bytes |
| 2 | exact selector `Q` | 15,272,464 ROM pairs; exact unique matches; zero clean reset/action failures |
| 3 | rail `R` and selector routing | two disjoint NN layers; zero collision, NN, endpoint, or return failures |
| 4 | full `A_auto=R Q` orbit | 3,908 steps; factors `0,...,3907`; packet returns to station zero |
| 5 | Cycle-655 composition | padded identity residual zero; inherited full128 residual `8.40686768501364e-15` |
| 6 | hostile controls | every order, offset, dirty-ancilla, token-domain, ROM, and program control active |
| 7 | resources | physical-law and power-execution counts separately close |

## Supplied structure

This bounded theorem supplies, rather than derives:

- the complete Cycle-655 finite encoder, pair-register preparation, contact,
  seam, decoding, routing, and re-encoding word;
- the six signed mode labels, seam-port label, decoded wire order, `beta=-0.3`,
  contact coupling `g=0.37`, seam attachment, and factor order;
- the exact 26-entry matrix table, nine controlled one-`M2` lifts, Toffoli and
  Fredkin decompositions, and route-and-return convention;
- the 3,908 station addresses, all fixed 33-bit program records, station
  orientation, and square rail embedding;
- chronological selector-before-shift order `A_auto=R Q`;
- the station-zero token and `E_full` packet placement;
- vacuum on all B packets and all inactive A packets;
- zero genesis for every selector flag, match-scratch factor, and bypass-work
  factor;
- the Cycle-655 cycle-auxiliary, repetition, register, corridor, and returned-
  work genesis;
- the enormous finite replicated `Q` circuit, both `R` layers, and their exact
  layer order; and
- the standard translations/proper-cubic coordinate action and supplied
  rotated cassette family.

Derived on that supplied surface are the exact one-step law, the exhaustive
factor-order induction, packet/work return, composition with the Cycle-655
full128 intertwiner, hostile domain controls, and resource census above.

## Claim boundary

This note does not establish translation invariance of the fixed cassette, a
translation-invariant recurrent law, a two-cell or full-neighborhood compiler,
overlapping/shared-port consistency, or a complete lattice stream law. The
proper-cubic statement remains the Cycle-655 supplied rotated family, not one
canonical off-code cassette invariant under every frame.

It does not derive, prepare, cool, select, or dynamically enforce the one-token,
fixed-program, code, blank, scratch, flag, or bypass genesis. It does not derive
the mode labels, couplings, program, orientation, factor order, or matrix table
from the framework axioms.

The circuit substeps and the moving token are not physical time, a clock rate,
energy, source, stress, gravity, framework Record, occurrence, realized
history, measurement, or Born/probability data. No full global physical matrix
is claimed to have been formed or executed.

No optimality, minimum-content, impossibility, shared-obstruction, no-go, or
axiom-pressure claim is made. This is a positive bounded fixed-law
compositional induction on the exact declared genesis.

## Reproducibility and audit boundary

Run:

```bash
python3 scripts/frontier_full128_two_rail_fixed_law_cycle656_probe_2026_07_24.py
```

The expected terminal is:

```text
FULL128_TWO_RAIL_FIXED_LAW_CYCLE656_CERTIFICATE
```

The runner declares the complete mutable source closure in a literal
`AUDIT_INPUT_PATHS` tuple. The receipt records source, note, and cache hashes
together with the exact trace, residual, hostile-control, resource, and claim-
boundary inventory.

Authority remains `none`; audit remains `unset`. Only the independent audit
lane may set an audit verdict or effective status.
