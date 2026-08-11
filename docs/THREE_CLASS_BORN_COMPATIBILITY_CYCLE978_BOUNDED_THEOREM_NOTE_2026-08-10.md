# Born compatibility with the three-class neighbour law — Cycle 978

Date: 2026-08-10

Authority: none

Audit: unset; independent audit remains required

Claim type: bounded_theorem

Actual current surface: bounded support. On the reconstructed finite event
space and the exhaustive word-length-at-most-one basis-state gate family
inside a target-centred radius-one star, all five finite event weightings are
compatible separately with each of the three covariant induced-law classes,
but none is compatible with all three as one unindexed conditional rule.
This does not construct a probability law on the full continuous `M_2(C)`
possibility domain and does not select a Born weighting.

Primary runner:

- [`frontier_cycle978_three_class_born_compatibility_2026_08_10.py`](../scripts/frontier_cycle978_three_class_born_compatibility_2026_08_10.py)

Independent refutation checker:

- [`frontier_cycle978_three_class_born_independent_check_2026_08_10.py`](../scripts/frontier_cycle978_three_class_born_independent_check_2026_08_10.py)

Pinned caches:

- [`frontier_cycle978_three_class_born_compatibility_2026_08_10.txt`](../logs/runner-cache/frontier_cycle978_three_class_born_compatibility_2026_08_10.txt)
- [`frontier_cycle978_three_class_born_independent_check_2026_08_10.txt`](../logs/runner-cache/frontier_cycle978_three_class_born_independent_check_2026_08_10.txt)

Receipts and provenance:

- [`three_class_born_compatibility_cycle978_receipt_2026_08_10.json`](../outputs/three_class_born_compatibility_cycle978_receipt_2026_08_10.json)
- [`three_class_born_compatibility_cycle978_independent_check_receipt_2026_08_10.json`](../outputs/three_class_born_compatibility_cycle978_independent_check_receipt_2026_08_10.json)
- [`cycle978_cited_primary_provenance_2026_08_10.json`](../outputs/cycle978_cited_primary_provenance_2026_08_10.json)

Constitutional effect: none. No axiom, primitive, audit result, registry,
policy, or effective-status surface is edited.

## A_REBUILD — independent reconstruction

The primary uses the landed
[`Cycle-719 semantic substrate`](../scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py)
to reconstruct the finite record-write event census. The cited Cycle-878,
Cycle-974, and Cycle-977 note/runner pairs are cached at declared commit/blob
pins, checked as note text and runner AST, and never imported or executed.
They provide provenance and falsifiable scope declarations, not verdicts.

The reconstruction gives 92,260 event atoms in 748 worlds, with 164 formed
worlds. The five weightings are:

| weighting | reconstructed definition | positive events | zero events |
|---|---|---:|---:|
| `M1_COUNTING` | `w(e)=1` | 92,260 | 0 |
| `M2_PER_WORLD_UNIFORM` | world score `a(w)=1`, uniform within each event-bearing world | 92,260 | 0 |
| `M3_OCCUPATION_WEIGHTED` | `a(w)=` clean-dwell occupation count, uniform within world | 19,172 | 73,088 |
| `M4_FORMATION_LIFETIME` | `a(w)=boundaries-formation_moment(w)+1` if formed, otherwise zero, uniform within world | 19,172 | 73,088 |
| `M5_FORMATION_MOMENT` | `a(w)=formation_moment(w)` if formed, otherwise zero, uniform within world | 16,076 | 76,184 |

Every vector is nonnegative and has positive total mass. Normalization
therefore defines a finite event probability `p_i(e)` for each row.

Independently, the primary enumerates every distinct word of length zero or
one over the landed `X`, `CNOT`, and `TOF` constructors, with distinct
operands supported anywhere in the seven-site star:

```text
1 identity + 7 X + 42 ordered CNOT + 105 TOF = 155 words.
```

Both target bits and all 64 neighbour conditions are evaluated, for 19,840
conditioned configurations. Exactly 21 words depend on a neighbour, in three
classes:

| class | representative law | exact witnesses |
|---|---|---|
| CNOT (6) | `y=x XOR n_(+x)` | `CNOT(+x->C)`, `CNOT(-x->C)`, `CNOT(+y->C)`, `CNOT(-y->C)`, `CNOT(+z->C)`, `CNOT(-z->C)` |
| perpendicular-control TOF (12) | `y=x XOR (n_(+x) AND n_(+y))` | `TOF(+x,+y->C)`, `TOF(+x,-y->C)`, `TOF(+x,+z->C)`, `TOF(+x,-z->C)`, `TOF(-x,+y->C)`, `TOF(-x,-y->C)`, `TOF(-x,+z->C)`, `TOF(-x,-z->C)`, `TOF(+y,+z->C)`, `TOF(+y,-z->C)`, `TOF(-y,+z->C)`, `TOF(-y,-z->C)` |
| opposite-control TOF (3) | `y=x XOR (n_(+x) AND n_(-x))` | `TOF(+x,-x->C)`, `TOF(+y,-y->C)`, `TOF(+z,-z->C)` |

The complete family has zero failures in 476,160 proper-rotation semantic
comparisons, 119,040 unit-translation semantic comparisons, and 19,840
landed-core/coordinate bridge comparisons.

## B_PER_CLASS_TEST — criterion and 5x3 result

For each class separately, the test uses Cycle 974's product-form criterion
verbatim, with the old single XOR kernel instantiated by the reconstructed
representative kernel `L_c`:

```text
P_i(e,x,n,y) = p_i(e) q(x,n) 1{y=L_c(x,n)},   q(x,n)=1/128.
```

