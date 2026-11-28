lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T20:14Z

# gap-mini-solve-v-opus: four-dimensional SU(2) Yang-Mills mass gap (plain brief, FINISH row 1234)

Queue row 1234 of `FINISH.md` (queued 2026-11-20T06:04Z). Plain brief: prove that four-dimensional SU(2) Yang-Mills
theory has a mass gap in the sense of Jaffe and Witten. Run by Claude Opus 5.5 at max effort on the Mac mini worker,
pinned at commit 56e523e38. Research-stage working state; nothing here is a public claim. Labels: PROVED, ARGUED,
GUIDE, OPEN. No numeric run is a proof step.

## Status log

- 2026-11-20T08:14Z (date -u) started; file created first per the save protocol. Next: read FINISH.md rule sections, `parts/gap.md`,
  the row-1218 reading `library/prior/gap-onebound-read-sol.md`, and the newest sibling rows (s, t, u, w, x).
- 2026-11-20T08:25Z (date -u) Section 1 (reading log and orientation) written.
- 2026-11-20T08:50Z (date -u) Section 2 (judgement and choice of work) written.
- 2026-11-20T08:55Z (date -u) Section 3 (the line-spin model at one coupling; Proposition LS) written.
- 2026-11-20T08:56Z (date -u) Section 3 corrected (hypothesis K >= 1 added; GUIDE check of (c)-(d) recorded, arithmetic slip fixed).
- 2026-11-20T08:57Z (date -u) Sections 4 (residual count, found again) and 5 (summary) written.
- 2026-11-20T08:59Z (date -u) re-read of Sections 3-5 done (wording and anchor fixes); RESULT line written.

## 1. Reading log and where the problem stands (reading only; no new claim)

Read at this pin (56e523e38): GOAL.md in full; FINISH.md L1-84 and L299-351 (how we work, joining, working efficiently, rules) and
row 1234 (this row) in full; the RESULT parts of rows 1222-1238; `parts/gap.md` L1-104 (state of attack, routes 1-36,
lead rules); `library/prior/gap-onebound-read-sol.md` (row 1218) in full; the plan and closing sections of the sibling
Opus rows 1228 (s), 1229 (t), 1233 (u), 1237 (w) and the opening of 1238 (x).

Where the problem stands on file (cited, not re-derived; every item is author-labelled in its row unless a check is named):

1. Consumer side. Beside the premises of Sussman and Alpoge's complete account (the T0 chain), the Jaffe-Witten gap on
   the account's tr F^2 sector follows from one lattice estimate, (N-phys) (row 1161 `gap-solve9-astra62.md` L146-148;
   row 1225 Theorem E-N; cross-provider check row 1232: HOLDS AFTER CORRECTION, with the rate at least (2/L) log(2^18/5041)
   on the matched scalar sector).
2. (N-phys), as restated in row 1218 (`prior/gap-onebound-read-sol.md` L38-44): there are a physical side L and j_0 such
   that for every cutoff j >= j_0 some integer u_j with 3 <= u_j <= n_j/K has s_+,j(u_j; n_j^3) <= 1/2, where s_+ is the
   centre-neutral excited trace of the vacuum-normalised periodic transfer matrix and K is fixed first.
3. Ultraviolet carry. Row 1233 (u) proved, given named statements of the account, that a one-cutoff seed suffices
   ((ONE-K) in corrected one-cutoff form), with remaining inputs (EDGE), (DET)'s (ID-a), (ID-b), (I-loc), and the
   account's own OUTSTANDING `9.1:prop-blind-site-expansions` (check row 1242 queued).
4. The infrared crux. The one-cutoff seed is the lattice gap of Wilson SU(2) at one coupling in the account's window, with
   an explicit finite-volume neutral trace bound (row 1225 Section 4; row 1233 Section 4). About two dozen plain-brief
   rows (1188-1238, letters a to x) found no engine that crosses the band of order-one coupling; the screening tables are rows 1189, 1194,
   1199, 1225, 1229 (Step 1.2), 1237 (Step 1.2), and the route registry of `parts/gap.md` (methods 1-36).
5. Published work on the same target (row 1218): A (Bhattacharjee et al., One Bound at One Scale) gives a full-trace
   thermal window criterion with a proved ascent at fixed coupling, stronger than (N-phys); B (One Cube Estimate) gives
   cube-dynamics criteria and a weak-coupling Poincare bound for coarse straight-path variables (Corollary 166), which
   row 1220 showed is the near-Haar property of long transports (Lemma NULL); C (Zeng) gives common-rate criteria and a
   conditional tunnelling route. None supplies the open Wilson estimate (row 1218 RESULT).

