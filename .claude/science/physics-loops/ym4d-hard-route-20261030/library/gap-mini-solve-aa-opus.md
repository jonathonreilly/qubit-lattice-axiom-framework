lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T21:01Z

# gap-mini-solve-aa-opus: mass gap for 4D SU(2) Yang-Mills (FINISH row 1244)

Started 2026-11-20T09:01Z on the Mac mini worker, branch `claude/ym4d-hard-route`, pinned at commit e3efb7b0d.
Labels: PROVED (written argument complete here), ARGUED (argument given, a step not fully written), GUIDE (heuristic or numeric guidance, never a proof step), OPEN.

## 0. Status of this file

All steps written (Step 0 09:25Z, Step 1 09:27Z, Step 2 09:41Z, Step 3 and Result 09:43Z, GUIDE run 2.5 at 09:44Z by date -u). Run complete.

## Step 0. Reading log (reading only; no new claim; written 2026-11-20 about 09:25Z by date -u)

Read at the pin e3efb7b0d: GOAL.md in full; FINISH.md L1-85 and L299-352 (state, how we work, joining, working
efficiently, rules); row 1244 (this row) in full; the RESULT lines of rows 1188-1202, 1212-1213, 1219-1220, 1224-1225,
1228-1229, 1233, 1237-1238, 1243 (files `library/gap-mini-solve-a-fable.md` to `-z-opus.md`); `parts/gap.md` L1-104
(formulation, the wall, methods 1-36, lead rules); `library/prior/gap-onebound-read-sol.md` (row 1218) in full;
`library/gap-mini-solve-z-opus.md` Steps 0-3 (row 1243); the plans of the running sibling rows 1234 (v-opus, Section 2)
and 1241 (y-opus, Step 0) as they stand at this pin. Read later, for Steps 1-2: `library/gap-short-step-max.md` L213-278
(row 1018 Section 4: Lemmas FLOW, PROJ, FR+, SPLIT); `library/gap-pinned-cell-gauge-max.md` L480-505 (row 1011 7.3-7.4);
`library/gap-mini-free-fable.md` L205-300 (row 1181 3.5-4.4); `library/gap-brainstorm-max.md` items 23-31, 27, G8-G16;
the headings and RESULT of `library/gap-mini-solve-p-fable.md` (row 1220); and grep hits named in Step 1.3.

Where the problem stands on file (cited, not re-derived):

1. Consumer side. Beside the premises of Sussman and Alpoge's complete account, the Jaffe-Witten gap on the
   account's tr F^2 sector follows from one lattice estimate, (N-phys) (row 1179 Theorem BP, check 1183; row 1225
   Theorem E-N, check 1232).
2. (N-phys) (row 1161; row 1179 L304-310): at one physical side L, for every cutoff j >= j_0, some u_j with
   3 <= u_j <= n_j/K has s_+(u_j; n_j^3) <= 1/2, where s_+ is the centre-neutral excited trace of the
   vacuum-normalised periodic transfer matrix on the spatial cube n_j^3, and K is fixed first.
3. Modulo the ultraviolet carry (UNIV-K), the crux is a finite seed for Wilson SU(2) at one fixed coupling in the
   account's window, where the running coupling is of order one (rows 1225, 1229, 1233, 1237, 1238).
4. About 45 engine families are screened with named failing steps (methods 1-36 of `parts/gap.md`; rows 1189, 1194,
   1199, 1200, 1229, 1237). This includes the orbit-space curvature route (Singer, Feynman; O'Neill's term), which is
   item 27 and G9 of `library/gap-brainstorm-max.md` and input 10 of row 1003's check.
5. Row 1218's published inputs (A: Bhattacharjee, Bhattacharya, Lockwood, Romanov, Sessford, Singha Roy; B: the
   first four authors; C: Zeng Chunping) give a full thermal one-scale seed with a proved conditional ascent (A),
   cube-dynamics criteria and a weak-coupling Poincare bound for straight-path block variables (B, Corollary 166;
   not selective by row 1220), and common-rate criteria (C). None proves the Wilson estimate at weak coupling.

Siblings on the same brief at this pin: rows 1234 (v: the thermal count at one coupling), 1241 (y: Step 1 not yet
written), 1243 (z: the sign of the non-abelian frame response, reduced to (S-V)), 1246 (gpt-6.2-astra), 1248-1249
(queued). This row keeps its item distinct from theirs.

## Step 1. How best to attack it (judgement; ARGUED; written 09:27Z by date -u)

