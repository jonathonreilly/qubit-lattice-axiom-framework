# Koide Fisher-Rao Spherical Reorganization

**Date:** 2026-06-01
**Claim type:** bounded_theorem
**Claim boundary:** Fisher-Rao coordinate identity and azimuth demarcation. PDG masses
are used only as observational comparators. This note adopts no Fisher records metric
and no radian convention.
**Primary runner:**
`scripts/frontier_koide_fisher_rao_spherical_reorganization.py`
with cache
`logs/runner-cache/frontier_koide_fisher_rao_spherical_reorganization.txt`.

## Result

For positive masses `m_k`, let `x_k=sqrt(m_k)` and let `theta_p` be the angle between
`x/||x||` and the democratic axis `(1,1,1)/sqrt(3)`. The runner verifies the exact
identity

```text
cos^2(theta_p) = (sum_k sqrt(m_k))^2 / (3 sum_k m_k) = 1/(3Q).
```

Thus `theta_p=pi/4` is exactly equivalent to `Q=2/3`. In the Brannen polar form, the
phase parameter is the azimuth of the same `sqrt(m)` point on the Fisher-Rao sphere.

The runner also checks the demarcation: the round Fisher-Rao metric has
`g_phi_phi=sin^2(theta)`, independent of `phi`, so the azimuth direction is a Killing
direction. The metric alone therefore cannot select the value `2/9`. PDG masses give an
azimuth close to `2/9`, but the azimuth drifts with the mass input; exact `2/9` requires
a shifted tau mass in the runner's comparator calculation.

## Boundary

This is a reorganization and no-go boundary for one route, not a value derivation.
Fisher-Rao geometry supplies a clean spherical coordinate system for the Koide mass
point, but an additional source functional would be needed to break the azimuthal
isometry and select a longitude. The note does not assert that Fisher-Rao is the
framework's records metric.

## No-Go Discipline Gate

**N1.** Routes tested: polar identity, Fisher azimuth, metric invariants, mass drift,
and cyclic relabeling. The polar identity is exact; the value route remains open.
**N2.** The value-selection wall and the period-normalization wall are independent.
**N3.** PDG masses are marked as comparator data, and Fisher-Rao metric use is scoped to
this bounded reorganization.
**N4.** The residual is the missing azimuth-selecting source functional.
**N5.** "Not Fisher-forced" means the metric alone does not choose the longitude; it does
not exclude a future non-isometric source functional.
**N6.** A records/Born functional on the simplex could close the route without an axiom
change.
**N7.** The strongest counterargument is that Fisher-Rao is the canonical statistical
metric. Granted; the canonical metric is still azimuthally symmetric.
**N8.** This matches earlier radian-bridge and unit-normalization residuals while adding
the exact polar identity.

## Load-Bearing Authorities

[KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md)
[AXIOM_FIRST_Z_N_EQUIVARIANT_SPECTRAL_ASYMMETRY_NARROW_THEOREM_NOTE_2026-05-26.md](AXIOM_FIRST_Z_N_EQUIVARIANT_SPECTRAL_ASYMMETRY_NARROW_THEOREM_NOTE_2026-05-26.md)
[KOIDE_DIMENSIONLESS_RADIAN_NATIVE_UNIT_SEPARATION_NARROW_THEOREM_NOTE_2026-05-25.md](KOIDE_DIMENSIONLESS_RADIAN_NATIVE_UNIT_SEPARATION_NARROW_THEOREM_NOTE_2026-05-25.md)
[KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md](KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md)

The [Q-readout quotient note](KOIDE_Q_READOUT_FACTORIZATION_THEOREM_2026-04-22.md)
is context only and is not used to prove the Fisher identity. It proves kernel
invariance only for the definitionally selected class
`S_L={Phi composed with L}`. Locality, bosonic/even parity, species resolution,
first-live rhetoric, and `C_3` covariance have not been shown to classify all
selectors into `S_L`; `S_z(u,v,w,z)=z` is a `C_3`-invariant, kernel-sensitive
counterexample. It supplies no physical charged-lepton selector/carrier,
normalization, `Q=2/3` law, mass spectrum, source law, comparator, or delta
bridge.
