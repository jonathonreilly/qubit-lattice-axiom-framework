# Witness-family completeness on the exhaustive one-step star — Cycle 977

Date: 2026-08-10

Authority: none

Audit: unset; independent audit still required

Status: bounded support. On the complete word-length-at-most-one landed
basis-state gate family with support inside a target-centred radius-one star,
there are exactly 21 neighbour-dependence witnesses in three covariant
induced-law classes. The six Cycle-972 witnesses were not complete at this
enlarged scope. This finite result is not a probability law on the full
continuous `M_2(C)` possibility domain and does not fulfill the complete
Admissibility axiom.

Claim type: bounded_theorem

Primary runner:

- [`frontier_cycle977_witness_family_completeness_2026_08_10.py`](../scripts/frontier_cycle977_witness_family_completeness_2026_08_10.py)

Independent refutation checker:

- [`frontier_cycle977_witness_family_independent_check_2026_08_10.py`](../scripts/frontier_cycle977_witness_family_independent_check_2026_08_10.py)

Pinned caches:

- [`frontier_cycle977_witness_family_completeness_2026_08_10.txt`](../logs/runner-cache/frontier_cycle977_witness_family_completeness_2026_08_10.txt)
- [`frontier_cycle977_witness_family_independent_check_2026_08_10.txt`](../logs/runner-cache/frontier_cycle977_witness_family_independent_check_2026_08_10.txt)

Receipts:

- [`witness_family_completeness_cycle977_receipt_2026_08_10.json`](../outputs/witness_family_completeness_cycle977_receipt_2026_08_10.json)
- [`witness_family_completeness_cycle977_independent_check_receipt_2026_08_10.json`](../outputs/witness_family_completeness_cycle977_independent_check_receipt_2026_08_10.json)

Constitutional effect: none. No axiom, primitive, registry, policy, audit
result, or effective-status surface is edited.

## A_ENLARGED_FAMILY — declared exhaustive scope

Fix target site `a` and its six nearest neighbours `a+d`,

```text
D = {+e_x,-e_x,+e_y,-e_y,+e_z,-e_z}.
```

The spatial horizon is exactly the seven-site star
`S_a={a} union {a+d:d in D}`. The word-length cap is one and the gate-support
cap is three sites. The gate alphabet is exactly the basis-state constructors
exposed by the landed Cycle-719 semantic substrate:

```text
X(target), CNOT(control,target), TOF(control_1,control_2,target).
```

All operands must be distinct and lie in `S_a`. `CNOT` is ordered. The two
`TOF` controls are an unordered pair because exchanging them produces the
same landed gate and Boolean action. There is deliberately no additional
adjacency restriction between operands inside the star. Consequently the
complete family is

```text
1 identity
+ 7 X
+ 7*6 = 42 ordered CNOT
+ 7*C(6,2) = 105 TOF
= 155 distinct words.
```

Both target inputs and all neighbour conditions are exhaustive:

```text
x in {0,1}, n in {0,1}^6,
155*2*64 = 19,840 conditioned configurations.
```

Excluded, with no extrapolation, are words of length two or more, gates with
support outside `S_a`, and probability measures on the continuous `M_2(C)`
domain.

## B_WITNESS_CENSUS — 21, not 6

For word `W`, fixed target input `x`, neighbour condition `n`, and target
output `y`, the runner uses the landed `apply_semantic` method. A word is a
witness exactly when toggling at least one neighbour bit while holding `x`
and the other five neighbour bits fixed changes `y`.

Exactly 21 of 155 words are witnesses:

```text
6 CNOT(a+d -> a),                                     d in D;
15 TOF(a+d,a+e -> a),                    {d,e} subset D, d != e.
```

The full machine census has 42 dependent word/input rows out of 310 and
1,344 changed one-neighbour-bit pairs out of 59,520. The count decomposes as

```text
CNOT: 6 words * 2 target inputs * 32 spectator contexts = 384;
TOF:  15 words * 2 target inputs * 2 controls * 16 active-control contexts
      = 960;
total = 1,344.
```

This is also an analytic completeness argument. A length-one word can change
the target bit only if its gate target is `a`. `X(a)` changes the target but
does not read a neighbour. An incoming `CNOT` then has exactly one of the six
neighbours as control, giving six witnesses. An incoming `TOF` has exactly an
unordered pair of the six neighbours as controls, giving `C(6,2)=15`
witnesses. Every gate targeted away from `a` leaves the target coordinate
unchanged. There is no remaining gate kind or support choice inside the
declared family.

## C_CLASS_STRUCTURE — three covariant induced laws

The realized spatial group is

```text
G = Z^3 semidirect O_cubic^+,       |O_cubic^+|=24,
(a,d,e,x) -> (R a+t,R d,R e,x).
```

The exact algebraic-normal-form truth tables split the 21 witnesses into
three inequivalent classes under `G`:

