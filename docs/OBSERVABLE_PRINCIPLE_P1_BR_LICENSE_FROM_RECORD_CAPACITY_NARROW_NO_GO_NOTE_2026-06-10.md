# Observable-Principle P1 — The (BR) License Has No Record-Capacity Supplier (Narrow No-Go), the Demand Reduces Further to the Increment Clause (BR-int), and the Missing Record Clause Is Exactly a Registration-Rate Cap

**Date:** 2026-06-10
**Claim type:** narrow no_go (license-absence over the retained
record/measurement surface, with computed witnesses splitting the capacity
clause into two independently failing sub-clauses) + two narrow positive
lemmas (Lemma W second demand reduction `(BR) => (BR-int)`; Lemma C
conditional record-capacity theorem).
**Claim scope (narrow):** the single open clause left by the (NU)-license
note `OBSERVABLE_PRINCIPLE_P1_NU_LICENSE_FROM_RETAINED_SURFACE_NARROW_NO_GO_NOTE_2026-06-10.md`
— the premise

```text
(BR)  sup_{z>0} |z W'(z)| < infinity   (bounded log-scale response of the
      T1-d readout on the declared domain R_{>0}),
```

whose ratification alone would convert the conditional `p = 0` exponent
selection of the barrier-selector chain into an unconditional selection of
`log`. That note named this hunt's target shape: "an *adjacent finite
retained structure* (a record-capacity or finite-register enumeration)".
This note executes that hunt over the retained record rows
(`record_function_finite_sector_algebra`,
`record_unbounded_finite_additivity_schema`,
`magnitude_reads_minimal_record_block`) and the quantum effect-side rows
(Busch/Gleason/local tomography), and lands a split result:

