# Two Conserved-Information Formalizations Non-Forcing No-Go Note

**Date:** 2026-07-12
**Status:** exact no-go proposal on the actual current surface; independent audit is required before any effective status change.
**Claim type:** no_go
**Claim boundary:** neither `CF-add` nor `CF-norm`, the two precise conserved-
information-flow semantics defined in §2, entails a single state-independent
linear unitary dynamics on its stated finite state space. Even after linear
Hilbert unitarity is supplied, it does not entail sparse/local generator
support. A conditional reconstruction theorem states the extra premises under
which self-adjoint generation and a support graph do follow.
**Status authority:** independent audit lane only.
**Runner:** `scripts/frontier_single_axiom_information_two_formalizations_nonforcing_2026_07_12.py`

## 1. Result

The quoted verbal sentence has no fixed mathematical semantics, so it is not
itself a premise from which a formal entailment can be proved. The two ordinary
precise semantics tested here do not close the requested positive derivation.
That scoped non-entailment can be closed negatively and exactly.

> **Two-formalization non-forcing theorem.** `CF-add` admits an additive-
> amount-preserving flow that is not unitary. `CF-norm` admits a reversible,
> cross-component, norm-preserving flow that is not a state-independent linear
> operator. Even after linear Hilbert dynamics and unitarity are supplied, a
> complete-support Hermitian family violates sparse locality. Without a
> supplied distinguished orthonormal carrier basis, generator support is not
> basis invariant. Thus neither tested formalization entails the sparse
> graph-unitary package.

The theorem is a non-entailment result on the two defined semantics, not a
claim that graph-unitary models are inconsistent and not an exhaustive theorem
about every possible meaning of the English sentence. Such models are
compatible with conserved information flow; they are not forced on the tested
surfaces.

The four old admitted inputs are not all equally primitive. Once a finite
complex Hilbert space, linear differentiable one-parameter dynamics, and norm
preservation for every state are supplied, self-adjoint generation and
exponentiation follow. The basis-to-edge definition and locality bound do not.

## 2. Minimal premise set and forbidden imports

The first-principles attempt uses the following minimal semantic content.

`CF-add` (additive reading):

1. there is a finite set `S` of distinguishable labels;
2. a state is a nonnegative vector `p` indexed by `S`;
3. the information amount is `I(p) = sum_i p_i`;
4. an autonomous flow preserves `I`.

`CF-norm` (stronger norm reading):

1. states are complex vectors;
2. the information amount is `I(psi) = ||psi||^2`;
3. an invertible continuous-time flow visibly transfers components and
   preserves `I`.

These are charitable formalizations, not new framework axioms. The verbal
sentence itself does not define “information,” a state space, addition,
complex scalars, an inner product, probabilities, linearity, reversibility, a
time parameter, or locality. A positive necessity claim must survive at least
the ordinary models admitted by these readings.

Forbidden as hidden proof inputs:

- a preselected Hilbert space or Born norm;
- linearity, superposition, or a one-parameter unitary group;
- a preselected Hamiltonian or transfer operator;
- “nonzero Hamiltonian entry = edge” as an unstated definition;
- sparsity, bounded degree, a metric, finite range, or a scaling family;
- an observed force law or a chosen gravity comparator.

No empirical value, fitted selector, unit convention, or literature theorem is
used in the no-go.

## 3. Exact countermodels

### 3.1 Additive conservation does not force unitarity

Take `S = {1,2}` and

```text
Q = [ -1   1 ] .
    [  1  -1 ]
```

For `t >= 0`, the flow `p(t) = T(t)p(0)` has

```text
T(t) = exp(tQ)
     = 1/2 [ 1+a  1-a ],    a = exp(-2t).
           [ 1-a  1+a ]
```

Every entry of `T(t)` is nonnegative and every column sums to one, so
nonnegative states remain nonnegative and

```text
I(T(t)p) = (1,1) T(t) p = (1,1) p = I(p).
```

But `T(t)` has eigenvalues `1` and `a`. For every `t > 0`, `0 < a < 1`.
Eigenvalue modulus is invariant under a change of basis, so `T(t)` cannot be
unitary in any positive-definite inner product. Equivalently, the difference
mode `(1,-1)` contracts by `a` while the total additive amount is exactly
conserved.

Thus `CF-add` does not imply unitary dynamics, Hermitian generation, or the
Schrödinger current formula. This is an exact two-state countermodel, not a
numerical comparison against a chosen dissipative factor.

### 3.2 Cross-component norm conservation does not force a linear unitary operator

On `C^2`, let `R(theta)` be the real two-component rotation matrix and define

