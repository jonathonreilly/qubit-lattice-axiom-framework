# Handoff

This branch is the landable follow-up to closed PR #3430.

It adds `D3_NATIVE_STABLE_ORBIT_UPPER_BOUND_COMPOSITION_NOTE_2026-06-09.md`
and a runner/cache. It does not edit the retained Bertrand support note, the
legacy upper-bound wrapper, the existing D3 gate, or any `docs/audit/**` file.

Review target:

- Accept the additive wrapper as a source-side composition certificate.
- Leave retained-row rewrites to a separate retained-row re-audit path if the
  project still wants to update old wording.
