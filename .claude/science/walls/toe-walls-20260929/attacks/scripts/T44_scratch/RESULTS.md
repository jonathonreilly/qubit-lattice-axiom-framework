# T44 results (see results.txt / results.json; script t44_test.py, seed 44, N=400000)

Deviations from PREREG.md (recorded, not hidden):
- Run 1 had a Cyrillic letter in a variable name; renamed, numbers unchanged.
- S1b (joint chi2 of lambda, A, rho_bar, eta_bar; Thales check on data) was added after run 1 and
  is not pre-registered.
- S2 pre-registered reading ("MS-bar alpha_s(v) more than 3% off -> fit depends on the lattice number")
  was NOT triggered: MS-bar 2-loop alpha_s(v) from alpha_s(MZ)=0.1180 is 0.10313 vs plaquette 0.10330.

Readings against the pre-registered rules:
- S1 Reading A triggered: lambda pull +3.32 sigma (atlas 0.22727 vs 0.22501+-0.00068). Joint chi2 of
  (lambda, A, rho_bar, eta_bar) = 13.74, 4 dof, p = 0.008; with a 1% theory error on lambda chi2 = 3.62 (p = 0.46).
- S3 triggered: n=3 in place of n=6 gives |Vub| +48% (+20 sigma) and delta 54.7 deg (-7.4 sigma).
- S4: on the tied S_SM grammar at tau = 3% (lambda tolerance = tau) p = 8e-5 (broad prior) and 5e-4 (jitter prior):
  below 0.01, so "evidence, worth deriving". On S_6 tied: 7e-4 / 5e-3. On S_12 tied: 4e-3 / 1.6e-2.
  Independent-slot (no Thales tie) S_12: 0.028 / 0.095. Range across all rows at tau <= 5%: 1e-5 to 0.42
  (the 0.42 is S_12, jitter, tau 5%, lambda 10%, independent slots - the loosest case).
  The "no evidence" alternative is not supported except for the loosest grammar and tolerance.
- S5 not triggered: max min(|V_ij|,1-|V_ij|) = 6.8e-13 over 1000 commuting pairs.
- S6: reading of the runner - 1/6 is hard-coded as 1/QUARK_BLOCK_DIM (lines 141-143); delta_A1 only in
  scalar-compare outputs. K_R / 13^3 Green function is not load-bearing for the leading-order numbers.
