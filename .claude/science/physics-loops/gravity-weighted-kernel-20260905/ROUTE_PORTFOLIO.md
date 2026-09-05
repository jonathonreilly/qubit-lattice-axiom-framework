# Route portfolio — block 213

## Prior-art sweep (hard prerequisite) — origin/main @ e249016f75, 2026-09-05
Commands:
  git grep -n -iE "(weighted.kernel.*dispersion|dispersion.*weighted.kernel|cone.*metric.*cone|metric's cone|light.cone.*symbol)" origin/main -- 'docs/*.md'
  git ls-tree -r --name-only origin/main -- docs/ | grep -iE "DISPERSION|WEIGHTED_KERNEL|LIGHT_CONE|SYMBOL"
Hits and classification (all NON-MATCHING or context-only):
- NONAFFINE_PURITY_WEIGHTED_KERNEL_IS_NOT_BARYCENTER_EVALUATION_BOUNDED_THEOREM_NOTE_2026-08-13 — a purity-weighted kernel (different object).
- DISPERSION_RELATION_NOTE / DISPERSION_HIGH_P_TIEBREAKER_NOTE / FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL (June) — staggered-fermion dispersion, not the DK cell-form kernel.
- GRAVITY_PREMISE4_REFRACTIVE_INDEX_FROM_DISPERSION (June) — refractive-index bridge, different premise class.
- LIGHT_CONE_* notes — support-recursion / Lieb-Robinson cones, not a symbol identity.
- BOOST_CONE_APBC_SIGN_NEUTRAL — boost-cone sign neutrality, not the weighted symbol.
In-chain (unlanded): R5 proved the FLAT symbol on (4,4)/(4,2,2) (campaign record, round 3); the weighted symbol is named there as the open successor. Target state: OPEN after matched-hit review.

## Approach families (see APPROACH_REGISTRY.md)
F1 exact plane-wave symbol (object: K(moduli) on the periodic bench; mechanism: translation covariance + roots of unity; terminal: closed-form sigma(k; moduli)).
F2 Schur/metric identification (object: the cell form's covariance object; mechanism: (g^-1)[pp] = Schur marginal law; terminal: principal part = g^{mu nu} k k) — checker's independent route.
F3 small-k gradient expansion of the exact symbol (weaker than F1 for the full cone; identifies the metric).
F4 counter-probe: a moduli point where the symbol is not quadratic-form-shaped (prunes the hypothesis).

## Scoring
F1+F3 first (one runner): highest claim-state movement (turns the named successor hypothesis into an exact statement either way), existing runner machinery (b201/b211 constructions), one unattended block. F2 as the refuting checker route. F4 folded into F1's witness set (pi = -1 class, PD boundary).
