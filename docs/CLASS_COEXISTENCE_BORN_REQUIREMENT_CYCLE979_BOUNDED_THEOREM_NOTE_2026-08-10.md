# Class coexistence and conditional weighting nondiscrimination — Cycle 979

Date: 2026-08-10

Authority: none

Audit: unset; independent audit remains required

Claim type: bounded_theorem

Actual current surface: bounded support. On the declared target-centred
radius-one, word-length-at-most-one basis-state family, the three
neighbour-sensitive classes are alternatives: no complete program instance
contains witnesses from more than one class. Conditional on the explicit
non-axiom premise `P_instance`, this selects a per-instance test, and all five
declared finite event weightings survive it. The Admissibility axiom does not
choose that program indexing; the relevance of a cross-program common-kernel
test remains open. This is a nondiscrimination result, not Born compatibility,
a Born-rule derivation, an axiom-level probability-law construction, or a
result on the full continuous `M_2(C)` possibility domain.

Primary runner:

- [`frontier_cycle979_class_coexistence_born_requirement_2026_08_10.py`](../scripts/frontier_cycle979_class_coexistence_born_requirement_2026_08_10.py)

Independent refutation checker:

- [`frontier_cycle979_class_coexistence_independent_check_2026_08_10.py`](../scripts/frontier_cycle979_class_coexistence_independent_check_2026_08_10.py)

Pinned caches:

- [`frontier_cycle979_class_coexistence_born_requirement_2026_08_10.txt`](../logs/runner-cache/frontier_cycle979_class_coexistence_born_requirement_2026_08_10.txt)
- [`frontier_cycle979_class_coexistence_independent_check_2026_08_10.txt`](../logs/runner-cache/frontier_cycle979_class_coexistence_independent_check_2026_08_10.txt)

Receipts:

- [`class_coexistence_born_requirement_cycle979_receipt_2026_08_10.json`](../outputs/class_coexistence_born_requirement_cycle979_receipt_2026_08_10.json)
- [`class_coexistence_born_requirement_cycle979_independent_check_receipt_2026_08_10.json`](../outputs/class_coexistence_born_requirement_cycle979_independent_check_receipt_2026_08_10.json)

Constitutional effect: none. No axiom, primitive, registry, audit result,
grade, queue, or effective-status surface is edited.

## Declared families and caps

The result declares every load-bearing family:

| family | exact declaration |
|---|---|
| spatial family | one target-centred radius-one star: centre `C` and neighbours `(+x,-x,+y,-y,+z,-z)` |
| local basis family | `{0,1}` at each of the seven sites |
| program family | the pairwise-distinct-operand semantic quotient of length-zero/one words over `I`, `X`, ordered `CNOT`, and `TOF`; TOF control order is canonicalized because the two orders have identical Boolean action although the underlying gate objects are unequal |
| program-instance condition | conditional premise `P_instance`: one descriptor is one complete program instance; an identity has zero gate steps and every other program has exactly one gate step |
| weighting family | `M1_COUNTING`, `M2_PER_WORLD_UNIFORM`, `M3_OCCUPATION_WEIGHTED`, `M4_FORMATION_LIFETIME`, `M5_FORMATION_MOMENT` |
| target-input family | `mu_p=p delta_0+(1-p) delta_1`, common across compared neighbour conditions; the runner samples `p=0,1/4,1/2,3/4,1` and derives the exact `|2p-1|` law on each representative |
| neighbour family | all `2^6=64` basis conditions; all one-edge comparisons and spectator contexts |

Finite event caps are inherited from the main-contained pinned Cycle-719
snapshot: two fixture banks, source counts two through five, horizon 16,384,
and record-register cap 64. The primary rebuilds 92,260 event atoms in 748
worlds, including 164 formed worlds. The prior Cycle-975 and Cycle-978
runners are neither imported nor executed.

