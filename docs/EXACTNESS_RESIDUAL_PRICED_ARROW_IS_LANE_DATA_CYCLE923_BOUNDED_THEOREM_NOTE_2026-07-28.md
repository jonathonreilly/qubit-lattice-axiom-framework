# The tension was an inverse in disguise: the exactness residual priced and split — Cycle 923

Date: 2026-08-05 (revised 2026-08-08, review iteration 1)

Authority: none

Audit: unset

Status: bounded worked result (owner-directed window 2b; no axiom
surface touched; narrowed at review iteration 1). The realized-state
reduction's named open — the exactness residual (why the
charged-lepton lane's registered r sits on the derived distinguished
cell so precisely) — is attacked from source. The
separatrix-vs-attractor "tension" DISSOLVES: the thermalizing map is
exactly the functional inverse of the sharpening map, and reciprocal
multipliers at a shared fixed point follow from the inverse-function
rule whenever the map is a C^1 local diffeomorphism there with
nonzero derivative. The exactness verdict is UNEXPLAINED ON THE
CURRENT SURFACE for a sharp reason: no dynamics is derived at all —
both maps are supplied — and the verdict flips between a map and its
inverse; this verdict is a support-only interpretation, conditional
on which supplied map is operative. A narrow fixed-point alternation
lemma (conditional on explicit hypotheses; NOT a universal no-go)
shows a continuous strictly increasing self-map of [0,1] with fixed
set exactly {0, 1/2, 1} cannot have all three fixed points locally
asymptotically attracting. And the residual itself SPLITS when
priced: its supported half is measure-free; its "surprise" half is
not statable from the current supplied premises alone — stating it
would need a measure over realized states, a separate new premise
outside the realized-state primitive's scope.

Claim type: bounded_theorem (the conditional two-sector
algebra-and-rate theorem below; every physical-arrow, time-reversal,
lane-data, or surprise reading is support-only and outside the
theorem grade)

## Review record (iteration 1)

