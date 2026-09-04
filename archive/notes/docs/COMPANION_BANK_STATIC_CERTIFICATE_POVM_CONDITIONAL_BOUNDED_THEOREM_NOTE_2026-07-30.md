# Conditional split/merge POVMs for supplied companion-bank static-certificate inputs

Date: 2026-07-30

Authority: none

Audit: unset

Status: bounded conditional construction

Claim type: bounded_theorem

Primary runner:

- [`frontier_companion_bank_static_certificate_povm_input_acceptance_2026_07_30.py`](../scripts/frontier_companion_bank_static_certificate_povm_input_acceptance_2026_07_30.py)

Independent reconstruction:

- [`frontier_companion_bank_static_certificate_povm_independent_check_2026_07_30.py`](../scripts/frontier_companion_bank_static_certificate_povm_independent_check_2026_07_30.py)

Load-bearing sources:

- [`COMPANION_BANK_LIVENESS_SCHEDULE_ENDPOINT_INTERVAL_PACKET_PROJECTION_BOUNDED_THEOREM_NOTE_2026-07-28.md`](./COMPANION_BANK_LIVENESS_SCHEDULE_ENDPOINT_INTERVAL_PACKET_PROJECTION_BOUNDED_THEOREM_NOTE_2026-07-28.md)
- [`PHYSICAL_CONTACT_TERNARY_BORN_FORCING_BRIDGE_CYCLE317_NOTE_2026-07-18.md`](./work_history/repo/review_feedback/PHYSICAL_CONTACT_TERNARY_BORN_FORCING_BRIDGE_CYCLE317_NOTE_2026-07-18.md)
- [`COMPANION_BANK_STATIC_CERTIFICATE_POVM_INPUT_CONVENTION_META_NOTE_2026-07-30.md`](./COMPANION_BANK_STATIC_CERTIFICATE_POVM_INPUT_CONVENTION_META_NOTE_2026-07-30.md)

Constitutional effect: none. This package changes no axiom, primitive,
registry, policy, audit result, or audit status. Its sources have authority
`none`; this dependent result is likewise unaudited and does not enter the
retained chain without independent audit.

## Result

For the exact finite arrays and every supplied association listed in the
convention note, the landed Cycle-317 split and merge constructors produce
normalized positive effect-valued measures (POVMs).

The first supplied array gives

```text
n = (1,1,1)/sqrt(3),
P(n) = (I + n_x X + n_y Y + n_z Z)/2,
U = diag(exp(0.37 i), 1),
s = (17/100, 29/100, 27/50).
```

For `j=1,2,3`, set `K_j = sqrt(s_j) P U`, and set
`K_4 = (I-P)U`. Since `sum_j s_j = 1`,

```text
sum_j K_j* K_j = U* ((sum_j s_j) P + I - P) U = I.
```

The four effects have spectra `{0,0.17}`, `{0,0.29}`, `{0,0.54}`, and
`{0,1}`.

The second supplied array reduces exactly to

```text
w = (25/86, 41/172, 45/172, 9/43),  sum_i w_i = 1.
```

Pair it positionally with
`n_1=(1,2,3)/sqrt(14)`, `n_2=-x`, `n_3=-y`, and `n_4=-z`.
For each `i`, set

```text
K_i+ = sqrt(w_i) P(n_i) U,
K_i- = sqrt(w_i) (I-P(n_i)) U.
```

Then

```text
sum_i ((K_i+)* K_i+ + (K_i-)* K_i-) = I.
```

Grouping the four plus labels gives a positive effect whose Bloch vector is

```text
m = ((50/sqrt(14)-41)/172,
     (100/sqrt(14)-45)/172,
     (150/sqrt(14)-36)/172).
```

Its norm is `sqrt(7502-23900/sqrt(14))/172`, approximately
`0.1940899635475093`, so the grouped plus-effect eigenvalues are
`(1-|m|)/2` and `(1+|m|)/2`, approximately
`0.40295501822624535` and `0.5970449817737546`.

## Numerical evidence

The primary runner reports the following quantities separately:

| construction | isometry residual | POVM-normalization residual |
|---|---:|---:|
| split | `2.4999285328858064e-16` | `2.220446049250313e-16` |
| merge | `0.0` | `3.1463121132764933e-16` |

The independent runner reimplements the Pauli projectors, Kraus blocks,
isometry stacks, coarse-graining, spectra, and exact rational reductions. It
does not import the primary runner or Cycle-317 module. It runs the primary as
a black box only after computing its own result.

Valid-domain controls show that a sign flip changes the split projector and a
reversed coefficient/projector pairing changes the merge plus effect even
though both mutated constructions remain lawful POVMs. All three-of-five
source-field selections return the same normalized vector because every field
count is 48. These controls confirm that the conditional algebra is valid
while the source does not determine the supplied mappings.

## Proof-obligation graph

```text
landed static-predicate totals
  + supplied field selection/order/sign/pooling/normalization
      -> one supplied unit Bloch direction
  + supplied split simplex and contact
      -> split isometry and four-effect POVM

landed liveness destination counts
  + supplied stage order and sum normalization
  + supplied projector directions, pairing, and contact
      -> merge isometry and five-effect POVM
```

Every association above is an explicit condition. There is no proof edge from
an equality of unrelated integers to either matrix identity, so the earlier
integer “binding” table and its receipt are not part of this salvage.

## Claim boundary

This is a finite conditional algebraic lemma. It is not a register-state
readout, dataflow theorem, source-derived apparatus program, physical
occurrence rule, actual-member selection, Record-formation law, realized
history, probability-law selection, repeated-process theorem, or empirical
calibration.

The existing
[`BORN_ACCEPTANCE_HARNESS_SUPPORT_NOTE_2026-07-28.md`](./BORN_ACCEPTANCE_HARNESS_SUPPORT_NOTE_2026-07-28.md)
covers only supplied Bloch-projector fixtures. This package adds narrow
candidate-input coverage for the split and merge constructors; it is not a
standing or canonical acceptance surface. Dilation, trace-functional, release,
and end-to-end physical-program coverage remain outside this result.

“Outside this result” is a scope statement, not a no-go or an assertion that
another route is unavailable.

## Reproduction

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=scripts \
  python3 scripts/frontier_companion_bank_static_certificate_povm_input_acceptance_2026_07_30.py

PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=scripts \
  python3 scripts/frontier_companion_bank_static_certificate_povm_independent_check_2026_07_30.py
```

The paired canonical runner-cache logs are reproducibility aids only. No
claim-status receipt or self-certificate is part of this package.