**1.1 What a proof has to contain (cited, not new).** Beside the T0 chain, the gap clause reads one lattice estimate,
(N-phys) (Step 0, item 1). Modulo the ultraviolet carry, (N-phys) is a finite seed for Wilson SU(2) at one fixed weak
coupling beta_0, on a box of side of order exp(c beta_0) lattice units (rows 1180, 1225, 1233, 1238). The 2D analogue
shows the shape of a possible proof: OpenAI's 2D O(3) construction needs, at one bare coupling, only a non-sharp
mixing length X(b) = C exp((4 pi - eta) b), and its renormalization group carries that one bound to every finer
cutoff (rows 1009, 1010). So in 4D the crux is the classical open problem in its weakest useful form: exponential
clustering, at any rate, of 4D lattice SU(2) at one weak coupling, with a thermal count. The seed box sits where the
running coupling is of order one.

**1.2 What kind of input can do it (cited).** Lead rule W2 of `parts/gap.md`: (K-one), a property of the measure at
one scale in the band, or (K-flow), a step carried through the band by an identity that fails for U(1), for frozen
groups and for products with a massless factor. A (K-one) seed needs a number at the band, and no hand expansion
reaches the band (character ratio about 0.48-0.52 there, about 0.045 at the hand-proved strong-coupling edge, row
1229); GOAL.md forbids a computed certificate. A (K-flow) step needs an exact identity with a non-abelian sign at
order-one response; the identities on file do not give one (row 1243 Step 2.2: gauge Ward identities move no
gauge-invariant datum, link symmetries are central (CEN, CEN+), lattice symmetries are finite, Schwinger-Dyson
equations need a small parameter, reflection positivity is blind).

**1.3 My own screening, each candidate grepped before any work (rule 0a).** I listed the band-crossing ideas I know
and searched the lane folder for each. Counts are files under `library/` and `parts/` that name the idea.

| Candidate | What it would use | On file |
|---|---|---|
| Curvature of the orbit space (Singer; Feynman 1981; O'Neill's term) | positive curvature added by the gauge quotient, zero for U(1) | yes: `gap-brainstorm-max.md` items 27, G9; input 10 of row 1003 (check row 1006): its consumer (Bakry-Emery) stops near beta 1/8; uniform curvature forces a trivial limit (row 1237 Proposition UNI) |
| Non-abelian unwinding of abelian flux (no conserved integer flux in SU(2)) | a 2 pi abelian flux is contractible in SU(2), not in U(1) | as a property: row 878 C4; as the flux and w_2 picture: brainstorm items 47, G18, rows 809-810; as the twist stiffness: rows 1011-1018, 1228, 1243 |
| Paramagnetic sign of gluon spin (Nielsen-Hughes split 11/3 = 4 - 1/3; Nielsen-Olesen unstable mode) | the spin term of the fluctuation operator | yes: row 1011 L496 (RECALLED), row 1195 (HM), brainstorm item 11 ("no step from saddle to free energy") |
| Topological charge, theta dependence, self-dual 't Hooft-symbol identification of Lambda^2_+ with su(2) | pi_3(SU(2)) = Z, absent for U(1) on R^4 | instantons in 43 files; theta dependence in 2 (rows 1200 and one other); the 't Hooft-symbol identification in 0. I found no inequality it yields: the identification is a fixed linear map, U(1) has the same spacetime group, and the non-abelian gauge-invariant cubic tr(F[F,F]) enters no exact identity I know |
| Dual weak coupling, as in Gopfert and Mack's 3D U(1) proof | a dual description that stays weakly coupled at all scales | yes: rows 859 (item 34), 1201 table item 8, 1237 Step 1.2 (dilute defect gas). In 4D SU(2) the defects at the physical scale are not dilute (their fugacity exp(-c/g^2(L)) is of order one at the band), so no small parameter is left |
| Conformal-window comparison (AF with a gapless infrared) | a test, not an engine | yes: row 998 C18 (outside the class K; BELIEF) |
| Loop equations, Nishimori line, positivity, chessboard, Lee-Yang, continuity in beta, Migdal-Kadanoff, Tomboulis, thin twisted torus, five-dimensional test | | all on file with a named failing step (methods 1-36 of `parts/gap.md`; rows 754-760, 797, 842, 1017, 1084, 1190, 1213) |

