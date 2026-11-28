lead: anthropic/claude-fable-5-2/max laptop-subagent

# FINISH row 1281, `gap-laptop-solve3-fable`: the mass gap of 4D SU(2) Yang-Mills

Status of this file: complete for this run. Each step below was appended when it was done.
Labels: PROVED (a complete argument is written here or in a named checked file),
ARGUED (an argument with a named missing step), GUIDE (numeric or heuristic, never a
proof step), OPEN (not established).

## Step 0. File created

- Created before any reading. Nothing is established yet.
- Next: read `parts/gap.md`, the `library/` index and the FINISH.md RESULT lines on the
  gap, then choose the attack.

## Step 1. What was read (statements about the record, not mine)

Row 1281, Claude Fable 5.2 (max), laptop subagent, 2026-11-20. Author only; checked by no one.

- `parts/gap.md` L1-104 (formulation, the wall (W), the blockage sentence, methods 19-36, lead rules CL and W2).
- `library/gap-laptop-solve-fable.md` (row 1217) and `library/gap-laptop-solve2-fable.md` (row 1269) in full.
  They are the same seat. Row 1217 chose shape inequalities from reflection positivity. Row 1269 chose a
  one-sided scale-monotone inequality for a response (the form of the two-dimensional O(4) proof) and took
  nine openings to a first failing step. I do not repeat either.
- RESULT lines of rows 1179-1216 and 1249-1276, read from `FINISH.md`.
- `library/gap-skeleton-final.md` Sections 0-4 (Routes T and Z, the filters).
- `library/prior/gap-o4-pinned-cell-read-opus.md` Steps 1-3 (the reading of OpenAI's O(4) stiffness
  iteration, to its Section 3.12).
- Not read: the proofs behind rows 720, 1161, 1179, 1180 (the reduction of the gap clause to (N-phys) and
  the continuum datum); the account of Sussman and Alpoge; the OpenAI papers themselves.

The record's own summary, which I do not re-derive. The Jaffe-Witten gap clause is reduced to (i) the
continuum datum (existence is not proved) and (ii) one infrared input at order-one effective coupling, in
the forms (W), (N-phys), (SEED), (SL)/(RR). By row 1180, (N-phys) is a finite one-cube seed size at every
fine coupling with a bound of asymptotic-scaling type. No row holds a mechanism for (ii). Rows 1188-1275
are about twenty plain-brief runs; each found the same map.

## Step 2. How best to attack it (GUIDE unless marked)

### 2.1 The choice

Two regimes are closed by known methods. Strong coupling: the cluster expansion (Osterwalder and Seiler).
The ultraviolet: Balaban's renormalization group, which the lane ports through the account of Sussman and
Alpoge. A proof must join them across a band where the effective coupling is of order one. I see three
kinds of joint.

- (a) A number at one coupling in the band. By hand this needs a convergent expansion. None reaches the
  window beta = 2.3 to 2.6: there the character ratio I_2(beta)/I_1(beta) is about 0.5.
- (b) A statement along scales at one coupling (the form of the two-dimensional O(4) proof). Row 1269
  took this and stopped at the frame term.
- (c) A statement along the coupling at fixed lattice sizes: a continuity argument in beta that starts at
  the strong-coupling side.

I took (c), and I worked it out before I searched the record for it. Reasons: the start is a theorem (the
strong-coupling seed; on file as Theorem DOB of row 708, checked in row 709: a seed, and with Theorem SH
a gap on every periodic cube, for beta below 1/18); every finite-volume partition function is real-analytic in beta and
every thermal sum is continuous; the set of couplings with a seed is open; so the proof needs exactly one a priori estimate, which makes that set closed. Compact U(1)
must violate the estimate at its transition, so the estimate is selective by construction.

### 2.2 The a priori estimate, in the forms I derived

Notation. B is a periodic cube, T_beta its transfer operator on gauge-invariant functions, with
eigenvalues lambda_0 > lambda_1 >= ... > 0, levels E_i = log(lambda_0/lambda_i), and thermal sums
S_beta(t; B) = sum over i >= 1 of exp(-t E_i).

