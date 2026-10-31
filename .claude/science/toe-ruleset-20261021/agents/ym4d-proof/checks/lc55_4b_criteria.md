# lc55_4b — criteria addendum (written after lc55_4 ran, before this script). Corrected horizontality-detector control.

lc55_4's control C4c perturbed w_2 at x = 4, where a(4 mod 3) = 0, so (Ad_{G(4)} − 1) = 0 and the perturbed vector is itself
exactly horizontal: the detector correctly read 0 and the control could not fire (a design error in the control, disclosed in
LCONV55). Corrected control C4c′: in the certified w(τ) at τ = 1/10, add 1/7 to the σ_1-component of w_1(4) only (no update of
the recursion). Expected: residual at x = 4 and x = 5 nonzero (the detector fires). Also C4c″: perturb w_2 at x = 3 (a(0) = +β,
so Ad − 1 ≠ 0 on charged components) by 1/7 in the σ_1-component. Expected: nonzero residual at x = 3.
PASS (control fired) iff both residuals are nonzero. The G4 / G4-agree verdicts are recomputed unchanged and must reproduce
lc55_4_out.txt's numbers exactly (n_2 = −2592, c_* = 2269084551038400/247334195090033).
