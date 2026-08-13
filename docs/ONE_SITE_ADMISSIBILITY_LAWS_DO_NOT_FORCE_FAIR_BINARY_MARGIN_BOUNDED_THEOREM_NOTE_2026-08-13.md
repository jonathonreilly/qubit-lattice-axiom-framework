---
claim_id: one_site_admissibility_laws_do_not_force_fair_binary_margin_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On a two-element possibility set, Admissibility names a nearest-neighbor-conditioned one-site law and does not equate the distinct full-support values p=1/2 and p=1/3; an independent product on {0,1}^2 is uniform iff every margin is 1/2; locking one factor does not reweight the other; the counting measure on Z/2 is an extra selector; independence plus one-site laws do not force a fair margin or formation."
upstream_dependencies:
  - minimal_axioms
  - admissibility_global_measure_menu_kernel_type_separation_bounded_theorem_note_2026-08-10
runner: scripts/one_site_admissibility_laws_do_not_force_fair_binary_margin_2026_08_13.py
---

# One-Site Admissibility Laws Do Not Force A Fair Binary Margin

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact Bernoulli products on declared two-element menus; value-open
margins; lock-non-reweighting of an independent factor; counting measure on
`Z/2` displayed as an extra selector.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/one_site_admissibility_laws_do_not_force_fair_binary_margin_2026_08_13.py`](../scripts/one_site_admissibility_laws_do_not_force_fair_binary_margin_2026_08_13.py)

## Result Up Front

The August 10 type-separation note
[`ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md`](ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md)
leaves open a physical construction that produces registered measurable event partitions. A finite register of bits would be one such construction. This note does not install that compiler. It proves that Admissibility names a one-site distribution and does not force the fair binary margin `p=1/2`.

The current Admissibility sentence in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) is quoted only
as a premise and is not edited:

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

The Admissibility reading note is quoted only as a premise. The distribution concerns which possibility a forming record locks, conditional on formation at that site; it does not supply the formation site, probability, or rate.

The current Record sentences are quoted only to type a binary readout of a locked local possibility as a bit. Formation is not derived:

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

For any finite collection of pairwise-disjoint records, scalar readout `I` is additive, with `I(empty)=0`.

Five exact statements locate the split.

1. **Value-open binary menus.** The pairs `p=1/2` and `p=1/3` are two distinct one-site laws on `{0,1}`. The Admissibility sentence names a distribution determined by nearest-neighbor conditions and does not equate those two values. Both have full support, so both possibilities are available.
2. **Product uniformity criterion.** For two independent one-site laws the four atoms are `P(00)=p1 p2`, `P(01)=p1(1-p2)`, `P(10)=(1-p1)p2`, `P(11)=(1-p1)(1-p2)`. These four equal `1/4` if and only if `p1=p2=1/2`. The witness `p1=p2=1/3` gives `P(00)=1/9 ≠ 1/4`. The witness `p1=1/2`, `p2=1/3` gives `P(00)=1/6 ≠ 1/4`.
3. **Lock does not reweight an independent factor.** On the product with margins `(1/2, 1/3)`, conditioning on the first bit locking to `0` leaves the second-bit law at `p2=1/3`, not `1/2`.
4. **Counting selector is extra.** The uniform counting measure on `{0,1}` (Haar on `Z/2`) is the law `p=1/2`. It is a selector, not a theorem of Admissibility. It is displayed; it is not installed.
5. **Scoped negatives.** Graph separation, even if assumed as a source of independent one-site laws, does not force fair margins and does not force formation. The note is not a physical menu compiler.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 1/2 versus 1/3 one-site pair, the n=2 product-uniformity criterion with witnesses 1/9 and 1/6, and the lock-non-reweighting identity are proved by exact Fraction arithmetic on declared two-element menus; formation and a physical fair-margin compiler remain open."
trace_class: negative_route_pruning
target_claim_id: fair_binary_margin_from_admissibility
target_blocker_text: "derive a fair binary margin p=1/2 for auxiliary Record bits"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "A physical compiler still needs a selector for p=1/2 and a formation rule; counting measure on Z/2 is extra. Do not adopt axiom text."
conditional_surface_status: "exact for the 1/9 versus 1/4 product split, the lock-non-reweighting identity, and the displayed counting selector; formation and a physical fair-margin compiler remain open"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Work on a declared two-element possibility set `{0,1}` at a site. This is a finite menu, not the full one-site algebraic domain `M_2(C)`. A **one-site law** is a pair

`(p, 1-p)`, `p = Fraction` in `(0,1]`,

read as `P(0)=p` and `P(1)=1-p`. The open interval `(0,1)` is the full-support locus. The endpoint `p=1` is a singleton-support boundary law and is not used as a fairness witness.

A **product of n independent one-site laws** with margins `p_1,...,p_n` is the law on `{0,1}^n` given by

`P(b_1,...,b_n) = ∏_k p_k^{1-b_k} (1-p_k)^{b_k}`.

Executed `n` is `2`. The four atoms are

```text
P(00) = p1 p2
P(01) = p1 (1-p2)
P(10) = (1-p1) p2
P(11) = (1-p1) (1-p2)
```

That table is uniform when every atom equals `1/4`.

A **Record lock** of a coordinate is ordinary conditioning of the product on that coordinate taking a locked admissible value. Content-only readout and additivity of `I` type a locked `{0,1}` possibility as a bit. They do not reweight an independent factor, and they do not force formation.

**Graph separation** is used only as an optional independence hypothesis: one-site laws whose nearest-neighbor condition supports are disjoint may be multiplied. The margin theorems do not depend on how independence was obtained, and they do not re-prove any lattice listing.

The **counting measure** on `{0,1}` is the two-point Haar measure of the group `Z/2`. It is the one-site law `p=1/2`. It is a selector.

The August 10 interface phrase, quoted only as the open parent, is that a physical construction that produces registered measurable event partitions remains open. The present objects are finite-menu Bernoulli laws, not that construction.

## Exact Target And Obligation Graph

**Exact target.** On declared two-element menus, exhibit two distinct full-support one-site laws; prove that an independent n=2 product is uniform if and only if both margins are `1/2`; show that locking one independent bit leaves the other margin unchanged; and record that the counting measure on `Z/2` is an extra selector, without deriving formation or a physical fair-bit compiler.

| Obligation | Role | Disposition |
|---|---|---|
| pin the Admissibility distribution sentence | premise | quoted; no edit |
| pin the formation reading note | premise | quoted; formation not derived |
| pin Record lock, content-only, and additivity | typing only | quoted; formation not derived |
| exhibit `p=1/2` and `p=1/3` as distinct full-support laws | Theorem 1 | exact pairs |
| prove the n=2 product is uniform iff `p1=p2=1/2` | Theorem 2 | four-atom algebra |
| witnesses `1/9` and `1/6` | Theorem 2 | `(1/3)*(1/3)` and `(1/2)*(1/3)` |
| show lock of bit 1 leaves bit 2 at `p2` | Theorem 3 | conditional of a product |
| display counting Haar as `p=1/2` and not derived | Theorem 4 | selector; not installed |
| record that fairness and formation are not forced | Theorem 5 | scoped negative |
| derive a physical menu compiler of fair formed bits | autonomous closure | open |
| claim that no compiler exists | non-claim | not attempted |

## Theorem 1 — Value-Open Binary Menus

**Claim.** The pairs `p=1/2` and `p=1/3` are two distinct one-site laws on `{0,1}`. Admissibility names a distribution and does not equate these two values. Both have full support, so both possibilities are available.

**Proof.** The one-site laws are the pairs

`(1/2, 1/2)` and `(1/3, 2/3)`.

These are unequal as ordered pairs of rationals. Each coordinate is strictly positive, so each law has support `{0,1}`. On a finite menu the Admissibility reading note identifies “available” with nonzero probability; both possibilities are therefore available under either law.

The governing sentence says only that, for each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions. That sentence names the *existence* of a condition-dependent law. It does not name a unique numerical value of `p`, and it does not contain an equation that would force `1/2=1/3`. Both pairs are therefore permitted one-site laws on the declared menu.

## Theorem 2 — Product Uniformity Criterion

**Claim.** For n=2 independent laws with margins `p1, p2`,

`P(00)=p1 p2`, `P(01)=p1(1-p2)`, `P(10)=(1-p1)p2`, `P(11)=(1-p1)(1-p2)`.

These four equal `1/4` if and only if `p1=p2=1/2`.

**Proof.** Independence is the product formula just written. Summation of the four atoms is `1` for every `(p1,p2)` in `(0,1]^2`. Uniformity on `{0,1}^2` is the four equations

`p1 p2 = 1/4`, `p1(1-p2)=1/4`, `(1-p1)p2=1/4`, `(1-p1)(1-p2)=1/4`.

Adding the first two gives `p1=1/2`. Adding the first and third gives `p2=1/2`. Conversely, if `p1=p2=1/2` then each atom is `(1/2)*(1/2)=1/4`.

**Witness.** `p1=p2=1/3` gives `P(00)=(1/3)*(1/3)=1/9 ≠ 1/4`. The remaining atoms are `2/9`, `2/9`, and `4/9`, none of which is `1/4`.

**Witness.** `p1=1/2`, `p2=1/3` gives `P(00)=(1/2)*(1/3)=1/6 ≠ 1/4`. The remaining atoms are `1/3`, `1/6`, and `1/3`.

Thus a product of one-site laws is uniform on `{0,1}^n` only when every margin is `1/2`. The n=2 case already supplies the obstruction: biased factors remain allowed one-site laws, and their product is not the uniform table.

## Theorem 3 — Lock Does Not Reweight An Independent Factor

**Claim.** On a product with margins `p1=1/2`, `p2=1/3`, condition on the first bit locking to `0`. The conditional law of the second bit is still `p2=1/3`, not `1/2`.

**Proof.** Record lock of the first coordinate to the admissible value `0` is the conditional

`P(second=0 | first=0) = P(00) / P(first=0)`.

Independence gives `P(00)=p1 p2` and `P(first=0)=p1`, so the ratio is `p2` whenever `p1>0`. Substituting the executed margins,

`P(00)=1/6`, `P(first=0)=1/2`, `P(second=0 | first=0)=(1/6)/(1/2)=1/3`.

The complementary mass is `2/3`. The conditional second-bit law is therefore exactly `(1/3, 2/3)`, the original factor. It is not `(1/2, 1/2)`.

Content-only readout of the locked first bit returns the locked content `0`. Additivity of `I` is not used. Neither typing sentence changes the second factor.

## Theorem 4 — Counting Selector Is Extra

**Claim.** The uniform counting measure on `{0,1}` (Haar on `Z/2`) is the law `p=1/2`. It is a selector, not a theorem of Admissibility. Display it; do not install it.

**Proof.** The two-point set `{0,1}` is the group `Z/2` under addition modulo `2`. Its unique Haar probability, equivalently the normalized counting measure, assigns mass `1/2` to each point. That is the one-site law `p=1/2`.

Theorem 1 already exhibited a different full-support law `p=1/3`. The Admissibility sentence determines a distribution by nearest-neighbor conditions and does not name Haar measure, counting measure, or the equation `p=1/2`. Selecting the counting measure would force fairness; that selection is an extra rule. It is displayed here so that the residual is explicit. It is not treated as axiom content.

## Theorem 5 — Scoped Negatives

**Claim.** The following statements are not theorems of Admissibility and Record on the objects above, even if independent one-site laws are granted by graph separation.

1. Admissibility forces `p=1/2`. False by Theorem 1: `p=1/3` is a distinct full-support one-site law, and the distribution sentence does not equate the two values.
2. Graph separation forces uniform binary margins. False by Theorem 2: an independent product of one-site laws is allowed, including the biased witness `P(00)=1/9`. Uniformity holds only when every margin is already `1/2`.
3. Record lock of one independent bit forces the other bit to `1/2`. False by Theorem 3: the conditional second-bit law remains `1/3`.
4. The counting measure on `Z/2` is a theorem of Admissibility. False by Theorem 4: it is the law `p=1/2`, displayed as a selector.
5. Graph separation, or the one-site law itself, forces records to form. False: the Admissibility reading note states that the distribution concerns which possibility a forming record locks, conditional on formation at that site; it does not supply the formation site, probability, or rate.

**Scope.** The negatives are restricted to *forcing* `p=1/2` from Admissibility, *forcing* fairness from graph separation, *forcing* a reweighting from Record lock, *identifying* counting Haar with axiom content, and *forcing* formation. They do not say that no compiler exists. They do not say that bits are physically formed. They do not propose axiom text.

**Steelman.** A constant one-site law that happens to equal `p=1/2` is allowed. That special case does not empty Theorem 1. Theorem 1 says fairness is not *forced*; a fair law is an allowed special case, not a derivation that every one-site law is fair.

## Boundary And Non-Claims

The note does not:

- edit an axiom sentence, or argue that an axiom update is necessary;
- install a physical menu compiler of registered event partitions;
- claim that no such compiler exists;
- claim that auxiliary bits are physically formed, or that they are fair;
- install the counting measure on `Z/2` as a physical law;
- identify the present two-element menu with the full one-site domain `M_2(C)`;
- close content-only identification of a mathematical event label with Record readout beyond the quoted typing sentences.

The scope is the exact finite-menu split: value-open one-site laws, the product-uniformity criterion, lock-non-reweighting of an independent factor, and a displayed extra selector.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current Admissibility distribution sentence | premise | quoted; no edit |
| current formation reading note | premise | quoted; formation not derived |
| current Record lock, content-only, and additivity sentences | typing premises | quoted; formation not derived |
| August 10 type-separation note | open interface phrase only | parent dependency; not re-proved |
| n=2 Bernoulli product, witnesses `1/9` and `1/6`, conditional `1/3` | Theorems 1--4 | computed here |
| physical bit compiler (formation and fair margin) | residual | open |
| observed frequencies or fitted margins | none | not used |

The exact advance is a finite probability theorem on two-element menus. Independent audit is required. This note authors no audit verdict.

## Promotion Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | August 10 states that a physical construction that produces registered measurable event partitions remains open. The Admissibility reading note states that the distribution does not supply the formation site, probability, or rate, and the governing sentence does not name numerical values of `p`. This note executes the residual that a fair binary margin is not forced. It does not call the upstream interface unratified. |
| V2 | New content? | Searched `origin/main` at `c45dd5ab30` by `git grep` for fair binary margin, `p=1/2` from Admissibility, Haar on `Z/2`, and one-site Bernoulli products. Hits: the August 10 type-separation note names the registered-partition interface and leaves construction open; the Admissibility reading note withholds formation site, probability, and rate; the flavor central-state note records that `C3` central-state admissibility does not choose `p=1/2` versus `p=1/3` (a different object: central-block weight); the area-law primitive packet has a selector that fixes `p=1/2` (a different object); the occupancy-grain counting-measure note is a different object (registered grain menus). No landed two-element product-uniformity / lock-non-reweighting / `Z/2` counting-selector theorem appears on that commit. Unmerged lattice-separation listings are not premises. |
| V3 | Independently checkable? | Textbook Bernoulli products and two-point Haar measure do not mention Record bits, Admissibility nearest-neighbor conditions, or a locked auxiliary readout. The runner recomputes the four atoms and the conditional by exact `Fraction` arithmetic. |
| V4 | More than a restatement? | Yes. The exact witnesses `(1/3)*(1/3)=1/9 ≠ 1/4` and `(1/2)*(1/3)=1/6 ≠ 1/4`, and the identity that lock of bit 1 leaves bit 2 at `1/3`, are not restatements of the parent type-separation or of the formation reading note. |
| V5 | One-step relabel? | No. The claim is not a corollary of the Admissibility sentence or of August 10. Quoting “determined by nearest-neighbor conditions” does not by itself produce the `1/9` versus `1/4` split. |

## No-Go Discipline Gate (Theorems 1 and 5 only)

The negative claims are restricted to: Admissibility does not force a fair binary margin; graph separation does not force a fair binary margin; Record lock does not reweight an independent factor to `1/2`; counting Haar is extra; formation is not forced. The gate does not ship a global non-existence theorem against compilers.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| force `p=1/2` from Admissibility | deduce a unique fair margin from the distribution sentence | Theorem 1: `p=1/3` is a distinct full-support law; the sentence does not equate the values | **ATTEMPTED** |
| force `p=1/2` from graph separation | grant independent one-site laws and deduce uniformity | Theorem 2: the product is uniform iff every margin is already `1/2`; witness `1/9 ≠ 1/4` | **ATTEMPTED** |
| force `p=1/2` from Record lock | condition on bit 1 locking to `0` and deduce that bit 2 is fair | Theorem 3: the conditional law remains `1/3` | **ATTEMPTED** |
| counting Haar selector | identify the normalized counting measure on `Z/2` with axiom content | Theorem 4: that measure is the law `p=1/2`; it is displayed as extra | **ATTEMPTED** |
| axiom-text edit | replace the distribution sentence by a fairness rule | forbidden; no axiom sentence is edited | **ATTEMPTED** (closed as non-route) |
| force formation | deduce that records form from Admissibility or from independence | reading note: the distribution does not supply the formation site, probability, or rate | **ATTEMPTED** |
| replace the product by the uniform `1/4` table | declare every n=2 law uniform | fails the `p=1/3` witness `1/9` | **ATTEMPTED** (mutation) |

### N2 — wall independence

Theorems 1 and 5 close only forced fairness from Admissibility, forced fairness from independence, forced reweighting from lock, identification of counting Haar with axiom content, and forced formation. They do not close a later physical compiler, a later selector for `p=1/2`, or a content-only event-label bridge. Those walls remain independent.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| two-element menu `{0,1}` | declared finite menu |
| one-site law `(p, 1-p)` with `p` in `(0,1]` | declared object |
| independent product of one-site laws | declared n=2 map |
| Record lock as conditioning | declared typing of lock |
| uniform counting measure / Haar on `Z/2` | extra selector; not derived |
| record formation | open; not assumed as a theorem |
| graph-separated neighbor supports | optional independence hypothesis; not re-proved |
| full one-site domain `M_2(C)` | live escape; not executed here |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | Admissibility distribution sentence; formation reading note; Record lock, content-only, and additivity sentences | quoted as premises only; no edit |
| August 10 type-separation note | “a physical construction that produces registered measurable event partitions” remains open | interface parent only; not re-proved |

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | named margins `1/2`, `1/3` and atoms `1/4`, `1/9`, `1/6` | no classification of every law on `M_2(C)` |
| per site | one-site laws and the n=2 product on a two-element menu | no composite bonded-pair theorem |
| per mode | Bernoulli product atoms, not spectral modes | no harmonic-mode exhaustion |
| per block | value-openness, uniformity criterion, lock-non-reweighting, displayed selector | no dynamics, formation rate, or physical compiler |
| lattice-wide | checked and not executed | no lattice-wide no-go against compilers |

The obstruction is per-site / declared two-element menu; it is not lattice-wide.

### N6 — live partial-closure paths

1. A later selector that forces each binary margin to `p=1/2`.
2. A later derivation that records form at the relevant sites.
3. A content-only bridge from the locked local possibility to a registered event-partition label.
4. A different menu geometry, including the full one-site domain, if and when that object is constructed from the axioms.

The quoted axiom sentences already name nearest-neighbor conditions, lock, content-only readout, and additivity. Formation and a fair binary margin remain open selectors. No axiom sentence is edited here. An axiom-text change is not required by the present split.

### N7 — hostile steelman

> The counting measure on `{0,1}` is the unique translation-invariant probability on `Z/2`, so Admissibility has already selected `p=1/2`.

**Answer.** Uniqueness of Haar measure is a fact about the group `Z/2`. It is not a fact about Admissibility. The governing sentence permits any nearest-neighbor-conditioned law, including the executed witness `p=1/3`. Displaying Haar identifies the extra selector; it does not derive that selector from the axiom sentence. The discriminating facts remain `(1/3)*(1/3)=1/9 ≠ 1/4` and the lock identity of Theorem 3.

### N8 — cross-cycle echo

August 10 Theorems 1--3 are parent negatives about singleton mass, atomless restriction, and contextual restriction at one `M_2(C)` site. The present negatives are a different residual: a two-element menu still has value-open one-site laws, and neither independence nor Record lock forces those laws to be fair. The positive listing (Theorems 2--4) does not cancel the parent type-separation; it answers the open-construction interface at the narrower question of the numerical margin.

**Gate disposition.** PASS for the scoped finite-menu split and the negatives of Theorems 1 and 5. FAIL / DO NOT SHIP for "no compiler exists" or "bits are physically formed and fair."

## Primary Runner

[`scripts/one_site_admissibility_laws_do_not_force_fair_binary_margin_2026_08_13.py`](../scripts/one_site_admissibility_laws_do_not_force_fair_binary_margin_2026_08_13.py)
recomputes one-site pairs, n=2 products, the uniformity criterion, the lock conditional, and the displayed counting selector in exact `Fraction` arithmetic. Identity gates call `product_law(ps)` and `is_uniform`. A predicate `always_fair(p)` that returns true for every `p` in `(0,1]` must fail on `p=1/3`. Replacing the product by the uniform `1/4` table must fail the `p=1/3` witness `1/9`. A predicate that lock of bit 1 forces bit 2 to `1/2` must fail Theorem 3.
