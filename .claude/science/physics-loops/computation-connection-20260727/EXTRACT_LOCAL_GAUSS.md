# Cycle-703 local-Gauss reference and Cycle-719 token-row surface

## Source boundary

This is a bounded extraction from exactly: (1) `docs/work_history/repo/review_feedback/CYCLE703_LOCAL_GAUSS_REFERENCE_ADVERSARIAL_NOTE_2026-07-25.md`; (2) `scripts/frontier_cycle703_local_gauss_reference_adversary_2026_07_25.py`; and (3) `scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py`, inspected only at the controller-token/rail map level.

No runner was executed. “Verified,” “tested,” and “exact” report source claims and encoded checks, not a fresh execution.

## 1. Cycle-703 result and exact claim ceiling

### Reviewed object and positive bounded local constraint capacity

The reviewed object is one reference fermion `r_x` for each coarse cell, with six matter modes `m_{x,a}` and the local constraint

```text
D_x = B(r_x) product_a B(m_{x,a}) = +1
```

inside fixed-even BKSF (note lines 5-7; runner lines 4-15). The status is exactly “local constraint capacity and bounded even-operator construction positive; physical BKSF common-E state encoder and preparation open” (note lines 12-13).

For `N` connected cells, the note states

```text
product_x D_x = product_(all 7N modes) B = +1
```

(note lines 17-22). This is already the fixed-even BKSF identity. Consequently:

- the `N` displayed `D_x` constraints have rank `N-1`, for odd and even `N`;
- the starting fixed-even seven-mode representation has `7N-1` qubits and imposing `D` leaves exactly `6N` logical qubits;
- every six-mode matter occupation string has the unique reference assignment

  ```text
  n(r_x) = sum_a n(m_x,a) mod 2.
  ```

- both total matter-parity sectors occur at every volume, without querying a global matter-parity bit (note lines 24-35).

Thus “positive capacity” means an exact dimension/rank and basis-bijection result for the local-`D` constrained, fixed-even construction. It does not mean that every displayed `D_x` is independently rank-active: one row is globally redundant. All commuting local penalties may still be enforced, but the product relation must be declared (note lines 101-118).

### Exact even-operator algebra content

For an oriented nearest-neighbor matter edge `u=(x,a)` to `v=(y,b)`, the note
defines the target-cell spectator parity

```text
P_(y,not b) = product_(c != b) B(m_y,c).
```

With each reference ordered after the six matter modes in its local Fock block,
the exact number-preserving hop on the local-`D` code is

```text
H_uv = - P_(y,not b) (1 - B_u B_v) A_uv A_rr / 2.
```

The corresponding fermionic swap is

```text
FSWAP_uv = (B_u + B_v)/2 + H_uv.
```

(note lines 37-56; runner lines 216-241).

The reported exact scope is:

- all `4,096` columns of the `12 -> 14` two-cell extended-Fock occupation map,
  for all 36 directed port pairs;
- hop and FSWAP agreement with an independently constructed fermionic target;
- FSWAP on all `2^14` extended two-cell basis states for every port pair,
  including Hermitian-involution behavior and preservation of both endpoint
  `D` parities off code;
- BKSF edge-qubit `A/B` operator identities, constraint commutators, and
  stabilizer ranks;
- tested hop/FSWAP, intracell coin edges, and diagonal contacts as a bounded
  representation of the parity-even update algebra;
- directed operator-family covariance through 24 proper-cubic frames and all
  576 ordered frame products after the explicit local CZ/Z order gauge
  (note lines 58-65, 78-90, 120-147, 179-204).

The deletion/ablation content is also part of the result: deleting `A_rr` violates exactly the two endpoint `D` constraints; omitting the five-spectator parity produces active sign failures; omitting `(1-B_uB_v)` admits pair-creation/deletion branches (note lines 61-65).

This is an exact **even-update operator-algebra** result at the tested layers. No claim is made for bounded isolated odd creation/annihilation fields or the full graded CAR: remote odd fermion fields anticommute whereas disjoint bosonic supports commute (note lines 86-90).

