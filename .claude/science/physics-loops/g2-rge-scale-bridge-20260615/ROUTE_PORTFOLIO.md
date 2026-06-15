# Route Portfolio

## Route A: Scale Log Bridge

Use the checked-in scale-reference primitive and hierarchy candidate map:

```text
v_cand = M_Pl * (7/8)^(1/4) * alpha_LM^16
ln(M_Pl/v_cand) = -ln((7/8)^(1/4) * alpha_LM^16)
```

Outcome: implemented in
`docs/SU2_WEAK_ONE_LOOP_INVERSE_ALPHA_SCALE_LOG_BRIDGE_NARROW_THEOREM_NOTE_2026-06-15.md`
and its runner.

## Route B: One-Loop Inverse-Alpha Integration

Starting from

```text
dg/dln(mu) = -b g^3/(16 pi^2)
alpha = g^2/(4 pi)
```

derive

```text
1/alpha(mu_IR) = 1/alpha(mu_UV) - (b/(2 pi)) ln(mu_UV/mu_IR)
```

Outcome: implemented in the same bridge note and runner.

## Route C: SU(2) Tadpole Closure

Derive or certify `u_0(SU(2)) in [0.96, 0.98]` from framework-native
nonperturbative data.

Outcome: not solved here; remains the high-value residual after X6/X7.
