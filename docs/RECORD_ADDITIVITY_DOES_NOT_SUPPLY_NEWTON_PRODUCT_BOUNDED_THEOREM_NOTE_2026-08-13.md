---
claim_id: record_additivity_does_not_supply_newton_product_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "Conditional on a separately supplied finite-additive scalar functional I with I(empty)=0, the pooled value I(S disjoint-union T) does not in general identify I(S)I(T): the free count model realizes (2,0), (1,1), and (0,2) at the same pooled value with different products. Separate evaluation of I on an ordered source/test pair does canonically define the product by ordinary scalar multiplication, so no abstract pairing is missing. The physical Newton residual is instead the source/test typing, mass-readout identification, and test-body response law. Current Record supplies none of the finite-additive scalar premise."
upstream_dependencies:
  - minimal_axioms
  - newton_law_derived_note
runner: scripts/record_additivity_does_not_supply_newton_product_2026_08_13.py
---

# Pooled Finite-Additive Readout Does Not Identify A Two-Body Product

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact conditional algebra for a separately supplied finite-additive
scalar functional, plus the boundary to the current Record axiom and the
Newton potential-kernel packet.
**Primary runner:**
[`scripts/record_additivity_does_not_supply_newton_product_2026_08_13.py`](../scripts/record_additivity_does_not_supply_newton_product_2026_08_13.py)
**Runner cache:**
[`logs/runner-cache/record_additivity_does_not_supply_newton_product_2026_08_13.txt`](../logs/runner-cache/record_additivity_does_not_supply_newton_product_2026_08_13.txt)

## Result Up Front

The current Record axiom does **not** contain a named scalar collection
functional `I`, finite additivity, or `I(empty)=0`. The current authority
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) instead says
that only records are readable, a readout value is determined by record
content alone, and a site with no record cannot be read. Therefore every
result below is conditional on a separately supplied mathematical input:

> **Finite-additive scalar hypothesis.** On a supplied class of finite record
> collections, `I` is scalar-valued, `I(empty)=0`, and
> `I(A disjoint-union B)=I(A)+I(B)` for disjoint `A,B`.

Under this hypothesis, the pooled statistic

`sigma := I(S disjoint-union T)=I(S)+I(T)`

does not in general determine the product `I(S)I(T)`. In the free count model,
the ordered pairs `(2,0)`, `(1,1)`, and `(0,2)` all have `sigma=2`, while
their products are `0,1,0`. Thus no single-valued `f(sigma)` equals the
product on all three pairs.

That narrow result does **not** mean the functional `I` lacks a product on
separately accessible inputs. Given an ordered pair `(S,T)`, ordinary scalar
multiplication canonically defines

`B_I(S,T):=I(S)I(T)`.

Finite additivity makes `B_I` separately additive in each collection
argument. No new abstract bilinear pairing rule is needed. What remains open
for Newton physics is the bridge that identifies separately accessible record
content as source mass and test mass, supplies their physical source/test
roles, and derives the response rule `F=-M_test grad(phi)`.

The Newton packet
[`NEWTON_LAW_DERIVED_NOTE.md`](NEWTON_LAW_DERIVED_NOTE.md) supplies only the
source-linear potential-kernel algebra. It already lists both the test-body
response rule and the physical two-mass product law as non-claims. This note
does not close either one and does not say gravity is impossible.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The free finite-additive count model proves exact pooled-statistic non-identifiability, while separate evaluation canonically supplies the scalar product. The finite-additive functional and every physical source/test bridge remain explicit conditions."
trace_class: negative_route_pruning
target_claim_id: newton_law_derived_note
target_blocker_text: "derive a physical test-body response and the two-mass product law from framework content"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Derive source/test typing, mass-readout identification, and the test-body response law; do not seek the scalar product in a pooled union value."
conditional_surface_status: "exact in the supplied finite-additive free-count model; no current-Record or physical Newton closure"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Conditional Objects

Let `C` be the free commutative monoid of finite labeled atoms. Supply a
scalar-valued functional `I:C -> Q` satisfying

`I(empty)=0`,

`I(A disjoint-union B)=I(A)+I(B)` for disjoint `A,B`.

This is a conditional mathematical structure, not current Record content.
The count model `I(A)=|A|` realizes the hypothesis. Weighted rational atoms
give a second model in which `I` is the sum of atom weights.

For an ordered disjoint pair `(S,T)`, write

`m_s=I(S)`, `m_t=I(T)`, and `sigma=I(S disjoint-union T)`.

The **pooled interface** exposes only `sigma`. The **separate interface**
exposes the ordered pair `(I(S),I(T))`. Keeping these interfaces distinct is
load-bearing.

## Theorem 1 — Pooled Non-Identifiability

In the count model, choose disjoint collections realizing

| `(m_s,m_t)` | `sigma=m_s+m_t` | `m_s m_t` |
|---|---:|---:|
| `(2,0)` | `2` | `0` |
| `(1,1)` | `2` | `1` |
| `(0,2)` | `2` | `0` |