**1.4 Judgement.** I found no engine of a new kind. The one structure I found unused, the identification of
self-dual 2-forms with su(2), gives no inequality that I can see (row of 1.3), so I do not open it as a route. This
agrees with rows 1219, 1225, 1229, 1237, 1238 and 1243. Row 1243 (Step 3.4) counted 59 solve-type rows between 1141
and 1246 and 53 RESULTs, all with the gap open; the missing (K-flow) identity is the same object since row 1013.

**1.5 What this row does.** Rule 0a forbids attacking a listed open lemma ((S-V), (DEC), (HM), (GC), (CAS) and the
rest are listed). An off-map engine is not available. So this row spends its effort on one question that is not
listed, is decidable in a session, and bears on every future (K-flow) row: **where, in the exact stiffness split of
Lemma FLOW (row 1018), does the one-loop asymptotic-freedom decrement of 4D SU(2) sit, compared with the 2D O(N)
models whose band-crossing proofs exist?** If the decrement sits in the variance term for every extension of a
given class, a Jensen-type (direct-term) argument with that class cannot capture asymptotic freedom even at weak
coupling, and (S-V) is impossible in that class; if it can sit in the direct term, the lane gets a weak-coupling
model of the extension it needs. I first check that this exact question is not on file (Step 2.0).

## Step 2. Where the one-loop running sits in the stiffness split (written 09:30Z-09:41Z by date -u)

**2.0 Duplicate check (rule 0a).** Nearest items on file, read: row 1018 4.1 (Lemma FLOW, the exact split
H_c = -E[V Psi_V] - Var(Psi_V); its minimiser is ARGUED to exist, not written); row 1011 7.4 (N3): "The orbital
(diamagnetic) part of the one-loop response has the sign that RAISES the stiffness; the spin (bracket) part lowers it
and is larger (RECALLED: the split 11/3 = 4 - 1/3 ...). A variance lower bound would have to capture the bracket part
while (N2) controls the other. Not derived here."; row 1195 (HM) (the orbital, Meissner cancellation of the seagull
by the current variance); row 1181 3.5 (the mass-like N^2 term is cancelled only by the variance); row 1228
Proposition P5 (Gaussian U(1) plate cells); rows 1013 (Lemmas WN, JEN) and 1181 (Fact 4.2, Proposition J) on fixed
moves. None writes the one-loop minimiser or locates the logarithm of the running in the split. This step derives
(N3)'s sentence in an exact model. It is a structural statement about the (K-flow) template; it does not touch the
seed.

**2.1 The Gaussian twist model and its exact split (PROVED).**

Setting. A finite set of sites, n real components per site, so fields phi in R^N. Real symmetric N x N matrices
M_0 > 0, M_1, M_2; M_theta := M_0 + theta M_1 + theta^2 M_2, positive for |theta| < theta_0. A smooth classical part
s(theta). Z(theta) := integral of exp(-s(theta) - (1/2)<phi, M_theta phi>) dphi, F := -log Z, G := M_0^(-1).
This is the one-loop (Gaussian) form of a pinned cell under a twist theta: s is the classical action of the twisted
background, M_theta the fluctuation operator in it.

**Lemma 2.1 (split for every linear flow).** For every real N x N matrix K (the flow phi -> exp(theta K) phi of the
fluctuations, together with the twist of the background),

    F''(0) = D_K - V_K,
    D_K = s''(0) + tr(G M_2) + 2 tr(G M_1 K) + tr(K^2) + tr(G K^T M_0 K),
    V_K = (1/2) tr((G N_K)^2) >= 0,      N_K := M_1 + M_0 K + K^T M_0,

and F''(0) = s''(0) + tr(G M_2) - (1/2) tr((G M_1)^2) for every K. V_K = 0 if and only if N_K = 0. The flow
K_* := -(1/2) G M_1 has N_(K_*) = 0, so D_(K_*) = F''(0).

