# Focused integration findings

One implementation defect was found and repaired by the author. No remaining
mathematical discrepancy was found within the final note's stated hypotheses.
This is a focused mathematical/implementation check, not a formal audit, landing
review, empirical validation, or retained-grade disposition. Root retains authorship.

## Final source identity

| Canonical source | SHA256 |
| --- | --- |
| `docs/SCALAR_OBSERVATION_INVERSE_AND_INPUT_BOUNDS_NOTE_2026-10-16.md` | `23185fcfd16a9f762a9d810efb843ed178e5a749e7dba73dfcfa9726c745f768` |
| `scripts/scalar_observation_inverse.py` | `d4cda09d0fd70b58d998783b8951c6f7596a2bc44909b0003c3679f7ae5d8405` |
| `scripts/scalar_observation_inverse_math.py` | `6c363eb9087e84f932c5ec12964257cb92470daaa51b107f4f0c0d35a2b30c44` |

The final independent run verifies these identities at both ends.
`FINAL_BINDING.json` checks the delivered canonical files and reproduction copies.
Source movement during the check was detected and preserved, including a real
failed identity check after the claim-type metadata addition.

## Finding and repair

The original bin helper raised `TypeError` on the valid positive integral
`H=((a+w)^2-a^2)/2`, with positive `a,w`: SymPy could not decide `H<=0` in that
unfactored representation. The author repaired the guard by factoring SymPy
expressions before inspecting `is_positive`, with `ValueError` for nonpositive
or uncertifiable signs. The final independent checker passes the original
unfactored integration result without caller preprocessing. The primary now
also covers that expression, zero, minus one and an unknown-sign real symbol.
This was an interface defect, not a counterexample to the bin inequality.

## Current independent evidence

The final independent calculation completed **29 checks, zero failures**, in
0.9889713330194354 seconds. It independently re-establishes:

- The helper's Einstein tensor and scalar-Hessian transport denominator, using
  the full four-dimensional connection/Ricci calculation from the metric.
- All diagonal metric equations and the scalar equation for the distinct
  non-power reconstruction `N=exp(r^2/16)`, `B=1/(1+r^2/5)`, on `1<=r<=2`,
  where `d,u>0`. This is an action-class control, not a kinetic-health claim.
- The primitive density and units at arbitrary light speed; all five bound
  coefficients, including both shared-clock contributions, compared against
  independently differentiated rational-function envelopes.
- The completed-square form of weighted Cauchy–Schwarz and equality for an
  actually integrated profile; the repaired helper's relevant domain guards.
- The dust metric/scalar equations and constant-branch scalar slope using
  independently computed curvature, rather than the helper's Einstein formulas.
- The restored reference-length invariant `(C/F)^(2/c)/r_*^2=1/r^2` and every
  diagonal metric/scalar equation for both power-witness exponents with arbitrary
  positive `r_*` and `C`. The new dimensional clarification is correct.

Counts include grouped component identities, guards and source identities;
they are not independent empirical tests. The note supplies the general proofs.
Hand checking confirms the stated endpoint terms, positive-envelope bounds,
finite-sample construction and proper-radius equator argument. For example,
the runner's normalized bump has `psi(0)<=4 exp(1/3)<6`, so its chosen baseline
is everywhere above `0.4`; positivity is not inferred from a sampled grid.

The integration preserves the nonzero `d,u` inverse chart, positive shared-label
margins, actual-overlap requirement for common-action registration, local scope
of the disjoint-range witness, and separation of the regular dust family from
the hypothetical sphere's constant branch. The kinetic sign is not presented
as nonlinear stability. Arbitrary spike functions are not claimed to share a
healthy action. Fixed action coefficients are not retuned during disturbances.
The reference length and numerical normalizations remain stipulated inputs.

## Primary reproduction and read closure

The final unmodified, byte-identical primary reproduction completed **56/56
controls** in 20.388758041895926 seconds. It executes only the isolated copies
in `reproduction_repaired/` and writes their isolated receipt. Observed repository
reads are the runner, imported helper and integrity reads of helper/note, with
an attempted absent bytecode-cache lookup. Bytecode writing was disabled. All
seven public helper functions are exercised, including the three dust-curvature
comparisons and the repaired symbolic-bin controls. Other open events are
Python/runtime/library reads, not undeclared repository data. Source inspection
and tracing support this execution closure; they do not claim every possible
Python environment has been exhaustively characterized.

Both owned programs declare `AUDIT_TIMEOUT_SEC=120` and exact literal input
lists. Every run used an external `subprocess.run(..., timeout=120)` bound.
`REPRODUCTION.md`, actual stdout, execution records and JSON residuals provide
reproduction details. No calculation remains pending.

## Provenance, limits and next obligation

Earlier block01/02/03 checks are context and provenance, not authority for the
current result. The current calculations above do not import them. Historical
52-control and pre-dimensional reproductions do not increase the independent
check count. `SESSION_FAILURES.md` identifies the two original author failures,
my unfactored-integral failure, and the detected note-binding failure; their
actual evidence is preserved. Old source/diff bytes are stored losslessly in
JSON. The author sources and Git state were never changed by this checker.

This check does not verify the cited prior-art paper or checkpoint Git identity,
run the shared landing pipeline, independently assess the author's mutation
suite, or issue an audit status. No new observations were opened. The remaining
scientific obligation is a coupled metric-scalar-matter response at fixed action
parameters, with independently justified forcing, preparation and readout that
discriminates the remaining parameters. The milestone establishes conditional
support, not empirical action choice, absolute calibration, initial state,
history, nonlinear stability or observed global completion.
