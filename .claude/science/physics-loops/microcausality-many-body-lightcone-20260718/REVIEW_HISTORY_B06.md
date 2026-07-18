# Review history — block06 (directional-tilt axis-cone refinement)

## Round 1 — combined adversarial lens (codex, read-only), 2026-07-18

Spec: `lens_b06_spec.md`. Output: `lens_b06_out.txt`. Verdict as
issued: no mathematical BLOCKER — "the axis-tilt theorem and its
constants survive independent recomputation" — with three MAJORs on
gate coverage and three MINORs. The lens independently re-derived the
height tables (all orientations), confirmed the mixed-type recursion
validity, the indicator/offset steps (noting the 2m−2 offset is SHARP
at m = 1), the term-by-term sibling match, the exact logarithm-free
display at y = 5/2, the certificate sums (Σ 1/n! = 1957/720; two-term
atanh = 312/343; final margin exactly 3234971/102900), and the scope
statements. Dispositions:

### Major (3)

1. **Scan-best gated against only 2 of 5 competitors** (a 12/5
   interloper would have been false-green). ACCEPTED: V3 now gates all
   five pairwise comparisons with the S_par values themselves gated;
   the note names the full five-fold certificate.
2. **Assembly gate did not reconstruct the sibling k-term.** ACCEPTED:
   new A3 rebuilds the k-term symbolically (2||A||(2J)^(k−1) prefactor,
   2J||B|| base, tilted count, t^k/k!) and sums it to the theorem
   display via sympy Sum; a mutation probe on the count exponent flips
   it.
3. **N-section overstatement** (battery attributed to the runner;
   ATTEMPTED markers missing on N2–N8; N8's repo-wide claim
   unevidenced). ACCEPTED: the battery sentence now names the
   loop-pack battery explicitly and states the runner performs no
   mutations; ATTEMPTED markers added throughout; N8 now records the
   performed search (all 246 NO_GO notes grepped; five
   comparator-only mentions; the closest — single-clock axis
   selection — dispositioned as orthogonal: it forbids deriving a
   time-axis selection, while this note's spatial axis is a
   hypothesis).

### Minor (3)

Finite-volume row-bound wording fixed ("on Z^3; a boundary bond's row
is a sub-sum of positive terms"); V2 now gates the exact finite sums
and the exact rational margin, and the note calls sympy sign checks
supplemental (fail closed on None); the cache is produced at landing
as promised.

### Lens-confirmed survivals

Height tables (all orientations); mixed-type walk validity of the
backward recursion; tilt algebra and domination factorization;
indicator and offset (sharp at m = 1); term-by-term sibling match
including the y^2 factor and k >= 1 start; the exact display
2ABn_X(625/1801)(4/25)^m(e^{(1801/50)J|t|}−1); all certificate
arithmetic; the m-not-d scoping; per-axis/simultaneous-bounds
statement; bond-only, scan-only, non-optimal, no-dynamics boundaries.

### Post-repair state

Runner 17/0 under the ordered label manifest. Batteries: 12 original
probes + 9 extended probes (five-way scan values, k-term exponent,
e-sum truncation, margin, manifest, needle), each flipping exactly the
targeted gate; collateral only same-mechanism (k02: D3→D4/D5/V1/V3,
all consumers of S_par).
