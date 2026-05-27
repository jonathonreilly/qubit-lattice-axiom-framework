# Omega_Lambda Arithmetic Cascade

**Date:** 2026-04-12; narrowed 2026-05-27
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_omega_lambda_arithmetic_cascade.py`
**Status authority:** independent audit lane only

---

## Status

This row is a bounded conditional arithmetic cascade. It no longer claims a
first-principles derivation of `Omega_Lambda` from retained framework inputs.

The retained-bounded support currently available to this row is the exact base
ratio identity
[`R_BASE_GROUP_THEORY_DERIVATION_THEOREM_NOTE_2026-04-24.md`](R_BASE_GROUP_THEORY_DERIVATION_THEOREM_NOTE_2026-04-24.md):

```text
R_base = (3/5) * [((4/3) * 8 + (3/4) * 3) / ((3/4) * 3)] = 31/9.
```

The remaining bridge inputs are declared premises for this row:

```text
Omega_b = 0.0492
R = Omega_DM / Omega_b = 5.38
Omega_total = 1
```

## Bounded Claim

Given the declared premises above:

```text
Omega_DM     = R * Omega_b
Omega_m      = Omega_b + Omega_DM
Omega_Lambda = Omega_total - Omega_m
```

the arithmetic gives:

```text
Omega_DM     = 0.264696
Omega_m      = 0.313896
Omega_Lambda = 0.686104
```

Rounded to the precision used in the historical note, this is
`Omega_Lambda = 0.686`.

The runner also records that the declared `R = 5.38` corresponds to a
Sommerfeld/continuation multiplier

```text
S = R / R_base = 5.38 / (31/9) = 1.561935483...
```

but this row does not derive that multiplier.

## What This Note Does Not Claim

- No derivation of `Omega_b` from `eta` or BBN.
- No derivation of the Sommerfeld/alpha_GUT continuation from `R_base = 31/9`
  to `R = 5.38`.
- No derivation of flatness `Omega_total = 1`.
- No derivation of the DM relic/matter-cosmology bridge.
- No claim that `Omega_Lambda` is retained as a first-principles cosmology
  prediction.
- No audit verdict and no direct ledger retag.

## Relation To The Historical Note

The historical note described a broader chain:

```text
eta(obs) -> Omega_b(BBN) -> R(bounded) -> Omega_DM -> Omega_m -> Omega_Lambda
```

The audit correctly found that only the arithmetic closes from supplied inputs.
This repair preserves that arithmetic and removes the unclosed bridge inputs
from the theorem surface. The broader cosmology story still requires separate
retained-grade bridge work for:

- baryon density / `eta` / BBN input;
- Sommerfeld/alpha_GUT continuation to `R = 5.38`;
- flatness;
- DM relic mapping.

## Verification

Run:

```bash
python3 scripts/frontier_omega_lambda_arithmetic_cascade.py
```

Expected result:

```text
Omega_Lambda arithmetic cascade: PASS
PASS=16 FAIL=0
```

## Audit Request

Please re-audit only the bounded arithmetic cascade above. The intended safe
outcome is retained-bounded status for the declared-input cascade if the
auditor agrees the runner closes those finite arithmetic statements. The
unclosed cosmology bridges should remain out of scope.
