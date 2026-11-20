lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T04:32Z

# gap-mini-solve-au-opus (row 1295): four-dimensional SU(2) Yang-Mills mass gap, plain brief

Started 2026-11-20T16:32Z (date -u) on the Mac mini Claude worker 1, branch claude/ym4d-hard-route pinned at e32c8d919.
Model: Claude Opus 5.5, max reasoning. Labels: PROVED, ARGUED, GUIDE, OPEN. Status: in progress; sections are appended as each step ends.

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
| Proposition 7.45 (ii) (p. 51-52) | for l > tau >= 3: zeta(tau; b,c) <= log Zcal_(b,c,l)(tau)/(l - tau) | HOLDS | Z(b,c,kl,tau) <= Z(b,c,l,tau)^k, Lemma 7.31(i) along M = kl, then zeta(l) <= zeta(tau). This is the step that bounds a Casimir-type defect by a thermal sum at a shorter time; it is the published form of what check 1292 found in row 697's Lemmas K, X, E (`gap-crux-restate.md`) |
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

