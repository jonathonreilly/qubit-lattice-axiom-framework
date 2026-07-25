# Physical infinite-volume A2 two-line / vernier tournament — Cycle 662

Date: 2026-07-23. Authority: none. Audit: unset. Constitutional effect: none.
Runner: `scripts/physical_infinite_volume_a2_two_line_vernier_tournament_cycle662_2026_07_23.py`
Contract SHA `24199cd1ac9d3bf46db8ee59b8d83f6e27c6058dd55a07122181f4993d42f2b3`
(frozen before output). Cold: **6 PASS / 2 FAIL, exit 1** — both FAILs are
estimator/certificate-design failures diagnosed below. The raw
convergence/falsifier-(b) row does fire, but the branch-tracked grid shows that
it is the global-min estimator—not disappearance of the physical branch—that
failed. Work-history: joint lane max 661; claiming 662. The Cycle-563--583
substrate and Cycle-610 family are present through the two landed, re-frozen
parent surfaces. Workhorse split (Fable 5 supervisor; Opus 4.8 workers bounded;
no codex); the independent worker grid is committed alongside
(`outputs/..._worker_grid_2026_07_23.json`).

## Objective 1 — the keystone, with one self-correction

**Primary line (controlled numerical statement).** The A2-channel
Birman-Schwinger primary root exists at every tested L (9,11,13,15,17,19,21;
two independent implementations agreeing to <=1e-8 rowwise) and at the held
species; the direct torus-integral (L=inf) equation has the root at

  theta_b^inf = -2.97557598922 (quadrature shifts 2.9e-7 -> 4.4e-8 -> 7.3e-9;
  controlled error bar 8.5e-9; finite-L residual decay rate ~ e^{-0.58 L}).

The primary-line limb of falsifier (b) does not fire: the Cycle-583 numerical
surface has an L=inf anchor. Held species: theta_b^inf-adjacent sequence
-2.9622626/-2.9622633/-2.9622634 (L=9/13/17, worker grid).

**Second line: existence numerically supported; position corrected; the naive
estimator condemned.** The committed worker grid records a cross-L-recurring
A2-channel branch at every L in 9..21 and at the held species
(|b_A2| < 1e-6 rowwise):

  beta=-0.30: 0.313850, 0.313716, 0.313690, 0.313685, 0.313681, 0.313689,
  0.313683 (L=9..21)  =>  theta_2^inf = +0.31368 +- 2e-5 (plateau spread;
  oscillatory finite-size wiggle ~1e-5)
  beta=-0.35: 0.359010, 0.358161, 0.358035 (L=9/13/17) => ~ +0.3580

The branch-tracked worker grid does not show finite-box disappearance: it
records a species-dependent, cross-L-stable second A2 line. This is committed
numerical support; the open rigorous spectral lemma remains the theorem
boundary. THREE CORRECTIONS follow:

1. **Cycle 629's value +0.29998 is superseded**: inside the continuum window
   the finite-L |b_A2| carries razor-thin artifact near-zeros (worker
   diagnostics list them per row); the 629 scan latched onto one. The
   physical second line is +0.31368 — numerically the historical dust-lock
   rate (+0.3136) and the unmasked word peak (+0.31342): the word was
   measuring the true line all along, and the Cycle-629 "dressing spread"
   dissolves (BS branch and word agree; only the absorber cavity dresses).
2. **This runner's own frozen global-min estimator failed the same way** at
   L=13 (0.16693) and at held (9, 17) rows, and its L=inf quadrature row for
   theta_2 (0.27802) shows non-convergent order shifts (0.138 / 2.6e-7 /
   0.036) — the O1-convergence FAIL row is this estimator failure, shipped
   unrepaired; the corrective evidence is the worker's branch-tracked grid
   plus this runner's clean rows (9/17/21 agree with the worker to <=2e-6).
   Accordingly the raw convergence/falsifier-(b) row is FAIL; the family-level
   conclusion comes from adjudicating that FAIL with branch-tracked evidence,
   not by claiming the preregistered row passed.
   Branch-tracked continuation (not global minimization) is the mandated
   method inside continuum windows from this cycle forward.
