---
claim_id: admissibility_support_constrains_content_not_formation_site_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "For the supplied finite conditional content law mu(A)=1/3, mu(B)=2/3, mu(C)=0, support is exactly {A,B}, so a formed record governed by this law cannot lock C. On a separate abstract two-label carrier, the same mu has well-typed nonempty formation extensions supported at x, at y, or at both labels. The projection from these extensions to the content law is therefore non-injective in site set and formation multiplicity. This is a finite type-separation witness, not a full Z^3 history, a derivation of mu, a formation process, or a rate theorem. Absence is only an external no-record tag and receives no readout value."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_support_constrains_content_not_formation_site_2026_08_13.py
---

# Admissibility Support Constrains Locked Content, Not a Formation Extension

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact support of one supplied finite conditional content law and
the fiber of finite formation extensions over that law.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/admissibility_support_constrains_content_not_formation_site_2026_08_13.py`](../scripts/admissibility_support_constrains_content_not_formation_site_2026_08_13.py)

## Result up front

The current Admissibility and Record authority
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) distinguishes
two kinds of data:

- a probability distribution over local possibilities, conditional on
  formation at a site and determined by nearest-neighbor conditions; and
- the fact that records form, without a supplied formation site,
  formation probability, process, or rate.

This note gives that type boundary one exact finite witness. For the supplied
finite law

```text
mu(A)=1/3,  mu(B)=2/3,  mu(C)=0,
```

the support is `{A,B}`. Conditional on formation governed by this law, `C`
cannot be locked. But the same `mu` is the projection of distinct well-typed
extensions whose formed-label sets are `{x}`, `{y}`, and `{x,y}`.

The conclusion is deliberately limited. The finite labels `x,y` do not form
an induced physical fragment of `Z^3`, and the note does not assert that either
has only one nearest neighbor. Equal content laws at the labels are supplied
toy data, not derived from lattice covariance. The static multiplicities one
and two are not rates. No time, transition law, or full lattice history is
constructed.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite support and three explicit formation-extension witnesses are exact; the content law, physical site selector, full lattice consistency, process, clock, and rate remain unsupplied."
trace_class: negative_route_pruning
target_claim_id: record_formation_site_and_multiplicity_rule
target_blocker_text: "derive a physical formation-site/process/rate rule rather than infer it from a conditional content distribution"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "supply or derive a full-lattice formation kernel with its law domain, site selector, transition semantics, and clock before making a rate claim"
conditional_surface_status: "exact only for the supplied finite content law and abstract two-label formation-extension type; no full Z^3 or rate closure"
hypothetical_axiom_status: no edit
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premise boundary

The current axiom memo supplies the sentences:

```text
For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

Records form.

