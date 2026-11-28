# Row 1342: is the seed (N-phys) the right seed for the Jaffe-Witten gap

Row 1342 of `FINISH.md`. Author run of Claude Fable 5.2 (max effort), laptop subagent, one session, started
2026-11-21 02:22Z. Research-stage working state. **No mass gap is claimed or proved here.** Nothing in this file is
checked by another model. The file was written in steps; each step was appended when it was finished.

Marks. PROVED = proved by hand in this file from the named inputs, not checked. PROVED GIVEN = follows from named
statements on file; their recorded checks are named at the place. ARGUED = a reasoned statement, not a proof.
GUIDE = physics belief or numerics, used in no proof. OPEN = not proved.

## 0. Answer in brief

1. **The statement that rows 1323 to 1339 attack is not (N-phys).** It is the periodic two-period bound of Theorem
   ZD-c, that is (W). On file, (W) is equivalent over the allowed sizes to (N-phys) together with the branch
   selection (the seven electric flux sectors of the periodic cube are heavy). The gap clause does not use the
   branch selection. Both facts are on file and checked (rows 1161 and 1162, rows 1179 and 1183). So the periodic
   bound asks for the gap and for confinement on tori. It is not the right target for the gap clause. (Section 3.)
2. **The weakest statement at one scale with a checked consumer is the neutral one.** It is (N-phys). Over the
   allowed sizes it is equivalent to the uniform kappa seed. Every other one-scale statement on file implies it at
   some admissible size. (Theorem O, Section 3; PROVED GIVEN checked rows; nothing new.)
3. **What the gap clause consumes is weaker, and it is not a statement at one scale.** It is (G_ev-phys): at each
   late cutoff, neutral cube gaps of at least M_* in physical units along some sequence of sides, and a neutral
   thermal sum that tends to zero along that sequence. No bound on the seed size in physical units is used.
   (Proposition C, Section 2.)
4. **New here, PROVED by hand, unchecked: the model ST_q.** It is local, hypercubic and reflection positive. Every
   periodic box of every shape has a simple vacuum and the exact gap log q. No cube of any size has a seed. The
   limit of its symmetric tori has no gap. So in the class of Theorem S a uniform gap on the cubes gives neither a
   seed nor the gap of the limit, at one fixed coupling. This answers, for that class, the question left open in
   rows 700, 720, 1259, 1291 and 1300. It stays open for models with a strictly positive kernel, such as Wilson.
   Consequence: a target that keeps only the gap of the cubes is wrong. The thermal clause of the seed does
   necessary work. (Section 4.)
5. **(N-phys) is sufficient and not necessary.** In the class its excess over (G_ev-phys) is one clause: the seed
   size is bounded in physical units (Proposition LS, rows 1234 and 1250). For Wilson: if the neutral cube gaps are
   uniform and (N-phys) fails at every size, then the Casimir free energy D^+ of the symmetric torus grows at least
   linearly in the physical size (Corollary F, Section 5). The account bounds D^+ at each size, given its own
   statements. Whether D^+ is sublinear for Wilson is OPEN. So necessity for Wilson is not proved, and a failure
   for Wilson is not shown.

**Decision (ARGUED from the statements of Sections 2 to 5).** Keep a thermal statement at one scale as the target
of the infrared chain. State it in the neutral form, (N-phys) or the kappa seed. Drop the periodic form: it adds
confinement on tori, which the gap clause does not use. Do not replace the seed by a uniform gap of the cubes: ST_q
shows that this is too weak. The seed is then "right in kind, wrong in sector" as the chain now words it.
(Section 6.)

## 1. Sources, credits, statements

### 1.1 What was read

Read for this row, statements and proofs at the places named: `FINISH.md` rows 1161, 1162, 1179, 1180, 1183, 1184,
1187, 1234, 1250, 1259, 1291, 1300 and 1323 to 1341 (RESULT lines); `GOAL.md`; `library/gap-phys-seed.md` (whole);
`library/gap-solve9-astra62.md` L1-200 and the statements at L215, L327-339, L379-409; `library/gap-solve9-check-opus.md`
(the list S1 to S45); `library/gap-mini-branch-fable.md` Sections 5 and 6; `library/gap-neutral-chain-check-astra.md`
(verdict lines); `library/gap-flux-exercise.md` 3.0 to 3.1 and the statements of 8.2 to 8.4;
`library/gap-seed-limit.md` Sections 1, 4.1, 4.3, 4.4, 6; `library/gap-os-equiv.md` Statements (3), (5), (7);
`library/gap-crux-restate.md` Section 1 and the setting of 3.4 with Lemmas K and X; `library/gap-mini-neutral-fable.md`
2.1; `library/gap-mini-solve-v-opus.md` Proposition LS; `library/gap-seed-sc.md` (statements of Theorems 1 to 3);
`parts/gap.md` (state of attack); the RESULT lines of rows 884, 1003, 1135, 1233, 1251 and 1302 to 1311. I did not
check the cited rows line by line again. Where I rely on one, I name its recorded check.

Repo search before Section 4 (the repo-first rule): `grep` of `library/*.md`, `parts/*.md` and `FINISH.md` for
"stratif", "row-constant", "column-constant", "one coordinate", "uniform gap and no seed", "linear growth of D". No
model of the kind of Section 4 was found. The places that leave the question open are quoted in 4.5.

### 1.2 Credits

Tadeusz Balaban: the block renormalization method that the account builds on. Ethan Sussman and Levent Alpoge, with
Claude and Codex as authors of their text: the account, the trajectory and the continuum datum that this lane ports.
G. 't Hooft: twists, electric and magnetic flux, the duality behind the two alternatives. K. Osterwalder and
E. Seiler, M. Luscher: the transfer operator and reflection positivity (through rows 667 and 671). Earlier rows of
this lane, which carry almost all of Sections 2, 3 and 5: Claude Fable 5.2 (rows 700, 720, 731, 1179, 1180, 1184:
Theorem L3, Theorem ZD-c, Corollary Z2, Theorem EV-L, the three sector sets, Theorem BP, the seed-size form);
gpt-6.2-astra (rows 1135, 1161: the line-spin model, the one-cube neutral theorem, the two alternatives; checks
1183, 1187, 1250); Claude Opus 5.5 (rows 1234, 1259, 1291, 1300: Proposition LS, Lemma CD, the three attacks on
(NS-gap); checks 703, 1162); gpt-6-astra (checks 699, 732). The model of Section 4 and the reading of Sections 5
and 6 are this row's.

