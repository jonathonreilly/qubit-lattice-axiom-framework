# T50 pre-registration (written before running lee_and_sensitivity.py)

Attacker: Claude Sonnet 5.5 (same family as supervisor; same-family checks).
Chain under test (runner `scripts/frontier_dm_neutrino_atmospheric_scale_theorem.py`, main 7146fe17a7):
 y = g^2/64 (g=0.653), v = M_Pl*C*a^16 (C=(7/8)^(1/4)), M_1 = M_Pl*a^8*(1-a/2),
 m_3 = y^2 v^2/M_1, m_1 = y^2 v^2/(M_Pl a^7), Dm2_31 = m_3^2 - m_1^2, a = alpha_LM = 1/(4 pi 0.5934^(1/4)).
 Target: Dm2_31 obs = 2.453e-3 eV^2 (the runner's number). "Hit" = within 5% (the runner's own gate); also 3.5%.

## A. Which bridges carry the hit? (leave-one-out and a coefficient-light form)
Predictions:
 A1 reproduces Dm2_31 = 2.539e-3, +3.5%.
 A2 dropping k_A (any k_A >= 7) moves Dm2_31 by < 1% (m_1^2 is ~0.75% of m_3^2).
 A3 dropping eps/B (r=0) moves it by about -9%; dropping C (C=1) by about +7%; the two nearly cancel.
 A4 "geometric-mean form": M_1 := sqrt(M_Pl v) with measured v = 246.22, no alpha_LM at all:
    m_3 = y^2 v^{3/2} / M_Pl^{1/2}. Predicted Dm2 about -1.7% from 2.453e-3 (inside 5%).
 PASS reading (hit is carried by two premises: log-midpoint M_1 and y=g^2/64): A2 <1%, A4 inside 5%.
 FAIL reading (all five bridges load-bearing): A4 outside 5% or A3 individual removals both leave hit intact
 while A4 breaks.

## B. Hidden-premise sensitivities
 B1 g read at scale mu with one-loop SM g2 running (b2 = -19/6): predicted that Dm2 stays inside 5% only for
    mu within a factor ~2-3 of M_Z; at mu = M_1 it misses by a factor ~3 (Dm2 x ~0.3).
 B2 T31's unquenched plaquette shifts dP = +0.021/+0.037/+0.065 (T31 attacker's numbers, not re-derived):
    formula chain (v from alpha_LM^16) predicted to leave the 5% window; geometric-mean form with measured v
    predicted unaffected.
 B3 reduced Planck mass (2.435e18) instead of 1.2209e19: predicted Dm2 changes by a large factor (>3).
 PASS reading for "success is robust to its hidden inputs": B1, B2(formula), B3 all stay in 5%. Predicted: FAIL for all.

## C. Look-elsewhere bounds (grammar coverage)
 C1 documented-alternatives grammar (each item appears in a repo note): k_B in {7,8,9}; eps/B in {0, 0.041, a/2};
    y in {g^2/64, g^2/32, g^2/128}; C exponent in {1/4, 0, 1/2}. 81 members. Count members within 5% / 3.5% of
    the target; coverage = fraction of ln(target) in [ln(obs/10), ln(obs*10)] within 5% of some member.
 C2 y-grammar in geometric-mean form: k in 1..15 (M_1 = M_Pl^{1-k/16} v^{k/16}), y = g^a/(2^b 3^c sqrt2^d),
    a in {1,2}, b in 0..8, c in {0,1}, d in {0,1}. Count (k,y) pairs within 5% / 3.5%; coverage as above.
 Readings: coverage >= 50% => a hit at this tolerance is expected from the grammar alone (no evidence unless the
 formula was fixed before seeing the target). coverage <= 10% => the documented alternatives alone do not explain
 the hit. The unknowable history-of-tuning factor is NOT computed; only the two ends are.
 Prediction: C1 coverage small (<15%), C2 coverage large (>50%).

## Addendum after run 1 (recorded honestly)
- Run 1 (`run1_with_illegal_kA_rows.out`) had k_A = 8, 9, 100 rows that break M_A > M_B; scripting error, replaced by k_A = 6, 5, -50.
- Prediction misses: A3 "drop C moves +7%" was wrong (Dm2 ~ C^4, so +14% vs chain, +18% vs target); "eps and C nearly cancel" was wrong
  (dropping both gives +7.75% vs target). C1 coverage predicted <15%, observed 29.8% (intermediate, not "small").
- Predictions that held: A1, A4 (-1.78% vs predicted -1.7%), B1 window 74-324 GeV, B2 chain fails / geo-form unaffected, B3 huge change, C2 >50%.