The current-main
[`Cycle-977 witness-family note`](WITNESS_FAMILY_COMPLETENESS_CYCLE977_BOUNDED_THEOREM_NOTE_2026-08-10.md)
already establishes this 155-member semantic quotient and the same class
census. The present runner recomputes every row; Cycle 977 is provenance and a
consistency comparator, not an executable premise or novelty claim.

## A_COEXISTENCE — exact per-descriptor census

The declared semantic quotient is exactly

```text
1 identity + 7 X + 42 ordered CNOT + 105 TOF = 155 complete programs.
```

Every nonidentity program contains one gate step. It therefore cannot contain
one witness class at one step and a second class at another step. Exhaustive
truth-table evaluation further identifies which single-step programs make the
centre output depend on a neighbour. The exact co-occurrence census is:

| classes present in one complete program | number of programs |
|---|---:|
| none | 134 |
| CNOT only | 6 |
| perpendicular-control TOF only | 12 |
| opposite-control TOF only | 3 |
| any pair of classes | 0 |
| all three classes | 0 |

Thus `multi_class_programs=0` and `max_classes_per_program=1`. The primary
receipt records all 155 programs individually, each with its stable index,
descriptor, word length, class list, neighbour-dependence flag, and changed
edge-pair count. Its full per-program census digest is

```text
4bdb22953055bd4bf1e4e094a4138aa04f63c6e6561e9dbf99d7d12898969771
```

The 21 nonempty per-program class lists are:

| class | exact programs, each with that class alone |
|---|---|
| CNOT | `CNOT(+x->C)`, `CNOT(-x->C)`, `CNOT(+y->C)`, `CNOT(-y->C)`, `CNOT(+z->C)`, `CNOT(-z->C)` |
| perpendicular-control TOF | `TOF(+x,+y->C)`, `TOF(+x,-y->C)`, `TOF(+x,+z->C)`, `TOF(+x,-z->C)`, `TOF(-x,+y->C)`, `TOF(-x,-y->C)`, `TOF(-x,+z->C)`, `TOF(-x,-z->C)`, `TOF(+y,+z->C)`, `TOF(+y,-z->C)`, `TOF(-y,+z->C)`, `TOF(-y,-z->C)` |
| opposite-control TOF | `TOF(+x,-x->C)`, `TOF(+y,-y->C)`, `TOF(+z,-z->C)` |

Every other program has the empty class list. The receipt enumerates those
134 names rather than hiding them behind a count. They are exactly the
identity, every `X`, every `CNOT` not directed from a neighbour into `C`, and
every `TOF` not having two neighbours control target `C`.

Thus, conditional on `P_instance`, **the three classes are alternative
programs, not coexisting witnesses inside one program instance.** The census
is data, not an integrity-gate expectation: the
requirement selector would return `JOINT` if any reconstructed program row
contained more than one class, and its injected-coexistence control confirms
that branch.

## B_CONDITIONAL_REQUIREMENT — what the census selects under `P_instance`

The exact Admissibility language used is:

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.

> For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

`P_instance` is an explicit condition from the user goal, not a consequence of
those sentences: one complete descriptor is treated as one substrate program
instance, and the finite compatibility test is scoped within that descriptor.
The declared family never places a CNOT word and either TOF word into the same
program at different sites or steps. Therefore, conditional on `P_instance`:

```text
conditional requirement: PER_INSTANCE
axiom implication status: NOT_DERIVED
cross-program JOINT trigger inside one declared instance: NOT_TRIGGERED
```

The runner also computes the cross-program fact directly, without relying on
an open PR: at `x=0` and `n=(1,0,0,0,0,0)`, `CNOT(+x->C)` outputs one while
`TOF(+x,+y->C)` and `TOF(+x,-x->C)` output zero. Whether the one fixed
Admissibility rule requires those alternative descriptors to share an
unindexed kernel is not decided by the current axiom text or by this theorem.
A future declared family containing a complete program with more than one
class would instead select the conditional `JOINT` branch within `P_instance`.

