lead: Anthropic/claude-opus-5-5/max laptop subagent, FINISH row 1302
lease_until: 2026-11-21T03:54Z

# Exercise: the directional zero-point wall in the reflection-positivity tiling (row 1302)

**Who wrote it.** Anthropic, Claude Opus 5.5 (claude-opus-5-5), maximum effort, one laptop Claude subagent session, FINISH row 1302. `--subagents 0`: every "pass" below is a context-isolated pass by this one session, so no pass is independent of another.

**Commit.** Branch `claude/ym4d-hard-route` at f0070179d for steps 0-8.2. Between 16:17Z and 16:37Z another process moved this clone to e1176ef2d (no git command of this run); row 1301's file and the re-checks of 8.3 were read at e1176ef2d. Skill and governance reference read from origin/main at 8b11ae2bb (no fetch run; freshness not re-verified beyond that ref).

**Date.** 2026-11-20 (UTC).

**Nothing in this file is checked by another model.**

**Framework refresher replaced.** This is a standalone proof target. Its `GOAL.md` contract reads no framework axiom or primitive. As the skill allows, this run read `GOAL.md` in full and `FINISH.md`'s sections "Where it stands", "What finishing means", "How we work", "Working efficiently" and "Rules" in place of the framework refresher list.

**What this run did not cover** (kept current):

- `FINISH.md` was searched, not read whole (about 2.7 MB).
- Closed files read in part only (step 5 lists the lines): rows 1273, 1286, 1274 at the lines named; rows 748 and
  750 by grep only; the crux exercises of rows 878, 998, 1003 by grep only. Row 1285 was read in full.
- Row 1301's file read in part (outline, L9-50, L137-162, L270-308), after step 5, because it appeared then; its
  proofs were not checked.
- No blind check of the plain wall (no subagents). No independent check of any statement: the adversarial pass of
  8.3 is a second pass of the same session.
- The open PR branches were not searched (no git fetch; the brief forbids git writes).
- Literature: the lane's records (rows 749, 729, 1216) plus two web queries whose sources were seen as abstracts
  or listings only.
- The two runs (8.1, 8.2) are free-field GUIDE runs; no Wilson SU(2) computation was made. The twisted overshoot
  and the sign of the eight-flux defect at finite coupling are tree-level guides.
- Row 1259's Lemma CD (the existence of the pressure limit) was not read; the sandwich's lower half is stated with
  a limsup so that it does not depend on it.

## Status block

| Step | State | Main result |
|---|---|---|
| 0 Locate record | done | open and closed lists written; literature record reused (rows 749, 729, 1216) |
| 1 Wall twice | done | plain and precise versions; no blind check (no subagents) |
| 2 Inventory | done | 38 marked items; tests: U(1)^3, photon product, adjoint Higgs, n = 1, strong coupling, massive scalar |
| 3 Reason up | done | C1-C8: the zero-point energy cancels from every normalized trace; RT-iii is priced at the Theorem S seed; deficit lever worth at most a factor ~71 |
| 4 Assumptions | done | 31 rows in six groups; top: tiling from provable small blocks (c1, c6); "the defect binds" (c3, c4) |
| 5 Earlier work | done | most of C2-C8 found again (rows 697, 708, 720, 751, 988, 1032, 1285, 1291, 1292); new: C1, the zero-deficit floor, RT by N, the sandwich l^3 sigma_3(l) <= D_l <= 14 log X_full(l/2; l) |
| 6 Filters | done | 18 methods; verdict 3 (budget 10^(-8)) too strong as a requirement, corrected per N; deficit-only hypotheses fail the log 2 test (row 1028); no tool comes back on the path |
| 7 Routes | done | six passes (not independent); R4 misframing survives; R6/R2 twisted blocks wounded; R1, R3 dead; R5 deferred |
| 8 Attempts | done | 8.1 PASS (sandwich holds on 30 free-field points; lower half tight to a factor about d); 8.2 HELPFUL-OVERSHOOT (twisted blocks above the bulk by 0.656/l, GUIDE), and Lemma FL kills R6; late comparison with row 1301; adversarial pass (same session) found no failing step |
| 9 Report | done | exact price (argued): the wall is the seed at one block, priced from both sides; the zero-point energy is not a lever on it; three work items, the first a cross-provider check |

## Step 0. Where the record of the wall is; what is open and what is closed

Written about 2026-11-20T15:58Z (estimated afterwards; date -u was not called at the time). The brief of FINISH row 1302 supplies the lists below. This run added the
object search (by "Casimir", "zero-point", "E_0(K_n)", "Casimir defect", "ES-1", "e_inf", "vacuum energy" over
`library/`, `parts/`, `gates/`, `checks/`), which found 138 files that mention "Casimir" and 19 that mention ES-1.
Only those named below were opened before step 5.

**Open now (read before step 2).**

| Item | Where | What was read |
|---|---|---|
| Target | `GOAL.md` (T0; "Later targets: ... the mass gap") | in full |
| Lane rules | `FINISH.md` sections "Where it stands" to "Current order", "Working efficiently", "Rules" | those sections |
| The wall | row 1285, `gap-owner-tiling-opus.md` L350-436 (Remark RT, its Consequence, the "On file" paragraph, Lemma E0, the tree-level Reading, verdict items 1-2) and L489 (RESULT) | those lines only |
| Check of the wall | row 1292, `gap-owner-tiling2-check-astra.md` L30-56, L85-96, L111-114, L135 | those lines only |
| One-block gap | rows 1273 and 1279, FINISH RESULT lines | RESULT lines only |
| Sewn tilings | rows 1286 and 1287, FINISH RESULT lines | RESULT lines only |
| (N-phys) | `gap-mini-neutral-fable.md` L30-70; row 1161 `gap-solve9-astra62.md` L140-150 | those lines |
| Theorem E-N | rows 1225 and 1232, FINISH RESULT lines | RESULT lines only |
| Row 697 (checked by rows 698, 699) | `gap-crux-restate.md` L29-46, L86-124, L170-230: (TM), (TM-c), Lemma A, Theorem D, Corollary D2, Proposition R, Lemmas K, X, E, E', Theorem S, Corollaries S2, S3, S3' | statements and their short proofs |
| Literature | `prior/gap-lit-casimir.md` (row 749) in full; `prior/gap-small-volume-lit.md` (row 729) in full; `prior/gap-lit-refresh-2026-11-20-luna.md` (row 1216) in full | statements of results only are used before step 5 |

**Closed until step 5.**

- Route discussion of `gap-owner-threeaxis-opus.md` (row 1273), `gap-owner-tiling-opus.md` (row 1285, outside the
  lines above), `gap-owner-tiling-astra62.md` (row 1286), `gap-owner-movingsites-opus.md`.
- The (ES-1) attack files of rows 748-753: `gap-es1-astra.md` (748), `gap-crux-exercise-astra.md` (750),
  `gap-es1-opus.md` (751), `gap-es1-opus-check.md` (753). Rows 749 and 752 are literature records.
- `parts/gap.md`'s method digest and route registry.
- Row 1291's file `gap-mini-solve-ar-opus.md`.
- Row 1301's file `gap-owner-tiling3-astra62.md` (running now; absent at 15:54Z).
- Earlier exercises that mention the wall's objects (by the search above): `gap-crux-exercise-max.md`,
  `gap-crux-exercise2-max.md`, `gap-crux-exercise3-max.md`, `gap-crux-exercise4-max.md`,
  `gap-crux-exercise-r858-max.md`, `gap-form-exercise.md`, `gap-face-exercise-fable.md`; and the object hits
  `gap-start-values.md`, `gap-wall-assume-max.md` and their checks.

**Incidental exposure, declared.** Row 1301's FINISH text, read while locating row 1302, carries a one-line
summary of row 1291 ("argues from Lemma CR that reflection-positive tiling cannot make the count decay",
unchecked). Check 1292's text quotes row 748's side-3 numbers (the defect 216 (beta/4)^9 against even sums
O(beta^12)). Nothing else from the closed files was seen.

**Literature record.** The lane has one (row 749, `prior/gap-lit-casimir.md`, searched 2026-11-11, two
forward-citation rounds): no general rigorous bound from a gap or a small thermal weight to the periodic
vacuum-energy defect was found; the exact thermal identity E_0(L) - F_L(beta) = beta^-1 log(g_L + S_L(beta)) moves
the problem to a finite-temperature size defect; the closest positive instance is Pawellek's mirror identity for
a free massive scalar (arXiv:1303.4708). Row 729 (`prior/gap-small-volume-lit.md`) holds the small-volume SU(2)
statements (van Baal's review hep-ph/0008206, sections 2-4 read in full by that row; Lüscher 1983 and
Lüscher-Münster 1984 not read). Row 1216 found no new unconditional result to 2026-11-19. This run reuses these
records and adds a targeted search only in step 7, for new route questions.

## Step 1. The wall, stated twice

Written about 2026-11-20T16:01Z (estimated afterwards).

### Plain version (about 150 words; no blind check ran, since this run has no subagents)

We want to prove that SU(2) Yang-Mills theory has a mass gap: every state above the vacuum costs at least a
fixed positive energy. In this lane that whole question has shrunk to one inequality on one large box: a
temperature-weighted count of the low neutral states must be at most 1/2. One way to reach a large box is to
bound it by many copies of a small box ("tiling"). Each copy then charges a price: how far the small box's
lowest energy per volume falls short of the value in infinite space. The owner's blocks, whose parts turn
about different directions, raise the small box's lowest energy, so they shrink that shortfall, and they do
this for SU(2) and not for electromagnetism. This is proved in a simplified model. But where it is proved,
the shortfall stays near 5, and the tiling needs it below about one part in 10^8. Passing the wall means a
combination of blocks whose total price fits, or a proof that none can.

### Precise version

**Target, (N-phys)** (`gap-mini-neutral-fable.md` L44-55, row 1161 L146-148 and L215; quoted, not rewritten):
"there is one admissible physical side L and an index j_0 such that for every j >= j_0, with n_j = L/a_j and
4 | n_j, there is an integer u_j with 3 <= u_j <= n_j/K and s_j(u_j; n_j) <= 1/2", with
s(u; n) = X_{0,0}(u) - 1 the periodic neutral excited sum of Wilson SU(2) on the cube n^3 and K = 512 in the
explicit version (n_j >= 2^70). Consumer: row 1225 Theorem E-N (check 1232, HOLDS AFTER CORRECTION): (N-phys)
gives, on the account's matched tr F^2 sector, a one-dimensional vacuum and a gap of at least
(2/L) log(2^18/5041) > 7.9/L.

**The wall** (row 1285 L352-411, with check 1292 L30-46 and L85-114). For the periodic Wilson torus,
D_l := l (l^3 e_inf - E_0(l)) >= 0 and, at u = N l/K,

    log X_{0,0}(u; N l) <= N^3 log X_full(u; l) + (N^4 D_l - D_{N l})/K            (RT-iii, exact form of check 1292)

So a tiling of the physical cube by N^3 periodic blocks of side l gives (N-phys) when the right side is at most
log(3/2). This is sufficient, not necessary (check 1292 L42). When the first term is negligible the budget for
D_l is about K log(3/2)/N^4, about 2 x 10^(-8) at N near 330, l m = 30 (row 1285 L370-373; GUIDE numbers). The
directional mechanism enters only through D_l: Lemma E0 (PROVED in the reduced model, check 1292 HOLDS):
n e_A (4/27)^(1/3) s_n^(2/3) <= E_0(K_n) <= (9n/8)(n-1)^(1/3), so 2.946 <= E_0(K_3) <= 4.252 in units g^(2/3)/l
(exact endpoints 2^(1/3)|a_1| and 27 2^(1/3)/8). Tree-level reading (GUIDE; HOLDS AFTER CORRECTION in check 1292:
5.025 is the continuum coefficient of six free modes, and Lemma E0 supplies no remainder or bulk matching):
D_l(SU(2)) = 5.025 - eps_0 g(l)^(2/3) + ..., D_l(U(1)^3) = 5.025, eps_0 in [2.95, 4.25].

**Corrections already on file (check 1292).** (1) The 10^(-8) threshold and "exponential decay is the only way"
do not follow (L42). (2) The blanket claim that thermal sums cannot control D_l FAILS: for even l >= 6,
D_l <= 14 log X_full(l/2; l), from row 697's Lemmas K, X, E (L89-95). (3) RT's "every block's gap is carried for
free" holds only at fixed (l, beta) as N grows; on the trajectory l, the block gap, X_full(3; l) and beta all move
with the cutoff (L40).

**Quantifiers and domain.** One physical side L; every lattice spacing a_j beyond j_0 (cutoff-uniform); beta_j on
the account's trajectory (Balaban's ultraviolet trajectory; Sussman and Alpoge's premises). SU(2), Wilson action,
periodic cubes, 4 | n.

**Allowed premises.** The account's constructive premises; lane statements checked by another model; written
proofs only (GOAL.md, "No computer-assisted steps").

**Forbidden weakenings and what does not count.** A gap uniform in the number of blocks at a fixed block (the
Sussman-Alpoge split, row 1285 L425-428); a fixed-(l, beta) limit N -> infinity; a small-volume or reduced-model
statement alone; a tree-level or GUIDE number; a run.

