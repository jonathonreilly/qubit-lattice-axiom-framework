# ts55_1 — criteria (pre-registered before any script exists)

Written 2026-10-29 (UTC time stamped by `date -u` in the record line at the end), by the TSE55 worker (claude-opus-5-5).
Script to be written AFTER this file: `checks/ts55_1_bubble.py`. Exact arithmetic only (fractions.Fraction; sympy only for the
√3 in the SU(3) generators of gate A5). No floats anywhere in a verdict.

## What is tested
The exact chain of constants behind the free-bubble coefficient c_bub = 12(N² − 1)/π⁴ of TSE55 §2.4, by a route independent of
nf55_a (symbolic differentiation + 12-component enumeration) and of CODEX_REVIEW_NONFREE R8 (six-component Λ²I inversion):
the closed tensor identity  Σ_{μνρσ} X_{μνρσ}² = (4d − 8)·tr(T²) + 4·(tr T)²,  where T_{μρ} := ∂_μ∂_ρ(1/P), P := Σ_α z_α², and
X_{μνρσ} := δ_{νσ}T_{μρ} − δ_{νρ}T_{μσ} − δ_{μσ}T_{νρ} + δ_{μρ}T_{νσ}  (so the continuum F-F correlator is D = −X/(4π²)).

## Gates (each PASS/FAIL as written; a control must FAIL for the gate to count)
- **A1.** d = 4, the 8 fixed nonzero rational points listed in the script header (chosen before running: integer and
  half-integer coordinates, no symmetry). T computed by the GENERIC quotient rule (∂_μ(1/P) = −∂_μP/P²,
  ∂_ρ∂_μ(1/P) = −∂_ρ∂_μP/P² + 2∂_μP∂_ρP/P³, with ∂_μP, ∂_ρ∂_μP computed from P's coefficient representation, not typed in).
  S := brute-force Σ over all 4⁴ index quadruples of X². PASS iff, at all 8 points, S = (4d − 8)tr T² + 4(tr T)² exactly AND
  S·P⁴ = 384 exactly.
- **A1-F (control).** The wrong closed form (4d − 4)tr T² + 4(tr T)² must differ from S at every point (expected: tr T² ≠ 0).
  The gate A1 counts only if A1-F differs at ≥ 1 point.
- **A2.** d = 3, 6 fixed rational points, same construction (1/P is not harmonic there): PASS iff S = (4·3 − 8)tr T² + 4(tr T)²
  at every point (the identity is dimension-general) AND S·P⁴ ≠ 384 at ≥ 1 point (the value 384 is a d = 4 fact).
- **A3.** d = 4: Σ over unordered pairs μ < ν, ρ < σ of X² equals S/4 exactly at all 8 points.
- **A4.** Amplitude arithmetic, two routes, both must give the rational 12 (= c_bub·π⁴/(N² − 1)):
  plaquette route 2·(S·P⁴/4)/16; clover route (1/32)·16·(S·P⁴/16). PASS iff both equal 12.
  **A4-F (control):** the clover route with 4 clover-pair terms in place of 16 must give a value ≠ 12.
- **A5.** Generator normalisation: tr(t^a t^b) = δ^{ab}/2 exactly for SU(2) (Pauli/2) and SU(3) (Gell-Mann/2, √3 symbolic);
  and the second-order Taylor coefficient of 1 − N⁻¹Re tr exp(iX) at X = √(2N)Σ_aF^at^a, for 3 fixed rational F-vectors per
  group, equals ½Σ_a(F^a)² exactly (sympy series in a scalar t multiplying X; exact rationals).
  **A5-F (control):** with generators normalised to tr(t^at^b) = δ^{ab} the coefficient must differ from ½Σ(F^a)².

## Verdict rule
ts55_1 PASS iff A1, A2, A3, A4, A5 all PASS and A1-F, A4-F, A5-F all behave as stated. Anything else: FAIL, recorded as such.

## What this check cannot decide
It does not test the lattice-to-continuum convergence of the F-propagator (input (LGF), [m]), the running-coupling structure,
or any Yang–Mills estimate. It certifies only the exact constants of the leading free bubble.

## Record
- criteria file completed 2026-10-29T06:08:21Z (date -u); no script for ts55_1 exists at this time.
