lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T19:19Z

# gap-mini-solve-w-opus (row 1237)

Started 2026-11-20T07:19Z (date -u), worker pinned at commit 398892bd4 on branch claude/ym4d-hard-route.

Task (row 1237): prove that four-dimensional SU(2) Yang-Mills theory has a mass gap in the sense of Jaffe and Witten. First consider how best to attack it, then do it.

Labels: PROVED, ARGUED, GUIDE, OPEN. Numeric runs guide only.

## Step 0. Reading log and the state of the problem (reading only; no new claim)

Read at this pin: GOAL.md; FINISH.md sections How we work, Joining, Working efficiently, Rules and the RESULT lines of
rows 1212-1236; `parts/gap.md` L1-104 (state of attack, routes, lead rules) and L105-222 (obligations, requests,
price); `library/gap-mini-neutral-fable.md` L1-140 (row 1180, the exact statement of (N-phys)); all of
`library/prior/gap-onebound-read-sol.md` (row 1218, the three published sources); the RESULT lines of rows 924-925
((UNIV-K)) and 1025, 1029 (the Tomboulis line).

**Where the problem stands on file (no new claim).**

- The gap clause on the account's tr F^2 sector follows from ONE open lattice estimate, (N-phys), beside the account's
  premises (the T0 chain): row 1179 Theorem BP (check 1183), row 1225 Theorem E-N with row 1212 Proposition D, both
  HOLD AFTER CORRECTION in the cross-provider check row 1232, with rate M_* = (2/L) log(2^18/5041).
- (N-phys) (row 1161 L146-148, row 1179 L304-310, restated in row 1180 Step 1): there are a physical side L and j_0
  such that for every j >= j_0, with n_j = L/a_j and 4 | n_j, some integer u_j with 3 <= u_j <= n_j/K has
  s_j(u_j; n_j) = Tr_neutral (F/lambda_0)^(u_j) - 1 <= 1/2 (K = 512, n_j >= 2^70 in the explicit version).
  In words: the centre-neutral thermal partition function of the box L^3 at temperature K/L is at most 3/2 in vacuum
  units, uniformly in the cutoff.
- Row 1180 Step 2.1: (N-phys) holds iff every fine coupling has a finite seed size nu(beta_j) and
  limsup_j a_j nu(beta_j) < infinity: a lattice gap at each weak coupling plus a bound of asymptotic-scaling type.
- Row 1225 (ARGUED): modulo the ultraviolet hypothesis (UNIV-K) (open since rows 924-925), the crux is the gap of
  Wilson SU(2) at one fixed coupling with a seed side of order exp(c beta_0).
- Row 1218: published work (Bhattacharjee et al., One Bound at One Scale, and One Cube Estimate; Zeng Chunping,
  Hexagon 2611.00543 and 2611.00492) supplies criteria stronger than or different in kind from (N-phys), and none
  proves it at weak coupling. Row 1220 Proposition U: the weak-coupling Corollary 166 of One Cube Estimate also
  holds for the massless Villain U(1) theory on bounded tori, so it is not selective.
- Route families on file: about 36 methods in `parts/gap.md` L52-103 plus the three screening tables of rows 1189,
  1194 and 1199 (`library/gap-mini-solve-b-fable.md`, `-e-fable.md` Step 2.1, `-i-fable.md` Step 1.2), about 32
  families, each with a named failing step. The lead's standing advice (row 998 9.5, `parts/gap.md` L76-78): no
  further fresh-framing exercise by this model family.

**Rule 0a.** `library/open-core.md` holds no gap-lane item (grep for gap, neutral, N-phys, glue: hits only in
hard-core rows 174, 263, 267, 524, none on this lane). The FINISH rows on (N-phys) are 1161-1236. Row 1236
(gpt-6.2-astra, `gap-solve27-astra62`) is running the general continuation now; row 1238 (`gap-mini-solve-x-opus`)
has this same brief and runs after this item.

## Step 1. How best to attack it (judgement; written 07:42Z by date -u)

**1.1 What a proof must contain (cited, not new).** Along the account's trajectory the gap clause needs (N-phys)
(Step 0). By row 1180 Step 2.1 it is a lattice gap at each weak coupling plus a bound of asymptotic-scaling type. Row
1225 (ARGUED) and row 1229 Step 1.1: modulo (UNIV-K) it is a finite mixing length at ONE fixed weak coupling, carried
to finer cutoffs by the renormalisation group, which is the structure of OpenAI's 2D O(3) continuum proof (row 1010).
So a proof needs two parts: (A) the ultraviolet carry, which is (UNIV-K) given the account; (B) one estimate at the
scale where the running coupling is of order one (the band), from a structure valid at every coupling, since no
computed certificate is allowed (GOAL.md) and no expansion converges there (row 1229 Step 2: character ratio about
0.48-0.52 in the window against about 0.045 at the hand-proved strong-coupling edge).

