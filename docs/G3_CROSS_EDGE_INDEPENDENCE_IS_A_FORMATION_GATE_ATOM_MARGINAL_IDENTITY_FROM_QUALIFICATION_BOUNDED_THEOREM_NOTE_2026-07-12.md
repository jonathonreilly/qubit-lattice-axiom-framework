# Cross-Edge Independence Is a Formation-Gate Atom; Marginal Identity Follows from the Qualification Under Law-Equivalence (Bounded Theorem)

**Date:** 2026-07-12
**Type:** bounded_theorem
**Claim scope:** formation-gate consolidation plus Qualification-conditional
single-registration marginal identity on a two-cell registered quotient; when
the two-registration answer is represented as a coupling of those marginals,
cross-edge independence is isolated, not derived.
**Primary runner:**
[`scripts/frontier_cross_edge_formation_gate_2026_07_12.py`](../scripts/frontier_cross_edge_formation_gate_2026_07_12.py)
**Runner cache:**
[`logs/runner-cache/frontier_cross_edge_formation_gate_2026_07_12.txt`](../logs/runner-cache/frontier_cross_edge_formation_gate_2026_07_12.txt)

> **VERDICT (bounded).** The cross-edge outcome-factorization condition
> (legacy shorthand: G3) and the
> per-cell formation weight occupy one formation gate. On the registered menu
> `X = {s,d}`, the single-registration formation answer is a weight vector,
> while the two-registration formation answer is a coupling of two such
> vectors. The Qualification and Lattice axioms force identical marginals only
> when (LE) the two fresh-site registrations have the same complete supplied
> formation-law condition after lattice transport and (LAW) the formation
> rule is a law in the axiom sense. Under those named elements the joint table
> has one free coordinate `a`; `C_ss = 0` then solves exactly to `a = p^2` and
> hence to the product law. No source inspected here supplies that last
> equation. Independence remains the irreducible cross-edge statistics atom.

> **BOUNDARY.** This note adopts no formation dynamics, product/default rule,
> physical-independence theorem, or supplied product-law condition. The Qualification says
> same condition gives the same answer; it does not relate joint answers at
> two events. Registrations at different epochs can have different record
> environments and therefore need not satisfy (LE).

## 1. Witnessed source surface and the consolidation duty

The witnessed surface is deliberately finite: the
[`outcome-factorization no-go`](G3_OUTCOME_FACTORIZATION_FROM_UNRAVELED_STEP_LAW_NARROW_NO_GO_NOTE_2026-07-11.md),
the
[`formation-gate relocation theorem`](KOIDE_FORMATION_GATE_RELOCATION_TIED_MEASURE_PER_CELL_WEIGHT_COMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the
[`fresh-site double-registration theorem`](RECORD_PERMANENCE_FORCES_FRESH_SITE_DOUBLE_REGISTRATION_AND_AGREEMENT_SURVIVAL_BOUNDED_THEOREM_NOTE_2026-07-11.md),
and the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md). The claim that no
supplier is present is confined to those four sources.

The outcome-factorization no-go names residual 4 verbatim:

> many-edge structure: **cross-edge independence and convolution structure are
> not tested here**.

It then gives the positive-discharge requirement verbatim:

> A positive discharge of G3 must deliver a cross-edge independence theorem on
> the registered quotient — not a single-edge non-degeneracy or a bi-frame
> quasi-stationarity of the mean, both of which this note shows are
> factorization-blind.

The minimal axioms place the relevant rule outside axiom content in this
verbatim open-gate sentence:

> context selection, measurement basis selection, Born weights, probability
> rules, update laws, decoherence mechanisms, and formation rules (which
> admissible possibility a new record locks, at which site, with what weight,
> or at what rate);

The formation-gate relocation theorem puts the normalized single-registration coordinate
`w` at exactly that gate. It constructs the formation state

```text
phi_w = (w, 1-w) on {singlet cell, doublet cell}
```

without choosing `w`. On the same labeled two-cell quotient used below,
`p = Pr(s) = w`. A joint law of successive formations assigns weights (or,
for a rate formulation, normalized history rates) to the four registered
histories `(s,s)`, `(s,d)`, `(d,s)`, `(d,d)`. Thus its marginal coordinate
`p` and its coupling coordinate live in the same formation-law object:

```text
single-event formation data       p = w,
two-event formation data          m(j,k),
compatibility                     sum_k m(j,k) = p_1(j),
                                  sum_j m(j,k) = p_2(k).
```

