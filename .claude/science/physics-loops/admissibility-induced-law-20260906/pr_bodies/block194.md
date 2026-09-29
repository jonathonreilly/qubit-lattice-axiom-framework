## Summary

Block 110 (landed) found that outside a spherical body the curvature member's fields are `χ = 1 + a/r` and `N = 1 − p/r`, and that the walk's long-wave rays see the index `n = χ³/N`. That is in the continuum; the lattice's corrections were left open. This note harvests probe HIT #9364, which answers them at first order in the charges.

- **T1.** The exterior is exactly `Q G` and `P G`, where `G` is the cubic lattice's unit-source potential. From the lattice symbol, `G = G₀ + G₁ + G₂ + G₃ + O(r⁻⁹)`:
  - `G₁ = (5Σx⁴ − 3r⁴)/(32πr⁷)` is already landed (the 2026-06-07 cubic-anisotropy note);
  - `G₂` and `G₃` are given here, each satisfying the lattice equation at its order, with no `l = 0` part;
  - the fields' relative anisotropy is `(5Σx⁴/r⁴ − 3)/(8r²)`.
- **T2.** The first-order turn is `(3a + p)[2/b + 2f₁/b³ + 4f₂/b⁵ + …]` toward the body, plus a sideways part `(3a + p)[f₁′/b³ + …]` along `t × β`, with `f₁ = ¼Σt⁴ + Σt²β² + ⅔Σβ⁴ − ¾`.
- **T3.** Tables for the axis (`f₁ = cos 4φ/6`), the face diagonal, and the body diagonal. On the body diagonal `f₁ ≡ 0` and the first anisotropy is `−(4/135) cos 6φ` at `b⁻⁵`. Azimuthal averages are zero, so the averaged turn is the continuum's.
- **T4.** With `a = p = M/2`, the lattice's `b⁻³` term exceeds the continuum's second order only when `Mb < 8/(45π)`.

Scope:
- first order in the charges, for cubic-symmetric content;
- the expansion's existence and remainder are imported;
- the ray-turn formula is first-order ray perturbation, checked by direct ray integration in floating point by the probe and the referee.

Provenance:
- derived by a Claude Opus 5.5 probe worker (HIT #9364);
- refereed by Claude Sonnet 5, same vendor family, which counts under the owner's ruling of 2026-09-28 (confirmed with scope corrections, including the prior art for `G₁`, all applied);
- harvested by the supervisor with its own exact runner.

Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_ON_THE_CUBIC_LATTICE_THE_MEMBERS_EXTERIOR_TURNS_RAYS_WITH_A_DIRECTION_DEPENDENT_PART_FIRST_AT_THE_INVERSE_CUBE_OF_THE_IMPACT_PARAMETER_BOUNDED_THEOREM_NOTE_2026-09-28.md`
- Runner: `scripts/admissibility_rule_on_the_cubic_lattice_the_members_exterior_turns_rays_with_a_direction_dependent_part_2026_09_28.py`, with its cache
- Pack: `GOAL_block194.md`, `RESULTS_block194.md`, `CLAIM_STATUS_CERTIFICATE_block194.md` and `CHECKER_block194_findings.md`, plus appends

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_on_the_cubic_lattice_the_members_exterior_turns_rays_with_a_direction_dependent_part_2026_09_28.py
```

- The runner gives `TOTAL: PASS=17 FAIL=0` in about 2 s.
- Mutation census 7/7.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
