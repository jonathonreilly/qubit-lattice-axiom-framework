# nf55_b — criteria (written before nf55_b.py exists)

Owner: NONFREE55 (claude-opus-5-5). Exact symbolic arithmetic (sympy, rational coefficients; pi kept symbolic). Purpose: the
normalisation chain behind the remark "e ~ F^aF^a/(2u) at tree level" and the expected amplitude of the witness. These are
remarks ([m] inputs: the trace-anomaly formula and b0), not load-bearing for any theorem.

Conventions (pinned): s(U) = 1 - Re tr(U)/N; lane coupling u = 1/g_lane^2 is the Wilson coefficient, u = 2N/g^2 with g = g_std
(FLOW.md "Coupling variable"); U_p = exp(i a^2 g F^a t^a), t^a Hermitian, tr(t^a t^b) = delta/2;
e_a(x) = (4a^4)^{-1} sum_{mu != nu} sum_{4 clover plaquettes} s(U_p) (ROTDEF 2.2).

Gates:
- B0: for SU(2), X = theta * n.sigma/2 (unit n), Re tr(1 - exp(iX)) = 2(1 - cos(theta/2)); its Taylor coefficient of theta^2
  equals tr(X^2)/2's coefficient (1/4). PASS iff equal.
- B1: with u = 2N/g^2 and s(U_p) = a^4 g^2 sum_a (F^a_{mu nu})^2/(4N) per plaquette, u * sum_{mu<nu} s(U_p) / a^4 equals
  (1/4) sum_{mu,nu} (F^a_{mu nu})^2 identically (symbolic N, symbolic F components for 2 colours suffice).
  PASS iff the difference simplifies to 0.
  Control B1-F: with u replaced by 1/g^2 (the lane coupling misread as g_std) the difference is nonzero (FIRES if nonzero).
- B2: e_a = (4a^4)^{-1} * sum_{mu != nu} 4 s(U_p) equals (1/(2u)) sum_{mu,nu} F^a F^a identically. PASS iff difference 0.
- B3: with Theta = (beta(g)/(2g)) F^aF^a, beta = -b0 g^3, b0 = 11N/(48 pi^2) [m], Theta / e = -11 N^2/(24 pi^2) at tree level.
  PASS iff exact.
- B4: (1/(2u))^2 * 48 (N^2-1)/pi^4 equals 12 (N^2-1)/(pi^4 u^2). PASS iff exact.
Verdict: PASS iff B0-B4 pass and B1-F fires.
