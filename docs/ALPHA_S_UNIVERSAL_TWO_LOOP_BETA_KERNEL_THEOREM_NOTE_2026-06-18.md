# Alpha_s Universal Two-Loop Beta-Kernel Theorem Note (2026-06-18)

**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status:** exact support theorem / source-side audit unlock candidate
**Primary runner:** `scripts/frontier_alpha_s_universal_beta_kernel_2026_06_18.py`
**Runner summary:** `SUMMARY: PASS=28 FAIL=0`
**Parent audit pressure:** `alpha_s_direct_wilson_loop_honest_status_audit_note_2026-05-02`

## 1. Purpose

The alpha_s direct Wilson-loop audit names "4-loop QCD running" as one of the
load-bearing imported corrections. This note carves out the part that can be
proved on the framework's existing SU(3) active-flavor surface without
adopting MSbar higher-loop counterterm machinery: the universal two-loop
beta-kernel, namely `beta_0` and `beta_1`.

The theorem is intentionally narrower than a physical alpha_s(M_Z) running
claim. It is a coefficient-kernel theorem for the universal one- and two-loop
terms.

## 2. Boundary Clauses

This note proves the universal two-loop beta-kernel.

This note does not derive beta_2, beta_3, MSbar counterterms, or four-loop running.

This note does not derive physical threshold masses.

This note does not promote any downstream alpha_s(M_Z) value to retained status.

This note does not derive the Sommer scale, a physical Wilson-loop scale
anchor, pure-gauge-to-full-QCD sea-quark transfer, or current `g_bare`
normalization.

## 3. Native Surface

Use the framework's SU(3) Gell-Mann-normalized active-flavor surface:

```text
N = 3
C_F = (N^2 - 1) / (2N) = 4/3
C_A = N = 3
T_F = 1/2
```

The active-flavor parameter `n_f` is left symbolic. Physical threshold
placement is not used.

## 4. Universal Coefficients

The one-loop and two-loop QCD coefficients are the scheme-independent
universal terms:

```text
beta_0(n_f) = (11/3) C_A - (4/3) T_F n_f

beta_1(n_f) =
  (34/3) C_A^2
  - 4 C_F T_F n_f
  - (20/3) C_A T_F n_f
```

Substituting the SU(3) surface gives exact rational functions:

```text
beta_0(n_f) = 11 - 2 n_f / 3
beta_1(n_f) = 102 - 38 n_f / 3
```

The runner verifies these exact forms and the active-flavor values:

```text
beta_0(6) = 7
beta_0(5) = 23/3
beta_1(6) = 26
beta_1(5) = 116/3
beta_1(4) = 154/3
beta_1(3) = 64
```

## 5. Coupling Conventions

For the gauge coupling convention

```text
dg / d ln(mu) =
  - beta_0 g^3 / (16 pi^2)
  - beta_1 g^5 / (16 pi^2)^2
```

and `alpha_s = g^2 / (4 pi)`, the runner verifies the induced alpha_s
convention:

```text
d alpha_s / d ln(mu) =
  - beta_0 alpha_s^2 / (2 pi)
  - beta_1 alpha_s^3 / (8 pi^2).
```

For `a = alpha_s / (4 pi)`, it verifies

```text
d a / d ln(mu) = -2 beta_0 a^2 - 2 beta_1 a^3.
```

These checks prevent coefficient-normalization drift from masquerading as a
science result.

## 6. Falsifiers

The runner includes deliberate wrong kernels:

- omitting the `C_F` term in `beta_1`;
- drifting the trace normalization from `T_F = 1/2` to `T_F = 1`;
- using generation count as active quark flavor count.

Each produces a different coefficient, so the theorem checks a real dependency
class rather than only printing known comparator values.

## 7. Audit Implication

If accepted, this theorem partially retires the "4-loop QCD running" import by
making the universal L1/L2 coefficient kernel native to the framework's SU(3)
surface.

It does not close the full alpha_s running bridge. The remaining residuals are:

- `beta_2` and `beta_3` in an MSbar or other specified scheme;
- dimensional-regularization/counterterm machinery for those scheme-dependent
  coefficients;
- physical threshold placement and decoupling beyond the abstract kernel;
- Sommer-scale or alternate physical scale setting;
- pure-gauge-to-full-QCD transfer;
- current normalization authority for the Wilson surface.

## 8. Reproducibility

Run:

```bash
python3 scripts/frontier_alpha_s_universal_beta_kernel_2026_06_18.py
```

Expected summary:

```text
SUMMARY: PASS=28 FAIL=0
```

The cached output is recorded at
`logs/runner-cache/frontier_alpha_s_universal_beta_kernel_2026_06_18.txt`.