- (LEV) Levels. There is K such that, for beta_0 <= beta <= beta', every ordered level of every cube has
  E_i(beta') >= theta E_i(beta), with theta = exp(-K (beta' - beta)). On an analytic branch this is
  -dE_i/d beta <= K E_i. So S_beta'(t; B) <= S_beta(theta t; B) for real t with theta t >= 1: a finer lattice is no colder than the coarser one at the time
  theta t. This is a one-sided lattice Callan-Symanzik inequality.
- (ACT) Action deficit. By first-order perturbation theory -dE_i/d beta is the mean action of one time
  slab in the level i minus its mean in the vacuum. So (LEV) says: the action deficit of a level is at
  most K times its energy. With asymptotic scaling the deficit of a massive level is c_AF E_i (1 + o(1)),
  c_AF = 3 pi^2/11 (GUIDE).
- (COV) Vacuum covariance (Hamiltonian form, Lemma V of Step 3). The deficit is the covariance, in the
  vacuum measure, of the squared amplitude of the level with the total plaquette.
- (CMP) Time against coupling. In the time variable the same inequality is free: for a reflected pair,
  G(t) = <O theta_t O> is log-convex and G(2t) G(0) >= G(t)^2, so Gamma = -log G obeys
  Gamma(2t) <= 2 Gamma(t) + log G(0). (LEV) is the image of this line under an exchange of the coupling
  derivative for a scale derivative at a bounded rate. That exchange is the unproved scaling.

What (LEV) gives (PROVED GIVEN Theorem S and Lemma E of `library/gap-crux-restate.md`; the derivation is
mine, the result is on file, see 2.3). Let s = S_beta(n; (2n)^3) < 1/5041. Theorem S gives
s_j := S_beta(2^j n; (2^(j+1) n)^3) <= (5041 s)^(2^j)/5041. Lemma E, used three times per doubling of the
side at fixed time, gives 1 + S_beta(2^j n; (2^(j+r+1) n)^3) <= (1 + s_j)^(c 8^r) with
c = prod over i >= 1 of (1 - 2^(-i))^(-3) < 42. With N = 2^(j+r) n and theta = 2^(-r), (LEV) gives
S_beta'(N; (2N)^3) <= S_beta(theta N; (2N)^3) <= (1 + s_j)^(42 x 8^r) - 1, which is below 1/5041 with a
fixed margin once 2^j log(1/(5041 s)) exceeds r log 8 + log 42 + a constant, so for j = log_2 r + O(1). So a
seed at (beta, n) gives a seed at (beta + (r log 2)/K, 2^(r + log_2 r + O(1)) n), and the seed size grows no
faster than exp((1 + o(1)) K beta). With a seed at one beta_0 this is a gap on dyadic cubes at every
beta >= beta_0, at least c exp(-(1 + o(1)) K beta).

### 2.3 Place in the record (checked after the derivation)

The attack is on file, in a better form than mine.

- `library/gap-mid-max.md` (row 708; its check is row 709, in which no statement of its Sections 4 to 8
  fails): Theorem TR and
  Corollary TR1 carry the strong-coupling seed along the characteristic t(s) = t_0 exp(integral of K) under
  (VIR_K), the thermal-mean form of (LEV); (LEV_K) is my (LEV); (DEF_K) is my (ACT). Its Section 4.4 records
  three failed ways to (DEF_K): a pointwise operator inequality (the magnetic part of a level lies below
  the vacuum by about 3 times its energy, GUIDE), a relative bound from locality (the constant depends on
  the gap, so the bound ends at a finite coupling), and convexity (the class forbids it). It ends at the
  open statement (VIR-log).
- `library/gap-ladder-max.md` (row 978): A2 (the continuity ladder, crux (NO-STALL)), A3 (the lattice
  Callan-Symanzik form, crux (SUM-RULE)), Lemma LAD (the set of couplings with a seed is open; the carry
  is the statement that its component is unbounded), Lemma G (continuity alone climbs a finite distance).