Proof. Substitute phi = exp(theta K) psi; the Jacobian is exp(theta tr K). With
g(theta, psi) := s(theta) - s(0) + (1/2)<e^(theta K) psi, M_theta e^(theta K) psi> - (1/2)<psi, M_0 psi> - theta tr K,
F(theta) - F(0) = -log E[exp(-g(theta, psi))], E the law N(0, G). So F''(0) = E[d^2 g] - Var(dg) at theta = 0.
Differentiating: dg = s' + (1/2)<psi, N_K psi> - tr K, and
d^2 g = s'' + <psi, M_2 psi> + <psi, (K^T M_1 + M_1 K) psi> + (1/2)<psi, ((K^T)^2 M_0 + 2 K^T M_0 K + M_0 K^2) psi>.
Gaussian moments: E<psi, A psi> = tr(G A), and Var((1/2)<psi, A psi>) = (1/2) tr(G A G A) for symmetric A. With
tr(G (K^T)^2 M_0) = tr(K^2) = tr(G M_0 K^2) and tr(G K^T M_1) = tr(G M_1 K) this gives D_K and V_K. Expanding,
(1/2) tr((G N_K)^2) = (1/2) tr((G M_1)^2) + 2 tr(G M_1 K) + tr(K^2) + tr(G K^T M_0 K) (each cross term reduces by
G M_0 = I and cyclicity), so D_K - V_K = s'' + tr(G M_2) - (1/2) tr((G M_1)^2), which is also (s + (1/2) log det
M_theta)'' at 0. Last, N_(K_*) = M_1 - (1/2) M_1 G M_0 - (1/2) M_0 G M_1 = 0. QED

Reading. D_K is the direct (Jensen) term of Lemma FLOW for the flow "twist the background, move the fluctuations by
K", and V_K is the variance it drops (row 1018 4.1, in Gaussian form). Every trace in D_K has at most ONE propagator G
(a tadpole: G at coincident or nearby points when K, M_1, M_2 are local). The only two-propagator trace, the bubble
(1/2) tr((G M_1)^2), enters F'' with a minus sign, and for the pure background twist K = 0 it is entirely the dropped
variance: D_0 = s'' + tr(G M_2) (classical plus seagull), V_0 = (1/2) tr((G M_1)^2). K_* is the derivative at
theta = 0 of the symmetric Gaussian transport phi -> M_theta^(-1/2) M_0^(1/2) phi between the fluctuation laws: it is
the linear response of the fluctuation field, computed with the propagator.

**2.2 A bounded flow cannot move the spin bubble into the direct term (PROVED).**

Model. The torus T_L = (Z/LZ)^4, V = L^4 sites, n components, M_0 = (-Delta + mu^2) (x) I_n with 0 < mu <= 1, Delta
the lattice Laplacian. Fourier modes p in (2 pi/L) Z^4 with entries in (-pi, pi]; eigenvalues
lambda(p) = sum_i 4 sin^2(p_i/2) + mu^2. Spin-only coupling: M_1 = I (x) m_0 with m_0 a constant real symmetric
n x n matrix (no derivative), M_2 arbitrary. ||.||_F is the Frobenius norm. S_j(eps) := sum over p with
lambda(p) <= eps of lambda(p)^(-j).

**Lemma 2.2 (lattice sums, d = 4).** For mu^2 < eps <= 1:
(a) S_2(eps) >= (V/(256 pi^2)) (log(eps/mu^2) - 1);
(b) S_1(eps) <= mu^(-2) + 4 eps V;
(c) S_2(infinity) <= mu^(-4) + V (625/256) (log_2 L + 2).

Proof. For |t| <= pi, (4/pi^2) t^2 <= 4 sin^2(t/2) <= t^2, so (4/pi^2)|p|^2 + mu^2 <= lambda(p) <= |p|^2 + mu^2.
Put delta = 2 pi/L. (a) h(q) := (|q|^2 + mu^2)^(-2) is radially decreasing. For p with all p_i >= 0, the cube
p + [0, delta)^4 lies in the closed positive orthant and h <= h(p) on it; these cubes cover {q >= 0 : |q| <= R} by
the cubes of the points p with |p| <= R (take p = delta floor(q/delta)). With R^2 = eps - mu^2 <= 1 < pi^2 every
such p is a mode and has lambda(p) <= |p|^2 + mu^2 <= eps. So
S_2(eps) >= sum over these p of h(p) >= delta^(-4) (1/16) integral over |q| <= R of h
= (V/(16 (2 pi)^4)) 2 pi^2 integral_0^R r^3 (r^2 + mu^2)^(-2) dr
= (V/(256 pi^2)) [log(eps/mu^2) + mu^2/eps - 1] >= (V/(256 pi^2)) (log(eps/mu^2) - 1).
(b) The mode p = 0 gives mu^(-2). For p != 0 sort by shells 2^k delta <= |p| < 2^(k+1) delta, k >= 0. A shell has at
most (2^(k+2) + 1)^4 <= 625 * 2^(4k) points and on it lambda(p)^(-1) <= (pi^2/4) 2^(-2k) delta^(-2). A shell meets
{lambda <= eps} only if (4/pi^2) 2^(2k) delta^2 <= eps. Summing the geometric series over those k,
sum <= 625 (pi^2/4) delta^(-2) (4/3) (pi^2/4) eps delta^(-2) = (625 pi^4/12) eps delta^(-4) = (625/192) eps V <= 4 eps V.
(c) The same shells with lambda(p)^(-2) <= (pi^4/16) 2^(-4k) delta^(-4) give at most 625 (pi^4/16) delta^(-4) =
(625/256) V per shell; |p| <= 2 pi gives at most log_2 L + 2 shells. QED

