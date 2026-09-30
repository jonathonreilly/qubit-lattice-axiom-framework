# T07 kill-round pre-registration (Claude Sonnet 5.5, same family as attacker), written before the new tests ran

K1 (independent implementation): rebuild the two-ring Bell ensemble equation with a different code path
(kron Hamiltonian, explicit pair list). PASS = start 3 (shift) and start 6 reproduce attacker's D8, S8, CHSH to <2%.
FAIL = a bug/convention error in attacker's `common.py` (then the S and CHSH numbers are suspect).

K2 (does the noise price '7 to 10 hop rates' survive packet size?). Single walker, H = sin k sigma_z on ring L=400,
coin (cos a, sin a), Gaussian amplitude width w in {1.5, 3, 6}; wrong start = Born marginal shifted by 1.9 prob-widths
(the attacker's start 3 in packet units); Metropolis noise gamma. Read at T = 8 w (after branches separate).
Measure gamma* = smallest gamma with TV(rho_T,P_T) <= 0.1 TV(rho_0,P_0) .
Prediction (from race argument): gamma* grows roughly linearly with w. PASS of prediction = gamma*(6)/gamma*(1.5) >= 2.
If gamma* is flat in w, the attacker's '7 to 10 hop rates' is a genuine constant and my objection fails.

K3 (formation-order objection to test F2): brute-force the best (a) general DAG conditional and (b) Gibbs-note product-rule
class for the order (x1,x3,x2) against the even-parity law. Prediction: (a) distance 0, (b) > 0.
If (a) > 0 my objection fails.