Registry grep before choosing (rule 0a; zsh loop over `library/*.md`, `library/prior/*.md`, `parts/gap.md`, file
counts): OSSS 5, Duminil 23, random-cluster 23, Schweinhart 16, Petkova 68, spectral independence 5, stochastic
localization 6, Simon-Lieb 13, Michalakis 11, Kogut-Susskind 18, Unsal 20, Tomboulis-Yaffe 28, Chatterjee 88,
Frohlich-Spencer 24, Edwards-Sokal 4, vortex free energy 40, Ginibre 78, Griffiths 59, Lee-Yang 23, complete
analyticity 25, Dobrushin-Shlosman 43; only "randomized algorithm" had 0 hits (the same tool is on file as OSSS).
Every band-crossing tool I could name is on file with a named failing step.

## 2. How best to attack it (judgement, ARGUED; written 2026-11-20T08:50Z by date -u)

**2.1 What a proof must contain (cited).** Modulo the account's premises and the ultraviolet carry, a proof needs
ONE infrared estimate for Wilson SU(2) at one coupling in the account's window: the one-cube neutral seed, i.e. a
uniform lattice gap on periodic cubes plus a thermal count (rows 1180 Step 2.1, 1225 Section 4, 1233 Section 4).
That is the classical open problem of exponential clustering of 4D lattice SU(2) at weak coupling, with explicit
finite-volume control. The published proofs of a 4D SU(2) gap stop at strong coupling (row 1218: A's Theorem 9.5,
beta_W <= 9/25; B's Corollary 74, beta_W < 2/9). No computed certificate may be used (GOAL.md).

**2.2 Engines.** I listed every band-crossing technique I know (Section 1 grep, plus semiclassical tunnelling as in
Zeng's TUN, anomaly constraints, sharpness by decision trees, loop soups and random surfaces, automorphic
equivalence of gapped phases). Each is on file with a failing step, or (anomalies, tunnelling) cannot produce a gap
by its nature: an anomaly forbids a trivially gapped phase but never forces one. Zeng's TUN (row 1218 reading) asks
for a foliated two-well structure along one loop with uniform controls; the zero set of the Wilson action on a torus
is a continuum (the flat connections), so TUN must be read on a slice, and row 1218 records no Wilson verification. I
did not read Zeng's text and make no claim about TUN beyond that. I found no engine of a new kind, which matches rows
1225, 1229, 1237 and 1238.

**2.3 What the sibling rows now cover (read at the branch tip 86fcc62, not at my pin).** Row 1238 (x) works on
(MAPCONV-F) of (UNIV-K) in YM4_1400 and records that the gap chain reads YM4_1400 while row 1233 read the complete
account's chapter 9; row 1233's remaining inputs are (EDGE), (DET)'s (ID-a), (ID-b), (I-loc) and the account's
OUTSTANDING `9.1:prop-blind-site-expansions`. I read that proposition's statement and route (CA-III 16560-16680,
fetched into a scratch folder at commit 31a47c543775): it is a repeat of Balaban's CMP 116 Section 2 expansion with
island-blind inputs at three sites, a multi-row project, not a session item. (EDGE) matches the lane's first-passage
data to chapter 9's tuned window; row 1238 has raised for the lead which text (YM4_1400 or the complete account) the
gap chain reads, and by my reading (EDGE) depends on that answer, so I do not take it.

**2.4 Decision.** No session-scale attack on the seed exists on file or in my list. So this row works on the one
part of the infrared input that the newest rows state loosely and that no row has separated: the COUNT. Rows 1225
and 1233 write "the seed at one coupling, equivalently the lattice gap of Wilson SU(2) there". Row 720 (L309) and row
700 ((NS-gap)) leave open whether a uniform gap forces a seed; row 1135 (iv) shows that a uniform physical gap does
not bound the torus excess ALONG the cutoff. The work items:

1. Decide what the line-spin model of row 1135 does at ONE fixed coupling, and what it says about the two routes
   (one-cutoff seed plus carry, against the all-cutoff (N-phys)).
2. State exactly what the count adds to the gap at one coupling, with the strongest bound I can prove from the gap
   and reflection positivity alone, and name the residual statement.

