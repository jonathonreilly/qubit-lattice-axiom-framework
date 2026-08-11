# Born compatibility on the finite true-`Z^3` adjacency instance — Cycle 984

Date: 2026-08-11

Claim type: `bounded_theorem`

Actual current surface: `bounded-support`

Audit-status authority: independent audit lane only

Effective status: pipeline-derived only after independent audit ratification
and dependency closure

Constitutional effect: none. This packet edits no axiom, approved primitive,
premise registry, audit verdict, queue, ledger, or effective-status surface.

## Artifact map

Primary runner:

- [`frontier_cycle984_born_compatibility_z3_adjacency_2026_08_11.py`](../scripts/frontier_cycle984_born_compatibility_z3_adjacency_2026_08_11.py)

Independent refutation checker:

- [`frontier_cycle984_born_compatibility_z3_adjacency_independent_check_2026_08_11.py`](../scripts/frontier_cycle984_born_compatibility_z3_adjacency_independent_check_2026_08_11.py)

Pinned caches:

- [`frontier_cycle984_born_compatibility_z3_adjacency_2026_08_11.txt`](../logs/runner-cache/frontier_cycle984_born_compatibility_z3_adjacency_2026_08_11.txt)
- [`frontier_cycle984_born_compatibility_z3_adjacency_independent_check_2026_08_11.txt`](../logs/runner-cache/frontier_cycle984_born_compatibility_z3_adjacency_independent_check_2026_08_11.txt)

Receipts:

- [`born_compatibility_z3_adjacency_cycle984_receipt_2026_08_11.json`](../outputs/born_compatibility_z3_adjacency_cycle984_receipt_2026_08_11.json)
- [`born_compatibility_z3_adjacency_cycle984_independent_check_receipt_2026_08_11.json`](../outputs/born_compatibility_z3_adjacency_cycle984_independent_check_receipt_2026_08_11.json)

The restricted audit packet must contain the independent checker through this
claim-scoped helper mapping:

```text
born_compatibility_z3_adjacency_cycle984_note_2026-08-11:
  scripts/frontier_cycle984_born_compatibility_z3_adjacency_independent_check_2026_08_11.py
```

## Headline

```text
Z3 survivors/5: 5/5
transfer verdict: TRANSFERS
Born wall: UNMOVED
first weighting lost: none
exclusion witness: none
```

The five substrate-surviving weightings named in the supervisor task all
survive the independently rebuilt true-`Z^3` finite instance. No prior-cycle
receipt, cache, survivor field, or verdict is imported. The substrate result
is used only as the comparison stated by the task: if any of the five named
weightings had been excluded here, `FAILS_TO_TRANSFER` plus that weighting's
first exact witness would have been the headline.

This is a finite-family compatibility theorem. It does not derive Born
weights, prefer one surviving weighting, construct a full probability law on
the continuous `M_2(C)` possibility domain, or realize one simultaneous
translation-uniform law on the infinite lattice.

## Declared scope and cap

| item | exact declaration |
|---|---|
| spatial support | centre `C=(0,0,0)` and its six true `Z^3` nearest neighbours `(+x,-x,+y,-y,+z,-z)` |
| adjacency | exactly the six `L1=1` edges from `C` to a signed unit vector |
| local basis | `{0,1}` at each of the seven sites |
| program family | `I`, `X(C)`, six `CNOT(n->C)`, and fifteen `TOF(n,m->C)` with unordered distinct neighbour controls |
| word cap | zero or one gate; one descriptor is one complete program instance |
| condition cap | both centre inputs and all `2^6=64` neighbour conditions for all 23 programs |
| proper rotations | all 24 determinant-`+1` signed coordinate permutations |
| event caps | two fixture banks, source counts two through five, horizon 16,384, register cap 64 |
| input family | `mu_p=p delta_0+(1-p) delta_1`; compatibility evaluated at the required non-uniform `p=1/4` and robustness checked at `p=0,1/4,1/2,3/4,1` |

The word family has

```text
1 identity + 1 target X + 6 incoming CNOT + C(6,2) target TOF = 23 programs.
```

The pinned Cycle-719 executable substrate supplies only the finite event
construction used to rebuild the five event laws. The `Z^3` coordinate map,
adjacency, 23 Boolean descriptors, class census, rotations, compatibility
test, and transfer result are implemented in this packet rather than imported
from Cycles 975, 979, or 982.