When present, a record locks exactly one admissible local possibility.
```

It also says that a site with no record cannot be read. The present theorem
uses no finite-additive scalar functional, no scalar value at absence, and no
readout of the absence tag.

The exact masses below are supplied for the finite witness. They are not
derived from a nearest-neighbor configuration or from the axiom memo. The
finite menu is likewise a declared test object; it does not replace the full
one-site possibility domain `M_2(C)`.

## Exact objects and obligation graph

Let

```text
X = {A,B,C},
F = {x,y},
mu = {A -> 1/3, B -> 2/3, C -> 0}.
```

For this atomic finite law, define

```text
supp(mu) = {a in X : mu(a)>0}.
```

A **finite formation extension over `mu`** is a pair `(S,ell)` where

- `S` is a nonempty subset of the abstract label set `F`; and
- `ell:S->supp(mu)` assigns one locked content to each formed label.

The projection `pi_mu(S,ell)=mu` forgets the site set and locks and remembers
only the conditional content law. This is a deliberately typed finite
construction, not the definition of a framework state.

| obligation | exact disposition |
|---|---|
| normalize the supplied finite law | `1/3+2/3+0=1` |
| compute its support | `{A,B}` |
| reject a formed lock of `C` | `C` is outside support |
| exhibit two site-distinct extensions over the same law | `E_x`, `E_y` below |
| exhibit two multiplicity-distinct extensions over the same law | `E_x`, `E_xy` below |
| derive either extension as the physical realized history | open and not claimed |
| construct time or a rate | outside the object type and not claimed |

## Theorem 1 — support constrains formed content

The masses are nonnegative and sum to one. Direct evaluation gives

```text
supp(mu)={A,B}.
```

Therefore any finite formation extension over `mu` may lock `A` or `B`, but
cannot lock `C`. The exclusion is conditional on this supplied law and on a
record being formed. A mutation that gives `C` positive mass puts `C` into
the support and defeats the exclusion, as the runner verifies.

This theorem says nothing about whether, where, or when formation occurs.

## Theorem 2 — the content-law projection is not site-injective

Define

```text
E_x := ({x}, {x -> A}),
E_y := ({y}, {y -> A}).
```

Both are well-typed extensions: their site sets are nonempty and every lock
lies in `{A,B}`. They are distinct because `{x}!={y}`, while

```text
pi_mu(E_x)=mu=pi_mu(E_y).
```

Thus the projection from finite formation extensions to the conditional
content law is non-injective in the formed-label set. This does not say that
no selector could ever be defined. It says that a selector is additional
data not encoded by the displayed probability vector itself.

No lattice claim is hidden here. In `Z^3` every site has six nearest
neighbors. The submitted draft's two-vertex “unique-neighbor star” was not a
valid induced model of that lattice and is not used.

## Theorem 3 — the content-law projection is not multiplicity-injective

Define a third extension

```text
E_xy := ({x,y}, {x -> A, y -> B}).
```

It is well typed and has multiplicity two, while `E_x` has multiplicity one.
Nevertheless

```text
pi_mu(E_x)=mu=pi_mu(E_xy).
```

The content-law projection is therefore non-injective in static formation
multiplicity. Multiplicity is a cardinality, not a rate. A rate would require
a transition or counting process plus a time parameter or clock, none of
which is defined here or supplied by `mu`.

The complete finite fiber has eight extensions. There are two singleton site
sets and two allowed locks on each, giving `2*2=4`; the two-site set has
`2^2=4` lock assignments. Hence the exact census is

```text
|Ext(mu)|=4+4=8,
site sets={{x},{y},{x,y}},
multiplicities={1,2}.
```

The paired runner enumerates this fiber independently of the three displayed
witnesses.

## Post-Record-reset absence boundary

For tabular display one may write “no record at `y`” when describing `E_x`.
That phrase is an external domain tag: `y` is not in the extension's formed
set. It is not a record content, is never passed to a readout map, and is not
assigned a scalar. In particular, this note does not reconstruct the removed
finite-additive `I` or a value at the empty collection.

The only occurrence analogue internal to the toy type is the definition
`S!=empty`. It lets the finite witnesses focus on site and multiplicity after
occurrence. It is not a proof that an arbitrary two-site region of a physical
history must contain a record.

## No-Go Discipline

The negative result is only projection non-injectivity for the displayed
finite data. It is not a universal no-go against formation-site or rate
theorems.

### N1 — materially distinct route scan

| route | marker | outcome relative to the narrow target |
|---|---|---|
| read site choice directly from the vector `(1/3,2/3,0)` | **ATTEMPTED** | `E_x` and `E_y` have the same vector and different formed-label sets |
| read multiplicity directly from that vector | **ATTEMPTED** | `E_x` and `E_xy` have the same vector and multiplicities one and two |
| use support as a formation-site probability | **ATTEMPTED** | support is a subset of content labels, not a probability on `F` |
| use translation/cubic covariance as a realized-site selector | **ATTEMPTED** | covariance constrains a supplied rule; it does not choose a representative without additional condition/rule data |
| use site-dependent nearest-neighbor conditions | **ATTEMPTED** | a derived formation functional of those conditions is a live route, but it is additional to the held-fixed `mu` vector |
| use a Hamiltonian, stochastic kernel, or record-production dynamics | **ATTEMPTED** | these are live partial-closure routes and are outside the finite projection theorem |
| use a clocked counting process | **ATTEMPTED** | this can define a rate once supplied or derived; static extension cardinality alone cannot |

### N2 — wall independence

One type wall is claimed: forgetting `(S,ell)` loses site and multiplicity
information. Content exclusion by support is a separate positive-support
calculation, not a second impossibility wall. No inflated wall count is used.

### N3 — hidden-wall scan

The finite menu, masses, label set, and extensions are all declared. No
full-lattice embedding, equal physical neighbor shells, formation dynamics,
time, scalar absence value, iid assumption, realized-state selector, or Born
frequency law is imported.

### N4 — residual matching

The current axiom memo's residual is a physical formation rule—site,
probability, process, and rate—not content support. Older formation-boundary
notes in the repository identify the same residual, but their pre-reset scalar
wording is not consumed here. The present witness neither closes nor enlarges
that residual.

### N5 — certificate granularity

```text
per-element: executed — support and every displayed lock are checked
per-site: executed — the two abstract labels x and y are enumerated
per-mode: not applicable — no modal or spectral decomposition is used
per-block: executed — only the declared two-label extension fiber is checked
lattice-wide: not executed — no Z^3 history or formation process is claimed
```

### N6 — partial-closure paths

A full-lattice formation kernel could depend on the actual nearest-neighbor
condition, a derived dynamics, a supplied stochastic law, or another physical
selector. A time-bearing process could then define a rate. Every such route
remains live and need not alter the axioms if derived from separately supported
structure.

### N7 — steelman

The strongest objection is that the complete nearest-neighbor rule, not one
held-fixed output vector, may encode where formation occurs. Correct: the
finite witness cannot exclude that. It proves only that the conditional
content vector by itself does not uniquely encode the extension.

### N8 — cross-cycle echo

Earlier formation work already separates occurrence from the formation rule.
The August 13 Record reset further removes any scalar/additive shortcut through
absence. This note agrees with both boundaries and contributes only the exact
finite projection witness.

## Boundaries and explicit non-claims

- The theorem is conditional on the supplied finite law; it does not derive
  the values `1/3`, `2/3`, or `0`.
- The labels `x,y` are not asserted to be an isolated subgraph of `Z^3`.
- Distinct extension cardinalities do not constitute distinct rates.
- The result does not classify all extensions or all lawful histories.
- It supplies no site selector, formation probability, process, time, or
  physical rate.
- Absence is unread and receives no scalar value.
- No axiom, primitive, registry, or audit verdict is edited.

## Verification

Run:

```bash
python3 scripts/admissibility_support_constrains_content_not_formation_site_2026_08_13.py
```

The runner uses exact rational arithmetic, constructs all three extensions,
checks mutation controls, pins the current post-reset Record boundary, and
verifies the N1–N8 packet. Expected summary:

```text
TOTAL: PASS>=35 FAIL=0
```
