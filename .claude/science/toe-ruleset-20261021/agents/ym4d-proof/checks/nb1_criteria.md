# checks/nb1_criteria.md — pre-registered criteria for check nb1 (T55-E, session 25)

**Born 2026-10-28T21:19Z, BEFORE `checks/nb1_logdiv.py` existed.** No constant below is derived in this
session. The only numbers that appear are: the dimension d = 4; the surface measure of the unit 3-sphere
in R⁴, |S³| = 2π² (a textbook constant, not a lane constant); and the exponents 4 and 5.

## What is being decided, and why a check is needed at all

GREENT.md proves (GT-2) |∇_μ∇_λ G_R(x)| ≤ C₂|x|₂^{−d} with C₂ = 1703 at d = 4, uniformly in the torus
side R. Part of target NB5 is whether that bound — the sharpest statement the lane has about the level-0
free Green's function — can supply the **fine half of (G♯_0-field)**, whose failure mode (G0-F2, RTARGET
§33 l.613-615) is *"the fine-level Calderón–Zygmund singularity: no bound in sup norm alone for f_0"*.

The question reduces to one arithmetic fact: **does a kernel bound |K(x)| ≤ C|x|₂^{−d} on Z^d make the
operator bounded ℓ^∞ → ℓ^∞?** It does iff Σ_{x≠0}|x|₂^{−d} converges. I do not want to assert the answer
from the continuum integral alone, because the lattice sum is the object the estimate is actually applied
to, and because a check that cannot fail is not evidence (session-25 addendum, systemic defect 3).

## The quantity

For R ∈ {3, 6, 12, 24} and exponent s ∈ {4, 5}:

  S_s(R) := Σ_{x ∈ Z⁴, 0 < |x|₂ ≤ R} |x|₂^{−s}

reported exactly as a float, together with the doubling increments Δ_s(R) := S_s(2R) − S_s(R).

## Pre-registered verdicts

- **nb1-A (the claim under test; s = 4).** PASS iff the increments Δ₄(R) for R = 3 → 6, 6 → 12 are both
  **within ±20 % of 2π² ln 2 = 13.6871…** and are **not decreasing towards 0** (each at least 0.8 × the
  previous). This is the signature of a logarithmically divergent sum: equal mass per octave.
  FAIL iff either increment falls outside the band, or the increments decay geometrically.
  *Consequence if PASS:* Σ|x|^{−4} diverges, so (GT-2) does **not** give an ℓ^∞ → ℓ^∞ bound, and GREENT
  cannot supply (G♯_0-field)'s fine half. *Consequence if FAIL:* my NB5 reasoning is wrong and I must
  withdraw the claim that (G0-F2) survives GREENT.

- **nb1-B (DESIGNED-FAIL CONTROL; s = 5).** The same test applied at s = 5, where the sum **must**
  converge. The control is deemed to have **worked** iff nb1-A's criterion **FAILS** at s = 5, i.e. the
  increments Δ₅(R) decay towards 0 and leave the ±20 % band around 13.6871.
  If the s = 5 input *passed* nb1-A's criterion, the criterion has no power to discriminate and the whole
  check is to be reported as **no evidence**, whatever s = 4 did.

- **nb1-C (sanity on the geometry).** The count of lattice points with 0 < |x|₂ ≤ R must satisfy
  N(R)/R⁴ → π²/2 = 4.9348… to within ±15 % at R = 24. FAIL means the enumeration is wrong and nb1-A/B
  are void.

## Not success

Any retuning of the ±20 % band, of the octave list, or of the exponents after seeing output. Any
re-run under the same id. A conclusion about (G♯_0-field) drawn from nb1 alone: nb1 decides only the
one arithmetic fact above, and the rest of NB5 is argument, not arithmetic.

## Resources

Plain Python 3, integer and float arithmetic only, no numpy, no BLAS — DRIVE_BRIEF rule 6 exempts this
from the numeric lock. `python3 -I`, `nice -n 10`, thread variables set to 1. Expected under 60 s and
under 100 MB. R is capped at 24 (49⁴ = 5 764 801 lattice points enumerated) so that it stays there.
