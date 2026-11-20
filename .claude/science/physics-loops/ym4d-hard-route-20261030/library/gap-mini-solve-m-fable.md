lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T17:25Z

# gap-mini-solve-m-fable: four-dimensional SU(2) Yang-Mills mass gap (row 1212)

Started 2026-11-20T05:25Z (date -u). Pinned commit b8c2bc658, branch
claude/ym4d-hard-route. Model: Claude Opus 5.5, max reasoning (the row's Fable
model hit its weekly limit; see the lead note in row 1212). No earlier text of
this item was on file at the pinned commit.

Labels: PROVED, ARGUED, GUIDE, OPEN, as the row asks.

## Step 0. Reading (written 2026-11-20T05:37Z, `date -u`)

Read for this row (bounded reads; no whole part file): GOAL.md in full; FINISH.md L1-85 and L299-352 (rules,
efficiency, joining); the RESULT text of rows 916, 917 and 1179-1227; `parts/gap.md` L1-104 (state of attack, routes
tried, lead rules); `library/gap-mini-branch-fable.md` L167-366 (Theorem L3-ev, Propositions P-ev and P'-ev,
Theorem BP, the statement of (N-phys)); the plan and stopping sections of the sibling rows of today,
`gap-mini-solve-n-fable.md` (L28-41, L83-140), `-o-` (L41-81), `-q-` (L1-102, L261-285). A grep of 28 further tool
names over `library/*.md` and `parts/*.md` (Bourgain, Kazhdan, expander, uncertainty principle, the x^2 y^2 potential,
Lieb-Thirring, NSVZ, low-energy theorem, anomaly matching, Georgi-Glashow, adjoint Higgs, Banks-Zaks, conformal
window, bootstrap, Kazakov, Kruczenski, spin foam, Lojasiewicz, Gaiotto, theta = pi, Elitzur, Bianchi, monopole,
Gopfert-Mack, Debye, Witten index, Kogut-Susskind, spin network): every name except "expander", "Banks-Zaks" and
"Witten index" has hits, and the conformal-window and Georgi-Glashow families are in the comparison tables
(`parts/gap.md` L293; `gap-outside-box-max.md` I11; `gap-compact-rigidity-max.md` A16).

**Where the problem stands on file (cited, not re-derived).**

1. The gap clause of the Jaffe-Witten target reduces to one lattice input, (N-phys), plus the continuum datum.
   Statement (row 1179 L304-310, from row 1161 L146-148): at one admissible physical side L, for every cutoff index
   j >= j_0, with n_j = L/a_j and 4 | n_j, some integer u_j with 3 <= u_j <= n_j/K has s_+(u_j; n_j^3) <= 1/2, where
   s_+ is the periodic centre-neutral excited trace of the spatial cube in units of its vacuum. The reduction is
   Theorem BP of row 1179 (checked across providers in row 1183, HOLDS AFTER CORRECTION). The branch selection (BS)
   is not an input of the gap clause.
2. The continuum datum ((H2), (TOT), (P1)-(P4)) on the tr F^2 sector is PROVED GIVEN the account's premises: row 916
   Theorem E, checked by gpt-6-astra in row 917 (HOLDS AFTER CORRECTION). It stays open with the T0 chain. (UNIV-K)
   of row 916 is open but is needed only for the one-K form; row 1180 notes that for one continuum datum a liminf
   along a subsequence suffices.
3. (N-phys) is open. In physical terms it asks for a dilute glueball gas at Euclidean time about 25/M in a box of
   side about 1.25e4/M (row 1219 Section 2, GUIDE arithmetic). About twenty plain-brief rows (1188-1225) and the
   astra chain (rows 1143-1227) end at the same statement: an estimate at one physical scale where the running
   coupling is of order one, uniform in the cutoff, that fails for massless comparison models. Rows 1219 and 1224
   recommend that a new row take one precise question with a consumer instead of another blind search.

## Step 1. How to attack it (in progress)
