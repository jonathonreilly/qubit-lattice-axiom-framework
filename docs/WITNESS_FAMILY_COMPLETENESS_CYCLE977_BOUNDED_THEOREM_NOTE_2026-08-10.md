# Witness-family completeness on a declared one-step semantic quotient — Cycle 977

Date: 2026-08-10

Authority: none

Audit: unset; independent audit still required

Status: bounded support. On the explicitly declared semantic quotient of
word-length-at-most-one basis-state gates with pairwise-distinct operands and
support inside a target-centred radius-one star, there are exactly 21
neighbour-dependence witnesses in three covariant induced-law classes. The six
Cycle-972 witnesses were not complete at this enlarged scope. This finite
result is not a probability law on the full continuous `M_2(C)` possibility
domain and does not fulfill the complete Admissibility axiom.

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
cap is three sites. The gate alphabet is an explicit theorem-family choice of
three basis-state constructors reachable through the landed
[`Cycle-719 semantic substrate`](../scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py)
and its [`Cycle-715 gate implementation`](../scripts/frontier_cycle715_recurrent_directional_packet_bank_2026_07_26.py):

```text
X(target), CNOT(control,target), TOF(control_1,control_2,target).
```

Pairwise-distinct operands are a declared scope restriction; the constructors
themselves do not enforce it. `CNOT` is ordered. The two `TOF` controls are an
unordered pair in this theorem's semantic quotient: exchanging them produces
the same Boolean action, although it produces unequal ordered-wire `Gate`
dataclass values. There is deliberately no additional adjacency restriction
between operands inside the star. Consequently the complete declared
semantic-quotient family is

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

Excluded, with no extrapolation, are repeated-operand gate objects, distinct
`Gate` encodings that differ only by TOF control order, gate kinds outside the
declared alphabet, words of length two or more, gates with support outside
`S_a`, and probability measures on the continuous `M_2(C)` domain.

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

This is also an analytic completeness argument on that declared quotient. A length-one word can change
the target bit only if its gate target is `a`. `X(a)` changes the target but
does not read a neighbour. An incoming `CNOT` then has exactly one of the six
neighbours as control, giving six witnesses. An incoming `TOF` has exactly an
unordered pair of the six neighbours as controls, giving `C(6,2)=15`
witnesses. Every gate targeted away from `a` leaves the target coordinate
unchanged. There is no remaining descriptor inside the declared family.

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

**NON-COVARIANT ENLARGED WITNESSES IN THE DECLARED QUOTIENT: NONE.** The family is closed under all 24
proper cubic rotations, and all three induced-law classes are covariant under
`Z^3 semidirect O_cubic^+` on the declared horizon.

The integrity certificate does not require this finding. A non-covariant
witness would remain a passing, prominently reported census result when the
failure lists and verdict reconcile.

## Why the 20-word family undercounted

[`Cycle 972`](COVARIANT_DEPENDENCE_LAW_CYCLE972_BOUNDED_THEOREM_NOTE_2026-08-09.md)
was complete on its declared 20-word family, but that declaration
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

[`Cycle 975`](INPUT_DISTRIBUTION_DEPENDENCE_LAW_CYCLE975_BOUNDED_THEOREM_NOTE_2026-08-10.md)'s
`|2p-1|` visibility mechanism remains consistent but its old
six-word marginal count is not silently extended here. For either new TOF
class, toggling one control changes the marginal only in contexts where the
other control equals one; on those contexts the same exchanged-XOR rows give
strength `|2p-1|`. Uniform input still cancels, while every non-uniform input
exposes the new witnesses on an appropriate neighbour context.

## D_CONTROLS and independent refutation

The primary reads exactly six explicit sources: the live axiom and Cycle-719
core, plus the Cycle-972 and Cycle-975 runner/note pairs at main-contained
pinned commits. Predecessor runners are parsed as AST and never executed;
predecessor notes are read as text. The live axiom and core are SHA-256 pinned.
The primary replays deterministically, runs below its 300-second timeout, and
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

## Premise boundary after the Record simplification

