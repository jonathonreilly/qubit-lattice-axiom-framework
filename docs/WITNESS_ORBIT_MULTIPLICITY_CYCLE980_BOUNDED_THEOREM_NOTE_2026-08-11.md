# Witness-orbit multiplicity bounded theorem

Date: 2026-08-11  
Cycle: 980  
Claim type: `bounded_theorem`  
Audit-status authority: independent audit lane only  
Effective status: pipeline-derived only after independent audit ratification and dependency closure

```yaml
claim_id: cycle980_witness_orbit_multiplicity
claim_type: bounded_theorem
actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "finite alphabet/support theorem; no branch-local retained-grade proposal"
audit_required_before_effective_retained: true
bare_retained_allowed: false
audit_status_authority: independent audit lane only
target_claim_id: null
target_blocker_text: "derive the 6/12/3 multiplicities and determine why exactly three classes occur"
source_of_blocker_text: user_goal
artifact_role: theorem
next_trace_action: "independent audit of the bounded theorem packet"
negative_assertion_classes: []
packet_primary_runner: scripts/frontier_cycle980_witness_orbit_multiplicity_2026_08_11.py
packet_helper_runner: scripts/frontier_cycle980_witness_orbit_multiplicity_independent_check_2026_08_11.py
packet_helper_claim_scope: cycle980_witness_orbit_multiplicity
```

## Claim

For the declared target-centred, radius-one, word-length-zero-or-one family
over the landed basis-state gate alphabet `{I, X, CNOT, TOF}`, the 21 words
whose target output varies with a neighbour bit form exactly three orbits of
the effective proper-cubic action:

| orbit | members | effective stabilizer | orbit-stabilizer check |
|---|---:|---:|---:|
| CNOT | 6 | 4 | `6 * 4 = 24` |
| perpendicular-control TOF | 12 | 2 | `12 * 2 = 24` |
| opposite-control TOF | 3 | 8 | `3 * 8 = 24` |

Thus `6 + 12 + 3 = 21` is an orbit decomposition, not merely a numerical
coincidence. The theorem is bounded to the finite family below. It does not
say that every admissibility realization has three classes.

## Declared family and cap

- Spatial support: the centre `C` and its six nearest neighbours
  `+x,-x,+y,-y,+z,-z`.
- Local site menu: `{0,1}`.
- Words: the identity or one landed gate.
- Operands: distinct wires; CNOT control and target are ordered; TOF controls
  are unordered; there is no within-star adjacency restriction.
- Gate counts: `1 I + 7 X + 7*6 CNOT + 7*C(6,2) TOF = 155`.
- Evaluation cap: all 155 words, both target inputs, all `2^6` neighbour
  conditions, and every neighbour-bit edge comparison. There is no sampling.
- Symmetry cap: translations and all 24 proper cubic rotations supplied by
  the [`Z^3` lattice axiom](MINIMAL_AXIOMS_2026-06-29.md).

The executable gate meanings come from the immutable Cycle-719 source at
commit `39c74017b870c27c804e3992f2a11e90336476b2`, path
[`frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py`](../scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py),
SHA-256
`0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4`.
The primary loads that source from an immutable Git archive and checks every
landed target truth table against a separate descriptor-level Boolean rule.

No observed value, fitted parameter, probability rule, normalization rule,
new axiom, or new framework primitive enters the calculation.

## Imports

| input | import class | load-bearing role |
|---|---|---|
| `minimal_axioms` | framework-derived | supplies the `Z^3` lattice, translations, nearest-neighbour star, and proper cubic rotations |
| pinned Cycle-719 core | one computed lattice input | supplies executable X/CNOT/TOF basis-state semantics; commit, path, SHA-256, and Git blob are checked |
| 155-word family declaration | explicit finite boundary condition | fixes the alphabet, support, operand ordering, and word-length cap proved here |

Observed targets, fitted selectors, literature values, normalization
conventions, and probability weights have no load-bearing role.

## What was tested rather than assumed

The suggestive orbit-size interpretation was treated as a candidate. The
primary first derives the witness set from the landed truth tables. It then:

