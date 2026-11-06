lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T17:20Z

# p6a-check: library/port/p6-correlation.md, first half (5.6:lem-weight, 5.5:lem-weight, 5.3:lem-driven-flow)

Status: in progress (started 2026-11-06T05:20Z). Sections are written as the check proceeds.

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker, fresh session. Repository commit b05bc0e47. Source: CA-I and CA-II fetched by raw URL at upstream 31a47c543775 (sha256 of CA-II 6a1f74b05f74...4b2b8f; 145,624 lines). One reading, not an audit, not human review.

## Quotation check (all three statements)

Every fenced `latex` block of the port in its first half (port lines 24-2634) was compared line by line with CA-II by a plain text comparison. All 17 blocks are exact copies of the source:

| Port lines | CA-II lines | Content |
|---|---|---|
| 24-169 | 45154-45299 | 5.6:lem-weight statement |
| 177-457 | 35258-35538 | 5.5:lem-weight statement |
| 648-678 | 26201-26231 | 5.3:lem-driven-flow statement |
| 750-815, 831-883, 891-951, 961-1069, 1079-1188 | 45301-45366, 45425-45477, 45583-45643, 45774-45882, 46020-46129 | 5.6 proofs (a), (b), (c), (d), (e)-(f) |
| 1223-1306, 1314-1429, 1439-1725, 1741-1953, 1961-2194, 2206-2517 | 35543-35626, 35628-35743, 35748-36034, 36037-36249, 36251-36484, 36486-36797 | 5.5 proofs (a1)-(a2), (a3)-(a4), (b), (c), (c')-(d), (e) |
| 2543-2634 | 26233-26324 | 5.3 proof |

So the check below is a check of the account's own proofs as ported, plus the port's annotations (fills, corrections, input tables). A text comparison is a check of quotation only; it proves nothing about the mathematics.

## B2a: 5.6:lem-weight (port lines 19-169, 733-1188)

Kind: check of their proof. Verdict: **faithful; proved as an implication from its named inputs.** First failing step: none.

What I redid by hand:

- (a), CA-II 45301-45366. The slice G_s is continuous and separately holomorphic on P_W(e^{kappa_1}) with |G_s| <= b, since [0,1]^{V\W} x P_W(e^{kappa_1}) lies in P_V(e^{kappa_1}). Lemma 5.6:lem-cauchy-estimates (45008-45152; I reread its proof: iterated Cauchy formula by induction on |W| with Fubini, then differentiation under the integral, then r_w -> R) gives |d^W F_t| <= b r(kappa_1)^m on the real cube. The probability measure costs 1. The supremum over data is taken last, so no datum regularity is used. Lemma 5.6:lem-cauchy-factor (44941-45006): x/(x-1)^2 <= e/x for x >= e reduces to x(sqrt e - 1) >= sqrt e, increasing in x, and at x = e to (e-1)^2 >= e, true since e > 8/3 > 21/8 > (3+sqrt 5)/2. Correct.
- (b), 45425-45477. (pi1) gives |W(p)| = n; (pi2) gives at most lambda^n pieces (ordered partitions = maps N' -> I). With r <= 1 the sum is <= b (lambda r)^n. The two floors are the stated logarithms. Correct.
- (c), 45583-45643. (pi3) gives exactly the hypotheses of (TL)_{c'} with Y_1 = Y_1(t), so l(Y) <= l(Y_1) + c'n, and -a l(Y_1) <= -a l(Y) + a c' n. Combined with (b) this is the first inequality of (5.6:eq-weight-d); the floor is the stated logarithm. The comparison 16 kappa + 1 >= 1 + log 3 + 8 kappa iff 8 kappa >= log 3 is right, and it covers the c' = 1 case too (14 kappa >= log 3). The "a <= 2 kappa" reading needs beta <= 1/3, which the statement writes as a hypothesis ("With lambda = 3, a <= 2 kappa ..."), so nothing is claimed beyond it.
- (d), 45774-45882. The rooting argument is right: a path in Y from a cell of a component C_i of A = Y \ Y_1 to Y_1 leaves C_i first into Y_1, so each C_i meets the outer boundary of Y_1, and the least such cell roots C_i. The code (root set, sizes, rooted components) is injective. Counts: at most 2^{D_d #Y_1} root sets, at most C(n-1,q-1) <= 2^{n-1} size vectors, at most (4 D_d)^{m_s - 1} rooted connected sets each (5.6:lem-rooted-sets, 45645-45701: depth-first walk, a word of 2(m-1) up/down letters and m-1 neighbour ranks; the parent on an up-step is the cell before the first visit, so the code determines C). Product <= 2^{D_d #Y_1}(8 D_d)^n. Geometric series <= 2 when kappa_1 >= 1 + log(16 lambda D_d). Prefactor: 5.6:lem-tree-cells (45703-45772) gives #Y_1 <= 3^d(2 d^fr + 1) <= 3^d(2 d^sub + 1), so 2^{D_d #Y_1} <= e^{c''_d} e^{2 c''_d l(Y_1)}, and e^{-(a - 2c'')l} <= e^{-(1-eps) a l} iff eps a >= 2 c''. All correct.
- 5.6:lem-tree-length-adjunction (45479-45581), read for (TL)_{c'}: breadth-first order from Y_1; (i) each new cell is joined by a coordinate-monotone path of at most dM bonds (each coordinate of the nearest site moves by at most M, since |a_mu - a'_mu| <= 1); (ii) under face adjacency a path of at most M-1 bonds inside the old cell plus one bond across the shared face, all inside the union. Correct. No claim for d^sub under closure-touching, as the source says.
- (e)-(f), 46020-46129. The bound: F_y is the product-form piece with W = y and base point 0, so (a) applies; for the second choice of N(F), d^y kills the constant F(1;d) when y is nonempty. The identity: E^1 = E^0 + I in each coordinate, operators of distinct cells commute on C^infinity of the closed cube (Clairaut, Fubini), expand the product, and the y-summand is F_y. Correct. (f) is a reading of the constants of (a)-(e) and the five lemmas; I found no other parameter.

Port annotations:

- **W6-C1 (port line 954) is a correct correction.** CA-II 45597-45598 says that l(Y_1(t)) = infinity "forces b = 0". That holds only for a > 0. For a = 0 the factor e^{-a l} must be read as 1 on both sides, and then (c) is (b). The repair changes no constant.
- W6-F1, W6-F2, W6-F3 are correct fills of steps the source writes out.
- Input table (port lines 735-743): loci checked. B1 = 5.6:prop-polydisc-holomorphy (46131-46165) is "Proof outstanding" at 46167, as the port says, and (H_o) is a hypothesis of the lemma, not a consequence of anything proved. (pi1)-(pi3) are hypotheses by the source's own words at 44846-44847 ("They are not proved here and enter as hypotheses wherever they are used").

One cosmetic point, not a failing step: 5.6:def-linear-sizes defines a "tree graph" as any finite connected subgraph, not an acyclic one, and the proof of 5.6:lem-tree-cells says the depth-first walk crosses "each bond of T ... once in each direction". For a T with a cycle that is false, but walking a spanning tree gives at most 2|T| steps and the same bound. The consequence (the only use, in (d)) takes an optimal T, which is acyclic. Nothing changes.