**1.2 The kinds of band-crossing engine in rigorous mathematical physics, and their 4D SU(2) status (rule 0a).** I
listed every proved case I know where a gap or a crossover is obtained with no small parameter at the scale of the
gap, or where the small parameter comes from a dual description. Each kind has its 4D SU(2) entry on file:

| Kind of engine | Proved case | 4D SU(2) status, where on file |
|---|---|---|
| Stiffness of a rigid non-abelian twist (bracket gain) | 2D O(N), N >= 3 (OpenAI; Ding, Huang and Yang, row 1007) | no carrier: Lemma CEN+ (row 1016, check 1020); plate and boundary twists squeeze (rows 1188 PC, 1228 P5); SO(4) twist has no dimensionless stiffness (row 1053); 1-form twist group is Z_2 |
| Positivity or association for the neutral half | 2D O(N) singlets (row 1193) | fails: FKG-NO (row 1213), HF (row 1188), row 1084; (POS-N) open with no consumer (row 1213) |
| Curvature or convexity (Bakry-Emery, Brascamp-Lieb) | strong coupling (row 1218 A Theorem A; B Theorem 5) | uniform forms prove too much (row 1229 Claim A, ARGUED); window form needs a certificate; multiscale forms end at a gap statement (rows 957, 968) |
| Duality to a dilute defect gas with a second small parameter | 3D U(1) (Gopfert-Mack, CMP 82, 1982); 2D Kosterlitz-Thouless | in 4D SU(2) every defect action runs (vortices, instantons): no small fugacity at the gap scale; the deformed theory on R^3 x S^1 is `gap-brainstorm2-max.md` item 25; Route T (rows 678, 862) |
| Large N or an exactly solvable recursion | Gross-Neveu at large N; Migdal-Kadanoff (Ito) | N = 2 is fixed; the Migdal-Kadanoff line is rows 1025, 1029 (Tomboulis bracket (TB)_n open, gives the flux half only) |
| Compactness and rigidity, continuity in beta | none for a gap | rows 1017 (Theorem CR), 1189 table |

I checked further candidates against the screening tables of rows 1189, 1194, 1199 (memory of this worker, re-read
in `parts/gap.md` L52-103): Feynman's orbit-space argument (= orbit-space curvature, method 31), Zwanziger's Coulomb
bound (wrong direction: V_coul >= V_phys), a frame from a maximal-tree or temporal gauge (= tree, Coulomb and
collapse frames, rows 1041, 1045, 1141), a fundamental Higgs flavour twist (row 1199 table), the topological
susceptibility (row 1200, theta sectors), Knabe-type local gap thresholds (row 1032 B2; not frustration-free).
Each is on file with a named failing step.

**1.3 Decision.** I found no carrier for the engines above that is not on file, and no engine of a new kind. So I do
not claim an attack on part (B). Following row 1229's note (its items 2-3), the session goes to two items that are
in scope and can close:

1. **Proposition UNI** (Step 2): a proof of row 1229's Claim A, which is ARGUED there on RECALLED inputs. Statement:
   a volume-uniform Poincare constant for any bounded-range reversible local dynamics of the Wilson measure, held
   along a trajectory, forces correlations to decay at a rate bounded below in lattice units, hence a trivial
   continuum limit (against NT1). Moves: turns the kill of all coupling-uniform curvature, Poincare and log-Sobolev
   routes from ARGUED to PROVED, and gives the necessary rate gamma_j <= C a_j M for any route of that kind.
2. **(CLASS) of (UNIV-K)** (Step 3, if the account text can be fetched at the line numbers row 924 used): row 924
   marks it ARGUED; row 1229 Step 3 calls it a short line-by-line check. Moves: one of the four open sub-items of
   (UNIV-K), the ultraviolet carry, part (A) above.

Neither item supplies the seed (part (B)); the RESULT will say so.

## Step 2. Proposition UNI: a uniform local dynamics gap forces a trivial limit (written 07:47Z by date -u)

Kind: a kill of a route class (no seed). It proves row 1229's Claim A for jump dynamics, which row 1229 left ARGUED
on two RECALLED inputs. The covariance bound is the standard implication "spectral gap of a local dynamics gives
exponential decay of correlations" (Holley; Stroock and Zegarlinski; Martinelli's lectures on Glauber dynamics;
RECALLED as sources, not used), rebuilt here for gauge fields with explicit constants. The continuum reading with a
fixed block size is also B's Theorem 66 read with n_k fixed (Bhattacharjee, Bhattacharya, Lockwood and Romanov, One
Cube Estimate, row 1218; unchecked there); the proof below does not use B.