This is a consolidation, not an identification: knowing `w` does not select a
coupling. The formation gate has a fiber of joint laws over its marginal
weight. The cross-edge factorization condition asks for one point in that fiber.

The fresh-site theorem supplies the geometry—successive records occupy distinct
sites and earlier records remain—but not their statistical coupling. Its
adjacent named premise is, verbatim:

> a **common epoch-comparable lane-readout rule**: the same mapping from
> record content to the coordinate `r_k` is used at every formation epoch, so
> values at different epochs may be compared. The rule does not assume those
> values are equal.

That premise concerns equality of the mapping used to read the deterministic
lane ratio `r`, not equality of the values produced at different epochs. It is
neither equality of the `{s,d}` formation marginals nor independence of the outcomes.
Fresh sites can carry correlated records, and equal epoch readout values can
hold or fail without deciding `m(j,k)`. The fresh-site note accordingly leaves
outcome factorization open.

Therefore, on the witnessed surface, the outcome-factorization no-go explicitly leaves independence
untested, the axioms explicitly leave formation weights/rates open, the
relocation theorem leaves `w` open, and the fresh-site theorem supplies only
geometry plus a distinct named readout premise. There is no cross-edge
independence supplier on this surface. The joint-statistics residue and the
formation weight `w` consolidate at one formation gate.

## 2. Exact finite setup and the law-equivalence element

Let `X = {s,d}` be the registered quotient. A fresh-site registration event
`e_i` has target site `x_i`, epoch label `t_i`, and a **complete supplied
formation condition** `c_i`. The condition contains every datum admitted in
the domain of the proposed formation law: in particular the transported local
admissibility condition, the admissible two-cell menu and its labels, the
nearest-neighbor/record environment if the law uses it, and every other
supplied law-domain variable. A bare site name or epoch counter is not an
extra input unless supplied structure makes it part of the condition.

The two axiom sentences doing the work are:

> No site is privileged. Sites are distinguished by the supplied lattice
> structure alone.

and

> A law privileges no states. Its domain is a supplied condition, and at every
> state where the condition holds it gives exactly one answer.

Write `G_lat` for standard lattice translations followed by proper cubic
rotations. Conditions are compared after transporting their sites, local
menus, labels, and domain data by `G_lat`.

**(LE) Law-equivalence element (named premise, exact statement).** Two
fresh-site registrations `e_1` and `e_2` are law-equivalent when there is a
`g in G_lat` taking `x_1` to `x_2` such that, after using `g` to identify the
two registered menus and all supplied domain data,

```text
g.c_1 = c_2 =: c,
g.X_1 = X_2 = {s,d},
g.s = s,   g.d = d.
```

Equivalently, their complete conditions define the same element `c` of the
formation law's domain modulo supplied lattice structure. This is a real
premise. Freshness and lattice-related sites alone do not imply it: at two
epochs of a realized history, permanent neighboring records can make
`g.c_1 != c_2`.

**(LAW) Formation-law element (named premise, exact statement).** The proposed
single-registration formation rule is a law in the Qualification's sense and
its unique answer is a normalized weight vector on `X`:

```text
F : C_form -> Delta(X),
F(c) = (f(c), 1-f(c)),       0 <= f(c) <= 1.
```

Its full argument is the supplied condition `c`; it has no additional bare
site or registration-index argument. This note neither derives the existence
of `F` nor selects the function `f`.

## 3. T1 — cross-edge independence is a formation-gate atom

For two successive fresh-site formations with conditions `(c_1,c_2)`, let

```text
m(j,k | c_1,c_2) >= 0,       sum_{j,k} m(j,k | c_1,c_2) = 1
```

be the formation law's two-registration history weights. Its projections are
the single-registration formation answers:

```text
sum_k m(j,k | c_1,c_2) = F_j(c_1),
sum_j m(j,k | c_1,c_2) = F_k(c_2).
```

Cross-edge independence is the additional formation-law equation

```text
m(j,k | c_1,c_2) = F_j(c_1) F_k(c_2)    for all j,k in X.
```

It decides the weights/rates of joint formation histories and is therefore a
multi-registration statistic of the formation law, not a consequence of the
record geometry and not a property of the tied Berezin measure underneath the
formation state. This places it at the same open formation gate as `w`, while
keeping the marginal coordinate and coupling coordinate mathematically
distinct.

## 4. T2 — conditional marginal identity from the Qualification

**Theorem (two-registration marginal identity).** Assume (LE) for `e_1,e_2`
and (LAW). Then the two single-registration formation marginals are identical:

