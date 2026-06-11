
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
