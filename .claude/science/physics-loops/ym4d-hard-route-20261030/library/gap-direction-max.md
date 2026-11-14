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

### Step 2 (2026-11-14T06:20Z): overlap check (rule 0a) for what this file attacks

Named open lemmas already owned by a row; I do NOT attack them: (CUT-TYP), (LSI-weak), averaged
(FORCE-COV) (row 930); (SEAM), (SEAM-L1), (XM) (row 929); (VAC-SUB), (VIR-log), (DEF_K) (rows 708,
913, 934, running); (JOIN-TH) (rows 907-911); EXC, (DRESS) (rows 872-890); (KURT), (WALL)_40 (rows
886-897); (S1), (SEED-DEC) (row 887); EXIT (rows 846-877); (UNIV-K) (rows 916-925); THERM-DI
(rows 905, 923); (Z0)+(COUNT) (row 895).

What this file states and attacks instead (Steps 4-6): a time-rate form of the full thermal free
energy at ONE coupling, (RATE)/(ANOM), and a gap/entropy comparison for the vacuum slice chain.
Greps at the pinned commit: `library/open-core.md` has 0 hits for "equation of state",
"interaction measure", "log-Sobolev|LSI|hypercontract", "Nash", "FE-CONTRACT", "Massieu". FINISH
has no row whose target is a rate in the time extent at fixed coupling. Nearest prior lane text,
credited and not repeated:
- `library/gap-phys-seed.md:195, 224` (Q4): the dimensionless thermal pressure pi(a) = a^4 p(1/a)
  with a step form pi(2a) <= sigma(pi(a)); it notes that the non-strict form is the sign of the
  interaction measure and that U(1) passes the non-strict form.
- `library/gap-mid-max.md` (row 708): transport along the COUPLING, (VIR_K): the beta-derivative of
  G = log(1 + S) against K t times its t-derivative; lines 184, 344 say that the continuum trace
  anomaly "has no lattice form". Row 913 ranks that transport first; row 934 holds its stop.
- `library/gap-brainstorm2-max.md:259` (G4): "(ES) is a low-temperature equation of state".
- `library/gap-thermpin-check-astra.md:170-178`: X'' is the thermal variance of E.
- Row 930's (LSI-weak) is a weak constant (C L_1/N) for the two-slice even law, used group-blind.
Verdict: no row owns the time-rate form or the vacuum-chain comparison below. I proceed, and I
keep off every lemma in the first list.

### Step 3 (2026-11-14T06:25Z): the candidate forms against the fact tests

Columns: U1 = "false for U(1) Coulomb (Gaussian model)"; FRZ = "false for frozen Q_8, 2T";
CEIL = "none of its hypotheses is a statement the checked ceilings refute". A crux form must
have YES in all three. "Stronger" means: implies the target half, no converse known.

