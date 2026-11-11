lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-12T08:00Z

# gap-kappa-order: (KP) for Wilson SU(2) (FINISH row 733, work item 4 of row 731)

Pinned commit d56f924ee. Proved by Claude Fable 5.2 medium; not yet checked by the other model. Research-stage working state; no status.


## 0. Repo search, rule 0a, sources

- Rule 0a. grep of `library/open-core.md` for "KP", "kappa": no hit. FINISH rows: (KP) is named only in rows 731 (source) and 733 (this row). No other row attacks it.
- Statement and notation: `library/gap-flux-exercise.md` 3.0 (twists, Z^k), 8.4 (W_per, W_kappa, order of the seeds), 8.7 (Y_h, Lemma GS, Proposition KP-Z2). Z_2 splitting: `library/gap-crux-restate.md` 4.4 (Mack and Petkova).
- Sussman-Alpoge account: the exercise's Step 5 row C5 found no kappa / Pfaffian sector sum there. I did not find one either. Nothing of theirs is used below.
- Credit. Twisted partition functions and the electric/magnetic sector sums: 't Hooft (Nucl. Phys. B 153, 1979). The splitting U = sV: Mack and Petkova. Both unchecked recollections, used only as language. All statements below are proved here from the definitions.

## 1. The statement in three equivalent forms (PROVED, finite algebra)

Wilson SU(2), torus n = (n_1..n_4), plaquette set P, x_p := (1/2) tr U_p. Z^k = integral of prod_p exp(-beta (1 - s^k_p x_p)).

(KP-a) sum over the 28 h with Pf(h) = 1 of Y_h >= 0. (Lemma GS.)

(KP-b) sum over k != 0 of (-1)^{Pf(k)} Z^k <= 7 Z^0.

(KP-c) Let r_0 := mean of Z^k/Z^0 over the 35 twists k != 0 with Pf(k) = 0, and r_1 := mean over the 28 twists with Pf(k) = 1. Then (KP) is 35 r_0 - 28 r_1 <= 7.

Proof. W_per - W_kappa = Z^0 - (1/8) sum_k (-1)^{Pf(k)} Z^k = (7/8) Z^0 - (1/8) sum_{k != 0} (-1)^{Pf(k)} Z^k. Pf(0) = 0. There are 36 twists with Pf = 0 and 28 with Pf = 1. QED

Two consequences (0 < Z^k <= Z^0 for every k: `gap-flux-exercise.md` (S2) applied in two frames, given (TM-tw)).

- (KP) holds whenever r_0 <= 1/5. So a violation needs Pf = 0 twists that are nearly free.
- (KP) fails if every Pf = 0 twist is free and every Pf = 1 twist is not: r_0 = 1, r_1 < 1 gives 35 - 28 r_1 > 7. At r_0 = r_1 = 1 (all twists free) (KP) is an equality.

So (KP) says: the twists with half-integer topological charge (Pf(k) = 1) are not much more expensive than the others. In terms of the deficits d_k := 1 - Z^k/Z^0 >= 0 it reads: sum_{Pf(k)=1} d_k <= sum_{Pf(k)=0} d_k.

## 2. Ways 1 and 2: the character expansion and the Z_2 splitting give one exact formula; it has no sign

**Proposition SC (surface formula; PROVED).** For a set S of plaquettes put

A(S) := integral over all links of prod_{p in S} sinh(beta x_p) prod_{p not in S} cosh(beta x_p).

Then A(S) = 0 unless S is closed (every link lies in an even number of plaquettes of S), and

Y_h = e^{-beta |P|} sum over closed S with h(S) = h of A(S), Z^k = e^{-beta |P|} sum over closed S of (-1)^{<k, h(S)>} A(S).

Here h(S)_{mu nu} is the parity of the number of plaquettes of S in the stack of the plane (mu, nu), as in Proposition KP-Z2.

Proof. For s = +-1, exp(beta s x) = cosh(beta x) + s sinh(beta x). Expand the product over P. A plaquette lies in the stack of its own plane or in no stack, so prod_{p in S} s^k_p = (-1)^{<k, h(S)>}. This gives the formula for Z^k with all S, and Fourier inversion on Z_2^6 gives Y_h. If a link l lies in an odd number of plaquettes of S, the change of variable U_l -> -U_l preserves Haar measure, changes the sign of x_p for the plaquettes at l, and so maps the integrand to minus itself (sinh is odd, cosh is even). So A(S) = 0. QED

**The two ways are this one formula.**

