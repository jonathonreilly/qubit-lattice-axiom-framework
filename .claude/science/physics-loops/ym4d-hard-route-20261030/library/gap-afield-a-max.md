lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-16T13:36Z

# gap-afield-a-max: far-afield invention row A (queue row 1031)

Research-stage working state. Nothing here is a public claim. Marks: PROVED (written argument, unchecked by a
second reader), ARGUED (argument with a named gap), OPEN, FAILS. A numeric run here can only refute or guide.

Pinned at commit 58baf6efc. Started 2026-11-16T01:36Z (by `date -u`). Worker: Claude Fable 5.2, max effort, Mac mini worker 1.
No subagents. No commit, claim or push from this machine.

## 0. Plan (eight steps; one step per response; each step appends its result here before the next)

1. Read the inputs: FINISH.md head and rules, `parts/gap.md` in full, `library/gap-dichotomy.md`, the exercise
   skill at main commit 8b11ae2bb9 with its reference file. Write Section 1: the wall as read, the open items and
   their consumers, the kill tests.
2. Registry grep before naming any idea: the lane's idea inventories and today's rows 1011-1030. Write Section 2:
   what is already on file for each of the named fields.
3. Generate at least ten ideas from the named fields (probability and stochastic analysis, optimal transport and
   entropy, ergodic theory of the scale shift). Each with source, exact statement needed on the 4D SU(2) lattice,
   consumer. Write Section 3.
4. Literature lens: fetch the sources that the ideas rest on and record the exact statements with pages. Write
   Section 4.
5. Kill fast: run each idea against the test list of the row (Lemma PT, Proposition NP, Theorem D2, Lemma SHEET,
   compact U(1), frozen Q_8 and 2T, the five-dimensional test, Lemma CEN, Lemma WN, the four-test spec check).
   A rename of the crux is a FAIL. Write Section 5.
6. Rank the survivors by (what they would change) / (cost to find out). Write Section 6.
7. For the top one or two: write the first lemma and try to prove it by hand, or build the counterexample.
   Write Section 7.
8. Re-read every PROVED item, take anchors from grep, write the verdict table and the RESULT line. Section 8.

## Status log (times from `date -u`)

- 2026-11-16T01:36Z: file created with the plan; inputs not yet read beyond GOAL.md and the queue row.
- 2026-11-16T01:36Z: Step 1 done. Read in full: GOAL.md, the queue row (FINISH L1112), FINISH.md L1-84 and L299-352,
  `parts/gap.md` (251 lines), `library/gap-dichotomy.md` (473 lines), the exercise skill (703 lines) and its
  reference `proof-search-governance.md` (126 lines), both fetched at main commit 8b11ae2bb9 into new /tmp folders.

## 1. The wall as read (exercise steps 0-1, short form)

Replacement made (skill, "Framework Refresher Read", last paragraph): this is a standalone proof target, so GOAL.md
and the rules of FINISH.md were read in place of the framework axiom files.

### 1.1 Plain version

We study the SU(2) lattice gauge theory in four dimensions in a periodic box. Two numbers describe a box of a
fixed physical size: its Casimir free energy D (free energy minus the bulk part) and its lowest energy gap times
its side, z. The lane proved an engine: if one box is "good" (excited states have total weight below 1/5041 at a
time of half the side), every larger box has a gap. The wall: nobody can show that a good box exists at any
physical size once the coupling is of order one. Every tool on file is also true for models with a massless
particle (compact U(1) at weak coupling, a product with a massless factor), where no good box exists. Getting
past the wall means one statement that is false for those models and provable for SU(2). Analogy (marked as
such): a staircase that is proved to go up for ever once one step is found, and no step is found.

### 1.2 Precise version (quoted; not rewritten)

- **(W), repaired form** (`parts/gap.md` L21-23, from `library/gap-zd-astra.md` item 18): there are a bound (L_0, D_0)
  of (BDD-Delta) and L in P with L >= 4 L_0 and z^-(L) > 256 D_0 + 30. Objects: `library/gap-dichotomy.md` 1.1-1.3.
- **Price** (`parts/gap.md` L246-250): (W) iff (BDD-Delta) and (Z-UNB) (Theorem ZD-c). (W) follows from (CAS)
  with theta < 1 and an extensive base. Theorem CR: given (BDD-Delta), (W) iff Omega(D_0) has no uniformly
  recurrent element, which is (LIOU).
- **Kinds of input** (`parts/gap.md` L47-50): (K-one) a property of the measure at one scale in the band;
  (K-flow) a statement that starts from first-passage data and is carried through the band by a step that fails
  for U(1), frozen groups and products with a massless factor.
- **Outcomes that do not count:** a computer-assisted step; a supremum over tilts (false by Theorem D2); a form
  uniform over plaquette coupling fields (false by Lemma SHEET); a statement that renames (W), (CAS), (LIOU),
  (BDD-Delta), (PHYS-SEED) or a unit-level log-Sobolev inequality without a new mechanism.

### 1.3 Open items named by the row, with their consumers (from `parts/gap.md` L108-143)

| Open item | Where | Consumer |
|---|---|---|
| (W) | row 998; `parts/gap.md` L108 | the gap |
| (BDD-Delta): D^+ bounded on physical sizes | L109; no row attacks it (`gap-dichotomy.md` L362) | Theorem ZD-c, Theorem CR |
| (LIOU): no uniformly recurrent critical element | L138; row 1017 | Theorem CR (4) |
| (CAS) with theta < 1 | L111; row 708 | (W) with the base (TH) |
| unit-level log-Sobolev inequality, (U1), (U2), (HC-phys), (LSI-br) | L115, L170 | (W) with (TH); route LC |
| (TB)_n, one inequality of the decimation line | L142; row 1025 | the flux half at one coupling (Tomboulis) |
| (SYM) with (REG): a local covariant frame with j - d conserved | L141; row 1026 | route (ii) of row 1018 |
| (SER), (SPR) with kappa phi < 1 | L140; row 1018 (T-vor) | vortex containers |
| (FL), (DEC) | L140; row 1018 (T-pin) | cross-cell Neumann covariance |
| (PLATEAU) | L143; row 1028 | Proposition A1 |
| (E0-tor) | L137; row 993 | (DET), (HC-phys) reduction |
| (EV-STEP) | L117; row 731 | (G_ev) |

### 1.4 Kill tests of the row (their valid form is the test table of `parts/gap.md` L196-237)

Lemma PT (product with a massless factor), Proposition NP (no-seed product with contracting D), Theorem D2
(supremum over tilts), Lemma SHEET (uniform over coupling fields), compact U(1), frozen Q_8 and 2T, the 5D test
of `library/gap-crux-fp.md` (per row 1028 it tests (BDD-Delta), not (LIOU)), Lemma CEN (link symmetries are
central), Lemma WN (free lab-frame moves do nothing), the four-test spec check. An idea that renames the crux FAILS.
