lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T23:38Z

# gap-mini-solve-aj-opus: mass gap for 4D SU(2) Yang-Mills (FINISH row 1264)

Started 2026-11-20T11:38Z on the Mac mini Claude worker 3, at commit 6c33935f9 of
branch claude/ym4d-hard-route. Claude Opus 5.5, max effort. Not committed by this
worker; a relay copies the file.

Labels: PROVED (written argument, checkable by hand), ARGUED (argument with a named
gap), GUIDE (heuristic or numeric guide, never a proof step), OPEN.

## Step 0. Orientation (written 2026-11-20T12:05Z by date -u)

**Read for this row.** GOAL.md; FINISH.md L1-84, L299-352 and row 1264; `library/prior/gap-onebound-read-sol.md`
(row 1218) in full; `parts/gap.md` L1-104; the RESULT lines of the gap-mini-solve rows a-ag (rows 1188-1258); row 1258
(`gap-mini-solve-ag-opus.md`) Sections 1, 4, 5; row 1233 (`gap-mini-solve-u-opus.md`) 3e-4; the opening of row 1260
(`gap-mini-solve-ai-opus.md`, worker 2, on (FI) at pins); `library/gap-bridge-exercise-check-opus.md` L250-300
(Proposition CA-FAIL as checked). Source fetched by URL into a scratch folder outside the repository: Sussman and
Alpoge's complete account, part III, at commit 31a47c543775 (`theorem_0_complete_account_raw_III.tex`; credit Ethan
Sussman and Levent Alpoge, with Claude and Codex as authors of their text, after Balaban). III:n below is its TeX line.

**What the record fixes (pointers to evidence, not evidence).**
- Beside the account's premises, the gap clause on the tr F^2 sector reads one infrared input, (N-phys) (rows 1161,
  1179, 1225; check 1232). On the one-cutoff carry it reads instead a seed at one base datum (rows 916-917, 1233, 1255,
  1256), and row 1258 (check 1265: holds after correction) states that base datum in its weakest proved-sufficient form:
  (SL), a bound tau_* on the total-variation dependence of a slab's middle slice on one boundary slice, uniform over all
  boundary slices, at ONE coupling in the window, slab thickness a few tens of correlation lengths.
- The one-cutoff carry also reads: (FI) at pins (row 1260 is on it now), (V9) at pins (row 1255; its check, row 1263, is
  running), the hypotheses (a)-(e) of the account's `9.1:thm-last-lattice-comparison` with (e) =
  `9.1:prop-blind-site-expansions` (III:16558, "Proof outstanding"), (DET)'s inputs (rows 987-994), clause (0)'s
  torus-independence lemma, and the account's premises. Row 1233 point 3: this route pays for clause (v) machinery,
  which `library/port-map.md` F3 puts off T0's chain.
- About eighty plain-brief rows found no engine that carries a selective input across the band (route registry RA-RG,
  methods 19-36 of `parts/gap.md`; the screening tables of rows 1189, 1194, 1199, 1237, 1256). Row 998 9.5 asks for no
  further fresh-framing exercise.

**Running beside this row (files not visible at this pin):** row 1259 (`gap-mini-solve-ah-opus`, worker 1; its file
holds only a header at this pin) and row 1260 (worker 2, (FI) at pins). Overlap with row 1259 cannot be checked here.

## Step 1. How to attack it, and the item chosen (written 2026-11-20T12:40Z by date -u)

**1.1 The crux (judgement, ARGUED; no new screen).** The open core is the base datum: (SL) of row 1258 at one coupling,
or (N-phys) at every cutoff. Either is a lattice gap of Wilson SU(2) with a volume-uniform count at order-one coupling,
with no small parameter. The worst-case forms are refuted at the window: suprema over pinnings (CA-FAIL, row 1072, check
L250-300 of `gap-bridge-exercise-check-opus.md`), over tilts (Theorem D2, row 977) and over coupling fields (Lemma SHEET,
row 996). The posted 2D O(N) mechanisms have no 4D carrier on gauge-invariant data (rows 1011-1016, 1228, 1229, 1241,
1243). I checked each idea I had against the record before working it: spectral independence and localisation schemes
(pinning or tilt suprema: CA-FAIL, D2), Polchinski-flow log-Sobolev (method 31), Birkhoff contraction of the slab kernel
(row 1258 Proposition RR), Durhuus-Frohlich slicing, Mack-Petkova and Tomboulis-Yaffe vortex inequalities,
Knabe-type local-gap criteria, Kogut-Susskind strong-coupling bounds (each term has 13 to 67 hits in `library/`), and the
newest literature (`library/prior/gap-lit-refresh-2026-11-20-luna.md`: no new unconditional 4D result to 2026-11-19).
I found no route off the map, so I do not attack the crux head-on in this row. This repeats the judgement of rows 1209,
1219, 1233 and 1258; it is recorded only so that the lead can see this row did not skip the crux.

**1.2 Items considered and set aside.**
- `9.1:prop-blind-site-expansions` (III:16558, "Proof outstanding"; on the one-cutoff carry; no owner, no FINISH row
  attacks it). Its route (III:16620-16760) is to repeat Balaban CMP 116 Section 2 with island-blind lengths. CMP 116 is
  not in the papers folder, and Project Euclid answered the PDF request with a bot check (Incapsula), so I stopped there
  as the rules require. Blocked for this worker; the account's five route points are not checked here.
- (FI) at pins: row 1260 works on it now. (V9) at pins: row 1255 with reading (R); its check (row 1263) is running.
  (DET)'s inputs: rows 990-994 with checks. (MON): only on the first-passage-top route (row 1256).

**1.3 Item chosen: H-C6a.** `8.6:lem-prefactor-monotone` (CA-II:102730-102830), the monotonicity of the common
prefactor under island removal, "Stated; proof incomplete at the step marked (*)". Registry row H-C6a
(`library/open-registry.md` L246): owner none, standing OPEN. Tree node: "R9 witness analytic inputs"
(`library/t0-tree.md` L213), on T0's chain through the finite-cutoff witness (non-triviality, which the Jaffe-Witten
statement needs: a gap of a trivial limit says nothing). Rule 0a: no FINISH row, no `library/open-core.md` entry and no
`library/l17c.md` entry names it (grep of `prefactor-monotone`, `H-C6a`, `Monotonicity of the common prefactor`).
The step (*) (CA-II:102804-102816) asks: on the cubes of side L M_2 R_k of a healed island X_a, wherever the
preparation's small-field characteristic function (CMP 122a (1.3)-(1.4)) equals 1, the step's own (CMP 119 (2.17),
(3.2)) also equals 1. The account gives two reasons that do not compare the thresholds and leaves the comparison open
("It remains to compare the thresholds ...", CA-II:102814-102816).

Moves: H-C6a (T0 tree, R9 witness analytic inputs). Success: (*) proved from the two papers' definitions, so the lemma
is an implication of its cited inputs. Failure: an explicit configuration on one cube where the preparation's
characteristic function is 1 and the step's is 0; then (8.6:eq-prefactor-monotone-a) fails as stated and the lemma
needs a different comparison. Either outcome changes the registry row.