**Setting.** Lambda is a finite periodic lattice in four dimensions, E its links, U = (U_e) in SU(2)^E, and mu the
Wilson measure at any coupling (any finite-range Gibbs measure on SU(2)^E with plaquette interactions works the same
way). Distance on links: dist(e, e') is the graph distance in the graph on E where two links are adjacent when they
lie in a common plaquette. For B a set of links, Nhat(B) := {e : dist(e, B) <= 1}. A *block family* is a finite list
Bfam of link sets with diam(B) <= b for each B. For B in Bfam let P_B f := mu(f | U_(E\B)), the heat-bath update of B
(a self-adjoint projection on L^2(mu) and a Markov operator). The generator is L := sum over B in Bfam of (P_B - I),
P_t := exp(t L). Put rho := b + 2 and Delta := max over B in Bfam of #{B' in Bfam : B' meets Nhat(B)}.

Let Acal be a subspace of L^2(mu) that contains the constants and is mapped into itself by every P_B (for example the
gauge-invariant functions, or the centre-neutral ones; both are preserved because mu and the conditioning are
invariant under gauge transformations and under link-wise central multiplications). *Poincare on Acal with constant
gamma > 0* means gamma Var(g) <= Ecal(g) := sum over B of mu((g - P_B g)^2) for all g in Acal.

A bounded function f is *supported in* S, a set of links, if f depends on U_S only.

**Proposition UNI (a), lattice form. PROVED.** Assume Poincare on Acal with constant gamma. Let f be bounded and
supported in S_f, let g in Acal be bounded and supported in S_g, and let d := dist(S_f, S_g) >= b + rho. Then

    abs(Cov_mu(f, g)) <= (1 + 2 abs(S_f) abs(S_g)) ||f||_inf ||g||_inf exp(-kappa (d - b)),
    kappa := min(1, gamma/(e^2 Delta))/rho.

For the single-link heat bath in four dimensions b = 0, rho = 2, Delta = 19 (a link and the 18 links that share one of
its six plaquettes), so kappa = min(1, gamma/(19 e^2))/2. Constants do not depend on Lambda or on the coupling.

*Proof.* Step (i), a restricted dynamics that leaves f fixed. Let Bfam' := {B in Bfam : B does not meet S_f},
L' := sum over Bfam' of (P_B - I), P'_t := exp(t L'). For B in Bfam', f is measurable in U_(E\B), so
P_B(f h) = f P_B h for bounded h; hence L'(f h) = f L' h and, since L' is bounded on L^inf (finite volume), the
exponential series gives P'_t(f h) = f P'_t h. Every P_B preserves mu, so mu(L' F) = 0 and mu(P'_t F) = mu(F). With
h = g: mu(f g) = mu(P'_t(f g)) = mu(f P'_t g). Since also mu(P_t g) = mu(g),

    Cov(f, g) = mu(f (P'_t g - P_t g)) + mu((f - mu f)(P_t g - mu g)).                                    (2.1)

Step (ii), the spectral term. g in Acal and P_t preserves Acal; Poincare on Acal gives
||P_t g - mu g||_2 <= exp(-gamma t) ||g - mu g||_2 (the derivative of ||P_t g - mu g||_2^2 is -2 Ecal(P_t g)
<= -2 gamma ||P_t g - mu g||_2^2). So the second term of (2.1) is at most ||f||_inf ||g||_inf exp(-gamma t).

Step (iii), finite speed. Duhamel: P'_t g - P_t g = - integral over s in [0, t] of P_(t-s) (L - L') P'_s g ds, and
P_(t-s) is a contraction on L^inf, so

    ||P'_t g - P_t g||_inf <= integral over [0, t] of sum over B in Bfam \ Bfam' of ||(P_B - I) P'_s g||_inf ds.   (2.2)

Represent P'_s by independent rate-one Poisson clocks, one for each B in Bfam': for a realisation omega with rings at
blocks B_1, ..., B_K at times tau_1 < ... < tau_K in [0, s], P'_s g = E_omega[h_omega] with
h_omega := P_(B_1) P_(B_2) ... P_(B_K) g. If h is supported in S, then P_B h is supported in (S \ B) union (Nhat(B) \ B),
because the conditional law of U_B given U_(E\B) depends only on the links sharing a plaquette with B; and P_B h = h
when B does not meet S. So, applying the operators from the inside out (latest ring first), the support of h_omega
grows only through rings at blocks that meet the current support, and each such block adds links of Nhat(B), all
within distance rho of the block it touches. Hence, if h_omega depends on a link at distance at least D from S_g,
there is a chain of rings at times s > sigma_1 > ... > sigma_m > 0 at blocks C_1, ..., C_m with C_1 meeting S_g,
C_k meeting Nhat(C_(k-1)), and m >= D/rho. The number of block sequences (C_1, ..., C_m) of this kind is at most
abs(S_g) Delta^m (at most abs(S_g) Delta choices for C_1, as #{B containing a given link} <= Delta, then at most Delta
each). For one sequence, the expected number of ring tuples at strictly decreasing times is the volume s^m/m! of the
simplex (factorial-moment density one for each Poisson process, also when blocks repeat). So

    P_omega(h_omega depends on some link at distance >= D from S_g) <= abs(S_g) (Delta s)^m/m!,  m = ceil(D/rho).

A block B in Bfam \ Bfam' meets S_f, so all its links are at distance >= d - b from S_g. Since (P_B - I) h = 0 when h
does not depend on U_B, and abs((P_B - I) h) <= 2 ||h||_inf <= 2 ||g||_inf, with D = d - b and
#(Bfam \ Bfam') <= abs(S_f) Delta:

    sum over B in Bfam \ Bfam' of ||(P_B - I) P'_s g||_inf <= 2 ||g||_inf abs(S_f) abs(S_g) Delta (Delta s)^m/m!.

Put into (2.2): ||P'_t g - P_t g||_inf <= 2 ||g||_inf abs(S_f) abs(S_g) (Delta t)^(m+1)/(m+1)!.

Step (iv), choice of t. (x)^(m+1)/(m+1)! <= (e x/(m+1))^(m+1). Take t := (m+1)/(e^2 Delta). Then the finite-speed
term is at most 2 abs(S_f) abs(S_g) ||f||_inf ||g||_inf exp(-(m+1)), and the spectral term is at most
||f||_inf ||g||_inf exp(-gamma (m+1)/(e^2 Delta)). Both exponents are at least min(1, gamma/(e^2 Delta)) (m+1), and
m + 1 >= (d - b)/rho. QED

**Proposition UNI (b), continuum form. PROVED GIVEN (a) and the stated normalisation.** Let (beta_j, a_j), a_j -> 0,
be a trajectory, and let the Wilson measures mu_j on a family of tori (or any infinite-volume limit of them) satisfy
Poincare on Acal for some block family of fixed lattice diameter <= b, with constants gamma_j >= gamma_0 > 0 for
all j and all tori. Let F_j be bounded and supported in a set of links of physical diameter at most R inside a region A,
and G_j in Acal supported likewise in a region B, with physical distance r > 0 between A and B, and assume the
polynomial normalisation ||F_j||_inf ||G_j||_inf <= C a_j^(-k) for some k (this covers lattice tr F^2 densities
and their smeared, renormalised versions). Then Cov_(mu_j)(F_j, G_j) -> 0, and in fact

    abs(Cov_(mu_j)(F_j, G_j)) <= C' a_j^(-k-8) exp(-kappa_0 (r/a_j - b - 1)),  kappa_0 = min(1, gamma_0/(e^2 Delta))/rho.

*Proof.* Links of a common plaquette have midpoints within sup-distance 1, so dist(e, e') >= r/a_j - 1 for e in A,
e' in B; the supports have at most C (R/a_j)^4 links each; apply (a), and pass to infinite-volume limits for fixed
local F_j, G_j since the bound is uniform in the torus. QED

**Corollary UNI-1 (the kill). PROVED GIVEN (b) and the OS reconstruction on file.** Under the hypotheses of (b) the
continuum limit is trivial on separated tests: for every positive-time test F of the matched algebra,
||F - <F> Omega||^2 = Cov(Theta Fbar, F) is a limit of covariances of observables at physical distance >= 2 t_0 > 0,
so it is 0, and the reconstructed Hilbert space is C Omega. So NT1 (GOAL.md) fails. Hence on any trajectory that
satisfies NT1, no block heat bath of bounded lattice diameter has a Poincare constant bounded below uniformly in volume
and in j, on any invariant algebra that contains the matched observables. Quantitatively: if one normalised separated
covariance of matched observables stays above delta > 0 at physical distance r, then

    gamma_j <= e^2 Delta rho a_j (log(C' a_j^(-k-8)/delta)) / (r - (b + 1) a_j) = O(a_j log(1/a_j)).

**What this kills and what it does not.**

- Killed (PROVED for jump dynamics): every route whose engine is a volume- and coupling-uniform Poincare or
  log-Sobolev inequality for a bounded-range heat bath (single link, plaquette blocks, cubes of fixed lattice side),
  in particular B's Corollary 74 and A's cube inequalities (Theorems B and 9.14) read along a weak-coupling
  trajectory with a fixed cube side (row 1218: these are fixed strong-coupling domains; UNI says they cannot be
  continued uniformly). The curvature theorems (A's Theorem A, B's Theorem 5) fall under the Langevin case below.
- Not killed: dynamics whose blocks grow like 1/a_j (B's Theorems 45, 66, 84 with n_k a_k <= ell). For those,
  (a) gives a lattice rate of order gamma/(e^2 Delta rho) with Delta of order n^4 and rho of order n, which is the
  scale of B's own m_* = 16 varpi/(625 e^2 ell). They are the crux in another form (row 1218, row 1220 Lemma NULL).
- Curvature (Langevin) forms, row 1229 Claim A's first case: PROVED in Proposition UNI (c) below (added at 07:49Z),
  by the Helffer-Sjostrand formula and a Combes-Thomas conjugation; no finite-speed bound is needed.

**Rule 0a.** The covariance bound is a standard theorem for spin systems (sources above). In the lane, the same
conclusion is row 1229 Claim A (ARGUED, RECALLED inputs) and B's Theorem 66 with fixed n (row 1218, unchecked). I
found no file in `library/` that writes the proof (grep for "finite speed", "Lieb-Robinson", "trivial continuum",
"prove too much" in `library/gap-*.md`: hits are row 1032 B2, which is the exact Lieb-Robinson cone of the transfer
step, not of a heat bath; row 1229 Claim A; and row 1224's Lemma 6.2, a finite-speed estimate for B's chain at one
cube size used in another argument). So the proof is new to the lane; the statement is not new in the literature.

**Proposition UNI (c), curvature form. PROVED (written 07:49Z).** Give SU(2) a bi-invariant metric and SU(2)^E the
product metric; write V := -beta sum_p (1/2) tr U_p, so mu = exp(-V) dHaar/Z, and L := Delta - grad V . grad (the
Langevin generator, symmetric in L^2(mu)). Let M := Ric + Hess V, a field of symmetric endomorphisms of the cotangent
bundle; its blocks M_(e e') act from the e'-th to the e-th factor. Assume the Bakry-Emery bound M >= kappa > 0 at every
point. Put D := max over e of sum over e' != e of sup over U of ||M_(e e')|| (only Hess V has off-diagonal blocks; two
links share at most one plaquette, so D <= 18 c_H beta with c_H an absolute constant fixed by the metric). Then for
smooth f, g supported in S_f, S_g with d := dist(S_f, S_g):

    abs(Cov_mu(f, g)) <= (2/kappa) exp(-lambda d) ||grad f||_(L^2(mu)) ||grad g||_(L^2(mu)),
    lambda := log(1 + kappa/(2 D)).

*Proof.* (1) Bochner: for smooth u, grad(L u) = Lhat grad u - M grad u, where Lhat := Delta_rough - nabla_(grad V)
acts on 1-forms; on the product manifold the Levi-Civita connection splits, so Lhat maps the e-th component of a
1-form to the e-th component, and -Lhat >= 0 in L^2(mu) (it is nabla* nabla with the mu-weighted adjoint). Put
A := -Lhat + M >= kappa. (2) Spectral gap: if -L u = nu u with u not constant, then grad u != 0 and
A grad u = nu grad u, so nu ||grad u||^2 = <grad u, A grad u> >= kappa ||grad u||^2 and nu >= kappa. SU(2)^E is
compact and V smooth, so -L has discrete spectrum and is invertible on mean-zero functions. (3) Helffer-Sjostrand:
let u solve -L u = g - mu(g). Then Cov(f, g) = mu(f (-L u)) = mu(<grad f, grad u>), and grad g = A grad u, so
Cov(f, g) = mu(<grad f, A^(-1) grad g>). (4) Combes-Thomas: let phi(e) := dist(e, S_g), which changes by at most 1
between links of a common plaquette. Multiplication by exp(lambda phi(e)) on the e-th component commutes with Lhat
(step 1). So A_lambda := exp(lambda phi) A exp(-lambda phi) = -Lhat + M_lambda, where M_lambda has blocks
M_(e e') exp(lambda (phi(e) - phi(e'))). Hence ||M_lambda - M|| <= (e^lambda - 1) D = kappa/2 pointwise, and
Re <omega, A_lambda omega> >= (kappa/2) ||omega||^2, so ||A_lambda^(-1)|| <= 2/kappa on L^2(mu; T*). Finally
Cov(f, g) = mu(<exp(-lambda phi) grad f, A_lambda^(-1) exp(lambda phi) grad g>), with exp(lambda phi) = 1 on S_g
and exp(-lambda phi) <= exp(-lambda d) on S_f. QED

**Corollary UNI-2. PROVED GIVEN (c) and the OS reconstruction on file.** If along a trajectory M_j >= kappa_0 > 0 for
all j and all tori, then the lattice decay rate is at least lambda_j = log(1 + kappa_0/(36 c_H beta_j)), so the
physical rate lambda_j/a_j is at least of order kappa_0/(beta_j a_j), which tends to infinity because beta_j grows
like log(1/a_j). Every separated covariance of polynomially normalised matched observables tends to 0, and NT1 fails
as in Corollary UNI-1. So the curvature row (method 31) is closed in every form that is uniform in volume and coupling;
this is row 1229 Claim A, now proved. It remains open, and is not touched here, only in forms whose constant degrades
along the trajectory (multiscale forms, rows 957, 968) or that hold at one coupling (which needs a certificate,
row 1229 Step 2).

Step 2 done.

## Step 3. (CLASS) of (UNIV-K): HOLDS in a corrected form; two clauses of (MAPCONV) hold exactly (written 07:55Z)

Kind: closure of one sub-item of the ultraviolet carry (part (A) of Step 1.1); no seed. Source: YM4_1400.tex of the
Sussman-Alpoge repository (Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text), fetched
by URL at commit 2bc0658f91d2, where the file was added; it has 136637 lines, the count row 924 gives for the lead's
sa1400 copy, so the line numbers below are row 924's. Lines READ: 94030-94200 (fixed presentation, frame, weights,
recursion, bounds, Proposition rts-bounded-UV-tuning and its proof), 93440-93600 (spaces, transport, adapted norm,
Gaussian data), 93600-93640 (formation bounds), 93700-93770 and 93800-93860 (relative box, profile slope, backward
contraction), 59306-59350 (the transported pointing (hit:actual-transferred-pointing)).

**What row 924 asked.** (CLASS): along the segment of maps M^B_j + s'(M^A_j - M^B_j), s' in [0, 1], the bounds R5
and ||T_j|| <= q hold, so that the tuning proposition R6 (Proposition rts-bounded-UV-tuning, L94131-94184) holds
along the segment with constants independent of the horizon. Run A is d's regular trajectory from step 1, run B that
of pi d from step 0, relabelled so that step j of both acts on the same lattice; N = K - 1; same endpoint X.

**What R6's proof reads (READ, L94146-94184 with L93700-93860).** (i) the forward profile bound
||h_(j+1)||_(j+1,*) <= q H_* + B_n + C e_j <= H_*, which reads the one-step contraction (hrt:one-step-contraction),
||n_j||_(j+1,*) <= B_n and ||f_j|| <= C e_j; (ii) the profile-coupling slope, which reads ||D_h f_j|| <= C e_j and
||d_x f_j|| <= C k_j; (iii) the backward map (Phi x)_j = a_j + zeta + sum over l >= j of r_l, whose contraction reads
abs(d_x r_l) <= C k_l and ||D_h r_l|| <= C e_l with the slope, and whose position in the relative box
{x : abs(x_j - a_j) <= delta a_j} (L93714) reads only the size of sum over l >= j of abs(r_l), compared with
delta a_j/2 (L93826-93834); (iv) holomorphy of the maps on enlarged domains, and the ceiling (rts:profile-ceiling).

**Observation 3.1 (the frames differ by a bounded, summable amount). PROVED from (rts:frozen-frame) and
(hrt:Gaussian-data).** With b^A_l = b_(l+1) and b^B_l = b_l, a^A_j - a^B_j = sum over l = j..N-1 of
(b_(l+1) - b_l) = b_N - b_j, so abs(a^A_j - a^B_j) <= B_b (lambda_b^N + lambda_b^j) <= 2 B_b lambda_b^j.

**Lemma 3.2 (the transport and the adapted norms are the same for the two runs). READ, with one ARGUED step.**
T_(i,k) is "the physical transport of (hit:actual-transferred-pointing), with no new Gaussian integration" (L93487-
93490), and that formula (L59343-59346) is R(w) = sum over old anchors z of theta_y(xi z) r_z(B_xi(w)): tent
weights with xi = L^(i-k) and the classical field map from scale k to scale i. Both depend only on the blocking
between the two scales, on the fixed radius and rate "at every scale" (L93453-93456) and on the torus. ARGUED (the
classical map B_xi was not traced to its definition): neither depends on the depth below scale i or on the coupling
frame. So T^A_j = T^B_j on the common lattice, the spaces B_j and their norms coincide, and the adapted norm
(hrt:adapted-norm) (L93549-93555), built from T and the common N, is the same for both runs. If the ARGUED step
failed, Lemma 3.4 below covers the case sum over j of ||T^A_j - T^B_j|| <= tau.

**Proposition 3.3 ((CLASS), corrected form). PROVED from the READ lines and Lemma 3.2.** Keep the REAL frame of run B
fixed, a_j := a^B_j (cutoffs, fluctuation scaling and weights e_j, k_j are read from it), and write the interpolated
recursion as

    x_(j+1) = x_j - b^B_j - rtilde_j(s'),     rtilde_j(s') := s' (b^A_j - b^B_j) + (1 - s') r^B_j + s' r^A_j,
    h_(j+1) = T_j h_j + n_j(s') + f_j(s'),     n_j(s') := (1 - s') n^B_j + s' n^A_j,  f_j(s') likewise,