Reviewed by Sol, 2026-08-08; disposition FIX_THEN_PROCEED. The
formerly headlined "arrow-universality no-go" ("no arrow on the
surface both concentrates onto 1/2 and leaves the other registered
settings persistent; any exactness account must be LANE-CONDITIONAL
— the arrow is itself lane data") is DEMOTED and withdrawn: the
executable evidence supported only the narrow fixed-point
alternation lemma stated below, the coded predicate was local
asymptotic attraction rather than any persistence/well-formedness
notion, and stateful, stochastic, nonmonotone, sector-conditioned,
extra-fixed-point, and weaker-persistence routes were never closed.
No prior gate checklist for that no-go may be cited as passed; the
broad claim has no standing surface here. Also demoted to
support-only: the physical time-reversal reading of the functional
inverse ("which arrow this history runs" is an OPEN bridge), and the
"a measure is forbidden by the primitive" wording (the primitive
supplies no measure; a measure would be a separate new premise, not
a contradiction). The exact preimage law replaces the former "halves
every step" exactness claim, whose dyadic form is a linearization.

Runners:

- [`frontier_cycle923_exactness_residual_2026_07_28.py`](../scripts/frontier_cycle923_exactness_residual_2026_07_28.py)
- [`frontier_cycle923_exactness_residual_independent_check_2026_07_28.py`](../scripts/frontier_cycle923_exactness_residual_independent_check_2026_07_28.py)

Receipt:

- [`exactness_residual_cycle923_receipt_2026_07_28.json`](../outputs/exactness_residual_cycle923_receipt_2026_07_28.json)
- [`exactness_residual_independent_check_cycle923_receipt_2026_07_28.json`](../outputs/exactness_residual_independent_check_cycle923_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status. One caveat flag is emitted (the comparator-digit convention
dependence, below); it asserts no audit verdict. Everything underivable
is PRICED, not proposed.

Worker disclosure: authored by a Claude Opus 5 worker under supervisor
spec (substitution disclosed). Novelty boundary stated honestly: the
inverse identity itself is already published (the durability note's
erasure-honesty item, 2026-06-11) — new here are the dissolution of
the reduction note's summary sentence (its S6), the Lyapunov
orientation, the coincidence deflation, and the narrow fixed-point
alternation lemma. One self-caught prose error (a hardcoded
figure in a checker summary sentence) was fixed in a dedicated
commit; the computed finding was always correct. The lever
reproduction uses its own seed — it reproduces the published claim,
not the source's exact draw. Independent audit still required.

## ABSOLUTE FIREWALL (inherited and checked)

Nothing here derives, forces, or prefers r = 1/2 as the
charged-lepton lane's setting. Mechanical S5 scan: 15 steps, zero
violations; every unique-r designator carries a named supplied
element; the designated settings across all steps span the whole
dial {0, 1/2, 1}; a planted unconditional selector makes the check
FAIL (tooth T3).

## The reconciliation (Q1) — there is no tension: g is f-inverse

Stated with the map forms, per the checker's determinacy finding
(the multiplier sentence alone is globally underdeterminate — a
constructed strictly-increasing map matches every multiplier claim
while fixing r = 1):

- the sharpening map is **f(r) = 2r^2**; the thermalizing map is
  **g(r) = sqrt(r/2)** — and **g = f^{-1} identically** (symbolic;
  numerically to 1e-12 on (0, 10]).
- Fix(f) = Fix(g) = {0, 1/2}; the multipliers at 1/2 are **2 and
  1/2 — reciprocal by the inverse-function rule**, which holds for
  any map that is a **C^1 local diffeomorphism with nonzero, finite
  derivative at the shared fixed point** (mere invertibility is not
  enough: at r = 0 this branch's own f has f'(0) = 0, the
  hypothesis fails, and g' diverges). "Unstable under one,
  attracting under the other" is forced generality under those
  hypotheses, not physics.
- The 2-sector entropy is not a third dynamics: it is the strict
  Lyapunov function that ORIENTS the pair (strictly decreasing
  under f, increasing under g, everywhere off 1/2). Its maximum is
  a static extremum that becomes an "attractor" only once the
  map g is supplied as the operative iteration.
- The inverse is a FUNCTIONAL (composition) inverse. Reading it as
  a physical time reversal, or reading either map as an operative
  physical arrow, is an OPEN bridge that no artifact here supplies
  — both maps are supplied, and no clock, semigroup, dynamical law
  or reversibility theorem is derived.
- The apparent conflict is a compression artefact of the reduction
  note's own summary sentence (its S6), verified mechanically: that
  sentence never names g(r) = sqrt(r/2).

**Coincidence deflation.** p^2/(p^2 + (1-p)^2) = p iff
p in {0, 1/2, 1} (symbolic): "interior fixed point of sharpening",
"uniform two-sector split", "maximum entropy", and "HS
equipartition 3a^2 = 6|b|^2" are ONE fact in different costumes.
The distinguished point is SINGLY, not multiply, distinguished.
(The r <-> 1-r swap fixed point is separate and merely arithmetic.)

## The exactness verdict (Q2) — UNEXPLAINED on the current surface, because map-conditional (support-only reading)

Both source notes state their map is SUPPLIED, not derived — so no
DERIVED dynamics concentrates anywhere, and every verdict below is
conditional on which supplied map is taken as operative (a
support-only interpretation, not theorem content). MARGINAL is
falsified as a description: the exact conjugacy u = 2r gives
u -> u^2 and u -> sqrt(u), so both branches are geometric in log —
**the split is in the SIGN of the exponent, not its size**:

- **Under g (thermalizing): GENERIC, conditional on g being the
  operative map.** Contraction ratio exactly 1/2 per step; within
  3e-6 of the cell from r = 1 in 17 steps (19 from r = 5; 27 from
  1e300); the basin is the ENTIRE half-line. No tuning anywhere.
- **Under f (sharpening — the map supplied by the Luders-rule
  composition-consistency note, cited as provenance only; that
  source row is unaudited on current origin/main and no retained
  grade is inherited): the exactness is amplified, not explained.**
  Expansion factor exactly 2 per step; a pattern at 3e-6 leaves the
  1e-1 window in 15 steps; remaining near the cell for N steps
  costs an initial one-sided offset of EXACTLY
  (1/2)[(1 + 6e-6)^(2^-N) − 1] (2.93e-9 at N = 10; 2.37e-36 at
  N = 100). The familiar dyadic law 3e-6 x 2^{-N} — "the admitted
  set halves every step" — is the small-eps LINEARIZATION of that
  closed form (relative error of order 3e-6), not an exact law; the
  admitted window's exact width is
  (1/2)[(1 + 6e-6)^(2^-N) − (1 − 6e-6)^(2^-N)]. Here the operative
  fixed point IS the separatrix.
- **Durability is CRITERIAL, not dynamical**: it selects the
  two-element set Fix = {0, 1/2} with no rate (exactly at 1/2:
  never leaves in 200 steps; offset 1e-5: leaves in ~14 —
  reproducing the durability note's published figure).
- The checker adds a third cell: balanced alternation gives
  f∘g = identity — **NEUTRAL** (persistence, no rate); the general
  multiplier is 2^{n_f - n_g}, so **the verdict is set by the
  composition BALANCE of the two supplied maps**, not map algebra.
- Curvature: S2''(1/2) = -1 nat exactly; the entropy deficit at
  |r - 1/2| = 3e-6 is 4.5e-12 nats (the quadratic Taylor term of
  the entropy difference, as computed). Two auxiliary gradient
  systems (constructed, labelled) — flat-metric gradient ascent of
  S2 in the r coordinate and, separately, in the p coordinate — are
  DISTINCT metric choices, not one flow rewritten; their rates
  differ (-1 vs -4) while the SIGN is common to every positive
  metric — the verdict uses only the sign.

## The firewall exhibit that doubles as a result

The dial at delta = 0 is an anti-diagonal: **each registered
setting is the unique maximum of a DIFFERENT derived functional** —
r = 0 maximizes the eigenvalue entropy (ln 3), r = 1/2 the
two-sector entropy (ln 2), r = 1 the three-degree-of-freedom
entropy (ln 3). Extremality cannot select a lane; it returns
whichever setting matches the functional you asked about. Sharper:
on this surface **r = 0 has the STRONGER exactness story** (its
functional's gradient flow arrives in finite time; f makes it
quadratically superstable) — run as an argument, the geometry
favours r = 0, not r = 1/2. (Honest asymmetry: S2 and S3 depend on
r alone; the eigenvalue entropy depends on (r, delta); all source
spectra sit at the standing delta = 0 pin (the K-reality gate G2),
untouched.)

## The fixed-point alternation lemma (narrowed at review; formerly styled an "arrow-universality no-go")

LEMMA (narrow; conditional on every stated hypothesis): let h be a
continuous, strictly increasing self-map of the interval [0, 1]
whose fixed-point set is exactly {0, 1/2, 1}. Then the three fixed
points cannot all be locally asymptotically attracting relative to
[0, 1] (attraction at the endpoints 0 and 1 read one-sidedly, from
inside the interval). Proof: on (0, 1/2), h(x) − x is continuous
and nonvanishing, hence of constant sign; since h is strictly
increasing and fixes 0 and 1/2, every orbit started in (0, 1/2)
stays in it and is monotone, so it converges to exactly one
endpoint of that interval — the one the sign selects. The other
endpoint therefore does not attract from inside (0, 1/2). The same
argument runs on (1/2, 1). So 1/2 attracts from both sides only if
0 fails from the right and 1 fails from the left; no assignment
makes all three attract. The executable runner exhibits an
eight-member polynomial family CONSISTENT with the lemma (a finite
exhibit, not the proof); the proof is the sign argument above.

Separately, a finite candidate sweep shows none of six coded
in-repo candidates (the two supplied maps, three auxiliary gradient
systems, and the durability criterion) is locally asymptotically
attracting at all three registered settings — a statement about
those six candidates only. Named escape (constructed, verified by
both runners): extra fixed points inside (0, 1/2) or (1/2, 1) make
all three registered settings attracting — at the price of
unregistered distinguished cells (falsifiable: no such cells are
registered).

NOT ESTABLISHED here (withdrawn at review iteration 1): any
universal claim that "no arrow can concentrate onto 1/2 while
leaving the other lanes persistent", that "any exactness account
must be lane-conditional", or that "the arrow is itself lane data".
The lemma's predicate is local asymptotic attraction — NOT
persistence or lane well-formedness (a repelling fixed point
remains an exact fixed point) — and the lemma says nothing about
nonmonotone maps, higher-dimensional or stateful dynamics,
stochastic evolutions, sector-conditioned laws, other fixed sets,
or weaker persistence predicates. A lane-universal evolution on an
enlarged state space with invariant sectors projecting to r remains
an open route entirely outside the lemma's hypothesis class.

## The residual priced and split (Q3)

Underivable on the current surface (each with its minimal sentence
and destination; priced, not proposed):

- **the operative-map premise (shorthand: c1)** (lane-conditional
  derivation route): "on the charged-lepton lane, re-registration
  moves the two-sector power split toward uniformity." Cannot
  arrive as a lane-universal monotone map with fixed set exactly
  {0, 1/2, 1} (the alternation lemma bars that packaging within its
  hypothesis class; other lane-universal routes remain open, not
  excluded). **This single sentence moves the verdict from
  UNEXPLAINED to GENERIC.**
- **the record-basis partition premise (shorthand: c2)** (the
  measure-side frontier): the physical record basis on the
  generation sector — upstream of c1.
- **the realized-state measure premise (shorthand: c3)** (would be
  a new premise OUTSIDE the primitive's scope — the primitive
  supplies pointwise evaluation only and supplies no measure,
  averaging, weighting, probability or typicality: "no typical or
  generic claim"). A separately derived or explicitly named measure
  would EXTEND the current premise set, not contradict the
  primitive. **The deepest result: the residual SPLITS.** Component
  (i) — "the registered r lies within the gate of the unique
  interior distinguished point" — is measure-free and fully
  supported, carrying NO explanatory deficit. Component (ii) —
  "and that is surprising" — is **not statable from the current
  supplied premises alone**: without a separately supplied
  measure/typicality bridge, "surprising" has no referent here. Any
  work treating the residual as a deficit is implicitly importing
  that measure.
- **the durability premise (shorthand: c4)** (new premise):
  firewall-safe, delivers exactness with no rate; price: it
  de-registers the r = 1 lane.
- **the initial-registration premise (shorthand: c5)**
  (realized-state registration): nearly free under g (the basin is
  everything); under f it IS the whole tuning cost.

Measurable but unmeasured (named): which supplied map is operative
(r at two registration scales — equivalent to Q at two scales via
the exact lever); whether other lanes sit on their own cells to
comparable precision (which, within the alternation lemma's
monotone-map class, would force the lemma's escape and its
falsifiable extra cells); the re-registration count N (g needs
N >= 17); the einselected partition.

## The comparator-digit caveat (caveat flag; no audit verdict)

The familiar "~3e-6" is **tau-mass-convention dependent and
non-monotonic**: 3.3e-6 at one committed convention, 9.2e-6 at
another, and EXACTLY ZERO at m_tau = 1776.96903 MeV — 0.039 MeV
above the value the reduction runner itself uses, with the
deviation sweeping 0 to ~9e-6 across a ~0.15 MeV window. The
published GATE (|r - 1/2| < 1e-5) is robust to every scanned
convention and no verdict above moves (<= 2 steps in any table).
**The explanandum is the gate, not the digit** — emitted as a
caveat flag against any future citation of the digit. Flagged, not
asserted (no external edition, table, or uncertainty is cited or
verified in-repo; the scan window is asserted for sensitivity
analysis only): if the zero-crossing were to lie inside the
externally published tau-mass uncertainty, the registered deviation
would be consistent with exactly zero — the named in-repo check is
the follow-up.

## Gates, teeth, checker

Primary: 199 PASS / 0 FAIL; 27 source values reproduced
value-for-value before any new number (both source notes' published
figures, the durability "~14", the lever on 200 circulants); 12/12
teeth; the derived-payload determinism digest is identical across a
double build (tooth T8); runtime ~0.3 s. Checker: 85 PASS / 0 FAIL
on independent machinery (symbolic sympy routes plus 60-digit
arithmetic; Tables A, B and C and the preimage-width law all
reproduced at 60 dps with zero mismatches; the 3e-6 endpoint's step
count confirmed not off-by-one); 12/12 teeth; zero refutations of
any checked claim; seven findings, all adopted above; runtime
~0.3 s. Scorecard caveat (review iteration 1): PASS totals count
executable assertions only; author-audited manual statements are
reported as findings, not checks, and several formerly literal-True
checks were replaced by computed conditions or removed from the
scorecard.

## Trace gate

```yaml
trace_class: direct_blocker_closure_candidate
target_claim_id: null
target_blocker_text: "the exactness residual (the realized-state reduction's named open inside the (i-realization) frontier: why the charged-lepton lane's registered r sits on the derived distinguished cell to the published gate)"
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: bounded_theorem
next_trace_action: "the residual is priced and split: the supported half is measure-free (no deficit); the surprise half is not statable from the current supplied premises alone (it needs a separate measure/typicality bridge, a new premise outside the realized-state primitive's scope); the summary-sentence tension is dissolved (g = f^{-1}; state the map forms, not just multipliers); the narrow fixed-point alternation lemma bars one lane-universal monotone-map packaging within its hypothesis class (the broad lane-data consequence is withdrawn); cheapest single item: the lane-conditional operative-map sentence (c1) (moves the verdict to GENERIC); named measurements: r at two registration scales, the other lanes' cell precision, the in-repo tau-mass-uncertainty check on the comparator digit; caveat flag: the digit is convention-dependent — cite the gate"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: "every dynamical statement is conditional on which SUPPLIED map governs (neither is derived; the checker's NEUTRAL cell covers balanced alternation); the exactness verdict is therefore map-conditional by construction and support-only; the alternation lemma is conditional on its explicit hypothesis class (continuous strictly increasing self-map of [0,1], fixed set exactly {0,1/2,1}, local asymptotic attraction); all spectra at the standing delta = 0 pin (K-reality gate G2); the comparator digit is convention-dependent (the gate is not); physical time-reversal / operative-arrow readings are an OPEN bridge, not claimed"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the inverse identity, the fixed-point sets, the reciprocal multipliers (under the C^1 local-diffeomorphism hypotheses), the Lyapunov property, the coincidence-deflation identity, and the entropy curvature are symbolic results verified on independent machinery at 60 dps; the rates are closed-form (2^{+-n}) with entry/residence tables reproduced by both runners and the backward-tuning table computed from the exact closed form (binary64 iteration confirms N<=20 and underflows beyond); the alternation lemma has a written sign-argument proof, a finite consistency exhibit, and a constructed escape check; 27 source values reproduced before any new number; the firewall is mechanically scanned with a planted-selector tooth"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports (load-bearing scope inputs; all linked, all pinned by the primary runner)

Every import below is a SUPPLIED definition, map, criterion or
value consumed by this block. None is independently retained on
current origin/main (their sharded rows report effective_status
unaudited where present); no authority grade is inherited from any
of them — they enter as declared scope inputs only.

- [the realized-state reduction note](ACPHILAMBDA_OCCUPANCY_SELECTION_REALIZED_STATE_REDUCTION_NOTE_2026-06-11.md)
  (the exactness-residual target, the dial, the S4.3 functional,
  and the comparator boundary);
- [the realized-state primitive note](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)
  (pointwise evaluation only; supplies no measure — the c3 split
  turns on its exact wording);
- [the separatrix note](FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md),
  [the thermalizing-arrow note](FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md), and
  [the stationarity note](FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md)
  (the two supplied maps and the stationarity criteria);
- [the flavor r-half assumptions audit note](FLAVOR_R_HALF_ASSUMPTIONS_AUDIT_NOTE_2026-05-30.md)
  (the assumption inventory behind the r-half surface);
- [the Koide circulant lever theorem note](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md)
  (the exact lever Q = 1/3 + (2/3) r) and
  [the charged-lepton Koide cone equivalence note](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md)
  (the biconditional);
- [the durability chain note](KOIDE_R_HALF_DURABILITY_STATIONARITY_CONDITIONAL_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-11.md)
  (the prior home of the inverse identity — novelty boundary — and
  the durability criterion).

### Provenance context (non-load-bearing)

- [the Luders-rule composition-consistency note](LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md):
  historical origin of the supplied map f. Cited as provenance
  only; the map form f(r) = 2r^2 is stipulated in-file by this
  block's runners, no content is read from that note by any gate,
  and its unaudited status confers no anchor or retained grade
  (the former "retained anchor" phrasing is withdrawn).
- MINIMAL_AXIOMS_2026-06-29.md was REMOVED from the runners' input
  closure at review iteration 1: no gate read it, and pinning a
  mutable axioms file made committed evidence input-stale. The
  claim depends only on the stipulated maps and coarse-grainings.

### Derived (conditional on the imports above)

- the reconciliation (g = f^{-1}; reciprocal multipliers under the
  C^1 local-diffeomorphism hypotheses; the Lyapunov orientation;
  the summary-sentence compression artefact named);
- the coincidence deflation (singly distinguished);
- the map-conditional verdict table with closed-form rates and the
  NEUTRAL cell (the verdicts themselves are support-only readings);
- the anti-diagonal firewall exhibit (extremality cannot select);
- the narrow fixed-point alternation lemma with its constructed
  escape (the broad no-go and lane-data consequence are withdrawn);
- the priced split of the residual (supported half measure-free;
  surprise half not statable from the current supplied premises
  alone — a separate measure bridge would be a new premise);
- the comparator-digit convention dependence (caveat flag).

### Open

- the lane-conditional operative-map sentence (c1) (the cheapest
  closure; priced, unadopted);
- the physical-arrow / time-reversal bridge (would be needed before
  any "which arrow does this history run" reading; OPEN, un-priced
  here beyond its naming);
- the named measurements (two-scale r; other lanes' cell
  precision; the in-repo tau-mass-uncertainty check; the
  partition);
- the (i-realization) frontier, unchanged in scope (the formerly
  claimed arrow-assignment sharpening is withdrawn with the broad
  no-go).

## Verdict

The residual that looked like a mystery about a number turns out to
be two different things stapled together: a fact the surface fully
supports — the registered pattern lies inside the gate of the one
interior point the geometry distinguishes — and a claim of surprise
that cannot be written down from the current supplied premises
alone, because writing it down requires a measure over realized
states that the primitive does not supply (adding one would be a
separate new premise, outside the primitive's scope). The famous
tension between the separatrix and the attractor dissolves into the
inverse-function rule for a supplied map and its functional
inverse; the three reasons the point seemed special collapse into
one. What remains open, support-side, is which supplied map — if
either — is operative on this lane, priced at one sentence (c1);
whether functional inversion corresponds to any physical time
direction is a separate OPEN bridge, and no lane-universal
impossibility is claimed — the narrow alternation lemma only bars
one monotone-map packaging within its stated hypothesis class. The
digit everyone quotes turns out to move with a mass convention
while the gate does not; cite the gate. Independent audit still
required.
