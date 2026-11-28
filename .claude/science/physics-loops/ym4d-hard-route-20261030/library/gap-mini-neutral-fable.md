lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T09:58Z

# gap-mini-neutral-fable: the one-cube physical neutral upper bound

FINISH row 1180 (`gap-mini-neutral-fable`). Status marks: PROVED, ARGUED, GUIDE, OPEN. No subagents.

**Provenance of this file.** An earlier run of this item (Claude Opus 5.5 at max effort, started
2026-11-19T21:48Z by its own `date -u`, pinned at commit 0d6295dd9) wrote only a header and the plan
below; its header lines were `lead: anthropic/claude-opus-5-5/max mac-mini-worker` and
`lease_until: 2026-11-20T09:48Z`. This session (Claude Fable 5.2 at max effort, started
2026-11-19T21:58Z by `date -u`, pinned at commit 3b1d5e14f on branch `claude/ym4d-hard-route`)
keeps that plan and continues from it. All mathematical content below is from this session.

## Plan (earlier run, kept; written before reading the chain)

1. Read the row's required sources: `library/gap-council-synthesis.md`, `parts/gap.md` (methods 1-36,
   route registry), RESULT lines of FINISH rows 1143-1177, and the defining texts of the "one-cube
   physical neutral upper bound" in rows 1161, 1175, 1177 (`gap-solve9-astra62.md`,
   `gap-solve16-astra62.md`, `gap-solve17-astra62.md`).
2. Write down the exact statement of the bound (call it N1) with every quantifier, and record what is
   already on file about it (grep open-core.md and FINISH rows; stop if another row covers it).
3. Attack: try to prove N1, or disprove it, or prove the strongest true statement toward it; for
   every route tried, record the precise obstruction.
4. One RESULT line at the end.

Each step below is appended as it finishes.

## Step log (this session)

### Step 1. The exact statement, and what is on file (reading only; no new claim)

Written 2026-11-19T22:04Z (`date -u`).

**Setting (row 1161, `gap-solve9-astra62.md` L13-63; credit: the positive transfer and trace identity GL8 of
Sussman and Alpoge, with Claude and Codex as authors of their text; Balaban for the ultraviolet trajectory).**
Wilson SU(2) at coupling beta on the periodic spatial cube n^3, 4 | n. F is the symmetric magnetic sandwich
(the positive transfer operator on gauge-invariant functions of the spatial links), lambda_0 = ||F||, G = (Z/2)^3
the centre flips. X_{m,q}(u) = Tr_q (F_m/lambda_0)^u for static magnetic twist m and electric character q, in
units of the periodic vacuum. The periodic neutral excited sum is

    s(u; n) = X_{0,0}(u) - 1 = sum over excited neutral levels of (lambda_i/lambda_0)^u.

**(N-phys), the one-cube physical neutral upper bound** (row 1161 L146-148 and L215; in the wording of row 1179,
`gap-mini-branch-fable.md` Section 6): there is one admissible physical side L and an index j_0 such that for
every j >= j_0, with n_j = L/a_j and 4 | n_j, there is an integer u_j with 3 <= u_j <= n_j/K and

    s_j(u_j; n_j) <= 1/2.

