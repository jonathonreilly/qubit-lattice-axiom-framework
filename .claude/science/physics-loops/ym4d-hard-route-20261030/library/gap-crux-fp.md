lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-12T00:17Z

# The crux from first principles, and its assumptions (row 712, `gap-crux-fp`)

Author run of Claude Fable 5.2 (model id claude-fable-5-2, max effort), Mac mini worker, one session, no subagents, pinned at commit ca30967e2. Started 2026-11-11T12:17Z. Research-stage working state. **No mass gap is claimed or proved here.** Nothing in this file is checked by another model.

**State of this file:** in progress. Parts are appended as they are done. The status block below is kept current.

**Marks.** PROVED = proved by hand in this file from the named inputs, not checked. PROVED GIVEN = proved from a named input; the input's check state is written. RECALLED = a known fact from memory, source named, not re-read in this run. GUIDE = a belief from physics or numerics; used in no proof. OPEN = not proved.

## Status block (kept current)

- Part 1 (first principles): done (Section 1). Proved there: P1 (the seed torus is at least 7.4 by 14.8 correlation lengths), P2 (the seed forces Z^tw/Z > 1 - 1/825). Conclusions C1 to C6.
- Part 2 (assumptions): done (Section 2). 29 assumptions in six groups, ranked in 2.7. Lemma 2.A: the glue half alone has no symmetric function, so Theorem S needs the flux sectors.
- Part 3 (compare): done (Section 3). New against the earlier work: the ranges where the tests bind, the N-test and the dimension test, Lemma 2.A, the form (C).
- Part 3b (tool blockage): done (Section 3b). 22 methods listed with reasons. Propositions T1 to T3: the worded U(1) and K7 tests are false, the valid form is proved, and below beta of about 1 the tests forbid nothing. Two verdicts are too strong in that range; one tool comes back (conditioning on one direction).
- Part 4 (attempts): Attempt 1 done (4.1): Lemma COV, Lemma REG (a uniform seed makes the free energy C^(1,1)), Proposition V (a weight test that rests on a theorem of van Enter and Shlosman). Attempt 2 done (4.2): Identity L (the flux half is the response of a three-dimensional spin model to antiperiodic boundary conditions), Proposition TW (the twist ratios for beta < 1/6, uniformly in the background), open statement (AS-bg). Attempt 3 done (4.3): Corollary C and (PHYS-SEED). Final section in progress.

## 0. What was read before Part 1 (the row's reading rule)

Read before Part 1, and nothing else of the gap files: FINISH.md header, rules and row 712; GOAL.md; `library/gap-crux-restate.md` Sections 0, 1 and 3.4 (Theorem S, Lemmas K, X, E, E', Corollaries S2, S3, S3'); the lead note and status block at the top of `library/gap-seed-shape.md` (Theorem SH, lines 1-36); `library/gap-transfer.md` lines 1-51 and Section 1 (the definitions and the trace identities). The attack files were not opened before Part 1 was written.

## 1. Part 1: from first principles

Written before any attack file was opened. Notation: torus with sides n = (n_1, ..., n_4); Z(n), F = log Z; box B = three sides; T_B the transfer operator; lambda_0 > lambda_1 >= ... its eigenvalues; m(B) = log(lambda_0/lambda_1); S(k; B) = sum over i >= 1 of (lambda_i/lambda_0)^k. "The seed at size n with threshold t" is S(n; (2n)^3) < t (t = 1/1650 by Theorem SH).

### 1.1 What is known to be true

Marks: DEF = a fact of the definitions. THM = a theorem; "THM, repo" is proved and checked in this repository; "THM, RECALLED" is a published theorem that I state from memory and did not re-read. GUIDE = a belief from physics or numerics.

| # | Item | Mark |
|---|---|---|
| F1 | The model is a finite product of copies of SU(2) with Haar measure and the weight exp(-beta A), 0 <= A <= 2 (number of plaquettes). Z(n) is positive, finite, and entire in beta. Every finite-volume quantity is real-analytic in beta. | DEF |
| F2 | Z(n) = Tr T^(n_mu) with T positive, trace class, top eigenvalue simple, ground state strictly positive. So m(B) > 0 for every finite box. | THM, repo (`gap-transfer.md`, check row 671). Origin: Osterwalder and Seiler 1978; Luscher 1977 (RECALLED) |
| F3 | Z is invariant under every permutation of the four sides. | DEF (lattice symmetry) |
| F4 | For fixed B, the function k -> Z(k, B) is the moment sequence of the eigenvalue counting measure of T_B. All spectral data of all boxes are in the one symmetric function Z on quadruples of integers. | DEF + F2 |
| F5 | Theorem S / SH: the seed at one size gives m(L^3) >= log(1/(K s))/n for every cube of side L >= 2n. It uses only F2, F3 and the finiteness of ell. It holds for every compact group, every dimension and every weight with a positive transfer operator. | THM, repo (`gap-crux-restate.md` 3.4, checks rows 698, 699; `gap-seed-shape.md`, check row 707) |
| F6 | The seed holds for beta < 1/18. | THM, repo (`gap-seed-sc.md` Theorem 1, check row 704; statement taken from row 712, file not yet read) |
| F7 | For small beta the cluster expansion converges: exponential clustering, area law, analyticity in beta. This holds for every compact group. | THM, RECALLED (Osterwalder and Seiler 1978; Seiler, Lecture Notes in Physics 159) |
| F8 | Four-dimensional U(1) at large beta has no area law and a massless phase. | THM, RECALLED (Guth 1980 for the Villain weight; Frohlich and Spencer 1982). I did not re-read which correlations have the proved power-law lower bound. |
| F9 | Four-dimensional Z_2 at large beta has a perimeter law. On a periodic box its flux sectors are degenerate up to a tunnelling term. | THM, RECALLED (Peierls argument; Wegner 1971 for the model) |
| F10 | SU(2) Wilson loops in the fundamental representation are bounded by Z_2 Wilson loops at the same beta. So the area law holds for SU(2) wherever it is proved for Z_2. | THM, RECALLED (Mack and Petkova 1979; Frohlich 1979) |
| F11 | At fixed time extent and large beta, the centre symmetry of the Polyakov loop is broken in infinite space. | THM, RECALLED (Borgs and Seiler 1983) |
| F12 | Three-dimensional U(1) (Villain) confines at every beta. | THM, RECALLED (Gopfert and Mack 1982). The only proved case of a gap-type statement at all couplings where perturbation theory shows no gap. |
| F13 | Ultraviolet stability of the four-dimensional theory under block renormalization at small effective coupling. | THM, RECALLED (Balaban, CMP 95-122); partly rebuilt in this target |
| F14 | SU(2) Wilson has no phase transition on the real beta axis. The correlation length is below one lattice unit for beta below about 2, and grows like exp(2.69 beta) at large beta (asymptotic freedom, two-loop factor left out). | GUIDE |
| F15 | The mixed fundamental-adjoint SU(2) weight has a first-order line that ends at a critical point near (beta_F, beta_A) = (1.5, 0.9). SU(N) Wilson for N >= 5 has a first-order bulk transition. SU(2) Wilson in five dimensions has a transition near beta = 1.6 to a phase with massless gluons. | GUIDE (Bhanot and Creutz 1981; Creutz 1979, 1981; RECALLED numerics) |
| F16 | Deconfinement lengths of SU(2) Wilson: N_c = 2, 3, 4, 8 at beta about 1.88, 2.18, 2.30, 2.51. Lightest glueball about 5.3 T_c, string tension about (T_c/0.69)^2. | GUIDE (RECALLED numerics; Fingberg, Heller and Karsch 1993) |

### 1.2 Reasoning up: four facts that follow at once

**P1 (the seed is not local; PROVED).** If S(n; B) < t then n m(B) > log(1/t). Proof: the top eigenvalue is simple, so (lambda_1/lambda_0)^n <= S(n; B) < t. QED. With t = 1/1650: the time side of the seed torus is more than 7.4 correlation lengths of its own box, and the space side more than 14.8. No statement at a smaller size can be the seed.

**P2 (the seed contains the vortex criterion; PROVED GIVEN (TM-c), checked rows 698, 699).** Let Z^(1 nu) be the partition function of the same torus with one twisted stack of (1, nu)-plaquettes. Then 0 <= 1 - Z^(1 nu)/Z <= 2 S/(1 + S), with S = S(n_1; B).
Proof. The centre flip C_nu is a substitution of variables that keeps Haar measure, so it maps positive functions to positive functions. It commutes with T. The top eigenvalue is simple with a positive eigenfunction Omega, so C_nu Omega = Omega. Choose a joint eigenbasis; let eps_i = +1 or -1 be the parity of the eigenvector i. Then Z - Z^(1 nu) = sum_i lambda_i^(n_1) (1 - eps_i) = 2 (sum over odd i of lambda_i^(n_1)) <= 2 lambda_0^(n_1) S, and every odd i is at least 1. Divide by Z = lambda_0^(n_1) (1 + S). QED
So the seed forces Z^tw/Z > 1 - 1/825 on the seed torus, for each of the three planes that contain the time direction. This is 't Hooft's criterion for confinement at one finite size. The seed is therefore two statements at once: (glue half) the thermal sum of the centre-even sector is small; (flux half) each twist changes Z by less than 0.13 percent.

