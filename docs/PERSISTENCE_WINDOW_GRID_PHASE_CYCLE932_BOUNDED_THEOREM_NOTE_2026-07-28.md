# The razor was a ruler: the window, the grid, and the phase — Cycle 932

Date: 2026-08-05

Authority: none

Audit: unset

Status: bounded worked result (owner-directed mass-lane closure,
window 2b; no axiom surface touched). The persistence razor — the
mass lane's last unexplained mechanism — is CLOSED, and the
mechanism is a WINDOW-versus-GRID fact, not a dynamics change. On
every measured cell the frozen certification predicate holds on
exactly ONE contiguous interval [t_open, t_close]: the opening edge
is set by the content gate and is degree-INDEPENDENT (it moves only
with the field); the closing edge is set by whichever gate bites
first (independence through degree 5, content from degree 6 at the
high field); the window's width W grows monotonically with degree;
and the persistence flag simply counts frozen grid points inside
the window. Degrees 3-4 fail NOT because their windows are too
narrow — both are wider than the 0.2 span three samples need — but
because the window opens ~0.006 after the grid point at Jt = 0.6:
in the band 2h <= W < 3h, THE GRID PHASE DECIDES. The scope
qualifier this puts on the lane's threshold is stated exactly and
not softened; the d-conjunct of the threshold law becomes DERIVABLE
from the two edges (48/48 anchors + 29/29 sealed predictions); and
the frozen verdicts are reproduced at deviation exactly 0 and then
explained — never re-graded.

Claim type: bounded_theorem

Runners:

- [`frontier_cycle932_persistence_razor_2026_07_28.py`](../scripts/frontier_cycle932_persistence_razor_2026_07_28.py)
- [`frontier_cycle932_persistence_razor_independent_check_2026_07_28.py`](../scripts/frontier_cycle932_persistence_razor_independent_check_2026_07_28.py)

Receipt:

