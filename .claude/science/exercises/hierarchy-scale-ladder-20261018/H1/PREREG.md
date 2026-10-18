# HIER-1 pre-registration (written 2026-10-18 11:38Z, before any run)

Item: HIER-1 of `.claude/science/exercises/hierarchy-scale-ladder-20261018/TESTS.md`
(branch `origin/claude/hierarchy-scale-ladder-20261018`). Readings are FIXED as
in TESTS.md: HIER-DERIVED / HIER-REDUCED / HIER-NO-GO / OPEN.
Worker: Claude Opus 5.5 (test agent). Deadline 17:30Z (coordinator correction).

## Sources read before this file

- PR #9702 note (`origin/claude/scale-ladder-20261018:docs/SCALE_LADDER_..._NOTE_2026-10-18.md`), whole.
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, whole.
- `docs/HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md`, whole (T1, B1-B5, corrigenda).
- Prior art on main: regulator-dependence no-go (05-10), B4 determinant-only
  factor-signature no-go (06-17), DELTA0 open gate (05-30), taste-transfer-ladder
  probe (06-11), BBS taste-blocking no-go (05-10), dim-trans notation note (05-16),
  value-frontier probe (06-05), spatial-BC/u0-scaling note (04-13), g_bare
  convention notes, SPIN10 symmetric atomic gap note (09-14), native-Weyl canonical
  closure note (09-13, P12 "gamma arbitrary").
- Ladder campaign evidence: B14 FINDINGS (E2a: scalar mass drops out of {H_m,H_m}),
  B15 FINDINGS (Dirac mass drops out at endpoint-mean timing), B7 (interacting escape).

## Questions and planned work

(a) Is the exponent 16 a cross-rung invariant (survives every admissible
coarse-graining), so that alpha^16 is transported? Gate B4 through the ladder.
Candidate invariant classes to test, each against the axiom symmetry group
(Z^3 translations, proper cubic rotations; plus the B3a four-direction surface):
  a1 species/doubler count of the naive symbol; a2 signed index / exact-symmetry
  anomaly; a3 singlet-axial ABJ coefficient; a4 mod-16 anomaly; a5 determinant
  degree; a6 the ladder's own forced multiplicities (B7/C20/corollary, step nodes).
  Then the base: is alpha (not the integer) transportable?

(b) Dimensional transmutation: does the ladder's built content carry an
asymptotically free marginal coupling? With supplied SU(N) + N_f fundamentals at
g_bare^2 = 1, which content reaches <= 1e-15, and is it outside the two-loop
Banks-Zaks region?

(c) Rung compounding: telescoping; rung-count invariance under regrouping;
hyperbolic bound on xi/a from a relevant coupling at distance delta >= 1e-2.
Then: is PR #9702's "relevant couplings are transported but never fixed" a
provable no-go, for which tool class, and is it a no-go for (c)?

## Runs (all via `zsh scripts/capped.sh OUT python3 ...`, 0.4 GB, one at a time)

- R1 `r1_species_invariants.py`: (i) zero count of naive + Wilson symbol on
  L^d grids, d = 3, 4, r in {0, 0.1, 0.5, 1}; hypercubic covariance of the Wilson
  term (all 384 signed permutations at d = 4); (ii) signed doubler chirality sum
  sum_S (-1)^|S| for d = 1..6; (iii) u0-degree of det(u0 D_stag) on APBC blocks
  (Ls, Lt) in {(2,2), (2,4), (4,2), (4,4)} by two-point ratio; (iv) 2D U(1) toy:
  spectral flow of H(m) = gamma5 (D - m) for naive and Wilson operators at Q = 1, 2
  (index vs unsigned near-zero count).
  PASS criteria: count 2^d at r = 0, 1 at r > 0; Wilson symbol invariant under
  all signed permutations; signed sum 0; degree = Ls^3 Lt (per colour, one
  component); naive net flow 0 with 2^d |Q| crossings, Wilson net flow = +-Q at
  the physical branch.
- R2 `r2_dt_scan.py`: SU(N), N = 2..8, N_f = 0..floor(11N/2) fundamental Dirac;
  one-loop decades 8 pi^2/(b0 g^2 ln 10) at g^2 in {1, 1/u0, 1/u0^2}; sign of b1;
  Banks-Zaks g*^2. Lemma check: decades >= 15 at g^2 = 1 implies b1 < 0, for
  N = 2..100. U(1): b0 sign with charged content.
- R3 `r3_closure_mass.py`: own-code check that on-site masses drop out of the
  lattice bracket {H(N), H(M)} (scalar; naive Dirac at endpoint-mean timing), with
  a Wilson-type hop as a control where it does not. Prior art B14 E2a / B15 T5-T6a.
- R4 `r4_hyperbolic_bound.py`: random C^1 hyperbolic toy flows; check
  xi/a <= C (1/delta)^(1/y_min); escapes shown explicitly (1D Ising K-chart,
  asymptotically free flow) to locate the hypothesis each one violates.

## Pre-declared interpretation

- (a) reads HIER-DERIVED only if some class a1-a6 gives 16 for every admissible
  (axiom-covariant) deformation AND a transported base alpha exists. Expected:
  no; each class either changes under an axiom-covariant deformation, gives 0/4,
  or depends on the block choice.
- (b) reads HIER-DERIVED only if a framework-fixed content and coupling give
  <= 1e-15 outside the conformal (b1 < 0) region with no tuning. Expected: no.
- (c) HIER-NO-GO if the hyperbolic bound is proved under stated hypotheses and
  the ladder's content has y_min >= 1. The "never fixed" claim: provable only for
  a named tool class; whether it is a no-go for (c) is decided by whether (c)
  uses those tools (expected: it does not, so the no-go for (c) is the bound).
- Labels: proved / checked / suggested / reading / comparator, with path:line.

## Follow-up (11:45Z, after runs)

- R1 PASS=25 FAIL=0 (r1.log). numpy/Accelerate printed spurious slogdet FP
  warnings; added run R1b (r1b_slogdet_sanity.py, r1b.log) confirming the
  determinants are nonsingular (min |eig| >= 2.8) and slogdet = sum log|eig|.
  The degree result is exact by homogeneity anyway.
- R2 PASS=9 FAIL=0 (r2.log). Its SU(3) N_f = 0, 6 numbers at the alpha_LM
  scheme reproduce main's value-frontier table (2.74, 4.30 decades).
- R3 PASS=10 FAIL=0 (r3.log). Extra observation, not pre-registered: with a
  Wilson-type (beta-proportional) hop the on-site mass does enter the bracket;
  recorded as an untested caveat, not a claim.
- R4: first run FAIL=1 from float cancellation (atanh(tanh(18)^2)); the check
  now uses the exact identity e^{-2K'} = 2t/(1+t^2), verified by the float route
  at K = 2. Criterion unchanged. Rerun PASS=7 FAIL=0 (r4.log).
- Interpretation added after the runs (not pre-registered): mechanism (c) over
  physically distinguished units (clockwork chains, perturbative order fixed by
  a selection rule, threshold cascades) is outside the hyperbolic class (it
  violates the bounded-crossover hypothesis H4 or the small-input hypothesis H3)
  and is recorded as an open escape, not tested.
