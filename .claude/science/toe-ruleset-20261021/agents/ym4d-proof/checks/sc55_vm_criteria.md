# sc55_vm — criteria (pre-registered before the script exists)

Written 2026-10-29 (UTC) by the SRCCD55 worker (claude-opus-5-5), before `sc55_vm.py` exists.

## What is tested
The numerical constants of SRCCD55 Lemma V (the single-link variance lower bound), all derived there by hand:
P_B := 2√2 e^{-1/2}/π^{3/2} (lower bound for P(|θ| ≤ κ^{-1/2}) under the von Mises law ∝ e^{κ cos θ}),
P_A := 2√2 e^{-9/2}/π^{3/2} (lower bound for P(2κ^{-1/2} ≤ |θ| ≤ 3κ^{-1/2})), c_v := P_A·P_B = 8e^{-5}/π³, and the final
constant c_v/1152. Also two elementary threshold inequalities used in the proof.

Method: exact rational interval arithmetic only. e^x for x ∈ {1/2, 9/2, 5} is enclosed by the Taylor partial sum S_n(x)
(lower) and S_n(x) + x^{n+1}/((n+1)!(1 - x/(n+2))) (upper), n = 40; e^{-x} by the reciprocals. π is enclosed by
Machin's formula π = 16 arctan(1/5) - 4 arctan(1/239) with alternating-series bounds (30 terms each). √2 and √π are
enclosed by rational bisection on squares (60 steps). No floats are used for any verdict.

## Pre-registered criteria
- **V1.** P_B ≥ 3/10 (the hand value is ≈ 0.308).
- **V2.** P_A ≥ 56/10000 (hand value ≈ 0.00564).
- **V3.** c_v = 8e^{-5}/π³ ≥ 17/10000 and the product of the certified lower bounds of P_A and P_B is ≥ 17/10000
  (hand value ≈ 0.0017385).
- **V4.** c_v/1152 ≥ 15/10^7 (hand value ≈ 1.509e-6).
- **V5.** Threshold algebra: 3/(2κ) - 2/(3κ²) - 1/κ = (3κ - 4)/(6κ²) symbolically (checked on 200 rational κ), so the
  gap δ ≥ 1/κ iff κ ≥ 4/3; and 4(1 - 2/(3κ))² ≥ 27/10 at κ = 4 (it is increasing in κ for κ > 2/3).
- **C (control; must FIRE).** The false claim c_v ≥ 18/10000 must be REJECTED by the certified upper bound (the true
  value ≈ 0.0017385 < 0.0018). FIRES iff the upper enclosure of c_v is < 18/10000.
- **Verdict.** PASS iff V1-V5 hold and C fires.
