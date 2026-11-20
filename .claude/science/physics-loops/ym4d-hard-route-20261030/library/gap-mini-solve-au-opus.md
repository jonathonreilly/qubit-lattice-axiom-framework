lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T04:32Z

# gap-mini-solve-au-opus (row 1295): four-dimensional SU(2) Yang-Mills mass gap, plain brief

Started 2026-11-20T16:32Z (date -u) on the Mac mini Claude worker 1, branch claude/ym4d-hard-route pinned at e32c8d919.
Model: Claude Opus 5.5, max reasoning. Labels: PROVED, ARGUED, GUIDE, OPEN. Status: finished 2026-11-20T17:09Z (date -u); author only,
checked by no one; no numeric run (none was needed: every number is hand arithmetic); no subagent.

## Step 0: record read (2026-11-20T16:34Z, date -u)

Read at pin e32c8d919: `GOAL.md` in full; `FINISH.md` L1-84, L299-350 and this row (L1376, row 1295); rows 1301-1303 (L1382-L1384:
the owner's tiling and positivity directions, run by rows 1301-1304 elsewhere); the OPEN clauses of the RESULT lines of rows
1259-1293; `parts/gap.md` L8-51 (state of attack, at an older pin); `library/prior/gap-onebound-read-sol.md` in full (row 1218:
Bhattacharjee, Bhattacharya, Lockwood, Romanov, Sessford and Singha Roy (A, B); Zeng Chunping (C)); the heads of the sibling
files of rows 1294 (`gap-mini-solve-at-opus.md`, the one-cutoff carry's (H-an'), (H-tail)) and 1296 (`gap-mini-solve-av-opus.md`,
the carry's normalisation identity). `library/open-core.md` registers no gap-lane item (grep "gap", "seed", "N-phys": one
unrelated hit, L524).

State, in one paragraph. The lane reduces the Jaffe-Witten gap for Wilson SU(2) to an infrared datum at one coupling in the
crossover band ((N-phys) of row 1161; (W) of row 998; (SL)/(RR) of row 1258; A's thermal window (A-B*) is a stronger full-trace
form, row 1218) plus an ultraviolet carry to finer cutoffs built on Balaban and on Sussman and Alpoge's account. Every plain-brief
row since 1188 ends with the infrared datum OPEN and "no route off the record". Siblings now own: the carry inputs (rows 1294,
1296), tilings (1301, 1302), the positivity object (1303, 1304), the astra chain (1298).

## Step 1: how best to attack it, and the choice made here (2026-11-20T16:59Z, date -u; judgement, ARGUED)

**Repo search (rule "Repo first"; this folder only).** Before choosing, every candidate mechanism I generated was grepped
over `library/gap-*.md`, `library/prior/gap-*.md` and `parts/gap.md` (file counts in brackets). All are on file:
Tomboulis decimation [111] (its one open obligation (TB)_n gives the flux half only, row 1025 L241, row 1296 L53);
vortex free energy [42], Tomboulis-Yaffe [31], Mack-Petkova [29]; Gribov [33], Zwanziger [19], O'Neill [19], Singer [30];
Bakry-Emery [109], Ricci [59], hypercontractivity [40], log-Sobolev [90]; OSSS [8] ("needs FKG, absent for SU(2)", row 839;
A8 of row 1031 FAILS); Duminil-Copin [24], sharpness [60]; Dobrushin-Shlosman [50], complete analyticity [25]; Polchinski
[46], Bauerschmidt [42], stochastic localization [6], spectral independence [9]; Langevin [109], stochastic quantization [7];
icosahedral [41], finite subgroup [61]; Higgs [98]; instanton [43]; Kogut-Susskind [27], spin network [21], Perron-Frobenius
[30]; trace anomaly [22], interaction measure [15], (VIR-log) [22] (row 708 L166-172: the coupling-continuity route stops at
(DEF_K); row 1281 re-found it). Terms with 0 hits: "Weitzenbock", "Witten-Veneziano", "Seiler-Stamatescu", "approximate
tensorization", "ultracontract", "Menshikov", "cluster algorithm"; none of them names a route the record lacks (each is a
variant of a tool on file: Bochner [25], topological susceptibility [2], entropy factorization [2], Aizenman-Barsky [5]).