- Row 1198 (the thermal flow form), row 1200 (the level flow "restates the gap"), row 1201 (the trace
  anomaly form (MONO-Delta)).

So this run adds no new route. It is one more independent recovery of route (c), by the same model
family as rows 708 and 978, and it is not independent evidence.

### 2.4 Other openings taken in thought to a first failing step (all on file in substance)

1. Soft twist arguments. A smooth twist needs a rigid frame. Left multiplication by a fixed-axis rotation
   is gauge-averaged to cos of the angle per corner (row 1269 (2.2)), so only the centre survives. A frame
   carried along a ray from the vortex core gives a measure-preserving map with no Jacobian (the rotated
   links do not carry the frame), but the frame is not flat on a two- or three-dimensional cut, and the
   bound is of area order with coefficient of order sqrt(beta) instead of beta (ARGUED). The same failure
   blocks three-dimensional SU(2), where the classical cost of a thick vortex already tends to zero; the
   soft proof of Chatterjee for three-dimensional theories uses a central U(1), which SU(2) lacks.
2. The layer form (Durhuus and Frohlich). The links that cross a cut are an O(4) model in a two-sided
   SO(4) background. The posted two-dimensional result allows one-sided twists only (as read in row
   1009). One side is trivial only if a whole slice is flat. Row 1139 has the two-sided case.
3. Thermodynamic sign. "The mean plaquette does not increase when a side is doubled" is the sign of the
   interaction measure, so it is the sign of the beta function and not a soft fact. A draft step of mine
   (Ginibre for compact U(1) by identifying periodic images) is wrong: the identified torus has coupling
   2 beta. Row 1201 has the same correction.
4. A uniform cube gap as the only input. The count of light states is a second input (row 1259, (TR)).
   The torus calculus alone cannot supply it: the function log Z = p |L| + log(sum over i of 2^(L_i)) has
   positive transfer operators in every direction (integer multiplicities 2^(L_j)), a uniform gap log 2
   and no seed, since S(n; (2n)^3) = 3 x 2^n. This is a function, not a local model (ARGUED as a remark on
   the calculus). Row 1234, Proposition LS, is a comparison-class result on the same half; I read its
   RESULT line only.
5. The gap as a flux energy. With two replicas, the ratio of the antisymmetric to the symmetric trace of
   (T x T)^t is (Z(t)^2 - Z(2t))/(Z(t)^2 + Z(2t)), and it decays like e^(-E_1 t). Two copies of SU(2) are
   a Spin(4) theory with the Dirac-spinor character as action, and the swap is the outer twist of Pin(4).
   The swap is not in the identity component, so the soft twist argument does not apply to it (swap
   forms: rows 1115-1122).
6. Operator inequalities between couplings. The Cordes inequality on antisymmetric powers gives
   sum_{i<k} log lambda_i(r beta_s, r tau) >= r sum_{i<k} log lambda_i(beta_s, tau) for r >= 1 (heat-kernel
   time weight tau, space coupling beta_s). It is Migdal-Kadanoff bond moving in the time direction as a
   majorization. Every gap bound from it carries the extensive vacuum term.

## Step 3. A fourth way to the deficit bound, and where it stops

Row 708 tried three ways to (DEF_K). I tried a fourth: write the deficit in the ground-state
representation of the time-continuum model and look for a bound from the Dirichlet form. It gives exact
identities and a square-root bound, and stops at the same place.

### 3.1 Setting (the Kogut-Susskind Hamiltonian of a periodic box)

B is a finite periodic spatial lattice with link set E. M = SU(2)^E carries the product of bi-invariant
metrics, with gradient nabla, Laplace-Beltrami operator Delta and normalised Haar measure dU.
W(U) = sum over spatial plaquettes of (1/2) tr U_p. For a, b > 0,

    H = H(a, b) = -(a/2) Delta - b W        on L^2(M, dU).

The physical line is a = 4/beta, b = beta/2, up to the normalisation of the metric.

