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

### Step 4 (2026-11-14T06:45Z): the form, exactly; the SU(2) property; where U(1) breaks

Notation. B a periodic spatial box, |B| its number of sites; T = T_B(beta) the gauge-invariant
Wilson transfer operator (all flux sectors), eigenvalues lambda_0 > lambda_1 >= ..., r_i =
lambda_i/lambda_0 = e^(-E_i). S(t; B) = sum over i >= 1 of r_i^t (real t >= 1),
X(t; B) := log(1 + S(t; B)), U(t; B) := -dX/dt = sum_i E_i r_i^t/(1 + S). Credit: the transfer
frame is the Sussman-Alpoge account's (GL8, as read by rows 920-930); Lemma SPLIT and Theorem SH
are rows 892, 707; the pressure reading is `gap-phys-seed.md` Q4.

**Form W (the weakest form that passes all fact tests; rows 892, 893; READ).** There is an
integer a >= 1 with, on the one box (a; (24a)^3) at the first-passage data of (SEED-FP):
(W-glue) S_ev(a; (24a)^3) <= 1/10 and (W-flux) Q_0 <= 1/20. By Lemma SPLIT then
X(a; (24a)^3) <= x_* := log(22/17) (= 0.2578), and this is the Theorem SH seed shape. For the
order-one question of this row the data are the bare Wilson weight at one beta in 2.3 to 2.6;
cutoff uniformity ((UNIV-K), rows 916-925) is a separate open input.

**The same form as one identity (PROVED; calculus on the spectrum).** Put
kappa_B(t) := t U(t; B)/X(t; B) and pi_B(t) := t^3 X(t; B)/|B|. For 1 < t_0 < t_1:

  (ANOM)  log pi_B(t_1) = log pi_B(t_0) - integral over [t_0, t_1] of (kappa_B(t) - 3) dt/t.

So with B = (24 t_1)^3: X(t_1; B) <= x_* holds if and only if
  integral over [t_0, t_1] of (kappa_B(t) - 3) dt/t >= log pi_B(t_0) + log(24^3/x_*)
  = log pi_B(t_0) + 10.89.
Proof. X is smooth and positive on t > 1 (sum_i E_i r_i^t <= sum_i r_i/(e (t - 1)), T trace
class), d log X/dt = -U/X, and d log(t^3)/dt = 3/t. log(13824/0.2578) = 10.89. QED
Reading (thermodynamic dictionary, ARGUED): X/|B| is p/T and U/|B| is the energy density at
T = 1/t, so kappa = eps/p and kappa - 3 = (eps - 3p)/p, the interaction measure over the
pressure. The seed is: the relative interaction measure, integrated over log t on the seed
box, exceeds a fixed number.

**Lemma HOT (PROVED, crude).** X(1; B) <= 12 beta |B|, so pi_B(1) <= 12 beta; and
e^(-12 beta |B|) <= Omega <= e^(12 beta |B|); and the one-step vacuum-chain density (Step 5)
has log p_1 <= 36 beta |B|.
Proof. With normalized Haar and |x_p| <= 1 over 3|B| space and 3|B| time plaquettes:
e^(-6 beta |B|) <= T(u, w) <= e^(6 beta |B|). Tr T <= sup T(u, u); lambda_0 >= <1, T 1>. Omega =
T Omega/lambda_0 gives sup Omega/inf Omega <= e^(12 beta |B|), and ||Omega||_2 = 1. QED
With t_0 -> 1: the seed at beta = 2.3 follows from an integrated relative interaction measure
of log(27.6) + 10.89 = 14.21 on the seed box (14.33 at beta = 2.6). This is the whole seed,
both halves, as one order-one number.

**Lemma TENS (PROVED).** If T = T_1 x T_2 (tensor product) then X = X_1 + X_2 and U = U_1 + U_2.
So a rate bound (RATE)_mu: U(t) >= mu X(t) on a window, passes from the factors to the product
with the same mu. The seed threshold S <= s does not (1 + S multiplies), and a gap bound does
not control X. (RATE) is the form of "gap and count" that tensorizes.
**Lemma GAPRATE (PROVED).** For every T: U/X >= E_1 (1 - e^(-X))/X >= E_1 (1 - X/2).
Proof. U >= E_1 S/(1 + S) and X = log(1 + S); (1 - e^(-x))/x >= 1 - x/2. QED
So a gap alone gives (RATE) only where X <= 1 (a cold box). The content of the seed is (RATE)
where X is extensive: from the hot bound X <= 12 beta |B| down to X of order one, in a time of
order log |B|.

