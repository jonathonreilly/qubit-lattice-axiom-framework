# checks/nl1_criteria.md — pre-registered criteria for check nl1 (the degree-2 analytic division)

Written 2026-10-28, BEFORE the script `checks/nl1_division.py` existed. Owner: the (N-loc) worker, session 24.
No constant derived in this session appears below. Exact integer polynomial arithmetic in plain python
(dict-of-monomials Laurent polynomials in z_1..z_4, z_α = e^{ip_α}, ν_α = z_α − 1); single process, no BLAS,
**no numeric lock taken** — permitted by the brief's rule 6 for exact rational/integer arithmetic.

## What is being checked
Lemma NL-11 of NLOC.md §L6 asserts that the explicit formulas
  b_β := T_1 F_{1β} (β ≥ 2),  b_1 := T_2(−E_1F_{12})
solve ν_α b_β − ν_β b_α = F_{αβ} for every closed 2-form symbol F, at d = 4, with
  E_α g := g|_{z_α = 1},  T_α g := (g − E_α g)/(z_α − 1).
The check tests the **identity**, in exact integer arithmetic, on randomly generated closed F. It tests nothing
about the strip bound κ(η, η′), which is proved analytically and is not a polynomial statement.

## Verdicts, pre-registered
- **nl1-A PASS** iff for every one of the 200 random test cases (F := ν∧a for a random integer 1-form symbol a with
  exponents in {0,1,2} and coefficients in [−4, 4]), the constructed b satisfies
  ν_α b_β − ν_β b_α − F_{αβ} ≡ 0 as a polynomial, for all 6 pairs α < β. Any single nonzero residual is a **FAIL**.
- **nl1-B PASS** iff in at least one test case b ≠ a as polynomials, i.e. the construction returns a genuinely
  different representative of the same gauge class (otherwise the check would be testing that the input is returned,
  which is not the lemma's content).
- **nl1-C (designed FAIL control) PASS** iff, for 20 random **non-closed** F (a random antisymmetric integer
  2-form symbol that is NOT of the form ν∧a), the same construction produces a **nonzero** residual in at least
  one pair for at least 19 of the 20 cases. If the residual vanishes for a non-closed input, the test in nl1-A is
  vacuous and the whole check is to be reported as uninformative.
- **nl1-D PASS** iff every T_α division is exact (zero remainder) in every case. A nonzero remainder means
  E_α g ≠ 0 where the lemma's proof claims it is zero, i.e. a defect in the proof, and is a **FAIL**.

## Failure handling, pre-registered
A FAIL is reported as a FAIL in NLOC.md §L9, the script and its output are kept unaltered, any re-run is under a
new id (nl2) with these criteria untouched, and any probe added after seeing a result is labelled post-hoc.
