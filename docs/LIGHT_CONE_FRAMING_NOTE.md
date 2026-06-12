# Light Cone Framing — Lieb-Robinson is Standard Lattice QFT

**Date:** 2026-04-11 (math corrected 2026-05-01; CN LR bridge added
2026-05-09; audit-named repair 2026-06-12)
**Status authority:** independent audit lane only. This source note does
not set or predict an audit outcome.
**Primary runner:**
[`scripts/light_cone_staggered_dispersion.py`](../scripts/light_cone_staggered_dispersion.py)
**Runner cache:**
[`logs/runner-cache/light_cone_staggered_dispersion.txt`](../logs/runner-cache/light_cone_staggered_dispersion.txt)
**Companion CN runner:**
[`scripts/light_cone_crank_nicolson_lr_2026_05_09.py`](../scripts/light_cone_crank_nicolson_lr_2026_05_09.py)

## The Concern

The Crank-Nicolson evolution gives a Lieb-Robinson cone with an
exponentially suppressed tail rather than a strict `v = 1` light cone at
finite lattice spacing. Is this a blocker?

## The Answer: No

At finite lattice spacing the repo-internal target is a finite-velocity
Lieb-Robinson envelope with explicit locality weights and declared
sector boundaries, not a strict continuum cone. This note now routes the
framing through the exact-log quasilocal suppliers and the repaired
Crank-Nicolson cone-inheritance statement. It does not use the withdrawn
fixed-step `v_LR^CN` formula, and it does not treat the exact
reconstructed logarithmic Hamiltonian as diameter-2 finite range.

## The Staggered Dispersion Argument (corrected)

The 1+1d staggered Dirac dispersion in lattice units (a = 1) is:

    E² = m² + sin²(k),    k ∈ (-π, π]

The group velocity is:

    v_g(k, m) = dE/dk = sin(k) cos(k) / E = sin(2k) / (2E)

Maximizing over k at fixed m: setting dv_g/dk = 0 gives the implicit
condition

    sin²(k*) = m·(√(m²+1) − m)

Substituting back yields the closed-form maximum

    **v_max(m) = √(m² + 1) − m**

Limits:
  - **m → 0:** v_max → 1, attained at k* → 0 (the linear-dispersion regime
    near the band minimum, where E ≈ |sin k| ≈ |k| and v_g = cos k → 1).
  - **m → ∞:** v_max → 1/(2m), the heavy-mass non-relativistic limit.

Crucially, v_max(m) ≤ 1 for all m ≥ 0, with equality only in the strict
massless limit. The dispersion is **subluminal** for every nonzero mass —
no superluminal velocities are predicted at finite k or finite m.

This corrects two long-standing typos in earlier drafts of this note,
which (a) reported v_max = 1/(2m) as the m << 1 result (it is the m >> 1
limit), and (b) located the massless maximum at k = π/2, where in fact
cos(k) = 0 and v_g = 0. The runner cited in the header validates the
corrected formula numerically against the dispersion at fine k.

## Repaired Authority Stack (2026-06-12)

### Exact reconstructed `H`

[`TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md`](TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md)
supplies the reconstructed free bilinear two-step Hamiltonian

```text
    H = -log(T_hat^2)/(2 a_tau),
    E_d(p) = arcsinh(sqrt(m^2 + sum_mu sin^2 p_mu)),
```

with explicit kernel bound, for every `0 < eta < eta* := arcsinh(m)`,

```text
    |h(z)| <= (1/a_tau) C_d(eta,m) exp(-eta ||z||_inf),
    C_d(eta,m) = sqrt(m^2 + (d-1) + cosh^2 eta).
```

The same authority records the load-bearing negative: on this free
bilinear sector the exact reconstructed `H` is not finite range. It has
nonzero range-4 hopping coefficients, so the old diameter-2
`J_action` surface is not a valid reconstructed-`H` input.

### Exact-evolution cone for reconstructed `H`

[`FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md`](FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md)
turns the exact-log kernel into the weighted-overlap Lieb-Robinson
envelope for the same free bilinear sector. For
`0 < d mu < eta < arcsinh(m)`,

```text
    W_mu := sup_x sum_y ||Phi_xy|| exp(mu d_1(x,y)) < infinity,
```

with the explicit shell-sum upper bound inherited from `C_d(eta,m)`,
and one-site observables obey

```text
    ||[alpha_t(A_x), B_y]||
      <= 2 ||A_x|| ||B_y|| exp(-mu d_1(x,y) + 4 W_mu |t|).
```

This gives a finite lattice cone parameter `v_mu = 4 W_mu/mu` for the
free bilinear exact-log sector. It is an overlap-weight cone parameter,
not a strict relativistic velocity value and not a fixed-step
Crank-Nicolson speed.

### Crank-Nicolson cone inheritance

[`LIGHT_CONE_CRANK_NICOLSON_LIEB_ROBINSON_BRIDGE_NOTE_2026-05-09.md`](LIGHT_CONE_CRANK_NICOLSON_LIEB_ROBINSON_BRIDGE_NOTE_2026-05-09.md)
withdraws the old fixed-step quasilocal-generator and velocity formula.
The replacement is cone inheritance with an explicit integrator defect.
For the Cayley step

```text
    U_CN(a_tau) = (I - i a_tau H/2) (I + i a_tau H/2)^(-1),
```

on a finite subcritical block

```text
    y := a_tau ||H||/2 < 1,
    zeta(A) := a_tau ||[H,A]|| y^2/(1 - y^2),
```

