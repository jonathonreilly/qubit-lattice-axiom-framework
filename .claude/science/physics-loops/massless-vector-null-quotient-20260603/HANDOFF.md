# Handoff

## Summary

This branch attacks the most tractable bridge item: the massless-vector
polarization row's audit blocker says the quotient calculation closes, but the
row imports physical QFT admissions AC1-AC5. The branch adds a separate exact
linear-algebra theorem proving only

```text
dim_C(ker L_k / span{k}) = 2
```

for a nonzero null vector in a four-dimensional complex vector space with
nondegenerate bilinear form `diag(1,-1,-1,-1)`.

## New artifacts

- `docs/MASSLESS_VECTOR_NULL_QUOTIENT_EXACT_LINEAR_ALGEBRA_THEOREM_NOTE_2026-06-03.md`
- `scripts/massless_vector_null_quotient_exact_linear_algebra_2026_06_03.py`
- `logs/runner-cache/massless_vector_null_quotient_exact_linear_algebra_2026_06_03.txt`

## Existing note touched

- `docs/MASSLESS_VECTOR_POLARIZATION_COUNT_FROM_LORENTZ_AND_GAUGE_BOUNDED_THEOREM_NOTE_2026-05-28.md`

The old note is updated only to point out that the abstract quotient identity
now has a dedicated exact theorem. It still says the physical QFT admissions
remain outside that theorem.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/massless_vector_null_quotient_exact_linear_algebra_2026_06_03.py
python3 scripts/cached_runner_output.py --refresh scripts/massless_vector_null_quotient_exact_linear_algebra_2026_06_03.py
python3 scripts/cached_runner_output.py --check-only scripts/massless_vector_null_quotient_exact_linear_algebra_2026_06_03.py
python3 -m py_compile scripts/massless_vector_null_quotient_exact_linear_algebra_2026_06_03.py
git diff --check
```

## Downstream implication if audit accepts

The algebraic quotient core can move from imported textbook math to one-hop
exact theorem support. That should help the old conditional row re-audit under
the "narrow to only the abstract quotient identity" repair path.

It does not by itself close physical Lorentzian spacetime, plane waves,
continuous gauge redundancy, Lorenz gauge, photon/gluon interpretation, or
thermal `g_*` inventory use.
