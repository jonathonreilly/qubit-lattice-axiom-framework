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