The finite census uses the Lattice covariance surface and the separately
declared Boolean gate semantics. It does not use Record, a scalar collection
functional `I`, finite additivity, `I(empty)=0`, a readout-context selector,
Born weights, or any record-production rule. The primary pins the current
[`Minimal Framework Axioms`](MINIMAL_AXIOMS_2026-06-29.md) and explicitly
checks the current Record surface: records form; a present record locks one
admissible local possibility; an empty site is unreadable; no scalar value or
additivity law is supplied. The Admissibility distribution sentence is context
only here; the theorem enumerates deterministic Boolean basis states and makes
no continuous-domain probability claim.

## No-Go Discipline Gate

The exclusion claim is only that no descriptor in the declared 155-member
semantic quotient is a further witness and that none of its 21 witnesses fails
the tested covariance law. It is not an exhaustion result for repeated
operands, ordered `Gate` encodings, other gate alphabets, longer words, larger
supports, or the continuous possibility domain.

- **N1 — alternative routes:** the five normalized attacks below materially
  differ in their object or terminal proof obligation. Each was `ATTEMPTED` in
  this cycle by the [primary runner](../scripts/frontier_cycle977_witness_family_completeness_2026_08_10.py),
  with the finite census independently reconstructed by the
  [refutation checker](../scripts/frontier_cycle977_witness_family_independent_check_2026_08_10.py).

| Route | Attempt | Why it does not refute the declared exclusion | Honesty marker | Authority/evidence |
|---|---|---|---|---|
| Descriptor omission | Generate every identity, X, ordered CNOT, and canonical-control TOF descriptor with distinct operands on seven sites and seek a missing member | Independent constructions both reconcile `1+7+42+105=155` unique descriptors | `ATTEMPTED` | primary A certificate; independent R0 |
| Hidden target-changing path | Search every non-targeted gate and target `X` for neighbour-sensitive target output | Full seven-bit evaluation shows only target-centred incoming CNOT/TOF reads a neighbour; all other descriptors leave the target neighbour-independent | `ATTEMPTED` | primary B; independent R1 |
| TOF control-order escape | Reverse both TOF controls and seek a new semantic witness | All 128 seven-bit actions agree for each exchanged pair; ordered dataclass values are explicitly quotiented, not silently identified | `ATTEMPTED` | primary input controls; independent canonical-control reconstruction |
| Class-merger or class-split escape | Seek a fourth witness orbit or merge the reported three | ANF neighbour degree separates CNOT from TOF, while the cubic-invariant control dot product separates perpendicular from opposite TOF pairs; exhaustive signatures partition all 21 | `ATTEMPTED` | primary C; independent R2 |
| Covariance escape | Rotate or translate a declared witness to a missing or semantically inequivalent member | All 24 proper rotations, six unit-translation generators, and the landed/coordinate bridge reconcile with zero failures on all declared states | `ATTEMPTED` | primary C; independent R2 |

- **N2 — scope-coordinate independence:** no derivation wall or new-axiom
  requirement is claimed. The four explicit domain caps are independently
  relaxable; neither direction in any pair follows automatically.

| Pair | Closing first closes second? | Closing second closes first? | Independent? |
|---|---|---|---|
| Boolean basis (B), radius-one star (S) | no | no | yes |
| B, word length at most one (L) | no | no | yes |
| B, declared gate/operand quotient (G) | no | no | yes |
| S, L | no | no | yes |
| S, G | no | no | yes |
| L, G | no | no | yes |

- **N3 — hidden-wall scan:** a case-insensitive scan for `we assume`, `by
  construction`, `as is standard`, `the framework provides`, `bridge
  context`, `background`, `naturally`, `obviously`, `standard QFT`,
  `registered`, and `canonical` found no hidden premise. The sole close hit,
  “canonical-control”, names the explicitly defined TOF control-order quotient
  rather than importing an authority. The basis, spatial, word-length,
  alphabet, distinct-operand, and quotient conditions are explicit above.
  “Landed” names the linked executable source; it is not used to import a
  theorem about all constructible gate objects.
- **N4 — residual matching:** neither predecessor is counted as a proof of the
  current exclusion; both are provenance only.