A weighting is excluded only if its weights fail nonnegativity or
normalization, the product fails to reproduce event marginal `p_i`, or an
exact `(witness,x,n,y)` configuration disagrees with the reconstructed
class kernel. Every exclusion must carry the first such witness and
configuration.

| weighting | CNOT | perpendicular-control TOF | opposite-control TOF |
|---|---|---|---|
| `M1_COUNTING` | SURVIVES | SURVIVES | SURVIVES |
| `M2_PER_WORLD_UNIFORM` | SURVIVES | SURVIVES | SURVIVES |
| `M3_OCCUPATION_WEIGHTED` | SURVIVES | SURVIVES | SURVIVES |
| `M4_FORMATION_LIFETIME` | SURVIVES | SURVIVES | SURVIVES |
| `M5_FORMATION_MOMENT` | SURVIVES | SURVIVES | SURVIVES |

Per-class exclusions: none. Therefore there are no disagreeing witnesses to
report.

This is Cycle 974's fixed-input product-extension test, not a derivation of
the full Admissibility probability law. In particular, `x` is auxiliary to
the nearest-neighbour condition `n`; marginalizing the uniform carrier over
`x` makes each displayed XOR-family output marginal uniform. Thus per-class
survival does not by itself establish the axiom's required variation with
nearest-neighbour conditions.

## C_JOINT_TEST — one simultaneous rule

The full-family test keeps one unindexed conditional kernel. The same
`K_i(y|x,n)` in one product extension must equal every reconstructed class
kernel pointwise:

```text
P_i(e,x,n,y) = p_i(e) q(x,n) K_i(y|x,n),
K_i(y|x,n) = L_c(y|x,n) for every class c.
```

No class label or carrier is added: gate-word class is not a
nearest-neighbour condition supplied to the substrate rule. Nonnegative event
weights and the event marginal therefore remain necessary but cannot repair
a pointwise disagreement between class kernels.

The first exact disagreement is common to all five weightings:

```text
x=0
n=(+x,-x,+y,-y,+z,-z)=(1,0,0,0,0,0)
CNOT(+x->C):       y=1, distribution [0,1]
TOF(+x,+y->C):    y=0, distribution [1,0]
```

Joint survivors: none. Joint-only exclusions are `M1_COUNTING`,
`M2_PER_WORLD_UNIFORM`, `M3_OCCUPATION_WEIGHTED`,
`M4_FORMATION_LIFETIME`, and `M5_FORMATION_MOMENT`. Each has the exact
disagreeing witness pair and configuration above. The opposite-control
representative `TOF(+x,-x->C)` also gives `y=0` on that configuration, so it
disagrees with the CNOT representative there as well.

## D_ARTIFACT_VERDICT

```text
NULL_WAS_FAMILY_ARTIFACT
survivors/5: 0/5
```

Cycle 974's five-survivor null does not survive the one-rule joint test. The
two additional TOF law classes conflict pointwise with the CNOT class, so all
five weightings that survive every separate class test are excluded jointly.
This does not select a Born weighting: zero survivors refutes simultaneous
common-kernel compatibility on this enlarged surrogate rather than deriving
an event-marginal selector, occurrence rule, or Born rule.

## E_CONTROLS and independent refutation

The primary declares exactly three worktree-relative `AUDIT_INPUT_PATHS`: the
pinned text/AST provenance bundle, the
[`minimal axioms`](MINIMAL_AXIOMS_2026-06-29.md), and the landed Cycle-719
semantic core. All have SHA-256 and git-blob pins. Cited predecessor runners
are blocklisted and never loaded. The deterministic short event replay and
independent family replay agree with the full calculation.

The primary completed in 52.179 seconds with 3,635 stdout bytes:

```text
A_REBUILD PASS
B_PER_CLASS_TEST PASS
C_JOINT_TEST PASS
D_ARTIFACT_VERDICT PASS
E_CONTROLS PASS
TOTAL: PASS=5 FAIL=0
```

The independent checker reads three worktree-relative files, parses the
primary as AST without importing it, and reconstructs the 155-word Boolean
family, 21 witnesses, three classes, and proper-rotation covariance without
Cycle-719. It derives the product-extension verdict algebraically, binds the
primary source/receipt/cache by SHA-256, and rejects eight active corruptions:
family size, witness count, class membership, a per-class verdict, joint
survivors, joint disagreeing witness, artifact label, and Born-wall status.

It completed in 0.862 seconds with 1,596 stdout bytes:

```text
R0_PRIMARY_AST_AND_PINS PASS
R1_INDEPENDENT_FAMILY_AND_CLASSES PASS
R2_REFUTE_PER_CLASS_AND_JOINT PASS
R3_RECEIPT_CACHE_BINDING PASS
R4_ACTIVE_CORRUPTION_PROBES PASS
R5_CONTROLS PASS
TOTAL: PASS=6 FAIL=0
```

The certificate gates construction, exhaustive reconciliation, partition
bookkeeping, binding, corruption sensitivity, determinism, and resource
controls. It does not gate on a desired survivor count or artifact verdict.

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "did Cycle 974's five-survivor null persist only because its 20-word family omitted two induced-law classes?"
source_of_blocker_text: user_goal
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "submit this bounded theorem to independent audit; do not promote it to a full continuous M_2(C) probability law"
```

## Claim boundary

```yaml
actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: "exact on the reconstructed finite event space and the declared 155-word one-step basis-state family"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "finite one-step basis-state horizon; no full continuous M_2(C) probability law or Born selector"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