### What remains open

The executed common `E` is only the sparse occupation-basis map from 12 matter modes to 14 extended fermion modes. It is **not** a BKSF edge-qubit common-`E` intertwiner (note lines 67-76, 136-147).

On a periodic three-torus, local BKSF loop stabilization plus `D` leaves three Wilson spectators. Fixing all three gives dimension `2^(6N)`. Stabilizer-rank equality proves that a finite-dimensional state isometry exists in each fixed Wilson character, but does not construct:

- explicit physical `E_BKSF` columns and phases;
- a bounded-radius/locality-preserving BKSF encoder from matter inputs and
  blank physical M2s;
- finite-depth preparation of the loop code or fixed Wilson/spin character;
- a physical residual `|| U_BKSF E_BKSF - E_BKSF U_matter ||`;
- leakage or orthogonal-complement residuals for the physical word;
- transformed-`E` covariance under frames/translations;
- bounded odd-field representatives (note lines 67-76, 136-165, 194-215).

The dynamics preserves whichever Wilson character is supplied; it does not select one. A fixed `+++` Wilson vacuum may be admitted as an explicit resource, but any stronger genesis claim needs a local preparation mechanism or a theorem that the resource is physically present (note lines 149-165).

The note's finite-isometry/local-encoder distinction is:

- finite linear isometry after supplying a fixed Wilson character: **yes**, for odd and even `N`, without a runtime parity query;
- bounded-radius locality-preserving physical BKSF encoder from product ancillas: **open**;
- bounded parity-even update representation: **yes** for the tested families;
- local full graded CAR: **not claimed** (note lines 78-90).

### N-gate and escape lines

The short gate lines are, verbatim:

> No route-independent no-go or axiom pressure is supported.

(note line 92)

> **Gate result: FAIL for a route-independent no-go.  Ship the layered positive
> and open boundary only.**

(note lines 219-220)

The explicit partial-closure escape is, verbatim:

> **N6 — Partial closure.** Build a stabilizer Clifford isometry for one finite
> periodic size and fixed Wilson character, orient its columns against the
> independent matter basis, and execute one dressed stream word on that common
> E.  Then compare held odd/even sizes and transformed encodings.  This is a
> concrete completion path requiring no axiom edit.

(note lines 245-249)

The runner's successful terminal token is exactly `LOCAL_GAUSS_ALGEBRA_AND_FOCK_ISOMETRY_POSITIVE_BKSF_COMMON_E_OPEN` (note lines 268-269; runner line 752).

## 2. Cycle-703 runner constructions

### Constraint rows, locality, and capacity accounting

- `local_d` is the product of the seven vertex-`B` words for modes `0..6` in
  one cell (runner lines 64-67). `local_d_rows` emits one such row per graph
  cell (lines 70-71).
- `local_loop_rows` maps every cycle returned by `base.local_cycles(graph)` to
  `graph.loop_pauli(vertices)` (lines 74-78).
- `wilson_rows` is empty for open graphs. On periodic graphs it emits three
  reference-mode (`mode == 6`) loops, one per axis, along the coordinate line
  whose other coordinates are zero (lines 81-92). These Wilson rows are
  noncontractible/global, not bounded local checks.
- The rank audit uses open `L=2` and periodic `L=3,4,5`, with `N=L^3`; it
  computes GF(2) symplectic stabilizer ranks for loops, loops+`D`, and
  loops+`D`+Wilsons (lines 95-145).
- The expected counts are `D_increment=N-1`, Wilson increment `0` open or `3`
  periodic, exponent `6N+3` before periodic Wilson fixing, and `6N` after
  fixing. Deleting any one `D` preserves the `N-1` increment; deleting two
  lowers it to `N-2` (lines 147-190).
- The runner measures `D` Pauli **weight**, not a metric radius: the note
  reports weight 6 on tested open-boundary cells and weight 12 in periodic
  bulk, independent of volume (note lines 101-105). No numerical locality
  radius for `D` or loop rows is computed in the runner.