- Way 1 (character expansion). cosh(beta x) is the sum over integer spins j of c_j(beta) chi_j, and sinh(beta x) the sum over half-odd spins, with c_j > 0. So A(S) is the sum, over spin assignments with half-odd spin exactly on S, of prod c_{j_p} times I(j) := integral of prod_p chi_{j_p}(U_p). The class weight Y_h is a sum of non-negative terms if and only if these terms are; the coefficients c_j are positive, so the question is the sign of the group integrals I(j) (and, coarser, of A(S)).
- Way 2 (Mack and Petkova). With U = sV, the Z_2 theory at fixed V has couplings beta J_p(V), and its class weight is Y_h[V] = e^{-beta|P|} sum_{closed S in h} prod_{p in S} sinh(beta J_p) prod_{p not in S} cosh(beta J_p), by the proof of Proposition KP-Z2 with beta replaced by beta J_p. Its integral over V is Proposition SC. For closed S the integrand is a function of the SO(3) field.

**Lemma NP (no pointwise sign; PROVED).** On every torus with sides at least 2, for every h with h_12 = 1 there is a configuration V at which Y_h[V] < 0. So the Z_2 splitting gives no proof of Y_h >= 0 for fixed environment; any proof must use the average over V.

Proof. Let U_1(x) = i sigma_1 if x_1 = 0 and 1 otherwise, U_2(x) = i sigma_2 if x_2 = 0 and 1 otherwise, U_3 = U_4 = 1. U_1 depends on x_1 only and U_2 on x_2 only. The (1,2)-plaquette at x is the commutator of U_1(x_1) and U_2(x_2). It is -1 if x_1 = x_2 = 0 and 1 otherwise. Every other plaquette is 1. So x_p = s^{k_0}_p with k_0 = (12). At this configuration the Z_2 theory is the Z_2 Wilson theory with twist k_0, and its class weight is (-1)^{<k_0, h>} Y_h^{Z_2} = -Y_h^{Z_2} < 0 (Y_h^{Z_2} > 0 for beta > 0: Proposition KP-Z2 and a flat representative of h). The integrand is continuous, so it is negative on an open set. QED

The same holds for every plane. For h = (12) + (34), a class with Pf(h) = 1, this is a set of positive measure where the class weight is negative. The sign of prod_{p in S} x_p for closed S is the Z_2 flux of the SO(3) field through S (the monopole number inside S if S bounds; the twist of the SO(3) bundle on a non-trivial S). So Y_h, up to the positive factor, is the mean over the SO(3) measure prod cosh(beta x_p) dU of a signed sum, and the sign is the SO(3) twist paired with h. (KP) is a statement on how the SO(3) twist is distributed. Neither way gives a sign.

**What I could show on the fine terms I(j).** All of the following are positive: (i) one closed manifold surface of constant spin (d_j to the Euler characteristic, times d_j^{-F}); (ii) two or three discs glued along one circle (a Clebsch-Gordan multiplicity); (iii) two flat sheets that meet in one site (Lemma T below). I did not find a negative I(j), and I did not prove that none exists. A term with a branching vertex (three sheets through one site that share lines, for example the planes (12), (13), (23) through one site with spins a, b, c) reduces by the disc lemma below to the single-site integral J(a,b,c) = integral of chi_a([L_1,L_2]) chi_b([L_1,L_3]) chi_c([L_2,L_3]) over three Haar variables. Its sign is not settled here (see Section 5, run 2). **Verdict of ways 1 and 2: an exact formula, no sign. Not a proof, not a refutation.**

## 3. Way 3: small beta on a fixed torus. (KP) holds strictly for 0 < beta < beta_0(n). PROVED by hand.

**Lemma M (area bound).** Sides at least 2. Let S be closed with h(S) = h. For the plane (mu, nu) and each of the n_mu n_nu base points (a, b) let stack(a, b) be the set of (mu,nu)-plaquettes whose base point has x_mu = a, x_nu = b. Then |S ∩ stack(a,b)| = h_{mu nu} mod 2 for every (a, b). So S has at least n_mu n_nu plaquettes of each plane with h_{mu nu} = 1, and |S| >= a(h) := sum over the planes of h of n_mu n_nu.

Proof. Let c be the set of nu-links based at points with x_mu = a+1, x_nu = b. S is closed, so the number of pairs (l, p), l in c, p in S, l in the boundary of p, is even. Count by p. A (mu,nu)-plaquette based at x has its nu-links based at x and x + e_mu; exactly one is in c if x_nu = b and x_mu is a or a+1, none otherwise (n_mu >= 2). A (nu,rho)-plaquette with rho not mu has its two nu-links at the same (x_mu, x_nu), so it has 0 or 2 links in c. Other plaquettes have none. So |S ∩ stack(a,b)| + |S ∩ stack(a+1,b)| is even. The same holds for the shift of b. The stacks of one plane are disjoint. QED

