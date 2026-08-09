# Seven exact algebraic results on stipulated definitions

Date: 2026-08-08

Authority: none

Audit: unset

Status: bounded support note. This note carries seven narrow exact
algebraic results, each restated on definitions stipulated in this
file and in the runners. Nothing here is a derivation from the repo
axioms, a route closure, a no-go, a physical identification, or a
selection among rival expressions. Every claim below is exact
rational/integer mathematics on its own stipulated objects, and each
unit says what it does NOT establish. Historical provenance (these
are the results a combined adversarial science review named
salvageable from a rejected package) is recorded in the Review record
at the end of this note.

Claim type: bounded_theorem (support-only; no headline claim; each
unit is bounded to its stipulated definitions)

Imports: none. All definitions are stipulated in this file and
restated verbatim in the runners. The primary runner has no file
inputs at all; the independent checker reads exactly one non-science
input — the primary's receipt, as execution evidence, declared in its
own receipt `inputs`. Neither runner pins axiom bytes, executes
git-history objects, or contains fitted or measured comparators.

Runners:

- [`salvaged_exact_algebra_2026_08_08.py`](../scripts/salvaged_exact_algebra_2026_08_08.py)
  (primary; 31 computed checks, fail-closed, exit 0 only on full PASS)
- [`salvaged_exact_algebra_independent_check_2026_08_08.py`](../scripts/salvaged_exact_algebra_independent_check_2026_08_08.py)
  (independent check; 27 computed checks; every unit recomputed by a
  different exact route; verifies the primary receipt fail-closed and
  full-surface — the entire receipt payload must equal a canonical
  expected record assembled from the checker's own seven routes, and
  two tamper regressions run every time: a byte tamper must break the
  digest, and the same semantic tamper with a recomputed self-digest
  must still be rejected by the full-payload comparison)

Receipts:

- [`salvaged_exact_algebra_receipt_2026_08_08.json`](../outputs/salvaged_exact_algebra_receipt_2026_08_08.json)
- [`salvaged_exact_algebra_independent_check_receipt_2026_08_08.json`](../outputs/salvaged_exact_algebra_independent_check_receipt_2026_08_08.json)

Runner logs:

- [`salvaged_exact_algebra_2026_08_08.txt`](../logs/runner-cache/salvaged_exact_algebra_2026_08_08.txt)
- [`salvaged_exact_algebra_independent_check_2026_08_08.txt`](../logs/runner-cache/salvaged_exact_algebra_independent_check_2026_08_08.txt)

Constitutional effect: none. This package changes no axiom,
foundation, primitive, registry, policy, queue, audit result, or
audit status.

Reproduction: both runners are self-contained Python 3 standard
library programs. `python3 scripts/salvaged_exact_algebra_2026_08_08.py`
then `python3 scripts/salvaged_exact_algebra_independent_check_2026_08_08.py`;
both exit 0 with the PASS counts above, and the receipts are
byte-deterministic (no timestamps), so cold reruns reproduce the
committed receipt bytes exactly.

## The seven units

Each unit names its stipulated objects first. The stipulation is the
boundary of the claim: nothing about physical records, readouts,
masses, angles, or lattice dynamics follows from any of it.

### 1. Trace-free/conformal split of a sector triple

Stipulated: a sector triple is a vector v in Q^3; the conformal
channel is conf(v) = (trace(v)/3)(1,1,1); the trace-free channel is
tf(v) = v - conf(v); the graded operator is
G_sigma(v) = tf(v) + sigma*conf(v); the recoil ledger family is
(-2w, w, w) for integer w.

Exact results: tf + conf = id; trace(tf(v)) = 0; the two projectors
are idempotent, complementary, and mutually annihilating; the
constant part of the split is unique; every ledger triple (-2w, w, w)
has sector trace zero, so its conformal channel vanishes and every
G_sigma fixes it; G_sigma fixes exactly the trace-free vectors when
sigma differs from 1. The independent check rebuilds the conformal
projector as the group average (I + C + C^2)/3 of the 3-cycle C and
reproduces all of it.

