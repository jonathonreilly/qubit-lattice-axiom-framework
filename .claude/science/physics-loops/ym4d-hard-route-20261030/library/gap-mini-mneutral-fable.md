lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-21T18:14Z

# Row 1356, gap-mini-mneutral-fable: attack on (M-neutral)

Worker: Claude Fable 5.2 (max effort) on the Mac mini, pinned at commit 30a300a5c of branch
`claude/ym4d-hard-route`. Research-stage working state; nothing here is a public claim. Every statement below
carries one of the labels PROVED, ARGUED, GUIDE, OPEN. A "PROVED" here means proved in this file and not yet
checked by anyone else.

## 0. Status log (times from `date -u` in the command that wrote the line)

- 2026-11-21T06:14Z: file created (save protocol). Nothing read yet beyond the queue row, GOAL.md and my navigation notes.
- 06:32Z: read the row, GOAL.md, the rule sections of FINISH.md, row 1353's file in full, the sibling file of row 1354, parts/gap.md L8-104, Theorem ZD-c, Identity I1, row 1168 (19)-(21), the route tables of rows 1180 and 1184; registry grep run; Section 1 written.
- 06:42Z: Sections 2 and 3 written (Lemma M1, Corollary M2, choice of attack). Next: Way 1, transport with comparison of all eigenvalues.
- 06:47Z: Section 4 written (Way 1: Proposition TR, Corollaries TR1 and TR2, Lemma UVC; supplier absent). Next: Way 2, coding.
- 06:50Z: Lemma VOL (4.7) and Section 5 written (Way 2: Proposition COD via row 1165 (19); supplier absent). Next: Way 3, the Wilson transfer operator with discrete time.
- 06:52Z: one-second guide check of Proposition TR on one link run under the numeric lock (pass); 4.8 (Lemma GAUSS, guide record) and Section 6 written (Way 3: Lemma JF, no count from the jump form).

## 1. Repo search and inputs (written 06:32Z, `date -u`)

Rule 0a and "Repo first". Before any derivation I searched `library/open-core.md`, every `library/gap-*.md`,
`library/prior/gap-*.md`, `parts/gap.md` and the `FINISH.md` rows with `/usr/bin/grep -l -i -F` for the terms of
each statement I considered. `library/open-core.md` has no line on (M-neutral), (N-phys) or a rank-one test.
Cross-branch search (main and the open YM4D pull requests): not repeated; rows 1351 and 1353 record it for the
same statement on the same day (`gap-blockstep4-astra62.md` L3), with no proof of the neutral seed found.

Inputs read. In full: `library/gap-mini-neutral-step-fable.md` (row 1353; its check, row 1355, has no file at
this pin, so its statements are "unchecked at this pin"); the file of the sibling row 1354 as far as it exists at
this pin (`library/gap-mini-nphys-fable.md`, Steps 0-2). In part: `GOAL.md`; `FINISH.md` L1-84, L320-351 and the
RESULT lines of rows 1326, 1331, 1332, 1335, 1340, 1342, 1349, 1351, 1352; `parts/gap.md` L8-104;
`library/gap-phys-seed.md` L283-327 (Lemma Z3, Theorems ZD and ZD-c, Corollaries Z2 and Z4);
`library/gap-compress-opus.md` L28-60 (Identities I1, I2); `library/gap-solve11-astra62.md` L286-320 (row 1165,
(19)-(21)); the route tables of rows 1180 and 1184 (`library/gap-mini-neutral-fable.md` L134-200,
`library/gap-mini-neutral2-fable.md` L109-200).

What the target is, on file. (M-neutral) is (N-phys) up to the choice of times (row 1353, Corollary BT2).
(N-phys) is the crux lemma (GLUE-FP)_sigma of rows 895 and 920 with other constants, and its consumer is row 1161
(7). Rows 1180, 1184 and 1353 are three earlier attacks by this model on the same statement. Their route tables
hold about 25 routes, each with its first failing step. I do not repeat them.

Matches for every form of the target that I derived again in this session (none is called new below):

