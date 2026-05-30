# Gate B Far-Field Bounded Harness Certificate

**Date:** 2026-04-05; review-loop boundary repair 2026-05-26
**Claim type:** bounded_theorem
**Status:** bounded numerical certificate over admitted runner ingredients on
the declared `h = 0.5` far-field rows. This is not a clean physical Gate B
bridge theorem.
**Primary runner:** [`scripts/gate_b_farfield_harness.py`](../scripts/gate_b_farfield_harness.py)
**Runner cache:** [`logs/runner-cache/gate_b_farfield_harness.txt`](../logs/runner-cache/gate_b_farfield_harness.txt)

## Purpose

This row preserves the long-run Gate B far-field harness result while stripping
the old physical-closure reading. The companion runner constructs the
runner-defined grown geometries, applies the runner-defined source field and
propagation/readout rule, and reports the far-field TOWARD and `F~M` checks.

The source law, propagation kernel, valley-linear action, and TOWARD/`F~M`
readout are admitted runner ingredients for this bounded certificate. This
note does not derive them from accepted primitives and does not promote them
to repo-wide axioms.

## Declared Scenario

The cached harness run uses:

```text
h = 0.5
W = 8
NL = 25
seeds = 12
z_masses = [3, 4, 5]
drift/restore rows = (0.3, 0.5), (0.2, 0.7), (0.1, 0.9), exact grid
```

For each drift/restore row, the runner performs twelve seeds by three
far-field `z` masses, for `36` tests per row.

## Bounded Claim

In the SHA-pinned runner cache, the harness reports:

| Row | TOWARD | F~M |
|---|---:|---:|
| `drift=0.3,rest=0.5` | `36/36` | `1.00` |
| `drift=0.2,rest=0.7` | `36/36` | `1.00` |
| `drift=0.1,rest=0.9` | `36/36` | `1.00` |
| `exact grid` | `36/36` | `1.00` |

Thus, under the declared runner ingredients and far-field rows, the harness
returns a clean bounded numerical far-field signature on the tested generated
geometries.

## Boundary

This row does not claim:

- that the grown-geometry rule is derived from accepted primitives;
- that the source law is derived from accepted primitives;
- that the propagation kernel or valley-linear action is derived from
  accepted primitives;
- that TOWARD/`F~M` is the retained physical gravity readout;
- clean Gate B far-field closure;
- a physical gravity or attraction theorem;
- any new axiom or audit verdict.

The primitive-to-physical-gravity bridge remains separate science work. This
row is only a bounded numerical certificate for the runner-defined scenario.

## Verification

The runner is intentionally long and declares `AUDIT_TIMEOUT_SEC = 1800`.
Use the runner cache for routine review and audit packet construction:

```bash
python3 scripts/cached_runner_output.py scripts/gate_b_farfield_harness.py
```