## C_CONDITIONAL_WEIGHT_TEST — five weights are not distinguished

For a realized program `g`, candidate event law `p_i(e)`, target-input law
`mu_p(x)`, uniform neighbour carrier `q(n)=1/64`, and its own landed Boolean
kernel `L_g`, the per-instance product extension is

```text
P_i,g(e,x,n,y) = p_i(e) mu_p(x) q(n) 1{y=L_g(x,n)}.
```

The target and neighbour factors normalize, so summing over `(x,n,y)` gives
`p_i(e)` exactly for every event, including zero-weight events. Each of all 155
landed program truth tables agrees on all `2*64` configurations with a
separately implemented Boolean descriptor evaluation. The three class sets
are each one complete orbit of the 24 proper cubic rotations, and the uniform
neighbour carrier is rotation-invariant. At `p=1/4`, every class also has a
strictly positive neighbour-variation witness. The conditional test excludes
a vector only for a negative event weight, a zero total, a failed event marginal, missing
required neighbour variation, failed proper-cubic closure, or a concrete
program/configuration mismatch. None occurs.

| weighting | conditional per-instance verdict | first exclusion witness |
|---|---|---|
| `M1_COUNTING` | SURVIVES | none |
| `M2_PER_WORLD_UNIFORM` | SURVIVES | none |
| `M3_OCCUPATION_WEIGHTED` | SURVIVES | none |
| `M4_FORMATION_LIFETIME` | SURVIVES | none |
| `M5_FORMATION_MOMENT` | SURVIVES | none |

```text
conditional-test survivors/5: 5/5
Born selection status: NOT_ADVANCED_BY_CONDITIONAL_TEST
```

The direct cross-program disagreement is not an exclusion witness inside the
conditional `PER_INSTANCE` test, because the descriptors are three alternative
complete programs. The open Cycle-978 PR is context only and has no authority
or load-bearing role here. Five survivors do not derive, prefer, or establish
compatibility with Born weights; they say only that this factorized conditional
test distinguishes none of the five finite event weightings. A full
nearest-neighbour probability law, the continuous `M_2(C)` domain, and a
local-to-event/Born lift remain open.

## D_INPUT_SCOPE — beyond the fixed-input representative

The conditional `5/5` result does not depend on a fixed `x=0` surrogate. The
product-extension marginal identity holds for every normalized
`mu_p`. The primary checks the two fixed endpoints, the uniform boundary, and
two non-uniform interior inputs.

For the required beyond-surrogate test, set

```text
p=P(X=0)=1/4,  P(X=1)=3/4.
```

For each class representative, choose neighbour conditions that change its
Boolean control function from zero to one. The output distributions are

```text
f(n)=0: P(Y=0,1)=[1/4,3/4]
f(n)=1: P(Y=0,1)=[3/4,1/4]
TV=1/2=|2p-1|.
```

The exhaustive class results are:

| class representative | first varied comparison at `p=1/4` | TV | survivors/5 |
|---|---|---:|---:|
| `CNOT(+x->C)` | vary `n_(+x)`, all other displayed bits zero | `1/2` | `5/5` |
| `TOF(+x,+y->C)` | vary `n_(+x)` with `n_(+y)=1` | `1/2` | `5/5` |
| `TOF(+x,-x->C)` | vary `n_(+x)` with `n_(-x)=1` | `1/2` | `5/5` |

This independently reproduces the Cycle-975 family law `TV=|2p-1|` on all
three representatives. At `p=1/2`, the output marginal is uniform and the TV
vanishes, while compatibility remains `5/5`; input visibility and weighting
compatibility are distinct questions. Thus C's conditional result is
input-independent inside the declared target-bit simplex. The selected
non-uniform samples exhibit the Admissibility memo's required neighbour
variation for these XOR-form representatives; they do not construct the
axiom-level probability law.

### Current Record boundary

