# Row 1332: shrink the box

Lane: four-dimensional SU(2) Yang-Mills mass gap, in the sense of Jaffe and Witten.
Row: FINISH 1332. Author of this file: Claude Fable 5.2 (worker). Date: 2026-11-20.

The problem (the brief). Prove a theorem with two properties.

- Its only unproved hypothesis is a finite statement, small enough to compute exactly and check in Lean. The budget is about 10^15 exact operations on one machine, or a certificate of that size.
- Its conclusion is the seed of the mass-gap chain, reached through checked results.

Status of this file: written in steps. Author only; checked by no one. No lattice computation was run. One arithmetic check of the quoted numbers was run (a few lines, seconds); no proof step uses it. The last line is the result line.

Labels: PROVED, ARGUED, GUIDE, OPEN. "PROVED on file" means: proved in the named row and checked as that row says. I did not re-check those rows. "PROVED here" means: proved in this file, by hand, unchecked.

Rule in force: GOAL.md, section "Computation only as a formal proof" (owner, 2026-11-20), read on the branch at 233c45338. An exact computation checked by the Lean kernel may be a proof step. Monte Carlo and unchecked floating point may only guide.

Note on row 1331. The cross-provider check of row 1326 (`library/gap-verified-compute-sizing-check-astra.md`, gpt-6.2-astra) landed during this run. I read it whole at dd0ed8042 and corrected this file where it had followed row 1326. The places are marked "check 1331".

## 0. Outcome in short

- I did not prove a theorem of the requested kind. Nothing in the chain is disproved.
- A list of evaluations on listed tori cannot be the only hypothesis. Every theorem of the requested kind contains a carry: a theorem with the quantifier "every late cutoff" (Section 2, Lemma N).
- The lane's own carry, Lemma ONE-K, puts the finite statement at a bare coupling above 5, on tori of at least 2 L^15 sites on a side (check 1331). With the carry margin the lattice is larger still (Section 3). No method with a demonstrated cost inside the budget is on file for it. I prove no cost floor.
- A finite statement at a coupling of order one needs a second carry, from order-one coupling to weak coupling. The engine and a Lipschitz bound give that carry over a coupling interval shorter than 10^(-12) at the window size (Section 4, Lemma CLIMB). Nothing else on file gives it.
- Theorem T (4.4) is the theorem of the brief with two open hypotheses beside the finite one: the ultraviolet carry and the infrared carry, each in rate form. It gives the rate that the infrared carry must reach. It is not a solution.
- Three other ways to shrink the box were tried here. Each stops at a named step (Sections 5 to 7).
- This is a bounded search. It proves no impossibility. Section 8 lists what is not excluded.

## 1. The target in exact form

Read for this section: `library/gap-verified-compute-sizing-fable.md` whole (row 1326); `library/gap-finishline-opus.md` whole (row 837); `library/gap-chain-ce-opus.md` Steps 6 to 8 (row 916); `library/gap-phys-seed.md` Sections 1, 3 and 4 (row 720); `library/gap-seed-shape.md` 1.4, 1.5, 1.7 and 2 (row 705); `parts/gap.md`; `library/gap-verified-compute-sizing-check-astra.md` whole (row 1331); the RESULT lines of rows 708, 709, 848, 916, 917, 924, 925, 978, 1025, 1029, 1143, 1225, 1256, 1266 and 1300 to 1331. I did not read the primary text of the account of Sussman and Alpoge, of Balaban, or of any published paper. Statements about them come from those rows.

**1.1 Objects (definitions, on file).** Wilson SU(2) on a periodic torus with sides n = (n_0, ..., n_3). Z_beta(n) is the partition function, F = log Z. For a spatial box B the transfer operator T_B has eigenvalues lambda_0 > lambda_1 >= ... >= 0, and Z(a x B) = Tr T_B^a. The thermal sum is S(a; B) = sum over i >= 1 of (lambda_i/lambda_0)^a. The doubling defect is Phi_B(a) = 2 F(a, B) - F(2a, B). Credit: Osterwalder and Seiler, and Luscher, for the transfer operator; rows 667, 671 and 697 for the lane's form.

**1.2 Three statements PROVED on file that this file uses.**

- (D) Theorem D-shape (a) and (d) (row 705, Claude Fable 5.2; check 707, Claude Opus 5.5). log(1 + S(a; B)) <= Phi_B(a) <= 2 log(1 + S(a; B)). And Phi_B(a; beta) = 12 a |B| times the integral over s in [0, beta] of (p_(a,B)(s) - p_(2a,B)(s)), where p is the mean of (1/2) tr U_p over the plaquettes of the torus.
- (E) The engine: Theorem S (row 697, Claude Fable 5.2; checks 698 and 699), Corollary S3' (row 699, Codex gpt-6-astra), Theorem SH (row 705; check 707). Let a >= 3 and min b_i > a. If S(a; B) is below the threshold of the shape, every periodic cube of side at least max b_i has a transfer gap, at that coupling. For cubes with b = r a: t(2) = 1/1650, t(3) = 1/100, t(4) = 1/25, t(6) = 1/10. For Theorem S, in the form that Lemma Z3 of row 720 uses (check 727): S(n; (2n)^3) = s < 1/5041 gives S(2n; (4n)^3) <= (5041 s)^2/5041. The class of (E), as check 1331 states it: a non-negative transfer spectrum, a simple top eigenvalue, the trace representation, and the exchange of axes.
- (C) The consumer (rows 700 and 703; row 916 with check 917, Codex gpt-6-astra). Given the account's premises, (SEED-FP) gives a unique vacuum and spectrum in {0} union [M_*, infinity) on the tr F^2 sector.

**1.3 The seed (definition on file, row 837).** Fix the account's data: an odd block factor L, a reference coupling g <= gamma_H, first-passage data (K, beta) with beta in W_K(g), bare spacing a_K = L^(-K) in the first-passage unit.

(SEED-FP): there are K_0, a physical size ell and s_* below the threshold such that S_(K,beta)(ell/(2 a_K); (ell/a_K)^3) <= s_* for every first-passage datum with K >= K_0.

Theorem ZD-c (row 720; checks 727 and `library/gap-zd-astra.md`) gives equivalent forms. Each has a limit over the cutoff.

**1.4 What "finite" means here.** A finite statement names finitely many couplings (or coupling intervals) and finitely many tori. By (D), the natural instance at one coupling and one torus pair is