```text
F_t(z) = R(t ||z||^2) z,
R(theta) = [ cos(theta)  -sin(theta) ].
           [ sin(theta)   cos(theta) ]
```

Rotation preserves the total norm, so `||F_t(z)|| = ||z||`. Because the norm
is unchanged, `F_t F_s = F_(t+s)` and `F_t^{-1} = F_{-t}`. For generic `z`
and `t`, both output components depend on both input components, so this is a
flow between the distinguishable components. The flow is continuous,
reversible, autonomous, and norm preserving.

It is not linear. For example, at any `t` with `R(4t)(1,0) != R(t)(1,0)`,

```text
F_t(2,0) = 2 R(4t)(1,0)
          != 2 R(t)(1,0) = 2 F_t(1,0).
```

Hence `CF-norm` does not yield a single state-independent linear unitary
operator on the stated state space. Linearity is an independent premise. The
example does not exclude state-dependent generators or linear dilations on an
enlarged state space; neither would establish the requested same-space
Hamiltonian derivation.

### 3.3 Unitarity does not force locality or sparsity

Now deliberately strengthen the surface to finite-dimensional Hilbert
dynamics. For every `N >= 2`, let

```text
H_N = J_N - I_N,
```

where `J_N` is the all-ones matrix. `H_N` is Hermitian, so
`U_N(t) = exp(-it H_N)` is unitary and preserves `||psi||^2` exactly. But
every off-diagonal entry of `H_N` is nonzero. The support graph is the complete
graph `K_N`, with `N(N-1)/2 = Theta(N^2)` edges and degree `N-1`.

This family satisfies the strengthened conservation/unitarity reading while
violating every bounded-degree or `O(N)`-support locality condition. Sparsity
is itself a statement about a family or an externally supplied tolerance; it
cannot follow from one finite conserved quantity without a scaling or metric
premise.

### 3.4 Generator support is not an intrinsic graph without a basis

Let `H_path` be the adjacency matrix of a finite path. In the site basis its
off-diagonal support is the path graph. In its orthonormal eigenbasis the same
operator is diagonal, so its off-diagonal support is empty. Unitary similarity
does not change the physical one-parameter group as an abstract operator, but
it changes the entrywise support.

Therefore “support of `H` = edges” becomes well-defined only after a
distinguished orthonormal carrier basis and a direct-coupling interpretation
are supplied. Bare distinguishable labels do not construct complex rays,
their inner product, or the identification of labels with an orthonormal
basis.

Even after such a basis is supplied, conservation does not select a topology:
path, cycle, complete, and empty-support Hermitian generators all conserve the
same norm. Defining the graph from whichever generator was chosen extracts a
graph; it does not derive the chosen generator or its locality.

## 4. Conditional reconstruction theorem

The strongest positive statement available is conditional and exact.

> **Finite-dimensional reconstruction theorem.** Let `V` be a finite
> complex Hilbert space. Let `U(t)` be a differentiable one-parameter group of
> linear maps with `U(0)=I`, and suppose `||U(t)psi||=||psi||` for every
> `psi` and every real `t`. Then there is a unique self-adjoint generator `H`
> such that `U(t)=exp(-itH)`. If a distinguished orthonormal basis
> `{|i> : i in S}` is additionally supplied and direct coupling is defined by
> `<i|H|j> != 0`, the off-diagonal support defines an undirected graph. That
> graph is sparse/local only if a separate support bound is supplied or
> derived.

**Proof.** Norm preservation plus the polarization identity gives inner-product
preservation, hence `U(t)^* U(t)=I`. Set `A = dU/dt|_(t=0)`. Differentiating
`U(t)^*U(t)=I` at zero gives `A^*+A=0`. Therefore `H=iA` is self-adjoint. The
group differential equation is `dU/dt = A U`, whose unique finite-dimensional
solution is `U(t)=exp(tA)=exp(-itH)`. In the supplied basis,
`H_ji = conjugate(H_ij)`, so nonzero off-diagonal support is symmetric and
defines an undirected graph. Nothing in the argument bounds the number or
range of nonzero entries; the complete-support family in §3.3 proves that no
such conclusion follows. QED.

This theorem retires the old “Hermitian-exponentiation readout” as an
independent convention only on the strengthened conditional surface. It does
not promote the verbal axiom: Hilbert geometry, linear group dynamics, the
carrier basis, the edge interpretation, and a locality bound remain supplied
structure.

## 5. Premise and import audit

