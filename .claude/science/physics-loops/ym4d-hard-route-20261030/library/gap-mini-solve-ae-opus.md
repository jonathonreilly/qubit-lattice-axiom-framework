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

## Step 1. How best to attack it (judgement, ARGUED; written 10:26Z by date -u)

**1.1 What a proof must contain (cited).** Beside the T0 chain, the gap clause reads (N-phys) (Step 0). Row 1180 splits
it into (a) a finite neutral seed at every fine coupling and (b) seed size O(1/a_j). The one-cutoff form (ONE-K)
(row 916, check 917) trades this for a seed at one cutoff plus the ultraviolet carry. Row 1233 Proposition 3.7 pays
the carry from the account's chapter 9 comparison; check 1242 (L52-76) keeps it only after a correction: the exact
decomposition is Phi(d) = P_9(d) + Delta H(d) + D(d), with D(d) = Delta log(S_8(d)/S_9(d)) the relative normalisation of
the chapter 8 and chapter 9 representatives, and row 1233 omitted D.

**1.2 My own screening of the infrared seed, grepped before any work (rule 0a).** Each idea is on file or dies at once.

| Idea | Status |
|---|---|
| Seed from strong spatial mixing (Dobrushin-Shlosman, Martinelli-Olivieri) at one coupling | FALSE as an input: mixing uniform over boxes and boundary data fails at every coupling of the window, because pinned slabs order (Proposition CA-FAIL, `gap-bridge-exercise-opus.md` L337, L463; check `gap-bridge-exercise-check-opus.md` L280) |
| Seed in small physical volume with twisted (twist-eater) boundary data, where the account controls the flow | dies at the massless floor: every scale-invariant spectrum gives the same s(L/K; L) at every L, so K must make the free gluon fail, and then small volumes fail too (method 26, row 988 Lemma FLOOR) |
| Degree-one gauge twists on the boundary of a 4-ball as a continuous stiffness (the instanton analogue of the 2D twist) | dies on the lattice: SU(2)^links is connected, every gauge twist of pinned data is removable (row 1013 Lemma TWIST); only centre twists survive (CEN+, row 1016) |
| Lossy mixing length at one weak coupling, as in OpenAI's 2D Proposition 2.1 | on file as the crux in that form (row 1229); a Jensen step with any bounded flow sees screening in one-loop 4D (row 1244) |
| Lower bound on the deconfinement temperature in physical units | it is (N-phys) (row 1199 table, "Thermal form") |
| Strong-coupling expansion of the Kogut-Susskind Hamiltonian in x = 2/g^4 | a (K-one) number at x about 0.7, far outside any hand-provable radius (rows 1229, 1251 1.2) |
| Migdal-Kadanoff or Tomboulis decimation bounds | route RG, retired (`parts/gap.md` L76-78; rows 797-801) |

Verdict (ARGUED): no engine off the record; the infrared seed at one coupling stays OPEN, as in rows 1219-1251.

**1.3 Choice for this row.** Rule 0 asks what changes. The one-cutoff carry (row 1233 Proposition 3.7 as corrected by
check 1242) is the step that turns a seed at one cutoff into (N-phys) along the trajectory. Its remaining open input
named by check 1242 that no row has attacked (grep at da81f7368: "S_8", "relative normalisation" hit only check 1242) is
D(d). Check 1242 L60-66 says what suffices: S_9 = S_8, or D constant on each predecessor chain, or D(d) - D(d_0) <= sigma
with sigma below the seed margin; and it names the likely mechanism: "If the sole difference can be identified as the
same omitted levels on both tori in the same vacuum family, the wrapping estimates above also bound that subseries."
This row does that identification from the account's text and then bounds D by hand. Moves: (ONE-K)'s carry of the
gap clause. Success: Proposition 3.7 holds with sigma explicit and small on large tori, modulo the account premises
check 1242 lists. Failure: the first account statement that the identification needs, by label and line.

## Step 2. What the account says about the two normalisations (READ; started 10:27Z by date -u)

Source: Sussman and Alpoge's complete account at commit 31a47c543775 (`theorem_0_complete_account_raw_I/II/III.tex`,
fetched into a scratch folder outside the repository; credit Ethan Sussman and Levent Alpoge, with Claude and Codex as
authors of their text; their construction uses Balaban's). Line numbers below are of those files.

**2.1 The chapter 9 mass (READ III:11812-11960, III:18136-18310).**
- Runs (III:11814-11818): A has length n and real centre zeta_*^n + u; B has length n+1 and centre
  zeta_*^(n+1) + n_n(u), with n_n the matching map. The flow stops at depth w = w(g); the last lattice T_w has
  N_w = 2L^(m_0 + w) sites per side; the stop level is k = n - w (III:11824-11831).
- Normalisation (III:11849-11860, eq. 9.1:eq-centre-normalisation-a): Z^c(c^c; v) = e^(E^c(v)) Z~^c(v), where Z^c is
  "the sourced integral of the run c at the stop", E^c(v) = sum_j sum_X [e^(j),c(X; c^c + v) - e^(j),c(X; c^c)] and
  Z~^c(v) = sum_h tau_h^c(v)(V_w). At zero residual source E^c(0) = 0, so Z^c(c^c; 0) = Z~^c(0) (III:11906-11907).
  So the chapter 9 mass at zero source, S_9 in check 1242's notation, is the sourced integral of the run at the stop.
- Remark 9.1:rem-centre-normalisation-b (1) (III:18226-18232, proof III:18286-18302): the vacuum constants that do not
  depend on z sit inside tau_h^c and are counted in the total load; "The normalisation admits exactly one free positive
  constant for each run and each centre."
- Corollary 9.1:cor-sourced-integrals (III:18136-18157): |Z~^B - Z~^A| <= eps*_n A at every source of P_IR and at the
  zero residual source, eps*_n <= C*_TC(N_w; g) e_w, with C*_TC independent of n.

(continuing: the step constants of the run between the bare level and the stop, and chapter 8's H_T.)