Standard facts used (not reproved here): H is self-adjoint with compact resolvent; exp(-tH) has a strictly
positive kernel on the connected compact manifold M, so the lowest eigenvalue E_0 is simple and its
eigenfunction psi_0 can be taken strictly positive; eigenfunctions are smooth (elliptic regularity); psi_0
is gauge invariant (uniqueness); E_0 and the normalised psi_0 are real-analytic in b (W is bounded; a
simple isolated eigenvalue of an analytic family). Every statement below holds on the gauge-invariant
subspace as well, because H commutes with gauge transformations.

Put mu_0 = psi_0^2 dU (a probability measure), phi = -log psi_0, <W>_0 = integral of W d mu_0, and for
smooth f

    L f := psi_0^(-1) (H - E_0)(f psi_0) = -(a/2) Delta f + a nabla phi . nabla f.

### 3.2 Lemma V (PROVED; elementary)

(V1) For smooth f, g: integral of g (L f) d mu_0 = (a/2) integral of nabla g . nabla f d mu_0.

(V2) u := psi_0^(-1) d psi_0/db is smooth, has mu_0-mean zero, and L u = W - <W>_0.

(V3) Let psi_i = f_i psi_0 be an eigenfunction of H with eigenvalue E_i, with integral of f_i^2 d mu_0 = 1,
on an analytic branch in b, and m_i = E_i - E_0. Then m_i = (a/2) integral of |nabla f_i|^2 d mu_0 and

    - d m_i/db = Cov_(mu_0)(f_i^2, W) = integral of f_i^2 (W - <W>_0) d mu_0
               = a integral of f_i (nabla f_i . nabla u) d mu_0.

(V4) - d^2 E_0/db^2 = a integral of |nabla u|^2 d mu_0.

(V5) (d m_i/db)^2 <= 2 a m_i integral of f_i^2 |nabla u|^2 d mu_0
                  = 2 m_i ( - d^2 E_0/db^2 + a Cov_(mu_0)(f_i^2, |nabla u|^2) ).

(V6) m_i is homogeneous of degree one in (a, b). Along a = 4/beta, b = beta/2:

    - d m_i/d beta = ( m_i + 2 b Cov_(mu_0)(f_i^2, W) ) / beta.

Proof.
(V1) (H - E_0)(f psi_0) = f (H - E_0) psi_0 - (a/2)(Delta f) psi_0 - a nabla f . nabla psi_0, and
nabla psi_0 = -psi_0 nabla phi; this is the formula for L. Then integrate by parts on M, which has no
boundary: -(a/2) integral of g psi_0^2 Delta f dU = (a/2) integral of nabla(g psi_0^2) . nabla f dU
= (a/2) integral of nabla g . nabla f d mu_0 - a integral of g (nabla phi . nabla f) d mu_0. The last term
cancels the drift term of L.
(V2) Differentiate (H - E_0) psi_0 = 0 in b: (H - E_0) d psi_0/db = (W + dE_0/db) psi_0. By first-order
perturbation theory dE_0/db = -<W>_0. So (H - E_0)(u psi_0) = (W - <W>_0) psi_0, which is L u = W - <W>_0.
The right side is smooth, so d psi_0/db and u are smooth. Differentiating the norm of psi_0 gives
integral of u d mu_0 = 0.
(V3) L f_i = m_i f_i and (V1) with g = f = f_i give the formula for m_i. First-order perturbation theory
on the branch gives dE_i/db = -integral of f_i^2 W d mu_0; subtract dE_0/db. Then
integral of f_i^2 (W - <W>_0) d mu_0 = integral of f_i^2 (L u) d mu_0 = (a/2) integral of
nabla(f_i^2) . nabla u d mu_0 by (V2) and (V1).
(V4) dE_0/db = -integral of W psi_0^2 dU, so d^2 E_0/db^2 = -2 integral of W u d mu_0
= -2 integral of (W - <W>_0) u d mu_0 = -2 integral of u (L u) d mu_0 = -a integral of |nabla u|^2 d mu_0.
(V5) The Cauchy-Schwarz inequality for the pair (nabla f_i, f_i nabla u) in L^2(mu_0), then (V3) for m_i
and (V4).
(V6) H(ta, tb) = t H(a, b), so a dm_i/da + b dm_i/db = m_i. Along the line, d/d beta = -(a/beta) d/da
+ (b/beta) d/db, so dm_i/d beta = -(m_i - 2 b dm_i/db)/beta; then (V3). QED