Not established: that any physical sector ledger has this form, or
any admissibility classification of graded operators.

### 2. Affine grading normal form on the line w(t) = (1, 1+t, 1-t)

Stipulated: the direction set D is the six unit vectors of Z^3 in the
fixed order (+x, -x, +y, -y, +z, -z); a configuration is a direction
d and a triple tau in D^3; the balance residual is
r(t) = sum_s w_s(t) D[tau_s] - w_0(t) D[d] on the grading line
w(t) = (1, 1+t, 1-t); the raw ledger is
(D[tau_0] - D[d], D[tau_1], D[tau_2]) and its sector trace is the sum
of its three vectors.

Exact results, verified on all 1296 configurations (7776 residual
identities at six rational probe points, and again by two-point
interpolation at two fresh probe points in the independent check):
r(t) = A + tB exactly, with A = D[tau_0] + D[tau_1] + D[tau_2] - D[d]
a function of the support alone and B = D[tau_1] - D[tau_2] never
depending on the direction or the first sector; the sector trace of
the raw ledger is identically A.

Not established: any census of lawful configurations, any retirement
of the parameter t, and any claim about which grading is physical.

### 3. The permutation module of C_3 on Q^3

Stipulated: C is the permutation matrix of the 3-cycle
(0 -> 1 -> 2 -> 0) acting on Q^3.

Exact results: the fixed subspace is the line spanned by (1,1,1); the
complement is C-invariant of dimension 2 with characteristic
polynomial x^2 + x + 1, irreducible over Q (rational root theorem)
and over R (negative discriminant), so the dimension pair over Q and
over R is (1, 2); over C the module splits into three character
lines, pattern (1, 1, 1). The independent check reproves this by
character theory with exact arithmetic in Z[w]/(w^2 + w + 1): the
multiplicities over C are (1, 1, 1) and the two nontrivial
Galois-conjugate characters fuse into one 2-dimensional
Q-irreducible.

Not established: any identification of these dimensions with record
weights, readout weights, formation weights, or any physical pair.
The review found that identification to be an unproved bridge; it is
removed here, not repaired.

### 4. Five-form collapse, family coincidence at N = 3, and the fixed-locus sum

Stipulated: the five closed forms in (w0, w1, n)

    w1/(w0+w1)^2,  w0*w1/n^2,  w1/n^2,  (n-1)/n^2,  w1/(w0*n^2)

on the locus (w0, w1) = (1, n-1); and the three rational families
(N-1)/N^2, (N^2-1)/(12N), (N-1)(N-2)/(3N).

Exact results: on the locus every one of the five forms equals
(n-1)/n^2 — as values for n = 2..50 in the primary and as
cross-multiplied polynomial identities in the independent check, so
the five-fold "choice" among them is a choice of expression, not of
value, on that locus. The three families coincide pairwise exactly at
N = 3 (common value 2/9) and separate at every other N in 2..200
(at N = 4 they read 3/16, 5/16, 1/2). The fixed-locus sum over the
nontrivial N-th roots of unity z of 1/((1-z)(1-z^{-1})) equals
(N^2-1)/12 exactly for N = 2..12, computed in the quotient ring
Q[x]/((x^N-1)/(x-1)) by the primary and independently as
Tr((L + J/N)^{-1}) - 1 for the N-cycle graph Laplacian L in the
check; its 1/N normalisation is the family (N^2-1)/(12N).

Not established: that any of these families is a readout functional
of anything, that N = 3 is selected by any principle (the coincidence
at N = 3 cuts BOTH ways: at the one point where the three families
agree, agreement cannot distinguish them), and any comparison against
a fitted or measured enclosure — the review found the fitted
comparator unpinned and it is dropped, not repaired.

### 5. The screened origin step

Stipulated: rationals G0 and G1 subject to the single origin equation
6*G1 - (6+m)*G0 = -1 with a rational screening parameter m.