Moves: the wording of the crux in rows 1225, 1233 and 1238 (ARGUED "equivalently the lattice gap"), and the lead's
choice between the one-cutoff route (row 1233) and the all-cutoff (N-phys). Success: a proved separation or a proved
implication. Failure: the exact residual statement. This does not supply the seed, and the RESULT will say so.

## 3. The count: the line-spin model at one fixed coupling (written 2026-11-20T08:55Z by date -u)

**Model (row 1135 L164-171, by gpt-6.2-astra; checked HOLDS in row 1138, S6a).** On a periodic 4D torus, each site x
carries four spins u^mu_x in SU(2). A spin of type mu interacts only with the next spin of type mu in direction mu,
through the SU(2) heat kernel C_a = exp[(m a/3) Delta] (eigenvalue exp[-(m a/3)(d^2 - 1)] on the d-dimensional matrix
coefficients, multiplicity d^2). Spins are integrated with normalised Haar measure. The model is local, hypercubic,
reflection positive, with compact spins and a simple vacuum (row 1135). It is a comparison model, not Wilson SU(2);
it has no gauge sectors, so "seed" below means the full trace, which bounds every sector trace.

Write eps := m a (the gap in lattice units), Z_line(b) := Tr C_a^b = 1 + sum_(d>=2) d^2 exp[-(eps/3) b (d^2 - 1)],
and s(u; n^3) := Tr U^u - 1 for the vacuum-normalised time transfer U on the spatial cube n^3.

**Proposition LS (PROVED by hand; new as stated, see the grep note below).** For K >= 1 and 0 < eps <= 1 <= K/eps:

(a) Tr U^u = Z_line(u)^(n^3), and the spectral gap of U is exactly eps.

(b) For eps u >= 3: 4 e^(-eps u) <= Z_line(u) - 1 <= 4.1 e^(-eps u).

(c) At this fixed coupling the seed holds on all large cubes: with u = floor(n/K), s(u; n^3) <= 1/2 for every
    n >= (K/eps)(4 log(K/eps) + 12). So the seed size nu(eps) (least n with some integer 3 <= u <= n/K and
    s(u; n^3) <= 1/2) is finite, and nu(eps) <= (K/eps)(4 log(K/eps) + 12).

(d) nu(eps) >= (K/eps)(3 log(K/eps) + 6.9).

(e) Along any trajectory a_j -> 0 at fixed m: a_j nu(m a_j) >= (K/m)(3 log(K/(m a_j)) + 6.9) -> infinity. So
    the analogue of condition (a) of row 1180 Step 2.1 (a finite seed size at every coupling) holds at every j, the
    analogue of condition (b) (limsup_j a_j nu_j < infinity) fails, and the analogue of (N-phys) fails at every
    physical side L, although the physical gap is exactly m at every cutoff. (Row 1180's nu also asks 4 | n and
    n >= 2^70; adding these side conditions changes none of (c)-(e) except the explicit constant in (c).)