**Proposition 2.3 (Jensen loss of bounded flows).** In the model of 2.2:
(i) If K is translation-invariant (a Fourier multiplier with n x n symbols K^(p)), then
    V_K = 2 sum over p of || Herm K^(p) + m_0/(2 lambda(p)) ||_F^2,     Herm X := (X + X^dagger)/2.
(ii) If moreover ||K^(p)||_op <= k for all p, then with eps_k := min(1, ||m_0||_F/(4 sqrt(n) k)),
    V_K >= (||m_0||_F^2/8) S_2(eps_k) >= (V ||m_0||_F^2/(2048 pi^2)) (log(eps_k/mu^2) - 1).
(iii) For every real K (not necessarily translation-invariant) and every eps in (mu^2, 1],
    V_K >= (1/2) [ ||m_0||_F S_2(eps)^(1/2) - 2 sqrt(eps) ||K||_op (n S_1(eps))^(1/2) ]_+^2 .
    With mu = 1/L and eps = min(1, ||m_0||_F^2/(20480 pi^2 n ||K||_op^2)) this gives
    V_K >= (V ||m_0||_F^2/(2048 pi^2)) (log(eps L^2) - 1) whenever log(eps L^2) >= 2.

Proof. (i) At each mode, G N_K acts as lambda^(-1)(m_0 + lambda (K^ + K^dagger)) = 2 Herm(K^) + m_0/lambda, a
Hermitian n x n matrix; tr((G N_K)^2) is the sum over p of its squared Frobenius norm. (ii) For lambda(p) <= eps_k,
||Herm K^(p)||_F <= sqrt(n) k <= ||m_0||_F/(4 lambda(p)), so the term is at least (||m_0||_F/(4 lambda(p)))^2; sum
and use Lemma 2.2 (a). (iii) Let P be the spectral projection of M_0 onto lambda <= eps; P commutes with G and with
I (x) m_0. X := G^(1/2) N_K G^(1/2) has V_K = (1/2)||X||_HS^2 >= (1/2)||P X P||_HS^2. P X P = A + C with
A = (G P) (x) m_0, ||A||_HS = ||m_0||_F S_2(eps)^(1/2), and C = P M_0^(1/2) K G^(1/2) P + P G^(1/2) K^T M_0^(1/2) P,
||C||_HS <= 2 ||P M_0^(1/2)||_op ||K||_op ||G^(1/2) P||_HS <= 2 sqrt(eps) ||K||_op (n S_1(eps))^(1/2). So
||P X P||_HS >= ||A||_HS - ||C||_HS. For the second form: mu = 1/L gives n S_1 <= n(L^2 + 4 eps V) <= 5 n V; the
choice of eps makes ||C||_HS <= ||A||_HS/2 once log(eps L^2) - 1 >= 1, by Lemma 2.2 (a). QED

Remarks. (1) The bound is attained in order: K_* = -(1/2) G (I (x) m_0) has symbol -m_0/(2 lambda(p)) and norm
||m_0||_op/(2 mu^2); the bound in (ii) stops losing the logarithm exactly when k reaches the size of K_* on the lowest
modes. (2) Translation-invariant flows that are local (finite range) have bounded symbols, so (ii) covers them; so does
every flow that moves every mode by at most k. (3) The whole bubble is (1/2)||m_0||_F^2 S_2(infinity) <=
(1/2)||m_0||_F^2 V (1 + (625/256)(log_2 L + 2)) by Lemma 2.2 (c) (mu = 1/L), so for fixed k the loss in (ii) is at
least a fixed fraction of the whole spin bubble as L grows: the logarithm of the spin part is lost, not only a
constant.