### 1.3 Notation and the statements compared

Trajectory (a_j, beta_j), spacing a_j -> 0. A physical side L is admissible when n_j = L/a_j is an integer on the
lane's grid for all late j. For a periodic box B: T_B is the Wilson transfer operator (positive, trace class, simple
top eigenvalue lambda_0(B)); S(a; B) = Tr T_B^a / lambda_0(B)^a - 1 is the periodic thermal sum over all eight
electric sectors. Twisted objects as in `gap-flux-exercise.md` 3.0 and `gap-solve9-astra62.md` L48: X_{m,q}(v) is the
trace of the v-th power of the magnetic transfer F_m in the electric character q, in units of lambda_0(B)^v;
s(v) = X_{0,0}(v) - 1 = S_ev(v; B) is the neutral excited trace; S_kappa(v) = s(v) + sum over m != 0 of X_{m,m}(v);
m_ev(B) is the gap of the neutral sector. Z^e is the partition function with the temporal twist e.

- **(PS), the periodic seed.** There is an admissible L with limsup_j S_j(n_j/2; n_j^3) < 1/1650. This is the
  two-stage seed of Theorem ZD-c (`gap-phys-seed.md` L311; row 720). In two-period form, as rows 1323 to 1339 use
  it: limsup_j Z(n_j, T_j)^2 / Z(n_j, 2T_j) < 1651/1650 with T_j = n_j/2. It is equivalent to (W) and to
  (PHYS-SEED).
- **(KS), the kappa seed.** There are ell > 0 and s_* < 1/5041 with S_{kappa,j}(N_j; (2N_j)^3) <= s_* for all late
  j, where N_j a_j = ell.
- **(N-phys)** (row 1161 L215; row 1179 Section 6; row 1180 2.1). There is an admissible L such that for all late
  j: 4 | n_j, n_j >= 2^70, and there is an integer u_j with 3 <= u_j <= n_j/512 and s_j(u_j; n_j^3) <= 1/2.
- **(a).** Every late coupling beta_j has a seed: an integer N_j >= 3 and a class w_j in (per, full, kappa) with
  S_{w_j}(N_j; (2N_j)^3) < 1/5041. No bound on N_j a_j.
- **(b).** In (a), the seeds can be chosen with one margin s_* < 1/5041 and with limsup_j N_j a_j finite.
- **(G-phys).** There is M_* > 0 and, for each late j, an integer L_j^0 with m_{ev,j}(L^3) >= M_* a_j for every
  integer side L >= L_j^0.
- **(G_ev-phys).** There is M_* > 0 such that for every late j there are integer sides L_i -> infinity and integers
  n_i <= L_i/2 with S_{ev,j}(n_i; L_i^3) -> 0, L_i - n_i -> infinity, and m_{ev,j}(L_i^3) >= M_* a_j for all i.
- **(BS), the branch selection.** At the cube of (N-phys), alternative I of row 1161 (9) holds for all late j: the
  seven electric sectors of the periodic cube are heavy, and every twist ratio tends to one.
- **The gap clause.** For the continuum time-reflection datum D_inf of the T0 chain, with (P1) to (P4), a class C
  of centre-blind observables, (H2) and (TOT): a unique vacuum and spec(H) in (0) union [M, infinity) for one
  M > 0 (`gap-os-equiv.md` Statement (5); `gap-mini-branch-fable.md` 5.3). The datum, (H2) and (TOT) are OPEN
  inputs of the T0 chain. They are not the subject of this row.

## 2. Step 1: what the gap clause consumes

How the question was attacked. The seed can be wrong in three ways. (i) It can contain sectors that the gap clause
does not read (the flux sectors). (ii) It can contain a count of states that the gap clause does not need. (iii)
It can be the wrong kind of statement, so that a weaker one (for example the gap of the cubes alone) would do. I
first fixed the exact statement that the checked consumer uses (this section). I then ordered the one-scale
statements on file (Section 3). Rows 731, 1161 and 1179 had already settled (i). For (ii) and (iii) the record had
one comparison model (line-spin) and one open question (does a uniform gap force a seed at one coupling). I looked
for a model that decides that question, and found one (Section 4). Section 5 then states what is proved in the
class and what is open for Wilson.

**Proposition C (the lattice input of the gap clause; PROVED GIVEN Theorem EV-L (d) of row 731 (cross-provider check
row 732), Theorem L3-ev and Proposition P'-ev of row 1179 (cross-provider check row 1183); a reading with the rate
named, no new step).** Assume (G_ev-phys). For each late j let nu_j be a limit state, restricted to the centre-blind
class A, of the periodic symmetric tori L_i^4 at the cutoff j, along a subsequence of the sides of (G_ev-phys). Then:

- (i) abs(nu_j(FH) - nu_j(F) nu_j(H)) <= norm(F) norm(H) exp(- M_* x) for F, H in A separated in a coordinate
  direction by the physical distance x = d a_j, d >= 1;
- (ii) the transfer operator of the datum D_(nu_j) satisfies norm(T^t psi) <= exp(- M_* t a_j) norm(psi) on the
  complement of the vacuum line in H_A(nu_j);
- (iii) every continuum datum D_inf with (P1) to (P3), a class C with maps into V_A, (H2) for the states nu_j and
  (TOT) has a unique vacuum and, with (P4), spec(H) in (0) union [M_*, infinity).

