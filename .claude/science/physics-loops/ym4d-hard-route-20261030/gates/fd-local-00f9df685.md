lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-02T13:21Z

# Gate fd-local (queue item 45), pinned at 00f9df685

**Provenance.** Model anthropic/claude-opus-5-5, effort high, worker mac-mini-worker, commit 00f9df685, side mapped. The gated file `library/fd-local.md` was written by OpenAI/Codex (its own pin 15c601852). So this reader is another provider, but this is one session's read: a same-model check is not independent in model, and neither this nor a cross-provider read is an audit. Verdicts steer research and grant no status.

**Outcome.** Sections 2 to 6 stand at the level of their steps. No statement is WRONG. The flat several-jump coercivity is ADVANCE given the one-jump premise, which this gate did not check. (G2) conflicts with no reader of t_0, and it already follows from the printed bound t_0 >= C R_1^fill once a_* is small against (R L)^-2. The domain gap of (G3) stands but is narrower than the file says. Curved (LC_U) stays a gap.

## Verdicts

| Statement | Section | Verdict | Note |
|---|---|---|---|
| Reading of the printed clearance: margins 3 t_0 s_l and (t_0/3 - 2 t_0/L) s_(l+1), common margin t_0 s_l/4 | 2 | ADVANCE | Rechecked against `quiet-boundary-rarity.md:45-49`. Valid for L >= 32 in either lattice metric |
| (G1), the near-two-wall family | 2 | ADVANCE | (N), (B) hold, using the x_d layers of Lemma BG. Walls are at distance 8 t_0/L^2 in units of s_(l+2) |
| Moving centres do not help | 2 | ADVANCE | Correct under its hypothesis of one global Lipschitz constant per cutoff. It shows no more than that; see "Not established" |
| (G2) available in the order of constants | 2 | ADVANCE, and stronger | See the next section. The cover uses t_0 >= 8000 R L^2 |
| (G3) on complete families, and unions | 2 | ADVANCE | Also holds for the consumer's w = 6 t_0 families: lower margin 2w/3 = 4 t_0, outer margin t_0 (2L - 7), both in level-l cells. This closes the check the file's Section 7, item 3 left open |
| (G3) for all data of (I_l^D) | 2 | CORRECT-NO-ADVANCE | The file's own gap. See D2 |
| Skipped-scale test; separation t_0 s_(k-1)/4 of boundary F_j and boundary F_k | 2 | ADVANCE | |
| Total-overlap lemma: h, sigma <= h <= L sigma, greedy cover, (G4), one jump per 10Q_i, chi_i | 3 | ADVANCE | The count is at most 12.12^4, below 16^4. |D chi_i| <= 530/r_i is enough; C_N = 10N is safe |
| h <= s^# with collar b = 1000R | 3 | ADVANCE | |
| (C1), (C2) | 4 | ADVANCE | The true overlap is 1 per component, so 8 is loose |
| Bumps, (C3), (C4) | 4 | ADVANCE | Moments rechecked by hand. Composite rows are exactly (1-t, t): at two levels W(z) = (z+1)/L^2, by hand. K_* is loose |
| Gauge test, (C5) | 4 | ADVANCE | Summation by parts and the commutator expansion rechecked term by term |
| Eps and ordinary commutators | 4 | ADVANCE | sqrt(2) suffices where the file has sqrt(6) |
| Flat IMS, W <= 16 C_0 E | 4 | ADVANCE, given one-jump coercivity with C_0 free of L | Absorption rechecked: (4C_0 + 1) e < 1/25. The premise is not gated here. See D3, D4 |
| No strengthened Cauchy-Schwarz needed | 4 | ADVANCE | |
| Scalar cutoff commutes; pure gauge by conjugation | 5 | ADVANCE | |
| (LC_U) at U = 1 and at pure gauges | 5 | ADVANCE | Support stays in P+; the constant is below 2^30 K_*^2 c_chi^2 |
| (LC_U) at curved backgrounds | 5 | gap, as labelled | The scaling S ||F||_(L^4(B_S)) <= C a_* agrees with `fibre-propagator.md:148` |
| Exact gauge test | 5 | ADVANCE | Conditional as stated |
| Section 6, consumer table and operator distinction | 6 | ADVANCE | Each cited line read and agrees |