**P3 (the seed is a pressure; DEF).** log(1 + S(n; B)) = F(n, B) - n log lambda_0(B). The right side is the free energy that the box B gains at temperature 1/n over its ground state. The seed says: at temperature 1/n the box of side 2n has thermal free energy below 1/1650.
GUIDE, from F16: a glueball gas reaches this at about 0.55 T_c. So n is about 1.8 N_c(beta): n = 3 up to beta about 1.3, n = 4 to about 1.8, n = 7 at 2.3, n = 14 at 2.5, and n grows like exp(2.69 beta) after that. (Leading strong-coupling orders give the same sizes: the wrapping tube of 4n plaquettes has weight u^(4n) times 3 (2n)^3 places, u = I_2(beta)/I_1(beta); this is below 1/1650 for n = 3 if u < 0.31 and for n = 4 if u < 0.40.)

**P4 (the smallest object; from F4, F5 and Theorem D (b) as quoted in `gap-crux-restate.md` 3.4).** The seed follows from Phi(n) = 16 F(n^4) - F((2n)^4) <= 1.9 x 10^(-4). So the smallest known carrier is a pair of numbers: the partition functions of two hypercubic tori, of sides n and 2n. One number cannot be enough: by F2 every single box has a gap, and what matters is how a quantity changes when the size doubles. In physical words Phi(n) is the total weight of everything that can tell the torus of side n from the torus of side 2n: particles that go around a cycle, flux sheets that wrap a 2-cycle.

### 1.3 What a proof must contain at the least

**(A) A step from one size to all sizes.** This exists: F5. It is blind to the group, to the dimension and to the weight.

**(B) One base inequality at a size of at least 7.4 correlation lengths (P1).** Because (A) is blind, all of the following must enter through (B), and (B) must fail in each of these cases (each is a model in the class of F5):

- U(1) in four dimensions at large beta (F8). So (B) must use that the group is not abelian, or that its centre is finite.
- Z_2 at large beta (F9), and the mixed weight in the limit of large beta_A. So the flux half of (B) must use that the group is connected.
- The mixed weight at its transition line and at its end point (F15, GUIDE). So (B) must use the shape of the Wilson weight, not only its symmetry and positivity.
- SU(N) Wilson at its bulk transition for N >= 5 (F15, GUIDE). So (B) must use N = 2 (or N <= 4).
- SU(2) Wilson in five dimensions at large beta (F15, GUIDE). So (B) must use the dimension.

The last two tests are not in row 712. I name them the N-test and the dimension test.

**(C) For the continuum gap, (B) uniformly in the lattice spacing on one physical torus.** The partition function of a torus is one number, whatever effective description is used. So Theorem S applies on the fine lattice as it is: if S(n_a; (2 n_a)^3) < t for a sequence of spacings a with n_a a = L fixed, the gap is at least log(1/(K s))/L in physical units along that sequence. The lattice gap at one fixed beta is neither needed for this nor enough.

### 1.4 Where the gap can come from

1. **Every finite box has a gap, for every compact group (F2).** It comes from compactness: T is trace class and improves positivity. This gap is at least exp(-24 beta N^3) and says nothing about uniformity.

2. **A gap can fail in two ways only, and P1 shows how.** If the seed fails at every size, every cube has a level within 7.4/n of its ground state at side 2n. Either that level is a massless excitation (energy of order 1/n from the momentum, as for the photon: exp(-pi) per mode at this shape), or it is a second vacuum (two phases at a first-order point; flux sectors of a broken centre symmetry). So the gap of SU(2) Wilson is the absence of three things: a massless particle, a coexistence point on the Wilson axis, a deconfined phase.

3. **Why U(1) has the first and SU(2) is believed not to (GUIDE).** The centre of U(1) is U(1). So the abelian model has a continuous symmetry that acts on lines (multiply the links by a flat U(1) field). In four dimensions it can break, and the photon is its Goldstone mode. In three dimensions it cannot, which agrees with F12. The centre of SU(2) is finite. If it breaks there is no Goldstone mode (F9: Z_2 has a bulk gap and degenerate flux sectors). SU(2) has no other continuous symmetry. This is the one structural difference that I can state from the definitions. It is not a proof: five-dimensional SU(2) has massless gluons at weak coupling with no symmetry reason (GUIDE).

4. **At beta below about 1.3: local disorder.** The correlation length is far below one lattice unit and the seed is believed true at n = 3 with a wide margin (P3). The plaquette weight varies by the factor exp(2 beta) over the group, and the entropy of the group wins. No structural fact is needed in this range: U(1) below beta = 1.01, Z_2 below 0.44 and the mixed weight below its line all have the gap too (GUIDE). So in this range the tests of (B) forbid nothing. What is missing is the strength of the estimates. I call this range R1.

5. **At larger beta: only the running of the coupling.** Plaquettes are ordered at the lattice scale. Each doubling of the scale lowers the effective beta by about 0.26 (one loop). The gap appears at the scale where the effective beta is of order one. The only known source of this drift is the one-loop determinant of the non-abelian fluctuations. It is a property of the fluctuations, not of the classical action. I call this range R2. A proof in R2 must contain, in some form, the statement that the flow goes one way: a quantity defined at each scale that moves toward disorder under doubling, for every value of the quantity, not only in the two end regimes.

6. **The flow in the language of F5.** Put s_k = S(2^k n; (2^(k+1) n)^3). Theorem S says s_(k+1) <= K s_k^2 when s_k < 1/K. This is the strong end of a step-scaling inequality, with 1/s as the coupling. Balaban's work (F13) controls a different coupling at the weak end. The crux is the middle: no quantity is known that is controlled at both ends, and no inequality is known in between. For U(1) at large beta the sequence s_k stays near a constant (scale invariance). For SU(2) at large beta it is believed to stay of order one to ten for about 3.9 beta doublings and then to fall.

### 1.5 First-principles conclusions (the list that Parts 2 to 4 use)

- **C1.** The crux is not one problem. In R1 (beta up to about 1.3 at n = 3; up to about 2 with n <= 5) it is a quantitative problem about a small box, and no test forbids a tool. In R2 it is a problem of many scales.
- **C2.** The words "a coupling of order one" hide this. For the lattice at fixed beta the first open point is beta = 1/18, deep inside R1, where the seed is true with a margin of many orders of magnitude (GUIDE).
- **C3.** For the continuum gap, R1 is not on the path. What is on the path is the seed on one physical torus, uniformly in the spacing (item (C)).
- **C4.** The seed is two statements (P2): a glue half and a flux half. The tests split the same way: U(1) and the critical end point attack the glue half; Z_2 attacks the flux half.
- **C5.** The least that (B) must use depends on the range. In R1: nothing beyond numbers. In R2: non-commutativity through the fluctuations, the shape of the weight, N, and the dimension.
- **C6.** A tool is not refuted by the fact that its proof also runs for U(1). It is refuted only if its hypothesis holds for U(1) at a coupling where the U(1) seed fails. Part 3b makes this exact.

## 2. Part 2: the assumptions exercise

Written after Part 1 and before the attack files were opened. Each line: the assumption; needed or habit; what follows if it is wrong; whether a change makes the problem easier; a check. "Needed by the method" means needed by Theorem S, not by the mass gap.

### 2.1 Group (a): the target statement

