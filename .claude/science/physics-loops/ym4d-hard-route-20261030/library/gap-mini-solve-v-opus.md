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