**Judgement (ARGUED).** The record reduces the gap to one datum at one coupling in the crossover band ((N-phys); (SL)/(RR)
of row 1258, `gap-mini-solve-ag-opus.md` L230-L256 and L342-L380; the published full-trace window A-B* of row 1218), plus
the ultraviolet carry. Every mechanism class I could name is on file with its failing step, or is being run now: tiling
(rows 1301, 1302), a positivity object (rows 1303, 1304), the thermal deletion chain (row 1298), the carry (rows 1294,
1296). Two quick kill tests of the chain's datum found nothing: (i) the four slab geometries of (4.1) have all sides at
least N (row 1258 L242-L246), so no thin periodic side lets a centre sector set by a boundary slice survive the slab;
(ii) a Z_2 magnetic flux carried by a boundary slice is not conserved through a slab of physical thickness in a confining
theory (it is in compact U(1), where it makes eta_* grow like beta: the datum is selective as it should be). So I do not
claim a route to the seed, and I do not attack it blind a fifteenth time.

**Choice.** One unowned item with a live consumer: the published thermal ascent of Bhattacharjee, Bhattacharya, Lockwood,
Romanov, Sessford and Singha Roy (A of row 1218): Proposition 7.57 (A-B** <=> A-B*), Theorem 7.56 (propagation of A-B* to
larger boxes) and Theorem F (full periodic transfer gap, one vacuum). Consumers: the gpt-6.2-astra chain targets A-B**
explicitly (row 1290 L425: "To use the published full thermal criterion, one needs J(1) <= y_0 V(s)/(2(96 T_0)^3)"), and
row 1224 checked A's slab route (Theorem B), not this ascent (its RESULT lists Lemmas 11.4-11.7, Theorem 11.8, App. G,
Lemma 6.2-Theorem B). Grep (`grep -l -F "7.56"`): A's Theorem 7.56 is cited in rows 1218, 1220 (`gap-mini-solve-p-fable.md` L197), 1224 (`gap-mini-solve-q-fable.md` L54, L295) and 1248 (`gap-mini-solve-ab-opus.md` L28), never checked; row 1224 L292-L295 proposes exactly this item ("(c) a check of A's full-thermal ascent (Theorem 7.56 and Theorem F)") and does not do it. Plan: (2) fetch A's
authors' copy (Zenodo 24147967, as row 1218 did) into a new scratch folder; (3) check 7.57, 7.56 and F line by line and
compare with the lane's own engine (Theorem S, `gap-crux-restate.md`); (4) the link from the chain's datum (RR) of row
1258 to A-B**, so that both chains aim at one statement; (5) verdicts, RESULT. If the ascent FAILS, the astra chain's
target changes; if it HOLDS, the lane has a second, published engine for the same datum, checked here.

## Step 2: source (2026-11-20T17:00Z, date -u)

A = Deep Bhattacharjee, Ushashi Bhattacharya, James Montgomery Lockwood, Tristan Romanov, Ikailo John Sessford and
Sanjeevan Singha Roy, "The Yang-Mills Mass Gap from One Bound at One Scale", authors' archive Zenodo record 24147967
(version 5.0.0, publication date 2026-11-12), file `papers/4Y-MPaper.pdf` (157 pages), the copy row 1218 read; fetched
into a new scratch folder, text extracted with PyMuPDF, nothing copied into this checkout. Byte identity with Preprints.org
202611.1282 v1 is not verified (as in row 1218). Page numbers below are PDF pages. Located: Lemma 7.51 (cost of a cut,
p. 55), Proposition 7.52 (extensivity at a fixed time, p. 56), Theorem 7.53 (ascent in time, with a gap, p. 56-57),
Theorem 7.54, Corollary 7.55 (p. 57), Section 7.11 and Theorem 7.56 (ascent without a gap hypothesis, p. 58-59),
Theorem F (p. 59-60), Propositions 7.57, 7.58 and Theorem 7.59 (p. 60-61). Step 3 checks 7.51, 7.52, 7.56, 7.57 and F.

## Step 3a: Theorem 7.56 of A, checked given its inputs (2026-11-20T17:01Z, date -u)

