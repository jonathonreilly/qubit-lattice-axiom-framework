# LSC round 2 gate: line-by-line check of the normalization repair in library/lsc.md

Referee: Claude (fresh session), 2026-11-05. One honest check, not a hostile reading. Text: library/lsc.md at 5129d8d4e (718 lines), round-2 changes only (diff 34660e272..5129d8d4e). Sources: scratchpad/sa/ca_I.tex, ca_II.tex, ym4.tex. Prior: gates/lsc-gate.md, gates/nrm-check.md.

## Notes as I go

- Read the round-2 diff hunks (git diff 34660e272 5129d8d4e), then lsc.md 1-310, 340-482, 483-540, 586-718.
- Sources read: CA-I 477-481, 924-933, 157030-157050, 157084-157130, 158119-158129, 159150-159161, 159288-159296, 159318-159336, 159410-159443, 159526-159552, 159571-159593. CA-II 728-740, 2930-2936, 25031-25043, 25231-25239, 59670-59712, 59766-59770, 59801-59835, 60368-60422, 60730-60742, 63195-63226, 63380-63394, 140880-140888, 140914-140927, 141703-141709. SA 23513-23528.
- (N1)-(N5) match CA-I 4.36 (159153-159160; 159321-159336; 159412-159443): E = sum_{j<K} E^{(j)}(T,T); E_k[empty] = sum_{j>=k}; coefficient (1/2)(d-1)D(L^d-1) = 9/2 (L^4-1) at d=4, SU(2); |r_k| <= C_r |T|_k by the geometric sum, independent of K. H=K is CA-I's own endpoint. Correct.
- (N5): -E^bare_k = E_vac + l_k - r_k. Correct algebra from (N2). Agrees with nrm-check (18).
- (N6): scaling by e^{-E_vac} commutes with every exact step (linear push-forward, partition of unity, m_{c tau}= c m_tau). Agrees with nrm-check (17) and CA-I (i-c). Correct.
- (9): CA-I 157114-157129 run with (N4) in place of the bare (h4)(a). Same proof, same E_- = C_E + C_r; this is also CA-I 4.36 (1) at 159530-159537 with proof 159571-159593, which feeds exactly E_k <= C_r|T|_k. Correct, at the standing of (h1)-(h3) and the vacuum theorem's hypotheses.
- Identification Z^J = hat Z with E = E_vac: II:737 and II:63388-63389 allow any field- and source-free E; II:2933-2935 gives mass preservation. Correct. The floor needs only the integral, not pointwise equality of the CA-I and Chapter 5 densities; the note says so (L198-199).
- Endpoint: the correlation run stops at K' = K-b <= K = H. (N4) at k = K' still gives l_{K'} >= 0 and |r_{K'}| <= C_r V_{K'}; the b omitted levels only add to l. Fine.
- Sourced side: II:25040-25043 and 25233-25238 show the initial E enters E_k^w with coefficient one. II:59801-59835 forms tilde Z = e^{-cal E} Z with E inside Z, then divides (S) by (F) on one run. II:140916-140926 identifies the correlation theorem's normalizing constant with sum_{j<K} E^{(j)}_vac, i.e. with (N2). SA 23515-23527 proves the floor for e^{-E}Z(0). All as the note says.
- Consumers: II:63474-63490 (Z = e^E Z^J, cumulants only); 63529-63565 (needs the (g,m)-dependence of E_+ and C_low through x_{K'} only); 63905-63935 (needs E_+ + C_low <= E_*, then a max over b); 64155-64184 (chessboard quotient Z(w^ch)/Z(0), same torus, same E, then (S),(F), then N^4/|C| = l^4); 64246-64283 (log Z(0) drops out; C_low "bounded above by a quantity free of m", so the consumer needs C_low uniform by itself, not only the sum); 68360-68368 (dependency list; the theorem uses probability cumulants, 66418-66430). Chapter 6's Z carries E (60368-60376) and E cancels in Z(v)/Z(0) (60412-60422).
- Floor (21): (17)-(20) unchanged from round 1 and accepted there. The new parts are (N6) for the mass and normalized (9) for the density. x A <= 3/4 V: x*48 B_3^2 s*^2 <= 48 x/(64 x*) <= 3/4. K'=0 case: -E_vac = l_0 - r_0 >= -C_r V_0 and V_0 = N^4 when K' = 0. Correct. C_low^* depends on E_-, c_H, a_1, B_3, A_0, p_0 and x^*(g) only.
- Upper (13)/(22): b_Gamma = 9/2 from (12b) = CA-I 4.36(2), 159538-159550, which bounds -E_k[S] in the vacuum convention; CA-I uses B-bar = C_beta+1 (159293, 158119-158129) and B_vac >= B-bar, so the enlargement is harmless. B_J = 9/2 + c_top > 0, so log x <= log x^* is legitimate in (22). A_J, B_J are retained construction constants with no N_T, K or level count.
- (30)-(31): signs checked. |e^{-cal E}Z_bare(w)| <= e^{E_vac + A V}, Z_bare(0) >= e^{E_vac - B V}, ratio <= e^{(A+B)V}; root over |C| cells gives (A+B) l^4 with no E_vac/|C| left. Correct.
- Round-1 rejected step (old L214, "Choose that E ... identifies this bare integral with int rho_{K'}^sf") is gone; the new L196-199, L371 and L446 say the opposite and are right. The convention-shift remark (L305-307) is stated as transport only, not as a source of estimates. No rejected item is reused.

## Report

First failing step: none.

### Findings by check item

(1) Normalized floor. Proved from inputs the account provides in that convention. (N2)-(N4) are CA-I 4.36(a) word for word, at d=4 and SU(2), with the endpoint H=K that CA-I uses. Then (h4)(a) holds for the vacuum-normalized density, and (N5) shows exactly the missing E_vac in the bare reading. (N6) carries the common scalar through every exact step. The lower member (9) is the CA-I 157114-157129 proof with (N4) inserted, and it is also CA-I 4.36(1) as printed (159530-159537, proof 159571-159593). The mass identity is (N6) plus II:2933-2935 with E=E_vac, not the bare Chapter 1 integral. The ball calculation (17)-(20) is round 1's, already accepted. The K'=0 case is handled correctly. The floor stands at the standing of (h1)-(h3), (i-c) and the vacuum theorem's hypotheses.

(2) Upper bound (13) in the same normalization. Yes. E enters the sourced exponent with coefficient one (II:25233-25238). With E=E_vac the source-free residual is E^vac_k[h], and (12b) = CA-I 4.36(2) is its vacuum-convention label bound. (13a) keeps e^{E_vac} on the bare side. The note does not rescale Z_bare <= 1, and says why not (L302). One identification is retained, not proved: the zero-source restriction of the Chapter 5 sourced format (its e^{(j)}(X;0) plus z-free logarithms) equals the CA-I one-step energies E^{(j)}. The authors make the same identification at II:140916-140926. The round-1 referee accepted (13) at the torus-bound proof's standing, so this is not a new gap.

(3) Cancellation at the four consumers. Exact at each. II:63531 (with 63474-63490) uses Z = e^E Z^J only for cumulants, plus the separate x_{K'}-dependence of E_+ and C_low. Both are now explicit in (13) and (21). II:63907-63920 uses the sum and a finite max over b. The cancellation is inside one run, and E_* is free of b. II:64272 (with 64157-64183) uses the chessboard quotient Z(w^ch)/Z(0) on one torus with one E. (31) checks the cell root with no E_vac/|C| left. This consumer also states C_low by itself is bounded free of m. The normalized (21) gives that; a bare floor would not. II:68364 is a dependency list. Its theorem uses probability cumulants and moments (66418-66477), which do not change under the scalar.

(4) Uniformity. C_low^* depends on E_-, c_H, a_1, B_3, A_0, p_0 and x^*(g). C_+^* = A_J + B_J log x^*, with B_J = 9/2 + c_top > 0 and A_J built from retained construction constants and the source budget (rho-dependent, as declared). E_* = their sum. None contains K, g_0, m_1, a, N_T, the level count or positions. E_vac is not uniform (about -(9/2) V_bare log x), and the note correctly never bounds it.

(5) Nothing rejected is reused. The old L214 identification is removed and its opposite is stated (L196-199, L371, L446). The convention-shift remark (L305-307) is restricted to transporting estimates already proved. The round-1 parts it keeps are the ones round 1 accepted.

Minor points (no effect on the proof):
- (12b) uses B_vac = max{B_sharp, C_beta+1, c_5}. CA-I's own constant is B-bar = C_beta+1 (159293), so this enlargement is harmless.
- The referee change log (L704-714) still says "in the same bare normalization" (L708). This is a record of round 1. A reader should take the Round 2 section and the Result as superseding it.
- Their text stays literally inconsistent. CA-I Definition 1.5 (929) points to the bare density of Definition 1.1, while 4.36 and II:140922 use exp[-x_0A - E]. LSC adopts the corrected reading explicitly. This is a correction to their text, and it should be credited as such in any outward note.

## Verdict

LSC is proved as their consumers need, as an implication from the account's retained inputs, in the vacuum-normalized convention e^{-E_vac}Z. Those inputs are: the CA flow and clause (0); the coefficient identification; (h1)-(h3), (i-c) and the vacuum-energy theorem's hypotheses; Balaban's real-background theorem; the correlation theorem's construction; and the eight retained sourced upper hypotheses. With round 1's accepted parts, (a)-(e), (5), (23) and the finite-torus completion (29) hold. E_vac cancels exactly at II:63531, 63907-63920, 64272 and 68364.

For clause (iii-b): its last open input, the last-scale floor and uniform constants, is now closed at the account's standing. So (iii-b) is no longer blocked by LSC. It stands where its upstream inputs stand: the correlation theorem's outstanding window-data statement (II:2810-2812), the eight sourced upper hypotheses, and the RG representation and vacuum hypotheses. This is a check of an implication. It grants no status and proves no upstream hypothesis. Frozen o4-two-point.md can cite (iii-b) at that standing, with the normalization correction named.

Checked line by line by Claude (fresh session).
