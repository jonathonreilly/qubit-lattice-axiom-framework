# G1 review — does PR #7334 discharge the Block-177 grading premise (B2b)?

Reviewed: PR #7334 "derive the source-functional grading boundary", branch
`physics-loop/toe-axiom-closure-block179-functional-grading-20260823`, tip `412c30cfc6`
(note `docs/ADMISSIBILITY_DIRAC_KAHLER_SOURCE_FUNCTIONAL_GRADING_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-23.md`,
runner + cached stdout, 32 PASS / 0 FAIL, runner_sha256 `8baa586a...`, exit 0).
Against: our landed Block 177 (`docs/ADMISSIBILITY_DIRAC_KAHLER_CONDITIONAL_SYMMETRIC_POWER_THEOREM_NOTE_2026-08-23.md`),
whose quasi-free sector identification is a NAMED PREMISE with exact mismatch witness
-35233/38760 (action-side herm([r Q]_SS) vs covariance-side herm([r (Q^-1)^T]_SS)).

## VERDICT: PARTIALLY

It discharges the KERNEL-SELECTION half of the premise and the vacuum leg; it does
not discharge the Hermitian sector identification. The conditional theorem does NOT
become unconditional; it contracts from a two-candidate quasi-free stipulation to a
single named prescription (Hermitianization / field-reflection) on a now-DERIVED kernel,
plus the open physical event/source-domain selection.

## (a) Which kernel, which tower

- By exact source differentiation of the normalized Gaussian exp(barJ^T G J) they derive
  G = Q^-1 and the full permanent Wick tower: equal-degree sectors are permanents of the
  two-point kernel, same-polarity and unequal-degree contractions vanish (runner checks
  SOURCE_TWO_POINT, SOURCE_WICK_PERMANENT — symbolic, dimension-general).
- The Block-107 displayed reflection K_ab = conj(G(b, theta a)) then forces
  K_S = E_S^dag r G^dag E_S, which on the four exactly-real fixtures reduces to
  E_S^T r G^T E_S — the RAW form of OUR covariance-side candidate [r (Q^-1)^T]_SS.
  This is the COVARIANCE side, exactly the direction our Block-177 per_mode recorded
  ("Wick contractions see the COVARIANCE side"); now derived, not asserted. Their note:
  "there is no freedom to substitute the action-side matrix for the covariance."
- The raw K is NON-Hermitian: anti-Hermitian rank 8 on all four extent/dial cells, because
  reflection covariance r Q^dag r = Q FAILS at the fixtures (exact (0,0) witnesses
  -997/27456 at 8x4, 3167/10560 at 12x4, dial-independent). Its Hermitian part has
  inertias (6,2,0) at 8x4 and (4,4,0) at 12x4, both dials, (n_+,n_-,n_0) — EXACTLY our
  Block-177 covariance-side inertias including the s_t=0 persistence. So herm(their
  derived K) IS our covariance-side candidate; their tower is our premised algebraic
  grading (permanent / Sym^n number grading), derived at the algebraic level only.

## (b) Fixtures and conventions — no translation needed

Their runner imports our modules directly: `import ..._conditional_symmetric_power_theorem_...
as b177`, builds `b177.Bench` at 8x4 / 12x4, s_t in {0, 1/4}, and takes inertias via
`b177.b165.real_symmetric_inertia` — our b165 (n_+,n_-,n_0) convention, bannered inline in
their claim_scope. It even reads `b177.NAMED_PREMISES` (check SECOND_GLUE_PREMISE_ABSENT)
to prove our note names a Sym^n premise but NO |Z_Q|^2-to-Sym^0 sewing premise. Zero
translation cost; same fixtures, same dials, same instruments.

## (c) The composition — what becomes derived, what remains

Composes cleanly, but not to UNCONDITIONAL. Ledger of the Block-177 premise after #7334:

DERIVED (premise discharged):
1. Which kernel the framework's own functional grades: the covariance side, raw
   K = E_S^dag r G^dag E_S. The action-side candidate is eliminated as "the framework's
   own" grading (survives only as a separately stipulated object). The -35233/38760
   witness is hereby explained: it measures stipulated-vs-derived, and B2b's "which
   kernel" question is ANSWERED.
2. The algebraic Wick number grading (permanent tower, vanishing off-diagonal degrees).
3. The vacuum leg: normalized vacuum coefficient = 1 (dial-INdependent); one-copy
   unnormalized Z_Q = pi^N/det Q positive AND dial-sensitive on all four cells. Our
   vacuum-sector positivity+sensitivity now has a derived carrier (one-copy level).

STILL PREMISED (their own classification, and I concur):
1. Hermitianization: "Replacing the raw kernel by its Hermitian part or by the
   action-side form is an added premise" — a real-part prescription is not a source
   derivative. Equivalently wall W_R: a field reflection making K Hermitian-positive
   on a physical domain. Our n>=1 indefiniteness theorem fires only through herm(K).