Place in the record. The ground-state calculus is on file (the check of row 1207 names rows 863 and 895).
I searched `library/` for the Poisson form of (V2)-(V3) by its key words and did not find it; a reader
should not treat that search as complete. Lemma V has no consumer.

### 3.3 What Lemma V says (ARGUED)

- In the time-continuum model, (LEV) with the constant K is the statement

      (COV)    2 b Cov_(mu_0)(f_i^2, W) <= (K beta - 1) m_i      for every level of every cube.

  With asymptotic scaling the left side is (c beta - 1) m_i (1 + o(1)), with c the scaling constant of the
  Hamiltonian scheme. So the plaquette excess of a level is, to leading order, c times its energy.
- (COV) is a statement on eigenfunctions only. As a quadratic form on all f it is false: K L - (W - <W>_0)
  is unitarily equivalent to K (H(a, b + 1/K) - E_0(b) - E_0'(b)/K), whose lowest eigenvalue is
  K (E_0(b + 1/K) - E_0(b) - E_0'(b)/K) < 0 by the strict concavity of E_0 (V4). The defect is of the order
  of the volume, so in a large box the form is negative also on the functions of mean zero (min-max: the
  infimum over a subspace of codimension one is at most the second eigenvalue). Two
  normalised transfer operators at different couplings are not comparable as operators for the same
  reason: their vacua are almost orthogonal in a large box. So no operator inequality between couplings
  can be the proof; the proof must use that a level differs from the vacuum by a bounded amount.
- (V5) is what the Dirichlet form gives without that input: the square root of each level is Lipschitz in
  b, with a constant set by the vacuum specific heat -E_0''. The specific heat is of the order of the
  volume, so the bound lets a level reach zero at a finite coupling as the box grows. It is of the same
  kind as Way 2 of row 708 and Lemma G of row 978: a bound that carries the volume.
- First failing step of this way: to pass from (V5) to (COV) one needs
  Cov_(mu_0)(f_i^2, w_p) <= C m_i / |B| for one plaquette w_p, with C independent of the gap: the local
  magnetic shift of a level is at most a constant times its energy density. Every locality theorem I
  know gives C as a negative power of the gap. This is the place where row 708 stopped.

### 3.4 Lemma Q: what concavity alone gives for the first level (PROVED; elementary)

Setting of 3.1. Let Lambda_2(b) be the sum of the two lowest eigenvalues of H(a, b), counted with
multiplicity, and m_1 = Lambda_2 - 2 E_0 >= 0 the first level. Let M >= -E_0'' on [b_0, b_1 + h_0].

(Q1) For b in [b_0, b_1] and 0 < h <= h_0: m_1(b + h) <= m_1(b) + h D m_1(b) + M h^2, where D is the right
derivative.

(Q2) If h_0^2 M >= sup of m_1 on [b_0, b_1], then sqrt(m_1(b)) + sqrt(M) b is non-decreasing on
[b_0, b_1]. So sqrt(m_1(b)) >= sqrt(m_1(b_0)) - sqrt(M) (b - b_0).

(Q3) -E_0'' = a integral of |nabla u|^2 d mu_0 <= 2 Var_(mu_0)(W)/m_1.

Proof. (Q1) Lambda_2(b) is the infimum over orthonormal pairs of <psi, H psi> + <psi', H psi'> (Ky Fan),
an infimum of affine functions of b. So it is concave, it has a right derivative, and
Lambda_2(b + h) <= Lambda_2(b) + h D Lambda_2(b). E_0 is analytic and
E_0(b + h) >= E_0(b) + h E_0'(b) - M h^2/2. Subtract twice the second line from the first.
(Q2) m_1(b + h) >= 0, so -D m_1(b) <= m_1(b)/h + M h. Where m_1(b) > 0 take h = sqrt(m_1(b)/M) <= h_0:
-D m_1 <= 2 sqrt(M m_1), so the right derivative of sqrt(m_1) is at least -sqrt(M). A continuous function
whose right derivative is at least -c on a set, and which is at its minimum 0 off that set, has
g(b) + c b non-decreasing. (Q3) By (V4), (V1) and (V2), -E_0'' = 2 <u, L u> = 2 <W - <W>_0, L^(-1)(W - <W>_0)>
in L^2(mu_0), and L >= m_1 on the functions of mean zero. QED

Reading. Row 708, Way 3, records no bound on a first derivative from convexity. In the time-continuum
model, concavity of Lambda_2 and of E_0 together with the positivity of the level give one: (Q2), a
square-root bound that carries the volume through M. The Euclidean thermal defect g = log Z - t log
lambda_0 of a torus with all sides even has the same property by the same argument: it is non-negative,
even in beta, and g'' <= Var(S) because log lambda_0 is convex, so |g'| <= sqrt(2 g sup Var(S)). Neither
bound gives (DEF_K), and neither changes a verdict: the ladder of row 978 still climbs a finite distance.

### 3.5 Checks of the signs (GUIDE)

- Gaussian model (a free field; not the lattice model): H = -(a/2) Delta + (b/2) <x, A x> has levels
  sqrt(ab) omega, so dm_i/db = m_i/(2b), Cov(f_i^2, W) = -m_i/(2b), and the right side of (V6) is zero.
  The lattice-unit levels of a free field do not depend on beta, and (COV) holds with room.
- For Wilson SU(2) the ratio 2 b Cov/m_i must move from -1 (perturbative levels of a small box) to
  c beta - 1 (levels that scale). A proof of (COV) must bound this move from above at order-one coupling.
- For compact U(1) the ratio is unbounded in the box size near the transition, as (COV) must fail there.
- One numeric run (GUIDE only; numpy with one thread, under one second, in a session scratch folder
  outside the repository; not kept). Model: two angles, H = -(1/2) Delta - b (cos x + cos y + cos(x - y)) on
  a 36 x 36 Fourier grid, b = 0.3, 1, 3. It reproduced (V3) three ways to six digits (for b = 1:
  -dm_1/db = Cov = pairing = -0.495208), (V4) (0.355182 against 0.355184), and the inequalities (V5) and
  (Q3) with room. It tests the algebra of Lemma V, not the lattice model.

## Step 4. What failed and what is left

- Not proved: the mass gap of four-dimensional SU(2) Yang-Mills theory in the sense of Jaffe and Witten.
  Nothing is disproved.
- The attack (Step 2): continuity in the coupling from the strong-coupling seed, closed by one a priori
  estimate, the one-sided lattice Callan-Symanzik inequality (LEV). I derived the attack and its
  consequence before I searched for it. It is on file in a better form (row 708 with its check 709, and
  row 978). I add no route.
- The fourth way to the estimate (Step 3): the ground-state form. Lemma V gives exact identities. They
  show that the estimate is not an operator inequality and not a quadratic-form inequality, so a proof
  must use the bounded difference between a level and the vacuum. Lemma V and Lemma Q then give bounds
  that carry the volume. First failing step: a bound of the plaquette shift of a level at one plaquette
  by its energy density, with a constant that does not depend on the gap. Row 708 stopped at the same
  statement.
- In one sentence: reflection positivity gives the inequality "Gamma(2t) <= 2 Gamma(t) + constant" in the
  time variable for free, and the missing statement is the exchange of the coupling derivative for a
  scale derivative at a bounded rate; I found no exact tool for that exchange, and compact U(1) shows that
  no tool of the class can exist.
- OPEN, unchanged: (VIR-log) and (DEF_K) of row 708 (my (LEV), (ACT), (COV)); (N-phys); (W); (SL)/(RR);
  the continuum datum (existence).
- Limits of this run. One author; no check by another model or provider; the same model family as most
  seats, so its agreement with the lane's map is not independent evidence. Read in full: Theorem S and
  Lemmas K, X, E of `library/gap-crux-restate.md`; Section 4.4 of `library/gap-mid-max.md`; Lemmas LAD
  and G of `library/gap-ladder-max.md`. Read by statement only: Theorem TR and Corollary TR1. Statements
  about the literature (Chatterjee on three-dimensional theories with a central U(1); Durhuus and
  Frohlich; the Cordes inequality; Ky Fan's principle) are recalled from memory and were not read in
  this run. No outside search. Searches of `library/` by key word are stated where used and are not
  proofs of absence.

Credits: Jaffe and Witten (the problem); Balaban (the renormalization group and ultraviolet stability);
Sussman and Alpoge, with Claude and Codex as authors of their text (the account the lane ports);
Osterwalder and Seiler (reflection positivity, the transfer operator, strong coupling); Kogut and Susskind
(the Hamiltonian); Hellmann and Feynman (first-order perturbation); Callan and Symanzik (the scaling
equation); Ky Fan (concavity of eigenvalue sums); Cordes, and Araki, Lieb and Thirring (the power
inequalities); Durhuus and Frohlich (the layer form); Chatterjee (the probabilistic formulation and the
three-dimensional result); Guth, and Frohlich and Spencer (the massless phase of U(1)); OpenAI, and Ding,
Huang and Yang (the two-dimensional O(N) proofs, as read in rows 1007-1010); the authors of rows 708,
709, 978, 1139, 1198, 1200, 1201, 1234, 1259 and 1269 of this lane, whose statements this file re-derives
or uses.

RESULT: Row 1281 (Claude Fable 5.2 max, laptop subagent; author only, checked by no one; one GUIDE run under one second, no outside search). The mass gap of four-dimensional SU(2) Yang-Mills is NOT proved and nothing is disproved. Attack judged best, and worked before the record was searched: continuity in the coupling from the strong-coupling seed, closed by one a priori estimate, a one-sided lattice Callan-Symanzik inequality (LEV): no ordered level of a periodic cube falls faster than at a bounded logarithmic rate K in beta. PROVED GIVEN (LEV), Theorem S and Lemma E of gap-crux-restate: a seed at one coupling gives seeds at every larger coupling, of size at most exp((1 + o(1)) K beta). The attack and this consequence are on file in a better form (row 708, checked in row 709: Theorem TR, (VIR_K), (LEV_K), (DEF_K); row 978: A2, A3, Lemmas LAD and G), so this run adds no route and is a further recovery by the same model family, not independent evidence. PROVED here, elementary, not selective, no consumer: Lemma V (for the Kogut-Susskind Hamiltonian of a periodic box, with u = d log psi_0/db: L u = W - <W>_0; the fall of a level is -dm_i/db = Cov(f_i^2, W) in the vacuum measure = a times the integral of f_i grad f_i . grad u; -E_0'' = a times the integral of |grad u|^2; (dm_i/db)^2 <= 2 a m_i times the integral of f_i^2 |grad u|^2); Lemma Q (from Ky Fan concavity and positivity, sqrt(m_1) + sqrt(M) b is non-decreasing, M a bound on the vacuum specific heat; a first-derivative bound from concavity and positivity, where row 708 Way 3 records none; it carries the volume). ARGUED: (LEV) is false as a quadratic form and as an operator inequality between two couplings (the concavity defect is of the order of the volume), so a proof must use that a level differs from the vacuum by a bounded amount; this fourth way stops where row 708 stopped, at a bound of the local plaquette shift of a level by its energy density with a constant independent of the gap. OPEN, unchanged: (VIR-log)/(DEF_K), (N-phys), (W), (SL)/(RR), the continuum datum. Output library/gap-laptop-solve3-fable.md.