The primary pins the current post-simplification Record section: records form;
when present, a record locks exactly one admissible local possibility; at most
one permanent record occupies a site; only record content is readable; and an
empty site cannot be read. It also guards that the current section does not
contain finite additivity or `I(empty)`. No part of the science here uses
Record, a scalar `I`, finite additivity, `I(empty)=0`, a Born weighting, or a
readout-selection rule. The event-vector reconstruction and finite Boolean
test are separate conditional machinery.

## Proof obligation graph

| obligation | disposition | evidence |
|---|---|---|
| A1 enumerate every declared complete program | discharged | exact 155 rows, kind counts `1/7/42/105`, stable digest |
| A2 attach every neighbour-sensitive class to its containing program | discharged | exhaustive truth-table edge scan; `134/6/12/3` census; three complete 24-rotation class orbits |
| A3 decide whether any one program has multiple classes | discharged | zero multi-class rows; maximum class count one |
| B1 separate the conditional test from the Admissibility axiom | discharged | two exact sentences pinned from the current memo; `P_instance` marked non-axiom; implication status `NOT_DERIVED` |
| C1 rebuild and validate the five event weightings | discharged | 92,260 events; every vector nonnegative and normalizable |
| C2 apply the conditional per-instance test | discharged | exact product marginal, 155 Boolean-kernel checks, `p=1/4` variation, and proper-cubic closure; `5/5` nondiscrimination |
| D1 test beyond fixed input | discharged | `p=1/4`; all three classes give `TV=1/2=|2p-1|` and `5/5` |
| M1 full axiom-level probability law and Born lift | open | not supplied by the finite program/product family |

## E_CONTROLS and independent refutation

The primary declares one mutable worktree source input: the current
[`minimal-axiom memo`](MINIMAL_AXIOMS_2026-06-29.md). The executable core
owned by the upstream
[`Cycle-719 bounded theorem note`](RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md)
is loaded with all of its transitive modules from an immutable Git archive of
the branch base, commit `39c74017b870c27c804e3992f2a11e90336476b2`; the core
is also bound by SHA-256 and git-blob pins. Live worktree changes anywhere in
that transitive bundle therefore cannot affect Cycle 979 without changing the
Cycle-979 source pin itself. The reconstructed event-weight vectors inherit
Cycle 719's bounded, audit-unset authority state; the Boolean program census
itself does not depend on that event-history import. The primary deterministic
replay agrees on the short event prefix and complete per-program census. The
canonical cache refresh records the exact runtime and stdout byte count.

```text
A_COEXISTENCE PASS
B_CONDITIONAL_REQUIREMENT PASS
C_CONDITIONAL_WEIGHT_TEST PASS
D_INPUT_SCOPE PASS
E_CONTROLS PASS
TOTAL: PASS=5 FAIL=0
```

The independent checker declares four inputs: primary source, primary receipt,
primary cache, and the minimal-axiom memo. The memo is read only to reproduce
the primary cache's declared-input fingerprint. The
checker parses the primary as AST without importing or executing it and
imports neither Cycle 719 nor the Cycle-975/Cycle-978 runners. It reconstructs
all Boolean descriptors, every per-program class row, all 24 proper rotations,
the conditional selection rule, direct cross-program mismatch, and the
`p=1/4` TV values. Receipt and cache headlines are
semantically bound to the canonical cache envelope's source and input pins.

Its refutation specification actively corrupts eight decisive claims:
program count, injected coexistence with an unchanged conditional selection,
class count, survivor count, exclusion without a witness, input dependence,
non-uniform TV, and the cache weight-test headline. All eight corruptions are
rejected. The canonical cache records its exact runtime and stdout byte count.

```text
R0_PRIMARY_AST_AND_PINS PASS
R1_INDEPENDENT_COEXISTENCE_CENSUS PASS
R2_REFUTE_CONDITIONAL_REQUIREMENT_AND_WEIGHT_TEST PASS
R3_NONUNIFORM_INPUT PASS
R4_RECEIPT_CACHE_BINDING PASS
R5_ACTIVE_CORRUPTION_PROBES PASS
R6_CONTROLS PASS
TOTAL: PASS=7 FAIL=0
```