Proof. At the cutoff j, (G_ev-phys) is the hypothesis (G_ev) of Theorem L3-ev (`gap-mini-branch-fable.md` 5.0, 5.1)
with m_0 = M_* a_j. Its parts (d-ev) and (e-ev) are (i) and (ii). (iii) is the proof of Proposition P'-ev: (H1) of
Statement (5) of row 668 holds with m_j = M_* and S_j the complement of the vacuum. QED

Remarks.

1. The hypothesis has no twist, no flux sector and no branch. It has no bound on a seed size in physical units.
   The thermal clause is used at each cutoff separately, with no uniformity in j. The only uniform number is M_*.
2. Where the thermal clause is used: Theorem EV-L (c), (d) compare the periodic symmetric torus with the cylinder
   (`gap-flux-exercise.md` L135-145). The gap of the cylinder state on A needs the neutral gap only (C1 of the same
   file). Statement (7c), (7d) of row 668 says the same: on cylinders only the rate must be uniform, and a statement
   on the cubic tori passes to the cylinder together with a bound on the thermal sum. Section 4 shows that for limits
   of symmetric tori the clause cannot be dropped.
3. The chain of sufficient statements (each arrow PROVED GIVEN the row named):
   (N-phys) gives (a) and (b), with the class kappa, N_j = n_j/2 and S_kappa < 2^(-18) (row 1161 L215, check 1162
   S12; Theorem BP (i) of row 1179). (a) and (b) give (G-phys) with M_* = log(1/(5041 s_*))/ell_*, where
   N_j a_j <= ell_* (Theorem S-w and Corollary EV of row 731; Proposition P-ev (a) of row 1179). (a) and (G-phys)
   give (G_ev-phys): from the seed of (a) at the cutoff j, Corollary EV gives along every sequence L_i -> infinity
   integers n_i <= L_i/2 with S_ev(n_i; L_i^3) -> 0 and L_i - n_i -> infinity; (G-phys) gives the rate.
4. So "(a) and (G-phys)" is a sufficient statement that is strictly weaker than (N-phys) in the class. By row 1180
   2.1 (check 1187), (N-phys) is "(a) and (b)" on the grid. The line-spin model has (a) and (G-phys) and not (b)
   (Proposition LS). The excess of (N-phys) over what is consumed is the clause (b): one seed size in physical units.
5. Not claimed: that (G_ev-phys) is necessary for the gap clause. Statement (5) of row 668 needs the rate only on
   the sector of the class, and only as a lower limit along the sequence.

## 3. Step 2: the one-scale statements on file, and their order

**Lemma TP (two periods; PROVED, elementary; the neutral case is row 1161 (12)).** Let R >= 0 be trace class with all
eigenvalues in [0, 1] and with 1 an eigenvalue. Put x(T) = Tr R^T - 1 >= 0 and rho(T) = (1 + x(T))^2/(1 + x(2T)).
Then 1 + x(T) <= rho(T) <= (1 + x(T))^2.
Proof. 0 <= x(2T) <= x(T), because r^(2T) <= r^T for 0 <= r <= 1. QED

Uses. Periodic: R = T_B/lambda_0, rho(T) = Z(n, T)^2/Z(n, 2T), so S(T; B) <= rho(T) - 1. A ratio below 1651/1650
gives S < 1/1650 (row 1334 (1)). Neutral: with Z_+(v) := (1/8) sum over the eight temporal twists e of Z^e(v; n^3)
= lambda_0^v (1 + s(v)) (formula (F1) of row 731), the number A_+ := Z_+(2u)/Z_+(u)^2 is 1/rho(u). So A_+ >= 2/3
gives s(u) <= 1/2, and s(u) <= 1/2 gives A_+ >= 4/9. Kappa: the normalized eigenvalues of the kappa transfer are
at most 1 (row 1161 (3)), so S_kappa(N) <= W_kappa(N)^2/W_kappa(2N) - 1.

**Theorem O (order of the one-scale statements; PROVED GIVEN the checked statements cited; nothing new).**

- (i) (PS) gives (N-phys) at a larger admissible size (row 1161 L150; check 1162 S11).
- (ii) (N-phys) gives (KS) at the same cube, with s_* = 2^(-18) and ell = L/2 (row 1161 L215; check 1162 S12;
  check 1183, link 1).
- (iii) (KS) gives (N-phys) at a larger admissible size (row 1161 L150 and L389-400, check 1162 S19; row 1180 2.1,
  check 1187: finitely many doublings, three for the margin 2^(-18), and one 512-fold enlargement).
- (iv) A uniform full seed gives (KS) at the same cube, because S_kappa <= S_full (row 731, C7).
- (v) (PS) holds if and only if (N-phys) and (BS) hold, over the allowed sizes (row 1161 L148, L150 and (13),
  (14); check 1162 S10, S11, S13, S14). Under (N-phys) with alternative II the periodic trace at the time n/2 is
  near 8, so (PS) fails at that cube while the gap on A holds (Theorem BP of row 1179).
- (vi) Each of (PS), (KS), (N-phys) gives (G_ev-phys) (Remark 3 of Section 2).

So (N-phys), which over the sizes is the uniform kappa seed, is implied by every one-scale statement on file that
has a checked consumer: the three seeds, the neutral two-size criteria of row 1161 (26) (S18, S19) and the
one-period test of row 1161 (11), (12) (S16). It is the weakest of them. Whether the neutral trace at aspect two
on one cube suffices alone is the open statement (EV-STEP) of row 731; this row did not attack it.

**Correction of the premise of this row.** The brief says that the chain asks for (N-phys), "equivalently" the
two-period bound of Theorem ZD-c. On file these are two statements. The ZD-c bound is (PS). By Theorem O (v) it is
(N-phys) and (BS) together. Rows 1323 to 1339 work on (PS): each of them reduces to a ratio of periodic partition
functions below 1651/1650 or to an equivalent overlap. What (BS) adds is the phase of the centre symmetry on tori
(row 1179 Section 6, items 2 and 3). It is on the path of (W) and not on the path of the gap clause (check 1183:
"Wilson branch selection enters only (W)").

