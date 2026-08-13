---
claim_id: one_formation_token_mutual_exclusion_two_ready_sites_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On two ready sites carrying the same one-site law μ on {A,B} with μ(A)=1/3 and μ(B)=2/3, a declared token T in {x, y, none} makes a history the pair (μ, T); formation at a site occurs iff T equals that site; μ is the same for all three tokens so the content law is not occurrence; T=x and T=y are mutually exclusive by declared one-token occupancy, not by an axiom derivation; the axioms do not select among the three tokens; a later one-token-per-window supplier would give mutual exclusion and a well-defined formed site, and that supplier is not Record additivity."
upstream_dependencies:
  - minimal_axioms
runner: scripts/one_formation_token_mutual_exclusion_two_ready_sites_2026_08_13.py
---

# One Formation Token, Mutual Exclusion, Two Ready Sites

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** one declared finite menu `{A,B}` with exact masses `1/3` and
`2/3`; two ready sites `{x,y}`; a declared token `T ∈ {x, y, none}`;
histories of the form `(μ, T)`; Record additivity used only as a content
readout on the empty collection and on a formed singleton.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/one_formation_token_mutual_exclusion_two_ready_sites_2026_08_13.py`](../scripts/one_formation_token_mutual_exclusion_two_ready_sites_2026_08_13.py)

## Result Up Front

A one-site Admissibility law is a content law. A formation token is a
separate occupancy mark. The two objects are not the same.

The current Admissibility sentence in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) is quoted only
as a premise and is not edited:

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

The Admissibility reading note is quoted only as a premise. The distribution
concerns which possibility a forming record locks, conditional on formation at
that site; it does not supply the formation site, probability, or rate.

The current Record lock sentence is quoted only as a premise:

When present, a record locks exactly one admissible local possibility.

The current Record additivity sentence is quoted only as a premise:

For any finite collection of pairwise-disjoint records, scalar readout
`I` is additive, with `I(empty)=0`.

A readout value is determined by record content alone.

Five exact statements locate the split on two ready sites.

1. **Content law is not occurrence.** The same `μ` is the content coordinate
   of the histories with `T=x`, `T=y`, and `T=none`.
2. **Declared mutual exclusion.** In this calculus there is no history in
   which both ready sites form. That is one-token occupancy, declared as the
   token alphabet, not derived from the quoted axiom sentences.
3. **No axiom selector among the three tokens.** All three histories are
   Admissibility-compatible: support permits `A` or `B` at whichever site
   forms, and `T=none` is allowed because formation is conditional.
4. **Positive extra structure.** If a later supplier provides exactly one
   token per window, mutual exclusion and a well-defined formed site follow.
   That supplier is not Record additivity: `I(empty)=0`, and `I` of a formed
   singleton is a content readout, not a site picker.
5. **Scoped negatives.** The note does not add a token sentence to the axiom
   memo. It does not claim that no formation rule exists.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The three-token history list, the shared content law, declared mutual exclusion, and the Record-additivity contrast are finite exact Fraction checks; a one-token-per-window supplier remains extra."
trace_class: negative_route_pruning
target_claim_id: one_formation_token_two_ready_sites
target_blocker_text: "derive which of two ready sites forms, or that both form, from the shared one-site content law or from Record additivity"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "A later one-token-per-window supplier would make mutual exclusion and a well-defined formed site; Record additivity is not that supplier. Do not add token text to the axiom memo."
conditional_surface_status: "exact for the declared token alphabet {x, y, none} and the shared full-support law μ on {A,B}; one-token-per-window remains extra"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Work with two named sites `{x, y}`. Each site carries the same one-site law
`μ` on the finite menu `{A, B}` with

`μ(A) = 1/3`, `μ(B) = 2/3`.

These masses are exact rationals. They sum to one:

`μ(A) + μ(B) = 1/3 + 2/3 = 1`.

Both masses are strictly positive, so the support is the whole menu:

`supp(μ) = {ω ∈ {A, B} : μ(ω) > 0} = {A, B}`.

On finite menus the axiom memo identifies available/admissible content with
that support. Both sites are therefore **ready**: if a record forms at either
site, it may lock `A` or `B`.

A **token** is a value `T ∈ {x, y, none}`.

A **history** is the pair `(μ, T)`. The content coordinate is the same `μ`
in every executed history. The occupancy coordinate is the token.

**Formation** at a site occurs if and only if the token equals that site:

- `T = x` forms at `x` and not at `y`,
- `T = y` forms at `y` and not at `x`,
- `T = none` forms at neither site.

The three executed histories are therefore

- `H_x = (μ, T=x)`,
- `H_y = (μ, T=y)`,
- `H_none = (μ, T=none)`.

There is no fourth token that names both sites. The formed-site set of a
history is at most a singleton.

A **later one-token-per-window supplier**, if provided, would restrict the
token to `{x, y}` inside a declared window. That restriction is extra
structure. It is not part of the three-history calculus above.

A **content readout** on a formed singleton is a scalar determined by the
locked label alone. The executed readout is

`I(empty) = 0`, `I({A}) = 1`, `I({B}) = 2`.

Those three values are a content table. They do not name `x` or `y`.

## Exact Target And Obligation Graph

**Exact target.** On the declared two-site token calculus, exhibit the shared
content law across `T ∈ {x, y, none}`, record that `T=x` and `T=y` cannot
both occur in one history, exhibit all three tokens as Admissibility-
compatible, record that a later one-token-per-window supplier would give
mutual exclusion and a well-defined formed site, and record that Record
additivity is not that supplier.

| Obligation | Role | Disposition |
|---|---|---|
| pin the Admissibility distribution sentence | premise | quoted; no edit |
| pin the formation-site/rate reading note | premise | quoted; no edit |
| pin Record “when present” | premise | quoted; no edit |
| pin Record additivity and `I(empty)=0` | premise | quoted; no edit |
| pin readout-by-content-alone | premise | quoted; no edit |
| show `μ` is the same for all three tokens | Theorem 1 | listing |
| show `T=x` and `T=y` are mutually exclusive | Theorem 2 | declared alphabet |
| exhibit all three tokens as compatible | Theorem 3 | support plus conditional formation |
| record that one-token-per-window is extra, and is not `I` | Theorem 4 | positive extra; additivity contrast |
| refuse a token-memo edit and a no-rule claim | Theorem 5 | scoped negative |

## Theorem 1 — Content Law Is Not Occurrence

**Claim.** The one-site law `μ` is the same for `T=x`, `T=y`, and `T=none`.
Content law is not occurrence.

**Proof.** By definition every executed history is a pair whose first
coordinate is the same map `μ`. The three second coordinates differ:

| History | token | formed sites | content law |
|---|---|---|---|
| `H_x` | `x` | `{x}` | `μ` |
| `H_y` | `y` | `{y}` | `μ` |
| `H_none` | `none` | empty | `μ` |

The masses `μ(A)=1/3` and `μ(B)=2/3` do not depend on `T`. Occurrence is
the token. The two coordinates are independent by construction.

The Admissibility sentence determines, for each site, a distribution from
nearest-neighbor conditions. The token is not among those conditions. The
reading note already types the distribution as a content law conditional on
formation, not as an occurrence mark.

A predicate that reads “`μ` selects `T`” therefore fails: one `μ` appears
with all three tokens.

## Theorem 2 — Mutual Exclusion Is Declared One-Token Occupancy

**Claim.** `T=x` and `T=y` are mutually exclusive. There is no history in
this calculus with both sites formed. This is declared one-token occupancy,
not a derivation from the quoted axiom sentences.

**Proof.** The token alphabet is `{x, y, none}`. A history carries exactly
one token. Formation at a site occurs iff that token equals the site. The
conjunction “`x` formed and `y` formed” would require `T=x` and `T=y` in
the same history, which the alphabet forbids. The formed-site sets of the
three histories are `{x}`, `{y}`, and empty. None is `{x, y}`.

The quoted axiom sentences do not supply this alphabet. Admissibility names
a content law conditional on formation. Record uniqueness says a site never
carries more than one record; it does not say that two ready sites cannot
both carry a record. The mutual-exclusion sentence of this note is therefore
the occupancy declaration of the token calculus, not an axiom theorem.

A predicate that reads “both ready sites form” fails on every history of
this calculus.

## Theorem 3 — The Axioms Do Not Select Among The Three Tokens

**Claim.** The quoted axiom sentences do not select among `{T=x, T=y,
T=none}`. All three histories are Admissibility-compatible.

**Proof.** Compatibility with Admissibility is the quoted reading note: the
distribution concerns which possibility a forming record locks, conditional
on formation at that site; it does not supply the formation site,
probability, or rate.

On `H_x` a record forms at `x`. The support `{A, B}` permits either lock.
On `H_y` a record forms at `y`. The same support permits either lock.
On `H_none` no record forms at either ready site. Formation is conditional,
so the same content law is not asked to lock a value at those sites.

Compatibility with Record’s lock sentence is the same split. When present,
a record locks exactly one admissible local possibility. On `H_x` and `H_y`
the present record locks `A` or `B`. On `H_none` no record is present at
those sites, so the lock sentence does not apply there.

`H_none` does not contradict “Records form.” That sentence is a global
occurrence mark. It may be realized at sites other than `{x, y}`. Emptiness
of the two ready sites is not emptiness of the lattice.

Theorem 1 already supplies one shared `μ` for all three tokens. Therefore
the content law does not select the token, and the quoted sentences do not
select among the three histories.

## Theorem 4 — One Token Per Window Is Extra, And Is Not Record Additivity

**Claim.** If a later supplier provides exactly one token per window, mutual
exclusion and a well-defined formed site follow. That supplier is not Record
additivity.

**Proof.** Restrict the token alphabet of one window to `{x, y}`. Then the
window has exactly one token, the formed-site set is a singleton, and the
formed site is the token itself. Mutual exclusion is the singleton. The
formed site is well-defined because the token is never `none`. That
restriction is extra structure. It is not present in the three-history
calculus of Theorems 1–3, which still includes `T=none`.

Record additivity is a different object. The axiom memo states that a
readout value is determined by record content alone, and that for any finite
collection of pairwise-disjoint records, scalar readout `I` is additive,
with `I(empty)=0`.

On the empty collection at the two ready sites the executed readout is

`I(empty) = 0`.

On a formed singleton the executed readout is a content table:

`I({A}) = 1`, `I({B}) = 2`.

Those values do not depend on which ready site formed. In particular

`I` of a singleton locking `A` at `x` equals `I` of a singleton locking `A`
at `y`,

and likewise for `B`. The readout of a formed singleton is therefore a
content readout, not a site picker. Additivity on disjoint unions is a sum
of such content values. A sum of content values does not name `T`.

So a later one-token-per-window supplier would give the positive structure
(mutual exclusion plus a well-defined formed site), and Record additivity
is not that supplier.

## Theorem 5 — Scoped Negatives

**Claim.** Theorems 1–4 do not add a token sentence to the axiom memo. They
do not claim that no formation rule exists.

**Scope.** The negatives are restricted to *forcing* a token, or both-site
formation, from the shared content law or from Record additivity on this
two-site fragment. They do not say that records never form. They do not say
that a later formation rule is impossible. They do not edit the four axiom
sentences. A one-token-per-window supplier remains extra until it is derived
from executable objects.

## Boundary And Non-Claims

The note does not:

- edit an axiom sentence, or argue that an axiom-sentence change is
  necessary;
- claim that no formation rule exists;
- claim that records never form, or that `H_none` is a completed empty
  universe;
- derive the masses `1/3` and `2/3` from nearest-neighbor data; they are
  the declared content law of the exhibit;
- identify the executed `{A, B}` menu with the full one-site possibility
  domain `M_2(C)`;
- treat mutual exclusion of `{x, y}` as an axiom theorem (Theorem 2 is a
  declaration of the token alphabet);
- treat Record additivity as a site picker.

The scope is the exact token split: one shared full-support law, three
tokens, declared one-token occupancy, and an additivity contrast.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current Admissibility distribution sentence | premise | quoted; no edit |
| Admissibility reading note on formation site/rate | premise | quoted; no edit |
| Record “when present” lock sentence | premise | quoted; no edit |
| Record additivity and `I(empty)=0` | premise | quoted; no edit |
| readout determined by content alone | premise | quoted; no edit |
| shared `μ` on `{A,B}` | Theorem 1 | declared; masses checked |
| token alphabet `{x, y, none}` | Theorem 2 | declared occupancy |
| three compatible histories | Theorem 3 | support plus conditional formation |
| one-token-per-window supplier | Theorem 4 | extra; not derived |
| content table `I(empty)=0`, `I({A})=1`, `I({B})=2` | Theorem 4 | executed readout; not a site picker |
| observed frequencies or fitted tokens | none | not used |

The exact advance is a finite token calculus plus an additivity contrast.
Independent audit is required. This note authors no audit verdict.

## Promotion Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | The current Admissibility reading note states that the distribution is conditional on formation and does not supply the formation site, probability, or rate. The named residual is which of two ready sites forms. This note asks whether a shared one-site law, or Record additivity, already selects the token, and answers no. |
| V2 | New content? | Searched `origin/main` at `c45dd5ab30` by filename and phrase for a declared token alphabet `{x, y, none}` on two ready sites with shared `μ(A)=1/3`, `μ(B)=2/3`, and for a Record-additivity contrast that `I` of a formed singleton is not a site picker. Landed formation notes address a process/rule residual or other objects, not this three-token calculus. No landed `H_x` / `H_y` / `H_none` split of one full-support law appears on that commit. |
| V3 | Independently checkable? | The runner rebuilds the three histories from the declared `μ` and token alphabet in exact `Fraction` arithmetic, checks that no history occupies both sites, checks that `μ` does not select `T`, and checks that `I(empty)=0` while singleton readouts ignore the site. |
| V4 | More than a restatement? | Yes. The discriminating witnesses are the three-token table with one `μ`, the empty intersection of formed-site sets `{x} ∩ {y}`, and the equality of singleton readouts at `x` and at `y`. Those identities are not restatements of the axiom sentence. |
| V5 | One-step relabel? | No. The Admissibility sentence names a per-site distribution. It does not name a token alphabet, mutual exclusion of two ready sites, or a one-token-per-window supplier. |

## No-Go Discipline Gate (Theorems 4 and 5 only)

The negative claims are restricted to: the shared content law does not
select the token; Record additivity does not pick the formed site; this is
not a claim that no formation rule exists. The gate does not ship a global
non-existence theorem against formation rules.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| content law selects the token | treat `μ` as already naming `T` | Theorem 1: one `μ` appears with all three tokens | **ATTEMPTED** |
| both ready sites form | treat readiness as double occupancy | Theorem 2: no history has formed-site set `{x, y}` | **ATTEMPTED** |
| Admissibility distribution forces the site | read the NN-determined law as a formation-site rule | reading note: the distribution is conditional on formation and does not supply the formation site, probability, or rate | **ATTEMPTED** |
| “when present” forces presence | treat the lock sentence as a selector that makes the record present | the lock sentence constrains a present record; it does not create one | **ATTEMPTED** |
| Record additivity picks the site | treat `I` of a formed singleton as naming `x` or `y` | Theorem 4: `I` depends on the locked label, not on the site | **ATTEMPTED** |
| axiom-memo token sentence | add a token sentence to close the residual | Theorem 5: the residual is extra; no axiom sentence is edited | **ATTEMPTED** |

### N2 — wall independence

Theorems 4 and 5 close only the route that reads a token, or a formed site,
off the shared content law or off Record additivity. They do not close a
later one-token-per-window derivation or a later executable formation rule.
Those walls remain independent.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| declared menu `{A, B}` | executed possibility set; not the full `M_2(C)` domain |
| masses `1/3`, `2/3` | declared content law |
| ready sites `{x, y}` | explicit hypothesis |
| token alphabet `{x, y, none}` | declared occupancy of this calculus |
| histories `H_x`, `H_y`, `H_none` | executed token list of one `μ` |
| one-token-per-window supplier | extra; not derived |
| content table for `I` | executed readout; not a site picker |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | Admissibility distribution sentence; formation-site/rate reading note; Record “when present”; Record additivity and `I(empty)=0`; readout by content alone | quoted as premises only; no edit |
| shared one-site law `μ` | content coordinate independent of `T` | declared here |
| token alphabet | mutual exclusion by listing | declared here |

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | menu labels `A`, `B` and token values `x`, `y`, `none` | no classification of every map on `Z^3` |
| per site | one shared law and one token mark at the two ready sites | no composite bonded-pair theorem |
| per mode | content masses versus occupancy tokens, not spectral modes | no harmonic-mode exhaustion |
| per block | the three-history token calculus and the additivity contrast only | no dynamics or formation rate |
| lattice-wide | checked and not executed | no lattice-wide no-go against formation rules |

The obstruction is per-site / declared token alphabet; it is not lattice-wide.

### N6 — live partial-closure paths

1. A later one-token-per-window supplier derived from executable objects.
2. A later formation rule that selects among `{T=x, T=y, T=none}` without
   editing the axiom memo.
3. A later content readout that remains a content readout while a separate
   occupancy mark is supplied by other objects.

The quoted Admissibility sentence already names a per-site distribution.
The token is a different coordinate. No axiom sentence is edited here. A
later derivation is not forbidden.

### N7 — hostile steelman

> Both sites are ready under the same `μ`. Readiness is permission to form.
> Permission to form is formation. Therefore both sites form, and a token
> that forbids double occupancy contradicts the content law.

**Answer.** That identification is exactly the predicate “both ready sites
form.” Theorem 1 separates the content law from the token. Theorem 2 lists
the formed-site sets and finds none equal to `{x, y}`. Theorem 3 types
`T=none` as compatible because formation is conditional. Readiness is
support of the content law, not occupancy.

### N8 — cross-cycle echo

Earlier landed notes prune routes that would force a formation rule, site,
or rate from the axiom baseline, or that would treat a content law as an
occurrence mark in other calculi. The present negatives face a narrower
residual: even after two sites share one full-support law, a declared token
is still not selected, and Record additivity still does not pick the site.
Those earlier notes are not cancelled. They remain notes about different
premises.

**Gate disposition.** PASS for the scoped token split and the two negatives
of Theorems 4 and 5. FAIL / DO NOT SHIP for “no formation rule exists” or
for adding token text to the axiom memo.

## Primary Runner

[`scripts/one_formation_token_mutual_exclusion_two_ready_sites_2026_08_13.py`](../scripts/one_formation_token_mutual_exclusion_two_ready_sites_2026_08_13.py)
rebuilds the shared `μ`, the three histories, the formed-site sets, the
content readout `I`, and the one-token-per-window restriction in exact
`Fraction` arithmetic. A predicate “both ready sites form” must fail on
this calculus. A predicate “`μ` selects `T`” must fail. No cache is
written.
