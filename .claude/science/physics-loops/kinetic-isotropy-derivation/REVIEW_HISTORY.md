
## block05, review round 1 (TWO synchronous referees + incremental findings files, 2026-06-10)

The synchronous-delivery clause + /tmp findings files (instituted after the
block04 process failure) worked: both referees delivered complete reports;
the math referee's incremental file additionally allowed early integration.

PROVENANCE referee: 2 BLOCKERS + 3 MAJOR + 4 MINOR/NIT.
| finding | resolution |
|---|---|
| BLOCKER: block04 was REWRITTEN by the reviewer on landing (287->154 lines, retitled); the note quoted phantom labels (F2b, E6, the "named refinement" sentence) from the superseded pre-landing text — the block03 lesson recurring | branch rebuilt from landed main; every block04 citation re-pointed to the LANDED text (Result 4, Result 6, the landed runner's own "named refinement" comment) |
| BLOCKER: open-1 numbers (450k leaves, hunts, census) were not runner-derived in shipped artifacts | E1 seeded census + deterministic G1 cap-exceedance PORTED into the runner; development-hunt claims descoped to no-claim-weight wording |
| MAJORs: review-history reference false; import-ledger row missing; "#3502 merged" implications | episode row shipped (this entry); block05 ledger row added; "landed via reviewer rewrite" wording |

MATH-PHYSICS referee: 2 BLOCKERS + 6 MAJOR + 5 MINOR/NIT — and an EXACT
PROOF GIFT that made the repaired theorem stronger.
| finding | resolution |
|---|---|
| BLOCKER: D1 "everywhere doubly degenerate" FALSE at generic moduli (splittings up to 2.39) — a phi=0-stratum fact; the symbolic square-check was a tautology (sympy sqrt(e)^2 -> e always) | D1 rewritten: family-wide lambda -> -lambda pairing (computed at 25 random moduli/momenta) + degeneracy as stratum property; "Kramers" deleted |
| BLOCKER: the velocity set {0, +-1/6} WRONG: "flat phi=0 stratum" was a central-difference artifact (sorted spectrum exactly even in t); true set = {+-1/6, +-1/(2 sqrt 3)}; slope 0 NEVER occurs | D3 rebuilt around the referee-supplied EXACT factorization 9p = Q_A Q_B / w^2 (verified as a rational identity in unimodular symbols); slopes derived exactly; the artifact documented (D3c) |
| MAJOR: "projective" is a MISNOMER — all cocycle relations close to +I (S3 has trivial Schur multiplier); the content is the eta SIGN TWIST vs the bare permutation rep | renamed throughout (note + runner + filenames): eta-twisted linear S3 action; triviality stated as computed fact |
| MAJOR: "cone" geometrically wrong — k=0 carries a rigid DRIFT VECTOR +-(1,1,1)/6 (tilted plane, transverse-flat); generically not a touching point; first-order transport maximally ANISOTROPIC | geometry rewritten; the anisotropy stated as a notable fact for the campaign, not hidden |
| MAJOR: "no kinetic dial" overclaimed — off-axis FRONT SPEEDS are continuously moduli-tunable (0.19-0.24); only the symmetric-point drift and the exactly-linear diagonal are rigid | the no-dial claim SCOPED; the continuous front content STATED as the family's honest moduli content |
| remaining MAJOR/MINOR (open-1 provenance overlap, N4 quote, docstring contradictions, W23^2 omission, F1 = exactly 2/3, f(D)-distinction wording) | all fixed |

DEVELOPMENT EPISODE (recorded per the provenance fix): the first-draft
"tunable 5/5" tangent-walk signals were momentum-translation +
fixed-momentum-comparison artifacts; resolved by translation-invariant cone
data, then superseded entirely by the exact factorization.

Runner after fixes: 13 checks expected (A1,B1,C1,C2,D1,D2,D3a,D3b,D3c,D4,F1,E1,G1).
**Disposition: pass** — 13/13 after three exactification iterations (the
Q_B role-assignment transcription corrected against my own sp.factor output;
numpy-float orbit signs cast to exact integers — float fuzz was defeating
the rational identity). The exact factorization now stands on the
artifact's own derivation with the referee's proof as corroboration.

## block06, review round 1 (TWO synchronous referees, 2026-06-11)

PROVENANCE: 0 BLOCKER, 4 MAJOR (paraphrase-in-quotes of the block05 sentence
being corrected; supersession under-scoped vs block05's ~6 occurrence sites;
missing Reproduction/Claim-scope sections; pack entries) + 2 MINOR (N4
misattribution; two newer landed same-surface notes uncited) — all fixed;
W-IR quote verified VERBATIM; all deps landed and accurately characterized.

MATH-PHYSICS: 1 BLOCKER + 2 MAJOR + 4 MINOR:
| finding | resolution |
|---|---|
| BLOCKER: E1 compared two hand-typed Rational(1,2) constants (vacuous PASS); the slope comparison was unit-INCOHERENT (family diagonal slope = 1/2 per axis-component but 1/(2 sqrt 3) per momentum arc length — sqrt-3 off vs the per-axis candidate against any single transfer dispersion) | E1 REBUILT: per-tick gradient VECTORS computed both sides (cycle exact from D1; family symbolic from the law, psi-independent) — IDENTICAL +-(1,1,1)/6: convention-independent OS0-indifference; the absolute unit identification split off as the NAMED premise U-T; equal-stratum datum named |
| MAJOR: "no isotropic cone in either candidate" FALSE — the within-block touchings are EXACTLY isotropic 3D cones Phi = |q|/sqrt 3 (referee-verified 7 directions) | new check E3; Part F and the cone row REWRITTEN POSITIVELY: an isotropic cone exists in the family at quantized slope 1/(2 sqrt 3); the H-slope (1/2) cone remains unrealized (sqrt-3 mismatch) |
| MAJOR: C2 proof gap — the line's gaplessness is INTER-block (shared-beta common root X = beta w), within-block touchings are isolated points; off-diagonal exclusion needed the difference factorization | C2 rebuilt: shared-root identity + Q_A - Q_B = (alpha-gamma)(3 beta - X sigma_bar), both exact |
| MINORs: unimodularity of both roots assumed (now proven: Y1Y2=1, real sum in [-2,2]); cycle bands co-move vs family counter-propagating (added to E2); "EVERY translation-invariant functional" overbroad (scoped to per-band; both inter-block offsets named); psi != 0 -> psi not 0 mod pi; "completely solved" scoped to the eigenvalue problem | all fixed |
| F4: the block05 front-speed correction CONFIRMED independently (the referee regenerated block05's exact RNG stream: cached values 0.169-0.232 reproduced by the single-block law to 5e-15) | quote/number wording aligned |

Runner after fixes: 13/13. NOTE the E1-insert initially vanished via another
silent str.replace overlap (caught by counting checks: 12 != 13 expected) —
grep-verify EVERY patch, count checks after every edit.
**Disposition: pass (13/13; both referee rounds integrated).**

## block07, review round 1 (TWO synchronous referees, 2026-06-11)

MATH-PHYSICS: NO BLOCKER. Independently confirmed all unit conversions
(rebuilt the actual walk matrix; one-sided rate 0.2886751 = 1/(2 sqrt 3));
confirmed the theta = Phi/2 double-cover is genuine, the tau-rescaling
dichotomy survives, E1's odd-vs-even obstruction is a real theorem, and no
vacuous checks. 2 MAJOR: (1) block06 dependency dangling (unlanded) —
fixed: branch reviewed after block06 landed; A3 rebuilt to RE-DERIVE the family cone
from the walk matrix on-branch (pi-wrap at lambda = -1 dodged by tracking
X = lambda^2); (2) "exhaustion of the covariant sector" overclaim — scoped
to the EXHIBITED set with block05's open named as the bound.

PROVENANCE: 2 BLOCKERS (stacked-PR requirement per SKILL; missing pack
entries) — both resolved; 3 MAJOR (runner docstring "all landed" false;
N4 stitched non-verbatim quote; the successor campaign pack shipped 2 of
13 SKILL-required files) — all fixed (docstring gated; N4 verbatim; the
matter-cone-larger-cell pack filled to the full file set with required
STATE.yaml fields); 4 MINOR (N7 cell-unit mislabel; A2 comment formula;
the chain-wide rational-placement survey claim enumerated+falsifiable;
PRs #3545/#3543 recorded in the successor pack and the W-IR row).

**Disposition: pass (9/9; reviewed after block06 landed).**