**2.3 The Yang-Mills instance (ARGUED for the identification; coefficients RECALLED).** At one loop in a background
field (Feynman gauge), the gluon fluctuation operator is -D^2 delta_(mu nu) - 2 ad(F)_(mu nu) and the ghosts carry
-D^2. For an abelian background (one colour axis) the zero-derivative part m = -2 ad(F) is a real symmetric matrix on
(Lorentz x colour) indices (F antisymmetric in mu nu times ad antisymmetric in colour); it is the spin coupling. The
derivative (orbital) part has Lorentz structure delta_(mu nu), so its trace against m over Lorentz indices vanishes;
with a constant field strength this is the orthogonality that lets 2.2 treat m alone. The spin bubble is the
paramagnetic part of the one-loop coefficient, the "4" of 11/3 = 4 - 1/3; the orbital part, "-1/3", has the
screening sign (Nielsen; Hughes; RECALLED, as in row 1011 7.4 (N3)). Reading 2.1-2.2 into this: with the pure
background twist (K = 0) the Jensen bound is classical plus seagull and drops the whole bubble; with any flow of
bounded strength it still drops at least a fixed fraction of the spin bubble's logarithm, so its logarithmic part is
never below the screening value. In words: **a Jensen bound with a bounded flow sees one-loop SU(2) Yang-Mills as a
screening theory.** (The torus with a constant field needs twisted boundary conditions for flux quantisation; the
model of 2.2 is the constant-coefficient core of that computation, not the computation. Not checked against a lattice
one-loop calculation.)

**2.4 The contrast with 2D O(N) (ARGUED at one loop; it matches the lane's reading of OpenAI's Lemma 2.3, row 1009).**
For the 2D O(N) model at coupling b, take the rigid rotation in the (e_0, e_1) plane with a harmonic profile f: a
local, bounded flow. At one loop its direct term is b cap <sigma^pl_x . sigma^pl_y> = (b - (N - 2) G_L(x,x) - 1/4) cap,
where the transverse tadpole G_L(x,x) = (1/(2 pi)) log L + O(1) in the bulk carries the whole one-loop running
(N - 2)/(2 pi); the linear part of Psi is b sum grad f . grad pi_1, whose variance b <grad f, Pi_D grad f> vanishes for
harmonic f (grad f is orthogonal to the gradients of Dirichlet functions), so the variance is of two-loop order. So
in 2D the running is a tadpole (one propagator at coincident points), which the direct term of a bounded local flow
keeps. In 4D the tadpole G_L(x,x) <= G_infinity(0) < infinity has no logarithm, and the running is the bubble
sum_y G(x,y)^2 ~ (1/(8 pi^2)) log L, a two-propagator object, which Lemma 2.1 puts in the variance for every flow and
Proposition 2.3 keeps there for every bounded flow. This is the dimensional reason, at one loop, why the 2D short step
(a Jensen bound with a symmetry-generated bounded flow) has no 4D copy, independent of the frame cost (rows 1011, 1141)
and of Lemma CEN+.

Note added to Proposition 2.3 (ii): if eps_k <= mu^2 the right side is negative and the bound is empty; Lemma 2.2 (a)
is used only for eps_k > mu^2.

**2.5 GUIDE control run (a run can refute or guide; it proves nothing).** Run 09:44Z under `numeric-lock` (54 percent
memory free, BLAS threads 1, nice, peak RSS 72 MB), script in a scratch folder outside the repository. Criteria fixed
before the run: (a) Lemma 2.1 on random 12 x 12 matrices: F'' by a finite difference of (1/2) log det M_theta equals
tr(G M_2) - (1/2) tr((G M_1)^2) to 1e-4; the simplified D_K equals the raw trace of d^2 g; D_K - V_K equals F''; N at
K_* vanishes. (b) Proposition 2.3 (i) on the torus L = 4, n = 2, mu^2 = 1/16, a random translation-invariant K with four
offsets: V_K from dense matrices equals the Fourier formula. (c) Lemma 2.2 (a)-(c) at L = 8, 16, 32, mu = 1/L,
eps = 1 and 1/4. Outcome: all pass (F'' = -0.338909 both ways; V_K = 583.2084628 both ways; every lattice-sum bound
holds). What it cannot show: anything beyond these instances. One observation: with mu = 1/L the zero mode alone gives
mu^(-4) = V to S_2, and at L <= 32 the logarithmic part of S_2 is only a few percent of V (about 0.025 V at L = 32), so
the constants of Lemma 2.2 (a) are far from sharp and the logarithm of Proposition 2.3 is an asymptotic statement.

## Step 3. What Step 2 means for the crux, the tests, and what stays open (ARGUED; written 09:43Z by date -u)