| Form (my words) | On file | Verdict |
|---|---|---|
| The squared Hilbert-Schmidt distance to rank one is the excited trace at twice the time; chi-square mutual information of two slices of the vacuum chain | Identity I1, `gap-compress-opus.md` L36-46 (row 839); Lemma BT of row 1353 | on file |
| Purity: (N-phys) says Tr rho^2 >= 2/3 for the neutral thermal state; Renyi-2 and min-entropy forms | Identity I2, `gap-compress-opus.md` L48-58; `gap-skeleton-max.md` L264; row 1354 Step 1.1 | on file |
| Trial vectors: the test holds if and only if some unit vector phi has <phi, P_0 T^w phi>^2 >= (21/25) Tr (P_0 T^(2w)); two-period form Z_+(2w)^2/Z_+(4w) | Lemma TP of row 1342 (`gap-seed-audit-fable.md` L159); row 1165 (19) (the trial vector there is the square root of the slice marginal) | on file |
| Hellinger or total-variation independence of the two opposite slices of the periodic torus gives the neutral count; local readings on collars suffice | row 1165, `gap-solve11-astra62.md` (19)-(21), L286-316 ("The same upper bound 1/32 with H = G gives the periodic neutral excited count s(u) <= 1/2"); mutual information also suffices there | on file, PROVED there; its check is row 1166 (`gap-solve11-check-opus.md`) |
| Gap plus count: the operator-norm form of the test (gap of the cube in units of 1/L above 256 D_0 + 30) together with a bounded torus excess | Theorem ZD-c and Corollary Z4, `gap-phys-seed.md` L311-322 (row 720); Lemma G5 of row 895 | on file |
| Thermal pressure, rotated frames, Casimir energy of a periodic direction | Lemma Z, Lemma Z', Proposition Delta (`gap-ladder-max.md` 5.7); Lemma CD of row 1259; rows 1180 R2, 1184 route 4 | on file |
| Operator inequalities against the electric operator (min-max, Golden-Thompson) | Lemma R4 of row 1180 (`gap-mini-neutral-fable.md` L208); `gap-constraints-max.md` B6 | on file: loses the vacuum energy |
| The vacuum chain is the electric product channel tilted by a positive function; link refresh | row 1135 (link-refresh model), row 1132 statement (A), row 1207 Theorem 2.3 (`gap-agy-solve2-argon.md` L104) | on file |
| Coupling integration, monotones, rigidity, thin twisted tori, Bakry-Emery curvature | rows 1180 R3, R5-R9; row 1184 routes 3, 6, 8, 9 | on file |

Two items had no match and are used below.

- The sharp constant of the rank-one test (Section 2, Lemma M1). `grep` for "Mirsky": 0 files; "Eckart": 1 file
  (`gap-solve32-check-opus.md` L310, about another operator); "4/21": no relevant hit. It changes a constant only.
