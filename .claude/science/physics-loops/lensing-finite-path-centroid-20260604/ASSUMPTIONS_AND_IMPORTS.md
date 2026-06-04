# Assumptions And Imports

## Retained Inputs Used

- Existing `scripts/lensing_analytical_finite_path.py` runner and cache.
- Existing `scripts/lensing_long_path_test.py` runner and cache.
- Existing `docs/LENSING_LONG_PATH_TEST_NOTE.md` as the Lane L++ data note named by audit.

## Still Open

- No retained layer-weighted theorem derives the detector-centroid observable
  from the literal harness geometry.
- No new axiom or accepted premise is introduced.

## Import Treatment

The finite-path ray formula remains a diagnostic comparator, not a proof input
for retained closure. The PR exposes it and the falsifying Lane L++ data so the
audit packet can be checked directly.