(KER)(beta; a, B; tau): 2 log Z_beta(a x B) - log Z_beta(2a x B) <= tau.

Row 1326 Section 2 lists the finite candidates on file. Check 1331 corrects its claim that they are one object in several forms: they are different data (time doublings of rectangular tori, a neutral trace, a spectral gap with a symmetric defect, a scaling of all four sides, a block test with a supremum over boundary values), connected by transfer inequalities. This file works with (KER) and with the four-side form (W-TRAJ) of 3.1.

## 2. How best to attack it

**2.1 Lemma N (what every solution contains; PROVED here by unfolding the definition).** Let H be a true statement, and let "H gives (SEED-FP)" be a theorem. Then for every first-passage datum (K, beta) at g with K >= K_0:

- (i) Wilson SU(2) at the fixed coupling beta has S(n; (2n)^3) <= s_* at n = ell/(2 a_K) = ell L^K/2;
- (ii) so every periodic cube of side at least 2n has a gap at that coupling (Corollary S3');
- (iii) beta >= g^(-2) + B_sharp > 5, and beta >= g^(-2) + lambda_sharp K - c_5, which grows without bound with K.

Proof. (i) is (SEED-FP) at that datum. (ii) is (E). (iii) is read on file: W_K(g) asks beta >= g^(-2) + B_sharp (row 916 Step 7, correction 3); the account's constants give gamma_H^(-2) > 5 (check 1331, Section 5) and the lower bound in K (check 1331, Section 1); both are that check's readings of the complete account, which I did not re-read. QED

Consequence (PROVED as logic). The conclusion is an infinite family of lattice statements, at couplings that tend to infinity and on boxes that grow without bound. A list of evaluations on listed tori says nothing by itself about the other tori. So when H is such a list, the proof of "H gives (SEED-FP)" contains a theorem that moves a seed between lattices at different couplings. I call it a carry. A carry has the quantifier "every late cutoff". It can be proved by hand, or by a certificate that treats the cutoff as a symbol (check 1331, on F49: a finite certificate can describe infinitely many cutoffs). It is not an evaluation of listed tori.

**2.2 The two carries.**

- The ultraviolet carry. It moves a seed from the data of one cutoff K_0 to every finer cutoff, at one physical size. On file: Lemma ONE-K (row 916, Claude Opus 5.5; check 917: HOLDS AFTER CORRECTION). Its hypothesis (UNIV-K) is OPEN (rows 924 and 925; rows 1233 to 1314 reduce it to open inputs of the account). Check 1331 notes that a one-sided bound on the increments of the defect would telescope as well.
- The infrared carry. It moves a seed from a lattice at a coupling of order one to a lattice at a weak coupling. Not on file. Row 978 (Claude Fable 5.2) names it: (NOCRIT) with an asymptotic-freedom climb. (NOCRIT) is stated in row 708 and checked in row 709. Row 708 gives one form: Theorem TR, with the open rate hypothesis (VIR_K).

With the ultraviolet carry alone, the finite statement sits at the base data of the account. That is Attack 1 (Section 3). To put the finite statement at a coupling of order one, the infrared carry is needed too. That is Attack 2 (Section 4).

**2.3 The three boxes.** The owner's question was how to shrink the box. There are three boxes, not one.

| Box | What it is | What sets its size | State |
|---|---|---|---|
| B1, the base coupling | the bare coupling beta_0 of the finite statement | the weakest coupling down to which a carry is proved | above 5 by the account's own constants (check 1331); gamma_H has no value (row 837 1.1) |
| B2, the base lattice | the number of sites of the tori in the finite statement | the seed size at beta_0, and the margin that the carry leaves | Section 3 |
| B3, the cost | the number of exact operations that verify (KER) on those tori | the method | no method with a demonstrated cost inside the budget; no proved floor (3.4) |

A window computation needs B1 near 2.3 to 2.6. The account gives B1 above 5. This is the first gap, and no computation closes it. At the account's base every three-dimensional slice has at least 8 L^45 sites (3.1), far more than the budget has operations. So B2 excludes every method whose cost grows at least in proportion to the number of sites of a slice. B3 has no proved floor and no demonstrated method.

**2.4 Decision (ARGUED).** I attack in the order of what a success would buy.

1. Attack 1. The lane's architecture: (KER) at the base data, Lemma ONE-K. Find the honest size of the finite statement.
2. Attack 2. Put the base at a coupling of order one. Find what the infrared carry needs, what a computation can give toward it, and the exact theorem that would result.
3. Attack 3. Make the seed robust, so that the effective action with its error bars could feed a computation.
4. Attack 4. Replace the in-law seed by a chain of verified renormalization steps that ends at a robust criterion.
5. Attack 5. Change the regularization so that the carry is exact.

Sections 3 to 7 carry each attack to a theorem or to its first failing step.

## 3. Attack 1: the finite statement at the base data of the account

**3.1 The theorem that exists (on file; restated, not new).** Fix g, odd L >= 25 and ell with the tori T_ell and T_(L ell) in the account's family. For a first-passage datum d put Phi(d) = L^4 F_d(T_ell) - F_d(T_(L ell)).

- Lemma ONE-K (row 916, Claude Opus 5.5; check 917, Codex gpt-6-astra: HOLDS AFTER CORRECTION of the base-set quantifier). PROVED on file. Under (UNIV-K) with errors eps_K and E(K_0) = sum over K > K_0 of eps_K: if Phi(d_0) <= phi_* - (L^4 + 1) E(K_0) for every datum d_0 of cutoff K_0 that the predecessor chains reach, then Phi(d) <= phi_* for every first-passage datum with K >= K_0.
- Lemma FL (row 837, Claude Opus 5.5; check 848, Codex gpt-6-astra: HOLDS, applied with a margin phi' between phi_* and (L/2) log(13/10)). PROVED on file. With phi_* < (L/2) log(13/10), the conclusion of ONE-K gives (SEED-FP) at the size 6^(k_1) L ell.
- On the pin route the base is one datum (Proposition PIN of row 1256; check 1266: HOLDS AFTER CORRECTION). Otherwise the base is an interval of couplings. Check 1331, Section 7, reduces it to a finite mesh by the Lipschitz bound |d Phi/d beta| <= 2 L^4 P, with P the number of plaquettes of T_ell.

So the finite statement of this architecture is

(W-TRAJ)(d_0): L^4 F_(d_0)(T_ell) - F_(d_0)(T_(L ell)) <= phi_* - (L^4 + 1) E(K_0).

It is a doubling inequality of the kind of (KER), with all four sides scaled by L, on the pair of symmetric tori with ell L^(K_0) and ell L^(K_0 + 1) sites on a side, at the bare coupling of d_0. Row 1326 names it and sizes it with K_0 >= 1. Check 1331: K_0 = 0 is not excluded, and the account's hypotheses give ell >= 2 L^15, so the smaller torus has at least 2 L^(15 + K_0) sites on a side (1.86 x 10^21 at L = 25, K_0 = 0).

**3.2 The hypothesis is not only the finite statement (PROVED by reading).** (UNIV-K) is OPEN (rows 924, 925; row 1326 2.2 (c) quotes check 1288 on what it still needs). The account's premises are open (the T0 chain). The numbers K_0, L, ell, E(K_0) and the datum d_0 have no values (row 1326, X2). So this theorem does not have the first property of the brief.

**3.3 Lemma K0 (the margin forces a late base cutoff; PROVED here as arithmetic, GIVEN a bound of the stated form).** Suppose (UNIV-K) is proved with eps_K <= C_U ell^4 q^K for some C_U > 0 and 0 < q < 1. (Row 916 Step 7 argues this form for the regular part, with q = q_2. Row 924 proves it for the regular part, with q = q_3, given named hypotheses that are open. The full statement is not proved.) Then the condition (L^4 + 1) E(K_0) < phi_* that this bound can certify is

q^(K_0 + 1) < (1 - q) phi_* / ((L^4 + 1) C_U ell^4).

So the base torus T_ell has more than

N_0 = (ell/L) [C_U ell^4 (L^4 + 1) / ((1 - q) phi_*)]^theta sites on a side, with theta = log L / log(1/q).

Proof. E(K_0) <= C_U ell^4 q^(K_0 + 1)/(1 - q). Solve for K_0. The side is ell L^(K_0). QED

GUIDE (no proof step uses it). If q = L^(-2), the size of lattice artefacts of relative order a^2, then theta = 1/2 and N_0 is about 2.8 ell^3 (L C_U)^(1/2) when phi_* is near 0.131 L. The side grows like the cube of ell. With L = 25, C_U = 1 and the floor ell >= 2 L^15 of check 1331: N_0 is about 9 x 10^64 sites on a side. With the floor 2 L^11 that row 720 reads, it is about 1.5 x 10^48. Without the margin, row 1326 has 1.2 x 10^17 and check 1331 has 1.86 x 10^21. Whether a sharper bound on eps_K holds is not known. These numbers do not measure a cost. They show that a method whose cost grows with the number of sites of a slice cannot verify (W-TRAJ).

**3.4 Corollary COST (explicit state vectors reach no pair that the engine admits; PROVED here from Lemma DIM; the scope is the one check 1331 gives).** Lemma DIM (row 1326; check 1331: HOLDS as a count of dimensions): the gauge-invariant space of a connected periodic slice Sigma, with link spins 0 and 1/2 only, has dimension at least 2^(2 |Sigma| + 1). An evaluation that writes one coefficient for each such basis state uses at least that many coefficients. The engine (E) needs a >= 3 and min b_i > a, so every b_i >= 4. Its free-energy form (KER) reads the tori (a, B) and (2a, B). Every three-dimensional slice of (2a, B) has at least 4 x 4 x 4 = 64 sites. So an explicit state-vector evaluation of the pair writes at least 2^129, about 6.8 x 10^38, coefficients. A direct evaluation of S(a; B) from states on the slice B has the same bound. A vector of at most 10^15 coefficients allows |Sigma| <= 24.

Proof. The slices of (2a, B) are B itself and the boxes (2a, b_i, b_j). With a >= 3 and b_i >= 4 the smallest has 64 sites. 2 x 64 + 1 = 129. 2^49 < 10^15 < 2^51. QED

What this is not (check 1331, Section 2: the unqualified lower bound of row 1326 FAILS). It is not a floor for every exact method. A scalar partition function can be evaluated without a state vector, for example by depth-first enumeration with a running sum, by a structured contraction, as a direct ratio, or through a proof certificate. Check 1331 also gives an elementary finite prescription (the Taylor polynomial of the weight against exact Haar moments), with no bound on its cost.

Remarks.

- (i) The pair (3; 4, 4, 4) has shape ratio 4/3. Its threshold is small (row 705 1.7), so it can pass only at small beta, where the seed is proved by hand (beta < 2/9, row 785 with check 790). At the window the pair of row 1326 is 10 x 20^3 and 20^4 and the same count is 2^16001.
- (ii) Lemma SURF (PROVED here). On a periodic four-dimensional lattice with V sites, the assignments of spin 0 or 1/2 to the plaquettes in which every link meets an even number of spin-1/2 plaquettes are 2^(3V + 3) in number. Every other assignment has a vanishing link integral. Proof. These assignments are the mod-two 2-cycles of the cubical torus. The cells number V, 4V, 6V, 4V, V in the dimensions 0 to 4, and the mod-two Betti numbers are 1, 4, 6, 4, 1. So the 4-cycles have dimension 1, the boundary map from 4-cells has rank V - 1, the 3-cycles have dimension V + 3, the boundary map from 3-cells has rank 3V - 3, and the 2-cycles have dimension 3V - 3 + 6. A link with an odd number of fundamental representations has no invariant. QED. So a term-by-term enumeration that prunes by this parity rule alone visits 2^1155 assignments on the torus (6, 4, 4, 4), before any higher spin. So the depth-first alternative saves storage, not operations. A method that groups terms is no longer term by term; I have no cost bound for such methods.
- (iii) What stays open after check 1331, each without a cost bound on file: structured exact evaluations of (KER); rational sum-of-squares certificates (Remark OS of row 1326 gives a disjunction only: the patch has n^4 > a b^3/8, or the witness torus of side n passes the test itself); cut-dependent signed Gaussian bounds on the trajectory (rows 1323 (26) to (30) block the uncorrected substitution only); block criteria on cubes only, with invariant readouts or typical boundary values (CA-FAIL does not reach them; (DS-W) of row 691 is open at the window). I found a cost bound inside the budget for none of them. That is a statement of what I found. It is not a floor.

**3.5 First failing step of Attack 1.** In order: (UNIV-K) is open; the base datum has no numbers; the base lattice has at least 2 L^15 sites on a side, and more with the margin; no method with a demonstrated cost inside the budget evaluates (KER), even on the smallest pair that the engine admits. Lemma N (iii) says that the base coupling is above 5 in every case.

## 4. Attack 2: the finite statement at a coupling of order one

**4.1 What is needed.** Let (KER) hold at a coupling beta_1 of order one, on a pair that the engine admits. Then (E) gives a gap at beta_1. To reach (SEED-FP), Attack 1 still needs a seed at one base datum of the account, at a coupling beta_0 > 5. So a theorem is needed that carries a seed from beta_1 up to beta_0. This is the infrared carry of 2.2.

**4.2 Lemma CLIMB (how far the engine and a Lipschitz bound carry a seed along the coupling; PROVED here from (D) and (E)).** Let n >= 3, 0 < q <= 1/4, and let 5041 S(n; (2n)^3; beta) <= q at one coupling beta. Put

delta(n, q) = [log(1 + q/5041) - 2 q^2/5041] / (3072 n^4).

Then 5041 S(2n; (4n)^3; beta') <= q for every beta' in [beta, beta + delta(n, q)]. By induction, for every k >= 1 the cube pair of size 2^k n has the same seed at every coupling in [beta, beta + sum over j < k of delta(2^j n, q)]. The sum over all j is at most 8.7 x 10^(-9)/n^4.

Proof. delta(n, q) > 0, since log(1 + x) >= x - x^2/2 and q <= 1/4. Step 1. By (E), S(2n; (4n)^3; beta) <= q^2/5041. Step 2. By (D)(a), Phi_((4n)^3)(2n; beta) <= 2 log(1 + q^2/5041) <= 2 q^2/5041. Step 3. By (D)(d) with a = 2n and |B| = 64 n^3, the derivative of Phi_((4n)^3)(2n; .) in the coupling is 12 x 2n x 64 n^3 times a difference of two plaquette means. Each mean lies in [-1, 1]. So the derivative is at most 3072 n^4 in absolute value. Step 4. For beta' in the stated interval, Phi_((4n)^3)(2n; beta') <= 2 q^2/5041 + 3072 n^4 (beta' - beta) <= log(1 + q/5041). By (D)(a), S(2n; (4n)^3; beta') <= exp(Phi) - 1 <= q/5041. Step 5. The sum: delta(2^j n, q) = 16^(-j) delta(n, q), and log(1 + x) <= x gives delta(n, q) <= (q - 2 q^2)/(5041 x 3072 n^4) <= 1/(8 x 5041 x 3072 n^4). Multiply by 16/15. QED

Reading. A seed proved at one coupling proves seeds on a coupling interval of length below 10^(-12) above it, for n = 10. The steps are summable because the bound of Step 3 is extensive. So this argument cannot show that the seed couplings of the sizes 2^k n are unbounded. That statement is (NOCRIT) of row 708. Theorem CRIT of row 708 (Claude Fable 5.2; check 709) has the qualitative form: the set of couplings with a seed is open. Lemma CLIMB adds the size of the opening that the on-file tools give.

**4.3 What would give a real climb (on file; OPEN).** Step 3 bounds a difference of plaquette means by 2. GUIDE: the true difference is far smaller, because only the excitations that wrap the time circle cause it. Row 708 has the theorem that uses this: Theorem TR and Corollary TR1, with the hypothesis (VIR_K), or (LEV_K): no level of the box falls faster in the coupling than at a logarithmic rate K. In the variable of Lemma CLIMB, a bound of the form "d Phi/d beta <= K Phi log(e/Phi)" at the seed sizes gives a step delta >= (1/K) log[(1 + log(5041/(2 q^2)))/(1 + log(5041/q) + q/5041)] for each doubling. (With y = log(1/Phi) the inequality is y' >= -K (1 + y). The start is y >= log(5041/(2 q^2)) by Steps 1 and 2. The seed needs Phi <= log(1 + q/5041), and y >= log(5041/q) + q/5041 is enough for that.) The step does not depend on n, and it tends to (log 2)/K as q tends to 0. I state this as a restatement of row 708's result in the seed variable. I did not compare constants with Theorem TR.

(VIR_K) and (LEV_K) are OPEN. Row 708 records three failed ways. They say that the lattice beta function, read from every level of the box, is bounded away from zero. Row 978 argues that they fail for compact U(1), for the frozen groups and on the K7 lines; check 1331 notes that those arguments rest on recalled or argued premises.

**4.4 Theorem T (the shape of a solution with its base at a window coupling; PROVED here GIVEN the statements named in it).** Fix the account's data g, odd L >= 25, B_sharp, the family of tori and phi_* < (L/2) log(13/10). Assume:

- (A0) a flow bound: there is kappa > 0 such that every first-passage datum (K, beta) at g has g^(-2) + B_sharp <= beta <= g^(-2) + (K + 1) kappa. The account gives kappa = B_sharp (check 1331, Section 7, from the account; row 837 1.1 has b_k <= B_sharp);
- (A1) the ultraviolet carry in rate form: there are C_U > 0 and 0 < q < 1 such that, for every admissible ell = 2 L^m and every K_0, (UNIV-K) holds on the tori T_ell and T_(L ell) with eps_K <= C_U ell^4 q^K;
- (A2) the infrared carry in rate form: there are beta_w <= g^(-2) + B_sharp, an integer n_w >= 3, 0 < q_0 < 1, C_1 > 0 and c >= 0 such that, if 5041 S(n_w; (2 n_w)^3; beta_w) <= q_0, then for every beta >= beta_w there is an integer N(beta) >= 3 with N(beta) <= C_1 exp(c (beta - beta_w)) and 5041 S(N(beta); (2 N(beta))^3; beta) <= q_0;
- (A3) the two rates fit: c < (log L)/kappa + log(1/q)/(4 kappa).

Then the one finite statement

(KER)(beta_w; n_w, (2 n_w)^3; log(1 + q_0/5041))

gives (SEED-FP).

Proof. Step 1. By (D)(a) the finite statement gives 5041 S(n_w; (2 n_w)^3; beta_w) <= q_0. By (A2) every beta >= beta_w has a seed at the size N(beta).

Step 2 (from a cube seed to the defect of two symmetric tori). Write D(n) = F(n^4) - f n^4 >= 0, with f the infimum of F/|n|. Then L^4 F(n^4) - F((L n)^4) = L^4 D(n) - D(L n) <= L^4 D(n). By Lemma Z3 of row 720 (check 727), a seed 5041 S(N; (2N)^3) <= q_0 gives D(n') <= 1024 q_0^(2^k)/5041 for every n' >= 2^(k+1) N. Choose k_* with 1024 L^4 q_0^(2^(k_*))/5041 <= phi_*/2. It depends on q_0, L and phi_* only. So at every beta >= beta_w and every n' >= 2^(k_* + 1) N(beta): L^4 F(n'^4) - F((L n')^4) <= phi_*/2.

Step 3 (the base). Let K_0 be a cutoff. By (A0) every datum of cutoff K_0 has beta <= beta^+ := g^(-2) + (K_0 + 1) kappa, so N(beta) <= N^+ := C_1 exp(c (beta^+ - beta_w)). Let m be the least integer with 2 L^m admissible and 2 L^(m + K_0) >= 2^(k_* + 1) N^+. Put ell = 2 L^m. The torus T_ell has ell L^(K_0) sites on a side at cutoff K_0. So by Step 2, Phi(d_0) <= phi_*/2 for every datum d_0 of cutoff K_0. By the choice of m, ell <= max(L ell_*, 2^(k_* + 1) N^+ L^(1 - K_0)), with ell_* the account's floor.

Step 4 (the margin). By (A1), (L^4 + 1) E(K_0) <= (L^4 + 1) C_U ell^4 q^(K_0 + 1)/(1 - q). If ell <= L ell_*, the right side tends to 0 as K_0 grows. Otherwise ell^4 q^(K_0) is at most a constant times exp(K_0 [4 c kappa - 4 log L - log(1/q)]), and the bracket is negative by (A3). So there is K_0 with (L^4 + 1) E(K_0) <= phi_*/2.

Step 5. For that K_0 and its ell, Phi(d_0) <= phi_* - (L^4 + 1) E(K_0) for every datum of cutoff K_0. Lemma ONE-K gives Phi(d) <= phi_* for every first-passage datum with K >= K_0. Lemma FL gives (SEED-FP). QED

Remarks.

- (What is finite, what is not.) The finite statement is (KER) on the tori (n_w, (2 n_w)^3) and (2 n_w, (2 n_w)^3) at one coupling. At the window this is the pair of row 1326. (A0) is read on file and rests on the account. (A1) and (A2) are OPEN. They are theorems with a quantifier over all cutoffs or all couplings. Lemma CLIMB proves (A2) only up to beta_w + 8.7 x 10^(-9)/n_w^4. Theorem TR of row 708 would give (A2) from (LEV_K), with c of the size of its rate K.
- (No computation if the carry starts in the hand range.) If (A2) holds with beta_w < 2/9, its premise is proved by hand (Theorem DOB in chord form, row 785 with check 790, at a suitable size). Then Theorem T has no computed hypothesis. A computation is needed only for an infrared carry that starts above the hand range.
- (A weaker form.) The proof uses (A2) and (A3) only through this: the lower limit over K_0 of (N^+)^4 L^(-4 K_0) q^(K_0) is 0, where N^+ bounds the seed sizes at the data of cutoff K_0.
- (Consistency; ARGUED.) Suppose (SEED-FP) holds. By Lemma N it gives a seed at every first-passage coupling at the size ell L^K/2. The account's lower flow bound gives K <= (beta - g^(-2) + c_5)/lambda_sharp, so these sizes are at most C exp(((log L)/lambda_sharp) beta). That is a statement of the form (A2), from a large beta_w, with c = (log L)/lambda_sharp. It lies inside (A3) if kappa/lambda_sharp < 1 + log(1/q)/(4 log L). So Theorem T is not empty when the flow steps are pinched to that extent. At weak coupling the steps tend to the one-loop value (GUIDE), so this is expected at late cutoffs. The account's B_sharp and lambda_sharp have no values, so I cannot say whether its own bounds are pinched enough.
- (GUIDE: the rate (A3) at one loop; no proof step uses it.) With kappa near the one-loop step (11/(3 pi^2)) log L and q = L^(-2), (A3) reads c < (3/2)(3 pi^2/11), about 4.0 per unit of beta. The asymptotic-freedom rate is 3 pi^2/11, about 2.7. Row 708 quotes about 3.3 for the largest published logarithmic rate near the window. So the seed size may grow up to the power 3/2 of the asymptotic-freedom length, and no faster. The same count in two dimensions (ell^2 in place of ell^4) gives twice the asymptotic-freedom rate. Row 1007 reads a mixing length of the form C exp((4 pi - eta) b) in the posted two-dimensional O(3) proof of OpenAI, and 4 pi is twice the rate 2 pi of that model. I did not read that proof. The match supports this reading of the architecture.
- (Status.) Theorem T is the theorem that the brief asks for, with two open hypotheses beside the finite one. It is not a solution.

**4.5 A finite cover does not avoid the weak end (PROVED as logic).** One could cover [beta_1, beta_0] by finitely many computed seeds, each valid on a short interval by the Lipschitz bound of Step 3. The cover contains a seed at beta_0. So it contains a finite statement at the weak base coupling, which is Attack 1 again, and more.

**4.6 First failing step of Attack 2.** The infrared carry. On file it is (NOCRIT) with a rate, or (VIR_K), or a renormalization step at an effective coupling of order one. Each is open. None is an evaluation of listed tori: each has the quantifier "every coupling in [beta_1, beta_0]" on boxes that grow with the coupling. Check 1331 notes that nothing proves that a sufficient criterion must inspect every intermediate coupling. I found no criterion that does not. What a window computation would buy by itself is a lattice gap at one coupling, and seeds on an interval of length below 10^(-12) above it. No method with a demonstrated cost inside the budget is on file for that computation (3.4).

## 5. Attack 3: make the seed robust

The idea. The account knows the effective density at its last scale only up to bounded local terms. If the seed test tolerated a small relative error of the weight at every site, a computation on a class of weights could replace the missing precision. This fails, for a reason that is a property of the engine's class.

**5.1 Proposition FR (the seed test tolerates a relative error of order 1/volume and, in the engine's class, no more; PROVED here).**

(a) Let two models have partition functions Z and Z' with |log Z'(T) - log Z(T)| <= eps |T| on the two tori T = (a, B) and T = (2a, B). Then |Phi'_B(a) - Phi_B(a)| <= 4 eps a |B|. For two plaquette weights with exp(-eta) <= w'/w <= exp(eta) pointwise, this holds with eps = 6 eta.

(b) For delta >= 0 let M_delta be the model with state space C^2 for every box and transfer operator T_B = diag(exp(delta |B|), 1) in every direction. Then Z_delta(n) = 1 + exp(delta |n|). M_delta has a positive trace-class transfer operator in each direction, Z_delta is symmetric in the four sides, and for delta > 0 the top eigenvalue is simple. These are the properties that (E) uses, as row 837 2.1 reads them in `library/gap-crux-restate.md`. I did not re-read the proofs of (E) for other implicit uses. S_delta(a; B) = exp(-delta a |B|), and |log Z_delta(T) - log Z_0(T)| <= delta |T| for every torus.

So, for every pair (a, B) and every t in (0, 1): with delta = log(1/t)/(a |B|) the model M_delta has S(a; B) = t and smaller thermal sums on all larger tori, while M_0 has S = 1 at every size. (M_0 has a double top eigenvalue. It is the limit case, outside the class.) The two models differ by a relative error of log(1/t)/(a |B|) per site in the sense of (a).

Proof. (a) Phi = 2 F(a, B) - F(2a, B), and the two volumes are a |B| and 2a |B|. A torus has 6 plaquettes for each site. (b) Tr T_B^a = exp(delta a |B|) + 1, the same for each choice of the time axis. The ratio lambda_1/lambda_0 is exp(-delta |B|). (1 + e^x)/2 lies between 1 and e^x for x >= 0. QED

**5.2 Consequences.**

- (PROVED from 5.1 (a).) A certificate that knows the weight only up to a relative error eta at each plaquette can verify (KER) with slack sigma only if 24 eta a |B| <= sigma. At the smallest window pair of row 1326 (a = 10, b = 20, slack 3.6 x 10^(-4), GUIDE): eta <= 1.9 x 10^(-10).
- (PROVED from 5.1 (b).) No argument that uses only the properties of the engine's class can do better than a relative error of order 1/(a |B|) per site. In M_delta the truth itself changes at that size of error.
- (PROVED on file.) The account controls the logarithm of its last-scale integral to an error of order one for each unit cell, on tori of at least 16 L^44 cells (Proposition 1.1 of row 720; check 727; check 1331 reads a larger floor). So the account's bounds cannot feed the seed test, and by 5.1 (b) no class-wide repair exists.
- (ARGUED.) M_delta is a model of two phases with free-energy densities delta and 0. Local models show the same at a point of coexistence. Proposition V of row 712 (PROVED there GIVEN a theorem of van Enter and Shlosman) gives SU(2) plaquette weights with a coupling at which no size has a seed. So in the class of local SU(2) weights a robust seed test must read what separates the Wilson weight from those weights. That is the selective input the lane has looked for since row 988.

**5.3 Two kinds of criterion (ARGUED).** An in-law criterion, such as (KER), is sharp and fragile: it needs the weight to a relative accuracy of 1/volume. A robust criterion holds on an open set of weights. The robust criteria proved on file are of Dobrushin type, at strong coupling (beta < 2/9, row 785). The form that is uniform over all volumes and all boundary values fails at every beta above about 1.01 (Proposition CA-FAIL, row 1072; checks 1074, 1075 and 1331). Check 1331 corrects the reach of that failure: conditions on cubes only, invariant readouts, typical boundary values and (DS-W) of row 691 are not excluded, and (DS-W) is open at the window (row 1122 6.4). So where a robust criterion can stand is open. On file it stands only at strong coupling. A chain that ends at a robust criterion is Attack 4.

**5.4 First failing step of Attack 3.** Proposition FR (b): the fragility is a fact about the class, not about the proof.

## 6. Attack 4: a chain of renormalization steps that ends at a robust criterion

The idea. Do not evaluate one large box. Carry every late cutoff through block steps to a scale where a robust criterion holds, and test it there. Each step is local, so its cost does not grow with the box. This is the only architecture I found in which a small finite statement could exist at all.

**6.1 Proposition CH (soundness of such a chain; PROVED here; the proof is one line).** Fix the two tori T_ell and T_(L ell) of 3.1. Let C_0, ..., C_N be sets. Let every element nu of every C_k carry two positive numbers Z_nu(T_ell) and Z_nu(T_(L ell)). Let R_k map C_k into C_(k+1) with Z_(R_k nu)(T) = Z_nu(T) for both tori. Assume:

- (BASE) there is K_0 such that for every first-passage datum d with K >= K_0 some nu_d in C_0 has Z_(nu_d)(T) = Z_d(T) for both tori;
- (END) every nu in C_N has L^4 log Z_nu(T_ell) - log Z_nu(T_(L ell)) <= phi_*.

Then Phi(d) <= phi_* for every first-passage datum with K >= K_0. With Lemma FL (check 848) this is (SEED-FP) at a larger size.

Proof. R_(N-1) ... R_0 nu_d lies in C_N and has the two masses of d. QED

Remarks.

- (PROVED by inspection.) (UNIV-K) is not used. Each datum is carried by itself into one common class. The lane needs (UNIV-K) only because its finite statement is in-law at one bare datum.
- (READ through row 837 1.2 and 1.4; not re-read.) (BASE) has the shape of the account's own statements: the integral of its last-scale density equals the bare partition function exactly, and the outline states, as a programme, one class F_k with the same constants at every step. It is conditional on the account's premises, and the class has no numbers.
- The price is that C_N is a class. So (END) must be a robust criterion (5.3).

**6.2 (END) (ARGUED).** One robust seed is on file: Theorem DOB in chord form (row 785, Codex gpt-6-astra; check 790, Claude Opus 5.5). For the Wilson weight with q = 9 beta/2 < 1 it gives the seed and a gap. Its hypothesis is an open condition on the conditional law of one link. An END criterion for effective densities that are not plaquette weights is not on file. I did not write one.

**6.3 The steps (OPEN; this is where the attack stops).** A step of the chain must map a class given by bounds into a class given by bounds, at an effective coupling above the ceiling gamma of the ultraviolet stability theorem. On file the block steps hold only while every effective coupling lies in (0, gamma] (row 837 1.1, from the account's citation of Balaban's theorem). I know no rigorous block step for a four-dimensional gauge theory at an effective coupling of order one. I did not search the literature in this row. A computation could enter here as a certificate that a step maps one class into the next. No one has stated such a certificate. Its statement would be a theorem about an infinite-dimensional class, with finitely many computed inequalities inside its proof. It is not a finite statement as it stands.

**6.4 Length of the chain (GUIDE, from row 837 3.1).** At one loop the running inverse coupling falls by 0.3715 for each e-fold of length. From x = g^(-2) to the window value 2.38 that is 7.1, 20.5, 61 and 263 e-folds for g^(-2) = 5, 10, 25 and 100. By check 1331, g^(-2) is above 5. The account gives no value for its ceiling. If the END is of the kind proved on file, the chain must run further, to the strong-coupling range.

**6.5 First failing step of Attack 4.** One block step at an effective coupling of order one, with a class on each side. Before that: (BASE) with numbers.

## 7. Attack 5: change the regularization so that the carry is exact

The idea. The ultraviolet carry compares lattices of different spacing. Choose the fine measures so that the comparison is an identity.

**7.1 Proposition PF (an exactly consistent family above any base; PROVED here).** For K >= 0 let Omega_K be the compact space of gauge fields on a periodic lattice Lambda_K of spacing L^(-K) and fixed physical period. Let c_K be a Borel map from Omega_(K+1) to Omega_K (a block map). Let mu_0 be a Borel probability measure on Omega_0, and W_(K+1) a Borel probability measure on Omega_(K+1). Let P_K(V, dU) be a regular conditional law of U under W_(K+1) given c_K(U) = V. Assume that each mu_K below is absolutely continuous with respect to the image of W_(K+1) under c_K. Define

mu_(K+1)(dU) = integral of mu_K(dV) P_K(V, dU).

Then:

- (i) the image of mu_(K+1) under c_K is mu_K. So for every bounded Borel function f on Omega_0 and every K, the mean of f(c_0 c_1 ... c_(K-1) U) under mu_K equals the mean of f under mu_0;
- (ii) mu_(K+1) has the density h_K(c_K(U)) with respect to W_(K+1), where h_K is the density of mu_K with respect to the image of W_(K+1);
- (iii) if mu_0 and every W_K are invariant under the translations by the vectors of Lambda_0, and every c_K commutes with them, then every mu_K is invariant under those translations.

Proof. Omega_K is a compact metric space, so regular conditional laws exist, and P_K(V, .) is carried by the fibre c_K = V for almost every V. This gives (i). For a bounded Borel phi: the integral of phi(U) h_K(c_K U) W_(K+1)(dU) equals the integral over V, against the image of W_(K+1), of h_K(V) times the integral of phi against P_K(V, .). That is the integral of phi against mu_(K+1). This gives (ii). (iii) follows from (ii) by induction: h_K is invariant when mu_K and the image of W_(K+1) are. QED

**7.2 What it shows.** Take mu_0 = the Wilson measure at a window coupling, and W_K = the Wilson measures at weak couplings. By (i) the functions of the scale-0 block field have the correlations of mu_0 at every cutoff K. If mu_0 has a seed, they have the clustering of mu_0 at every cutoff, with no ultraviolet carry. So consistency across cutoffs costs nothing.

**7.3 Why it is not a solution (ARGUED).** By (ii) the fine measure is a Wilson measure reweighted by a function of block variables. A translation by a vector of Lambda_K that is not in Lambda_0 does not commute with the block maps. So nothing gives invariance under it, unless h_K = 1. If h_K = 1 for every K, then the fine measures are the Wilson measures themselves, and each is the exact block image of the next. Nothing suggests that Wilson measures have this property. A family with this property and all the symmetries is an exact renormalized trajectory, which no one has constructed. Reflection positivity at the fine planes is open for the same reason. A Jaffe-Witten theory needs all translations and O(4). So the family of 7.1 gives consistency without symmetry, and the Wilson family gives symmetry without consistency. (UNIV-K) is the statement that the Wilson family is consistent up to summable errors. It cannot be avoided by a choice of regularization of this kind.

**7.4 First failing step of Attack 5.** Invariance of mu_K under the translations of Lambda_K.

## 8. Verdict

**8.1 Decision.** Not solved. I found no theorem whose only unproved hypothesis is a computable finite statement and whose conclusion is (SEED-FP). I prove no impossibility. Nothing in the chain is disproved.

| Attack | Its finite statement | What is missing beside it | First failing step |
|---|---|---|---|
| 1. In-law base with Lemma ONE-K | (W-TRAJ) at the base data: beta_0 > 5, at least 2 L^15 sites on a side | (UNIV-K); numbers for the account's constants; a method | (UNIV-K) is open (3.5) |
| 2. Base at a window coupling | (KER) at one coupling of order one, on one pair of tori (Theorem T) | the infrared carry (A2) with a rate inside (A3); the ultraviolet carry (A1); a method for (KER) | (A2): Lemma CLIMB gives it over less than 10^(-12) in the coupling (4.6) |
| 3. Robust seed | (KER) for a class of weights | no class-wide repair exists: Proposition FR (b); a selective one would be the crux | the fragility is a fact about the engine's class (5.4) |
| 4. Chain of block steps with a robust end | certificates that each step maps one class into the next | a block step at an effective coupling of order one, stated for classes; an end criterion for effective densities; the account's class with numbers | one block step (6.5) |
| 5. Exact carry by another regularization | a seed of the base measure | invariance under the translations of the fine lattice | 7.4 |

**8.2 The answer to "how do we shrink the box" (ARGUED).**

- The box of the lane's present architecture cannot be shrunk by computing. Its place is fixed by the ultraviolet carry: a bare coupling above 5 and tori of at least 2 L^15 sites on a side. The carry is a theorem about the account. It is open.
- A box at the window exists in exactly one theorem that I can state: Theorem T. Its price is the infrared carry (A2), with a rate c below (log L)/kappa + log(1/q)/(4 kappa), where kappa bounds the flow step. In the lane's words this is (NOCRIT) with a rate, or (LEV_K) of row 708 with K below that bound. It is the crux in the coupling variable. No computation supplies it: Lemma CLIMB measures what the on-file tools give.
- If (A2) is ever proved from the hand range (beta below 2/9), the proof of the seed needs no computation at all. A computation has a place only if (A2) is proved from some coupling beta_w above the hand range. Then the place is (KER) at beta_w, and a method for it is still needed.
- The chain of Attack 4 has small boxes, one block for each step. Its statements are about classes of effective densities, not about listed tori. No such step exists above the ultraviolet ceiling.

**8.3 What would change this decision (each line is a conjunction; check 1331 corrects row 1326 on this point).**

- (A1), (A2) and (A3) as theorems, with a verified (KER) at beta_w, or with beta_w in the hand range.
- Or: (BASE) with numbers, a block step for classes at every effective coupling from the ultraviolet ceiling down to an end class, and an end criterion (Proposition CH).
- Or: a direct proof of the seed on the trajectory.

**8.4 What is not excluded (from check 1331 and from this file).** Structured exact evaluations of (KER) below the state-vector count; rational sum-of-squares certificates with a patch as large as the first passing witness torus; cut-dependent signed Gaussian bounds on the trajectory; block criteria on cubes only, with invariant readouts or typical boundary values, at the window; a certificate that treats the cutoff as a symbol; a carry that does not inspect every intermediate coupling. I found no instance of any of them with a proof or a cost bound.

**8.5 What a kernel-checked computation can serve now (ARGUED; row 1326 6.3 with the notes of check 1331 on the trusted base).** The numeric constants of the hand proofs, and exact small counterexamples. Not the seed.

**8.6 Suggestions for the lead (suggestions only).**

1. A check of this file by another model. In order: Theorem T (Steps 2 to 4, and the use of Lemma Z3, ONE-K and FL); Lemma CLIMB; Proposition FR (b) (is M_delta in the class of (E)?); Lemma SURF; Lemma K0; Propositions CH and PF.
2. For rows on the infrared carry: the target of Theorem T. A seed at every coupling above beta_w, at a size at most C exp(c beta), with c inside (A3). GUIDE: c below about 4.0 per unit of beta, against 2.7 for asymptotic freedom and about 3.3 at the window.
3. For the ultraviolet carry: Theorem T uses (UNIV-K) in the rate form (A1), with the dependence on ell written out. Rows 924 and 925 have the form eps_K <= C ell^4 q^K for the regular part only.
4. No row on a verified computation of the seed before (A2) exists with beta_w above the hand range.

**8.7 Not done.** I did not read the primary text of the account, of Balaban, or of any published paper. I did not search the literature for a block step at an effective coupling of order one, or for exact evaluation methods. I ran no lattice computation and no guide run of a model; the one run was an arithmetic check of the numbers quoted here. I did not re-check Lemma ONE-K, Lemma FL, Lemma Z3, Theorem S, Theorem SH or Theorem D-shape; I used them as their checks state them. The class of (E) is taken from row 837 2.1 and check 1331, not from the proofs. The flow bound (A0) and the bound beta > 5 are taken from check 1331. Nothing in this file is checked by another model.

**Credits.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text: the account, its first-passage data, its tori and its constants. Tadeusz Balaban: the block renormalization method and the ultraviolet stability theorem. Osterwalder and Seiler; Luscher: the transfer operator. Dobrushin; Dobrushin and Shlosman: the uniqueness condition and the block criteria. Frohlich, Simon and Spencer: long-range order of the three-dimensional O(4) model. Van Enter and Shlosman: the transition used in Proposition V. Anderson and Kruczenski; Kazakov and Zheng: the loop-equation bootstrap behind the sum-of-squares certificates (through rows 760 and 1326). OpenAI: the posted two-dimensional O(3) proof, as read in row 1007. In the lane: Claude Fable 5.2 (rows 697, 705, 708, 720, 978, 1326: Theorems S, SH, D-shape, TR, CRIT, ZD-c, Lemma Z3, Lemma DIM); Codex gpt-6-astra and gpt-6.2-astra (rows 699, 760, 767, 785, 848, 917, 925, 1323, 1331: Corollary S3', Theorem O, Theorem DOB in chord form, and the checks cited, among them the corrections of row 1331 that this file follows); Claude Opus 5.5 (rows 837, 916, 924, 1072, 1225, 1256: the finish line, Lemmas FL and ONE-K, Proposition CA-FAIL, Proposition PIN, and the checks cited).

RESULT: Row 1332 (Claude Fable 5.2 max, laptop subagent; author only, checked by no one; no lattice computation run; corrected against check 1331 during the run). NOT solved: no theorem whose only unproved hypothesis is a computable finite statement and whose conclusion is (SEED-FP) was found; no impossibility is proved; nothing in the chain is disproved. PROVED here GIVEN named statements: Theorem T, the theorem of the brief with two open hypotheses beside the finite one: given the account's flow bound, the ultraviolet carry (UNIV-K) in rate form eps_K <= C ell^4 q^K, and an infrared carry that takes a seed at one coupling beta_w to a seed at every larger coupling at a size at most C exp(c beta) with c < (log L)/kappa + log(1/q)/(4 kappa), kappa an upper bound for the flow step (kappa = B_sharp from the account), the one inequality (KER) on one pair of tori at beta_w gives (SEED-FP) (through Lemma Z3, ONE-K and FL); GUIDE: c below about 4.0 per unit of beta at one loop, against 2.7 for asymptotic freedom. PROVED here (elementary, unchecked): Lemma N (a list of evaluations cannot be the only hypothesis; every first-passage coupling is above 5 by check 1331); Lemma CLIMB (the engine with the Lipschitz bound of Theorem D-shape (d) carries a seed at size n up the coupling by at most 8.7e-9/n^4 in total, below 1e-12 at the window size); Lemma K0 (with that rate form the margin of ONE-K forces a base torus of more than (ell/L)[C ell^4 (L^4+1)/((1-q) phi_*)]^(log L/log(1/q)) sites on a side); Corollary COST with Lemma SURF (an explicit state-vector evaluation needs at least 2^129 coefficients on every pair the engine admits, and a term-by-term enumeration 2^(3V+3) assignments; by check 1331 these are not floors for every exact method); Proposition FR (the seed test tolerates a relative weight error of order 1/volume per site, and in the engine's class no more: the two-level models M_delta); Proposition CH (a chain of mass-preserving block steps into a robust end class gives (SEED-L) with no (UNIV-K)); Proposition PF (above any base measure there is an exactly consistent family of fine measures with the base's correlations and only the base lattice's translations). First failing steps: (UNIV-K) for the in-law base; the infrared carry for a window base; Proposition FR (b) for a robust seed; one block step at an effective coupling of order one for the chain; fine-lattice translation invariance for the exact carry. OPEN: (UNIV-K) in rate form, the infrared carry (NOCRIT with a rate, or (LEV_K)), a method with a demonstrated cost for (KER), the seed, the mass gap. Output library/gap-shrink-box-fable.md.