- Lipschitz transport with comparison of ALL eigenvalues (E. Milman's observation). `grep` for "Milman": 3 files,
  all saying "not tried" (`gap-transport-check.md` L183, row 682; `gap-afield-a-max.md` L188 and L341, row 1031,
  item F6: "not tried, needs a bounded perturbation; blind"; `gap-target-max.md` L156, row 913). "Caffarelli", "Brenier",
  "curvature-dimension": 0 files. Section 3 takes this route, because it is the one tool I know that gives the
  gap and the count together, in the law of the model, with no supremum over boundary values.

Credits. K. Wilson (the action and the transfer operator); K. Osterwalder and E. Seiler, M. Luscher (transfer
operator, reflection positivity); T. Balaban; E. Sussman and L. Alpoge with Claude and Codex as authors of their
text (the account, the trajectory); G. 't Hooft, G. Mack and V. Petkova (twists, flux sectors, centre split);
L. Mirsky and C. Eckart, G. Young (singular value inequalities); E. Milman (eigenvalue comparison under
contracting maps), L. Caffarelli, Y.-H. Kim and E. Milman, D. Mikulincer and Y. Shenfeld (Lipschitz transport
maps); M. Luscher (trivializing maps). In this lane: gpt-6.2-astra (rows 1161, 1165: the neutral consumer and the
Hellinger test); Claude Opus 5.5 (Identity I1); Claude Fable 5.2 (rows 1180, 1184, 1342, 1353).

## 2. The target with its sharp constant (written 06:42Z, `date -u`)

Notation as in row 1353, 6.1: n^3 is the spatial box, T the Wilson transfer operator on L^2 of the slice
configurations (Haar measure, gauge-invariant functions), P_0 the mean of the eight centre translations,
lambda_0 the vacuum eigenvalue, x_a = lambda_a/lambda_0 the relative neutral eigenvalues (a >= 1), and
s(u) = sum over a >= 1 of x_a^u. Norms of operators are Hilbert-Schmidt norms.

(M-neutral), from row 1353 6.3: there are an admissible L and, for all late j, an integer w_j <= n_j/1024, a unit
vector phi_j and c_j > 0 with norm(P_0 T_j^(w_j)/c_j - |phi_j><phi_j|) <= 2/5.

### 2.1 Lemma M1 (the exact distance to rank one; PROVED, elementary)

Let B be a positive semi-definite Hilbert-Schmidt operator, B not 0, with eigenvalues mu_0 >= mu_1 >= ... >= 0, and
put sigma = sum over i >= 1 of (mu_i/mu_0)^2. Then

    min over c > 0 and over operators Q of rank one with norm(Q) = 1 of norm(B/c - Q)^2  =  sigma/(1 + sigma).

The minimum is attained at Q = the projection on a top eigenvector and c = Tr B^2/mu_0. Equivalently

    sup over unit vectors phi of <phi, B phi>^2 / Tr B^2  =  1/(1 + sigma).

Proof. For Q of rank one with Hilbert-Schmidt norm 1 the trace norm of Q is 1, so abs(Tr Q* B) <= mu_0. With
t = 1/c: norm(tB - Q)^2 = t^2 Tr B^2 - 2 t Re Tr Q* B + 1 >= t^2 Tr B^2 - 2 t mu_0 + 1 >= 1 - mu_0^2/Tr B^2, and
Tr B^2 = mu_0^2 (1 + sigma). Both inequalities are equalities for Q = |phi_0><phi_0| and t = mu_0/Tr B^2. For the
second display take Q = |phi><phi|: the minimum over t of norm(tB - Q)^2 is 1 - <phi, B phi>^2/Tr B^2. QED

This is the case k = 1 of the theorem of C. Eckart and G. Young, with the free scale c added.

### 2.2 Corollary M2 (PROVED from Lemma M1)

For B = P_0 T^w: sigma = s(2w). So, for one box, one integer w >= 1 and one tolerance delta in (0, 1):

- (i) the rank-one test at tolerance delta holds at the time w if and only if s(2w) <= delta^2/(1 - delta^2). For
  delta = 2/5 this is s(2w) <= 4/21. Row 1353, Corollary BT2 (i), has the weaker bound 4/9.
- (ii) Hence (M-neutral) gives (N-phys) with u_j = 2 w_j and the margin 4/21 in place of 1/2, with no loss in the
  time. In the other direction, s(u) <= 1/2 gives s(3u) <= 1/8 < 4/21, so the test holds at any integer time
  w >= 3u/2.
- (iii) The threshold of the test is 1/sqrt 2. If the test holds at a time w with a tolerance delta < 1/sqrt 2,
  then q := delta^2/(1 - delta^2) < 1, the neutral gap obeys x_1^(2w) <= q, and the test at tolerance 2/5 holds at
  every time k w with q^k <= 4/21, because s(2kw) <= s(2w)^k (a sum of non-negative terms; Lemma N1 of row 1184).
  At delta = 1/sqrt 2 the test proves nothing in the class of positive operators: a projection of rank two has
  sigma = 1 and distance exactly 1/sqrt 2 from rank one, and it has no gap.
- (iv) The test is a statement about two numbers. With Z_+(t) = Tr (P_0 T^t): the test at tolerance delta holds
  at w if and only if lambda_0^(2w) >= (1 - delta^2) Z_+(2w). So a proof needs an upper bound U >= Z_+(2w) and a
  lower bound <phi, P_0 T^w phi> >= l for one unit vector phi, with l^2 >= (1 - delta^2) U. For delta = 2/5 the two
  bounds together may lose the factor 25/21 in total, on a lattice of 2 w n^3 >= 2^270 sites.

Item (iv) is the two-period form on file (Lemma TP of row 1342) with a trial vector in place of the second
period; row 1165 (19) uses the square root of the slice marginal as the trial vector. I state it because it fixes
the choice of attack in Section 3.

## 3. How best to attack it (written 06:42Z, `date -u`; ARGUED, except where a proof is cited)

1. What the record says. (M-neutral) is the crux of the gap lane. Rows 1180, 1184 and 1353 list about 25 routes
   with their first failing steps, and rows 1188-1259 found that further blind lists return items on file. The
   forms I derived again in this session are all in the table of Section 1. So this row does not make a list.
2. What kind of statement it is. By Corollary M2 (iv) the test compares two partition functions of more than
   2^270 sites up to a total factor 25/21. A bound that loses any fixed factor per site, or per unit of
   boundary, is useless. This is on file as Proposition FR of row 1332 (tolerance of order 1/volume per site)
   and as Lemma R4 of row 1180 (an operator comparison on L^2 of Haar measure loses the vacuum energy). A proof
   must therefore use a relation that is exact at rank one. I know three kinds.
   - (a) Convexity and reflection positivity of the masses themselves. This is the engine (Theorem S, Theorem
     ZD-c). It needs a seed, and (M-neutral) is the seed.
   - (b) A convergent expansion whose leading term is the same on both sides. This is the chain of block steps
     into an end class (rows 1332-1353). Its open step is the block step at order-one coupling.
   - (c) A comparison made in the ground-state representation, where the vacuum is the constant function on both
     sides and no vacuum energy appears. Two tools of this kind exist: comparison of Dirichlet forms under a map
     (a transport map), and a coupling of the two slices (total variation). Both are statements in the law of
     the model, with no supremum over boundary values.
3. Choice. Kinds (a) and (b) are owned by the chain rows and by row 1353. Kind (c) has one executed consumer on
   file, the Hellinger test of row 1165 (19)-(21), and one consumer for the gap alone, statement (A) of row 1132
   (a minorization in Moser coordinates). The transport tool that gives all eigenvalues, hence the count and the
   gap together, is recorded as "not tried" (Section 1). So I attack through (c), in three ways:
   - Way 1 (Section 4): a Lipschitz transport map and the comparison of all eigenvalues.
   - Way 2 (Section 5): a coding of the periodic law by independent variables, fed to the test of row 1165.
   - Way 3 (Section 6): the same comparison for the Wilson transfer operator itself, which has discrete time.
   For each I prove the consumer and then look for the supplier. Each section ends with its first failing step.
4. What would count as success. A supplier that is a finite statement, or a statement that the account's
   first-passage data can be shown to satisfy. Anything else is a restatement of the crux, and I say so.

## 4. Way 1: a transport map and the comparison of all eigenvalues (written 06:47Z, `date -u`)

On file before this section. Transport maps for functional inequalities: route B1 of row 669
(`gap-skeleton-max.md` L366-369, L401: a trivializing map along the coupling for the four-dimensional measure;
verdict there "pointwise (T) fails in a solvable model; (T-avg) is the conclusion"); row 682
(`gap-transport-check.md` L183: the Lipschitz results of Kim and Milman and of Mikulincer and Shenfeld "not
tried"); item F6 of row 1031. Moser's map onto the vacuum law and a minorization in those coordinates: statement
(A) of row 1132 (`gap-council-op-astra.md`, "Choice of coordinates" and "First statement (A)"), with a consumer for
the gap. Vacuum log-Sobolev and hypercontractivity: rows 940, 941. What I did not find: a map onto the vacuum
law of a slice used for ALL eigenvalues, which gives the count. That is this section.

### 4.1 Proposition TR (PROVED; the observation is E. Milman's, for contracting maps)

Let nu and gamma be probability measures on spaces X and Y. Let q_nu be a non-negative quadratic form on a dense
subspace D_nu of L^2(nu), and q_gamma on D_gamma in L^2(gamma). For k >= 0 put

    kappa_k(q) = inf over subspaces V of the domain with dim V = k + 1 of  sup { q(f) : f in V, norm(f) = 1 }.

Let S: Y -> X be measurable with S_* gamma = nu, and let L > 0 be such that, for every f in D_nu, the function
f o S lies in D_gamma and q_gamma(f o S) <= L^2 q_nu(f). Then kappa_k(q_nu) >= kappa_k(q_gamma)/L^2 for every k.

If a group Gamma acts on X and on Y by measure-preserving maps that keep the domains and the forms, and S
commutes with the two actions, the same inequality holds for the numbers kappa_k^Gamma defined with
Gamma-invariant functions only.

Proof. J f = f o S is linear and norm(J f) in L^2(gamma) equals norm(f) in L^2(nu), because S_* gamma = nu. So J is
injective, and J V has dimension k + 1 when V has. For such V in D_nu: sup over unit f in V of q_nu(f) >=
L^(-2) sup over unit g in J V of q_gamma(g) >= kappa_k(q_gamma)/L^2. Take the infimum over V. If S is equivariant,
J maps invariant functions to invariant functions. QED

When q is closable and its operator G has compact resolvent, the kappa_k are the eigenvalues of G counted with
multiplicity (min-max principle). Then Tr e^(-t G_nu) <= Tr e^(-(t/L^2) G_gamma) for every t > 0. The comparison
is tight at the bottom when both forms vanish on the constants: both sides have kappa_0 = 0. No vacuum energy
enters. This is the property that Section 3 asks for.

### 4.2 Setting H: the lattice theory with continuous time

X = SU(2)^E, E the 3 n^3 links of the periodic box, n >= 4, with the product of the metrics of the unit
three-sphere and Haar probability measure dA. Gamma is the group generated by the vertex gauge transformations
and the eight centre translations; it acts by isometries. For b > 0 and a smooth real Gamma-invariant function V
on X put H = -(1/(2b)) Laplacian + V on L^2(dA). The Hamiltonian of Kogut and Susskind has this form (V a
multiple of the sum of 1 - x_p over the spatial plaquettes); the constants play no part below.

Facts used (standard; PROVED in outline, each step is textbook). H is bounded below with compact resolvent. The
kernel of e^(-tH) is smooth and strictly positive (Feynman-Kac on a compact connected manifold). So the lowest
eigenvalue E_0 is simple, with a smooth strictly positive eigenfunction Omega, and Omega is Gamma-invariant. Put
nu = Omega^2 dA. For smooth f,

    <Omega f, (H - E_0) Omega f>  =  (1/(2b)) integral of |grad f|^2 d nu   =: q_nu(f),

because (H - E_0)(Omega f) = -(1/(2b)) (Omega Laplacian f + 2 grad Omega . grad f) and
Omega^2 Laplacian f + 2 Omega grad Omega . grad f = div(Omega^2 grad f). The map f -> Omega f is unitary from
L^2(nu) onto L^2(dA) and keeps the smooth functions, a core. So the eigenvalues of H - E_0 on the Gamma-invariant
functions are the numbers kappa_k^Gamma(q_nu), with D_nu the smooth functions.

Reference: gamma = dA and q_gamma(g) = (1/(2b)) integral of |grad g|^2 dA on Lipschitz functions. By the theorem
of Peter and Weyl its eigenvalues are (1/(2b)) sum over links of (d_l^2 - 1), d_l in {1, 2, 3, ...}, with
multiplicity prod d_l^2 (the Laplace eigenvalue of spin j on the unit sphere is -4j(j+1) = 1 - d^2, d = 2j + 1;
row 1132's file uses the same normalization).

### 4.3 Corollary TR1 (PROVED from Proposition TR)

In Setting H let S: X -> X be Gamma-equivariant, Lipschitz with constant L for the product metric, with
S_* dA = nu. Let E_0 < E_1 <= E_2 <= ... be the eigenvalues of H on the Gamma-invariant functions. Then

- (i) E_1 - E_0 >= 6/(b L^2);
- (ii) for t > 0: sum over a >= 1 of e^(-t (E_a - E_0)) <= (1 + theta(t/L^2))^(3 n^3) - 1, where
  theta(tau) = sum over d >= 2 of d^2 e^(-tau (d^2 - 1)/(2b));
- (iii) the rank-one test at tolerance 2/5 holds for e^(-tH) on the Gamma-invariant functions at every time
  t >= b L^2 (log n + 1.49).

Proof. For smooth f, f o S is Lipschitz, S is differentiable almost everywhere with operator norm of its
derivative at most L (Rademacher), and |grad (f o S)| <= L |grad f| o S almost everywhere. So
q_gamma(f o S) <= L^2 integral of |grad f|^2 o S dA = L^2 q_nu(f). Proposition TR applies in the invariant
sector. (i) A non-constant Gamma-invariant eigenfunction of the reference has at least four links with d_l >= 2:
at a vertex with exactly one such link the product of the representations has no invariant vector, so the set
of these links has no vertex of degree one, and a non-empty such set in the periodic cubic lattice with n >= 4
has at least 4 links. Each such link adds at least 3/(2b). (ii) The invariant trace of the reference is at most
its trace on all of L^2, which is (1 + theta)^(3 n^3); the terms k = 0 are 1 on both sides. (iii) For
tau >= b: theta(tau) <= 4 e^(-3 tau/(2b)) (1 + (9/4) e^(-5/2) + 4 e^(-6) + ...) <= 5 e^(-3 tau/(2b)). By
Corollary M2 (i) the test at t needs the sum of (ii) at 2t to be at most 4/21. It is at most
exp(15 n^3 e^(-3t/(b L^2))) - 1, and 15 n^3 e^(-3t/(b L^2)) <= log(25/21) = 0.1743... when
t >= (b L^2/3)(3 log n + 4.46). Then also 2t/L^2 >= b. QED

Reading. At one fixed b, a Lipschitz constant that is uniform in the volume gives the gap and the count at
once, and the test holds at t <= n/1024 as soon as n/(log n + 1.49) >= 1024 b L^2. The constant may even grow
with the box, up to L^2 = n/(1024 b (log n + 1.49)).

### 4.4 Lemma UVC (PROVED; the Haar reference cannot serve all late cutoffs at one physical size)

Suppose that, along a sequence of data with n_j -> infinity, Corollary TR1 (iii) gives the test at times
t_j <= n_j/1024. Then n_j (E_1 - E_0)_j >= 6144 (log n_j + 1.49), which tends to infinity.

Proof. The hypothesis is b_j L_j^2 (log n_j + 1.49) <= t_j <= n_j/1024. By (i), E_1 - E_0 >= 6/(b_j L_j^2) >=
6144 (log n_j + 1.49)/n_j. QED

So on a trajectory where the gap of the box of one physical side L stays bounded in units of 1/L as the cutoff
is removed (z^+(L) finite; every massive or massless continuum theory has this), the route through TR1 fails
for late j. The reason is in (ii): the reference counts the lattice modes, 3 n_j^3 of them, and the true count
is physical. A reference with a physical count is needed.

### 4.5 Corollary TR2 (PROVED from Proposition TR; a reference with a physical count)

Cut the box into N = (n/l)^3 cubes of side l, and split E into the sets E_c of the links that start in the cube c.
On X_c = SU(2)^(E_c) take any Hamiltonian H_c = -(1/(2b)) Laplacian + V_c with V_c smooth, its vacuum measure
nu_c, and its excited trace on all of L^2(X_c): s_c(tau) = sum over k >= 1 of e^(-tau eps_k), eps_k the eigenvalues
of H_c above its lowest one. Let S from the product of the X_c to X be Lipschitz with constant L for the product
metric, with S_* (product of the nu_c) = nu. Then, on the Gamma-invariant functions,

    sum over a >= 1 of e^(-t (E_a - E_0))  <=  prod over c of (1 + s_c(t/L^2))  -  1      for every t > 0.

So the rank-one test at tolerance 2/5 holds at the time t when the sum over c of s_c(2t/L^2) is at most
log(25/21).

Proof. Proposition TR without a group, with q_gamma the sum of the forms of the cubes; its operator is the sum
of the commuting operators H_c - E_0(H_c) on the product space, and its trace is the product of the traces of
the cubes. The eigenvalues of H - E_0 on invariant functions are among those on all of L^2(nu). QED

Reading (ARGUED). If the cubes have a gap eps_1 and a count s_c(tau_0) <= K at one time tau_0, both in physical
units and uniform in the cutoff, the test at a physical time t follows from
L^2 <= 2t/(tau_0 + (log N + log K + 1.75)/eps_1). The number of cubes N = (L_phys/l_phys)^3 is physical. So the
gluing map may have a Lipschitz constant that grows like the square root of t/tau_0, up to the logarithm. I
call the hypothesis (GLUE-LIP). It is the lane's glue lemma in transport form (rows 895, 920).

### 4.6 Supplier, tests, and the first failing step

- Tests (PROVED from Corollary TR1 (i)). The hypothesis fails where it must. A model whose box has a gap of order
  1/n (compact U(1) at weak coupling, or a product with a massless factor, restricted to functions of that
  factor) admits no map with L^2 = o(n). So the hypothesis is selective through its constant only. It is of the
  kind (K-one) of lead rule W2: a property of the measure at one scale with a number in it.
- Supplier (from memory, NOT read in this session; the lane's notes are row 669 L368-369 and row 682 L183).
  The known Lipschitz maps come from convexity: Caffarelli (a uniformly log-concave target on a Euclidean
  space), Kim and Milman (the heat flow), Mikulincer and Shenfeld, and Shenfeld (the Polchinski flow under the
  multiscale Bakry-Emery condition). On file for the vacuum measure: the pointwise curvature condition fails
  above beta = 1, the mid-slice form above 2, the both-neighbours form above 3/2 (row 941), and the multiscale
  form did not close at the window (rows 957, 968). So no convexity supplier reaches a coupling of order one.
- The vacuum measure is not explicit. Row 941 gives log Omega = -V/2 + Lambda(beta x) - const with Lambda convex
  for the Wilson chain without gauge projection. I found no way to build a map from that form.
- First failing step of Way 1. A Lipschitz bound, uniform in the volume, for one equivariant map onto the vacuum
  measure at one coupling of order one; or (GLUE-LIP) along the trajectory. Neither is a finite statement, and
  neither is implied by anything on file. With it, Setting H would have the test. Setting H is not the Wilson
  transfer operator; Section 6 treats that difference.

### 4.7 Lemma VOL (PROVED; a floor for the Lipschitz constant of any map from Haar measure)

Let X be a compact connected Riemannian manifold of dimension d with normalized volume dA, nu a probability
measure with full support, and S: X -> X Lipschitz with constant L and S_* dA = nu. Then S is onto, and
L^d >= vol(C)/nu(C) for every Borel set C with nu(C) > 0. In particular L >= 1, and
L^d >= 1/(essential infimum of d nu/dA).

Proof. S(X) is compact and nu(S(X)) = 1, so S(X) contains the support of nu, which is X. For a Borel set C,
C = S(S^(-1) C), and a map with Lipschitz constant L multiplies d-dimensional volume by at most L^d. So
vol(C) <= L^d vol(S^(-1) C) = L^d nu(C). QED

Reading (ARGUED; the size is an estimate, not a proof). For the vacuum measure of a box, d = 9 n^3, and the
density Omega^2 at the slices whose plaquettes are all near -1 is smaller than its mean by a factor
exp(-c beta n^3) with c of order one (such slices exist for even n; their weight can be bounded by the chessboard
estimate in the time direction). So L >= exp(c beta/9 - C): a map from Haar measure has a Lipschitz constant
that grows exponentially in the bare coupling. Together with Lemma UVC this makes Corollary TR1 a tool for one
coupling of order one. Along the trajectory the reference must be local in scale, as in Corollary TR2.

## 5. Way 2: a coding by independent variables, fed to the Hellinger test (written 06:50Z, `date -u`)

On file before this section. The consumer: row 1165 (19), `gap-solve11-astra62.md` L283-292 (check row 1166, S1:
HOLDS). It reads: on the ordinary periodic Wilson cylinder of even period u = 2t, let P_G be the law of the two
opposite slices, each taken modulo gauge and modulo the eight centre flips, rho_G its marginal, and
d_G = norm(sqrt(dP_G) - sqrt(d(rho_G x rho_G))) in L^2. Then 1 + s(u) <= (h_8 - d_G)^(-2) with
h_8 = 2 x 8^(-1/4)/(1 + 8^(-1/2)) = 0.8786..., so d_G < 1/32 gives s(u) <= 1/2. Couplings and disagreement
percolation: 21 lane files name them, all for conditions uniform in the boundary values; criteria in the law
for pinned cells are method 34 (`parts/gap.md`, rows 1115-1122). What I did not find: the statement that a coding
of the periodic law gives the test. `grep` for "finitary" and "factor of i.i.d": 0 files; "coding radius": 2 files.

### 5.1 Proposition COD (PROVED; the method is standard, van den Berg and Steif, Spinka)

Let Lambda be the torus (Z/u) x (Z/n)^3 with u = 2t, V its sites, and mu the periodic Wilson measure on its
links. A coding of mu is a family xi = (xi_v), v in V, of independent random variables and a measurable map F
with F(xi) distributed as mu. For a set A of links and r >= 0 let N_r(A) be the set of sites within lattice
distance r of an end of a link of A. Let xi' be an independent copy of xi and let xi^(A,r) equal xi on N_r(A) and
xi' elsewhere. The resampling defect is

    delta(A, r) = Prob( F(xi) and F(xi^(A,r)) differ on some link of A ).

- (a) If A and B are sets of links with N_r(A) and N_r(B) disjoint, the total variation distance between the
  law of (U_A, U_B) under mu and the product of its two marginals is at most delta(A, r) + delta(B, r).
- (b) Let A and B be the sets of spatial links at the times 0 and t, and r = ceil(t/2) - 1. If
  delta(A, r) <= 1/4096 and delta(B, r) <= 1/4096, then d_G <= 1/32, and row 1165 (19) gives
  1 + s(2t) <= (0.8786 - 0.0313)^(-2) < 1.40, so s(2t) <= 1/2: the neutral seed of (N-phys) at u = 2t when
  2t <= n/512, and by Corollary M2 (ii) the rank-one test at tolerance 2/5 at the time 3t.

Proof. (a) Take three independent copies xi, xi', xi''. Put eta = xi on N_r(A) and xi' elsewhere, and zeta = xi
on N_r(B) and xi'' elsewhere. The two neighbourhoods are disjoint and the variables are independent over the
sites, so eta and zeta are independent and each has the law of xi. Hence (F(eta)_A, F(zeta)_B) has the product
of the marginals as its law. It differs from (F(xi)_A, F(xi)_B) with probability at most
delta(A, r) + delta(B, r). (b) The two time neighbourhoods are disjoint because 2r < t on a circle of length 2t.
By (a) the total variation distance is at most 1/2048. The quotients by gauge and centre act on each slice
separately, so they do not increase it. For probability densities p, q: the integral of sqrt(pq) is at least
the integral of min(p, q) = 1 - TV, so d^2 = 2 (1 - integral of sqrt(pq)) <= 2 TV <= 1/1024. Then row 1165 (19)
with H = G. QED

If F has coding radii R_l (F(xi)_l is fixed by xi on N_(R_l)(l)), then delta(A, r) is at most the sum over the
links l of A of Prob(R_l > r).

### 5.2 Supplier, and the first failing step

- At beta = 0 the links are independent and delta = 0. At small beta a coding with exponential tails follows
  from the heat-bath dynamics run from the past with a bounding chain, in the Dobrushin range (ARGUED; the
  method is that of Propp and Wilson and of Haggstrom and Steif; I did not write it). That range ends below
  about beta = 1 (the hand ceilings of the lane, `gap-status-1113.md` L31, L65, L110-112). Nothing new comes out of
  it: the seed is on file there.
- At a coupling of order one a coding needs a coupling of two copies that agree, link by link, outside a
  disagreement set with summable tails, in the law of the model. The single-link conditional laws under two
  different staples are far apart in total variation at beta = 2.3 (the staple sum has norm up to 6 beta), so
  the percolation of disagreement is not subcritical by any one-link bound. Block versions are suprema over
  surroundings, and those fail above the threshold of Frohlich, Simon and Spencer (Proposition CA-FAIL,
  `gap-bridge-exercise-opus.md` L337, row 1072; layer form above 1.0109, `gap-status-1113.md` L112) or are not finite within the budget
  (Lemma DIM-B, `gap-blockstep-fable.md` L276, row 1340).
- Along the trajectory the tails must also be right in the ultraviolet: with n_j^3 links in a slice at a fixed
  physical time t, the sum of the tails is small only if Prob(R_l > r) falls at least like (a_j/r)^3 between
  the lattice scale and the physical scale. A coding with one exponential rate in lattice units fails for late
  j, for the same reason as Lemma UVC.
- First failing step of Way 2. A coding of the periodic law with summable tails at one coupling of order one.
  It is a statement in the law of the model and it is not finite. It implies the mixing statements that method
  34 could not supply.

### 4.8 Two controls of Way 1 (added 06:52Z, `date -u`)

**Lemma GAUSS (PROVED; the hypothesis of Corollary TR2 holds with L = 1 for a free massive field).** On a finite
periodic lattice let H = (1/2) sum of pi_x^2 + (1/2) <phi, A phi> with A = -Laplacian + m^2, m > 0. Its vacuum
measure is the Gaussian measure with covariance Sigma = (1/2) A^(-1/2). Cut the lattice into blocks and let A_ref
be A without the bonds that join different blocks. Then A >= A_ref >= m^2, so A^(1/2) >= A_ref^(1/2) and
Sigma <= Sigma_ref = (1/2) A_ref^(-1/2) (the square root is operator monotone and the inverse reverses the
order). The reference measure is the product of the vacuum measures of the blocks. The linear map
S = Sigma^(1/2) Sigma_ref^(-1/2) sends it to the vacuum measure of H, and
norm(S)^2 = norm(Sigma_ref^(-1/2) Sigma Sigma_ref^(-1/2)) <= 1. So S is a contraction, and Proposition TR gives
kappa_k(H) >= kappa_k(sum of the block Hamiltonians) for every k. QED

So the hypothesis is not empty: for a free field with a mass the gluing map is a contraction, the block gap is
at least m, and the block count is physical. For m = 0 the constant mode of a block has no gap and the count
of the reference is infinite, as it must be. For the gauge theory the same construction drops the plaquettes
that join the cubes. There the map cannot be a contraction: by Proposition TR its constant satisfies
L^2 >= eps_1/(E_1 - E_0), and the small-volume gap eps_1 of a cube is far above the gap of the box.

**GUIDE (one link; a control of the normalizations of 4.2 and 4.3, not a proof).** For one copy of the
three-sphere, nu proportional to exp(b x) dA, and the radial monotone map S, I computed the first ten
eigenvalues kappa_k of the form of nu on class functions and the Lipschitz constant L. Criterion written before
the run: kappa_k L^2/(k(k + 2)) >= 1 for k = 1, ..., 10. Result: the minimum over k is 1.43 at b = 0.5 (L = 1.195),
6.96 at b = 2.3 (L = 2.630) and 130 at b = 5 (L = 11.25). No violation. The value of L agrees with the hand
formula L^3 = 2 I_1(b) e^b/b at the antipode (2.63 at b = 2.3). The run took one second under the numeric lock
(holder row1356-mneutral, acquired and released; memory 66 percent free), plain floating point, script
`tr_check.py` kept in the worker's scratch folder, not in the repository. It can refute a normalization. It
proves nothing.

## 6. Way 3: the same comparison for the Wilson transfer operator (written 06:52Z, `date -u`)

(M-neutral) is about the Wilson operator, which has discrete time. Setting W: T = M C M on the Gamma-invariant
functions of L^2(dA), M the multiplication by exp((beta/2) sum of x_p over the spatial plaquettes), C the product
over the links of the convolution with the density e^(beta x)/A(beta), with eigenvalue
c_j = I_(2j+1)(beta)/I_1(beta) on spin j (the form T = M C_E P M of row 1132; outline GL3-GL4). Omega is the
vacuum, nu = Omega^2 dA, P f = T(Omega f)/(lambda_0 Omega) the vacuum chain, and
pi(dA, dB) = Omega(A) K_1(A, B) Omega(B) dA dB/lambda_0 its edge measure, with both marginals nu. Then
<f, (1 - P) f> in L^2(nu) equals (1/2) integral of (f(A) - f(B))^2 pi(dA, dB), and the eigenvalues of 1 - P on the
invariant functions are 1 - x_k.

### 6.1 Lemma JF (PROVED from Proposition TR; a case of statement (A) of row 1132)

Let E(A, dB) be the kernel of C. Let S: X -> X be measurable and Gamma-equivariant with S_* dA = nu, and let L be
such that the image of the measure dA E(A, dB) under S x S is at most L^2 pi on the complement of the diagonal.
Let 1 = e_0 > e_1 >= e_2 >= ... be the eigenvalues of C on the invariant functions. Then 1 - x_k >= (1 - e_k)/L^2
for every k. In particular x_1 <= 1 - (1 - c_*)/L^2 with c_* = (I_2(beta)/I_1(beta))^4, the largest e_k with k >= 1
(four links of spin 1/2, as in Corollary TR1 (i)).

Proof. For f in L^2(nu): <f o S, (1 - C) f o S> in L^2(dA) is (1/2) the integral of (f(A) - f(B))^2 against the
image measure, and the integrand vanishes on the diagonal. So it is at most L^2 <f, (1 - P) f>. Proposition TR
with these two bounded forms. QED

In the coordinates S^(-1) the hypothesis says that the one-step transition density of the vacuum chain
dominates L^(-2) times the electric step. Statement (A) of row 1132 is this with k steps, commutator kicks in
place of C and one more kernel; its consumer for (Z-UNB) is proved there. So Lemma JF adds no new hypothesis.

### 6.2 The jump form gives no count (PROVED by an example)

Take nu = dA, S the identity and P' = L^(-2) C + (1 - L^(-2)) Id with L > 1. P' is a positive Markov operator,
symmetric for dA, and it satisfies the hypothesis of Lemma JF with equality. Its eigenvalues are
1 - (1 - e_k)/L^2 >= 1 - L^(-2) for all k, so Tr P'^(2w) is infinite for every w. So no hypothesis of the kind of
Lemma JF, and no minorization of the kind (A), can by itself bound the excited trace. For the Wilson operator
the count has to come from another statement. On file it comes from the engine: Theorem ZD-c needs the bounded
torus excess (BDD-Delta) beside the gap in units of the inverse side.

### 6.3 Why Way 1 does not transfer to discrete time (ARGUED; each inequality is on file)

- C is a mixture of heat kernels: c_j = integral of e^(-(d^2 - 1) tau/2) against a probability measure in tau,
  by the Hartman-Watson law (on file: `gap-tu-retry.md` L477). So 1 - C <= (mean of tau/2)(-Laplacian) on each
  link. This bounds the jump form from ABOVE by the gradient form. The comparison of Way 1 needs it from below,
  and from below it holds only on low modes.
- Between T = e^(-V/2) e^(-K) e^(-V/2) and e^(-(K+V)) the known relations are the Golden-Thompson inequality and
  Araki's log-majorization. They bound products of the top eigenvalues of T from below. They give no upper
  bound on the ratios x_k. On file: `gap-constraints-max.md` B6; Lemma R4 of row 1180.
- First failing step of Way 3. A comparison between the Wilson operator and a generator with continuous time
  that is tight at the vacuum. I found none. Without it Way 1 proves the test for Setting H only, and for the
  Wilson operator the three ways give the gap alone, through hypotheses of the kind (A).