Proof. (a) Spins of type mu meet only spins of the same type on the same line, so the weight factorises over lines.
In the time direction, the n^3 time-parallel lines give the transfer factor C_a tensored n^3 times; the
perpendicular spins of one time slice interact only inside the slice, so they give the rank-one factor
A(V) A(V'), A the square root of their slice weight (row 1135 L171). Hence the nonzero spectrum of T is
<A, A> times the products over x of exp[-(eps/3)(d_x^2 - 1)], each with multiplicity the product of d_x^2. The top
eigenvalue <A, A> is simple (all d_x = 1), the next is <A, A> e^(-eps) (one d_x = 2), and Tr U^u = Z_line(u)^(n^3).
(b) The d = 2 term is 4 e^(-eps u). For d >= 3 and eps u >= 3, (eps u/3)(d^2 - 1) >= eps u + (d^2 - 4), so
sum_(d>=3) d^2 exp[-(eps u/3)(d^2 - 1)] <= e^(-eps u) sum_(d>=3) d^2 e^(-(d^2 - 4)) = e^(-eps u)(9 e^(-5) + 16 e^(-12)
+ 25 e^(-21) + ...) < 0.061 e^(-eps u).
(c) By (a), (b) and 1 + x <= e^x: s <= exp(4.1 n^3 e^(-eps u)) - 1 when eps u >= 3, and this is at most 1/2 when
4.1 n^3 e^(-eps u) <= log(3/2) = 0.405..., that is when eps u >= log(10.12 n^3). With u = floor(n/K) >= n/K - 1 it is
enough that eps(n/K - 1) >= max(3, 2.315 + 3 log n). Put n = (K/eps) z and w = log(K/eps) >= 0. For z >= 4w + 12:
z - eps >= 4w + 11 >= 3, and 4w + 11 >= 2.315 + 3w + 3 log z holds at z = 4w + 12 because w + 8.685 >= 3 log(4w + 12)
for all w >= 0 (at w = 0 it holds strictly, 8.685 > 7.46; the left side grows at rate 1, the right at rate
12/(4w + 12) <= 1). For larger z the left side z - eps grows at rate 1 and the right side 2.315 + 3 log n at rate
3/z < 1, so the inequality persists. Finally u = floor(n/K) >= 3 since n >= 12 K/eps >= 12 K.
(d) By (a), (b) and Bernoulli's inequality, s(u; n^3) >= n^3 (Z_line(u) - 1) >= 4 n^3 e^(-eps u). If s <= 1/2 for
some integer 3 <= u <= n/K, then eps n/K >= eps u >= log(8 n^3) >= log(8 (3K)^3) > 5. Put z = eps n/K >= 5. Then
z >= log 8 + 3 log n = 2.079 + 3 w + 3 log z >= 3 w + 2.079 + 3 log 5 = 3 w + 6.91.
(e) Multiply (d) by a_j = eps_j/m. For (N-phys) at a side L: with n_j = L/a_j, every admissible u has
eps_j u <= m L/K, so s(u; n_j^3) >= 4 (L/a_j)^3 e^(-mL/K), which tends to infinity. QED

GUIDE (not a proof step; run 2026-11-20T08:56Z under the numeric lock, holder confirmed, memory 54 percent free, about one
second; script in a scratch folder outside the repository): the exact seed size of the model, found by bisection on n
with u = floor(n/K) and the full series for Z_line, lies inside the bounds (c)-(d) in all 15 cases K in {1, 8, 512},
eps in {1, 0.3, 0.1, 0.01, 0.001}. Example K = 512, eps = 0.01: bounds 2.02 x 10^6 <= nu <= 2.84 x 10^6, exact
nu = 2,372,096. (An earlier draft line of this paragraph gave 3.2-4.0 x 10^5; that was an arithmetic slip, corrected
here.)

**Reading (ARGUED).**
1. The obstruction of row 1135 (iv) is a cutoff-uniform count: the number of light levels per physical volume,
   (L/a)^3 lines each with a level at energy m, grows without bound as a -> 0. At any ONE coupling the same model has
   a finite seed. So the line-spin model does not bind a one-cutoff seed; it binds only the passage from seeds at
   every coupling to (N-phys), that is condition (b).
2. In the one-cutoff route (row 1233 Proposition 3.7) that passage is the carry, whose input is the account's
   summable two-cutoff increments of the stop part. The line-spin family has no such increments: at a fixed physical
   size its torus excess D (row 1135) and its doubling defect Phi = 32 n^3 [2 log Z_line(n) - log Z_line(2n)]
   >= 32 n^3 log Z_line(n) both grow like (L/a)^3 e^(-mL) with n = L/a. So in the one-cutoff route the
   ultraviolet count is the account's, and the infrared input is condition (a) at ONE coupling: the seed of one
   lattice theory. In the all-cutoff route condition (b) must be supplied for Wilson SU(2) by an ultraviolet
   argument of the same kind.
3. Consequence for the wording of rows 1225, 1233 and 1238: "the seed at one coupling, equivalently the lattice gap
   there" is exact only up to the fixed-coupling count, i.e. modulo (NS-gap) of row 700 (`gap-seed-limit.md` L234;
   open since rows 697 and 720 L309: whether a uniform gap forces a seed at one coupling). The line-spin model satisfies (NS-gap)'s conclusion at
   every fixed coupling (its D_a(n) = 4 n^3 log Z_line(n) <= 16.4 n^3 e^(-eps n) for eps n >= 3, which tends to 0),
   so it is not a counterexample
   to (NS-gap); none is known to me.