**Boundary and degenerate cases the answer must respect.** N = 1: the defect term vanishes and the tiling is the
target itself. U(1)^3 and SU(2) times a free photon: (N-phys) is false at every size (row 1285 item 4, PROVED;
check 1292 HOLDS AFTER CORRECTION with a normalized vacuum), so every valid tiling bound must fail there. One
direction (n = 1): no neutral gap in the reduced model (Lemma S_n, check 1279).

**What fails now.** No bound on D_l, nor on the block thermal sums, at any block size on the trajectory, of the
size the budget asks.

**What would count.** Progress: a proved bound on D_l (or on the whole right side of RT-iii) at one block on the
trajectory; or a different combination of blocks whose price is provably smaller. Closure: (N-phys). Demotion:
a proof that the tiling's requirement is equivalent to a known open statement of the lane (an exact price), or
that the "size a tiling needs" is an artifact of a supplied choice (a misframing).

## Step 2. Inventory: what is known to be true

Written about 2026-11-20T16:06Z (estimated afterwards). Sources: the open-now list of step 0 only. "checked (row R)" names the check
record; "read" says how this run read it. Abbreviations: GCR = `gap-crux-restate.md` (row 697, checked by rows
698 and 699); T85 = `gap-owner-tiling-opus.md` (row 1285); C92 = `gap-owner-tiling2-check-astra.md` (check 1292).

