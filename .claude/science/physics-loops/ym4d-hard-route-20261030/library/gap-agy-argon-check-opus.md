lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T13:10Z

# gap-agy-argon-check-opus: cross-provider check of row 1205 (`library/gap-agy-solve-argon.md`)

Queue row 1206. Worker: Claude Opus 5.5, reasoning max, Mac mini Claude worker 2,
pinned at commit beea72f25. Lease start from `date -u` = 2026-11-20T01:10Z.
Checked file: `library/gap-agy-solve-argon.md` (row 1205, gemini-4-argon-high).
Provenance: this check is by a different provider from the author of the
checked file; it is one reader, not an independent derivation unless a
statement below says that a separate derivation was made.

## Plan (at most eight steps; each response does one step and appends)

1. Read the checked file in full, rows 1141, 1188-1190, 1196, 1205 and the
   FINISH rules (Build on published work, efficiency); list every PROVED
   statement with its line numbers.
2. Theorem 2.1, line by line.
3. Theorem 2.2, including the norm 1/256 and the Casimir gap 12.
4. Theorem 2.3 and Proposition 2.4 (volume bound on the Perron eigenvalue:
   correct? anything beyond normalization?).
5. Theorems 3.1-3.3; does 3.3 answer row 1141 as claimed?
6. Proposition 4.1.
7. Novelty: grep library/open-core.md and the FINISH rows for each
   statement, name the matching row; numeric guide only if memory allows.
8. Verdict table (HOLDS / HOLDS AFTER CORRECTION / FAILS), rating against the
   plain-brief rows 1188-1190 (checked in 1196), RESULT line.

## Step log

### Step 1. Inventory (done)

Read in full: `library/gap-agy-solve-argon.md` (343 lines at beea72f25), the
FINISH rows 1034, 1132, 1141, 1142, 1188-1190, 1196, 1205, and the FINISH
sections on building on published work, efficiency and rules. Memory was
42 percent free at the start (`memory_pressure`), below the 50 percent floor,
so no numeric job is started; every step below is by hand.

Statements labelled PROVED in the checked file, with lines:

| Id | Lines | Claim in one line |
|---|---|---|
| S1.1 | 19-25 | PROVED GIVEN rows 1161, 1179, 1183: gap clause splits into the continuum datum, (N-phys), and (BS) is needed for (W) only |
| T2.1 | 68-81 | A*A / AA* isospectrality of F_+ and the electric sandwich; identity (2.3) |
| T2.2 | 87-109 | Peter-Weyl selection rules; Casimir gap 12; C_E norm a_2^4; W_E norm 1/256 on the neutral complement |
| T2.3 | 115-127 | Courant-Fischer bounds (2.7)-(2.9) |
| P2.4 | 131-154 | lambda_0 <= ||M||_inf^2 exp(-c_0 n^3); ratio (2.10) >= 1 |
| T3.1 | 179-194 | integration by parts (3.1)-(3.3) from Identity STAR (3.4) |
| T3.2 | 208-232 | marginal equations (3.7); 2-link read sets; "6 raised to 9" |
| T3.3 | 242-269 | tree-transport frame: (3.10)-(3.14) |
| P4.1 | 284-302 | Le Cam chain (4.1)-(4.3); threshold (4.4) |
| S4.2 | 308-315 | comparison-model table, labelled PROVED |

Note on the FINISH summary of row 1205: it names "a magnetic-variance ratio
Theta_mag" and "OPEN: uniform-in-n bounds on Theta_mag". The file at
beea72f25 has no Theta_mag; the nearest object is the covariance term of
(2.7). This check reads the file as it stands.

