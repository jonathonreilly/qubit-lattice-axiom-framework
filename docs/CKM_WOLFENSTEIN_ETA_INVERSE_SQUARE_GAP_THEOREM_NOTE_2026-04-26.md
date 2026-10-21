# CKM Wolfenstein `eta^2` Inverse-Square Structural Reading Theorem

**Date:** 2026-04-26

**Claim type:** bounded_theorem
**Status:** conditional supplied-value algebra; no independent CP mechanism

**Primary runner:** `scripts/frontier_ckm_wolfenstein_eta_inverse_square_gap.py`

## Claim

Given the supplied counts and CKM value

```text
eta^2 = 5/36
```

admits a new exact structural reading from the same quark-doublet source that
now grounds `A^2` below `W2`:

```text
(W1)  eta^2
    = 1/N_pair^2 - 1/N_color^2
    = 1/(dim_SU2(Q_L))^2 - 1/(dim_SU3(Q_L))^2
    = 1/4 - 1/9
    = 5/36.
```

Here `N_pair = 2` and `N_color = 3` are read directly from the supplied
matter-content literal

```text
Q_L : (2,3)_{+1/3}.
```

This is a **new supplied structural reading** of the already-supplied CKM
parameter `eta^2`. It is **not** a below-`Wn` closure claim and it does **not**
promote any non-main authority.

## Additional Exact Identities

The same supplied package gives five companion algebraic identities:

```text
(W2)  rho A^2 = 1/N_color^2 = 1/9

(W3)  eta^2 + rho A^2 = 1/N_pair^2 = 1/4

(W4)  eta^2 + 2 rho A^2 = 1/N_pair^2 + 1/N_color^2 = 13/36

(W5)  rho = 1/(N_pair N_color) = 1/6

(W6)  eta^2 = (N_color^2 - N_pair^2)/N_quark^2 = 5/36.
```

The theorem packages these as CKM-side structural readouts on the supplied
source surface. In particular:

- `W2` is an exact factorization of supplied `rho` and supplied `A^2`; it is
  **not** an SM-uniqueness theorem.
- `W1`, `W3`, `W4`, and `W6` are exact supplied-value identities at the
  sourced `Q_L:(2,3)` counts.

## Structural Interpretation

The formula is an algebraic interpretation of the supplied eta^2 value using two supplied dimensions. It neither derives those dimensions as physical representations nor explains CP violation dynamically:

```text
eta^2
= 1/(SU(2)_L doublet dimension)^2
  - 1/(SU(3)_c triplet dimension)^2.
```

Equivalently, the CKM CP-phase package may now be read as

```text
rho      = 1/(N_pair N_color),
eta^2    = 1/N_pair^2 - 1/N_color^2,
rho A^2  = 1/N_color^2,
```

so that `rho`, `eta^2`, and `rho A^2` split naturally into factorizations over
the same sourced structural integers `(N_pair, N_color) = (2,3)`.

## Supplied Inputs

| input | authority on `main` | role |
| --- | --- | --- |
| `Q_L:(2,3)_{+1/3}` | [`LEFT_HANDED_CHARGE_MATCHING_NOTE.md`](LEFT_HANDED_CHARGE_MATCHING_NOTE.md) | supplied source literal fixing `N_pair=2`, `N_color=3` |
| `u_R:(1,3)`, `d_R:(1,3)` | [`ONE_GENERATION_MATTER_CLOSURE_NOTE.md`](ONE_GENERATION_MATTER_CLOSURE_NOTE.md) | same-sector color cross-check |
| below-`W2` quark-doublet source theorem | [`CKM_A_SQUARED_BELOW_W2_Y_QUANTUM_CLOSURE_THEOREM_NOTE_2026-04-25.md`](CKM_A_SQUARED_BELOW_W2_Y_QUANTUM_CLOSURE_THEOREM_NOTE_2026-04-25.md) | mainline source theorem reusing the same supplied literal |
| `A^2 = N_pair/N_color = 2/3` | [`WOLFENSTEIN_LAMBDA_A_STRUCTURAL_IDENTITIES_THEOREM_NOTE_2026-04-24.md`](WOLFENSTEIN_LAMBDA_A_STRUCTURAL_IDENTITIES_THEOREM_NOTE_2026-04-24.md) | supplied Wolfenstein count ratio |
| `rho = 1/N_quark`, `eta^2 = (N_quark-1)/N_quark^2` | [`CKM_CP_PHASE_STRUCTURAL_IDENTITY_THEOREM_NOTE_2026-04-24.md`](CKM_CP_PHASE_STRUCTURAL_IDENTITY_THEOREM_NOTE_2026-04-24.md) | supplied CKM CP-phase package |
| `N_quark = N_pair N_color = 6` | [`CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md`](CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md) | supplied structural counts |
| Bernoulli-family comparator | `CKM_MULTI_PROJECTION_BERNOULLI_FAMILY_THEOREM_NOTE_2026-04-25.md` | consistency cross-check only |