- [`persistence_razor_cycle932_receipt_2026_07_28.json`](../outputs/persistence_razor_cycle932_receipt_2026_07_28.json)
- [`persistence_razor_independent_check_cycle932_receipt_2026_07_28.json`](../outputs/persistence_razor_independent_check_cycle932_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status. Two dated scope qualifications (the 919 and 926 notes) are
executed on their branches with pins refreshed (below).

Worker disclosure: authored by a Claude Opus 5 worker under supervisor
spec (substitution disclosed). The deciding structure (grid phase)
was NOT among the supervisor's four candidates — followed per the
minimal-premise rule. Three self-caught traps disclosed (a
wall-clock key leaking into the timing-free digest — now guarded by
a hard-fail scan, the same trap 931 disclosed; an axis-convention
reversal caught by the route-vs-route gate at 0.99 bit; mpmath
discarding imaginary parts, caught by a bracket failure). One tooth
limitation disclosed in-tooth: the Euler guard cannot use H_Z (the
global X-flip symmetry pins the branch weights for ANY
symmetry-preserving integrator) — it guards on C_ab and chi.
Independent audit still required.

## The frozen definitions (quoted from pinned bytes)

The sample grid Jt = 0.0(0.1)1.2 (13 points, h = 0.1); the run rule
("three consecutive certification samples", PERSIST_N = 3); the
deadline Jt <= 1; the independence gate 0.02; the C_ab formula.
21/21 frozen constants byte-verified, quote-identical SEVEN-way
(917/919/921/926/927/929/931). The certification code executes
VERBATIM from the pinned 919 bytes (33 functions) — the gates test
this environment, not a paraphrase.

## Q1 — the curves (diagnostic-grade; the frozen grid is the claim surface)

Identical structure on all 48 cells: ONE contiguous certifiable
interval; C_ab strictly monotone rising on [0.4, 1.3] with zero
sign changes (33/33 curve cells). t_open is the content gate's and
is degree-independent (spread 2.1e-3 across d = 2..8), moving only
with the field (~0.599 at 0.05; ~0.606 at 0.10). t_close and the
clip identity at the high field: independence clips through d = 5
(t_close 0.686 / 0.824 / 0.886 / 0.933 at d = 2/3/4/5), content
clips from d = 6 (0.955-0.957); W/h runs 0.81 / 2.18 / 2.79 /
3.27 / 3.48 / 3.50 / 3.51 for d = 2..8 — the smallest degree with
W >= 3h is FIVE, the frozen threshold. At 0.05 content clips
everywhere (W ~ 0.37, run 4). The edges are bisected on the frozen
predicate to 1e-12 (no published edge depends on the scan step);
the frozen grid is coarser than Nyquist on every cell — a sampling
protocol, not a numerical grid. Through the 931 lens
(C = 2s(1,t) - s(2,t), verified 4.0e-15): the normalized profiles
COLLAPSE across d = 3..8 to 2.6% — **d = 4 and d = 5 differ by
1.6% in shape; the razor is amplitude, not shape.**

## Q2 — the discrimination

Oscillation/trough REFUTED (zero non-monotone cells; the checker
extended the no-revival hunt to Jt = 3.0). Ceiling churn REAL BUT
NOT THE RAZOR (it occurs exactly where arms are non-isomorphic;
the edge predicate reproduces every verdict with no reference to
pair identity). Window width SUPPORTED and early closure SUPPORTED
AND SHARPENED (the clip-identity switch). **The deciding structure
is (e), GRID PHASE** — not a supervisor candidate: W >= 3h forces
run >= 3 at every phase; W < 2h forces run <= 2 at every phase;
in between, the phase decides.

## Q3 — the verdict, the qualifier, the derivation

**Mechanism grade: a measured law with a derived combinatorial
core.** Derived: given the two edges, run and verdict follow by
counting grid points (floor(W/h) <= run <= floor(W/h) + 1 — a
sampling theorem, 48/48). Imported: the amplitude law C_ab(d,
lambda) (927's arity dilution) and the universal time profile —
the honest residue, and exactly the object Cycle 933 is attacking.

**(i) The persistence count: HONESTLY SPLIT, exactly.** persist=3
has principled content at both ends and none between: at 0.10,
d <= 2 is robust-NO at every phase, d >= 5 robust-YES at every
phase, d = 3-4 PHASE-DEPENDENT — their windows (0.218 / 0.279) are
WIDER than the 0.2 span three samples need; they fail because the
window opens 0.0060 / 0.0064 after the Jt = 0.6 grid point.

> **THE SCOPE QUALIFIER (carried, not softened):** "pointer degree
> >= 5 certifies at lambda = 0.10" holds AT THE FROZEN SAMPLE GRID
> Jt = 0.0(0.1)1.2 AT PHASE 0. Phase-invariant content: d <= 2
> fails and d >= 5 certifies at every grid phase; d = 3-4 are
> decided by the phase. A grid shifted +0.010 in Jt moves the
> threshold to 3. Over 401 offsets spanning two grid periods the
> threshold is 5 on 20.7% of phases, 4 on 61.8%, 3 on 17.5% — the
> frozen phase's answer is the LEAST COMMON of the three; the
> modal answer is 4. The frozen verdicts reproduce exactly and are
> explained; the coincidence of the frozen threshold with the
> phase-invariant certifying threshold is a favourable accident,
> not a derivation.

**(ii) The d-conjunct IS derivable from the curve family**: run =
the number of grid points in [t_open, t_close], verdict YES iff
run >= 3 with the first sample <= 1.0 — reproducing 48/48 anchor
cells AND re-deriving 926's entire persistence axis (persist 2 ->
threshold 3; 3 -> 5; 4/5 -> nothing) and deadline axis (robust
0.7-1.2; dead below) from the same two edges.

**(iii) The seal: 29/29** — built from the window edges alone with
a hard guard proving zero frozen-machinery evaluations of sealed
cells at seal time; cells at three never-used fields, degrees 9-10,
and tree anchors; the sealed offset map re-verified with the FULL
frozen machinery on shifted grids at 5 offsets, all agreeing.

## The corrections executed (post-ship-edit pattern)

Dated grid-phase scope qualifications added to the 919 note
(beside its existing 926 gate-band qualification) and to the 926
note's threshold law (whose d-conjunct is now derived and
phase-scoped), pins refreshed on both branches.

## Checker