- Stream edges are positive-axis nearest-neighbor bonds: source matter mode
  `2*axis+1`, target matter mode `2*axis`, and reference mode 6 at both cells
  (runner lines 193-201). The hop also uses the five non-target matter `B`
  factors in the target cell (lines 204-241).
- Hop Pauli weight is measured over periodic `L=3` and reported as a maximum
  in the result object, but no literal numerical maximum is asserted in source
  without running it. The runner marks support bounded independently of volume
  because cell size and graph degree are fixed (lines 244-345; note lines
  131-134).

### Verification style

- Rank/capacity: exact GF(2) symplectic ranks, phase-consistency checks,
  constraint/loop/Wilson commutators, product-row identity, held odd/even
  volumes, and one-/two-row deletion checks (runner lines 99-190).
- Operator algebra: exact Pauli equality/commutation, Hermiticity parity,
  support-weight census, endpoint ablation, all positive-axis bonds on
  periodic `L=3`, and all allowed intracell matter pairs (lines 244-345).
- Common `E`: exhaustive enumeration of `2^12=4,096` logical columns for each
  of 36 directed port pairs, plus all `2^14` raw extended states for every
  FSWAP pair; active ablations test spectator parity, number projector, and
  reference edge (lines 467-577).
- Covariance: exact transport of `D` and both hop terms through 24 frames,
  raw-order mismatch detection, local-gauge correction, and all 576 frame
  products (lines 580-682).
- Scope: textual guardrails require the note to retain algebra/state/
  preparation/no-go distinctions; summary booleans keep missing physical
  layers false (lines 685-724).

### Every runner-defined function and exact signature

The runner defines the following functions; line numbers are definition starts.

| Line | Exact signature | Role |
| ---: | --- | --- |
| 47 | `check(label: str, condition: bool, detail: object = "") -> None` | PASS/FAIL accumulator and reporter |
| 57 | `pauli_product(rows) -> base.Pauli` | ordered Pauli-row product |
| 64 | `local_d(graph: base.ReferenceGraph, cell: tuple[int, int, int]) -> base.Pauli` | one seven-mode cell constraint |
| 70 | `local_d_rows(graph: base.ReferenceGraph) -> list[base.Pauli]` | all cell-`D` rows |
| 74 | `local_loop_rows(graph: base.ReferenceGraph) -> list[base.Pauli]` | bounded local loop rows |
| 81 | `wilson_rows(graph: base.ReferenceGraph) -> list[base.Pauli]` | three periodic reference Wilsons, or none open |
| 95 | `stabilizer_rank(rows, qubits: int) -> int` | GF(2) symplectic rank |
| 99 | `rank_and_sector_controls() -> dict[str, object]` | capacity, redundancy, phase, and parity audit |
| 193 | `stream_vertices(graph: base.ReferenceGraph, cell, axis: int)` | oriented matter/reference stream endpoints |
| 204 | `spectator_parity(graph: base.ReferenceGraph, cell: tuple[int, int, int], excluded_mode: int) -> base.Pauli` | five-mode target-cell parity |
| 216 | `hop_pauli_terms(graph: base.ReferenceGraph, matter_u: int, matter_v: int, reference_u: int, reference_v: int, target_cell: tuple[int, int, int], target_mode: int) -> tuple[base.Pauli, base.Pauli]` | two Pauli words of dressed hop, without common `1/2` |
| 244 | `operator_algebra_controls() -> dict[str, object]` | commutator, support, Hermiticity, and deletion audit |
| 348 | `parity_before(bits: tuple[int, ...], mode: int) -> int` | Fock-order prefix parity |
| 352 | `apply_gamma(bits: tuple[int, ...], mode: int) -> tuple[tuple[int, ...], complex]` | occupation-basis Majorana action |
| 361 | `apply_a(bits: tuple[int, ...], source: int, target: int) -> tuple[tuple[int, ...], complex]` | oriented `A` action |
| 372 | `apply_c(bits: tuple[int, ...], mode: int, creation: bool) -> tuple[tuple[int, ...] \| None, complex]` | creation/annihilation action |
| 383 | `logical_hop_action(bits: tuple[int, ...], left: int, right: int) -> tuple[tuple[int, ...] \| None, complex]` | independent logical hop target |
| 401 | `extended_codeword(logical: tuple[int, ...]) -> tuple[int, ...]` | append each cell's local parity reference |
| 407 | `remove_references(extended: tuple[int, ...]) -> tuple[int, ...]` | delete reference positions 6 and 13 |
| 411 | `apply_core(extended: tuple[int, ...], left_mode: int, right_mode: int) -> tuple[tuple[int, ...], complex]` | reference-edge then matter-edge action |
| 419 | `corrected_hop_action(extended: tuple[int, ...], left_mode: int, right_mode: int) -> tuple[tuple[int, ...] \| None, complex]` | projector and spectator-corrected hop |
| 433 | `target_fswap_action(logical: tuple[int, ...], left: int, right: int) -> tuple[tuple[int, ...], complex]` | independent fermionic-swap target |
| 451 | `corrected_fswap_action(extended: tuple[int, ...], left_mode: int, right_mode: int) -> tuple[tuple[int, ...], complex]` | dressed extended-Fock FSWAP |
| 463 | `d_bits(extended: tuple[int, ...]) -> tuple[int, int]` | the two cell-parity observables |
| 467 | `two_cell_common_e_controls() -> dict[str, object]` | exhaustive code/off-code comparison |
| 580 | `corrected_frame_data(graph: base.ReferenceGraph, frame: np.ndarray)` | frame maps and local order-gauge correction |
| 593 | `frame_key(frame: np.ndarray) -> tuple[tuple[int, ...], ...]` | hashable integer frame |
| 597 | `covariance_controls() -> dict[str, object]` | 24-frame/576-product operator audit |
| 685 | `scope_and_note_controls() -> dict[str, object]` | claim-boundary guard |
| 727 | `main() -> None` | assemble summary and terminal |

