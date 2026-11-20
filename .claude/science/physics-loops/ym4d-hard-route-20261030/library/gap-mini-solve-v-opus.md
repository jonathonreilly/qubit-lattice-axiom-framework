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

## 1. Reading log and where the problem stands (reading only; no new claim)

Read at this pin (56e523e38): GOAL.md in full; FINISH.md L1-84 and L299-351 (rules, joining, efficiency, rules) and
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
   an explicit finite-volume neutral trace bound (row 1225 Section 4; row 1233 Section 4). Twenty-five plain-brief rows
   (1188-1238) found no engine that crosses the band of order-one coupling; the screening tables are rows 1189, 1194,
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

- 2026-11-20T08:50Z (date -u) Section 2 (judgement and choice of work) written.

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
by its nature: an anomaly forbids a trivially gapped phase but never forces one, and Zeng's two-well picture has no
two isolated non-degenerate minima for the Wilson action (its minima are the flat connections, a continuum of
torons). I found no engine of a new kind, which matches rows 1225, 1229, 1237 and 1238.

**2.3 What the sibling rows now cover (read at the branch tip 86fcc62, not at my pin).** Row 1238 (x) works on
(MAPCONV-F) of (UNIV-K) in YM4_1400 and records that the gap chain reads YM4_1400 while row 1233 read the complete
account's chapter 9; row 1233's remaining inputs are (EDGE), (DET)'s (ID-a), (ID-b), (I-loc) and the account's
OUTSTANDING `9.1:prop-blind-site-expansions`. I read that proposition's statement and route (CA-III 16560-16680,
fetched into a scratch folder at commit 31a47c543775): it is a repeat of Balaban's CMP 116 Section 2 expansion with
island-blind inputs at three sites, a multi-row project, not a session item. (EDGE) depends on which text defines the
first-passage data, which row 1238 has raised for the lead; I do not take it.

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

