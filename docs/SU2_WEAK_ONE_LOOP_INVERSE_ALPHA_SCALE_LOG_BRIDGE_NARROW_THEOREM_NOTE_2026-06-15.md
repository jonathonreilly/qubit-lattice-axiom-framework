# SU(2)_L One-Loop Inverse-Alpha And Scale-Log Bridge Narrow Theorem

**Date:** 2026-06-15
**Type:** bounded_theorem
**Claim scope:** narrow source-side bridge for the `g_2(v)` bounded
interval row. It proves two framework-local pieces that had been
recorded there as separate named admissions:

1. Given the already-isolated one-loop SU(2)_L beta-coefficient
   convention and value `b_2 = 19/6`, plus the standard
   `alpha = g^2/(4 pi)` convention already consumed by the SU(2)
   lattice-alpha anchor, the inverse-alpha propagation law is the
   exact calculus identity

   ```text
   1/alpha_2(mu_IR)
     = 1/alpha_2(mu_UV) - (b_2/(2 pi)) ln(mu_UV/mu_IR).
   ```

2. Given the approved scale-reference primitive `a^-1 = M_Pl` and the
   hierarchy candidate readout surface
   `v_cand = M_Pl * (7/8)^(1/4) * alpha_LM^16`, the dimensionless log
   interval is fixed internally as

   ```text
   L_cand := ln(M_Pl/v_cand)
           = -ln((7/8)^(1/4) * alpha_LM^16)
           = 38.442224515163...,
   ```

   so the existing exact-symbolic surrogate `L = 3844/100 = 38.44`
   used by the `g_2(v)` companion runner is a rounded scale-log readout,
   not an independent external number.

This bridge does not derive the numerical `u_0(SU(2))` interval, does
not derive the continuum one-loop beta law beyond the textbook
one-loop convention already isolated in the beta-coefficient row, and
does not promote the hierarchy candidate readout to an electroweak VEV
prediction. It only removes duplicate/import-style uses of scale-log
arithmetic and the integrated inverse-alpha formula from downstream
`g_2(v)` bookkeeping.

**Status authority:** independent audit lane only. This source note does
not set or predict an audit outcome.

**Runner:** [`scripts/audit_companion_su2_weak_one_loop_inverse_alpha_scale_log_bridge_2026_06_15.py`](../scripts/audit_companion_su2_weak_one_loop_inverse_alpha_scale_log_bridge_2026_06_15.py)

## Inputs

**(B1) SU(2)_L beta-coefficient convention and value.**
[`SU2_WEAK_BETA_COEFFICIENT_NARROW_THEOREM_NOTE_2026-05-10.md`](SU2_WEAK_BETA_COEFFICIENT_NARROW_THEOREM_NOTE_2026-05-10.md)
isolates the standard one-loop SU(2)_L beta-coefficient convention and
the framework count substitution `b_2 = 19/6`. This bridge consumes that
row's coefficient surface; it does not rederive textbook perturbative
QFT.

**(B2) Fine-structure convention and lattice alpha anchor.**
[`SU2_WEAK_ALPHA_LATTICE_ONE_OVER_SIXTEEN_PI_ANCHOR_NARROW_THEOREM_NOTE_2026-05-28.md`](SU2_WEAK_ALPHA_LATTICE_ONE_OVER_SIXTEEN_PI_ANCHOR_NARROW_THEOREM_NOTE_2026-05-28.md)
already isolates the standard `alpha = g^2/(4 pi)` convention and the
bounded one-hop SU(2)_L lattice anchor `1/alpha_2^bare = 16 pi`.

**(B3) Scale-reference primitive.**
[`SCALE_REFERENCE_PRIMITIVE_NOTE.md`](SCALE_REFERENCE_PRIMITIVE_NOTE.md)
registers the single dimensionful ruler `a^-1 = M_Pl`. This is a units
conversion and carries no dimensionless physics by itself.

**(B4) Hierarchy candidate readout surface.**
[`HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md`](HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md)
separates the structural hierarchy support theorem from the declared
candidate map

