lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-12T11:09Z

# gap-means-max: which means could verify a seed or (G_ev) for SU(2) at the scale of the correlation length

Queue row 737 of `FINISH.md`. Pinned commit e6c83cc9a. Author document, research-stage working state. It grants no status and is not a public claim. One model wrote it; nothing here is checked by another model.

Labels used: **proved** (full argument written here or in the cited note), **argued** (argument written, a step is not closed), **reading** (what a source says, with its place), **belief** (no argument), **guide** (numeric or heuristic, cannot discharge a step), **open**.

Status of this file: complete for this run (2026-11-12 UTC). Section 4 (the proof attempt) was written first, so that it survives an error; Sections 1 to 3 were written after it.

**No mass gap is proved here.** No statement of this file was checked by a model that did not write it.

## 0. Repo search, rule 0a, sources read

**Read in full for this item.** `GOAL.md`. `FINISH.md` lines 1 to 84, 299 to 349, row 737. `library/gap-skeleton-final.md` Sections 0 to 5, 8 to 11, 13.14 to 13.17. `library/gap-flux-exercise.md` Steps 0 to 3, 8.1 to 8.5, 8.7, 9. `library/gap-flux-exercise-check.md` Sections 7, 8. `library/gap-form-exercise.md` 2.D, Step 3, Steps 6, 7, 9. `library/prior/gap-precedent-lit.md`. `library/gap-kappa-order.md`. `library/gap-crux-restate.md` Section 3.4 (Lemmas K, X, E, E', Theorem S, Corollaries S2, S3').

**Rule 0a (before the attack of Section 4).** The statement attacked is a form of (EV-STEP) (`gap-flux-exercise.md` 8.5). `library/open-core.md`: no line for "EV-STEP", "even step", "rigid", "light sector", "group of four". FINISH rows that name (EV-STEP): 731 (its source; it states the statement open, "no mechanism", and does not queue it) and 732 (the check; "(EV-STEP) stays open"). `gap-skeleton-final.md` 13.16 lists it as open and not queued. No row owns it or attacks it. Section 4 attacks it with a mechanism that those files do not hold (4.9 says what is new and what is theirs).

**Other branches.** A scratch fetch of main and of the pull requests 10114, 10133, 10141, 10144, 10149 was searched for flux-sector work; the result is in Section 6.

**The account.** `gap-flux-exercise-check.md` Section 8 (Codex gpt-6-astra) searched the index of the complete account of Sussman and Alpoge (with Claude and Codex) and found no centre-flux, dyonic or Pfaffian-sector theorem; CA-I 2702-2712 excludes a mass-gap assertion. I did not repeat that search. Nothing of the account is ported in this file. Its Wilson convolution and transfer construction is the base of `gap-transfer.md`, which every statement below reads through (TM-tw).

**Credit.** The twist and flux frame, and the argument that in a massive phase the light fluxes form a self-dual set: G. 't Hooft, Nucl. Phys. B 153 (1979) 141 (recalled, not re-read; no step below rests on it). The sector sums, the crossing identity (*), the sum rule (SR), Lemma CL1, Proposition CL and Theorem S-w: `gap-flux-exercise.md` (Claude Fable 5.2; checked by Codex gpt-6-astra, row 732). Lemmas A, K, X, E, E' and Theorem S: `gap-crux-restate.md` and `gap-seed-check-astra.md` (rows 697 to 699). The four means (M1) to (M4): `gap-form-exercise.md` (row 735).

## 1. The answer in short

1. **The flux half of the crux has a means, and it is (M4).** Reflection positivity in each sector, the self-duality of the crossed sector weights and a doubling of the time give a dichotomy: every flux sector is light or heavy, and the light ones form one of three groups (Theorem R, Section 4; proved here, not checked). The parameter of the dichotomy is the time extent. The hypothesis is on the centre-even sector alone.
2. **So the crux has one form with no flux sector: the even seed (ES)** at one physical size: the even thermal sum of the symmetric torus a^4 and the defect of additivity of the vacuum energy between the cubes of side a and 2a are both below 10^(-7). (ES) at some size is equivalent to a seed of Corollary EV at some size (Corollaries R4, R5).
3. **For the even half none of (M1) to (M4) is present today, and no fifth means that I can state is present.** For each the reason is marked in Section 2: a belief for (M1) and (M2); a theorem and a test model for (M3); for (M4) an open problem (Ginibre), a sign (argued: non-orientable surfaces of half-integer spin enter the character expansion with a minus sign in four dimensions) and three test models for the exclusion of order.
4. **The plan (Section 3)** has three routes. Route 1 is the reduction of item 2; its first statement is proved in Section 4. Route 2 is the only regime with a small number for this action, the thin torus with a twist, now with a finite criterion in the even language; it stops at the continuity in the fibre size. Route 3 is one explicit lattice surface; it would close the positive-representation form of (M4) by a counterexample that can be checked by hand.
5. **No number of SU(2) at a coupling of order one moved.** No mass gap is proved.

## 2. The means, one by one

"Needs" is the exact statement the means would need for Wilson SU(2). "Absent because" carries one of the marks **theorem**, **counterexample**, **belief**. "Test" is the smallest test that would show the means present or absent. The criterion to verify is (ES) at one physical size a, about 20 correlation lengths, uniformly in the cutoff (Section 4.6), or one of the three seeds; by Corollaries R4 and R5 these are the same target.

### 2.1 (M1) A small number at the scale of the correlation length

