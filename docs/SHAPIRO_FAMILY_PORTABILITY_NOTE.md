# Shapiro Family Portability Note

**Date:** 2026-04-06; bounded-source repair 2026-06-17
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status:** bounded finite cross-family replay / source-support packet;
independent audit required before any effective status change
**Primary runner:** [`scripts/shapiro_family_portability.py`](../scripts/shapiro_family_portability.py)
**Cached runner output:** [`logs/runner-cache/shapiro_family_portability.txt`](../logs/runner-cache/shapiro_family_portability.txt)

## Artifact Chain

- [`scripts/shapiro_family_portability.py`](../scripts/shapiro_family_portability.py)
- [`logs/runner-cache/shapiro_family_portability.txt`](../logs/runner-cache/shapiro_family_portability.txt)
- [`SHAPIRO_DELAY_NOTE.md`](SHAPIRO_DELAY_NOTE.md)
- [`SHAPIRO_STATIC_DISCRIMINATOR_NOTE.md`](SHAPIRO_STATIC_DISCRIMINATOR_NOTE.md)

The archived complex-interaction renderer and diamond bridge rows are not live
dependencies for this bounded cross-family replay. The base Shapiro phase-lag
row must itself be accepted only within its bounded proxy scope before this
family-portability row can be used downstream.

## Question

Does the c-dependent proxy phase table reproduce across the three configured
portable grown families with exact zero controls and small cross-family spread?

## Exact Controls

The zero-source control is exact on all three families:

- Fam1: zero lag = `+0.000e+00`
- Fam2: zero lag = `+0.000e+00`
- Fam3: zero lag = `+0.000e+00`

That is the first gate for the bounded portability replay, and it passes.

## Cross-Family Phase Table

| c | Fam1 | Fam2 | Fam3 | max diff |
| ---: | ---: | ---: | ---: | ---: |
| inst | +0.0000 | +0.0000 | +0.0000 | 0.0000 |
| 2.0 | +0.0401 | +0.0401 | +0.0400 | 0.0001 |
| 1.0 | +0.0499 | +0.0501 | +0.0499 | 0.0002 |
| 0.5 | +0.0621 | +0.0622 | +0.0620 | 0.0002 |
| 0.25 | +0.0679 | +0.0679 | +0.0679 | 0.0001 |

The seed rows remain stable within each family:

- the two seeds differ only at the `1e-4` to `1e-3` rad level;
- the family means agree below `2.5e-4 rad` at every finite `c`;
- the proxy phase grows monotonically as `c` decreases.

## Runner Checks

The primary runner asserts:

- exact zero-source control on all three configured families;
- family spread below `2.5e-4 rad` at every finite `c`;
- monotone phase increase as `c` decreases;
- bounded source status and no retained/proposed-retained wording;
- no failed archived bridge dependency in this live source note;
- no absolute diamond/NV calibration, physical field-speed measurement, or
  unique causal-discriminator claim.

## Safe Read

- the Shapiro-style proxy phase table is reproducible across the three
  configured portable grown families;
- the zero-source control remains exact;
- this is a bounded portability replay for the proxy phase observable, not an
  absolute NV calibration;
- the static-cone no-go remains load-bearing: this row does not make the phase
  lag a unique causal discriminator;
- the claim is family-portable inside the configured proxy harness, not a
  physical Shapiro law and not a new value of `c`.

## Claim Boundary

This row may support bounded source-side portability for the proxy phase table
if audit accepts the computation and scope. It does not retain the physical
Shapiro package, the failed diamond bridge rows, the complex-interaction
renderer, or any unique-causality claim.
