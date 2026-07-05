# Alpha_s Sommer Static-Potential Root Kernel Theorem Note (2026-06-18)

**Status:** exact support theorem / source-side audit unlock candidate
**Primary runner:** `scripts/frontier_alpha_s_sommer_static_potential_root_kernel_2026_06_18.py`
**Runner summary:** `SUMMARY: PASS=23 FAIL=0`
**Parent audit pressure:** `alpha_s_direct_wilson_loop_honest_status_audit_note_2026-05-02`

## 1. Purpose

The alpha_s direct Wilson-loop audit names the physical Sommer scale
`r0 = 0.5 fm` as a load-bearing imported scale-setting input. This note carves
out the part that is already native to the finite Wilson/static-potential
certificate: the dimensionless Sommer root kernel `r0/a` extracted from the
Cornell fit.

This note proves the dimensionless Sommer root kernel.

It does not derive the physical scale anchor.

## 2. Boundary Clauses

This note does not derive the physical anchor r0 = 0.5 fm.

This note does not promote alpha_s(M_Z) to retained status.

This note does not use r0_anchor_fm as proof input.

This note does not derive physical units, QCD running, threshold matching,
pure-gauge-to-full-QCD transfer, or Wilson-surface normalization.

## 3. Certificate Surface

The source data are the finite Wilson/static-potential certificate:

```text
outputs/alpha_s_direct_wilson_loop_certificate_2026-04-30.json
```

The load-bearing certificate fields are:

```text
scale_setting.global_cornell_fit.sigma
scale_setting.global_cornell_fit.e
scale_setting.global_cornell_fit.r0_over_a
scale_setting.global_r0_over_a
scale_setting.per_volume_r0_over_a_diagnostic
```

The physical field

```text
scale_setting.r0_anchor_fm = 0.5
```

is not used to prove `r0/a`. It is only a downstream conversion from
dimensionless lattice units to femtometers.

## 4. Root Formula

For the certificate's Cornell static potential convention,

```text
V(R) = V0 + sigma R - e/R,
```

the force is

```text
F(R) = sigma + e/R^2.
```

The Sommer root is defined by

```text
F(r0) r0^2 = 1.65.
```

Therefore, in lattice units,

```text
sigma (r0/a)^2 + e = 1.65
```

and the dimensionless root is

```text
r0/a = sqrt((1.65 - e) / sigma).
```

For the certificate values

```text
sigma = 0.054485636694192124
e     = 0.284764583881128
```

the runner recomputes

```text
r0/a = 5.005676254205751.
```

This matches both the global Cornell-fit field and the global scale-setting
field in the certificate.

## 5. Physical Anchor Separation

The certificate also records

```text
r0_anchor_fm = 0.5
global_a_fm = 0.09988660364918762.
```

Those satisfy

```text
a_fm = r0_anchor_fm / (r0/a).
```

This is a downstream physical-unit conversion. If `r0_anchor_fm` is changed,
`a_fm` changes, but the dimensionless root `r0/a` does not. The runner checks
that separation explicitly.

## 6. Falsifiers

The runner includes false kernels that:

- omit the Coulomb `e` term;
- use the wrong force-sign convention;
- use the wrong Sommer target;
- try a nonpositive `sigma`.

Each fails against the certificate's root. The theorem therefore checks the
actual root dependency class rather than merely reading a stored `r0_over_a`
number.

## 7. Audit Implication

If accepted, this theorem partially retires the Sommer-scale blocker by making
the dimensionless static-potential root `r0/a` native to the finite Wilson
certificate.

It does not close the physical Sommer-scale bridge. The remaining Sommer-side
residual is the physical anchor or a replacement scale-setting theorem that
turns the dimensionless root into physical units without importing
`r0 = 0.5 fm`.

## 8. Reproducibility

Run:

```bash
python3 scripts/frontier_alpha_s_sommer_static_potential_root_kernel_2026_06_18.py
```

Expected summary:

```text
SUMMARY: PASS=23 FAIL=0
```

The cached output is recorded at
`logs/runner-cache/frontier_alpha_s_sommer_static_potential_root_kernel_2026_06_18.txt`.
