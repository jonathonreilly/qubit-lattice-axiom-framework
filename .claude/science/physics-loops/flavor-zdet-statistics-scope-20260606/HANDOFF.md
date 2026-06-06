# Handoff

## Summary

This branch repairs the Z=det fermionic-statistics locator by preserving the
finite determinant-realization checks and removing admission/baseline promotion.

## Files

- `docs/FLAVOR_ZDET_FERMIONIC_STATISTICS_ADMISSION_2026-06-04.md`
- `scripts/flavor_zdet_fermionic_statistics_admission_2026_06_04.py`
- `logs/runner-cache/flavor_zdet_fermionic_statistics_admission_2026_06_04.txt`

## Science

The packet now says:

- supplied Grassmann/CAR variables realize determinant amplitudes;
- ordinary cross-site tensor-product ladders commute;
- Jordan-Wigner is a realization after a generator choice;
- local dimension two does not distinguish fermions from hard-core bosons;
- spatial CAR and internal `Gamma_chi` are separate residuals.

## What Review Should Check

- The note does not promote FS as derived or admitted.
- The runner source-boundary guard enforces that source text.
- No `docs/audit/**` files are changed.

## Next Science

The follow-up remains a derivation or admission of FS, likely via a dedicated
spin-statistics/reconstruction loop.
