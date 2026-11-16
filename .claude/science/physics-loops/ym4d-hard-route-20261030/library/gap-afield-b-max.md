lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-17T00:18Z

# gap-afield-b-max (queue row 1032): far-afield invention row B

Started 2026-11-16T01:36Z (from `date -u`), pinned at commit 58baf6efc. Session model: claude-fable-5-2 at max effort. No subagents, no numeric job started so far.

Run 2 (this run): started 2026-11-16T12:18Z (from `date -u`), pinned at commit 594d6491b. The first run (01:36Z) wrote only the plan below and then failed for lack of credits (lead note in FINISH.md row 1032); its plan is kept and followed. Session model: claude-fable-5-2 at max effort. No subagents.

This file is written section by section. Each section states what was done, what failed, and what is left.

## 0. Status line (updated in place)

- State: run 2 started 2026-11-16T12:18Z; step 1 done (digest in Section 1); step 2 (lane grep and kill tests) in progress.

## Plan (eight steps, one per response; each appends its result here before the next)

1. Read: FINISH.md (rules, efficiency, Build on published work), `parts/gap.md` in full, `library/gap-dichotomy.md`; fetch the exercise skill at main commit 8b11ae2bb9 into a new scratch folder and follow it. Record the wall, the repaired (W), the dichotomy and the open items in a short digest (section 1).
2. Lane grep: rows 1011-1030 and their library files, `library/open-core.md`, the registry in `parts/gap.md`; list what is already tried so no idea is redone, and write the kill tests in usable form (Lemma PT, Proposition NP, Theorem D2, Lemma SHEET, compact U(1), frozen Q_8 and 2T, the five-dimensional test, Lemma CEN, Lemma WN, the four-test spec check) (section 2).
3. Ideas, fields A and B: quantum many-body and quantum information; operator algebras and axiomatic field theory. Each idea: source, exact statement needed on the 4D SU(2) lattice, consumer in the chain (section 3).
4. Ideas, fields C, D, E: geometric analysis; representation theory and harmonic analysis on SU(2); topology. Same format. At least ten ideas in total (section 4).
5. Kill fast: every idea against every kill test; an idea that renames the crux is a FAIL (section 5).
6. Rank survivors by (what they would change) / (cost to find out) (section 6).
7. Top one or two survivors: write the first lemma and try to prove it by hand, or build the counterexample (section 7, split over several responses if long).
8. Close: marks PROVED / ARGUED / OPEN / FAILS, credits, complete briefs for follow-up work items, RESULT line (section 8).

## 1. Digest of the wall (step 1; read, no verdict changed)

Read in full in this run: `GOAL.md`; `FINISH.md` L1-84, L299-362, rows 1031-1033 and the lead notes at L1128-1131; `parts/gap.md` (all 255 lines); `library/gap-dichotomy.md` (all 473 lines); the exercise skill at main commit 8b11ae2bb9 (703 lines, fetched to a scratch folder) and the reference it requires before its step 7, `physics-loop/references/proof-search-governance.md` (126 lines, same commit). The skill's framework refresher read is replaced by `GOAL.md` and `FINISH.md`: this is a standalone proof target that reads no framework axiom (skill L130-132). As in row 1031, this run is the slice of the skill's steps 6c-9 (tests in valid form, routes, kill, rank, real attempts, report); steps 0-6b were done by rows 878, 998, 1003 and are not redone.

**Objects** (`gap-dichotomy.md` 1.1-1.3). Wilson SU(2) on a periodic torus with integer sides n = (n_1, ..., n_4), all at least 3; A(U) = sum over plaquettes of (1 - (1/2) tr U_p); Z(n; beta) = integral of exp(-beta A); F = log Z; f = inf F(n)/abs(n); Delta(n) = F(n) - f abs(n) >= 0; the Casimir free energy D(a) = Delta(a, a, a, a). For a box B of three sides, T_B is the transfer operator, Z(k, B) = Tr T_B^k, eigenvalues lambda_0 > lambda_1 >= ... >= 0, gap m(B) = log(lambda_0/lambda_1), thermal sum S(k; B) = sum over i >= 1 of (lambda_i/lambda_0)^k. A family with units: data Z_j at the couplings beta_j of the Sussman-Alpoge trajectory, u_j = l_1/a_j, (S0): u_j a multiple of 4, at least 12. P = {2^i l_1}. D^+(L) = upper limit of D_j(L/a_j); z^-(L) = lower limit of (L/a_j) m_j((L/a_j)^3).

