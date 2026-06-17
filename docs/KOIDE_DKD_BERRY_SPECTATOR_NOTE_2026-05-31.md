# Koide Kahler-Dirac Form-Parity Berry Boundary

**Date:** 2026-05-31
**Claim type:** open_gate
**Claim boundary:** corrected finite Fock-space runner and Berry-boundary repair.
This note does not derive `Q=2/3`, does not certify a zero-Berry spectator theorem, and
sets no verdict.
**Primary runner:**
`scripts/frontier_koide_dkd_berry_spectator_2026_05_31.py`
with cache
`logs/runner-cache/frontier_koide_dkd_berry_spectator_2026_05_31.txt`.

## Result

The runner corrects the `Lambda^1` embedding used by the submitted spectator check. The
one-particle states are created from the unique `N=0` vacuum, and the corrected lift has
`lift(C)^3 = lift(I)` on `Lambda^1`.

With that correction, the durable finite facts are:

- `iD_KD` is Hermitian on `Lambda*(C^3)`;
- form parity `Gamma_F=(-1)^N` anticommutes with `iD_KD`;
- `Gamma_F` restricts to the scalar `-I` on `Lambda^1`, so it cannot by itself impose a
  non-scalar generation grading condition;
- the two circulant `b`-derivative directions commute.

The submitted stronger claim does not survive the correction. The Wilson-loop check for
the tested coupling is not identically zero across the sampled `kappa` and band choices,
so the branch does not certify a Kahler-Dirac Berry-spectator theorem.

## Boundary

This is an open gate and bug repair. It leaves the form-degree Berry role unresolved and
blocks reuse of the stale zero-Berry claim. A future theorem must specify the exact
inter-grade coupling, band-isolation regime, and Berry observable before making a
positive or negative statement about an off-generation monopole route.

## Downstream Source-Boundary Firewall

The F3 commuting-derivative fact is only a local algebra diagnostic for the
tested circulant `b` directions. It is not, by itself, a zero-curvature Berry
theorem and must not be cited as a theorem about form-degree Berry
spectators.

A future positive or negative Berry theorem must separately provide the
inter-grade coupling, band-isolation regime, Berry observable, parameter
domain, and gauge/Wilson-loop convention. This packet only blocks reuse of
the stale zero-Berry spectator claim and records that the corrected finite
Wilson-loop sweep is not identically zero across the tested `kappa` and band
choices.

## Load-Bearing Authorities

[STAGGERED_DIRAC_SUBSTEP2_KAHLER_DIRAC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-17.md](STAGGERED_DIRAC_SUBSTEP2_KAHLER_DIRAC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-17.md)
[KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
[KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md)
