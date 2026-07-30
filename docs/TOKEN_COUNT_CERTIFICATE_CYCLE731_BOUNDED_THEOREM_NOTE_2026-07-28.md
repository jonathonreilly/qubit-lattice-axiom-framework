# Bounded A-rail occupancy counter/comparator and ring-11 refusal fixture — Cycle 731

Date: 2026-07-28

Authority: none

Audit: unset

Status: bounded conditional theorem

Claim type: bounded_theorem

Primary runner:
[`frontier_cycle731_token_count_certificate_2026_07_28.py`](../scripts/frontier_cycle731_token_count_certificate_2026_07_28.py)

Independent check:
[`frontier_cycle731_count_certificate_independent_check_2026_07_28.py`](../scripts/frontier_cycle731_count_certificate_independent_check_2026_07_28.py)

Load-bearing proposal-only dependencies:

- [Cycle 719 recurrent matter-history controller](RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md)
- [Cycle 724 local token-row refusal construction](LOCAL_TOKEN_ROW_ENFORCEMENT_CYCLE724_BOUNDED_THEOREM_NOTE_2026-07-28.md)
- [Cycle 728 existential reference-chain compression](BKSF_HOLONOMY_COMPRESSION_CYCLE728_BOUNDED_THEOREM_NOTE_2026-07-28.md)
- [Cycle 730 local charge-row refusal guard](CHARGE_ROW_ENFORCEMENT_CYCLE730_BOUNDED_THEOREM_NOTE_2026-07-28.md)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result

For `N >= 1`, let `A_0,...,A_(N-1)` be Boolean A-rail occupancy
bits. Supply a clean `N.bit_length()`-bit counter, clean increment and
comparison scratch, a clean mismatch latch, and an expected A-rail occupancy
`k` with `0 <= k <= N`. The emitted high-carry-first reversible word:

1. computes `popcount(A)` into the little-endian counter;
2. sets the latch exactly when `popcount(A) != k`;
3. leaves the A rail unchanged and does not touch B, the reference rail, or
   `h`; and
4. restores every counter/comparison work bit under the literal reverse.

The proof is the binary-increment induction below. The primary and independent
runner also execute the actual emitted X/CNOT/TOF gates exhaustively for every
A mask and every `k` on `N=1,...,12`: 98,304 cases, zero behavioral,
scratch, or inverse failures. The ring-11, `k=1` counter/comparator gate stream
has 122 gates and SHA-256
`e5d68c4614075757500e1f4f661a9dc078eeebf2adaeb329b5d6a71437147ff8`.
The bounded outcome table SHA-256 is
`db9d3f14a45f7cad3b074da497364a60bee6e32485e9597236dd888374c223b3`.

This is an **A-rail occupancy** statement. It is not a count of total A+B
occupancy.

## Integrated finite fixture

The same counter/comparator is inserted into the Cycle-730 refusal word as one
fixed global logical register. On the following exact finite domain:

- the 11-station two-bank program;
- every unordered two-site A placement (`C(11,2)=55`);
- `B=0`, `h=0`;
- the `r_0=0` canonical static reference extension constructed separately for
  each placement;
- the fixed clean data and auxiliary genesis; and
- supplied expected A occupancy `k=1`;

one actual integrated word refuses the data action for all 55 placements,
rotates the rails as declared, returns references, `h`, and every auxiliary
clean, and reverses exactly. The `(0,5)` placement has reference mask `62`.
The refusal-event table SHA-256 is
`73ad99cfa287b117673e877363c73b736926395b1dd0b24d2d97b2f453844efd`.

This 55-case result is a fixed-reference, one-word fixture. It is not a
recurrent admission theorem.

## Proof of the counter/comparator lemma

Write the counter as little-endian bits `c_0,...,c_(w-1)`. For one control
bit `a`, the increment word visits targets from high to low. Before `c_j` is
toggled, the lower bits `c_0,...,c_(j-1)` still contain their pre-increment
values, so the multi-controlled toggle on `c_j` fires exactly when `a=1` and
all lower bits carry. The final CNOT toggles `c_0` exactly when `a=1`.
Therefore the word adds `a` modulo `2^w`.

Starting from zero and applying this once for each A bit yields
`popcount(A)`. Because `w=N.bit_length()`, the largest value `N` fits without
overflow. The comparator X-conjugates counter bits where `k` has a zero,
initializes the latch to one, and toggles it only when every conjugated counter
bit is one. Thus the live latch is zero exactly at `popcount(A)=k` and one
otherwise. Every primitive is self-inverse; reversing comparison and counting
restores the supplied clean work.

The runners additionally check the width and overflow inequalities for
`N=1,...,129` and reject the out-of-domain ring-11 values `k=-1` and `k=12`.

## Explicit global-parity boundary

Cycle 730 constructs a per-active-station local charge guard, not a global
parity acceptor. Cycle 731 does not promote it. The actual integrated word
freezes the concrete boundary input

`(A_mask, B_mask, refs_mask, h, k) = (1, 0, 2, 0, 1)`.

Its A occupancy matches `k`, while total rail parity does not match `h`.
Nevertheless the data changes after one word and after the full 11-word orbit;
references, `h`, and auxiliaries return clean, and both evolutions invert
exactly. This executable counterexample is part of both runner checks. No
count-and-parity behavioral iff is asserted.

## Supplied, derived, and open

### Supplied

- expected A occupancy `k` (with the integrated fixture using `k=1`);
- clean counter, increment scratch, comparison scratch, and mismatch latch;
- ring size, program, orientation, static reference rail, `h`, B rail, and
  clean data/controller genesis for the integrated fixture;
- all load-bearing Cycle 719/724/728/730 proposal-only constructions linked
  above.

### Derived

- the reversible A-rail counter/comparator lemma;
- bounded actual-gate confirmation on `N=1,...,12`;
- exact counter/comparator uncompute and zero B/reference/`h` touches;
- refusal and exact returned work for the stated 55-case ring-11 fixture;
- the concrete global-parity scope counterexample.

### Open

- derivation or autonomous preparation of the expected occupancy and clean
  genesis;
- total two-rail A+B inventory enforcement;
- any global parity acceptor or count-and-parity behavioral equivalence;
- recurrent preservation or preparation of reference admissibility;
- a uniform controller/program family beyond the stated proof premises; and
- any physical transport, nearest-neighbor compilation, or execution
  equivalence for the fixed global logical counter register.

## Evidence discipline

Both runners freeze the complete recursive mutable-input closure, including
this note, and exercise missing-file, extra-file, and transitive-mutation
controls. The independent checker does not import the primary module or share
its evaluator. It obtains the actual primary gate stream through an explicit
source-execution boundary, evaluates those gates with a separate literal
bit-plane interpreter, and matches two independently launched primary semantic
report hashes. Runtime is recorded outside each deterministic semantic digest.

This is a proposal-only bounded theorem candidate. Authority remains `none`;
Audit remains `unset`; no audit grade or verdict is claimed.