**A statement on local observables only (ARGUED).** No one-scale statement about finitely many local
gauge-invariant observables has a consumer on file, and I do not expect one. The reason is completeness: a light
state that couples weakly to every observable of the list changes no listed number by more than a small amount.
Row 1161 L404-413 (check S43) proves this for Markov kernels on one slice with the Wilson vacuum: two kernels with
the same correlations of any finite family of neutral slice observables at all time separations, one with zero
neutral excited trace and one with a neutral eigenvalue near one. That statement is about kernels on the slice, not
about the Wilson transfer operator, so for Wilson it is a warning and not a theorem. A trace is the one-scale
object on file that reads all states. The price is that it also counts them.

**Sizes (GUIDE; ideal-gas estimate of check 1183, its Step on N2, with the mass ratios of row 1063).** The seeds at
aspect two, (PS) and (KS), need a box of about 23 correlation lengths. (N-phys) at K = 512 needs about 11000. So
(N-phys) has an order-one margin, no flux sector and a positive measure, and it pays with the size of the box. The
kappa seed keeps the small box and the small margin and has a signed sum over the 64 twists.

## 4. Step 3: the stratified model ST_q. A uniform gap on every box, no seed, no gap of the limit

This section is new. Everything in 4.1 to 4.4 is PROVED by hand here and is not checked by another model. The proofs
use only counting. A small exact enumeration (4.6) agrees; it is a GUIDE and no proof step.

### 4.1 The model

Fix an integer q >= 2 and a dimension d >= 2. The lattice is a torus with sides n = (n_1, ..., n_d), all n_mu >= 2.
A spin sigma(x) in {1, ..., q} sits on each site. A bond is *satisfied* when its two spins are equal. A plaquette with
corners x, x + e_mu, x + e_nu, x + e_mu + e_nu (mu != nu) is *paired* when its two mu-bonds are satisfied or its
two nu-bonds are satisfied. The weight of a configuration is 1 if every plaquette is paired and 0 if not. Z_ST(n) is
the number of configurations of weight 1.

The weight is a product over the plaquettes of one function of four spins. It is invariant under translations, under
the hypercubic group and under the permutations of the q values. So the model is local and hypercubic. It is a model
with hard constraints: the weight takes the value 0.

### 4.2 The admissible configurations

**Lemma ST1 (PROVED).** Every plaquette is paired if and only if sigma depends on at most one coordinate: there are
a direction mu and a function xi with sigma(x) = xi(x_mu) for all x.

