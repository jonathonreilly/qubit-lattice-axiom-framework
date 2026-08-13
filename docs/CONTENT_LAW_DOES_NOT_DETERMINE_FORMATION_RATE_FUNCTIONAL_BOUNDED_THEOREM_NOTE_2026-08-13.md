---
claim_id: content_law_does_not_determine_formation_rate_functional_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On the exact finite menu {A,B,C} with μ(A)=1/3, μ(B)=2/3, μ(C)=0, four lawful lock histories on a 4-site window have empirical rates 1/4, 1/2, 3/4, and 1, so no functional of μ equals the empirical window rate on every lawful history; the counting selector that every site forms is extra, and a physical rate supplier remains open."
upstream_dependencies:
  - minimal_axioms
runner: scripts/content_law_does_not_determine_formation_rate_functional_2026_08_13.py
---

# A Content Law Does Not Determine A Formation-Rate Functional

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact finite-menu content law `μ=(1/3,2/3,0)` and empirical
window rates on one 4-site set; no map of `μ` alone recovers every lawful
rate; a physical rate supplier remains extra.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/content_law_does_not_determine_formation_rate_functional_2026_08_13.py`](../scripts/content_law_does_not_determine_formation_rate_functional_2026_08_13.py)

## Result Up Front

The current Admissibility sentence in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) is quoted only
as a premise and is not edited:

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Read with Record, that distribution is the content law for a forming record.
The current reading note is likewise quoted only as a premise:

> it does not supply the formation site, probability, or rate.

The current Record occurrence sentence is likewise quoted only as a premise:

> Records form.

Those sentences already split content from rate. They do not, by themselves,
exhibit a four-value rejector or prove that no functional of a declared
content law can equal the empirical window rate on every lawful history.

On the declared three-point menu the content law is

`μ(A)=1/3`, `μ(B)=2/3`, `μ(C)=0`.

Support is `{A,B}`. On a 4-site window the four prefix histories that lock
the first `k` sites to `A`, for `k=1,2,3,4`, are lawful and nonempty. Their
empirical rates are `1/4`, `1/2`, `3/4`, and `1`. Any map that depends on
`μ` alone is constant on that four-tuple. The four rates are not constant.
Therefore no functional `ρ(μ)` equals `r(h)` for every lawful `h`.

The counting selector “every site forms” forces rate `1`. It is a selector,
not a theorem of Admissibility or Record. A 2-site occupancy pair with
formation counts `1` and `2` is reconstructed here as a coarser count
witness; it is not a four-rate functional gap. Support still forbids a lock
of `C`. A physical formation-rate supplier remains open. This note does not
adopt a rate, a Poisson intensity, a constant `λ`, or axiom text.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Four lawful prefix histories on a 4-site window have empirical rates 1/4, 1/2, 3/4, 1; any μ-only map is constant on those histories, so no functional of the content law equals the empirical window rate. A physical rate supplier remains extra."
trace_class: negative_route_pruning
target_claim_id: physical_formation_rate_supplier
target_blocker_text: "supply a formation rate from Admissibility or Record"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "No functional of the content law equals the empirical window rate. A physical rate supplier remains extra. Do not adopt axiom text."
conditional_surface_status: "exact for the four prefix rates on one 4-site window and the μ-only constancy rejector; a physical rate supplier remains extra"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Let the finite local possibility menu be

`X = {A, B, C}`.

Let `μ` be the probability measure on `X` with

`μ(A) = 1/3`, `μ(B) = 2/3`, `μ(C) = 0`.

These three masses are the declared content law. They sum to one:

`μ(A) + μ(B) + μ(C) = 1/3 + 2/3 + 0 = 1`.

On finite menus the current axiom memo identifies available/admissible
content with support: exactly the possibilities of nonzero probability.

`supp(μ) = {ω ∈ X : μ(ω) > 0} = {A, B}`.

Thus `C` is not admissible.

Write `e1=(1,0,0)`, `e2=(0,1,0)`, `e3=(0,0,1)`, and `0=(0,0,0)` in `Z^3`.
The executed window is the 4-site path

`W = {0, e1, 2e1, 3e1} ⊂ Z^3`, `|W|=4`.

The four sites of a unit tetrahedron `{0, e1, e2, e3}` are an equivalent
4-site set: they have the same cardinality, so they carry the same possible
empirical rates `{0,1/4,1/2,3/4,1}`. Prefix histories below are written on
the path, which supplies a linear order.

A **lock history** is a partial map `h: W ⇀ {A,B,C}`. An undefined value
means no record at that site. Record uniqueness makes the partial map at
most single-valued. Write

`N(h) := |dom(h)|`, `r(h) := N(h)/|W| = N(h)/4`.

The possible values of `r` on this window are `{0, 1/4, 1/2, 3/4, 1}`.

A history is **lawful** for `μ` when every locked value lies in `supp(μ)`,
equivalently when no site locks `C`. A history **satisfies occurrence**
when `N(h) ≥ 1`. The sentence Records form. is used only as occurrence:
the all-empty completed history is excluded, so executed histories have
`N≥1` and `r ∈ {1/4, 1/2, 3/4, 1}`.

The current lock wording used below is:

When present, a record locks exactly one admissible local possibility.

The four **prefix histories** lock the first `k` path sites to `A` and
leave the rest empty:

| History | lock at `0` | `e1` | `2e1` | `3e1` | `N` | `r` |
|---|---|---|---|---|---|---|
| `h_1` | `A` | empty | empty | empty | `1` | `1/4` |
| `h_2` | `A` | `A` | empty | empty | `2` | `1/2` |
| `h_3` | `A` | `A` | `A` | empty | `3` | `3/4` |
| `h_4` | `A` | `A` | `A` | `A` | `4` | `1` |

A **functional of the content law** is a map `ρ` whose value on a history
depends on `μ` alone, not on `h`. On the four prefix histories any such
`ρ` is a single rational `ρ(μ)`.

The **always-form selector** is the extra rule that every site of `W`
carries a lock. On this window it forces `N=4` and `r=1`.

A reconstructed **2-site star exhibit** uses `{x,y}={0,e1}` with the same
`μ`. The two lawful patterns that lock `A` at `x` only, and that lock `A`
at `x` and `B` at `y`, have formation counts `1` and `2`. Those counts are
a coarser occupancy witness, not a four-rate functional uniqueness gap.

## Exact Target And Obligation Graph

**Exact target.** Exhibit four distinct lawful empirical rates on one
4-site window, prove that no functional of `μ` equals `r(h)` on every
lawful history, and record that a counting selector and a physical rate
supplier remain extra.

| Obligation | Role | Disposition |
|---|---|---|
| pin the rate non-supply sentence and Records form. | premise | quoted from the axiom memo |
| exhibit four lawful rates `1/4,1/2,3/4,1` | Theorem 1 | prefix histories `h_k` |
| show no `ρ(μ)` equals every `r(h)` | Theorem 2 | constancy versus four values |
| display the always-form selector as extra | Theorem 3 | forces `r=1` |
| show support still forbids `C` | Theorem 4 | rate freedom is not content freedom |
| leave a physical rate supplier open | Theorem 5 | scoped residual |
| adopt a Poisson intensity, a constant `λ`, or a rate | non-claim | not performed |
| edit an axiom to name a rate | non-claim | not required |

## Theorem 1 — Four Distinct Lawful Rates

**Claim.** The prefix histories `h_k` for `k=1,2,3,4` are lawful for `μ`
and satisfy occurrence. Their empirical rates are

`r(h_1)=1/4`, `r(h_2)=1/2`, `r(h_3)=3/4`, `r(h_4)=1`.

**Proof.** Each `h_k` locks only the label `A`. Because `μ(A)=1/3>0`, the
point `A` lies in `supp(μ)`, so every lock is admissible and each `h_k` is
lawful. The domains have sizes `1,2,3,4`, so occurrence holds and

`r(h_k)=k/4`.

Those four rationals are pairwise distinct. The same four values are the
possible nonempty occupancy fractions on any 4-site set, including the
tetrahedron `{0,e1,e2,e3}`.

## Theorem 2 — No Functional Of `μ` Equals `r`

**Claim.** Let `ρ` be any map that depends only on the content law `μ`
and not on the history. Then `ρ` is constant on `{h_1,h_2,h_3,h_4}`. The
values `r(h_k)` are not constant. Therefore `ρ(μ)` cannot equal `r(h)` for
every lawful `h`.

**Proof.** The four prefix histories carry the same declared measure `μ`.
A map whose only input is `μ` therefore returns a single rational
`c := ρ(μ)` at each of `h_1,\ldots,h_4`. Theorem 1 gives

`r(h_1)=1/4 ≠ 1=r(h_4)`.

No single rational equals both `1/4` and `1`. Hence `c` cannot equal
`r(h)` on every lawful prefix history, and cannot equal `r(h)` on every
lawful history.

The same obstruction meets any concrete `μ`-only formula. The support
mass `μ(A)+μ(B)=1` recovers only `r(h_4)`. The mass `μ(A)=1/3` equals
none of the four rates. A declared constant intensity `λ` is likewise a
single rational and fails the same four-value rejector.

## Theorem 3 — The Counting Selector Is Extra

**Claim.** The rule “every site forms” forces `r=1` on `W`. It is a
selector on histories, not a theorem of Admissibility or Record. The rule
is displayed; it is not adopted.

**Proof.** If every site of `W` carries a lock, then `N(h)=4` and
`r(h)=1`. Filling the empty slots of `h_1` with `A` produces `h_4` and
replaces the rate `1/4` by `1`. Admissibility constrains locked content
to `supp(μ)`; it does not force a lock to be present at every site.
Record occurrence requires only `N≥1`. The four lawful rates of Theorem 1
already include values other than `1`. Therefore the always-form rule is
an extra selector. It is not forced by the quoted sentences.

## Theorem 4 — Support Still Constrains Content

**Claim.** No lawful history may lock `C`. Rate freedom is not content
freedom. In particular `μ(C)=0` does not forbid `N=4`: the history `h_4`
locks four copies of `A` and is lawful.

**Proof.** Lawfulness requires every locked label to lie in `supp(μ)={A,B}`.
A history that locks `C` at any site of `W` is not lawful. The four prefix
histories lock only `A` and remain lawful at every occupancy, including
`N=4`. A mixed full lock `(A,B,A,B)` is likewise lawful and has rate `1`.
Zero mass at `C` excludes a label; it does not cap the number of locks.

The reconstructed 2-site star `{0,e1}` with the same `μ` likewise admits
a single lock of `A` and a double lock `(A,B)`. Those formation counts
`1` and `2` are compatible with the same content law. They show unfixed
occupancy at a coarser grain. They do not replace Theorem 2: two counts
on a 2-site set are not a proof that no functional of `μ` can match four
distinct window rates.

## Theorem 5 — Scoped Residual

**Claim.** A physical formation-rate supplier remains open. This note does
not adopt a Poisson intensity, a constant `λ`, or axiom text.

**Proof.** Theorems 1 and 2 show that the empirical window rate is not a
function of the declared content law. Theorem 3 shows that forcing every
site to form is a selector rather than a consequence of Admissibility or
Record. Those facts prune the route that would read a rate off `μ` alone.

They do not close a later physical supplier. A Poisson intensity, a
constant `λ`, a dynamics that would output a unique occupancy fraction, or
an axiom sentence naming a rate would be extra objects. None of those
objects is derived here, and none is declared. The quoted rate non-supply
sentence already withholds a rate; it does not become a rate law by being
quoted. An axiom edit that named a rate is not required by the four-value
rejector and is not performed.

The residual is scoped. It does not say that a later physical rate cannot
be reached by some later bridge. It says that the present content law,
the occurrence sentence, and the always-form selector do not supply one.

## Boundary And Non-Claims

The note does not:

- edit an axiom sentence, or argue that an axiom update is necessary;
- adopt a formation rate, a Poisson intensity, or a constant `λ`;
- identify `{A,B,C}` with a physical laboratory basis, or replace the
  full one-site domain `M_2(C)`;
- derive the masses `1/3`, `2/3`, `0` from nearest-neighbor data;
- classify every lawful history on `Z^3`, or install a dynamics;
- treat the reconstructed 2-site counts as a landed parent.

The scope is the exact functional gap on one 4-site window: four lawful
rates, no `μ`-only map, and a scoped residual that a physical rate
supplier remains extra.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current rate non-supply sentence | premise | quoted; no edit |
| current occurrence sentence Records form. | premise | quoted; no edit |
| current finite-menu support clause | premise | quoted; no edit |
| declared masses `1/3`, `2/3`, `0` | declared content law | computed here |
| four prefix histories and `r=k/4` | Theorem 1 | computed here |
| `μ`-only constancy versus four rates | Theorem 2 | computed here |
| always-form selector | Theorem 3 | displayed; not adopted |
| 2-site counts `1` and `2` | reconstructed witness | computed here; not a parent |
| physical rate supplier, Poisson `λ` | residuals | extra; not declared |

The exact advance is a finite four-rate rejector for maps of a content
law. Independent audit is required. This note authors no audit verdict.

## Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | The axiom memo states that the distribution does not supply the formation site, probability, or rate. The named residual is a physical formation-rate supplier from Admissibility or Record. This note asks whether a functional of the declared content law already equals the empirical window rate, and answers no. |
| V2 | New content? | Searched `origin/main` at `c45dd5ab30` by `git grep` for a formation-rate functional, an empirical window rate `N(h)/|W|`, and a map `ρ(μ)=r(h)`. Hits: the axiom memo states the type split and withholds site, probability, and rate; the 2026-07-08 formation-rate law-class note is a conditional calculus identity for a supplied `F(A(r))`, not a uniqueness gap for a map from a content law to an empirical window rate; other formation-rate notes withhold a rate without exhibiting four lawful values or rejecting `ρ(μ)`. An unmerged 2-site occupancy exhibit with formation counts `1` and `2` is a sibling count witness, not a landed functional-uniqueness theorem, and is reconstructed here rather than cited as a parent. No landed four-rate rejector appears on that commit. |
| V3 | Independently checkable? | Textbook occupancy rate `N/n` does not mention Record, Admissibility, or a content law `μ`. The runner recomputes `r(h)=N(h)/4` and lawfulness from the declared masses in exact `Fraction` arithmetic. |
| V4 | More than a restatement? | Yes. The discriminating witnesses are `r(h_1)=1/4` against `r(h_4)=1` on one content law. Those two rationals are not a restatement of the rate non-supply sentence. |
| V5 | One-step relabel? | No. The claim is not a corollary of the axiom sentence alone. That sentence withholds a rate; it does not name the four prefix histories, the empirical window rate, or the constancy rejector that no `ρ(μ)` can match `1/4` and `1` at once. |

## No-Go Discipline Gate (Theorems 2, 3, and 5 only)

The negative claims are restricted to: no functional of the declared
content law equals the empirical window rate on every lawful history; the
always-form rule is a selector, not a theorem of Admissibility or Record;
a physical rate supplier remains extra and is not declared. The gate does
not ship a global non-existence theorem against later physical rates.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| functional `ρ(μ)` | take any map of the content law alone and ask it to equal `r(h)` on `{h_1,…,h_4}` | Theorem 2: the map is constant, the rates are `1/4,1/2,3/4,1` | **ATTEMPTED** |
| always-form selector | require every site of `W` to lock | Theorem 3: forces `r=1`; contradicts `r(h_1)=1/4`; extra selector | **ATTEMPTED** |
| Poisson intensity `λ` | declare a constant intensity and read it as the window rate | Theorem 2 and Theorem 5: a single rational cannot match four rates; not declared | **ATTEMPTED** |
| 2-site counts | take lawful formation counts `1` and `2` on `{0,e1}` as if they closed the functional gap | Theorem 4: reconstructed as a coarser occupancy witness; two counts are not a four-rate uniqueness proof | **ATTEMPTED** |
| axiom edit naming a rate | treat the residual as requiring an axiom-sentence change | Theorem 5: the four-rate rejector does not require an axiom edit; none is performed | **ATTEMPTED** |
| `μ(C)=0` forbids `N=4` | read zero mass at `C` as a cap on occupancy | Theorem 4: `h_4` locks four copies of `A` and is lawful | **ATTEMPTED** (mutation) |

### N2 — wall independence

Theorems 2, 3, and 5 close only the route that would read a window rate
off the content law, off the always-form selector, or off a declared
Poisson intensity. They do not close a later physical supplier, a later
dynamics that would output a unique occupancy fraction, or a later
content-only bridge that is not a map of `μ` alone. Those walls remain
independent. Four distinct lawful rates do not by themselves make a rate
law.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| finite menu `{A,B,C}` and masses `1/3,2/3,0` | declared content law |
| support `{A,B}` | computed from positive mass |
| 4-site path `W` and tetrahedron of size `4` | declared windows |
| prefix histories `h_k` and `r=k/4` | explicit witnesses |
| occurrence `N≥1` | quoted Record sentence |
| always-form selector | extra rule; displayed |
| 2-site counts `1` and `2` | reconstructed coarser witness |
| Poisson `λ` and a physical rate supplier | residuals; not declared |
| axiom edit naming a rate | live governance path; not required |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | rate non-supply sentence; Records form.; finite-menu support | quoted as premises only; no edit |
| four prefix histories | `r ∈ {1/4,1/2,3/4,1}` | computed here |
| `μ`-only maps | constancy on those histories | computed here |

No unmerged occupancy note is used as a parent. The 2-site counts are
recomputed here.

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | menu points `{A,B,C}` and the four prefix rates | no classification of every history on `Z^3` |
| per site | occupancy is a per-site 0/1 mark on one 4-site window | no composite carrier or lattice source field |
| per mode | empirical rate `N/4` and lawfulness, not spectral modes | no harmonic-mode exhaustion |
| per block | four-rate rejector, always-form selector, and the scoped residual only | no Poisson law and no axiom edit |
| lattice-wide | checked and not executed | no lattice-wide formation process or rate law |

The residual is a functional gap on one window. It is not lattice-wide.

### N6 — live partial-closure paths

1. A later physical construction that supplies a unique occupancy
   fraction by more than the content law — for example a declared
   dynamics — without editing an axiom.
2. A later selector other than always-form, if and when it is derived
   rather than declared. Always-form itself remains extra.
3. A later executable intensity, including a Poisson law, if and when it
   is derived. A constant `λ` is not forced by `μ`.
4. An owner-approved typed axiom addition that named a rate. The
   four-rate rejector does not require that addition.

The quoted sentences already withhold a formation rate and require only
that records form. They do not name `ρ` or `r(h)`. No axiom sentence is
edited here.

### N7 — hostile steelman

> The axiom memo already says the distribution does not supply the rate,
> and Records form. already means that every site forms, so the window
> rate is `1` and Theorem 2 is empty.

**Answer.** Records form. is occurrence: at least one lock exists in a
completed history. It does not fill every site. Theorem 1 exhibits four
lawful nonempty histories with rates `1/4` through `1`. Theorem 3 is
exactly the gap between occurrence and the always-form selector. The
axiom sentence withholds a rate; Theorem 2 is the finite rejector that no
function of `μ` can return both `1/4` and `1`. Withholding is not the
four-value proof.

### N8 — cross-cycle echo

The axiom reading note already separates content-law support from site
and rate. The 2026-07-08 formation-rate law-class note is a conditional
chain-rule identity for a supplied differentiable `F(A(r))`; it does not
select `F` and does not discuss a map `ρ(μ)`. The present four-rate
rejector does not reverse those boundaries. It answers a different
question: among maps of one declared content law, the empirical window
rate is not determined; among Record readouts, a rate law is still extra.

**Gate disposition.** PASS for the four-rate functional gap and for the
scoped residual that a physical rate supplier remains extra. FAIL / DO
NOT SHIP for “a rate is derived,” “always-form is a theorem,” or “an
axiom edit is required.”

## Primary Runner

[`scripts/content_law_does_not_determine_formation_rate_functional_2026_08_13.py`](../scripts/content_law_does_not_determine_formation_rate_functional_2026_08_13.py)
recomputes the three masses, support, the four prefix histories, the
empirical rates `1/4,1/2,3/4,1`, `μ`-only constancy, the always-form
selector, the illicit `C` lock, and the reconstructed 2-site counts in
exact rational arithmetic. Identity gates call `empirical_rate(h)` and
`lawful(h, μ)`. A predicate `rate_is_function_of_mu` that returns one
rational for all histories with this `μ` must fail Theorem 2. Replacing
the four histories by four copies of `h_1` must fail four distinct rates.
A predicate that `μ(C)=0` forbids `N=4` must fail, because all four locks
can be `A`.