Notation of A (p. 39-61): for a spatial torus s = (s_1, s_2, s_3), Z(s, T) is the Wilson partition function of the
four-torus s x T; lambda_0(s) the top eigenvalue of the time transfer matrix T_s, E_0(s) = -log lambda_0(s);
Zcal_s(T) = Z(s, T) e^(T E_0(s)) = sum_i r_i^T with r_i = lambda_i/lambda_0 in [0, 1] (nonnegative by A's Lemma 7.3(vii));
D_s(T) = Zcal_s(T) - 1 = sum_(i >= 1) r_i^T; V(s) = s_1 s_2 s_3; T_i = 2^i T_0.

**Statement (A, Theorem 7.56, p. 58-59).** T_0 >= 3 an integer and (B*): log Zcal_s(T_0) <= gamma V(s) for every s with all
sides in [2 T_0, 48 T_0), with y_0 = 2 gamma (96 T_0)^3 <= 1/20. Put y_(i+1) = 16 (e^(y_i) - 1)^2, u_0 = 16.83 y_0. Then
(a) y_i <= 1/20, 16.83 y_i <= u_0^(2^i), and log Zcal_t(T_i) <= F_i V(t), F_i = y_i (96 T_i)^(-3), for every t with all sides
>= 2 T_i; (b) every t with all sides in [2 T_i, 96 T_i) has r_1(t) <= u_0^(1/T_0) (so every cube of side >= 2 T_0, and every
torus with smallest side a >= 2 T_0 and largest side < 24 a, has the gap delta_* = log(1/u_0)/T_0 >= 0.172/T_0);
(c) Zcal_n(n) - 1 <= 1.9e-11 u_0^(n/(2 T_0)) for cubes of side n >= 2 T_0.

**Check (HOLDS given Proposition 7.52, Lemma 7.27 (both inequalities) and Lemma 7.12; Claude Opus 5.5 max, this row).**
I redid every line:
- Base: Proposition 7.52 at (T, P) = (T_0, 24 T_0) needs P > 12 T (true) and bounds g(T_0, 24 T_0) by gamma through (B*):
  log Zcal_t(T_0) <= 2 gamma V(t) = F_0 V(t) for every t with sides >= 2 T_0, F_0 (96 T_0)^3 = y_0. Correct.
- Step: for s with sides in [2 T_(i+1), 48 T_(i+1)) = [4 T_i, 96 T_i), the sides are >= 2 T_i, so D_s(T_i) <= e^(F_i V(s)) - 1
  by (a) at i. The second inequality of Lemma 7.27 is D_s(2T) <= D_s(T)^2; it is elementary: D_s(2T) = sum_(i>=1) r_i^(2T) <=
  (sum_(i>=1) r_i^T)^2 because every r_i^T >= 0 (this uses only nonnegativity of the spectrum, A's Lemma 7.3(vii)). With
  log(1 + x) <= x: log Zcal_s(T_(i+1)) <= (e^(F_i V(s)) - 1)^2. The map v -> (e^(F v) - 1)^2/v is increasing on v > 0 and
  V(s) < (96 T_i)^3, so log Zcal_s(T_(i+1))/V(s) <= (e^(y_i) - 1)^2/(96 T_i)^3. That bounds g(T_(i+1), 24 T_(i+1)), whose window is
  exactly [2 T_(i+1), 48 T_(i+1)); Proposition 7.52 then gives the coefficient 2 (e^(y_i) - 1)^2 (96 T_i)^(-3) = y_(i+1) (96 T_(i+1))^(-3).
  Correct.
- Numbers: chord bound e^y - 1 <= 20 (e^(1/20) - 1) y = 1.02542 y on [0, 1/20]; 16 x 1.0255^2 = 16.827 <= 16.83;
  16.83/20 = 0.8415. So y_(i+1) <= 16.83 y_i^2 <= 0.8415 y_i and 16.83 y_(i+1) <= (16.83 y_i)^2, hence 16.83 y_i <= u_0^(2^i).
  Correct.
- (b): for t with sides in [2 T_i, 96 T_i), V(t) < (96 T_i)^3, so r_1^(T_i) <= D_t(T_i) <= e^(y_i) - 1 <= 1.0255 y_i <= 0.0610 u_0^(2^i);
  r_1 <= u_0^(2^i/T_i) = u_0^(1/T_0); log(1/0.8415) = 0.1726. The two geometric clauses follow from the choice of the largest i
  with 2 T_i <= (smallest side). Correct.
- (c): with 2 T_i <= n < 4 T_i, F_i n^3 < 64 T_i^3 F_i = y_i/13824 <= 3.7e-6; D_t(T_i) <= y_i/13823; D_t is nonincreasing in the
  time (r_i <= 1); D_t(n) <= D_t(2 T_i) <= D_t(T_i)^2 <= (u_0^(2^i)/(16.83 x 13823))^2 = 1.848e-11 u_0^(2^(i+1)) and
  n/(2 T_0) < 2^(i+1). Correct.
So the ascent itself is a short, correct argument; its weight sits in Proposition 7.52 (extensivity at a fixed time),
which rests on Lemma 7.51, which rests on Lemma 7.27 (first inequality), Lemma 7.31(ii), Lemma 7.44 and Proposition 7.45(ii).
Those are checked next (Step 3b). The first part of Lemma 7.51 already HOLDS: each single cut of a side is
Tr M^(a+b) <= Tr M^a Tr M^b for the positive transfer matrix M in the cut direction (Tr M^a M^b <= Tr M^a ||M^b|| <= Tr M^a Tr M^b),
so Z(t, tau) <= product over pieces of Z(s, tau); tau -> infinity gives kappa[P](t) >= 0, and multiplying by e^(T E_0(t)) gives
log Zcal_t(T) <= T kappa[P](t) + sum_s log Zcal_s(T).

## Step 3b: the inputs of the ascent, checked (2026-11-20T17:03Z, date -u)

All page numbers are PDF pages of A. Verdicts by Claude Opus 5.5 max (this row), one reading, not an audit.

| A's statement | What it says | Verdict | Note |
|---|---|---|---|
| Lemma 7.27 (p. 39) | Z(n'+n'', ...) <= Z(n', ...) Z(n'', ...) in every direction; D(M'+M'') <= D(M') D(M'') | HOLDS | sum of lambda_i^(a+b) <= (sum lambda_i^a)(sum lambda_i^b) for lambda_i >= 0; needs the transfer matrix in each direction to be nonnegative (A's Lemma 7.3(vii), the standard positivity of the Wilson transfer matrix for beta >= 0) |
| Lemma 7.31 (i)-(ii) (p. 41) | e(b,c) = lim E_0(b,c,M)/M exists in (-inf, 0]; zeta(l; b,c) = l e - E_0(l,b,c) >= 0 is the growth rate of the direction-1 relative partition function; single-cut defect = zeta(l') + zeta(l'') - zeta(l) <= zeta(l') + zeta(l'') | HOLDS | Fekete for the superadditive M -> E_0(b,c,M); E_0 symmetric in its arguments because Z is; the identity is (i) three times |
| Lemma 7.44 (ii) (p. 51) | l -> zeta(l; b,c) is nonincreasing | HOLDS | limit of M^(-1) log of sum_i r_i^l with 0 <= r_i <= 1 |
| Proposition 7.45 (ii) (p. 51-52) | for l > tau >= 3: zeta(tau; b,c) <= log Zcal_(b,c,l)(tau)/(l - tau) | HOLDS | Z(b,c,kl,tau) <= Z(b,c,l,tau)^k, Lemma 7.31(i) along M = kl, then zeta(l) <= zeta(tau). This is the step that bounds a Casimir-type defect by a thermal sum at a shorter time. Row 697 has the same mechanism (`gap-crux-restate.md` L182-L186): with zeta_A(b; c, d) = kappa_lane(b), Lemma X's crossing identity a kappa(b) + g(a, b) = b kappa(a) + g(b, a) and Lemma K (d) give (b - a) kappa(a) <= g(a, b), which is A's (ii); Lemma X as printed states the weaker (b - a) kappa(b) <= g(a, b). Found independently (row 697 is earlier than A's 2026-11-12 archive) |
| Lemma 7.51 (p. 55-56) | cut of mesh P (P >= 2T, pieces with sides in [2T, 2P)): log Zcal_t(T) <= T kappa[P](t) + sum_s log Zcal_s(T), kappa[P](t) <= 12 f_S(T) V(t)/P | HOLDS | each single cut costs <= 2 zeta(T; B, C) <= 2 log Zcal_(B,C,2T)(T)/T <= 4 f_S(T) B C (the torus (B, C, 2T) has its sides in [2T, S]); at most t_1/P cuts in direction 1, and the slab sums give V(t)/P in directions 2 and 3 |
| Proposition 7.52 (p. 56) | P > 12T: log Zcal_t(T) <= g(T,P) V(t)/(1 - 12T/P) for all t with sides >= 2T; factor 2 at P = 24T | HOLDS | f_S <= (12T/P) f_S + g, f_S finite (finite maximum) |
| Theorem 7.56 (p. 58-59) | (B*) at T_0 with y_0 <= 1/20 gives (a)-(c) of Step 3a | HOLDS given the rows above | Step 3a |
| Lemma 7.33 (p. 42) and Proposition 7.57 (p. 60-61) | log Zcal(M) <= psi(M) <= 2 log Zcal(M), psi(M) = 2 log Z(M) - log Z(2M); (B**) with gamma gives (B*) with gamma, (B*) with gamma gives (B**) with 2 gamma | HOLDS | 1 <= Zcal(2M) <= Zcal(M) |
| Theorem F (i), (ii) (p. 59-60) | if (B*) holds at T_0 <= N t_0 for all late (p, N): Zcal - 1 <= 1.9e-11 e^(-Delta L_p/2), and every transfer eigenvalue of the cylinder of side N L_p other than lambda_0 is at most e^(-Delta/N) lambda_0, Delta = log(1/u_0)/t_0 | HOLDS | Theorem 7.56(c) and (b) with n = N L_p >= 2 T_0 and T_0 <= N t_0 |
| Theorem F (iii) (p. 60) | with A's construction hypothesis (W): the Wightman theory has sigma(H) in 0 and [Delta, infinity), 0 simple | NOT CHECKED here | rests on A's Section 7.6 (Theorem E, Proposition 7.4, Lemma 7.5, Proposition 7.10, Corollary 7.11) and on (W); row 1224 L294 lists "a check of A's Section 7 hypotheses (W), (U) against the account's construction order" as another open item |

**Result of Step 3 (PROVED as a check; unchecked by another provider).** The lattice half of A's ascent is correct:
(B**) (equivalently (B*)) at one time T_0, on the spatial window [2 T_0, 48 T_0)^3, with y_0 <= 1/20, gives a transfer gap
log(1/u_0)/T_0 on every cube of side >= 2 T_0 and on every torus of aspect below 24, uniformly in the size, using only
positivity of the transfer matrices in the four directions and the symmetry of Z under permutations of the axes. Nothing
in it is specific to SU(2) or to four dimensions beyond the constants (A states the d-dimensional constants after
Theorem 7.53). It is a Knabe-type finite-size criterion, as A says. Its weak-coupling input (B*) along beta -> infinity is
open, as A says (p. 58, p. 61: "A proof of (B*) along couplings beta -> infinity therefore proves exponential clustering").

## Step 4: two links between the chain's datum, A's hypothesis and (N-phys) (2026-11-20T17:06Z, date -u)

Definitions used (grep-verified): row 1258 (`gap-mini-solve-ag-opus.md` L66-L68) writes F(t, B) = log Z(t x B) on the periodic
torus (Z/t) x B and Phi_B(a) = 2 F(a, B) - F(2a, B); so Phi_s(T) is exactly A's psi_s(T) of Lemma 7.33 (p. 42). Row 1258's
Proposition RR (i) (L350) gives Phi_B(t) <= eta_*(t, B; beta), and Lemma WS' (L236-L240) gives eta_*(a, B; beta) <= 6 pi beta
abs(B) tau_*(a, B; beta) for a >= 3. (N-phys) is row 1161's statement (`gap-solve9-astra62.md` L146-L148), with K = 512
admissible (L215, lattice range 4 | n, n >= 2^70); its consumer reads s_+(floor(n/K)) <= 1/2, and s_+ is nonincreasing in
the time, so an integer u in [3, n/K] with s_+(u) <= 1/2 suffices.

**Corollary AU1 (the chain's datum gives A's hypothesis; PROVED given row 1258's Proposition RR (i) and A's Lemma 7.33,
both elementary).** Let beta >= 0 and T_0 >= 3. If
    eta_*(T_0, s; beta) <= V(s) / (40 (96 T_0)^3)   for every spatial torus s with all sides in [2 T_0, 48 T_0),     (AU1)
then (B**) and (B*) hold at T_0 with gamma = 1/(40 (96 T_0)^3), i.e. y_0 = 1/20, and A's Theorem 7.56 (checked in Step 3)
gives at this coupling: r_1(t) <= 0.8415^(1/T_0) (a transfer gap at least 0.172/T_0) on every cube of side >= 2 T_0 and on
every torus of aspect below 24 with smallest side >= 2 T_0. By Lemma WS', (AU1) holds if
    tau_*(T_0, s; beta) <= 1/(240 pi beta (96 T_0)^3)   on the same window,                                              (AU1')
a bound with no volume factor (abs(s) = V(s) cancels).
Proof. psi_s(T_0) = Phi_s(T_0) <= eta_*(T_0, s) <= gamma V(s): that is (B**) with gamma; Lemma 7.33 gives log Zcal_s(T_0) <=
psi_s(T_0), which is (B*) with gamma, and y_0 = 2 gamma (96 T_0)^3 = 1/20. (AU1') times 6 pi beta abs(s) is (AU1). QED

**Corollary AU2 (A's hypothesis at every late cutoff gives (N-phys); PROVED given A's Theorem 7.56 (a), checked in Step 3;
this turns row 1218's reason 1, ARGUED there, into a proof).** Fix K >= 2 and let i_* >= 0 be an integer with
    u_0^(2^(i_*)) <= 16.83 log(3/2) (48/K)^3,   u_0 = 16.83 y_0.                                                          (AU2)
Suppose that at every cutoff j >= j_0 (spacing a_j, coupling beta_j) (B*) holds at some integer T_0(j) >= 3 with
T_0(j) a_j <= t_0 and y_0 <= 1/20. Then for the physical side L = K 2^(i_*) t_0, at every j >= j_0 with n_j = L/a_j an integer
(and 4 | n_j where the consumer asks it), there is an integer u_j in [3, n_j/K] with D_(n_j^3)(u_j) <= 1/2, hence
s_+(u_j; n_j^3) <= 1/2: (N-phys) holds at L. For K = 512 and y_0 = 1/20 (u_0 = 0.8415), (AU2) holds with i_* = 5
(2^(i_*) >= 30.0), so L = 512 x 2^5 t_0 = 16384 t_0.
Proof. Fix j and write T_i = 2^i T_0(j). Let i_j be the largest i with K T_i <= n_j. Since K 2^(i_*) T_0(j) <= K 2^(i_*) t_0/a_j = n_j,
i_j >= i_*; by maximality n_j < 2K T_(i_j). The cube t = (n_j, n_j, n_j) has all sides >= K T_(i_j) >= 2 T_(i_j), so Theorem
7.56 (a) gives log Zcal_t(T_(i_j)) <= y_(i_j) (n_j/(96 T_(i_j)))^3 < y_(i_j) (2K/96)^3. The sequence y_i is nonincreasing with
16.83 y_i <= u_0^(2^i), so y_(i_j) <= u_0^(2^(i_*))/16.83 <= log(3/2) (48/K)^3 by (AU2), and log Zcal_t(T_(i_j)) <= log(3/2), i.e.
D_t(T_(i_j)) <= 1/2. Put u_j = T_(i_j): an integer with 3 <= T_0(j) <= u_j <= n_j/K. The vacuum of the periodic cube is
centre-invariant (it is the unique, positive Perron-Frobenius vector and the centre flips permute configurations), so the
neutral excited sum is a sub-sum of the full one: s_+(u_j) <= D_t(u_j) <= 1/2. QED

**What the two links change (ARGUED from the statements above).**
- The gpt-6.2-astra chain aims at A-B** (row 1290 L425). By Corollary AU2 its target, at every late cutoff, already feeds
  the lane's own checked consumer of (N-phys) (row 1161; its check, row 1162 `gap-solve9-check-opus.md`, reports 44 HOLD and 1 HOLDS AFTER CORRECTION (credit only), with K = 512, 4 | n, n >= 2^70 recomputed); it does
  NOT need A's construction hypothesis (W) or A's Section 7.6, the part of Theorem F not checked here.
- Row 1258's datum (RR) implies A's hypothesis at one cutoff (Corollary AU1). So the two running chains aim at
  statements of one family: (RR) (supremum over boundary slices) is the strongest, A-B** (periodic doubling defect on a
  window of shapes) sits between, (N-phys) (neutral, one aspect) is the weakest of the three (row 1218 table).
- Neither link touches the open input: (AU1), (B*) and (N-phys) along beta_j -> infinity are all OPEN.

## Step 5: A's engine against the lane's own checked engine (Theorem S) (2026-11-20T17:08Z, date -u)

Both are full-trace engines at one coupling that use only positivity of the transfer matrices and the symmetry of Z.
Statements compared (READ): the lane's Theorem S (`gap-crux-restate.md` L192-L198; checked in rows 698 and 699): if
s = S(n; (2n)^3) < 1/5041 (the excited sum of the cube of side 2n at time n), then every cube of side 2^(k+1) n has the gap
log(1/(5041 s))/n. A's Theorem 7.56 (Step 3): (B*) on the window [2 T_0, 48 T_0)^3 at time T_0 with y_0 <= 1/20.

**Remark AU3 (arithmetic PROVED; reading ARGUED).** Per unit spatial volume the two data ask:
- Theorem S: log(1 + s)/(8 n^3) < log(1 + 1/5041)/(8 n^3) = 2.48e-5/n^3, on one cube shape, at time n;
- A: log Zcal_s(T_0)/V(s) <= y_0/(2 (96 T_0)^3) <= 2.83e-8/T_0^3 (y_0 = 1/20; at A's fixed point y_0 -> 0.0589 it is 3.3e-8),
  on every shape of the window, aspect up to 24.
So at the same time scale the lane's engine tolerates a thermal density about 876 times larger (7.5 times larger even
against A's fixed point), on cubes only. In a gas of particles of mass m the density at time T falls like e^(-mT), so the
difference is a shift of the base time by about log(876)/m = 6.8/m: both data sit in the band, neither is easier in kind.
What A gives that Theorem S does not: the gap on every torus of aspect below 24 and the full ascent in four lines; what
Theorem S gives that A does not: a datum on one shape, nearly three orders of magnitude weaker. (N-phys) (row 1161) is
weaker than both, since it reads only the neutral sector (row 1218 table).
Consequence for the gpt-6.2-astra chain (ARGUED, for the lead; row 1290's J(1) of (27) is the thermal doubling ratio of
A-B**, as its check row 1297 says at `gap-solve33-check-opus.md` L406): its stated target A-B** (row 1290 L425) is sufficient by
Corollary AU2, but the lane's own consumers accept a weaker statement at the same scale: Theorem S's seed on one cube, or
(N-phys) on the neutral sector. Precisely: Theorem S's seed at n holds as soon as Phi_B(n) = psi_B(n) < log(1 + 1/5041)
= 1.98e-4 for the ONE box B = (2n)^3 (log(1 + s) <= psi_B(n) by A's Lemma 7.33 = row 1258 (2.3)), while A-B** asks
psi_s(T_0) <= 2.83e-8 V(s)/T_0^3 on every s of the window, which on s = (2 T_0)^3 is 2.26e-7, 876 times smaller.

## Step 6: summary, credits, check request (2026-11-20T17:09Z, date -u)

**What this row did.** It did not prove the mass gap and did not attack the infrared seed blind: every mechanism class
named in Step 1 is on file with its failing step or is being run by another row now. It took one unowned item with live
consumers, proposed but not done by row 1224 (L292-L295): a line-by-line check of the published thermal ascent of
Bhattacharjee, Bhattacharya, Lockwood, Romanov, Sessford and Singha Roy.

| Item | Label | Where |
|---|---|---|
| A's Lemma 7.27, Lemma 7.31 (i)-(ii), Lemma 7.33, Lemma 7.44 (ii), Proposition 7.45 (ii), Lemma 7.51, Proposition 7.52, Theorem 7.56 (a)-(c), Proposition 7.57, Theorem F (i)-(ii) | HOLD (checked line by line here, one reading by Claude Opus 5.5; no other provider) | Steps 3a, 3b |
| A's Theorem F (iii) (continuum half: Section 7.6 and hypothesis (W)) | NOT CHECKED; not needed by the lane, see Corollary AU2 | Step 3b |
| Corollary AU1: row 1258's datum (RR), eta_*(T_0, s) <= V(s)/(40 (96 T_0)^3) on A's window, gives (B*) with y_0 = 1/20, hence a transfer gap 0.172/T_0 on all cubes >= 2 T_0 at that coupling; in (SL) form tau_* <= 1/(240 pi beta (96 T_0)^3), no volume factor | PROVED (given row 1258 Proposition RR (i), Lemma WS', and A's Theorem 7.56 as checked) | Step 4 |
| Corollary AU2: (B*) at every late cutoff with T_0(j) a_j <= t_0 gives (N-phys) at L = K 2^(i_*) t_0 for every K; L = 16384 t_0 for row 1161's K = 512 | PROVED (given A's Theorem 7.56 (a) as checked); turns row 1218's reason 1 (ARGUED) into a proof | Step 4 |
| Remark AU3: per unit volume the lane's Theorem S seed tolerates a thermal density 876 times larger than A-B** at the same time scale, on one cube shape | arithmetic PROVED; consequence for the astra chain ARGUED | Step 5 |
| Kill tests of the chain's datum (thin sides; Z_2 flux through a slab) | ARGUED, no kill | Step 1 |
| The infrared seed ((N-phys), (SL)/(RR), (B*), Theorem S's seed) along beta -> infinity; the carry; the account's premises | OPEN, not attacked | Step 1 |

**What changes if the lead accepts it.** (1) The lane has a second, published full-trace engine, checked once here; it
needs nothing specific to SU(2). (2) The astra chain's target A-B** feeds the lane's own checked consumer of (N-phys)
(row 1161, check 1162) through Corollary AU2, with no use of A's (W) or Section 7.6. (3) The same chain can aim lower:
Theorem S's seed asks psi_B(n) < 1.98e-4 on the single box (2n)^3, where A-B** asks 2.26e-7 there and more shapes.

**Credits.** A: Deep Bhattacharjee, Ushashi Bhattacharya, James Montgomery Lockwood, Tristan Romanov, Ikailo John
Sessford, Sanjeevan Singha Roy (every A statement above is theirs; this row only checks it). Row 697 (Claude; Lemmas K,
X, E and Theorem S, `gap-crux-restate.md`, checked in rows 698, 699): the same deficit-by-thermal-sum mechanism, found
independently. Row 1258 (Claude Opus 5.5; Proposition RR, Lemma WS'). Row 1161 (gpt-6.2-astra; (N-phys), K = 512) and its
check row 1162. Row 1218 (Codex reading of A, B and Zeng). Row 1224 (proposed this check). Rows 1290 and 1297 (the astra
chain's target and its check). Sussman and Alpoge's account and Balaban's papers are not used in this row.

**Check request.** One cross-provider reading of Steps 3a-3b (the ten A statements, against A's pages 39-42, 51-52,
55-61 of the Zenodo 24147967 copy), Corollaries AU1-AU2 and the arithmetic of Remark AU3. Nothing here goes outward
without the owner.

RESULT: Row 1295 (Claude Opus 5.5 max, Mac mini worker 1, 16:32Z-17:09Z by date -u; author only, checked by no one; no numeric run, no subagent). The Jaffe-Witten mass gap of four-dimensional SU(2) Yang-Mills is NOT proved and nothing is disproved; the infrared seed ((N-phys), (SL)/(RR), A's (B*)) stays OPEN and was not attacked (every mechanism named in Step 1 is on file or run by rows 1294-1304). Worked item (proposed by row 1224, unowned): a line-by-line check of the published thermal ascent of Bhattacharjee, Bhattacharya, Lockwood, Romanov, Sessford and Singha Roy (Zenodo 24147967): Lemmas 7.27, 7.31, 7.33, 7.44, 7.51, Propositions 7.45 (ii), 7.52, 7.57, Theorem 7.56 and Theorem F (i)-(ii) HOLD (Theorem F (iii), the continuum half, not checked); their Proposition 7.45 (ii) is the deficit bound of row 697's Lemma X in a slightly sharper form. PROVED: Corollary AU1 (row 1258's datum (RR) on A's window gives A's (B*) with y_0 = 1/20, so a lattice gap 0.172/T_0 at that coupling; in (SL) form tau_* <= 1/(240 pi beta (96 T_0)^3) with no volume factor); Corollary AU2 ((B*) at every late cutoff gives (N-phys) at L = 16384 t_0 for K = 512, turning row 1218's reason 1 from ARGUED into a proof, so the astra chain's target A-B** feeds the lane's checked consumer without A's (W)); Remark AU3 (arithmetic: the lane's Theorem S seed tolerates an 876 times larger thermal density than A-B** on one cube shape). OPEN: the infrared seed at weak coupling in every form, the one-cutoff carry's inputs, the account's premises, the mass gap. Output library/gap-mini-solve-au-opus.md.