**Fact tests of (ANOM) and (RATE).**
- U(1), Gaussian model FP of row 929 (PROVED given 929 Theorem A2): X(a; (24a)^3) > 31 at
  every a and beta, so the seed fails by a factor above 31/x_* = 120, and the integral in (ANOM)
  falls short by more than log 120 = 4.78 for every window. Per mode (PROVED from 929 Theorem A1):
  X_k = -2 log(1 - e^(-t omega_k)), U_k = 2 omega_k/(e^(t omega_k) - 1), and t U_k <= (1 + t omega_k) X_k.
  The mechanism (ARGUED, continuum limit): X = (pi^2/45)|B|/t^3 depends on t/b only, so
  kappa = 3 exactly: the integrand of (ANOM) is zero. The photon breaks the seed at the exact
  scale covariance of the Gaussian fixed point. The same holds for the toron tower: its part of
  X depends on t/(beta b) only (929 Lemma F), and at b = 24a it is 3 log(sum_e e^(-e^2/(48 beta))),
  about 3 log(sqrt(48 pi beta)) = 8.8 at beta = 2.3 (ARGUED: Gaussian sum), again scale-free.
- Frozen Q_8, 2T (PROVED given check 896 D6): S_ev >= 1/2 on a fixed box at large finite beta,
  so X >= log(3/2) > x_*. Mechanism (ARGUED): degenerate flat states have E_i -> 0, so U -> 0 and
  kappa -> 0: the integrand of (ANOM) tends to -3.
- Ceilings: (ANOM) and (RATE) quantify over no background and no exterior. YES.
So the rivals fail at opposite ends of one inequality: U(1) by kappa = 3 (scale covariance),
the frozen groups by kappa = 0 (degeneracy).

**The SU(2) property that must enter.** Among the three groups, SU(2) is the one that is
connected AND has a finite centre (compact semisimple). Both parts are needed.
- Connected: every link carries Lie-algebra directions, so the slice laws carry a Dirichlet
  form and Haar has no atoms. Q_8 and 2T fail here: no gradient, degenerate flat sectors,
  heat-bath response 0 and gap 0 (930 F1, F2).
