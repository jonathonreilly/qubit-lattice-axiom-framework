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
- Curvature (Langevin) forms, row 1229 Claim A's first case: ARGUED, not proved here. The same proof works once the
  Langevin semigroup on SU(2)^E has a finite-speed bound sup over U of abs(grad_e P_t g) <= ||grad g|| abs(S_g)
  (C beta t)^D/D! for links e at distance D from S_g (a Lieb-Robinson bound with speed proportional to the
  plaquette coupling). With it the lattice rate is of order kappa_curv/(C beta_j), the physical mass at least
  c kappa_curv/(beta_j a_j), which still diverges since beta_j a_j -> 0. The missing piece is that bound; I did not
  write it.

**Rule 0a.** The covariance bound is a standard theorem for spin systems (sources above). In the lane, the same
conclusion is row 1229 Claim A (ARGUED, RECALLED inputs) and B's Theorem 66 with fixed n (row 1218, unchecked). I
found no file in `library/` that writes the proof (grep for "finite speed", "Lieb-Robinson", "trivial continuum",
"prove too much" in `library/gap-*.md`: hits are row 1032 B2, which is the exact Lieb-Robinson cone of the transfer
step, not of a heat bath; row 1229 Claim A; and row 1224's Lemma 6.2, a finite-speed estimate for B's chain at one
cube size used in another argument). So the proof is new to the lane; the statement is not new in the literature.

Step 2 done.