## (G2) against the readers of t_0

**Decision: no conflict.** Two independent reasons.

1. **(G2) is already available from the printed bound.** Line 24 of the mapped file has t_0 >= C R_1^fill with R_1^fill = (K_1/T)^(1/2) and T = a_*/L^2, so t_0 >= C K_1^(1/2) L a_*^(-1/2). Hence

       a_* <= C^2 K_1 / (10^8 R^2 L^2)    implies    t_0 >= 10^4 R L^2.

   a_* has only an upper bound and comes after L, and R comes before L, so this is one more condition on a_th(L). The file says (G2) is "not an existing proved consequence of the smaller printed lower bounds" and leaves open whether line 24 forces it. It does, under this smallness of a_*. On this route no reader changes form, because every C(L) is uniform in a_* <= a_th(L) (mapped:947). I found K_1 only through T R_1^2 = K_1 (mapped:1077). Its independence of a_* is read from line 24, not proved. If that failed, reason 2 still applies.

2. **Taken as a direct lower bound, it meets no upper bound.** Every bound on the brick side that I found is a lower bound, or sets a constant fixed after t_0:

| Reader | What a larger t_0 does | Where it is paid |
|---|---|---|
| (RAR^1) exp(-8 w_0 lambda_l), w_0 = 6 t_0/L | lambda smaller by about w_0/3 | l_0, l_1 come after w_0 (upper-chain:1569) |
| r_(j+1) >= 112 w_0 | C_B(L) >= exp(112 kappa w_0) | Free constant, read only through ratios (upper-chain:1569) |
| tau = eps_q T/(2 t_0^2 |b^++|^(1/2)) (QBR:225, upper-chain:1533) | mu-side rate falls as a power of t_0 | l_0, l_1 |
| Typical Dev_b, entropy t_0^4 log x (QBR:25, 336) | x_* grows | x_* is last |
| |N_pay| <= C (d_x + t_0)^4 |Y| (QBR:247) | Losses per cell grow | x_*. The rough-top use read at statement level only |
| r_lift = (C/rho) log(t_0/(eps_q T)) | Logarithmic | t_0 >= 4 r_S and t_0 >= r_S L/3 stay solvable, and (G2) helps the second |
| (J+), r_0, Lemma BG, r_c = 36 t_0 <= t_0 L | Lower bounds, L >= 36 | None |
| Copy counts with B >= 8 t_0 (`seam-nlpay.md:338`, `paid-inputs-frozen-energy.md:173`) | Later start level of a counterexample count | Not a bound on t_0: those notes hold t_0 fixed |

Constants printed before t_0 do not read it: (6.1) and (AE-S) of `energy-by-stages.md` have no t_0 in C_5, C_6, c_S'. The count of patches is by disjointness. The costs above are real: rates fall as powers of t_0 and x_* rises, but all of it lands on constants chosen later.

Scope of this survey: a pattern search for inequalities in t_0 across the mapped part, upper chain and allowed library files, then reads of the hits (`checks/gate_fd_local/t0_readers.txt`). It is not a line-by-line read of 35 files.

## Defects

**D1. Source, not this file: the clearance claimed for (NC) is not supplied.** `fibre-propagator.md:142` says clearance t_0 cells of the coarser level, and the proof below it says each patch meets at most one wall "by clearance". The supplier gives 3 t_0 fine cells on one side. Failure: (G1) with 8 t_0 < R_0 L^2 has both walls in one patch. Breaks the proof of (NC) as printed unless a_* is small as above. Repair in hand: (G2), or the a_* condition. For the owner of `fibre-propagator.md`; the lead forwards.