| class | representative | induced target law | members | stabilizer |
|---|---|---|---:|---:|
| linear | `CNOT(a+e_x -> a)` | `y=x XOR n_(+x)` | 6 | 4 |
| perpendicular controls | `TOF(a+e_x,a+e_y -> a)` | `y=x XOR (n_(+x) AND n_(+y))` | 12 | 2 |
| opposite controls | `TOF(a+e_x,a-e_x -> a)` | `y=x XOR (n_(+x) AND n_(-x))` | 3 | 8 |

The CNOT class cannot merge with either TOF class because its Boolean
polynomial has degree one in neighbour bits rather than degree two. The two
TOF classes cannot merge because proper cubic rotations preserve the control
direction inner product: perpendicular pairs have `d dot e=0`, whereas
opposite pairs have `d dot e=-1`.

The primary exhausts every full seven-bit state, not merely the target bit,
under every rotation and unit-translation generator:

```text
rotation semantic comparisons:           24*155*2*64 = 476,160, failures 0;
translation-generator comparisons:         6*155*2*64 = 119,040, failures 0;
landed-core/coordinate bridge comparisons:   155*2*64 =  19,840, failures 0.
```

The class-specific transported comparison counts are 18,432 rotations and
4,608 translations for linear CNOT; 36,864 and 9,216 for perpendicular TOF;
and 9,216 and 2,304 for opposite TOF. Every class has zero failures.

### Prominent covariance finding

**NON-COVARIANT ENLARGED WITNESSES: NONE.** The family is closed under all 24
proper cubic rotations, and all three induced-law classes are covariant under
`Z^3 semidirect O_cubic^+` on the declared horizon.

The integrity certificate does not require this finding. A non-covariant
witness would remain a passing, prominently reported census result when the
failure lists and verdict reconcile.

## Why the 20-word family undercounted

Cycle 972 was complete on its declared 20-word family, but that declaration
imposed two extra restrictions not implied by word length one and radius-one
support: it omitted `TOF` by a two-site arity restriction, and it admitted
only centre-neighbour CNOTs rather than every ordered CNOT supported in the
star.

The exhaustive enlargement adds 135 words:

```text
30 off-centre CNOT + 105 TOF.
```

The 30 extra CNOTs add zero witnesses: a one-step CNOT affects `a` only when
`a` is its target, and all six such incoming centre-edge CNOTs were already in
the 20-word family. The 105 TOFs add exactly 15 witnesses: precisely those
with target `a` and both controls among its six neighbours. Thus

```text
old 6 witnesses + 0 extra-CNOT witnesses + 15 TOF witnesses = 21.
```

The undercount was exactly an artifact of excluding the substrate's
three-site `TOF` gate kind. It was not caused by the narrower CNOT edge menu.

Cycle 975's `|2p-1|` visibility mechanism remains consistent but its old
six-word marginal count is not silently extended here. For either new TOF
class, toggling one control changes the marginal only in contexts where the
other control equals one; on those contexts the same exchanged-XOR rows give
strength `|2p-1|`. Uniform input still cancels, while every non-uniform input
exposes the new witnesses on an appropriate neighbour context.

## D_CONTROLS and independent refutation

The primary reads exactly six explicit sources: the landed axiom and
Cycle-719 core, plus the Cycle-972 and Cycle-975 runner/note pairs at pinned
commits. Predecessor runners are parsed as AST and never executed; predecessor
notes are read as text. The live axiom and core are SHA-256 pinned. The
primary replays deterministically, runs below its 300-second timeout, and
stays below the 6 KB stdout ceiling.

The independent checker reads three files: primary source as AST, primary
receipt, and primary cache. It imports neither the primary nor Cycle-719. It
reconstructs the 155-word Boolean family, builds the proper rotations from
oriented orthonormal frames, and recomputes every witness signature, class,
rotation comparison, and translation comparison. It reproduces the 21-word
census and all three classes. Six active corruptions—family size, witness
count, representative law, class count, covariance flag, and undercount
cause—are all rejected.

```text
PASS R0_REFUTE_ENLARGED_FAMILY
PASS R1_REFUTE_WITNESS_CENSUS
PASS R2_REFUTE_CLASSES_AND_COVARIANCE
PASS R3_PRIMARY_RECEIPT_CACHE_BINDING
PASS R4_ACTIVE_CORRUPTION_PROBES
PASS R5_CONTROLS
VERDICT: PRIMARY_SURVIVES_INDEPENDENT_REFUTATION_ATTEMPT
TOTAL: PASS=6 FAIL=0
```

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "is the six-word Cycle-972 witness census complete, or an artifact of its declared 20-word family?"
source_of_blocker_text: user_goal
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "independently audit the 155-word bounded theorem; do not promote it to the full continuous M_2(C) Admissibility law"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: "exact on the declared 155-word, radius-one, word-length-at-most-one landed basis-state family"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "finite basis-state and one-step support cap; no full continuous M_2(C) probability law"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Verdict

Six was not the complete witness count at the exhaustive one-step star scope.
The complete count is 21, and the single Cycle-972 XOR class enlarges to three
covariant classes: incoming CNOT, incoming TOF with perpendicular controls,
and incoming TOF with opposite controls. No non-covariant enlarged witness is
present. The exact source of the old undercount is the declared exclusion of
`TOF`, not a failure of the earlier census on its own 20-word horizon.