## A_REBUILD_ON_Z3

### The independently rebuilt star

The primary prints the complete coordinate map, all six edges, and all 23
program names. Its explicit star is

```text
C=(0,0,0)
+x=(1,0,0)   -x=(-1,0,0)
+y=(0,1,0)   -y=(0,-1,0)
+z=(0,0,1)   -z=(0,0,-1)
E_Z3={{C,+x},{C,-x},{C,+y},{C,-y},{C,+z},{C,-z}}.
```

For target input `x` and neighbour bits `n`, the independently declared laws
are

```text
I:                 y=x
X(C):              y=x XOR 1
CNOT(d->C):        y=x XOR n_d
TOF(d,e->C):       y=x XOR (n_d AND n_e).
```

All `23*2*64=2944` target truth rows agree with a separately written Boolean
evaluator. Identity and `X(C)` carry no neighbour witness. The remaining 21
programs each carry exactly one of three classes:

| class | programs | orbit size | stabilizer | `J=||sum controls||^2` |
|---|---:|---:|---:|---:|
| incoming CNOT | 6 | 6 | 4 | 1 |
| perpendicular-control TOF | 12 | 12 | 2 | 2 |
| opposite-control TOF | 3 | 3 | 8 | 0 |

Thus the rebuilt class census is `NONE=2`, `CNOT=6`, perpendicular TOF `=12`,
opposite TOF `=3`, with `multi_class_programs=0` and
`max_classes_per_program=1`.

### The independently rebuilt five weightings

The primary rebuilds 92,260 event atoms across 748 event-bearing worlds:

```text
F=164, B0=47,872, B1=44,224; formed worlds=164; boundaries=180,224.
```

Let `N_w` be the event count of world `w`, let `D=1,073,280` be a common
multiple of all positive `N_w`, let `o(w)` be its clean-dwell occupation, and
let `f(w)` be its formation moment when formed. Integer numerators are enough
because each vector is normalized by its own positive total. The five
reconstructed laws are:

| weighting | event numerator in world `w` | total | zero / positive events | certificate digest |
|---|---|---:|---:|---|
| `M1_COUNTING` | `1` | 92,260 | `0 / 92,260` | `09d378b0359182d8a6bbf2020fbc27febe7a41e941d0568ee6b55cb9208a07d7` |
| `M2_PER_WORLD_UNIFORM` | `D/N_w` | 802,813,440 | `0 / 92,260` | `a48f74b6d20a95ba711b3a0e9c01611dca4f02d378a05141f2c28f8db2e9b1e4` |
| `M3_OCCUPATION_WEIGHTED` | `o(w)D/N_w` | 897,595,870,080 | `73,088 / 19,172` | `5779f8decc9e98a68b6f79e3f59b0dc722385f1c2a4a67ca3d40dcbb2e1b42d8` |
| `M4_FORMATION_LIFETIME` | `(180225-f(w))D/N_w` if formed, else `0` | 29,530,480,287,360 | `73,088 / 19,172` | `9ad27d71be675dd61136128557e8dba9410c3cb436863408f5aecd79eaf37e5d` |
| `M5_FORMATION_MOMENT` | `f(w)D/N_w` if formed, else `0` | 2,192,349,344,640 | `76,184 / 16,076` | `ed90e224161c1d9c502f0b0569ed31fd9869d83aafc97f9be613b00fd7916781` |

All five vectors are nonnegative and have positive total. The independent
checker does not load Cycle 719: it recomputes every numerator, total,
zero/positive count, and certificate digest from the primary receipt's 748
per-world sufficient-statistic rows.

## B_PER_INSTANCE_TEST

The criterion is reproduced verbatim from the landed Cycle-979 reading:

> An exclusion is licensed only by a negative event weight, a zero total, a failed event marginal, missing required neighbour variation, failed proper-cubic closure, or a concrete program/configuration mismatch.

**Adaptation:** none. The criterion is unchanged. The declared domain is
replaced by the axiom-native 23-program true-`Z^3` target-local family because
this task asks for the same per-instance test on that adjacency. The change
from 155 all-site descriptors to 23 target-local descriptors removes exactly
the 132 programs that cannot change the centre in one word; it removes no
centre neighbour-dependence witness. Each descriptor remains one complete
program instance.