Suppose one function `f:Q->Q` recovered the product from the pooled value on
all three pairs. The first pair would require `f(2)=0`, while the second would
require `f(2)=1`, a contradiction. Therefore no such `f` exists on this
model and domain.

More generally, if a finite-additive model contains two ordered pairs with
the same sum and different products, its pooled statistic cannot identify the
product. Finite additivity alone does not exclude such models, so it does not
entail a universal pooled recovery rule.

The domain qualifier matters. On a restricted diagonal `m_s=m_t`, the
product is `(sigma/2)^2`; if `m_t` is externally fixed, it is
`m_t(sigma-m_t)`. Those are additional restrictions, not counterexamples to
the stated free-model theorem.

## Theorem 2 — Separate Evaluation Already Supplies The Scalar Product

At the separate interface define

`B_I(S,T)=I(S)I(T)`.

This uses only the supplied functional twice and ordinary multiplication in
its scalar codomain. If `S_1,S_2,T` are pairwise disjoint, then

`B_I(S_1 disjoint-union S_2,T)`

`=(I(S_1)+I(S_2))I(T)`

`=B_I(S_1,T)+B_I(S_2,T)`.

The same calculation holds in the second argument. Hence `B_I` is separately
additive. It returns `0,1,0` on the three pairs above.

This corrects the submitted broad reading. A second abstract pairing is not
the algebraic residual. The separately accessible ordered pair is additional
interface structure relative to the pooled value, but once it exists the
scalar product follows canonically.

## Theorem 3 — The Newton Kernel Is Source-Linear Only

The cited Newton packet gives, for `r>0`,

`G(r)=1/(4 pi r)`,

`phi(r)=m_s G(r)`,

`|grad phi|=m_s/(4 pi r^2)`.

The displayed gradient contains no `m_t`. Composing it with the separate
test-body response rule

`F=-m_t grad(phi)`

would give the two-mass product, but that response rule is exactly a non-claim
of the Newton packet. The scalar multiplication needed after the response
rule is elementary; the physical response rule and the interpretation of the
two scalars as masses are not.

## Proof-Obligation Boundary

| Obligation | Disposition |
|---|---|
| current Record excludes finite-additive `I` and a value at absence | source-bound boundary |
| explicit finite-additive scalar functional | separately supplied condition |
| free count model and three-pair collision | proved here |
| arbitrary pooled post-processing cannot resolve the collision | proved here |
| separate evaluation gives `I(S)I(T)` | proved here |
| source/test typing of record content | open physical bridge |
| identification of the two scalar readouts with physical masses | open physical bridge |
| test-body response `F=-M_test grad(phi)` | open Newton bridge |
| full Newton force law or gravity closure | not claimed |

The proof boundary is **CONDITIONAL**: the exact algebra closes under the
stated finite-additive input, while the target-equivalent physical response
and interpretation remain open.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current Record wording | exclusion boundary | approved `minimal_axioms`; supplies no `I` |
| finite-additive scalar `I`, `I(empty)=0` | mathematical input | separately supplied; no current retained supplier asserted |
| free count/weighted-atom models | countermodels | constructed here |
| Newton kernel and source-linear potential | parent algebra | bounded parent, not promoted here |
| source/test record typing | physical input | open |
| mass/readout identification | physical input | open |
| test-body response rule | physical input | open |
| observational data | input | none |

## Boundary And Non-Claims

- The note does not restore finite additivity or `I(empty)=0` to Record.
- It assigns no readout value to a site with no record.
- It does not identify record collections with physical masses.
- It does not claim that finite additivity prevents a product at the separate
  interface; Theorem 2 proves the opposite.
- It does not derive the test-body response rule or a Newton force law.
- It does not exhaust restricted domains, extra statistics, dynamics, or
  two-body actions.
- It does not edit an axiom or install a framework primitive.

## Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | It isolates why a pooled additive statistic cannot by itself encode the two-body product used downstream of a test-body response. |
| V2 | New content? | The durable content is the explicit interface split: pooled non-identifiability versus canonical product from separate evaluation. |
| V3 | Independently checkable? | Yes. The count model, collision, separate-additivity identities, and Green derivative are exact. |
| V4 | More than a restatement? | Yes. The Newton packet names a non-claim; this theorem distinguishes an irrelevant pooled route from the real physical response residual. |
| V5 | One-step relabel? | No. The review correction changes the proof-obligation graph by removing the false claim that an abstract pairing is missing. |

## No-Go Discipline Gate

The only negative shipped is: on the stated free finite-additive model, no
function of the pooled scalar alone recovers the two-body product on all three
rejector pairs. No global non-derivability or gravity no-go is claimed.

### N1 — Materially distinct routes

