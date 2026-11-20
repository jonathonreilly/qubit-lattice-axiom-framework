lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T19:59Z

# gap-mini-solve-x-opus: the mass gap for four-dimensional SU(2) Yang-Mills

Queue row 1238 of `FINISH.md`. Worker: Claude Opus 5.5, max effort, Mac mini worker 2, at branch
`claude/ym4d-hard-route` commit 6150ee2a3. Started 2026-11-20T07:59Z (date -u).

Labels: PROVED (complete written argument here or cited with its proof on file), ARGUED (argument
given, a step not fully written), GUIDE (heuristic or numeric orientation only), OPEN.

## Step 0. Reading log (reading only; no new claim)

Read at this pin: GOAL.md; FINISH.md L1-90 and L299-356 (rules, joining, efficiency) and the RESULT lines of rows
1218-1239; `parts/gap.md` L1-104 (state of attack, routes 1-36, lead rules); `library/prior/gap-onebound-read-sol.md`
(row 1218) in full; `library/gap-mini-solve-r-fable.md` Sections 1-4 (row 1225: Lemma A0, Theorem E-N);
`library/gap-mini-solve-t-opus.md` Steps 1.3-3 (row 1229); `library/gap-mini-solve-w-opus.md` Steps 0-1 and its
RESULT (row 1237); `library/gap-mini-solve-u-opus.md` (row 1233, as it stands at this pin: chapter 9 of the
complete account against (UNIV-K)); the statement table of `library/gap-univk-opus.md` (row 924, L430-466).

Where the problem stands on file (cited, not re-derived):

- Beside the account's premises (the T0 chain), the Jaffe-Witten gap clause on the account's tr F^2 sector follows
  from one lattice estimate, (N-phys) (row 1225 Theorem E-N; cross-provider check row 1232 HOLDS AFTER CORRECTION).
- (N-phys) holds iff every fine coupling has a finite one-cube seed size nu(beta_j) with limsup a_j nu(beta_j) finite
  (row 1180, checked 1187). Given (UNIV-K), a seed at one cutoff's window suffices (row 916 (ONE-K), checked 917).
- (UNIV-K) is OPEN in (MAPCONV), (VAC-ID), (DENS-K) B1-B2 (row 924); (CLASS) closed in corrected form and two clauses
  of (MAPCONV) by row 1237; row 1233 (running in parallel on worker 3) reads the account's chapter 9 for it.
- The infrared seed has no route: every structure valid at every coupling on file (twist stiffness, positivity,
  curvature, dilute defect duality, exact recursion, compactness) has a cited failing step (rows 1225, 1229, 1237
  tables; screening tables of rows 1189, 1194, 1199). Row 998 9.5 lists another fresh screening by this model family
  as waste.

Rule 0a: `library/open-core.md` has no gap-lane item (row 1237 Step 0 grep, repeated here for "N-phys", "neutral",
"seed": no hit outside hard-core rows). Gap rows 1161-1239 are the FINISH matches.

## Step 1. How best to attack it (judgement, ARGUED; written 08:15Z by date -u)

**1.1 The two open inputs of the gap path (cited).** Beside the T0 chain, the gap clause needs (N-phys). By row 916
(ONE-K) (checked 917), (N-phys) follows from a seed at ONE cutoff's window plus the ultraviolet carry (UNIV-K). So a
proof needs (A) the carry (UNIV-K) and (B) one infrared estimate at one fixed coupling, a lattice gap of Wilson SU(2)
with a finite seed (rows 1225, 1229, 1237 Step 1.1).

**1.2 Part (B), the seed.** I tried, before reading further, to name a band-crossing engine of a kind not in the
tables of rows 1229 (Step 1.2), 1237 (Step 1.2) and the screening tables of rows 1189, 1194, 1199. Each candidate I
could name maps to a row on file:

| Candidate | Where on file |
|---|---|
| level derivative of the seed size in beta (a K-flow bound d log nu/d beta <= C, consistent with asymptotic scaling) | (VIR), rows 708-711, 895, 934, 1128: needs kappa about 7 on the band |
| remnant global colour symmetry of a complete gauge (Landau, Coulomb, tree) as the rigid group of the 2D stiffness engine | frames, rows 1041, 1045, 1141; typical-field frame repair reads first-passage data (rows 1013, 1016 7.4) |
| confinement (string tension) implies the neutral gap | not true blind: a decoupled massless neutral factor keeps the area law; product tests of Lemma PT, Proposition NP |
| Schwinger-Dyson (loop) equations, whose splitting terms are the non-abelian part | master-loop contractions work at strong coupling only (Chatterjee; Basu-Ganguly; row 1199 table, random surfaces) |
| electric-basis (spin network) energy counting, glueball as closed flux | strong coupling only; at weak coupling the basis is not diagonal (rows 1132, 1215) |
| a positive dual for the heat-kernel action | crosscap and 6j signs (method 35, rows 737, 744, 878) |
| finite subgroup 2I at the window | frozen-group comparison cases (rows 884, 998); not frozen at beta 2.3-2.6 |

So I do not claim an attack on (B), and I do not screen further (row 998 9.5).

**1.3 Decision: part (A), sub-item (MAPCONV-F).** Row 1237 Step 3 closed (CLASS) in a corrected form and the
transport, norm and b clauses of (MAPCONV), with one ARGUED step (Lemma 3.2: the classical field map B_xi of
(hit:actual-transferred-pointing) does not read the depth below the old scale). It left

    (MAPCONV-F) on the common domain, sup abs(r^A_j - r^B_j) + ||n^A_j - n^B_j|| + sup ||f^A_j - f^B_j|| <= C lambda_0^j,

"Not attacked further here". Rule 0a (grep at 08:16Z): open-core.md has no match; the only FINISH or QUEUE_DONE row
whose text names MAPCONV is 924; library files naming it are rows 924, 925 (check), 934 (in passing), 1225, 1229,
1233, 1237. None attacks (MAPCONV-F). Row 1233 (running) asks a different question, whether the complete account's
chapter 9 supplies (UNIV-K) as a whole. If it does, this step becomes moot, and I say so in the result.

Moves: (UNIV-K), the carry, which is needed even when a seed exists, because a structural seed bound is not expected
to be sharp (the 2D O(3) proof needs its RG carry for the same reason, row 1010). Success: the regular part of
(UNIV-K) is closed given endpoint matching. Failure: the exact missing account statement, by name and line.

Plan: (1a) fetch YM4_1400.tex at 2bc0658f91d2 into a new scratch folder; (1b) trace B_xi (the ARGUED step of row 1237
Lemma 3.2); (1c) read the definitions of r_j, n_j, f_j and find what each reads of the depth and the frame;
(1d) prove (MAPCONV-F) clause by clause or name the first clause that needs an estimate the account does not make.
