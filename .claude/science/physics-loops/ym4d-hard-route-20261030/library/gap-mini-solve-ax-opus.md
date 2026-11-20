lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T04:37Z

# gap-mini-solve-ax-opus: the SU(2) four-dimensional mass gap

Queue row 1300 of `FINISH.md`. Pinned commit e0f6f898f, branch `claude/ym4d-hard-route`.
Started 2026-11-20T16:37Z. Labels: PROVED, ARGUED, GUIDE, OPEN, as the row asks.

## 0. Status of this file

Step 0 (record read) done 16:55Z. Step 1 (how to attack) done 17:18Z. Work continues below; nothing proved yet.

## Step 0: record read (2026-11-20, 16:37Z-16:55Z by date -u)

Read at pin e0f6f898f: `GOAL.md` in full; `FINISH.md` L1-84, L299-356 and row 1300 (this item); the RESULT lines of
rows 1288, 1291, 1293, 1294, 1297; the briefs of rows 1295-1304 (in flight); `parts/gap.md` L1-104 and L223-322
(state, route registry, test table, exact price); `library/prior/gap-onebound-read-sol.md` in full (row 1218, credited
there to Bhattacharjee, Bhattacharya, Lockwood, Romanov, Sessford and Singha Roy (A, B) and to Zeng Chunping (C));
`library/gap-mini-solve-av-opus.md` Steps 0-1 (row 1296) and the head of `gap-mini-solve-au-opus.md` (row 1295);
`library/gap-mini-solve-ah-opus.md` (row 1259) at its (TR) lines. `library/open-core.md` registers no gap item (grep
"seed", "gap", "N-phys", "thermal": one unrelated hit, L524).

What the record fixes (statements about the record, not evidence):

1. Modulo the ultraviolet carry, the gap reads one lattice input at order-one coupling: (N-phys) of row 1161, or
   equivalently a uniform cube gap plus the count (TR) of row 1259 at one coupling in the window 2.3-2.6.
2. Every plain-brief row since 1188 ends with that input OPEN and "no route off the record". Rows 1259, 1291 and
   1296 each screened about ten routes and matched each on file at its first failing step.
3. In flight and owned elsewhere: the one-cutoff carry (rows 1294, 1296), tilings (1301, 1302), the positivity
   object (1303, 1304), the astra chain (1298), and rows 1295 and 1299 (plain brief, no item named at this pin).

## Step 1: how best to attack it (judgement, ARGUED; written 2026-11-20T17:18Z by date -u)

**The problem, as the record fixes it.** Modulo the ultraviolet carry, the Jaffe-Witten gap for Wilson SU(2) reads
one lattice input at order-one coupling: (N-phys) of row 1161, equivalently a uniform cube gap plus the count (TR)
of row 1259 at one coupling of the window 2.3-2.6. There the glueball correlation length is one or two lattice
spacings (row 1278), every published rigorous method stops about ten times lower in beta (row 1278), and every
criterion uniform over boundary data fails (Proposition CA-FAIL, rows 1072-1077).

**My judgement of the best attack (ARGUED).** Under the rule of `GOAL.md` (no numerics, no machine enumeration,
finite arithmetic only when it can be checked by hand), a seed at a window coupling can come from only two kinds of
argument. (i) A beta-specific estimate at correlation length one or two lattice spacings. Every such estimate I can
name (cluster expansion, Dobrushin or disagreement percolation on blocks, a finite-box criterion such as A-B* of
row 1218 or the cube inequality of B) needs explicit information about the Wilson measure near beta = 2.4 that no
hand calculation supplies. (ii) A soft mechanism valid uniformly in beta, as in the two posted 2D proofs (OpenAI;
Ding, Huang and Yang; rows 1007-1010). So the best attack is a 4D soft mechanism. Its missing parts are on file:
the 2D gain needs a global non-abelian symmetry, and pure 4D SU(2) has only central link symmetries (Lemma CEN+,
row 1016, checked by row 1020); the 2D templates, read in 4D, act on centre-charged observables, that is on the flux
half, and the crux is in the neutral half (rows 1193, 1213, 1241, 1258; the 2D singlet gap follows from the charged
gap, which has no 4D analogue); and in 4D even the "base" bound of such a proof (McBryan-Spencer or spin-wave level
decay of neutral correlations at every beta) is not available (`gap-crux-*`, `gap-arealaw-*` files).

