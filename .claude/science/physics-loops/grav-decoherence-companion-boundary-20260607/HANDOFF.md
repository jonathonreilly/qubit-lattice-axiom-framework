# Handoff

This PR repairs `grav_decoherence_derived_note` by retargeting it to bounded companion arithmetic and source-boundary hygiene.

What changed:

- The note now marks the direct target as bounded companion / external-model arithmetic.
- The note states that the supplied physical model is not a load-bearing retained premise for this row.
- The runner source-boundary checks enforce the new boundary.
- The cache now reports `PASS=19 FAIL=0`.

What this does not claim:

- No framework-native gravitational decoherence theorem.
- No derivation of mass-source/readout, `G_N`, SI normalization, Penrose-Diosi rate law, BMV geometry, Planck pin, or `L^{-1}=G_0`.
- No audit verdict edits.

Verification:

```text
frontier_grav_decoherence_derived.py: PASS=19 FAIL=0
cached_runner_output check-only: fresh
```