**Lemma F (the minimal surfaces of a pair class).** Sides at least 2, h = (12) + (34). A closed S with h(S) = h and |S| = n_1 n_2 + n_3 n_4 is the union of one plane P_12(b) = {(1,2)-plaquettes with (x_3, x_4) = b} and one plane P_34(c). There are n_1 n_2 n_3 n_4 such S. The same holds for the other two pairs.

Proof. By Lemma M, S has exactly one (1,2)-plaquette in each (1,2)-stack, one (3,4)-plaquette in each (3,4)-stack, and no other plaquette. A 1-link based at y lies in the (1,2)-plaquettes based at y and y - e_2 and otherwise only in (1,3)- and (1,4)-plaquettes. S is closed, so both or neither of the two (1,2)-plaquettes is in S. So the set of base points of the (1,2)-plaquettes of S is invariant under shifts in direction 2 and, by the 2-links, in direction 1. It is a union of planes, and it meets each stack once, so it is one plane. The same for (3,4). QED

**Lemma T (torus integral).** Write f(U) = (1/2) tr U. (a) integral of f(AU) f(U^{-1}B) dU = (1/4) f(AB). (b) integral of f(A U B U^{-1}) dU = f(A) f(B). (c) integral of f^2 = 1/4. (d) For a flat m x n torus of plaquettes (m, n >= 2), T(m,n) := integral over its 2mn links of prod_p x_p = 4^{-mn}.

Proof. (a), (b), (c) are Schur orthogonality for the two-dimensional representation: the integral of U_{ij} (U^{-1})_{kl} is delta_{il} delta_{jk} / 2. (d) Disc lemma: for an a x b rectangle of plaquettes, the integral over its interior links of prod x_p is 4^{-(ab-1)} f(W), W the holonomy of the boundary. Add the plaquettes row by row. A new plaquette meets the region built so far in one link, or in two consecutive links at a corner. In both cases the shared path gamma occurs once in the boundary word of the region and once, inverted, in the new plaquette; integrate one link of gamma with the other fixed (gamma is then Haar distributed) and use (a). Each step gives a factor 1/4. Now cut the torus along the m 1-links with x_2 = 0 and the n 2-links with x_1 = 0. The rest is an m x n rectangle with boundary holonomy A B A^{-1} B^{-1}, A and B the ordered products of the cut links, which are independent and Haar distributed. By (b) with U = B, the integral over B of f(A B A^{-1} B^{-1}) is f(A) f(A^{-1}) = f(A)^2, and (c) gives 1/4. So T = 4^{-(mn-1)} / 4. QED

**Theorem SB (small beta).** Torus with sides at least 3. Let a_* be the least of n_1 n_2 + n_3 n_4, n_1 n_3 + n_2 n_4, n_1 n_4 + n_2 n_3, and N_* in {1, 2, 3} the number of pairs that attain it. Then, as beta -> 0,

sum over Pf(h) = 1 of Y_h = N_* n_1 n_2 n_3 n_4 (beta/4)^{a_*} (1 + O(beta)).

So there is beta_0(n) > 0 such that W_kappa < W_per for 0 < beta < beta_0(n).

Proof. A(S) is an entire function of beta, and A(S) = beta^{|S|} I(S) + O(beta^{|S|+2}) with I(S) the integral of prod_{p in S} x_p, because sinh(beta x) = beta x + O(beta^3) and cosh(beta x) = 1 + O(beta^2) uniformly for |x| <= 1. The number of sets S is finite and e^{-beta|P|} = 1 + O(beta). Pf(h) = 1 means that h contains an odd number of the three complementary pairs. So h contains a pair; if h is not that pair, a(h) >= a_* + 9. By Lemma M the terms of order beta^{a_*} come only from the pair classes with a(h) = a_* and from their S with |S| = a(h). By Lemma F these are the n_1 n_2 n_3 n_4 unions of two planes. The two planes have no common link (one has 1- and 2-links, the other 3- and 4-links), so I(S) = T(n_1,n_2) T(n_3,n_4) = 4^{-a_*} by Lemma T. QED

**What Theorem SB does not show.** beta_0 depends on the torus. A bound uniform in the torus needs a convergent polymer expansion of the ratio of the pair-class weight to its leading term; not done here. This confirms, with proof, the reading at the end of 8.7 of `gap-flux-exercise.md` ("two flat sheets that meet in one site").