**Screen (rule 0a), short.** Each idea I formed before reading the tables has a match on file with its first failing
step; I do not repeat them: 2D pinned-cell stiffness and DHY loop soups (rows 1007-1018); orbit-space curvature and
Bakry-Emery (rows 1229, 1237); twisted and multi-direction blocks (rows 1215, 1273, 1285-1287, 1301-1302);
weakened-wall interpolation of the free energy (`gap-fw-wilson-max.md`; (DS-W), row 1122 6.4); area-law and
density-of-states links (`gap-arealaw-opus.md`, `gap-arealaw2-opus.md`); Gribov horizon and Coulomb frames
(`gap-coulomb-frame.md`); "uniform gap implies the count" ((NS-gap) of row 700; rows 1135, 1234, 1259, 1291; the
line-spin model satisfies (NS-gap) at every fixed coupling, row 1234 3 (c)).

**Two probes of my own, this session (GUIDE; no claim recorded as PROVED).**
1. *A kill test of row 1298's open estimate (37)* (gpt-6.2-astra, committed after this row's pin, at e44ecf93c):
   "gamma_d >= c a uniformly", the gap of the flagged-cap resampling chain restricted to G_d. Local heat-bath dynamics
   usually relax physical-scale modes at rate of order a^2 (critical slowing down), which would kill (37). It does not
   here: the resampling of (29)-(31) conditions on the two neighbouring time slices, so for a free massive field the
   zero-momentum one-particle state has Dirichlet ratio about 2 delta (m a), delta the flag density (one flagged link
   changes by about beta^(-1/2), the zero mode has equal-time variance about 1/(2 beta m a)). So (37) is consistent
   with a gapped free field at c of order delta m, fails for the massless field, and is the gap in Dirichlet form, as
   row 1298 found for (34) by its one-mode calculation. A second worry, winding traces (spatial Polyakov loops) that
   pass the local energy tests, also does not kill (37): a single winding holonomy changes by about (delta n/beta)^(1/2)
   per step, and a smeared toron coordinate has variance of order n^(-2) in a confining state. No kill.
2. *Is CMP 116 reachable?* The carry inputs (CE), (E0)-(E5) and `9.1:prop-blind-site-expansions` (CA-III L16559,
   "Proof outstanding"; its printed route repeats Balaban CMP 116 Section 2 with island-blind inputs) need Balaban's
   CMP 116. It is not in `~/ym4d-papers`, and Project Euclid answered with a bot check (stopped there, FINISH Rules).
   Row 1299 works (CE) and (E0)-(E5) through the account's own printed machine.

**Decision.** No route to the seed off the record, in agreement with rows 998, 1219, 1278, 1284, 1291, 1296. I take
the count half, because it is the one piece of the seed that is a statement about a single lattice theory with no
band input in its hypothesis: (NS-gap), "a uniform cube gap at one coupling forces a seed at that coupling", open
since row 700, with no counterexample (rows 1234, 1259) and no owner at this pin (rule 0a: FINISH rows naming
(NS-gap) are 700, 703, 1234, 1250, 1251, 1259; none in flight). A proof would reduce the crux to the lattice gap at one
coupling; a counterexample inside the class of local reflection-positive models with a simple gapped vacuum would show
that the count is a separate obligation for every route. Moves: the count half of the seed (`parts/gap.md`, the
exact price; row 1259 Corollary CD1).

## Step 2: the count half, (NS-gap), attacked three ways (written 2026-11-20T17:21Z by date -u)

**Statement (row 700, `gap-seed-limit.md` L229-231; row 720, `gap-phys-seed.md` Corollary Z2).** At one coupling, let the
periodic cubes have a uniform gap, m(b^3) >= m_0 > 0 for b >= b_0. (NS-gap): then the model has a seed. By Corollary
Z2 it is enough that liminf_a D(a)/a < m_0/64, D(a) = F(a^4) - f_inf a^4; a model with a uniform gap and no seed must
have D(a) >= (m_0/64) a - 0.12 for all large a. With Lemma CD of row 1259, D(a) = g(a; a^3) + a sigma_1(a) +
a^2 sigma_2(a) + a^3 sigma_3(a), every term >= 0.