| # | Assumption | Needed or habit | If it is wrong or dropped | Easier? | Check |
|---|---|---|---|---|---|
| a1 | The gap is the gap of the transfer operator on periodic cubes at one fixed beta. | Habit for the Clay target, which is a continuum statement. | The target becomes item (C) of 1.3: the seed on one physical torus, uniformly in the spacing. R1 leaves the path. The lattice gap at beta = 2 is then not needed. | Not easier (R2 stays), but smaller: one range instead of two. | Exact: Theorem S applies on the fine lattice as it is (1.3 (C)). |
| a2 | The gap is on the whole space of the box, flux sectors included. | Needed by the method; not needed for a bulk gap. Z_2 at large beta has a bulk gap and fails the seed (F9). | If SU(2) had a bulk gap without confinement at some beta, the seed would be false at every size and the method could not see a true gap. Dropping a2 needs a new step from one size to all sizes. | No. See Lemma 2.A below: the glue half alone has no symmetric function. | P2 shows the flux half is forced by the seed. |
| a3 | Observables: every gauge-invariant function of one time slice. | Same as a2. | A gap for local observables in infinite volume is weaker and is what the Wightman theory needs. | Weaker target, but no finite criterion is known for it in a gauge theory (row 691 owns the one candidate, (DS-tw)). | - |
| a4 | The group is SU(2). | Set by T0 (SU(2) first). | SU(3): same problem. SU(N), N >= 5: the Wilson axis has a bulk transition (F15, GUIDE), so the lattice gap at every beta is false there and only (C) can be true. | No group is known for which the seed at a correlation length of order one is easier. | N-test of 1.3. |
| a5 | Dimension four. | Set by the target. | In three dimensions the correlation length grows like beta, not like exp(2.69 beta): R2 has about log_2(beta) doublings. Still open. | A smaller model of the same crux; not our target. | - |
| a6 | "At every beta", or "at a coupling of order one". | Habit. The continuum needs only large beta; the lattice statement at every beta is a separate theorem. | See C1 to C3. | The split R1/R2 makes two problems, each with fewer constraints. | - |

**Lemma 2.A (why a2 cannot simply be dropped; PROVED GIVEN (TM-c) and its extension to products of flips, which I have not seen stated; so this is a reduction with one named input).** The centre-even trace Tr(T_B^a P_0), P_0 = the projection on the functions that are even under all three flips, equals (1/8) times the sum of the partition functions over the 8 choices of twists in the planes (1,2), (1,3), (1,4). It is not invariant under the exchange of the directions 1 and 2: that exchange maps the planes (1,3), (1,4) to (2,3), (2,4). The smallest invariant object is the sum over all 64 twists of the six planes. Seen from any time direction, it is the trace over the even sector of the direct sum of the 8 boxes with magnetic twists. Reading: in a confining phase the magnetic twists cost exponentially little ('t Hooft's duality, RECALLED), so this direct sum has eight nearly equal top eigenvalues, and its thermal sum is near 7. So a seed for the centre-even sector cannot be obtained by symmetrizing over twists. A gap of the glue half alone needs a different step from one size to all sizes. OPEN.

### 2.2 Group (b): the lattice formulation

| # | Assumption | Needed or habit | If dropped | Easier? | Check |
|---|---|---|---|---|---|
| b1 | The Wilson weight. | Habit for the continuum target; fixed for the lattice statement. Theorem S holds for every weight with a positive transfer operator (for example the heat kernel weight, whose character coefficients are positive). | For target (C) any weight in the class may be chosen, also one that changes with the spacing. | Unknown. No weight is known whose seed is provable at a correlation length of order one. The heat kernel weight has the semigroup law K_t * K_s = K_(t+s); in two dimensions this solves the model, in four it does not. | The shape of the weight is the content of test K7 (Part 3b). |
| b2 | Isotropy: the same beta in all six planes. | Needed by the method: Theorem S uses the exchange of time with each space direction. | With two couplings, only the three space directions can be exchanged. The lemmas then give statements on screening lengths, not on the gap. The Hamiltonian limit (continuous time) is outside the method. | No. | - |
| b3 | Periodic boxes without twist. | Needed by the method. A twisted torus keeps the symmetry only if all six planes are twisted, and then the trace carries a flip and is not a sum of positive terms. A twist in the plane (3,4) alone keeps the lemmas K, X, E for the pair (1,2) only. | Free or fixed walls lose the trace formula in the cut direction. | No. Twists would remove the constant modes at weak coupling (RECALLED: Gonzalez-Arroyo and others), which helps a weak-coupling analysis but not the crux. | PROVED in this line from (TM-c): the plane (3,4) is spatial for both directions 1 and 2. |
| b4 | The time direction is a lattice axis and T is one lattice step. | Needed for F2. | - | - | - |

### 2.3 Group (c): the reduction