**Grep note (rule 0a).** The general mechanism, a multiplicity d_j -> infinity at fixed physical energy, is on file:
check row 1187 (`gap-neutral-pair-check-astra.md` L174) and row 1180 R9 (`gap-mini-neutral-fable.md` L195-197); the
line-spin model and D^+ = infinity are row 1135 L164-177 (check 1138 S6a). What I did not find on file: that the same
model has a finite seed at every fixed coupling with nu(eps) of order (K/eps) log(K/eps), which makes it an explicit
witness that condition (a) of row 1180 does not imply condition (b) even with an exact uniform physical gap. Searched:
"line-spin", "seed size", "nu(", "fixed coupling" in `library/*.md` and `parts/gap.md`.

## 4. What the count adds to a uniform gap at one coupling (written 2026-11-20T08:57Z by date -u; found again)

Work item 2 of Section 2.4. I derived, from reflection positivity and a uniform gap m_0 on the periodic boxes with
sides in [b, 2b] (aspect ratio at most 2, which the four one-direction doublings of b^4 -> (2b)^4 pass through), a
bound of the form: the doubling defect Phi(b) is at most a fixed multiple of exp(-m_0 b/2 + 64 D(b/2)). With
D(b) = sum over k >= 0 of 16^(-(k+1)) Phi(2^k b), this gives D bounded (indeed exponentially small) when
D(b) <= c b for all large b with c < m_0/64. The ingredients: Phi(b) <= 2 times the weighted sum of the thermal
excesses x(b; C) over the four cross-sections C of the doubling chain; the gap on C gives
x(b; C) <= exp(-m_0 b/2 + x(b/2; C)); and x(b/2; C) <= 64 D(b/2) by the reflection-positivity monotonicity of F/|B|
under doubling (row 720 L272). The threshold m_0/64 is that of Corollary Z2 of row 720 (`gap-phys-seed.md` L306,
HOLDS in check row 727 `gap-phys-seed-check.md` L71 and in check row 730 `gap-zd-astra.md` L183), whose liminf form
is stronger (it goes through Theorem ZD), and of Corollary N3 of row 700 (`gap-seed-limit.md` L226; check 727 L106
identifies the two). Found again; no new statement.

I then tried to exclude linear growth D(b) >= c b with c >= m_0/64 from the gap and reflection positivity alone.
Every identity I wrote reads one torus in two frames, G(B) = t c(C) + x(t; C) with c(C) the vacuum Casimir of the
cross-section C and x(t; C) the thermal excess, and the gap only moves weight from the thermal excess in one frame to
the vacuum Casimir in the rotated frame (this is row 1180 R2 = Lemmas Z, Z' of row 720 in another variable). No
manipulation of this kind closed, and the self-consistent linear growth survives them. So the residual statement at
one coupling is (NS-gap) of row 700 (`gap-seed-limit.md` L234, stated there for SU(2) Wilson at the given beta),
unchanged: OPEN. Proposition LS shows that the one comparison model on file
with an unbounded count satisfies (NS-gap)'s conclusion at every fixed coupling, so it is no counterexample.

## 5. Summary, consumers, what stays open (written 2026-11-20T08:57Z by date -u)

**Verdict on the brief.** The mass gap of four-dimensional SU(2) Yang-Mills is NOT proved, and nothing on the chain
is disproved. The infrared input is one estimate for one lattice theory (Section 2.1), and no engine that crosses the
band of order-one coupling is on file or was found here (Section 2.2), in agreement with rows 1225, 1229, 1237, 1238.

**What this row established (author only; checked by no one; one GUIDE run of about one second).**
1. PROVED by hand: Proposition LS (Section 3). In the line-spin comparison model of row 1135 (local, hypercubic,
   reflection positive, simple vacuum, exact physical gap m at every cutoff), every coupling has a finite one-cube
   seed, with (K/eps)(3 log(K/eps) + 6.9) <= nu(eps) <= (K/eps)(4 log(K/eps) + 12), eps = m a; along a -> 0 the seed
   size in physical units diverges like (3K/m) log(1/(m a)), so (N-phys) fails although condition (a) of row 1180
   holds at every cutoff. So condition (b) of row 1180 (asymptotic scaling of the seed size) is independent of
   condition (a) even with an exact uniform physical gap.
2. ARGUED (Section 3, Reading): the count obstruction of row 1135 is an ultraviolet one (light levels per physical
   volume growing like a^(-3)); the one-cutoff route of row 1233 pays it through the account's summable two-cutoff
   increments (the line-spin family has none: its torus excess and its doubling defect at a fixed physical size
   both grow like (L/a)^3, e.g. Phi >= 32 n^3 log Z_line(n) >= 32 (L/a)^3 log(1 + 4 e^(-mL)) with n = L/a), so its
   infrared input is condition (a) at ONE coupling; the all-cutoff route needs condition (b) from an ultraviolet
   argument of the same kind.
3. Wording correction (ARGUED): rows 1225, 1233 and 1238 write "the seed at one coupling, equivalently the lattice
   gap there"; this holds modulo (NS-gap) of row 700 (whether a uniform gap forces a seed at one coupling), which
   stays OPEN (Section 4).
4. Section 2.2 adds anomaly constraints (which forbid but never force a trivially gapped phase) to the list of tools
   that cannot supply the seed by their nature; I made no claim about Zeng's TUN beyond row 1218's reading.

**Consumers.** `parts/gap.md` (registry, R9 / count lines) and the lead's choice between the one-cutoff route (row
1233, check row 1242) and the all-cutoff (N-phys): Proposition LS shows that the cutoff-uniform part of the count is
not implied by a gap, so whichever route is taken must obtain it from the account's ultraviolet control.