SUPPORTED, 17/17 teeth, ZERO refutations, on machinery sharing
nothing with the primary or any parent (sparse CSR, self-written
Lanczos cross-validated at 1e-12, tensordot, brentq, reversed
iteration, one edge end-to-end in 50-digit mpmath agreeing with
the float64 bisection at 1.6e-13). Rivals beaten quantitatively
(time-rescaling loses to amplitude-only by 20.8x; the "C_ab(0.9)"
shortcut is frozen-field-correct but fails off-field and
off-phase; width-without-phase mispredicts d = 3-4). Ten unseen
out-of-sample cells reproduce run, verdict, and bracket. Two
findings ADOPTED mid-block and re-verified: the phase histogram
(the least-common fact) and the statistic-dependence of the d = 2
exception's isolation (disclosed). Runtimes: primary 210.6 s,
checker 46.7 s; both bit-identical timing-free digests on double
runs.

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "the persistence razor (degrees 3-4 reach the ceiling with dependence far under gate yet persist only 2 of 3 samples — the mass lane's last unexplained mechanism; 926's persist-axis fragility)"
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "the razor is a WINDOW-vs-GRID fact: one monotone certifiable interval per cell (t_open content-set and degree-independent; t_close clip-switching; W monotone in d) with persistence counting grid points — the d-conjunct DERIVES from the two edges (48/48 + 29/29 sealed; 926's persist and deadline axes re-derived); CARRY THE SCOPE QUALIFIER on every threshold citation (frozen grid, phase 0; d=3-4 phase-decided; the frozen answer is the least-common across phases, modal 4); the honest residue is the amplitude law C_ab(d, lambda) = 927's baseline table (Cycle 933's target) and the unexamined t_open(lambda) regularity; the frozen verdicts are explained, never re-graded"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: "all continuous-time and offset-shifted results are diagnostic-grade (the frozen grid is the claim surface; the shifted-grid excess-gate baseline construction is declared and is not the frozen protocol); the amplitude law and the universal profile's form are imported/undegraded (the residue); n>11 cells use the declared capped scan (edges still bisected to 1e-12); G6 not re-run (919's own exclusion); degrees 7-10 abstract; the revival hunt is bounded, not a proof of absence"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the frozen verdicts and every parent surface reproduce at deviation exactly 0 with the certification code executed verbatim from pinned bytes; the window edges are bisected to 1e-12 and confirmed at 50 digits; the edge-counting law is exact on 48 anchors and 29 sealed cells built from edges alone under a hard no-pre-evaluation guard; the phase sweep is verified on full frozen machinery at 5 offsets; the checker refutes nothing on fully disjoint machinery and its two findings are adopted"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports

- the three frozen memos (definitions quoted; the certification
  code executed from pinned bytes), the 919/926/927/929/931
  primaries + receipts (all reproduced at zero), the axiom memo
  (pinned); the amplitude law (927's — the declared import).

### Derived

- the single-window structure with the content-set,
  degree-independent opening edge and the clip-identity switch;
- the edge-counting law (the sampling theorem core) and the
  derivation of 926's persistence and deadline axes from two
  edges;
- the phase classification (robust-NO / phase-decided /
  robust-YES) with the 401-offset histogram;
- the scope qualifier and the favourable-accident finding;
- the 29-cell sealed verification;
- the two executed note qualifications.

### Open

- the amplitude law C_ab(d, lambda) — the razor's only remaining
  input (= 927's baseline table = the s(k) shape; Cycle 933,
  running);
- the t_open(lambda) degree-independence (an unexamined
  regularity fixing the window's left edge);
- the universal profile's functional form.

## Verdict

The razor the lane kept cutting itself on turns out to be a ruler
laid slightly askew: every geometry opens one honest window, the
window widens with degree exactly as the dilution law says it
must, and certification was never anything but counting how many
tick marks fall inside. The degrees that failed were not too weak
— their windows hold three samples' worth of room — they were
unlucky by six thousandths of a unit of time against a grid frozen
long before anyone knew there was a window. Said plainly and kept
on the claim surface: the threshold's phase-invariant content is
real at both ends, the middle belongs to the grid, and the frozen
protocol's famous answer is the rarest of the three it could have
given. Nothing shipped is re-graded — it is explained, sealed,
and qualified where it lives, and the one number still entering
from outside is the amplitude table whose derivation is already
running as the next block. Independent audit still required.