| # | Assumption | Needed or habit | If dropped | Easier? | Check |
|---|---|---|---|---|---|
| c1 | The proof goes through one finite box. | Habit, but any equal statement has the size of P1. Infinite-volume criteria (Dobrushin, cluster expansion, logarithmic Sobolev) are local and reach only where the coupling between neighbours is small. | A criterion weaker than the seed that still gives the gap could live at one or two correlation lengths. For ferromagnets this is the Simon-Lieb inequality. None is known for a gauge theory. | Yes if found: the box shrinks by a factor of about 7 in each side. | `gap-seed-shape.md`: the threshold rises to 1/10 at aspect ratio 6 and tends to 1. |
| c2 | The proof goes through Theorem S, so through F2 and F3 only. | Habit. | Other structure of Z is unused: reflection positivity in all hyperplanes at once (chessboard bounds), the twists, convexity in beta. | Unknown. | Part 4. |
| c3 | The seed is a trace (all states with multiplicity), not one ratio lambda_1/lambda_0. | Needed by the method: the doubling step bounds traces. | The multiplicity costs about log(3 (2n)^3) in the exponent, so about 1.5 correlation lengths of box size. | Slightly. | - |
| c4 | beta is the same at every step of the recursion. | Needed by the method. | A step that compares (beta, 2n) with (beta', n) would carry the seed from small beta to large beta. Every known comparison of this kind (Migdal and Kadanoff) is one-sided for the free energy and gives nothing for a ratio; it also flows to disorder for U(1), which is wrong (Tomboulis 2007; Ito and Seiler 2007, RECALLED). | Yes if found; this is the form "the flow goes one way" of 1.4. | - |
| c5 | The seed is proved at one beta at a time. | Habit. | The set G of beta at which the seed holds at some size is open (F1) and contains [0, 1/18). Its complement is closed. If the complement is not empty, its smallest point beta_c is a point where the seed fails at every size and holds at every smaller beta. So "the lattice gap at every beta" is equal to "there is no first critical point". | Not by itself. It changes what a tool must do: exclude a first critical point approached from the massive side. | PROVED in this line, given F1 and F5. |
| c6 | One tool proves the whole seed. | Habit. | P2 splits the seed. The flux half has its own exact tools (twists, F10). The glue half has none. | Yes for the flux half. | Part 3b. |

### 2.4 Group (d): the tests

| # | Assumption | Needed or habit | If wrong | Check |
|---|---|---|---|---|
| d1 | "A tool that also holds for U(1) cannot work." | As worded it is false: Theorem S and the cluster expansion both hold for U(1), and both work. The valid form is C6: a tool is refuted only if its hypothesis is true for U(1) at a coupling where the U(1) seed fails at every size. | Tools were set aside that are sound and useful in R1. In R1 the test forbids nothing, because U(1) has the gap below beta = 1.01 (GUIDE). | Part 3b proves the valid form and applies it to each verdict. |
| d2 | Test K7 (the mixed weight). | Same form. The test rests on numerics for the phase diagram (GUIDE), not on a theorem that I know. | If the mixed model has no transition where the numerics see one, the test is empty. If it has one, the valid form applies only at the couplings of the line. | Part 3b. |
| d3 | The two tests are enough. | Habit. | Part 1 adds the N-test, the dimension test, and Z_2 for the flux half. A tool that passes U(1) and K7 can still be unsound. | 1.3. |
| d4 | A tool whose constant depends on the gap is circular. | Mostly right. | Not circular if the dependence is on the gap of a smaller box (induction on the size), or if the tool is used in a proof by contradiction at a first critical point (c5). | Part 3b. |

### 2.5 Group (e): beliefs from physics

| # | Belief | If wrong | Does the method depend on it? | Check |
|---|---|---|---|---|
| e1 | No transition on the Wilson axis. | The lattice gap fails at one beta at least. The continuum gap can still hold. | The lattice target at every beta does. Target (C) does not. | Numerics only (GUIDE). The N-test shows that the belief is special to small N. |
| e2 | Confinement at every beta. | The seed is false where confinement fails, even if the bulk gap holds (a2). | Yes. | F10 gives it only where Z_2 confines. |
| e3 | Asymptotic freedom: the flow reaches disorder from every beta. | There is no gap at large beta and the problem is false. | Yes. | One loop is a computation; beyond it there is no theorem. |
| e4 | The seed box has n about 1.8 N_c(beta) (P3). | If the true size is larger, R1 ends at a smaller beta. | Only the plan. | A Monte Carlo run of the pressure at 0.55 T_c would test it (GUIDE only). |
| e5 | The seed is true at some size whenever the gap and confinement hold. | Then the method could fail to see a true gap. | Yes. | It needs a bound on the number of states; `gap-crux-restate.md` 3.4 says this is not proved. |
| e6 | There is no small number at the crossover. | A hidden small number would give an expansion. | - | At beta = 2.2 the loop factor g^2 N/(16 pi^2) is 0.023 and the strong-coupling parameter u is 0.47. Both series are believed to work up to the crossover from their own side (Creutz 1980, RECALLED), and neither is proved near it. |

### 2.6 Group (f): the rules of the work (owner rules; kept)

| # | Rule | What it costs here | What a different rule would give (not used) |
|---|---|---|---|
| f1 | A hand proof. | In R1 the seed is one inequality between two integrals over SU(2)^324 and SU(2)^5184 (n = 3). No hand method reaches it beyond small beta. | - |
| f2 | Lean-formalizable. | Nothing beyond f1. | - |
| f3 | No computer-assisted step. | Same as f1. | With rigorous machine bounds: the cluster expansion could be enumerated to a high order with a proved tail. I estimate (GUIDE) that this moves the proved range from 1/18 to a few tenths, not to 1.3. In R2 it gives nothing: the seed box at beta = 2.5 has more than 10^5 links and no small parameter. So this rule is not what blocks the crux. |

### 2.7 Ranking: how much the problem changes if the assumption is dropped

1. **a1 with a6** (fixed-beta lattice gap, "order one"). Dropping it removes R1 from the path of the continuum gap and leaves one statement: the seed on a physical torus, uniformly in the spacing.
2. **e1** (no transition on the Wilson axis). If false, the lattice target is false and only (C) stays.
3. **d1, d2 in the worded form.** Dropping the wording for the valid form re-admits every quantitative tool in R1.
4. **c4** (the same beta at every step). A proved comparison across couplings would be the missing statement itself.
5. **c1, c3** (the size of the criterion). A criterion at one or two correlation lengths would shrink the box by a factor of about 7 per side.
6. **a2** (flux included). Dropping it loses Theorem S (Lemma 2.A).
7. **b1** (the Wilson weight). Free for target (C).
8. **c5, c6** (one beta at a time, one tool).
9. **f** (the rules). Small effect on R1, none on R2.
10. **b2, b3, b4.** Needed by the method; no gain from a change.

## 3. Part 3: compare with the earlier work

Read for this part: `library/gap-mid-max.md` Sections 2, 5, 9, 10; `library/gap-skeleton-final.md` 13.11, 13.12; `library/gap-crux-restate.md` Section 4 (the flux half, to avoid a duplicate). Grep of `library/gap-*.md` and `library/prior/gap-*.md` for the key words of Parts 1 and 2.

| Item of Part 1 or 2 | Already in the earlier work? | Where |
|---|---|---|
| P1, the seed torus is at least 7.4 by 14.8 correlation lengths | Used as a guide (10.4 to 12 inverse masses from a gas model); the one-line bound is not stated | 13.11; row 706 |
| P2, the seed forces the twist ratios near 1 | **Yes, and stronger:** Identity FL, 1 + S = (1 + S_0)/(1 - U) | `gap-mid-max.md` Section 6 |
| P3, the seed as a pressure; the size n(beta) | Yes. Row 706 finds larger boxes than my estimate: n = 10 at beta = 2.30, n = 24 at 2.60. Use those numbers, not mine. | 13.11 |
| P4, the smallest object is two free energies | Yes | Theorem D, D-shape, Proposition Delta |
| (A) and (B): the step is blind, the group must enter in the base | Yes ("the fall has to come from the group") | 13.11 |
| Tests U(1), Z_2, K7 | Yes | `gap-mid-max.md` Section 2 |
| **N-test and dimension test** | **New.** No file names SU(N >= 5) or five dimensions. | - |
| (C), the seed on a physical torus, uniform in the spacing | Not found in the passages read. The target (GAP) of the final skeleton is a continuum statement; the files of rows 697 to 710 work at fixed beta. To be checked against 13.8 to 13.10 before use. | - |
| 1.4.2, a gap fails only by a massless level or a second vacuum | Yes in substance | Theorem CRIT, "What it says" |
| 1.4.3, the continuous centre symmetry of U(1) and its Goldstone mode | Yes | run 2, `gap-skeleton-max-b.md` line 114 |
| 1.4.5 and 1.4.6, "the flow goes one way"; step scaling | Yes | run 2, A5 (STEP); (CAS) |
| **C1, C2, the split R1 / R2, and "in R1 the tests forbid nothing"** | **New as a statement.** Theorem DOB's remark (3) accepts a group-blind tool at small beta; no file says where the tests start to bind. | Part 3b gives the ranges |
| C6, the valid form of the tests | Partly. 13.12 says "cannot give the seed at every coupling". The digests use the stronger form ("NO as an SU(2)-true/U(1)-false input"). | Part 3b |
| a2 with Lemma 2.A (the glue half has no symmetric function) | **New** | - |
| b3, a twist in the plane (3,4) keeps Lemmas K, X, E for the pair (1,2) | In substance yes: Remark F3 of `gap-crux-restate.md` 4.3 | - |
| c4, a comparison across couplings | Yes in another form: Theorem TR carries the seed along beta on one box, given (VIR_K) | `gap-mid-max.md` Section 4 |
| c5, "no first critical point" | **Yes:** Theorem CRIT and (NOCRIT) | `gap-mid-max.md` 5.1 |
| c6, the seed is two statements | Yes | Identity FL |
| d3, more tests are needed | New (N-test, dimension test; and Part 4 adds a test that rests on a theorem) | - |
| e6, both series are numerically good up to the crossover | Not found | - |
| f, the rules do not block R2 | Not found as a statement | - |

**Reading.** The earlier work had most of the structure: the split of the seed, the first critical coupling, the tests U(1) and K7, and the remark that the Wilson weight is log-linear in x. What Parts 1 and 2 add: the ranges in which the tests bind; two more tests; Lemma 2.A; and the form (C).

## 3b. Part 3b: the tool blockage

### 3b.1 The methods that were set aside, and the reason given

From the files of Part 3 and the digests `prior/gap-crux-lit-2.md` (synthesis, C1, "Routes bounded"), `prior/gap-crux-lit-cross.md` (synthesis), `prior/gap-crux-lit-nonab.md` (synthesis), `prior/gap-seed-lit.md` (final synthesis). The digests were read at their synthesis sections only.

| # | Method | Reason given | Kind |
|---|---|---|---|
| 1 | Correlation inequalities of Griffiths type (Griffiths, Kelly, Sherman; Ginibre) | They hold for Z_2 and U(1), where the seed fails | U(1) |
| 2 | Dual forms with positive weights (surfaces, currents) | The same | U(1) |
| 3 | A monotone quantity along the scale (the deficit kappa; (CAS); step scaling) | It exists for every group; strictness restates the seed | restates |
| 4 | Derivative in beta, (VIR_K) and (DEF_K) | Three ways failed: the pointwise constant is off by a factor 8; the locality constant depends on the gap; convexity bounds second derivatives | gap; wrong quantity |
| 5 | Curvature: Bakry and Emery (Shen, Zhu and Zhu; (BE-block)) | The tensor is negative above beta = 1/3 at an explicit configuration; published range abs(beta) < 1/(16 (d - 1)) in the normalisation of that paper (as read in the digest; not converted here) | small number; K7 |
| 6 | Dobrushin's condition on one link (Theorem DOB; `gap-zf-box-x.md`) | alpha = 18 beta < 1; with the sharp one-link bound about 0.10 | small number |
| 7 | Cluster expansion (Osterwalder and Seiler; `gap-seed-sc.md`) | beta < 1/12800 in the written form | small number |
| 8 | Zeros of Z in complex beta, continued along the coupling | The zero-free radius shrinks like a power of the gap; the continuation ends at a finite coupling | gap |
| 9 | Polchinski flow and two-scale logarithmic Sobolev criteria (Bauerschmidt and Bodineau; Otto and Reznikoff) | A Hessian bound at every scale is needed; it would not tell U(1) from SU(2) | U(1); unverified |
| 10 | Migdal-Kadanoff bounds (Tomboulis) | An unproved inequality (Ito and Seiler); the argument would also confine U(1) | U(1) |
| 11 | Simon and Lieb; Aizenman and Simon (gap above the mean-field temperature for N-component ferromagnets) | A spin system; it includes O(2), so "NO as an SU(2)-true/U(1)-false input" | U(1) |
| 12 | Infrared bounds (Frohlich, Simon and Spencer) | They prove order, not decay | wrong quantity |
| 13 | Durhuus and Frohlich: gauge theory in d dimensions against the sigma model in d - 1 (run 1, B8) | The comparison model orders at large beta; a comparison across two dimensions is open | large beta |
| 14 | Loop equations and bootstrap (Kazakov and Zheng; (BOOT_eps)) | Numerical optimisation; bounds for local observables, not for two volumes | rule f; wrong quantity |
| 15 | Twist ratios: Tomboulis and Yaffe, Kanazawa; (TUBE'); the Z_2 splitting of Mack and Petkova | The premise is open at the needed coupling; "no bound follows from the identity alone" | open |
| 16 | Finite-size criteria for frustration-free chains (Knabe; Lemm and Mozgunov) | Another setting; excluded by the rate filter | setting |
| 17 | Exact duality in three dimensions (Gopfert and Mack) | Abelian only | setting |
| 18 | Small-volume spectrum (Luscher; Koller and van Baal) | Small volume only | setting |
| 19 | Curvature of the orbit space (Singer; Mondal) | Heuristic; depends on a regulator | unverified |
| 20 | Random-cluster sharpness for gauge models (Duncan and Schweinhart) | Potts gauge models only | setting |
| 21 | Mixing hypotheses on a box, (W), (DS-tw) (row 691) | A hypothesis; no verification at order one | open |
| 22 | Large N (Kopper for O(N)) | N must be large | small number |

### 3b.2 First principles: what a tool must do

**From the definitions.** By Theorem D-shape (13.11) the seed is 2 F(a, B) - F(2a, B) <= log(1 + t), about 6 x 10^(-4) at r = 2. Each F is of the order of the volume, 6 beta a abs(B) at most. So a tool must control the difference of two extensive quantities to an absolute error of 6 x 10^(-4). A bound on each term cannot do this. Only two kinds of statement can:

- (i) **locality**: the difference is a sum over places of responses to a far change, and each response is exponentially small in the distance (Lemma M and Proposition MIX of `gap-mid-max.md` are this form);
- (ii) **an identity** that removes the extensive part exactly.

Every method of the table that proves something is of kind (i): it proves a contraction at the lattice scale (lines 5, 6, 7, 9, 22) and so needs a small number at that scale. The methods of kind (ii) (lines 3, 4, 12, 14) give a sign or a bound on the wrong side. This is the blockage in one sentence: **a contraction is known only at the scale where it is visible in one step, and no identity is known.** A contraction at a larger scale is an induction over scales, and its base step is a computation with no small number.

**The least that a tool must use, by range.** The tests give this as a list of models in which the seed fails at every size. A tool must use a property that fails in each of them. The marks say how each failure is known.

| Model where the seed fails | Known how | What the tool must use | From which beta of the Wilson SU(2) axis the test binds |
|---|---|---|---|
| U(1) Wilson at large beta | THM, RECALLED (F8) for large beta; numerics for beta > 1.01 | the group is not abelian | about 1.01 for a tool that sees the weight only on a maximal torus (Proposition T3) |
| Z_2 at large beta | THM, RECALLED (F9) | the group is connected (flux half only) | about 0.44 (GUIDE: the self-dual point) for a tool blind to the difference of SU(2) and its centre |
| Mixed weight K7 on its line | GUIDE (numerics) | the weight is not too convex in x | about 1.6 for a tool that sees only the oscillation of log w; about 3.9 for one that sees only its Lipschitz constant in x (numbers in 3b.3) |
| Weight exp(beta ((1+x)/2)^p), p large | THM (van Enter and Shlosman; Proposition V of Part 4) | the same; and: a single well is not enough | large (of the order of log p) |
| SU(N) Wilson, N >= 5 | GUIDE (numerics) | N <= 4; for SU(2), that the group is a round sphere | at the bulk transition |
| SU(2) Wilson in five dimensions | GUIDE (numerics) | the dimension | about 1.6 |

So below beta of about 1 no test asks anything of a tool. Above about 2 a tool must use all of: a non-abelian connected group, a weight close to log-linear in x, N <= 4, dimension at most four. No single exact property does it. In particular the remark of 13.12, "a proof must use the Wilson weight itself, which means its loop equations", is too narrow in two ways. First, the family exp(beta ((1+x)/2)^p) contains the Wilson weight at p = 1 and has a transition at large p, with every qualitative property of the Wilson weight except linearity (single well, monotone in x, positive characters, same continuum limit). So what a tool must use is a bound on the non-linearity, a number, not a qualitative property. Second, the loop equations are not the only place where the linearity of the weight is used: see line 12 in 3b.4.

### 3b.3 The two tests: what is valid, what is not

A model of the class: a compact group, a positive class function w as one-plaquette weight with non-negative character coefficients, a dimension, a coupling. Seed(M) means: there is a >= 3 with S(a; (2a)^3) below the threshold of Theorem SH. A tool is a hypothesis H on models together with a proof of "H(M) implies Seed(M)" for every model M of a class that contains SU(2) Wilson.

**Proposition T1 (the valid form; PROVED, it is logic).** If M' is in the class of the tool and Seed(M') is false, then H(M') is false. So a tool is refuted by one model in its class with H true and the seed false. It is not refuted by a model with H true and the seed true, and not by the fact that its proof also runs for that model.

**Proposition T2 (the worded form is false; PROVED by two examples).** "A tool that also holds for U(1) (or for the weight of K7) cannot give the seed" is false. Example 1: Theorem DOB. Lemma DC is blind to the model, and Lemma INF holds for U(1), for Z_2 and for the mixed weight with the oscillation of the one-link exponent in place of 4 s. The tool gives the seed for SU(2) at beta < 1/18. Example 2: the cluster expansion of `gap-seed-sc.md`. Both are sound because their hypothesis fails for U(1) at every coupling where the U(1) seed fails.

**Proposition T3 (the range form; PROVED GIVEN the failure of the seed in the comparison model).** Let H be blind to a difference of two models: H(M at coupling beta) implies H(M' at coupling beta). Then the tool proves nothing for M at any beta at which Seed(M') fails. Proof: T1. Three uses:

- *Blind to the group beyond a maximal torus.* On a maximal torus the SU(2) Wilson weight exp(beta cos phi) is the U(1) Wilson weight at the same beta. Lemma INF is blind in this sense. Such a tool ends below beta_U := the smallest beta at which the U(1) seed fails at every size. RECALLED theorem (F8): beta_U is finite. GUIDE: beta_U is about 1.01.
- *Blind to the weight beyond its oscillation.* At the end point of the K7 line, (beta_F, beta_A) = (1.48, 0.90), log w = beta_F x + beta_A (4 x^2 - 1)/3 has its minimum at x = -3 beta_F/(8 beta_A) = -0.617, value -0.756, and its maximum 2.38 at x = 1. The oscillation is 3.14, which is that of the Wilson weight at beta = 1.57. The Lipschitz constant in x is beta_F + 8 beta_A/3 = 3.88. (GUIDE values of the end point; the arithmetic is by hand.)
- *Blind to the dimension, or to N.* The tool ends below the transition of the five-dimensional model, or of SU(5).

**Corollary (what the tests forbid).** A tool whose hypothesis is a number computed from the one-plaquette weight and the incidence numbers of the lattice (Dobrushin, Bakry and Emery, cluster expansion: lines 5 to 7) is sound, and the tests bound its range by about beta = 1 (U(1)) and 1.6 (K7). These tools stop at 0.1 to 0.33 for their own reasons, far below the bound of the tests. So in R1 the tests explain nothing. What stops the tools there is the size of their constants.

**Standing of the two tests.** The U(1) test rests on a theorem only at large beta. Test K7 rests on numerics. Proposition V in Part 4 gives a test of the same kind that rests on a published theorem.

### 3b.4 Each verdict: what it assumes, and what follows if it is wrong

| # | The verdict assumes | Valid? | If wrong, or what is left |
|---|---|---|---|
| 1, 2 | The tool is the mechanism by itself, at every beta | Valid above beta_U. Moot: no such inequality or dual form is known for SU(2). | Nothing to bring back. |
| 3 | Monotone is not strict | Valid. | - |
| 4 | The constant is needed at the same box and coupling | Valid as computed there; I did not re-derive it. | The form (VIR-log) stays; row 710 owns it. |
| 5 | The criterion is pointwise in the configuration | Valid in that form (Proposition BE is a counterexample, not an estimate). | An averaged form is a mixing hypothesis (row 691). |
| 6, 7 | The small number is the bare beta, and all 18 neighbours of a link count | **Too strong for the flux half.** By conditioning on all links but those of one direction (the idea of line 13), the flux half needs a contraction with 6 neighbours, not 18. | Part 4, Attempt 2: Proposition TW proves the flux half for beta < 1/6. |
| 8 | The radius depends on the gap as a power | Valid as reported; not re-derived. | - |
| 9 | A Gaussian reference measure with scales exists | Valid: Haar measure is a product, so there is no flow to integrate. The remark "it would not tell U(1) from SU(2)" is the worded test and adds nothing. | - |
| 10 | - | Valid at large beta by T1 (U(1) fails there). | - |
| 11 | The input must be false for U(1) | **Not valid in R1** (T2). The true obstacle is another one: in a gauge theory the spin model appears only after conditioning, with a background gauge field, and the inequalities of Aizenman and Simon need ferromagnetic couplings. | Dobrushin's estimate is uniform in the background and replaces them: Part 4, Attempt 2. Open: a gap above the mean-field temperature, beta < 2/3, uniformly in a background (statement (AS-bg) there). |
| 12 | The quantity bounded is on the wrong side | Valid. But the method deserves a line: Gaussian domination is the one classical tool whose proof uses exactly the linearity of the Wilson weight in the coordinates of R^4 (x_p = 1 - (1/2) abs(u - u')^2 for a time-like plaquette in temporal gauge). Its proof fails for the weight of K7 and for the weights of Proposition V. It holds for U(1), Z_2 and every SU(N). It gives the mean plaquette at least 1 - 2/beta (RECALLED method of Frohlich, Simon and Spencer; the gauge form is not proved here). | It passes K7 "the right way" and fails the U(1) test and the N-test. So it cannot be the mechanism. It shows that the loop equations are not the only carrier of the weight. |
| 13 | The tool is used at large beta | **Not valid in R1.** | Part 4, Attempt 2. |
| 14 | Rule f | Valid under the rule. | - |
| 15 | - | The flux half is open at order one. | Part 4, Attempt 2 gives a second exact form of it (Identity L). |
| 16 to 20, 22 | The setting differs | Valid. | - |
| 21 | - | A hypothesis, not a tool. | - |

**Summary of 3b.** No verdict that matters at a correlation length above one lattice unit is wrong. Two verdicts (lines 11 and 13) and the reading of lines 6 and 7 are too strong below it: they discard a tool by the worded U(1) test or by its failure at large beta, in a range where neither applies. The tool that comes back is the conditioning of Durhuus and Frohlich with Dobrushin's estimate. It goes to Part 4.

## 4. Part 4: real attempts

Rule 0a, done before each attempt. Grep of `library/open-core.md`: no entry on the gap, the seed, the twist ratio or a first-order transition. Grep of the FINISH rows and of `library/gap-*.md`, `library/prior/gap-*.md`: "van Enter" has no hit; "antiperiodic" has hits only in the twist files of route T (another object: the thin torus); "Durhuus" only in run 1 (B8) and in the final skeleton, as a route that was set aside. The open statements (TUBE'), (VORT), (MF) at a coupling of order one belong to rows 697 and 708 and are not attacked here. Attempt 2 proves (MF) in a range of strong coupling by a tool that those rows did not use, and names one open statement that no row holds.

### 4.1 Attempt 1: a test that rests on a theorem (Lemma COV, Lemma REG, Proposition V)

**Aim.** Test K7 rests on numerics. I replace it by a test that rests on a published theorem, and I show what that test excludes. The step that was missing is a lemma of this file: on an interval of couplings with a uniform seed, the free energy density is differentiable. So a point where it is not differentiable is a point where the seed fails at every size.

**Setting.** A model of the class with one-plaquette weight exp(beta phi(U)), phi a continuous class function with values in [-1, 1] and non-negative character coefficients. F(n; beta) = log of the integral of exp(beta sum_p phi_p). f(beta) = inf over n of F(n)/abs(n) = the limit along cubes (F/abs(n) is non-increasing in each side, `gap-crux-restate.md` Section 1). Input (TM-gen): the statements (TM) and Lemma 4.1 (a) of `gap-mid-max.md` (the thermal sum of a fixed box is continuous in beta) hold for this weight. For the Wilson weight both are proved and checked (rows 671, 709). For a general phi I did not re-read the proofs; the kernel is continuous, positive and of positive type, which is what the statements of `gap-transfer.md` name. This is an unchecked input.

**Notation.** Cube of side D, time extent D. That = T/lambda_0 = P_0 + Rhat, P_0 the projection on the ground state, Rhat = That (1 - P_0). r = lambda_1/lambda_0 = exp(-m). For j >= 1: the operator norm of Rhat^j is r^j, its trace norm is S(j) = S(j; D^3), its Hilbert-Schmidt norm is S(2j)^(1/2).

**Lemma COV (covariance on the torus from the gap and the thermal sum; PROVED GIVEN the trace formula with insertions, see the proof).** Let D >= 4 be even, and let sigma := S(D/2; D^3) <= 1/2. Let A and B be measurable functions with abs(A), abs(B) <= 1. Let A depend only on the two slices t_A, t_A + 1 and the time-like links between them, and B the same for t_B. Let the cyclic distance d of t_A and t_B be at least 2. Then

abs( <AB> - <A><B> ) <= 2 (1 + sigma) r^(d - 1) + 5 sigma.

Proof. Step 1 (insertions). By (1.2) of `gap-transfer.md`, exp(-S) is the product over the layers of T_0(U(t), g_t . U(t+1)), and each g_t occurs in one factor. So the integral of A exp(-S) over the time-like links is the product of the kernels A_T(U(t), U(t+1)) with the one factor of the layer t_A replaced by A_T^A(u, v) := the integral over h of A(u, h, v) T_0(u, h . v). The same holds with two insertions in two different layers. abs(A_T^A) <= A_T pointwise. Let T_A be the integral operator with kernel A_T^A. For f, g in L^2: abs(<f, T_A g>) <= <abs(f), T abs(g)> <= lambda_0 times the norms. So the norm of That_A := T_A/lambda_0 is at most 1. With a = d - 1 >= 1 and b = D - 2 - a >= a (the shorter way is taken, so d <= D/2):

Z <AB> = Tr(T_A T^a T_B T^b), Z <A> = Tr(T_A T^(D-1)), Z = Tr T^D.

(The trace of a product of at least two integral operators with bounded continuous kernels on a compact space is the integral of the cyclic product of the kernels: A0 (e) of `gap-transfer.md`, used there for (1b) and (1c). I use it with the kernel A_T^A, which is bounded and measurable; if A is not continuous this is one more application of Fubini. Not re-proved.)
Step 2 (expansion). Put That^a = P_0 + Rhat^a and That^b = P_0 + Rhat^b. With alpha = <Omega, That_A Omega> and gamma = <Omega, That_B Omega>, both in [-1, 1]:

N_AB := Tr(That_A That^a That_B That^b) = alpha gamma + <Omega, That_B Rhat^b That_A Omega> + <Omega, That_A Rhat^a That_B Omega> + Tr(That_A Rhat^a That_B Rhat^b).

The second term is at most r^b, the third at most r^a. The fourth is at most the norm of That_A Rhat^a That_B times the trace norm of Rhat^b, so at most r^a S(b); it is also at most the product of the Hilbert-Schmidt norms of That_A Rhat^a and That_B Rhat^b, so at most (S(2a) S(2b))^(1/2). If b >= D/2, the first bound gives at most sigma. If b < D/2 then a = b = D/2 - 1, and the second bound gives S(D - 2) <= sigma (D - 2 >= D/2). So N_AB = alpha gamma + E_AB with abs(E_AB) <= 2 r^a + sigma.
In the same way N_A := Tr(That_A That^(D-1)) = alpha + E_A with abs(E_A) <= S(D - 1) <= sigma, the same for B, and N_1 := Tr That^D = 1 + S(D), S(D) <= sigma.
Step 3. <AB> - <A><B> = (N_AB N_1 - N_A N_B)/N_1^2, and N_AB N_1 - N_A N_B = alpha gamma S(D) + E_AB (1 + S(D)) - alpha E_B - gamma E_A - E_A E_B. Its absolute value is at most sigma + (2 r^a + sigma)(1 + sigma) + 2 sigma + sigma^2 = 2 (1 + sigma) r^a + 4 sigma + 2 sigma^2 <= 2 (1 + sigma) r^a + 5 sigma (sigma <= 1/2). N_1 >= 1. QED

**Lemma REG (a uniform seed makes the free energy C^(1,1); PROVED GIVEN Theorem S and Corollary S3' (checked, rows 698, 699), Lemma COV, (TM-gen)).** Let I be an open interval of couplings. Assume there are an integer n >= 3 and q < 1 with 5041 S(n; (2n)^3; beta) <= q for every beta in I. Then f is differentiable on I and f' is Lipschitz there, with a constant C(n, q).

Proof. Put D_k = 2^(k+1) n and f_k = F(D_k^4)/D_k^4. Then f_k tends to f pointwise. Each f_k is smooth and convex, with f_k'' = D_k^(-4) Var(sum_p phi_p). By translation invariance, f_k'' is the sum, over the six orientations o, of the sum over all plaquettes p' of Cov(phi_(p_o), phi_(p')), where p_o is one fixed plaquette of the orientation o.
Fix beta in I and k. By Theorem S and Corollary S3', sigma_k := S(D_k/2; D_k^3) <= q^(2^k)/5041 and r <= q^(1/n). For two plaquettes let delta be the largest over the four directions of the cyclic distance of their base points. Every plaquette lies in a layer of two neighbouring slices of each direction (a plaquette orthogonal to the direction is a function of one slice). If delta >= 2, Lemma COV with that direction as time gives abs(Cov) <= 2.001 r^(delta - 1) + 5 sigma_k. If delta <= 1, abs(Cov) <= 1; there are at most 6 x 3^4 = 486 such p'. The number of base points with delta = j is at most (2j+1)^4 - (2j-1)^4 = 64 j^3 + 16 j <= 72 j^3 for j >= 2. So

f_k'' <= 6 ( 486 + 865 (sum over j >= 2 of j^3 q^((j-1)/n)) + 30 D_k^4 sigma_k ).

D_k^4 sigma_k <= 16 n^4 2^(4k) q^(2^k)/5041, which is bounded in k. So f_k'' <= C(n, q) for all k and all beta in I.
Now let x be in I. abs(f_k'(x)) <= 6. Take a subsequence along which f_k'(x) tends to some g. For y in I: f_k(y) <= f_k(x) + f_k'(x)(y - x) + C (y - x)^2/2. In the limit, f(y) <= f(x) + g (y - x) + C (y - x)^2/2. f is convex. If g' is a subgradient of f at x, then (g' - g)(y - x) <= C (y - x)^2/2 for all y near x, so g' = g. A convex function with one subgradient at x is differentiable at x. The same inequality at two points gives the Lipschitz bound. QED

**Remark.** Lemma REG is one direction only. It says nothing at a point where the seed fails at every size.

**The theorem that is used (read in this run; not checked).** A. C. D. van Enter and S. B. Shlosman, "Provable first-order transitions for liquid crystal and lattice gauge models with continuous symmetries", arXiv:cond-mat/0306362 (the later version is Commun. Math. Phys. 255 (2005), "Provable first-order transitions for nonlinear vector and gauge models with continuous symmetries"). I fetched the preprint and read its page 4 to 7. Theorem 2 there: "For lattice gauge models with plaquette action ((1 + L(U_P))/2)^p, (where L(U_P) = Tr(U_P + U_P^*)) in dimension 3 and more and p high enough, there is a first order transition, that is there exists a temperature at which the free energy is not differentiable in the temperature parameter." The text before it says that the variables are in "a compact continuous gauge group, e.g. U(1), SU(n)", "(with either abelian or non-abelian symmetries)", and writes the argument "in the simplest case of a U(1)-invariant interaction in 3 dimensions", by reflection positivity and chessboard estimates. Two points are open for our use and I mark them: the normalisation of L (in their formula (3) for U(1) the base is (1 + cos)/2, in [0, 1]; I read the SU(2) case as (1 + x)/2 with x = (1/2) tr U_P); and the proof for SU(2) in four dimensions is stated, not written.

**Proposition V (a theorem-backed weight test; PROVED GIVEN Theorem 2 of van Enter and Shlosman for SU(2) in four dimensions with the base (1 + x)/2, Lemma REG, (TM-gen)).** Let w_p(U) = exp(beta ((1 + x)/2)^p), x = (1/2) tr U, p a positive integer.
(a) w_p is in the class: ((1 + x)/2)^p is a polynomial in the character of the fundamental representation with non-negative coefficients, products of characters of SU(2) are sums of characters, and the exponential series keeps non-negative coefficients for beta >= 0. For p = 1 it is the Wilson weight at the coupling beta/2, times a constant.
(b) For every p for which the cited theorem holds, with beta_t its point of non-differentiability: S(a; (2a)^3; beta_t) >= 1/5041 for every a >= 3.
Proof of (b). If S(a; (2a)^3; beta_t) < 1/5041 for one a, then by continuity in beta ((TM-gen)) there are an open interval I around beta_t and q < 1 with 5041 S(a; (2a)^3; beta) <= q on I. By Lemma REG f is differentiable at beta_t. QED

**What Proposition V excludes.** Every w_p has: the group SU(2), its centre and the twists with zero classical cost, reflection positivity, positive character coefficients, the Ricci curvature of the group, one maximum at the identity and no other local maximum (it is increasing in x), and the same quadratic form at the identity up to the factor p (so the same weak-coupling limit; GUIDE for the one-loop coefficient). By Proposition T1, no tool whose hypothesis follows from these properties can give the seed at every coupling. This is the statement that 13.12 draws from K7, now from a theorem. It also adds one thing that K7 does not show: **one maximum is not enough.** The weight of K7 has a second local maximum at U = -1 on its whole line (log w is increasing in x only for beta_A <= 3 beta_F/8, and the end point has 0.90 > 0.56). So K7 left open that "one well" is the separating property. Proposition V closes that door: w_p has one well for every p.

**What is left as the separating property.** In the family w_p the Wilson weight is the member p = 1. The transition is proved for large p and believed absent at p = 1. So the family has a threshold in p. The property that a tool must use is therefore a bound on a number (how far log w is from a linear function of x), not a qualitative property. This agrees with K7, where the transition needs beta_A/beta_F above about 0.6.

**Marks.** Lemma COV and Lemma REG: PROVED GIVEN the named inputs, not checked. Proposition V: PROVED GIVEN the cited theorem in the reading above; that reading is the weak point. No statement about the Wilson weight is proved in this attempt.

### 4.2 Attempt 2: the tool that comes back. One direction at a time (Identity L, Proposition TW, statement (AS-bg))

**Idea (Durhuus and Frohlich 1980, RECALLED through run 1, B8; their paper was not read).** Given all links but those of one direction, the links of that direction are spin models on the layers, with nearest-neighbour couplings, in a background. Run 1 set the idea aside because the comparison model orders at large beta. Here it is used for another purpose and in another range: the flux half of the seed needs only the layer model, so it needs a contraction with 6 neighbours and not 18.

**The layer model.** B a spatial box with sides b_1, b_2, b_3 >= 3, u and v two configurations of the spatial links (elements of X). For h in G^B (one element of SU(2) at each site) and a spatial link b = (x, i) put y_b(h) = (1/2) tr( h(x) v_b h(x + e_i)^(-1) u_b^(-1) ), a number in [-1, 1], and

I(u, v) = the integral over h of the product over b of exp(-beta (1 - y_b(h))).

By (1a) of `gap-transfer.md`, the kernel of the transfer operator is A_T(u, v) = exp(-(V(u) + V(v))/2) I(u, v). So I(u, v) is the partition function of a spin model on B with values in SU(2), in the background (u, v). For u = v = 1 it is the O(4) model, y_b = <h(x), h(x + e_i)>.

**Identity L (PROVED from (1a), (1b) of `gap-transfer.md` and (TM-c)).** For k in Z_2^3 let c^k be the product of the centre flips c_nu with k_nu = 1, and Z[k] = Tr(T^t C^k) (as in Identity FL). Then on every torus with time extent t >= 3 and spatial box B:

Z[k]/Z = E( I(u, c^k v)/I(u, v) ),

where (u, v) = (U(t-1), U(0)) are two neighbouring time slices and E is the expectation of the torus measure.
Proof. (C^k f)(v) = f(c^k v), and c^k is an involution that keeps the Haar measure. So T C^k is the integral operator with kernel A_T(u, c^k w). The trace of T^(t-1) (T C^k) is the integral of A_T(u_0, u_1) ... A_T(u_(t-2), u_(t-1)) A_T(u_(t-1), c^k u_0), and Z is the same integral without c^k. A_T > 0. Divide. A spatial plaquette contains zero or two flipped links, so V(c^k v) = V(v), and the ratio of the kernels is I(u, c^k v)/I(u, v). QED

In the layer model, the flip v -> c_nu v changes the sign of y_b on the bonds of direction nu that cross one plane. So I(u, c_nu v) is the layer model with antiperiodic boundary conditions in the direction nu. **The flux half of the seed is the mean, over two neighbouring slices, of the response of a three-dimensional spin model to antiperiodic boundary conditions.** With Identity FL: U = (1/8) times the sum over k not 0 of E(1 - I(u, c^k v)/I(u, v)).

**Proposition TW (the twist ratios for beta < 1/6, uniformly in the background; PROVED GIVEN Lemma DC of `gap-mid-max.md` Section 10, checked in row 709 with two added lines).** Let beta < 1/6 and alpha = 6 beta. For every box B with sides at least 3, every u, v in X and every direction nu:

abs( log( I(u, c_nu v)/I(u, v) ) ) <= 4 beta (abs(B)/b_nu) alpha^(floor(b_nu/2) - 1)/(1 - alpha).

So on every torus with spatial cube b^3 and time extent at least 3: U <= 6 beta b^2 alpha^(floor(b/2) - 1)/(1 - alpha). The bound does not depend on the time extent.

Proof. Step 1 (influence). The one-site conditional law of h(x) has density proportional to exp(beta sum of J_b y_b over the six bonds at x), with couplings J_b in [-1, 1]. Let y be a neighbour of x, joined to x by the bond b. As a function of h(x), y_b = (1/2) tr(h(x) M) with M in SU(2) fixed by h(y), u_b, v_b (if x is the end point of b, use tr(g^(-1)) = tr(g)). A change of h(y) changes M to M'. M - M' = a_0 + i a.sigma with (a_0, a) real of length at most 2, so the exponent changes by a function of oscillation at most 4 beta. As in Lemma INF of `gap-mid-max.md`, the total variation distance of the two conditional laws is at most beta. Sides at least 3: the six neighbours are distinct and each shares one bond with x. So the influence matrix has row sums alpha <= 6 beta, for every background and all couplings in [-1, 1].
Step 2 (a path of couplings). Let Sigma_0 be the bonds of direction nu that the flip c_nu changes; choose the coordinate so that they go from x_nu = b_nu - 1 to x_nu = 0. For theta in [0, 1] let J^theta be 1 - 2 theta on Sigma_0 and 1 elsewhere, and I_theta the partition function with these couplings. I_0 = I(u, v), I_1 = I(u, c_nu v), and d/d theta log I_theta = -2 beta times the sum over b in Sigma_0 of <y_b>_(J^theta).
Step 3 (a flip). Let j_1 = floor(b_nu/2), Sigma_1 the bonds of direction nu from x_nu = j_1 - 1 to j_1, and H the set of sites with 0 <= x_nu <= j_1 - 1. The bonds with exactly one end in H are those of Sigma_0 and Sigma_1. The substitution h(x) -> -h(x) for x in H keeps the Haar measure and changes the sign of y_b exactly on Sigma_0 and Sigma_1. Let K^theta be the couplings 1 - 2 theta on Sigma_0, -1 on Sigma_1, 1 elsewhere. The substitution maps the model J^theta to the model K^(1 - theta). So <y_b>_(J^theta) = - <y_b>_(K^(1 - theta)) for b in Sigma_0. Hence

the integral over theta in [0, 1] of <y_b>_(J^theta) = (1/2) times the integral of ( <y_b>_(J^theta) + <y_b>_(J^(1 - theta)) ) = (1/2) times the integral of ( <y_b>_(J^theta) - <y_b>_(K^theta) ).

Step 4 (comparison). The models J^theta and K^theta have the same one-site conditional laws at every site outside D := the sites with x_nu in {j_1 - 1, j_1}. f = y_b for b in Sigma_0 depends on two sites, with x_nu in {b_nu - 1, 0}, and changes by at most 2 when one of them changes; so Delta(f) <= 4. The distance from these sites to D is at least min(j_1 - 1, b_nu - 1 - j_1) = floor(b_nu/2) - 1. By Lemma DC, abs(<y_b>_(J^theta) - <y_b>_(K^theta)) <= 4 alpha^(floor(b_nu/2) - 1)/(1 - alpha).
Step 5. abs(log(I_1/I_0)) <= 2 beta abs(Sigma_0) (1/2) 4 alpha^(floor(b_nu/2) - 1)/(1 - alpha), and abs(Sigma_0) = abs(B)/b_nu.
Step 6 (several flips, and U). For k with two or three flips, I(u, c^k v)/I(u, v) is a product of ratios of the same form with other backgrounds; the bound is uniform in the background, so the bounds add. Z[k] <= Z, so 0 <= 1 - Z[k]/Z <= abs(log(Z[k]/Z)), and by Identity L this is at most the supremum over (u, v) of abs(log(I(u, c^k v)/I(u, v))). For the cube b^3 this is at most (number of flips in k) times 4 beta b^2 alpha^(floor(b/2) - 1)/(1 - alpha). The numbers of flips of the seven k add to 12. So U <= (12/8) 4 beta b^2 alpha^(floor(b/2) - 1)/(1 - alpha). QED

**Example.** beta = 1/12, alpha = 1/2, b = 2a: U <= 8 a^2 2^(-a). For a = 25: 8 x 625/2^25 < 1.5 x 10^(-4) < 1/4950. So (MF) of `gap-mid-max.md` (U <= t/3, t = 1/1650) holds on the cube of side 50 at beta = 1/12, for every time extent.

**What this is, and what it is not.**
- It is the flux half of the seed in the range 1/18 <= beta < 1/6, where it was not proved. Theorem DOB gives both halves below 1/18.
- It does not give the seed above 1/18. The glue half (S_0) still needs the mixing of the four-dimensional measure, with 18 neighbours. I found no way to condition it away: with the links of one direction as one block and the rest as background, the block version of Dobrushin's condition gives 12 beta/(1 - 6 beta) < 1, which is beta < 1/18 again.
- Tests. The proof runs for U(1) and for Z_2 with other constants in Step 1. That is right (Proposition T2): both confine at small beta. For Z_2 the flat background at large beta gives I(1, c 1)/I(1, 1) of the order exp(-2 beta b^2), far from 1, as it must be (F9).
- The range 1/6 is what the crude influence bound gives. A sharper one-site bound moves it by a constant factor (GUIDE: the total variation distance of two von Mises-Fisher laws on S^3 whose parameters differ by 2 beta is about 0.42 beta for small beta, which would give about 0.39).

**The exact open statement of this approach.**

(AS-bg) at beta_1: there are C and m > 0 such that for every beta <= beta_1, every box B with sides at least 3, every background (u, v) and every nu: abs(log(I(u, c_nu v)/I(u, v))) <= C (abs(B)/b_nu) exp(-m b_nu).

- PROVED for beta_1 < 1/6 (Proposition TW).
- OPEN for 1/6 <= beta_1 < 2/3. For the flat background the layer model is the O(4) model in three dimensions, and 2/3 = N/(2d) is its mean-field temperature. Aizenman and Simon (1980) prove a gap there for ferromagnetic couplings (RECALLED from the digest `prior/gap-crux-lit-2.md`, C1; abstract only). Their inequalities need ferromagnetic couplings; a background is a frustration. So (AS-bg) up to 2/3 is a new statement, not a citation.
- FALSE for beta_1 above the critical coupling of the three-dimensional O(4) model (GUIDE: about 0.94), by the flat background: an ordered model pays a twist. So the uniform form of this approach ends below beta = 1, inside R1.
- Beyond that, only the mean over the true law of (u, v) can be small: (MF) itself, in the form of Identity L. At large beta the slices are close to a pure gauge at short distance and the layer model is ordered up to the correlation length. This is the same crux, seen in a three-dimensional spin model with a random background.

**Marks.** Identity L: PROVED. Proposition TW: PROVED GIVEN Lemma DC (checked, row 709). (AS-bg) between 1/6 and 2/3: OPEN. Nothing here is checked.

### 4.3 Attempt 3: the form (C), the seed on a physical torus

**Corollary C (PROVED from Corollary S3' of `gap-crux-restate.md`; one line).** Let (beta_j, N_j) be a sequence of couplings and integers N_j >= 3 with s := sup over j of S(N_j; (2 N_j)^3; beta_j) < 1/5041. Then for every j and every integer L >= 2 N_j: N_j m(L^3; beta_j) >= log(1/(5041 s)).
Proof. Corollary S3' at each j. QED

**Reading.** Let a_j be a lattice spacing and ell = 2 N_j a_j one fixed physical length. Then the gap of every cube of side at least ell, in physical units, is at least 2 log(1/(5041 s))/ell, uniformly in j. So the continuum gap along a trajectory beta_j = beta(a_j) follows from

(PHYS-SEED) limsup over j of S(N_j; (2 N_j)^3; beta_j) < 1/5041, with 2 N_j a_j = ell fixed,

together with the passage from uniform gaps of periodic cubes to the limit theory (row 700 does this at fixed beta; the uniform version is not written anywhere that I read). By P1, ell must be at least 14.8 physical correlation lengths. The step of Theorem S holds on physical sizes as it is: if (PHYS-SEED) holds at ell with bound s, it holds at 2 ell with bound 5041 s^2.

**What this changes.** For the target (GAP) of `gap-skeleton-final.md` Section 1, which is a continuum statement, the open range of the lattice at fixed beta (from 1/18 to about 2) is not on the path. On the path is one statement at one physical size. The T0 chain controls the torus where the running coupling is small; (PHYS-SEED) lives where it is of order one. Between the two is the flow of 1.4, items 5 and 6. So the crux for the Clay gap has no strong-coupling half: every improvement of the proved range in R1 (Theorem DOB, Proposition TW, a sharper one-link bound) moves a lattice theorem and does not move (GAP).

**Not attempted.** (PHYS-SEED) is the crux in its continuum form. I have no tool for it.