Exact results: the equation is equivalent to
G0 - G1 = (1 - m*G0)/6 — verified on a rational grid by the primary
and as a bivariate polynomial identity after eliminating G1 in the
independent check; 6*(G0 - G1) - 1 = -m*G0 identically, so the step
equals 1/6 exactly when m*G0 = 0, and on the half-line G0 > 0 exactly
when m = 0.

Not established: that any lattice Green function satisfies the
stipulated one-orbit symmetry, positivity of G0, or any repair of a
harmonic sector.

### 6. Projector-ratio witness

Stipulated: J is the all-ones n x n matrix, P = J/n, Qp = I - P;
diag(M) = M[0][0]; totalsum(M) = the sum of all entries.

Exact results: diag(Qp) = (n-1)/n and totalsum(J) = n^2, so
diag(Qp)/totalsum(J) = (n-1)/n^3, which is 2/27 at n = 3; the
independent check re-derives the diagonal by the equal-diagonal/trace
route. Reachability only: the rival expression diag(Qp)/n =
(n-1)/n^2 on the same two matrices is exhibited in the same runner,
so exhibiting an expression that reaches a value demonstrably selects
nothing.

Not established: that any physical constant equals (n-1)/n^3, or that
the structure prefers this witness over any other.

### 7. Pointer-cycle identity

Stipulated: G is a finite simple graph on labelled vertices with a
marked vertex S.

Exact result: a cycle through S exists iff two distinct neighbours of
S are joined in G - S, and then the shortest cycle through S has
length exactly 2 + min over distinct neighbour pairs (a, b) of S of
the distance from a to b in G - S. Proof shape: any cycle through S
runs S, a, ..., b, S with the inner path avoiding S, giving the lower
bound; a shortest inner path closes to a simple cycle attaining it.
Verified exhaustively on all 32768 graphs on 6 labelled vertices
(brute-force cycle enumeration vs the formula) and, in the
independent check, by the distinct edge-removal BFS route on all 1024
graphs on 5 vertices, 200 seeded 8-vertex graphs, and the same full
6-vertex census recomputed independently.

Not established: any three-regime loop-cost law, any mechanism claim,
and any statement about measured loop costs on frozen fields — the
review found that content to be a finite numerical classifier with
non-reconstructible inputs, and it is dropped, not repaired.

## Review record (salvage pass on PR #5995)

The combined adversarial review of PR #5995 (129 delta files, 17
notes, 34 runners, 44 receipts, 34 logs) returned disposition FAIL
and named as salvageable only "narrow exact results ... separable
from the failed bridges/no-go rhetoric" (its salvage finding, F14).
The salvage pass (commit `b472df1c1b`) deleted every delta file of
that package and rebuilt exactly the salvageable algebra as the
single package above. The deleted files remain recoverable at the
untouched PR head: branch `physics-loop/toe-time-blockAC2-20260802`,
immutable commit `867aff0edc16f64b5e8d5cc1022cbf9ce92b92de`.

Salvaged (source -> unit above): Cycle 872 exact conformal/trace-free
algebra -> unit 1; Cycles 876/895 exact affine normal form -> unit 2;
Cycle 883 permutation-module split with all Record/physical-weight
language removed -> unit 3; Cycle 899 algebraic identities (five-form
collapse, fixed-locus sum) plus the family-separation facts the
review verified -> unit 4; Cycle 900 signed origin equation and
massless-slice statement -> unit 5; Cycle 904 explicit witness
(n-1)/n^3 as reachability-only -> unit 6; Cycle 921 exact
graph-distance/cycle-length identity -> unit 7.

Dropped, with the reviewer's reason compressed (finding IDs refer to
the PR #5995 review record):

- Cycle 928 route-sweep note, both runners, receipts, and the
  type-gap/new-primitive closure: primary PASS forced by hard-coded
  false gates on every real candidate, hard-coded exact-target and
  typing answers, vacuous angle-context assertion (F1); committed
  PASS not reproducible at the PR's own HEAD — fresh run fails 46/2
  and the checker then reads the failed receipt (F9); load-bearing
  Cycle 924 ancestor note absent from origin/main (F2); "emitted"
  audit rows are prose inside a receipt, not dispatchable (F13);
  terminal no-go language fails all of N1-N8 (F5). The narrow
  angle-packaging observation inside it was not named salvageable and
  goes with the package.