## 3. Cycle-719 controller token surface

### A/B rail layout and one-token convention

For `P=len(program)` stations, controller state uses two length-`P` bit tuples, `a_tokens` and `b_tokens` (`apply_controller_step`, line 181). In the literal word layout:

```text
A_s = data_wires + s
B_s = data_wires + P + s
work_s = data_wires + 2P + s
```

(`controller_word`, lines 162-178). Physically, `a_sites=track[::2]`, `b_sites=track[1::2]`, and each `work_s` is one site below `A_s`; the controller uses `3P` M2s (lines 432-440, 478).

`Q` is controlled by local occupancy `A_s`: if `a[s]` is set, station `s`'s bounded macro acts (lines 165-169, 187-190). `R` has two disjoint local SWAP layers:

```text
R1: A_s <-> B_s
R2: B_s <-> A_(s+1 mod P)
```

(lines 170-178, 191-195). Thus a full `H=RQ` advances an `A` token one station; `B` is the intermediate rail.

The declared one-token initialization is:

```text
A_s = 1 iff s is in token_positions, with token_positions=(0,) by default
B_s = 0 for every s
```

(`run_orbit`, lines 209-223). The supplied resource is “one controller token at source station and zero B/work rails” (lines 554-559). Thus the one-token sector is the **global** condition

```text
sum_s (A_s + B_s) = 1,
```

with held orbit sampled at full-step `A`-rail boundaries. Zero- and two-token inputs test domain sensitivity (lines 307-349).

### Local visibility versus global count

A bounded local check can see:

- the occupation bit `A_s` that controls `Q_s`;
- the same-station SWAP pair `(A_s,B_s)`;
- the transport-edge SWAP pair `(B_s,A_{s+1})`;
- therefore a double occupation on one such local pair, and pairwise
  collisions of tokens that lie within the chosen bounded neighborhood;
- local conformance of the two SWAP layers and a local clean-work condition.