**What stays OPEN.** (N-phys); the one-coupling seed (condition (a) at one window coupling); (NS-gap) at one
coupling; the inputs of row 1233's Proposition 3.7 ((EDGE), (DET)'s (ID-a), (ID-b), (I-loc), the account's
outstanding `9.1:prop-blind-site-expansions`); the account's premises on the T0 chain; the Jaffe-Witten mass gap.

**Checks wanted.** Proposition LS (a)-(e) by another provider: a short check (statement, the bounds (b)-(d), and the
limit in (e)). The GUIDE run is not a proof step.

**Credits.** Row 1135's line-spin model and its D^+ computation are gpt-6.2-astra's (checked by Claude Opus 5.5 in
row 1138). Corollaries Z2 and N3 are rows 720 and 700 (Claude). The published works A, B, C of row 1218 are by
Bhattacharjee, Bhattacharya, Lockwood, Romanov, Sessford and Singha Roy (A), Bhattacharjee, Bhattacharya, Lockwood and
Romanov (B), and Zeng Chunping (C); the complete account is by Ethan Sussman and Levent Alpoge, with Claude and Codex
as authors of their text. I used them only as cited readings; no new reading of A, B or C was made in this row.

No subagent was used. Sources fetched: the complete account's part III at commit 31a47c543775 (for the statement of
`9.1:prop-blind-site-expansions`, CA-III 16560-16680), into a scratch folder outside the repository.

RESULT: Row 1234 (Claude Opus 5.5 max, Mac mini worker 1, 08:14Z-08:59Z by date -u; author only, checked by no one; one GUIDE arithmetic run of about one second under the numeric lock; no subagent). The Jaffe-Witten mass gap of four-dimensional SU(2) Yang-Mills is NOT proved and nothing on the chain is disproved; the infrared crux, the one-cube seed of Wilson SU(2) at one coupling in the account's window (a uniform lattice gap plus a fixed-coupling count), stays OPEN, and no band-crossing engine beyond those on file was found (ARGUED, Section 2). PROVED by hand (Proposition LS): in the line-spin comparison model of row 1135 (local, hypercubic, reflection positive, simple vacuum, exact physical gap m at every cutoff) every coupling has a finite seed, with (K/eps)(3 log(K/eps) + 6.9) <= nu(eps) <= (K/eps)(4 log(K/eps) + 12), eps = m a, while the seed size in physical units diverges like (3K/m) log(1/(m a)) and (N-phys) fails at every side; so condition (b) of row 1180 (asymptotic scaling of the seed size) is independent of condition (a) even with an exact uniform gap. ARGUED: row 1135's count obstruction is ultraviolet (light levels per physical volume growing like a^(-3)); the one-cutoff route of row 1233 pays it through the account's summable increments, so its infrared input is condition (a) at one coupling; the wording "equivalently the lattice gap" of rows 1225, 1233, 1238 holds modulo (NS-gap) of row 700, which stays OPEN (found again: the gap plus reflection positivity give only the m_0/64 threshold of Corollary Z2). OPEN: (N-phys); the one-coupling seed; (NS-gap); row 1233's inputs (EDGE), (DET) (ID-a), (ID-b), (I-loc) and the account's outstanding 9.1:prop-blind-site-expansions; the account's premises. Output library/gap-mini-solve-v-opus.md.