- Cycle 882 multiplicative closed-library wall (note + runners): the
  no-go theorem is invalid — a multiplicatively closed set need not
  contain the identity (counterexample {(2/9)^n : n >= 1}); sampled
  exponent windows include the empty product and are not closed;
  checker repeats the mistake (F10); its own lemma is classified
  equivalent to the original obligation (F4). Explicitly listed by
  the review as not-to-salvage.
- Cycle 883 Record-weight-pair note and both runners: representation
  dimensions renamed as physical Record weights without deriving the
  coefficient module, equivariance, or the identification; over C the
  pair is a convention-dependent repackaging (F3). Only the pure
  representation theory survives, as unit 3.
- Cycle 901 space-identification note and both runners
  ("DECIDED-F_DIM"): excluding one candidate functional does not
  positively select the other from infinitely many; the missing
  positive-selection lemma is target-equivalent to the disputed
  binding (F4). Explicitly listed as not-to-salvage. The exact family
  values it relied on are carried, without any selection reading, in
  unit 4.
- Cycle 916 theta-reconciliation note and both runners: reproducible
  only from nine git blobs and two commits unreachable from
  origin/main; a fresh clone fails before the claimed comparison
  (F7).
- Cycle 921 loop-cost note, both runners, and the three-regime
  pair-cycle law with its measurement table: the law is a
  field-branched classifier scored on the surface used to identify it
  (F11); the primary hard-pins thirteen absent input files and its
  own load-bearing receipt was never committed, so the closure is not
  reconstructible (F15). Only the exact graph identity survives, as
  unit 7.
- Cycle 899 fitted-enclosure comparison (the "empirically clean"
  numeric claim): the fitted enclosure is hard-coded, unpinned, and
  absent from the imports list; the checker copies the same literals
  (F6). Only the exact algebra survives, as unit 4.
- Cycles 886, 888, 890, 898, 903, 904 notes and runners (censuses,
  scope pricing, escape coverage, terminal clauses): unqualified
  terminal/no-go conclusions over finite enumerations fail the no-go
  audit — four route families instead of five, coupled walls,
  imported referents, terminal rhetoric, no cross-cycle persistence
  table (F5); bare workstream codes as primary scientific names
  (F12); none of their negative closeouts was named salvageable. The
  single exact witness inside Cycle 904 survives, as unit 6.
- Cycles 872, 876, 895, 900 notes and runners as shipped: obsolete
  axiom-byte pins that hard-fail preflight on current origin/main
  (F8); declared source runners/receipts absent from the worktree and
  from origin/main (F15 — Cycle 872's two source runners, Cycle 895's
  Cycle 873/880 inputs, Cycle 900's Cycle 884 inputs); their exact
  algebra survives as units 1, 2, and 5 on in-file stipulations with
  no pins (Cycle 899's algebra, unit 4, is covered in its own entry
  above).
- All 34 committed runner logs and 44 receipts of the old package:
  caches of runners whose executable closure cannot be reconstructed
  (F9, F15) or whose gates were not evidence-driven (F1).
- The nine prose "audit rows" and all campaign/window process
  language on science surfaces: not machine-visible to the audit
  worker, missing dependency links (F13); branch-local process
  vocabulary on durable surfaces (F12). This note requests no extra
  dispatch or re-audit rows; its own ordinary claim row is
  pipeline-seeded and remains `unaudited` for independent review.

What this salvage does NOT do: it does not repair, re-derive, or
re-assert any dropped claim; it does not touch the axiom surface; it
authors no audit verdict and requests no extra dispatch or re-audit
rows (its own pipeline-seeded claim row remains `unaudited`); it does
not compare anything to fitted, measured, or imported values.