```text
p_1(s) = f(c_1) = f(c) = f(c_2) = p_2(s) =: p,
p_1(d) = 1-p = p_2(d).
```

**Proof.** By (LE), after the supplied lattice identification the complete
arguments of `F` are equal: `c_1 = c_2 = c`. By (LAW) and the Qualification,
`F` gives exactly one answer at `c`; by “No site is privileged,” no bare site
label can change that answer. Hence `F(c_1)=F(c_2)`. Component equality gives
the displayed result. ∎

This pays the source no-go's residuals 1+3 only in their role as the
identical-marginal prerequisite on the registered formation quotient, and only
under (LE)+(LAW). It does not prove stationarity or edge identity for another
object, and it does not say different supplied conditions have the same
answer.

**Joint-law boundary inside the theorem.** The conclusion is only
`F(c_1)=F(c_2)`. The proof contains no equation relating joint weights to
products of marginal weights. Indeed, for any `0 < p < 1`, both

```text
m_product = (p^2, p(1-p), p(1-p), (1-p)^2),
m_locked  = (p,   0,      0,      1-p)
```

in the order `(ss,sd,ds,dd)` have the identical marginals `(p,1-p)`, while
only the first is independent. The Qualification's same-condition/same-answer
rule therefore fixes the marginal answer and nothing about the coupling.

### Why this does not contradict the unraveled-step findings

The outcome-factorization no-go reports that the **unraveled step law** has a link-level step mean
moving `O(1)` at every depth and that displayed edge laws differ at order one.
That step law is an induced-link, measure-side object. That source's deliverables
are single-registration functionals of that object. The `F` in T2 is instead
the downstream **formation law** whose answer is a registered outcome-weight
vector for a complete supplied formation condition.

T2 therefore makes no claim that the unraveled step mean is stationary, and
no claim that two epochs with different record environments are
law-equivalent. Even for `F`, different conditions may give different
marginals. The order-one depth motion and T2 can both hold because they concern
different objects; additionally, T2 is activated only by equality of the full
formation condition.

## 5. T3 — the irreducible independence atom

Under T2, write

```text
a = m(s,s).
```

The two identical marginal equations and normalization solve the complete
joint table exactly:

```text
m(s,s) = a,
m(s,d) = p-a,
m(d,s) = p-a,
m(d,d) = 1-2p+a,
max(0,2p-1) <= a <= p.
```

Define the registered-quotient cumulant

```text
C_ss = m(s,s) - p_s p_s = a-p^2.
```

Imposing cross-edge independence at this binary quotient gives

```text
C_ss = 0
=> a-p^2 = 0
=> a = p^2.
```

Substitution then gives, without an endpoint or target value inserted,

```text
m(s,d) = p-p^2     = p(1-p),
m(d,s) = p-p^2     = p(1-p),
m(d,d) = 1-2p+p^2 = (1-p)^2.
```

Thus `m(j,k)=p_j p_k` for every `j,k`. Conversely, product factorization gives
`C_ss=0`. On this two-cell quotient with T2's identical marginals, the sole
remaining cross-edge statistics atom is exactly

```text
C_ss = 0.
```

For `p=0` or `p=1` the admissible coupling fiber is already a singleton. For
`0<p<1`, `a=p^2` is the unique independent point in the nontrivial Fréchet
interval. No independence premise has been adopted in obtaining this
conditional reduction.

## 6. What could derive or condition independence (none adopted)

| possible payer | grade used here | exact content required | disposition |
|---|---|---|---|
| formation dynamics | prospective derivation or bridge | Derive a two-event formation kernel on law-equivalent, disjoint fresh sites and prove `m(j,k\|c,c)=F_j(c)F_k(c)` for every `j,k`. | Open formation gate; no supplier on the witnessed surface. |
| product / maximal-ignorance default | candidate note-owned licensing criterion, analogous in grade to the classification theorem's note-owned criterion | Given only fixed registered marginals and no supplied coupling datum, license the unique product coupling; equivalently, on the finite menu choose the unique maximum-Shannon-entropy coupling `F(c_1) tensor F(c_2)`. | Candidate only. It would require a derivation or a separately approved registry/policy change; neither occurs here. |
| physical locality | prospective physical theorem | Prove a screening/factorization statement for formation outcomes at the relevant disjoint sites, strong enough to imply the displayed product equation. | Fresh-site disjointness alone is insufficient. Record additivity concerns readout `I`, not probability. |
| supplied product-law condition | explicit non-satisfying condition | Supply `m(j,k\|c_1,c_2)=F_j(c_1)F_k(c_2)` on the registered quotient. | Would leave every consumer conditional and would not chain-satisfy; not adopted. |