The needed numerical/model premises are displayed explicitly. This note does not establish their physical selection or current audit authority.

## Derivation

From the supplied source literal `Q_L:(2,3)_{+1/3}`:

```text
N_pair  = 2,
N_color = 3,
N_quark = N_pair N_color = 6.
```

From the supplied CKM package:

```text
A^2   = N_pair/N_color = 2/3,
rho   = 1/N_quark = 1/6,
eta^2 = (N_quark - 1)/N_quark^2 = 5/36.
```

Then:

```text
1/N_pair^2 - 1/N_color^2
= 1/4 - 1/9
= 5/36
= eta^2,
```

which is `(W1)`.

Also:

```text
rho A^2
= (1/N_quark)(N_pair/N_color)
= (1/(N_pair N_color))(N_pair/N_color)
= 1/N_color^2,
```

which is `(W2)`.

Then:

```text
eta^2 + rho A^2
= (1/N_pair^2 - 1/N_color^2) + 1/N_color^2
= 1/N_pair^2,
```

giving `(W3)`, and

```text
eta^2 + 2 rho A^2
= (1/N_pair^2 - 1/N_color^2) + 2/N_color^2
= 1/N_pair^2 + 1/N_color^2,
```

giving `(W4)`.

Finally,

```text
eta^2
= 5/36
= (9 - 4)/36
= (N_color^2 - N_pair^2)/N_quark^2,
```

which is `(W6)` at the supplied sourced values.

## Comparator and Scope

This theorem is deliberately narrow.

It does:

- add a new supplied structural reading of `eta^2`,
- package exact companion identities `W2`-`W6`,
- cross-check compatibility with the supplied Bernoulli-family reading
  `eta^2 = V(N_pair) M(N_color) M(N_quark)`.

It does not:

- claim a new below-`Wn` closure,
- claim `rho A^2 = 1/N_color^2` is SM-unique,
- rely on any unmerged or support-only theorem to carry the derivation.

## Science Value

The supplied CKM value `eta^2 = 5/36` already had two exact structural
packagings on `main`:

```text
eta^2 = (N_quark - 1)/N_quark^2,
eta^2 = V(N_pair) M(N_color) M(N_quark).
```

This theorem adds a third:

```text
eta^2 = 1/N_pair^2 - 1/N_color^2.
```

This is another rewriting at the same supplied `(2,3)` counts, not independent corroboration of a physical CP mechanism. It also exposes
the exact sum identities `W3` and `W4`, which were not previously packaged on
`main`.

## Verification

The runner:

- extracts `Q_L:(2,3)` by regex from disk,
- displays documentary source-status labels and checks canonical `effective_status`
  values from the seven tracked rows under `docs/audit/data/ledger/`, using
  the repository ledger API to locate them; these ledger values provide
  audit provenance, not mathematical proof,
- derives `W1`-`W6` by exact `Fraction` arithmetic,
- cross-checks Bernoulli compatibility,
- audits that `W2` is a generic factorization on the count surface rather than
  an SM-uniqueness statement.

## Live-runner changelog (2026-09-03 densify repair H1)

A 2026-09-01 live re-run of the primary runner reports `FAIL=7`. All seven
failures are **retained-tier status pins** checked against the epoch-reset
(wholly unaudited) ledger; every exact-arithmetic science check passes. This
note asserts no expected PASS/FAIL scorecard, so nothing here is stale; this
line records the live result and its diagnosis so a future reader does not
mistake tier pins for science failures. Re-pinning the tier checks to the live
ledger is audit-lane work.
