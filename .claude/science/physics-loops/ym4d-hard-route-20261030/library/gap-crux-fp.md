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
- Part 4 (attempts): not started.

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
| 5 | Curvature: Bakry and Emery (Shen, Zhu and Zhu; (BE-block)) | The tensor is negative above beta = 1/3 at an explicit configuration; published range beta < 1/48 in four dimensions | small number; K7 |
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
| Z_2 at large beta | THM, RECALLED (F9) | the group is connected (flux half only) | about 0.44 for a tool blind to the difference of SU(2) and its centre |
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

