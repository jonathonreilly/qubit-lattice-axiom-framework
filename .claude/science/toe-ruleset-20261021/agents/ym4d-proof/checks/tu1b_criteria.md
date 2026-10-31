# checks/tu1b_criteria.md — repair of the tu1-D criterion only (session 25, T-uniformity worker)

Written 2026-10-28T21:36Z, after reading tu1_out.txt. **tu1_criteria.md, tu1_twisted.py and tu1_out.txt are
kept unaltered and tu1-D is reported as a FAIL.** This file repairs one pre-registration arithmetic error and
nothing else; tu1-A, tu1-B, tu1-C and tu1-E are not re-run and not re-judged.

## The error being repaired
tu1-D asked for the uncorrected `max|b|` to grow "by a factor >= 10^3 across" the four values
eps = 1e-1, 1e-2, 1e-3, 1e-4. Four values span **three** decades, so a clean 1/eps pole can give at most a
factor of about 10^3, and at eps = 1e-1 the pole is not yet dominant. **The criterion was unsatisfiable by a
true 1/eps pole, by construction** — the same defect class as GREENT's gt1-D (a gate that cannot PASS).

## Repaired criterion (the phenomenon, not a total)
- **tu1b-D.** With b_1 omitted, at eps = 1e-1 … 1e-6 (six values), the successive ratios
  `max|b|(eps_{j+1}) / max|b|(eps_j)` must each be >= 9.0 and must approach 10 (the last ratio >= 9.9):
  a simple pole in 1/nu_1. With b_1 present, `max|b|` must vary over the same six values by a factor < 10.
  **PASS** iff both hold. **FAIL** otherwise. The two thresholds (9.0, 9.9) and the six-value ladder are fixed
  here, before the script, and are properties of a simple pole, not of any constant of this session.