A bounded-radius check on an arbitrarily long ring cannot infer `sum_s(A_s+B_s)=1`. Forbidding every adjacent collision establishes only a local hard-core condition: two sufficiently distant tokens pass. A neighborhood also cannot distinguish “one distant token” from “no token,” so global **at least one** is missing.

Existing token-related observations in the Cycle-719 core are:

- per-station `if a[station]` as the local `Q` control (lines 188-190);
- `live_before` and `live_after`, tuples of all occupied `A` indices, plus
  `sum(b)` in the orbit trace (lines 216-223);
- exact terminal comparison with `A=(1,0,...,0)` and `any(B)==False`
  (lines 226-241);
- the explicitly global diagnostic
  `sum(da) + sum(db) == 2` for a two-token run (lines 319-346);
- geometrical nearest-neighbor verification for every consecutive pair of
  sites on the alternating physical track (lines 432-453).

There is no named per-station token-number observable, per-edge charge observable, local projector enforcing global Hamming weight one, or autonomous one-token preparation/enforcement. The latter is explicitly open (lines 567-570). `A_s+B_s` and `B_s+A_{s+1}` are inferable local occupancies of displayed SWAP endpoints, not named/certified observables.

Relevant exact signatures are:

| Line | Exact signature | Token-surface role |
| ---: | --- | --- |
| 162 | `controller_word(program, data_wires)` | lays out `Q`, `A_s<->B_s`, and `B_s<->A_(s+1)` |
| 181 | `apply_controller_step(data, program, a_tokens, b_tokens, *, reverse=False, q_order=None)` | semantic two-rail step |
| 209 | `run_orbit(data, program, *, token_positions=(0,), reverse=False, q_orders=None)` | constructs token rows and traces one orbit |
| 226 | `held_certificate(bank_count)` | checks exact source return and empty `B` after an orbit |
| 307 | `order_and_domain_controls()` | zero-/two-token and order/domain attacks |
| 432 | `physical_controller_certificate(bank_count)` | alternating track placement and NN rail-cycle check |

## 4. Synthesis for a Cycle-724 spec writer

- A concrete **local hard-core token row** could check `(A_s,B_s)` and `(B_s,A_{s+1})` for double occupation, plus clean `work_s` and the local `Q`/SWAP transition. This detects coincident/adjacent collisions only; it does **not** prove exactly one ring token.

- A **Gauss-style local parity/charge row** could imitate Cycle-703 by attaching a local reference mode and constraining its parity against token/local modes. Cycle-703 supports this only for its seven-fermion BKSF cell with explicit Pauli definitions. Mapping Cycle-719 M2s into that graph, choosing modes, and supplying words are **new required data**.

- With a **supplied one-token source state**, local SWAPs preserve token number, so a refusal wrapper could reject malformed local occupancy, dirty work, or invalid transitions. No permitted source defines the Cycle-723 wrap; its predicates, failure action, radius, and composition law must be supplied.

- “Exactly one token,” “all non-source stations empty at terminal,” and comparison against `(1,0,...,0)` are **ring-global**. They need a global count/reduction, nonlocal label, bounded-size exhaustive fixture, or admitted genesis/certificate data. Adjacent-collision checks cannot replace them.

- A Cycle-719-style terminal steelman is therefore only **partially executable at bounded local resolution**: source occupancy, nearby emptiness, clean local work, and transitions are local; exclusion of a distant second token and global existence are not. Cycle-703 removes a matter-parity query for its basis bijection, but supplies neither a local exact-one ring counter nor physical encoder/preparation genesis.

## COMPLETENESS

All requested Cycle-703 claims are separated into proved/tested capacity, even-operator algebra, and open physical state/preparation layers. Every Cycle-703 runner function is listed with definition line, exact normalized signature, and role. Cycle-719 coverage is limited to A/B rails, one-token convention, local/global visibility, and token diagnostics. The synthesis marks global-count, Cycle-723-wrap, controller-to-BKSF-map, and preparation requirements explicitly.
