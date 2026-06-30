# AC_phi_lambda r=1/2 From Durable Two-Outcome Record Idempotence

**Date:** 2026-06-30
**Claim type:** positive theorem candidate / conditional bridge theorem.
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit the Tier-A registry, register a primitive, refresh generated
ledgers, derive record occurrence, or claim AC_phi_lambda retirement.
**Primary runner:**
[`scripts/acphilambda_r_half_durable_record_idempotence_bridge_2026_06_30.py`](../scripts/acphilambda_r_half_durable_record_idempotence_bridge_2026_06_30.py)

## Claim

On the #4747 axiom surface, the right `r = 1/2` theorem is not a universal law
for every site or every sector. It is a finite record theorem:

```text
For an already-present finite record context, repeated readout must leave the
record content invariant. If repeated readout is represented by agreement
composition of the same scalar record readout, then durable records are exactly
the fixed points of that agreement-composition map.
```

For normalized nonnegative scalar readout weights `w_i` on the active outcome
support,

```text
    w_i -> w_i^2 / sum_j w_j^2.
```

The fixed points with unchanged active support are uniform on that active
support. Therefore a durable two-active-outcome record has equal record weights.

In the charged-lepton two-outcome context, with singlet outcome `s` and
doublet-orbit outcome `d`,

```text
    x = w_d / w_s = 1.
```

The charged-lepton dictionary is `x = 2r`, so the durable recorded value is:

```text
    r = 1/2,        Q = 1/3 + (2/3)r = 2/3.
```

This is the force we want: not "everything records `r = 1/2`," but "a durable
charged-lepton two-outcome record reads `r = 1/2`."

## Relation To The New Axioms

The current axiom set supplies exactly the pieces this theorem is allowed to
use:

- **Record:** a record locks one available local possibility, invariant under
  repeated readout; only records are readable.
- **Qubit/Admissibility/Lattice:** the local possibility and admissibility
  substrate, without supplying a probability rule or record-production process.
- **Qualification:** further physical structure requires derivation, bridge,
  explicit admission, or approved primitive registration.

Agreement composition is the bridge content here. It is not a probability law,
Born rule, measurement context selector, or occurrence rule. It is the finite
record-readout consistency condition that two readings of the same context,
conditioned on agreement, must not change a durable record's active readout
content.

## The Finite Theorem

Let `A` be the active support of a finite record readout context. Let

```text
    w_i > 0,    sum_{i in A} w_i = 1
```

be its normalized scalar readout weights on that active support. The agreement
composition map is

```text
    F(w)_i = w_i^2 / S,       S = sum_{j in A} w_j^2.
```

If the record is durable under this repeated-readout composition, then

```text
    F(w)_i = w_i       for all i in A.
```

For every active `i`, this gives:

```text
    w_i = w_i^2 / S.
```

Since `w_i > 0`, divide by `w_i`:

```text
    w_i = S.
```

So all active weights are equal. If `|A| = n`, normalization gives:

```text
    w_i = 1/n.
```

Thus:

- one active outcome gives a one-outcome durable record;
- two active outcomes give equal weights `(1/2, 1/2)`;
- three active outcomes give `(1/3, 1/3, 1/3)`;
- no active outcome is impossible.

The theorem forces uniformity **on the active support only**. It does not force
which support is active, whether a record occurs, or which physical context is
being read.

## Charged-Lepton Consequence

The charged-lepton record context uses two active readable outcomes:

```text
    s = singlet outcome
    d = doublet K-orbit outcome
```

Durability under agreement composition gives:

```text
    w_s = w_d = 1/2,
    x = w_d / w_s = 1.
```

The charged-lepton dictionary is:

```text
    x = 2r.
```

Therefore:

```text
    r = 1/2.
```

Using the retained Koide-block lever:

```text
    Q = 1/3 + (2/3)r = 2/3.
```

## What This Closes, If Retained

This closes the `r` atom only in the following conditional sense:

```text
#4747 axioms
  + #4748 strict nearest-neighbor composition
  + charged-lepton two-active-outcome record context
  + charged-lepton dictionary x = 2r
  + agreement-composition reading of repeated scalar record readout
  -> durable record fixed point x = 1
  -> r = 1/2
```

It removes the need for a global `r = 1/2` law. It also removes the need to say
all sites are recorded. The theorem starts after a finite record context exists.

## What Remains Outside This Theorem

