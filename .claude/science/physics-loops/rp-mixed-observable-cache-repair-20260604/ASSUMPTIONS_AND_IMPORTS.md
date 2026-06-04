# Assumptions And Imports

## Native Inputs

- Finite sampled carriers used by
  `scripts/rp_combined_mixed_observable_u_integrated_2026_05_29.py`.
- Supplied PSD gauge transfer kernel.
- Supplied block-diagonal fixed-gauge fermion two-step core.
- Supplied mixed-observable OS transfer representation.

## Convention Repair

For the U(1) kernel

```text
K(theta) = exp(-beta (1 - cos theta))
         = exp(-beta) exp(beta cos theta),
```

the Fourier coefficients are `exp(-beta) I_n(beta)`, all positive. Suppressing
the positive scalar factor is harmless for PSD, but the source note now states
the full coefficient.

## Open Imports

- The compact-group SU(3) Wilson positivity theorem is not proved by this
  finite sampled diagnostic.
- The full path-integral to transfer-representation bridge is not proved here.
