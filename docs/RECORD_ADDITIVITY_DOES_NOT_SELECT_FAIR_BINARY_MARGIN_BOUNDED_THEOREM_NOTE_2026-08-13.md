---
claim_id: record_additivity_does_not_select_fair_binary_margin_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "Scalar Record additivity on formed unit binary records supplies only the integer count I of 1-contents, which cannot equal the law-level fair margin p=1/2 on the executed family, and the possible I values do not distinguish p=1/3 from p=1/2; the note does not install fairness or claim that no fair compiler exists."
upstream_dependencies:
  - minimal_axioms
runner: scripts/record_additivity_does_not_select_fair_binary_margin_2026_08_13.py
---

# Record Additivity Does Not Select The Fair Binary Margin

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** finite exact algebra of scalar Record additivity on formed unit
binary records versus a one-site Bernoulli margin `p`.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/record_additivity_does_not_select_fair_binary_margin_2026_08_13.py`](../scripts/record_additivity_does_not_select_fair_binary_margin_2026_08_13.py)

## Result Up Front

A physical compiler of formed bits still needs a fair binary margin
`p=1/2` after a product law is granted as a comparison object. This note
does not install fairness and does not claim that no fair compiler exists.

The current Record axiom in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies a
content-only additive scalar on finite pairwise-disjoint record collections:

> A readout value is determined by record content alone.
> For any finite collection of pairwise-disjoint records, scalar readout
> `I` is additive, with `I(empty)=0`.

The current Admissibility axiom supplies a one-site law over possibilities:

> For each site, the probability distribution over the possibilities is
> determined by, and varies with, the nearest-neighbor conditions.

The matching interpretive reading note, non-governing, says that the
distribution concerns which possibility a forming record locks, conditional
on formation at that site; it does not supply the formation site,
probability, or rate. That sentence is about formation, not about a unique
Bernoulli margin on a binary menu.

If a record forms and locks content `c∈{0,1}` at unit strength, content-only
readout of that atom is `c`. For `n` formed pairwise-disjoint unit binary
records, `I` is the number of `1`-contents, so `I∈{0,1,...,n}`. Declared
comparison margins are `p∈{0,1/3,1/2,1}`, with `P(content=1)=p`.

Record additivity therefore supplies an integer count of locked content.
That count is not the law-level margin `p`. Every Bernoulli law on a binary
menu is compatible with the same possible `I` values whenever `p∈(0,1)`.
Fairness `p=1/2` is not a Record readout.

## Machine Status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "On the executed formed binary family, Record I is an integer count and cannot equal p=1/2. The possible I values do not distinguish p=1/3 from p=1/2. Expectation n p is a law-level number, not a Record readout."
trace_class: negative_route_pruning
target_claim_id: fair_binary_margin_compiler
target_blocker_text: "remaining compiler residual is record formation at those sites and a fair binary margin"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "A physical selector for p=1/2, or a formation process whose typical I/n converges to 1/2, remains open; do not adopt axiom text."
conditional_surface_status: "exact for I∈{0,...,n} versus p=1/2 on the executed family; fairness remains a live law-level selector"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Work with finite formed record collections in the sense of the Record axiom.
A **binary content menu** is `{0,1}` for a formed record of unit strength.
A **one-site binary law** is a Bernoulli parameter `p∈[0,1]`:
`P(content=1)=p`. That parameter is a law-level number. It is not Record
content.

If a record forms and locks content `c∈{0,1}`, content-only readout of that
atom is `c`. Write `I_of_bits(c_1,...,c_n)` for the additive scalar on `n`
formed pairwise-disjoint unit bits. Additivity and `I(empty)=0` force

`I_of_bits(c_1,...,c_n)=c_1+...+c_n∈{0,1,...,n}`.

A **declared comparison family** is `n` formed bits carrying a common
one-site Bernoulli parameter `p`. Product structure is a comparison object,
not an axiom consequence. The executed family is `n=3` together with the
one-bit case `n=1`. Declared comparison margins are

`p∈{0, 1/3, 1/2, 1}`.

Write `bernoulli_I_support(n,p)` for the set of `I` values with positive
Bernoulli mass. For `p∈(0,1)` that set is `{0,1,...,n}`. The degenerate
endpoints are content-support facts: `p=0` has `I=0` almost surely, and
`p=1` has `I=n` almost surely. Those facts are not fairness.

| pair | unit realization | `I` | equals `1/2`? |
|---|---|---|---|
| one bit, content `0` | `{c=0}` | `0` | no |
| one bit, content `1` | `{c=1}` | `1` | no |
| three bits, all `0` | `(0,0,0)` | `0` | no |
| three bits, one `1` | e.g. `(1,0,0)` | `1` | no |
| three bits, two `1` | e.g. `(1,1,0)` | `2` | no |
| three bits, all `1` | `(1,1,1)` | `3` | no |

On the executed `n=3` family the finite-sample ratios are

`I/3∈{0, 1/3, 2/3, 1}`.

The fair margin `1/2` is not in that set. The law-level expectation
`E[I]=n p` equals `3/2` at `p=1/2` and is not a realized `I`.

## Exact Target And Obligation Graph

**Exact target.** Decide whether the additive scalar `I` on a finite formed
binary collection can equal, or select, the law-level fair margin `p=1/2`.

| Obligation | Role | Disposition |
|---|---|---|
| pin content-only readout and disjoint additivity | premise | quoted from the axiom memo |
| pin the Admissibility distribution sentence | premise | quoted from the axiom memo |
| pin the reading note's formation-rate sentence | interpretive, non-governing | quoted; it does not name a unique `p` |
| show one-bit `I∈{0,1}` | Theorem 1 | content-only additivity |
| show `n=3` `I∈{0,1,2,3}` | Theorem 2 | count of `1`-contents |
| show open margins share `I`-support | Theorem 3 | Bernoulli mass on `{0,...,n}` |
| separate `E[I]=n p` from realized `I` | Theorem 4 | expectation is extra |
| scoped negative: no Record function of `I` is `1/2` on the executed family | Theorem 5 | N-gate |
| install fairness or claim no fair compiler exists | non-claim | not attempted |
| derive a physical selector for `p=1/2` | autonomous closure | open |

## Theorem 1 — `I` Of One Formed Bit Is Not `p`

Let one formed unit binary record lock content `c∈{0,1}`. Content-only
readout and additivity give

`I_of_bits((c))=c∈{0,1}`.

The declared open margins include `p=1/3` and `p=1/2`. Neither value lies in
`{0,1}`. Therefore `I` cannot equal `p` when `p∈{1/3,1/2}`. In particular
fairness `p=1/2` is not a Record readout of one formed bit.

The one-bit witnesses are exact:

`I(0)=0`, `I(1)=1`, and neither equals `1/2`.

## Theorem 2 — `n` Formed Bits: `I` Is A Count

Let `n=3` formed pairwise-disjoint unit bits lock contents
`(c_1,c_2,c_3)∈{0,1}^3`. Additivity gives

`I_of_bits((c_1,c_2,c_3))=c_1+c_2+c_3∈{0,1,2,3}`

regardless of the declared comparison margin `p`. In particular `I` is never
`1/2` and never `1/3`. The same count set is obtained from every declared
`p`, including the degenerate endpoints, because every `0/1` triple is a
possible content tuple; law-level masses may vanish only at those endpoints,
which Theorem 3 isolates as support facts.

Thus `I` on the executed three-bit family is an integer count of locked
`1`-contents. It is not a fractional margin.

## Theorem 3 — Same `I`-Support For Open Margins

Fix `n=3` and a declared Bernoulli parameter `p`. The mass of the count
`I=k` is the exact binomial value

`P(I=k)=C(3,k) p^k (1-p)^{3-k}`.

For every `p∈(0,1)` each mass is strictly positive, so

`bernoulli_I_support(3,p)={0,1,2,3}`.

The two open comparison margins therefore share support:

`supp_I(p=1/3)=supp_I(p=1/2)={0,1,2,3}`.

The possible Record values do not distinguish `p=1/3` from `p=1/2`. Exact
masses differ — at `p=1/3` they are `8/27,12/27,6/27,1/27`, and at `p=1/2`
they are `1/8,3/8,3/8,1/8` — but those masses are law-level numbers, not
Record readouts.

The degenerate endpoints are different objects:

`bernoulli_I_support(3,0)={0}`, `bernoulli_I_support(3,1)={3}`.

Those are content-support facts, not fairness. Restricting attention to
`p∈{0,1}` changes the claim.

## Theorem 4 — Expectation Is Extra

The Bernoulli mean of the count is the law-level number

`E[I]=n p`.

On the executed family at `p=1/2` this is `E[I]=3/2`. The realized Record
values are `{0,1,2,3}`, so `3/2` is not a realized `I`. Identifying
`p=I/n` is a law-of-large-numbers estimator, not axiom content. On the
executed `n=3` family

`I/3∈{0, 1/3, 2/3, 1}`,

which equals `1/2` for no realized `I`.

`E[I]` is therefore extra. It is a number computed from a declared law, not
a Record readout. Dividing the realized count by `n` does not recover
`1/2` on the executed family.

## Theorem 5 — Scoped Negative

No function of the realized additive scalar `I` supplied by Record
additivity equals the law-level fair margin `1/2` on every realization in
the executed family.

The Record-supplied functions of a formed binary collection are the
realized sum `I` and, if one later divides by the declared count `n`, the
finite-sample ratio `I/n`. On the executed family:

- `I∈{0,1}` for one bit and `I∈{0,1,2,3}` for three bits, so `I` is never
  `1/2`;
- `I/3∈{0,1/3,2/3,1}`, so the finite-sample estimator is never `1/2`;
- `E[I]/n=p` is not a Record readout.

Admissibility determines a distribution from nearest-neighbor conditions
and, by the reading note, does so only conditional on formation. It does
not select `p=1/2` among binary laws. The same possible `I` values occur
for `p=1/3` and for `p=1/2`.

This scoped obstruction does not say that bits cannot be fair. It does not say that no fair compiler exists. It does not
say that no fair compiler exists. A later physical selector for `p=1/2`,
or a formation process whose typical `I/n` converges to `1/2`, remains
open.

## Boundary And Non-Claims

The note does not:

- edit an axiom, or argue that an axiom update is necessary;
- claim that bits cannot be fair, or that no fair compiler exists;
- claim independence, or derive a product law from the four axioms;
- identify `E[I]=n p` or `I/n` with a physical Record law;
- select among `p∈{0,1/3,1/2,1}` by any physical mechanism;
- close record formation at those sites;
- restated-as-new any spacing-3 disjoint nearest-neighbor theorem.

The scope is the exact gap: Record additivity supplies a count, and that
count is not the fair binary margin.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current content-only sentence and Record additivity | premise | quoted; no edit |
| current Admissibility distribution sentence | premise | quoted; no edit |
| reading note on formation site/rate | interpretive | quoted; non-governing |
| declared Bernoulli comparison family | comparison object | not derived |
| one-bit and `n=3` rejectors | declared algebra | computed here |
| physical selector for `p=1/2` | escape route | live, not derived |

The exact advance is a finite count-versus-margin theorem. Independent
audit remains required before any effective status may change.

## Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | The campaign handoff residual still asks for a fair binary margin after a bit compiler is granted a product law. This note shows Record `I` cannot be that margin. That is a derivation gap on the readout, not an "upstream unratified" complaint. |
| V2 | New content? | Searched `origin/main` `c45dd5ab30` for fair binary, `p=1/2` Record readout, Bernoulli margin, and `I` versus `p`. Hits: the Admissibility reading note (formation site/rate not supplied); occupancy/formation non-supply notes attack `R_η` or occupancy grain, different objects; the post-record count firewall and the Cycle 42 identifiability probe treat empirical frequency versus a predictive law, not `I` as a Record readout of `p=1/2`; the flavor-find central-block weights `p=1/2` versus `p=1/3` are a `C3` state object. No landed `I`-versus-`p=1/2` rejector on a binary Record collection. |
| V3 | Independently checkable? | Yes. Textbook Bernoulli support does not mention Record additivity or the axiom `I`. The runner recomputes `I_of_bits` from `0/1` contents and `bernoulli_I_support` from exact binomial masses. |
| V4 | More than a restatement? | Yes: exact `I/3∈{0,1/3,2/3,1}` never equals `1/2`; supports of `p=1/3` and `p=1/2` coincide on `{0,1,2,3}`; `E[I]=3/2` at `p=1/2` is not a realized `I`. |
| V5 | One-step relabel? | No. The claim is not a corollary of "Records form" or of the reading note's formation-rate sentence. Closest is that reading note; this note is about the margin, not the formation bit. |

## No-Go Discipline Gate

The negative claim is restricted to realized additive `I` versus the
law-level fair margin `1/2` on the executed family. The gate does not
certify that bits cannot be fair or that no compiler exists.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| Read `I` of one bit | treat the content-only readout of one formed bit as the margin | Theorem 1: `I∈{0,1}`, so `I` is never `1/2` | **ATTEMPTED** |
| Finite estimator `I/n` | divide the realized count by the declared collection size | Theorem 2 and Theorem 4: on `n=3`, `I/3∈{0,1/3,2/3,1}` never hits `1/2` | **ATTEMPTED** |
| Expectation `E[I]/n` | replace the realized sum by its Bernoulli mean | Theorem 4: `E[I]=3/2` at `p=1/2` is not a Record readout | **ATTEMPTED** |
| Restrict to `p∈{0,1}` | recover a definite `I` from degenerate support | Theorem 3: those are content-support facts, not fairness | **ATTEMPTED** |
| Take `n→∞` and a law of large numbers | let typical `I/n` converge to `p` | live escape; not executed on the finite family | **ATTEMPTED** as open |
| Rewrite the axiom memo to force `p=1/2` | close the margin by editing Admissibility or Record | forbidden in this lane; not proposed | **ATTEMPTED** as closed to this note |

The first three routes are the Record-supplied functions of a formed
collection. They fail as readouts of `1/2` on the executed family. The
fourth route is a different claim. The fifth remains live and is why
fairness is not declared impossible.

### N2 — wall independence and collapse

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| realized `I` is a count / open supports coincide | no: a count can still carry `p`-dependent masses | no: shared support does not by itself prove `I≠1/2` | witnesses of one wall |
| realized `I` is a count / `E[I]` is extra | no: forbidding the mean does not force `I` integer | no: integer-valued `I` does not address expectation | witnesses of one wall |
| open supports coincide / `E[I]` is extra | no: support equality is not a mean statement | no: the mean distinguishes `p` while support does not | witnesses of one wall |

The raw list collapses to one scoped wall: on the executed family, Record
additivity does not supply the fair margin `1/2`. Shared open support and
the extra status of `E[I]` are witnesses, not independent walls.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| formed records | explicit scope; the count is conditional on formation, matching the reading note |
| unit strength and menu `{0,1}` | declared objects, not inferred from Lattice nearest-neighbor geometry |
| product Bernoulli family | declared comparison object; independence is not claimed as axiom content |
| `p∈{0,1/3,1/2,1}` | declared comparison margins |
| `n=1` and `n=3` | executed family; the large-`n` estimator is named as a live escape |
| "registered" / "canonical" | not used as load-bearing predicates |
| observations or empirical frequencies | none |

No hidden continuity, typicality, or formation-rate hypothesis is used in
Theorems 1–5.

### N4 — source residual matching

| Source | Residual that source attacks | Residual claimed here | Match? |
|---|---|---|---|
| [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) reading note | formation site, probability, or rate | law-level margin `p=1/2` versus realized `I` | no; cited only as the formation-rate sentence |
| [`ACPHILAMBDA_R_ETA_RECORD_FORMATION_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md`](ACPHILAMBDA_R_ETA_RECORD_FORMATION_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md) | `R_η` selector from "Records form" | binary `I` versus `p=1/2` | no |
| [`ACPHILAMBDA_OCCUPANCY_FORMATION_APPEND_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md`](ACPHILAMBDA_OCCUPANCY_FORMATION_APPEND_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md) | occupancy grain / doublet dictionary | binary `I` versus `p=1/2` | no |
| [`POST_RECORD_COUNT_PROBABILITY_FIREWALL_2026-06-06.md`](POST_RECORD_COUNT_PROBABILITY_FIREWALL_2026-06-06.md) | counts as a unique predictive law | `I` as a readout of the fair margin | related shape; not the same residual |
| work-history Cycle 42 identifiability probe | exact law identity from a finite transcript | `I` as a Record readout of `p=1/2` | related shape; not landed as this rejector |

Dropped as authorities for the present rejector: every occupancy/`R_η`
note, and every identifiability note that never mentions Record `I` as a
stand-in for `p=1/2`. The witnesses computed here do not lean on those
residuals.

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | each `0/1` atom has `I∈{0,1}` | no claim about every conceivable readout map |
| per site | one formed binary record, or a finite disjoint collection | no composite-carrier or intervention theorem |
| per mode | no spectral-mode object is present | no mode exhaustion |
| per block | realized additive `I` versus `p=1/2` on the executed family | no lattice-wide compiler closure |
| lattice-wide | checked and not executed | no lattice-wide fairness selector |

The runner emits substantive `per_element`, `per_site`, `per_mode`,
`per_block`, and `lattice_wide` lines.

### N6 — live partial-closure paths

A later derivation may still select `p=1/2` without editing the axiom
memo: a physical formation process, a typicality-plus-large-`n` theorem,
or another law-level selector could do that work. Those paths are live.
This note does not argue that an axiom update is necessary, and it does
not offer axiom text.

Approved scale-reference, kinetic-isotropy, and realized-state primitives
supply no Bernoulli margin. They are not counted as extra walls.

### N7 — hostile steelman

> Typicality plus large `n` already gives fairness from the count. If
> records form independently at many sites, `I/n` converges to `p`, and
> some later symmetry or maximum-entropy reading can force `p=1/2`. The
> finite `n=3` miss is then only a small-sample defect, not an obstruction
> to a fair compiler.

Typicality is not axiom content. On every finite executed `n`, `I/n` is a
multiple of `1/n` and misses `1/2` whenever `n` is odd. The steelman is a
live large-`n` escape. It is why the shipped claim stays scoped to the
executed family and does not say bits cannot be fair.

### N8 — cross-cycle echo

| Earlier surface | Later movement | Echo here |
|---|---|---|
| Admissibility reading note | formation site/rate left downstream | this note keeps formation open and attacks the margin instead |
| occupancy/formation non-supply | `R_η` and grain remain separate objects | those residuals are not re-used as this rejector |
| post-record count firewall | counts audit a law after the law is supplied | same type split, different object: `I` versus `p=1/2` |
| flavor-find central-block weights | `p=1/2` versus `p=1/3` on a `C3` state | different object; not binary Record `I` |

No structurally similar landed wall was later retired by a mechanism that
would already make realized `I` equal `1/2` on the executed family.

**Gate disposition:** PASS for the scoped obstruction that realized
additive `I` does not equal, and does not select, `p=1/2` on the executed
family. FAIL / DO NOT SHIP for "bits cannot be fair" or "no compiler
exists."

## Primary Runner

[`scripts/record_additivity_does_not_select_fair_binary_margin_2026_08_13.py`](../scripts/record_additivity_does_not_select_fair_binary_margin_2026_08_13.py)
recomputes `I_of_bits` from `0/1` contents, `bernoulli_I_support` from
exact binomial masses, the `n=3` ratio set, and the extra status of
`E[I]` in exact arithmetic.