| Item | Role | Current class | Load-bearing? | Disposition |
|---|---|---|---|---|
| finite labeled carrier | `CF-add` countermodel domain | explicit charitable formalization | yes, for that witness | weaker than the old admitted finite state set |
| additive conserved amount | `CF-add` meaning of conservation | explicit charitable formalization | yes, for that witness | exact countermodel shows insufficiency |
| complex norm | `CF-norm` strengthened meaning | explicit charitable formalization | yes, for that witness | exact nonlinear countermodel shows insufficiency |
| finite-dimensional linear algebra | proof infrastructure | standard mathematics | yes | no physical content imported |
| complex Hilbert space | conditional reconstruction | conditional premise | yes, positive theorem only | not derived from the verbal axiom |
| linear differentiable one-parameter group | conditional reconstruction | conditional premise | yes, positive theorem only | not derived from the verbal axiom |
| distinguished orthonormal carrier basis | support-graph extraction | conditional premise | yes, graph only | not derived from bare labels |
| support-as-direct-coupling rule | graph semantics | explicit definition | yes, graph only | extraction, not selection |
| finite-range/bounded-degree support | locality | open premise | yes, locality only | logically independent by dense family |
| current minimal framework axioms | framework context | approved axiom premise | no, theorem proof | already supply `Z^3` locality separately and explicitly state that no Hamiltonian is selected |

The no-go itself has no open dependency. A positive graph-unitary derivation
has the five open structural inputs listed in the lower half of the table.

## 6. Relation to the current framework

The current authority memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies the
`Z^3` nearest-neighbor lattice as the **Lattice** axiom. It also states that
**Admissibility is not dynamics** and does not choose a Hamiltonian, transfer
operator, probability weights, or kinetic branch. The framework therefore
already maintains the firewall exposed by the theorem: locality and dynamics
are separate supplied or downstream structures, not consequences of the
verbal conserved-flow sentence.

This note does not alter that memo, the audit ledger, the axiom-premise
registry, publication tables, or any repo-wide authority surface.

The prior meta note cited `MINIMAL_AXIOMS_2026-04-11.md` and then admitted sparse
Hermitian `H`. That presentation demonstrated compatibility after choosing the
target object. It did not test necessity. The countermodels above replace that
load-bearing substitution with a scoped proof by counterexample.

## 7. Runner certificate

[`frontier_single_axiom_information_two_formalizations_nonforcing_2026_07_12.py`](../scripts/frontier_single_axiom_information_two_formalizations_nonforcing_2026_07_12.py)
checks the exact witness formulas and the conditional reconstruction boundary:

1. the two-state Markov flow is positive and conserves additive amount while
   contracting a mode and failing unitarity;
2. the nonlinear reversible cross-component flow preserves norm and the group
   law while failing linearity;
3. the complete-support Hermitian family generates unitary dynamics with
   quadratic edge growth;
4. path-generator support changes under an eigenbasis transformation;
5. the conditional reconstruction identities hold on their stated supplied
   Hilbert surface.

The runner is a certificate for explicit finite witnesses. The theorem does
not depend on numerical tolerances: every decisive identity and inequality is
written analytically in §§3–4.

## 8. No-go discipline gate

**Author packet:** N1-N8 are complete for the theorem in §1; independent
no-go review remains required. The result is restricted to the two precise
semantics in §2. It does not rule out stronger axioms, other meanings of the
verbal sentence, or graph-unitary models.

### N1 — alternative-route enumeration

| Route | Honesty marker | Positive attack | Result and evidence |
|---|---|---|---|
| additive conserved flow | `ATTEMPTED` | derive a probability-preserving unitary from total conservation | exact Markov contraction preserves the total but is nonunitary; §3.1 and runner A01-A05 |
| norm plus reversible flow | `ATTEMPTED` | strengthen “information” to squared norm and require a reversible group | norm-dependent rotation transfers components and preserves norm but is nonlinear; §3.2 and runner B01-B04 |
| Hilbert linear group | `ATTEMPTED` | use norm preservation to derive `H=H*` | succeeds only after Hilbert geometry and linear differentiable group dynamics are supplied; §4 and runner E01-E03 |
| support reconstruction | `ATTEMPTED` | identify direct flow with nonzero generator entries | gives an undirected graph only after a carrier basis and extraction definition are supplied; §§3.4, 4 and runner D01-D02/E04-E05 |
| locality from unitarity | `ATTEMPTED` | derive sparse or finite-range support from a unitary group | exact `H_N=J_N-I_N` family is unitary with complete support; §3.3 and runner C04-C20 |
| transition-probability semantics | `ATTEMPTED` | define conservation as preservation of all projective transition probabilities | recovers the conditional Hilbert route only by supplying projective geometry, while the dense family still refutes locality; §§3.3, 4 and N7 |