2. The physical event/source domain, wall W_E: the rank-two X (from #7332/b178) gives
   X^dag K X exactly Hermitian, positive definite, transport-sensitive at both extents
   and dials (exact positive half-trace gaps) — but X is an imposed falsifier; period-two
   translation symmetry does NOT select its 4/5, 3/5 weights, and the X-subspace leaks
   under r, Q and the action form (rank-2 residuals). Positive domain exists, unselected.
3. If the doubled readout |Z_Q|^2 is kept: a reweighting/doubling/sewing rule, wall W_D
   (their N2 proves W_E/W_R/W_D pairwise independent).

NET RESULT if we fold their derivation in: the conditional symmetric-power theorem
becomes ONE-PRESCRIPTION conditional — "for the DERIVED covariance-side kernel under the
Hermitianization prescription, every n>=1 sector is indefinite ((6,2,0)/(4,4,0), both
dials, both extents) while the vacuum leg is derivably positive and dial-sensitive at the
one-copy level" — with the quasi-free two-candidate stipulation retired. Their N8 row on
our Block-177 NO_GO_LEDGER says exactly this: retired "Partly"; raw Wick grading derived,
vacuum repaired; Hermitianization premise, domain/reflection, doubled-readout remain.
Standing caveats carry over unchanged: two extents, two dials, s_t temporal-only.
OPERATIONAL: their b179 depends_on b178 (= #7332 content, NOT on our main), so any fold
inherits the #7332 landing; adjudicate #7332's transport status first, per the SYNC.

## (d) Conflict with our landed 176-178

NONE found. Exact agreement everywhere the surfaces touch: covariance-side inertias match
ours cell-for-cell; Block 176's |Z_Q|^2-as-partition-level-pairing is cited and preserved;
our det Q = c P(s_t)^4 factorization and 1/|det Q|^2 vacuum readout survive verbatim; no
parent file edited. Block 178 is used only as provenance for X (their N4 marks it "No as a
witness" and recomputes covariance-side positivity directly). One corpus flag, not a
conflict: a latent Block-107 orientation defect — the b107 runner builds conj(G(a,theta b)),
the TRANSPOSE of its prose equation conj(G(b,theta a)); proved adjoints on generic G, so on
real fixtures Hermitian parts coincide and NO landed verdict changes, but the convention
must be fixed before any genuinely complex fixture. Carry this into G2/G4 specs.

## (e) The truncated "repairs the va..." = repairs the VACUUM ACCOUNTING

They repaired their OWN broader negative vacuum reading ("no positive dial-sensitive
vacuum in the Gaussian's own tower") — falsified by their cold-check, withdrawn and
demoted in the N-gate ("failed, was demoted, and is withdrawn"). The repair is the
three-way separation: normalized vacuum 1 (dial-independent) / one-copy Z_Q (positive,
dial-sensitive — closes their former vacuum wall) / doubled |Z_Q|^2 (partition-level,
needs a sewing rule to be Sym^0). It touches our objects only in support: it removes an
incorrect obstruction that would have blocked composing our vacuum leg with their tower,
and drops an overbroad use of our Block 177 as evidence against a positive one-copy
vacuum (their N4). No landed note of ours is corrected or contradicted.

## #7338 seam skim (claim_scope only) — for G2/G4

Branch `physics-loop/toe-axiom-closure-block181-canonical-reduction-20260823`, note
`docs/ADMISSIBILITY_REFLECTED_CURVATURE_CANONICAL_REDUCTION_SCHUR_POLE_TT_SPECTRAL_WEIGHT_BOUNDARY_...`.
The obstruction: on the 22-edge reflected curvature action at mu=1/1024, BOTH
pre-registered stationary-section charts (momentum-orthogonal; fixed-zero-momentum-
complement) develop an explicit METRIC-COUPLED VERTICAL SCHUR POLE, while the full action
keeps numerical rank 18 and the exact Ward map rank 4 (the 22/18/4 structure); independently
at momentum (pi/2,0,0) the odd y/z-reflection gauge-border polynomial has 14 finite nonzero
Laurent roots and the local TT-plus covariance carries WRONG-SIGN root/weight pairings
(negative root with positive weight, positive root with negative weight, plus the expected
positive TT root). Bounded numerical evidence that neither two-chart construction nor the
raw odd quotient is an automatically physical reduction; explicitly NOT gravity failure,
not an all-complement theorem, no Record-clock or inner-product construction. For G2: the
common-differential solve must not assume a pole-free canonical section; for G4: the curved
OS question must join through a chart that clears the metric-coupled pole or through a
quotient with corrected spectral weights.

## Recommended G1 fold

Fold #7334's derivation into the lane record as the B2b kernel answer; restate our theorem
in its one-prescription form above; keep W_E/W_R/W_D as the named open walls; gate the
fold on #7332 adjudication; log the Block-107 convention fix as a pre-complex-fixture
obligation. Nothing here registers, adopts, or edits any landed note.
