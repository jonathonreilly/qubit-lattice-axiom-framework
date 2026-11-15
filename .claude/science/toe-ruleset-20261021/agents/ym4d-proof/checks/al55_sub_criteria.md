# al55_sub — criteria (written before the script; ALIGN55.md §5.4/§6, input (SUB))

Purpose: certify, in exact rational arithmetic, that a concrete L-adic interpolatory subdivision scheme has C^{1,β} limit functions with
β > θ, for the lane's working value θ = 1/2 (BFT_A §7: α = 1/4, θ = 1/2), and record its polynomial-reproduction degree. This is input
(SUB) of the hierarchical Coulomb-detail gauge Λ_HC. Python fractions/ints only; `python3 -I -B`; stdout only.

## Schemes
- s3: ternary (L = 3) 4-point Deslauriers–Dubuc scheme: fine values at J + r/3 (r = 1, 2) by cubic Lagrange interpolation from c_{J−1..J+2},
  coarse values kept. Mask (×81): a_{−5..5} = (−4, −5, 0, 30, 60, 81, 60, 30, 0, −5, −4).
- s5: the 5-adic 4-point DD scheme (same rule at r/5, r = 1..4), mask computed in the script from the Lagrange weights.
- control lin3: ternary linear interpolation, mask (1, 2, 3, 2, 1)/3 at −2..2 (limit = hat function: C^0, not C^1).

## Method (derived in ALIGN55.md §6; standard theory)
σ_b(z) := 1 + z + … + z^{b−1}. With D^{(n)} = b^nΔc^{(n)} the first divided differences after n steps, ΔD^{(n+1)} = S_{c}ΔD^{(n)} with
c(z) := b·a(z)/σ_b(z)². If ‖S_c^n‖_∞ < b^{−nθ} for some n, then ‖ΔD^{(m)}‖ ≲ μ^m with μ := ‖S_c^n‖^{1/n} < b^{−θ}, so the limit is C^1 with
derivative Hölder exponent ≥ −log_bμ > θ. ‖S_c^n‖_∞ = max over residues r mod b^n of Σ_j|c^{[n]}_{r + b^nj}|, c^{[n]}(z) := Π_{i<n}c(z^{b^i}).

## PASS criteria
- P1: for s3, σ_3(z)^4 divides a(z) (cubic reproduction) — exact polynomial division with zero remainder; and σ_3^5 does not.
- P2: for s3, there is n ≤ 7 with ‖S_c^n‖_∞² · 3^n < 1 (certifies β > 1/2). The smallest such n and the value are printed.
- P3: for s5, σ_5^4 | a, and there is n ≤ 5 with ‖S_c^n‖_∞² · 5^n < 1. (Reported; a FAIL here is recorded, not hidden — it would mean only
  that this particular L = 5 scheme is not certified at n ≤ 5, not that no L = 5 scheme exists.)
- P4: interpolation: a_{bm} = δ_{m0} for s3 and s5.

## Controls (must FIRE)
- C1: lin3's c = 3a/σ_3² gives ‖S_c^n‖_∞² · 3^n ≥ 1 for every n ≤ 7 (no certification of C^{1,β} for a C^0 scheme).
- C2: perturbing s3's a_1 by +1/81 (breaking cubic reproduction) makes σ_3^2 ∤ a or leaves P2 uncertified — at least one of the two fails.

## What this check cannot decide
Anything about the gauge construction itself; the d = 4 tensor scheme's smoothness is inherited from the 1D factor (a product of C^{1,β}
functions), which is not re-tested; the optimal Hölder exponent is not computed (only a certified lower bound).
