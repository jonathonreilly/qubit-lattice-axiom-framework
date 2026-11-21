lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-21T18:38Z

# Row 1358, gap-mini-dualstep-fable: the step into the dual end class

Started 2026-11-21T06:38Z (date -u) at commit 6c42642f5 on branch claude/ym4d-hard-route. Research-stage working state. It grants no status, and nothing here is a public claim.

Labels: PROVED, ARGUED, GUIDE, OPEN, as the queue row asks.

## Step 0. Orientation (written 2026-11-21T06:51Z, date -u)

Read, statements only unless a proof is named:

- `GOAL.md` (whole); `FINISH.md` L1-84, L299-360, and the rows 1326, 1331, 1332, 1335, 1340-1358.
- `parts/gap.md` L1-104 and L213-322 (state of attack, route registry, test table, the exact price).
- `library/gap-mini-nphys-fable.md` (row 1354, whole; an earlier row of this worker).
- `library/gap-blockstep2-astra62.md` (row 1345, whole): the centre-sign block map (1)-(3), the bounds (4)-(10),
  the end class (11)-(12), the failure (14).
- `library/gap-blockstep4-astra62.md` (row 1351) L1-150: the neutral end class (10)-(11) and its proof.
- `library/gap-shrink-box-fable.md` (row 1332) Sections 1 and 6: Proposition CH.
- This worker's notes on the route-screening tables (rows 1189, 1194, 1199, 1200, 1237, 1241, 1273), on the
  prior-identity list and on row 1354.

The item, as the queue row states it: carry the Wilson trajectory, uniformly in the cutoff and through
mass-preserving block steps, from a coupling above the hand range into an end class with a strict margin that a
confining theory can reach. Row 1354 proposed the class (10*) of its Theorem E.

Not on disk at this pin: the outputs of rows 1356 and 1357 (running). The checks 1352 and 1355 are read in their
RESULT lines only.

## Step 1. How best to attack it (written 2026-11-21T07:03Z, date -u)

Also read for this step: `library/gap-mini-neutral-step-fable.md` (row 1353) Sections 2, 3, 5 and 6; the RESULT
line of its check (row 1355).

**1.1 What is on file for each leg (READ; rule 0a).**

- End classes. Coherent centre weights with a product reference: row 1345 (11)-(12) (periodic mass), row 1351
  (10)-(11) and (23)-(24) (neutral mass; an alternative-II class by row 1354). The Fourier-dual class (10*): row
  1354 Theorem E. Block links with a nearly Haar law and windows of any range: row 1353 Theorem END-D. END-D
  gives the two-period bound for each of the eight twisted masses, so it is an alternative-I class, and it is
  the natural home of (10*): a plaquette weight with a small odd part and a nearly constant even part is one
  window. Dobrushin ends: row 785 Theorem DOB, row 1340 Lemma END-RAY.
- Exact maps. The 2^4 cube map (row 1341), the centre-sign map (row 1345), the gluing and the strip elimination
  (row 1351), noise steps with pins (rows 861, 1340). Row 1353 2.2: Proposition CH is vacuous without maps that
  are local and explicit; row 1353 2.3: no class is carried by any map on file.
- The step. Open in every row. Row 1354 6.1 states it as (BS*). The single-link Doeblin bound (Simon and
  Yaffe) gives a perimeter law at every coupling and for every compact group; it is not selective
  (`gap-mini-solve-ab-opus.md` L52, `gap-brainstorm-max.md` L312).

**1.2 The plan.** The queue row names a target class, (10*). Before any step is attacked, one question decides
which map can have that target: what are the electric sheet weights of the Wilson image under the maps on file?
Row 1354 left this open. Its 4.4 said that the sheets "can be rare only after the angular environment is
integrated, by cancellation of the signs", and its 6.2 item 1 read the cost of a coarse centre monopole as a
thick-monopole free energy of order beta. Step 2 answers the question with a proof. The answer changes the
target, so it comes first.

After that the plan is: (Step 3) say which coarse variable has rare sheets and what the step then is, as one
statement in the law of the fine model; (Step 4 on) attack that statement.

**1.3 What I do not expect (GUIDE).** A proof of the step at a coupling of order one. Every row since 998 ends
at the same place, and the tools on file that reach order one are blind to the group. I state this before the
work so that the labels below are read against it.

