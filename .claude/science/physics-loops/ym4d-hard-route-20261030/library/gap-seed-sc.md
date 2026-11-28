lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-11T21:40Z

# gap-seed-sc: the seed on a strong-coupling disc (FINISH row 701)

Provenance: one session, Claude Fable 5.2 (medium), Mac mini worker 1, commit 87f777e7a, started 2026-11-11T09:40Z. Written step by step. Checked line by line by Claude Opus 5.5 high (FINISH row 704, `library/gap-seed-sc-check.md`, 2026-11-11): every numbered statement holds; two remarks, no correction (lead note). Not checked by a model of another provider. No computer run was made; every step is by hand.

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
The sign Phi >= 0 in (i) is Theorem D (a) of `gap-crux-restate.md` and uses its input (TM). Nothing else in Theorems 1 to 3 uses (TM).

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

**Theorem 4 (the gap that follows; PROVED GIVEN Theorem S and Corollary S3' of `gap-crux-restate.md`, checked in rows 698 and 699, and their input (TM)).** Let 0 < beta < 1/12800, theta = 12800 beta, and n >= 4 with n theta^n <= 0.18 (for example n >= n_seed(beta), or n = 5 for beta <= 1/25600). Then every periodic cube of integer side L >= 2n has

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

## 3. Step 2: the bound

**Proof of Theorem 1 (iii).** By (P), on |beta| < R each of the two logarithms is -beta N + N Log c_0 + log Xi. The torus n^4 has N = 6 n^4 plaquettes and the torus (2n)^4 has 96 n^4 = 16 x 6 n^4. So the terms -beta N + N Log c_0 cancel exactly in Phi, and

|Phi(n; beta)| <= 16 (32/3) |beta| 6 n^4 + (32/3) |beta| 96 n^4 = 2048 |beta| n^4 < 2048 n^4 / 12800 = 0.16 n^4.

Phi is analytic on the disc with a zero of order at least e(n) at 0 (Theorem 1 (ii)). So Phi = beta^e(n) h with h analytic. For |beta| < r < R the maximum principle gives |h(beta)| <= 0.16 n^4 / r^e(n). Let r tend to R:

|Phi(n; beta)| <= 0.16 n^4 (|beta|/R)^e(n) = 0.16 n^4 (12800 |beta|)^e(n).

This is the Schwarz step of SC Section 4. At real beta = R the bound holds by continuity: Z is entire and positive on the real axis, so F and Phi are continuous there. QED

**Proof of Corollary 1'.** The first line is Theorem 1 (iii) with e(n) = 4n. For r_1 = R/2: (beta/R)^(4n) = 16^(-n) (beta/r_1)^(4n). The sequence n^4 16^(-n) decreases for n >= 4, because ((n+1)/n)^4 <= (5/4)^4 < 16. At n = 4 it is 256/65536 = 1/256. So 0.16 n^4 16^(-n) <= 0.16/256 = 1/1600, which gives the form with p = 0. The form with p = 3 follows from 1/1600 <= n^3/100. For n = 3: 0.16 x 81 = 12.96. QED

Remark on p. With a radius that is not sharp, the power p carries no information: a smaller r_1 absorbs any power of n. The power of n has a meaning only in the leading term, and there it is 3 (Theorem 2).

**Defect of the row's target, with the explicit failure.** The row asks for the exponent 4n for every n >= 3. At n = 3 this is false (Theorem 2, Section 4): Phi(3; beta)/beta^9 tends to 27/8192 > 0, and C 3^p (beta/r_1)^12 / beta^9 tends to 0. The reason is the remark after SC Lemma 2.3: on a periodic side of length 3 a straight line of 3 links is a cycle. The plane that this line sweeps in a second direction of side 3 is a closed surface of 9 plaquettes. A tube has 12. The corrected statement is Theorem 1 with e(n) = min(4n, n^2). The same correction applies to item 2 of the list in `gap-crux-restate.md` (line 363), which states the bound for n >= 3; I did not edit that file.

## 4. The exact leading term (test of the guess p = 3)

This section is not needed for Theorems 1, 3 and 4. It proves Theorem 2.

**Lemma 4.1 (two Haar integrals; PROVED).** For 2 x 2 complex matrices A, B and Haar measure on SU(2):
(O1) the integral of tr(A U) tr(U^(-1) B) is (1/2) tr(A B);
(O2) the integral of tr(A U B U^(-1)) is (1/2) tr A tr B.
Proof. For a matrix X put M(X) = integral of U X U^(-1). By invariance of Haar measure, M(X) commutes with every element of SU(2). The elements 1, i sigma_1, i sigma_2, i sigma_3 of SU(2) span all 2 x 2 matrices, so M(X) is a scalar matrix, and its trace is tr X. So M(X) = (1/2)(tr X) 1. (This is the step that Lemma J of `gap-crux-restate.md` uses.) (O2): the integral is tr(A M(B)). (O1): tr(AU) tr(U^(-1) B) = sum over i, j, k, l of A_ij U_ji (U^(-1))_kl B_lk, and U_ji (U^(-1))_kl = (U E_ik U^(-1))_jl with E_ik the matrix unit. Its integral is (1/2) delta_ik delta_jl. The sum is (1/2) sum of A_ij B_ji. QED

**Lemma 4.2 (the moment of a tube or a plane; PROVED GIVEN Lemma 4.1).** Let k >= 3, and let gamma be a cycle in B with a >= 3 distinct vertices u_0, ..., u_(a-1) and edges e_x = {u_x, u_(x+1)}, x in Z_a. Let M = gamma x Z_k be the set of the a k time-like plaquettes p(x,t) = e_x x [t, t+1]. Then, under Haar measure, the expectation of the product of s_p over all p in M is 4^(-ak).
Proof. Let h(x,t) be the variable of the link e_x at time t, oriented from u_x to u_(x+1), and v(x,t) the variable of the time-like link at u_x over slab t. These 2ak links are distinct. For SU(2), tr U = tr U^(-1), so s_p does not depend on the orientation or the starting point of p, and

2 s_p(x,t) = tr( v(x,t)^(-1) h(x,t) v(x+1,t) h(x,t+1)^(-1) ).

Among the plaquettes of M, v(x,t) lies in p(x-1,t) and p(x,t) only.
Fix t and all h. Claim: for 1 <= j <= a, the integral over v(1,t), ..., v(j-1,t) of the product over x < j of tr U_p(x,t) is

(1/2)^(j-1) tr( v(0,t)^(-1) h(0,t) ... h(j-1,t) v(j,t) h(j-1,t+1)^(-1) ... h(0,t+1)^(-1) ).

For j = 1 this is the display. Step from j to j+1 <= a: the trace is tr(A U) with U = v(j,t) and A = h(j-1,t+1)^(-1) ... h(0,t+1)^(-1) v(0,t)^(-1) h(0,t) ... h(j-1,t), by cyclicity. The next factor is tr(U^(-1) B) with B = h(j,t) v(j+1,t) h(j,t+1)^(-1). Neither A nor B contains v(j,t) (for j = a-1, B contains v(a,t) = v(0,t), which is not v(a-1,t)). (O1) gives (1/2) tr(AB), which is the claim for j+1 after a cyclic shift.
For j = a, with v(a,t) = v(0,t) and H_t := h(0,t) ... h(a-1,t): the row gives (1/2)^(a-1) tr( v(0,t)^(-1) H_t v(0,t) H_(t+1)^(-1) ). By (O2) the integral over v(0,t) is (1/2)^a tr H_t tr H_(t+1)^(-1) = (1/2)^a tr H_t tr H_(t+1).
The rows use disjoint sets of v-variables. So the integral over all v of the product over M of tr U_p is 2^(-ak) times the product over t in Z_k of (tr H_t)^2. The H_t are functions of disjoint sets of h-variables, so they are independent, and each is Haar distributed (a product of independent Haar variables). By (O1) with A = B = 1, the expectation of (tr H)^2 = tr H tr H^(-1) is 1. So the expectation of the product of tr U_p is 2^(-ak), and that of the product of s_p is 2^(-2ak). QED

**Lemma 4.3 (the cumulant is the moment; PROVED GIVEN SC Lemma 2.1).** For M as in Lemma 4.2 and T any ordering of M without repetition, kappa(T) = 4^(-ak).
Proof. (1) Every proper nonempty subset A of M has moment 0. The adjacency graph of M is connected, so some p in A is adjacent to some p' in M outside A, through a link l. Each link of a plaquette of M lies in exactly two plaquettes of M (v(x,t) in p(x-1,t), p(x,t); h(x,t) in p(x,t-1), p(x,t), distinct because k >= 3). So l lies in no other plaquette of A. By SC Lemma 2.1 (c), s_p is independent of the other s of A. The expectation of s_p is 0, because Haar measure is invariant under V -> -V. So the moment of A is 0.
(2) Write E exp(sum of t_r Y_r) = 1 + x(t), with x a convergent power series without constant term. For a set A of indices, the coefficient of the monomial product of t_r, r in A, in x is the moment of A. log(1 + x) = sum over j >= 1 of (-1)^(j-1) x^j / j as power series. The monomial t_1 ... t_m appears in x^j only as a product of j monomials of x whose exponents add to (1, ..., 1). These are the monomials of j disjoint nonempty sets with union {1..m}. For j >= 2 each set is proper, and its coefficient is 0 by (1). So kappa(T), the coefficient of t_1 ... t_m in log(1 + x), is the moment of M. Lemma 4.2 gives the value. QED

**Proposition 4.4 (the first coefficient that does not cancel; PROVED GIVEN Lemmas 2.1, 4.2, 4.3 and Corollary 2.3).** Let k >= 3, q >= 2, B periodic with sides at least 3, c = c_B, and cyc(B) the number of cycles of length c in B (as sets of edges). Then

[beta^(ck)] ( log Z(k, B) - (1/q) log Z(qk, B) ) = cyc(B) 4^(-ck) > 0,

and cyc(B) = (number of directions i with b_i = 3) |B|/3 for c = 3, and cyc(B) = 3 |B| + (number of directions i with b_i = 4) |B|/4 for c = 4.
Proof. By Corollary 2.3 the coefficient is (W_k(ck) - (1/q) W~_(qk)(ck))/(ck)!.
W_k(ck). Let T be good, of length ck, not short, M = set(T). M has a time-like plaquette over each of the k slabs, at least c over each (Lemma 2.1 (a)), and |M| <= ck. So |M| = ck, T lists M without repetition, M has no spatial plaquette, and each G_t has exactly c edges. G_t contains a cycle of length at least c, so G_t is a cycle of length c. By Lemma 2.1 (c), G_(t+1) contains G_t, so they are equal. So M = gamma x Z_k with gamma a cycle of length c. Conversely each such M is connected and has (C) (proof of Lemma 4.3, (1)), and has (ck)! orderings. By Lemma 4.3, W_k(ck) = (ck)! cyc(B) 4^(-ck).
W~_(qk)(ck). Let T~ be good, of length ck, not short. Its set has time-like plaquettes over at least k slabs (one of each residue), at least c over each, so it has exactly k such slabs and no spatial plaquette. By Lemma 2.1 (c), if slab t is occupied then slab t+1 is occupied. So all qk > k slabs are occupied. Contradiction. So W~ = 0.
The count of cycles is Lemma 2.1 (b). A unit square is given by its lower corner and its plane: 3 |B|. A straight line in direction i is given by its direction and the other two coordinates: |B|/b_i. QED

**Proof of Theorem 2.** By (T) and D_j = 2 (log Z(n, B_j) - (1/2) log Z(2n, B_j)), the coefficient of beta^e(n) in Phi(n) is 2 x 4^(-e(n)) x (8 cyc(B_1) + 4 cyc(B_2) + 2 cyc(B_3) + cyc(B_4)), where for n = 3 the term of B_4 is absent (c = 4 there, order at least 12).
- n >= 5: cyc(B_j) = 3 |B_j| = 3n^3, 6n^3, 12n^3, 24n^3. The bracket is 24 n^3 x 4 = 96 n^3. A_n = 192 n^3 4^(-4n).
- n = 4: cyc = 3 x 64 + 3 x 16 = 240; 3 x 128 + 2 x 32 = 448; 3 x 256 + 64 = 832; 3 x 512 = 1536. The bracket is 1920 + 1792 + 1664 + 1536 = 6912. A_4 = 13824 x 4^(-16).
- n = 3: cyc(B_1) = 3 x 9 = 27; cyc(B_2) = 2 x 18 = 36; cyc(B_3) = 1 x 36 = 36. The bracket is 216 + 144 + 72 = 432. A_3 = 864/4^9 = 864/262144 = 27/8192.
Cross-check by a direct count on the torus n^4 (the large torus has no term of this order): 16 x (number of surfaces) x 4^(-e(n)). n >= 5: tubes, 4 directions x 3 n^3 unit squares of the transverse box: 16 x 12 n^3 = 192 n^3. n = 4: 768 tubes and 6 x 16 = 96 planes: 16 x 864 = 13824. n = 3: 6 x 9 = 54 planes: 16 x 54 = 864. All three agree.
Phi is analytic at 0, so the remainder is O(beta^(e(n)+1)). The statement for n = 3 follows as in Section 3. QED

What Theorem 2 shows. The leading term of Phi(n) is 192 n^3 (beta/4)^(4n) for n >= 5. So the true base of the exponential is beta/4 (the first coefficient of the character expansion; RECALLED name, not used), and the bound of Theorem 1 has the base 12800 beta. The constants of Theorem 1 are crude by the factor 51200 in the radius. What Theorem 2 does not show: a bound that is uniform in n with the base beta/4. The O-term depends on n.

## 5. Step 3: the seed

**Proof of Theorem 3.** Let n >= 4 and n theta^n <= 0.18. By Theorem 1 (iii), Phi(n; beta) <= 0.16 (n theta^n)^4 <= 0.16 x 0.18^4. Now 0.18^2 = 0.0324 and 0.0324^2 = 0.00104976, so the bound is at most 0.000168 < 1.9 x 10^(-4).
The explicit n. With theta = exp(-lambda): n exp(-lambda n) = (1/lambda) (lambda n exp(-lambda n/2)) exp(-lambda n/2) <= (2/(e lambda)) exp(-lambda n/2), because y exp(-y/2) <= 2/e for y >= 0 (the maximum is at y = 2). This is at most 0.18 when exp(-lambda n/2) <= 0.09 e lambda, that is, when n >= (2/lambda) log(1/(0.09 e lambda)). Since 0.09 x 2.718 x 4.1 > 1, we have 1/(0.09 e) < 4.1, so n >= (2/lambda) log(4.1/lambda) is enough. (For lambda >= 4.1 the right side is not positive and every n >= 4 qualifies.)
n = 3, beta <= 1/51200 (theta <= 1/4): Phi(3) <= 12.96 x 4^(-9) = 12.96/262144 < 5 x 10^(-5).
n = 5, beta <= 1/25600 (theta <= 1/2): Phi(5) <= 0.16 x 625 / 2^20 = 100/1048576 < 9.6 x 10^(-5). QED

Remarks.
- For beta <= 1/51200 the smallest seed size is n = 3, the smallest size that the setting allows. So "the smallest n" is exactly 3 there.
- For 1/51200 < beta < 1/12800, n_seed(beta) is a sufficient size, not the smallest one. It grows like (2/lambda) log(1/lambda) as beta tends to 1/12800. This growth comes from the crude radius, not from the model: by Theorem 2 the seed at fixed n holds for all small beta with base beta/4. I did not prove a seed for any beta >= 1/12800.
- The seed at a size n gives nothing new about the model at this coupling beyond the cubes: at beta < 1/12800 the infinite-volume gap is known from the polymer expansion (RECALLED). The value of this section is that the hypothesis of Theorem S is now a theorem on an interval of couplings, with explicit constants, so Theorem S has one case in which every input is proved.

## 6. Step 4: the gap from Theorem S, against the rate kappa_0

**Proof of Theorem 4.** Let n >= 4 with n theta^n <= 0.18. By Theorems 3 and 1 (iii), Phi(n) <= min(1.9 x 10^(-4), 0.16 n^4 theta^(4n)). By Theorem D (b) of `gap-crux-restate.md`, s = S(n; (2n)^3) <= exp(Phi(n)) - 1 <= 2 Phi(n) (e^x - 1 <= 2x on [0,1]). So q := 5041 s <= 10082 x 0.16 n^4 theta^(4n) <= 1614 n^4 theta^(4n), and q < 1 by the last line of Theorem S. Corollary S3' (row 699) gives, for every integer L >= 2n,

m(L^3) >= log(1/q)/n >= 4 log(1/theta) - (4 log n + log 1614)/n.

Every n' >= n_seed(beta) qualifies (Theorem 3). For L tending to infinity take n' = floor(L/2), which is at least n_seed(beta) for large L. The correction tends to 0, so liminf of m(L^3) is at least 4 log(1/theta). QED

**Comparison with `gap-sc-box.md`.** Theorem SC bounds the winding part of log Z by C_0 |B| k exp(-kappa_0 k) on the disc |beta| <= theta R, with kappa_0 = 4 log(1/theta); for theta = 1/2 this is 4 log 2. Theorem 4 gives the gap 4 log(1/theta) - (4 log n + log 1614)/n at real beta = theta R. So:
- The two rates agree in order, and their leading constants are equal. The loss of Theorem S is the term (4 log n + log 1614)/n. It comes from the factor 5041, from e^x - 1 <= 2x, and from the volume factor 0.16 n^4. It tends to 0 as the seed size grows.
- Numbers at theta = 1/2, by hand: 4 log 2 > 2.77. At n = 5 the correction is (4 log 5 + log 1614)/5 < (6.44 + 7.39)/5 < 2.77, so the bound at n = 5 is positive and small. At n = 40: (4 log 40 + log 1614)/40 < (14.76 + 7.39)/40 < 0.56, so m(L^3) > 2.2 for every L >= 80. (log 5 < 1.61, log 40 < 3.69, log 1614 < 7.39.)
- So Theorem S is not weaker in the rate. It is weaker at a small seed size by the additive term above, and the gap bound holds only from side 2n on.

**Test against the known answer (the exact leading term).** For fixed n >= 5, Theorem D (c) and Theorem 2 give exp(-n m((2n)^3)) <= exp(Phi(n)) - 1 = 192 n^3 (beta/4)^(4n) (1 + O(beta)) as beta tends to 0. So (PROVED GIVEN Theorem D (c)):

liminf as beta -> 0 of ( m((2n)^3; beta) - 4 log(4/beta) ) >= -(3 log n + log 192)/n.

The strong-coupling mass of the lightest state is 4 log(4/beta) at leading order (RECALLED, Münster; not read, not used in a proof). So at fixed n the chain from Phi to the gap gives the right rate with the right constant 4 and the right base beta/4, up to (3 log n + log 192)/n. Theorem D and Theorem S pass this test: they do not claim more than the known gap, and they lose only a term that vanishes with the seed size. The uniform bound of Theorem 4 is below the recalled value by the additive constant 4 log 51200 (about 43); this loss is in the radius R of Theorem SC, not in Theorem S.

## 7. Final status

Kind of result: a proof of a step that the plan states as a target (the seed of row 697, item 2), with one correction of the target (n = 3).

| Statement | Mark |
|---|---|
| (P), port of SC Proposition 3.6 to tori with sides at least 3 | PROVED GIVEN SC Lemmas 3.1 to 3.5 (checked, row 694) |
| Lemma 2.1 (count on a periodic box, cycles of length c_B) | PROVED |
| Lemma 2.2, Corollary 2.3 (exact cancellation of the terms that do not wind) | PROVED GIVEN SC (F1) to (F3), SC Lemmas 2.1, 2.2, (P) |
| Theorem 1 (zero of order e(n), bound 0.16 n^4 (12800 abs(beta))^e(n)) | PROVED GIVEN the above |
| Corollary 1' (the row's form, n >= 4; r_1 = 1/12800 with p = 4, r_1 = 1/25600 with p = 3 or p = 0) | PROVED GIVEN Theorem 1 |
| The row's target at n = 3 with exponent 12 | FALSE; the exact order is 9 (Theorem 2) |
| Lemmas 4.1 to 4.3, Proposition 4.4, Theorem 2 (leading term A_n beta^e(n)) | PROVED GIVEN Lemma 2.1, Corollary 2.3, SC Lemma 2.1 |
| Theorem 3 (seed for beta < 1/12800 at n >= n_seed(beta)) | PROVED GIVEN Theorem 1 |
| Theorem 4 (gap at least 4 log(1/(12800 beta)) - (4 log n + log 1614)/n for L >= 2n) | PROVED GIVEN Theorem 3, Theorem D (b), Theorem S, Corollary S3', (TM) |
| The seed at any beta >= 1/12800 | OPEN, not attempted (the crux; out of the scope of this row) |
| A bound uniform in n with the sharp base beta/4 | OPEN, not attempted; not needed by any consumer I know |