**Attack A, rotation and the cube's Casimir density (inequality PROVED, elementary; found again: it is row 1291's
Lemma CR in another form).** For all t, b >= 1,

    sigma_3(t) <= g(t; b^3)/b^3 + t eps(b),   eps(b) := [sigma_1(b) + b sigma_2(b) + b^2 sigma_3(b)]/b^3 >= 0.     (A1)

*Proof.* By reflection positivity F/|T| does not increase when a side is doubled (row 1259, Lemma CD (c)), so
Lambda_3(t) = lim F(t, T, T, T)/T^3 <= F(t, b, b, b)/b^3 along T = 2^k b. Next F(t, b, b, b) = t Lambda_1(b^3) + g(t; b^3)
(Lemma CD (b)), and the telescoping of Lemma CD (c) at side b gives Lambda_1(b^3) = b^3 f_inf + sigma_1(b) + b sigma_2(b)
+ b^2 sigma_3(b). Subtract t f_inf. QED
The cube gap enters (A1) only through g(t; b^3) <= log(1 + e^(12 beta b^3) e^(-m_0 (t - 1))), which is small only for
b^3 << m_0 t/(12 beta). Then t eps(b) carries the factor t/b >= t^(2/3): (A1) moves the count from scale b to scale t
with a growing coefficient, and with the trace bounds sigma_k(b) <= 12 beta b^(3-k) it gives nothing below the trivial
sigma_3 <= 12 beta. **Fails at:** a bound eps(b) = o(1/t) at some b with b^3 << t, which is the count at the smaller
scale. Row 1291 Lemma CR states the same obstruction for every tiling bound.

**Attack B, gap plus reflection positivity in time and space (ARGUED; matches rows 700, 703, 1291).** The gap gives
S(t; X) <= e^(-m_0 (t - s)) S(s; X) for s < t. Reflection positivity in a space direction gives
1 + S(t; (2b, b, b)) <= (1 + S(t; b^3))^2 e^(t kappa(b)), kappa(b) := 2 log lambda_0(b^3) - log lambda_0(2b, b, b) >= 0.
Neither reduces the extensive trace bound log(1 + S) <= 12 beta |X| (row 700, as corrected by row 703: "too weak by the
power n^2"), and the spatial step adds the ground-state Casimir term t kappa(b). **Fails at:** any bound on the
number of levels of the cube below a fixed energy that is better than e^(c |X|), that is (NS) of row 700 with
theta < 1.

**Attack C, a counterexample in the class (GUIDE; no model built).** By Corollary Z2, a counterexample needs, on cubes
of side n, about e^(c n) levels at bounded energy above the gap (c > m_0/K at aspect ratio K), that is extended
excitations whose energy does not grow with their length but whose number of internal states does. In every
construction I tried, such zero-tension objects either close around the torus at no cost, which makes the vacuum
degenerate and breaks the uniform gap, or carry a positive tension h, which caps the internal entropy per length
(Hagedorn temperature h/log 2) and gives a finite seed at every fixed coupling. This is the mechanism of row 1259
point 3 (subsystem-symmetric candidates lose their gap) and of row 1234 (the line-spin model satisfies (NS-gap) at
every fixed coupling). No counterexample; none is on file.

**Result of Step 2.** (NS-gap) is equivalent, through Corollary Z2 and Lemma CD, to a statement about the low-lying
spectrum of one lattice theory: on large cubes, the number of levels below a fixed energy grows slower than
exponentially in the side (row 700's (NS) with theta < 1). For models whose excitations are local particles this holds
with a wide margin (row 700's free-particle guide); a proof for Wilson SU(2) would need a structure theorem for the
excitations of a gapped transfer operator that no tool in the lane (or known to me) supplies, and a counterexample
needs gapped zero-tension extended excitations, which I could not build. OPEN, unchanged; no new statement is claimed.
By FINISH rule "How we work" item 4 (two reductions, gap to seed to the count half, with no closure), I stop here and
report.
