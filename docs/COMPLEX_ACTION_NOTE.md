# Complex Action Free-Gamma No-Go Certificate

**Date:** 2026-04-05; no-go repair 2026-05-26
**Runner:** `scripts/complex_action_harness.py`
**Claim type:** no_go
**Status:** exact negative boundary for the current complex-action packet.

## Purpose

The previous row recorded useful finite-lattice behavior for the imposed
complex kernel

```text
S = L(1 - f) + i * gamma * L * f
```

but repeatedly failed audit because `gamma` and the imaginary action term were
introduced by hand. This repair preserves the runner-verified finite facts and
makes the scientific boundary explicit:

The current packet cannot derive a gravity-horizon unification theorem,
horizon observable, or retained complex-action law from the registered inputs.
It is a one-parameter ansatz model with free real `gamma`.

## Exact Negative Boundary

For fixed edge length `L`, field average `f`, wave number `k`, and real
parameter `gamma`, the kernel factor is

```text
exp(i * k * L * (1 - f)) * exp(-k * gamma * L * f)
```

The first factor is the real-action phase. The second factor is an imposed
amplitude weight controlled directly by `gamma`.

Two exact consequences follow inside this packet:

1. At `gamma = 0`, the complex kernel reduces to the real-action propagator.
2. For any edge with `L > 0` and `f > 0`, changing `gamma` changes only the
   imposed amplitude factor by
   `exp(-k * (gamma_2 - gamma_1) * L * f)`.

No equation in this packet fixes `gamma`, derives `i * gamma * L * f`, or maps
the centroid/escape proxy to a horizon observable. Therefore the packet cannot
support a retained gravity-horizon unification theorem. The strongest honest
result is this no-go boundary plus the bounded finite-model table below.

## Preserved Finite Facts

The committed cache `logs/runner-cache/complex_action_harness.txt` verifies
the finite setup

```text
h = 0.5, W = 6, L = 30, s = 0.1, z_src = 3.0
```

and reports:

- `gamma = 0` exactly matches the standard real-action propagator:
  `+9.339748e-02` vs `+9.339748e-02`;
- sampled Born proxies remain at machine precision:
  `2.38e-15`, `1.13e-15`, `1.03e-16`;
- the gamma sweep changes the detector response from TOWARD/amplified to
  AWAY/suppressed, with escape falling from `43.5943` at `gamma=-0.50`
  to `0.0002` at `gamma=2.00`.

Those are valid finite-model facts about the imposed kernel. They do not
derive the kernel.

## Boundary

This row does not claim:

- derivation of `gamma` from retained primitives;
- derivation of the imaginary action term;
- photon-sphere, Schwarzschild, Hawking, or causal-horizon behavior;
- full gravity-horizon unification;
- a continuum theorem;
- any new axiom or audit verdict.

The row is a no-go certificate for the current complex-action route: without a
separate retained bridge fixing `gamma` and a horizon-specific observable, the
finite sweep cannot become a retained gravity-horizon theorem.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/complex_action_harness.py
```

Expected summary:

```text
PASS=38 FAIL=0
```