**Not done.** No check by another model. No numerics (none needed; memory state was not queried). I did not read Osterwalder-Seiler or Münster; both names are from memory. I did not re-check the proofs of SC Lemmas 3.1 to 3.5, of Theorem D, of Theorem S or of Corollary S3'; they are inputs with their own checks (rows 694, 698, 699). I did not edit any other file. Not committed, not pushed.

**For the lead.**
1. The statement of the seed in row 701 and in `gap-crux-restate.md` line 363 needs "n >= 4", or the exponent e(n) = min(4n, n^2).
2. The one exact next statement: a line-by-line check, by a model that did not write this file, of Lemma 2.1 (b), (c), Lemma 2.2, Corollary 2.3, the port list of Section 2.2, Lemma 4.2 (the row integration) and the arithmetic of Theorems 2 and 3.

**Credits.** Theorem SC and all its lemmas: `gap-sc-box.md` (Claude Opus 5.5, row 683; check by Codex gpt-6-astra, row 694); its remark on the spatial torus of side 3 led to the correction at n = 3. Phi, Theorem D, Theorem S: `gap-crux-restate.md` (Claude Fable 5.2 max, row 697); Corollary S3': Codex gpt-6-astra (row 699). The guess p = 3 and the tube of 4n plaquettes: the author of row 697. The method: Osterwalder and Seiler. Zero-freeness criterion: Dobrushin, as rebuilt in SC Section 3. Sussman and Alpoge with Claude and Codex: general polymer tools, cited in Section 0, not used.