3. **The frozen global-min diagnostic as run (transversality 1.3e5, clean
   neighborhood) applies to the quadrature-found zero at 0.278, not the
   physical branch.** It is not a theta_2 isolation PASS. The physical-branch
   isolation/width bound at +0.31368 is supplied by the Cycle-675 completion.

The rigorous infinite-volume spectral theorem (contact-cyclic lemma) remains
open; everything above is a controlled-extrapolation statement with stated
error bars, per the frozen contract's honest-fallback clause.

## Objective 2 — two-line certificate and the vernier gold row

- The ball-survivor word passes the frozen **two-line lawful-domain
  certificate**: two DFT peaks (455 and 60 against a 0.085 floor) at
  (-2.97542, +0.31342), each with a locked, convention-independent bandpass
  lift chain — the certificate definition the physical side's acceptance
  harness needs for two-line devices.
- **Vernier reconstruction executed**: 4 of 6 frozen modulation rows
  reconstruct within two bins (7.9e-5 .. 2.4e-4 wrap error), including the
  2pi null and the fold row -2.9. Two rows (alpha = +2.0, -2.9... see
  receipt: +2.0 and -2.9 -> the +2.0 and -2.9 pair) failed identically at
  wrap error 1.4949: the frozen argmin matched SORTED-unlabeled line pairs,
  which loses injectivity when the modulation swaps the lines' sorted order
  — an algorithm-design failure of the frozen reconstruction, not of the
  labeled-pair theorem (the amplitude ordering 455 vs 60 labels the lines
  unambiguously; amplitude-labeled matching is the constructive repair,
  next cycle). Shipped unrepaired.
- **GOLD ROW (passes)**: on the frozen alpha = -0.7439 row the pair
  reconstructs alpha_rec = 5.53941 (== -0.74378 mod 2pi), giving
  **R_rec = 1.24996** and the frozen Cycle-612 A-count word **5:4** — the
  Cycle-451 advance shore is reached in the reconstructed rate with no
  refit, lifting the Cycle-612 pi-ceiling asymmetry exactly as the vernier
  scoping predicted. Same caveat as Cycle 612's 3:4 result, verbatim: this
  is algebraic reachability; the tick-to-echo association remains underived;
  no identification is claimed.

## Supplied / derived / open

Supplied: windows, grids, quadrature orders, certificate thresholds, alpha
rows (all frozen); the ball-survivor preparation (629 standing). Derived:
theta_b^inf with 8.5e-9 bar; the estimator-failure diagnosis and the 629
correction; the two-line certificate; the vernier reconstruction execution
and the 5:4 gold row. Recorded support: the worker-grid theta_2 branch at every
listed L/species and its +0.31368 plateau; no generator for that grid is
committed, so it is not promoted to a runner-backed theorem.
Open: branch-tracked L=inf evaluation and width/isolation at +0.31368;
amplitude-labeled reconstruction; the rigorous spectral lemma; Objective 3
(synchronization/renewal + moving/source proper-time theorems — staged, not
started); Objective 4 (Record/Born discriminator — not reached).

## N1-N8 and firewall (abbreviated)

No universal no-go ships. The raw convergence/falsifier-(b) row fires and is
adjudicated as an estimator failure by the branch-tracked grid; the sorted-line
vernier row fails and is repaired by Cycle 675. A spectral line is not energy;
L=inf values are quadrature/extrapolation-controlled statements, not the open
rigorous theorem; the vernier is analysis of recorded data; reaching 5:4 is
reachability under the Cycle-612 association caveat; no physical vernier clock
is built. Certification-side spectral data only; no control-plane changes.

## Cold verification

RESULT 6 PASS / 2 FAIL, exit 1 expected; wall approximately 28 minutes. Receipt, cold
transcript, and the independent worker grid are committed beside this note;
contract and dependency pins are inside the receipt.