1. constructs all orientation-preserving signed permutation matrices;
2. verifies identity, closure, inverses, and determinant `+1`;
3. applies every resulting rotation to every derived witness descriptor;
4. computes ambient orbits and descriptor stabilizers;
5. tests closure on the witness set, disjoint coverage, and the
   orbit-stabilizer products; and
6. separately computes the proposed invariant and the full alphabet-subset
   census.

The integrity gates certify that these measurements reconcile. They do not
require three orbits, closure on the witness set, or a separating invariant.
A null, non-closed, merged, or enlarged outcome would therefore remain a
cleanly reportable result.

## Why there are 21 witnesses

Let `x` be the centre input and let `n_d` be the neighbour bit at signed-axis
direction `d`.

An identity word leaves `x` unchanged. An X gate either flips `x`
independently of all neighbours or acts away from the centre. Neither is a
neighbour-dependence witness.

A CNOT changes the centre output only when its target is `C`. Its control must
then be one of the six distinct neighbour wires, giving

```text
x' = x XOR n_d,                     d in {+x,-x,+y,-y,+z,-z}.
```

There are therefore six CNOT witnesses.

A TOF changes the centre output only when its target is `C`. Its two distinct,
unordered controls must then be chosen from the six neighbours, giving

```text
x' = x XOR (n_a AND n_b),           {a,b} subset of the six directions.
```

There are `C(6,2)=15` TOF witnesses. Two distinct signed coordinate vectors
have dot product either `0` or `-1`:

- Perpendicular: choose two of the three coordinate axes and one sign on
  each, giving `C(3,2)*2*2 = 12` pairs.
- Opposite: choose one of the three axes and take both signs, giving `3`
  pairs.

No other member of the 155-word family can alter the centre through a
neighbour bit. Hence the witness count is `6 + 12 + 3 = 21` before any orbit
interpretation is imposed.

## Exact group action

The ambient realized symmetry is `Z^3 semidirect O+_cubic`. Witness data are
stored as centre-relative descriptors. Translating the centre and every gate
operand by the same lattice vector and then recentering returns the identical
descriptor. Consequently the translation subgroup `Z^3` is the kernel on
this finite witness data, and the effective action is the quotient
`O+_cubic`, of order 24.

For a proper cubic rotation `R`, the action is

```text
R . CNOT(c -> C)       = CNOT(Rc -> C),
R . TOF({a,b} -> C)    = TOF({Ra,Rb} -> C).
```

The exhaustive action is closed on all 21 derived witnesses and gives:

- A signed direction is transitive under `O+_cubic`. The stabilizer of `+x`
  comprises the four quarter-turns about that oriented axis. Therefore the
  CNOT orbit has size `24/4 = 6`.
- An unordered perpendicular pair such as `{+x,+y}` has a two-element
  setwise stabilizer. Therefore its TOF orbit has size `24/2 = 12`.
- An unordered opposite pair such as `{+x,-x}` is an unoriented coordinate
  axis. Its setwise stabilizer has eight elements. Therefore its TOF orbit has
  size `24/8 = 3`.

The computation enumerates each stabilizer rather than inserting these
orders as expected constants.

## Exact invariant separator

For any derived witness word `w`, let `c_i` be the centre-relative displacement
vector of its controls and define

```text
J(w) = || sum_i c_i ||^2.
```

This is integer-valued and computable directly from a word descriptor. A
proper cubic rotation preserves vector addition and Euclidean norm, while a
translation cancels on recentering, so `J` is invariant under the effective
action.

| orbit | control arity | off-diagonal control Gram entries | `J` |
|---|---:|---:|---:|
| CNOT | 1 | empty | 1 |
| perpendicular-control TOF | 2 | `{0}` | 2 |
| opposite-control TOF | 2 | `{-1}` | 0 |

The exhaustive result verifies that `J` is constant on each orbit and that
its three values are distinct. Thus `J` alone separates the three classes;
the fuller pair `(control arity, control Gram multiset)` records the same
control geometry without compression.

## Is three forced?

