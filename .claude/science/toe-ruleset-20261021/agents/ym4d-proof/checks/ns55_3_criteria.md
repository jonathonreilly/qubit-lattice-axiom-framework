# ns55_3 — criteria (written before the script; NSL55.md resumed run, claude-opus-5-5)

Written (UTC) 2026-10-29, after `date -u` = 03:16:42 and before `ns55_3_kg.py` exists.

## What is checked (decides nothing load-bearing; K_G only enters smallness thresholds)
NSL55 §3.2 (Lemma B) displays "K_G ≤ 2C_alg·max(m(1/20)·20², 2m(1/10)·10²) ≤ 1.5·10³" with C_alg = 8 and
m(R) := −log(2 − e^{4R}) + 2R. The resumed run's derivation (§R) gives instead K_G ≤ C_alg·max(400·m(1/20), 200·m(1/10)).
Claim A: the draft's displayed expression 2·8·max(400 m(1/20), 200 m(1/10)) is > 1500 (so the displayed "≤ 1.5·10³" is false
for the displayed formula). Claim B: the re-derived expression 8·max(400 m(1/20), 200 m(1/10)) is < 1500.

## Method
Exact Fractions, plain python (`python3 -I`), no floats in any verdict. exp(q) for rational q ≥ 0 bracketed by Taylor partial
sums (lower) and partial sum + tail bound q^{N+1}/(N+1)!·1/(1 − q/(N+2)) (upper). log(w) for rational w > 1 bracketed by
2·Σ_{n odd ≤ N} t^n/n (lower) and that + 2t^{N+2}/((N+2)(1 − t²)) (upper), t = (w − 1)/(w + 1). m(R) bracketed using monotonicity.

## PASS / FAIL (pre-registered)
- K1 (control): the code must report m(R) undefined (2 − e^{4R} ≤ 0 possible) at R = 9/50 (e^{0.72} > 2). FAIL of the CHECK if it
  returns a bracket there.
- K2 (control): bracket widths for m(1/20), m(1/10) are < 10^{-6}. FAIL of the CHECK otherwise (cannot decide).
- K3 (control): the log bracket contains a known value: log(e-bracket of 1/2) must contain 1/2 (consistency of exp and log code).
- A: lower bound of 16·max(400 m(1/20), 200 m(1/10)) > 1500. B: upper bound of 8·max(400 m(1/20), 200 m(1/10)) < 1500.
- Overall PASS iff K1, K2, K3, A and B hold. A FAIL of A or B is reported as such (it would mean my §R recomputation or my
  reading of the draft is wrong).
