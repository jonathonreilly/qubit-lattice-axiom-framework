# Companion-bank packet-count tensor projections and finite constraint membership

Date: 2026-07-28

Authority: none

Audit: unset

Status: bounded conditional support

**Type:** bounded_theorem

Primary runner:

- [`frontier_companion_bank_packet_count_tensor_projection_constraint_membership_2026_07_28.py`](../scripts/frontier_companion_bank_packet_count_tensor_projection_constraint_membership_2026_07_28.py)

Independent reconstruction:

- [`frontier_companion_bank_packet_count_tensor_projection_independent_check_2026_07_28.py`](../scripts/frontier_companion_bank_packet_count_tensor_projection_independent_check_2026_07_28.py)

Load-bearing packet-schedule predecessor:

- [`COMPANION_BANK_LIVENESS_SCHEDULE_ENDPOINT_INTERVAL_PACKET_PROJECTION_BOUNDED_THEOREM_NOTE_2026-07-28.md`](./COMPANION_BANK_LIVENESS_SCHEDULE_ENDPOINT_INTERVAL_PACKET_PROJECTION_BOUNDED_THEOREM_NOTE_2026-07-28.md)

Imported tensor-fixture dependency:

- [`SIGNED_GRAVITY_ORIENTED_TENSOR_SOURCE_LIFT_NOTE.md`](./SIGNED_GRAVITY_ORIENTED_TENSOR_SOURCE_LIFT_NOTE.md)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

Both dependencies carry authority `none`. The packet predecessor has audit
`unset`, and the tensor-fixture dependency is listed as `unaudited` in the
audit ledger. This dependent calculation is therefore unaudited support and
does not enter the retained chain.

## Result

On the held `2x2x2` box, the landed packet predecessor builds clean Stage-E
schedule extensions for its `primary` and `alternate_port` variants. Each
variant contains 24 declared packet rows and, for each of the five packet
roles, 24 declared Stage-E reads. These are software schedule counts. They are
not register-state values or measurements.

Two explicitly supplied count-to-coordinate conventions give two finite
vectors:

1. The **fixture-scaled convention** assigns the ten declared role-read
   counts to the ten coordinates of the deterministic S1 fixture and
   multiplies coordinate by coordinate. Because every count is 24, the result
   is exactly 24 times the existing fixture. Its residual against the
   existing S1 matrix is approximately `2.44e-14`, below the frozen tolerance
   `1e-9`.
2. The **stage-slot convention** assigns the five primary and five alternate
   Stage-A-through-E slot counts directly to the ten coordinates, producing
   `[225, 9, 112, 17304, 24, 225, 18, 0, 17304, 24]`. This vector is not
   proportional to the S1 fixture, and its residual against the same matrix is
   approximately `1.92e4`, above the frozen tolerance.

The first result is a homogeneous replay by construction, not a new source
feed. The second is one constructed nonmember under an arbitrary declared
coordinate assignment, not a classification of packet projections.

The S1 module calls its deterministic matrix a Ward-like constraint, but its
own implementation constructs a generic seeded `4x10` random matrix. This
note therefore claims membership only in that supplied finite matrix
nullspace. It does not claim that a physical Ward identity has been derived
or tested.

## Exact supplied conventions

The fixture-scaled assignment is:

| S1 coordinate | packet variant | declared Stage-E role-read count |
|---:|---|---|
| 0 | `primary` | `certificate` |
| 1 | `primary` | `binder` |
| 2 | `primary` | `actuality` |
| 3 | `primary` | `admissibility` |
| 4 | `primary` | `law_domain` |
| 5 | `alternate_port` | `certificate` |
| 6 | `alternate_port` | `binder` |
| 7 | `alternate_port` | `actuality` |
| 8 | `alternate_port` | `admissibility` |
| 9 | `alternate_port` | `law_domain` |

If `n_i` is the declared read count and `f_i` is the S1 fixture coordinate,
the projected vector is defined by `v_i = n_i f_i`. This is a definition, not
a derived encoder. On the held schedules every `n_i = 24`.

The stage-slot assignment is:

| S1 coordinate | packet variant | extended-schedule stage |
|---:|---|---|
| 0 | `primary` | A |
| 1 | `primary` | B |
| 2 | `primary` | C |
| 3 | `primary` | D |
| 4 | `primary` | E |
| 5 | `alternate_port` | A |
| 6 | `alternate_port` | B |
| 7 | `alternate_port` | C |
| 8 | `alternate_port` | D |
| 9 | `alternate_port` | E |

Each slot count is used with unit coefficient and no fitting or normalization.
Nothing in the packet predecessor or the S1 dependency selects this
assignment.

## What is inherited and what is recomputed

### Supplied

- the packet predecessor's finite schedule, packet rows, static-predicate
  values, and liveness conventions;
- both count-to-coordinate assignment tables;
- the deterministic S1 fixture and its generic constraint matrix; and
- the numerical nullspace tolerance `1e-9`.

### Derived

- the literal declared-read and extended-schedule slot counts;
- the two vectors under the two supplied assignments;
- exact scalar-multiple and nonproportionality checks; and
- raw finite matrix residual norms for signs `+1`, `-1`, and `0`.

The equal `+1` and `-1` residual norms and zero-vector residual are elementary
linearity checks. They do not add a physical orientation or source theorem.

### Not tested

- register-state readout or a reversible packet encoder;
- an end-to-end composite channel or packet feed to `JointOrder`;
- a physical tensor source, energy/stress law, source law, Ward identity,
  gravity identification, or Born content;
- a derivation selecting either count-to-coordinate convention; or
- a classification or no-go theorem for other packet projections.

“Not tested” records scope. It is not evidence that any route is impossible or
structurally closed.

## Independent reconstruction

The independent runner blocklists the primary module. It parses only the
primary's two literal assignment tables, rebuilds the two landed packet
schedules directly, recounts Stage-E read declarations and stage slots, calls
the existing S1 fixture generator, and evaluates the raw matrix products with
NumPy. It does not call the primary's projection or check functions.

Both runners pin the landed packet and S1 module bytes. A control replaces one
coordinate of the homogeneous vector with the primary Stage-A slot count; the
raw residual changes from the numerical nullspace scale to approximately
`5.43e2`.

## Retention disposition

NatureRetentionReviewer: `BOUNDED_SUPPORT`. The finite arithmetic is
reproducible, but the first arm is algebraically inherited and the second arm
depends on an arbitrary coordinate assignment. The matrix and source
interpretation are imported from an unaudited dependency. No Nature-grade
physical claim is retained.

NoGoDisciplineReviewer: no negative closure survives in this note, so N1-N8
are not invoked as proof of an impossibility result.

## Claim boundary

This bounded theorem is only a conditional two-vector membership comparison
under two supplied projections and one supplied generic matrix. It is not an
epoch-state theorem, packet-to-tensor dataflow theorem, physical source
construction, Ward-law theorem, projection-selection theorem, or no-go
theorem.
