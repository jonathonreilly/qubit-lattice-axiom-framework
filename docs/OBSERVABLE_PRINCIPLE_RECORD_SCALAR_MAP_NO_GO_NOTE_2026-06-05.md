# Observable-Principle Record Scalar Map No-Go

**Date:** 2026-06-05
**Claim type:** no_go
**Runner:** `scripts/frontier_observable_principle_record_scalar_map_no_go_2026_06_05.py`

This note salvages the current-framework core of the record-information route:
Record additivity is now an approved axiom, but it is narrow. Once a finite
scalar record surface is specified, Record says that scalar is additive over
disjoint record collections. It does not identify a Born branch probability,
a determinant modulus, or a log-det expression as that scalar.

The baseline source is
[`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md). In that
language, the relevant question is not whether records are allowed. They are.
The question is whether Record alone derives the map from a multiplicative
branch quantity to the additive scalar record.

## Result

The record scalar route has only two faces.

1. Keep the branch quantity as a Born-style weight `p`. For independent
   branches this is multiplicative: `p_AB = p_A p_B`. Any power family
   `Phi_q(p) = p^q` remains multiplicative and does not become additive.
2. Convert the multiplicative branch quantity into an additive scalar. The
   continuous homomorphism from `(R_+, x)` to `(R, +)` is `c log p`; with the
   information sign this is `-c log p`. That is exactly the P1/additive
   selector being tested, not an independent derivation of it.

Free-monoid record length does not escape the split. Word length is genuinely
additive under concatenation, but the map from a branch of probability `p` to a
word length is either a `-log_b p` coding rule, which reintroduces the log, or a
bare integer count, which is a different quantized observable and is not fixed
by the three axioms.

So Record supports additive scalar readout after the scalar is supplied. It
does not derive the branch-to-scalar map, log-det generator, P1 exponent
selection, Born weight, determinant amplitude, or arbitrary physical-observable
identification.

## Scope

This is a narrow negative statement. It does not say P1 is false, does not
foreclose future owner-approved primitives or admissions, and does not deny that
record additivity is a valid framework axiom. It only rules out this derivation:

```text
Record additivity alone
  => branch probability or determinant modulus is the scalar record
  => the additive scalar must be log-det / P1
```

The missing step is the middle arrow. Record additivity is a rule for an already
specified finite scalar record surface, not a rule that chooses that surface.

## No-Go Discipline Gate

This gate applies only to the route above: deriving the branch-to-scalar map
from Record alone.

### N1 - Alternative Route Enumeration

| Route | What it attempts | Result |
| --- | --- | --- |
| Record axiom route | Use Record additivity to derive the full scalar map. | Narrows to additivity after the scalar is specified. |
| Born branch route | Use the branch weight `p` as the record scalar. | Multiplicative on independent branches, not additive. |
| Power-family route | Use `p^q` or `|Z|^q` as the scalar. | Multiplicative for every `q`; additivity selects the log limit. |
| Free-monoid route | Use mark-count length as the scalar. | Additive on words, but branch-to-word sizing is either `-log p` or a new integer observable. |
| Time-generator route | Use a generator such as `H = -log(T^2)` as the record scalar. | The log coordinate is already inserted. |
| Convention route | Approve the scalar map as a named premise. | Possible governance route, but not a derivation from Record alone. |

### N2 - Wall Independence

The collapsed wall is the branch-to-scalar identification. Additivity of an
already supplied scalar and selection of the scalar are independent. Closing
the first does not close the second.

### N3 - Hidden-Wall Scan

"Record" means finite scalar record additivity only. The note does not smuggle
Born weights, log-det, determinant amplitude, source/action data, or arbitrary
observable identification into the Record axiom.

### N4 - Residual Matching

The residual tested here is exact: multiplicative branch data to additive
scalar record. Prior P1 and flavor notes are only context unless they address
that same residual.

### N5 - Rhetoric Audit

The claim is not a universal no-go against P1 or against records. It is only a
no-go for deriving the branch-to-scalar map from Record additivity alone.

### N6 - Partial-Closure Path Scan

An owner-approved primitive, Tier-A admission, or later derivation could supply
the branch-to-scalar map. The current note leaves those paths open.

### N7 - Steelman

A strong counterargument says that a physical record should count marks, not
probability weights, and that mark count is additive without logarithms. That
does not break this note: it defines a new integer record observable, and the
axioms do not assign a branch of probability `p` to that integer length.

### N8 - Cross-Cycle Echo

Earlier P1 attempts repeatedly split form additivity from physical readout
selection. The current Record axiom retires the finite scalar additivity part,
but it does not retire the readout-selection part.

**Gate result:** pass for the narrow record-scalar-map no-go only.

## Validation

The runner proves the branch facts with exact algebra:

- independent Born-style weights multiply;
- the power family is multiplicative, while the additive coordinate is the log
  limit;
- normalized power readouts are exponent-blind;
- free-monoid length is additive, but assigning probability `1/3` to an integer
  binary length would require `2^n = 3`;
- the current minimal axiom note contains finite scalar record additivity and
  excludes log-det, Born weights, and arbitrary observable identification from
  Record.
