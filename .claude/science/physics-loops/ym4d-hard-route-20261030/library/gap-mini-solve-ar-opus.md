lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T02:55Z

# gap-mini-solve-ar-opus: an attack on the SU(2) four-dimensional mass gap

Queue row 1291 of `FINISH.md`. Worker: Claude Opus 5.5, max effort, Mac mini worker 3.
Pinned commit: 404e2e322. Started 2026-11-20T14:55Z.

Labels: PROVED (a complete written argument here or in a cited, checked library file),
ARGUED (an argument with a named gap), GUIDE (heuristic or numeric orientation only),
OPEN (not established).

## 0. Status of this file

All steps done; RESULT at the end (2026-11-20T15:40Z by date -u). Checked by no one. No numeric run, no subagent.

## 1. Briefing digest (what this row starts from)

Read at the pin: `GOAL.md`; `FINISH.md` rules, How we work, Working efficiently, row 1291;
`parts/gap.md` State of attack, route registry, test table, price (L1-104, L223-330);
`library/prior/gap-onebound-read-sol.md` in full (row 1218, gpt-6.1-sol reading);
the RESULT lines of the solve, laptop and owner rows among 1217-1290 (mini-solve s to ap, laptop-solve 1-3, rows
1273, 1274, 1285, 1286, astra solve 29-32, fresh, fresh2); row 1259 Step 2 (`gap-mini-solve-ah-opus.md` L71-172);
row 1278 2.3; `gap-crux-restate.md` L29-124; `gap-council-op-astra.md` Section 2; row 1135's RESULT; and, at the branch
head fetched 15:20Z-15:35Z, the opening steps of rows 1284 and 1293 and check 1288 Sections 6-7. Nothing in this
section is new; it fixes the starting point.

1. The crux, as the lane states it: (N-phys) of row 1161 (`gap-solve9-astra62.md` 146-148), restated in
   row 1218: there are L and j_0 such that for every j >= j_0 some integer u_j with 3 <= u_j <= n_j/K has
   s_{+,j}(u_j; n_j^3) = Tr_{H_+} U_j^{u_j} - 1 <= 1/2 (centre-neutral thermal sum of the periodic spatial
   cube of physical side L at physical time u_j a_j, uniform in the cutoff). Equivalent forms on file:
   (W) with (BDD-Delta) and (Z-UNB) (row 720, Theorem ZD-c); (SL)/(RR) of row 1258 at one coupling.
