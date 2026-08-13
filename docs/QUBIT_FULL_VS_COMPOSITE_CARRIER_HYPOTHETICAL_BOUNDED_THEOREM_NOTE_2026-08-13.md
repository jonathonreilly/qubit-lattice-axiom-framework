---
claim_id: qubit_full_vs_composite_carrier_hypothetical_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "Integer dimension facts 9>4 and 8>2 are reconstructed here: there is no injective C-linear map M_3(C)→M_2(C), and C^8 is not the one-site Hilbert space C^2. Current Qubit sentence S and displayed counterfactual S' agree that the one-site algebra is M_2(C). The wall 'color/P-HY cannot exist unless we add an axiom' is a reading of S as 'nothing physical is larger than one-site A2', not a consequence of the dimension facts. S' is displayed and not adopted. A3 is not identified with QCD, C^8 is not identified with generations, and Y is not identified with U(1)_Y."
upstream_dependencies:
  - minimal_axioms
runner: scripts/qubit_full_vs_composite_carrier_hypothetical_2026_08_13.py
---

# Qubit “Full” Versus Composite Carrier (Hypothetical)

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact complex dimensions of `M_2(C)`, `M_3(C)`, and `C^8`,
together with a displayed, not adopted, reading of the Qubit sentence.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/qubit_full_vs_composite_carrier_hypothetical_2026_08_13.py`](../scripts/qubit_full_vs_composite_carrier_hypothetical_2026_08_13.py)

## Result Up Front

This is a hypothetical discriminating test, not an axiom edit.

The current Qubit sentence names `M_2(C)` as the full one-site possibility
algebra. The integer facts `9>4` and `8>2` then say that `M_3(C)` does not
inject into that one-site algebra and that `C^8` is not the one-site Hilbert
space. Those facts survive under both the current sentence and a displayed
counterfactual that keeps the same one-site algebra while allowing a physical
object to be a declared finite composite of sites or a declared larger
carrier.

What does not survive is a particular *reading* of the current sentence:
that nothing physical may be larger than one-site `M_2(C)`. That reading,
not the dimension comparison, is what turns color/`P-HY` into a “must add
an axiom” wall. The counterfactual is displayed so the two readings can be
told apart. It is not adopted.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: negative_route_pruning
target_claim_id: qubit_full_vs_composite_carrier_hypothetical
target_blocker_text: "separate the 9>4 and 8>2 dimension facts from a reading of Qubit that nothing physical is larger than one-site M_2(C)"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
campaign_native_target_reachability: advances
conditional_surface_status: "exact integer dimensions and a displayed, not adopted, Qubit counterfactual; no axiom edit"
hypothetical_axiom_status: "C2 counterfactual: M_2 is the local possibility algebra; physical carriers may be composites; not adopted"
admitted_observation_status: null
claim_type_reason: "The complex dimensions of M_2(C), M_3(C), C^8, and one-site C^2 are counted from standard bases. Injectivity failure is the finite-dimensional comparison. Agreement of S and S' on dim A2 is textual. Adoption of S' remains open."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write

`A2 = M_2(C)`, `A3 = M_3(C)`, `H8 = C^8`.

The standard matrix units `{E_{ij}: 1 ≤ i,j ≤ n}` are a basis of `M_n(C)`
over `C`, so

`dim_C A2 = 2·2 = 4`, `dim_C A3 = 3·3 = 9`.

The standard basis of `C^n` has `n` vectors, so

`dim_C H8 = 8`.

The one-site Hilbert space for `A2` is `C^2`, with

`dim_C C^2 = 2`.

These four integers are counted here. They are not imported from another
block.

Current Qubit sentence **S**, quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

Counterfactual sentence **S′** (displayed, not adopted):

> The local possibility algebra at a site is `M_2(C)`; a physical object
> may be a declared finite composite of sites or a declared larger carrier.

Both sentences name `A2` as the local one-site presentation. Neither
sentence is rewritten in the axiom memo.

## Theorem 1 — `9>4` And `8>2`

Because `dim_C A3 = 9` and `dim_C A2 = 4`,

`9 > 4`.

A `C`-linear map `φ: A3 → A2` therefore cannot be injective: an injective
linear map of finite-dimensional vector spaces exists only when the source
dimension is at most the target dimension. Equivalently, any matrix of
`φ` in the standard bases is a `4 × 9` matrix, hence has rank at most `4`
and a kernel of dimension at least `5`.

Because `dim_C H8 = 8` and the one-site Hilbert space has dimension `2`,

`8 > 2`.

So `C^8` is not the one-site Hilbert space of `A2`.

The runner identity gates call `dim_m2()`, `dim_m3()`, and `dim_c8()`,
which count the standard bases rather than storing the integers `4`, `9`,
and `8` as bare constants.

This theorem is only a dimension comparison. It does not name a physical
color algebra, a generation space, or a hypercharge operator.

## Theorem 2 — `S` And `S′` Agree On The One-Site Algebra

Sentence `S` names `M_2(C)` as the algebraic presentation of the one-site
possibility domain. Sentence `S′` names `M_2(C)` as the local possibility
algebra at a site. Both therefore assign

`dim_C A2 = 4`

to the one-site algebra. A predicate “`S` and `S′` disagree about
`dim A2`” fails.

The integer facts of Theorem 1 are facts about `A2`, `A3`, and `C^8` as
vector spaces. They do not depend on which of `S` or `S′` is read as the
Qubit sentence. They survive under both.

## Theorem 3 — The Wall Is A Reading Of `S`, Not Of The Dimensions

Read `S` as “nothing physical is larger than one-site `A2`.” Under that
reading, `A3` and `C^8` are extras *to the axiom*: any object whose
carrier is nine-dimensional as an algebra or eight-dimensional as a
Hilbert space is forbidden unless a new axiom names it.

Read `S′`. The local algebra remains `A2`. The same objects are extras *to one site*.
They may be declared finite composites of sites or declared larger carriers. The dimension facts of Theorem 1 still say they are not
one-site `A2` and not one-site `C^2`. Those facts no longer say they are
outside the axiom.

The TOE wall “color/`P-HY` cannot exist unless we add an axiom” is a
reading of `S`, not of the dimension facts. Display `S′`. Do not adopt
it. This note does not rewrite the Qubit axiom.

## Theorem 4 — No QCD, No Generations, No `U(1)_Y`, No Forced Ray

This note does not identify `A3` with QCD. `M_3(C)` is a trial matrix
algebra used only for the dimension comparison.

This note does not identify `C^8` with generations, a taste cube, or a
three-factor tensor. `C^8` is a trial Hilbert space used only for the
comparison `8>2`.

This note does not identify `Y` with `U(1)_Y`. No hypercharge operator is
constructed.

This note does not import `0.5934`. No numerical residue, fit, or
prefactor from another lane is used.

This note does not force `r=1/2`. No Bloch radius, mixed-state ray, or
Born weight is selected.

This note does not claim that a later multi-site compiler cannot realize
a nine-dimensional algebra or an eight-dimensional carrier. It claims
only that such a realization is extra to one site, and that whether it is
extra to the axiom depends on the reading of the Qubit sentence.

## Mutation Predicates

The runner identity gates call `dim_m2()`, `dim_m3()`, and `dim_c8()`.

The predicate “`dim M_3 ≤ dim M_2`” is tested as
`dim_m3() ≤ dim_m2()` and must fail (`9 ≰ 4`).

The predicate “`S` and `S′` disagree about `dim A2`” is tested by
comparing the one-site dimension named by each sentence and must fail
(both say `4`).

## Claim Boundary

| Claim | Status in this note |
|---|---|
| `dim_C M_2(C)=4`, `dim_C M_3(C)=9`, `dim_C C^8=8`, one-site `dim_C C^2=2` | proved by counting standard bases |
| no injective `C`-linear map `A3 → A2` | proved from `9>4` |
| `C^8` is not the one-site Hilbert space | proved from `8>2` |
| `S` and `S′` agree that the one-site algebra is `A2` | textual; both name `M_2(C)` |
| Theorem 1 survives under both `S` and `S′` | same vector-space comparison |
| color/`P-HY` cannot exist unless an axiom is added | a reading of `S`, not a dimension theorem |
| `S′` is the new Qubit axiom | not adopted |
| `A3` is QCD | not claimed |
| `C^8` is a generation space | not claimed |
| `Y` is `U(1)_Y` | not claimed |
| `0.5934` or `r=1/2` is used or forced | not claimed |

## Imports And Claim Boundary

| Item | Role | Provenance | Open-bridge status |
|---|---|---|---|
| current Qubit sentence `S` | exact semantic baseline | current axiom memo | supplied; not rewritten |
| displayed sentence `S′` | C2 counterfactual | this note | displayed; not adopted |
| `A2`, `A3`, `H8`, one-site `C^2` | dimension witnesses | constructed here | not identified with SM objects |
| finite-dimensional injectivity | Theorem 1 | linear algebra | definition-level |
| color/`P-HY` as physical content | none | not imported | wall is a reading of `S` |
| QCD, generations, `U(1)_Y`, `0.5934`, `r=1/2` | none | not used | not applicable |

Independent audit remains required before the repository may assign any
effective claim status.