Integrity gates gate bookkeeping only. The primary's A and B checks reconcile
whatever census is derived and map `multi_class_programs>0` to `JOINT`; they
do not require the observed alternative-program outcome. The injected
coexistence control verifies the unobserved branch.

## No-Go Discipline Gate

**Gate result:** a broad claim that the singular axiom can never impose a
cross-program rule is not made. The retained disposition is the exact finite
census plus a test explicitly conditional on non-axiom premise `P_instance`.
Longer programs, simultaneous spatial embedding, and a global
program-aggregation law remain open.

### N1 — alternative attacks on the bounded census

| attack route | status | result against the declared claim |
|---|---|---|
| omitted length-zero/one constructors | `ATTEMPTED` | the independent enumeration reproduces `1+7+42+105=155` |
| defect in the landed gate evaluator | `ATTEMPTED` | all 155 `2*64` truth tables match a separately implemented Boolean evaluator |
| overlap hidden by the class predicates | `ATTEMPTED` | CNOT and TOF gate kinds are disjoint; the TOF axial-control pairs partition exactly into 12 perpendicular and 3 opposite pairs |
| missing proper-cubic images | `ATTEMPTED` | each class is one complete orbit under all 24 proper cubic rotations |
| hidden failure of the factorized event-weight route | `ATTEMPTED` | all 92,260 event atoms are explicitly marginalized for each of five normalized nonnegative vectors; all five remain indistinguishable under the conditional test |

Longer programs and spatially combined programs were not executed and remain
open; they are not counted as attempted attacks.

### N2 — wall independence

There is one explicit non-axiom condition, `P_instance`: one complete
descriptor is treated as one substrate program instance. No collection of
independent walls is claimed, so there is no pairwise wall set to inflate or
collapse.

### N3 — hidden-condition scan

“Once a program is selected” has been replaced by the explicit `P_instance`
condition above. “Axiom,” “boundary,” and “program construction” refer,
respectively, to the quoted memo, the declared finite scope, and enumerated
Boolean data. None is used as an unstated physics input. “Canonical cache” is
bookkeeping evidence, not scientific authority.

### N4 — residual matching

| comparator | comparator residual | residual used here | match |
|---|---|---|---|
| direct finite cross-program probe | outputs `1,0,0` for the three representatives at the displayed `(x,n)` | recomputed in both primary and independent runners; relevance left open outside `P_instance` | yes |
| Cycle 978 / open PR #6104 | proposed common-kernel comparison | context only; zero authority and zero load-bearing witness weight | not used |
| Cycle 975 / PR #6084 | target-input dependence `TV=|2p-1|` | the same law, independently reproduced at `p=1/4` | yes |
| Cycle 977 / PR #6087 | current-main 155-member quotient and `134/6/12/3` census | independently recomputed here | yes |
| Cycle 719 bounded theorem | finite event/controller and gate semantics | event-vector and landed-gate executable import only | yes, with upstream conditionality retained |

### N5 — rhetoric and resolution

The primary cache lands substantive `per_element`, `per_site`, `per_mode`,
`per_block`, and `lattice_wide` lines. It checks five event vectors, the centre
readout under all six neighbour positions and spectator contexts, all 155
semantic-quotient programs, and proper-cubic orbit closure on the radius-one
star. It does not execute continuous modes or an infinite lattice embedding,
and no sentence promotes those unexecuted scopes to a negative.

### N6 — partial-closure paths

A global unindexed rule, a locally encoded program field, stochastic class
aggregation, and longer words remain legitimate follow-up constructions.
Nothing here calls them impossible or says that they require a new axiom. The
finite census and `P_instance` result remain useful without closing them.