| Cited provenance | Residual attacked there | Current residual | Match? | Disposition |
|---|---|---|---|---|
| [Cycle 972](COVARIANT_DEPENDENCE_LAW_CYCLE972_BOUNDED_THEOREM_NOTE_2026-08-09.md) | completeness and covariance on its declared 20-word I/X/centre-edge-CNOT family | completeness and covariance on the new 155-member semantic quotient including every declared TOF | no | provenance/undercount comparison only; zero no-go witness weight |
| [Cycle 975](INPUT_DISTRIBUTION_DEPENDENCE_LAW_CYCLE975_BOUNDED_THEOREM_NOTE_2026-08-10.md) | marginal visibility of the earlier XOR witnesses under a common input law | descriptor and witness completeness before probabilistic marginalization | no | consistency context only; zero no-go witness weight |

  The present exclusion therefore stands on the new direct enumeration and
  analytic target-locality argument, not a residual-mismatched citation.
- **N5 — resolution rhetoric:** the primary cache lands these exact execution
  certificates:

```text
per_element: checked and executed -- all 19,840 declared word and seven-bit basis-state configurations were evaluated
per_site: checked and executed -- the target and each of its six radius-one neighbour coordinates were toggled and transported
per_mode: checked and not executed -- this finite Boolean basis theorem has no Fourier, momentum, or continuous-mode exclusion
per_block: checked and executed -- all identity, X, CNOT, and TOF descriptor blocks and all three witness classes were reconciled
lattice_wide: checked and not executed -- generator covariance was proved by coordinate relabeling; no infinite lattice state was enumerated
```

- **N6 — partial-closure routes:** broader menus can be investigated by
  enlarging a theorem family: allow repeated operands, retain ordered gate
  encodings, add gate kinds, increase word length, expand spatial support, or
  introduce an explicit probability-law bridge. None is called a new axiom.
  The current Record axiom supplies no finite additivity, scalar `I`,
  `I(empty)=0`, readout selection, Born weights, or dynamics, and none is used
  or misclassified as a wall here.
- **N7 — steelman:** *A hostile reviewer should reject the broad phrase “all
  one-step landed gates”: the linked constructors accept repeated operands,
  reversed TOF controls are unequal `Gate` dataclass values, `mcx` exposes
  composed higher-control operations, and the wider framework contains other
  quantum primitives. Those routes can create additional encodings or longer
  words that the count 155 never enumerates. The terminal obligation for a
  broader theorem is to define validity/equivalence for the full constructor
  API and repeat the census on that enlarged menu.* This steelman defeats the
  broad reading, so the note does not ship it. It does not defeat the explicit
  pairwise-distinct, three-kind, word-length-one semantic quotient actually
  enumerated here; `mcx` is a returned tuple of primitive gates and lies beyond
  that word-length cap except where it reduces to an already listed CNOT/TOF.
- **N8 — cross-cycle echo:** the prescribed repository search covered
  `structurally undecidable`, `no retained primitive`, `requires new axiom`,
  and `cannot be derived from A_min`, together with the directly similar
  Cycle-972/975 witness notes. Cycle 972 is the decisive echo: its six-witness
  result stayed correct on its stated 20-word menu but ceased to be exhaustive
  after the menu was enlarged to include TOF. The retirement mechanism was a
  broader explicit finite census, not a new axiom. The same mechanism applies
  to every open enlargement named in N6, so this note keeps each cap visible
  and makes no claim beyond it. No prior new-axiom wall is inherited.

Disposition: PASS for the narrowly scoped finite exclusion. No route outside
the declared semantic quotient is ruled out.

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
packet_helper_runner: scripts/frontier_cycle977_witness_family_independent_check_2026_08_10.py
```

## Verdict

Six was not the complete witness count on the declared 155-member one-step
star semantic quotient. The complete count there is 21, and the single
Cycle-972 XOR class enlarges to three covariant classes: incoming CNOT,
incoming TOF with perpendicular controls, and incoming TOF with opposite
controls. No non-covariant witness is present in that quotient. The exact
source of the old undercount is the declared exclusion of `TOF`, not a failure
of the earlier census on its own 20-word horizon.
