# T33 pre-registration (written BEFORE any T33 script was run; Claude Sonnet 5.5, same family as supervisor)

Wall T33 = {L06-W5, L16-W5, L06-W14}: the weak/hypercharge couplings (g_2^2 = 1/4, g_Y^2 = 1/5 by "dimension counting"),
sin^2(theta_W) = 4/9 bare, alpha_em and the unit charge are not derived.

## What I already know from reading (so the tests are not repeats)
- T28 (W/attacks/T28.md, T28_scratch/testA_output.txt) already ran the lane's suggested test: the exact SU(2) Wilson unit point
  is beta = 3.9-4.4, not the weak anchor's 16. So "same tick law" gives g_2^2 ~ 1, not 1/4. Not repeated here.
- The lane's chains use DIFFERENT transport rules: SU(3): alpha_s(v) = alpha_bare/u0^2 with NO running (ALPHA_S_CMT note :12-16);
  SU(2): 1/alpha_2(v) = 16 pi u0^2 - (b_2/2pi) L with full SM 1-loop running (G_2_V note (R1)).
- Hand estimate (unrun): SM extrapolation to M_Pl puts g_3^2, g_2^2, g'^2 all near 1/4 (0.24, 0.25, 0.23).

## Common inputs (comparators only; SM content only, no tastes; MS-bar)
M_Z = 91.1876; 1/alpha_em(M_Z) = 127.951; sin^2 theta_W(M_Z) = 0.23122; alpha_s(M_Z) = 0.1179; M_Pl = 1.2209e19 GeV;
v = 246.28 GeV (framework's v_cand; L = ln(M_Pl/v) = 38.4422). SM RGE: 2-loop gauge + 1-loop y_t (Machacek-Vaughn coefficients).

## TEST A: what lattice-scale couplings does the SM data ask for? (script t33_A_targets.py)
Report 1/alpha_3, 1/alpha_2, 1/alpha_Y (SM Y normalisation, Q = T3 + Y/2) at M_Pl, 1-loop and 2-loop.
PASS (near-universal reading): g_3^2, g_2^2, g_Y^2 at M_Pl agree with spread (max-min)/mean <= 0.15 (2-loop).
FAIL: spread > 0.25.   Guess: PASS (spread ~ 0.12).
If PASS, the lane's triple (g_3^2, g_2^2, g_Y^2) = (1, 1/4, 1/5) is not what SM-type running asks for in the SU(3) slot (4x off).

## TEST B: is the lane's triple consistent under ONE transport rule? (t33_B_transport.py)
Rules: R-map (coupling at v = tadpole-improved bare, no running; the SU(3)/CMT rule), R-run (SM 1-loop from tadpole-improved bare
over L = 38.44; the SU(2) rule). Inputs u0(SU(3)) = 0.5934^(1/4); u0(SU(2), beta = 16) in {0.9761 lane single-plaquette, 0.988 weak comparator};
u0(U(1)) = 1 (upper bound on the tadpole shift). Observed g_i(v) from SM running M_Z -> v.
PASS (lane triple jointly consistent): some single rule puts g_3(v), g_2(v), g_Y(v) all within 10% of observed.
FAIL: no single rule does.   Guess: FAIL (R-map: SU(2) -21%, U(1) +25% or worse; R-run: SU(3) Landau pole).

## TEST C: routes to the pair (g_2^2, g_Y^2) and a trial factor (t33_C_routes.py)
Candidate lattice pairs run DOWN M_Pl -> M_Z (g_3 and y_t initial values at M_Pl taken from the SM upward run):
  (c1) counting pair (1/4, 1/5); (c2) Pati-Salam relation route: SU(4) x SU(2)_L x SU(2)_R with g_4^2 = 1 (the lane's g_3^2),
  g_L^2 = g_R^2 = 1/4, so 1/g_Y^2 = 1/g_R^2 + (2/3)/g_4^2 = 14/3, g_Y^2 = 3/14 (B-L on the lane's left-handed surface = its Y);
  (c3) fully unified SU(5)/PS with g^2 = 1/4 (sin^2 = 3/8);  (c4) universal g^2 = 1/4 for both.
Metrics: relative error of sin^2 theta_W(M_Z) and 1/alpha_em(M_Z) against the comparators.
PASS for a pair (route survives as 'wounded', not dead): BOTH errors <= 3% (sin^2) and <= 5% (1/alpha_em).
FAIL: either larger.   Guess: (c1) FAIL on 1/alpha_em (~6%), sin^2 ~3.5%; (c2) PASS; (c3) FAIL (sin^2 ~ 0.21).
Trial factor: family F = {(1/n, 1/m): n, m = 1..12} (144 pairs; covers d+k, N_pair^2, N_quark-1, dim H readings).
  Count pairs at least as good as (c1) in both errors; and Monte-Carlo the base rate that a random log-uniform (g_2^2, g_Y^2) in [0.1,0.5]^2
  falls in (c1)'s error box, giving the expected number of chance hits in F.
Reading rule: if expected chance hits in F >= 0.5, the (1/4, 1/5) match carries < 1 bit and is not evidence for the counting rule.

## TEST D: 'alpha_G is 40x too big' (t33_D_insensitivity.py)
Toy: a U(1) with unit-charge coupling alpha_G at M_Pl (ring model: 0.28-0.37; comparator: 1/(20 pi)) and the SM charged fermions
(sum N_c Q^2 = 8 per three generations, thresholds at the fermion masses) screening it down to M_Z; also 1-loop SM for the (g_2, g_Y) pair.
PASS (the '40x' is a category error): for alpha_G in [0.28, 0.37] the IR 1/alpha_em(M_Z) is within a factor 3 of 127.95 (i.e. >= 43),
and the IR value varies by less than a factor 2 over alpha_G^-1 in [3, 63].   FAIL otherwise.   Guess: PASS (1/alpha ~ 69 vs 128).

## Outcome logic (fixed before running)
- STANDS or PRICED if no route passes; PRICED only if I can name the premise set that reproduces the lane's numbers exactly.
- MISFRAMED if Tests A and D pass AND B fails: the wall bundles a transport-rule question and a one-number question under 'three values'.

## Deviations recorded after running (honesty log)
- Test A: PASS as guessed (2-loop spread 11.5%).  Test B: FAIL as guessed for every single rule; the lane's actual mixed use is within 3.6%.
- Test C: counting pair FAIL on 1/alpha_em (+6.9%; sin^2 -3.0% sits at the bound); Pati-Salam pair PASS (+0.1%, +3.6%).
  The Pati-Salam idea was formed AFTER the hand estimate of the target region (Test A), so it is a post hoc fit, not a confirmation.
  A first draft of t33_E swapped the argument order of down_from_mpl (gave sin^2 = 0.0013 for the SU(4)-only case); fixed, rerun.
  The first Monte Carlo in t33_C (40,000 ODE solves) timed out; replaced by a vectorised 1-loop estimate (boxes recomputed at 1 loop for consistency).
- Test D: pre-registered as one PASS/FAIL; result is split. Screening-only toy passes (IR 1/alpha about 70, spread 1.86x); full SM sum fails (IR about 26, spread 3.3x).
  Also found: the 'category error' guess for the raw 40x was wrong in spirit: the UV coupling the data need is 17-39x below the ring model's, so the wall is real for the ring model.
- Test F (added after reading the historic intake): replication matches the note's four numbers to 4-5 digits; it is a two-knob fit.
- Outcome logic: MISFRAMED required A and D to pass and B to fail; D was split, so I record MISFRAMED with that qualification
  (the reframing rests on A, B and the convention argument, not on D).