- Finite centre, that is, no abelian factor: no one-parameter group commutes with a generic
  pair of link variables ("an element commuting with two non-commuting elements of SU(2) is
  central", 930 Section 6.2). U(1) fails here: its centre is the whole group, so the 1-form
  symmetry acting on a slice is continuous. Its k = 0 orbit is the toron (flux half, 930 G1-G4)
  and its k != 0 Goldstone modes are the photons (glue half, 929 A1-A2). One object carries both
  U(1) failures; the two halves see different momenta of it.
- **The step where U(1) breaks, in one place**: any step that bounds below a Dirichlet-form
  constant (Poincare for the flux half, entropy-type for the glue half, by F4) of a slice law on
  functions that vary along the 1-form symmetry orbit. For U(1) the orbit is an exact symmetry of
  every conditional law, with |grad|^2 of order (length)/(cross-section) for k = 0 and of order
  |k|^2 per mode for k != 0, so every such constant tends to 0 with the box. For SU(2) the orbit
  is the two points +-1. This is necessary, not sufficient: Q_8 has the same two-point orbit.

### Step 5 (2026-11-14T07:05Z): proof attempt on the hardest lemma, stage 1 (variance level)

The hardest lemma of Form W is the count in the glue half (F4): bring X from extensive to
order one in a time of order log |B|. The attempt works on the vacuum slice chain, at one
coupling, with no supremum over backgrounds in the statements that are proved.

Setting (READ: row 863 I1 through row 929 Section 6.1). nu = Omega^2 dU on slice
configurations; P = Omega^(-1) (T/lambda_0) Omega, a self-adjoint Markov operator on L^2(nu) with
eigenvalues r_i on gauge-invariant functions. One-step law pi_u(dw) = T(u, w) Omega(w) dw/(lambda_0
Omega(u)). p_s(u, v) = sum_i r_i^s phi_i(u) phi_i(v) is the density of P^s(u, .) with respect to nu.
grad_u is the gradient over the 3|B| links of u (unit S^3 metric per link).
G(u, w) := grad_u log T(u, w) (the one-step score; its part from V(u) does not depend on w).
Gamma(u) := the largest eigenvalue of the covariance matrix of G(u, .) under pi_u;
Gamma^* := ess sup over u. gamma := the Poincare constant of nu: Var_nu(h) <= E_nu|grad h|^2/gamma
for smooth gauge-invariant h.

(5.1) (PROVED) grad_u (P f)(u) = Cov_(pi_u)(G(u, .), f), for bounded gauge-invariant f.
Proof. (P f)(u) is the integral of pi_u(w) f(w) dw; grad_u log pi_u(w) = G(u, w) - grad log Omega(u),
and its pi_u-mean is grad_u of the constant 1. QED
(5.2) (PROVED) E_nu[ Var_(pi_u)(f) ] = ||f||^2 - ||P f||^2 (stationarity of nu).
(5.3) (PROVED) 1 + S(2s; B) = E_(u ~ nu) ||p_s(u, .)||^2 in L^2(nu). So S(2s) is the mean over the
starting slice of the chi-square distance of P^s(u, .) from nu, and it is the chi-square mutual
information of two slices at lag s in the vacuum chain (as in row 839, check 849).

**Theorem V (gap comparison for the vacuum chain; PROVED, group-blind; not yet checked).**
For gauge-invariant f with E_nu f = 0:
  ||P f||^2 <= E_nu[ Gamma(u) Var_(pi_u)(f) ]/gamma <= Theta (||f||^2 - ||P f||^2),  Theta := Gamma^*/gamma.
Hence ||P f||^2 <= (Theta/(1 + Theta)) ||f||^2, r_i^2 <= Theta/(1 + Theta) for every i >= 1 (all
sectors), and E_1 >= (1/2) log(1 + gamma/Gamma^*).
Proof. By (5.1) and Cauchy-Schwarz over unit tangent vectors z: |grad P f(u)|^2 = sup_z
Cov(z.G, f)^2 <= Gamma(u) Var_(pi_u)(f). P f is smooth, gauge invariant and nu-centred; apply the
Poincare inequality, then (5.2). QED
Kill test by hand (PROVED): one photon mode of FP (929 Section 3.1). pi_q is Gaussian in q' with
precision beta e^omega and mean e^(-omega) q; G = beta q' + const, so Gamma = beta e^(-omega);
nu = exp(-beta sigma q^2), so gamma = 2 beta sigma. Theta/(1 + Theta) = e^(-omega)/(2 sigma + e^(-omega))
= e^(-2 omega) = r_1^2. **Theorem V is an equality for the free photon, mode by mode.**
Reading. (i) Theorem V is the Euclidean, discrete-time form of the ground-state representation:
in the Hamiltonian limit the generator of P is a multiple of the Langevin generator of nu, and
gamma is the mass gap up to that multiple (ARGUED, classical). (ii) It is row 930's Theorem R
mechanism (covariance of a force with a martingale increment, a Poincare inequality, a
telescoping identity), moved from the even ring laws w_e^(s) to the stationary chain; credit
row 930. (iii) The force factor is NOT where U(1) fails here: on the photon modes of FP, Gamma <= beta
at every size (max over modes of beta e^(-omega); the toron factor is not computed here). In row 930 the sup force covariance failed in U(1) because
the slab was conditioned at both ends (the barrier top); the one-step law pi_u is conditioned at
one end only. U(1) fails Theorem V's hypothesis at gamma alone: gamma <= 2 beta sinh(omega_min),
about 4 pi beta/b, and the toron direction has gamma <= L_1/N. (iv) Theorem V gives a gap, not a
count: iterating it on (5.3) gives S(2s) <= (Theta/(1 + Theta))^(s-1) S(2), and S(2) is
exp(extensive). This is F4 in a formula.

**Proposition HC (PROVED implication; the count from hypercontractivity).** Assume
  (HC-vac)_alpha: for every integer m >= 0, ||P^m h||_2 <= ||h||_(q'), q' = 1 + e^(-2 alpha m),
  norms in L^p(nu), h gauge invariant.
Then X(2m + 2; B) <= 72 beta |B| e^(-2 alpha m) for every m >= 0, and E_1 >= alpha.
Proof. p_(m+1)(u, .) = P^m p_1(u, .). For a density g: ||g||_(q')^(q') = E[g g^(q'-1)] <=
(sup g)^(q'-1), so ||g||_(q') <= exp((q' - 1) log sup g). By Lemma HOT, log sup p_1 <= 36 beta |B|.
So ||p_(m+1)(u, .)||_2^2 <= exp(72 beta |B| e^(-2 alpha m)) for every u; average over u, (5.3).
For the gap: r_1^(2m+2) <= S(2m + 2) <= 2 X(2m + 2) once X <= 1; take m-th roots. QED
Consequences. (a) Seed size: X(a; (24a)^3) <= x_* as soon as alpha (a - 2) >= log(72 beta 24^3/x_*)
+ 3 log a (= 16.0 + 3 log a at beta = 2.3). Any box-uniform alpha > 0 gives the whole seed, both
halves, at a of order (16 + 3 log a)/alpha. (b) Fact tests (PROVED from E_1 >= alpha): FP has
E_1 = omega_min -> 0 and the toron level 1/(2 beta b) -> 0; frozen Q_8 and 2T have E_1 -> 0
on a fixed box (degenerate flat vectors, check 896 D6, ARGUED rate). So all rivals fail
(HC-vac) with a box-uniform alpha. (c) By duality (HC-vac) is ||P^m||_(2 -> q) <= 1 with
q = 1 + e^(2 alpha m), Nelson's and Gross's exponent. In the Hamiltonian limit Gross's theorem
(classical, RECALLED, not rebuilt) makes it equivalent to a log-Sobolev inequality for nu.

### Step 6 (2026-11-14T07:20Z): proof attempt, stage 2 (entropy level), and the exact stop

Inputs, named.
  (LSI-vac)_alpha: Ent_nu(h) <= E_nu[ |grad h|^2/h ]/(2 alpha) for smooth gauge-invariant densities h.
  (SG-step)_sigma: for almost every u and every unit tangent vector z at u, z.G(u, .) is
  sub-Gaussian under pi_u with variance proxy sigma^2 (E e^(lambda (phi - E phi)) <= e^(lambda^2 sigma^2/2)).

**Theorem E (entropy contraction of the vacuum chain; PROVED GIVEN (LSI-vac), (SG-step); not
yet checked).** For every gauge-invariant density g with respect to nu:
  Ent_nu(P g) <= (Theta_H/(1 + Theta_H)) Ent_nu(g),  Theta_H := sigma^2/alpha.
Proof. (i) Chain rule and stationarity: E_nu[ Ent_(pi_u)(g) ] = Ent_nu(g) - Ent_nu(P g).
(ii) For a sigma^2-sub-Gaussian phi under pi and h >= 0 with pi-mean m > 0, the entropy
variational formula gives E_(h pi/m)[phi] - E_pi[phi] <= sqrt(2 sigma^2 Ent_pi(h)/m), so
Cov_pi(phi, h)^2 <= 2 sigma^2 m Ent_pi(h). (iii) With (5.1): |grad P g(u)|^2 <= 2 sigma^2 (P g)(u)
Ent_(pi_u)(g). Divide by P g, integrate, use (i): the Fisher information of P g is at most
2 sigma^2 (Ent_nu(g) - Ent_nu(P g)). (iv) (LSI-vac) for h = P g. QED
Corollary E1 (PROVED GIVEN the same). The mutual information of two slices at lag s in the
vacuum chain obeys I(U_0; U_s) <= rho^(s-1) 36 beta |B|, rho = Theta_H/(1 + Theta_H): it reaches
order one at s of order log |B|.
Check in one Gaussian mode (by hand): sigma^2 = Var(G) = beta e^(-omega), alpha = gamma = 2 beta sigma,
so rho = e^(-2 omega), the true entropy rate of that mode.

**Why this does not finish, exactly.** (PROVED) I(U_0; U_s) <= X(2s): for each u,
Ent(p_s(u, .)) <= log(1 + chi^2_u), then Jensen and (5.3). So Corollary E1 is on the necessary
side of the seed. The seed needs the chi-square (Renyi-2) information, and a small relative
entropy does not bound an L^2 norm. The step from Theorem E to (HC-vac) is the L^q form of
the same argument with a moving exponent. I did not close it: at fixed q > 1 the telescoping
gives a fixed per-step factor on a quantity that starts at exp(extensive), which is Theorem V
again; the gain of Proposition HC needs q to grow along the chain, and in discrete time the
Dirichlet form of P is not the gradient form of (LSI-vac). (RECALLED, not used: a strong
data-processing constant of a channel gives hypercontractivity only in the limit of large
exponents, Ahlswede and Gacs 1976.)

**The stop.** Open lemma (E-to-HC), group-blind: (LSI-vac)_alpha and (SG-step)_sigma imply
(HC-vac)_alpha' with alpha' = c(alpha, sigma) > 0. In the Hamiltonian limit this is Gross's
theorem with alpha' proportional to alpha. One attempt, one failure point (above). No row owns
this lemma (Step 2).

**Chain proved in Steps 4-6 (each arrow PROVED unless marked).**
  (LSI-vac) + (SG-step)  --Theorem E-->  entropy contraction  --(E-to-HC), OPEN-->  (HC-vac)
  --Proposition HC-->  X(2m + 2) <= 72 beta |B| e^(-2 alpha m)  -->  Form W at a ~ (16 + 3 log a)/alpha.
  gamma, Gamma^*  --Theorem V-->  E_1 >= (1/2) log(1 + gamma/Gamma^*)   (gap only, no count).