- **Needs.** (M1-S): there are R and a single-scale criterion (a convergent polymer bound, the weighted Dobrushin-Shlosman hypothesis (W) of `gap-ds-gauge.md`, or a Bakry-Emery bound) such that the effective measures of the account, blocked to the scale R xi, satisfy it for every cutoff. This is (P-c) of `gap-form-exercise.md` 3.6.
- **Absent because.** *Belief:* the continuum theory has no free dimensionless number, so at the scale xi every dimensionless quantity is a pure number, and none is known to be small before the conclusion (exp(-m a) at a = 20 xi is small, and it is the conclusion). *Theorem (the lane's):* the proved single-scale criteria hold for beta below about 1/18 (rows 701, 711), and the Hessian bound is 2 - 30 beta (`gap-skeleton-final.md` Section 6). *Rule:* a criterion on a block of side xi at a coupling of order one is a finite computation far beyond a hand check.
- **Test.** A guide run of (ES) itself (Corollary R7 needs four partition functions) at the couplings where xi is about one lattice spacing: at which size a does the pair (eps, delta) fall below 10^(-2)? If that size is above about 6, no hand criterion at the lattice scale can exist for this action. Not run here.

### 2.2 (M2) A second small number after an exact change of variables

- **Needs.** (M2-S): an exact identity that writes the even partition functions of Corollary R7 as a gas of objects with an activity z -> 0 along the trajectory, over a background that is integrable or uniformly convergent, with xi a power of 1/z.
- **Candidates and why absent.**
 - *Thin centre vortices and Z_2 monopoles (the Mack-Petkova splitting).* Activity exp(-c beta). *Belief:* they are dilute at the lattice scale and do not make the gap; the background (the SO(3) part) is as hard as the problem. In Z_2 itself the same dilute defects give the even gap at large beta, with the electric sectors light: the means works there because the background is trivial.
 - *1/N.* N = 2. *Belief:* no statement uniform in N down to 2 is in sight; the lane's control case (Kopper) needs N above exp(c beta).
 - *The twist on a thin torus (Tanizaki and Unsal; the lane's Route T).* Small number exp(-4 pi^2/g(s)^2) at a fibre of size s far below xi. Present only there (and node T2 is still open). To reach the four-dimensional theory it needs the continuity in s, (AC') of `gap-skeleton-final.md` 4.1. *Belief* that (AC') holds; nothing proved.
 - *Other calculable deformations* (a fundamental or an adjoint Higgs field, soft supersymmetry breaking): each needs a continuity statement of the same kind, and the adjoint Higgs model has a massless phase (recalled).
- **Test.** T2 in the even language: Remark R8 gives the finite criterion; the test is whether eps_tw and Delta_tw of the twisted slice can be bounded by 3 x 10^(-4) at beta >= beta_0(s) by the chart (CH) of row 679. If yes, (M2) is present on thin tori as a theorem. It does not test the continuity.

### 2.3 (M3) Exact closure, or one-sided closure on a restricted class

- **Needs.** (M3-S): a class K of weights that contains Wilson's, a block map R with R(K) inside K, and for every w in K: (eps, delta) of w at the size 2a are bounded by (eps, delta) of R(w) at the size a; and the iterates of the Wilson weight enter the strong-coupling range.
- **Absent because.** *Theorem (elementary):* in dimension above two the integral over one link is a function of the six staples at that link and is not a product of functions of plaquettes; so no class of plaquette weights is closed under exact block integration. *Counterexample for a class-wide one-sided form:* the Migdal-Kadanoff recursion drives every compact group to strong coupling in four dimensions (recalled; A9' of row 735), and U(1) has no gap at weak coupling (recalled theorem). So an inequality "the true (eps, delta) are bounded by the recursion's", proved from properties that U(1) shares, proves a false statement. (ES) needs both an upper bound on one partition function and a lower bound on another, and the bond-moving bound gives one side only (the failure of Tomboulis's argument that Ito and Seiler name; row 735, A9).
- **Test.** For any proposed one-sided inequality: state it for the Villain U(1) weight. If it holds there with the same proof, it cannot give (ES).

### 2.4 (M4) A correlation inequality with a parameter that gives a dichotomy

**For the flux half: present.** Theorem R. The inequality is Tr S^(2t) <= (Tr S^t)^2 in each crossed sector; the exact identity is the self-duality p = Hp; the dichotomy is "weight near 0 or near 1". *Proved in Section 4, not checked.*

**For the even half.**

- **Needs.** (M4-S): (i) a finite criterion: (ES) or a seed (have it). (ii) A one-parameter family of measures through the Wilson measure. (iii) An inequality which shows: if the criterion fails at every size at the parameter t_0, then an order parameter is bounded below for t beyond t_0. (iv) A proof that the order is absent on the range.
- **Absent because.**
 - *(iii) by Ginibre's method: an open problem.* Ginibre's proof needs sum and difference variables, which exist for Abelian groups. For the classical O(N) spin models with N at least 3 the second Griffiths inequality for the invariant products is a known open problem (recalled); the gauge case is not easier. No counterexample is known to me.
 - *(iii) by a positive surface representation: false term by term in four dimensions (argued).* See Proposition NS below. The Z_2 form of the same obstruction is Lemma NP of row 733.
 - *(iv): counterexamples in the class.* No soft theorem excludes order in four dimensions: Z_2 at large beta (light electric flux), U(1) at weak coupling (no gap), and the SU(2) theory with an adjoint Higgs field (a massless phase; recalled) have the symmetries, the positivity and the centre of the Wilson theory.
 - *Monotony in beta* points the wrong way (F4 of row 735).
- **Test.** T4a below.

**Proposition NS (a negative term; argued, the surface is not constructed).** Let S be a finite set of plaquettes such that every link lies in exactly two plaquettes of S or in none, and let S be connected through shared links. So S is a closed surface, up to points where sheets touch; let chi(S) be its Euler characteristic. Then, with x_p = (1/2) tr U_p,

integral over the links of the product over p in S of x_p = sgn(S) 2^(chi(S) - 2|S|), sgn(S) = -1 if chi(S) is odd, +1 if it is even.

So the term A(S) of Proposition SC of `gap-kappa-order.md` is beta^|S| sgn(S) 2^(chi(S) - 2|S|) (1 + O(beta^2)), and it is negative at small beta when chi(S) is odd, for example for a projective plane.

Argument. Three integrals for the character chi = 2x of the two-dimensional representation: (1) the integral of chi(AU) chi(U^(-1)B) dU is chi(AB)/2; (2) the integral of chi(A U B U^(-1)) dU is chi(A) chi(B)/2; (3) the integral of chi(A U B U) dU is -chi(A B^(-1))/2. (1) and (2) are Lemma T of row 733. (3): the substitution U -> U B^(-1) turns chi(A U B U) into chi(B^(-1) A U^2), and the integral of U^2 over SU(2) is -1/2 times the identity (the mean of chi(U^2) is -1: chi(U^2) = 4 x^2 - 2 and the mean of x^2 is 1/4; the integral of U^2 commutes with the group). Glue the plaquettes along a spanning tree of the dual graph with (1): the result is 2^(-(|S|-1)) chi(W), W the boundary word of a polygon in which every remaining link occurs twice. Reduce W by the standard steps of the classification of surfaces; a pair of the form (2) gives no sign, a pair of the form (3) gives one minus sign, and the number of pairs of the form (3) has the parity of the number of cross-caps, which is the parity of chi(S). The power of 2 is V - E by a count. (This is the lattice form of the two-dimensional Yang-Mills partition function on a non-orientable surface, recalled from Witten 1991; I did not write the induction.) QED (argued)

*Existence of S.* A closed embedded surface in a three-dimensional lattice is orientable, so the sign does not occur in three dimensions at this level. In four dimensions the projective plane embeds in R^4 and, by cubical approximation, in the 2-skeleton of the lattice (recalled; **not constructed here**). A finite search of the 2-skeleton of one hypercube and of a box of two hypercubes found no closed plaquette set with odd Euler characteristic (`/tmp/gmm-737/scripts/rp2.py`, `rp2b.py`; a guide to where not to look, nothing more).

*What it does and does not show.* If S exists, the character expansion of the four-dimensional Wilson SU(2) theory is not a sum of non-negative terms, and no proof of (KP), of Y_h >= 0, or of a switching lemma can go term by term. It does not show that a class weight Y_h is negative.

**A guide on the branching terms.** Row 733 left open the sign of the single-site three-plane integral J(a, b, c) for higher spins. A Monte Carlo guide (3 x 10^7 Haar triples; `/tmp/gmm-737/scripts/jabc.py`; reading written first; numeric lock held) finds all 56 values with spins from 1/2 to 3 positive, each by more than 150 standard errors (from 0.556 for (1/2,1/2,1/2), in agreement with 5/9 to 0.8 standard errors, down to 0.154 for (1/2,3,3)). So the first branching term gives no sign. The sign of Proposition NS comes from the topology of the sheet, not from branching. *guide.*

**Test T4a (the smallest test of the positive-representation form of (M4)).** Exhibit one closed plaquette surface with odd Euler characteristic in the four-dimensional lattice, as a list of plaquettes that a person can check (every link in two plaquettes, one cycle of plaquettes around every vertex, V - E + F odd). Then Proposition NS is a counterexample by hand. If a proof shows that no such lattice surface exists, the sign obstruction falls back to Lemma NP alone.

### 2.5 Fifth means

Each line: what it is; needs; absent because (mark); test.

- **(M5) The continuity method.** The set G of couplings (or of points on a path of actions) at which (ES) holds at some size is open, because the quantities of a fixed torus are continuous (Corollary R6 uses this). A closed G would give (ES) on the whole path from strong coupling. *Needs* an a priori bound, for example: on G, the least size a at which (ES) holds is bounded on compact sets of couplings; or |d log m_ev / d beta| <= C. *Absent: counterexample in the class and belief for SU(2).* In the two-dimensional Ising model G is open and not closed (the gap closes at K_c), so closedness is not a property of the class; for SU(2) it is the statement "no transition on the path", which is the target. The lane tried the derivative form three ways (rows 710, 712, 715: Theorem U is an exact formula, no bound). *Test:* none cheaper than the target. Corollary R6 is what the method gives without the bound: the flux phase is constant on each interval of G.
- **(M6) A zero-free region in a symmetry-breaking field (Lee and Yang).** For Ising, plane rotator and classical Heisenberg ferromagnets a field h gives a gap at every temperature (recalled: Frohlich and Rodriguez). For a gauge theory the field is a fundamental Higgs coupling in the unitary gauge. *Needs* the Lee-Yang property in h for four-body plaquette weights, and a gap that survives h -> 0. *Absent: counterexample at one end.* At beta = infinity the model is the four-dimensional O(4) spin model, which has long-range order at large h and none at small h (recalled theorems), so the zeros reach the real axis. And the mass given by the method vanishes with h. *Test:* none needed.
- **(M7) Convexity** (Brascamp and Lieb, Bakry and Emery, or a Hessian bound along a renormalization flow as in Bauerschmidt and Bodineau). *Needs* a lower bound on the Hessian of the effective potential at every scale up to xi. *Absent: belief;* this is (HESS) of `gap-skeleton-final.md` Section 5, with no bound between about 1/15 and about 40. *Test:* as recorded there.
- **(M8) A finite certificate of positivity** (loop equations with positivity; an operator inequality H^2 >= mH for a frustration-free form). *Absent by rule:* the known certificates are numerical. The Langevin generator is frustration-free, and a criterion of Knabe type for it is the all-boundary criterion at the scale xi, that is (M1).
- **(M9) Kinematics** (anomaly matching, monotone quantities of the flow, theorems of Mermin-Wagner type for the centre symmetry). *Absent: counterexample.* The adjoint Higgs model and U(1) have the same symmetries and a massless phase; a discrete one-form symmetry can break in four dimensions (Z_2 at large beta).
- **(M10) Duality rigidity** (a sum rule from self-duality, sub-multiplicativity, and weights in [0,1]). It is the means of Theorem R. *Present for the flux half.* For the even half I found no identity of this kind: the even sum enters p = Hp only as the normalization.

I do not claim that this list is complete.

## 3. The plan: three routes, ranked

**Route 1. The even seed by duality rigidity. Means: (M4) for the flux half; none yet for the even half.**

- *First statement:* Theorem R (Section 4.6). Proved here; one check by a model that did not write it is the next step. Points to test first: Lemma R1 (b) as an application of Lemma CL1 to w(k) = Z^k(a, a, c, d); the direction of every inequality in Proposition R3; dominance and Step 3; the arithmetic of Steps 4 and 5.
- *Then, in order:* (ES-1) of 4.9 (does a small even thermal sum bound the deficit for the lattice theory, by locality?); the two-dimensional form as a control with exact numbers.
- *Where it fails first:* at (ES) for SU(2) at one physical size. Route 1 changes the statement of the crux and verifies nothing at a coupling of order one. Inside the route, the first place to look for an error is Step 2 (the symmetry of the cube acts on all 64 sectors as claimed).
- *If Theorem R is checked:* the crux of `gap-skeleton-final.md` 13.16 can be stated as (ES); (EV-STEP) is closed in the form of Corollary R4; the three seeds, (KP) and the order of the seeds become consequences and leave the list of things to decide; a tool is judged only on vacuum energies and even thermal sums of periodic cubes (Corollary R7: four partition functions); the test "Z_2 at large beta" stops being special, because (ES) holds there. *If it is refuted:* the three seeds stay, and 13.16 stands as written.

**Route 2. The thin torus with a twist. Means: (M2) at a small fibre, then a continuity in the fibre size.**

- *First statement:* Remark R8 written line by line, then (ES_tw) for beta >= beta_0(s): eps_tw, Delta_tw <= 3 x 10^(-4) at one base size, from the chart (CH) (rows 679, 695). This is node T2 of `gap-skeleton-final.md` 4.1 with a finite criterion in the place of a decay statement.
- *Where it fails first:* at (AC'), the fibre sizes of the order of xi. In the language of Section 4: the light group of the twisted slice must stay the magnetic one for every s, and Proposition R3 shows that it can change only where eps_tw or Delta_tw is of order one. No tool bounds them there. Rows 669 and 678 already say that the approach dies here; this plan does not say otherwise.
- *If the first statement is proved:* the first gap theorem at weak coupling for this four-dimensional action with two infinite directions (S1 of the skeleton), in a form that Theorem S can iterate. *If refuted:* Route T loses its base and should be closed.

**Route 3. One explicit surface. Means: none; it is a test that can close the positive-representation form of (M4).**

- *First statement:* T4a of 2.4, a lattice projective plane as a checkable list. One short lane; a search may find the surface, the list is checked by hand.
- *Where it fails first:* if no such lattice surface exists (I expect that it does; recalled topology).
- *If proved:* "no positive surface representation in four dimensions" is a counterexample, not a belief; route D of row 735 is closed in its term-by-term form, and the only open form of (M4) for the even half is an inequality after the sum over surfaces, for which no mechanism is known. *If refuted:* Lemma NP is the only sign obstruction, and the branching guide of 2.4 (all positive) makes a positive representation in three dimensions a fair question.

**What the ranking is.** Route 1 is first because its first statement is proved and changes what every other route must verify. Route 2 is second because it is the one place where a small number exists for this action. Route 3 is third because it is cheap and decides one door. None of the three reaches (ES) at a coupling of order one. I know no route that does.

## 4. Route 1, first statement: an even seed at one size gives two of the three seeds (Theorem R)

All of Section 4 is **proved** by Claude Fable 5.2 (max) in this file, given the inputs of 4.1. It is not checked by another model. Sections 1 to 3 (the means and the plan) follow this section in the file's numbering and were written after it.

**In words.** The lane has three seeds, and each one counts seven flux sectors. Theorem R below needs no flux sector in its hypothesis. It reads two numbers of the centre-even sector of one symmetric torus: its thermal sum, and the defect of additivity of the vacuum energy. If both are small, the flux sectors have no choice: four of every sixteen crossed sectors weigh as much as the vacuum sector and twelve weigh nothing, the four form a self-dual group, and two of the three seeds hold. This is 't Hooft's dichotomy for a massive phase, as a finite inequality with constants.

### 4.1 Inputs

Each input is a statement of the lane that another model checked. I use them as written.

- **(TM-tw), (F1), (S3)**: `gap-flux-exercise.md` 3.0 and 3.1; checked by Codex gpt-6-astra (row 732, "The input (TM-tw), including Pf(k)=1: HOLDS"). For every box B with sides at least 3 and every magnetic twist m: T_{B,m} is a positive trace-class operator that commutes with the flips; Z^{e+m}(t, B) = Tr(T_{B,m}^t C^e) for t >= 3; a permutation of the axes maps the twist to its image and keeps Z^k; the sector sums are Z_{chi,m}(t; B) = Tr(T_{B,m}^t P_chi) = (1/8) sum_e (-1)^{chi.e} Z^{e+m} >= 0; every eigenvalue of T_{B,m} is at most lambda_0(B), the top eigenvalue of the periodic box, which is simple with an even eigenvector.
- **Lemma A (a)**: for S >= 0 trace class, (Tr S^k)^(1/k) is non-increasing in k (`gap-crux-restate.md` L37; rows 698, 699).
- **Lemma K (b)**: e(jb) <= j e(b), where e(b) = log lambda_0(b, c, d) and c, d are fixed (`gap-crux-restate.md` 3.4).
- **Lemma CL1 and Proposition X16**: `gap-flux-exercise.md` 8.3, 8.5; checked (row 732).
- **Lemma W, Theorem S-w, Corollary EV, Theorem EV-L**: `gap-flux-exercise.md` 8.2, 8.4; checked (row 732). Lemmas X and E' for W_w: by Theorem S-w.

### 4.2 Notation

Tori have sides (n_1, n_2, n_3, n_4), all at least 3. Frame 1: direction 1 is time. A sector of a box B is (chi; m) in Z_2^3 x Z_2^3, with indices 2, 3, 4. Z_{chi,m}(t; B) is its sector sum at time t. e(B) := log lambda_0(B). The even sector is 0 := (0; 0), and S_ev(t; B) = Z_0(t; B)/lambda_0(B)^t - 1 >= 0.

X := Z_2^4. A point x = (x_1, x_2, x_3, x_4) of X stands for the sector chi = (0, x_1, x_2), m = (0, x_3, x_4). So x_1, x_2 are the parities under the flips of the directions 3, 4, and x_3, x_4 are the twists m_3 = k_24, m_4 = k_23. On X: B(x, y) := x_1 y_4 + x_2 y_3 + x_3 y_2 + x_4 y_1 (mod 2), and for a function f on X, (Hf)(x) := (1/4) sum over y of (-1)^{B(x,y)} f(y). B is bilinear, symmetric, B(x, x) = 0, and B(u, .) = 0 only for u = 0. So H H = 1. A subgroup L of X is *isotropic* if B = 0 on L x L.

The three sector sets of Proposition CL (b), written by one element alpha of Z_2^2 each: Sigma_w = {(chi; m): (chi_nu, m_nu) is (0,0) or alpha_w, for nu = 2, 3, 4}, with alpha_per = (1,0), alpha_full = (0,1), alpha_kappa = (1,1).

### 4.3 Lemma R1 (the crossed slices)

Let a, b, c, d >= 3.

(a) Z_0(a; (b, c, d)) = (1/4) sum over z in X of Z_z(b; (a, c, d)).

(b) On a torus with n_1 = n_2 = a: for each (chi_2, m_2) in Z_2^2 the function G(x) := Z_{(chi_2, x_1, x_2), (m_2, x_3, x_4)}(a; (a, c, d)) on X satisfies G = HG. So G(x) <= G(0) for every x, and the sum of G over X is 4 G(0).

Proof. (a) is (*) of Proposition X16. (b) Put w(k) := Z^k(a, a, c, d) for k in K. The exchange tau of the axes 1 and 2 maps the torus (a, a, c, d) to itself, so w o tau = w by (TM-tw). In the notation of 8.3, what(chi; m) = sum_e w(e; m) (-1)^{chi.e} = 8 Z_{chi,m}(a; (a, c, d)) by (F1). Lemma CL1 gives G = HG for every slice. G >= 0, so G(x) = (1/4) sum_y (-1)^{B(x,y)} G(y) <= (1/4) sum_y G(y) = G(0). QED

### 4.4 Lemma R2 (finite algebra: weights that are almost 0 or 1)

Let p be a function on X with p >= 0, Hp = p, p(0) = 1. Put Q := sum over x of p(x)(1 - p(x)).

(a) p <= 1 and the sum of p over X is 4. So Q >= 0.

(b) If Q <= 4 theta with theta < 1/20, then L := {x: p(x) > 1/2} is an isotropic subgroup of X with exactly four elements, and

eta := sum over x in L of (1 - p(x)) + sum over x not in L of p(x) <= 2Q <= 8 theta.

Proof. (a) As in Lemma R1 (b). (b) For x in L: 1 - p(x) <= 2 p(x)(1 - p(x)). For x not in L: p(x) <= 2 p(x)(1 - p(x)). So eta <= 2Q <= 8 theta < 2/5.
*Count.* 4 = sum p = |L| - sum_{L} (1 - p) + sum_{not L} p, so | |L| - 4 | <= eta < 1, and |L| = 4.
*Isotropic.* Let x be in L, and let n be the number of y in L with B(x, y) = 1. Then 4 p(x) = sum_y (-1)^{B(x,y)} p(y) <= (4 - n) - (n - sum_{L}(1 - p)) + sum_{not L} p = 4 - 2n + eta. Also p(x) >= 1 - eta. So 2n <= 5 eta < 2, and n = 0.
*Subgroup.* 0 is in L. Let x, x' be in L. Then B(x + x', y) = 0 for y in L, so 4 p(x + x') >= sum_{L} p - sum_{not L} p >= 4 - eta > 2. So x + x' is in L. QED

### 4.5 Proposition R3 (rigidity for one pair of axes)

Let a, c, d >= 3, A := (a, c, d), and

eps := S_ev(a; A), Delta := a (2 e(a, c, d) - e(2a, c, d)), theta := 1 - exp(-Delta) (1 + eps)^(-2), p(x) := Z_x(a; A)/Z_0(a; A) for x in X.

Then: (a) Delta >= 0, p >= 0, Hp = p, p(0) = 1, and sum over x of p(x)(1 - p(x)) <= 4 theta. (b) If theta < 1/20, the conclusion of Lemma R2 (b) holds for p.

So the sixteen sectors of the box A at the time a split into four that carry the weight of the even sector, up to eta, and twelve that carry at most eta in total.

Proof. Delta >= 0 by Lemma K (b) with j = 2. Hp = p by Lemma R1 (b) for the slice (chi_2, m_2) = (0, 0) of the torus (a, a, c, d).
*The lower bound.* Lemma R1 (a) on the torus (a, 2a, c, d): Z_0(a; (2a, c, d)) = (1/4) sum_z Z_z(2a; A). The left side is at least lambda_0(2a, c, d)^a, because S_ev >= 0.
*The upper bound.* For each z = (chi; m), the operator S := T_{A,m} P_chi is positive and trace class, and Z_z(t; A) = Tr S^t. By Lemma A (a), Z_z(2a; A) <= Z_z(a; A)^2.
*Together.* 4 lambda_0(2a, c, d)^a <= sum_z Z_z(a; A)^2 = Z_0(a; A)^2 sum_z p(z)^2, and Z_0(a; A) = lambda_0(A)^a (1 + eps). So sum p^2 >= 4 exp(-Delta)(1 + eps)^(-2) = 4 (1 - theta). With sum p = 4 this is sum p(1 - p) <= 4 theta. QED

**Where the information comes from.** The lane used the same two facts in Proposition EVL to bound the even sum of the doubled box from above, and lost a factor Theta. Here they are used the other way: the even sum of the doubled box is at least 1 for free, and this bounds sum p^2 from below. The weights lie in [0, 1] and sum to 4, so sum p^2 = 4 forces them to be 0 or 1.

### 4.6 Theorem R

**Definition (ES), the even seed at the size a.** Let a >= 3 and

eps := S_ev(a; (a, a, a)), delta := a (8 e(a, a, a) - e(2a, 2a, 2a)).

(ES) at a is: eps <= 10^(-7) and delta <= 10^(-7).

eps is the thermal sum of the centre-even sector of the cube of side a at the time a (the symmetric torus a^4). delta/a is E_0((2a)^3) - 8 E_0(a^3), with E_0 = -e the ground energy of the periodic cube: the defect of additivity of the vacuum energy. Both read the even sector only: lambda_0(B) is the limit of Z_0(t; B)^(1/t).

**Theorem R.** delta >= 0. If (ES) holds at a, then there is exactly one alpha in {(1,0), (0,1), (1,1)} such that:

(a) for each of the two w in {per, full, kappa} with alpha_w != alpha: S_w(a; (a, a, a)) <= 1.27 x 10^(-5), and

S_w(a; (2a, 2a, 2a)) <= 1.02 x 10^(-4) < 1/5041;

(b) for the w with alpha_w = alpha: S_w(a; (a, a, a)) > 2.

So an even seed gives two of the three seeds of Corollary EV at the size N = a, and it says which one fails.

Proof. *Step 0 (the three deficits).* Put Delta_1 := a (2 e(a, a, a) - e(2a, a, a)), Delta_2 := a (2 e(2a, a, a) - e(2a, 2a, a)), Delta_3 := a (2 e(2a, 2a, a) - e(2a, 2a, 2a)). Each is >= 0 by Lemma K (b), applied to one side of the box with the other two fixed (e(B) does not depend on the order of the sides, by (TM-tw)). 4 Delta_1 + 2 Delta_2 + Delta_3 = delta. So delta >= 0 and Delta_1 <= delta/4.

*Step 1 (rigidity on a^4).* Proposition R3 with c = d = a. theta = 1 - exp(-Delta_1)(1 + eps)^(-2) <= Delta_1 + 2 eps <= 2.25 x 10^(-7) < 1/20, because exp(-u) >= 1 - u and (1 + eps)^(-2) >= 1 - 2 eps. So L := {x in X: p(x) > 1/2} is an isotropic subgroup with four elements and eta <= 8 theta <= 1.8 x 10^(-6).

*Step 2 (symmetry and dominance).* For each of the 64 sectors sigma = (chi; m) of the cube put rho(sigma) := Z_sigma(a; (a, a, a))/Z_0(a; (a, a, a)). So rho = p on X. A permutation pi of {2, 3, 4} acts on sectors by permuting the indices of chi and of m alike, and rho(pi sigma) = rho(sigma): by (TM-tw) Z^{pi k} = Z^k on the torus a^4, and pi permutes the indices of e and of m alike (8.3), so (F1) gives the claim. For nu in {2, 3, 4} let sigma|nu be the sector that keeps (chi_nu, m_nu) and has the other four entries 0. **Dominance: rho(sigma) <= rho(sigma|nu).** For nu = 2 this is Lemma R1 (b) for the slice (chi_2, m_2) of sigma. For nu = 3, 4 apply the permutation that exchanges 2 and nu.

*Step 3 (the group L is one of three).* For (c, n) in Z_2^2 let t(c, n) be the sector chi = (0, 0, c), m = (0, 0, n), that is the point (0, c, 0, n) of X. Put A_0 := {(c, n): (0, c, 0, n) in L}. A_0 is a subgroup of Z_2^2, because L is a subgroup. Let x be in L and sigma its sector. sigma|3 has chi = (0, x_1, 0), m = (0, x_3, 0); the exchange of 3 and 4 maps it to t(x_1, x_3). By dominance and symmetry, p((0, x_1, 0, x_3)) = rho(sigma|3) >= rho(sigma) > 1/2, so (x_1, x_3) is in A_0. In the same way sigma|4 = t(x_2, x_4) gives (x_2, x_4) in A_0. So L lies in {x: (x_1, x_3) in A_0 and (x_2, x_4) in A_0}, a set with |A_0|^2 elements. Hence |A_0| >= 2. If |A_0| = 4, then L contains the four points (0, c, 0, n), so L is that set; the exchange of 3 and 4 maps L to itself (Step 2) and maps that set to {(c, 0, n, 0)}, a different set. So |A_0| = 2: A_0 = {(0,0), alpha} for one alpha != (0,0), and L = {x: (x_1, x_3) in A_0 and (x_2, x_4) in A_0}.

*Step 4 (two sector sets are small on a^4).* Let alpha_w != alpha and sigma in Sigma_w, sigma != 0. Some nu has (chi_nu, m_nu) = alpha_w. By dominance and symmetry rho(sigma) <= rho(sigma|nu) = p(x*), with x* := (0, alpha_w1, 0, alpha_w2). x* is not in L, because alpha_w is not in A_0. So rho(sigma) <= eta. Now 1 + S_w(a; (a,a,a)) = (1 + eps) sum over sigma in Sigma_w of rho(sigma), so

S_w(a; (a, a, a)) <= eps + 7 eta (1 + eps) <= 10^(-7) + 7 (1.8 x 10^(-6))(1 + 10^(-7)) < 1.27 x 10^(-5).

*Step 5 (three doublings of the box at the fixed time a).* Let B be a box and B' the box with one side doubled, from a to 2a, the other two sides fixed. W_w is invariant under permutations of the sides, and W_w(t, B) = Tr (T^w_B)^t with top eigenvalue lambda_0(B) (Lemma W). Cross the doubled side with the time: W_w(a, B') = Tr (T^w_{B_a})^(2a) <= (Tr (T^w_{B_a})^a)^2 = W_w(a, B)^2, where B_a is the box with the sides a (the old time) and the two fixed sides; Lemma A (a). So

1 + S_w(a; B') <= (1 + S_w(a; B))^2 exp(a (2 e(B) - e(B'))).

Apply this along (a, a, a), (2a, a, a), (2a, 2a, a), (2a, 2a, 2a):

1 + S_w(a; (2a)^3) <= (1 + S_w(a; a^3))^8 exp(4 Delta_1 + 2 Delta_2 + Delta_3) = (1 + S_w(a; a^3))^8 exp(delta).

With Step 4: S_w(a; (2a)^3) <= exp(8 x 1.27 x 10^(-5) + 10^(-7)) - 1 = exp(1.017 x 10^(-4)) - 1 < 1.02 x 10^(-4), and 1/5041 > 1.98 x 10^(-4).

*Step 6 (the third set).* For alpha_w = alpha the three points of L other than 0 are sectors of Sigma_w. So S_w(a; a^3) >= (1 + eps)(3 - eta) > 2. alpha is unique because A_0 is defined by the weights. QED

### 4.7 Corollaries

**Corollary R4 ((ES) at one size gives (G_ev) at all sizes, and the gap of the periodic limit on the centre-blind functions).** Let (ES) hold at a. Then for every integer L >= 2a, with k >= 0 such that D := 2^(k+1) a <= L < 2D:

S_ev(D/2; L^3) <= q^(2^k)/71 with q <= 5041 x 1.02 x 10^(-4) < 0.515, and m_ev(L^3) >= log(1/q)/a > 0.66/a.

Every limit point of the periodic symmetric tori clusters exponentially at the rate 0.66/a on the functions with (i) of 8.2, in the four directions.

Proof. Theorem R (a) is the hypothesis of Corollary EV with N = a. QED

This is (EV-STEP) of `gap-flux-exercise.md` 8.5 with the hypothesis (ES) in place of "S_ev(N; (2N)^3) <= t_0". The hypothesis is on the even sector alone, at one size.

**Corollary R5 (the converse: a seed gives (ES) at a larger size).** Let S_w(N; (2N)^3) < 1/5041 for one w and one N >= 3, q := 5041 S_w(N; (2N)^3). Then (ES) holds at a = 2^(k+1) N for every k with q^(2^k) <= 4.5 x 10^(-6).

Proof. Put s_k := S_w(a/2; a^3) <= q^(2^k)/5041 (Theorem S-w). *eps.* The even sector is in Sigma_w and thermal sums do not increase with the time: eps <= S_w(a; a^3) <= s_k. *delta.* Lemma X for W_w: (b - a') kappa(b) <= g(a', b) for a' < b, with kappa >= 0 the deficit in the side b. For a doubling of one side from a to 2a: a (2 e(B) - e(B')) = a (2 kappa(a) - kappa(2a)) <= 2a kappa(a) <= 4 g_w(a/2; B). So Delta_1 <= 4 log(1 + s_k). By Lemma E' with (a', b, h) = (a/2, a, 2a) the exponent is 4: g_w(a/2; (2a, a, a)) <= 4 log(1 + s_k) and g_w(a/2; (2a, 2a, a)) <= 16 log(1 + s_k). So Delta_2 <= 16 log(1 + s_k), Delta_3 <= 64 log(1 + s_k), and delta <= (16 + 32 + 64) log(1 + s_k) <= 112 s_k. Both are at most 10^(-7) if 112 q^(2^k)/5041 <= 10^(-7). QED