| # | Form (half) | U1 | FRZ | CEIL | Verdict |
|---|---|---|---|---|---|
| 1 | (GLUE-FP): S_ev(a; (24a)^3) <= 1/10 (glue; the consumer's own statement) | YES: log(1+S_ev) > 31 (929 A2) | YES: S_ev >= 1/2 (896 D6) | YES | passes; weakest for glue by definition |
| 2 | (CORE): Q_0 <= 1/20 on (a, b, b, b), b >= 24a (flux; the consumer's own statement) | YES: p -> 1/2 (930 G2) | YES: p = 10/23, 30/61 (930 F1) | YES | passes; weakest for flux by definition |
| 3 | signed theta-average of Delta <= psi_* (glue) | as 1 | as 1 | YES | passes; EQUIVALENT to 1 by (INS) |
| 4 | (SEAM-L1), (SEAM) sup form (glue) | YES at every size (929) | YES | YES | pass; stronger than 1 (sup/average grows like a in U(1)) |
| 5 | endpoint Delta_0 <= psi_* alone (glue) | NO for a > 4.8e4 (929 item 3) | - | - | FAILS U1; also not sufficient |
| 6 | (Z0) + (COUNT) (glue, Lemma G5) | YES, at (Z0) (gap times a is scale-free and small); (COUNT) alone is passed by U(1) (ARGUED: a scale-free hot box has bounded free energy) | YES at (Z0) | YES | passes as a pair; (COUNT) alone is not selective; stronger than 1 |
| 7 | Proposition Q hypothesis S_ev(2n)(1 + X(k)) <= (psi_*/9)^2 (glue) | YES | YES | YES | passes; far stronger than 1 |
| 8 | (I1)-(I3) in local sup form (glue) | - | - | NO at 2.3 (worst-case local criteria) | not needed (929 Q1), capped |
| 9 | (FR) alone (flux) | NO for boxes above about 420 (930) | NO: response 0 (930 F2) | YES | FAILS U1 and FRZ: not a crux |
| 10 | p <= FR/(2 lambda_odd) (flux) | YES through lambda_odd | YES through the gap | YES | passes; stronger than 2; empty in U(1) at step (b) |
| 11 | Theorem R inputs: (ODD-GAP)_s + (FORCE-COV)_s, sup form (flux) | YES | YES | NO: sup form false in U(1), not volume-free | FAILS CEIL in sup form |
| 12 | Theorem R inputs with AVERAGED force covariance (flux) | YES | YES | YES | passes; stronger than 2 |
| 13 | (CUT-TYP) + (LSI-weak) (flux, supplies (ODD-GAP)) | YES: no good environment | YES: gap 0 | YES (typical, not sup) | passes; stronger than 12 |
| 14 | (KURT)_eta or (WALL)_40 with GLUE (flux) | only through GLUE: U(1) has kappa = 3/2 exactly in 2D and >= 3/2 by symmetry (checks 889, 897) | only through GLUE: Q_8 has kappa = 4 in 2D (check 897) | YES | the flux-side factor is NOT selective; all selectivity sits in GLUE at 160^(-16) |
| 15 | (E17), HA, (C2), EXC, (DRESS), (S1) (flux) | YES | YES | HA: NO in background-uniform form (check 870); others YES | pass (HA only off the uniform form); all ask a rate or area law, stronger than 2 |
| 16 | (VIR-log) / (VAC-SUB) transport along beta (both halves) | YES across the transition (708) | YES | YES | passes; a path statement, stronger than the seed at beta_1; owned by rows 913, 934 |
| 17 | free-wall engine: (JOIN-TH) + seed on a cold box (both) | only through its seed | (JOIN-TH) is satisfied by frozen groups (910, ARGUED) | YES | the doubling factor is not selective; its seed is forms 1-2 again |
| 18 | (SEED-Delta), (SEED-L), (CAS) (both; torus against pressure) | YES | YES | YES | pass; equivalent family to the seed (rows 697-708, 837) |
| 19 | (ANOM), Step 4 below (both; one identity) | YES | YES | YES | passes; EQUIVALENT to the SH seed |

Findings of the table (the answer to the row's question, part 1).

- F1. A form passes all three tests only if it carries a spectral factor of the slice transfer
  operator on the seed box: the even count (forms 1, 3, 4, 6, 7), the odd gap (10, 12, 13), or the
  full trace (16, 18, 19). Every factor of response type fails a test or is not selective:
  (FR) (9), the endpoint Delta_0 (5), sup force covariance (11), (COUNT) alone (6), the kurtosis
  factor (14), the doubling factor (17).
- F2. **The weakest form that passes all fact tests is the split seed itself**: (GLUE-FP) and
  (CORE) on one box (forms 1, 2; Lemma SPLIT, rows 892, 893). No form on the table is strictly
  weaker than these and still sufficient; every other passing form is equivalent (3, 18, 19) or
  stronger. So the two U(1) tests do not single out a weaker target. They sort the forms.
- F3. No form fails ALL tests for a structural reason that would close the route: the plain
  statement "no form passes" is FALSE. But the passing forms carry no handle that the seed lacks.
- F4. The halves differ in the STRENGTH of what they need (new reading, used in Step 4): the flux
  half is the variance of ONE bounded odd function (p/(1 - p) = Var(R_t), |R_t| < 1), so a
  Poincare-type (variance) contraction suffices and no count enters (930 Theorem R, V_1 <= 1).
  The glue half is a trace: S_ev(a) is the mean over the starting slice of a chi-square distance
  that is exp(extensive) after one step (Step 5, (5.3)). A per-step variance contraction then
  needs a time of the order of the volume. So the glue half needs a contraction at the level of
  entropy (a count), not of variance. This is the asymmetry behind "two U(1) carriers".
