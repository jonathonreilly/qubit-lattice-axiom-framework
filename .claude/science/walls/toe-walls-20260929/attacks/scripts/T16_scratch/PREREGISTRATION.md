# T16 pre-registration (written before any script was run)

Attacker: Claude Sonnet 5.5 (same family as supervisor). Same-family checks.
Wall T16 = L01-W6 + L04-W10 + L13-W5: "the arrow of time needs a low-record past".

## Working reading being tested (MISFRAMED candidate)

The wall bundles four things: (i) the direction of the record-inclusion order
(axiom-level: permanence), (ii) a first/blank state, (iii) alignment of matter's
entropy with that order, (iv) L13-W5's homogeneity/horizon clause. I expect (i) and (ii)
to need no supplied low-entropy state, (iii) to be the T03 coupling fork, and (iv) to
be a separate wall.

## Test 1 (t1_june_toy_audit.py): is the wall's own evidence a property of the axiom's record?

System: the June 2026-06-05 toy (1 pointer qubit + 5 fragments, H_k = (pi/2) P1 (x) X_k).
- 1a. Reproduce the reported R_red: forward from low-record [0,1,2,3,4,5]; reversed
  high-record [5,..,0]; GHZ [5,..,0]; I/d flat.
- 1b. Apply the SAME generators a second pass (k=0..4 again) after the forward run.
- 1c. Fraction of random product starts (pointer + 5 fragments each random pure) for which
  one pass raises / lowers / leaves R_red.
Pass reading (route "toy record is not the axiom's record"): 1a reproduces AND 1b takes
R_red from 5 back to 0 (records erased by the toy's own forward map; not permanent).
Fail reading: 1b leaves R_red = 5. Then the toy's reversal is genuine start dependence of a
permanent-looking functional, and my "misstated evidence" claim dies.

## Test 2 (t2_symmetric_start.py): is the blank state the unique symmetric one, and can a
deterministic covariant law leave it?

Finite model: ring of 6 sites, possibility menu = 6 octahedron vertices (pure possibilities),
group G = translations x reflection x octahedral rotations acting on the menu (order 6*2*24 = 288).
Configurations: each site empty or one possibility (7^6 = 117649).
- 2a. Number of configurations fixed by all of G. Predict 1 (empty).
- 2b. Add one invariant possibility ("centre", the I/2-like point). Predict exactly 2 fixed
  configurations (empty, all-centre).
- 2c. Stabiliser order is non-increasing along every single-birth edge; count strict drops.
  Predict 0 violations.
- 2d. Deterministic covariant closure from empty for count-threshold rules A subset {0,1,2}:
  synchronous update gives empty or full in ONE step; sequential site-order update is not
  translation covariant. Predict: no rule gives a partial configuration from empty.
Pass reading (Curie route: blank = unique symmetric point, arrow needs a stochastic order): 2a-2d all as predicted.
Fail reading: a non-empty fixed configuration for the pure menu, or any stabiliser increase
along a birth, or a covariant deterministic rule that gives a partial invariant configuration.

## Test 3 (t3_growth_homogeneity.py): does a symmetric start buy L13-W5's homogeneity?

2D torus 96x96, growth with rate lam0 + lam1*k (k recorded neighbours), lock content s=+-1 with
NN bias. Starts: (a) empty + uniform nucleation, (b) 4 seeds, no nucleation, (c) Bernoulli 5e-4.
Stop at mean density 0.3. Observables: block-density variance (block 24) normalised to binomial;
content correlation C(r) versus twice the front distance.
Pass reading (homogeneity is free only from the symmetric ensemble, and superhorizon content
correlation is exactly zero, so the horizon clause is NOT solved): (a) and (c) within 1.6x
binomial, (b) more than 5x; C(r) consistent with 0 (|C| < 3 sigma) for r beyond twice the
front distance.
Fail reading: (a) also inhomogeneous (>3x) or a superhorizon correlation.

## Test 4 (t4_coupling_census.py): which physical arrow is free, and under which coupling?

8-qubit chain, H = sum (XX+YY+0.5ZZ) + 0.7 sum (-1)^i Z + 0.3 sum Z_i Z_{i+2}.
Starts: ground state, Neel, Haar random, time-reversed evolved Neel.
Branches: passive records (wave untouched, record value sampled from the z-marginal) and
active locks (projective z-lock, site frozen).  6 record births at unit spacing.
Observables: count n, half-chain entanglement entropy S, energy <H_orig>.
Predictions: count rises in all 8 cases. Passive: dS > 0 for Neel, ~0 for Haar, exactly 0
(and dE = 0) for ground, < 0 for reversed: alignment with count depends on the start.
Active: ground-state dE > 0.5 (heating); dS for Haar < 0 (purification).
Pass reading (the free arrow needs the wave to be acted on by records, i.e. T03 horn 1; passive keeps the wall): as predicted.
Fail reading: passive ground state changes, or active ground dE ~ 0, or passive reversed dS >= 0.

## Amendments made after seeing run 1 (recorded honestly; each is post hoc)

- Test 2c FAILED as pre-registered: the stabiliser of a configuration as a SET is not monotone
  along births (a second record can raise the set symmetry, e.g. records at sites 0 and 3 of the
  6-ring). The "arrow = monotone loss of symmetry" Lyapunov claim is dead. Only the internal
  pointwise stabiliser is monotone (2c'), and it saturates after two non-collinear records.
- Test 3 normalisation (1.6x binomial) was mis-specified: a growth ensemble has a finite
  correlation area. Run 1 (L=192) gave plateau ratio S48/S12 = 2.80 / 1.66 / 8.00 for
  nucleation / Bernoulli / 4 seeds, not yet plateaued at b=48. Amended criterion (chosen after
  run 1): L=384, plateau ratio S(96)/S(24) < 2 for (a),(c) and > 4 for (b).
- Test 4 run 1 (tau = 1, 6 births, window 6) FAILED "passive reversed dS < 0": the Neel entropy
  saturates by t ~ 2, so a window of 6 is beyond the echo. Re-run with tau = 0.3, Trev = 1.8
  (window 1.8, inside the relaxation time). New prediction added before the re-run, from the
  run-1 energies: in the ACTIVE branch <E> moves toward the spectrum mean (E = 0) from both
  sides, i.e. sign(dE) = -sign(E_start) for |E_start| > 1.5; test 4b checks this on nine
  microcanonical-window starts with E_start from -10 to +8. Passive dE = 0 exactly.