**So the crux has an equivalent form with no flux sector in it:**

(there are w and N with S_w(N; (2N)^3) < 1/5041) if and only if (there is a with (ES) at a).

**Corollary R7 (a sufficient free-energy form of (ES)).** Write Z_ev(t; B) := Z_0(t; B) = (1/8) sum over e in E_1 of Z^e(t, B). Then

eps <= Z_ev(a; a^3)^2 / Z_ev(2a; a^3) - 1, and delta <= 8 log Z_ev(a; a^3) + log Z_ev(a; (2a)^3) - log Z_ev(2a; (2a)^3).

So (ES) holds at a if both right sides are at most 10^(-7). They read four even partition functions, on the tori a^4, (2a, a, a, a), (a, 2a, 2a, 2a) and (2a)^4.

Proof. For a box B let S := T_B P_0 >= 0, with top eigenvalue lambda_0(B). Tr S^(2t) <= lambda_0^t Tr S^t and lambda_0^t <= Tr S^t. So lambda_0(a^3)^a >= Z_ev(2a; a^3)/Z_ev(a; a^3), which gives the first bound. Also a e(a^3) <= log Z_ev(a; a^3) and a e((2a)^3) >= log Z_ev(2a; (2a)^3) - log Z_ev(a; (2a)^3), which give the second. QED