the repaired CN note supplies

```text
    ||alpha_CN(A) - alpha_{a_tau}(A)|| <= zeta(A),
    ||alpha_CN^n(A) - alpha_t(A)|| <= n zeta(A),    t = n a_tau,
```

and therefore

```text
    ||[alpha_CN^n(A_x), B_y]||
      <= ||[alpha_t(A_x), B_y]|| + 2 ||B_y|| n zeta(A_x).
```

Composed with the exact-evolution envelope above, the repaired framing
statement is

```text
    ||[alpha_CN^n(A_x), B_y]||
      <= 2 ||A_x|| ||B_y|| exp(-mu d_1(x,y) + 4 W_mu |t|)
         + 2 ||B_y|| n zeta(A_x),
```

under the stated free-bilinear, finite-block, subcritical, and
`0 < d mu < eta < arcsinh(m)` hypotheses. The additive CN defect is
`O(t a_tau^2)` at fixed `t` on that subcritical surface.

## Retired Formulas

The following legacy surfaces are no longer used by this note:

- The former diameter-2 action-density `J_action` budget as a
  reconstructed-`H` locality input. The exact reconstructed `H` is
  quasilocal on the free bilinear sector, with weights controlled by
  `C_d(eta,m)`, `W_mu`, and the shell sums above.
- The former fixed-step Crank-Nicolson velocity-denominator reading.
  The repaired CN authority explicitly withdraws that velocity formula;
  this note uses the cone-inheritance inequality with additive defect
  instead.

The finite-range microcausality bridge path
`docs/MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`
remains useful context for the older support-family vocabulary, but it
is not cited here as an authority for finite-range exact reconstructed
`H`. The requested class-theorem filename
`docs/EXP_DECAY_LIEB_ROBINSON_QUASILOCAL_BRIDGE_THEOREM_NOTE_2026-06-11.md`
is absent in this checkout; the one-hop quasilocal LR bridge used here
is the free-bilinear bridge linked above.

## What This Architecture Provides

1. **Correct continuum dispersion** in the small-k regime:
   `E ≈ sqrt(m^2 + k^2)`.
2. **Exact free-bilinear reconstructed-`H` quasilocality** with sharp
   rate `eta* = arcsinh(m)` and explicit prefactor `C_d(eta,m)`.
3. **A weighted-overlap Lieb-Robinson envelope** for the free-bilinear
   exact-log Hamiltonian, with finite `W_mu` when
   `0 < d mu < eta < arcsinh(m)`.
4. **Crank-Nicolson cone inheritance** from the exact-evolution cone,
   with additive defect `2 ||B_y|| n zeta(A_x)` on subcritical finite
   blocks.
5. **v_max < 1 for massive particles**, with the explicit dispersion
   formula `v_max(m) = sqrt(m^2 + 1) - m`.

## What It Does Not Provide

- **Strict `v = 1` at finite lattice spacing.**
- **Exact finite range for the reconstructed `H`.** The free-bilinear
  exact log has nonzero longer-range hopping coefficients.
- **A fixed-step Crank-Nicolson velocity value.** The old
  `v_LR^CN` formula is withdrawn; the replacement is a cone bound plus
  an additive defect.
- **A gauged or interacting exact-log LR theorem.** The repaired
  authority stack here is scoped to the free (`U = 1`) bilinear
  two-step sector.
- **A volume-independent CN defect constant.** The repaired CN bridge
  keeps the finite-block `y = a_tau ||H||/2 < 1` hypothesis explicit.
- **A theorem from observed containment percentages.** Finite-spacing
  containment diagnostics remain consistency checks, not proof inputs.

## Repair Log (2026-06-12)

This repair addresses the audit-named stale surfaces by replacing the
finite-range `J_action` reading with the exact-log quasilocal
membership and weighted-overlap LR bridge, and by replacing the
withdrawn fixed-step `v_LR^CN` expression with the repaired
Crank-Nicolson cone-inheritance inequality. Residual open targets are
the gauged/interacting exact-log locality bridge and any
volume-independent sharpening of the CN defect.

## Runner Coverage

`scripts/light_cone_staggered_dispersion.py` checks the dispersion
maximum, the maximizer identity
`sin^2(k*) = m(sqrt(m^2+1)-m)`, the source-note rewiring guards, the
weighted-overlap shell condition, and a small finite-block
Crank-Nicolson cone-inheritance inequality using the Cayley convention
displayed above.

The companion CN runner
`scripts/light_cone_crank_nicolson_lr_2026_05_09.py` remains the
authority for the withdrawal witnesses and the full CN-C' diagnostic
suite.

## Authorities and Context

- [`TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md`](TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md)
  — exact-log quasilocality, sharp rate, prefactor, support-family
  translation, and strict finite-range failure on the free bilinear
  sector.
- [`FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md`](FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md)
  — weighted-overlap Lieb-Robinson envelope for the free bilinear
  exact-log Hamiltonian.
- [`LIGHT_CONE_CRANK_NICOLSON_LIEB_ROBINSON_BRIDGE_NOTE_2026-05-09.md`](LIGHT_CONE_CRANK_NICOLSON_LIEB_ROBINSON_BRIDGE_NOTE_2026-05-09.md)
  — withdrawal of the old fixed-step CN formula and replacement by
  cone inheritance with quantified additive defect.
- `docs/MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`
  — non-authority context in this note for the retired finite-range
  exact-`H` wording and support-family vocabulary.