**3.1 Consequence for the (K-flow) template (ARGUED).** Row 1243 reduced a (K-flow) seed to (DEC) and then to (S-V):
an explicit flow V whose direct term is below the abelian value on typical SU(2) fields. Step 2 says what such a flow
must look like where the account already controls the measure (small effective coupling, cells far above the band):

1. It cannot be the twist of the background alone, nor the background twist plus any flow of the fluctuations of
   bounded strength. Each of these drops at least a fixed fraction of the spin bubble's logarithm (Proposition 2.3),
   so its direct term has, at one loop, no antiscreening logarithm: it sees a screening theory (2.3).
2. The flow that keeps the whole one-loop response in the direct term is K_* = -(1/2) G M_1 (Lemma 2.1): each
   fluctuation mode is moved by -m/(2 lambda(p)), by the twist angle on the longest modes and by almost nothing on
   modes of lattice size. It is the derivative of the Gaussian transport between the fluctuation laws at twist theta
   and at 0, which is the fluctuation part of one renormalization-group step in the twisted background.
3. So at weak coupling a 4D short step of the Jensen kind IS an RG step with its fluctuation response. The 2D short
   step is a symmetry move with a bounded local flow; the reason it works in 2D and not in 4D is dimensional at one
   loop: the 2D running is a tadpole (kept by Jensen), the 4D running is a bubble (dropped by Jensen with any bounded
   flow) (2.4). This is a second obstruction to a 4D copy of the 2D step, independent of the frame cost (Lemma FR,
   FR+, rows 1011, 1018, 1141) and of Lemma CEN+: even a Ward identity that removed the mass-like frame term ((N2) of
   row 1011) would leave a direct term with no running, unless the flow also carries the propagator response.
4. At the band the object that 2 needs is the propagator of the fluctuations in the actual field of a cell, at
   order-one coupling. The Dirichlet covariant Laplacian of a cell is invertible on every configuration and is
   dominated by the free one through the diamagnetic inequality (Kato; Simon; RECALLED, not rebuilt), so a covariant
   flow of the form "covariant Green's function applied to the spin coupling of the actual field" is defined on every
   configuration at every coupling. Whether its direct term can be bounded at the band is (S-V) in a sharper form. Not
   attacked here (rule 0a: (S-V) is listed by row 1243); OPEN, and no claim that it works.

**3.2 Tests of the Step 2 statements (each in the valid form: the hypothesis holds in the test model).**