**Remark R8 (the same for a twisted fibre; argued, not written line by line).** Fix c, d and the slice (chi_2, m_2) = (0, 1): the sixteen sectors with the twist k_34 = 1 in the plane of the sides c, d. Let lambda_tw(b) be the top eigenvalue of T_{(b,c,d),(1,0,0)}. (i) The crossing of Lemma R1 holds for this slice for all a, b: the computation of Proposition X16 does not move chi_2 and m_2. (ii) Every eigenvalue of T_{(b,c,d),(1,m_3,m_4)} is at most lambda_tw(b): the twists k_24, k_23 are electric in the frame of the direction 2, so Z^{(34)+m_3(24)+m_4(23)} <= Z^{(34)} as in the proof of (S2). (iii) For an isotropic group Lambda of four points of X, W_Lambda(a, b) := the sum over x in Lambda of the sector sums of the slice is symmetric in (a, b) and is a trace of powers; so Lemma K and Corollary S2 hold for it. Then Proposition R3 holds for the slice with eps_tw and Delta_tw in place of eps and Delta, and with eps_tw, Delta_tw <= 3 x 10^(-4) the doubling of Step 5 gives S_Lambda(a; 2a) <= 0.045 < 1/20 for every isotropic Lambda that meets the light group in 0 only. This is a finite criterion for the gap of the twisted thin torus in its two long directions, at a fixed fibre. It is the form in which Route 2 of Section 3 would use Section 4.