K is the aspect of row 1161's finite-aspect statement; the explicit version is K = 512 with n_j >= 2^70
(row 1161 L215). Rows 1175 and 1177 read the same premise (row 1175 L59 "row 1161's short-period periodic
neutral premise at one permitted physical side"; row 1177 RESULT "given the one-cube physical neutral bound").
So the three rows need one statement, (N-phys).

**In plain words.** With H_n = -log(F/lambda_0) on the cube n^3, (N-phys) says Tr_neutral exp(-u H_n) <= 3/2 at
u = n/512: the centre-neutral thermal partition function at temperature 512/L on the box L^3 is at most 3/2 in
vacuum units, uniformly in the cutoff. GUIDE: for a free massless field the same trace is exp(c 512^3); for a
theory with lightest neutral mass m it is about 512^3 (x/2 pi)^(3/2) exp(-x) with x = m L/512, so the bound asks
for m L of order 10^4. It is a statement at one large physical size, not a small-volume statement.

**What is on file about (N-phys)** (each line read at this pin):

1. Consumer, PROVED in row 1161 (checked by Opus 5.5 max in row 1162): (N-phys) gives a cutoff-uniform
   Pfaffian seed S_kappa < 2^(-18) at time n/2, and one of two flux alternatives (9).
2. Row 1179 (`gap-mini-branch-fable.md` Theorem BP, PROVED GIVEN rows 697, 700, 731, 1161; checked by no one):
   (N-phys) alone gives a cutoff-uniform gap on the centre-blind sector and, with the continuum datum, the
   Jaffe-Witten gap clause in both flux alternatives. So (N-phys) is the whole gap clause in this lane.
3. Necessity, PROVED in row 1161 L150: (W) implies (N-phys) on all large dyadic sizes.
4. Equivalent forms over physical sizes, PROVED in row 1161 (26) and L389-400: a cutoff-uniform Pfaffian seed
   iff S^+_ev(L) -> 0 on dyadic sizes iff (S^+_ev bounded and the neutral dimensionless gap z^-_+ unbounded),
   where S^+_ev(L) = limsup_j s_j(n/2; n) is the neutral excited sum at aspect two.
5. Lower bounds, PROVED in row 1161 (17), (19): s(u) >= c n^3 exp(-C u) at every beta >= 1, so u = o(log n)
   is excluded. Row 1153: the short-period trace is a free gluon gas.
6. Abstract obstructions, PROVED: the sign-product comparison (row 1161 L375), the finite-moment construction
   (row 1161 L404), the local neutral spectator (row 1175 (29)), the centre-spectator principle of the council
   (rows 1128-1134), Lemma PT and Proposition NP (rows 998, 1003).
7. The glue-half engine: rows 1124-1125 ((GLUE-STEP), found-again, no first leaf), row 731 ((G_ev), (EV-STEP)),
   route RE. No published theorem gives an order-one four-dimensional non-abelian glue-half seed (row 1124).

**Rule 0a.** `grep -i neutral library/open-core.md` returns nothing. FINISH rows that name the neutral bound:
1161-1177 (the chain that states it as OPEN), 1178 (`gap-solve18-astra62`, the chain's general continuation on
(W), running now), 1179 (branch selection, not this bound), 1181 (free method). No other row is assigned the
neutral bound; row 1180 (this row) is. I proceed.

**Kind of statement (lead rule W2).** (N-phys) is selective: it is false for the free photon and for compact
U(1) in its Coulomb phase (massless neutral states at every size), and it is violated by a product with a
massless or slowly cooling neutral spectator (item 6). A proof must read the non-abelian group at a scale of
order one in the coupling. It is (K-flow) in the lane's terms if proved along the trajectory, (K-one) if proved
at one bare coupling with a carry to finer cutoffs.

### Step 2. What (N-phys) says at each fixed coupling (corollaries of statements on file)

Written 2026-11-19T22:38Z (`date -u`). Nothing in this step closes (N-phys).

**2.1 Fixed-coupling form (PROVED GIVEN row 1161 L215 and L335; a corollary, no new input).** Let nu(beta)
be the least n with 4 | n, n >= 2^70 and s(floor(n/512); n) <= 1/2 at the bare coupling beta, and nu = infinity
if there is none. Row 1161 L335 proves this chain at a fixed coupling: the test at (beta, n) gives a Pfaffian
seed at n (L215); Theorem S-w propagates it to the sides 2^k n; Proposition B3 enlarges the cube 512-fold at a
fixed multiplier on the log excess; so the test holds again at the sides 512 * 2^k * n for every k >= k_0. The
integer k_0 depends only on the seed margin 2^(-18) and on the multiplier, so it is absolute. Arithmetic
(ARGUED: it uses Theorem S-w of row 731, `gap-flux-exercise.md` L507-509, and (B3-q) of `gap-seed-shape.md`
L76 as read, for the class kappa as row 1161 L335 does; no line-by-line check): with q < 5041 x 2^(-18) < 0.0193
and b = 2^k n, S_kappa(b/2; b^3) <= q^(2^k)/71; (B3-q) with a = b/2 gives the multiplier 512^3 x 8 = 2^30 on the
log excess; so s(b; (512 b)^3) <= exp(2^30 q^(2^k)/71) - 1, which is at most 1/2 when 2^k log(1/q) >= 17.5, that
is from 2^k = 8. So k_0 = 3 is enough. Hence, on the lane's dyadic grid (row 1161 L150, L389):

    (N-phys) at some admissible L   iff   limsup_j a_j nu'(beta_j) < infinity,

where nu' is nu restricted to grid sizes. The "only if" part is the definition. The "if" part is the chain.

In words, (N-phys) is two statements.
- (a) Every fine coupling beta_j has a finite seed size. This is a lattice gap for centre-neutral states at
  arbitrarily weak coupling.
- (b) The seed size grows no faster than 1/a_j. This is a lower bound of asymptotic-scaling type on that gap.

**2.2 Subsequences (on file: row 1179, Proposition P'-ev).** Row 1161 L148 applies the premise one cutoff at a
time. Row 1179's Proposition P'-ev (`gap-mini-branch-fable.md` L253-259) is stated for any cutoffs iota_j with
a_(iota_j) -> 0 along which the seed holds. So the gap clause for a continuum datum reached along such cutoffs
needs the premise along them only: liminf_j a_j nu'(beta_j) < infinity is enough, given that row's hypotheses
(H2), (TOT), (P4). This is that row's statement read with 2.1. It is not a new result.

**2.3 Size of the task (reading).** By row 1179 Theorem BP (ii), (N-phys) gives at every fine coupling beta_j a
centre-even gap of at least M_* a_j on every large periodic cube. Row 1124 found no published theorem that gives
a gap or a thermal seed for four-dimensional Wilson SU(2) at a coupling of order one. So a proof of (N-phys)
contains a new theorem at each beta_j. This measures the task. It is not an obstruction.

**2.4 Where the bound can first hold (GUIDE; no proof reads this).** For a dilute gas of one scalar of mass m on
the box L^3 at temperature K/L, log(1 + s) is about K^3 (x/2 pi)^(3/2) exp(-x) with x = m L/K. With K = 512 this
is below log(3/2) from x of about 21, so from m L of about 1.1 x 10^4. With the lane's guide value m = 3.78
sqrt(sigma) (row 1063) this is L sqrt(sigma) of about 2900, and the temperature 512/L is about a quarter of the
deconfinement temperature. Below that size the short direction is hot, and log(1 + s) is of the order of
512^3. So (N-phys) is a statement about one very large cube. No small-volume expansion reaches it.

### Step 3. Routes tried, with the first failing step of each

Written 2026-11-19T22:38Z (`date -u`). Each route below was worked by hand in this session until it reached a
precise failing step. For each, the obstruction is stated, and the place where the lane already has it is
named. I found no route whose first failing step is not on file. No line below is a new result.

**R1. Count by reflection positivity, then decay by one gap.** Chain: s(u; n) <= (count at an earlier time v)
x exp(-m_+ (u - v)). The ultraviolet bounds give an extensive count, log(1 + s(v; n)) <= c_0 (L/l)^3, with l
the first-passage scale and v a_j = tau_0 fixed. Arithmetic (PROVED, elementary): with a cutoff-uniform gap M,
the chain gives s <= 1/2 at u = n/K only if M L/K >= c_0 (L/l)^3 + log 2 + M tau_0 for some L >= l. The left
side minus the first term on the right is concave in L, with slope M/K - 3 c_0/l at L = l. So a solution with
L >= l needs M l >= K min(c_0 + log 2, 3 c_0), which is at least K c_0. The count must therefore have a density
scale of at least K c_0 correlation lengths. At the first-passage scale M l is small. So the count has to be
an infrared input.
On file: row 1153 L393-397 (the exact first gap applied to the whole short-period multiplicity diverges); row
1161 L185-190 (the same chain with (BDD-Delta) as the count); row 1135 (a gap does not bound the torus excess
in general: the line-spin model; `parts/gap.md` L188).

**R2. The thermodynamic form.** Reading the torus n^3 x u in the other three frames gives
1 + S_per(u; n^3) <= exp(n^3 u [e(n^3) - e(u^3)]) (1 + S_per(n; u^3)), with e(B) the vacuum energy per site of
the box B, and e(n^3) >= e(n, n, u) >= e(n, u, u) >= e(u^3) when u divides n. I derived this by hand and then
found it in the lane: it is Lemma Z and Lemma Z' of row 720 (`gap-phys-seed.md` L253-279) with Proposition B3
(`gap-seed-shape.md` L72-77), in the variable F(n)/abs(n). First failing step: the excess of the periodic torus
of side u must be below log(3/2)/K^3 uniformly in the cutoff. That is a periodic seed at side u. It is stronger
than (N-phys).

**R3. Integration in the coupling at a fixed lattice shape.** d/d beta of log(1 + S_per(u; n)) is the sum over
the plaquettes of n^3 x u of the plaquette mean at period u minus its mean in the vacuum. The bound is true at
small beta. First failing step: a signed bound on this response at couplings of order one. On file: row 1145,
inequality (24) ("the real form of (W)", on the path in the spatial coupling), with its proved obstructions to
continuation, and rows 1147-1151; for the path in the isotropic coupling, row 1161 L325-339 (the sets P, M, N
and the fixed-coupling obstruction to a change of branch).

**R4. Operator inequalities (min-max against the electric operator; Golden-Thompson is of the same kind).** First
failing step: the comparison trace does not carry the vacuum energy of F, so the bound exceeds lambda_0^u by a
factor exp(c u n^3). PROVED for the min-max comparison in Lemma R4 of Step 3a, at every beta; ARGUED for
Golden-Thompson. On file in kind, not in this form: method 35 (`parts/gap.md` L69); row 1145 (absolute
summation).

**R5. Crossing at the symmetric torus without the premise.** A scale-invariant spectrum satisfies crossing and
positivity in all four frames at every size. So crossing gives no upper bound on s without a seed. On file: the
massless floor (row 988, Lemma FLOOR; method 26); the test table rows "free photon" and "product with a massless
factor" (`parts/gap.md` L296-297).

**R6. A selective seed at weak coupling on thin or twisted boxes.** With a twist through two short sides the
gluon modes have no zero momentum, so the box has a gap of order 1/(short side) at weak coupling, and compact
U(1) has none. First failing step: no engine carries a seed from a box with short sides to a cube, and doubling a
twisted side removes the twist. On file: Route T and (AC'-lat), rows 678-687 (`gap-ac-lat.md`); the council,
2c (`gap-council-synthesis.md` L54-59).

**R7. Curvature of the group at the lattice scale.** A Bakry-Emery bound with the Ricci curvature of SU(2)
would give a gap of order 1/beta in lattice units. First failing step: the pointwise curvature condition for
the vacuum measure fails beyond beta = pi^2/4 (PROVED, Lemma R7 of Step 3a). On file: method 31 (rows 957, 968);
row 1128, Proposition G1.

**R8. One coupling, then a carry to finer cutoffs.** In the form of 2.1: a seed at one beta_J and
nu(beta_(j+1)) <= 2 nu(beta_j) from J on. First failing step: the carry needs the thermal trace at a fixed
physical shape to converge as the cutoff is removed, with an error o(1) in the total. The ultraviolet bounds
give errors per unit physical volume. On file: row 978 (no carrier; the carry is (NOCRIT) of row 709 plus a
climb), with the correction of its check.

**R9. The count from the gap.** First failing step: a uniform gap does not give a bounded count in the class.
On file: row 1135 (line-spin model; sufficient extra input liminf D^+(L)/L below m_0/64); the hypothesis (DS-W)
of row 691 (`parts/gap.md`, route registry).

### Step 3a. The obstructions of R4 and R7 as precise statements

Written 2026-11-19T22:48Z (`date -u`). Two short lemmas, so that R4 and R7 do not rest on an argued sentence.
Both are elementary. Neither moves the wall. Conventions: row 1161 L17 and L248 (F = D C D on gauge-invariant
functions of the 3 n^3 spatial links, C the normalized electric convolution with one-link density proportional
to exp(beta w), w = half the trace, D multiplication by exp((beta/2) A), A the sum of w over the 3 n^3 spatial
plaquettes, psi the positive vacuum, pi = psi^2 dx). Put r = I_2(beta)/I_1(beta), the mean of w under the
one-link density; 0 < r < 1.

**Lemma R4 (PROVED; uses the bounded-difference inequality of McDiarmid, cited, not rebuilt).** For every
beta > 0 and even n,

    lambda_0(F) <= 4 ||D||^2 exp(-2 c_4 n^3),   c_4 = min{ (3/256)(1 - r^4)^2, (3/4) beta (1 - r^4) }.

So the min-max comparison lambda_k(F) <= ||D||^2 lambda_k(C) gives no better bound on the neutral trace than
(exp(2 c_4 n^3)/4)^u, which is above 3/2 on every cube with n^3 > 0.9/c_4.

Proof. Let theta = (1 - r^4)/2, G = {A >= (1 - theta) 3 n^3} and P the multiplication by its indicator. For a
unit vector phi, <phi, D C D phi> = ||C^(1/2) D phi||^2, and D phi = P D phi + (1 - P) D phi. The first part has
norm at most ||P C P||^(1/2) ||D||. The second has norm at most ||D|| exp(-(3/2) beta theta n^3), because
D <= ||D|| exp(-(beta/2) theta 3 n^3) off G. So lambda_0(F) <= ||D||^2 (||P C P||^(1/2) + exp(-(3/2) beta theta
n^3))^2. The kernel of P C P is symmetric and non-negative, so ||P C P|| <= sup_x (C 1_G)(x) (Schur test), and
(C 1_G)(x) is the probability that x xi lies in G, with one independent link noise xi_e per link. The mean of a
central noise in the fundamental representation is r times the identity, so the mean of w_p(x xi) is r^4 w_p(x),
at most r^4, for every x. One link lies in four spatial plaquettes, so one noise changes A by at most 8. McDiarmid
gives P(A - mean >= t) <= exp(-2 t^2/(64 x 3 n^3)); with t = (3/2)(1 - r^4) n^3 this is exp(-(3/128)(1 - r^4)^2
n^3). Both exponentials are at most exp(-c_4 n^3). The comparison: the non-zero spectrum of D C D is that of
C^(1/2) D^2 C^(1/2) <= ||D||^2 C, on the neutral gauge-invariant space as well, and Tr_neutral C^u >= 1. QED

**Lemma R7 (PROVED).** Let M be the product of the 3 n^3 unit three-spheres with its product metric (Ricci = 2
on each factor). For beta > pi^2/4 there are a point of M and a unit single-link direction v with
Ric(v, v) + Hess(-log pi)(v, v) <= 2 - 8 beta/pi^2 < 0. So no curvature bound CD(kappa, infinity) with kappa >= 0
holds for (M, pi) beyond beta = pi^2/4.

Proof. Move one link e along the closed unit-speed geodesic x_e(t) = cos t + i sin t sigma_3, 0 <= t <= 2 pi,
all other links equal to the identity, and put h(t) = -2 log psi along it. psi is smooth and positive, since
psi = lambda^(-1) D C D psi with smooth positive kernels. At t = 0 all plaquettes equal 1; at t = pi the four
plaquettes through e equal -1. So D(0)/D(pi) = exp(4 beta). The one-link kernel ratio c(y_e)/c(-y_e) =
exp(2 beta w(y_e)) is at least exp(-2 beta). Hence psi(0)/psi(pi) >= exp(2 beta) and the oscillation of h is at
least 4 beta. If h'' >= -a on the circle, Taylor's formula at a maximum point gives an oscillation of at most
a pi^2/2. So h'' <= -8 beta/pi^2 at some t, and h'' is the Hessian of -log pi in the unit direction of the
geodesic. QED

Scope: Lemma R7 is for the product manifold, not for the quotient by gauge transformations, and for a pointwise
bound only. Averaged curvature is the lane's method 31 (`gap-avgcurv-max.md`, rows 957, 968); I did not reread
those files, so I do not claim Lemma R7 is new.

### Step 4. Verdict

Written 2026-11-19T22:44Z (`date -u`).

**(N-phys) is OPEN.** This session did not prove it and did not disprove it.

- No proof. Each of the nine routes of Step 3 stops at an inequality at a coupling of order one that must read
  the group. This is the lane's wall (`parts/gap.md`, "The exact price").
- No disproof. A disproof would be a massless or critical centre-neutral sector for continuum SU(2) at every
  physical size. No statement on file gives that, and none was found here. The proved lower bounds on s (row 1161
  (17), (19); row 1153) stop at periods far below a fixed fraction of the side.
- Strongest true statements toward it, all on file before this session: the consumer and the necessity of row
  1161; the equivalent forms of row 1161 (26) and L389-400; the fixed-coupling sets of row 1161 (22). Step 2.1 of
  this file only rewrites (N-phys) with them: every beta_j has a finite seed size, and that size is O(1/a_j).

**What this row changes for the lane.** Nothing in the proof chain. It gives one more reading of the kind the
council gave (row 1134, 2a): an independent pass from the thermal side reached the lane's own entries at every
route. So a further row whose task is a new form of (N-phys), or a new soft route to it, is not worth its cost.
The two open inputs are those of 2.1: (a) a seed at a fixed coupling (the lane's (SEED), route RC), and (b) the
carry to finer cutoffs (row 978, (NOCRIT) of row 709).

**Not done, not verified.**
- I did not read the files of rows 1163-1173 and 1177 beyond their FINISH RESULT lines and the entries in
  `parts/gap.md`. I read rows 1161 (all), 1175 (L300-338 and the neutral lines), 1153 (the lines on J_m and
  L393-413), and the statements of Lemma Z, Lemma Z', Proposition B3 and Theorem S-w.
- The value k_0 = 3 of 2.1 is ARGUED (arithmetic on two statements as read, not a line-by-line check).
- Lemmas R4 and R7 of Step 3a are proved here by hand and not checked; the Golden-Thompson part of R4 is ARGUED.
- No numeric run was made. No statement here was checked by another model.
- Search scope: this checkout only. `origin/main` and the open pull-request branches were not searched (they are
  not refs in this checkout).

**Credits.** Tadeusz Balaban (the renormalization group behind the trajectory). Ethan Sussman and Levent Alpoge,
with Claude and Codex as authors of their text (the positive transfer operator and trace identity GL8, and the
account that supplies the trajectory). Sourav Chatterjee (the weak-coupling free-energy method used in rows
1143-1153). The gpt-6.2-astra chain, rows 1143-1177, and Claude Opus 5.5 as its checker: every statement about
(N-phys) used here is theirs. Row 1179 (Claude Fable 5.2): Theorem BP.

RESULT: Row 1180 (Claude Fable 5.2 max, Mac mini worker; author, checked by no one; no numeric run; no mass gap claimed). The one-cube physical neutral upper bound (N-phys), s_j(floor(n_j/512); n_j) <= 1/2 at one admissible physical side uniformly in the cutoff, is NOT proved and NOT disproved; it stays OPEN. FOUND-AGAIN: nine routes were worked from the thermal side to a precise first failing step (count by reflection positivity plus one gap; the vacuum-energy form; integration in the coupling; operator inequalities; crossing without a premise; weak-coupling seeds on thin or twisted boxes; group curvature at the lattice scale; one coupling plus a carry; the count from the gap), and every one is already on file (rows 678-687, 709, 720, 957, 968, 978, 988, 1128, 1135, 1145, 1153, 1161, methods 26, 31, 35). PROVED GIVEN row 1161 (a corollary, no new input): (N-phys) holds iff every fine coupling beta_j has a finite one-cube seed size nu(beta_j) and limsup_j a_j nu(beta_j) is finite on the dyadic grid; so it is a lattice gap for centre-neutral states at arbitrarily weak coupling together with a lower bound of asymptotic-scaling type. For one continuum datum, liminf in place of limsup is enough (this is row 1179's Proposition P'-ev read with the corollary). PROVED by hand, unchecked, elementary, and they do not move the wall: Lemma R4 (the electric min-max comparison loses a factor exp(2 c_4 n^3)/4 per time step at every beta) and Lemma R7 (the pointwise Bakry-Emery condition for the vacuum measure fails beyond beta = pi^2/4). OPEN: (N-phys); the seed at a fixed coupling in the band; the carry to finer cutoffs; the selective inequality; (W); the mass gap.
