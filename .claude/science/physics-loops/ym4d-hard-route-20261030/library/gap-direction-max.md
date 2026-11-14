lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-14T16:54Z

# gap-direction-max (queue row 931): which order-one crux form for SEED-FP passes all fact tests

Status of this file: WORKING, written step by step. Pinned at commit 63cadeea0 on
`claude/ym4d-hard-route`. Author run, Claude Fable 5.2 at max effort, Mac mini worker 2,
started 2026-11-14T04:54Z. Nothing here is a public claim; research-stage working state.

Labels used below: PROVED (argument written here in full, checkable by hand), CONDITIONAL
(on named inputs), GUIDE (numeric or heuristic, carries no proof weight), OPEN.

## Plan (at most eight steps; one step per response; each appended before the next)

1. Read row 931's named inputs in full: `library/gap-seam-max.md` (row 929),
   `library/gap-oddgap-max.md` (row 930), their checks if present (rows 932-933), and
   `library/gap-status-1113.md` (the 912 consolidation). Record the exact statements of the
   fact tests (U(1) Coulomb, frozen Q_8, frozen 2T, ceilings) and of every candidate form.
2. Overlap check (rule of the prompt): grep `library/open-core.md` and the FINISH rows for the
   lemma I intend to attack; name any row that already covers it and stay off it.
3. Table of candidate crux forms against all fact tests; pick the weakest form that passes
   all of them, or state plainly that none does.
4. State the chosen form exactly, name the SU(2) property that must enter, and the step
   where U(1) breaks.
5. Proof attempt on its hardest lemma, stage 1 (set-up and reduction).
6. Proof attempt, stage 2 (the core estimate; record exactly what fails, if it fails).
7. Fact-test the attempt's own intermediate statements (U(1), Q_8, 2T, ceilings); a numeric
   run only as GUIDE, under the machine lock.
8. Next two attacks, each with its fact test, ranked by the chance the proof dies there;
   final RESULT line.

## Step log

### Step 1a (2026-11-14T05:10Z): inputs read in full (READ = read at the pinned commit, not re-proved)

Read in full: `library/gap-seam-max.md` (row 929, 478 lines), `library/gap-oddgap-max.md`
(row 930, 620 lines), `library/gap-status-1113.md` (row 912, 449 lines), FINISH rows 929-935.
Checks 932 (`gap-seam-check-astra.md`) and 933 (`gap-oddgap-check-astra.md`) are NOT on disk at
this commit, so rows 929 and 930 are used here as unchecked author results. Row 934
(`gap-vacsub-max.md`) holds only its header.

The four fact tests, as the rows state them (collected; each is a necessary condition on a
crux form, not evidence for it):

- FT-U1 (U(1) Coulomb must FAIL the form). Exact Gaussian values now exist for both halves.
  Glue half: free-photon model FP, log(1 + S_ev(a; (24a)^3)) > 31 (row 929 Theorem A2, PROVED
  unchecked; GUIDE 3.0e3); carrier = the k != 0 thermal photons (52 soft modes suffice) plus
  the even flux tower e = 2j. Flux half: Model G, p = 1/2 - 1.4e-10 at the seed box, and
  lambda_odd <= L_1/N at every size (row 930 G2, G4, PROVED unchecked); carrier = the k = 0
  toron Phi_1 alone (photons drop out exactly, Lemma G1).
- FT-FROZEN (frozen Q_8 and 2T must FAIL the form at large finite beta). Glue: S_ev >= 1/2
  (check 896 D6, through check 921 12.2; two inequivalent even flat vectors). Flux: p = 10/23
  and 30/61 at beta = infinity, the twist absorbed at zero action, heat-bath response 0 and
  gap 0 (row 930 F1, F2, PROVED unchecked).
- FT-CEIL (the form's inputs must not be statements the checked ceilings refute or cap):
  worst-case single-link criteria stop at 1/3; no weighted single-site Dobrushin passes 2/3;
  vertex blocks with worst-case single-link responses fail at 0.775; background-uniform layer
  twist bounds are false above 4 G_3 = 1.0109 (rows 834-841, 849, 857); environment-uniform
  conditional parity bounds are false (Z_2 Peierls, beta > 2.191, check 870); literal annealed
  (AN1) is the worst case (check 852); clustering cannot give the flux half (check 882).
- FT-Z2 (standing side test from the same rows): frozen Z_2 passes the glue half
  (S_ev -> 0 on a fixed box) and fails the flux half (p = 1/2).

What the two new U(1) tests add (my reading, to be used in Step 3):
(a) the two halves have DIFFERENT U(1) carriers (photons k != 0 for glue; the toron k = 0 for
flux), so no single-mode statement can be the crux of the whole seed;
(b) every form in rows 929-930 dies in all three rivals at one factor of the same kind: a
count of soft or degenerate states (the even count sum_i r_i^t for glue; the odd Poincare
constant lambda_odd for flux); response-type factors ((FR), the seam Delta at the endpoint)
are NOT selective: frozen groups and large U(1) boxes pass them.

### Step 1b (2026-11-14T05:25Z): FINISH rows 913-928 read (RESULT parts; READ)

Forms added after the 912 consolidation, with the check verdict that binds each:

- Transport of the full thermal trace along the Wilson coupling (row 913; check 914): Lemma F,
  Lemma KF, Identity 6.4 HOLD; Theorem ABS HOLDS AFTER CORRECTION; it stops at the vacuum
  subtraction (VAC-SUB) (row 934, running on worker 1; NOT mine to attack).
- (ONE-K)/(UNIV-K) (rows 916, 917, 924, 925): links (c), (e) of the chain are checked; (UNIV-K)
  OPEN. Cutoff uniformity is a separate open input and is not the subject of row 931.
- Margins (rows 918, 919): after check 919 only "hot boxes have NO ROOM" survives as GUIDE; the
  cold seed size, (CORE) room and transport are UNMEASURED. So no size a is known for the seed.
- (SEAM) and (INS) (rows 920, 921, 929): the glue half's insertion identity is checked; the
  seam form is bracketed by thermal sums (row 929, unchecked).
- (FR), lambda_odd, Theorem R, Lemma CUT, (CUT-TYP) (rows 922, 927, 930): row 930 unchecked.
- THERM-DI-pin (rows 923, 926): OPEN; low-h statements assume confinement.
- Reading rows 915, 928: no published supplier for either form (bounded searches).

Step 1 is complete. Step 2 (overlap check) next.
