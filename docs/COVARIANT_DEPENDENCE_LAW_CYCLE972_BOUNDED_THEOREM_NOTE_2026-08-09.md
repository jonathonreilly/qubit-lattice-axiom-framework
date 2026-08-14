# The covariant neighbour-dependence law on the landed radius-one gate family — Cycle 972

Date: 2026-08-09

Authority: none

Audit: unset; independent audit still required

Status: bounded support. The landed deterministic basis-state machinery has
one covariant spatial class of nearest-neighbour XOR dependence on the
declared finite radius-one, word-length-at-most-one family. This is not a
probability law on the full continuous `M_2(C)` possibility domain and does
not by itself fulfill the complete Admissibility axiom.

Claim type: bounded_theorem

Primary runner:

- [`frontier_cycle972_covariant_dependence_law_2026_08_09.py`](../scripts/frontier_cycle972_covariant_dependence_law_2026_08_09.py)

Independent refutation checker:

- [`frontier_cycle972_law_independent_check_2026_08_09.py`](../scripts/frontier_cycle972_law_independent_check_2026_08_09.py)

Pinned caches:

- [`frontier_cycle972_covariant_dependence_law_2026_08_09.txt`](../logs/runner-cache/frontier_cycle972_covariant_dependence_law_2026_08_09.txt)
- [`frontier_cycle972_law_independent_check_2026_08_09.txt`](../logs/runner-cache/frontier_cycle972_law_independent_check_2026_08_09.txt)

Receipts:

- [`covariant_dependence_law_cycle972_receipt_2026_08_09.json`](../outputs/covariant_dependence_law_cycle972_receipt_2026_08_09.json)
- [`covariant_dependence_law_cycle972_independent_check_receipt_2026_08_09.json`](../outputs/covariant_dependence_law_cycle972_independent_check_receipt_2026_08_09.json)

Constitutional effect: none. No axiom, primitive, premise registry, policy,
audit result, or effective-status surface is edited. The claim-scoped helper
packet map is extended only so the declared independent checker reaches the
restricted audit packet.

## Exact target, premises, and obligation graph

The exact target is to classify neighbour-dependent target maps, prove their
translation/proper-cubic-rotation covariance and orbit counts, and evaluate the
explicit uniform-target-input marginal for every word in the declared 20-word
basis-state family below. The obligation graph has four leaves: exhaustive
family and truth-table enumeration; covariance under the stated spatial group;
orbit/stabilizer reconciliation; and the two-point marginal identity. The
primary and independent checker discharge those four finite leaves. No terminal
lemma stronger than the target is imported.

The load-bearing inputs are the current Lattice geometry in the
[`minimal axioms`](MINIMAL_AXIOMS_2026-06-29.md), the landed Cycle-719 Boolean
gate semantics, the declared word/gate/basis caps below, and—only for the
marginal subclaim—the explicitly chosen equal weights `1/2,1/2`. That uniform
weighting is a mathematical diagnostic, not a probability distribution supplied
by Admissibility or Record. Cycle 970 is provenance only, not a premise.

The current Record axiom contributes no step here. In particular, this result
uses no named scalar collection functional `I`, finite additivity,
`I(empty)=0`, scalar value for an absent record, readout-context selection, or
record-formation rule. The Qubit axiom identifies the wider one-site algebraic
domain only to state the boundary: the continuous-domain probability law,
longer words, other gate kinds, nonuniform marginals, and physical formation or
selection remain outside this theorem.

## Exact family, caps, and horizon

Fix a target site `a` of the [`Z^3` lattice](MINIMAL_AXIOMS_2026-06-29.md)
and its six nearest neighbours `a+d`, with

```text
d in D = {+e_x,-e_x,+e_y,-e_y,+e_z,-e_z}.
```

The finite spatial horizon is the seven-site star `{a} union {a+d:d in D}`.
The target and neighbour inputs range over the basis menu `{0,1}`, and all
`2^6=64` neighbour conditions are enumerated. The word-length cap is one.
The gate-kind menu is exactly the identity, `X`, and `CNOT` basis-state kinds
executed by the landed
[`Cycle-719 core`](../scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py).
The family consists of the distinct words

```text
1 identity
+ 7 X words, one at each star site
+ 12 CNOT words, both orientations on each of the six centre-neighbour edges
= 20 words.
```

`TOF` is excluded by the declared two-site gate-kind/arity condition; this is
a material family choice, not a consequence of radius one or the word-length
cap alone. Words of length two or more and continuous `M_2(C)` distributions are outside the declared horizon. In
particular, the marginal statement below is not extrapolated to longer
landed words.