- Record occurrence and record-production dynamics.
- Selection of the charged-lepton readout context.
- The physical species bridge.
- `A_R-eta`.
- Theta.
- Born weights, probability, and measurement semantics.
- A proof that every sector uses the charged-lepton two-outcome dictionary.
- Any global exclusion of valid one-outcome, three-outcome, or sector-cell
  records in other contexts.

## Why This Does Not Over-Freeze The World

The active-support clause is load-bearing. A one-active-outcome record is durable
without being `r = 1/2`. A different context with a different dictionary can be
durable at a different cell. A site with no record is not constrained by this
theorem at all.

So the theorem is compatible with sparse records:

```text
not every site records;
not every context records;
not every durable record has two active charged-lepton outcomes;
but if this charged-lepton two-outcome record is durable, its recorded ratio is
r = 1/2.
```

## No-Go Discipline Gate

**Status:** PASS for the narrow negative boundaries only. The positive theorem
is the finite fixed-point classification above. The negative boundaries are:
no universal `r = 1/2` law, no record occurrence theorem, and no closure of the
other AC_phi_lambda atoms.

### N1 - Alternative Route Enumeration

| Route | Marker | Result |
|---|---|---|
| Universal `r = 1/2` forcing | ATTEMPTED by scope analysis | Rejected as too strong; valid supports and other contexts remain. |
| Static polarization | RULED OUT BY PRIOR for full closure | Prior static routes do not select the readout horn. |
| Dirac kinetic branch | PARTIAL via #4748 | Supplies first-order kinetic order but not record-context idempotence. |
| First-order determinant | PARTIAL by existing staggered determinant note | Supplies count-once surface but leaves horn/context open. |
| Durable agreement composition | ATTEMPTED here | Succeeds conditionally: active-support fixed points are uniform. |
| Realized-state registration | RULED OUT BY PRIOR as exactness explanation | Classifies values as registered data but does not explain durable exactness. |

### N2 - Wall Independence

The collapsed residual set after this theorem is:

```text
W_context = why the charged-lepton readout context is the physical one
W_eta     = A_R-eta
W_species = physical species/locus bridge
```

The agreement-composition theorem does not supply those residuals, and closing
any one of them does not automatically close the others.

### N3 - Hidden-Wall Scan

"Agreement composition" is named bridge content, not smuggled axiom content.
"Active support" is explicit. "Scalar record weights" are normalized record
readout weights in a finite context, not Born probabilities. "Charged-lepton
dictionary" is supplied downstream context, not generic Record content.

### N4 - Residual Matching

| Witness | Residual there | Residual here | Match |
|---|---|---|---|
| `ACPHILAMBDA_R_HALF_RECORDED_VALUE_TARGET...` | exact target was durable recorded value, not global forcing | same target, now theorem-shaped | yes |
| `OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY...` | fixed outcome ratio needs a dictionary to read as `r` | dictionary consumed explicitly | yes |
| `KOIDE_R_HALF_DURABILITY_STATIONARITY...` | R-D + side conditions gives unique durable `r = 1/2` | finite fixed-point core isolated here | yes |
| `OCCUPANCY_NONEXCLUSIVITY...` | no global exclusion of `r = 1` | active-support boundary preserves this | yes |
| `ACPHILAMBDA_POST_DIRAC_REDUCTION_MAP...` | next atom was `r = 1/2` signed/statistics readout | theorem attacks that atom only | yes |

### N5 - Rhetoric Audit

The theorem says "two-active-outcome durable charged-lepton record," not
"the framework derives every `r`" and not "all sites record." The word
"force" is used only inside the stated conditional.

### N6 - Partial-Closure Path Scan

If retained, this note is an import-retirement path for the `r` exactness atom
inside the charged-lepton context. It does not require adding a new axiom. If
review rejects agreement composition as bridge content, the exact remaining
input is the named agreement-composition bridge, not a broad Dynamics axiom.

### N7 - Steelman

A hostile reviewer can object that the theorem still depends on the
charged-lepton two-outcome context and the dictionary `x = 2r`; therefore it
does not retire all of AC_phi_lambda. Correct. This theorem only closes the
conditional recorded-value step after that context is supplied.

### N8 - Cross-Cycle Echo

Prior cycles failed when they tried to extract a global occupancy rule from
Record, static polarization, or generic dynamics. This theorem uses the narrower
record-local shape that survived those failures: a durable existing record must
be fixed under repeated readout.

## Verification

Run:

```bash
python3 scripts/acphilambda_r_half_durable_record_idempotence_bridge_2026_06_30.py
```

Expected close:

```text
TOTAL: PASS=66 FAIL=0
```
