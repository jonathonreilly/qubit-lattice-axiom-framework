# Native I_S: the Composite-H_unit Matching Kernel, Settled (Bounded)

**Date:** 2026-06-16
**Claim type:** bounded_theorem
**Claim boundary:** settles the propagator-kernel fork and computes the
framework-native scalar matching coefficient `I_S` from primitives + the
framework tadpole; bounded on the canonical plaquette `<P>` and the staggered
taste count `N_taste=16`. Does **not** import the literature `I_S in [4,10]`.
**Status authority:** independent audit lane only; effective status is
pipeline-derived after audit. No audit verdict asserted here.
**Primary runner:**
[`scripts/yt_p1_i_s_native_kernel_settled_2026_06_16.py`](../scripts/yt_p1_i_s_native_kernel_settled_2026_06_16.py)
**Cached log:**
[`logs/runner-cache/yt_p1_i_s_native_kernel_settled_2026_06_16.txt`](../logs/runner-cache/yt_p1_i_s_native_kernel_settled_2026_06_16.txt)
(PASS=9 FAIL=0)

## The fork this settles

A prior native 1-loop BZ quadrature of the composite-`H_unit` scalar-bilinear
matching coefficient `I_S` reached an honest PARTIAL: the value swung
**3.46 .. 161.9** depending on an unsettled propagator-kernel form,
`D_psi^-2 D_g^-1` vs `D_psi^-1 D_g^-1`. This note **derives** the correct form.

## Derivation (from the operator + Feynman rules, not from the target value)

For `H_unit = (1/sqrt(N_c N_iso)) sum psi_bar psi` (scalar insertion = identity)
dressed by one gluon, the 1PI `D_S1` sandwich has two untraced fermion
propagators and one gluon propagator (the apparent `D_psi^-2 D_g^-1`). But the
**scalar trace reduces one power of `D_psi`**: with `S(k) = -i slash{s}/D_psi`
and `slash{s} slash{s} = (sum_rho s_rho^2) 1 = D_psi(k) 1`,

```
Tr[ S(k) . 1 . S(k) ] = -Tr[ slash{s} slash{s} ] / D_psi^2 = -4 D_psi / D_psi^2 = -4 / D_psi,
```

so the trace-reduced matching kernel is `N_S(k) / (D_psi(k) D_g(k))`, **not**
`N_S(k) / (D_psi^2 D_g)` (using both `N_S` and `D_psi^-2` double-counts).

**Continuum consistency confirms it:** with the settled kernel `D_psi -> k^2`,
`D_g -> k^2`, `N_S -> 4` gives the standard subtraction `4/(k^2+m^2)^2`
(runner ratio `1.0000000`); the literal `D_psi^-2 D_g^-1` form has the WRONG
continuum power (`~4/k^6`) and is rejected (ratio `3.3e6`).

## Result

`I_S = 3.902216606`, stable under grid refinement (N=32->48->64 drift `6e-5`,
no fork-scale swing). Computed with the framework tadpole `u0 = <P>^(1/4)`,
`<P> = 0.5934`, and `N_taste = 16`. **No literature `I_S` value enters the
load-bearing computation** (runner imports only `numpy`).

## What this changes (the honest part)

- The kernel fork -- the one blocker on the `native_I_S` quadrature -- is
  **settled**, and the literature import `I_S in [4,10]` is **replaced** by a
  framework-native value.
- **`I_S = 3.90` lands BELOW the literature bracket `[4,10]`** (central 6). This
  is a genuine discrepancy, not reverse-engineering -- a kernel chosen to hit
  `[4,10]` was explicitly disallowed. **Downstream P1-budget rows that used
  `[4,10]` will therefore re-compute to lower values** on re-audit; this is a
  value change, not a clean status flip.
- The native value remains **bounded on** the framework tadpole `<P>=0.5934`
  (a gauge-vacuum quantity tied to the beta=6 surface) and `N_taste=16` --
  framework admissions, not the retired literature import.

## Provenance

Derived by a supervised workhorse worker (codex `gpt-5.5`); independently re-run
and ledger-audited by the Opus-4.8 supervisor (PASS=9 reproduced; no smuggled
`[4,10]`; the scalar-trace leg-count `Tr[(-i slash{s}/D_psi)^2] = -4/D_psi`
checked by hand; the `D_psi^-2` form's wrong continuum power confirmed).

## Deep-investigation correction (2026-06-16) -- the value is NOT settled

A two-pronged audit (independent full re-derivation + literature/factor audit)
found that the **kernel fork is settled** (`D_psi^-1 D_g^-1`, with no missing
operator-tadpole/sail/seagull/measure diagram for the local `H_unit`), but the
**final value `3.90` is NOT reliable**, for two reasons:

1. **The `[4,10]` comparator is MIS-ATTRIBUTED.** The framework note labels
   `[4,10]` "tadpole-improved Wilson + 1-link staggered," but the primary
   sources (Lee-Sharpe hep-lat/0208018: unimproved `c_S = -29.4`, `|c_S|` up to
   `38.1`; Bhattacharya-Gupta hep-lat/9710095, the cited paper: TI single-link
   `39.1`) give `~29-39` for the single-link/plaquette staggered scalar in the
   IDENTICAL convention. `[4,10]~6` is actually the **smeared-action** band
   (HYP/Fat-7/asqtad). The framework uses Wilson-plaquette + single-link `D_psi`,
   so the correct comparator is `~29-39`, not `[4,10]`.

2. **The `/N_TASTE` division is CONTESTED (3.90 vs ~32).** The runner divides
   the full-BZ integral by `N_TASTE=16` (-> `3.90`), but `D_psi_full`'s own
   docstring says the 16-taste sum is ALREADY in the full-BZ extent and one must
   NOT divide by `N_TASTE` (-> `~32`). The two audits split:
   - *literature/factor audit:* the `/16` double-counts (the runner contradicts
     its own docstring; no-division `~32` matches the single-link literature
     `29-39`; the sibling `HIGGS_CHANNEL_EFFECTIVE_NTASTE_BOUNDARY` note already
     flags `N_taste=16` as an UNDERIVED admission) -> the correct value is `~32`.
   - *independent re-derivation:* `3.90` is the correct *narrow* per-flavor
     coefficient after taste projection + `Z_q` + tadpole -- a different object
     from the full literature bilinear.

**Status: the I_S value is UNRESOLVED** (`3.90` with `/N_TASTE`, `~32` without),
pending a derivation of whether the per-flavor `H_unit` coefficient genuinely
carries the `/N_TASTE` taste-projection given the full-BZ extent already covers
the 16 corners. The evidence (the runner's own docstring + the single-link
literature match at `~32` + the underived-admission flag) leans toward NO
division (`~32`), but it is genuinely contested. **No P1 precision claim should
rest on `I_S=3.90` until this is resolved.** The kernel-fork result stands.