```text
v_cand := M_Pl * K,
K := (7/8)^(1/4) * alpha_LM^16,
alpha_LM := alpha_bare/u_0,
alpha_bare := 1/(4 pi),
u_0 := <P>^(1/4),  <P> = 0.5934.
```

This bridge consumes only the dimensionless candidate-map arithmetic
needed to compute `ln(M_Pl/v_cand)`. It does not use the fenced PDG
comparator and does not close the hierarchy row's B3/B4/B5 formula
gates.

## Theorem A: inverse-alpha one-loop integration

Let `t = ln(mu)` and assume the standard one-loop beta-law convention
already isolated by `(B1)`:

```text
dg/dt = - b g^3/(16 pi^2),     b > 0.
```

With the fine-structure convention `(B2)`,

```text
alpha := g^2/(4 pi).
```

Then

```text
d alpha/dt = (g/(2 pi)) dg/dt
            = - b g^4/(32 pi^3)
            = - b alpha^2/(2 pi),
```

and therefore

```text
d(1/alpha)/dt = b/(2 pi).
```

Integrating from `mu_UV` down to `mu_IR` gives

```text
1/alpha(mu_IR)
  = 1/alpha(mu_UV) + (b/(2 pi)) (ln(mu_IR) - ln(mu_UV))
  = 1/alpha(mu_UV) - (b/(2 pi)) ln(mu_UV/mu_IR).
```

At `b = b_2 = 19/6`, `mu_UV = M_Pl`, and `mu_IR = v_cand`, this is the
running equation consumed by the `g_2(v)` interval row.

## Theorem B: scale-log arithmetic from the hierarchy readout

By `(B3)` and `(B4)`,

```text
v_cand = M_Pl * K,
K = (7/8)^(1/4) * alpha_LM^16.
```

Thus the Planck-to-candidate-scale logarithm is dimensionless and the
`M_Pl` unit drops out:

```text
ln(M_Pl/v_cand) = ln(M_Pl/(M_Pl K)) = -ln(K).
```

Substituting the declared hierarchy surface values

```text
alpha_bare = 1/(4 pi),
u_0 = 0.5934^(1/4),
alpha_LM = alpha_bare/u_0,
K = (7/8)^(1/4) * alpha_LM^16
```

gives

```text
K = 2.017223509625105...e-17,
L_cand = -ln(K) = 38.44222451516312...
v_cand = 1.2209e19 GeV * K = 246.282818290129... GeV.
```

The downstream `g_2(v)` companion runner historically used the exact
rational surrogate

```text
L_100 := 3844/100 = 38.44.
```

This bridge proves that `L_100` is the two-decimal rounded readout of
the framework hierarchy candidate log:

```text
|L_cand - L_100| = 0.00222451516312... < 0.003.
```

## What This Claims

- The integrated inverse-alpha one-loop law follows by calculus from
  the already-isolated one-loop beta coefficient convention.
- The scale logarithm used by the `g_2(v)` bounded interval row is
  computed from the repo's scale-reference primitive and hierarchy
  candidate map; the two-decimal value `38.44` is a rounded readout of
  `L_cand`, not an independent external number.
- The bridge is reusable by downstream rows that need only the
  inverse-alpha integration formula or the Planck-to-hierarchy-candidate
  scale log.

## What This Does Not Claim

- Does **not** derive the continuum one-loop beta-law convention from
  Cl(3) alone. That textbook perturbative-QFT content remains isolated
  in the beta-coefficient authority surface consumed here.
- Does **not** derive the numerical `u_0(SU(2))` interval
  `[0.96, 0.98]`; that remains the open residual for the `g_2(v)`
  interval row.
- Does **not** derive or promote the full hierarchy formula as an
  electroweak VEV prediction. The result is a bounded scale-log bridge
  over the declared hierarchy candidate map.
- Does **not** consume observed `g_2(v)`, PDG electroweak couplings,
  fitted selectors, or any new axiom.

## Validation

Run:

```bash
python3 scripts/audit_companion_su2_weak_one_loop_inverse_alpha_scale_log_bridge_2026_06_15.py
```

Expected summary:

```text
TOTAL: PASS=19 FAIL=0
```
