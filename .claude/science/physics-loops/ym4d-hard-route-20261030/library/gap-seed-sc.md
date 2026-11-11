lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-11T21:40Z

# gap-seed-sc: the seed on a strong-coupling disc (FINISH row 701)

Provenance: one session, Claude Fable 5.2 (medium), Mac mini worker 1, commit 87f777e7a, started 2026-11-11T09:40Z. Written step by step. Not checked by another model. No computer run was made; every step is by hand.

**No mass gap at a coupling of order one is proved by this file.** The seed is proved only for beta below 1/12800.

## Status block (kept current)

- Section 0 (repo search, duplicate check): written.
- Section 1 (statements): written.
- Section 2 (step 1 and step 5: the torus port of `gap-sc-box.md`, the cancellation): written.
- Section 3 (step 2: the bound; the correction at n = 3): written.
- Section 4 (the exact leading term; test of the guess p = 3): written.
- Section 5 (step 3: the seed size): written.
- Section 6 (step 4: the gap bound from Theorem S against the rate 4 log 2): written.
- Section 7 (final status): written.

## 0. Repo search, duplicate check, sources

- Duplicate check. `library/open-core.md` has no entry for the seed, for (SEED), for Phi or for a strong-coupling expansion on the periodic torus (grep for seed, strong coupling, SC_B, winding, Phi(n: one unrelated hit, line 524). In the FINISH rows the seed on the strong-coupling disc is owned by row 701 only. Row 683 (`gap-sc-box.md`) owns the box with free walls. Rows 698, 699 check Theorem S. Row 700 (`gap-seed-limit.md`, line 272) says that row 701 treats strong coupling. No other row covers this item.
- Repo search. `library/gap-sc-box.md` (row 683, Claude Opus 5.5; checked by Codex gpt-6-astra, row 694) has every tool that is needed, for a spatial set B in Z^3 with free walls. Its Remark after Lemma 2.3 says that a spatial torus of side 3 breaks the count. That remark is the source of the correction at n = 3 below. `library/gap-skeleton-max-b.md` line 305 states (SC) for the torus as an input, with no proof. No file in `library/` proves a strong-coupling bound for the fully periodic torus.
- What this file reuses and does not redo: Sections 2.1, 2.2, 2.3, 2.5 and Section 3 of `gap-sc-box.md`, cited by number with the prefix SC (for example SC Lemma 2.4). Section 2 below says, line by line, which of these statements use the free walls. Only SC Lemma 2.3 does.
- Sources. Sussman and Alpoge with Claude and Codex: their general polymer theorem (`YM4_sketch_500.tex` at 31a47c543775, lines 1150-1174 and 1271-1347, as recorded in `gap-sc-box.md` Section 0) is a tool of the same kind as SC Section 3. It is not used here, and their text does not treat this object. Osterwalder and Seiler (the strong-coupling expansion; recalled, not read). Münster (the strong-coupling glueball mass, 4 log(4/beta) at leading order for SU(2); RECALLED, not read; used only as the known answer in the test of Section 6, in no proof). `library/gap-crux-restate.md` (row 697, Claude Fable 5.2 max): Phi, Theorem D, Theorem S, Corollary S3' (Codex gpt-6-astra, row 699).

## 1. Statements

Notation. For n >= 3, the torus n^4 is (Z_n)^4 with the Wilson SU(2) action A = sum over plaquettes of a_p, a_p = 1 - s_p, s_p = (1/2) tr U_p. Z(n_1, ..., n_4; beta) is the integral of exp(-beta A) over product Haar measure, entire in beta. F = log Z. Phi(n; beta) = 16 F(n,n,n,n) - F(2n,2n,2n,2n). R = 1/12800 (the radius of Theorem SC). Put

e(3) = 9 and e(n) = 4n for n >= 4. So e(n) = min(4n, n^2).

**Theorem 1 (the seed bound; PROVED GIVEN Theorem SC's lemmas, which are checked in row 694, and the port Lemmas 2.1 to 2.4 below).** For every n >= 3:
(i) Z(n,n,n,n; beta) and Z(2n,2n,2n,2n; beta) have no zero in |beta| <= R. With the branches of the logarithm that vanish at 0, Phi(n; .) is analytic on |beta| < R, and real and non-negative on [0, R].
(ii) Phi(n; .) has a zero of order at least e(n) at beta = 0.
(iii) |Phi(n; beta)| <= 0.16 n^4 (12800 |beta|)^e(n) for |beta| < R, and for real beta in [0, R].

**Corollary 1' (the form of the row; PROVED GIVEN the same).** For n >= 4 and 0 <= beta <= r_1:
- with r_1 = 1/12800: Phi(n; beta) <= 0.16 n^4 (beta/r_1)^(4n) (C = 0.16, p = 4);
- with r_1 = 1/25600: Phi(n; beta) <= (1/100) n^3 (beta/r_1)^(4n) (C = 1/100, p = 3), and also Phi(n; beta) <= (1/1600) (beta/r_1)^(4n) (p = 0).
For n = 3 and 0 <= beta <= 1/12800: Phi(3; beta) <= 12.96 (12800 beta)^9.

**Theorem 2 (the target of the row is false at n = 3; the exact leading term; PROVED GIVEN the same).** As beta tends to 0, Phi(n; beta) = A_n beta^e(n) + O(beta^(e(n)+1)) with

A_3 = 27/8192, A_4 = 13824 x 4^(-16), A_n = 192 n^3 4^(-4n) for n >= 5.

So the order e(n) of Theorem 1 (ii) is exact. For n = 3 no constants C, p and r_1 give Phi(3; beta) <= C 3^p (beta/r_1)^12 on an interval (0, r_1]: the left side is of exact order beta^9. The smallest set that winds on the torus 3^4 is a plane of 9 plaquettes, not a tube of 12. For n >= 4 the row's exponent 4n is right, and the author's guess p = 3 is the exact power of n in the leading term.

**Theorem 3 (the seed; PROVED GIVEN the same).** Let 0 < beta < 1/12800, theta = 12800 beta and lambda = log(1/theta). Then Phi(n; beta) <= 1.9 x 10^(-4) for every n >= 4 with n theta^n <= 0.18, and in particular for every

n >= n_seed(beta) := max(4, (2/lambda) log(4.1/lambda)).

Special cases: n = 3 for beta <= 1/51200; n = 5 for beta <= 1/25600.

**Theorem 4 (the gap that follows; PROVED GIVEN Theorem S and Corollary S3' of `gap-crux-restate.md`, checked in rows 698 and 699, and their input (TM)).** Let 0 < beta < 1/12800 and n >= max(4, n_seed(beta)). Then every periodic cube of integer side L >= 2n has

m(L^3) >= 4 log(1/(12800 beta)) - (4 log n + log 1614)/n.

So liminf over L of m(L^3) >= 4 log(1/(12800 beta)). At beta = 1/25600 this is 4 log 2, the rate kappa_0 of `gap-sc-box.md`. Theorem S loses nothing in the exponential rate against the bound it is fed.

## 2. Step 1 and step 5: the expansion on the periodic torus, and the cancellation

### 2.1 The one-direction form

Let B = Z_(b_1) x Z_(b_2) x Z_(b_3) be a periodic spatial box with all b_i >= 3. Its spatial links are the pairs {x, x + e_i}, and its spatial plaquettes are the unit squares, all read with periodic coordinates. For k >= 3, Lambda_k = B x Z_k is the four-dimensional torus (k, b_1, b_2, b_3), with the plaquettes and the time-like links of `gap-sc-box.md` Section 1. Write Z(k, B; beta) for its partition function, and

c_B := min(4, b_1, b_2, b_3), which is 3 or 4.

The telescoping identity. For n >= 3 put B_1 = (n,n,n), B_2 = (2n,n,n), B_3 = (2n,2n,n), B_4 = (2n,2n,2n), and D_j := 2 F(n, B_j) - F(2n, B_j), where the first argument is the side of the direction that is doubled at step j. Z is invariant under a permutation of the axes. So

(T) Phi(n) = 8 D_1 + 4 D_2 + 2 D_3 + D_4.

Check: 8 (2 F(n,n,n,n) - F(2n,n,n,n)) + 4 (2 F(2n,n,n,n) - F(2n,2n,n,n)) + 2 (2 F(2n,2n,n,n) - F(2n,2n,2n,n)) + (2 F(2n,2n,2n,n) - F(2n,2n,2n,2n)) = 16 F(n,n,n,n) - F(2n,2n,2n,2n).

Each D_j is twice the quantity D = log Z(k) - (1/q) log Z(qk) of Theorem SC, with k = n, q = 2, and the periodic box B_j in place of a box with free walls. So step 1 of the row is the port of Theorem SC to a periodic B. This is the statement that `gap-sc-box.md` does not have (step 5 of the row).

### 2.2 The port: which statements of `gap-sc-box.md` use the free walls

I read each statement of SC Sections 2 and 3 for its use of B.

- SC 2.1, (K1) to (K3): no lattice.
- SC Lemma 2.1 uses that the four links of each plaquette are distinct. On Lambda_k with k >= 3 and all b_i >= 3 this holds: a plaquette in the plane (mu, nu) at x has the links (x, mu), (x + e_mu, nu), (x + e_nu, mu), (x, nu). The two mu-links differ because e_nu is not 0 mod the side of nu, and so for the two nu-links. The proof is then unchanged.
- SC Lemma 2.2: uses SC Lemma 2.1 and (K1), (K2) only.
- SC Lemma 2.3: uses the free walls (bipartite graph in Z^3). It is replaced by Lemma 2.1 below.
- SC 2.5, (F1) to (F3): they use only the time coordinate and that pi keeps the spatial position. Unchanged.
- SC Lemma 2.4, Proposition 2.5, Corollary 2.6: they use SC Lemma 2.3 through the number 4 only. They are replaced by Lemma 2.2 and Corollary 2.3 below, with c_B in place of 4.
- SC Lemma 3.1: one plaquette. Unchanged.
- SC Lemma 3.2: uses that the links are independent and that two components share no link. Unchanged.
- SC Lemma 3.3 (a): on Lambda_k every link of direction mu lies in exactly two plaquettes for each of the three other directions nu (at x and at x - e_nu, distinct because every side is at least 3). So a link lies in exactly 6 plaquettes, and a plaquette has at most 4 x 5 = 20 neighbours. The statement holds. (b) follows from (a) as written.
- SC Lemma 3.4, Corollary 3.5: abstract. Unchanged.
- SC Proposition 3.6: uses SC Lemmas 3.1 to 3.5 only. So it holds for every four-dimensional torus with all sides at least 3:

**(P) (the port of SC Proposition 3.6; PROVED GIVEN SC Lemmas 3.1 to 3.5).** Let Lambda be a torus with sides n_1, ..., n_4 >= 3, with N = 6 n_1 n_2 n_3 n_4 plaquettes, and |beta| <= R = 1/12800. Then Z(Lambda; beta) is not 0. The function log Z = -beta N + N Log c_0(beta) + log Xi(beta) is analytic on |beta| < R, vanishes at 0, is real on the real segment, satisfies exp(log Z) = Z, and |log Xi(beta)| <= (32/3) |beta| N.

N = 6 |Lambda| because each site is the lower corner of one plaquette in each of the 6 planes.

### 2.3 The count on a periodic box

**Lemma 2.1 (replaces SC Lemma 2.3; PROVED).** Let m >= 3, B periodic with all sides at least 3, and let M be a set of plaquettes of Lambda_m with property (C) of SC 2.3. Suppose M has a time-like plaquette over slab t. Let G_t be the graph on B with an edge e exactly when e x [t, t+1] is in M. Then:
(a) G_t contains a cycle, and every cycle of the nearest-neighbour graph of B has length at least c_B. So M has at least c_B time-like plaquettes over slab t. If M has time-like plaquettes over j slabs, then |M| >= c_B j.
(b) A cycle of length exactly c_B in B is one of these: for c_B = 4, the boundary of a unit square, or a straight line {x, x + e_i, x + 2 e_i, x + 3 e_i} in a direction with b_i = 4; for c_B = 3, a straight line {x, x + e_i, x + 2 e_i} in a direction with b_i = 3.
(c) If M has no spatial plaquette at time t+1, then G_(t+1) contains G_t.

Proof. (a) The nearest-neighbour graph of B is simple, because every side is at least 3: x + e_i and x - e_i differ, and x + e_i = x + e_j or x - e_j only for i = j. As in SC Lemma 2.3, the time-like link at (x, slab t) lies exactly in the plaquettes e' x [t, t+1] with x in e'. So by (C) every vertex of G_t that meets an edge has degree at least 2, and the longest-path argument of SC Lemma 2.3 gives a cycle of length at least 3 with distinct vertices.
Let v_0, v_1, ..., v_L = v_0 be a cycle with distinct vertices v_0, ..., v_(L-1) and L >= 3. Each step is +e_i or -e_i mod the sides. Lift it to a walk in Z^3 from 0 with the same steps. Its end point d lies in b_1 Z x b_2 Z x b_3 Z. If d = 0, the lift is a closed walk in Z^3. Then L is even (parity of the coordinate sum), so L >= 4. If d is not 0, some coordinate of d has absolute value at least b_i, and each step changes one coordinate by 1, so L >= b_i. So L >= min(4, b_1, b_2, b_3) = c_B.
(b) Let L = c_B. Case d not 0: then L >= b_i for the coordinate i with d_i not 0, and L = c_B <= b_i, so b_i = c_B, |d_i| = L, and all L steps are in the direction i with one sign. This is the straight line. Case d = 0: then L is even, so L = 4 = c_B. A closed walk of 4 steps in Z^3 with 4 distinct vertices mod the sides: the steps are unit vectors a, b, c, d with a + b + c + d = 0. A sum of four unit coordinate vectors is 0 only if they form two pairs of opposite vectors, so -a is one of b, c, d, and the other two are opposite. If b = -a, then v_2 = v_0, excluded. If d = -a, then c = -b and v_3 = v_0 + a = v_1, excluded. So c = -a and d = -b. Here b is not -a (done), and b is not a (then the steps are a, a, -a, -a and v_3 = v_1, excluded). So b is a unit vector of another direction, and the walk a, b, -a, -b is the boundary of a unit square.
(c) Let e be an edge of G_t. The spatial link e at time t+1 is a link of e x [t, t+1]. It lies in the spatial plaquettes at time t+1 that contain e, in e x [t, t+1] and in e x [t+1, t+2], and in no other plaquette. By (C) and the hypothesis, e x [t+1, t+2] is in M. QED

**Lemma 2.2 (replaces SC Lemma 2.4; PROVED GIVEN SC (F1) to (F3), SC Lemmas 2.1, 2.2).** Let k >= 3, q >= 1, B periodic with sides at least 3, pi: Lambda_(qk) -> Lambda_k as in SC 2.5. Call a good tuple T of Lambda_k short if set(T) has no time-like plaquette over some slab t_0. Call a good tuple T~ of Lambda_(qk) short if set(T~) has no time-like plaquette over any slab of some residue t_0 mod k. Then for every length:
(a) if T~ is good and short, then pi(T~) is good and short, and kappa(pi T~) = kappa(T~);
(b) every good short T has exactly q good preimages, and each of them is short.
(c) Every good tuple of length less than c_B k, of Lambda_k or of Lambda_(qk), is short.

Proof. (a) and (b) are the proofs of SC Lemma 2.4 (a) and (b) from the point "some t_0 is not among them" on. Those lines use only (F1) to (F3) and the choice of t_0. In (a), set(pi T~) lies in R(t_0), so pi T~ is short. In (b), each preimage lies in one G_j, which has no time-like plaquette over a slab of residue t_0. (c) By Lemma 2.1 (a), a set with fewer than c_B k plaquettes has time-like plaquettes over fewer than k slabs. In Lambda_(qk) these have fewer than k residues. QED

**Corollary 2.3 (the cancellation; replaces SC Proposition 2.5 and Corollary 2.6; PROVED GIVEN the same and (P)).** Let W_k(m) be the sum of kappa(T) over the good tuples T of length m of Lambda_k that are not short, and W~_(qk)(m) the same sum for Lambda_(qk). Then for every m >= 1

kappa_m(S_(qk)) - W~_(qk)(m) = q (kappa_m(S_k) - W_k(m)).

On the disc |beta| < R, D = log Z(k, B) - (1/q) log Z(qk, B) has the Taylor coefficients

[beta^m] D = (1/m!) (W_k(m) - (1/q) W~_(qk)(m)) for m >= 1, and D(0) = 0.

These vanish for m < c_B k.

Proof. By (K3) and SC Lemma 2.2, kappa_m(S_k) = N_k c_m + (sum over good short T) + W_k(m), and the same for qk. N_(qk) = q N_k. By Lemma 2.2 (a), (b) the map T~ -> pi T~ is exactly q to 1 from the good short tuples of Lambda_(qk) onto the good short tuples of Lambda_k and keeps kappa. This gives the first identity. The Taylor coefficients are those of SC Corollary 2.6: the coefficient of beta^m in log Z(m') is kappa_m(S_(m'))/m! - N_(m') [m = 1], and the terms with N cancel. By Lemma 2.2 (c), W and W~ are empty sums for m < c_B k. QED

**What step 1 of the row asked, in words.**
- Terms of the small torus that are not terms of the large one: the good tuples of Lambda_k whose plaquette set has a time-like plaquette over every slab of the doubled direction. Such a set winds around that direction. A good preimage of such a tuple, if it has one, is not short either, so it is counted in W~ and not in the matched part.
- The converse: terms of the large torus that are not lifts of terms of the small one are the good tuples whose set has a time-like plaquette over a slab of every residue mod k. Its image in the small torus overlaps itself or closes up.
- All other terms cancel exactly in each D_j, to every order (Corollary 2.3). This is exact, not an estimate.
- The smallest size at which the cancellation fails is c_B k plaquettes: for Phi(n) this is e(n) = 9 for n = 3 and 4n for n >= 4. Theorem 2 shows that it does fail at that size, with a positive coefficient.

**Proof of Theorem 1 (i), (ii).** (i) is (P) for the tori n^4 and (2n)^4. Phi >= 0 for real beta is Theorem D (a) of `gap-crux-restate.md` (Lemma A there); for beta = 0 it is 0. (ii) By (P) every F in (T) is analytic on the disc, and (T) holds there because it holds for the branches that vanish at 0. For n >= 4 every B_j has c_B = 4, so every D_j vanishes to order 4n (Corollary 2.3 with k = n, q = 2; D_j = 2D). For n = 3, B_1, B_2, B_3 have a side 3, so c_B = 3 and the order is at least 9; B_4 = (6,6,6) has c_B = 4 and order at least 12. QED