For candidate event law `p_i(e)`, target law `mu_p(x)`, uniform neighbour
carrier `q(n)=1/64`, and the rebuilt Boolean kernel `L_g`, define separately
for each complete program `g`

```text
P_i,g(e,x,n,y) = p_i(e) mu_p(x) q(n) 1{y=L_g(x,n)}.
```

The target and neighbour carriers normalize, and every `(g,x,n)` has exactly
one Boolean output. Hence summing over `(x,n,y)` returns `p_i(e)` for every
event, including zero-weight events. All three class sets are complete proper-
cubic orbits. At `p=1/4`, every class has a strict positive neighbour-
variation witness. No truth-table mismatch occurs.

| weighting | per-instance verdict | first exclusion witness |
|---|---|---|
| `M1_COUNTING` | `SURVIVES` | none |
| `M2_PER_WORLD_UNIFORM` | `SURVIVES` | none |
| `M3_OCCUPATION_WEIGHTED` | `SURVIVES` | none |
| `M4_FORMATION_LIFETIME` | `SURVIVES` | none |
| `M5_FORMATION_MOMENT` | `SURVIVES` | none |

```text
survivors/5: 5/5
```

The primary's requirement selector is not hard-coded to the observed branch:
`multi_class_programs=0` selects `PER_INSTANCE`, while an injected coherent
multi-class row selects `JOINT`. Its candidate validator also accepts a
coherent synthetic one-exclusion result when the first exact witness is
present.

## C_TRANSFER_VERDICT

```text
TRANSFERS
```

Every one of the five weightings identified by the task as a substrate
survivor remains a survivor on the true-`Z^3` adjacency instance. Therefore
there is no lost weighting and no exclusion witness to headline. The Born wall
is `UNMOVED`: this compatibility test selects none of the five.

The transfer statement is deliberately narrower than a substrate equivalence.
It says only that the survivor set is unchanged under the declared finite
true-`Z^3` replacement. It does not identify semantic `K_7` wiring with
nearest-neighbour adjacency and does not extrapolate to longer words or an
infinite simultaneous law.

## D_INPUT_ROBUSTNESS

Set

```text
p=P(X=0)=1/4,  P(X=1)=3/4.
```

For every class representative, one neighbour comparison changes the Boolean
control function from zero to one. The two output distributions are

```text
f(n)=0: [1/4,3/4]
f(n)=1: [3/4,1/4]
TV=1/2=|2p-1|.
```

| class representative | first varied control | TV at `p=1/4` | survivors/5 |
|---|---|---:|---:|
| `CNOT(+x->C)` | `+x` | `1/2` | `5/5` |
| `TOF(+x,+y->C)` | `+x`, with the other control active | `1/2` | `5/5` |
| `TOF(+x,-x->C)` | `+x`, with the other control active | `1/2` | `5/5` |

The primary additionally evaluates `p=0,1/4,1/2,3/4,1`; all three classes
give `TV=|2p-1|` pointwise. Thus the transfer verdict is not bound to a fixed
`x=0` surrogate. The zero at uniform `p=1/2` is the known marginal-
visibility boundary, not a weighting preference.

## E_CONTROLS

The primary:

1. reconstructs rather than imports the `Z^3` instance and verdict;
2. pins the sole executable substrate to commit
   `39c74017b870c27c804e3992f2a11e90336476b2`, SHA-256
   `0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4`,
   and Git blob `c123b8d681c3d76fce08ef13d7673622deac64ad`;
3. blocklists prior verdict modules and records that none were loaded;
4. replays a 192-orbit prefix twice and requires exact equality;
5. tests both branches of the requirement selector;
6. accepts a coherent synthetic one-exclusion outcome with a witness; and
7. lands the five-line resolution certificate in its canonical cache.

The independent checker parses the primary AST without importing or executing
it, loads neither Cycle 719 nor a prior cycle, independently reconstructs the
star, all 23 Boolean laws, all 24 rotations, the three orbit certificates, the
five weighting formulas, the per-instance results, the transfer, and the
`|2p-1|` family. It rejects ten active corruptions: coordinate map, program
count, class count, weighting total, survivor count, witnessless exclusion,
transfer headline, non-uniform TV, primary source pin, and cached survivor
headline.

Canonical cached results are:

