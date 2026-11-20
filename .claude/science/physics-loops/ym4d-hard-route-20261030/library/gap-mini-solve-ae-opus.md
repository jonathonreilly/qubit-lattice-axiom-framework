lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T22:11Z

# gap-mini-solve-ae-opus: mass gap for 4D SU(2) Yang-Mills (queue row 1255)

Started 2026-11-20T10:11Z (date -u) at commit da81f7368 on branch claude/ym4d-hard-route. Research-stage working state; no status, no public claim.

Labels: PROVED (every step written here or in a cited checked note), ARGUED (argument written, a step not fully closed), GUIDE (heuristic or numeric guide only), OPEN.

## Step 0. Reading and plan

Reading done by 2026-11-20T10:15Z (date -u). Read: GOAL.md in full; FINISH.md L1-90 and L299-356 (rules, joining, efficiency);
queue row 1255 in full; the RESULT lines of rows 1161, 1179, 1180, 1183 and 1200-1256; `parts/gap.md` L1-104;
`library/prior/gap-onebound-read-sol.md` L19-218 (row 1218); the screening tables of rows 1189 (`gap-mini-solve-b-fable.md`
2.1), 1194 (`gap-mini-solve-e-fable.md` 2.1) and 1199 (`gap-mini-solve-i-fable.md` 1.2); the sibling row 1251
(`gap-mini-solve-ad-opus.md`, running, Zeng's package) in full.

**What the record fixes (cited; not re-derived).**
- The gap clause on the tr F^2 sector reads one open lattice estimate beside the account's premises: (N-phys)
  (row 1161 L146-148; row 1179 Theorem BP, check 1183 HOLDS AFTER CORRECTION; row 1225 Theorem E-N, check 1232).
  In the notation of row 1218 L33-44: there are L and j_0 such that for every j >= j_0 some integer u_j with
  3 <= u_j <= n_j/K has s_(+,j)(u_j; n_j^3) = Tr_(H_(+,j)) U_j^(u_j) - 1 <= 1/2, where U_j is the vacuum-normalized
  periodic transfer of the spatial cube of side n_j = L/a_j and H_(+,j) its centre-neutral sector.
- Row 1180: (N-phys) holds iff every fine coupling has a finite one-cube seed nu(beta_j) and limsup a_j nu(beta_j) is
  finite. Row 1233 (check 1242: HOLDS AFTER CORRECTION, conditional) pays the second half from the account's
  two-cutoff comparison, given its representatives. Row 1234 (check 1250 HOLDS): a uniform lattice gap alone does not
  give (N-phys).
- About 45 route families are on file with a first failing step (rows 1189, 1190, 1194, 1199 tables; `parts/gap.md`
  methods 19-36; route registry RA-RG). Every one stops at one of: a one-scale number at order-one coupling (K7,
  Proposition V), a selective non-abelian step with no identity fixing its sign (lead rule W2, row 1243), or the
  neutral conversion (SING) with no association (rows 1115, 1194, 1241).

**Plan (written before the attack).** Step 1 decides the attack by asking which statement, if proved, changes what the
lane does, and checks it against the record by grep. Steps 2 onward do the attack, one stage per response, each
appended here with its label. The last step states what stays open and ends with one RESULT line.
