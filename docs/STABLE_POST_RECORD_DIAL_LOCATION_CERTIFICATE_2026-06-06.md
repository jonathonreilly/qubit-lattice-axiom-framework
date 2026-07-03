# Stable Post-Record Dial Location Certificate

**Date:** 2026-06-06
**Claim type:** bounded_theorem
**Status:** exact-support branch-local stable-location certificate; not a
dial-selection theorem, not a Koide closure, and not an audit verdict.
**Primary runner:**
[`scripts/frontier_stable_post_record_dial_location_certificate_2026_06_06.py`](../scripts/frontier_stable_post_record_dial_location_certificate_2026_06_06.py)
**Runner output:**
[`logs/runner-cache/frontier_stable_post_record_dial_location_certificate_2026_06_06.txt`](../logs/runner-cache/frontier_stable_post_record_dial_location_certificate_2026_06_06.txt)

## Purpose

This certificate records the safe dial statement unlocked by the Record
dynamics stack:

```text
s = 0, r = 1/2, Q = 2/3
```

is a stable post-record equal-letter location on the two-atom record surface.
It is not forced by the Record axiom, not selected by post-record count
dynamics, and not a physical dial-value theorem.

The distinction matters because downstream flavor/Koide rows need a stable
place on the dial, not a forced value.

## Certified Statement

For the two-record alphabet with target

```text
u = (1/2, 1/2),
```

the atom-symmetric reset map

```text
Phi_alpha(p) = (1 - alpha) p + alpha u,     0 < alpha < 1
```

has `u` as a stationary attracting fixed point:

```text
Phi_alpha(p) - u = (1 - alpha)(p - u).
```

Using the supplied generation dial

```text
pi_s = (1/(1 + 2^s), 2^s/(1 + 2^s)),
r(s) = 2^(s - 1),
Q(s) = 1/3 + (2/3) r(s),
```

the equal-letter target is exactly

```text
s = 0, r = 1/2, Q = 2/3.
```

This is a stable location certificate.

## Why It Does Not Force The Dial

The same reset construction works for every fixed dial target `pi_s`:

```text
Phi_{s,alpha}(p) = (1 - alpha) p + alpha pi_s.
```

So stability by itself does not choose `s`. The chosen target comes from the
invariance granularity or prior supplied to the dynamics:

| Surface | Natural target | Dial read |
|---|---|---|
| post-record atom symmetry | `(1/2, 1/2)` | `s=0`, `r=1/2`, `Q=2/3` |
| pre-record microstate/dimension symmetry | `(1/3, 2/3)` | `s=1`, `r=1`, `Q=1` |
| post-record token frequency under Born draws | `(1/3, 2/3)` | `s=1`, `r=1`, `Q=1` |

The equal-letter point is therefore a coherent stable post-record target. It is
not selected unless the post-record atom-symmetric target is part of the
physical dynamics.

## Safe Downstream Wording

Allowed:

```text
s=0 / r=1/2 is a stable post-record equal-letter location.
```

Not allowed:

```text
Record dynamics forces s=0.
Post-record counts select Koide.
The physical dial value is fixed by this certificate.
```

## What This Unlocks

- Downstream rows can use `s=0` as a stable setting without pretending it is
  selected.
- Review can reject "forced Koide" wording while preserving the useful stable
  location.
- Dial work can now ask the sharper next question: what physical dynamics or
  invariance surface, if any, chooses among stable `pi_s` targets?

## Non-Claims

This note does not claim:

- Koide is forced;
- the physical dial is fixed;
- post-record count dynamics selects equal-letter;
- a record-production dynamics theorem;
- a Born/probability derivation;
- a repo-wide audit verdict or status-board update.

## Verification

Run:

```bash
python3 scripts/frontier_stable_post_record_dial_location_certificate_2026_06_06.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_stable_post_record_dial_location_certificate_2026_06_06.py
```

Expected summary:

```text
SUMMARY: PASS=43 FAIL=0
```