Proof. If sigma(x) = xi(x_mu), every bond in a direction other than mu is satisfied. A plaquette in a plane (mu, nu)
has its two nu-bonds satisfied. A plaquette in a plane (nu, nu') has all four bonds satisfied. So every plaquette is
paired.

Conversely let every plaquette be paired.

Step 1. Let the mu-bond at x (from x to x + e_mu) be unsatisfied, and let nu != mu. The plaquette at x in the plane
(mu, nu) contains this bond, so its two mu-bonds are not both satisfied. It is paired, so its two nu-bonds are
satisfied: sigma(x + e_nu) = sigma(x) and sigma(x + e_mu + e_nu) = sigma(x + e_mu). So the mu-bond at x + e_nu is
unsatisfied and carries the same two values. The plaquette at x - e_nu gives the same for x - e_nu.

Step 2. Repeat Step 1 from the new sites. Every site of the hyperplane H = (y: y_mu = x_mu) is reached from x by
steps of the form +e_nu or -e_nu with nu != mu. So sigma is a constant c on H and a constant c' != c on the next
hyperplane H' = (y: y_mu = x_mu + 1).

Step 3. Let also a nu-bond at some site y be unsatisfied, with nu != mu. By Step 2 for the direction nu, sigma is a
constant u on (z: z_nu = y_nu) and a constant u' != u on (z: z_nu = y_nu + 1). Each of these two hyperplanes meets H
(take a point with mu-coordinate x_mu). On H the spin is c. So u = c = u'. This is a contradiction.

So if a mu-bond is unsatisfied, all bonds in the other directions are satisfied, and then sigma depends on x_mu only.
If no bond is unsatisfied, sigma is constant. QED

**Corollary ST2 (PROVED).** Z_ST(n) = q^(n_1) + ... + q^(n_d) - (d - 1) q.
Proof. There are q^(n_mu) configurations that depend on x_mu only. Two of these sets, for two directions, meet
exactly in the q constant configurations. QED

So Z_ST is positive and invariant under the permutations of the sides.

### 4.3 The transfer operator

Take d = 4, the direction 1 as time with a = n_1 >= 2 steps, and the box B = (n_2, n_3, n_4). Let A_B be the set of
slice configurations tau on B all of whose spatial plaquettes are paired. By Lemma ST1 in three dimensions, tau is in
A_B if and only if it depends on at most one spatial coordinate, and A_B has q^(n_2) + q^(n_3) + q^(n_4) - 2q
elements. Define the matrix T_B on the functions on A_B by T_B(tau, tau') = 1 if every time-like plaquette between
tau and tau' is paired, and 0 if not.

**Lemma ST3 (PROVED).** (i) Z_ST(a, B) = Tr T_B^a. (ii) T_B(tau, tau') = 1 if and only if tau = tau' or both are
constant. (iii) T_B is the identity on the M_B := q^(n_2) + q^(n_3) + q^(n_4) - 3q non-constant slices of A_B, plus
the q x q matrix J_q of ones on the q constant slices. Its eigenvalues are q (multiplicity one, eigenvector the
uniform function on the constant slices), 1 (multiplicity M_B) and 0 (multiplicity q - 1). T_B is real, symmetric
and positive semi-definite.

Proof. (i) A configuration on the torus is a sequence of slices tau_1, ..., tau_a. Its plaquettes are the spatial
plaquettes of each slice and the time-like plaquettes between consecutive slices (cyclically). So its weight is the
product over t of [tau_t in A_B] T_B(tau_t, tau_(t+1)).
(ii) The time-like plaquette over the spatial bond (y, y + e_i) is paired when tau(y) = tau(y + e_i) and
tau'(y) = tau'(y + e_i), or when tau(y) = tau'(y) and tau(y + e_i) = tau'(y + e_i). If tau = tau' the second case
holds on every bond. If tau(y) != tau'(y) for one y, the second case fails on every bond at y, so the first case
holds there: tau and tau' take at each neighbour of y the values they take at y, and they differ there too. B is
connected, so tau and tau' are constant, with different constants. Two constant slices satisfy the first case on
every bond.
(iii) follows from (ii). J_q has the eigenvalues q, once, and 0. QED

Check against Corollary ST2: Tr T_B^a = q^a + M_B = q^a + q^(n_2) + q^(n_3) + q^(n_4) - 3q.

### 4.4 The theorem

**Theorem ST (PROVED by hand here; not checked).** For every q >= 2 the four-dimensional model ST_q has these
properties.

- (a) *It is in the class of Theorem S.* Z_ST is positive and symmetric in the sides. For each direction and each
  box, Z_ST(a, B) = Tr T_B^a with T_B positive semi-definite, of finite rank, with a simple top eigenvalue. So the
  setting of the lemmas of Theorem S holds (`gap-crux-restate.md` L174, with W(a, b) = Z_ST(a, b, c, d)), and so do
  Lemma A and (LB). The model is local and hypercubic. It is reflection positive at site mirrors and at mirrors
  that bisect links, in each direction (the transfer matrix is positive semi-definite).
- (b) *Uniform gap.* For every box B with sides at least 2: lambda_0(B) = q, the second eigenvalue is 1, and
  m(B) = log q. The gap is the same for every size and every shape.
- (c) *No seed.* S(a; B) = M_B q^(-a). For a cube: S(a; b^3) = 3 (q^b - q) q^(-a). If b > a >= 3 this is at least
  3q - 3q^(1-a) >= 5. So S(N; (2N)^3) >= 5 for every N >= 3, and no shape with a space side longer than the time
  passes any threshold of Theorem SH (they are at most 3/10).
- (d) *Casimir free energy.* f = inf F/abs(n) = 0, and D(a) = F(a^4) = log(4 q^a - 3q), so
  a log q <= D(a) <= a log q + log 4. In the two-variable setting the deficit of Lemma K is kappa(b) = log q for
  every b. So b m(b^3) = b log q is unbounded, and D is unbounded: of the two halves of Theorem ZD, (Z-UNB) holds
  and (BDD-Delta) fails, at one fixed coupling.
- (e) *The limit of the symmetric tori has no gap.* The state of the torus n^4 is the uniform law on the admissible
  configurations. As n grows it converges on every local function to nu_sym = (1/4)(nu_1 + nu_2 + nu_3 + nu_4),
  where under nu_mu the field is sigma(x) = xi(x_mu) with independent uniform values xi(k). Let
  F = 1[sigma(0) = 1] - 1/q and let tau_t be the translation by t in the time direction 1. Then nu_sym(F) = 0 and

      nu_sym(F tau_t F) = (3/4) (1/q) (1 - 1/q)   for every t >= 1.

  So nu_sym does not cluster in the time direction at any rate, and the conclusion (d) of Theorem L3 fails for it.
  In the words of row 668: nu_sym is reflection positive in time (nu_1 has independent slices, the other three
  laws do not depend on the time, and a mixture of reflection positive laws is reflection positive), so it has a
  time-reflection datum; that datum violates (X_m) for the class (F) and every m > 0; by Statement (3c)(ii) it
  has no gap. The limit of the cylinders b^3 x Z is nu_1 alone: the vacuum of T_B is the uniform function on the constant
  slices, and consecutive slices are independent. That state has decay at every rate in the time direction and none
  in the space directions.
- (f) *Products.* For a model X of the class, the product X x ST_q has, on every box, the gap
  min(m_X(B), log q), and 1 + S = (1 + S_X)(1 + S_ST) for every one of the three sector sets of X. So it has no
  seed of any class at any size. With X the Wilson SU(2) model at beta below 1/12800 (it has a seed, and so gaps
  on all large cubes; `gap-seed-sc.md` Theorem 3, row 701, check row 704) this is a lattice gauge model with
  decoupled matter that has uniform cube gaps and no seed.

Proof. (a) Corollary ST2 and Lemma ST3. Lemma A holds for every positive trace-class operator. Reflection
positivity, on a torus with time extent 2k. Site mirror t -> -t, F a function of the slices at the times 0 to k:
the sum of conj(F(theta sigma)) F(sigma) over the admissible configurations is the sum over the pairs
(tau_0, tau_k) of abs(Phi_F(tau_0, tau_k))^2, where Phi_F is the sum over the slices at the times 1 to k - 1 of F
times the product of the matrix elements of T_B; the other half of the torus gives the complex conjugate because
T_B is real and symmetric. Link mirror t -> 1 - t, F a function of the slices at the times 1 to k: the two halves
are joined by the two bonds (0, 1) and (k, k + 1), and the sum is <Psi_F, (T_B x T_B) Psi_F> >= 0, with Psi_F a
function of (tau_1, tau_k), because T_B is positive semi-definite. The other directions follow from the hypercubic
symmetry. (b), (c) Lemma ST3
(iii); M_B >= 3q^2 - 3q > 0. For the cube, M_B = 3(q^b - q), and 3(q^b - q) q^(-a) >= 3(q^(a+1) - q) q^(-a).
(d) Z_ST >= q > 1, so F > 0, and F(n^4)/n^4 tends to 0. In the two-variable setting lambda(b) = q, so e(b) = log q,
ell = 0 and kappa(b) = log q.
(e) On n^4 there are q^n - q non-constant admissible configurations for each direction and q constant ones, out of
4 q^n - 3q. So each direction has probability tending to 1/4, and the constants have probability tending to 0.
Given the direction mu, the values xi(1), ..., xi(n) are uniform on the non-constant sequences; on a finite set of
indices this tends to the independent uniform law. Under nu_1 the spins sigma(0) and tau_t sigma(0) are xi(0) and
xi(t), independent, so nu_1(F tau_t F) = 0. Under nu_i with i = 2, 3, 4 they are equal, so
nu_i(F tau_t F) = (1/q)(1 - 1/q). For the cylinder, T_B^k/q^k tends to the projection on the top eigenvector.
(f) The partition functions multiply, also with twists on the factor X; the top eigenvalues multiply. QED

### 4.5 What ST_q settles, and what it does not

**The question on file.** Row 700 (`gap-seed-limit.md` L232-234): "A uniform gap alone does not give the seed by any
argument in this file ... I have no example of a lattice gauge theory with a uniform gap on cubes and no seed at any
size", with the open statement (NS-gap). Row 720 (`gap-phys-seed.md` L309): "I do not know a model of the class with
a uniform gap and linear growth of D. OPEN". Row 1259: "'uniform gap implies a seed' stays OPEN with no
counterexample in the Wilson class". Row 1291: OPEN, "'uniform cube gap implies a seed' in the class". Row 1300
(`gap-mini-solve-ax-opus.md` L88-90): "a counterexample inside the class of local reflection-positive models with a
simple gapped vacuum would show that the count is a separate obligation for every route."

**What is settled (PROVED GIVEN Theorem ST).**

1. In the class of Theorem S, "a uniform gap on the cubes implies a seed" is false, at one fixed coupling. ST_q is
   local, hypercubic and reflection positive, its vacuum is simple, its gap is exact and the same on every box, and
   it has no seed. So the count is a separate obligation for every route that uses only those properties.
2. Corollary Z2 of row 720 is sharp in order. It says that a uniform gap m_0 without a seed forces
   D(a) >= (m_0/64) a - 0.12. ST_q has D(a) = m_0 a + O(1). Only the constant 64 is open.
3. The thermal clause in Theorem L3 and in Theorem EV-L (d) cannot be replaced by the gap of the cubes in any proof
   that uses only properties that ST_q shares. ST_q has (G3) of row 700 on every cube and not (G1), and its limit
   of symmetric tori has no gap.
4. The model is a new case for the paragraph "The tests in this form" of `gap-phys-seed.md` 3.1 ("in every
   comparison model the failing half is (Z-UNB), and (BDD-Delta) holds"): here (Z-UNB) holds and (BDD-Delta) fails.

**The mechanism, in words.** The excited levels of T_B are not particles. They are whole slices ordered along one
space direction: n_i layers, each with q free values, all at the one energy log q. Their number q^(n_i) beats the
weight q^(-a) as soon as the side is longer than the time. The four ways to stratify the torus coexist. The time
decides which one is the vacuum. It is a thermal transition at aspect ratio one, at every size. The seed test reads
exactly this: S(a; B) = sum over i of (q^(n_i) - q) q^(-a) is the weight of the other three phases in units of the
vacuum. GUIDE:
for Yang-Mills the nearest analogue is the deconfined phase on a short direction (K6 of run 2); the seed shape
avoids it when its time side is above the inverse deconfinement temperature.

**What is not settled.**

- (NS-gap) itself. It is a statement about Wilson SU(2). ST_q does not decide it.
- Models with a strictly positive kernel. (TM) states for Wilson that the vacuum eigenfunction is strictly positive.
  In ST_q the matrix T_B is reducible, the vacuum lives on the constant slices only, and the bulk free energy is
  zero. ST_q has no finite-energy property (Lemma FE of row 700 fails for it). So the question stays OPEN in this
  form: does a uniform gap on the cubes, with finite energy, force a seed? What ST_q shows is that a proof of
  (NS-gap) must use the strict positivity of the Wilson kernel, or more.
- A soft version. With a small positive weight for each plaquette that is not paired, the kernel is strictly
  positive. Then the q^n stratified ground states get fluctuation free energies that can depend on the pattern
  of the layers, and I did not analyse which patterns survive. ARGUED, not proved: by the hypercubic symmetry the
  entropy per layer of the surviving patterns along a space direction equals the gain per time step of the vacuum
  sector, so the balance of (c) would persist whenever that entropy is positive. OPEN.
- I did not search the literature for this model.

### 4.6 The enumeration (GUIDE; exact, small, no proof step)

All configurations were listed on small tori and the paired ones counted: sides (3,3), (3,4), (4,4), (3,5) with
q = 2; (3,3), (2,3) with q = 3; (2,3,3), (3,3,2) with q = 2; (2,2,3) with q = 3; (2,2,2,2), (2,2,2,3) with q = 2.
The counts are 14, 22, 30, 38, 51, 33, 16, 16, 39, 10, 14. Each equals the sum of q^(n_mu) minus (d - 1) q, and
every paired configuration depends on one coordinate. The transfer matrices of the two-dimensional model on rings of
3 and 4 sites (q = 2) and 3 sites (q = 3) have the eigenvalues q once, 1 with multiplicity q^b - q, and 0 with
multiplicity q - 1; the traces of their third, fourth and fifth powers equal q^a + q^b - q. The largest case has
2^24 configurations. The script is a scratch file outside the repository.

## 5. Step 4: necessity. What holds in the class, and what is open for Wilson

### 5.1 The cases side by side

| Model | cube gaps uniform | (a): a seed at each coupling | (N-phys) | (PS) | gap of the limit of the symmetric tori |
|---|---|---|---|---|---|
| ST_q (Section 4; one coupling) | yes, exact | no | no | no | no |
| line-spin (rows 1135, 1234; checks 1138, 1250) | yes, exact, in physical units | yes | no | no | yes |
| (N-phys) with alternative II of row 1161 (9) | yes on the neutral sector | yes (kappa) | yes | no | yes on A |
| Wilson SU(2) on the account's trajectory | OPEN | OPEN | OPEN | OPEN | OPEN |

Reading, with the mark of each entry.

- Line 1 is Theorem ST (PROVED here, unchecked).
- Line 2 is Proposition LS (PROVED in row 1234, checked by row 1250 after repairs). Its last entry is a direct
  computation: the model is a product of independent chains with the correlation exp(- eps t), and row 1234 records
  the exact physical gap. For the line-spin model the three sector sets do not apply (it has no centre symmetry);
  read (N-phys) and (PS) as the same statement on the whole trace.
- Line 3 is Theorem BP of row 1179 with the two alternatives of row 1161 (checks 1162, 1183). It is a statement of
  logic: the checked theorems give the gap on A in both alternatives and give (PS) in alternative I only. A model
  that is PROVED to have the neutral premise with alternative II is not on file. Frozen Z_2 above 2.191 has no
  periodic seed (the lane's Peierls bound, `gap-l3-direction-fable.md` L127); that its neutral seed holds is
  expected and not proved (row 731, table 6c).
- Line 4: no entry is known. GUIDE: every entry is believed to be "yes".

So the periodic seed exceeds what the gap clause consumes in two ways, and a third clause cannot be dropped:

1. **the branch** (line 3): (PS) is (N-phys) and (BS), and (BS) is not consumed;
2. **the cutoff-uniform seed size** (line 2): (N-phys) is (a) and (b), and (b) is not consumed;
3. **the thermal clause stays** (line 1): without it the cube gaps do not give the gap of the limit of the
   symmetric tori.

### 5.2 The price of a failure for Wilson

**Corollary F (PROVED GIVEN row 1161 L185-190, check 1162 S15).** Let K = 512. Suppose there are M_* > 0 and a
floor such that for every admissible L above the floor and all late j: m_{+,j}(n_j^3) >= M_* a_j, where n_j = L/a_j
is divisible by 2K and m_+ is the neutral gap of the cube. If (N-phys) fails at every admissible L, then for every
such L, with l = L/1024:

    D^+(l) >= (M_* l - log 2) / 2^30.

Here D_j(n) = F(n^4) - f n^4 is the Casimir free energy of the periodic symmetric torus and D^+(l) is the upper
limit over j of D_j(l/a_j).

Proof. Row 1161 proves, at every coupling, s_j(n/K) <= exp((2K)^3 D_j(n/(2K)) - n m_{+,j}(n^3)/(2K)). If (N-phys)
fails at L, then for infinitely many j the test fails at the integer u = n_j/K, so s_j(n_j/K) > 1/2 (the lattice
range 4 | n_j, n_j >= 2^70 holds for late j). For those j: (2K)^3 D_j(n_j/(2K)) > n_j m_{+,j}/(2K) - log 2
>= L M_*/(2K) - log 2. Take the upper limit; (2K)^3 = 2^30 and L/(2K) = l. QED

Remarks.

1. The contrapositive is the neutral, physical form of Corollary Z2 of row 720, with a worse constant: uniform
   neutral cube gaps and D^+(l) < (M_* l - log 2)/2^30 at one admissible l give (N-phys). In neutral variables the
   two-sided statement is row 1161 L389-400 (check 1162 S19).
2. The account excludes the line-spin mechanism for Wilson (PROVED GIVEN the statements of the account quoted in
   row 720 1.1.2: the torus conditions (UV-Z) of Obligation D1 and the torus-independence of the vacuum density,
   CA-II 8.22; row 720 read the statements, not the proofs). By row 720 1.1.5 (iii), D_j(l/a_j) <= C l^4 on the
   account's tori, uniformly in the cutoff, and multiplying the four sides by an integer multiplies the bound by its
   fourth power (`gap-crux-restate.md` Section 1). So D^+(l) is finite at each such size. In the line-spin model
   D^+ is infinite at every fixed physical size (row 1135; check 1138).
3. So for Wilson, given the account, a failure of (N-phys) with uniform neutral gaps needs
   (M_* l - log 2)/2^30 <= D^+(l) at every size l = L/1024 with L admissible, and D^+(l) <= C l^4 at the
   multiples of the account's sides: a Casimir free energy of the symmetric torus that grows at least linearly for
   ever. In ST_q this happens, with D(a) = m_0 a + O(1). So no argument that uses
   only the class properties turns Corollary F into a contradiction. GUIDE: for Wilson D^+ is expected to fall
   exponentially (thermal pressure of a gapped phase below the deconfinement temperature).

### 5.3 The three options of the brief

- **Option 1, the weakest statement at one scale that suffices through checked results.** Done. It is (N-phys),
  over the sizes the uniform kappa seed (Theorem O). It reads the neutral sector only. The statement consumed is
  weaker and is not at one scale: (G_ev-phys) (Proposition C). A statement on local observables only has no consumer
  and is not expected to have one (Section 3, ARGUED).
- **Option 2, necessity of (N-phys) for Wilson up to constants.** NOT proved. Shown: it does not follow from the
  class properties, at one coupling (ST_q) or along the cutoff (line-spin). Under uniform neutral cube gaps it
  follows from a bound on D^+ below the line of Corollary F at one size. That bound is OPEN for Wilson ((NS-gap) of
  row 700 in physical form). A proof must use the strict positivity of the Wilson kernel and the account's bound
  on D^+, or more.
- **Option 3, the seed fails for Wilson while the gap holds.** NOT shown. In the class each excess can fail alone
  (5.1). For Wilson a failure of (N-phys) with the gap clause true needs one of two things: the limit has a gap
  while the neutral gaps of the finite cubes are not uniform in physical units; or the linear growth of
  Corollary F. No checked statement excludes either. GUIDE: neither is expected. For (PS) there is a third way to
  fail, alternative II, which no checked statement excludes for Wilson and which GUIDE physics (confinement) does.

## 6. Decision, and what changes

**Decision (ARGUED; each item rests on the statement named in it).**

1. *Right in kind.* The target of the infrared chain should stay a thermal statement at one scale. The engine on
   file (Theorem S-w) reads traces. A statement on finitely many local observables has no consumer. A uniform gap
   of the cubes is too weak in the class: ST_q has it and has neither a seed nor a gap of the limit. For Wilson it
   could do only through a property that ST_q lacks (item (2) of "What would change the decision").
2. *Wrong in sector, as the chain now words it.* The periodic two-period bound of Theorem ZD-c is (N-phys) and the
   branch selection. The gap clause uses (N-phys) only. The branch selection is confinement on tori. It is a
   second theorem, not a step of the first.
3. *Sufficient, not necessary.* (N-phys) also asserts that the seed size is bounded in physical units. The gap
   clause does not use that (line-spin). Nothing weaker at one scale is on file. So a proof of the gap clause through
   any seed proves more than the Jaffe-Witten gap: it also bounds the number of light neutral states of one cube.

**The three forms of the target, with their constants (PROVED GIVEN Lemma TP and the rows cited in Theorem O).**

- (T-N), neutral, positive measure, order-one margin, aspect 512. With Z_+(v) the mean, over the eight temporal
  twists (the trivial one included), of the partition functions of the torus v x n_j^3: for all late j there is an
  integer 3 <= u_j <= n_j/512 with Z_+(2u_j)/Z_+(u_j)^2 >= 2/3, at one admissible L (4 | n_j, n_j >= 2^70). This
  gives (N-phys).
- (T-K), kappa, signed sum over the 64 twists, small margin, aspect two. For all late j:
  W_kappa(N_j)^2/W_kappa(2N_j) <= 1 + s_* on the cube (2N_j)^3, with s_* < 1/5041 and N_j a_j fixed. This gives
  (KS).
- (T-P), periodic, as in rows 1323 to 1339. It gives (PS). It is (T-N) at a larger size together with (BS).

GUIDE on sizes: (T-P) and (T-K) need about 23 correlation lengths, (T-N) about 11000 (Section 3).

**What this does not say.** I have no evidence that (T-N) or (T-K) is easier to prove for Wilson than (T-P). Both
are true if (T-P) is true at a larger size, and both are statements at a coupling of order one. What is certain
is the logic: they need no branch selection, and a method that does not read the centre can reach them and cannot
reach (T-P).

**Two tests for later rows (proposed to the lead; no file other than this one was edited).**

- *The ST_q test.* A proposed derivation of a seed, or of the gap of the limit of the symmetric tori, from gaps of
  periodic boxes must use a property that ST_q does not have (strict positivity of the kernel, finite energy, or
  a thermal clause). If every hypothesis holds in ST_q, the derivation is wrong.
- *The line-spin test* (on file since row 1234). A proposed derivation of (N-phys) from (G_ev-phys) must use a
  count that is uniform in the cutoff, such as the account's bound on D^+.

**What would change the decision.** (1) A proof of (EV-STEP): then the neutral trace at aspect two on one cube
would be the target. (2) A way to identify the limits of the symmetric tori and of the cylinders without a thermal
sum, using a property that ST_q lacks: then the cube gaps would be enough. (3) A proof that alternative II cannot
occur for Wilson: then (T-P) and (T-N) would be one statement over the sizes.

## 7. What this row did not do

1. It did not check the cited rows line by line again. Proposition C, Theorem O and Corollary F are readings of
   statements whose recorded checks are named. A checker should confirm three points: that the hypothesis of
   Theorem L3-ev is (G_ev) with a free rate m_0; the third arrow of Remark 3 in Section 2; the arithmetic of
   Corollary F.
2. Theorem ST, Lemmas ST1 and ST3 and Corollary ST2 are proved by hand and not checked. Points to test first: Step
   2 of Lemma ST1 on a side of length 2; Lemma ST3 (ii); the limit in Theorem ST (e).
3. It read no published literature and did not search for the model ST_q there.
4. It did not construct a version of ST_q with a strictly positive kernel.
5. It did not attack (N-phys), (BS), (EV-STEP), (NS-gap) or the continuum datum. They stay OPEN.
6. It ran no large computation. The one run is the enumeration of 4.6, under a minute, a GUIDE.

RESULT: Row 1342 (Claude Fable 5.2 max, laptop subagent; author only, checked by no one; one exact guide enumeration of under a minute, no large computation). Decision: the seed is right in kind and wrong in sector as the chain words it. (1) The two-period bound of Theorem ZD-c that rows 1323-1339 attack is not (N-phys): it is (N-phys) plus the branch selection (confinement on tori), and the gap clause uses (N-phys) only (PROVED GIVEN rows 1161 and 1179 with checks 1162 and 1183; Theorem O: (N-phys), over the sizes the uniform kappa seed, is the weakest one-scale statement with a checked consumer; in two-period form, Z_+(2u)/Z_+(u)^2 at least 2/3 at one u at most n/512 for the mean Z_+ of the eight temporal twists). (2) What the gap clause consumes is weaker and not at one scale: (G_ev-phys), neutral cube gaps of at least M_* in physical units with a neutral thermal sum tending to zero at each cutoff, with no bound on the seed size (Proposition C, a reading of rows 731 and 1179). (3) NEW, PROVED by hand, unchecked: the stratified model ST_q (q-state spins, every plaquette paired) is local, hypercubic and reflection positive, has a simple vacuum and the exact gap log q on every periodic box, has S(N; (2N)^3) at least 5 for every N and D(a) = log(4 q^a - 3q), and its limit of symmetric tori does not cluster; so in the class of Theorem S a uniform gap gives neither a seed nor the gap of the limit at one coupling (open since rows 700 and 720), Corollary Z2 is sharp in order, and a gap-only target is wrong; ST_q has hard constraints and a reducible transfer matrix, so the question stays open for strictly positive kernels such as Wilson. (4) (N-phys) is sufficient and not necessary in the class (Proposition LS); for Wilson, uniform neutral gaps with (N-phys) failing at every size force D^+(l) at least (M_* l - log 2)/2^30 (Corollary F, PROVED GIVEN row 1161, check S15), while the account bounds D^+ at each size; necessity for Wilson is NOT proved and a failure for Wilson is NOT shown. OPEN: (N-phys), sublinear D^+ for Wilson ((NS-gap)), the branch selection, (EV-STEP), a soft version of ST_q, the continuum datum, the mass gap. Output library/gap-seed-audit-fable.md.
