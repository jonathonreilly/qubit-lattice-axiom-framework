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

## Block 214 prior-art sweep (hard prerequisite) — origin/main @ e249016f759f224d9b429932cd0d1db4d452dc1a, 2026-09-05
Commands (after `git fetch origin main`):
  git grep -n -iE "duality parameter" origin/main -- 'docs/*.md'          -> 0 hits
  git grep -n -iE "D07|D16|D25|D34" origin/main -- 'docs/*.md'            -> 233 hits
  git grep -n -iE "grade.parity" origin/main -- 'docs/*.md'               -> 3 hits
  git grep -n -iE "cross.degree" origin/main -- 'docs/*.md'               -> 0 hits
  git grep -n -iE "irreducible quartic" origin/main -- 'docs/*.md'        -> 0 hits
Classification:
- "D07|D16|D25|D34" (233): every hit is a hex digest fragment (sha256 / workflow ids such as `d073ccc...`, `wf_400cd07a`) or the
  Ward-identity label `D16` of the charged-lepton / g_bare notes (CHARGED_LEPTON_Y_TAU_WARD_IDENTITY_SU2_ANCHOR_NOTE_2026-04-28,
  G_BARE_H_UNIT_SAME_PROJECTED_1PI_RESIDUE_EXHAUSTION_NARROW_THEOREM_NOTE_2026-06-12, G_BARE_TWO_WARD_CLOSURE_NOTE_2026-04-18):
  a diagram-completeness label, NOT a cell-form duality pairing. NON-MATCHING.
- "grade.parity" (3): GRAVITY_SIGN_IS_NOT_A_NEW_ADMISSION_..._2026-06-18 — the e_4 grade-parity identity of the Clifford sign datum,
  not the grade parity of a folded Hodge matrix under a cell-form assembly. CONTEXT-ONLY.
- The duality parameters D07, D16, D25, D34 (Block 211), the folded H0 (Block 213) and the principal part M = H0 D + D^T H0 exist
  only in this branch's unlanded stack (Blocks 201-213). Nothing on origin/main states the parity-breaking mechanism, the
  factorization type of det M under the parameters, or the fate of the coincidence locus. Target state: OPEN.