| Route | Attempt and outcome | Marker |
|---|---|---|
| Arbitrary pooled post-processing | Let `f` be completely arbitrary; the common input `2` would need outputs `0` and `1`, so the collision survives | **ATTEMPTED** |
| Polynomial/nonlinear pooled map | Identity, constant, quadratic, rational, or discontinuous choices remain single-valued at `2`; functional complexity cannot split one input | **ATTEMPTED** |
| Restrict the domain | On `m_s=m_t` or externally fixed `m_t`, the product is a function of `sigma`; this evades the theorem by adding a domain condition | **ATTEMPTED** |
| Evaluate `I` separately | The ordered pair `(I(S),I(T))` gives the product immediately; this defeats the submitted broad claim and is incorporated as Theorem 2 | **ATTEMPTED** |
| Add a second pooled statistic | Supplying `delta=m_s-m_t` gives `m_s m_t=(sigma^2-delta^2)/4`; the added statistic is outside the one-scalar interface | **ATTEMPTED** |
| Compose source and test-response linearities | A derived response `F=-m_t grad(phi)` yields the product without pooled recovery; this is the live Newton route, not ruled out | **ATTEMPTED** |

### N2 — Wall independence

For physical use, the collapsed open set is:

- `W1`: a scalar mass/readout functional, including its finite-additive form
  if that form is intended;
- `W2`: physical source/test typing with separate accessibility;
- `W3`: the test-body response law.

| Pair | First closes second? | Second closes first? | Independent? |
|---|---:|---:|---:|
| `W1/W2` | no | no | yes |
| `W1/W3` | no | no | yes |
| `W2/W3` | no | no | yes |

There is no fourth “abstract pairing” wall: `W1+W2` and scalar
multiplication already define the numerical product.

### N3 — Hidden-condition scan

| Phrase/object | Classification |
|---|---|
| finite-additive `I` and `I(empty)=0` | explicit separately supplied condition |
| free count model | explicit constructed countermodel |
| range values `0,1,2` | realized in that model, not claimed for every `I` |
| ordered source/test pair | explicit extra interface structure |
| ordinary scalar multiplication | textbook codomain operation, not a physical bridge |
| Newton kernel | cited bounded parent algebra |
| physical mass interpretation/response | explicit open walls |

### N4 — Residual matching

| Witness | Witness residual | Current residual | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:140-149` | finite additivity, named `I`, and `I(empty)=0` are absent from current Record | classify the scalar premise as conditional | yes |
| `docs/NEWTON_LAW_DERIVED_NOTE.md:90-99` | test-body response and two-mass product are non-claims | identify the live physical residual after pooled-route pruning | yes |

No earlier product-law companion is used as a no-go witness.

### N5 — Rhetoric audit

- per-element: atom weights and scalar values are evaluated in the explicit free model;
- per-site: no assertion is made that one site supplies a collection functional or mass;
- per-mode: no spectral or Fourier decomposition is used or excluded by the theorem;
- per-block: pooled versus separately accessible two-collection interfaces are distinguished exactly;
- lattice-wide: no lattice dynamics, two-body response, or gravity closure is claimed or tested.

### N6 — Partial-closure path

`docs/G_NEWTON_WEAK_FIELD_RESPONSE_BOUNDED_CLOSURE_NOTE_2026-05-10_gnewtonG3.md`
is currently unaudited and conditionally studies a test-body response after a
canonical coupling is supplied. `docs/EMERGENT_PRODUCT_LAW_NOTE.md` is also
currently unaudited and exhibits a product on a supplied cross-field Poisson
model through source and test-response linearities. Either shape confirms
that the residual is a bridge/response problem, not a demand for a new axiom
or abstract scalar pairing. Neither is imported as authority here.

### N7 — Hostile steelman

> An additive functional is not merely its value on the union. It can be
> evaluated on `S` and `T` separately, after which ordinary multiplication
> gives `I(S)I(T)`. Moreover, the standard Newton mechanism composes source
> linearity with test-body response linearity. The proposed “missing pairing”
> is artificial and cannot support a Newton obstruction.

**Answer.** Correct against the submitted broad framing. That framing is
removed. The surviving theorem concerns only non-identifiability from the
pooled scalar and explicitly preserves separate evaluation and response-law
composition as live closure paths.

### N8 — Cross-cycle echo

The older `docs/AXIOM_REDUCTION_NOTE.md` (meta) and
`docs/EMERGENT_PRODUCT_LAW_NOTE.md` (currently unaudited bounded theorem)
describe the same two-linearity escape: source response supplies one mass
factor and test-body response supplies the other. That analogous wall was
handled by an explicit conditional model rather than by a pooled additive
readout. The same mechanism remains applicable here, so no broad no-go or
new-axiom requirement is shipped.

**No-Go Discipline status: PASS** for the narrowed pooled-interface claim.

## Primary Runner

The runner verifies the current Record exclusion boundary, constructs the
finite-additive free and weighted models, checks pooled collisions and
restricted-domain escapes, derives separate additivity of `B_I`, differentiates
the source-linear Newton kernel, and emits the five-resolution execution
certificate required for later independent audit.