**D2. (G3) is not identified with the data of (I_l^D).** The file's gap stands, with this sharper form. Failure: `quiet-boundary-rarity.md:61` allows "a set of frozen level-l bonds" with no collar, and :277 says only that Sigma_k lies under frozen parents. If the frozen level-l set is exactly the shadow of Sigma_(l-1), then F_(l-1) and F_l share a boundary, the leaf scale jumps two levels, and the cover does not apply. This is not a refutation: no proof I read uses such a datum.
- (a) A top collar is vacuous at the top of a fibre. At fibre level k all level-(k+1) parents are fixed, so F_(k+1) is whole. Stops at QBR:111, 163 create a family with top t at the fibre they work in, and recursion goes down, so a family is read only at levels <= t. Read at statement level, unchecked through each proof.
- (b) What stays open is lateral closure: a new family closed on an older layer (QBR:35-39), where (N), (B) do not hold for the new family alone. There one must show that a point of the new Sigma_l near the junction has its cube in the union F_(l+1).
- Repair, unproved: put the collar in the definition of an admissible datum, and check it at each stop and at junctions.

**D3. Line 24 needs new entries.** The note uses R before L, and L >= 4K from (C3). With the file's constants R >= about 2^290 (1 + C_0)^(1/2) and L_0 >= 2^122. Absolute, so harmless, but R before L needs C_0 free of L. That rests on Lemma D-coer (`fibre-propagator.md:122`), not checked here. Repair: add R and these bounds to the order.

**D4. Facets in a patch: the scale check is missing.** Section 3 hands several facets to the brick extension premise without checking size. Lemma BG(b) needs a ball of radius t_0 s_l/8, so 10 R s_(l+1) <= t_0 s_l/8, that is t_0 >= 80 R L. (G2) gives this. Source line 156 says "one flat wall", but a patch can hold a fan of up to five bricks, so C_0 must be the constant of Lemma D-coer with C_ext for fans. Repaired here, given that lemma.

**D5. Symbols.** t_0 also names a moment parameter (mapped:109, 846, 848, upper-chain:619, where t_0 <= c T^2), a gap (upper-chain:568) and a gauge transformation (`lattice-uhlenbeck.md:107`). These are not brick sides, and a future reader searching for upper bounds will hit them. Line 24 prints tau before t_0, while QBR:225 defines a tau that reads t_0; if they are the same symbol it should move after t_0. Harmless: only l_0, l_1 read it.

## Not established

- That L^2 clearance is necessary. Section 2 excludes one normalized kind of partition. A cutoff with a sharper slope on the fine side escapes its hypothesis, though it then costs about L^2/R^2 at the coarse weight. The file does not claim necessity.
- Lemma D-coer, one-jump F-D, inf-sup and conjugation at curved backgrounds, and (LC_U).

## Runs

One, `checks/gate_fd_local/exact_rows_bumps.py`, exact rational arithmetic, criteria written first, output in `exact_rows_bumps.out`. **First run: PASS on all criteria.** Composite rows are exactly (1-t, t) at L = 32, 33, levels 2 and 3. Bump moments and the bounds on avg(b), the p-masses, v, sup and Lipschitz hold at m = 32, 33, 40, 64, 1024. The IMS absorption holds at C_0 = 1, 4, 100, 10^6. This covers those sizes only and discharges nothing; the verdicts rest on the hand arguments. Actual sizes are far inside the file's constants: v about 0.0104, sup about 14, Lipschitz about 207.

Memory free read 47, 51, 45, 45, 42, then 56, 54 percent. A first lock at 01:36Z was released unused when memory fell to 45. The job ran under the lock at 01:39Z, at 54 percent. `checks/gate_fd_local/t0_readers.py` is a text search, not a numeric job.

## Read, and not read

Read: `library/fd-local.md` Sections 2 to 6 by hand first, then Sections 1, 7, 8, whose conclusions agree with the above except for the (G2) decision and the narrowing in D2. Passages cited above in `quiet-boundary-rarity.md`, `fibre-propagator.md`, `fd-jumps.md`, `energy-by-stages.md`, `ue-multilevel.md`, `history-budget-sum.md`, `seam-nlpay.md`, `paid-inputs-frozen-energy.md`, `parts/hard-core--mapped.md`, `parts/upper-chain.md`.

Not read: `library/lc-u.md`, the Sussman-Alpoge repository, any gate.

Firewall: no file barred on the mapped side was opened. Some wildcard searches passed over the whole of `library/`, including barred files; none of their lines appeared in the output. The `parts/upper-chain.md` interface lines read carry a few clauses about the independent map, as that file does; they fed no proof here.
