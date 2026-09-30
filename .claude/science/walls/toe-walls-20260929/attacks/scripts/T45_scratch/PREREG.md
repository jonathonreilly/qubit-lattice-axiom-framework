# T45 pre-registration (written before running t45_test.py)

Wall: derive the quark CP phase delta = arctan sqrt5 (cos^2 delta = 1/6), or say why quarks have a phase at all.

Working hypothesis under test (not assumed true): the wall factorises into a DISCRETE phase
(the right angle alpha = pi/2) plus a REAL magnitude datum (R_u^2 = |V_ub|^2/(|V_us V_cb|)^2 = 1/6),
so "arctan sqrt5" is a magnitude statement, not a phase statement.

## Test A: gauge covariance of the 1+5 projector (Schur)
Build (2,3) of SU(2)xSU(3) from Kronecker products. Compute dim of commutant.
- PASS (route "1+5 is a coefficient of a gauge-invariant operator" is dead): dim = 1 (scalars only).
  Also under SU(3)_c x U(1)_em: dim = 2, and every covariant projector has diagonal entries in {0,1}
  on the weight basis (no fractional weight such as 1/6, 1/3, 1/2).
- FAIL (route alive): any covariant projector with a fractional diagonal entry.

## Test B: discrete-group phases (geometric CP violation)
- PASS (route dead for the value): cos(2 delta) = -2/3 is rational and not in {0, +-1/2, +-1}, so by
  Niven's theorem delta/pi is irrational; numerical corroboration: no p/q (q<=3000) within 1e-9.
- FAIL: delta/pi rational.

## Test C: moduli fix the phase; CP shows in CP-even data
Exact standard-parametrisation CKM from atlas (lambda^2=alpha_s/2, A^2=2/3, rho=1/6, eta=sqrt5/6, alpha_s=0.10330).
- C1 PASS: delta recovered from |V_us|,|V_cb|,|V_ub|,|V_td| alone matches input to 1e-9.
- C2 PASS (reframing supported): the two real-orthogonal completions (delta=0, pi) of the three tree
  moduli predict |V_td| differing from the atlas |V_td| by more than 30 percent. FAIL: within 10 percent.
- C3: exact right-angle residual  B11 B13 + B31 B33 - B21 B23  (B=|V|^2) at finite lambda, relative to B21 B23.

## Test D: data vs the 1/k family (looks at the wall's "cheapest test")
PDG 2024 fit: rho-bar = 0.1581+-0.0092, eta-bar = 0.3548+-0.0072 (uncorrelated propagation, an approximation);
LHCb direct gamma = 63.8 +3.5 -3.7 deg.
- Wall claim under test: "a ~1 deg gamma measurement separates 1+5 from 2+4/3+3".
- PASS (wall claim is stale): 2+4 and 3+3 already excluded > 3 sigma by the fit-derived gamma.
- Also report which k in arccos(1/sqrt k) survive (k=5,6,7 expected).

## Test E: texture route (outside-lane template: Antusch-King-Malinsky-Spinrath PRD 81, 033008 (2010))
Ensemble of hierarchical 4-zero Hermitian textures, all entries real except ONE purely imaginary element
(the (1,2) element of the up matrix). Control: same ensemble with a random phase on that element.
- PASS (route survives as a factorisation): among realistic-window samples, median |alpha-90deg| < 5 deg
  in the imaginary case AND fraction with |alpha-90deg|<5deg at least 3x the control fraction;
  and |cos(gamma) - R_u| small relative to R_u (median < 10 percent).
- FAIL: right angle not robust, or control equally good (then the pi/2 is not doing the work).

## Test F: Born-triangle lemma (proof check)
For unit u in C^6, basis vector e, p = |<e|u>|^2 = 1/6: apex = <e|u> e in the (u,v) frame has
(rho, eta) = (p, sqrt(p(1-p))), alpha = 90 deg, gamma = arctan sqrt5, r = cos delta.
- PASS: numerical identity to 1e-12. FAIL: any mismatch.

Outcome mapping: A+B PASS and C2 PASS and E PASS -> MISFRAMED (cheaper question = real magnitude datum).
If E FAILS -> STANDS (reframing still recorded, best route = record-lock Born weight). No result here can give PASSED.