```text
A_REBUILD_ON_Z3 PASS
B_PER_INSTANCE_TEST PASS
C_TRANSFER_VERDICT PASS
D_INPUT_ROBUSTNESS PASS
E_CONTROLS PASS
TOTAL: PASS=5 FAIL=0

R0_PRIMARY_AST_AND_PINS PASS
R1_INDEPENDENT_Z3_AND_ORBITS PASS
R2_INDEPENDENT_WEIGHTINGS PASS
R3_PER_INSTANCE_AND_TRANSFER PASS
R4_NONUNIFORM_INPUT PASS
R5_RECEIPT_CACHE_BINDING PASS
R6_ACTIVE_CORRUPTION_PROBES PASS
R7_CONTROLS PASS
TOTAL: PASS=8 FAIL=0
```

## Proof-obligation graph

| obligation | disposition | evidence |
|---|---|---|
| rebuild true-`Z^3` support and adjacency | discharged | explicit seven coordinates and six `L1=1` edges |
| exhaust target-local word cap | discharged | all 23 descriptors and 2,944 truth rows |
| recover dependence/covariance structure | discharged | `2/6/12/3` census, 24 rotations, stabilizers `4/2/8`, `J=1/2/0` |
| rebuild five event laws | discharged | 92,260 atoms, 748 per-world rows, five independently recomputed certificate digests |
| select licensed compatibility domain | discharged | zero multi-class instances; injected-coexistence selector control |
| apply the verbatim exclusion criterion | discharged | five event laws, event-marginal identity, variation, closure, and mismatch checks |
| compare with the task's substrate survivor set | discharged | `5/5` on `Z^3`, so `TRANSFERS` |
| test a non-uniform input | discharged | `p=1/4`, TV `1/2` in every class, `5/5` |
| full Born-law derivation | open | finite compatibility supplies no unique weighting or continuous-domain lift |

## Assumptions, imports, and counterfactuals

| item | class | role | counterfactual |
|---|---|---|---|
| true-`Z^3` star | zero-input structural | supplies seven coordinates and six nearest-neighbour conditions | changing adjacency changes the declared instance and requires a new transfer test |
| `{0,1}` basis | explicit finite boundary condition | makes the truth-table family exhaustive | continuous `M_2(C)` measures remain outside this theorem |
| 23 target-local descriptors | explicit finite boundary condition | fixes the complete per-instance program cap | longer words or simultaneous class embeddings can create coexistence and require a new criterion application |
| pinned Cycle-719 substrate | one computed lattice input | rebuilds event histories used by the five laws | a different event substrate can change the weight vectors and must be rebuilt separately |
| uniform neighbour carrier | explicit normalization condition | forms the product extension | a neighbour-correlated carrier is a different law family |
| common `mu_p` on compared branches | explicit normalization condition | isolates Boolean response | a neighbour-conditioned target input changes the intervention and its visibility boundary |

No observed value, fitted selector, literature value, new axiom, new approved
primitive, or prior verdict is load-bearing.

## Honest boundary and next action

The strongest proved statement is the exact finite transfer: on the declared
true-`Z^3` radius-one, word-length-at-most-one basis-state instance, all five
declared finite event weightings pass the verbatim per-instance compatibility
criterion at `p=1/4`, and all three dependence classes reproduce
`TV=|2p-1|` over the sampled exact input family.

The exact remaining obligation is stronger than this target: construct and
classify a full continuous-domain, translation-uniform nearest-neighbour
probability law and a local-to-event/Born lift that actually selects a
weighting. This packet does not approach that obligation by relabeling finite
compatibility as a Born derivation.

## Trace gate and status fields

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "does the five-of-five per-instance Born-compatibility verdict survive when the adjacency is the axiom-native Z3 star?"
source_of_blocker_text: user_goal
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "submit the finite transfer theorem and paired refutation checker to independent audit; do not extrapolate it to a unique Born weighting or infinite-lattice law"
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "exact exhaustive compatibility and transfer theorem on a declared finite true-Z3 target-local family"
conditional_surface_status: "exact on the declared seven-site, 23-program, five-weighting finite family"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
packet_primary_runner: scripts/frontier_cycle984_born_compatibility_z3_adjacency_2026_08_11.py
packet_helper_runner: scripts/frontier_cycle984_born_compatibility_z3_adjacency_independent_check_2026_08_11.py
packet_helper_claim_scope: cycle984_born_compatibility_z3_adjacency
```
