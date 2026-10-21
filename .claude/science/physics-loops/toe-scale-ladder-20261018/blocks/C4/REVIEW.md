# C4 independent review

Reviewer: a Claude subagent (same model as the author), spawned as an independent-review subagent.
Provenance: same model family as the author; independence is of *code and route*, not of model.

## Phase A — blind counts (recorded 2026-10-18 21:43:33 UTC, before opening any author log/results table)

Read before this point: NOTE.md lines 56-117 (setup + method), parent stabilizer note on main and
its runner's action definitions (Q(R) for trivial / sign diag(1,s,s) / axis s|R| / full R), the
soldering-menu note. The author's headline counts were also visible in the review task prompt, so
this phase is "blind to logs/code", not blind to the target numbers.

Reviewer code (from scratch, no import or copy of c4lib.py / author scripts):
- review_scripts/rv_common.py — O, the five actions (sign-f = half turn about (0,1,1) on odd R),
  homomorphism check, phased single-site Pauli multiplication, beta_R on signed strings.
- review_scripts/rv_linear.py — covariant F2 space with own bitset Gaussian elimination
  (checked: dim = 2 x 2 x #O-orbits for trivial: 16 on the 27-cell, 40 on the 125-ball).
- review_scripts/rv_classify.py — exhaustive enumeration of W with all symplectic conditions as F2
  quadratic forms (hi/lo split), each survivor re-checked by explicit Pauli-string commutation
  with every overlapping translate, signs fixed by explicit phased multiplication for all 24 R.
- review_scripts/rv_bruteforce.py — completeness cross-check: plain loop over all 2^dim W, explicit
  commutation only.

| action | dim W (27-cell) | unsigned | signed |
|---|---|---|---|
| trivial | 16 | 132 | 528 |
| sign | 16 | 132 | 176 |
| sign-f | 10 | 16 | 32 |
| axis | 7 | 1 (identity) | 1 |
| full | 7 | 1 (identity) | 1 |

Range 2 (125-ball), dim W = 25 for both axis and full: **4 unsigned, 4 signed** each (each
unsigned solution admits exactly the sign choice (+,+)); the identity plus three non-trivial QCAs,
same F2 matrices for axis and full.

Logs: review_scripts/rv_r1.log (TOTAL: PASS=5 FAIL=0), review_scripts/rv_bruteforce.log
(TOTAL: PASS=4 FAIL=0), review_scripts/rv_r2.log (TOTAL: PASS=2 FAIL=0).

## Phase B — comparison with the author (opened 2026-10-18 21:53:40 UTC)

| quantity | author (NOTE Thm 1 / 1b, logs c4_02, c4_06) | reviewer (Phase A) | agree |
|---|---|---|---|
| dim W, 27-cell: trivial/sign/sign-f/axis/full | 16/16/10/7/7 | 16/16/10/7/7 | yes |
| unsigned / signed, trivial | 132 / 528 | 132 / 528 | yes |
| unsigned / signed, sign | 132 / 176 | 132 / 176 | yes |
| unsigned / signed, sign-f | 16 / 32 | 16 / 32 | yes |
| unsigned / signed, axis | 1 / 1 (identity) | 1 / 1 (identity) | yes |
| unsigned / signed, full | 1 / 1 (identity) | 1 / 1 (identity) | yes |
| nonconstant tau among 132 (trivial, sign) | 84 | 84 (rv_trace.log) | yes |
| sign-f: all tau = 0 | yes | yes (0 nonconstant) | yes |
| dim W, 125-ball, axis/full | 25 / 25 | 25 / 25 | yes |
| range-2 unsigned / signed, axis and full | 4 / 4 each | 4 / 4 each, sign (+,+) only | yes |
| range-2 solution supports (X-image) | 1, 12-site-string circuit, Chamon circuit, 73 sites | 1, 33, 17, 73 sites | yes |

No discrepancy to resolve. The reviewer route differs from the author's: own bitset elimination,
quadratic-form hi/lo enumeration, explicit Pauli-string commutation re-check, and a plain 2^dim
brute force on the 27-cell (which shows the enumerator misses nothing there). Sign-f was realised
as the half turn about (0,1,1) on odd R. By on-site Clifford conjugation, the count does not depend
on the representative chosen in the Clifford class. The reviewer did not repeat the 58-homomorphism
sweep, the subgroup table, the twist runs, or the C1 E(g) C2 structure claim.

## Phase C — proofs and the circuit claims

### Theorem 2 (trace trichotomy, light cone, glider no-go)

- (a) det M = 1, tau H-invariant: **correct.** M^dag Lambda M = Lambda gives det M det M^dag = 1, so
  det M is a monomial x^m. Covariance reads M = rho(R) M^R rho(R)^{-1} with rho(R) in SL2(F2).
  So det and tr are R-invariant, and H fixes no nonzero m, which gives m = 0. Instance check: rv_trace.log.
- (b) tau in F2 gives M^2 = 1 or M^3 = 1, and the period with phases divides 4 or 6: **correct.**
  alpha^2 (or alpha^3) is the identity on the F2 layer, so it acts by a sign character. Squaring it gives the identity.
- (c) Dickson identity and vertex front: **correct.** D_0 = tr 1 = 0 and D_1 = tau. x^{nv} has
  coefficient 1 in tau^n because v is a vertex. Since 0 = centroid lies in P and v != 0, l(v) > 0,
  so (n-2j)P does not reach nv. Instance check for all 84 + 84 nonconstant-tau matrices with n <= 5: rv_trace.log.
- (d) Galois step: **correct.** Case lambda in K = Frac(R): R is a UFD, so lambda is in R. It is a unit,
  hence a monomial x^r, and tau = x^r + x^{-r} (r = 0 gives tau = 0). Case lambda not in K: then
  tau != 0, because tau = 0 would give lambda = 1 in K. So the quadratic is irreducible and separable.
  The nontrivial automorphism swaps lambda and 1/lambda and fixes x^t. That gives lambda^{2n} = 1, x^{2t} = 1,
  t = 0, and lambda is a root of unity. tau = lambda + 1/lambda is then algebraic over F2 and lies
  in R. F2 is algebraically closed in F2(x,y,z), since a nonconstant Laurent polynomial is
  transcendental, so tau is in F2. The pigeonhole step for "diameter tends to infinity" also holds
  along every subsequence, so "tending to infinity" (not only unbounded) is justified. The step
  "x^r + x^{-r} H-invariant forces H r within {±r}, hence r = 0 for O and T" is correct: the kernel of
  the induced map H -> {±1} would have index at most 2 and fix r, and T = A4 has no index-2 subgroup.
- **Issue C-1 (minor, correct with fix).** Theorem 2(d), first "Consequently" bullet, is stated
  for general H: "If tau is nonconstant, every nonidentity finite Pauli operator has support
  diameter tending to infinity". That is false when tau = x^r + x^{-r} with r != 0, which is
  nonconstant and has a bounded glider. The author's own D4/D3 rows exhibit such gliders.
  Fix: "If tau is nonconstant and not of the form x^r + x^{-r}". For H = O or T this case cannot
  occur, so no O/T conclusion changes. The Result-up-front item 3 is stated for O/T and is fine as written.

### Range-2 circuit claims (Theorem 1b)

- **[2] = prod_r exp(i pi/4 C_r), C = Chamon X(±x) Y(±y) Z(±z): correct, including phases.** The
  reviewer built the circuit with exact phases (rv_circuits.py). Its images lie in the 125-ball,
  are signed-covariant for axis and for full, and equal the reviewer's 17-site solution with its
  unique sign (+,+). Either sign of the exponent gives the same automorphism: each of X_0 and Z_0
  anticommutes with 4 translates, and i^4 = (-i)^4.
- **[1] = the same construction with the 12-site cuboctahedral string: correct, including phases**
  (33-site solution, 8 anticommuting translates). The author's c4_08 checks the transvection only
  at the F2 level and writes "exp(±i pi/4)". The reviewer confirms phases and that the ± does not matter.
  Suggested fix (cosmetic): state that the sign is immaterial.
- All four solutions have tau = 0 and M^2 = 1, and alpha^2 = id with phases: **correct** (rv_circuits.log, rv_period.log).
- Non-closure: pairwise products have range 4 and do not commute: **correct**, matching c4_07's two
  retained FAILs.
- [3], the 73-site involution, is not decomposed: **unverified/open**, as the author states.

### Other

- c4_05 is described honestly: same author, expected constants taken from c4_02. This review
  supplies the blind cross-route.
- Reviewer provenance: same model family as the author. The independence is in the code and the
  route, not in the model.

## Verdict table

| claim | verdict | severity | fix |
|---|---|---|---|
| Thm 1 counts (27-cell, 5 actions, signed/unsigned) | correct | — | — |
| 84 nonconstant-tau; sign-f all involutions | correct | — | — |
| Thm 1b: range-2 axis/full = 4/4 each | correct | — | — |
| Thm 1b: [2] = prod exp(i pi/4 C_r) Chamon, [1] cuboctahedral | correct (phases verified) | — | note that the exponent sign is immaterial |
| Thm 1b: [3] structure | unverified (open, disclosed) | — | — |
| Thm 2(a)-(c) | correct | — | — |
| Thm 2(d) Galois step and O/T no-glider | correct | — | — |
| Thm 2(d) "nonconstant tau implies unbounded" for general H | correct with fix | minor | exclude tau = x^r + x^{-r} |
| subgroup table, twists, C1 E(g) C2 structure, 58-hom sweep | not re-checked | — | — |

## Evidence (review_scripts/)

- rv_r1.log — TOTAL: PASS=5 FAIL=0
- rv_bruteforce.log — TOTAL: PASS=4 FAIL=0
- rv_r2.log — TOTAL: PASS=2 FAIL=0
- rv_circuits.log — TOTAL: PASS=14 FAIL=0
- rv_trace.log — TOTAL: PASS=9 FAIL=0
- rv_period.log — TOTAL: PASS=4 FAIL=0

## Correction confirmation (2026-10-18 21:55:44 UTC)

I re-read the complete corrected NOTE.md.

- **C-1 resolved.** Theorem 2(d) now says "nonconstant **and not of the form x^r + x^{-r}**". It
  also explains the glider form and the D4/D3 rows, and states that O and T are unaffected.
  The proof text is unchanged and was already correct.
- **Cosmetic point resolved.** Theorem 1b states that the exponent sign is immaterial, and that the [1] and [2] phases were confirmed by the reviewer.
- **Disclosures accurate.** "Review dispositions" describes my phase-A blindness correctly (the
  prompt contained the headline counts) and lists the not-re-checked items faithfully. Item [3] is
  marked open. The status line says "Independently reviewed; unaudited".
- **No new defect was introduced by the edits.**
- **New finding, C-2 (minor; pre-existing text, not introduced by the correction).** The NOTE says
  ballistic spreading "occurs exactly for the 84 nonconstant-tau matrices of the trivial and sign
  actions" (Answers (b)), and Result item 2 has similar wording. Under the **sign** action only
  **14** of those 84 unsigned matrices admit a covariant phase choice; the trivial action admits
  all 84. Evidence: review_scripts/rv_sign_spread.py, log rv_sign_spread.log, TOTAL: PASS=1
  FAIL=0. Fix: "84 (trivial) / 14 phase-valid (sign)", or mark 84 as an unsigned count, as the subgroup table already does with
  "valid". The headline conclusions do not change, since spreading still occurs under the sign action.

**Final verdict: READY**, conditional on the one-line C-2 wording fix. The fix is non-blocking for the
headline (soldered ⇒ frozen at ranges 1 and 2; no O/T gliders at any range).