For word `W`, fixed target input `x`, neighbour condition
`n=(n_d)_{d in D}`, and target outcome `y`, the measured distribution is the
deterministic point measure

```text
D[W,a,x](y | n) = 1{applying W to the seven-site basis state outputs y at a}.
```

The primary imports and calls the real landed `apply_semantic` method. The
coordinate translation check separately mutates a copied coordinate-state
dictionary. Before using that coordinate representation, the primary compares
it pointwise with landed `apply_semantic` on all 20 words, both target inputs,
and all 64 conditions: 2,560 bridge comparisons with zero failures. No
mutation claim is inferred from unchanged metadata.

## Full witness census

Exactly six of the 20 words induce state-resolved neighbour dependence at
the target:

```text
CNOT(a+e_x -> a)   CNOT(a-e_x -> a)
CNOT(a+e_y -> a)   CNOT(a-e_y -> a)
CNOT(a+e_z -> a)   CNOT(a-e_z -> a).
```

Every witness reads exactly its control bit `n_d`, moves the target basis
coordinate at `a`, leaves the control coordinate at `a+d` unchanged, and has
the same complete law

```text
y = x XOR n_d.
```

All five other neighbour bits are spectators and may be arbitrary. The exact
separated-pair templates, replicated over all `2^5=32` spectator contexts,
are

```text
x=0:  (target,control) (0,0)->(0,0), (0,1)->(1,1)
      D(y|n_d=0)=[1,0], D(y|n_d=1)=[0,1]

x=1:  (target,control) (1,0)->(1,0), (1,1)->(0,1)
      D(y|n_d=0)=[0,1], D(y|n_d=1)=[1,0].
```

Thus the exhaustive census has six witness words out of 20, 12 dependent
word/input rows out of 40, and 384 changed one-bit edge comparisons out of
7,680. Those 12 rows contain 768 of the 2,560 enumerated conditioned
configurations. Identity, every `X`, and every outward
`CNOT(a -> a+d)` is independent of all six neighbour bits at target `a`.
The primary also checks the claimed XOR value and unchanged control bit on all
`6*2*64=768` witness truth-table rows; both failure counts are zero.

The certificate checks only family construction and count reconciliation. It
does not require six witnesses, or any witness, for PASS.

## Covariance and exact orbit data

The realized spatial action is

```text
G = Z^3 semidirect O_cubic^+,
|O_cubic^+| = 24,
(a,d,x) -> (R a+t, R d, x).
```

The primary exhausts all 24 proper signed-permutation rotations, every family
word, both target inputs, and all 64 neighbour conditions: 61,440 semantic
comparisons. It also exhausts the six unit translation generators on the
same word/input/condition family: 15,360 comparisons. Unit generators imply
all translations in `Z^3`. There are no family-closure, rotation-semantic, or
translation-semantic failures. Therefore every translated or properly
rotated witness is another witness with its control direction, target site,
spectator bits, and XOR structure transported. The bounded witness law is
covariant under the realized group; no non-covariant witness was found.

At the induced word-law level, all six directions form one class. A
representative is `CNOT(a-e_x -> a)`; its rotation orbit has size six and its
proper-rotation stabilizer has size four. Under the full space group the orbit
is countably infinite, parameterized by arbitrary `a in Z^3` and the six
directions `d`.

At the finer state-resolved comparison level there are exactly two classes,
represented by

```text
(CNOT(a-e_x -> a), x=0)
(CNOT(a-e_x -> a), x=1).
```

Each has a six-element local rotation orbit and a four-element stabilizer.
They do not merge because translations and proper cubic rotations act on
lattice position, not on the basis value `x`. This two-row degeneracy does
not create a second induced dependence function: both rows belong to the
single law `y=x XOR n_d`.

The covariance certificate gates group construction, closure, exhaustive
comparison totals, failure-list reconciliation, and orbit-stabilizer
bookkeeping. The gate does not require a full orbit or an orbit-stabilizer
product for the observed witness subset, so it would pass and report a
non-covariant witness as a finding.

## Why the uniform marginal erases the dependence

The uniform-target-input marginal is

```text
Dbar[W,a](y | n) = (D[W,a,0](y | n) + D[W,a,1](y | n))/2.
```

For an incoming CNOT, fixed `n_d` makes `x -> x XOR n_d` a permutation of
`{0,1}`. Hence, for each `y` and either value of `n_d`,