**The wall, repaired form** (`parts/gap.md` L21-23). (W): there are a bound (L_0, D_0) of (BDD-Delta) and L in P with L at least 4 L_0 and z^-(L) > 256 D_0 + 30.

**The engine** (Theorem S; Corollary S3'; Theorem ZD-c). (PHYS-SEED): one physical size l with upper limit of S_j(l/(2 a_j); (l/a_j)^3) below 1/5041. A seed gives a gap for every larger cube, uniformly in j. (W) iff (PHYS-SEED) iff [(BDD-Delta) and (Z-UNB)]. Note for my fields: Theorem S is already a finite-size criterion in the sense of Knabe (a property of one finite box gives the gap of all larger boxes). So an idea "use a finite-size criterion" is not new as a frame; it must supply the seed, which is the wall.

**The trichotomy.** Exactly one of (I) (PHYS-SEED); (II) not (BDD-Delta) (the Casimir free energy is unbounded on physical sizes); (III) (BDD-Delta) and z^-(L) <= 256 D_0 + 30 at every size (branch G at every size). Form 2 (Theorem CR): given (BDD-Delta), (W) iff Omega(D_0) is empty iff it has no uniformly recurrent element. (LIOU) = no uniformly recurrent critical element; target-equivalent given (BDD-Delta).

**The open items the row names**, with where they stand at this pin (`parts/gap.md` L108-148):

| Item | What it is | Standing |
|---|---|---|
| (W) | the wall | OPEN |
| (BDD-Delta) | D^+ bounded on physical sizes from some L_0 on | OPEN; target of no row; row 1031's "no soft proof" claim is unsupported after its checks |
| (LIOU) | no uniformly recurrent critical element | OPEN, target-equivalent given (BDD-Delta) |
| (PLATEAU) | the open alternative in Proposition A1 of row 1028 (keeping the ultraviolet data in the limits) | OPEN |
| (TB)_n | the one inequality of the Tomboulis-Kanazawa decimation line (row 1025) | OPEN; gives the flux half at one coupling, not the seed |
| (SYM) with (REG) | a local covariant frame with j - d conserved and square integrable (route (ii), rows 1026, 1034) | not decided, not the deciding obligation (row 1034); O1, O2 named; rows 1036-1046 continue |
| (SER), (SPR) | the two open items of the vortex-container form (T-vor) of the short step (row 1018) | OPEN |
| (FL), (DEC) | the two open items of the pinned form (T-pin) (row 1018) | OPEN |
| unit-level log-Sobolev inequality | route LC's reopen condition (row 1021) | OPEN, the wall in log-Sobolev form |
| (E0-tor) | torus independence of the account's vacuum counterterm | OPEN (supply side) |

**What a new idea must be** (`parts/gap.md` L47-50, L93, L233-242, L254-255). A (K-flow) statement: it reads the first-passage data of Wilson SU(2) and is carried through the band by a step that is false for compact U(1), for frozen groups and for a product with a massless factor; or a (K-one) property of the measure at one scale. "Selective" means false for a massless factor. A pass of the tests is no support. For (K-flow) tools the lane has constraints and no refutation device.

**Standing verdict of the lane before this row**: no route is near closure; every proved piece is blind (true for every datum); the 2D pinned-cell port fails in the class of all pins; route (ii) (aligned frames) is open with (N1)-(N3), upper faces and (O1) remaining; row 1031's ten ideas all failed.

Left for step 2: the exact statements of the kill tests, and the grep of the lane for my five fields.