2. Bhattacharjee et al. (preprint 202611.1282, authors' archive copy) prove a conditional ascent from the
   full-thermal one-scale seed (A-B*) to a transfer gap; the seed at weak coupling is open in their text.
   Their B paper (Hexagon 2610.00341v7) proves BP(n,1/2) for very coarse straight-path block variables of
   Wilson SU(2) at growing beta_W <= k+2 on tori of size R <= exp(2^k/(17k)) (Corollary 166), by
   convolution damping of non-trivial representations; the ascent (H2)/(S) is open. Zeng's tunnelling package
   is conditional; row 1251 found its (TUN) to be the gap itself.
3. Route registry (row 998): RA, RB, RC, RF blocked-equivalent; RE blocked-local; RG retired; RD survives as
   a weaker statement. Methods 1-36 set aside (parts/gap.md L52-79). The theorem-grade tests for a carry
   tool are compact U(1), the free photon, a product with a massless factor, Theorem D2 (no supremum over
   tilts), Lemma SHEET (no uniformity over coupling fields), and (row 1140) no uniformity over backgrounds
   at large b.
4. The recent Opus rows (1228-1280) screened about sixty ideas for the seed and found none off the record;
   most then worked side items of the one-cutoff carry (rows 1233, 1248, 1255, 1256, 1260, 1264, 1267, 1268,
   1275, 1278, 1280). Row 1278: at the window coupling the glueball correlation length is about one lattice
   spacing, and every published rigorous method stops roughly ten times lower in beta; Proposition CA-FAIL
   rules out criteria uniform over boundary data.
5. Owner direction for this row: horsepower on the crux; a plain brief ("solve the problem").

## 2. How best to attack it (judgement; ARGUED unless cited)

**2.1 Where the problem stands.** By the record (Section 1, items 1-4), and modulo the open inputs of the
one-cutoff carry, the Jaffe-Witten gap for SU(2) needs one infrared input: a seed of Wilson SU(2) at one weak
coupling, that is, a uniform gap of the periodic cubes plus a count of light states (row 1259, Corollary CD1),
at a size of many correlation lengths. In the form (N-phys) with K = 512 this is a pressure bound deep in the
confined phase (row 1284, Step 0 item 2, read at the branch head). It is the lattice mass-gap problem at one coupling. No hand method in
the lane or in the literature read here reaches it.

**2.2 What the 2D proofs show, and why the port stops (GUIDE; from the RESULT lines and `parts/gap.md` entries of
rows 1009-1016, 1140, 1243-1249, and row 1284's citation of rows 1072-1074, which I did not read).**
The posted 2D O(N) proofs (OpenAI; Ding, Huang and Yang; unrefereed) reach the one-coupling statement by a
bound that holds at every coupling, with a non-optimal exponential rate. They get it from a stiffness
iteration whose gain is a tadpole (the curvature of the target sphere), proved uniformly over pins and
strengths. In 4D gauge theory three facts on file block the port:
(a) the class "uniform over pins" does not close: two pinned slices make a 3D O(4) magnet (Proposition CA-FAIL,
rows 1072-1074), and coupling fields make critical members (Lemma SHEET, row 996);
(b) the gauge theory has no rigid non-abelian twist on its integration variables (CEN+, row 1016; Lemma DR,
row 1273);
(c) the 4D one-loop gain is a two-propagator bubble whose sign comes from the paramagnetic spin term; one-sided
tools (Jensen with a flow of bounded strength) keep only the screening part (row 1244 Proposition 2.3; row 1249).
In my own terms, (c) is this: in -log(Z(B)/Z(0)) the anti-screening part is minus half a variance of the
spin coupling, a second cumulant, and Jensen drops every cumulant beyond the first. A flow can restore it only
if the flow is long-range, which is an RG step through the band.

**2.3 Decision.** A further screen of mechanisms is named waste on file (row 998 9.5; by the count in rows 1284 and 1293,
about sixty families are screened on file with none off the record). I checked eight more names against the record before deciding
(Yamazaki-Yonekura reduction and adiabatic continuity: Route T, rows 842, 862; spectral independence, entropy
factorisation and localisation schemes: `gap-mini-solve-o-fable.md` L55 with `prior/gap-lit-tiltcov.md` Step 3,
"each is an engine; its local input at block scale is a one-scale seed of kind (K-one)"; Bakry-Emery and Polchinski
flow: method 31; Gribov region: the screen table of `gap-mini-solve-am-opus.md` L32; the Kogut-Susskind ground-state
transform: row 1281, Lemma V; Nielsen-Olesen and gluon paramagnetism: row 1244; Bogoliubov and single-mode bounds: double commutators in rows 1207
and 1236, and `gap-tiltproof-max.md` L339; the count half (TR): row 1259). All are on file. So I do not run another screen.

I also tested whether the count half is free given the gap (a counterexample or a proof would settle row 1259's
open sentence "the implication uniform gap implies a seed itself stays OPEN"). Result, ARGUED: neither direction
is reachable by soft tools. (i) A proof needs the low-lying states to be particle-like: RP, locality and a gap on
every box shape give nothing per unit volume, because a chessboard or doubling bound always reintroduces the
Casimir term t c(Y) of a smaller box (Section 3.0 below writes this out). (ii) A counterexample needs exponentially
many states at bounded energy above a unique gapped vacuum; the known sources of such counts (subsystem
symmetries, fracton and topological sectors) come with degenerate vacua, so they lose the uniform gap. I record
this and stop there.

**What the rest of the row does.** The infrared seed stays OPEN here. My plan was to spend the rest of the row on a
closable carry input that no row owns and whose sources are on this machine. The rule-0a check (Section 3.2) found
every such input owned by the parallel rows 1284 and 1293 or blocked, so I took none. Sections 3.0 and 3.1 write out
the two seed-side questions I had tested while deciding.

## 3. Work done

### 3.0 The count half: why soft bounds cannot make it decay (Lemma CR, PROVED; consequence ARGUED)

Notation of row 1259, Lemma CD (`gap-mini-solve-ah-opus.md` L80-L127): F(t, X) = log Z(t, X) for a time extent t
and a spatial torus X; Lambda_1(X) = lim_t F(t, X)/t = log lambda_0(X); g(t; X) = F(t, X) - t Lambda_1(X) >= 0;
f_infinity = lim F(T)/|T|; sigma_3(t) = lim over X of g(t; X)/|X|. Put

    c(X) := Lambda_1(X) - f_infinity |X|,        Delta(t, X) := F(t, X) - f_infinity t |X|.

**Lemma CR (PROVED; elementary; Claude Opus 5.5, checked by no one).** For every spatial torus X and every t >= 1:
(a) c(X) >= 0 and Delta(t, X) = t c(X) + g(t; X), both terms non-negative;
(b) for every spatial torus Y, sigma_3(t) <= Delta(t, Y)/|Y| = [t c(Y) + g(t; Y)]/|Y|;
(c) for the cube Y = (y, y, y), c(Y) = sigma_1(y) + y sigma_2(y) + y^2 sigma_3(y), so c(Y) >= y^2 sigma_3(y).

Proof. (a) Lemma A (a) of `gap-crux-restate.md` L37 (from reflection positivity) gives F(kT) <= k^4 F(T) for every
torus T and integer k >= 1 (all four sides multiplied by k), so F(kT)/|kT| <= F(T)/|T|. As k -> infinity the left side
tends to f_infinity (Lemma CD (b)). So F(T)/|T| >= f_infinity for every torus T. Hence F(t, X) >= f_infinity t |X| for all t; divide by t and let t -> infinity:
Lambda_1(X) >= f_infinity |X|. The identity is the definition of g. (b) Let X = kY (each spatial side times k). Lemma A
(a) in the three spatial directions gives F(t, kY) <= k^3 F(t, Y). Write both sides with Lambda_1 and g:
g(t; kY) <= k^3 g(t; Y) + t [k^3 Lambda_1(Y) - Lambda_1(kY)] = k^3 g(t; Y) + t [k^3 c(Y) - c(kY)], since the f_infinity
terms cancel (k^3 |Y| = |kY|). Drop -t c(kY) <= 0 by (a), divide by |kY| = k^3 |Y| and let k -> infinity; the limit
defining sigma_3 may be taken along X = kY (Lemma CD (b)). (c) By (a), D(y) = Delta(y, Y) = y c(Y) + g(y; Y); compare
with (CD), D(y) = g(y; Y) + y sigma_1(y) + y^2 sigma_2(y) + y^3 sigma_3(y). QED

**Consequence (ARGUED from Lemma CR).** Every bound on the thermal pressure sigma_3(t) obtained by tiling with a smaller
box Y through reflection positivity (the only extensive tool on file; Lemma CD (b) is the case Y = X) carries the term
t c(Y)/|Y| >= (t/y) sigma_3(y). A uniform gap m_0 of Y shrinks g(t; Y) like e^(-(t-s) m_0), but the Casimir term grows
linearly in t. So for t > y the tiled bound is weaker than the monotone bound sigma_3(t) <= sigma_3(y) already in
Lemma CD (d). The count needs c(Y) itself to be small. Since c(Y) <= D(y)/y by (a), that is a statement of seed size at the size of
Y (Corollary CD2 gives it from a seed; nothing on file gives it without one). This makes
precise, in one inequality, row 1259's verdict that the count is not easier than the gap (row 1259 L150-166, item 2,
"an additive gain that vanishes per unit volume"). It is found again in substance; the form (b) with the Casimir term is
the only addition.

**The other direction (ARGUED).** A counterexample in the class (reflection positive, hypercubic, local, compact) to
"uniform cube gap implies a seed" needs exponentially many states in the side at bounded energy above a unique gapped
vacuum, because by (a) and (CD) D(a)/a < m_0/64 fails only if g(a; a^3) or a c(a^3) grows linearly in a. The sources of
such counts that I know (planar subsystem symmetries, fracton and topological sectors) have degenerate or nearly
degenerate vacua on the torus, which breaks the uniform gap; local perturbations cannot lift a sector that is locally
indistinguishable from the vacuum. For a free gas of particle species with energies at least m_0 and finite multiplicity below
each energy, every term of the thermal pressure carries a factor e^(-t m_0), so sigma_3(t) <= e^(-(t - t_0) m_0)
sigma_3(t_0) for t >= t_0 and (TR) holds; for interacting particle-like spectra this is a heuristic, not a proof.
I found neither a proof nor a counterexample; row 1259's open sentence stands.

### 3.1 The paramagnetic term as a second cumulant: a one-sided bound exists, but it has no 4D consumer

Section 2.2 (c) says Jensen bounds keep only the first cumulant. This section asks whether the obstruction is
about one-sidedness as such. Answer: no; a one-sided bound with the anti-screening sign exists for curvatures of the
free energy, but it does not open a route.

**Lemma PV (PROVED; elementary; Claude Opus 5.5, checked by no one).** Let S_lambda be a family of log-weights on
SU(2)^E of the periodic torus Z_N x Lambda (N even), smooth in lambda, Z(lambda) = int exp(S_lambda) dU, and
F(lambda) = -log Z(lambda). Then
(a) F''(lambda) = -<S''_lambda>_lambda - Var_lambda(S'_lambda).
(b) Suppose the measure exp(S_lambda) dU / Z(lambda) is reflection positive for every time reflection of the torus
(through sites and between sites). This is a hypothesis. It holds for the Wilson action (Osterwalder and Seiler),
and the same argument covers fixed group elements inserted in the plaquette traces when the insertions are invariant
under time translations and time reflections; I do not prove that extension here. Suppose also that S'_lambda = sum over t in Z_N of V_t, where
V_t = tau_t V_0, V_0 depends only on the links of the closed slab between times 0 and 1, and V_0 is invariant under the
reflection t -> 1 - t. Then Cov(V_0, V_s) >= 0 for 0 <= s <= N - 1, hence
    Var(S'_lambda) >= N Var(V_0),   and   F''(lambda) <= -<S''_lambda> - sum_(|s| <= T) N Cov(V_0, V_s)   for every T.

Proof. (a) (log Z)' = <S'> and (log Z)'' = <S''> + <S'^2> - <S'>^2. (b) For 1 <= s <= N - 1, the reflection
theta_s: t -> s + 1 - t (mod N) is a symmetry of the torus; its fixed planes are t = (s+1)/2 and t = (s+1)/2 + N/2, of
the same type because N is even. The slab [0, 1] lies in the half-torus between (s+1)/2 - N/2 and (s+1)/2, since
1 <= s <= N - 1. By the symmetry of V_0, theta_s V_0 = tau_s V_0 = V_s. Reflection positivity applied to
G = V_0 - <V_0>, which is supported in that half, gives <G theta_s G> >= 0, and <theta_s G> = 0, so
Cov(V_0, V_s) = <G theta_s G> >= 0. By translation invariance Var(sum_t V_t) = N sum_(s in Z_N) Cov(V_0, V_s); keep the
s = 0 term or any subset, since all terms are >= 0. QED

**Reading.** F'' is the stiffness of the free energy against the background parameter (a twist, or a background field
on a stack of plaquettes). Lemma PV (b) bounds the stiffness from ABOVE by single-slab static quantities: the
seagull term -<S''> minus a positive part of the paramagnetic second cumulant. That is the anti-screening direction, and it
is rigorous at every coupling. So Section 2.2 (c) is a statement about free-energy bounds of Jensen type, not about
every one-sided bound. The identity (a) is standard, and exact Hessian identities of this kind are on file (row 1228
Lemma P2; row 1244 Lemma 2.1 splits the twist stiffness exactly for every linear flow; I did not check that its
no-flow case is (a)); positivity of time covariances by reflection positivity is a standard tool used on
file (for example `gap-d2-inputs.md`, Lemma RP); its use in (b) to bound a stiffness from above I did not find by grep
("second cumulant", "superadditiv", covariance with reflection positivity in `library/gap-*.md`), so I count Lemma PV
as found again in substance and claim nothing new for it.

**Why it opens no route (ARGUED).**
(i) Size. In one-loop SU(2) the running of the stiffness at scale L is a logarithm collected from time separations
between the lattice spacing and L (the spin bubble of row 1244). The truncation at a fixed T keeps the sign and the
power-law part that cancels against the seagull (gauge invariance), and drops the part of the logarithm from scales
T to L. To keep it, T must be of order L, so the bound reads the actual correlations of the stationary law at all times
up to L. At the band that is the unknown. This is the Hamiltonian form of row 1249's finding that a flow must be
long-range to keep the logarithm.
(ii) Consumer. In 2D a small stiffness becomes mixing through a class that is uniform over pins (rows 1009-1010). In
4D that class does not close (Proposition CA-FAIL, rows 1072-1074, as cited by row 1284; Lemma SHEET, row 996), and no consumer on file
turns a stiffness number into a seed: (SEED), (N-phys), (W), (A-B*) and BP read free energies, thermal sums or
relaxation, not one curvature of F. A stiffness bound would need its own consumer, which is the open step "small
effective coupling at one scale implies a seed" in another form.
(iii) Selectivity. Lemma PV holds for compact U(1) and for the free photon too. It becomes selective only through
a lower bound on Var(V_0) (or on the truncated sum) that beats the U(1) value, which is again a statement about the
stationary law at the band.

### 3.2 Rule 0a and the parallel rows (record, 2026-11-20T15:20Z-15:35Z by date -u)

Before choosing a carry input I fetched the branch head and read the rows running beside this one. Row 1284
(`gap-mini-solve-aq-opus.md`, worker 1) took (U-dom) of row 1280 and the connectedness clause of Lemma H2' (row 1278
2.3). Row 1293 (`gap-mini-solve-as-opus.md`, worker 2) took the parity envelope (PE) of row 1280. The other open carry
inputs are blocked here or are not session-sized: (E0)-(E6), (E+) and `9.1:prop-blind-site-expansions` read Balaban's
CMP 116, which is not on this machine (check 1288 records the publisher's subscription page); (V9) needs an identity
attaching the account's chosen section 9.1 masses to the physical bare densities, which check 1288 shows the account
does not supply (its counterexample to row 1275's reading N2; check 1288 section 7 item 3); (DET)'s open inputs are
pr-lay W (an import of the hard-core lane, `pr-lay.md` section 2) and the normalisation (r4) (rows 993-994). So I took
no carry input, to avoid a duplicate attack, and spent the row on the two seed-side questions of Section 3.0 and 3.1.

## 4. Status

| Statement | Label | Where |
|---|---|---|
| Jaffe-Witten mass gap for 4D SU(2) | OPEN, not proved here | - |
| The infrared seed ((N-phys), or the seed at one weak coupling: uniform cube gap plus the count (TR)) | OPEN; no route off the record | Section 2 |
| Lemma CR: Delta(t, X) = t c(X) + g(t; X) with c >= 0; sigma_3(t) <= Delta(t, Y)/abs(Y); c(y^3) = sigma_1 + y sigma_2 + y^2 sigma_3 | PROVED (elementary, from Lemma CD and Lemma A); checked by no one; found again in substance (row 1259 item 2) | 3.0 |
| Tiling bounds on the thermal pressure cannot decay (the Casimir term of the smaller box returns with factor t) | ARGUED from Lemma CR | 3.0 |
| "Uniform cube gap implies a seed" in the class | OPEN; neither proof nor counterexample found | 3.0 |
| Lemma PV: F'' = -<S''> - Var(S'); reflection positivity gives Var(S') >= N Var(V_0) and the truncated upper bound on the stiffness | PROVED (elementary); checked by no one; found again in substance (exact Hessian identities of rows 1228, 1244; reflection-positive covariance positivity of `gap-d2-inputs.md`) | 3.1 |
| Lemma PV opens no route: the truncation drops the logarithm from scales T to L; no 4D consumer turns a stiffness into a seed; not selective by itself | ARGUED | 3.1 |
| Parallel rows 1284 and 1293 own (U-dom), the H2' connectedness clause and (PE) | record | 3.2 |

**Credits.** The reductions used in Sections 1-2 are the lane's (rows cited inline). Published work read through
the lane's notes: Ethan Sussman and Levent Alpoge's complete account (with Claude and Codex as authors of its text),
after Balaban (CMP 89-122); Bhattacharjee, Bhattacharya, Lockwood, Romanov, Sessford and Singha Roy (preprint
202611.1282 and Hexagon 2610.00341v7) and Zeng (Hexagon 2611.00543, 2611.00492), as read in row 1218; the posted 2D
O(N) proofs of OpenAI and of Ding, Huang and Yang (arXiv:2611.04908), as read in rows 1007-1012; Osterwalder and
Seiler for reflection positivity of lattice gauge theories; Nielsen and Hughes for the one-loop paramagnetic split
(as recalled in row 1244). No source was read directly in this row.

**For the lead.** This row adds no closure on the critical path. Its use is negative and bounded: the count half
cannot be made to decay by tiling bounds (Lemma CR), and the paramagnetic sign is not by itself the missing tool
(Lemma PV), because the logarithm lives at all scales up to L and no 4D consumer reads a stiffness. Both are found
again in substance. The recommendation of row 998 9.5 stands; on this evidence, further plain-brief seed rows by this
model family are unlikely to add closures until a new engine or a new source appears.

RESULT: Row 1291 (Claude Opus 5.5 max, Mac mini worker 3, 14:55Z-15:40Z by date -u; author only, checked by no one; no numeric run, no subagent): the Jaffe-Witten mass gap of four-dimensional SU(2) Yang-Mills is NOT proved and nothing is disproved; the infrared seed (uniform cube gap plus the count at one weak coupling, equivalently (N-phys)) stays OPEN with no route off the record (eight more names checked against the record, all on file), and no carry input was taken because rows 1284 and 1293 hold (U-dom), the H2' connectedness clause and (PE) while the rest need CMP 116 or the account's missing normalisation identity (check 1288); PROVED, elementary, found again in substance: Lemma CR (Delta(t, X) = t c(X) + g(t; X), and any tiling bound on the thermal pressure carries the Casimir term t c(Y)/abs(Y) >= (t/y) sigma_3(y), so the count cannot be made to decay by reflection-positive tiling) and Lemma PV (F'' = -<S''> - Var(S'), with Var(S') >= N Var(V_0) by reflection positivity, a rigorous anti-screening-sign upper bound on a stiffness that drops the logarithm from scales T to L and has no 4D consumer); OPEN: the seed, "uniform cube gap implies a seed" in the class, the carry inputs listed in check 1288, the mass gap. Output library/gap-mini-solve-ar-opus.md.