### N7 — steelman

The strongest objection is that “one fixed rule” might mean one global
unindexed substrate law shared across alternative program descriptors. Then
the direct `1,0,0` cross-program disagreement is decisive unless the local
state encodes a program selector or a covariant aggregation law is
constructed. This remains live outside `P_instance`; it blocks any broader
no-go and is why every requirement statement here is explicitly conditional.

### N8 — cross-cycle echo

The open Cycle-978 PR echoes the global-common-kernel objection but supplies no
authority here; the mismatch is recomputed directly. Cycle 977 already owns
the finite witness-family census. Cycle 975 shows that fixed-input blindness
is repaired by non-uniform inputs, not by selecting a weighting. Cycle 719
supplies only the bounded executable substrate. None closes the longer-program
or global-aggregation routes.

## Review record and hard landing condition

The bounded scope ends at the declared 155-member semantic quotient and five
reconstructed finite event vectors. Review made `P_instance` explicitly
non-axiomatic, moved the cross-program mismatch into both runners, bound the
current Record surface and its non-use, identified the already-landed
Cycle-977 census, and narrowed the conclusion to conditional
nondiscrimination. No full-domain Born-law or longer-program conclusion is
proposed.

The independent refutation checker is load-bearing and must be present in the
restricted packet. The hard co-landing mapping is:

```text
"class_coexistence_born_requirement_cycle979_bounded_theorem_note_2026-08-10": ["scripts/frontier_cycle979_class_coexistence_independent_check_2026_08_10.py"]
```

The note, primary, independent checker, both canonical runner caches, both
receipts, helper mapping, and regenerated citation-graph manifest are one
landing unit. No generated audit verdict, queue, ledger, or effective-status
surface is part of that unit.

## Imports, derived facts, and open boundary

- **Executable import:** the core owned by the
  [`Cycle-719 bounded theorem note`](RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md)
  supplies event/controller construction and gate semantics; its upstream
  conditionality is inherited for the five event vectors.
- **Axiom text:** the current minimal-axiom memo supplies only the two quoted
  Admissibility sentences and the guarded current Record boundary; Record is
  not used by the science.
- **Current-main provenance:** Cycle 977 owns the already-landed 155-member
  semantic quotient and class census; every row is recomputed here.
- **Comparator only:** Cycle 975 (PR #6084) names the `|2p-1|` input family;
  Cycle 978 (open PR #6104) names a proposed common-kernel comparison. Neither
  prior runner is executed or treated as a verdict, and the cross-program
  mismatch is recomputed here.
- **Derived here:** all 155 per-program rows, the exact co-occurrence census,
  the conditional selection under `P_instance`, the direct cross-program
  mismatch, five nondiscriminated weights, and the non-uniform input test on
  all three representatives.
- **Open:** longer and multi-step programs, simultaneous spatial embedding of
  multiple classes, stochastic class aggregation, full continuous `M_2(C)`
  measures, and the local-to-event/Born lift.

No observational value, fitted selector, literature value, new axiom, or new
primitive enters the proof.

## Trace gate and claim boundary

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "conditional on P_instance, do the three displayed witness classes coexist inside one declared one-word program, and does the resulting per-instance test distinguish any of five finite weights?"
source_of_blocker_text: user_goal
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "submit the bounded conditional nondiscrimination result to independent audit; leave global indexing, longer programs, and a full Born law open"
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "exact finite census and conditional nondiscrimination theorem on a declared radius-one, word-length-at-most-one basis-state semantic quotient"
conditional_surface_status: "conditional on non-axiom premise P_instance; exact on the declared 155-member semantic quotient and five reconstructed finite event weightings"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "finite alternative-program family and product-extension compatibility test; no full continuous-domain probability law or Born selector"
audit_required_before_effective_retained: true
bare_retained_allowed: false
packet_helper_runner: scripts/frontier_cycle979_class_coexistence_independent_check_2026_08_10.py
```