### N2 — wall-independence audit

Let `W_G` be Hilbert state geometry, `W_L` linear differentiable group
dynamics, `W_B` a distinguished carrier basis, `W_E` support-as-physical-edge
semantics, and `W_R` a finite-range/bounded-degree locality rule.

| Pair | First closes second? | Second closes first? | Independent? | Witness |
|---|---|---|---|---|
| `W_G`, `W_L` | no | no | yes | §3.2 preserves a norm nonlinearly; bare linearity supplies no inner product |
| `W_G`, `W_B` | no | no | yes | Hilbert spaces have many bases; labels alone supply no inner product |
| `W_G`, `W_E` | no | no | yes | an inner product does not identify matrix support with physical adjacency |
| `W_G`, `W_R` | no | no | yes | §3.3 is Hilbert-unitary and dense; locality supplies no state geometry |
| `W_L`, `W_B` | no | no | yes | abstract linear groups have many bases; a basis supplies no time law |
| `W_L`, `W_E` | no | no | yes | linear dynamics does not interpret entries as edges; edge semantics supplies no dynamics |
| `W_L`, `W_R` | no | no | yes | §3.3 is linear-unitary and dense; a range bound supplies no group law |
| `W_B`, `W_E` | no | no | yes | a named basis does not make support physical; an abstract support rule does not select a basis |
| `W_B`, `W_R` | no | no | yes | a basis does not bound support; a range rule requires but does not construct carrier rays |
| `W_E`, `W_R` | no | no | yes | support extraction permits complete graphs; locality does not by itself define direct coupling |

No wall collapses into another. The positive chain's collapsed wall set is
`{W_G,W_L,W_B,W_E,W_R}`. The headline negative result needs only one
countermodel per claimed implication; the full witness family separates all
five positive inputs.

### N3 — hidden-wall scan

| Required trigger or close variant | Occurrence | Classification |
|---|---|---|
| “we assume” | absent | no hidden condition |
| “by construction” | countermodel definitions in §3 in substance | explicit witness definitions, not premises asserted of every model |
| “as is standard” / “standard QFT” | absent | none |
| “the framework provides” | §6 in substance | linked framework context; explicitly non-load-bearing |
| “bridge context” / “background” | absent | none |
| “naturally” / “obviously” | absent | none |
| “registered” | §6 and N6 | registry/governance firewall only; no primitive enters the proof |
| “canonical” | absent from proof | no uniqueness premise |
| “information” | §2 | split into two formal semantics; no exhaustive English meaning claimed |
| “flow” | §§3.1-3.2 | semigroup in `CF-add`; reversible cross-component group in `CF-norm` |
| “graph” | §§3.3-3.4 | support graph only under an explicit definition |
| “local” / “sparse” | §§3.3, 4 | family-level bounded-support property; never inferred from finite numerics |
| observations, fits, or target values | absent | none |

### N4 — residual matching