```text
(1/2) sum_{x in {0,1}} 1{y=x XOR n_d} = 1/2.
```

The two state-resolved point masses exchange labels and average to the same
uniform distribution `[1/2,1/2]`. Identity, target `X`, neighbour `X`, and
outward CNOT likewise induce a permutation of `x` or leave it unchanged at
the target. Therefore zero of the 20 declared words, and zero of 3,840
one-bit marginal comparisons, breaks marginal independence. This is the
precise coexistence mechanism: state-resolved dependence is removed by a
uniform average over the variable that XOR permutes.

The length cap is essential. For example, the excluded length-two word
`CNOT(a -> a+d); CNOT(a+d -> a)` sends the target to `y=n_d`, so uniform
averaging over the original `x` would not erase neighbour dependence. No claim
about that word or any other longer landed word is included in the `0/20`
result.

## Independent refutation outcome

The checker imports neither primary nor core. It blocklists all five cited
inputs from execution, parses the Python inputs as AST, independently
reconstructs the gate family with Boolean semantics, and constructs the 24
rotations from oriented orthonormal frames rather than signed permutations.
It reproduced the 20-word census, six witnesses, two state-resolved classes,
one word-law class, every exact XOR/control truth-table row, 61,440 transported
rotation comparisons, 15,360 translated-state comparisons, and the zero
marginal result. Five active corruptions—witness count, covariance flag, class
count, marginal count, and an XOR-to-XNOR truth-table mutation—were all
rejected.

```text
PASS R0_PINS_BLOCKLIST_AND_AST
PASS R1_REFUTE_FULL_WITNESS_CENSUS
PASS R2_REFUTE_COVARIANCE_AND_CLASSES
PASS R3_REFUTE_MARGINAL_GAP
PASS R4_ACTIVE_CORRUPTION_PROBES
PASS R5_CONTROLS
VERDICT: PRIMARY_SURVIVES_INDEPENDENT_REFUTATION_ATTEMPT
TOTAL: PASS=6 FAIL=0
```

## Provenance and controls

Cycle 970 is consumed only as provenance at pinned commit
`6fd0de0a288d212a4a6ce3fdd4dc9019f30dbbad`: its runner blob
`4670bcb9d83cfc039f1336398c6a4aa4af014f7c` is parsed as AST and never
executed, while its note blob `f7b788d8076e7864bc5dbcbb33cb9e49554e494a`
is read as text. The primary confirms the earlier five-word family and its
declared open covariant residual before extending the orientation horizon.
The landed axiom and Cycle-719 core are SHA-pinned in the receipt. Both
runners replay deterministically, declare and enforce 300-second timeouts,
bind the primary receipt/cache to the current primary source and live landed
inputs, and remain under the stricter 6 KB stdout ceiling. Receipts are written
only after the actual stdout-size gate passes.

## Review record and hard landing condition

The sibling checker is load-bearing review evidence but is not imported by the
primary. Its restricted audit packet therefore requires the exact claim-scoped
mapping

```text
covariant_dependence_law_cycle972_bounded_theorem_note_2026-08-09
  -> scripts/frontier_cycle972_law_independent_check_2026_08_09.py
```

in `EXPLICIT_PACKET_HELPER_RUNNER_PATHS` in
`docs/audit/scripts/build_citation_graph.py`. Landing without that mapping would
leave the independent checker outside the audit packet and is forbidden.

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "is the state-resolved neighbour-dependence witness covariant under translations and proper cubic rotations, and is its bounded law unique?"
source_of_blocker_text: user_goal
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "independently audit the bounded covariance and orbit claims; do not promote this finite basis-menu result to the full continuous M_2(C) Admissibility law"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: "exact on the declared 20-word, radius-one, basis-state family"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "finite exact theorem conditional on the declared gate, word-length, basis-menu, and uniform-marginal choices"
packet_helper_runner: scripts/frontier_cycle972_law_independent_check_2026_08_09.py
proposal_allowed: false
proposal_allowed_reason: "finite basis menu and word-length cap; no full continuous M_2(C) probability law"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Verdict

Inside the declared landed family, neighbour dependence is the unique spatial
XOR law `y=x XOR n_d`, transported covariantly over every lattice target and
all six nearest-neighbour directions. The spatial law has one orbit; fixed
inputs `x=0` and `x=1` give two state-resolved row orbits. Uniform averaging
over `x` erases the dependence exactly. This closes the bounded covariant-law
question and leaves the full continuous-domain Admissibility law open.