**Corollary R6 (the flux phase cannot change while an even seed exists; argued, the continuity step is not written with constants).** At a fixed coupling, alpha is the same at every size a at which (ES) holds. (If (ES) holds at a_1 with alpha_1 and at a_2 >= 2 a_1 with alpha_2 != alpha_1, then the w with alpha_w = alpha_2 has a seed at a_1 by Theorem R (a), so S_w is small on the cube of side a_2 by Corollary S3' and the monotony in the time; this contradicts Theorem R (b) at a_2. Two sizes closer than a factor 2 are compared through a third, larger size, which Corollary R5 supplies.) All the quantities of a fixed torus are continuous in beta, and at a size where (ES) holds with room the sixteen weights stay in [0, eta] or [1 - eta, 1], so the group L cannot change under a small change of beta. So on an interval of couplings on which (ES) holds at some size for every coupling, alpha is constant. At small beta the periodic seed is proved (`gap-seed-sc.md`, row 701: beta below 1/12800; row 711: below 1/18, as `gap-skeleton-final.md` 13.10 and 13.12 report; I did not re-read those proofs). By Theorem R (b) alpha is then not alpha_per. Consequence: **if an even seed exists at every coupling of an interval (0, beta_1], then the periodic seed holds on all of it.** In words: with a gap of the centre-blind sector at every coupling, heavy electric flux at strong coupling stays heavy. Confinement cannot be lost without the even seed failing first. (Whether alpha is alpha_full or alpha_kappa at small beta decides the kappa seed in the same way. I expect alpha_full, because all twists are free at strong coupling; that is recalled, and I did not find it written in the lane.)

### 4.8 Tests of Theorem R against known cases

- **Z_2 gauge theory at large beta** (Proposition Z2 of `gap-form-exercise.md`: the full and the kappa seed hold at N = 3 for beta >= 91). Theorem R allows this: alpha = alpha_per, the electric sectors are the four light ones. Pass.
- **A scale-invariant model.** Theorem R must not apply. In the two-dimensional critical Ising model (recalled conformal data, as in 8.6 of row 731; the two-dimensional form of R3 has four sectors, sum p = 2) the weights at a = b are about (1, 0.456, 0.456, 0.086): not 0 or 1. The hypothesis fails there through Delta: a (2 kappa(a) - kappa(2a)) = pi c/4 = 0.39 with c = 1/2, so theta is about 0.33. The even sum alone is small there (about exp(-2 pi) = 0.002). So **the deficit hypothesis cannot be dropped from Proposition R3**, and eps <= 10^(-7) alone is not shown to suffice (open; see 4.9). *recalled data; a guide.*
- **U(1) at weak coupling.** No gap. (ES) fails: the photon gives eps of order exp(-2 pi) and delta of order one (recalled; Casimir energy -c/L). Pass.
- **A guide run in two dimensions** is in 4.10.

### 4.9 What is new, what is not shown, what is open

**New against the lane's record.** Proposition EVL has the two facts (the crossing identity (*) and Lemma A in each sector) and reads them as a loss Theta in [1/4, 4]. Its text says "(EV-STEP) follows from: an even seed at N forces one of the three seeds at a comparable size ... In a massive phase 't Hooft's argument says that they are (recalled; not proved)". Section 4 proves that statement, with the deficit as the second hypothesis. The three steps that the record does not hold: the weights are at most the even weight at a = b (Lemma R1 (b)); the doubled even sum is used as a lower bound (R3); dominance and the symmetry of the cube select one of three groups (Steps 2, 3). The idea that a massive phase has a self-dual set of light fluxes is 't Hooft's.

**Not shown.**
1. (ES) for SU(2) at any size at any coupling above the strong-coupling range. At small beta it holds by Corollary R5 and the proved periodic seed.
2. That eps small implies delta small. In the class of the lemmas I know no proof and no counterexample. A hypothetical table with eps = 0 and all fifteen flux weights 1/5 satisfies p = Hp and the bounds used here, and has exp(-Delta) <= 0.4. It is not shown to come from a model: two equal fluxes should fuse to an even state of twice the energy, and that uses locality, which the class does not hold.
3. Anything for the functions that see the centre.
4. The constants 10^(-7) are not optimized.

**Open (named).** (ES-1) Is there, for Wilson SU(2), a bound delta <= C eps or delta <= C S_ev at a comparable shape? It would make the even seed one number. A route: the deficit kappa(a) is the growth rate of the even thermal sum on long boxes, kappa(a) = lim over b of (1/b) log(1 + S_ev(a; (b, c, d))) (from Lemma R1 (a): only the sectors of the crossed box with top eigenvalue lambda_0 survive as b grows); what is missing is the step from the box of length a to long boxes without the factor 4.

### 4.10 A guide run in two dimensions (a run can refute or guide; it proves nothing)

**What was run.** The two-dimensional Ising model, where the same algebra has four sectors z = (chi, m) (parity under the global flip; antiperiodic closing), B_2(z, z') = chi m' + chi' m, H_2 = (1/2)(-1)^{B_2}, sum p = 2 and the bound of R3 reads Q <= 2 theta. Exact transfer matrices by parity blocks, chains of length a and 2a for a = 3, 4, 5, 6, couplings K = 0.2, 0.3, 0.38, K_c, 0.5, 0.6, 0.8. Script `/tmp/gmm-737/scripts/rigid2d.py`, output `/tmp/gmm-737/out/rigid2d.out` on the Mini; not in git. Numeric lock held as `gap-means-max-737` and released; memory free 53 percent at the start; BLAS threads 1; the script stops above 2 GB.

**Criteria, written in the script header before the run.** C1: rho(a; a) = H_2 rho(a; a). C2: Z_00(a; 2a) = (1/2) sum_z Z_z(2a; a). C3: p <= 1, Delta >= 0 and Q <= 2 theta. C4: 1 + S_w(a; 2a) <= (1 + S_w(a; a))^2 exp(Delta) for the three sets. FAIL at any point would mean that the algebra of Section 4 is wrong in two dimensions.

**Result: PASS at all 28 points.** C1 and C2 hold to 10^(-13). Selected rows (p for the sectors (1,0), (0,1), (1,1)):

| K | a | eps | Delta | theta | Q | 2 theta - Q | p | S_per, S_full, S_kappa at (a; 2a) |
|---|---|---|---|---|---|---|---|---|
| 0.2 | 6 | 2.3 x 10^(-7) | 1.81 x 10^(-3) | 1.81 x 10^(-3) | 3.62 x 10^(-3) | 4 x 10^(-6) | 0.0009, 0.9982, 0.0009 | 0.0018, 1.00, 0.0018 |
| 0.3 | 6 | 7.1 x 10^(-5) | 0.040 | 0.040 | 0.078 | 0.0015 | 0.024, 0.960, 0.017 | 0.042, 1.00, 0.041 |
| K_c | 6 | 2.2 x 10^(-3) | 0.401 | 0.334 | 0.580 | 0.087 | 0.453, 0.453, 0.093 | 0.80, 0.80, 0.50 |
| 0.6 | 6 | 1.1 x 10^(-4) | 0.053 | 0.052 | 0.102 | 0.0026 | 0.947, 0.032, 0.021 | 1.00, 0.056, 0.055 |
| 0.8 | 6 | 3.2 x 10^(-7) | 2.15 x 10^(-3) | 2.15 x 10^(-3) | 4.30 x 10^(-3) | 6 x 10^(-6) | 0.9978, 0.0011, 0.0010 | 1.00, 0.0022, 0.0022 |

**Readings (guides).**

1. The inequality Q <= 2 theta is close to an equality away from the critical point. So R3 loses little.
2. In the disordered phase the light sector is the magnetic one and the periodic and kappa seeds are small; in the ordered phase the light sector is the electric one and the full and kappa seeds are small. This is Theorem R in two dimensions.
3. At K_c the weights tend to about (0.45, 0.45, 0.09) and Delta to about 0.40 (pi/8 = 0.393): the recalled conformal values of 4.8. The even sum eps is small there, and the hypothesis fails through Delta alone.
4. **In every row eps is far below Delta, and Delta is about Q/2.** So the deficit is not a side condition. It is the number that carries the flux information: the vacuum energy of the periodic box feels every light object that can wind the box, and by crossing these are the sectors of the crossed box. (ES) has no flux sector in its *form*. In substance its second number weighs the heavy sectors. The gain of Theorem R is one object (vacuum energies and the even thermal sum of periodic cubes) in the place of three sums over flux sectors, and an equivalence in the place of three one-way statements. It is not a weaker statement, and by Corollary R5 it cannot be.

## 5. What not to do, with reasons

1. **No lane on a flux statement as a step toward the crux**: (KP), the order of the seeds, twist ratios, vortex containers, the choice between the three seeds. By Corollaries R4 and R5 they follow from (ES) or are equivalent to it, and by 4.10 the flux information is already in the vacuum-energy defect. (Wait for the check of Theorem R before acting on this.)
2. **Do not drop the deficit from (ES).** In the two-dimensional critical model the even sum at a = b is about 0.002 and the deficit is 0.39. "S_ev small at one shape" is not shown to be a seed. (ES-1) is open.
3. **Do not read Theorem R as progress on the even half.** It moves no number of SU(2). At a coupling of order one (ES) is as far as a seed, exactly (Corollary R5).
4. **No proof of a positivity statement for SU(2) term by term in the character expansion in four dimensions**, before test T4a. Proposition NS (argued) says the terms have both signs there.
5. **No author run on the continuity method** (in beta, in the fibre size, or along a path of actions) without a named a priori bound. Openness is free and closedness is the target (2.5, (M5)). The same for (AC').
6. **No route through a Higgs field, a Lee-Yang property, an anomaly or a monotone quantity of the flow.** Each has a test model in which its hypotheses hold and the gap fails (2.5, (M6), (M9)).
7. **No class-wide step and no monotony in beta** (F4, F5 of row 735; not re-derived here). Theorem R is not such a step: it changes the criterion at one size.
8. **No one-sided closure of Migdal-Kadanoff type** unless the inequality fails for U(1) by its statement (2.3).
9. **Do not take a pass on Z_2, on the two-dimensional model or on a guide run as support for a tool.** In this file they test the algebra of Section 4 only.
10. **Do not quote 10^(-7) as a physical threshold.** The constants are not optimized; Theorem SH of row 707 (other shapes) may relax them. I did not try.
11. **No computer certificate** for (ES) at a finite size: the owner's rule. A run may only say at which size a hand proof would have to work (test of 2.1).

## 6. Report

**Kind of result.** A direction document (row 737), with one proof of a step that the lane's record and the account of Sussman and Alpoge do not hold (Section 4), three guide runs, and a plan.

**Proved here (Claude Fable 5.2 max; not checked by another model), given the checked inputs of 4.1.**

- Lemma R1, Lemma R2, Proposition R3: on a torus with two equal sides, the sixteen crossed sector weights, divided by the even weight, lie in [0, 1], sum to 4, and satisfy sum p(1 - p) <= 4 theta with theta = 1 - exp(-Delta)(1 + eps)^(-2). For theta < 1/20 four are within 8 theta of 1, twelve within 8 theta of 0, and the four form an isotropic group.
- Theorem R: (ES) at a (eps, delta <= 10^(-7) on the cubes of side a and 2a) gives S_w(a; (2a)^3) <= 1.02 x 10^(-4) < 1/5041 for two of the three w, and S_w(a; a^3) > 2 for the third.
- Corollary R4: (ES) at one size gives (G_ev) at all sizes and exponential clustering of every periodic limit on the centre-blind functions, at the rate 0.66/a. This is (EV-STEP) with (ES) as hypothesis.
- Corollary R5: a seed of any of the three kinds gives (ES) at a larger size. So the two forms of the crux are equivalent.
- Corollary R7: a sufficient form of (ES) in four even partition functions.

**Argued (a step is not written).** Corollary R6 (the flux phase is constant on an interval of couplings with an even seed; so the periodic seed, proved at small beta, holds as long as an even seed exists). Remark R8 (the same rigidity and a two-dimensional seed for the twisted fibre). Proposition NS (a closed plaquette surface with odd Euler characteristic gives a negative term of the character expansion; the lattice surface is recalled, not constructed).

**Guides.** Two-dimensional Ising model, 28 points: the identities and inequalities of Section 4 pass; the bound of R3 is nearly sharp; the deficit, not the even sum, is the binding number. Group integrals J(a, b, c) for spins up to 3: all positive. A finite search of two small boxes found no lattice surface with odd Euler characteristic.

**Means (Section 2).** (M4) is present for the flux half, as duality rigidity. For the even half: (M1) absent (belief, and the size of the criterion); (M2) present only on a thin twisted torus, absent at the scale xi (belief); (M3) absent (a theorem for exact closure, the U(1) test for one-sided closure); (M4) absent (an open problem, a sign that is argued, test models for the exclusion of order); six further means stated, none present.

**Other branches (rule "repo first").** A scratch fetch of main and of the pull requests 10114, 10133, 10141, 10144, 10149 (depth 1; `/tmp/gmm-737/git`). In the YM4D folders of main, 10141, 10144 and 10149: no file matches twisted partition functions, flux sectors, 't Hooft duality, or a centre-even sector. In 10114: about 20 files match; the lines sampled are about U(1) line-bundle flux on a torus and about clock and shift backgrounds of the soft-kernel route. I read the sampled lines only, not the files. None states a relation between crossed sector weights. PR 10133 was fetched and not searched (its tree is close to 10114 by file count). A second search over every text file of 10114 was stopped by its time limit and is not part of this result.

**Not done.** No literature was fetched: every statement about papers is marked recalled. The check of Section 4. The explicit surface of T4a. The guide run of 2.1. (ES-1). The line-by-line form of R6, R8 and NS.

**For the lead.** (1) Queue one check of Section 4 (Lemma R1 to Corollary R5, R7) by a model that did not write it; the points to test first are in Section 3, Route 1. (2) If it holds: state the crux in `gap-skeleton-final.md` as (ES), with the three seeds as its consequences, and mark (EV-STEP) closed in the form of Corollary R4. I did not edit that file, `t0-tree.md` or the registry. (3) One short lane for T4a. (4) Route 2 only if the lead wants theorem S1 of the skeleton; it does not move the crux.

RESULT: Proved here, not yet checked by another model: an even seed (ES) at one size a (even thermal sum of the torus a^4 and vacuum-energy defect a(8e(a^3) - e((2a)^3)), both <= 10^(-7)) forces two of the three seeds of Corollary EV at N = a and says which one fails (Theorem R, by duality rigidity: sum p(1-p) <= 4 theta for the sixteen crossed sector weights); so (EV-STEP) holds with hypothesis (ES), and "a seed at some size" is equivalent to "(ES) at some size" (Corollaries R4, R5). Means: (M4) is present for the flux half; for the even half none of (M1) to (M4) and none of six further means is present (marks in Section 2; Proposition NS, a negative term from non-orientable surfaces in four dimensions, is argued and needs one explicit lattice surface). Plan: Route 1 the even seed (first statement proved), Route 2 the twisted thin torus with the finite criterion of Remark R8 (stops at the continuity in the fibre size), Route 3 the surface test T4a. Open: (ES) for SU(2) at any coupling of order one, uniformly in the cutoff; whether a small even thermal sum bounds the deficit (ES-1); the check of Section 4. No mass gap is proved.