| # | Item | Mark | Source | Standing; reading state |
|---|---|---|---|---|
| I1 | Wilson SU(2) on a periodic torus of sides n_mu >= 3; A = sum_p (1 - tr U_p/2); Z(n) = int exp(-beta A) dHaar. | DEF | GCR L31 | |
| I2 | (TM): for each direction and each choice of the other sides, a positive trace-class transfer T with Z = Tr T^(n_mu); simple top eigenvalue, strictly positive eigenvector; every box with sides >= 3. | THM | GCR L33 | checked (rows 671, 698, 699); statement read |
| I3 | (TM-c): centre flips C_nu commute with T; Tr(T^(n_mu) C_nu) = Z^(mu nu), the torus with one flipped plaquette stack. | THM | GCR L35 | checked (698, 699); statement read |
| I4 | Lemma A: (Tr S^k)^(1/k) non-increasing, tends to lambda_0; Tr S^(jk) <= (Tr S^k)^j; lambda_0^k >= Tr S^(2k)/Tr S^k. | THM | GCR L37 | checked; read |
| I5 | X_{m,q}(u) = Tr_q (F_m/lambda_0)^u (twist m, electric character q, G = (Z/2)^3); s(u; n) = X_{0,0}(u) - 1; X_full = sum_q X_{0,q}. | DEF | `gap-mini-neutral-fable.md` L35-42; T85 L354 | |
| I6 | (N-phys), as quoted in step 1, K = 512 explicit with n_j >= 2^70. | DEF | `gap-mini-neutral-fable.md` L44-50 | |
| I7 | Row 1161 consumer: (N-phys) gives a cutoff-uniform Pfaffian seed below 2^(-18) at time n/2 and one of two flux alternatives (9). | THM | `gap-solve9-astra62.md` L146-148 | checked (row 1162, Opus 5.5 max); statement read |
| I8 | Row 1161 necessity: (W) implies (N-phys) on all large dyadic sizes, through the propagated shape-two seed at time b/2 and Proposition B3 (a multiplier (2n/b)^3 on the log trace). | THM | `gap-solve9-astra62.md` L150 | PROVED by row 1161's author; whether row 1162 covered L150 was not read here: argued |
| I9 | Theorem E-N: (N-phys) gives, on the matched tr F^2 sector, a one-dimensional vacuum and a gap >= (2/L) log(2^18/5041) > 7.9/L. | THM | rows 1225, 1232 | checked after correction (1232); RESULT read |
| I10 | Remark RT (i)-(iii): Z(u,(Nl)^3) <= Z(u,l^3)^(N^3); E_0(Nl) >= N^3 E_0(l); e(n) := E_0(n)/n^3 increases along multiples; e_inf := sup e finite; D_l := l(l^3 e_inf - E_0(l)) >= 0; log X_{0,0}(u;Nl) <= N^3 log X_full(u;l) + u delta_{l,N}, l delta_{l,N} = N^3 D_l - D_{Nl}/N. | THM | T85 L352-364; C92 L32-38 | checked (1292 HOLDS); read |
| I11 | 0 <= e(n) <= 12 beta. | THM | C92 L32 | checked in 1292's derivation; read |
| I12 | RT consequence: at fixed (l, beta) and u = Nl/K, N^3 log X_full(u; l) -> 0 as N grows (Perron-Frobenius gap of the full block). Not a transfer of a gap on the trajectory. | THM | T85 L366-369; C92 L40 | checked (1292, HOLDS as a fixed-block estimate; FAILS as gap transfer) |
| I13 | Budget: (N-phys) at Nl follows from N^3 log X_full(Nl/K; l) + (N^4/K) D_l <= log(3/2); the 2 x 10^(-8) figure assumes the first term negligible; the sharper form keeps -D_{Nl}/K; neither is necessary. | THM | C92 L42 | checked-as-corrected (1292); read |
| I14 | Lemma E0 (reduced model K_n = -Delta/2 + (1/2) sum_{i<j} abs(y_i x y_j)^2 on L^2(R^(3n))): n e_A (4/27)^(1/3) s_n^(2/3) <= E_0(K_n) <= (9n/8)(n-1)^(1/3); n = 3: 3 < E_0(K_3) < 4.25 by hand. | THM | T85 L380-394; C92 L48-56 | checked (1292 HOLDS); read |
| I15 | Lemma S_n: K_n >= s_n W, W = sum_i abs(y_i), s_n = ((n-1)/2)^(1/2); n >= 2 non-commuting directions give a discrete singlet spectrum and gap kappa_n g^(2/3)/L in the reduced model; n = 1 none. | THM | row 1273, check 1279 | checked (1279 HOLD); RESULT and C92's citation read |
| I16 | Sewn reduced tilings (tree, stiff, cyclic) of N^3 blocks: singlet gap ~ kappa_r g^(2/3)/(N l) at fixed N as g -> 0; cyclic adjoint sewing has >= 3N^3 soft neutral levels; reduced tiling is one box of side L with L m = kappa_r g^(2/3). | THM | rows 1286, 1287 | checked (1287 HOLDS); RESULT read |
| I17 | Lemma K: e(b) = lim_a (1/a) log W(a,b); e(jb) <= j e(b); kappa := e - l_inf b >= 0, convex, non-increasing in b (here e = log lambda, the opposite sign to I10's E_0). | THM | GCR L178-180 | checked; read |
| I18 | Lemma X (exact crossing identity): a kappa(b) + g(a,b) = b kappa(a) + g(b,a), g = log(1 + S); for a < b, (b - a) kappa(b) <= g(a,b). | THM | GCR L182-186 | checked; read |
| I19 | Lemmas E, E': 1 + S(a; h) <= (1 + S(a; b))^(h/(b-a)) for h >= b > a >= 3. | THM | GCR L188-190, L213-215 | checked (E: 698, 699; E': written by row 699, re-derived by the lead) |
| I20 | Theorem S and Corollary S3': s := S(N; (2N)^3) < 1/5041 gives m(L^3) >= log(1/(5041 s))/N for every L >= 2N, and S(D/2; L^3) <= q^(2^k)/71. | THM | GCR L192-221 | checked; read |
| I21 | Theorem D, Proposition R: 1 + S(n; (2n)^3) <= exp(Phi(n)); a seed Delta(n^4) <= eps reaches cubes 2^k n with 8^k eps <= 1, and no further by this argument. | THM | GCR L90-123 | checked; read |
| I22 | Positive comparison (correction in check 1292): for even l >= 6, D_l <= 14 log X_full(l/2; l). | THM | C92 L89-95 | argued by gpt-6.2-astra inside a check record, from I17-I19; no second reader; re-derived in step 3 |
| I23 | ES-1 at side 3, strong coupling: the doubling defect is 216 (beta/4)^9 + O(beta^10), the even thermal sums O(beta^12); so no coupling-uniform linear bound of the defect by the even sums. | THM | rows 751, 753 via T85 L374-378, C92 L44 | checked (753); read only as quoted (attack files closed) |
| I24 | SU(2) times a free photon keeps every block-holonomy statistic and violates (N-phys) at every size. | THM | T85 RESULT item (4); C92 L77 | checked after correction (normalized finite-box vacuum) |
| I25 | Continuum free-field Casimir: a massless periodic scalar on a cube of side l has bulk-subtracted ground energy -(2 pi^2 l)^(-1) sum_{m != 0} abs(m)^(-4); six transverse colour modes: six times this, decimal -5.025/l. | THM (decimal: GUIDE) | T85 L396-399; C92 L111 | Poisson-summation sketch in C92; constant 16.5323 recalled; not a finite-spacing value |
| I26 | Tree-level reading D_l(SU(2)) = 5.025 - eps_0 g(l)^(2/3) + ..., D_l(U(1)^3) = 5.025, eps_0 in [2.95, 4.25]. | BELIEF (GUIDE) | T85 L400-404; C92 L111-113 | no remainder, no bulk matching (C92); the predicted crossover at 5.025/eps_0 FAILS as an inference (C92 L113) |
| I27 | For a theory with lightest neutral mass m, (N-phys) asks m L of order 10^4. | BELIEF (GUIDE) | `gap-mini-neutral-fable.md` L56-59 | |
| I28 | For a massive theory D_l is exponentially small in l m; massless theories keep D_l of order one. | BELIEF | T85 L371-373 | C92 L113: neither direction follows in general |
| I29 | Exact thermal identity: E_0(L) - F_L(beta) = beta^(-1) log(g_L + S_L(beta)); the vacuum defect differs from the free-energy defect by thermal weights. | THM | `prior/gap-lit-casimir.md` | elementary; derived in row 749's record; re-derivable in one line |
| I30 | Seam comparison: abs(D(L)) <= norm(V) for a bounded finite-range Hamiltonian cut into cells; boundary-order, not exponential; not derived for Wilson. | THM (other setting) | `prior/gap-lit-casimir.md` | argued in row 749's record |
| I31 | Pawellek (arXiv:1303.4708): for a free massive periodic lattice scalar the Casimir term is a mirror free energy at temperature 1/L. | THM (literature) | row 749 record | read in full by row 749; not by this run |
| I32 | Lüscher, CMP 104 (1986): finite-volume mass shifts of stable particles are exponentially small; perturbative to all orders; not about the vacuum energy. | THM (literature) | row 749 record | abstract only (row 749); recalled here |
| I33 | Small-volume SU(2) (Lüscher 1983; van Baal's review): the nine constant modes carry an effective Hamiltonian on the scale g^(2/3)/L; scalar mass m_0 = eps_1 g^(2/3)/L, eps_1 = 4.1167 (computed); electric-flux splitting ~ exp(-S/g(L)), S = 12.4637; field-space boundary effects from z = m_0 L > 0.9; crossover near z = 2; instantons from z near 5-6. | THM (literature; numbers GUIDE) | `prior/gap-small-volume-lit.md` | van Baal sections 2-4 read in full by row 729; Lüscher 1983, Lüscher-Münster 1984 abstracts only |
| I34 | Sussman and Alpoge (outline 2.6): a block-constrained gap uniform in the number of blocks "supplies neither ... nor a mass gap". | THM (their text) | T85 L425-428 quoting L766-779 | read only through row 1285's quote |
| I35 | Nearest false models for Theorem S's seed: U(1) at weak coupling, s >= 12 exp(-pi)(1 - o(1)) about 0.52; Z_2 at the transition s >= 1 - o(1); Z_2 at large beta s >= 7 - o(1). | THM (recalled) | GCR L227 | recalled by row 697; not re-derived |
| I36 | Adjoint-Higgs endpoint: in the infinite-hopping limit all transports lie in one U(1); the finite-box endpoint is exact and binds any directional proof. | THM | row 1004 Lemma GG; checks 1279, 1292 L103 | checked (1279, 1292); statement read |
| I37 | Strong coupling (small beta): Wilson SU(2) has a gap by the cluster expansion (Osterwalder and Seiler). | THM (literature) | recalled | not on the trajectory |
| I38 | SU(2) Yang-Mills has a mass gap, glueball near 1.5-2 GeV (lattice numerics). | BELIEF | physics | used in no proof |

**Nearest models (they become the tests of step 6).** Target false: U(1)^3 and SU(2) times a free photon (I24,
I26); adjoint Higgs at infinite hopping (I36); one-direction reduced model (I15). Target true for a known reason:
strong coupling (I37); a free massive scalar (I31).

## Step 3. Reasoning up from the inventory

Written about 2026-11-20T16:15Z (estimated afterwards; the numeric lock was taken at 16:13Z). Only items I1-I38 are used. Notation of row 697 (I17, I18): for fixed
spectator sides (c, d), W(a, b) = Z(a, b, c, d) = Tr T_b^a, e(b) = log lambda(b), l_inf := inf log W/(ab),
kappa(b) = e(b) - l_inf b >= 0 (the ground-energy deficit of the box (b, c, d) against the (c, d)-tube bulk),
g(a, b) = log X_full(a; (b, c, d)). One GUIDE run of arithmetic (under the numeric lock, outside the repository,
under one second) produced the decimals marked GUIDE; each decimal that a statement uses also has a hand bound.

### 3.1 What follows at once

**F1 (the zero-point energy cancels from every normalized trace; argued, from I5, I6, I14, I20).** For a
self-adjoint H bounded below with e^(-uH) trace class, Tr e^(-u(H - E_0(H))) is unchanged by H -> H + c. Every
quantity of the target and of the lane's engine is of this normalized kind: s(u; n), X_{m,q}(u), X_full(u; n),
the seed S(n; (2n)^3) of Theorem S, the Pfaffian seed of row 1161. They depend on the spectrum only through the
gaps lambda_i/lambda_0. In the tree-level picture of I26 the block Hamiltonian splits into zero modes and
nonzero modes, and E_0(K_n) g^(2/3)/l is the ground energy of the zero-mode part: it is a constant shift of every
level, and it cancels from all of these traces. **So Lemma E0 bounds the one number that the target and the
seed do not see.** It is visible only to quantities that compare ground energies of different boxes: D_l,
delta_{l,N}, kappa, Phi, Delta. The directional mechanism reaches the normalized traces only through the gaps
above the vacuum (Lemma S_n: kappa_n g^(2/3)/l) and the state count.

**F2 (crossing: a Casimir deficit is a thermal free energy in the crossed channel; argued, from I17, I18).**
(a) For every b >= 3: kappa(b) = lim over a -> infinity of g(b, a)/a. *Proof.* Lemma X: a kappa(b) + g(a, b) =
b kappa(a) + g(b, a). As a grows, g(a, b) = log(1 + S(a; b)) -> 0 (simple top eigenvalue, trace class), and
kappa(a) stays in [0, kappa(3)] (Lemma K). Divide by a. QED. In words: the deficit of the box (b, c, d) is the
free energy per unit length, at temperature 1/b, of the long (c, d)-tube.
(b) For the cube n^3 at time u < n (spectators (n, n); kappa now refers to the slab (u, n, n)):

    (n - u) kappa(u) + g(n, u)  <=  log X_full(u; n^3)  <=  n kappa(u) + g(n, u).

*Proof.* Lemma X gives log X_full(u; n^3) = g(u, n) = n kappa(u) - u kappa(n) + g(n, u), and
0 <= kappa(n) <= kappa(u) (Lemma K). QED. At u = n/K: **the full form of (N-phys) (log X_full <= log(3/2), which
implies (N-phys) because X_{0,0} <= X_full) is, within the factor 1 - 1/K and the long-time term g(n, n/K) >= 0, a
bound n kappa(n/K) <= log(3/2) on the Casimir deficit of one slab of thickness n/K.** So "the binding factor is
a Casimir defect" is not special to tilings: the target itself is a Casimir-defect statement in the crossed
channel. A tiling trades the slab's deficit for the deficits of N^3 cubes.

**F3 (re-derivation of I22; argued, from I4, I10, I17, I18).** For even l >= 6 and every N >= 1:
l delta_{l,N} <= 14 N^3 G_0 with G_0 := log X_full(l/2; l), hence D_l = sup_N l delta_{l,N}/N^3 <= 14 G_0.
*Proof.* Enlarge one direction at a time: (l,l,l) -> (Nl,l,l) -> (Nl,Nl,l) -> (Nl,Nl,Nl). In a step with
spectators (c, d), the ground-energy increment is d_i = N kappa(l) - kappa(Nl) <= N kappa(l) <= 2N G_{i-1}/l by
Lemma X at (a, b) = (l/2, l), where G_{i-1} is log X_full(l/2; .) of the box before the step. Lemma A in the
enlarged direction gives G_i <= N G_{i-1} + (l/2) d_i <= 2N G_{i-1}. So d_1 <= 2N G_0/l, d_2 <= 4N^2 G_0/l,
d_3 <= 8N^3 G_0/l, and delta_{l,N} = N^2 d_1 + N d_2 + d_3 <= 14 N^3 G_0/l. Finally e_inf = sup_N e(Nl), since
e(ml) >= e(m) for every m (RT (ii) with block m). QED. This agrees with check 1292 L89-95.

**F4 (the deficit inside the engine's doubling step, and its floor; argued, from I4, I17, I20).** From
W(a, 2b) <= W(a, b)^2 (Lemma A) and e = kappa + l_inf b:

    g(a, 2b) <= 2 g(a, b) + a (2 kappa(b) - kappa(2b)),   with   2 kappa(b) - kappa(2b) >= kappa(b) >= 0.

Lemma E is this line with Lemma X's bound kappa(b) <= g(a, b)/(b - a). So a smaller deficit can improve the
engine only down to the floor g(a, 2b) <= 2 g(a, b) (extensivity of the log trace), which no deficit bound can
pass. With a perfect deficit bound, Theorem S's recursion becomes s' <= ((1 + s)^8 - 1)^2 in place of
((1 + s)^64 - 1)^2. By hand: for x <= 1/100, (1 + x)^8 - 1 <= 8x e^(8x) <= 8.67x, so s <= 1/100 gives
s_k <= (75.2 s)^(2^k)/75.2. Theorem S's stated threshold is 1/5041. The exact fixed points of the two maps are
x* = 1/70.7 and x* = 1/4159 (GUIDE). **So the whole value of the deficit lever inside the engine is a constant:
the seed threshold moves from 1/5041 to at best about 1/71, a factor of about 59 to 71.** The seed itself is a
normalized trace, from which the zero-point energy cancels (F1).

### 3.2 The least a solution must contain

A proof of (N-phys) by any bound "big box <= product of blocks" (RT-iii, Lemma E, Theorem S) must fail on U(1)^3
and on SU(2) times a free photon, where (N-phys) is false at every size (I24). In those models the block gap is
of order 2 pi/l with a volume's worth of low states, and D_l stays of order one (I25; GUIDE). Block-holonomy
statistics do not separate them from SU(2) (I24). So the proof must use a property that these models lack at the
block scale: a small normalized block trace at aspect at most 1/2 (by F3 this also makes D_l small), that is, a
block gap together with a count of the low states. The ground-energy shift of Lemma E0 is not such a property
(F1). The directional gap of Lemma S_n is such a property, but it is kappa_n g^(2/3)/l, which vanishes in units of
1/l at small block size (I15).

### 3.3 The smallest object, and a toy in which the wall bites

The smallest object is one number at one block: the full seed s(l) = X_full(l/2; l) - 1. RT needs at most the
triple (s(l), D_l, X_full(Nl/K; l)), and F3 bounds D_l by s(l).

**Toy (tree level: free nonzero modes plus the reduced zero modes; GUIDE, by hand).** Six free massless modes at
temperature 1/u on a box of side l give, by the Stefan-Boltzmann law, log X_full ~ 6 (pi^2/90)(l/u)^3 =
0.658 (l/u)^3 for u << l. At u = Nl/K the first term of RT-iii is N^3 x 0.658 (K/N)^3 = 0.658 K^3, about
8.8 x 10^7, for every N << K, whatever the zero-point energy. The defect term needs D_l <= K log(3/2)/N^4:
12.97 at N = 2, 2.56 at N = 3, 0.81 at N = 4, 0.33 at N = 5, 1.8 x 10^(-8) at N = 330 (GUIDE). The tree-level
SU(2) defect 5.025 - eps_0 g^(2/3) with eps_0 <= 4.25 is at least 0.78, so it fits the defect budget only for
N <= 4. **So in the toy the wall bites at every N, but through the first term, by about eight orders of
magnitude; the defect binds only where the first term is already lost.** The toy confirms the wall and moves it.

### 3.4 Where the result could come from

Mechanisms that would make RT-iii's right side small: (i) a block gap with a state count (the massive regime;
then F3 makes D_l small too); (ii) a cancellation in D_l between zero-point and Casimir terms at intermediate l
(no structural reason; positivity does not force a crossover, C92 L113); (iii) other boundary conditions on the
blocks. For (iii): Lemma A tiles only with periodic blocks, because Z^tw <= Z^per for each block, so
Z^per(Nl) <= (Z^tw(l))^N fails already at N = 1; and an electric projection P = (1 + C)/2 can be carried
through a tiling in one direction (Tr(T^(Nl) P) <= (Tr(T^l P))^N), but the other two projections turn into
twisted transfer operators and are lost at the next direction (argued). So a three-direction tiling bounds
X_{0,0} of the big box only by X_full of the blocks, as RT-iii does. It is one problem, not several: the full
seed at one block on the trajectory.

### 3.5 Making the requirement less wrong

"D_l of order 10^(-8)" is the requirement of one choice: N near 330 with the first term assumed negligible. Over
all N the requirement splits (argued; numbers GUIDE with hand bounds):

- **N <= 4:** the defect budget is at least 0.81, which the tree-level directional zero-point energy can meet
  (GUIDE, tree level only). But the first term is then the full form of the target on a block of side at least
  L/4 with aspect at least K/4: no real reduction.
- **13 <= N <= K/2:** Nl/K <= l/2, and X_full is non-increasing in time, so the first term alone gives
  N^3 G_0 <= log(3/2), that is G_0 <= log(3/2)/13^3 < 1.85 x 10^(-4) < log(1 + 1/5041): **Theorem S's seed at
  n = l/2.** (Hand: log(3/2) < 0.4055, 13^3 = 2197, log(1 + x) >= x - x^2/2.) The engine already gives
  (N-phys) from that seed (I8, I20), so RT adds nothing in this range.
- **5 <= N <= 12:** the first term gives G_0 <= log(3/2)/N^3 <= 3.3 x 10^(-3), below the defect-free threshold
  1/100 of F4 but above Theorem S's; the scale reduction is at most 12.
- **N > K/2:** the first term is a low-temperature block trace; the defect term needs
  D_l <= K log(3/2)/N^4 < 16 log(3/2)/K^3 = 4.8 x 10^(-8). The only bound of D_l by normalized traces on file (F3)
  turns this into G_0 <= 3.5 x 10^(-9), far below Theorem S's seed. The sharper form keeps -D_{Nl}/K, a defect of
  the physical box itself, which by F2 is the target in the crossed channel.

### 3.6 The price

What RT-iii needs, at every N, is at least one of: Theorem S's seed at the block (13 <= N <= K/2), the full
target at a block of side at least L/12 (N <= 12), or a direct bound D_l <= 4.8 x 10^(-8) that the record can
supply only through a seed of 3.5 x 10^(-9) (N > K/2). The directional zero-point energy enters none of the
normalized traces (F1) and is worth at most a factor of about 71 in the engine's seed threshold (F4).

### Conclusions of step 3

- **C1** Lemma E0's quantity, the zero-mode ground energy, cancels from (N-phys), from every X_{m,q}, from
  X_full and from the seed. Argued; I5, I14.
- **C2** Exact crossing: kappa(b) = lim_a g(b, a)/a, and (n - u) kappa_slab(u) + g(n, u) <= log X_full(u; n^3)
  <= n kappa_slab(u) + g(n, u). The full form of (N-phys) is a one-slab Casimir-defect bound. Argued; I17, I18.
- **C3** l delta_{l,N} <= 14 N^3 log X_full(l/2; l) and D_l <= 14 log X_full(l/2; l), even l >= 6. Argued
  (re-derives I22); I4, I10, I17, I18.
- **C4** In the engine the deficit enters additively, with floor g(a, 2b) <= 2 g(a, b); perfect deficit control
  moves the seed threshold from 1/5041 to 1/100 by hand (about 1/71 exactly, GUIDE). Argued; I4, I17, I20.
- **C5** RT-iii by ranges of N, as in 3.5. Argued; I10, I13, I20, C3; tree-level numbers GUIDE (I26 is a BELIEF).
- **C6** At weak coupling the binding factor of RT-iii is the first term (about 0.66 K^3 for every N << K),
  not the defect. Reading (GUIDE): rests on the free-field toy, I25, I26.
- **C7** A valid tool must use a small normalized block trace at aspect at most 1/2 (a block gap with a state
  count); the ground-energy shift is not one. Argued from the tests I24 and C1, C3; sizes rest on I26 (BELIEF).
- **C8** The wall's sentence "falls short of the size a tiling needs" is priced at the seed of Theorem S at one
  block, not at D_l: making D_l smaller cannot move RT-iii past what Theorem S already does with the same block.
  Argued from C1-C5.

## Step 4. The assumptions table

Written 2026-11-20T16:16Z (date -u at the end of the step). Taken from the wall's statement (T85 L350-436), check 1292, the
(N-phys) definition and row 697, then the hidden ones. "Needed" says by what: target, method, or habit.

| ID | Assumption, in plain words | Where used | Needed or habit | If wrong or dropped | Easier? | Check |
|---|---|---|---|---|---|---|
| a1 | The gap is wanted through (N-phys): one physical box, neutral sector, threshold 1/2 | `gap-mini-neutral-fable.md` L44-50; E-N | target (lane's reduction; E-N checked) | Theorem S's full seed or (W) also suffice (I8, I20) | the full seed is a smaller box but all sectors | rows 1161, 1225, 1232 |
| a2 | Aspect K = 512 (time at most n/512) | row 1161 L215 | method (existence argument; explicit only with n >= 2^70) | a smaller K shrinks the physical box (L m of order 20 K, GUIDE) and every RT budget scales with K | yes, linearly | none; cheapest: explicit constants in row 1161's compactness step |
| a3 | The neutral sector only (q = 0) | DEF I5, I6 | target | the full trace needs electric flux suppressed too | no | row 1161 equivalences (I7, I8) |
| b1 | Wilson SU(2), periodic cubes, 4 \| n, isotropic lattice | GCR L31 | target (the account's setting) | an anisotropic lattice breaks axis exchange, so Lemma X, F2, F3 fail | no | none needed |
| b2 | Positive trace-class transfer in every direction, simple top eigenvalue | (TM), I2 | method | Lemma A, K, X all fail | no | checked (671, 698, 699) |
| b3 | The reduced zero-mode model K_n represents the block's zero modes | T85 L380; row 1273 | method (supplied model) | E0's numbers do not transfer; by C1 they are irrelevant to normalized traces anyway | no change | check 1279 holds within the model |
| b4 | Tree-level matching D_l = 5.025 - eps_0 g^(2/3) + ... | T85 L400-404 | habit (supplied reading) | the defect budget comparison changes; by C5, C6 the first term binds first | no | C92 L111-113: no remainder or bulk matching |
| b5 | Every trace is normalized by the box's own top eigenvalue | DEF I5 | target | with a bulk normalization the zero-point energy would enter, but the quantity would no longer be s | no | definition |
| b6 | The coupling runs along the account's trajectory; a block of side l has coupling g(l) | GOAL.md; I26 | target | a block's small-volume physics is fixed by g(l), not chosen | no | Balaban; the account (theirs-cited) |
| c1 | Route: tile the physical cube by N^3 periodic cubes through Lemma A (RT-iii) | T85 L352-364 | method (the owner's idea, as row 1285 formalized it) | the engine (Theorem S plus enlargement) needs less at the same block (C5) | yes | C5 (argued here) |
| c2 | Blocks are bounded by their full traces, so the neutral projection is lost | T85 L363 | method (3D Lemma A keeps at most one projection, 3.4) | a neutral-preserving tiling would drop the 8-fold flux degeneracy from the first term at small volume; the Stefan-Boltzmann part of the first term would remain (C6) | partly | 3.4, argued |
| c3 | N near 330 with the first term negligible ("fixed block, N to infinity") | T85 L366-373 | habit | the budget must be read per N (C5) | it is wrong, not hard | C92 L40-42 corrected it |
| c4 | "The defect is the binding factor" | T85 L369, L425 | habit (from c3) | at weak coupling the first term binds by about 10^8 (C6) | yes | C6 (GUIDE toy) |
| c5 | Blocks and the big box share one time u = Nl/K | T85 L362 | method (spatial Lemma A at fixed time) | a tiling in time goes the wrong way (Lemma A bounds long times by short) | no | Lemma A |
| c6 | The blocks' spectra are provable while the big box's is not | implicit in the route | method (the reason to tile) | if no block regime is provable, tiling has no input | n/a | small volume: only perturbative and reduced-model statements (I15, I33) |
| c7 | One inequality from blocks to L ("one tool") | T85 Section 5.2 | habit | multi-scale engines (Theorem S's doubling, propagation) do better (C4, C5) | yes | C5 |
| d1 | "Thermal sums cannot control the Casimir defect" | T85 L374-378, L425 | discard test | FAILS unrestricted (C92 L89); valid form only: no coupling-uniform linear bound by the even sums at side 3 | moot | C92; C3 |
| d2 | "Tilings carry free energies, not gaps" | T85 L417-430 | discard test | true of RT-iii; "every block's gap carried for free" holds only at fixed (l, beta) | n/a | C92 L40 |
| d3 | "Below the band multi-direction blocks fail every tiling theorem on file" | T85 L431-434 (rows 720, 669, 988, 1274) | discard test | not re-derived here | ? | closed files; step 5 |
| d4 | The photon product keeps every block-holonomy statistic | I24 | discard test | holds; rules out tools whose input is a holonomy statistic | n/a | checked |
| d5 | The adjoint-Higgs endpoint binds any directional proof | I36 | discard test | holds as a restriction on proofs (C92 L103) | n/a | checked |
| d6 | Sewn reduced tilings lose the gap (kappa_r g^(2/3)/L) | I16 | discard test | holds for those sewings; says nothing about RT-iii with Wilson blocks | n/a | checked (1287) |
| d7 | "A tiling needs D_l of order 10^(-8)" | T85 L370-373 | discard test (the wall itself) | corrected by C92 L42 and C5: per N, from 12.97 (N = 2) to 4.8 x 10^(-8) (N > K/2) | yes | C5 |
| d8 | "Only exponential decay of D_l in a massive phase reaches it" | T85 L408-409 | discard test | FAILS as an inference (C92 L42, L113) | n/a | C92 |
| e1 | SU(2) Yang-Mills has a mass gap | physics | belief | the target is false | n/a | none |
| e2 | D_l decays like exp(-m l) in a massive phase | T85 L371 | belief | the massive-regime estimates of C5 change | n/a | none (Lüscher-type, recalled) |
| e3 | (N-phys) asks m L of order 10^4 | `gap-mini-neutral-fable.md` L56-59 | belief (GUIDE) | the size of N changes; C5's ranges stay | n/a | none |
| e4 | The first term is about the target's own thermal sum (extensivity) | C6 | belief (free-field GUIDE) | if blocks were much "colder" than the big box, tiling would gain | ? | free fields only |
| e5 | The band (intermediate couplings) is where any seed must be proved | T85 RESULT | belief | if a seed held at small volume, the wall would move there; I33 and the toy say it does not | n/a | I33 (literature) |
| f1 | No computer-assisted proof steps (owner, GOAL.md) | GOAL.md | working rule | not used: a certified evaluation of one block's seed would be the usual constructive route | n/a | binding |
| f2 | Port the account; proof lanes only where it is open | GOAL.md | working rule | binding | n/a | binding |
| f3 | No subagents; one session; 2-hour test budget; write only the output file; no git writes | brief | working rule | binding | n/a | binding |

**Ranking (what the lane would do differently if the row were dropped).**

1. **c1 with c6** (tile from small, provable blocks): drop it and the lane's question is the seed at one block on
   the trajectory (C5, C8), which the engine already consumes. The lane would stop pricing D_l and price the
   seed. *Owner decision: yes (the owner's tiling idea).*
2. **c4 with c3** ("the defect binds", from the fixed-block limit): drop it and the binding factor at weak
   coupling is the first term by about eight orders of magnitude (C6); the zero-point energy is then a correction
   to a subleading term.
3. **b5** (normalized traces): it cannot be dropped (it is the target), and it is the reason Lemma E0's quantity
   cancels (C1). The lane would stop treating E_0(K_n) as a lever on the target.
4. **a2** (K = 512): a smaller explicit K would shrink the physical box and every budget in proportion. The lane
   would ask for explicit constants in row 1161's compactness step.
5. **c2** (full block traces): a neutral-preserving tiling would remove the electric-flux part of the first term
   at small volume, not the Stefan-Boltzmann part. The lane would not gain a route from it.

## Step 5. Comparison with the earlier work

Written 2026-11-20T16:25Z (date -u). Opened: row 1285 in full (L1-349, L437-488 added to what step 0 read);
`parts/gap.md` L8-104 and L223-322 (state of attack, route registry, test table, price); rows 748, 750, 751, 753
(RESULT lines; `gap-es1-opus.md` statements of Theorems V and LB, L14-32, L88-117, L196-233); row 708
`gap-mid-max.md` L64-67, L209-215, L335-339; row 988 `gap-unit-max.md` L174-185 (Lemma FLOOR and its use); row
1032 `gap-afield-b-max.md` L326-395; row 1291 `gap-mini-solve-ar-opus.md` L101-143 and RESULT;
`gap-means-max.md` L24, L164, L299, L322; `gap-mini-neutral-fable.md` R5 (L173-174); row 1273's file at its
zero-point and Casimir lines (L191-201, L368-373, L421-431); row 1286's file at its zero-point line (L7). **Read
only by grep, not in full:** `gap-crux-exercise-astra.md` (row 750, 1533 lines), `gap-es1-astra.md` (row 748),
`gap-owner-movingsites-opus.md` (row 1274), the crux exercises of rows 878, 998, 1003 (grep of "Casimir",
"pressure", "zero-point"), row 1273's route sections beyond the lines named, row 1286 beyond L7. Row 1301's file
`gap-owner-tiling3-astra62.md` did not exist at 16:17Z.

**Search scope for every "new" mark below:** all of `library/*.md`, `library/prior/*.md`, `parts/*.md`,
`gates/`, `checks/`, `FINISH.md`, `QUEUE_DONE.md` at f0070179d, by at least two wordings each: (C1) "cancel" with
"zero-point", "ground energy", "normaliz", "shift", and "E_0(K"; (C2) "crossed channel", "crossing identity",
"per unit length", "slab" with "Casimir"/"deficit", "Lemma X" in the files that name (N-phys); (C4) "(1+s)^8",
"^8 - 1", "1/64", "1/71", "zero deficit", "deficit-free", "perfect deficit", "8.52"; (C5) "N^4", "first term" with
"Casimir"/"defect"; (sandwich) "sigma_3" with "Casimir"/"D_l"/"c(Y)", "two-sided", "between ... pressure". The
open PR branches were not searched (no git fetch; brief forbids git writes).

| Item | In the earlier work? | Where | Note |
|---|---|---|---|
| C1 zero-point energy cancels from normalized traces | **new** (scope above) | - | check 1292 L50 says ground energy and first excitation "are distinct numbers"; row 1285 L409-411 says the Euclidean seed sees the opposite sign; neither states the cancellation |
| C2(a) kappa(b) = lim g(b, a)/a | **yes** | `gap-means-max.md` L299 (from Lemma R1 (a)); row 751 Theorem LB (iv) (even-sector form) | found again |
| C2(b) full (N-phys) as a one-slab deficit bound | partly | Lemma X (row 697); row 1291 Lemma CR (a)-(b); `gap-mini-neutral-fable.md` R5 ("crossing gives no upper bound on s without a seed") | the reading of the target as a slab deficit is not found in those words; the content is a corollary of checked lemmas |
| C3 D_l <= 14 log X_full(l/2; l) | **yes** | check 1292 L89-95 | found again; re-derived |
| C4 deficit inside the doubling step; the floor | partly | Lemma E (row 697) is the line with Lemma X inserted; row 988 Lemma FLOOR (17.04) and its use paragraph (L183-185: "the Casimir deficit of a box is bounded by its thermal sum only at a time shorter than the side. So that seed feeds no engine") | the zero-deficit map ((1+s)^8 - 1)^2, its threshold 1/100 by hand (1/71 exact), and the halved floor 8.52 are **new** (scope above) |
| C5 RT-iii by ranges of N | partly | check 1292 L42 (the budget is sufficient, not necessary; the sharper form keeps D_{Nl}); row 1291's consequence (a tiled bound at t > y is weaker than monotonicity) | the ranges N <= 4, 5-12, 13-K/2, > K/2 and the implication of Theorem S's seed for 13 <= N <= K/2 are **new** (scope above) |
| C6 at weak coupling the first term binds (Stefan-Boltzmann) | partly | row 720 count (`gap-phys-seed.md` L109: seven flux sectors and the constant-mode levels make S(L/2; L^3) diverge), cited in row 1285 2.3; Lemma FLOOR's use (2 pi against 17.04) | found again in substance; the RT-specific size 0.66 K^3 is a GUIDE reading |
| C7 the least a tool must use | **yes** | row 998 test table (`parts/gap.md` L280-303: "a rate ... the whole state space"); row 1285 5.1 product test; Lemma FLOOR | found again |
| C8 price at the seed of one block | **yes** | row 1285 2.5 and verdict item 5; row 1032 L383-389 (the seed = a count below one plus a small ground-level deficit); row 708 (CAS) "restates the seed in steps" | found again |
| The deficit is bounded below by the block's own thermal pressure | **yes** (lower half) | row 1291 Lemma CR (c): c(Y) >= y^2 sigma_3(y), PROVED by Claude Opus 5.5, checked by no one | found again; its use against the zero-point lever is below |
| D_l sandwiched between two normalized thermal quantities, l^3 sigma_3(l) <= D_l <= 14 log X_full(l/2; l), and the consequence for the zero-point lever | **new as a combination** (scope above) | halves: row 1291 (lower), check 1292 (upper) | see 5.1 |
| b5/C1: Lemma E0's lower bound is the non-variational kind the deficit needs | partly | row 1032 L389: "an upper bound on lambda_0 of a periodic box is not variational" | the remark that E0's lower half is of that kind is **new** but has no consumer (5.1) |
| Rank-1 assumption c1/c6 (tile from provable small blocks) | yes | row 1285 2.5, item 5; row 1291 consequence | found again |
| Rank-2 c3/c4 ("the defect binds") | partly | check 1292 L40-42 corrected the fixed-block limit; row 988 Lemma FLOOR use: the deficit binds for times at least the side | the split by regime (5.1) sharpens it |
| Rank-4 a2 (explicit K) | not found as a request | row 1161 L215 gives K = 512 with n >= 2^70 | a work item |

### 5.1 What the comparison changes in steps 2-4

**Correction to the inventory (I28, I26).** Row 1291 Lemma CR (c) is a THM on file that I missed in step 2,
because its file was closed. With it, D_l >= l^3 sigma_3(l), where sigma_3(t) := lim over X of g(t; X)/abs(X) is
the vacuum-subtracted thermal pressure at time t (row 1259 Lemma CD (b) gives the limit; not read here). Re-derived
here so that this file does not lean on an unchecked row (argued, given the existence of that limit along the boxes
used): write c(Y) = l^3 e_inf - E_0(l) for Y = l^3, eps(l, l) := lim_b E_0(b, l, l)/b (the energy per unit length of
the (l, l)-tube), so c(Y) = kappa(l) + l (l^2 e_inf - eps(l, l)) with both terms non-negative, and kappa(l) =
lim_a g(l; (a, l, l))/a by C2(a). Lemma A in the two transverse directions gives, for the long box (a, kl, kl) at
time l, g(l; (a, kl, kl)) <= k^2 g(l; (a, l, l)) + l [E_0(a, kl, kl) - k^2 E_0(a, l, l)]. Divide by a k^2 l^2 and let
a, then k, grow: l^2 sigma_3(l) <= kappa(l) + l (l^2 e_inf - eps(l, l)) = c(Y). QED. So D_l = l c(Y) >= l^3 sigma_3(l).

**The sandwich (argued; lower half re-derived above from row 1291's idea, upper half C3).** For even l >= 6,

    l^3 sigma_3(l)  <=  D_l  <=  14 log X_full(l/2; l).

Both outer quantities are normalized thermal quantities, from which the zero-mode ground energy cancels (C1).
**Consequence (argued).** Adding a positive term to the block's ground energy (the directional zero-point energy)
can lower D_l, but never below the thermal pressure of the bulk at the block's own temperature 1/l. That pressure
is a bulk quantity, blind to the block's zero modes. At weak coupling it is about 6 pi^2/90 = 0.658 in these units
(Stefan-Boltzmann for six gluon modes; GUIDE, recalled, with corrections of order g^2), consistent with the
tree-level value 5.025 - eps_0 g^(2/3) >= 0.78 at the edge of the expansion. So:

- every RT-iii budget below about 0.66 (that is N >= 5) is out of reach at weak coupling whatever the zero modes add;
- the deficit threshold of row 1032's worked instance (5.7 x 10^(-10)/L) is reachable only at a block whose own
  thermal pressure is that small, which is a statement about the block's spectrum, not about its ground energy;
- **"D_l at most eps" forces l^3 sigma_3(l) at most eps, and follows from log X_full(l/2; l) at most eps/14. The
  wall is the seed at one block, priced from both sides, and the zero-point energy is not a lever on either side.**

**The regime split (sharpens c3, c4; row 988's use paragraph is the source of the key remark).** At times at most
half the side, Lemma X bounds the deficit by the thermal sum, so the deficit never binds before the seed does
(C3, C4). At times at least the side, Lemma X gives nothing, and the deficit does bind (row 988: "that seed feeds
no engine"). That is the regime of row 1285's long-time tiling and of the owner's wall. There, for periodic SU(2)
blocks at small volume, RT-iii's first term is ruined first by the eight electric-flux sectors within
exp(-12.46/g(l)) of the vacuum (row 720's count), which no deficit bound touches; and the sandwich keeps D_l above
about 0.66. So in neither regime is the size of the zero-point energy the binding fact.

**Lemma E0's lower half (remark).** Row 1032 L389 notes that a deficit bound needs a non-variational upper bound
on lambda_0 (a lower bound on E_0). Lemma E0's lower bound (K_n >= t T + (1 - t) s_n W) is of that kind. It
has no consumer: by the sandwich it can only move D_l inside an interval whose lower end is set by the bulk.

**What the fresh pass added (new against the scope above):** C1 (the cancellation); the zero-deficit doubling map,
its threshold (1/100 by hand) and the halved massless floor 8.52, still above 2 pi (C4 with Lemma FLOOR); RT-iii by
ranges of N, with Theorem S's seed implied for 13 <= N <= K/2 (C5); the sandwich as a combination, and its
consequence that no positive ground-energy term can bring D_l below the bulk pressure at the block's temperature.

**What it only found again:** the crossing identity (Lemma R1; row 751 Theorem LB (iv)); the bound by the full
trace at half the side (check 1292); the reduction of every tiling question to the seed at one block (rows 1285,
1032, 708, 998); the small-volume seed count (row 720); the long-time-seed obstruction (row 988); the lower bound of
the deficit by the pressure (row 1291); the tests a tool must pass (row 998, row 1285 5.1).

## Step 6. The blockage: discard tests and set-aside methods

Written 2026-11-20T16:26Z (date -u at the end of the step). Scope: the methods set aside **on this wall** (the deficit and the
zero-point lever in tilings: rows 1273-1292 and the Casimir and ES-1 records they cite), plus the two methods of the
crux-wide list (`parts/gap.md` methods 1-36) that touch the deficit (26 and 35). The rest of that list was re-judged
by row 998 and is not re-judged here.

### 6a. Methods set aside

| # | Method (authors) | Reason given | Where (read first-hand unless noted) | Kind |
|---|---|---|---|---|
| 1 | Linear (ES-1): bound the doubling defect by even thermal sums (rows 748, 751; gpt-6-astra, Claude Opus 5.5) | side 3: delta = 216 (beta/4)^9 against even sums O(beta^12) | RESULT lines 748, 751, 753; `gap-es1-opus.md` L22 | fails a test |
| 2 | "Thermal sums cannot control the Casimir defect" (row 1285, as a blanket discard of thermal control) | rows 748-753 | T85 L374-378, L425 | other setting (corrected: check 1292 L89) |
| 3 | Long-time RT tiling of small multi-direction blocks (row 1285 5.2; Claude Opus 5.5) | D_l of order one against a budget of 10^(-8) | T85 L366-411 | needs a small number |
| 4 | Carry of a block's gap through a tiling, (C-phys) (row 1285 2.1) | m(l) = kappa g^(2/3)/l diverges as l falls | T85 L67-74 | other setting |
| 5 | Tiling whose input is a junction statistic (row 1285 5.1) | the photon product keeps every block-holonomy statistic | T85 L324-348 | fails a test |
| 6 | Sewn reduced tilings: tree, stiff, cyclic (row 1286; gpt-6.2-astra) | gap kappa_r g^(2/3)/L, not uniform; cyclic soft modes are an artifact | RESULT 1286, 1287 | fails a test (non-uniform) |
| 7 | Block form of Simon's bound (row 1273 Lemma GA) | the spin term (row 1193) overturns the orbital zero-point energy | row 1273 L421-431 | fails a test |
| 8 | Alignment of block axes at weak coupling (row 1273) | does not follow (check 1279); axes generic (row 1285 AX) | RESULT 1279; T85 Section 3 | wrong quantity |
| 9 | A long-time (twisted) seed, time about six sides (row 988) | "the Casimir deficit of a box is bounded by its thermal sum only at a time shorter than the side. So that seed feeds no engine" | `gap-unit-max.md` L183-185 | open premise (a deficit bound) |
| 10 | Twisted cubes to remove the toron valley (row 988) | floor 17.04 against pi | `gap-unit-max.md` L180-183 | needs a small number |
| 11 | (CAS), contraction of the symmetric-torus Casimir free energy (row 708; Claude Fable 5.2) | restates the seed in steps; theta tends to 1 in the ultraviolet | `gap-mid-max.md` L64-67, L209-215 | circular (restatement) |
| 12 | Tiling bounds on the thermal pressure (row 1291; Claude Opus 5.5) | the Casimir term t c(Y)/abs(Y) >= (t/y) sigma_3(y) | `gap-mini-solve-ar-opus.md` L131-137 | fails a test (weaker than monotonicity) |
| 13 | Tree-level crossover prediction (row 1285) | positivity gives no breakdown scale | C92 L113 | unverified |
| 14 | Physical gap transfer from RT alone (row 1285 consequence) | a fixed-block limit; photon frequencies fall with size | C92 L40 | other setting |
| 15 | Value of Lemma S's gap as a tiling input (rows 669, 988, 1274) | the photon has side times gap 2 pi at every size | T85 L117-121 | fails a test |
| 16 | Method 26: a seed below the massless floor (row 988) | Lemma FLOOR: side times gap above 17.04 | `parts/gap.md` L64; `gap-unit-max.md` L174 | needs a small number |
| 17 | Method 35: expansions of the twist deficit or the doubling defect with positive weights per support (rows 1127, 1131, 1133) | absolute sums grow; a proof must cancel between supports | `parts/gap.md` L67 (digest) | fails a test (digest only) |
| 18 | Deficit-only seed criteria (implicit in the owner's lever) | the constant log 2 is a critical element with zero deficits and no seed | row 1032 L387-388 (Proposition CONST of row 1028) | fails a test |

### 6b. First principles on the blockage

A tool for this wall must bound, at one block l on the trajectory, the right side of RT-iii (or of any tiling
that bounds a big box by blocks). By the sandwich (5.1), a bound D_l <= eps forces the bulk thermal pressure at
the block's temperature to satisfy l^3 sigma_3(l) <= eps, and by C3 it follows from a full seed of size eps/14. By
row 1032's critical element (6a row 18) a small deficit alone does not give the seed: the count must be small too.
So the least a tool must use is the spectrum above the vacuum at scale l: a gap with a count of the low states,
at the block or in the bulk at temperature 1/l. **The blockage in one sentence: a deficit bound at one block is
pinned between two thermal quantities that see only the spectrum above the vacuum, so lowering the block's
ground energy, which is all that the directional zero-point energy does, cannot reach the budget unless the
spectrum above it already does.**

### 6c. The discard tests in their valid form

| Test (model M') | Class K | The exact T that fails in M' | How the failure is known | What a tool must use to pass | Binds from |
|---|---|---|---|---|---|
| Free photon, U(1)^3 | reflection-positive torus models with (TM) | (N-phys) at every size; RT-iii's right side >= its defect term with D_l(photon) >= l^3 sigma_3 = 2 pi^2/90 per photon | (N-phys) failure: THM (T85 5.1, C92); the deficit floor: reading only, since the sandwich needs (TM) and the photon needs the normalized finite-box regularization of C92 L77 | a small bulk pressure at the block's temperature, which the photon lacks at every l | every size |
| SU(2) times a free photon | same | the same | THM (T85 item 4, C92 L77) | the whole state space | every size |
| Side-3 Wilson SU(2) and Z_2 at small beta, large beta (rows 748, 751) | the lane's class | a coupling-uniform linear bound of the doubling defect by **even** sums | THM, checked (753) | the full trace at a shorter time (C3), or a nonlinear modulus (C92 L44) | at side 3, as beta tends to 0 (SU(2)) or infinity (Z_2): **off the trajectory**, which is weak coupling at growing side |
| The constant log 2 (two phases; 2D Ising ordered as a GUIDE) | limit objects of the class (row 1028, 1032) | the seed, with zero deficits | THM (Proposition CONST, row 1028; read through row 1032 L387) | a small count, not only a small deficit | the class of limit objects |
| Adjoint Higgs at infinite hopping | lattice gauge-Higgs models | the gap (a U(1) photon remains) | THM (row 1004 Lemma GG; checks 1279, 1292) | pure-gauge dynamics; a directional proof must fail there | the endpoint (finite box exact) |
| Massive free scalar | free fields | none: D_l and the seed are exponentially small | THM (Pawellek, read by row 749) | passes; no constraint | - |
| Lemma FLOOR (not a model) | any trace-class T with simple top | s < 1/5041 forces side times gap > 17.04; with zero deficit, s < 1/71 forces side times gap > 8.52 | THM (row 988, one line); the zero-deficit form argued (C4) | a block gap above 8.52/side at the seed block, against 2 pi for free modes and kappa g^(2/3) for the zero modes | every block |

Points from the valid form.

1. **The ES-1 test binds only the even-sum linear form, and only off the trajectory.** It does not refute a
   deficit bound by the full trace at half the side (C3), which is the form the engine uses. Row 1285's use of it
   against "thermal sums" (6a row 2) was outside its class of T: corrected by check 1292, confirmed here.
2. **The photon and the product bind through the sandwich's lower half.** A tool whose hypothesis is "D_l small"
   must use a property that gives a small bulk pressure at temperature 1/l; the photon has pressure
   2 pi^2/(90 l^3) per photon at every l.
3. **The log 2 element binds deficit-only hypotheses.** Even a perfect directional lowering of D_l would not by
   itself give a seed: the count half remains. This is the valid form of the owner's sentence "helps, but not
   enough": the directional zero-point energy acts on one of two necessary halves, and on that half it is bounded
   below by the bulk.
4. **Are the tests enough?** For deficit tools, yes in this sense: the sandwich turns every deficit statement into
   seed-type statements, and the seed's tests are row 998's table.

### 6d. The verdicts re-judged

| # | The verdict assumes | Valid in the corrected form? | What comes back, and where |
|---|---|---|---|
| 1 | linear, even sums, side 3, uniform in the coupling | valid only in that range | the full-trace, half-side form (C3); nonlinear moduli (C92 L44); off the path of the target |
| 2 | that the ES-1 failure covers all thermal sums | wrong (check 1292), confirmed | C3 |
| 3 | a budget of 10^(-8) | too strong as a requirement; valid as the large-N budget | per-N budgets (C5): 12.97 at N = 2 to 4.8 x 10^(-8) beyond K/2; nothing comes back on the path, because for N >= 5 the sandwich keeps D_l above about 0.66 at weak coupling (GUIDE size) and for 13 <= N <= K/2 the first term already implies Theorem S's seed |
| 4 | carry at every N | valid | - |
| 5 | inputs that read only SU(2) holonomies | valid (product test, PROVED) | - |
| 6 | the reduced sewings | valid as reported (check 1287); not re-derived | - |
| 7 | the transverse zero-point energy in a block | valid as reported (row 1193); not re-derived | - |
| 8 | deterministic alignment | valid (check 1279; row 1285 AX) | - |
| 9 | Lemma X as the only deficit bound | valid as stated: no deficit bound at times above the side is on file | a direct deficit bound would bring long-time seeds back (C4 shows what it buys: any aspect becomes usable); the sandwich says such a bound must see the bulk pressure at temperature 1/l, so it is a seed-type input; on the path, as an open premise |
| 10 | the floor at 17.04 | valid; with a perfect deficit bound the floor is 8.52, still above pi and 2 pi | nothing comes back for small twisted or periodic cubes |
| 11 | (CAS) as a mechanism | valid as reported (row 708); not re-derived | - |
| 12 | tiling bounds with c(Y) not small | valid (the lower half of the sandwich is its inequality) | - |
| 13, 14 | positivity alone; fixed-block limit | valid (check 1292) | - |
| 15 | the gap value at z <= 2 pi | valid | - |
| 16 | threshold 1/5041 | valid; moot for this wall (the zero-deficit form 8.52 is also out of reach of free modes) | - |
| 17 | positive weights per support | valid as reported (digest only); not re-derived | - |
| 18 | a criterion that reads the deficit only | valid (row 1028's critical element) | - |

**Where the corrected verdicts matter.** Rows 3 and 9 are on the path of the target, and both now point to the
same open premise: a bound on a block's spectrum above the vacuum at one scale (the seed), not a bound on its
ground energy. No set-aside tool comes back on the path. Row 1 is corrected off the path.

## Step 7. Routes: generate, try to kill, rank

Written 2026-11-20T16:29Z (date -u at the end of the step). Governance: `docs/ai_methodology/skills/physics-loop/references/proof-search-governance.md`
read at origin/main 8b11ae2bb before this step. Target contract: step 1's precise version. `--subagents 0`: six
context-isolated passes by this session, each started from step 1's precise version and step 4's table only, then
one kill pass per route. **These passes are not independent of each other or of steps 3-6** (same session).

### 7.1 Passes and routes (concrete returns)

- **Pass A (in-lane: lower the deficit directly).** R1: a non-variational lower bound on the block's ground
  energy E_0(l) (Lemma E0's lower half, K_n >= t T + (1 - t) s_n W, plus the nonzero modes), giving D_l <= eps at one
  block. Return: the obligation "D_l <= eps at one block on the trajectory", with the sandwich as its dependency.
- **Pass B (use the deficit where it binds).** R2: seeds at time longer than the side (perturbatively small for
  twisted cubes, row 988), fed to Lemma E with an explicit deficit bound (C4: with the deficit controlled, every
  aspect a/b works). Return: the obligation "a deficit bound in a twisted fibre at aspect above 1", and its first
  test (8.2).
- **Pass C (outside lens: mirror or crossing duality, as in Pawellek's mirror free energy and thermodynamic Bethe
  ansatz).** R3: rewrite the full target as a slab deficit (C2 (b)) and attack the slab through the mirror theory at
  temperature n/K. Return: the identity C2 (b); the slab deficit at thickness n/K is the target itself.
- **Pass D (misframing).** R4: the wall is misframed. Its quantity D_l is pinned between two normalized thermal
  quantities (sandwich, 5.1); the zero-mode ground energy cancels from both (C1); and a small deficit alone does
  not give a seed (row 1028's log 2 element). The question that replaces it: does the directional structure lower
  the count above the vacuum (gap times side, level density) at one block in the band? Return: the sandwich with
  its proof, and a falsification test (8.1).
- **Pass E (explicit constants).** R5: make K explicit and small in row 1161's finite-aspect step (a2). Return: the
  exact missing statement "the compactness step of row 1161 L146 with explicit K and n_0".
- **Pass F (the directional extreme).** R6: the owner's blocks with perpendicular half-turns are 't Hooft's
  m = (1,1,1) twisted box (row 1273 Lemma CC, check 1279). Twisted boxes have no zero modes. If their tree-level
  vacuum energy lies above the periodic bulk, the directional idea at its extreme over-corrects the deficit.
  Return: a sign test (8.2) and the tiling obligation it would need.

### 7.2 Outside view (targeted search for the new route questions, 2026-11-20)

| Source | What it shows | Maps to the repo? | What does not map | Read |
|---|---|---|---|---|
| C. P. Bachas, "Comment on the sign of the Casimir force", arXiv:quant-ph/0611082 (after O. Kenneth and I. Klich) | reflection positivity makes the force between mirror-image probes attractive; the energy is concave in the separation | the sign D_l >= 0 is of this kind | no size, no gap | search abstract only |
| A. Gonzalez-Arroyo and coauthors (twisted SU(2), small volume); P. van Baal, Nucl. Phys. B 289 (1987) 628 (chromomagnetic energy with twist) | twisted conditions remove the gauge zero modes and keep the exponential approach to infinite volume; the vacuum energy as a function of flux and volume at one and two loops | R6's sign question | lattice and nonperturbative content | search descriptions only |
| E. Poppitz and F. D. Wandler, arXiv:2211.10347 | SU(2) on a small twisted torus (the "femtouniverse") | R6 | - | search listing only |
| Twisted SU(N) principal chiral model, arXiv:1511.08491 | a twist can make the one-loop vacuum (Casimir) energy vanish exactly | R6: twists move the Casimir energy | 2D, a different model | search listing only |
| Row 749's record (Pawellek; Lüscher; Borgs and Kotecký; Hastings and Koma) | no general bound from a gap or a thermal weight to the vacuum defect | R1, R3 | - | row 749's reading |

No source found states the crossed-channel inequality "Casimir deficit >= thermal pressure at the crossed
temperature" in this form; the lane has it (row 1291). Search scope: two web queries; not a completed survey.

### 7.3 Lenses

Used: operator inequalities and convexity (the sandwich; Lemma E0); spectral counting (Lemma FLOOR); modular
or crossing duality (C2). Considered and empty for this wall: finite groups (the centre enters only through the flux
sectors, already counted by row 720); K-theory and index theory (no index in a ground-energy defect); large
deviations (the pressure is the relevant rate function, already used); logic and independence (none).

### 7.4 Kill pass, one per route

| Route | Assumes the target? | Contradicts a checked result? | Already tried? | Fails a valid test? | Rule or new premise? | Terminal obligation | Verdict |
|---|---|---|---|---|---|---|---|
| R1 | no | no | partly (row 1032: "an upper bound on lambda_0 of a periodic box is not variational") | yes: by the sandwich, D_l <= eps forces l^3 sigma_3(l) <= eps; at weak coupling the pressure is Stefan-Boltzmann-sized (about 0.66, GUIDE) | no | a bulk-pressure bound at temperature 1/l of size eps: seed-type, target-equivalent at the needed eps | **dead** on the weak-coupling range; blocked-equivalent elsewhere |
| R2 | no | no | partly (row 988's remark; Theorem S-w of the flux exercise for twisted fibres) | first step: Lemma A tiles a twisted fibre only in the two directions outside the twist plane (3.4), so a cube cannot be grown | no | a deficit bound in a twisted fibre at aspect above 1, plus a growth step across the twist plane | **wounded** at the first step; 8.2 runs its sign test |
| R3 | yes, after the identity: the slab deficit at n/K is the full target | no | yes (Lemma R1, row 751 LB (iv), row 1161 R5) | - | no | the target | **dead** (restatement) |
| R4 | no | no | its pieces are on file (rows 1032, 1028, 1291, check 1292); the combination and C1 are not | the sandwich is argued, not checked; 8.1 tries to refute it on free fields | no | none of its own: it re-prices the wall; the replacement question is the lane's crux | **survives** as a misframing result; as a route to the target, blocked-equivalent |
| R5 | no | no | no request on file | no | no | an explicit K in row 1161's compactness step | **survives**, not attempted (cost; it changes sizes, not the wall) |
| R6 | no | no | partly (row 988: twisted cubes; Lemma FLOOR use) | the same tiling obstruction as R2 | no | as R2 | **wounded**; its sign test is cheap (8.2) |

### 7.5 Ranking

| Rank | Route | Family (object; mechanism; terminal obligation) | Assumption challenged | What you would have to believe | Strength vs target | Kill verdict | Cost | First artifact | What it changes | Stop or reopen |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | R4 | (D_l; sandwich, cancellation, log 2 element; none) | c3, c4, b5 | that the sandwich holds (argued) | re-prices the wall | survives | low | 8.1 run and the written lemma | the owner's lever is moved from the ground energy to the count | stop if 8.1 refutes a half |
| 2 | R6 / R2 | (twisted fibre; long-time seed with deficit bound; a three-direction growth step) | c2, c5 | that a twisted tiling or growth step exists across the twist plane | unknown | wounded | low for the sign, high beyond | 8.2 lattice sums | if the sign is helpful, a precise statement of what twisted blocks would need | reopen on a valid inequality that tiles across a twist plane |
| 3 | R5 | (row 1161's K; compactness made explicit; explicit K) | a2 | that the compactness step has a constructive version | weaker (sizes only) | survives | high | none here | all budgets scale with K | queue as a work item |
| - | R1 | (E_0(l); operator lower bound; D_l <= eps) | b4 | that the bulk pressure at 1/l is small at weak coupling | target-equivalent | dead | - | - | - | reopen on a failure of the sandwich |
| - | R3 | (slab; crossing; slab deficit) | - | - | target-equivalent | dead | - | - | - | reopen on a mirror theory with a provable gap |

## Step 8. Real attempts

Started 2026-11-20T16:31Z (date -u). Budget: about 2 hours. Registry check before the attempts: `library/open-registry.md` and
the FINISH rows have no owner or row for the sandwich, for the twisted-box Casimir sign, or for the zero-point lever
(greps "sandwich", "sigma_3", "deficit" with "pressure", "twisted" with "Casimir", "zero-point"; the FINISH hits for
these words, rows 708, 720, 745, 895, 1003, do not state either statement).

### 8.1 Attempt on R4: try to refute the sandwich on free lattice fields (GUIDE run; pre-registered)

**Statement under test (argued in 5.1 and C3).** For even l >= 6: l^d sigma_d(l) <= D_l <= c_d log X_full(l/2; l),
with c_d = 2(2^d - 1) (c_3 = 14), and in d = 1 the lower half is an equality (crossing, C2 (a)).

**Model.** The free massive scalar on the isotropic hypercubic lattice in d + 1 dimensions, periodic, unit
spacing: a member of the class (positive trace-class transfer in every direction, axis exchange). Single-particle
transfer energy eps(k) = 2 arcsinh(omega(k)/2), omega^2 = m^2 + sum_i 4 sin^2(k_i/2). Then
E_0(l) - l^d e_inf = (1/2)[sum over k in the box of eps(k) - l^d integral eps], D_l = l (l^d e_inf - E_0(l)),
sigma_d(t) = - integral log(1 - e^(-t eps)), log X_full(t; l) = - sum over the box of log(1 - e^(-t eps)). The
integrals are Riemann sums on a grid of M points per axis, whose error is of the order exp(-m M) for m > 0.

**Points.** d in {1, 2, 3}; m in {0.1, 0.3, 1.0}; l in {6, 8, 12, 16}; M = 600 (d = 3, by slices), 4000 (d = 2),
200000 (d = 1). *Amended at 16:33Z (date -u), before any run:* m = 1.0 only at l = 6, 8, because at l = 12, 16 the
cancellation inside D_l (a difference of two numbers near 10^3) exceeds the 1e-9 tolerance in double precision.

**Pre-registered reading (written before the run, not changed after).** PASS-lower: l^d sigma_d(l) <= D_l (1 + 1e-9)
at every point, and in d = 1 the relative difference is below 1e-8. PASS-upper: D_l <= c_d log X_full(l/2; l) at
every point. Any violation beyond these tolerances is a FAIL of the argued sandwich as stated, and R4 stops there.
A PASS refutes nothing and proves nothing; it is a guide on one model family.

### 8.2 Attempt on R6: the sign of the tree-level deficit of 't Hooft-twisted blocks (GUIDE run; pre-registered)

**Question.** The owner's blocks with perpendicular half-turns are the m = (1,1,1) twisted box (row 1273 Lemma CC).
At tree level each adjoint colour component a of the free SU(2) field is periodic in direction a and antiperiodic in
the two other directions, with two polarizations, and there are no zero modes. Is the twisted box's vacuum energy
above the periodic bulk (a deficit D^tw = -l [E_0^tw - l^3 e_inf] below zero, an overshoot of the helpful sign)?

**Computation.** For the free massless lattice scalar on l^3 with antiperiodic conditions in the directions of a
set A, C(A; l) := l [E_0^A(l) - l^3 e_inf] = (l/2)[sum over the shifted momenta of eps - l^3 integral eps], for
A = {}, {1}, {1,2}, {1,2,3}, at l = 8, 16, 24, 32. Tree-level SU(2): periodic box 6 C({}; l) (plus the zero-mode
energy of Lemma E0, not included), m = (1,1,1) twisted box 6 C({1,2}; l). Continuum reference: 6 C({}) tends to
-5.025 (row 1285's recalled constant).

**Pre-registered reading.** Report C(A; l) for each A and l. HELPFUL-OVERSHOOT if 6 C({1,2}; l) > 0 at l = 16, 24 and
32 (the twisted vacuum lies above the periodic bulk at tree level); HELPFUL-PARTIAL if -5.025 < 6 C({1,2}; l) <= 0;
UNHELPFUL if 6 C({1,2}; l) <= 6 C({}; l). Self-test: 6 C({}; 32) within 2 percent of -5.025 (the lattice
correction is of order 1/l^2). Whatever the sign, R6 also needs a tiling inequality with twisted blocks; that part is
argued by hand after the run.

### 8.1 Result (recorded at 16:35Z by date -u; run 16:34Z under the numeric lock, 16 s, peak RSS 51 MB)

Script and output kept in this session's scratch folder, outside the repository (`sandwich.py`, sha256 prefix
beed20cc4732a04f; `sandwich.out`, cb73a48f8f98d54a); `python3 -E -P`, `nice`, BLAS threads 1, RSS guard 1 GB.

**PASS-lower and PASS-upper at all 30 points (GUIDE; it refutes nothing and proves nothing).** Selected rows:

| d | m | l | D_l | l^d sigma_d(l) | c_d log X_full(l/2; l) | D_l / (l^d sigma_d) |
|---|---|---|---|---|---|---|
| 1 | 0.1 | 6 | 3.13665994e-01 | 3.13665994e-01 | 2.97 | 1.000000 |
| 1 | 1.0 | 8 | 5.9126669e-04 | 5.9126669e-04 | 8.88e-02 | 1.000000 |
| 2 | 0.1 | 6 | 4.870e-01 | 1.659e-01 | 10.6 | 2.94 |
| 2 | 1.0 | 8 | 1.645e-03 | 8.125e-04 | 0.622 | 2.02 |
| 3 | 0.1 | 6 | 6.201e-01 | 1.133e-01 | 34.2 | 5.47 |
| 3 | 0.3 | 16 | 2.783e-02 | 8.370e-03 | 5.41 | 3.33 |
| 3 | 1.0 | 8 | 3.613e-03 | 1.182e-03 | 3.89 | 3.06 |

**Reading (not a proof).** (1) In d = 1 the lower half is an equality to ten digits at every point: this is the
crossing identity C2 (a) on the lattice, a self-test of the code. (2) In d = 2 and d = 3 the lower half holds with
ratio D_l/(l^d sigma_d) between 2.0 and 2.9 (d = 2) and between 3.1 and 5.5 (d = 3), approaching d at large m l.
This matches the image count of the free continuum formulas (2d nearest images in the Casimir sum against two
in the thermal sum), and tends toward about 7.6 for a massless scalar in d = 3 (16.53/(2 x 1.0823)). So **the lower
half is tight up to a factor of order d**: no positive term in a block's ground energy can buy more than that
factor. (3) The upper half is loose, by factors of 9 to 1075. The run gives no reason to doubt the argued sandwich.

### 8.2 Result (recorded at 16:35Z by date -u; run 16:35Z under the numeric lock, 7 s, peak RSS 182 MB)

Script `twisted.py` (sha256 prefix 95296d70c36897a3), output `twisted.out` (8866831075f49262), same folder and
settings.

| l | C({}) | C({1}) | C({1,2}) | C({1,2,3}) | 6 C({}) periodic | 6 C({1,2}) twisted m = (1,1,1) |
|---|---|---|---|---|---|---|
| 8 | -0.859351 | -0.042660 | 0.116503 | 0.216573 | -5.15611 | +0.69902 |
| 16 | -0.842498 | -0.036701 | 0.110917 | 0.200474 | -5.05499 | +0.66550 |
| 32 | -0.838753 | -0.035355 | 0.109673 | 0.196879 | -5.03252 | +0.65804 |
| 64 | -0.837839 | -0.035026 | 0.109370 | 0.196001 | -5.02704 | +0.65622 |
| continuum image sum (truncated at abs(n_i) <= 60) | -0.8288 | -0.0349 | +0.1093 | +0.1957 | -4.97 (truncation) | +0.6556 |

Self-tests: the sum rule C({}) + 3 C({1}) + 3 C({1,2}) + C({1,2,3}) = C({}; 2l)/2 holds to six digits at
l = 8, 16, 32; 6 C({}; 32) = -5.0325 is within 0.15 percent of -5.025. **Pre-registered reading: HELPFUL-OVERSHOOT**
(6 C({1,2}; l) > 0 at l = 16, 24, 32). GUIDE, tree level only.

**What it says.** At tree level the owner's blocks at their most directional (perpendicular half-turns, the
m = (1,1,1) twist) have no zero modes and a vacuum energy **above** the periodic bulk, by about 0.656/l. The
periodic box lies below it by 5.025/l, minus the zero-point energy eps_0 g^(2/3)/l. So the twist does not only
lower the deficit: it overshoots, to D^tw = -0.656 + O(g^2) against the periodic bulk (GUIDE).

**Why this kills R6 instead of rescuing it (argued; the hypothesis is the GUIDE overshoot).**

*Lemma FL (the floor of every product tiling; argued, elementary).* Let the big box B and blocks b_1, ..., b_k
have positive trace-class time transfers, and suppose that for all large integers u,
X_B(u) <= C^k prod_i X_(b_i)(u) exp(u delta) with C independent of u, where X are normalized traces (sector traces
allowed) that tend to the ground multiplicities as u grows, and delta = E_0(B) - sum_i E_0(b_i). Then delta >= 0.
*Proof.* Let u grow: the left side tends to a multiplicity of at least 1, the product to a finite constant, so
exp(u delta) cannot tend to 0. QED. Equivalently, without normalization: if
Z_B(u) <= C^k prod_i Z_(b_i)(u) for all large u, then E_0(B) >= sum_i E_0(b_i).

*Corollary FL1 (argued, given the overshoot).* If a twisted block has E_0^tw(l) > l^3 e_inf, then no inequality
Z^per(u; (Nl)^3) <= C^(N^3) Z^tw(u; l^3)^(N^3) with C independent of u holds for any N. *Proof.* By Lemma FL it would
give E_0^per(Nl) >= N^3 E_0^tw(l) > (Nl)^3 e_inf, against e(Nl) <= e_inf (RT (ii)). QED.

So the overshoot is exactly what excludes twisted blocks from every product upper bound on the periodic box, by any
method, not only by Lemma A. (Lemma A itself fails for them already: a twist plane containing direction i is a
slice insertion C in the direction-i transfer, and Tr(T^(Nl) C) <= (Tr(T^l C))^N is false in general; two levels
{1, r} with C = diag(1, -1) and N = 2 give (1 - r^l)^2 < 1 - r^(2l).) **Lemma FL is the general form of the owner's
wall: in any valid product tiling the deficit is at least 0, the directional zero-point energy can only push it
toward 0, and for periodic blocks the sandwich puts the floor at l^3 sigma_3(l), not at 0.** R6 is dead at the
tiling step; the flux half (twisted fibres with their own bulk, Theorem S-w) is not touched by the sign, because
there the deficit is measured against the twisted bulk and is non-negative by Lemma K.

### 8.3 Late comparison with row 1301, and the adversarial pass (written 16:39Z by date -u)

**Row 1301 appeared after step 5.** `gap-owner-tiling3-astra62.md` (gpt-6.2-astra max, Mac mini Codex runner,
author only, checked by no one; committed upstream as d655a02ea) was absent at 16:17Z and present at 16:37Z, when
another process had moved this clone from f0070179d to e1176ef2d (no git command of this run). Read at e1176ef2d:
its outline, L9-50 and L137-162, L270-308 (RESULT). Its proofs were not checked here.

| Row 1301 statement (its label) | Relation to this run |
|---|---|
| (1) eight tiles of a doubled cube, one per magnetic flux m in (Z_2)^3: E_0(2b) - sum_m E_m(b) -> 0 as beta -> infinity at fixed b (PROVED by its author) | a stronger combination than this run's R6 (identical twisted blocks, which overshoot): the mix lands **on** Lemma FL's floor. Its parity decomposition sum_p S_b(pi p) = S_(2b)(0) is the sum rule this run used as a self-test in 8.2, found independently |
| its J_m = log(Z_m(t)^2/Z_m(2t)) and K = 2 log A(t) - log A(2t): the vacuum defect cancels exactly ("No vacuum-energy estimate is needed") | the same fact as C1, used constructively: its criterion (14)-(15) is free of every ground energy, so Lemma FL does not bind it |
| (6) and the following paragraph: positive averages that keep the all-periodic term keep the rate E_0(2b) - 8 E_0(b) | agrees with 3.4 and with Lemma FL's floor |
| a model (12-plaquettes only) in which the mixed product is below the doubled periodic trace | agrees in direction with Corollary FL1 below |
| OPEN: the signed seam integral, K_beta <= sum_m W_m for all large t at a positive physical tile width, which would give the gap fraction (15) | a normalized-trace inequality at one scale: the same kind of open input as this run's price (the count, not the deficit) |

**A cross-result (argued, given a GUIDE sign).** At finite small coupling the periodic tile of row 1301's mix
carries the zero-mode energy E_0(K_3) g(b)^(2/3)/b, the doubled cube only E_0(K_3) g(2b)^(2/3)/(2b), and the seven
twisted tiles carry none. With (1) for the nonzero modes, the leading defect of the mix is
delta_mix = E_0(K_3) [g(2b)^(2/3)/(2b) - g(b)^(2/3)/b] + ..., about -E_0(K_3) g^(2/3)/(2b) < 0 (GUIDE: tree level plus
the leading zero-mode term; Lemma E0 gives E_0(K_3) > 3). Then by Lemma FL no inequality
Z^per(t; (2b)^3) <= C^8 prod_m Z^m(t; b^3) with C independent of t holds at such couplings. **So in the eight-sector
mix the directional zero-point energy has the unhelpful sign for a product bound.** It is harmless to row 1301's
route (14)-(15), from which it cancels. Here too the zero-point energy is a vacuum-energy effect: it moves deficits,
helpfully or not, and drops out of every normalized criterion.

**Adversarial pass (a second pass in this same session, not independent; brief: "find the failing step").**

1. *Sandwich, lower half.* Checked: (i) l_inf = -eps(l, l), because kappa(b)/b -> 0 (Lemma K); (ii) C2 (a) is applied
   with spectators (kl, kl) to the box (l, kl, kl); (iii) the transverse tiling is Lemma A in the two directions of
   side kl; (iv) eps(kl, kl)/(kl)^2 <= e_inf follows from Lemma A by tiling a large cube with copies of
   (b, kl, kl), so no shape-independence of the bulk is needed. **Correction made here:** sigma_3(l) must be read as
   sigma_bar_3(l) := limsup over k of lim over a of g(l; (a, kl, kl))/(a k^2 l^2). The inequality D_l >= l^3
   sigma_bar_3(l) needs no existence of a limit. Reading sigma_bar_3 as "the thermal pressure" uses the existence of
   the infinite-volume pressure along these boxes (row 1259 Lemma CD (b), not read).
2. *Lemma FL.* Checked: the left side must be normalized by its own sector's top eigenvalue, so that it tends to a
   multiplicity of at least one; stated so. Corollary FL1 rests on the GUIDE overshoot; it is marked so.
3. *C5 (13 <= N <= K/2 implies Theorem S's seed).* Checked: it uses only delta_{l,N} >= 0 (RT (ii)), monotonicity of
   X_full in time, and log(3/2)/13^3 < log(1 + 1/5041) (hand). "RT adds nothing there" also uses I8 (row 1161's
   propagation to (N-phys)), which is argued, not read as checked.
4. *C1.* Trivial and checked. Its scope: normalized traces, ratios such as Z(t)^2/Z(2t), and the seeds; not D_l,
   delta, Phi, Delta.
5. *The tree-level overshoot of 8.2 and delta_mix.* GUIDE only: free modes, no remainder estimate, as check 1292 said
   of row 1285's reading.

No failing step was found. Two scope corrections were made (items 1 and 2).

## Step 9. Report

Written 16:41Z (date -u). Marks as in the skill's output rules: argued, argued counterexample, guide, reading, open.
Nothing here is checked by another model.

### 9.1 The wall, in plain words (corrected by the exercise)

We want to prove that SU(2) Yang-Mills theory has a mass gap. In this lane that comes down to one inequality on
one large box: a temperature-weighted count of the neutral excited states must be at most 1/2. One idea is to
bound the large box by many small blocks. Such a bound charges each block a "shortfall": how far the block's
lowest energy falls below its share of the infinite-space value. The owner's blocks, whose parts turn about
different directions, raise the block's lowest energy and so shrink the shortfall. The exercise found that the
shortfall is never the real obstacle. It is squeezed between two counts of excited states: the block's own count
at half its size (from above), and the count of the infinite system at the block's temperature (from below).
Raising the lowest energy changes neither count. So the shortfall can be small only where those counts already
are, and that is the input the lane has always lacked.

### 9.2 What the exercise found

1. The quantity that the directional zero-point energy changes, the block's lowest energy, cancels from the target
   and from the lane's main tool, because both use energies measured from the vacuum (C1; argued).
2. The block's shortfall D_l is pinned between two such counts:
   l^3 sigma_bar_3(l) <= D_l <= 14 log X_full(l/2; l) (5.1; argued; tested on free lattice fields in 8.1, where it
   held at all 30 points and the lower half was tight to a factor of about the dimension; guide). At weak coupling
   the lower count is about 0.66 (guide), while a tiling with five or more blocks per side needs the shortfall below
   0.33. So no rise in the lowest energy can bring a weak-coupling block within such a budget.
3. Even perfect control of the shortfall would help the lane's main tool only by a constant: its threshold moves
   from 1/5041 to about 1/71, and the smallest admissible "block size times gap" from 17.04 to 8.52, still above
   the free-wave value 2 pi (C4; argued).
4. The most directional blocks (perpendicular half-turns, which are 't Hooft-twisted boxes) overshoot at tree
   level: their lowest energy lies above the infinite-space value by about 0.656/l (8.2; guide). A general lemma
   shows that such blocks cannot appear in any product upper bound of the periodic box (Lemma FL, Corollary FL1;
   argued, given the guide sign).
5. Row 1301, run in parallel by gpt-6.2-astra, found a better mix: one block of each of the eight twist types,
   whose shortfall cancels exactly at weak coupling, and a test built from ratios in which no vacuum energy appears.
   Its open step is a count-type inequality at one block size. At finite coupling the zero-point energy makes that
   mix's shortfall slightly negative (guide), which rules out the plain product form, but not row 1301's ratio test.

### 9.3 Filters corrected

- **"A tiling needs D_l of order 10^(-8)"** (row 1285): too strong as a requirement. The budget depends on the
  number N of blocks per side: 12.97 at N = 2, 2.56 at N = 3, 0.81 at N = 4, 0.33 at N = 5, 4.8 x 10^(-8) beyond
  N = K/2 (C5; argued, decimals guide). For N <= 4 the tree-level zero-point energy fits the budget (guide), and the
  binding term is then the blocks' own count, which is the target itself at a block of side at least L/4. On the
  path; no tool comes back.
- **"The binding factor of a tiling is each block's Casimir defect"** (row 1285, from the fixed-block limit): wrong
  at weak coupling for N well below K, where the first term binds by about eight orders of magnitude (C6; reading,
  guide); right only for times longer than the block (row 988's regime), where for small periodic blocks the
  near-degenerate flux sectors bind first (row 720).
- **"The directional zero-point energy lowers the defect but falls short of the size a tiling needs"** (the owner's
  sentence): it cannot reach that size, for a structural reason (the sandwich's floor), and it is the wrong lever,
  because it cancels from the target (C1).
- Confirmed, not new: check 1292's correction that thermal sums do control the defect (C3, re-derived).

### 9.4 Routes worth doing

1. **Row 1301's seam inequality** (K_beta <= sum_m W_m for all large t at a positive physical tile width, its (13)-(15)).
   You would have to believe that the signed seam integral of the eight-flux mix is controlled at one physical scale.
   Cost: high. First test: a check of row 1301's PROVED statements (W2). It would change the lane's crux into one
   explicit normalized inequality between eight blocks and one doubled cube, with a fixed gap fraction as output.
2. **R5, an explicit small K in row 1161's finite-aspect step.** You would have to believe that the compactness
   argument has a constructive version. Cost: high. First test: find the step of row 1161 L146 that has no explicit
   constant. It would shrink the needed physical box and every budget in proportion to K; it does not touch the wall.

### 9.5 What not to do next

- No lane on lowering D_l of periodic blocks, or on a larger zero-point energy: C1 and the sandwich say it cannot
  move the target.
- No tiling by identical twisted blocks: Corollary FL1 (given the guide overshoot).
- No mirror or slab rewrite of the target as a route (R3): it is the target restated.
- No Wilson simulation of D_l as evidence: a run cannot discharge, and the sandwich already prices D_l.
- No further exercise on this wall.

### 9.6 The exact price (argued, not checked)

For tilings by periodic blocks, "D_l <= eps at one block" forces l^3 sigma_bar_3(l) <= eps and follows from
log X_full(l/2; l) <= eps/14. Both are statements about the count of excited states at the block, from which the
zero-point energy cancels. Within RT-iii, every range of N needs at least one of: Theorem S's seed at the block
(13 <= N <= K/2), the full target at a block of side at least L/12 (N <= 12), or D_l <= 4.8 x 10^(-8) (N > K/2),
which the record can supply only through a seed of 3.5 x 10^(-9). So the wall is the seed at one block, priced
from both sides; it is not a statement about the size of the directional zero-point energy.

### 9.7 Work items

**W1 (check request; first).** A model that did not write this file (gpt-6.2-astra max preferred, cross-provider)
checks, line by line by hand, in this file: C1 (3.1); C2 (a), (b); C3's re-derivation; C4 (the defect-explicit
doubling inequality, the thresholds 1/100 by hand and the floor 8.52); C5 (the ranges, especially the implication
for 13 <= N <= K/2); the sandwich's lower half (5.1, with the correction of 8.3 item 1); Lemma FL and Corollary FL1
(8.2); the cross-result on row 1301's mix (8.3). Inputs: `gap-crux-restate.md` L29-46, L170-230;
`gap-owner-tiling-opus.md` L352-411; `gap-owner-tiling2-check-astra.md` L30-56, L85-96;
`gap-mini-solve-ar-opus.md` L101-143; `gap-owner-tiling3-astra62.md` L21-50, L270-308. Test first: the transverse
tiling and the two limits in the lower half; FL's normalization; C5's use of delta >= 0. Verdict per statement:
HOLDS, HOLDS AFTER CORRECTION, FAILS (with the line and a counterexample if one exists). Committed files carry no
home-directory paths. Output `library/gap-exercise-dirzeropoint-check-astra.md`, ending with one RESULT line.

**W2 (if not already queued; at 16:42Z an untracked `library/gap-owner-tiling3-check-opus.md` of another session
existed in this clone, so a check of row 1301 seems to be under way; then send only the zero-mode question below to
it).** Claude Opus 5.5 max checks row 1301 (`gap-owner-tiling3-astra62.md`) line by line:
(1) and its parity decomposition; (6) and the averaging argument; the 12-plaquette counterexample; (12); the
identity (13); (14) and the weak-coupling sign; (15). Add: does the leading zero-mode term (8.3 of row 1302) change
any of them? Output `library/gap-owner-tiling3-check-opus.md`.

**W3 (R5).** One reading pass (gpt-6.1-sol or gpt-6-luna) of row 1161's finite-aspect argument
(`gap-solve9-astra62.md` L140-150 and the lines it cites) that names each constant chosen by an existence argument,
and the first step with no explicit bound. Output `library/gap-k-explicit-read.md`.

**Not proposed.** A proof lane on D_l of periodic blocks (priced above); a lattice computation of the twisted
overshoot beyond tree level (it would only sharpen Corollary FL1, whose route is dead); a race on the replacement
question (it is the lane's crux, already raced: rows 998, 1032, 1291).

### 9.8 Appendix: approach registry, and short lists

| Family | Object or formulation | Mechanism or invariant | Terminal obligation | Strength vs target | Status | Concrete evidence | Reopen condition |
|---|---|---|---|---|---|---|---|
| R1 deficit lowering | E_0(l) of periodic blocks | operator lower bounds (Lemma E0's lower half) | D_l <= eps at one block | target-equivalent at the needed eps | blocked-equivalent | sandwich (5.1), C1 | a failure of the sandwich |
| R2 long-time twisted seeds | twisted fibre | Lemma E with an explicit deficit | deficit bound at aspect above 1; growth across the twist plane | unknown | blocked-local | 3.4; row 988's remark | a valid inequality that tiles across a twist plane |
| R3 mirror slab | slab of thickness n/K | crossing (C2) | the slab deficit | target-equivalent | retired | C2 (b) | a mirror theory with a provable gap |
| R4 misframing | D_l and the counts | sandwich, cancellation, log 2 element | none (re-prices the wall) | not a route | candidate-complete as a price, argued | 5.1, 8.1 | a FAILS in W1 |
| R5 explicit K | row 1161's aspect | compactness made explicit | an explicit K | weaker (sizes only) | unexplored | none | - |
| R6 identical twisted blocks | m = (1,1,1) boxes | overshoot of the vacuum energy | a product upper bound | - | retired (Lemma FL, Corollary FL1) | 8.2 | a guide sign reversed beyond tree level |
| Row 1301's mix (not this run's) | eight flux sectors on a doubled cube | exact cancellation of the vacuum defect; ratio test | K_beta <= sum_m W_m at a physical width | unknown | active (row 1301) | row 1301 (1), (14), (15) | - |

**Assumptions most likely to be wrong:** c3/c4 ("the defect binds"; corrected here); d7 (the 10^(-8) budget as a
requirement; corrected); b4 (tree-level matching as a guide to signs beyond tree level; 8.2 and 8.3 rest on it).
**Most expensive if wrong:** a1 ((N-phys) as the lane's gap target; rows 1161, 1225, 1232); b2 ((TM), on which every
lemma here rests; checked). **Literature worth translating:** Bachas (arXiv:quant-ph/0611082), a reflection-positivity
sign for Casimir energies, as a template for Lemma FL-type statements; Pawellek (arXiv:1303.4708), an exact
crossing identity for free massive lattice fields, as a test of the sandwich's sharpness; van Baal, Nucl. Phys. B 289
(1987) 628, for one- and two-loop twisted-box energies, to turn 8.2's tree-level overshoot into a lattice statement.

**Strong words re-read.** "New" is used only with the search scope of step 5. "Every" in C1 means every normalized
trace and every ratio in which the ground energies cancel. "Exact price" is argued, not checked. Nothing here is
called proved, sound or a theorem of the lane.


RESULT: Row 1302 gap-exercise-dirzeropoint-opus (Claude Opus 5.5 max, laptop subagent, 15:54Z-16:42Z by date -u; repo exercise skill steps 0-9 at origin/main 8b11ae2bb, --subagents 0, GOAL.md contract in place of the framework refresher; author only, checked by no one; two free-field GUIDE runs under the numeric lock). Mass gap NOT proved, nothing disproved; (N-phys), (W) and the seed at one block stay OPEN. Argued here (unchecked): (C1) the directional zero-point energy, Lemma E0's quantity, is a ground-energy shift and cancels from (N-phys), from every normalized trace and from the seed; (sandwich) for even l >= 6, l^3 sigma_bar_3(l) <= D_l <= 14 log X_full(l/2; l) (lower half re-derived from the idea of row 1291's Lemma CR, upper half re-derived after check 1292), so raising a block's ground energy can lower its Casimir defect only to the bulk thermal pressure at the block's temperature, about 0.66 at weak coupling (GUIDE), below which lie all RT-iii budgets for N >= 5 (GUIDE run: the sandwich holds at 30 free-field points, lower half tight to a factor of about d); (C5) RT-iii by ranges of N, with Theorem S's seed implied for 13 <= N <= K/2; (C4) perfect defect control would move Theorem S's threshold only from 1/5041 to 1/100 by hand (1/71 exact) and the massless floor from 17.04 to 8.52, still above 2 pi; (Lemma FL) every product tiling bound has a non-negative defect, so blocks whose vacuum lies above the bulk cannot appear, and the m = (1,1,1) twisted (perpendicular half-turn) blocks overshoot by 0.656/l at tree level (GUIDE; Corollary FL1). Corrected filters: the 10^(-8) budget is a large-N figure, not a requirement (12.97 at N = 2, 0.81 at N = 4); 'the binding factor is the Casimir defect' fails at weak coupling, where the blocks' own thermal term binds by about 10^8 (GUIDE). Exact price (argued): the wall is the seed at one block, a count of excited states, priced from both sides, not the size of the zero-point energy. Late comparison: row 1301 (gpt-6.2-astra, unchecked) independently cancels the defect with eight flux sectors and uses a vacuum-free ratio test, consistent with C1; at finite coupling the zero-point energy makes that mix's product defect negative (GUIDE), so only its ratio route survives, open at its signed seam integral. Output library/gap-exercise-dirzeropoint-opus.md.