> **(1) No-go (the honest core).** (BR) has **no retained record-capacity
> supplier**, and the candidate Route-A theorem — "any readout realized
> through the retained finite-sector record algebra has uniformly bounded
> log-scale response" — is **false**, with computed witnesses. Under record
> realization the capacity demand splits into two sub-clauses, and each
> fails **independently** on the retained surface: the per-sector magnitude
> cap (CAP-M) is violated by `W_Q = (z^2-1)/2` registered as a *single*
> sector per e-fold (bounded count `K = 1`, unbounded datum — the
> finite-sector algebra itself proves its sector data are arbitrary); the
> per-e-fold registration-rate cap (CAP-K) is violated by assigning `4^k`
> *unit* records to e-fold `k` (every datum exactly `1`, every prefix an
> exact finite disjoint collection `sum = (4^{K+1}-1)/3` — fully compliant
> with the retained unbounded-additivity schema, which **affirmatively
> licenses** arbitrary finite counts with no cap and no link to amplitude).
> The retained surface supplies bounded increments per *unit record* and
> unbounded totals per *collection*; (BR) needs a bound per *e-fold of
> amplitude*, and no retained row couples records to amplitude e-folds —
> that coupling is a quantitative slice of the record-scalar-map no-go's
> "middle arrow".
>
> **(2) Route-B kill (quantum, assessed at full strength).** Finite local
> dimension does bound the **per-register** datum: qubit effects have
> spectrum in `[0,1]`, so any Busch/Gleason frame-function value
> `Tr(sigma E)` lies in `[0,1]` (recomputed exactly) — an (CAP-M)-shaped
> fact, and even that is conditional on a *supplied* probability measure
> (the count-probability firewall blocks it as a supplier). The rate side
> cannot follow: `Z^3` supplies strictly increasing register counts
> `(2n+1)^3` with no cap (the retained schema's own mechanism), and the
> Busch/Gleason/tomography rows are effect-side — the readout `W` does not
> occur in their statements (readout-blind, the same structural class as
> the amplitude-side rows of the (NU) note).
>
> **(3) Demand reduction + conditional theorem (the campaign yield).**
> **Lemma W:** (BR) implies, and is strictly stronger than, the
> *increment* clause
>
> ```text
> (BR-int)  sup_{z>0} |W(e z) - W(z)| < infinity
> ```
>
> (strictness witness `W_V = log z + (sin z - sin 1)/(1 + log^2 z)`:
> e-fold increments bounded by `1 + 2(1 + sin 1) < 5`, response `zW'`
> unbounded along `z_m = 2 pi m`). (BR-int) **alone still point-selects
> `p = 0`** (e-fold increment `s e^{pu}(e^p-1)/p`, unbounded for every
> `p != 0`) and **escapes the extended irreducible class** by the same
> sin/cos witness family (recomputed). The demand ladder is now
> `(Add) => (NU) => (BR) => (BR-int)`, each implication strict.
> **Lemma C:** if the T1-d readout's e-fold increments are realized as
> finite-sector record readouts `I(A_z) = chi.v_z` (the retained identity,
> recomputed on all 81 ordered disjoint pairs) with `|v_i| <= M` (CAP-M)
> and at most `K` sectors per e-fold (CAP-K), then
> `sup|W(ez) - W(z)| <= K.M`: (BR-int) holds and `p = 0` is selected. In
> the retained unit-record schema (CAP-M) holds with `M = 1` **by the
> schema's own normalization** — so the entire open content is the
> realization clause plus the single rate cap (CAP-K).

**Result.** (BR) is **not derivable from the current retained surface**;
this note does NOT retire P1 and does NOT license (BR), (BR-int), or any
(CAP) clause. What it changes, monotonically, is the size and shape of the
open premise: from the analytic boundedness clause (BR) to the strictly
weaker increment clause (BR-int) (Lemma W), and — on the supplier side —
from "some finite-resolution structure" to the exactly named record form

```text
(CAP, open):  the T1-d readout's e-fold increments are realized through
the retained unit-record schema (CAP-real) with a uniform finite cap K on
registrations per e-fold of amplitude (CAP-K).
```

Lemma C then yields (BR-int) with constant `K`, and the selection chain
completes. Both remaining sub-clauses are open: (CAP-real) is a
quantitative slice of the forbidden middle arrow (so it must be supplied
or governed, never smuggled), and (CAP-K) has zero retained suppliers —
the retained schema licenses its violation. The next hunt, or the
governance decision, is now a single rate clause.

**Status authority:** independent audit lane only. This source note does
not set or predict an audit outcome; later status is generated by the
audit pipeline after independent review.
**Source-note proposal disclaimer:** this note is a source-note proposal;
audit verdict and downstream status are set only by the independent audit
lane.
**Primary runner:**
[`scripts/observable_principle_p1_br_license_check_2026_06_10.py`](../scripts/observable_principle_p1_br_license_check_2026_06_10.py)
(expected `TOTAL: PASS=31 FAIL=0`, exact SymPy, deterministic, < 5 s).

## 0. Honest framing and the precedent meta-move

This is wave 2 of the campaign that produced the barrier-selector note and
the (NU)-license note (both 2026-06-10, unaudited; every consumed fact is
recomputed here). The meta-move is unchanged (the Tier-A retirement
precedent): split the open premise into finite mechanically checkable
clauses; hunt, clause by clause, for an adjacent *already-retained* finite
structure that covers one clause; ship the residual strictly smaller.
Applied here: the hunted clause (BR) is first *weakened* to (BR-int)
(Lemma W — the selection survives), then *decomposed* under record
realization into (CAP-real) + (CAP-M) + (CAP-K) (Lemma C); the hunt finds
that the retained unit-record normalization covers (CAP-M) (`M = 1`)
within that realization class, and **fails with computed witnesses** on
(CAP-M)-general and on (CAP-K) — each independently. The admission is
smaller and sharper (one rate clause); it is not closed.

Scoping, stated precisely because the firewalls demand it: the clause
hunted here is **the response bound of whatever scalar readout T1-d
declares** — a property *of* the declared readout `W`, quantified over the
declared domain. This note does not construct, identify, or select that
readout; no probability law is constructed for records; no branch-to-scalar
map is asserted. The witness "realizations" below are hostile counter-
examples to supplier claims, not proposed readouts.

This note explicitly does NOT:

- retire P1, ratify (BR)/(BR-int)/(CAP), or alter Boundary T1-d;
- promote, demote, or predict the status of any cited row;
- construct a probability law for records or assert a branch-to-scalar
  map (Section 5);
- introduce a new framework axiom or repo vocabulary tag ("(BR-int)",
  "(CAP-real)", "(CAP-M)", "(CAP-K)" are local labels for clauses of this
  note's lemmas, not registry entries).

## 1. Inputs and licenses (one-hop)

| Input | Where used | License / status (ledger grades read 2026-06-10) |
|---|---|---|
| The (BR) clause, the exponent family `{s.g_p}`, the extended irreducible class and Lemma-R screening, the compact-collapse fact, the hunt-target naming | the target whose supplier is hunted; Sections 2–4 | `OBSERVABLE_PRINCIPLE_P1_NU_LICENSE_FROM_RETAINED_SURFACE_NARROW_NO_GO_NOTE_2026-06-10.md` — unaudited (landed 2026-06-10). Every consumed fact **recomputed in this note's runner**. |
| (NU) selector and its conditional theorem | campaign context only | `OBSERVABLE_PRINCIPLE_P1_EXPONENT_BARRIER_PARAMETER_SELECTOR_NARROW_THEOREM_NOTE_2026-06-10.md` — unaudited; presence + declared-unlicensed string checked (T9). |
| Irreducible class definition; the N7 hatch | what a selector must escape | `OBSERVABLE_PRINCIPLE_P1_EXPONENT_FIXING_IRREDUCIBILITY_NARROW_NOTE_2026-05-31.md` — `retained_no_go` (audited_clean). |
| Finite-sector record algebra: `I(A) = chi_A . v`, finite additivity over disjoint records, coarse-graining, the two-sector freedom (`d = p u/(1-p)`) | Lemma C's realization identity; the (CAP-M) no-go | `RECORD_FUNCTION_FINITE_SECTOR_ALGEBRA_2026-06-05.md` — `retained` (audited_clean). Identity **recomputed** on all 81 ordered disjoint subset pairs of a 4-sector model (runner T5); the freedom identity recomputed (T6). |
| Unbounded finite-additivity schema: `I(R_n) = n`, unit records, arbitrary finite collections via `Z^3`, "no intrinsic finite upper bound" | the unit normalization (`M = 1`) and the (CAP-K) no-go | `RECORD_UNBOUNDED_FINITE_ADDITIVITY_SCHEMA_2026-06-06.md` — `retained` (audited_clean). Geometric-prefix sums recomputed exactly (T6). |
| Record supplies no readout context / scale selector | the rate clause is not Record's to give | `MAGNITUDE_READS_MINIMAL_RECORD_BLOCK_2026-06-06.md` — `retained_no_go` (audited_clean): "durable finite realized records, no scale selector". |
| Record supplies no probability; counts are not a law | firewall wall (Section 5); blocks the Busch/Gleason measure hypotheses as suppliers | `POST_RECORD_COUNT_PROBABILITY_FIREWALL_2026-06-06.md` — `retained_no_go`. |
| No branch-to-scalar map from Record alone; free-monoid route: branch-to-word-length sizing is either a log coding rule ("which reintroduces the log") or a "bare integer count" not fixed by the axioms | firewall wall; the (CAP-real) classification | `OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md` — `retained_no_go`. |
| Finite certificates do not lift to unbounded laws | adjacent wall: no finite e-fold audit can certify the uniform cap | `POST_RECORD_FINITE_TO_UNBOUNDED_FAMILY_LIFT_NO_GO_2026-06-06.md` — `retained_no_go`. |
| Qubit effect-algebra measure `m(E) = Tr(sigma E)`; projection-lattice states; local tomography | Route B, assessed and killed (Section 4.3) | `BUSCH_POVM_EXTENSION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md` (`retained`), `GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md` (`retained`), `LOCAL_TOMOGRAPHY_FROM_QUBIT_COMPLEX_STRUCTURE_NARROW_THEOREM_NOTE_2026-06-03.md` (`retained_bounded`) — all audited_clean. The effect bound is **recomputed** on an exact rotated-effect family (T7); the rows are consumed as candidate suppliers being assessed, not as readout authorities. |
| T1-d wording (W function of `Z` alone, continuous, on all of `R_{>0}`) | the declared boundary the witnesses satisfy | `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` — unaudited parent; quoted as the declared boundary, not consumed as authority. |

No PDG values, no fitted constants, no numerical comparators, no
same-surface family arguments.

## 2. The positive half: Lemma W and Lemma C

### 2.1 Lemma W (second demand reduction): (BR) => (BR-int), strictly

**Statement.** In `u = log z`, `h(u) = W(e^u)`: if `sup|h'| < infinity`
(that is (BR)), then `sup_u |h(u+1) - h(u)| < infinity` (that is (BR-int)),
by the mean value theorem, with the same constant. The converse fails:

```text
W_V(z) = log z + (sin z - sin 1)/(1 + (log z)^2)
```

is smooth on `R_{>0}` with `W_V(1) = 0`; its perturbation `phi` obeys
`|phi| <= (1 + sin 1)/(1 + u^2)`, so every e-fold increment is bounded by
`1 + 2(1 + sin 1) < 5` — (BR-int) holds — while at `z_m = 2 pi m`
(`sin(2 pi m) = 0`, `cos(2 pi m) = 1` exactly)

```text
z W_V'(z_m) = 1 + [2 pi m (1 + L^2) + 2 L sin 1]/(1 + L^2)^2,  L = log(2 pi m),
```

which exceeds every cap (runner T4: `> 10, 100, 1000` at
`m = 10^2, 10^4, 10^6`; the exact value at `m = 10^6` is `~2.55 x 10^4`).
(BR) fails. ∎

**(BR-int) is still a point-selector (runner T2).** On `{s.g_p}` the
e-fold increment is exactly `s e^{pu}(e^p - 1)/p`: unbounded as
`u -> +infinity` for `p > 0` (including the linear member `p = 1` — no
curvature leg), unbounded as `u -> -infinity` for `p < 0`, and identically
`s` for `p = 0`. Pass set: exactly `{p = 0}`; rescaling cannot rescue any
`p != 0`.

**(BR-int) escapes the extended irreducible class (runner T3).** The same
sin/cos witness family as for (NU)/(BR): both witnesses pass (BR-int)
(their increments are bounded — the cos witness exactly by
`1 + (1/5) sin(1/2) < 11/10`), while for every nondegenerate pair some
witness violates the additive identity there (residuals recomputed: at
`(e, e)`, at `(e, 1/e)`, the small-`omega` expansion
`-eps.omega^3 u_1 u_2 (u_1+u_2)/2`, and the `u_1 + u_2 = 0` slice covered
by the cos witness). By the Lemma-R screening criterion, (BR-int) entails
no additive-identity instance: outside the extended class.

**The demand ladder, all strict (runner T4).**

```text
(Add) ==> (NU) ==> (BR) ==> (BR-int)
```

with strictness witnesses: the cos witness ((NU) without (Add)); `W_F =
log((z + 1/z)/2)` ((BR) without (NU): curvature vanishes at
`tanh u_0 = (sqrt 5 - 1)/2` with `zW' != 0`, `sup|zW'| = 1`); `W_V`
((BR-int) without (BR)). Each rung point-selects `p = 0`; (BR-int) is the
weakest tested clause that still does. The minimal missing license shrinks
again.

### 2.2 Lemma C (conditional record-capacity theorem — Route A's honest yield)

**Premises (all declared, none retained as a package).**

- **(CAP-real)** for every `z > 0` the e-fold increment `W(ez) - W(z)`
  equals the finite-sector readout `I(A_z) = chi.v_z` of a finite disjoint
  record collection registered for that e-fold (the retained finite-sector
  identity supplies the *algebra* of such readouts; it does not supply the
  association `z -> A_z` — see Section 4.1);
- **(CAP-M)** every registered sector datum obeys `|v_i| <= M`;
- **(CAP-K)** every e-fold collection has at most `K` sectors.

**Conclusion.** `|W(ez) - W(z)| = |sum_{i in A_z} v_i| <= K.M` for every
`z` (finite additivity + triangle inequality, runner T5), i.e. (BR-int)
holds with constant `K.M`; by Lemma W's selection leg the pass set on
`{s.g_p}` is exactly `{p = 0}`. ∎

**Unit-record normalization.** In the retained unbounded-additivity
schema every unit record contributes exactly `1`, so (CAP-M) holds there
with `M = 1` *by the schema's own normalization* (runner T5). Hence within
unit-record realizations the entire open content of (BR) is
**(CAP-real) + (CAP-K)** — the realization clause and one rate cap. This
is the physical reading the barrier note gestured at ("the readout
resolves the amplitude domain with finitely many distinguishable units"),
now as a precise conditional theorem: **one e-fold of source change may
register at most a bounded record increment** is exactly (CAP-K) given
the schema's unit normalization, and it selects the logarithm.

## 3. The no-go: the candidate Route-A theorem is false, sub-clause by sub-clause

The hunted candidate was: *"any readout realized through the retained
finite-sector record algebra has uniformly bounded log-scale response on
the licensed domain."* This is **false**; the capacity caps are doing all
the work, and neither cap is retained. The witnesses (runner T6) satisfy
every formalized retained constraint (functions of `Z` alone, continuous
on `R_{>0}`, `W(1) = 0`, exact finite additivity on every registered
collection):

| Witness realization | (CAP-M) | (CAP-K) | (BR-int)/(BR) | kills |
|---|---|---|---|---|
| `W_Q = (z^2-1)/2`, one sector per e-fold, datum `z^2(e^2-1)/2` | **fails** (datum unbounded) | holds (`K = 1`) | fail | any claim that the finite-sector algebra alone bounds the response: the algebra's own two-sector freedom (`d = p u/(1-p)`, normalized coordinate exactly `p`, recomputed) proves sector data are arbitrary — "Record alone cannot select a value" |
| `4^k` unit records assigned to e-fold `k` | holds (`M = 1`, every datum exactly `1`) | **fails** (count `4^k` exceeds any cap; `4^10 > 10^6`) | fail | any claim that the unbounded-additivity schema bounds the rate: the schema **licenses** arbitrary finite collections (`I(R_n) = n`, "no intrinsic finite upper bound"; prefix sums `(4^{K+1}-1)/3` exact) and contains no amplitude coupling |

The two sub-clauses fail independently — exactly parallel to the
`W_G`/`W_Q` split of the (NU) note's clauses (ii)/(iii). Since nothing
retained excludes either witness realization, no retained row (nor any
conjunction) entails (CAP-M)-general, (CAP-K), or therefore (BR)/(BR-int).

## 4. Why each candidate supplier class fails (structurally)

### 4.1 The record rows: right algebra, no amplitude coupling, no caps

The finite-sector algebra row is *deliberately* cap-free: its own text
proves the two-sector normalized coordinate is arbitrary ("Thus Record
alone cannot select a value"), and its sector data are supplied scalars
with no magnitude constraint. The unbounded-additivity schema is
*affirmatively anti-cap*: its content is that finite additivity over
arbitrary finite collections has "no intrinsic finite upper bound", with
`Z^3` supplying arbitrarily large index sets. And the magnitude-block
no-go (`retained_no_go`) states Record supplies "no scale selector" — no
readout context, weighting, or scale. So the retained record surface
supplies: bounded increments per **unit record**, unbounded totals per
**collection**, and **no association between records and amplitude**. (BR)
needs a bound per **e-fold of amplitude**. The missing association
(CAP-real) is a quantitative slice of the record-scalar-map no-go's middle
arrow — its free-monoid route already names the two faces of any such
sizing: a log coding rule ("which reintroduces the log" — consistent with,
not circular for, the selection theorem, since (CAP) assumes only a bound,
not the log form) or a "bare integer count" not fixed by the axioms. The
missing cap (CAP-K) has no retained carrier at all (runner T9 scan).

### 4.2 The adjacent wall (cap certification)

Even the *audit shape* of a future (CAP-K) supplier is constrained: the
retained finite-to-unbounded family-lift no-go blocks deriving an
unbounded-domain law from finitely many post-record checks ("finite
post-record certificate alone => unbounded retained law" is not a valid
route). A (CAP-K) supplier must therefore be a structural/schema row (a
per-e-fold capacity *principle*), not a finite certificate — this is
recorded so the next hunt does not waste a cycle on certificate-shaped
candidates (runner T6).

### 4.3 Route B (quantum), assessed at full strength and killed (runner T7)

Steelman: "the per-site algebra is finite-dimensional (one qubit,
U4-closed); finite local dimension bounds the per-record information
increment; the retained Busch/Gleason/tomography rows carry exactly this
boundedness." Assessed:

1. **The M-side is real but conditional and M-shaped only.** Qubit
   effects `0 <= E <= I` have spectrum in `[0,1]`; for any density
   `sigma`, `Tr(sigma E) in [0,1]` — recomputed exactly on a rotated
   effect family (multilinear corner argument). So each *register* yields
   a bounded datum. But as a frame-function statement this is conditional
   on a **supplied** normalized measure (the Busch row's (M1)–(M3)
   hypotheses) — a probability path on records, blocked as a supplier by
   the count-probability firewall. Even granted gratis, it supplies only
   (CAP-M), which the unit-record normalization already covers.
2. **The K-side cannot follow.** `Z^3` supplies strictly increasing
   register counts `(2n+1)^3` with no cap (recomputed; this is the
   retained schema's own unboundedness mechanism). Bounded-per-register
   times unboundedly-many-registers gives no per-e-fold bound; the
   missing input is again the amplitude-to-register rate — (CAP-K).
3. **Readout-blindness.** The Busch/Gleason/tomography statements
   constrain states and effects (`m(E) = Tr(sigma E)`, projection-lattice
   measures, state identification from local data); the readout `W` does
   not occur in them (runner string-proxy + structural classification), so
   they are satisfied identically by every candidate `W` and cannot
   discriminate (BR) from its violations — the same readout-blind class as
   the amplitude-side rows of the (NU) note.

### 4.4 The precise missing clause (the next hunt's target, or the governance spec)

```text
(CAP-K license, open):  retained-grade structure forcing a uniform finite
cap on record registrations per e-fold of amplitude, together with the
realization clause (CAP-real) associating the T1-d readout's e-fold
increments with registered collections.
```

Given the retained unit normalization (`M = 1`), Lemma C then yields
(BR-int) with constant `K` and the exponent selection completes. If
admitted by governance instead, the admission spec is minimal: one rate
cap plus one realization clause, both named, with the witness pair of
Section 3 certifying that nothing weaker suffices.

## 5. Firewall compliance (explicit)

- **Count-probability firewall (`retained_no_go`) — respected:** no
  probability law is constructed for records anywhere in this note or
  runner. The Busch/Gleason measure hypotheses are consumed only inside
  the assessment that Route B fails (and are flagged there as the
  firewall-blocked bridge); realized counts (`4^k`, `I(R_n) = n`) are used
  as exact finite readouts, never promoted to frequencies or laws.
- **Record-scalar-map no-go (`retained_no_go`) — respected:** no
  branch-to-scalar map is asserted. The hunted clause is the response
  bound of whatever scalar readout T1-d declares; the realization clause
  (CAP-real) is **declared as part of the open premise** precisely because
  asserting it would be the forbidden middle arrow; the witness
  realizations are hostile counterexamples to supplier claims, not
  proposed readouts; no readout is identified.

## 6. What T1-d / P1 becomes

Unchanged in status: P1 is **not** retired; T1-d is **not** edited. The
open premise's shape sharpens monotonically:

- after the barrier note: the two-clause barrier condition (NU);
- after the (NU)-license note: the single boundedness clause (BR);
- after this note: on the demand side, the strictly weaker increment
  clause (BR-int) — bounded readout increment per e-fold, still a
  point-selector, still outside the irreducible class; on the supplier
  side, the exact record form (CAP-real) + (CAP-K) with (CAP-M) covered
  at `M = 1` by the retained unit-record normalization, and with both
  record routes and the quantum route shown unable to supply the rate
  clause (witnessed, not only keyword-scanned). The admitted-premise
  count is unchanged; the premise is smaller and now names one cap.

## 7. No-Go Discipline Gate (for the license-absence half)

**N1 — Alternative route enumeration.**

| Candidate supplier route | Marker | Outcome |
|---|---|---|
| Finite-sector record algebra (the named hunt target) | ATTEMPTED | algebra recomputed; cap-free by its own freedom identity; `W_Q` single-sector witness (T6) — supplies the realization *algebra* (consumed in Lemma C), not the caps |
| Unbounded finite-additivity schema (unit records) | ATTEMPTED | supplies (CAP-M) at `M = 1` by normalization (T5) — and affirmatively licenses (CAP-K) violations (`4^k` witness, T6) |
| Magnitude minimal-record-block row | RULED OUT BY ITS OWN STATEMENT | it is a `retained_no_go`: Record supplies "no scale selector" — confirms the gap, supplies nothing |
| Busch/Gleason/local-tomography (Route B) | ATTEMPTED (steelmanned) | M-shaped fact only, probability-conditional (firewall), readout-blind; no rate (T7) |
| Finite e-fold certificates | RULED OUT BY ADJACENT WALL | finite-to-unbounded family-lift `retained_no_go` (T6) |
| Ledger keyword sweep (extended: capacity/rate/resolution/response) | ATTEMPTED | zero retained-grade matches (T9) |
| Governance ratification of (CAP) (or directly of (BR)/(BR-int)) | OPEN (named, spec'd minimal in 4.4) | not a derivation; owner/audit lane decision |

**N2 — Wall-independence.** Two independent walls: (i) the retained
record surface is cap-free in two independent directions (magnitude and
rate — separate witnesses); (ii) the probability/branch-map firewalls
block the only quantum row carrying a bound. The witnesses cut both walls.

**N3 — Hidden-wall scan.** "(BR-int)", "(CAP-real)", "(CAP-M)", "(CAP-K)"
are local labels of this note, defined in-text; the mean value theorem and
triangle inequality are standard mathematics with every consumed instance
reproven in the runner. No retained status is asserted for the two
2026-06-10 campaign notes (unaudited; everything consumed is recomputed).

**N4 — Residual matching.** The residual attacked is exactly the (NU)
note's Section 4.4 open clause: retained-grade structure forcing bounded
log-scale response. The selection theorem, the class escape, and the
ladder are not weakened — they are extended one rung down to (BR-int).

**N5 — Rhetoric audit.** No claim that P1 is closed, that any (CAP)
clause holds, or that the record/effect rows are deficient — they are
correct on their subjects; the no-go is that their subjects include
neither an amplitude coupling nor a rate cap.

**N6 — Partial-closure path scan.** Named paths: (a) a future retained
per-e-fold capacity principle supplying (CAP-K) (+ the realization clause)
— Lemma C then completes the selection; (b) governance ratification of
(CAP) or (BR-int) directly (minimal spec in 4.4); (c) a future derivation
coupling amplitude e-folds to register counts from dynamics rows — which
would have to enter through the record-scalar-map no-go's named escape
(its N6: owner-approved primitive, admission, or later derivation), not
around it.

**N7 — Steelman.** Strongest objection: "the unit-record schema *does*
bound the increment per record at 1, and finite local dimension bounds
each register — surely boundedness per e-fold follows for any *physical*
readout." Response: quantified and refuted — boundedness per record times
unboundedly many records per e-fold is unbounded per e-fold, and the
retained schema itself licenses the unbounded assignment (`4^k` witness,
exact); the inference needs precisely the rate cap, which is the named
open clause, not a consequence. Second steelman: "(BR-int) is weaker than
(BR), so the note trades a clean analytic clause for a record-flavored
one." Response: (BR-int) is proven strictly weaker *and* still selecting
(Lemma W, witness `W_V`) — a monotone improvement on the demand side
independent of any record language; the record decomposition is the
supplier-side analysis and is kept separate.

**N8 — Cross-cycle echo.** The (NU) note's echo was "retained positivity
is amplitude-side; readout-side second-order structure has never been
retained." This note adds the record-side dual: *retained record structure
is per-record bounded but per-collection unbounded, and carries no
amplitude coupling* — the same middle-arrow lesson, now at the level of
capacity rates. The Pattern-L wall is not re-litigated: (BR-int) is proven
outside it (T3), extending the escape to the weakest rung yet.

## 8. Reproduction

```bash
python3 scripts/observable_principle_p1_br_license_check_2026_06_10.py
```

Expected output (matches stdout):

```text
== T1: the clause under hunt — (BR) and its selection chain, recomputed ==
  [PASS][A] family normalization: g_p(1) = 0, g_p'(1) = 1, p -> 0 limit is log z (selected member)
  [PASS][A] log-scale response identity: z*(s g_p)' = s z^p exactly; log passes (BR) with sup|zW'| = |s|
  [PASS][A] (BR) selection chain recomputed: pass set on {s*g_p} over p in {0, 2, 1, 1/2, -1/2} is exactly {p = 0} (rescaling cannot rescue: |s| is linear, z-unboundedness s-invariant)
== T2: Lemma W — second demand reduction (BR) => (BR-int), and (BR-int) still point-selects ==
  [PASS][A] e-fold increment identity: s*(g_p(e^{u+1}) - g_p(e^u)) = s e^{pu}(e^p - 1)/p exactly
  [PASS][A] p != 0 increments unbounded (p > 0 at u -> +oo, p < 0 at u -> -oo; includes the linear member p = 1 with no curvature leg); p = 0 increment identically s
  [PASS][A] (BR) => (BR-int) verified (mean value): log has increment = s = sup|zW'| (equality); cos witness increment = 1 - (1/5) sin(1/2) sin(u + 1/2), so sup-increment 1 + (1/5) sin(1/2) <= sup|h'| = 11/10  (<=> 2 sin(1/2) <= 1)
  [PASS][A] (BR-int) selection: pass set on the family is exactly {p = 0} — the strictly weaker increment clause is still a point-selector
== T3: (BR-int) escapes the extended irreducible class (witness family recomputed) ==
  [PASS][A] cos witness passes (BR-int) (sup-increment <= 1 + (1/5) sin(1/2) < 11/10) yet violates the additive identity at (e, e) AND at the reciprocal pair (e, 1/e): residuals nonzero  -- res(e,e)=-0.049675, res(e,1/e)=0.091940
  [PASS][A] sin witness ((BR-int)-passing: increments of u + eps sin(omega u) bounded by 1 + 2|eps|): additive residual -eps omega^3 uA uB (uA+uB)/2 + O(omega^5); cos witness covers the uA + uB = 0 slice (residual 2 eps (1 - cos(omega uA)) != 0) — (BR-int) entails NO additive-identity instance at any nondegenerate pair: outside the extended class
== T4: strictness — W_V separates (BR-int) from (BR); the full demand ladder ==
  [PASS][A] W_V = log z + (sin z - sin 1)/(1 + log^2 z): W_V(1) = 0, smooth on R_>0; |phi| <= (1 + sin 1)/(1 + u^2) <= 1 + sin 1, so every e-fold increment is bounded by 1 + 2(1 + sin 1) < 5: (BR-int) HOLDS
  [PASS][D] yet (BR) FAILS for W_V: at z_m = 2 pi m (sin(2 pi m) = 0, cos(2 pi m) = 1 exactly), z W' = 1 + [2 pi m (1+L^2) + 2 L sin 1]/(1+L^2)^2, L = log(2 pi m) — exceeds caps 10/100/1000 at m = 1e2/1e4/1e6: response unbounded, so (BR-int) is STRICTLY weaker  -- zW'(2pi*1e6) = 25539.4
  [PASS][A] demand ladder (Add) => (NU) => (BR) => (BR-int), ALL strict: (Add)+cont => c log z with nu = |c| (in class); cos witness has (NU) w/o (Add) (curvature -1 - (sqrt2/10) cos(u+pi/4) constant sign); W_F = log((z+1/z)/2) has (BR) w/o (NU) (curvature zero at tanh u0 = (sqrt5-1)/2 with zW' != 0, sup|zW'| = 1); W_V has (BR-int) w/o (BR)
== T5: Lemma C — the conditional record-capacity theorem (Route A's honest yield) ==
  [PASS][C] retained finite-sector identity recomputed (not cited blind): I(A) = chi_A . v and I(A u B) = I(A) + I(B) on ALL 81 ordered disjoint subset pairs of a 4-sector model  -- pairs=81
  [PASS][A] capacity bound: |I(A_z)| = |sum v_i| <= K*M by finite additivity + triangle inequality (extremal instance sum = 5M = K*M; mixed-sign instance |7M/6| <= 5M, K = 5)
  [PASS][A] Lemma C chain: (CAP-real)+(CAP-M)+(CAP-K) => every e-fold increment <= K*M => (BR-int) => pass set exactly {p = 0} (selection completed conditionally — the gap is exactly the caps)
  [PASS][A] unit-record normalization: in the retained unbounded-additivity schema every unit datum is exactly 1, so (CAP-M) holds there with M = 1 by normalization (I(R_7) = 7 recomputed); the open content is the realization clause + the rate cap (CAP-K)
== T6: the no-go — neither capacity sub-clause has a retained supplier (witnesses) ==
  [PASS][D] (CAP-M) unsupplied for general sector data: the finite-sector algebra's own freedom recomputed — for ANY p in (0,1), d = p u/(1-p) gives normalized coordinate d/(u+d) = p exactly: sector data are arbitrary scalars, no magnitude cap is retained
  [PASS][D] witness W_Q = (z^2-1)/2 registered as ONE sector per e-fold (K = 1 bounded!): satisfies the finite-sector algebra verbatim (singleton decomposition, additivity trivially exact) yet its e-fold increment z^2 (e^2-1)/2 -> oo: bounded count + unbounded datum kills any 'the algebra alone bounds the response' claim
  [PASS][D] (CAP-K) unsupplied — and the schema affirmatively licenses its violation: assign 4^k UNIT records to e-fold k (M = 1 holds); every prefix is an exact finite disjoint collection (sum_{k<=K} 4^k = (4^{K+1}-1)/3 recomputed), yet the per-e-fold count 4^k exceeds ANY cap (4^10 = 1048576 > 10^6): a fully schema-compliant unit-record realization violates (BR-int) — the sub-clauses fail independently (W_Q: K fine/M unbounded; 4^k: M = 1/K unbounded)  -- 4^10 = 1048576
  [PASS][B] adjacent retained wall agrees: the finite-to-unbounded family-lift no-go (retained_no_go) blocks certifying the uniform cap from finitely many e-fold checks ('finite post-record certificate alone => unbounded retained law' is not a valid route)
== T7: Route B (quantum) — finite local dimension gives an M-shaped fact, never the rate ==
  [PASS][C] qubit effect bound (per-register datum): effects on M_2 have spectrum in [0,1]; for any density sigma the value Tr(sigma E) is multilinear in (a, b, q) and lies in [0,1] at all 8 corners (so on the whole box) — bounded per-register increment, an (CAP-M)-shaped fact; NOTE: as a Busch/Gleason frame-function statement it is conditional on a SUPPLIED probability measure (count-probability firewall: blocked as a supplier)
  [PASS][C] the K-side cannot follow from finite local dimension: Z^3 supplies strictly increasing register counts (2n+1)^3 (derivative 6(2n+1)^2 > 0; (2*50+1)^3 = 1030301 > 10^6) with no cap — per-site boundedness times unbounded site count yields NO per-e-fold cap; no retained row couples amplitude e-folds to register counts
  [PASS][B] effect-side rows are readout-blind: Busch/Gleason/local-tomography notes present, their subject is the effect/state measure (Busch note's load-bearing direction is m(E)=Tr(sigma E)), and none of them contains readout-response vocabulary — the readout W does not occur in their statements, so they cannot discriminate (BR) from its violations
== T8: falsification legs — compact collapse and the granted-clause completion ==
  [PASS][D] compact collapse: on [1, e] and on the licensed L2 Neumann image [1, 85/64] every member has finite response and finite e-fold increment (monotone endpoint evaluation) — (BR)/(BR-int)/(CAP) select NOTHING there; the full-R_>0 clause is exactly the declared T1-d / lemma-L3 domain hypothesis, no hidden domain freedom
  [PASS][D] granting the missing capacity clauses completes the selection exactly: with (CAP-M)+(CAP-K) granted the pass set is {p = 0} and W = c log z follows with T1-d's remaining clauses — the missing license is the single load-bearing gap
== T9: ledger scan — zero retained-grade capacity/rate suppliers (extends NU-note T9) ==
  [PASS][B] extended ledger scan: ZERO retained-grade rows match capacity/rate/resolution/response-bound vocabulary — (BR), (BR-int), and the (CAP) clauses are all unlicensed  -- matches=[]
  [PASS][B] cited rows present at the cited effective statuses (one-hop, presence check)
  [PASS][B] the three candidate record-capacity suppliers are audited_clean (assessed at full strength, not strawmanned)
  [PASS][B] campaign chain on disk: the (NU)-license note names this hunt's target shape ('record-capacity or finite-register') and the barrier note declares its premise unlicensed
== T10: note honest-scope, firewall-compliance, and boundary strings ==
  [PASS][B] note honest-scope and firewall-compliance strings present  -- missing=[]
  [PASS][B] forbidden promotion strings absent  -- found=[]

TOTAL: PASS=31 FAIL=0
```

A passing run supports only: (i) Lemma W (the (BR) => (BR-int) reduction
with strictness witness `W_V`), the (BR-int) point-selection, and the
class escape; (ii) Lemma C (the conditional capacity theorem) and the unit
normalization fact; (iii) the witnessed absence of any retained supplier
for (CAP-M)-general, (CAP-K), and hence (BR)/(BR-int); (iv) the Route-B
kill; (v) the ledger and boundary facts. It does **NOT** retire P1, does
**NOT** license (BR), (BR-int), or (CAP), and does **NOT** promote any
row.

## 9. Cross-references

- `OBSERVABLE_PRINCIPLE_P1_NU_LICENSE_FROM_RETAINED_SURFACE_NARROW_NO_GO_NOTE_2026-06-10.md`
  — the target: its open clause (BR) is the hunted license; its hunt-target
  naming is executed here; its demand ladder is extended one strict rung.
- `OBSERVABLE_PRINCIPLE_P1_EXPONENT_BARRIER_PARAMETER_SELECTOR_NARROW_THEOREM_NOTE_2026-06-10.md`
  — campaign context; conditional selector intact, now reachable from the
  weaker (BR-int).
- `OBSERVABLE_PRINCIPLE_P1_EXPONENT_FIXING_IRREDUCIBILITY_NARROW_NOTE_2026-05-31.md`
  — the retained_no_go defining the class (BR-int) escapes.
- `RECORD_FUNCTION_FINITE_SECTOR_ALGEBRA_2026-06-05.md` — supplies the
  realization algebra consumed by Lemma C; cap-free by its own freedom
  identity (recomputed).
- `RECORD_UNBOUNDED_FINITE_ADDITIVITY_SCHEMA_2026-06-06.md` — supplies the
  unit normalization (`M = 1`); affirmatively licenses the (CAP-K)
  violation witness.
- `MAGNITUDE_READS_MINIMAL_RECORD_BLOCK_2026-06-06.md` — the retained_no_go
  confirming Record supplies no readout scale.
- `POST_RECORD_COUNT_PROBABILITY_FIREWALL_2026-06-06.md`,
  `OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md` — the
  walls; compliance stated in Section 5.
- `POST_RECORD_FINITE_TO_UNBOUNDED_FAMILY_LIFT_NO_GO_2026-06-06.md` — the
  adjacent wall constraining future (CAP-K) supplier shapes.
- `BUSCH_POVM_EXTENSION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`,
  `GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`,
  `LOCAL_TOMOGRAPHY_FROM_QUBIT_COMPLEX_STRUCTURE_NARROW_THEOREM_NOTE_2026-06-03.md`
  — Route-B candidate suppliers, assessed and killed (Section 4.3).
- `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` — T1-d domain clause quoted as
  the declared boundary (context only).

### Source-note boundary

**Hypothesis set used:** (1) the normalized exponent family `{s.g_p}` on
the real-positive branch (parametrization, elementary, recomputed); (2)
Lemma W (mean value theorem instance-verified; increment identities exact;
strictness witness exact); (3) Lemma C (finite additivity + triangle
inequality, instance-verified; its (CAP) premises declared, never asserted
as supplied); (4) the witness computations (elementary, exact); (5) the
T1-d/L3 full-`R_{>0}` domain clause — declared by the parent chain,
consumed as the declared boundary it already is, with its load-bearing
role re-quantified (compact collapse); (6) ledger reads
(presence/status checks only). Throughout: no probability law is
constructed; no branch-to-scalar map is asserted; no readout is
identified; the hunted clause is
the response bound of whatever scalar readout T1-d declares.

**Forbidden-imports check:** no new framework axiom; no new repo
vocabulary tag; no PDG/fitted/observed values; no status promotion or
prediction for any row.

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any cited row. The independent audit lane is the only
status authority.

## Changelog

- **2026-06-10** — initial note. (BR)-license hunt over the retained
  record/measurement surface (wave 2 of the P1 exponent campaign): no-go
  (the candidate record-capacity theorem is false as stated; capacity
  splits into (CAP-M)/(CAP-K), each independently unsupplied — witnessed
  by the single-sector `W_Q` realization and the `4^k` unit-record rate
  assignment, both exactly compliant with the retained rows); Route B
  killed (qubit effect bound recomputed: M-shaped, probability-conditional,
  readout-blind rows; `Z^3` register growth defeats the rate); Lemma W
  second demand reduction `(BR) => (BR-int)` with strictness witness
  `W_V`, (BR-int) point-selection and class escape, ladder
  `(Add) => (NU) => (BR) => (BR-int)` all strict; Lemma C conditional
  capacity theorem (`sup-increment <= K.M`) with the unit-record
  normalization covering (CAP-M) at `M = 1`. Runner
  `TOTAL: PASS=31 FAIL=0`. P1 not retired; nothing ratified; next hunt
  target named: a retained per-e-fold registration-rate cap (CAP-K) plus
  the realization clause (CAP-real).