The locality distinction is exact. The Record axiom says that for disjoint
records the scalar readout is pointwise additive,

```text
I(R_1 union R_2) = I(R_1) + I(R_2).
```

Two perfectly correlated Bernoulli records can satisfy that identity on every
outcome while having `C_ss=p-p^2 != 0` for `0<p<1`. Additivity is a statement
about the value assigned to a union of records; independence is a statement
about the probability of their joint contents. The former must not be
laundered into the latter.

## 7. Residuals and fragile interfaces

1. **Cross-edge independence:** open. With (LE)+(LAW), it is the sole
   joint-statistics equation, `C_ss=0`, on this binary quotient.
2. **Law-equivalence (LE):** named conditional element, not automatic across
   epochs. Any difference in complete supplied record environment blocks T2.
3. **Formation law (LAW):** named conditional element. The axioms say what a
   law must look like; they do not supply the formation law or its values.
4. **Multi-registration domain:** T1 treats normalized weights/rates of finite
   formation histories as joint statistics of the formation rule. If a future
   framework formalism splits single-event formation and history coupling into
   separately named laws, both remain at the same open gate but the packaging
   should be renamed.
5. **Label transport:** T2 assumes the supplied lattice identification also
   identifies the registered labels `s,d`. A symmetry that permutes or changes
   the quotient labels requires the corresponding equivariant version, not
   literal component equality.

## 8. What this note does not claim

- It does not derive, assume, prefer, supply, or adopt cross-edge independence.
- It does not derive a formation dynamics, a value of `w` or `p`, or a joint
  formation law.
- It does not make all fresh sites law-equivalent. Equality of the complete
  supplied formation condition is (LE), and changing record environments can
  defeat it.
- It does not infer any joint distribution from the Qualification. That axiom
  gives same-condition/same-answer for a law; it does not impose product
  structure.
- It does not infer statistical independence from spatial disjointness or
  from the Record axiom's additivity of scalar readout `I`.
- It does not identify the unraveled step law with the formation law, and it
  does not contradict the reported order-one motion of the former.
- It does not choose the product/maximal-ignorance candidate criterion.
- It does not threshold a comparator or insert a target value on a derivation
  path. All runner arithmetic is symbolic or exact rational arithmetic.

## 9. Reproved here and cited at source scope

**Reproved by the paired runner:** the (LE)+(LAW) marginal-identity implication;
the complete identical-marginal joint-table solve; its exact positivity
interval in both `p<=1/2` and `p>=1/2` regimes; `C_ss=0 <=> a=p^2`; full binary
factorization after substitution; a same-marginal correlated comparator; and
the compatibility of pointwise additive readout with nonzero cross-edge
cumulant.

**Cited at source scope:**

- [Outcome-factorization no-go](G3_OUTCOME_FACTORIZATION_FROM_UNRAVELED_STEP_LAW_NARROW_NO_GO_NOTE_2026-07-11.md): residual 4,
  the positive-discharge sentence, the identical-marginal prerequisite, and
  the single-registration scope of the unraveled-step results.
- [Formation-gate relocation theorem](KOIDE_FORMATION_GATE_RELOCATION_TIED_MEASURE_PER_CELL_WEIGHT_COMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-12.md): the
  independent per-cell coordinate `w`, the two-cell formation state, and its
  location at the axioms' open formation gate.
- [Fresh-site double-registration theorem](RECORD_PERMANENCE_FORCES_FRESH_SITE_DOUBLE_REGISTRATION_AND_AGREEMENT_SURVIVAL_BOUNDED_THEOREM_NOTE_2026-07-11.md):
  T1's fresh-site/full-retention geometry and T2's distinct, supplied common
  epoch-comparable lane-readout rule. Its repaired T3 is a finite-horizon
  persistence bound and is not consumed here.
- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md): Lattice,
  Qualification, Record additivity, and the verbatim formation-rule open gate.

## 10. Verification

Run:

```bash
python3 scripts/frontier_cross_edge_formation_gate_2026_07_12.py
```

Expected: numbered `[PASS]` lines, then a verdict-first summary containing the
exact T2 statement, (LE), the four possible independence payers, the check
count, proposed `claim_scope`, and hostile-review uncertainties. The summary
contains `TOTAL: PASS=20 FAIL=0`; the process exits `0` if and only if
`FAIL=0`.