Three is forced only after fixing the full declared alphabet and support
rules. It is not forced by proper cubic covariance alone. The runner
exhaustively repeats the witness/orbit calculation for all eight subsets of
the landed gate menu, with identity always present:

| landed alphabet | orbit count |
|---|---:|
| `{I}` | 0 |
| `{I,X}` | 0 |
| `{I,CNOT}` | 1 |
| `{I,TOF}` | 2 |
| `{I,X,CNOT}` | 1 |
| `{I,X,TOF}` | 2 |
| `{I,CNOT,TOF}` | 3 |
| `{I,X,CNOT,TOF}` | 3 |

Adding X never changes the count because X has no neighbour-dependent centre
law in a one-gate word. Adding CNOT contributes the single signed-direction
orbit. Adding TOF contributes the two unordered-pair geometry orbits. The
full landed one-gate alphabet has no further primitive gate kind to add.

Therefore “exactly three” is a theorem of the full 155-word alphabetic family,
but an artifact of choosing that alphabet when read as a statement about
arbitrary landed subfamilies.

## Falsifiers and scope boundary

This bounded theorem is false if any of the following occurs under the
declared computation:

- a derived witness lies outside the stated 21 descriptors;
- proper cubic transport is not closed on the derived witness set;
- any reported orbit has an overlap or omission;
- an orbit size times its enumerated stabilizer order differs from 24;
- `J` changes within a reported orbit or is shared by two reported orbits; or
- an alphabet-subset row fails its independently reconstructed census.

The result classifies Boolean target-output dependence for this one-gate,
seven-site family. It does not derive a probability law, Born weights,
measurement dynamics, a general multi-gate classification, or an alphabet
beyond the landed X/CNOT/TOF constructors.

## Artifacts and reproduction

Primary:

- [`frontier_cycle980_witness_orbit_multiplicity_2026_08_11.py`](../scripts/frontier_cycle980_witness_orbit_multiplicity_2026_08_11.py)
- [`witness_orbit_multiplicity_cycle980_receipt_2026_08_11.json`](../outputs/witness_orbit_multiplicity_cycle980_receipt_2026_08_11.json)
- [`frontier_cycle980_witness_orbit_multiplicity_2026_08_11.txt`](../logs/runner-cache/frontier_cycle980_witness_orbit_multiplicity_2026_08_11.txt)

Independent refutation checker:

- [`frontier_cycle980_witness_orbit_multiplicity_independent_check_2026_08_11.py`](../scripts/frontier_cycle980_witness_orbit_multiplicity_independent_check_2026_08_11.py)
- [`witness_orbit_multiplicity_cycle980_independent_check_receipt_2026_08_11.json`](../outputs/witness_orbit_multiplicity_cycle980_independent_check_receipt_2026_08_11.json)
- [`frontier_cycle980_witness_orbit_multiplicity_independent_check_2026_08_11.txt`](../logs/runner-cache/frontier_cycle980_witness_orbit_multiplicity_independent_check_2026_08_11.txt)

```bash
python3 scripts/cached_runner_output.py --refresh --timeout-sec 1400 scripts/frontier_cycle980_witness_orbit_multiplicity_2026_08_11.py
python3 scripts/cached_runner_output.py --refresh --timeout-sec 300 scripts/frontier_cycle980_witness_orbit_multiplicity_independent_check_2026_08_11.py
```

The checker imports and executes neither the primary nor Cycle-719. It parses
the primary as text/AST, independently rebuilds the Boolean family using a
different signed-permutation representation, binds primary source/receipt/cache
identities and stdout, and rejects eight declared corruptions targeting witness
membership, orbit size, stabilizer order, invariant separation, translation
kernel, alphabet sensitivity, and the cache headline.

Both runners use literal `AUDIT_INPUT_PATHS`, enforce text and AST provenance
blocklists, replay deterministically, run below 1400 seconds, keep stdout below
6000 bytes (and therefore below 150 KB), and end with `TOTAL: ... FAIL=0` only
when all bookkeeping controls pass. The runners write receipts; the canonical
`scripts/runner_cache.py` path, invoked through `cached_runner_output.py`, owns
cache envelope creation and records the actual process exit status and elapsed
time.
