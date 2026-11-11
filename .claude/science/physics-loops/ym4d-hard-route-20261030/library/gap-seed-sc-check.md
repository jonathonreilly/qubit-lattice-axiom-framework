lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-11T22:06Z

# gap-seed-sc-check: line-by-line check of `library/gap-seed-sc.md` (FINISH row 704)

Provenance: written by Claude Opus 5.5 (effort high), Mac mini worker 2, on branch `claude/ym4d-hard-route` at commit 95828cfbf, 2026-11-11. This is a same-provider check of a file written by another Claude model (Fable 5.2); it is not an audit and it is not an independent cross-provider check. No subagents. No numerics run unless stated below.

## Status block (kept current)

- Started 2026-11-11T10:06Z. Section order: repo search; independent hand count (before reading the author's count); verdicts one statement at a time.
- Not yet covered: everything below is filled in as it is done.

## 0. Repo search and what was read

- Read in full: `library/gap-seed-sc.md` (the file checked), `library/gap-sc-box.md` (Theorem SC, Proposition 3.6, the polymer bounds), and `library/gap-crux-restate.md` Sections 1, 3.1, 3.4 (Theorem D, Theorem S, Lemma E', Corollary S3', with the corrections of rows 698 and 699 as applied there). FINISH rows 694, 701, 704.
- Repo search: `grep -n` for `gap-seed-sc`, `seed`, `1/12800`, `12800` in `library/open-core.md`, `FINISH.md`, `library/gap-*.md`. Results in Section 0.1 below.
- Nothing fetched from the network; no numerics run (the count below is by hand; no guide run was needed).

## 1. Independent test (done before reading the author's count, Section 4 of the file)

Read before this test: only the definitions in `gap-crux-restate.md` Section 1 and Theorem D (Phi(n) = 16 F(n^4) - F((2n)^4), action sum_p (1 - (1/2) tr U_p), SU(2), Haar measure). The counts of `gap-seed-sc.md` Section 4 were not read until this section was on disk.

**Setup.** For SU(2), U = diag(e^{i t}, e^{-i t}): exp(-beta (1 - (1/2) tr U)) = e^{-beta} exp(beta cos t) = e^{-beta} c_0(beta) (1 + sum_{j >= 1/2} d_j a_j(beta) chi_j(U)), d_j = 2j + 1, with c_0 = 2 I_1(beta)/beta and d_j a_j = (2j+1) I_{2j+1}(beta)/I_1(beta) (the generating formula exp(beta cos t) = (2/beta) sum_j (2j+1) I_{2j+1}(beta) chi_j(t); RECALLED, but only its first coefficient is used and that one is a two-line check: d_{1/2} a_{1/2} = (beta/2) int (tr U)^2 dU + O(beta^3) = beta/2 + O(beta^3), so u := a_{1/2} = beta/4 + O(beta^3)). d_j a_j = O(beta^{2j}).

The factor (e^{-beta} c_0)^{#plaquettes} contributes 6|n| log(e^{-beta} c_0) to F(n); in Phi it enters as 16 * 6 n^4 - 6 (2n)^4 = 0. So Phi = 16 log Ztil(n^4) - log Ztil((2n)^4), Ztil = int prod_p (1 + sum_j d_j a_j chi_j(U_p)) dU.

**Gluing rule (by hand).** int chi_r(A U) chi_s(U^{-1} B) dU = delta_rs chi_r(AB)/d_r and int chi_r(W) chi_s(W^{-1}) dW = delta_rs give, for a closed surface of F plaquettes, Euler characteristic chi_E, every plaquette in the representation r with weight d_r a_r chi_r and every link in exactly two plaquettes: d_r^{chi_E} a_r^F. (Check: a sphere made of two discs gives sum_r d_r^2 a_r^F.) For a surface of genus 1 the term is a_r^F.

**Slab lemma (by hand).** Let P be a set of plaquettes of the torus n^4 with labels j_p >= 1/2 and non-zero Haar integral. Then every link of P is in at least two plaquettes of P (a link in exactly one plaquette integrates chi_j against Haar measure: zero). Fix mu and the slab t (the mu-links from x_mu = t to t + 1). A mu-link of the slab lies only in mu-plaquettes ((mu, nu)-plaquettes) of the same slab. Let C_t be the set of transverse links (in the transverse torus with sides n) under the mu-plaquettes of P in slab t; distinct plaquettes give distinct links. If a mu-link at the transverse vertex x is used, x has degree >= 2 in C_t. So a non-empty C_t contains a cycle of the transverse torus, of length >= min(4, n): length 3 is possible only as a straight line winding once in a direction of side 3, length 4 only as a unit square or (side 4) a straight winding line. If some slab of direction mu has C_t empty, P does not use that slab and lifts in direction mu. If this holds for every direction, P lifts injectively to Z^4 and its Haar integral equals that of the lift; such P and every cluster made of them contribute to log Ztil the same density per volume on n^4 and (2n)^4 as long as the lift of the cluster injects into both tori, and then cancel in Phi. A set that does not lift in direction mu has C_t non-empty for all n slabs, hence at least n min(4, n) plaquettes, each of order >= beta. Equality forces: all labels 1/2, no plaquette without mu, and then a transverse link of C_t at level t + 1 is covered again only by the plaquette over it in slab t + 1, so C_t = C_{t+1} = C, a single cycle of length min(4, n). A cluster on Z^4 whose lift does not inject into the torus contains two elements n e_mu apart, crosses at least n slabs of Z^4 with cycles of length >= 4 (Z^3 has no shorter cycles) and must close off, so it has at least 4n + 2 plaquettes: 14 > 9, 18 > 16, 4n + 2 > 4n. Clusters of several polymers whose union does not lift: the same slab count applies to the union (each polymer covers its own links twice), and at the minimal order each polymer would be a constant-cross-section set touching every slab, hence itself non-liftable; so at the minimal order only single polymers contribute. On (2n)^4 the minimal order is 2n min(4, 2n) = 8n > n min(4, n) for n >= 3.

**Minimal winding sets and their count.**

- n = 3 (order beta^9): C is a straight line of length 3 winding in a transverse direction nu, so P is the flat (mu, nu)-plane: 9 plaquettes, a torus, term u^9. Number of planes on 3^4: 6 orientations times 3^2 positions = 54. (Per direction mu: 3 * 9 = 27 lines, each plane found from both of its directions: 4 * 27 / 2 = 54.) Leading term: Phi(3) = 16 * 54 u^9 + O(beta^10) = 864 u^9 = (864/4^9) beta^9 = (27/8192) beta^9 + O(beta^10). [Higher orders of u give beta^11; the next set sizes give beta^10 at the earliest; this test does not determine the next order.]
- n = 4 (order beta^16): C is a unit square (a tube) or a straight line of length 4 (a plane). Tubes: 4 winding directions times 3 * 4^3 unit squares = 768, each 16 plaquettes, V = 16, E = 32, F = 16, chi_E = 0, term u^16. Planes: 6 * 16 = 96, 16 plaquettes, term u^16. Total 864 sets. Phi(4) = 16 * 864 u^16 + ... = 13824 * 4^(-16) beta^16 + ... . Planes and tubes are both counted.
- n >= 5 (order beta^(4n)): only unit squares, tubes: 4 * 3 n^3 = 12 n^3, term u^(4n) (genus 1). Phi(n) = 16 * 12 n^3 u^(4n) + ... = 192 n^3 4^(-4n) beta^(4n) + ... . For n = 5: 24000 * 4^(-20) beta^20.

**Result of the test.** A_3 = 27/8192, A_4 = 13824 * 4^(-16), A_n = 192 n^3 4^(-4n) (n >= 5), with the leading order n min(4, n). This was derived before the comparison; Section 4 below compares with the file.

**Comparison with the file (Section 4 of `gap-seed-sc.md`, read after the test above was on disk).** The file expands log E exp(beta S), S = sum_p s_p, s_p = (1/2) tr U_p, in joint cumulants; the test above expands in characters with u = a_{1/2}. The two agree at leading order: E prod_{p in M} s_p = 2^(-F) int prod chi_{1/2}(U_p) = 2^(-F) 2^(chi_E - F) = 4^(-F) for a genus-1 surface, which is the file's 4^(-ak) (Lemma 4.2), and u^F = 4^(-F) beta^F + O(beta^(F+2)). The file's two counts (through (T) and Proposition 4.4, and the direct count on n^4) both give 864, 13824, 192 n^3 times 4^(-e(n)), equal to the test. Its order e(n) = min(4n, n^2) equals the test's n min(4, n) for n >= 3 (n = 3: 9; n = 4: 16; n >= 5: 4n). At n = 4 the file's 864 = 768 tubes + 96 planes counts both kinds, and its count through (T) gets the planes as the straight lines of length 4 in cyc(B_j) (48 = 3 * 16, 64 = 2 * 32, 64 = 1 * 64, 0 for B_1 to B_4). Split check: planes 2 (8 * 48 + 4 * 64 + 2 * 64 + 0) = 2 * 768 = 1536 = 16 * 96; tubes 2 (8 * 192 + 4 * 384 + 2 * 768 + 1536) = 2 * 6144 = 12288 = 16 * 768. So the telescoped count and the direct count agree separately for planes and for tubes, not only in the total.

## 0.1 Repo search result

- `library/open-core.md`: no entry for the seed, (SEED), 12800 or a periodic strong-coupling bound. FINISH: row 701 (author), row 704 (this check), row 683 / 694 (`gap-sc-box.md` and its Codex check), rows 698 / 699 (checks of Theorem S). `ls library | grep seed` shows no other check of `gap-seed-sc.md`. No other row covers this item.
- Row 694 corrections (`gap-sc-box-check.md`, verdict table lines 485-492): 4a (q = 1 and the interior-slab list) and 8b (one fixed c in Proposition 3.6) are applied in `gap-sc-box.md`. The port uses q = 2 only, and (P) inherits the fixed-c form. So the corrected text is what was checked.

## 2. Verdicts, one per numbered statement

Legend: HOLDS = every line re-derived here; HOLDS AFTER CORRECTION gives the text; FAILS gives the line; NOT CHECKED gives the reason. Inputs taken as given (their own checks): Theorem D (a), (b), (c) of `gap-crux-restate.md` and its input (TM); Theorem S, Lemma E', Corollary S3' (rows 698, 699); SC Lemmas 2.1, 2.2, (K1)-(K3), (F1)-(F3), 3.1-3.5 (row 694). I re-read SC 2.1-2.5 and 3.1-3.6 in full for the port, and re-did the arithmetic of SC Proposition 3.6 (Steps 1-3: 0.06 |X|; (1/2)(4 e^(-0.06))^|X| >= 1; 400 * 2x <= 1/4; (8/3) x N = (32/3) |beta| N): HOLDS.

**(T), the telescoping identity. HOLDS.** With D_j = 2 F(n, B_j) - F(2n, B_j) and the axis permutation invariance of Z (F(n, 2n, n, n) = F(2n, n, n, n) etc.), 8 D_1 + 4 D_2 + 2 D_3 + D_4 = 16 F(n^4) + (-8 + 8) F(2n,n,n,n) + (-4 + 4) F(2n,2n,n,n) + (-2 + 2) F(2n,2n,2n,n) - F((2n)^4). D_j = 2 (F(n,B_j) - (1/2) F(2n,B_j)) is twice the SC quantity with k = n, q = 2. On the disc the identity holds for the branches vanishing at 0 (identity theorem from small real beta).

**(P), the port of SC Proposition 3.6. HOLDS.** Port list, entry by entry:
- SC 2.1 (K1)-(K3): no lattice. HOLDS.
- SC Lemma 2.1 (four distinct links): on a torus with every side >= 3 (>= 2 would do), the two mu-links of a (mu, nu)-plaquette differ by e_nu != 0 mod n_nu, same for the nu-links. HOLDS; the proof of SC 2.1 (a)-(c) then reads unchanged.
- SC Lemma 2.2: uses SC 2.1, (K1), (K2). HOLDS.
- SC Lemma 2.3: uses bipartiteness of Z^3; correctly replaced (Lemma 2.1 below).
- SC (F1)-(F3): only the time coordinate and the spatial position enter; the injectivity of pi on L(G_j) uses times in W_j distinct mod k and interior slabs distinct mod k, independent of B. HOLDS.
- SC Lemma 2.4, Proposition 2.5, Corollary 2.6: they use SC Lemma 2.3 only through the number 4 (in Lemma 2.4 (a), (b), the existence of t_0). Correctly replaced by Lemma 2.2, Corollary 2.3. HOLDS.
- SC Lemma 3.1: a statement on SU(2). HOLDS.
- SC Lemma 3.2: factorisation over link-disjoint components. HOLDS.
- SC Lemma 3.3 (a): on a 4-torus with sides >= 3 a mu-link lies in the (mu, nu)-plaquettes at x and x - e_nu for the three nu != mu, distinct: exactly 6; at most 4 * 5 = 20 neighbours. (b) uses only 20. HOLDS.
- SC Lemma 3.4, Corollary 3.5: abstract. HOLDS.
- SC Proposition 3.6: uses 3.1-3.5 and N; on the torus N = 6 n_1 n_2 n_3 n_4 (each site the lower corner of one plaquette in each of the 6 planes). HOLDS.

**Lemma 2.1 (a). HOLDS.** The nearest-neighbour graph of a periodic B with sides >= 3 is simple (x + e_i != x - e_i since b_i does not divide 2; x + e_i != x +- e_j for i != j). The time-like link at (x, slab t) lies exactly in the plaquettes e' x [t, t+1] with x in e', so (C) gives degree >= 2 at every used vertex, and the longest-path argument gives a cycle with >= 3 distinct vertices. Lift: end point d in b_1 Z x b_2 Z x b_3 Z; d = 0 gives even L, so L >= 4; d != 0 gives L >= |d_i| >= b_i. So L >= c_B, hence >= c_B time-like plaquettes per occupied slab and |M| >= c_B j.
**Lemma 2.1 (b). HOLDS.** d != 0: b_i <= |d_i| <= L = c_B <= b_i, so all L steps are +e_i (or all -e_i): the straight line of b_i = c_B links. d = 0: L even, so L = 4 = c_B. Four unit vectors summing to 0 form two opposite pairs; b = -a gives v_2 = v_0; d = -a gives c = -b and v_3 = v_1; so c = -a, d = -b, and b = a gives v_3 = v_1; so b is a unit vector of another direction: a unit square. (The vertex-set notation {x, ..., x + 3 e_i} for the line is unambiguous: the vertex set of a straight line determines its edges.)
**Lemma 2.1 (c). HOLDS.** The spatial link e at time t+1 lies in the spatial plaquettes at time t+1 through e and in e x [t, t+1], e x [t+1, t+2] (distinct for m >= 2), and in nothing else; (C) with no spatial plaquette at t+1 forces e x [t+1, t+2] in M.
These are the length of cycles on a periodic box: shortest cycle min(4, b_1, b_2, b_3), with the shortest ones exactly the unit squares and the straight lines through a side equal to c_B.

**Lemma 2.2. HOLDS.** (a) A short T~ (no time-like plaquette over any slab of residue t_0) lies in pi^(-1)(R(t_0)); by (F3) in one G_j; by (F1) pi is an incidence isomorphism on G_j, L(G_j), so pi T~ is good, has the same law (same word in independent Haar links), and set(pi T~) lies in R(t_0): short. (b) For a good short T with slab t_0 free, the q tuples (pi|G_j)^(-1) T are good, distinct and short (G_j has no time-like plaquette over a slab of residue t_0: its interior slabs have residues t_0 + 1, ..., t_0 + k - 1). Any good preimage is connected inside pi^(-1)(R(t_0)), so in one G_j, so equal to one of them. (c) A good set with < c_B k plaquettes occupies < k slabs (Lemma 2.1 (a)), so < k residues. The new definition of "short" makes the matching exact at every order, which is the right strengthening of SC Lemma 2.4 (n < 4k there).
**Corollary 2.3. HOLDS.** kappa_m(S) = N c_m + (good short) + W by (K3) and SC Lemma 2.2; N_(qk) = 6 qk |B| = q N_k; the matched part is q to 1 with equal kappa by Lemma 2.2 (a), (b) (a good preimage of a non-short T is non-short by (a)). The coefficient formula follows from SC Corollary 2.6's identification, which needs zero-freeness on the disc: (P). W and W~ are empty sums for m < c_B k by Lemma 2.2 (c). So the terms that do not wind cancel exactly, and the coefficients below c_B k vanish.

**The maximum-principle step (proof of Theorem 1 (iii)). HOLDS.** 16 * (32/3) |beta| * 6 n^4 + (32/3) |beta| * 96 n^4 = (32/3) * 192 |beta| n^4 = 2048 |beta| n^4, and 2048/12800 = 0.16. The -beta N + N Log c_0 terms cancel since 16 * 6 n^4 = 96 n^4. Phi = beta^e(n) h; on |z| = r < R, |Phi| <= 2048 r n^4 < 0.16 n^4, so |h| <= 0.16 n^4 / r^e(n); r -> R gives 0.16 n^4 (12800 |beta|)^e(n). At beta = R: the disc branch is real, vanishes at 0 and exponentiates to Z > 0, so it is the real log on [0, R), and continuity of the real log of the entire positive Z gives the bound at R.

**Theorem 1. HOLDS.** (i) Zero-freeness on |beta| <= R for n^4 and (2n)^4 (and for the mixed tori of (T)) is (P); real on [0, R] by (P); Phi >= 0 for beta > 0 is Theorem D (a) (uses (TM)), Phi(0) = 0. (ii) For n >= 4 every B_j has all sides >= 4, c_B = 4, order >= 4n; for n = 3, B_1, B_2, B_3 have a side 3 (c = 3, order >= 9) and B_4 = (6,6,6) has c = 4 (order >= 12). So order >= e(n) = min(4n, n^2) (9 = min(12, 9); 16 = 16; 4n < n^2 for n >= 5). (iii) the step above.

**Corollary 1'. HOLDS.** r_1 = R/2: (beta/R)^(4n) = 16^(-n) (beta/r_1)^(4n). n^4 16^(-n) is decreasing for n >= 4 ((5/4)^4 = 2.44... < 16), equal to 1/256 at n = 4; 0.16/256 = 1/1600; 1/1600 <= n^3/100. n = 3: 0.16 * 81 = 12.96.