| Cited witness and locator | Witness residual | Residual used here | Match? |
|---|---|---|---|
| `docs/SINGLE_AXIOM_INFORMATION_NOTE.md:66-83` | derive sparsity, Hermiticity, locality, and Hamiltonian structure rather than define them into `H` | whether `CF-add`/`CF-norm` force linear unitary dynamics and whether unitarity forces locality | yes for the tested formalizations; no exhaustive English-semantics claim |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:106-119` | Admissibility chooses no Hamiltonian, transfer operator, or kinetic branch | positive dynamics-selection wall | yes as framework context; not proof of the self-contained countermodels |
| `docs/SINGLE_AXIOM_HILBERT_NOTE.md:82-96` | local tensor-product Hilbert structure is admitted rather than derived | state-geometry and carrier-basis wall | yes as non-retained context; not authority closure |

No nonmatching prior result is counted as proof of the headline theorem.

### N5 — rhetoric and resolution audit

| Resolution | Established | Not claimed |
|---|---|---|
| two-state additive model | exact conservation with a contracting mode | universal classification of information measures |
| two-component norm model | exact reversible nonlinear norm preservation | a physical quantum theory |
| finite `N` dense family | exact unitary complete support and `Theta(N^2)` edges | a metric or continuum limit |
| abstract operator | basis dependence of entrywise support | that a supplied physical site basis is illegitimate |
| conditional Hilbert surface | self-adjoint generator and symmetric support relation | derivation of Hilbert geometry, basis, edge semantics, or locality |

### N6 — partial-closure and premise scan

| Path | What it closes | What remains open |
|---|---|---|
| finite-dimensional reconstruction theorem (§4) | Hermiticity and exponential dynamics | origin of Hilbert geometry, linearity, and time-group structure |
| distinguished carrier basis plus support definition | an undirected support graph | physical adjacency meaning and topology selection |
| separate bounded-degree/finite-range premise | locality by assumption | derivation of that premise |
| current Lattice axiom | physical `Z^3` nearest-neighbor substrate | does not compress locality into conserved flow |
| current Admissibility axiom | local availability constraint | explicitly supplies no dynamics |
| separate negative claim identity (this note) | polarity-safe exact non-entailment | does not convert the existing meta note or satisfy its positive consumers |
| scale-reference primitive | units conversion only | no state geometry, dynamics, carrier basis, edge semantics, or locality |
| kinetic-isotropy primitive | `c_t=c_s` structural isotropy only | no dynamics, graph, or finite-range selector |
| realized-state primitive | evaluation at a supplied state only | no state selection, dynamics, or graph |

The primitive registry and premise-decision history contain no convention or
approved primitive that retires the five-wall set. A future approved primitive
could supply a wall, but that would be an explicit supplied premise rather
than a derivation from `CF-add` or `CF-norm`.

### N7 — strongest steelman

> A hostile reviewer should interpret “information” not as one conserved
> scalar but as the complete transition-probability geometry of pure states.
> A bijection preserving all transition probabilities is unitary or
> antiunitary up to phase; continuous time selects the unitary component, and
> the infinitesimal generator then supplies `H`. “Things” should be read as a
> distinguished orthonormal carrier basis and “flows between” as nonzero
> infinitesimal matrix elements, so the graph follows too.

The strongest repo context for this route is
`docs/SINGLE_AXIOM_HILBERT_NOTE.md:82-96`, which names the local Hilbert
surface but records it as admitted rather than derived; the current Qubit
axiom supplies only the one-site `M_2(C)` presentation. The projective
transition-preservation theorem is standard mathematical context, not a
load-bearing imported closure here.

This steelman recovers the conditional theorem, not the scoped entailment.
It adds projective Hilbert states, transition probabilities, bijectivity,
continuity, a carrier basis, and the direct-coupling definition. Moreover the
dense family in §3.3 satisfies the resulting unitarity while refuting
locality. The steelman therefore identifies a possible stronger axiom packet;
it does not invalidate either countermodel on the stated scope.

### N8 — cross-cycle echo

| Prior/current surface and locator | Retirement mechanism tested | Could it close this result? |
|---|---|---|
| `docs/STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md:36-39` | separate negative claim identity preserves dependency polarity | yes for packaging only; adopted here, but it supplies none of `W_G`-`W_R` |
| previous `docs/SINGLE_AXIOM_INFORMATION_NOTE.md:97-120` | admit sparse Hermitian `H`, then extract graph and unitary | no; this is the substitution the audit rejected |
| `docs/SINGLE_AXIOM_HILBERT_NOTE.md:82-96` | admit local tensor-product Hilbert structure and Born readout | partial supplied route; it does not derive those structures or locality from the tested semantics |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:34-64,106-119` | approve Lattice/Qubit/Admissibility/Record explicitly | supplies lattice locality separately and explicitly leaves dynamics downstream; it does not compress the axioms into conserved flow |
| `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md:20-44` | owner-approved primitive retires a units-only wall | no; the mechanism could supply a new premise but cannot turn supply into derivation |
| `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md:62-75` | owner-approved primitive supplies structural kinetic isotropy | no; its boundary explicitly excludes dynamics and a locality selector |
| conditional reconstruction theorem (§4) | derive Hermiticity from a linear Hilbert norm-preserving group | partial; does not derive Hilbert geometry, basis, edge semantics, or locality |

The repo-wide analogous-wall scan found premise approval, convention
separation, and conditional reconstruction as the live retirement mechanisms.
All are represented above. None makes the two scoped entailments true.

## 9. Exact remaining blocker for any positive reformulation

A positive theorem beyond the two tested semantics would need a new formal
axiom or retained bridge whose own content
specifies, or independently derives:

1. a complex projective/Hilbert state geometry and its information measure;
2. linear reversible continuous-time composition;
3. a distinguished carrier basis and direct-coupling semantics;
4. a metric, finite-range rule, bounded-degree law, or other locality selector.

Items 1–3 give the conditional reconstruction chain. Item 4 is not a
consequence of them. Folding all four into the meaning of “conserved
information flow” would again be definitional compression, not a derivation.

The exact next scientific route, if a positive compression remains desired,
is to propose and independently justify a formal local information axiom that
excludes both the Markov/nonlinear witnesses and the dense Hermitian family
without naming unitary Hamiltonian locality in equivalent words.