for s' in U_eps := {s' complex : dist(s', [0, 1]) < eps}. Then, after a floor increase that depends only on delta,
B_b, lambda_b, eps and the constants of R5, the conclusions of Proposition rts-bounded-UV-tuning hold for every s' in
U_eps, with constants independent of N; the tuned trajectory is jointly holomorphic in (H, zeta, s'); at s' = 0 it is
run B, and at s' = 1 it is run A.

*Proof.* Domains: by Observation 3.1 and a >= c X_0, the relative box of half-width delta a^B_j/2 around a^B_j lies
in both runs' enlarged coupling domains once 2 B_b <= delta c X_0/4; the profile balls are the same (Lemma 3.2). On
this common domain, for s' in U_eps, abs(1 - s') + abs(s') <= 1 + 2 eps, so each bound of (rts:derivative-bounds) for
the convex parts of rtilde_j, f_j(s') holds with C replaced by (1 + 2 eps) C (1 + C'/X_0): the weights of the two
frames satisfy e(a^A_j) <= (1 + C'/X_0) e(a^B_j) and the same for k, since the frames differ by at most 2 B_b and
e(t) = (log t)^m/t. Also ||n_j(s')||_(j+1,*) <= (1 + 2 eps) B_n, and T_j is the common transport, so
(hrt:one-step-contraction) holds verbatim. The extra term s'(b^A_j - b^B_j) is a constant in (x, h): it changes no
derivative, does not enter the profile equation, and adds at most (1 + eps) 2 B_b/(1 - lambda_b) to
sum over l >= j of abs(rtilde_l). So (i) and (ii) hold as in L94149-94163 with H_* chosen from (rts:profile-ceiling)
with (1 + 2 eps) B_n; (iii) holds since the backward correction is at most
abs(zeta) + C(1 + (log a_j)^(m+1)) + 4 B_b/(1 - lambda_b), which is below delta a_j/2 after the floor increase
(L93826-93834 with a larger constant), and the contraction constant is unchanged (L93847-93854). The fixed-point
iteration is locally normally convergent in (H, zeta, s'), since every map is affine in s' and holomorphic in (x, h);
this gives joint holomorphy. At s' = 1 the coupling recursion reads x_(j+1) = x_j - b^A_j - r^A_j, run A's own; run
A's tuned trajectory lies in its own box, hence (Observation 3.1) in the box used here, so by uniqueness it is the
s' = 1 trajectory. QED

*Why the correction.* Row 924's form interpolates the frame as well. Then either the frame is complex for
non-real s' (the account freezes real frames, L94071-94080 and L93604-93606), or R5's first bound
abs(r_j) <= C e_j fails for the interpolated remainder at small j, because abs(b^A_j - b^B_j) is of order lambda_b^j,
not of order e_j. Proposition 3.3 avoids both by keeping B's real frame and moving the increment difference into the
remainder; R6's proof needs only the summability of that constant term.

**Lemma 3.4 (if the transports differ). PROVED.** If T^A_j = T^B_j failed but sum over j of
||T^A_j - T^B_j||_(B_j -> B_(j+1)) <= tau with tau independent of K, put E_j := (1 - s')(T^B_j - T^A_j). Expanding the
product, ||prod over i = j..j+n-1 of (T^A_i + E_i)|| <= C_T lambda^n prod over i of (1 + C_T ||E_i||/lambda)
<= C_T exp((1 + eps) C_T tau/lambda) lambda^n. So the interpolated transports satisfy (hrt:transport-bound) with
C_T' = C_T exp((1 + eps) C_T tau/lambda), the adapted norm (hrt:adapted-norm) built from them gives
(hrt:one-step-contraction) with C_T', and Proposition 3.3 holds with H_* chosen from C_T'.

**Consequence for (MAPCONV).** Row 924's (MAPCONV) had four clauses: b and r, then T, n and f, then the
equivalence of the adapted norms. By Lemma 3.2 the transport clause and the norm clause hold exactly (T^A = T^B,
identical adapted norms; ARGUED in one step as stated). By R10 (L94530-94545, read in row 924) the b clause holds:
abs(b^A_j - b^B_j) <= 2 B_b lambda_b^j. What is left of (MAPCONV) is:

    (MAPCONV-F) on the common domain, sup abs(r^A_j - r^B_j) + ||n^A_j - n^B_j|| + sup ||f^A_j - f^B_j|| <= C lambda_0^j,

the convergence in depth of the Gaussian pointing and of the formation remainders between consecutive depths and
frames. OPEN: the account proves the analogue only for the scalar coefficients b_j, m_j. READ at L61186-61215
(lcf:Gaussian-weight-jet): it identifies m_j = (11/(3 pi^2)) log L + O(L^(-sigma j)) through Proposition
agc-actual-anisotropic-increment, while the zero-readout remainder q_(j,e) of the pointing's weight jet is only bounded,
||q_(j,e)|| <= C abs(e), with no decay in j. So the n clause is not in the account either. Not attacked further here.

**Status of (UNIV-K) after this step.** Open sub-items: (MAPCONV-F); (VAC-ID); (DENS-K) B1 and B2. (CLASS) is closed in
the form of Proposition 3.3, which is the form Proposition 4.4 of row 924 needs: its s'-derivative solves R11 with
sigma_j = -(b^A_j - b^B_j) - (r^A_j - r^B_j), exactly the derivative of rtilde_j. As Step 1 says, (UNIV-K) is the carry
only; it supplies no seed.

## Step 4. A block-size bound, the state after this row, and the result (written 07:57Z by date -u)

**Corollary UNI-3 (cube dynamics need cubes of nearly physical size). PROVED GIVEN Proposition UNI (a), (b).** Take
the cube heat bath of One Cube Estimate (B's Definition 62: all cubes x + [0, n)^4 of the torus, each updated at rate
one, so that B's form is n^(-4) times the form Ecal of Step 2 and BP(n, varpi) is Poincare with gamma = n^4 varpi).
For these blocks b <= 4n + 1, rho <= 4n + 3 and Delta <= (2n + 3)^4, so (a) gives a lattice rate at least
kappa >= min(1, n^4 varpi/(e^2 (2n + 3)^4))/(4n + 3), which is at least varpi/(e^2 5^4 n) for n >= 3 and varpi <= 1.
So if BP(n_j, varpi_0) holds along a trajectory and some normalised separated covariance of matched observables stays
above delta > 0 at physical distance r, then, with the normalisation of (b),

    n_j a_j >= varpi_0 r/(625 e^2 log(C' a_j^(-k-8)/delta)) (1 - o(1)),

so n_j a_j may tend to 0 at most like 1/log(1/a_j). In words: the cube side of any BP criterion must be within a
logarithm of the physical scale. B's Theorems 45, 66 and 84 take n_k a_k <= ell with ell physical, and this is the
other side of that choice. (The rate here is of the same order as B's m_* = 16 varpi/(625 e^2 ell); the proof is
independent of B.)

**State after this row.**

| Item | Before | After this row |
|---|---|---|
| (N-phys), the seed at the band (part (B) of Step 1.1) | OPEN, no attack on file | OPEN; no carrier or engine found beyond the record (Step 1.2) |
| Row 1229 Claim A: coupling-uniform dynamics or curvature gaps prove too much | ARGUED, RECALLED inputs | PROVED: Proposition UNI (a)-(c), Corollaries UNI-1, UNI-2; with the necessary rate gamma_j = O(a_j log(1/a_j)) and Corollary UNI-3 |
| (UNIV-K) sub-item (CLASS) | ARGUED (row 924) | PROVED in corrected form, Proposition 3.3 (real frame of run B kept; increment difference moved into the remainder) |
| (UNIV-K) sub-item (MAPCONV) | OPEN (row 924) | transport and norm clauses hold exactly (Lemma 3.2, one ARGUED step); b clause by the account's R10; left: (MAPCONV-F), OPEN |
| (UNIV-K) sub-items (VAC-ID), (DENS-K) B1, B2 | OPEN | OPEN, not attacked |

**Note for the lead (process; not a proof claim).**

1. This is the fifth Opus row in a row on the plain brief (rows 1212, 1219, 1225, 1229 and this one) to find no attack
   on the seed. Step 1.2 adds the dilute-defect-gas kind (Gopfert-Mack) to row 1229's table with its 4D status, and
   I found no other kind of engine.
2. Checks wanted (other provider): Proposition UNI (a) and (c), and Proposition 3.3 with Lemma 3.2. The ARGUED step of
   Lemma 3.2 (the classical map B_xi of (hit:actual-transferred-pointing) does not read the depth below the old scale)
   needs the definition of B_xi traced in the account; Lemma 3.4 makes Proposition 3.3 independent of it, given a
   summable transport difference.
3. For the account text on a Mini worker: YM4_1400.tex at the Sussman-Alpoge commit 2bc0658f91d2 (raw GitHub URL,
   repository root) has 136637 lines and reproduces the line numbers of row 924; at their HEAD the file is under YM4/.
4. (MAPCONV-F) is the core of the regular part of (UNIV-K): the account proves depth convergence at rate lambda_0^j
   for the scalar increments b_j, m_j only ("The actual comparison proves", L94539-94545); the full Gaussian pointing
   n_j and the formation remainders r_j, f_j need the same convergence between consecutive depths and frames.

No numeric run was made. No subagent was used. Inputs read are listed in Steps 0 and 3.

RESULT: Row 1237 (Claude Opus 5.5 max, Mac mini worker 2, 07:19Z-07:57Z by date -u; author only, checked by no one; no numeric run). The mass gap of four-dimensional SU(2) Yang-Mills is NOT proved and nothing in the chain is disproved; (N-phys), the seed at the band, stays OPEN with no carrier or engine found beyond the record (Step 1.2 adds the dilute-defect-gas kind, Gopfert-Mack, with its 4D status). PROVED by hand: Proposition UNI (a) a volume-uniform Poincare constant gamma for any bounded-range heat bath of a lattice gauge measure gives covariance decay at lattice rate min(1, gamma/(e^2 Delta))/(b + 2) (single link: Delta = 19); (b)-(c) and Corollaries UNI-1, UNI-2: along a trajectory, a coupling-uniform Poincare constant or Bakry-Emery bound Ric + Hess V >= kappa (Helffer-Sjostrand formula with a Combes-Thomas conjugation) makes every separated correlation vanish, so NT1 fails; this proves row 1229's Claim A and gives the necessary rate gamma_j = O(a_j log(1/a_j)); Corollary UNI-3: a BP cube criterion needs cube side n_j a_j at least of order 1/log(1/a_j). PROVED from the account (YM4_1400.tex, Sussman and Alpoge with Claude and Codex): (CLASS) of (UNIV-K) in a corrected form (Proposition 3.3: keep run B's real frame, move the increment difference b_N - b_j into the remainder); the transport and norm clauses of (MAPCONV) hold exactly (Lemma 3.2, one ARGUED step; Lemma 3.4 covers a summable difference). OPEN: (N-phys); (UNIV-K) in (MAPCONV-F), (VAC-ID), (DENS-K) B1-B2; the account's premises (T0 chain). Output library/gap-mini-solve-w-opus.md.