| Test | Hypothesis of 2.2 holds? | Outcome |
|---|---|---|
| Compact U(1) at weak coupling, Gaussian form | yes, with m_0 = 0 (neutral photon: no spin and no orbital coupling at one loop) | V_0 = 0, F'' = classical, no running: consistent with the absence of a logarithm (pass) |
| 2D O(N), N >= 3 | not the model of 2.2 (no zero-derivative coupling); 2.4 applies | the bounded rigid rotation keeps the running in the direct term (consistent with OpenAI's Lemma 2.3 as read in row 1009) |
| Five dimensions | yes | sum over y of G(x,y)^2 converges in d = 5 (no logarithm), so there is no running to lose: consistent with an infrared-free theory |
| Lemma PT (product with a massless factor) | yes | the bound reads the spin coupling of the SU(2) factor only; it is a statement about where a logarithm sits, not a seed, so PT does not bind it |
| Frozen Q_8 and 2T | no Gaussian fluctuations | not applicable |

**3.3 What this row does not show.** Step 2 is a one-loop statement in a Gaussian model with a constant spin coupling
on a torus; its transfer to the pinned cells of the Wilson measure is ARGUED (2.3), not proved, and the one-loop
coefficients 4 and -1/3 are RECALLED. It proves no bound on any Wilson quantity, it gives no seed, and it does not
exclude a (K-flow) step that is not of the Jensen kind. It shrinks the (K-flow) search space: a Jensen-type step must
carry the propagator response of the fluctuations, i.e. it must be an RG step, which is where the account's control
ends at the band.

**3.4 Note for the lead (a recommendation, not a ruling).** This is the 27th plain-brief row on the crux in the
`gap-mini-solve` series (rows 1188-1249), after 59 solve-type rows counted by row 1243. Every RESULT I read (rows 1188-1202,
1212-1213, 1219-1220, 1224-1225, 1228-1229, 1233, 1237-1238, 1243; in full only row 1243 Steps 0-3) records the gap
as open, and the rows among them that screen engines, with this row, found none of a new kind. Proof work that moves an open
statement of the gap clause now lies in two places the plain brief does not point at: the ultraviolet carry
((UNIV-K) items of rows 1233, 1237, 1238) and the account's open premises. A further plain-brief row on the crux is
unlikely to move (N-phys) unless it starts from a named new mechanism.

## Result

| Statement | Label | Where |
|---|---|---|
| Mass gap of 4D SU(2) Yang-Mills (Jaffe-Witten) | OPEN; not proved, nothing disproved | Steps 1-3 |
| (N-phys), the one open lattice input of the gap clause | OPEN | Step 0 |
| No engine of a new kind; six idea families screened (orbit-space curvature, flux unwinding, gluon-spin paramagnetism, topological charge and self-dual identification, dual weak coupling, conformal-window test), each on file or with no inequality | ARGUED | Step 1.3-1.4 |
| Lemma 2.1: exact one-loop split of the twist stiffness for every linear fluctuation flow; explicit minimiser K_* = -(1/2) G M_1 (the Gaussian transport) | PROVED (by hand, unchecked) | 2.1 |
| Lemma 2.2: 4D torus lattice sums S_2 >= (V/(256 pi^2))(log(eps/mu^2) - 1), S_1 <= mu^(-2) + 4 eps V, S_2(infinity) bound | PROVED (by hand, unchecked) | 2.2 |
| Proposition 2.3: every flow of bounded strength loses at least (V ||m_0||_F^2/(2048 pi^2))(log(eps_k/mu^2) - 1) of the spin bubble in the Jensen bound; exact formula for translation-invariant flows | PROVED (by hand, unchecked) | 2.2 |
| In one-loop SU(2) Yang-Mills a Jensen bound with a bounded flow sees screening; the 2D running is a tadpole, the 4D running a bubble; a 4D Jensen step must carry an RG step's fluctuation response | ARGUED (identification with the Wilson cells and the coefficients 4, -1/3 RECALLED) | 2.3-2.4, 3.1 |
| (S-V), (DEC), the covariant Green's-function flow of 3.1 item 4 | OPEN | 3.1 |

Checked by no one. One GUIDE control run of the algebra and lattice sums (2.5); no proof step rests on it. No subagent. No outside source was
fetched. Credits: OpenAI (the 2D O(3) and O(4) papers, through the lane's readings in rows 1009-1010); Bhattacharjee,
Bhattacharya, Lockwood, Romanov, Sessford and Singha Roy, and Zeng Chunping (through row 1218); Sussman and Alpoge with
Claude and Codex as authors of their text (the account, through rows 1179, 1225, 1233, 1237, 1238); Nielsen and Hughes
(the spin and orbital split of the one-loop coefficient, RECALLED); Singer and Feynman (orbit-space curvature, as on
file); Gopfert and Mack (3D U(1), as on file); Kato and Simon (diamagnetic inequality, RECALLED).

RESULT: Row 1244 (Claude Opus 5.5 max, Mac mini worker 3, 09:01Z-09:46Z by date -u; author only, checked by no one; one GUIDE control run of the algebra, no subagent): the mass gap of four-dimensional SU(2) Yang-Mills is NOT proved and nothing is disproved; (N-phys) stays OPEN, and a screen of six idea families found no engine off the record (ARGUED). PROVED by hand, unchecked, in a one-loop Gaussian model: Lemma 2.1 (the exact split F'' = D_K - V_K of the twist stiffness for every linear fluctuation flow K, with the explicit minimiser K_* = -(1/2) G M_1, the derivative of the Gaussian transport) and Proposition 2.3 with Lemma 2.2 (on the 4D torus with a constant zero-derivative spin coupling m_0, every flow of strength at most k loses at least (V ||m_0||^2/(2048 pi^2))(log(eps_k L^2) - 1), eps_k = min(1, ||m_0||/(4 sqrt(n) k)), of the spin bubble in the Jensen bound). ARGUED: in one-loop SU(2) Yang-Mills a Jensen bound with any bounded flow sees screening, because the 4D running is a two-propagator bubble while the 2D O(N) running is a tadpole that the rigid rotation keeps; so the 2D short step has no 4D copy even at weak coupling, and a 4D step of the Jensen kind must carry the fluctuation response of an RG step. OPEN: (N-phys), (S-V), (DEC), the ultraviolet carry and the account's premises. Output library/gap-mini-solve-aa-opus.md.
